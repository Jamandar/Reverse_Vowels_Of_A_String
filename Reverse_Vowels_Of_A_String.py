def reverse_vowels_of_a_string(astr):
    '''
    Write a function that takes a string as input and 
    reverse only the vowels of a string.
    Example 1:
    Given s = "hello", return "holle".
    Example 2:
    Given s = "leetcode", return "leotcede".
    Note:
    The vowels does not include the letter "y".
    https://leetcode.com/problems/reverse-vowels-of-a-string/description/
    Time : O(N)
    Space: O(N)
    Note :
    1. 2 indices left and right
    2. progress if index is a consonant
    3. stop and swap if both are vowels, then move both
    4. repeat till left < right
    '''
    if astr == None or len(astr.strip()) < 2:
        return astr

    left = 0
    right = len(astr) - 1
    reversed_astr = [''] * len(astr)
    vowels = 'aeiouAEIOU'

    while left < right:
        if astr[left] in vowels and astr[right] in vowels:
            reversed_astr.insert(right, astr[left])
            reversed_
