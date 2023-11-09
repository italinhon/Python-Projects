with open("hr_system.txt") as hr_system:
    for line in hr_system:
        rem_blank_spc = line.strip()
        parts = rem_blank_spc.split(" ")
        name = parts[0]
        id_num = int(parts[1])
        job_tittle = parts[2]
        salary = float(parts[3])
        salary /= 24

        if job_tittle.lower() == "engineer":
            salary += 1000
        print(f"{name} (ID: {id_num}), {job_tittle} - ${salary:.2f}")