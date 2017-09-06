#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
文件相关

Class:


Function :
* create_not_exists : 创建文件夹
* delete_exists : 删除文件或文件夹
* delete_outdate_file : 删除过期文件或文件夹
* zip_file_folder : 压缩文件或文件夹
"""

import datetime
import os
import shutil
import zipfile

from wpn_date import is_outdate


def create_not_exists(path):
    """
    确保文件夹存在 如果不存在新建一个空文件夹
    :param path: 文件夹路径
    :return: 
    """
    if not os.path.exists(path):
        os.makedirs(path)


def delete_exists(path):
    """
    确保文件夹不存在 存在的话删除该文件夹
    :param path: 文件夹路径
    :return: 
    """
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


def delete_outdate_file(path, keep_day, end_date, file_type):
    """
    删除过期的文件或文件夹 时间以文件的创建日期为准
    :param path: 文件或者文件夹的路径
    :param keep_day: 文件保存的时间
    :param end_date: 日期截止时间
    :param file_type: 文件类型 支持*表示全部
    :return: 
    """
    if os.path.isdir(path):
        # 遍历文件夹 判断创建时间是否过期 然后删除
        for dirpath, _, filenames in os.walk(path):

            # 过滤要删除的文件类型
            if file_type != "*":
                filenames = filter(lambda x: x.endswith(file_type), filenames)

            for filename in filenames:
                file_path = os.path.join(dirpath, filename)

                file_crt_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                if is_outdate(file_crt_date, keep_day, end_date):
                    delete_exists(file_path)

    elif os.path.isfile(path):
        # 删除创建日期过期文件
        file_crt_date = datetime.datetime.fromtimestamp(os.path.getctime(path))
        if is_outdate(file_crt_date, keep_day, end_date):
            delete_exists(path)


def zip_file_folder(from_path, to_path, file_name):
    """
    压缩文件或文件夹 将src_path压缩成tgt_path/file_name形式
    :param from_path: 要压缩的文件夹或文件路径
    :param to_path: 目标文件夹路径
    :param file_name: 目标文件名
    :return: 
    """
    with zipfile.ZipFile(os.path.join(to_path, file_name), 'w', zipfile.ZIP_DEFLATED) as zip_obj:
        if os.path.isdir(from_path):
            for dirpath, _, filenames in os.walk(from_path):
                for filename in filenames:
                    zip_obj.write(os.path.join(dirpath, filename), filename)
        elif os.path.isfile(from_path):
            zip_obj.write(from_path, os.path.basename(from_path))
