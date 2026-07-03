# Cloudflare Just Built a WordPress Killer

- YouTube: https://www.youtube.com/watch?v=E51bELugdnM
- Video ID: E51bELugdnM
- Upload date: 2026-04-03T06:10:18-07:00
- Transcript source: supadata
- Status: ok
- Language: en
- Fetched at: 2026-07-03T17:13:51+00:00
- Supadata billable requests: 1

## Transcript

[00:00] If you're using Claude Code right now,
[00:02] two things happened this week that
[00:03] affects you directly. First, Anthropic
[00:06] leaked Claude Code's entire source code.
[00:09] That's half a million lines of code, all
[00:11] the unreleased features, system prompts,
[00:13] everything. We'll go through what was
[00:15] revealed and what that means for
[00:16] business owners and marketers. Second,
[00:19] usage limits are burning faster than
[00:21] ever. We've got some practical tips to
[00:23] stretch your tokens further. And
[00:25] Cloudflare launched Mdash, an
[00:28] open-source WordPress alternative built
[00:30] on Astro, the same framework we vibe
[00:33] coded our website on. I'm Mark Webster.
[00:35] I'm joined as always by my co-host and
[00:37] co-founder of Authority Hacker, Gail
[00:39] Brandon. Gail, it was a big leak. I
[00:42] think I read the number 512,000 lines of
[00:45] code 1,96
[00:48] files. Basically, the entire source code
[00:50] of Claude Code was leaked. Like, how did
[00:54] this happen? Did they just vibe code it
[00:56] and like was that some kind of mistake?
[00:58] >> So that's what everyone was saying on X,
[01:00] but the guy who created code C code like
[01:02] Boris just said that it was a human
[01:04] error. Actually, they just [ __ ] it up.
[01:06] It happens, you know. It's just it's not
[01:07] great, but it happened. And yeah, that's
[01:10] a big big blow for Entropic who like
[01:13] historically has been one of the only
[01:15] developers of these kind of harnesses to
[01:17] keep it closed uh code like before like
[01:19] almost everyone else is open source. So
[01:21] for example, Codex from OpenAI is open
[01:23] source. you have access to the code for
[01:25] a long time. But CL code was trying to
[01:27] build a bit of a mode by keeping things
[01:28] secret and there's no more secrets.
[01:31] >> And I think it's fair to say they did
[01:32] have a decent mode. They had a very
[01:34] loyal following of users. Like even when
[01:37] you know you could argue that codeex
[01:39] openi's model was getting better for
[01:41] certain use cases like like coding still
[01:44] a lot of people just were like nah I
[01:46] think cloud's good enough for what we
[01:48] want to use it for right now. No point
[01:49] in switching. I like the features. I
[01:51] like how it works. and you know that was
[01:53] fine but now it's kind of like opened
[01:55] the floodgates to everyone kind of
[01:57] ripping off everything they do basically
[01:59] and they may I don't know do you think
[02:01] they may even have to make claude code
[02:03] open source completely or
[02:04] >> nah I think they will just start over
[02:06] like the point is like yeah now it's
[02:08] like you can give this code base to your
[02:10] AI agent and be like hey build the same
[02:11] feature on my AI agent and then it's
[02:14] like it's going to take you know half an
[02:16] hour and you get a workable version like
[02:18] you still need to refine it if you're a
[02:19] big company and so on but the point is
[02:21] it's that simple You have the whole
[02:23] blueprint. You have every single system
[02:25] prompt and how they use it and how they
[02:26] use sub agents etc. that was hidden
[02:28] behind the scenes and it's like the
[02:30] whole architecture has been leaked out
[02:31] which means in the near future probably
[02:34] all competitors will be able to rip off
[02:36] all the best features of cloud code and
[02:37] replicate them in their own way inside
[02:39] their code which means cloud has to
[02:42] rebuild their mode from scratch and
[02:43] that's kind of a blow to a company that
[02:45] has been probably doing the best job in
[02:47] the industry doing this. But at the same
[02:49] time, if you consider the rate at which
[02:50] Entropic is shipping features, which is
[02:52] pretty much every day there's something
[02:54] new in code, it will only take a few new
[02:56] features after that leak to come out for
[02:58] them to start rebuilding a mode and
[03:00] people wanting to stick to it. On top of
[03:02] the fact that even with recent rate
[03:04] limits, you still get an incredible deal
[03:06] in how much usage you get for how much
[03:07] you spend with a subscription.
[03:09] >> No, we have we do actually have some
[03:11] insights into some of those new features
[03:12] because they were also released in
[03:14] >> Yeah, because they have betas, right?
[03:16] >> Uh let's talk about some of those now. I
[03:18] want to start with Chyros, how you
[03:19] pronounce it, I think.
[03:20] >> I guess it's like an always on
[03:23] background mode and they have this kind
[03:25] of autodream feature where it kind of
[03:27] like thinks about your work while you
[03:30] sleep. Sounds kind of spooky. What's
[03:32] going on here?
[03:32] >> Well, think about how humans consolidate
[03:35] their memories. Actually, your memories
[03:37] get consolidated inside your brain while
[03:39] you sleep, which is why they call it
[03:41] auto sleep because they mimicked the
[03:43] logic of that, which is when you're not
[03:46] using it, the model kind of like goes
[03:47] back through your chat history and
[03:48] things that were done, etc. And
[03:50] essentially makes a summary of what
[03:52] happens and keeps like a much shorter
[03:54] version of that inside its memory files
[03:56] to get a little bit of continuity
[03:58] between chats and the ability to work on
[04:00] the same codebase, file system, etc. But
[04:02] again like yeah when your memor is
[04:04] considered in your brain like you don't
[04:05] remember every single detail. They kind
[04:07] of like you get a summary in your
[04:08] [laughter] brain as well. And so they
[04:10] they've just mimic that. There was some
[04:12] of that already but I guess they just
[04:14] building more systems in there that will
[04:17] allow like a feeling of continuity when
[04:20] you walk inside the project on code.
[04:22] >> Yeah. Apparently it's going to write
[04:23] like a daily observation log based all
[04:27] your all the chats you've [laughter] had
[04:28] that day, everything you've said. Yeah.
[04:31] So it's I guess you're right like is
[04:33] kind of like mimicking how humans think
[04:36] about and reflect on things they've done
[04:38] previously maybe.
[04:39] >> And I've even seen a leak another leak
[04:41] of like apparently they they're working
[04:42] on like an always on mode a little bit
[04:44] like kind of like open claw that wakes
[04:46] up and like thinks of like new features
[04:47] it could build into your codebase etc.
[04:50] So it wasn't in that leak specifically
[04:51] but I've seen other leaks that talk
[04:52] about that. So you can see that entropic
[04:55] is trying to make code work when you're
[04:56] not at your computer anymore. And that's
[04:58] quite interesting actually. They also
[05:00] have this uh ultra plan feature it's
[05:02] called, which apparently it offloads
[05:05] complex planning to uh a cloud version
[05:08] of Opus. It says for about 30 minutes or
[05:10] so. Like what does that even mean? Like
[05:12] how is it able to access your local
[05:13] context when it's doing that?
[05:15] >> I'm not exactly sure how it's going to
[05:16] work, but it looks like a little bit of
[05:19] a kind of like deep research for
[05:21] planning mode kind of like kind of like
[05:23] a deeper version of that. A cloud
[05:25] version of Office. It's always a cloud
[05:27] version. Opus never runs on your
[05:28] computer. Um, so it's like I think what
[05:31] this means is like you know when you use
[05:33] cloud code on a desktop app, you can
[05:35] choose to use your local files or to use
[05:37] a cloud version of it. It depends where
[05:39] the code runs. Is the cloud code
[05:41] instance running on your computer which
[05:43] then calls the models to do things or is
[05:45] the actual terminal that calls the model
[05:48] running in the cloud and that means for
[05:51] example if you have environment
[05:52] variables set up with like API keys then
[05:55] they need to be set up on that cloud
[05:56] environment and that doesn't use your
[05:58] local resources it's bit technical
[06:00] basically uh but it won't change
[06:02] >> like another way another way of looking
[06:04] at it is like typically when you're
[06:05] doing something you plan it and then you
[06:08] do it right so But plan often is
[06:11] kickstarted by an idea which you could
[06:13] have anywhere like in the car, on the
[06:15] bus, like out and about.
[06:17] >> So if you're able to kick off the
[06:19] planning like on your phone remotely,
[06:23] that planning happens, you know, in in
[06:25] the cloud. I know you say everything's
[06:26] in the cloud, but then you can
[06:28] >> continue that plan in the app. Though,
[06:30] you know,
[06:31] >> you can you could also do remote control
[06:33] like, you know, there's also remote
[06:35] control that would run it on your
[06:36] computer. So it's like it's just
[06:37] entropic has this cloud environments and
[06:39] I think it's helpful when you're
[06:40] collaborating with multiple people on
[06:42] the same project because then it's like
[06:44] the thing is like hosted on their thing
[06:46] um and you can continue there with
[06:47] multiple people but you know entropic
[06:50] now releases so many features that do
[06:52] the same thing. So like remote control
[06:54] is kind of like the local like you can
[06:56] run locally but remotely whereas like if
[06:58] you run in there it really depends does
[07:00] it run on your computer or does it run
[07:02] on entropics computer basically that's
[07:04] really the main thing that you need to
[07:05] think about and permissions etc will be
[07:07] different it's a little bit technical
[07:09] the idea is it will just like it will
[07:12] work probably only on entropics cloud
[07:15] environment and not on your local
[07:17] computer and it will be deep research
[07:19] for plan mode like think about it like
[07:21] that
[07:21] >> and they also have this undercover mode
[07:24] it's called coming out which apparently
[07:25] like hides the fact that it's AI and I
[07:28] think there was some kind of talk about
[07:30] they plan to just release like this
[07:32] autonomously go around and like update
[07:34] open source code and improve it and
[07:37] things like that.
[07:37] >> It looks like a dev mode. It looks like
[07:39] you know if you're developing CL code
[07:40] and you're having that because also this
[07:42] undercover mode mentions set 4.8 8 and
[07:45] Opus 4.7 for example like it actually
[07:48] says in the prompt like do not mention
[07:49] which model is used so that if you're
[07:51] using some kind of development model
[07:52] it's not going to be in the release
[07:54] notes on GitHub for example um but the
[07:57] point is they name the models in the
[07:58] instructions in the prompts for the
[08:00] models so it's like some new models that
[08:01] are not released yet are mentioned so to
[08:03] me this undercover model is kind of like
[08:05] you know what entropic employees are
[08:07] using on pre-releases of clo code that
[08:10] kind of stuff I guess not 100% sure
[08:13] again this is all interpretation is not
[08:14] like a fact for sure. We only have the
[08:17] client part of the leak, right? We don't
[08:18] know what's running on entropic servers.
[08:20] And so like we only have half the story
[08:22] here.
[08:23] >> And speaking of models, there's uh talk
[08:25] of a new tier of model uh sort of above
[08:28] opus. This is called Mythos.
[08:30] >> Can you just explain like a little bit
[08:32] about this like on what's the difference
[08:34] between that and Opus?
[08:36] >> We don't know a lot, right? Again, these
[08:37] are unreleased things. uh they haven't
[08:40] communicated about it and all we have is
[08:41] leaks and actually I think it was a blog
[08:44] post that leaked it wasn't in that
[08:46] source code
[08:47] >> and I think it was saying that it was
[08:49] only on Q3 which is quite far away
[08:52] >> and it looks like Entropic is remote to
[08:54] IPO this year so it would make sense
[08:56] that they have like some big splashing
[08:58] releases just before the IPO to inflate
[09:00] their valuation because it's quite
[09:02] dangerous when they IPO if like the the
[09:04] stocks tank when they IPO then the whole
[09:08] industry could crash. Actually, it's
[09:10] like they they need to kind of prevent
[09:12] against that and they probably send
[09:13] bagging a little bit now and they
[09:15] release their big stuff then. My
[09:17] understanding of Mitos is like it's kind
[09:18] of like one tier higher than Opus and
[09:20] it's extremely expensive to use right
[09:22] now. Like in their blog post they're
[09:24] like it's only released to researchers
[09:25] as well because it can literally just
[09:27] hack anything. I found like a bunch of
[09:29] vulnerabilities in a lot of software a
[09:30] lot of people use. So it's like they're
[09:32] almost probably preparing and kind of
[09:34] like almost communicating to all this
[09:36] open source software that people use and
[09:37] like hey there's all these
[09:38] vulnerabilities our model found that
[09:40] could be exploited when that model is
[09:42] released. So there's a security concern
[09:43] and there's a cost concern with that.
[09:45] But my understanding of this is it's
[09:46] going to be similar to the pro model on
[09:49] chapity which most people don't have
[09:50] access to. The only people who have
[09:52] access to it are the people on the
[09:54] business plans and the people on the pro
[09:55] plan that cost $200 per month at this
[09:57] point. I suspect open air is going to
[10:00] release a $100 plan this week that will
[10:02] also uh give access to this model. But
[10:04] the idea is like this is a very very
[10:06] slow model that you know reasons for 30
[10:08] 40 minutes runs a really long time but
[10:10] is arguably smarter than anything else.
[10:12] It's way smarter than Opus etc. Google
[10:14] also has something similar called Gemini
[10:16] Deep think and it's mostly used for
[10:19] research like you know genetic
[10:21] mathematics
[10:21] >> science based stuff. Yeah. So usually
[10:24] most people are too dumb to get good
[10:26] value of these models because literally
[10:28] the problems you submit to them are not
[10:30] are not like complicated enough that
[10:31] you'd see a massive difference from like
[10:32] a thinking model and it's not really for
[10:34] your day-to-day tasks. is for this kind
[10:36] of like high level
[10:37] >> and as a dumb person that's uh probably
[10:40] use of that model like do any of these
[10:42] leaks actually matter to me the small
[10:46] business owner because it's like yeah
[10:48] okay Chyros ultra plan some cool
[10:50] features there but it's like it's a bit
[10:52] of seems a bit of a whatever like I'm
[10:54] just going to keep using cloud code to
[10:56] do my mark
[10:57] >> the continuous improvement of the of the
[10:59] tooling I think what matters to you is
[11:01] that a lot of the features that exist
[11:03] today in cloud code and in this league
[11:05] are probably going to make their way to
[11:06] the competition. And what that means is
[11:08] like, you know, Entropic basically was
[11:11] building up their mode so they can
[11:12] charge more and they can start building
[11:13] up their profit margins hopefully before
[11:15] this IPO as well so that they can
[11:17] actually show some good revenue numbers
[11:19] that will inflate their valuation,
[11:20] right? They want to make money, right?
[11:21] That's pretty much the plan. And so that
[11:24] kills a little bit this plan because the
[11:27] mode was not just the models, it was all
[11:29] the features in code and you're getting
[11:31] attached to them. But now the
[11:32] competition can copy them much easier
[11:34] rather than trying to guess what the
[11:35] prompt is behind the scenes and how the
[11:37] architecture works on the stuff that is
[11:39] not shown. Now they can just literally
[11:40] read that and see how it works. Which
[11:42] means again it will take just a few
[11:44] weeks to see a lot of these features pop
[11:45] up on codeex pop up on open code pop up
[11:48] on cursor etc. Um because they will 100%
[11:52] use this. That means that they can't
[11:53] inflate their price as much because
[11:55] their mode is has been reduced
[11:56] basically. So for you as a user
[11:59] >> it probably would be a good thing
[12:00] actually. So essentially for me as a
[12:02] user uh even though Gemini even though
[12:05] OpenAI are trying to replicate clawed
[12:07] code as much as possible they it's kind
[12:09] of never been quite there and those
[12:11] subtle differences maybe would stop me
[12:14] of switching but now
[12:16] >> if they want they can replicate it one
[12:18] and therefore massive learnings for them
[12:20] friction is lower.
[12:21] >> Think about how much these engineers
[12:22] that build cloud code are paid per year.
[12:24] Think about the amount of value there is
[12:26] in looking at that code and how they've
[12:28] done it and the logic behind it and so
[12:30] on. So that's the point is and what that
[12:32] means is you'll be able to switch more
[12:34] seamlessly between these systems and
[12:36] that also means that because there's
[12:38] less mode for a company like entropic
[12:40] they won't be able to overinflate the
[12:42] price they charge you against what you
[12:44] get because the same features will be in
[12:47] the competitor's products at least until
[12:49] the point of the leak basically. Does
[12:51] this leak make you want to use cloud
[12:53] code more or less? Are you more likely
[12:55] to switch from it?
[12:57] >> I mean, to be honest, my main issue with
[12:59] cloud code right now is more usage
[13:01] limits than features. At this point,
[13:02] it's almost like most people don't use
[13:04] it to the maximum of its abilities
[13:06] already. And the challenge is actually
[13:09] to build your setup around it. Like we
[13:11] don't need more features. For most
[13:12] people, it would take years before they
[13:13] actually use it properly. Even if
[13:15] nothing was released,
[13:16] >> people are the bottleneck, not clawed
[13:18] basically. And then as you use it more
[13:20] like your token usage increase and then
[13:21] limits become more of an issue. Limits
[13:23] and like models getting dumber that kind
[13:25] of stuff. Like that's kind of like
[13:28] >> let's talk about that because that's
[13:29] been another big story over the last
[13:30] week. Um is the clawed limit crisis. So
[13:34] basically they silently introduced off-
[13:38] peak multi
[13:39] >> not silently they did it during the
[13:41] promo right like they made they were
[13:43] like oh you get two times more usage
[13:44] during off peak hours initially
[13:47] >> and then they switched it to like you
[13:49] get less usage during peak hours last
[13:51] week.
[13:52] >> Yeah. So a peak hour multiplier, a
[13:55] hidden peak hour multiplier essentially
[13:57] that during US business hours your
[14:00] tokens burned faster for doing the same
[14:03] amount of work. And this was kind of
[14:04] like a somewhat silent thing.
[14:07] >> It wasn't it was announced like I mean
[14:09] it was announced on Twitter etc. Like
[14:10] it's not like super public. They didn't
[14:12] email you but it's like if you went on X
[14:14] like there's a guy called Tic that works
[14:16] for Android and he said it. So like the
[14:19] way they introduced it is like they gave
[14:20] you two times more usage outside peak
[14:22] hours initially. So that was a bonus.
[14:24] People were happy about it and then
[14:27] >> yeah and that's what ended on March
[14:29] 28th.
[14:30] >> Yeah. Towards the end like a few days
[14:32] before the end of that promo then TK
[14:34] from Entropic was like actually we are
[14:36] reducing the usage off outside of peak
[14:38] hours. So now the 2x usage of peak hours
[14:41] is gone. So you're back to your normal
[14:43] usage during these hours and you get
[14:45] lower usage during peak hours.
[14:47] >> Okay. So
[14:48] >> I mean that's not what you said before
[14:49] like the peak hour multiplier what I
[14:51] pulled this from the there's a mega
[14:54] thread on Reddit which basically said
[14:55] that they had silently introduced this
[14:57] um
[14:59] >> sounds like what that
[15:00] >> they introduced it silently for like two
[15:02] days and eventually like oh actually we
[15:03] reduce the limits doing powers. Yeah
[15:05] that's true.
[15:06] >> Yeah. Okay fine. But I mean that I think
[15:09] it cost them a bit of goodwill. I see a
[15:10] lot of people I mean people say like I'm
[15:12] going to move away from it all the time.
[15:14] Like are they actually I don't know. But
[15:16] it's been a real problem for certain
[15:17] users. There was a few just oddball. It
[15:20] seemed to be like genuine bugs use cases
[15:22] where people were sending like a high
[15:25] message using 30% of their limits or
[15:27] like you know before they even sent
[15:29] anything they' used 100% of their limits
[15:31] and yeah okay few bugs here here and
[15:33] there. I think there were also a few
[15:34] people who were just you know had a ton
[15:36] of MCPS in the background and you know
[15:39] were just like using it very
[15:40] inefficiently.
[15:42] >> Um and that was causing some issues as
[15:43] well.
[15:44] >> Yeah. So you can see that actually this
[15:46] is an entropic employee. You can see
[15:48] like she works on cloth anthropic and
[15:50] she actually also posted that they were
[15:51] aware that some people are essentially
[15:53] getting their limits used faster. So
[15:55] they probably introduced a bug at the
[15:56] same time at which they reduced the
[15:58] limits which like went way faster. Like
[16:00] it's true like I had some days I jumped
[16:02] 25% over one task on a max plan. Um, so
[16:06] it was painful basically.
[16:08] >> And they said this affected like 8% of
[16:10] users or something, but it seems like
[16:12] most
[16:13] >> for the reduced limits, not for the bug,
[16:15] >> for the reduced limits only. So like
[16:17] when they said they reduce the limit on
[16:18] the peak time, they were like, "Oh, 7%
[16:20] of people are going to hit limits when
[16:21] they wouldn't have hit them before." Not
[16:23] for the bug. The bug were probably way
[16:24] more. I can see where the confusion's
[16:26] coming of this because there's like a
[16:27] couple of different threads here and
[16:29] like it's people aren't sure which of
[16:31] >> and also they're lawyering their way
[16:32] through because like 7% of users okay
[16:35] but like it depends where you live. If
[16:37] you live in the US and this is like your
[16:39] main walking window that's probably like
[16:40] 20% of users or 25% of users and then
[16:44] it's like you know they count all their
[16:46] Asian users but it's like middle of the
[16:47] night for example and that kind of like
[16:50] users don't use it or whatever.
[16:52] >> Exactly. Okay. So, it's like they lawyer
[16:53] their way around it the same way Google
[16:55] lawyers their way around the impact of
[16:56] updates basically. And so, like the
[16:58] reality is a lot of people are affected
[17:00] from what I've seen and people see lower
[17:02] usage limits. Now, in Europe, it like
[17:04] for us it starts at 3 p.m. finishes at
[17:06] 9:00 p.m. with the time change. Not too
[17:08] bad to be honest. I do most of my work
[17:09] in the morning. So, I can survive that.
[17:11] But for people who live in US, it's
[17:13] quite painful. It's almost like an extra
[17:14] tax basically on using AI. So, scheduled
[17:17] tasks are your best friend at this
[17:18] point. Like you can use schedule tasks
[17:19] on code or on co-work and you can
[17:22] schedule them for off peak hours and
[17:23] you'll get more usage. I you know I
[17:25] showed my notion system last week. I
[17:27] have a schedule thing. I can set a due
[17:29] date and it will just run at the time
[17:30] that I set. So that there's ways to get
[17:33] around it. It's not nearly as good but
[17:35] welcome to you know we warned people
[17:37] several weeks ago about that. And
[17:39] actually I have this case study of this
[17:40] guy who's like a big X user as well and
[17:43] he just ran a test like Codex versus
[17:46] code knowing that Codex also was running
[17:48] a two times usage uh promo until today.
[17:51] Uh so it's finishing today actually
[17:53] which is why I'm saying they will
[17:54] probably introduce the $100 plan very
[17:56] soon. There's been some hints on that as
[17:57] well. And so you can see that for the
[18:00] same task that he had 93% usage left on
[18:04] his five hour rate limit. Whereas for
[18:07] code he consumed after consuming 80% of
[18:11] his 5 hour rate limit he actually it
[18:13] wasn't done yet basically. So the
[18:15] contrast of usage limits of codeex
[18:17] versus cl code on the same task on the
[18:20] same prompt was quite significant. We
[18:22] don't know if that was affected by the
[18:24] bug hopefully it was but like you know
[18:26] the value you get out of a codeex
[18:27] subscription is a lot better. And you
[18:29] also have to consider codeex is half of
[18:31] that now. So it still would be much
[18:33] better but not as big of a contrast. So
[18:36] I want to get your take on how we can
[18:38] use tokens a bit more efficiently. But
[18:40] before that I think I have a broader
[18:42] question. Is this all just a way for
[18:46] them to kind of like stop subsidizing
[18:48] their model? Like is this the kind of
[18:50] initification of uh the data pipeline?
[18:54] >> It's a start of that. Yeah, I think so.
[18:56] It's like they've given a lot. I mean
[18:57] again a $200 subscription is like $5,000
[19:00] of API more if you use all the tokens
[19:02] which most people don't, right? Um, so
[19:04] it's like in reality you probably and
[19:06] then also the API price is not the cost
[19:09] for them. It's
[19:10] >> I think I saw something like they're
[19:12] losing you know 80 cents on the dollar
[19:14] or something on
[19:15] >> it's quite possible like something so
[19:17] essentially trying to buy market share.
[19:18] The thinking is whoever is still there
[19:21] at the end can then jack up the prices
[19:23] and have a big big
[19:24] >> and then the IPO is coming soon. So they
[19:26] need to show some numbers like by the
[19:28] time the IPO is coming towards the end
[19:30] of the year probably like again nothing
[19:31] is announced nothing is sure but like
[19:33] you know they're all kind of hinting at
[19:34] it like wink wink it's coming and so
[19:38] yeah they need to start showing like
[19:39] increased revenue numbers and they're
[19:41] going to have to squeeze it a bit more
[19:42] like obviously they still want to show
[19:44] high growth as well so it's going to be
[19:46] a balancing act for them between like
[19:48] the pricing and the growth but yeah it's
[19:50] quite interesting it's like they they
[19:52] need to make more money and all these
[19:53] companies are doing this so even Google
[19:55] for example They massively slashed the
[19:57] limits on anti-gravity because literally
[19:59] no serious person would use anti-gravity
[20:02] and only free
[20:02] >> What is anti-gravity?
[20:04] >> Anti-gravity is like a Google's kind of
[20:06] like cursor competitor. It's like a VS
[20:08] Code uh fork. But like the point is
[20:11] because it's the worst of the three.
[20:13] Only people who cannot afford OpenAI and
[20:17] Entropic would use it. And so Google has
[20:19] the worst user base that doesn't spend
[20:22] any money. And therefore they had to
[20:23] slash the limits because again they were
[20:24] just costing them a lot. So across the
[20:26] board, you know, these companies are
[20:29] slashing their expenses on people who do
[20:32] not make that money at least.
[20:33] >> Okay. Does this kind of feel a little
[20:36] bit like uh cell phone networks in the
[20:39] way that they all try to be, you know,
[20:41] be this this fancy feature loaded thing
[20:43] and then at the end of the day they all
[20:44] just become kind of like dumb data
[20:46] pipelines where, you know, all you
[20:48] really need is data to use it. And then,
[20:50] you know, they weren't too much more
[20:51] than that.
[20:52] >> I mean, everything is just becoming
[20:54] normal, right? Becoming a utility, a new
[20:56] utility that you pay for. And it's like,
[20:58] yeah, they need to kind of normalize
[21:00] their cost against their revenue. That's
[21:01] it. It's just becoming that eventually
[21:03] just the reality. Like, we're all drunk
[21:05] on free tokens right now. And then that
[21:07] party is going to slowly go down.
[21:11] >> Yeah. And I think that party might end
[21:13] quicker than a lot of people realize. So
[21:16] businesses are going to have to get a
[21:17] lot more efficient with the way they are
[21:20] using this and some businesses which are
[21:23] you know operating on very low margins
[21:25] or you know operating inefficiently it's
[21:27] just not going to be worth it to pay for
[21:29] tokens to do some of these things.
[21:31] >> A lot of people cannot run like full LM
[21:34] driven pipelines. So like skills is a
[21:36] good example right like if you run your
[21:37] skills just on markdown files it's like
[21:39] you use a lot of tokens to interpret
[21:40] that markdown into a workflow. But like
[21:42] the better way of using it is to
[21:44] actually create Python scripts that the
[21:45] model can use to like you know automate
[21:48] part of the walk without using any
[21:50] tokens. Like a lot of the skills I built
[21:52] have a lot of Python scripts because
[21:53] that just makes things more efficient.
[21:55] And it's like that's the thing right
[21:56] now. Nobody's trying to optimize
[21:57] anything because it's so cheap. But I
[21:59] suspect there will be a phase sometime
[22:02] next year probably where everyone's
[22:04] going to be like, "Oh, I have all these
[22:05] AI processes. I spend 10 grands a month
[22:07] on tokens because the prices went up so
[22:09] much." And now it's like I need to kind
[22:11] of optimize all these things. And I
[22:12] actually suspect a lot of our work next
[22:14] year is going to be communicating around
[22:16] that and helping people around that.
[22:18] Like right now it's adoption and then
[22:19] eventually it will be like optimization
[22:21] uh of these things.
[22:22] >> It's kind of like gas guzzling cars in
[22:24] the 1970s when there's like an oil
[22:26] crisis then suddenly there becomes a
[22:28] push to have you know more efficient
[22:30] vehicles.
[22:31] >> Sounds very current.
[22:32] >> Same same principle. Yeah. Um, is there
[22:34] anything people can do right now today
[22:36] though to make their token usage more
[22:39] um efficient?
[22:40] >> I think if you use clothes code, I think
[22:42] one of the big ones is like sonet 4.6 is
[22:44] actually a very good model and for many
[22:46] tasks you can use it and actually now
[22:47] they've changed how skills work and you
[22:50] can select a model for the skill. So
[22:52] even if you're set up on obus you can
[22:53] say when you run that skill this skill
[22:55] runs on set for example. So if it's a
[22:57] simple like update upload this or
[22:58] reformat this or whatever like honestly
[23:01] switching to sun I think uses limits
[23:03] like three times slower and so being
[23:04] able to kind of like granularly assign
[23:06] models to things is a good way to reduce
[23:10] that same like
[23:11] >> there's three models right so you got
[23:12] opus which is the top one son at the
[23:14] middle one and haiku which is the bottom
[23:16] one when is the use case to use haiku
[23:18] >> haiku is like simple tasks it's like you
[23:21] know again format this read this and
[23:23] summarize it go and find the research
[23:26] and find this information like it's just
[23:28] kind of like it's here to eat a lot of
[23:30] tokens very cheaply and do this kind of
[23:32] like token heavy but simple cognitively
[23:34] tasks for you that's why for example
[23:36] when your cloud code goes through your
[23:38] codebase and researches things it
[23:39] actually uses a hiker agent
[23:41] >> when it uses fetch for example you give
[23:43] it a URL and you like read this actually
[23:45] haiku reads the HTML summarizes it and
[23:47] passes it back to opus that just reads
[23:49] the summary of that which uses less for
[23:51] example um so that's why you use it so
[23:53] that is kind of like good for like if
[23:55] you have a plan that's made for example
[23:57] like if you use the plan mode with opus
[23:59] so that's pretty good at executing that
[24:00] plan and actually there is a secret mode
[24:02] in cl code if you type if you're on a
[24:03] terminal and you type /model opus plan
[24:07] it will use opus for the plan mode and
[24:09] sonet for the execution and that will
[24:11] reduce your token usage a lot like your
[24:14] limits are going to go a lot slower
[24:16] thing I didn't say as well is on skills
[24:17] you can also select thinking level now
[24:19] so you can say thinking level high
[24:21] medium low and again if it's like a
[24:22] simple upload etc like probably low
[24:24] medium is enough and that will use a lot
[24:27] less thinking token. So usually like
[24:28] kind of like switching your model is
[24:29] going to be 90% of the job. I see on the
[24:32] notes you wrote disconnect MCPS but
[24:34] actually I think by default now MCPS
[24:36] don't eat tokens. I'm not 100% sure but
[24:39] I think so. If you're not sure you can
[24:40] type slash context on your cloud code
[24:42] and it will show you a little graph of
[24:44] how many tokens are eaten by your MCPS.
[24:47] Um, but I think now tool search is
[24:49] turned on by default, which means it
[24:51] doesn't load the tools unless it needs
[24:53] them, which already is optimized.
[24:56] >> There's a few other simple things you
[24:57] can do like not using a very long chat.
[25:00] A lot of people don't realize that when
[25:02] you're sending uh, you know, the 10th
[25:04] reply in a a chat, you're essentially
[25:07] sending the entire chat history in every
[25:10] message you send from that point. So,
[25:12] you know, the further you go, the the
[25:14] exponentially more context you're using.
[25:17] So, you know, if you don't need that
[25:18] previous stuff, just start a new chat
[25:20] and it's going to burn through context
[25:22] much much slower.
[25:23] >> Yeah. Also, your cloud MD is passed with
[25:26] every message that you send. So, if your
[25:27] cloud MD is very heavy, that is a [ __ ]
[25:30] ton of tokens. So, you're better having
[25:32] a very lean cloud. MD that links to
[25:34] documentation that is read when it's
[25:36] needed. So, the point of the cloud MD is
[25:38] to almost be a table of content. Uh, and
[25:40] it's like that's also how I build my
[25:41] scales. Like my scale.md files now,
[25:43] they're very small and they just link to
[25:45] documentation. It's like, oh, when you
[25:46] need to do this, you go, you do this,
[25:48] you go read this, etc. And it just reads
[25:49] when it needs, and it doesn't load the
[25:51] context when you don't need because it's
[25:52] quite easy to bloat these things as
[25:54] well. I have some scales that I had to
[25:56] refactor that had like 700 lines of
[25:59] instructions. And I went down to like
[26:01] >> I have a few of those.
[26:02] >> I went down to like 60 by refactor. I
[26:04] made a refactor skill skill and it just
[26:07] kind of like splits it off.
[26:09] The whole purpose of skills was exactly
[26:12] this though like because it doesn't it's
[26:14] not loading all of the context. Yeah. Um
[26:16] it only has a small amount of context
[26:19] using in the beginning and then more as
[26:21] needed. So yeah, I I think like even a
[26:24] while ago these companies are they're
[26:26] thinking about the context crisis for
[26:29] one of a better word because this is
[26:31] going to I think come come up at a lot
[26:33] of people quite quickly and I don't
[26:36] think too many businesses are prepared
[26:39] for it because yeah I don't see too many
[26:42] people talking about how to use this
[26:43] stuff efficiently. Now they're worried
[26:44] about adoption but like as costs rise
[26:47] the people will start worrying about
[26:48] efficiency. It's not in people's mind
[26:51] yet, but if you start thinking about it
[26:52] as you're building things now, you can
[26:54] already like be prepared for the future.
[26:56] That's why like yeah, I've been
[26:57] reoptimizing a lot of skills that we're
[26:59] building and I'm like a lot more
[27:00] conscious of uh token optim like now
[27:02] when I test my skills, I actually have a
[27:04] counter of how many tokens are used and
[27:05] then when I evaluate the changes, I can
[27:07] see uh how it's optimized because again
[27:10] that matters.
[27:11] >> I think like eventually a lot of this
[27:12] stuff will be under the hood and happen
[27:15] automatically. I'm thinking like in a
[27:16] car like you're not controlling you know
[27:18] exact amount of fuel going through you
[27:20] just press eco mode or it's on by
[27:21] default and it's becomes you know more
[27:24] >> it will be a consultant thing actually I
[27:26] do think like there's going to be a
[27:27] whole consultant layer around the AI
[27:29] market and people will pay people to do
[27:30] this as well like AI will be able to do
[27:32] it to some extent but you know it's the
[27:34] same it's like you're still listening to
[27:35] this podcast if you're listening to this
[27:37] podcast AI could not give you all the
[27:38] information we're giving you right now
[27:39] and there's still a kind of a layer of
[27:41] experience uh and that will be here
[27:44] which is a good thing for humans It
[27:45] shows you you're not fully replaced yet,
[27:46] but you'll be able to build skills that
[27:48] help it, etc. But you're still driving
[27:50] it as a human for now at least. And if
[27:53] you want to learn more about Claude
[27:55] Code, if you're not using it at the
[27:56] moment, especially, um, if you head on
[27:58] over to
[27:59] authorityhacker.com/learnclaudecode,
[28:02] we've put a a page on our new site and
[28:05] there's a video there showing how we use
[28:08] Claude Code in our business for things
[28:10] like sales, marketing, operations with
[28:13] some of the exact processes and and
[28:15] outputs um, like shown in the video
[28:17] there. I know sometimes a lot of this
[28:19] can feel a bit theoretical on a podcast.
[28:21] So if you want to see what this stuff
[28:23] looks like in action, um, go on over to
[28:26] authorityhacker.com/learnclaudecode
[28:29] and there's a free video there and you
[28:31] can check that out. I just want to say I
[28:32] just show some of the skills that we
[28:34] talked about actually so people will be
[28:36] able to do that.
[28:38] >> Awesome. Let's talk now about Mdash. Now
[28:41] when you sent this to me yesterday uh on
[28:43] April 1st, I was like this has to be an
[28:45] April Fool. like calling it M dash, you
[28:48] know, like with
[28:49] >> AI. Yeah. Like, you know, chatbt was
[28:52] infamous for having like thousands of M
[28:54] dashes every time it wrote a sentence.
[28:57] Um, but no, Cloudflare has built an
[28:59] open-source content management system.
[29:01] They're calling it the spiritual
[29:03] successor to WordPress, and it certainly
[29:06] looks a lot like WordPress. I saw a
[29:09] screenshot on
[29:10] >> I have it here,
[29:10] >> Yoast on Yoast. Uh, I think that's how
[29:15] you pronounce his actual name in Dutch.
[29:16] Yoast.
[29:17] >> Um, who runs, but it's spelled J O S T.
[29:22] He runs Yoast, Y O A S T SO, like the
[29:26] SEO plugin for WordPress. Um, and it
[29:29] looked exactly like WordPress. I thought
[29:31] it was WordPress, but oh, that's his old
[29:33] WordPress.
[29:34] >> Yeah, look at my screen. This is it.
[29:35] >> This is M Dash. If you're on the YouTube
[29:37] version, look at your phone. Look at
[29:39] your screen right now. It's I mean, it
[29:41] looks like WordPress. Yeah, they're
[29:43] clearly going for that market and want
[29:45] to make sure that people feel
[29:47] comfortable with it. But it's it's
[29:49] really nothing like WordPress at all.
[29:51] It's completely built from the ground
[29:52] up. It's serverless, which we'll talk
[29:54] about in just a minute. And everything
[29:56] you can do in there is designed so that
[29:58] AI can execute that thing for you. So,
[30:02] it's really built for agents to make
[30:04] websites. So, what's your first
[30:06] impression of this and are you planning
[30:08] to switch to it? First of all, the
[30:10] WordPress interface is like 20 plus
[30:12] years old and they just did the exact
[30:15] same thing. And you know, if you look at
[30:17] competitors to WordPress, there are much
[30:18] better CMS interfaces. What's really
[30:21] nice is much faster, right? You can see
[30:22] it's on a new thing. It's like it
[30:24] doesn't load on, you know, you don't
[30:26] have this little spinning wheel for like
[30:27] 5 seconds when you click on things like
[30:29] you do on WordPress. Uh it's still very
[30:31] basic to me. Uh you know, even the text
[30:34] editor, like this is far away from
[30:36] Gutenberg. like Gutenberg is a better
[30:38] text editor. Uh, arguably this is the
[30:40] kind of like old WordPress, but it's
[30:42] familiar at the same time. It's like we
[30:45] talk to a lot of people and they're
[30:46] like, "Ah, we're used to WordPress. Our
[30:47] clients are used to WordPress. They want
[30:49] to use WordPress." And it's like they
[30:50] don't want to change. And so for these
[30:52] people, like yes, that's kind of like a
[30:53] killer feature. It does feel like very
[30:55] rough around the edges. And this is a
[30:57] version 0.1, but there's a lot of very
[31:00] good ideas also under the hood. So yeah,
[31:04] would I build a new site on it? No
[31:07] reason why is because a lot of these
[31:08] projects are abandoned eventually and so
[31:10] there's a risk that this will be
[31:11] abandoned as well. At the same time,
[31:14] Cloudflare bought Astro that it's built
[31:17] on. So they own their underlying
[31:19] platform and their main competitor
[31:21] Versel runs Nex.js which is you know
[31:24] their own kind of like website
[31:26] framework/app framework. And so it's
[31:30] pretty evident that Cloudflare wants to
[31:32] make Astro that direct competitor. So
[31:35] investing in the ecosystem makes sense.
[31:38] So provided there is ongoing effort
[31:41] going into this, this is going to be a
[31:43] banger, but there's still a large chance
[31:46] this could also fail because of a low
[31:48] adoption rate. So I
[31:50] >> have quite a good feeling about this to
[31:51] be honest. I think they really captured
[31:53] the
[31:54] >> what's been missing with all this kind
[31:56] of like AI web design stuff is that yes
[31:59] okay the web designer the agency making
[32:01] the website it's useful for them but the
[32:04] end user it was like gave them no
[32:06] interface and no control and it was
[32:08] scary
[32:09] >> yeah but imagine makes it not scary
[32:11] >> no imagine like the homepage like
[32:13] there's no way this would fit like our
[32:15] homepage how do you fit this into this
[32:17] format here like you don't you cannot it
[32:20] will not work this will work for like
[32:22] simple blog posts with like headlines
[32:24] and images and stuff. It's nice. They
[32:25] have like a
[32:26] >> which for 90% of people is is enough.
[32:30] But like the flip side of that is like
[32:31] not having an interface where you know a
[32:34] junior employee can go in and edit some
[32:36] text easily without you know connecting
[32:38] a bunch of [ __ ] is like it's a problem.
[32:41] >> But the for example the junior employee
[32:42] would not be able to edit the homepage
[32:44] for example because of the structure. So
[32:46] it's like you still need to kind of go
[32:47] through like
[32:48] >> and they may not be editing that stuff
[32:50] very often like
[32:52] >> fine. I'm just saying there is
[32:54] limitations. So it's like it will work
[32:55] for a blog, it will work for like a
[32:57] simple content system but then you kind
[33:00] of still need to vibe code like you can
[33:02] make sections that I've seen as well. So
[33:03] you can like you know they have this
[33:05] about the auto thing and then you can
[33:06] edit it but like it's still extremely
[33:08] extremely basic. So I think the editor
[33:10] part needs to be developed but again
[33:12] with AI I don't think it would be very
[33:14] difficult to build something like
[33:17] Gutenberg for example like I think they
[33:18] can do it quite quickly if they want to.
[33:20] >> I think the thing with Gutenberg as well
[33:21] is it's also like a learning curve to it
[33:24] and there's there's a it creates a lot
[33:26] of um
[33:28] >> friction. There's no simple way to edit
[33:30] a website with a complicated layout
[33:32] though. That's the problem.
[33:33] >> Exactly. Unless you have an actual page
[33:35] builder like element or something where
[33:37] you would click and edit that it doesn't
[33:39] exist. Here here's the thing though.
[33:41] Most solution all solutions up until
[33:43] this point they're like well we can't do
[33:45] it exclusively for like the normies
[33:48] otherwise will have like wix or
[33:50] something like you know you can't do
[33:51] anything in or the other end it's like
[33:54] you know full vibe coded you do
[33:56] everything from cloud code and then like
[33:58] all the normies the idiots like me can't
[34:01] figure out how to do [ __ ]
[34:03] >> by yourself you're doing it now
[34:04] >> so so well I mean we're all idiots
[34:07] according to you uh earlier in this this
[34:09] vlog that's Oh, just because you can't
[34:11] use the pro model. Come on.
[34:13] >> I I I'm I'm joking. I'm joking. Um so so
[34:17] like the compromise is bad for everyone
[34:19] in a way. Like the Gutenberg compromise
[34:21] is bad for everyone cuz like it's bad
[34:23] for the experienced people. It's bad for
[34:24] the basic people, but at least everyone
[34:26] can kind of do everything. What they're
[34:28] doing here is they're saying, well,
[34:30] forget about that middle ground. Let's
[34:32] make something that's perfect for the
[34:35] newbies, for the the idiots, and it's
[34:37] also perfect for the smart uh site
[34:40] builders, web designers, and they work
[34:42] in conjunction together. So, it's almost
[34:44] like there's two solutions, two ways to
[34:46] do everything in one. There's like the
[34:49] human aspect, the AI aspect, and
[34:51] honestly, I think they're on for an
[34:52] absolute banger with this. And I can see
[34:54] why they've done it as well because it's
[34:56] all built on this like serverless
[34:58] architecture where I mean you need to
[35:00] correct me if I'm wrong here but as I
[35:02] understand they only
[35:04] >> serve you the site when you request it.
[35:07] So it's not like there's a computer
[35:08] always running
[35:09] >> which is why no one's coming to it which
[35:12] is why they'll give you the hosting for
[35:13] free basically. By the way they have an
[35:15] importer for your website so you can
[35:17] just put your WordPress site URL and
[35:18] import your content. By the way I don't
[35:20] know how well it works. Um, but it yeah,
[35:25] it is an easy
[35:26] >> that it says at the top there, import
[35:28] post pages and custom post types from
[35:31] WordPress. I'm not sure if that's like
[35:32] the full site design and you know, all
[35:35] the databases and other stuff as well.
[35:37] But, you know, if it's just import all
[35:39] your WordPress content, that alone is
[35:41] like it's a it's a
[35:42] >> it's a very nice thing to have.
[35:44] >> Yeah.
[35:44] >> And like cost nothing to play around
[35:46] with this either.
[35:47] >> The one thing I want to push back on you
[35:49] is like, oh, it's for normies, etc.
[35:50] Well, to install it, you need to clone a
[35:52] GitHub repository right now. So, I don't
[35:54] know.
[35:54] >> I understand that, but you know, when I
[35:57] first installed WordPress, I had to fire
[35:59] up an FTP server to upload it and like
[36:01] you don't have to do that anymore.
[36:02] >> There will be a result eventually like
[36:04] there will be some kind of without I
[36:06] agree. But for now, it's like it's not
[36:08] really version 0.1 and the vision is
[36:10] great. Now, let's see if it actually
[36:12] realizes itself. Now, for the serverless
[36:13] stuff, yeah, that's kind of the thing.
[36:15] It's like WordPress sites are built on
[36:17] ancient internet uh principles and
[36:20] that's the problem. It's like that's why
[36:22] you pay so much for a WordPress hosting
[36:24] because you have to keep up a server
[36:26] that is strong enough to handle the
[36:30] maximum amount of traffic that you
[36:32] potentially will get on your website and
[36:34] that's why you have to pay and it's
[36:35] always on whether someone is on it or
[36:37] not. Whereas the system of workers on
[36:39] Cloudflare it starts only when people
[36:41] open the page. So it does your website
[36:43] is shut down if nobody's on your website
[36:46] and when people request the URL the
[36:48] server starts extremely fast during the
[36:50] load time basically and will be able to
[36:53] serve the page and they have a whole
[36:54] caching system etc that you know that
[36:56] they can essentially speed it up. Uh and
[36:58] the idea is like you know the power of
[37:01] your server will scale up and down based
[37:03] on how much traffic is on your website
[37:05] right now which in total uses just a lot
[37:08] less resources than a WordPress site
[37:10] would and as a result like you know as I
[37:12] say like now if you run you cannot run
[37:14] in static like but you could probably
[37:17] get like 60 70,000 visits per month on a
[37:19] site like this and not pay anything for
[37:21] the hosting and still be faster than a
[37:23] premium WordPress hosting uh which I
[37:25] know a lot of people care about page
[37:26] speed well that will be better basically
[37:28] Yeah, WordPress is always going to have
[37:29] this problem. It's 23 years old now.
[37:31] It's older than some people listening to
[37:33] this podcast right now. Um, and if you
[37:35] can imagine how people listen to us
[37:38] >> computer or your phone was like 23 years
[37:41] ago. Um, and I know it's obviously
[37:43] WordPress been updated from then, but
[37:45] there's some kind of architectural
[37:48] things that hold it back and this is a
[37:50] kind of like, hey, let's have a fresh
[37:51] start and we've reimagined it. So, I'm
[37:54] I'm very excited for this.
[37:55] >> They have also some interesting things.
[37:56] So for example, the problem with
[37:57] WordPress is security. Why? Because when
[37:59] you install a plug-in, like the plug-in
[38:01] has access to everything on your website
[38:03] and can hack your database and can [ __ ]
[38:05] it up, etc. Whereas the way they run the
[38:06] plugins here is almost like their own
[38:08] server, like their own walker and only
[38:11] kind of has an interface with the
[38:12] website that's kind of indirect and in
[38:15] that way cannot like poison your
[38:17] website, which increases security
[38:19] massively. Uh, and the other thing that
[38:21] they have that's built in that's
[38:23] actually pretty cool is there's a new
[38:25] kind of like uh process I can't remember
[38:28] XX42
[38:30] which is protocol for chatbots to pay
[38:34] for using the content on your site. It's
[38:36] kind of like automatic. So again, I
[38:38] don't think OpenAI is paying for any
[38:40] content right now, but if the internet
[38:41] was ready to start actually, you know,
[38:44] paying content creators for using their
[38:45] content in these kind of things and that
[38:47] became a standard, then this is already
[38:49] built in. And as a content creator,
[38:51] you'll be able to start automatically
[38:54] collecting revenue for your content
[38:56] being used by uh LLM companies, which
[38:58] is, you know, it's kind of future proof
[39:00] basically.
[39:01] >> And of course, if you're Cloudflare,
[39:03] then all this is built on their
[39:04] infrastructure. So if it takes off then
[39:07] a lot more people instead of using
[39:09] WordPress hosting which I know like a
[39:10] lot of it is actually goes back to word
[39:12] pler anyway but
[39:13] >> not really because they don't have like
[39:15] permanent servers so it's going to be
[39:16] more on AWS etc like t only stateless
[39:19] servers pretty much
[39:20] >> so they're going after a market that
[39:22] pays like website market that a lot of
[39:24] them pay for these servers that they
[39:25] don't run
[39:26] >> and then they they want to eat that. So
[39:28] like if you're WP Engine for example
[39:30] >> I honestly think it's a I honestly think
[39:31] it's a slam dunk. I think they have
[39:33] everything they need to to take over.
[39:35] Like it of course is a critical mass
[39:37] factor. It needs adoption. It needs you
[39:40] know people to support it. But um Yoast
[39:43] the Yoast SEO creator um is already
[39:46] moving his site towards this. So you
[39:48] know that's like that's one has built-in
[39:51] SEO as well and all that stuff. You
[39:52] don't need plugins for that. They did
[39:54] like also you can manage your redirects
[39:55] from it. You can and it's all just
[39:57] Cloudflare behind the scenes. So it's
[39:58] extremely efficient and fast. Yeah. It's
[40:00] it could be excellent. it needs
[40:02] refinement. The good news is if you're
[40:04] building a website using Astro like we
[40:06] teach on a accelerator, you can probably
[40:08] migrate to this very very easily like
[40:09] cloud code can probably do it for you or
[40:11] codeex and uh and that will give you a
[40:15] bit of a familiar feel on how you manage
[40:17] your content while at the same time the
[40:19] codebase is fully editable by your
[40:21] chatbot and you'll be able to vive code
[40:23] away unlike you can do it on WordPress
[40:26] like WordPress doesn't really allow you
[40:27] to do that. You know, it's worth
[40:29] pointing out as well, Astro. It's the
[40:30] same framework which we teach in the AI
[40:33] accelerator. So, and it's what we've
[40:35] used to build the new version of
[40:36] authorityhacker.com which is live now.
[40:39] So, you can go check that out. And
[40:40] specifically, you can go to
[40:41] authorityhacker.com
[40:44] accelerator. If you want to learn more
[40:47] about our courses and community inside
[40:49] the accelerator, um, including the new
[40:52] course we released last week on vibe
[40:54] coding a site exactly like this. I think
[40:58] it's uh,
[40:59] >> yeah, it's super impressive what you can
[41:01] do with zero design skills basically
[41:04] now. Like you don't need a designer, you
[41:05] don't need a developer to build a really
[41:07] nice looking site. Um, and that's a
[41:09] pretty big change compared to even six
[41:11] months ago. So yeah, check that out.
[41:13] authorityhacker.comac
[41:15] accelerator. Let's talk now though about
[41:19] ads because a couple months ago, the
[41:22] start of February, OpenAI rolled out ads
[41:26] and there there was some controversy.
[41:28] Claude paid for a bunch of Super Bowl
[41:30] ads to that were kind of poking fun at
[41:32] it, saying, you know, was going to
[41:34] implying indirectly that they were going
[41:36] to mess up the replies. They knew they
[41:40] weren't. They knew they were having
[41:41] separate disclosed ad sections, but it
[41:44] caused some friction. It caused some
[41:45] controversy there. Um, we're now two
[41:47] months into it
[41:49] >> and OpenAI is saying that it has $100
[41:53] million
[41:55] in annual recurring revenue from 600
[41:58] advertisers. I don't know exactly how
[42:00] that works. I think that's what it
[42:02] means. if they've taken the two months
[42:04] and like annualized that or something.
[42:08] >> Recurring just [laughter]
[42:10] >> Yeah, it's surely not going to be an
[42:11] annual recurring contract like locked in
[42:15] for multiple years cuz like this is all
[42:17] >> I think it's PR. Yeah,
[42:19] >> they've thrown out this hund00 million
[42:21] number to say like yeah, there's a lot
[42:23] of money going into this. Um, what's
[42:26] really important though for small
[42:28] business owners to know is that this
[42:30] month they are launching selfs serve
[42:32] which means that anybody any business
[42:34] owner can go and run ads inside chat
[42:38] GBT. Now it's I believe just in the US,
[42:41] Canada, Australia and New Zealand. I
[42:43] don't think Europe is getting ads yet.
[42:46] Um I I could be wrong on that. They also
[42:50] released some numbers as well which I
[42:51] think were quite interesting. So, we've
[42:53] heard this $60 CPM. So, the cost per
[42:56] thousand impressions being $60, which is
[42:59] three times higher than something like
[43:01] display ads. Um, but they've now
[43:04] released the clickth through rate uh
[43:08] data. So,
[43:08] >> interesting.
[43:09] >> 0.91%
[43:11] CTR, which means that just under one in
[43:14] 100 people are clicking on an ad. If you
[43:17] compare that to a Google ad, like at
[43:20] the, you know, the top of a search
[43:22] query, they get about 6.4%. So quite a
[43:25] bit more. But if you compare it to a
[43:27] display ad that you'd see on a website,
[43:30] that is much lower, about 0.35%.
[43:33] So it's about just under triple the CTR
[43:36] of a display ad,
[43:38] >> which is it's not nothing. So, you know,
[43:41] if you're treating this like a display
[43:43] ad, but you know, it has
[43:47] >> it has more of the properties of a
[43:50] Google ad, I think, because they're
[43:51] matching the intent much better because
[43:54] you're actually typing stuff and they
[43:55] have context about what you're looking
[43:57] for. And I think that's really the angle
[43:59] they're trying to play up here.
[44:01] >> Um, so it's going to be really
[44:02] interesting to see. And as always in
[44:05] when there's any new kind of ad
[44:07] inventory gets released
[44:08] >> first users are going to get a bunch of
[44:10] cheap inventory. Um so you know it pays
[44:13] to be an early adopters sometimes in
[44:15] this.
[44:16] >> I think that's the biggest opportunity
[44:17] of the year for marketers actually to
[44:19] figure this out. It's like there will be
[44:21] lots of demand for it. It will be much
[44:24] more predictable than trying to rank
[44:25] organically etc. And that's going to
[44:27] work. Now the 0.35 on display ads from
[44:30] Google like you need to put that in
[44:31] brackets because the advertiser like the
[44:34] website decides where the ad displays
[44:36] and quite often the ads are poorly
[44:37] displayed. Sometimes they're not even in
[44:39] the viewport like they load a little bit
[44:41] before you scroll to them, right? So
[44:42] that they don't load as they appear.
[44:44] >> Well, it depends which site. If you go
[44:46] on any like tabloid newspaper these
[44:48] days, you get about 6,000 ads before you
[44:50] see any content.
[44:51] >> I understand. But this is all the ads
[44:53] and so therefore there's a lot of
[44:54] inventory that's poorly placed, etc. I
[44:56] think it's like it's okay, but like 0.91
[44:59] CTR unless they really charge a lot per
[45:01] impression. Like I don't even think it
[45:03] pays for the costs basically. I don't
[45:06] think it's very good. And that would
[45:07] explain why OpenAI is still pivoting
[45:10] towards enterprise even though they have
[45:11] this kind of like ad play running for
[45:13] B2C. Basically, I still think it will
[45:15] help dampen like it will reduce the cost
[45:17] to them and they hope they can improve
[45:19] it probably. They will change the layout
[45:20] slowly to like increase CTRs and
[45:22] whatever.
[45:24] I actually want to show the layout for a
[45:25] second because I don't think we've shown
[45:27] that here. So here's we can't get it
[45:29] here in the UK. But um here's an article
[45:32] on Wired where they shared it and it's I
[45:35] mean it's pretty separated, right? You
[45:37] got the end of your prompt here and then
[45:39] you know the the icons that almost acts
[45:42] as a little barrier and then there's
[45:44] this Uber ad in there and it's like you
[45:46] know it's not super in your face but you
[45:48] know you certainly notice it. It's got
[45:50] like an image and stuff in there, so
[45:52] it's a bit more visual than like uh you
[45:54] know Google search result ad.
[45:56] >> I think they can improve the CTR
[45:58] massively by like moving the buttons
[46:00] below the ad by moving the Uber
[46:02] sponsored label below the ad as well. Uh
[46:05] it's fine. They can still show it but
[46:06] it's below. It's almost feels like part
[46:07] of the answer, but it's kind of like
[46:09] sponsored. Like the point is like they
[46:10] can probably double the CTR. So they
[46:12] have lots of levers to do that.
[46:15] >> Here's another one for target. Uh same
[46:18] thing. There's like a there's a really
[46:20] small image of what is that like a
[46:22] toothpick or no brooch? I don't even
[46:25] know what
[46:25] >> crochet hooks.
[46:28] >> It's for like knitting, you know.
[46:32] >> Ah, okay. Right. Yeah. Not not something
[46:34] I'm super familiar with, but uh
[46:36] >> looks like a toothbrush or something.
[46:38] But anyway, that's kind of part of the
[46:40] problem, right? You know, I'm looking at
[46:41] this on a monitor and like I can barely
[46:43] see what that is.
[46:44] >> They need to make it bigger.
[46:46] >> My phone that would be tiny. They need
[46:47] to make those things bigger. So
[46:49] >> they have room. This is the clean
[46:51] version. Like they will probably cover
[46:53] the API cost through this.
[46:55] >> Yeah. They always start with like, you
[46:56] know, ads which are not too in your face
[46:58] and then they're like, "Oh, we can make
[47:00] more money if we just make it more in
[47:01] your face and then they dial that up."
[47:04] >> Yeah. Basically. So
[47:05] >> So that that's coming and I I think it's
[47:08] an opportunity. I think if you're a
[47:09] marketer looking for like a new
[47:10] direction or whatever or a new service
[47:12] like as soon as there's the subs of
[47:14] stuff if you like show these screenshots
[47:15] to people be like hey you you know AI is
[47:17] the next big thing you want your
[47:18] business to show up there etc. I'll I'll
[47:20] say that for you. I'm specializing in
[47:22] that. It's going to be a killer.
[47:24] >> And look, um, we talk a lot about AI SEO
[47:28] or GEO and how, you know, we're sort of
[47:32] dubious sometimes about like the actual
[47:34] impact of that. But whatever our
[47:37] opinion, like every business is asking
[47:39] for it at the moment. So, every SEO
[47:41] agency, marketing agency is is trying to
[47:44] serve it to them. I think we're in for
[47:46] that same wave here on the ad side this
[47:50] year. And I I've really I haven't I
[47:51] haven't seen any ad agencies talking
[47:53] about this. Like it's it really feels
[47:55] like uh
[47:56] >> this is a wave which not too many people
[47:58] are getting.
[48:00] >> It's much more predictable like you know
[48:01] you pay per per thousand impressions
[48:03] anyway. Like you will not be charged if
[48:05] your ad doesn't show. So it's like it's
[48:07] much easier to get results to people
[48:09] provided you can afford the price. Yeah,
[48:11] I think it's going to be a banger. I
[48:12] think there will be also a new way of
[48:13] advertising like making it feel native
[48:15] etc. You're going to have to think a
[48:16] little bit like how these chat bots work
[48:18] and what the experience is for the user
[48:20] and so there will be all these kind of
[48:21] competitive edges you can build.
[48:23] >> I'm always a bit dubious about companies
[48:25] that advertise c you know certain types
[48:28] of products. So okay you know if it's
[48:29] like Uber or Target or something like
[48:31] that you know it's not too bad. So, I
[48:33] was looking at the list of companies or
[48:36] rather product types that were being
[48:37] advertised that the wired editor had had
[48:40] found and it's, you know, simple stuff
[48:42] like dog food, travel, printers, hotels,
[48:45] productivity software, credit cards,
[48:47] streaming services. I'm like, okay,
[48:49] fine, that's kind of what I expected.
[48:50] But there were a couple in there that I
[48:52] thought, ah, that's kind of interesting.
[48:54] And one of them was skin care articles.
[48:57] Now, that in that really got my uh
[49:02] Spidey create a post.
[49:05] >> Well, I don't know. Like, we couldn't
[49:06] see you didn't share the exact one, but
[49:08] a skincare article.
[49:10] >> Why would a company share content about
[49:13] it? Like, is it because
[49:14] >> it's a pre-sales landing page.
[49:16] >> It's like it looks like an article and
[49:18] it's like, hey, three ways to make your
[49:20] skin look a doctor on it.
[49:23] >> You sign up for some subscription to a
[49:25] diet pill or something and it's hard to
[49:27] get out of and Yeah. So I'm like surely
[49:31] they're going to prevent that stuff. You
[49:32] know for for many years Facebook and
[49:34] Meta was like really really against any
[49:37] kind of like dodgy advertising and then
[49:39] slowly they realized that those paying
[49:42] paying more money and you know they
[49:44] could make more money off the back of
[49:45] it. So they it kind of loosened their
[49:47] restrictions a little bit. So it'd be
[49:49] interesting to see where I have a
[49:51] different roll this up.
[49:53] >> My take is they're gonna like so open
[49:56] air is building this super app right now
[49:57] right? They say they're building some
[49:59] kind of new app. In my opinion, Chad
[50:00] Gypty is going to stay kind of like the
[50:01] B2C app and this is not moving. It's too
[50:04] difficult to move users to that and
[50:06] they're going to build like a new app
[50:07] for professionals that will kind of be
[50:09] bringing the some features of CH GPD
[50:11] with codeex with the browser and more
[50:13] advanced users of their subscriptions
[50:15] and probably they will split the
[50:16] subscriptions too. Um and my guess is
[50:19] that charge
[50:20] >> this is all speculation by the way
[50:22] >> is charge is going to go full trash tier
[50:25] max monetization because anyway there's
[50:27] no like these companies have understood
[50:29] that the B2C market is not very
[50:31] lucrative in AI anyway. So that's a way
[50:33] for them to separate and make like a
[50:34] high quality professional service on one
[50:36] side and then full like let's monetize
[50:39] however we want on the success of chat
[50:41] GBT which is still massive and they will
[50:44] have these trashy ads and they will have
[50:45] all of that and a professional app will
[50:47] have no ads and it will be subscription
[50:48] only basically and they're going to
[50:50] split these two experiences uh because
[50:52] even Gemini for example like for sure
[50:54] the experience has gone down quite a bit
[50:56] like the big B2C chat apps they try to
[50:59] make money they haven't figured it out
[51:00] they need to lower their cost and
[51:02] increase their revenue and that's
[51:03] probably going to be like lower quality
[51:05] models combined with a lot of ads and we
[51:08] don't give a [ __ ] how we make money and
[51:10] then the professional market which is
[51:11] like premium experience sa models no ads
[51:14] you pay a bunch of money per month
[51:15] basically and they need to split these
[51:17] two
[51:17] >> I can see this happening because you
[51:19] know 80% of B2C users they might not
[51:22] even have heard of claude or or Gemini
[51:24] so like a chat DVD is AI to them and
[51:27] they're kind of locked in whether one
[51:29] model's slightly better than the other
[51:31] or the business users like they're much
[51:34] more sensitive about those things about
[51:35] those features. So it it makes sense to
[51:37] split them. Although splitting isn't
[51:39] really making a super app. It's like
[51:41] it's kind of like for me a super app is
[51:43] like everything is in one.
[51:45] >> Yeah. Yeah. But there would be like a
[51:46] professional app and a B2C app. And the
[51:48] reason I say that as well is it's been
[51:50] leaks on social media on like error
[51:51] messages and one of them was for example
[51:54] like you cannot use CHP you are on a
[51:56] codeex plan. And so that says that this
[51:59] is splitting up and so like I can
[52:01] imagine like trag
[52:04] that will be filled with ads if you
[52:06] don't pay and they will have like the $9
[52:08] plan as well something like that. It
[52:10] will be the three tiers and you'll have
[52:11] codecs that will start at $20 and go all
[52:13] the way to 200 and slowly increase
[52:15] together with entropic and the consumer
[52:17] app. I'm telling you they will advertise
[52:19] a lot of [ __ ] to grow their revenue for
[52:22] the IPO. That's my guess. All right, I
[52:25] want to finish up by talking about
[52:27] something Gemini's done uh recently and
[52:30] they are making it super easy for you to
[52:33] port all of your chat GBT or clawed data
[52:37] into Gemini. So basically reducing the
[52:39] friction from switching friction being
[52:41] things like your chat history, your
[52:43] memories, anything which you you know
[52:46] you associate with okay yeah this is my
[52:49] workspace that I've used before. So do
[52:51] you want to tell us a bit about how this
[52:52] works? I mean it's just a prompt. It's
[52:55] like they copied what clo did it when
[52:57] there was the department of war drama
[52:59] with open air and code and you know all
[53:00] of that and cloud made that thing. It's
[53:02] like they gave you a prompt that you
[53:04] would paste in charge GPT charge would
[53:06] spit out an answer like with most of
[53:08] your memories and you would just paste
[53:10] that back into code and it would just
[53:12] update its memory based on that and it
[53:14] would feel like there's some kind of
[53:15] continuity between your trag experience
[53:18] and your code experience. Well, Gemini
[53:20] decided to vibe code a copy of that.
[53:22] [laughter]
[53:22] Basically, they took a screenshot
[53:24] probably and they were like, "Build me
[53:25] this and it's just a prompt and then you
[53:27] just send it." Now, they also allow you
[53:29] to import chat history and you need to
[53:30] also think that Gemini has this uh
[53:33] personal intelligence in the US only
[53:35] where it uses like your Gmail, it uses
[53:38] your Google photos, etc. And so, the
[53:40] idea is like if you also import your
[53:42] chat history, it will just make it feel
[53:43] a lot more personal. So like Gemini in
[53:46] Europe, like how we have it, there's
[53:47] literally almost no personalization
[53:49] option. You can just kind of like save
[53:51] things manually if you want. But in the
[53:53] US, yeah, that's going to feel a lot
[53:54] more personal and better. And again,
[53:56] Gemini is also the default voice
[53:58] assistant on Android, which funnily
[54:00] enough is not very used in the US, but
[54:02] very used outside of the US. And so
[54:04] yeah, it kind of makes sense for a lot
[54:05] for B2C. I think it makes sense to
[54:07] switch. I don't think Charg if you don't
[54:08] pay for it, is better than Gemini. If
[54:11] you pay, you know, it's debatable. I
[54:14] would say Gemini has gone down a lot as
[54:15] a chatbot. So, yeah.
[54:17] >> Yeah. I I basically stopped using Gemini
[54:19] for like the last two three months.
[54:21] >> Gemini 3.1 Pro was not a good model.
[54:23] Like it's just it's just a little bit
[54:24] more rigid and it's like it just feels
[54:26] like a last gen model compared to like
[54:27] Opus or even Gypty 5.4 which are really
[54:30] good. Um
[54:30] >> their image model is obviously still
[54:32] good, but it just seems to have like
[54:34] fallen back a little bit to be honest.
[54:36] Gemini free flash is very good in when
[54:37] you stop paying API prices when you use
[54:39] the API. The value of Gemini free flash
[54:42] is excellent because it's like a little
[54:43] bit below sonet. Um but it's three times
[54:46] cheaper. So it's quite handy if you want
[54:48] to like do summaries or if you want to
[54:50] process lots of data and not spend a ton
[54:52] of money. Like actually one of our
[54:53] members today was like oh I'm paying
[54:55] like 50 bucks per day on set for all my
[54:57] stuff. I'm like switch to Gemini 3 flash
[54:59] and you'll probably pay like seven
[55:00] bucks. So like yeah the flash models are
[55:03] great value from Google but the frontier
[55:04] is always kind of a bit worse and and
[55:08] it's like it's just not there right now
[55:09] for coding it's like don't bother Gemini
[55:11] CLA sucks. So yeah.
[55:13] >> Okay awesome. Uh any final words of
[55:15] wisdom before we wrap up?
[55:16] >> No just uh probably good luck to
[55:18] everyone who has to upgrade their plan
[55:20] as we predicted because all the limits
[55:22] of all the things are down. You still
[55:24] are like we can complain all we want.
[55:26] They're still losing a lot of money on
[55:27] us. So it's like the reality is we
[55:30] should feel good about it and you will
[55:31] regret today's limits probably by this
[55:34] time next year. So let's just enjoy it
[55:36] while it lasts. The good news is the
[55:37] Frontier is going to get better anyway.
[55:39] So it's like you'll get more for your
[55:40] money. But yeah. Yeah. Get started.
[55:42] >> And it's a it's another good reason to
[55:44] subscribe to this podcast because as
[55:46] this develops over the next year or so,
[55:48] we're going to continue to produce a lot
[55:50] of content around how to use AI in a
[55:53] more efficient, more token efficient
[55:55] way. So, if you're a small business
[55:56] owner, then yeah, definitely subscribe
[55:59] so you don't miss out on that content.
[56:00] Thanks for watching this episode. We do
[56:02] release a new one every single week, so
[56:05] hope to catch you next week. Drop us a
[56:06] comment if you have any questions or
[56:08] thoughts. We read and answer all of
[56:10] those on YouTube. So yeah, see you next
