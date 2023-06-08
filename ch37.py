#!/bin/python

#Script: Ops 401 Class 37 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 7 JUN 2023
#Purpose: Create a python script that retrieves coockies from a website generates a .html file and opens it with firefox

#!/usr/bin/env python3

import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp"  # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster():
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

def send_cookie_and_capture_response(url, cookie):
    session = requests.Session()
    session.cookies.update(cookie)
    response = session.get(url)
    html_content = response.text

    # Generate HTML file
    with open('response.html', 'w') as file:
        file.write(html_content)

    return 'response.html'

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Send the cookie back to the site and capture the response
html_file = send_cookie_and_capture_response(targetsite, cookie)
print("Response saved to:", html_file)

# Open the HTML file with Firefox
webbrowser.get('firefox').open(html_file)
