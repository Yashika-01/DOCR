const imagesToPdf = require("images-to-pdf")
await imagesToPdf(["{% url ''%}", "path/to/image2.png"], "path/to/combined.pdf")