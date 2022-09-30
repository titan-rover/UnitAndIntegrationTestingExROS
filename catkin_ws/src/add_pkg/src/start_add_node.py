#!/usr/bin/env python

"""start_add_node.py
ROS uses this file to launch the add_node node because the main function for
the add_node.py file is used for automated unit testing.
"""

import add_node

if __name__ == '__main__':
    add_node.ros_main()
