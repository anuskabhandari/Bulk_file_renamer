from setuptools import setup, find_packages

setup(
    name="bulk_renamer-anuska",
    version="0.1.0",
    author="Anuska Bhandari",
    author_email="bhandarirekha652@gmail.com",
    description="Python package to automatically organize files by type",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anuskabhandari/Bulk_file_renamer",  # add GitHub link later
    packages=find_packages(),  # automatically finds your package folder
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)