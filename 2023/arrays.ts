export type Point = [x: number, y: number];

export const getNeighbours = (point: Point): Point[] => {
  const [x, y] = point;
  // prettier-ignore
  const possibleNeighbours = [
        [x - 1, y - 1], [x, y - 1], [x + 1, y - 1],
        [x - 1, y],   /* The point */, [x + 1, y],
        [x - 1, y + 1], [x, y + 1], [x + 1, y + 1],
    ] as Point[];

  return possibleNeighbours.filter((p) => p.every((n) => n >= 0));
};
