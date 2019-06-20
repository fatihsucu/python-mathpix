from setuptools import setup

setup(
    name='python-mathpix',
    version='0.4',
    description='Python Mathpix Api Wrapper',
    url='https://github.com/fatihsucu/python-mathpix',
    author='Fatih Sucu',
    author_email='fatihsucu0@gmail.com',
    license='MIT',
    packages=['mathpix'],
    install_requires=[
        "requests"
    ],
    zip_safe=False
)
