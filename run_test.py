import os
import random
import re


def run(source_dic, output_path):
    dic_list = os.listdir(source_dic)
    for dirname in dic_list:
        namepath = source_dic[source_dic.rfind('\\')+1:] + '\\' + dirname + '\\'
        os.chdir(source_dic + '\\' + dirname)
        allfile = os.listdir()
        allcpp = [s for s in allfile if s[-4] == '.cpp']
        print(get_input_format())


def get_input_format():
    file = open('stdin_format.txt')
    file_str = ''.join([s for s in file.readlines()])
    return re.findall(r'(int|char|string)\((.*?),(.*?)\)', file_str)


def compile(cpp_file, exe_file):
    os.system('g++ ' + cpp_file + ' -o ' + exe_file)