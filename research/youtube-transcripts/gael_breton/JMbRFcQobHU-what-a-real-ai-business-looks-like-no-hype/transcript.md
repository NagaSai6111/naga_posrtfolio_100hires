# What a Real AI Business Looks Like (No Hype)

- YouTube: https://www.youtube.com/watch?v=JMbRFcQobHU
- Video ID: JMbRFcQobHU
- Upload date: 2026-06-10T05:09:49-07:00
- Transcript source: supadata
- Status: ok
- Language: en
- Fetched at: 2026-07-03T17:13:24+00:00
- Supadata billable requests: 1

## Transcript

[00:00] Today, we're lifting the curtain on how
[00:02] a real business actually uses AI behind
[00:05] the scenes. Not the flashy social media
[00:07] post that everyone makes, but the boring
[00:09] internal work that saves us hours and
[00:12] brings in lots of revenue, like our
[00:14] support bot that answers members
[00:16] questions while we sleep, a database
[00:18] that flags which customers are about to
[00:21] cancel, and a course that Claude Code
[00:23] built in just 45 minutes. I'm joined by
[00:26] Gail Breton, my co-founder, Authority
[00:27] Hacker, where we show you what actually
[00:29] works for business owners, not what
[00:32] looks good on camera. Let's jump right
[00:34] in. And really, the goal of this
[00:35] episode, Mark, is just to show people in
[00:38] real life how we use vibe coding to run
[00:41] a business that is mostly information
[00:43] work that you know, operations that are
[00:45] not necessarily what people do, but
[00:47] rather things they can get inspired from
[00:49] that could help them in their daily
[00:51] operations. And you'll see that most of
[00:52] this is non-custofacing. And yeah, let's
[00:54] just jump on the first one.
[00:55] >> Okay, so uh I'm going to go first. One
[00:57] of the things which we offer in our
[01:01] product in the plus tier is a WhatsApp
[01:04] community. And it's literally just a
[01:05] WhatsApp chat group that I've set up.
[01:08] It's none of the we don't have any of
[01:09] the business infrastructure set up. It's
[01:11] just like me personally on my phone set
[01:13] that up. And I need to make sure that
[01:16] the hund and something people who are
[01:18] trying to join that a are entitled to
[01:22] like they have the right membership
[01:23] access to be able to do that. I need to
[01:25] make sure I have their phone numbers. I
[01:26] need to make sure I add them to WhatsApp
[01:28] and that I've track in our system in
[01:31] circle uh our memberships software that
[01:34] they have been added so I don't try and
[01:36] do that again or anything and I know if
[01:38] I need to remove people in future that
[01:39] that's easy to keep track of as well.
[01:41] So, it's a really simple process that I
[01:44] was just doing it manually in the
[01:45] beginning cuz it's like ah, it takes 2
[01:47] minutes. Like, doesn't matter. But, it's
[01:49] one of these things that just the more
[01:50] it comes up, the more you do it, it's
[01:52] like, ah, this is a pain. This is a
[01:53] pain. I wish I'd automated this sooner
[01:55] and kind of bought back some of this
[01:56] time. Uh, so I'm just going to show you
[01:58] the automation in practice. All I do
[02:01] load up Cloud Code. And if you type/W
[02:04] WhatsApp on boarding, it's going to load
[02:06] my WhatsApp on boarding skill. It's
[02:09] going to pull the data from the
[02:11] application sheet which it's set up and
[02:14] it's going to give me the phone number
[02:15] of the person I need to or the people I
[02:18] need to add to WhatsApp. I copy that, I
[02:20] go over to WhatsApp and I paste that in
[02:23] and add them. That bit is manual, but
[02:25] the rest, all the logging, all the
[02:27] templating is automated. And I've just
[02:30] now also set that up as a routine, which
[02:33] is a triggered workflow. So every day at
[02:36] 6:00 a.m. now, this workflow is going to
[02:40] run and it's going to do it. So I don't
[02:42] have to even like think of doing it
[02:44] manually. It's just automatically going
[02:45] to happen.
[02:46] >> The one thing you need to watch out with
[02:47] routines is the threats don't show up on
[02:49] your chat history on the left. They show
[02:51] up in that routine and on your phone
[02:53] only.
[02:53] >> Yeah.
[02:54] >> So yeah, and it's good 6 a.m. because it
[02:56] starts your limits early as well, which
[02:57] means you get a shorter session on your
[02:58] first session, which means you can
[02:59] hammer close code when you wake up. All
[03:01] right, so let's talk about how this
[03:03] actually works in practice. And this is
[03:06] the unfiltered reality of how we set it
[03:09] up. And I just want to say now, it's not
[03:11] perfect. So Gail, I know you're like
[03:14] here shaking your head in disgust that
[03:16] why I still have Zap here, but I'll
[03:18] explain that as I'm going through it. So
[03:20] we have a form which is embedded in our
[03:23] circle community in a space that only
[03:26] plus members and max members have access
[03:27] to and they update their profile field
[03:31] basically and when they do that Zapier
[03:34] is listening out and it triggers an
[03:36] automation which sends me a Slack
[03:38] notification and it adds that data to
[03:40] Google sheet 100% we can automate this
[03:44] with cloud code like we don't need
[03:46] Zapier for it at all
[03:47] >> when I set it up we have have a Zapier
[03:49] account. We're using it for some other
[03:51] stuff. I was like, this is the lowest
[03:52] friction way to do this right now. I
[03:54] just I just need to need this set up.
[03:56] This was before I built the skill. By
[03:57] the way, uh this was just to trigger
[03:59] notifications. So, it gets added to a
[04:01] Google sheet, and I used to just have to
[04:03] go in, check that Google sheet, update
[04:05] it manually, check if they had the right
[04:07] access, do all that stuff. Now, however,
[04:10] when that skill runs, it has access to
[04:12] my Google Drive through the Google Drive
[04:16] CLI, which is like a sort of MCP thing.
[04:18] It's basically has full access to read
[04:20] and write everything. It was a bit of a
[04:21] pain in the ass to set up, but you know,
[04:23] Claude Code walked me through it. And
[04:25] once you have that set up, you can read
[04:26] and write things. I think my mistake
[04:28] early on was I thought I could use the
[04:31] clawed connector in there to do
[04:33] everything, but apparently that can only
[04:35] read information.
[04:36] >> It doesn't have a right title,
[04:37] >> not write to it. So that was that was a
[04:39] bit of a Yeah.
[04:40] >> For the members who are listening, I
[04:42] actually made a lesson on connecting
[04:43] this specific CLA in a new course. And
[04:46] so it's like I teach CLA in general, but
[04:48] I use that one because I know it's a
[04:50] handy one. So it's like there's
[04:51] >> all it is, all a CLI is really is a way
[04:54] for AI in this case, so cloud code to
[04:58] access all of the functions that are
[05:01] possible inside Google Workspace, right?
[05:04] So it can open a sheet, it can read a
[05:06] sheet, it can write to a cell, that kind
[05:08] of thing. And it just makes it very
[05:09] streamlined and very easy and very quick
[05:11] for it to do. So you can also achieve
[05:13] the same thing using the MCP as well. So
[05:16] next thing is Claude will read the sheet
[05:18] and it looks up the members circle ID.
[05:22] So that's the data we get out of circle
[05:24] and I think out of Zapier as well. It's
[05:26] like this ID. It doesn't mean anything
[05:27] to me. I have to use AI to look it up
[05:30] but it does automatically. It figures
[05:32] out what membership tier they're in and
[05:35] if they are in the right membership tier
[05:37] then it's going to add it to my list of
[05:39] people to add and I just copy it. Gives
[05:42] me everything in a copy pasteable
[05:44] format. I add them to WhatsApp. They're
[05:46] in WhatsApp. I type done and then Claude
[05:49] tags everyone correctly so we know who's
[05:52] who's in there. Updates the member
[05:53] fields. Very very very simple
[05:56] automation. And as you can see like
[05:58] Claude does all these like really minor
[06:01] things like you know checks there's no
[06:03] duplicates so nobody's added twice. you
[06:06] know, it makes sure they have the right
[06:07] membership tier. Make sure like all the
[06:09] data in circles uh added and it's like
[06:12] uh it's very easy for me to copy paste
[06:14] in uh because it has like the plus
[06:15] symbol for international phone numbers
[06:17] cuz like sometimes people don't have
[06:19] that. It's like it just fixes all the
[06:21] tiny stuff that takes me like a few
[06:23] seconds or a minute here or there. But
[06:25] that [ __ ] really adds up over time.
[06:27] >> Here's my question. that
[06:28] >> why don't you try to use the computer
[06:31] use to have it add people on the
[06:32] WhatsApp app if it runs like 6 a.m.
[06:35] >> Yeah. I mean it's probably the next
[06:37] thing I could do with it. Uh I mean the
[06:38] honest answer is when I last used
[06:40] computer use admittedly this was like 4
[06:42] months ago or something. It was pretty
[06:45] crap. But I I hear it's gotten a lot
[06:47] better. So yeah.
[06:48] >> And it's not just that. It's like you
[06:50] have time right 6 a.m. You're probably
[06:51] not at your computer at the time. So
[06:52] even if it's slow as hell like you can
[06:55] probably just do it. I do more and more
[06:57] browser use, computer use now actually.
[06:59] It's not perfect. It's slower and it's
[07:01] clunky but it will do it eventually if
[07:03] you give it enough time basically. So
[07:05] yeah, I mean that's like very simple
[07:06] basic skill. I think anyone can build
[07:08] that in a very short space of time. You
[07:11] though have created a slightly more
[07:13] complex skill and then done something
[07:15] quite different with that. So that's
[07:18] probably like the next level up from
[07:20] just building a simple skill. You want
[07:22] to talk to us about that now?
[07:23] >> Yeah. So I mean as we said we're going
[07:25] gradually more complex through this.
[07:27] Your first one was like a simple scale.
[07:28] The next one I have is actually still
[07:30] kind of a scale and the output is
[07:33] basically like the lesson notes. So for
[07:35] example this is the new course that we
[07:37] just released like the clo code means
[07:38] business one which is an update to our
[07:40] code course but it has like new work
[07:42] templates works a little bit like open
[07:45] and her and stuff but the point is the
[07:47] entire course inside circle which is the
[07:49] platform that we use was created by
[07:51] cloud code. The only thing I did was
[07:52] shoot the videos and they were edited
[07:54] through the script and then I basically
[07:57] gave clude code the link to the videos
[07:59] on the script and it did everything. It
[08:01] created the lesson notes. It created the
[08:04] illustrations. It humanized the whole
[08:06] thing. So you won't see a single m dash
[08:08] here and it actually sounds pretty good
[08:09] and sounds like me. Did all that. Uh and
[08:12] it didn't create one lesson. It created
[08:14] all lessons, all notes, everything when
[08:17] the course is done in one prompt
[08:19] basically. And I can actually show you
[08:21] the prompt. You can see the prompt that
[08:23] I uh actually gave it was like hey I
[08:25] want to create a new course called cloud
[08:26] coin business and circle not published
[08:28] yet. Uh create the lessons video 1 to9
[08:31] including 2.5. It's like a lesson I put
[08:33] in between and I just I did not even
[08:35] export the videos or the transcripts or
[08:37] anything. I just gave it the link to the
[08:39] folder on the script which is like the
[08:41] you know cloud video editing tool that
[08:42] we're using. And I was like, for each
[08:44] video I want you to create beginner
[08:45] friendly non-jargony lesson notes that
[08:47] walk them through the step and the
[08:48] concept and what to do well formatted.
[08:51] When explaining concept, create images
[08:52] using GPT images, which is another skill
[08:55] that we have, like the image that you
[08:56] just showed, for example, just basically
[08:58] did that. And I just told it like
[08:59] whiteboard plus handdrawn marker, which
[09:01] is kind of the style I usually go for.
[09:03] And I kind of keep it consistent. For
[09:05] each lesson, create a thumbnail with my
[09:06] photo. And so again, for all the
[09:08] thumbnails of all the videos were also
[09:10] created in one shot. So that means 10
[09:12] thumbnails plus about 30 to 40 images
[09:14] plus about 10 lesson notes. And I said,
[09:16] "When you're done, upload everything on
[09:18] Circle. Point me to the folder with the
[09:19] thumbnails cuz the thumbnails I need to
[09:20] upload with the videos at the end. Ask
[09:22] me any question if you need more
[09:23] context. You can see the outline of the
[09:25] course here." And I gave it a notion
[09:27] link. Like again, I did not export
[09:28] anything or whatever. It's just all
[09:30] connected to everything. And Godspeed.
[09:32] >> I uh I like how you wrote Godspeed at
[09:34] the end. Does that think that made any
[09:36] difference?
[09:37] >> No. Uh it's just fun for me. So this is
[09:40] like a really complex project. Not a
[09:42] task, it's a project. I mean when we had
[09:44] a team of people before this was, you
[09:47] know, like multiple people working on
[09:48] this for, you know, days if if not a
[09:51] week
[09:52] >> to pull something like this together. So
[09:53] it's pretty impressive you're able to do
[09:55] that with just this one prompt. Now
[09:57] >> this was about basically because the
[09:59] model is like clawed code and the model
[10:01] is so good now or what's the reason it's
[10:03] able to pull this off? Yeah, it's just
[10:05] able to kind of like stay on track
[10:07] longer and I think that's kind of what
[10:08] you see in terms of the models getting
[10:10] better. So a lot of people are like ah
[10:12] Opus 4.8 is it really better than Opus
[10:14] 4.5 etc. It is but not necessarily like
[10:17] early in the context of for small tasks.
[10:19] It's like the way I explain to people is
[10:20] like you cannot write emails 10 times
[10:23] better anymore with AI. Like there's no
[10:26] way to write better.
[10:27] >> Diminishing returns on what you can get.
[10:29] And especially if you watch, you know,
[10:31] we're guilty of this as well, like
[10:32] YouTube videos, podcasts, uh where
[10:34] people are talking about the new models
[10:36] like they come out and they have a few
[10:38] hours or minutes to test it. So they go
[10:40] like, oh, generate an image or write an
[10:42] email or do all the stuff they've done
[10:43] before. But it there's marginal
[10:46] difference versus like a big project
[10:47] like this with thought uh you know it
[10:50] takes like a lot longer to actually
[10:52] produce it. So that's where you're
[10:53] seeing the difference. So
[10:54] >> yeah it's like these outputs are
[10:55] saturated basically at this point like
[10:57] they will get marginally better with the
[10:58] new models and like you'll find a slight
[11:00] improvement but the reality is like this
[11:01] is where we've progressed in the last
[11:03] six months is like you need to be more
[11:04] ambitious with your prompts and give
[11:06] them bigger things. It's a discussion we
[11:07] have a lot internally is like how can we
[11:09] just offload more responsibility. This
[11:11] was literally like this is going to be
[11:12] studentf facing and you're building
[11:14] this. Now the two things that I had to
[11:16] do that was uploading the videos and the
[11:18] thumbnails mostly because the MCP
[11:20] doesn't allow not because clo couldn't
[11:21] do it. It's just like it doesn't have
[11:23] >> circle MCP doesn't allow uh yeah
[11:26] uploading videos. Okay, that makes
[11:27] sense.
[11:28] >> And then other than that it was adding
[11:30] some screenshots. So like taking
[11:32] screenshots for some areas. So for
[11:33] example the initial install. You can see
[11:35] the thumbnails are good by the way.
[11:36] They're not too bad basically. And like
[11:38] these screenshots for example I did
[11:39] manually because we're not at the point
[11:42] where it's good enough to create the
[11:43] right screenshots at the right place
[11:45] etc. So I created a few screenshots. You
[11:46] can see otherwise the explainer images
[11:48] etc. They're good. They're like simple
[11:50] for beginners. Uh yeah it's very
[11:52] scannable. It did the formatting very
[11:54] well. It did all of that. It figured it
[11:55] all out for me basically. And so in the
[11:57] end putting this whole course together
[11:59] was like code walking for 45 minutes and
[12:01] me maybe another 45 minutes of like
[12:03] making sure that screenshots are here,
[12:04] uploading the videos and uploading the
[12:06] thumbnails basically. And there's about
[12:08] 10 lessons. There's 10 more that are
[12:09] coming out actually uh this week. So
[12:11] this course will be at 20 lessons. But
[12:13] the idea is like yeah, I just need to
[12:15] shoot videos now. And then everything
[12:17] else is almost fully automated and it's
[12:20] quality like I don't think the quality
[12:22] compared to what we used to do
[12:23] previously. I don't think the quality
[12:24] has dropped. Arguably it's better like
[12:27] the explainer images etc. We didn't do
[12:29] that before. So that shows you as well
[12:31] how you can combine multiple skills
[12:32] because there's a skill for creating the
[12:33] lesson nodes. There's a skill for
[12:34] creating images. There is like some
[12:36] skills that explain how to use circle
[12:38] for example. It kind of combines all
[12:39] these things into one mega prompt and
[12:41] does that.
[12:42] >> Something I want to add here because you
[12:43] know a lot of people challenge us on
[12:46] like hey you know when I use AI it's it
[12:48] just gives me kind of slop it's not as
[12:50] good but I think the difference here is
[12:52] that you have created original content
[12:55] here in the tutorial
[12:56] >> the video. Yeah right exactly the video.
[12:58] >> So it's not like making up facts about
[13:00] how to get cloud code up and running
[13:03] itself. It's using your information and
[13:06] it's just like finding nicer or clear
[13:08] ways to articulate points that you've
[13:11] already made. So, it's really like a
[13:13] repurposing task rather than a full
[13:16] generation task here. That's why it
[13:18] sounds
[13:18] >> does it has a bit of freedom in the
[13:20] sense that it's allowed to expand a
[13:21] little bit what I say. So, you can go
[13:22] and use web search and it's like let's
[13:24] say there's like some details, some
[13:25] settings that I forgot to mention,
[13:27] whatever. It will kind of correct me in
[13:29] the le notes and then make sure the
[13:31] whole thing is better. But like, you
[13:33] know, it's like a little bit of wiggle
[13:34] room, not like start from scratch. And I
[13:36] did the planning. I did all of that. I
[13:38] used AI to help me with the planning.
[13:39] Sure. But it's like I was involved and
[13:42] it wasn't like fully automated,
[13:43] whatever. What was fully automated was
[13:44] like all the boring work basically like
[13:47] all the rewriting things and making sure
[13:49] the notes are clear, uh, making these
[13:50] explainer images, briefing them, all of
[13:53] that, like the prompting. I didn't have
[13:54] to download them. I didn't have to do
[13:55] anything. It just uploaded them for me.
[13:57] Like all that busy work. And I think
[13:59] that's kind of the thing. It's like
[14:00] people aim to make AI create their
[14:02] content. But I think they should free up
[14:04] their time to create content uh exactly
[14:07] and then just have AI do all the boring
[14:09] stuff uploading all the even editing
[14:11] etc. And then that's how you create
[14:13] content that people still care about. So
[14:15] this course is quality like people love
[14:16] it so far. We've had really good
[14:18] feedback.
[14:19] >> I think as well people are so people
[14:23] might be watching this and think oh I'm
[14:24] not creating courses or I'm not so much
[14:26] of a content creator. This doesn't apply
[14:28] to me. But let's say you know you're an
[14:29] agency or you're in an internal sort of
[14:32] B2B team right you are creating content
[14:35] when you have calls with your clients or
[14:37] sales calls or any kind of call that you
[14:39] have a transcript with you can run a
[14:41] similar process here to you know
[14:43] generate your proposals or
[14:46] >> um your project plans or whatever else
[14:48] it might be and it'll like it's not
[14:50] difficult to build something like that.
[14:52] I mean you saw Gail's prompt there as
[14:54] well like three or four paragraphs
[14:55] >> because there's a lot of skills behind
[14:56] but yeah sure like once you've built
[14:58] your infrastructure like you need to
[14:59] kind of build this kind of knowledge
[15:00] base same like my workspace has a lot of
[15:03] knowledge about the company the tone
[15:04] everything like it has a lot of context
[15:06] to use and that's why like I think it
[15:08] reads well like I think it's like the
[15:10] reading the writing for example is very
[15:12] clear and it doesn't feel like it was
[15:14] like super badly written by AI for
[15:16] example um because you have that context
[15:19] >> and I'm just going to take a sec to do a
[15:20] shameless plug here but if you want to
[15:21] learn how to build a workspace exactly
[15:23] like that and all the skills that go
[15:25] behind that. Then we're actually running
[15:26] a free webinar for you guys next
[15:29] Tuesday. That's going to be the 16th of
[15:31] June. It's at 5:00 p.m. UK time, so it's
[15:33] about noon Eastern time. Uh it's
[15:35] completely free. Gail and I'll be
[15:37] hosting it and we're going to show you
[15:38] behind the scenes on how we build all
[15:40] this kind of stuff, how we set up our
[15:41] Claude Code workspace. And it is for
[15:44] business owners who are non-technical.
[15:46] So don't worry if you've never written a
[15:48] line of code in your life. We don't
[15:50] write code. We communicate with claude
[15:51] code in English. Uh, and you can build
[15:54] all this stuff pretty quickly. Y
[15:56] >> um, and we'll show you how to do stuff.
[15:57] >> We're going to show you some better
[15:58] ones. These are the easy things. This is
[16:00] the lowest level basically
[16:02] >> like day one or week one stuff. Yeah.
[16:04] >> Yeah. This is so
[16:05] authorityhacker.com/webinar
[16:08] and you can sign up for free there. Hope
[16:10] to see you there. All right, Gail. So,
[16:12] we've talked about making simple skills.
[16:15] We talked about making some more
[16:16] advanced skills, but something we've
[16:19] been doing a little bit more of is
[16:20] taking skills and turning them into kind
[16:23] of autonomous agents or bots or what
[16:26] would you really call these things?
[16:28] Yeah. I mean, basically moving them like
[16:30] these things, they run on your clothes
[16:31] code. You're usually typing on your
[16:32] keyboard for these things to happen.
[16:34] It's like how do you make them happen
[16:35] when you're not at your keyboard? And I
[16:37] think you wrap a bit more code around it
[16:39] and you host it on the cloud basically.
[16:42] Like how do you do that? And I think
[16:43] that's kind of the logic like
[16:45] progression. You start with like making
[16:46] a skill. You're like, am I happy with
[16:48] this? Is AI doing a good job? Etc. And
[16:50] then for some jobs, for the courses, I
[16:52] wouldn't do that. But like for some of
[16:54] the jobs we're going to show you, it
[16:55] makes sense that you should not even be
[16:57] intervening at all and it just happens.
[16:59] And then that's kind of like you build
[17:01] this for the multiplayer when your
[17:03] attention is not even needed for the
[17:05] thing to happen because that's kind of
[17:06] the limitation that we are starting to
[17:08] feel right now. It's like we run all of
[17:09] these things on code etc. But you're
[17:11] kind of running like five threads at
[17:13] once and so on and there's a lot of
[17:14] things happening and then it's like
[17:15] you're still
[17:16] >> it's not it's not even like that's not
[17:18] the problem that you're running five
[17:19] physical threads in claw code. It can
[17:21] handle that. It's your like it's your
[17:23] brain.
[17:24] >> My brain is the bottleneck. Yeah. Cuz
[17:26] like you do five times as much work and
[17:28] that's great, but then you have to think
[17:30] about five times as many things. And
[17:31] even though you're not physically doing
[17:33] it, it's like you're doing less actions
[17:35] like actions per minute but like your
[17:37] thoughts per minute is like way way
[17:39] higher. And that is tiring.
[17:41] >> Yep.
[17:42] >> Uh so this kind of gets around that.
[17:43] >> Okay. So the next part I want to show
[17:45] you is actually our support bot. So it's
[17:47] actually we have a get help section and
[17:50] you can see that for example people can
[17:52] ask questions and get help and we help
[17:54] them like we are still here helping
[17:56] people. However, I am not awake 24 hours
[17:58] a day and I'm not always at my computer
[18:01] and sometimes people are stuck on things
[18:02] and it's not great to wait for like many
[18:05] hours. And the thing is I often found
[18:08] that people's problems I could solve not
[18:10] necessarily by my great knowledge in my
[18:12] head but rather by prompting AI
[18:14] properly. And so quite often I would
[18:15] just answer to people like a summary of
[18:17] what I would get from an AI chatbot
[18:19] connected to the knowledge base that I
[18:21] have also in my workspace and you know
[18:23] my notes and and all that stuff
[18:24] basically. And then I was like wait I'm
[18:27] becoming a copy paste machine again. uh
[18:29] was like it's like it feels like added
[18:32] value but really it isn't like because
[18:34] it's like I wasn't doing much. And so
[18:36] what I did is I built this little age
[18:38] helper. Uh age helper is basically that
[18:40] for this is my avatar. This is the age
[18:42] helper avatar which is me uh as a robot
[18:46] basically and the idea is agehelper is
[18:49] always here to help you out and whenever
[18:51] you post a question in the uh get help
[18:55] section only then if it's a technical
[18:57] question it's going to answer. if it's
[18:58] not a technical question like if
[19:00] someone's like super mad at us etc. is
[19:01] actually going to skip answering and
[19:03] it's going to wait for a human to
[19:04] answer. So it's pretty smart in a way it
[19:06] decides what to do. And so initially I
[19:08] built it on my computer. So I would call
[19:09] my computer and my computer would wake
[19:11] up and we start it's built on codeex and
[19:13] then it was connected to a whole
[19:15] prompting system. It gives like these
[19:16] pretty cool things these pretty cool
[19:18] instructions and stuff. Sometimes it
[19:19] even gives prompt for people to give to
[19:21] their code. So that code solves the
[19:23] problem for them. Like we've built all
[19:25] that stuff and the idea is I get back to
[19:26] them. And so how is it? Just to be clear
[19:29] though, so you had this system like
[19:32] internally that you were using to answer
[19:34] a lot of questions. Yeah. Before
[19:35] >> I did it manually. I had a skill
[19:38] >> and then I was like, I'll make it a bot.
[19:39] It run on my computer and then
[19:41] eventually I was like, well, what if I'm
[19:42] traveling? My computer is off. I run on
[19:44] a laptop. I don't have a Mac Mini.
[19:46] >> So from a skill to a bot to an
[19:48] autonomous bot essentially.
[19:49] >> Yeah, pretty much. That's where I'm at,
[19:50] right? And now I'm actually expanding
[19:52] it. So I'm building like DMs into it,
[19:54] for example. So people can DM it and not
[19:56] necessarily share publicly their issues
[19:57] and it can help them because people are
[19:58] liking it quite a lot actually. Um and
[20:01] so
[20:01] >> and and I want to be very clear as well
[20:03] because I know a lot of companies will
[20:05] be like oh I don't want to automate my
[20:06] support. That's a bad experience. They
[20:08] have you know horror stories from uh big
[20:11] companies like PayPal that you can never
[20:13] get through someone and you just keep
[20:14] getting automated answers things like
[20:15] that.
[20:16] >> Yeah.
[20:16] >> Well we've fully disclosed that this is
[20:19] uh AI helper. Like if you come out of
[20:21] this Gale, there's a big image at the
[20:22] top of the get help section that
[20:24] explains how the system works. Like
[20:26] you'll get your AI helper reply and then
[20:28] we will come and reply when we're awake.
[20:31] >> And you can see I jumped in, right? It's
[20:32] like I jumped in later and I was like,
[20:33] "Yeah, I actually agree with what the
[20:34] bot said." So yeah, whatever.
[20:37] >> So people are getting the best of both
[20:38] worlds. They're still getting the same
[20:41] answer or similar answer to what we
[20:42] would have given them anyway. they're
[20:44] still getting the marker gale kind of
[20:46] oversight and they're also getting an
[20:48] instant answer as well. And so when you
[20:50] present it like that, then it's a
[20:52] win-win for everybody.
[20:53] >> Yeah, I agree. And it's like, you know,
[20:55] for example, like Detroit this guy and
[20:57] actually this was before I fixed the
[20:58] formatting issue with the new bot, but
[21:00] like this guy asked this complex
[21:01] question and then AI helper gave him
[21:04] like this answer and gave him the prompt
[21:06] to give to code for like how to build
[21:08] his strategy and everything. And
[21:09] literally like people are like, "Oh,
[21:10] this is super helpful. I hope to learn
[21:12] how to hire someone like you later. So,
[21:14] it's like it's actually a good thing,
[21:15] right? It's like uh
[21:16] >> I I think we get away with it a little
[21:18] bit more because
[21:19] >> because it's an AI thing,
[21:20] >> AI, right? So, you do have to be a
[21:22] little bit careful with that stuff, but
[21:24] I mean customers getting instant answers
[21:26] that are good.
[21:27] >> Yeah. And then I DM
[21:28] >> that's a very positive thing.
[21:29] >> Then I jumped in. I DM'd him a skill
[21:31] that I use for strategy and I was like
[21:33] try to use this. And the point is this
[21:35] guy has to Anyway, let's go back to how
[21:37] this works. I don't think people care
[21:38] too much about how we run things. And
[21:39] so, how does this work? is like yeah
[21:41] member ask and now what I've done is
[21:43] actually the codeex instance that runs
[21:45] this is on the digital ocean server
[21:47] which means that it's always on and then
[21:50] my computer can be off and it is just a
[21:51] terminal on a digital ocean server I
[21:53] think we pay $12 per month and it
[21:55] basically operates that and I've worked
[21:57] quite a lot on protecting it from prompt
[21:59] injection and things like that so for
[22:01] example uh it does not have many tools
[22:03] it can only do web search and the
[22:06] context of like the membership and all
[22:08] the notes that we gave it for like
[22:09] knowing what to and and the knowledge is
[22:11] actually gathered by a third party
[22:14] Python script. So it's kind of like
[22:15] gathered by a script that runs before
[22:17] and then it gives it to the bot as
[22:19] context to use. Basically it just and
[22:21] then the but can use that or not use
[22:23] that. Then what happens is the bot can
[22:26] only draft an answer and it doesn't even
[22:28] interact with circle. So someone cannot
[22:30] prompt inject it on like you know do
[22:32] some crazy things on circle and then
[22:34] what happens is just it passes text to a
[22:36] script that uh then post the answer
[22:39] which means like the script itself
[22:40] cannot be prompt injected and can only
[22:42] do one thing which is post an answer it
[22:44] cannot interact in any other way with
[22:46] circle so the point is like I've thought
[22:47] a lot about security on these things I'm
[22:49] a bit if you guys are in the membership
[22:50] you know I'm a bit stupid on security
[22:52] maybe but I care a lot about that and
[22:54] it's not just a random codeex thing
[22:56] >> stupid is the right word I think
[22:57] paranoid is the right word I'm I'm a bit
[22:59] scared. So basically I wasn't careful.
[23:01] >> Uh and so the point is like
[23:03] >> stupid would imply you're don't care
[23:04] about it. So I the opposite.
[23:07] >> I care about it a little bit too much
[23:08] sometimes. So that's kind of the way I
[23:10] built it. And it's quite interesting
[23:11] because it has a filter. So the AI
[23:13] before it answers basically decides if
[23:15] it's going to answer or not. So in the
[23:16] output it says post it or don't post it.
[23:18] And it will help with like technical
[23:20] issues for example and finding resources
[23:21] on the thing. But like if someone's like
[23:23] hey I want a refund or you guys suck or
[23:25] whatever. um then it's not going to
[23:27] start replying.
[23:28] >> No, no one's posted that so far though,
[23:30] right?
[23:31] >> So far, it hasn't happened, but who
[23:32] knows? That might happen one day. And if
[23:34] it does, in principle, it should not
[23:35] respond basically. And so that's the
[23:37] idea. Now, one thing that's really kind
[23:39] of cool with this bot is it, as I say,
[23:41] it runs on codec cli, which runs on the
[23:43] subscription, which means like this
[23:44] basically runs like this whole thing
[23:46] runs on 20 bucks per month subscription.
[23:48] This runs on Gypy 5.5. So, it's a good
[23:49] model. It's expensive as well, and
[23:51] that's why the answers are so good. But
[23:52] the point is if we paid API prices, we'd
[23:54] probably pay hundreds of dollars. And
[23:55] because I actually built it on a server
[23:57] that can run a terminal, I can connect
[23:59] it to a basically subsidized
[24:01] subscription from OpenAI and therefore
[24:05] reduce our cost significantly.
[24:07] >> Is that kind of kosher or is that a bit
[24:10] >> actually open is kind of cool with it.
[24:12] So like if it was entropic, they would
[24:14] not be cool with it. But like Sam Atman
[24:16] came out and like if you pay for
[24:18] subscription, you can use it however you
[24:19] want and they're fine with programmatic
[24:21] use or whatever. So it's like so far so
[24:23] good. It might change in the future,
[24:25] especially as need to turn more of a
[24:26] profit. But right now, it's worth doing
[24:28] for us. And that's kind of a tip for
[24:30] those of you who care about that is that
[24:32] if you run on something like a digital
[24:34] ocean server, you could run the
[24:35] terminal, you can run a subscription,
[24:37] and you can save a lot of money. Like a
[24:38] $200 subscription would give us like so
[24:40] much. Like eventually, I could imagine
[24:42] us expanding this, paying $200 a month
[24:44] and get like basically unlimited usage
[24:46] for all these bots, for all our needs,
[24:48] our automated needs basically. That's
[24:50] kind of how I see it. And then
[24:52] eventually if they stop it.
[24:53] >> Does that have to be a full-time 24/7
[24:55] server? That would that work on like a
[24:57] Cloudflare work?
[24:58] >> No, it wouldn't. I don't think it would
[24:59] work. Maybe it would. I I mean I'm not a
[25:01] programmer so I'm sure there's like a
[25:03] crazy way to make it work, but like out
[25:05] of the box you kind of need like a
[25:06] terminal. Uh and so that this runs on
[25:08] Linux and it's a terminal and everything
[25:10] and but you can run it on very cheap
[25:11] server. I think the server we run is $12
[25:13] per month. So yeah. And just to be clear
[25:15] as well, like we really don't know the
[25:17] ins and outs of all of the like, you
[25:19] know, Cloudflare and Digital Ocean and
[25:21] things like that. It's like Claude had
[25:23] or Codex has built it for.
[25:24] >> This is a proper vibe coding podcast.
[25:26] Like we're talking about like it's like
[25:28] even a lot of these logics on like I was
[25:30] like let's just make it secure. Let's
[25:32] brainstorm ways to make it secure. And
[25:33] it was like okay well we need to prepare
[25:35] for prompt injection. So we're going to
[25:36] gather the context outside. We also
[25:38] won't make it take any action. It's just
[25:40] going to write text basically. So it
[25:41] cannot do anything. You're not starting
[25:44] by saying hey here are the five steps I
[25:46] want you to follow. What you're doing is
[25:48] you're saying I want it to this is the
[25:49] outcome and I want you to think about
[25:51] security.
[25:52] >> Yeah. I'm scared of prompt injection.
[25:54] How do we fix that? Uh update the plan
[25:57] and then basically we'll do some
[25:58] research and do it right.
[26:00] >> It's almost like a good way to think
[26:01] about it is like you're the like uh non-
[26:04] techsavvy CEO talking to the CTO who has
[26:08] to then go away and like build it. And
[26:10] that CTO is now clawed or codec.
[26:13] >> Yeah, exactly. You come with your
[26:15] questions and your problems and then you
[26:17] have it walk on solutions and now is
[26:19] this going to be like, you know,
[26:20] enterprisegrade solution. No, but like
[26:23] for a bot that just answers on the
[26:25] private community, it's fine. Basically,
[26:28] >> and something that you said to me last
[26:30] week actually was like try and push the
[26:34] envelope out a little bit more. Um
[26:36] because I think a lot of people they
[26:38] have an idea of what they think AI can
[26:40] do. Yeah.
[26:41] >> Especially if you're kind of a bit of a
[26:43] perfectionist and you're quite
[26:44] particular about how things are done.
[26:46] >> Um I'm sure a few people can relate to
[26:48] that.
[26:49] >> Then you kind of like tell it what it
[26:51] needs to do. But if you just give it the
[26:53] goal and the objective, you might be
[26:56] quite surprised at like how capable it
[26:58] really is. Now, and what I like to make
[26:59] it do as well is I'm like, "Oh, instead
[27:01] of trying to come up with things, just
[27:02] do some research in like GitHub
[27:04] repositories and how people are
[27:05] addressing this problem, right? So, it's
[27:07] it goes on like a bit of a web search or
[27:08] it sends like a sub agent that does a
[27:10] bunch of web search and that comes back
[27:12] with useful context that then guides its
[27:15] technical decisions. And so, you're kind
[27:16] of piggyback writing technical people
[27:19] that posted stuff on the internet
[27:21] basically. So I'm not using codeex very
[27:24] much at all right now but I'm building
[27:26] most of my stuff in cloud code.
[27:28] Sometimes when it does that it comes
[27:30] back with like you know quite technical
[27:33] program type language and I get a little
[27:35] bit like I don't know what this means.
[27:38] >> Quite often. Yeah. Yeah. quite often
[27:40] inside my chats I just stop it and I
[27:42] write Eli 10 what this means like
[27:46] explain this like I'm 10 years old what
[27:48] this means and it and it makes a very
[27:50] nice analogy and it's just like oh okay
[27:52] right I get that
[27:53] >> exactly so it's just a lot of people do
[27:54] that right they get an answer from AI
[27:56] that they don't understand and they're
[27:57] like oh that's it I'm in technical land
[27:59] I can't do this and it's like they give
[28:01] up but actually it's just like hey I
[28:02] have no clue what you just said like
[28:05] explain again quite often as well ask me
[28:07] questions and it's like I have to make
[28:08] decisions it's like oh do you prefer
[28:09] using this uh this crazy branch of this
[28:12] thing or do you want like to create a
[28:14] custom CLA about the API? You know,
[28:16] crazy technical terms. I'm like, I have
[28:18] no idea what you're saying. Just just
[28:20] rephrase this please in a simple way.
[28:22] >> Another good one is like, all right, now
[28:24] we need to set up the server and do this
[28:26] and like that would be step one. Step
[28:28] two would be this. And the answer is do
[28:30] it yourself or just just do it for me.
[28:32] >> It does that. It gives you walk and you
[28:33] shouldn't do it.
[28:34] >> Yeah.
[28:35] >> It's like I'm like no, no, no. I don't
[28:36] do anything. still on the chat and uh
[28:39] yeah that's one I think that's one thing
[28:40] we talked about as well is like you
[28:42] install the terminal tool and then you
[28:43] just have it operate the terminal tool
[28:44] and you don't leave your chatbot the
[28:47] truth is the most of this customer
[28:48] support I built on my phone I built on
[28:50] the Codex app by just talking to it like
[28:52] a walkie-talkie while walking my dog and
[28:55] most of actually a lot of my codeex
[28:58] building time is on my phone now and
[29:00] just kind of talking into it at the gym
[29:02] outside whatever or even like on my sofa
[29:05] end of the day when I'm super tired and
[29:07] just get ideas for features. So, for
[29:08] example, like last Sunday, I was like,
[29:09] "Ah, would be great if people could DM
[29:11] and kind of talk about more sensitive
[29:13] topics with the bot cuz it's pretty
[29:14] helpful." And then it's like I already
[29:15] have a feature that's set up now. It's
[29:17] not live, but it works. And then it's
[29:19] like I need to test it more. But like uh
[29:21] eventually,
[29:21] >> you are you reading the response it gets
[29:23] or do you have it like text to voice
[29:25] into an AirPod or something?
[29:27] >> I like to read like I'm a I'm a reader,
[29:29] but everyone to their own like if you
[29:32] want it, you could do that. Uh but yeah,
[29:34] anyway, that's the support bot. It's
[29:35] kind of handy. And again, that could be
[29:37] answering customers emails, that could
[29:39] be helping with technical questions,
[29:40] that could be anything like eventually I
[29:42] want to make it almost like an API. And
[29:44] I want to plug it into all our customer
[29:46] support channels basically. So that's a
[29:48] VIP code project that went all the way
[29:50] from a scale to like a proper bot that
[29:52] runs.
[29:52] >> Nice. I want to move on now and talk
[29:55] about something which I first heard
[29:57] about when back in the day when I had a
[29:59] real job in a large enterprise company.
[30:02] It's called data warehousing. And it's
[30:04] one of those terms that sounds like kind
[30:06] of corporate [ __ ] bingo that I just
[30:08] like, oh, send me to sleep now. Kill
[30:10] kill kill me now.
[30:10] >> It sounds boring.
[30:11] >> It sounds boring, but it's super cool
[30:15] when you don't have to do any of the
[30:16] work behind it and you just kind of give
[30:18] it the guidance to do it. So, do you
[30:19] want to explain what the problem is
[30:21] we're actually trying to solve with this
[30:23] and how we built this warehouse of all
[30:25] our data?
[30:26] >> And I actually have this little image
[30:27] that was prepared for that. And
[30:28] basically, it's the idea of creating one
[30:30] database that has every single event
[30:32] that happens in your company. So if you
[30:33] look at what we do for example, we
[30:35] collect payments on stripe. When people
[30:38] check out it comes there. People use our
[30:41] product on circle which is like a
[30:43] community platform. So whether they
[30:44] watched a video, they logged in or they
[30:46] liked something or whatever like that
[30:48] data lives there. Then we do email
[30:50] marketing with a tool called Bento.
[30:51] Again they have all our open rates,
[30:53] their click rate, when people
[30:54] subscribed. We also track like you know
[30:57] when subscribers visit certain pages on
[30:59] the website for example that kind of
[31:00] stuff. It's pretty handy for like signal
[31:02] of whether people are going to buy or
[31:03] not. Uh we have all our support
[31:05] questions on help scout which is another
[31:07] support platform. And then we usually
[31:09] collect kind of like forms through an
[31:11] app called EU form, right? And then
[31:13] there's even more.
[31:14] >> The reason the reason we use euform by
[31:15] the way is because we got this amazing
[31:17] lifetime deal on it many years ago and
[31:19] it's it's been brilliant.
[31:20] >> The truth is you could v code a U form
[31:23] in about 30 minutes I think now. But
[31:25] it's finally
[31:26] >> 30 seconds now probably. Um, honestly,
[31:29] it's so well built and so nice and it
[31:31] integrates with everything. It's just
[31:32] like cool, we just use that.
[31:34] >> But the truth is,
[31:35] >> you know, they even have an AI agent
[31:36] that I now get prompts to copy paste
[31:39] into that agent and it just builds the
[31:40] form for me as well. So,
[31:42] >> okay.
[31:42] >> Okay. Not bad. But yeah, still you could
[31:44] just V code.
[31:45] >> How about you form by the way? Yeah.
[31:46] >> Yeah. So, anyway, we have all that
[31:48] business data living in different
[31:49] places. But the thing is like the story
[31:51] of a customer lives across all these
[31:53] platforms, right? So, it's like they
[31:54] might have some support tickets, then we
[31:56] have some activity data here. we know
[31:58] what they paid on Stripe etc. It's kind
[32:00] of difficult to tell for example like is
[32:01] a customer about to cancel for example
[32:03] which like to tell that you need to be
[32:05] able to know when their payment plan
[32:07] ends for example their level of activity
[32:10] are they subscribed or not to the list
[32:11] did they complain about anything on
[32:13] helps card or like is there any activity
[32:15] from any form that we have and then if
[32:17] you combine all that data you can start
[32:18] telling the story of where this customer
[32:20] is at with your product but individually
[32:22] each of these things doesn't really help
[32:24] you tell the story and so what we v
[32:25] coded was basically just a simple way to
[32:28] send all the data of all these platforms
[32:30] into one big company database that we
[32:32] host on Superbase. You can start for
[32:35] free. We pay $25 per month for that. Uh
[32:37] right now, mostly because we actually
[32:39] process quite a lot of data. Uh and but
[32:41] it's fine like we will be
[32:43] >> I mean that's it's crazy compared to the
[32:44] like the hundreds of thousands of
[32:46] companies pay for some like Oracle or
[32:48] you know one of these big enterprise
[32:50] database systems.
[32:51] >> And that's kind of the thing with small
[32:52] businesses, right? We've always had all
[32:54] that data in all these tools, but we
[32:55] never really made use of it because it
[32:57] just was too much time, too much effort,
[32:58] and too difficult technically to do it,
[33:00] right?
[33:00] >> And because it's in different places.
[33:02] Yeah. It's difficult to do.
[33:03] >> It's just it was difficult like
[33:04] connecting APIs, all of that. It just
[33:05] breaks and you have to update it and you
[33:07] know what I mean? Like and so now we can
[33:09] actually go on code and for example, you
[33:10] know, I said use superbase, which is the
[33:12] database, and tell me how many member
[33:13] subscriptions are expiring this week.
[33:15] And I can tell exactly that there are 14
[33:17] memberships expiring this week. And I
[33:19] can tell, you know, like one that is
[33:20] expiring, so they already cancelled.
[33:22] there is four that are renewing for sure
[33:24] and these are actually unknown. So I
[33:26] would need to dig deep and then I could
[33:27] say like okay which of these members are
[33:29] at risk for example and what it would do
[33:31] would get is it would get the data from
[33:33] circle and it would say which ones did
[33:34] not log in for example in the last 14
[33:36] days or something and we just kind of
[33:37] highlight them to me and I say then
[33:39] please email them and propose them to
[33:41] have a free catchup call with me for
[33:43] example and then all of a sudden I can
[33:45] reactivate these people and they can
[33:46] keep paying me and that was literally
[33:48] three prompts on cloud code now it's
[33:50] connected on the database and so that's
[33:53] what this database does is it allows us
[33:55] to get visib ility and take action and
[33:57] not only us take action but the AI takes
[33:59] action on people basically and we can
[34:02] just optimize our revenue just by being
[34:05] helpful to the right people at the right
[34:06] time basically.
[34:07] >> Yeah. And because that now cloud code
[34:10] has access to that anytime we do
[34:12] something that touches members. So a
[34:14] good example would be the member survey
[34:16] we did a couple weeks ago. So we got
[34:18] about 250 people to reply, fill in like
[34:21] eight or nine questions multiple choice
[34:23] and there was usually we used to do just
[34:25] multiple choice questions on surveys but
[34:27] now because we have AI analyze it we had
[34:29] like an open text field for you know
[34:31] like what could we improve you know the
[34:33] questions like that and it was able to
[34:34] not only analyze that but cross that
[34:36] data against with what was in the
[34:39] superbase database you know what type of
[34:41] member are they how active are they and
[34:43] you know we can see like what are the
[34:45] active people doing what their lifetime
[34:47] big spenders.
[34:48] >> Yeah, exactly. So, it's like you don't
[34:50] just take the survey output, you just
[34:51] actually can wait it for like how much
[34:53] revenue that is for you and which
[34:54] segment you should optimize for that
[34:56] kind of stuff and that changes
[34:57] everything. Basically, you don't just
[34:59] data
[35:00] >> instead of Gail and I, which we were
[35:02] actually doing having like quai
[35:04] arguments about like no our members need
[35:07] this. This is what they want. This is
[35:08] what they hate. This is these are the
[35:10] problems. We're like why are we let's
[35:12] just ask them and then have AI figure it
[35:14] out. And it did.
[35:15] >> It was good. Being able to get that
[35:17] level of insight about your business and
[35:19] your customers and what they need and
[35:21] where you should take your product is
[35:23] invaluable. Every business needs to do
[35:25] that.
[35:25] >> I mean consultants pay like charge
[35:27] literally tens of thousands of dollars
[35:29] to do that and all we did was like a
[35:30] Google
[35:30] >> millions of dollars millions of dollars
[35:32] for like Mckenzie to go into an
[35:34] enterprise.
[35:35] >> Most of our listeners don't hire
[35:36] McKenzie. So probably the level of
[35:38] consultants they will hire will be tens
[35:40] of thousands. Uh
[35:42] >> I'm just saying like the same way um
[35:44] building a lot of infrastructure you
[35:47] know with code was out of reach for
[35:48] small business because code used to be
[35:50] expensive now things like having a not
[35:53] it's not really a consultant but like
[35:56] this level of data analysis it was
[35:58] completely out of reach before because
[35:59] it was so expensive but now everyone can
[36:01] do it. It's a great equalizer.
[36:03] >> Yeah. And just to explain quickly the
[36:06] technical way how it works is basically
[36:08] every time something happens there's
[36:09] something called a web hook in these
[36:11] apps. So for example, Stripe sends a web
[36:12] hook and it's like it sends data to a
[36:14] Cloudflare worker and that Cloudflare
[36:16] worker basically cues it to update to
[36:18] Superbase and then every 15 minutes
[36:20] depending on which APIs it will actually
[36:23] query the API to see if it missed any
[36:26] event basically and it just kind of
[36:27] updates itself and the idea is like the
[36:29] data is constantly updated like every
[36:30] time someone likes a post on Circle,
[36:32] every time someone logs in, every time
[36:34] someone clicks on an email, every time
[36:35] someone opens and we can just reconcile
[36:37] that into member profiles and we get
[36:38] like full data basically. It's very very
[36:40] cool. You should do that if you have any
[36:42] customer data. And one thing about the
[36:44] survey that you didn't mention as well
[36:45] is like the survey was only like seven
[36:47] or eight questions. It was very small
[36:48] which was easy to do for people. But at
[36:50] the same time, because we could cross it
[36:51] over with the data, we got an insane
[36:53] amount of insights actually. And so like
[36:54] it goes well beyond what you imagine
[36:56] when you do that. And you don't even
[36:58] need to know what you're doing. What we
[37:00] did is we're like here's the survey
[37:01] output, use the database and figure out
[37:04] what people want basically and focus on
[37:06] like and help us segment people by
[37:08] revenue activity etc. and do all these
[37:11] segments and that's it and we got it. So
[37:13] yeah, that's pretty powerful. So yeah,
[37:15] you can ask all these questions that who
[37:16] might cancel soon, who applied to our
[37:19] plus level, was that person's full
[37:21] history? And yeah, Cloudflare, we pay $5
[37:23] per month. Superbase, we pay $25 per
[37:25] month. And these APIs are usually
[37:26] included in whatever tool you're paying
[37:29] for. So it's not expensive basically.
[37:31] >> Yeah. And the interesting thing about
[37:33] building on Superbase is you can
[37:36] actually kind of build software within
[37:41] there. Let me sort of talk you through
[37:43] an example here. So they have something
[37:45] called edge functions which is as far as
[37:48] I understand a little bit like a
[37:49] cloudflare worker but it's kind of built
[37:51] directly into superbase.
[37:53] >> Yeah, that's correct.
[37:55] >> Yeah. Am I right there?
[37:56] >> That's correct. That's correct.
[37:57] >> It's waiting to be you don't even know
[37:59] what we built. It's fine. It's true.
[38:01] >> Yeah. This is the point like I don't
[38:03] like
[38:04] >> but it's working right.
[38:05] >> But I still have this work like I built
[38:06] this yesterday in like couple hours. So,
[38:09] we now have a cancellation or refund
[38:12] form on our website. Again, shout out to
[38:15] you form AI uh gave me all the prompts
[38:18] to build this. So, when somebody fills
[38:20] that in uh and they want to cancel their
[38:22] subscription, we get some data and we
[38:24] ask them like why they're cancelling and
[38:26] you know what we could have done to
[38:27] convince them to stay. Very, very useful
[38:29] information to have. So, what happens is
[38:31] they'll fill in that form. Um, we have a
[38:34] quick check to make sure it's not a bot
[38:35] and you know that form's not getting
[38:37] spammed. Um, but then it sends that data
[38:40] into Superbase, but the edge function
[38:44] within Superbase is essentially like
[38:46] this agent that spawns up and starts
[38:48] doing a few different tasks here. So,
[38:50] it's going to look up all the data about
[38:53] that member. So, for example, which
[38:55] courses have they taken, which lessons
[38:56] have they been through, how much have
[38:58] they paid, how long have they been a
[39:00] member, like those types of things. and
[39:01] it's going to use all of that data to
[39:04] then generate a response to their
[39:07] cancellation request. So, you know, if
[39:10] they just want to cancel, like, hey,
[39:12] this isn't for me. I'm not interested.
[39:13] Fine. I'm not going to try and stop
[39:15] anyone. But if they're like, oh, it was
[39:17] too difficult and I couldn't figure out
[39:18] how to do this and this. Then that's an
[39:21] opportunity for us to save that sale and
[39:24] to offer them a solution to that. That
[39:26] may be directing them to the relevant
[39:28] content. that might be, you know, some
[39:30] kind of discount or promotion or some
[39:32] kind of offer that we can give to people
[39:34] that way. And being able to do that in a
[39:37] highly tailored and personalized way is
[39:40] really, really valuable because, you
[39:42] know, we've all been through these
[39:43] cancellation process before and it's
[39:45] like you get a generic, hey, you know,
[39:48] you're trying to cancel, here's a free
[39:49] month or something like that and it's
[39:51] like you don't really care about me.
[39:53] This is just your automation. But in
[39:54] this way, we're giving people a more
[39:57] custom kind of experience of this and
[39:59] kind of really helping them to solve
[40:01] their actual problems in there. So, how
[40:03] that looks at the end is when someone
[40:05] fills in this cancellation form, it has
[40:07] this decision logic in here. So, you
[40:09] know, are they eligible for a refund?
[40:11] What's their the kind of monthly billing
[40:13] uh cadence? You know, those types of
[40:14] things, what's set and what's not. And
[40:16] then it's not going to send them, it's
[40:18] going to draft them a reply. And so,
[40:20] this is a super super basic reply. By
[40:22] the way, I just built this yesterday,
[40:24] but it shows you what you can do with
[40:26] it. And I can just go in there and edit
[40:28] that as I want or just send it as it is.
[40:31] And and we're kind of good to go from
[40:32] there. The edge function itself is
[40:35] receiving the data from the U form. So
[40:38] from the ticket, it's using GPT 5.5 to
[40:41] draft a reply using all of that data and
[40:44] then sending that draft into Help Scout
[40:46] or customer support software. Uh, and so
[40:48] all of that, which would have taken me,
[40:50] you know, 5 10 minutes to do, and I
[40:53] wouldn't even have been able to do all
[40:54] of the stuff in there because there's no
[40:56] way I'm going through all of their data
[40:57] and all of their, you know, view history
[40:59] and lesson history every single time.
[41:01] It's like it's just not feasible to do
[41:03] that. It does all that in literally like
[41:06] seconds. Uh, because it's the edge
[41:09] function sits right inside Superbase, so
[41:11] it can access the data really, really
[41:13] quickly. There's like zero delay there
[41:15] basically. So yeah, this is something
[41:18] that I built on top of the database that
[41:20] Gail set up there.
[41:21] >> Yeah, and that's the thing. We can now
[41:22] start building all these stuff and do
[41:24] that basically. It's really cool. Just
[41:27] wanted to say one thing about the model
[41:29] selection because people were like, "Oh,
[41:31] why are you using GT5.5?"
[41:32] And the reason is because actually GT5.5
[41:35] is actually a very uh efficient model.
[41:38] It's very cheap if you run it in low
[41:42] reasoning and medium reasoning. And I
[41:44] actually have some data to prove it. So
[41:45] this is artificial analysis and a lot of
[41:47] people run on 4.6 which is kind of like
[41:50] considered like a costefficient way to
[41:52] do which is not much cheaper than Opus
[41:54] anymore by the way. Opus is almost the
[41:56] same price was $4,200. But if you run
[41:58] G5.5 in medium or low you can see G5.5
[42:02] medium did the same test for $1,199
[42:04] and low did it for $500 which is pretty
[42:07] good. Uh and it's actually like almost
[42:10] on par. It's almost on par with Gemini
[42:12] 3.5 flash actually if I put it in
[42:14] perspective. So if I put 3.5 flash in
[42:17] there actually 3.5 flash high is here.
[42:19] Yeah, it's actually higher. 3.5 flash is
[42:21] $1,500 and GP 5.5 medium is $1,200. So
[42:25] actually 5.5 if you use it as like not
[42:29] maximum reasoning is actually a pretty
[42:31] good cost efficient model that writes
[42:32] pretty well and is pretty smart
[42:34] basically. So my recommendation right
[42:35] now and I used to recommend flash but
[42:37] flash got expensive is to actually use
[42:40] 5.5 in low or medium reasoning for bang
[42:43] for your buck for API actually. So yeah
[42:45] it's like that's the kind of vibe coding
[42:47] projects I guess that that was the last
[42:49] one right?
[42:49] >> Yeah that's I mean that's everything
[42:51] we've been through quite a lot there but
[42:53] just wanted to kind of give everyone a
[42:55] practical behind thescenes look at the
[42:57] stuff we're actually building hopefully
[42:59] to give you guys some similar ideas
[43:01] really.
[43:01] >> And it's the stuff that's like not
[43:03] flashy. It's kind of internal mostly,
[43:05] but that's what I mean it's allowed us
[43:07] to run this whole thing almost just us
[43:10] because like literally like the product
[43:12] is getting a lot of assistance. The
[43:13] support is getting a lot of assistance
[43:15] and then in the end like we still have
[43:17] to kind of manage a lot and we're in a
[43:18] process of like automating anduling a
[43:21] lot more things now. But in general like
[43:23] that's the kind of like vibe coding
[43:24] projects that you should undertake in
[43:26] your company that will make a
[43:27] difference. It doesn't have beautiful
[43:29] front end. It doesn't have any of that
[43:31] but it actually will save you a ton of
[43:33] time and you just need to learn a few
[43:34] things like learning superbase learning
[43:36] cloudflare workers for example and then
[43:39] playing a little bit with API
[43:40] >> just to be clear you don't need to learn
[43:42] that you need to learn they exist what
[43:44] it does to yeah what it does so that you
[43:47] can kind of talk to AI and it will do it
[43:49] for you
[43:50] >> yeah so like most of these things like I
[43:52] could see when you presented the superb
[43:53] stuff you basically didn't even know
[43:55] >> yeah like I don't really know what it is
[43:58] >> it's probably worse like you know all
[44:00] these tools both code and codeex they
[44:02] have security review plugins it's
[44:04] probably worth running your code through
[44:06] that if you're vi coding these things it
[44:08] will help there are special tools as
[44:10] well there's tools like code rabbit etc
[44:11] that help catching issues but the truth
[44:13] is the best models like don't use a
[44:15] cheap model but the best models they
[44:16] have a lot less security flows now than
[44:18] they used to have like these kind of
[44:19] like nightmares of vip coding etc it's
[44:21] not as bad as it used to be doesn't mean
[44:23] it can't exist doesn't mean you
[44:24] shouldn't check but it's less much much
[44:26] less likely than it used to be even a
[44:28] year ago
[44:28] >> and you can We're still quite cautious
[44:30] around things like look, it's not
[44:32] sending messages and support. It's
[44:34] drafting them. It's not it has no access
[44:36] to payments or, you know, anything like
[44:38] that.
[44:39] >> Uh so, you know, there's there's some
[44:41] hardcoded like walls that it just can't
[44:44] do and can't get access to, but we're
[44:46] generally quite cautious about this
[44:47] stuff. We're not vibe coding our
[44:48] shopping cart software. We're using
[44:51] like, you know, established companies to
[44:53] do that. So,
[44:55] >> yeah. I mean, I think sometimes what
[44:57] pisses me off is on social media, even
[45:00] on YouTube, a lot of the examples that
[45:03] people share are like, "Here's how I
[45:06] create content or do some like flashy
[45:08] visual thing using AI." But the truth is
[45:12] 90% of businesses out there, they're not
[45:15] content businesses. They're not social
[45:18] media influencers. they have a product
[45:21] or a service and they kind of like
[45:22] deliver that and it's it's kind of a bit
[45:24] boring sometimes and it's that boring
[45:26] stuff that you need to work on
[45:29] automating because that is the core of
[45:31] your business. you automate this stuff
[45:33] and then you make content still
[45:35] involving yourself because I think
[45:37] that's the hardest thing like sure you
[45:38] can do as love you can make like a baby
[45:40] podcast and then you get lots of views
[45:42] on Tik Tok you won't make much sales if
[45:44] you want to make sales and if you want
[45:45] to sell stuff it actually is worth doing
[45:48] the human stuff that people connect with
[45:50] still like with AI assistance but like
[45:52] not necessarily fully automated I don't
[45:53] make like a clone of myself on a gen and
[45:55] post videos about that for example and
[45:57] then just basically take everything else
[45:59] away with AI and that part is almost
[46:02] invisible to people and so you're not
[46:04] dropping your quality, you're not
[46:06] discounting your brand or anything like
[46:07] that and things like the database. Yeah,
[46:09] if anything it makes the experience
[46:11] better for people. So that's what you
[46:13] should focus on. I know we get a lot of
[46:15] people like how do I make content with
[46:17] AI? I reluctantly do a little bit of it,
[46:19] but I'm not a big fan because I actually
[46:21] think that's not what they should focus
[46:22] on. Uh what they should focus on is
[46:24] automating what they sell and all the
[46:27] service layer around what they sell. And
[46:29] then the content part is now you have
[46:31] time to do it and then you actually have
[46:33] a chance because most people who like
[46:34] fully automate their content with AI
[46:36] like point to me apart from a few
[46:39] YouTube channels or Tik Tokers or
[46:40] whatever there's not a lot that
[46:42] >> but even then they have the high high
[46:44] views but like are they really you know
[46:46] like making a lot of money and selling a
[46:47] lot of product off the back of that.
[46:49] >> Everyone dreams of doing that. I mean,
[46:51] sure, with SEO show, I'm sure you can
[46:52] point at some of it, but like for
[46:54] anything else, like, I'm sorry, but
[46:56] like, show me a real business channel
[46:58] that makes a lot of money with the fully
[47:01] AI generated content. However, show me
[47:03] businesses that v code these kind of
[47:04] projects. We show many of them,
[47:06] actually. So, yeah, that's the final
[47:08] words of wisdom, I guess.
[47:09] >> Okay, brilliant. Well, thanks for tuning
[47:11] in to this episode of the podcast. We're
[47:13] only really able to go in depth with
[47:16] this stuff in a long format piece of
[47:18] content like a podcast like this. So,
[47:21] thanks. It's an hour long. Appreciate
[47:23] you staying to the end. Make sure you're
[47:24] subscribed because we're going to be
[47:26] doing a lot more episodes like this. If
[47:28] you enjoyed it, head on over to our
[47:30] YouTube channel. Um, just search for
[47:32] Authority Hacker, find the episode
[47:34] there, and leave us a comment. Tell us,
[47:36] do you like this type of format? Do you
[47:38] want us to show us more quote unquote
[47:40] boring automations uh from our business
[47:43] and things that you could do as well in
[47:45] your business like this? We'd love to
[47:46] hear your feedback on that. So, thanks
[47:48] for listening and we'll see you again
[47:50] next week for another
