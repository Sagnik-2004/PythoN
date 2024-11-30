import matplotlib.pyplot as plt

# Data for the pie chart
machines = ["Machine A", "Machine B", "Machine C", "Machine D"]
productions = [35, 25, 15, 25]

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(
    productions, 
    labels=machines, 
    autopct="%1.1f%%",  # Display percentage with one decimal place
    startangle=90,      # Start from 90 degrees
    colors=["skyblue", "orange", "lightgreen", "pink"],  # Custom colors
)

# Adding a title
plt.title("Production Percentage by Machines", fontsize=16)

# Display the chart
plt.show()
