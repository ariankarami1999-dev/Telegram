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
<img src="https://cdn4.telesco.pe/file/Y_jSktuvsFhV0Kx2gy3l4stVQEtXuc8U1nJmK_n39L0iiCM6OkECDfhbjd8duQfzEutHONwagdvlGRaIVy6Kyb7PZcARhiQuPTUoIgc8ntH3_Sc9xA6f_zhlkZk0ginDi8HgcccLT595iRDylLUbQpuhUh9GNHF_hpNmRK6JOkpryD91GH6-OdgvxXh2iAcg5gSrPOfe-7zoG1Ku70mapjApS84Z6VmjI49rgtvVClX_AUvAYTiVL0GNPwKDI5JZ-8A9lRIgvpJWuigcuOlgZOmL4Hh1JnT9Ue9N-oM0aUq60uH5d6XLlXh8tTYxVa8x0vcnlV1jNutsYPOkaEk6vQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 971K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 17:54:52</div>
<hr>

<div class="tg-post" id="msg-125575">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c3ae38d3.mp4?token=VbizpjOqa9Sh4YKgGiSyuZAfFaf_QH-tLUgH9lrbiAqbkCwQXRQwY911dWa0PihnF4VnFbp615n4eRknTWUbWhGUJgImRnaNYRZtOw-P_cclnq3lcMhpz0onP420RshLzWdYnJTuLtRzxbH-ss7lpK2jS-W8Nx7mNC2hEQDEuwbeBva65lk60hkQLxaIBeAkGDrww1abf69bns6yrAE31kzLznHMyoCt0dNG6GHuJM7qJmzxhxSAhb3UZr9E2b2QzwzcTYFFlRAtb_elcdPDtZP1y9nNcoymkBsyVTi4MQarxAmQ2wf7sfVp2Ud9dvqRHIhacEHOlNAf9DLJVvWFwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c3ae38d3.mp4?token=VbizpjOqa9Sh4YKgGiSyuZAfFaf_QH-tLUgH9lrbiAqbkCwQXRQwY911dWa0PihnF4VnFbp615n4eRknTWUbWhGUJgImRnaNYRZtOw-P_cclnq3lcMhpz0onP420RshLzWdYnJTuLtRzxbH-ss7lpK2jS-W8Nx7mNC2hEQDEuwbeBva65lk60hkQLxaIBeAkGDrww1abf69bns6yrAE31kzLznHMyoCt0dNG6GHuJM7qJmzxhxSAhb3UZr9E2b2QzwzcTYFFlRAtb_elcdPDtZP1y9nNcoymkBsyVTi4MQarxAmQ2wf7sfVp2Ud9dvqRHIhacEHOlNAf9DLJVvWFwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استفاده از جرثقیل برای تکان دادن پرچم در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/alonews/125575" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125574">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vj1jrNtuZG3r0p3lSLSgUwxYM9jEgZezcPuwV63FbqOclnzkC2PI87yX_tKVoy4ZwK6jm_dEHJO-On7SPpWRhg--vayYJBtuNZJfmVNW8ub1i5CxMl5us2jBQCiTTbzMbMV_AGQQWkMDLrVHX6kmjtG5vKh11hHpWkLzmhUuhD4gH-osm6Z5jtivB-Sg-UJsh5HIXHpDE4zK5cyPGPedxa2jlQynLTdJY1y795_0JfZO5FU-QUjiHIiryzcPgpzV4DgiKr_tEjEfqMz0TWR9qh5iBmMu_ZtlfYMqvBlaAqPlesxV3rF7-8jo9JIp1P193KLxWVETCtOzmlMhks4vMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیصر، خواننده انقلابی: نظام ما یک تنه جلوی امپریالیسم ایستاده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/alonews/125574" target="_blank">📅 17:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125573">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVnsT6JxGDis2HrU0r2UcQvkFJNtAQGTkj_3FPpenFmjWt5OUcMz9dlgnmoM_xbe-UjXVF1PmCHiCBFQN8YvXcQQHISAWMuRk8TYbPrH17YzLp95LYL8h6SRwczQBu0zukCAV9hDIhkiZdaVkjb_DILI31At79A4PZWhm_Iufbt6t5mZIJeAJG3oMBiTKUNuBS7bPXFnPQB-Ge3HPenGnKx1A80fWDo9tHJGrdDJUv5exN-2zpds7dbR1rA7clUezJIwbnozaXpHEn21Qo2RwALfTTLw7OWJ5AENPhqsf5An2_cJjDoXEg4ea1aUTwVFuXKKYyMKCog1RwHxky6nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسروپناه، دبیر شورای عالی انقلاب فرهنگی تو شبکه خبر رسما اعلام کرد که تاثیر معدل یازدهم تو کنکور قطعی می‌مونه و قرار نیست مثبت بشه
🔴
پ.ن: دانش آموزا یه جمله به خسروپناه بگید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/125573" target="_blank">📅 17:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125572">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc2ba7680.mp4?token=fxXZ4igpyQWRCPzxV4fbH4T7eVs4RUHEpo4pOLZcNgbz88dlA6eQmGZiYoPGfqorNuIbUkIePerAtVMa5TECTb2FKc1NsKP6RvDYj6Gm-RDUSpPxajDH2CCYx3mtKd6J4zVTYfZOweq3I7SoLEQSKKNNqzP3ciT-xRs9Joz5veZO79Xko-KfDstXUFZ7Tnji6gqNP2zNNTP5Ven6d37VQVdaP48qYCyMPHWXYi8qYcSfdOBiNxMM3mPl_378AtW6rkzdUhM7TquDtlTdu4n8CEkbWMyUes4TbKnEmQct4GU1-zTp56xJkVJ4t4znPS2ezJPJi_-5kyN9QITQdb91SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc2ba7680.mp4?token=fxXZ4igpyQWRCPzxV4fbH4T7eVs4RUHEpo4pOLZcNgbz88dlA6eQmGZiYoPGfqorNuIbUkIePerAtVMa5TECTb2FKc1NsKP6RvDYj6Gm-RDUSpPxajDH2CCYx3mtKd6J4zVTYfZOweq3I7SoLEQSKKNNqzP3ciT-xRs9Joz5veZO79Xko-KfDstXUFZ7Tnji6gqNP2zNNTP5Ven6d37VQVdaP48qYCyMPHWXYi8qYcSfdOBiNxMM3mPl_378AtW6rkzdUhM7TquDtlTdu4n8CEkbWMyUes4TbKnEmQct4GU1-zTp56xJkVJ4t4znPS2ezJPJi_-5kyN9QITQdb91SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادی کنیم از روزی که تو صدا و سیما گفتن ناو آبراهام لینکلن رو زدیم
🔴
فقط اونجایی که آخونده رو جو میگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/125572" target="_blank">📅 17:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125571">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d397f35c8.mp4?token=eTGI3XvnUwSF02g5kO3PlOloEnrScknEqzUwpftbvUxOIn88N76oyV6pwyh9VutgAzGYT-cCfOBY9xCgKqs1A8Ij28e0mPBkaXGv_Ikjf_pdtIcDc17NuZiqiOKvR1UGAd7X3GJRPO9CrSnemae6sSm5lb3ew6gOEgW9K2G8iLUDR_104i6aSl7wTC3F7BZTFCi_C3mZq5gx7Ud-f5cCLWZqw_JaPnM0HGE0aMX-y24xwkHYTeVkYoGmIUcGvGSM7EIFTCFmDwPYz1QXw3roqgd-8zFIdGZFRfXMpdQCKFGc8dh7AJCepsGqZSr53TaSpcfhleiu3lJSsAIS9dw7Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d397f35c8.mp4?token=eTGI3XvnUwSF02g5kO3PlOloEnrScknEqzUwpftbvUxOIn88N76oyV6pwyh9VutgAzGYT-cCfOBY9xCgKqs1A8Ij28e0mPBkaXGv_Ikjf_pdtIcDc17NuZiqiOKvR1UGAd7X3GJRPO9CrSnemae6sSm5lb3ew6gOEgW9K2G8iLUDR_104i6aSl7wTC3F7BZTFCi_C3mZq5gx7Ud-f5cCLWZqw_JaPnM0HGE0aMX-y24xwkHYTeVkYoGmIUcGvGSM7EIFTCFmDwPYz1QXw3roqgd-8zFIdGZFRfXMpdQCKFGc8dh7AJCepsGqZSr53TaSpcfhleiu3lJSsAIS9dw7Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ
از خواب بیدار شد و تصمیم گرفت یک "موزیک ویدئو" تولید شده توسط هوش مصنوعی منتشر کند که نشان می دهد همه عاشق ترامپ هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125571" target="_blank">📅 17:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmaXeF1KxkN0pKmmR5JW8hfo9xyxdz4HyeBG6cafrM2L8WiUNRIuZ3Q3xnBCiJmUav4DoIBMx1pTTXSN3ZvQjm7lMpcqRuDmcCGV3bFgIdVAQQ-AtqanyAIcWfpmaUHZaJ6J7QX72DaNMda3l5VUZIvb36Z3rZ7diPZCoqJEYVx8K502KJsrp7KuZ3DERwV1PEPPR2LqDS-i1nyzPB38zvjTNDdt8ub6FYUhUWotAqTUaZ3ZgId9tQ6ZvwdCSqwjOJPYpA3XunUP41o1PZr5LFkzRmF6aNebCO3ljv9Li1WKreum5xLFfAhMuVH1TpizPnHV7ZGTWxr0yNV0eSWpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HbYX08rcNf53YpKhtJVzKPKmo8-VmHFMcG0k6o7mNSwmqq3W1fvPpKnCwz_wPOI5UXTaTyOHSTUbK-xbYve3a64lok-2X08cQsA8W8xYHPvSEG8hcmdCN5MQ_8TQ-W7Mp577FxQbQ42-GHD5UmlIgiloMGvgV-brMva4nMiLzUAielrK5IyivRUvH8axjGYoTu2QGicNAtdkcsyXdNK8K3zu8GwlCLQRTpVSBGvDA8UsERerU8fPqegZiRENe3O4pIV2O1OmHNYjJyVRPc1L3ubrGCy8-BBnL6pzKwUYAUp5gKcfLuEIHcXDRf3SxSI-IRut16MNLQRYtSFMP3cRlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تئوفیلوس سوم از اورشلیم، رئیس برادری صلیب مقدس، در دفتر بیضی با پرزیدنت ترامپ و در کنار مشاور ارشد مسعد بولوس دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125569" target="_blank">📅 17:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuo0BoicIyOp-KWdu6Kb5vSphjXk3TDG__szZDyecu4PEVwx3aH9SIc5S-LdBWjIj_S2pnlfAOFjc_oWE7IB32XVIV0CfqYqLjX418efdxVzA4ELiWxgXupaLPdp-hLKxEGwK-ksW4KtkaQpzdXVwgtBA-M9UJJCtXPYDwibdl8PuKEYWDQ2rPqPUz-vChBhhdHsHjVxhH4OX1l1N1QItgkRViK7h-xLaCnLADZCcjKxlTsrlHQS3kQN73pW6ExJL7hL3t6h5QDkTupujLlCE-Y3QdiEjlK5iQqgju0mSRonWO8oMWXNda8VmCLse0pHXU45qpe0wiNs91iu0Y6ksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/125568" target="_blank">📅 17:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترکیه در حال توسعه یک شبکه دفاع هوایی چندلایه موسوم به «گنبد فولادی» است که در آن رادار، جنگ الکترونیک و سلاح لیزری به‌صورت هماهنگ برای مقابله با پهپادها عمل می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/125567" target="_blank">📅 17:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfMeQ9sUrEhuIrL6i-J3VUUxdw2RVs_w2McpKU-RagOpm82MbM-pBHBUSKGEdbRkGSrs_XJc5wIJx2taMltTk0sZyAWD7L0_dkwjT4OTSvW6wfR4N8m3ZMk3D9zEMTfpIDP2yCYUQI7KXmG93FDcJpJGDcTT6jdcAgiAe8D0g0Axot7LF8aJNj5OaRWw5cBQHKvUljFdscKkGqXrjtvmszSU_oM45XXeII1TTsQukWVcHvTn9v6230KzvpBUMqhugfITHaUG4IgqqOuZ894AnYfDyCJwgYTYuem3mpU_CYvM-AHWVS5ylF1oCHjjreBoR955oQg0TY_ij-t8Bhs0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جهانبخش: آنطور که من شنیده‌ام کارتل‌های مواد مخدر مکزیک، ایرانی‌ها رو دوست دارند و گفته اند مشکلی با آنها نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/125566" target="_blank">📅 16:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزارت امورخارجه برای بار هزارم، نقض آتش بس توسط آمریکا را به شدت محکوم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/125565" target="_blank">📅 16:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD-zTx42vO1MhcWJKkBVYrA_EyufOWDLQ9nDgGAUV2r3mjH4OZHzXgwvEYHwsN5vf3dnMBjbGhPkcsG8-bGBsr-GG9Roxs6N2iAQCr0u1Ezj3W11CRxNjgyt41dlzr1Tm4rPiD5gzRLU_vMBSjDyOBb3PwEtNWrjdOqEFcLCz50iD3RsC-qp_8gFsR6XCviFFoH2E8SkXeo0WVG7gpj1rVRVQpGehhNd42tHu-vU88sApCLV59PK7eok2OuJYiGcT1Gc8K-Ixd4BmS35uyZRz7pSDDEybPDAqH56YCEbbEAVlWbQw6WTZypR0prLDLH24QbMmk7F5jFj6vDUfcRaqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفع بزرگ اقتصادی چین از جنگ ایران
🔴
جنگ ایران و بستن تنگه هرمز، به صادرات تکنولوژی‌های پاک چین مانند باتری، خودروی برقی و ... منجر شده و به ماهی ۲۰ میلیارد دلار رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125564" target="_blank">📅 16:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkFwQ4iCK-FQgq-AusIJrUp6p8qnfgrJGG6Qf6v2X1j6odwDDpQZuqy94644eW0tSPxHel_IaTPHf-bfVtFSMgcFKvQrOC6v345TclHw6BUjnhYE_OURQTeAPziK3UQoPm1YMRNAaMSQvIO5IhnyfibfBS3Gyt9EkZSMN8HUfdavyv-etJuIIYnAHlRWzgOAIJaA_GRIrMlC-6SZKb6bv_fSdqmfogEU3UXeOnKhTY7KU_vKO9EG1Y372grGVIAqym28NeOvhS1Y4QsLfv3vvKATtjg6bPUKFzwyKGHNzmD_z7ZKGoEpGS0F7ci2pFjvltu_udjFfETxTgbhXbhPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار وزیر کشور پاکستان با شهباز شریف پیش از عزیمت به ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125563" target="_blank">📅 16:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پست ترامپ با عکس‌های خودش و آهنگ : ترامپ ترامپ ترامپ، هی دونالد ترامپ...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125562" target="_blank">📅 16:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مسیر غرب به شرق تونل نیایش و پل صدر امشب (۱۶ خرداد) از ساعت ۲۴ تا ۵ صبح مسدود است و مسیرهای جایگزین، بزرگراه‌های حکیم و همت به سمت شرق می‌باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125561" target="_blank">📅 16:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
خضریان در نامه به عراقچی: صدور ویزای ۱۳ کادر تیم ملی در بالاترین سطح دیپلماتیک پیگیری شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125560" target="_blank">📅 16:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزارت خارجه کویت در پی حمله صبح امروز به پایگاه نظامی آمریکایی علی السالم، بیانیه ای صادر و این اقدام را محکوم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125559" target="_blank">📅 16:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزیر کشور پاکستان، لاهور را به مقصد تهران ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125558" target="_blank">📅 16:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125557">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزارت خارجه ایران: وزارت امور خارجه موکداً کشورهای منطقه را به رعایت اصل حسن هم‌جواری و پایبندی به اصل بنیادین حقوق بین‌الملل مبنی بر خودداری از اجازه‌دادن به طرف‌های متجاوز برای استفاده از قلمرو و امکانات آنها جهت طراحی و انجام اقدامات تجاوزکارانه علیه جمهوری اسلامی ایران فرا می‌خواند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/125557" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125556">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت خارجه ایران: نقض مکرر آتش‌بس از سوی آمریکا بار دیگر اثبات می‌کند که
این کشور نه‌تنها اراده‌ای برای کاهش تنش و بازگشت به مسیر ثبات ندارد،
بلکه با اقدامات ماجراجویانه خود امنیت منطقه را با مخاطرات جدی مواجه می‌کند و
مسئولیت کلیه آثار و تبعات ناشی از این اقدامات غیرقانونی و نیز هرگونه تشدید تنش احتمالی، بر عهده دولت آمریکا خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125556" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125555">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزارت خارجه ایران: نیروهای مسلح مقتدر جمهوری اسلامی ایران در چارچوب حق ذاتی دفاع مشروع و با هوشیاری، قاطعیت و اقتدار کامل،
پاسخ متناسب و مؤثری به این اقدام تجاوزکارانه داده و اجازه ندادند که اهداف شرورانه طراحان این تجاوز محقق شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/125555" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125554">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزارت خارجه قطر: ایران نباید مدام با حملات بی توجیه خود، امنیت و آسایش منطقه را برهم بزند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/125554" target="_blank">📅 16:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125553">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4f1fac45.mp4?token=UOJ2-YsPhGyCeFiRUNguRD4vsRQD2geK9bgZPFHoLPGVJM4YjC5h-SqrZ8TTGq5DgqYQP6AWSIS_-LITdS9fpV1rkbsCKy6Yxx-8-0CMS5Xj0IAbwI1EaRRhEu-zAv7agwCvr89RflI76M63eQwjYoQHGf9W7O_VkocXeVMS2oYxLGR8XRwlBpoh-ZBE7ieHgbuP_ucuv10oQ0Eg_kWxvHRnJxBYSgyaD0sc8kJ36_Gc4oPfQ2PBZizQKUqFpeHyLcXhopAiITr4i3EyJdfPmZwbH5Bndl8I35RGSgJyvXUkevfQDsyMbx-vicldom58vutS3pItfS31jy_cwaBogw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4f1fac45.mp4?token=UOJ2-YsPhGyCeFiRUNguRD4vsRQD2geK9bgZPFHoLPGVJM4YjC5h-SqrZ8TTGq5DgqYQP6AWSIS_-LITdS9fpV1rkbsCKy6Yxx-8-0CMS5Xj0IAbwI1EaRRhEu-zAv7agwCvr89RflI76M63eQwjYoQHGf9W7O_VkocXeVMS2oYxLGR8XRwlBpoh-ZBE7ieHgbuP_ucuv10oQ0Eg_kWxvHRnJxBYSgyaD0sc8kJ36_Gc4oPfQ2PBZizQKUqFpeHyLcXhopAiITr4i3EyJdfPmZwbH5Bndl8I35RGSgJyvXUkevfQDsyMbx-vicldom58vutS3pItfS31jy_cwaBogw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلمی از ۱۸دی خیابان سهرودی تهران
🔴
از سری جنایاتی که جمهوری اسلامی با قطعی اینترنت در صدد مخفی کردنش بود.
🤔
عرزشی حرام زاده این مردم تروریست بودن که بهشون شلیک میکردین؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125553" target="_blank">📅 16:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125552">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل: همه امیدوار بودن که آتش‌بس دووم بیاره اما ظاهرآ قواعد بازی داره کاملا عوض می‌شه. خودتون رو برای  آخر هفته‌ای داغ تو خاورمیانه  آماده کنید، زیرا ایران و آمریکا درحال گذار از حملات پراکنده و شبانه به رویارویی‌های گسترده در روشنایی روز هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125552" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9995675c84.mp4?token=Z6FzkoI-K11M0776wP3bVkeJFxd-ULYstiYE94UsXlHC2iEjyxPnXS2NUrwjQKB8Fj-6y3EOAhi7WEncrYoqAsGbVf-QWauopxShzcn0IGSo97BCujk_aA3yNKyrcvwl8GRXfjYYJNG2-VwG0R3ev_CJA4D_Uvga5nwUnoWSJBWG8fpSN8CBHYYxIzEAqlgM7v9lj72AuAf7EKE3eooUUA_s7FyiPYdxzvzJtpyasT4LaU22AO2WJDe7tcqIB47QrBiIBt3MnzCT02P4MEB8csWLMLGJadYF6e725opjqnU3nEVh1oet9PdVSmqqOV0JRAWqCwEXnJsw-jj6JTHntg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9995675c84.mp4?token=Z6FzkoI-K11M0776wP3bVkeJFxd-ULYstiYE94UsXlHC2iEjyxPnXS2NUrwjQKB8Fj-6y3EOAhi7WEncrYoqAsGbVf-QWauopxShzcn0IGSo97BCujk_aA3yNKyrcvwl8GRXfjYYJNG2-VwG0R3ev_CJA4D_Uvga5nwUnoWSJBWG8fpSN8CBHYYxIzEAqlgM7v9lj72AuAf7EKE3eooUUA_s7FyiPYdxzvzJtpyasT4LaU22AO2WJDe7tcqIB47QrBiIBt3MnzCT02P4MEB8csWLMLGJadYF6e725opjqnU3nEVh1oet9PdVSmqqOV0JRAWqCwEXnJsw-jj6JTHntg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه فیلمی منتشر کرده که نشان می‌دهد  آن‌ها بامداد امروز موشک‌های بالستیک به سمت کویت و بحرین پرتاب کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125551" target="_blank">📅 16:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e63a2b05.mp4?token=COjtLsQLZnv0zi4JSZ0u8Q-gz8o2GsCmnoaw4_zWlpZYoNQHW28eSx7GQvES72g2usEwPhgEOR7Yh2W7Ywjbh1vmSc7mpEwSAHt3UA95rWlWSkesD-6VsrtV0XKJQlYC4FvGAW_aGBE0hupLtlRxwYyvmrBGZv_7O9xy69yR56YNShxFDg32u_lei00PK_xXBO2DWx1lGxruYqoZDRi96eeBcyxgX8e1Z3Aa8hG-pHaZGuHZSpjmu1vdAh0qdRkP-dgPZ-sK6V6cOg4jFve5ntovYhvM4sjmV9X3tGdS1uET032jc2oJxUvlqGvxLmP5Mn5AP0r-dhYNH51rGflg9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e63a2b05.mp4?token=COjtLsQLZnv0zi4JSZ0u8Q-gz8o2GsCmnoaw4_zWlpZYoNQHW28eSx7GQvES72g2usEwPhgEOR7Yh2W7Ywjbh1vmSc7mpEwSAHt3UA95rWlWSkesD-6VsrtV0XKJQlYC4FvGAW_aGBE0hupLtlRxwYyvmrBGZv_7O9xy69yR56YNShxFDg32u_lei00PK_xXBO2DWx1lGxruYqoZDRi96eeBcyxgX8e1Z3Aa8hG-pHaZGuHZSpjmu1vdAh0qdRkP-dgPZ-sK6V6cOg4jFve5ntovYhvM4sjmV9X3tGdS1uET032jc2oJxUvlqGvxLmP5Mn5AP0r-dhYNH51rGflg9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه در حال استقرار سامانه‌های پدافند هوایی Pantsir-SMD بر روی پشت‌بام ساختمان‌های بلند در مسکو با استفاده از هلیکوپترهای Mi-26 است، به عنوان بخشی از تلاش‌ها برای تقویت شبکه پدافند هوایی پایتخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125550" target="_blank">📅 16:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: تحریم‌هایی علیه شبکه‌های دخیل در قاچاق سوخت ایرانی. ما سیاست فشار حداکثری بر نظام ایران را ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125549" target="_blank">📅 16:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125545">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aph_W4vCwxFej7kP9bcAmNFp5_AhGwcZMP_W3a7iJALTknln2KOfJTXsUuIJZAMpbrFCFKaDeQhJf6Po4mHQV3zQnpLSyN23uUxrkzWXJ0pl_vgiZtnvrh1-Ga_AXqz_3k5njel9RSg9XBL07tfpkG4VXmpDnt052nA19npY2DKiS6p8H0m4G1sQh3CKYd85pgq0pRM3FjHf0vJpeJSuCN9RjmW5_5s6FEc-7Ee6wGSstJEomVbZPebnuX_fYya6leiYnT9nqHCD0kqGTXdKdOnl4SfVkrnxJo36xEbQw7oqUhnknTX-3HB6f5EFWPh6dRu7kmDb4AtseNDbJ4dt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukxogvXu03mnsi86GAT3zS8S7RsQDQ_XNDKxqyXlzrcUS1Wgao42NNRgvz5CqxjvNghmvS30VVNVb4Mve7yJDq5iDdcd0HSQe0TLY_rbE57FuwzVmANVtVEenkv_2XH1ALEnSJTxr0atRluNRlsHsGZ33c0qi5f5qxgHXEYpTteqhgfZWFVl_ylv3W1kMW3pvXwgn6Sp17_QMh5DJp1qbK1WkITX3mPw1-0BtZ0zZT6oBNRXopG5UiIBT66XEKX61svB7n9PjncdvHEY5GFmBaLq_HSQXmXlCXl7BuG7xbVbaNLjBIRYyhY-O5HD14g0vIFZNHXR-0waUy37FJRCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3gklu0Z659sp4l_Pd-BERyBebqhdyutSdaDc81M3y4JijfMXLVHhSQyracMQOBaKtImQvCVmGlqgZubEIUuYCQVGLUmbUIMoMqNj4IYZdyhfhi3MqqjGjr-JR1u7a4nTN4AVhirVYfIR2KTDXKe8BWKWVzLMseezwwai6JqVuPF63aBj8eEtNUfld26Uqb7z8dtU7UAzDQEN4mNph3wyTn9mtoFv5NqAjXRiOriCa_4hKvDqzHWlNRnzsnRCKw-eXSlpC1DvrF2m-SxdYJRseyieO9g5MbPQJYY-PQCd9Nf5GsEM-u5EKsx1jKmek4-J1aQNMShghiO4o35LvD-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJLGNtkHRDF90cL1g9PhZ4Md37TT5GUTtO04ual22Q8I0vtknssytVSUPQ55hrEk_uOxUM0GyXn1-CzvQJccXQtb5sVMgSXoskkYFsJ_dfnSvxrS50e-Wb_bh7j4UcYbmtSxzvz_fiV5mnXdlJULZ1rvd9KCrMQIX71T1dRDoyfRTutFQDmZLTo4TC2dSf0FOFb6yjS3d_EVRwxdcAtVWHLAGadpaHSHL56zPFFhnUCm7BTOUDrgltlAYCfmU757RXWL8eetXeLK7Y_EXsBU-fUYYGlhAXQe3kbeSQ4i9bZ8W6bvvGVUozr5Xxi0pwRoQH51FqPdIoazSPQxiy1TPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی در چند ساعت گذشته حملات هوایی را در سراسر جنوب لبنان انجام داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125545" target="_blank">📅 16:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNuiS5AFfW_iFH89Z7ixie9JF7Ediovlm1BLeFLh8SNEhDf5h-nyDr78STNWkculx5qGTe5stoneTJmyOrYXiFdRZhBuHt82PWlQ4NlZQhYftcJBmH1i0w8Or9fwewXB9CAjO15QBa4p_BKYqqtTI_plt7_FUmdZ7wgUEQkKzxwGTQRahk6C2r0oEnUuT-f5KcvM2yW37xcI7w7foWFxq6u269mMZPfgDd7AzgzlwUUTw78Jls2k6ifvzXCSNpmUorfLY2k3Xr5OoHmc-Pl-KjMlJ3M6V9-3inABm7cnqeiu2B3EEivTRCjlnN3n3K5JU5DiBdc9iDALip0jrYRBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kn9dlxyUCol9eyhU0z9x5ch0kDv5n7-x0vpNwLX5-bYMWWWjAdZXurs6Ttm2xmiXajOBARV1fgq8EJ83AqFOY3YBk8pM04XxeRendMA-dxYhq3II80POQG5NTFIbAOMn94SakpPu6TeEwVBTpiszXRH7D6GdMNSAd8qG-1EhxquR3r-e2pRdeNrymNn2SZgfUnGMJogAzxiUC8GYpW3-e9zIexkwfAHuLBkjm8gYsEtJwLHfWnY7O1XShLgj0CvS-96YNKSsqhXw9nLyp7FoJS2dkDDuaOK3ZoB120MZ8N1FWo2EZRVjSANy-Q71HyAlsLUWJlGmRJComzp2SEQEKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nb3d-npASTk_34aKBEGaMycquC6Re_utibdYiiqjDt4bkeZvZn0VFvzu5toNmvtpTgNBGDARZB-wcizGmSlZnuOdBJqpxDhaeul2DTlON-oicPzQfIjtcZGCyS8NrwtwSgCY6hmFOyf5sYNXqcNCwzPtB_IRAbHZsYk0cLaLe8Af3OPQcrtdJOuzcF8z2-Kuaje6uYS4p1Z5hKazsElXltdV7ShdhmsXCJUIhziDYkfuWfVBsYfY5ZBswmHAWfqXc38zSXIX-S7EhDVPBQOnjfvkUl-f4u3yoZB4-j9H4lOWYsemqRx9PwjZlrY-ijsFxRgIKGe4y1wUpqthDGAbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPTcs2CLeYewkBzdarwJzHQfTSwLplTKD66YH1f2oX8d1BdCO5KUFLfXVsdk_SQpEouakSVsyhyz_PLRBpSf0Iifkd0w4z7HXgDRVJt7YCWr7q7bLvLjM5Fa_c_ekA4gGjUfsUgoeC_-tDGlE1I1QKY9Oqm7orBNcl15e7JtfQIZrDNQtDbeLgOfCcCY_C1JMH69RuFYPIUUFtq_iwONyXb-N33tnKOkXBFeodr-vtKtYdW4H-ejP14TxBtPYF7WgYM5nRtdyeGAlGPpxAjVaZAdmCkUIP_lj-mzF36IfrkAuDf2tRyqBXLAhJOHRro6KOeQh-I9E9dhnYDh6C-hQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCXhqUMNKOxSWPRichIZMEaexHjHFBOGt4xGs-_G7Me0yDVTvMOVmxnNqe_Dpv8HmwTRGHH6JpOatG4wXFxG6Z76Far43RD7sZlWo1r4WVgdpGmqv9irrkHaYvmvh-HevUF7sRFT54mRlP1dhy8wEjIn8fGUOJSvjgY1TokiDSKOMfNsREK49BEAfnjHyZHLr8v5tuYbZ-OHwtwr1Qnt1I4sdWOMBaYstjmyQkGu9ptMS9hcJNvmPm0fpr_vHbLghZCby8SmM9G28BmnTP4EQWuG8vROwuAqk6iMkdJeMgXOXzRKvnqGWusx2vtINXJUTdEMp6gwlfTz5JNknDbIPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کاخ‌ها و دروازه‌های تخت جمشید
۵۰۰ سال قبل از میلاد مسیح vs امروز...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125540" target="_blank">📅 16:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGDJiEEihDVnGj2DJqHp3PlhmndUYQJYlCcdP7Zy8TlKxhxvZLB0T-4H3-QAM8j7TCKCnuDiTRfIC8QQtIc-Dv3t1TV_fYo_kTZTLPsWPnSJIqwrMuxpTbyOwfVaruKuerH3avlRqsQ2mzGEKHkS--3rQRWC20-dJxBl2X6X8FMN-B_ypzhvkoMaNw1nynqJC6Kns9M6wgmRNyhWcwp2jSrNd9i5DifIaGNPJc4NUbnthR7eu6E6gnr_CFyr5BBwyOx5P4uZJXwO1kSq3QG4csfBfyDGJZrYJtWE4fI1acJU-i4daSOrE4z6k02uVfUI0BF0lPWAQStH5FiZLKDdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ : پیش‌تر هشدار داده می‌شد که بسته شدن تنگه هرمز یک فاجعه تمام‌عیار برای اقتصاد جهانی خواهد بود؛ اما اکنون مجموعه‌ای از راهکارهای جایگزین توانسته اثرات این بحران را خنثی کرده و مانع از عبور قیمت نفت خام از مرز ۱۰۰ دلار در هر بشکه شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125539" target="_blank">📅 15:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125538">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSMfRatoZRerlYrCC45QPIMT5ZDw1U4SvYzS-PfAuCrYa-2GGVU7OyA8c1VggjNBmdZ_kkOer9-TfK6asQhZecVT0WQJzY6rdqvolwEOS3XuPKX_DopL1efCgYA5NAjhv0uQYFUW51DWCu8K6uC58h4vpES6zfZ8FQmllnKZDBDp9yNeyXqnN-di9AY01zyjJkurdcNSMlFPaS9W1mQxNyJqFyeZt_hDzmL5ITK_KiXcIv8p8XJ_optjjztgzVkBBKr0Z0mBkCfZrmXc-_-4wlESGhMoY_c-A5ysxERlHmRlvnD0D2iUdSPM3tKDuszio9_1cqwhgA8Lh3BwnkJyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستاد کل ارتش کویت در بیانیه‌ای مدعی شد سامانه‌های دفاعی این کشور امروز موفق به رهگیری و مقابله با ۷ موشک بالستیک شلیک‌شده از سوی ایران شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125538" target="_blank">📅 15:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
صدر اعظم آلمان مرز: آمار مهاجرت غیرقانونی در سال ۲۰۲۶ نسبت به سال ۲۰۲۵ به میزان ۵۰٪ کاهش یافته و نسبت به دو سال پیش بیش از ۶۰٪ کاهش داشته است.
🔴
ما این مشکلات را به روشی بسیار آرام اما بسیار مؤثر حل می‌کنیم
🔴
ما به افرادی که برای کار به آلمان می‌آیند تهمت نمی‌زنیم. ما از آن‌ها استقبال می‌کنیم.
🔴
ما می‌خواهیم آن‌ها اینجا کار کنند، اینجا زندگی کنند و در اینجا ادغام شوند.
🔴
این دیدگاه ما از یک کشور باز، لیبرال و آزاد است — نه انزوا، تبعیض و تحقیر شخصی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125537" target="_blank">📅 15:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C28C5mje19vK1r630f0IdeLHxvwBHgZ23Kt-6V6-9c8GlJnrfsZxGmrasazmBCyIcm6PwZzt5dEiahW0MNQPGyyrzVWSRdBJ59jhNzbTSihoTRVpzJs7a5eMpZgj6oKkTr51M-44PjvxVowtTW4l0DkUe4e29ULgTUmEspdwmbAjxZvlUQjYr1Yd7ZB17VLIA4bx9DZfWqe1ZW5gYa6XZVVqU5bWVtyLFLf15lrBTt46OZDplzPkKrCXRJdxc4tQsRnK7r6Vq17xEUSY-jYNtOzHWSUT0oaBRELRTtqIwpCd6sQJVzlTRKNIs_MIeehJXAY7q9dE90HHT977JIGqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده فروش نظامی خارجی احتمالی به ارزش ۱.۵ میلیارد دلار به نیوزیلند را برای پنج فروند هلیکوپتر MH-60R Seahawk و تجهیزات مرتبط تأیید کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125536" target="_blank">📅 15:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=XvRpqLJTZGB8pY7081csxqFPThwib7mZhlPNSRz6nMOcB3WHFNMCIPr05JoJG76MAuY5kgDu78gfvkxpfh0wabJuGf61fjhmgZ0bf22LW1kJ6ZIAUZxE-ZlJ-Bl2NjLzY4__LjQlsU-0fXDGFBO6DPLNDTnRPkgtiJ0IUdOWTmD9ZZK7HC4PKks2_NBE7Xd6D1Jb_9Uwz5Ft4Rozhr3kh182eAWtg8K3Sx_HFB0bkDkgRPhCF3N_NKwXI7gqgbLbHBXNS7F2SgQ9K5i7-i5IO8dhtQK9ZVXl7cF9dqlu2ngpVmkr979tWongH4NUnOOz8uMasPvhN3pKw-fTIDY6Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=XvRpqLJTZGB8pY7081csxqFPThwib7mZhlPNSRz6nMOcB3WHFNMCIPr05JoJG76MAuY5kgDu78gfvkxpfh0wabJuGf61fjhmgZ0bf22LW1kJ6ZIAUZxE-ZlJ-Bl2NjLzY4__LjQlsU-0fXDGFBO6DPLNDTnRPkgtiJ0IUdOWTmD9ZZK7HC4PKks2_NBE7Xd6D1Jb_9Uwz5Ft4Rozhr3kh182eAWtg8K3Sx_HFB0bkDkgRPhCF3N_NKwXI7gqgbLbHBXNS7F2SgQ9K5i7-i5IO8dhtQK9ZVXl7cF9dqlu2ngpVmkr979tWongH4NUnOOz8uMasPvhN3pKw-fTIDY6Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اطلاع‌رسانی عجیب مجری صداوسیما: مرکز ناوگان پنجم دریای آمریکا مورد اصابت موشک قرار گرفت؛
نه ببخشید اشتباه شد
؛ صدای انفجار در جزیره خارک شنیده شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125535" target="_blank">📅 15:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ    برای ۱۰۰ نفر اول و یک ربع بعد
😍
❤️
🔥
آتیش زدم به مالم به خاطر عیالم  بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
🫴
ویژه ۱۰۰ نفر اول
💥
بدون محدودیت…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/125534" target="_blank">📅 15:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHvUz67QqPXuBEOympxb_88uVEzkKMceRbqxNxhVQ0eaSj4BkO1HuvkwNkfK_1q6T7INrL8QknPJL2pI1WsL2zvh-72kOb8o72ZuQQ_z4FjawptzmFb9dBdEFPqxpTaugdGcfn1cB3QdtCqSZuJ8okMc1yWzHaEhF2I3f_fFgXVXCc8UEAMobZQqorXKRW7DhPUrAfyc7fK_rmlY3N3UBt6ij8pG1Ds2YyQYPdq-N2mrYl5REjsjrTpvOlyxWRye4lUtb8Bvp7yUD8rJF2MGRuhKjfPBPK6mk7oV_H2H_CmzDEkkMxHotKir9siB9zVHxavI7DhJURdtiDNdjC3MEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
برای ۱۰۰ نفر اول و یک ربع بعد
😍
❤️
🔥
آتیش زدم به مالم به خاطر عیالم
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
🫴
ویژه ۱۰۰ نفر اول
💥
بدون محدودیت حجم
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/125533" target="_blank">📅 15:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125532">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFUWvuM43TKnQKETj2V9JjK0y4fq4ftc6L9aSEhMDJ3nSB_YesPN0NQFk3UZSg5MvsZ_LicOPtZT7F7WyksSdZon-rj1IC1vF0c4IeBPaI--Q7CnXjuflQvwP-4cVgdVND3i29H3hidi966TFCcv6Vc67lo-XWkslvY26RQeaxDKBPrrEakvIWgdiURZxt90zkEhVEHvRUfgQUkDX_CnTDXQaIcAiosG5MCxGqjZpFtI5LtCh6BY8t2khmCCbF5XzL2_ISGi6F8n-BbAvaHV8YdHDdjwaVBS89ZtU0oSQvBU1D8z6L67yjnVwPedXhS3LKjtaJxT-sGI-y0uHsO01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ : از ماه می ایران نتوانسته نفتی را از طریق تنگه هرمز صادر کند و ۸۰ میلیون بشکه نفت ایران پشت تنگه هرمز گیر افتاده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125532" target="_blank">📅 15:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125531">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری / الجزیره به نقل از یک منبع پاکستانی: وزیر کشور پاکستان در سفر به تهران حامل نامه‌ای درمورد پیشنهادهایی برای بحث منابع ارزی مسدودشده ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125531" target="_blank">📅 15:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125530">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سازمان اورژانس : روزی حدود ۶۰۰ تا تماس مزاحم داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125530" target="_blank">📅 15:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ459Y7cJP38PHx71VFI-JF7M_ZSIobV-t0IvxPk9g93ZCgbaH6IwyNfFVOxWoJSeGbwY9GIhV2upzDDl4GD58cKv3kGq_GVfEtAfPiZ9pwTyZgkjK_Cb_ysrycVkeQ5TY0LA7Yci8oEKavA4F-vKRi0HNy47vTtWz1kECg1QBFHn_dT8Pz1bJmV2HGsl5OvR06yB2dF_4w4nxd1m0ewEwExpxlUK4v5iqUQhqk-dE-3XcPfZhhmnEQgqJNLVs_Kg08_F-TQPex5CtBCzOragKpoVnU72IyNoWr9R7L1Gux-XKxpjyGIs_OA9CjSNyC0jzddE7-f_bShurr3V9Z1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیرحسین قیاسی: سکوتم در جنگ اشتباه بود!
🔴
حتى در صورت سكوت هم معلومه كه من مقابل كسى هستم كه بدخواه كشورمه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125529" target="_blank">📅 15:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbYGtnLWdkBaBtuGfoHi2ezVyrIy5BTT5aiSWvuTT8WCv-u41MjE5TxXb9E8B76xTrMYwSRm_QrItDZeuBdS4FFJTBbvMhRo6zEQUSVCOE-ooxc_yjGIAsDP0fZgTaHhyvPIHjApuljt3KYX9myOjwIBRC5h53uccDA5P7VQ3ZemkWWniywNZOO_2WYXPYiQU-l8fsoyIVyegtgIJgLbg9dkZJLFSVA2ulUjWuyLzsxzKlE7iuG3JjGxVwEJhtHEtLlbrapHVr3NRR7HoaTN9_QplQ5El-Iz7K1X77e52Q_91Demm4vyTN4q7kcVENPZE9ZUwhN6vD7xZEBFatp9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزرای کشور کشورهای عضو شورای همکاری خلیج فارس (GCC) جلسه اضطراری تشکیل می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125528" target="_blank">📅 15:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125527">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=fU50Hs6QBDgx7xorn-yLgg_imy3Nw9IVoJNMQRFMHw2IesPxAI9OlELuUEMktkYkTWdbJTVd1WRCwHE0C6meOKme1JKy_j9g7SJcgCC5ThIGCyEyGTbsVml0SZJ51LV3c8VSwK4xKgEbTvmWzcwg8l7YAjFo3yglRrzYDbtTlv2JFY1J1RoYcC1eQs87y_z2mc8x8ksfNQgNV_ThRhjpFNaTuUMCocJW_HB-hi0BcIKAWYZZrG2Np-qY_eJht0dai_wbkChqEltBr14nt910R21Y8-oQQUZs1HjjnJ763l9t-eqqC0OUUucCXy4PCPiYNr7C_azXulU1BctXf9bEag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=fU50Hs6QBDgx7xorn-yLgg_imy3Nw9IVoJNMQRFMHw2IesPxAI9OlELuUEMktkYkTWdbJTVd1WRCwHE0C6meOKme1JKy_j9g7SJcgCC5ThIGCyEyGTbsVml0SZJ51LV3c8VSwK4xKgEbTvmWzcwg8l7YAjFo3yglRrzYDbtTlv2JFY1J1RoYcC1eQs87y_z2mc8x8ksfNQgNV_ThRhjpFNaTuUMCocJW_HB-hi0BcIKAWYZZrG2Np-qY_eJht0dai_wbkChqEltBr14nt910R21Y8-oQQUZs1HjjnJ763l9t-eqqC0OUUucCXy4PCPiYNr7C_azXulU1BctXf9bEag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فوران آخرالزمانی یک آتشفشان در هاوایی
🔴
طبق اعلام وزارت کشور آمریکا، فعالیت این آتشفشان در ایالت هاوایی همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125527" target="_blank">📅 15:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125525">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiVSr0dJkXYYHeifbGYzOTk8u_UTMXUBmp7aKFzQUrwxW_vBFVlaF8urgRri12qmcZvEHVjvnx7Mt4ph4SRMCKu9v_dxsRGdzaM7NFFjioCM3QW_AyC2gGK6_1LeriFhQCpquVcA-L293jDcwM_GEBQB-iFNZQFM6iKf_wFecCypGimItPeg81CABHP1yU_9zfDkOjo7aRK_nG8oBoxzxlBF2JLlY7Hrrp9zDu3z6xsQ5pvhW3Egq1LKItmGoiybC99mIsA5LIsAqHZZovU6y7KHmet6yBE_lkecqb6i00g-FsYxRR29-8mqLnBxIX8Sz0BhDVPziTws0gOzANbhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25126b98d.mp4?token=AYSrVuWR_kxz3Y3Dub6dyHioNUianu5UNxzlv7wXAB3kvH2njtZ74bZO6lksPnKQ1BCBbep_6fDDVlNvvVd0ldCLnGh3xa4vwBAlhTDGNV45rfKB1ZlaQDYsSQ7-d0qIBNNQs5lNjq61oytowdKwlA_5wg69CgEHi9jbDZiDEk-jUJHzWYTT5HjKvzGDP7_MGO-lzxTyITwrtSUjL_LeSoklcMRA6DG4PKPZKjImlMTvr6VT4loirBirV9X48NoDYiFeQYtJtkDYGQfCLyg2BkEYnQbLm_1Uxud4Ahqx4-YG6UG7BcxLzoBdb1TIRZG7zj6H2uU3ibMz7D9Xn0Czdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25126b98d.mp4?token=AYSrVuWR_kxz3Y3Dub6dyHioNUianu5UNxzlv7wXAB3kvH2njtZ74bZO6lksPnKQ1BCBbep_6fDDVlNvvVd0ldCLnGh3xa4vwBAlhTDGNV45rfKB1ZlaQDYsSQ7-d0qIBNNQs5lNjq61oytowdKwlA_5wg69CgEHi9jbDZiDEk-jUJHzWYTT5HjKvzGDP7_MGO-lzxTyITwrtSUjL_LeSoklcMRA6DG4PKPZKjImlMTvr6VT4loirBirV9X48NoDYiFeQYtJtkDYGQfCLyg2BkEYnQbLm_1Uxud4Ahqx4-YG6UG7BcxLzoBdb1TIRZG7zj6H2uU3ibMz7D9Xn0Czdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیفا ایرانیان را از آوردن پرچم شیر و خورشید ایران به مسابقات جام جهانی منع کرده است.
🔴
یکی از راه‌حل‌های هوشمندانه‌ای که ایرانیان ارائه داده‌اند، ایجاد اپلیکیشنی است که به آنها امکان می‌دهد پرچم را به صورت دیجیتالی و گروهی نمایش دهند.
🔴
از ۴ نفر تا ۳۸۰ نفر
👑
https://www.iransync.com
#جام_جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125525" target="_blank">📅 15:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125524">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزارت خارجه قطر: بر ضرورت دور نگه داشتن منطقه از پیامدهای حملات بی‌دلیل تأکید می‌کنیم و بر کاهش تنش برای بازگرداندن امنیت و ثبات تأکید داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125524" target="_blank">📅 15:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125523">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
الحدث به نقل از منابع ارشد پاکستانی:
وزیر کشور پاکستان پس از دیدار با نخست‌وزیر شهباز شریف و مقامات ارشد، امروز عازم تهران خواهد شد
🔴
نخست‌وزیر پاکستان دستورات ویژه‌ای به وزیر کشور خود درباره مذاکرات بین ایران و آمریکا داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125523" target="_blank">📅 14:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125522">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سرتیپ ویسام صبرا در حمله‌ای که صبح امروز در جاده خُردلی رخ داد، همراه با تعدادی از نیروهای نظامی کشته شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125522" target="_blank">📅 14:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125521">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
منابع رسانه‌ای و وزارت دفاع بحرین از وقوع چند انفجار درپی حملات موشکی و پهپادی به این کشور خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125521" target="_blank">📅 14:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125520">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
اینترنت  دیتاسنترها همچنان قطع است
کسب‌وکارهای اینترنتی کماکان با مشکل مواجه‌اند
مدیرعامل شرکت آسیاتک در گفت‌وگو با سیتنا:
🔴
برخلاف برخی اظهارنظرها مبنی بر بازگشت وضعیت  اینترنت  بین‌الملل به شرایط پیش از دی‌ماه سال گذشته، دسترسی مشتریان مراکز داده (دیتاسنترها) همچنان برقرار نشده و  کسب‌وکارهای اینترنتی کماکان با چالش مواجه‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125520" target="_blank">📅 14:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125519">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سفیر چین در تهران: همه طرف ها باید به حقوق مشروع ایران در تنگه هرمز احترام بگذارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125519" target="_blank">📅 14:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125518">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5580004caa.mp4?token=rLT6CKVHCdt7rS9tf40vZ7yVyL2Fl0Ucl9tEjjmkak9te3-4xqOOOxSNM-N-Sy0XdaOSykrHhOzH9Xtk5S3EojTVqYNWyx7hOzrkPbsqSatUHykBKW35O3XiEOmvsuIUnrTcJyzlPmd032ulP3LNNlp7ljCPi9NPm1APso0CBfBFevEIXDd_VpQqLkBDdIWZrXp3unL3rmNPm6rboG6UMc__fbHVDl1LDBAp6jGNLntizO8Qn38AYIojBl8kkbjsWaEK2Vv0bGMEsudykv63pnlK-w960HKvKsoHqilxXrqWPo4VoWT7lxzu9ehv3r-tnRjjlrN57QyrpisMvt4xDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5580004caa.mp4?token=rLT6CKVHCdt7rS9tf40vZ7yVyL2Fl0Ucl9tEjjmkak9te3-4xqOOOxSNM-N-Sy0XdaOSykrHhOzH9Xtk5S3EojTVqYNWyx7hOzrkPbsqSatUHykBKW35O3XiEOmvsuIUnrTcJyzlPmd032ulP3LNNlp7ljCPi9NPm1APso0CBfBFevEIXDd_VpQqLkBDdIWZrXp3unL3rmNPm6rboG6UMc__fbHVDl1LDBAp6jGNLntizO8Qn38AYIojBl8kkbjsWaEK2Vv0bGMEsudykv63pnlK-w960HKvKsoHqilxXrqWPo4VoWT7lxzu9ehv3r-tnRjjlrN57QyrpisMvt4xDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی از احتمال بارش باران، رعدوبرق و تگرگ در نوار شمالی کشور خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125518" target="_blank">📅 14:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125517">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ به میانجی‌ها گفته ایران باید زود جواب بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125517" target="_blank">📅 14:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125516">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
غریب آبادی: موضوع رفع تحریم‌ها و مباحث مرتبط با مسائل هسته‌ای در مرحله دوم مذاکرات قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125516" target="_blank">📅 14:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125515">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری / الجزیره: وزیر کشور پاکستان در سفر به ایران حامل پیامی برای رهبر ایران خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125515" target="_blank">📅 14:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125514">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجارهای کنترل شده در بندرعباس به مدت چهار روز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125514" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125513">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxomYn7VVHEnudxlmqsn_n2pNgpHFHuDUKTrcSdt3jGvTQ5MCcJIyYb1OJBRiMFBxrE2F-o429U1bKcpenscHV9cCtcwbelwjQ9tvLtdbxu-TgydarfTlf0ub1AvzYGC47PHSmBvbGOu4LUQS_7b7epOotxzVVkwnmfL6QVYRn1MyIWd2eTOisjRno_B4FpDoQ0qFEVFpwCrqs6QHzl-QoLndEp90WgvUZmxWccbqcO2KasafFjA4z6isQvdxRkckEQEn9_tBthtnjZMt-d2DiTncWnkDzBzpegUd8tvMfXCMxjaD6xqZj-6ZBU1taN0MqVBN8JLwTNWsPF0ZMChFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: نواف سلام، نخست وزیر لبنان با اشاره به اینکه مشکلات مردم جنوب، مشکلات تمام لبنانی ها است، خاطرنشان کرد تا زمانی که این منطقه در معرض تهدید باشد، کشور در ثبات نخواهد بود و دولت از حق لبنان در دفاع از حاکمیت و امنیت خود کوتاه نمی‌آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125513" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125512">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
دبیر انجمن صنفی شرکت‌های حمل‌ونقل ریلی مسافری: ۳۰ درصد قطعات یدکی قطار وارداتی است و دستمزد نیز حدود ۵۸ درصد بالا رفته که افزایش هزینه‌ها را به دنبال دارد. قیمت بلیت قطار در همه مسیرها ۲۱ درصد افزایش داشته و از فردا اعمال می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125512" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999b104f0a.mp4?token=TYUG3K290Yq7GMWouQ3cpeb7OQ9tiiB6MkUlu4KSKQ2u7qR99F4DNVyCjrGTBh5okPJBfdh-tc1tNWckrJMuPqazMRU92-vewARFhcnzpluomz9Vl7qZ5_0cDGynjIWtoCEL9KRJ2iqAtn4BI_Q6EE3AWrO64kDplr2cLgiZgt9AF4-Tu1J_Tqvu30JkqTSgQemUpfeCwXCNvvyIFSx7AmnsypXTDzmQUuIvTZnjNzg8465iESB2ID1IweYNij4dSu57vh-4zycgnLzHDs6sSl_k7vWce0_tA69xHHfHOJ1rqmHq8VT0QzgGWxZWOOAabi5_774QoismcZ_7C8RKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999b104f0a.mp4?token=TYUG3K290Yq7GMWouQ3cpeb7OQ9tiiB6MkUlu4KSKQ2u7qR99F4DNVyCjrGTBh5okPJBfdh-tc1tNWckrJMuPqazMRU92-vewARFhcnzpluomz9Vl7qZ5_0cDGynjIWtoCEL9KRJ2iqAtn4BI_Q6EE3AWrO64kDplr2cLgiZgt9AF4-Tu1J_Tqvu30JkqTSgQemUpfeCwXCNvvyIFSx7AmnsypXTDzmQUuIvTZnjNzg8465iESB2ID1IweYNij4dSu57vh-4zycgnLzHDs6sSl_k7vWce0_tA69xHHfHOJ1rqmHq8VT0QzgGWxZWOOAabi5_774QoismcZ_7C8RKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امروز هم در سراسر کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن و حتی جمعیت از سه شنبه هم بیشتره.
«خسرو پناه حیا کن، کنکوریو رها کن»
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125509" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ697uIi4ilC2JYfY6EVdlZZqn2QrLuXvTrP5Y0jv-CpcjbDGYzYzcIxvffxv6PkN62pPxlO-f-rNgBKWyONZJLhq-nlHMQL0SrvxeVdryxX8TtMMEtahp1ijt6FWsQVNX5cl59J5vYbpj2mSsFu0p0L1FTEQ9Rjk7tcXXBmWblfMc20R9HYU_wLaBP2okjJyWKlAopKkF3FQdRr8yvmFIRPusqrEkhpOdEoxHYQ5Mq83WNEdICAxHdM6vsDY6PvnGAsg3IKjrGEF95EGN-BGyWTDliyhViSRTSnD2_vGNzTnYjPwGUUbNSXch-bqi0bTJruhytcYNPAG9t7W4BreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داخل امارات یه منطقه ای هست که جزو عمانه و داخل اون منطقه یه منطقه دیگه هست که برای اماراته!
🔴
خاورمیانه همینقدر عجیب غریبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125508" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125507">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c6f0cb3e.mp4?token=vFy9rk8o0z8yUxgUDwopDOIebRQXuiG7oCBPb5VXyY_xv2NooSuUeILn8Vqr6sLjVU6kR9yuIT-8snY3Nqa_IcYv1xZ-28DGmyEMQnYCa5e8qRv9Ei_oBMrH8yaBPk4iMNMay-0KeRLDZ5SMlU0ebWC3UWxlJ-uFiAVSI2c4gQOnesORqaGtIY8M8HBuxJVP_Wft66ywDKF6DAFkI_EVH3VlZRCew953ztvwOMzk2fdtQ8p-oaVXaraDCi_XwRxC-3Zvw-FoOAu3QH_WeHEq2h9EzPwzrreuxL-WmwnpSdf-5S7NMI39bqqMamZS1L3o5OBibNkEUGQJJxdlul7EXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c6f0cb3e.mp4?token=vFy9rk8o0z8yUxgUDwopDOIebRQXuiG7oCBPb5VXyY_xv2NooSuUeILn8Vqr6sLjVU6kR9yuIT-8snY3Nqa_IcYv1xZ-28DGmyEMQnYCa5e8qRv9Ei_oBMrH8yaBPk4iMNMay-0KeRLDZ5SMlU0ebWC3UWxlJ-uFiAVSI2c4gQOnesORqaGtIY8M8HBuxJVP_Wft66ywDKF6DAFkI_EVH3VlZRCew953ztvwOMzk2fdtQ8p-oaVXaraDCi_XwRxC-3Zvw-FoOAu3QH_WeHEq2h9EzPwzrreuxL-WmwnpSdf-5S7NMI39bqqMamZS1L3o5OBibNkEUGQJJxdlul7EXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
«هویت ایرانی» ما بر روح و‌جان ما حک شده! غیر قابل نابودی است!
🔴
ایران بر همه چیز الویت داره.
🤔
قابل توجه عرزشی حرام زاده که از تخم عرب های سوسمار خور عربستانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125507" target="_blank">📅 14:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125506">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=ojM8QB905N1YAKuM27PDIalD_TqwsCx3zWGwAEw4MWCSyq83_9cSUzSNuIHlyiipnBQSRcDcYjsnhThuLuoq2gJTKH-_TlSZKieGKLbThBkQ30LFc2klH75pbaHsUM3kYwFA9-G_db3nlhy-exyaKhVsDm_zXMseofTxWCI7SJK-plMaYLVk4DJWvod_g6nfLmpI9vL0zZvMT4wqYiYar2qJBz8A297e6Bb0HzN9zFr2AwBsQPZ6pIOY_oMbHhXBnpNsriwfmxoHdsGr2IhjdeVieAXENJGvGm1KpUi8aEtM8zvjJkpVnfeK3te7WFK08wsXOlNnkrW207lWcvH74w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=ojM8QB905N1YAKuM27PDIalD_TqwsCx3zWGwAEw4MWCSyq83_9cSUzSNuIHlyiipnBQSRcDcYjsnhThuLuoq2gJTKH-_TlSZKieGKLbThBkQ30LFc2klH75pbaHsUM3kYwFA9-G_db3nlhy-exyaKhVsDm_zXMseofTxWCI7SJK-plMaYLVk4DJWvod_g6nfLmpI9vL0zZvMT4wqYiYar2qJBz8A297e6Bb0HzN9zFr2AwBsQPZ6pIOY_oMbHhXBnpNsriwfmxoHdsGr2IhjdeVieAXENJGvGm1KpUi8aEtM8zvjJkpVnfeK3te7WFK08wsXOlNnkrW207lWcvH74w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: مرکز ناوگان پنجم دریای آمریکا مورد اصابت موشک قرار گرفت؛ نه ببخشید اشتباه شد؛ صدای انفجار در جزیره خارک شنیده شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125506" target="_blank">📅 14:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125505">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy2fJHcdtrmdCdpkJDn-GuqgBO4b2M_vIx8aPdcBuckOzMrSLDtrpIG7Ur-Pi_PWvRij1FXxoEnXCmZNXD-A9uDKBA9TkhrAKh2HooIyy2sgmyz7t_43cyt7uEUBSL9a7JkAxwqVGX6rd6GWsDZGsn0l5awmeFjBf3P1phZek7goBYnQSj3lTOJXdkr2aWsSPzOTSv8QkAEyzGICuTXqz9mDlgnvSEdnRzxs1zGEZ9p0sDjoGOjBF8ZDswDqCnslztwf2By8jDZuHQ09a7ZehyN0YrbaJtX420j4Ru_PN4C5eGUu1dPOBkYunWjB2P-MS4lJYmT8HQZwbtasW0laKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز پیش گروهی از اتحادیه معلمان مکزیک، ساختمان آموزش پرورش در مکزیکوسیتی را تصرف کردن و خواهان افزایش حقوق شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125505" target="_blank">📅 14:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125504">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد که نیروهای ما بر منطقه «شوچنکو» در اطراف خارکیف تسلط پیدا کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125504" target="_blank">📅 14:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125503">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
فارس: ۴۱۷ میلیون متر مکعب آب از افغانستان راهی شمال سیستان و بلوچستان شد؛ یعنی کمتر از نصف حقابه ایران که در سال‌های نرمال آبی پرداخت می‌شود
🔴
فارس نوشت: افغانستان یکی از پرباران‌ترین دوره‌های خود در قرن اخیر را پشت سر می‌گذارد اما تاکنون تنها نیمی از حقابه ایران از رودخانه هیرمند پرداخت شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125503" target="_blank">📅 13:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125502">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بحرین: ما مورد حمله ۳ موشک و چندین پهپاد قرار گرفتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125502" target="_blank">📅 13:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125501">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وال استریت ژورنال: دادن پول به ایران برای ترامپ خیلی سخت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125501" target="_blank">📅 13:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125500">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: امتحانات پایه‌های یازدهم و دوازدهم نهایی و حضوری برگزار می‌شود
🔴
کاظمی: تلاش می‌کنیم امتحانات از ۱۳ تیر آغاز شود.
🔴
همه ملاحظات لازم برای کاهش نگرانی دانش آموزان و خانواده‌ها رعایت می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125500" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125498">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gOovc0iHUjbPHasXqax7lGPmdunAKtetZo4KxtiuiFeHbc1DmiI9Y_CwfPx7ppkzLr5Ymg2g1JWLFwFnRUvIg0vgsfn7P1wiMR_zOMNm9TkdfyeI_Xvko-LOTaQewVIZvLS3jSZOSS2aodPkaEEQYcUWZ_X5-YI_PnqoR7CjCKo7Qk60dO4AH_QUxUzo_t7ZghLYs3EzKrvUG4zFNInmdPJ6UAGg7EkowmEH9IvygV6R9EmZbaY_xdoDh0lfvPp5uKiEdw7FuqcYraJxoxrgyQWzAqY04SCjbaeN8oK9c8H4F0aYREqA6Ad64qYgctX-wbZIr2sCZ4LO9bBxR3UmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ww-j_Elkw03YsxBdGmFeDcbINDfFp898TbOInEX9514CdiJ29E5GmhGBkWMzQBdyx7WzW2kZeYSgMFcA1DP3N_DN3-sIIK1YxbKRpCQC5X3-RKDlK7IjctygoAIpni48vqQexvNMiLNkdwWqzs6aKr5_e7PQlRKrBWpo0NGAb1OsFNNWFCeHm-DQeJB_FFHhtmlyDRDj6ZzbpkozB1ONbnVrFpOOYQXbpcaYC65f86sRozjrVyT_eqzFgBFDu7tqxavz2MiegPgCCGNesru8CGs4MV8Q4WrwjNz2txs1e45YPftU3Vw31TfXDh7vGswhISLqo0AgPENnvfHbkUDLtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آتش سوزی منتسب به اطراف پایگاه هوایی استان شیراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125498" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125497">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ایرنا: وزیر کشور پاکستان امروز به تهران سفر می کند/وی در قرقیزستان طی روزهای پنجشنبه و جمعه، دو بار با اسکندر مؤمنی همتای ایرانی خود دیدار کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125497" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125496">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125496" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125495">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزارت امور خارجه کویت : ما حملات مکرر ایران، که آخرین مورد آن امروز صبح رخ داد و نادیده گرفتن خواسته‌های بین‌المللی برای توقف تجاوز بود را محکوم می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125495" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125494">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
العربیه : پیام‌های بین آمریکا و ایران از طریق عراقچی و ویتکوف منتقل می‌شود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125494" target="_blank">📅 13:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125493">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKwgtIWPs0JAELeWHAweCKhPC8F7k7lhGqjgvFIaaT37liIB3Vj70zNDVHG_ZoM4ndP4z_Ezt2u6ldRrVxSx0GY5ZsC6QeaU0nV5KxUWaWucvVGUm4tkBK5ecwFG0vU3wurvH46GNZHzYhMdQEe8j_sNCONT2t3lDDepdOT8RJyHKbuFQmOApS-Tl5aDEvAGQMOpeXekqWd332cjBX8_GvV3quPe99_ySeIbLdarydy4shmpd4so5r-tGN3PTTkBFkWwHFrATrc07YpHKiApZRHK_bPxLQJxkk4FJa6VvsKwgz1Ul2kT9OPy6gbm9CbV1Kjs8wnVU7Bi1aECtlZ0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه
:
پیام‌های بین آمریکا و ایران از طریق عراقچی و ویتکوف منتقل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125493" target="_blank">📅 13:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125492">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">⚽️
🇺🇸
یک مقام آمریکایی در گفتگو با رسانه اتلتیک گفت:
🔻
ویزای ساعتی بازیکنان ایران و اعضای ضروری کادر فنی این تیم صادر شده است ولی ویزای افرادی که هیچ ارتباطی با ورزش ندارند برای آمریکا صادر نخواهد شد.
🇮🇷
اسامی افراد تیم فوتبال ایران که ایالت متحده آمریکا درخواست ویزایشان را رد کرده:
مهدی تاج - رئیس فدراسیون
مهدی محمدنبی - مدیر تیم
محسن معتمدکیا - مدیررسانه
مهدی خراطی - مدیراجرایی
مسعود اردشیر - عضو اجرایی
مهدی ملک آباد - رئیس حراست
سروش سلماسی- آنالیزور
مهرپویا اسدی - آنالیزور
رضا جاودان- تدارکات
حامد افضلی - بین الملل
سیامک قلیچ‌خانی - رسانه
امید جمالی - رئیس بین‌الملل
🔻
تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
@AloSport</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125492" target="_blank">📅 13:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125491">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سازمان میادین میوه و تره بار شهرداری تهران: قیمت مرغ تازه در میادین و بازارهای میوه و تره بار، بسته‌بندی کیسه‌ای( پوشش کیسه نایلونی) کیلویی ۳۵۰ هزار تومان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125491" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125490">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">😍
قبل خرید، رایگان تست کن  ما کیفیتو با حرف ثابت نمیکنیم
😉
با تست رایگان ثابت میکنیم
🔥
@Netaazaadbot  @NetAazaadBOT
🚀
VPN پرسرعت و پایدار
📩
برای دریافت تست داخل کانال عضو شو
😍</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/alonews/125490" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125489">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MF7zvvXdWbmhLrh8huj3VI04WpsWJaEunRKtGLCG5B5SfRMOEB0RjDJx6DSPvMkFdN7OFfCszAaaPgrKnJwhyW2HOYB9WZaLir2aMJ0-oIQBrRUJxAC-59neAGvMeN-wfVJvjzik4V01N6BuueI8Jf43DlqWIr4ydhH3BLjBuLXdVuK1dvCvHNUk6WPhgKbDLxL5I1X1UVismbM3c6c0f1ROFe9B_89CSQjB3w6sVuNvEGJKAhShbLrdIzpgAb2CCEsABCesWMh7ZK7oSTiTA55vOZyq05bUzJ0tRQbKQxiZ6g0-b8kw90VIR0JqDK09g1lDJIKOK_FMJazCaljWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
قبل خرید، رایگان تست کن
ما کیفیتو با حرف ثابت نمیکنیم
😉
با تست رایگان ثابت میکنیم
🔥
@Netaazaadbot
@NetAazaadBOT
🚀
VPN پرسرعت و پایدار
📩
برای دریافت تست داخل کانال عضو شو
😍</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/alonews/125489" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125488">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ژوزف عون، رئیس‌جمهور لبنان: هدف قرار دادن یک گشتی از ارتش ما توسط اسرائیل، نقض حاکمیت علیرغم تلاش‌های ما در مذاکرات واشنگتن برای توقف تجاوزات است.
🔴
از جامعه بین‌المللی می‌خواهیم مسئولیت خود را انجام دهد و به تجاوزات اسرائیل پایان داده و احترام به قوانین بین‌المللی را تضمین کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125488" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125485">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCEzXJ18kiQh2nTh_pNP-PawWdETaLm5V8spBsws2eD5LSwZzKVWUNn4ZlVEdO76_ODbYV5yz8S9XXq_p-qoqhhVNEvIsTKdfpJloSimp_EnIy8wlgXfYeoSXFpjhPAxHtBtmMRiU0JtCOzST6ORBmPTpG5nScLjx8zX495_KYSy5eWPRQ6Eu1WzqYIZqkKZpPXKlWIohlYwu93qfg-WrYaMct0B4Vut7CXqqhUHFRIqgNZxwZsqvtmPBku_QlB0S-SJZnSxQiyaemx_WrZSs4BEZkKVzjNUGdPSGIssquVS-_L2SXP0wn_bUjJIO_4oVNnsUYlQ3ia4XMXM37-qdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LihQq_Z9Ph1X2tAukGBku4E4u2HqIu58NROmCfFgU1rmVf_B0S7UUPfv769PW2PG9jOA7iOU39b0qC4q6F07KK_KEiSzi2GplTdX42X3MoO7aVpeJAPysMT1XSV3HiCMkgGVuhTRicM9S-IUYJ13HjJEPbZTddyP6vICB52GgxnKj62e5ezneYi9tfF4zEOTtXphwxakyEf51AEKfvoiytajwOFEZA6r5_zeRsuh8mc4LOkpDtFABqp43XeVMQN8iykbacfYSTKIuVDsYu8YC_ZOQZS9MGUWZIK9XlzwHX7MMriyMfabdKvSQwG--vGITCu0abXtOCSZpvzTshJ-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBP0zLNESpZ-XoIWiDOb9IVWN-0GdfNnzz3LG38isWamRuj8mbsb64tx3WpNz2B7gglGCo80UwJ1DFtIvjd7MnzNWZnvTCcD_Nchrjr9UTid4hdVtQ0M-6UZRfLf1oOd6MyriORuKNmDGlfTpbRZvZjzvsJnhIoc4TtDpQTVFbqyxz1yxH19Ta_XiBUrcYVrZrNblOjH8ZfKy5keWc8JWSBcpJRIJAczH60OBknOZJWS5qO1FgHCrC19mlsAjrdYYjUug9x2BmFC-6kPS9d_axSPUOw7VoP2t0bvDf5Kz-V-JU4Y7_X3oIpXvzGiE5H8ERdywUC1VbHCoelfDe5ylA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125485" target="_blank">📅 12:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125484">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نواف سلام، نخست‌وزیر لبنان: قلب‌های ما با جنوب است و دولت شما از حق لبنان در حاکمیت و امنیت خود دست نخواهد کشید.
🔴
درود بر تمام روستاهای جنوب و به آنان می‌گویم که رنج شما، رنج همه ماست.
🔴
تا زمانی که جنوب تهدید می‌شود، ثباتی در لبنان وجود نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125484" target="_blank">📅 12:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125483">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
غریب آبادی: آژانس نمی‌تواند از ایران هزینه سیاسی ناامنی ایجادشده توسط متجاوزان را بخواهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125483" target="_blank">📅 12:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125482">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQFrs4_7xBhAWOwbdFKDtVv2aDPzU6h5tXxtXFbYsFJ9dKw2iu_yfSoZbxc153mDjohgQYAI58auHpUdmceL9A9CHYae3pu04zG0d-H0_-szPk18qAk1LtW-I-E1B23au8vfZYk9ue8v_0Q63vHOk9aCQlpcP4dDC9R0ETFDloFftHA59_mRYZXIrq_6bVd_4Q9BvSOnioo_j8yyFlsnqhEw57ik7N1cvNXKP_DTc-oBIhJmZWhZ56PLOZlOI7OcN0E_znQ9eyGP3mMkHOr-6ayBpLUl3lRcmyJHi5tfRsh_uf2Q2fQzAe_BUkpVh3kdCi2DOkDV9hz42PI7JuV84g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که به تازگی در فضای مجازی منتشر شده است/دادخواست مطالبه ۴۱۴ سکه مهریه دو روز بعد از ثبت ازدواج توسط زوجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125482" target="_blank">📅 12:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125481">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn2MJ8xwbnp8Ecc_fPjcfrz846xcIXu-J4fpoxW0-p7oXxjbaJ-SmhN6tFwfpL2mRmuZcZEn4EX8bsxp7vsEXxAREucgzKl81a05Uvm3WGGkoUJMuAIO-WSPHPy_jCL8zDA3OgjQ66yTWefWy0IyxNaTHj-GhE4I4LH5JmwofwlDS-ePfVO5MwGOgrOjweSNrEkls1ARzOVA8IuLYPJViRJx81whOFXpPBVWhk0WWMzVNMGdjyzhRiZaUWedr0xv4hjooQhCSXYgXjer7eLs6AuMflvX4vfsnk8wVfz-noBlEBIY6QxYtu924k4jNxCgabNU2GgY0SV9B9R5Oagymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشکل جایگزینی پهپادهای منهدم شده آمریکا در جنگ علیه ایران
🔴
ناوگان MQ-9 نیروی هوایی از 165 فروند در آغاز سال 2026 به حدود 135 فروند در حال حاضر کاهش یافته است. طبق اعلام فرمانده سنتکام، این پهپاد در جنگ اخیر علیه ایران شاکله اصلی حملات علیه ایران بوده و بیش از 4 هزار عملیات شناسایی و رزمی انجام داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125481" target="_blank">📅 12:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125480">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sb-fwLBCQw3hQ7arJq_Pjg4HgRXAVCbS9uIOEyI4fVDhJNe7YFwaTVQ6UNqKxHobwQ_Bp460tdwU4lisRFyAbNGwqYX6uG-zGompdpCRWtss7waOSvDPuaVZ81_1p7doBRoNFJ6_1pvCEJ-JdM-zuVgxhLxZYhizZp9A0-HT0J4hmhOLWWFoi9sBoQIJRcpJjNuSd-koFCpW55VefZsbo8w84Jmeul2M5BPte01crYKDQ9dz9xIvy1xlyFEP3feUE37DK4wlTQOl3tAvf90xXc80B-wJHzGGAa6AANtBC3z0fdH5AJO24WKsUJWLUfxUjH7Zcaah7GxK3l2noPQsAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۳۲ هزار واحدی شاخص بورس
🔴
شاخص کل بورس با رشد ۳۲ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۳۹۱ هزار واحد رسید.
🔴
شاخص کل (هم وزن): ۱۱ هزار واحد مثبت
🔴
ارزش معاملات: ۲۰۷۵۰۰ میلیارد تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125480" target="_blank">📅 12:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125479">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/082a0108d0.mp4?token=Fva-yzm8y3NPQQZCO-69jKkWL0D1ymggiSoTm1XGSQEv5v9kKnyd4VFNlnbDt2iqis7XaS3CdAAMtT_vpBmQhDE_QMizmuGuViuD5galBjDI0zxXIjOTHECPnAG3Z2fZ_7mvAq0BBYuwK25w4Hg2vxsG6LTZkubZl5anMPq5OKVxRpOYHPphyz7eW73_LbW5lkX972zRB-4FE90ltsSpJ9f-HaTD9KLG0smbYXDQ16P-_RpOUlNRiyDX9N_B-sBZhGnb1zMgwe7e0wfn-b7_w9n9L32S2PZej-JVNkCmjaLa_KiRkRXLqEucM5H8T4VeL9duk1KMz8X7RBlXswy7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/082a0108d0.mp4?token=Fva-yzm8y3NPQQZCO-69jKkWL0D1ymggiSoTm1XGSQEv5v9kKnyd4VFNlnbDt2iqis7XaS3CdAAMtT_vpBmQhDE_QMizmuGuViuD5galBjDI0zxXIjOTHECPnAG3Z2fZ_7mvAq0BBYuwK25w4Hg2vxsG6LTZkubZl5anMPq5OKVxRpOYHPphyz7eW73_LbW5lkX972zRB-4FE90ltsSpJ9f-HaTD9KLG0smbYXDQ16P-_RpOUlNRiyDX9N_B-sBZhGnb1zMgwe7e0wfn-b7_w9n9L32S2PZej-JVNkCmjaLa_KiRkRXLqEucM5H8T4VeL9duk1KMz8X7RBlXswy7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پیش بینی های درست تاریخ
🔴
نسل 57 چون زندگیشون تامین بود و نگران آیندشون نبودن ،دنبال یکی میگشتن که بگه بعد مرگتون من بهشت براتون می‌سازم.
🤔
یه مشت حرام زاده سکان کشور رو گرفتن که به این روز افتادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125479" target="_blank">📅 12:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125478">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر خارجه ایران :
آژانس اگه روی بعضی سایت‌های هسته‌ای نظارت نداره، به‌خاطر حملات نظامیه، نه اینکه ایران همکاری نکرده باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125478" target="_blank">📅 12:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125477">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1yhZWnEM_Vh_UPZi4upR2PSB14CrSHU4OK7JQs28ckyAaz2IsHy12yICEkuW4JHlAlYL9vrrW93UzBoZ1kEgocg01JOlIj-QD14bmP_jUwGYxEWFtR4cE6ZCPndozZ1PSqy-Q1ZnLsTd5p2Mb0-aOA9YhxqfvBI01mOVvT2_Wy0y-UXx96Cpe_mdaBB1wpr7OccpSjYj_qqFDnjsxOxN9jBx8jX_29yE0Nb9SdlzXKPxidY_djB2JKmy92zm-gKLbL8QZ4yRX2c16qnCb3XYGsFksYlH2DhTs40GOzy_5PMjEMgvR-SfCTT1aGvk0F92MpAToMvjqVqqw210Vn1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل یک سرتیپ ارتش لبنان و دیگر پرسنل را در حمله‌ای ترور در جاده خاردالی-نبطیه هدف قرار داده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125477" target="_blank">📅 12:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125476">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ایرنا: وزیر کشور پاکستان امروز به تهران سفر می کند/وی در قرقیزستان طی روزهای پنجشنبه و جمعه، دو بار با اسکندر مؤمنی همتای ایرانی خود دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125476" target="_blank">📅 12:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125475">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
لاوروف، وزیر خارجه روسیه: روسیه ناگزیر حقوق روس‌زبانان در اوکراین را احیا خواهد کرد.
🔴
این یک پیش‌شرط برای راه‌حلی بلندمدت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125475" target="_blank">📅 12:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125474">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گروسی: ایران نسبت به ما تعهداتی دارد و باید دسترسی‌های لازم برای بازرسی‌های ما را فراهم کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125474" target="_blank">📅 12:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125473">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f714df4f8.mp4?token=qFtVJtjwa4NylDonUVExEIFwF3mEfFEbvHaOUTF_y2V1jfoTXbOb_pJJZkvjLCH2-BNDTlQ0lxSomU0KuKiUeLOk14aaC_geEpWUnWEu6UXQbqgQDyYGwXGXbzXc2TWRN0jvFK8zYUkXO6eQ1SS0Sh05M-yPPJFifCReoOiZsV_SwFls8bLNvtCnadOsyGvxbhUOUOasXFzDFqqKV8InVpbAf_wmPYP0p05GbVs9EvyZhA_PJoR46pqjfc96bdskvRMYt4WEBwrQZYx2W391xZ3NQUlGJg7NE5g2zkJz0i7u-p06YKhHR87lqTXl4lXhTgQbR6yFBny-0AnvcwpKuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f714df4f8.mp4?token=qFtVJtjwa4NylDonUVExEIFwF3mEfFEbvHaOUTF_y2V1jfoTXbOb_pJJZkvjLCH2-BNDTlQ0lxSomU0KuKiUeLOk14aaC_geEpWUnWEu6UXQbqgQDyYGwXGXbzXc2TWRN0jvFK8zYUkXO6eQ1SS0Sh05M-yPPJFifCReoOiZsV_SwFls8bLNvtCnadOsyGvxbhUOUOasXFzDFqqKV8InVpbAf_wmPYP0p05GbVs9EvyZhA_PJoR46pqjfc96bdskvRMYt4WEBwrQZYx2W391xZ3NQUlGJg7NE5g2zkJz0i7u-p06YKhHR87lqTXl4lXhTgQbR6yFBny-0AnvcwpKuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ هوایی اسرائیل به شهر
السکسیا
تو جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125473" target="_blank">📅 12:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125472">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
زلنسکی: این جنگ باید پایان یابد. اما رهبر روسیه می‌خواهد به جنگ ادامه دهد.
🔴
شب گذشته، پهپادهای ما حدود ۱۰۰۰ کیلومتر را تا منطقه سنت پترزبورگ پیمودند و انبارهای دریایی دشمن و پایگاه کرونشتات را هدف گرفتند.
🔴
قدرت ضربتی دوربرد ما همچنین حدود ۵۰۰ کیلومتر از منطقه کراسنودار را پوشش داد و یک انبار نفت را مورد اصابت قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125472" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125469">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=T5mx-fKpgmYISjm_OM2wy3ndeXpDZEDB0cw8t8ud0EQlb78GZ9sdgWzrF9tgD-YoWeGpu0GY77XfVus3L42IyBdhq9ooip-BkBy6v2yd1vQN5FS2H4Ye6GKxrqzq_7ej9mEHHBsTUldipGZ-6wZT9kTH9TZgESM5RTv4K9uL9tCGU90lob96mqRrTByyjZ1qpZGzIug9CqnXFQPP4rryVdf2nxdZcZdjpPBXxnPJgmL_KGC42dLi95H-jeUgCUMEjYQixRABpSotjXVPZEFMUyYB2k8vJ14nBNw6j1181RTWP6KuyeKz1TD8tjg-tiT2Bxy0krvqlwq_Lp81M3FG0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=T5mx-fKpgmYISjm_OM2wy3ndeXpDZEDB0cw8t8ud0EQlb78GZ9sdgWzrF9tgD-YoWeGpu0GY77XfVus3L42IyBdhq9ooip-BkBy6v2yd1vQN5FS2H4Ye6GKxrqzq_7ej9mEHHBsTUldipGZ-6wZT9kTH9TZgESM5RTv4K9uL9tCGU90lob96mqRrTByyjZ1qpZGzIug9CqnXFQPP4rryVdf2nxdZcZdjpPBXxnPJgmL_KGC42dLi95H-jeUgCUMEjYQixRABpSotjXVPZEFMUyYB2k8vJ14nBNw6j1181RTWP6KuyeKz1TD8tjg-tiT2Bxy0krvqlwq_Lp81M3FG0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز در کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن
🔴
«خسرو پناه حیا کن، کنکوریو رها کن»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125469" target="_blank">📅 12:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125468">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uInVomGDf2OL3bIczPHzFLHWAmTKRPkTkf0QEQttk3H9-1el1ETEdXY314EyxdJaihkvlKwBhhnB5eCWaPNqu2gKtECjp2NgUnnbf1pdnxEQc-4CSJDgHiOWcpYaQSEegHP3oVftQLLQpsiXLdMjCiYist-9a9ujJ_9f6FRIQlHQh8XAQsV2ljii1ngPWpzkhLZo7O0Z-O2M1IFkqRF1AvRDo4FQz3Mk9Tb1vxMhvmSLeOQcoFP2qmtND0IEhNMaxsVuRqEKzPEebfGJbGcM3uoqZ738mPZ1JnuvFPQd2H5pDup2mBbuaEiiCDbFzDRF80NpeCTuUISw_vLjndrDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تریتا پارسی: به بازیکنان جام جهانی ایران ویزای ورود به ایالات متحده اعطا شده است. اما آنها شب را در ایالات متحده نخواهند ماند
🔴
آنها در مکزیک مستقر خواهند شد و سپس برای هر بازی به آنجا پرواز خواهند کرد.
🔴
این بدان معناست که آنها باید در همان روز بازی از طریق اداره مهاجرت ایالات متحده از مرز عبور کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125468" target="_blank">📅 12:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125467">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
معاون وزیر بهداشت: بخاطر قطعی اینترنت یک رتبه علمی در جهان نزول کردیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125467" target="_blank">📅 11:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125466">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juQyP-JwhKb_C9fEf3Wv4Uu7E4tlkAg65EYVHQgOIOZqQ3snK16Lc_2eMlYi690dYqO5pyDgr9JzyBAFQh9SKWlfIlgJ2Iyc2R_0CJ1UpGZAyRghavnD-RW5oud3cWBOldhB5F2hz_70F4uA8KHecmF4Per4bnvuKlwpf0zMhxGP8aWye36r2yIBkEh34BFtU9r8sl-oG2BfDpMJ58GxZmtDqCz8X8ftjcqp-0Kkz2pMvwuKlcK8_-DXVaKg0w_II46L-mrAEnxz6LwKHwZibhRbM-uSCtN4cs13WDYrefvRtFseWKTgYtuIiBZLBqhKyXJoUW7Kda8rQ5lE4mM00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت مردم پاکستان داره قطع میشه بدلیل اعتراضات مردمی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125466" target="_blank">📅 11:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125465">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مشاور امنیت ملی عراق تاکید کرد که ایران پیشتر اعلام کرده که عراق از محدودیت‌های عبور از تنگه هرمز مستثنی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125465" target="_blank">📅 11:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125464">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سازمان هواپیمایی کشوری کویت:
از سرگیری ناوبری هوایی پس از تعطیلی موقت دو ساعته.
🔴
تغییر مسیر ۱۱ پرواز به منظور حفظ ایمنی مسافران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125464" target="_blank">📅 11:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125463">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
تهدید جدی تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125463" target="_blank">📅 11:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125462">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ادعای آسوشیتدپرس به نقل از مقامات آمریکایی:درخواست ویزای برخی از اعضای تیم ملی ایران به دلیل ارائه «اطلاعات گمراه‌کننده» رد شده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125462" target="_blank">📅 11:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125461">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رویترز به نقل از وزیر انرژی آمریکا: کاهش قیمت بنزین در گروی توافق با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125461" target="_blank">📅 11:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125460">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
الجزیره: ارتش لبنان اعلام کرده است که چندین سرباز، از جمله یک افسر ارشد، در حمله‌ای اسرائیلی به یک خودروی نظامی در نزدیکی نبطیه در جنوب لبنان امروز صبح ترور شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125460" target="_blank">📅 11:10 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
