from src.ducklings import parameter_ducks


class TestParameterDucks:
    def test_list_to_list(self):
        x = ["one", "two"]
        y = parameter_ducks.duck_sequence(x)
        assert x == y

    def test_instance_to_list(self):
        x = "one"
        y = parameter_ducks.duck_sequence(x)

        assert isinstance(y, list)
        assert len(y) == 1
        assert y[0] == "one"

    def test_instance_to_set(self):
        x = "one"
        y = parameter_ducks.duck_sequence(x, set)

        assert isinstance(y, set)
        assert len(y) == 1
        assert "one" in y

    def test_decorator(self):
        @parameter_ducks.duck_sequence_param("test")
        def my_func(_, test: parameter_ducks.SeqOR[str]):
            return test

        x = ["one"]
        one = my_func(0, x)
        assert one == x

        x = ["one"]
        two = my_func(0, test=x)
        assert two == x

        three = my_func(0, "one")
        assert isinstance(three, list)
        assert three[0] == "one"

        four = my_func(0, test="one")
        assert isinstance(four, list)
        assert four[0] == "one"
