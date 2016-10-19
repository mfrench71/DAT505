import random
import time
import wikipedia
from unidecode import unidecode

firstConversation = True
secondConversation = True
thirdConversation = True
result = ""

# Define stop words list

stopWords = ["a", "a's", "able", "about", "above", "abroad", "according", "accordingly", \
             "across", "actually", "adj", "after", "afterwards", "again", "against", "ago", \
             "ahead", "ain't", "aint", "all", "allow", "allows", "almost", "alone", "along",\
             "alongside", "already", "also", "although", "always", "am", "amid", "amidst", \
             "among", "amongst", "amoungst", "amount", "an", "and", "another", "any", "anybody", \
             "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere", "apart", "appear", \
             "appreciate", "appropriate", "are", "aren't", "arent", "around", "as", "aside", "ask", \
             "asking", "associated", "at", "available", "away", "awfully", "b", "back", "backward", \
             "backwards", "be", "became", "because", "become", "becomes", "becoming", "been", \
             "before", "beforehand", "begin", "behind", "being", "believe", "below", "beside", \
             "besides", "best", "better", "between", "beyond", "bill", "both", "bottom", "brief", \
             "but", "by", "c", "c'mon", "c's", "call", "came", "can", "can't", "cannot", "cant", \
             "caption", "cause", "causes", "certain", "certainly", "changes", "clearly", "cmon", \
             "co", "co.", "com", "come", "comes", "computer", "con", "concerning", "consequently",\
             "consider", "considering", "contain", "containing", "contains", "corresponding", "could",\
             "couldn't", "couldnt", "course", "cry", "currently", "d", "dare", "daren't", "darent", \
             "de", "definitely", "describe", "described", "despite", "detail", "did", "didn't", \
             "didnt", "different", "directly", "do", "does", "doesn't", "doesnt", "doing", "don't", \
             "done", "dont", "down", "downwards", "due", "during", "e", "each", "edu", "eg", "eight",\
             "eighty", "either", "eleven", "else", "elsewhere", "empty", "end", "ending", "enough",\
             "entirely", "especially", "et", "etc", "even", "ever", "evermore", "every", "everybody", \
             "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "f",\
             "fairly", "far", "farther", "few", "fewer", "fifteen", "fifth", "fify", "fill", "find", \
             "fire", "first", "five", "followed", "following", "follows", "for", "forever", "former",\
             "formerly", "forth", "forty", "forward", "found", "four", "from", "front", "full", "further", "furthermore", "g", "get", "gets", "getting", "give", "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "h", "had", "hadn't", "hadnt", "half", "happens", "hardly", "has", "hasn't", "hasnt", "have", "haven't", "havent", "having", "he", "he'd", "he'll", "he's", "hello", "help", "hence", "her", "here", "here's", "hereafter", "hereby", "herein", "heres", "hereupon", "hers", "herse", "herself", "hi", "him", "himse", "himself", "his", "hither", "hopefully", "how", "how's", "howbeit", "however", "hows", "hundred", "i", "i'd", "i'll", "i'm", "i've", "ie", "if", "ignored", "immediate", "in", "inasmuch", "inc", "inc.", "indeed", "indicate", "indicated", "indicates", "inner", "inside", "insofar", "instead", "interest", "into", "inward", "is", "isn't", "isnt", "it", "it'd", "it'll", "it's", "itd", "itll", "its", "itse", "itself", "j", "just", "k", "keep", "keeps", "kept", "know", "known", "knows", "l", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "let's", "lets", "like", "liked", "likely", "likewise", "little", "look", "looking", "looks", "low", "lower", "ltd", "m", "made", "mainly", "make", "makes", "many", "may", "maybe", "mayn't", "maynt", "me", "mean", "meantime", "meanwhile", "merely", "might", "mightn't", "mightnt", "mill", "mine", "minus", "miss", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "much", "must", "mustn't", "mustnt", "my", "myse", "myself", "n", "name", "namely", "nd", "near", "nearly", "necessary", "need", "needn't", "neednt", "needs", "neither", "never", "neverf", "neverless", "nevertheless", "new", "next", "nine", "ninety", "no", "no-one", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "not", "nothing", "notwithstanding", "novel", "now", "nowhere", "o", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "on", "once", "one", "one's", "ones", "only", "onto", "opposite", "or", "other", "others", "otherwise", "ought", "oughtn't", "oughtnt", "our", "ours", "ourselves", "out", "outside", "over", "overall", "own", "p", "part", "particular", "particularly", "past", "per", "perhaps", "placed", "please", "plus", "possible", "presumably", "probably", "provided", "provides", "put", "q", "que", "quite", "qv", "r", "rather", "rd", "re", "really", "reasonably", "recent", "recently", "regarding", "regardless", "regards", "relatively", "respectively", "right", "round", "s", "said", "same", "saw", "say", "saying", "says", "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "shan't", "shant", "she", "she'd", "she'll", "she's", "shes", "should", "shouldn't", "shouldnt", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somebody", "someday", "somehow", "someone", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify", "specifying", "still", "sub", "such", "sup", "sure", "system", "t", "t's", "take", "taken", "taking", "tell", "ten", "tends", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "that's", "that've", "thatll", "thats", "thatve", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "there'd", "there'll", "there're", "there's", "there've", "thereafter", "thereby", "thered", "therefore", "therein", "therell", "therere", "theres", "thereupon", "thereve", "these", "they", "they'd", "they'll", "they're", "they've", "theyd", "theyll", "theyre", "theyve", "thick", "thin", "thing", "things", "think", "third", "thirty", "this", "thorough", "thoroughly", "those", "though", "three", "through", "throughout", "thru", "thus", "till", "to", "together", "too", "took", "top", "toward", "towards", "tried", "tries", "truly", "try", "trying", "twelve", "twenty", "twice", "two", "u", "un", "under", "underneath", "undoing", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "up", "upon", "upwards", "us", "use", "used", "useful", "uses", "using", "usually", "v", "value", "various", "versus", "very", "via", "viz", "vs", "w", "want", "wants", "was", "wasn't", "wasnt", "way", "we", "we'd", "we'll", "we're", "we've", "welcome", "well", "went", "were", "weren't", "werent", "weve", "what", "what'll", "what's", "what've", "whatever", "whatll", "whats", "whatve", "when", "when's", "whence", "whenever", "whens", "where", "where's", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which", "whichever", "while", "whilst", "whither", "who", "who'd", "who'll", "who's", "whod", "whoever", "whole", "wholl", "whom", "whomever", "whos", "whose", "why", "why's", "whys", "will", "willing", "wish", "with", "within", "without", "won't", "wonder", "wont", "would", "wouldn't", "wouldnt", "x", "y", "yes", "yet", "you", "you'd", "you'll", "you're", "you've", "youd", \
             "youll", "your", "youre", "yours", "yourself", "yourselves", "youve", "z", "zero"]

