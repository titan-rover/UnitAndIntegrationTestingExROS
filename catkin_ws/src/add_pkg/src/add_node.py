#!/usr/bin/env python

import unittest
import rospy
from add_pkg.srv import AddMsg, AddMsgRequest


class AddNode():
    NODE_NAME = 'add_node'

    def __init__(self):
        rospy.init_node(self.NODE_NAME)

        self.add_service = rospy.Service(
            'add_service',
            AddMsg,
            self.add_handler
        )

    def add_handler(self, req: AddMsgRequest):
        return add(req.x, req.y)


def add(x, y):
    return x + y


class AddUnitTests(unittest.TestCase):
    def add_test(self):
        x = 5
        y = 10
        expected = 15

        actual = add(x, y)

        self.assertEqual(expected, actual)


def ros_main():
    add_node = AddNode()
    rospy.spin()


if __name__ == '__main__':
    import rosunit
    rosunit.unitrun('add_pkg', 'add_unit_tests', AddUnitTests)
