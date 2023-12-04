chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request === 'extractHtml') {
    const commentsContainer = document.querySelector('ytd-comments#comments #contents');
    const commentSection = commentsContainer.outerHTML;

    sendResponse({html: commentSection});
  }
});