# Define pairs of trigger strings and responses

greetings = ['hola', 'hello', 'hi','hey!','hello','hey']
questions = ['how are you?','how are you doing?','how are you','how are you feeling','how are you today']
responses = ['Okay','I am fine','very good','very well','not so good']
validations = ['yes','yeah','yea','no','nah','of course','of course not']
confirmations = ['are you sure?','you sure?','you sure?','sure?','really?','honestly?','definintely?']
names = ['Matthew','Simon','Bob']
prompts = ['What can I do for you?','Do you have a question for me?','How about a nice game of chess?','Is there something you wanted to ask?']
unrecognised = ["I'm sorry, I did not understand","Come again?","Try asking something else",'Could you rephrase that?']

link_pairs = (greetings, greetings), (questions, responses), (confirmations, validations)

# Divider

divider = "****************************************************"

# Get the current hour and year

current_hour = time.strptime(time.ctime(time.time())).tm_hour
current_year = time.strptime(time.ctime(time.time())).tm_year

# Set age for PC

pcAge = random.randint(16,65)

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

print("Hello. What is your name?")
tempName = raw_input()
stripWords(tempName)

# Time-based greeting based on hour with random name returned
# Capitalise first letter of name in case it is entered in lower case

print(divider)

myName = result.capitalize()
print(greeting + ", " + myName)
pcName = random.choice(names)
print("My name is " + pcName)

