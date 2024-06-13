import re
from collections import Counter

def analyze_text(text):
    # Accented characters
    accented_chars = 'âîû'
    
    # Regex expression for all characters
    all_chars_regex = re.compile(r'\w')
    
    # Regex expression for accented characters
    accented_chars_regex = re.compile(r'[âîû]')
    
    # Split text into words
    words = text.split()
    
    # Total number of characters
    total_chars = len(re.findall(all_chars_regex, text))
    
    # Number of accented characters
    accented_char_count = len(re.findall(accented_chars_regex, text))
    
    # Number of accented characters in each word
    accented_char_in_words = [len(re.findall(accented_chars_regex, word)) for word in words]
    
    # Average number of accented characters per word
    average_accented_per_word = sum(accented_char_in_words) / len(words) if words else 0
    
    # Ratio of accented characters to total characters
    ratio_accented_to_total = accented_char_count / total_chars if total_chars else 0
    
    # Frequency of accented characters
    frequency_accented_chars = dict(Counter(re.findall(accented_chars_regex, text)))
    
    # Print results
    print(f"Average number of accented characters per word: {average_accented_per_word}")
    print(f"Ratio of accented characters to total characters: {ratio_accented_to_total}")
    print(f"Frequency of accented characters: {frequency_accented_chars}")
    
    return average_accented_per_word, ratio_accented_to_total, total_chars, accented_char_count

def rewrite_hatten(text, average_accented_per_word, ratio_accented_to_total, total_chars, accented_char_count):
    # Accented characters and their unaccented counterparts
    replace_map = {'a': 'â', 'i': 'î', 'u': 'û'}
    
    # Regex expression for all characters
    all_chars_regex = re.compile(r'\w')
    
    # Regex expression for accented characters
    accented_chars_regex = re.compile(r'[âîû]')
    
    words = text.split()
    new_text = []
    
    # Increase the count of accented characters in words
    new_accented_char_count = accented_char_count
    new_total_chars = total_chars
    
    for word in words:
        new_word = word  # Start with the original word to create the new word
        if new_accented_char_count / new_total_chars < ratio_accented_to_total:
            for char in word:
                if char in replace_map:
                    new_word = new_word.replace(char, replace_map[char], 1)
                    new_accented_char_count += 1
                    if new_accented_char_count / new_total_chars >= ratio_accented_to_total:
                        break
        new_text.append(new_word)
        new_total_chars += len(new_word)
    
    # Write the new text to a file
    with open('new-cool-hat.txt', 'w', encoding='utf-8') as file:
        file.write(" ".join(new_text))
    
    return " ".join(new_text)

def main():
    combined_text = ""
    
    # Read and combine text files from 1 to 16
    for i in range(1, 17):
        file_path = f'metin-{i}.txt'
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                combined_text += file.read() + " "  # Add a space when combining files
        except FileNotFoundError:
            print(f"{file_path} not found.")
    
    # Analyze the combined text
    average_accented_per_word, ratio_accented_to_total, total_chars, accented_char_count = analyze_text(combined_text)
    
    # Read new text file from user input
    try:
        new_text_file = input("\nPlease enter the name of the new text file: ")
        with open(new_text_file, 'r', encoding='utf-8') as file:
            user_input_text = file.read()
    except FileNotFoundError:
        print(f"{new_text_file} not found.")
        return
    
    # Rewrite and save text while maintaining accented character ratios
    new_text = rewrite_hatten(user_input_text, average_accented_per_word, ratio_accented_to_total, total_chars, accented_char_count)
    
    # Analyze and print results of the new text
    print("\nAnalysis results of the new text:")
    analyze_text(new_text)
    print("\nNew text:")
    print(new_text)

# Example usage
main()
