from unittest.mock import patch
from dailizabot.main import dailiza_answer, run_dailiza_bot


def test_dailiza_answer():
    user_input = "Wie geht es dir denn so?"
    expected_responses = [
        "Danke. Mir geht es gut und dir?",
        "Sehr gut, danke. Und wie läuft's bei dir?",
        "Ich kann nicht klagen. Was ist mit dir?"
    ]

    response = dailiza_answer(user_input)
    assert response in expected_responses, f"Unexpected response: {response}"


def test_run_dailiza_bot(capfd):
    user_input = ["asdkjhwez", "exit"]
    
    with patch('builtins.input', side_effect=user_input):
        run_dailiza_bot()
    
    captured_output = capfd.readouterr().out.splitlines()

    assert captured_output[0] == "Hey Hallo! Ich bin Dailiza. Womit kann ich dir helfen?"
    assert "Das habe ich nicht verstanden." in captured_output[2]
