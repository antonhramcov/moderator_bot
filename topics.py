def add_topic_in_list(id, name):
    with open('topic/list_topics.txt', 'a') as f:
        f.writelines(f'{id}:{name}\n')

def get_topics():
    with open('topic/list_topics.txt', 'r') as f:
        dic1 = {}
        for s in f.readlines():
            s = s.strip().split(':')
            dic1[s[0]] = s[1]
        return dic1


def get_topics_names():
    with open('topic/list_topics.txt', 'r') as f:
        dic1 = {}
        for s in f.readlines():
            s = s.strip().split(':')
            dic1[s[0]] = s[1]
        return list(dic1.values())
