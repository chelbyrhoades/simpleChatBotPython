import random
import time
import socket

print("Welcome to MilitaryBot.")
greet = ["hello", "hi", "hola"]
greetR = ["hello citizen", "hello human", "Welcome to a non-suspicious base."]
pun = ["Wat do you call a fake noodle? An impasta!", "What do you call a fish that doesn't share? Shellfish."]
secrets = ["Tupac is still alive", "Parker is the leader of the illuminati", "Cilantro is devil spawn", "Birds aren't real.", "Elon Musk is a martian", "Captain America is from Canada", "Alexa is always listening", "Billie Eilish is an alien", "Donald Trump is a cat person", "Chuck Norris is our leader"]

while True:
	ask = raw_input(">>>")
	if ask in greet:
		response = random.choice(greetR)
		print(response)
	elif ask == "tell me a pun":
		response = random.choice(pun)
		print(response)
	elif ask == "goodbye":
		print("Goodbye!")
		break
	elif ask == "shut up":
		print("Excuse me??? I am the government, I will end you.")
	elif ask == "area 51":
		print("You're not authorized to know anything about that, citizen.")
	elif ask == "password123":
		response = random.choice(secrets)
		print(response)
	elif ask == "download":
		time.sleep(1)
		print("Downloading Ultron Virus.")
		print("Virus ID Number: 57954y7584938gfb45")
		time.sleep(1)
		print("00000000")
		time.sleep(1)
		print("0000||||")
		time.sleep(1)
		print("000|||||")
		time.sleep(1)
		print("00||||||")
		time.sleep(1)
		print("||||||||")
		time.sleep(1)
		print("Download complete. Web cam access granted.")
		time.sleep(1)
		print("Connected to IP " + socket.gethostbyname(socket.gethostname()))
	else:
		print("I'm sorry, I didn't understand")