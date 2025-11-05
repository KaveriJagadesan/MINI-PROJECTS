import random

def simulate_coin_flips(num_flips=1000):
    """
    Simulate a number of coin flips and calculate the probability of getting heads.

    Parameters:
    num_flips (int): Number of times the coin is flipped.

    Returns:
    float: Estimated probability of getting heads.
    """
    heads_count = 0

    for _ in range(num_flips):
        flip = random.randint(0, 1)  # 0 = Tails, 1 = Heads
        if flip == 1:
            heads_count += 1

    probability_of_heads = heads_count / num_flips
    return probability_of_heads


# Example usage:
result = simulate_coin_flips(1000)
print(f"Estimated Probability of Heads after 1000 flips: {result:.3f}")
