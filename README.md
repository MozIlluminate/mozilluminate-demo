MozIlluminate
[![Build Status](https://travis-ci.org/MozIlluminate/mozilluminate-demo.svg)](https://travis-ci.org/MozIlluminate/mozilluminate-demo)
============================

This repo is an example of MozIlluminate, our next-generation test case management system for Firefox OS QA

##How it works
Our goal is to enable user to write test cases in source code repos like [mozilla-b2g/gaia](https://github.com/mozilla-b2g/gaia). The test case will be in various formats, like text instructions, matrices (implemented), mindmaps or UI state diagrams. (Only plain text and tables are supported right now.) Every commit will trigger a automatic build on our [Travis CI Server](https://travis-ci.org/MozIlluminate/mozilluminate-demo/builds). The automatic build will transform and push the test cases s into [MozTrap](https://moztrap.mozilla.org/) (During the beta testing phase, the test cases will be pushed to [MozTrap-dev server](https://moztrap-dev.allizom.org/))

##Try it out
This repo replicates the folder structure for [mozilla-b2g/gaia](https://github.com/mozilla-b2g/gaia).

1. Clone this repo
2. Create/Edit test cases under `apps/\<app name\>/test/manual/test_\<something\>.md` ( 
 Check [`apps/example/test/manual/test_example.md`](https://github.com/MozIlluminate/mozilluminate-demo/blob/master/apps/example/test/manual/test_example.md) for example)
3. `git add`, `git commit` and `git push` (You are suggested to create a new branch)
4. Create a pull request to this repo. A automatic syntax check will be triggered on [Travis CI](https://travis-ci.org/MozIlluminate/mozilluminate-demo/pull_requests)
5. If the syntax check failed, go back to step 2 and fix your syntax.
6. Ask for peer review.
7. After your pull request is merged by the reviewer, go the the [Travis CI Server](https://travis-ci.org/MozIlluminate/mozilluminate-demo/builds) and see your modifications being pushed to MozTrap.
5. After the build finished. Go to [MozTrap-dev server](https://moztrap-dev.allizom.org/manage/cases/) to execute your test cases.

## Markdown Style Guide
You may want to read the [syntax guide](https://github.com/JohanLorenzo/markdown-testfile-to-json#syntax)

The test case body is in a simplified [cucumber](https://cucumber.io/) format. You specify the instruction and expected behavior usine `WHEN ... THEN ...` syntax (All capital letters). Please do not insert empty lines between steps.

##Travis CI configs
* Build pushes = ON 
* Build pull requests = ON
* Limit concurrent jobs = On
* Environment Variables
  * mz_user_name: MozTrap username
  * mz_api_key: MozTrap API key
  * Display value in build log = OFF

##Known Issues
* We will support WHEN/THEN syntax (instrucation/expectation) very soon!
* We will support table style test cases very soon.

##Contribute
* [Report bugs](https://github.com/MozIlluminate/mozilluminate-demo/issues/new)
* Join the discussion in IRC channel `#moztrap-enhancement`
* Join the discussion in the [project trello board](https://trello.com/b/4GQutOUA/git-moztrap)
