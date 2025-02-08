def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""

# Example usage
if __name__ == "__main__":
    print("Longest Word:", longest_word("Find the longest word in this sentence"))