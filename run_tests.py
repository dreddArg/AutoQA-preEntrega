import pytest

# Pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_inventory.py"
]

# Seteo de argumentos para reports
pytest_args = test_files + ["--html=reports/report_tests.html","--self-contained-html","-v"]

pytest.main(pytest_args)