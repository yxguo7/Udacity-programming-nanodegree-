import urllib

def read_text():
	quotes = open ("/Users/yuxiaoguo/Google Drive/Udacity nonodegree/stage3/movie_quotes.txt")
	contents_of_file = quotes.read()

	quotes.close()
	check_profanity(contents_of_file)


def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	print (output)
	connection.close()
	if "true" in output:
		print ("Profanity Alert!!")
	elif "false" in output:
		print ("This document has no curse words!")
	else: 
		print("Could not scan the document properly.")

read_text()