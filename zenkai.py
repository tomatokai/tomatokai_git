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

#用於把數據存入mongodb
class easyLink():
	#用於檢查pymongo是否已經連上mongodb
	def mongotest(host_t,port_t,db_n_t,db_collection_t):
		client = pymongo.MongoClient(host_t,port_t)
		db = client[db_n_t]
		db_col = db[db_collection_t]
		return db_col.find_one()	

	#字典存入mongodb中
	def dictToMongo_all(host,port,db_n,db_collection,dict_data):
		client = pymongo.MongoClient(host,port)
		db = client[db_n]
		db_col = db[db_collection]
		data = dict_data
		for j in data:
			db_col.insert_one(j)
		print('导入数据',db_col)

class easyFile():
	#移动文件
	def move_file(f_from,f_to)
		for i in f_from:
			shutil.move(i,f_to)
			print(i,'移动到',f_to)
