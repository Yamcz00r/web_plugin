import {token} from "./store";

export function load({cookies}) {
    const newToken = cookies.get('auth');
    let oldToken;
    token.subscribe((value) => (oldToken = value));
    if (oldToken)
        cookies.set('auth', oldToken, {
            httpOnly: false,
            secure: false,
            path: '/',
            maxAge: 60 * 60 * 24 * 7
        });
    if (newToken) token.update(() => newToken)
}
