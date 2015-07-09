import urllib
import urllib2
import time

def print_url_postMsg(para_dic,response):
	print "[url_posMsg]: {[key]:test [rank]:%s [time]:%s [response]:%s}"\
	%(para_dic["rank"],para_dic["time"],response.read())
	
url = "http://trend.recom.i.weibo.com/v4/datachart/interface/add.php"
del_url = "http://trend.recom.i.weibo.com/v4/datachart/interface/delete.php"
now = int(time.time())
para_dic = {"key":"test","rank":"0","time":str(now)}
del_para_dic = {"key":"test","time":str(now)}

#for i in range(0,100):
#	para_dic["rank"] = i%3+5
#	para_dic["time"] = str(now-i*5*60)
#	para_data = urllib.urlencode(para_dic)
#	response = urllib2.urlopen(url, para_data)
#	print_url_postMsg(para_dic,response)
for i in range(0,24*60):
	del_para_dic["time"] = str(now-i*60)
	para_data = urllib.urlencode(del_para_dic)
	response = urllib2.urlopen(url,para_data,100)
	print response.read()
	
