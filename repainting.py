naylon = int(input())
paint = int(input())
thinner =int(input())
hours = int(input())

sum_naylon = (naylon + 2) * 1.50
sum_paint = (paint + paint * 0.1) * 14.50
sum_thinner = thinner * 5
bags = 0.40

materials_sum = sum_naylon + sum_paint + sum_thinner + bags

workers_sum = materials_sum * 0.30 * hours

total_sum = materials_sum + workers_sum

print(total_sum)