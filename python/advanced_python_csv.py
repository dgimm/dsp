import csv

with open('emails.csv', "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    for val in faculty_email_list:
        writer.writerow([val])
