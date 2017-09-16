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


logging.basicConfig(
		level = logging.DEBUG,
		format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
		#,filename='myapp.log',
		#filemode='a+'
		)

sys.stdout = io.TextIOWrapper(
				sys.stdout.buffer,
				encoding='utf-8') #改变标准输出的默认编码


PutPath = '24_analysis.txt'				#JsVirus文件(卡饭精睿包2016.12.16.24).
OutPath = '24_EngRefactorObfuscate.vir'	#提取到的文件.


#global area
myInputList = []
varStr 	= []
varStrRemoveRepeat = []
varStrRemoveRepeat.append('ahoo')



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

	

class RandomSequence(object):

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
		global varStrRemoveRepeat
		varName = self.randStr_az(3,7)
		while varName in varStrRemoveRepeat:
			varName = self.randStr_az(4,8)
		varStrItem = 'var '+ varName + ' = "' + itemstr + '"\n'
		varStrRemoveRepeat.append(varName)
		
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
		
		logging.debug(varTem)
		
		#3.输出
		fpClass.WriteOutputFileEx_ListShuffle(OutPath,varStr)
		fpClass.WriteOutputFile(OutPath,writeTem)
		fpClass.OpenOutPath(OutPath)
		
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
