import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(name="emailHelpers-KTibow",
      version='1.0',
      packages=['emailHelpers'],
      author="Kendell R.",
      author_email="kidscodingplace@gmail.com",
      license="MIT",
      description="Two classes to help with managing emails.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      download_url="https://github.com/family-richards/Python-Email-Helpers",
      url="https://github.com/family-richards/Python-Email-Helpers",
      packages=setuptools.find_packages(),
      python_requires='>=3.0')
