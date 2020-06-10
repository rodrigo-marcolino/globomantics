$(function(){
  $(".comment-form").submit(function(event){
    event.preventDefault();
    var form = $(this);

    $.ajax({
      type: form.attr("method"),
      url:  form.attr("action"),
      data: form.serialize() + "&ajax=1"
    }).done(function(data){
      $("#content").val("");
      $(".placeholder-comment").hide();
      $(data).insertAfter(".form-border");
    }).fail(function(data){
      $("#content").val("");
      $(".comment-error").show();
      $(".comment-error").html(data.responseText);
      $(".comment-error").fadeOut(2500);
    });
  });
});
