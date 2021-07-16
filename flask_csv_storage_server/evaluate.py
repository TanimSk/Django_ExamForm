import json


def sub_lists(l):
    lists = []
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists


def mcq_list(ans):
    array = []
    for i in ans['mcq_ans']:
        array.append(str(ans['mcq_ans'][i])[1:-1])
    return str(array)[1:-1]


def evaluate(ques_json, ans_json):
    ques_json = json.loads(ques_json)
    ans_json = json.loads(ans_json)
    print(ques_json, ans_json)
    print(type(ques_json), type(ans_json))
    mark = 0
    for i in ans_json['mcq_ans']:
        if len(ques_json['mcq_correct'][i]) >= len(ans_json['mcq_ans'][i]):
            for c in sub_lists(ques_json['mcq_correct'][i]):
                if ans_json['mcq_ans'][i] == c:
                    mark += 1

    qa_ans = str(ans_json['qa_ans'])[1:-1]
    mcq_ans = mcq_list(ans_json)
    csv_response = [ans_json['name'], ans_json['duration'], mark, qa_ans, mcq_ans]

    return csv_response

# q = json.loads('{"mcq": {"0": ["aa", "bb", "cc", "dd"], "1": ["tyt", "ty"]}, "date": 20210716, "title": "teteee", "images": {"0": [], "1": [], "2": []}, "starts": 47220, "ques_qa": ["tyrtyet"], "duration": 18000, "ques_mcq": ["tetetet", "tyty"], "qa_correct": ["rterte"], "mcq_correct": {"0": ["aa", "bb"], "1": ["ty"]}}')
# a = json.loads('{"mcq_ans":{"0":["cc"],"1":["tyt"]},"qa_ans":["pop"],"name":"tanim","duration":"04:56:26"}')
# print(evaluate(q, a))
# print(mcq_list(a))
