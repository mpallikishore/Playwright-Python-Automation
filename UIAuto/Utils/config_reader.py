"""
We can write utilities functions.
Env: Testing -> Lower env - >Staging, QA, Milestone -> Production

prod: https://automationexercise.com/
stag: https://staging.automationexercise.com/
qa: https://qa.automationexercise.com/
milestone: https://milestone.automationexercise.com/

"""
import json
from pathlib import Path


def get_config():
    config_path = Path(r"C:\Users\motup\PycharmProjects\PythonProject\Auomation excercise with playwright\UIAuto\Config\qa_env.json")

    with open(config_path, "r") as file:
        return json.load(file)