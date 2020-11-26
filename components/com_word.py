
# Used to open word files
import win32com.client as com

def start_word():

	word_application = com.gencache.EnsureDispatch("Word.Application")
	word_application.Visible = False
	word_application.DisplayAlerts = False

	return word_application


def close_word(word_application):
	word_application.Quit()

