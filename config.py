#coding:utf8
import time
import pymysql

IGNORE_EXT = ['css','js','jpg','png','gif','rar','pdf','doc']
#不期待的文件后缀
EXPECT_EXT = ['php','jsp','asp','aspx']

HEADER = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
}
QUEUE = []
TOTAL_URL = set()
SIMILAR_SET = set()

def get_ctime():
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def get_conn():
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='scan_data',
						   charset='utf8')
	return conn