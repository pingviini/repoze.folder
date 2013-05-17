from repoze.folder.interfaces import (
    IObjectAddedEvent,
    IObjectWillBeAddedEvent,
    IObjectRemovedEvent,
    IObjectWillBeRemovedEvent,
)
from zope.interface import implementer


class _ObjectEvent(object):
    def __init__(self, object, parent, name):
        self.object = object
        self.parent = parent
        self.name = name


@implementer(IObjectAddedEvent)
class ObjectAddedEvent(_ObjectEvent):
    """ObjectAddedEvent."""


@implementer(IObjectWillBeAddedEvent)
class ObjectWillBeAddedEvent(_ObjectEvent):
    """ObjectWillBeAddedEvent."""


@implementer(IObjectRemovedEvent)
class ObjectRemovedEvent(_ObjectEvent):
    """ObjectRemovedEvent."""


@implementer(IObjectWillBeRemovedEvent)
class ObjectWillBeRemovedEvent(_ObjectEvent):
    """ObjectWillBeRemovedEvent."""
