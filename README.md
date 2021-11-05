# TinyBook Documentation
Version 1.0.4-Python 3 edition

# IMPORTANT MAJOR BUG
tinybook.read.read() is flakey when returning its data properly. We are working on this issue right now. We haven't abandoned this!
## Requirements:
- A complete install Python 3 or newer
### A quick side note this may work 2.7.18 and above, I have not tested it.
## Tinybook info
- Latest Metadata Version is 1.0
## Release Notes
- Added self updating \(Only works on python 3.5.9 and above\)
- Added book reading in html.  
- Added book reading in markdown.
# Table of contents
[1:What is TinyBook](#What-is-TinyBook)  
[2:How to use the library](#How-to-use-the-library)  
[3:Making Books](#Making-Books)  
[4:Metadata](#metadata)  
[5:Making Pages](#Making-Pages)  
[6:Making the book](#Making-the-book)  
[7:Gathering book info](#Gathering-book-info)  
[8:Gathering chapter info](#Gathering-chapter-info)  
[9:Reading Books](#Reading-Books)  
[10:The Generator](#The-Generator)  
[11:Generating Pages](#Generating-Pages)  
[12:Generating Chapters](#Generating-Chapters)  
[13:The Format](#The-Format)  
[14:How It Works](#How-it-works)  
[15:The metadata attributes](#The-metadata-attributes)  
[16:The ver attribute](#The-ver-attribute)  
[17:The title attribute](#The-title-attribute)  
[18:The pages attribute](#The-pages-attribute)  
[19:The ci attribute](#The-ci-attribute)  
[20:The cover attribute (BETA)](#The-cover-attribute-(BETA))  
[21:The bookdata attributes](#The-bookdata-attributes)  
[22:The pages attribute](#The-page-format)  
[23:The metadata attribute (Coming soon)](#The-metadata-attribute)  
[24:The data attributes](#The-data-attributes)  
[25:The h attribute](#The-h-attribute)  
[26:The p attribute](#The-p-attribute)  
[27:The t attribute](#The-t-attribute)  
[28:Examples](#Examples)  
[29:A Testbook](#A-Testbook)  
[30:Plans for the future](#Plans-for-the-future)  
[31:Feature Updates](#Feature-Updates)  
[32:Updating the library](#Updating-the-library)  
[33:Porting](#Porting)  
[34:License](#License)
# What is TinyBook
Tiny book is a ebook format thats meant ot be small and work across multiple platforms. It strives to beat the ebook format

# How to use the library
```python
import tinybook
```
# Making Books
## Metadata
```python
tinybook.makebook.metadata
```
Any metadata object that is called will create the metadata attribute of the book if it hasnt been added already
#### title(title)
Adds a title to the book  
title must be a string  
Sugested Usage:
```python
bm = tinybook.makebook
md = bm.metadata
md.title('Abbreviations of today')
```
All-in-one-go usage:
```python
tinybook.makebook.metadata.title('Abbreviations of today')
```
#### version(ver)
Sets the book metadata version  
At this time there is only one version (1.0)
version must be int  
Sugested Usage:
```python
bm = tinybook.makebook
md = bm.metadata
md.ver(1.0)
```
All-in-one-go usage:
```python
tinybook.makebook.metadata.version(1.0)
```
#### chapters(chap_info)
Adds chapters to the book  
chap_info must be a tinybook dict  
Refer to the [Generator Class](#The-Generator) for easy generation of chapters.
Refer to [The Chapter Format](##The-ci-attribute) for doing it the less easy way  
Sugested Usage:
```python
chaps = {'1':'This si a test'}
bm = tinybook.makebook
md = bm.metadata
md.chapters(chaps)
```
All-in-one-go usage:
```python
tinybook.makebook.metadata.chaps({'1':'This si a test'})
```
#### pages(page_num)
Adds number of pages to the book  
page_num must be an int  
The page_num should be total amount of pages in the book
Sugested Usage:
```python
bm = tinybook.makebook
md = bm.metadata
md.pages(1)
```
All-in-one-go usage:
```python
tinybook.makebook.metadata.pages(1)
```
#### cover(img_data,img_type)
Adds a cover image to the book  
img_dta must be ascii encoded bytes  
img_type must be string  
img_type options:    
'bmp' Bitmap file  
'png' Portable Network Graphics (.png) file    
Sugested Usage:
```python
file = open('test.bmp','rb')
data = file.read()
file.close()
bm = tinybook.makebook
md = bm.metadata
md.cover(data,'bmp')
```
All-in-one-go usage:
```python
tinybook.makebook.metadata.cover(open('test.bmp','rb').read(),'bmp')
```
## Making Pages
```python
tinybook.makebook.add
```
#### page(page_num, data)
Adds a page to the book 
page_num must be an int   
data must be a tinybook dict  
Refer to the [Generator Class](#The-Generator) for easy generation of chapters.
Refer to [The Page Format](###The-page-format) for doing it the less easy way  
Sugested Usage:
```python
c = {'h':'This is is a heading','t':'this is text'}
bm = tinybook.makebook
md = bm.add
md.page(1,c)
```
All-in-one-go usage:
```python
tinybook.makebook.add.page(1,{'h':'This is is a heading','t':'thiss is text'})
```
## Making the book
```python
tinybook.makebook
```
#### make(bookname)
Compile the book to a tinybook file  
name must be str (do not add an extention to the file name)  
Use this when you have completed making your book
Sugested Usage:
```python
bm = tinybook.makebook
bm.make('testbook')
```
All-in-one-go usage:
```python
tinybook.makebook.make('testbook')
```
# Gathering book info
```python
tinybook.Book.info
```
#### title(fn)
Get the title from the book file  
fn must be a string  
Returns the book's title as a string
Sugested Usage:
```python
bm = tinybook.Book
info = bm.info
info.title('testbook.tb')
```
All-in-one-go usage:
```python
tinybook.Book.title('testbook.tb')
```
#### pages(fn)
Get the total amount of pages from the book file  
fn must be a string  
Returns the amount of pages as an int  
Sugested Usage:
```python
bm = tinybook.Book
info = bm.info
info.pages('testbook.tb')
```
All-in-one-go usage:
```python
tinybook.Book.pages('testbook.tb')
```
## Getting chapter Info
```python
tinybook.Book.info.chapters
```
#### list(fn)
Gets a list of the chpaters names  
fn must be a string  
Returns the chapter titles as a list
Sugested Usage:
```python
bm = tinybook.Book
info = bm.info
chap = info.chapters
chap.list('testbook.tb')
```
All-in-one-go usage:
```python
tinybook.Book.info.chapters.list('testbook.tb')
```
#### total(fn)
Gets total chapters in book 
fn must be a string  
Returns the amount of chapters as an int
Sugested Usage:
```python
bm = tinybook.Book
info = bm.info
chap = info.chapters
chap.total('testbook.tb')
```
All-in-one-go usage:
```python
tinybook.Book.info.chapters.total('testbook.tb')
```
# Reading Books
```python
tinybook.read
```
#### read(fn)
Gets book contents
fn must be a string  
Returns the content of the book in a list
There are 3 levels in the list
Sugested Usage:
```python
bm = tinybook.read
f = bm.read('testbook.tb')
```
All-in-one-go usage:
```python
tinybook.read.read('testbook.tb')
```
#### term_ready(fn,offset)
Gets book contents and makes it sutible for terminal reading
fn must be a string
offset is optional  
offset is used in case the width of the dividing lines is too high or too low (The width is gathered from your terminal size) a negative number will remove x amount of the dividing lines and a positive number will add x amount to the dividing line  
Returns the content of the book
There are 3 levels in the list
Sugested Usage:
```python
bm = tinybook.read
f = bm.read('testbook.tb')
```
All-in-one-go usage:
```python
tinybook.read.read('testbook.tb')
```
#### renderhtml(fn)
Renders your book as an html file.  
fn must be a string  
Returns contents of book in stringed html
#### rendermarkdown(fn)
Renders your book as an markdown file.  
fn must be a string  
Returns contents of book in stringed markdown
# The Generator
The generator class is used for easy generation of tinybook formated data.  
```python
tinybook.Generator.generate
```
## Generating Pages
#### heading(text,idn)
Generates a heading object  
text must be a string  
idn must be a string  
idn is a optional id for elements
We recommend using idn when you have multiple instances of the same element  
e.g.  
```python
gen = tinybook.Generator.generate.page
f = gen.heading("Heading",'1')
fe = gen.heading("Heading","2")
```
Returns tinybook formated data
Sugested Usage:
```python
bm = tinybook.Generator
gen = bm.generate.page
page_1_0 = gen.heading('Helpful Heading')
```  
All-in-one-go usage:
```python
tinybook.Generator.generate.page.heading('Heading')
```  
or a paragraph  
```python
bm = tinybook.Generator
gen = bm.generate
page_1_0 = gen.heading('Helpful Heading',idn='1')
```  
All-in-one-go usage:
```python
tinybook.Generator.generate.page.heading('Heading',idn='1')
```
#### paragraph(text,idn)
Generates a paragraph object  
text must be a string  
idn must be a string  
idn is a optional id for elements
We recommend using idn when you have multiple instances of the same element  
e.g.  
```python
gen = tinybook.Generator.generate.apge
f = gen.paragraph("paragraph",'1')
fe = gen.paragraph("paragraph","2")
```
Returns tinybook formated data
Sugested Usage:
```python
bm = tinybook.Generator
gen = bm.generate.page
page_1_0 = gen.paragraph('paragraph')
```  
All-in-one-go usage:
```python
tinybook.Generator.generate.page.paragraph('Paragraph')
```  
or if you want multiple elements  
```python
bm = tinybook.Generator
gen = bm.generate.page
page_1_0 = gen.paragraph('Paragraph',idn='1')
```  
All-in-one-go usage:
```python
tinybook.Generator.generate.page.paragraph('Paragraph',idn='1')
```
#### paragraph(text,idn)
Generates a text object  
text must be a string  
idn must be a string  
idn is a optional id for elements
We recommend using idn when you have multiple instances of the same element  
e.g.  
```python
gen = tinybook.Generator.generate.page
f = gen.text("text",'1')
fe = gen.text("text","2")
```
Returns tinybook formated data
Sugested Usage:
```python
bm = tinybook.Generator
gen = bm.generate.page
page_1_0 = gen.text('text')
```  
All-in-one-go usage:
```python
tinybook.Generator.generate.page.text('text')
```  
or if you want multiple elements  
```python
bm = tinybook.Generator
gen = bm.generate.page
page_1_0 = gen.text('text',idn='1')
```  
All-in-one-go usage:
```python
tinybook.Generator.generate.page.text('text',idn='1')
```
#### join(data)
Joins text data into tinybook dict that can be used as a page.  
data must be a list of generated book elements dict's  
Returns tinybook generated data
Sugested Usage:
```python
bm = tinybook.Generator
pages = dm.generate.page

pages.join([tinybook generated data,tinybook generated data])
```
All-in-one-go usage:
```python
tinybook.Generator.generate.page.join([tinybook generated data,tinybook generated data])
```
## Generating Chapters
```python
tinybook.Generator.generate.chapters
```
#### make(data)
Makes a tinybook compatible chapter list  
Chapters must be a list and be in the following format
Chapters should be in a list each item being a string.  
The page number should be the page the chapter starts on  
The chapter title should be a string
```python
[[page_number,chapter_title]]
```
or  
```python
[['1','A brand new chapter']]
```
```python
bm = tinybook.Generator
chaps = dm.generate.chpaters
chap = [[page_number,chapter_title]]
pages.make(chaps)
```
All-in-one-go usage:
```python
tinybook.Generator.generate.chapters([page_number,chapter_title])
```
# Updating the library
```python
tinybook.update()
```
Use this command to update the library and readme  
*This only works with python version 3.5.9 and above*
# The Format
The formats tinybooks are written in are nothing special, It just a json file. It's contents however are different.

In this chapter of the documentation we will go over on how the format is made and used.  
Cool thing, this documentation will be made in a tinybook format soon


## How it works

Tinybook files are json files with a different extention.
  
This is what a tiny book file looks like
```json
{"metadata": {"ver": "1.0", "title": "Testbook", "pages": "1", "ci": {"1": "A Test"}, "cover": {"type": "", "cover": ""}}, "bookdata": {"1": {"metadata": {}, "data": {"h1": "This is a heading", "p": "This is a paragraph", "t": "This is text"}}}}
```
A Clearer way  
```json
{
	"metadata": {
		"ver": "1.0",
		"title": "Testbook",
		"pages": "1",
		"ci": {
			"1": "A Test"
		}, 
		"cover": {
			"type": "",
			"cover": ""
		}
	}, 
	"bookdata": {
		"1": {
			"metadata": {
			}, 
			"data": {
				"h1": "This is a heading", 
				"p": "This is a paragraph", 
				"t": "This is text"
			}
		}
	}
}
```
Lets break this down,  

## The metadata attributes
```json
"metadata": {
		"ver": "1.0",
		"title": "Testbook",
		"pages": "1",
		"ci": {
			"1": "A Test"
		}, 
		"cover": {
			"type": "",
			"cover": ""
		}
	}
```
### The ver attribute
```json
"ver": "1.0"
```
The version attribute lets the application know what version of tinybook the file was written in  
At this point there is only one version (1.0)

### The title attribute
```json
"title": ""
```
The title attribute is the name (title of the book)

### The pages attribute
```json
"pages": ""
```
The pages attribute tells the application how many pages total are in the book

### The ci attribute
```json
"ci": {}
```
The ci attribute tells the application what page and what the title page starts on.  
For instance:  
If Chapter 1 starts on page 1 and the name is "A New Chapter" in the tinybook format within the ci attribute it would look like
```json
"ci": {"1":"A New Chapter"}
```
add a comma and a space after that if you want to add more chapters, Then to add more do the same thing.  
Here is a ci attribute with more than one chapter
```json
"ci": {"1":"A New Chpater", "2":"A Whole New Chapter"}
```
Easy!  
### The cover attribute (BETA)
```json
"cover": {"type":"", "cover":""}
```
The cover attribute gives the application a cover page to show on a book selection screen, and while book data is being parsed before it can be read.  
The cover "type:" attribute tells the application whether the cover image is a Bitmap file, or a PNG file.  
The cover "cover:" attribute is the data of the png file as a string

Thats all for the Metadata attribute, now...

## The bookdata attributes
```json
"bookdata": {
		"1": {
			"metadata": {
			}, 
			"data": {
				"h1": "This is a heading", 
				"p": "This is a paragraph", 
				"t": "This is text"
			}
		}
	}
```
### The page format
To begin a page in the bookdata attribute you would do
```json
"1":{}
```
The key in the pair being the page number  
The value in the pair being the data in the book
#### The metadata attribute
(Not in use currently)  
This will be used for custom page styling. (Coming Soon)

#### The data attributes
The data attributes contain the content of the page in the book
```json
"data": {}
```
##### The h attribute
```json
"h": "Heading"
```
The heading attribute tells the application that this parts of text is a heading.  
If you want to you add multiple headings to the page add extra characters after the h to differenciate the headings, if you dont, the last instance of the headings with the same key 'h', will become the first heading, An Example:  
```json
"data":{"h":"Heading","h":"Another Heading"}
```
The first heading result in:  
```
Another Heading
```  
But if you add characters to the second one:  
```json
"data":{"h":"Heading","h2":"Another Heading"}
```
The first heading will result in:  
```
Heading
```
##### The p attribute
```json
"p": "paragraph"
```
The paragraph attribute tells the application that this parts of text is a paragraph.  
If you want to you add multiple paragraphs to the page add extra characters after the h to differenciate the paragraphs, if you dont, the last instance of the paragraphs with the same key 'p', will become the first paragraph, An Example:  
```json
"data":{"p":"paragraph","p":"Another paragraph"}
```
The first paragraph result in:  
```
Another paragraph
```  
But if you add characters to the second one:  
```json
"data":{"p":"paragraph","p2":"Another paragraph"}
```
The first paragraph will result in:  
```
paragraph
```
##### The t attribute
```json
"t": "text"
```
The text attribute tells the application that this parts of text is a text.  
If you want to you add multiple texts to the page add extra characters after the 't' to differenciate the texts, if you dont, the last instance of the texts with the same key 't', will become the first text, An Example:  
```json
"data":{"t":"text","t":"Another text"}
```
The first text result in:  
```
Another text
```  
But if you add characters to the second one:  
```json
"data":{"t":"text","t2":"Another text"}
```
The first text will result in:  
```
text
```
# Examples
You can find examples in the examples folder
Copy and paste the code in the examples to your current directory
# A Testbook
A test book file is included in the repository.  
# Plans for the future
## Feature Updates
- Adding ability to style page elements.
- Adding ability to add images to pages.
- Fixing term_ready() command
- More PORTS
- HTML rendering
## Porting:
In order of importance
- Micropython (Active
- Rust (Paused)
- C/C++ (Paused)
- Javascript (Waiting...)
- Java (Waiting...)
# License
*Also available in the library with tinybook.\_\_license\_\_*

©2021 Seth Edwards
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
# You have made it to the end of the documentation!
Happy Reading and Bookmaking!  

This book was produced by typing on keyboards  

©2021 Seth Edwards
