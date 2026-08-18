from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements=f.read().splitlines()

setup(
    name="medical-chatbot",
    version="0.1",
    author="Vardhan ",
    packages=find_packages(),
    install_requires=requirements
)