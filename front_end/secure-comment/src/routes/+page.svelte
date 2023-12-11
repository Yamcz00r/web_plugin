<script lang="ts">
    import {handleExtractHtml} from './utils/dataScraper.svelte';
    import {data} from './store.js'
</script>

<button on:click={()=>{handleExtractHtml()}} type="button" class="btn variant-filled">Button</button>
<h4 class="h4">{ $data }</h4>
