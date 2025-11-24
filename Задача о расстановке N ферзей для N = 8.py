def solve_n_queens(n=8):
    """
    Решает задачу о расстановке N ферзей на доске N×N
    Args:
        n: размер доски и количество ферзей
    Returns:
        Список всех возможных расстановок
    """
    def is_safe(board, row, col):
        """
        Проверяет, можно ли безопасно разместить ферзя на позиции (row, col)
        Args:
            board: текущая расстановка ферзей
            row: строка для размещения
            col: столбец для размещения
        """
        # Проверяем все предыдущие строки
        for i in range(row):
            # Проверка по вертикали и диагоналям
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True
    def backtrack(row, current_board):
        """
        Рекурсивная функция для поиска всех расстановок
        Args:
            row: текущая строка для размещения ферзя
            current_board: текущая расстановка (индекс = строка, значение = столбец)
        """
        # Базовый случай: все ферзи размещены
        if row == n:
            # Сохраняем найденное решение
            solutions.append(current_board[:])
            return
        # Пробуем разместить ферзя в каждом столбце текущей строки
        for col in range(n):
            if is_safe(current_board, row, col):
                # Размещаем ферзя
                current_board[row] = col
                # Рекурсивно размещаем остальных ферзей
                backtrack(row + 1, current_board)
                # Backtrack: убираем ферзя для尝试 других вариантов
                current_board[row] = -1
    solutions = []
    # Инициализируем доску: -1 означает, что в строке нет ферзя
    initial_board = [-1] * n
    backtrack(0, initial_board)
    return solutions
# Решаем для N=8
solutions = solve_n_queens(8)
print(f"Найдено {len(solutions)} решений для 8 ферзей")
