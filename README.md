# InputSwitcher
Switches MX MCHNCL keyboard between a Linux host and a Windows11 host based on mice activity. 

As opposed to solutions like [input-leap](https://github.com/input-leap/input-leap/tree/master) keyboard events are not tunneled through a server to the client, but the MX MCHNCL keyboard is directly re-connected to the appropriate host via Bluetooth. This minimizes latency and increases security.

For InputSwitcher we need a single MX MCHNCL keyboard and two mice. The keyboard is connected on channel 2, resp. channel 3 via Bluetooth LE with the Windows host, resp. with the Linux host.
Each host has its own mouse connected to an USB radio stick.

InputSwitcher automatically switches the keyboard to the host where the mouse has been last touched, that is the keyboard follows the mice.

Channel switching is done by sending the switching command to the MX MCHNCL using [hidapitester](https://github.com/todbot/hidapitester). Hosts communicate via ssh to initiate the channel switching.

See also: [youtube](https://www.youtube.com/shorts/89gC9yr_D7g)
