# Libraries #
import re # regular expressions.

# Functions #
def count_words(words):
    count = words.count('"') 
    
    if count % 2 != 0: # Even.
        raise ValueError("Number of quotes is odd, please recheck for any misplaced ones.")
    return count // 2

def extract_words(input_words):
    # Find all words enclosed in double quotes(""), including spaces #
    return re.findall(r'"([^"]+)"', input_words)

def find_common_words(in_words1, in_words2):
    words1 = extract_words(in_words1)
    words2 = extract_words(in_words2)
    return set(words1) & set(words2)

def main():
    input_words1 = input("\n[SYSTEM] Give your words/strings: ")
    
    try:
        total_words = count_words(input_words1)
        print("\n[SYSTEM] Total number of words:", total_words)
    except ValueError as e:
        print(f"[ERROR] {e}")
    
    # Ask the user if he wishes to find Common words between sets #
    choice = int(input("\nYou wish to compare the words you provided? (y/n) -> ")).strip().lower()
    if choice == 'y':
        input_words2 = input("\n[SYSTEM] Give your words/strings that will be compared: ")
        common_words = find_common_words(input_words1, input_words2)
        print("\n[SYSTEM] Common words are: ", common_words)

# Execute the Program #
if __name__ == "__main__":
    main()
    
