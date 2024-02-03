#hangman text based game

import random
import sqlite3



words = ['about', 'above', 'abuse', 'accept', 'accident', 'accuse', 'across', 'activist', 'actor', 'administration', 'admit', 'adult', 'advertise', 'advise',
         'affect', 'afraid', 'after', 'again', 'against', 'agency', 'aggression', 'agree', 'agriculture', 'force', 'airplane', 'airport', 'album', 'alcohol',
         'alive', 'almost', 'alone', 'along', 'already', 'although', 'always', 'ambassador', 'amend', 'ammunition', 'among', 'amount', 'anarchy', 'ancestor',
         'ancient', 'anger', 'animal', 'anniversary', 'announce', 'another', 'answer', 'apologize', 'appeal', 'appear', 'appoint', 'approve', 'archeology',
         'argue', 'around', 'arrest', 'arrive', 'artillery', 'assist', 'astronaut', 'astronomy', 'asylum', 'atmosphere', 'attach', 'attack', 'attempt', 'attend',
         'attention', 'automobile', 'autumn', 'available', 'average', 'avoid', 'awake', 'award', 'balance', 'balloon', 'ballot', 'barrier', 'battle', 'beauty',
         'because', 'become', 'before', 'begin', 'behavior', 'behind', 'believe', 'belong', 'below', 'betray', 'better', 'between', 'biology', 'black', 'blame',
         'bleed', 'blind', 'block', 'blood', 'border', 'borrow', 'bottle', 'bottom', 'boycott', 'brain', 'brave', 'bread', 'breathe', 'bridge', 'brief', 'bright',
         'bring', 'broadcast', 'brother', 'brown', 'budget', 'build', 'building', 'bullet', 'burst', 'business', 'cabinet', 'camera', 'campaign', 'cancel', 'cancer',
         'candidate', 'capital', 'capture', 'career', 'careful', 'carry', 'catch', 'cause', 'ceasefire', 'celebrate', 'center', 'century', 'ceremony', 'chairman',
         'champion', 'chance', 'change', 'charge', 'chase', 'cheat', 'cheer', 'chemicals', 'chemistry', 'chief', 'child', 'children', 'choose', 'circle', 'citizen',
         'civilian', 'civil', 'rights', 'claim', 'clash', 'clean', 'clear', 'clergy', 'climate', 'climb', 'clock', 'close', 'cloth', 'clothes', 'cloud', 'coalition',
         'coast', 'coffee', 'collapse', 'collect', 'college', 'colony', 'color', 'combine', 'command', 'comment', 'committee', 'common', 'communicate', 'community',
         'company', 'compare', 'compete', 'complete', 'complex', 'compromise', 'computer', 'concern', 'condemn', 'condition', 'conference', 'confirm', 'conflict',
         'congratulate', 'congress', 'connect', 'conservative', 'consider', 'constitution', 'contact', 'contain', 'container', 'continent', 'control', 'convention',
         'cooperate', 'correct', 'corruption', 'cotton', 'count', 'country', 'court', 'cover', 'crash', 'create', 'creature', 'credit', 'crime', 'criminal', 'crisis',
         'criticize', 'crops', 'cross', 'crowd', 'crush', 'culture', 'curfew', 'current', 'custom', 'customs', 'damage', 'dance', 'danger', 'daughter', 'debate',
         'decide', 'declare', 'decrease', 'defeat', 'defend', 'deficit', 'define', 'degree', 'delay', 'delegate', 'demand', 'democracy', 'demonstrate', 'denounce',
         'depend', 'deplore', 'deploy', 'depression', 'describe', 'desert', 'design', 'desire', 'destroy', 'detail', 'detain', 'develop', 'device', 'dictator',
         'different', 'difficult', 'dinner', 'diplomat', 'direct', 'direction', 'disappear', 'disarm', 'disaster', 'discover', 'discrimination', 'discuss',
         'disease', 'dismiss', 'dispute', 'dissident', 'distance', 'divide', 'doctor', 'document', 'dollar', 'donate', 'double', 'dream', 'drink', 'drive', 'drown',
         'during', 'early', 'earth,' 'earthquake', 'ecology', 'economy', 'education', 'effect', 'effort', 'either', 'elect', 'electricity', 'embassy', 'embryo',
         'emergency', 'emotion', 'employ', 'empty', 'enemy', 'energy', 'enforce', 'engine', 'engineer', 'enjoy', 'enough', 'enter', 'environment', 'equal',
         'equipment', 'escape', 'especially', 'establish', 'estimate', 'ethnic', 'evaporate', 'event', 'every', 'evidence', 'exact', 'examine', 'example',
         'excellent', 'exchange', 'excuse', 'execute', 'exercise', 'exile', 'exist', 'expand', 'expect', 'expel', 'experience', 'experiment', 'expert', 'explain',
         'explode', 'explore', 'export', 'express', 'extend', 'extra', 'extraordinary', 'extreme', 'extremist', 'factory', 'false', 'family', 'famous', 'father',
         'favorite', 'federal', 'female', 'fence', 'fertile', 'field', 'fierce', 'fight', 'final', 'financial', 'finish', 'fireworks', 'first', 'float', 'flood',
         'floor', 'flower', 'fluid', 'follow', 'force', 'foreign', 'forest', 'forget', 'forgive', 'former', 'forward', 'freedom', 'freeze', 'fresh', 'friend',
         'frighten', 'front', 'fruit', 'funeral', 'future', 'gather', 'general', 'generation', 'genocide', 'gentle', 'glass', 'goods', 'govern', 'government',
         'grain', 'grass', 'great', 'green', 'grind', 'ground', 'group', 'guarantee', 'guard', 'guerrilla', 'guide', 'guilty', 'happen', 'happy', 'harvest',
         'headquarters', 'health', 'heavy', 'helicopter', 'hijack', 'history', 'holiday', 'honest', 'honor', 'horrible', 'horse', 'hospital', 'hostage', 'hostile',
         'hotel', 'house', 'however', 'human', 'humor', 'hunger', 'hurry,' 'husband', 'identify', 'ignore', 'illegal', 'imagine', 'immediate', 'immigrant',
         'important', 'improve', 'incident', 'incite', 'include', 'increase', 'independent', 'individual', 'industry', 'infect', 'inflation', 'influence', 'inform',
         'information', 'inject', 'injure', 'innocent', 'insane', 'insect', 'inspect', 'instead', 'instrument', 'insult', 'intelligence', 'intelligent', 'intense',
         'interest', 'interfere', 'international', 'internet', 'intervene', 'invade', 'invent', 'invest', 'investigate', 'invite', 'involve', 'island', 'issue',
         'jewel', 'joint', 'judge', 'justice', 'kidnap', 'knife', 'knowledge', 'labor', 'laboratory', 'language', 'large', 'laugh', 'launch', 'learn', 'leave',
         'legal', 'legislature', 'letter', 'level', 'liberal', 'light', 'lightning', 'limit', 'liquid', 'listen', 'literature', 'little', 'local', 'lonely',
         'loyal', 'machine', 'magazine', 'major', 'majority', 'manufacture', 'march', 'market', 'marry', 'material', 'mathematics', 'matter', 'mayor', 'measure',
         'media', 'medicine', 'member', 'memorial', 'memory', 'mental', 'message', 'metal', 'method', 'microscope', 'middle', 'militant', 'military', 'militia',
         'mineral', 'minister', 'minor', 'minority', 'minute', 'missile', 'missing', 'mistake', 'model', 'moderate', 'modern', 'money', 'month', 'moral', 'morning',
         'mother', 'motion', 'mountain', 'mourn', 'movement', 'movie', 'murder', 'music', 'mystery', 'narrow', 'nation', 'native', 'natural', 'nature', 'necessary',
         'negotiate', 'neighbor', 'neither', 'neutral', 'never', 'night', 'noise', 'nominate', 'normal', 'north', 'nothing', 'nowhere', 'nuclear', 'number', 'object',
         'observe', 'occupy', 'ocean', 'offensive', 'offer', 'office', 'officer', 'official', 'often', 'operate', 'opinion', 'oppose', 'opposite', 'oppress,'
         'orbit', 'order', 'organize', 'other', 'overthrow', 'paint', 'paper', 'parachute', 'parade', 'pardon', 'parent', 'parliament', 'partner', 'party',
         'passenger', 'passport', 'patient', 'peace', 'people', 'percent', 'perfect', 'perform', 'period', 'permanent', 'permit', 'person', 'persuade', 'physical',
         'physics', 'picture', 'piece', 'pilot', 'place', 'planet', 'plant', 'plastic', 'please', 'plenty', 'point', 'poison', 'police', 'policy', 'politics',
         'pollute', 'popular', 'population', 'position', 'possess', 'possible', 'postpone', 'poverty', 'power', 'praise', 'predict', 'pregnant', 'present',
         'president', 'press', 'pressure', 'prevent', 'price', 'prison', 'private', 'prize', 'probably', 'problem', 'process', 'produce', 'profession',
         'professor', 'profit', 'program', 'progress', 'project', 'promise', 'propaganda', 'property', 'propose', 'protect', 'protest', 'prove', 'provide',
         'public', 'publication', 'publish', 'punish', 'purchase', 'purpose', 'quality', 'question', 'quick', 'quiet', 'radar', 'radiation', 'radio', 'railroad',
         'reach', 'react', 'ready', 'realistic', 'reason', 'reasonable', 'rebel', 'receive', 'recent', 'recession', 'recognize', 'record', 'recover', 'reduce',
         'reform', 'refugee', 'refuse', 'register', 'regret', 'reject', 'relations', 'release', 'religion', 'remain', 'remains', 'remember', 'remove', 'repair',
         'repeat', 'report', 'represent', 'repress', 'request', 'require', 'rescue', 'research', 'resign', 'resist', 'resolution', 'resource', 'respect',
         'responsible', 'restaurant', 'restrain', 'restrict', 'result', 'retire', 'revolt', 'right', 'river', 'rocket', 'rough', 'round', 'rubber', 'rural',
         'sabotage', 'sacrifice', 'sailor', 'satellite', 'satisfy', 'school', 'science', 'search', 'season', 'second', 'secret', 'security', 'seeking', 'seize',
         'senate', 'sense', 'sentence', 'separate', 'series', 'serious', 'serve', 'service', 'settle', 'several', 'severe', 'shake', 'shape', 'share', 'sharp',
         'sheep', 'shell', 'shelter', 'shine', 'shock', 'shoot', 'short', 'should', 'shout', 'shrink', 'sickness', 'signal', 'silence', 'silver', 'similar',
         'simple', 'since', 'single', 'sister', 'situation', 'skeleton', 'skill', 'slave', 'sleep', 'slide', 'small', 'smash', 'smell', 'smoke', 'smooth', 'social',
         'soldier', 'solid', 'solve', 'sound', 'south', 'space', 'speak', 'special', 'speech', 'speed', 'spend', 'spill', 'spirit', 'split', 'sport', 'spread',
         'spring', 'square', 'stand', 'start', 'starve', 'state', 'station', 'statue', 'steal', 'steam', 'steel', 'stick', 'still', 'stone', 'store', 'storm',
         'story', 'stove', 'straight', 'strange', 'street', 'stretch', 'strike', 'strong', 'structure', 'struggle', 'study', 'stupid', 'subject', 'submarine',
         'substance', 'substitute', 'subversion', 'succeed', 'sudden', 'suffer', 'sugar', 'suggest', 'suicide', 'summer', 'supervise', 'supply', 'support', 'suppose',
         'suppress', 'surface', 'surplus', 'surprise', 'surrender', 'surround', 'survive', 'suspect', 'suspend', 'swallow', 'swear', 'sweet', 'sympathy', 'system',
         'target', 'taste', 'teach', 'technical', 'technology', 'telephone', 'telescope', 'television', 'temperature', 'temporary', 'tense', 'terrible', 'territory',
         'terror', 'terrorist', 'thank', 'theater', 'theory', 'there', 'these', 'thick', 'thing', 'think', 'third', 'threaten', 'through', 'throw', 'tired', 'today',
         'together', 'tomorrow', 'tonight', 'torture', 'total', 'touch', 'toward', 'trade', 'tradition', 'traffic', 'tragic', 'train', 'transport', 'transportation',
         'travel', 'treason', 'treasure', 'treat', 'treatment', 'treaty', 'trial', 'tribe', 'trick', 'troops', 'trouble', 'truce', 'truck', 'trust', 'under',
         'understand', 'unite', 'universe', 'university', 'unless', 'until', 'urgent', 'usual', 'vacation', 'vaccine', 'valley', 'value', 'vegetable', 'vehicle',
         'version', 'victim', 'victory', 'video', 'village', 'violate', 'violence', 'visit', 'voice', 'volcano', 'volunteer', 'wages', 'waste', 'watch', 'water',
         'wealth', 'weapon', 'weather', 'weigh', 'welcome', 'wheat', 'wheel', 'where', 'whether', 'which', 'white', 'whole', 'willing', 'window', 'winter',
         'withdraw', 'without', 'witness', 'woman', 'wonder', 'wonderful', 'world', 'worry', 'worse', 'worth', 'wound', 'wreck', 'wreckage', 'write', 'wrong',
         'yellow', 'yesterday', 'young', 'zebra']
