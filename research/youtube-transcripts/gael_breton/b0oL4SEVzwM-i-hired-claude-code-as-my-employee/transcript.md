# I Hired Claude Code as My Employee

- YouTube: https://www.youtube.com/watch?v=b0oL4SEVzwM
- Video ID: b0oL4SEVzwM
- Upload date: 2026-03-25T05:08:18-07:00
- Transcript source: supadata
- Status: ok
- Language: en
- Fetched at: 2026-07-03T17:13:55+00:00
- Supadata billable requests: 1

## Transcript

[00:00] You're at lunch. You pull out your phone
[00:02] and tell Claude to build a landing page
[00:04] for a new product launch. And by the
[00:05] time you're back at your desk, it's
[00:07] done. This is possible because last
[00:08] week, Anthropic shipped co-work
[00:10] dispatch. But this now works with Claude
[00:13] Code, too. So, you can fully control
[00:15] Claude Code from your phone. We took
[00:17] this a step further and built a system
[00:19] where we can assign work to Claude Code
[00:21] directly from Notion. That changes
[00:23] Notion from being our task manager to
[00:26] our task executor. It literally does all
[00:28] the work itself. Now, we'll also show
[00:30] you Claude's new computer use feature
[00:33] where it takes over your keyboard and
[00:34] mouse and a skill we built that oneshots
[00:37] entire websites. I'm joined by Gail
[00:40] Breton, my co-founder, Authority Hacker,
[00:42] where we separate what works for
[00:43] business owners and knowledge workers
[00:45] from what's just noise in the AI space.
[00:48] How's it going, Gail?
[00:49] >> Like the new catchphrase at the
[00:51] beginning. It's like, [laughter]
[00:53] did AI write this?
[00:54] >> It did, but I kind of directed it. I do
[00:58] in this space.
[00:59] >> It sounds like a local news station's uh
[01:02] catchphrase a little bit, which is like
[01:04] it's both good and bad, you know? But
[01:07] >> there's maybe a reason why all news
[01:09] stations have things like this. And one
[01:11] of the problems we had with our podcast
[01:13] is like new people come and they're
[01:15] like, who is this for? Who are you guys?
[01:17] What is this? It's fine if you've been
[01:19] listening for 10 years, but not everyone
[01:21] has. So for the benefit of those people,
[01:23] we hope you're in the right place now.
[01:25] And we got a bunch of new listeners last
[01:27] week actually. So, welcome to everyone.
[01:29] >> Yeah, thanks for tuning in this week as
[01:32] well if you just found us last week.
[01:33] Today we're going to talk about
[01:35] controlling Claude remotely in various
[01:38] ways, some very basic and some a bit
[01:41] more advanced.
[01:42] >> So, Gail, let's start off if we can with
[01:44] co-work. It was originally called
[01:46] co-work dispatch, but my understanding
[01:47] is that it now works with claude code.
[01:50] So, it's just yeah, just dispatch.
[01:52] >> Um, yeah, I've told a lot of people
[01:54] about this. this I was at an event last
[01:55] week and the first question everyone
[01:58] said was oh can it control my VS code or
[02:01] how is it working and it can't but it
[02:04] kind of can do the same thing anyway so
[02:06] you want to kind of fill us in on
[02:08] exactly what's going on here I mean
[02:09] there's two things right there's the
[02:11] dispatch that connects cloud code but it
[02:13] connects to cloud code on your desktop
[02:14] app and it's kind of a weird one right
[02:16] because when you use dispatch you
[02:18] basically have this one feed with
[02:21] everything and it just never clears it
[02:23] it's just one feed and then that acts as
[02:25] an orchestrator that then starts either
[02:27] co-work sessions or code code sessions
[02:30] on your desktop app which with whatever
[02:31] setting you have on your desktop app. So
[02:33] if you haven't connected your MCPS on
[02:35] your desktop app or whatever it's not
[02:37] going to work but if you have it will
[02:39] work actually and it kind of decides
[02:40] what to do like it's you don't really
[02:42] have too much control.
[02:44] >> You can replicate VS Code essentially by
[02:48] setting the folder it's working on to be
[02:50] the same folder that your VS Code works
[02:52] on
[02:52] >> enough but not really. So let's imagine
[02:54] for example we have this meta ad scale
[02:56] that we showed a few episodes ago that
[02:58] creates images right to run that skill
[03:00] you need a Gemini API key because it
[03:01] uses an open banana right it's like it's
[03:04] not a skill it's like it's just an API
[03:06] key that it calls when it calls the API
[03:08] and as a result it's like you cannot
[03:09] store secrets in the cloud app for
[03:11] example right now so you could not run
[03:13] that skill for example it wouldn't work
[03:15] so it's like there are still limitations
[03:17] and it's still not perfect like it's
[03:20] evolving like you know by this time next
[03:22] week it will probably be solved given
[03:23] and how fast these things are being
[03:25] done, etc. And it's kind of like it
[03:27] works very well if you have your code on
[03:29] GitHub, but then there's still like the
[03:30] secret management that's still a little
[03:31] bit janky. Like you can make
[03:32] environments, but it's not very clear.
[03:34] Like entropic is throwing a lot of [ __ ]
[03:36] at the wall right now. A lot of it kind
[03:38] of overlaps and it's like 80% done every
[03:41] time they release it. So it's like it's
[03:42] kind of good, but it's kind of also not
[03:44] that good because it's all vibe coded.
[03:46] And so like my guess is they're just
[03:48] throwing everything they can at the
[03:49] wall. They see what people use and they
[03:51] consolidate. I can imagine that
[03:52] eventually they will focus on the things
[03:54] that people use and and abandon the
[03:56] things that people don't use and
[03:58] depreciate them.
[03:59] >> So right now, how are you using it or
[04:01] how would a business owner be using
[04:04] this? Yeah,
[04:04] >> I'm not using it because I built a
[04:06] better system on notion that we're talk
[04:08] about later.
[04:09] >> Okay.
[04:09] >> Um so I am
[04:11] >> that aside like what would you be using
[04:13] it for?
[04:13] >> I don't think I would use it for cl
[04:15] code. I think the best way to use it
[04:17] right now is to actually focus on
[04:18] co-work connect your MCPs connect it to
[04:22] your folders and then have skill loaded
[04:24] on co-work and then you can run all
[04:26] these stuff. It's pretty good on
[04:28] co-work. It will not do everything you
[04:30] can do on VS Code if you're on VS Code,
[04:31] but it can do, you know, 70% of it. Uh
[04:33] it doesn't have a terminal, but that's
[04:35] how I would set it up. And so I've set
[04:36] it up a little bit with co-work. It
[04:38] works kind of okay, but I really don't
[04:40] like the way it works because it's
[04:42] basically like it works like a chat, but
[04:44] it's not really like a chat. It's an
[04:45] orchestrator. You talk to the
[04:47] orchestrator and then it just spawns a
[04:48] session of co-work, but you see nothing.
[04:50] So, you're on your phone and it's just
[04:52] kind of like idle for 10 minutes while
[04:55] it's running the co-work session and
[04:57] it's like boom, it's done or it failed
[04:59] or it just kind of like hangs because
[05:01] it's like it's failed silently or
[05:03] something. What's good is it does have
[05:04] the approval thing. So if it needs
[05:06] access to a folder or something, it will
[05:07] just pop you like I think you can see it
[05:09] on the Twitter image here. Like it asks
[05:11] you for access and so that's decent. It
[05:14] works, but it still feels like you don't
[05:17] really know. It's kind of this weird
[05:18] hybrid where there's a chat happening in
[05:20] the background where you don't see the
[05:21] chat. So you don't see what it's doing.
[05:23] So you don't know if it's going well or
[05:24] not well. You cannot interrupt like load
[05:25] code. And so that's why it's like bro
[05:28] type thing.
[05:29] >> Well, it's not just that. It's like I
[05:30] want to read this file and you're like
[05:32] why? It's like why are you doing this?
[05:34] And it's like you don't know. Um, and so
[05:36] like that's why actually the notion
[05:37] system I built, I like it better because
[05:38] it's fully asynchronous. So you kind of
[05:40] assume it's just going to go do its
[05:41] task, but you set it as a task, it just
[05:44] comes back to it, but you're not like
[05:45] hanging on the chat. It's just doing it
[05:46] basically.
[05:47] >> Ju just before we jump on the notion
[05:48] thing because I can see you're eager to
[05:50] get there.
[05:51] >> Not that it's just like I don't use this
[05:53] dispatch. Basically,
[05:54] >> one of the things that I hate a lot
[05:57] about the AI industry is the weak use
[05:59] cases. you know, they'll they'll release
[06:01] this new feature and like,
[06:02] >> yeah, you can,
[06:04] >> you know, use your voice to send an
[06:06] email or like, you know, look up the
[06:08] weather or you open your calculator or
[06:10] something like and it's like that's
[06:12] stupid. That's a stupid use case. Are
[06:14] there any realistic practical use cases
[06:17] that business owners or knowledge
[06:19] workers would use dispatch for today?
[06:21] >> Yeah. If you have any MCPS that has
[06:24] valuable data, let's say you again lots
[06:26] of SEOs listening to us, right? like
[06:28] you're on a meeting with a client and
[06:30] you need to pull the latest data from
[06:32] their site and you have a small phone
[06:34] like I have. It's kind of complicated.
[06:36] You could open HS but honestly like
[06:38] navigating HS with all the filters
[06:40] sounds like a nightmare. If you have the
[06:42] HS MCP connected to coark you can just
[06:44] drop your query and it will just operate
[06:46] the whole thing for you and it can make
[06:47] you a PowerPoint or whatever if you want
[06:49] for example. pretty handy if you're like
[06:51] on the go or you're in the car or
[06:53] whatever and you can use your tools that
[06:56] are connected via MCP or skill that
[06:58] don't require API keys, just MCPS. Um,
[07:01] so still pretty good.
[07:03] >> I'm thinking as well if you're at like a
[07:05] conference or an event and you're
[07:07] speaking to someone, you could, you
[07:08] know, like pull it up there and then and
[07:10] in a couple minutes like during the
[07:11] conversation, you could have like
[07:12] something meaningful to show them too.
[07:14] >> With the new code integration, like you
[07:16] know, we're going to show the site
[07:17] building skill, right? I've built this
[07:18] skill to like start new sites. Um, you
[07:21] could literally talk to someone and just
[07:23] prompt on your phone. I would start a
[07:24] cloud code with that skill. I would spin
[07:26] up prototypes like and then as you're
[07:29] having that conversation is building
[07:31] like I do that quite often on calls. I
[07:32] just launch these things and I'm like I
[07:34] know that's what they want to do and I
[07:35] show them I can achieve 80% of it by the
[07:37] end of the call. So you you could do
[07:39] that like a site redesign or a landing
[07:41] page concept or like a marketing
[07:43] campaign you talked about be like hey
[07:44] you can prototype this, you can do all
[07:45] of that. Like it can do all of that. So
[07:47] it's good. So
[07:48] >> for people who are meeting others,
[07:51] meeting clients, meeting prospects, like
[07:53] in the field face to face, you know,
[07:56] going to their office for a meeting or
[07:59] an event or a conference, then there's
[08:01] probably quite a lot of use cases here.
[08:03] But for you and I who like are scared to
[08:05] leave our bedrooms, um, you know, maybe
[08:08] not quite so much.
[08:10] >> Uh, yeah. I mean I think it's really the
[08:12] idea of like you can take a lot of
[08:13] clothes capabilities outside of like you
[08:16] know having a big screen having multiple
[08:18] windows juggling and it kind of does it
[08:20] for you and it's like it's a first
[08:22] attempt at it. I personally like the
[08:24] idea of moving to asynchronous things
[08:27] where it's like you know you don't
[08:28] necessarily have to hang on the chat
[08:29] window for things to happen. It's
[08:32] getting there and that's what's
[08:33] happening. People are kind of like
[08:34] working more with these tools right now
[08:36] more hours and they kind of feel like oh
[08:38] my god I have all these limits left. I
[08:39] need to use it right now or like I could
[08:41] just keep it going. It's not super
[08:43] difficult. I need to go do groceries
[08:45] where I kind of want to keep my thread
[08:46] going etc. You can start doing these
[08:48] things now as this is going. This is
[08:50] also a big dig at open obviously like
[08:52] this is basically how open CL was
[08:54] working. So now we're like 80 90% open
[08:58] is built into the cloud app already and
[09:00] there's not really much use case for
[09:03] anymore. The obvious limitation which we
[09:06] have talked about in previous episodes
[09:07] is that your computer where you're
[09:10] running cloud code needs to need to be
[09:12] on and connected to the internet. You
[09:14] know, you can't use it. It's not full
[09:15] server side processing at the moment.
[09:18] >> But you can there's plenty of tools to
[09:19] like keep your computer like awake but
[09:21] the screen goes off etc. It doesn't
[09:22] destroy your Mac battery. It's all all
[09:24] on Mac by the way. So it's like if you
[09:26] have a Windows computer, bad luck. But
[09:29] uh yeah, it's it's not too bad. It's
[09:31] just yeah in the use case when like
[09:33] you're traveling your laptop is in your
[09:34] backpack and it's not plugged and
[09:36] everything then it's not going to work.
[09:38] Yeah.
[09:38] >> So you weren't a huge fan of open claw
[09:41] in the beginning anyway. Um is it
[09:43] >> all but dead now like has has just
[09:46] copied the best features and then or is
[09:48] there any use case for it?
[09:49] >> And actually it's better because you can
[09:51] see like this window shows it like the
[09:53] asking for access to things means that
[09:56] they can't just go rogue and just mess
[09:58] stuff up basically. And that's kind of
[09:59] the the thing is like if you want to run
[10:01] a more secure setup then you can
[10:04] basically
[10:06] >> so yeah it's better for 99% of people.
[10:09] It's probably like a bit worse for some
[10:11] people but overall I don't think there's
[10:14] a point if you haven't picked it up and
[10:16] if you don't have your whole setup yet
[10:17] on open I don't think there's a point
[10:20] doing it anymore. You might as well just
[10:22] start on cloud and in two weeks it will
[10:23] cover all use cases.
[10:25] >> Okay sounds good. So on Sunday morning
[10:28] you sent me a message saying that you
[10:30] had created or you set up headless
[10:34] >> headless claude code in notion.
[10:37] >> Um and I've come across this term
[10:39] headless before. It's like a I don't
[10:41] quite understand exactly what it means
[10:43] but we now have a box in our notion
[10:46] setup. It says delegate to claude code.
[10:48] And if you take it, Claude code somehow
[10:52] and I'm hoping you're gonna explain that
[10:53] to me right now goes and executes the
[10:55] task. So what what have you built here?
[10:58] What have you unleashed?
[11:00] >> I mean first of all it's all voded. So I
[11:01] hope things will go okay. You can see my
[11:03] inotion right now actually. So this is
[11:05] kind of experimental still. So this is
[11:07] like a different task database. It's
[11:09] remote from the rest etc. But if you
[11:10] look at the activity you can see that
[11:12] now cloud code is a co-orker basically
[11:14] and it's just tackling tasks. And so the
[11:16] idea is like I can create a task, you
[11:19] know, like I would on notion. I can give
[11:21] it a name. So like I don't know, let's
[11:23] say just test task and I can just say
[11:28] say hello in the comments.
[11:31] That's it. And then if I set it to to-do
[11:35] and I click delegate to cloud code, it's
[11:37] actually going to through an automation
[11:39] on notion, it's going to pick it up.
[11:40] Just give it a minute. You can see that
[11:42] I have this automation and this is a
[11:44] demo but the idea is like when these
[11:46] conditions are gathered then it sends a
[11:48] web hook to a URL I'm not going to share
[11:50] on this podcast and it sends the content
[11:53] of the task and what that does is it
[11:54] starts a terminal headlessly which means
[11:57] it like my screen did not open a
[11:59] terminal right now but I have a little
[12:01] uh thing that says that the server
[12:03] started and you can see that our test
[12:04] just moved to in progress as I was
[12:06] showing you that for example and and so
[12:08] it's going to run my cloud code work
[12:11] folder So with the same folder I work on
[12:13] on VS Code on the terminal or something
[12:15] is the same one with all the skills with
[12:17] everything like and then as I update it
[12:19] it will also update the CL code that
[12:21] works on notion. It just feels like the
[12:23] same person kind of and the point is
[12:26] that it's using the notion CLI which is
[12:30] like it's a single release. It allows
[12:32] cloud to use notion through the terminal
[12:34] and it's just much more token efficient
[12:36] which is what has unlocked this
[12:38] workflow. Um, and the point is like,
[12:41] yeah, I just basically
[12:43] >> So, can you just explain that that bit
[12:44] that it allows claw to use notion more
[12:47] efficiently through the terminal?
[12:48] >> It can basically get the content of a
[12:50] page in markdown format. So, it's very
[12:52] token efficient and then it just can,
[12:54] you know, drop comments. It can create
[12:56] new pages, etc. Um, so for
[12:59] >> it it could do that before using
[13:01] >> just it's more efficient like it's just
[13:03] it's more fluid like it's just it's
[13:05] better using it. Um, and so the idea is
[13:08] like actually just before this podcast I
[13:09] I just wrote that task. I said, "Hey, I
[13:11] need to explain to Mark how this works."
[13:13] Um, so I said, "Hey, I need to make a
[13:16] presentation how it works, blah blah
[13:17] blah. Please make me a presentation.
[13:19] There's a presentation mode on notion."
[13:21] So I was like, "Make me a presentation I
[13:22] can do to mark basically." And then it
[13:25] say it just ran for a bit and then it
[13:27] just dropped a comment that said, "Hey,
[13:29] I made a 12 slide presentation. It's
[13:30] here." And it just kind of like gives me
[13:32] details on the run and it just run the
[13:34] task basically. And so if we open it uh
[13:38] you can see this is the presentation
[13:39] mode. So let me see if I can actually
[13:41] put it uh and let's see what code
[13:43] actually prepared as a presentation. So
[13:45] if I click on present. Oh this is big.
[13:47] Can you see? Yeah you can see
[13:48] >> the task. Yeah.
[13:49] >> So code tasks. What is it? Your notion
[13:52] to do this just learn how to execute
[13:53] itself. The problem you have ideas
[13:55] faster than you execute them. Uh your
[13:57] notion task board is a graveyard of good
[13:59] intentions. [laughter] What if checking
[14:01] your box could actually get the work
[14:02] done? not a VA, not a freelancer by
[14:04] cloud running headlessly on your Mac
[14:06] 247.
[14:07] >> Okay. What is so I mean like if you're
[14:09] listening on the audio version, it's
[14:10] basically
[14:12] >> designer and thing, but there's bullet
[14:14] points, there's like simple explanations
[14:16] of what's happening here. So
[14:17] >> yeah.
[14:18] >> And then it also made you an infographic
[14:21] explaining how this works basically. So
[14:24] yeah, that's the idea.
[14:25] >> And so did Claude use Nanobanana to do
[14:29] that or how did it make the infographic?
[14:31] >> It used Nano Banana. Yeah.
[14:33] >> Okay, cool. So that was like one of the
[14:35] limitations you were saying before with
[14:37] dispatch is that it wouldn't be able to
[14:39] call external APIs but because you're
[14:42] doing it this way it can
[14:43] >> and so you can see for example my test
[14:45] task is actually marked as done and you
[14:48] can see say hello that's it and so just
[14:50] checking as request received executed
[14:51] and done basically and you can see it
[14:53] just so the point is like why do you do
[14:55] that like why why is this interesting
[14:57] right and the point is when you're in VS
[14:59] Code or when you're in a chat interface
[15:01] the problem is that you you kind of like
[15:06] are in the single chat and you don't
[15:08] think of like your projects and how you
[15:10] know you don't think of the high level
[15:11] of the big project that you're doing.
[15:13] You're working on a single task at a
[15:14] time. When you use a tool like notion,
[15:16] you can use things like project
[15:19] templates. So you can have like you know
[15:20] 10 tasks being created in one click and
[15:22] then you can also it's a multiplayer uh
[15:26] workspace which means that if you want
[15:28] to comment on that task and review what
[15:30] cloud did or that presentation he did
[15:31] for me you can jump in and drop a
[15:33] comment right uh and
[15:35] >> so when when I set this up it's using
[15:38] your claw code to execute on it. So it's
[15:40] a way
[15:40] >> I could set it up for you too I would
[15:42] need to set it up for you but yeah the
[15:44] idea as well is I've built some
[15:45] protection in that. So for example, it
[15:47] only will execute if the task was
[15:49] created by me. So if you go in and tick
[15:51] that box, but it's obviously tied to
[15:53] your account. You know, there's a
[15:54] created by property. Then it will
[15:57] actually comment and tag me and be like,
[15:59] is it okay if I run this task? And then
[16:01] if I reply yes, it will run. But if I
[16:04] don't reply or I say no, it will not
[16:06] run. So that's a way to protect uh my
[16:09] computer basically. Uh and you know, any
[16:12] other integration could start creating
[16:13] tasks otherwise. for example, it's a
[16:15] little bit dangerous. So again, this way
[16:17] the only my account can create tasks. So
[16:20] as long as like I don't give access to
[16:21] my account for something else to create
[16:23] tasks in principle, I'm the only one
[16:25] that is in charge. But you can
[16:27] absolutely, you know, go ahead and
[16:29] comment on that presentation and then I
[16:31] can put it back into like to do the
[16:34] status and say go ahead do it and it
[16:37] will read your comment and take that
[16:39] into consideration in the way it's going
[16:40] to revise the task. Um so for example um
[16:43] like I actually worked on building a
[16:45] newsletter skill industry news etc. And
[16:48] you know usually I do that on VS code
[16:49] but like I was like oh what if I run
[16:51] this like a project right I make tasks
[16:53] etc and it just does it and in this case
[16:55] actually I just ask it to research I
[16:57] kind of like prepared the whole outline
[16:59] for the skill and everything and then it
[17:01] ran an eval on all of it and then I'm in
[17:05] the process now where I'm reviewing it.
[17:07] So it's like actually attached all the
[17:09] test newsletters directly in notion. I
[17:12] can highlight text and I can drop
[17:14] comments for example this headline is
[17:16] quite weak or like I say never use m
[17:19] dashes for example etc. So I can kind of
[17:21] review it like I would review a Google
[17:23] doc and then I can put the test back and
[17:25] I be like hey just you update the scale
[17:27] based on my comments on the document for
[17:29] example and you update all that and it's
[17:31] kind of like nicer than working VS Code
[17:33] to be honest.
[17:35] Yeah, I can see that for like editing a
[17:37] document or commenting on a document.
[17:39] You know, the the Google Docs style
[17:40] commenting within notion is really good.
[17:42] >> But also you can review it. You can drop
[17:45] command. I can make a task for you to
[17:46] review to a human and I can make a task
[17:49] for to be like when Mark is done
[17:50] reviewing you update the skill. And so
[17:54] you can see how this become
[17:56] >> like a much better team work. Yeah.
[17:59] >> Uh tool actually than just staying in VS
[18:02] Code. And so that's why I'm like I'm
[18:05] just starting. There's also another
[18:06] thing that this has unlocked that is
[18:08] massively powerful is like if you want
[18:10] to run a code on your VS code, you need
[18:13] to be at your computer and type in,
[18:15] right? Like you can kind of schedule
[18:16] desktop app, but again that's the
[18:18] desktop app that's not your VS code blah
[18:19] blah blah. If I set a due date here and
[18:22] a due time on any task, it will run it
[18:24] at the time end date I set, which means
[18:27] that
[18:28] >> and you can set recurring tasks in
[18:29] notion as well. automatically do that
[18:32] >> which means it's like and again project
[18:34] templates and all of that blocked tasks
[18:37] so I could be like oh Mark reviews and
[18:39] then when that is unblocked then clo
[18:41] reviews it and automatically does that
[18:42] so you can see how you can start
[18:44] building these much more collaborative
[18:46] hybrid workflows where multiple people
[18:49] can actually be part of it and code just
[18:51] becomes one of the co-workers and that
[18:53] still runs on the setup that I've highly
[18:55] customized for my use basically. Yeah,
[18:58] because this is like one of the biggest
[19:00] push backs or questions we get from uh
[19:03] members in the AI accelerator is like,
[19:05] you know, how do I get my team to use
[19:07] this or how do we use this across a
[19:09] team? But like I'm starting to see how,
[19:11] you know, especially for like
[19:12] non-technical people that don't want to
[19:14] open VS Code
[19:15] >> using something like this, especially
[19:17] because everybody's already using Notion
[19:19] or ClickUp or whatever your system is,
[19:21] >> you know, to to build this on. Like it's
[19:23] not a huge leap forward to do that, but
[19:26] it unlocks so much.
[19:27] >> If there is someone not technical in the
[19:29] team, they can essentially piggyback
[19:31] ride my code. So they can set the task.
[19:34] I will still have to approve it, right?
[19:35] But it's just like I can be on my phone.
[19:37] >> But you could set it so you didn't have
[19:38] to approve.
[19:39] >> I could set it so it's just a security
[19:41] thing for me.
[19:43] >> Um, so it's like again, it's always a
[19:44] trade-off between security and and
[19:47] access. I could set it so it could
[19:49] piggyback, right? Nice thing you could
[19:50] have a Mac Mini running and everyone in
[19:52] your team uses the same code for example
[19:54] and it can run like each task is a
[19:57] different thread. So each task is a
[19:58] different one but if I comment back on
[20:00] this task for example right it will
[20:02] reopen the same thread with all the
[20:04] history. So it will not have to rebuild
[20:05] everything. So one task equals one
[20:08] thread and so you get one million
[20:10] context now which is plenty for a task
[20:11] at this point.
[20:12] >> So are you now convinced because I know
[20:14] before this podcast you like I don't
[20:16] really see it. It's like
[20:17] >> how did you figure this out? Because
[20:18] like I haven't seen many people talk
[20:20] about this.
[20:21] >> I just came up with it. [laughter] I
[20:23] just Yeah, I just kind of like came up
[20:25] with it. I was like, is it possible to
[20:26] do this? Is it possible to do that? And
[20:28] I kind of came up with the edge cases
[20:29] like the publish date uh like you know
[20:31] the dates in the future, the security
[20:33] all of that like as edge
[20:34] >> you can't you can't like hack it. You
[20:36] can't change the created by field on
[20:38] notion is that fixed by your account. So
[20:41] that's kind of a way for me to protect
[20:43] it. like you cannot
[20:45] >> change that property once a page is
[20:46] created.
[20:47] >> So it's like it's not perfect. I'm sure
[20:49] there is holes in it.
[20:51] >> So for example, like if you create a
[20:52] task, could I not just then go and edit
[20:54] the task? It's still created by you.
[20:57] >> Yeah, you could. I think you could
[20:58] actually. So I mean in principle inside
[21:00] notion, you are with friends, right?
[21:02] >> Yeah, of course.
[21:03] >> You know what I mean? It's like it's not
[21:05] public on the internet. So it's like I
[21:08] don't feel like I need to build like
[21:09] insane security.
[21:11] But yeah, there's another thing that
[21:14] I've done is I actually clothe connected
[21:16] me to a tool called Swiftbot. I had no
[21:18] idea about it just came up with it was
[21:20] like oh I can actually make you a little
[21:22] widget on your taskbar. It shows you
[21:23] which tasks are running right now on
[21:25] your computer. So you can kind of keep
[21:26] an eye so it kind of like lights up on
[21:28] my taskbar on the right. It's like it's
[21:30] grayed out now because it's not working,
[21:32] but then when it's working, it turns
[21:33] green. And then I can click on it. I can
[21:35] see all the tasks that are running. And
[21:37] then in my VS Code, I've also created an
[21:40] audit skill. So it can kind of like look
[21:42] at what happened. And you know, I can I
[21:45] have a emergency button basically. So I
[21:47] could literally click I could even
[21:49] create a task in notion to just stop
[21:51] everything and it would just stop
[21:52] basically.
[21:53] >> You've built that. That's not like you
[21:55] built those safe.
[21:56] >> This is all custom built basically.
[21:58] Yeah. It's just me talking to AI for
[22:02] Sunday morning.
[22:03] >> Yeah.
[22:04] >> Super interesting actually. Yeah.
[22:05] >> So, okay. I'm happy you're excited
[22:07] because it's like I know before you were
[22:08] like ah
[22:09] >> I mean like I was coming from this the
[22:10] perspective of like there's two of us in
[22:12] our team like we're trying to trying to
[22:14] grow using AI not humans. And you know I
[22:17] could see how this would be super useful
[22:19] like if you had a team that needed to
[22:21] use stuff in your cloud code. But yeah,
[22:23] like the kind of feedback um commenting
[22:27] thing like I can see in
[22:29] >> the comments and back and forth like hey
[22:30] check this out you know I'm working on
[22:32] this with clothes check this out Mark
[22:34] whatever like this is kind of handy you
[22:36] share it with someone else you do all
[22:37] that like and the thing is like you can
[22:39] go further it's like my next step now is
[22:41] prompting the notion AI to write better
[22:44] tasks. So I talk to it and I write the
[22:47] tasks and as the tasks are better laid
[22:50] out I'm hoping to get a better result
[22:52] out of cloud code. So I'm going to use
[22:54] notion AI as a way to administer the
[22:57] task list basically and and all the
[22:59] automations that you can plug into
[23:01] notion as well. Like it's flexible
[23:02] enough as a system that that you can
[23:05] really do a lot. It really is like a
[23:07] it's a total sandbox notion like if
[23:09] you're not used to like constructing
[23:12] things in that way you know we came off
[23:14] of I think to-d doist before this and it
[23:17] was like
[23:17] >> asana
[23:18] >> asana sorry yeah we used to doist before
[23:20] that it was yeah sana's very fixed in
[23:23] the way it works so like you kind of
[23:25] have to have an idea of what you're you
[23:26] want to build with notion which I think
[23:28] puts a lot of people off of it because
[23:30] it's not like the task system
[23:33] >> is not like out of the box so to big but
[23:36] right now literally like this is a
[23:37] sandbox this test list it's just me kind
[23:40] of expand I will expand it I think the
[23:42] test is successful so far as I said I
[23:44] built like an entire new skill etc like
[23:46] it's actually good like it's like it
[23:47] built newsletters I will probably
[23:49] release that skill um like it's good um
[23:52] and uh yeah it's good
[23:54] >> let's talk about on the subject of
[23:56] skills though you know which is what we
[23:58] give away inside the AI accelerator
[24:00] which is the thing we sell but we're we
[24:02] want to talk today about building
[24:05] websites with cloud code because it has
[24:06] changed a lot recently. We have made
[24:09] podcast episodes last year
[24:12] >> on some ways to do this where you would,
[24:14] you know, pick and choose different
[24:15] components and have AI assemble it all,
[24:17] but it's gotten so good right now that
[24:20] it can kind of oneshot a full site. So,
[24:24] do you want to tell us about how the
[24:26] website creation skill works? Yeah, I
[24:29] mean it's like a whole course I made,
[24:30] but I made a skill to kind of like
[24:31] bootstrap the websites, whether that's
[24:33] doing a redesign or starting a new site
[24:36] from scratch. You kind of do both. This
[24:38] is kind of the case study site we built
[24:39] for the course on vibe coding your site.
[24:41] So, I think, you know, compare that to
[24:43] most people's WordPress sites that's
[24:45] live on the internet as well. You can go
[24:46] check it out. It's not perfect. Like, I
[24:48] didn't want to fix all the imperfections
[24:49] because I wanted realistic expectations
[24:51] from people. Um, but I mean, this is a
[24:53] good site. This is your wife's website,
[24:55] right? Uh I mean it's your wife's
[24:57] business that I used as an inspiration
[24:59] for this and it has like you know
[25:00] service pages etc. Like that's a local
[25:03] business. Uh it has
[25:04] >> I would I would say as well like if
[25:06] anyone's ever worked with a web
[25:07] developer like when they give it to you
[25:09] like there's always a bunch of stuff
[25:11] that's that's wrong like you know you
[25:13] notice you want to change. So like yeah
[25:15] >> this was built in two and a half hours I
[25:17] would say of actual work. Like I did
[25:19] more with the shooting etc when I did
[25:21] the course but that's two and a half
[25:23] hours and that includes hosting it. That
[25:25] includes you know hosting the images
[25:27] which is something you need to do with
[25:28] custom size etc. You see there's still
[25:30] like some issues here. For example, I
[25:32] didn't want to remove them. I wanted to
[25:33] be honest with how we did it.
[25:35] >> What is the secret sauce then in the
[25:37] skill and like why is it so good? Is the
[25:40] models better or like what else?
[25:41] >> The models got a lot better. The thing
[25:43] with AI is kind of like every time you
[25:45] do a design you're kind of rolling a
[25:46] dice like it's like you know what I
[25:48] mean? it just kind of and so the idea
[25:49] was like if you roll the dice once you
[25:51] might win or you might lose but if you
[25:53] roll the dice like four or five times
[25:55] like you'll probably have one role that
[25:57] you're probably happy with. So it's like
[25:58] I went after 99 designs like principle
[26:01] which is like you know you go it's a
[26:03] marketplace where you submit a design
[26:04] brief for a website or logo or something
[26:07] and then many designers come up with
[26:10] their version of your branding and you
[26:13] pick the one that wins and you pay that
[26:14] one basically that's kind of the idea
[26:16] right um so I did that with AI and
[26:18] that's what this skill does so it's like
[26:19] this is actually I took one of our
[26:21] members website in the last mastermind
[26:23] call like a very old website called
[26:24] miracledata.com and I was like yeah he
[26:27] could use a redesign Fine. I think we
[26:28] can do better. The idea is like I
[26:30] literally just put his URL in the scale
[26:32] and I told it to not use the images. So
[26:35] it would use images like in the site
[26:37] that I did for the dog training there
[26:38] was images. In this case like this was
[26:40] stock images. So I was like let's not
[26:41] even bother with it. And I told it to
[26:43] just kind of reimagine this business
[26:45] branding from scratch. And it that's
[26:48] what it did. It's kind of like came up
[26:50] with like four different designs that
[26:52] have four directions. And you can see
[26:53] like dark, monumental, light and warm
[26:55] etc. And so the idea is like if you
[26:58] click on each one, it's a completely
[26:59] different direction. This first one was
[27:02] this kind of like dark mode uh city art
[27:04] sourcing etc. Not perfect. You can see
[27:05] there's some issues with the animations
[27:07] here, but overall you get the vibe,
[27:08] right? It's a vibe shot here. And uh not
[27:12] a big fan of that vibe to be honest, but
[27:14] you can say it's a bad design. I think
[27:16] >> I think with with all first designs, you
[27:18] kind of have to imagine them with like
[27:20] images as well because that's really
[27:21] what likes when the site kind of starts
[27:24] to take shape. That's why this one had
[27:26] no images. But I even tried to make some
[27:28] animations, but I would probably put an
[27:29] image here instead, for example. Like
[27:31] the idea
[27:31] >> it looks it looks super clean. Like
[27:34] there's just like
[27:35] >> I mean we've made many websites. We've
[27:37] worked with many companies and many uh
[27:39] web designers, developers over the
[27:40] years, and there's just there's
[27:41] something about like it hit when the
[27:44] quality hits a certain point, it's just
[27:46] like ah yeah, they get it. It's it's
[27:48] crisp. It's clean. They get it. And this
[27:51] one when I saw it this example uh here
[27:53] it's like yeah okay that's that's at
[27:55] that threshold for me.
[27:56] >> Yeah. And like I think this one is also
[27:59] pretty nice actually.
[28:00] >> Different style more traditional but
[28:02] yeah it's still like it's nicely built.
[28:05] Yeah.
[28:06] >> Uh there's a bit of an issue on this box
[28:07] here. You can see like these were one
[28:09] shot, right? Like don't don't judge too.
[28:11] You can fix these things very easily.
[28:12] And so yeah, that's the idea. The system
[28:14] is like it creates multiple shots at
[28:16] your potential branding. Then you you
[28:18] can kind of vibe code a bit and you know
[28:20] ah maybe change the dark green to dark
[28:22] blue or something like that. Then once
[28:24] you've picked a direction I've made
[28:26] another scale that transforms that
[28:28] direction into a design system. So you
[28:30] know if we go back on the dock training
[28:32] site for example if I go on design
[28:33] system which is no indexed you can see
[28:35] that the model has transformed that into
[28:37] a set of rules to reuse everywhere. And
[28:40] so the idea is like you know this is the
[28:42] CSS behind the scenes and all of that.
[28:44] It writes itself a code MD that tells it
[28:46] how to use things and so on, right? Um,
[28:49] and then the idea is after that, so in
[28:51] the lesson I actually just build the
[28:52] design system and I'm like, okay, now
[28:54] let me show you how this works. And I
[28:56] just, you know, I have kind of the
[28:57] homepage like this. I kind of edited a
[28:59] bit since then, but not too much. And
[29:01] I'm like, okay, now you make the about
[29:02] page. Just use the design system, right?
[29:04] And this was one shot. I didn't touch
[29:05] anything after. This just came out as
[29:09] the about page. Now, is it like an
[29:10] incredible about page? No. But it's
[29:13] okay. as this was literally not touched.
[29:14] >> It was better than what we have at the
[29:16] moment, but yeah.
[29:17] >> Yeah. And it's like you don't have one
[29:19] actually. [laughter]
[29:20] So it's like it's better and yeah that's
[29:23] the idea. The idea is like it's able to
[29:25] build more pages any page you want. Same
[29:27] with the contact page. I was like you
[29:28] make a page in the team and I just made
[29:30] this page and even the form is like you
[29:32] know it doesn't look like a shitty
[29:34] gravity form that you embedded quickly
[29:35] or something like it actually looks nice
[29:37] and it's like yeah it's in team. So
[29:39] that's the idea and then after that you
[29:40] can kind of vibe code. We talk about
[29:42] many ways of editing your site and I
[29:45] know a lot of people are like oh but
[29:46] this is code is difficult etc actually
[29:50] not that difficult I'm going to share
[29:52] the code app but you can literally edit
[29:55] these sites on the code app now so if
[29:58] you just open it in the code and then
[30:00] you just tell it to start the preview
[30:01] site you literally have this window here
[30:03] and you can just like select an element
[30:06] like for example I could say maybe
[30:08] services instead of what we do so I
[30:10] click on the element I want to edit
[30:11] I say change copy to
[30:15] services instead.
[30:18] >> You still have to prompt it. You can't
[30:19] just change the what we do text to
[30:21] services text.
[30:22] >> You would need to go in the code for
[30:23] that. But you can literally just select
[30:25] the text and say change it to that
[30:27] basically. And after that, I'm not going
[30:28] to do it, but you click two buttons and
[30:30] it just updates your life.
[30:32] >> So like that's that's how simple it is
[30:33] for at least the base changes. And it's
[30:37] it's much easier now. There's obviously
[30:39] a lot more considerations when
[30:41] publishing a website, you know, things
[30:43] like hosting, SEO. You covered all that
[30:45] stuff as well in the course, right?
[30:47] >> Yeah, it's it's all covered. I know like
[30:48] people have these things and I'm
[30:50] actually going to shoot lessons on how
[30:51] to connect a WordPress install, even
[30:52] your old WordPress site if you wanted to
[30:55] manage a blog on the site. So, you don't
[30:57] even have to migrate anything. You can
[30:58] then move your WordPress site to like a
[31:00] $5 per month hosting. It doesn't receive
[31:02] any traffic. It's just used as a CMS.
[31:04] But I know a lot of people are like,
[31:05] "Oh, how do I upload my blog posts?" I
[31:08] think you should just have cloud code do
[31:09] it for you. But if you really want to do
[31:11] it manually then uh then it's possible.
[31:13] >> Interesting as well. And you you also
[31:15] said that the hosting for these types of
[31:17] sites because you're doing on cloudflare
[31:19] it's more or less free at the volume
[31:22] >> actually. Yeah. Like if you set it as a
[31:23] static site you could get close to like
[31:25] actually a million visits per month and
[31:27] it's still free. So yeah it's very good.
[31:30] And that's the thing it's like and same
[31:31] with like the form for example right
[31:33] again we talked about gravity forms. if
[31:35] you had to pay for Gravity Forms for
[31:37] this like it's like 60 bucks a year or
[31:39] something like this like and that's the
[31:41] problem with WordPress you end up with
[31:42] like five to 10 plugins that you pay you
[31:45] know $30 to $60 per year plus you're
[31:47] hosting
[31:48] >> let's say 30 to $99 per month uh
[31:52] WordPress and then if you want any
[31:53] change or custom development you pay a
[31:55] dev because it's not super easy to vibe
[31:57] code it and so
[31:58] >> or you just don't update it because it's
[32:00] a pain in the ass
[32:00] >> right and so that's kind of the thing
[32:02] it's like now you can literally just
[32:04] connect your codebase into code and you
[32:06] you vibe code your changes. You click
[32:08] the button and then it will I made a
[32:10] video that we're going to email to our
[32:12] subscribers. So, subscribe if you want
[32:13] to see more details.
[32:14] >> Authorityhacker.com/subscribe.
[32:16] >> Yep.
[32:17] >> And then yeah, it just goes live on your
[32:18] site and it's like you can you don't
[32:20] even have to open the code editors
[32:21] anymore. So, I think that you know I've
[32:25] talked for a long time to people like
[32:26] stop using WordPress. It doesn't make
[32:28] sense anymore. And to make matters
[32:30] worse, the creator of WordPress SEO,
[32:33] Yoast, just moved his site to this
[32:36] framework that I just added to the
[32:37] course actually. So the guy who was one
[32:39] of the most invested in WordPress just
[32:41] literally started like moved his site
[32:43] completely was and he's like, "Oh,
[32:44] that's way easier." [laughter]
[32:46] >> Well, there's going to be a long lag
[32:48] here because, you know, WordPress is
[32:50] such a I don't even know what percentage
[32:52] of the internet is these days, but like
[32:54] a significant percentage. Um, and you
[32:57] know, there's people that like aren't
[32:58] going to be involved in this or vibe
[33:01] coding, but there's also, I think,
[33:02] people that have client sites and the
[33:04] clients want to be able to go in and
[33:05] just use, you know, they're used to
[33:07] updating WordPress and the CMS there.
[33:09] But you're saying that they will still
[33:11] be able to do that to like upload blog
[33:13] post
[33:13] >> for the blog. Yeah. Not for the course
[33:15] pages, but for the blog. Yes. Um, yeah,
[33:17] but to be honest, like you should
[33:18] probably set up your clients on cloud
[33:20] and just have them, you know, if they
[33:22] have the CL desktop app, just set it up
[33:24] for them once, then they just have to go
[33:25] to the code tab and they just start a
[33:27] new session and push a strange and it's
[33:29] that more difficult than using a CMS.
[33:31] Sometimes it's easier. So, and the
[33:33] models like know the tech. So, in a way,
[33:35] there's kind of a guardrail that doesn't
[33:36] exist when you edit yourself and you're
[33:38] not technical, you know? So, I don't
[33:40] know. It's like to me I think it's time
[33:42] to change to to open your mind a bit
[33:45] because we are there.
[33:47] >> Okay. Well, and if you are interested in
[33:49] changing your mind and uh launching a
[33:52] new site or landing page using this,
[33:54] then you can head on over to
[33:56] authorityhacker.comacelerator
[33:59] and you can join the AI accelerator
[34:00] there where you get this course, all of
[34:03] the skills, all everything you need to
[34:05] execute on this. Like how long does it
[34:07] take to for someone to spin something
[34:09] like this up?
[34:10] >> I mean to do the site maybe like three
[34:13] four hours. I think like we had someone
[34:14] who's really not technical did do one in
[34:16] five to six hours.
[34:18] >> Um
[34:18] >> and a lot of that is kind of giving
[34:20] feedback and saying you know like you
[34:21] know the angle you want to take who your
[34:23] customers are those those types of
[34:25] >> if you start a clock right now and
[34:26] you're like make a one page site live
[34:30] how fast can you go? I would say 15 to
[34:33] 20 minutes for me.
[34:35] something like that.
[34:36] >> I mean, that's pretty impressive. Um, so
[34:38] yeah, you can get that plus our whole
[34:40] plug-and-play library with all our
[34:42] skills automations workflows prompts
[34:45] that are actually useful for business
[34:47] owners and knowledge workers. Everything
[34:49] we build in there is is tested by us. We
[34:52] spend a lot of time making sure it's
[34:53] actually usable and it's stuff that we
[34:55] would actually use ourselves. So, if you
[34:57] are afraid of being left behind by AI,
[35:00] um, fear not. You can join the AI
[35:02] accelerator at authorityhacker.comai
[35:05] accelerator. But speaking of fears,
[35:07] something which is scaring a lot of
[35:09] people has happened to the limits in
[35:14] >> Claude. And we talked about this last
[35:16] week on this show where they had this
[35:19] like double usage promo that was going
[35:21] away at the end of the month, but we're
[35:23] not even at the end of the month yet.
[35:25] And something kind of underhanded seems
[35:28] to have happened. There are a lot of
[35:30] reports now over the last 24 hours um on
[35:34] Reddit and on other places. Someone's
[35:35] even consolidated all the reports into
[35:38] this one Reddit thread
[35:40] >> um of people essentially getting like a
[35:42] quarter of the use usage they were, you
[35:45] know, not even including like the double
[35:47] usage promo. So like it seems to have
[35:49] fallen off a cliff somewhere. I think
[35:51] people are suspecting that maybe
[35:54] Anthropic is trying to kind of like
[35:55] secretly dial it down behind the scenes.
[35:58] There's rumors of that. We have nothing
[36:00] to confirm that. But Anthropic also
[36:02] haven't released a statement or
[36:03] explained what's happening here.
[36:05] >> They're not answering to anyone.
[36:07] >> Yeah. Usually when there's a problem,
[36:08] they were like, "Oh, we have a problem.
[36:10] We're going to look at this." And then
[36:11] they reset the limits. That's kind of
[36:12] like the way it works. Codex has done
[36:14] that so many times. It's kind of a meme
[36:15] at this point. How many times they
[36:17] limit. But now they're saying nothing.
[36:20] And the best time to hide reduction in
[36:23] limits is like during these two times
[36:25] promosing because it's kind of blurry,
[36:27] right? your usage changes all the time,
[36:28] like usage limit changes all the time.
[36:30] It doesn't feel like you don't really
[36:32] understand what the baseline is because
[36:34] it's always different.
[36:35] >> No, when the the promo so that when the
[36:37] promo does end, you're like, "Oh, it was
[36:39] because it was because [laughter] the
[36:41] promo ended rather than because they
[36:43] dialed it down behind the scenes." Okay.
[36:44] >> So, my I mean that starts to confirm
[36:48] what we said in last week's episode. So,
[36:49] I kind of feel good about that. don't
[36:51] feel so good looking at my usage limits
[36:53] because yesterday I was not even using
[36:56] it that much and it just hit the limits
[36:58] like really really quickly. So yeah, I
[37:01] as we said you're probably going to have
[37:03] to end up paying more for what you used
[37:05] to have and it starts this step one
[37:08] basically and then in one week
[37:11] >> this 2x usage limit ends. Now what's
[37:13] interesting with the two exit limits
[37:15] from entropic is that you know they do
[37:16] different times which you know they have
[37:18] essentially peak time and not peak time
[37:20] which works a little bit like
[37:21] electricity you know um and if you think
[37:23] of their data centers it's a little bit
[37:25] similar like they have the time where
[37:28] everyone's coding at the same time they
[37:29] need all the GPUs that they have and
[37:31] then during the off peak time they have
[37:34] a lot of their GPUs that are like not
[37:36] even used right and so I'm wondering if
[37:39] they're not thinking of introducing this
[37:41] peak time of peak time usage limits and
[37:44] if these things could not become
[37:46] something that stays maybe not as much
[37:49] usage etc. But it would make sense
[37:51] logistically.
[37:52] >> It's it's a good analogy. It's a good
[37:54] analogy looking at the power grid
[37:55] because all of the problem with power
[37:57] generation is peak usage, right? And how
[38:00] do you address that? If you can spread
[38:02] it out among other to other times, it's
[38:04] so much easier to manage. And maybe
[38:08] that's why they're pushing a lot of
[38:10] these tools like schedule tasks, like
[38:12] dispatch, you know, so you're able to
[38:14] actually do stuff which you don't
[38:16] actually need to do right now in this
[38:18] second, but just because you're at your
[38:19] computer,
[38:20] >> you can do it. You can set that to run
[38:22] overnight during off peak hours when
[38:24] it's cheaper and you're not going to hit
[38:26] your limits as fast. So yeah, I can I'm
[38:28] starting to see like a a strategy
[38:31] evolving here amongst everything that
[38:33] they're throwing out there.
[38:35] >> Yeah. And if you think also there's a
[38:36] Sam outman interview recently where he
[38:38] actually used the same analogy of like
[38:40] oh we think that people are going to be
[38:42] buying metered intelligence from us the
[38:44] same way you buy metered electricity. Uh
[38:46] I think because they have to think of
[38:48] the logistics of the delivery which you
[38:50] don't think about as a user but for them
[38:51] it's like servers energy usage GPUs etc
[38:55] like they think a lot in these terms and
[38:57] how do we like maximize the usage.
[39:00] My guess is maybe at the end of this
[39:02] promo we see the introduction of peak
[39:04] time and uh you get maybe the usage
[39:08] limits that you used to have at the off
[39:10] peak time and then you get reduced usage
[39:12] limits during the peak times and then
[39:14] that becomes semiacceptable to people.
[39:17] >> Yeah. Because that's like if they
[39:19] instead of taking away like we know this
[39:22] is getting taken away but if they then
[39:23] in April introduce off big time and give
[39:26] you more back that's like seen as a
[39:28] positive thing. So yeah, that's that's
[39:30] how I would do it.
[39:31] >> Maybe that exactly like it's like
[39:33] knowing how companies have to manage
[39:34] resources, it's like it's not a given,
[39:36] it's just a hunch, but so far the hunch
[39:38] has been correct, right? So uh
[39:40] >> I think it's I think it's all worth
[39:42] putting into context as well. It's like
[39:43] it's still massively subsidized. Like
[39:45] they're losing money on all the
[39:47] processing that they're selling us
[39:49] through our through our
[39:50] >> to get closer to the baseline
[39:51] eventually, right? It's like they it has
[39:53] to happen and it's like it's a mix of
[39:56] like gains in efficiency that are
[39:58] invisible to you. So like they manage to
[39:59] run the model for cheaper but they don't
[40:02] increase your limits. Uh and on the
[40:03] other side just reducing your limits.
[40:05] Yeah.
[40:06] >> Um like sorry to go off track a little
[40:08] bit. We hadn't sort of prepared for this
[40:09] but like I'm hearing a lot of news about
[40:12] them trying to build not necessarily
[40:14] anthropic but um Elon Musk trying to
[40:17] build like AI data centers in space.
[40:20] Have you been following that? Is that an
[40:21] energy thing as well or what's going on
[40:22] there?
[40:23] >> There's two things that are bottleneck
[40:25] with these things, right? It's like
[40:26] energy and when you're in space you can
[40:28] capture like way more sun energy there
[40:30] like not the atmosphere and second
[40:32] cooling is a big problem for these
[40:34] servers and guess what is called outer
[40:37] space [laughter] and it's like infinite
[40:39] cooling and so it wouldn't be hard to
[40:43] like literally just cool things in
[40:45] space. So like for these two reasons it
[40:47] kind of makes sense. Google is also
[40:48] working on it. They said that they're
[40:50] already doing tests this year. They will
[40:51] launch some uh stuff in space this year.
[40:54] Yeah. And just as you said that I was
[40:56] like, "Yeah, of course." Like it's
[40:57] really cold in space, but you also have
[40:59] 24 hours sunlight, right? Because
[41:00] >> Yeah. Exactly. So they can have the
[41:02] satellites. Yeah. Exactly. So it kind of
[41:04] makes sense. They can harvest more
[41:05] energy and the cooling is also sorted.
[41:08] The obvious problem is like something
[41:10] gets down like like how do you reboot?
[41:12] Where's the reboot button? [laughter]
[41:14] >> Yeah. Yeah.
[41:15] >> So
[41:15] >> send an engineer up there. Yeah.
[41:17] >> Yeah. I mean that's exactly that's
[41:19] exactly the idea. But like they imagine
[41:21] that the demand is going to be so big
[41:23] that it's going to be worth the costs of
[41:26] [snorts]
[41:27] like having it so remote basically. So
[41:29] it's like you know it's kind of a
[41:31] moonshot at this point. It sounds a
[41:32] little bit crazy but if we 1,00x our
[41:37] demand and also you know the US has a
[41:39] big problem which is the power grid
[41:40] cannot sustain the upcoming demand. like
[41:42] they this power grid sucks in the US and
[41:45] so like they have that problem if the
[41:46] administration wants them to run this in
[41:48] the US for security reasons for
[41:51] patriotic reasons or whatever and at the
[41:53] same time they don't have the energy
[41:54] [laughter]
[41:55] so it's like well space sounds not too
[41:58] bad you know this by an island I guess
[42:01] but yeah
[42:01] >> great let's move on then let's talk
[42:03] about openai's alleged or proposed super
[42:06] app that we're hearing about so last
[42:08] week we talked about that leaked memo
[42:10] where they they basically They said,
[42:12] "Hey, we need to focus on enterprise and
[42:15] on coding because that's where the money
[42:16] is and we need to make money."
[42:18] >> Um, we're hearing now that they're
[42:21] planning on merging chat GPT desktop
[42:24] app, codeex, and even the Atlas browser
[42:27] all together into one like chat GPT
[42:30] OpenAI super app. So, what have you
[42:33] heard about this and is it a good idea?
[42:35] I mean, we haven't heard much, but
[42:36] there's a lot of devs on X, like, you
[42:38] know, from OpenAI that are hinting at
[42:40] this, like, oh, it's all coming together
[42:42] and so on. I think it's a good idea.
[42:44] Like, the CH GPT desktop app is
[42:46] basically abandonware at this point.
[42:48] Like, it's missing most of the new
[42:49] features that have been coming out.
[42:51] There hasn't been many coming out to
[42:52] CHP, but even even it's missing that
[42:55] stuff. Uh, it's bad. The Atlas browser
[42:58] is like two guys running it on X as
[42:59] well. like there's literally like
[43:01] there's no money behind it and it's so
[43:04] slow at updating that it's like it's not
[43:06] great. The only thing that has momentum
[43:08] right now is codeex and codex is great
[43:11] but again it's very code oriented and
[43:14] they're missing this co-work type thing
[43:16] like this how do you use something like
[43:18] codeex for everything and so I think
[43:20] they're kind of like the idea would be
[43:22] like the chat of charge could become
[43:24] this co-work thing probably or like
[43:26] maybe this app becomes as they focus on
[43:28] professionals co-work plus codeex and
[43:30] then the charg app stays for consumers
[43:33] basically
[43:33] >> I disagree I think centralizing it all
[43:35] in one app like it gives them access to
[43:37] their distribution that they have
[43:39] through the GPT name and stuff. But I
[43:41] would say that you know 95% of Chad GPT
[43:43] users they've never even heard of Codeex
[43:45] or Atlas.
[43:48] >> But but this will give them access to
[43:50] those in the same way like Claude
[43:52] introduced co-work in the claude app. So
[43:54] everyone that uses claude is now aware
[43:56] of co-work and now of claude code
[43:58] because that's in there as well. So it's
[44:00] kind of like you know bringing people up
[44:01] that value chain that ladder those who
[44:03] are willing to take it. But chat just
[44:05] has such wide distribution that that's
[44:08] going to be you would think a big
[44:09] advantage for them in getting their paid
[44:11] products uh to a wider audience.
[44:13] >> Yeah, I think it's again more formal
[44:15] from cloud, right? Because clo has been
[44:16] consolidating everything in one app and
[44:18] the cloud app was like laughingly slow
[44:20] for a long time, but they've actually
[44:22] optimized it a lot recently and it's
[44:23] acceptable. I wouldn't say it's great,
[44:25] but it's acceptable again because
[44:26] they're vi coding it all. So now they
[44:28] can have loops of just optimizing the
[44:30] app on its own and it's decent. And I
[44:32] think yeah they they see that the app
[44:34] usage on cloud is high. The app usage
[44:36] like you should not use the desktop app
[44:39] on Mac for chargely outdated at this
[44:42] point and uh they're missing out. Yeah.
[44:45] >> It's interesting this notion of a super
[44:47] app because I think that originated in
[44:49] China with um is it WeChat?
[44:52] >> Yeah. And there was another one as well
[44:54] which basically does like it's like
[44:56] messaging, blogging, food delivery, uh
[45:00] you know your your email,
[45:03] like it it's like it's it does
[45:04] everything you'd need. You can actually
[45:06] only use that app and like do most of
[45:09] the things you would need to do
[45:10] throughout your day. that doesn't exist
[45:12] so much in Europe in the US because you
[45:15] know Uber is separate from WhatsApp is
[45:19] separate from Google Docs uh Google
[45:21] Drive you know like
[45:22] >> I don't think that's where they're going
[45:24] though I don't think they're starting a
[45:25] social network or something like that I
[45:27] just can't imagine it so yeah I don't
[45:30] think it's going all the way to a super
[45:32] app but it's more like a super app that
[45:34] has every service that open AAI offers
[45:38] >> yeah but you know you at the same time
[45:40] you hear the kind of longer term vision
[45:42] of these AI companies just eating, you
[45:45] know, smaller businesses, especially SAS
[45:47] tools, things like that.
[45:48] >> If
[45:50] OpenAI is bringing Atlas, which is a
[45:52] browser, into the chat GPT app,
[45:55] >> suddenly like the possibilities for what
[45:57] you can do in that one app become pretty
[46:00] interesting. So yeah, I mean we were a
[46:03] while away from seeing this come into
[46:05] into play, but uh we'll definitely
[46:06] >> even slowly open AI ships is like it's
[46:09] going to take a while because like you
[46:10] know clo delivers an update every day
[46:12] and when was the last time you saw
[46:13] something you charge GPT it's been a
[46:15] while. Um so
[46:17] >> they haven't hit that low state with
[46:19] their releases yet. So
[46:20] >> they must be in full panic state right
[46:22] now like when they see the speed at
[46:24] which entropic is shipping and then how
[46:25] slow they're getting. Like Codex is fine
[46:27] like the Codex team is fine but
[46:28] everything else in OpenAI sucks. Uh, and
[46:31] the models are good too, but yeah, the
[46:32] product is not there. So,
[46:33] >> and speaking about uh anthropic shipping
[46:37] stuff fast, couple of other things that
[46:38] they've released this week. Um, yeah, so
[46:41] they released Claude computer use. This
[46:45] lets you use your computer, your
[46:47] keyboard and mouse from Claude. Uh, you
[46:50] have to update your app to the latest
[46:52] version to be able to use this. Um,
[46:54] what's your first impression scale?
[46:57] >> Uh, it's like it sounds very cool. like
[47:00] it basically it's a user of your
[47:02] computer. It just can open a window. You
[47:03] can click on things. It can do things.
[47:06] The problem is like how much of your
[47:07] life apart from like your VS Code setup,
[47:09] how much of your life is still locally
[47:12] on your desktop with something that you
[47:13] could not use in the cloud? To me, not
[47:15] that much to be frank. And so like
[47:18] sounds very cool in practice. It's
[47:20] pretty handy if like there's a file that
[47:22] you forgot to download on your downloads
[47:25] folder for example and you need it right
[47:27] now and you're on your phone like it can
[47:29] do that. And I think what it's good for
[47:31] is it like all the apps that don't have
[47:33] an MCP. So like you know they show
[47:34] Photoshop for example. Um that's kind of
[47:37] interesting. Um maybe for that it's
[47:40] okay.
[47:41] >> But what's actually happening just to
[47:43] explain is that it's taking a screenshot
[47:46] of your screen. It's analyzing that
[47:48] screenshot. It's thinking and it's
[47:50] reasoning with itself and then it's
[47:52] executing the mouse or the keyboard
[47:54] press.
[47:54] >> Yeah.
[47:55] >> So although the keyboard press and the
[47:56] mouse click it is very fast. It can
[47:58] enter data quickly.
[47:59] >> Takes time.
[48:00] >> Taking that screenshot and thinking and
[48:01] reasoning is not fast at all. So you
[48:04] know it's not doing any tasks that you
[48:06] can do yourself really much faster at
[48:09] least at a basic level. I'm sure there
[48:11] you could kind of build some combination
[48:13] things there that would work. But yeah,
[48:16] like the use cases I've seen other
[48:18] people um share with this have been like
[48:20] super weak and I just yeah I haven't
[48:22] been impressed with it and it's like I'm
[48:23] not really that motivated to use this
[48:25] right now.
[48:26] >> One thing that's also kind of like
[48:27] limiting is that the vision capabilities
[48:30] of Antropic, they're not amazing. So,
[48:33] I've seen it when I do website design.
[48:35] You know, I have this loop where I
[48:36] connect the Chrome MCP and it kind of
[48:38] like opens the website, starts taking
[48:40] screenshots and looking at things and it
[48:42] misses a lot of small issues that I have
[48:44] to point myself. Hopefully, this
[48:45] improves, but obviously for this kind of
[48:47] work, like Photoshop, like obviously
[48:51] it's not going to be very good at it.
[48:53] And so, that's the problem is that
[48:55] Gemini for example is a lot better at
[48:57] vision than entropic. sucks at
[49:00] everything else much more, but it's
[49:02] better at vision. And so, like, again,
[49:05] this Photoshop example, in my opinion,
[49:08] like the chances of you getting like a
[49:10] good image out of the model using
[49:12] Photoshop for you are fairly low, I
[49:15] would say. And
[49:16] >> you need to think as well that they can
[49:19] the terminal use allows you to do so
[49:21] much stuff already, like you know,
[49:23] resizing images and cropping and
[49:25] everything. You know, our thumbnails,
[49:27] they're made by like adding our photos
[49:28] on top of a background generated banana
[49:30] banana. That's not made with computer
[49:33] use. It's not like taking the mouse and
[49:35] moving the thing. It's literally just
[49:36] using the terminal to just superose an
[49:38] image without using a mouse. And it's
[49:41] arguably a better user of the terminal
[49:44] that it is at using your mouse and
[49:46] keyboard. So it's almost like because
[49:49] people don't really understand
[49:51] everything you can do with terminal
[49:52] comments that like it kind of bridges
[49:55] that cognitive gap of like what can AI
[49:57] do. It does open some more like as I
[49:59] said on the apps that cannot be used
[50:01] with a terminal but I don't think it's
[50:03] as big of a leap as people think it is
[50:06] but it's a cool edge case like it's fine
[50:08] for daily release. I'm just don't think
[50:10] it's a revolution. Yeah, it feels like
[50:12] using the model to decide what to do and
[50:15] to like take screenshots. It's just a
[50:17] bit kind of a janky process like there
[50:19] needs to like if there's some deeper
[50:20] integration into your like operating
[50:22] system.
[50:23] >> Yeah, it could be a bit faster and it's
[50:26] like almost like streaming it rather
[50:28] than taking screenshots every every time
[50:30] it does something like it would just do
[50:33] it a lot faster. So,
[50:34] >> yeah, we're not there yet.
[50:35] >> I'm sure it'll come, but we're not there
[50:36] yet. Uh where we are though with uh
[50:40] again another claude feature that they
[50:41] released in the last week is visual and
[50:44] interactive content. So this transforms
[50:46] claude chatbot from instead of just
[50:48] giving you text back all the time, it
[50:51] now starts generating these visual andor
[50:54] interactive elements. So you can trigger
[50:57] it. Here's an example of what's the
[50:59] weather today and it showed you like a
[51:00] moving cloud in the background. You
[51:02] know, not that impressive. Where it I
[51:05] think comes into its own is if you ask
[51:07] it to for example show me how inflation
[51:11] works instead of like how does inflation
[51:13] work but if you use the word show me or
[51:15] something similar it went and without
[51:17] any other prompting just built this
[51:19] interactive inflation calculator that
[51:22] you can you know increase the inflation
[51:24] rate uh the number of years starting
[51:26] saving point and like it shows you how
[51:29] inflation eats into your savings over
[51:30] time and then how much milk or rent is
[51:33] likely to increase. Uh,
[51:35] >> can we have a graphic on how tariffs
[51:37] work for some people that don't
[51:40] [laughter]
[51:40] >> Yes. Can you do that?
[51:43] >> Um, it could absolutely do that. Whether
[51:45] or not you will believe that that's how
[51:47] they work might depend on um how you
[51:49] vote, but we won't get into that today.
[51:52] >> This is Yeah, it's interesting in its
[51:54] own right. You you said you were using
[51:55] it for um like shopping and like
[51:59] understanding like difference in
[52:00] products which is something that a lot
[52:02] of our older listeners will be familiar
[52:04] with in terms of creating you know like
[52:06] roundup reviews reviews of products on
[52:08] on websites something we used to do a
[52:11] lot back in our SEO days but this is
[52:13] really starting to eat into what you
[52:16] would see on some of these these
[52:18] resources. So for me, this kind of feels
[52:20] like at least one part of the browsing
[52:23] experience from a a shopping or an
[52:25] information gathering perspective is
[52:27] being replicated inside the chatbot
[52:29] here. So again, another reason why we
[52:31] don't need to use our browser to find
[52:33] certain types of information.
[52:35] >> And that's the thing is like people were
[52:36] like, "Oh, but like if you, you know,
[52:38] put all this effort in making these
[52:39] custom graphs and everything that AI
[52:41] can't do because it's just text, etc."
[52:44] And well, here we are. It can now now do
[52:47] all of it. You can, by the way, you can
[52:50] share this, but it'll just share an
[52:51] image of it. But you in Claude, you can
[52:53] save it as an artifact
[52:55] >> and then uh share that. You can publish
[52:58] that artifact and then share that and
[53:00] other people can use that as well. So
[53:02] again, pretty cool, I would say.
[53:04] >> Yeah, I like this. I actually use the
[53:06] chat app quite a lot on my phone. I like
[53:08] to use the chat app and I almost like
[53:10] using the chat back now. Like I have
[53:12] this crazy VS Code setup, etc. But
[53:14] sometimes you kind of want to go back
[53:16] when you think in principles and high
[53:18] level ideas. It's kind of nice to go
[53:19] back to a contextf free uh discussion
[53:22] and talk about ideas and based on what
[53:24] comes up there then you go back to your
[53:27] big VS code setup with all your stuff
[53:29] and then you just actually execute on
[53:31] that. Um so it's like saying saying one
[53:34] of the benefits of chat bots is that it
[53:36] doesn't have context.
[53:37] >> Yeah. Okay.
[53:38] >> It's not biased. You
[53:39] >> kind of come full circle in a way.
[53:41] >> Yeah, you do. It's like it's sometimes
[53:42] it's nice to kind of like work in an
[53:44] unbiased environment and you do want it
[53:46] to be biased when you work on tasks and
[53:48] have all the context etc.
[53:50] It's nice to it's almost like fresh
[53:52] perspectives, right? It's like instead
[53:53] of being completely ingrained in what
[53:55] you do and knowing exactly how you would
[53:56] do things, it actually takes a step back
[53:58] and gives you different perspectives and
[54:00] that broadens your horizon. So, it's
[54:02] like I actually do use the chat quite a
[54:04] bit for that and and quite often and
[54:06] then work is done on my VS Code setup
[54:08] still and now starting to be on the
[54:10] ocean as well.
[54:11] >> Okay, so that's been everything we're
[54:13] going to go through this week. Any final
[54:14] words of wisdom, Gail? Um, no, just uh
[54:19] just again things are moving. I think
[54:20] the website stuff is probably like the
[54:22] one that is the most important for
[54:24] people on this episode. Um, it really is
[54:27] not that difficult. It you don't need to
[54:29] know code to make websites. Like making
[54:31] custom SAS with complex API keys, et
[54:34] like maybe you shouldn't start there.
[54:36] But like simple HTML websites now, I'm
[54:40] 99% sure they look better than your
[54:41] site. I'm 99% sure they're faster than
[54:44] your site. I'm 99% sure the code is
[54:46] cleaner than your site and I'm 99% sure
[54:48] it's easier to administrate than your
[54:50] site. Um, and so it's
[54:52] >> Yeah, just just to interject there, it's
[54:54] not just for like redesigning your
[54:56] website, right? If you are in the
[54:58] marketing department and you want to run
[54:59] a campaign for a new product that you're
[55:01] launching or something like that, you
[55:03] can, you know, just launch a landing
[55:05] page for that. It kind of frees you in a
[55:07] way of having to go through, you know,
[55:09] procedure and red tape to get a new page
[55:12] uh deployed and that might have been
[55:15] quite restrictive for certain small
[55:16] businesses before.
[55:17] >> Yeah, you can just put it on a
[55:18] subdomain, right? If you want to do a
[55:20] PPC campaign or something like that,
[55:21] like it's super easy and you don't need
[55:23] to redesign your website. Actually, the
[55:24] skill I did can lift off your branding.
[55:27] So, it's like it can go on your existing
[55:29] website, lift your branding, your fonts,
[55:31] your color codes, etc., and build
[55:33] landing pages that use that branding.
[55:36] So, it's like it's not going to be one
[55:38] to one perfect, but it's going to feel
[55:40] branded. Um, and then you can steer it
[55:42] from there. And as a treat for those
[55:44] who've listened to the end of the
[55:45] podcast, I think we can reveal that
[55:47] we're actually about to redeploy or um
[55:51] release the new version of our website
[55:53] and authority.com as as
[55:55] >> Exactly like that. Yeah.
[55:57] >> Yeah.
[55:57] >> So, it's like we do what we say. By the
[56:00] time this goes out, is it going to be up
[56:02] or later?
[56:03] >> Uh, maybe. Maybe. It's like just I don't
[56:06] want to be saying for sure because I
[56:08] don't know when this goes up and if
[56:09] there's any issues. But, uh, hopefully
[56:11] depends on your review. I'm waiting for
[56:13] you to review it.
[56:14] >> Uh, either way, it's something I think
[56:16] we could probably talk a little bit
[56:17] about next week on the podcast. So,
[56:20] thanks for watching. Don't forget to
[56:22] subscribe so you don't miss that episode
[56:24] as well. And if you're on YouTube, drop
[56:26] us a comment with your thoughts on any
[56:27] of these stories. We read through them
[56:29] all and uh respond to those.
