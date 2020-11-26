# main.py

# import local dependencies to run Microsoft Word and process changes to duplicated files
from components import com_word, folderCloner


def clone_folder(directory, replacement_dict_list):
	"""
	Clones the folder in the provided directory by making changes based on the provided replacement_dictionary.
	:param directory:
	:replacement_dict_list: A list of dictionaries, each dictionary consisting of keys of terms that are to be
	 replaced by their corresponding values in all word documents contained in the directory provided to clone.  
	"""

	# output to user
	print('Cloning', directory, '...')

	# Start an application of Word on the current system
	word = com_word.start_word()

	# Iterate over the dictionary in the replacement list
	for file_dict in replacement_dict_list:
		
		# For each replacement dictionary, run the folder cloner using the current word applicatoin, the sample directory, and the provided replacement dictionary
		folderCloner.cloneFolder(word_application=word, directory_to_clone=directory, replacement_dictionary=file_dict)

	# When all dictioanries have been processed, close word and end script
	com_word.close_word(word)

	# output to user
	print('Process completed.')
