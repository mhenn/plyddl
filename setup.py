from setuptools import setup, find_packages

setup(name='plyddl',
      version='0.0.1',
      author='mike-henning',
      author_email='mikeianhenni93@gmail.com',
      url='https://github.com/mhenn/plyddl/',
      project_urls={
            'Homepage': 'https://github.com/mhenn/plyddl/',
            'Source': 'https://github.com/mhenn/plyddl/',
            'Tracker': 'https://github.com/mhenn/plyddl/issues',
      },
      description='A simple pddl parser supporting most basic pddl features and numeric fluents from pddl2.1',
      packages=find_packages(),
      python_requires='>=3.6',
      py_modules='plyddl',
      install_requires=['ply']
      )