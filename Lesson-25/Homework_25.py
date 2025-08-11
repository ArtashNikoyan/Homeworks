import json

# # 1  - pycharm-ում կարդալ data ֆայլը,
# #    - կարդացած list-ում կթողնի միայն 3-ի բաժանվող թվերը,
# #    - կտպի ստացված list-ի արժեքների միջին թվաբանականը։
#
# with open('data.json', 'r+') as f:
#     file = json.load(f)
#
#     res = []
#     for num in file:
#         if num % 3 == 0:
#             res.append(num)
#
# avg = sum(res) / len(res)
# print(int(avg))

# # 2․ Գրել ծրագիր, որը․
# #    - հետևյալ dict_1-ից կստանա նոր dict_2 այնպես, որ dict_2-ի key-երը լինեն dict_1-ի value-ները,
# #      իսկ value-ները՝ dict_1-ի value-ների երկարությունները,
# #    օրինակ՝ dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'},
# #    պետք է ստացվի՝ dict_2 = {'red': 3, 'green': 5, 'black': 5, 'white': 5}:
#
# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dict_2 = {}
#
# for key, value in dict_1.items():
#     dict_2[value] = key
#
# print(dict_1)
# print(dict_2)

# 3. Գրել ֆունկցիա, որը․
#    - կֆիլտրի տրված dictionary-ի value-ները, թողնելով միայն կենտ թվերը,
#    - կվերադարձնի ստացված dictionary-ն,
#    օրինակ՝ {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]},
#    պետք է ստացվի՝ {'a': [1, 3, 7], 'b': [], 'c': [9, 9, 5]}:

dict_1 = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
lst = []

for key, value in dict_1.items():
    for i in value:
        if i % 2 != 0:
            lst.append(i)
    dict_1[key] = lst
    lst = []
    
print(dict_1)

# 4. Այսուհետ բոլոր տնայինները տեղադրելու եք ձեր GitHub-ի էջ, և ինձ ուղարկելու եք ձեր GitHub-ի տնայինի repo-ի հղումը։
