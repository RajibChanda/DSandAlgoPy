# O(nlogn) running time
def is_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    ''' wwe have to soet the letters of the strings and then we have 
        to compare the letters with the same indexes'''
    # is has O(NlogN) running time complexity
    str1 = sorted(str1)
    str2 = sorted(str2)

    # O(n) running time
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True
        
if __name__ == '__main__':
    # s1 = ['f', 'l', 'u', 's','t', 'e', 'r']
    # s2 = ['r','e', 's', 't', 'f', 'u', 'l']

    #print(is_anagram(s1,s2))
    print(is_anagram('fluster','restful'))