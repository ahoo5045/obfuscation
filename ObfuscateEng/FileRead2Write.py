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


sys.stdout = io.TextIOWrapper(
				sys.stdout.buffer,
				encoding='utf-8') #改变标准输出的默认编码

class FileRead2Write(object):
	
	def __init__(self):
		self.AuthorSign = True
		
	def ReadInputFile(
			self,
			InPath,
			ReadTye = 'r'):
		
		logall = []
		
		#这个判断应该放到参数类里. if not os.path.isfile(InPath):
		fpR = codecs.open(InPath,ReadTye,'utf-8')
		for line in fpR:
			if None == line:
				pass
			else:
				logall.append(line)
		fpR.close()
		return logall

	def WriteOutputFile(self,OutPath,OutList= [],WriteTye = 'a+'):	#后面可能改成词典
		fpW = codecs.open(OutPath,WriteTye,'utf-8')
		if self.AuthorSign == True:
			fpW.write('\n*****************************************************\r\n')
			fpW.write('*		 		ahoo EngObfuscate 					    ')
			fpW.write('\n***************************************************\r\n\n')
			self.AuthorSign = False
		for i in OutList:
			fpW.write(i)
		fpW.close()
		return True
		
	def WriteOutputFileEx_ListShuffle(self,OutPath,OutList= [],WriteTye = 'a+'):	#后面可能改成词典
		fpW = codecs.open(OutPath,WriteTye,'utf-8')
		if self.AuthorSign == True:
			fpW.write('\n*****************************************************\r\n')
			fpW.write('*		 		ahoo EngObfuscate 					    ')
			fpW.write('\n***************************************************\r\n\n')
			self.AuthorSign = False
		if len(OutList)	== 0:
			fpW.write('\n')
			return True
		random.shuffle(OutList)
		for i in OutList:
			fpW.write(i)
		fpW.close()
		return True
		
	def WriteOutputFileEx_LineStr(self,OutPath,LineStr,WriteTye = 'a+'):
		fpW = codecs.open(OutPath,WriteTye,'utf-8')
		if self.AuthorSign == True:
			fpW.write('\n***************************************************\n')
			fpW.write('*		 		ahoo EngObfuscate 					    ')
			fpW.write('\n***************************************************\n\n')
			self.AuthorSign = False
		fpW.write('\n' + LineStr + '\n')
		fpW.close()
		return True
		
	def OpenOutPath(self,OutPath,program = '"D:\\Program Files (x86)\\Notepad++\\notepad++.exe" '):
		return os.system(program + OutPath) 		# program = 'notepad.exe' 
	
	#将list写入另一个中.
	def WriteList2List(self,list1 = [],list2 = []):
		if len(list1) == 0:
			pass
		else:
			for i in list1:
				list2.append(i)
			
		return True
		
	'''	1.list排序
		ransomFamilyList = list(set(ransomFamilyList))
		2.list最后一行去掉\n
		ransomFamilyList[-1] = ransomFamilyList[-1].strip('\n')
		3.去空格.
		ransomFamilyList.append(i.strip(' ') + '\n')	
		
		4.遍历目录
		for parent,dirnames,filenames in os.walk(InputDir):
			for filename in filenames:
				fpRan.ReadInputFile(os.path.join(parent, filename)) 
		
		5.for循环 #a =1
		#[i for i in range(0,10,1)	a = a+i ]
	'''