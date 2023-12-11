<script lang="ts" context="module">
    import {extractHtml} from "./dataExtractor";
    import {data} from "../store"

    export async function handleExtractHtml() {
        data.set(await extractHtml());
    }

</script>
