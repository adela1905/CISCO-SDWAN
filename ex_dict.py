questions = ['name', 'quest', 'favorite colour']
answers = ['lancelot', 'holy grail', 'blue']
for q, a in zip(questions, answers):
	print ('What is your {0}? It is {1}'.format(q, a))
