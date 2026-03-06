"""
program: doctor.py
Chapter 5 Case Study (pages 138 - 139)
3/5/2026

Application that simulates a therapy session by modifying user input.
"""

import random
import pyttsx3

# Global variables of list objects the all functions can share
hedges = ("Please, tell me more...", "Many of my patients tell me the same thing.", "Please continue.", "You don't say...", "Go on, go on...", "That's interesting...")

qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")

replacement = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "am":"are", "you":"I", "are":"am"}

# Definition of the speak() function that uses the pyttsx3 module
def speak(text):
	"""Speaks the text given the function out loud."""
	engine = pyttsx3.init()
	engine.say("Testing")
	engine.runandwait()

# Definition of the reply() Function
def reply(sentence):
	"""Builds and returns a reply to the sentence passed to this function."""
	probability = random.randint(1, 10)
	if probability == 1:
		return random.randint(hedges)
	else:
		return random.randint(qualifiers) + changePerson(sentence)

# Definition of the changePerson() function
def changePerson(sentence):
	"""Replace first-person words with second-person"""
	words = sentence.split()
	replywords = []
	# FOR loop that looks at the 'words' list
	for word in words:
		replyWords.append(replacements.get(word,word))
	return " ".join(replyWords)

# Definition of the main() function
def main():
	"""Handles the interaction between patient and doctor"""
	greeting1 = "Good day, I hope you are well today"
	greeting2 = "What can I do for you?\nEnter your response or type QUIT to exit."
	
	print(greeting1)
	speak(greeting1)

	print(greeting2)
	speak(greeting2)

	while True:
		sentence = input("\n>>")
		if sentence.upper().strip() == "QUIT":
			goodbye = "Have a great day! Press ENTER to exit."
			speak(goodbye)
			input(goodbye)
			break
		elif sentence == "":
			warning = "Did you mean to say something? Or you can type QUIT to exit."
			print(warning)
			print(warning)
		else:
			response = reply(sentence)
			print(response)
			speak(response)

# Global call to main() for program entry
if __name__ == '__main__':
	main()