#words = ['spaghetti', 'flight']


#words = ['will']
#-----------------------------------------------------------------------------#

#this literall just picks a random word form the list and then generates
#string that is the same length but is all asterisks
def word_pick(words):
    word = random.choice(words)#this picks a random word from the list
    x_word = ''
    for letters in word:
        x_word=x_word+"*"
    return(word, x_word)

#stole this off stack overflow but it replaces the letter in a string based
#on the index, nothing in it is mine lmao - 'ti7' on stack overflow
def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]



#this is the fucntion that takes the users guess and displays how much they
#got right in the word
def guess(word, a, incorrect_letters):#new word is the returned variable
    global won, lives, x_word, guessed_letters, guesses
    repeat = False
    if won == False:
        guess = input("enter your guess: ")
        geuss = guess.lower()
    else:
        guess = '495768374'
    count=-1
    new_word = x_word
    #incorrect_letters=[]
    correct_letters = []
    for letter in x_word:
        if letter != '*':
            correct_letters.append(letter)
    #print(correct_letters)

    if len(guess) == 1:#if the guess is 1 character
        
        if guess in correct_letters or guess in incorrect_letters:
            screen_clear()
            print('you have already guessed this letter, try again')
            repeat = True

        for letter in word:#loops thru each letter
            count = count +1
            if letter == guess and repeat == False:#if the guess is correct
                repeat = True
                x_word = replacer(x_word, guess, count)
                screen_clear()
                print('correct guess!')
                guesses = guesses +1
            elif letter == guess:#had to make another if bcs the first one would add to the guesses which is effectively the score if there was a double letter which meseed up the leaderboard
                x_word = replacer(x_word, guess, count)
                
        if guess not in word and guess not in incorrect_letters:#if its a new
            incorrect_letters = letter_bank(guess, incorrect_letters)
            screen_clear()
            print('incorrect guess')
            global lives
            lives =lives +1
            guesses = guesses+1
            
    elif len(guess) == len(word):
        if guess == word:
            guesses = guesses+1
            win()
        if guess != word:
            print('incorrect guess')
            lives = lives +1
    elif guess == '495768374':
        x=1
    elif guess == '':
        pooop = 1
        screen_clear()
    else:
        screen_clear()
        print('incorrect guess')
        lives = lives+1

    if x_word == word:
        win()

    #print('guessed letters: '+str(incorrect_letters))
    #print(correct_letters)
    
                
                 
        
