#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
	目前版本v0.6
	
	计划:
	v0.7 --随机好多废数据.
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

PutPath = '24_analysis.txt'	#JsVirus文件(卡饭精睿包2016.12.16.24).
OutPath = '24_EngRefactorObfuscate.vir'	#提取到的文件.

myInputList = []
varStr 	= []
varStrRemoveRepeat = []
varStrRemoveRepeat.append('ahoo')


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码 

class FileRead2Write(object):
	
	def __init__(self):
		self.AuthorSign = True
		
	def ReadInputFile(self,InPath,ReadTye = 'r'):
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
		
	def OpenOutPath(self,OutPath, = '"D:\\Program Files (x86)\\Notepad++\\notepad++.exe" '):
		return os.system(program + OutPath) 		# program = 'notepad.exe' 
		
	'''	list排序
		ransomFamilyList = list(set(ransomFamilyList))
		list最后一行去掉\n
		ransomFamilyList[-1] = ransomFamilyList[-1].strip('\n')
		去空格.
		ransomFamilyList.append(i.strip(' ') + '\n')	
		
		遍历目录
		for parent,dirnames,filenames in os.walk(InputDir):
			for filename in filenames:
				fpRan.ReadInputFile(os.path.join(parent, filename)) 
		
		
	'''
		
		
		
		
		
class RandomSequence(object):
	def __init__(self):
		pass
	
	#随机一个长度2-5的字符串,一般用作变量名	
	def randStr_az(self,minNum=2,maxNum=5):			#判断一下大小传反了的情况
		try:
			randstr = ''
			if minNum > maxNum:
				minNum = min(minNum,maxNum)
				maxNum = max(minNum,maxNum)
			strLengt = random.randint(minNum,maxNum)
			for i in range(1,strLengt,1):
				chrTem = chr(random.randint(97,122))
				randstr = randstr + chrTem
			return randstr
		except Exception as e:
			print(e)
			return 'ahoo'
			pass
		
		
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
	
	#应该从正常的代码列表中随机一句,当废话用,混淆效果更好.
	#吧代码生成一个pprint py库在这调用,下版.
	JsCodeList = ['new Function("a", "b", "return a+b;");','var ybdetof5 = new ActiveXObject("Scripting.FileSystemObject");']
	def randCodeLine(self,CodeList = []):
		if len(CodeList) == 0:
			CodeList.append('Life is short,U need the Eng')
		return random.choice(CodeList)
		
	def randChr(self):
		return random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
		
	#在一段字符串中随选择若干个字符，形成列表
	def randChrEx_List(self):
		return random.sample('zyxwvutsrqponmlkjihgfedcba', 5)
		
	#随机生成一个List
	def randStrList(self,minNum=3,maxNum = 5):
		if minNum > maxNum:
			minNum = min(minNum,maxNum)
			maxNum = max(minNum,maxNum)
		
		arrLengt= random.randint(minNum,maxNum)
		arrList =[]
		for i in range(0,arrLengt,1):
			arrList.append(self.randStr_az())
		return arrList
	
	#生成数组模式1,2直接替换为变量.
	
	
	
	#随机一个function vbs的
	def randFun_Vb(self):
		return 'waitfortest\r\n coming~'
		pass
		
	def randFunList_Vb(self,MaxLen):
		funList=[]
		[i for i in range(0,MaxLen,1) funList.append(self.randFun_Vb()) ]
		return funList
			
		#a =1
		#[i for i in range(0,10,1)	a = a+i ]

class StrSplitEng(object):

	def __init__(self):
		pass
		
	#分割一个line中的元素返回list.
	def StrSplitLine(self,strForSplit):
		result = []
		if len(strForSplit) == 0:
			#print(strForSplit)
			return result

		strleng = len(strForSplit)
		if strleng <= 4:
			result.append(strForSplit)
		else:
			randlen = random.randint(2,4)
			result.append(strForSplit[:randlen])
			tempList = StrSplitLine(strForSplit[randlen:])
			
			for j in tempList:
				result.append(j)
		return result
	
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
	

		
		
