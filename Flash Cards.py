class flashcard:
    def __init__(self, word, meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash=[]
print("Welcome to flashcard Application")
while(True):
    word=input("Enter the name you want to add to flashcard: ")
    meaning=input("Enter the meaning of the word: ")
    flash.append(flashcard(word, meaning))
    option=int(input("Enter 0, If you want to add another flashcard otherwise enter 1: "))
    if (option):
        break 
print("\nYour Flashcards")
for i in flash:
    print(">", i)