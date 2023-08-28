### Counting disease carriers ###

q_squares = [float(q_2) for q_2 in '0.400154086558 0.638847407928 0.279609467999 0.352440021147 0.579171072764 0.87366243 0.362374392832 0.0280832693491 0.279283856597 0.635040515443 0.832010486457 0.804308835197 0.211532601472 0.0666062295615 0.250651354476 0.195920560751'.split()]
p_squares_complements = []
for q_2 in q_squares:
    p_squares_complements.append((1 - (1 - q_2 ** 0.5) ** 2))
print(' '.join(str(prob) for prob in p_squares_complements))