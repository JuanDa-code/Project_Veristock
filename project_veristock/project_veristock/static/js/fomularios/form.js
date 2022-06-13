var vents = {
    items : {
        customer: '',
        date: '',
        totalSale: 0,
        user: '',
        products: [],
    },
    add: function (){ 

    }
};

$(function () {

    // Búsqueda de productos

    var availableTags = [
        "ActionScript",
        "AppleScript",
        "Asp",
        "BASIC",
        "C",
        "C++",
        "Clojure",
        "COBOL",
        "ColdFusion",
        "Erlang",
        "Fortran",
        "Groovy",
        "Haskell",
        "Java",
        "JavaScript",
        "Lisp",
        "Perl",
        "PHP",
        "Python",
        "Ruby",
        "Scala",
        "Scheme"
      ];
      $('input[name="buscar"]').autocomplete({
        source: availableTags
      });
})