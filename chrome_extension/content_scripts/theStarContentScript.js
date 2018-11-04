function removePunctuation(s) {
    const longHypthenLess = s.replace(/[—]/g, ' ');
    const punctuationLess = longHypthenLess.replace(/[.,\/#!$?%\^&\*;:{}=\-_'"’”“`~()]/g,'');
    return punctuationLess.replace(/\s{2,}/g,' ').toLowerCase();
}

function getArticleContent() {
    res = ''
    for (let i = 0; i < 15; i++) {
        const contentClass = '.trackContent-' + i.toString();
        const contentDiv = $(contentClass);

        if (!contentDiv.length) {
            continue;
        }

        contentDiv.each(function() {
            res += $(this).text() + ' ';
        });

        res = res.trim();   
    }

    return removePunctuation(res.trim());
}

let h1 = $('.article__headline').html();
const headerContent = removePunctuation(h1);
const articleContent = getArticleContent();

chrome.runtime.sendMessage({header: headerContent, article: articleContent}, function(response) {
    console.log(response.farewell);
});  