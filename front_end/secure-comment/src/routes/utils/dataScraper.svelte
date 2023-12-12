<script lang="ts" context="module">
    import {extractHtml} from "./dataExtractor";
    import {data} from "../store"

    export async function handleExtractHtml() {
        const comments = await extractHtml();
        if (comments) {
            data.set(comments)
            let separatedComments = JSON.stringify(comments).split('<ytd-comment-thread-renderer class=\\"style-scope ytd-item-section-renderer\\">');
            // let commentsList = {};
            // separatedComments.forEach((comment) => {
            //     const userName = comment
            // })
            console.log(separatedComments)
        }
    }

</script>
