from random import randint as ri
total = int(input('Введите кол-во конфет: '))
while total <= 0:
    total = int(input('Введите другое кол-во конфет: '))
# def game():
#     const_c = total
#     while const_c != 0:
#             player_one = int(input('Сколько хотите взять конфет? '))
#             if 0<player_one<=const_c:
#                 const_c = const_c - player_one
#                 result = const_c
#             else:
#                 print('Вы не можете взять это число')
#                 continue
#             print(f'В банке осталость {const_c} конфет')
#             if result == 0:
#                 print('Игра окончена. Победил игрок')
#             else:
#                 bot = ri(1,const_c)
#                 print(f'Бот взял {bot} конфет')
#                 const_c = const_c - bot
#                 result1 = const_c
#                 print(f'В банке осталость {const_c} конфет')
#                 if result1 == 0:
#                     print('Игра окончена. Победил бот')
# game()

# def games_pl():
#     const_c = total
#     while const_c != 0:
#         player_one = int(input('Сколько хотите взять конфет, первый игрок? '))
#         if 0<player_one<=const_c:
#             const_c = const_c - player_one
#             result = const_c
#         else:
#             print('Вы не можете взять это число')
#             continue
#         print(f'В банке осталость {const_c} конфет')
#         if result == 0:
#             print('Игра окончена. Победил первый игрок')
#             break
#         player_two = int(input('Сколько хотите взять конфет, второй игрок? '))
#         if 0<player_two<=const_c:
#             const_c = const_c - player_two
#             result1 = const_c
#         else:
#             print('Вы не можете взять это число')
#             continue
#         print(f'В банке осталость {const_c} конфет')
#         if result1 == 0:
#             print('Игра окончена. Победил второй игрок')
#             break
# games_pl()