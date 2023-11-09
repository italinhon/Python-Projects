countries = []
years = []
life_expeactancies = []

with open("life-expectancy.csv") as file_info:
    for index, line in enumerate(file_info): # enumerate it's like a buffer
        if index == 0:
            continue # It will jump the first line from the document

        info = str(line).split(",")
        countries.append(info[0]) # .append adds something new inside the array
        years.append(int(info[2])) # .append here is for add the string info on the array number 2
        life_expeactancies.append(float(info[3]))

# Do the analysis
user_year_input = input("Enter the year of interest: ")

# Search how to find the maximum number
overall_max_life_idx = 0
overall_max_life = 0
max_year = 0
max_country = ""

overall_min_life_idx = 999999999
overall_min_life = 999999999
min_year = 999999999
min_country = ""

total_life_expectancy = 0
count = 0 # It will count the averege

for index, year in enumerate(years):
    if year == int(user_year_input):
        total_life_expectancy += life_expeactancies[index]
        count += 1

    if life_expeactancies[index] > overall_max_life:
        overall_max_life = life_expeactancies[index]
        overall_max_life_idx = index
        max_year = years[index]
        max_country = countries[index]

    if life_expeactancies[index] < overall_min_life:
        overall_min_life = life_expeactancies[index]
        overall_min_life_idx = index
        min_year = years[index]
        min_country = countries[index]

if count > 0:
    avarege_life_expectancy = total_life_expectancy / count
else:
    avarege_life_expectancy = 0

print(f"The overall max life expectancy is: {overall_max_life} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {overall_min_life} from {min_country} in {min_year}")
print()
print(f"For the year {user_year_input}")
print(f"The average life expectancy across all countries was {avarege_life_expectancy:.2f}")
print(f"The max life expectancy was in {max_country} with {overall_max_life_idx}")
print(f"The max life expectancy was in {min_country} with {overall_min_life_idx}")