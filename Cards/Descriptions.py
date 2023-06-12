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

def search_word(word):
    if word in word_dict:
        return word_dict[word]