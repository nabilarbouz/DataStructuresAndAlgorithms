
def color_sort(user_list, size_of_list):
    red_marker = 0
    green_marker = 0
    blue_marker = size_of_list

    while green_marker < blue_marker:
        if user_list[green_marker] == "Red":
            # swap the Red item to the Red zone by swapping it with the
            # current red zone marker
            # and push both green and red flags forward by 1 index to adjust
            # the green and red zones
            temp = user_list[red_marker]
            user_list[red_marker] = user_list[green_marker]
            user_list[green_marker] = temp
            red_marker += 1
            green_marker += 1
        elif user_list[green_marker] == "Blue":
            # swap the blue item with current blue zone marker and decrement
            # the blue flag by 1 to adjust the blue zone
            blue_marker -= 1
            temp = user_list[blue_marker]
            user_list[blue_marker] = user_list[green_marker]
            user_list[green_marker] = temp
        else:
            # if this green item is already in the green zone, we just
            # increment the green marker index by 1 so that it converges
            # with the blue marker
            green_marker += 1

    print(user_list)


def main():
    a = ["Green", "Blue", "Blue", "Red", "Green"]
    size_of_a = len(a)
    color_sort(a, size_of_a)


main()
