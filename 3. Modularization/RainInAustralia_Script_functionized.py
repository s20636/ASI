import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle


# Rain in Australia https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package
# Przewidujemy czy jutro będzie padać - RainTomorrow

def read_data():
    df = pd.read_csv("data/weatherAUS.csv")
    df.Date = df.Date.astype(np.datetime64)
    df.set_index('Date', inplace=True)  # Wczytuje dane do pandas i ustawiam datę jako indeks
    return df


def clean_data(df):
    location_df = df.query(
        "Location == 'Darwin'")  # Wybieram tylko miasto Darwin z całego datasetu, żeby szybciej się liczyło
    location_df = location_df.drop(columns='Location')  # Wszędzie jest lokacja darwin, więc wyrzucam tą kolumnę
    location_df = location_df.dropna(
        subset=['RainTomorrow'])  # Wyrzucza wiersze z brakującą wartością zmiennej objaśnianej
    location_df = location_df.replace({"No": False, "Yes": True}).astype(
        {'RainToday': bool, 'RainTomorrow': bool})  # Zmienia typ na bool
    location_df = location_df.ffill()  # Uzupełniam brakujące dane za pomocą danych z poprzedniego dnia
    location_df = pd.get_dummies(
        data=location_df)  # One hot encoding - czyli zamieniam dane kategoryczne na zera i jedynki
    return location_df


def train_test(df):
    X = df.drop(columns="RainTomorrow")
    y = df.RainTomorrow
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101, stratify=y)
    return X_train, X_test, y_train, y_test


def scale_data(x_train, x_test):
    # Skalowanie danych - zamienia wartości liczbowe na takie ze średnią w 0 i odchyleniem standardowym 1
    scaler = StandardScaler()
    scaled_X_train = scaler.fit_transform(x_train)
    scaled_X_test = scaler.transform(x_test)
    return scaled_X_train, scaled_X_test, scaler


def train_model(x_train, x_test, y_train, y_test, model_type='log'):
    """
    :param model_type: either 'log' or 'forest'
    :return: trained sklearn model
    """
    model = None
    if model_type == 'log':
        model = LogisticRegression(random_state=101)
        model.fit(x_train, y_train)
    elif model_type == 'forest':
        model = RandomForestClassifier(random_state=101, max_depth=6)
        model.fit(x_train, y_train)
    return model

def evaluate_model(model, x_test, y_test):
    y_pred = model.predict(x_test)
    print(classification_report(y_test, y_pred))

def save_model(model, scaler):
    pickle.dump(model, open('model/model.sav', 'wb'))
    pickle.dump(scaler, open('model/scaler.sav', 'wb'))
    print('...Model and scaler saved...')


def main():
    df = read_data()
    df = clean_data(df)
    X_train, X_test, y_train, y_test = train_test(df)
    X_train, X_test, scaler = scale_data(X_train, X_test)
    model = train_model(X_train, X_test, y_train, y_test)
    evaluate_model(model, X_test, y_test)
    save_model(model, scaler)

main()
