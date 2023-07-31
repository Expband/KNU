import math
import pandas as pd
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def distance_minkowski(point1, point2, p):
    """
    point1, point2 - координати двох точок у вигляді кортежів або списків
    p - параметр відстані Мінковського, повинен бути цілим числом
    """
    if len(point1) != len(point2):
        raise ValueError("Кількість координат в точках не співпадає")

    if p < 1:
        raise ValueError("Параметр p повинен бути не менше 1")

    sum_of_powers = sum([abs(point1[i] - point2[i]) ** p for i in range(len(point1))])
    distance = sum_of_powers ** (1 / p)

    return distance


def k_means(data, k, max_iterations=150):
    """
    Виконує кластеризацію методом k-середніх для заданої кількості кластерів k та даних data.
    max_iterations – максимальна кількість ітерацій алгоритму.
    """
    centroids = data.sample(k).values  # Ініціалізація центроїдів випадковими точками даних.
    for _ in range(max_iterations):
        # Створення порожніх списків кожного кластера.
        clusters = {i: [] for i in range(k)}
        # Ітерація з кожної точки даних.
        for point in data.values:
            # Обчислення відстані між точкою та кожним центроїдом.
            distances = [distance_minkowski(point, centroid, 2) for centroid in centroids]
            # Визначення індексу кластера з найменшою відстанню.
            cluster_index = np.argmin(distances)
            # Додавання крапки у відповідний кластер.
            clusters[cluster_index].append(point)

        # Обчислення нових центроїдів з урахуванням середніх значень точок у кожному кластері.
        new_centroids = [np.mean(clusters[i], axis=0) for i in range(k)]

        # Перевірка на рівність старих та нових центроїдів. Якщо центроїди не змінилися, вихід із циклу.
        if np.all([np.allclose(a, b, rtol=1e-5) for a, b in zip(centroids, new_centroids)]):
            break
        centroids = new_centroids
    return clusters


def cluster_purity(cluster_labels, ground_truth_labels):
    """
    Обчислює чистоту кластера, порівнюючи його мітки з істинними мітками ground_truth_labels.
    """
    label_count = {}
    for label in ground_truth_labels:
        if label in label_count:
            label_count[label] += 1
        else:
            label_count[label] = 1
    majority_count = max(label_count.values())
    purity = majority_count / len(ground_truth_labels)
    return purity, max(label_count, key=label_count.get)


# Завантаження даних та міток.
iris_data = pd.read_csv('iris.csv')
data = iris_data.drop(columns=['variety'])
labels = iris_data['variety']

# Виконання кластеризації для k=3.
k = 3
clusters = k_means(data, k)

# Виведення інформації про кластер
print("Number of instances in each cluster:")
for i, cluster in clusters.items():
    cluster_labels = []
    for point in data.values:
        for c in cluster:
            if np.array_equal(point, c):
                cluster_labels.append(
                    labels[data.index[data.apply(lambda x: np.array_equal(x, point), axis=1)].tolist()[0]])
                break
    purity, majority_label = cluster_purity(cluster_labels, labels)
    print(f"Cluster {i + 1}: {len(cluster)} instances, Majority label: {majority_label}, Purity: {purity:.2f}")

species_counts = iris_data['variety'].value_counts().sort_index()
print("\nKnown class distribution:")
for index, count in species_counts.items():
    print(f"{index}: {count} instances")

CustomColorMap = ListedColormap(['crimson', 'mediumblue', 'darkmagenta'])
fix, ax = plt.subplots(figsize=(8, 6))
plt.scatter(x=iris_data['sepal.length'], y=iris_data['petal.width'], s=150,
            c=iris_data['petal.width'].astype('category'),
            cmap=CustomColorMap)
ax.set_xlabel(r'x', fontsize=14)
ax.set_ylabel(r'y', fontsize=14)
plt.show()
