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



class RandomSequence(object):
	
	varStrRemoveRepeatL = []
	varStrRemoveRepeatL.append('ahoo')
	
	def __init__(self):
		self.author = 'ahoo'
		pass
	
	
	#随机一个长度2-5的字符串,一般用作变量名	
	def randStr_az(
			self,
			minNum=2,
			maxNum=5):			#判断一下大小传反了的情况
		
		randstr = ''
		if minNum > maxNum:
			minNum = min(minNum,maxNum)
			maxNum = max(minNum,maxNum)
		strLengt = random.randint(minNum,maxNum)
		for i in range(1,strLengt,1):
			chrTem = chr(random.randint(97,122))
			randstr = randstr + chrTem
		return randstr
		
	
	
	def randStr_AZUp(self,minNum=2,maxNum=5):
		randstr = ''
		if minNum > maxNum:
			minNum = min(minNum,maxNum)
			maxNum = max(minNum,maxNum)
		strLengt = random.randint(minNum,maxNum)
		for i in range(1,strLengt,1):
			chrTem = chr(random.randint(65,92))
			randstr = randstr + chrTem
		return randstr
	
	
	#从正常的代码列表中随机一句,当废话用,混淆效果更好.
	'''吧代码生成一个pprint py库在这调用,下版.'''
	JsCodeList = [
		'new Function("a", "b", "return a+b;");',
		'var ybdetof5 = new ActiveXObject("Scripting.FileSystemObject");'
		]
	def randCodeLine(self,CodeList = []):
		if len(CodeList) == 0:
			CodeList.append('Life is short,U need the Eng')
		return random.choice(CodeList)
	
	
	#随机字符:'m'
	def randChr(self):
		return random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
	
	
	#随机字符list:['n','f','y','b']
	def randChrEx_List(self):
		return random.sample('zyxwvutsrqponmlkjihgfedcba', 5)
	
	
	#随机生成一个List:['nihao','ahoo','a']
	def randStrList(self,minNum=3,maxNum = 5):
		if minNum > maxNum:
			minNum = min(minNum,maxNum)
			maxNum = max(minNum,maxNum)
		
		arrLengt= random.randint(minNum,maxNum)
		arrList =[]
		for i in range(0,arrLengt,1):
			arrList.append(self.randStr_az())
		return arrList
	
	
	#生成数组模式1:['xu', 'm', 'l', 'ahoo', 'milh'][3]
	def randStrArrary(self,itemstr):
		arrList 	= self.randStrList()
		index 		= random.randint(0,len(arrList)-1)
		arrList[index] = itemstr
		return str(arrList) + '[' + str(index) + ']'
	
	
	#生成数组模式2: ('var ab = "ahoo"', "['df', ab, 'puu', 'chx', 'avu'][1]")
	def randStrArryEx_var(self,itemstr):
		arrList 	= self.randStrList()
		index 		= random.randint(0,len(arrList)-1)
		
		#随机一个varName,确保不要重复.
		varName = self.randStr_az(3,7)
		while varName in self.varStrRemoveRepeatL:
			varName = self.randStr_az(4,8)
		varStrItem = 'var '+ varName + ' = "' + itemstr + '"\n'
		self.varStrRemoveRepeatL.append(varName)
		
		#生成数组
		arrList[index] = varName
		replaceTemp = str(arrList) + '[' + str(index) + ']'
		
		#替换为变量形式.
		replaceTemp_pattern = re.compile('\''+varName+'\'')
		replaceTemp = replaceTemp_pattern.sub(varName,replaceTemp)
		
		return varStrItem , replaceTemp
	
	
	#生成数组模式3: 将一句话(自定义特殊格式)分割为数组加变量: 
	#'open#@process' ---> {'var ax = "open"' : '['nihao',ax,'a'][1]',,}
	def randSelfTypeStr2ArraryTypeStr(self,SelfTypeStr):
		replacestr = ''
		varStrList = []
		for i_list_split_line in SelfTypeStr.split('#@'):
			varStr,arrStr = self.randStrArryEx_var(i_list_split_line)
			replacestr = replacestr + arrStr + ' + '
			varStrList.append(varStr)
		return varStrList,replacestr[:-3]
	
	
	#随机一个function vbs的
	def randFun_Vb(self):
		return 'waitfortest\r\n coming~\r\n'
		pass
	
	
	def randFunList_Vb(self,MaxLen):
		funList=[]
		for i in range(0,MaxLen,1):
			funList.append(self.randFun_Vb())
		return funList