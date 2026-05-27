function sendMessage(event){

  event.preventDefault();

  alert("Thank you! Your message has been sent successfully.");

}

function scrollToProjects(){

  document.getElementById("projects").scrollIntoView({
    behavior:"smooth"
  });

}