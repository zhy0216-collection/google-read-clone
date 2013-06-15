
$(function () {

//router
    $.router.add("/feedsite/:feedsiteid", function(data) {
    
        active(data.feedsiteid);
        $.get("/api/feedsite/"+data.feedsiteid).done(function (tdata) {
            var $rc   = $('#reader-content');
            $rc.unbind("scroll");
            $rc.scrollTop(0);
            $rc.html(tdata);
            $rc.scroll(read_content_scroll());
        });
    });
    
    $.router.add("/folder/:folderid", function(data) {
        $.get("/folder/"+data.folderid).done(function (tdata) {
            $("#reader-content").html(tdata);
        });
    });
    

    
    $(document).on("click",".keep-link",function(e){
        // e.stopPropagation();
        e.preventDefault();
        window.open($(this).attr("href"));
    });

    $(document).on("click","[feedid]",function(){
        var $this   = $(this);
        var $rc     = $('#reader-content');
        $this.addClass("reading-item-active");
        if($this.hasClass("unread-item")){
          $this.removeClass("unread-item");
          //reduce feedsite count..
        }
        console.log("$this.offset().top");
        console.log($this.offset().top);
        $rc.scrollTop($rc.scrollTop()+$this.offset().top-81);
    });
    
//window.location.href




    var height = $(window).height();
    var max_height = height-100;
    $('#nav-scroll').height(max_height - 30);
    $('#reader-content').height(max_height);
    
    $('#nav-scroll').scroll(function() {
      if ($(this).scrollTop()>0){
        $("#scrollable-sections-top-shadow").css("opacity","1.3");
      }else{
        $("#scrollable-sections-top-shadow").css("opacity","0");
      }
    });
    
    
    $('#reader-content').scroll(read_content_scroll());
    
    
    
    // $(document).on( 'clickoutside', "#nav .popover",function(event) {
      // console.log("outside");
      // $('#subsribe-btn').popover('hide');
    // });
    
    
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

var read_content_scroll = function(cur_item){
    var cur_reading_item = cur_item || null;
    var $read_content = $("#reader-content");
    var _top          = $read_content.offset().top;
    var height        = $read_content.height();
    var half_height   = (_top+height)/2-100;
    
    return function(){
      var on_top        = false;
      var $item         = $(".sub-item-show");
      if (cur_reading_item==null){
          cur_reading_item = $item.first();
          on_top = true;
      }
      
      console.log("half_height:");
      console.log(half_height);
      for(var i=0,max=$item.length; i < max; i++){
          if(on_top){
            break;
          }
          var t_top     = $item.offset().top; 
          var bottom  = t_top + $item.height();
          if(half_height >= t_top && half_height < bottom){
            if(cur_reading_item != null){
              cur_reading_item.removeClass("reading-item-active");
            }
            cur_reading_item = $item.first();
            break;
          }
          $item = $item.next()
      }
      cur_reading_item.addClass("reading-item-active");
      cur_reading_item.removeClass("unread-item");
    }
}


function go(href){
    if (window.location.pathname == href){
      return ;
    }
    $.router.go(href);
}

var active = (function(){
  var current_active = "home";
  return function(nodeid){
      $('#'+current_active).removeClass('active');
      current_active = nodeid;
      $('#'+nodeid).addClass('active');
  }
})()

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


var subBtnToggle = (function(){
  var subBtnShowPopover = false;
  return function (node){
      if(!subBtnShowPopover){
          subBtnShowPopover = true;
          node.popover('show');
          $('.popover').css('left','44px');
      }else{
          subBtnShowPopover = false;
          node.popover('destroy');
      }
  }
})();

function addURL(){
    console.log('addurl');
    
    //do not consider animation first
    // do not consider friendly UI
    // do it directly
    var feed_url = $("#nav .popover #input-url").val();
    $.post("/api/feedsite/", {
        feed_url : feed_url
    })
    .done(function (data) {
        if (data.rcode == 200) {
            console.log("done")
        }
    });
    
    
    
    
    
    $('#subsribe-btn').click();
}

function notice(content){
    $('#notify-message').html(content);
    $('#notify-message').fadeIn('slow');
}

function closeNotice(){
    $('#notify-message').fadeOut('slow');
}






