import sys
import chardet
from typing import Dict
import os


def read_txt(txt_file: str) -> str: 
    """reads a .txt file and returns its content as a string"""
    with open(txt_file, "rb") as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding_detected = result['encoding']

    with open(txt_file, "r", encoding=encoding_detected) as file:
        txt_content = file.read()
        return txt_content


def ConstructBCT (word:str) -> Dict[str, int]: 
    """Constructs the BCT (bad character table)"""
    BCT={}
    for index, letter in enumerate(word): #enumerate(iterable, start=0) 
        BCT[letter]=index
    return BCT


def BoyerMoore (bm_text:str, bm_pattern:str, bad_character_table: Dict[str, int])->str:
    """Implements the Boyer Moore algorithm with a BCT"""
    len_text=len(bm_text)
    len_pattern=len(bm_pattern)
    pos=0
    coincidences=[]

    while pos<=len_text-len_pattern:
        counter=len_pattern-1
        #print("Comparando:", repr(bm_text[pos:pos + Len_pattern]))
        while counter >= 0 and bm_pattern[counter] == bm_text[pos + counter]:
            counter-=1
        if counter<0:
                coincidences.append(pos+1)
                pos += len_pattern
                continue
        else:
            mismatched_char=bm_text[pos + counter]
            if mismatched_char in bad_character_table:
                value=bad_character_table[mismatched_char]
                jump=max(1, counter-value)
            else: 
                jump=len_pattern
        pos+=jump
    if coincidences:
        return "coincidences found in positions: " + ", ".join(str(p) for p in coincidences)
    else:
        return "Coincidence not found"



textFile = input("Introduce the file (.txt) route:")
if not os.path.isfile(textFile):
    print(f"Error: File '{textFile}' does not exist.")
    exit()

pattern = input("Introduce the pattern you want to search for:")
if not pattern.strip():
    print("Error: Pattern is empty.")
    exit()

text = read_txt (textFile)
if not text.strip():
    print(f"Error: File '{textFile}' is empty.")
    exit()

pattern = pattern.lower()
text = text.lower()
#print (text, pattern)

result=BoyerMoore (text ,pattern, ConstructBCT(pattern))
print(result)