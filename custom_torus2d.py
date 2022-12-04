from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.log import setLogLevel, info
from mininet.cli import CLI



class Torus2dNetwork():
    net = Mininet(topo = None, build = False)

    info( "*** Adding controller\n" )
    c0 = net.addController(name="c0", controller=RemoteController)    

    info( "*** Adding hosts\n" )
    h1 = net.addHost("h1")
    h2 = net.addHost("h2")
    h3 = net.addHost("h3")
    h4 = net.addHost("h4")
    h5 = net.addHost("h5")
    h6 = net.addHost("h6")
    h7 = net.addHost("h7")
    h8 = net.addHost("h8")
    h9 = net.addHost("h9")

    info( "*** Adding links\n" )
    net.addLink( h1, h2 )
    net.addLink( h2, h3 ) 
    net.addLink( h3, h1 ) 

    net.addLink( h4, h5 ) 
    net.addLink( h5, h6 )
    net.addLink( h6, h4 )

    net.addLink( h7, h8 )
    net.addLink( h8, h9 )
    net.addLink( h9, h7 )

    net.addLink( h1, h4 )
    net.addLink( h4, h7 )
    net.addLink( h7, h1 )

    net.addLink( h2, h5 )
    net.addLink( h5, h8 ) 
    net.addLink( h8, h2 )

    net.addLink( h3, h6 )
    net.addLink( h6, h9 )
    net.addLink( h9, h3 )


    info( "*** Start network\n")
    net.build()

    info("*** Start controllers\n")
    for controller in net.controllers: 
        controller.start()

    CLI(net)
    net.stop()


if __name__ == "__main__":
    setLogLevel('info')
    Torus1dNetwork()
