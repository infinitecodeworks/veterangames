#!/usr/bin/env python3
"""Build the Veteran Games static site.

Run from anywhere:  python3 _src/build.py
Writes plain HTML into the repository root. No dependencies beyond Python 3.
Edit content in this file, re-run, commit. GitHub Pages serves the result.
"""
import os
import posixpath
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_src")
DOMAIN = "https://www.theveterangames.co.uk"
YEAR = "2026"

NAV = [
    ("games.html", "The Games"),
    ("wellbeing.html", "Wellbeing"),
    ("team.html", "Team"),
    ("partners.html", "Partners"),
    ("archive/index.html", "Archive"),
    ("app.html", "App"),
    ("contact.html", "Contact"),
]

# --------------------------------------------------------------------------
# Archive content
# --------------------------------------------------------------------------

PRESS = [
    dict(
        slug="its-changed-my-life-british-and-israeli-veterans-compete-at-inspirational-veteran-games",
        title="“It’s changed my life”: British and Overseas veterans compete at inspirational Veteran Games",
        source="Jewish News", img="it-s-changed-my-life.jpg",
        teaser="Over 60 British veterans travelled with their families to participate in the Veteran Games.",
        url="https://www.jewishnews.co.uk/its-changed-my-life-british-and-israeli-veterans-compete-at-inspirational-veteran-games/",
        body=[
            "Over 60 British veterans this week with their families to participate in the Veteran Games. The five-day trip also includes family time at the Dead Sea and visiting Jerusalem.",
            "“I was always proud of him.” Travis Eagersham is watching his dad, Phillip, helping another British veteran with his skills at the shooting range.",
            "It’s clear that there’s a strong bond between the two. Phillip is one of more than 60 British veterans who came with their families to compete in the annual Veteran Games, an event initiated and organised by the charity Veteran Games and supported by philanthropic donations from the UK.",
        ]),
    dict(
        slug="johnny-mercer-praises-wounded-veterans-competing-at-veteran-games",
        title="Johnny Mercer praises wounded veterans competing at Veteran Games",
        source="Forces News", img="johnny-mercer-praises.jpg",
        teaser="Minister for Veterans' Affairs Johnny Mercer, an ex-Army Captain, was present at the event on the first day of competition where he presented medals to some athletes.",
        url="https://www.forces.net/military-life/veterans/its-amazing-enterprise-johnny-mercer-praises-wounded-veterans-competing",
        body=[
            "Veterans from the UK and overseas have gathered for the third annual Veteran Games, a multi-sport friendly competition between veterans.",
            "The five-day sports competition brings together wounded, sick and injured veterans from the UK and overseas to compete in events in swimming, shooting and CrossFit.",
            "Minister for Veterans' Affairs Johnny Mercer, an ex-Army Captain was present at the event on the first day of competition where he presented medals to some athletes.",
        ]),
    dict(
        slug="i-cage-fight-to-relax-and-was-a-royal-marine-commando-but-this-is-my-biggest-fear",
        title="I cage fight to relax and was a Royal Marine Commando – but this is my biggest fear",
        source="The Independent", img="i-cage-fight-to-relax.jpg",
        teaser="A Veteran Games featured insight into mental health and depression.",
        url="https://www.independent.co.uk/voices/veteran-games-mental-health-depression-b2347670.html",
        body=[
            "“Come on, mate. You’re a 6ft 2in, 95kg Welshman built like a brick proverbial,” I tell myself. “You cage fight to relax. You were a Royal Marine Commando for seven years. You hiked 30 miles over Dartmoor in full fighting gear to win your green beret. And now you’re scared of 15-year-olds? Get some perspective!”",
        ]),
    dict(
        slug="ex-raf-policewoman-with-ms-to-compete-at-veteran-games",
        title="Ex-RAF policewoman with MS to compete at Veteran Games",
        source="BBC News", img="ex-raf-policewoman.jpg",
        teaser="Ann Hughes, from Shifnal in Shropshire, was among 65 British wounded, sick and injured armed forces veterans at the event.",
        url="https://www.bbc.co.uk/news/uk-england-shropshire-65698080",
        body=[
            "An RAF veteran with multiple sclerosis is among those taking part in this year's Veteran Games. Ann Hughes, from Shifnal in Shropshire, will be among 65 British wounded, sick and injured armed forces veterans at the event, starting on Saturday.",
            "Ms Hughes, 53, who was an RAF policewoman for 20 years, was diagnosed with secondary progressive MS in 2007. She said she was “most looking forward to meeting other veterans”.",
            "Her condition affects her sight and mobility and causes muscle spasms and severe fatigue. She uses a crutch or a wheelchair to travel longer distances. At the games Ms Hughes will represent the RAF Benevolent Fund, which housed her in 2009 and made the necessary adaptations to make her home more accessible.",
        ]),
    dict(
        slug="veteran-games-brings-soldiers-together",
        title="Veteran Games brings soldiers together",
        source="Daily Mail (video)", img="veteran-games-brings-soldiers-together-daily-mail.jpg",
        teaser="Daily Mail video reel on Facebook Watch.",
        url="https://fb.watch/kU0Kx_scfe/",
        link_label="Watch the video on Facebook",
        body=["A Daily Mail video reel about the Veteran Games, published on Facebook Watch."]),
    dict(
        slug="changed-my-life-inside-the-veterans-games-where-injured-heroes-compete-against-other-soldiers-to-help-with-their-recovery",
        title="“Changed my life”: inside the Veterans Games where injured heroes compete against other soldiers to help with their recovery",
        source="The Sun", img="lifting-the-barbell.jpg",
        teaser="Former Royal Marine commando Mitchell Singleton, 59, who served in the Falklands War, knew he had come a long way in his recovery.",
        url="https://www.thesun.co.uk/news/22538569/veterans-games-injured-heroes-compete-soldiers-help-recovery/",
        body=[
            "Lifting the barbell proudly above his head, former Royal Marine commando Mitchell Singleton knew he had come a long way in his recovery.",
            "The 59-year-old, who served in the Falklands War and in Iraq, is one of a 60-strong team chosen by British military charities for the Veterans Games.",
            "Unlike other events such as the Invictus Games, competitors aren’t required to qualify, instead charities choose veterans most in need of uplifting.",
            "Veterans Minister Johnny Mercer paid a visit to the Games, where the Brit heroes compete against overseas veterans across different disciplines including swimming and cross fit.",
            "Among the heroes was Craig Lundberg, 37, from Liverpool, who lost his sight in a rocket grenade attack in Iraq.",
        ]),
]

NEWS = [
    dict(
        slug="competing-in-israel-gave-me-back-my-pride",
        title="“Competing gave me back my pride”", img="news3.jpg",
        teaser="Britain’s veterans minister hailed the way Israel honours its military veterans as injured UK servicemen and women spoke of how the Games had transformed their lives.",
        body=[
            "Britain’s veterans minister hailed the way Israel honours its military veterans last night as injured UK servicemen and women spoke movingly of how taking part in an historic sporting event with their Israeli counterparts had transformed their lives.",
            "It came during the launch of the second Veteran Games and Conference. In 2019, the charity took 60 injured Brits to Israel to take part in a four days of sporting competition with Israelis who had also lost limbs or suffered post-traumatic stress as a result of conflict. Joined by their spouses and children, they also had an opportunity to spend quality time together, build friendships that have lasted until today and tour some amazing sites.",
        ]),
    dict(
        slug="after-the-veteran-games-i-feel-i-can-achieve-anything",
        title="“After the Veteran Games, I feel I can achieve anything”", img="news1.jpg",
        teaser="Heroes of the third Veteran Games returned to the UK with tales of “miracles” after a week of building confidence, enhancing family bonds and making lifelong friends.",
        body=[
            "Heroes of the third Veteran Games returned to the UK this week with tales of “miracles” after a week of building confidence, enhancing family bonds and making lifelong friends.",
            "Sixty-two wounded veterans returned from the event where they competed in swimming, X-fit and shooting. The spectacle – organised by Veteran Games and supported by communal philanthropists – also involved the families who are often key to rehabilitation.",
        ]),
    dict(
        slug="uk-veterans-travel-to-israel-for-veteran-games",
        title="UK veterans travel for Veteran Games", img="news2.jpg",
        teaser="65 British wounded, sick and injured Armed Forces veterans travel with their families to compete with counterparts battling identical challenges.",
        body=[
            "First held in 2019, this event will see 65 British wounded, sick and injured Armed Forces veterans travel with their families where they will compete with their counterparts who are battling identical challenges.",
            "The Veteran Games recognise the fundamental role played by sport and family in supporting the ongoing recovery of veterans who have suffered physical and psychological challenges as a result of serving their country.",
            "Veterans will compete in a variety of sports while learning how their respective countries provide care for those wounded, sick and injured in the service of their country. Families will have the chance to meet and share common experiences in a relaxed and supportive environment while enjoying social activities and cultural events that will provide an insight into Israel’s rich heritage and history.",
        ]),
]

