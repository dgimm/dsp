#Q6
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

#Q7
