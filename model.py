import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def load_model():
    df = pd.read_csv("data/students.csv", sep=";")

    # Убираем пробелы в названиях колонок
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace('"', '')
    df.columns = df.columns.str.replace("/", "_")
    df.columns = df.columns.str.replace(" ", "_")

    # Target
    target_col = [col for col in df.columns if "target" in col.lower()][0]

    # Берём только нужные признаки (как во frontend)
    features = [
        "Marital_status",
        "Application_mode",
        "Application_order",
        "Course",
        "Daytime_evening_attendance",
        "Previous_qualification",
        "Admission_grade",
        "Gender",
        "Age_at_enrollment",
        "Scholarship_holder"
]

    X = df[features]
    y = df[target_col]

    # Кодируем Target
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    # Обучаем модель
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y_encoded)

    return model, encoder