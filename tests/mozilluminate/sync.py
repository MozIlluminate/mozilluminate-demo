import moztrap_integration.moztrapcli.mtapi as mtapi
import os
import subprocess

#TODO: eliminate this tmp file
tmpfile="tmp.json"
script_dir = os.path.dirname(os.path.realpath(__file__))

#FIXME: hardcoded feature file name
testcase_files = [script_dir + "/../../apps/*/test/manual/*test.md"]

cmd = "%s %s > %s" % (script_dir + '/../../node_modules/.bin/markdown-testfile-to-json',
                      ' '.join(testcase_files),
                      tmpfile)
parser_error_code = subprocess.call(cmd, shell=True)

if parser_error_code != 0:
    exit(parser_error_code)

#TODO: detect for changed/added/delete case only and ignore the rest

if os.getenv("TRAVIS_PULL_REQUEST") == "false":
    mtapi.mtorigin = "https://moztrap-dev.allizom.org"
    #The mz_user_name and mz_api_key is set in Travis CI
    mtapi.load_json_into_moztrap(tmpfile, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})
