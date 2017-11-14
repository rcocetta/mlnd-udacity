# P(D)
p_diabetes = 0.01

# P(~D)
p_no_diabetes = 0.99

# Sensitivity or P(Pos|D)
p_pos_diabetes = 0.9

# Specificity or P(Neg/~D)
p_neg_no_diabetes = 0.9


p_pos = (p_diabetes * p_pos_diabetes) + (p_no_diabetes * (1 - p_neg_no_diabetes))


p_d_pos = p_diabetes * p_pos_diabetes / p_pos
p_notd_pos = p_no_diabetes * (1 - p_neg_no_diabetes) / p_pos

print('The probability of getting a positive test result P(Pos) is: {}',format(p_pos))
print('The probability of being a diabetic with a positive test result is P(D|Pos) is: {}',format(p_d_pos))
print('The probability of being a not diabetic with a positive test result is P(D|Pos) is: {}',format(p_notd_pos))