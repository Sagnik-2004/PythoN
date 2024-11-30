# Original list
data = [17, 49, 8, 67, 15, 91, 88, 55, 84]
print("Original List:", data)

# Calculate the size of each chunk
chunk_size = len(data) // 3  

# Initialize the chunks
chunk1, chunk2, chunk3 = [], [], []

# Loop to divide the list into chunks
for i in range(len(data)):
    if i < chunk_size:
        chunk1.append(data[i])  # First chunk
    elif i < 2 * chunk_size:
        chunk2.append(data[i])  # Second chunk
    else:
        chunk3.append(data[i])  # Third chunk

print("Chunk 1 :", chunk1)
print("Chunk 2 :", chunk2)
print("Chunk 3 :", chunk3)

# Function to reverse a list using a loop
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# Reverse each chunk
chunk1 = reverse_list(chunk1)
chunk2 = reverse_list(chunk2)
chunk3 = reverse_list(chunk3)

# Display results
print("Chunk 1 (Reversed):", chunk1)
print("Chunk 2 (Reversed):", chunk2)
print("Chunk 3 (Reversed):", chunk3)