LETTERS = [
    dict(slug="jonathan", name="Jonathan",
         teaser="I want to thank you from the bottom of my heart for organising and delivering the second Veteran Games and Conference, and for welcoming me to them with Jane.",
         body=[
             "Dear Andy",
             "I want to thank you from the bottom of my heart for organising and delivering the second Veteran Games and Conference, and for welcoming me to them with Jane.",
             "You will have seen the feedback on social media from those who attended, so will be under no illusion as to the life-changing impact they have made on the British veterans and families who attended. I’d go as far as saying (maybe having forgotten the feedback in 2019) that these Games made even more positive impact on the participants: once again, the principle of not having to qualify to compete was extremely significant and made a profound positive impact on those who were daunted by the prospect of sporting competition against the Israeli veterans, who were quickly put at ease and came away knowing they could indeed achieve, overcoming their own lack of self-confidence. There’s no doubt that those returning will face their daily challenges with a far more positive outlook and determination.",
             "Your organisation along with Spencer and Karina was as before simply superb, and you had clearly reflected carefully on lessons learned in 2019 to make the physical demands on the families less exhausting. The programme was still full on, but I don’t think anyone was overwhelmed, and nobody I have spoken to would have swapped a moment for more sleep or another afternoon on the beach.",
             "Once again, the Games reunited those of the same cap badge who had fallen apart, and rekindled friendship which means they will care for each other more closely going forward. Once again new friendships were made with those of differing units which will be enduring. Once again, friendships were made with comrades which I hope will last.",
             "Once again the welcome provided was absolutely outstanding, and the warmth of that welcome each day by every staff member. The Conference was extremely useful, bringing together British SMEs who actually don’t meet in the UK, as well as giving them a chance to hear from the Israeli attendees. I learned much, and will be following up with a number of the participants back in the UK, as did Jane for her work with school pupils, an unexpected bonus.",
             "The Games host team were just as wonderful as last time, perhaps even more so, achieving just the right measure of firmness in getting everyone where they were meant to be at the right time, along with getting to know the attendees and supporting them.",
             "But let me finish by feeding back to you the comments I have received from wheelchair-bound attendee Martin K, which for me demonstrates just how much your trouble to ensure that all are included, demonstrating that no-one cannot be catered for:",
             "“I know I caused many headaches in the lead up to the event with the uncertainty about my being prepared to take part, but thank God I did, because it truly was an amazing, once in a lifetime experience. The whole trip was outstanding, both from an organisational point of view, and an experience for the veterans and their families. The experience of meeting and spending time exchanging experiences of our recovery process with other veterans and their families was extremely beneficial to all concerned and I have learned so much from the experience and formed new friendships.”",
             "We really are still buzzing about the whole weeks experience, outstanding!!",
             "It was great to see you again, hoping we can catch up soon in England!",
         ], sign=["Every good wish as ever", "Jonathan"]),
    dict(slug="michael-and-nicola-bassett", name="Michael and Nicola",
         teaser="Thank you from the bottom of our hearts for the incredible week that you hosted for the UK Veterans. The visit surpassed any expectations we held.",
         body=[
             "Dear Spencer,",
             "Thank you from the bottom of our hearts for the incredible week that you hosted for the UK Veterans. The visit surpassed any expectations we held. The smiles and laughter are imprinted in my mind forever. We returned reinvigorated, inspired, hopeful and humbled. Not to mention the many new friends we have met.",
             "Michael & I live in Northern Ireland and served here in the Army. Caroline was injured on duty in Northern Ireland. We met by pure chance in London in 2019 and instantly became close friends. My greatest wish is to have Caroline visit our home and meet the decent humans who are grateful for the protection the military provided us in our hour of need, despite what the mainstream media report. Caroline and I share a passion in spreading hope to other wounded veterans all over the UK.",
             "I am travelling to Waterloo Battlefield in early July with a team from Anglia Ruskin University in conjunction with the Waterloo Uncovered charity to make a film about how archaeology helps veterans in their recovery. I have learnt so much from my time at the Veteran Games and will be using these lessons in the film production. We are certainly going to show the benefits of bringing veterans of other nations together and to see the gulf in the care provided by respective governments. Hopefully Mr Leo Docherty picked up a few ideas too.",
             "Once again THANK YOU to everyone involved in the Veterans Games 2022.",
         ], sign=["Michael and Nicola"]),
    dict(slug="helen-helliwell", name="Helen",
         teaser="I just wanted to drop a line to congratulate you all on such a fantastic week and to say a huge thank you to each of you.",
         body=[
             "Dear Spencer, Andy and Karina,",
             "I just wanted to drop a line to congratulate you all on such a fantastic week and to say a huge thank you to each of you:",
             "Spencer – your vision for these games, generosity, sheer energy (and dance moves) will long stay with me!",
             "Andy – your organisation of the event, making it look so easy and remaining so calm – a true Royal.",
             "Karina – thank you so much for sorting out the conference and all that goes with that – particularly my last minute zoom intervention!",
             "The programme was superbly organised and incredibly rich; I think we all really enjoyed the mix of conference / sport / cultural programme and the opportunity to engage with colleagues, competitors and their families.",
             "The visits programme certainly gave the Games a unique perspective into the host country, and something I don’t think any other international Games does. I can only imagine the amount of organisation this took and the team absolutely nailed it. The generosity of the sponsors too, in making this an experience that we will all remember for a long time to come.",
             "What was really valuable for me though, was just having that quality time with the veterans and their families, to really hear about their experience and what I can do from a Defence Policy perspective, to make it better – I’m actively pursuing a few things with my team which I think will bring long lasting benefits to many. So a huge thank you again, and wishing you all the very best,",
         ], sign=["Helen", "Director – People – AFPPol"]),
    dict(slug="pete", name="Pete",
         teaser="Wanted to send you a heartfelt thank you from my family and I for this week. It has been such an experience we will not forget!",
         body=[
             "Hi Karina,",
             "Wanted to send you a heartfelt thank you from my family and I for this week. It has been such an experience we will not forget!!",
             "Last night was emotional for personal reasons, seeing myself and what Shlomi and his team did made me cry.",
             "I’ve never sat and told my story as in depth as I did with them & to be told I’m an inspiration from them was such an honour. I did tell them last night but if you could let them know again that would be appreciated!! Thank you for helping sort out our daughter after her accident, from bottom of our hearts, to you & all the staff.",
             "Thank you again and sorry didn’t get to give you a hug goodbye, but hopefully our paths cross again? If I could repay in anyway I would, and would love to/jump at the chance to help as an ambassador if that’s possible?",
             "Let me know if that is something I can do, and what you need from me.",
             "Thanks and thanks again, all our love the Lauder family.",
         ], sign=["Cheers", "Pete"]),
    dict(slug="alistair-roos-allsop", name="Alistair",
         teaser="Congratulations and thank you for delivering the awesome Veteran Games 2022; your passion and dedication shone through.",
         body=[
             "Andy,",
             "Congratulations and thank you for delivering the awesome Veteran Games 2022; your passion and dedication shone through, and I hope that you too had the opportunity to see the joy that the games and experience brought to the veterans, their partners, and their children. I often say that I have the best job in Medicine, in some cases I have been fortunate to work with the patient prior to injury, treat the patient on the battlefield, support them through their recovery and rehabilitation, see them transition out of Service and start a new life. It is humbling to see how successful they have been, to catch up with their wives and meet their children many of whom were babies when I last met them. To be able to recognise the family sacrifices and indeed courage is special. I will always remember the pride from being ‘roped’ into playing water polo alongside both Lee’s and Frazer’s children. There is a bond that links all veterans irrespective of background, nationality, age or gender and the balance of competition and inclusivity was perfect for everyone to gain a ‘victory of their impairment’.",
             "The Conference was a perfect setting to try to develop and focus close working practices; many of my patients are part of the Advance Study (one of the presentations) and to be able to feed back their frustrations is crucial. Helen Helliwell and Leo Docherty MP both plan to visit later this year to follow up our discussions; it has been a great opportunity for Joe Winch in particular to present how some areas of policy have unintended consequences and how it impacts on his recovery.",
             "I feel privileged to have been part of it. Thank you. I would be very grateful if you pass on my thanks to Spencer and Karina; as a team you were awesome.",
         ], sign=["Alistair"]),
    dict(slug="carra-stuart-sophie-ben", name="Carra, Stuart, Sophie & Ben",
         teaser="I want to personally thank you from the bottom of my heart for what this trip has done for myself and my family.",
         body=[
             "Spencer,",
             "I want to personally thank you from the bottom of my heart for what this trip has done for myself and my family. The last few years have been so very difficult. My children & husband, Stuart have had to pick me up when I have fallen down whilst watching me struggle to complete even the simplest of tasks, they have held my hand as I have cried in pain day after day, even had to wash and dress me after I have been through surgery after surgery but they have always remained strong for me. They have never once complained.",
             "Throughout the Veteran Games we have come to realise that we are not alone, we have been able to see that so many other people have similar struggles but everyday they continue to smile, proving that life is what you make it, life is fun. For myself, I’ve proven that I can still do things I didn’t even know I could, I have learnt that I am strong, with the support of family & friends around me I can achieve anything. Having been injured and discharged from the Royal Navy some 19 years ago which ended my career, prompting Stuart to leave to provide me with the care and support I now needed has made both myself and Stuart feel so far removed from the life we once knew as serving members of the Armed Forces, serving our country with pride and passion. We felt alone and isolated.",
             "The Games have given us both a renewed faith in a community that we were once a part of. Having the opportunity to share with our children the camaraderie, the team work and the fighting spirit the Armed Forces are renowned for has been so incredibly important to us and none of this would have been possible without you and your altruistic team, the sponsors, the charities and the other veterans who I am proud to now call my friends. The memories of the week and the immense amount of work and effort that went into making the trip so special will stay with us all forever. The close bonds that were made between us all will last a lifetime.",
             "It would be amazing to be able to stay in touch and who knows, maybe we will meet up again in the near future.",
         ], sign=["Kind regards,", "Carra, Stuart, Sophie & Ben"]),
    dict(slug="jason-hare", name="Jason",
         teaser="The trip was by far one of the best experiences I have ever been on, especially as I was able to be with my youngest daughter.",
         body=[
             "Dear Phil, Jonathan and Andy,",
             "Straight back into work for me on return from the Veteran Games, to deliver an intensive course up here then a quick turnaround for a very big charity fundraising event in London. So my apologies for the lateness of this message but it has given me time to reflect with my daughter on some terrific memories of a fantastic event. The trip was by far one of the best experiences I have ever been on, especially as I was able to be with my youngest daughter. At 11 years of age she was able to meet up with some of her Dad’s old friends and their families which was just brilliant, and get involved in so many family based activities. My youngest made so many friends and enjoyed every minute of the adventure. For the competitors, it allowed us to rekindle that camaraderie and athletic competitive spirit which is often lost after service, as we get older and due to circumstances and in many cases restricted by our careers, jobs and livelihoods. But we got the opportunity to throw our hats into the ring once more.",
             "The games were incredible and I was so proud to be a part of them with such likeminded veterans as well as so many people I knew and had served with within the Corps. Truly special and very inspirational. The hospitality shown to us was second to none and was always heart-warming and heartfelt by everyone involved. A truly magical experience and something that will be remembered by myself and my daughter for the rest of our lives. After losing a lot of very close family members and friends, coupled with covid, things personally have been a little strained. My relationship with my youngest has been at the forefront of my mind due to her age during all this. This week away gave us the ability as father and daughter to bond even closer. To share things, to talk, to enjoy adventurous activities, create happy memories, spend quality time together and make unique experiences which will last a lifetime for us. For that I am truly thankful to all of you, I really am. That to me was so very important and down to you, and the experience, knowledge, leadership, organisation skills, patience, heart and passion of all involved in the Veterans Games 2022. We had the best trip a father and daughter could ever have. Thank you so much!",
         ], sign=["Kind regards,", "Jason", "Director of Courses"]),
    dict(slug="anthony-lock", name="Anthony",
         teaser="I would like to start by thanking you, the entire team and the sponsors for the outstanding work you do for veteran communities.",
         body=[
             "Dear Spencer,",
             "I would like to start by thanking you, the entire team and the sponsors for the outstanding work you do for veteran communities.",
             "I should have waited before emailing you to allow me to fully digest everything I have just seen, done and participated in during the Veteran Games 2022. The truth is in a few days time it will be my thirteenth anniversary of the day my world crashed down and rather than things easing over time it seems to get harder.",
             "I was unfortunate enough to have been blown up twice in the space of six weeks in Afghanistan and unknowingly broke my neck in the first blast. Then, just a few weeks later I woke from a coma to be told that I had been blown up again but this time my life had changed forever. After suffering many serious life changing injuries I found myself isolated and cut off from the support and rehabilitation I should have received and found life incredibly discriminating and woeful. Instead I headed downhill on a collision course with death. My mind and my body was Broken By War. For six years I was alone with just my wife and daughter to live for. The military had left me to rot and many of the big charities also. I found myself fighting to survive, clinging on for my family. I had attempted to end my life many times but could not find the strength to end it.",
             "I was saved by The Not Forgotten Charity in 2019.",
             "They invited a broken, lost and forgotten man into their charity. Before finding this charity I sadly had to share my story to be found. I wrote an extremely powerful book called Broken By War. The book inspired many people across the world to reach out for help including our younger generation. I proudly beat many to claim second at the English Veteran Awards for inspiration, not bad for a Welshman. A 15 year old boy became so inspired by my story went on to win ITV’s Good Morning Britain Young Loneliness Award. However it wasn’t the book or praise I was after it was help. That’s where The Not Forgotten Stepped in. Unaware of my book they were informed from someone who had read my book of me. Sadly I hadn’t heard of the charity before they made contact with me, but they did and they saved my life.",
             "I was invited along to the games at short notice as someone withdrew in April. I suffer badly with CPTSD and my nerves and anxiety are through the roof. Because I trusted The Not Forgotten this empowered me to push myself out of my comfort zone and make the trip. I wasn’t in shape due to the notice given but knew I had some fight still inside my broken body. On seeing the size of some of the athletes on the trip especially those stood either side of me in the swimming I was petrified but not defeated. Throughout the week I found so much strength, love and compassion from everyone, that I’m sat at home still smiling. I didn’t need to win a medal, instead I won a confidence battle and found love for a veterans community I felt no part of before I made the trip.",
             "I return home with hope, hope that my newfound confidence will enable me to change my life. This is down to you and every member of staff from the events team right down to the bus drivers and the sponsors. You are all amazing human beings.",
             "One day if I ever have the chance to return, I would not hesitate. I will return stronger and a genuine medal contender, but Spencer you would have to make me a promise that my kit will be medium in size. I would be honoured to send you a signed copy of my book Broken By War as a sincere thank you for everything you do.",
         ], sign=["Yours sincerely", "Anthony", "Broken By War"]),
    dict(slug="steve-richards", name="Steve",
         teaser="Please accept my personal thanks and that of my fellow Royal Marines for all your extraordinary hard work and good humour. Your vision is delivering in spades.",
         body=[
             "Dear Spencer,",
             "Please accept my personal thanks and that of my fellow Royal Marines for all your extraordinary hard work and good humour. Your vision is delivering in spades. You and your team have changed lives and we are all the better for the experience. Veteran Games is a world leader and the UK and overseas teaming up will benefit our veterans immensely. I have returned reinvigorated and ready to continue my own rehab as have many others. It was a pleasure to meet you and Karina, of course Andy Garland. We have known each other for over 30yrs, and the perfect man for the job, but you know that! Competing and making new friends on the way was a very special moment in my life. I have agreed to stay in touch with many of the Israeli veterans I met and we swapped many stories of shared experiences. I also had the chance to bond with my daughter after too much time apart.",
         ], sign=["Until we meet again, our utmost thanks from me,", "Steve, Emma and the veterans of Her Majesty’s Royal Marines Commandos."]),
]

