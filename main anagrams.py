# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    #return True

    if(len(word)==len(anagram)):
        sorted_str1=sorted(word)
        sorted_str2=sorted(anagram)

        if(sorted_str1 == sorted_str2):
            print("\nTrue")
            #return True
        else:
            print("\nFalse")
            #return False
    else:
        print(word + "and " + anagram + " are not anagram.")

find_anagram("stop","post")#the programme will reaturn trur because they are anagrams



