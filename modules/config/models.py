from dataclasses import dataclass, asdict


@dataclass
class SessionConfig:
    def __str__(self):
        return f'{self.phone} - {self.id} - {self.profile_name} {f"- @{self.username}" if self.username else ""}'

    def json(self):
        return asdict(self)

    phone: str
    profile_name: str
    id: int
    username: str | None = None
