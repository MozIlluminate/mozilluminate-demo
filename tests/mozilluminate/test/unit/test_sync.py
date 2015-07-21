#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../../")

import unittest
import json

import sync



class TestSync(unittest.TestCase):
    # def setUp(self):

    def _assertResult(self, diff, exp_adds=[], exp_modifies=[], exp_removes=[], exp_suite_adds=[], exp_suite_removes=[]):
        self.assertEqual(diff['case']['added'], exp_adds)
        self.assertEqual(diff['case']['modified'], exp_modifies)
        self.assertEqual(diff['case']['removed'], exp_removes)
        self.assertEqual(diff['suite']['added'], exp_suite_adds)
        self.assertEqual(diff['suite']['removed'], exp_suite_removes)

    def test_summarize_diff_add_case(self):
        with open('before.json', 'r') as bf:
            before_json = json.load(bf)
        with open('after_add_case.json', 'r') as af:
            after_json = json.load(af)

        diff = sync.summarize_diff(sync.flatten(before_json),
                                                      sync.flatten(after_json))

        expected_adds= [{
                            "bug": 2,
                            "id": "fxos.func.sanity.launch_foobar",
                            "instructions": "Launch FOOBAR",
                            "state": "draft",
                            "userStory": 1,
                            "suites": ["Launch suite"],
                        }]
        self._assertResult(diff,
                           exp_adds= expected_adds)

    def test_summarize_diff_remove_case(self):
        with open('before.json', 'r') as bf:
            before_json = json.load(bf)
        with open('after_remove_case.json', 'r') as af:
            after_json = json.load(af)

        diff = sync.summarize_diff(sync.flatten(before_json),
                                                      sync.flatten(after_json))

        expected_removes = [{
                                "bug": 4,
                                "id": "fxos.func.sanity.launch_settings",
                                "instructions": "Launch settings, oh yeah",
                                "state": "draft",
                                "userStory": 3,
                                "suites": ["Launch suite"],
                            }]
        self._assertResult(diff,
                           exp_removes = expected_removes)

    def test_summarize_diff_modify_case(self):
        with open('before.json', 'r') as bf:
            before_json = json.load(bf)
        with open('after_modify_case.json', 'r') as af:
            after_json = json.load(af)

        diff = sync.summarize_diff(sync.flatten(before_json),
                                                      sync.flatten(after_json))

        expected_modifies= [{
                                "bug": 2,
                                "id": "fxos.func.sanity.launch_contacts",
                                "instructions": "Launch contacts! OH I MODIFIED THIS!!!",
                                "state": "draft",
                                "userStory": 1,
                                "suites": ["Launch suite"],
                            }]
        self._assertResult(diff,
                           exp_modifies= expected_modifies)

    def test_summarize_diff_add_suite_and_move_case_between_suite(self):
        with open('before.json', 'r') as bf:
            before_json = json.load(bf)
        with open('after_move_between_suite.json', 'r') as af:
            after_json = json.load(af)

        diff = sync.summarize_diff(sync.flatten(before_json),
                                                      sync.flatten(after_json))

        expected_modifies = [{
                                "bug": 4,
                                "id": "fxos.func.sanity.launch_settings",
                                "instructions": "Launch settings, oh yeah",
                                "state": "draft",
                                "userStory": 3,
                                "suites": ["Close suite"]
                            }]
        self._assertResult(diff,
                           exp_modifies = expected_modifies,
                           exp_suite_adds = expected_modifies[0]['suites'])

    def test_summarize_diff_delete_suite(self):
        with open('before.json', 'r') as bf:
            before_json = json.load(bf)

        after_json = []

        diff = sync.summarize_diff(sync.flatten(before_json),
                                                      sync.flatten(after_json))

        expected_removes = [
            {
                "bug": 2,
                "id": "fxos.func.sanity.launch_contacts",
                "instructions": "Launch contacts! this is an updated version",
                "state": "draft",
                "userStory": 1,
                "suites": ["Launch suite"]
            },
            {
                "bug": 4,
                "id": "fxos.func.sanity.launch_settings",
                "instructions": "Launch settings, oh yeah",
                "state": "draft",
                "userStory": 3,
                "suites": ["Launch suite"]
            }
        ]
        self._assertResult(diff,
                           exp_removes = expected_removes,
                           exp_suite_removes = expected_removes[0]['suites']  )

    def test_flatten(self):
        with open('before.json', 'r') as bf:
            before_json = json.load(bf)


        expected_out = [
            {
                "bug": 2,
                "id": "fxos.func.sanity.launch_contacts",
                "instructions": "Launch contacts! this is an updated version",
                "state": "draft",
                "userStory": 1,
                "suites": ["Launch suite"]
            },
            {
                "bug": 4,
                "id": "fxos.func.sanity.launch_settings",
                "instructions": "Launch settings, oh yeah",
                "state": "draft",
                "userStory": 3,
                "suites": ["Launch suite"]
            }
        ]

        self.assertEqual(sync.flatten(before_json), expected_out)

if __name__ == '__main__':
    unittest.main()
