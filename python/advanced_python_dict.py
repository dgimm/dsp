#Q6
faculty_edit = faculty.copy()

faculty_edit['name'] = faculty['name'].str.split().str[-1]

faculty_dictionary = faculty_edit.set_index('name').T.to_dict('list') #I spent the last 10 hours trying to figure out a way to group the values under the same key(same last name), but my approach did not allow duplicate indexes. I struggled with Advanced Python in general and I will review key concepts and gain more understanding of Python to fully comprehend the process.  

faculty_dictionary

#Q7
faculty['firstname'] = faculty['name'].str.extract('([A-Z]\w{0,})', expand=True)

faculty['name'] = faculty['name'].str.split().str[-1]

faculty_dictionary_edit = faculty.set_index(['firstname', 'name']).T.to_dict('list')

faculty_dictionary_edit

#Q8
faculty_dictionary_edit2 = faculty.set_index(['name', 'firstname']).T.to_dict('list')

faculty_dictionary_edit2