QUOTES = [
    ("I think that this week has brought people together and allowed that osmosis of knowledge and experience sharing so people know that they aren’t alone.", "David", "Conference participant"),
    ("In our effort to provide a global gold standard there are definitely insights to be gained from the first-class provisions available.", "Leo Docherty MP", "Then Minister for Defence People and Veterans"),
    ("It’s taken me a while to digest all your kindness. I cannot thank you and everyone involved enough. I have hope again. I have found a new strength. You and the team made this happen. I have found my smile again. Thank you so much.", "Anthony", "Conference participant"),
    ("Veteran Games is a world leader and will benefit our veterans immensely. I have returned reinvigorated and ready to continue my own rehab as have many others.", "Steve", "The Royal Marines Charity"),
    ("When I arrived, I was a shell of the person I am now, I just hope I can take it forward. It’s down to the amazing support we’ve received and being part of a community again, like when we served.", "Amanda", "SSAFA"),
    ("It was truly inspiring to meet other veterans and humbling to learn about their experiences. Everyone had different abilities – there were people in wheelchairs, those who were blind or had other disabilities. But there was a real sense of pride in what they were doing, and they all refused to give up.", "Fraser", "Veterans Scotland"),
    ("These games, these amazing veterans’ games do just that. They restore the pride we once felt when we wore our military uniforms. That pride we once had, being part of a troop, a detachment, a Corps. They give us the opportunity to create new friendships; they give us understanding of what other veterans in other countries have experienced, and how they have been supported in their rehabilitation. They give us the chance to meet with each other’s families in a safe, friendly space to talk about the challenges we all face and how we can continue to support each other. And they give us wonderful, lifelong memories.", "Caroline", "The Not Forgotten Association"),
]

