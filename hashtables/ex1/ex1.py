def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # if there is no two values to add...
    if len(weights) == 1:
        return None
    # if there is only two values...
    elif len(weights) == 2:
        # return the index of the list
        return (1,0)
    # if there is more than two elements in the list...
    else:
        # create a dict to cache the weights with its indicies
        weight_dict = {}
        # list to hold the indicies
        ans_lst = []
        # iterate through weights and its index
        for i, v in enumerate(weights):
            # create a key off the weight and set the value to its index
            weight_dict[v] = i
        # iterate through weights
        for i in weights:
            # if limit - i is in the weights dictionary...
            if limit - i in weight_dict:
                # then append it to the ans_lst list
                ans_lst.append(weight_dict[i])

        # if index 1's value is greater than index 0's...
        if ans_lst[1] > ans_lst[0]:
            # flip the values
            ans_lst[0], ans_lst[1] = ans_lst[1], ans_lst[0]
        # convert the list into a tuple
        ans_tup = tuple(ans_lst)
        # return the tuple
        return ans_tup


    return None
