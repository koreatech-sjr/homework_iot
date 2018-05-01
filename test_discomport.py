temp = 30
humidity = 60

discomport = 1.8*temp - 0.55*( 1.0 - humidity*0.01 )*(1.8*temp-26.0)+32.0

print(discomport)
