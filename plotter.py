import matplotlib.pyplot as plt
import numpy as np

x_list = range(0, 24)
y1_list = [5.43, 5.29, 5.33, 5.33, 5.3, 5.05, 5.05, 5.05, 7.7, 7.98, 7.96, 7.98, 7.99, 7.99, 15.76, 24, 27.19, 28.06, 27.68, 23.68, 28.27, 27.27, 36.56, 36.55]
x_indexes = np.arange(len(x_list))

plt.title("USD to UAH exchange rate")
plt.xticks(x_indexes, ['2000', '2001', '2002', '2003', '2004', '2005',
                      '2006', '2007', '2008', '2009', '2010',
                      '2011', '2012', '2013', '2014', '2015',
                      '2016', '2017', '2018', '2019', '2020',
                      '2021', '2022', '2023'])
plt.xlabel("Years 2000 - 2023")
plt.ylabel("Rate")
plt.bar(x_list, y1_list)
# plt.plot(x_list, y1_list, marker='.')

plt.show()
