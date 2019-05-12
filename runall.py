# -*- coding: utf-8 -*-
import unittest,csv
import os,sys
import time
#导入testbaidu1,testbaidu2
import testBaidu1
import testBaidu2

#手工添加案例到套件，
def creatsuite():
    suite = unittest.TestSuite()
    #将测试用例添加到测试容器（套件）中
    #addTest()
    # suite.addTest(testBaidu1.Baidu1("test_baidusearch"))
    # suite.addTest(testBaidu1.Baidu1("test_hao"))
    # suite.addTest(testBaidu2.Baidu2("test_baidusearch"))

    #makeSuite()
    # suite.addTest(unittest.makeSuite(testBaidu1.Baidu1))
    # suite.addTest(unittest.makeSuite(testBaidu2.Baidu2))

    #TestLoader()
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(testBaidu1.Baidu1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(testBaidu2.Baidu2)
    # suite = unittest.TestSuite([suite1,suite2])
    #return suite

    #discover
    discover = unittest.defaultTestLoader.discover('../test1',pattern='test*.py',top_level_dir=None)
    print(discover)
    return discover

if __name__=="__main__":
    suite = creatsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)