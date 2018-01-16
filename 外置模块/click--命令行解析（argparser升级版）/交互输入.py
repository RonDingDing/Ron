# -*- coding: utf-8 -*-
import click

@click.command()
@click.option('--name', prompt='enter your name here: ',
            help='greet to given name')
def hello(name):
    click.echo('Hello World! hello %s' % name)

if __name__ == '__main__':
    hello()


# prompt可以把命令变成交互输入
