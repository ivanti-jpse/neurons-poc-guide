# プラットフォーム要件

Neurons Agent をインストールできる、サポート対象のオペレーティング システムの一覧です。POC 環境の対象デバイスの OS が本一覧に含まれていることを確認してください。
参照元ヘルプは機能ごと(パッチ、リモート コントロールなど)のサポート可否をマトリクス表で示していますが、本ページでは **OS ファミリー別のサポート対象バージョン一覧** として簡略化しています。

!!! info "参照元"
    - [オペレーティング システム互換性マトリクス](https://help.ivanti.com/ht/help/ja_JP/CLOUD/vNow/compatibility.htm)

---

## サポート対象 OS 一覧

### Microsoft Windows

- Windows 10
- Windows 11
- Windows 11 (ARM64)

!!! note
    Windows 10 / 11 は、Microsoft のサポート期間内のリリースのみサポート対象です。詳細は [Microsoft 製品とサービスのライフサイクル情報](https://learn.microsoft.com/en-us/lifecycle/products/?products=windows)を参照してください。

### Microsoft Windows Server

- Windows Server 2012 *(サポート終了。ESU コンテンツの受信には追加サブスクリプションが必要。詳細は Ivanti サポートへ問い合わせ)*
- Windows Server 2012 R2 *(サポート終了。同上)*
- Windows Server 2016
- Windows Server 2019
- Windows Server 2022
- Windows Server 2022 Core Edition
- Windows Server 2025

### Apple macOS

- macOS 12.x
- macOS 13.x
- macOS 14.x
- macOS 15.x
- macOS 26.x

!!! note
    macOS にインストールされた Neurons エージェントは、配布・検出タスクを直接実行できません。配布は配布機能が有効な Windows デバイス経由、検出は Neurons for Discovery 経由で対応します。

### Linux

- Amazon Linux 2023
- Amazon Linux v2
- Oracle Linux v7
- Oracle Linux v8
- Oracle Linux v9
- RHEL v8
- RHEL v9
- RHEL v10
- Ubuntu v20
- Ubuntu v22
- Ubuntu v24.04

!!! note
    上記は参照元マトリクス表のうち **パッチ機能に対応しているディストリビューションのみ** を抜粋したものです。パッチ機能に対応していない Rocky Linux(全バージョン)、SUSE(全バージョン)、Oracle Linux v10 は掲載していません。

---

## 機能ごとの対応可否について

エージェントのインストール可否ではなく、パッチ管理・リモート コントロール・Edge Intelligence などの **機能単位の対応 OS** を確認したい場合は、参照元の互換性マトリクス内の表(OS ファミリーごとに機能列でサポート状況アイコンを表示)を直接参照してください。
