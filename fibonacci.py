"""
Nabil Arbouz
Algorithms Spring 2020
Fibonacci Class
"""


class Fibonacci:
    def __init__(self):
        # we will seed the first two values for 0 and 1
        self.calculated_n_list = [0, 1]

    def calculate_fibonacci(self, n):
        # Check the base cases
        if n < 0:
            return "not a valid n value"
        elif n == 0:
            return self.calculated_n_list[0]
        elif n == 1:
            return self.calculated_n_list[1]
        # We know fill the list up to the point necessary
        elif n >= 2:
            # If the number is in the list, return it
            if n < len(self.calculated_n_list):
                return self.calculated_n_list[n]
            # if it is not in the list fill the list up to that point
            else:
                self.fill_fibonacci_list(n)
                return self.calculated_n_list[n]

    def fill_fibonacci_list(self, n):
        last_calculated_index = len(self.calculated_n_list) - 1

        # We continue to calculate the n's until we reach the desired value
        while last_calculated_index <= n:
            # We add the previous two numbers to each new position needed
            self.calculated_n_list.append(
                    self.calculated_n_list[last_calculated_index] +
                    self.calculated_n_list[last_calculated_index - 1])
            last_calculated_index += 1
