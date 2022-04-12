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
        hh={}
        file=open(r'test_file.txt')
        lst=[]
        for line in file:
          lst.append([ float(x) for x in line.split()])
          column1 = [ x[0] for x in lst]
          column2 = [ x[1] for x in lst]
        for i in column1:
            s='s'+str(i)
            d[s]=self.addSwitch(s)
            h='h'+str(i)
            hh[h]=self.addHost(h)
        for i in column2:
            s='s'+str(i)
            d[s]=self.addSwitch(s)
            h='h'+str(i)
            hh[h]=self.addHost(h)
        for i in range(len(column1)):
          self.addLink('s'+str(column1[i]),'s'+str(column2[i]))
          
          



topos = { 'mytopo': ( lambda: MyTopo() ) }
