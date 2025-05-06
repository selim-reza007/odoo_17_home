import xmlrpc.client

url = 'http://localhost:8066'
db = 'odoo_17_dev'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#authenticate from Odoo and get user info
uid = common.authenticate(db, username, password, {})
if uid:
    print("Authentication success!")
else:
    print("Authentication fail!")
