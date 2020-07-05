# Python Lighting System
This is a work in progress piece of code. It synchronises your DMX lights with DJ Traktor Studio 3. 
You also automatically change the effects when a new track is played on Deck 1 & 2 

## Requirements 
### Equipment
* A USB Serial DMX adapter 
    - Tested with OPTO-USBDMX: https://fr.audiofanzine.com/controleur-d-eclairage-informati/electroconcept/opto-usb-dmx/. It should work with other devices
* DJ Traktor
    - Tested with Traktor Pro 3
    
### Setup
* Create a virtual midi interface: 
  - Open Traktor Pro 3
  - Go to Settings > Controller Manager
    - Add: Generic MIDI. Out-port: Traktor Virtual Output
    - Add: Denon.DN.HC4500. Out-port: Traktor Virtual Output
  - Go to Settings > External Sync
    - Activate: Enable MIDI Clock

* Creates a song.csv file inside src/ 
  - You may use songs.csv.template file 
  - Write:
    - First column: the exact name of the track
    - Second column: the name of the effect you want to play
    - Third column: ignored for now
    - Fourth column: the timestamp when you want the effect to be triggered 
    
### Structures 
* scenes/ contains scenes. You may need to adapt it to your configuration 
* effects/ is a combination of scenes that are triggered each time a MIDI beat is received 

### To be done
* A better UI 
