def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd length
        tmp = expand_around_center(i, i)
        if len(tmp) > len(longest):
            longest = tmp
        # Even length
        tmp = expand_around_center(i, i + 1)
        if len(tmp) > len(longest):
            longest = tmp
    return longest

# Example usage
s = "babad"
print("Longest Palindromic Substring:", longest_palindromic_substring(s))