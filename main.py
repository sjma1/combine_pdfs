#Seong Ma

import functions, os, PyPDF2

#Use pip to install PyPDF2 first


'''
This program will allow the user to either input a directory and create a new pdf
containing the contents of all pdf files in the directory or input individual pdf
file paths and then combine those into one pdf
'''


if __name__ == '__main__':
    while True:
        continue_search = input("Enter \'q\' to quit and anything else to continue: ")
        
        pdf_write = PyPDF2.PdfFileWriter()
        
        if continue_search.lower() == 'q':
            break
        
        new_pdf_location = functions.get_directory()
        os.chdir(new_pdf_location)
        
        select_mode = functions.get_file_select_mode()
        pdf_writer = PyPDF2.PdfFileWriter
        
        if select_mode == 'd':
            temp_dir = functions.get_directory()
            pdf_writer = functions.add_pdfs_from_directory(temp_dir, pdf_writer)
            
        else:
            pdf_locations = []
            while True:
                location = functions.get_pdf_location()
                if location.lower() == 'q':
                    break
                pdf_locations.append(location)
                
            for location in pdf_locations:
                pass

            