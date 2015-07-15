#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../../")

import unittest
import json

import sync



class TestSync(unittest.TestCase):
    # def setUp(self):

    def _assertResult(self, adds, modifies, removes, exp_adds=[], exp_modifies=[], exp_removes=[]):
        self.assertEqual(adds, exp_adds)
        self.assertEqual(modifies, exp_modifies)
        self.assertEqual(removes, exp_removes)

    def test_summarize_diff_add_case(self):
        with open('before.json', 'r') as bf:
            before_json = json.load(bf)
        with open('after_add_case.json', 'r') as af:
            after_json = json.load(af)

        adds, modifies, removes = sync.summarize_diff(before_json, after_json)

        expected_adds= [{
            "name": "Launch suite",
            "testcases": [
                {
                    "bug": 2,
                    "id": "fxos.func.sanity.launch_foobar",
                    "instructions": "Launch FOOBAR",
                    "state": "draft",
                    "userStory": 1
                }
            ]
        }]
        self._assertResult(adds, modifies, removes,
                           exp_adds= expected_adds)

    def test_summarize_diff_remove_case(self):
        with open('before.json', 'r') as bf:
            before_json = json.load(bf)
        with open('after_remove_case.json', 'r') as af:
            after_json = json.load(af)

        adds, modifies, removes = sync.summarize_diff(before_json, after_json)

        expected_removes = [{
                            "name": "Launch suite",
                            "testcases": [
                                {
                                    "bug": 4,
                                    "id": "fxos.func.sanity.launch_settings",
                                    "instructions": "Launch settings, oh yeah",
                                    "state": "draft",
                                    "userStory": 3
                                }
                            ]
                        }]
        self._assertResult(adds, modifies, removes,
                           exp_removes = expected_removes)

    def test_summarize_diff_modify_case(self):
        with open('before.json', 'r') as bf:
            before_json = json.load(bf)
        with open('after_modify_case.json', 'r') as af:
            after_json = json.load(af)

        adds, modifies, removes = sync.summarize_diff(before_json, after_json)

        expected_modifies= [{
                            "name": "Launch suite",
                            "testcases": [
                                {
                                    "bug": 2,
                                    "id": "fxos.func.sanity.launch_contacts",
                                    "instructions": "Launch contacts! OH I MODIFIED THIS!!!",
                                    "state": "draft",
                                    "userStory": 1
                                }
                            ]
                        }]
        self._assertResult(adds, modifies, removes,
                           exp_modifies= expected_modifies)

if __name__ == '__main__':
    unittest.main()
