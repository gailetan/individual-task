'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    #find subject matter muna #set #use in
    #if follows
    if from_member in social_graph:
        subj_fols = social_graph[from_member]['following']
    #if doesn't
    else:
        subj_fols = [ ]
    #object matter following
    #if follows
    if to_member in social_graph:
        obj_fols = social_graph[to_member]['following']
    #if doesn't
    else:
        obj_fols = [ ]
    #relationships
    #friends first bc will use and
    #subj in obf's ff and obj in subj's ff = "friends"
    if (from_member in obj_fols) and (to_member in subj_fols):
        status = "friends"
    #subject follows object = obj in subj's ff = "follower"
    elif to_member in subj_fols:
        status = "follower"
    #object follows subject = subj in obj's ff = "followed by"
    elif from_member in obj_fols:
        status = "followed by"
    #don't follow each other = "no relationship"
    else:
        status = "no relationship"
    return status


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    #horizontal
    horizontal = [b for b in board]
    #vertical #use *
    vertical = [b for b in zip(*board)]
    #diagonal up-down
    up_down = [board[i][i] for i, v in enumerate(board)]
    #diagonal down-up
    #can't use board[2-i][i] bc board isn't always 3x3
    #get length of board then replace it sa 2
    down_up = [board[(len(board)-1)-i][i] for i, v in enumerate(board)]
    #if X is winner then X
    #if horizontal (any) or vertical (any) or diagonal up down (all) or diagonal down up (all)
    if any(a == ["X"]*len(board) for a in horizontal) or any(a == tuple(["X"]*len(board)) for a in vertical) or all(a == ["X"] for a in up_down) or all(a == ["X"] for a in down_up):
        result = "X"
    #if O is winner then O
    #if horizontal (any) or vertical (any) or diagonal up down (all) or diagonal down up (all)
    elif any(a == ["O"]*len(board) for a in horizontal) or any(a == tuple(["O"]*len(board)) for a in vertical) or all(a == ["O"] for a in up_down) or all(a == ["O"] for a in down_up):
        result = "O"
    #else no winner
    else:
        result = "NO WINNER"
    return result

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    #if within
    if (first_stop, second_stop) in route_map:
        return route_map[first_stop, second_stop]["travel_time_mins"]
    #overlap
    time = 0
    first = [stop[0] for stop in route_map]
    second = [stop[1] for stop in route_map]
    i = first.index(first_stop)

    while True:
        while i >= len(route_map):
            i -= len(route_map)
        time += route_map[first[i], second[i]]["travel_time_mins"]
        if second[i] == second_stop:
            return time
        i += 1