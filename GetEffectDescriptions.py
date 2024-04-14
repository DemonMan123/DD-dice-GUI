Descriptions = {
    # The Jester
    'Fools Fortune': "The party encounters a friendly jester who grants them better luck, allowing all party members to have [Advantaged Rolls] on their [Death Saving] rolls.",
    'Tricksters Bounty': "The Tarot Holder stumbles upon a hidden cache of treasures left behind by a mischievous trickster, gaining valuable items and money.",
    'Laughters Blessing' : "The Tarot Holder gains 3 extra [Social Points] to their [Charisma].",
    'Jesters Gambit' : "The party encounters a malevolent jester who tricks them into a dangerous situation, resulting in the loss of valuable items or money.",
    'Fools Misfortune' : "The Tarot Holder becomes unpredictable when attacking, causing [Disadvantaged Rolls] on attack-based actions and [Death Saving] rolls.",
    'Mocking Mirage' : "The party becomes ensnared in an illusory trap set by a trickster, causing the party to fight each other and have [Disadvantaged Rolls] on attack-based actions. Each party member must roll a success to break from the trap.",
    # The Sorcerer
    'Arcane Revelation' : "The party encounters a wise Evobionic who imparts Mawic knowledge. This could grant the Bionic-class party member an additional fourth skill that can be used once every floor.",
    'Mawic Attunement' : "The Tarot Holder finds a Mawic item that grants them protection from Mawic exposure and attacks.",
    'Sorcerers Insight' : "The Tarot Holder gains 3 extra [Social Points] to their [Wisdom]. If the holder is a Bionic, they gain the ability to see souls and ritualistic writings.",
    'Mawic Backlack' : "The Tarot Holder will experience hallucinations and hear voices, making them paranoid. If the holder is a Bionic, their Mawic powers will cause damage to themselves and nearby party members.",
    'Chaos Surge' : "The Tarot Holder becomes exposed to the Maw, allowing portals to open around them to create [Void Burn] hazards at random.",
    'Sorcerers Curse' : "The Tarot Holder's attacks are now rolled on [Disadvantaged Rolls].",
    # The Creedsmen
    'Code of Honor' : "The party encounters a group of Creedsmen who recognize their valor and grant them new weapons that are effective against Evobionic enemies.",
    'Oathsworn Alliance' : "The party forms an alliance with a group of Creedsmen, gaining assistance to enter specific areas or gain information.",
    'Creeds Protection' : "The Tarot Holder becomes resistant to Psychomancy and the Evophage.",
    'Broken Oath' : "The Tarot Holder loses the trust and favor of any Creedsmen they come across. This decreases [Charisma] by 2 [Social Points] when interacting with Creedsmen.",
    'Fallen Comrades' : "The Creedsmen are hostile to the party due to orders from someone else, forcing them to attack you.",
    'Creeds Judgement' : "The Creedsmen deem the party heretics and will from now on hunt the party till they can prove their innocence.",
    # The Mistress
    'Enthralling Charm' : "The party encounters a charismatic mistress who offers them valuable information or assistance in exchange for a favor, granting them access to hidden knowledge or resources.",
    'Seductive Veil' : "The Tarot Holder has maximum [Charisma].",
    'Mistresss Embrace' : "The Tarot Holder is suddenly much braver, making them immune to being mind controlled or frightened.",
    'Temptations Trap' : "The Tarot Holder falls victim to the manipulative charm of a deceitful mistress, resulting in betrayal or being led into a dangerous situation.",
    'Lusts Ensnarement' : "The Tarot Holder becomes infatuated with a seductive mistress, causing distraction and a 2 [Social Points] decrease on [Wisdom].",
    'Jealous Wrath' : "The party incurs the wrath of a jealous mistress, becoming the target of her vindictive schemes and facing 5 [Social Points] to [Charisma] when interacting with Gangers.",
    # The Primordial
    'Ancient Wisdom' : "The Tarot Holder encounters an ancient primordial entity who imparts profound wisdom and knowledge of the natural world, granting them insight into rituals and otherworldly texts.",
    'Primal Blessing' : "The Tarot Holder gains enhanced physical strength and resistance to non-Mawic damage.",
    'Natures Harmony' : "The Tarot Holder gains an advantage on [Survival] and [Nature] rolls.",
    'Raging Elements' : "The party experiences natural disasters or environmental hazards in the area.",
    'Primeval Curse' : "The party becomes more susceptible to possession when in the presence of Mawic portals.",
    'Chaos of Creation' : "The party encounters a ritual being done that will summon a Possessor of the Maw if not interrupted.",
    # The Oracle
    'Divine Insight' : "The Tarot Holder receives a vision of the future.",
    'Oracles Eye' : "The Tarot Holder is able to see the actions of their enemies before they do it.",
    'Fates Intervention' : "The Tarot Holder gains protection from another force, granting them [Advantaged Rolls] on their [Death Saving] rolls against harmful effects (Bleed, Void Burn, and Burning).",
    'Cryptic Visions' : "The Tarot Holder is plagued by cryptic visions from the oracle, causing confusion and uncertainty about their true meaning.",
    'Twisted Fate' : "The Tarot Holder's actions can alter the course of fate, leading to unintended consequences.",
    'Oracles Curse' : "The Tarot Holder will be cursed if they seek out forbidden knowledge, attracting the attention of malevolent forces seeking to manipulate their destiny.",
}

def getEffectDescription(Effect):
    Description = ""
    if Effect in Descriptions:
        Description = Descriptions[Effect]
    else:
        Description = "NULL"
    return Description