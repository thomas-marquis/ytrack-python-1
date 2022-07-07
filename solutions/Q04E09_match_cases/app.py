import os

from dock_repositories import SpaceDockRepository, SpaceDockFileRepository, SpaceDockInMemoryRepository


def init_dock_repository() -> SpaceDockRepository:
    match os.getenv('DOCK_REPOSITORY', 'IN_MEMORY').lower():
        case 'file':
            return SpaceDockFileRepository('fleet.pickle')
        case 'in_memory':
            return SpaceDockInMemoryRepository()
        case other:
            raise ValueError(f'Repository {other} does not exist')
