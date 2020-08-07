def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # list to hold all the dictionarys
    dict_list = []
    # iterate through the lists
    for i in arrays:
        # create a dict to hold all the list values
        new_dict = {}
        # iterate through the elements of a given list
        for j in i:
            # create a key based on the passed in list value
            new_dict[j] = j
        # append the dict into the dict_list list
        dict_list.append(new_dict)
    # list to hold intersections
    result = []
    # iterate through the first list to check for intersections
    for i in arrays[0]:
        # iterate through the list of dicts, excluding the first dict
        for j in dict_list[1:]:
            # if a value from the first list is in the dict keys...
            if i in j:
                # if the value from the list is not in the result list...
                if i not in result:
                    # then append that list value into the result list
                    result.append(i)
    # return the result
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
