# Script to Tweet page title of most recently visited URL (Windows/Firefox and OSX/Chrome)

# Import the required libraries
import sqlite3
import urllib2
import twitter
import datetime
import time
import random
import sys
import shutil
from unidecode import unidecode
from BeautifulSoup import BeautifulSoup

# Define a list of prefixes
prefixList = ["I'm really liking: ", "Currently browsing: ", "Loitering around: ", "Why not join me at: "]

# Divider
divider = "*" * 100
spacer = "* "

# Function to pause loop and display a countdown
def countdown(t): # in seconds
    for i in range(t,0,-1):
        print spacer + 'Next update in %d seconds\r' % i,
        sys.stdout.flush()
        time.sleep(1)

# Infinite loop

while True:
    
    # Choose prefix at random
    prefix = random.choice(prefixList)
    
    # Generate 'random' number to prevent duplicate tweet issue
    randomNumber = random.randint(1000,9999)
    
    # Copy Chrome History file so we can query DB while Chrome is running (otherwise DB lock error)
    sourceFileChrome = "/Users/matthewfrench/Library/Application Support/Google/Chrome/Default/History"
    destinationFileChrome ="/Users/matthewfrench/Library/Application Support/Google/Chrome/Default/History_copy"
    shutil.copy(sourceFileChrome, destinationFileChrome)

    # Connect to database file and get a "cursor"
    
    # Windows OS/Firefox
    # console = sqlite3.connect("C:/Users/mfren/AppData/Roaming/Mozilla/Firefox/Profiles/bmgr8w5y.default/places.sqlite")
    
    # OSX/Chrome
    console = sqlite3.connect("/Users/matthewfrench/Library/Application Support/Google/Chrome/Default/History_copy")
    
    cursor = console.cursor()

    # Query Firefox places.sqlite database for browsing history
    # No TOP command so LIMIT to 1 result sorted by date and bring most recent to top (DESC)
    
    # Windows OS/Firefox
    # cursor.execute("SELECT datetime(moz_historyvisits.visit_date/1000000, 'unixepoch', 'localtime') AS Time, moz_places.url FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id ORDER BY Time DESC LIMIT 1;")
    
    # Query Chrome History database for browsing history
    # OSX/Chrome
    cursor.execute("SELECT datetime(((visits.visit_time/1000000)-11644473600), \"unixepoch\") AS Time, urls.url, urls.title FROM urls, visits WHERE urls.id = visits.url ORDER BY Time DESC LIMIT 1;")

    # Get all the search results into a list (array)
    rows = cursor.fetchall()

    # Print out second row in the results set (URL)
    for row in rows:
        print (divider)
        print (spacer + "URL: " + row[1])
        # Store URL in variable
        url = row[1]

    # Open URL
    # Add User Agent header to get around 403 error on some sites
    request = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
    soup = BeautifulSoup(urllib2.urlopen(request))
    # Retrieve HTML Title from URL
    # Printing unicode characters causes an error (on Windows) so decode
    urlTitle = unidecode(soup.title.string)
    # Truncate to limit to 140 characters (including prefix, random number and ellipsis)
    prefixTruncate = 140 - (len(prefix)+10)
    #print prefixTruncate
    urlTitle = urlTitle[:prefixTruncate] + (urlTitle[prefixTruncate:] and '...')
    
    # Print page title to console
    print (divider)
    print (spacer + "Page Title: " + urlTitle)
    print (divider)

    # Close the console to disconnect from the database
    console.close()

    # Load in my keys and secrets from the credentials file into a list (array)
    file = open("TwitterCredentials.txt")
    creds = file.read().splitlines()
    file.close

    # Create a new API wrapper, passing in my credentials one at a time
    api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

    # Find out what time it is now (in Coordinated Universal Time) - not used
    timestamp = datetime.datetime.utcnow()

    # Post status update and get the response from Twitter
    response = api.PostUpdate("(" + str(randomNumber) + ") " + prefix + urlTitle)

    # Print out response text (should be the status update if everything worked)
    print(spacer + "Status updated to: " + response.text)
    print (divider)
    
    # Pause and display countdown to next update
    countdown(20)