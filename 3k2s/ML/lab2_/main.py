import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
# Припускаємо, що ми вже завантажили дані у DataFrame
# Тут ми створимо приклад DataFrame, використовуючи вказані дані
data = pd.read_csv('df\\tested.csv')

df = pd.DataFrame(data)

# Розділення на тренувальну, валідаційну та тестову вибірки в пропорції 70/15/15
train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42)
validation_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

# Опис обробки NaN значень (для прикладу, ми заповнимо відсутні значення середнім для числових колонок)
# Вибір заповнення середнім значенням для числових колонок обумовлений бажанням зберегти загальну статистичну інформацію даних
# і не впливати на розподіл ознак. Для категорійних даних ми можемо використати найпоширенішу категорію або спеціальну мітку.
# У цьому прикладі, виберемо спеціальну мітку "Unknown" для категорійних даних та середнє для числових.

# Обробка відсутніх значень
for column in ['Age', 'Fare']:
    train_df[column] = train_df[column].fillna(train_df[column].mean())
    validation_df[column] = validation_df[column].fillna(train_df[column].mean())
    test_df[column] = test_df[column].fillna(train_df[column].mean())


train_df.fillna('Unknown', inplace=True)
validation_df.fillna('Unknown', inplace=True)
test_df.fillna('Unknown', inplace=True)

print(train_df.head(10))
# Нормалізація числових даних
numerical_features = ['Age', 'SibSp', 'Parch', 'Fare']
scaler = StandardScaler()

train_df[column] = train_df[column].fillna(train_df[column].mean())
validation_df[column] = validation_df[column].fillna(train_df[column].mean())
test_df[column] = test_df[column].fillna(train_df[column].mean())


train_df.head()

# Вибір числових ознак для тренування моделі
features = ['Age', 'SibSp', 'Parch', 'Fare']
X_train = train_df[features]
y_train = train_df['Survived']
X_validation = validation_df[features]
y_validation = validation_df['Survived']

# Побудова трьох дерев рішень з різною глибиною
depths = [2, 4, 6]
trees = []
accuracies_train = []
accuracies_validation = []

for depth in depths:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)
    trees.append(dt)
    accuracies_train.append(dt.score(X_train, y_train))
    accuracies_validation.append(dt.score(X_validation, y_validation))

# Візуалізація дерев рішень
plt.figure(figsize=(20, 10))
for i, tree in enumerate(trees):
    plt.subplot(1, 3, i+1)
    plot_tree(tree, feature_names=features, class_names=['Not Survived', 'Survived'], filled=True)
    plt.title(f'Decision Tree with depth={depths[i]}')
plt.tight_layout()
plt.show()

# Виведення точності для кожної глибини
for i, depth in enumerate(depths):
    print(f"Depth: {depth}, Train accuracy: {accuracies_train[i]:.2f}, Validation accuracy: {accuracies_validation[i]:.2f}")

# Перерахунок точності моделей без використання індексів з попереднього розрахунку
accuracies_train_corrected = [tree.score(X_train, y_train) for tree in trees]
accuracies_validation_corrected = [tree.score(X_validation, y_validation) for tree in trees]

# Виведення коректної точності для кожної глибини
for i, depth in enumerate(depths):
    print(f"Corrected Depth: {depth}, Train accuracy: {accuracies_train_corrected[i]:.2f}, Validation accuracy: {accuracies_validation_corrected[i]:.2f}")

# Додавання шуму до тренувальних даних
noise = np.random.uniform(-0.1, 0.1, X_train.shape)
X_train_noisy = X_train + noise

# Побудова трьох дерев рішень з різною глибиною на зашумлених даних
trees_noisy = []
accuracies_train_noisy = []
accuracies_validation_noisy = []

for depth in depths:
    dt_noisy = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt_noisy.fit(X_train_noisy, y_train)
    trees_noisy.append(dt_noisy)
    accuracies_train_noisy.append(dt_noisy.score(X_train_noisy, y_train))
    accuracies_validation_noisy.append(dt_noisy.score(X_validation, y_validation))

