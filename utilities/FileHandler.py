from comtypes.client import CreateObject
import os


def convert_word_to_pdf(source, destination):
    wdFormatPDF = 17
    word = CreateObject('Word.Application')
    doc = word.Documents.Open(source)
    doc.SaveAs(destination, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


def delete_all_files_in_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
