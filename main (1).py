#The word that shows up the most often
#How many unique four-letter words are in the book
#Every word that shows up more than 500 times, and how many times that word shows up 
    #throughout the book (see the "Walkthrough" section for an example)




# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

draculaText = readBook()

#split text
draculaWords = draculaText.split()

#Dracula Dictionary
dracula = {}

for eachWord in draculaWords:
  if eachWord in dracula:
    dracula[eachWord] += 1
  else:
    dracula[eachWord] = 1

#print(dracula)
#What word shows up the most often?
#count each unique everytime it is used
#display the word with the highest count

mostWord = ""
highValue = 0

#for mWord in draculaWords:
 # if mWord 
for mWord in dracula:
  if dracula[mWord] > highValue:
    mostWord = mWord
    highValue = dracula[mWord] 

print(f"'{mostWord}' is the word that appears the most throught the text, a total of {highValue} times")
# 
    
print()  

#Find number of unique 4 letter words in txt
#find all words with a len(gth) = 4
#count the words count += 1
count = 0
#display final count

for fourLetter in dracula:
  if (len(fourLetter) == 4):
    count += 1


    

print(f"There are {count} words that are four letters long")
  



print()
#Display every word that appears more than 500 times
#Display how many times each of those words appears
#not sure, maybe a dictionary??
#then display results with a value > 500

#for key, value in pairs
# if (value) > 500:
# print (f"{key} {value}")
biggestWords = ""
largeValue = 499

print("I noticed that these words show up 500 or more times:")
for bigWord in dracula:
  if dracula[bigWord] > largeValue:
    biggestWords = bigWord
    
    print(f" {bigWord} - {dracula[bigWord]} ")