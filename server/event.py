# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = event_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast
from datetime import datetime
from uuid import UUID
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Reaction:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'Reaction':
        assert isinstance(obj, dict)
        return Reaction()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class User:
    id: str
    role: str
    created_at: datetime
    updated_at: datetime
    banned: bool
    online: bool
    channel_unread_count: int
    channel_last_read_at: datetime
    total_unread_count: int
    unread_channels: int
    unread_count: int
    name: str

    def __init__(self, id: str, role: str, created_at: datetime, updated_at: datetime, banned: bool, online: bool, channel_unread_count: int, channel_last_read_at: datetime, total_unread_count: int, unread_channels: int, unread_count: int, name: str) -> None:
        self.id = id
        self.role = role
        self.created_at = created_at
        self.updated_at = updated_at
        self.banned = banned
        self.online = online
        self.channel_unread_count = channel_unread_count
        self.channel_last_read_at = channel_last_read_at
        self.total_unread_count = total_unread_count
        self.unread_channels = unread_channels
        self.unread_count = unread_count
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        role = from_str(obj.get("role"))
        created_at = from_datetime(obj.get("created_at"))
        updated_at = from_datetime(obj.get("updated_at"))
        banned = from_bool(obj.get("banned"))
        online = from_bool(obj.get("online"))
        channel_unread_count = from_int(obj.get("channel_unread_count"))
        channel_last_read_at = from_datetime(obj.get("channel_last_read_at"))
        total_unread_count = from_int(obj.get("total_unread_count"))
        unread_channels = from_int(obj.get("unread_channels"))
        unread_count = from_int(obj.get("unread_count"))
        name = from_str(obj.get("name"))
        return User(id, role, created_at, updated_at, banned, online, channel_unread_count, channel_last_read_at, total_unread_count, unread_channels, unread_count, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["role"] = from_str(self.role)
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        result["banned"] = from_bool(self.banned)
        result["online"] = from_bool(self.online)
        result["channel_unread_count"] = from_int(self.channel_unread_count)
        result["channel_last_read_at"] = self.channel_last_read_at.isoformat()
        result["total_unread_count"] = from_int(self.total_unread_count)
        result["unread_channels"] = from_int(self.unread_channels)
        result["unread_count"] = from_int(self.unread_count)
        result["name"] = from_str(self.name)
        return result


class Message:
    id: UUID
    text: str
    html: str
    type: str
    user: User
    attachments: List[Any]
    latest_reactions: List[Any]
    own_reactions: List[Any]
    reaction_counts: Reaction
    reaction_scores: Reaction
    reply_count: int
    cid: str
    created_at: datetime
    updated_at: datetime
    shadowed: bool
    mentioned_users: List[Any]
    silent: bool
    pinned: bool
    pinned_at: None
    pinned_by: None
    pin_expires: None

    def __init__(self, id: UUID, text: str, html: str, type: str, user: User, attachments: List[Any], latest_reactions: List[Any], own_reactions: List[Any], reaction_counts: Reaction, reaction_scores: Reaction, reply_count: int, cid: str, created_at: datetime, updated_at: datetime, shadowed: bool, mentioned_users: List[Any], silent: bool, pinned: bool, pinned_at: None, pinned_by: None, pin_expires: None) -> None:
        self.id = id
        self.text = text
        self.html = html
        self.type = type
        self.user = user
        self.attachments = attachments
        self.latest_reactions = latest_reactions
        self.own_reactions = own_reactions
        self.reaction_counts = reaction_counts
        self.reaction_scores = reaction_scores
        self.reply_count = reply_count
        self.cid = cid
        self.created_at = created_at
        self.updated_at = updated_at
        self.shadowed = shadowed
        self.mentioned_users = mentioned_users
        self.silent = silent
        self.pinned = pinned
        self.pinned_at = pinned_at
        self.pinned_by = pinned_by
        self.pin_expires = pin_expires

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        id = UUID(obj.get("id"))
        text = from_str(obj.get("text"))
        html = from_str(obj.get("html"))
        type = from_str(obj.get("type"))
        user = User.from_dict(obj.get("user"))
        attachments = from_list(lambda x: x, obj.get("attachments"))
        latest_reactions = from_list(lambda x: x, obj.get("latest_reactions"))
        own_reactions = from_list(lambda x: x, obj.get("own_reactions"))
        reaction_counts = Reaction.from_dict(obj.get("reaction_counts"))
        reaction_scores = Reaction.from_dict(obj.get("reaction_scores"))
        reply_count = from_int(obj.get("reply_count"))
        cid = from_str(obj.get("cid"))
        created_at = from_datetime(obj.get("created_at"))
        updated_at = from_datetime(obj.get("updated_at"))
        shadowed = from_bool(obj.get("shadowed"))
        mentioned_users = from_list(lambda x: x, obj.get("mentioned_users"))
        silent = from_bool(obj.get("silent"))
        pinned = from_bool(obj.get("pinned"))
        pinned_at = from_none(obj.get("pinned_at"))
        pinned_by = from_none(obj.get("pinned_by"))
        pin_expires = from_none(obj.get("pin_expires"))
        return Message(id, text, html, type, user, attachments, latest_reactions, own_reactions, reaction_counts, reaction_scores, reply_count, cid, created_at, updated_at, shadowed, mentioned_users, silent, pinned, pinned_at, pinned_by, pin_expires)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = str(self.id)
        result["text"] = from_str(self.text)
        result["html"] = from_str(self.html)
        result["type"] = from_str(self.type)
        result["user"] = to_class(User, self.user)
        result["attachments"] = from_list(lambda x: x, self.attachments)
        result["latest_reactions"] = from_list(lambda x: x, self.latest_reactions)
        result["own_reactions"] = from_list(lambda x: x, self.own_reactions)
        result["reaction_counts"] = to_class(Reaction, self.reaction_counts)
        result["reaction_scores"] = to_class(Reaction, self.reaction_scores)
        result["reply_count"] = from_int(self.reply_count)
        result["cid"] = from_str(self.cid)
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        result["shadowed"] = from_bool(self.shadowed)
        result["mentioned_users"] = from_list(lambda x: x, self.mentioned_users)
        result["silent"] = from_bool(self.silent)
        result["pinned"] = from_bool(self.pinned)
        result["pinned_at"] = from_none(self.pinned_at)
        result["pinned_by"] = from_none(self.pinned_by)
        result["pin_expires"] = from_none(self.pin_expires)
        return result


class Event:
    type: str
    cid: str
    channel_id: str
    channel_type: str
    message: Message
    user: User
    watcher_count: int
    created_at: datetime
    message_id: UUID

    def __init__(self, type: str, cid: str, channel_id: str, channel_type: str, message: Message, user: User, watcher_count: int, created_at: datetime, message_id: UUID) -> None:
        self.type = type
        self.cid = cid
        self.channel_id = channel_id
        self.channel_type = channel_type
        self.message = message
        self.user = user
        self.watcher_count = watcher_count
        self.created_at = created_at
        self.message_id = message_id

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        cid = from_str(obj.get("cid"))
        channel_id = from_str(obj.get("channel_id"))
        channel_type = from_str(obj.get("channel_type"))
        message = Message.from_dict(obj.get("message"))
        user = User.from_dict(obj.get("user"))
        watcher_count = from_int(obj.get("watcher_count"))
        created_at = from_datetime(obj.get("created_at"))
        message_id = UUID(obj.get("message_id"))
        return Event(type, cid, channel_id, channel_type, message, user, watcher_count, created_at, message_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["cid"] = from_str(self.cid)
        result["channel_id"] = from_str(self.channel_id)
        result["channel_type"] = from_str(self.channel_type)
        result["message"] = to_class(Message, self.message)
        result["user"] = to_class(User, self.user)
        result["watcher_count"] = from_int(self.watcher_count)
        result["created_at"] = self.created_at.isoformat()
        result["message_id"] = str(self.message_id)
        return result


def event_from_dict(s: Any) -> Event:
    return Event.from_dict(s)


def event_to_dict(x: Event) -> Any:
    return to_class(Event, x)
