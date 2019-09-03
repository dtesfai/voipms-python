from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

print("Which category does this endpoint fall under?")
subdir_index = int(input("1: accounts, 2: call_detail_records, 3: dids, 4: general, 5: voicemail: "))
subdir = ("accounts", "call_detail_records", "dids", "general", "voicemail")[subdir_index - 1]

endpoint = input("endpoint name? ")
method = input("method name? ")

filename = "../voipms/api/{}/{}.py".format(subdir, method)

template = env.get_template('endpoint.j2')
method_split = method.split('_')
class_name = ''.join((i.title() for i in method_split))
output = template.render(endpoint=endpoint, class_name=class_name)

with open(filename, 'a') as file:
    file.writelines(output)



filename = "../voipms/api/{}/__init__.py".format(subdir)
template = env.get_template('import.j2')
method_split = method.split('_')
class_name = ''.join((i.title() for i in method_split))
output_import = template.render(method_name=method, class_name=class_name, category_name=subdir)

template = env.get_template('initialize.j2')
output_init = template.render(method_name=method)

template = env.get_template('subdir_init.j2')
output_property = template.render(method_name=method, class_name=class_name)

with open(filename, 'r') as file:
    contents = file.readlines()

pos = 0

for k, v in enumerate(contents):
    if v == "\n":
        contents.insert(k, output_import + "\n")
        pos = k
        break

for k, v in enumerate(contents[pos+2:], pos+2):
    if v == "\n":
        contents.insert(k, output_init + "\n")
        break
    
contents.append("\n\n" + output_property)

with open(filename, 'w') as file:
    file.writelines(contents)



filename = "../voipms/api/__init__.py"

template = env.get_template('dir_init.j2')
output = template.render(subdir=subdir, method_name=method)

with open(filename, 'a') as file:
    file.writelines("\n\n" + output)