from re import sub
from template2instance import get_license_short_text

def current_year(_: dict) -> str:
    from datetime import datetime
    return int(datetime.now().year)


def license_reference(variables: dict) -> str:
    """
    This function returns the license reference for the project.

    Parameters
    ----------
    variables : dict
        The variables of the project
    
    Returns
    -------
    str
        The license reference for the project
    """
    return get_license_short_text(variables["PACKAGE_LICENSE"])
