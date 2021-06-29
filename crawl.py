#coding:utf8

import threading
import lxml.html
import vul_module
import urllib
from urllib import request,parse
import chardet
from config import *


class SpiderThread(threading.Thread):
	
	def __init__(self,target,url,logfile,pathfile):
		threading.Thread.__init__(self)
		self.target = target
		self.deep_url = url
		self.logfile = logfile
		self.path = pathfile
		#获取链接


	def GetLinks(self,host,html):
		link_list = []
		try:
			tmp = lxml.html.document_fromstring(html)
			tmp.make_links_absolute(host)
			links = tmp.iterlinks()
			link_list = list(set([i[2] for i in links]))
			# print('GetLinks',link_list)
		except Exception as e:
			print (get_ctime() + '\tXml error:',str(e))
			self.logfile.write(get_ctime() + '\tXml error:' + str(e) + '\turl:' + self.deep_url[1] +'\n')
			self.logfile.flush()
		return link_list
	#爬取links页面信息
	def SpiderPage(self):
		link_tmp = []
		try:
			html = urllib.request.urlopen(self.deep_url[1],timeout=10).read().lower()
			if chardet.detect(html)['encoding'] == 'GB2312':
				html = html.decode('gb2312').encode('utf8')
				#link列表
			link_list = self.GetLinks(self.target,html)
			for i in link_list:
				ext =parse.urlparse(i)[2].split('.')[-1]
				#不是图片等格式的链接
				if ext not in IGNORE_EXT:
					link_tmp.append(i)

		except Exception as e:
			print (get_ctime() + '\tHttp error:',str(e))
			self.logfile.write(get_ctime() + '\tHttp error:' + str(e) + '\turl:' + self.deep_url[1] +'\n')
			self.logfile.flush()
		link_list = link_tmp
		# print('SpiderPage',link_list)
		return link_list,self.deep_url[1]

	def url_similar_check(self,url):
		'''
		URL相似度分析
		当url路径和参数键值类似时，则判为重复
		'''
		global SIMILAR_SET
		url_struct = parse.urlparse(url)
		query_key = '|'.join(sorted([ i.split('=')[0] for i in url_struct.query.split('&') ]))
		url_hash = hash(url_struct.path + query_key)
		if url_hash not in SIMILAR_SET:
			SIMILAR_SET.add(url_hash)
			return True
		return False

	def run(self):
		global QUEUE
		global TOTAL_URL
		sql_data = []
		tmp_link_list = self.SpiderPage()[0]
		#目标url
		urlid = self.SpiderPage()[1]
		pre_url_list = TOTAL_URL

		#判断link是否是在目标域下
		link_list = []
		for i in tmp_link_list:
			if parse.urlparse(self.target).netloc == parse.urlparse(i).netloc:
				link_list.append(i)

		TOTAL_URL = TOTAL_URL | set(link_list)
		new_url_list = list(TOTAL_URL - pre_url_list)
		new_url_list1 = '__'.join(new_url_list)


		#添加deep信息,并进行url相似度分析
		depth = self.deep_url[0] + 1

		for i in range(len(new_url_list)):
			if self.url_similar_check(new_url_list[i]):
				print (get_ctime() + '\tCrawl url:' + new_url_list[i])
				vul_module.vul_module(new_url_list[i],self.logfile).check(self.path)
				self.logfile.write(get_ctime() + '\tCrawl url:' + new_url_list[i] + ',depth:' + str(depth) + '\n')
				self.logfile.flush()
				QUEUE.append([depth,new_url_list[i]])
		sql_data.append(self.deep_url[1])
		sql_data.append(self.deep_url[0] + 1)
		sql_data.append(new_url_list1)
		sql_data.append(get_ctime())

		conn = get_conn()
		cur = conn.cursor()

		sql_crawl = "INSERT INTO crawl_url (uid,GetParam,PostParam,UrlSet,UrlDepth,CrawlerID,RequestHeader,ResponseHeader,Addtime) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(str(sql_data[0]),'','',sql_data[2], sql_data[1],'0','','',str(sql_data[3]))
		cur.execute(sql_crawl)
		conn.commit()
		result = cur.fetchall()
		# print("数据库插入与查询检测", result)

if __name__ == '__main__':
	test = SpiderThread()
	test.run()

