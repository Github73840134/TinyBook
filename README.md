# TinyBook Documentation
Version 1.0-Python 3 edition


## Requirements:
- A complete install Python 3 or newer
## Tinybook info
- Latest Metadata Version is 1.0
# Table of contents
[1.What is TinyBook](##What-is-TinyBook)  
[2.How to use the Library](#How-to-use-the-library)  
[3.Reading Books]()

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
Any metadata object that is called will create the metadata atrribute of the book f it hasnt been added already
#### title(title)
Adds a title to the book  
title must be a string  
Sugested Usage:
```python
bm = tinybook.makebook
md = bm.metadata
md.title('Book Title')
```
All-in-one-go usage:
```python
tinybook.makebook.metadata.title('Boook Title')
```
#### version(ver)
Sets the book metadata verson  
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
Refer to [The Chapter Format](##The-Chapter-Format) for doing it the less easy way  
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
'png' Portable Network Graphics (.png) File    
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
Refer to [The Page Format](##The-Page-Format) for doing it the less easy way  
Sugested Usage:
```python
c = {'h':'This is is a heading','t':'thiss is text'}
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
name msut be str (do not add extention to the file name)  
Use this when you have compelted making your book
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
Returns the books title as a string
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
## Getting Chapter Info
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
bm = tinybook.Book
info = bm.info
chap = info.chapters
chap.total('testbook.tb')
```
All-in-one-go usage:
```python
tinybook.Book.info.chapters.total('testbook.tb')
```
# The Generator
