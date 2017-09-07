from setuptools import setup
setup(name='mypy-lang',
      version='0.5.0',
      description="Dummy to remind people to switch to 'pip install mypy'",
      author="Guido van Rossum",
      author_email='guido@python.org',
      license="MIT License",
      packages=['mypy'],
      entry_points={'console_scripts': ['mypy=mypy.__main__:console_entry']},
      )
