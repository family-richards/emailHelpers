print("Going to install...")
from distutils.core import setup
print("Imported setup tool...")
setup(name="emailHelpers",
      version='1.0',
      packages=['emailHelpers'],
      author="Kendell R.",
      author_email="ejrejr@hotmail.com",
      url="https://github.com/family-richards/Python-Email-Helpers")
print("Package installed!")
