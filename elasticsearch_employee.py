import pandas as pd

# Load the dataset into a DataFrame
#df = pd.read_csv(r'C:\Hash Agile\Employee Sample Data.csv')  
df = pd.read_csv(r'C:\Hash Agile\Employee Sample Data.csv', encoding='ISO-8859-1')
 # Update with your CSV file path

# Initialize in-memory collections
collections = {}

# Function to create a collection
def createCollection(p_collection_name):
    collections[p_collection_name] = []

# Function to index data into the specified collection
def indexData(p_collection_name, p_exclude_column):
    if p_collection_name in collections:
        # Exclude the specified column and convert to list of dicts
        data_to_index = df.drop(columns=[p_exclude_column]).to_dict(orient='records')
        collections[p_collection_name].extend(data_to_index)

# Function to search by column
def searchByColumn(p_collection_name, p_column_name, p_column_value):
    if p_collection_name in collections:
        return [record for record in collections[p_collection_name] if record.get(p_column_name) == p_column_value]
    return []


def getEmpCount(p_collection_name):
    return len(collections[p_collection_name]) if p_collection_name in collections else 0


def delEmpById(p_collection_name, p_employee_id):
    if p_collection_name in collections:
        collections[p_collection_name] = [record for record in collections[p_collection_name] if record.get('EmployeeID') != p_employee_id]


def getDepFacet(p_collection_name):
    if p_collection_name in collections:
        department_count = {}
        for record in collections[p_collection_name]:
            department = record.get('Department')
            if department:
                if department not in department_count:
                    department_count[department] = 0
                department_count[department] += 1
        return department_count
    return {}

# Define collections
v_nameCollection = 'Hash_Robert Patel'  # Replace with your name
v_phoneCollection = 'Hash_1234'  # Replace with your phone last four digits

# Create collections
createCollection(v_nameCollection)
createCollection(v_phoneCollection)

# Function executions
print("Initial employee count in v_nameCollection:", getEmpCount(v_nameCollection))  # Output: 0

# Index data into collections
indexData(v_nameCollection, 'Department')  # Index data excluding the 'Department' column
indexData(v_phoneCollection, 'Gender')      # Index data excluding the 'Gender' column

# Get employee count
print("Employee count in v_nameCollection after indexing:", getEmpCount(v_nameCollection))  # Output: number of indexed documents

# Delete employee by ID
delEmpById(v_nameCollection, 'E02003')

# Get employee count after deletion
print("Employee count in v_nameCollection after deletion:", getEmpCount(v_nameCollection))  # Output: updated count

# Search by column
print("Search 'IT' in Department:", searchByColumn(v_nameCollection, 'Department', 'IT'))  # Output: list of matching records
print("Search 'Male' in Gender:", searchByColumn(v_nameCollection, 'Gender', 'Male'))  # Output: list of matching records

# Get department facets
print("Department facet for v_nameCollection:", getDepFacet(v_nameCollection))  # Output: count of employees by department
print("Department facet for v_phoneCollection:", getDepFacet(v_phoneCollection))  # Output: count of employees by department
