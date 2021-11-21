'''TinyBook'''
import json
import os
import socket
import urllib.request
import sys
import time
import shutil
import base64
__version__ = '1.0.4.1.3'
__xedoc_version = '0.1.0 (2018 Edition, Oct 29 2021, 23:52:26 CEST)'
__info__ = '©2021 Github73840134.'
__metadata_ver__ = '1.0'
__port__ = 'CPython'
__releasenotes__ = '''-Fixed Bugs'''
__credits__ = {'Formats':[["xedoc","RustedTerrier","https://codeberg.org/RustedTerrier/xedoc"]],"Special Thanks":[["RustedTerrier","https://codeberg.org/RustedTerrier"]]}
__license__ = '''
©2021 Github73840134
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
__xedoc_license__ = '''
Mozilla Public License
Version 2.0
1. Definitions

1.1. “Contributor”

    means each individual or legal entity that creates, contributes to the creation of, or owns Covered Software.
1.2. “Contributor Version”

    means the combination of the Contributions of others (if any) used by a Contributor and that particular Contributor’s Contribution.
1.3. “Contribution”

    means Covered Software of a particular Contributor.
1.4. “Covered Software”

    means Source Code Form to which the initial Contributor has attached the notice in Exhibit A, the Executable Form of such Source Code Form, and Modifications of such Source Code Form, in each case including portions thereof.
1.5. “Incompatible With Secondary Licenses”

    means

        that the initial Contributor has attached the notice described in Exhibit B to the Covered Software; or

        that the Covered Software was made available under the terms of version 1.1 or earlier of the License, but not also under the terms of a Secondary License.

1.6. “Executable Form”

    means any form of the work other than Source Code Form.
1.7. “Larger Work”

    means a work that combines Covered Software with other material, in a separate file or files, that is not Covered Software.
1.8. “License”

    means this document.
1.9. “Licensable”

    means having the right to grant, to the maximum extent possible, whether at the time of the initial grant or subsequently, any and all of the rights conveyed by this License.
1.10. “Modifications”

    means any of the following:

        any file in Source Code Form that results from an addition to, deletion from, or modification of the contents of Covered Software; or

        any new file in Source Code Form that contains any Covered Software.

1.11. “Patent Claims” of a Contributor

    means any patent claim(s), including without limitation, method, process, and apparatus claims, in any patent Licensable by such Contributor that would be infringed, but for the grant of the License, by the making, using, selling, offering for sale, having made, import, or transfer of either its Contributions or its Contributor Version.
1.12. “Secondary License”

    means either the GNU General Public License, Version 2.0, the GNU Lesser General Public License, Version 2.1, the GNU Affero General Public License, Version 3.0, or any later versions of those licenses.
1.13. “Source Code Form”

    means the form of the work preferred for making modifications.
1.14. “You” (or “Your”)

    means an individual or a legal entity exercising rights under this License. For legal entities, “You” includes any entity that controls, is controlled by, or is under common control with You. For purposes of this definition, “control” means (a) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (b) ownership of more than fifty percent (50%) of the outstanding shares or beneficial ownership of such entity.

2. License Grants and Conditions
2.1. Grants

Each Contributor hereby grants You a world-wide, royalty-free, non-exclusive license:

    under intellectual property rights (other than patent or trademark) Licensable by such Contributor to use, reproduce, make available, modify, display, perform, distribute, and otherwise exploit its Contributions, either on an unmodified basis, with Modifications, or as part of a Larger Work; and

    under Patent Claims of such Contributor to make, use, sell, offer for sale, have made, import, and otherwise transfer either its Contributions or its Contributor Version.

2.2. Effective Date

The licenses granted in Section 2.1 with respect to any Contribution become effective for each Contribution on the date the Contributor first distributes such Contribution.
2.3. Limitations on Grant Scope

The licenses granted in this Section 2 are the only rights granted under this License. No additional rights or licenses will be implied from the distribution or licensing of Covered Software under ths License. Notwithstanding Section 2.1(b) above, no patent license is granted by a Contributor:

    for any code that a Contributor has removed from Covered Software; or

    for infringements caused by: (i) Your and any other third party’s modifications of Covered Software, or (ii) the combination of its Contributions with other software (except as part of its Contributor Version); or

    under Patent Claims infringed by Covered Software in the absence of its Contributions.

This License does not grant any rights in the trademarks, service marks, or logos of any Contributor (except as may be necessary to comply with the notice requirements in Section 3.4).
2.4. Subsequent Licenses

