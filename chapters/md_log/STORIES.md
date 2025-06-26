# Sep - Dec 2024
- ✅ started off with `TheBloke/dolphin-2.2.1-mistral-7B-GGUF/dolphin-2.2.1-mistral-7b.Q4_K_M.gguf`

# Jan - Feb 2025
- ✅ switched to `gpt-4o-mini` via azure openai because it has better quality
- ✅ reworked the story prompt in the pattern of external and internal motivations. 
 - it starts off with external motivation to change e.g., failing at work due to health => go to healthcare professional HP.
 - then HP gives external instruction e.g., walk 10 minutes a day.
 - as the Px practices these, he or she sees the benefit. this builds the internal motivation
 - then the _reason behind the HP's external instruction_ becomes the internal instruction

# Apr - June 2025
- ✅ switched story prompt to match Gabi's new form structure
- 👉 switched from DefaultV2 content filter to my custom filter which ignores all jailbreak-detection triggers so I can use the models without being blocked for false-negative jailbreak triggers.
- ✅ checking to see if Hero's Journey can be incorportated into our story structure.
    - ✅ got it working to make a story outline.
    - ✅ added it to our story pipeline march_batch.
    - ➡️ tweaking to get good flow
    - ✅ created a ChASE table and it works. (on paper)
    - ➡️ breaking up ChASE's _Actions_ column into Action-Reason-Outcome-Reason for more fine-grained control over story gen.
- ➡️ low-hanging fruit from Redmond...
    - image emotion should match the paragraph emotion. perhaps on the last sentence.
    - simplify the story english. it's still too educated-sounding.
- ✅ fix the participant dets on the PDF - fix formating, add pronoun. 
- ➡️ Add Yes/No so it's clearer to the LLM.
- ➡️ use the actual participant details as toggles / sources for the generation
    - _culture_ influences their looks. can it influence some of the story decisions too?
    - we're not using _religion_ in any meaningful way. maybe at the identity change we can employ it esp Chrisitianity. check if this is also part of their _support network_.
    - maybe use _hobbies and activities_ at the trouble stage (px fails to do or enjoy the hobby bse of health)
    - maybe use _hobbies and activities_ at the lifestyle/identity stage (px incorporating changes into their hobby)
    - use _healthcare access, freq, and resources_ to shape where the px goes to seek help from. Gabi was supposed to send the T2D/medical access heirarchy.
    - use _tobacco and alcohol_ in a meaningful way. currently they're not shown.
    - maybe _support network_ can make up the enemies and allies so that in the end, the bond is stronger..?

- Jacki email about testing diff patient dets and their influence on the story.
    - ✅ does image bg match _city/town_ and _location description_?
        - not aligned. suggests similar environments to urban schools for user Test001 who lives in a rural area. [PDF is on fifty90]
    - ✅ does _safety rating_ match exercise decision esp walking/jogging?
        - not aligned. still suggests walks for user Test001 even when input says there are safety concerns affecting outdoor activity. [PDF is on alienware]
    - ➡️ need to go through the form and align story generation to specific inputs from it (similar to previous point above).

- ➡️ mixture of experts models... 
- ➡️ retreival-augmented finetuning... 