<script lang="ts">
    import {superForm} from "sveltekit-superforms/client";
    import type {PageData} from "./$types";
    import SuperDebug from "sveltekit-superforms/client/SuperDebug.svelte";

    export let data: PageData;
    const {form} = superForm(data.form)
</script>

<SuperDebug data={$form}/>

<div class="w-full flex justify-center bg-opacity-0 mt-4 md:mt-8 lg:mt-12 xl:mt-16">
    <form method="POST" class="w-1/2 md:w-1/3 lg:w-1/4 flex flex-col p-4 self-center">
        <h2 class="h2 self-center"> Sign In </h2>
        <label for="email" class="label py-3 justify-self-center"> Email </label>
        <input class="input" id="email" name="email" type="email" placeholder="john@example.com"
               autocomplete="email" bind:value={$form.email}/>
        <label for="password" class="label py-3 justify-self-center"> Password </label>
        <input class="input" id="password" name="password" type="password" placeholder="password"
               bind:value={$form.password}/>
        <button type="submit" class="btn variant-filled mt-8">Sign In</button>
    </form>
</div>
