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
#     result = channel_from_dict(json.loads(json_string))

from typing import Any, List, Optional, TypeVar, Callable, Type, cast
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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


class Command:
    name: str
    description: str
    args: str
    set: str

    def __init__(self, name: str, description: str, args: str, set: str) -> None:
        self.name = name
        self.description = description
        self.args = args
        self.set = set

    @staticmethod
    def from_dict(obj: Any) -> 'Command':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        args = from_str(obj.get("args"))
        set = from_str(obj.get("set"))
        return Command(name, description, args, set)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["args"] = from_str(self.args)
        result["set"] = from_str(self.set)
        return result


class Config:
    created_at: datetime
    updated_at: datetime
    name: str
    typing_events: bool
    read_events: bool
    connect_events: bool
    search: bool
    reactions: bool
    replies: bool
    quotes: bool
    mutes: bool
    uploads: bool
    url_enrichment: bool
    custom_events: bool
    push_notifications: bool
    message_retention: str
    max_message_length: int
    automod: str
    automod_behavior: str
    commands: List[Command]

    def __init__(self, created_at: datetime, updated_at: datetime, name: str, typing_events: bool, read_events: bool, connect_events: bool, search: bool, reactions: bool, replies: bool, quotes: bool, mutes: bool, uploads: bool, url_enrichment: bool, custom_events: bool, push_notifications: bool, message_retention: str, max_message_length: int, automod: str, automod_behavior: str, commands: List[Command]) -> None:
        self.created_at = created_at
        self.updated_at = updated_at
        self.name = name
        self.typing_events = typing_events
        self.read_events = read_events
        self.connect_events = connect_events
        self.search = search
        self.reactions = reactions
        self.replies = replies
        self.quotes = quotes
        self.mutes = mutes
        self.uploads = uploads
        self.url_enrichment = url_enrichment
        self.custom_events = custom_events
        self.push_notifications = push_notifications
        self.message_retention = message_retention
        self.max_message_length = max_message_length
        self.automod = automod
        self.automod_behavior = automod_behavior
        self.commands = commands

    @staticmethod
    def from_dict(obj: Any) -> 'Config':
        assert isinstance(obj, dict)
        created_at = from_datetime(obj.get("created_at"))
        updated_at = from_datetime(obj.get("updated_at"))
        name = from_str(obj.get("name"))
        typing_events = from_bool(obj.get("typing_events"))
        read_events = from_bool(obj.get("read_events"))
        connect_events = from_bool(obj.get("connect_events"))
        search = from_bool(obj.get("search"))
        reactions = from_bool(obj.get("reactions"))
        replies = from_bool(obj.get("replies"))
        quotes = from_bool(obj.get("quotes"))
        mutes = from_bool(obj.get("mutes"))
        uploads = from_bool(obj.get("uploads"))
        url_enrichment = from_bool(obj.get("url_enrichment"))
        custom_events = from_bool(obj.get("custom_events"))
        push_notifications = from_bool(obj.get("push_notifications"))
        message_retention = from_str(obj.get("message_retention"))
        max_message_length = from_int(obj.get("max_message_length"))
        automod = from_str(obj.get("automod"))
        automod_behavior = from_str(obj.get("automod_behavior"))
        commands = from_list(Command.from_dict, obj.get("commands"))
        return Config(created_at, updated_at, name, typing_events, read_events, connect_events, search, reactions, replies, quotes, mutes, uploads, url_enrichment, custom_events, push_notifications, message_retention, max_message_length, automod, automod_behavior, commands)

    def to_dict(self) -> dict:
        result: dict = {}
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        result["name"] = from_str(self.name)
        result["typing_events"] = from_bool(self.typing_events)
        result["read_events"] = from_bool(self.read_events)
        result["connect_events"] = from_bool(self.connect_events)
        result["search"] = from_bool(self.search)
        result["reactions"] = from_bool(self.reactions)
        result["replies"] = from_bool(self.replies)
        result["quotes"] = from_bool(self.quotes)
        result["mutes"] = from_bool(self.mutes)
        result["uploads"] = from_bool(self.uploads)
        result["url_enrichment"] = from_bool(self.url_enrichment)
        result["custom_events"] = from_bool(self.custom_events)
        result["push_notifications"] = from_bool(self.push_notifications)
        result["message_retention"] = from_str(self.message_retention)
        result["max_message_length"] = from_int(self.max_message_length)
        result["automod"] = from_str(self.automod)
        result["automod_behavior"] = from_str(self.automod_behavior)
        result["commands"] = from_list(lambda x: to_class(Command, x), self.commands)
        return result


