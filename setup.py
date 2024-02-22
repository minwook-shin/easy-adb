import setuptools
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="easy-adb",
    version="0.0.3",
    description="Easy to use ADB commands in Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="minwook-shin",
    author_email="minwook0106@gmail.com",
    url="https://github.com/minwook-shin/easy-adb",
    project_urls={
        "Homepage": "https://github.com/minwook-shin/easy-adb",
        "Bug Reports": "https://github.com/minwook-shin/easy-adb/issues"
    },
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
    ],
    keywords=["python", "adb", "android"],
    license="LGPLv3",
    install_requires=[
        "requests==2.31.0",
        "adb-shell== 0.4.4"
    ],
    python_requires=">=3.9",
    include_package_data=True,
    packages=setuptools.find_packages(),
    package_data={"": ["*.txt"]},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'easy-adb = easy_adb.cli:main',
        ],
    }
)
