GZCONFIG = \
    """
[paths]
main:  ./gzdoom
logs:  ./logs
saves: ./saves

main.docs:   ${main}/docs
main.engine: ${main}/engine
main.games:  ${main}/games
main.mods:   ${main}/mods

engine.linux64:   ${main.engine}/linux_x86_64/gzdoom
engine.linux32:   ${main.engine}/linux_i386/gzdoom
engine.windows64: ${main.engine}/windows_x64/gzdoom.exe
engine.windows32: ${main.engine}/windows_x86/gzdoom.exe
engine.config:    ${main.engine}/gzdoom.ini

mods.gameplay: ${main.mods}/gameplay
mods.maps:     ${main.mods}/maps

[doom]
description:
    Ultimate DOOM!
game:
    ${paths:main.games}/doom.wad
mods:
    ${paths:mods.gameplay}/bd21RC8.pk3,
    ${paths:mods.gameplay}/EnchancedBulletPuffs.pk3,
    ${paths:mods.gameplay}/flashlight.pk7,
    ${paths:mods.gameplay}/flamecannon.pk3,
    ${paths:mods.gameplay}/knuckle_dusters.pk3,
    ${paths:mods.gameplay}/pistol.pk3,
    ${paths:mods.gameplay}/riffle.pk3,
    ${paths:mods.gameplay}/shotgun.pk3,

[doom2]
description:
    Doom 2
game:
    ${paths:main.games}/doom.wad
mods:
    ${paths:mods.gameplay}/bd21RC8.pk3,
    ${paths:mods.gameplay}/EnchancedBulletPuffs.pk3,
    ${paths:mods.gameplay}/flashlight.pk7,
    ${paths:mods.gameplay}/flamecannon.pk3,
    ${paths:mods.gameplay}/knuckle_dusters.pk3,
    ${paths:mods.gameplay}/pistol.pk3,
    ${paths:mods.gameplay}/riffle.pk3,
    ${paths:mods.gameplay}/shotgun.pk3,

[freedoom]
description:
    Free content game based on the Doom engine.
game:
    ${paths:main.games}/freedoom.wad
mods:
    ${paths:mods.gameplay}/bd21RC8.pk3,
    ${paths:mods.gameplay}/EnchancedBulletPuffs.pk3,
    ${paths:mods.gameplay}/flashlight.pk7,
    ${paths:mods.gameplay}/flamecannon.pk3,
    ${paths:mods.gameplay}/knuckle_dusters.pk3,
    ${paths:mods.gameplay}/pistol.pk3,
    ${paths:mods.gameplay}/riffle.pk3,
    ${paths:mods.gameplay}/shotgun.pk3,

[freedoom2]
description:
    Free content game based on the Doom engine.
game:
    ${paths:main.games}/freedoom2.wad
mods:
    ${paths:mods.gameplay}/bd21RC8.pk3,
    ${paths:mods.gameplay}/EnchancedBulletPuffs.pk3,
    ${paths:mods.gameplay}/flashlight.pk7,
    ${paths:mods.gameplay}/flamecannon.pk3,
    ${paths:mods.gameplay}/knuckle_dusters.pk3,
    ${paths:mods.gameplay}/pistol.pk3,
    ${paths:mods.gameplay}/riffle.pk3,
    ${paths:mods.gameplay}/shotgun.pk3,

[plutonia]
description:
    The Plutonia Experiment
game:
    ${paths:main.games}/plutonia.wad
mods:
    ${paths:mods.gameplay}/bd21RC8.pk3,
    ${paths:mods.gameplay}/EnchancedBulletPuffs.pk3,
    ${paths:mods.gameplay}/flashlight.pk7,
    ${paths:mods.gameplay}/flamecannon.pk3,
    ${paths:mods.gameplay}/knuckle_dusters.pk3,
    ${paths:mods.gameplay}/pistol.pk3,
    ${paths:mods.gameplay}/riffle.pk3,
    ${paths:mods.gameplay}/shotgun.pk3,

[tnt]
description:
    TNT: Evilution
game:
    ${paths:main.games}/tnt.wad
mods:
    ${paths:mods.gameplay}/bd21RC8.pk3,
    ${paths:mods.gameplay}/EnchancedBulletPuffs.pk3,
    ${paths:mods.gameplay}/flashlight.pk7,
    ${paths:mods.gameplay}/flamecannon.pk3,
    ${paths:mods.gameplay}/knuckle_dusters.pk3,
    ${paths:mods.gameplay}/pistol.pk3,
    ${paths:mods.gameplay}/riffle.pk3,
    ${paths:mods.gameplay}/shotgun.pk3,

[scythe]
description:
    Scythe
game:
    ${paths:main.games}/doom2.wad
mods:
    ${paths:mods.maps}/scythe.wad,
    ${paths:mods.gameplay}/bd21RC8.pk3,
    ${paths:mods.gameplay}/EnchancedBulletPuffs.pk3,
    ${paths:mods.gameplay}/flashlight.pk7,
    ${paths:mods.gameplay}/flamecannon.pk3,
    ${paths:mods.gameplay}/knuckle_dusters.pk3,
    ${paths:mods.gameplay}/pistol.pk3,
    ${paths:mods.gameplay}/riffle.pk3,
    ${paths:mods.gameplay}/shotgun.pk3,

[scythe2]
description:
    Scythe2
game:
    ${paths:main.games}/doom2.wad
mods:
    ${paths:mods.maps}/scythe2.wad,
    ${paths:mods.gameplay}/bd21RC8.pk3,
    ${paths:mods.gameplay}/EnchancedBulletPuffs.pk3,
    ${paths:mods.gameplay}/flashlight.pk7,
    ${paths:mods.gameplay}/flamecannon.pk3,
    ${paths:mods.gameplay}/knuckle_dusters.pk3,
    ${paths:mods.gameplay}/pistol.pk3,
    ${paths:mods.gameplay}/riffle.pk3,
    ${paths:mods.gameplay}/shotgun.pk3,

[clau]
description:
    Claustrophobia 1024
game:
    ${paths:main.games}/doom2.wad
mods:
    ${paths:mods.maps}/1024CLAU.wad,
    ${paths:mods.gameplay}/bd21RC8.pk3,
    ${paths:mods.gameplay}/EnchancedBulletPuffs.pk3,
    ${paths:mods.gameplay}/flashlight.pk7,
    ${paths:mods.gameplay}/flamecannon.pk3,
    ${paths:mods.gameplay}/knuckle_dusters.pk3,
    ${paths:mods.gameplay}/pistol.pk3,
    ${paths:mods.gameplay}/riffle.pk3,
    ${paths:mods.gameplay}/shotgun.pk3,

[av]
description:
    Alien Vendetta
game:
    ${paths:main.games}/doom2.wad
mods:
    ${paths:mods.maps}/av.wad,
    ${paths:mods.maps}/avmovfix.wad,
    ${paths:mods.gameplay}/bd21RC8.pk3,
    ${paths:mods.gameplay}/EnchancedBulletPuffs.pk3,
    ${paths:mods.gameplay}/flashlight.pk7,
    ${paths:mods.gameplay}/flamecannon.pk3,
    ${paths:mods.gameplay}/knuckle_dusters.pk3,
    ${paths:mods.gameplay}/pistol.pk3,
    ${paths:mods.gameplay}/riffle.pk3,
    ${paths:mods.gameplay}/shotgun.pk3,

[strife]
description:
    Strife game
game:
    ${paths:main.games}/strife1.wad,
    ${paths:main.games}/strife1_voices.wad
mods:
    ${paths:mods.gameplay}/sm4BBgorev2.pk3

[square]
description:
    Square game
game:
    ${paths:main.games}/square1.pk3
mods:
    ${paths:mods.gameplay}/sm4BBgorev2.pk3

[heretic]
description:
    Heretic game
game:
    ${paths:main.games}/heretic.wad
mods:
    ${paths:mods.gameplay}/sm4BBgorev2.pk3

[hexen]
description:
    Hexen game
game:
    ${paths:main.games}/hexen.wad
mods:
    ${paths:mods.gameplay}/sm4BBgorev2.pk3
"""
