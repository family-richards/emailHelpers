import setuptools
version = "v0.3.0"
with open("PYPI.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "w") as fh:
    fh.write("\n".join(setuptools.find_packages()))
setuptools.setup(name="emailHelpers",
      version=version,
      author="Kendell R.",
      author_email="kidscodingplace@gmail.com",
      license="MIT",
      description="emailHelpers is a wrapper for the smtplib and email packages.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      download_url="https://github.com/family-richards/Python-Email-Helpers",
      url="https://github.com/family-richards/Python-Email-Helpers",
      packages=setuptools.find_packages(),
      python_requires='>=3.0')
