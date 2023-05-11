import random

# Creating a main function that displays the entire sentence and calls the make_sentence function with the parameters requested in the assignment.
def main():
    make_sentence(1,"past")
    make_sentence(1,"present")
    make_sentence(1,"future")
    make_sentence(2,"past")
    make_sentence(2,"present")
    make_sentence(2,"future")
    pass

# Function that build that sentence merging all the functions that generates the words 
def make_sentence(quantity, tense):
    sentence = get_determiner(quantity).capitalize()+" "+get_adjective().lower()+" "+get_noun(quantity)+" "+get_prepositional_phrase(quantity)+" "+get_verb(quantity,tense)
    print(sentence)
    return sentence

# Function to randomly select a determiner with condition to check if it's singular or plural 
def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word

# Function to randomly select an adjective
def get_adjective():
    adjectives = ["Artificial","Bad","Big ","Small","Beautiful","Boring","Classic","Cool","Cute","Dangerous","Delicate","Elegant","Fast","Friendly","Unfriendly","Good","Intelligent","Lovely","Old ","New","Popular","Poor","Quiet","Red","Blue","Green","Black","White","Yellow","Orange","Purple"]
    return random.choice(adjectives)

# Function to randomly select a noun with condition to check if it's singular or plural 
def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else: nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    return random.choice(nouns)

# Function to randomly select a verb based on the tense with condition to check if it's past ,present or future.
def get_verb(quantity, tense):
    word_tense = []
    if tense.lower() == "past":
        word_tense = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense.lower() == "present" and quantity == 1:
        word_tense = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    elif tense.lower() == "present" and quantity != 1:
        word_tense = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense.lower() == "future":
        word_tense = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    randon_words = random.choice(word_tense)
    return randon_words

# Function to randomly select an preposition
def get_preposition():
    prepositions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    return random.choice(prepositions)

# Function that build that sentence merging the functions prepositions determiner and noun. 
# This frase will be use in the make_sentence Function
def get_prepositional_phrase(quantity):
    prepositional_phase = get_preposition()+" "+get_determiner(quantity)+" "+get_noun(quantity)
    return prepositional_phase

main()
