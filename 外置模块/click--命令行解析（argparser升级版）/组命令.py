# -*- coding: utf-8 -*-
##group
##
##使用 group 可以把多个函数组合成子命令；
##
##有两种方式：
##
##A:
##
##通过@click.group()装饰器定义一个函数 A，最后通过 
##A.add_command(hello)把别的函数加入到group函数中去。
##注意 `hello` 是脚本中定义的一个命令行函数
##
##
##B:
##通过@click.group()装饰器定义一个函数 B，在定义一般命令行函数的时候，用
##@B.command()来替代@click.command()装饰命令行函数hello
##

## python script
import click


@click.group()
def gpfun():
    pass

@click.command()
@click.option('--name', prompt='enter your name here: ', help='greet to given name')
def hello(name):
    click.echo('Hello World! hello %s' % name)

gpfun.add_command(hello)

if __name__ == '__main__':
    gpfun()

# 文件名后面可以加hello来调用hello函数
 
