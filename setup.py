import pathlib
import setuptools

setuptools.setup(
    name="pypi-test-package",
    version="0.0.1",
    description="A small example package",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="123.com",
    author="Author Name",
    author_email="author@example.com",
    license="MIT",
    project_urls={
        "Documentation": "",
        "Source": "",
        "Bug Tracker": "",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - Planning",
    ],
    python_requires=">=3.7,<3.12",
    install_requires=[
        "requests",
        "pandas>=2.0",
    ],
    extras_require={
        "excel": [
            "openpyxl>=3.0.7,<3.1.0",
        ],
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "pypi-test-package = src.cli:main",
        ]
    },
)
