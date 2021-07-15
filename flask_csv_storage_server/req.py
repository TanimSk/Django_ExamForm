import requests

requests.post('http://127.0.0.1:5000/csv_manager', {'mode': 'wh', 'filename': "thh/chondro_bindu.csv", 'row': '[[1, 2, 2], [1, 2, 2]]', 'key': 'KEY'})
