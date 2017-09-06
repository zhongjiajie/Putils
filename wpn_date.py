#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
时间相关

Class:
* UnpackRangeDate : 将给的时间段转成时期范围

Function:
* is_valid_date : 验证是否符合给定的时间格式
* is_outdate : 判断日期是否过期
"""

import datetime


class UnpackRangeDate(object):
    """
    将指定类型的时间区间的值转换成相应的明细时间
    """

    def __init__(self, start_date, end_date,
                 from_date_format="%Y%m%d", to_date_format="%Y%m%d"):
        self.start_date = start_date
        self.end_date = end_date
        self.from_date_format = from_date_format
        self.to_date_format = to_date_format

    def unpack2list(self):
        start_date = datetime.datetime.strptime(self.start_date, self.from_date_format)
        end_date = datetime.datetime.strptime(self.end_date, self.from_date_format)

        date_list = []

        while start_date <= end_date:
            date_str = start_date.strftime(self.to_date_format)
            date_list.append(date_str)
            start_date += datetime.timedelta(days=1)

        return date_list

    def unpack2yield(self):
        start_date = datetime.datetime.strptime(self.start_date, self.from_date_format)
        end_date = datetime.datetime.strptime(self.end_date, self.from_date_format)

        while start_date <= end_date:
            date_str = start_date.strftime(self.to_date_format)
            yield date_str

            start_date += datetime.timedelta(days=1)


def is_valid_date(date_str, date_format="%Y%m%d"):
    """
    验证date_str是否指定时间格式的时间
    :param date_str: 验证的时间值
    :param date_format: 验证的时间格式
    :return:
    """
    if isinstance(date_str, str):
        return True if datetime.datetime.strptime(date_str, date_format) else False
    if isinstance(date_str, int):
        return True if datetime.datetime.strptime(str(date_str), date_format) else False


def is_outdate(start_day, keep_day, check_day=None):
    """
    判断日期是否过期 过期返回True 没有过期返回False
    :param start_day: 开始计算日期的天数
    :param keep_day: 保留的天数
    :param check_day: 要校验的日期
    :return: True or False
    """
    if not check_day:
        check_day = datetime.datetime.now()
    if isinstance(start_day, datetime.datetime) and isinstance(check_day, datetime.datetime):
        delta = start_day - check_day
        return delta.days >= keep_day
