# Import libraries

import random
import time
import wikipedia
from unidecode import unidecode
from bs4 import BeautifulSoup
import requests

# Set booleans to control conversation flow

firstConversation = True
secondConversation = True
result = ""

# Define stop words list
# Read extenal file and into list and strip newlines

with open('stopwords.txt', 'r') as f:
    stopWords = f.read().splitlines()
    f.close()
    
# Define list of common first names
    
with open('names.txt', 'r') as f:
    namesList = f.read().splitlines()
    f.close()

# Define other lists, prompts and responses

names = ['Matthew','Simon','Bob']
prompts = ['What can I do for you?','Do you have a question for me?','Is there something you wanted to ask?']
unrecognised = ["I'm sorry, I did not understand","Come again?","Try asking something else",'Could you rephrase that?']

# Divider for readability

divider = "*" * 100
prefix = "*  "

# Get the current hour and year

current_hour = time.strptime(time.ctime(time.time())).tm_hour
current_year = time.strptime(time.ctime(time.time())).tm_year

# Set age and year of birth for PC

pcAge = random.randint(16,65)
pcBirthYear = current_year - pcAge

# Function to strip stop words from input

def stripWords(words):
    global result
    # Separate all words in supplied input
    querywords = words.split()
    # Loop through words of supplied input and store those not in stop word list in resultwords variable
    # Stop words are all in lower case, so convert input to lower case
    resultwords  = [word for word in querywords if word.lower() not in stopWords]
    # Join 'meaningful' words together divided by space
    result = ' '.join(resultwords)
    # Return the result to the main script
    return result

# Set greeting based on hour
 
if current_hour < 12 :
    greeting = "Good morning"
elif current_hour == 12 :
    greeting = "Good day"
elif current_hour > 12 and current_hour < 18 :
    greeting = "Good afternoon"
elif current_hour >= 18 :
    greeting = "Good evening"
    
# Guided conversation

# Request name and strip stop words

print(divider)

print(prefix + "Hello. What is your name?")
tempName = raw_input()
stripWords(tempName)

# Compare supplied name against list of common first names and prompt until a match is found

while result.capitalize() not in namesList:
    print("Is that really your name? ... please try that again ...")
    tempName = raw_input()
    stripWords(tempName)
    

# Time-based greeting based on hour with random PC name returned
# Capitalise first letter of name in case it is entered in lower case

print(divider)

myName = result.capitalize()
print(greeting + ", " + myName)
pcName = random.choice(names)
print("My name is " + pcName)

# Check user's name against random name and display message if equal

if pcName == result.capitalize():
    print("What a coincidence!")

print(divider)

print("Tell me something interesting about yourself")

result = ""
query = raw_input()
stripWords(query)

print(divider)

print("Here's what I found out about '" + result + "' ... ")

# Wikipedia scrape 1
# Use Unidecode to allow Windows to display unsupported characters
# Limit number of sentences returned
# Handle disambiguation

try: 
    print unidecode(wikipedia.summary(result, sentences = 3))
except:
    topics = wikipedia.search(result)
    print ("Did you mean? ...")
    # Loop through search results with count/values
    for i, topic in enumerate(topics):
        # Print numbered list of results
        print (i, unidecode(topic))
    # Prompt user to choose an item
    choice = int(raw_input("Choose one ..."))
    # Check option chosen is included in available options
    if choice in xrange (len(topics)):
        # If it is, print the Wikipedia summary for chosen option
        print unidecode(wikipedia.summary(topics[choice], sentences = 3))
    # Otherwise, error
    else:
        print("Oops")

print(divider)
time.sleep(2)

print("What would you like to know about?")

result = ""
query = raw_input()
stripWords(query)

print(divider)
print("Here's what I found out about '" + result + "' ... ")
time.sleep(2)

# Wikipedia scrape 2
# Use Unidecode to allow Windows to display unsupported characters
# Limit number of sentences returned
# Handle disambiguation

try: 
    print unidecode(wikipedia.summary(result, sentences = 3))
except:
    topics = wikipedia.search(result)
    print ("Did you mean? ...")
    # Loop through search results with count/values
    for i, topic in enumerate(topics):
        # Print numbered list of results
        print (i, unidecode(topic))
    # Prompt user to choose an item
    choice = int(raw_input("Choose one ..."))
    # Check option chosen is included in available options
    if choice in xrange (len(topics)):
        # If it is, print the Wikipedia summary for chosen option
        print unidecode(wikipedia.summary(topics[choice], sentences = 3))
    # Otherwise, error
    else:
        print("Oops")
        
