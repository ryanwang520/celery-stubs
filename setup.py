from setuptools import setup
import os

name = 'celery-stubs'
description = 'celery stubs'

install_instructions = """\
```
pip install celery-stubs
```
"""


def find_stub_files():
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith('.pyi'):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


setup(name='celery-stubs',
      version='0.1.2',
      description=description,
      long_description=install_instructions,
      long_description_content_type='text/markdown',
      author='Ryan Wang',
      author_email='hwwangwang@gmail.com',
      license='MIT License',
      url="https://github.com/ryanwang520/celery-stubs",
      install_requires=[
          'mypy>=0.950',
          'typing-extensions>=4.2.0'
      ],
      packages=['celery-stubs'],
      package_data={'celery-stubs': find_stub_files()},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3'
      ]
)
