# ============================================
# Python
# ============================================

# </> Bash
# Command                     	Purpose
# $ python --version            Check Python Version
# or
# $ python3 --version

# ============================================
# VS Code Basics
# ============================================
# Shortcut	            Action

# Ctrl + `	           Open Terminal
# Ctrl + S	           Save File
# Ctrl + C	           Stop Running Program
# Ctrl + /	           Comment/Uncomment Code
# Ctrl + Shift + P	   Command Palette
# F5	                   Run with Debugger
# Ctrl + F	           Find Text

# ============================================
# Terminal Basics
# ============================================
# Command                     Purpose                  Example

# pwd                       Show Current Folder        C:\Users\Rifa\Python
# dir (Windows )            List Files
# ls (Linux/macOS)          List Files
# cd folder_name            Change Folder              cd Projects
# Go back one folder
# mkdir folder_name         Create Folder              cd ..
# cls (Windows)             Clear Terminal
# clear (Linux/macOS)       Clear Terminal

# ============================================
# PIP PACKAGE MANAGEMENT
# ============================================

# 1. WHAT IS PIP?
# Pip is the official package installer ("App Store") for Python.
# It downloads and installs external libraries built by the community.

# 2. CORE TERMINAL COMMANDS (Run these inside your terminal, not in Python)
# ---------------------------------------------------------------------
# Check Pip Version:
# $ pip --version

# Install a new package (e.g., 'requests' for web scraping):
# $ pip install requests

# List all packages installed in your active environment:
# $ pip list

# Uninstall an unwanted package:
# $ pip uninstall requests

# 3. VIRTUAL ENVIRONMENTS (.venv)
# Always keep your project dependencies isolated inside your local folder.
# Never install global packages to your base operating system!

# To activate your Linux/WSL virtual environment manually if it turns off:
# $ source .venv/bin/activate


# pip is Python's package manager.
# Its job is to:
# Download libraries
# Install libraries
# Update libraries
# Remove libraries

# A library is reusable Python code.
# pip is Python's package manager.
# Use pip install package_name to install packages.
# @Use pip list to see installed packages.
# Use pip uninstall package_name to remove a package.
# Verify package names and install only trusted libraries.

# Command                     	Purpose

# pip --version	                Check if pip is installed
# pip install requests	        Install a package
# pip install package==version   Install a specific version
# pip install --upgrade package  Update a package
# pip uninstall package	        Remove a package
# pip list	                    Show installed packages
# pip show package	            Show package information
# pip show requests              Show Information About a Library
##------Importing a Library--------
import requests

# ----------Built-in vs Third-party-----------
# Built-in Modules (No Installation Needed)
import os
import json
import math
import random
import socket
import hashlib

# Third-party Libraries (Install First)
# </> Bash
# $pip install requests
# </> Python
import requests

# Installing Securely
# ✔ Install only from PyPI.

# ✔ Check the package name carefully.

# ✔ Read the documentation.

# ✔ Keep packages updated.

# ✔ Don't install random packages from unknown websites.

# -----Libraries You'll Use in Cybersecurity----
# Library	            Purpose

# requests	        HTTP Requests
# scapy	            Packet Analysis
# python-nmap	           Run Nmap Scans
# paramiko	         SSH Automation
# colorama	        Colored Terminal Output
# beautifulsoup4	     HTML Parsing
# pandas	            Data Analysis

# 🛡 CYBERSECURITY EXAMPLE

# Suppose you're writing a web scanner.

# Instead of writing HTTP code yourself:

# pip install requests
# Now:

import requests

# response = requests.get("https://example.com")

# print(response.status_code)
# One library replaces hundreds of lines of networking code.

# WHAT HAPPENS BEHIND THE SCENES?
# You type
# ↓
# pip install requests
# ↓
# pip connects to PyPI
# ↓
# Downloads package
# ↓
# Installs package
# ↓
# Python can import it

# ============================================
# Virtual Environments (venv)
# ============================================
# Different projects may need different library versions.
# A virtual environment keeps each project's libraries separate.
# Think of it like having a separate toolbox for each project.

# --Create Virtual Environment--:
# </> Bash
# $ python -m venv venv
# This creates a folder named: venv/

# ---Activate (Windows)---:
# </> Bash
# $ venv\Scripts\activate
# ---Activate (Linux/macOS)---:
# </> Bash
# $ source venv/bin/activate

# ---Deactivate---:
# </> Bash
# $ deactivate

# ============================================
# Python Interpreter
# ============================================
# Open the interpreter
# </> Bash
# $ python
# Exit
exit()
# or
# </> Bash
# $ Ctrl + Z
# open NEPL
# </> Bash
# $ python3
# exit : exit() or ctrl + D
# to cancel a code : ctrl + C

# ============================================
# Git
# ============================================
# Git is a Version Control System (VCS).
# It helps you:
# Track changes
# Save project history
# Undo mistakes
# Work with other developers

