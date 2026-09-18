# Program for calculating HDI(Only diffrence is worst index)
from math import log, cbrt, e

# Health
MIN_EXPECTANCY = 20
MAX_EXPECTANCY = 85
# Education
MAX_SCHOOLING_YEARS = 18
MAX_MEAN_SCHOOLING = 15
# GNI
MIN_GNI = 100
MAX_GNI = 75000

country = input("Enter name of your country: ")
# Health
life_expentancy = float(input(f'Enter life expentancy in {country}: '))

# Education
schooling_years = float(input(f'Enter how much schooling years in {country}: '))
mean_schooling_years = float(input(f'Enter mean of schooling years in {country}: '))

# GNI
gni_value = float(input(f'Enter GNI per capita in {country}: '))


health_index = (life_expentancy - MIN_EXPECTANCY)/(MAX_EXPECTANCY - MIN_EXPECTANCY)

expected_years_index = schooling_years / MAX_SCHOOLING_YEARS
mean_years_index = mean_schooling_years / MAX_MEAN_SCHOOLING
education_index = (expected_years_index + mean_years_index) / 2

gni_index = (log(gni_value)- log(MIN_GNI)) / (log(MAX_GNI) - log(MIN_GNI))

worst_index = min(health_index, education_index, gni_index)

hdi_index = cbrt(health_index * education_index * gni_index)


print(f'Life expectancy index for {country} is {health_index:.4f}.')
print(f'Education index for {country} is {education_index:.4f}.')
print(f'GNI index for {country} is {gni_index:.4f}.')
print(f'HDI for {country} is {hdi_index:.3f}.')
print(f'HDI for {country} is high: {0.7<=hdi_index}.')
print(f'The worst index for {country} is {worst_index == education_index and "Education index" or  worst_index == health_index and "Life expectancy index" or worst_index == gni_index and "GNI index"}.')


