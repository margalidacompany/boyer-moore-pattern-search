from typing import Dict

def ConstructBCT(word: str) -> Dict[str, int]: 
    """Constructs the BCT (bad character table)"""
    BCT = {}
    for index, letter in enumerate(word):
        BCT[letter] = index
    return BCT

def BoyerMoore(text: str, pattern: str, bad_character_table: Dict[str, int]) -> str:
    """Implements the Boyer Moore algorithm with a BCT"""
    len_text = len(text)
    len_pattern = len(pattern)
    pos = 0
    coincidences = []

    while pos <= len_text - len_pattern:
        counter = len_pattern - 1
        while counter >= 0 and pattern[counter] == text[pos + counter]:
            counter -= 1
        if counter < 0:
            coincidences.append(pos + 1)
            pos += len_pattern
            continue
        else:
            mismatched_char = text[pos + counter]
            if mismatched_char in bad_character_table:
                value = bad_character_table[mismatched_char]
                jump = max(1, counter - value)
            else: 
                jump = len_pattern
        pos += jump

    if coincidences:
        return "Coincidences found at positions: " + ", ".join(str(p) for p in coincidences)
    else:
        return "No coincidence found"
