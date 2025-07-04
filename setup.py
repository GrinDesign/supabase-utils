from setuptools import setup, find_packages

setup(
    name="supabase_utils",
    version="0.1.0",
    description="Supabaseユーティリティ集",
    packages=find_packages(),
    install_requires=[
        "supabase",
        "python-dotenv"
    ],
)
