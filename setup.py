import sys
version = "v1.0.0"
with open("PYPI.md", "r") as fh:
    long_description = fh.read()
if sys.version_info.major == 3:
    try:
        from setuptools import find_packages, setup
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
                         classifiers=["Topic :: Communications :: Email", "Natural Language :: English", "Operating System :: OS Independent"],
                         python_requires='>=3.0')
    except Exception as e:
        from distutils.core import setup
        from pkgutil import walk_packages
        import emailHelpers
        def find_pcks(path, prefix):
            yield prefix
            prefix = prefix + "."
            for _, name, ispkg in walk_packages(path, prefix):
                if ispkg:
                    yield name
        pcks = list(find_pcks(emailHelpers.__path__, emailHelpers.__name__))
        setup(name="emailHelpers",
                         version=version,
                         author="Kendell R.",
                         author_email="kidscodingplace@gmail.com",
                         license="MIT",
                         description="emailHelpers is a wrapper for the smtplib and email packages.",
                         long_description=long_description,
                         long_description_content_type="text/markdown",
                         url="https://family-richards.github.io/emailHelpers/",
                         packages=pcks,
                         classifiers=["Topic :: Communications :: Email", "Natural Language :: English", "Operating System :: OS Independent"],
                         python_requires='>=2.7')
