class TestFirst:
    def test_short_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "Phrase length is not shorter than 15"