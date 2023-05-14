import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('mylab-da0bf-firebase-adminsdk-1w6kd-498aefc91d.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mylab-da0bf-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('restricted_access/secret_document')
print(ref.get())

# Get a database reference to our posts
user = 'Sommai'
ref = db.reference('users/' + user + '/age')

# Read the data at the posts reference (this is a blocking operation)
print('Age of ' + user + ': ' + str(ref.get()))

ref_somsong = db.reference('users/Sommai')
print(ref_somsong.get())
