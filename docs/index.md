# Ivanti Neurons Platform ガイド

Ivanti Neurons Platform の導入・設定・POC 実施手順をまとめたガイドサイトです。

!!! note "本サイトについて"
    本ガイドは Ivanti 公式ドキュメント([help.ivanti.com](https://help.ivanti.com/ht/help/ja_JP/CLOUD/vNow/what's-new.htm))をもとに、
    POC・導入支援の観点で再構成したものです。最新の正式情報は必ず公式ドキュメントを参照してください。

## コンテンツ

- [エージェントのインストール](neurons/agent-install.md) — Neurons Agent の展開方式の選択からインストール、登録確認まで
- [パッチ管理](neurons/patch-management.md) — パッチ設定の作成からエージェント ポリシーへの反映、脆弱性・Patch Intelligence の確認、パッチ配布、レポート作成まで
- [リモート コントロール](neurons/remote-control.md) — エージェント ポリシーでの機能有効化からセッション開始、チャット・ファイル転送・リモート実行まで
- [アプリの配布](neurons/app-distribution.md) — アプリ カタログへの登録からパッケージ アクションの設定、対象デバイスへの配布、配布ステータスの確認まで
- [Edge Intelligence](neurons/edge-intelligence.md) — マップでのデバイス位置確認から、デバイス ダッシュボードでの CPU/メモリ確認、CPU 使用率の履歴による時系列推移の確認まで
- [ボット](neurons/bots.md) — テンプレートからのボット作成からトリガ設定でのカスタム アクション有効化、デバイス ビューからの実行、結果確認まで
- [エージェントのアンインストール](neurons/agent-uninstall.md) — コンソールからのアンインストールと OS 別の手動アンインストール、エージェント エンドポイントの削除まで

---

## POC 環境

共用のPOC環境をご用意しています。ネットワーク要件の調整や検証マシンの準備が難しい場合は、仮想マシンのエンドポイントを利用いただけます。

!!! success "各種要件はスキップ可能"
    下記に記載のエンドポイントを利用して POC を実施する場合は、[前提条件]タブにある各種要件はスキップしてください。

| 項目 | 内容 |
| --- | --- |
| Neurons コンソール URL | [https://meriken.ivanticloud.com](https://meriken.ivanticloud.com) |
