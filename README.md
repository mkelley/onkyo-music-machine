# onkyo-music-machine
Web control of my home stereo.

## HDMI control (CEC)

Turn on in Onkyo's hardware settings

Install cec-utils.

```
$ echo 'scan' | cec-client -s -d 1
opening a connection to the CEC adapter...
requesting CEC bus information ...
CEC bus information
===================
device #1: Recorder 1
address:       1.0.0.0
active source: no
vendor:        Pulse Eight
osd string:    CECTester
CEC version:   1.4
power status:  on
language:      eng


device #5: Audio
address:       f.f.f.f
active source: no
vendor:        Onkyo
osd string:    TX-SR607
CEC version:   1.3a
power status:  on
language:      ???


currently active source: unknown (-1)
```

Send command: `echo 'command' | cec-client -s -d 1`

For device #5:

| Action | Command | Notes |
|--------|---------|-------|
| Power on | on 5 | |
| Standby | standby 5 | |



## Old notes when I tried to get the RI 3.5 mm interface to work

Requires pigpiod running.

## RI Codes for the TX-SR607

| Action | Command | Notes |
|--------|---------|-------|
| Input CD | 0x20 | Switch input to CD channel |
| Turn On + CD | 0x2F | Turn ON receiver and select CD as input channel |
| Input TV/TAPE | 0x70 | Switch input to TAPE channel |
| Turn On + TAPE | 0x7F | Turn ON receiver and select TAPE as input channel
| Input BD/DVD | 0x120 | Switch input to BD/DVD channel |
| Turn On + BD/DVD | 0x12F | Turn ON receiver and select BD/DVD as input channel |
| Dimmer Hi | 0x2B0 | Set dimmer brightness to highest level |
| Dimmer Mid | 0x2B1 | Set dimmer brightness to mid level |
| Dimmer Lo | 0x2B2 | Set dimmer brightness to lowest level |
| Dimmer Hi | 0x2B8 | Set dimmer brightness to highest level |
| Dimmer Lo | 0x2BF | Set dimmer brightness to lowest level |
| Test mode | 0x421 - 0x424 | Some kind of test modes. Test modes clear receiver settings. |
Radio search next	0x430	Tune next radio station when radio is selected.
Radio search previous	0x431	Tune previous radio station when radio is selected.
Radio Stereo/Mono	0x432	Switch between Stereo and Mono when FM radio is selected.
Radio station next	0x433	Jump to next stored radio station when radio is selected.
Radio station previous	0x434	Jump to previous stored radio station when radio is selected.


