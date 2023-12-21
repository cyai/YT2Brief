import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="yt2brief",
    version="0.0.1",
    author="Vardhaman Kalloli",
    author_email="vardhamankalloli722@gmail.com",
    description=(
        "Transcribe and summarize YouTube videos using Langchain with the power of LLMs."
        "Store your summaries in Notion."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyai/YT2Brief",
    project_urls={
        "Bug Tracker": "https://github.com/cyai/YT2Brief/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "click"],  # Add click to the dependencies
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "yt2brief = yt2brief.cli:main",
            "yt2brief-setup = yt2brief.config_keys:setup",  # Include the setup script entry point
        ]
    },
)