No Contributor makes additional grants as a result of Your choice to distribute the Covered Software under a subsequent version of this License (see Section 10.2) or under the terms of a Secondary License (if permitted under the terms of Section 3.3).
2.5. Representation

Each Contributor represents that the Contributor believes its Contributions are its original creation(s) or it has sufficient rights to grant the rights to its Contributions conveyed by this License.
2.6. Fair Use

This License is not intended to limit any rights You have under applicable copyright doctrines of fair use, fair dealing, or other equivalents.
2.7. Conditions

Sections 3.1, 3.2, 3.3, and 3.4 are conditions of the licenses granted in Section 2.1.
3. Responsibilities
3.1. Distribution of Source Form

All distribution of Covered Software in Source Code Form, including any Modifications that You create or to which You contribute, must be under the terms of this License. You must inform recipients that the Source Code Form of the Covered Software is governed by the terms of this License, and how they can obtain a copy of this License. You may not attempt to alter or restrict the recipients’ rights in the Source Code Form.
3.2. Distribution of Executable Form

If You distribute Covered Software in Executable Form then:

    such Covered Software must also be made available in Source Code Form, as described in Section 3.1, and You must inform recipients of the Executable Form how they can obtain a copy of such Source Code Form by reasonable means in a timely manner, at a charge no more than the cost of distribution to the recipient; and

    You may distribute such Executable Form under the terms of this License, or sublicense it under different terms, provided that the license for the Executable Form does not attempt to limit or alter the recipients’ rights in the Source Code Form under this License.

3.3. Distribution of a Larger Work

You may create and distribute a Larger Work under terms of Your choice, provided that You also comply with the requirements of this License for the Covered Software. If the Larger Work is a combination of Covered Software with a work governed by one or more Secondary Licenses, and the Covered Software is not Incompatible With Secondary Licenses, this License permits You to additionally distribute such Covered Software under the terms of such Secondary License(s), so that the recipient of the Larger Work may, at their option, further distribute the Covered Software under the terms of either this License or such Secondary License(s).
3.4. Notices

You may not remove or alter the substance of any license notices (including copyright notices, patent notices, disclaimers of warranty, or limitations of liability) contained within the Source Code Form of the Covered Software, except that You may alter any license notices to the extent required to remedy known factual inaccuracies.
3.5. Application of Additional Terms

You may choose to offer, and to charge a fee for, warranty, support, indemnity or liability obligations to one or more recipients of Covered Software. However, You may do so only on Your own behalf, and not on behalf of any Contributor. You must make it absolutely clear that any such warranty, support, indemnity, or liability obligation is offered by You alone, and You hereby agree to indemnify every Contributor for any liability incurred by such Contributor as a result of warranty, support, indemnity or liability terms You offer. You may include additional disclaimers of warranty and limitations of liability specific to any jurisdiction.
4. Inability to Comply Due to Statute or Regulation

If it is impossible for You to comply with any of the terms of this License with respect to some or all of the Covered Software due to statute, judicial order, or regulation then You must: (a) comply with the terms of this License to the maximum extent possible; and (b) describe the limitations and the code they affect. Such description must be placed in a text file included with all distributions of the Covered Software under this License. Except to the extent prohibited by statute or regulation, such description must be sufficiently detailed for a recipient of ordinary skill to be able to understand it.
5. Termination

5.1. The rights granted under this License will terminate automatically if You fail to comply with any of its terms. However, if You become compliant, then the rights granted under this License from a particular Contributor are reinstated (a) provisionally, unless and until such Contributor explicitly and finally terminates Your grants, and (b) on an ongoing basis, if such Contributor fails to notify You of the non-compliance by some reasonable means prior to 60 days after You have come back into compliance. Moreover, Your grants from a particular Contributor are reinstated on an ongoing basis if such Contributor notifies You of the non-compliance by some reasonable means, this is the first time You have received notice of non-compliance with this License from such Contributor, and You become compliant prior to 30 days after Your receipt of the notice.

5.2. If You initiate litigation against any entity by asserting a patent infringement claim (excluding declaratory judgment actions, counter-claims, and cross-claims) alleging that a Contributor Version directly or indirectly infringes any patent, then the rights granted to You by any and all Contributors for the Covered Software under Section 2.1 of this License shall terminate.

5.3. In the event of termination under Sections 5.1 or 5.2 above, all end user license agreements (excluding distributors and resellers) which have been validly granted by You or Your distributors under this License prior to termination shall survive termination.
6. Disclaimer of Warranty

