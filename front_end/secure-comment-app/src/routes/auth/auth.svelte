<script lang="ts">
    import {parse} from "cookie";
    import {token} from "../store";

    export const setToken = (newToken: any) =>{
        console.log("test2")
        if (newToken) {
            setCookie("auth", newToken, 7);
        } else {
            const cookieToken = getCookie("auth");

            if (cookieToken) {
                token.update(() => cookieToken);
            }
        }
    }

    function setCookie(name: string, value: string, days: number) {
        // const expires = new Date();
        // expires.setDate(expires.getDate() + days);
        // document.cookie = `${name}=${value}; expires=${expires.toUTCString()}; path=/`;
    }

    function getCookie(name: string): string | undefined {
        // try {
        //     const cookies = parse(document.cookie);
        //     return cookies[name];
        // } catch (err) {
        //     token.update(() => '')
        // }

    }
</script>
