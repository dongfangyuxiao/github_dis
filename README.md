# github_dis

说明：
	一款精简版github信息泄露搜集工具
https://github.com/dongfangyuxiao/github_dis/
看了很多大佬的工具，自己写了一款，用起来效果还不错，分享给大家，欢迎多提意见

脚本非常简单，包含以下方法：
1、	load_keyword加载keyword.txt 里面的内容，这个txt文件中放置要搜索的关键字，一般为单位的信息，比如”阿里巴巴”、“百度”、等，支持中英文，域名，各类字符。建议包含各类关键信息，比如单位内网域名、标识、名称等信息。
 2、	load_type加载type.txt，里面放置各类配置信息，如jdbc、mysql、jenkins等，默认有56个，可以增添删除。
 3、	_auto_login,登录github账户，里面配置的是我自己的小号，在54行可以更改为自己的账号。 
4、	Run方法从两个队列中取要搜索的内容，并正则判断页数，判断后调用search方法，匹配去重后调用write方法写入github.txt。

5、	用法非常简单，python github.py，等待结果写入当前目录的github.txt

6、	脚本采用单线程，原因在于频率快的话会被封禁，测试，keyword中执行一个关键字需要时间在1分钟—2分钟之间。

7、	python2.7,需要的模块在requestsment.txt中，kali下可直接运行，其他的可以根据提示安装

参考：https://github.com/repoog/GitPrey 
https://github.com/FeeiCN/GSIL
