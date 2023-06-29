#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ret_res = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            ret_res += 1
        except IndexError:
            break
    print("")
    return ret_res
