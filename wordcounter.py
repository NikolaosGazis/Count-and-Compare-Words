# Libraries #
import re # regular expressions.

# Functions #
def count_words(words):
    count = words.count('"') # must be an even number, else there is an error.
    
    if (count % 2 == 0):
        return count // 2
    else:
        print("Number of quotes are odd, check again.")

def extract_words(input_words):
    # Find all words enclosed in double quotes, including spaces #
    words = re.findall(r'"([^"]+)"', input_words)
    return words

def find_common_words(in_words1, in_words2):
    words1 = extract_words(in_words1)
    words2 = extract_words(in_words2)
    
    # Find Common Words #
    common_words = set(words1) & set(words2)
    return common_words 

def main():
    input_words1 = str(input("\n[SYSTEM] Give your words/strings: "))
    
    # Count words #
    total_words = count_words(input_words1)
    print("\n[SYSTEM] Total number of words:", total_words)
    
    # Ask the user if he wishes to find common words #
    answear = int(input("\nType 1 if you wish to compare the initial strings. "))
    
    if (answear == 1):
        input_words2 = str(input("\n[SYSTEM] Give your words/strings (2): "))
        common_words = find_common_words(input_words1, input_words2)
        print("\n[SYSTEM] Common words are: ", common_words)

if __name__ == "__main__":
    main()