CHARITY_PARTNERS = [
    ("Blesma", "https://blesma.org", "partner-blesma.png"),
    ("Blind Veterans UK", "https://www.blindveterans.org.uk", "partner-blind-veterans.png"),
    ("Felix Fund", "https://www.felixfund.org.uk", "partner-felix-fund.png"),
    ("Legion Scotland", "https://www.legionscotland.org.uk", "partner-legion-scotland.png"),
    ("Poppyscotland", "https://www.poppyscotland.org.uk", "partner-poppyscotland.png"),
    ("RAF Benevolent Fund", "https://www.rafbf.org", "partner-rafbf.png"),
    ("Rock2Recovery", "https://www.rock2recovery.co.uk", "partner-rock2recovery.png"),
    ("The Royal Marines Charity", "https://rma-trmc.org", "partner-royal-marines-charity.png"),
    ("SSAFA", "https://www.ssafa.org.uk", "partner-ssafa.png"),
    ("The Not Forgotten", "https://thenotforgotten.org", "partner-not-forgotten.png"),
    ("Veterans Scotland", "https://veteransscotland.org.uk", "partner-veterans-scotland.png"),
]

SPONSORS = [
    ("The Charles Wolfson Charitable Trust", "sponsor-charles-wolfson.jpg"),
    ("Chelsea FC Foundation", "sponsor-chelsea-foundation.jpg"),
    ("Forces Children’s Trust", "sponsor-forces-childrens-trust.jpg"),
    ("Future Directions Foundation", "sponsor-future-directions.png"),
    ("The Gerald and Gail Ronson Family Foundation", "sponsor-ronson.png"),
    ("Patron Charitable Initiatives", "sponsor-patron.jpg"),
    ("Pears Foundation", "sponsor-pears.png"),
    ("Rachel Charitable Trust", "sponsor-rachel-trust.png"),
    ("Regatta Professional", "sponsor-regatta.png"),
    ("The Exilarch’s Foundation", "sponsor-exilarchs.png"),
    ("The Maurice Wohl Charitable Foundation", "sponsor-maurice-wohl.png"),
    ("The Wolfson Family Charitable Trust", "sponsor-wolfson-family.png"),
]

COMMUNITY = [
    ("Entrain", "https://entrainspace.co.uk/", "community-entrain.png"),
    ("Virgin Atlantic", "https://www.virginatlantic.com/", "community-virgin-atlantic.png"),
    ("Give Us Time", "https://giveustime.org.uk/", "community-give-us-time.png"),
    ("Royal Marines Association Golf Society", None, "community-rma-golf.png"),
    ("Woody’s Lodge", "https://www.woodyslodge.org/", "community-woodys-lodge.png"),
    ("Commando Force Airsoft", "https://www.commandoforceairsoft.com/", "community-commando-force-airsoft.jpg"),
]

# --------------------------------------------------------------------------
# Rendering helpers
# --------------------------------------------------------------------------

def e(s):
    return escape(s, quote=True)


def rel(page, target):
    """Relative URL from output file `page` to site path `target`."""
    base = posixpath.dirname(page)
    path, _, frag = target.partition("#")
    r = posixpath.relpath(path, base or ".")
    return r + ("#" + frag if frag else "")


def paras(items):
    return "\n".join(f"<p>{e(p)}</p>" for p in items)


def layout(page, title, body, desc="", current=None):
    R = lambda t: rel(page, t)
    nav_items = "\n".join(
        f'<li><a href="{R(href)}"{" aria-current=\"page\"" if href == current else ""}>{label}</a></li>'
        for href, label in NAV
    )
    full_title = "Veteran Games and Conference" if title is None else f"{title} | Veteran Games and Conference"
    canonical = DOMAIN + "/" + ("" if page == "index.html" else page.replace("index.html", ""))
    desc = desc or "The Veteran Games and Conference brought together wounded, sick and injured UK veterans and their families with their overseas counterparts for sport, conversation and culture."
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{e(canonical)}">
<meta property="og:title" content="{e(title or 'Veteran Games and Conference')}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{DOMAIN}/assets/img/games-15.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="{R('assets/img/logo.png')}">
<link rel="preload" href="{R('assets/fonts/libre-franklin-800.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{R('assets/css/style.css')}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{R('index.html')}"><img src="{R('assets/img/logo.png')}" alt="" width="62" height="62"><span>Veteran Games<br>and Conference</span></a>
    <nav class="nav" aria-label="Main">
      <ul>{nav_items}</ul>
      <details><summary>Menu</summary><ul>{nav_items}</ul></details>
    </nav>
  </div>
  <div class="rule" role="presentation"></div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <h2>Veteran Games and Conference</h2>
      <p>Registered Charity No. 1202198<br>Suite 3, One Bridge Lane<br>London NW11 0EA</p>
      <p class="small" style="color:#b9bcd3">&copy; {YEAR} Veteran Games and Conference</p>
    </div>
    <div>
      <h2>About</h2>
      <ul>
        <li><a href="{R('games.html')}">The Games</a></li>
        <li><a href="{R('wellbeing.html')}">Wellbeing Programme</a></li>
        <li><a href="{R('team.html')}">Team</a></li>
        <li><a href="{R('partners.html')}">Partners and sponsors</a></li>
      </ul>
    </div>
    <div>
      <h2>More</h2>
      <ul>
        <li><a href="{R('archive/index.html')}">Archive</a></li>
        <li><a href="{R('members.html')}">Members&rsquo; web app</a></li>
        <li><a href="{R('contact.html')}">Contact</a></li>
        <li><a href="{R('privacy.html')}">Privacy</a></li>
      </ul>
    </div>
  </div>
</footer>
</body>
</html>
"""


def img(page, name, alt, w=None, h=None, lazy=True, cls=""):
    attrs = f' class="{cls}"' if cls else ""
    size = f' width="{w}" height="{h}"' if w and h else ""
    return f'<img src="{rel(page, "assets/img/" + name)}" alt="{e(alt)}"{size}{" loading=\"lazy\"" if lazy else ""}{attrs}>'


def write(page, html):
    path = os.path.join(ROOT, page)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------

def press_list(page, items):
    out = []
    for it in items:
        out.append(
            f'<li><a href="{rel(page, "archive/" + it["slug"] + ".html")}">'
            f'{img(page, it["img"], "")}'
            f'<span class="source">{e(it["source"])}</span>'
            f'<h3>{e(it["title"])}</h3><p>{e(it["teaser"])}</p></a></li>'
        )
    return '<ul class="list">' + "".join(out) + "</ul>"


def news_list(page, items):
    out = []
    for it in items:
        out.append(
            f'<li><a href="{rel(page, "archive/" + it["slug"] + ".html")}">'
            f'{img(page, it["img"], "")}'
            f'<h3>{e(it["title"])}</h3><p>{e(it["teaser"])}</p></a></li>'
        )
    return '<ul class="list">' + "".join(out) + "</ul>"


def letters_list(page, items):
    out = []
    for it in items:
        out.append(
            f'<li><a href="{rel(page, "archive/" + it["slug"] + ".html")}">'
            f'<strong>{e(it["name"])}</strong><p>{e(it["teaser"])}</p></a></li>'
        )
    return '<ul class="letters">' + "".join(out) + "</ul>"


def logo_grid(page, items, linked=True):
    out = []
    for item in items:
        if linked:
            name, url, file = item
            if url:
                out.append(f'<li><a href="{e(url)}" rel="noopener">{img(page, file, name)}</a></li>')
            else:
                out.append(f"<li>{img(page, file, name)}</li>")
        else:
            name, file = item
            out.append(f"<li>{img(page, file, name)}</li>")
    return '<ul class="logos">' + "".join(out) + "</ul>"


def build_home():
    p = "index.html"
    body = f"""
