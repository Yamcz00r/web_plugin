<script lang="ts">
    import { extractHtml } from './utils/dataExtractor';

    let x:string = 'protected';

    async function handleExtractHtml() {
        x = "test";
        x = await extractHtml();
    }

</script>

<button on:click={()=>{handleExtractHtml()}} type="button" class="btn variant-filled">Button</button>
<h4 class="h4">{x}</h4>
