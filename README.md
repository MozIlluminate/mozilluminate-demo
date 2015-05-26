MozIlluminate
============================

This repo is an example of MozIlluminate, our next-generation test case management system for Firefox OS QA

##How it works
Our goal is to enable user to write test cases in source code repos like [mozilla-b2g/gaia](https://github.com/mozilla-b2g/gaia). The test case will be in various formats, like text instructions, matrices (implemented), mindmaps or UI state diagrams. Every commit will trigger a automatic build on our [Travis CI Server](https://travis-ci.org/MozIlluminate/mozilluminate-demo/builds). The automatic build will transform and push the tests into [MozTrap](https://moztrap.mozilla.org/)

##Try it out
This repo replicates the folder structure for [mozilla-b2g/gaia](https://github.com/mozilla-b2g/gaia).

1. Clone this repo
2. Edit the [apps/search/test/manual/rocketbar.md](https://github.com/MozIlluminate/mozilluminate-demo/blob/master/apps/search/test/manual/rocketbar.md) file. (This is the only one file that will work for now. We hard-coded the filename before automatic test file discovery is ready)
3. `git add`, `git commit` and `git push` as usual. (You may want to try creating a PR, too.)
4. After your `git push` (or PR merge) is successful, go the the [Travis CI Server](https://travis-ci.org/MozIlluminate/mozilluminate-demo/builds) and see your modifications being built.
5. After the build finished. Go to [MozTrap-dev server](https://moztrap-dev.allizom.org/manage/cases/) to see if your test case is successfully added/updated. (We use the dev site for demostration purpose)

##Known Issues
* Hard-coded filename, only `rocketbar.md` will work
* Does not support Johan's parser yet. (i.e. No tags and suites)
* We should update only the updated cases to minimize the network traffic. The current implementation is not fine-grain enough

##Contribute
* [Report bugs](https://github.com/MozIlluminate/mozilluminate-demo/issues/new)
* Join the discussion in IRC `#moztrap-enhancement`
* Join the discussion in the [project trello board](https://trello.com/b/4GQutOUA/git-moztrap)
