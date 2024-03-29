cheats = {
    "PIXEL": [0, 0],
    "ZENITH": [100, 100],
    "NADIR": [99, 104],
    "PORT": [100, 114],
    "STARBOARD": [107, 116],
    "VOXEL": [110, 117],
    "POLY": [201, 200]
}

riddleAns = False
all = [
    {
        "name": "Home",
        "desc": "You're inside of a small apartment, cluttered with dishes and dirty clothes. The solitary window provides you with a grainy view of cars on a highway. There is a kitchen to your east and a bathroom to your north. There is a door to your south.",
        "x": 0,
        "y": 0,
        "gone": False,
        "items": []
    },
    {
        "name": "Kitchen",
        "desc": "There's a counter here, old worn marble. A sink is flooded with water, dishes are piled up to a near-tipping point.",
        "x": 1,
        "y": 0,
        "gone": False,
        "items": ["ticket"]
    },
    {
        "name": "Bathroom",
        "desc": "You are in a small bathroom. The tiled floor is worn, and chipped in places. There is a small walk-in closet to your west.",
        "x": 0,
        "y": 1,
        "gone": False,
        "items": []
    },
    {
        "name": "Closet",
        "desc": "You are inside a walk-in closet. There are a number of coats and shirts here, many worn and full of holes. The bathroom is to your east.",
        "x": -1,
        "y": 1,
        "gone": False,
        "items": ["life potion"]
    },
    {
        "name": "Street",
        "desc": "You walk outside of your apartment and onto a street. The air smells foul, and the humidity condenses on your skin. There is a train station to your south, and an apartment to your north.",
        "x": 0,
        "y": -1,
        "gone": False,
        "items": []
    },
    {
        "name": "Station",
        "desc": "You're in a crowded room, the sounds of voices reverberating inside of the station. To your south is an automated door. It requires a ticket.",
        "x": 0,
        "y": -2,
        "gone": False,
        "items": []
    },
    {
        "name": "Sidewalk",
        "desc": "You're on a sidewalk now. The walkway is dirty, and plastered with gum and dirt. To your west is a large metal fence and to your east is the main street.",
        "x": -1,
        "y": -1,
        "gone": False,
        "items": ["coin"]
    },
    {
        "name": "Ridge",
        "desc": "You're standing on a narrow passageway, a massive port to your east. Vast machines lift crates with incredible power, and belch smoke into the air.",
        "x": 1,
        "y": -1,
        "gone": False,
        "items": ["paperclip"]
    },
    {
        "name": "Train",
        "desc": "You're on the inside of a municipal train. The train is somewhat crowded, but it's not as bad as it could be.",
        "x": 0,
        "y": -3,
        "gone": False,
        "items": []
    },
    {
        "name": "Clearing",
        "desc": "You're standing in a large field. Sunlight streams in from an unknown source, the ground is covered with dew that feels good on your feet. The area has a sort of surreal feel, the lighting makes it feel ethereal.",
        "x": 100,
        "y": 100,
        "gone": False,
        "items": ["green shard"]
    },
    {
        "name": "Weathertop",
        "desc": "The land here grows more ragged, eventually forming mountains. These are too large to be scaled.",
        "x": 100,
        "y": 99,
        "gone": False,
        "items": ["coin"]
    },
    {
        "name": "Prairie",
        "desc": "You stand in a prairie. To your north lies a magestic temple, crafted expertly out of a beautiful wood. It seems right at home with the mountains behind it.",
        "x": 100,
        "y": 101,
        "gone": False,
        "items": []
    },
    {
        "name": "Grassland",
        "desc": "You're on a large, open plain. The ground slopes slightly in your favor, allowing you a clear view of the area. Vast mountain ranges, their peaks topped in snow, loom above you.",
        "x": 101,
        "y": 100,
        "gone": False,
        "items": []
    },
    {
        "name": "Valley",
        "desc": "The land begins to slope downwards, forming a valley. A river rages in the center, far too deep to wade across.",
        "x": 102,
        "y": 100,
        "gone": False,
        "items": ["coin"]
    },
    {
        "name": "River",
        "desc": "To your east lies a raging river. It would be impassible without a raft.",
        "x": 101,
        "y": 99,
        "gone": False,
        "items": []
    },
    {
        "name": "Canyon",
        "desc": "The valley deepens until it forma a sizable canyon, far too large to climb down. It curves west, meaning that further passage north is impossible from here. A temple is visible on your west.",
        "x": 101,
        "y": 101,
        "gone": False,
        "items": []
    },
    {
        "name": "Wood's end",
        "desc": "You are standing in a forest clearing. The forest thickens to the west, becoming impassible.",
        "x": 99,
        "y": 100,
        "gone": False,
        "items": ["wildberry"]
    },
    {
        "name": "Forest",
        "desc": "You are standing in large forest. To your north is a clearing. The westernmost parts of this forest are too overgrown to visit.",
        "x": 99,
        "y": 99,
        "gone": False,
        "items": []
    },
    {
        "name": "Woods",
        "desc": "The forest here thins, turning into a grassland. In front if you is a tea garden. There is a wall on this side of the temple, to enter it you would need to go east.",
        "x": 99,
        "y": 101,
        "gone": False,
        "items": []
    },
    {
        "name": "Side Garden",
        "desc": "The wood to your south finally thins into a grassland. To your north is the westmost wall of the temple. To enter the temple, you would need to go east.",
        "x": 99,
        "y": 102,
        "gone": False,
        "items": ["coin"]
    },
    {
        "name": "Garden",
        "desc": "You're in an impeccably manicured tea garden, complete with a small koi pond. From this location, the true grandeur of the temple is apparent. The temple door is to your north. It has a small slot in it, it's shape strikingly similar to the green shard in Clearing. There is a large canyon to your east, rendering that direction impassible.",
        "x": 100,
        "y": 102,
        "gone": False,
        "items": []
    },
    {
        "name": "Temple",
        "desc": "You stand inside of a large temple. The tatami mats feel good on your feet, the air feels warm but not hot. To your west is a short man, standing by a number of crystals and stones.",
        "x": 100,
        "y": 103,
        "gone": False,
        "items": []
    },
    {
        "name": "Temple Exit",
        "desc": "You are in the western wing of the temple. The crystals emit a strange warmth. Hot wind blows across your face from the northern entrance.",
        "x": 99,
        "y": 103,
        "gone": False,
        "items": []
    },
    {
        "name": "Desert",
        "desc": "You stand on a sand dune, overlooking a large desert. The sand is fine, you hold some up and watch it slip through your hand. The air is dry and warm, the sun is relentlessly hot. There is a temple to the south of you.",
        "x": 99,
        "y": 104,
        "gone": False,
        "items": []
    },
    {
        "name": "Flat",
        "desc": "To your east is a vast desert flatland, rendering that direction impassible.",
        "x": 100,
        "y": 104,
        "gone": False,
        "items": []
    },
    {
        "name": "Sandpit",
        "desc": "You attempt to stand in the sandpit, but quicksand begins to pull you under. You barely manage to make it back.",
        "x": 98,
        "y": 104,
        "gone": False,
        "items": [],
        "damage": "quicksand",
        "d": 30,
    },
    {
        "name": "Outlook",
        "desc": "You're now closer to the oasis. You can see the reflection of the sun on the water, and you notice a number of trees by the lagoon.",
        "x": 98,
        "y": 105,
        "gone": False,
        "items": []
    },
    {
        "name": "Marsh",
        "desc": "There is a lagoon in front of you. From here, you stand under a number of trees. You notice something shiny in one of them, but the tree is impossible to scale. The lagoon above you reflects the trees, and through the ripples in the water you are able to get a better glimpse of the shiny object. It seems crystaline in nature, refracting light in an odd effect not unlike that of the rippling water.",
        "x": 98,
        "y": 106,
        "gone": False,
        "items": []
    },
    {
        "name": "Oasis",
        "desc": "You're standing in the middle of an oasis. The water reaches up to your legs, and you have to roll your pants up to avoid their getting wet. The wet sand and cool water feel good on your feet, especially after such hot terrain.",
        "x": 98,
        "y": 107,
        "gone": False,
        "items": ["coin"]
    },
    {
        "name": "Oasis Shore",
        "desc": "You're standing on the eastern shore of an oasis. There are a number of trees to your southwest. The reflection of the sun on the water is bright, the ripples on the water make the sunlight dance on the sand. You notice an odd shack to your northeast.",
        "x": 99,
        "y": 107,
        "gone": False,
        "items": []
    },
    {
        "name": "Dune View",
        "desc": "There's a shack to your east. There's a wall on that side, so you'll need to go further southeast. There is a large sand dune to your north, rendering passage in that direction impossible.",
        "x": 99,
        "y": 108,
        "gone": False,
        "items": []
    },
    {
        "name": "Oasis View",
        "desc": "An oasis is visible on the horizon. Its refreshing blue water sharply contrasts the sandy landscape.",
        "x": 99,
        "y": 106,
        "gone": False,
        "items": []
    },
    {
        "name": "Sand Lowers",
        "desc": "The sand dune slopes at a steep angle. You imagine it would be fun to sled on.",
        "x": 99,
        "y": 105,
        "gone": False,
        "items": []
    },
    {
        "name": "Flattening",
        "desc": "The sand flattens out, and it turns into a featureless desert. It would be pointless to go further east.",
        "x": 100,
        "y": 105,
        "gone": False,
        "items": []
    },
    {
        "name": "Flatland",
        "desc": "An oasis is visible to the far northwest of you, but it's hard to tell this far down. Going further east would be pointless, as the land is incredibly flat.",
        "x": 100,
        "y": 106,
        "gone": False,
        "items": []
    },
    {
        "name": "Flatland 2",
        "desc": "Land here is featureless, hot. This only continues in the westernmost strip of desert, rendering it impassible. There's an oasis to the west, and you notice an odd sort of shack to your north.",
        "x": 100,
        "y": 107,
        "gone": False,
        "items": ["coin"]
    },
    {
        "name": "Oasis Flat",
        "desc": "The land starts to curve up to the northwest, eventually forming a slope so high it's impassible in both directions. There's a odd shack to your east.",
        "x": 98,
        "y": 108,
        "gone": False,
        "items": []
    },
    {
        "name": "Shack",
        "desc": "You stand inside a small shack. There's a door to the north, it's ornate decorations feel out of place out in the tacky shack. It seems to require a shard. The fine details are colored yellow.",
        "x": 100,
        "y": 108,
        "gone": False,
        "items": ["axe", "coin"]
    },
    {
        "name": "Hallway",
        "desc": "You're in a oddly majestic hallway. It seems to stretch for a long while.",
        "x": 100,
        "y": 109,
        "gone": False,
        "items": []
    },
    {
        "name": "Hallway",
        "desc": "You continue down the hallway. It's lit by torches, giving it a dungeon-ish feel.",
        "x": 100,
        "y": 110,
        "gone": False,
        "items": []
    },
    {
        "name": "Hallway",
        "desc": "The hallway begins to reach its end. You can see a strange machine at the end.",
        "x": 100,
        "y": 111,
        "gone": False,
        "items": []
    },
    {
        "name": "Endview",
        "desc": "You see the machine to your immediate north. It has a strange sort of aura about it as you go closer, it seems to play a high-pitched sound.",
        "x": 100,
        "y": 112,
        "gone": False,
        "items": []
    },
    {
        "name": "Endway",
        "desc": "You're at the end of the hallway, looking through an opening at the world beyond. You feel frigid air blowing on your face, and see a snow-covered land beyond.",
        "x": 100,
        "y": 113,
        "gone": False,
        "items": []
    },

    {
        "name": "Duneblock",
        "desc": "A massive dune to your west slopes upward, rendering passage in that direction impossible",
        "x": 97,
        "y": 104,
        "gone": False,
        "items": []
    },

    {
        "name": "Duneblock",
        "desc": "A massive dune to your west slopes upward, rendering passage in that direction impossible",
        "x": 97,
        "y": 105,
        "gone": False,
        "items": []
    },

    {
        "name": "Duneblock",
        "desc": "A massive dune to your west slopes upward, rendering passage in that direction impossible",
        "x": 97,
        "y": 106,
        "gone": False,
        "items": []
    },

    {
        "name": "Duneblock",
        "desc": "A massive dune to your west slopes upward, rendering passage in that direction impossible",
        "x": 97,
        "y": 107,
        "gone": False,
        "items": []
    },

    {
        "name": "Duneblock",
        "desc": "A massive dune to your west and north slopes upward, rendering passage in those directions impossible",
        "x": 97,
        "y": 108,
        "gone": False,
        "items": ["coin"]
    },
    {
        "name": "Mountain",
        "desc": "You're standing on a large mountain, overlooking a sizable range. The air is frigid, you pull your shirt up to your nose to keep warm.",
        "x": 100,
        "y": 114,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Landtop",
        "desc": "There is a large cliff that wraps from your west to south. To your far northeast, you notice a cabin.",
        "x": 101,
        "y": 114,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Landtop",
        "desc": "There is a large cliff to your south. To your northeast, you notice a cabin.",
        "x": 102,
        "y": 114,
        "gone": False,
        "items": ["coin"],
        "damage": "the cold"
    },
    {
        "name": "Landtop",
        "desc": "There is a large cliff to your south. There is a cabin entrance to your north.",
        "x": 103,
        "y": 114,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Edge",
        "desc": "The cliff to your west subsides, but leads to an impassible mountain range to your southeast. There is a cabin to your north.",
        "x": 104,
        "y": 114,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Cliffend",
        "desc": "A sizable cliff lies to your southwest, making it impossible to go further in those directions. You can see snow falling on the mountains beyond, causing a haze that somehow makes the vast alps both more stunning and alien.",
        "x": 99,
        "y": 114,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Mountview",
        "desc": "You stand on the peak of the mountain, overlooking a vast icy land. You see a small cabin to your far east, although it's hard to tell from this distance.",
        "x": 100,
        "y": 115,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Cliff",
        "desc": "There's a massive cliff to your west, making it impossible to go further.",
        "x": 99,
        "y": 115,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Door 2",
        "desc": "You stand in front of a door with a small keyhole in it. There are two more doors, one to your east and one to your west.",
        "x": 100,
        "y": 116,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Door 1",
        "desc": "You stand in front of a door with a small keyhole in it. There are two more doors to your east. A sharp cliff to your west renders that direction impassible.",
        "x": 99,
        "y": 116,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Door 3",
        "desc": "You stand in front of a door with a small keyhole in it. There are two more doors to your west.",
        "x": 101,
        "y": 116,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Snowblock",
        "desc": "You're in a snowy flat area, a partially frozen brook gurgles past you. There is a large mountain to your east, making passage in that direction impossible.",
        "x": 102,
        "y": 116,
        "gone": False,
        "items": ["coin"],
        "damage": "the cold"
    },

    {
        "name": "Room 2",
        "desc": "You step inside the room, but are instantly met with an unpleasant suprise: a number of hornets trapped inside attack you, and you lose substantial health.",
        "x": 100,
        "y": 117,
        "gone": False,
        "items": [],
        "damage": "hornets",
        "d": 50,
    },
    {
        "name": "Room 1",
        "desc": "You enter the room, but what's inside is not pretty: the room begins to flood, causing you significant damage.",
        "x": 99,
        "y": 117,
        "gone": False,
        "items": [],
        "damage": "flood",
        "d": 50,
    },
    {
        "name": "Room 3",
        "desc": "You stand in the room. It's quite barren, there are a few crates on the floor.",
        "x": 101,
        "y": 117,
        "gone": False,
        "items": ["white shard"],
        "damage": "the cold"
    },
    {
        "name": "Wall",
        "desc": "You're inside a dimly lit hallway. There's a retro arcade machine to your north.",
        "x": 101,
        "y": 118,
        "gone": False,
        "items": [],
    },
    {
        "name": "Arcade",
        "desc": "You stand next to the old arcade machine, and boot it up.",
        "x": 101,
        "y": 119,
        "gone": False,
        "items": [],
    },
    {
        "name": "Lookout",
        "desc": "You stand at the edge of the current mountain, further passage to the north would be impossible. From this location you can look out on the range below. It's a stunning sight, both beautiful and ominous. You notice a sort of dark cloud far away to your north, but you decide it's but a trick of the eye.",
        "x": 102,
        "y": 117,
        "gone": False,
        "items": ["coin"],
        "damage": "the cold"
    },

    {
        "name": "Block",
        "desc": "You're at the edge of a number of snowy mountains, further passage northeast would be impossible.",
        "x": 103,
        "y": 117,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },

    {
        "name": "Mountend",
        "desc": "The mountain lowers here, providing a view of a cabin to your east. It looks comfertable.",
        "x": 101,
        "y": 115,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Cabinway",
        "desc": "You're standing right next to a cabin, in the doorway. You can feel the warmth radiating from it, and think you hear a fire.",
        "x": 102,
        "y": 115,
        "gone": False,
        "items": [],
        "damage": "the cold"
    },
    {
        "name": "Cabin",
        "desc": "You are inside a cabin. There's a large fireplace here, and it feels good. There's a large, glossy poster here, and it seems quite of of place in such a cabin. There's a hallway to your east, with a door at the end.",
        "x": 103,
        "y": 115,
        "gone": False,
        "items": ["sweater","poster"],
    },

    {
        "name": "Hall",
        "desc": "You're standing in a short-ish hallway. The central cabin is to your west, and there's a door to your east, made of black obsidian. The door has white ridges, and a slot for a shard.",
        "x": 104,
        "y": 115,
        "gone": False,
        "items": [],
    },

    {
        "name": "Walkway",
        "desc": "The hallway seems to slope down, and a bubbling noise is audible.",
        "x": 105,
        "y": 115,
        "gone": False,
        "items": [],
    },

    {
        "name": "Walkway",
        "desc": "You're quite close to what appears to be the end of the walkway now. You can feel the fish nibbling on you, a large number of them are to the east of you.",
        "x": 106,
        "y": 115,
        "gone": False,
        "items": ["coin"],
    },

    {
        "name": "Beach",
        "desc": "You stand on a sandy beach. There is a hallway to your west, and a jungle to your east. You can see a vast ocean to your north and south west.",
        "x": 107,
        "y": 115,
        "gone": False,
        "items": [],
    },

    {
        "name": "Beachfront",
        "desc": "The beach extends here. You notice a fort of sorts to your north. There is an impassible jungle to your east, and an ocean to your west.",
        "x": 107,
        "y": 116,
        "gone": False,
        "items": ["shard part"],
    },

    {
        "name": "Beachend",
        "desc": "The beach continues here. The jungle to your east wraps around, meaning that passage both north and east is impossible. There is a door to your east, with the fine details done in a luminescent blue.",
        "x": 107,
        "y": 117,
        "gone": False,
        "items": [],
    },

    {
        "name": "Path",
        "desc": "There is a path here, hacked out of the jungle. There is a woman standing at the end of the path.",
        "x": 108,
        "y": 117,
        "gone": False,
        "items": [],
    },

    {
        "name": "Path End",
        "desc": "You look out on the world to your east with horror. The land is black and scorched, as if a fire had just torn through. The air smells foul, and you struggle to breathe.",
        "x": 109,
        "y": 117,
        "gone": False,
        "items": [],
    },

    {
        "name": "Sandland™",
        "desc": "The beach furthers here. There is a jungle to your east, so thick that passage would be impossible. There is a sea to your west.",
        "x": 107,
        "y": 114,
        "gone": False,
        "items": [],
    },

    {
        "name": "Beachblock",
        "desc": "The jungle to your east wraps to your south, making passage in that direction impossible. There is a jungle clearing to your east.",
        "x": 107,
        "y": 113,
        "gone": False,
        "items": [],
    },

    {
        "name": "Ocean Reef",
        "desc": "You're on a flat bit of land, standing in a coral reef. You can feel fish swimming around you, tickling your legs. To your south, the reef cuts out and moves to a sharp decline, making it impossible to move further in that direction.",
        "x": 106,
        "y": 113,
        "gone": False,
        "items": [],
        "damage": "water"
    },

    {
        "name": "Reef",
        "desc": "The reef continues here. There's what appears to be the mast of a sunken ship here, and there are a number of items on the ground. The ground cuts off to the southwest, making passage there impossible.",
        "x": 105,
        "y": 113,
        "gone": False,
        "items": ["coin", "shard part"],
        "damage": "water"
    },

    {
        "name": "Plane",
        "desc": "You're standing on a large plane. You can feel the fine sand, squelching between your feet.",
        "x": 106,
        "y": 114,
        "gone": False,
        "items": [],
        "damage": "water"
    },

    {
        "name": "Plane end",
        "desc": "The plane ends here, dropping off into a deep abyss to your west.",
        "x": 105,
        "y": 114,
        "gone": False,
        "items": [],
        "damage": "water"
    },

    {
        "name": "Block",
        "desc": "You're on a small scrap of rock, barely holding you back from the abyss below. Although you know falling wouldn't be dangerous, it's terrifying nonetheless.",
        "x": 106,
        "y": 117,
        "gone": False,
        "items": [],
        "damage": "water"
    },

    {
        "name": "Kelp View",
        "desc": "You're on a small plane. There's what appears to be a kelp forest to your west.",
        "x": 106,
        "y": 116,
        "gone": False,
        "items": [],
        "damage": "water"
    },

    {
        "name": "Kelp",
        "desc": "You're standing inside a kelp forest, incredibly tall and majestic. Small fish dart about, occasionally nibbling on your feet.",
        "x": 105,
        "y": 116,
        "gone": False,
        "items": [],
        "damage": "water"
    },

    {
        "name": "Forest",
        "desc": "The kelp forest grows only deeper here, becoming so thick that it's impossible to go further in most directions.",
        "x": 104,
        "y": 116,
        "gone": False,
        "items": ["shard part"],
        "damage": "water"
    },

    {
        "name": "Jungle",
        "desc": "The jungle clears in a small patch here, allowing you to enter. The air is humid, and the floor is thick with leaves.",
        "x": 108,
        "y": 113,
        "gone": False,
        "items": ["shard part"],
    },

    {
        "name": "Lookout",
        "desc": "You stand on top of a large hill. From here you can see a large city to your east, glowing ominously against the dark background. You see smoke rising from a number of ruins to your east.",
        "x": 110,
        "y": 117,
        "gone": False,
        "items": [],
    },

    {
        "name": "Ruin View",
        "desc": "You see what looks like a destroyed city to your north. The ground is littered with rubble and ash, and a number of small fires burn what organic material remains to the ground.",
        "x": 110,
        "y": 118,
        "gone": False,
        "items": [],
    },

    {
        "name": "Ruins",
        "desc": "You stand in the middle of a wrecked city. You can see toppled houses, smoldering trees. In places, entire amounts of the ground are blown out. There is a house to your east, and it remains partially intact.",
        "x": 110,
        "y": 119,
        "gone": False,
        "items": [],
    },

    {
        "name": "Hole",
        "desc": "You walk forward, and stumble into a large hole, still smoldering.",
        "x": 110,
        "y": 120,
        "gone": False,
        "items": [],
        "damage": "crater",
        "d": 20,
    },

    {
        "name": "Hole",
        "desc": "You walk forward, and stumble into a large hole, still smoldering.",
        "x": 111,
        "y": 118,
        "gone": False,
        "items": [],
        "damage": "crater",
        "d": 20,
    },

    {
        "name": "Wasteland",
        "desc": "The land here is charred, almost like a bed of coals. This area is completely devoid of life.",
        "x": 109,
        "y": 119,
        "gone": False,
        "items": [],
    },

    {
        "name": "Wasteland",
        "desc": "The wasteland continues here. There's a large rock to your north.",
        "x": 109,
        "y": 120,
        "gone": False,
        "items": [],
    },

    {
        "name": "Rock",
        "desc": "There's a sizable bolder here. You see a small glimmer from inside of it.",
        "x": 109,
        "y": 121,
        "gone": False,
        "items": [],
    },

    {
        "name": "Cliff",
        "desc": "A large rock falls off the cliff here, causing you significant damage.",
        "x": 108,
        "y": 119,
        "gone": False,
        "items": [],
        "damage": "rock",
        "d": 50,
    },

    {
        "name": "Cliff",
        "desc": "A large rock falls off the cliff here, causing you significant damage.",
        "x": 109,
        "y": 118,
        "gone": False,
        "items": [],
        "damage": "rock",
        "d": 50,
    },

    {
        "name": "House",
        "desc": "You're inside a wrecked house, full of rubble. The roof is partially destroyed, allowing a small amount of ambient light. There is a small closet to your east.",
        "x": 111,
        "y": 119,
        "gone": False,
        "items": [],
    },

    {
        "name": "Rubble",
        "desc": "There is large amount of rubble here, bits of clothing and plastic strewn around.",
        "x": 111,
        "y": 120,
        "gone": False,
        "items": ["pickaxe"],
    },

    {
        "name": "Closet",
        "desc": "You stand inside a small closet. The ceiling here is completely busted, allowing what little amounts of light the sun could muster to shine through. The closet seems to glow in an odd manner, a sort of dark light is prevalent.",
        "x": 112,
        "y": 119,
        "gone": False,
        "items": ["black shard"],
    },

    {
        "name": "Labyrinth",
        "desc": "You're in a large labyrinth, every room indistinguishable from the last.",
        "x": 200,
        "y": 200,
        "gone": False,
        "items": [],
    },

    {
        "name": "Labyrinth",
        "desc": "You're in a large labyrinth, every room indistinguishable from the last.",
        "x": 201,
        "y": 200,
        "gone": False,
        "items": [],
    },

    {
        "name": "Labyrinth",
        "desc": "You fall in a large pit, taking sizable damage. You climb back out.",
        "x": 202,
        "y": 200,
        "gone": False,
        "items": [],
        "damage": "pit",
        "d": 30,
    },

    {
        "name": "Labyrinth",
        "desc": "You're in a large labyrinth, every room indistinguishable from the last.",
        "x": 199,
        "y": 200,
        "gone": False,
        "items": [],
    },

    {
        "name": "Labyrinth",
        "desc": "You're in a large labyrinth, every room indistinguishable from the last.",
        "x": 199,
        "y": 201,
        "gone": False,
        "items": [],
    },

    {
        "name": "Labyrinth",
        "desc": "A large hole opens up underneath you, revealing a spike pit. You take considerable damage.",
        "x": 199,
        "y": 202,
        "gone": False,
        "items": [],
        "damage": "spikes",
        "d": 70,
    },

    {
        "name": "Labyrinth",
        "desc": "A large hole opens up underneath you, revealing a spike pit. You take considerable damage.",
        "x": 202,
        "y": 203,
        "gone": False,
        "items": [],
        "damage": "spikes",
        "d": 70,
    },

    {
        "name": "Labyrinth",
        "desc": "A large land mine explodes under you, doing you considerable damage.",
        "x": 204,
        "y": 203,
        "gone": False,
        "items": [],
        "damage": "spikes",
        "d": 40,
    },

    {
        "name": "Labyrinth",
        "desc": "A large land mine explodes under you, doing you considerable damage.",
        "x": 202,
        "y": 204,
        "gone": False,
        "items": [],
        "damage": "spikes",
        "d": 40,
    },

    {
        "name": "Labyrinth",
        "desc": "You fall in a large pit, taking sizable damage. You climb back out.",
        "x": 118,
        "y": 200,
        "gone": False,
        "items": [],
        "damage": "pit",
        "d": 30,
    },

    {
        "name": "Labyrinth",
        "desc": "You're in a large labyrinth, every room indistinguishable from the last.",
        "x": 201,
        "y": 201,
        "gone": False,
        "items": [],
    },

    {
        "name": "Labyrinth",
        "desc": "You're in a large labyrinth, every room indistinguishable from the last.",
        "x": 201,
        "y": 202,
        "gone": False,
        "items": [],
    },

    {
        "name": "Labyrinth",
        "desc": "You're in a large labyrinth, every room indistinguishable from the last.",
        "x": 202,
        "y": 202,
        "gone": False,
        "items": [],
    },

    {
        "name": "Labyrinth",
        "desc": "You can see an exit to your north.",
        "x": 203,
        "y": 202,
        "gone": False,
        "items": [],
    },

    {
        "name": "Labyrinth",
        "desc": "A large hole opens up underneath you, revealing a spike pit. You take considerable damage.",
        "x": 200,
        "y": 201,
        "gone": False,
        "items": [],
        "damage": "spikes",
        "d": 70,
    },

    {
        "name": "Core",
        "desc": "There's a large black crystal here, standing on a pedestal. It seems to radiate green light, pulsating in a sickening manner. The crystal in your inventory glows stronger and stronger, eventually becoming overwhelmingly bright.",
        "x": 203,
        "y": 203,
        "gone": False,
        "items": [],
    },

]

