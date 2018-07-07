import setuptools

setuptools.setup(
    name='backup',
    version='0.0.1',
    author='Jeff Moorhead',
    author_email='jeff.moorhead1@gmail.com',
    description='A package to backup files.',
    url='https://github.com/Jeff-Moorhead/Autobackup',
    packages=['backup'],
    classifiers=(
        'Programming Language :: Python :: 3',
    ),
    entry_points = {
        'console_scripts': ['backup=backup.backup_funcs:main']
        },
)
