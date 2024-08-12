import os


def pytest_terminal_summary():
    '''
    Merges coverage to a single xml for coverage gutters.
    '''
    venv = os.path.join(os.getcwd(), 'venv')
    if os.path.isdir(venv):
        os.system('venv/bin/python -m coverage xml')
    else:
        os.system('python -m coverage xml')
