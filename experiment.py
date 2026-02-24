import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating sample data
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": [75, 88, 92, 60, 85]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display Data
print("Student Data:")
print(df)

# Plot using matplotlib
plt.figure()
plt.plot(df["Student"], df["Marks"])
plt.title("Student Marks Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
