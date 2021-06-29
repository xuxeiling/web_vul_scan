######创建爬虫链接抓取表#####
"""""""""
CREATE TABLE `crawl_url` (
  `uid` varchar(255) NOT NULL COMMENT '站点url',
  `GetParam` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'Get参数',
  `PostParam` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'Post参数',
  `UrlSet` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '解析出来的url集合',
  `UrlDepth` int(255) NOT NULL COMMENT '扫描深度',
  `CrawlerID` int(255) NOT NULL AUTO_INCREMENT COMMENT '数据库自增ID',
  `RequestHeader` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '请求头',
  `ResponseHeader` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '响应头',
  `Addtime` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '增加时间',
  PRIMARY KEY (`CrawlerID`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=765 DEFAULT CHARSET=utf8;

"""

######创建扫描表#####
"""
CREATE TABLE `sql_scan` (
  `Url` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '存在sql注入漏洞的URL',
  `TestParam` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '被测试的参数',
  `TestItem` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '构造异常参数值',
  `RequestHeader` longtext CHARACTER SET utf8 COLLATE utf8_general_ci COMMENT '请求头',
  `SqlID` int(11) NOT NULL AUTO_INCREMENT COMMENT '数据库自增id',
  `ResponseHeader` longtext CHARACTER SET utf8 COLLATE utf8_general_ci COMMENT '响应头',
  `Addtime` varchar(255) NOT NULL,
  `module_type` varchar(255) NOT NULL COMMENT '测试类型',
  PRIMARY KEY (`SqlID`)
) ENGINE=InnoDB AUTO_INCREMENT=2903 DEFAULT CHARSET=utf8;
"""