# Age

print(divider)
time.sleep(2)

while True:
    try:
        print("How old are you, " + myName + "?")
        myAge = int(raw_input())
    except ValueError:
        print("Sorry, " + myName + "; I didn't understand that.")
        #Invalid input - return to the start of the loop
        continue
    else:
        #Valid input - exit loop
        break
if myAge == pcAge:
    time.sleep(2)
    print(divider)
    print("We are the same age, " + myName)
    print(divider)
else:
    if myAge > pcAge:
        time.sleep(2)
        print(divider)
        print("I am younger than you, " + myName)
        print(divider)
    else:
        if myAge < pcAge:
            time.sleep(2)
            print(divider)
            print("I am older than you, " + myName)
            print(divider)
            
birthYear = str((current_year - myAge))

time.sleep(2)
print("You were born in " + birthYear)

print(divider)

time.sleep(2)
print("Some interesting (mostly American) facts about " + str(birthYear) + " ...")
print(divider)
time.sleep(2)

# URL Scrape for year-related info

url = "http://www.onthisday.com/events/date/" + str(birthYear)
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")
# Filter scrape on class and return five items - text only
for link in soup.find_all("li", class_="event-list__item", limit = 5):
    print(unidecode(link.get_text()))

# End of guided conversation

# First conversation looks for specific occurences of words

print(divider)
time.sleep(2)

while firstConversation:
    
    # Prompt user with a random prompt
    
    print (random.choice(prompts))
    followUp = raw_input()
    
    if 'old' in followUp:
        
        print("A gentleman doesn't ask")
        print(" ... but as it happens, I am " + str(pcAge) + " years old")
        print(divider)
        time.sleep(2)
        print("Which means I was born in " + str(pcBirthYear))
        print(divider)
        time.sleep(2)
        print("Some interesting (mostly American) facts about " + str(pcBirthYear) + " ...")
        print(divider)
        time.sleep(2)
        
        # URL Scrape for year-related info
        url = "http://www.onthisday.com/events/date/" + str(pcBirthYear)
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        
        # Filter scrape on class and return five items - text only
        for link in soup.find_all("li", class_="event-list__item", limit = 5):
            print(unidecode(link.get_text()))
        print(divider)
        continue
        
    else:
        if 'name' in followUp:
            print("I already told you ... it's " + pcName)
            print(divider)
            continue
            
        else:
            if 'doing' in followUp:
                print("Talking to you of course!")
                print(divider)
                continue
                
            else:
                if 'weather' in followUp:
                    print("Well, " + myName + " ... today's weather looks like this ...")
                    print(divider)
                    urlWeather="http://www.bbc.co.uk/weather/2640194"
                    r = requests.get(urlWeather)
                    weatherData = r.text
                    weatherSoup = BeautifulSoup(weatherData,"html.parser")
                    for link in weatherSoup.find_all("p", class_="body", limit = 1):
                        print(link.get_text())
                
                else:
                    #print(random.choice(unrecognised))
                    print("I didn't get that, so let's move on ... ")
                    firstConversation = False
                
# Second conversation is more random and uses lists as keywords and responses

# Define pairs of trigger strings and responses

greetings = ['hola', 'hello', 'hi','hey!','hello','hey']
questions = ['how are you?','how are you doing?','how are you','how are you feeling','how are you today']
responses = ['Okay','I am fine','very good','very well, thank you','not so good']
validations = ['yes','yeah','yea','no','nah','of course','of course not']
confirmations = ['are you sure?','you sure?','you sure?','sure?','really?','honestly?','definintely?']

signoffs = ['goodbye','quit','bye','finish','finished']

link_pairs = (greetings, greetings), (questions, responses), (confirmations, validations)

print(divider)
print("*** We are now in secondConversation ***")
time.sleep(2)

while secondConversation:
    
    # Prompt user with a random prompt
    print(random.choice(prompts))
    userInput = raw_input()
    for triggers, outputs in link_pairs:
        if not userInput.lower() in triggers:
            continue
            
        random_output = random.choice(outputs)
        print(random_output)
        
    else:
        if userInput.lower() in signoffs:
            print("Thank you for talking to me, " + myName)
            secondConversation = False