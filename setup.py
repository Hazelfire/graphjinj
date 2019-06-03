from setuptools import setup, find_packages

setup(
    name="graphjinj",
    version="0.1",
    py_modules=find_packages(),
    install_requires=["jinja2", "requests"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
