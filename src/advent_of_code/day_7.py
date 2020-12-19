from typing import List, Set


def convert_single_human_contained_bag_string_to_dict(human_string: str) -> dict:
    words = human_string.strip().split(' ')
    number = int(words[0])
    color = ' '.join(words[1:3])
    return {color: number}


def convert_composite_human_contained_bag_string_to_dict(human_string: str) -> dict:
    contained_bags = {}
    if human_string.strip() != 'no other bags.':
        contained_bag_strings = human_string.split(',')
        for bag_string in contained_bag_strings:
            contained_bags.update(convert_single_human_contained_bag_string_to_dict(bag_string))
    return contained_bags


def convert_human_rule_to_dict(human_rule: str) -> dict:
    this_bag_string, contained_bags_string = human_rule.split('contain')
    color = ' '.join(this_bag_string.strip().split(' ')[:2])
    contained_bags = convert_composite_human_contained_bag_string_to_dict(contained_bags_string)
    return {color: contained_bags}


def convert_human_rules_to_ruleset_dict(human_rules: List[str]) -> dict:
    ruleset = {}
    for rule in human_rules:
        ruleset.update(convert_human_rule_to_dict(rule))
    return ruleset


def get_bags_that_contain_given_bags_directly(bags: Set[str], ruleset: dict) -> Set[str]:
    return {
        color
        for color, contained_bags in ruleset.items()
        if bags.intersection(contained_bags)
    }


def get_bags_that_contain_given_bag(bag: str, ruleset: dict) -> Set[str]:
    bags = {bag, }
    while True:
        original_bags = len(bags)
        new_direct_bags = get_bags_that_contain_given_bags_directly(bags=bags, ruleset=ruleset)
        bags = bags.union(new_direct_bags)
        if len(bags) == original_bags:
            bags.remove(bag)
            return bags


def get_total_bags_within_given_bag(bag: str, ruleset: dict) -> int:
    counts = []
    for child_bag, child_bag_count in ruleset[bag].items():
        bags_in_child_bag = get_total_bags_within_given_bag(bag=child_bag, ruleset=ruleset)
        counts.append(child_bag_count * (1 + bags_in_child_bag))
    return sum(counts)


def main():
    with open('input_files/day_7.txt') as f:
        human_rules = [line.replace('\n', '') for line in f.readlines()]
    ruleset = convert_human_rules_to_ruleset_dict(human_rules=human_rules)
    shiny_gold_bags = get_bags_that_contain_given_bag(bag='shiny gold', ruleset=ruleset)
    print(f'{len(shiny_gold_bags)} will eventually contain a shiny gold bag: {", ".join(shiny_gold_bags)}')
    bags_in_shiny_gold_bags = get_total_bags_within_given_bag(bag='shiny gold', ruleset=ruleset)
    print(f'each shiny gold bag contains {bags_in_shiny_gold_bags} bags')


if __name__ == '__main__':
    main()
