easy = """Washington, D.C. is the capital of the __1__. The signing of the
Residence Act on July 16, __2__, approved the creation of a capital district
located along the __3__ on the country's __4__ Coast. """
medium = """__1__ is the capital of the most populous country in the world,
the People's Republic of __2__. With a population of __3__ million people,
it is the nation's second-largest city after __4__."""
hard = """The city of __1__ or Berne is the capital of Switzerland.
With a population of __2__ (April 2016), Bern is the fourth most populous
city in Switzerland. The official language in Bern is the Swiss variety of
Standard __3__, but the most-spoken language is an Alemannic Swiss German
dialect, __4__."""
easy_answer_list = ['United States', '1790', 'Potomac River', "East"]
medium_answer_list = ['Beijing','China', '21.5','Shanghai']
hard_answer_list = ['Bern','141107','German','Bernese German']
replacement = ["__1__","__2__","__3__","__4__"]
#procedure replace is to search for blank spots in question.

user_answer = ["", "", "", ""]

def replace(word, user_answer, answer_list):
	for index, blank in enumerate(replacement):
		if blank in word and user_answer[index] != answer_list[index]:
			return index
	return -1

"""define procedure answer_question for user to typein answers for blanks
after choosing level.  question_sring== certen level.  This procedure will
return a user_answer list for further decision procedure."""
def answer_question(question,replacement,answer_list):
	for index, word in enumerate(question):
		print word
		replaced_index = replace(word, user_answer, answer_list)
		if replaced_index != -1:
			user_input = raw_input('Your answer for ' + replacement[replaced_index] + ' is: ')
			user_answer[replaced_index] = user_input
print answer_question(easy, replacement, easy_answer_list)

'''
"""define procedure decision to check each answer verse certern answer_list
and print out decision based on correctness."""
def decision(user_answer, answer_list):
	decision = []
	n = 0
	while n < len(user_answer):
		if user_answer[n] == answer_list[n]:
			decision.append('Your answer ' + user_answer[n] + ' for ' + str(n+1) + ' is correct.  ' )
		n+=1
	if user_answer != answer_list:
		decision.append('Can you figure out the rest? ')
	decision = ''.join(decision)
	return decision


# Define main procedure
def quiz(q1,q2,q3):
 	level = raw_input('Choose a level: 1. Easy/ 2. Mediam/ 3. Hard: ')
 	question_string = ""
 	answer_list = []
 	while level.lower() not in ["easy", "mediam", "hard", "1", "2", "3"]:
 		level = raw_input("Invalid input.  Choose a level: 1. Easy/ 2. Mediam/ 3. Hard: ")

	if level.lower() == 'easy' or level == "1":
		question_string = easy
	 	answer_list = easy_answer_list
	if level.lower() == "medium" or level == "2":
	 	question_string = medium
	 	answer_list = medium_answer_list
	if level.lower() == "hard" or level == "3":
	 	question_string = hard
	 	answer_list = hard_answer_list

	print question_string

 	question = question_string.split()
 	while True:
 		answer_question(question, replacement, answer_list)
 		result = decision(user_answer, answer_list)
 		print result
 		if user_answer == answer_list:
 			break

print quiz(easy, medium, hard)
















