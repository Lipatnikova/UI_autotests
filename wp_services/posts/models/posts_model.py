from typing import List

from pydantic import BaseModel, RootModel, Field, HttpUrl


class Guid(BaseModel):
    rendered: HttpUrl


class Title(BaseModel):
    rendered: str


class Content(BaseModel):
    rendered: str
    protected: bool


class Excerpt(BaseModel):
    rendered: str
    protected: bool


class Meta(BaseModel):
    footnotes: str


class SelfItem(BaseModel):
    href: HttpUrl


class CollectionItem(BaseModel):
    href: HttpUrl


class AboutItem(BaseModel):
    href: HttpUrl


class AuthorItem(BaseModel):
    embeddable: bool
    href: HttpUrl


class Reply(BaseModel):
    embeddable: bool
    href: HttpUrl


class VersionHistoryItem(BaseModel):
    count: int
    href: HttpUrl


class PredecessorVersionItem(BaseModel):
    id: int
    href: HttpUrl


class WpAttachmentItem(BaseModel):
    href: HttpUrl


class WpTermItem(BaseModel):
    taxonomy: str
    embeddable: bool
    href: HttpUrl


class Curie(BaseModel):
    name: str
    href: HttpUrl
    templated: bool


class _Links(BaseModel):
    self: List[SelfItem]
    collection: List[CollectionItem]
    about: List[AboutItem]
    author: List[AuthorItem]
    replies: List[Reply]
    version_history: List[VersionHistoryItem] = Field(..., alias='version-history')
    predecessor_version: List[PredecessorVersionItem] = Field(
        ..., alias='predecessor-version'
    )
    wp_attachment: List[WpAttachmentItem] = Field(..., alias='wp:attachment')
    wp_term: List[WpTermItem] = Field(..., alias='wp:term')
    curies: List[Curie]


class PostModel(BaseModel):
    id: int
    date: str
    date_gmt: str
    guid: Guid
    modified: str
    modified_gmt: str
    slug: str
    status: str
    type: str
    link: HttpUrl
    title: Title
    content: Content
    excerpt: Excerpt
    author: int
    featured_media: int
    comment_status: str
    ping_status: str
    sticky: bool
    template: str
    format: str
    meta: Meta
    categories: List[int]
    tags: List
    _links: _Links


class AllPostsModel(RootModel):
    root: List[PostModel]


class PayloadCreatePost(BaseModel):
    title: str
    content: str
    status: str
    comment_status: str
    ping_status: str


class PayloadUpdatePost(BaseModel):
    title: str
    content: str
    comment_status: str