Covered Software is provided under this License on an “as is” basis, without warranty of any kind, either expressed, implied, or statutory, including, without limitation, warranties that the Covered Software is free of defects, merchantable, fit for a particular purpose or non-infringing. The entire risk as to the quality and performance of the Covered Software is with You. Should any Covered Software prove defective in any respect, You (not any Contributor) assume the cost of any necessary servicing, repair, or correction. This disclaimer of warranty constitutes an essential part of this License. No use of any Covered Software is authorized under this License except under this disclaimer.
7. Limitation of Liability

Under no circumstances and under no legal theory, whether tort (including negligence), contract, or otherwise, shall any Contributor, or anyone who distributes Covered Software as permitted above, be liable to You for any direct, indirect, special, incidental, or consequential damages of any character including, without limitation, damages for lost profits, loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses, even if such party shall have been informed of the possibility of such damages. This limitation of liability shall not apply to liability for death or personal injury resulting from such party’s negligence to the extent applicable law prohibits such limitation. Some jurisdictions do not allow the exclusion or limitation of incidental or consequential damages, so this exclusion and limitation may not apply to You.
8. Litigation

Any litigation relating to this License may be brought only in the courts of a jurisdiction where the defendant maintains its principal place of business and such litigation shall be governed by laws of that jurisdiction, without reference to its conflict-of-law provisions. Nothing in this Section shall prevent a party’s ability to bring cross-claims or counter-claims.
9. Miscellaneous

This License represents the complete agreement concerning the subject matter hereof. If any provision of this License is held to be unenforceable, such provision shall be reformed only to the extent necessary to make it enforceable. Any law or regulation which provides that the language of a contract shall be construed against the drafter shall not be used to construe this License against a Contributor.
10. Versions of the License
10.1. New Versions

Mozilla Foundation is the license steward. Except as provided in Section 10.3, no one other than the license steward has the right to modify or publish new versions of this License. Each version will be given a distinguishing version number.
10.2. Effect of New Versions

You may distribute the Covered Software under the terms of the version of the License under which You originally received the Covered Software, or under the terms of any subsequent version published by the license steward.
10.3. Modified Versions

If you create software not governed by this License, and you want to create a new license for such software, you may create and use a modified version of this License if you rename the license and remove any references to the name of the license steward (except to note that such modified license differs from this License).
10.4. Distributing Source Code Form that is Incompatible With Secondary Licenses

If You choose to distribute Source Code Form that is Incompatible With Secondary Licenses under the terms of this version of the License, the notice described in Exhibit B of this License must be attached.
Exhibit A - Source Code Form License Notice

    This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

If it is not possible or desirable to put the notice in a particular file, then You may include the notice in a location (such as a LICENSE file in a relevant directory) where a recipient would be likely to look for such a notice.

