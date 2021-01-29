"""
Nabil Arbouz and Anna Daccache
HW 1
String Matching Exercise
Algorithms Spring 2020
"""


def string_matcher(corpus_array, candidate_array):
    """
    This is a string matching function that loops through the corpus array until
    it finds a character that matches the first character of the candidate
    array. Once it matches the first character of the candidate array, the
    algorithm will check to see if the rest of the candidate array matches the
    sequence in the corpus array. If there is a match, it will return True;
    otherwise, the algorithm will skip the past the incorrect sequence in the
    corpus array and begin another search. If no match is found, the function
    will return a False boolean.
    @params corpus_array: array of characters that may contain the pattern
        found in candidate array
    @params candidate_array: an array of characters that may appear in the
        corpus_array
    """
    loop_counter = 0
    candidate_found = False
    corpus_index = 0
    # The maximum amount of checks needed is the length of the corpus array
    # minus the length of the candidate array + 1
    max_checks = (len(corpus_array) - len(candidate_array) + 1)
    while corpus_index < max_checks:
        # We use the previous candidate index as a check to see if we need to
        # increment the candidate index by 1 if it did not trigger a candidate
        # match
        previous_can_index = corpus_index
        # We use a loop counter to track the efficiency of the algorithm
        loop_counter += 1
        # We do not activate the loop that scans the candidate array unless
        # we have a match on the with the current corpus character and
        # the first candidate array character
        if corpus_array[corpus_index] == candidate_array[0]:
            for j in range(1, len(candidate_array)):
                loop_counter += 1
                # We add j to the candidate index to check the correct index
                if corpus_array[corpus_index + j] == candidate_array[j]:
                    candidate_found = True
                # We check to see if the incorrect character in the sequence
                # is the same as the first character in the candidate array
                # so we do not skip over it when we exit the loop
                elif corpus_array[corpus_index + j] == candidate_array[0]:
                    candidate_found = False
                    break
                # If the incorrect character is not the first character in the
                # candidate array, we can skip over it after we exit the
                # candidate checker loop by adding (j + 1) to the corpus index.
                else:
                    corpus_index += j + 1
                    candidate_found = False
                    break
            # We check to see if the candidate characters were found in the
            # corpus array and return True if they were found.
            if candidate_found:
                print("The total number of loops is:", loop_counter)
                return True, corpus_index
        # If we did not increment the corpus index through the candidate
        # checking loop, we increment the corpus index here
        if previous_can_index == corpus_index:
            corpus_index += 1
    print("The total number of loops is:", loop_counter)
    # If we have iterated through the entire corpus array without finding a
    # match we will return 0
    return False, "not available"


def main():
    test_corpus = list("MKkvlhTmtBuitpcYPPpLuOZgpQdpQU")
    print("The length of the corpus is: ", len(test_corpus))
    test_candidate = list("uit")

    result, location = string_matcher(test_corpus, test_candidate)
    print(result, "and found at index:", location)


main()


"""
Written Response:
1. What might break a string matching function?
    a. A data type other than an array of strings is used as input for the 
        function.
    b. A corpus array that is smaller than the candidate array
2. What is the big O time complexity of your string match?
    It is O(n * m)
3. Your boss wants a more powerful string matcher –
    what 3 things might they ask for and how would you handle the requests?
    a. Check for bad input. We would use  a try-except statement to make sure 
        the input type is  correct.
    b. Return the indexes of where the matching pattern was found. To do this,
        we would need to return the boolean and the locations in a tuple. To get
        all of the indexes, we would not exit out of the function at the first
        successful find and continue through the rest of the corpus array to 
        search for any additional matches.
        (Partially-Implemented)
    c. Make the algorithm more efficient by skipping over the characters in the 
        corpus array that we know are incorrect. You could do this by adding the 
        candidate index to the corpus array index when you continue a search.
        (Implemented)
"""
