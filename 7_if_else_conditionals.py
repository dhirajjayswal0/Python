def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    
    return the_mean

monday_temperature = [8.8, 9.1, 9.9]
student_grades = {"sam":8.8, "john":9.1, "sid":9.9}
print(mean(monday_temperature))
print(mean(student_grades))