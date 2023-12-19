def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key

# Example usage:
scores = {'Alice': 90, 'Bob': 75, 'Charlie': 88, 'David': 95}
best = best_score(scores)
print(f"The student with the best score is: {best}")

