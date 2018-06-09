# ‘v’ - просит ввести новый визит (начало, затем конец)
# ‘p’ - просит ввести дату следующего визита, говорит, сколько дней вы можете провести в шенгене
# ‘e’ - выход

# На зачёт с отличием:
 # ‘r’ - просит ввести начало и конец визита, удаляет визит
 # Вывод ошибки, если визиты пересекаются.

residence_limit = 90
schengen_constraint = 180

visits = [[1, 10], [61, 90], [101, 140], [141, 160], [271, 290]]

print(visits)

def get_visit_length(visit):
  return visit[1] - visit[0] + 1

def get_days_for_visits(visits):
	days_for_visits = []
	for visit in visits:
	    days_for_visit = 0
	    for past_visit in visits:
	        if visit[0] - schengen_constraint < past_visit[0] < visit[0]:
	            days_for_visit += get_visit_length(past_visit)
	    days_for_visit += get_visit_length(visit)
	    days_for_visits.append(days_for_visit)
	return days_for_visits

days_for_visits = get_days_for_visits(visits)

for visit, total_days in zip(visits, days_for_visits):
  if total_days > residence_limit:
    overstay_time = total_days - residence_limit
    print('during the visit', visit, 'number of days of stay is exceeded by:', overstay_time, 'days')

def predict_visit_days(day_in_future):
  visits_with_future = visits + [[day_in_future, day_in_future]]
  days_for_visits_in_future = get_days_for_visits(visits_with_future)

  days_in_es_for_future_visit = days_for_visits_in_future[len(days_for_visits_in_future)-1]

  days_we_can_stay_in_es = residence_limit - days_in_es_for_future_visit + 1
  print('I can stay in schengen {0} days, if I arrive on {1} day'.format(days_we_can_stay_in_es, day_in_future))

def add_visit():
  print('beggining of trip:')
  start = int(input())
  print('end of trip:')
  end = int(input())
  visits.append([start, end])
  for visit1 in visits:
    for visit2 in visits:
      if visit1[0] > visit2[0] and visit1[0] < visit2[1]:
        raise Exception('days of visits cannot be overlapping')
  print(visits)
  for visit, total_days in zip(visits, days_for_visits):
    if total_days > residence_limit:
      overstay_time = total_days - residence_limit
      print('during the visit', visit, 'number of days of stay is exceeded by:', overstay_time, 'days')

def predict_visit():
  print('planning of trip')
  print('Write the date of trip:')
  day_of_visit = int(input())
  predict_visit_days(day_of_visit)

def delete_visit():
  print('Write the day of arrival')
  day_of_arrival = int(input())
  print('day of leave')
  day_of_leave = int(input())
  Visit_to_delete = [day_of_arrival, day_of_leave]
  #print(visit)
  #for N in visits:
  visits.remove(Visit_to_delete)
  print(visits)
  for visit, total_days in zip(visits, days_for_visits):
    if total_days > residence_limit:
      overstay_time = total_days - residence_limit
      print('during the visit', visit, 'number of days of stay is exceeded by:', overstay_time, 'days')

while True:
	print('Write Command')
	print('v - добавить визит')
	print('p - predict how many days can I stay in schengen')
	print('e - stop the programme')
	print('r - for deleting visit from the list')
	user_input = input()
	if user_input == 'v':
	  add_visit()
	if user_input == 'p':
	  predict_visit()
	if user_input == 'e':
	  break
	if user_input == 'r':
	  delete_visit()
