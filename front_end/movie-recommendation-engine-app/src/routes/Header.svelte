<script lang="ts">
    import {AppBar, getDrawerStore} from "@skeletonlabs/skeleton";
    import type { DrawerSettings } from '@skeletonlabs/skeleton';
    import { page } from '$app/stores';

    const drawerStore = getDrawerStore()

    const drawerSettings: DrawerSettings = {
        id: 'example-3',
        // Provide your property overrides:
        bgDrawer: 'bg-purple-900 text-white',
        bgBackdrop: 'bg-gradient-to-tr from-indigo-500/50 via-purple-500/50 to-pink-500/50',
        width: 'w-[120px] md:w-[240px]',
        padding: 'p-4',
        rounded: 'rounded-xl',
    };

    function openDrawer(): void {
        drawerStore.open(drawerSettings);
    }



</script>


<AppBar gridColumns="grid-cols-3" slotDefault="place-self-center" slotTrail="place-content-end">
    <svelte:fragment slot="lead"><button on:click={() => openDrawer()} type="button" class="btn variant-ghost w-24 lg:w-1/3">Menu</button></svelte:fragment>
    <h1 class="h1">
        <span class="bg-gradient-to-br from-blue-500 to-cyan-300 bg-clip-text text-transparent box-decoration-clone">Title</span>
    </h1>
    <svelte:fragment slot="trail">
        {#if $page.url.pathname === "/"  }
        <a href="/auth/signin" type="button" class="btn variant-ghost w-24 lg:w-1/3">Sign In</a>
        {:else if $page.url.pathname === "/auth/login" || $page.url.pathname === "/auth/signin"}
            <a href="/" type="button" class="btn variant-ghost w-24 lg:w-1/3">Home</a>
        {/if}
    </svelte:fragment>
</AppBar>
