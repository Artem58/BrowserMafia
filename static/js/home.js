"use strict";

$(document).ready(function () {
    $('#loginButton').click(function () {
        let jsonData = JSON.stringify({
            'user': $('#userName').val(),
            'password': $('#password').val()
        });
        $.ajax({
            url: '/verifyUser',
            type: 'POST',
            contentType: 'application/json',
            data: jsonData,
            success: function (jsonResult) {
                let tokenObject = JSON.parse(jsonResult);
                document.cookie = "token=" + tokenObject.token.toString();
                window.location.href = '/chooseGame';
            }
        })
    });
    $('footer').css(
        {
            backgroundColor: '#CCFF85'
        }
    );
});