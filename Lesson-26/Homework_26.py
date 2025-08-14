import math


# # 1․ Գրել ֆունկցիա, որը․
# #    - որպես արգումենտ կընդունի շրջանագծի շառավիղը (r) և սեկտորի անկյունը (alpha) ռադիաններով արտահայտված,
# #    - կհաշվի և կտպի համապատասխան շառավղով և անկյունով սեկտորի մակերեսը,
# #    - բանաձևը՝ S = (pi * r ** 2) * alpha / 360, բանաձևի մեջ alpha-ն արտահայտված է աստիճաններով։
#
#
# def get_sector_area(r: int | float, alpha: int | float) -> float:
#     s = (math.pi * r ** 2) * alpha / 360
#
#     return round(s, 2)
#
#
# print(get_sector_area(5, 120))

# # 2․ Գրել ֆունկցիա, որը․
# #    - կստանա արգումենտ արաբական բնական թիվ (0-ից մեծ),
# #    - կվերադրձնի այդ թիվը հռոմեական տեսքով,
# #    հռոմեական թվերի համարժեքները՝ I-1, V-5, X-10, L-50, C-100, D-500, M-1000,
# #    օրինակ՝ 15 -> XV,
# #            72 -> LXXII,
# #            9 -> IX:
# #
#
# def get_roman_num(n: int) -> str:
#     roman_map = {
#         1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
#         100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
#         10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
#     }
#
#     if n == 0:
#         return ''
#
#     for i in roman_map:
#         if i <= n:
#             return roman_map[i] + get_roman_num(n - i)
#
#
# print(get_roman_num(1987))

# # 3․ Գրել ֆունկցիա, որը․
# #    - տրված բառերի list-ը կֆիլտրի այնպես, որ կթողի միայն ամենաերկար բառերը
# #      (այսինքն՝ կգտնի ամենաերկար բառի երկարությունը և լիստում կթողնի միայն այդ երկարության բառերը),
# #    օրինակ՝ input = ["aba", "aa", "z", "ad", "vcd", "aba"]
# #            output = ["aba", "vcd", "aba"],
# #
# #            input = ["aba", "aa", "z", "advc", "vcd", "aba"]
# #            output = ["advc"],
#
# def len_filter(lst: list) -> list:
#     max_len = len(max(lst, key=len))
#     res = list(filter(lambda x: len(x) == max_len, lst))
#
#     return res
#
#
# print(len_filter(["aba", "aa", "z", "ad", "vcd", "aba"]))
# print(len_filter(["aba", "aa", "z", "advc", "vcd", "aba"]))

# 4. Գնահատեք Ձեր գրած կոդերը Big O notation-ի միջոցով։

# 1. O(1)
# 1. O(n^2)
# 1. O(n)
