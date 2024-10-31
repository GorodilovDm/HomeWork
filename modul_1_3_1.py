number_of_completed_homework = 12
number_of_spent_hours = 1.5
cours_name = 'Python'
time_for_1_task = number_of_spent_hours / number_of_completed_homework

print('Курс: ' + cours_name + ',' + ' всего задач:', number_of_completed_homework, ',' +
      ' затрачено часов:', number_of_spent_hours, ',' +
      ' среднее время выполнения:', time_for_1_task, 'часа')

print(f'Курс: {cours_name}, всего задач: {number_of_completed_homework},'
      f' затрачено часов: {number_of_spent_hours}, '
      f'среднее время выполнения: {time_for_1_task} часа')
