
# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

with open('it_company.csv') as file:
   for line in file:
      if job_title in line:
         print(line)