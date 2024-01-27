import {token} from "./store";
import type {Cookies} from "@sveltejs/kit";
export function load({cookies}) {
    let oldToken;
    token.subscribe((value) => (oldToken = value));
    if (oldToken && oldToken !== '') {
        setCookie(cookies, oldToken);
    } else {
        const newToken = cookies.get('auth');
        if (newToken) {
            token.update(() => newToken)
            setCookie(cookies, newToken);
        }
    }
}

function setCookie (cookies: Cookies, value: string) {
    cookies.set('auth', value, {
        httpOnly: false,
        secure: false,
        path: '/',
        maxAge: 60 * 60 * 24 * 7
    });
}
