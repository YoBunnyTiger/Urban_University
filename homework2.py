number_of_completed_homeworks = 12
number_of_hours_spent = 1.5
name_of_the_course = 'Python'
time_for_one_task = number_of_hours_spent / number_of_completed_homeworks

print('Курс: ', name_of_the_course, ', всего задач: ',
      number_of_completed_homeworks, ', затрачено часов: ',
      number_of_hours_spent, ', среднее время выполнения: ',
      time_for_one_task, ' часа.', sep='')
