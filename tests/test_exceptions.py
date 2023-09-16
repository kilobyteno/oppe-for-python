from oppe.exceptions import EventRequestError, OppeError, UuidValidationError


def test_default_parameters():
    """ Test default parameters """
    error = OppeError()
    assert error.msg == 'Unknown error occurred'
    assert error.data is None


def test_custom_parameters():
    """ Test custom parameters """
    error = OppeError(msg='Custom error message', data={'key': 'value'})
    assert error.msg == 'Custom error message'
    assert error.data == {'key': 'value'}


def test_empty_string_message():
    """ Test empty string message """
    error = OppeError('')
    assert error.msg == ''
    assert error.data is None


def test_with_only_msg_attribute():
    """ Test with only msg attribute """
    error = OppeError('Error message')
    assert str(error) == 'Error message'


def test_subclass_uuid_validation_error():
    """ Test subclass UuidValidationError """
    error = UuidValidationError(msg='Uuid Validation Error')
    assert error.msg == 'Uuid Validation Error'
    assert error.data is None


def test_subclass_event_request_error():
    """ Test subclass EventRequestError """
    error = EventRequestError(msg='Event Request Error')
    assert error.msg == 'Event Request Error'
    assert error.data is None
