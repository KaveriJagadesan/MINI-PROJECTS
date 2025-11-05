def bayes_theorem(p_disease, p_positive_given_disease, p_negative_given_no_disease):
    """
    Calculate P(Disease | Positive) using Bayes' Theorem.

    Parameters:
    p_disease (float): Probability of having the disease (prevalence)
    p_positive_given_disease (float): Sensitivity - probability of a positive test given disease
    p_negative_given_no_disease (float): Specificity - probability of a negative test given no disease

    Returns:
    float: Probability of having the disease given a positive test result
    """
    # Complementary probabilities
    p_no_disease = 1 - p_disease
    p_positive_given_no_disease = 1 - p_negative_given_no_disease

    # Marginal probability of testing positive
    p_positive = (p_positive_given_disease * p_disease) + (p_positive_given_no_disease * p_no_disease)

    # Apply Bayes' Theorem
    p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive

    return p_disease_given_positive


# Example usage:
p_disease = 0.01  # 1% of people have the disease
p_positive_given_disease = 0.95  # 95% sensitivity
p_negative_given_no_disease = 0.90  # 90% specificity

result = bayes_theorem(p_disease, p_positive_given_disease, p_negative_given_no_disease)
print(f"P(Disease | Positive) = {result:.4f} ({result*100:.2f}%)")
