<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/WygcAuCcEozahrsNiYhKU9OCl5yh_ztITpu-NnznMYi2Oc9ZKIgyMazgJ3MHYtOJdbtXRymoKLCh2NZvrFtyf3WItFSA2MgsaKuUSf0iU8oRnIyPH_C8iofPItrGh3E7wtKpN1Q4Qc4Q-lcvqPadrwNe0m7Fv6QNx-9l0LQ7F_ZPsj0WylvwmIM-4-F1TkiyJ6Z2zC-2-7YY_TXLHP1jTd1UtUHbwwVCuO9n4OIwBA83TSPuoPX7aB3ygnQmtPBdIrDEh2CIrcBlCL2FZoC7TNcEoi-_YM-uqCEnHa_b_z-V6x5K0JWqrc7juPdwMYAwpho4lNhJJRIy0Mj-rO03_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 108K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-71623">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
دقایقی پیش چندین انفجار سنگین در چابهار سیستان و بلوچستان رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/news_hut/71623" target="_blank">📅 18:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71622">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
ویدیویی از عملیات نجات افسر تسلیحات ملقب به "براوو Bravo"(زیرنویس فارسی)
@News_Hut</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/news_hut/71622" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71621">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctcEcPGIehp7Kx4Je-u6VzKJejDoST3uZswmPdmBM38cC6naCeK-F79SRlM-6vvYYFJGWZPIGSOdIbOzzuMhFIr5ClCQzbi-f74SoSoEgRpJpRltCF4_k3XNiFXyZTSs6Jn5RK2luD0r9QX4-2se78buC9SjfDNoQS-4-cijyxLsHN6DVeUn0VsAiLkWb_ZS2Bq7Hl7BggDG0S1TuCa30RcJKV-st4CWjQTsHpEePgYYov3xDZPN2bkMDTXweNSE5PkXHR0UYmkn-W0sb5c1l0DtM5s7AhoRNP73NdUFB3e94Q7izhvPc7tsFCx5SY-N9WeVH3FeFa4crklNEKTFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو هفته آینده برای سخنرانی در مجمع عمومی سازمان ملل در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/news_hut/71621" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71620">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=d1ZxyzES8ByhpN74Uv4BAmoh0OgVkWXBXmNHYUYf5DlVjJvYWlJDUiLqMcLNuquWz-qD6qDQYCv8h7VpW3tlOXKdUl3HHwitmoew30FsqfAWxI556VWZFu2G4NH3yHMWNVdrJIsQr8d0VNEb26zePxCOAy4AP2Okxni0xpVGKA6TAxQfqq_xXB-Bunrie00pFgqSWMJhj1R-tcPngCQQJaLP0t04s9txn1ycjicxjlcrf3BA_KY5ZHcls7q5H_KyI3GzFQFswDzQyB2erUZXscNnEy9oO-Dmfmml3bSwAhOlRHKYDSrNuLe28YFftg7xeqSzNc694OMlxY0Ie0tXRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=d1ZxyzES8ByhpN74Uv4BAmoh0OgVkWXBXmNHYUYf5DlVjJvYWlJDUiLqMcLNuquWz-qD6qDQYCv8h7VpW3tlOXKdUl3HHwitmoew30FsqfAWxI556VWZFu2G4NH3yHMWNVdrJIsQr8d0VNEb26zePxCOAy4AP2Okxni0xpVGKA6TAxQfqq_xXB-Bunrie00pFgqSWMJhj1R-tcPngCQQJaLP0t04s9txn1ycjicxjlcrf3BA_KY5ZHcls7q5H_KyI3GzFQFswDzQyB2erUZXscNnEy9oO-Dmfmml3bSwAhOlRHKYDSrNuLe28YFftg7xeqSzNc694OMlxY0Ie0tXRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک پهپاد روسی «گران» (Geran) در بخشی از جاده در شهر «پاولوگراد» که مملو از خودروهای غیرنظامیان بود، سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/news_hut/71620" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71619">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=fiZKPsnoeh_oX4delG2EEZnwcnwXIqrp1nvX423vbh6zhhWmLjYz6lgcQeg8SxFelw9JZqME9MDvk9UPe_k_zOxVInCmDwNZKYXCbJYqs2fjdJXnnP2A4B6i4ICGkB2yiH_wD2CZVBSQ48UB8h1v87tvMfjzRuA54TxbTQQvrSIom6HcJ_sDIdunNzrIYy_MPAKOy2V8gtMFn8zQQ9MWDqfAINyUVAbHXdXae--UzurSwTO078iGmDQIv-jvIgmkmNvrfO9okCss5K7iX1YECH7UOhDoGdcObnILOf8ADhEhyVP5dXff28bAP57C2P4QJY-huNEY9cHQ2qGbFljleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=fiZKPsnoeh_oX4delG2EEZnwcnwXIqrp1nvX423vbh6zhhWmLjYz6lgcQeg8SxFelw9JZqME9MDvk9UPe_k_zOxVInCmDwNZKYXCbJYqs2fjdJXnnP2A4B6i4ICGkB2yiH_wD2CZVBSQ48UB8h1v87tvMfjzRuA54TxbTQQvrSIom6HcJ_sDIdunNzrIYy_MPAKOy2V8gtMFn8zQQ9MWDqfAINyUVAbHXdXae--UzurSwTO078iGmDQIv-jvIgmkmNvrfO9okCss5K7iX1YECH7UOhDoGdcObnILOf8ADhEhyVP5dXff28bAP57C2P4QJY-huNEY9cHQ2qGbFljleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگزاری این کنسرت خیابونی مختلط توی کیش باعث شده صدای طرفداران حکومت در بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/news_hut/71619" target="_blank">📅 16:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71618">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=QVNeShKHLR8pdQKUFTw11PWVwtIsYLKWdGUhi-xByGyqeieAm1fh4tGBhIJ_7iCh3CMMhWTx3sLv28dPel22KLtBVxKH9uwooFmO2xcdGmtaY-qA_r3cqdneM_JIVFqWQg106I4yo7R4_7u1f_UbeLdZamHYnWxPInLZAwfERJcJopPeqGNpgeltkhezQIsTtpOcjFIuSpmVUqD29TQpgRFuWChJqVe5D1skplmgHadMCvRfZ3QFA9tkdqHmNfJ6Av0eRfZvusmUdAyrnpnXvSIDp-zSNLG4UjbtaVdqfODebC0kRmoGjFe_h7AUjRaNyGg1Nc9YSJ3UG4w5osf4ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=QVNeShKHLR8pdQKUFTw11PWVwtIsYLKWdGUhi-xByGyqeieAm1fh4tGBhIJ_7iCh3CMMhWTx3sLv28dPel22KLtBVxKH9uwooFmO2xcdGmtaY-qA_r3cqdneM_JIVFqWQg106I4yo7R4_7u1f_UbeLdZamHYnWxPInLZAwfERJcJopPeqGNpgeltkhezQIsTtpOcjFIuSpmVUqD29TQpgRFuWChJqVe5D1skplmgHadMCvRfZ3QFA9tkdqHmNfJ6Av0eRfZvusmUdAyrnpnXvSIDp-zSNLG4UjbtaVdqfODebC0kRmoGjFe_h7AUjRaNyGg1Nc9YSJ3UG4w5osf4ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ و بی‌بی ترسیدن نکنید اقا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/71618" target="_blank">📅 16:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71617">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=mmG8xpD-VOug-25w65dAxtHitzV5iVOWQMVYravxcecCBzERODGXOyxqPP6Tnniaz0y0kwMumYVywI7nLob9F6P3m1GjCtwc4Yl7_TMpN-8xZkeR6LGWNqeNhde6suT3ii5JsemNaxFbsXP24iOVwxq1-w5rF1Bn3-FMt-jhQfCimfenpN7aE7EAp_kPtDBX3laieSw-ZxSnDPNpnwPPpULHc0yPwCoXCr41i2wjG4Fo2_FskLz_T90036hBzN23eG-9GYto67VIf2MZK4DM3DcuvxQoWYNUaidUy-wq1ik0zZM2uvAtGc1ckBRaEfo0lSZKmdtQSUDI3GRrvVEBOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=mmG8xpD-VOug-25w65dAxtHitzV5iVOWQMVYravxcecCBzERODGXOyxqPP6Tnniaz0y0kwMumYVywI7nLob9F6P3m1GjCtwc4Yl7_TMpN-8xZkeR6LGWNqeNhde6suT3ii5JsemNaxFbsXP24iOVwxq1-w5rF1Bn3-FMt-jhQfCimfenpN7aE7EAp_kPtDBX3laieSw-ZxSnDPNpnwPPpULHc0yPwCoXCr41i2wjG4Fo2_FskLz_T90036hBzN23eG-9GYto67VIf2MZK4DM3DcuvxQoWYNUaidUy-wq1ik0zZM2uvAtGc1ckBRaEfo0lSZKmdtQSUDI3GRrvVEBOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سرقت آیفون ۱۷ پرو ، در کسری از ثانیه در کافه ای در اندرزگو تهران
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/71617" target="_blank">📅 15:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71616">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=TnZlxOln6nIz5ukeqhw6-MSHGRas2vYRPMetoZL8Tw5PtXa8e9wg8zpAV_VoLsUYdfXLCrUInpkL63Awzw7lLY9yn7DmzXk5n-zF-Wb1n9fJkItY9pxsrvxutcZaFkxM1dc93cgsTQfAPXDTbFEtgvQTKnQf7QC723IKA3_M2o96FboOks3rlogjiqddLlTFOJPj7stDMhfyg0qUJEe7Ms_I-6ftU2j5EwfHw0lJe_dTIjHcSafUVHrmxJT1AHCW_l_PvJweLwuzjguOU5S6cRyERLagfShYyn7C9R0YAPy_dwisfGwjegCoX2zbg82CXOy8uqsKp3IqAb_0qaQN6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=TnZlxOln6nIz5ukeqhw6-MSHGRas2vYRPMetoZL8Tw5PtXa8e9wg8zpAV_VoLsUYdfXLCrUInpkL63Awzw7lLY9yn7DmzXk5n-zF-Wb1n9fJkItY9pxsrvxutcZaFkxM1dc93cgsTQfAPXDTbFEtgvQTKnQf7QC723IKA3_M2o96FboOks3rlogjiqddLlTFOJPj7stDMhfyg0qUJEe7Ms_I-6ftU2j5EwfHw0lJe_dTIjHcSafUVHrmxJT1AHCW_l_PvJweLwuzjguOU5S6cRyERLagfShYyn7C9R0YAPy_dwisfGwjegCoX2zbg82CXOy8uqsKp3IqAb_0qaQN6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
در ۴۵ روز گذشته، ۹ آتشفشان فوران کرده؛ انگار در جهان، یک تغییر بزرگ در جریانه
!
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/71616" target="_blank">📅 15:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71615">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=vc8aAvw7g8vFR7keZ14nctRzF3M2g00H3Gt-Yaav7MkyKU2ybXNnitdsWEVfCzWDr_EklrQqVJIyYfjNfAeSi9zLGyAWYBXtXVHjPNU6LdMlkPFY37E383FiAKJ_uz_JIB3WK5e2ytjRmeZr04JZ5_XYSn9wgbTMczI7Lh2CX9yfTZq90M3kP_8xUBm9JdV1QGRqcpArzDrGopJFtWkyvubUBrQXstGK6SJXftkSnqpuM70NIJolUL9CzURHGjRtsl9dzXefpKcJ4Ts0PKcYodzK1kwNyXrLPvR4VXFg-o-EMqesJCqXcuLcsuZ5zbriReKXcIcBZPyWrSsF1w0HpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=vc8aAvw7g8vFR7keZ14nctRzF3M2g00H3Gt-Yaav7MkyKU2ybXNnitdsWEVfCzWDr_EklrQqVJIyYfjNfAeSi9zLGyAWYBXtXVHjPNU6LdMlkPFY37E383FiAKJ_uz_JIB3WK5e2ytjRmeZr04JZ5_XYSn9wgbTMczI7Lh2CX9yfTZq90M3kP_8xUBm9JdV1QGRqcpArzDrGopJFtWkyvubUBrQXstGK6SJXftkSnqpuM70NIJolUL9CzURHGjRtsl9dzXefpKcJ4Ts0PKcYodzK1kwNyXrLPvR4VXFg-o-EMqesJCqXcuLcsuZ5zbriReKXcIcBZPyWrSsF1w0HpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
ما امروز از قبل از جنگ هم آماده‌تریم!
تو حوزه مرزبانی، انتظامی و خدماتی آماده‌تریم.
با امنیت مردم شوخی نداریم، ما شرایط‌مون جنگیه، اگه وطن‌فروشی به دعوت دشمن بخواد ناامنی ایجاد بکنه، ما اون رو مثل دشمن می‌بینیم و باهاشون برخوردی رو می‌کنیم که دارن با دشمن برخورد میکنن.
دشمن میخواست چهارشنبه آخر سال 1404، همون مدل دیِ 1404 رو راه بندازه ولی حضور مردم تو صحنه، متوقفش کرد.
مردم ما فریب دشمن رو نمیخورن، 30 میلیون جان‌فدا داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71615" target="_blank">📅 14:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71614">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OycgADxJvm3xeKHGQbE_yHDoUjtLQ4iZvddirRnnYPWlFblW9y-pbIjhAbYhC1dC4CLQpiIjyLFug272yyijOxrWRK3FOk3k9WNSqyOa9fQPyZaTe9GASQOS-ZtHQByvXSqwzAFPdWelZqlhNln38o6XUAyCM2yei34KN49FT741QFKLPVkyHfiZvQ7XHroHMmb3BttUWmDIw-dAyF9mzcNivamRnQXQt2_ZEo_buHm0qbZmUmJT9Ni_Dl6RzUY2fFgdFPgDuPR-gtUIrIger7pVfAZScBrtZN9GWaquxSUd0KO1zfmC8BZr1Huy0gEdgaYnWZZf5S21D707TKs65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🇮🇷
🇺🇸
بلومبرگ:
پس از آنکه اتریش تحت فشار دولت ترامپ از ورود محمد اسلامی، رئیس سازمان انرژی اتمی ایران، به این کشور جلوگیری کرد، حضور او در کنفرانس عمومی آژانس بین‌المللی انرژی اتمی در وین منتفی شد.
قرار بود اسلامی روز دوشنبه در این کنفرانس سخنرانی کند؛ اکنون احتمال دارد نماینده‌ای دیگر از ایران در اواخر هفته به جای او سخنرانی نماید.
انتظار می‌رود کریس رایت، وزیر انرژی آمریکا، در این کنفرانس ضمن تأکید بر اینکه «ایران هرگز نباید به سلاح هسته‌ای دست یابد یا آن را تولید کند»، خواستار همکاری کامل ایران با آژانس و دسترسی بازرسان آن شود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71614" target="_blank">📅 13:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71613">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=bw_UZOAp6VTlOXRmrolZI-kOd5pncvfE_vXuTCyjnJlEK__rrKB3PVu1JfI_eV-v4HdNAQH56Lm5iLJvzTM8O3K0FIV17uDubWnp9xEHQ5qjzv-eQB7RcN6mJq8_X-LVVEC2coD_PK4n0h1nXmWtzNTGKwR-KcUakdwl6tULR19RUYRDU8JzZIaqTPoctvvmnIUtEv297P5lv3966zBcD48W10O1cdPuicq38gXLrq8ndG74pXtkTnrbZyD4eXXTvBz8-Jw1NX3tjV95xb8n045cfUUpM_ZbSlFI5hnOU3nnhfxX1YW9KPMpok8L6coy9ESqjRtXWtrLjwNoMrBwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=bw_UZOAp6VTlOXRmrolZI-kOd5pncvfE_vXuTCyjnJlEK__rrKB3PVu1JfI_eV-v4HdNAQH56Lm5iLJvzTM8O3K0FIV17uDubWnp9xEHQ5qjzv-eQB7RcN6mJq8_X-LVVEC2coD_PK4n0h1nXmWtzNTGKwR-KcUakdwl6tULR19RUYRDU8JzZIaqTPoctvvmnIUtEv297P5lv3966zBcD48W10O1cdPuicq38gXLrq8ndG74pXtkTnrbZyD4eXXTvBz8-Jw1NX3tjV95xb8n045cfUUpM_ZbSlFI5hnOU3nnhfxX1YW9KPMpok8L6coy9ESqjRtXWtrLjwNoMrBwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇳
سخنگوی وزارت امور خارجه هند در جریان سخنرانی مسعود پزشکیان در اجلاس بریکس در دهلی نو، با خوردن یک‌نفسِ یک ظرف آجیل — شامل خوردن، لیسیدن انگشتان و برداشتن دوباره از ظرف تا زمانی که کارکنان تشریفات آن را گرفتند خبرساز شد
😏
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71613" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71612">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567356c89d.mp4?token=BqTS8dMJYN5MIpiw4Rc1s9LHQuKEpS8J8pfFPFnOEhsC38UuFjG20bkErpWwTikFGmtscpjMUwWzLqXa7FXSJaYnX08RM_28T8kkGc44NdJoeekg1Rr90bXqTNxSoZdqYICEM0uGeh5QfmIPBdOAXxpF8PJICIE5Q6KnrL1Q2_ycBqHFmMeAeEE5MIGIp77LJld04hNOcNpHPaqMoayBD9gHMGxSB1wxQIgFrGbk3EXycB-gYss0HdW7ysNQfAB5NTaYkDi4gNuD_BRtwxlK7Du3CWsnjv_JAKQA1LFFlAdCvgJDWFqjPKu24lyPBgumQU6JT0p_0DaB4QG23hctUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567356c89d.mp4?token=BqTS8dMJYN5MIpiw4Rc1s9LHQuKEpS8J8pfFPFnOEhsC38UuFjG20bkErpWwTikFGmtscpjMUwWzLqXa7FXSJaYnX08RM_28T8kkGc44NdJoeekg1Rr90bXqTNxSoZdqYICEM0uGeh5QfmIPBdOAXxpF8PJICIE5Q6KnrL1Q2_ycBqHFmMeAeEE5MIGIp77LJld04hNOcNpHPaqMoayBD9gHMGxSB1wxQIgFrGbk3EXycB-gYss0HdW7ysNQfAB5NTaYkDi4gNuD_BRtwxlK7Du3CWsnjv_JAKQA1LFFlAdCvgJDWFqjPKu24lyPBgumQU6JT0p_0DaB4QG23hctUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی:
توافق میان ایران و عمان حاصل هفته‌ها مذاکرات فشرده است و حقوق حاکمیتی هر دو کشور را به‌طور کامل محترم می‌شمارد.
از کشورهای همسایه انتظار می‌رود اختلافات گذشته را کنار بگذارند، برای تقویت امنیت منطقه‌ای گفتگو کنند و نفوذ بازیگران مخرب فرامنطقه‌ای را محدود سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71612" target="_blank">📅 12:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71611">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rD3B7HUyyDCamfdVArpMSVlCQOGzdjsLupxubGgscFwFZ_yScz7XsZnYWzk8SDC7SkmMVQA9tHUs3pMIro-sEyGubTpMKVubCtDQcqtXIDGX9OUaPvp91xv_XG66j46vFuJMjo-BDIbyWecWu1fBIN44Y7Q5IWGqGq7dzBUsZ_dFJy8urkkgHAsNFvVhe-kWGDZdCO46g-SwFFcUX5Lvq0LbNzfq7_D3UkoqxZW9JAmq2oNrOu9hCVm9ExuxQ3z_4N34OaO0L7CtMAbLbonIYT8JOs3rRbQFYX9cODdiJGQzoUinoyU6592GQC81DKMrTryFcF_lWyKEGYHktobCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه دختر شماره یه پسرو که روش کراش داشته داده رفیقش، و رفیقش تو نیم ساعت این اطلاعات رو از پسره درآورده!
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71611" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71610">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71610" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71609">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0IP3rTdJdusY_1eKzkZoUtrt9cGH6RtyqyBViGTZW-4WemB3homO45nKtUuAIEaJkkTxhLsL2DgvhMKhlvZsILhRgCIof5X56zUWB_vMnj51WxN42yV7_ylhExgqHA5uPtryPl4Rfu7p1CQcBx8z1nBa-73FzjpVqRLtH26EySBiUPjyTL2-8u1rKJgOxRkUNTSlJdZhdOmutKX5XHQtL2ECQ4Iu2vbU0hC4KKTQ5lBz7mpSdw5iKr6Rj3U9hsOjQ0hisS7yp07fcPHqGDFKQQ1O7TlMrHZ3UPwm6DghlfvSGdFZ-aWxAXtKlpKQFrazxXYcPFPN0pCq1qVn4j2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
لیدز
رم
🆚
تورینو
اودینزه
🆚
اینتر
السد
🆚
استقلال
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71609" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71608">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001bfae793.mp4?token=aTfHQ0gHkgUvpIN4K_F06BaQMUUcM3UMYCJ47M4u5q6xUO5_D8xnv0dLbiPX9XP9slSU1hdaSlUo3BKL6y6PSSOO5G8iTTkzQspV8QhsFtZrUI49UijujjSkBwbM8jOgvYr5wnGTsyJFmFJdLfjxvVXKolupcQE0KHb8E8cXOAoyVwqaNjKANBgv8sAGIVu0HXLrhckiaFDIR-PCLLH-C6WicRrRLmFza2zw2kc4Fz4QV70PV4SlIy9XfBPV2CRrASIETZcyfUiEjNGXqdeoyvkNMjeOz-4ldUZke42zz8S79UHroYOhMf7c562iDNWVV-Mc6bBxjTHuvI7SXRD-YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001bfae793.mp4?token=aTfHQ0gHkgUvpIN4K_F06BaQMUUcM3UMYCJ47M4u5q6xUO5_D8xnv0dLbiPX9XP9slSU1hdaSlUo3BKL6y6PSSOO5G8iTTkzQspV8QhsFtZrUI49UijujjSkBwbM8jOgvYr5wnGTsyJFmFJdLfjxvVXKolupcQE0KHb8E8cXOAoyVwqaNjKANBgv8sAGIVu0HXLrhckiaFDIR-PCLLH-C6WicRrRLmFza2zw2kc4Fz4QV70PV4SlIy9XfBPV2CRrASIETZcyfUiEjNGXqdeoyvkNMjeOz-4ldUZke42zz8S79UHroYOhMf7c562iDNWVV-Mc6bBxjTHuvI7SXRD-YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤡
مجری صداوسیما:
اصلا نگران نباشید اوستاد خوش‌چشم مجدد توی برنامه ها شرکت خواهند کرد و انقد پیام ندید و مارو نوازش نکنید که چرا اوستاد چند وقته نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71608" target="_blank">📅 12:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71607">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=JEOdp7KbZeSxgr9CyYfqh9KclQkLdwwJPxNX5-QMDtAT6Of8RC3v7dBfwklNblYPDY6COCUhNyqhOEAsVYIWN1VT-9HXXshaFs0bfyHMV9KJ1nsJsw3t_SsjF64pMarJjHj686k7VMck6VMWH0cpOnHVYP6_T7cEjF4yBd4OxHrTQRSM4OSnsSX1h0efWH5_WTBlSHrjPrc21JL8uZMhbznryJFQq7MfL5ilLxes5uCmqcziIGlptN6vYJAk5lEiRlGLUVmubMiR9NguQgpMdoBe1bTT_9rW_o2K7Cqf59RVtBhZrDMvZ9m_gcExAAP2nWIvoWocbyW3vbHSesFf6x_MJL0HN2OzVoEV_4z0Re1RUQN_fvy4ylxuBd85ite-5wghZM5LMnaxfRd4OtwncKnKP34DJsX1Nk5dGbVADIJL3-kh__SUlTFia_30HtkAIt4e1ksg1lKJtIoESCU2rjFobxl7SSYv6DHlTcv6rrsihc_APPVxqJbOVDW-cgawFjhQDVZl3JUWV6QbYBzuVeZ-UfSNPGwjIynXOjpoL2l8YVEXTaJdN4nvhZvt07oI6eLb4EC7W4dWKelmBBDEIbWLOnUO9s0tw3IZNG-klTu26p2J9HYAvp4Rlm_Ys9YG35ahdu2EuUu-nKpt_Fz5alBVBO_BW7FJ4ce7qo4Hoxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=JEOdp7KbZeSxgr9CyYfqh9KclQkLdwwJPxNX5-QMDtAT6Of8RC3v7dBfwklNblYPDY6COCUhNyqhOEAsVYIWN1VT-9HXXshaFs0bfyHMV9KJ1nsJsw3t_SsjF64pMarJjHj686k7VMck6VMWH0cpOnHVYP6_T7cEjF4yBd4OxHrTQRSM4OSnsSX1h0efWH5_WTBlSHrjPrc21JL8uZMhbznryJFQq7MfL5ilLxes5uCmqcziIGlptN6vYJAk5lEiRlGLUVmubMiR9NguQgpMdoBe1bTT_9rW_o2K7Cqf59RVtBhZrDMvZ9m_gcExAAP2nWIvoWocbyW3vbHSesFf6x_MJL0HN2OzVoEV_4z0Re1RUQN_fvy4ylxuBd85ite-5wghZM5LMnaxfRd4OtwncKnKP34DJsX1Nk5dGbVADIJL3-kh__SUlTFia_30HtkAIt4e1ksg1lKJtIoESCU2rjFobxl7SSYv6DHlTcv6rrsihc_APPVxqJbOVDW-cgawFjhQDVZl3JUWV6QbYBzuVeZ-UfSNPGwjIynXOjpoL2l8YVEXTaJdN4nvhZvt07oI6eLb4EC7W4dWKelmBBDEIbWLOnUO9s0tw3IZNG-klTu26p2J9HYAvp4Rlm_Ys9YG35ahdu2EuUu-nKpt_Fz5alBVBO_BW7FJ4ce7qo4Hoxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ℹ️
باز و بسته کردن (مونتاژ و دمونتاژ) کلاشنیکف AK-74 توسط این بانوی روس
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71607" target="_blank">📅 11:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71606">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
اگه نیسان کشنده ندیده بودی
این ویدیو رو ببین تا ببینی همچی توی ایران ممکنه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71606" target="_blank">📅 10:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71605">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=XAE2eDy4YtBoutO6XweTpgHQTdMTJwkxGlOFQGzibltbi8RcGAxBvTny--20-r1snjEin9AFKOXBiWeD9SHwW2f2rLBAMSD2ZyjPCcOmUZQFjRrxnpvJBpadcTwvjwR-g7O2YETwu-FpnTB7leNSI86zV_KNfI4JERY6xqAZppnfBh9rVI1bN_E8mbA70ccRYXr450tsQYiegOzNXrZZ-GIR5nGV5PwZVD6nCz0M1GvbN9y4Hdevs03dypg7DkLF-kz6mfjy959rcxSWhhhzd9Dn6Cso-FkEYYqJlVDfsxnwo0AR9fVABSxCQDtk2Xy8g_Tg2Jr5VVq63HLVlglfhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=XAE2eDy4YtBoutO6XweTpgHQTdMTJwkxGlOFQGzibltbi8RcGAxBvTny--20-r1snjEin9AFKOXBiWeD9SHwW2f2rLBAMSD2ZyjPCcOmUZQFjRrxnpvJBpadcTwvjwR-g7O2YETwu-FpnTB7leNSI86zV_KNfI4JERY6xqAZppnfBh9rVI1bN_E8mbA70ccRYXr450tsQYiegOzNXrZZ-GIR5nGV5PwZVD6nCz0M1GvbN9y4Hdevs03dypg7DkLF-kz6mfjy959rcxSWhhhzd9Dn6Cso-FkEYYqJlVDfsxnwo0AR9fVABSxCQDtk2Xy8g_Tg2Jr5VVq63HLVlglfhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست سلاح جنگی بر روی شتر توسط یک عرب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71605" target="_blank">📅 10:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71604">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=rzYgSS67SuHatGv6nG-BVSKBt6LPq6zhWCBYZIFlLpRl7MwM8YB-fnxsnlJZJL-vrQExRmuHAYBPqn6jtvwJ2mNDB7WWnBQepoqTpc3n4ZzawbvAwXPPhMFo3yjq6D6o1aVI2sRex2_4zcUTdbca9Rmo79K2oMRCH-YFt4c_4gDZvj10JEEjCwEHsVETBGABNUhbXAzxYHIqiRZJcDD0prdJys3G7gIclNLxxDw402Yt2kT0t8KWJpG5s-0BKHP5D07-d5BYq5tr_XQA2LtsgLP8DVj7CU0tNWfPrFM5bwVgO2VDObWf0pfmLbTpSsB2yn5PD9S5wIT3iC1a_uoviQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=rzYgSS67SuHatGv6nG-BVSKBt6LPq6zhWCBYZIFlLpRl7MwM8YB-fnxsnlJZJL-vrQExRmuHAYBPqn6jtvwJ2mNDB7WWnBQepoqTpc3n4ZzawbvAwXPPhMFo3yjq6D6o1aVI2sRex2_4zcUTdbca9Rmo79K2oMRCH-YFt4c_4gDZvj10JEEjCwEHsVETBGABNUhbXAzxYHIqiRZJcDD0prdJys3G7gIclNLxxDw402Yt2kT0t8KWJpG5s-0BKHP5D07-d5BYq5tr_XQA2LtsgLP8DVj7CU0tNWfPrFM5bwVgO2VDObWf0pfmLbTpSsB2yn5PD9S5wIT3iC1a_uoviQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
زنده یاد مانوک خدابخشیان:
تنها برگ برنده دونالد ترامپ این است که پرونده رژیم جمهوری اسلامی بسته شود. این بزرگترین پیروزی است، درست مثل فروپاشی شوروی؛ این را فراموش نکنید.
چرا او باید وارد جنگی شود که سال‌ها طول بکشد و دوباره در باتلاق خاورمیانه بماند؟
هدف این است که از خاورمیانه بیرون بیاید.
شما به اصطلاح آن دکه جمهوری اسلامی را ببندید، همان‌طوری که دکه کمونیسم بسته شد و همه فرو ریختند، تمام این‌ها هم فرو خواهند ریخت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71604" target="_blank">📅 10:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71603">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
لحظاتی قبل یک فروند پهپاد پیشرفته MQ۱ توسط سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71603" target="_blank">📅 09:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71602">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
یه ایرانی رفته توی تجمعات حامیان فلسطین توی خارج و بهشون میگه <<کص ننت فلسطین>> یعنی فلسطین رو دوس دارم
😂
اونا هم بدون اینکه معنیشو بدونن دارن تکرار میکنن
در ادامه میگه فلسطین رو از حماس آزاد کنید
در آخرم شعار جاویدشاه رو سر میده
👑
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71602" target="_blank">📅 09:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71601">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
مصاحبه کامل و ترجمه شده افسر تسلیحات نجات یافته ملقب به "براوو Bravo" با برنامه Minutes 60 پیرامون عملیات CSAR که در ماه آوریل در عمق خاک ایران انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71601" target="_blank">📅 09:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71600">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
⭕️
تصاویر تازه‌منتشرشده‌ای که توسط برنامه «۶۰ دقیقه» (60 Minutes) پخش شد، عملیات نجات دو افسر نیروی هوایی ایالات متحده را نشان می‌دهد؛ افسرانی که با نام‌های عملیاتی «آلفا» و «براوو» شناخته می‌شوند و جت جنگنده F-15E آن‌ها در ماه آوریل بر فراز ایران سرنگون شده بود.
این دو نفر در حالی که نیروهای ایرانی در جستجوی آن‌ها بودند، در منطقه‌ای کوهستانی در جنوب اصفهان و با فاصله‌ای حدود پنج مایل از یکدیگر فرود آمدند. در این گزارش همچنین تصاویری از حمله به نیروهای ایرانی به نمایش درآمد.
آلفا» هشت ساعت پس از خروج اضطراری (اجکت) از هواپیما، طی یک عملیات پرخطر در روز که با مشارکت ۲۱ فروند هواپیمای آمریکایی انجام شد، نجات یافت.
«براوو» حدود دو روز در پشت خطوط دشمن باقی ماند. او با وجود شکستگی کمر و سایر جراحات ناشی از فرود سخت (به‌دلیل نقص در چتر نجات)، از یک خط‌الرأس کوهستانی به ارتفاع ۷۰۰۰ پا بالا رفت تا اینکه دو تن از نیروهای ویژه امداد و نجات نیروی هوایی به او رسیدند و وی را به بالگرد آمریکایی منتقل کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71600" target="_blank">📅 07:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71599">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71599" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71599" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71598">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX_l-ZFPkxBrv2OLqHAprvfHK9A785xpTTaLiGHVkjae6cWjelgE_NkYeuzGBKLE4R2zwc63293XfoLAlZrRfaW1YpaEBiFS6vEnKYtKpXEL8J7G75Q_7CvK0viMFoS2eeuU3ewPYGwgog4b0XOhBTMMfwfPfKE60xdRmAPR0F5tXnUOexSSIlgjCAMtRcbSyFoso4HY7eY_wLcH3Cii4pZxczPL0skIL5WCzkCKg7JIsMDhtvg_AtiXchyK-qWLkWYz4f1uagVZA93alxD75kLO4Oua9NSewjDO6yzrYUBzRUKfNFMDDTyHsT8di6GEdvgPtTGJvnNVqMAPOKpTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71598" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71597">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=kJpw0uwLlgTVoS9kTNrVRFQlLp_j5osdICSWtBFRdm5vLIF65Wr-p8Co64Q8tVpe41AsCzQrvV5lm06jJbeDlxWVN0S81_r1IUU-vE-qwMjXpCfILkfpTglprcQpmAWcHSb-F0UUN7hKLX6XQ_mrZ57TcUziM9HpkH9Oj1gomnVkXQSIk2LJSVjBTCInpKoT1Ex9MisBXAjxlhrXp29Q4mtvoKdnfGm2zuBogJ1Toprsw6KaJGl4DGSHJ0p4k3JMvxkXtT3DVcz1ynPM3KNXaNfFyL7AVL1rCts5xn2JA_x-a692V_fGraG3LPqGIYqGbID8PPGaA5lEfutr4OTlKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=kJpw0uwLlgTVoS9kTNrVRFQlLp_j5osdICSWtBFRdm5vLIF65Wr-p8Co64Q8tVpe41AsCzQrvV5lm06jJbeDlxWVN0S81_r1IUU-vE-qwMjXpCfILkfpTglprcQpmAWcHSb-F0UUN7hKLX6XQ_mrZ57TcUziM9HpkH9Oj1gomnVkXQSIk2LJSVjBTCInpKoT1Ex9MisBXAjxlhrXp29Q4mtvoKdnfGm2zuBogJ1Toprsw6KaJGl4DGSHJ0p4k3JMvxkXtT3DVcz1ynPM3KNXaNfFyL7AVL1rCts5xn2JA_x-a692V_fGraG3LPqGIYqGbID8PPGaA5lEfutr4OTlKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سپاه به طرف تنگه هرمز موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71597" target="_blank">📅 01:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71596">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZisGzl6WolWFcsoCmKj-CkyjfABzleqXUFjmg6wXkIPxWAWkUcglpRLB8F3mU03YohXseR3GSZXOpLJnNiWoe0nVMhhqpCOxrLZzmDaOi2iLhvzpJ78ONRSymGttF-EOa0TyfQ8oHfLwio-zWcPJuSqMDmQ85onYwIlIaVQYsPH3XpfYh4MaG-TnK1f0ZoYbRVpIi3GfW0ZalQRVscZQgbDnQdC1Y5Rf2uyEev-A1AiAkxU5N1Hk7WqAhuE36PLFKOjC-m-RtUvdt9yxrHiwgQc_wc_DJIAxkiIirtMFyaztKpinS6EDBSPnuHhp82Peg4xCnsx6w2y0hyodKOOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
❌
🇮🇷
🇴🇲
باراک راوید:
یک مقام حوزه خلیج فارس به من گفت که عربستان سعودی اصلاحاتی را در طرح پیشنهادی عمان و ایران در خصوص تنگه هرمز ارائه کرده است؛
زیرا نگران بود که عبارات پیشنهادی عملاً منجر به ایجاد وضعیت موجود جدیدی در این تنگه شود که برای این کشور یا سایر کشورهای عضو شورای همکاری خلیج فارس قابل قبول نباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71596" target="_blank">📅 01:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71595">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=uO0fDWWirbbLOObcygoMgMmjiLIGM2UvfPIc6tQSBhu5rijtYzYGQbmwqY9qx8_b6HH69wAmpka1-0ub0tF9NSsR6UUBhxoxfHvGVSWqX0EHTld-r92EkkTxvrzP5DQwPhEtwMmaj2rRrM-DzzpQbWxxJ1EBW9GNZ9oJ2atFLrFOTk9SJEskjSFWRFCj7YCmYfRXZq0sTIc4WBU05gSEl6CsThx8D-mLkzB_0e-YyXdqfvcfWo4ug2hlO9vBhbuKWiuoqsX7FJeMdlv-qVCgxNmRppGGh4YjApqa4_Pc6KqQ7RVvQpUhYlJfbVWdCKOBBTakMqNcuIJtM_mX__P-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=uO0fDWWirbbLOObcygoMgMmjiLIGM2UvfPIc6tQSBhu5rijtYzYGQbmwqY9qx8_b6HH69wAmpka1-0ub0tF9NSsR6UUBhxoxfHvGVSWqX0EHTld-r92EkkTxvrzP5DQwPhEtwMmaj2rRrM-DzzpQbWxxJ1EBW9GNZ9oJ2atFLrFOTk9SJEskjSFWRFCj7YCmYfRXZq0sTIc4WBU05gSEl6CsThx8D-mLkzB_0e-YyXdqfvcfWo4ug2hlO9vBhbuKWiuoqsX7FJeMdlv-qVCgxNmRppGGh4YjApqa4_Pc6KqQ7RVvQpUhYlJfbVWdCKOBBTakMqNcuIJtM_mX__P-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
ایران می‌گوید دیشب به یکی از شناورهایش حمله شده است. آیا کار آمریکا بود؟
🇺🇸
ترامپ:
نمی‌خواهم بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71595" target="_blank">📅 00:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71594">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjXNAsNK9kIPlaPl3gUBcmD_mVLPQ7oM2Mf9TK_Yzf2kfLu18bIHZlOv4WEfq_ulZyTFzKmYvtsHcNMonpafmbowGfEkHIX85qmheh9LIhWqne0ndKI3EqTlxQl1ZtOtuEkjVXeVpZu5cGbNK5SMAWFzabaOjO4li_NBQ_jlJm5WhzD3c7iIi5tysF1Vi0IiddsDyR-vLE225njU1JE7fL_KuKjWiIjhtFythdlyC0iM-oSB66S-Q38ZOBHPYu0Yf7ArLXYJK6a0-H88O9VFkmrEbXYHi-fZcczxvGE3ToUXA_iWqtYUa4-7tbksiuFikGtKwomrHAg7rxJP9ZE-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇴🇲
بدر‌البوسعیدی وزیر خارجه عمان:
در راستای دستیابی به اجماع، نشست منطقه‌ای که قرار بود فردا در صلاله برگزار شود، به تعویق افتاد.
ما همچنان به ترویج گفت‌وگویی که حامی ثبات و همکاری پایدار در منطقه ما باشد، متعهد هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71594" target="_blank">📅 00:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71593">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
⭕️
نشستی که قرار بود فردا در عمان میان ایران و کشورهای حوزه خلیج فارس درباره تنگه هرمز برگزار شود، به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71593" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71592">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqxX0pa4HUiE-lmMcFJ_8seTmAnk8kgRgXXIhUnbgJDD78GI9kyh7H668ouqn6aCckuLFUhwSvZorBno33iKLTA1tsThNNSiq66QXCawT4wpvx7F6mvMK3XFwag56lh-SxxPWUVQJHAbTN3sMuG3IdCKOl8leBnOB7nyBW63OUJGcklhViqBSQfQR17DWTiGJZEZFwQYxI_r3uiI8m6WYn6Mx9s9WIMeiovrNwQbTo5I4rz3RbfLZ0jHdurHslMXfQbuaX2h5yeMn1fTKFqijWv6tz9TcFKG8fFhGQMAJbagqxTQ6PEEGBDG54CYgdqyvRf-AfBNVphvKlpurXn2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های عجیب پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71592" target="_blank">📅 00:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71591">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=cjiExMHjTu9v_Ow4uuD-wseKljyxaOc3-QQFpmxijo-XijzLnhJ8XZnwkCt6vwaF3a2012FledA1aCvUV4ebeedMx9s6pFe4rZTXA4eI_ujKEy_bLI6t6UE03o155Bd5xu2iAXtma7kyxtESjhKeP_LxjNGoOcJCTxvDAEJ6CWH3WRWg-w1VXXYA6P9Ndluh3fdxiRVMpoZ2213QJ91NPIeYVeIw3E5l-uVVD3g_aRUek2zHJGaxX7eLAnUe-cTGeXHRqOz4dNNVCpZzqxASJImT7jQZDXZeNBkzD6HCmbBEEL0H_CXc2-ZVg5QCspDOpRXr1G-A4WRIPVCiN6I7ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=cjiExMHjTu9v_Ow4uuD-wseKljyxaOc3-QQFpmxijo-XijzLnhJ8XZnwkCt6vwaF3a2012FledA1aCvUV4ebeedMx9s6pFe4rZTXA4eI_ujKEy_bLI6t6UE03o155Bd5xu2iAXtma7kyxtESjhKeP_LxjNGoOcJCTxvDAEJ6CWH3WRWg-w1VXXYA6P9Ndluh3fdxiRVMpoZ2213QJ91NPIeYVeIw3E5l-uVVD3g_aRUek2zHJGaxX7eLAnUe-cTGeXHRqOz4dNNVCpZzqxASJImT7jQZDXZeNBkzD6HCmbBEEL0H_CXc2-ZVg5QCspDOpRXr1G-A4WRIPVCiN6I7ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو تبلیغاتی بانو سیدنی سویینی برای novig
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71591" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71590">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1NIjOfYv9lsbi0I8685bK4-Mut3c9MtH5HiwSEpeD4WFHWzKujfHMuheYx7DLI_g_Q6_vcMoM_YgOSLG4vasFaJgRVazLezrtLdzB0A70pKJZIfG_ucI3Yb1ZDN-UCUwnfzcyi9NTodwnL9XPCo7B4LWRWDos1v0m_eqv7qcoDTHxD-9YUVP4M_T3r_MIfx8djRMmRM0yJvfMOBOwTuTxOkeodNNEodcY24CtWHbtocOa0YUFQnS-ibKsYrmZmMawDXUux1pLGnau-HlsyfSdVfalZI1r0qO0ZG8VA_4d4zDRm9dDU7IqHsvjZGOxKm5PxI3hYFgXgQGh_hmH64-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇺🇸
نیویورک‌تایمز:
مقامات ایرانی می‌گویند که رهبری این کشور طی هفته‌های اخیر بر سر دو راهبرد برای شکستن بن‌بست با ایالات متحده دچار اختلاف نظر بوده است: بازگشت به مذاکرات یا تشدید درگیری‌ها.
بر اساس طرح تشدید تنش، ایران حملات خود به اهداف آمریکایی - از جمله شناورهای نیروی دریایی و نیروهای نظامی ایالات متحده - را افزایش می‌دهد و هم‌زمان تلاش می‌کند با بالا بردن قیمت جهانی نفت، طرف مقابل را وادار به پایان دادن به محاصره دریایی کند؛ محاصره‌ای که تجارت ایران را فلج کرده و صادرات نفت این کشور را به صفر رسانده است.
ژنرال‌های تندرو، از جمله سرتیپ سید مجید موسوی (فرمانده نیروی هوافضای سپاه پاسداران)، طرح جنگی مفصلی را به شورای عالی امنیت ملی ارائه کردند. این طرح خواستار آن بود که ایران و گروه‌های هم‌پیمانش - به‌ویژه حوثی‌ها (انصارالله) در یمن و شبه‌نظامیان شیعه در عراق - دامنه حملات خود علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را گسترش دهند.
مسعود پزشکیان، رئیس‌جمهور، و محمدباقر قالیباف، رئیس مجلس، با این طرح مخالفت کردند و هشدار دادند که اجرای آن می‌تواند ایران را به جنگی بسیار گسترده‌تر بکشاند، موجب حملات هوایی سنگین‌تر آمریکا شود و بحران اقتصادی کشور را عمیق‌تر سازد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71590" target="_blank">📅 23:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71589">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=jDfEKh9m9HTRYoF2BDxKJtMB54ibPocYUkmDlHr1NDTk3ZI4LFz7BR9TBMR-ytSREo8l1kLADsOwWO3X8R2cHEVo4hulKjlvhlBQmuLk3rRcNOtT-A12IfbgJfm5eM17HAF3KM8Yj5UeD2fcznqbOVN7qBhTHUfXa_XimdLrssN4bDDm5HxD83sCGb6jKXa94I_qt0D8rEQXMi_ireJdWQTTZParcVlmfSExhc8Xzxar_CCA8Qd81EeXzzqAr4zJdsdyyZtyVz0Qy87n_7LL5o3kisAIJuEbo6BR28Nlnt0QvK-lAPga1zbNDuxknBStDOZeteFCrng6DNXDXEJzTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=jDfEKh9m9HTRYoF2BDxKJtMB54ibPocYUkmDlHr1NDTk3ZI4LFz7BR9TBMR-ytSREo8l1kLADsOwWO3X8R2cHEVo4hulKjlvhlBQmuLk3rRcNOtT-A12IfbgJfm5eM17HAF3KM8Yj5UeD2fcznqbOVN7qBhTHUfXa_XimdLrssN4bDDm5HxD83sCGb6jKXa94I_qt0D8rEQXMi_ireJdWQTTZParcVlmfSExhc8Xzxar_CCA8Qd81EeXzzqAr4zJdsdyyZtyVz0Qy87n_7LL5o3kisAIJuEbo6BR28Nlnt0QvK-lAPga1zbNDuxknBStDOZeteFCrng6DNXDXEJzTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کشتی که امروز صبح در نزدیکی جزیره قشم در جنوب ایران مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71589" target="_blank">📅 22:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71588">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=TatlCTvBBtWKuW8sy6yw7tksW0n-rkwHV6NU4PuwZjBIQVBPBA9asyHkICROS5meH2qc3q2zS1x4-yImBbDZO2I7LNzfDYWS5Ufy-LCWgSI9SJR9_KKKDJ5F0UuA4gN3CTFStRPEvbQL55ujQ_PMw1OImK5ISDt9DlDkx6fnkYyeOq9Ba9JDTlmgHfvH8rVKy3IqQu_gPepVx0Di6hUchUT8E4AXJ7BGPqya554uEgCdm5wegvZGi5VLCeaEbZDAyVeuQXPYmBM1wSSOmYF3pqLmyin6tDlaq5seMJ4DlM1vZE3AqZnkx6lx7rarc02lPFfNYZl4Ov_6gaCXi066eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=TatlCTvBBtWKuW8sy6yw7tksW0n-rkwHV6NU4PuwZjBIQVBPBA9asyHkICROS5meH2qc3q2zS1x4-yImBbDZO2I7LNzfDYWS5Ufy-LCWgSI9SJR9_KKKDJ5F0UuA4gN3CTFStRPEvbQL55ujQ_PMw1OImK5ISDt9DlDkx6fnkYyeOq9Ba9JDTlmgHfvH8rVKy3IqQu_gPepVx0Di6hUchUT8E4AXJ7BGPqya554uEgCdm5wegvZGi5VLCeaEbZDAyVeuQXPYmBM1wSSOmYF3pqLmyin6tDlaq5seMJ4DlM1vZE3AqZnkx6lx7rarc02lPFfNYZl4Ov_6gaCXi066eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
زهران ممدانی شهردار نیویورک :
قربانی اصلی حمله ۱۱ سپتامبر عمه‌ی من بود که بعد از اون اتفاق نمی‌تونست با امنیت از مترو استفاده کنه چون حجاب داشت
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71588" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71587">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU33dNlGbP51v2miujiTF48-CM1Jr9PCDavI1H-ol7rm-CGzQbzCLIncqrM1uCMyauEStvSv8d0hPfga_iA8306NxN8l3DGShGZvpDwWXWOsz-jlLHKG1Rh3MeGCYLO5u5ugiK2TgnesZc1V9V9uYg0s7vMTNEYPyQgdUziK5R8YphsNcxzCE-vuILKX4SwBlZ6eRJ8hALnQmHeTp0CF5Dly2GZOQC2dP35CtKDpwt-I2NwB3QKmGJzV01OFcW45CrFnIFBWxz5Ln7BYKZqOwZQmQrPfMBVquVaPfCiS3WoQ2Z7-xMJObo4WGAGVrnpiZp2J7TXQqvinhzkXfhMnlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
🎮
کنسول بازی ps5 pro به قیمت تقریبا ۳۰۰ میلیون تومان رسیده!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71587" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71586">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643027f01a.mp4?token=PS5J1tYfKZFUDK6TOpPGi6ygaTvrbYDzWYDSwbdbidl2tZ3xJ0ZhsBRbFnvU6fvAihvtVhDO0XpMagclES3Q0_U_tHL_D-nt9xqNO6QehtkRQkFiEXN_j93LZVM28ZlHnScxecZSa8LGTAmxMfCRsBUq1ziaCNzHt1DERCIvSOc6K_hlejmQyi371GFAA_mQN7SHeeLdvoY40oZ1WsuX0tdf05EHy2G3uh8eQMN6P8HXXIuy38o-8W7aCfRJ1ZS75EmHNFzqGPxcxyve4vJpx4wRytxsAUsAbOA0RQNID0v8Jv-i4o1S4ZqZBauVAbHHi0tL0s02RKvxbWu4kGlGpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643027f01a.mp4?token=PS5J1tYfKZFUDK6TOpPGi6ygaTvrbYDzWYDSwbdbidl2tZ3xJ0ZhsBRbFnvU6fvAihvtVhDO0XpMagclES3Q0_U_tHL_D-nt9xqNO6QehtkRQkFiEXN_j93LZVM28ZlHnScxecZSa8LGTAmxMfCRsBUq1ziaCNzHt1DERCIvSOc6K_hlejmQyi371GFAA_mQN7SHeeLdvoY40oZ1WsuX0tdf05EHy2G3uh8eQMN6P8HXXIuy38o-8W7aCfRJ1ZS75EmHNFzqGPxcxyve4vJpx4wRytxsAUsAbOA0RQNID0v8Jv-i4o1S4ZqZBauVAbHHi0tL0s02RKvxbWu4kGlGpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مدیر سامانۀ هوشمند سوخت:
خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71586" target="_blank">📅 20:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71585">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
اطلاعیه قرارگاه جانفدا:
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71585" target="_blank">📅 20:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71584">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=H2olKdCe_2KQ4-AZHoLMfQIXRfmbIM-7dU2tzN_8_kH_qWPcaqh_WTuCtKBu5diO2_wu1d_rZjHRriCh1pk2qtEHC1Bz-Uqss0SuZjuZRx3VIrXZe3-Wr-mB500qjMoCxJS_I3yPW3xksXy8Tf96zbR-C1SZBii1iucTvDfQIkSxe-TGkB6JaQU764ty5uxIol5SHhRCOBLhIWawDIw_9exruSUbKuLmc9eRVRdCPWYArKYjX5ZSIl6uhaqZWpQ_wYZBEwnwex8dhvtahQHA025QBg9nZKNug7nYwROl9-E7bRiAEDp_iNCrFDt0NWea-5zQcl2eVqmIpRLOWpkdJlmaJCtqTvC0Z_qxYfeLTt0kc8grmR_byiq-H568NrCBQcalyEwX1lI39j5EjcR5Qw1gcmfBGkOuDaO_gg2pJIVTol01wkSP2jLgbVv2a5YBUndbfUO3xsqsjpEBkHKMm2uC6V5a_gGljKiQkyb6AIX8yPA4pfbV4nui08x0gZz7fVXyzvGO0mXQeZ-VigAY8qS-rUgOJIgc_LQqVWmJzcdnP-mpYFV3--une1mSUxixscrAepXvzMOYY2JAXMF0S5kRK_Nll5dNK6FMCEtQ1KOQBE4HRDo5QOrZPcVQuPeKdewgn-ajhoWh-IrN9_4FCc-10C6XpZvh_yXWQLXWDWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=H2olKdCe_2KQ4-AZHoLMfQIXRfmbIM-7dU2tzN_8_kH_qWPcaqh_WTuCtKBu5diO2_wu1d_rZjHRriCh1pk2qtEHC1Bz-Uqss0SuZjuZRx3VIrXZe3-Wr-mB500qjMoCxJS_I3yPW3xksXy8Tf96zbR-C1SZBii1iucTvDfQIkSxe-TGkB6JaQU764ty5uxIol5SHhRCOBLhIWawDIw_9exruSUbKuLmc9eRVRdCPWYArKYjX5ZSIl6uhaqZWpQ_wYZBEwnwex8dhvtahQHA025QBg9nZKNug7nYwROl9-E7bRiAEDp_iNCrFDt0NWea-5zQcl2eVqmIpRLOWpkdJlmaJCtqTvC0Z_qxYfeLTt0kc8grmR_byiq-H568NrCBQcalyEwX1lI39j5EjcR5Qw1gcmfBGkOuDaO_gg2pJIVTol01wkSP2jLgbVv2a5YBUndbfUO3xsqsjpEBkHKMm2uC6V5a_gGljKiQkyb6AIX8yPA4pfbV4nui08x0gZz7fVXyzvGO0mXQeZ-VigAY8qS-rUgOJIgc_LQqVWmJzcdnP-mpYFV3--une1mSUxixscrAepXvzMOYY2JAXMF0S5kRK_Nll5dNK6FMCEtQ1KOQBE4HRDo5QOrZPcVQuPeKdewgn-ajhoWh-IrN9_4FCc-10C6XpZvh_yXWQLXWDWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی آموزشی برای دخترای موتور‌سوار چنل که قطعا بکارشون میاد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71584" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71582">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFbKsJLf5PwEaBG-0Lhtj7tLrfXrGeqimfKENaBzHwbGGlHoVlOyXyrJGG8tLLgmBJRS6AvntnVYMU-DyGdZe77JRIcMXdK8bdpF8hHxd8k320OIXOpyfkCXDSFCX2QBmVf8OmhuevgAVtFSixY3nqMO8g3CynF0OBfqTz4vjT6Hcu89xfr-yBWsno9up2e0KDV0OCyien-MnzUFl5U0lIh3FQA5WORi6xrWYBxlsZyARW5lzitAd3KPzR5zf9Sq6wbcFFqxPH4PppzPsTQx3Fb4TyDCfIEkGRJmTChs42dyLL6Ta747XO4sY9TCquCbvTWVQsvK0tpNq-rglqGJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5vStwuQbt37-4o3QKFA1HCEsLiMYjT0WLaVV_HDj2ja_tjF4M4jUnwdumr4BDI45sxRo6Qy6V4TW_Atfs8H7RU6FdTN9A0EcH_XbgATt8F3xdXDk6v65OVGcegoc9VRHnBgZZsHp6-3jHRlaGQi0S1vg_4ITRnChG9afZxQg9q7OKwURqvRcLPTGsaeQusoXvgej3MV4_Z6TBVw76pJnj-BeTVL_1pXIiNNOwnvl_JBCtsBZpG37AZ_7fA1B9Glzpdh9ZZKPyJUatSBGSqp9zCBVwNM4wPNuN91Es7XUngo3bSL9uy1lhuAVhchCuSRJZ_BFjjgaJPPZwQuVblybA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👑
دفتر شاهزاده رضا پهلوی:دستگاه کشتار و سرکوب جمهوری اسلامی بار دیگر قصد جان یک زن جوان را کرده است. سودا (مرضیه) ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، پس از ماه‌ها بازداشت و تحمل شکنجه، تنها به دلیل فعالیت رسانه‌ای، در بی‌دادگاه رژیم با مجازات اعدام روبه‌رو شده است.
صدای سودا باشیم و از همه ظرفیت‌ها برای فشار بین‌المللی جهت توقف ماشین کشتار رژیم استفاده کنیم.
سودا ۳۳سال دارد و ساکن بندرعباس است.
او در تاریخ ۹فروردین بازداشت و اکنون با اتهاماتی چون "عکسبرداری از فاصله دور محل اصابت یک موشک و ارسال این تصویر برای یک رسانه فارسی خارج از کشور" به اعدام محکوم شده است.
او حدود شش سال است که به بیماری ام‌اس مبتلاست و علاوه بر آن از بیماری‌های پسوریازیس، نارکولپسی و کولیک معده نیز رنج می‌برد و نمیتواند در زندان بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71582" target="_blank">📅 18:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71581">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mor02-pMo1ythnvCidGgNo0BVu_R6RUtXId4_K2t3MPFkG7XsagCJoApYz1-BXAp5CYBNlZB9Vn9Ypq0EsLR2YYAE6PqnrmFLLAU9Q1qj0PS8LPn3v-kkwaQen2hQ31Ts3jJ6swFB2WtcKxW0verVnHmm9UJXTzJBrCLb9y2UKxKIcPN4Z1pqJpEvtxri6XXwy29WKfKcrai_Xgyd48Ncf4SwXFD-rv39fpQjO5NbgB9I25p6692WfiGHTdEBX_Ojx9ji15FAvoYNn0yLuT3SLjaPElE0XZYCzZ8U7wYz-nN7Zexpd9dzX7B1aZFWEQGQi0GSgaB-RQ7Rfafw3KunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
نیویورک تایمز:به گفته مقامات ایرانی، تندروهای ایران با صدور دستور حمله به سه کشتی تجاری در تنگه هرمز در تاریخ ۷ ژوئیه، مخفیانه توافق صلح با ایالات متحده را که اوایل همان ماه حاصل شده بود، مختل کردند.
گزارش‌ها حاکی از آن است که مسعود پزشکیان، رئیس‌جمهور، احمد وحیدی و بخش عمده‌ای از رهبری ایران از این عملیات بی‌اطلاع بودند.
بازرسان رد این تصمیم را به جناحی مرتبط با حسین طائب — روحانی بانفوذ و رئیس پیشین اطلاعات سپاه که از همان ابتدا با این توافق مخالف بود — رساندند.
حملات ۷ ژوئیه منجر به حملات متقابل ایالات متحده در روز بعد و همچنین یک کشمکش قدرت بزرگ در داخل ایران شد.
تا ماه سپتامبر، ژنرال‌های تندرو دست بالا را پیدا کردند و به جای بازگشت به میز مذاکره، راهبرد تشدید حملات علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را پیش گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71581" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71580">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71580" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71580" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71579">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_pH1vsAuN37bpXVpNslibAjYDgLm5pHFvTftyAmp11M0zAdv37KbVqUgh-9ODPD-3e1CpLxLRAenoGSSF8TJxtKoRx4SG5Nzz1_VWKIzr1KFkFoNEP6m9FRUlfw7IJzLM71FeuNw9GpHE7LXhyLTajQTFZu3IbjXmHDzU9MBFapFpZNHTXBZlH_ZSACs4xImkDrWndpPQsgqi3pLYR_GnXa6UF-11B2Tqh3Tj2bTToSErCoyzf1llY2k0d2TvNvHveimr3lZ3SOoeOqo04qrRWzkQOzc48CCWRKZns9VqW3LaoMWFoSOV4rck_pK--8uy0QdQY11Zg-kh0NWDCpog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71579" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71578">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=t46RAolgLTdOIlAxWPu-2ldQZQQgIJzhu0U6aa44Fu9WgnGvVNigpYPviH7i7SJzDVhYPLuOWTFjzK1QMo1dWcigCzZDRK-HwBeb-YHKvnlTE5TW_aXjwTIjyU_vMv9De-xzpmbkMf1ab4dq1jw8Xbqzw_Y3lpfEk7R4jQLSRF3K9mv3nbGPzc98IGkFqGZi8_JeJA7jrlhriyjHJoe03dpyg6mRgB5m8xkYcp70WX7Q8cqdrbLWCvmXwN3fxgE_-yDWmHp0PcmUqyBTFVcxBCDzPJFcTgY23eaX5YKsRc6SBHjD0_Lv10RlBkPbfBDGondHT8IOSAcTM9_Cgv4cA5GFZdYn7orlps8MyO7byQcUI5Hz-SA1rqyYRPLHohZOezLCudKn9XhDFBvXbG5YGVitSwbfLBxthf4aqAg8RUQtlM7EkZwjsmX7I7w4Xs9xONkRrFFWQcE_AgYX524dIw9Uyc7BoSzVJ2v79Ea6ATGumTMpYXRtKvwrblvNjhkeLL0N3A6AT4DS4Y2m8Zi-OuoIYwvg-t8MZVk4ocWSuiMz3g1dJklOnKePpN6gZGXrGQYsUvnRyoBzAetkiH6VbB4zUoArM4kvoOi3nK5hAhPuwMggLRFnnyfG_G_xrygmsCNvvz2uCeUF_fRLp2V6E_xjptBtbu_QH87jEO6-6IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=t46RAolgLTdOIlAxWPu-2ldQZQQgIJzhu0U6aa44Fu9WgnGvVNigpYPviH7i7SJzDVhYPLuOWTFjzK1QMo1dWcigCzZDRK-HwBeb-YHKvnlTE5TW_aXjwTIjyU_vMv9De-xzpmbkMf1ab4dq1jw8Xbqzw_Y3lpfEk7R4jQLSRF3K9mv3nbGPzc98IGkFqGZi8_JeJA7jrlhriyjHJoe03dpyg6mRgB5m8xkYcp70WX7Q8cqdrbLWCvmXwN3fxgE_-yDWmHp0PcmUqyBTFVcxBCDzPJFcTgY23eaX5YKsRc6SBHjD0_Lv10RlBkPbfBDGondHT8IOSAcTM9_Cgv4cA5GFZdYn7orlps8MyO7byQcUI5Hz-SA1rqyYRPLHohZOezLCudKn9XhDFBvXbG5YGVitSwbfLBxthf4aqAg8RUQtlM7EkZwjsmX7I7w4Xs9xONkRrFFWQcE_AgYX524dIw9Uyc7BoSzVJ2v79Ea6ATGumTMpYXRtKvwrblvNjhkeLL0N3A6AT4DS4Y2m8Zi-OuoIYwvg-t8MZVk4ocWSuiMz3g1dJklOnKePpN6gZGXrGQYsUvnRyoBzAetkiH6VbB4zUoArM4kvoOi3nK5hAhPuwMggLRFnnyfG_G_xrygmsCNvvz2uCeUF_fRLp2V6E_xjptBtbu_QH87jEO6-6IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ایران به‌شدت خواهان توافق است.
آن‌ها مدام تماس می‌گیرند. می‌خواهند توافق کنند. اما باید توافق درستی باشد؛
من تن به توافقی که خوب نباشد، نخواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71578" target="_blank">📅 17:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71577">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=E086XbFJxl3JQM2JociRuxa89KXT4BBoxn_7lSXZbWyTEUA-7LbADD2zhiO7zoWYzP6MK_GCcyrquBh-YFXR1xJTbWTair83qdmFWODWwn2_GaKgN7YX6FIFnB0yFwhNzew9avYoulONmYblUt3M2VOgdVwvE_9W81kTV9uTt5lHMMkhiQd_NQJkO8rwLCx6KVaNb_R7jNzk0aNZksJA8B1gB7g6EiOWa0bSmANpWFWPsjhpQjbRBoF98z-50_LApQXpDPHZTHgJzrcPHz99jhGO-tJjSWymLVpJzy69F2mqs8Oz4rdzc1ETRDh36SMmtJfT_I7e1NpfU0cOJur3aK3T4kzp3NQXA5eHaQx8u1PMVTs3fUSpL58ual9sZ8szgn_f9dvEQmuB68LNgq1EZwPksZtrWjhW0s3uC_zxYWoF35TK71bH0NXHOI4izPnfT1DxnyFmYeoE8v_3sntDT7sEpwGHoJjJRzvAha3XuYOwuqKqd94WmCmmN7ktMUHDvmPcr2b6VCpSm_RB1W4Q_n5EFz-p_CnXnQdaAsCpbWQzHyZmO8EwAjr8xa0YBJlzND3Gw4pxXL88OV3VSCwpohgZDAJooVCLNOtFUc912-q8nrCXeIFpp8TEEDXr9xBlx5MLazisDoxxGmjaH2LnW3r2UFEwhem8UszcqzNVdNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=E086XbFJxl3JQM2JociRuxa89KXT4BBoxn_7lSXZbWyTEUA-7LbADD2zhiO7zoWYzP6MK_GCcyrquBh-YFXR1xJTbWTair83qdmFWODWwn2_GaKgN7YX6FIFnB0yFwhNzew9avYoulONmYblUt3M2VOgdVwvE_9W81kTV9uTt5lHMMkhiQd_NQJkO8rwLCx6KVaNb_R7jNzk0aNZksJA8B1gB7g6EiOWa0bSmANpWFWPsjhpQjbRBoF98z-50_LApQXpDPHZTHgJzrcPHz99jhGO-tJjSWymLVpJzy69F2mqs8Oz4rdzc1ETRDh36SMmtJfT_I7e1NpfU0cOJur3aK3T4kzp3NQXA5eHaQx8u1PMVTs3fUSpL58ual9sZ8szgn_f9dvEQmuB68LNgq1EZwPksZtrWjhW0s3uC_zxYWoF35TK71bH0NXHOI4izPnfT1DxnyFmYeoE8v_3sntDT7sEpwGHoJjJRzvAha3XuYOwuqKqd94WmCmmN7ktMUHDvmPcr2b6VCpSm_RB1W4Q_n5EFz-p_CnXnQdaAsCpbWQzHyZmO8EwAjr8xa0YBJlzND3Gw4pxXL88OV3VSCwpohgZDAJooVCLNOtFUc912-q8nrCXeIFpp8TEEDXr9xBlx5MLazisDoxxGmjaH2LnW3r2UFEwhem8UszcqzNVdNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ماجرای ایران درست بعد از انتخابات میان‌دوره‌ای تمام می‌شود؛ شاید هم قبل از آن، اما قطعاً بلافاصله پس از انتخابات میان‌دوره‌ای پایان می‌یابد.
قیمت بنزین به‌شدت سقوط خواهد کرد،خب، من می‌دانستم چه کار می‌کنم و باید آن کار را انجام می‌دادم.
ایران نباید به سلاح هسته‌ای دست پیدا کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71577" target="_blank">📅 17:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71576">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=Hk6JQRTuF7lK96r9i3hm8O8mccEYByquGzI0lCR3AUsYwCTYmOIt7f96yvOUAvhiIpr0JgxoHcnh2ype1tn7u10b_z4_8NlSVifr7OrSfQ_vqIXzQCHsgKgrRxgmAOEKXk3toe3jZ8dREvC4kjoXmFppxBFR66gDUgxVeO_eiD1Mk6o5MawAVS1NvsiWOJwn1_myn1bEOhou7cfQ6qvUJrDbQwCdgEwJ7JwQhGmtXApB_PeZrO_AHX0Q8lboZqr_DVrTJXMtd_qQNbtNZZh7JdHzJBYa8Fg0Oi7vTzxiq59tpYHZ3tt_Z1f1s2BDe99nUvoeqs_R_r3mM6gZseGHhVtaItFAu5YBTse0ysJDHB4lEx6fDNe-IQEBTqjgYNkAnJ7ANY8pxVP8Vul1_EdB2wAurp_urTy2NGzTIdKREWqK0dz2wepWeyYj2bz-M2s8Wf8LEXa5bva6aFjKElyLnQ9d-uDDyhyRCtqksed5QRgyeeDTeSpNA6DrcsRGM7zym9bWOeC47Gta9iBQV1Vm02lH9ceOlVfhv5mK-5QrAfrZf3Ht70Le6VshNsnWmvmPrWgziGk8vEsUyhxjB4LKV523mX-d-_byDFu3uXH4mNHrDmOh9RPBUI2cZXTB41BWnoaSBAoCMtevNqnpctVEdM96Q68f4WCXBpkBAgBi0U4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=Hk6JQRTuF7lK96r9i3hm8O8mccEYByquGzI0lCR3AUsYwCTYmOIt7f96yvOUAvhiIpr0JgxoHcnh2ype1tn7u10b_z4_8NlSVifr7OrSfQ_vqIXzQCHsgKgrRxgmAOEKXk3toe3jZ8dREvC4kjoXmFppxBFR66gDUgxVeO_eiD1Mk6o5MawAVS1NvsiWOJwn1_myn1bEOhou7cfQ6qvUJrDbQwCdgEwJ7JwQhGmtXApB_PeZrO_AHX0Q8lboZqr_DVrTJXMtd_qQNbtNZZh7JdHzJBYa8Fg0Oi7vTzxiq59tpYHZ3tt_Z1f1s2BDe99nUvoeqs_R_r3mM6gZseGHhVtaItFAu5YBTse0ysJDHB4lEx6fDNe-IQEBTqjgYNkAnJ7ANY8pxVP8Vul1_EdB2wAurp_urTy2NGzTIdKREWqK0dz2wepWeyYj2bz-M2s8Wf8LEXa5bva6aFjKElyLnQ9d-uDDyhyRCtqksed5QRgyeeDTeSpNA6DrcsRGM7zym9bWOeC47Gta9iBQV1Vm02lH9ceOlVfhv5mK-5QrAfrZf3Ht70Le6VshNsnWmvmPrWgziGk8vEsUyhxjB4LKV523mX-d-_byDFu3uXH4mNHrDmOh9RPBUI2cZXTB41BWnoaSBAoCMtevNqnpctVEdM96Q68f4WCXBpkBAgBi0U4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، آیا فکر می‌کنید کنگره باید آن ۵۰۰۰ دلار را تصویب کند؟
🇺🇸
ترامپ:
همان‌طور که گفتم، نمی‌دانم اگر جمهوری‌خواهان پیروز شوند، انجام این کار چقدر آسان خواهد بود.
صحبت از ۵۰۰۰ دلار برای تمام بزرگسالان کشور است و ما به‌راحتی از پسِ آن برمی‌آییم، چون درآمدهای کلانی داریم؛
وضعیت ما هرگز تا این حد عالی نبوده است. دموکرات‌ها نمی‌توانند چنین وعده‌ای بدهند، چون در آن صورت اوضاع بلافاصله به هم می‌ریزد و نابود می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71576" target="_blank">📅 17:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71575">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=YjwQbCxZnNgEWXow5ys7zT0skxCSCRX2hS37AqPvGMPb5pQsTDG4gWK9Jyl1yrmFQf6k7Fd-VxGO8FFg6eMlfvJTtSvyxT7DSies9ZAu7rdg1H2Cg6MdQc5glShmEg5tjAJFLI4bq0VnMpX42SWTePp96gRmLGoFsGVVaHqR5YyRXCw1qZXazm9FbJJyWFC4EKlJxBA0GJK4j4VX79w08zFkFMk78n7JK1roQM_CQltwvoyws2M4v5n_m2n9q2hPnquel5JiTiU0-Om8Ul4XTKb4YwiAcHd9LiWjAp0k0MeL0ZKSGSmkk8749mzTe6yxmLGf_YTgdZWt5m29hF_B0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=YjwQbCxZnNgEWXow5ys7zT0skxCSCRX2hS37AqPvGMPb5pQsTDG4gWK9Jyl1yrmFQf6k7Fd-VxGO8FFg6eMlfvJTtSvyxT7DSies9ZAu7rdg1H2Cg6MdQc5glShmEg5tjAJFLI4bq0VnMpX42SWTePp96gRmLGoFsGVVaHqR5YyRXCw1qZXazm9FbJJyWFC4EKlJxBA0GJK4j4VX79w08zFkFMk78n7JK1roQM_CQltwvoyws2M4v5n_m2n9q2hPnquel5JiTiU0-Om8Ul4XTKb4YwiAcHd9LiWjAp0k0MeL0ZKSGSmkk8749mzTe6yxmLGf_YTgdZWt5m29hF_B0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
نظر شما درباره دیدار کشورهای حوزه خلیج فارس با ایران چیست؟
🇺🇸
ترامپ:
برایم اهمیتی ندارد. این به خودشان مربوط است. اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71575" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71574">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=Rw_attYKAqZvfFfDg65sZXwjLP9MbXILdtfCZhksWI3gT1TyMCCwTJA0SKlzLFjOX3a40B6OH1SpvadYQ59WlUvwcIoXHGe9fRXiIJBpIMo1X4ySo58hyKwh6JwVWyMpvcJc2_2JBdhT43Vn8xGzSGyqD2VEqOCF7kTv5HtJBmBSCiZxqjpzAqCqJ7v8iAY7CrADQCnV6RouU-ZFFOPD5J5NWXkaUqoe-NDIZwjNj-NSpO78T2p-x_kwoEGEXy1tKpdfLZDsw2sXQ9P5di3quJ3_U7D2o3BwMtyoh98A7i38iUPkTPnMC5LWwUKAQyU6BJRl4JqtZ5CdYrTXu7YYUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=Rw_attYKAqZvfFfDg65sZXwjLP9MbXILdtfCZhksWI3gT1TyMCCwTJA0SKlzLFjOX3a40B6OH1SpvadYQ59WlUvwcIoXHGe9fRXiIJBpIMo1X4ySo58hyKwh6JwVWyMpvcJc2_2JBdhT43Vn8xGzSGyqD2VEqOCF7kTv5HtJBmBSCiZxqjpzAqCqJ7v8iAY7CrADQCnV6RouU-ZFFOPD5J5NWXkaUqoe-NDIZwjNj-NSpO78T2p-x_kwoEGEXy1tKpdfLZDsw2sXQ9P5di3quJ3_U7D2o3BwMtyoh98A7i38iUPkTPnMC5LWwUKAQyU6BJRl4JqtZ5CdYrTXu7YYUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
در نهایت ما آنجا را ترک خواهیم کرد، مگر اینکه تصمیم بگیریم بمانیم و نفت را برای خود نگه داریم؛ درست مثل ونزوئلا.
دیگر درباره ونزوئلا حرفی نمی‌زنید، مگر نه؟ خوب به این موضوع فکر کنید: میلیاردها و میلیاردها و میلیاردها دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71574" target="_blank">📅 17:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71573">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇾🇪
حوثی‌های یمن تصاویر مفصلی از عملیات نظامی جدید خود با عنوان «و خداوند از نظر قدرت و کیفر، سخت‌گیرتر است» منتشر کردند؛ ویدئویی که صحنه‌های نبرد در جریان تهاجم اخیر آن‌ها در ساحل غربی را به تصویر می‌کشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71573" target="_blank">📅 17:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71572">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=dXDTusq-Qd0brX6sZLbWJFhgc5tcO47usfFjkWGgBdZyzG5KBqakx-s2knCQfmqihaKj6frAeZIWhXUpG8k6EyU8XcRD2ksKxOz1kYXS8Ex6Swe_ZvuubAelHRVDqD9Gk6PL-B0VNOphX6B2dbiOuxTYZ-xTdrp9PM_dw6WEVa8oK5mg_5yyHFIjso4dHyw4Oosp-PSVg-LV6NZaC3Ms2dmyGTlSveBLY-_ZB8-SI3CeEmLyHSgCB12BMXut_VwE01TrULULL7ofxQA8vbCRX3AH54hxoknwVYm0dTeLdIGTi9ykQ_g_x-HZs9JgUcEzc1TUFRZLjPK7lFV0Tc8nPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=dXDTusq-Qd0brX6sZLbWJFhgc5tcO47usfFjkWGgBdZyzG5KBqakx-s2knCQfmqihaKj6frAeZIWhXUpG8k6EyU8XcRD2ksKxOz1kYXS8Ex6Swe_ZvuubAelHRVDqD9Gk6PL-B0VNOphX6B2dbiOuxTYZ-xTdrp9PM_dw6WEVa8oK5mg_5yyHFIjso4dHyw4Oosp-PSVg-LV6NZaC3Ms2dmyGTlSveBLY-_ZB8-SI3CeEmLyHSgCB12BMXut_VwE01TrULULL7ofxQA8vbCRX3AH54hxoknwVYm0dTeLdIGTi9ykQ_g_x-HZs9JgUcEzc1TUFRZLjPK7lFV0Tc8nPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی مملکت یه سری کارگاه آموزشی گذاشتن و به افراد بالای 60 سال آموزش میدن که چطوری اسنپ بگیرن.
هزینه شرکت تو این کارگاه بین ۱ـ۲ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71572" target="_blank">📅 16:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71571">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=bPwdibaAvNiYFaohcekt05GzzBF1wvdMIq697dfrSngz0UzTrsNTUXygS7DjU7JoMKiyT8XTGb_88V2Jt_4ijeeGcBvhzYhSFDh0n2f5RR1WQfHWcPbUVSM6lmGkWmUuinbDhPcTTPC2Ks7vOUD3PdKt8O9b9_xSM-xHxJiINrdRNvXnNKJ_aI8EJPqKfVKA2VA2f5pgpQrqUCHETPMS91yvWSPjnJUynsQc3lF7BZm0oUxFWnpxnkUnM83w_BVRmN_OM75Lh50X7044yAB88S303H21hCWboJN3lKUJFGgMEHVdV0wU_csCn5FDE6BIFwjmey08niDj5z8tavljyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=bPwdibaAvNiYFaohcekt05GzzBF1wvdMIq697dfrSngz0UzTrsNTUXygS7DjU7JoMKiyT8XTGb_88V2Jt_4ijeeGcBvhzYhSFDh0n2f5RR1WQfHWcPbUVSM6lmGkWmUuinbDhPcTTPC2Ks7vOUD3PdKt8O9b9_xSM-xHxJiINrdRNvXnNKJ_aI8EJPqKfVKA2VA2f5pgpQrqUCHETPMS91yvWSPjnJUynsQc3lF7BZm0oUxFWnpxnkUnM83w_BVRmN_OM75Lh50X7044yAB88S303H21hCWboJN3lKUJFGgMEHVdV0wU_csCn5FDE6BIFwjmey08niDj5z8tavljyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیویی جالب از یک پهپاد اوکراینی که به سمت یک کشتی روسی در حال حرکته و یه بالگرد روسی تلاش می‌کنه اونو بزنه ولی، این پهباد در نهایت خودشو به کشتی میرسونه و منفجرش میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71571" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71570">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=cJeaBE1UAfPtOISaFj42zrvMzhdYrfwMbOhHlkkrFXXfukRkduHNj6u4Kr5lTsL0m9eWxNYBFkWsbDxGJPbH_ikwBksqU72WPjVzeLHIjCiMpFE3oEdCAlLFruG-M-BA3A2HIPVMuVCv8NpxQ_ASqk2ozTjvvWd8zPhbErhsdRAm2N7ffcH0w65Y6aWxCFieJzapCofiyZ4jbJWvpkIeOPzqZbnwhQMvyw71d7GuViXOS7fk2763YjI3xLKu4Fem4MJP_09SVhh_m1c8AouCh4PUfc5kRu9cs-4mMwRvycy98WjqLtl1_I1arArOvKPc7nYm4EBvPyOiWUT0HZGnVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=cJeaBE1UAfPtOISaFj42zrvMzhdYrfwMbOhHlkkrFXXfukRkduHNj6u4Kr5lTsL0m9eWxNYBFkWsbDxGJPbH_ikwBksqU72WPjVzeLHIjCiMpFE3oEdCAlLFruG-M-BA3A2HIPVMuVCv8NpxQ_ASqk2ozTjvvWd8zPhbErhsdRAm2N7ffcH0w65Y6aWxCFieJzapCofiyZ4jbJWvpkIeOPzqZbnwhQMvyw71d7GuViXOS7fk2763YjI3xLKu4Fem4MJP_09SVhh_m1c8AouCh4PUfc5kRu9cs-4mMwRvycy98WjqLtl1_I1arArOvKPc7nYm4EBvPyOiWUT0HZGnVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری صداوسیما:
از جنگ تحمیلی دوم حدود ۱۵ ماه اینا هست میگذره دیگه
مقامات صهیونیستی و امریکایی پر تکرار گفته ان که با حمله به ایران ظهور مهدی موعود رو به عقب انداختیم
دلیل اصلی بمباران تاسیسات هسته‌ای ایران به عقب انداختن ظهور بود
اونا نگاهشون آخرالزمانی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71570" target="_blank">📅 15:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71569">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4RwNb4tksCjlPNLVROpdIqTuiIA6cf1k_tLThYK5E8_sM5D0_2MLGEdDeKeZAFt8bLp2SiiUYAx54-Ft1RSeQsSkjseYafhF-ND4eUAcrMXWskadUfhCA6tsiOqqi8P_4lsamjrBgKv3ISvQnBy7priTF2IBLDdxKu_Ldee0xPU4UQUTWD48diVgMH_xIGSaVxexk6URt7X61jZGqV8e0feqfTV_QDhLG6-dUhKeqaEzpvz3rnWJ9Wa2zXZRxJrKu_JxvN9BaYnEzRtFNHCxzbYvjPcQbH1jOxMf93-IfHD-Ygz1CXsQxQkIa0NONGIX9KkbEfJC8QaNB_YXYjvfV94s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4RwNb4tksCjlPNLVROpdIqTuiIA6cf1k_tLThYK5E8_sM5D0_2MLGEdDeKeZAFt8bLp2SiiUYAx54-Ft1RSeQsSkjseYafhF-ND4eUAcrMXWskadUfhCA6tsiOqqi8P_4lsamjrBgKv3ISvQnBy7priTF2IBLDdxKu_Ldee0xPU4UQUTWD48diVgMH_xIGSaVxexk6URt7X61jZGqV8e0feqfTV_QDhLG6-dUhKeqaEzpvz3rnWJ9Wa2zXZRxJrKu_JxvN9BaYnEzRtFNHCxzbYvjPcQbH1jOxMf93-IfHD-Ygz1CXsQxQkIa0NONGIX9KkbEfJC8QaNB_YXYjvfV94s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇾🇪
تصاویر بسیج قبایل حوثی، ستون‌های طویلی از خودروهای تویوتا (تکنیکال) مجهز به سلاح را در بیابان به نمایش می‌گذارد؛ تصویری که نماد کلاسیک جنگ یمن است.
قبایل «بنی‌حشیش» برای پیشروی به سوی «مأرب» — آخرین پایگاه عمده دولت در شمال — اعلام آمادگی کرده‌اند.
وانت‌های تویوتا مجهز به سلاح، همچنان ستون فقرات نیروی زمینی حوثی‌ها را تشکیل می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71569" target="_blank">📅 14:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71568">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jajjJvNhAUD2uL3p6nKbr9643BHeYAw-EKBNnjTNke3wVSGJZH9Hxa6Tev3qr_q7YWnUCr6f5biyYPTb1GgqNNjAzNFq72fJGZ7rbP9J4mnTcjd61YV9bJNDePeQiEQHiuJzuXQPflQrB5THSWQWttW_dXllInodZKoU7N4hE82M8QBm8q7I5UiCXhhpjNG1PCA5cfCy8cCAs5BGLYoiKPZRCTJYQV3COyel52-K4YVJplKhMA0gIjSFXzla7fiTR4fJ_QCONCkeKN0kqwJtuw_ukJFDllAWu51VoQEeukPigM93dLPJQOR5EJytclJnHGW9S5Ako98GQpNBslSGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس: محمد بن سلمان، ولیعهد عربستان سعودی، روز پنج‌شنبه دو بار با دونالد ترامپ، رئیس‌جمهور آمریکا، تماس گرفت و از ایالات متحده خواست تا هم‌زمان با پیشروی حوثی‌ها به سوی یک نقطه راهبردی و حیاتی در دریای سرخ، به آن‌ها حمله کند.
ترامپ این درخواست را نپذیرفت و مقامات آمریکایی اعلام کردند که در حال حاضر هیچ برنامه‌ای برای مداخله مستقیم علیه حوثی‌ها وجود ندارد.
دریاسالار کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، نیز روز پنج‌شنبه برای هماهنگی‌های اضطراری به ریاض سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71568" target="_blank">📅 14:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71567">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=O3U2tnwCYCqhCp9AFeZWQLxJxELkK42DWMAhXXC52BtwDGeBgcIZpNv6LckPlcybiduUyI_X1QNsKVGeLrUYRdXxGNImHucJ1PNaybWYhZBGDHAN4KqkMdeuISDdgeKy46PghXwxT5owKjWyTp87jnpFPcUgl4WXGsV12NmYy5quZ01XuKcRhbXpK0hXBPB0IpqQZSMHim0bCThVVL46fnOUCoJYvRy8TWiwHjgZnFFl3P6xAnj2glDO7eHTRFkMp-lXhyfzB1UmXuUkkfWGDXckln0ypumlxseQVr6F39tx--Grhido2VlrinC-Hw-8qfTrPcjn2QEkEbduaJxrlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=O3U2tnwCYCqhCp9AFeZWQLxJxELkK42DWMAhXXC52BtwDGeBgcIZpNv6LckPlcybiduUyI_X1QNsKVGeLrUYRdXxGNImHucJ1PNaybWYhZBGDHAN4KqkMdeuISDdgeKy46PghXwxT5owKjWyTp87jnpFPcUgl4WXGsV12NmYy5quZ01XuKcRhbXpK0hXBPB0IpqQZSMHim0bCThVVL46fnOUCoJYvRy8TWiwHjgZnFFl3P6xAnj2glDO7eHTRFkMp-lXhyfzB1UmXuUkkfWGDXckln0ypumlxseQVr6F39tx--Grhido2VlrinC-Hw-8qfTrPcjn2QEkEbduaJxrlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کنعانی مقدم:
اگر رهبری اجازه دهند، ظرف ۲۴ ساعت از سلاح هسته‌ای استفاده خواهیم کرد
خرید فیوز هسته‌ای از کره شمالی، کار خیلی ساده‌ای است و ۵۰ تا فیوز می‌توانیم بخریم
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71567" target="_blank">📅 13:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71566">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=ETBFWcwXfef8AfKEnRREiwIJeAkhwzUoE8O1i_dO25Gx4cMIFN0yvtPVg7ZAR5FQFbu7m6bV5IuIg2gQXUM8dPVOdg8BkKdBOXz18DkgStVQZVK-5fOIlzygGUrfeVjsSE0nV5XApADwsjUwwVU-v6kJkQHM7m-tCQ0Bv0_NxNWEX2a5zubv9EFvYeXAHiYOenYcdoC6gQa0_pmp8-QgVoIJxy9a4VMPfOV_UnfSqmgCopmobbRseZ2XkPyGfEoraG-LWi3k-aDZsWA4RxC7Or09I1q-GgtDJgYgQsGRieCZFbKJHnrQaUiyiovnqkSl15L8MCaaPzKRGlSEhxC8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=ETBFWcwXfef8AfKEnRREiwIJeAkhwzUoE8O1i_dO25Gx4cMIFN0yvtPVg7ZAR5FQFbu7m6bV5IuIg2gQXUM8dPVOdg8BkKdBOXz18DkgStVQZVK-5fOIlzygGUrfeVjsSE0nV5XApADwsjUwwVU-v6kJkQHM7m-tCQ0Bv0_NxNWEX2a5zubv9EFvYeXAHiYOenYcdoC6gQa0_pmp8-QgVoIJxy9a4VMPfOV_UnfSqmgCopmobbRseZ2XkPyGfEoraG-LWi3k-aDZsWA4RxC7Or09I1q-GgtDJgYgQsGRieCZFbKJHnrQaUiyiovnqkSl15L8MCaaPzKRGlSEhxC8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎯
ویدیویی از هدف قرار گرفتن نیروهای انصارالله توسط نیروی اسنایپر مورد حمایت عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71566" target="_blank">📅 13:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71565">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=QnR3-xHFdhem95WczSS9JxF9u1iiSJZlybldAtu9lGAfHnNpNwWNG7-uAWXThxmBZ5Ry-p1qnh_24RpcB-hPtH97OMzEYX_z6i66o6Yqz0rLk2DB8CqEMUDP7virLMV1Pt57P24PBcuQCzP0DwVOcI36H3Du7E45nQUsxBd81olvAan-ch3piqBwUSu1oSWjA1VfvLX61IfaewvZQuqgwvhCzQg7dH-3gGLpkX5pbxP47prjn6Tf21brSKN93yPfKnZSaD2Mleu11cDdX32gY3qlpIMk1VmX6EhOsYufF8U059D_zRXeBH_9qwl3Su7R1EITJa44Gla4lLS8Z5zlkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=QnR3-xHFdhem95WczSS9JxF9u1iiSJZlybldAtu9lGAfHnNpNwWNG7-uAWXThxmBZ5Ry-p1qnh_24RpcB-hPtH97OMzEYX_z6i66o6Yqz0rLk2DB8CqEMUDP7virLMV1Pt57P24PBcuQCzP0DwVOcI36H3Du7E45nQUsxBd81olvAan-ch3piqBwUSu1oSWjA1VfvLX61IfaewvZQuqgwvhCzQg7dH-3gGLpkX5pbxP47prjn6Tf21brSKN93yPfKnZSaD2Mleu11cDdX32gY3qlpIMk1VmX6EhOsYufF8U059D_zRXeBH_9qwl3Su7R1EITJa44Gla4lLS8Z5zlkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
این رهبران جدید و رهبران واقعی که رئیس‌جمهور ترامپ از آن‌ها صحبت می‌کند، چه کسانی هستند؟
🇮🇷
پزشکیان:
به گمانم باید این را از خود او پرسید، چرا که هر روز حرف متفاوتی می‌زند.
یک روز می‌خواهد ایران را نابود کند و روز دیگر می‌گوید ما دوست ایران هستیم؛ یک روز می‌گوید ما را به رسمیت می‌شناسد و روز دیگر می‌گوید ما را قبول ندارد.
بنابراین، ما مطمئن نیستیم که باید کدام اظهارنظر را بپذیریم و بر اساس کدام‌یک عمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71565" target="_blank">📅 12:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71564">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71564" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71563">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzeK4GsMzypogit-cewVzah1A2Qx7U8u_ApifIu_YnOnABnWy0V5RY4H1soBnyMkmbQe0RxiQgfeUOqkAcTWZn7GUFmww1gRWxHG5B-_rEct8ka5XJR7FWoxms8MSSIqkQebPY37NBidB0St82S0zSMDCxU6r-lYpHaBS0SrCnZWV9-VyWWbAEBteLkQvmIVk75TCzkV50WgNdmuzAXdhBRIyN9y1_q1uA7PpIvs12tiRalL9_MiAvtQATBMduNR1UB3GiNEGTauc9YRt-ZsoB8ZaCfNiHMRuVL1F02mTGCwDyqLkq3HfJxt6_QVIq8qHgJ1iKVToMqUiBli7X47rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد بزرگ منچستر در راه است!
نبرد هیجان انگیز
⚽️
منچستریونایتد
🆚
منچسترسیتی
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ دربی اخیر منچستر:
⚽️
منچستریونایتد: ۲ برد، ۲ تساوی، ۱ شکست و ۵ گل زده
⚽️
منچسترسیتی: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71563" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71562">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqnm0y86goGwE925H-R-m5H09pF31kcpfnnr6RVv0TH7CDEK7hw8FyTU2nKmL8Wxi9kWO-TKCK6KunYuAjZfQvJc7emzUOifFbpUbfdvigLMpklvh6vQ4Z_zpRUpqbptVUMF3HClhCAgqWHfalerIEVSE-sIP48QV594t0iIzW9huazwHC_0jBkoxxyOFSi1Lc5BGg7LTwg9rubvTY4LEv4u4VwofSbMT2GCblamPAkMuZxbPAuscP40FyZz3MQTqbG3CMEqv_KNS-8dP81OHGEOW4ZYKoF91EzuEKrcoCeyjT6P2We64KiIdMFah2D2jcRQPGpsOqeaSX426oSXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
روز یکشنبه در گزارشی اعلام کرد که بر اثر اصابت یک پرتابه ناشناس به شناوری در حال عبور از تنگه هرمز، در آن کشتی آتش‌سوزی رخ داده است.
این سازمان اعلام کرد که مقامات محلی در حال کمک به تخلیه خدمه کشتی هستند. در این گزارش، نام شناور یا اطلاعاتی درباره تلفات، خسارات و یا پیامدهای احتمالی زیست‌محیطی آن ذکر نشده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71562" target="_blank">📅 11:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71561">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
🇯🇴
ویدئویی از پرتاب انبوه موشک‌های رهگیر «پاتریوت PAC-3» از پایگاه هوایی «موفق سلطی» در اردن در سه روز گذشته، برای مقابله با موشک‌های بالستیک ورودی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71561" target="_blank">📅 11:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71560">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=votXcOQZHlH-hlj0NWEObCp9MZ_F9If9AEe_0BE5K62jAWnVoz-fPN5w8IZ6J6vgelxf-nRVvRkJwuxvv0X-qMwYKN2FKX4uhqluUsh0j8Yao8F_Ip89C6LEk_GbnTVpPJwCxAGM2Ubdreva2H0vOpadYWUpWuKZNxQHcVWUWwztJBlUf17nkdnpyp5TYibf5ZExip7q4c2oXAcYCMtDXNNsGQ096e50mUFn2F-tRHh5Lnws68WQJZoj4F_6IHGmKfEx7_r1Rj87E_T3gPl52yIxZhPXLYZXtpkmtvAMCBpNHAh68R8f_ylKLiZDd37y_bFNGrkJ-4D7J0u-nrKe1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=votXcOQZHlH-hlj0NWEObCp9MZ_F9If9AEe_0BE5K62jAWnVoz-fPN5w8IZ6J6vgelxf-nRVvRkJwuxvv0X-qMwYKN2FKX4uhqluUsh0j8Yao8F_Ip89C6LEk_GbnTVpPJwCxAGM2Ubdreva2H0vOpadYWUpWuKZNxQHcVWUWwztJBlUf17nkdnpyp5TYibf5ZExip7q4c2oXAcYCMtDXNNsGQ096e50mUFn2F-tRHh5Lnws68WQJZoj4F_6IHGmKfEx7_r1Rj87E_T3gPl52yIxZhPXLYZXtpkmtvAMCBpNHAh68R8f_ylKLiZDd37y_bFNGrkJ-4D7J0u-nrKe1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نظرات متناقض هادی چوپان درباره هانی رامبد:
بعد از قهرمانی
بعد از جدایی
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71560" target="_blank">📅 11:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71559">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097559287c.mp4?token=R-1YHaMWJsoeSCpSQOH-FSVPIVCMpBFAhiBfBfSiuQwvS_Z0Jk2ovguyea0DU8jILeYq7k7ut9qwpcdaomPZ1CD_LGv1I4WCdbZQCvXhfVXGlTEjHMgIkOLTLuV9kOdBb7KDztHLFYSkg6IP-RJXiVk6djYXJ4HL3GXIJM3Aa8sxAEs5x_ZxcLencr88qY2W3ru3zNTHC6m4GipiQbnN5aD6UmzAxRmOu13RojeRtQcHkjsn7f2PNOmrOFE6rQDueKLHASSRO9Nd2k7TtShfq9YsvCJG7ZnLJcX09yHYjNQJ5m39SCZT4sifsn6GoxhC5_CjKIX87kJgP7oKiGlgqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097559287c.mp4?token=R-1YHaMWJsoeSCpSQOH-FSVPIVCMpBFAhiBfBfSiuQwvS_Z0Jk2ovguyea0DU8jILeYq7k7ut9qwpcdaomPZ1CD_LGv1I4WCdbZQCvXhfVXGlTEjHMgIkOLTLuV9kOdBb7KDztHLFYSkg6IP-RJXiVk6djYXJ4HL3GXIJM3Aa8sxAEs5x_ZxcLencr88qY2W3ru3zNTHC6m4GipiQbnN5aD6UmzAxRmOu13RojeRtQcHkjsn7f2PNOmrOFE6rQDueKLHASSRO9Nd2k7TtShfq9YsvCJG7ZnLJcX09yHYjNQJ5m39SCZT4sifsn6GoxhC5_CjKIX87kJgP7oKiGlgqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
تلاش ابی برای بوسیدن دست یکی از بازیگران برنامه عشق ابدی که ویدئوش به شدت در حال وایرال شدنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71559" target="_blank">📅 10:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71558">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=hYPBafyd6MAgrBtpBeTCg263Cc-5OJD4t5ooo0Qgrc9dqwougkD_KcU6-Q0GcgvEWfqnhxLPDngntRHQfaCD6chkk7TPRMHou6wuz7TzMmS2lMCSLOA3pZ7fPN_dFa5kIaiZKVvDW5xPjQakFKjUmcAXHO9LdI6cmrPLJHSEp0ltj20uaaL9UStgjmrDMJgXwPLvTngfoB80axNePehqLAY13cQ7pq_4rDzX824lArN6l6sUjzRTGWbCHV4HwDAJi1Y4htc-lgZHrWQUlt_qPBj9ko_nko6lj4Cl6wQmy5HEtE3IInuxqkVmWtIXFU2RWQD2MVjCOY_eqYBzqpkEqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=hYPBafyd6MAgrBtpBeTCg263Cc-5OJD4t5ooo0Qgrc9dqwougkD_KcU6-Q0GcgvEWfqnhxLPDngntRHQfaCD6chkk7TPRMHou6wuz7TzMmS2lMCSLOA3pZ7fPN_dFa5kIaiZKVvDW5xPjQakFKjUmcAXHO9LdI6cmrPLJHSEp0ltj20uaaL9UStgjmrDMJgXwPLvTngfoB80axNePehqLAY13cQ7pq_4rDzX824lArN6l6sUjzRTGWbCHV4HwDAJi1Y4htc-lgZHrWQUlt_qPBj9ko_nko6lj4Cl6wQmy5HEtE3IInuxqkVmWtIXFU2RWQD2MVjCOY_eqYBzqpkEqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده از 9 اسفند - روز شروع جنگ و بمباران تهران و واکنش  دانش‌آموزانی که خرکیف شدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71558" target="_blank">📅 09:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71557">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇮🇷
امیر تیموری فرماندار شهرستان قشم:
یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب دراز جزیره قشم مورد اصابت قرار گرفته است.
در این حادثه  یک نفر شهید  و سه نفر مجروح شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71557" target="_blank">📅 09:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71556">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaZ7rf0tcIq_0BzYI705yBWANj7myja6L-v5EUR7rX_gOyVWqt1hzZdYj0hK91zrIomkyUgj8PTONUtFiMvXCIkelOcccunhFdLVBChBvJF2_BZCv17onxNUuI21gWKe2yYkwN-j4xN3vLArToPjB0o54q2PhNGUgy8XA-K1rM11sDekC-UVCiP0_gDyQqyIZcNR0-CgzZxwYEA4P6YUxp7HMXo8E2CJc4GLyF4uhatSvfUvXQC1bNsA1Xcy7w5_vEE8o6fmYsVeH3FaZ1RaAFm-F_oM13cT_MSoP8a4h250NrBn5_2A1DV7OQfOz1E7_7zKYvD_zmkO8i7F8e3Rpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇮🇷
📰
وال استریت ژورنال:
مقامات آمریکایی می‌گویند ایران پیش از حمله موشکی بالستیک ۱۷ ژوئیه به پایگاه هوایی «موفق سلطی» در اردن — که منجر به کشته شدن سه سرباز آمریکایی و زخمی شدن چهار تن دیگر شد — تصاویر ماهواره‌ای با وضوح بالا از نهادهای چینی دریافت کرده بود.
این مقامات معتقدند که تصاویر مذکور با این حمله مرتبط بوده و احتمالاً به ایران در شناسایی دقیق‌تر اهداف ارزشمند کمک کرده است.
آن‌ها دولت چین را به مشارکت مستقیم در این حمله متهم نکرده‌اند و هویت نهادهای چینیِ دخیل در این ماجرا نیز مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71556" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71555">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی TREXBET !   فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛ اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی، Promo Code یک‌دلاری رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی! …</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71555" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71554">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBxOQk6W_mKOJsAmj81Yr6XppRvBBGwHAzU7B0019foeyxQH3KOcThpz_iMlySHH_S2P_KRTBitOCNxmCKr4ofX0e5tsrP1IfrkVlKr202LOiOz7aEYrlK4S_JXryLqHjpWYpKk18R0FGwvrbDPrjpUe7mtDYZF_BXhTY4rZSIGwd27tV0CaoM57PDapK5voV_d8tz9nIHbAjHXqzmcld6fH0ZX912sk4oqO5T-4X5t5YdfSA0d8qfQN6Os-N-pIi1wCkUYAy1XTHt1IkyVKPoQWmYj2N6wgzUu26H_lmLdOFtqwz7ZLk6VB5T2bCiq70-99poT09o25AqDduO6FsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی
TREXBET
!
فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛
اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی،
Promo Code یک‌دلاری
رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی!
⏰
چالش اول → 18:30
⏰
چالش دوم → 20:00
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71554" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71553">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=ZwRo2V2_Osf4K9_skEiZSnadiCFGS0QwMl5CQz-d05zwklo6v3yg2GIaiuxFwKo9H2HJ0ppA1spTK1tu9pnG-A2VtEJ_sWi35GclsGT_5L3e2n7-L6tCR8wPKgBwi87ZA_9RLLNEKRMjysQIN5TH0gVbUhYk-sAarwdstWeaT5jw_bFGgEoCzaHmIo9ykdeLcb9kjpivBCu92lXYSzmiIUxtuiVGoFA8sFG6hLt--T5yyQxATgcY39XkKG_zsjJhpqQknPCUrkS40inI9pyK03NLvhebtPSJIcVp6yHmxA-GP48vVoPqd9-yXmc4fjqbMdcTPf6NiEyCb6k9_LnLCxGyFRJG7HGxZPLGb3fLTuSQdGzzWeKVxG1wAl0ywMy_NC_KyVAjCBza7j-sh15erdJbveJLzKUl7xpbAU8P4HOsbBcsG7P9KUMGew9mQzR9WAxnSNqLIFEqDTreIyGC2s2bsDfbFhBC607qeYeg3XVaJtKz0rNzEMH9Ww82KwcQz5O8Y98_beKZ3DlQwniSy4LtFQK0fnPu3R27ePTzvNHX-5E1cOX6Ke54rAgQMepxxkeWD8YaPTyUteVaborkxHirfG00AKhEKrJ13oRwevGboal0VQrPqxIUHVJ_bvW8HPO-QOf6T-v9CdUehHFhrt8TkyzDbYTG453P4bx170A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=ZwRo2V2_Osf4K9_skEiZSnadiCFGS0QwMl5CQz-d05zwklo6v3yg2GIaiuxFwKo9H2HJ0ppA1spTK1tu9pnG-A2VtEJ_sWi35GclsGT_5L3e2n7-L6tCR8wPKgBwi87ZA_9RLLNEKRMjysQIN5TH0gVbUhYk-sAarwdstWeaT5jw_bFGgEoCzaHmIo9ykdeLcb9kjpivBCu92lXYSzmiIUxtuiVGoFA8sFG6hLt--T5yyQxATgcY39XkKG_zsjJhpqQknPCUrkS40inI9pyK03NLvhebtPSJIcVp6yHmxA-GP48vVoPqd9-yXmc4fjqbMdcTPf6NiEyCb6k9_LnLCxGyFRJG7HGxZPLGb3fLTuSQdGzzWeKVxG1wAl0ywMy_NC_KyVAjCBza7j-sh15erdJbveJLzKUl7xpbAU8P4HOsbBcsG7P9KUMGew9mQzR9WAxnSNqLIFEqDTreIyGC2s2bsDfbFhBC607qeYeg3XVaJtKz0rNzEMH9Ww82KwcQz5O8Y98_beKZ3DlQwniSy4LtFQK0fnPu3R27ePTzvNHX-5E1cOX6Ke54rAgQMepxxkeWD8YaPTyUteVaborkxHirfG00AKhEKrJ13oRwevGboal0VQrPqxIUHVJ_bvW8HPO-QOf6T-v9CdUehHFhrt8TkyzDbYTG453P4bx170A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🟥
گزارش فاکس‌نیوز:
جنگنده‌ها از ناو «یو‌اس‌اس جورج واشنگتن» (USS George Washington) در حال برخاستن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71553" target="_blank">📅 01:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71552">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QERMzBQ6VssKelzMWQ4wDZOmEX36UsuBzA18lRtjZrr75HMONwDXc1BkBZCVt9L3QFzotCVSH1K-hT1omkYX-4YiC4mwfUGDDT7ZnHa9VRqNzf98ju3_yS6Pc8et9CMStc8hZmABnSSlsad0yA4pS0EZuNzS9MDEsbt-8pQs3OO4NPfFU4zoS2NDo78bD3Xc18VHGbqre9B6TU-vQkB5ZaWZ_jQrNOenZec4PUIa7SnKStlY4Lg-fiVIdevSISW-gPjWy7ek0s40XxoTpgl_FdKc2TdrFQWhqD3fE6QKX4bG4Ue1Bu4JDFjOvaTeYTpKT0GuduK48ve9gYylVjZkMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛کانال۱۴ اسرائیل:ایران برای خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) و آزمایش بمب هسته‌ای آماده می‌شود.
حاجی‌دلیگانی، نماینده مجلس، از آماده بودن طرحی با قید سه فوریت خبر داد و افزود: «باید هرچه سریع‌تر آزمایش‌های لازم برای سلاح هسته‌ای را انجام دهیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71552" target="_blank">📅 00:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71549">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt5NPbVWGkuOHPjpt60irC3iJbXTaS-ne_2qL0ZnNRvqvTUoVHktc3iUQNw0mRJzcyi40Bk3xLok5fj1P7al5F_oEpbypsl8W6InJtRkYDOaDpqNvbW3c3gx8L7XnMSVuGxA_CahHNSFWUo6FAWp-qmKHiJptt3Ng6Td7ZvBvB14ja5KE3R8ojWg50q6Zz0PFgEOYn9-EuVf15JYqqRA76zaSjEC3IhJeMqgLZ3Pmv9O_n2kMs_WmvQ8IBCsEA2DsBncXotu0vIcZikdOEBysjSwcfYHz2aNtDlim3veNV6UUtQVK5ISSHaqF93E2WbtqpQ-rMWTmXSQv9xROQWJsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=BGFPs2mbAbwdB3DGll11KBCIYU98Dg19fj-kNTdSv5H-Vd81unNIwjio34P2RD29bwf0dmqp4DK06oZzp9gjbPcrpIet-6yXzlqhWSl1VzhR-b1CzwFzjwfWqXGa1j98RW8Jx0rZxYb6jCmxSmA4n3JGlOeXyrMAspon44h81TyWKAetbZSCrDgRj64bal_4u2Jv4DNAuEXn5-BvuX7H8Aqfv3bhPlxawvSealE7VA2r6Vi1IxMqkFDWtXWTOjsdmdVy5kv4nK1LmUt8Cn57Zta_rBHLpp4qWmWxmRD21S4SSc7_SnB1P2Z9vOByb7j9aDPMs75fr0K10l7bN7t8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=BGFPs2mbAbwdB3DGll11KBCIYU98Dg19fj-kNTdSv5H-Vd81unNIwjio34P2RD29bwf0dmqp4DK06oZzp9gjbPcrpIet-6yXzlqhWSl1VzhR-b1CzwFzjwfWqXGa1j98RW8Jx0rZxYb6jCmxSmA4n3JGlOeXyrMAspon44h81TyWKAetbZSCrDgRj64bal_4u2Jv4DNAuEXn5-BvuX7H8Aqfv3bhPlxawvSealE7VA2r6Vi1IxMqkFDWtXWTOjsdmdVy5kv4nK1LmUt8Cn57Zta_rBHLpp4qWmWxmRD21S4SSc7_SnB1P2Z9vOByb7j9aDPMs75fr0K10l7bN7t8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
درحالی‌که شرکت اپل ایران رو تحریم کرده، قمی‌ها طی یه حرکت عجیب، همزمان با مراسم معرفی محصولات جدید اپل، خودشون هم به‌صورت جداگانه یه ایونت برگزار کردن و از آیفون‌های جدید این شرکت رونمایی کردن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71549" target="_blank">📅 23:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71548">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=J6qxGWrakUIv4670oK69gu_dm0OSWy7fmu80PrSgWd_9nD17divm8zquetibzeQf2jrDnTwlkwJ10yqlkIWTBCm5-nvluYuCSf0FteOoQtcR0H66cRjBSFdEUDPc9at-PvHmwsIhbRAQyJXyP4cN6bk_xFUxVV9LirYoZRCsRY_cYxrhGSW9BHJy__mZ8tzognTxt5Z2aziE04Ysx3fX55MmgccS6bB-XlLssOaQ6pdOtl_togr8vhXEzPWqD59RjUBgdWST-PFKawwZb7_-CC1idKjbGfzHodLUJGCUu3GY8fSAogNZj4Dxgt-VZ-x86QMdomsUroYXzIFdzO3ZCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=J6qxGWrakUIv4670oK69gu_dm0OSWy7fmu80PrSgWd_9nD17divm8zquetibzeQf2jrDnTwlkwJ10yqlkIWTBCm5-nvluYuCSf0FteOoQtcR0H66cRjBSFdEUDPc9at-PvHmwsIhbRAQyJXyP4cN6bk_xFUxVV9LirYoZRCsRY_cYxrhGSW9BHJy__mZ8tzognTxt5Z2aziE04Ysx3fX55MmgccS6bB-XlLssOaQ6pdOtl_togr8vhXEzPWqD59RjUBgdWST-PFKawwZb7_-CC1idKjbGfzHodLUJGCUu3GY8fSAogNZj4Dxgt-VZ-x86QMdomsUroYXzIFdzO3ZCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
لحظه‌ای که جورج دبلیو بوش خبر حمله به برج‌های دوقلو را دریافت می‌کند
جورج دبلیو بوش آن صبح در مدرسه ابتدایی Emma E. Booker در ساراسوتای فلوریدا بود و برای دانش‌آموزان کلاس دوم در یک برنامه کتاب‌خوانی حضور داشت.
نکته جالب این است که بلافاصله از جا بلند نشد و کلاس را ترک نکرد. چند لحظه در همان صندلی ماند و سعی کرد آرامش خود را حفظ کند تا دانش‌آموزان وحشت نکنند.
چهره‌اش به‌وضوح تغییر کرد و حالت شوک و نگرانی در آن دیده می‌شود. دانش‌آموزانی که آنجا بودند بعدها گفتند تغییر حالت چهره او را به‌خوبی به یاد دارند.
جالب‌تر اینکه او حدود هفت دقیقه دیگر در کلاس ماند و بعد از پایان بخش کوتاه کتاب‌خوانی، از کلاس خارج شد و در همان مدرسه برای خبرنگاران صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/71548" target="_blank">📅 23:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71547">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=Fob9RqR5HOzQtpt1K_abb2kyo-NjLiyyV3_Tfi4FWNGUEvQ0vlpSfzR2p5IgLhLOJJmaHUFXWj1sjCcZXH6jXNGHRTOUa2BoxiaKjeXgdyhKG_NqtUev9n4M_ls-klU4Xv9WKMTfl-rOVd3rBNzJejh05T-Tt6h0Zs3A8r3chpHHKdT9kpFr3wwKkGKolVYvYpyYSxPsouCFf9kakpn08PpiLJBCTRdRnNBj9L6QWRPwEeskUmY7KZGcuIhMyVaOe7agmXIYyRd24c79cNovXW96HS-ewo9FTlvJwoGOQtkAJ2QdkPxexf68G79Je7g5AzvuffcSTRjDmnIFbbXDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=Fob9RqR5HOzQtpt1K_abb2kyo-NjLiyyV3_Tfi4FWNGUEvQ0vlpSfzR2p5IgLhLOJJmaHUFXWj1sjCcZXH6jXNGHRTOUa2BoxiaKjeXgdyhKG_NqtUev9n4M_ls-klU4Xv9WKMTfl-rOVd3rBNzJejh05T-Tt6h0Zs3A8r3chpHHKdT9kpFr3wwKkGKolVYvYpyYSxPsouCFf9kakpn08PpiLJBCTRdRnNBj9L6QWRPwEeskUmY7KZGcuIhMyVaOe7agmXIYyRd24c79cNovXW96HS-ewo9FTlvJwoGOQtkAJ2QdkPxexf68G79Je7g5AzvuffcSTRjDmnIFbbXDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مشهد اردهالِ کاشان، از " نمادِ مشت گره کرده‌ی علی خامنه‌ای " رونمایی کردن ولی انقد بد ساخته بودنش که صدای طرفدارهای حکومت رو هم دراوردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71547" target="_blank">📅 22:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SIe49gpzUEpbxpmh5-9s70RCe5v_32lLmXUpGmU-A61hG4L_F1op_zuyYQhB-YUuPpOVxzZFJr2vEzDpw9QBGLcafXHQb-Nzw7SuYkk4qcXuWgXGsZFHrVqCGXoD408HVKEVRm1hwsAIE3zO5ybhYlwG-EP8N-u4R5IwaKVhjqem1KeqZ9DLr2UcBZWKVcIhxJzUnnNnF0xAnv1YNjkYcCmwn4YyIdfBkvQwNRTpiq7PFHRwoL3k3kAHEJd6OYgpVad1kZL2DZDZurOzMe7FYLYdltukO8fRUcso8LdvEChHeXF1nSy-9IOI1iB9NYobWD0AH2afJFDrQf7HcJjWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IV0tcDMOFooQrm6_1qzSAloXmqwwNAFDSTZJHvG_WLjMcKRnzZiB4Pr2Prnd_ON21HmVAsLBKOsE9nqdd21-TpFg6g9Fch8MDl-y1hKRf8Fbm0wjhYFk90LmIaBx8B1dJczQXRZ30Ow6TLQrGFnUX6ZxskLoO5-BQs7pXb4KrFZ1DTi_LgIjtSfTRk7cNlA9-1hhYj-6CdJwg_rhsHoZjfPjKDeLaID0Ro9WNouDrHlWs1HbCpVMc7r9M1aRswsmQSGn0ZahQ0ileBiVS6jv0_Q86mKFzXNNSoIreT39QBNlsPMS9w5XE3s8QwhxjHRURybwrB9hL9ZFIhcoIBF0Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HEG-Mdwc6C-ml-XmmNffw14JZMWAulyJN4JBIaaTLiqeob3SMHq9rSBjXOXoyzzo_6fOjxzu3_uWvAxhVDU8WBaP9mwSnQlqVBnk7x7VH5zGNkzrWlhwe0R9N-Tm-bd8dDw5pYv5ytVpGNlJsGg4XJEOLMr2JRAOESwaIyIHSfv2C1TGbc-ggHEEOTJ7ZQ2k89MgRHR5NujkFEnmJvHdLjuuytqWLe8lddpIjmx6NbtEeHiQhIDdFj00EhnA35o4pW-dFmF61VU3ozX6ClGCE3MhpJb8YrKuSDpABSdOt8HCAIv9CTv-X9lu28E7KAYAHR3VJtFkQ_BGkicDDOlBfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
کشتی‌ها و نفتکش‌های آسیب‌دیده ایرانی در خلیج فارس.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71544" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
شلیک یک موشک/پهباد به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71543" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfIigfh-BqRPofZH2xz1W54SJkCh__svd7fa_K60zFrKuK51W9nyjQiYX5fBWrKJ_WzqZYQki0bhmpZsLSiv-fjKFS0c_JIa_WPaq6Fms08l14aQhSlZlwu2kyFG_7ef1atk444bi75ZPowIU_oxHli8dHuGHOAdXjg1YI0vHTcR_MQkbzV4wtv0PwAt6i6-iFSJ7SKm1DD2r0KhA6o5Fj2sLRFVJr1t9pZxr_lf-vUAcT_vmWlRf0XJ8R4LnfbzSLDmzYxYz4RpUm1Q4zexc3YY0X9qtKPir_tv5I5BRUDgE_CrTMZ1_59aJltkNsWICb3FAx8J0syB99kzyzSSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
شعار جدید عرزشی‌ها برای حسن روحانی
😂
نهپاد: نفوذی هدایت پذیر از راه دور
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71542" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71540">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=kDb-nC-1CrQ4RzyXW0RUHf-RFUlaIMQSkM7b47JbGwjajrHgTTTXVRjZE8dmCn17g6fcSB_fG9aEFKnb_xYpIqywg6BthpQ_GyZK5XfgpXDNEvxlwYn0CzR1su7dJ3k3loizprXlt6YfewXpH-p9vOqBsT2iD06fnnHJE3S0t4m_ik2s_qefcMAqOXLSgWARi9PVbfo3nh08HGUj2Gt99VO_P2TB_c0ButTGHIsgybUJ3xluQjoip7ge_JbPIq-GYisPMbPokgpHXWjU-t59QJt83srQVsfnXFDleTZyKV2lpN_filAKPYEzhqIHlTGcYZyBOuKISoeCoEqFlfLbZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=kDb-nC-1CrQ4RzyXW0RUHf-RFUlaIMQSkM7b47JbGwjajrHgTTTXVRjZE8dmCn17g6fcSB_fG9aEFKnb_xYpIqywg6BthpQ_GyZK5XfgpXDNEvxlwYn0CzR1su7dJ3k3loizprXlt6YfewXpH-p9vOqBsT2iD06fnnHJE3S0t4m_ik2s_qefcMAqOXLSgWARi9PVbfo3nh08HGUj2Gt99VO_P2TB_c0ButTGHIsgybUJ3xluQjoip7ge_JbPIq-GYisPMbPokgpHXWjU-t59QJt83srQVsfnXFDleTZyKV2lpN_filAKPYEzhqIHlTGcYZyBOuKISoeCoEqFlfLbZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
حملات هوایی جنگنده‌های عربستان سعودی به استان البیضاء یمن
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71540" target="_blank">📅 20:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71539">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhK8yMQRJ6QRPwDpEaZwrCk9ZOJi0IV_AFLYp4O8UkOz0G-CkLf6p_Lx8gF9_wjH_Sr4eefLwnvXtXujUk-PMEoL-M4byb_rBh8hW1QczQZsDeL19yxgDAK3VS65dedDfHcwKSD2D0_UZkJGz6hlH7v6lpiWtzDCTrgVxqeBdUNfwJ3uQ4PwxtOGMJ8zxdqmcOftD1BPTSITJLIlNXu2Ld-kPz46nT12K7ePJux_9Y4ERPKZkEiNU_js7Lcn4Ye7GoYH0zFMsaLuu5K4Cto4Cz7JPCSoM6UL68otbx1_wPz4dhojioDmqGKAFvrQ-GWWAgeVZX-6b6xLUG1mepW4GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
مذاکره متوقف شده است چیزی وجود ندارد که میانجیگر داشته باشد.
عاصم منیر هم جمع بندی ندارد که اگر وارد جنگ یمن شد، بتواند پیروز شود و پرتابه‌ای سمت تاسیسات حیاتی پاکستان نرود
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71539" target="_blank">📅 19:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71538">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J52D8zBUnABgjOgRQwn1TgcNN7SZJ3UEFehREzGyupdXJ1CLevVOBFTdwHqvvd476Q5KelSO9tc2ff6v7V3i1y2kRDrJidsMB8gI-WvWzwHGiLpiNikDiWell59EOzQKDwdya47PptCAQcmpRK51nSRhJihTryQu3W3a4UoyFf7p-hy-SUUGCLnC4RSuDcoMrzEJ_LN-jhM-Fo1tBrdHll_R5myzWE7H8L-nguZ4vktmjf5iEMEVM8V8KvfW8YaL38b3VS5SV7C8bpEebr0LFnWla_KHi4YwbjumfAew14TD0qp7V8wH57VmTJ74a5z6vdR_orS08sUVfPsvK_zbDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره موسوم به «دیوار فولادی» علیه ایران توسط آمریکا در ۶۰ روز گذشته، نیروهای سنتکام مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
حتی یک کشتی هم بدون مجوز نیروهای آمریکایی از این محاصره عبور نکرده است و نظامیان آمریکایی همچنان با تمرکز کامل بر این مأموریت متمرکز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71538" target="_blank">📅 19:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71537">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇧🇭
❌
🇮🇷
بحرین اعلام کرد تا زمانی که روابط دیپلماتیک با ایران از سر گرفته نشود، در هیچ‌گونه نشستی با این کشور شرکت نخواهد کرد و بدین ترتیب پیشنهاد عمان برای برگزاری نشست وزرای کشورهای حوزه خلیج فارس و ایران پیرامون مسئله هرمز را رد کرد.
🗣️
بحرین چهار شرط تعیین کرد:
توقف حملات
پرداخت غرامت
احترام به حاکمیت
حل‌وفصل اختلافات از مجاری قانونی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71537" target="_blank">📅 19:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71533">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=D4QsW5V8p87Hty1mXWSihcfO9L2FWL2lblIozPspNJL480E3_lZUweuAasrBA8JhRXL6rmsze13gZ8WsAwvdiIDKP_3-08nd09c-ZlV5wRzwmRBZdFSV5LiWEZffQj75bku9z1K6JEVlVigYXbSj8csvCZmhFvkgCCOu26GoEK2H283sxAEG0c81xZf2SiS0P4MdJVm0Llm5iNcsAIcwwFdm2Atjo0oV4t7lPGd4MY8HnO0HZtFNQL8T-cU2aVpTYWzxhPQhy-EkfuFDIww_wCmC1qbJg8zJuJ4nvLuTvSLPCgjnWjzS_X8h11NKhckcZklKOh64toN8VpmPH6qo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=D4QsW5V8p87Hty1mXWSihcfO9L2FWL2lblIozPspNJL480E3_lZUweuAasrBA8JhRXL6rmsze13gZ8WsAwvdiIDKP_3-08nd09c-ZlV5wRzwmRBZdFSV5LiWEZffQj75bku9z1K6JEVlVigYXbSj8csvCZmhFvkgCCOu26GoEK2H283sxAEG0c81xZf2SiS0P4MdJVm0Llm5iNcsAIcwwFdm2Atjo0oV4t7lPGd4MY8HnO0HZtFNQL8T-cU2aVpTYWzxhPQhy-EkfuFDIww_wCmC1qbJg8zJuJ4nvLuTvSLPCgjnWjzS_X8h11NKhckcZklKOh64toN8VpmPH6qo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین  به اهدافی در چهار منطقه روسیه حمله کرد که حملات ساراتوف تایید شده‌ترین و چشمگیرترین آنها بود.
مرکز لجستیک عظیم اوزون در ساراتوف (با بیش از ۱۰۰۰۰۰ متر مربع مساحت، بیش از ۳۰ میلیون قلم کالا ذخیره شده، تا ۹۰۰ هزار سفارش در روز).
طبق گزارش‌ها، پالایشگاه نفت ساراتوف (روس‌نفت، که قبلاً بارها هدف قرار گرفته بود) نیز آتش گرفت.
در ولگوگراد، فرماندار تایید کرد که آوار به یک مرکز صنعتی و یک ساختمان آپارتمانی برخورد کرده است.
منابع اوکراینی می‌گویند که هدف صنعتی، پالایشگاه ولگوگراد لوک‌اویل بوده است.
برخی ادعا می‌کنند که از موشک‌های کروز در کنار پهپادها استفاده شده است.
انفجارهایی در انگلس (محل پایگاه بمب‌افکن‌های استراتژیک روسیه) گزارش شده است، اما هنوز هیچ اصابت تایید شده‌ای به فرودگاه وجود ندارد.
بنا به گزارش‌ها، منطقه بندری کاسپیسک/داغستان نیز هدف قرار گرفته است - پس از حمله تایید شده شب گذشته به بندر ماخاچکالا.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71533" target="_blank">📅 18:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71532">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71532" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71531">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aR_YEwPv-qI8-B_gjDzSHJZvotFB1oid9eC1kSnzyadSIIE6l4ViJZxY1UVk8FJmrRreZvBnKK9OtFWCUewp-QIDfqoCF8U7zRhQdbNC19s7wK79LZb0UJ2iuTTKzCBCGvDHCdvSjH9qmxVde_gFfxkZlef3-yCIPDdXVyTkJM19lcCgmMlp-CHCzI4RhWIT58zinKsnmO1Pznv5TVRBWbzLSqMvL2yUK_CfNJ08aaFgcpp9VPPFKs7uzdwBHo4DGtG1XMbQPGm1_nGYl8ixizMS_vFkHUMrwmHBk4pJhDMoQks54eiAnZO9I5fV9dBWtJOI_TvFNIyjCxWIliot_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71531" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71530">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554b629d89.mp4?token=JQFE7dWIGiDf_Lc7ufQfZuLtojd2cYAtUGkEGSAzCvKlMdjF4CWs8pvHS_AW0Aaejv_ZcxHsfgqc-AJGaZ75shH3xlGXd5O48ytbVYIAZRZPX-05497f3_D1IEUWh01rXHWo1aeKqqSTgf64v1_HvdKbTf5T4j-kXPMcowA2GakpPaRZ1B2VMIH6XFIMY0z6tqnKrFx6c6PEtilUjXpMOuqeXCLtCiPMLbsPukftT0jPf2QH5VV19s9rBtZz5HSDOPXzplhmjNinFfpV_IT0LiBZwz3RS-QdhAau-8X31u6DqgiZFsVdHx7nZ9dT6VMbYvdfV0qB10q41cSUFyq201zBCMR9Anp9RtVYNza6euXHL1RpLEUvIRab3HvWXtNQFo_7wOmAD9XwuniEJmPFlQseX65R1nHF4uYJo3e1Ygz3J0L1Z6JDFVIui8h0oXGLUEP6yDsuOgyvaTTETpWfcQkFtAanl1OtwRdRPZeehmCcNw12ZQAiWhWQk1pbw-Nq9sQb8DhSFHNvUEzHvaqOhKLuNLrGxmv1pcmGETwMFNYBYmzebyKuOby6K7BDMlQCxlyreskvwWT-1_OvqF7wYk3dVm2hYgF6tCBI391eKvX6LGxSCVfK2N_5p-h4NFptGKPd-sgHqkRiROm-DXIdIIItsKmonlorRbQ5Rwok-Hk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554b629d89.mp4?token=JQFE7dWIGiDf_Lc7ufQfZuLtojd2cYAtUGkEGSAzCvKlMdjF4CWs8pvHS_AW0Aaejv_ZcxHsfgqc-AJGaZ75shH3xlGXd5O48ytbVYIAZRZPX-05497f3_D1IEUWh01rXHWo1aeKqqSTgf64v1_HvdKbTf5T4j-kXPMcowA2GakpPaRZ1B2VMIH6XFIMY0z6tqnKrFx6c6PEtilUjXpMOuqeXCLtCiPMLbsPukftT0jPf2QH5VV19s9rBtZz5HSDOPXzplhmjNinFfpV_IT0LiBZwz3RS-QdhAau-8X31u6DqgiZFsVdHx7nZ9dT6VMbYvdfV0qB10q41cSUFyq201zBCMR9Anp9RtVYNza6euXHL1RpLEUvIRab3HvWXtNQFo_7wOmAD9XwuniEJmPFlQseX65R1nHF4uYJo3e1Ygz3J0L1Z6JDFVIui8h0oXGLUEP6yDsuOgyvaTTETpWfcQkFtAanl1OtwRdRPZeehmCcNw12ZQAiWhWQk1pbw-Nq9sQb8DhSFHNvUEzHvaqOhKLuNLrGxmv1pcmGETwMFNYBYmzebyKuOby6K7BDMlQCxlyreskvwWT-1_OvqF7wYk3dVm2hYgF6tCBI391eKvX6LGxSCVfK2N_5p-h4NFptGKPd-sgHqkRiROm-DXIdIIItsKmonlorRbQ5Rwok-Hk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پست جدید هیچکس (سروش لشگری ) توی اینستاگرام که وایرال شده؛
«هنو به یادتم»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71530" target="_blank">📅 18:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71528">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=gAP9jGwudsbKlHoSBPRT_QJYOr54pxR0HsWWw52c6c4Pig1J0VT5Ya3VIQDzx9wnWVXr0QW4l_UyeRHmN-Qrlvmk94dq40Z789WOrjxlfH-MAcY8-CH8arvy-Bxcb4NfeWKqcVkcG77TfyoKikIjQKXLONrQqLQnUp-kNSFMraAP573XaSUUeykUeGeBQXdkwu5tGg6UEjeTrke50W44hpa10L3taSS4KjvYoq4rfbL601eOspL7f9oLMwZAftgv6Pj5e4LAD-mGe5ZGKsCH72g6MtLwzql2tZsqtbjeyomHjlDNYr2ZalKZvQoAmietOAq4Jbtp8bu_RQx6GtnqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=gAP9jGwudsbKlHoSBPRT_QJYOr54pxR0HsWWw52c6c4Pig1J0VT5Ya3VIQDzx9wnWVXr0QW4l_UyeRHmN-Qrlvmk94dq40Z789WOrjxlfH-MAcY8-CH8arvy-Bxcb4NfeWKqcVkcG77TfyoKikIjQKXLONrQqLQnUp-kNSFMraAP573XaSUUeykUeGeBQXdkwu5tGg6UEjeTrke50W44hpa10L3taSS4KjvYoq4rfbL601eOspL7f9oLMwZAftgv6Pj5e4LAD-mGe5ZGKsCH72g6MtLwzql2tZsqtbjeyomHjlDNYr2ZalKZvQoAmietOAq4Jbtp8bu_RQx6GtnqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعار «مرگ بر روحانی» در تجمع شبانه عرزشی‌ها
:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71528" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71527">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=Q5ujL8fkBVJQ5UwMO3qCwdryLe6XBcnb4bDAISS1EctmQiSQydrMUNe4Vk11WcBBPekvI-UW7t5BRFcJ8SCBM4J6TTWLdWQDxl4mcFo4kYfSyMQzNsh29nGr-pwuetPrVadkNGcJwhgwJq08O7jaemgxm25sVah0Co2DVzHLTiel2StBSbeHgZSQOEdDqC19Bkcsofzfk-bWwWSAk3Ibb-WYm7KvL77T_89Q_U_ZFRWwk3twQrKDJi5hPHCEX6Pl3BPCtpmKutr9RvgrwLBU0M9_ZDvNUifvQA8XQKWmYWzQC5ZDsS0u4N6xdXtg_YPbz0fGElGoCdDzQe6v3PtK4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=Q5ujL8fkBVJQ5UwMO3qCwdryLe6XBcnb4bDAISS1EctmQiSQydrMUNe4Vk11WcBBPekvI-UW7t5BRFcJ8SCBM4J6TTWLdWQDxl4mcFo4kYfSyMQzNsh29nGr-pwuetPrVadkNGcJwhgwJq08O7jaemgxm25sVah0Co2DVzHLTiel2StBSbeHgZSQOEdDqC19Bkcsofzfk-bWwWSAk3Ibb-WYm7KvL77T_89Q_U_ZFRWwk3twQrKDJi5hPHCEX6Pl3BPCtpmKutr9RvgrwLBU0M9_ZDvNUifvQA8XQKWmYWzQC5ZDsS0u4N6xdXtg_YPbz0fGElGoCdDzQe6v3PtK4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
یک شهروند ایرانی با انتشار ویدیویی اعلام کرد ترکیه مرزش رو به روی ایرانیا بسته و اجازه عبور و مرور رو نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71527" target="_blank">📅 17:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71526">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=Cn5oAsi-y7ivLSHkvq5vUP-DGVftlku6SUItBKIcF7uvqHogs3bAb8-kQOBdPWkxBT17tSflG91HLPUY3Qlcr9I8p4GrDWBCAO2TIs02u7OCx3aeXFpFRckVFuw_G3IQ9hOw5fgyygIKFZyUcMzOHQK0ATlOXct6rsaUnb9qcxrBe3XktxSnjcoY_y2qWpJ9N0l3mJwypoTe4iJi74ID33J3zFgRr-L_CJs6BLgH2rDUILFzJsU2Ha94XgrNkfTMbklC8OqxuHzSpYaEI3ZghJWtDGKscbk2uaYw2gPyiVVHbqxYLMd0OJIEyhHDQfohdn6vGw7YtA0ZcRk1tngYmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=Cn5oAsi-y7ivLSHkvq5vUP-DGVftlku6SUItBKIcF7uvqHogs3bAb8-kQOBdPWkxBT17tSflG91HLPUY3Qlcr9I8p4GrDWBCAO2TIs02u7OCx3aeXFpFRckVFuw_G3IQ9hOw5fgyygIKFZyUcMzOHQK0ATlOXct6rsaUnb9qcxrBe3XktxSnjcoY_y2qWpJ9N0l3mJwypoTe4iJi74ID33J3zFgRr-L_CJs6BLgH2rDUILFzJsU2Ha94XgrNkfTMbklC8OqxuHzSpYaEI3ZghJWtDGKscbk2uaYw2gPyiVVHbqxYLMd0OJIEyhHDQfohdn6vGw7YtA0ZcRk1tngYmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از عشق و ابراز علاقه زیبای یه پیرمرد و پیرزن ایرانی توی پارک خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71526" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71525">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=GBNObE4dKCVYDVCkUzk2HDpsMV3a3FohQgOJEQtC2WR6u4CN6xxdozdTy7CO5mAFJ2vf5ZySYCekEiyxDXv0ajr5geeb91DKrChziUMUUUSQu-dDzoHGpj_M4_QQaRyyplZzGGv7z1PzVimwIsXltXPSioYm1TOvi3e1Xn0wyEAdNrVApJ_q03qI8szVfIcKoOkBHj72wQ13Cl4aZLzSmgO7usjuf9uEt-3hnD6pQkmkBlHJDTe6s-qWrAgAKEOqvVE6iZH1-jYtd8QoghmBAO-L7f0zcQAi6OUycJDBBBC_H7l-xBNtaxn0NoXAkj5OuuynFmTkrlKas_pn558E7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=GBNObE4dKCVYDVCkUzk2HDpsMV3a3FohQgOJEQtC2WR6u4CN6xxdozdTy7CO5mAFJ2vf5ZySYCekEiyxDXv0ajr5geeb91DKrChziUMUUUSQu-dDzoHGpj_M4_QQaRyyplZzGGv7z1PzVimwIsXltXPSioYm1TOvi3e1Xn0wyEAdNrVApJ_q03qI8szVfIcKoOkBHj72wQ13Cl4aZLzSmgO7usjuf9uEt-3hnD6pQkmkBlHJDTe6s-qWrAgAKEOqvVE6iZH1-jYtd8QoghmBAO-L7f0zcQAi6OUycJDBBBC_H7l-xBNtaxn0NoXAkj5OuuynFmTkrlKas_pn558E7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
چرا پزشکیان ۱۷ شهریور که تولد مجتبی خامنه‌ای هست بنزین رو گرون کرد؟ چرا روز تولد خودش گرون نکرد؟
میخواین همه تقصیرات رو بندازین گردن امامِ ما یعنی مجتبی؟ کور خوندین!
ما دیگه فریب بازی‌هاتون رو نمی‌خوریم که میخواین علیه رهبرمون کودتا کنین.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71525" target="_blank">📅 16:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71523">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=bAoLtZrQy8d7iFdQsu4U6He5U9iW8cEy2Ji8cmBTIbCC-jbfHTl1KsifyiGeP1AQoGU3eFjJvNnn0OwNyUe139_mP2WGP2Nyck0J9lfDMDjzUy8ZEHLbogVymT3ln6YLFNiKYFwPJyFLHe61U7ntTbTPExq9E2YmHd4CGzFSPB_nbeegS9g8ZT5-UM8l1nSfjQChsBNOy-J6naoj5A_WGxGChk0KyAgOQFx9_URyveWh8vlakW3S-WJN-Nd2AC6fWRCzf4AJYPhmYfXwDLtYtwIuqKWeYn8h1jGjWl3kO81LN2LGRywZ4F6iL7m4r81XmJ_TV3P4c4A49yY14RTOGgNSDdynJzrwQP2nbYluxXLPv8XSqgH299Hj9SVmpsWZYJSpG33UMDU79A3I7P7ZMKdSVgqqZGRf4c8I59F5LOIN2dQej3Ia9CZcJNi1ZNQBN-hwObOUqIpfxdgvt532qAgENwmUkPRoEP5R26iMRggfCX41aC3VEVngoapKG7P_cxXm8F4EzOwRhmF9yTNmiCTun33-Ufmwu5FsWuKrGr26d9Z9ygIzcGbeepymC_hT8g-uC_Ud8de3p3C4oYpyA11pceuNJ_JGUL7XMlo4lXuK9uUiY8keORuwMeoZrfofYgSPpBizkemxxBr5qo-xJ1sv4TTY71GbTwTOCkTQfw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=bAoLtZrQy8d7iFdQsu4U6He5U9iW8cEy2Ji8cmBTIbCC-jbfHTl1KsifyiGeP1AQoGU3eFjJvNnn0OwNyUe139_mP2WGP2Nyck0J9lfDMDjzUy8ZEHLbogVymT3ln6YLFNiKYFwPJyFLHe61U7ntTbTPExq9E2YmHd4CGzFSPB_nbeegS9g8ZT5-UM8l1nSfjQChsBNOy-J6naoj5A_WGxGChk0KyAgOQFx9_URyveWh8vlakW3S-WJN-Nd2AC6fWRCzf4AJYPhmYfXwDLtYtwIuqKWeYn8h1jGjWl3kO81LN2LGRywZ4F6iL7m4r81XmJ_TV3P4c4A49yY14RTOGgNSDdynJzrwQP2nbYluxXLPv8XSqgH299Hj9SVmpsWZYJSpG33UMDU79A3I7P7ZMKdSVgqqZGRf4c8I59F5LOIN2dQej3Ia9CZcJNi1ZNQBN-hwObOUqIpfxdgvt532qAgENwmUkPRoEP5R26iMRggfCX41aC3VEVngoapKG7P_cxXm8F4EzOwRhmF9yTNmiCTun33-Ufmwu5FsWuKrGr26d9Z9ygIzcGbeepymC_hT8g-uC_Ud8de3p3C4oYpyA11pceuNJ_JGUL7XMlo4lXuK9uUiY8keORuwMeoZrfofYgSPpBizkemxxBr5qo-xJ1sv4TTY71GbTwTOCkTQfw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره ایران:
«ما کنترل تنگه هرمز را به دست گرفتیم. تمام مین‌ها را پاکسازی کردیم.
من گفتم: «خب، پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟»
گفتند: «قربان، این مین‌روب‌ها زیر آب هستند. آنها همیشه در زیر آب فعالیت می‌کنند.»
گفتم: «چرا این کار را می‌کنید؟»
گفتند: «خب، به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه هم خصومت و درگیری زیادی وجود دارد.»
یعنی اگر در یک آبراه مین وجود داشته باشد، معمولاً افرادی هم هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
حالا دیگر هیچ مینی آنجا نیست، هیچ چیز دیگری هم نیست. و اگر ببینیم آنها [دوباره مین‌گذاری می‌کنند/اقدام به این کار می‌کنند]، آن‌وقت می‌بینید چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71523" target="_blank">📅 15:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71522">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=QvX86-XsTOjIQMB_w99gffCV12_DnndnH2_yYy-Z7rXMl5O7GAYo5_SY8OI7kdZjUeezr99v7UznkFynB8uNEBfqa60HyotOhi84L9yWSXfrlyyXA34KEJzWhY11mYoZlNDDRYTdi_8iryKRYgpmXDZN6J5DMmv1_lofem1Y4xS5E5kLVaGJg4whVhixDBjUy79FqlKnnWJoEwcdgrzXMwebOb76DuSqmfQvQ3Avya9lT22LWIbB7I5H2Y24QLTiBH-0A4hgdI2yBry1hyyswjUMfM4p7IvH9eOml5fkO5dtk4ANyTUT7hkZhJ2JoNwVlPLW1Oul0k_8t4U4GhtikQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=QvX86-XsTOjIQMB_w99gffCV12_DnndnH2_yYy-Z7rXMl5O7GAYo5_SY8OI7kdZjUeezr99v7UznkFynB8uNEBfqa60HyotOhi84L9yWSXfrlyyXA34KEJzWhY11mYoZlNDDRYTdi_8iryKRYgpmXDZN6J5DMmv1_lofem1Y4xS5E5kLVaGJg4whVhixDBjUy79FqlKnnWJoEwcdgrzXMwebOb76DuSqmfQvQ3Avya9lT22LWIbB7I5H2Y24QLTiBH-0A4hgdI2yBry1hyyswjUMfM4p7IvH9eOml5fkO5dtk4ANyTUT7hkZhJ2JoNwVlPLW1Oul0k_8t4U4GhtikQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هادی چوپان :
هانی رامبد از پشت بهم خنجر زد.
گفت پشت جمهوری اسلامی نباید باشی ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71522" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71521">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhQkxUMakUnY-YSY9kBgH2jBNwMu1Zddbh8JwmuC5LqhlzUZx4aQMunVl2C4z_-1nOTf2a8CRcK-s7lBIzIHFl-I_iUMEK_dBDfQwn4Ah2BA2NQtsHmgpueiggyB5FQydWXUcPekqDS0Cnp0gUukv-0kqFZ6SubW9KyTLcGEfY-o7bRVXcgP1oQMdmsm4WjMjbhmQRuFxKVYixbFINlIohS22OEWecec73atbq6Tc5QpFHjpV_CDUSXuscsV2T1SVUQqw0fjYtR4xv20S1HtZ-m1iH0-QdLYRib9OGCznpoLN9J6pnsxHWlRtlmTCPKrK8CXECA9_C0pCrcxToLvCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
پزشکیان در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان رئیس امارات متحده عربی دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71521" target="_blank">📅 14:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71520">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=rhefe1q-TcnBOZfrq1VD_54mfJ6zkZdakugGO9CBDuCNA0ynjmaCawlPsxeKZMdVthK0G9n-xLoUTl5xOCjXisjPmQYbfypohzjReYbdop7bKaOc_VIVDDUNrl_j58AQH2ZvEtoXKDt5cAwcn-tWwSanzAhwYhNSwCmLZDhkcnriVquC1LdJX8XaJkxE9MncTZsZJakYbfKv6h6gsyu1Ao2iboeDdlSHAOD1L_H90AC91As2E-AC3p9iZ8L4JuenC6-Em8Whj9IvMF1G36uRzMpaz4wWAsl8OKCceIGJ3y3wi78NIjahoVjiQP03zQiimHyMW2xIk2tsdN0MBo0S9GtVOcBmrq-0LNSmcfeKdzYMcPa8dUE8EYpoosoV-JxxjVWers5tM-O2lfOWOl0pf0bFUwMoa0sbII5uA6cE_sV23w_Mpbb61d4FHyKVJFveMSOt6fym8iBWZqdzOkjKcQqmvKKCch2dgGo5uMTOMuQLZHYBHp6TMlw0SBQYPaAuu6PLLFLS3f9ADfFSMlMJxYVBmYQ7N7l4D3YiTz2K0BFC5qBL2GY3L-FtgJHxdXtqAaczeQqQa84cuf6u7MyjNYewBivxRc_-RARxPBlWhDtaL6PPRd2Ktyr3ZuZB33feMzBZpVnj-GIqK7bUochgspYv7Zrqvdu9kVvwpstUT_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=rhefe1q-TcnBOZfrq1VD_54mfJ6zkZdakugGO9CBDuCNA0ynjmaCawlPsxeKZMdVthK0G9n-xLoUTl5xOCjXisjPmQYbfypohzjReYbdop7bKaOc_VIVDDUNrl_j58AQH2ZvEtoXKDt5cAwcn-tWwSanzAhwYhNSwCmLZDhkcnriVquC1LdJX8XaJkxE9MncTZsZJakYbfKv6h6gsyu1Ao2iboeDdlSHAOD1L_H90AC91As2E-AC3p9iZ8L4JuenC6-Em8Whj9IvMF1G36uRzMpaz4wWAsl8OKCceIGJ3y3wi78NIjahoVjiQP03zQiimHyMW2xIk2tsdN0MBo0S9GtVOcBmrq-0LNSmcfeKdzYMcPa8dUE8EYpoosoV-JxxjVWers5tM-O2lfOWOl0pf0bFUwMoa0sbII5uA6cE_sV23w_Mpbb61d4FHyKVJFveMSOt6fym8iBWZqdzOkjKcQqmvKKCch2dgGo5uMTOMuQLZHYBHp6TMlw0SBQYPaAuu6PLLFLS3f9ADfFSMlMJxYVBmYQ7N7l4D3YiTz2K0BFC5qBL2GY3L-FtgJHxdXtqAaczeQqQa84cuf6u7MyjNYewBivxRc_-RARxPBlWhDtaL6PPRd2Ktyr3ZuZB33feMzBZpVnj-GIqK7bUochgspYv7Zrqvdu9kVvwpstUT_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
ببینید، ما کار فوق‌العاده‌ای انجام دادیم. می‌دانید، ما آنجا را تحت کنترل گرفتیم. ما واقعاً با اقتدار کامل بر «تنگه هرمز» مسلط شدیم و هیچ‌کس متوجه این ماجرا نشد.
ما کنترل بسیار قدرتمندی بر آن داشتیم.
ما یک محاصره دریایی اعمال کردیم که واقعاً بی‌نظیر بود.
ما تعداد زیادی از شناورها را بیرون می‌کشیم؛ به‌طور میانگین روزی ۲۵ شناور را خارج می‌کنیم که بیشترشان در شب انجام می‌شود.
اما به‌طور متوسط، هر روز حدود ۲۵ شناور را از کار می‌اندازیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71520" target="_blank">📅 13:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71519">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، جنگ در ایران چه زمانی پایان می‌یابد؟
🇺🇸
ترامپ:
فکر می‌کنم خیلی زود. گمان می‌کنم احتمالاً درست پس از پایان دوره [فعلی انتخابات] باشد. آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا وضعیت انتخابات را پیچیده سازند. اما فکر می‌کنم مردم متوجه ماجرا هستند، چرا که ایران نمی‌تواند سلاح هسته‌ای داشته باشد. موضوع بسیار ساده‌ای است؛ مسئله خیلی ساده‌ای است. ایران نباید چنین سلاحی داشته باشد. آن‌ها تنها دو هفته با دستیابی به سلاح هسته‌ای فاصله داشتند.
اگر این کار را نکرده بودند [و جلوی آن‌ها گرفته نمی‌شد]، اسرائیل را نابود می‌کردند، خاورمیانه را به آتش می‌کشیدند و به برخی شهرهای اروپا — و حتی فراتر از شهرها — حمله می‌کردند. و احتمالاً پیش از آنکه ما بتوانیم آتش را خاموش کنیم، به خود ما هم حمله می‌کردند. اما آن‌ها نباید سلاح هسته‌ای داشته باشند. با این حال، می‌گویم که [این اتفاق] به‌زودی رخ خواهد داد و قیمت نفت به‌شدت سقوط خواهد کرد. وقتی آن اتفاق بیفتد، قیمت نفت به‌شدت پایین خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71519" target="_blank">📅 13:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71518">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⏺
🇮🇷
قرارگاه قدس نیروی زمینی سپاه:
درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به هلاکت رسیدند؛ همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از مخفیگاه این تیم کشف گردید.
در این عملیات که تا پیش از ظهر امروز ادامه داشت ۳ نفر از پاسداران گمنام امام زمان(عج) نیز به شهادت رسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71518" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71517">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=FwOwZTDZq4chSKIrNtbhsryH9IwNlrIs8GToPqG1rIBdYqNUtw0nIpw0MrfJIECX-XQiA3oGjYhU3FO6A3bbr0m0poqTOE-bGIJjMWHF3rgs157mxPnwpMYJUnLFpnYdEOBJX5u-cPC8x45CM0lnKygJfMbENt56VDft6WHoGxKowF8YGAuIw9ezRp05QiS0qi6Gki1Rm1sM05HOLrSNvw-GSew7860PigrB4lvqPzQ7N0msIj4GtdWug6-LHVRS-1EbOes00sorfqKV1mhfQLv-R6yeHkFDxCXm3LfKzi0DkucAtzytXrEu5IG0opurYQN69hF26sEh2oZFTizmlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=FwOwZTDZq4chSKIrNtbhsryH9IwNlrIs8GToPqG1rIBdYqNUtw0nIpw0MrfJIECX-XQiA3oGjYhU3FO6A3bbr0m0poqTOE-bGIJjMWHF3rgs157mxPnwpMYJUnLFpnYdEOBJX5u-cPC8x45CM0lnKygJfMbENt56VDft6WHoGxKowF8YGAuIw9ezRp05QiS0qi6Gki1Rm1sM05HOLrSNvw-GSew7860PigrB4lvqPzQ7N0msIj4GtdWug6-LHVRS-1EbOes00sorfqKV1mhfQLv-R6yeHkFDxCXm3LfKzi0DkucAtzytXrEu5IG0opurYQN69hF26sEh2oZFTizmlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران مسئول حمله به خط لوله «شرق-غرب» است؟
و به نظر شما عربستان سعودی چه کاری می‌تواند انجام دهد؟
🇺🇸
ترامپ:
خب، فکر می‌کنم همین‌طور است. احتمالاً همین‌طور است.
آن‌ها در حال حاضر در وضعیت آماده‌باش و هوشیاری کامل هستند، اما فکر می‌کنم مسئول آن هستند.
آن‌ها مدتی است که کنترل آن را در دست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71517" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71516">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=kzM9oZMj3xEws4CYxMGEZO0yhwghHpG8zJddVNNK4C9Ka_M6x55A41D8zuRPnxWNodLjDTNOppe_LQkL7a5uC800l6NgVCyPZpGUcf0SHQk9NvJbgdAFM2-5aZhPQrmqOUpx7XuAJSHa9iBk55Aqvls8BMz72N12eAr1xllYeVFkMczElMeeYjzIzQKQK01a2jBZcMEKeKlNcj4rOXxbiHaH_cnZmCY4P3WPoltezAbEWYieHpQLa-iA9hPw79X8xU8iooeRYluTaP2Xerrn7XzYm2scair4mOWa5AvB7nGjVPinEi-OtZFJ35951bF_7XiI_y44A0Eqm5146o309g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=kzM9oZMj3xEws4CYxMGEZO0yhwghHpG8zJddVNNK4C9Ka_M6x55A41D8zuRPnxWNodLjDTNOppe_LQkL7a5uC800l6NgVCyPZpGUcf0SHQk9NvJbgdAFM2-5aZhPQrmqOUpx7XuAJSHa9iBk55Aqvls8BMz72N12eAr1xllYeVFkMczElMeeYjzIzQKQK01a2jBZcMEKeKlNcj4rOXxbiHaH_cnZmCY4P3WPoltezAbEWYieHpQLa-iA9hPw79X8xU8iooeRYluTaP2Xerrn7XzYm2scair4mOWa5AvB7nGjVPinEi-OtZFJ35951bF_7XiI_y44A0Eqm5146o309g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
این رستوران توی تهرانه
نوشته : هیچی کتلت بی بی نمیشه:)))
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71516" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71515">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=dkc0cP0iJWZpgSGy5PPPE7dwtnWwhpHFcYOTUcS3BqRN8ADl0B96AKqcQDbBTkju9JycORNESb0oZ7W_K1YH7eVDYdaxjRAfm7DM2W7cj4VIZAf_g2RqcbJuz0oXlk7hCyZIVXT_KE1xy3CPk-skHOQQkq8UrigFbkpVyeQyBHjv05i-2h1P_iWaMbm_ajmJP95VeN6bTOBgRv849L-B-PoDt9-rCZkRtzyY3PF-2h5nkVfPoLMxtllLTYQcq89nrLb2UXBikfTx1WzRWqFYsM7Z_OtOxDgBwBwDzE4-dsVSp-KV2PJ2POE6-BPiRqsZ0p_T8vAKwMc2Sz0-nu15gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=dkc0cP0iJWZpgSGy5PPPE7dwtnWwhpHFcYOTUcS3BqRN8ADl0B96AKqcQDbBTkju9JycORNESb0oZ7W_K1YH7eVDYdaxjRAfm7DM2W7cj4VIZAf_g2RqcbJuz0oXlk7hCyZIVXT_KE1xy3CPk-skHOQQkq8UrigFbkpVyeQyBHjv05i-2h1P_iWaMbm_ajmJP95VeN6bTOBgRv849L-B-PoDt9-rCZkRtzyY3PF-2h5nkVfPoLMxtllLTYQcq89nrLb2UXBikfTx1WzRWqFYsM7Z_OtOxDgBwBwDzE4-dsVSp-KV2PJ2POE6-BPiRqsZ0p_T8vAKwMc2Sz0-nu15gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
🇺🇸
پست جدید دونالد ترامپ در تروث سوشال:
با این رئیس جمهور بازی نکنید، زیرا نتیجه خوبی نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71515" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71514">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRyo57_J1dJwRzrSV-r_gUBtfhJDhESPlQnWsSUm7IS5v1l45ZIt2LCK-REOypXtgMmBWlXC1MArHC347vQFbtZY0V5nQpooZAOXp-r68V5jHL7QSOkkD_Q77Fq5zSpf4vnxpCcDMmGHpurh-scL5fmvB2U-yi8p9zbqxBFUVI1jx9ofev5t20XhSJRNzOJZarWWLrtkQVt0D4hX6jnfMpJ8bHfdpT_9D45r10x4TH1hgaMPtUZOPGwtHREFNYejGIhvTG2zqUJfAdF6KbsjOEfwfMkGm6-7Mwdt5Nkwx4oIL-PzG6mzDjpBpqW6mMXNtdcJMk_niKSicE8QbA49YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها تو راهه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71514" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71513">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71513" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
