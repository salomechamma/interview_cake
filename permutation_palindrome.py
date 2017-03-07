# function with dictionnary

def permutation_palindrome(word):
    rep = {}
    for i in range(len(word)):
        rep[word[i]] = rep.get(word[i],0) + 1
    found_odd = False
    for tot in rep.keys():
        if rep[tot] % 2 != 0:
            if not found_odd:
                found_odd = True
            else:
                return False
    return True


# function with set

def permutation_palindrome2(word):
    odd_char = set()
    for i in range(len(word)):
        if word[i] in odd_char:
            odd_char.remove(word[i])
        else:
            odd_char.add(word[i])
    return len(odd_char)==0 or len(odd_char)==1
