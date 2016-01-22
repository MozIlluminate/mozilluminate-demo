MozIlluminate [![Build Status](https://travis-ci.org/MozIlluminate/mozilluminate-demo.svg)](https://travis-ci.org/MozIlluminate/mozilluminate-demo) 
============================

This repo is an example of MozIlluminate, our next-generation test case management system for Firefox OS QA

#What is MozIlluminate?
MozIlluminate allows you to write test cases in Google spreadsheet, and automatically check-in to GitHub, then automatically sync to MozTrap. So you get the best of both worlds, namely:
* Easy to read/edit/search with Google spreadsheet
* Version control with GitHub
* Test execution and reporting from MozTrap

#Prerequisite
* Use Linux or Mac OSX
* Install python and pip
* `sudo pip install oauth2client gspread`
  * If the installation failedon OSX due to the `six` package deprecation, run the command with  flag `--ignore-installed six`

#Usage 

1. Write your test cases in Google Spreadsheet ([example](https://docs.google.com/spreadsheets/d/10R1v-Vt5RZSLt-kw12zPL9dS-1npVFfKvB5OjG-g86k/edit#gid=491677371))
2. Clone this repository
3. Ask the admin to give you commit permission to this repository
3. Ask the admin to give you a credential JSON file, put it in the root directory of this repository
4. Add the link of the spreadsheet to `testcases_locations.txt`
5. Share the spreadsheet with this robot user: `ci-458@mozilluminate-1160.iam.gserviceaccount.com`
6. Edit the spreadsheet as you like
7. When you are done editing, run the `commit.sh` script, you'll be prompted to type a commit message, your github username and password
8. Once the script finished without error, Go to https://travis-ci.org/MozIlluminate/mozilluminate-demo/builds to see the test cases being synced to MozTrap-dev
9. Go to https://moztrap-dev.allizom.org/manage/cases/ to see your new test cases.

# How it works
* When you run `commit.sh`, the script downloads the google spreadsheet and transform it into a local json file
* Then the `commit.sh` script does `git add`, `git commit` and `git push`
* Travis CI server detects the push, and run the `.travis.yml` file
* The `.travis.yml` file triggers the `tests/MozIlluminate/sync.py`
* `tests/MozIlluminate/sync.py` checks for the diff between HEAD and HEAD~1 and push the difference to MozTrap throught its REST API

# Admins
* Shing Lyu (slyu@mozilla.com)

# Known Issues
* Tags don't work write now, blocked by https://github.com/mozilla/moztrap/pull/101
* Product Version is hard-coded to v2.5.
* Only supports one suite per test case (the spreadsheet name).
* Environments are not handled
* All test case steps goes into the first step on MozTrap, need to define a test step format.
