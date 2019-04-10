  $(function(){ 
            $("#headerSearch").keyup(function(){
                $.ajax({
                    type: "POST",
                    url: "/ajax_calls/search/",
                    data:{
                        'search_text': $('#headerSearch').val(),
                        'csrfmiddlewaretoken': $('input[name-csrfmiddlewaretoken]').val()
                    },
                    success: searchSuccess,
                    dataType: 'html'


                });

            });
        });

  function searchSuccess(data,textStatus, jqXHR)
  {
    $('#search_result').html(data);
  }