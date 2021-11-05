import json
import os
os.chdir('examples')

def walk(ls,lst={}):
	for i in ls:
		if os.path.isdir(i):
			lst[i] = {'action':'+d'}
			print("Entering Directory:",i)
			os.chdir(i)
			lst.update(walk(os.listdir()))
			print("Exiting Directory:",i)
			os.chdir('../')
		else:
			print("Adding File:",i)
			try:
				lst[i] = {'action':'+','data':open(i,'r').read()}
				print("File Added:",i)
			except:
				print("Adding File",i,"Failed")
	return lst
print("Starting")
e = {'data':walk(os.listdir())}
os.chdir('../')
print("Generating")
json.dump(e,open('examples.udf','w+'))
print("Done")