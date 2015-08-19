import subprocess
import moztrap_integration.moztrapcli.mtapi as mtapi
import moztrap_integration.moztrapcli.orm as orm
import os
import tempfile
from git import Repo
import json
import re

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
    # TODO: we may want to output the part that has changed only, e.g. steps vs
    # case modifiers
    added = []
    tmp_modified = []
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
    tmp_modified += [ x for x in after
                    if x not in before
                        and x['id'] in intersect_titles]
    modified = []

    for aftermodifiedcase in tmp_modified:
        beforemodifiedcase = filter(lambda x: x['id'] == aftermodifiedcase['id'], before)[0]
        before_s = set(beforemodifiedcase['suites'])
        after_s = set(aftermodifiedcase['suites'])
        aftermodifiedcase['suites_added'] = list(after_s.difference(before_s))
        aftermodifiedcase['suites_removed'] = list(before_s.difference(after_s))
        modified.append(aftermodifiedcase)


    before_suites = set()
    after_suites = set()

    for case in before:
        before_suites = before_suites.union(case['suites'])
    for case in after:
        after_suites = after_suites.union(case['suites'])

    added_suites = list(after_suites.difference(before_suites))
    removed_suites = list(before_suites.difference(after_suites))
    existing_suites = list(before_suites.intersection(after_suites))

    #return (added, modified, removed, added_suites, removed_suites)
    return ({
        'case':{
            'added':added,
            'modified':modified,
            'removed':removed
        },
        'suite':{
            'added':added_suites,
            'existing':existing_suites,
            'removed':removed_suites,
        }
    })


        #added = list(set(new) - set(old))
        #removed= list(set(old) - set(new))
        #for
    #print before_json


def expand_table_if_exist(testcase_json):
    if 'variables' not in testcase_json:
        return testcase_json['instructions']
    else:
        extended_testcase_json = []
        for variable in testcase_json['variables']:
            temp = testcase_json['instructions']

            for index, value in variable.iteritems():
                regex = re.compile(':' + str(index))
                temp = regex.sub(value, temp)

            extended_testcase_json.append(temp)
        return "\n".join(extended_testcase_json)


def main():
    tmpfile="tmp.json"
    script_dir = os.path.dirname(os.path.realpath(__file__))

#FIXME: hardcoded feature file name #testcase_files = [script_dir + "/../../apps/search/test/manual/rocketbar.md"]
#testcase_files = [script_dir + "/../../apps/sms/test/manual/README.md"]

    repo = Repo('../../')
   # repo = Repo('../../../../') #for debuggin

    updated_diffs = filter(lambda x: "apps" in x.b_path and "test/manual" in x.b_path, repo.commit('HEAD~1').diff('HEAD'))

#print(updated_diffs)

#for testcase_file in testcase_files:
    diff_outs = []
    for diff in updated_diffs:
        #how to deteced diff type:
        #if diff.new_file: #&& edit only
        #elif diff.deleted_file:
        #elif diff.renamed:
        #else:

        testcase_before = tempfile.NamedTemporaryFile()
        testcase_after = tempfile.NamedTemporaryFile()
        after_file_is_empty = False
        before_file_is_empty = False

        try:
            testcase_before.write(diff.a_blob.data_stream.read())
        except AttributeError:
            testcase_before.write(json.dumps([]))
            before_file_is_empty = True
        try:
            testcase_after.write(diff.b_blob.data_stream.read())
        except AttributeError:
            testcase_after.write(json.dumps([]))

        testcase_before.flush()
        testcase_after.flush()

        before_json = []
        after_json = []

        flatten_before_json = []
        flatten_after_json = []
        #cmd = "%s %s > %s" % (script_dir + '/moztrap_integration/markdown-testfile-to-json/cli.js', testcase_file,
        #                    parsed_json_f.name)
        #os.system(cmd)
        #print subprocess.check_output(['cat', testcase_before.name])
        #TODO: Reduce this duplication to a function
        if not before_file_is_empty: #TODO:remove this flag?
            before_json += json.loads(subprocess.check_output([script_dir + '/moztrap_integration/markdown-testfile-to-json/cli.js', testcase_before.name]))
            flatten_before_json = flatten(before_json)
            for testcase_json in flatten_before_json:

                testcase_json['instructions'] = expand_table_if_exist(testcase_json)
                testcase_json['instructions'] = orm.parseCaseStep(testcase_json['instructions'])

        after_json += json.loads(subprocess.check_output([script_dir + '/moztrap_integration/markdown-testfile-to-json/cli.js', testcase_after.name]))

        flatten_after_json = flatten(after_json)
        for testcase_json in flatten_after_json:

            testcase_json['instructions'] = expand_table_if_exist(testcase_json)
            testcase_json['instructions'] = orm.parseCaseStep(testcase_json['instructions'])

        diff_outs.append(summarize_diff(flatten_before_json, flatten_after_json))
        # diff = (add, modify, remove)
        #print json.dumps(diff_out, indent=3)


    #parsed_json_f = tempfile.NamedTemporaryFile()

    mtapi.mtorigin = "https://moztrap-dev.allizom.org"
#The mz_user_name and mz_api_key is set in Travis CI
#mtapi.convert_mark_file_into_moztrap(tmpfile, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})
    #mtapi.load_json_into_moztrap(parsed_json_f.name, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})
    print diff_outs

    isPR = os.getenv('TRAVIS_PULL_REQUEST')
    if isPR == 'false' or isPR is None: #Don't sync PR builds
        mtapi.sync_diff_to_moztrap(diff_outs, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})

if __name__ == '__main__':
    main()
