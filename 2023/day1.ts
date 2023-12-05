import { readAsStrings, workingDirectory } from "./io";
import * as path from "path";
import { getFirstAndLastDigitsAsNumber, add } from "./numbers";

const main = async () => {
  const workingPath = workingDirectory();

  const filePath = path.join(workingPath, "day1.data");
  const strings = await readAsStrings(filePath);
  const total = strings.map(getFirstAndLastDigitsAsNumber).reduce(add, 0);
  console.log(total);
};

(async function () {
  await main();
})();
