import { readAsStrings, workingDirectory } from "./io";
import * as path from "path";
import { getFirstAndLastDigitsAsNumber, add, stringToNumber } from "./numbers";
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
  const forwardsNumbers = [
    ..."0123456789".split(""), // digits
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];

  const backwardsNumbers = [
    ..."0123456789".split(""), // digits
    "eno",
    "owt",
    "eerht",
    "ruof",
    "evif",
    "xis",
    "neves",
    "thgie",
    "enin",
  ];

  const firstDigits = strings
    .map((s) => findFirst(forwardsNumbers, s))
    .map((s) => stringToNumber(s));
  const secondDigits = strings
    .map((s) => findFirst(backwardsNumbers, reverse(s)))
    .map((s) => stringToNumber(s, true));

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
