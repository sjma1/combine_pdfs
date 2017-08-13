import os, PyPDF2

def get_file_select_mode():
    while True:
        select_mode = input("Get PDF locations individually or by directory (i/d): ")
        if select_mode.lower() == 'i' or select_mode.lower() == 'd':
            return select_mode
        print('INVALID INPUT, ENTER EITHER \'i\' or \'d\'!\n')

def get_directory():
    while True:
        directory = input("Enter the path of the directory the combined .pdf file will be placed in: ")
        if os.path.isdir(directory):
            return directory
        print('INVALID PATH\n')

def get_pdf_location():
    while True:
        pdf_path = input("Enter the path of a .pdf file or \'q\' to stop: ")
        if (os.path.isfile(pdf_path) and pdf_path.endswith('.pdf')) or pdf_path.lower() == 'q':
            return pdf_path
        print("INVALID INPUT, PATH MUST BE VALID AND END WITH .PDF\n")
        
def add_pdfs_from_directory(directory, pdf_writer):
    for item in os.listdir(directory):
        if os.path.isfile(item) and item.endswith('.pdf'):
            pdf_reader = PyPDF2.PdfFileReader(open(item, 'rb'))
            for page_num in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
    return pdf_writer
    