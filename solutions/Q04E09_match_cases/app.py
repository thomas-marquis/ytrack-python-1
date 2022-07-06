import os

from dock_repositories import SpaceDockRepository, SpaceDockFileRepository, SpaceDockInMemoryRepository


def init_dock_repository() -> SpaceDockRepository:
    match os.getenv('DOCK_REPOSITORY', 'IN_MEMORY').lower():
        case 'in_memory':
            return SpaceDockFileRepository('fleet.pickle')
        case 'file':
            return SpaceDockInMemoryRepository()
        case other:
            raise ValueError(f'Repository {other} does not exist')
