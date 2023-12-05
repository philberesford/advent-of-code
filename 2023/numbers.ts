import { findFirstDigit, reverse } from "./strings";

export const getFirstAndLastDigitsAsNumber = (s: string): number => {
    const firstDigit = findFirstDigit(s);
    const lastDigit = findFirstDigit(reverse(s));
    const combined = firstDigit + lastDigit
    return parseInt(combined, 10)
}

export const add = (first: number, second: number): number => {
    return first + second
}
