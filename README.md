# 802_22_Testing Repo the WRAN HAMNET project
GNURadio / Octave - code and scripts for testing the 802.22 PHY and MAC

The basic testing setup at the moment (Jan/23) is

GNU Radio <-> hackrf  <-direct connection-> limesdr-{usb,mini} <-> 802_22_Base code -> Octave for IQ Data verification

On GnuRadio a OFDM frame is create based on the parameters which are used for WRAN 802.22 based setup; based on the limits given for the HAMRadio application it is aimed for (52MHr +/- and 2MHz BW)

The setup will be extended based on the software development steps. At the moment the main goal is to test superframe and frame syncing.

Next testing steps are most likely CPE ranging as this is minial bases for the OFDMA setup on 802.22 to have an in sync basestation and cpe relationsship

The data received via the limesdr is used in Octave to (a) verify that the software is getting proper data from lime and is processing it correctly (iq handling, queuing, timinig,...) and (b) to get have an instance for verification for the 802.22_BASE software.

For the processing of the IQ data the liquid-dsp library will be used. Which has an OFDM frame example - but this is based on 802.11 and needs to be adopted for 802.22.