import PyPDF2
from gtts import gTTS
import os

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

    def convert2Audio(self, text, language="en" ):
        tts = gTTS(text=text, lang=language)
        tts.save("output.mp3")
        os.system(f'open {"output.mp3"}')




test = ReadPDF('.\content2audio\sample_files\sample.pdf')
test.parsefile()
text = test.getText()
print(text)
test.convert2Audio(text)

