
# Used to open word files
import win32com.client as com

# Used to obtain the parent directory
from pathlib import Path

# Used for replacing string function
from utils import file_processing

# Used for navigation
import os


def document_replace(current_word_app, target_string, replacement_string):
    """

    :param current_word_app: 
    :param target_string: 
    :param replacement_string:
    :return: 
    """

    # TODO: currently has two issues, maintains case of previous text and does not change within tables


    # Sets up some numerical option paramaters
    wrap_value = 1
    wd_replace_all_value = 2
    
    # Find and Replace the provided target_string with the replacement_string inside the current_document
    current_word_app.Selection.Find.Execute(
        FindText=target_string, 
        MatchCase=False, 
        MatchWholeWord=False, 
        MatchWildcards=False, 
        MatchSoundsLike=False, 
        MatchAllWordForms=False, 
        Forward=True, 
        Wrap=wrap_value, 
        Format=False, 
        ReplaceWith=replacement_string, 
        Replace=wd_replace_all_value)

    # Make the same replacement in headers and footers
    doc = current_word_app.ActiveDocument

    # iterate through all sections of the document
    sections = doc.Sections
    for section in sections:

        # Make replacement in headers
        headersCollection = section.Headers
        for header in headersCollection:
            header.Range.Find.Execute(
                FindText=target_string, 
                MatchCase=False, 
                MatchWholeWord=False, 
                MatchWildcards=False, 
                MatchSoundsLike=False, 
                MatchAllWordForms=False, 
                Forward=True, 
                Wrap=wrap_value, 
                Format=False, 
                ReplaceWith=replacement_string, 
                Replace=wd_replace_all_value)

        # make replacement in footers
        footersCollection = section.Footers
        for footer in footersCollection:
            footer.Range.Find.Execute(
                FindText=target_string, 
                MatchCase=False, 
                MatchWholeWord=False, 
                MatchWildcards=False, 
                MatchSoundsLike=False, 
                MatchAllWordForms=False, 
                Forward=True, 
                Wrap=wrap_value, 
                Format=False, 
                ReplaceWith=replacement_string, 
                Replace=wd_replace_all_value)

def process_document(word_app, filename, replacement_dictionary, cloned_directory):

    # If the current file is word file, perform the necessary replacements for text

    if filename.endswith('.doc') or filename.endswith('.docx'):

        # Save the current working directory (the original folder)
        original_working_dir = os.getcwd()

        # Create a new filename (without the original extension) using the replacement string 
        original_filename = filename.split('.doc')[0]
        new_filename = file_processing.replace_string_contents(raw_string=original_filename, renaming_dictionary=replacement_dictionary)

        # Create a variable for the original file (the one we will be cloning)
        original_doc_path = os.path.join(original_working_dir, filename)

        # Open the original document
        original_doc = word_app.Documents.Open(original_doc_path)
        print('--- opened', filename)

        # Save a copy of the original file as a clone in the cloned directory
        # FileFormat code 0 saves as .doc
        cloned_file_path = os.path.abspath(cloned_directory +'\\' + new_filename)

        print('os.listdir():', os.listdir())
        print('cloned_file_path:', cloned_file_path)

        # In some cases, word believes that the cloned_file_path is already open.
        # This try except block ensures that the cloned file is closed before continuing
        try:
            cloned = word_app.Documents.Open(cloned_file_path)
            cloned.Close()
        except BaseException as e: # To catch situation where cloned file has not been created
            print('An error occurred:', e.args)

        original_doc.SaveAs(cloned_file_path, FileFormat=0) #ERROR
        print('--- saved', filename, 'into', cloned_file_path)

        # Close the original file
        original_doc.Close()
        print('--- closed', filename)

        # Navigate to the cloned directory
        os.chdir(cloned_directory)

        # open the cloned file from the cloned directory
        cloned_doc = word_app.Documents.Open(cloned_file_path)
        print('--- opened', cloned_file_path)

        # Iterate over the keys of the replacement dictionary
        for key in replacement_dictionary:

            # For each key of the replacement dictionary, perform the replacement in the cloned document
            document_replace(current_word_app=word_app, target_string=key, replacement_string=replacement_dictionary[key])

        # Close the cloned file
        cloned_doc.Close()
        print('--- closed', cloned_file_path)

        # Return to the original folder
        os.chdir(original_working_dir)

    else:
        print(f'{filename} is not a word document and was not processed.')


def cloneFolder(word_application, directory_to_clone, replacement_dictionary):

    """
    Creates a clone of a directory in the parent directory by replacing text content of all files based on a replacement_dictionary
    """
    print(f'Cloning {directory_to_clone}...')

    # Change the current directory to the provided directory (the folder to clone)
    os.chdir(directory_to_clone)

    # Create a new folder in the parent directory using a new name provided by the replacment dictionary
    # Obtain the original folder name as a string
    original_folder_name = directory_to_clone.split('\\')[-1]
    print('original_folder_name', original_folder_name)

    # Create a cloned folder name by using the replacement dictionary to rename as needed
    cloned_folder_name = file_processing.replace_string_contents(raw_string=original_folder_name, renaming_dictionary=replacement_dictionary)
    print('cloned_folder_name', cloned_folder_name)

    # Obtain the parent directory of the current directory to clone
    parent_directory = Path(directory_to_clone).parent

    # Create a new folder using the cloned folder name inside the parent directory
    cloned_directory_path = os.path.join(parent_directory, cloned_folder_name)
    os.makedirs(cloned_directory_path, exist_ok=True)

    print('Transfering files to cloned folder...')
    # Iterate over files in the directory to clone
    for file in os.listdir("."):
        process_document(word_app=word_application, filename=file, replacement_dictionary=replacement_dictionary, cloned_directory=cloned_directory_path)

    # Let the user know the clone has been complete
    print(f'...{directory_to_clone} has successfully been cloned into {cloned_directory_path}.')


