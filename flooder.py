import requests
# -------------------------------------------
# ngl.link flooder by SkemiiL
# -------------------------------------------

# defining logo and printing it
logo = """
             _   _ _       _       __ _                 _           
 _ __   __ _| | | (_)_ __ | | __  / _| | ___   ___   __| | ___ _ __ 
| '_ \ / _` | | | | | '_ \| |/ / | |_| |/ _ \ / _ \ / _` |/ _ \ '__|
| | | | (_| | |_| | | | | |   <  |  _| | (_) | (_) | (_| |  __/ |   
|_| |_|\__, |_(_)_|_|_| |_|_|\_\ |_| |_|\___/ \___/ \__,_|\___|_|   
       |___/                                         by Skemiil
"""
print(logo)

# user input
text = input("Text: ")
url = "https://ngl.link/" + input("username: ")
amt = int(input("Amount of messages: "))

# sending a post request to ngl.link
for x in range(0, amt):
    requests.post(url, allow_redirects=False, data={
    "question": text
    })
    print("[+] Sending text: %s to %s. Message %i out of %i" % (text, url, x, amt))
print("[-] Finished flood!")