<div class="hero">
  {img(p, "games-15.jpg", "Veteran Games participants and families gathered at night behind a large illuminated Veteran Games sign", 1600, 1067, lazy=False)}
  <div class="wrap">
    <h1>Uniting extraordinary people</h1>
    <p>Bringing together wounded, sick and injured UK veterans and their families with their overseas counterparts for five days of sporting competition, round table discussions and social and cultural activities.</p>
  </div>
</div>

<section>
  <div class="wrap split">
    <div>
      <h2>Recognising the fundamental role of sport and family in supporting ongoing recovery</h2>
    </div>
    <div class="prose">
      <p>The Veteran Games and Conference brought together 180 wounded, sick or injured UK veterans and their families alongside their overseas counterparts. Every participant was referred by a partner UK veteran charity, and nobody had to qualify to compete.</p>
      <p>Inclusivity and family were key to the ethos of the Games, in recognition of the role played by sport and family in supporting the ongoing recovery of veterans who have suffered physical and psychological challenges as a result of serving their country.</p>
      <div class="actions"><a class="button" href="games.html">About the Games</a><a class="button ghost" href="archive/">Browse the archive</a></div>
    </div>
  </div>
</section>

<section class="mist">
  <div class="wrap">
    <h2>The Games so far</h2>
    <ol class="timeline">
      <li><b>2018</b><span>The Veteran Games and Conference is first conceived</span></li>
      <li><b>2019</b><span>The inaugural Games and Mental Health Conference take place in the spring</span></li>
      <li><b>2022</b><span>The second Games and Conference</span></li>
      <li><b>2023</b><span>The third Games, with 180 UK veterans and their families</span></li>
    </ol>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>In the press</h2>
    {press_list(p, PRESS[:3])}
    <div class="actions"><a class="button ghost" href="archive/#press">All press coverage</a></div>
  </div>
</section>

<section class="mist">
  <div class="wrap">
    <blockquote>
      <p class="pull">“I have hope again. I have found a new strength. You and the team made this happen. I have found my smile again.”</p>
      <footer class="small">Anthony, Conference participant</footer>
    </blockquote>
    <div class="actions"><a class="button ghost" href="archive/#letters">Read letters from participants</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Our UK veteran charity partners</h2>
    <p class="lede">Participants were referred to the Games by these charities.</p>
    {logo_grid(p, CHARITY_PARTNERS)}
  </div>
</section>
"""
    write(p, layout(p, None, body))


def build_games():
    p = "games.html"
    gallery = "".join(
        img(p, f"games-{n}.jpg", alt)
        for n, alt in [
            (1, "Veterans in team kit walking through a war cemetery"),
            (2, "A veteran in a wheelchair leading children in a warm-up"),
            (4, "A veteran with a prosthetic leg lifting a barbell"),
            (9, "A veteran throwing a medicine ball"),
            (10, "A swimmer mid-stroke in a pool lane"),
            (12, "A veteran in a wheelchair holding a poppy wreath"),
            (3, "Three medal winners embracing after their event"),
            (7, "A veteran with prosthetic legs walking through a cemetery"),
            (13, "Two veterans covered in Dead Sea mud"),
            (14, "A veteran in an all-terrain wheelchair arriving at the venue"),
            (8, "A prosthetic leg resting beside a beach chair"),
            (6, "A team mascot bear on a gym floor"),
        ]
    )
    body = f"""
<div class="page-head"><div class="wrap">
  <h1>About the Veteran Games</h1>
  <p class="lede">A five-day programme of sport, conversation and culture for wounded, sick and injured veterans and their families.</p>
</div></div>

<section style="padding-top:0">
  <div class="wrap">
    <div class="gallery">{gallery}</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap"><div class="prose">
    <p>The Veteran Games and Conference is a programme that brings together 180 wounded, sick or injured UK Veterans and their families alongside their overseas counterparts. It was first conceived in 2018 and the inaugural event took place in the spring of 2019. The event proved phenomenally successful, so much so that the second event was held in 2022 and the third in 2023.</p>
    <p>The Veteran Games is a five-day event based around a sports competition between wounded, sick and injured veterans from the UK and overseas. This sporting element provides the focus; however, it is augmented and complemented by a full and varied social and cultural programme. Inclusivity and family are key to the ethos of the Veteran Games, in recognition of the fundamental role played by sport and family in supporting the ongoing recovery of veterans who have suffered physical and psychological challenges as a result of serving their country. As such this event is the first of its kind. The inclusion in 2019 of Chelsea Football Club to run football coaching activities for the children of the veterans was a particular success.</p>
    <p>The event draws UK veterans from across the Army, Royal Navy, Royal Air Force and Royal Marines and is backed by leading rehabilitation and Armed Forces charities who have selected beneficiaries to compete. These include Rock2Recovery, the Royal Air Force Benevolent Fund, The Not Forgotten Association, The Royal Marines Charity, Combat Stress, The Association of Jewish Ex-Servicemen and Women, Veterans Scotland, Felix Fund, SSAFA, Poppyscotland, Legion Scotland and Blind Veterans UK. The programme was also backed by Johnny Mercer MP, then Minister of State for Veterans’ Affairs.</p>
    <p>The Games bring wounded, sick and injured veterans and the families of both participating nations together. Both groups of veterans already hold many common values and have encountered similar challenges in their personal and professional lives. By exploring their shared experiences, it is hoped that the veterans, together with their families, will take benefit from the sporting and social interaction on offer and form attachments based on mutual understanding.</p>
    <p>The competition element of the Games has been designed to maximise participation. Inclusivity is key, and all veterans are strongly encouraged to take part in the activities on offer regardless of experience. This approach is supported by the deliberate absence of trials or any process of team selection. Team selection across the activities is guided by the preferences expressed by each veteran.</p>
    <p>The social and cultural programme that runs alongside the competition gives the UK contingent the opportunity to sample a rich and vibrant culture, socialise with their overseas counterparts, and explore internationally renowned and historically significant locations and sights.</p>
    <p>The Veteran Games initiative is funded entirely through the kind and generous donations of individuals and charitable foundations as well as from corporate sponsors.</p>
    <p>Participants were referred by one of our <a href="partners.html">partner UK veteran charities</a>.</p>
  </div></div>
</section>

<section class="mist" id="conference">
  <div class="wrap split">
    <div class="prose">
      <h2>The Conference</h2>
      <p>In conjunction with the 2019 and 2022 Veteran Games, a Mental Health Conference was convened under the chairmanship of Sir Simon Wessely and Professor Zahava Solomon. The gathering of medical professionals was widely hailed as a success, uniting innovators in the mental health field and facilitating profound discussions on crucial issues. Cross-border collaboration of this kind is crucial in advancing our understanding of mental health support for veterans.</p>
      <p>The 2022 Conference focused on three areas. Delegates first explored the historical evolution of civilian–military relationships, with a particular emphasis on the experiences of veterans. Second, the conference examined the present-day role of sport, exercise and competition in promoting veterans’ integration and rehabilitation, covering both physical rehabilitation and its implications for psychiatric rehabilitation. Finally, participants looked ahead to developments in service delivery and treatment innovation, with a specific focus on the evolving landscape of Post-Traumatic Stress Disorder (PTSD) care.</p>
    </div>
    <div>
      {img(p, "conference.jpg", "A veteran in a wheelchair speaking with a colleague at the Veteran Games office")}
      <figure style="margin-top:28px;display:grid;grid-template-columns:120px 1fr;gap:18px;align-items:start">
        {img(p, "sir-simon-wessely.jpg", "Professor Sir Simon Wessely")}
        <figcaption style="margin-top:0">Professor Sir Simon Wessely is a British psychiatrist, Director of the King’s Centre for Military Health Research and civilian consultant advisor in psychiatry to the British Army. He was knighted in the 2013 New Year Honours for services to military healthcare and to psychological medicine.</figcaption>
      </figure>
    </div>
  </div>
