from setuptools import find_packages,setup
hyphen_e='-e .'
def get_requirements(file_path):

    #this function returns a list of packages to be installed

    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Trishita',
    author_email='trishitadhara123@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)