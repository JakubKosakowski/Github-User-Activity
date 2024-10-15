__app_name__ = 'github-user-activity'
__version__ = '0.1.0'

(
    SUCCESS,
    HTTP_ERROR,
    TIMEOUT_ERROR
) = range(3)

ERRORS = {
    HTTP_ERROR: 'http error',
    TIMEOUT_ERROR: 'request timed out'
}

EVENTS = {
    'CommitCommentEvent': {'info': "Commit {} in {}", 'payload': 'action'},
    'CreateEvent': {'info': 'Created {} event to {}', 'payload': 'ref'},
    'DeleteEvent': {'info': 'Deleted {} event from {}', 'payload': 'ref'},
    'ForkEvent': {'info': 'Created fork to repository {}', 'payload': 'forkee'},
    'GollumEvent': {'info': '{}{}', 'payload': 'pages'},
    'IssueCommentEvent': {'info': 'Issue comment was {} in {}', 'payload': 'action'},
    'IssuesEvent': {'info': 'Issue comment was {} in {}', 'payload': 'action'},
    'MemberEvent': {'info': 'New member was added to {}', 'payload': 'action'},
    'PublicEvent': {'info': 'Repository {} visibility was changed to "public"', 'payload': None},
    'PullRequestEvent': {'info': 'Pull request {} in {}', 'payload': 'action'},
    'PullRequestReviewEvent': {'info': 'Pull request review {} in {}', 'payload': 'action'},
    'PullRequestReviewCommentEvent': {'info': 'Pull request review comment {} in {}', 'payload': 'action'},
    'PullRequestReviewThreadEvent': {'info': 'Pull request review thread {} in {}', 'payload': 'action'},
    'PushEvent': {"info": "Pushed {} commits to {}", 'payload': 'size'},
    'ReleaseEvent': {'info': 'Repository {} was released', 'payload': 'action'},
    'SponsorshipEvent': {'info': 'Sponsorship was {} in {}', 'payload': 'action'},
    'WatchEvent': {'info': 'User {} star {}', 'payload': 'action'}
}