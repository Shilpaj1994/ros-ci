#! /usr/bin/python3
"""
Node to check activity status of other nodes during execution
Author: Shilpaj Bhalerao
Date: Sep 26, 2020
"""
import rosnode
import rospy


class Inspector:
    """
    Class to Inspect the node status
    """
    def __init__(self):
        self._nodes = []
        self._active_nodes = []

        rospy.init_node("Inspector")
        rate = rospy.Rate(0.5)
        self.load_nodes()

        while not rospy.is_shutdown():
            self.current_nodes()
            self.check_status()
            # self.log_data()
            rate.sleep()

    def load_nodes(self):
        """
        Method to load the pre-loaded active node
        """
        self._nodes = ['/rosout', '/node1', '/node2','/node3',
                       '/node4', '/node5', '/Launcher', '/Inspector']
        # print("Nodes loaded: ", self._nodes)

    def current_nodes(self):
        """
        Method to check the current active nodes
        """
        self._active_nodes = rosnode.get_node_names()
        # print("Nodes loaded: ", self._nodes)
        # print("Active Nodes: ", self._active_nodes)

    def check_status(self):
        """
        Method to check the status of the nodes
        """
        self._nodes.sort()
        self._active_nodes.sort()

        # print(self._nodes)
        # print(self._active_nodes)

        # Common Bug - https://stackoverflow.com/questions/
        # 7301110/why-does-return-list-sort-return-none-not-the-list
        if self._active_nodes == self._nodes:
            rospy.loginfo("All nodes are active. System Status: Healthy")
        else:
            rospy.logwarn("All nodes are NOT active. System Status: Sick")

        print("-----------------------------------------")

    def log_data(self):
        """
        Method to log the data at a certain time interval
        """

    # TODO: Sort the current nodes based on the department packages


def exit_procedure():
    """
    Function to execute the shutdown protocol
    """


def main():
    """
    Main function
    """
    try:
        Inspector()
    except Exception as error:
        rospy.logerr(error)


if __name__ == "__main__":
    main()
