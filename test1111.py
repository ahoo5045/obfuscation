#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ahoo'

from ObfuscateEng import EngCla

PutPath = 'Sample\\24_analysis.txt'				#JsVirus文件(卡饭精睿包2016.12.16.24).
OutPath = 'Sample\\24_EngRefactorObfuscate.vir'	#提取到的文件.

def test():
	ob = EngCla(PutPath,OutPath)
	ob.Eng()
	return True

if __name__ == '__main__':

    test()
