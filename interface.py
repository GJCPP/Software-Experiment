import os
import run_test


def interface():
    input_dic = './input'
    output_dic = './output'
    testcases = 10
    while True:
        if not os.path.isabs(input_dic):
            input_dic = os.path.abspath(input_dic)
        if not os.path.isabs(output_dic):
            output_dic = os.path.abspath(output_dic)
        print('欢迎：')
        print('    1. 更改待测试文件目录，当前:' + input_dic)
        print('    2. 更改输出目录，当前:' + output_dic)
        print('    3. 更改随机生成测试样例数，当前:' + str(testcases))
        print('    4. 运行测试')
        print('    5. 结束程序')
        choose = input()
        if choose == '1':
            input_dic = input_input_dic()
        elif choose == '2':
            output_dic = input_output_dic()
        elif choose == '3':
            testcases = input_testcase()
        elif choose == '4':
            start_test(input_dic, output_dic, testcases)
        elif choose == '5':
            return
        else:
            print('指令无效！请重新输入。')


def input_input_dic():
    os.system('clear')
    ret = ''
    while True:
        print('请输入待测试文件目录:')
        ret = input()
        if os.path.exists(ret):
            break
        print('未能找到文件夹:' + ret)
        print('请重新输入！')
    os.system('clear')
    return ret


def input_output_dic():
    os.system('clear')
    ret = ''
    while True:
        print('请输入用来输出测试结果的目录:')
        ret = input()
        if os.path.exists(ret):
            break
        print('未能找到文件夹:' + ret)
        print('请重新输入！')
    os.system('clear')
    return ret


def input_testcase():
    os.system('clear')
    ret = ''
    while True:
        print('请输入随机生成的测试样例数:')
        ret = input()
        try:
            ret = int(ret)
        except:
            print('请输入一个整数！')
            continue
        if ret <= 0:
            print('请输入一个正整数！')
            continue
        break
    os.system('clear')
    return ret


def start_test(source_dic, output_path, testcases):
    os.system('clear')
    if not os.path.exists(source_dic):
        print('待测试文件目录无效！请选择1并输入一个有效的文件夹。')
        return
    if not os.path.exists(output_path):
        print('输出文件目录无效！请选择2并输入一个有效的文件夹。')
        return
    os.system('clear')
    same, diff = run_test.run(source_dic, output_path, testcases)
    os.system('clear')
    print(f'测试结束，共判定出 {same} 对等价源程序， {diff} 对不等价源程序。')
    print(f'详情请见 {output_path} 下输出的两个csv文件。')


