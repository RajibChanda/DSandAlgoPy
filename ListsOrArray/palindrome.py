
''' it has O(s) linear running time complexity as far as the number 
    of letters in the string is concerned '''
def is_palindrome(str):
    original_str = str

    reversed_str = reverse(str)

    if original_str == reversed_str:
        return True

    return False

def reverse(data):

    # convert the string to a list
    data = list(data)

    start_idx = 0
    end_idx = len(data)-1

    while end_idx > start_idx:

        
        #keep swapping the items 
        data[start_idx], data[end_idx] = data[end_idx], data[start_idx]

        start_idx = start_idx + 1
        end_idx = end_idx - 1

    # transform the list of letters into a string
    return ''.join(data)

def palindrome_python(str):
    if str == str[::-1]:
        return True
    
    return False


if __name__ == '__main__':
    print(palindrome_python('yes'))
    print(is_palindrome('ooioo'))