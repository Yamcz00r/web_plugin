<script lang="ts">
    import "../app.pcss";
    import {AppShell} from '@skeletonlabs/skeleton';
    import {token} from "./store";
    import {getCookie} from "./utils/cookieExtractor";


    $: ()=>{
        if (!$token || $token === '') {
            const newToken = getCookie()

            const expirationDays = 7;
            const expirationMillis = expirationDays * 24 * 60 * 60 * 1000; // Convert days to milliseconds
            const expirationDate = new Date(Date.now() + expirationMillis);

            document.cookie = `auth=${newToken}; expires=${expirationDate.toUTCString()}; path=/`;
        } else {
            const expirationDays = 7;
            const expirationMillis = expirationDays * 24 * 60 * 60 * 1000; // Convert days to milliseconds
            const expirationDate = new Date(Date.now() + expirationMillis);

            document.cookie = `auth=${$token}; expires=${expirationDate.toUTCString()}; path=/`;
        }
    }
</script>
<AppShell>
    <slot></slot>
</AppShell>

