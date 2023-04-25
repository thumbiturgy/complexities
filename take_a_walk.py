# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

# Time Complexity is O(1). We iterate through a set of at most 4 values and count exactly 10 values.

# Space Complexity is O(N) since the Auxilary Space of the passed list object is not known

def is_valid_walk(walk): # O(N) Aux Space
    #determine if walk is valid
    if len(walk) != 10: #O(1) Time and Space
        return False
    movements = {'n': 0, 's': 0, 'e': 0, 'w': 0} #O(N) Space
    for direction in set(walk): #O(1) Time
        movements[direction] = walk.count(direction) # O(1) Time 
    if movements['n'] - movements['s'] != 0:
        return False
    if movements['e'] - movements['w'] != 0:
        return False
    return True