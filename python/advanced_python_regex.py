#Q1
import pandas as pd

faculty = pd.read_csv('Desktop/metis/prework/dsp/python/faculty.csv')

faculty = faculty.rename(columns=lambda x: x.strip())

faculty['degree'] = faculty['degree'].str.replace('.', '')
faculty['degree'] = faculty['degree'].str.replace('.', '')
faculty['degree'] = faculty['degree'].str.strip()

faculty_degree = faculty['degree']
faculty_degree = faculty_degree.str.split(' ').apply(pd.Series)     
faculty_degree = faculty_degree.stack()

faculty_degree.value_counts()

#Q2
faculty['title'] = faculty['title'].replace('is', 'of', regex=True)
faculty['title'] = faculty['title'].replace('Assoftant', 'Assistant', regex=True)

faculty['title'].value_counts()

#Q3
faculty_email_list = list(faculty['email'])

print(faculty_email_list)

#4
faculty_email = faculty['email'].str.extract('(@.+)')

faculty_email.value_counts()
