import platform
import sys

from config import settings


def create_allure_environment_file():
    data = [f'{key}={value}' for key,value in settings.model_dump().items()]
    data.append(f'os_info={platform.system()}, {platform.release()}')
    data.append(f'python_version={sys.version}')
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w') as f:
        f.write('\n'.join(data))