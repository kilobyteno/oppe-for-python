import setuptools

# Add README.md as long description using open() and read()
with open('README.md') as f:
    readme = f.read()

# Add requirements.txt as install_requires using open() and readlines()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="oppe",
    version='0.0.1',
    description="A Python API Wrapper for Oppe",
    long_description=readme,
    long_description_content_type="text/markdown",
    project_urls={
        'Homepage': 'https://oppe.app',
        'Documentation': 'https://oppe.app',
        'Github': 'https://github.com/kilobyteno/oppe.py'
    },
    url="https://github.com/kilobyteno/oppe.py",
    author="Kilobyte AS",
    author_email="daniel@kilobyte.no",
    license="MIT",
    python_requires='>=3.6',
    packages=["oppe"],
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
