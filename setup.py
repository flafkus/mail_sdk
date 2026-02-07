from setuptools import setup, find_packages

setup(
    name='mail_sdk',
    version='1.0',
    description='Python SDK for mail.tm and mail.gw',
    install_requires=["requests"],
    packages=find_packages()
)
