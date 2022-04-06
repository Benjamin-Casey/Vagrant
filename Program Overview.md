## Game
- Prints Tile info, then calls input hander to ask for and call action functions.
- Args/Dependencies:
	- Player
	- Map
	- Input Handler

## Input Handler
- Asks for input, saves it, then calls relevant action functions
- Args/Dependencies:
	- Player functions (Player)

## World map
- Generates a tile set based on the preliminary 2d list 
- Args:
	- None

## Tile
- Stores x, y, and description data for each tile
- Args:
	- None

## Player
- Stores player data and functions to move the player around the world, etc.
- Args/Dependencies:
	- World map for adjacent tiles. Move this to map.
