import json, random, os

def create_dir():
    os.mkdir('feedback/json')
    with open('feedback/list_feedback.txt','w') as f:
        f.close()
    with open('feedback/current_feedback.txt','w') as f:
        f.close()

def create_current_feedback(id:int):
    if get_name_current_feedback(id) != None:
        name = get_name_current_feedback(id)
        with open('feedback/current_feedback.txt', 'r') as f:
            spisok = f.readlines()
        for i in range(len(spisok)):
            if str(id) in spisok[i]:
                break
        spisok.pop(i)
        with open('feedback/current_feedback.txt', 'w') as f:
            f.writelines(spisok)
        os.remove(f'feedback/json/{name}.json')
    name = ''
    for _ in range(32):
        name += random.choice('0123456789abcdef')
    with open('feedback/current_feedback.txt', 'a') as f:
        f.write(f'{id}:{name}\n')
    data = {}
    with open(f"feedback/json/{name}.json", "w") as f:
        json.dump(data, f)

def add_to_current_feedback(id:int, key, val):
    name = get_name_current_feedback(id)
    with open(f"feedback/json/{name}.json", "r") as read_file:
        data = json.load(read_file)
    if key not in data:
        data[key] = val
    else:
        if isinstance(data[key], list):
            data[key].append(val)
        else:
            data[key] = [data[key], val]
    with open(f"feedback/json/{name}.json", "w") as write_file:
        json.dump(data, write_file)

def check_key_in_feedback(id:int, key):
    name = get_name_current_feedback(id)
    with open(f"feedback/json/{name}.json", "r") as read_file:
        data = json.load(read_file)
    return key in data

def get_name_current_feedback(id:int):
    with open('feedback/current_feedback.txt', 'r') as f:
        spisok = list(map(lambda x: [int(x.split(':')[0]),x.split(':')[1].strip()], f.readlines()))
    dic1 = {}
    for i in range(len(spisok)):
        dic1[spisok[i][0]] = spisok[i][1]
    if id in dic1:
        return dic1[id]

def get_current_feedback(id:int):
    name = get_name_current_feedback(id)
    with open(f"feedback/json/{name}.json", "r") as read_file:
        data = json.load(read_file)
    return data

def send_current_feedback_to_moderator(id:int):
    with open(f"feedback/current_feedback.txt", "r") as read_file:
        spisok =read_file.readlines()
    id_delete = 0
    for i in range(len(spisok)):
        if str(id) in spisok[i]:
            search = spisok[i]
            id_delete = i
            break
    with open(f"feedback/list_feedback.txt", "r") as read_file:
        spisok =read_file.readlines()
    spisok.append(search)
    with open(f"feedback/list_feedback.txt", "w") as write_file:
        write_file.writelines(spisok)

def dell_current_feedback(id:int):
    with open(f"feedback/current_feedback.txt", "r") as read_file:
        spisok =read_file.readlines()
    id_delete = 0
    for i in range(len(spisok)):
        if str(id) in spisok[i]:
            id_delete = i
            break
    spisok.pop(id_delete)
    with open(f"feedback/current_feedback.txt", "w") as write_file:
        write_file.writelines(spisok)

