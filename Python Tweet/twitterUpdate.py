# Import required modules
import twitter, datetime

#Load in my keys and secrets from the credentials file into a list (array)
file = open("TwitterCredentials.txt")
creds = file.read().split('\n')

#Create a new API wrapper, passing in my credentials one at a time
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

#Find out what time it is now (in Coordinated Universal Time)
timestamp = datetime.datetime.utcnow()

#Post status update and get the response from Twitter
response = api.PostUpdate("Hello Cass - Tweeted at " + str(timestamp))

#Print out response text (should be the status update if everything worked)
print("Status updated to: " + response.text)