</section>
"""
    write(p, layout(p, "About the Games", body, current=p,
                    desc="The Veteran Games and Conference: five days of sport, conversation and culture for wounded, sick and injured veterans and their families."))


def build_wellbeing():
    p = "wellbeing.html"
    quotes = [
        ("Phil Eaglesham’s talk was a powerful and inspiring experience. His first hand accounts of military service resonated deeply, offering a profound insight into dedication and sacrifice. Phil’s ability to blend honesty with hope left an indelible mark, reminding me of the importance of resilience and the true meaning of service.", "Mark", "King’s College"),
        ("Such a wonderful experience and so moving. Thanks for organising. We must have him back.", "Sam Adams", "Assistant Head of 6th Form, Latymer Upper School"),
        ("We were thrilled to welcome Phil to Epsom College to speak. He was incredibly inspirational to the students. They loved learning about his new wheelchair design. A lot of students came up afterwards to speak personally to him about his condition. Truly inspirational.", "Sue Church-Jones", "Teacher, Epsom College"),
        ("Jamie’s visit to our school was a deeply moving experience that left an enduring impact on all of us. His accounts of resilience, sacrifice, and service were not just stories; they were windows into a world of dedication and bravery.", "Mia G", "JFS School"),
    ]
    qhtml = "".join(
        f'<blockquote><p>“{e(q)}”</p><footer>{e(n)}<span>{e(r)}</span></footer></blockquote>'
        for q, n, r in quotes
    )
    body = f"""
<div class="page-head"><div class="wrap">
  <h1>Our Wellbeing Programme</h1>
  <p class="lede">Veterans sharing their stories of rehabilitation with schools, community clubs and businesses.</p>
</div></div>

<section style="padding-top:0">
  <div class="wrap split">
    <div class="prose">
      <p>Since its inception in 2019, the Veteran Games and Conference has grown into an organisation that operates year-round. The charity is not just about one big trip a year: the focus lies in creating meaningful connections and empowering veterans throughout their recovery journey.</p>
      <p>Introduced in June 2022, the Wellbeing Programme brings veterans and audiences together to share their stories of rehabilitation. These candid conversations about their challenges and the importance of resilience had reached over 7,600 teenagers from schools across the country by January 2024, along with numerous community clubs and businesses. The ability of these veterans to connect with audiences on a personal level has proven transformative and inspiring for people of all ages.</p>
      <p>Sessions typically last around an hour: an introduction to the charity, then a UK veteran sharing their story, with images and video, built around the messages of resilience, mental health and asking for help.</p>
      <p>The programme has been fully funded. Schools may make a contribution if they can afford to, which helps the charity extend the programme into inner-city and disadvantaged areas. Corporates and organisations may sponsor a session for £250.</p>
      <div class="actions"><a class="button" href="contact.html">Ask about a talk</a></div>
    </div>
    <div>{img(p, "phil-at-vg.jpg", "Phil Eaglesham in an elevated wheelchair at the Veteran Games")}</div>
  </div>
</section>

<section class="mist">
  <div class="wrap split">
    <figure>
      {img(p, "phil-in-army-uniform.jpg", "Phil Eaglesham in Royal Marines uniform")}
      <figcaption>Phil Eaglesham</figcaption>
    </figure>
    <div class="prose">
      <h2>Phil Eaglesham</h2>
      <p>Phil attended the Veteran Games with his family in 2023. He is a former Royal Marine Commando, a Paralympic sport shooter, businessperson and mental health campaigner. Phil served as a Corporal with the Royal Marines. Following his third tour of duty, Afghanistan in 2010, he was diagnosed with Q fever, which left him with chronic disabilities.</p>
      <p>Phil was introduced to Para Shooting in 2012 and competed at the Paralympic Games in Rio 2016. In 2018 he competed in the World Shooting Para Sport Championships in South Korea and won a silver medal at the US Nationals in Georgia. In 2019 he won bronze at the World Championships in Australia, Ireland’s first ever World Championship medal in Para Shooting, qualifying him for the 2020 Tokyo Paralympics.</p>
      <p>Married with three children, Phil is founder and project manager of Victor Mobility, specialising in elevated wheelchair design. He won the Institute of Engineering Designers Alex Moulton Award 2018 for product innovation, and is a keen advocate for mental health awareness.</p>
      <p>Alongside Phil, the charity has worked with seven other veterans, training them to deliver their stories to a broader audience.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>What schools said</h2>
    <div class="quotes">{qhtml}</div>
  </div>
</section>
"""
    write(p, layout(p, "Wellbeing Programme", body, current=p,
                    desc="The Veteran Games Wellbeing Programme brings veterans into schools, community clubs and businesses to share their stories of rehabilitation."))


def build_team():
    p = "team.html"
    def person(file, name, role, ps):
        return (f'<div class="person">{img(p, file, name)}<div class="prose">'
                f'<h3>{e(name)}</h3>' + (f'<p class="role">{e(role)}</p>' if role else "") + paras(ps) + "</div></div>")
    team = [
        ("andrew-garland.jpg", "Andrew Garland", "Chief Executive", [
            "Andrew is a former Royal Marine with an extensive military career spanning 37 years, split almost equally between non-commissioned and commissioned rank. He has served across the globe in a broad range of operational, training, staff, command and policy appointments.",
            "On leaving the Royal Marines at the end of 2015 he was employed as the Operational Executive with an investment company based in London, one of the original sponsors of the Veteran Games and Conference. He was first introduced to the team behind the Games in 2018 during the planning and development phase ahead of the inaugural event in 2019.",
            "He combined work in support of the Games with his other employment until spring 2023, when, in recognition of the growth of the programme, he was appointed CEO on a full-time basis. Andrew is married with three children."]),
        ("spencer.jpg", "Spencer Gelding", "Chief Operating Officer", [
            "Together with Andrew Wolfson, Spencer was instrumental in establishing the Veteran Games and Conference in 2018. Beyond his philanthropic work, Spencer has a background in property and jewellery businesses spanning over three decades.",
            "Away from work, Spencer is an avid whisky collector and keen traveller. He has been married to Sasha for two decades, and together they have two daughters, Mia and Emily."]),
        ("david-thrilling.jpg", "David Thrilling", "Project Manager", [
            "David has a diverse background in mentoring, training, coaching, facilitating and project management within commercial and charitable organisations across sectors including banking, fashion, sport and education.",
            "David has over twenty years’ experience as a volunteer and joined the team as Project Manager in October 2023. His passion is helping others, and he is an avid football fan. David is married to Jeanette and is the proud father of Max and James."]),
    ]
    trustees = [
        ("andrew-w.jpg", "Andrew Wolfson", "Chairman", [
            "Andrew is a founder and CEO of Pembroke Investment Managers LLP. He chose not to attend university, instead embarking on a business career that has taken him across sectors including manufacturing, telecoms and hospitality.",
            "As chairman of Benesco Charity Limited, The Charles Wolfson Charitable Trust and MiSST (Music in Secondary Schools Trust), he contributes to initiatives across many areas of society. Andrew is also Chairman of the Veteran Games and Conference charity.",
            "Andrew is an avid golfer and enjoys exploring the world of wine. He is married to Orly and they have three children."]),
        ("marc-samuels.jpg", "Marc Samuels", "", [
            "Marc left school at 15 to pursue a career in the building trade. From beginnings as a labourer on a building site, he spent the next 35 years building a successful business in the property industry.",
            "His desire to help others led him to form his own charitable trust focused on supporting those in need. His involvement with the Veteran Games and Conference began in 2019, and Marc and his family volunteered at the 2019, 2022 and 2023 Games.",
            "Marc has three children, Amelie, Isabelle and Josh, and actively encourages them to volunteer with numerous charities."]),
    ]
    body = f"""
