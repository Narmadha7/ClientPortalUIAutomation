import pytest
import json

# Pytest -v -s --browser "chrome" --report_path "reports" --test_scenario "positive"

configData = {}
with open("nar.json") as f:
    configData = json.load(f)

# print(" ".join(["-m", f"{configData['marker']}", "--browser", f"{configData['browser']}"]))
print(" ".join(["-m",'"'+ " and ".join(configData["marker"])+'"', "--browser", f'"{configData['browser']}"']))
# pytest.main(["-m", f"{configData['marker']}", "--browser", f"{configData['browser']}"])
# pytest.main(["-m",'" "'+ " and ".join(configData["marker"])+ '" "', "--browser", f"{configData['browser']}"])

