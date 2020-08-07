def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # dictionary to hold list values
    dict_list = {}
    # iterate through passed in list
    for i in a:
        # put list inside dictionary
        dict_list[i] = i
    # list to hold positive numbers that have
    # corresponding negative numbers
    result = []
    # iterate through list
    for i in a:
        # if an element in the list is greater than 0...
        if i > 0:
            # and if the negative value of the element of the list
            # is a key in the dictionary...
            if -i in dict_list:
                # append the list eleemnt to the result list
                result.append(i)
    # return the result list
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
