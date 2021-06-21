# Vagrant - A Python Text Adventure

This is the last of many, many text adventures that I have started and 
never finished. With this piece of software, my python text adventure
(a project I started over 5 years ago, and abandoned many times since),
will either come to light or die forever.

This program will be written right, or not at all. So, here is what 
needs to happen to develop this software.

## Project vision

Combat in a text adventure is more than likely boring. Hence, the focus 
will be on exploration and puzzle solving. The world will need to be 
interesting, vast, have interesting mechanics, and excellent descriptors
for the tiles.

Perhaps it will set it a world with low magic, you're in the shoes of a 
character who is looking for something lost, and there is treasure to
find along the way. Either way, the way this character carries out his 
journey is in the hands of the player.

A looming castle peers down from its mountainous peak, as the player 
searches for their lost friend, said to be poking around here. Armed
only with thier wit and some supplies they had brought with them on the
road, the player must enter this unsettling region.

## To get started

**First** and foremost, a world with a set of basic tiles as well as a 
player character will need to be created. The first demo should aim for:
- A character that can move between a set of tiles.

**Secondly**, we should be able to interact with some of the tiles. 
If there is an object on the tile, we should be able to pick it up, 
which would remove the item from the tile. Similarly, we should be able 
to leave items:
- Taking and leaving items/interacting with terrain and having it save.

**Third** will be some sort of puzzle where the palyer must find a key 
and use it on a locked door.

### Demo One:
- A **player object** with XY coord values and move_direction functions
- A set of **tile objects** with XY coord values
- A list or dict containing the set of tiles
- A game loop

### Program data/information

- Coordinates and tile/character location should be on a 3D plane. This 
  means using XYZ coordinate system, though Z coordinate may be able to
  be included at a later date.