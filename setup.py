from setuptools import find_packages, setup
version = "1.1.1"
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(name="emailHelpers",
                 version=version,
                 author="Kendell R.",
                 author_email="kidscodingplace@gmail.com",
                 license="MIT",
                 description="An easy way to integrate email into your projects.",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://family-richards.github.io/emailHelpers/",
                 packages=find_packages(),
                 classifiers=["Topic :: Communications :: Email", "Natural Language :: English", "Operating System :: OS Independent", "Programming Language :: Python :: 3 :: Only", "Topic :: Software Development :: Libraries :: Python Modules", "Development Status :: 5 - Production/Stable", "License :: OSI Approved :: MIT License"],
                 python_requires='>=3.0',
                 project_urls={
                     "Tracker": "https://github.com/family-richards/emailHelpers/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc",
                     "Source": "https://github.com/family-richards/emailHelpers/",
                     "CI": "https://github.com/family-richards/emailHelpers/actions",
                     "SayThanks!": "https://saythanks.io/to/kidscodingplace@gmail.com"
                 })
