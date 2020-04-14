from pathlib import Path
from datetime import datetime
from shutil import copyfile
from utilities.FileHandler import *
from utilities.Variables import *


def get_latest_resume():
    resources_dir = os.path.join(Path(__file__).parent.parent, "resources")
    delete_all_files_in_folder(resources_dir)
    latest_resume_filepath = job_hunt_dir + resume_file_name + DOCX_EXTN
    resources_resume_word_filepath = os.path.join(resources_dir, resume_file_name + DOCX_EXTN)
    copyfile(latest_resume_filepath, resources_resume_word_filepath)
    resources_resume_pdf_filepath = os.path.join(resources_dir,
                                                 resume_file_name + datetime.now().strftime("_%Y%m%d") + PDF_EXTN)
    convert_word_to_pdf(resources_resume_word_filepath, resources_resume_pdf_filepath)
    return resources_resume_pdf_filepath


