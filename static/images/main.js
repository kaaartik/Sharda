function value(vars) {
  return vars;
}
function sendemail() {
  Email.send({
    Host: "smtp.gmail.com",
    Username: "yash2505bhoite@gmail.com",
    Password: "Hsay@2505",
    To: "akadam3690@gmail.com",
    From: document.getElementById("email").value,
    Subject: "Contact Form Response",
    Body:
      "First Name: " +
      document.getElementById("first_name").value +
      "<br> Last Name: " +
      document.getElementById("last_name").value +
      "<br> Email: " +
      document.getElementById("email").value +
      "<br> Phone Number: " +
      document.getElementById("phone").value +
      "<br> Message: " +
      document.getElementById("message").value,
  }).then((message) => alert("Message Sent Successfully"));
}
var a = 0;
$(window).scroll(function () {
  var oTop = $(".counter").offset().top - window.innerHeight;
  if (a == 0 && $(window).scrollTop() > oTop) {
    $(".counter-value").each(function () {
      var $this = $(this),
        countTo = $this.attr("data-count");
      $({
        countNum: $this.text(),
      }).animate(
        {
          countNum: countTo,
        },

        {
          duration: 4000,
          easing: "swing",
          step: function () {
            $this.text(Math.floor(this.countNum));
          },
          complete: function () {
            $this.text(this.countNum);
            //alert('finished');
          },
        }
      );
    });
    a = 1;
  }
});

// filter section

function change() {
  var modelCbs = document.querySelectorAll(".models input[type='checkbox']");
  var processorCbs = document.querySelectorAll(
    ".processors input[type='checkbox']"
  );
  var filters = {
    models: getClassOfCheckedCheckboxes(modelCbs),
    processors: getClassOfCheckedCheckboxes(processorCbs),
  };

  filterResults(filters);
}

function getClassOfCheckedCheckboxes(checkboxes) {
  var classes = [];

  if (checkboxes && checkboxes.length > 0) {
    for (var i = 0; i < checkboxes.length; i++) {
      var cb = checkboxes[i];

      if (cb.checked) {
        classes.push(cb.getAttribute("rel"));
      }
    }
  }
  return classes;
}

function filterResults(filters) {
  var rElems = document.querySelectorAll(".result .class-mcard");
  var hiddenElems = [];

  if (!rElems || rElems.length <= 0) {
    return;
  }

  for (var i = 0; i < rElems.length; i++) {
    var el = rElems[i];

    if (filters.models.length > 0) {
      var isHidden = true;

      for (var j = 0; j < filters.models.length; j++) {
        var filter = filters.models[j];

        if (el.classList.contains(filter)) {
          isHidden = false;
          break;
        }
      }

      if (isHidden) {
        hiddenElems.push(el);
      }
    }

    if (filters.processors.length > 0) {
      var isHidden = true;

      for (var j = 0; j < filters.processors.length; j++) {
        var filter = filters.processors[j];

        if (el.classList.contains(filter)) {
          isHidden = false;
          break;
        }
      }
      if (isHidden) {
        hiddenElems.push(el);
      }
    }
  }

  for (var i = 0; i < rElems.length; i++) {
    rElems[i].style.display = "block";
  }

  if (hiddenElems.length <= 0) {
    return;
  }

  for (var i = 0; i < hiddenElems.length; i++) {
    hiddenElems[i].style.display = "none";
  }
}

var menu_btn = document.querySelector("#menu-btn");
var sidebar = document.querySelector("#sidebar");
var container = document.querySelector(".my-container");
menu_btn.addEventListener("click", () => {
  sidebar.classList.toggle("active-nav");
  container.classList.toggle("active-cont");
});

function changeImage() {
  var image = document.getElementById("img");
  if (image.src.match("/static/images/right-arrow.svg")) {
    image.src = "/static/images/left-arrow.svg";
    if (window.innerWidth <= 981) {
      // document.querySelector(".my-container button").style.marginLeft="270px";
      document.querySelector(".my-container button").style.transform =
        "translateX(270px)";
    }
    if (window.innerWidth <= 425) {
      // document.querySelector(".my-container button").style.marginLeft="270px";
      document.querySelector(".my-container button").style.transform =
        "translateX(240px)";
    }
  } else {
    image.src = "/static/images/right-arrow.svg";
    // document.querySelector(".my-container button").style.marginLeft="0%";

    document.querySelector(".my-container button").style.transform =
      "translateX(0px)";
  }
}

//Get the button
let mybutton = document.getElementById("btn-back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

function visible() {
  document.getElementById("upload").style.display = "block";
}

function show() {
  document.getElementById("div1").style.display = "block";
}
function hide() {
  document.getElementById("div1").style.display = "none";
}
// $("#contact").on("click", function () {
//   $("#div1").show();
// });

// $("#close").on("click", function () {
//   $("#div1").hide();
// });
