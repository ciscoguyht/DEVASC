
#!/usr/bin/env python3  
from urllib.request import urlopen

def fetch_words():
    story = urlopen("http://sixty-north.com/c/t.txt")
    listOfWords = []
    for line in story:
        lines = line.decode("utf8").split()
        for words in lines:
           listOfWords.append(words)

    story.close()
    return listOfWords

def print_words(listOfWords):
    for mot in listOfWords:
        print (mot)
        #return (mot)

def main():
    words = fetch_words()
    print_words(words)

#print(__name__)
if __name__ == "__main__":
    main()
    


#fetch_words , first loop with split method return a list of words for each line   Exam:['It', 'was', 'the', 'best', 'of', 'times']
#fetch_words , first loop with split method print a list of words for only first line   Exam:['It', 'was', 'the', 'best', 'of', 'times']
#fetch_words , first loop with split method, second loop  return a list of all words within the webpage:             Example: ['It', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst'

#fetch_words , first loop with strip method print lines (exact match of website)  Exam: It was the best of times
#fetch_words , first loop with strip method return only first line inside of parenthesis   Exam: 'It was the best of times'
#fetch_words , first loop with split method, second loop  return a list of all characters within the webpage:        Example :['I', 't', ' ', 'w', 'a', 's', ' ', 't', 'h', 'e', ' ', 'b', 'e', 's', 't', ' ', 'o', 'f', ' ', 't', 'i',

#main  with strip method print a character per line
#main with split method  print a word per line 
