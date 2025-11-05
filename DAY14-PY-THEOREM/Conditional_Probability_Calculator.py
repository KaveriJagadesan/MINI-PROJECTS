def conditional_probability(p_a_and_b, p_b):
    """
    Calculate the conditional probability P(A|B).

    Parameters:
    p_a_and_b (float): Probability of both events A and B occurring.
    p_b (float): Probability of event B occurring.

    Returns:
    float: The conditional probability P(A|B).
    """
    if p_b == 0:
        raise ValueError("The probability of event B (p_b) cannot be zero.")
    
    return p_a_and_b / p_b


# Example usage:
# P(Rain AND Sprinklers) = 0.05
# P(Sprinklers) = 0.1
result = conditional_probability(0.05, 0.1)
print("P(Rain | Sprinklers) =", result)
