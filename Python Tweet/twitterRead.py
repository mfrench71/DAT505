#First import the required libraries
import twitter
from unidecode import unidecode

#Hardcode a user ID into a variable (Stephen Fry)
user = 15439395

#Load in my keys and secrets from the credentials file into a list (array)
file = open("TwitterCredentials.txt")
creds = file.read().split('\n')

#Create a new API wrapper, passing in my credentials one at a time
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

#Get the most recent batch of status updates from the user
statuses = api.GetUserTimeline(user)

#Just print out the most recent one
print unidecode((statuses[0].text))