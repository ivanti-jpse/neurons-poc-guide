// 本文中の画像をクリックすると、オーバーレイで拡大表示する。
// もう一度クリック(またはオーバーレイ背景クリック)で閉じる。
// アイコン等の小さい画像(幅48px未満)は対象外。
(function () {
  function initZoom() {
    var overlay = document.createElement("div");
    overlay.className = "image-zoom-overlay";
    var overlayImg = document.createElement("img");
    overlay.appendChild(overlayImg);
    document.body.appendChild(overlay);

    function close() {
      overlay.classList.remove("is-active");
    }

    overlay.addEventListener("click", close);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") close();
    });

    function bindImages() {
      var imgs = document.querySelectorAll(".md-typeset img:not(.image-zoom-bound)");
      imgs.forEach(function (img) {
        img.classList.add("image-zoom-bound");

        function maybeEnable() {
          if (img.naturalWidth >= 48) {
            img.classList.add("image-zoom-target");
            img.addEventListener("click", function (e) {
              e.stopPropagation();
              overlayImg.src = img.currentSrc || img.src;
              overlayImg.alt = img.alt || "";
              overlay.classList.add("is-active");
            });
          }
        }

        if (img.complete) {
          maybeEnable();
        } else {
          img.addEventListener("load", maybeEnable);
        }
      });
    }

    bindImages();

    // MkDocs Material の instant navigation でページ遷移しても再バインドする
    if (window.document$ && typeof window.document$.subscribe === "function") {
      window.document$.subscribe(bindImages);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initZoom);
  } else {
    initZoom();
  }
})();
