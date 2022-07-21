#!/usr/bin/env python
from obspy import read_inventory, UTCDateTime, read, Stream
from obspy.clients.fdsn import Client

net, sta, loc, chan = 'IU', 'ANMO', '00,10', 'LHZ'

stime = UTCDateTime('2022-01-15T00:00:00')

print(stime.julday, type(stime.julday), type(stime))

client = Client('IRIS')
st = Stream()
inv = read_inventory()

inv = client.get_stations(network=net, station=sta, location=loc, 
                          channel=chan, starttime=stime, level='response')
st += client.get_waveforms(network=net, station=sta, location=loc, 
                           channel=chan, starttime=stime, 
                           endtime=stime+24*60*60)


#st.detrend()
st.remove_response(inventory=inv, output='DISP' )

import matplotlib.pyplot as plt
st.sort()
fig = plt.figure(1)
for tr in st:
    plt.plot(tr.times()/(60*60), tr.data)
plt.show()
