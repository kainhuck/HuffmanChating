#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : KainHuck

class HfNode():
    '''赫夫曼数结点类'''
    def __init__(self, left=None, right=None, weight=None, parent=None, star=False, code=None):
        self.left = left    # 左子树
        self.right = right   # 右子树
        self.weight = weight    # 权值
        self.parent = parent    # 双亲结点
        self.star = star    # 区分普通结点
        self.code = code    # 编码

def find_code(node, store_list):
    '''查找数的对应编码'''
    if node.star != 'head':
        # print(node.code)
        store_list.append(node.code)
        find_code(node.parent, store_list)

def Test1_Create_HfTree():
    '''第一个测试题'''
    init_list = [5, 29, 7, 8, 14, 23, 3, 11]  # 给定的频率列表

    # 构建赫夫曼树结点
    HfNode_list = []    # 存放赫夫曼树结点的列表
    for each in init_list:
        temp_node = HfNode(weight=each, star=True)
        HfNode_list.append(temp_node)

    # 对赫夫曼结点列表排序
    order_list = sorted(HfNode_list, key=lambda node: node.weight)

    # 连接结点
    while len(order_list) > 1:
        left = order_list.pop(0)    # 弹出第一个结点
        right = order_list.pop(0)   # 弹出第二个结点
        if left.star:
            new_node = HfNode(left, right, left.weight + right.weight)  # 生成新的结点
            left.parent = new_node
            left.code = '0'
            right.parent = new_node
            right.code = '1'
        else:
            new_node = HfNode(right, left, left.weight + right.weight)  # 生成新的结点
            left.parent = new_node
            left.code = '1'
            right.parent = new_node
            right.code = '0'

        order_list.append(new_node) # 将新的结点加入列表
        order_list = sorted(order_list, key=lambda node: node.weight)   # 再次排序

    # 循环之后列表中只剩一个头结点
    head_node = order_list[0]
    head_node.star = 'head' # 标记头结点

    code_dict = {}  # 存放编码的字典
    for each in HfNode_list:
        store_list = []
        print(each.weight, end=' ')
        find_code(each, store_list)
        store_list.reverse()
        print(store_list)
        code_dict[each.weight] = store_list

    with open('password.txt', 'w') as f:
        for each in code_dict:
            f.write(str(each))
            f.write(' : ')
            for elem in code_dict[each]:
                f.write(str(elem))
                f.write(' ')
            f.write('\n')

def Main_HfTree():
    '''测试题二的英文字符编码'''
    character_list = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                      'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # 字符列表
    num_list = [186, 64, 13, 22, 32, 103, 21, 15, 47, 57, 1, 5,
                32, 20, 57, 63, 15, 1, 48, 51, 80, 23, 8, 18, 1,
                16, 1]   # 对应频率的列表

    init_list = zip(character_list, num_list)

    # 构建赫夫曼树结点
    HfNode_list = []  # 存放赫夫曼树结点的列表
    for each in init_list:
        temp_node = HfNode(weight=each, star=True)
        HfNode_list.append(temp_node)

    # 对赫夫曼结点列表排序
    order_list = sorted(HfNode_list, key=lambda node: node.weight[1])

    # 连接结点
    while len(order_list) > 1:
        left = order_list.pop(0)  # 弹出第一个结点
        right = order_list.pop(0)  # 弹出第二个结点
        if left.star:
            temp_weight = (None, left.weight[1] + right.weight[1])
            new_node = HfNode(left, right, temp_weight)  # 生成新的结点
            left.parent = new_node
            left.code = '0'
            right.parent = new_node
            right.code = '1'
        else:
            temp_weight = (None, left.weight[1] + right.weight[1])
            new_node = HfNode(right, left, temp_weight)  # 生成新的结点
            left.parent = new_node
            left.code = '1'
            right.parent = new_node
            right.code = '0'

        order_list.append(new_node)  # 将新的结点加入列表
        order_list = sorted(order_list, key=lambda node: node.weight[1])  # 再次排序

    # 循环之后列表中只剩一个头结点
    head_node = order_list[0]
    head_node.star = 'head'  # 标记头结点

    code_dict = {}  # 存放编码的字典
    for each in HfNode_list:
        store_list = []
        find_code(each, store_list)
        store_list.reverse()
        code_dict[each.weight[0]] = store_list

    # 写入密码本
    with open('password_plus.txt', 'w') as f:
        for each in code_dict:
            f.write(str(each))
            f.write(' : ')
            for elem in code_dict[each]:
                f.write(str(elem))
                f.write(' ')
            f.write('\n')

    return (code_dict,head_node)    # 返回密码字典和头结点

def write_tofile():
    '''输入字符串,并写入文件'''
    string = input("请输入通讯语句:")
    with open('hfmTree.txt', 'w') as f:
        f.write(string)

    return string

def decode(code, root, head, text_list):
    '''解码过程'''
    if root.star and root.star != 'head':           # 找到一个标记结点
        print(root.weight[0], end='')   # 输出字符
        text_list.append(root.weight[0])
        root = head         # 重置根节点为头结点
        decode(code, root, head, text_list)
    else:                   # 未找到标记结点
        if len(code) == 0:
            return  # 解码结束,退出递归
        single_code = code.pop(0)
        if single_code == '0':
            decode(code, root.left, head, text_list)   # 向左找
        else:
            decode(code, root.right, head, text_list) # 向右找

if __name__ == '__main__':
    # Test1_Create_HfTree()
    code_dict_head = Main_HfTree()
    string = list(write_tofile())  # 将字符串转换成列表
    encode_string = [code_dict_head[0][str(each)] for each in string]  # 加密之后的列表
    # 将编码存进文件
    with open('CodeFile.txt', 'w') as f:
        for each in encode_string:
            for i in each:
                f.write(i)

    with open('CodeFile.txt', 'r') as f:
        code_string = f.readlines()[0]

    text_list = []  # 存放译文的列表
    print('编码后:', code_string)
    print("解密:",end=' ')
    decode(list(code_string), code_dict_head[1], code_dict_head[1], text_list)
    # print(text_list)
    # 将译文写入文件
    with open('Textfile.txt', 'w') as f:
        for each in text_list:
            f.write(each)

