#!/usr/bin/python
#directory bruteforcing 
#python3 
import requests
print("============================================")
print("*                                           ")
print("*++++   Nisir Cyber Security            ++++")
print("*++++     Nisirbuster v1.0              ++++")
print("*      FOR ETHICAL PURPOSE ONLY             ")
print("*  Created by:Kaleab Abdurahman             ")
print("*  twitter: https://twitter.com/kaluabd     ")
print("*  Website: https://nisircyber.com          ")
print("============================================")



def request(url):
		try:
				return requests.get("http://" + url)
		except requests.exceptions.ConnectionError:
				pass

target_url = input("Please Enter the url: ")
#put common directory names in the same directory calling it wordlist.txt
file = open("wordlist.txt","r")
for line in file:
		word = line.strip()
		full_url = target_url + "/" + word 
		response = request(full_url)
		if response:
			print("[+] Discovered Directory At This Link: " + full_url)
		else :
			print("Directory not found at this link: " + full_url)