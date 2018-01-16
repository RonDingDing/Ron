# -*- coding: utf-8 -*-
 

import click

@click.command()
def hello():
    click.echo('Hello World!')

if __name__ == '__main__':
    hello()

 

# 只能命令行运行！！
