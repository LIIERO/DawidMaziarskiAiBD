from solve_quadratic_equation_real import solve_quadratic_equation_real, QuadraticEquationArgumentError
import pytest


# Test przypadków w którym funkcja ma zwrócić 2 rozwiązania
testdata_2_sol = [([6, 11, -35], (-7/2, 5/3)),
                  ([6, 11, -35], (5/3, -7/2)),
                  ([2, -4, -2], (1 - 2**0.5, 1 + 2**0.5))]
@pytest.mark.parametrize('args_list, expected_output', testdata_2_sol)
def test_solve_quadratic_equation_real_2_solutions(args_list, expected_output):
    # W przypadku dwóch rozwiązań nie ma znaczenia ich kolejność
    assert sorted(expected_output) == sorted(solve_quadratic_equation_real(*args_list))


# Test przypadków w którym funkcja ma zwrócić 1 rozwiązanie
testdata_1_sol = [([1, -5, 6.25], 2.5),
                  ([2, 4*(3**0.5), 6], -3**0.5)]
@pytest.mark.parametrize('args_list, expected_output', testdata_1_sol)
def test_solve_quadratic_equation_real_1_solution(args_list, expected_output):
    assert expected_output == solve_quadratic_equation_real(*args_list)


# Test przypadków w którym funkcja ma zwrócić None (0 rozwiązań)
testdata_0_sol = [[6, 11, 35]]
@pytest.mark.parametrize('args_list', testdata_0_sol)
def test_solve_quadratic_equation_real_0_solutions(args_list):
    assert solve_quadratic_equation_real(*args_list) is None


# Test przypadku w którym funkcja ma wyrzucić błąd QuadraticEquationArgumentError
def test_solve_quadratic_equation_real_QuadraticEquationArgumentError_handling():
    with pytest.raises(QuadraticEquationArgumentError):
        solve_quadratic_equation_real(1, 2, '3')