doors = {
    str([[0, 0],[0, -1]]): {
        "open": False,
        "require": ".none",
        "use": False,
        "txt": ".none"
    },
    str([[102, 115],[103, 115]]): {
        "open": False,
        "require": ".none",
        "use": False,
        "txt": ".none"
    },
    str([[100, 102],[100, 103]]): {
        "open": False,
        "require": "green shard",
        "use": False,
        "txt": "You gently place the shard inside the slot. It recedes inside the door, and the door starts go glow gently green. The door glows brighter and brigher, until you need to avert your eyes. Suddenly, the door opens and the crystal pops out. You pick it back up."
    },

    str([[100, 108],[100, 109]]): {
        "open": False,
        "require": "yellow shard",
        "use": False,
        "txt": "You press the yellow shard to the door, and an odd web-like pattern appears on it. The web glows stronger and stronger, until the door crumbles into pieces."
    },

    str([[104, 115],[105, 115]]): {
        "open": False,
        "require": "white shard",
        "use": False,
        "txt": "You insert the white shard. The door slides open in two parts, like an old elevator door. The shard pops out and you pick it back up."
    },


    str([[107, 117],[108, 117]]): {
        "open": False,
        "require": "blue shard",
        "use": False,
        "txt": "You tap the blue shard onto the door, and the door recedes into the ground, revealing a path through the jungle."
    },

    str([[0, -2],[0, -3]]): {
        "open": False,
        "require": "ticket",
        "use": True,
        "txt": "The door gobbles your ticket, and slides open. Instead of the normal train, a portal opens to your south. It pulsates, impossibly blue deep. No one else seems to notice it, walking through it and straight onto the other side."
    },

    str([[100, 116],[100, 117]]): {
        "open": False,
        "require": "key",
        "use": False,
        "txt": "You turn the key, and the door slides open."
    },

    str([[111, 119],[112, 119]]): {
        "open": False,
        "require": "gold key",
        "use": False,
        "txt": "You turn the key, and the door slides open."
    },

    str([[99, 116],[99, 117]]): {
        "open": False,
        "require": "key",
        "use": False,
        "txt": "You turn the key, and the door slides open."
    },

    str([[101, 116],[101, 117]]): {
        "open": False,
        "require": "key",
        "use": False,
        "txt": "You turn the key, and the door slides open."
    },
}

walls = [
    str([[-1, 0],[-1, -1]]), 
    str([[1, 0],[1, -1]]),
    str([[99, 102],[99, 103]]),
    str([[100, 103],[100, 104]]),
    str([[99, 108],[100, 108]]),
    str([[100, 108],[101, 108]]),
    str([[99, 117],[100, 117]]),
    str([[100, 117],[101, 117]]),
    str([[101, 117],[102, 117]]),
    str([[104, 115],[104, 114]]),
    str([[103, 115],[103, 114]]),
    str([[104, 115],[104, 116]]),
    str([[105, 114],[105, 115]]),
    str([[105, 115],[105, 116]]),
    str([[106, 115],[106, 116]]),
    str([[106, 115],[106, 114]]),
    str([[104, 114],[105, 114],])
]