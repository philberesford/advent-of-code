import { getNeighbours } from "./arrays";

describe("getNeighbours", () => {
    test("it to return the top left point", () => {
        const neighbours = getNeighbours([1,1]);

        expect(neighbours).toContainEqual([0,0]);
    });
})
