import setuptools

setuptools.setup(
    name='django-celery-task-queue',
    version='2020.7.2',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
