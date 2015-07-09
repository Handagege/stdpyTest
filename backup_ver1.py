#!/usr/bin/python
#Filename=backup_ver.py

import os
import time

source=['.']

target_dir='/data1/zhanghan/python_code/'
today=target_dir+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')
if not os.path.exists(today):
	os.mkdir(today)
	print 'Success created directory',today
target=today+os.sep+now+'.zip'

zip_command="zip -qr %s %s"%(target,''.join(source))

if os.system(zip_command)==0:
	print 'Success backup to',target
else:
	print 'Backup failed'

