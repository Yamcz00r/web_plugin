<script lang="ts" context="module">
    import {extractHtml} from "./dataExtractor";
    import {data} from "../store"

    const regexUser = /<a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-view-model"[^>]*>[\s\S]*?<\/a>/g;
    const regexComment = /<span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap" dir="auto"[^>]*>[\s\S]*?<\/span>/g;

    export async function handleExtractHtml() {
        const comments = await extractHtml();
        if (comments) {
            let separatedComments = comments.split('<ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">');
            let commentsList = {};
            separatedComments.forEach((comment) => {
                const user = comment.match(regexUser);
                const commentElement = comment.match(regexComment);
                commentsList[Object.keys(commentsList).length] = [user, commentElement];
            })
            data.set(JSON.stringify(commentsList));
            console.log(separatedComments, commentsList)
        }
    }
</script>
