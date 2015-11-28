from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams,LTContainer,LTTextBox,LTText,LTImage
from pdfminer.converter import TextConverter
import re

pagenos = set()
caching = True
showpageno = False

infp = open('/tmp/test2.pdf', 'rb')
outfp = open('/tmp/test2refs.txt', 'w')

class RefsExtractor(TextConverter):

    def __init__(self, rsrcmgr, outfp, codec='utf-8', pageno=1, laparams=None,
                 showpageno=False, imagewriter=None):
        TextConverter.__init__(self, rsrcmgr, outfp, codec=codec, pageno=pageno, laparams=laparams)
        self.showpageno = showpageno
        self.imagewriter = imagewriter
        self.text = ''
        return

    def receive_layout(self, ltpage):
        def render(item):
            if isinstance(item, LTContainer):
                for child in item:
                    render(child)
            elif isinstance(item, LTText):
                self.text += item.get_text()
            if isinstance(item, LTTextBox):
                if re.search(r'^\[[0-9]+\] ',self.text) or \
                   re.search(r'^[A-Z][a-z]+, [a-zA-Z]\.',self.text):
                    TextConverter.write_text(self,self.text)
                TextConverter.write_text(self,'\n')
                self.text = ''
            elif isinstance(item, LTImage):
                if self.imagewriter is not None:
                    self.imagewriter.export_image(item)
        if self.showpageno:
            TextConverter.write_text(self,'Page %s\n' % ltpage.pageid)
        render(ltpage)
        TextConverter.write_text(self,'\f')
        return

rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = RefsExtractor(rsrcmgr, outfp, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in PDFPage.get_pages(infp, pagenos,
                              caching=caching,
                              check_extractable=True):
    interpreter.process_page(page)

infp.close()
outfp.close()
