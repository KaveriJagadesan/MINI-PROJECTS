# Total cards in deck
total_cards = 52

# Number of face cards (J, Q, K in 4 suits)
face_cards = 12  

# Number of red face cards (J, Q, K in hearts and diamonds)
red_face_cards = 6  

# Conditional probability: P(Red | Face) = P(Red and Face) / P(Face)
prob_red_given_face = red_face_cards / face_cards

print(f"Probability of drawing a red card given it's a face card: {prob_red_given_face:.2f}")
