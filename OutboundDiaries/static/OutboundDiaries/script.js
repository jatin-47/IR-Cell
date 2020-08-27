document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('aside').style.top = `${document.querySelector('.navbar').offsetHeight}px`;
    document.querySelector('#list').onclick = () => {
        var c = document.querySelector('#list').childNodes[3].style;
        if(c.display == "flex"){  
            c.display = "none";
        }
        else{
            c.display = "flex";
        }
    };
    window.onresize = () => {
        document.querySelector('aside').style.top = `${document.querySelector('.navbar').offsetHeight}px`;
    };
    let open = 1;
    let once = 1;
    document.querySelector('button').onclick = () => {
        document.querySelector('.fa-angle-double-left').style.transform = "rotate(180deg)";
        if(open)
        {
            document.querySelector('aside').style.left = `-${document.querySelector('aside').offsetWidth}px`;
            document.querySelector('.fa-angle-double-left').style.transform = "rotate(180deg)";
            open = 0;
        }
        else{
            document.querySelector('aside').style.left = '0px';
            document.querySelector('.fa-angle-double-left').style.transform = "rotate(0deg)";
            open = 1;
        }
        
    };  
    window.onscroll = () => {
        if (window.scrollY >= 80) {
            document.querySelector('.navbar').style.boxShadow = "0px 10px 10px rgba(0, 0, 0, 0.25)";
            document.querySelector('.navbar').style.background = "#222222";
            if(once){
                document.querySelector('aside').style.left = `-${document.querySelector('aside').offsetWidth}px`;
                document.querySelector('.fa-angle-double-left').style.transform = "rotate(180deg)";
                open = 0;
                once = 0;
            }
        } else {
            document.querySelector('.navbar').style.boxShadow = 'none';
            document.querySelector('.navbar').style.background = "#fff7e7";
        }
    
    };
});

