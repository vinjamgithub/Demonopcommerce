pytest -s -v -m "sanity and regression" --html=Reports\report.html testcases/ --browser chrome

rem pytest -s -v -m "sanity or regression" --html=Reports\report.html testcases/ --browser chrome

rem pytest -s -v -m "sanity" --html=Reports\report.html testcases/ --browser chrome