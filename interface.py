import os


def interface():
    input_dic = 'NULL'
    output_dic = 'NULL'
    choose = ''
    while True:
        print('欢迎：')
        print('    1. 更改待测试文件文件夹，当前:' + input_dic)
        print('    2. 更改输出文件夹，当前:' + output_dic)
        print('    3. 运行测试')
        choose = input()
        if choose == '1':
            input_dic = input_input_dic()
        elif choose == '2':
            output_dic = input_output_dic()
        elif choose == '3':
            run_test()
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


def run_test():
    pass