<div class="page-head"><div class="wrap"><h1>The team</h1></div></div>
<section style="padding-top:0"><div class="wrap"><h2>The UK team</h2><div class="people">{''.join(person(*t) for t in team)}</div></div></section>
<section class="mist"><div class="wrap"><h2>Trustees</h2><div class="people">{''.join(person(*t) for t in trustees)}</div></div></section>
"""
    write(p, layout(p, "The team", body, current=p, desc="The people behind the Veteran Games and Conference."))


def build_partners():
    p = "partners.html"
    body = f"""
<div class="page-head"><div class="wrap">
  <h1>Partners and sponsors</h1>
  <p class="lede">The Veteran Games were made possible by UK veteran charities, charitable foundations, corporate sponsors and many anonymous donors.</p>
</div></div>

<section style="padding-top:0">
  <div class="wrap">
    <h2>UK veteran charity partners</h2>
    <p>Participants were referred to the Games by one of these charities.</p>
    {logo_grid(p, CHARITY_PARTNERS)}
  </div>
</section>

<section class="mist" id="sponsors">
  <div class="wrap">
    <h2>Event sponsors</h2>
    <p class="prose">A special thanks to those who have kindly sponsored the Veteran Games programme since its establishment in 2019. We would also like to thank the many anonymous sponsors who have helped along the way.</p>
    {logo_grid(p, SPONSORS, linked=False)}
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Community and corporate partners</h2>
    {logo_grid(p, COMMUNITY)}
  </div>
</section>
"""
    write(p, layout(p, "Partners and sponsors", body, current=p,
                    desc="The UK veteran charities, sponsors and partners behind the Veteran Games and Conference."))


def build_archive():
    p = "archive/index.html"
    qhtml = "".join(
        f'<blockquote><p>“{e(q)}”</p><footer>{e(n)}<span>{e(r)}</span></footer></blockquote>'
        for q, n, r in QUOTES
    )
    body = f"""
<div class="page-head"><div class="wrap">
  <h1>Archive</h1>
  <p class="lede">Press coverage, news and letters from the 2019, 2022 and 2023 Games.</p>
</div></div>

<section style="padding-top:0" id="press">
  <div class="wrap"><h2>In the press</h2>{press_list(p, PRESS)}</div>
</section>

<section class="mist" id="news">
  <div class="wrap"><h2>News</h2>{news_list(p, NEWS)}</div>
</section>

<section id="letters">
  <div class="wrap">
    <h2>Letters from participants</h2>
    <p class="lede">Letters written to the team by veterans, families and partners after the Games.</p>
    {letters_list(p, LETTERS)}
  </div>
</section>

<section class="mist" id="testimonials">
  <div class="wrap"><h2>What people said</h2><div class="quotes">{qhtml}</div></div>
</section>
"""
    write(p, layout(p, "Archive", body, current="archive/index.html",
                    desc="Press coverage, news and letters from the Veteran Games and Conference."))

    for it in PRESS:
        q = f"archive/{it['slug']}.html"
        label = it.get("link_label", f"Read the full article at {it['source']}")
        body = f"""
<article class="wrap" style="padding-top:clamp(32px,5vw,64px);padding-bottom:clamp(40px,6vw,80px)">
  <a class="back" href="./#press">Back to the archive</a>
  <span class="source">{e(it['source'])}</span>
  <h1 style="max-width:24ch">{e(it['title'])}</h1>
  <figure class="article-hero">{img(q, it['img'], '', lazy=False)}</figure>
  <div class="prose">
    {paras(it['body'])}
    <p class="small">An excerpt from the original coverage.</p>
    <div class="actions"><a class="button" href="{e(it['url'])}" rel="noopener">{e(label)}</a></div>
  </div>
</article>"""
        write(q, layout(q, it["title"], body, current="archive/index.html", desc=it["teaser"]))

    for it in NEWS:
        q = f"archive/{it['slug']}.html"
        body = f"""
<article class="wrap" style="padding-top:clamp(32px,5vw,64px);padding-bottom:clamp(40px,6vw,80px)">
  <a class="back" href="./#news">Back to the archive</a>
  <h1 style="max-width:24ch">{e(it['title'])}</h1>
  <figure class="article-hero">{img(q, it['img'], '', lazy=False)}</figure>
  <div class="prose">{paras(it['body'])}</div>
</article>"""
        write(q, layout(q, it["title"], body, current="archive/index.html", desc=it["teaser"]))

    for it in LETTERS:
        q = f"archive/{it['slug']}.html"
        sign = "<br>".join(e(s) for s in it["sign"])
        body = f"""
<article class="wrap" style="padding-top:clamp(32px,5vw,64px);padding-bottom:clamp(40px,6vw,80px)">
  <a class="back" href="./#letters">Back to the letters</a>
  <h1>A letter from {e(it['name'])}</h1>
  <div class="letter">{paras(it['body'])}<p class="sign">{sign}</p></div>
</article>"""
        write(q, layout(q, f"A letter from {it['name']}", body, current="archive/index.html", desc=it["teaser"]))


def build_app():
    p = "app.html"
    feats = [
        ("icon-connect.png", "Connect", "Keep the Veteran Games community together for current and previous participants, family and support team, with connection and regular engagement throughout the year."),
        ("icon-career.png", "Career and interest", "Groups, resources and connections that may help you, whether with career decisions or a shared interest."),
        ("icon-support.png", "Support", "Peer support, social engagement and access to welfare resources at the heart of the platform."),
        ("icon-family.png", "Family", "Likeminded people from every year of the Veteran Games and Conference, with a shared set of values and respect."),
    ]
    fhtml = "".join(f'<div>{img(p, f, "")}<h3>{e(t)}</h3><p>{e(d)}</p></div>' for f, t, d in feats)
    body = f"""
<div class="page-head"><div class="wrap">
  <h1>The Veteran Games app</h1>
  <p class="lede">A private community space for Veteran Games participants and families, run on the Military App platform.</p>
</div></div>

<section style="padding-top:0">
  <div class="wrap">
    <div class="features">{fhtml}</div>
  </div>
</section>

<section class="mist">
  <div class="wrap split">
    <div>
      {img(p, "digital-platform-mobile.jpg", "The Veteran Games app on a phone")}
      <h2 style="margin-top:24px">Mobile app</h2>
      <p>Download the app for Android or iOS. You can find old friends and members near you, join Veteran Games groups, and take part in wider social, career, wellbeing and interest groups with events and chat.</p>
      <div class="badges">
        <a href="https://apps.apple.com/gb/app/military-app/id1635519057" rel="noopener">{img(p, "apple-download.png", "Download on the App Store")}</a>
        <a href="https://play.google.com/store/apps/details?id=com.allegr.military" rel="noopener">{img(p, "google-download.png", "Get it on Google Play")}</a>
      </div>
    </div>
    <div>
      {img(p, "digital-platform-web.jpg", "The Veteran Games web app on a laptop")}
      <h2 style="margin-top:24px">Web app</h2>
      <p>If you prefer a laptop or home computer, the web app uses the same login and the same community. If you run a group or post regularly, the web app can make that quicker.</p>
      <div class="actions" style="margin-top:0"><a class="button" href="members.html">Sign in to the web app</a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="prose">
      <h2>Registering</h2>
      <p>To register you need the Veteran Games group access code. It has been shared by email and in the private Veteran Games social media groups, rather than in public.</p>
      <p>If you don’t have the code, or need help at any stage, email the Military App help desk at <a href="mailto:help@militaryapp.org">help@militaryapp.org</a>. You can also use the ‘Support and FAQ’ button at the bottom of the app’s sign-in screen.</p>
      <p>Once registered, members have a private pinboard for photos and updates, private groups, events and chat, and a Support Suite with over 650 support videos and a library of more than 250 support charities.</p>
      <div class="actions">
        <a class="button ghost" href="https://www.militaryapp.org/login/making-the-most-of-the-app" rel="noopener">Making the most of the app</a>
        <a class="button ghost" href="https://www.militaryapp.org/login/app-support#faq" rel="noopener">FAQs and support</a>
      </div>
    </div>
    <div>
      {img(p, "wider-community.jpg", "Members of the wider Military App community")}
      <h3 style="margin-top:20px">The wider Military App community</h3>
      <p>You join through your Veteran Games groups, and can also connect with people, events and groups across the wider Military App community, including over 70 Walk+Talk groups and member-run Coffee Clubs across the UK and internationally.</p>
    </div>
  </div>
</section>
"""
    write(p, layout(p, "The Veteran Games app", body, current=p,
                    desc="The Veteran Games and Conference app: a private community for participants and their families."))


def build_members():
    p = "members.html"
    body = """
