from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyami_asterisk',
    version='1.0.0',
    description='pyami_asterisk is a library based on python’s AsyncIO to play with Asterisk Manager Interface (AMI)',
    author='Denis Streltsov',
    author_email='dsv.streltsov@gmail.com',
    url='https://github.com/streltsovdenis/pyami_asterisk.git',
    keywords=["AMI", "Asterisk", "asyncio", "python"],
    install_requires=['pytest', 'pytest-asyncio', 'pyyaml'],
    license='MIT license',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Communications :: Telephony',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)