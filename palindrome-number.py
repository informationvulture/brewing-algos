"""
Takes a number (int) and returns whether or not it's a palindrome.
No conversion to a string is done.
"""

def isPalindrome(placer):
    # If the number meets these conditions we disregard:
    #   - Less than 0
    #   - Number has 0 at the end of it but doesn't have it at the start
    if (placer < 0 or (placer % 10 == 0 and placer != 0)):
        return False
    revertedNumber = 0
    while placer > revertedNumber:
        revertedNumber = revertedNumber * 10 + placer % 10
        placer //= 10

    return placer == revertedNumber or placer == revertedNumber//10

