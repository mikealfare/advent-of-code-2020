from typing import List, Dict, Tuple, Union


Message = str
HumanRule = str
SubRule = Tuple[int, ...]
Rules = Dict[int, Union[str, List[SubRule]]]
Rule = Rules
Patterns = Dict[int, List[Message]]


def get_rules(human_rules: List[HumanRule]) -> Rules:
    rules = {}
    for rule in human_rules:
        rule_id, rule_value = rule.split(':')
        rule_id = rule_id.zfill(3)
        rule_value = rule_value.strip()
        if '"' in rule_value:
            char = rule_value.replace('"', '')
            rules.update({rule_id: char})
            continue
        zfilled_sub_rules = [
            sub_rule if sub_rule == '|'
            else sub_rule.zfill(3)
            for sub_rule in rule_value.split(' ')
        ]
        rules.update({rule_id: ' '.join(zfilled_sub_rules)})
    return rules


def collapse_rules(rules: Rules) -> Rules:
    if len(rules) == 1:
        return rules
    to_replace = None
    replace_with = None
    while not to_replace or not replace_with:
        for rule, sub_rules in rules:
            if rule != '000':
                to_replace = rule
                replace_with = sub_rules
                break
    for rule, sub_rules in rules:
        sub_rules.replace(to_replace, replace_with)
    del rules[to_replace]
    return collapse_rules(rules)


def convert_to_binary(message: Message) -> int:
    binary = message.replace('a', '0').replace('b', '1')
    return int(binary, 2)


def evaluate(message: Message, rules: Rules, rule: int) -> bool:
    if rules[rule] in 'ab':
        return
    for sub_rule in rules[rule]:
        pass



def main():
    with open('input_files/day_18.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    rules = get_rules(lines[:138])
    messages = lines[140:]


if __name__ == '__main__':
    main()
