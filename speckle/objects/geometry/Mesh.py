# generated by datamodel-codegen:
#   filename:  Mesh.json
#   timestamp: 2020-11-24T16:33:16+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Mesh(BaseModel):
    vertices: Optional[List[float]] = None
    faces: Optional[List[int]] = None
    colors: Optional[List[int]] = None
    textureCoordinates: Optional[List[float]] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None
