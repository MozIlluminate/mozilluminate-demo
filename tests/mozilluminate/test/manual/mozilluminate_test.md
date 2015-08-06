# MozIlluminate 

## mozilluminate.git_to_moztrap.test_case_CRUD
WHEN Create a new case within a new suite
THEN It should happen in MozTrap, check title, description, suite, tag, status

WHEN Add a new case to the existing suite (use different status)
THEN It should happen in MozTrap, check title, description, suite, tag, status

WHEN Create new step 
THEN It should happen in MozTrap

WHEN Update existing step 
THEN It should happen in MozTrap

WHEN Delete a step
THEN It should happen in MozTrap

## mozilluminate.git_to_moztrap.test_case_CRUD
WHEN Update a suite name 
THEN A new suite should be created with all cases moved to it, old suite should be deleted

WHEN Delete a suite
THEN The case should be deleted from MozTrap

## mozilluminate.git_to_moztrap.new_branch
WHEN Create a new branch
THEN A new set of cases should be created with the new product version

## mozilluminate.git_to_moztrap.check_branch
WHEN Create two cases in two different branches
THEN The two cases should be added under different productversion

## mozilluminate.git_to_moztrap.PR_linter
WHEN Create a malformed case, then create a PR
THEN The PR should be blocked, showing a user-friendly linter error

## mozilluminate.git_to_moztrap.diffing
WHEN Test the following:
* add new file
  * one suite
  * multiple suite
* modifiy existing file
  * add case to existing suite
  * modify case in existing suite
  * remove case from existing suite
  * add new suite 
  * modify existing suite name (??)
  * remove suite
* remove file

## End to end (no delete)
WHEN Open a new suite A and new case X, commit
THEN Case X added and is the the new suite A

WHEN Edit the instruction in old case X, commit 
THEN Case X updated

WHEN Create a new suite B, move the case X to the new suite B, delete the old suite A, commit
THEN Case moved to new suite B, old suite A is deleted

WHEN Move the case X back to the old suite A, add a new case Y to suite B, commit
THEN Case X moved to suite A, case Y is created and is in suite B

WHEN Delete case Y and suite B, commit
THEN Case Y and Suite B deleted
