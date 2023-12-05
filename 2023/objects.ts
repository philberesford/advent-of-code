import { reverse } from "./strings";

export const cloneMapWithReversedKeys = (obj: {}): {} => {
    const newProps = Object.entries(obj).map((value: [key: string, value: unknown]) => {
        return [reverse(value[0]), value[1]]
    });
    return Object.fromEntries(newProps)
}