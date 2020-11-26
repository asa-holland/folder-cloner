# folderCloner.py


# Used to open word files
import win32com.client as com

# Used to obtain the parent directory
from pathlib import Path, PurePosixPath

# Used for navigation
import os


def replace_string_contents(raw_string, renaming_dictionary):
    """
    Takes a string and replaces it with any changes provided in a renaming dictionary
    :param raw_string: a raw string with which to pass through the renaming dictioanary
    :param renaming_dictionary: a dictionary containing keys to be replaced with their associated values
    :return: string identical to the raw string provided with all changes made based on the renaming dictionary
    """

    # Renames a string using a provided renaming dictionary
    replacement_string = raw_string

    # Iterate over keys in renaming dictionary
    for key in renaming_dictionary:

        # For any keys found in the provided string, replace them using the value of the provided dictionary for that key
        if key in replacement_string:
            replacement_string = replacement_string.replace(key, renaming_dictionary[key])

    # return the modified string
    return replacement_string



def document_replace(current_word_app, target_string, replacement_string):
    """
    Replaces a single string in an open word document with a replacement string.
    :param current_word_app: Takes a currently running com Word Application
    :param target_string: Takes a string to search for matches in a word document
    :param replacement_string: Takes a string to replace in the word document, based on occurances of the target_string
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
    """
    Process a single document in the current folder. If it is a word document, 
    make all replacements based on the replacement dictionary and create a renamed copy of the file in the provided cloned directory.
    :param word_app: Takes a currently running com Word Application
    :param filename: Takes the string representing the current filename being opened
    :param replacement_dictionary: Takes a dictionary of key value pairs such that keys are strings that are to be removed from the original file and replaced with the provided dictionary values.
    :param cloned_directory: Takes the path of the cloned directory in which to place the newly cloned files
    """

    # If the current file is word file, perform the necessary replacements for text

    if (filename.endswith('.doc') or filename.endswith('.docx')) and '~$' not in filename:

        # Save the current working directory (the original folder)
        original_working_dir = os.getcwd()

        # Create a new filename (without the original extension) using the replacement string 
        original_filename = filename.split('.doc')[0]
        new_filename = replace_string_contents(raw_string=original_filename, renaming_dictionary=replacement_dictionary)

        # add the document type
        new_filename_with_ext = ''.join([new_filename, '.doc'])

        # Create a variable for the original file (the one we will be cloning)
        original_doc_path = os.path.join(original_working_dir, filename)

        # Open the original document
        original_doc = word_app.Documents.Open(original_doc_path)

        # Save a copy of the original file as a clone in the cloned directory
        cloned_file_path = os.path.abspath(cloned_directory + '\\' + new_filename_with_ext)

        # In some cases, word believes that the cloned_file_path is already open.
        # This try except block ensures that the cloned file is closed before continuing
        try:
            cloned = word_app.Documents.Open(cloned_file_path)
            cloned.Close()
        except BaseException as e: # To catch situation where cloned file has not been created
            pass
            #print('An error occurred:', e.args)

        # FileFormat code 0 saves as .doc
        original_doc.SaveAs(cloned_file_path, FileFormat=0) #ERROR

        # Close the original file
        original_doc.Close()

        # Navigate to the cloned directory
        os.chdir(cloned_directory)

        # open the cloned file from the cloned directory
        cloned_doc = word_app.Documents.Open(cloned_file_path)

        # Iterate over the keys of the replacement dictionary
        for key in replacement_dictionary:

            # For each key of the replacement dictionary, perform the replacement in the cloned document
            document_replace(current_word_app=word_app, target_string=key, replacement_string=replacement_dictionary[key])

        # Close the cloned file
        cloned_doc.Close()

        # Return to the original folder
        os.chdir(original_working_dir)

    else:
        print(f'{filename} is not a Word document and was not processed.')


def cloneFolder(word_application, directory_to_clone, replacement_dictionary):
    """
    Creates a clone of a directory in the parent directory by replacing text content of all files based on a replacement_dictionary
    :param directory_to_clone: Takes a path of a directory to clone.
    :param replacement_dictionary: Takes the dictionary of all replacments needed to be made on a single folder
    """

    # Change the current directory to the provided directory (the folder to clone)
    os.chdir(directory_to_clone)

    # Create a new folder in the parent directory using a new name provided by the replacment dictionary
    # Obtain the original folder name as a string
    original_folder_name = str(PurePosixPath(directory_to_clone)).replace('\\', '')

    # Create a cloned folder name by using the replacement dictionary to rename as needed
    cloned_folder_name = replace_string_contents(raw_string=original_folder_name, renaming_dictionary=replacement_dictionary)

    # Obtain the parent directory of the current directory to clone
    parent_directory = str(Path(directory_to_clone).parent)

    # Create a new folder using the cloned folder name inside the parent directory
    # cloned_directory_path = os.path.join(parent_directory, cloned_folder_name)
    # os.makedirs(cloned_directory_path, exist_ok=True)

    os.chdir(parent_directory)

    new_directory = Path.cwd() / cloned_folder_name
    new_directory.mkdir(exist_ok=True)

    cloned_directory_path = str(new_directory)

    # Change back into the directory we want to clone
    os.chdir(directory_to_clone)

    # Iterate over files in the directory to clone
    for file in os.listdir("."):
        process_document(word_app=word_application, filename=file, replacement_dictionary=replacement_dictionary, cloned_directory=cloned_directory_path)

    # Let the user know the clone has been complete
    print(f'...{directory_to_clone} has successfully been cloned into {cloned_directory_path}.')


