[tag:3dprinting]

Phone camera holder
===================

## Introduction

This project did not fully achieve the results I was hoping for, but I'm going to post it anyways in case it gives someone some ideas.

Using my cell phone as a camera sometimes requires an awkward grip, which I'm sure most readers are already familiar with performing. One-handed shooting is especially precarious as I hold the phone between my pinky and index finger while pressing the shutter with my thumb. When capturing video, there is the added difficulty of keeping my palm away from the microphone hole. These are some of the problems I wanted to solve.

[![](thumbs/phone_1.jpg)](phone_1.jpg)

[![](thumbs/phone_2.jpg)](phone_2.jpg)

The other problem I wanted to solve is footstep motion and jitter when filming videos. My phone does digital image stabilization (a post-processing effect, unlike optical image stabilization which is a hardware effect), but I find that every time I take a step, my video goes blurry for a few frames, as if I am he-fi-fo-fumming everywhere I go, even when I try to tread lightly.

If you search the internet for "diy camera stabilizer", you'll find various devices that hold the camera between two handles. The distance between the handles reduces the high-frequency movement from your hands, at least in the roll axis. This two-handle design was my inspiration.

## My design

This is what I came up with:

[![](thumbs/model.png)](model.png)

[![](thumbs/slicer.png)](slicer.png)

[![](thumbs/holder_1.jpg)](holder_1.jpg)

[![](thumbs/holder_2.jpg)](holder_2.jpg)

The phone snaps in with a friction fit, and there is a lip around the front face to hold the phone still. Four notches are taken from the sides so you can bend and twist the entire holder to release the phone. The handles are raised in the Z axis to allow for a charging cable. There is a hole in front of the microphone to let the world in.

The size of my holder was limited by my print bed, and I printed it at a 45 degree angle.

My dimensions were not quite perfect, and I added some blue tape to act as shims and get a good fit. It is very important that the phone be held firmly, because if it rattles around inside the plastic, the noise will pick up very loudly on the microphone and ruin all of your audio.

Here are some of the good things about this design:

1. I can hold it quite sturdily and am mostly confident the phone won't fall out on its own, even when pointing it straight up.

2. It is much easier to take photos one-handed.

3. When shooting video, I can switch between my left and right hand more easily. Without the holder, the left hand posture must not block the camera and the right hand posture must not block the mic. With the holder it is more symmetric and easy.

4. The handles look like car spoilers.

[![](thumbs/holder_3.jpg)](holder_3.jpg)

[![](thumbs/holder_4.jpg)](holder_4.jpg)

[![](thumbs/holder_5.jpg)](holder_5.jpg)

And here are some of the bad:

1. It is difficult to achieve a perfect friction fit. The case must be tight enough to prevent rattling and shifting noise, but not clamp down on all the buttons, and still be easy to release. As it is, I had to cut a relief hole over the power button. I wonder if I could achieve more with less -- instead of wrapping the whole phone in plastic, maybe four or six little grabbers could hold it at each corner, so they can be designed with a very tight grip without interfering with anything else.

2. This holder really didn't solve the thundering footsteps problem. I think an important factor in camera stabilization is weight. A heavier device has more inertia and resists small vibrations. Since I am printing plastic, the holder adds very little weight.

4. The whole thing looks like a serving tray.

It might also be fun to make a holder that looks more like a traditional camera. The phone could slide in from the top and wedge between some fabric to get a gentle, tight grip.

[![](thumbs/idea.png)](idea.png)

Though this is surely pointless skeumorphism, and is the opposite of what I just said about not wrapping the phone in plastic.

## Download

This design was made for an LG G8X and won't be suitable for any other phone without modification. Some parts of the design are hard-coded, like the position and size of the microphone hole. Nevertheless, you can download it here:

[phonecamera.scad](phonecamera.scad)

[phonecamera.stl](phonecamera.stl)
