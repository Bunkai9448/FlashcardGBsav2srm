# README

I have this chinese everdrive clone:  
![Clone Everdrive Picture](https://github.com/Bunkai9448/FlashcardGBsav2srm/blob/main/everdrive.jpg)

Until now, using the [Online savefileconverter](https://savefileconverter.com/#/srm-sav), I was only able to get a working sav for
mgba and other emulators, but I was unable to do the conversion back from sav to the flashcard SRM. So, I decided to test 
[chat GPT's AI](https://chatgpt.com/) with the online converter and the code from [c99koder/srm-to-sav](https://github.com/c99koder/srm-to-sav) to 
create a converter for my saves. I tested the output with 2 games ("Pokemon - Aka (Japan) (SGB Enhanced)" and "Mickey's Racing Adventure") with positive results. Hence why I put them here for anyone interested in using them.

## Use
*Run the appropiate command from the folder that contains your .sav or .srm files.*

- From SAV to SRM
`python sav2srm.py -i <input.sav> -o <output.srm>`

- From SRM to SAV
`python sav-to-srm.py -i <input.sav> -o <output.srm>`

# FAQ

- I've already sent a message to the [Online savefileconverter](https://savefileconverter.com/#/srm-sav) owner in case s/he wants to add it.
- I haven't tested in more games yet, but feel free to do it and report the results with an [issue](https://github.com/Bunkai9448/FlashcardGBsav2srm/issues) 
stating the game and if it did work or not.

## Game's Tested

- Pokemon - Aka (Japan) (SGB Enhanced) > Works
- Pocket Monsters Gin (Japan) (Rev A) (SGB Enhanced) > Works
- Mickey's Racing Adventure > Works
- Initial D Gaiden (Japan) (SGB Enhanced) > Works
