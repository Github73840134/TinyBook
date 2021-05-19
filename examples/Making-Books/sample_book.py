import tinybook as bm
book = bm.makebook
md = book.metadata
md.version()
md.title("Testbook")
md.pages(1)
md.chapters({"1":"hi"})
book.add.page('1',{"h":"I told you",'p':"THIS is the hard way"})
book.make('test')