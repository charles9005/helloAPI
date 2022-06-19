import pytest
import os
from Common.handle_path import reports_dir

if __name__ == '__main__':
    pytest.main([f'--junitxml={reports_dir+"/results.xml"}'])
    os.system("allure generate Outputs/reports/temps  -o Outputs/reports/allures --clean")
