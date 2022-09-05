import json


def load_candidates():
    with open("candidates.json", 'rt', encoding="utf-8") as file:
        return json.loads(file.read())


def get_by_pk(pk):
    for candidate in load_candidates():
        if candidate["pk"] == pk:
            url = candidate['picture']
            result = f"<img src = '{url}'>"
            result += "<br>" + candidate['name']
            result += "<br>" + candidate["position"]
            result += "<br>" + candidate["skills"]
            return result
    return "no found"


def get_all():
    result = ""
    for candidate in load_candidates():
        result += "<br>" + candidate['name']
        result += "<br>" + candidate["position"]
        result += "<br>" + candidate["skills"] + "<br>"
    return result

def get_by_skill(skill_name):
    result = ""
    for candidate in load_candidates():
        for skill in candidate['skills'].split(', '):
            if skill_name.lower() == skill.lower():
                result += "<br>" + candidate['name']
                result += "<br>" + candidate["position"]
                result += "<br>" + candidate["skills"] + "<br>"
    return result





