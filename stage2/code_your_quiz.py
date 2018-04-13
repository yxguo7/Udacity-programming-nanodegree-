easy = """Washington, D.C. is the capital of the __1__. The signing of the Residence Act on July 16, __2__, approved the creation of a capital district located along the __3__ on the country's __4__ Coast. """
medium = """__1__ is the capital of the most populous country in the world, the People's Republic of __2__. With a population of __3__ million people, it is the nation's second-largest city after __4__."""
hard = """The city of __1__ or Berne is the capital of Switzerland.
With a population of __2__ (April 2016), Bern is the fourth most populous
city in Switzerland. The official language in Bern is the Swiss variety of Standard __3__, but the most-spoken language is an Alemannic Swiss German
dialect, __4__."""
easy_answer_list = ['United States', '1790', 'Potomac River', "East"]
medium_answer_list = ['Beijing','China', '21.5','Shanghai']
hard_answer_list = ['Bern','141107','German','Bernese German']
replacement = ["__1__","__2__","__3__","__4__"]
user_answer = []

'''define replace procedure to search for blank spots in question'''
def replace(word, replacement):
	for index, blank in enumerate(replacement):
		if blank in word:
			return index
	return -1

"""Answer_question procedure asks user to typein answers for blanks.  question == certen level.  Then system compare user's answer with answer_list.  If correct, ask user to answer next blank.  Otherwise, ask user to answer this blank again till correct.  This procedure will return a user_answer list for further decision procedure."""
def answer_question(question, replacement, answer_list):
	question_list = question.split()
	for index, word in enumerate(question_list):
		replaced_index = replace(word,replacement)
		if replaced_index != -1:
			user_input = raw_input("Your answer for " + replacement[replaced_index] + "is: ")
			while user_input != answer_list[replaced_index]:
				user_input = raw_input("Your answer for " + replacement[replaced_index] + "is incorrect.  Could you try again? ")
			if user_input == answer_list[replaced_index]:
				user_answer.append(user_input)
				print question.replace(word, user_input)
				question = question.replace(word, user_input)
				question_list = question.split()

'''Define main procedure for user to choose level and make final decision'''
def quiz(q1,q2,q3):
 	level = raw_input('Choose a level: 1. Easy/ 2. Mediam/ 3. Hard: ')
 	question = ""
 	answer_list = []
 	while level.lower() not in ["easy", "mediam", "hard", "1", "2", "3"]:
 		level = raw_input("Invalid input.  Choose a level: 1. Easy/ 2. Mediam/ 3. Hard: ")

	if level.lower() == 'easy' or level == "1":
		question = easy
	 	answer_list = easy_answer_list
	if level.lower() == "medium" or level == "2":
	 	question = medium
	 	answer_list = medium_answer_list
	if level.lower() == "hard" or level == "3":
	 	question = hard
	 	answer_list = hard_answer_list

	print question

	answer_question(question, replacement, answer_list)
	if user_answer == answer_list:
		print "Congradulations!!!"

print quiz(easy, medium, hard)




