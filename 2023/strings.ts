export const findFirstDigit = (s: string): string => {
  const digits = "0123456789".split("");
  return findFirst(digits, s);
};

export const reverse = (s: string): string => {
  return s.split("").reverse().join("");
};

export const findFirst = (lookFor: string[], lookIn: string): string => {
  const positions: [string, number][] = lookFor.map((s) => [s, lookIn.indexOf(s)]);
  let first: [string, number];
  positions
    .filter((tuple) => tuple[1] >= 0) // Only consider tuples where the string was found;
    .forEach((tuple) => {
      if (!first) {
        first = tuple;
      }
      if (tuple[1] < first[1]) {
        first = tuple;
      }
    });
  return first[0];
};