# Візуалізація дерев рішень на зашумлених даних
plt.figure(figsize=(20, 10))
for i, tree in enumerate(trees_noisy):
    plt.subplot(1, 3, i+1)
    plot_tree(tree, feature_names=features, class_names=['Not Survived', 'Survived'], filled=True)
    plt.title(f'Decision Tree with depth={depths[i]} (Noisy Data)')
plt.tight_layout()
plt.show()

# Виведення точності для кожної глибини на зашумлених даних
for i, depth in enumerate(depths):
    print(f"Noisy Data - Depth: {depth}, Train accuracy: {accuracies_train_noisy[i]:.2f}, Validation accuracy: {accuracies_validation_noisy[i]:.2f}")

# Обрахунок PCA на оригінальній тренувальній вибірці
pca = PCA(n_components=2)  # Використовуємо 2 компоненти для візуалізації
X_train_pca = pca.fit_transform(X_train)

# Обрахунок PCA на зашумленій тренувальній вибірці
pca_noisy = PCA(n_components=2)
X_train_noisy_pca = pca_noisy.fit_transform(X_train_noisy)

# Візуалізація PCA компонентів
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=y_train, cmap='viridis', edgecolor='k', s=20)
plt.title('PCA of Original Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.subplot(1, 2, 2)
plt.scatter(X_train_noisy_pca[:, 0], X_train_noisy_pca[:, 1], c=y_train, cmap='viridis', edgecolor='k', s=20)
plt.title('PCA of Noisy Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.tight_layout()
plt.show()

# Обрахунок PCA на зашумленій тренувальній вибірці для 95% variance
pca_95 = PCA(n_components=0.95)
X_train_noisy_pca_95 = pca_95.fit_transform(X_train_noisy)
X_train_noisy_reconstructed = pca_95.inverse_transform(X_train_noisy_pca_95)

# Візуалізація оригінальних, зашумлених і знешумлених даних
# Оскільки ми працюємо з багатовимірними даними, візуалізуємо лише перші дві компоненти
plt.figure(figsize=(20, 6))

plt.subplot(1, 3, 1)
plt.scatter(X_train.iloc[:, 0], X_train.iloc[:, 1], c=y_train, cmap='viridis', edgecolor='k', s=20)
plt.title('Original Data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.subplot(1, 3, 2)
plt.scatter(X_train_noisy.iloc[:, 0], X_train_noisy.iloc[:, 1], c=y_train, cmap='viridis', edgecolor='k', s=20)
plt.title('Noisy Data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.subplot(1, 3, 3)
plt.scatter(X_train_noisy_reconstructed[:, 0], X_train_noisy_reconstructed[:, 1], c=y_train, cmap='viridis', edgecolor='k', s=20)
plt.title('Denoised Data using PCA')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.tight_layout()
plt.show()

X_train_denoised = pd.DataFrame(X_train_noisy_reconstructed, columns=features)

trees_denoised = []
accuracies_train_denoised = []
accuracies_validation_denoised = []

for depth in depths:
    dt_denoised = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt_denoised.fit(X_train_denoised, y_train)
    trees_denoised.append(dt_denoised)
    accuracies_train_denoised.append(dt_denoised.score(X_train_denoised, y_train))
    accuracies_validation_denoised.append(dt_denoised.score(X_validation, y_validation))

plt.figure(figsize=(20, 10))
for i, tree in enumerate(trees_denoised):
    plt.subplot(1, 3, i+1)
    plot_tree(tree, feature_names=features, class_names=['Not Survived', 'Survived'], filled=True)
    plt.title(f'Decision Tree (Denoised Data) with depth={depths[i]}')
plt.tight_layout()
plt.show()

for i, depth in enumerate(depths):
    print(f"Depth: {depth}, Noisy Data - Train accuracy: {accuracies_train_noisy[i]:.2f}, Validation accuracy: {accuracies_validation_noisy[i]:.2f}")
    print(f"Depth: {depth}, Denoised Data - Train accuracy: {accuracies_train_denoised[i]:.2f}, Validation accuracy: {accuracies_validation_denoised[i]:.2f}")

