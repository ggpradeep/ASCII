student_data = {"id1":{"name":"Sam","class":"A","subject":"English"},"id2":{"name":"Joseph","class": "B","subject":"Science"},"id3":{"name":"Ava","class":"A","subject":"Art"},"id4":{"name":"Mary","class":"C","subject":"Math"}}
print("Student records:")
print(student_data)

print("")
print("Details of id1:")
print(student_data.get("id1","Not Found"))

print("")
print("Details of id5:")
print(student_data.get("id5","Not Found"))

student_data["id5"] = {"name":"Jack","class":"C","subject":"History"}
print("")
print("Details of id5 after update:")
print(student_data.get("id5","Not Found"))

student_data["id2"]["subject"] = "Geography"
print("")
print("Details of id2 after update:")
print(student_data["id2"])
cleaned_data = {}
seen_records = []
for student_id, details in student_data.items():
    unique_key = (details["name"],details["class"], details["subject"])
if unique_key not in seen_records: 
    seen_records.append(unique_key)
cleaned_data[student_id] = details
student_data = cleaned_data
print("")
print("Details of student data after duplicate records:")
print(student_data)

removed_student = student_data.pop("id4", "Student not found")
print("")
print("Removed student:")
print(removed_student)

print("")
print("Total student records left:", len(student_data))

print("")
print("----- Final student subject records -----")
for student_id, details in student_data.items():
    print(student_id, ":" , details)
print("=================================================")