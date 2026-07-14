student_data = {"id1": {"name": "jack", "class": "A", "subject": "math"}, "id2": {"name": "sophia", "class": "A", "subject": "english"}, "id3":{"name": "evan", "class": "A", "subject": "history"}}
result = {}
seen_keys = []
for student_id, details in student_data.items():
    unique_key = (details["name"],details["class"],details["subject"])
if unique_key not in seen_keys:
    seen_keys.append(unique_key)
    result[student_id] = details
for k, v in result.items():
    print(k, ":", v)
