from setuptools import setup, find_packages

setup(
    name="cointiger-sdk",
    version="0.1",
    keywords=("cointiger", "sdk"),
    description="sdk for cointiger exchange, containd rest api and websocket api",
    license="MIT Licence",

    url="https://github.com/jianglijie/cointiger-python.git",
    author="jianglijie",
    author_email="jianglj@jianglijie.net",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "requests",
        "websocket-client",
    ],
    zip_safe=False
)