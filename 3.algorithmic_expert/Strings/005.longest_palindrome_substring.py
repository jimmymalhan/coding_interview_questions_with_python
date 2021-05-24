string = "abaxyzzyxf"
# O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
	currentLongest = [0, 1]
	for i in range(1, len(string)): # starting from 1, as index[0] is already a palindrome
		odd = getLongestPalindromeFrom(string, i - 1, i + 1) # i-1 = leftIdx & i + 1 = rightIdx
		even = getLongestPalindromeFrom(string, i - 1, i)
		longest = max(odd, even, key=lambda x: x[1] - x[0])
		currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
	return string[currentLongest[0] : currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	return [leftIdx + 1, rightIdx]

print(longestPalindromicSubstring(string))

# ====================================================================================================

# O(n^3) time | O(n) space
def longestPalindromicSubstring(string):
    longest = ""
    for i in range(len(string)): # from index 0
        for j in range(i, len(string)): # idx[0-6], [1-6], [2-6], [3-6], [4-6], [5,6],[6]
            substring = string[i : j + 1] # string at index[0, 0-1..., 0-9, 1, 1-2 ...]
            if len(substring) > len(longest) and isPalindrome(substring): # len(substring)= 1-10, 1-9 ... > len(longest) and becomes palindrome
				longest = substring
	return longest

def isPalindrome(string):
	leftIdx = 0
	rightIdx = len(string) - 1
	while leftIdx < rightIdx:
		if string[leftIdx] != string[rightIdx]:
			return False
		leftIdx += 1
		rightIdx -= 1
	return True