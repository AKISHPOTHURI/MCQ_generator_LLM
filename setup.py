from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='akish pothuri',
    author_email='akishpothuri@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)