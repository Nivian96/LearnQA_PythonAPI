class TestInput:
    def test_check_len_phrase(self):
        expected_boundary_value = 15
        phrase = input(f"Enter any phrase shorter than {expected_boundary_value} characters: ")
        assert len(phrase) < expected_boundary_value, f"The entered phrase has {expected_boundary_value} or more characters"
