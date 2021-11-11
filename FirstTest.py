import os
import random


class Dog:
    '''这是一个狗类'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗被命令下蹲'''
        print(self.name + "is now sitting.")

    def roll_over(self):
        '''模拟小狗被命令打滚'''
        print(self.name + "rolled over!")

    import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(files)  # 当前路径下所有非目录子文件
    print(len(files))


def main():
    for i in range(1, 100, 1):
        print(random.choice(range(2)))


if __name__ == '__main__':
    main()
