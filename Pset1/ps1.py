###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time
import operator

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    sortedCows = [k for v,k in sorted([(v,k) for k,v in cows.items()], reverse = True)]
    
    # Initialize variable which will store the list of trips
    result = []
    
    # Initialize variable to keep track of cows left and cows used
    cowsLeft = len(sortedCows)
    cowsUsed = []
    
    # Keep going until all cows used
    while cowsLeft > 0:
        # Initialize variable to store each trip
        trip = []
        # Initialize variable to store weight on current trip
        weight = 0
        # Iterate through each cow in the sorted list
        for item in sortedCows:
            # Check if cow has been used yet
            if item not in cowsUsed:
                # Check if there is still room on this trip
                if weight + cows[item] <= limit:
                    # Add cow to this trip
                    trip.append(item)
                    # Mark cow as having been used
                    cowsUsed.append(item)
                    cowsLeft -= 1
                    # Add cow to the weight of this trip
                    weight += cows[item]
        result.append(trip)
    
    # Return best result
    return result


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_filtered = {k:v for k,v in cows.items() if v <= limit}

    transports = []
    for partition in get_partitions(cows_filtered):
        flag = True  
        for transport in partition:
            if sum(map(cows_filtered.get, transport)) > limit:
                flag = False
                break
        if flag:
            if len(partition) < len(transports) or len(transports) == 0:
                transports = partition
    return transports

        
# Problem 3
def compare_cow_transport_algorithms(cows, limit):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start_greedy = time.time()
	## code to be timed
    greedy = greedy_cow_transport(cows, limit)
    end_greedy = time.time()
    print("Greedy algorithm take: {:.4f} ms".format((end_greedy - start_greedy)*1000))
	
	
    start_brute_force = time.time()
	## code to be timed
    brute_force = brute_force_cow_transport(cows, limit)
    end_brute_force = time.time()
    print("Brute force algorithm take: {:.4f} ms".format((end_brute_force - start_brute_force)*1000))
	
	


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
#limit=100
limit = 10 
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms(cows, limit)
