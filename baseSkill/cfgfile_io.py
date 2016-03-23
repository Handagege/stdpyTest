#!/usr/bin/python

import ConfigParser


config = ConfigParser.ConfigParser()
config.readfp(open('o.ini','r'))

source = config.get('info','source')
target_dir = config.get('info','target_dir')
time_range = config.get('info','time_range')

print source
print target_dir
print time_range

