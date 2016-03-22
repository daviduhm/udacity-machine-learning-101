#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of people: ", len(enron_data)
print "Number of features: ", len(enron_data[enron_data.keys()[0]])

count = 0
for key in enron_data.keys():
	if enron_data[key]["poi"] == 1:
		count = count + 1
print "Number of POI in enron_data: ", count

# for feature in enron_data["PRENTICE JAMES"]:
	# print feature
print "Total value of the stock belonging to James Prentice: ", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Number of messages from Wesley Colwell to POIs: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
