# clone_test.py

# imported main function to run a sample test using a real folder of files and sample data
import main

# import pathlib to handle paths
from pathlib import Path

# import os to handle folder navigation
import os

# Sample replacement dictionary list. Thie list contains dictionaries, each dictionary consisting of key value pairs using the following system:
	# key: the term that will be replaced from the original file
	# value: the replacement term that will be found in the updated replacement file
rep_list = [
	{'Ipsum': 'Python\'s Something Completely Different', 'Lorem': 'Monty ', '123': 'foobar'}, 
	{'Ipsum': 'Python\'s Life of Brian', 'Lorem': 'Monty', '123': 'barbar'},
	{'Ipsum': 'Python\'s Holy Grail', 'Lorem': 'Monty', '123': 'foofoo'}, 
]

# Link to the sample directory that contains word files that will be duplicated and replaced in the cloning process
path_to_folder_cloner = Path('/folder-cloner')
path_to_sample_data_folder = path_to_folder_cloner / 'sample_test' / '123 Folder we want to clone Lorem Ipsum'

# Run the clone folder function using the sample data and sample directory
main.clone_folder(directory=path_to_sample_data_folder, replacement_dict_list=rep_list)

