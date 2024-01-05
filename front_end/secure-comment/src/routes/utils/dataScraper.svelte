<script lang="ts" context="module">
    import {extractHtml} from "./dataExtractor";
    import {data} from "../store"

    type Comment = {
        id: number,
        userName: string,
        comment: string
    }
    const regexUser = /<a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-view-model"[^>]*>[\s\S]*?<\/a>/g;
    const regexComment = /<span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap" dir="auto"[^>]*>[\s\S]*?<\/span>/g;

    async function handleExtractHtml() {
        const comments = await extractHtml();
        if (comments) {
            let separatedComments: string[] = (comments as string).split('<ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">');
            let commentsList: Comment[] = [];

            separatedComments.forEach((comment) => {
                const dirtyUser: RegExpMatchArray | null = comment.match(regexUser)
                const dirtyCommentElement: RegExpMatchArray | null = comment.match(regexComment)
                const id: number = commentsList.length
                const user: RegExpMatchArray | null = JSON.stringify(dirtyUser).match(/@([^<\\]+)/)
                const commentElement: RegExpMatchArray | null = JSON.stringify(dirtyCommentElement).match(/>[\s\S]*?</)
                if (user && commentElement) {
                    commentsList.push({id: id, userName: user[0], comment: commentElement[0]});
                }
            })
            return commentsList;
        }
        return undefined;
    }

    export async function commentCheck() {
        const commentArray: Comment[] | undefined = await handleExtractHtml()
        data.set(JSON.stringify(commentArray));
        console.log(commentArray);
        const response = await fetch('', {
            method: 'POST',
            body: JSON.stringify({

            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }
</script>
