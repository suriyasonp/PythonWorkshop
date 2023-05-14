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

#Save data

# Get a database reference to our blog.
ref = db.reference('')

users_ref = ref.child('users')
users_ref.set({
    'Sommai': {
        'date_of_birth': 'June 23, 1990',
        'full_name': 'Sommai Painaidee'
    },
    'Somsri': {
        'date_of_birth': 'December 9, 1995',
        'full_name': 'Somsri Meeginmeechai'
    }
})


posts_ref = ref.child('users')

new_post_ref = posts_ref.push()
new_post_ref.set({
    'author': 'gracehop',
    'title': 'Announcing COBOL, a New Programming Language'
})

# We can also chain the two calls together
posts_ref.push().set({
    'author': 'alanisawesome',
    'title': 'The Turing Machine'
})


hopper_ref = users_ref.child('gracehop')
hopper_ref.update({
    'nickname': 'Amazing Grace1111'
})

hopper_ref = ref.child('gracehop')
hopper_ref.delete()
print(ref.get())