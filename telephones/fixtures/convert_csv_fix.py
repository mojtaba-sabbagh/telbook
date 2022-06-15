import csv
import json

csv_file_path = 'csv/fani.csv'
json_file_path = 'fani.json'
MODEL_NAME = 'telephones.Profile'
#create a dictionary
rows = []
with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
    #convert each row into a dictionary
    #and add the converted data to the data_variable
    csv_reader = csv.DictReader(csv_file_handler)
    i = 0
    for row in csv_reader:
        i += 1
        #assuming a column named 'No'
        #to be the primary key
        data_dict = {"model":MODEL_NAME, "pk":0, "fields":{}}
        data_dict['pk'] = i
        data_dict["fields"]['first_name'] = row['first_name'].strip()
        data_dict["fields"]['last_name'] = row['\ufefflast_name'].strip()
        data_dict["fields"]['gender'] = row['gender'].strip()
        rows.append(data_dict)

    with open(json_file_path, 'w', encoding='utf-8') as json_file_handler:
        #Step 4
        json_file_handler.write(json.dumps(rows, indent = 2))
 