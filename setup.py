from setuptools import setup

setup(
    name="git-jirate",
    version="0.0.1",
    description="Git extension to show commits by author grouped by day",
    author="Bartosz Rumiński",
    packages=["git_jirate"],
    entry_points={
        "console_scripts": [
            "git-jirate=git_jirate.__main__:main"
        ]
    },
    python_requires='>=3.6',
)