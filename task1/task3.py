import matplotlib.pyplot as plt

file_size = [10, 25, 50, 75, 100, 150, 200]
time_loading = [2, 5, 9, 14, 20, 31, 45]

plt.plot(file_size, time_loading, marker="o")

plt.xlabel("Размер файла, МБ")
plt.ylabel("Время загрузки, сек")
plt.grid()

plt.show()
# Время загрузки при увеличении размера файлы увеличивается
# Да, можно сказать, что зависимость похожа на линейный рост
