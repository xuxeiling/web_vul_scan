# web_vul_scan
#web_vul_scan
web漏洞扫描器
基于爬虫的多线程web漏洞扫描器
    
    python run.py --help
    Usage: run.py [options]
    
    Options:
      -h, --help            show this help message and exit
      -d DOMAIN, --domain=DOMAIN
                            Start the domain name
      -t THREAD_NUM, --thread=THREAD_NUM
                            Numbers of threads
      --depth=DEPTH         Crawling dept
      --pathfile=pathfile       file for vulnerability module(sql,xss,rfi)
      --policy=POLICY       Scan vulnerability when crawling: 0,Scan vulnerability
                            after crawling: 1
      --log=LOGFILE_NAME    save log file

支持多线程，爬虫深度，漏洞模块设置。
目前写好了sql注入，xss，文件包含三个模块。
更多的漏洞扫描后续可以继续优化。
已实现测试数据分离，目前支持的一下操作步骤：
 # 操作步骤 modlu_type
 Integer_sqlinj_scan
 Str_sqlinj_scan
 Sql_error_scan 
 RFI_PAYLOAD
用例文档实例可以参照 yongli.xlsx

# 数据存数据库
