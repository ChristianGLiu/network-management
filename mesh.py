#!/usr/bin/python

"""Build a mesh topology in mininet based on user variables"""

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from itertools import combinations

def meshNet():

    """Create an empty network and add nodes to it."""

    # Add controller configuration variables
    host_count = 20
    switch_count = 10
    net = Mininet ( controller=RemoteController )
    links = []
    linklist = []

    info( '*** Adding controller\n' )
    # Modify controller IP and port to suit needs; add extra entries for multiple controllers
    net.addController( 'c0' , controller=RemoteController, ip="127.0.0.1", port=6633)

    info( '*** Adding hosts\n' )
    hosts = [('h%s' % (h + 1)) for h in range(host_count)]
    for host in hosts:
        net.addHost(host)

    info( '*** Adding switch\n' )
    switches = [('s%s' % (s + 1)) for s in range(switch_count)]
    for switch in switches:
        net.addSwitch(switch)

    for l in list(combinations(switches, 2)):
        links.append(l)

    for a, b in links:
        net.addLink(a, b )

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    meshNet()
