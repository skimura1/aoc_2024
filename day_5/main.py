from collections import defaultdict
from functools import cmp_to_key


def validate_pages(pages_arr: list[str]) -> tuple[list[list[str]], list[list[str]]]:
    valid_pages = []
    invalid_pages = []
    for page in pages_arr:
        page_nums = page.split(",")
        valid = True
        for x in range(1, len(page_nums)):
            if page_nums[x] not in rule_dict[page_nums[x - 1]]:
                invalid_pages.append(page_nums)
                valid = False
                break
        if valid:
            valid_pages.append(page_nums)

    return (valid_pages, invalid_pages)


def compare_pages(a, b):
    if b in rule_dict[a]:
        return -1
    elif a in rule_dict[b]:
        return 1
    else:
        return 0


def correct_page(page_arr: list[str]) -> list[str]:
    return sorted(page_arr, key=cmp_to_key(compare_pages))


if __name__ == "__main__":
    input = ""
    with open("input.txt", "r") as f:
        input = f.read()

    rules, pages = input.split("\n\n")

    rule_dict = defaultdict(list)

    rules_arr = rules.split()

    for rule in rules_arr:
        rule1, rule2 = rule.split("|")
        rule_dict[rule1].append(rule2)

    pages_arr = pages.split()
    valid_pages, invalid_pages = validate_pages(pages_arr)
    sum_1 = 0
    sum_2 = 0

    for valid_page in valid_pages:
        sum_1 += int(valid_page[len(valid_page) // 2])

    for page in invalid_pages:
        corrected_pages = correct_page(page)
        sum_2 += int(corrected_pages[len(corrected_pages) // 2])

    print(sum_1)
    print(sum_2)
