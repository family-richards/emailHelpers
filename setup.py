print("Going to install...")
from distutils.core import setup
print("Imported setup tool...")
setup(name="emailHelpers",
      version='0.1.0',
      packages=['emailHelpers'],
      author="Kendell R.",
      author_email="ejrejr@hotmail.com",
      license="MIT",
      description="Two classes to help with managing emails.",
      download_url="https://github.com/family-richards/Python-Email-Helpers",
      url="https://github.com/family-richards/Python-Email-Helpers")
print("Package installed!")
