<script lang="ts">
    import { extractHtml } from './utils/dataExtractor';

    let x:string|unknown = 'protected';

    async function handleExtractHtml() {
        x = await extractHtml();
        console.log(x)
    }

</script>

<button on:click={()=>{handleExtractHtml()}} type="button" class="btn variant-filled">Button</button>
<h4 class="h4">{x}</h4>