class User:
    id: str
    role: str
    created_at: datetime
    updated_at: datetime
    banned: bool
    online: bool
    name: str
    last_active: Optional[datetime]

    def __init__(self, id: str, role: str, created_at: datetime, updated_at: datetime, banned: bool, online: bool, name: str, last_active: Optional[datetime]) -> None:
        self.id = id
        self.role = role
        self.created_at = created_at
        self.updated_at = updated_at
        self.banned = banned
        self.online = online
        self.name = name
        self.last_active = last_active

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        role = from_str(obj.get("role"))
        created_at = from_datetime(obj.get("created_at"))
        updated_at = from_datetime(obj.get("updated_at"))
        banned = from_bool(obj.get("banned"))
        online = from_bool(obj.get("online"))
        name = from_str(obj.get("name"))
        last_active = from_union([from_datetime, from_none], obj.get("last_active"))
        return User(id, role, created_at, updated_at, banned, online, name, last_active)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["role"] = from_str(self.role)
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        result["banned"] = from_bool(self.banned)
        result["online"] = from_bool(self.online)
        result["name"] = from_str(self.name)
        result["last_active"] = from_union([lambda x: x.isoformat(), from_none], self.last_active)
        return result


class ChannelInfo:
    id: str
    type: str
    cid: str
    last_message_at: datetime
    created_at: datetime
    updated_at: datetime
    created_by: User
    frozen: bool
    disabled: bool
    config: Config
    own_capabilities: List[str]
    hidden: bool

    def __init__(self, id: str, type: str, cid: str, last_message_at: datetime, created_at: datetime, updated_at: datetime, created_by: User, frozen: bool, disabled: bool, config: Config, own_capabilities: List[str], hidden: bool) -> None:
        self.id = id
        self.type = type
        self.cid = cid
        self.last_message_at = last_message_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by
        self.frozen = frozen
        self.disabled = disabled
        self.config = config
        self.own_capabilities = own_capabilities
        self.hidden = hidden

    @staticmethod
    def from_dict(obj: Any) -> 'ChannelInfo':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        type = from_str(obj.get("type"))
        cid = from_str(obj.get("cid"))
        last_message_at = from_datetime(obj.get("last_message_at"))
        created_at = from_datetime(obj.get("created_at"))
        updated_at = from_datetime(obj.get("updated_at"))
        created_by = User.from_dict(obj.get("created_by"))
        frozen = from_bool(obj.get("frozen"))
        disabled = from_bool(obj.get("disabled"))
        config = Config.from_dict(obj.get("config"))
        own_capabilities = from_list(from_str, obj.get("own_capabilities"))
        hidden = from_bool(obj.get("hidden"))
        return ChannelInfo(id, type, cid, last_message_at, created_at, updated_at, created_by, frozen, disabled, config, own_capabilities, hidden)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["type"] = from_str(self.type)
        result["cid"] = from_str(self.cid)
        result["last_message_at"] = self.last_message_at.isoformat()
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        result["created_by"] = to_class(User, self.created_by)
        result["frozen"] = from_bool(self.frozen)
        result["disabled"] = from_bool(self.disabled)
        result["config"] = to_class(Config, self.config)
        result["own_capabilities"] = from_list(from_str, self.own_capabilities)
        result["hidden"] = from_bool(self.hidden)
        return result


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


class Channel:
    channel: ChannelInfo
    messages: List[Message]
    pinned_messages: List[Any]
    watcher_count: int
    members: List[Any]
    membership: None
    duration: str

    def __init__(self, channel: ChannelInfo, messages: List[Message], pinned_messages: List[Any], watcher_count: int, members: List[Any], membership: None, duration: str) -> None:
        self.channel = channel
        self.messages = messages
        self.pinned_messages = pinned_messages
        self.watcher_count = watcher_count
        self.members = members
        self.membership = membership
        self.duration = duration

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        channel = ChannelInfo.from_dict(obj.get("channel"))
        messages = from_list(Message.from_dict, obj.get("messages"))
        pinned_messages = from_list(lambda x: x, obj.get("pinned_messages"))
        watcher_count = from_int(obj.get("watcher_count"))
        members = from_list(lambda x: x, obj.get("members"))
        membership = from_none(obj.get("membership"))
        duration = from_str(obj.get("duration"))
        return Channel(channel, messages, pinned_messages, watcher_count, members, membership, duration)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channel"] = to_class(ChannelInfo, self.channel)
        result["messages"] = from_list(lambda x: to_class(Message, x), self.messages)
        result["pinned_messages"] = from_list(lambda x: x, self.pinned_messages)
        result["watcher_count"] = from_int(self.watcher_count)
        result["members"] = from_list(lambda x: x, self.members)
        result["membership"] = from_none(self.membership)
        result["duration"] = from_str(self.duration)
        return result


def channel_from_dict(s: Any) -> Channel:
    return Channel.from_dict(s)


def channel_to_dict(x: Channel) -> Any:
    return to_class(Channel, x)
