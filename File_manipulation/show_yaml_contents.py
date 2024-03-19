import yaml

# Load the YAML file
with open('C:/Users/racha/OneDrive/Desktop/Cloud_training/info.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Print directories
print("Directories:")
for directory in data['directories']:
    print(f"- {directory}")

# Print math files
print("\nMath Files:")
for math_file in data['math']:
    print(f"- {math_file}")

# Print all files
print("\nAll Files:")
for file in data['files']:
    print(f"- {file}")
