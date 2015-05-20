import subprocess
import moztrap_integration.moztrapcli.mtapi as mtapi
import os

#TODO: eliminate this tmp file
tmpfile="tmp.txt"

#FIXME: hardcoded feature file name
cmd = "%s %s -r %s > %s" % ('./moztrap_integration/cucumber-js/bin/cucumber.js', 'fxos.rocketbar.feature',
                            './moztrap_integration/step_definitions/moztrap.steps.js', tmpfile)
os.system(cmd)
#TODO: detect for changed/added/delete case only and ignore the rest

#FIXME: hardcoded username/apikey
mtapi.mtorigin = "https://moztrap-dev.allizom.org"
mtapi.convert_mark_file_into_moztrap(tmpfile, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})

