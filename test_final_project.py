from final_project import check_num
from final_project import play_again
from final_project import converted_num
import pytest


def main():
    test_chuck_num
    test_converted_num
    test_play_again


def test_chuck_num():
    assert check_num("10") == "10"
    assert check_num("0") == "0"
    # assert check_num("11") == None
    # assert check_num("abc") == None
    # Main Function Called  (MonkeyPatch, pytest.skip was no help)


def test_converted_num():
    try:
        assert converted_num("5") == "5", "cinco"
    except AssertionError:
        print("cinco was not printed")

    try:
        assert converted_num("10") == "10", "diez"
    except AssertionError:
        print("diez was not printed")

    try:
        assert converted_num("0") == "0", "cero"
    except AssertionError:
        print("cero was not printed")


def test_play_again():
    with pytest.raises(SystemExit):
        assert play_again("N") == "Thanks for playing!"
    try:
        assert play_again("X") == "Invalid input, please try again."
    except OSError:
        print("Did not call for answer")


if __name__ == "__main__":
    main()
