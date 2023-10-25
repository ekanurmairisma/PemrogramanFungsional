def konversi(w=0):
    def hari(d=0):
        def jam(h=0):
            def menit(m=0):
                return ((w * 7 * 24 * 60) + (d * 24 * 60) + (h * 60) + m)
            return menit
        return jam
    return hari
 
def convert_to_minutes(data):
    parts = data.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])

    total_minutes = konversi(weeks)(days)(hours)(minutes)

    return total_minutes

data = ["3 minggu 3 hari 7 jam 21 menit", 
        "5 minggu 5 hari 8 jam 11 menit", 
        "7 minggu 1 hari 5 jam 33 menit"]

output_data = [convert_to_minutes(entry) for entry in data]
print(output_data)
