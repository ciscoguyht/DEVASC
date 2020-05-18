
from urllib.request import urlopen

def fetch_words():
    story = urlopen("http://sixty-north.com/c/t.txt")
    listOfWords = []
    for line in story:
        lines = line.decode("utf8").split()
        for words in lines:
            listOfWords.append(words)

    story.close()

    for mot in listOfWords:
        print (mot)
    
#print(__name__)
if __name__ == "__main__":
    fetch_words()