# Check user's name against random name and display message if equal

if pcName == result.capitalize():
    print("What a coincidence!")

# Testing stripWords function

print(divider)

print("Tell me something interesting about yourself")

query = raw_input()
stripWords(query)

print(divider)

print("This is what I found interesting...")

if result:
    print(result)
else:
    print("Not much")

print(divider)

print("Here's what I found out about " + query + " ... ")

# Use Unidecode to allow Windows to display unsupported characters
# Limit to returning one sentence

print unidecode(wikipedia.summary(result, sentences = 1))

# Wikipedia library test

print(divider)

print("What would you like to know about?")

query = raw_input()
stripWords(query)

print(divider)
print("Here's what I found out about " + query + " ... ")

# Use Unidecode to allow Windows to display unsupported characters
# Limit to returning one sentence

print unidecode(wikipedia.summary(query, sentences = 1))
    
# Age

print(divider)

while True:
    try:
        print("How old are you, " + myName)
        myAge = int(raw_input())
    except ValueError:
        print("Sorry, " + myName + "; I didn't understand that.")
        #Invalid input - return to the start of the loop
        continue
    else:
        #Valid input - exit loop
        break
if myAge == pcAge: 
    print(divider)
    print("We are the same age, " + myName)
    print(divider)
else:
    if myAge > pcAge:
        print(divider)
        print("I am younger than you, " + myName)
        print(divider)
    else:
        if myAge < pcAge:
            print(divider)
            print("You are older than me, " + myName)
            print(divider)
            
birthYear = str((current_year - myAge))
            
print("You were born in " + birthYear)

print(divider)
      
print unidecode(wikipedia.summary(birthYear, sentences = 1))

# First conversation looks for specific occurences of words   

print(divider)

while firstConversation:
    
    followUp = raw_input(random.choice(prompts))
    
    if 'old' in followUp:
        print("A gentleman doesn't ask")
        print(" ... but as it happens, I am " + str(pcAge) + " years old")
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
                #print(random.choice(unrecognised))
                print("I didn't get that, so let's move on ... ")
                firstConversation = False
                
# Second conversation is more random and uses lists as keywords and responses
                
while secondConversation:
    
    print("*** We are now in secondConversation ***")
    
    # Prompt user with a random prompt
    print(random.choice(prompts))
    userInput = raw_input()
    for triggers, outputs in link_pairs:
        if not userInput.lower() in triggers:
            continue
            
        random_output = random.choice(outputs)
            
        print(random_output)
        break
        
    else:
        if 'sure' in userInput:
            response = "Sure about what?"
            print response
        else:
            print(random.choice(unrecognised))
            secondConversation = False
            
myQuestions = ['What are you doing?','What are you up to?']
pcAnswers = ['I am talking to you','I am typing this']
myFollowUps = ['Thats nice','Oh dear']
pcFollowUps = ['Thank you','I know']
linkedQA = (myQuestions,pcAnswers), (myFollowUps,pcFollowUps)

print("*** We are now in thirdConversation")

while thirdConversation:
    
    # Prompt user with a random prompt
    print(random.choice(prompts))
    
    myQuestion = raw_input()
    for questions, answers in linkedQA:
        if not myQuestion in questions:
            continue
            
        random_answer = random.choice(answers)
        print(random_answer)
        
        myFollowUp = raw_input()
        for questions, answers in linkedQA:
            if not myFollowUp in questions:
                continue
                
            random_followUp = random.choice(answers)
            print(random_followUp)
        
        break
        
    else:
        if 'sure' in userInput:
            response = "Sure about what?"
            print response
        else:
            print(random.choice(unrecognised))
            #thirdConversation = False