import { readAsStrings, workingDirectory } from "./io";
import * as path from "path";

const main = async () => {
  const workingPath = workingDirectory();

  const filePath = path.join(workingPath, "day1.data");
  const strings = await readAsStrings(filePath);
  console.log(strings);
};

(async function () {
  await main();
})();
