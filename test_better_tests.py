from writing_better_tests import handle_rate_limit


def test_handle_without_rate_limit():
    fake_response = {
    }
    rate_limit = handle_rate_limit(fake_response)
    assert rate_limit is False


def test_handle_with_rate_limit():
    fake_response = {
        'standoff_time': 5
    }
    rate_limit = handle_rate_limit(fake_response)
    assert rate_limit is True
