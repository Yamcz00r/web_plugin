export async function extractHtml() {
    return new Promise((resolve) => {
        chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
            let comments = request.comments;
            resolve(comments);
        })
        chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
            if (tabs[0].id) {
                chrome.scripting.executeScript({
                    target: {tabId: tabs[0].id},
                    func: scrapeComments,
                })
            }
        });

    });
}

function scrapeComments() {
    const commentsSection = document.querySelector("ytd-comments#comments div#contents");
    const comments = commentsSection?.outerHTML;
    chrome.runtime.sendMessage({comments});
}
