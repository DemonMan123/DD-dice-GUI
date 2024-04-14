word_dict = {
    'The Fool': "New beginnings, taking risks, living in the moment.",
    'The Magician': "Manifestation, creativity, self-confidence, skill.",
    'The High Priestess': "Intuition, secrets, hidden knowledge, mystery.", 
    'The Empress': "Nurturing, abundance, creativity, motherhood.", 
    'The Emperor': "Authority, structure, stability, leadership.", 
    'The Hierophant': "Tradition, conformity, spiritual guidance, education.", 
    'The Lovers': "Love, relationships, choices, harmony.", 
    'The Chariot': "Control, willpower, determination, progress.", 
    'Strength': "Inner strength, courage, self-discipline, endurance.", 
    'The Hermit': "Solitude, introspection, inner wisdom, guidance.", 
    'The Wheel of Fortune': "Cycles, fate, change, karma.", 
    'Justice': "Balance, fairness, truth, accountability.", 
    'The Hanged Man': "Surrender, letting go, suspension, sacrifice.", 
    'Death': "Transformation, endings, rebirth, change.", 
    'Temperance': "Balance, moderation, harmony, patience.", 
    'The Devil': "Materialism, attachment, addiction, temptation.", 
    'The Tower': "Crisis, upheaval, sudden change, revelation.", 
    'The Star': "Hope, inspiration, faith, renewal.", 
    'The Moon': "Intuition, emotions, uncertainty, illusion.", 
    'The Sun': "Joy, success, happiness, clarity.", 
    'Judgement': "Renewal, rebirth, awakening, transformation.", 
    'The World': "Completion, fulfillment, unity, accomplishment."
}
'''
word_dict = {
    'The Jester': "Symbolizing unpredictability, playfulness, and the unexpected twists of fate.",
    'The Sorcerer': "Represents mastery over the elements, arcane knowledge, and the power of transformation.",
    'The Creedsmen': "Signifies adherence to a set of beliefs or principles, unwavering dedication, and the strength of convictions.",
    'The Mistress': "Embodies allure, seduction, and the influence of feminine energy.",
    'The Primordial': "Represents the beginning, primal forces of nature, and the raw, untamed essence of existence.",
    'The Oracle': "Symbolizes wisdom, foresight, and divine guidance.",
    'The Geminic Bond': "Signifies duality, partnerships, and the interconnectedness of relationships.",
    'The Warp Drive': "Represents innovation, progress, and the ability to traverse great distances or overcome obstacles swiftly.",
    'The Guardian Shield': "Embodies protection, strength, and the safeguarding of what is precious.",
    'The Isolationist': "Symbolizes withdrawal, introspection, and the necessity of solitude for growth.",
    'The Shifting Maw': "Signifies change, instability, and the relentless cycle of creation and destruction.",
    'The Adjudication': "Represents justice, fairness, and the resolution of conflicts through impartial judgment.",
    'The Martyr': "Embodies sacrifice, selflessness, and the willingness to endure suffering for a greater cause.",
    'The Maw': "Symbolizes the abyss, the unknown, and the consuming darkness that lurks within.",
    'Angel of the Maw': "Represents redemption, salvation, and the guiding light within the darkness.",
    'Possessor of the Maw': "Signifies control over primal forces, inner demons, and the harnessing of raw power.",
    'High Spire': "Embodies aspiration, elevation, and the pursuit of lofty goals.",
    'The Gate': "Symbolizes transitions, thresholds, and the passage from one phase of life to another.",
    'Black Moon': "Represents mystery, hidden truths, and the unseen forces that shape our destinies.",
    'Solar Beacon': "Signifies illumination, clarity, and the guiding light that leads the way through darkness.",
    'Call of the Maw': "Embodies temptation, allure, and the irresistible pull of the unknown.",
    'Astral Realm': "Represents transcendence, spiritual awakening, and the boundless expanses of the cosmos."
}
'''
def search_word(word):
    if word in word_dict:
        return word_dict[word]