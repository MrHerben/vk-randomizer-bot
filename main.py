
# Бот Рандомайзер | Генератор случайных чисел
# v1.05
#
# Код для самой работы бота (база данных, личные сообщения) был взят из исходника DimPy
#
# За всем остальным, то есть основную работу, код, его декорация, генерация и т.д стоит Herben
# VK: https://vk.com/armemmm
#
# Оригинал: https://vk.com/bot_randomizer

import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType
from os.path import abspath as tdir
import random

vk_session = vk_api.VkApi(token = 'tut_dlinniy_token') # Api Токен
longpoll = VkLongPoll(vk_session)

class User(): # Значения у каждого пользователя в базе данных
	def __init__(self, id, mode, second_num, first_num, random, additional):
		self.id = id
		self.mode = mode
		self.second_num = second_num
		self.first_num = first_num
		self.random = random
		self.additional = additional

def check_registration(id): # Функция проверки регистрации
	members = vk_session.method('groups.getMembers', {'group_id' : 206993699})['items']
	return (id in members)

def save_bd(users): # Функция сохранения базы данных
	lines = []
	for user in users:
		lines.append(f'"id" : {user.id}, "mode" : "{user.mode}", "first_num" : "{user.first_num}", "second_num" : "{user.second_num}", "random" : "{user.random}", "additional" : {user.additional}')
	lines = '\n'.join(lines)
	with open(f'{tdir(__file__)}/data.txt'.replace('\\', '/').replace('main.py/', ''), 'w', encoding = 'utf-8') as file:
		file.write(lines)
		file.close()

def read_bd(): # Функция считывания базы данных
	users = []
	with open(f'{tdir(__file__)}/data.txt'.replace('\\', '/').replace('main.py/', ''), 'r', encoding = 'utf-8') as file:
		lines = [x.replace('\n', '') for x in file.readlines()]
		file.close()
	for line in lines:
		line = eval('{' + line + '}')
		if line != '{}':
			users.append(User(id = line['id'], mode = line['mode'], random = line['random'], second_num = line['second_num'], first_num = line['first_num'], additional = line['additional']))
	return users

def get_keyboard(buts): # Функция создания клавиатур
	nb = []
	color = ''
	for i in range(len(buts)):
		nb.append([])
		for k in range(len(buts[i])):
			nb[i].append(None)
	for i in range(len(buts)):
		for k in range(len(buts[i])):
			text = buts[i][k][0]
			color = {'зелёный' : 'positive', 'красный' : 'negative', 'синий' : 'primary', 'белый' : 'secondary'}[buts[i][k][1]]
			nb[i][k] = {"action": {"type": "text", "payload": "{\"button\": \"" + "1" + "\"}", "label": f"{text}"}, "color": f"{color}"}
	first_keyboard = {'one_time': False, 'buttons': nb}
	first_keyboard = json.dumps(first_keyboard, ensure_ascii=False).encode('utf-8')
	first_keyboard = str(first_keyboard.decode('utf-8'))
	return first_keyboard

def sender(id, text, key): # Отправка сообщения со сменной клавиатуры
	vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : key, 'dont_parse_links' : 1})

def sender_info(id, text): # Отправка сообщения
	vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'dont_parse_links' : 1})

start_key = get_keyboard([
	[('Начать', 'синий')]
])

rocket_key = get_keyboard([
	[('👍 Полностью за!', 'белый')],
	[('✅ Да, конечно', 'синий')],
	[('😌 Непротив', 'красный')]
])

tryagain_key = get_keyboard([
	[('процентом ракет долетевших до омэрики', 'синий')]
])

menu_key = get_keyboard([
	[('⚡ Сгенерировать', 'синий')],
    [('❗ Инфо', 'белый')]
])

r_choose_key = get_keyboard([
	[('🎱 Числовой (ОТ число ДО число)', 'синий')],
	[('🆎 Буквенный (Слово или Слово)', 'белый')],
	[('Назад', 'красный')]
])

retry_key = get_keyboard([
	[('🔄 Повторить', 'синий')],
    [('⏮ В главное меню', 'белый')]
])

