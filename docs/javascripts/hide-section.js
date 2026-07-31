// URL クエリパラメータ ?hide=env が指定された場合、
// POC 環境セクション(id="poc-env")を非表示にし、その設定を
// このブラウザに保存する(以後、パラメータなしでアクセスしても非表示のまま)。
// 再表示したい場合は ?hide=off でリセットできる。
// 例:
//   非表示にする: https://example.com/?hide=env
//   再表示する:   https://example.com/?hide=off
(function () {
  var STORAGE_KEY = "hidePocEnv";

  document.addEventListener("DOMContentLoaded", function () {
    var params = new URLSearchParams(window.location.search);
    var hideParam = params.get("hide");

    if (hideParam === "env") {
      localStorage.setItem(STORAGE_KEY, "1");
    } else if (hideParam === "off") {
      localStorage.removeItem(STORAGE_KEY);
    }

    if (localStorage.getItem(STORAGE_KEY) === "1") {
      var el = document.getElementById("poc-env");
      if (el) {
        el.style.display = "none";
      }
    }
  });
})();
