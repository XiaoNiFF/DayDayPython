import calendar as calx
import time as tm


def show_time():
    tm.strftime(tm.localtime(tm.time()))

if __name__ == "__main__":
    pr_cal(2020,3)