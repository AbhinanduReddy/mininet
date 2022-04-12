"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."
        d={}
        for i in range(250,300):
            s='s'+str(i)
            d[s]=self.addSwitch(s)
        with open(r'test_file.txt') as f:
          line = f.readline()
          while line:
            line = f.readline()
            self.addLink(d[line[0:3]],d[line[4::]])
#          # Add hosts and switches
#         leftHost = self.addHost( 'h1' )
#         rightHost = self.addHost( 'h2' )
#         leftSwitch = self.addSwitch( 's251' )
#         rightSwitch = self.addSwitch( 's256' )

#         # Add links
#         self.addLink( leftHost, leftSwitch )
#         self.addLink( leftSwitch, rightSwitch )
#         self.addLink( rightSwitch, rightHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }
