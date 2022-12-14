import csv
import requests

# Open the CSV file containing the dataset
with open('dataset.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    # Iterate over the rows in the CSV file
    for row in reader:
        # Get the data from the row
        data = {
            'field1': row[0],
            'field2': row[1],
            'field3': row[2],
        }
        
        # Submit the data to the form using a POST request
        response = requests.post('http://form.url', data=data)
        
        # Check the response status to see if the form was submitted successfully
        if response.status_code == 200:
            print('Form was submitted successfully')
        else:
            print('Failed to submit form')