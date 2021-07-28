import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ConsulClient",
    version="0.1.2",
    author="Rodrigo Alejandro Loza Lucero",
    author_email="lozuwaucb@gmail.com",
    description="A library that abstracts consul rest api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lozuwa/ConsulClient",
    packages=setuptools.find_packages(),
    keywords=['consul', 'distributed', 'key', 'value'],
    install_requires=[
        'bleach==3.3.0',
        'certifi==2018.11.29',
        'chardet==3.0.4',
        'docutils==0.14',
        'setuptools==40.8.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

