import setuptools
version = "v1.0.0"
with open("PYPI.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(name="emailHelpers",
                 version=version,
                 author="Kendell R.",
                 author_email="kidscodingplace@gmail.com",
                 license="MIT",
                 description="emailHelpers is a wrapper for the smtplib and email packages.",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://family-richards.github.io/emailHelpers/",
                 packages=setuptools.find_packages(),
                 classifiers=["Topic :: Communications :: Email", "Natural Language :: English"],
                 python_requires='>=3.0')
