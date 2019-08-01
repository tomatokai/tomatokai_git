#!/usr/bin/env python
# config: utf-8

import os
import shutil
import pymongo

#用來獲取文件名
class easyGet():
	#參數為：文件夾路經，文件格式
	def get_file_name(file_path,file_format,word_bin,word_end):
		L = []
		for root,dirs,files in os.walk(file_path):
			if os.path.splitext(file)[1] == file_format:#控制讀取格式
				L.append(os.path.join(root,file))
		list_new = []
		for i in L:
			i = i[word_bin:word_end]
			list_new.append(i)
		return list_new
