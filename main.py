import os
from boyer_moore import BoyerMoore, ConstructBCT
from file_utils import read_txt

textFile = input("Introduce the path of the text file (.txt): ")
if not os.path.isfile(textFile):
    print(f"Error: File '{textFile}' does not exist.")
    exit()

pattern = input("Introduce the pattern you want to search for: ")
if not pattern.strip():
    print("Error: Pattern is empty.")
    exit()

text = read_txt(textFile)
if not text.strip():
    print(f"Error: File '{textFile}' is empty.")
    exit()

pattern = pattern.lower()
text = text.lower()

result = BoyerMoore(text, pattern, ConstructBCT(pattern))
print(result)
