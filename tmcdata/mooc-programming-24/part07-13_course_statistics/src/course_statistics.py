# Write your solution here
import urllib.request
import json
import math

def retrieve_all():
	request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
	active_course = []
	data = request.read()
	courses = json.loads(data)
	for dic in courses:
		if dic['enabled'] == True:
			course = (dic['fullName'], dic['name'], dic['year'], sum(dic['exercises']))
			active_course.append(course)
	return (active_course)

def retrieve_course(course_name: str):
	request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
	course_info = {}
	course = json.loads(request.read())
	course_info['weeks'] = len(course)
	max_student = 1
	total_hours = 0
	exercises = 0
	for week, content in course.items():
		if int(content['students']) > max_student:
			max_student = int(content['students'])
		total_hours += int(content['hour_total'])
		exercises += int(content['exercise_total'])
	course_info['students'] = max_student
	course_info['hours'] = total_hours
	course_info['hours_average'] = math.floor(total_hours / max_student)
	course_info['exercises'] = exercises
	course_info['exercises_average'] = math.floor(exercises / max_student)
	return (course_info)

if __name__ == "__main__":
	print(retrieve_course("docker2019"))
	
			 