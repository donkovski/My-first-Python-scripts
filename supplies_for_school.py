ballpoint_pen = int(input())

markers = int(input())

liquid_for_desk_board = int(input())

discount = int(input())

price_for_ballpoint_pen = ballpoint_pen * 5.80

price_for_markers = markers * 7.20

price_for_liquid = liquid_for_desk_board * 1.20

final_discount = discount / 100

sum_of_all = (price_for_ballpoint_pen + price_for_markers + price_for_liquid)

final_sum = sum_of_all - (sum_of_all * final_discount)

print(final_sum)
