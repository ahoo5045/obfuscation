#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
	v1.0 --发布.
'''
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
from Obfuscateer.FileRead2Write import FileRead2Write 
from Obfuscateer.RandomSequence import RandomSequence
from Obfuscateer.StrSplitEng 	import StrSplitEng

#--------------------文件配置----------
logfilePath = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig('logging.conf')
logging.getLogger()


#sys.stdout = io.TextIOWrapper(
#				sys.stdout.buffer,
#				encoding='utf-8') #改变标准输出的默认编码


class ObfuscateMethod(object):
	
	rdClass = RandomSequence()
	spClass = StrSplitEng()
	
	def __init__(self):
		self.author = 'ahoo'
		
		
	#1.替换""之间的.	
	def ObfuscateQuotes(self,InputList=[]):
		writeListTemp = []
		varStrTemp = []
		if len(InputList) == 0:
			return varStrTemp,writeListTemp
		
		for lin1 in InputList:
			if lin1 == "":
				#writeListTemp.append(lin1)
				pass
			else:
				for m in re.findall('"\s*[^"\,\+]+\s*"',lin1):
					if len(m) >= 2:
						pattern_quotes = re.compile(m[1:-1])
						strtemp = self.spClass.StrSplitLine2SelfTypeStr(m[1:-1])
						varlsit,replaceTempstr =  self.rdClass.randSelfTypeStr2ArraryTypeStr(strtemp)
						#print(replaceTempstr1)
						lin1 = pattern_quotes.sub(replaceTempstr,lin1,count=1)
						#print(lin1)
						for varItem in varlsit:
							varStrTemp.append(varItem)
					else:
						lin1 = m
				writeListTemp.append(lin1)
				pass
		
		return varStrTemp,writeListTemp
	
	#2.替换[]和()之间的.
	def OufuscateBracket(self,InputList1=[]):
		writeListTemp1 = []
		varStrTemp1 = []
		
		if len(InputList1) == 0:
			return varStrTemp1,writeListTemp1
			
		for line in InputList1:
			if line == "":
				#writeListTemp1.append(line)
				pass
			else:
				for i in re.findall('\[(\s*"[^\[\]\(\)]+"\s*)\]',line):
					pattern_bracket = re.compile(i)
					strtemp = self.spClass.StrSplitLine2SelfTypeStr(i)
					varlsit,replaceTempstr = self.rdClass.randSelfTypeStr2ArraryTypeStr(strtemp)
					line = pattern_bracket.sub(replaceTempstr,line,count=1)
					for varItem in varlsit:
							varStrTemp1.append(varItem)
				
				for j in re.findall('\((\s*"[^\[\]\(\)]+"\s*)\)',line):
					pattern_bracket = re.compile(j)
					strtemp = self.spClass.StrSplitLine2SelfTypeStr(j)
					varlsit,replaceTempstr = self.rdClass.randSelfTypeStr2ArraryTypeStr(strtemp)
					line = pattern_bracket.sub(replaceTempstr,line,count=1)
					for varItem in varlsit:
							varStrTemp1.append(varItem)
				writeListTemp1.append(line)	
				pass
		
		return varStrTemp1,writeListTemp1

class EngCla(object):
	
	varStr = []
	
	def __init__(self,PutPath,OutPath):
		self.author = 'ahoo'
		self.PutPath = PutPath
		self.OutPath = OutPath
	def Eng(self):
		try:
			
			fpClass = FileRead2Write()
			obfuCla	= ObfuscateMethod()

			#1.读取文件到LineList
			myInputList = fpClass.ReadInputFile(self.PutPath)
			
			
			#2.替换.
			varTem,writeTem  = obfuCla.ObfuscateQuotes(myInputList)
			#varTem1,__  = obfuCla.OufuscateBracket(myInputList)
			
			fpClass.WriteList2List(varTem,self.varStr)
			#fpClass.WriteList2List(varTem1,self.varStr)
			
			#logging.debug(varTem)
			
			#3.输出
			fpClass.WriteOutputFileEx_ListShuffle(self.OutPath,self.varStr)
			fpClass.WriteOutputFile(self.OutPath,writeTem)
			#fpClass.OpenOutPath(self.OutPath)
			
			logging.info('The Code has been Splited,there is my advice! Thanks!')
			print('The Code has been Splited,there is my advice! Thanks!')
			
		except :											#except Exception as e:  logging.debug(e)
			logging.exception('Eng has a exception info.')
			
		return True
