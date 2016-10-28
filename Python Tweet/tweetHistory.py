# Script to Tweet last URL visited (Windows/Firefox)

# Import the required libraries
import sqlite3
import urllib2
import twitter
import datetime
import time
from unidecode import unidecode
from BeautifulSoup import BeautifulSoup

# Infinite loop

while True:

    # Connect to database file and get a "cursor"
    # Windows OS/Firefox
    console = sqlite3.connect("C:/Users/mfren/AppData/Roaming/Mozilla/Firefox/Profiles/bmgr8w5y.default/places.sqlite")
    cursor = console.cursor()

    # Query Firefox places.sqlite database for browsing history
    # No TOP command so LIMIT to 1 result and bring most recent to top (DESC)
    cursor.execute("SELECT datetime(moz_historyvisits.visit_date/1000000, 'unixepoch', 'localtime') AS Time, moz_places.url FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id ORDER BY Time DESC LIMIT 1;")

    # Get all the search results into a list (array)
    rows = cursor.fetchall()

    # Print out second row in the results set (URL)
    for row in rows:
        print row[1]
        # Store URL in variable
        url = row[1]

    soup = BeautifulSoup(urllib2.urlopen(url))
    # Retrieve HTML Title from URL
    urlTitle = soup.title.string
    # Truncate to limit to 140 characters (including 'I'm really liking ')
    urlTitle = urlTitle[:119] + (urlTitle[119:] and '...')
    # Unicode characters cause an error (on Windows) so decode
    print unidecode(urlTitle)

    # Close the console to disconnect from the database
    console.close()

    # Load in my keys and secrets from the credentials file into a list (array)
    file = open("TwitterCredentials.txt")
    creds = file.read().split('\n')

    # Create a new API wrapper, passing in my credentials one at a time
    api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

    # Find out what time it is now (in Coordinated Universal Time)
    timestamp = datetime.datetime.utcnow()

    # Post status update and get the response from Twitter
    response = api.PostUpdate("I'm really liking " + urlTitle)

    # Print out response text (should be the status update if everything worked)
    print("Status updated to: " + response.text)
    
    # Pause
    # 3600 is 1 hour
    time.sleep(20)