import json
import os
import sys
gfl = {}
e = {'data':{}}
def walk(ls,lst={}):
	global gfl
	for i in ls:
		if os.path.isdir(i):
			lst[i] = {'action':'+d'}
			print("Entering Directory:",i)
			os.chdir(i)
			gfl[os.getcwd()] = 'd'
			lst.update(walk(os.listdir()),)
			print("Exiting Directory:",i)
			os.chdir('../')
		else:
			print("Adding File:",i)
			try:
				gfl[os.getcwd()+'/'+i] = 'f'
				lst['examples/'+os.path.basename(os.getcwd())+'/'+i] = {'action':'+','data':open(i,'r').read()}
				print("File Added:",i)
			except:
				print("Adding File",i,"Failed")
	return lst
print("Starting")
try:
	print("Checking changelog")
	file = open('changelog.clog','r')
	c = json.loads(file.read())
	for i in c:
		if c[i] == 'f':
			if os.path.isfile(i) == False:
				print("File:'",i,"'does not exist")
				e['data'][i.strip('/home/runner/Tinybook')] = {'action':'-'}
		if c[i] == 'd':
			if os.path.isdir(i) == False:
				print("Folder:'",i,"'does not exist")
				e['data'][i.strip('/home/runner/Tinybook')] = {'action':'-d'}
	print("Changelog read!")
except Exception as e:
	print("Error Reading Changelog",e)
os.chdir('examples')
t = walk(os.listdir())
e['data'].update(t)
os.chdir('../')
print("Generating udf")
json.dump(e,open('examples.udf','w+'))
print("Generating Changelog")
with open('changelog.clog','w+') as file:
	file.write(json.dumps(gfl))
	file.close()
print("Done")