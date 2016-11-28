print('Homework 2''\n''Section 002 Wednesday 5:30-6:30 PM''\n''Samantha Moross')

print ('------------')

print('PART 1', '\n')

import requests #Import requests module
from bs4 import BeautifulSoup #Import BeautifulSoup4 module

base_url = 'http://www.nytimes.com'
r = requests.get(base_url) #get contents of nytimes homepage
soup = BeautifulSoup(r.text, 'lxml') #gets HTML from the homepage 

print('New York Times -- First 10 Story Headlines: ','\n') 

x = 0
for story_heading in soup.find_all(class_="story-heading"): 
#loops through and finds the top 10 elements with the story-heading class
    if story_heading.a: #uses tag name to find story-headings that begin with 'a' (as in <a href...)
        story = (story_heading.a.text.replace("\n", " ").strip()) #story headings separated by newline set to variable story
        if story != "" : #if the title is not a string weeds out headlines that have no text
        	if x < 10: #limit to 10 headlines
        		print (story.strip()) #prints the headlines. .strip() removes whitespace 
        		x += 1 #counts the headlines printed

print ('------------')

print('PART 2', '\n')

base_url = 'http://www.michigandaily.com/section/opinion'
r = requests.get(base_url) #get contents of Michigan Daily opinion page
soup = BeautifulSoup(r.text, 'lxml') #retrieves the HTML from the opinion page 

print('Michigan Daily -- Most Read: ', '\n')

for most_read in soup.find_all(class_ = "pane-mostread"): 
#loops through text and finds elements with the class 'panel-pane pane-mostread' heading
	for title in most_read.find_all('a'): 
#loops through most read links to find those that begin with 'a' (as in <a href...)
		if title.a: #uses tag name to find titles within the links that begin with 'a'
			print(title.a.text.replace("\n", " ").strip()) #prints titles each on a new line
		else:
			print (title.contents[0].strip()) #otherwise removes the title from the text

print ('------------')

print('PART 3', '\n')

base_url = 'http://www.collemc.people.si.umich.edu/data/gallery.html'
r = requests.get(base_url) #get contents of Colleen's page
soup = BeautifulSoup(r.text, 'lxml') #retrieves the HTML from the page 

print("Colleen's Page -- Alt tags")

images = soup.find_all('img') #finds all text that has str 'img'
for image in images: #loops through each line of text that has 'img' in it
	if (image.get('alt')) == None: #if there is no value to str 'alt' within the line of text 
		print ("No alternative text provided!!") 
	else:
		print (image.get('alt')) #retrieves the value of alt, which is the title of the image

print ('------------')

print('PART 4', '\n')
#Extracts the single email from one webpage with one staff member's information: www.si.umich.edu/node/9949
#and then all the emails from the directory that includes all staff member's information: www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All


import re
import urllib.request, urllib.parse, urllib.error
base_url = 'http://www.si.umich.edu/node/9949'
html = urllib.request.urlopen(base_url).read() #retrieves the HTML using urllib
soup = BeautifulSoup(html, 'html.parser') #parses the HTML neatly using BeautifulSoup

for staff_member in soup.find_all(class_='field-name-field-person-email'): 
#loops through the HTML and finds the email within the class 'field-name-field-person-email'
	tag = staff_member.find('a') #Finds the links with tag 'a'
	email = tag.text #Retrieves the text of the email
	print (email)

print ('------------')

#Additional 10 points 
print('Emails connected to UMSI directory')
base_url = 'http://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All'
html = urllib.request.urlopen(base_url).read() #retrieves the HTML using urllib
soup = BeautifulSoup(html, 'html.parser') #parses the HTML neatly using BeautifulSoup

for contact in soup.find_all(class_='field-name-contact-details'):
#loops through the HTML and finds the email within the class 'field-name-contact-details'
	tag = contact.find('a') #Finds the links with tag 'a'
	page = tag['href'] #Provides the links we want to specify the page for each contact
	base_url2 = 'http://www.si.umich.edu' + page #Gives the specified URLs, so we can find the emails for each 
	html2 = urllib.request.urlopen(base_url2).read() #retrieves HTML from specific page
	soup2 = BeautifulSoup(html2, 'html.parser') #parses specific HTML neatly using BeautifulSoup
	
	class1 = soup2.find(class_='field-name-field-person-email') #Finds email under the class 
	tag2 = class1.find('a') #Finds links with tag 'a'
	email2 = tag2.text #Provides the represented text
	print (email2) 

print ('------------')

print('Expected grade: 150')




	













		


				



