﻿var current_active = "home";


$(function () {
    var height = $(window).height();
    var max_height = height-100;
    $('#nav-scroll').height(max_height - 30);
    $('#reader-content').height(max_height);
    
    
    $('.li1>a .unfold').click(function(e){
        //killevent(e);
        var target = $(e.target);
        li1fold(target);
        console.log("li1 unfold:"+target);
        return false;
    });
    
    $( '.li1>a .fold').click(function(e){
        //killevent(e);
        var target = $(e.target);
        li1unfold(target);
        console.log("li1 fold:"+target);
        return false;
    });
    
    
    $('.li2 .unfold').click(function(e){
        //killevent(e);
        var target = $(e.target);
        li2fold(target);
        console.log("li2 unfold:"+target);
        return false;
    });
    
    $('.li2 .fold').click(function(e){
        //killevent(e);
        var target = $(e.target);
        li2unfold(target);
        console.log("li2 fold:"+target);
        return false;
    });
    
    /*
    $('.unfold').click(function(e){
        var target = $(e.target);
        console.log(target);
        console.log(target.parent());
        target.parent().parent().hide('slow');
        target.parent().show();
    });
    */
    
});

function active(nodeid){
    $('#'+current_active).removeClass('active');
    current_active = nodeid;
    $('#'+nodeid).addClass('active');
}

function li1fold(node){
    node.removeClass('unfold');
    node.removeClass('icon-caret-down');
    node.addClass('fold');
    node.addClass('icon-caret-right');
    node.parent().next().hide();
    node.unbind();
    node.click(function(e){
        killevent(e);
        event.stopPropagation();
        var target = $(e.target);
        li1unfold(node);
    });
    
}

function li1unfold(node){
    node.removeClass('fold');
    node.removeClass('icon-caret-right');
    node.addClass('unfold');
    node.addClass('icon-caret-down');
    node.parent().next().show();
    node.unbind();
    node.click(function(e){
        killevent(e);
        var target = $(e.target);
        li1fold(node);
    });
}

function li2fold(node){
    node.removeClass('unfold');
    node.removeClass('icon-caret-down');
    node.next().removeClass('icon-folder-open');
    node.addClass('fold');
    node.addClass('icon-caret-right');
    node.next().addClass('icon-folder-close');
    
    node.parent().next().hide();
    node.unbind();
    node.click(function(e){
        killevent(e);
        
        event.stopPropagation();
        var target = $(e.target);
        li2unfold(node);
    });
    
}

function li2unfold(node){
    node.removeClass('fold');
    node.removeClass('icon-caret-right');
    node.next().removeClass('icon-folder-close');
    node.addClass('fold');
    node.addClass('icon-caret-down');
    node.next().addClass('icon-folder-open');
    
    node.parent().next().show();
    node.unbind();
    node.click(function(e){
        killevent(e);
        event.stopPropagation();
        var target = $(e.target);
        li2fold(node);
    });
    
}

function killevent(e){
    e.stopPropagation();
    e.preventDefault();
}

var subBtnShowPopover = false;
function subBtnToggle(node){
    if(!subBtnShowPopover){
        subBtnShowPopover = true;
        node.popover('show');
        $('.popover').css('left','44px');
    }else{
        subBtnShowPopover = false;
        node.popover('destroy');
    }
    
}

function addURL(){
    console.log('addurl');
    $('#subsribe-btn').click();
}

function notice(content){
    $('#notify-message').html(content);
    $('#notify-message').fadeIn('slow');
}

function closeNotice(){
    $('#notify-message').fadeOut('slow');
}