#分割引擎
def JSVirus_Split():
	
	fpClass = FileRead2Write(PutPath,OutPath)
	#1.读取文件到LineList
	myInputList = fpClass.ReadInputFile()
	
	fpClass.WriteOutputFileEx_LineStr("This is my first refactor code!")
	fpClass.WriteOutputFile(myInputList)
	fpClass.WriteOutputFileEx_ListShuffle(myInputList)
	
	'''
	#2.1替换[] 和()之间的.
	writeList = []
	for line in myInputList:
		if line == "":
			#writeList.append(line)
			pass
		else:
			for i in re.findall('\[(\s*"[^\[\]\(\)]+"\s*)\]',line):
				patternFang = re.compile(i)
				replaceTempstr = replaceFindStrUsArrlist(i)
				line = patternFang.sub(replaceTempstr,line,count=1)
			
			for j in re.findall('\((\s*"[^\[\]\(\)]+"\s*)\)',line):
				patternFang = re.compile(j)
				replaceTempstr = replaceFindStrUsArrlist(j)
				line = patternFang.sub(replaceTempstr,line,count=1)
			writeList.append(line)	
			pass
			
	#2.2替换""之间的.	
	writeList2 = []
	for lin1 in myInputList:
		if lin1 == "":
			#writeList2.append(lin1)
			pass
		else:
			#print(lin1)
			for m in re.findall('"\s*[^"\,\+]+\s*"',lin1):
				if len(m) >= 2:
					patternYin = re.compile(m[1:-1])
					replaceTempstr1 = replaceFindStrUsArrlist(m[1:-1])
					#print(replaceTempstr1)
					lin1 = patternYin.sub(replaceTempstr1,lin1,count=1)
					#print(lin1)
				else:
					lin1 = m
			writeList2.append(lin1)
			pass
	#print(writeList2)
	'''
	os.system('"D:\\Program Files (x86)\\Notepad++\\notepad++.exe" ' + OutPath)
	print('The Code has been Splited,there is my advice! Thanks!')
	return True	


#替换符合条件的查找到的为数组类型.------------?应该在这个地方生成var同时返回
def replaceFindStrUsArrlist(findstr):
	'''
	list_split_line = []
	list_split_line =  StrSplitLine(findstr)
	print(list_split_line)
	
	
	list_replace_usarry = []
	for i_list_split_line in list_split_line:
		strArry =  replaceListItemUsArrary(i_list_split_line)
		list_replace_usarry.append(strArry)
	print(list_replace_usarry)
	'''
	replacestr = ''
	#缺少个判断小于3个字符怎么办.
	if len(findstr) <=3:
		return findstr
	for i_list_split_line in StrSplitLine(findstr):
		replacestr = replacestr + replaceListItemUsArrary(i_list_split_line) + ' + '
	#print(replacestr[:-3])
	return replacestr[:-3]


#替换某一个元素为数组类型	
def replaceListItemUsArrary(listItem):
	
	#对分割后数组的某个元素进行替换:随机数组长度.(index = random -1)
	arrLengt = 10
	index 	= random.randint(0,arrLengt-1)
	
	
		
	#v0.6
	varName = randStr(3,7)
	while varName in varStrRemoveRepeat:
		varName = randStr(4,8)
		
	varStrItem = 'var '+ varName + ' = "' + listItem + '"'
	#-------------------------------
	arrList[index] = varName
	replaceTemp = str(arrList) + '[' + str(index) + ']'
	
	replaceTemp_pattern = re.compile('\''+varName+'\'')
	replaceTemp = replaceTemp_pattern.sub(varName,replaceTemp)
	
	
	
	#print(arrList)
	#print(listItem)
	varStr.append(varStrItem)
	varStrRemoveRepeat.append(varName)
	print(varStrItem)
	print(replaceTemp)

	return replaceTemp


#v0.8---先不用开发了,有时间做个重构和优化吧.
	


if __name__ == '__main__':
    JSVirus_Split()
