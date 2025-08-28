# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main

# Test your function by calling it here
from demographic_data_analyzer import calculate_demographic_data

calculate_demographic_data()

# Run unit tests automatically
main(module='test_module', exit=False)