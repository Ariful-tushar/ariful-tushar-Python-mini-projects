from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2



output_file_name = input("Enter the pdf name where you want to save the watermark pdf: ")
inp_pdf = input ("Please enter the pdf file name where you want to add the water mark: ")
water_pdf = input ("Please enter the name of your water mark pdf: ")

def water_mark (folder_name, input_file_name, watermark_file_name):
    try:
        input_pdf = PyPDF2.PdfFileReader(open(f"pdf/{inp_pdf}.pdf", "rb"))
        wtr_pdf = PyPDF2.PdfFileReader(open(f"pdf/{water_pdf}.pdf", "rb"))
        output_pdf = PyPDF2.PdfFileWriter()

        for i in range(input_pdf.getNumPages()):
            page = input_pdf.getPage(i)
            page.mergePage(wtr_pdf.getPage(0))
            output_pdf.addPage(page)
            with open (f"pdf/{output_file_name}.pdf", "wb") as new_pdf:
                output_pdf.write(new_pdf)
        print ("Watermark added!")
    except:
        print (f"There is not any file named {inp_pdf} or {water_pdf}. Please enter a valid file name located inside the folder pdf")


water_mark (output_file_name, inp_pdf, water_pdf)
