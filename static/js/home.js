"use strict";

$(document).ready(function () {
    $('#loginButton').click(function () {
        alert("You logged in\nUsername is " + $('#userName').val() + "\nPassword is " + $('#password').val());
    });
    $('footer').css(
        {
            backgroundColor: '#CCFF85'
        }
    );
});