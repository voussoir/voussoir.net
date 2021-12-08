IPFS misconceptions
===================

## Introduction

I am interested in [IPFS](https://ipfs.io/). I don't run a node, but I look forward to seeing the technology grow. I like peer-to-peer networks and hope they make a strong resurgence.

However, IPFS has marketing problems. I am subscribed to /r/ipfs which is inundated daily with posts by people who have clearly gotten the wrong idea about what IPFS is and isn't, and the IPFS homepage hasn't exactly stepped up to clarify the misunderstandings.

## IPFS is not a place you upload to, it's a network you're a part of

> Won't there be hard drive capacity isssues if everyone used IPFS?

> The way I understand it is everyone who opts in to be an IPFS server will download all the content on the web that I browse to, and host it.

-

> Would it be a good idea to make an ipfs mobile app

> They have made a web browser plug-in but I'm wondering if it would be a good idea to somehow make an app for your mobile device that works with ipfs maybe something you could use to sync your contacts but then again to run into the same problem you would need somebody to run the gateway node for you I mean I have 64 gigabytes of storage on my phone but I don't think it is enough to run and ipfs Gateway on there lol I had a computer with a 2 terabyte hard drive and it managed to fill that thing up in less than a week I Can Only Imagine how fast it could fill up 64GB

-

> Any way to get an mp4 to loop infinitely when uploading to IPFS?

-

> After uploading content on the IPFS network and having its relative CID address available, that content and address will never be more removable or editable, correct?

-

> IPFS Soundcloud. How would one upload an audio file to IPFS through the browser?

> I am new to IPFS and javascript programming in general. I am trying to build the barebones beginnings of a "Soundcloud" clone that can live and stream entirely from IPFS.

> I was able to get the streaming working but even after reading documentation, I'm having trouble figuring out how to implement uploading. I know there's a method to ipfs-add a file.

-

> I thought when you upload something on IPFS it is stored across all nodes on the network. What makes it different from centralized services? How to know who are using IPFS that is global and won't get down?

-

> Is it a good idea to store avatars for my project on IPFS?

> I want to use the least amount of money for my project as a challenge so I was wondering if it was possible and is a good idea to store avatars (around 2-8mb) on IPFS and use an API to access them later.

-

> How does ipfs avoid spam and bad actors?

> What if I would try to upload several petabytes of data, what would prevent me doing that to overload the current network?

-

> I heard that any node will host also a bit of other random ones, what can have illegal things. Am I totally safe for using IPFS?

-

> Hey guys I decided to spin up own IPFS node.

> Works perfect in docker 24/7.

> Some questions:

> How permanent are IPFS uploads?

The number one problem with IPFS's public perception is that a huge, huge number of people think that IPFS is a place you just "upload" to, and it'll hold your files forever. People see the word "decentralized" or "distributed" and assume that IPFS distributes your files for you, for free, everywhere.

This is understandable, since most end users are not accustomed to being an equal, active participant in the great glowing mass we call the internet. We are accustomed to interactions between service providers: Google, Apple, Facebook; and service users: us. We upload photos to Facebook and then leave. We upload videos to YouTube and then leave. The internet just runs 24/7 and I don't have to do anything about it.

Most of us feel that 'the internet' is this big thing that is separate from ourselves, managed by far away entities with billions of dollars, which we use and then leave; which we are not a part of. Proportionally, the number of people who have ever hosted a web server or game server themselves and had their friends connect, or transferred files between two devices in their home via LAN IP is dwindling all the time. Recently I explained to someone that a modem connects your house to the internet and your router connects your devices to each other -- and they asked me why you'd want to do that. The word "Internet" means "between networks", and necessarily postdates the smaller institutional- and home-level networks we started with.

You don't even need a domain name to have a website: just run an http server, open your ports, and give your friends your IP. You're live. Welcome to the internet. It's made by people, and you're a people too. You can even run a website [off of a cell phone](https://old.reddit.com/r/androiddev/comments/9lirv0/best_libraryframework_for_running_a_web_server_on/), except that Google and Apple are making this harder all the time in order to groom your Stockholm syndrome.

IPFS is not a place you just upload to and then leave. It is a network you're a part of. You need to download and run the client software, either on your home PC or on a rented server, and allow other people to connect to you. Then you need to *leave it running*, because if you turn it off then of course nobody can get your files. What did you expect.

The selling point of IPFS -- the nature of its decentralization -- is that anybody who downloads your files can seed them to anyone else using the exact same link. The `ipfs://` links contain the hash of the file rather than the address of your computer specifically.

This is the difference between IPFS and the regular HTTP web: if a video gets deleted from youtube.com, it's *possible* someone else in the world made a copy, but how are you going to find that person? If you get lucky, someone will generously reupload it, but it's going to be at a different link. And if their link gets deleted, you need to find another one. Over and over again. With IPFS, the original link works as long as a single person in the solar system is willing to keep it alive.

There are companies or entities known as [pinning services](https://docs.ipfs.io/how-to/work-with-pinning-services/), who will host your files on IPFS for you if you pay them. However, even this is not "uploading to IPFS" any more than uploading a file to Amazon S3 is "uploading to The Internet". The agreement to host the file in exchange for money is between you and the service provider. IPFS the protocol and the IPFS community at large aren't responsible if that host goes out of business and stops hosting your file.

## "But why would strangers want to help me host my files?"

> Who pays for the storage on IPFS?

> I keep coming back to the same question, who pays for the storage space. Like I can create a local node and upload my draft-version2-history report but why on earth would that be getting replicated across the network. It's great for me because now I can globally access it, but who would want to store that file solely for me who didn't pay anything for that replication?

-

> What stops ipfs from becoming a tragedy of the commons?

> I look at my own hard drive and half the contents - perhaps most - is ephemeral, intermediate, or junk. Sometimes I'm forced to sift through Everest-sized piles of digital rubbish to reclaim disk space, though in the process I inevitably lose some of the baby along with the bathwater.

> Now imagine all that cruft on a planetary scale, petabytes of obsolete memes, shopping lists, programs in the process of being developed, temporary files -- and billions of idiots who pin them all someplace else as a free cloud backup.

> If I run a node on my home server, how many terabytes do I reserve to replicate an infinitely expanding pin list, assuming I only have to host the content I offer or have previously downloaded?

> > What makes you think you can just "pin them all some place else as a free cloud backup"? Most pinning services charge you per GB*month (or equivalent) for the things you pin. If you stop paying, they stop pinning it.

> > > I just want to be sure I understand the objective -- is it fundamentally a gimmick to part rubes from their crypto, or a genuine innovation in distributed storage?

> > > > ipfs has nothing to do with bitcoin. Its just an alternative to http. its a way to share data that is not inherently centralized.

> > > > > I expect most or all cluster providers will require or at least allow payment by means of their preferred wankcoin, don't you?

-

> What's the difference between storing files on AWS cloud and IPFS?

> From this subreddit, I learned that IPFS does not store your files permanently even if I pinned them. If so, why should I store on it? So that my files can't be hacked? So that in case Amazon goes bankrupt I still have my files? But if I use a pinned service like Pinata.cloud, they might go bust too.

-

> If I host my own node, how to ensure that the file I uploaded goes into my node?

> I learned that files are not forever on ipfs and the best way to make them permanent is by hosting my own node. So, if I do host one, do I just redirect my files into my node or will ALL nodes have ALL files from around the world from everyone?

> Cos otherwise, if all my files are only in my node then what's the point of decentralization.

-

> What's the point of IPFS? Why wouldn't I just host the files myself?

> From what I understand, IPFS isn't private, your IP is public, and nodes only host the files they want to host.

> Since most people only care about their own stuff, most files will be hosted from a single machine with a public IP.

> Why wouldn't I just host the files from a single machine with a public IP?

> What is IPFS actually providing?

> > I am grappling with a similar question, how can we incentivize fellow nodes to pin our data? Is there any quid pro quo proposal or protocol in place?

-

> Okay so if no one pinned anything and just hosted what they host then it would be just like the internet without IPFS. So what incentivises people to pin?

> > Incentive seems to be one of the fundamentally unsolved problems for decentralized storage. Not only does hosting content need to be profitable, but there needs to be systems in place that make sure that users aren't just hosting the same popular content that gets the most traffic and dumping less popular content because it isn't generating the same amount of revenue.

This misconception often stems from the first, that IPFS is a giant magical hard drive in the sky where other people will hold on to your stuff for you forever, so naturally there must be some big incentive for them to do that. "What's in it for me?" is the only language we understand. That was the idea behind [Filecoin](https://filecoin.io/) -- it gives members a financial incentive to share their storage space with the network. As it happens, Filecoin operates on a [completely separate peer network](https://github.com/filecoin-project/specs/issues/1191#issuecomment-704065968), unreachable by the regular IPFS client, since they need to keep their accounts payable in order. Yet, people conflate Filecoin with IPFS itself, and assume that all IPFS involves the use of Filecoin or other payment, because they can't fathom what sort of incentives exist besides financial ones.

There is no "push" mechanism in IPFS. There is no forcing people to take a copy of your stuff if they didn't specifically ask for it. From the IPFS homepage:

> Each network node stores only content it is interested in.

That's right, idiots. Nobody's going to help you replicate your history book report for the same reason that they won't let you put your lawnmower in their garage after your garage gets full. They're not interested. This shouldn't be surprising.

This is related to the previous idea, that people are only familiar with online services backed by faceless corporations. It's difficult to imagine that the system is made of actual people and you have to make it worth their while to download what you're sharing.

That's the magical effect of money, of course: people **will** suddenly become interested in your homework assignments and lawnmowers if you pay them to be. But in the absence of the financial incentive, you are left with the fact that nobody else is interested in your random junk files.

For many of these people, the line of reasoning stops there. If the network won't host my stuff for me for free, it's pointless. Ok, bye. Meanwhile, the people who generate valuable data that is interesting and desirable to others will see their files propagate. If NASA started advertising CIDs for original moon landing footage, they'd get plenty of help replicating it.

Let me specifically address the point about "strangers". Because IPFS is free and global and public, any stranger can download a file you're hosting and become a second seed, and that's very kind of them. But IPFS as a protocol is agnostic to this. IPFS can very well be deployed in an enterprise setting where no one is a stranger to each other, and they don't need financial incentives to host each others' files because they're working for the same organization. A website operator like Google could serve their javascript or image assets over IPFS, and replace their traditional CDN servers with IPFS nodes that are programmed to replicate each other. This might sound pointless -- replacing one kind of server with another -- but it removes the necessity of DNS management and allows them to just dump IPFS nodes all over the place and let the protocol balance things automatically. If random strangers want to pin Google's assets, they can do that too, but Google would always know that keeping their files alive is their responsibility. They would never *rely* on strangers' pins when the functionality of their website is at stake.

Plus, if a team of researchers in Antarctica (or on Mars) are accessing google.com, only a single one of them needs to get the assets via satellite connection and then they can seed it to the rest of the camp over a faster local network. The point of IPFS is not "strangers keep my stuff", it's "people sharing files" for whatever reasons they need.

## IPFS is not anonymous or "dark web"

> Why do we need decentralised/censorship resistant communication platforms when they already exist on darknet?

> they probably aren't decentralised but they do the job

-

> Can my uploaded IPFS files be traced to get my IP address?

> I'd like to use IPFS to share my files with others on Discord, however I'm concerned someone might grab my IP. Is this possible, and if it is, how do I protect myself from being attacked?

-

> I love the idea of decentralized file storage, but how would IPFS prevent something like the distribution of child porn or hate speech?

-

> What is stopping someone from creating a child porn IPFS website?

-

> What are the ways in which ipfs prevents piracy?

> I was thinking that all the successful decentralized networks today are highly utilised for piracy which harms the reputation of the technology. So what are the ways in which ipfs prevents that and what are the disadvantages of those implementations?

-

> What Prevents IPFS from becoming the next uTorrent?

> I believe this a problem that IPFS will face as in any peer to peer network, piracy is a big issue.

> I propose that we make a "hash blacklist" which will have a list of hashes which are illegal. Though we would have to build a proper system around it and make sure that not any or every hash is added to it, kinda like a dmca takedown.

-

> I want to join the IPFS, but I'm concerned about ending up with illegal content on my computer somehow. I tried to find information about this on the web but haven't been successful, so I thought I'd ask here.

> I don't want illegal movies, music, etc., but I'm especially concerned about illegal sexual content like child porn. Having even traces of that stuff on your system could be disastrous. So, if I get involved in the decentralized web, and particularly with IPFS, how do I protect myself from illegal content?

-

> What stops people from distributing illegal copies of different types of media?

> (1) If I were a bad person and started uploading pirated copies of movies or games, what stops someone from doing this?

> (2) If I have the legal rights to a movie and I found an illegal copy on IPFS for free. How could I prevent this from spreading; or stopping this illegal activity from happening? I guess this wouldn't be possible as the whole point is to spread data around so people can download it even if the original uploader is offline.

You can find lots of posts from people who are worried about illegal or unsavory things happening through IPFS, and much of the messaging surrounding IPFS does describe it as "unstoppable" or "censorship-resistant" or "can't be taken down". There are a couple of angles we can get at here depending on your concern.

Some of these people believe that IPFS is a place you upload to, or that all nodes assist with the hosting of all files, which leads them to believe that by running an IPFS node they will wind up with illegal files on their computer. There is precedence for p2p networks where all peers help host all files, like [GNUnet](https://en.wikipedia.org/wiki/GNUnet) and [Freenet](https://en.wikipedia.org/wiki/Freenet), but this is not the case with IPFS. You only host what you visit and pin.

On the other hand, some people might just feel generally uneasy knowing that pedophiles can use new tools like IPFS to share their material, and they wish the system had some innate kind of block against that.

From a technical perspective, how do you expect the IPFS software to know whether a file is being blocked for a "good" reason, like preventing the spread of child pornography, versus a "bad" reason, like preventing the spread of Tiananmen Square photos? Both of these situations are basically the same: it's material that people are not allowed to look at. It just depends who's doing the allowing and disallowing in your jurisdiction. Should there be a human-curated ban list built into the default client? Curated by people from which country? The client is open source anyway so they'd just compile the program without that. It just doesn't work. Using technical solutions to address social problems rarely does.

You'll also notice that knives do not have special handles that prevent you from committing murder, beer bottles do not prevent you from driving drunk, cash does not prevent you from buying drugs, pens do not prevent you from forging signatures. The tool is agnostic and the crime is up to you.

IPFS is nothing more than a protocol. It is a language that two computers speak when they talk to each other. There is no sequence of words in the English language that will instantly alert the police when I say them, no matter how bad the words are. Likewise, there is no kind of file that will cause IPFS to alert the police.

However, (here comes the point of this section), IPFS is not anonymous. When you run an IPFS node and people connect to you, they're connecting to your public IP address assigned to you by your internet service provider. If the police catch wind of any CIDs for illegal files, they'll just check out which IP addresses are sharing that file and try to pin down the owners of those IPs.

People have begun to conflate decentralization with anonymity, which is not correct. As I described earlier, companies decentralize their CDN servers because it improves latency for each region, but they are certainly not anonymous. Tor, by contrast, aims for anonymity by never connecting two peers directly to each other, instead routing the conversation through several intermediate nodes.

If a journalist in China tries to publicize the Tiananmen Square incident, the Chinese government might discover it and try to shut that person down. But, because a single `ipfs://` link can work anywhere in the world, that journalist only needs a single friend outside of the country to also pin the file and make it available globally, then the journalist can turn off their node. Other countries like USA will not prosecute a person for hosting the photos. (Realistically, the journalist should transfer the file to their friend through a separate, encrypted channel, not IPFS, in the first place.)

As with other technologies, like bittorrent or even just http, you could gain anonymity by running the program on a far away server which you rent (careful that your payment method doesn't reveal you), or by diligently routing your PC traffic through a VPN.

When it comes to child pornography or pirated media, the IPFS situation is not much different than what we have now. If the hosting node is located in a region with lax laws, or there is no information linking the node to an individual, then there's no difference whether it's an IPFS node or a bittorrent client or emule or an HTTP website. The person who wants to download the files should prepare for the possibility of connecting to a honeypot source, and they probably should remove the file from their IPFS node afterward so it doesn't seed back to anyone else. Again, this is not much different from what we have now.

From what I've seen so far, the censorship-resistance claims of IPFS are predicated on the idea that you're first able to get your files out of the jurisdiction that wants to censor them and into a jurisdiction where they're permitted. IPFS does not provide any more secrecy than bittorrent does, and if the whole world is after you, IPFS isn't a magic shield.

Now, one of those comments I quoted made a great point, which is that the reputation of the technology as a whole can be ruined if it's known for piracy or criminal material. When people give a demonstration of how to use a bittorrent client, they always show how to download a Linux release or Big Buck Bunny, because that's the only thing they can think of that isn't a copyright violation. Many people think that torrents are illegal in and of themselves. So far, IPFS hasn't become a popular piracy tool to my knowledge, and all of their messaging centers around webpages. The fact of the matter is that the regular HTTP web already carries both copyrighted and illegal material, but new protocols are subjected to higher scrutiny and criticism than the incumbents just as a matter of course.

## IPFS's copywriting is bad

Am I doing a good job so far? Let's compare what I've written with what appears on the IPFS homepage to see how poorly they communicate their project to newcomers. All of the statements they make are technically correct, but they only make sense if you already know how IPFS works. If you don't...

> **Today's web can't preserve humanity's history**

> The average lifespan of a web page is 100 days before it's gone forever. It's not good enough for the primary medium of our era to be this fragile. IPFS keeps every version of your files and makes it simple to set up resilient networks for mirroring data.

To the layperson, this implies that 'the network' stores your files forever once you put them in. It does absolutely nothing to address the mindset that most internet users have, which is that service providers and service users are clearly delineated.

Have you heard the phrase "guns don't kill people, people kill people"? Well, the network doesn't store anything, it's the people that store things, and IPFS is the network by which you can reach them. But people can get bored of holding on to a particular file and delete it to make space for something else.

Are you still holding on to copies of all the webpages you read 100 days ago? No? Why not? Don't you want to contribute to the permanence of all those pages? I clutch my pearls in your general direction. See, it's easy to sit around fawning over IPFS for being 'the permanent web' until you realize that permanence isn't actually a guarantee of the protocol. Permanence is a *possibility*, only to be realized by the collective choice of individuals to host the material they believe is important. And unless you're doing your part to preserve and host the files you think are important, you don't have much ground to stand on when you find that other people aren't keeping the stuff you want either.

> **Archivists**

> IPFS provides deduplication, high performance, and clustered persistence — empowering you to store the world's information for future generations.

Similar to the previous one, the word "provides" here gives the wrong impression to people who approach this page with the mindset that IPFS is a web storage service like DropBox. I'm not saying that's the only possible interpretation, but it's a very common one and IPFS should write more clearly to disambiguate.

"IPFS provides me with high performance storage? Sure, I'll take it! What? No, I don't want to actually *run* anything..."

I will give them credit for "empowering you to store", giving agency to the reader. Just make sure you use the power once you've got it.

> **Blockchains**

> With IPFS, you can address large amounts of data and put immutable, permanent links in transactions — timestamping and securing content without having to put the data itself on-chain.

This doesn't mention the fact that the link is only good as long as someone keeps the file. When everyone assumes "oh, the network's got it, I can delete mine", you'll suddenly find there's no copies left. By omission, this implies that IPFS just holds things forever.

> **Here's how IPFS works**

> Take a look at what happens when you add a file to IPFS.

Wording here could be changed to "when you add a file to your IPFS node" to remind that you're processing your own files; this isn't happening remotely on some kind of IPFS service.

> Your file, and all of the blocks within it, is given a unique fingerprint called a cryptographic hash.

> IPFS removes duplications across the network.

This statement is poorly worded. I get it, because two identical files, or two files containing some identical blocks will produce matching hashes, so you don't get "duplicate" links and mostly-same files will sit better in the cache. But understanding the details of this sentence requires much more specificity than is given, so it is weirdly out of place.

In the context of "what happens when you add to IPFS", removing duplications sounds like the opposite of what the reader wants -- high availability and low latency is achieved only after many duplicates of the file are spread around the world and shared by many peers. By contrast, it is the centralized file hosts like Google Drive who benefit most from deduplication: if two people upload the same file to GD, Google can just store it once and let both people download it, saving themselves disk space.

Furthermore, this statement uses third-person voice for both IPFS and "the network", which is a double-whammy against the agency of the reader. It sounds like a remote service.

> Each network node stores only content it is interested in, plus some indexing information that helps figure out which node is storing what.

Should be reworded to "You only store content you're interested in" to remind that IPFS is not a remote service and give agency to the reader.

> When you look up a file to view or download, you're asking the network to find the nodes that are storing the content behind that file's hash.

This is weird. "Asking the network to find the nodes"? That's like asking the wave to find the water. What is the network if not nodes? And the sentence structure reminds me of the dog that killed the cat that caught the mouse that ate the cheese.

Should be reworded to "you're asking your peers to find who has a copy of that file".

> **Content creators**

> IPFS brings the freedom and independent spirit of the web in full force — and can help you deliver your content at a much lower cost.

The IPFS copywriters should be aware that approximately 100% of today's content creators are accustomed to uploading their videos, music, photos, and blog posts to online ad-supported services without having to pay to do so. You probably should let them know that hosting their creations on IPFS requires them to run a node or pay a pinning service, and that the decentralization only happens after they have fans who are willing to store and pin their works.

IPFS's homepage is bad. I wonder if they are intentionally toeing the line with their messaging, since the implications are always more grandiose and fabulous than the reality. I've said it once and I'll say it again: sqlite.org has a front-page link to [When to use SQLite](https://sqlite.org/whentouse.html) which also plainly describes when **not** to use it. IPFS doesn't do this because they're [not as chad as SQLite](/writing/sqlite_what_a_hunk). Can't blame them on that one. No one is.

Clearly, IPFS's messaging, and the messaging from crypto nuts who advocate IPFS without really knowing what it is either, has led people to believe that IPFS is a giant decentralized cloud storage system that may or may not be free to use. In my opinion, the copywriters need to turn this ship around and make it clear that IPFS is not a magic dumping ground for your random personal junk to be replicated globally. It's a peer-to-peer network that you need to actually participate in if you ever want to get anything done.

Welcome to the internet.
