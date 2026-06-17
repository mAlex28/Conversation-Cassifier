"""
Transcripts are generated using claude.

Prompt: Generate 10 call transcrispts. Each transcript should include "id", "expected_outcome", "expected_name", and "transcript" field. 
"id" - use the main theme of the call as the id. e.g: electricity_outage.
"expected_outcome" - one of callback, resolved, complaint or follow-up.
"expected names" - leave some names as null. 

Do not mention customer phone numbers in any of the transcripts. 
Return the output as a JSON list. 

"""

TRANSCRIPTS = [
    {
        "id": "broadband_dropout",
        "expected_outcome": "callback",
        "expected_name": "Sam Whitfield",
        "transcript": """Agent: Thanks for calling, you're through to support. Can I take your name?
Customer: Yeah, it's Sam Whitfield.
Agent: Thanks Sam, how can I help?
Customer: My broadband's been dropping out for three days now. I work from home so this is a nightmare.
Agent: I'm sorry to hear that. Let me run a line check... it does look like there's an issue on your connection.
Customer: Right, well I can't be on the phone all day, I've got meetings. Can someone just call me back this afternoon once you've figured it out?
Agent: Of course, I'll arrange for an engineer to call you back after 2pm.
Customer: Thanks, that works.""",
    },
    {
        "id": "wrong_size_order",
        "expected_outcome": "resolved",
        "expected_name": None,
        "transcript": """Agent: Hello, how can I help today?
Customer: Hi, I ordered a jacket last week and got sent the wrong size. It's a medium, I needed a large.
Agent: No problem at all. I can send out the large today and email you a free returns label for the medium.
Customer: Oh great. Do I get charged anything?
Agent: Nothing at all, it's on us.
Customer: Perfect, that's sorted then. Thanks very much.
Agent: You're welcome, have a good day.""",
    },
    {
        "id": "careless_delivery",
        "expected_outcome": "complaint",
        "expected_name": "Priya Anand",
        "transcript": """Agent: Hello, how can I help?
Customer: I don't need anything fixed, I just want to register a complaint. Your delivery driver left my parcel in the pouring rain on the doorstep and it was soaked through.
Agent: I'm very sorry to hear that.
Customer: The item's fine, luckily, so I don't want a replacement. I just think it's unacceptable and someone should know.
Agent: Understood, I'll log that feedback about the driver.
Customer: Good. That's all I wanted to say.""",
    },
    {
        "id": "boiler_part_wait",
        "expected_outcome": "follow-up",
        "expected_name": None,
        "transcript": """Agent: Good morning, how can I help?
Customer: My boiler's making a banging noise. An engineer came out last week but said he needed a part.
Agent: Let me check the notes... yes, the part's been ordered. It's due to arrive in about five working days.
Customer: Okay. So what happens then?
Agent: Once it's in, we'll book you a follow-up visit to fit it. We'll be in touch to arrange a date.
Customer: Alright, I'll wait to hear from you then.
Agent: That's right, we'll contact you once the part's in.""",
    },
    {
        "id": "password_reset",
        "expected_outcome": "resolved",
        "expected_name": "Jordan Blake",
        "transcript": """Agent: Support, how can I help?
Customer: I can't log into my account, it keeps saying my password's wrong.
Agent: No worries. Can I take your name and the email on the account?
Customer: Jordan Blake, and the email's jordan.blake@gmail.com.
Agent: Thanks Jordan, I've sent a reset link to that address now. You should see it in a minute.
Customer: Yep, got it... right, resetting now... okay I'm in. Brilliant.
Agent: Perfect, anything else?
Customer: No that's it, cheers.""",
    },
    {
        "id": "missing_parcel",
        "expected_outcome": "callback",
        "expected_name": None,
        "transcript": """Agent: Hello, you've reached deliveries. How can I help?
Customer: My parcel was meant to come yesterday and it never turned up. Tracking just says 'out for delivery'.
Agent: Let me look into that for you... I can see it's been delayed at the depot.
Customer: I'm heading out now and won't be back till evening. Can you call me back later once you know what's happening with it?
Agent: Absolutely, I'll give you a call after 5pm with an update.
Customer: Great, speak then.""",
    },
    {
        "id": "subscription_not_cancelled",
        "expected_outcome": "resolved",
        "expected_name": "Tom Reilly",
        "transcript": """Agent: Hi, who am I speaking with?
Customer: Tom Reilly.
Agent: Thanks Tom, what can I help you with?
Customer: I cancelled my subscription two months ago and you're STILL taking money out of my account.
Agent: I'm sorry about that, let me check.
Customer: I've got the cancellation email right here. This is ridiculous. You've taken nearly forty quid you shouldn't have.
Agent: I do apologise, I can see the cancellation didn't process correctly. I'll refund both payments now.
Customer: I should hope so. Honestly, terrible service.""",
    },
    {
        "id": "storm_damage_claim",
        "expected_outcome": "follow-up",
        "expected_name": None,
        "transcript": """Agent: Claims department, how can I help?
Customer: I'm calling about my claim from the storm damage, reference 4471.
Agent: Let me pull that up... yes, it's currently with our assessors.
Customer: How long does that take?
Agent: They're reviewing it now. We're waiting on the surveyor's report before we can confirm the payout.
Customer: Okay, so there's nothing I need to do right now?
Agent: Nothing for the moment. Once the report's back we'll process it and update you.
Customer: Right, I'll sit tight then.""",
    },
    {
        "id": "contract_price_hike",
        "expected_outcome": "callback",
        "expected_name": "Dani Okafor",
        "transcript": """Agent: Hello, how can I help? Can I take your name?
Customer: Dani Okafor. My phone contract renewed at double the price without anyone telling me. I'm furious.
Agent: I'm sorry Dani, let me look at the account.
Customer: I don't have time right now, I'm at work. But I am NOT paying double. Someone needs to ring me back today and fix this or I'm cancelling everything.
Agent: Understood, I'll have someone call you back this afternoon to sort the pricing.
Customer: They'd better. This is appalling.""",
    },
    {
        "id": "address_change_hold",
        "expected_outcome": "resolved",
        "expected_name": None,
        "transcript": """Agent: Support, how can I help?
Customer: I've been on hold for forty-five minutes. Forty-five! Just to change my address.
Agent: I'm really sorry about the wait. I can update that for you right now though.
Customer: Go on then.
Agent: Done, your address is updated. Is the rest of your account correct?
Customer: Yeah, that's all I needed. But forty-five minutes for that is a joke, honestly.
Agent: I understand, and I'm sorry again. Anything else?
Customer: No. Bye.""",
    },
]
