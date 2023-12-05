import { readAsStrings, workingDirectory } from "./io";
import * as path from "path";
import {
  getFirstAndLastDigitsAsNumber,
  add,
  stringToNumber,
  getWordsForDigits,
  getDigitsAsString,
  backwardsStringToNumber,
} from "./numbers";
import { findFirst, reverse } from "./strings";

const main = async () => {
  const workingPath = workingDirectory();

  const filePath = path.join(workingPath, "day2.data");
  const strings = await readAsStrings(filePath);
  part1(strings);
};

const part1 = (strings: string[]) => {
  const gameIsPossibleCriteria = (gameResult: GameResult) =>
    isPossible(12, 13, 14, gameResult);
  const gameIdTotaliser = (possible: boolean, gameIndex: number) =>
    possible ? gameIndex + 1 : 0;

  const totalOfGameIds = strings
    .map(stringToGameResult)
    .map(gameIsPossibleCriteria)
    .map(gameIdTotaliser)
    .reduce(add, 0);

  console.log(totalOfGameIds);
};

type Colour = "red" | "blue" | "green";
type SelectionResult = [number, Colour];
type RoundResult = SelectionResult[];
type GameResult = RoundResult[];

const stringToGameResult = (s: string): GameResult => {
  const gameInfo = s.split(":")[1];
  const rounds = gameInfo.split(";");
  const gameResult: GameResult = rounds.map((selections) => {
    const roundResult: RoundResult = selections
      .split(",")
      .map((selection) => selection.trim())
      .map((selection) => {
        const components = selection.split(" ").map((s) => s.trim());
        const selectionResult: SelectionResult = [
          parseInt(components[0], 10),
          components[1] as Colour,
        ];
        return selectionResult;
      });
    return roundResult;
  });

  return gameResult;
};

const isPossible = (
  redCount: number,
  greenCount: number,
  blueCount: number,
  result: GameResult
) => {
  return result.every(
    (round) =>
      ballCount("red", round) <= redCount &&
      ballCount("green", round) <= greenCount &&
      ballCount("blue", round) <= blueCount
  );
};

const ballCount = (colour: Colour, round: RoundResult) => {
  const selection: SelectionResult = round.find(
    (selection) => colour === selection[1]
  );
  return selection ? selection[0] : 0; // If the colour isn't found, then there's no balls of that colour in the Round Result
};

(async function () {
  await main();
})();
