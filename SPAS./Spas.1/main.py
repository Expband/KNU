import pandas as pn
import matplotlib.pyplot as plp

exported_Data = pn.read_csv('/Users/macbook/Desktop/КНУ/SPAS/СПАС1/Spas1.csv')
print(exported_Data)
print('______________________')

sorted_Data= exported_Data.groupby(['City']).mean()
sorted_Data.sort_values(['Price'])
sorted_Data = sorted_Data.drop(columns='Sqeuare')
print(sorted_Data)

plt= plp.plot(sorted_Data)
plp.show()

sorted_Data.to_csv('Spas1_mod.csv')
sorted_Data.to_excel('Spas1_mod.xlsx')
sorted_Data.to_html('Spas1_mod.html')