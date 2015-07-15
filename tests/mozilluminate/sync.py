import subprocess
import moztrap_integration.moztrapcli.mtapi as mtapi
import os
import tempfile
from git import Repo
import json

#TODO: eliminate this tmp file
#tmpfile="tmp.txt"

def summarize_diff(before, after):
    added = []
    modified = []
    removed = []

    suite_pairs = map(None,
        sorted(before, key=lambda x: x['name']),
        sorted(after, key=lambda x: x['name'])
        )
    for suite_pair in suite_pairs:
        if suite_pair[0] is None:
            raise NotImplementedError
            #added suite
        elif suite_pair[1] is None:
            raise NotImplementedError
            #removed suite
        else:
            intersect_titles = list( # cases that are in both before and after, may be a modified or not modified case
                set(map(lambda x: x['id'], suite_pair[0]['testcases'])) &
                set(map(lambda x: x['id'], suite_pair[1]['testcases']))
            )
            adds = [ x for x in suite_pair[1]['testcases']
                        if x not in suite_pair[0]['testcases']
                            and x['id'] not in intersect_titles]
            removes = [ x for x in suite_pair[0]['testcases']
                          if x not in suite_pair[1]['testcases']
                                and x['id'] not in intersect_titles]
            modifies = [ x for x in suite_pair[1]['testcases']
                            if x not in suite_pair[0]['testcases']
                                and x['id'] in intersect_titles]
            if (len(adds) > 0):
                added.append({
                    'name': suite_pair[0]['name'],
                    'testcases': adds
                })
            if (len(removes) > 0):
                removed.append({
                    'name': suite_pair[0]['name'],
                    'testcases': removes
                })
            if (len(modifies) > 0):
                modified.append({
                    'name': suite_pair[0]['name'],
                    'testcases': modifies
                })

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

#repo = Repo('../../')
    repo = Repo('../../../../') #for debuggin

    updated_diffs = filter(lambda x: "apps" in x.b_path and "test/manual" in x.b_path, repo.commit('HEAD~1').diff('HEAD'))

#print(updated_diffs)

#for testcase_file in testcase_files:
    for diff in updated_diffs:
        if diff.new_file: #&& edit only
            raise NotImplementedError


#TODO: detect for changed/added/delete case only and ignore the rest

        elif diff.deleted_file:
            raise NotImplementedError
            #TODO
        elif diff.renamed:
            raise NotImplementedError
            #TODO
        else:

            #cmd = "%s %s -r %s > %s" % (script_dir + '/moztrap_integration/cucumber-js/bin/cucumber.js', testcase_file,
            #                            script_dir + '/moztrap_integration/step_definitions/moztrap.steps.js', tmpfile)
            # subprocesscheck_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False).
            #parsed_json_f = tempfile.NamedTemporaryFile()
            testcase_before = tempfile.NamedTemporaryFile()
            testcase_after = tempfile.NamedTemporaryFile()

            testcase_before.write(diff.a_blob.data_stream.read())
            testcase_before.flush()

            testcase_after.write(diff.b_blob.data_stream.read())
            testcase_after.flush()

            #cmd = "%s %s > %s" % (script_dir + '/moztrap_integration/markdown-testfile-to-json/cli.js', testcase_file,
            #                    parsed_json_f.name)
            #os.system(cmd)
            #print subprocess.check_output(['cat', testcase_before.name])
            before_json = json.loads(subprocess.check_output([script_dir + '/moztrap_integration/markdown-testfile-to-json/cli.js', testcase_before.name]))
            after_json = json.loads(subprocess.check_output([script_dir + '/moztrap_integration/markdown-testfile-to-json/cli.js', testcase_after.name]))

            pairs = map(None,
                sorted(before_json, key=lambda x: x['name']),
                sorted(after_json, key=lambda x: x['name'])
                )
            print "preparing paris"
            print pairs
            for pair in pairs:
                if pair[0] is None:
                    raise NotImplementedError
                    #added suite
                if pair[1] is None:
                    raise NotImplementedError
                    #removed suite

                #added = list(set(new) - set(old))
                #removed= list(set(old) - set(new))
                #for
            #print before_json

    parsed_json_f = tempfile.NamedTemporaryFile()

    mtapi.mtorigin = "https://moztrap-dev.allizom.org"
#The mz_user_name and mz_api_key is set in Travis CI
#mtapi.convert_mark_file_into_moztrap(tmpfile, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})
    mtapi.load_json_into_moztrap(parsed_json_f.name, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})

if __name__ == '__main__':
    main()
