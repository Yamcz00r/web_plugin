<script lang="ts" context="module">
    import {extractHtml} from "./dataExtractor";
    import {data} from "../store"

    const regexUser = "z";
    const regexComment = /<span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap" dir="auto"[^>]*>[\s\S]*?<\/span>/g;
    export async function handleExtractHtml() {
        const comments = await extractHtml();
        if (comments) {
            data.set(comments)
            let separatedComments = comments.split('<ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">');
            let commentsList = {
                test: "test",
            };
            separatedComments.forEach((comment) => {
                commentsList[Object.keys(commentsList).length] = comment.match(regexComment);
            })
            console.log(separatedComments, commentsList)
        }
    }

</script>
