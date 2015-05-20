import subprocess
import moztrap_integration.moztrapcli.mtapi as mtapi
import os

#TODO: eliminate this tmp file
tmpfile="tmp.txt"
script_dir = os.path.dirname(os.path.realpath(__file__))

#FIXME: hardcoded feature file name
testcase_files = [script_dir + "/../../apps/search/test/manual/rocketbar.md"]

for testcase_file in testcase_files:
    cmd = "%s %s -r %s > %s" % (script_dir + '/moztrap_integration/cucumber-js/bin/cucumber.js', testcase_file,
                                script_dir + '/moztrap_integration/step_definitions/moztrap.steps.js', tmpfile)
    os.system(cmd)
#TODO: detect for changed/added/delete case only and ignore the rest

    mtapi.mtorigin = "https://moztrap-dev.allizom.org"
#The mz_user_name and mz_api_key is set in Travis CI
    mtapi.convert_mark_file_into_moztrap(tmpfile, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})
