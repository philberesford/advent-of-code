import { findFirst, findFirstDigit, reverse } from "./strings";

export const getFirstAndLastDigitsAsNumber = (s: string): number => {
  const firstDigit = findFirstDigit(s);
  const lastDigit = findFirstDigit(reverse(s));
  const combined = firstDigit + lastDigit;
  return parseInt(combined, 10);
};

export const add = (first: number, second: number): number => {
  return first + second;
};

const wordsToNumbersMap = {
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven: 7,
  eight: 8,
  nine: 9,
};

const backwardsWordsToNumbersMap = {
  eno: 1,
  owt: 2,
  eerht: 3,
  ruof: 4,
  evif: 5,
  xis: 6,
  neves: 7,
  thgie: 8,
  enin: 9,
};

const numbersMap = {
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
};

export const stringToNumber = (
  s: string,
  backwards: boolean = false
): number => {
  const allStringsToNumbers = backwards
    ? { ...numbersMap, ...backwardsWordsToNumbersMap }
    : { ...numbersMap, ...wordsToNumbersMap };
  if (Object.keys(allStringsToNumbers).indexOf(s) >= 0) {
    return allStringsToNumbers[s];
  }

  throw Error(`Number ${s} not found in set of numbers to search`);
};
