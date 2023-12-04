export async function extractHtml() {
  return new Promise((resolve) => {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        if (tabs[0].id)
      chrome.tabs.sendMessage(tabs[0].id, {action: 'extractHtml'}, (response) => {
        resolve(response.html);
      });
    });
  })
}
