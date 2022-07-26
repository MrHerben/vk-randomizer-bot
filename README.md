# Бот Рандомайзер | Генератор случайных чисел v1.05

Простой бот для лс сообщества в вк с шуточными ответами вместо ошибок при неправильном вводе пользователем значений

*Оригинал: https://vk.com/bot_randomizer*

## Установка библиотеки

Для Windows введите в поиск пуска cmd и нажмите Enter, там введите:

```python
pip3 install vk_api
```

Для Linux честно в душе не ебу, как-то там через консоль и тоже это прописать

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

UPD: Это был мой самый первый проект на питоне и на программировании в принципе.
Хоть он по правде говоря и не использует random.org, а псевдо генерироаание вшитое в питоне, но согласитесь — говнокода в основном тут нет.
Интересно эту страницу хоть кто-то, кроме меня чешущего своё самолюбие заходит?