# -----📁 CREATE A NEW GIT REPOSITORY--------

# Go to your project folder.
# </> Bash :cd my_project
# Initialize Git.
# </> Bash :git init

# Output: Initialized empty Git repository
# Now Git is tracking this folder.

# ------📂 CHECK PROJECT STATUS----------
# </> Bash :git status
# Shows:
# New files
# Modified files
# Files ready to save

# -----------➕ ADD FILES-------------
# Add one file.
# </> Bash :git add main.py
# Add everything.
# </> Bash :git add .

# --------💾 SAVE A VERSION (COMMIT)---------
# </> Bash :git commit -m "Created first scanner"
# A commit is like taking a snapshot of your project.
# History updated

# -------📜 VIEW HISTORY---------
# </> Bash :git log
# Shows every commit.

# Example : Added scanner
#          Fixed bug
#          Updated README

# -------✏️ SEE CHANGES-----------
# </> Bash :git diff
# Shows what changed since the last commit.

# --------🔄 RESTORE A FILE---------------
# Discard changes.
# </> Bash :git restore main.py
# The file returns to its last committed version.

# ----------❌ REMOVE A FILE-----------
# </> Bash :git rm notes.txt
# Removes the file and stages the deletion.

# -------🌐 CONNECT TO GITHUB-----------

# Add your GitHub repository.

# </> Bash :git remote add origin https://github.com/username/project.git

# Now your local project knows where the online repository is.

# ---------⬆️ UPLOAD TO GITHUB------------

# First upload.
# </> Bash :git push -u origin main
# Later uploads.
# </> Bash :git push

# ---------⬇️ DOWNLOAD A PROJECT--------------
# </> Bash :git clone https://github.com/username/project.git

# Git downloads the repository to your computer.

# --------📥 GET LATEST CHANGES------------
# git pull

# Downloads and merges updates from GitHub.

# ------------🌱 CREATE A NEW BRANCH--------------
# </> Bash :git branch new-feature
# A branch lets you work on new features without affecting the main project.

# ------------🔀 SWITCH BRANCHES--------------
# </> Bash :git switch new-feature

# Or (older command)

# Bash :git checkout new-feature
# -----------📋 VIEW BRANCHES------------
# </> Bash :git branch
# Current branch has a *.

# Example : * main
#          new-feature

# --------🛡 CYBERSECURITY EXAMPLE------------

# Project:
# Port Scanner
# Workflow:
# Create scanner
# ↓
# $ git add .
# ↓
# $ git commit -m "Initial scanner"
# ↓
# Add banner grabbing
# ↓
# $ git add .
# ↓
# $ git commit -m "Added banner grabbing"
# ↓
# Bug appears
# ↓
# Return to previous version

# Git keeps every step of your progress.

# ============================================
# Git Repository
# ============================================

# Create a Repository
# Click: New Repository

# Example: python-notes or cybersecurity-notes

# Choose:

# Public (recommended for learning)
# OR Private (only you can see it)

# Click:
# Create Repository
# 🛠️ STEP 3 — Open Your Project
# Example folder:

# Python/
# │
# ├── 00 - Environment & Tools.md
# ├── 01 - Variables.md
# ├── 02 - If Statements.md
# ├── scripts/
# └── README.md

# Open the terminal inside that folder.

# 🛠️ STEP 4 — Initialize Git
# $ git init
# 🛠️ STEP 5 — Add Files
# $ git add .

# This stages every file in the current folder.

# 🛠️ STEP 6 — Create Your First Commit
# $ git commit -m "Initial commit"

# 🛠️ STEP 7 — Connect to GitHub

# Copy your repository URL.
# Example:https://github.com/yourusername/python-notes.git

# Connect it:
# $ git remote add origin https://github.com/yourusername/python-notes.git

# 🛠️ STEP 8 — Upload Everything
# $ git branch -M main
# $ git push -u origin main

# After this, all your notes are backed up on GitHub.

# 🔄 EVERYDAY WORKFLOW

# Whenever you finish studying:

# $ git status
# ↓
# $ git add .
# ↓
# $ git commit -m "Added notes on File Handling"
# ↓
# $ git push

# This uploads your latest work to GitHub.

# 🛡️ SECURITY TIPS

# Push code and notes.
# Never push:

# Passwords
# API keys
# Private SSH keys
# .env files containing secrets
# Personal information

# Use a .gitignore file to exclude files that shouldn't be uploaded.
# Example:
# venv/
# .env
# __pycache__/
# *.pyc

# One-time setup
# git init
# git remote add origin <repository-url>

# First upload
# git add .
# git commit -m "Initial commit"
# git branch -M main
# git push -u origin main

# Daily workflow
# git status
# git add .
# git commit -m "Describe what changed"
# git push
