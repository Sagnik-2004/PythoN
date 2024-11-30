# Step 1: Create the dictionary
places = {
    1: "Howrah",
    3: "Dumdum",
    2: "Bally",
    4: "Jadavpur"
}

# Step 2: Modify the value of key '3'
places[3] = "Dakshineswar"

# Step 3: Sort the dictionary by keys
sorted_places = dict(sorted(places.items()))  # This creates a new sorted dictionary

# Step 4: Display all the values in sorted form
sorted_values = sorted(sorted_places.values())  # Extract values and sort them

# Display the results
print("Modified Dictionary:", places)
print("Dictionary Sorted by Keys:", sorted_places)
print("Values in Sorted Form:", sorted_values)
