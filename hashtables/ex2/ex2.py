#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # dictionary to hold tickets
    ticket_dict = {}
    # list to hold ticket order
    result = []
    # var to hold current location
    curr_loc = None
    # iterate through the tickets list
    for i in tickets:
        # set the source of a ticket as the key and the destination
        # as the value
        ticket_dict[i.source] = i.destination
    # if NONE exists as a key in the ticket dictionary...
    if 'NONE' in ticket_dict:
        # append the destination to the result list
        result.append(ticket_dict['NONE'])
        # and set the current location to the destination
        curr_loc = ticket_dict['NONE']
    # iterate through the length - 1 because we already went through
    # one ticket already
    for i in range(length - 1):
        # if the current location is in the ticket dictionary...
        if curr_loc in ticket_dict:
            # append the destination to the result list
            result.append(ticket_dict[curr_loc])
            # and set the current location to the destination
            curr_loc = ticket_dict[curr_loc]
    # return the result list
    return result
