from setuptools import setup

setup(
    name='tempmail_sdk',
    version='1.0',
    description='Python SDK for mail.tm and mail.gw',
    url="https://github.com/flafkus/mail_sdk",  # Update with your repo URL
    author="flafkus",  # Update with your name
    author_email="122836545+flafkus@users.noreply.github.com",  # Update with your email
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ],
    keywords="API sdk tempmail mail.tm mail.gw",
    install_requires=["requests"],
    packages=["mail_gw", "mail_tm"],
    project_urls={
        "Bug Reports": "https://github.com/flafkus/mail_sdk/issues",
        "Source": "https://github.com/flafkus/mail_sdk",
    },
)
