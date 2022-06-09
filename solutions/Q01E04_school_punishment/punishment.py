def do_punishment(first_part: str, second_part: str, nb_lines: int) -> str:
    base_sentence = f'{first_part.strip()} {second_part.strip().rstrip(".")}. '
    return (base_sentence * nb_lines).strip()
