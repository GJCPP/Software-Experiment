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
        print('    1. 更改待测试文件文件夹，当前:' + input_dic)
        print('    2. 更改输出文件夹，当前:' + output_dic)
        print('    3. 更改随机生成测试样例数，当前:' + str(testcases))
        print('    4. 运行测试')
        choose = input()
        if choose == '1':
            input_dic = input_input_dic()
        elif choose == '2':
            output_dic = input_output_dic()
        elif choose == '3':
            testcases = input_testcase()
        elif choose == '4':
            start_test(input_dic, output_dic, testcases)
        else:
            print('指令无效！请重新输入。')


def input_input_dic():
    os.system('cls')
    ret = ''
    while True:
        print('请输入待测试文件文件夹:')
        ret = input()
        if os.path.exists(ret):
            break
        print('未能找到文件夹:' + ret)
        print('请重新输入！')
    return ret


def input_output_dic():
    os.system('cls')
    ret = ''
    while True:
        print('请输入用来输出测试结果的文件夹:')
        ret = input()
        if os.path.exists(ret):
            break
        print('未能找到文件夹:' + ret)
        print('请重新输入！')
    return ret


def input_testcase():
    os.system('cls')
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
    return ret


def start_test(source_dic, output_path, testcases):
    run_test.run(source_dic, output_path, testcases)


