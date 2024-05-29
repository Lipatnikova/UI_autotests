from typing import List

from pydantic import BaseModel, field_validator


class Guid(BaseModel):
    rendered: str
    raw: str


class Title(BaseModel):
    raw: str
    rendered: str


class Content(BaseModel):
    raw: str
    rendered: str
    protected: bool
    block_version: int


class Excerpt(BaseModel):
    raw: str
    rendered: str
    protected: bool


class Meta(BaseModel):
    footnotes: str


class Previous(BaseModel):
    id: int
    date: str
    date_gmt: str
    guid: Guid
    modified: str
    modified_gmt: str
    password: str
    slug: str
    status: str
    type: str
    link: str
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
    permalink_template: str
    generated_slug: str


class PostModelDel(BaseModel):
    deleted: bool
    previous: Previous


@field_validator('deleted')
def check_deleted_value(deleted):
    if deleted != True:
        raise ValueError('The deleted value must be set to True')
    return deleted