<div class="embed">
  <iframe id="MAembed" title="Veteran Games members' web app" width="100%" allow="clipboard-read; clipboard-write"></iframe>
  <script src="https://cdn.militaryapp.org/embed-scripts/embed-app.js"></script>
</div>
"""
    write(p, layout(p, "Members’ web app", body, current="app.html",
                    desc="Sign in to the Veteran Games members' web app."))


def build_contact():
    p = "contact.html"
    body = f"""
<div class="page-head"><div class="wrap">
  <h1>Contact us</h1>
  <p class="lede">Questions about the Veteran Games, the Wellbeing Programme, sponsorship or leaving a legacy gift are all welcome.</p>
</div></div>

<section style="padding-top:0">
  <div class="wrap split">
    <div>
      <dl class="facts">
        <dt>Email</dt><dd><a href="mailto:davidt@veterangames.co.uk">davidt@veterangames.co.uk</a></dd>
        <dt>Telephone</dt><dd><a href="tel:+442084582455">020 8458 2455</a></dd>
        <dt>Post</dt><dd>Veteran Games and Conference<br>Suite 3, One Bridge Lane<br>London NW11 0EA</dd>
        <dt>Charity</dt><dd>Registered Charity No. 1202198</dd>
      </dl>
      <h2 style="margin-top:40px">The team</h2>
      <p><strong>Andrew Garland</strong>, Chief Executive<br><strong>Spencer Gelding</strong>, Chief Operating Officer<br><strong>David Thrilling</strong>, Project Manager</p>
      <h2 style="margin-top:40px">App support</h2>
      <p>For help with the Veteran Games app or web app, email the Military App team at <a href="mailto:help@militaryapp.org">help@militaryapp.org</a>.</p>
    </div>
    <div>
      {img(p, "team-photo.jpg", "Veteran Games participants and families at a reception")}
      <h2 style="margin-top:32px">Leaving a legacy gift</h2>
      <div class="prose"><p>A gift in your Will to benefit the participants of the Veteran Games programme helps secure its future, giving future generations of veterans opportunities for physical activity, social connection and rehabilitation. To talk to the team about a legacy gift, please get in touch and we will call you back or arrange a meeting.</p></div>
    </div>
  </div>
</section>
"""
    write(p, layout(p, "Contact", body, current=p, desc="Contact the Veteran Games and Conference team."))


def build_privacy():
    p = "privacy.html"
    body = """
<div class="page-head"><div class="wrap"><h1>Privacy</h1></div></div>
<section style="padding-top:0">
  <div class="wrap"><div class="prose">
    <p>This notice explains how the Veteran Games and Conference (Registered Charity No. 1202198) handles personal information in connection with this website.</p>
    <h2>What this website collects</h2>
    <p>This website does not use forms, cookies, analytics or advertising trackers. Its fonts and images are served from the site itself rather than from third parties.</p>
    <p>The site is hosted on GitHub Pages. Like most web hosts, GitHub logs the IP addresses of visitors for security and to keep the service running. GitHub’s handling of this data is described in the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub General Privacy Statement</a>.</p>
    <h2>Members’ web app</h2>
    <p>The members’ sign-in page embeds the Military App web app. If you sign in or register, your information is handled by the Military App under its own privacy policy, available within the app.</p>
    <h2>Contacting us</h2>
    <p>If you email or phone us, we use the details you give us only to respond to your enquiry. You can ask us what information we hold about you, or ask us to correct or delete it, by emailing <a href="mailto:davidt@veterangames.co.uk">davidt@veterangames.co.uk</a> or writing to Suite 3, One Bridge Lane, London NW11 0EA.</p>
    <p>If you are unhappy with how we have handled your information, you can complain to the Information Commissioner’s Office at <a href="https://ico.org.uk" rel="noopener">ico.org.uk</a>.</p>
  </div></div>
</section>
"""
    write(p, layout(p, "Privacy", body, desc="How the Veteran Games and Conference website handles personal information."))


def build_404():
    p = "404.html"
    # GitHub Pages serves 404.html at any depth, so use root-absolute links here.
    body = """
<div class="page-head"><div class="wrap">
  <h1>This page has moved</h1>
  <p class="lede">The Veteran Games website has been simplified and this address no longer exists.</p>
  <div class="actions"><a class="button" href="/">Go to the home page</a><a class="button ghost" href="/archive/">Browse the archive</a></div>
</div></div>
"""
    html = layout(p, "Page not found", body)
    html = html.replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/')
    for href, _ in NAV + [("index.html", ""), ("members.html", ""), ("privacy.html", "")]:
        html = html.replace(f'href="{href}"', f'href="/{href.replace("index.html", "")}"')
    write(p, html)


# Old Webflow URLs -> new pages, so existing links and search results keep working.
REDIRECTS = {
    "about/about-the-veteran-games": "games.html",
    "about/about-the-conference": "games.html#conference",
    "about/looking-ahead-to-2024": "games.html",
    "about/our-uk-veteran-charity-partners": "partners.html",
    "about/veteran-games-sponsors": "partners.html#sponsors",
    "about/the-team": "team.html",
    "about/wellbeing-programme": "wellbeing.html",
    "about/about-the-veteran-games-app": "app.html",
    "about/testimonials": "archive/index.html#letters",
    "contact-form": "contact.html",
    "leave-a-legacy-gift": "contact.html",
    "privacy-policy": "privacy.html",
    "news-events/media": "archive/index.html#press",
    "news-events/featured-news-events": "archive/index.html#news",
    "news-events/past-events": "archive/index.html",
    "sign-in/app": "members.html",
    "sign-in/app-support": "app.html",
    "sign-in/web-app-support": "app.html",
    "get-support/concerned-about-a-comrade": "index.html",
    "get-support/group-code-request": "app.html",
    "get-support/useful-links": "index.html",
}
for s in ["corporate", "golf", "march-of-the-living", "revelation-tv", "tower-of-london", "triathlon", "veteran-games-2025"]:
    REDIRECTS["events/" + s] = "index.html"
for s in ["east", "london-southeast", "midlands", "north-east", "south-west", "wales"]:
    REDIRECTS["groups/" + s] = "index.html"
for it in PRESS:
    REDIRECTS["press-release/" + it["slug"]] = f"archive/{it['slug']}.html"
for it in NEWS:
    REDIRECTS["news-and-events/" + it["slug"]] = f"archive/{it['slug']}.html"
for it in LETTERS:
    REDIRECTS["testimonials/" + it["slug"]] = f"archive/{it['slug']}.html"


def build_redirects():
    for old, new in REDIRECTS.items():
        page = old + ".html"   # GitHub Pages serves /about/x from about/x.html
        target = rel(page, new)
        absolute = DOMAIN + "/" + new.replace("index.html", "")
        write(page, f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8">
<title>Moved</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{absolute}">
<meta http-equiv="refresh" content="0; url={target}">
</head><body><p>This page has moved to <a href="{target}">{absolute}</a>.</p></body></html>
""")


def build_static_files():
    os.makedirs(os.path.join(ROOT, "assets/css"), exist_ok=True)
    with open(os.path.join(SRC, "fonts.css"), encoding="utf-8") as f:
        fonts = f.read()
    with open(os.path.join(SRC, "style.css"), encoding="utf-8") as f:
        style = f.read()
    with open(os.path.join(ROOT, "assets/css/style.css"), "w", encoding="utf-8") as f:
        f.write(fonts + "\n" + style)
    pages = ["", "games.html", "wellbeing.html", "team.html", "partners.html", "archive/", "app.html", "contact.html", "privacy.html"]
    pages += [f"archive/{it['slug']}.html" for it in PRESS + NEWS + LETTERS]
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for pg in pages:
            f.write(f"  <url><loc>{DOMAIN}/{pg}</loc></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    with open(os.path.join(ROOT, "CNAME"), "w", encoding="utf-8") as f:
        f.write("www.theveterangames.co.uk\n")


if __name__ == "__main__":
    build_static_files()
    build_home()
    build_games()
    build_wellbeing()
    build_team()
    build_partners()
    build_archive()
    build_app()
    build_members()
    build_contact()
    build_privacy()
    build_404()
    build_redirects()
    print("Built", sum(len(fs) for _, _, fs in os.walk(ROOT) if "_src" not in _ and "assets" not in _), "files")
