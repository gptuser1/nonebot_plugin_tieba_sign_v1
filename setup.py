import setuptools
with open("README.md", "r",encoding="utf-8",errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot_plugin_tieba_sign_v1",
    version="0.0.1",
    author="gptuser1",
    author_email="gpt.user1@outlook.com",
    keywords=["pip", "nonebot2", "nonebot", "tieba", "nonebot_plugin"],
    description="""每日贴吧自动签到。""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gptuser1/nonebot_plugin_tieba_sign_v1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=[
        "nonebot2 >= 2.0.0b1",
        "nonebot-adapter-onebot >= 2.0.0b1",
        "requests >= 2.23.1"
    ]
)
