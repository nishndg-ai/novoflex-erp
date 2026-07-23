from __future__ import annotations


class WorkflowException(Exception):
    """
    Base workflow exception.
    """


class WorkflowNotFoundError(WorkflowException):
    """
    Raised when a workflow definition cannot be found.
    """


class InvalidWorkflowStateError(WorkflowException):
    """
    Raised when a workflow state is invalid.
    """


class InvalidWorkflowTransitionError(WorkflowException):
    """
    Raised when a transition is not allowed.
    """


class WorkflowAuthorizationError(WorkflowException):
    """
    Raised when the current user is not authorized
    to execute a workflow transition.
    """


class WorkflowCommentRequiredError(WorkflowException):
    """
    Raised when a transition requires a comment.
    """