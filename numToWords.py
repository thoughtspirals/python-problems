# Break the Number into Chunks:

# Process the number in chunks of 3 digits (hundreds, tens, units).
# For example, 743,657,863 is broken into 743, 657, and 863.
# Convert Each Chunk to Words:

# Use helper functions to convert each 3-digit chunk into words.
# Handle hundreds, tens, and units separately.
# Add Scale Words:

# Append the appropriate scale word (e.g., "Thousand", "Million", "Billion") to each chunk based on its position.
# Combine the Results:

# Concatenate the words for all chunks to form the final result.


def number_to_words(num):
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
             "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", 
            "Eighty", "Ninety"]
    scales = ["", "Thousand", "Million", "Billion", "Trillion"]

    if num == 0:
        return "Zero"

    def convert_chunk(chunk):
        """Converts a 3-digit chunk to words."""
        if chunk == 0:
            return ""
        words = ""
        if chunk >= 100:
            words += units[chunk // 100] + " Hundred "
            chunk %= 100
        if chunk >= 20:
            words += tens[chunk // 10] + " "
            chunk %= 10
        if 10 <= chunk < 20:
            words += teens[chunk - 10] + " "
            chunk = 0
        if chunk < 10 and chunk != 0:
            words += units[chunk] + " "
        return words.strip()

    words = ""
    scale_index = 0
    while num > 0:
        chunk = num % 1000
        if chunk != 0:
            words = convert_chunk(chunk) + " " + scales[scale_index] + " " + words
        num //= 1000
        scale_index += 1

    return words.strip()

# Example usage
number = int(input("Enter a number: "))
print(f"{number} in words is: {number_to_words(number)}")