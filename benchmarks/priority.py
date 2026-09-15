def normalize(items):
    """Return validated, normalized priority records without mutating input."""
    raise NotImplementedError


def ordered(items):
    """Return records ordered high, medium, low while preserving ties."""
    raise NotImplementedError


def counts(items):
    """Return counts for every supported priority, including zeroes."""
    raise NotImplementedError
