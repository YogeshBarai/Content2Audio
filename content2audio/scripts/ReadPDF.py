import PyPDF2

class ReadPDF:
    def __init__(self, fname):
        self.fname = fname
        self.ftext = ''
    
    def parsefile(self):
        # Open File Object
        try:
            FileObj = open(self.fname,'rb')
        except Exception:
            print('File Not Found')
            exit()
        # Get PDFReader Obj
        ReaderObj = PyPDF2.PdfFileReader(FileObj)

        # Parse each page and get text
        for eachPageNum in range(ReaderObj.numPages):
            pageObj = ReaderObj.getPage(eachPageNum)
            self.ftext += pageObj.extractText()
        
        FileObj.close()
    
    def getText(self):
        return self.ftext


test = ReadPDF('.\content2audio\sample_files\sample.pdf')
test.parsefile()
text = test.getText()
print(text)

