class Vector:
    def __init__(self, components: list[float]):
        self.components = components

    def __getitem__(self, item):
        return self.components[item]

    def __len__(self):
        return len(self.components)

    def __iter__(self):
        return iter(self.components)

    def __str__(self):
        serialized_components = ", ".join(map(str, self.components))
        return f"<{serialized_components}>"


def loads(input_txt: str, begin_seq="<", end_seq=">", sep=", ") -> Vector:
    if not input_txt.startswith("<") or not input_txt.endswith(">"):
        raise ValueError(f"Vectors must start with '{begin_seq}' and end with '{end_seq}'.")

    decoded_body = input_txt[len(begin_seq):-len(end_seq)]
    components = decoded_body.split(sep=sep)

    return Vector(list(map(float, components)))
