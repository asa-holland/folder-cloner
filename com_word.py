# com_word.py



# Used to open word files
import win32com.client as com

def start_word():
	"""
	Shorthand function to start a Microsoft Word application using the win32com client fucntions
	"""

	# Open the word applicaton
	word_application = com.gencache.EnsureDispatch("Word.Application")

	# Set the visibility of the Word Application to False
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

