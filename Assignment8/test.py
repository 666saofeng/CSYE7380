import Assignment8.views.views
from django.test import TestCase


# excel_data = pd.read_excel('/Users/shelton/Documents/my-class/CSYE7380/CSYE7380/Assignment8/Categories.xlsx')
# engine = sa.create_engine('mysql+mysqlconnector://root:12345678@localhost:3306/travel_agent')

# excel_data.to_sql(name='travel_agent', con=engine, if_exists='append', index=False)
#preprocess of the dataset
# open the file in read mode

# datasets = pd.read_csv('/Users/shelton/Documents/my-class/CSYE7380/CSYE7380/Assignment8/Travel_details_dataset.csv')
# datasets['Accommodation cost'] = pd.to_numeric(datasets['Accommodation cost'], errors='coerce')
# datasets['Transportation cost'] = pd.to_numeric(datasets['Transportation cost'], errors='coerce')
# datasets['Total cost'] = datasets['Accommodation cost']+datasets['Transportation cost']
# datasets.to_csv('/Users/shelton/Documents/my-class/CSYE7380/CSYE7380/Assignment8/Travel_details_dataset.csv', index=False)
# datasets = pd.read_csv('/Users/shelton/Documents/my-class/CSYE7380/CSYE7380/Assignment8/Travel_details_dataset.csv')
# print(datasets.head())

schema = Assignment8.views.views.test_command()
print(schema)