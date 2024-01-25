def insertion_sort(arr):
    n = len(arr)  
      
    if n <= 1:
        return  
 
    for i in range(1, n): 
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
  

if __name__ == "__main__":
    arr = [12, 11, 1000, 13, 5, 6,  -1]
    insertion_sort(arr)
    print(arr)