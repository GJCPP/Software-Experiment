import os
import random
import re


def run(source_dic, output_path, testcases):
    dic_list = os.listdir(source_dic)
    differ_set = set()
    same_set = set()
    testfile = 'test.input'
    output_diff_file = output_path + '/inequal.csv'
    output_same_file = output_path + '/equal.csv'
    for dirname in dic_list:
        namepath = source_dic[source_dic.rfind('/')+1:] + '/' + dirname + '/'
        os.chdir(source_dic + '/' + dirname)
        input_format = get_input_format()
        allfile = os.listdir()
        allcpp = [s for s in allfile if s[-4:] == '.cpp']
        allexe = []
        for name in allcpp:
            compile_cpp(name, exe_name(name))
            allexe.append(exe_name(name))
        for _ in range(testcases):
            generate_test(input_format, testfile)
            runtime_err = dict()
            for name in allcpp:
                runtime_err[name] = os.system('./' + exe_name(name) + ' < ' + testfile + ' > ' + output_name(name))
            for first in allcpp:
                if runtime_err[first] != 0:
                    continue
                for second in allcpp:
                    if runtime_err[second] != 0 or (namepath + first, namepath + second) in differ_set:
                        continue
                    if first != second and not compare(output_name(first), output_name(second)):
                        differ_set.add((namepath + first, namepath + second))
        for first in allcpp:
            for second in allcpp:
                if (namepath + first, namepath + second) not in differ_set:
                    same_set.add((namepath + first, namepath + second))
        for name in allcpp:
            os.remove(output_name(name))
            os.remove(exe_name(name))
        os.remove(testfile)
    output_res(output_diff_file, differ_set, output_same_file, same_set)


def output_res(differ_file, differ_set, same_file, same_set):
    out = []
    for item in differ_set:
        out.append(item[0] + ', ' + item[1] + '\n')
    out.sort()
    differ_file = open(differ_file, 'w+')
    differ_file.write('file1, file2\n')
    for item in out:
        differ_file.write(item)
    differ_file.close()

    out = []
    for item in same_set:
        out.append(item[0] + ', ' + item[1] + '\n')
    out.sort()
    same_file = open(same_file, 'w+')
    same_file.write('file1, file2\n')
    for item in out:
        same_file.write(item)
    same_file.close()


def generate_test(input_format, testfile_name):
    s = ''
    for ask in input_format:
        if ask[0] == 'int':
            s += str(random.randint(ask[1], ask[2])) + ' '
        else:
            cnt = 1 if ask[0] == 'char' else random.randint(ask[1], ask[2])
            for i in range(cnt):
                c = random.randint(0, 51)
                if c < 26:
                    c = chr(ord('a') + c)
                else:
                    c = chr(ord('A') + c - 26)
                s += c
            s += ' '
    file = open(testfile_name, 'w+')
    file.write(s)
    file.close()


def output_name(cpp_file_name):
    return cpp_file_name + '.output'


def exe_name(cpp_file_name):
    return cpp_file_name + '.out'


def get_input_format():
    file = open('stdin_format.txt')
    file_str = ''.join([s for s in file.readlines()])
    ret = re.findall(r'(int|string|char)(?:\((.*?),(.*?)\))?', file_str)
    for i in range(len(ret)):
        if ret[i][1] != '':
            ret[i] = (ret[i][0], int(ret[i][1]), int(ret[i][2]))
    return ret


def compile_cpp(cpp_file, exe_file):
    os.system('g++ ' + cpp_file + ' -o ' + exe_file)


def compare(file1, file2):
    file1 = open(file1, 'r')
    file2 = open(file2, 'r')
    s1 = '.'.join([s for s in file1.readlines()])
    s2 = '.'.join([s for s in file2.readlines()])
    s1 = s1.split()
    s2 = s2.split()
    for item in s1:
        if item in s2:
            s2.remove(item)
        else:
            if len(s2) == 0:
                return True
            return False
    return True
