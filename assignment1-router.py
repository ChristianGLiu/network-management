#!/usr/bin/python

"""Build a mesh topology in mininet for csci 6706 assignment 1"""

from mininet.net import Mininet # import basic library for mininet
from mininet.node import RemoteController # import remotecontroller for opendaylight
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from itertools import combinations # for simplify the host links
from mininet.link import TCLink # config link parameters
from mininet.node import Node
from mininet.topo import Topo

class LinuxRouter( Node ):

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class NetworkTopo( Topo ):

    def build( self, **_opts ):
        r1 = self.addNode( 'r1', cls=LinuxRouter, ip='192.168.10.1/24' )
        r2 = self.addNode('r2', cls=LinuxRouter, ip='192.168.10.2/24')
        r3 = self.addNode('r3', cls=LinuxRouter, ip='192.168.10.3/24')
        r4 = self.addNode('r4', cls=LinuxRouter, ip='192.168.10.4/24')

        r_added = [r1, r2, r3, r4]
        links = []

        for l in list(combinations(r_added, 2)):
            links.append(l)

        info('*** connecting switch\n')
        for a, b in links:
            self.addLink(a, b)

def run():
    topo = NetworkTopo()
    net = Mininet( topo=topo)
    net.start()
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()