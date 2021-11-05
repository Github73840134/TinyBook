import json
import os
os.chdir('examples')

def walk(ls,lst={}):
	for i in ls:
		if os.path.isdir(i):
			lst[i] = {'action':'+d'}
			os.chdir(i)
			lst.update(walk(os.listdir()))
			os.chdir('../')
		else:
			lst[i] = {'action':'+','data':open(i,'r').read()}
	return lst
e = walk(os.listdir())
print(e)
os.chdir('../')
json.dump(e,open('examples.udf','w+'))