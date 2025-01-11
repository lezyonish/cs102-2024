import pathlib
import typing as tp
import random

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    return [values[i:i + n] for i in range(0, len(values), n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    row_idx = pos[0]
    return grid[row_idx]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    col_idx = pos[1]
    return [grid[row_idx][col_idx] for row_idx in range(9)]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    block_row, block_col = pos[0] // 3, pos[1] // 3
    block = []
    for i in range(block_row * 3, (block_row + 1) * 3):
        for j in range(block_col * 3, (block_col + 1) * 3):
            block.append(grid[i][j])
    return block


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    for row_idx in range(9):
        for col_idx in range(9):
            if grid[row_idx][col_idx] == '.':
                return (row_idx, col_idx)
    return None


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    row_vals = set(get_row(grid, pos))
    col_vals = set(get_col(grid, pos))
    block_vals = set(get_block(grid, pos))

    all_vals = set("123456789")
    used_vals = row_vals | col_vals | block_vals

    return all_vals - used_vals


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    empty_pos = find_empty_positions(grid)
    if not empty_pos:
        return grid

    row, col = empty_pos
    possible_values = find_possible_values(grid, empty_pos)

    for value in possible_values:
        grid[row][col] = value
        solution = solve(grid)
        if solution:
            return solution
        grid[row][col] = '.'

    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    for i in range(9):
        if len(set(solution[i])) != 9:
            return False
        if len(set(get_col(solution, (i, 0)))) != 9:
            return False

    for i in range(3):
        for j in range(3):
            block = get_block(solution, (i * 3, j * 3))
            if len(set(block)) != 9:
                return False

    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    grid = [['.' for _ in range(9)] for _ in range(9)]
    solution = solve(grid)
    if not solution:
        raise ValueError("Could not generate a valid solution.")

    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)

    for r, c in positions[:81 - N]:
        grid[r][c] = '.'

    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)

