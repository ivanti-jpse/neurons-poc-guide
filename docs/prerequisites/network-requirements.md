# ネットワーク要件

Ivanti Neurons Platform / Neurons Agent は、テナントの「ランドスケープ」ごとに定義された社外 URL・IP アドレス・ポートと通信します。
本ページでは、日本を拠点とするテナント向けのランドスケープ **TKU** を対象に、POC 環境で最低限ファイアウォール側の許可設定が必要な項目に絞って解説します。
社内 LAN 上で完結する通信 (ローカル トラフィック) は対象外です。

!!! success "アウトバウンド通信のみ"
    本ページに記載する通信は、すべてエージェント / エンドポイントから Neurons プラットフォームへの **アウトバウンド通信のみ** です。外部からエンドポイントへのインバウンド通信は発生しないため、ファイアウォールでインバウンド ポートを開放する必要はありません。

!!! info "参照元"
    本ページは以下の Ivanti 公式ドキュメントに基づいています。最新情報は必ず参照元を確認してください。

    - [必須の URL、IP アドレス、ポート](https://help.ivanti.com/ht/help/ja_JP/CLOUD/vNow/platform-allowlist.htm)
    - [Content URL Exception List for EPM Ivanti Endpoint Management and Ivanti Neurons UEM](https://hub.ivanti.com/s/article/Content-URL-exception-list-for-EPM-Ivanti-Endpoint-Management?language=en_US)
---

## TKU ランドスケープの通信要件(ファイアウォール許可が必要なもの)

すべての送信トラフィックは基本的に **ポート 443**、エージェント⇔Neurons 間のリアルタイム通信は **ポート 8883 (MQTT)** 、証明書失効リストのアクセスに **ポート 80** を使用します。
社内ネットワーク内で完結する通信(検出エンジン・配布エンジンの SMB/NETBIOS 通信、エージェント間のピア ダウンロードなど)は本ページでは省略しています。

### 登録・基幹通信(全ランドスケープ共通)

| 用途 | URL | IP アドレス | ポート |
| --- | --- | --- | --- |
| エージェント登録・同期 | agentreg.ivanticloud.com<br>agentsync.ivanticloud.com<br>download.ivanticloud.com | 動的 IP | 443 (TCP) |
| エッジ ロケーション | edgelocation.ivanticloud.com | 20.77.156.110 | 443 (TCP) |

!!! warning "証明書失効リスト (CRL) へのアクセスも必須"
    上記に加え、CRL 用 URL(`crl3.digicert.com` / `crl4.digicert.com` / `c.pki.goog` など)にアクセスできないと、エージェントの登録・インストール自体が失敗します。詳細は[参照元](https://help.ivanti.com/ht/help/ja_JP/CLOUD/vNow/platform-allowlist.htm#Certific)の「証明書失効リスト」セクションを確認してください。

### TKU ランドスケープ固有

| 機能 | URL | IP アドレス | ポート |
| --- | --- | --- | --- |
| 基幹 Neurons 通信 | tkuprd-sfc.ivanticloud.com | 動的 | 443 (TCP) |
| エージェント通信 / Edge Intelligence リアルタイム エンジン | tku-prd.mqtt.ivanticloud.com<br>ws-mqtt-tku-prd.ivanticloud.com | 4.189.25.254(動的) | 8883 (TCP、推奨)<br>443 (TCP、WebSocket代替) |
| App Control エンジン | https://saappctrltku.blob.core.windows.net/ | 動的 | 443 (TCP) |
| リモート コントロール(エンドポイント側) | tkuprd-rc.ivanticloud.com | 4.241.23.131 | 44345–44348 (TCP) |
| リモート コントロール(アナリスト側) | ― | ― | 453444–45347 (TCP) |
| 配布エンジン(ステータス) | tkuprd-adpstat.ivanticloud.com | 動的 | 443 (TCP) |
| パッチ エンジン - ベンダ | 各ベンダの配布サイト(vendor list は forums.ivanti.com を参照) | ― | 443 / 80 (TCP、アウトバウンドのみ) |
| パッチ エンジン - サイドロード | Sapatchtenantfiles7d3d2f.blob.core.windows.net | 動的 | 443 (TCP、アウトバウンドのみ) |
| UI ライブ更新(SignalR) | agent-management-signalr-notifications-tku-prd.service.signalr.net | ― | 443 (TCP) |
| App Distribution クラウド ストレージ | https://satkuprddefaul0x08888888.blob.core.windows.net/<br>https://satkuprdautoma0x08888888.blob.core.windows.net/(プラットフォーム自動化用)<br>https://saappdisttku.blob.core.windows.net/ | 動的(Azure Blob) | 443 (TCP) |

### コンテンツ・更新のダウンロード(全ランドスケープ共通)

| 用途 | URL | ポート |
| --- | --- | --- |
| .NET / C++ ランタイム更新 | download.visualstudio.microsoft.com | 443 (TCP) |
| テレメトリ | dc.services.visualstudio.com<br>westeurope-2.in.applicationinsights.azure.com | 443 (TCP) |
| Windows Update 経由のパッチ | download.windowsupdate.com<br>download.microsoft.com | 443 (TCP) |
| Ivanti パッチデータ | content.ivanti.com | 443 (TCP) |
| Patch コンテンツ配信 CDN | CloudFront の IP アドレス範囲(AWS 公開情報を参照) | 443 (TCP) |

---

## ホワイトリスト(パッチ配信元ベンダー URL)

パッチ管理でエージェントがピア/プリファード サーバーを経由せず、ベンダーのダウンロード サイトから直接パッチを取得する構成の場合、各ベンダーの配布 URL もファイアウォールで個別に許可する必要があります。ベンダー URL は数が多く、IP アドレスも動的なため、以下の KB 記事の **Related Files** に用意されている CSV ファイルをダウンロードし、そこに記載された URL 一覧をホワイトリスト登録してください。

1. [Content URL Exception List for EPM Ivanti Endpoint Management and Ivanti Neurons UEM](https://hub.ivanti.com/s/article/Content-URL-exception-list-for-EPM-Ivanti-Endpoint-Management?language=en_US)にアクセスします
2. ページ最下部の **Related Files** セクションにある `UrlData-<更新日>` という名前の CSV ファイルをダウンロードします
3. CSV に記載された URL(`URLData` 列)をファイアウォール / プロキシの許可リストに追加します
4. ベンダーによっては CDN を利用しているため、利用地域によって追加のドメイン許可が必要になる場合があります

!!! note "CSV は定期更新される"
    このファイルはカタログへの新製品追加にあわせて定期的に更新されます。POC 開始前に最新版を取得してください。個別 URL を全て登録する代わりに、`*.domain.com` のようにドメイン単位で許可する方法もあります。

---

## 設定後の確認

- 対象エンドポイントから、上表の TKU 固有 URL(特に `tkuprd-sfc.ivanticloud.com` と `tku-prd.mqtt.ivanticloud.com`)への疎通(ポート 443 / 8883)が確立できることを確認します
- [エージェントのインストール](../neurons/agent-install.md)の手順に沿ってエージェントを登録し、Neurons コンソールの **[エージェント] > [エージェント管理]** でデバイスの **[ステータス]** が **[アクティブ]** になることを確認します
