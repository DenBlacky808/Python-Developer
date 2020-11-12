fruits_1 = ['apples', 'pears', 'bananas', 'orange', 'lime']
fruits_2 = ['pears', 'tangerines', 'dragonfruit', 'pomelo', 'lime']

result = [fruit for fruit in fruits_1 if fruit in fruits_2]

print(result)
