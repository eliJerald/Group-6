import os
import shutil
import time
import json

def get_file_creation_time(filepath):
    """Returns the creation time of a file in human-readable format."""
    return time.ctime(os.path.getctime(filepath))

def determine_language(path):
    """Determines the programming language based on the directory structure."""
    lang_char = path.split('/')[-4][0]  # Extracts the first letter of the directory (e.g., 'B' or 'A')
    return 'CS' if lang_char == 'B' else 'C' if lang_char == 'A' else 'Unknown'

def extract_metadata(path):
    """Extracts metadata (year, course, assignment, student ID) from the file path."""
    parts = path.split('/')
    #vvvv path example vvvv
    #rosale5@gpu.cs.unlv.edu:/data/src/B2016/Z1/Z1/student9999.cpp 
    #          [0]           / [1]/[2]/[3]  /[4]/[5]/[6]
    
    student_file = parts[-1]  # e.g., 'student9999.cpp'
    student_id = student_file.split('t')[2].replace('.cpp', '')  # Extracts ID from 'student9999.cpp' -> '9999'

    assignment = f"Assignment {parts[-2][1]}"  # e.g., 'Assignment 1'
    course = parts[-3]  # e.g., 'Z1'
    year = parts[-4].split('B')[1]  # Extracts year from 'B2016'

    return [year, course, assignment, student_file, student_id] #in a list

def determine_term(creation_time):
    """Determines the academic term based on the file creation month."""
    month = creation_time.split(' ')[1]
    term_mapping = {
        "Jan": "Spr", "Feb": "Spr", "Mar": "Spr", "Apr": "Spr", "May": "Spr",
        "Jun": "Summ", "Jul": "Summ",
        "Aug": "Wint", "Sep": "Wint", "Oct": "Wint", "Nov": "Wint", "Dec": "Wint"
    }
    return term_mapping.get(month, "Unknown Term")

def copy_and_rename_file(src_path, dest_dir, student_name):
    """Copies a file to the destination and renames it to 'main.cpp'."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    if os.path.isfile(src_path):
        new_file_path = os.path.join(dest_dir, 'main.cpp')
        shutil.copy(src_path, new_file_path)
        print(f"Copied {src_path} to {new_file_path}")
        return new_file_path
    return None

def copy_files(paths, dest_dir, section_num, prof_name, student_name, student_dict):
    """Main function to process and copy student files while structuring the output folder."""
    for path in paths:
        lang = determine_language(path)
        year, course, assignment, student_file, student_id = extract_metadata(path)
        term = determine_term(get_file_creation_time(path))

        output_folder = os.path.join(dest_dir, lang, f"CS 135 {section_num} - {year} {term} - {assignment}")
        copied_file = copy_and_rename_file(path, output_folder, student_name)

        if copied_file:
            new_student = {
                "id": student_id,
                "name": student_name,
                "term": term,
                "course": "CS 135",
                "section": section_num,
                "prof": prof_name
            }
            student_dict["Students"].append(new_student)
