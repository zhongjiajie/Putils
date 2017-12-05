#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np


def rm_arr_col(col_idx):
    """
    删除numpy中指定的col_idx
    :param col_idx: 要删除的col_idx
    :return:
    """

    def _decorator(func):
        def _rm_arr_col(*args, **kwargs):
            a = args[0]
            args = args[1:]

            keep_idx = range(a.shape[1])
            keep_idx.remove(col_idx)

            return func(a[:, keep_idx], *args, **kwargs)

        return _rm_arr_col

    return _decorator


def fix_arr_col(col_idx):
    """
    固定numpy数组中指定col_idx的列不参加运算
    :param col_idx: 需要固定的列
    :return:
    """

    def _decorator(func):
        def _fix_arr_col(*args, **kwargs):
            a = args[0]
            args = args[1:]

            keep_idx = range(a.shape[1])
            keep_idx.remove(col_idx)

            fix_a = a[:, col_idx].reshape(len(a), 1)
            tmp_a = func(a[:, keep_idx], *args, **kwargs)

            post_a = np.concatenate((fix_a, tmp_a), axis=1)

            return post_a

        return _fix_arr_col

    return _decorator
