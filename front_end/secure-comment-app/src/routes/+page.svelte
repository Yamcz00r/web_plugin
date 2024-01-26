<script lang="ts">
    import {token} from "./store.js";
    import { setToken } from "./auth/auth.svelte"

    console.log("test", $token)

    $:{
        setToken($token);
    }

</script>

<div>

</div>

