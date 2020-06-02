#!/usr/bin/python

"""Build a mesh original topology in mininet for csci 6706 assignment 1"""

from mininet.net import Mininet # import basic library for mininet
from mininet.node import RemoteController # import remotecontroller for opendaylight
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from itertools import combinations # for simplify the host links
from mininet.link import TCLink # config link parameters

def meshNet():

    """Create an empty network and add nodes to it."""

    # Add controller configuration variables
    host_count = 4
    switch_count = 4
    net = Mininet ( controller=RemoteController, link=TCLink)
    links = []
    switch_added = []

    info( '*** Adding controller\n' )
    # Modify controller IP and port to suit needs; add extra entries for multiple controllers
    net.addController( 'c0' , controller=RemoteController, ip="192.168.247.130", port=6633)

    info( '*** Adding hosts\n' )
    h1 = net.addHost("A", ip="192.168.10.1/24")
    h2 = net.addHost("B", ip="192.168.10.2/24")
    h3 = net.addHost("C", ip="192.168.10.3/24")
    h4 = net.addHost("D", ip="192.168.10.4/24")
    host_added = [h1, h2, h3, h4]

    info('*** Adding switch\n')
    switches = [('s%s' % (s + 1)) for s in range(switch_count)]
    for switch in switches:
        s = net.addSwitch(switch)
        switch_added.append(s)

    for l in list(combinations(switch_added, 2)):
        links.append(l)

    info('*** connecting switch\n')
    for a, b in links:
        net.addLink(a, b, bw=10)

    info('*** connecting host\n')
    for i in range(host_count):
        net.addLink(host_added[i], switch_added[i], bw=10)

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    meshNet()
