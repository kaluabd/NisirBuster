import requests

url = input("Enter the URL: ")
wordlist = input("Enter the path to the wordlist: ")

with open(wordlist) as f:
    for line in f:
        directory = line.strip()
        full_url = url + "/" + directory
        r = requests.get(full_url)
        if r.status_code == 200:
            print("[+] Directory found:", full_url)
