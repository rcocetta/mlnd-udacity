
p_freedom_jill = 0.1
p_immigration_jill = 0.1
p_environment_jill = 0.8

p_freedom_gary = 0.7
p_immigration_gary = 0.2
p_environment_gary = 0.1



p_jill_text = 0.5 * p_immigration_jill * p_freedom_jill
p_gary_text = 0.5 * p_immigration_gary * p_freedom_gary
print('P(G|F,I) = {}'.format(p_gary_text))
print('P(J|F,I) = {}'.format(p_jill_text))

p_freedom_immigration = p_jill_text + p_gary_text
print('P(F,I) = {}'.format(p_freedom_immigration))

p_jill_freedom_immigration = p_jill_text / p_freedom_immigration
print('P(J|F,I) = {}'.format(p_jill_freedom_immigration))

p_gary_freedom_immigration = p_gary_text / p_freedom_immigration
print('P(G|F,I) = {}'.format(p_gary_freedom_immigration))
