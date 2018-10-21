var d = function () {
    var uri = document.getElementsByTagName('video')[0].src
    window.open(uri, '', 'width=200,height=100');
}

// for directory structure
var list = document.getElementsByTagName('section');
var counter = 0;
var folder_index = 0;
var videos = {};
var names = [];
var title = document.getElementById('course-title-link').innerHTML;
console.log(`${title}#####`);// to be used by python
for (var i = 0; i < list.length; i++) {
    if (list[i].className.match(/\bmodule\b/)) {
        var header_text = list[i].getElementsByTagName('h2')[0].innerText;
        var ul = list[i].getElementsByClassName('clips');
        var li_list = ul[0].getElementsByClassName('side-menu-clip-title');
        if (li_list.length > 0) {
            console.log(` --- ${header_text} --- `); // to be used by python
            folder_index++;
            for (var y = 0; y < li_list.length; y++) {
                counter += 1;
                var videoname = li_list[y].innerText;
                console.log(`${counter} - ${videoname}%%%${folder_index}`); // to be used by python
                names.push(`${counter} - ${videoname}`);
                // Store the videos's: name, element and Url 
                // future ...
                videos[`${counter} - ${videoname}`] = {
                    'name': videoname,
                    'ele': li_list[y],
                    'url': document.getElementsByTagName('video')[0].src, videoname,
                }
            }
            console.log(' ');
            console.log(' ');
        }
    }
}



/*
for (const [key, value] of Object.entries(videos)) {
    console.log(key, value);
    value['ele'].click();
    setTimeout(function () { }, 7000);
    //window.open(value['url'], '', 'width=200,height=100');
}
*/

