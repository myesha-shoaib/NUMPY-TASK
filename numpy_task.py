import numpy as np
# 1. IMPORT NUMPY

print("\n1. IMPORT NUMPY")
print("NumPy Version:", np.__version__)

# 2. PYTHON LIST VS NUMPY ARRAY
print("\n2. PYTHON LIST VS NUMPY ARRAY")

python_list = [10, 20, 30, 40]
numpy_array = np.array([10, 20, 30, 40])

print("Python List:", python_list)
print("NumPy Array:", numpy_array)

# 3. CREATING NUMPY ARRAYS

print("\n3. CREATING NUMPY ARRAYS")

# One-Dimensional Array
arr1 = np.array([10, 20, 30, 40, 50])
print("One-Dimensional Array:")
print(arr1)

# Two-Dimensional Array
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Two-Dimensional Array:")
print(arr2)

# 4. IMPORTANT ARRAY PROPERTIES

print("\n4. IMPORTANT ARRAY PROPERTIES")

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("ndim:", arr.ndim)
print("shape:", arr.shape)
print("size:", arr.size)
print("dtype:", arr.dtype)

# 5. INDEXING
print("\n5. INDEXING")

arr = np.array([10, 20, 30, 40, 50])

print("First Element:", arr[0])
print("Second Element:", arr[1])
print("Last Element:", arr[-1])

# 6. INDEXING IN A 2D ARRAY

print("\n6. INDEXING IN A 2D ARRAY")

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("First Row, First Column:", arr[0, 0])
print("First Row, Second Column:", arr[0, 1])
print("Second Row, Third Column:", arr[1, 2])

# 7. SLICING

print("\n7. SLICING")

arr = np.array([10, 20, 30, 40, 50, 60])

print("First Three Elements:", arr[:3])
print("Elements from Index 2:", arr[2:])
print("Elements from Index 1 to 4:", arr[1:4])

# 8. VECTORIZED OPERATIONS


print("\n8. VECTORIZED OPERATIONS")

arr = np.array([10, 20, 30])

print("Original Array:", arr)

print("Addition (+ 5):", arr + 5)
print("Subtraction (- 5):", arr - 5)
print("Multiplication (* 2):", arr * 2)
print("Division (/ 2):", arr / 2)


# 9. OPERATIONS BETWEEN TWO ARRAYS


print("\n9. OPERATIONS BETWEEN TWO ARRAYS")

arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

# Addition
print("Addition:")

result = arr1 + arr2

for a, b, c in zip(arr1, arr2, result):
    print(f"{a} + {b} = {c}")

# Subtraction
print("Subtraction:", arr1 - arr2)

# Multiplication
print("Multiplication:")

result = arr1 * arr2

for a, b, c in zip(arr1, arr2, result):
    print(f"{a} * {b} = {c}")

# Division
print("Division:", arr1 / arr2)


# 10. MATHEMATICAL FUNCTIONS

print("\n10. MATHEMATICAL FUNCTIONS")

arr = np.array([4, 9, 16, 25])

# Square Root
print("Square Root:", np.sqrt(arr))

# Power
print("Power 2:", np.power(arr, 2))

# Absolute Value
arr2 = np.array([-10, -20, 30, -40])
print("Absolute Value:", np.abs(arr2))

# Round
arr3 = np.array([2.456, 3.678, 4.234])
print("Rounded Values:", np.round(arr3, 2))

# 11. AGGREGATION FUNCTIONS

print("\n11. AGGREGATION FUNCTIONS")

arr = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))
print("Maximum Value:", np.max(arr))
print("Minimum Value:", np.min(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

# 12. CONDITIONS IN NUMPY
print("\n12. CONDITIONS IN NUMPY")

arr = np.array([10, 25, 30, 45, 50])

print("Original Array:", arr)

print("Greater than 30:", arr > 30)
print("Less than 30:", arr < 30)
print("Equal to 30:", arr == 30)

# 13. FILTERING DATA

print("\n13. FILTERING DATA")

arr = np.array([10, 25, 30, 45, 50, 60])

# Select values greater than 30
filtered_data = arr[arr > 30]

print("Original Array:", arr)
print("Values Greater than 30:", filtered_data)

# Select even numbers
even_numbers = arr[arr % 2 == 0]

print("Even Numbers:", even_numbers)

# 14. RESHAPE

print("\n14. RESHAPE")

arr = np.array([1, 2, 3, 4, 5, 6])

reshaped_array = arr.reshape(2, 3)

print("Original Array:")
print(arr)

print("Reshaped Array:")
print(reshaped_array)

# 15. FLATTEN
print("\n15. FLATTEN")

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flattened_array = arr.flatten()

print("Original 2D Array:")
print(arr)

print("Flattened 1D Array:")
print(flattened_array)

# 16. USEFUL NUMPY FUNCTIONS

print("\n16. USEFUL NUMPY FUNCTIONS")

# zeros()
zero_array = np.zeros(5)

print("Zeros Array:")
print(zero_array)

# arange()
range_array = np.arange(1, 11)

print("Array using arange():")
print(range_array)

# 17. RANDOM NUMBERS

print("\n17. RANDOM NUMBERS")

# Generate 5 random decimal numbers
random_array = np.random.rand(5)

print("Random Decimal Numbers:")
print(random_array)

# Generate 5 random integers between 1 and 100
random_integers = np.random.randint(1, 101, size=5)

print("Random Integers:")
print(random_integers)

# Generate a 2D random array
random_2d = np.random.randint(1, 51, size=(2, 3))

print("Random 2D Array:")
print(random_2d)

print("\nALL NUMPY TASKS COMPLETED!")