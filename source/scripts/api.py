def validate_per_page(value) -> int:
    """Check value of parameter in call to GitHub API.
    
    ---
    ### Parameters
    - `value` `Any`
    
    ---
    ### Returns
    - `int`: even if value of `per_page` parameter is invalid"""
    if not 1 <= value <= 100:
        errStr = f"Invalid value \"results\". Should be from 1 to 100, not {value} Listing 100 results:"
        logger.error(errStr)
        print("\n" + errStr, "red")
        return 100
    else:
        return value


def is_status_code_ok(status_code: int) -> bool:
    """Check value of response status code.
    
    ---
    ### Parameters
    - `status_code` `int`
    
    ---
    ### Returns
    - `True`: if status code is 200 (OK)
    - `False`: if status code is not 200 (OK)"""
    logger.debug(f"{status_code=}")
    if status_code == 404:
        errStr = 'Invalid user name'
        logger.error(errStr)
        print("\n" + errStr, "red")
        return False
    elif status_code == 422:
        errStr = 'Pagination is limited for this resource'
        logger.error(errStr)
        print("\n" + errStr, "red")
        return False
    else: return True


def fetch_data(user_name, per_page: int = 100, page: int = 1) -> (list | None):
    """Pull data using GitHub API and return it.
    
    ---
    ### Parameters
    - `user_name` `str`: real user name on GitHub
    - `page` `int`: page number that represents results
    - `per_page` `int`: amount of results represented on each page
    
    ---
    ### Returns
    - `list`: items in dict format of user activity
    - `None`: if response status code by GitHub API is not 200 (OK)"""
    per_page = validate_per_page(per_page)
    call = f"https://api.github.com/users/{user_name}/events?per_page={per_page}&page={page}"
    response = rq.get(call)
    if not is_status_code_ok(response.status_code): return None
    data = response.json()
    return data


if __name__ != "__main__":
    import requests as rq
    import logging as lg
    
    # get logger
    logger = lg.getLogger(name=__name__)