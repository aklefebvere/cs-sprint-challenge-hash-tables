# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # dictionary to hold all query elements from list
    query_dict = {}
    # iterate through the queries list
    for i in queries:
        # insert values from list into dictionary
        query_dict[i] = i
    # list to hold the results
    result = []
    # iterate through paths list
    for i in files:
        # split the str on "/" and grab the last element
        check = i.split("/")[-1]
        # if that last elemement is a key in the dict...
        if check in query_dict:
            # append the path to the result list
            result.append(i)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
