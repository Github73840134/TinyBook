'''TinyBook'''
import json
import os
import socket
import urllib.request
import sys
import time
__version__ = '1.0.3'
__info__ = '©2021 Seth Edwards.'
__metadata_ver__ = '1.0'
__port__ = 'CPython'
__releasenotes__ = '- Added self updating (Only works on python 3.5.9 and above)'
__license__ = '''
©2021 Seth Edwards
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
book = {}
class makebook:
	'''
	Class: Book Maker
	'''
	class metadata:
		'''
		Add metadata to book
		'''
		@staticmethod
		def title(title):
			'''
			Add chapter data to book\n
			:param title (str): Book title
			'''
			if 'metadata' not in book:
				book['metadata'] = {}
			book['metadata']['title'] = title
		@staticmethod
		def chapters(chap_data):
			'''
			Add chapter data to book\n
			:param chap_data (dict): Chapter data (Must be in tinybook format)\nRefer to the documentation on ways to generate
			'''

			if 'metadata' not in book:
				book['metadata'] = {}
			book['metadata']['ci'] = chap_data
		@staticmethod
		def version(ver=1.0):
			'''
			Select the metadata version
			Currently only version 1.0
			:param ver (int): Version number
			'''
			if 'metadata' not in book:
				book['metadata'] = {}
			if ver != 0 and not ver > 1.0:
				book['metadata']['ver'] = str(ver)
			else:
				if ver <= 0:
					raise ValueError("Version cant be 0 or less")
				if ver > 1.0:
					raise ValueError("Invalid Version")
		@staticmethod
		def cover(img_data,img_type='bmp'):
			'''
			Adds a cover to the book\n
			Cover can either be a .png file or a .bmp file\n
			:param img_data (bytes): Image data (Must be in ascii)
			'''
			if type(img_type) != str:
				raise TypeError('img_type must be str')
			if type(img_data) != bytes:
				raise TypeError('img_data must be bytes')
			if 'metadata' not in book:
				book['metadata'] = {}
			if img_type == 'bmp':
				book['metadata']['cover'] = {'type':'bmp','data':img_data}
			if img_type == 'png':
				book['metadata']['cover'] = {'type':'bmp','png':img_data}
			else:
				raise Exception("img_type must be either bmp or png")
		@staticmethod
		def pages(pages):
			if 'metadata' not in book:
				book['metadata'] = {}
			book['metadata']['pages'] = str(pages)
	@staticmethod
	class add:
		@staticmethod
		def page(page_num,data):
			'''
			Adds a page to the book\n
			:param page_num (int): Page number\n
			:param data (dict): Page data in the tinybook format\n
			'''
			if 'metadata' not in book:
				book['metadata'] = {}
			if 'bookdata' not in book:
				book['bookdata'] = {}
			book['bookdata'][str(page_num)] = {'metadata':{},'data':data}
	@staticmethod
	def showbook():
		'''
		Returns the raw book data
		'''
		return book
	@staticmethod
	def make(name):
		'''
		:param name (str): File name of the book\n
		Make the book from the book object.
		'''
		def set_default(obj):
			if isinstance(obj, set):
				return list(obj)
			raise TypeError
		if book != None:
			if 'ver' not in book['metadata']:
				book['metadata']['ver'] = '1.0'
			if 'title' not in book['metadata']:
				book['metadata']['title'] = ''
			if 'pages' not in book['metadata']:
				book['metadata']['pages'] = str(len(book['bookdata']))
			if 'cover' not in book['metadata']:
				book['metadata']['cover'] = {'type':'','cover':''}
			result = json.dump(book, fp=open(name+'.tb','w+'),default=set_default)
class Book:
	'''
	Allows you to get book data
	'''
	class info:
		'''
		Get info on book
		'''
		@staticmethod
		def title(fn):
			'''
			Get book title from book\n
			:param: fn filename (str)\n
			Returns:str
			'''
			d = json.loads(open(fn,'r').read())
			if 'metadata' in d:
				if 'title' in d['metadata']:
					return d['metadata']['title']
				else:
					raise Exception("Book Metadata Corrupted")
			else:
				raise Exception("Corrupted Book")
		@staticmethod
		def pages(fn):
			"Get total pages from book\n:param: fn filename (str)\nReturns: int"
			d = json.loads(open(fn,'r').read())
			if 'metadata' in d:
				if 'pages' in d['metadata']:
					return int(d['metadata']['pages'])
				else:
					raise Exception("Book Metadata Corrupted")
			else:
				raise Exception("Corrupted Book")
		class chapters:
			"Get chapters info"
			@staticmethod
			def total(fn):
				'''
				Gets total chapters from book\n
				:param fn: filename (str)\n
				Returns:int'''
				d = json.loads(open(fn,'r').read())
				if 'metadata' in d:
					if 'ci' in d['metadata']:
						return len(d['metadata']['ci'])
					else:
						raise Exception("Book Metadata Corrupted")
				else:
					raise Exception("Corrupted Book")
			@staticmethod
			def list(fn):
				'''
				Gets all chaptername in book\n
				:param fn (str): filename of book
				'''
				d = json.loads(open(fn,'r').read())
				if 'metadata' in d:
					if 'ci' in d['metadata']:
						chapters = []
						for i in d['metadata']['ci']:
							chapters.append(d['metadata']['ci'][i])
						return chapters
					else:
						return None
				else:
					raise Exception("Corrupted Book")
class Generator:
	'Easy to use data generator for making your tinybook'
	class generate:
		'Allows you to generate elements for your tinybook'
		@staticmethod
		class page:
			'Page data generator'
			@staticmethod
			def paragraph(text,idn=''):
				'''
				make a tinybook compatible paragraph\n
				:param text (str): paragraph\n
				:param idn (str): A unique id number for the paragraph (Only use if you want multiple paragraphs on page)\n
				Recommended 1 Paragraph Per page
				\n
				Returns: A tinybook compatible dict
				'''
				return {'p'+idn:text}
			@staticmethod
			def text(text,idn=''):
				'''
				make a tinybook compatible text\n
				:param text (str): text\n
				:param idn (str): A unique id number for the text (Only use if you want multiple text elements on page)\n
				Returns: A tinybook compatible dict
				'''
				return {'t'+idn:text}
			@staticmethod
			def heading(text,idn=''):
				'''
				make a tinybook compatible heading\n
				:param text (str): heading\n
				:param idn (str): A unique id number for the heading (Only use if you want multiple heading on page)
				\n
				Returns: A tinybook compatible dict
				'''
				return {'h'+idn:text}
			@staticmethod
			def join(data):
				'''
				Joins all page data objects into one\n
				:param data (list): list containing tinybook format dict
				'''
				def Merge(dict1,dict2):
					return(dict2.update(dict1))
				output = {}
				for i in range(len(data)):
					Merge(data[i],output)
				return output
		@staticmethod
		class chapters:
			'''
			Chapter Generator
			'''
			@staticmethod
			def make(chapters):
				'''
				Makes Chapters from a list\n
				:param chapters (list): Chapter data\n
				--How to use--\n
				Chapters should be in a list each item being a string.\n
				[[page_number,chapter_title]]\n
				page_number should be the page the chapters start on.\n
				chapter_title should be the chapter title.\n
				e.g.\n
				[['1','Look your learning'],['2','Cool Right']]\nmake([['1','Look your learning'],['2','Cool Right']])
				\n\n
				Returns Tinybook compatible dict
				'''
				return dict(chapters)
class read:
	'''
	Read a tinybook file
	'''
	@staticmethod
	def read(fn):
		'''
		Reads a tiny book file and returns the plain text\n
		:param fn (str): filename\n
		Returns a list in the following format(where indent=sublist):\n
		Book:\n
			Chapter:\n
				Page:\n
		would be\n
		[[["Page1"]]]
		 
		'''
		d = json.loads(open(fn,'r').read())
		outbook = [[]]
		if 'metadata' not in d:
			raise Exception("Corrupted Book")
		if 'ci' not in d['metadata']:
			raise Exception("Book Metadata Corrupted")
		if 'pages' not in d['metadata']:
			raise Exception("Book Metadata Corrupted")
		if 'bookdata' not in d:
			return None
		pages = list(d['bookdata'])
		cpages = list(d['metadata']['ci'])
		ticker = 0
		for i in range(len(pages)):
			outbook[ticker].append([])
			for t in d['bookdata'][pages[i]]['data']:
				if 'h' in t:
					outbook[ticker][i].append('\u001b[1m'+d['bookdata'][pages[i]]['data'][t]+'\u001b[0m\n\n')
				if 'p' in t:
					outbook[ticker][i].append('\t'+d['bookdata'][pages[i]]['data'][t]+'\n')
				if 't' in t:
					outbook[ticker][i].append(d['bookdata'][pages[i]]['data'][t]+'\n')
			if str(i+2) in cpages:
				ticker += 1
				outbook.append([[]])
		print(outbook)
		return outbook
	@staticmethod
	def term_ready(fn,offset=-17):
		'''
		Reads the tinybook and return a premade terminal output
		:param fn (str): Filename of tinybook
		:param offset (int): Terminal width offset for divider line (negative number to trim back, positive to add) 
		'''
		d = json.loads(open(fn,'r').read())
		outbook = ''
		if 'metadata' not in d:
			raise Exception("Corrupted Book")
		if 'ci' not in d['metadata']:
			raise Exception("Book Metadata Corrupted")
		if 'pages' not in d['metadata']:
			raise Exception("Book Metadata Corrupted")
		if 'bookdata' not in d:
			return None
		pages = list(d['bookdata'])
		cpages = list(d['metadata']['ci'])
		ticker = 0
		w,h = os.get_terminal_size()
		for i in range(len(pages)):
			outbookt = h
			for t in d['bookdata'][pages[i]]['data']:
				if 'h' in t:
					outbook += '\u001b[1m'+d['bookdata'][pages[i]]['data'][t]+'\u001b[0m\n\n'
					k = '\u001b[1m'+d['bookdata'][pages[i]]['data'][t]+'\u001b[0m\n\n'
					outbookt -= len(k.split('\n'))
				if 'p' in t:
					outbook += '\t'+d['bookdata'][pages[i]]['data'][t]+'\n'
					k = '\u001b[1m'+d['bookdata'][pages[i]]['data'][t]+'\u001b[0m\n\n'
					outbookt -= len(k.split('\n'))
				if 't' in t:
					outbook += d['bookdata'][pages[i]]['data'][t]+'\n'
					k = '\u001b[1m'+d['bookdata'][pages[i]]['data'][t]+'\u001b[0m\n\n'
					outbookt -= len(k.split('\n'))
				if str(i+2) in cpages:
					ticker += 1
			for g in range(outbookt):
				outbook += '\n'
			outbook += str(i)+'Chapter:'+str(ticker+1)+' Page:' + str(i+1) + ' of ' + str(len(pages)) + '\n'
			for e in range(w-(-offset)):
				outbook += '-'
			outbook += '\n'
		return outbook
def update():
	if sys.version_info[0] < 3 and sys.version_info[1] < 5 and sys.version_info[2] < 9:
		raise Exception("Must be using Python 3.5 or above to use this function")
	print("Connecting to server")
	s = urllib.request.urlopen('https://tinybookdownload.sethedwards.repl.co/')
	print("Connected")
	dt = s.read().decode('utf-8')
	length = len(dt)
	print("Update size:",length,'bytes')
	datastr = ''
	op = 0
	for i in range(0,length):
		if round(((i+1)/length)*100) != op:
			print("\u001b[1000D\u001b[2KDownloading",str(round(((i+1)/length)*100))+'%',end='',flush=True)
			op = round(((i+1)/length)*100)
		time.sleep(0.00001)
		datastr += dt[i]
	data = json.loads(datastr)
	print("Starting update")
	file = open('tinybook.py','w+')
	for i in range(0,len(data['lib'])):
		if round(((i+1)/len(data['lib']))*100) != op:
			print("\u001b[1000D\u001b[2KUpdating Library",str(round(((i+1)/len(data['lib']))*100))+'%',end='',flush=True)
			op = round(((i+1)/len(data['lib']))*100)
		file.write(data['lib'][i])
		time.sleep(0.00001)
	file.close()
	file = open('README.md','w+')
	for i in range(0,len(data['readme'])):
		if round(((i+1)/len(data['readme']))*100) != op:
			print("\u001b[1000D\u001b[2KUpdating README",str(round(((i+1)/len(data['readme']))*100))+'%',end='',flush=True)
			op = round(((i+1)/len(data['readme']))*100)
		file.write(data['readme'][i])
		time.sleep(0.00001)
	file.close()