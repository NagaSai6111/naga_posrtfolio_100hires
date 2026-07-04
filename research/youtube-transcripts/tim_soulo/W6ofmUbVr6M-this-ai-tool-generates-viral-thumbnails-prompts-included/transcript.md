# This AI Tool Generates Viral Thumbnails (Prompts Included)

- YouTube: https://www.youtube.com/watch?v=W6ofmUbVr6M
- Video ID: W6ofmUbVr6M
- Upload date: 2026-05-27T05:00:01-07:00
- Transcript source: supadata
- Status: ok
- Language: en
- Fetched at: 2026-07-04T14:05:55+00:00
- Supadata billable requests: 1

## Transcript

[00:00] So, most AI thumbnail generators, they
[00:01] just spit out very generic images that
[00:04] look exactly the same as everything else
[00:06] out there. And so, I actually built one
[00:08] that's trained on 8 years of YouTube
[00:10] best practices. [music] So, it's stuff
[00:12] that I've learned from spending tens of
[00:13] thousands of dollars with the
[00:15] consultants behind some of the biggest
[00:17] channels online. So, let me show you.
[00:19] So, right now I'm creating a video
[00:20] called why I switched from ChatGPT to
[00:23] Claude, and it's a talking head video on
[00:27] exactly that.
[00:29] And I want myself to be in the image.
[00:32] So, I'm going to drag that and hit
[00:34] generate three thumbnail concepts.
[00:37] And right now it's generating the images
[00:38] with Gemini. And we actually have some
[00:40] decent thumbnails. They're all three
[00:42] completely different concepts. People
[00:44] typically look like me, but I'm using
[00:46] this mostly for prototyping. You can
[00:47] download the thumbnail if you want to
[00:49] know why it works based on YouTube best
[00:51] practices. I've trained it to do that.
[00:53] This is the image prompt that it came up
[00:54] with that it'll give to Gemini to
[00:56] actually generate these. All right, so
[00:57] let's go to YouTube and let's try
[00:59] something different here.
[01:00] Living with Tom Brady for a day. Yeah,
[01:03] let's try that. So, let's say living
[01:05] with Tom Brady for a day. Let's just say
[01:08] that we want to do something like this.
[01:09] We'll hit generate. It's going to ask
[01:11] Claude for thumbnail concepts. I'm
[01:13] really curious what this is going to
[01:14] look like. Yeah, and look at that. So,
[01:16] Tom Brady's crazy diet, living with Tom
[01:18] Brady for a day. Tom Brady's in the
[01:20] background. I train like Brady.
[01:22] 24 hours with Brady. I don't really like
[01:24] that one, but the other two are actually
[01:26] kind of decent and they do follow the
[01:27] YouTube best principles, which I'll get
[01:28] into
[01:30] in a bit. So, here's the prompt that I
[01:31] used to build this thumbnail generator.
[01:33] So, I said, build me a YouTube thumbnail
[01:35] generator as an internal console
[01:37] application for my team. What it does,
[01:40] so it's going to generate three distinct
[01:43] thumbnail concepts, and it's going to
[01:44] render each as a downloadable mock-up
[01:46] styled like a real YouTube feed tile.
[01:49] And for each concept, I want to know in
[01:51] roughly two to three sentences why it's
[01:53] going to earn clicks. So, it has
[01:56] psychological hook, etc. The inputs, I'm
[01:59] going to give it a working title. I can
[02:00] give it a script or a description, and
[02:02] based on my experience, it works much
[02:04] better with just a short description.
[02:05] And a reference image of a person if I
[02:07] want that person to be in the thumbnail.
[02:08] So, it's going to use the latest Opus
[02:10] model from Anthropic, which is also
[02:12] Claude, uh to generate three concepts
[02:16] following the best practice uh packaging
[02:19] document I'm uploading. So, you can see
[02:20] that I I uploaded a document up here,
[02:23] and this is basically like a summarized
[02:25] version of years of notes that I've been
[02:27] taking. And for each concept, Opus
[02:30] should write a detailed image prompt.
[02:32] So, basically, Opus is is coming up with
[02:34] these concepts, and then it's going to
[02:36] write a prompt for Gemini, and it's
[02:38] going to pass that image prompt over to
[02:40] Gemini, and it's going to actually
[02:41] produce the thumbnail. So, that's how
[02:43] this is going to work. Obviously,
[02:45] thumbnails should be 16:9, and the text
[02:47] overlay should be baked in directly to
[02:50] the generated image. In terms of output,
[02:52] we're going to see three thumbnails side
[02:54] by side that kind of look like a YouTube
[02:57] feed, and each one should have a
[02:58] download button where you can download
[03:00] them. Each card should be expandable
[03:02] about why this works. And we're also
[03:03] going to have a history tab uh where we
[03:05] can, you know, generate different
[03:07] thumbnails and see everything that's
[03:08] been done. And then finally, I just
[03:09] mentioned again that I'm going to be
[03:11] uploading the best practices document
[03:14] for the AI to actually do this. And the
[03:16] tool that I actually ran this in is
[03:18] called Agent A, and it's an AI agent
[03:20] that has unrestricted access to Ahrefs
[03:22] data. So, it can actually pull real SEO,
[03:25] Google, and marketing data, which is
[03:27] super powerful for any marketer. Uh and
[03:30] rather than just like generating
[03:31] reports, it can actually build stuff. It
[03:33] can do stuff for you. And I'm going to
[03:35] show you why this matters a lot for
[03:37] YouTube in a bit. So, I'm going to walk
[03:39] you through the build now. So, it starts
[03:41] off, says that it understands what I
[03:43] want, and then it kind of asks me
[03:45] questions like Claude has planning mode,
[03:47] and it asks me about style. So, like how
[03:51] do I want it to look here? I just said
[03:53] that I wanted to have a generic
[03:54] placeholder, so do you want to upload
[03:56] like your brand logo and stuff? I don't
[03:58] really need that, not a huge deal.
[04:00] Um should you be able to delete stuff? I
[04:02] said no, let's let's keep the history
[04:04] permanent so we can actually see the
[04:05] different um versions that we have,
[04:08] especially right now it generates three,
[04:10] so let's say that I wanted to generate
[04:11] three times and I'd have nine thumbnails
[04:13] to look from. I can see them all side by
[04:15] side on one screen and actually decide
[04:18] what I want. And then there's just one
[04:19] other technical question here about um
[04:22] Gemini. So it has all the answers that
[04:23] it needs, it goes through and it
[04:25] actually starts building everything.
[04:27] Very similar to the way that Claude
[04:29] works and it makes sense because we're
[04:30] using the Opus 4.7 model. Whole bunch of
[04:33] different models that you can use here,
[04:34] there's actually a free one here, too. I
[04:36] haven't tried and it's basically just
[04:38] walking you through the thought process
[04:41] and everything that it's actually doing
[04:42] to build what it needs to do. Roughly 16
[04:45] minutes to complete the build of this
[04:49] thumbnail generator tool. And this app
[04:51] only cost me $3.29
[04:54] to build. And so this is what we ended
[04:56] up with. You just enter a title, a
[04:58] description,
[04:59] you can upload an image if you want and
[05:00] then it'll actually build a thumbnail
[05:02] for you. So let's try to go into YouTube
[05:04] here.
[05:05] Um can we survive a one-star golf
[05:08] course? Okay?
[05:10] Build the thumbnail here. Can we survive
[05:13] a one-star golf course?
[05:16] I love YouTube golf, by the way. I'm
[05:18] going to drag and drop an image of me
[05:20] here. Just use that same green screen
[05:22] one and it's actually really good at
[05:24] changing the expressions. It's pretty
[05:26] standard photo of me, right? Making like
[05:27] a a no expression face, like
[05:30] right? Nothing crazy there, so I'm going
[05:32] to hit the generate thumbnail. Our
[05:34] original sample is right here.
[05:36] Yeah, you know, like these thumbnails
[05:38] are actually like quite decent, like
[05:42] I really like this thumbnail.
[05:44] Uh I would totally use this. Anyway, let
[05:46] me walk you through some of the YouTube
[05:47] best practices so you can see that it's
[05:49] using um contrasting colors, so the blue
[05:52] and the green here. It has the hint of
[05:54] yellow here. One thing that a lot of
[05:57] people who create thumbnails do is they
[05:58] put too much inside the thumbnail. So,
[06:01] in the actual training document, it
[06:03] should limit it to only three focal
[06:05] points. So, if you look at these
[06:06] thumbnails,
[06:08] at least the first two, that's exactly
[06:09] what you get. So, you get me in all
[06:12] white, which contrasts from this color.
[06:14] You have the club here, and then you
[06:16] have the dirty course, like with long
[06:18] grass. Here, I actually really like this
[06:20] thumbnail. We have a bigger close-up
[06:22] photo of me
[06:24] pointing towards what? A golf cart
[06:26] that's sinking here. So, we have focal
[06:28] point one, focal point two, large or
[06:31] really good contrasting colors here,
[06:33] short text. Some people put in way too
[06:35] much text. People aren't reading that.
[06:37] And so, this is basically how it works.
[06:40] It And if we go through the history,
[06:42] you're going to see some of those best
[06:43] practices come into play here. Same
[06:45] thing here. We have one, two, three. For
[06:48] these ones here, uh do YouTube ads
[06:50] actually work? We made a video on this
[06:51] as well. And I actually really like this
[06:55] thumbnail here. It's really bright. So,
[06:57] using bright colors is good. Yeah, so
[06:59] that's basically it. But, I want to show
[07:00] you why I built this in Agent A rather
[07:02] than Claude or another tool. And so, if
[07:04] you remember before I said that I built
[07:07] in an Agent A because it has
[07:08] unrestricted access to Ahrefs data, and
[07:10] that's actually going to be super
[07:11] helpful for YouTube. So, what I did here
[07:13] was I asked it to find me three
[07:15] high-traffic keywords in the digital
[07:16] marketing niche, cuz that's where we
[07:18] are, where the YouTube videos are
[07:20] currently ranking on Google's first
[07:23] page. So, if you've been paying
[07:24] attention, there's YouTube videos pretty
[07:26] much in every single Google search
[07:28] results page. Um and if you can rank
[07:30] your videos there, then people are going
[07:32] to click them and you're going to get
[07:33] more views doing that. So, it's
[07:34] basically video SEO plus YouTube SEO,
[07:37] and I'm asking Agent A to find me which
[07:40] keywords I should be ranking for in
[07:43] Google and in YouTube and then to
[07:45] provide me with with those keywords are.
[07:48] Give me working titles that I can use to
[07:50] rank for it. Give me the YouTube URLs
[07:52] that are ranking so I can actually see
[07:54] data on these videos.
[07:56] And then I want you to actually run it
[07:57] through the thumbnail generator that we
[07:58] just created. And so
[08:00] this is what happened. Took my my query
[08:03] and it figured out exactly what to do in
[08:05] Ahrefs. So it went into keywords
[08:07] explorer and it found digital marketing
[08:09] keywords and then it pulled the SERP
[08:11] which are the search engine results
[08:12] pages. It's just a two to three working
[08:15] titles and and then it ran it through
[08:17] the thumbnail generator. So it's
[08:18] basically creating that plan so I can
[08:20] see what it's doing. It goes in, it
[08:22] pulls all that data, bing bang boom,
[08:25] eventually it comes down to 5,197
[08:28] rows here,
[08:29] 200 different keywords and it's just
[08:31] giving me three of them. So it says the
[08:33] keyword is Facebook Ads Library, search
[08:35] volume of this,
[08:37] keyword difficulty of this, potential
[08:39] traffic of this, which I would say is an
[08:41] overestimation. It tells you the intent
[08:43] of it which is informational which means
[08:45] that we can create a YouTube video on
[08:47] this and it says that the existing
[08:48] number eight video gets roughly 328
[08:51] visits per month to that video. So let's
[08:54] see here.
[08:55] We can actually click that video
[08:57] and you can see right here
[09:00] the views to this video. It was
[09:01] published a year ago and this is the
[09:05] graph of a video that gets search
[09:08] traffic. It's passive, it's consistent,
[09:11] and it continues to grow even though the
[09:13] video was published a year ago. That's
[09:15] not how YouTube works for anyone who's,
[09:17] you know, getting views through browser
[09:18] suggested. This is very much a search
[09:21] based videos. That's affirmation for me.
[09:23] So check this out. Um it gives me
[09:25] working titles to consider. So I spied
[09:27] on the top brands and you know, you can
[09:28] just say like how you can just change
[09:30] this in and create the same video. How
[09:32] to use Facebook Ads Library to find
[09:34] winning ads. Like you can create the
[09:36] same video. You can create both if you
[09:38] want. Um but yeah, it gives me this this
[09:41] title here, Facebook Ads Library, which
[09:43] is more likely to rank. It's like a
[09:44] hybrid between search and browse. If we
[09:46] wanted to, we could have adjusted the
[09:48] prompt to say that we want
[09:50] search-focused titles if that's strictly
[09:52] what we're going for. The next one that
[09:54] it came up with is email marketing
[09:56] services. Right? We have some titles
[09:58] here like I tested 26 email marketing
[10:00] tools. We can call it email marketing
[10:03] services if you want to go verbatim. Uh
[10:05] and it comes up with these different
[10:06] thumbnail ideas, right? How to start
[10:08] affiliate marketing. It shows you all
[10:09] the search data here. And then it shows
[10:11] you different titles. And then it says,
[10:13] "To view or download the actual
[10:14] generated thumbnails, open the history
[10:16] tab in the thumbnail generator panel."
[10:19] And we can see the three that were
[10:20] generated here. So, this is actually a
[10:22] decent thumbnail for what it is. So,
[10:25] let's say I wanted to download this one.
[10:27] I can send this to my thumbnail
[10:28] designer, and he can go out, use his
[10:31] essence inspiration. I can say this is
[10:33] generally what I want, but I want to
[10:34] change the text to this or that. And you
[10:36] can actually make adjustments directly
[10:39] in the chat. So, let's say that I don't
[10:41] like the way that the tool is, or
[10:42] there's a feature that I want to add to
[10:44] it. Then I can just type in the chat
[10:46] exactly what I want, and Agent A will go
[10:48] and make those adjustments. Now, if you
[10:50] want this exact thumbnail generator, you
[10:52] can build it yourself using the steps
[10:53] and prompts that I just walk you
[10:55] through. Or if you've got an Agent A
[10:57] workspace, you can actually just
[10:58] download it by clicking on apps, click
[11:00] on install beside thumbnail generator,
[11:02] and it'll be in your workspace. And if
[11:04] there's anything that you want me to
[11:05] build for you, just tell me in the
[11:06] comments below.
