# generated by datamodel-codegen:
#   filename:  Wall.json
#   timestamp: 2020-11-24T16:33:37+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class IGeometry(BaseModel):
    __root__: Optional[Dict[str, Any]]


class Mesh(BaseModel):
    vertices: Optional[List[float]] = None
    faces: Optional[List[int]] = None
    colors: Optional[List[int]] = None
    textureCoordinates: Optional[List[float]] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None


class Level(BaseModel):
    name: Optional[Optional[str]] = None
    elevation: Optional[float] = None
    baseGeometry: Optional[IGeometry] = None
    displayMesh: Optional[Mesh] = None
    type: Optional[Optional[str]] = None
    level: Optional[Level] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None


class Wall(BaseModel):
    height: Optional[float] = None
    baseGeometry: Optional[IGeometry] = None
    displayMesh: Optional[Mesh] = None
    type: Optional[Optional[str]] = None
    level: Optional[Level] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None


Level.update_forward_refs()
