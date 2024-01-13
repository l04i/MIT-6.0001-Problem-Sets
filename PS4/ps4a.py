# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    final_list = []
    if len(sequence) == 1:
        return list(sequence)
    else:
         first_letter = sequence[0]
         remaining_letters_list = get_permutations(sequence[1:])   
         for letters in remaining_letters_list:
             final_list.append(first_letter + letters)
             final_list.append(letters + first_letter)
             for n in range(len(sequence)-2):  
                 final_list.append(letters[:n+1]+first_letter+letters[n+1:])
    return final_list

if __name__ == '__main__':
#    #EXAMPLE
    example_input1 = 'a'
    print('Input:', example_input1)
    print('Expected Output:', ['a'])
    print('Actual Output:', len(get_permutations(example_input1)))

    example_input2 = 'ab'
    print('Input:', example_input2)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', len(get_permutations(example_input2)))

    example_input3 = 'abc'
    print('Input:', example_input3)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', len(get_permutations(example_input3)))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)



