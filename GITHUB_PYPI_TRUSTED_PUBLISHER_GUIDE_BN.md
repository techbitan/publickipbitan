# publickipbitan - GitHub to PyPI Trusted Publisher Guide

Developer: Bitan Bhattachirjee  
Email: mr.bitanbhattachirjee@gmail.com

## PyPI form values

PyPI Project Name: publickipbitan  
Owner: techbitan  
Repository name: publickipbitan  
Workflow name: publish.yml  
Environment name: pypi

## GitHub repository

Create repository name:

publickipbitan

Upload all files from this folder into that repository.

## GitHub Environment

Repository Settings → Environments → New environment

Environment name:

pypi

## Publish

Go to GitHub repository → Actions → Publish Python Package to PyPI → Run workflow

Successful হলে PyPI project create হবে এবং user install করতে পারবে:

pip install publickipbitan
