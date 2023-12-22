<script lang="ts" context="module">
    import {extractHtml} from "./dataExtractor";
    import {data} from "../store"

    type Commeent = {
        id: number,
        userName: string,
        comment: string
    }
    const regexUser = /<a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-view-model"[^>]*>[\s\S]*?<\/a>/g;
    const regexComment = /<span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap" dir="auto"[^>]*>[\s\S]*?<\/span>/g;

    export async function handleExtractHtml() {
        const comments = await extractHtml();
        if (comments) {
            let separatedComments: string[] = (comments as string).split('<ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">');
            let commentsList: Commeent[] = [];
            separatedComments.forEach((comment) => {
                const id: number = commentsList.length
                const user: RegExpMatchArray | null = comment.match(regexUser)
                const commentElement: RegExpMatchArray | null = comment.match(regexComment);
                if (user && commentElement) {
                    commentsList.push({id: id, userName: user[0], comment: commentElement[0]});
                }
            })
        }
    }
</script>
