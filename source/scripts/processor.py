# ================
# Unused functions
# ================
def create_storage(dataPath: str) -> None:
    """Create storage in JSON format for fetched data.
    
    ---
    ### Parameters:
    - `dataPath` `str`: a full path to the file"""
    dataDir, _ = os.path.split(dataPath)
    if not os.path.exists(dataDir):
        os.mkdir(dataDir)
    if not os.path.exists(dataPath):
        with open(dataPath, "w", encoding="utf-8"): pass


def set_data(data: dict, dataPath: str) -> None:
    """Save data in JSON format to the storage.
    Turn dict type file into JSON object.
    
    ---
    ### Parameters
    - `data` `dict`: data itself in dict type
    - `dataPath` `str`: path to the storage file"""
    create_storage(dataPath)  # create storage if doesn't exist
    with open(file=dataPath, mode="w", encoding="utf-8") as file:
        js.dump(data, file, indent=4)
        

def get_data(dataPath: str) -> dict:
    """Pull data from storage and return it in dict type.
    
    ---
    ### Parameters
    - `dataPath` `str`: path to the storage"""
    with open(file=dataPath, mode="r", encoding="utf-8") as file:
        return js.load(file)


# ==============
# Used functions
# ==============
def process_data(user_name: str, per_page: int = 100, page: int = 1) -> None:
    """Fetch data using GitHub API and show results in CLI.
    
    ---
    ### Parameters
    - `user_name` `str`: real user name on GitHub
    - `page` `int`: page number that represents results
    - `per_page` `int`: amount of results represented on each page"""
    data = api.fetch_data(user_name, per_page, page)  # call data using GitHub API
    if data == None: return  # stop execution if no data represented
    logger.debug(f"{len(data)=} {data=}")
    events = get_events(data)  # get list of string of activities by event type
    # show user activity
    if len(data) != 0:
        print()
        for e in events:
            print(f"{e}")
    else:
        print("\nNo events...", "grey")


def get_events(data: list) -> list:
    """Get data in list of strings fromat from JSON object.
    
    ---
    ### Parameters
    - `data` `list`: data itself gotten by GitHub API
    
    ---
    ### Returns
    - `list`: list of strings of information about user activity"""
    events = []
    for event in data:
        time = f"{event["created_at"][:10]} {event["created_at"][11:-1]}"
        repo = event["repo"]["name"]
        payload = event["payload"]
        logger.debug(f"{time=} {repo=} {payload=}")
        match event["type"]:
            case "WatchEvent":
                eventStr = f"starred repository"
            case "PushEvent":
                eventStr = f"pushed {len(payload["commits"])} {"commits" if len(payload["commits"]) > 1 else "commit"}"
            case "CreateEvent":
                eventStr = f'created {payload["ref_type"]}{f' "{payload["ref"]}"' if payload["ref"] != None else ""}'
            case "CommitCommentEvent":
                eventStr = f"commented commit"
            case "DeleteEvent":
                eventStr = f"deleted {payload["ref_type"]}{f' "{payload["ref"]}"' if payload["ref"] != None else ""}"
            case "ForkEvent":
                eventStr = f'{payload["forkee"]["owner"]["login"]} forked repository'
            case "GollumEvent":
                eventStr = ''
                for page in payload["pages"]:
                    eventStr += f'{page["action"]} a wiki page "{page["page_name"]}"' + (", " if page != payload["pages"][-1] else "")
            case "IssueCommentEvent":
                eventStr = f'{payload["action"]} an issue #{payload["issue"]["number"]}'
            case "IssuesEvent":
                eventStr = f'{payload["action"]} an issue #{payload["issue"]["number"]}'
            case "MemberEvent":
                eventStr = f'{payload["action"]} {payload["member"]["name"]}'
            case "PublicEvent":
                eventStr = f'made public'
            case "PullRequestEvent":
                eventStr = f'{payload["action"]} the pull request #{payload["number"]}'
            case "PullRequestReviewEvent":
                eventStr = f'{payload["action"]} review on the pull request #{payload["pull_request"]["number"]}'
            case "PullRequestReviewCommentEvent":
                eventStr = f'{payload["action"]} comment to the review on the pull request #{payload["pull_request"]["number"]}'
            case "PullRequestReviewThreadEvent":
                eventStr = f'{payload["action"]} comment thread on the pull request #{payload["pull_request"]["number"]}'
            case "PushEvent":
                eventStr = f'pushed {payload["size"]} commits'
            case "ReleaseEvent":
                eventStr = f'{payload["action"]} release #{payload["release"]["release_id"]}'
            case "SponsorshipEvent":
                eventStr = f'{payload["action"]} sponsorship list'
        events.append(f"{time} {repo} {eventStr}")
    logger.debug(f"{events=}")
    return events
    
    
if __name__ != "__main__":
    import json as js
    import os
    import logging as lg
    
    from . import api
    
    # get logger
    logger = lg.getLogger(name=__name__)
    