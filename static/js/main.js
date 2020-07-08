$(document).ready(function () {
    $("nav ul li > a:not(:only-child)").click(function (e) {
      $(this).siblings(".nav-dropdown").toggle();
      // Close one dropdown menu when selecting another
      $(".nav-dropdown").not($(this).siblings()).hide();
      e.stopPropagation();
    });
    // Clicking away from dropdown will remove the dropdown class
    $("html").click(function () {
      $(".nav-dropdown").hide();
    });
    // Hide the dropdown menu when the mouse moved away
    $(".nav-dropdown").mouseleave(function(){
      $(this).hide();
    });
    // Clicking the nav-toggle will toggle the active css
    $("#nav-toggle").on("click", function () {
      this.classList.toggle("active");
    });
    // Clicking on the nav-toggle which show and hide the menu
    $("#nav-toggle").click(function () {
      $("nav ul").toggle();
    });
    // Clicking on the add item will append newitem to parent div
    var newitem = '<div class="form-row"><div class="form-group col-10"><input type="text" class="form-control" id="ingredient" name="ingredient" required="" oninvalid="this.setCustomValidity("You must enter an ingredient")" oninput="setCustomValidity("")" /></div><div class="form-group col-2"><a href="javascript:void(0)" class="remove_item" title="Remove item"><i class="fas fa-minus-circle"></i></a></div></div>'
    $('.add_item').click(function() {
      $('#Ingredients').append(newitem);
      });
    // Clicking on the remove item will remove that ingredient  
    $('#Ingredients').on('click', '.remove_item', function(e){
      e.preventDefault();
      $(this).parent().parent('div').remove(); //Remove newitem
    });
    // Clicking on the add item will append newitem to parent div
    var newstep = '<div class="form-row"><div class="form-group col-10"><input type="text" class="form-control" id="step" name="step" required="" oninvalid="this.setCustomValidity("You must enter a cooking step")" oninput="setCustomValidity("")" /></div><div class="form-group col-2"><a href="javascript:void(0)" class="remove_step" title="Remove Step"><i class="fas fa-minus-circle"></i></a></div></div>'
    $('.add_step').click(function() {
      $('#Method').append(newstep);
      });
    // Clicking on the remove item will remove that ingredient  
    $('#Method').on('click', '.remove_step', function(e){
      e.preventDefault();
      $(this).parent().parent('div').remove(); //Remove newitem
    });

  });

  // Validate Form Function
  function validateForm(){
      var username = $('#username').val();
      var password1 = $('#password1').val();
      var password2 = $('#password2').val();
      var firstname = $('#firstname').val();
      var lastname = $('#lastname').val();
      var email = $('#email').val();
      var errors = 0;  
      console.log(errors);
      
      // Validate username
      if (username.length == 0 || username.length <= 4){
        $('#username-message').removeClass().addClass("error-message");
        $('#username').removeClass("success").addClass("error");
        $('#username-message').html("Username cannot be blank & must be greater than four characters.");
        errors++;
      }
      else{
        $('#username-message').removeClass().addClass("success-message").html("Looks good!");
        $('#username').removeClass("error").addClass("success");
      }
      // Validate Password Fields
      if (password1.length == 0 || password1.length <= 6) {
        $('#password-message').removeClass().addClass("error-message").html("Password cannot be blank & must be greater than six characters.");
        $('#password1').removeClass("success").addClass("error");
        errors++;
      }
      else if (password2.length < 1) {
        $('#password-message').removeClass().addClass("error-message").html("Please enter the confirm password");
        $('#password2').removeClass("success").addClass("error");
        errors++;
      }
      else if (password1 != password2) {
        $('#password-message').removeClass().addClass("error-message").html("Passwords do not match");
        $('#password1').removeClass("success").addClass("error");
        $('#password2').removeClass("success").addClass("error");
        errors++;
      }
      else {
        $('#password-message').removeClass().addClass("success-message").html("Looks good!");
        $('#password1').removeClass("error").addClass("success");
        $('#password2').removeClass("error").addClass("success");
      }
      
      // Validate first and last name length
      if (firstname.length < 1 || lastname.length < 1) {
        $('#firstname').removeClass("success").addClass("error");
        $('#lastname').removeClass("success").addClass("error");
        $('#name-message').removeClass().addClass("error-message").html("First or Last name cannot be blank");
        errors++;
      }
      else {
        $('#name-message').removeClass().addClass("success-message");
        $('#name-message').html("Looks good!");
        $('#firstname').removeClass("error").addClass("success");
        $('#lastname').removeClass("error").addClass("success");
      }

      //Validate email address
      if (email.length < 1){
        $('#email').removeClass("success").addClass("error");
        $('#email-message').removeClass().addClass("error-message").html("Email address cannot be blank");
        errors++;
      }
      else if (!validEmail(email)){
        $('#email').removeClass("success").addClass("error");
        $('#email-message').removeClass().addClass("error-message").html("Email address is invalid");
        errors++;
      }
      else {
        $('#email-message').removeClass().addClass("success-message").html("Looks good!");
        $('#email').removeClass("error").addClass("success");
      }
      
      // Validate Email Function
      function validEmail(e){
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e);
      }
      
      // If errors exist return false
      if (errors > 0){
        return false;
      }
  }