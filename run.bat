venv\scripts\activate
pytest -s -v -m "sanity and regression" --html=Reports\report.html testcases/ --browser chrome

