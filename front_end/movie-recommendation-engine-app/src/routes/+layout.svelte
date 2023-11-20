<script lang="ts">
    import '../app.postcss';
    import {AppShell, Drawer} from "@skeletonlabs/skeleton";
    import Header from "./Header.svelte";
    import { initializeStores } from '@skeletonlabs/skeleton';

    initializeStores();
</script>
<Drawer>

</Drawer>

<AppShell>
    <svelte:fragment slot="pageHeader">
        <Header/>
    </svelte:fragment>
    <slot/>
</AppShell>
