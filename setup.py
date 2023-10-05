from setuptools import setup
REQUIRES = [
    'records',
    'structlog',
    'allure-pytest'
]



setup(
    name='orm_client',
    version='0.1',
    packages=['orm_client'],
    url='https://github.com/DiLysenk/restclient_dl',
    license='MIT',
    author='lysenkodmitry',
    author_email='-',
    install_requires=REQUIRES,
    description='orm_client ohh'
)
