#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ahoo'

import sys
import io
import os
import codecs
import re
import shutil
import random
import logging
import logging.config

#--------------------文件配置----------
logfilePath = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig('logging.conf')
logging.getLogger()


#sys.stdout = io.TextIOWrapper(
#				sys.stdout.buffer,
#				encoding='utf-8') #改变标准输出的默认编码


PutPath = '24_analysis.txt'				#JsVirus文件(卡饭精睿包2016.12.16.24).
OutPath = '24_EngRefactorObfuscate.vir'	#提取到的文件.

class StrSplitEng(object):

	def __init__(self):
		self.author = 'ahoo'
		pass
		
	#分割line返回list:'Scripting.FileSystemObject'-->['Sc', 'ri', 'pt', 'ing', '.Fil', 'eSys', 'temO', 'bj', 'ect']
	def StrSplitLine2List(self,strForSplit):
		result = []
		strleng = len(strForSplit)
		if len(strForSplit) == 0:
			pass
		elif strleng <= 4:
			result.append(strForSplit)
		else:
			randlen = random.randint(2,4)
			result.append(strForSplit[:randlen])
			tempList = self.StrSplitLine2List(strForSplit[randlen:])
			
			for j in tempList:
				result.append(j)
		return result
	
	
	#分割一个line中的元素返回以'#@'分割的字符串.
	# 'Scripting.FileSystemObject'-->Scri#@pti#@ng.F#@ileS#@yst#@em#@Ob#@ject
	def StrSplitLine2SelfTypeStr(self,strForSplit1):
		resultStr = ''
		tempList = self.StrSplitLine2List(strForSplit1)
		if len(tempList) == 0:
			return resultStr	
		else:
			for i in tempList:
				resultStr  = resultStr + i + '#@'
		
		return resultStr[:-2]
		
	
	#分割一个list中的元素返回list.	
	def StrSplit(self,strForSplit = []):
		strSplitList = []
		result = []
		if len(strForSplit) == 0:
			#print(strForSplit)
			return result

		for i in strForSplit:
			strleng = len(i)
			if strleng <= 4:
				result.append(i)
			else:
				#randlen = random.randint(2,int(strleng/2))
				randlen = random.randint(2,4)
				#print(randlen)
				#print(i[:randlen])
				#print(i[randlen:])
				strSplitList.append(i[:randlen])
				strSplitList.append(i[randlen:])
				#print(strSplitList)
				tempList = StrSplit(strSplitList)
				
				for j in tempList:
					result.append(j)
		#print('result\n')
		#print(result)
		return result