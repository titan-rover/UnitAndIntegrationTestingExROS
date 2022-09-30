#!/usr/bin/env python

import sys
import rospy
import rostest
import unittest
from add_pkg.srv import AddMsg


class TestAddService(unittest.TestCase):
    def test_add_service(self):
        # The launch file starts the add_node.
        # add_node contains the add_service, so we wait for the node to start.
        rospy.wait_for_service('add_service')
        add_service = rospy.ServiceProxy('add_service', AddMsg)
        # Set up.
        x = 5
        y = 10
        expected = 15
        # Perform action.
        actual = add_service(x, y).result
        # Assert results.
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    rostest.rosrun(
        'add_pkg',
        'add_test',
        TestAddService,
        sys.argv
    )
