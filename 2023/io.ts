import * as fs from "fs";
import { trim } from "./strings";

export const readAsStrings = async (path: string): Promise<string[]> => {
  const content = await fs.readFileSync(path, "utf8");
  return content.split("\n").map(trim);
};

export const workingDirectory = (): string => {
  return __dirname;
};
