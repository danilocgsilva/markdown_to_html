from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="markdown_to_html",
    version=VERSION,
    description="Converts markdown text to html",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="markdown html static",
    url="https://github.com/danilocgsilva/markdown_to_html",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["markdown_to_html"],
    entry_points={"console_scripts": ["mth=markdown_to_html.__main__:main"],},
    include_package_data=True
)

