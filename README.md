# Бот Рандомайзер | Генератор случайных чисел v1.05

![image](https://user-images.githubusercontent.com/92934389/139707853-b46f177e-4942-4bcf-9a04-483215db6ba6.png)
![image](https://user-images.githubusercontent.com/92934389/139708451-a4b2e88e-dbe9-4b42-ae5d-66adc7123ef8.png)
![image](https://user-images.githubusercontent.com/92934389/139708645-e635e58c-aa44-47a7-ae47-f71796588254.png)


Простой бот для лс сообщества в вк с шуточными ответами вместо ошибок при неправильном вводе пользователем значений

*Оригинал: https://vk.com/bot_randomizer*

## Установка библиотеки

Для Windows зайдите в папку своего пользователя

![image](https://user-images.githubusercontent.com/92934389/139820839-bb94b4f9-9355-4ce8-92dc-96f834425020.png)

Нажмите на строку места

![image](https://user-images.githubusercontent.com/92934389/139820872-248bd1e0-3537-4042-a345-283cf2b1f39f.png)

Введите "cmd" и нажмите Enter

![image](https://user-images.githubusercontent.com/92934389/139820939-c5d079b0-89db-403f-9b3f-367ad9bab2ed.png)

И в появившейся коснсоли пишем команду ниже:

```python
pip3 install vk_api
```

Для Linux достаточно с рабочего стола ввести эту команду (насколько мне известно)

## Настройка
Перед запуском необходимо создать токен в сообществе и вставить его в main.py
![image](https://user-images.githubusercontent.com/92934389/139710924-937da8a8-f726-498f-b268-156ecfa8fa37.png)
![image](https://user-images.githubusercontent.com/92934389/139710811-bf391752-3d8b-4031-acc9-78d3b751eff8.png)
![image](https://user-images.githubusercontent.com/92934389/139711045-6d8cf1af-a1e0-4ed0-bdce-8d6ccf9e55f6.png)
![image](https://user-images.githubusercontent.com/92934389/139711128-91966c97-816a-4e12-8bef-e7b653d216e9.png)
![image](https://user-images.githubusercontent.com/92934389/139711224-9a4f8f0c-44ac-455a-acbd-30fe3da2067f.png)
![image](https://user-images.githubusercontent.com/92934389/139711262-f73fd86e-5021-480e-a6d7-804a0ff84c21.png)

```python
vk_session = vk_api.VkApi(token = 'Сюда вставляем токен') # Api Токен
```

Например:

```python
vk_session = vk_api.VkApi(token = '67DBcnduASZfbAfaBSC783dfbAJScmOAC7ANDaoiskcNSuH8c9C7HCn&CgABCuAGCCjACoiacAOIUHC') # Api Токен
```
#### И iD
![image](https://user-images.githubusercontent.com/92934389/139712213-d6952951-91c8-493e-8fc9-d76745e11413.png)


```python
	members = vk_session.method('groups.getMembers', {'group_id' : Тут только цифрами iD сообщества})['items']
```

Например:

```python
	members = vk_session.method('groups.getMembers', {'group_id' : 206993699})['items']
```

Создайте файл "data.txt" (база данных) в папке с main.py

## Запуск

Запускайте main.py, пишите "начать" в личные сообщения сообщества и наслаждайтесь!

![image](https://user-images.githubusercontent.com/92934389/139713895-343a5484-e843-4c68-8b8f-81e8abcf7c05.png)
