from collections import defaultdict


def validate_pages(pages_arr: list[str]) -> tuple[list[list[str]], list[list[str]]]:
    valid_pages = []
    invalid_pages = []
    for page in pages_arr:
        page_nums = page.split(",")
        valid = True
        for x in range(1, len(page_nums)):
            if page_nums[x] not in rule_dict[page_nums[x-1]]:
                invalid_pages.append(page_nums)
                valid = False
                break
        if valid:
            valid_pages.append(page_nums)

    return (valid_pages, invalid_pages)

def correct_page(page_arr: list[str]) -> list[str]:
    correct_page = page_arr.copy()
    x = 1
    while x < len(correct_page):
        y = 0
        while x + y < len(correct_page) and correct_page[x + y] not in rule_dict.get(correct_page[x + y], []):
            y += 1

        if x + y < len(correct_page):
            item = correct_page.pop(x + y)
            correct_page.insert(x + y, item)
        x += 1


    return correct_page 

if __name__ == "__main__":
    input = ""
    with open("example.txt", "r") as f:
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
        print(corrected_pages)
        sum_2 += int(page[len(page) // 2])

    print(sum_1)
    print(sum_2)
