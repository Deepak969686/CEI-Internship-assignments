# CEI-Internship-assignments
# 📌Week-1 Assignment Complete

# 📌Week-2 Assignment:
✔ Data Preprocessing  
✔ Exploratory Data Analysis  
✔ Feature Engineering  
✔ Regression Modeling  
✔ Linear Regression  
✔ Ridge Regression  
✔ Lasso Regression  
✔ Evaluation Metrics  
✔ Cross Validation  
✔ Hyperparameter Tuning  
✔ Time Series Analysis  
✔ Forecasting  

# 📌 Week-3 Assignment Classification, Ensemble Learning & Clustering:
# 🌍 Country Development Intelligence System using Machine Learning

## 📖 Project Overview

The Country Development Intelligence System is an end-to-end Machine Learning project designed to analyze socio-economic indicators of countries and identify their development status.

The project combines **unsupervised clustering** and **supervised classification** techniques to discover hidden country segments and predict development categories.

The system uses clustering algorithms to generate meaningful country groups and ensemble learning models to classify development patterns with optimized performance.

---

## 🎯 Objective

The main objectives of this project are:

- Analyze global socio-economic indicators through Exploratory Data Analysis (EDA)
- Segment countries into development groups using clustering algorithms
- Build classification models to predict country categories
- Optimize model performance using hyperparameter tuning
- Identify key factors influencing country development using feature importance analysis

---

## 📂 Dataset

Dataset Used:

**Country-data.csv**

The dataset contains various economic and health indicators for different countries.

### Features:

| Feature | Description |
|---|---|
| country | Name of country |
| child_mort | Child mortality rate |
| exports | Export percentage |
| health | Healthcare spending |
| imports | Import percentage |
| income | Average income |
| inflation | Inflation rate |
| life_expec | Life expectancy |
| total_fer | Fertility rate |
| gdpp | GDP per capita |

---

# 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Kaggle Notebook

---

# 🔍 Project Workflow


## 1. Data Understanding

Performed initial analysis:

- Dataset shape
- Feature information
- Statistical summary
- Data types inspection


---

## 2. Data Quality Check

Checked:

✔ Missing values  
✔ Duplicate records  
✔ Unique values  


---

## 3. Exploratory Data Analysis (EDA)

Performed:

### Feature Distribution Analysis

Analyzed distribution patterns of:

- GDP
- Income
- Healthcare
- Life expectancy
- Mortality rates


### Outlier Analysis

Detected extreme economic differences among countries.


### Correlation Analysis

Identified relationships between socio-economic factors.


---

# ⚙️ Data Preprocessing

Steps performed:

### Feature Selection

Removed non-numeric identifier:

# 📌Week-4 Assignment:

# 📘 CIFAR-10 Image Classification: ANN vs CNN

## 📌 Project Overview

This project demonstrates image classification on the CIFAR-10 dataset using Deep Learning models.

The main goal is to understand and compare:

- Artificial Neural Network (ANN)
- Convolutional Neural Network (CNN)

The project shows how model architecture and training strategies affect performance.

---

## 🎯 Objectives

- Understand the complete image classification pipeline
- Build an ANN model for image classification
- Build a CNN model for image classification
- Compare model accuracy and loss
- Analyze why CNN performs better for image tasks
- Improve model performance using training techniques

---

## 📂 Dataset: CIFAR-10

CIFAR-10 contains:

- 60,000 color images
- Image size: 32 × 32 × 3
- 50,000 training images
- 10,000 testing images
- 10 different classes

### Classes:

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Matplotlib

---

## 🧹 Data Preprocessing

Performed preprocessing steps:

- Loaded CIFAR-10 dataset
- Visualized sample images
- Normalized pixel values:

```
0-255 → 0-1
```

- Flattened images for ANN:

```
32 × 32 × 3 → 3072 features
```

---

# 🧠 Artificial Neural Network (ANN)

ANN architecture:

- Dense Layer (1024 neurons)
- Dropout
- Dense Layer (512 neurons)
- Dropout
- Dense Layer (256 neurons)
- Output Layer (10 classes)

### Observation:

- ANN can classify images
- Increasing layers improves learning capacity
- Spatial image information is lost during flattening

---

# 🧠 Convolutional Neural Network (CNN)

CNN architecture:

- Conv2D (32 filters)
- Batch Normalization
- MaxPooling

- Conv2D (64 filters)
- Batch Normalization
- MaxPooling

- Conv2D (128 filters)

- Dense Layer
- Dropout
- Output Layer

### Advantages:

- Preserves spatial information
- Learns edges, shapes, and patterns
- Performs better than ANN for images

---

# 🚀 Training Improvements

Implemented techniques:

### ✅ Dropout
Reduces overfitting by randomly disabling neurons.

### ✅ Batch Normalization
Improves training stability and convergence.

### ✅ EarlyStopping
Stops training when validation loss stops improving.

Configuration:

```python
monitor="val_loss"
patience=3
restore_best_weights=True
```

### ✅ Data Augmentation

Applied transformations:

- Random horizontal flip
- Random rotation
- Random zoom

Improves model generalization.

---

# 📊 Model Comparison

Models compared:

| Model | Description |
|---|---|
| ANN | Fully connected neural network |
| CNN | Convolution based model |
| CNN + Augmentation | CNN with training improvements |

Metrics:

- Test Accuracy
- Validation Accuracy Curve
- Validation Loss Curve

---

# 📈 Results

Expected performance trend:

```
CNN + Augmentation > CNN > ANN
```

CNN achieves better results because convolution layers extract meaningful spatial features from images.

---

# 📚 Learning Outcomes

After completing this project:

- Understood image classification workflow
- Learned ANN limitations for images
- Learned CNN feature extraction
- Applied regularization techniques
- Improved generalization using augmentation

---

# ✅ Conclusion

- ANN works but ignores image structure.
- CNN extracts spatial features and performs significantly better.
- Batch Normalization and Dropout improve training stability.
- EarlyStopping prevents overfitting.
- Data Augmentation improves generalization.
- This project builds strong fundamentals for Computer Vision and Deep Learning.

