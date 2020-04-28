if(typeof(EventSource) !== "undefined") {
  var source = new EventSource("contract/inbox-notification");
  source.onmessage = function(event) {
      inbox = document.getElementById("inbox-link");
      if (event.data != "0"){
        inbox.innerHTML = "Inbox + " + event.data;
      } else {
        inbox.innerHTML = "Inbox";
      }
  };
}
