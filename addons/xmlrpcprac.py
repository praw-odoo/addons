import xmlrpc.client

db = "test"
username = "admin"
password ="admin"

# common = xmlrpc.client.ServerProxy('http:localhost:8069/xmlrpc/2/common')
common = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

print(common.version())

if uid:
    print("connection successful")

models = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/object')
if models.execute_kw(db, uid, password, 'estate.property', 'create', [{'name':'xmlrpc data', 'state':'new', 'expected_price':'45000'}]):
    print("property successfully created")
