"""
Não é possivel concatenar tipos diferentes de dados
Para exibir o resultado conforme exemplo abaixo, é necessário fazer a conversão do int e float em string

"""

# savings = 100
# result = 100 * 1.10 ** 7

# print(f'I started with ${str(savings)} and now have ${str(result)}. Awesome!')


# Create the areas list
# areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50, "lalal", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
# eat_sleep_area = areas[0::2]

# Print the variable eat_sleep_area
# print(eat_sleep_area)


# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
print(areas_1)
print(areas)


# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)