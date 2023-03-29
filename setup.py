from setuptools import setup, find_packages

setup(
    name="chat-gpt-assistant",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pyttsx3",
        "SpeechRecognition",
        "openai",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "assistant=scripts.assistant:main"
        ]
    },
    author="Antônio Pedro Rodrigues Santos",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
