<script lang="ts">
    import {commentCheck} from './utils/dataScraper.svelte';
    import {data} from './store.js'
</script>

<button on:click={()=>{commentCheck()}} type="button" class="btn variant-filled">Button</button>
<h4 class="h4">{ $data }</h4>
