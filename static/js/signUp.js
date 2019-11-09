"use strict";

$(document).ready(function () {
    $('#registerButton').click(function () {
        let jsonData = JSON.stringify({
            'user': $('#userName').val(),
            'password': $('#password').val(),
            'name': $('#name').val(),
            'surName': $('#surName').val()
        });
        $.ajax({
            url: '/signUp',
            type: 'POST',
            contentType: 'application/json',
            data: jsonData,
            success: function (data) {
                window.location.href = '/';
            },
            error: function () {
                alert('Имя пользователя занято')
            }
        })
    });
    $('footer').css(
        {
            backgroundColor: '#CCFF85'
        }
    );
});