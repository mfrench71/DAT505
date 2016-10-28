# Script to Tweet last web page title and URL visited (Windows/Firefox)

# Import the required libraries
import sqlite3
import urllib2
import twitter
import datetime
import time
import random
from unidecode import unidecode
from BeautifulSoup import BeautifulSoup

# Define a list of prefixes
prefixList = ["I'm really liking ", "Currently browsing: ", "Loitering around: ", "Why not join me at "]

# Choose prefix at random
prefix = random.choice(prefixList)

# Infinite loop

while True:

    # Connect to database file and get a "cursor"
    # Windows OS/Firefox
    console = sqlite3.connect("C:/Users/mfren/AppData/Roaming/Mozilla/Firefox/Profiles/bmgr8w5y.default/places.sqlite")
    cursor = console.cursor()

    # Query Firefox places.sqlite database for browsing history
    # No TOP command so LIMIT to 1 result sorted by date and bring most recent to top (DESC)
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
    urlTitle = unidecode(soup.title.string)
    # Truncate to limit to 140 characters (including prefix and ellipsis)
    prefixTruncate = 140 - (len(prefix)+3)
    #print prefixTruncate
    urlTitle = urlTitle[:prefixTruncate] + (urlTitle[prefixTruncate:] and '...')
    
    # Printing unicode characters cause an error (on Windows) so decode
    print urlTitle

    # Close the console to disconnect from the database
    console.close()

    # Load in my keys and secrets from the credentials file into a list (array)
    file = open("TwitterCredentials.txt")
    creds = file.read().split('\n')

    # Create a new API wrapper, passing in my credentials one at a time
    api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

    # Find out what time it is now (in Coordinated Universal Time) - not used
    timestamp = datetime.datetime.utcnow()

    # Post status update and get the response from Twitter
    response = api.PostUpdate(prefix + urlTitle)

    # Print out response text (should be the status update if everything worked)
    print("Status updated to: " + response.text)
    
    # Pause
    # 3600 is 1 hour
    time.sleep(20)