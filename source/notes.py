

def bubble_sorted(array):
    for i in range(len(array) - 1):
        # Check if it is out of order
        if array[i] > array[i + 1]:
            # Swap
            array[i], array[i + 1] = array[i + 1], array[i]
