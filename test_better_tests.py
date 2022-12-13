from writing_better_tests import handle_rate_limit
from itertools import cycle
from unittest.mock import MagicMock

def test_handle_without_rate_limit():
    fake_response = {
    }
    rate_limit = handle_rate_limit(fake_response)
    assert rate_limit is False


def test_handle_with_rate_limit(mocker):
    fake_time = mocker.patch('writing_better_tests.time', autospec=True)
    #fake_time.sleep.side_effect = lambda x: print('Somebody called sleep!')
    #fake_time.sleep.side_effect = cycle([1, 2, ValueError])
    #fake_time.sleep.side_effect = ValueError
    #fake_time.sleep.side_effect = lambda x: True 
    fake_response = {
        'standoff_time': 5
    }
    spy_response = MagicMock()
    spy_response.__getitem__.side_effect = fake_response.__getitem__
    rate_limit = handle_rate_limit(spy_response)
    assert rate_limit is True
    assert fake_time.sleep.call_count == 1
    print(spy_response.__getitem__.call_args_list)
    # print(fake_time.sleep.call_count)
    # print(fake_time.sleep.called)
    # print(fake_time.sleep.call_args_list)
    # print(fake_time.sleep.call_args)