#this jus does the guess() subroutine again bcs it didnt let me call it inside
#of itself
def reguess(word, x_word, incorrect_letters):
    #print('you have already guessed this letter, try again')
    guess(word, x_word, incorrect_letters)

#this jus prints a bunch of empty lines so the screan gets cleared
def screen_clear():
    f = open('hangman states\empty.txt', 'r')
    print(f.read())
    f.close()

#this displays how ever far thru you are in drawing the hangman person
#stage is how far thru you are (0-12, 12 being lost)
def lives_left(stage):
    if stage == 13:
        loose()
    else:
        f = open('hangman states\hangman'+ str(stage) +'.txt', 'r')
        print(f.read())
        f.close()

#the rules and how to play
def rules():
    print("this is a text based hangman game. the computer will randomly")
    print("select a word and you will either have to guess a letter or guess")
    print("the entire word. if you guess the correct letter it will be revealed")
    print("within the hidden word and if you guess a letter incorrectly it will")
    print("be added to the 'letter bank'. you can also guess the entire word")
    print("if you think you know it. once you have inputted your name, your")
    print("score will then be added to the leaderboard if you win (fewer guesses")
    print("means a higher score!)")
    print()


#what happens when you have won the game
def win():
    global won, player_name
    won = True
    screen_clear()
    f = open('hangman states\cake.txt', 'r')
    print(f.read())
    f.close()
    print('horray, you won!')
    print('the hidden word was {}, and you guessed it in {} guesses!'.format(word, guesses))
    print('ready for anothe round?')

    con = sqlite3.connect('scores.db')
    curs = con.cursor()
    values = [player_name, guesses]
    curs.execute("INSERT INTO player_score VALUES(?,?)", values)
    con.commit()

