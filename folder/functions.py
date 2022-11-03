import pdfkit
import os, time
#import wkhtmltopdf

#pdfkit.configuration("C:\Program Files\wkhtmltopdf\bin")
#path_check = "C:\Program Files\wkhtmltopdf\\bin"
#if os.path.exists(path_check):
#    exec_path = path_check + "\wkhtmltopdf.exe"
#    if os.path.exists(exec_path):
#        conf = pdfkit.configuration(wkhtmltopdf=exec_path)
        #pdfkit.PDFKit("localhost:1234/fillform","url")

#else:
#    print("Psyc")


class Listener:
    def __init__(self, event):
        pass
    def onclickFunction(event):
        data_list = []
        if event is not None:
            data_list.append(event)
        return data_list 

class PdfConvert:
    def html_to_pdf(route, file_name):
        path =  "./resumes"
        if os.path.exists(path):
            pass
        else:
            os.mkdir("./resumes")
        pdfkit.from_url(f"{route}",f"./resumes/{file_name}.pdf" )#,configuration=conf)
    def delete_files(file_name):
        time.sleep(5)
        os.remove(f"./{file_name}.pdf")
        

