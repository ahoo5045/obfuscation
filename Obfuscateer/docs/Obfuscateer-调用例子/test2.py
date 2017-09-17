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

import os
import logging
import logging.config
from Obfuscateer.ObfuscateEngM 	import EngCla
#1.NeedReplaceFile--".C:\Users\tech\AppData\Local\Programs\Python\Python35\Lib\site-packages\Obfuscateer-0.1-py3.5.egg\Obfuscateer\ObfuscateEngM.py" --Fix---：from Obfuscateer.FileRead2Write import FileRead2Write 

#--------------------文件配置----------
logfilePath = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig('logging.conf')
logging.getLogger()


PutPath = 'Sample\\24_analysis.txt'				#JsVirus文件(卡饭精睿包2016.12.16.24).
OutPath = 'Sample\\24_EngRefactorObfuscate.vir'	#提取到的文件.



if __name__ == '__main__':
    eng = EngCla(PutPath,OutPath)
    eng.Eng()