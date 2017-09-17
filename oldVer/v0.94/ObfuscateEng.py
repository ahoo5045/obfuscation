#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
	目前版本v0.8--Refactor
	
	计划:
	v0.8 --用vb二次加密.
	v0.9 --自变形.
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
from FileRead2Write import FileRead2Write 
from RandomSequence import RandomSequence
from StrSplitEng 	import StrSplitEng

#--------------------文件配置----------
logfilePath = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig('logging.conf')
logging.getLogger()


#sys.stdout = io.TextIOWrapper(
#				sys.stdout.buffer,
#				encoding='utf-8') #改变标准输出的默认编码


PutPath = 'Sample\\24_analysis.txt'				#JsVirus文件(卡饭精睿包2016.12.16.24).
OutPath = 'Sample\\24_EngRefactorObfuscate.vir'	#提取到的文件.

#global area
myInputList = []
varStr 	= []


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
		
	
	

#分割引擎
def Eng():
	
	try:
		
		fpClass = FileRead2Write()
		obfuCla	= ObfuscateMethod()

		#1.读取文件到LineList
		global myInputList
		myInputList = fpClass.ReadInputFile(PutPath)
		
		
		#2.替换.
		global varStr
		varTem,writeTem  = obfuCla.ObfuscateQuotes(myInputList)
		#varTem1,__  = obfuCla.OufuscateBracket(myInputList)
		
		fpClass.WriteList2List(varTem,varStr)
		#fpClass.WriteList2List(varTem1,varStr)
		
		#logging.debug(varTem)
		
		#3.输出
		fpClass.WriteOutputFileEx_ListShuffle(OutPath,varStr)
		fpClass.WriteOutputFile(OutPath,writeTem)
		#fpClass.OpenOutPath(OutPath)
		
		
		logging.info('The Code has been Splited,there is my advice! Thanks!')
		print('The Code has been Splited,there is my advice! Thanks!')
		
	except :											#except Exception as e:  logging.debug(e)
		logging.exception('Eng has a exception info.')
		
	return True	

	
def Example():
	'''
	fpClass = FileRead2Write()
	rdClass = RandomSequence()
	spClass = StrSplitEng()
	
	#1.读取文件到LineList
	global myInputList
	myInputList = fpClass.ReadInputFile(PutPath)
	
	
	fpClass.WriteOutputFileEx_LineStr(OutPath,"This is my first refactor code!")
	fpClass.WriteOutputFile(OutPath,rdClass.randFunList_Vb(8))
	fpClass.WriteOutputFile(OutPath,rdClass.randStrList(6,10))
	fpClass.WriteOutputFileEx_ListShuffle(OutPath,myInputList)
	print(rdClass.randStrArrary('ahoo'))
	print(rdClass.randStrArryEx_var('ahoo'))
	strtemp = spClass.StrSplitLine2List("Scripting.FileSystemObject")
	print(strtemp)
	strtemp1 = spClass.StrSplitLine2SelfTypeStr('Scripting.FileSystemObject')
	print(strtemp1)
	strtemp1 = spClass.StrSplitLine2SelfTypeStr('Scripting.FileSystemObject')
	varlsit,replace =  rdClass.randSelfTypeStr2ArraryTypeStr(strtemp1)
	print(replace)
	print(varlsit)
	#['nktk', 'qr', qaxccb, 'rxoh', 'w'][2] + ['fhn', 'pqlh', fpweqc][2] + ['uwm', ihcjzc, 'uzm'][1] + ['l', lh, 't', 'gkx'][1] + ['mjld', 'kwas', wzgc, 'jjog', 'xx'][2] + ['okm', 'axr', dbz, 'ipg', 'p'][2] + ['fde', 'pd', btgrqw][2] + [dlnim, 'g', 'iaah', 'm', 'r'][0]
	#['var qaxccb = "Sc"', 'var fpweqc = "ri"', 'var ihcjzc = "pti"', 'var lh = "ng.F"', 'var wzgc = "ileS"', 'var dbz = "yst"', 'var btgrqw = "emOb"', 'var dlnim ="ject"']
	'''
	pass
	

if __name__ == '__main__':
    Eng()
