[tag:electronics]

Auto-off power banks
====================

The essential parts of a USB power bank are:

1. A battery.
2. Charge controller to receive USB input and safely charge the battery.
3. Protection circuit to prevent the battery from being excessively discharged.
4. Voltage regulator to convert the battery's voltage to 5 V for USB output.

Artist's rendition:

![Photograph of a breadboard containing a TP4056 charge controller, a 5 V USB regulator, and an 18650 battery cell. A cable connects this breadboard to a cell phone which is being charged.](breadboard1.jpg)

But the majority of power banks on the market go the extra mile by adding a microcontroller that detects when the output current is low, and turns off the power bank.

The expected use case for these products is, first and foremost, to charge cell phones. I would love to be more broad and inclusive with that, but, no, it's mainly about cell phones. The phone will draw a high current while it is charging, and a low current when it is full, so the power bank detects that and shuts off.

This drives me crazy! These auto-off power banks make it impossible to:

- run low-current loads like gentle ambient lights.
- run arduino or other microcontroller projects that draw less than the minimum current.
- deliberately keep the phone out of [doze mode](https://git.voussoir.net/voussoir/trkpt#doze).
- use an inline switch, or a device with its own power switch.

A couple of quick searches will find you plenty of electronics hobbyists and DIYers who'd rather their power banks not turn off:

- /r/usbchardware: [USB powerbanks without "trickle" switching](usbchardware_powerbank.html)
- arduino.cc: [USB battery bank without low current shutoff](arduino_powerbank.html)
- candlepowerforums: [USB powerbank WITHOUT auto off?](candlepowerforums_powerbank.html)
- electronics.stackexchange: [A proper way to stop power banks to turn off, and how to power low-current devices through USB](stackexchange_powerbank.html)
- mtbr: [Power Bank with no "on button"](mtbr_powerbank.html)
- pistonheads: ['Always On' Powerbank without auto standby](pistonheads_powerbank.html)
- /r/homeautomation: [Always on powerbank?](homeautomation_powerbank.html)
- hackernews: [There's no reason anymore that a power bank should ever even have an off mode](hackernews_powerbank.html)

When I look at power banks for sale, the majority that I see have a single-button user interface, where pressing the button wakes up the power bank and displays the remaining charge level. Some brands, but not all, offer a low current mode that disables the auto-off feature, accessed by double-pressing the button, or holding it for a few seconds, etc. The joys of single-button UIs. This only takes effect for a single discharge session, and often comes with the caveat that it will **still** turn itself off after a [few hours](xiaomi_manual.png).

For power banks that don't offer a low current mode, the most commonly recommended solution is to put a resistor across the power bank's output. At 5 V, a 50 Ohm resistor will dissipate 100 mA, for example. That's right, the solution to your low-power project is simply to draw more power! Wow! Some more ambitious problem solvers will put the resistor on a timer so it draws a burst of current just often enough to keep the battery awake and minimize waste. But this still adds a clunky, intermediate dongle to your project.

Some of the very cheap power banks don't turn themselves off at all, and are valuable to the hobbyists. But they usually come from anonymous brands of no repute, which makes it impossible to provide a specific product recommendation because the brand won't exist in six months, and barely exists today. They typically don't even consider "always on" to be one of their selling points, so they don't mention it, which makes it nearly impossible to search a marketplace by keyword.

What I mean is, there are plenty of auto-off power banks that don't mention they are auto-off because it's considered standard behavior; and there are always-on power banks that don't mention they are always-on because it's not considered to be a selling point. The absence of either keyword practically means you have to assume it is auto-off.

One of the very, very few brands that prominently advertises their always-on power banks is [Voltaic](voltaic.html), and they charge a hefty price premium for what is, from this perspective, feature subtraction. The high price is accounted for by other perspectives: they're designed to charge from solar without browning out, they explicitly support charging while discharging, and they're aiming towards business clients purchasing in high volume. But that's not what I was looking for.

If you want an always-on battery, the most likely candidates are the $5 unit from a no-name whitelabeler that was too cheap to include the auto-off microcontroller, or the $50+ unit from the premium B2B IOT market, it seems. There are precious few in the middle, but they do exist, sometimes. I bought [this unit](aliexpress_listing.png) via aliexpress for $19 and now that seller has gone bust, probably because they were falsely using Xiaomi's name or committing other scams. I was desperate.

So far, I haven't even talked about why power banks do the auto-off thing. I don't really know. It's probably because all the manufacturers are putting together building blocks from a small handful of suppliers and someone came up with it and now they're all the same.

Ostensibly it's to save power, and that's the answer people give. Are they referring to the output voltage regulator, drawing some current even when not in use? That's a good point, I wonder what else we can do to disconnect loads when they are not in use.

Artist's rendition:

![Closeup photo of an on-off rocker switch](switch.jpg)

![Photo of the same breadboard from before, this time with the rocker switch inserted in the circuit before the 5 V output regulator.](breadboard2.jpg)

I don't get it. Why do I see hundreds of power banks with the one-button interface, and none with a plain old on-off switch? Is that too 20th century? Even if you leave it switched on accidentally, it will still take weeks or months to self-discharge from the quiescent current. I know this because the always-on batteries I have sometimes go months without use. It's not the same as leaving a flashlight burning in your backpack.

The only other way I can think auto-off saves power is that the device being charged -- remember, as a product designer you should anticipate it could be anything as long as it's a cell phone -- will perform more background activity while it's plugged in. As I mentioned, Android will not enter Doze mode while it detects the charger, and I'd expect iOS to also use charging as an opportunity to do more syncing or network activity or whatever. So, specifically, I'm referring to a device that has reached full capacity and the user has not unplugged it from the power bank yet, so it's using a few extra milliwatts. And that's apparently worth discarding all other low-power use cases.

Some people will guess that the auto-off feature is to protect the power bank's own battery from overdischarge, but this is wrong. Low-voltage cutoff is done by the protection circuit which, ideally, is provided by a dedicated chip immediately in series with the battery. Auto-off also cannot be to protect the phone's battery, because the power bank cannot force the phone to take more power than it wants. Or else, mains-powered chargers would be popping everyone's phones.

A rant about batteries, of all things. I'm sure there are bigger problems out there. But this is simply one example of an annoying and pervasive trend in tech: solved problems becoming unsolved over time due to reduction in user control. Stuff used to be made with buttons and switches so I can decide what it does. Now it is made "smart" so it can decide what it does. A slight change in the product's design can improve the experience of one group of users with no downsides for the other. I am very tired of:

- devices and appliances calling themselves smart devices, where the word "smart" means it does something you didn't ask for because the designers couldn't imagine more than one use case or mode of operation. I want you to do less!

- devices that are non-configurable, non-customizable, and non-openable. I would be totally fine with a DIP switch on the inside of the unit, or soldering a jumper, if only you wouldn't use one-way plastic snaps in its construction!

- single-button user interfaces, their multi-click and hold incantations, and internal state machines taking the place of simple physical toggle switches.

- marketplaces flooded with thousands of whitelabeled copies of the same products, swamping out the few that are actually different.

- feeling dismayed by our failure to do easy things.
