def remove_match_char(list1, list2):
    # Loop through each character in list1
    for i in range(len(list1)):
        for j in range(len(list2)):
            # If a matching character is found in both lists
            if list1[i] == list2[j]:
                c = list1[i]
                # Remove that character from both lists
                list1.remove(c)
                list2.remove(c)
                # Combine the remaining characters with a '*' as a separator
                list3 = list1 + ['*'] + list2
                # Return the combined list and True (indicating a match was found)
                return [list3, True]

    # If no match found, return the combined list with False
    list3 = list1 + ['*'] + list2
    return [list3, False]


if __name__ == '__main__':
    # Take Player 1's name as input
    p1 = input("Player 1 Name: ")
    p1 = p1.lower()          # Convert to lowercase
    p1 = p1.replace(" ", "") # Remove spaces
    p1_list = list(p1)       # Convert name to list of characters

    # Take Player 2's name as input
    p2 = input("Player 2 Name: ")
    p2 = p2.lower()
    p2 = p2.replace(" ", "")
    p2_list = list(p2)

    proceed = True
    # Keep removing matching characters until none are left
    while proceed:
        return_list = remove_match_char(p1_list, p2_list)
        con_list = return_list[0]   # The updated list after removal
        proceed = return_list[1]    # True if a match was removed, False otherwise

        # Split back into p1_list and p2_list using '*' as a divider
        star_index = con_list.index("*")
        p1_list = con_list[:star_index]
        p2_list = con_list[star_index + 1:]

    # Count total remaining characters after removals
    count = len(p1_list) + len(p2_list)

    # Relationship categories
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    # FLAMES calculation loop
    while len(result) > 1:
        # Find the index based on count
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[:split_index]
            
            result = right + left  # Re-arrange list by removing the counted-out element
        else:
            # If split_index is -1, remove the last element
            result = result[:len(result) - 1]

    # Print final relationship status
    print('RelationShip Status:', result[0])
