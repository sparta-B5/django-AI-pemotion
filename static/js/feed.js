// card_feed 모달 
$('#feedMoreModel').on('show.bs.modal', function(event) {          
    target_id = $(event.relatedTarget).data('notifyid');
    // target_auth = $(event.relatedTarget).data('auth');

    // if(target_auth){
       
        $(this).find(".btn_edit").show();
        $(this).find(".btn_deletemodel").show();
        $(this).find(".btn_unfollow").hide();
    // }else{
    //     $(this).find(".btn_edit").hide();
    //     $(this).find(".btn_deletemodel").hide();
    //     $(this).find(".btn_unfollow").show();
    // }
    $(this).attr("data-target",target_id);
    $(this).find(".btn_goFeed").attr("onclick","location.href='/diary/"+target_id+"'");
});

$('#deleteModal').on('show.bs.modal', function(event) {     
    target_id = $(event.relatedTarget).closest(".modal").attr("data-target")
    $(this).find(".btn_delete").attr("onclick","location.href='/diary/delete/"+target_id+"'");
});

$("#staticBackdrop").on("show.bs.modal",function(event){
    target_id = $(event.relatedTarget).closest(".modal").attr("data-target");
    if(target_id){
        // 게시글 수정
        console.log("edit");
        $(this).find(".modal-title").text("게시글 수정");
        let form_url = '/diary/update/'+target_id
        $(this).find("form").attr("action",form_url);
        let form_content = $("#feed_"+target_id).find(".feed_content").text();
        $(this).find("form textarea").val(form_content);
        let form_img = $("#feed_"+target_id).find(".feed-images img").attr("src")
        console.log(form_img)
        $(this).find("form .image_name").text();

    }else{
        console.log("create");
        $(this).find(".modal-title").text("게시글 작성");
        let form_url = '/diary/'
        $(this).find("form").attr("action",form_url);
        $(this).find("form textarea").val("");
        $(this).find("form .image_name").text("");
    }
});