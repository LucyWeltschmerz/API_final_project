import json

import requests
from pytest import fixture
from config import Config


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="base_url", help="Environment to run tests against")


@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@fixture(scope="session")
def authentication(env):
    login_info = Config(env)
    login_info_dict = login_info.login_params
    access_token_text = requests.post('https://fakestoreapi.com/auth/login', login_info_dict).text
    access_token_json = json.loads(access_token_text)

    return access_token_json['token']


@fixture(scope="session")
def app_config(env, authentication):
    conf = Config(env)
    conf.token = authentication
    return conf
