[tag:life]

Advertising
===========

## Introduction

Every once in a while, someone will ask me "have you seen that commercial about..." and my response is almost always "no". I haven't seen that commercial. I do my best to not see any commercials.

Throughout this article I will use the term "adblock" as a common noun, not a proper noun. I am not referring to any particular adblocker and [certainly not the one by the name of Adblock](https://old.reddit.com/r/privacy/comments/bvj5nj/use_ublock_origin_not_adblock/) or [Adblock Plus](https://news.ycombinator.com/item?id=12487307). Today, [uBlock Origin](https://github.com/gorhill/uBlock) is widely accepted as the best adblocker, but this will of course change [with time](https://en.wikipedia.org/wiki/Ozymandias). This article contains some external links. Make sure to install an adblocker before clicking on any of them.

I will mostly be talking about advertising over the internet, because that's the medium where I have the most knowledge and experience. I don't watch TV or listen to the radio. There are too many ads there.

The URL for this article is `advertixing` because when it was called `advertising`, the inlined images were being adblocked by `/advertising/*` URL pattern matchers. Ha.

This article has been a work in progress for a very long time, so some references to supposedly current events may seem a bit temporally challenged.

## Types of advertisements

In some sections of this article, I criticize the advertisers who create ads, and in others I criticize the publishers who publish those ads in exchange for money. The incentives and issues surrounding each are different and I'll try to make it clear which one I'm referring to, but in my blind rage I'm sure I'll switch topics without mentioning it. Let's start by defining what we're dealing with.

I find that advertisements can be separated into three broad categories by their mode of propagation:

1. **Sponsorship**, in which a product seller pays a publisher to publish ads about their product. This is a very traditional and straightforward kind of ad.

    This includes the ads you see on TV, radio, magazines, newspapers, web sidebars, headers, popups, in apps, as [product placement](https://en.wikipedia.org/wiki/Product_placement), and as [bloatware](https://en.wikipedia.org/wiki/Pre-installed_software). This does not include first-party upsells or encouragements to upgrade to the premium edition of something you already have.

    Sponsorship advertisements might be explicitly labeled, or they might be hidden amongst regular content so that you don't realize you're being advertised to. The second is more lucrative though FTC regulations against them exist.

    ![](sponsorship.png)

2. **Spam**, in which a product seller self-publishes ads for their product in spaces where ads don't belong and without getting permission from the owner of the space.

    This includes uninvited email and phone calls and private messages, self-promotional forum posts, SEO keyword abuse, fliers stuck under your windshield wipers, door-to-door salesmen, and solicitors outside grocery stores.

    Colloquially, one might include first-party upsells, because they're annoying and feel like spam, but I think it depends whether they intrude into your personal space, such as a spam email appearing in your inbox, or occur within the first-party's space, such as a banner on their webpage. You are allowed to always hate upsells but that doesn't mean they are always spam.

    Most spammers are cowards. They won't own up to their actions. They'll say "I'm not spamming, I'm just letting you know about this cool new thing".

    ![](spam.png)

3. **Chumps**, publishers who discuss a product and give it ad-like publicity without compensation from the seller because they think they can use it to attract an audience of their own, usually because the product is currently a hot topic. This is different from word of mouth because the chump isn't actually passionate about the product, and may not even have it. The chump probably gets their income from other sponsors unrelated to the product in question, or by selling their own product.

    This includes bloggers, reviewers, and opinionators discussing new products, press releases, scandals, speculation, leaks, and hype. Product sellers can intentionally create scandals or leaks to get free advertising from chumps. Chumps will often regurgitate basic product information instead of forming their own opinions. Also keep an eye out for product reviews released too quickly after the product's launch, which indicates it was a sponsored job or the reviewer simply spent no time with it. Check out [this MKBHD video](https://www.youtube.com/watch?v=Ns8ydpZ5-4o&t=8m03s "Escobar Responds! A PSA (2020-05-29)") where he calls out chump media outlets giving free attention to a certain scandalous device, which I am now ironically propagating by showing it to you. inb4 [MKBHD also speculates](https://www.youtube.com/watch?v=bATUW8G2ONE "iPhone 12: What to Expect! (2020-07-07)").

    ![](chumps.png)

    I feel that I need to give a concrete example of chumping to make my definition clear, so I'll continue with MKBHD though normally I don't want to speak ill of individuals [footnote_link]. He releases lots of videos after spending only a week with a product, and the release of the video is often clearly aligned with an embargo, i.e. the companies are using him as part of their scheduled marketing. These products attract viewers to his channel because they are new and hot, but he isn't getting paid cash by the likes of Samsung (probably) -- he performs ad segments for [other sponsors](https://www.youtube.com/watch?v=vax8FCuQUsE&t=2m46s "Galaxy S22 Impressions / sponsored by Morning Brew"). The end result is that the viewer is being double-advertised to: they get to hear the product's basic specsheet read aloud to them with only superficial opinionation, then hear from another sponsor on top of that.

The majority of this article deals with sponsorship advertisements because they are the most systemically accepted of the three. Consider:

- **There's as not much to say about spam**. Everybody already hates spam. This article is about systemic problems with advertisements and spam is built upon the abuse of systems by definition. Discussing the problems with spam is like discussing the problems with homicide. It's not systemically accepted but occurs anyway. Spam will exist as long as ~~[there's two people left on the planet](https://www.youtube.com/watch?v=9NZDwZbyDus "Meet the Sniper")~~ popular systems and spaces exist. Spam can only be countered with diligent policing by the owner of the space, or by convincing the spammer to repent. Good luck with that. Sponsorship, on the other hand, exists comfortably within the system. I dedicate [one section](#the_problem_with_spam_your_life_as_an_arms_race) to spam but otherwise I don't have much to say about spam except that I hate it too.

- **Chumps usually rely on sponsorships to do what they do**. There is not much need for me to discuss chumps because if we could eliminate sponsorships, we'd bring the majority of chumps down at the same time. By my definition, chumps are not actually interested in the product, they only talk about it to get attention. Without sponsorships to make chumping worthwhile, most chumps would quit. Only those who sell their own product would continue, and I believe that to be a minority.

As such, of these three kinds of advertisements, sponsorships are the ones that I find most worth writing about.

**Glossary**:

- Product seller, advertiser: People who make and sell some product or service to customers as their main source of income.
- Publisher: Websites, TV channels, radio stations, newspapers, app developers, storefront owners, social media creators et al. who create media or own a space. For my purposes this will also include performers, racecar drivers, and other personalities who promote a brand, even though we wouldn't normally call them publishers. The space they are selling is their body, image, and reputation.
- Sponsor: A product seller who pays a publisher to show ads for their product in the publisher's space.

[footnote_text] This paragraph applies to the majority of hot-topic reviewers, I just don't watch very many of them. Also, the only reason I'm able to criticize his work is because I still watch what he makes. I like that he does get into [industry critique](https://www.youtube.com/watch?v=a6zvvlrd-jw "The Electric Car Pre-Order Problem") and [Youtube critique](https://youtu.be/1Cw-vODp-8Y "YouTube comment impersonation spam") from time to time, but I'm sure the chump videos are better at paying the bills.

## The damage of advertisements

### The basics of capitalism

Capitalism is a complicated topic. The core principles are pretty simple and don't sound inherently malicious, at least to me. Sellers try to sell for the highest price they can, buyers try to buy for the lowest, and everybody either strikes a deal they're satisfied with or goes home empty-handed. Beyond the essentials of food, water, and shelter, the human as animal doesn't technically need very much, and the worst that can happen in most transactions is disappointment.

Sellers do research to learn buying habits, buyers do research to learn of alternative sellers and price points. Sellers don't necessarily need to have the absolute highest quality product on the market, they just need to hit a good quality-per-price ratio, or value, to accommodate different segments of the market: some buyers are professionals who need the best quality tools and will pay a lot for them, other buyers just need something that works well enough.

When a person decides to start selling products, they start from a position where nobody else knows they exist. Sellers advertise so that they can enter the buyer's decision-making process, and if they're better than the competition they'll rightfully win the sale. Competition drives sellers to innovate, lest they stagnate and be undercut or outperformed by new sellers. The result is a continuous progression of higher quality products at lower prices, and a steady churn of advertising along the way.

If I lived in the era where advertisements were barely more than hand-painted signs like "Visit Farmer John's farm for some tasty corn", I wouldn't mind them very much. It's fair to say that if Farmer John didn't make the sign, I might not know I could buy corn from him. His corn may in fact be the best in town, so I'll be glad to have learned of it. When I watch movies or see pictures of the wild west, with towns popping up along unpaved roads, I am sometimes jealous of how simple their economy seems. They weren't blasted with advertisements over radio and television and the internet, they heard from their neighbors and whoever came through town.

![](buck_and_the_preacher.jpg)

Then again, this is exactly when [snake oil](https://en.wikipedia.org/wiki/Snake_oil) entered our vernacular, so now I'm doubting myself about that!

Indeed, it seems that these basics of capitalism do "work", in the sense that right now I can buy a computerized internet-connected device with only a day's wage, which is truly a feat of humanity. Products improve and prices drop. So although I hate advertisements as they exist today, it's hard for me to say that the deepest, fundamental notion of advertising is inherently malicious. It is not wrong for a furniture maker to want to sell his furniture.

You can consider this article to be a Capitalism sequel to my [Insurance](/writing/complicated_topics_insurance) article: the primordial elements of Capitalism seem reasonable, but the current state of affairs is objectionable. Maybe there is a level at which advertising can be called a force for good. But things change when we reach the scale of multi-billion dollar global companies and their ads, and they've ruined it for everyone.

![](sonic.jpg)

### Breakdown of conventional incentives & distortion of metrics (& clickbait)

According to the basic principles of capitalism, sellers should try to sell high quality products because the only way to get the money out of the customer's pocket is to have the best quality-per-price ratio on the market. Capitalist competition is grounded in this. When a company makes its money through goods-for-money transactions, we'd expect them to try making a good product.

But that's hard :(

What if you could just skip the customers? What if the money could come from somewhere besides the customer? By displaying a sponsor's advertisement alongside your product, you can earn more money without having to make your product better. You might be able to reduce the price of your product to attract a wider range of customers, netting overall higher sales. If the sponsor pays you enough, you might even be able to offer the product to the customer for the irresistible price of *free*. And if it's free, then the quality-per-price ratio becomes a division by zero and the fundamentals of capitalism implode. Suddenly, all levels of quality are functionally equivalent. The quality of the product is now irrelevant, detached from the means of income.

If the product seller wants to increase their income, increasing the quality of the product won't help anymore. All they can do is try to show the sponsor's ads to more and more people. That means the seller has just pivoted their entire business model away from creating their actual product towards reaching more eyeballs. This shift is much bigger than most realize -- reaching eyeballs is an entire industry of its own: it's called the media. Whatever you thought your business was can go right out the window, because you're a media production house now and you're competing with the likes of Hollywood in the quest to reach more eyeballs.

You might be thinking that the quality of the product still comes into play because if two competing products are both free-with-ads, the customerbase will still gravitate towards the better one, thus rewarding it with more sponsorship money and longevity. The end result could be just as if the customers had paid for it themselves, just [using their eyeballs instead of their wallets](https://www.youtube.com/watch?v=50R21mblLb0 "The Attention Economy - Will Schoder").

There are some cases where this doesn't work at all because of network effects or surrounding ecosystems. Users don't want to join the most technically superior social network, because their friends are on the old one. Users don't want to switch to the most technically superior spreadsheet tool, because there are lots of video tutorials about the old one.

There are other cases where it does work -- but only briefly -- because the better product is coming from a young and idealistic company that hasn't fully realized the consequences of their recent pivot into the media production industry. Young companies, especially those with angel investors, can undercut the incumbents because they're willing to operate at a loss in an attempt to fast-track their market share. But when it comes time for them to start returning on their investments, they realize they need to start recouping their costs via sponsorships and they become just like the incumbents they destroyed. See how imgur.com took over the image hosting space with their easy UI and straightforward hotlinking. Now, they are "Your upload will resume after this ad, or press ESC", impossible to visit hotlinks without getting redirected to the webpage, pushing you to download the app. Like ImageShack before it, Imgur has gone downhill and is ready to be replaced by a new starry-eyed image host destined to repeat the process. Some day, Imgur will die, and its in wake will be millions of image links that no longer work. Free-with-ads products live on a treadmill and the entire internet suffers for it.

[Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law) says "When a measure becomes a target, it ceases to be a good measure". We've all seen this: students who change the font size on their essay to 12.5 pt so they can hit the minimum page requirement more easily; programmers [closing issue discussions](https://news.ycombinator.com/item?id=28998374) to keep the issue count low; Youtubers who fluff up empty ideas into 10+ minute videos for algorithm [favorance](https://www.youtube.com/watch?v=Gi6FcI2wFrw); entrepreneurs who cash in on [dead-cobra bounties](https://en.wikipedia.org/wiki/Cobra_effect) by breeding more cobras to kill. People in general are very adept at exploiting these kinds of opportunities and, as [game theory](https://en.wikipedia.org/wiki/Game_theory) will tell you, it'd be silly not to.

See [cost per impression](https://en.wikipedia.org/wiki/Cost_per_impression) (CPI). An Impression is when a person sees an advertisement, and the CPI is the dollar amount the sponsor pays the publisher for those. And you better believe that for the publishers, increasing impressions can easily become the top -- or only -- priority. Every day, the publisher has to choose between improving its product or finding new ways to reach eyeballs for its sponsors. One of these has direct financial incentive and the other doesn't. In order to increase the number of impressions, the publisher must increase page visits, video views, minutes spent on site, density of advertisement amongst regular content, etc. Attention is turned towards questions like:

- How can we keep people coming back?
- How can we make them stay longer?
- How can we make them share with their friends?
- How many ads can we show them before they get too annoyed and leave?

The answers to these questions are usually along the lines of:

- Add an "infinite scroll" to reduce the friction of staying on site.
- Use enticing thumbnails and hero images to bring attention to content that can't otherwise earn it on its own.
- Promote harmless, easy, cute, emotional, sexy, and, above all, Like-able content over serious, contemplative, or deep reading.
- Cater to the lowest common denominator so that every piece of content can reach a maximum number of eyeballs instead of wasting time on small audiences.
- Outrage, scandals, and exposés are all good too, as long as they are easy and shallow and free of nuance, because people [click on more things when they're fired up](https://www.youtube.com/watch?v=rE3j_RHkqJc "This Video Will Make You Angry - CGP Grey").
- Hide advertisements within the real content as much as possible.

It doesn't matter if you're enjoying yourself or hating every minute of it, just as long as it's a lot of minutes. This is the origin of clickbait.

Businesses love to willingly fall into the Goodhart trap of maximizing engagement and eyeball reachitude because they love seeing pretty graphs that climb every quarter. The other metrics -- the ones that are hard to graph -- get ignored. Metrics like:

- Are we bringing people something they can't find anywhere else?
- Are we staying true to the vision that we started with?
- Are the users who contribute the most to our community going to stick around?
- Do people respect us?

I will reiterate because it is so important: when a product is free with ads, the fundamental rules of seller competition under capitalism are subverted. The need for a quality product becomes zero, replaced by a need to drive impressions at the cost of anything else.

The software industry is notable for its focus on metrics since it's so much easier to track digital actions than real-life actions [footnote_link], thus metrics are much easier to collect and deify. This is to the detriment of product quality and long term consistency. Engineers (or their bosses) will pick some specific [metric](https://en.wikipedia.org/wiki/Performance_indicator) to optimize, beat the hell out of it, and pat themselves on the back until-- Wait!, look over there!, we should be optimizing for this other specific metric instead! Look over there!, Apple is doing it this way now! At every step of the way there is a delusion of climbing towards some peak quality or efficiency, when actually it's just going up and down a bunch of separate peaks in a mountain range. I wonder how much is deliberate by engineers who want to stick it to their dumb managers and get a fat paycheck for essentially wasting time, and how much is really, earnestly believed internally. Either way, the user is the guinea pig who has to deal with a product that continues to change and re-prioritize for no good reason.

[footnote_text] At least until face and gait recognition in store security cameras become universal.

### Manipulation & asymmetric information & budgets

We would all like to think that we're immune to the manipulative effects of advertising. That we make our buying decisions only after comparing our options and coming to the best conclusions. That we can see right through the doctored footage, fake food, irrelevant celebrity endorsements, industry buzzwords, and [hopelessly incompetent baboon actors](https://old.reddit.com/r/wheredidthesodago).

What's the longest you've ever spent thinking about a purchase before making it? Try to remember a time when you wanted to buy the most perfect option that would match your needs exactly. Maybe it was a cell phone, or vehicle, or pair of hiking boots. Remember how many searches you did, how many alternatives you compared, how you divided the price by your hourly wage to get a feel for how many work-hours you were about to trade for that item. How many hours of research did you do? One or two? Five? You could answer 100, and I'd believe you.

It doesn't matter, because every single marketer and salesperson who works for the company that sold you the item puts in 8 hours a day, every single day, trying to sell it. Buying products is what you do in your time off. Selling products is what they do for a living. Multiply that by the number of staff on their marketing department and immediately it's clear you're up against quite a force. And this was the exceptional example -- what about the other 99% of purchases that you make in life which don't receive even a fraction of that research time? This imbalance of effort is a good first hint that individuals can't expect their buying decisions to ever be perfectly well-informed.

As a buyer, I need to juggle the pros and cons of a million different aspects of a million different products at a million different price points and find where they converge. For every technical detail that I can devote a few minutes or hours of research to, there is someone whose livelihood it is to understand that detail and find the right way to sell it.
How should I feel about [GMO](https://en.wikipedia.org/wiki/Dennis_Gonsalves) food?
Does "cage free" necessarily mean the animal is treated well or [not](https://www.google.com/search?q=cage+free+crowded&tbm=isch)?
Does this unlocked cell phone support the cellular bands I need for my carrier?
What's the difference between all these [space heaters](https://www.youtube.com/watch?v=V-jmSjy2ArM "Space Heater Nonsense - Technology Connections")?
What's the relationship between megapixels, sensor size, and f-numbers?
Do I want more cores or more gigahertz?
How many plies do I want in my toilet paper?
What the lux is a lumen anyway?
Is 4k *always* better than 1080p?
How do I know this hard drive isn't secretly [SMR](https://old.reddit.com/r/DataHoarder/comments/gagori/are_there_any_ethical_companies_that_are/)?
My buying energy is spread graphene-thin, but a company's marketing department can focus entirely on selling their product.

Some people are rich enough to have a personal butler wherever they go. But how about a personal psychologist-butler, who can tell you about all the ways the people you interact with are taking advantage of your natural thought processes? Your psychobutler could say Pardon me, Sir/Madam, may I inform you that the small, medium, and large sodas are so close in price so that you [focus on the relative deal](<https://en.wikipedia.org/wiki/Anchoring_(cognitive_bias)>) and not realize it's a total racket no matter what you pick? If I may interrupt, Sir/Madam, the colors used in ads are [carefully chosen](https://en.wikipedia.org/wiki/Color_psychology) to push you in the right direction based on research correlating color with emotional response [footnote_link]. Salesmen encourage feelings of urgency with their buy now! last chance! one day only! messaging to prevent you from calmly measuring the sale. Items are priced as $XX.99 so that you mentally round it to $XX.00 instead of $XY.00. The [milk is at the back of the store](https://en.wikipedia.org/wiki/Loss_leader) so that you pass by everything else on your way there. Thumbnails with faces, and especially surprised expressions, pique the most interest and clicks. Ads show crowds of people to help induce [FOMO](https://en.wikipedia.org/wiki/Fear_of_missing_out) and peer pressure. The free continental breakfast is paid for by the cost of your room. Businesses sell coupon packets where the savings is greater than the cost of the coupons, but they make you feel obligated to visit more often to use them up, spending more money than you would have without them [footnote_link].

Do you have a personal psychobutler? The advertisers do. Teams of them. All working around the clock to find the optimal way to disrespect your decision-making autonomy, because you're an ape with an ape brain and you can be tricked.

I've reached the point that I no longer question business decisions any more. Sometimes I'll see a product that looks stupid, and in the past I would have said "that's stupid, why would they do it like that?". Now, I think "that's stupid, but I guess they think it'll make more money", because that's always the answer. I certainly still spend a lot of time criticizing business decisions, but not questioning them.

That's not to say all companies are perfectly rational, for they too are made of apes. There's quite a bit of cargo-culting and trend-following. Apple removed the headphone jack? Oh my god, we'll look so behind if we don't remove it too! I've given up on thinking that big companies ever intentionally make anything good [footnote_link]. That's just a byproduct when quality accidentally coincides with profit.

As they say, you need to know your limits. I for one recognize that no matter how smart I think I am [footnote_link], I do not have the capacity to compete with the behemoth that is modern marketing. I recognize that advertising can influence me even if I don't feel it and can't articulate how. I cannot understand the intricate details of every product well enough to counteract the positive spin that advertisements will always try to place on them.

As such, I am better off cutting advertising out of my life as much as possible, rather than lying to myself that I'm immune. And you are too. People like to think they're not influenced by ads, but if that was true then surely the companies would have given up on making them by now. The industry is foolish, but not that foolish. Avoiding ads doesn't suddenly give me an infinite amount of time to research before buying, but it helps me to start my research from a more objective standpoint rather than being primed by ads.

Hacker News user ineedasername shared his thoughts on some mobile game advertisements:

> Cunningham's Law states "the best way to get the right answer on the internet is not to ask a question; it's to post the wrong answer."

> > A sort of interesting "corollary" to this is something I've noticed in mobile games with in-app ads for other mobile games:

> > The best way to attract a player isn't by showing them someone playing well, it's by showing them someone playing very bad.

> > Because these ads show demo play (usually of puzzles) where the player is making obviously bad decisions, and watching it is sort of like seeing a dozen objects in a row, but one of them is completely askew, and there's an urge to straighten in out a bit.

> > I only noticed this after seeing a bunch of ads recently for perhaps a dozen different games, and realized that I felt somewhat uneasy when they came on instead of simply impatient, and eventually. I tracked this feeling down to the crappy gameplay phenomenon. And once I realized that was the issue, the unease went away.

> > Further reflection made me realize I'd been much more tempted to download those games to "do it right" than other random games that didn't seem to use this tactic. It was actually when I broke and was about to download one that I had the realization, basically "this game looks awful and tedious, why am I about to download it?"

> > https://news.ycombinator.com/item?id=30523075

macksd shares his children's reaction to TV commercials:

> We went quite a few years without ever seeing cable. My kids would stream shows and consume other media on-demand, but any advertising was minimal and fairly non-intrusive. And then they were watching a kids show at a hotel once and the ads came on and the effect it had on them was crazy. They suddenly desperately needed all the toys in the commercials and were repeating catch phrases from ads after only seeing them a couple of times. The contrast in their behavior was insane. And they HAD to keep watching it like I hadn't seen before.

> https://news.ycombinator.com/item?id=30430324

David Foster Wallace comments on advertisements that make fun of advertisements:

> Isuzu Inc. hit pay dirt with its series of "Joe Isuzu" spots, featuring an oily, Satanic-looking salesman who told whoppers about Isuzus' genuine llama-skin upholstery and ability to run on tap water. Though the ads rarely said much of anything about why Isuzus are in fact good cars, sales and awards accrued. The ads succeeded as parodies of how oily and Satanic car commercials are. They invited viewers to congratulate Isuzu ads for being ironic, to congratulate themselves for getting the joke, and to congratulate Isuzu Inc. for being "fearless" and "irreverent" enough to acknowledge that car ads are ridiculous and that the Audience is dumb to believe them. The ads invite the lone viewer to drive an Isuzu as some sort of anti-advertising statement. The ads successfully associate Isuzu-purchase with fearlessness and irreverence and the capacity to see through deception.

> [E unibus pluram (1993)](https://jsomers.net/DFW_TV.pdf)

> https://www.youtube.com/watch?v=nJMq_7alQpU [footnote_link]

Please do yourself a favor and read E unibus pluram in its entirety!

[footnote_text] Don't forget to enable grayscale mode on your phone or computer. Look for something along the lines of Settings > Accessibility > Vision > Grayscale, or Settings > Ease of Access > Color Filters > Grayscale.

[footnote_text] Some of you are probably shaking your head at my exasperated presentation of this paragraph. This is Marketing 101 level stuff, everyone knows it, stop sounding so dramatic. So why does it still work on people!

[footnote_text] I realize this is a No True Scotsman. Any company that does make anything good is simply "not big enough yet".

[footnote_text] very

[footnote_text] Notice that Joe Isuzu fires the whole bullet. That's 65% more bullet per [bullet](https://www.youtube.com/watch?v=6i-nMWgBUp0 "Aperture Investment Opportunity #3: Turrets - Valve, Portal 2").

### Tracking & targeted ads

When a publisher puts ads on their website, how should they get paid? Is it enough to tell their sponsor "we had X,000 visitors who spent YY,000 minutes on the site"? The sponsor is unlikely to [trust like that](https://www.youtube.com/watch?v=zONW46d50A0 "Eric Andre - Harry's Car Place"). The reality of web advertising is that the publisher will have to include a javascript package served by the advertiser so that the advertiser can see for themselves how many impressions they're making. We affectionately refer to these as "trackers" while we block them and curse their existence.

When two different websites use the same advertising package -- take Google AdSense for example -- then the advertiser Google will know that you visited both sites. So although each individual website cannot follow you around the internet on their own, they can aid Google in doing so by linking AdSense to their page. The more websites that use AdSense, the more eyes Google will have into your life, your browsing habits, your interests, your race and gender and sexuality, your purchases, your political affiliations. Like if every time you went to visit a friend's house, you found that some other dude with a clipboard had also been invited.

![](advertiser_tracking.png)

The vague concept of web tracking has become widely known in the past few years, but I think the specifics of how it works have not. Let's make this perfectly clear: the only reason advertisers are able to follow you around the internet is because all of the websites you visit are inviting them in. You are on a daily basis being betrayed by almost everyone who has even the slightest financial incentive to betray you. They will sell you off for a single cent, because $0.01 is bigger than $0.00. Why do you tolerate this? When Google tracks you, you must blame more than just Google, you must blame every single webpage that invited Google into the session.

It's time for a pop quiz! Ready?

![](mcdonalds_cookies.png)

Question: How can McDonalds make the above cookie menu a better experience for the end user?

A) Allow the user to dismiss the modal by clicking the background area, instead of just the X.

B) Add a one-click "Accept all" button so the user doesn't have to think about what they're reading.

C) Remind the user that this is all the GDPR's fault and we really wish we didn't have to do this.

D) Stop using trackers and eliminate the entire thing.

The correct answer is D! The GDPR does not require companies to obtain cookie consent if the only cookies used are completely necessary for the website to function:

> Strictly necessary cookies — These cookies are essential for you to browse the website and use its features, such as accessing secure areas of the site. Cookies that allow web shops to hold your items in your cart while you are shopping online are an example of strictly necessary cookies. These cookies will generally be first-party session cookies. While it is not required to obtain consent for these cookies, what they do and why they are necessary should be explained to the user.

> https://gdpr.eu/cookies/

Whenever you see a cookie banner that starts with the phrase "Because we respect your right to privacy, ...", just remember that they don't actually respect you enough to stop sending you trackers. They'd rather moan and whine about how the GDPR forced their hand into adding this big annoying cookie banner and there was just no other way, we're so sorry you have to deal with it. Indeed, many cookie banners can be considered a form of [malicious compliance](https://en.wikipedia.org/wiki/Malicious_compliance) -- if the website can convince you that a banner is required for all forms of cookies and that the law is to blame, they can sway public opinion against the legislature. The big bad government is the one ruining your web browsing experience, not us. Contact your representatives and get them to repeal GDPR so we can go back to sending you all of our trackers without telling you, the way it used to be.

If the user declines the tracking cookies, you can punish them by showing them the banner every time they come back, until they give up and accept (or block the element with their adblocker). If you wanted the "don't show me the banner again" cookie to persist, you should have enabled cookies! Bwahahahahaha.

If you're interested in this topic, you've probably already heard the apocryphal story about Target [inadvertently outing a young pregnant girl](nyt_target_story.html) by sending maternity-related coupons to the family:

> "My daughter got this in the mail!" he said. "She's still in high school, and you're sending her coupons for baby clothes and cribs? Are you trying to encourage her to get pregnant?"

> The manager didn't have any idea what the man was talking about. He looked at the mailer. Sure enough, it was addressed to the man's daughter and contained advertisements for maternity clothing, nursery furniture and pictures of smiling infants. The manager apologized and then called a few days later to apologize again.

> On the phone, though, the father was somewhat abashed. "I had a talk with my daughter," he said. "It turns out there's been some activities in my house I haven't been completely aware of. She's due in August. I owe you an apology."

Like an Aesop fable for the ethically bankrupt, the moral of the story is:

> We started mixing in all these ads for things we knew pregnant women would never buy, so the baby ads looked random.

> As long as a pregnant woman thinks she hasn't been spied on, she'll use the coupons.

Whether the Target story is true or not, it has become extremely well known and has surely sparked the imagination of many an advertiser and thus contributes to the advertising landscape today. Any competent advertiser who is accurately tracking you will be sure to recover their plausible deniability by adding noise, thanks in part to this story.

Why do I think the Target story may be false?

1. The article cites "an employee who participated in the conversation", so nobody was willing to put their name on these quotes, giving the author free reign to embellish. The father's last quote sounds like it was written by an author, though oddly they forgot to mention that he received a [round of applause and $100](https://old.reddit.com/r/thathappened) for his humility.

2. Even if the coupon packets were distributed at random, they're bound to hit this kind of situation at least once with an audience of Target's size. This is a typical statistical "surprise" [footnote_link].

3. Despite the nonstop development of advertising and machine learning in the years since, this story from 2012 still comes up as the first and often only example of eerily-accurate targeted ads. That would lead me to believe that either the intelligent ads industry hasn't advanced very far since then, or else has advanced so far as to become undetectable with no intermediary standout headlines -- every other advertiser instantly skipped to a higher level of competence. The whole ["cat food"](https://www.reddit.com/r/privacy/comments/79jenh/facebook_iphone_listening_into_our_conversations/dp2fm1q/) thing came close but I don't think the evidence was very good. Here's a comment by Hacker News user segfaultbuserr:

    > Amazon is a $250 billion dollar company that reacts to you buying a vacuum by going THIS GUY LOVES BUYING VACUUMS HERE ARE SOME MORE VACUUMS

    > https://twitter.com/kibblesmith/status/724817086309142529

    > > Everyone thinks this problem is really annoying, but to me it's a good sign - it indicates the current technical capabilities on using and abusing personal information is still limited, the predicted machine learning apocalypse is not here yet. In other words: despite the large quantity of personal information collected by advertisers, they still cannot exploit it efficiently enough, so far all they can do mostly is showing you the same things over and over

    > > https://news.ycombinator.com/item?id=25109026

    But maybe that's all part of a larger plot:

    > Let's say you buy a washing machine on Amazon. You're not likely to need more than one. Amazon knows whether you canceled or returned your order.

    > So the only way it makes any sense is if Amazon is advertising on the chance that you're going to cancel or return it in the future. Amazon certainly has those numbers. But do you think the chance you're going to cancel or return it is so high Amazon should advertise the same product to you instead of something else you might buy?

    > https://news.ycombinator.com/item?id=23749738

In data science, it is common wisdom to collect as much data as you can while you have the chance and filter it down later, because if you don't collect it now you might regret it. A political surveyor could ask you what state you live in so that they can make state-by-state comparisons, but it makes more sense for them to also ask about your city, so they can make intra-state comparisons from the same survey data instead of having to go out and do another survey.

This principle of data collection should not be considered slimy in and of itself. It is simply pragmatic, and applies to all areas: professional photographers tell their cameras to store [raw photo data](https://en.wikipedia.org/wiki/Raw_image_format) instead of jpegs because their editing software can make better changes when it has the raw light and color information, and they can't go back in time to capture that moment again.

The problem is that advertisers haven't really figured out how to deliver on the whole well-targeted ads premise yet, but they're storing absolutely everything they can so they'll be ready for the algorithmic breakthrough if and when it comes. They're like pathological hoarders who keep every single paperclip because "it might come in handy someday", except the paperclip is your mother's maiden name and place of birth.

So if you think targeted advertisements are already accurate beyond detection and advertisers are [magic-bulletting](https://en.wikipedia.org/wiki/Hypodermic_needle_model) the population, you have cause for upset. And if you think targeted advertisements are still "buy more vacuums"-level useless, then that means that despite collecting the private details of billions of peoples' lives over several years, the advertising industry is too pathetically incompetent to make anything of it and is clearly unfit for the responsibility of handling such data in the first place, and you have cause for upset. [Get upset!](https://www.youtube.com/watch?v=ZwMVMbmQBug&t=1m09s "I'm as mad as hell and I'm not going to take this any more!")

[footnote_text] When you pick a random number between one and one million, do you think it feels lucky?

### Slapping everyone once

Here's a quaint documentary from the 1960s called [Advertising: What it's doing to your life](https://www.youtube.com/watch?v=Lz_q4PxZFxA) [footnote_link]. For this section, I want to pull a particular quote:

> If the product isn't all it's advertised, you'll never buy it again. This is important because it forces the advertised product to maintain a reputation. And any time it fails on quality or value, it loses you and your business. Now that isn't true of an un-advertised product, because it has no reputation to maintain. And it isn't true in the case of an advertised product that only seeks to sell you once.

> [16:58](https://www.youtube.com/watch?v=Lz_q4PxZFxA&t=16m58s)

And comment by Hacker News user WalterBright:

> I asked the prof who taught my accounting class about his career in used car sales. He said you could tell a good dealer from bad by how long he'd been in business. A good lot will last more than 5 years, because by then he'll be running on repeat business rather than running out of suckers in the community.

> https://news.ycombinator.com/item?id=23253296

What the 1960s documentary didn't anticipate was the advent of the internet, which gives the product an effectively endless supply of new potential customers. So even a product that "only seeks to sell you once" has significantly more opportunity now than it did in the 60s. And it's not that easy to get a bearing on a company's reputation when they only exist as Amazon brand pages with product reviews of questionable veracity, especially when all they have to do to get a clean slate is take down their Amazon page and put up a new one with the exact same poorly photoshopped pictures.

![](poorly_photoshopped.jpg)

This tactic of slapping everyone once isn't the most lucrative in terms of absolute dollar figures, but is sufficiently low effort and low cost that some product sellers would rather play this way than just make a legitimately better product. To continue the theme of advertising subverting the principles of capitalism, try to imagine how any of these scam-and-spam pieces of junk would get even two feet off the ground without the ability to advertise to fresh gullible eyes all day long. [footnote_link]

If you slapped someone in the face a hundred million times, I think you'd go to jail. But with a bit of care, I think you could get away with slapping a hundred million people once each. Let me know how it goes.

[footnote_text] You'll find that the documentary as a whole is apologetic towards advertising, its importance, and how it creates value and jobs. I recommend giving it a watch, but if you were hoping for a progressive anti-advertising message from the 60s, sorry!

[footnote_text] I can think of one market segment where crap products can survive long-term without the help of advertising, and that's where the buyer is not the ultimate consumer. Think gift shops full of cheap trinkets, where the buyer doesn't know or care about any of the brands' reputations, and the gift recipient will say "thanks, that's so thoughtful of you" no matter how bad it is. Thus, there is no feedback loop for consumer opinion to affect buyer behavior.

### Destruction of public spaces & race to the bottom

> People are taking the piss out of you everyday. They butt into your life, take a cheap shot at you and then disappear. They leer at you from tall buildings and make you feel small. They make flippant comments from buses that imply you're not sexy enough and that all the fun is happening somewhere else. They are on TV making your girlfriend feel inadequate. They have access to the most sophisticated technology the world has ever seen and they bully you with it. They are The Advertisers and they are laughing at you.

> You, however, are forbidden to touch them. Trademarks, intellectual property rights and copyright law mean advertisers can say what they like wherever they like with total impunity.

> Fuck that. Any advert in a public space that gives you no choice whether you see it or not is yours. It's yours to take, re-arrange and re-use. You can do whatever you like with it. Asking for permission is like asking to keep a rock someone just threw at your head.

> You owe the companies nothing. Less than nothing, you especially don't owe them any courtesy. They owe you. They have re-arranged the world to put themselves in front of you. They never asked for your permission, don't even start asking for theirs.

> -- Banksy

We've talked about the media industry competing to reach more eyeballs, and much of this competition takes place in public. "Visit Farmer John's farm" doesn't cut it. Advertisements must get bigger, brighter, flashier, and more animated all the time in order for advertisers to continue out-competing each other. You may have noticed how many advertisements show people dancing, because watching people dance is naturally hypnotic. Roadside billboards, in all their awful 672 square foot glory, have been electrified so they can show a rotation of animated advertisements instead of a single static photo, and they can be bright enough to signal incoming spacecraft.

[![](billboard.jpg)](https://www.reddit.com/r/LosAngeles/comments/m4o2v4 "Does anyone know what that insanely bright billboard just outside of downtown LA is all about?")

It is hardly possible to step outside without being advertised to, unless you recede all the way out into the woods. As I prepared to write this paragraph, I had to ask myself, what would the alternative even be? What kind of cityscape am I imagining that would allow me to be out in a public space and not be advertised to? It is such a foreign notion that it is difficult to even answer. Buildings in a public space are either homes or businesses, and the businesses will want advertise on their space, right?

Well, if you're interested in foreign notions, look to [São Paulo, Brazil](https://en.wikipedia.org/wiki/Cidade_Limpa), which enacted a "clean city" law in 2006.

![](sao_paulo_1.jpg)

![](sao_paulo_2.jpg)

I think it's not wrong for a business to have their name on a sign, but our cities are just totally soaked in advertising that isn't necessary. Billboards, windows, telephones, train stations, bus stops, hell, even the buses themselves are wrapped in advertising reminding you who you should thank for sponsoring the continued existence of the public sphere, as if it would otherwise collapse. Sixteen years later, São Paulo hasn't collapsed.

![](mcdonalds_crosswalk.jpg)

In 2019 a company called StartRocket wanted to [launch logos into space](startrocket.html) [footnote_link].

> "We are ruled by brands and events," he told Futurism. "The Super Bowl, Coca Cola, Brexit, the Olympics, Mercedes, FIFA, Supreme and the Mexican wall. The economy is the blood system of society. Entertainment and advertising are at its heart. We will live in space, and humankind will start delivering its culture to space. The more professional and experienced pioneers will make it better for everyone."

-

> The company didn't share how much a space advertisement might cost, but a pitch deck sent to Futurism opined that brands will pay for the ads because the "ego is brighter than the sun."

-

> "If you ask about advertising and entertainment in general — haters gonna hate," Skorupsky said. "We are developing a new medium. At the advent of television no one loved ads at all."

![](startrocket.jpg)

![](they_live_1.jpg)

![](they_live_2.jpg)

If you're in the mood to deface some advertisements, here's a design you could print out on sticker paper and fill in with marker:

![](warning_sticker.svg "THIS AD PROMISES 𝓫𝓮𝓪𝓾𝓽𝔂, BUT ONLY SELLS 𝓶𝓪𝓴𝓮𝓾𝓹")

[footnote_text] The next step in [cola's domination of the universe](https://www.youtube.com/watch?v=Cry7kbpPlDA&t=4m14s "Ross's Game Dungeon: The Journeyman Project").

### Stifling of expression and choice to match the sponsor's

It is no secret that people who receive things from sponsors feel pressured to keep the sponsor happy by [censoring themselves](https://en.wikipedia.org/wiki/Chilling_effect). For example, a product reviewer who receives free samples from manufacturers might choose to temper their criticisms so they don't risk the chance of not receiving the next free product. I can respect reviewers like [Mr. Mobile](https://www.youtube.com/channel/UCSOpcUkE-is7u7c4AkLgqTw/videos) who end every review by denying any editorial input from the manufacturer, but I also think that his criticisms are usually quite lightweight. Even if he's not being told what to say, he's either self-censoring or just not as discerning as I would be in his position. Better yet are the likes of [Project Farm](https://www.youtube.com/channel/UC2rzsm1Qi6N1X-wuOg_p0Ng/videos) who always purchases everything he tests -- when he says "very impressive!" it actually means something.

Self-censorship also includes not talking about particular topics deemed taboo by the sponsor. The [Youtube Adpocalypse](https://youtube.fandom.com/wiki/YouTube_Adpocalypse) and Youtube's [COPPA agreement](https://www.youtube.com/watch?v=LuScIN4emyo) are both great example of a mass chilling effect that left video creators unsure of what they can and can not say or show. Superstition like "you can say the f-word, but only after 30 seconds" became [officially encouraged](https://www.youtube.com/watch?v=VWAdzMmNLy0&t=1m02s "What the &$!#^%!!! 🤬 Profanity in YOUR YouTube videos and how it affects the MONETIZATION icon 🤑 - Creator Insider (actual youtube staff members)") for a while. People became worried that everything they do has to be family-friendly or else they'll get banned. Youtube's continued decline into artificial incompetence and automated decisionmaking have only made things worse. Even now, many are superstitious that saying the words "covid" or "Ukraine conflict" out loud will weight the video towards being demonetized.

I already feel that basing your income and internet presence on a free website is [risky](/writing/cancel_this_album) at best, but in a basic sense I don't mind platforms having rules and people abiding by them. As time goes on, though, we've seen more and more people consolidate themselves under a shrinking number of platform brands, so the rules that apply to creators of today are ever more monochromatic. If you pay the creators that you want to see succeed, and they diversify or even self-host their publications, and we all come to our senses and start using RSS again, we'd see a lot more color.

The internet presents us with enormous opportunity to develop the long tail, and we are refusing to take advantage of it. In the ages before the internet, if your interests were too niche and specific, you'd never be able to get in front of enough people to find the like-minded among them. Now, with the internet, we have the possibility for people around the entire world to reach each other in milliseconds, to catalog and index and search through all that exists, but instead we stick to what we know, and that's the television-era way of doing things.

### If you're not paying, you're the product

There is a very well-known mantra that goes "if you're not paying, you're the product". You can use Facebook for free, but only because Facebook is selling you to advertisers. If you've heard this once, you've heard it a thousand times.

What this means is that your eyeballs and your attention are the product being sold by the publisher to the sponsor. The sponsor doesn't care about you as a human being, they care about how many clicks are landing on their website, and the publisher promises they can generate so many clicks in exchange for CPI. We like to think of ourselves as the customer using the Facebook product, but in fact we're more like cattle on the Facebook ranch, and the advertiser is the customer hungry for steak.

Cattle ranches like Facebook, Instagram, and Twitter do odd things that make the service less convenient for the cattle, like obscuring chronological timelines in favor of discovery and recommendation systems. One might say that these changes make the product worse, but since the real product is the cattle's mere continued existence and not their happiness, these changes actually make the product better from the perspective of the advertiser.

This also explains why it's so difficult for users to get help when something is wrong with their account, and why their opinions are rarely considered when changes are being made to the system. The happiness of the cattle is not really important, and it's better to pursue two new ones than help one old one. At this point I am basically repeating what I said earlier about becoming a media production house.

That's fairly straightforward, but there are some situations where the "you're the product" concept starts to get a little twisted. That's when a content platform shares some of its advertising income with the content creators. Youtube, for example: [They're deleting my channel, but they don't know why?](https://news.ycombinator.com/item?id=24571038)

> If Google/Youtube were NOT a monopoly, they would have invested significant amount of money in customer support. However, there is zero. They are saving hundreds of millions in support costs by not delivering any support. Unlike more overt monopolistic actions like raising prices, etc, what they do instead is increase their profits by taking away functionality that their customers should be receiving.

> > They do have support infrastructure for their customers. Youtube content creators are not customers, they're more akin to contractors (when paid) and volunteers (when not). In fact, google is the customer in this relationship, and they are within their rights to stop buying the product without having to explain why.

> > It is on content creators to diversify their business. If a contractor has only a single customer because that customer is the most profitable, would you pity them when they are fired by that customer? Or would you call them bad at business for failing to diversify?

We have a situation where simultaneously:

1. The advertiser is the customer and the viewer's attention is the product.
2. Google is the customer and the video is the product.

![](youtube_youretheproduct_1.png)

But the thing that makes this relationship even more twisted is that even though video creators expect to get paid for their videos, they don't actually have any contract guaranteeing it. Officially, each video is offered up to Google for free, and Google may or may not decide to kick some revenue towards the creator. This lack of contract also means that the creator has no production quotas or deadlines, they publish as much or as little as they want. The difficulty of getting paid by Youtube has led many video creators to make deals directly with advertisers and perform the advertisement as part of the video. This leads to viewers seeing twice as many ads in the practical sense, except in the minority case where Google decides not to run their sponsors' ads on the video because the topic is too risqué for them.

![](youtube_youretheproduct_2.png "Note to future readers: the yellow dollar sign indicates limited or no advertising run by Google's sponsors")

Collectively, creators have complete leverage over the site's ability to operate. Without new videos, Youtube would be in big trouble with the advertisers. But individually they are basically holding out their hats and hoping they'll catch some of the falling coins. The strongest threat that an individual creator can make is "I'm not gonna upload any more videos for you!", which measures at about 0.0001 on the Richter scale. Google is always prepared for individual creators to come and go, which is why they don't draft contracts or guarantee payment, so without significant collective action on the part of creators hurting the bottom line, Google has no incentive to change. Not to mention you'd be asking creators to sacrifice their own income by withdrawing their hat.

One more good comment:

> People could stop using Google today but most don't, because Google is just so much better than everyone else at searching.

> Should Google/YouTube be regulated because people dislike what the company is doing, but just not enough to actually stop using their products?

### If you're paying, you're still the product

"Hey", said the director of marketing to the product manager, "the users on the free plan are earning us $3.50 per month in advertisements, and the users who upgraded to the premium plan are earning us $8.00 per month."

The product manager eyeballed the quarterly report and saw that these figures were accurate. "Things are looking good."

"But if we show them the ads too, we could be making $11.50."

![](stonks.jpg)

Hulu is one of the more notorious examples that comes to mind. You can find lots of people wondering why they [still see ads](https://www.google.com/search?q=hulu+ads+on+paid+site:reddit.com) after upgrading to the plan called "Hulu (No Ads)". Hulu's help center has [an answer to this question](https://help.hulu.com/s/article/ads-on-hulu): their service provides both on-demand media and live television, but "No Ads" only refers to the on-demand media because the live television is, well, live from another broadcaster that controls the stream. That answer is pretty reasonable in my opinion but, gee, maybe they shouldn't call it "No Ads", huh? A reasonable consumer might be misled into thinking they're paying for a plan that will not include any advertising. Perhaps Hulu is only targeting the unreasonable consumers.

The current state of so-called smart televisions is a horrifying glimpse of this future. There are endless reports of [Samsung televisions showing ads in the UI](https://www.google.com/search?q=samsung+smart+tv+showing+ads+site:reddit.com). And when you see the option to "turn off personalized ads", that doesn't mean you get to turn off the ads, just that they won't be personalized any more. Probably. I'm waiting patiently for some [evidence](https://old.reddit.com/r/assholedesign/comments/dm8vv9/my_2500_tv_has_sponsored_content_built_into_the/f4ytbn8/ "I've had a Samsung TV for about 2 years, and the ads just showed up recently after an update") of manufacturers delaying the showing of ads until a 90-day return period has expired.

The tech-savvy TV buyers know that you should never, ever give your TV your wifi password, because it will use it to advertise to you. But get your tin foil [footnote_link] ready because soon that won't be good enough -- cellular providers offer [IoT data plans](att_iot.html) for around $1.00 per month, [or less](hologram_iot.html) when arranged in bulk. Your next TV could very well come with a cellular modem and a SIM card inside, essentially all the important guts of a cell phone, so that it can connect to the internet all by itself. The TV manufacturer would pay the monthly cost of the SIM and you'd never know it's there.

"But the advertisements subsidize the TV and make it cheaper for the consumer", you'll hear. Firstly, I think this is basically hogwash. If it's true at all, it will only be a temporary effect. The manufacturers picking up money on advertising can afford to drop the sticker price and take a loss on the TV itself to undercut the competitors. But once all the competitors follow suit and every television at your local big box store has advertising built in, we'll be back to square one in a new fresh layer of hell. Secondly, the whole [Moore's law](https://en.wikipedia.org/wiki/Moore%27s_law) thing took place from the 1960s to the 2000s and demonstrated within one lifetime that electronics technology can become better and cheaper without every single transistor sending you spam mail. To say that letting your TV advertise to you has opened up new doors for affordable technology is myopic. This isn't the only way forward.

[![](make_it_your_way.png)](US8246454B2.pdf "SYSTEM FOR CONVERTING TELEVISION COMMERCIALS INTO INTERACTIVE NETWORKED VIDEO GAMES, Sony Computer Entertainment America LLC")

[![](say_mcdonalds.png)](US8246454B2.pdf "SYSTEM FOR CONVERTING TELEVISION COMMERCIALS INTO INTERACTIVE NETWORKED VIDEO GAMES, Sony Computer Entertainment America LLC")

The TV is one thing. It's a media device anyway. Next up is your refrigerator, dishwasher, clothes washer, dryer, air conditioner, heater, stove, oven. Looks like you're running low on detergent, why not pick up some Tide™? Looks like you've been running the AC pretty often, you should ask Home Depot™ about installing some double-paned windows to improve your home's insulation. You've started cooking more recently -- new hobby? -- you might like a fresh set of Lodge™ cast iron skillets. The manufacturers will not put a screen on your appliance that tells you these things, but they'll collect the data and use it to decide what you see on the web tomorrow [footnote_link].

"As long as a pregnant woman thinks she hasn't been spied on, she'll use the coupons."

And every time you see a "smart" version of a product that you didn't know needed to be smart, you should be very suspicious. As soon as the manufacturer of your bed, your couch, your [pillow](https://www.youtube.com/watch?v=VkVGtQOko1A "JerryRigEverything - This Smart Pillow costs $300!?!"), your dresser, your cabinets can convince you to plug your furniture into the wall, you're taking the bait and they're going to use your [own electricity](https://www.youtube.com/watch?v=kTCmpYDzq3w "Two of my own pies!?") to advertise to you. It's a bad habit to get into.

![](please_drink_verification_can.png)

There's another point that I was only recently enlightened to. One way that appliance manufacturers are able to get these anti-user products into users' homes is by making deals with home builders and landlords, and having their appliances installed before the would-be home buyer has any say in the matter. After all, the home builders aren't the ones that have to actually use it. This is another example of advertising subverting the foundations of capitalism: the manufacturer doesn't need to win over the customer with a good product, they just need to find novel ways of getting in your face.

This is okay though, because as we all know, the free market will sort itself out. You as a home buyer will simply have to do comprehensive research on every single electronic device that is included in the home and be ready to drop the entire deal at a moment's notice. In this economy. Good luck!

[footnote_text] Reynolds Wrap™ is perfect for making faraday cages and also [hats](https://www.youtube.com/watch?v=urglg3WimHA "Weird Al Yankovic, Foil")!

[footnote_text] But remember, the only reason your stove can influence the ads you see on Twitter is because Twitter is selling you out, and you've got to blame both parties.

### Spam: your life as an arms race

Spam is built upon the abuse of systems by definition. Unlike sponsors, who make a deal with the publisher to show ads in their system in exchange for payment, spammers are people who try to slip between the cracks of the system and get their advertisements directly to you. Like bomb-carrying terrorists, spammers will target venues that:

1. are pre-established, because spammers can't attract an audience on their own.
2. are highly trafficked, because spammers need to hit as many people as possible before getting caught.
3. provide otherwise legitimate value to your life, so that you will not simply leave the venue after the spammers invade.

Your email inbox and your telephone are systems for communicating with people you know, and spammers abuse it to send you junk. Web forums are systems for conversation, and spammers abuse them by making fake posts. Grocery stores are systems for buying food, and spammers abuse the traffic flow to hand out fliers. [Parking lots](/writing/not_just_bikes) are part of our transit system, and spammers leave advertisements under your wipers because you're not there to stop them. The front door of your house is for yourself and your guests, and spammers abuse it by turning it into ad space.

The problem with spam is not just that it's annoying, but that it converts your entire life into an arms race. Spam is hostile. It is mean. Spam takes every aspect of your life and turns it into an opportunity to make a buck off of you. No matter how hard you work to avoid advertisements and carefully pick the publishers you want to pay for, spammers can override your decisions and advertise to you anyway. I am not kidding when I compare spam to terrorism, though I am exaggerating. Spam positions you against enemies you didn't know you had. Enemies who come from afar to your place of residence to disrespect your time, attention, and belongings, and sneak away. Unlike a TV which can be turned off or a magazine which can be closed, spam offers no means to opt-out. Spammers will hit you and run without showing their face. What are you going to do about it, not have an email address?

People dump their ugly fliers on your doorstep, and for some reason the onus is on you to clean it up and hang a No Soliciting sign to stop it from happening again. Do we also need to hang a "Please don't throw eggs at my house" sign, just in case? How about "No Bombing"?

Consider for a moment the extraordinary amount of resources that have been utterly wasted by spam. How many millions of square miles of paper are printed into pre-approved credit card offers so they can go straight to the shredder. How many talented software engineers have been relegated to writing spam filters, email blockers, abuse heuristics, shadowbanners, phishing protection, and anti-spoof measures just to stop worthless dirtbag spammers from polluting their website and the internet at large. All this effort could have been put to better use. As I write this I feel like I am describing police versus fraudsters.

Spam is a crime against humanity and I'd like to see the worst offenders jailed.

## Arguments against ads

Even if we consider the above the be a list of reasons why ads are evil, some may say they are a necessary evil. Below are some reasons that advertisements are less necessary than we think.

### Not every job's a living

When people complain about ads on the internet, mobile apps, and so forth, there is a common defense that always comes up. It's that "website owners/app developers need to eat too!". I agree with this and will take it a step further: everyone needs to eat. No, further: everyone *deserves* to eat. And everyone deserves to have a comfortable home and enough time in the day for leisure. Woah! So progressive! I'm pretty ahead of the game here. But how can I reconcile such a utopian vision with a rejection of the ads that make all of these things possible? You know that nobody ate until the advertisement was invented.

Whenever I think about this, there's an analogy that always pops into my head. I've had it for years, and it goes like this:

Suppose someone decides they want to make a living selling bottlecaps, or refurbishing used napkins, or decorating toilets, or teaching underwater basket weaving [footnote_link]. So they stand on a street corner peddling their wares and find they don't get many takers. Turns out people don't want to spend money on that. Panic sets in. "I've set my sights on this job!" they cry. Rent and bills continue to pile up but the money's just not coming in.

The situation becomes desperate as they realize their monetization scheme -- you know, exchanging their goods and services with customers for money -- isn't going to pan out. With the business failing and the market clearly not ready for their idea, they finally make the obvious choice... huh?... find another job? No, I mean they start yelling at passersby with a script someone else is paying them to say, and slipping tracking devices into their pockets as they go. And if any of them complain, it's the same old story: *I'm sorry you don't like the ads, but used napkin refurbishers need to eat, too!*

Such is the current state of the software, web publishing, and mobile app industry.

I know that our society has got a pretty serious problem with undervaluing software. Why is it that I'm willing to spend $10 on a pizza that I'll get three meals out of, but I'm not willing to spend $10 on software I'll use hundreds of times over the course of years? I don't know. Partly because we have problems assigning value to intangibles, and partly because I've been conditioned by the plethora of great, free, no-ads software I've already [got](/writing/sqlite_what_a_hunk). And partly because of DRM which aims to strip control even from paying customers, but that's another matter. If I was getting free pizza regularly I'd surely stop paying for that, too, even if the paid ones were a little better.

But that's not really the point. That's an [is/ought problem](https://en.wikipedia.org/wiki/Is%E2%80%93ought_problem). Consumers *ought* to be willing to pay for good software or web experiences or mobile apps, but the reality is they mostly *aren't*. The economy and the world in general is full of is/oughts, and when it comes to making a living and paying rent, I think most of us understand that we have to follow the is. What absolutely boggles my mind is that developers whose goal is to make money with their idea [footnote_link] can recognize the state of the industry, understand that the likelihood of making sales with it is near zero, and then **proceed anyway** before, oops!, needing ads to pay the bills. In fact, I'm being disingenuous here by implying that developers even intend to use honest sales in the first place; the situation today is that ads are the expected and planned business model for many or most. Look at how many websites and apps are launched with analytics, tracking, and ads baked in from day one.

Can you imagine applying this line of reasoning to any other industry? Mom, when I grow up I'm going to become a napkin refurbisher. But darling, no one's going to pay for that, are you sure you can make a living? It's okay I'll run ads. Mom, I'm going to start a business decorating toilets. Will anyone pay for that? Maybe a few, and I'll run ads to earn the rest. Mom, I'm going to **enter a market in which there are not enough paying customers to make a living**, but it's ok I'll run ads. Does this not sound totally wild?

My feelings here would be different if we were still in the exploratory phase of computers, back when we weren't really sure if money-for-goods style transactions could work here. But we're not in that phase. Those pioneers have come and gone, and they left a bunch of signposts saying "people don't pay for this stuff". Very occasionally, someone will realize a market opportunity that does work. Steam sells loads of games and does so because "it's easier than piracy". I don't use Spotify but I've heard they're in a similar position. Netflix captured the movie-streaming market first, and were worth paying for until the more recent fragmentation of everyone trying to start their own streaming service and pulling their licenses from Netflix. I just simply cannot sympathize with someone who knows that making websites or mobile games doesn't pay the bills without ads, then starts doing it anyway and complains that they can't pay the bills without ads, despite not having a remotely unique take on the problem. Likewise, I expect that you would not sympathize with me if I tried to start a napkin refurbishing business and found it to be unsustainable.

Job titles are descriptive, not prescriptive. It's not like you are born an app developer and therefore you must make a living making apps. You're an app developer because that's what you chose to do. So when people say "app developers need to eat too!", all I can think of is "then why did they choose that job!?". This is not discrimination against something out of your control. *Everybody* needs to eat, so the fact that they become full-time app developers confounds me.

I don't understand why we're so hell-bent on making apps and websites and social media networks. Our culture has become absolutely tunnel-visioned, barrelling along on the locomotive of PUBLISH MORE PUBLISH MORE, we've become incapable of considering that our hobbies weren't meant to be full-time jobs. All we can do is double down, insist with our dying breath that Twitter must go on!, injecting it with engagement-boosters whenever growth slows. Have ye no shame, corrupting your work like this? Didn't you begin the project out of passion?

![](tetsuo.jpg)

If this line of reasoning works for web/app developers, why haven't we seen the degenerative collapse of other industries in which people do unprofitable things but spin it off into an ad-slinging business to make ends meet? Why isn't every single auto mechanic, grocery store, and restaurant offering their primary service for free, and making up for it by showing advertisements for sponsors [footnote_link]? Well, first and foremost it's because there are actually customers willing to pay for those. But moreover, the technology industry is unique because it's the biggest force-multiplier the world has ever seen. Real-life businesses are going to be bound by the high costs of property and lights and inventory and staff. If Grocery Mart gives out groceries for free and hopes to make their money on third-party ads, they're gonna have to show a hell of a lot of ads and still will never achieve a big enough reach to make it pay off. Meanwhile, ads on the internet are highly passive from the point of view of the website owner or app developer, and they reach thousands of times more eyeballs, and the cost of hosting a website or distributing an app's worth of megabytes is dirt cheap compared to leasing store property and giving away real inventory.

It's all a bunch of is/ought/is/ought/is/oughts. I'm gonna go crazy over this stuff [footnote_link].

[footnote_text] When I equate the writing of software with these trades, I'm not doing so on the basis of the craft itself. I'm doing so on the basis of the number of paying clientele, and furthermore I'm exaggerating to make a point. Writing software is much more useful and impactful than refurbishing napkins, etc etc etc, and we could harvest a million is/oughts out of this situation.

[footnote_text] If your goal is not to make money, then proceeding with an unprofitable idea is perfectly fine. That's called having a hobby. I'm talking about people who want to enter a market that won't support them and then saying Sorry! I had to run ads or I'd be out of business! as if that outcome wasn't obvious from the beginning, and as if staying in business was mandatory.

[footnote_text] Yes, grocery stores do have signage and priority shelving spots which suppliers pay extra for, and fast food chains have agreements with ketchup and soda suppliers. The difference is that shelving is physical, limited real estate. So the decision of what to put where comes down to logistics with sponsorship as a tie-breaker. Furthermore these things are contextually relevant to the domain, and I enter these places with the expectation of spending money, neither of which are the case for web ads.

[footnote_text] I already have.

### Without ad-supported content, would there be any content?

During the previous section, you may have been thinking that a developer slinging ads on a free site or app is more acceptable than a napkin refurbisher slinging ads, because websites and apps improve our lives in a way that refurbished napkins don't. This is also true for Youtubers who quit their day jobs to make videos, funded by ads.

One facet I want to express is that the value, I mean benefit-to-the-world value, of ad-supported websites and services is almost universally overstated. And the value that is there can hardly overcome the damaging cost of ads. Humanity has survived for thousands of years without Instagram and can continue to do so. I don't know why we've developed this "all business ventures must survive forever" mindset, especially when it leads to the corruption and rotting of the original business. What's that, Snapchat wouldn't be able to continue operating if it weren't for ads? The History Channel, a shell of its former self and a disgrace to its name, would have to stop broadcasting? Hmmm, this is all sounding pretty good!

But surely if I got my wish and ad-supported websites all shut down, there'd be nothing left, right?

There would be less, that much is true. There'd be a **lot** less. But increasingly, and overwhelmingly as of late, that's sounding like a good thing to me. The internet used to be small, but most things you could find were interesting or at least made by someone who was genuinely interested in making it. Now the internet is enormous and nobody cares about anything except getting clicks. Browsing the internet now is like swimming in a polluted lake.

Veritasium gave a presentation about fake news and facts on the internet:

> I was an optimist. Maybe I was naive about the internet. My thinking about having an international communication system whereby anyone anywhere can share anything -- regardless of their education background or their class standing -- and get access to real information through Wikipedia. My thinking was the internet was going to make everyone happier and more informed, more educated, and probably more tolerant of others around them.

> [Post-Truth: Why Facts Don't Matter Anymore](https://www.youtube.com/watch?v=dvk2PQNcg8w)

His thesis is about misinformation and intolerance [footnote_link], but I share his feelings of disappointed optimism. What was once called the information superhighway and touted as all of human knowledge [at your fingertips](https://www.youtube.com/watch?v=A81IwlDeV6c) is now sadistically impossible to navigate, with little tidbits of value hidden beneath mountains of SEO gamification, low-density listicles, promoted posts, and flat-out spam.

When I say that I long for the internet to be small again, I'm not saying I want the clock to roll back in time -- that would mean there'd be fewer people connected and I certainly want the internet to be global. But I want it to be personal, and passionate. I want to find things that people made because they enjoyed making them, not because it was the most algorithmically optimal thing to make. I'm sick of communications platforms becoming walled silos because if they allow anyone else to access their data they'd lose their advantage over the analytics that feed their advertising. I'm sick of gmail being synonymous with email. I'm sick of everyone and everything being factored in to a monetization strategy writeup.

I use adblock and I visit websites which are fueled by ads. I do not whitelist anybody. So I don't have a right to complain or fuss when they eventually shut down, since I was never helping them stay up. That's why I [download](/writing/download_podcasts) everything that I care about. Suppose I get my wish and ads disappear forever, and every website becomes either purely-free, or subscription-based, or shuts down entirely. Which ones would I pay for? Out of all the ad-supported websites and services that I use today, the only one with content that I consider worth paying for would be Youtube, because video is my favorite medium and I'm well aware that hosting video costs money. [footnote_link]. If reddit were to die I'd be 50/50 bummed and relieved. [Pushshift](https://pushshift.io/) has got it backed up anyway, so as far as historical knowledgebase goes we wouldn't be losing much. Hacker News is already free without ads, though subsidized by YC's business ventures.

[footnote_text] I won't say that advertising and misinformation or intolerance are directly causally linked, but I will say that [stormfront.org has Google Analytics](stormfront.html).

[footnote_text] If I were to pay Youtube, I'd want the money to be used only for hosting the videos, **not** for paying the creators. Youtube has gone through periods of prioritizing video length, or watch duration as a percentage, or publication frequency, etc. for controlling *the algorithm* and payout. Goodhart tells us that distributing the money based on any of these factors will make the creators change their behavior and poison the system. If I want to give the creators any money, I'd use Patreon to pay them directly, and I have done so. The cesspool channels that no one is willing to directly fund, unable to survive without advertisements, would go extinct. We'd also lose some genuinely good creators who can't devote their time to making free videos, and that's a bummer, but it's a sacrifice I'm willing to make in exchange for the higher median quality level.

![](someofyoumaydie.jpg)

### You paid for the ads

I would like to quote a portion of this champion comment by Hacker News user eevilspock which permanently altered my perspective of advertising. It starts with the "if you're not paying, you're the product" mantra we all know and love, but then takes it a step further which I hadn't seen before:

> IT'S NOT FREE

> We're not Facebook's customers, advertisers are. But we are the advertiser's customers, and the cost of the "free lunch" is simply shifted to the price of the things we buy from them. In other words we still end up paying for the full cost of Facebook. Costs may even shift regressively, to advertised products predominately consumed by those with lower incomes, in which case the poor are subsidizing the better off.

> IT'S MORE EXPENSIVE

> Not only are you still paying for the full cost of the Facebook product you use, you are paying for all the advertising overhead: the costs of its advertising technology and infrastructure (huge, btw), the agency and creative costs [...], and the advertiser's big marketing departments (that often outnumber and outspend the people making the product!).

> [...]

> Our identities and privacy are bought and sold to the highest bidders. And where do the bidders get their money? From us of course! A double whammy!

> https://news.ycombinator.com/item?id=7485773

This comment left a big impact on me and I can't possibly discuss advertising without mentioning it. Whenever I imagine myself getting into a conversation about ads (which is often), I imagine myself paraphrasing this argument.

[Investopedia says that Coca Cola spends $4 billion per year on advertising, out of their $35 billion revenue](investopedia_coke.html). Where did Coke get 4 billion dollars to spend on ads? From the customers' pockets, of course. That's a percentage of the cost of every single drink that winds up going to their marketing department so they can make advertisements that you don't want to see. The idea that "ads allow publishers to make things available for free" is cumulatively false because any time you buy a Coke, your money is going to all of the publishers they sponsor (even the ones you don't read) *and* all of the operational and staffing overhead involved in the advertising machine.

![](nowthatswhaticallfree.png)

Earlier in the article, I said "by displaying a sponsor's advertisement alongside your product, you can earn more money without having to make your product better". In that section I wanted to focus on the publisher's perspective, but there's an interesting dynamic here that we can evaluate from the sponsor's perspective. After all, both parties are hoping to increase their revenue, but they approach it in opposite ways: the publisher reduces the price of their product, possibly down to free, and "makes it up in volume" with the help of the sponsor; meanwhile the sponsor is dishing out money to the publisher, so they need to recoup that cost somehow. Isn't that a bit strange? What techniques are they using to earn that money back, and why couldn't the publisher apply those techniques to their own product in the first place, so they could earn their way without showing ads? Why are so many publishers unable to get enough money from customers' pockets to stay afloat, while Coke is pulling in enough money to support both themselves and the publishers?

It is a brain-wrinkler for sure. I have not figured it out. Perhaps it is like the phrase "those who can, do; those who can't, teach". The alpha males who know how to sell a product become the sponsors, the beta males who can't sell their product take on sponsors. Of course, the sponsors are the ones coming up with disgusting, manipulative psychological tactics to do their selling, so it is not exactly an honorable title. Many of them wouldn't be able to survive without stooping to new lows every week [footnote_link], but I guess being abusive, uncaring, and ready to kill is what makes one an alpha. 

Part of the problem, which I touched on earlier, is that people have been conditioned to not pay for software or websites, whereas we're already accustomed to paying for sodas. But I don't think that's the full answer, because the internet is young compared to the usual suspects of sponsorship advertisements: tv, radio, newspapers, magazines. Television and radio were uniquely dependent on sponsorship revenue because it's not really possible to charge someone for access to an RF frequency unless you encrypt the datastream and sell them the key, which wasn't developed at the time. But print media was, and still is, something that the reader paid for, yet it became swamped with ads quite a long time ago. Were they just too beta to compete the normal way? I don't know yet.

Here is another take by bondarchuk,

> "What about the revenue the city gets from advertising space?"

> Someone pays the city to show me something. That means the ability to show it to me is worth more to them than what they pay the city. It also means that at the end of the day, the money is somehow coming from me, and this amount could be larger than what the city gets out of it, even. Therefore I would actually save money if the city abolished advertising and just raised taxes a little.

> https://news.ycombinator.com/item?id=27193190

If ads were eliminated from the world, everything could hypothetically be several percent cheaper and:

1. You could instead give your money to the publisher directly, which would definitely be more than they get from the CPI of advertising to you, but you only have to pay them if you think their publications are worth buying.

2. The sponsor would have to focus on building a strong reputation and making a good product, instead of designing ads that manipulate people into thinking they have a good product.

3. The sponsors who cannot maintain a customerbase without the help of advertisements would go extinct.

4. The publishers whose products are not good enough to pay for on their own would go extinct.

5. New businesses would have a hard time getting their first customers.

![](extinct.jpg)

Could this really happen? If the marketing departments vanished overnight, would product sellers actually reduce the cost of their product to match their reduced expenditure? No. Customers have already demonstrated that they are willing to buy it at the current price. But São Paulo has shown that legislators can force the ads to come down. Once the brand is physically unable to buy ad space, they're going to have to redirect their marketing budget somewhere. Sure, they might just hoard the extra cash. But I do think that if a new generation of customers were to be raised in an ad-free world, and a new generation of brands were to be formed with no marketing expenditure, they would see the opportunity to undercut the incumbent brands who forgot to lower their prices, and a shift may occur.

Regarding point 5, it may be reasonable to legislate a maximum advertising expenditure, instead of forcing it all the way down to zero. Suppose we allow business to have advertising budgets, but we clamp it down so low as to stay in the "Visit Farmer John's farm for some tasty corn" territory. That is to say, businesses would not be able to spread themselves thin trying to advertise to the whole nation or world, so they'd naturally have to stay more local, putting young businesses on more equal footing with larger brands and re-igniting a real sense of competition over the quality of the product instead of the psychoterroristic manipulation of the advertisement. I'm still glad to have a global internet, of course, but it would be word of mouth that spreads your product far and wide, not your advertisement.

Making this change is like planting a tree: the best time to do it was 20 years ago, the second best time was 19 years ago, the... um... it's better today than never.

I'm sure you will want to remind me of [economies of scale](https://en.wikipedia.org/wiki/Economies_of_scale), and that advertisements help companies reach large scales which bring their unit costs down, thus the price of the product can't necessarily be reduced by exactly the amount of the marketing budget if the marketing department were dissolved. I get it.

[footnote_text] When I see or hear children performing advertisements on tv or radio, it makes my skin crawl. I wasn't sure where else in the article to mention this, so I'm putting it here. It's low.

## Unspoken agreement between publishers and visitors

Although I am vehemently against ads, it's time for me to distance myself from one of the common anti-advertisement arguments. I am not a zealot and I will not blindly agree with any anti-advertising stance that comes my way.

Scenario: A website publishes articles and has ads on the page. A user enables adblock and reads the article with no ads. Is this user in the moral right or wrong?

There are some proponents of adblock who will assert that they are in the right because it's their computer and they should have the power to decide what their computer does. In the very same way that I as a human reader can choose to not read paragraphs that begin with the word "But", I should be allowed to have my browser block anything that calls itself `<div class="ad">`, and I should be allowed to prevent any `ads.js` from being executed.

**I think this is absolutely true**. It's my computer, it's my electricity, it's my processor cycles, and it's my eyeballs. Nobody should have the right to run unscrupulous code on my computer just because I visited them once. I am under no obligation to see that div if I don't want to. On that front, this argument is sound.

**But**, this argument is only good for approximately a single visit before it runs out of steam. When I go to a website for the first time, I don't know how many `ads.js` they're going to try to hit me with, and I have every right to armor up before clicking the link. For every visit after that, though, the justification is all but lost. You've seen what they're sending you and you don't like it. Why do you keep coming back? You're not obligated to visit that website, you're freeloading. It is immensely obvious to me as a reader that the publisher is only allowing me to visit this page because they assume I will see the ads along with it. It is obvious to me that if they could physically prevent me from reading the page without ads, they would do so.

This is not the same as a reader skipping over paragraphs that start with "But" because those paragraphs are probably not uniquely responsible for the author's income when compared with the other paragraphs. The divs marked `class="ad"` are uniquely responsible for their income when compared with the other divs. Where do you think the arms race of adblock-block-block-blockers comes from? It is obvious to me that they did not intend for me to read the page for free, and in doing so I am violating the trust they had in my readership.

Notice that word, "trust". Anybody who perpetuates this "it's my computer" argument is being willfully disingenuous and approaching what is obviously a social problem, trust, with a purely technical solution, adblockers. "Your computer sent my computer a bunch of different bytes, and I had my computer filter out some particular bytes before showing it to me, because I prefer reading it that way. It's not my fault that those particular bytes are the ones that make you money. They're just ones and zeroes why do you care so much\~".

Using a technological bypass around the social matter of trust does not put you in the moral right. You're not "getting back" at them for wronging you. You could achieve that by leaving, never to return. Even though I've always got my adblocker on, there is a growing list of sites that I simply do not click on, because I resent what they try to send me.

I think there are some cyborgs out there who do not make the link to the social element of this problem, and only see it as a tech issue. These cyborgs are the ones who go around offering technical solutions to the publisher, like suggesting that they should either suck it up or put in a paywall if they want to keep out freeloaders so much. But that's like telling someone they should have locked their doors better after you've wandered around inside their house, and that they should have known someone would sneak in. It is logically accurate but not morally right.

I started by calling this an unspoken agreement, but when you start seeing "please disable adblock to view this page", then it's very much spoken, I think you'll agree.

Do I still use adblock on ad-fueled sites anyway? Yes! Do I treat the "please disable adblock" popups with scorn? Yes!! But you won't see me using this "it's my computer" argument to defend that practice. I'm freeloading because I like freeloading and am willing to recognize it as such. And if being called a freeloader when you use adblock offends you, then I guess you'll have to stop doing it or grow thicker skin.

## HailCorporate

There is a subreddit called /r/HailCorporate, whose stated purpose is to point out posts on reddit that *act as advertisements*. This means giving a brand excessive or undue attention, framing photos the way an ad or product placement shot might frame them, and mentioning brand names when they aren't actually relevant to the event at hand. For example, "My box of Toasty Bites fits perfectly between two of the shelves in my pantry!" could have just said "My box of cereal".

The phrase "act as advertisements" is key. Some outsiders visit the subreddit assuming that the purpose of HailCorporate is to identify posts that are actual, paid, what you might call traditional native advertisement posts. Then they see HC users talking about posts which *aren't* traditional paid ads, and assume HC users are idiots for thinking that those posts *are* traditional paid ads. You can see how the logic goes, but it's frustrating how many people don't understand the original premise of HC [footnote_link]. HC is not about thinking that Toasty Bites literally paid someone to take a photo of their pantry, it's that the photographer had no reason to call the cereal by name but did it anyway. Here are some other values we can learn from HailCorporate:

1. You should take pride in what you do, not what you buy. There are a **lot** of posts on reddit that are just pictures of products that the user purchased, still in their boxes, without any subsequent pictures of the products being put to good use. This is sometimes called box posting. People post pictures of unopened hard drives on /r/datahoarder, new and untouched headphones on /r/headphones, unused pens on /r/pens, translations of Harry Potter in /r/languagelearning, etc. Like, wow, you... spent money? Wouldn't it be more personal, meaningful, and interesting to the hobby community to share what you actually make and do with these things, rather than just the fact that you bought them? Here's an [HC post](https://old.reddit.com/r/HailCorporate/comments/gqeb9o) about a [povertyfinance post](https://old.reddit.com/r/povertyfinance/comments/gpstkm/) in which the OP shares a *screenshot of the store page* for a stove they bought. It's not a box post, it's not even a receipt post, it's just the product listing! How eager for internet affirmation must you be to do this, that you can't even wait until it arrives and is installed [footnote_link]?

  Why do people make these posts? First and foremost it's because buying is easy and doing is hard, and people will make posts that are easy to make. Box posts will make the community regulars groan, but sharing something you've actually made opens the door for people to criticize you and your work and the value of your life. Box posting requires no vulnerability. Everyone in the /r/pens community will like looking at fancy new pens, but they might not like looking at the bad drawings you made with those pens, and that makes box posting the safest option.

  I also think a lot of us fall into the mental trap that we're not **real** artists without the best brand of pens; not **real** hikers without the best boots and backpacks; not **real** music enthusiasts without the best headphones. We look at the people doing work we envy, and see that they use expensive equipment, and deduce that the equipment made the work. But this is putting the cart before the horse. Most professionals buy the expensive equipment *after* they've devoted significant time and energy to the craft.

  You've probably heard about people who buy lottery tickets knowing full well they'll never net any money, but they do it because the price of the ticket is worth the small moment they can spend dreaming about winning. This really applies to other purchases too: spend $X00 on something online and enjoy the next 6-8 business days dreaming about all the cool stuff you'll do with it when it arrives... whether or not that actually pans out in the end. Buying is easy and doing is hard.

2. All publicity is good publicity & Mindshare. Sometimes, a post will come up in HailCorporate where a brand name is juxtaposed with something lewd or offensive. Imagine that someone decides to mock a company by taking a picture of Nazis and replacing the swastikas with the company's logo. Of course it's not a real ad for the company. They didn't pay someone to draw them as Nazis. But it can *act as an ad* by bringing the brand into the viewer's mind.

  Perhaps you've heard of the [Streisand Effect](https://en.wikipedia.org/wiki/Streisand_effect), named after Barbra Streisand after she tried to prevent some photos of her house from being published, but in her efforts attracted more attention to them. Nowadays, the people who know the term Streisand Effect surely outnumber the people who knew or cared about the house. The context for the original publicity can be completely forgotten while the publicity itself remains, and people remember Streisand's name.

  Publicity with regards to brands works in the same way. Maybe that company did something bad and the author was inspired to depict them as Nazis for their actions. The author's intention may have been to shame or mock the company, but it doesn't matter. For every 1 person that knows the details of the situation, there are 10 or 100 people who chuckle at the funny picture and move on, but don't otherwise care, and won't internalize the bad thing the company did, and represent a +1 exposure event for the brand. This is especially true when the post gets a lot of upvotes that carry it out of the topic group and into the general sphere of everybody else. Even if the author of the Nazi photo decides to continue mocking the brand and "voting with their wallet" by not buying their products, they've created a huge attention multiplier in favor of the brand.

  It's like a spinoff of the [Miranda warning](https://en.wikipedia.org/wiki/Miranda_warning): "anything you say or do can and will be used to help promote the brand". When all is said and done, the offensive "can't possibly be an ad" content still acts like an ad by making people think of the brand when they otherwise wouldn't have, and the impression can remain after the bad part is forgotten [footnote_link].

  Is this to say that we shouldn't speak up when a brand does something bad? It's a tricky subject. If the goal is only to hurt the company, I believe the safest course of action is simply to never utter their name again. Brands hate nothing more than not being talked about, and you've got the right to remain silent. Earlier I talked about recognizing our limits, and in this case we should accept that most of us aren't capable of launching a crusade against a brand without accidentally creating more converts for them. If the problem is a specific product they've made, then a review video clearly demonstrating the failure can be effective, but for abstract topics I'd stay clear.

  On the other hand, if the goal is to rescue people who have been duped by the company, proceed with caution. It's hard to get publicity out about the company's bad deed without creating disproportionately more exposure events on the fringes. I don't have an answer here, but my advice would be to stick to well-written and well-documented text content rather than images, since images are more easily consumed by the passersby.

3. Ads have trained us how to take pictures of objects. That is, with the logo facing the camera. If you notice that your box of Toasty Bites fits perfectly on your pantry shelf, take a moment to think before snapping the picture and drafting a title. You've found a funny coincidence involving the size of two things. Does anybody else on the planet care that one of those things happens to be Toasty Bites, or is it sufficient for them to know that it's cereal? Other than scientific reproducibility, what does advertising the brand name contribute to this charming coincidence you've discovered in your kitchen? I for one am at a complete loss as to why people do this, and yet it's amazingly prevalent [footnote_link].

  I am reminded of Tom Scott's video about the [cooperative principle](https://www.youtube.com/watch?v=IJEaMtNN_dM) of language, which discusses the balance of explicit and implicit information in our words. Interesting that the shelf never gets proper attribution for its role in the event, right? Where are all the "My box of Toasty Bites fits perfectly in my Home&House pantry" posts? Ah, but the pantry doesn't have a logo on it [footnote_link]. We've been trained by advertisements to think that if a product is in frame, it ought to be turned to the camera and the name ought to be read out loud. Advertisers do it that way because they're paid to, but you're not. Feel free to shoot the back side of the cereal box next time.

Once you've gotten past the "awareness" stage of HC, there's not much point visiting the subreddit any more. To do so is a little self-defeating: a bunch of anti-ad people gathered around to look at pictures of brands. In the act of collecting links for this article I've exposed myself to more radiation than I would have over a normal week. Besides, I personally am no longer interested in reddits-about-reddit. It's the kind of subreddit that you read for a little while and then leave, and that's okay because you'll be leaving with a new perspective on inadvertent advertising.

These days I make a very conscious effort to de-brand my vocabulary. And by conscious I mean that it really does require me to slow down and think about what I say. I no longer use "Google" as a verb, I just say "search the internet" or "search for" or even just "look it up" [footnote_link]. Of course I'm aware of [brand genericization](https://en.wikipedia.org/wiki/Generic_trademark), so maybe I could help accelerate the effect by using the brand name more often, but, eh, no thanks. It does lead to an interesting dissonance where the genericizations that occurred before I knew them feel normal, but the ones which occur now or in the future feel gross. One of my current borderline examples is photoshop, which I hesitate to reduce to just "photo editing" because I want to distinguish between more sophisticated edits and what the average Joe can get out of [Kid Pix](https://en.wikipedia.org/wiki/Kid_Pix).

[footnote_text] Well, it doesn't help that HC's current tab-title is "ads, ads, everywhere"...

[footnote_text] For clarity, I'm not questioning the discussion of the stove itself. Home appliances are significant, meaningful purchases, and the whole point of the povertyfinance community is to do well with less. No, my criticism here is that OP could have taken a picture of themselves making a delicious home-cooked meal on their new stove, but they just couldn't wait for that and had to talk about the act of buying instead. This is something we should all learn from, and consider what it is we care about enough to share.

[footnote_text] One last note: advertisers don't expect ads to make you immediately jump out of your seat to buy something. People like to make fun of car commercials because "Wow, look how happy this family is! I should buy a car!". No, the point is that *when the time comes*, the first options that come to your mind will be the ones you've seen the most frequently. Unfortunately for the Nazi photo editor, bad exposures contribute to this frequency just as well as the good ones.

[footnote_text] Before you think I'm strawmanning, here's [one](https://old.reddit.com/r/Perfectfit/comments/grju19/ "This Guinness in my fridge..."), [two](https://old.reddit.com/r/Perfectfit/comments/grzlv1/ "My Nintendo consoles in my new entertainment center"), [three](https://old.reddit.com/r/Perfectfit/comments/gryx0a/ "Papa John's sauce in the bottom of my cup"), [four](https://old.reddit.com/r/Perfectfit/comments/griiaq/ "A box of Chex perfectly fits"), [five](https://old.reddit.com/r/Perfectfit/comments/grq6lh/ "O'Reilly Auto Parts got game."), [six](https://old.reddit.com/r/Perfectfit/comments/grqk3b/ "Charger Doctor in the house!"), [seven](https://old.reddit.com/r/Perfectfit/comments/gqybac/ "Sold this online, and received a package from Amazon today, and the box was the perfect fit for it. So Satisfying!!") posts on /r/Perfectfit within a 24 hour period! Big shoutout to [this dude](https://old.reddit.com/r/Perfectfit/comments/gs6xxe/ "My pantry shelf and this bottle of vinegar.") who resisted the temptation.

[footnote_text] Take a look at the things around your house, and notice what has a conspicuous logo or maker's mark, and what doesn't. I find that when something is ubiquitous, essential, or adds obvious value to our lives, it is less likely to have a logo. The less inherently valuable something is, the more likely it will feel the need to aggressively advertise itself.

[footnote_text] Context is important, and I'm not so dogmatic as to let this get in the way of communicating my point. For people who are not tech savvy, "go ahead and google xxxxx" is more easily understood than "go ahead and search for xxxxx" because they might not know what kind of search I'm talking about. Remember to know your audience.

## Hall of shame

An advertising hall of shame could be infinitely long. This is simply a short list of material I came across or was reminded of while working on this article that I think deserve special disdain.

General internet:

- Facebook, Twitter, Instagram, etc. don't want you to see posts in chronological order, because then you'd know exactly when to stop browsing: when you see something from last time! They'd prefer to scramble things up a little to prioritize popular lowest-common-denominator posts, prevent you from ever feeling truly caught up, and hide ads in the mix all the while.

- Mobile games have devolved into [slot machines](https://www.youtube.com/watch?v=gvQxtotEX-M "Tristan Harris on CBS with Anderson Cooper") with delays, timers, and special events to keep people returning to them frequently throughout the day, achieving enough in each play session to strengthen the addiction but not enough to feel done with the game.

- Low quality articles or listicles are often split over several pages so that you can get a fresh load of ads on each page and they can measure how far people are reading (then they can know which corners to cut next time). I'm already sick of pathetic holdovers from physical print in the digital era anyway, but paged online articles are egregiously useless.

Google:

- AMP pages are pages which Google has downloaded from the publishing website and saved in their own caches, so they can serve the content to the user via Google servers. The stated purpose is to make web browsing faster for the end user (because Google's servers are faster than yours). One way to make your website faster and more AMP-eligible is to use sanctioned ad distributors, say for example, oh how about Google Ads? And because the user is actually visiting Google's servers and not yours, Google gets first pickings on all the metrics they want to harvest from the user. Don't worry, publishers, no one's forcing you to use AMP, but oh don't forget that AMP pages will rank higher in search than non-AMP pages because Google owns the search too :-).

- Google brought updates to Chrome and AMP to make [AMP URLs appear as if they were being served from the original domain](https://news.ycombinator.com/item?id=20256917). This continues their mission of keeping people comfortably swaddled in Google-hosted content without giving their poor fragile hearts a scare by showing them the actual google.com/amp URL they're visiting.

Microsoft:

- Windows start menu advertisements:

    ![](windows_start_menu.jpg)

- [Outlook just asked me if I want to upgrade to bigger ads](https://news.ycombinator.com/item?id=30388788)

    ![](outlook_inline_ads.jpg)

- [Microsoft is testing ads in the Windows 11 File Explorer
](https://www.bleepingcomputer.com/news/microsoft/microsoft-is-testing-ads-in-the-windows-11-file-explorer/)

    ![](windows_explorer.png)

Youtube, the system:

- "The algorithm" takes by [CGP Grey](https://www.youtube.com/watch?v=KW0eUrUiyxo), [Tom Scott](https://www.youtube.com/watch?v=BSpAWkQLlgM), [Folding Ideas](https://www.youtube.com/watch?v=LKp2gikIkD8).

    I'd like to take this opportunity to ~~advertise~~ *tell you about* my own program, [YCDL](https://github.com/voussoir/ycdl), which presents me with a custom interface for subscribing to, watching, and downloading videos. Imagine watching youtube without a "recommendation" feed, autoplay, unrelated spam, or algorithmic determination of what does or doesn't show in the sub box. As long as you can tolerate the slower channel refresh cycle.

    I'd also like to ~~advertise~~ spread the word about [SponsorBlock](https://sponsor.ajay.app/), a browser extension which automatically skips in-video sponsorship segments based on crowdsourced reports. The database can be freely downloaded so you could hypothetically implement a system for sponsorblocking locally saved videos. This would be great, since I was just about ready to starting excising them with ffmpeg.

Youtubers, the people:

- [Elsagate](https://en.wikipedia.org/wiki/Elsagate) ([Folding Ideas](https://www.youtube.com/watch?v=LKp2gikIkD8 "Weird Kids' Videos and Gaming the Algorithm")).
- [Strange Asian Holes](https://www.youtube.com/watch?v=tSI-kj9A_pc "STOP DOING THIS - Strange Asian Holes - iDubbbz").
- Five minute crafts ([How To Cook That](https://www.youtube.com/watch?v=pvqa8dsBtno "Debunking Fake Videos & WHO'S behind 5-min crafts?"), [Folding Ideas](https://www.youtube.com/watch?v=4EXVrzOACv4&t=15m42s "Cooking Food On The Internet For Fun And Profit")).
- [Copycats](https://www.youtube.com/results?search_query=primitive+technology) riding on the coattails of [Primitive Technology](http://youtube.com/channel/UCAL3JXZSzSm8AlZyD3nQdBA). Notice their awkward titles creaking under the weight of SEO keywords, their clickbaity photoshopped thumbnails, and their "child holding item to camera with a Wow face" cheapshots. OG PT would never do this. ([JonTron](https://www.youtube.com/watch?v=RiGDwQy6eoE)). (Temporal note: youtube has reduced the search ranking of the copycats since I included this so you will have to scroll down a bit. Great!)

Reddit:

- [In 2017](https://old.reddit.com/r/modnews/comments/704bt8/experiment_new_and_improved_onboarding_for_reddit/dn0a7yu/), reddit removed the word "(optional)" from the email field of their registration form, despite the fact that it's still optional. One justification is password recovery, the other is advertising and data collection.

- reddit now places advertisements (oops, I mean, "promoted posts" (promoted by advertisers)) in line with real posts. I don't know when this started, but ads used to be relegated to the sidebar only.

- Newreddit is designed mobile-first and media-first, designed for scrolling through images and videos on your phone. The [Fluff Principle](http://www.paulgraham.com/hackernews.html) says that easy-to-judge content will dominate a vote-based system, and reddit is more than happy to enable that.

- Newreddit has implemented a feature where clicking on the "X comments" link from a listing page will display the comment thread in a sort of modal, and clicking outside the modal will close the comments and show the listing again (in the [SPA](https://en.wikipedia.org/wiki/Single-page_application) style where you've never actually navigated off the first page). They want it to be as easy as possible for you to bail on a topic and come back to the firehose laced with ~~ads~~ promoted posts.

- Newreddit likes to show a measly two comments to logged-out users before suggesting that they redirect to another post, because dilly-dallying in the comments section doesn't make them money. This isn't on on some kind of overview page, this is on the actual /comments URL where you'd expect all 51 comments to be visible. This example gets bonus points for the fact that they're suggesting I leave a text post to see a fluff image post.

    ![](newreddit_only_two_comments.png)

- Moderators begged site staff for multiple *weeks* to have more control over the kinds of awards that can be put on posts, because some awards are being used to troll sensitive topics ([one](https://old.reddit.com/r/ModSupport/comments/fut93p/please_consider_giving_subs_the_ability_to/), [two](https://old.reddit.com/r/ModSupport/comments/ghn9be/inappropriate_reddit_community_awards_used_for/), [three](https://old.reddit.com/r/ModSupport/comments/gj3h05/now_getting_harassing_message_sent_through_reddit/), [four](https://old.reddit.com/r/ModSupport/comments/gve2id/can_the_admins_please_disable_certain_awards/), [five](https://old.reddit.com/r/ModSupport/comments/hc4efv/reddit_community_awards_continue_to_be_used_for/), [you get the point](https://old.reddit.com/r/ModSupport/search?q=awards&restrict_sr=on&include_over_18=on&sort=relevance&t=all)). After hemming and hawing and espousing continued "support" and "appreciation" and "we hear you"s, staff have finally put the Yikes award [on pause](https://old.reddit.com/r/ModSupport/comments/gwlvtq/put_your_money_where_your_mouth_is_remove_the/). Just that one, and not the others. It only took them an unjust death and nationwide protesting and rioting to finally lift their finger towards disabling a single source of income [footnote_link].

- In [2020](https://old.reddit.com/r/modnews/comments/hmd17x/karma_experiment/), site staff started an experiment that adds "award karma" as a separate karma category. "Our goals with this change are to recognize awarding as a key part of the Reddit community and to drive more of it, ... Awarding is an important part of our direct-to-consumer revenue; it complements advertising revenue and gives us a strong footing to pursue our mission into the future. By giving awards, users not only recognize others but also help Reddit in its mission to bring more community and belonging to the world". Oh, so that's what the awards system developers have been working on while ignoring all the other issues. Got it.

Smart appliances:

- ["At Samsung, life runs through us. Your advertising should too."](https://www.youtube.com/watch?v=N9kiSEhbLXs "Samsung Ads Life Runs Through Us Web")

    ![](samsung_advertising_1.jpg)

    ![](samsung_advertising_2.jpg)

    [No one knows the Samsung household better](https://www.samsung.com/us/business/samsungads/). Not even the families that live there.

    ![](samsung_advertising_3.png)

- [Android TV's homescreen ads are rolling out](https://9to5google.com/2020/08/18/android-tv-homescreen-ads-turn-off-staff-picks/)

    ![](android_tv.png)

- [Vizio TVs are now showing banner ads over live TV]()

    ![](vizio_jump_ads.png)

Retail IRL:

- [Cooler Screens](https://www.coolerscreens.com/) creates giant display screens that cover up the refrigerators in grocery stores so they can ~~show advertisements instead of what's actually in the fridge~~ provide the retail experience consumers want and deserve.

    ![](cooler_screens.png)

- Other destruction of public space:

    ![](mobil_gas.jpg)

    ![](urinals.jpg)

    The subway stations in Toronto, Canada [show advertisements](https://www.youtube.com/watch?v=tXcmyUtCmCo "Designing Better Next Train Arrival Screens - RMTransit") on the signs that are supposed to help you find your train. The vestigial timing clock is relegated to a third of the screen.

    [![](toronto_subway.jpg)](https://www.youtube.com/watch?v=tXcmyUtCmCo)

Here's a fun comment from Hacker News user skizm that I wasn't sure where else in this article to quote:

> I really do feel like there are two versions of the internet. One for people who aggressively use ad-blockers, pay for premium (non-ad) versions of things, manage their inboxes well, and generally are tech savvy enough to avoid 95% of unwanted advertising. Then there's everyone else who just accept the hundreds of ads washing over them at all times, that 60% of their screen real-estate is for ads, are completely comfortable with auto-playing videos, that are okay sitting through 30-second ads before watching a random funny video on youtube, etc. The second category can be sub-divided by motivations (some don't know there's a better way, some don't think it's worth the effort, etc.), but the resulting experience is the same no matter where you fall in group 2.

> Here's the (a?) kicker: advertisers are willing to pay orders of magnitude more to get ads in front of group 1. They'll pour so many resources into it that they'll make everything "worse" for group 2. Group 1 adjusts their filters (both technical and mental), get back to neutral, but the rest of the internet is just a little worse off going forward because advertisers and publishers saw a very slight up tick in clicks after their scorched earth campaign to reach group 1. Rinse and repeat until we find ourselves where we are now.

> I used to think that over time group 2 members would trickle into group 1, sort of like how programmers and hackers were using Google before it was cool and slowly the world followed, but that doesn't seem to be happening. Personally I'm seeing the groups continuing to divide. Group 2 really just doesn't see the problems, doesn't care, or isn't willing to put in the slightest effort to improve their interactions with technology and the internet.

> My "favorite" outcome of all this is when a member of group 1 is forced to use a device owned by someone in group 2 and are horrified at what they see (favorite because it is equal parts sad and funny).

> https://news.ycombinator.com/item?id=31070801

[footnote_text] You might think that reddit gold and their other newfangled abominations don't belong on an article about advertising, since it's a form of direct monetization for the site, essentially a donation. That's partially true, but the important difference between reddit gold and just donating money to reddit is the visibility of that golden badge. When you see someone else's post with a nice shiny gold on it, that's a prominent reminder that regular people, just like you!, can make a post so cool or funny that it earns a gold star from a total stranger. Gee whiz, if only I were that cool or funny! I'd better stay on reddit and keep trying until I get one too! Many young people will get sucked into the trap of striving for this pseudonymous congratulations and fame, and making ad impressions the whole while. As if the upvotes weren't bad enough.

## Enacting change

I believe that the world is simple and there really aren't that many underlying, secret forces. The big things in our world are simply made of smaller things. Advertising is not an indivisible phenomenon that we can pack away into a clean little box and banish from society. It is an emergent property of incentives, [game theory](https://en.wikipedia.org/wiki/Game_theory), [Dunbar's number](https://en.wikipedia.org/wiki/Dunbar%27s_number), psychology, information, trust, greed, and consumers who don't stand up for themselves. It is difficult to stamp out because it is a result of our natural traits.

But we have a lot of natural traits that we suppress in the name of decency or common good. We don't pee on the ground, for one. We have outlawed murder, burglary, kidnapping. We don't even allow child labor. These things are crimes because even though a few members of society benefit from them, the majority of society doesn't, and the majority got together and put it on the books. Advertising is similar. The beneficiaries are few, the violated are many, we just have to do something about it.

Some will say that banning advertisements is impossible because we run into challenges regarding the nature of free speech. What, am I not allowed to say I like a product any more? This is the kind of question people will smugly ask when you suggest that ads should be banned, because it's an easy strawman and the answer is no. I will continue to be in favor of word of mouth. But as soon as the brand starts paying people to say those things, or giving them free items in return, it's advertising. Others will say that there is no point in banning advertising since it would go underground and be hard to audit. To this, I remind you that we already ban other kinds of fraud and bribery, and I think it will be difficult for Coke to spend four billion dollars underground. [The Pareto principle](https://en.wikipedia.org/wiki/Pareto_principle) reassures us that we can make a big difference without auditing 100% of everything.

Outlawing advertisements, or at least clamping advertising expenditure, will not happen quickly. In the meantime, we as the public should block as many advertisements from our lives as we can, to reduce the amount of money the publishers and sponsors earn and drive them into the ground unless they get their act together. If they have any survival instincts, they'll come up with a new plan. If they don't, RIP.

I have said much about banning advertisements, or legislating limitations against them. Indeed, it is easy to sit back and pray that an abstract force from on high will come and solve the problem for us. But I spent some time thinking about [politics](/writing/everything_is_politics) recently, and I want to say again here that there is no politics external from ourselves. We are the politics and we are the legislation. If you stop watching ads, and teach your children to not watch ads, and they teach their children to not watch ads, the next generations of politicians will be politicians against ads. Be a role model.

Please,

- Install [an adblocker](https://github.com/gorhill/uBlock).
- Install [SponsorBlock](https://sponsor.ajay.app/).
- Use tools to [cut advertisements out](/writing/download_podcasts#cutting_ads) of other forms of media.
- Stop reading, watching, and listening to publishers that make their ads unskippable.
- Download the things you care about to preserve them from tomorrow's link rot.
- Donate a few dollars to people who make things you like.
- Encourage others to do the same.

In discussions of politics, you will sometimes hear people say "if you don't like it, get out". This is a [small-minded position](https://en.wikipedia.org/wiki/Thought-terminating_clich%C3%A9), and if you've read the 19,000 words leading up to this point in the article, you probably don't say that. These people think that the past [twelve thousand years](https://en.wikipedia.org/wiki/Cradle_of_civilization) of tumultuous human history have come to a sudden stop, and the present situation will remain static from here on out. Unlikely. In a sense, installing an adblocker is one part of "getting out". It is removing myself from the environment where I see ads. I did not need to write this article. I could have sat down and shut up and turned off my computer and stopped going outside, and I'd be "out". But I'm not content with that. The world is not static, it is going to change, and I'd like to contribute to the way it changes.

Are ads truly necessary for our survival? If everyone followed these steps, would the world grind to a halt, burst into flames, go up in smoke, go down the drain? There's only one way to find out! Follow your heart. Don't waste your time thinking about whether you have some moral obligation to watch an advertisement in order to keep the world functioning properly. If you don't want to see ads, then stop seeing ads. Let the rest of the world figure out for themselves how they're going to keep their heart pumping. Their income is not your responsibility.

Here's a message from Jackie Chan, [speaking to filmmakers](https://www.youtube.com/watch?v=Z1PCtIaM_GQ&t=8m16s "Every Frame a Painting - Jackie Chan - How to Do Action Comedy"):

> Whatever you do, do the best you can, because the film lives forever. "No, because, that day was raining, and the actor didn't have time...". Would you go to every theater to tell the audience? No! The audience sees in the theater good movie, bad movie, that's all.

I think about this quote very often because it applies to every kind of published work and, indeed, our whole economy. As agents in a free market, we do not need to contort ourselves into sympathizing with whatever decisions led to the inclusion of advertisements in a product; we just need to say "bad movie" and pick something else. It is the seller's responsibility to make good work and earn our favor.

## My virtues

Here are my promises to you, reader.

If I come up with a program or website that I think is a worthy venture to make money from, I'll do so via one-time purchases, well-justified subscriptions, or [donations](/donate), not advertisements. And as you know I publish plenty of what I make [for free](https://github.com/voussoir).

The website you are reading now will always be free of third-party ads. If your adblocker ever reports more than 0 hits, it's probably due to URL patterns or CSS names, so please let me know and I will fix it. Obviously this is a website about myself so in a sense I'm generally advertising myself, but it's your choice to come here and read about me.

I would like to try my hand at making videos from time to time again, and I have thoughts about getting into other forms of online media like podcasting or making short films. If and when I do, they'll be free of ads.

Will I ever work for a company that makes some of its money from ads? Almost certainly yes, since that's the state of almost every organization and unfortunately I can't let my idealism keep me incomeless. But I will seek organizations and positions that provide value to the world, and will avoid those that seem corrupt.

## Conclusion

I started working on this article in March 2020, and I'm very glad to be through with it. It's one of the reasons I started writing at all. I've picked it up and put it down and felt guilty about not completing it too many times. One of the things I find difficult about writing is that because I spend so much time thinking about the topic, by the time I'm done I feel like the ideas are boring or lame. I have to remind myself that the creators of the stuff I watch and read probably feel the same way, and I should finish this article instead of sitting on it forever. I hope at least some part was interesting or new to you. Or maybe it is lame!

I honestly think that enforcing a maximum dollar cap on advertising expenditure is worth a try. I'm willing to accept that some amount of advertising is necessary for businesses to exist, and for me to be able to buy things instead of having to grow my own food and make my own furniture and invent my own internet; but we need to keep them on a leash. So many of us are sick of mega-billion dollar companies ruining the world and then publishing ads of smiling babies. The amount of advertising we are subjected to is not fundamentally necessary, and any claims that it is are pure spin. As they say "it is difficult to make a man understand something if his salary depends on his not understanding it".

Marry and reproduce.
