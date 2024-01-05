<script lang="ts">
    import '../app.postcss';
    import {AppShell, Drawer} from "@skeletonlabs/skeleton";
    import Header from "./Header.svelte";
    import {initializeStores} from '@skeletonlabs/skeleton';
    import {page} from "$app/stores";

    initializeStores();
</script>
<Drawer>
    <div class="w-full h-full flex flex-col p-5 justify-between">
        <div class="">
            <h4 class="h4">Menu</h4>
        </div>
        {#if $page.url.pathname === "/"  }
            <div class="">
                <hr/>
                <a href="/auth/signin"  class="btn variant-ghost-surface w-full mt-5">Sign In</a>
            </div>
        {/if}
    </div>
</Drawer>

<AppShell>
    <svelte:fragment slot="pageHeader">
        <Header/>
    </svelte:fragment>
    <slot/>
</AppShell>
