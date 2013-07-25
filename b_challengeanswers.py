#!/usr/bin/env python

import requests, base64, json, re, sys, os

'''
  	Creator:		B-Dawg
		Usage:			Solve Da Challenges

		Version Data:	
						2013-07-18 - Challenge 1 Individual Function 
						2013-07-18 - Challenge 2 Individual Function					
						2013-07-19 - Challenge 3 Individual Function
						2013-07-22 - Challenge 1v2 Individual Function
						2013-07-22 - Challenge 2v2 Individual Function
						2013-07-24 - Challenge 3v2 Individual Function
						2013-07-25 - Built main and exit functions.
									 Tidied a little of the code up.
'''

	#TPC = The Python Club!
TPC = "http://thepythonclub.org"


'''Functions'''
def challenge1():
		#Thief TPC challenge 1 page/challenge 'question'
	response = requests.get(TPC+':8081/challenge1')
		#Steal base64 encoded string
	b64string = response.text.split('"')[1]
		#Create dict and add URL data and base64 decoded stolen string
	textstring = {'answer':base64.b64decode(b64string)}
		#Post answer to challenge1
	post = requests.post(TPC+':8081/challenge1', data=json.dumps(textstring))
		
		#Clarification
	print
	print "\tChallenge 1:"
	print response.text
	print "base64 encoded string  = " + b64string
	print "base64 decoded strings = " + textstring['answer'] + '\n'
	print "\tChallenge 1 Answer: "
	print post.text
		#Create Variable for Challenge1 Answer - Currently unused.
	key1 = post.text.split('"')[1]
	return main()

def challenge2():
		#Dict for Words to Numbers: Zero through Ten
	numbers = {
		'one' : 1,'two' : 2,'three' : 3,'four' : 4,'five' : 5,
		'six' : 6,'seven' : 7,'eight' : 8,'nine' : 9,'ten' : 10,
	}
		#Dict for Numebrs to Words: 0 through 30
	nums = {
		0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',
		6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',
		12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
		16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
		20:'twenty',21:'twenty-one',22:'twenty-two',23:'twenty-three',
		24:'twenty-four',25:'twenty-five',26:'twenty-six',
		27:'twenty-seven',28:'twenty-eight',29:'twenty-nine',30:'thirty',
	}
		#Thief TPC challenge 2 page/challenge 'question'
	response = requests.get(TPC+':8082/challenge2')
		#Pull individual words from challenge question
		#Makes the assumption that there will be only 5 words
		#Three words for numbers and two words for operators
	words = (response.text.split('"')[1]).split()
		#Assign words to assumed list for numbers or operators
	variables = [words[0], words[2], words[4]]
	operators = [words[1], words[3]]
		#Loop to translate assumed 'number words' to numerical number
	var = []
	for i in variables:
		var.append(numbers[i])
	
		#Two loops to evaluate first and second operator, respectively
		#Loops make assumption that the only operators are plus and minus	
	equation = 0
	if operators[0] == 'plus':
		equation = var[0] + var[1]
	elif operators[0] == 'minus':
		equation = var[0] - var[1]

	if operators[1] == 'plus':
		equation = equation + var[2]
	elif operators[1] == 'minus':
		equation = equation - var[2]

		#Create dict & add URL data and translated numerical number to word
	solution = {'answer':nums[equation]}

		#Post answer to challenge2
	post = requests.post(TPC+':8082/challenge2', data=json.dumps(solution))
		#Clarification
	print 
	print "\tChallenge 2:"
	print response.text
	print "Solution to equation : " + solution['answer'] + '\n'
	print "\tChallenge 2 Answer: "
	print post.text

		#Create Variable for Challenge2 Answer - Currently unused
	key2 = post.text.split('"')[1]
	return main()

def challenge3():
		#Thief TPC challenge 3 page/challenge 'question'
	response = requests.get(TPC+':8083/challenge3')
	html = response.text

		#Search and strip out url for user list and create dict
	userurl = TPC + '/tmp/user' + re.findall(re.escape("/tmp/user")+ \
		"(.*)"+re.escape("\">User IDs"),html)[0]

	userfile = json.loads(requests.get(userurl).text)
		#Strip out User's name from challenge question
	user = response.text.split('"')[1]
		#Loop to find User's UserID #
	for i in userfile:
		if user == userfile[i]["Name"]:
			userid = i

		#Search and strip out url for password list and create dict
	passurl = TPC + '/tmp/pass' + re.findall(re.escape("/tmp/pass")+ \
		"(.*)"+re.escape("\">Password"),html)[0]

	passfile = json.loads(requests.get(passurl).text)
		#Loop to find password for userID # and base64 decode it
	for i in passfile:
		if userid == i:
			password =  base64.b64decode(passfile[i])
		#Create dict and add URL data and base64 decoded password
	answer = {'answer':password}
		#Post answer to challenge3
	post = requests.post(TPC + ':8083/challenge3', data=json.dumps(answer))
		#Clarification
	print 
	print "\tChallenge 3:"
	print "Password information for  : " + user
	print "Password in Password List : " + base64.b64encode(password)
	print "Base64 decoded password   : " + password + '\n'
	print "\tChallenge 3 Answer: "
	print post.text
		#Create Variable for Challenge3 Answer - Currently unused
	key3 = post.text.split('"')[2]
	return main()

def exit():
	sys.exit()

def main():
	print '\nWhat challenge would you like to complete?'
	print '   Available Challenges: 1, 2, 3'
	print '        \"DIE\" to exit.\n'
	choice = raw_input('Choice : ').lower()

	if choice == '1':
		challenge1()
	elif choice == '2':
		challenge2()
	elif choice == '3':
		challenge3()
	elif choice == 'die!':
		exit()
	else:
		print "Incorrect Selection - REBOOT!\n"
		main()


if __name__ == '__main__':
	#Clears CMD Prompt (for windows - 'clear' for unix)
	os.system('cls')
	main()
