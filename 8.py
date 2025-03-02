from collections import deque

def word_ladder(begin_word, end_word, word_list):
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    queue = deque([(begin_word, 1)])
    while queue:
        current_word, level = queue.popleft()
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word == end_word:
                    return level + 1
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, level + 1))
    return 0

# Example usage
begin_word = "hit"
end_word = "cog"
word_list = ["hot","dot","dog","lot","log","cog"]
print("Shortest Transformation Sequence Length:", word_ladder(begin_word, end_word, word_list))