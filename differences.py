import difflib

#Source: pymotw: The difflib module contains tools for computing and working with differences between sequences. 
#It is especially useful for comparing text, and includes functions that produce reports using several common difference formats.

def compare_strings(str1, str2):
    if str1 == str2:
        print("They match!")
    else:
        print("They don't match! Differences:")
        diff = difflib.ndiff(str1, str2)
        highlighted_diff = "".join(f"[{char[2:]}]" if char.startswith('-') else char[2:] for char in diff)
        print(highlighted_diff)

#Input
string1 = "Hello World!"
string2 = "hello, World"

compare_strings(string1, string2)