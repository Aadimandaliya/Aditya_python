# Write a Python func�on that checks whether a passed string is palindrome or not

def isPalindrome(str):
	l = 0
	r = len(str) - 1
	
	while r >= l:
		if not str[l] == str[r]:
			return False
		l += 1
		r -= 1
	return True

print(isPalindrome('level')) 
print(isPalindrome('radar')) 
print(isPalindrome('12321')) 
print(isPalindrome('oops!!')) 



