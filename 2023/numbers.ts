import { findFirstDigit, reverse } from "./strings";
import { cloneMapWithReversedKeys } from "./objects";

export const getFirstAndLastDigitsAsNumber = (s: string): number => {
  const firstDigit = findFirstDigit(s);
  const lastDigit = findFirstDigit(reverse(s));
  const combined = firstDigit + lastDigit;
  return toInt(combined);
};

export const add = (first: number, second: number): number => {
  return first + second;
};

export const multiply = (first: number, second: number): number => {
  return first * second;
};

export const toInt = (s: string): number => {
  return parseInt(s, 10);
};

const wordsToNumericValueMap = {
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

const numbersToValueMap = {
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

export const getDigitsAsString = () => Object.keys(numbersToValueMap);

export const getWordsForDigits = () => Object.keys(wordsToNumericValueMap);

export const stringToNumber = (s: string): number => {
  const stringsToNumericValuesMap = {
    ...numbersToValueMap,
    ...wordsToNumericValueMap,
  };

  if (Object.keys(stringsToNumericValuesMap).indexOf(s) >= 0) {
    return stringsToNumericValuesMap[s];
  }

  throw Error(`Number ${s} not found in set of numbers to search`);
};

export const backwardsStringToNumber = (s: string): number => {
  const backwardsWordsToNumericValueMap = cloneMapWithReversedKeys(wordsToNumericValueMap);

  const stringsToNumericValuesMap = {
    ...numbersToValueMap,
    ...backwardsWordsToNumericValueMap,
  };

  if (Object.keys(stringsToNumericValuesMap).indexOf(s) >= 0) {
    return stringsToNumericValuesMap[s];
  }

  throw Error(`Number ${s} not found in set of numbers to search`);
};
