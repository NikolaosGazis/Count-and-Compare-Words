# Libraries #
import re # regular expressions.

# Functions #
def count_words(words):
    count = words.count('"') 
    
    if (count % 2 == 0): # Even.
        return count // 2
    else:
        print("Number of quotes are odd, check and run again.")

def extract_words(input_words):
    # Find all words enclosed in double quotes(""), including spaces #
    words = re.findall(r'"([^"]+)"', input_words)
    return words

def find_common_words(in_words1, in_words2):
    words1 = extract_words(in_words1)
    words2 = extract_words(in_words2)
    
    # Save common words #
    common_words = set(words1) & set(words2)
    return common_words 

def main():
    input_words1 = input("\n[SYSTEM] Give your words/strings: ")
    
    # Count words #
    total_words = count_words(input_words1)
    print("\n[SYSTEM] Total number of words:", total_words)
    
    # Ask the user if he wishes to find Common words between sets #
    answear = int(input("\nType 1 if you wish to compare the initial strings.-> "))
    if (answear == 1):
        input_words2 = input("\n[SYSTEM] Give your words/strings that will be compared: ")
        common_words = find_common_words(input_words1, input_words2)
        print("\n[SYSTEM] Common words are: ", common_words)

# Execute Program #
if __name__ == "__main__":
    main()