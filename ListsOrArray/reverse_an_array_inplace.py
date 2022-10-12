def reverse(data):
# linear runnig time O(n)

    start_idx = 0
    end_idx = len(data)-1

    while end_idx > start_idx:
        #keep swapping the items 
        data[start_idx], data[end_idx] = data[end_idx], data[start_idx]

        start_idx = start_idx + 1
        end_idx = end_idx - 1

    return data


if __name__ == '__main__':

    nums = [5,2,10,-2,15,12]

    new_nums =  reverse(nums)
    print(new_nums)