export const findFirstDigit = (str: string): string => {
    const digits = "0123456789".split("");
    const strings = str.split("");
    return strings.find(s => digits.indexOf(s) > -1);
}

export const reverse = (s: string): string => {
    return s.split("").reverse().join("");
}