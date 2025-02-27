# GitHub User Activity

![Englsih](https://img.shields.io/badge/English-red?style=for-the-badge)
[![Russian](https://img.shields.io/badge/Русский-blue?style=for-the-badge)](./documents/README_RU.md)

## Description

This project is inspired by [roadmap.sh](https://roadmap.sh/projects/github-user-activity).

## Installation

> Note: Steps for installation are provided only for Windows OS.

1. Clone the repository:
    
    ```shell
    git clone https://github.com/IliaStarchevus/GitHubActivity.git
    ```

2. Install requirements:
    
    ```shell
    pip install -r requirements.txt
    ```

3. Add path to the `ghact.py` into your system environment variables.
   1. Press `Ctrl + R` and type `sysdm.cpl`.
   2. Press button `Additional` on the top and then `Environment Variables`.
   3. Add path to the `ghact.py` into the `Path` in user environment variables.
   4. Add `.PY` into `PATHEXT` in system variables.

4. Check the program can run:

    ```shell
    ghact -h
    ```