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
    'CommitCommentEvent': '',
    'CreateEvent': '',
    'DeleteEvent': '',
    'ForkEvent': '',
    'GollumEvent': '',
    'IssueCommentEvent': '',
    'IssuesEvent': '',
    'MemberEvent': '',
    'PublicEvent': '',
    'PullRequestEvent': '',
    'PullRequestReviewEvent': '',
    'PullRequestReviewCommentEvent': '',
    'PullRequestReviewThreadEvent': '',
    'PushEvent': "Pushed {} commits to {}",
    'ReleaseEvent': '',
    'SponsorshipEvent': '',
    'WatchEvent': ''
}