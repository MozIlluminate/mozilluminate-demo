import subprocess
import moztrap_integration.moztrapcli.mtapi as mtapi
import os
import tempfile
from git import Repo
import json

#TODO: eliminate this tmp file
#tmpfile="tmp.txt"

def flatten(suites):
    flattened = []
    for suite in suites:
        for testcase in suite['testcases']:
            testcase['suites'] = [suite['name']]
            flattened.append(testcase)
    return flattened

def summarize_diff(before, after):
    added = []
    modified = []
    removed = []

#    suite_pairs = map(None,
#        sorted(before, key=lambda x: x['name']),
#        sorted(after, key=lambda x: x['name'])
#        )
#    for suite_pair in suite_pairs:
#    if suite_pair[0] is None:
#        raise NotImplementedError
#        #added suite
#    elif suite_pair[1] is None:
#        raise NotImplementedError
#        #removed suite
#    else:
    intersect_titles = list( # cases that are in both before and after, may be a modified or not modified case
        set(map(lambda x: x['id'], before)) &
        set(map(lambda x: x['id'], after))
    )
    added += [ x for x in after
                if x not in before
                    and x['id'] not in intersect_titles]
    removed += [ x for x in before
                    if x not in after
                        and x['id'] not in intersect_titles]
    modified += [ x for x in after
                    if x not in before
                        and x['id'] in intersect_titles]

    return (added, modified, removed)


        #added = list(set(new) - set(old))
        #removed= list(set(old) - set(new))
        #for
    #print before_json


def main():
    tmpfile="tmp.json"
    script_dir = os.path.dirname(os.path.realpath(__file__))

#FIXME: hardcoded feature file name
#testcase_files = [script_dir + "/../../apps/search/test/manual/rocketbar.md"]
#testcase_files = [script_dir + "/../../apps/sms/test/manual/README.md"]

    repo = Repo('../../')
   # repo = Repo('../../../../') #for debuggin

    updated_diffs = filter(lambda x: "apps" in x.b_path and "test/manual" in x.b_path, repo.commit('HEAD~1').diff('HEAD'))

#print(updated_diffs)

#for testcase_file in testcase_files:
    for diff in updated_diffs:
        #how to deteced diff type:
        #if diff.new_file: #&& edit only
        #elif diff.deleted_file:
        #elif diff.renamed:
        #else:

        testcase_before = tempfile.NamedTemporaryFile()
        testcase_after = tempfile.NamedTemporaryFile()

        try:
            testcase_before.write(diff.a_blob.data_stream.read())
        except AttributeError:
            testcase_before.write(json.dumps([]))
        try:
            testcase_after.write(diff.b_blob.data_stream.read())
        except AttributeError:
            testcase_before.write(json.dumps([]))

        testcase_before.flush()
        testcase_after.flush()

        #cmd = "%s %s > %s" % (script_dir + '/moztrap_integration/markdown-testfile-to-json/cli.js', testcase_file,
        #                    parsed_json_f.name)
        #os.system(cmd)
        #print subprocess.check_output(['cat', testcase_before.name])
        before_json += json.loads(subprocess.check_output([script_dir + '/moztrap_integration/markdown-testfile-to-json/cli.js', testcase_before.name]))
        after_json += json.loads(subprocess.check_output([script_dir + '/moztrap_integration/markdown-testfile-to-json/cli.js', testcase_after.name]))

        diff = summarize_diff(before_json, after_json)


    #parsed_json_f = tempfile.NamedTemporaryFile()

    mtapi.mtorigin = "https://moztrap-dev.allizom.org"
#The mz_user_name and mz_api_key is set in Travis CI
#mtapi.convert_mark_file_into_moztrap(tmpfile, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})
    #mtapi.load_json_into_moztrap(parsed_json_f.name, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})
    mtapi.sync_diff_to_moztrap(diff, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})

if __name__ == '__main__':
    main()
