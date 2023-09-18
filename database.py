from pymongo import MongoClient

# Replace these with your actual credentials
username = 'antony313'
password = 'hcXPkEGLdvMqxYIC'
cluster_url = 'my-prodb.f72oapk.mongodb.net/'

# Function to create a MongoDB client and return the database
def get_db():
    connection_string = f"mongodb+srv://{username}:{password}@{cluster_url}"
    client = MongoClient(connection_string)
    db = client['my-proDB']  # Replace with your actual database name
    return db
