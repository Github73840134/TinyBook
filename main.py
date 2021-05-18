import tinybook as bm
book = bm.makebook
md = book.metadata
md.version()
md.title("Testbook")
gen = bm.Generator.generate
c = gen.chapters.make([['1',"A Test"]])
page = gen.page.heading('This is a heading','1')
page2 = gen.page.paragraph('This is a paragraph')
page3 = gen.page.text('This is text','')
md.pages(1)
fe = gen.page.join([page,page2,page3])
md.chapters(c)
book.add.page(1,fe)
book.make('testbooki')

print(bm.read.read('testbooki.tb'))