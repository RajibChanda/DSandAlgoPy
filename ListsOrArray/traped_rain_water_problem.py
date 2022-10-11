def trapping_water_problem(heights):
    '''
    Returns an integer indicating amount of trapped rain water according to the Trapping Rain Water
    Problem.
    Args:
        heights : a list of integers depicting heights(number of blocks in each index position)
    '''

    if len(heights) <3:
        return 0

    left_max = [0 for _ in range(len(heights))]
    right_max = [0 for _ in range(len(heights))]

    ########### Dynamic programming approach to save left max and right max values for 
    # each index of array height ##############

    # dealing with the left max values
    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i-1], heights[i - 1])

    # dealing with the right max values
    for i in range(len(heights) - 2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i + 1])

    ############ Dynamic Programming approach ends #############

    # consider all the items in O(N) and sum up the trapped rain water units
    trapped = 0

    for i in range(1, len(heights)-1):
        if min(left_max[i], right_max[i]) > heights[i]:
            trapped += min(left_max[i], right_max[i]) - heights[i]


    return trapped

if __name__ == '__main__':
    print(f'Amount of Trapped water is: {trapping_water_problem([3,2,1,7,5,7])}')