instructions = "This is a quiz to test your knowledge of a\
 Dr. Seuss book called \"One fish two fish red fish blue fish\".\
 Try to fill in the blanks to the best of your ability. To\
 begin, enter the level quiz you would like to take: easy,\
 medium, or hard."

guess_again = "Nope. That's not the correct answer.\
Guess again."

easy_quiz = "One *fish two *fish red *fish blue *fish.\
 This one has a little *star. This one has a *little car. Say!\
 what a lot of fish there *are."

easy_quiz_answer = ["fish", "star", "little", "are"]

medium_quiz = "Yes. Some are *red. And some are blue. Some are\
 *old and some are new. Some are *sad. And some are glad.\
 And some are very, very bad. Why are they *sad and *glad\
 and *bad? I do not know. Go ask your *dad."

medium_quiz_answer = ["red", "old", "sad", "glad","bad", "dad"]

hard_quiz = "From *there to here, from *here to there,\
 funny things are *everywhere. Here are some who like to *run.\
 They run for *fun in the hot, hot *sun. Oh *me!\
 Oh my! What a *lot of funny things go *by."

hard_quiz_answer = ["there", "here", "everywhere", "run", \
 "fun", "sun", "me", "lot", "by"]

congratulations = "Congratulations! You have displayed your knowledge\
 of \"One fish two fish\"."

print instructions
user_input = raw_input()

#This function returns the length of the starred words, including the star,
#but not including the punctuation following.This allows me to refer
#to it in the next function when I want the program to print the punctuation at
#the end of the blanks.
def word_len(quiz, answer_key):
	for answer in answer_key:
		if ("*" + answer) in quiz:
			return len(answer) + 1

correct_answers = []
#Although this variable isn't used in this version, I included it to allow me
#to implement a grading system later on if I so wish.
incorrect_answers = []
#This function takes the original strings and replaces the starred words with
#blanks, or correct answers, based on what the user has guessed correctly.
def replace(quiz):
	index = 1
	replaced_string = ''
	for quiz_word in quiz.split():
		make_blanks = quiz_word.replace(quiz_word, "___" + str(index) + "___")
		fill_in_answers = quiz_word.replace(quiz_word, quiz_word[1:])
		if quiz_word[0] == "*":
			if quiz_word[1:word_len(quiz_word, answer_key)] in correct_answers:
				replaced_string = replaced_string + fill_in_answers + " "
				index = index + 1
			else:
				replaced_string = replaced_string + make_blanks + quiz_word[word_len(quiz_word, answer_key):] + " "
				index = index + 1
		else:
			replaced_string = replaced_string + quiz_word + " "
	return replaced_string

if user_input == "easy":
	answer_key = easy_quiz_answer
	quiz = easy_quiz
if user_input == "medium":
	answer_key = medium_quiz_answer
	quiz = medium_quiz
if user_input == "hard":
	answer_key = hard_quiz_answer
	quiz = hard_quiz

print (replace(quiz))

#This function will be the first prompt and the prompts that follow a correct
#guess. Instead of incrementing the number of the blank by one each time, the
#number of the blank is a specialized number that corresponds to the blank
#that the user is up to.
def guess_the_word(correct_answers):
	numbered_blank = 1
	for correct_answer in correct_answers:
		numbered_blank = numbered_blank + quiz.count("*" + correct_answer)
	return ("___" + str(numbered_blank) + "___ = ")

index = 0
user_input = raw_input(guess_the_word(correct_answers))
while len(correct_answers) <= len(answer_key)-1:
	if user_input == answer_key[index]:
		correct_answers.append(user_input)
		print replace(quiz)
		index = index + 1
		if len(correct_answers) <= len(answer_key)-1:
			user_input = raw_input(guess_the_word(correct_answers))
	else:
		incorrect_answers.append(user_input)
		print guess_again
		user_input = raw_input(guess_the_word(correct_answers))

print congratulations
