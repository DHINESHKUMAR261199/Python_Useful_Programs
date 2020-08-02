from PyPDF2 import PdfFileMerger
import os
m=PdfFileMerger()
l=os.listdir()
l=sorted(l)
for i in l:
    if i.endswith(".pdf"):
        m.append(i)

m.write("All_in_one.pdf")
m.close()
