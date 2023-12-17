[tag:electronics] [tag:today_i_did_this]

Mediasonic Probox fan replacement
=================================

I have a Mediasonic Probox for file storage. After 3.5 years of use (purchased May 2020), one of the fans has gone bad:

<audio src="before.flac" controls></audio>

The stock fans are labeled YLTC DFS802012H, 12 Volts, 0.23 Amps, and measure 80x80x20mm.

For my replacement, I chose the Arctic P8 because it seems to have a good reputation for being quiet, and I feel that a pressure-optimized fan (the P series) is more appropriate than a flow-optimized fan (the F series) for pushing air around the box's motherboard and between the drives.

![](old_fan_new_fan.jpg)

Before doing some research, it hadn't occurred to me that the thicknesses of 80mm case fans wouldn't all be the same. On this [Mediasonic forum post](mediasonic_forum_4054.html) about fan replacement, someone commented that most fans on the market are 25mm thick and would not be a drop-in replacement for the 20mm stock. The screws are not long enough to go all the way through a 25mm fan, and the shroud, and have any real bite left over.

![](fan_thickness.jpg)

Besides the problem of length, there is also diameter: without the shroud, the screws slip straight through the mounting holes in the fan itself, so the shroud is necessary... or so I thought. Then I found [this thingiverse thing](https://www.thingiverse.com/thing:4965892 "Mediasonic Probox fan stanchion by fl0rm") where the author takes advantage of the empty space between the two faces of the fan housing to slip in a little hollow post. This bypasses the extra 5mm of fan thickness by placing the screw head within the Z-profile of the fan, and gives it something to grab onto, solving both problems at once! Very clever!

```OpenSCAD
$fa = 0.1;
$fs = 0.1;

difference()
{
    cylinder(d=5.5, h=10);
    cylinder(d=2.9, h=10);
}

```

Please excuse the poor quality of the prints...

![](standoffs.jpg)

![](standoff_length.jpg)

Also, most fans use a three-pin connector with one wire carrying RPM signal data, but the Mediasonic only uses the two power pins and a 2mm connector. There are [adapters](https://www.aliexpress.us/item/2251832624753638.html "ARSYLID Conversion cable 3 pin to 2 pin 2.0mm adapter fan cable 12V cooler fan for VGA cooling fan 2pin micro-2pin") out there, mentioned in the forum post, so you can make the swap non-destructively. I was not in the mood to wait multiple weeks for aliexpress shipping, so I cut and soldered the ends.

![](wires_cut.jpg)

![](wires_soldered.jpg)

Of course, you could just buy a fan that's 20mm thick with a two-pin connector in the first place. But all the options I saw were very cheap/generic looking, and the per-fan prices were not cheaper than the Arctics, and I've been wanting to replace the stock fans with quieter ones for a long time anyway. In this case, I'd rather buy a fan from a known brand with a good reputation for quiet, even if it requires some modification.

You have to admit this doesn't really seem like the ideal air path:

![](guts.jpg)

But the replacement went just fine and the fan feels very secure.

![](install_1.jpg)

![](install_2.jpg)

![](install_3.jpg)

![](install_4.jpg)

I felt I should add a bit of tape around the edge to discourage air from leaking into the sides, since the shroud is gone now.

![](tape_seal.jpg)

After this, I also replaced the other fan in the same manner.

At low speed the new fans are essentially inaudible:

<audio src="after_low.flac" controls></audio>

At full speed, they're still pretty quiet:

<audio src="after_high.flac" controls></audio>

These recordings were made with no hard drives in the box. Once the drives are in... well... it's quieter than it was before but it's not exactly life-changing.

For the first few days, I heard a new sound that made me think the whole thing was pointless -- it was a kind of ringing, or resonance, or beat frequency that was audible when I sat in my chair, but seemed to disappear when I got close to the box to listen for it. I'm not sure if it was an illusion, or the [heart](https://en.wikipedia.org/wiki/The_Tell-Tale_Heart) of my latest victim, or the bearings just breaking themselves in, but it's better now.

I don't normally publish this kind of thing, since I feel it's a little trivial or unimpressive, and because it mentions [brand names](/writing/advertixing#HailCorporate). But whenever I am solving a problem, I rely on posts made by other people solving the same problem -- something as simple as a hollow cylinder turned out to be a very helpful bit of inspiration to me. If that person thought a cylinder was too trivial to share, it would have taken me longer to do this. So maybe I should contribute back in the same way more often.

