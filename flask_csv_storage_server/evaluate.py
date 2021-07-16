import json


def sub_lists(l):
    lists = []
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists


def evaluate(ques_json, ans_json):
    ques_json = json.loads(ques_json)
    ans_json = json.loads(ans_json)
    mark = 0
    for i in ans_json['mcq_ans']:
        if len(ques_json['mcq_correct'][i]) >= len(ans_json['mcq_ans'][i]):
            for c in sub_lists(ques_json['mcq_correct'][i]):
                if ans_json['mcq_ans'][i] == c:
                    mark += 1

    # qa_ans = str(ans_json['qa_ans'])[1:-1]
    # mcq_ans = mcq_list(ans_json)
    csv_response = [ans_json['name'], ans_json['duration'], mark]


    for x in ans_json['qa_ans']:
        csv_response.append(x)


    for i in ans_json['mcq_ans']:
        arr = ""
        for c in ans_json['mcq_ans'][i]:
            arr += c +","
        csv_response.append(arr[:-1])


    return csv_response

# q = '{"mcq": {"0": ["aa", "bb", "cc", "dd"], "1": ["tyt", "ty"]}, "date": 20210716, "title": "teteee", "images": {"0": [], "1": [], "2": []}, "starts": 47220, "ques_qa": ["tyrtyet"], "duration": 18000, "ques_mcq": ["tetetet", "tyty"], "qa_correct": ["rterte"], "mcq_correct": {"0": ["aa", "bb"], "1": ["ty"]}}'
# a = '{"mcq_ans":{"0":["cc"],"1":["tyt"]},"qa_ans":["pop"],"name":"tanim","duration":"04:56:26"}'
# print(evaluate(q, a))
# # print(mcq_list(a))