def loose():
    global won, name
    won = True
    screen_clear()
    f = open('hangman states\death.txt', 'r')
    print(f.read())
    f.close()
    print('uh oh, you lost :(')
    print('the hidden word was {}'.format(word))
    print('wanna try again?')
    print()

def letter_bank(guess, incorrect_letters):
    incorrect_letters.append(guess)
    return(incorrect_letters)

def output(x_word, guessed_letters):
    print()
    print('guessed letters: '+str(incorrect_letters))
    print()
    print('hidden word: '+x_word)
    print()


def leaderboard():
    #i know i shouldtn open the database in here but it doesnt exactly need to
    #optimesd for speed so im going to open and close it each time i load it
    #i also loaded the entire database each time bcs i dont know how to load the
    #top 5 scores
    con = sqlite3.connect('scores.db')
    curs = con.cursor()
    i = 1
    names = []
    screen_clear()
    print('Leaderboard:')
    print()
    print('place: name, guesses')
    print()
    print()
    for row in curs.execute("SELECT * FROM player_score ORDER BY guesses asc"):
        if row[0] not in names and i <= 10:            
            print('{}: {}, {} guesses'.format(i, row[0], row[1]))
            i = i+1
            names.append(row[0])

def change_name():
    global player_name
    print()
    player_name = input('name: ')
    print()
    
#------------------------------------------------------------------------------#
print('4'+'4')

#main script

running = True
player_name = ''


screen_clear()
rules()

while running == True:
    incorrect_letters = []
    lives = 1
    word = word_pick(words)
    x_word = word[1]
    word = word[0]
    won = False
    guessed_letters = []
    guesses = 0
    
    print()
    if player_name == '':
        change_name()
    print('1: play')
    print('2: change name')
    print('3: view leaderboard')
    print('4: quit')
    play = str(input("enter your choice (1/2/3/4): "))
    if play == '1':
        screen_clear()
        while won == False:
            output(x_word, guessed_letters)
            lives_left(lives)
            guess(word, x_word, incorrect_letters)
            
    elif play == '2':
        change_name()
        
    elif play == '3':
        leaderboard()
        
    elif play == '4':
        quit()
    else:
        print("incorrect input")

    
