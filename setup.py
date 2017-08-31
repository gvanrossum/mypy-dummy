from setuptools import setup
setup(name='mypy',
      version='0.5.0',
      description="Dummy to remind people to switch to 'pip install mypy'",
      author="Gudo van Rossum",
      author_email='guido@python.org',
      license="MIT License",
      packages=['mypy'],
      entry_points={'console_scripts': ['mypy=mypy.__main__:console_entry']},
      )