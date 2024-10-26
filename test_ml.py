import pytest
import pickle
from train_model import data
from sklearn.ensemble import RandomForestClassifier


def test_one():
    """
    Test if the model pickle file loads correctly.
    """
    pickle_result = False
    try:
        with open("model/model.pkl", "rb") as f:
            pickle.load(f)
        pickle_result = True
    except:
        print("Error loading pickle file in test_ml.py")

    assert pickle_result == True


def test_two():
    """
    Verifying there are 15 columns in the loaded dataset.
    """
    column_count = 15
    assert len(data.columns) == column_count


def test_three():
    """
    Testing if the model is a RandomForestClassifier.
    """
    with open("model/model.pkl", "rb") as f:
        model = pickle.load(f)

    assert isinstance(model, RandomForestClassifier)
