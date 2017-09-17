

1.需要修改的地方.
	dir: NAME
	tests/NAME_tests.py
	tests/NAME_tests.py-->import NAME
	setup.py--->config--> 'packages': ['NAME'],
	
2.以这种方式调用要替换文件.C:\Users\tech\AppData\Local\Programs\Python\Python35\Lib\site-packages\Obfuscateer-0.1-py3.5.egg\Obfuscateer\ObfuscateEngM.py ----修改导入方式为：from Obfuscateer.FileRead2Write import FileRead2Write 

3.调用例子有两种.

4.骨架测试:F:\AlreadyDoneForRecord\test\ObfuscateEng: 路径cmd命令： nosetests