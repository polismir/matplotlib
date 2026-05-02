import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
tasks = [3, 5, 4, 6, 7, 8, 6]

plt.plot(days, tasks, marker="o")

plt.title("Решённые задачи за неделю")
plt.xlabel("День")
plt.ylabel("Количество задач")
plt.grid()

plt.show()
# Больше всего задач было решено в шестой день.
