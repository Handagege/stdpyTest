#/usr/bin/python

import json

obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
print repr(obj)
print encodedjson

for i in obj:
	print i

decodedjson = json.loads(encodedjson)
print decodedjson[-1]

f = open("testjson1.json")
decodedjson = json.load(f)
print decodedjson
lines = f.readlines()
for line in lines:
	print line
