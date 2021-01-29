#This algorithm will find the maximum x-coordinate and y-coordinate in a convex polygon
def max_x(x_list, low, high):
    n_value = len(x_list)
    while low <= high:
        mid = low + (high - low) // 2

        if x_list[low] > x_list[(low + 1) % n_value] and \
                x_list[low] > x_list[(low - 1) % n_value]:
            return x_list[low]
        else:
            if x_list[mid] > x_list[mid + 1] and \
                    x_list[mid] > x_list[mid - 1]:
                return x_list[mid]
            elif x_list[mid + 1] < x_list[mid] < x_list[mid - 1]:
                high = mid - 1
                low = low + 1
            else:
                low = mid + 1


def max_y(y_list, low, high):
    n_value = len(y_list)
    while low <= high:
        mid = low + (high - low) // 2
        if y_list[low] > y_list[(low + 1) % n_value] \
                and y_list[low] > y_list[(low - 1) % n_value]:
            return y_list[low]
        else:
            if y_list[mid] > y_list[mid + 1] and \
                    y_list[mid] > y_list[mid - 1]:
                return y_list[mid]
            elif y_list[mid + 1] < y_list[mid] < y_list[mid - 1]:
                high = mid - 1
                low = low + 1
            else:
                low = mid + 1


def main():
    input_x_list = [0.9, 1.9, 4.2, 5.71, 4.62, 2.43]

    input_y_list = [3.4, 1.83, 1.4, 2.65, 4.18, 4.54]

    print("largest x value: " + str(max_x(input_x_list, 0, len(input_x_list) - 1)))
    print("largest y value: " + str(max_y(input_y_list, 0, len(input_y_list) - 1)))


main()
