from dataclasses import dataclass, field

@dataclass
class Flashcard:
    front: str
    back: str
    source_language: str
    target_language: str
    example: str = ""
    example_translation: str = ""
    notes: str = ""
    tags: list[str] = field(default_factory=list)
