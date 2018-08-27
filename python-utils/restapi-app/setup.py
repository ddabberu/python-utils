"""setuptools to package the application and dependencies"""
from setuptools import find_packages,setup
setup(
    name='app',
    version='1.0.0',
    description='flask restapi example',
    author='ddabberu',
    packages=find_packages(), #find packages in the codee and import
    include_package_data=True, #includes whatever it can find in manifests.in
    zip_safe=False,
    install_requires=[
        'flask',
    ]
)