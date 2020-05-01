from setuptools import find_packages, setup
version = "1.0.1"
with open("PYPI.md", "r") as fh:
    long_description = fh.read()
setup(name="emailHelpers",
                 version=version,
                 author="Kendell R.",
                 author_email="kidscodingplace@gmail.com",
                 license="MIT",
                 description="emailHelpers is a wrapper for the smtplib and email packages.",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://family-richards.github.io/emailHelpers/",
                 packages=find_packages(),
                 classifiers=["Topic :: Communications :: Email", "Natural Language :: English", "Operating System :: OS Independent", "Programming Language :: Python :: 3 :: Only", "Topic :: Software Development :: Libraries :: Python Modules"],
                 python_requires='>=3.0')
