# com_word.py



# Used to open word files
import win32com.client as com

def start_word():
	"""
	Shorthand function to start a Microsoft Word application using the win32com client fucntions
	"""

	# Try creating the word application using com
	try:
	    word_application = com.gencache.EnsureDispatch("Word.Application")

	    # enforce the applicattion to be not visible (repeat the code to be sure)
	    word_application.Visible = False
	
	# Handle the case where word is not able to recognize the atributes provided to it
	# This code adapted from fossum on GitHub:
	# Source: https://gist.github.com/rdapaz/63590adb94a46039ca4a10994dff9dbe
	except AttributeError:
	    
	    # Corner case dependencies.
	    import os
	    import re
	    import sys
	    import shutil
	    
	    # Remove cache and try again.
	    MODULE_LIST = [m.__name__ for m in sys.modules.values()]
	    
	    # Iterate over the modules listed in the system
	    for module in MODULE_LIST:

	    	# look for the module matching win32com
	        if re.match(r'win32com\.gen_py\..+', module):

	        	# if found, delete it
	            del sys.modules[module]

	    # Once deleted, remove the gen_py folder as well for a clean sweep
	    shutil.rmtree(os.path.join(os.environ.get('LOCALAPPDATA'), 'Temp', 'gen_py'))

	    # reimport win32com
	    from win32com import client

	    # run the application
	    word_application = com.gencache.EnsureDispatch("Word.Application")

	    # enforce the applicattion to be not visible (repeat the code to be sure)
	    word_application.Visible = False

	# Set the visibility of the Word Application to False
	# This is repeated to catch any lag time where the word application's visibility has not previously been turned off
	word_application.Visible = False

	# Disable alert displays on the Word Application
	word_application.DisplayAlerts = False

	# Return the currently running word application so that it can be used to open and edit .doc files 
	return word_application


def close_word(word_application):
	"""
	Shorthand masking function to close a provided word application
	"""

	# Quits the provided word application
	word_application.Quit()