back_key = get_keyboard([
	[('Назад', 'красный')]
])

clear_key = get_keyboard([])

users = read_bd()

print('[OK]...')
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:

			id = event.user_id
			msg = event.text.lower()

			if msg == 'начать':

				if check_registration(id):
					flag = 0
					for user in users:
						if user.id == id:
							flag = 1
							break
					if not(flag): # Если пользователя нет в базе данных, то он записывается и получает сообщение
						users.append( User(id = id, mode = 'start', first_num = 0, second_num = 0, random = 0, additional = 0) )
						print('+1')
						sender_info(id, '👋 Добро пожаловать в простой недо-рофловый рандомайзер!')
						sender(id, '⚙ Выберите действие:', menu_key)
					elif flag: # Если пользователь есть в базе данных, то он отправляется в главное меню
						for user in users:
							if user.id == id:
								sender(id, '⚙ Выберите действие:', menu_key)
								user.mode = 'start'
				else:
					sender(id, '❌ Подписка не обнаружена!\nДля работы бота, необходимо подписаться на сообщество!', start_key)

			else:
				for user in users:
					if user.id == id:

						if user.id == id:
							if user.mode == 'start':

								if msg == '❗ инфо':
									sender(id, '🤖 Бот сделан с ❤ на:\n\n👅 Языке Python\n✅ Оригинальном VkApi\n', back_key)
									user.mode = 'info'

								if msg == '⚡ сгенерировать':
									sender(id, '⚙ Выберите способ:', r_choose_key)
									user.mode = 'r_choose'

								if msg == 'назад':
									sender_info(id, '❕ Вы уже в главном меню\n\n Скорее всего у вас плохой интернет, потому что при нажатии кнопки "Назад", сразу появляются другие')

								if msg == '⏮ в главное меню':
									sender_info(id, '❕ Вы уже в главном меню\n\n Скорее всего у вас плохой интернет, потому что при нажатии кнопки "⏮ В главное меню", сразу появляются другие')

							elif user.mode == 'r_choose':
								if msg == '🎱 числовой (от число до число)':
									sender(id, '📝 [1/2] Введите ОТ скольки рандомизировать число:\nНапример: 1', back_key)
									user.mode = 'random_1'
								if msg == '🆎 буквенный (слово или слово)':
									sender(id, '📝 [1/2] Введите первое слово:\nНапример: Красный доширак', back_key)
									user.mode = 'random_a'
								if msg == 'процентом ракет долетевших до омэрики':
									sender(id, 'сколько запустить ракет?', clear_key)
									user.mode = 'rocket'
								if msg == 'назад':
									sender(id, '⚙ Выберите действие:', menu_key)
									user.mode = 'start'

							elif user.mode == 'rocket':
								user.first_num = event.text
								if user.first_num.isdigit():
									if int(user.first_num) <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
										sender(id, 'подготовка ядерных боеголовок...', clear_key)
										sender_info(id, '✅ ядерные боеголовки успешно подготовлены')
										sender_info(id, 'раскрашивание их в российский флаг...')
										sender_info(id, '✅ ядерные боеголовки успешно раскрашены в российский флаг')
										sender_info(id, 'направление их на белый дом...')
										sender_info(id, '✅ направление на белый дом задано успешно')
										sender(id, 'Запустить ракеты?', rocket_key)
										user.mode = 'rocket_ready'
									else:
										sender(id, '❌Ошибка!\n\n🚀 Столько ракет ещё не построено, пожалуйста попробуйте ещё раз', tryagain_key)
										user.mode = 'r_choose'
								else:
									sender(id, '❌Ошибка!\n\n😟Похоже что вы пиндос, но ладно, мы прощаем, раз уж вы сами захотели запустить ракеты на свою страну, так вот, нужно ввести число, попробуйте ещё раз', tryagain_key)
									user.mode = 'r_choose'

							elif user.mode == 'rocket_ready':
								sender_info(id, '..🚀🚀🚀........🇺🇸')
								sender_info(id, '....🚀🚀🚀......🇺🇸')
								sender_info(id, '......🚀🚀🚀....🇺🇸')
								sender_info(id, '........🚀🚀🚀..🇺🇸')
								sender_info(id, '..........🚀🚀🚀🇺🇸')
								sender(id, f'✅ До омэрики успешно долетели все {user.first_num} ракет', menu_key)
								user.mode = 'start'

							elif user.mode == 'random_a':
								if msg == 'назад':
									sender(id, '⚙ Выберите способ:', r_choose_key)
									user.mode = 'r_choose'
								else:
									user.first_num = event.text
									sender(id, '📝 [2/2] Введите второе слово:\nНапример: Зелёный доширак', back_key)
									user.mode = 'random_b'

							elif user.mode == 'random_b':
								if msg == 'назад':
									sender(id, '📝 [1/2] Введите первое слово:\nНапример: Красный доширак', back_key)
									user.mode = 'random_a'
								else:
									user.second_num = event.text
									or_or = [user.first_num, user.second_num]
									user.random = random.choice(or_or)
									if len(str(user.random)) >= 1000:
										sender(id, 'Чувак, я просил слово, а не войну и мир', menu_key)
										user.mode = 'start'
									else:
										if user.first_num == user.second_num:
											sender(id, 'Происходит вычисление для тупого кожанного ублюдка не знающего что он ввёл одно и тоже значение...', retry_key)
											sender_info(id, 'Загрузка.')
											sender_info(id, 'Загрузка..')
											sender_info(id, 'Загрузка...')
											sender_info(id, f'✅ Выпадает {user.random}')
											user.mode = 'final_ab'
										else:
											sender(id, f'✅ Выпадает {user.random}', retry_key)
											user.mode = 'final_ab'

							elif user.mode == 'random_1':
								if msg == 'назад':
									sender(id, '⚙ Выберите способ:', r_choose_key)
									user.mode = 'r_choose'
								else:
									user.first_num = event.text
									if user.first_num.isdigit():
										sender(id, '📝 [2/2] Введите ДО скольки рандомизировать число:\nНапример: 100', back_key)
										user.mode = 'random_2'
									else:
										sender(id, '❗ Необходимо ввести ЧИСЛО!', back_key)
										sender(id, '📝 [1/2] Введите ОТ скольки рандомизировать число:\nНапример: 1', back_key)
										user.additional += 1
										user.mode = 'random_1'

							elif user.mode == 'random_2':
								if msg == 'назад':
									sender(id, '📝 [1/2] Введите ОТ скольки рандомизировать число:\nНапример: 1', back_key)
									user.mode = 'random_1'
								else:
									user.second_num = event.text
									if user.second_num.isdigit():
										if int(user.first_num) < int(user.second_num):
											user.random = random.randint(int(user.first_num), int(user.second_num))
											if int(user.second_num) >= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
												sender(id, 'ты ебобо?', menu_key)
												sender_info(id, 'я тебе не сервер пентагона шобы такие нагрузки выдерживать')
												user.mode = 'start'
											else:
												sender(id, f'✅ Выпадает {user.random}', retry_key)
												user.mode = 'final'
										if int(user.first_num) == int(user.second_num):
											sender_info(id, f'Эм ну... чел, я обычный бот сделаный чисто по приколу другим челом от скуки хостящийся на серверах у казахов, я просто физически не могу сгенерировать число от {user.first_num} до {user.second_num}. Я не супер компьютер от IBM или Илона Маска, но раз ты просишь, я попробую сгенерировать это число')
											user.random = random.randint(int(user.first_num), int(user.second_num))
											if int(user.random) >= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
												sender(id, 'ты ебобо?', menu_key)
												sender_info(id, 'я тебе не сервер пентагона шобы такие нагрузки выдерживать')
												user.mode = 'start'
											else:
												sender(id, f'✅ Выпадает {user.random}', retry_key)
												user.mode = 'final'
										if int(user.first_num) > int(user.second_num):
											sender_info(id, 'какие же вы кожаные ублюдки конечно тупые')
											sender_info(id, f'По русски сказано — ОТ и ДО, то есть от {user.second_num} до {user.first_num}')
											sender_info(id, f'ТЫ ЖЕ МНЕ ПИШЕШЬ — ОТ {user.first_num} ДО {user.second_num}')
											sender(id, 'к твоему счастью в отличие от тебя я умею думать, поэтому держи результат:', retry_key)
											user.random = random.randint(int(user.second_num), int(user.first_num))
											if user.first_num >= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
												sender(id, 'ты ебобо?', menu_key)
												sender_info(id, 'я тебе не сервер пентагона шобы такие нагрузки выдерживать')
												user.mode = 'start'
											else:
												sender(id, f'✅ Выпадает {user.random}', retry_key)
												user.mode = 'final'
									else:
										sender(id, '❗ Необходимо ввести ЧИСЛО!', back_key)
										sender(id, '📝 [2/2] Введите ДО скольки рандомизировать число:\nНапример: 100', back_key)
										user.additional += 1
										user.mode = 'random_2'

							if user.additional == 2:
								sender(id, 'блять ты долбаёб сука, твой родной язык джаваскрипт что-ли я не понимаю', back_key)
								user.additional +=1

							if user.additional == 4:
								sender(id, 'бля иди нахуй короче не буду я тебе ничего генерировать', menu_key)
								user.additional = 0
								user.mode = 'start'

							elif user.mode == 'final_ab':
								if msg == '⏮ в главное меню':
									sender(id, '⚙ Выберите действие:', menu_key)
									user.mode = 'start'
									user.first_num = 0
									user.second_num = 0
									user.random = 0
								if msg == '🔄 повторить':
									if user.first_num == user.second_num:
										sender_info(id, 'Уважаемый кожанный ублюдок, так как вы всё равно игнорируете моё сообщение о том, что вы ввели одно и тоже значение и генерировать тут нечего, то я тут тихонько попою')
										sender_info(id, "I want to break free...\nI want to break free...\nI want to break free from your lies\n\nYou're so self-satisfied, I don't need you\n\nI've got to break free\n\nGod knows... God knows, I want to break free...")
										or_or = [user.first_num, user.second_num]
										user.random = random.choice(or_or)
										sender(id, f'✅ Выпадает {user.random}', retry_key)
									else:
										or_or = [user.first_num, user.second_num]
										user.random = random.choice(or_or)
										sender(id, f'✅ Выпадает {user.random}', retry_key)

							elif user.mode == 'final':
								if msg == '⏮ в главное меню':
									sender(id, '⚙ Выберите действие:', menu_key)
									user.mode = 'start'
									user.first_num = 0
									user.second_num = 0
									user.random = 0
								if msg == '🔄 повторить':
									if int(user.first_num) < int(user.second_num):
										user.random = random.randint(int(user.first_num), int(user.second_num))
										sender(id, f'✅ Выпадает {user.random}', retry_key)
									if int(user.first_num) == int(user.second_num):
										user.random = random.randint(int(user.first_num), int(user.second_num))
										sender(id, '✅ Выпадает {user.random}❌Ошибка', retry_key)
										sender(id, '❌Ошибка', clear_key)
										sender_info(id, '❌БОТ ПЕРЕГРУЖЕН!')
										sender_info(id, '❌БОТ ПЕРЕГРУЖЕН!')
										sender_info(id, '❌БОТ ПЕРЕГРУЖЕН!')
										sender_info(id, '🔃 Перезагрузка, пожалуйста подождите')
										sender_info(id, '👋 Здраствуйте, кожанный ублюдок\n\nВ связи с тем что какой-то ёбик уронил бота — был выполнен перезапуск')
										sender(id, '⚙ Выберите действие:', menu_key)
										user.mode = 'start'
									if int(user.first_num) > int(user.second_num):
										user.random = random.randint(int(user.second_num), int(user.first_num))
										sender(id, f'✅ Выпадает {user.random}', retry_key)
										user.mode = 'final'

							elif user.mode == 'info':
								if msg == 'назад':
									sender(id, '⚙ Выберите действие:', menu_key)
									user.mode = 'start'

								pass

			save_bd(users)
