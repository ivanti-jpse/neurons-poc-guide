// URL クエリパラメータ ?hide=env が指定されている場合、
// POC 環境セクション(id="poc-env")を非表示にする。
// 例: https://example.com/?hide=env
document.addEventListener("DOMContentLoaded", function () {
  var params = new URLSearchParams(window.location.search);
  if (params.get("hide") === "env") {
    var el = document.getElementById("poc-env");
    if (el) {
      el.style.display = "none";
    }
  }
});
