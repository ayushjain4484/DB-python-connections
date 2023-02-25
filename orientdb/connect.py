import pyorient

# Initialize the Client
client = pyorient.OrientDB("localhost", 2424)

# Enable Token-based Authentication
client.set_session_token(True)

# Fetch Session Token
sessionToken = client.get_session_token()


session_id = client.connect('root', 'root')

if(session_id):
    print("connected")