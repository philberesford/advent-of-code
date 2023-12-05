import { readAsStrings, workingDirectory } from "./io";
import * as path from "path";
import {
  getFirstAndLastDigitsAsNumber,
  add,
  stringToNumber,
  getWordsForDigits,
  getDigitsAsString,
  backwardsStringToNumber
} from "./numbers";
import { findFirst, reverse } from "./strings";

const main = async () => {
  const workingPath = workingDirectory();

  const filePath = path.join(workingPath, "day1.data");
  const strings = await readAsStrings(filePath);
  part1(strings);
  part2(strings);
};

const part1 = (strings: string[]) => {
  const total = strings.map(getFirstAndLastDigitsAsNumber).reduce(add, 0);
  console.log(total);
};

const part2 = (strings: string[]) => {
  const numbersAsString = [
    ...getDigitsAsString(),
    ...getWordsForDigits()
  ];

  const firstDigits = strings
    .map(s => findFirst(numbersAsString, s))
    .map(stringToNumber);

  // Now look through the strings backwards - being mindful to look for the reversed words!
  const backwardsNumbersAsString = numbersAsString.map(reverse)
  const secondDigits = strings
    .map(s => findFirst(backwardsNumbersAsString, reverse(s)))
    .map(backwardsStringToNumber);

  const total = firstDigits
    .map((value, index) => {
      return parseInt(`${value}${secondDigits[index]}`, 10);
    })
    .reduce(add, 0);

  console.log(total);
};

(async function () {
  await main();
})();
