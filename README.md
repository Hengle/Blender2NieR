![Blender2NieR](https://i.imgur.com/WhfOZ90.png)
## VERY IMPORTANT
My addon Nier2Blender_2.8 is a REQUIREMENT. Without it, nothing will work, you will understand why. <br>
https://github.com/WoefulWolf/Nier2Blender_2.8 <br>
THIS IS ALSO STILL IN DEVELOPMENT BUT IS AS STABLE AS IT CURRENTLY CAN BE. If any updates break something that worked in the past, please let me know immediately. Every update is intended to be fully functional, the next just better than the prior. <br>
<br>
If you use my tool and release something, please give appropriate credit and info. I would really love for my tools to become more 
widely known so that others can start modding too. :)

## Some Tips:
#### For now you should just understand these basic rules:
* You can find info/tutorials at the wiki (near top of this page).
* Watch https://youtu.be/Mr-zmXAwM5g for a very basic example video.
* Visit our [NieR:Modding](https://discord.gg/7F76ZVv) community Discord server for help.
* Any model you wish to edit or replace must first be imported using my above-mentioned addon WITH materials/shaders. Thus DTT import is recommended to have it do everything automatically for you. <br>
* THINGS YOU SHOULD NOT CHANGE (unless you know what you are doing) include object names, armatures or any custom properties on objects, materials, bones, armatures, etc. <br>
* An object cannot have more than one material. (Thus using the original from import is recommended, textures are separate). <br>
* All unused materials should be purged before export (something I might fix in the future, but not a priority). <br>
* When working with bone weights, one vertex cannot belong to more than 4 groups (in other words have weights belonging to more than 4 bones) <br>
* All meshes must be triangulated. (This gets done automatically, but you can do it yourself to ensure no unexpected results.) <br>
* Open the Blender Console Window when exporting, this allows you to see its progress and any export errors. <br>
* A lot of my code is put together with duct-tape and instant ramen, thus it is unoptimized, ugly and straight up fucked at places. :)

## WTP & WTA Exporting
* The WTP/WTA Exporter can be found under the "Output" tab of the "Properties" window.
* I recommend to "Purge Materials" before Fetching N:A Materials.
* I recommend loading the original textures before adding/replacing with custom ones. To do this, use the "Select Textures Directory" option and load the "textures" folder created by NieR2Blender_2.8 when importing a model (*/nier2blender_extracted/######.dtt/textures/*)
* After adding or changing a unique texture identifier, make sure to "Sync Identifiers in Materials" before exporting a WMB.
* Leave texture paths set to "None" if not using the texture map.

## DAT & DAT Packing
* The DAT/DTT Exporter can be found under the "Output" tab of the "Properties" window.
* Make sure you have the required metadata files also located in the folder you wish to pack (metadata files are generated by NieR2Blender_2.8 when importing a DTT and can be found the the nier2blender_extracted directories).
 
## Bug Reports and Contact
* Please leave bug reports. You can leave them here on the GitHub under issues. Remember to post as much info as you can. <br>
* Feel free to contact me for any questions or issues you might be having. You can contact me, and some other members of the NieR:Modding community at our Discord server: https://discord.gg/7F76ZVv

# GL HF!

## THANKS:
* The wonderful people from Bayonetta Tools, namely Elediane.
* Kekoulis, literal months of support and help with testing.
* DevolasRevenge, for help with testing and the writing of wiki pages.
* The BONE boi Ameii.
* Comrade Petrarca. o7
* Martino.
* delle the texture man.
* Platinum Games.
* **Yoko Taro.**
