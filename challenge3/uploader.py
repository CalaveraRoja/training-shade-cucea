from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

print "Upload objects:" 
container_name = 'YOUR_CONTAINER'
container = conn.create_container(container_name)

pokemons = {'OBJECT_NAME_1': 'OBJECT_PATH_1', 'OBJECT_NAME_2': 'OBJECT_PATH_2', 'OBJECT_NAME_3': 'OBJECT_PATH_3'}
for object_name, file_path in pokemons.items():
    conn.create_object(container=container_name, name=object_name, filename=file_path)