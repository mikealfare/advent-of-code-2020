from typing import Set, Dict
from pathlib import Path


Bag = str
ContainedBags = Dict[Bag, int]
RuleSet = Dict[Bag, ContainedBags]


def get_contained_bag_counts_as_dict(human_string: str) -> ContainedBags:
    contained_bags = {}
    if human_string.strip() != 'no other bags.':
        contained_bag_strings = human_string.split(',')
        for bag_string in contained_bag_strings:
            words = bag_string.strip().split(' ')
            number = int(words[0])
            color = ' '.join(words[1:3])
            contained_bags.update({color: number})
    return contained_bags


def convert_human_rule_to_rule(human_rule: str) -> RuleSet:
    this_bag_string, contained_bags_string = human_rule.split('contain')
    color = ' '.join(this_bag_string.strip().split(' ')[:2])
    contained_bags = get_contained_bag_counts_as_dict(contained_bags_string)
    return {color: contained_bags}


def convert_human_rules_to_ruleset(human_rules: Set[str]) -> RuleSet:
    ruleset = {}
    for rule in human_rules:
        ruleset.update(convert_human_rule_to_rule(rule))
    return ruleset


def get_bags_that_contain_given_bag(bag: Bag, ruleset: RuleSet) -> Set[Bag]:
    bags = {bag, }
    while True:
        original_bags = len(bags)
        new_direct_bags = {
            color
            for color, contained_bags in ruleset.items()
            if bags.intersection(contained_bags)
        }
        bags = bags.union(new_direct_bags)
        if len(bags) == original_bags:
            bags.remove(bag)
            return bags


def get_total_bags_within_given_bag(bag: Bag, ruleset: RuleSet) -> int:
    counts = []
    for child_bag, child_bag_count in ruleset[bag].items():
        bags_in_child_bag = get_total_bags_within_given_bag(bag=child_bag, ruleset=ruleset)
        counts.append(child_bag_count * (1 + bags_in_child_bag))
    return sum(counts)


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_07.txt'):
    with open(file_path) as f:
        human_rules = {line.strip() for line in f.readlines()}
    ruleset = convert_human_rules_to_ruleset(human_rules)
    shiny_gold_bags = get_bags_that_contain_given_bag('shiny gold', ruleset)
    print(f'{len(shiny_gold_bags)} will eventually contain a shiny gold bag')
    bags_in_shiny_gold_bags = get_total_bags_within_given_bag('shiny gold', ruleset)
    print(f'each shiny gold bag contains {bags_in_shiny_gold_bags} bags')


if __name__ == '__main__':
    main()
