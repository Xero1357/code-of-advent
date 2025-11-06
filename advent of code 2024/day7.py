from itertools import product
import os

def read_input(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read()
        lines = data.split('\n')
        equations = []
        for line in lines:
            if line.strip():
                try:
                    test_value, nums = line.split(': ')
                    test_value = int(test_value)
                    nums = [int(x) for x in nums.split()]
                    equations.append((test_value, nums))
                except ValueError:
                    print(f"Skipping invalid line: {line}")
                    continue
        return equations
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def can_produce_value(nums, target, operators):
    if not nums:
        return False
    n = len(nums)
    if n == 1:
        return nums[0] == target
    memo = {}
    def evaluate(index, current_value):
        if index == len(nums):
            return current_value == target
        state = (index, current_value)
        if state in memo:
            return memo[state]
        result = False
        next_num = nums[index]
        for op in operators:
            if op == '+':
                result |= evaluate(index + 1, current_value + next_num)
            elif op == '*':
                result |= evaluate(index + 1, current_value * next_num)
            elif op == '||':
                concat_value = int(str(current_value) + str(next_num))
                result |= evaluate(index + 1, concat_value)
            if result:
                break
        memo[state] = result
        return result
    return evaluate(1, nums[0])

def solve_part(equations, operators):
    return sum(test_value for test_value, nums in equations if can_produce_value(nums, test_value, operators))

def main():
    file_path = "day7.txt"
    if not os.path.isabs(file_path):
        file_path = os.path.join(os.getcwd(), file_path)
    equations = read_input(file_path)
    if not equations:
        print("No valid equations found.")
        return
    total_calibration_part1 = solve_part(equations, ['+', '*'])
    print("Part 1 - Total calibration result:", total_calibration_part1)
    total_calibration_part2 = solve_part(equations, ['+', '*', '||'])
    print("Part 2 - Total calibration result:", total_calibration_part2)

if __name__ == "__main__":
    main()