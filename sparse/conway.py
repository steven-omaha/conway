from types_conway import Cell, Field

NEAR = (-1, 0, 1)
NEIGHBOUR_OFFSETS: Field = set([(x, y) for x in NEAR for y in NEAR if not (x, y) == (0, 0)])


def iterate(field: Field) -> Field:
    to_maintain = _maintain_alive_cells(field)
    to_spawn = _spawn_new_cells(field)
    return to_maintain.union(to_spawn)


def _get_neighbours(cell: Cell) -> Field:
    x, y = cell
    neighbours = {(x + dx, y + dy) for dx, dy in NEIGHBOUR_OFFSETS}
    return neighbours


def _get_alive_neighbour_count(cell: Cell, field: Field) -> int:
    return sum([1 for neighbour in _get_neighbours(cell) if neighbour in field])


def _get_dead_cells_adjacent_to_alive_cells(field: Field) -> Field:
    adjacent_dead_cells = set()
    for cell in field:
        [adjacent_dead_cells.add(neighbour) for neighbour in _get_neighbours(cell) if neighbour not in field]
    return adjacent_dead_cells


def _spawn_new_cells(field: Field) -> Field:
    return {cell for cell in _get_dead_cells_adjacent_to_alive_cells(field)
            if _get_alive_neighbour_count(cell, field) == 3}


def _maintain_alive_cells(field: Field) -> Field:
    return {cell for cell in field if _get_alive_neighbour_count(cell, field) in (2, 3)}
