# 5 Months Of Claude Code (As A Business Owner)

- YouTube: https://www.youtube.com/watch?v=OYJa8XPd210
- Video ID: OYJa8XPd210
- Upload date: 2026-05-21T03:01:17-07:00
- Transcript source: supadata
- Status: ok
- Language: en
- Fetched at: 2026-07-03T17:13:32+00:00
- Supadata billable requests: 1

## Transcript

[00:00] I let my co-founder roast my Claude code
[00:03] setup live in this video and he didn't
[00:06] hold back. So 5 months in, I thought I
[00:09] had Claude Code pretty dialed in. But it
[00:11] turns out my claw.md file is missing the
[00:14] most important thing. My folder
[00:16] structure is making my life harder and
[00:19] I'm still manually triggering a whole
[00:21] bunch of tasks that Claude could be
[00:23] doing automatically for me. So, in this
[00:25] video, we're going to go through the
[00:26] whole audit, the specific fixes I'm
[00:28] making this week, and the one rule Gail
[00:32] says every business owner should add to
[00:34] their claw.md so it maintains its own
[00:37] documentation as you work. We're Mark
[00:39] and Gail from Authority Hacker and we
[00:41] teach real world cla
[00:44] to busy online business owners. All
[00:46] right, Mark. So we are reviewing your
[00:49] setup today and let's just start with
[00:52] like what are you using code code for
[00:55] day-to-day like I want to you know I
[00:57] want to see what you use it for and how
[00:59] you use VS code how you do all that
[01:01] stuff and let's try to modernize your
[01:02] setup a little bit. Okay. Sure. So, I do
[01:05] a lot of oneoff kind of marketing
[01:08] businessy type tasks. So, think if we're
[01:11] doing a promotion with a different
[01:13] community or a JV webinar or a launch or
[01:18] something like that. It tends to be
[01:19] quite unique. So, I'll use it for kind
[01:21] of organizing the project and for, you
[01:24] know, creating emails, creating
[01:25] marketing materials and that. I use it a
[01:27] lot for kind of troubleshooting AI when
[01:29] I'm trying to set up. A good example
[01:32] would be the meta ads conversion API or
[01:35] their new meta ads CLI like figuring out
[01:37] how to set that up because it wasn't
[01:39] super obvious.
[01:40] >> Building some basic automation things
[01:43] for example welcome email sequences to
[01:46] new members which you know it's mostly
[01:48] creating the content for that rather
[01:50] than the full end to end automation. Uh
[01:53] I've got some regular processes I would
[01:56] say I do you know almost every week or
[01:57] every couple weeks things like uploading
[01:59] the podcast. So creating thumbnails,
[02:02] titles, descriptions, you know, chapter
[02:05] markers, like all those kind of things.
[02:07] I do uh our email newsletter, some
[02:10] customer support things. Again, that's
[02:12] not really well kind of integrated into
[02:14] all our tools. I'm still kind of copy
[02:16] pasting.
[02:17] >> That's why I want to dig. That's why I
[02:18] want to dig [laughter]
[02:20] >> in our uh AI accelerator for the plus
[02:23] members. Um when people apply for that,
[02:25] we review them manually. So I'll go and
[02:27] kind of use AI to help me. I mean, I
[02:29] still look at it, but I use AI to help
[02:32] me kind of draft the responses to that
[02:34] and whatnot. Uh, all of the changes on
[02:36] our website, so new landing pages, you
[02:39] know, changes to the sales page, things
[02:41] like that, I do using cloud code as
[02:44] well.
[02:45] >> Do you run everything in VS Code? Is
[02:47] everything running through VS Code?
[02:49] >> 99%
[02:51] of the time I use VS Code. So, I do have
[02:54] the Claude desktop app and I do have
[02:56] Claude code set up on the same folder
[02:58] working, you know, with all the same
[03:00] information. I just find myself not
[03:03] using it that much. Maybe sometimes when
[03:06] I
[03:07] >> I don't even know why to be honest with
[03:09] you. The main times I use it are when I
[03:12] have so many tabs open in VS Code that
[03:14] I'm like, ah, I don't want to lose
[03:15] everything. I'll just use clo desktop
[03:17] for a while.
[03:19] >> Interesting. Okay. Okay. Cool. I think
[03:21] we'll talk about that. I think it's
[03:22] quite interesting to talk about the
[03:24] desktop app versus VS Code as well
[03:26] because things have changed quite a bit
[03:27] recently.
[03:28] >> Yeah.
[03:28] >> Uh and actually my recommendation is
[03:30] most people start on the desktop app
[03:32] right now. I'm actually going to update
[03:33] our course soon based on that
[03:35] >> and the reason why is because you see
[03:37] how like let's say you're working VS
[03:39] code now and your folder is called code
[03:41] but that means you're basically dumping
[03:43] everything you do in this folder, right?
[03:45] And eventually this folder gets messy
[03:47] and we'll talk about organization etc.
[03:49] But obviously you're going to have a lot
[03:51] of your stuff in there. But like the
[03:52] reality is like your job is many things,
[03:54] right? Is some support, some website
[03:56] stuff, some marketing, and within
[03:59] marketing there is email and there is
[04:00] ads and there is you know what I mean?
[04:02] Like you could kind of like break it
[04:03] down
[04:04] >> and and the you know where the code
[04:06] desktop app wins over VS Code is in VS
[04:09] Code you're working in that one folder
[04:10] here that you open. So you kind of have
[04:12] to dump everything. Whereas on the cloud
[04:14] desktop app, you can open multiple
[04:15] folders and they all run in parallel and
[04:17] you can essentially just chat with
[04:18] either folder depending on where you
[04:20] click. And what that means is you can
[04:21] kind of be more granular and then you
[04:23] can do more customization in your code.
[04:25] MD and in how things work in the context
[04:28] etc. And you can start organizing things
[04:30] a little bit differently and so I tried
[04:33] to do that. I mean I set up VS code
[04:35] before the cloud code and the cloud
[04:37] desktop app was really a thing. I tried
[04:39] to do that with this areas section here.
[04:42] >> Yeah. Uh so I have my
[04:43] >> and you were opening the subfolder
[04:46] >> initially I was but then I got lazy and
[04:48] stopped doing it. So for things like
[04:51] podcast or even marketing in general
[04:53] email marketing I would have like
[04:54] different claw.md files here
[04:57] >> and then in my root claw.md
[05:01] folder
[05:02] >> it would have it would kind of like
[05:03] mention the different directories and
[05:05] you know some of them have area context
[05:06] some have different claw.md files. So, I
[05:09] mean that was the thinking like honestly
[05:12] it's not wellmaintained and uh
[05:14] >> and then you end up with like 60 like
[05:16] windows of VS Code all floating on top
[05:18] of each other and your desktop becomes
[05:20] overwhelming and you're like this was
[05:22] supposed to be simpler and uh
[05:24] >> Yeah. And I think what's happening now,
[05:26] so I'm 5 months into it, something like
[05:28] that.
[05:28] >> Yeah.
[05:29] >> Is it's still doing a really good job.
[05:31] like it for whatever reason it
[05:32] understands mostly what we're doing. But
[05:34] I feel like I feel like we're starting
[05:36] to get a bit of drift
[05:37] >> in that you know some things we do in
[05:39] the business have changed a little bit
[05:41] >> and I haven't necessarily found out
[05:44] where that's still referenced in my file
[05:47] structure and yeah it's just it's not
[05:49] too bad now it's still like very very
[05:51] good but I feel like if you fast forward
[05:52] another six months some things might
[05:54] start to get too far out of sync if that
[05:56] makes sense.
[05:57] >> Which is why I'm changing a little bit
[05:58] my opinion. And it's like initially when
[06:01] we talk code it was like oh work within
[06:02] that one folder and keep it organized
[06:04] but now I feel it's almost better to
[06:06] kind of split it up and that's where the
[06:08] desktop app makes sense because then you
[06:09] can make multiple folders and you can
[06:11] chat with either right you can have an
[06:13] email marketing thread go at the same
[06:15] time as a support one etc and they all
[06:17] run within their different folders. So
[06:19] if you
[06:19] >> I don't quite understand. And do you
[06:20] want to show us that though cuz I can
[06:22] only understand that.
[06:23] >> I don't really have the same job as you.
[06:25] So I don't have as many folders and
[06:26] levels but like for example this is my
[06:29] code desktop app right and you can see
[06:31] that for example I have the website
[06:33] folder here and I have like my prompting
[06:34] L which is like my historical catch all
[06:37] thing and this is my project for my
[06:39] tasks on notion that I shared on another
[06:42] podcast. Right. So if I wanted I could
[06:44] like start a new task on the website. So
[06:46] I could say change the H1 on homepage to
[06:51] and let me switch to office 4.7
[06:54] uh and then to hello Mark. Uh don't
[06:57] worry I'm not going to commit this but
[06:59] the point is like I can launch this task
[07:00] and then I can start another thread on
[07:02] prompting lab and I can say prepare a
[07:06] newsletter sharing the updates at Google
[07:10] IO yesterday and it's going to call the
[07:13] right scale etc. The point is now I have
[07:16] a thread going on in my prompting light
[07:18] folder.
[07:18] >> How does it know which one to use?
[07:21] >> The way it works is when you make a new
[07:22] session here, you can pick a folder.
[07:25] >> Okay, so you pick each
[07:26] >> and then you can order you can
[07:29] essentially group by project. And what
[07:31] that does is it just basically creates
[07:32] these groups per project. And so you are
[07:34] able to create smaller folders that
[07:36] contain more specific thing and then
[07:38] each one can have its own code MD can
[07:40] have all of that etc. And then the idea
[07:42] is you can just launch
[07:44] >> as many as you want in different
[07:46] folders, but that still operates within
[07:47] one interface and that's kind of nice.
[07:49] Basically,
[07:49] >> that interface. Yeah, I like that a lot.
[07:52] Yeah.
[07:52] >> So, do you see do you see the value now
[07:54] when you connect the different folders,
[07:55] etc. And so, you'll be able to be a
[07:57] little bit more granular and then you'll
[07:58] be able to spend more time on your code
[08:00] MD for things that matter and then you
[08:02] can still reference files outside the
[08:03] folder like CL will still be able to go
[08:05] outside the folder and you could have
[08:06] like a common ground place where you
[08:08] have some context that it reads
[08:09] basically, right? So yeah, that's pretty
[08:12] much uh that's pretty much why I think
[08:14] this is good.
[08:15] >> What desktop app? Can I just ask cuz
[08:17] like when it launched it wasn't very
[08:19] good at it your files like
[08:22] >> there's two ways to do that. So
[08:24] basically the first one is you can
[08:25] actually click on files here and then
[08:26] you can see your files. So I have a
[08:28] little bit of mess. Don't be mad. But
[08:30] like you have this basic file reader
[08:32] which is like okay but not great. But
[08:34] the point is let's say you want to go
[08:35] deeper. You want a better uh file
[08:37] editor, right? You can always rightclick
[08:39] here and open in VS Code. And what that
[08:42] does is this opens a new window of VS
[08:44] Code exactly in that folder and you can
[08:47] resume that thread if you want to. And
[08:49] then you basically are working in the
[08:51] same folder because remember whether you
[08:53] walk in VS Code or you walk in the CL
[08:55] code app as long as it's working within
[08:57] the same folder is the same thing,
[08:58] right? It's like it's not a client that
[09:00] matters. That's a really important thing
[09:02] because one of the questions we get
[09:04] asked a lot and like to be honest I was
[09:07] asking that question in the beginning is
[09:08] like which should I use VS code or
[09:10] >> you don't have to choose yeah
[09:11] >> cloud code or even like if you're
[09:12] looking something like using codecs from
[09:14] open AI it's different system but
[09:16] >> you're not really locked in in the same
[09:18] way cuz what you're saying is like all
[09:20] the files and folders are local so you
[09:22] just use them in a different app
[09:24] >> and the point is that the way I would
[09:26] say for most people it's easier is now
[09:27] to kind of connect all your folders to
[09:29] the cloud desktop app start here And
[09:31] you're like, well, you know what? Like,
[09:32] let's say I wrote me a newsletter. It's
[09:33] not finished now. It's working. But
[09:34] let's say I wrote a newsletter and I'm
[09:36] like, oh, I want to have the thing where
[09:37] I can highlight text. It is what I
[09:39] highlight. I can give feedback, etc.
[09:40] Well, no problem. Right click, open in
[09:42] VS Code. And then I can resume the same
[09:44] chat in the VS Code extension like by
[09:47] going to the chat history and it will
[09:49] show there because it's in the same
[09:50] folder. And then I can just open the
[09:52] markdown file and just start
[09:54] highlighting text and just commenting on
[09:56] this. And when I'm done, I close VS Code
[09:57] and I resume back here. And that chat is
[09:59] also updated because it's the same chat.
[10:01] Right.
[10:02] >> Right. Okay. So, yeah, I'm thinking how
[10:05] I would use this then for my work. Like
[10:07] would you go granular? Like would you
[10:09] have you know a podcast folder, an email
[10:12] folder or would you have like one level
[10:14] up like a marketing folder?
[10:15] >> Probably a marketing folder. Probably I
[10:17] would do a marketing one, a support one.
[10:19] I you see that even with all your stuff
[10:20] it's still decent at dealing with it. So
[10:22] it's like if you keep things like as
[10:24] broad areas of interest, I think that's
[10:26] fine. Even if you have a small business,
[10:28] like it can still be okay to do
[10:29] everything within one folder, but like
[10:31] the point is as context grows, this
[10:32] becomes a problem. And so you kind of
[10:34] need to kind of address, but it's not
[10:35] really a problem because you know how we
[10:37] teach people to have these areas, right?
[10:39] Like you showed. Well, you can
[10:40] essentially just branch them off as
[10:42] their own folder or even just not even
[10:44] move them. You can literally just open
[10:45] them as a folder. So you just make a
[10:48] thing and instead of opening prompting
[10:50] lab here I can just open uh if I go in
[10:53] code uh let's go prompting lab and then
[10:56] I could go into an area for example uh
[10:59] and then I could open let's say website
[11:01] or social content and boom that becomes
[11:03] a new folder that runs even though it's
[11:05] a subfolder and then yeah and that was
[11:07] what I thought I was doing initially in
[11:10] VS Code
[11:11] >> but now you can do it within one window.
[11:13] >> Yeah, exactly. because what happened in
[11:14] reality was I just I was too lazy to go
[11:17] file open and you know
[11:18] >> and have like many windows at the same
[11:20] time it's confusing and you have to alab
[11:22] etc. So that simplifies everything and
[11:24] that's the idea and then you can have a
[11:25] CL MD that goes live in that social
[11:27] folder and boom it can use that context
[11:30] directly and so that's why I kind of
[11:32] like the idea of like you can start here
[11:33] you right click you open it you go I
[11:35] mean you see I have many code editors
[11:36] but if you just have VS code it you just
[11:38] show VS code and then you pick that one
[11:39] and it will just you you find your same
[11:41] setup and you can resume the chat that
[11:43] was running in the cloud app and that's
[11:45] kind of the beauty of the ecosystem is
[11:47] it's folder based and so the chat
[11:49] history is also folder based which means
[11:51] that it will actually work in VS Code.
[11:54] >> Yeah. Okay. So, I mean action for me
[11:56] after we finish recording [laughter]
[11:57] this is like I don't actually think I
[11:59] need to create new folders. I think I
[12:00] just sub folders but I if I use them to
[12:03] the cloud app that's going to give me a
[12:05] nicer easier to use interface in order
[12:07] to access them. And to be honest with
[12:09] you, for a lot of those tasks, I'm
[12:11] thinking, you know, podcast one, there's
[12:13] a lot of image generation and for
[12:15] thumbnails, it's nicer to use the claw
[12:18] app because it fully renders like in the
[12:20] chat flow the images, whereas VS Code,
[12:22] you kind of you can still open it in
[12:23] there, but you have to kind of click to
[12:25] open it and it's it's not not as smooth
[12:27] not as smooth of an experience.
[12:28] >> I agree. So let's say for example like
[12:30] you have this view that you can select
[12:32] here in diff and diff basically shows
[12:34] you what the agent removed or updated on
[12:37] the file right um so let's say created a
[12:39] file you
[12:40] >> does that mean stupid question does that
[12:42] mean yes it [laughter]
[12:45] >> and the point is like you know how on vs
[12:47] code you can highlight the text and you
[12:49] can comment and it's kind of missing in
[12:50] the desktop app but the thing what you
[12:52] can do is you can open one of these divs
[12:53] and you can start selecting the text
[12:55] like that by clicking on this plus thing
[12:56] and then dragging down and then you have
[12:58] this comment thing and you can just say
[12:59] like let's imagine this is actual copy
[13:01] you can say make it shorter for example
[13:03] and what that does is it starts creating
[13:05] these comments and you can have multiple
[13:06] of them right so you can just pick that
[13:08] and you can pick this and say like make
[13:10] it longer and then you can just go
[13:13] through all your comments comments
[13:14] >> and then you just send it and it will
[13:16] just process them
[13:18] >> so you can that's quite nice like
[13:21] honestly even just having like the green
[13:22] and red highlight like the old and the
[13:24] new like it's much nicer than the way it
[13:27] work it's just that's displayed in VS
[13:29] Code.
[13:30] >> Yeah. So, it's like you can do that.
[13:31] It's not perfect, but it's one way you
[13:33] can do that. So, it's kind of like you
[13:34] either open the markdown file in fire
[13:36] and it's like you can't really do
[13:37] anything or you open the diff and then
[13:38] you can do that and you can just cue
[13:39] your comments like a Google doc.
[13:41] >> But if you let's say create a newsletter
[13:44] for example, then it's kind of nice. You
[13:46] get like basically you get a full green
[13:48] new file like new markdown file created
[13:49] and you can go and comment on each line
[13:51] and drop your comments. It will just
[13:53] know what to do and do it basically. Um,
[13:56] so you get the idea. Like that's how it
[13:58] works. So yeah, that's pretty much how
[13:59] it works and it's a good starting point.
[14:01] I think there's still things missing in
[14:02] the desktop app, but it's kind of nice
[14:04] when you kind of like run it like that.
[14:06] Like you remove everything and it's like
[14:07] literally you just have this one thing
[14:08] and you can just go on the side and see
[14:10] all your threads here basically. Like
[14:11] it's very simple.
[14:13] >> I really can't emphasize enough like for
[14:15] me in this position like there is no
[14:17] downside to use like I have them both
[14:19] open right now. They're both accessed in
[14:21] the same folder. like it's not like a
[14:24] one-way door type decision that you're
[14:26] locking yourself into one app or one
[14:28] ecosystem.
[14:29] >> Yeah, you can just start on the desktop
[14:31] and then just jump onto the text editor
[14:33] only when you need the complexity and
[14:35] the advanced text editing features of
[14:36] it. That's kind of the beauty. So, let's
[14:38] go back to your setup and keep going.
[14:40] >> So, I mean, I've got my claw.md file
[14:43] open here. Do you want to have a look
[14:45] through that and tell me uh if I'm I'm
[14:47] setting this up correctly? So it's I I'm
[14:50] thinking or I was told somewhere
[14:52] probably by you like try and keep it as
[14:54] short as possible because this is the
[14:56] this file is sent secretly like in the
[14:59] background of every single chat I'm
[15:01] sending to provide context to
[15:03] >> Claude. So I have couple sentences about
[15:06] what our business does, you me our
[15:08] product, who the key people are a little
[15:11] bit like about a brand voice just avoid
[15:14] you know cheesy words like be practical
[15:17] uh that kind of thing. my never use m
[15:19] dashes
[15:21] >> writing style is just don't use m dashes
[15:22] [laughter]
[15:23] >> honestly this works like I don't know
[15:26] how but like it knows the writing style
[15:28] it gets it and it's never uses m dash
[15:30] >> I'll show you a better way
[15:32] >> okay I've then [snorts] got my directory
[15:34] structure so on my left here I've got
[15:36] you know the projects folder the dump
[15:38] where I'm you know
[15:39] >> dragging and dropping in files to work
[15:40] with I've got my areas and I got data uh
[15:44] which I've started populating but I
[15:45] haven't really kind of like solved this
[15:47] data uh thing. My idea was have you know
[15:50] like all of our podcast transcripts or
[15:53] you know data uh things like design for
[15:56] the website like all of our logos icons
[15:58] are here or photos of you and me that we
[16:01] use regularly across thumbnails and
[16:02] different things. I wanted to have them
[16:04] all there so they're in an easy to find
[16:06] place that I have in my cloud. MV file
[16:08] the MCP servers which I have access to.
[16:11] So I mean initially it just you know I
[16:13] was asked it to interview me and it kind
[16:15] of created a few of these. You can see
[16:17] here, for example, the meta ads one
[16:19] where I've added this later and I've
[16:21] just told it, hey, go update my claw.md
[16:23] file and it's written to be honest, I
[16:25] think more than it needs to have in in
[16:27] here.
[16:27] >> Yeah, because I was going to say the MCP
[16:29] servers, they already loaded in context
[16:31] as well or somehow like and so like I
[16:35] think what would be more interesting is
[16:36] like when you wanted to use these tools.
[16:39] Okay. Um, so it's like it because like
[16:41] it kind of it can discover what these
[16:44] tools are and what they do quite easily.
[16:46] Like it's in the description of the
[16:47] tools, but however, it doesn't know when
[16:48] and how you want to use them. And so
[16:50] like that's kind of the context that's
[16:51] interesting. It's like ah like use
[16:53] notion when we want to save some notes
[16:54] and use bento when we want to email our
[16:57] subscribers that are not necessarily uh
[16:59] customers for example like you know that
[17:01] kind of stuff is not baked into the tool
[17:03] description. It's interesting
[17:05] >> but explaining that Bento is email
[17:07] marketing is not needed. It knows what
[17:08] it knows what it is.
[17:10] >> Okay.
[17:10] >> Because you're connected to the MCP.
[17:12] >> I still I find myself like a you know a
[17:14] boomer. I'm still like really directing
[17:16] it quite closely like use the Bento MCP
[17:19] to upload this email rather like I don't
[17:23] upload this. Yeah.
[17:24] >> Because you have not inferred in the
[17:26] content that like hey when we send
[17:27] newsletter we send it to Bento for
[17:29] example. And so that is not in the
[17:30] context and if it was baked in then you
[17:32] would not need to babysit it as much
[17:34] because it would infer it right. Um and
[17:36] so so it's more like it's still
[17:39] interesting to describe the tools you
[17:40] have but in a different way not what
[17:41] they do but like when they are relevant
[17:43] and who like you know who uses them in
[17:46] what context etc.
[17:47] >> Um so
[17:48] >> that's useful
[17:49] >> and then the last section is my area
[17:51] context which is just like here's all
[17:53] the different areas you had. Yeah.
[17:56] >> Yeah. Different other cloud MDs. Yeah.
[17:57] And then specifically like we had this
[17:59] marketing strategy one cuz I'm doing a
[18:01] lot of marketing stuff. It refers back
[18:03] to that I think quite frequently.
[18:05] >> Yeah. Um, just for things like, you
[18:06] know, what's the price point of our
[18:08] product, who's our uh, you know,
[18:11] things like that. How do you
[18:12] >> how does to be honest with you, it's
[18:14] been a while since I updated, but it
[18:16] hasn't changed like a [snorts] lot in
[18:17] the last six weeks or so. So,
[18:19] >> all right. Like this is okay, but like
[18:22] you it's still not a lot of context
[18:24] basically. So, yeah, the question is
[18:26] like how do we give more context without
[18:28] bloating the code, right?
[18:30] >> I know the answer to this. Yeah,
[18:32] >> it's progressive disclosure which is you
[18:34] have another markdown file which is
[18:36] linked to from your cloud.md file. So
[18:39] when it needs to it can go there, right?
[18:41] >> So so how
[18:42] >> which is kind of what I tried to do with
[18:43] area context. But
[18:45] >> so there's two problems. One it's like
[18:46] for example the writing style etc. You
[18:48] need to write a lot more about like how
[18:50] you like things written the context of
[18:52] the company as well. We need to give a
[18:53] lot more context. Who is the target
[18:55] customer? That would be very handy to
[18:56] have it. So it's like what you're
[18:58] missing is you're missing a
[18:59] documentation folder or some kind of
[19:00] like wiki that cloud maintains itself.
[19:03] Um and so what you need to go ahead and
[19:06] do is be like hey like we're not going
[19:07] to put everything inside the cloud MD
[19:09] but we're going to link to documentation
[19:12] files that it can go read when it needs.
[19:14] So it's like hey if we're working on
[19:15] something that reaches the audience go
[19:17] read the file that describes what the
[19:18] audience is but it will not read it when
[19:20] you do something else. Right? If we go
[19:22] if we write some copy, just go read that
[19:24] guide on like what our voice is with the
[19:26] examples and everything. And again, it
[19:28] can be a quite decently big markdown
[19:30] file, but it will not be read when
[19:31] you're doing something else like support
[19:33] or something.
[19:34] >> My idea for that was to kind of put that
[19:36] in the data folder and kind of reference
[19:39] that there. I don't know if that's the
[19:40] best place for
[19:41] >> but there's another part that you're
[19:42] missing in this is like, okay, the
[19:44] documentation folder matters, but the
[19:45] problem is you told me it's not updated,
[19:47] right? You haven't updated the marketing
[19:48] strategy, etc. So what you need to say
[19:50] in the cloud MD is rules. It's like,
[19:52] hey, every time something new comes up
[19:54] that is different from what you've read
[19:56] in the documentation as you did the
[19:58] task, offer to update the documentation.
[20:00] And so what's going to happen when you
[20:03] finish a test, be like, hey, I noticed
[20:04] that we did this thing and it's
[20:05] different from what I read in the file
[20:07] when I was doing the task. Do you want
[20:09] me to update it? And you'll say yes. And
[20:11] it will just go ahead and update your
[20:12] documentation and your context going to
[20:14] keep updating with minimal work on your
[20:16] end basically.
[20:17] >> Okay. Yeah, that would be super useful
[20:19] cuz I mean I was thinking like it would
[20:21] update it automatically and I would be
[20:23] like I didn't want that to happen in
[20:25] case it like you know goes a bit rogue
[20:26] and updates in a way I don't want. Uh
[20:29] but that's yeah
[20:30] >> yeah you just say you proactively offer
[20:32] to update the documentation and it will
[20:34] just and you tell which file you're
[20:35] targeting and what you're going to
[20:36] change and at the end of a task when you
[20:37] say something like hey you know I was
[20:38] reading this file because the code MD
[20:40] told me to read it and now we say the
[20:42] price is this much when actually my
[20:44] documentation said it's this much should
[20:46] we update the price on the documentation
[20:47] you say yes and we just go boom and just
[20:49] go update all the files basically
[20:51] >> and so you kind of want it to maintain
[20:53] its own mini wiki like that and you want
[20:56] it to take care of it because The
[20:58] problem with documentation is always
[21:00] outdated and it's not going to be
[21:01] perfect, right? Like sometimes you'll
[21:02] need to have a bit of a bass etc on
[21:04] cleaning things up, but it's going to
[21:05] help a lot in not because the problem is
[21:09] probably inside your folder now you have
[21:10] a lot of stuff that's getting older now
[21:12] >> and then as it's getting older the
[21:14] quality of what you get is going to drop
[21:17] because it's going to be outdated.
[21:19] >> So you need to update your CL you need
[21:21] to make a documentation folder. So like
[21:22] literally make a new chat at some point
[21:24] be like hey we're making a mini wiki
[21:25] that's just for you. uh make sure you
[21:27] update your code MD that you know that
[21:28] and then let's kind of like you know try
[21:31] to go through the workspace and try to
[21:33] build this wiki based on what we have
[21:34] and build it together spend half an hour
[21:37] doing that and then update your code MD
[21:38] pointing at each documentation file and
[21:40] then change the code MD to tell it to
[21:42] update things
[21:43] >> I'm thinking that principle of asking it
[21:46] to prompt me to if it wants to update
[21:49] things can be applied in other areas as
[21:51] well so for example uh like any task I'm
[21:53] running regularly specifically I'm
[21:55] thinking like uh create things, email
[21:57] marketing and podcast publishing,
[21:59] especially like thumbnails, titles, that
[22:01] kind of thing. It can kind of update its
[22:03] skill prompt if you want to update the
[22:05] skill based on what I've changed or
[22:07] something like that rather than cuz when
[22:09] it doesn't prompt me, I'm like, "Oh,
[22:11] I'll figure it out next week or
[22:13] something." And I I never go back and
[22:14] update. Just
[22:15] >> the way you do it is like you kind of
[22:17] need to give a clear signal that the
[22:18] task is done. Let's say you worked on
[22:19] the newsletter and it's like you get a
[22:21] you're like, "Okay, we're done now." and
[22:23] you say, "Hey, when you were done and
[22:25] we've just run the skill, you review the
[22:27] chat and then you review the skill and
[22:30] you propose edits to the skill that
[22:32] match the specific use cases." And so
[22:34] then the only thing you need to say is
[22:35] like we're done and then it will know to
[22:38] do this process when you say we're done.
[22:40] You know,
[22:41] >> even that I think I would probably
[22:42] wouldn't do all the time. I might have
[22:45] it ask me are you happy now that we're
[22:47] done? And then like it will look for
[22:49] that like trigger before it then does
[22:51] that prompt or something like that. But
[22:52] the point is like you just need to
[22:53] signal that this is the final version of
[22:55] the task because otherwise it might
[22:57] think you're iterating again and so it
[22:59] will not know when to trigger that. But
[23:02] yeah, that's kind of like a flow that
[23:03] you can have and it's just minimal work
[23:05] as well. And you can see how the goal is
[23:07] to kind of like offload all the tedious
[23:08] stuff to the model and have it do it
[23:11] rather than do it yourself. So it's like
[23:13] a thing that I have with a lot of people
[23:15] I talk to is like instead of putting
[23:17] just context in your cloud MD, you kind
[23:19] of want to put rules, rules that build
[23:21] context basically and you go one level
[23:23] of abstraction up and you just tell it
[23:24] how to maintain its own context. So
[23:27] that's in my opinion that's kind of like
[23:29] one of the biggest ones for you is like
[23:31] I would do that actually. One thing that
[23:32] you can do as well is you can add some
[23:34] rules that kind of like offset the
[23:36] weaknesses of the models. So did this
[23:39] happen to you for example that sometimes
[23:40] you're talking to cloud code and it's
[23:41] like ah go and type this in your
[23:43] terminal or like you should go and copy
[23:45] paste this in this file etc where you
[23:47] can tell it can clearly do it right
[23:49] >> always and I just replied do it yourself
[23:51] yeah
[23:52] >> so again these are the kind of rules you
[23:54] probably want to put in your club MD
[23:56] which is like if you can do the thing
[23:58] don't ask me do it [laughter] and it's
[24:01] like that's the kind of rules that I
[24:02] like to put in there same I always tell
[24:04] it to always verify and correct its work
[24:06] so after it's done with the task, it
[24:08] should review it and then apply fixes if
[24:10] it needs to apply fixes. It sounds
[24:11] obvious, but like you kind of reinforce
[24:14] these behaviors by putting these
[24:15] oneliners into your CLMD. So I have
[24:17] these kind of like workflow rules. And
[24:19] so like find all the annoying things
[24:20] that happen in terms of the workflow
[24:22] that you have with cloud and that's what
[24:24] your cloud is for is just putting some
[24:26] kind of like highle workflow rules. So
[24:28] one thing as well that happens quite
[24:30] often is you know I dictate my prompts
[24:32] and opus 4.7 likes to take things very
[24:35] literally and so like it just does what
[24:37] you say nothing more nothing less and so
[24:40] I have instructions to tell it to infer
[24:42] the meaning of my prompt and kind of go
[24:45] beyond what I just said to behave a
[24:47] little bit more like opus 4.6 six for
[24:49] example, right? And then if it's not
[24:50] sure to ask me and to use the question
[24:52] tool and so find the things that
[24:55] irritate you with your workflows or that
[24:57] makes it stop when it shouldn't and put
[25:00] very highle prompts to tell it not to do
[25:03] that basically and that that will make
[25:05] your experience significantly better.
[25:08] >> Okay, great. All right, let's talk about
[25:10] skills now. So for those who don't know,
[25:12] scales are basically saved workflows as
[25:14] a mix of markdown and scripts that allow
[25:17] you to repeat the same workflow and to
[25:19] document it in great details so that you
[25:22] can get a consistent output every time.
[25:24] So you can see that this leaves under
[25:25] the dotcloth folder on Mark's computer
[25:27] under the skills subfolder and then
[25:29] below that then you have a folder for
[25:31] each skill and then if you open one of
[25:33] them you'll see you have at least a
[25:34] skill.md and you could have other
[25:35] folders basically. Uh yep. So scale.m MD
[25:39] is the kind of like trunk of the
[25:41] workflow that gives the steps to follow
[25:44] and potentially links to other
[25:45] documentation. Again, progressive
[25:46] disclosure. So you give the high level
[25:48] against goes and read some documentation
[25:51] when it needs if it needs to and the
[25:53] model decides. So let's talk about some
[25:55] of the skills you use and see how do you
[25:56] use them.
[25:57] >> Okay. So, I mean the most complex skill
[26:00] I would say I use is the podcast
[26:03] publishing one um where I'm analyzing
[26:06] the transcript of this and I'll be doing
[26:08] this after our call or our recording.
[26:11] Then it's generating a number of
[26:15] thumbnails, YouTube thumbnails, as well
[26:16] as like title ideas and stuff. It's a
[26:19] bit back and forth process there to kind
[26:21] of get something that that fits. Like
[26:23] it's not fully automated. I still need
[26:25] to kind of guide it and steer it a bit.
[26:26] Why do you have to g it? Like what do
[26:28] you have to get about it?
[26:29] >> It's just I mean it doesn't hit it
[26:31] doesn't give me three perfect ideas
[26:33] every time. Like I have it give me 10
[26:35] ideas and then I select three that I
[26:38] think are going to work better cuz some
[26:39] of them are like
[26:40] >> I agree. This is the kind of stuff where
[26:42] like you still need some kind of human
[26:44] taste and you could improve it but I
[26:45] don't think you could make it perfect
[26:47] basically. Uh so it's like fair. It's
[26:49] not
[26:50] >> you know the single biggest thing that
[26:52] improved that was switching from nano
[26:54] banana uh image model GPT images too
[26:58] like it's completely transformed it so
[27:01] >> it's a good model GP images like very
[27:03] very bullish on that model yeah if there
[27:04] was a way to upload that to YouTube to
[27:06] get to upload to YouTube that would be
[27:08] amazing but I don't think there is I was
[27:09] just thinking of the email broadcast one
[27:11] which I got open actually so if you want
[27:13] to do a promo for you know a new skill
[27:16] that we've released inside AI
[27:17] accelerator or a new course or thing.
[27:19] Um, I often use this and it will write
[27:22] it plus uh upload the email to Bento,
[27:25] which our email tool as a draft ready to
[27:28] send. There's a few quirks like it
[27:30] doesn't do the preheader text and things
[27:32] like that, but it does save some copy
[27:34] pasting.
[27:35] >> Why doesn't it do the preheader text?
[27:37] >> Don't think it's possible in Bento to do
[27:39] the preheader text. So, I edited the
[27:41] skill.
[27:42] >> I don't have one open actually, but it
[27:44] maybe this one this one has it.
[27:47] No, I don't think so. So, I edited the
[27:49] skill where it will give me all this,
[27:52] you know, say, "Hey, I've uploaded this
[27:53] and then it'll like give me the text to
[27:56] copy paste into the preheader." So,
[27:58] >> not too bad.
[28:00] >> Uh, and so what's frustrating you with
[28:02] these scales? Like, do you think it
[28:03] could be better? Is there anything that
[28:04] you still do manually that could be
[28:05] automated?
[28:06] >> So, the what's happened is like the
[28:09] processes which I run, you know, every
[28:11] week are pretty decent, I would say. you
[28:14] know there's minimal copy pasting what's
[28:17] happening though is there's a lot of
[28:18] like kind of small you know oh it only
[28:21] takes five minutes type tasks which I do
[28:24] which I'm automating parts of in clawed
[28:26] code but I still end up copy pasting a
[28:28] bunch of stuff and my barrier is really
[28:30] the setup the integration setup with all
[28:33] the tools it's like ah it's going to
[28:35] take me half an hour to figure out how
[28:37] to connect my Google uh so here's a good
[28:39] example we have a group right and it's
[28:44] for our plus members only. And so people
[28:46] have to apply to join that. Um, and I
[28:49] have to manually invite them to
[28:50] WhatsApp. Like there's no way around
[28:51] that at the moment. When they update
[28:54] their WhatsApp number, I get a
[28:56] notification. It saves it in a sheet.
[28:58] And then this is able to because I've
[29:00] connected Google Sheets into Claude
[29:03] through the desktop app.
[29:05] >> Yeah, it's much easier.
[29:06] >> It can only read. It can't write. So it
[29:10] can read the circle ID and check if they
[29:13] have access and it can give me the name
[29:15] and the email from the circle ID. Um and
[29:18] I can say okay yeah this
[29:19] >> but you cannot update the spreadsheet
[29:20] saying you processed it right.
[29:22] >> Yeah. So at the end I have to just go
[29:24] copy paste that manually and it's like
[29:26] yeah again it takes 5 seconds 20 seconds
[29:30] each time I do it. But you know it's one
[29:32] of those things that
[29:33] >> so this one is particularly annoying
[29:36] because Google sucks at making these
[29:39] APIs easy to access. If you've never
[29:41] done it it's done through the Google
[29:43] Cloud Console which is kind of like the
[29:44] enterprise API type stuff. And that's
[29:47] kind of the only way to have read and
[29:49] write access to a lot of the tools. you
[29:51] can get access to your entire Google
[29:53] workspace which is awesome. Uh and then
[29:55] if you connect it through the Google
[29:57] Workspace skill workspace skills sorry
[30:00] then it's really quite powerful
[30:01] actually. You can really do a lot with
[30:03] this but it's it's like a 15step process
[30:07] of a confusing dashboard to click around
[30:10] download some JSON files and then link
[30:12] to them. It's very complicated.
[30:13] >> I think what's happened as well is
[30:15] they've obviously changed the like menu
[30:17] layouts over time. So whenever you ask
[30:20] AI what to do it's like oh click on um
[30:23] you know this doesn't exist
[30:25] >> you know there's a solution right which
[30:26] is there's actually CLI which is short
[30:29] for common line interface which is
[30:32] essentially a terminal tool that allows
[30:34] cloud or codeex to operate the cloud
[30:38] console like the confusing dashboard and
[30:40] so it can go do most of the work for
[30:42] you. So if you actually connected the
[30:44] Google cloud console and then you just
[30:46] need to authenticate right with your
[30:47] account and just give it full access and
[30:49] then you can just tell it hey I want to
[30:52] like create a new API key you know for
[30:55] this thing uh to connect it and then
[30:57] it's going to do most of the work and
[30:59] it's just going to give you a URL to
[31:00] click on and then you're just I need to
[31:02] download this JSON file that they
[31:03] require and just tell it where it is
[31:05] basically you know copy the path or even
[31:07] drag and drop it into your code
[31:08] basically and that's the only thing that
[31:11] you will have left to do manually. Cloud
[31:14] can do all the API setups for you and
[31:17] you can do all of that. So it's like the
[31:19] high
[31:19] >> like first of all u can we just talk
[31:21] about what a CLI is compared to an MCP
[31:24] like it's essentially like if you don't
[31:26] care about the technicalities they both
[31:28] let you access all of functionality of a
[31:32] system.
[31:32] >> Yeah. But CLI is like better or more
[31:35] efficient in some way.
[31:37] >> Yeah. It's a terminal tool. It's meant
[31:38] for humans in principle but just agents
[31:40] are very good at using it. they're very
[31:41] good at terminal and so you can connect
[31:43] that you can authenticate yourself and
[31:45] then anytime you need an API from Google
[31:47] you can just say hey can you add the API
[31:50] to my project and it will just do it um
[31:53] so this goes 15 minutes
[31:55] >> this goes on to my next yeah that's my
[31:57] next question is like is that a bollig
[31:59] to set up
[32:00] >> it's a 10 to 15 minutes and there's
[32:02] literally two pages to open rather than
[32:05] 15 to 25 with the manual setup
[32:08] [laughter]
[32:09] so that's the solution and then you can
[32:11] update your skill to update your
[32:13] spreadsheet so you don't have to go and
[32:14] open it and mark everyone who has added.
[32:16] If you use the code desktop app, uh you
[32:20] could have it use computer use and add
[32:22] people through the WhatsApp app if you
[32:24] want. So you can take over your mouse
[32:26] and go and add people as well if you
[32:28] want. Uh not super super clean. The
[32:30] computer usage is like mediocre I would
[32:32] say with cloud but potentially you could
[32:34] launch that, go for lunch, come back and
[32:36] it's done or it deleted everything. But
[32:38] yeah. Yeah, I haven't been impressed
[32:39] with computer use. I mean, I haven't
[32:41] used it recently on Claude, but you
[32:43] know, 3 4 months ago, like it was it
[32:46] just was super slow to do anything. So,
[32:48] if I'm at my computer, it's it's not
[32:51] speeding anything up,
[32:52] >> especially
[32:54] when we first launched there was like 50
[32:56] people to add or something, but now,
[32:58] >> you know, it's like one every couple,
[33:00] >> but that spreadsheet should update
[33:01] itself. Like, that's not good.
[33:03] >> Yeah. Yeah, definitely.
[33:04] >> Any any other skill you want to show?
[33:06] >> Yeah. Yeah. So I have this skill which
[33:08] does plus member application. So when
[33:11] before people join AI accelerator plus
[33:14] uh we screen everyone and they fill in a
[33:18] form on our website and then uh I get
[33:20] the application and
[33:22] >> at a time of my choosing so not
[33:24] automatically I'll go through and review
[33:27] them.
[33:28] >> And so I I have a skill I type slash
[33:31] plus applications.
[33:33] >> What was happening
[33:34] >> as well? Why did you have
[33:35] >> what was happening is it worked seemed
[33:38] to work quite well initially but I don't
[33:39] know if the notion CRM thing that we
[33:42] built started getting lots and lots of
[33:43] names on it or something but it would do
[33:46] like plus applications and it's supposed
[33:47] to look for you know new or not
[33:49] processed whatever the initial um
[33:51] category is
[33:52] >> and even if there's like two people in
[33:54] there it would be like searching through
[33:56] like all the other name you know spend
[33:58] like really a long time just trying to
[33:59] try trying to find
[34:01] >> people so I'm using the notion MCP I
[34:04] think I can't even remember when I think
[34:06] I set that up in the cloud.
[34:07] >> The desktop app I can see because if it
[34:09] says cloud AI then this is the desktop
[34:12] app. So you can see in your tool calls
[34:13] it says clude AI which means yeah that's
[34:16] good. That's good to know cuz like one
[34:17] thing I did wonder is like how the hell
[34:19] does have access to my notion because I
[34:20] didn't remember setting that up in VS
[34:22] Code. If you also do type SLMCP, it will
[34:24] show you which ones are connected
[34:26] through the notion app. And no, if you
[34:28] type just in in the Yeah. / just type
[34:32] Yeah. Search MCP MCP servers.
[34:34] >> Press enter.
[34:35] >> And you can see see local cloud AI etc.
[34:39] You can see which ones are connected.
[34:40] Cloud AI is the desktop remember.
[34:43] >> Yeah.
[34:43] >> So you can see what is connected
[34:44] through. And then you can see your Gmail
[34:46] is connected, your calendar is
[34:47] disconnected and stripe is disconnected.
[34:49] Uh and you have circle twice I think.
[34:52] No, you only have it once. Sorry. But
[34:53] it's disconnected.
[34:54] >> No, no, it's twice. Oh, you have it
[34:55] >> twice and Okay. So again, context
[34:59] optimization if you wanted to. So let's
[35:00] go back to the notion workflow. So I
[35:03] think yeah, you have a scale problem.
[35:04] First of all, like the fact that you
[35:05] cannot find the pending stuff, I guess
[35:07] it's either an MCP program or skip
[35:08] program, but I can see the return is
[35:10] like this heavy JSON basically like I
[35:12] can see I can see the tool. So I don't
[35:16] use the notion MCP. I use the notion CLI
[35:19] again. And what's really cool is it it's
[35:22] more efficient basically it just gives
[35:23] less big payloads to the agent and same
[35:27] for pages right when it reads a page it
[35:29] you know notion has all this formatting
[35:31] etc that ends up being just lots of
[35:33] characters to express that but it now
[35:36] gives the content of a page in markdown
[35:38] for example when the agent goes so it's
[35:40] very very efficient it's almost as if
[35:41] you had local markdown files but it's
[35:43] kind of nice on notion so it's the ntn
[35:46] the ntn extension so that's why it's
[35:48] called the ntn cli Okay. N so sorry N
[35:51] like the letter N TN
[35:53] >> TN cla
[35:54] >> okay
[35:56] >> and uh if you search for that you'll
[35:58] find it and it's it's very good
[36:00] basically um so you install it you
[36:03] activate it it's already activated on
[36:04] our workspace and you give it access to
[36:06] things and you remove the notion MCP
[36:09] otherwise it's going to default to that
[36:11] >> okay
[36:11] >> and then you tell it in your cloud MD be
[36:13] like hey when you track with notion use
[36:15] the NTN CLI for example
[36:17] >> so question for you this because I'm
[36:19] going to be using uh the cloud desktop
[36:22] app quite a lot more now after this
[36:24] conversation.
[36:24] >> You can still do that.
[36:25] >> Should should I be setting up does it
[36:27] matter where I set the MCPS up? Like do
[36:30] they need to be in you know the claw.ai?
[36:32] >> It works anyway. So the desktop app it's
[36:35] the same like you can see how your
[36:36] desktop app MCPS are showing up in your
[36:38] VS code right now.
[36:40] >> Yeah.
[36:40] >> And vice versa. If you have a C MCP
[36:43] setup in the folder that you're working
[36:44] it's going to read that file and also
[36:46] use that. Um, so that's why it's really
[36:48] interchangeable completely and it's like
[36:50] there's no issue with switching. So
[36:53] yeah, set that one up and I guess it's
[36:55] like you need to make it sure that it
[36:56] reads the statuses properly. So what
[36:58] does it do? It gets the data. Then what
[37:00] >> it gets the data and then we go through
[37:02] this process. It makes a recommendation
[37:05] about like uh you know should we approve
[37:07] this person, get a call, ask for more
[37:10] information? How does it do that?
[37:12] >> I can't even remember. So I mean what
[37:14] happens here? Uh I mean it's a very
[37:16] simple skill. It's just a skill.md file,
[37:18] right? Um okay.
[37:20] >> And we automatically enrich the
[37:22] application with data inside notion. So
[37:25] when it pulls the notion page, it's
[37:27] pulling the context of the application
[37:31] plus
[37:32] >> what AI has already found out through
[37:34] its research and its assessment. Right?
[37:37] So there's that that assessment, but
[37:39] it's never automatically approving
[37:41] someone or anything like that. It's just
[37:42] presenting it. And honestly, mostly it's
[37:45] kind of like my read on this person like
[37:48] how we want to proceed.
[37:49] >> How does AI enrich the lead?
[37:52] >> I don't know. You set that up.
[37:54] [laughter]
[37:54] >> Ah, it's my workflow then. It's just
[37:57] it's a Gemini uh search basically.
[38:00] >> I mean, we did that a while ago. I'm
[38:02] sure we could do better now, but
[38:03] >> yeah, I can see. Okay, cool. So, it just
[38:05] basically just decides with I didn't
[38:07] realize it was still on. [laughter] It's
[38:09] okay. Uh so okay so it tells you that
[38:11] and you just get that and then you just
[38:13] decide basically. So do you decide in
[38:15] code or do you go back to notion?
[38:16] >> Yeah no it gives me a few options and
[38:18] then it'll write the email based on that
[38:22] and it does a pretty good job of doing
[38:24] that and I just kind of copy that copy
[38:26] paste that email.
[38:27] >> Um [laughter]
[38:28] >> what well this is so this is where it's
[38:32] a little bit complicated. So what was
[38:34] happening was we were initially emailing
[38:37] these people and say, "Hey, thanks for
[38:38] your application. We want to get on a
[38:40] call. Here's a calendar link."
[38:42] >> But then we started having these
[38:43] deliverability issues because what
[38:45] happens is a lot of people send out, you
[38:48] know, spam emails or uh you know, cold
[38:50] outreach saying, "Hey, you know, let's
[38:52] get on a call so I can sell you
[38:53] something."
[38:54] >> But because they hadn't emailed us, you
[38:57] know, we were sort of essentially cold
[38:59] emailing them from the mail provider's
[39:02] perspective. So
[39:03] >> they were not getting through. So what
[39:05] it's set up to do is it the form is
[39:08] built on Uformm. So U form will send me
[39:11] but the reply address is the customer.
[39:14] Uh so then I reply to the U form email.
[39:16] So it's like a re email rather than a
[39:19] new email. And I don't include a
[39:21] Calendarly link. I say I ask if you want
[39:23] to get on a call in the next few days.
[39:25] Um and then usually they say yeah like
[39:27] when I'm free. And then
[39:28] >> what does why does that stop you from
[39:30] automating this? It doesn't. [laughter]
[39:34] >> That's the question. It's like all of
[39:35] this for that for nothing. The point is
[39:38] like you should have your Gmail
[39:39] connected. It should send that email
[39:41] rather than you doing it and copy
[39:44] pasting.
[39:44] >> This is the same situation as before is
[39:47] like, oh, how do I connect my Gmail to
[39:49] this uh write maybe read only? Maybe
[39:53] it's read only. Yeah. Okay. But again,
[39:54] it's the same Google Cloud Console
[39:56] thing.
[39:57] >> It wasn't just that. So, it's also how
[39:59] do I tie the email I received back to
[40:02] this application? It's not as if it's
[40:04] reading that email and replying. It's
[40:06] reading the notion and then it needs to
[40:08] find that email, which obviously it's
[40:10] going to have the same email address,
[40:11] right? So, it should be easy to do.
[40:12] >> Oh my god, it sounds very hard for AI.
[40:15] [laughter]
[40:15] >> I know. I know. I know. It's it's just
[40:17] it's it's that like mental barrier of
[40:19] like, oh, I'm going to have to like
[40:20] spend a few minutes like focusing on
[40:22] this and I just haven't done it yet.
[40:24] >> Okay. So, it can do all of that. I think
[40:26] we could improve our research and most
[40:28] importantly this skill should be
[40:29] scheduled. You should not run it.
[40:31] >> Um what should happen is
[40:34] >> potentially
[40:35] >> scheduled or triggered.
[40:36] >> Is it important to reply to people fast
[40:38] and how fast you respond right now?
[40:40] >> No, usually in like uh you know the next
[40:43] working day. Um
[40:44] >> so I think schedule is better because
[40:46] then you can batch all applications at
[40:48] once.
[40:48] >> And so what you probably want to do is
[40:50] you want to do a batch run as a routine,
[40:53] right? So on the cloud desktop app you
[40:54] can schedule tasks. Um so let's go back
[40:57] to mine actually and it's super easy.
[41:00] First of all like the newsletter on
[41:03] Google IO is ready [laughter]
[41:05] actually made me a newsletter while we
[41:07] were talking but and that's one of our
[41:09] skills in AI accelerator. But the point
[41:11] is you have these routines here that you
[41:12] can create and so you can just create a
[41:15] new routine run it locally run it in
[41:17] whichever folder you want. So again if
[41:19] you've broken down your folders you can
[41:20] do that. Ju sorry you're going fast
[41:22] here. So just so I understand a routine
[41:25] is a scheduled task and there's local
[41:27] routines which require your computer to
[41:29] be on and cloud routines which don't but
[41:33] some cost to that or something.
[41:35] >> Yeah, it costs more money and it's like
[41:37] uh it's you need a cloud environment set
[41:39] up. It's for developers. It's not for
[41:40] you. Don't use it and put in auto mode
[41:43] so that you know it can
[41:44] >> like it's not for me specifically.
[41:46] >> No, it's not for anyone listening to
[41:48] this podcast to be honest. Um, and it's
[41:51] like I don't think I would recommend you
[41:52] do that. Like run things locally for
[41:54] now. And you can set a schedule. You can
[41:56] say every day at 9:00 a.m. And the point
[41:57] is like the prompt would be like go
[41:59] through all pending applications and
[42:02] prepare like if you don't want to send
[42:04] the email just say prepare the drafts.
[42:06] And then what's going to happen is you
[42:07] have that thread waiting for you in your
[42:09] threads on code and you know you you
[42:11] wake up in the morning be like hey I
[42:12] reviewed them. I prepared the drafts
[42:14] etc. Uh are you okay for me to send
[42:16] them? And you're like oh maybe send the
[42:17] first two but don't send the last one. I
[42:19] don't think we should approve him, for
[42:20] example. And you're done. And the idea
[42:22] is like the thread has run already. Uh,
[42:24] and you're just kind of like you input
[42:27] the last prompt that sends the emails.
[42:29] Uh, and you can do the review quickly,
[42:31] like your manual review as you do it.
[42:33] And so that's another perk of switching
[42:34] to the desktop app is you have these
[42:37] scheduled ones that you can do. And you
[42:38] don't even have to open this interface.
[42:40] If you just make a chat and you say,
[42:41] "Let's make a new routine." And you chat
[42:43] on what you wanted to do and which
[42:45] skills you, it will just create it for
[42:46] you. So you can just have a chat on
[42:48] like, hey, every morning I want you to
[42:50] do that and every evening I want you to
[42:51] do that, etc. And use this skill and
[42:53] everything. It will write the prompts
[42:54] for you. It will do everything. And so
[42:56] that's the other thing that you need to
[42:58] think about is like not only how do I
[43:00] make skills, but also which skills
[43:01] should run on their own. And you can run
[43:03] them up to the last approval point. So
[43:06] they like you could say, for example,
[43:07] like imagine for example, we have a a
[43:10] skill section on our circle, right? What
[43:14] you could do is you could say every time
[43:16] G posts a new skill, it's only me
[43:17] posting there, right?
[43:19] >> Prepare the draft for the email for the
[43:21] email list
[43:23] >> and then you just basically you get it
[43:26] ready and then you just can open the
[43:28] markdown file. You're like yes, no or
[43:30] like you give some be like okay cute on
[43:31] bento and that's done and you don't have
[43:33] to think about it.
[43:35] >> Yeah. Yeah. I see. I see. So okay this
[43:38] is cool. So [laughter]
[43:40] like to use an analogy here, it's like
[43:42] you know when you like sometimes feel
[43:45] like not going to the gym.
[43:47] >> It's like the only thing you need to do
[43:49] is not go to the gym and work out. It's
[43:51] just put your shoes on or like get your
[43:53] gym kit ready or put on whatever.
[43:55] >> Some of these tasks like I know AI can
[43:58] do it really easily, but it's like it's
[43:59] just that like mental hurdle of like
[44:02] starting it that's uh that's there's
[44:04] some friction. But the point is you can
[44:06] do it manually and then be like hey okay
[44:07] let's schedule it and then don't don't
[44:10] put the last publishing step like make
[44:12] it stop at that point so that you retain
[44:14] all the control and then you can run it
[44:16] like 10 times and then when you're like
[44:17] fully confident it works every time you
[44:19] never change anything you're like okay
[44:20] now you can do the last step just update
[44:22] the automation
[44:23] >> but just to ask so the routines are
[44:25] triggered at a set time whereas the one
[44:28] with circle you're talking about
[44:29] wouldn't that be better to just like as
[44:30] soon as you post it be uh
[44:32] >> potentially but again is it released
[44:34] that time sensitive.
[44:36] >> No,
[44:36] >> like not really, right? If it checked
[44:38] once a day
[44:39] >> or like whatever. The thing is like
[44:41] Antropic is a little bit sneaky because
[44:43] they kind of limit you. You have limits
[44:45] for routines.
[44:46] >> Um,
[44:48] >> let's show me show you. So, if you
[44:49] actually go into settings and then
[44:52] usage, you will see that you have uh
[44:57] daily routine runs. And you can see you
[44:59] can run 15 a day, which is fine for most
[45:01] people. Like it means you can run 15
[45:03] automations per day. And it'll be
[45:04] annoying for that.
[45:05] >> Does that mean if I'm running it weekly,
[45:07] I you know,
[45:08] >> you use one for one day.
[45:10] >> Okay. Right. So, you know, let's say I
[45:13] had seven routines all week on different
[45:16] days. That's one routine of my one of
[45:18] 15.
[45:19] >> Yeah.
[45:20] >> Okay.
[45:20] >> So, it's not it's not that bad.
[45:22] Basically, uh you can automate a lot of
[45:24] stuff and provided you hit that ceiling,
[45:26] we can totally vibe code an alternative
[45:28] to this if you want to. Um and it's not
[45:31] it's not super difficult basically.
[45:32] >> Okay. So if you're using the hourly
[45:34] routine, then you're going to use more.
[45:36] >> Yeah. That and for most of the time
[45:38] that's like that's when collect is good
[45:39] because collect doesn't limit you at all
[45:41] on automations. You can do as many as
[45:43] you want.
[45:44] >> Um but yeah, you can see how now you can
[45:46] start thinking of like not being the
[45:48] trigger for these things anymore, which
[45:49] I think is kind of the next step for you
[45:52] is like how do I like what happens
[45:54] systematically and I can have AI get to
[45:58] the point where I'm needed without me
[46:00] thinking about it. And then you'll just
[46:01] see these threads pop up in your code
[46:03] desktop app in the right subfolder and
[46:06] you'll just have these little
[46:07] notifications like I have here for uh
[46:09] the newsletter for example. So you can
[46:10] see for example I have this little dot
[46:11] here next to prepare newsletter that
[46:13] means it needs my attention. So you'll
[46:14] get a thread like that basically. And so
[46:16] if these things get ready as well you're
[46:18] more likely to actually do them rather
[46:19] than skip them because they're just kind
[46:21] of cued and waiting for you.
[46:22] >> Yeah.
[46:23] >> And I think more likely to do them
[46:24] quickly as well.
[46:26] >> Exactly. And then it removes the need to
[46:28] think about it in your head which kind
[46:31] of frees mental space which is kind of
[46:33] like you know switching to the desktop
[46:34] in my opinion it will free mental space
[46:36] for you because you won't always stare
[46:38] at VS Code all the time and it's
[46:42] >> that mental space that is my blocker
[46:44] right now because you know this allows
[46:45] me to do so much but it's like that
[46:48] there's also so much more to like kind
[46:50] of just think about and you know make
[46:54] sure it's happening type thing. So yeah,
[46:56] >> so
[46:57] >> I'm literally going to when we're done
[46:58] with this, I'm going to take the
[46:59] transcript of this call and be like,
[47:01] make me a list of things I need to do in
[47:04] cloud code. Now,
[47:05] >> I'm curious to see how people like this
[47:07] episode though. Let us know in the
[47:09] comments. Uh if you think this is
[47:11] interesting or if you're more like that,
[47:13] if I should bring more people to grill
[47:15] on the podcast or something.
[47:16] >> Yeah, we could do a series of [laughter]
[47:17] like G roster your cloud code setup. Uh
[47:20] and yeah, it'd be interesting to see how
[47:22] different businesses use it as well.
[47:24] >> Cool. But yeah, so I mean I think that's
[47:26] the main stuff for you. It's like
[47:27] basically make your skills do more,
[47:29] connect all the tools, then automate
[47:30] them up to the point where it gets
[47:32] published so that you have no drop in
[47:34] quality. You can always give your
[47:35] feedback like you always do, but it just
[47:36] does it. Uh clo MD should have more
[47:39] rules uh and should also have you need a
[47:41] wiki that has a lot more context. So it
[47:43] goes and read the context it needs for
[47:44] the task at hand, but it doesn't read
[47:46] everything.
[47:46] >> Actually, one question I had, what's the
[47:48] best way to build that context? So you
[47:50] know, take the writing style example.
[47:52] Would that be just to like look at
[47:53] writing like emails and things that we
[47:55] put out before and reverse engineer it
[47:57] or
[47:58] >> Yeah, I know how you are. You'll be
[47:59] like, I want it to be perfect on day
[48:00] one. Don't try that. Uh all that matters
[48:02] is that you just want a document that
[48:04] says writing style and yeah, you can
[48:06] give it three emails and be like, hey,
[48:07] write a writing style document based on
[48:09] that. And then
[48:10] >> okay,
[48:11] >> because it has the rule of updating its
[48:14] documentation in the cloud. MD it will
[48:16] whenever you give feedback on an email
[48:18] it wrote it should offer you to update
[48:21] the writing guidelines and these writing
[48:23] guidelines just get better same as your
[48:25] skills as you use them basically.
[48:27] >> Yeah. Okay.
[48:28] >> And so that's why these kind of like
[48:30] highlevel rules matter more than hard
[48:33] facts almost you want to tell it how to
[48:35] think and what are the big highle
[48:38] frameworks
[48:39] >> how to think but how to improve as well.
[48:41] I think that's the key. But that's the
[48:42] point that it should think of improving
[48:44] itself and it should think of like doing
[48:46] the task if it can do it rather than
[48:48] telling you to do anything etc. And so
[48:50] like that's that's what your cloud MD is
[48:52] for.
[48:53] >> Yeah. Awesome.
[48:54] >> All right.
[48:55] >> It's actually super useful podcast for
[48:57] me for a change. [laughter]
[49:00] >> All right. Well, I guess uh I guess
[49:01] we're good, right?
[49:02] >> Yeah. So, uh you know, we've obviously
[49:04] been through a lot with Claude Code
[49:05] here. If you're not currently using
[49:07] claude code or you need some help
[49:09] getting set up initially, you can
[49:11] actually go on to
[49:12] authorityhacker.com/learnclaudecode
[49:15] and you enter your email there and we're
[49:17] giving away the first two lessons which
[49:19] includes the setup of claude code from
[49:22] our claude code course which is inside
[49:24] our product AI accelerator. So
[49:26] authorityhacker.com/learnclaudecode
[49:30] and you can start getting set up there
[49:32] uh as well. So, thanks Gail for uh
[49:34] roasting my quad code setup today. That
[49:37] was a humbling uh but a very ultimately
[49:40] very useful exercise. So, thanks for
[49:43] that and thank you for watching this
[49:45] podcast on YouTube. If you have any
[49:47] questions about your own claude code
[49:49] setup, leave a comment on YouTube and
[49:51] we'll go through those in the next few
[49:53] days after this podcast is out and we'll
[49:55] try and uh you know give you guys some
[49:57] help and feedback on that as well. And
[49:59] also let us know as Gail said in the
[50:01] YouTube comments if you would like more
[50:03] episodes like this where we kind of go
[50:05] into the kind of practical behind
[50:06] the-scenes setup of how businesses
[50:09] business owners are using AI in
[50:11] different ways. And yeah, of course,
[50:13] subscribe so you don't miss the next
[50:14] episode. We'll see you next week for
[50:16] another episode of the Authority Hacker
