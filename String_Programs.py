from collections import Counter
import string 

def capitalize_first_last_letter(Text):
   for w in Text.split(","):
    print(w[0].upper()+w[1:-1]+w[-1].upper(),end =' ') 

def find_maximum_occurance_of_charactres(Text):
   Counts=Counter(Text)
   result=Counts.most_common(1) 

def adding_spaces_in_the_beginning(Text):
    spaces=[char for char in Text if char==" "]
    no_of_spaces=len(spaces)
    result = " "*no_of_spaces + Text
    print(result)

def second_most_occurance_word(Text):
    Counts=Counter(Text)
    WordsCount=Counts.most_common(2)
    second_most_occurance_word=WordsCount[1]

def strip_char(Text,Char):
    Temp=[]
    for char in Text:
      if char not in Char:
        Temp.append(char)
        Result=''.join(Result)
    print(Result)  # This will strip specified character from text

def position_of_char(Text):
   for i,letter in enumerate(Test):
    print(f"Position od {letter} is at {i}") 

def check_all_are_alphabet(Text):
 characters=string.ascii_lowercase
 for char in Text:
     if char not in characters.lower() and char !=" ":
      print('Other than alphabets present')
    