You may add additional accurate notices of copyright ownership.
Exhibit B - “Incompatible With Secondary Licenses” Notice

    This Source Code Form is “Incompatible With Secondary Licenses”, as defined by the Mozilla Public License, v. 2.0.
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
				book['metadata']['cover'] = {'type':'bmp','data':base64.b64encode(img_data).decode()}
			if img_type == 'png':
				book['metadata']['cover'] = {'type':'bmp','png':base64.b64encode(img_data).decode()}
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
			json.dump(book, fp=open(name+'.tb','w+'),default=set_default)
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
	def renderhtml(fn):
		file = open(fn,'r')
		d = json.loads(file.read())
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
		print(pages,cpages)
		render = '<html>\n\t'
		for i in range(len(pages)):
			if str(i+1) in cpages:
				render += '<h1>'+d['metadata']['ci'][str(i+1)]+'</h1>\n\t'
				render += '<div>\n\t'
			for t in d['bookdata'][pages[i]]['data']:
				if 'h' in t:
					render += '<h2>'+d['bookdata'][pages[i]]['data'][t]+'</h2>\n\t'
				if 'p' in t:
					render += '<p>'+d['bookdata'][pages[i]]['data'][t]+'</p>\n\t'
				if 't' in t:
					render += '<div>'+d['bookdata'][pages[i]]['data'][t]+'</div>\n\t'
			if str(i+2) in cpages:
				render += '</div>\n\t'
				render += '<div>Page ' + str(i+1) + ' of ' + str(len(pages)) + '</div>\n\t'
			elif cpages[i] == cpages[len(cpages)-1]:
				render += '</div>\n\t'
				render += '<div>Page ' + str(i+1) + ' of ' + str(len(pages)) + '</div>\n\t'
		render += '\b\b\b\b\b\b</html>'
		return render
	def rendermarkdown(fn):
		file = open(fn,'r')
		d = json.loads(file.read())
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
		print(pages,cpages)
		render = ''
		for i in range(len(pages)):
			if str(i+1) in cpages:
				render += '# '+d['metadata']['ci'][str(i+1)]+'  \n'
			for t in d['bookdata'][pages[i]]['data']:
				if 'h' in t:
					render += '## '+d['bookdata'][pages[i]]['data'][t]+'  \n'
				if 'p' in t:
					render += d['bookdata'][pages[i]]['data'][t]+'  \n'
				if 't' in t:
					render += d['bookdata'][pages[i]]['data'][t]+'  \n'
			if str(i+2) in cpages:
				render += '###### Page ' + str(i+1) + ' of ' + str(len(pages)) + '  \n'
			elif cpages[i] == cpages[len(cpages)-1]:
				render += '###### Page ' + str(i+1) + ' of ' + str(len(pages)) + '  \n'
		return render
	def renderxedoc(fn):
		file = open(fn,'r')
		d = json.loads(file.read())
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
		print(pages,cpages)
		render = ''
		for i in range(len(pages)):
			if str(i+1) in cpages:
				render += 'r a | '+d['metadata']['ci'][str(i+1)]+'  \n'
			for t in d['bookdata'][pages[i]]['data']:
				if 'h' in t:
					render += 'r b | '+d['bookdata'][pages[i]]['data'][t]+'  \n'
				if 'p' in t:
					render += 'r p | '+d['bookdata'][pages[i]]['data'][t]+'  \n'
				if 't' in t:
					render += 'r p | '+d['bookdata'][pages[i]]['data'][t]+'  \n'
			if str(i+2) in cpages:
				render += 'r f | Page ' + str(i+1) + ' of ' + str(len(pages)) + '  \n'
			elif cpages[i] == cpages[len(cpages)-1]:
				render += 'r f | Page ' + str(i+1) + ' of ' + str(len(pages)) + '  \n'
		return render
def update():
	global __version__
	if sys.version_info[0] < 3 and sys.version_info[1] < 5 and sys.version_info[2] < 9:
		raise Exception("Must be using Python 3.5 or above to use this function")
	print("Connecting to server")
	s = urllib.request.urlopen('https://tinybookdownload.sethedwards.repl.co/cv')
	dt = s.read().decode('utf-8')
	print("Connected")
	if dt != __version__:
		print("Updating Version...")
		s = urllib.request.urlopen('https://tinybookdownload.sethedwards.repl.co/')
	else:
		print("No updates available.")
		return
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
	print('\nGiving System a 15 second rest')
	time.sleep(15)
	file = open('README.md','w+')
	file.close()
	print('Giving System a 15 second rest to prevent freezing...')
	time.sleep(15)
	for i in range(0,len(data['readme'])):
		if round(((i+1)/len(data['readme']))*100) != op:
			print("\u001b[1000D\u001b[2KUpdating README",str(round(((i+1)/len(data['readme']))*100))+'%',end='',flush=True)
			op = round(((i+1)/len(data['readme']))*100)
		file = open('README.md','a')
		file.write(data['readme'][i])
		file.close()
		time.sleep(0.0001)
	ud = json.loads(data['example'])
	for i in ud['data']:
		if ud['data'][i]['action'] == '+d':
			try:
				os.mkdir(i)
			except:
				pass
		if ud['data'][i]['action'] == '-d':
			try:
				shutil.rmtree(i)
			except:
				pass
		if ud['data'][i]['action'] == '+':
			print("Editing/Adding File:",i)
			file = open(i,'w+')
			for c in range(0,len(ud['data'][i]['data'])):
				file = open(i,'a')
				file.write(ud['data'][i]['data'][c])
				if round(((c+1)/len(ud['data'][i]['data']))*100) != op:
					print("\u001b[1000D\u001b[2KUpdating",i,str(round(((c+1)/len(ud['data'][i]['data']))*100))+'%',end='',flush=True)
				op = round(((c+1)/len(ud['data'][i]['data']))*100)
				file.close()
				time.sleep(0.0001)
			print("File",i,"done")
			time.sleep(2)
		if ud['data'][i]['action'] == '-':
			print("Removing file:",i)
			try:
				os.remove(i)
			except:
				pass
			file.close()
		print('')