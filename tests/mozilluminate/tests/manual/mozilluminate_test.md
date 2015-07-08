# MozIlluminate 

## mozilluminate.git_to_moztrap.create_and_update
WHEN Create a new case within a new suite
THEN It should happen in MozTrap, check title, description, suite, tag

WHEN Update the description of an existing case
THEN It should happen in MozTrap

WHEN Update the step of an existing case
THEN It should happen in MozTrap

WHEN Update the description of the suite
THEN It should happen in MozTrap


## mozilluminate.git_to_moztrap.change_suite
GIVEN the suite exists, and the case exists in the suite
WHEN Change the name of the suite
THEN The case should be moved to the new suite, old suite should be deleted

## mozilluminate.git_to_moztrap.new_branch
WHEN Create a new branch
THEN A new set of cases should be created with the new product version

## mozilluminate.git_to_moztrap.check_branch
WHEN Create two cases in two different branches
THEN The two cases should be added under different productversion

## mozilluminate.git_to_moztrap.PR_linter
WHEN Create a malformed case, then create a PR
THEN The PR should be blocked, showing a user-friendly linter error
