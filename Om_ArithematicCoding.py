from collections import Counter

def calculate_frequencies(message):
    # Count the frequency of each symbol in the message
    frequency = Counter(message)
    total_symbols = len(message)
    # Calculate probabilities
    probabilities = {symbol: freq / total_symbols for symbol, freq in frequency.items()}
    return frequency, probabilities

def calculate_intervals(probabilities):
    # Calculate cumulative intervals for each symbol
    intervals = {}
    cumulative_probability = 0.0
    for symbol, prob in sorted(probabilities.items()):
        intervals[symbol] = (cumulative_probability, cumulative_probability + prob)
        cumulative_probability += prob
    return intervals

def arithmetic_encode(message, intervals):
    low = 0.0
    high = 1.0
    
    for symbol in message:
        symbol_low, symbol_high = intervals[symbol]
        range_ = high - low
        high = low + range_ * symbol_high
        low = low + range_ * symbol_low
    
    return (low + high) / 2  # The encoded value

def arithmetic_coding(message):
    frequency, probabilities = calculate_frequencies(message)
    intervals = calculate_intervals(probabilities)
    encoded_value = arithmetic_encode(message, intervals)
    return encoded_value, intervals

# Example message
message = "abacabad"

# Perform arithmetic coding
encoded_value, intervals = arithmetic_coding(message)

print("Symbol Intervals:")
for symbol, interval in intervals.items():
    print(f"
