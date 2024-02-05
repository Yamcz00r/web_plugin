export function getCookie() {
    return new Promise((resolve, reject) => {
        console.log('Getting active tab...');
        chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
            const activeTab = tabs[0];
            if (!activeTab) {
                console.error("No active tab found");
                reject("No active tab found");
                return;
            }

            console.log('Active tab:', activeTab);

            chrome.cookies.get({url: activeTab.url, name: "auth"}, (cookie) => {
                if (chrome.runtime.lastError) {
                    console.error("Error getting cookie:", chrome.runtime.lastError);
                    reject(chrome.runtime.lastError);
                } else {
                    const cookieValue = cookie ? cookie.value : null;
                    console.log('Cookie value:', cookieValue);
                    resolve(cookieValue);
                }
            });
        });
    });
}
