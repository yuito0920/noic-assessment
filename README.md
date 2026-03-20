# NOIC 脳アセスメント（Web）

- **本番 URL**: https://yuito0920.github.io/noic-assessment/

## 状態

- **GitHub Pages**: 公開済み（`main` / ルートの `index.html`）
- **Firestore 共有**: `index.html` 内の `FB_CONFIG` に SDK 設定を入れると有効（未設定時はブラウザローカルのみ）

## Firebase を有効にする（初回のみ）

1. [Firebase Console](https://console.firebase.google.com/) でプロジェクトを開く（例: `noic-assessment`）
2. **Firestore** を作成（未作成なら）  
   直リンク: https://console.firebase.google.com/project/noic-assessment/firestore  
   リージョン: **asia-northeast1（東京）**
3. Firestore の **ルール** に、このリポジトリの `firestore.rules` の内容をコピーして公開
4. **プロジェクトの設定** → **マイアプリ** → ウェブ `</>` を追加 → 表示される **firebaseConfig** を JSON で保存（例: `firebase-config.json`）
5. ローカルで注入して push:

```bash
cp firebase-config.example.json firebase-config.json   # 中身をコンソールの値に差し替え
python3 inject_firebase_config.py firebase-config.json index.html
git add index.html && git commit -m "Add Firebase SDK config" && git push
```

数分後に本番 URL で **「☁ クラウド接続」** と表示されれば同期有効です。

## 正本（開発用）

ワークスペースの `NOIC/脳アセスメントシート/NOIC脳アセスメントチェック_cloud.html` を編集し、同内容を `index.html` に反映して push してください。
