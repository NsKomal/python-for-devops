server_details = [ 
     {
         'name': 'app',
         'size': 'small',
         'ip':'10.2.2.2'
     },
     {'name': 'db', 'size':'medium', 'ip':'10.3.3.3' },
     {
         'name': 'web',
         'size':'large',
         'ip':'10.4.4.4'
     }
]

print(server_details[2]["name"])
