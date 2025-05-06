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

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#search method
partner = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 2, 'limit': 5})
# print("Partner : ",partner)

#read method
partner_record = models.execute_kw(db, uid, password, 'res.partner', 'read', [partner],  {'fields': ['id', 'name']})
# print(partner_record)

#search count
partner_record_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
print("partner_record_count : ",partner_record_count)