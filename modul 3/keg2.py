data = ["3 minggu 3 hari 7 jam 21 menit", 
        "5 minggu 5 hari 8 jam 11 menit", 
        "7 minggu 1 hari 5 jam 33 menit"]

def extract_values(entry):
    parts = entry.split()
    integers = [part for part in parts if part.isdigit()]
    return integers

# list comprehension untuk menghasilkan daftar nilai integer
result = [extract_values(entry) for entry in data]

for item in result:
    print(item)
