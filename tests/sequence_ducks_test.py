from src.ducklings import sequence_ducks


class TestGetTwosFromList:
    def test_two_from_list_three(self):
        inp = ["one", "two", "three"]
        out = [("one", "two"), ("two", "three")]
        result = sequence_ducks.get_2_from_list(inp)

        assert len(out) == len(result)
        for test in zip(out, result):
            assert test[0] == test[1]

    def test_two_from_list_two(self):
        inp = ["one", "two"]
        out = [("one", "two")]
        result = sequence_ducks.get_2_from_list(inp)

        assert len(out) == len(result)
        for test in zip(out, result):
            assert test[0] == test[1]

    def test_two_from_list_one(self):
        inp = ["one"]
        result = sequence_ducks.get_2_from_list(inp)

        assert len(result) == 0
