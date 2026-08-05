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
<img src="https://cdn4.telesco.pe/file/IAp0lxosLpzmXajifemzV0lrtYevhYkhQGChPvGRd57HMR6sMQyEfKw3DXyE_S3eZGf0Va4qqSIMv7NP-K8-C3ow_sT935BmghzcPtOE55Z3s4SOcXu7P7n1KufUFDmso8R3xzeWRIMcrqcRpAogN96pIKtsuKjPNtk47E45V1xMJz1uaS6BOUacuqHHSBeBRk1JjtC0HE2tcC7epAZGccZm86GOB-D1YMgnrIQdtjBNefKpek94QydNrHhYxhfu5jnGkGUYud-AIqdJ7zv6bjO2a4BJmesqIleKW24frv_jl8vD7-XK3ZdAzon2yb3Eh4wZfl3mTtmfLUdw1jPJKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 134K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 13:56:31</div>
<hr>

<div class="tg-post" id="msg-69569">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db3cnonA-aY3BBQ-RTrETMfG_Pb2Z2pS4P6NAkg2UrswauH9cakLKHhJSf2L4DsoJmXIMt7Ws8y0Yck9jCroTPb1nPvPTxeBKfQozhhGSX6FUj2WMzAKmAhSUGlLWyXZuVp8B-g1ooH34eRX8VppN77TvYAh13dwNSe4cw2ds9xwNNF6DtyX3ROcTD1Ao1-6m03qggxuDdAy5btdZ9n06aW_ieldvBYoduR0IO_qDwjFjEHHewjP1Xz0pwoBj4p-_qoHM7GylzY8M5JDgksTMZChzCjaPzL4rW3q5yJJAGCDl5iLbdml46geB170ySNLIE9QMT5ybOlZHkLVi2Z19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
❌
حمله هوایی ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/news_hut/69569" target="_blank">📅 13:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69568">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=j5y7JDSbRIrjWznonCRx63zZgN6JwdDjwHZ5B8zNh1YMNet2chFXNDyeOMd5cMQCLMVh0N1f95lgfgbUojQyC9jvh5pgGIGX75_iQfboiLIgnlQa0euPNLHqf0JUy8cIGWMrDRfi5PPKmyStfatAJSbNimGXZU-2EEPCFAVFhLAnyz4XMz3VfrpuQcuyc1pciWUCOSDGQsl_p5dhEzXXqVZh1XyGRjqjNmJ9rdZQ64pwXfWXhWELby_Zjt5bJ5fUs6iLjOJ3f1HiwSej7gaITKESyMCDCxeBMR8OfI-6VjfaFV66-yGN21gpx4E6_lfpEc-S4kPOywbMInOtsrxgXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=j5y7JDSbRIrjWznonCRx63zZgN6JwdDjwHZ5B8zNh1YMNet2chFXNDyeOMd5cMQCLMVh0N1f95lgfgbUojQyC9jvh5pgGIGX75_iQfboiLIgnlQa0euPNLHqf0JUy8cIGWMrDRfi5PPKmyStfatAJSbNimGXZU-2EEPCFAVFhLAnyz4XMz3VfrpuQcuyc1pciWUCOSDGQsl_p5dhEzXXqVZh1XyGRjqjNmJ9rdZQ64pwXfWXhWELby_Zjt5bJ5fUs6iLjOJ3f1HiwSej7gaITKESyMCDCxeBMR8OfI-6VjfaFV66-yGN21gpx4E6_lfpEc-S4kPOywbMInOtsrxgXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
دیروز طی یه مراسم تو روسیه، یه چترباز از هواپیما پرید پایین ولی چترش باز نشد و سقوط کرد و درجا مُرد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/news_hut/69568" target="_blank">📅 13:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69567">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phgihB6RglSJEha4QerpHlyF7p4wA69xQj7mxULcANw9pyKATSBWbsUgQDwymmPuLRNMWL5WCUfIUW0h1zdefrJSnIIv3TDs4BbCNiryvZqhaBPnyVfCQNlfK4ZZ2SRLDAcO36FoG5lw1NeKFbaYhmSsF7QxGb9DR-ZKxWx5JAz3NdRi7cvjrvaD-7Bab_8yT2FLsfqa7cXx-woF7M0ooZCWF01otCxDTjBTjD2d05lFirweHToUSNCEffFaFxu-1XivNwfR6yEl9UWc4oj333htIwmiuiHW2wLdOPgJx1Fp6C9nGemcqBoIVKsHiW2QAXZzqSBpvu9X5JJYlMTfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دونالد ترامپ تصویری با هوش مصنوعی از خود منتشر کرد که در آن با لباس نظامی در کنار ژنرال پتن و ژنرال مک‌آرتور دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/news_hut/69567" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69566">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=LGcZOONBYTnbLzFwfeB7G6rmAhhxoTQpKExgZ0oNY9wgacToIDTzFLmGQF2Mpx0kDKrWf4gmy4DUfnt_puedoLl4stAO8FxdmTAf-AlUOY_PozX7f7qOzUC-NFvya8YgfYK7MfTNIYmo_6Pevg9QFnZMBmriRDSlR3iBM3QQWTBs4R1VsmtV253jpDohTXFjRc3j55LzrlpkUtRHbq8WDwRT2P8YllBrbzP-HxYgTKCiLiIyFbxUnoAESHmY4HD1w9cF3pNfoYHJELRvxEW0tXqw0cYV-B7Ha3W07vKzj1n0jkDgwRZrKIduaZ1iEkIov3pzwVQ1arE_VTsQKDm1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=LGcZOONBYTnbLzFwfeB7G6rmAhhxoTQpKExgZ0oNY9wgacToIDTzFLmGQF2Mpx0kDKrWf4gmy4DUfnt_puedoLl4stAO8FxdmTAf-AlUOY_PozX7f7qOzUC-NFvya8YgfYK7MfTNIYmo_6Pevg9QFnZMBmriRDSlR3iBM3QQWTBs4R1VsmtV253jpDohTXFjRc3j55LzrlpkUtRHbq8WDwRT2P8YllBrbzP-HxYgTKCiLiIyFbxUnoAESHmY4HD1w9cF3pNfoYHJELRvxEW0tXqw0cYV-B7Ha3W07vKzj1n0jkDgwRZrKIduaZ1iEkIov3pzwVQ1arE_VTsQKDm1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره ایران:
خب، اگر دوباره پا پس بکشند، ضربه بسیار سختی خواهند خورد. آن‌ها این را می‌دانند؛ آن‌ها این موضوع را درک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/69566" target="_blank">📅 12:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69565">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=ifpHp6iNapfj6SbkxiKKGRS1bkQOTDDqGW4z5XBexaO9pfW2r4MU0EiPVBmBh-5Is8Qh1Im7jtO-UEyttdLCRoxm13ONCsIR3nOmzE4AOSH8kqkBuIxiX3ZTFrletD77b3D2IXRwd31tcUE2HVx7rBCplebI1BXJY323iRan6OGf_2GfLY95-1AAloVRZkRUeK3WF7oJiaDFi4r9xJfndoCuJAAfCdW-sguKiJMrFq-5c4JK-9lf1Gb3DHE8Bch9Roji7oNKydcVwI3CmKaA_MgmpM0F2dyPR4X78rism7HUXL-D--8CmhNtGUStRvt0CYco2is1XRmV8HIa9afgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=ifpHp6iNapfj6SbkxiKKGRS1bkQOTDDqGW4z5XBexaO9pfW2r4MU0EiPVBmBh-5Is8Qh1Im7jtO-UEyttdLCRoxm13ONCsIR3nOmzE4AOSH8kqkBuIxiX3ZTFrletD77b3D2IXRwd31tcUE2HVx7rBCplebI1BXJY323iRan6OGf_2GfLY95-1AAloVRZkRUeK3WF7oJiaDFi4r9xJfndoCuJAAfCdW-sguKiJMrFq-5c4JK-9lf1Gb3DHE8Bch9Roji7oNKydcVwI3CmKaA_MgmpM0F2dyPR4X78rism7HUXL-D--8CmhNtGUStRvt0CYco2is1XRmV8HIa9afgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فریادهای مجری کشمیری(هند)صداوسیما درباره تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/69565" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69564">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/news_hut/69564" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69563">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoUC7Nr72cbFM3f1p-UCG20K_XicwfYhKgR8hKnPz6QJ-MPf3GyS4w8HRDL1mPx57AVXvykj7j7pHl_V8YNBB7XZIhZQCOUy7icqMpXkyZXOJdyKDub2F2xq-P7xYzH5QibjUcf8fLl2M2P8qWfjclFfIyIzwDN1VKOu9w_EGd05T6XVW-bd_vYHKxP2bH4xDZGHQq-OtoUHBu_7mxesPM12eWSGrjx52M1bSLFo5LNkzBz0yoU2YhiK7TKn85cfzo8dvsDVaqJ34aV46KVm3SO0MR_ORuiNr6Vp3_S_AlMjtqYOaEdduszIi-n1S_WxVIaSMR3bE6Vx85Rc20NkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/news_hut/69563" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69562">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=gEaNg3PNy9RWfRpqRCHes4ImAjT3A2FFxp3Amx4xiOI0SjJF41JoG1h1OwzIoODJVZCWmDTiIf1upYQFqkhfqCOgb3q4X5zt6NaIfBhWe8V3QdFwJkkyI4fyZqUQnFTiSucdafl3HgdA_So_GQ6QWIUH1wgMeZD9fzDxwCH8MIbTS3LzDwA8_F4d2hScRicQG3-0j4i8jgLJBkdF5-21tk0nJ_XeMqIiQqlGSiVBTwsb7gfb0tl_Oon-1A057-Ca0jrRFMyGkjxvgOtASHhq6vD7B6d_zPT-tyZE0sPwh6h_v6GKDD0bSHSbCFwPJ1u-WMWvl2WyeoIc7MacAIwAAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=gEaNg3PNy9RWfRpqRCHes4ImAjT3A2FFxp3Amx4xiOI0SjJF41JoG1h1OwzIoODJVZCWmDTiIf1upYQFqkhfqCOgb3q4X5zt6NaIfBhWe8V3QdFwJkkyI4fyZqUQnFTiSucdafl3HgdA_So_GQ6QWIUH1wgMeZD9fzDxwCH8MIbTS3LzDwA8_F4d2hScRicQG3-0j4i8jgLJBkdF5-21tk0nJ_XeMqIiQqlGSiVBTwsb7gfb0tl_Oon-1A057-Ca0jrRFMyGkjxvgOtASHhq6vD7B6d_zPT-tyZE0sPwh6h_v6GKDD0bSHSbCFwPJ1u-WMWvl2WyeoIc7MacAIwAAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی :
به عنوان یک سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن. چون ما داریم در کنار آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم. این شرایط گذراست.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69562" target="_blank">📅 11:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69561">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=qWN8rEHJn6kfPrawv8SZ2sumGFcIcOAzfzX-i5NDvx1imgI6EJgpk-9hyiPyHlT3xSDa-joXwigfBS9ru8OD12NyTIaB75BGluDvpuhzq8dIbA0QH9lU0jSRaRjwr3GEO4brHTzZipRUDSLzgUlhImtOkoGWvRFaMst-SO0vYvnTOasP6Oap9i6o-V4UYDDgD8uDCusLlRluKiDLpm3HZMuNnVgDVIlXsqCwOkIpaA9tyOpASfVibF1tDqWd2sL3TaBs2dUn6par3vC1gC0UOdFYS9BiGBfBzDrNzlLrukYlEEJl74pRitVm-6SNMH0yIYkPvljZXf87Zxf-7l_nNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=qWN8rEHJn6kfPrawv8SZ2sumGFcIcOAzfzX-i5NDvx1imgI6EJgpk-9hyiPyHlT3xSDa-joXwigfBS9ru8OD12NyTIaB75BGluDvpuhzq8dIbA0QH9lU0jSRaRjwr3GEO4brHTzZipRUDSLzgUlhImtOkoGWvRFaMst-SO0vYvnTOasP6Oap9i6o-V4UYDDgD8uDCusLlRluKiDLpm3HZMuNnVgDVIlXsqCwOkIpaA9tyOpASfVibF1tDqWd2sL3TaBs2dUn6par3vC1gC0UOdFYS9BiGBfBzDrNzlLrukYlEEJl74pRitVm-6SNMH0yIYkPvljZXf87Zxf-7l_nNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکیه دلقک:
تا ۴۸ ساعت آینده خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69561" target="_blank">📅 11:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjSZUxtcYmQnuZ8I6JcM4NEJA0LgJ3tqJ3DlKo3xrfR4-qiLyLJftYrEikIqemF68aa7XzCnCNGEkkCXch5MAzVR9FLLZ0fftHkBQbiKn-q---jFqA75TCOsqFO8kN0HwkSzHtLi4_ECwrq538g_Si2EcPbxGInUwIpyecEwHHpTNvZZYqXJkZoTYwZsa1BuksHAMzLJb9oSZl1XtEAmHFiD3GUrYUMS2C1SwXpcbwh1Os5YSX9Yg8BTGsLCzOf4gaL9I-m3ewlinEqrIgKkyqytTsaVZGky2KRktciVBXgou4YhzIXBiI6dI9-mrQLNovHfKwJZddT7W6GG6pj22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=d9yubhK-8Sb5vq7G-badToAdPKxBXJDkpMay0Xjls14Fn9CzW_igDY8mTVxV6pSmPnRZQiOmHMOZSPSOmZfjpOSuBRsT01_ZaEpYiCdRO2MtxAe0yGBal3ZINivOAJyymdGVPgOksahEm4L7ZHI2Zvb2sPhC8Q6NGIkjmDMdwyx6qfTt79REjafTGStY0Iqf81kDT4Pm1w1eSEz8-WNocrYHWwUBsud31yAhPiCA8W93CybCjVFGJhdIcDWcWBNQYFAio06901XGaYzgyZwkzLgocHwQQOb0us34Cnl5MOzjVDC8mFlkkdCyE6Q1I67wy2v-kcIjTuR6HvmgQF-_kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=d9yubhK-8Sb5vq7G-badToAdPKxBXJDkpMay0Xjls14Fn9CzW_igDY8mTVxV6pSmPnRZQiOmHMOZSPSOmZfjpOSuBRsT01_ZaEpYiCdRO2MtxAe0yGBal3ZINivOAJyymdGVPgOksahEm4L7ZHI2Zvb2sPhC8Q6NGIkjmDMdwyx6qfTt79REjafTGStY0Iqf81kDT4Pm1w1eSEz8-WNocrYHWwUBsud31yAhPiCA8W93CybCjVFGJhdIcDWcWBNQYFAio06901XGaYzgyZwkzLgocHwQQOb0us34Cnl5MOzjVDC8mFlkkdCyE6Q1I67wy2v-kcIjTuR6HvmgQF-_kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
🇮🇷
جمهوری اسلامی دریای خزر رو فروخت رفت!
در تازه‌ترین قرارداد، جمهوری اسلامی دریای خزر رو تقدیم روسیه کرده و یواشکی دارن میبرن مجلس و تصویبش کنن.
سهم ایران فقط به ۱۱ درصد رسیده! شما ایران رو فروختین و شرمتون میاد بیاین به مردم بگین.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69559" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=HEIY2iQxUM20jNzPn4NZN7vdR_SYxEm094lqFeUl-237XJ0Hh1nr43WBy6mV3f57MKNXxNbPcxyaJxSSC-Eb9cY8s7wrnHmNRwSvTX8IorIm85kRafz1LubeiLiYXmzgd5ac9tUv_DYQqO2-I6WrhiocATFzIOw10Mdawl2LLWL2YmLm1R36XIktg5roYJ0KDuYRv-OkTNeMFHV23u8S920QTiZtzUYfHS6YOkZywZgBhhZrCVW2pNKMZx6pHJInRw6598Bnhlhij0nXywXBnhf18XxOU4fmAyd49VJUX8onDrb-ex3C02uKqseNMj_wpCNaD2JFtGp06zH2lez_DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=HEIY2iQxUM20jNzPn4NZN7vdR_SYxEm094lqFeUl-237XJ0Hh1nr43WBy6mV3f57MKNXxNbPcxyaJxSSC-Eb9cY8s7wrnHmNRwSvTX8IorIm85kRafz1LubeiLiYXmzgd5ac9tUv_DYQqO2-I6WrhiocATFzIOw10Mdawl2LLWL2YmLm1R36XIktg5roYJ0KDuYRv-OkTNeMFHV23u8S920QTiZtzUYfHS6YOkZywZgBhhZrCVW2pNKMZx6pHJInRw6598Bnhlhij0nXywXBnhf18XxOU4fmAyd49VJUX8onDrb-ex3C02uKqseNMj_wpCNaD2JFtGp06zH2lez_DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پرزیدنت سابق، جورج بوشِ پسر:
مذاکره با قاتلان، گزینه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69558" target="_blank">📅 10:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcljIWTQq1fJwSx03X_Cwed5Ku6pdpNWwKDPMBFXEKIazQ90U6zObHPGOAT5wv1Tudmm6VGCvpvFavCaDVacM_LnSj5AmdkQNGyKphl6KEYOnX0ZWx2TEg8NVRpau7XcsQOAZU8ERW0Y2w7ea6SDoL4KQCH5WdpFa7V_jXXKtH-muXAIcRT2M8hBHq-ggrWpuMF5isRSdNwJb53r3UBoOfwKRL98s4oXHjRiDd6K8g7mI74rxDshJFymeHij1L-fT_1EKqYPcZxS-v-w8YwiC3huHCawEl6nR7UY7GTfakf9AZigz3D_K0lYZfR1bvD7Mt4fMhCSKGoHMgnFQ2-_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
🔝
بر اساس گزارش آکسیوس، آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و احتمال دارد این توافق روز چهارشنبه از سوی آمریکا اعلام شود.
🔴
مفاد اصلی توافق:
- کشتی‌های ورودی از مسیر شمالی در آب‌های ایران تردد می‌کنند.
- کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان و با هماهنگی ایران عبور خواهند کرد.
- برای عبور کشتی‌ها هیچ عوارض یا هزینه‌ای دریافت نخواهد شد.
- مین‌های دریایی در مسیر مرکزی ظرف ۳۰ روز پاکسازی می‌شوند و سپس این مسیر برای تردد دوطرفه باز خواهد شد.
- پس از این دوره، عمان و ایران درباره یک توافق دائمی مذاکره خواهند کرد.
همچنین قطر، پاکستان و عربستان سعودی در میانجی‌گری نقش داشته‌اند و کاخ سفید نیز مستقیماً در مذاکرات مشارکت کرده است.
طبق این گزارش، عباس عراقچی با این توافق به‌صورت اصولی موافقت کرده بود، اما تأیید نهایی باید از سوی رهبری جمهوری اسلامی و شورای عالی امنیت ملی انجام می‌شد. یک مقام آمریکایی و یک منبع منطقه‌ای نیز مدعی شده‌اند که این تأیید روز سه‌شنبه نهایی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69557" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=aV6SOQAACF1NtH7Rs-r08wZG9dyrI791jv_mVJXybMHHltmZSwEKxWNpX_vlU2oAUnjsLfTkpT8uE0igCfJ0YkjGqpzHvYZ9jS-PlBd6Mcs-AZirceNcvdaOpq28SgMAZ6k1UeEOaavwC8JIy-8QLSkuz-FPqTuSGF3tuGSbRJVtLYZcHyQgNffWvdOa2mXLQxtW4ErQt994R1Rmo7RRaLom5Ikqu6J8NELqIekhT9UcM31YWZAKmlrOIDGEaTxMB78ZT1YTo3XtunErhH6aPWTDPPy1KzP5NiQWVqQMoWOJcFU1r7bhxMOus4-H7EzU2e-LUlkRuGDOLCL2k2KFR7pGhzbmCf9adhpRrEiQS8FDd78DojIyURUf5ZJRpftVUDkcDUzRmFV9Nb8OuJYlJldYLS9SFTai04vkzjlPLAD_0xt-G_YUYr8GlN3W4vpm9zVcCaN2-k3c0KAU7vKV_5r_4onpFFR4i4NR5z-p4AeBXgcV_nw_SxRn4qP7GD0RTyQ7nXTkaaFIizQiw8kdHwhG9mOQyNbW7lgb72N_AcNg8gMgeZYCH6MY2m2dOmESPUvJc1A7q9B-UE8vxvYnCg49h2x0Tbln233xAGb1dUDiJlwdLdxT79Rn963mppmBIeTihuab-KMvdl3-lzuiWE5fq8XyGImTXLCwW5LMke4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=aV6SOQAACF1NtH7Rs-r08wZG9dyrI791jv_mVJXybMHHltmZSwEKxWNpX_vlU2oAUnjsLfTkpT8uE0igCfJ0YkjGqpzHvYZ9jS-PlBd6Mcs-AZirceNcvdaOpq28SgMAZ6k1UeEOaavwC8JIy-8QLSkuz-FPqTuSGF3tuGSbRJVtLYZcHyQgNffWvdOa2mXLQxtW4ErQt994R1Rmo7RRaLom5Ikqu6J8NELqIekhT9UcM31YWZAKmlrOIDGEaTxMB78ZT1YTo3XtunErhH6aPWTDPPy1KzP5NiQWVqQMoWOJcFU1r7bhxMOus4-H7EzU2e-LUlkRuGDOLCL2k2KFR7pGhzbmCf9adhpRrEiQS8FDd78DojIyURUf5ZJRpftVUDkcDUzRmFV9Nb8OuJYlJldYLS9SFTai04vkzjlPLAD_0xt-G_YUYr8GlN3W4vpm9zVcCaN2-k3c0KAU7vKV_5r_4onpFFR4i4NR5z-p4AeBXgcV_nw_SxRn4qP7GD0RTyQ7nXTkaaFIizQiw8kdHwhG9mOQyNbW7lgb72N_AcNg8gMgeZYCH6MY2m2dOmESPUvJc1A7q9B-UE8vxvYnCg49h2x0Tbln233xAGb1dUDiJlwdLdxT79Rn963mppmBIeTihuab-KMvdl3-lzuiWE5fq8XyGImTXLCwW5LMke4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
تنگه به زودی باز میشه یا ضربه شدیدی بهشون وارد میشه ک باز کنن
اونا با من مودبانه تماس گرفتن گفتن میتونیم صحبت بکنیم؟
ضربه سخت ایران تو راهه ولی قدری دردناکه نمیخام ازش استفاده بکنم
خیلی بحث هایی خوبی داریم ولی اونا نمیخان اعتراف کنن چون یکم نگرانن
شما میگین مذاکرات فوق العاده داریم ولی اونا میگن دروغ میگین
اونا میخان معامله بکنن و بشدت خواهان توافق هستن
در عرض ۴۸ ساعت خواهیم دید چه خواهد شد
قیمت نفت و گاز دیوونه وار میاد پایین چون سه شنبه مذاکرات فوق العاده داشتیم
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/69556" target="_blank">📅 09:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d290294320.mp4?token=rbDd-MLPSkqIp3va4q9ewfqOa_FNzyuqiqeWPsldh4MGMrH0fr9HiaaFne_-GOc_EwTa2k06f38QxNahpNz-u0BZymvulbSQOPnf7DYomXkltmG0qiMhPyizsH6PWe4dkFH77J5hdnt9Ss88nBtTr6MV2jEUfpU3ba5tthz-jJ3GsEQ0rYftrpGawdQoL7YjTgVF0QTZXwlowa-nM03qK8XkDg9Gc8AaJubIzajnFeHi7WL9yArLJhcVneIvXrW2jwIfgWXfi0UaaGUMCcau0MOf0kjR626TlT3fKDOuKB6YUHu4Tvi-h4eTiGWx71xFm1mE4cNAh2GmNs17n4GcDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d290294320.mp4?token=rbDd-MLPSkqIp3va4q9ewfqOa_FNzyuqiqeWPsldh4MGMrH0fr9HiaaFne_-GOc_EwTa2k06f38QxNahpNz-u0BZymvulbSQOPnf7DYomXkltmG0qiMhPyizsH6PWe4dkFH77J5hdnt9Ss88nBtTr6MV2jEUfpU3ba5tthz-jJ3GsEQ0rYftrpGawdQoL7YjTgVF0QTZXwlowa-nM03qK8XkDg9Gc8AaJubIzajnFeHi7WL9yArLJhcVneIvXrW2jwIfgWXfi0UaaGUMCcau0MOf0kjR626TlT3fKDOuKB6YUHu4Tvi-h4eTiGWx71xFm1mE4cNAh2GmNs17n4GcDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اینترنشنال:پزشکیان و مجتبی خامنه ای باهم دیدار داشتن و این دیدار تو یه ماشین بوده
؛
مجتبی خامنه ای صندلی عقب ماشین نشسته و تو یک مکان نامعلوم و پزشکیان صندلی جلو نشسته و حق نداشته عقب رو نگاه کنه فقط صداش رو شنیده
.
پزشکیان از مکان هم بی خبر بود فقط برده بودن ببینه اونو.
پزشکیان قرار بود از فرماندهان سپاه از جمله وحیدی بهش اعتراض بکنه که زیاد در دولت دخالت میکنه.
مجتبی اجازه مذاکرات رو بهش میگه ولی با هماهنگی سپاه پاسداران.
پزشکیان کلی مشکلات اقتصادی رو بهش میگه و میگه که اینطور بره ورشکست میشه دولت.
پزشکیان از این دیدار خسته میشه و میگه میخام مجتبی رو ببینم ولی به هیچ وجه اجازه دیدن رو بهش نمیدن.
پزشکیان که فوقش یه ساعت میشد فقط صدا می‌شنید چهره ای از مجتبی ندیده بود.
پزشکیان اصلا از این کار رضایت پیدا نمیکنه وبه رئیس دفتر اعتراض میکنه.
میگه این کار جز خورد و حقیر کردن من نتیجه ای نداره .
بدجور عصبانی میشه و جلسه خیلی کوتاه تموم میشه.
تصمیم استعفا از این جلسه شروع میشه چون پزشکیان احساس میکنه دیگه قدرتی نداره توی اداره کشور.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69555" target="_blank">📅 09:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=agHeGS9OsGj0xZkKIJT1scMTMy2EyarruO8HtvTra_m5gGz8R-ezq7okB9iFt_Ne3ASGO9AuBdxq9MM-m0RFFeyyk1DWpJi9_WHjOUe3_LYGQ2c-nXWxRjnYG3VtdTwfEHNVwAMyHwko6ozS6aZcctmJaS5BN9Qe7UTroAhW3MjGnE5uNGdOnrJ6PW9epXsj_zwBygct4aAn3TAB3KD5uZKk4g7BauibZ4PnIlUsbl5c8hnIyJDDAkGGviZbHsAvcYLottEqMC9G4aHpg1QzFeT9ThFE6EhNdzFuQyo837fBWnrCCiT049-XX91gmR2TcfhayS7dJ760GGV9azKg-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=agHeGS9OsGj0xZkKIJT1scMTMy2EyarruO8HtvTra_m5gGz8R-ezq7okB9iFt_Ne3ASGO9AuBdxq9MM-m0RFFeyyk1DWpJi9_WHjOUe3_LYGQ2c-nXWxRjnYG3VtdTwfEHNVwAMyHwko6ozS6aZcctmJaS5BN9Qe7UTroAhW3MjGnE5uNGdOnrJ6PW9epXsj_zwBygct4aAn3TAB3KD5uZKk4g7BauibZ4PnIlUsbl5c8hnIyJDDAkGGviZbHsAvcYLottEqMC9G4aHpg1QzFeT9ThFE6EhNdzFuQyo837fBWnrCCiT049-XX91gmR2TcfhayS7dJ760GGV9azKg-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازم ترامپ از ترور جون سالم به در برد:
⏺
فاکس نیوز؛
مقامات اعلام کردند که یک مظنون مسلح به نام «جنین جان تائله»، ۳۸ ساله، در زمین گلف «ترامپ نشنال» دستگیر شده است؛ وی متهم است که پیش از سفر رئیس‌جمهور ترامپ، تدابیر امنیتی را زیر نظر داشته است.
پلیس اعلام کرد که متعاقباً از منزل این فرد، یک قبضه تفنگ مدل AR که به‌طور غیرقانونی تغییر یافته بود، جلیقه ضدگلوله، خشاب‌هایی با ظرفیت بالا، مهمات و دفترچه‌هایی حاوی «مطالب نگران‌کننده» کشف و ضبط کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69554" target="_blank">📅 02:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش پر حاشیه در آستانه پرسپولیسی شدددددن  https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69553" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69552">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8GjKeDsmjXIxxnFEomLQ-5ykilfp_a4WJNOuAWdP4ngAIGHJEa0qn9za8M7x84s7oL2IlSu7tBjrrpDRPc_smDrH3TrezIqKVeX53XNdz3c05f14jfzDxxTfc73WJwBgXTFimdqZ0PlTi39if4ml8ed2PAFMcYhl4QeP33wAoxbSNkfIINRdsGaSHRv43Lzp6UwAFd4h2ELbfvScTj7pEe-k8VzaLQw7Q3sD6038gaQcyY5l9-IIMgIiDXmkddy9mYswHIGvk-QHBXxIG3lBG55YDXpKAlcrGPU8hWE38EX4cUtrnD1t10ELk1po6-3pkfIoBWeHAbnzA_1tZQ7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و پرسپولیس هنوز هم شانس رسیدن به هم را دارند!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69552" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjhTbHSzWrpmmcqdvLYpogz5smzlz4xVlqJArkjTZPcDxOk0AGcVth3XAUyPA_M94LfNyPLNZHG17AqZrJwW0gVWyZesVHOeoeIVjpK1mzgrcjm2fGN02eQ2-WyVSNy1lZY_0ZDsGrzMdQ9q1ZwZNq3hoaaBx3EgcuV_HZ1jTs-uvbunrsTv4PD44sXKOmmgYTGYhr7OghcHFehqGjulNt8rRJNJFdZRsr4TiI0BFinwaHGr3TSncbf-G1qZPTv7z0z_LlrmYcnck8ZFosvZjEdKWwV53D2euDaZxS09pZoE0sCemtNi9oGZywXtFLCHhvKQ-g5bKElrnHwrtxJPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیزارم اینو یادتون بره
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69551" target="_blank">📅 02:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69548">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSpbY4Bn7879deH84mNvbQG6eEY5xp8YLtbpWlTY_Y7i0cNlWwI0EgFY3lpPilI4TvtI1lG_zpIQOZfcl5Rg3iPuiGDHYUkJUZp02BJ1d81gCMUhhNmOFz5PO_aLy3_89wgxnnQFHe8FSjLjuXUD94qPcWGFOOeECLwlgtcCYsMaSRpsYH8VnPVR5iJZ4zk45vTD8xaEzRQ9lF49xb9GjEZ2j7GV9Yzl8XqvL1volnmbTLdiDJP6fmn2b4vfRzW097i75HRR87LCo-QeTTfeogAsgEq3kG-tQZGVaXHNY2dxhcu24vfWFoITJsQPBflWrGhzs2FLYl56z4Hp7mF3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RI9qXqxAS-W5IjzCRJbc0VhJf0UkgZUBJFu_6KyEF93fBFENUWLTI2MfpMBom6UBOmkK8ZMYzGYjfl9H3hIwltjIftU7NxhPvqbbCSctnyUHvBsZawSEKOA4xOHp5MmgxSab01T1_cnkPm9Fi3X8qC5G6OjQnlnVN9GPY97dOm6MJnZX2iEFRoW0k6AmPFMfNh_lJXmD7rWweKfP2BabbUngtA-WeVjxkuuX_6ftpiM7H6ZcLTNqQio3JOVGeDUvNcsVNFuUUSzYg9rk8f9aruKdJu3SnZ6831cErQjxT__lp18asxCZPTQwrxJ_12l3Mr-csTWTTkeWdoSM6E9u5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=bShf72abCQ-80qSUO8L1lesfjTCtcXbmyrDs5jm44qxVQuHBBIWpPWobSB4eui4RzFKIh4P-XzeIv_RC6XtxAf0aWQRgPX8XHkJLzq2OCuQ4fB1gEWyhb04Wh1N1nLxY9-65PVNeTBXXmljd4KiVLGeZwYa4KXdLOmcOIozBBC22lVC_zIg0EZi8PE8WKgmBVm-8k4R0qBKYtXqXPyPf4phRWqYeFwavuEUfDKgsU75v6j5jN1pz1A84SRRPbQ3D0Q2VSYblWzD-7Ra7LRBgYiyHxdZrsPEiL1GnwnD9t59XFyPp-7W7oP9F_dCZppW67tMohygvP8j0CmVrfCs5LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=bShf72abCQ-80qSUO8L1lesfjTCtcXbmyrDs5jm44qxVQuHBBIWpPWobSB4eui4RzFKIh4P-XzeIv_RC6XtxAf0aWQRgPX8XHkJLzq2OCuQ4fB1gEWyhb04Wh1N1nLxY9-65PVNeTBXXmljd4KiVLGeZwYa4KXdLOmcOIozBBC22lVC_zIg0EZi8PE8WKgmBVm-8k4R0qBKYtXqXPyPf4phRWqYeFwavuEUfDKgsU75v6j5jN1pz1A84SRRPbQ3D0Q2VSYblWzD-7Ra7LRBgYiyHxdZrsPEiL1GnwnD9t59XFyPp-7W7oP9F_dCZppW67tMohygvP8j0CmVrfCs5LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
حملات شدید و سنگین روسیه به کی‌یف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69548" target="_blank">📅 01:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69547">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwegdNTHBifrCNGBYkygHXxegJAtLzJ0gy0XVuQg9cqbu5Tb_JUR4qnuDx9M0nPGgkQW20_Dtc7YJ8SvQuFKuQhiDddKBIAYvvAj4-1VcShCCowlGtSuPxOvGrv43LHOLCk1sKpS0hsx1oPPT-iKCSCwQ9DQrIESA-gfgeIKSil8ttHge-mvj1ZgtyBTVOQWrWtfILl7Y9OToksYePyK0Y4Y_z4CtCRHYSAVuugll1RWITzgvNMVTyQQW7Co0A_GklGMMrLrNqanr_fLnqGwGhUzeSa-I70N75xumWrpIUW4hVCZO2k7exzxFrHawFsXiM6UPeerLnzn-D0zH78lPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
علی قلهکی:به نظر میاد یکی از گره‌های اصلی مذاکرات ایران و آمریکا، ماجرای تردد کشتی‌ها توی تنگه هرمزه و هنوز سر جزئیاتش به توافق نرسیدن.
هنوز مشخص نیست کشتی‌ها دقیقاً از کدوم مسیر باید رد بشن و مسئول امنیت و هماهنگی عبورشون کیه.
ایران می‌خواد کشتی‌ها بیشتر از مسیر آب‌های خودش عبور کنن، اما آمریکا و طرف مقابل مسیر عمان رو ترجیح میدن.
اختلاف اصلی هم روی نحوه مدیریت، امنیت و کنترل تردد کشتی‌هاست.
هر اتفاقی توی تنگه هرمز می‌تونه روی روند مذاکرات هسته‌ای هم تاثیر مستقیم بذاره.
آخرین پیشنهادی مطرح شده مطلوب ایران اینه که کشتی ها حتما مسیر ورودشون، مسیر ایرانی(شمال)باشه و مسیر خروجشون حدود ۴۰٪ کشتی‌ها از مسیر ایران و حدود ۶۰٪ از مسیر عمان (جنوبی) عبور کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69547" target="_blank">📅 01:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69546">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKNadVKoMJvUOBHv1cdMsdv45_D4I4Db54hi7DvcmuqGrfz32sWoxNzS6yvCsvTXAhC_CWOo6lx9-xVZ3n21RYj81Ehpy_Ah2D7LixZ2aUpaXQ8u5ybZ-9Lk_4NtbpN8C-uVvZmlUXUozhUFWnzVcQlXpundYy8fHkvO_4W-sb2mnqurQQhzSpcC-ZUSXbpgC0DZwUdth5VaSatZsTd5nukTjt2qSntXShh8h8SfG5e2ie0a1tlbinczIFsh2lJe5xyVaXHiBlk0H71n36YuX4-H_Qa2IznzxoHDYolJK7h7bSmRnRZKKTtosE4dhIAXULB4G81dUFybIo21I8VauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
بازگشت غول‌های سوخت‌رسان؛ بزرگ‌ترین آرایش هوایی آمریکا از زمان جنگ خلیج فارس ۱۹۹۱.
پس از پایان جنگ جهانی دوم، جنگ خلیج فارس در سال ۱۹۹۱ با استقرار حدود ۳۰۲ فروند هواپیمای سوخت‌رسان، بزرگ‌ترین تجمع هواپیماهای سوخت‌رسان در یک عملیات نظامی به‌شمار می‌رود.
اکنون نیز در سال ۲۰۲۶، با استقرار حدود ۱۹۳ فروند هواپیمای سوخت‌رسان در منطقه برای پشتیبانی از عملیات علیه جمهوری اسلامی، یکی از بزرگ‌ترین تجمع‌های سوخت‌رسان‌های نظامی از زمان جنگ ۱۹۹۱ شکل گرفته است؛ آرایشی که در بیش از سه دهه اخیر کم‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69546" target="_blank">📅 01:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69545">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOtVA9SXgZTpcKpebpq70qLfnxzJA0h8cM3UwMLFDmmHJMuNOOidUGelnvwOrma2uzCU588e_i9WKNtoYTUiTwcLKeA5P56f13zUGf6KE_xQYa2FMf8QaCZUFFV3XBy4pvnkNYpM2tXkNu5hMBYvEVipIRD8O_rDXCZvMcMtalhZ0FiIdyCMK7K9AMK3-33r08MiJ40TtWZts1q9y1SYS0aQgrYPwkPFRoVfMLesjrAuXcLwf5qfWzHGLQyZJ3HfA0FSTzPEK_OKpmTnvPPTne8J17zTibrD4p-HWp69drIthbciroHkhDy5zp2PKDOVk5AGRefPn6HU87Z9QYCMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:مسیر جنوبی از طریق تنگه هرمز برای تمامی شناورهای تجاری که قصد عبور از این آبراه بین‌المللی را دارند، همچنان آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی علی‌رغم اقدامات خصمانه و بی‌دلیل ایران، به بیش از ۱۰۰۰ شناور برای عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند و این ترددها همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69545" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69544">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=NF8r_k3izn7kM5-PnxUIThmfeLFPbBf2iVGbm0fgpNaG3doGaSXjaUkRvV2pDuUjYrWkBMcRFhgaoVOT5v299wDLbpK8q6xzH6TvgOYyQeEfcOfz3M4YYK1dzYsj1-VPcD73f5VYKKvN8RMJ1wARO4bQ7a0y1rzQAEGgPY0ddgE1j3tDt1_UEl6TgxgqlT7erpa-JbifGHHklzYb613MtGavgLEK5rWkY_ZXJsgHChyShbDT7WOkx11gGVz-R4MNCiL7giUMUfnhg9Rz5ATyd4MMMMvSmAEkC4Ktp0cobeAeiLt-AaY-3Ugg4VcoxE2L3DU6TRY8Xc-0pClAKzkgxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=NF8r_k3izn7kM5-PnxUIThmfeLFPbBf2iVGbm0fgpNaG3doGaSXjaUkRvV2pDuUjYrWkBMcRFhgaoVOT5v299wDLbpK8q6xzH6TvgOYyQeEfcOfz3M4YYK1dzYsj1-VPcD73f5VYKKvN8RMJ1wARO4bQ7a0y1rzQAEGgPY0ddgE1j3tDt1_UEl6TgxgqlT7erpa-JbifGHHklzYb613MtGavgLEK5rWkY_ZXJsgHChyShbDT7WOkx11gGVz-R4MNCiL7giUMUfnhg9Rz5ATyd4MMMMvSmAEkC4Ktp0cobeAeiLt-AaY-3Ugg4VcoxE2L3DU6TRY8Xc-0pClAKzkgxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم.
می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر.
همه مردم برای ایران سختی‌ها را تحمل می‌کنند.
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69544" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69541">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/My3Bmz3aIJEFchM_cPpyN4ENUzealH2VlLpsAQhBk4Is4hXFuFYxcjtj9Ka5UlVYtQww5bsSVhJLRAMQQWjsY86VYibpd0ZaNAsssCxYFXnvvRhAcskhi1KTxqgsk66atQNq7BaZXckEgruKREnYoDeKT2mGxL4_r94O-G2BNvjAT_e-Yrhop_l-sHMrJu_wQoAtb2t47XNC3pwKIVjv5buk4NWakWy1GJPm6LtCbSmyh3r3DpbuDgVEpivtuSFnVm-TQy5y4WKbyMDWXTlbWZT2NxFunzwrhqcyGjkb93Fc9zLzMB0qye42EHqDpCVVTzuHYZgwAmvttvGICcb-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KBULGeAgwqa5u_Sp_hgTFEL35SwXNO6tBLVG1VC1fZLesRD6638B0U-ebN8tv6G5Qjy3sGg8C3wUUYivpmwlnUr2HuMf4ZSWWy5XX5a9CLJMdM6294jnNGR6HmBpHM9i89DGaZtdktnAKeThIKPXl9XqJl5SBeAtbGl9mBe2v633B7Km9rL399HQ7qQ8vx9LiN_YdCReGOGGiyL77fYLrbdXoxW64EmIp_w79Hi7rQ20D50e74PXUL7j5rfYhaddn6LKplpmuJayMiXuhym5SBhLnUwyvUCWAC6GAnHiFnUrXn_z9kqF9x5DwkN_0W0txXfI42dk2KKvRDWd8c7ung.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▪
🇺🇦
رونمایی اوکراین از ربات رزمی «Droid TW 40»
.
شرکت اوکراینی
DevDroid
از ربات زمینی تهاجمی
Droid TW 40
رونمایی کرد.
این سامانه با حداکثر سرعت
۱۳ کیلومتر بر ساعت
، برد عملیاتی
۵۰ تا ۷۰ کیلومتر
و ماژول رزمی
Wolly
مجهز به نارنجک‌انداز
Mk-19
کالیبر
۴۰ میلی‌متری
عرضه شده است.
برد مؤثر این ربات برای درگیری با اهداف
۱.۵ تا ۲ کیلومتر
اعلام شده و
Droid TW 40
می‌تواند در حالت آماده‌باش تا
۱۲۰ ساعت
در میدان نبرد باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69541" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69540">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqlQULPdVJ2g7uzSiDnzDZHk3mWOiJgitPtBC62RbrL-hnoQ_NnKOx0ktKqSv02HHmiLPCBkIjpo6UtaZAw1jB1_Phls2W44yOKTFZ7KIrxq45-8XrEYzITOOMLds6Jpr5hnmMEFEpAaA8eHnmEUqxpbPZbhgWqUg26im84LAaAixIzfg9MnBqS5fRlpgSmZRlazHtb0W-pwJwT8ilr8ittgW9crOMSsbN53HaNXnTZUYFTNMMawQeEGxiwd2i-sZAoIsJeXJZ-szUKzqonLLXsawNJrTKLfBMqw-y-zj9KM_C0Dm72cvZKg_ecKANn_n4y67wCZpbgX73holZQB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
نقاشی وایرال شده از زمان قاجار:
در زمان قاجار زنان روی یک وسیله تاب مانند میشستن و یک زن قدرتمند، اونارو بالا و پایین میکرد.
شاه یا یکی از سران مملکت هم اون پایین دراز می‌کشیدن تا زن انقد روی آلتش فرود می آمد و بالا می‌رفت، تا ارضا میشد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69540" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69539">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=BhTGwk1KNBVa_dce1-udH4-IPaiDIC3Krs2pkI6yQFibYkcMMLIeJaWf7G0rm07XBlWdcATYoin8bugTOLioUUW3cOr2On3BtEisITPbKzbkeMFLSriCmApUt3Oh429d3dLhpzCbBSkS2HFcWbEO_UbhBqdq-78kZk2QfSJAjgxh2EzMX6xTi1tlYiBXw5w-XE5IRO4O2ImxzKtRC3NVN6x1wosEYetXECNE1sVQG2jOSNiTGCbT9gin-Hfe3HGneQUefqh5MeXAz2w6v_HGT2YrpGJ2DibfHyYkGAfCqZ20WqB0JjYwRuq-uaQqER-nN99QwRZjojxf_gkTLdHC7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=BhTGwk1KNBVa_dce1-udH4-IPaiDIC3Krs2pkI6yQFibYkcMMLIeJaWf7G0rm07XBlWdcATYoin8bugTOLioUUW3cOr2On3BtEisITPbKzbkeMFLSriCmApUt3Oh429d3dLhpzCbBSkS2HFcWbEO_UbhBqdq-78kZk2QfSJAjgxh2EzMX6xTi1tlYiBXw5w-XE5IRO4O2ImxzKtRC3NVN6x1wosEYetXECNE1sVQG2jOSNiTGCbT9gin-Hfe3HGneQUefqh5MeXAz2w6v_HGT2YrpGJ2DibfHyYkGAfCqZ20WqB0JjYwRuq-uaQqER-nN99QwRZjojxf_gkTLdHC7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای از یک پهباد روسی که یک شهروند اوکراین رو تهدید میکنه و در آخر هم خودشو میکوبه به طرف و منفجر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69539" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69538">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3447971507.mp4?token=MCgzKMqe9-Gnb2v8cMzWCsCeftEzNfR-ctdysxOL_Ct5gj0rRmmtFPW2HipRoRE0xQzRrdw3HyRh5KEyaInXvjmaaJfcSFaYkAL7FRg9uvSDTUSBkm-yrmzKSAMg5g6xo1wf8LsPc-6qJtc8wuUWY4w8Q3cmlKS7ZbUFp6T18EG6h6Y_CQHp7KpMJQZqKdDyDtV1D3zPBltmNKk6ECengDIBNY5YGlC-2wLlHXpB3y-oHxDc0aCesBHClKSoMh1wKUEb2Kh_sPngDOwkpHuVJ5EOforh2rPfxxhHEC9c8St-vkyXC_OD2k9MobzW0u0QU01bzizq4zT6qnKJTbgZ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3447971507.mp4?token=MCgzKMqe9-Gnb2v8cMzWCsCeftEzNfR-ctdysxOL_Ct5gj0rRmmtFPW2HipRoRE0xQzRrdw3HyRh5KEyaInXvjmaaJfcSFaYkAL7FRg9uvSDTUSBkm-yrmzKSAMg5g6xo1wf8LsPc-6qJtc8wuUWY4w8Q3cmlKS7ZbUFp6T18EG6h6Y_CQHp7KpMJQZqKdDyDtV1D3zPBltmNKk6ECengDIBNY5YGlC-2wLlHXpB3y-oHxDc0aCesBHClKSoMh1wKUEb2Kh_sPngDOwkpHuVJ5EOforh2rPfxxhHEC9c8St-vkyXC_OD2k9MobzW0u0QU01bzizq4zT6qnKJTbgZ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
چهار سال پیش در چنین روزی، یعنی ۴ اوت ۲۰۲۰، انفجار بندر بیروت — بزرگ‌ترین انفجار غیرهسته‌ای در تاریخ معاصر — پایتخت لبنان را ویران کرد.
هزاران تن نیترات آمونیوم که به‌شکل نامناسبی در آشیانه شماره ۱۲ انبار شده بود، دچار حریق و انفجار شد و موج انفجاری ویرانگر ایجاد کرد که چهره بیروت را در عرض چند ثانیه دگرگون ساخت.
این انفجار دست‌کم ۲۱۸ کشته و بیش از ۷۰۰۰ مجروح بر جای گذاشت، حدود ۳۰۰ هزار نفر را آواره کرد و خسارتی بالغ بر ۱۵ میلیارد دلار به بار آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69538" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69537">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=MXekHXz3KebBU53S8sr9JIg8LV_RbBzKuibwoxpVQC3PMiLR43GdOd7HLaZ-BI7mQ2hST_RSuZHOH4YhU2mGLGt5rGo89hHQJsjPn_wD_m0uTA4SseDJD5jH2MyDHGPG_E-aCSDcSpYM83x2SQ96mLh3x5sr_CLMzPNjYfpeAL88HUtvuoz_n4N_yF2sZ79DpWpD78kz54DbsXiOJsp7fMdLEpXATiMSIw7OxHQZh2IoySGP6EeO8IVthGFbCQIOIwzaeW9zo40gATXV6Deoh7MYGZM_NCJmPpmbLKAzqukA3gUKrVElConOyXR0SybKUhbdjdIdnkjrSBaonBaIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=MXekHXz3KebBU53S8sr9JIg8LV_RbBzKuibwoxpVQC3PMiLR43GdOd7HLaZ-BI7mQ2hST_RSuZHOH4YhU2mGLGt5rGo89hHQJsjPn_wD_m0uTA4SseDJD5jH2MyDHGPG_E-aCSDcSpYM83x2SQ96mLh3x5sr_CLMzPNjYfpeAL88HUtvuoz_n4N_yF2sZ79DpWpD78kz54DbsXiOJsp7fMdLEpXATiMSIw7OxHQZh2IoySGP6EeO8IVthGFbCQIOIwzaeW9zo40gATXV6Deoh7MYGZM_NCJmPpmbLKAzqukA3gUKrVElConOyXR0SybKUhbdjdIdnkjrSBaonBaIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ترامپ و تیمش تصور می‌کنند که می‌توانند حماس را به خلع سلاح و غیرنظامی‌سازی غزه وادار کنند.
آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم.
این پیش‌نویسِ ما نیست؛ ما نظرات خود را ارسال کردیم. ضمناً، ما نظراتمان را پیش از آنکه شاهد هیاهوی رسانه‌ای پیرامون این موضوع باشیم، ارائه داده بودیم. موضع ما همین است.
و ما بر سر منافع خود، هم با درایت و هم با قاطعیت، ایستادگی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69537" target="_blank">📅 21:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69536">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjVzAoFY2fxI5XqLi5wBFKNJhhZ_NZXUDNJC99bCXvmKLkRNI7ghGf6TuJZ_3f1L-SmoakjKhf88l5NjrvSjhMUuQ30gnb6RqdP4dvHQQmhZP6fJ6ELMnlgfSuG6AruxlmZTLpJ9qPjDXvHvE9w9DvcXtszw58D6k9boIFjKXa1pxD20eyyyT3kXWHAVliTZ1f_eOazPMVzSQeLWXTYkZVUI9sQAj4q1QUJWpKCIp1wxWnRPn6uMJG96IFq5O_eQGm6Jr5ZCAkLvo5_PKgmGHKO7etofYNyNtwHJDG4pb1SJs3RE1FOv0r5Ko0W22qWrU-QRy63LGiSRWKWKoSlQZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال‌استریت ژورنال: در حالی که دولت ترامپ بر نزدیک بودن احتمال دستیابی به توافق تأکید داشت، وقوع حمله‌ای جدید به یک کشتی در حال عبور از تنگه هرمز و بروز اختلاف بر سر مسئله عوارض در جریان مذاکرات برای بازگشایی این آبراه، چشم‌انداز این کریدور حیاتی انرژی را با ابهام مواجه کرد.
به گفته میانجی‌گران منطقه‌ای، بر اساس پیشنهادی که هم‌اکنون در دست بررسی است، کشتی‌های عازم خلیج فارس از مسیر آب‌های ایران وارد می‌شوند، در حالی که شناورهای خروجی از خلیج بدون پرداخت عوارض از آب‌های عمان عبور خواهند کرد.
میانجی‌گران اظهار داشتند که اگرچه دیپلمات‌های ایرانی در ابتدا از این پیشنهاد استقبال کردند (زیرا تا حدی کنترل بر تنگه را حفظ می‌کرد)، اما تهران خواستار حق دریافت عوارض ــ که احتمالاً با عمان تقسیم شود ــ و همچنین دریافت تضمین‌هایی در برابر حملات مجدد، پایان محاصره دریایی آمریکا و کاهش تحریم‌های نفتی شده است.
مقامات ارشد منطقه‌ای اعلام کردند که آمریکا و دولت‌های منطقه با درخواست دریافت عوارض مخالفت کرده و خواهان تضمین‌هایی هستند مبنی بر اینکه ایران و نیروهای نیابتی‌اش، قلمرو آن‌ها را تهدید نخواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69536" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69535">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtTBqr9Y7cJXGgnVFOy8H_sdB1-MaofDDq0z1SwI483rFyFyZyGAeGjC_d5p84ZkzcHdEGScrn-WzoPYHlFBthgEB0nXQPZuKkqCw5ZJ4eWeuAFPfzWUkDONwYtVTlHjqHYjrVJII7ScgQZZUWW10aH3KabXyAAmlCxclaKUdNbmqJJSP9bjqimh1jErv5tBkbsGX0dZFLoaSqYc1qZvfaQOYuI27pJNbhqD_J22mafhFP75zdSTpOVQz8gu66UStk3a5UkuSH5ZMM3ZP-A_1WGuqtkvzJOvyqGvAx-RJKTKUT4lT--Vl1EzzWLCIaUeXZ1TDre6SzwB7XwEciiGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:یک ملوان نیروی دریایی ایالات متحده در «مرکز اطلاعات رزمی» ناو «یو‌اس‌اس باکسر» (LHD 4) مشغول نگهبانی است؛
😃
این ناو تهاجمی-آبی‌خاکی در حالی که از محاصره اعمال‌شده توسط آمریکا علیه ایران پشتیبانی می‌کند، در آب‌های منطقه در حال حرکت است.
تا تاریخ ۴ اوت، نیروهای آمریکایی مسیر ۴۵ کشتی تجاری را تغییر داده، ۲ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی دیگر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69535" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69534">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=YXUIqEmlANW7R3PJ0uO_mxc_NEmurAiBX_VKsJTAVwi6wv1RFs1NcBYFVFzflsATgT3t87ovmoVvq3aGV5plrmiyuOwCgE0KIvlT5MQ7vgXjp0yjOT-q7EkR5jGOphrmq5nLCR1selLQDb7RsRHS-ds6iQvmTrRKKuEhXRbIMZnxz5dr9uRosJ_XMtvZUOuhWdhDFFvsUi0I8s4mwoRgUQGw_Z0t6z1nMmo-wXF8DEsxhjkeXn2uMM7MYYTr3taODhpgPieBR-ywwt6qsQukviqXpyNSErc767XclgNncwqH_FzMAZxZRNDWc-52Sk7Yuq_hNOdlN1FhSZKYLKBCrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=YXUIqEmlANW7R3PJ0uO_mxc_NEmurAiBX_VKsJTAVwi6wv1RFs1NcBYFVFzflsATgT3t87ovmoVvq3aGV5plrmiyuOwCgE0KIvlT5MQ7vgXjp0yjOT-q7EkR5jGOphrmq5nLCR1selLQDb7RsRHS-ds6iQvmTrRKKuEhXRbIMZnxz5dr9uRosJ_XMtvZUOuhWdhDFFvsUi0I8s4mwoRgUQGw_Z0t6z1nMmo-wXF8DEsxhjkeXn2uMM7MYYTr3taODhpgPieBR-ywwt6qsQukviqXpyNSErc767XclgNncwqH_FzMAZxZRNDWc-52Sk7Yuq_hNOdlN1FhSZKYLKBCrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
یک جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در آسمان خاورمیانه از یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت دریافت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69534" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69533">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjfXYc2aFoa5GTdVfNwR7ObAE46CHFE3E8NzVK_FV71P5r6B2PUKmDx1HyBbn5F_SIbiXm7Ps77yX7S1670shZg8dS5RRVoty6kYVsnxaVgVlWztsh7t7-pddX8EYZkTFp-7yDjoCavZ-wDOuxrY9WUt_9fweEpnzu_eHg4Ol3Wdn_9TmtMaPMSCt6Tok_n0xCgILrfJsfu5sjWacf09-utCWzRNswQTPAmVjuSUWyJK9HNbwY2H5_6vRHUIAixOFvKfYXezjUbSmRVrpLl7DPNfB7DhSrISobfiwxfZnj6ZK1XKxIH1MOTEl3LihVsIeLwFK0_81SscnjhJ-Xz6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ایران در حال بررسی امکان مشارکت کشورهای اروپایی در عملیات مین‌روبی در تنگه هرمز است؛ اقدامی که نشان‌دهنده احتمال تعدیل موضع پیشین این کشور بوده و می‌تواند به تلاش‌ها برای ازسرگیری کشتیرانی و پیشبرد مذاکرات با ایالات متحده کمک کند.
تهران پیش‌تر به‌طور علنی با هرگونه نقش‌آفرینی خارجی در مین‌روبی این آبراه راهبردی مخالفت کرده بود، اما در هفته‌های اخیر و در چارچوب گفتگوهای گسترده‌تر پیرامون عادی‌سازی تردد دریایی و کاهش تنش‌ها، انعطاف‌پذیری بیشتری از خود نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69533" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69532">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=ZY2IiGg26ug4sir1WcCm_JeJfmd9zO0Z4bUDBK4Y1mPTP6UXKwu8NepcBaBdF4S4Rh8Rk5e7S_W8NAbMrflKkz0qDT9uV1JPc-OKbHcFCaZODS7FEQmQNx7Ht68ES3uPrh2vefgahPRvS5tvpYTro4nAF2vZD2MBS1uhxZVR-4LxTIRWqkA_aVmsUeIsjVjsrQbyJGMj6U7P635HeBRX6wn8M16duRJwqb_ruHEH1qVgIv3BLt7rFuoROzZ7IZ94O7QBXCrOB4eSVqAZF1jQGXNXfUHtW8kDkpYVWnEV7NZUaaNHZxq2XGSQ1l1_3kVTa3C4Y1ewWpjweh76wvolrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=ZY2IiGg26ug4sir1WcCm_JeJfmd9zO0Z4bUDBK4Y1mPTP6UXKwu8NepcBaBdF4S4Rh8Rk5e7S_W8NAbMrflKkz0qDT9uV1JPc-OKbHcFCaZODS7FEQmQNx7Ht68ES3uPrh2vefgahPRvS5tvpYTro4nAF2vZD2MBS1uhxZVR-4LxTIRWqkA_aVmsUeIsjVjsrQbyJGMj6U7P635HeBRX6wn8M16duRJwqb_ruHEH1qVgIv3BLt7rFuoROzZ7IZ94O7QBXCrOB4eSVqAZF1jQGXNXfUHtW8kDkpYVWnEV7NZUaaNHZxq2XGSQ1l1_3kVTa3C4Y1ewWpjweh76wvolrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسن عباسی:
زیر جزایر و سواحل تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69532" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69531">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfGpF1JfB0fr8WX3X9CHH9RVKVabMb4uz2BrW2TlgaqEBQVyrHg3k7-ubr64CWG1rvdFMpZe7fdnT0tzm4j5yC8kWODtZUVeEr6UEVcBfOoLoCicTdLxRvhc7KkfbRxukqfnIZigAgB0Ypby4PXqJ2aXYhSkPzy10jYT_yl6xVJpvGB39zGwaRYFj4NHOgJwzGaqz4a3Tt9DjxLz--qjijfV1kCeKFjAcMSsdIFJLjGap7UTVGF2tbnGw_SjG5tbDduf8mkDMlzu0KjnfkAFwXe0OWSkFB915_qyV6_H8Xg7lLx8wya0i3D1kv6738Bs8tp6_znRTDWJ1cMrt3C6eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69531" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=G9Vr5L9z-FlvoMBulbWG9arRTYlzBrD0s2OqgrX8x-8a3wApdrR06dZbAfJho-dDuTH-4QGW8KS-NKaTNly-k3HeUYKoDfaNRZpoJDFZIwzIZNx6YprJDBOQba7TKDlE4atybL1RROfjZV6cDm6UIK2ONjug9yv-9NIpwIa_rxF06LLU099tEV2ahPKCBKGQ9_ZPioerif-MBLCCVHPLFmvQuwhh5t32ROZolU1tF1xjnMfofiacpPLtBi2mEZWDIaTxswgY9ckTm0y-psvWuUU4dVFdFMOYf2unP9JYqB4vkAMuK2oDOQUz_dnbxVxPSHgiMC1g-vtc-i5U-MyKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=G9Vr5L9z-FlvoMBulbWG9arRTYlzBrD0s2OqgrX8x-8a3wApdrR06dZbAfJho-dDuTH-4QGW8KS-NKaTNly-k3HeUYKoDfaNRZpoJDFZIwzIZNx6YprJDBOQba7TKDlE4atybL1RROfjZV6cDm6UIK2ONjug9yv-9NIpwIa_rxF06LLU099tEV2ahPKCBKGQ9_ZPioerif-MBLCCVHPLFmvQuwhh5t32ROZolU1tF1xjnMfofiacpPLtBi2mEZWDIaTxswgY9ckTm0y-psvWuUU4dVFdFMOYf2unP9JYqB4vkAMuK2oDOQUz_dnbxVxPSHgiMC1g-vtc-i5U-MyKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
غنی‌سازی اورانیوم چطور انجام میشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p97U5erLPHgiBW3X33bl54AIhdDgkMp--_L7vqVDZ38V-g4T_nftNeM3bKAgHt5rHBhbAvGQ8ZZCDURn-jXM_PrNpHxIlyMPGmbA3UVeBytagDOIFsmiy8tmImzlw1_C4FUaJNSW-Salx3sRMytRgDjWyscMywsf7gNkrqR_AklteS5EwdGP8Tp8QWLJhhKpccBhZGOGchhJpdrkatcVDj1H1vo0uFiE-JS2tbWJJICU6rZJlD0AyrIZPMxPzG-7SfBtuyEzi2WaxjsEGhp_LGFxS6l2pgMpP9vBph2A-DJMaF-HzNPMQrTT9arNvbQj6ksPsGkL68kRBq5mSg-vag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=hEN_GOZnLV7mKmNfXEwa81IQBRvv-9u6oQt7UbGCKF75S1Ql8YLuEJC43kln2rUuUbFyPolUGypGVqgvoZO9AMLzqsfY9sxLNGbfkKiERT7h7C0euvQ1-7jBaHJ4WZxtRUiaq49LXjZRs3QrE6piILqWk_kHLQY-SGun87aitx8nz9dIa_8FES47gLYXtcwqGLIlKUwUTjyW_L4X04F4ffRbmi3XoyePh_qGzzRkABdQqVbU5LfPTPsk9AhPQ9Q_m0GXrqqEUWD2SO2sl44TLwxpxHKWtHKzT6vYLDP4A6ivTUDT7YGLKTRdGEZU7S2FO1zY1u-MqWxi20TFxaadlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=hEN_GOZnLV7mKmNfXEwa81IQBRvv-9u6oQt7UbGCKF75S1Ql8YLuEJC43kln2rUuUbFyPolUGypGVqgvoZO9AMLzqsfY9sxLNGbfkKiERT7h7C0euvQ1-7jBaHJ4WZxtRUiaq49LXjZRs3QrE6piILqWk_kHLQY-SGun87aitx8nz9dIa_8FES47gLYXtcwqGLIlKUwUTjyW_L4X04F4ffRbmi3XoyePh_qGzzRkABdQqVbU5LfPTPsk9AhPQ9Q_m0GXrqqEUWD2SO2sl44TLwxpxHKWtHKzT6vYLDP4A6ivTUDT7YGLKTRdGEZU7S2FO1zY1u-MqWxi20TFxaadlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:
کشتی‌هایی در حال عبور از تنگه هستند.
هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است.
تنگه باز است.
ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت و هم‌زمان با حرکت به سوی مذاکرات بلندمدت‌تر پیرامون خلع سلاح هسته‌ای، امکان عبور ایمن تعداد بیشتری از کشتی‌ها از تنگه هرمز را فراهم کنیم.
در مذاکرات برای بازگشایی تنگه پیشرفت‌هایی حاصل شده، اما هنوز توافق نهایی صورت نگرفته است.
ما امیدواریم که این توافق به‌زودی نهایی شود
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=T4flvaw_lbYtNQiKzYVQw_oxYfvv_hAPQtXypwCFGxTDEPy43FYy0FUrIuPqJjXxLr2a_wsn8NayMG8MWNPQxDum7CnqZcSe3SbYHEfF_imvG14LDq_gvWfwLUKdXo4TsBkwVUhscp7MbAI8fLNX_UbiB7CfSK0u4GT3e6K3EihBzh8rWesM-qeV8aehzOtq9QKFQWTFIE6qdEREr1huYSxKw8w3wOrw029w_Hd1qdCyMmigzmm6Wx3iAWSeKx1efCsdr7WnliocWJL0ebKl7POPHn9-0BGlBWSrmCFTVrbFyGjYBEmtxopKZsWclCKxhm8JX6R_kQhLlRlP0bNd3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=T4flvaw_lbYtNQiKzYVQw_oxYfvv_hAPQtXypwCFGxTDEPy43FYy0FUrIuPqJjXxLr2a_wsn8NayMG8MWNPQxDum7CnqZcSe3SbYHEfF_imvG14LDq_gvWfwLUKdXo4TsBkwVUhscp7MbAI8fLNX_UbiB7CfSK0u4GT3e6K3EihBzh8rWesM-qeV8aehzOtq9QKFQWTFIE6qdEREr1huYSxKw8w3wOrw029w_Hd1qdCyMmigzmm6Wx3iAWSeKx1efCsdr7WnliocWJL0ebKl7POPHn9-0BGlBWSrmCFTVrbFyGjYBEmtxopKZsWclCKxhm8JX6R_kQhLlRlP0bNd3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو پاکستان، یه تجمع ضد جنگ برگزار شده بود که وسطش یه گروه جنگی اومدن انتحاری زدن در رفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=ctSlnAtD_d5BYNb5qPTIScQ8K4N9pZxm-tSzhry1Ut6nF8ygp-sSA5hQK72tD3gurANNuQ7Spn46-12C8OshHSzZewx5vJZ_UfC0oWQlmGmTsnzOhzKGhOHfbYF2ybDgoz_gYrfQjNrVo8xcxKbFc9YG73hTM3b8LGoLk_oObISa5dw9H_spJWRfKtYckl35k_p3pN2oXki2ljOBj5BUkXkyaCc5hIOEVDMPUlSgxRVcy4wISQxgLitaugvtfdAlh0ea2Vwc7A3BewKiAeGIwa6a3BYElwD1WDyTl6Q1byYuxdcZULgQDfgZDMxYHsOqOp3geqW7sHAo5vBFVL36lpm9Y1V8NSLK-XwAWBQoeEs_wfylCcaHhBvCvkKL2LIDibRV9s3ZbYHuJabCb0jON0lY8i--w33DCOEVJdOVhL1G0aRA89FEygid09m1mVxGIhlfjsM08uxZy_slMp4GBFI0k8KxRt_pGZCXXMvZNLad2qarKf1zOHeZLaQi0B5wCxdCBLYr1kdFeRx5pCylOqNqjNfxEJ6hdZLflYLlxn96oS2YJvPCNRjppVcFpx-LAx5nEkY-rKbWpBGPioSUMQrndpJs4jWX3u7FB652hDUR3QwJRoKSaV7sMmmqQ3f6EgbpSgpvoRk4zhGEQp8oSz1b7on38IuXfFNRHSbGszs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=ctSlnAtD_d5BYNb5qPTIScQ8K4N9pZxm-tSzhry1Ut6nF8ygp-sSA5hQK72tD3gurANNuQ7Spn46-12C8OshHSzZewx5vJZ_UfC0oWQlmGmTsnzOhzKGhOHfbYF2ybDgoz_gYrfQjNrVo8xcxKbFc9YG73hTM3b8LGoLk_oObISa5dw9H_spJWRfKtYckl35k_p3pN2oXki2ljOBj5BUkXkyaCc5hIOEVDMPUlSgxRVcy4wISQxgLitaugvtfdAlh0ea2Vwc7A3BewKiAeGIwa6a3BYElwD1WDyTl6Q1byYuxdcZULgQDfgZDMxYHsOqOp3geqW7sHAo5vBFVL36lpm9Y1V8NSLK-XwAWBQoeEs_wfylCcaHhBvCvkKL2LIDibRV9s3ZbYHuJabCb0jON0lY8i--w33DCOEVJdOVhL1G0aRA89FEygid09m1mVxGIhlfjsM08uxZy_slMp4GBFI0k8KxRt_pGZCXXMvZNLad2qarKf1zOHeZLaQi0B5wCxdCBLYr1kdFeRx5pCylOqNqjNfxEJ6hdZLflYLlxn96oS2YJvPCNRjppVcFpx-LAx5nEkY-rKbWpBGPioSUMQrndpJs4jWX3u7FB652hDUR3QwJRoKSaV7sMmmqQ3f6EgbpSgpvoRk4zhGEQp8oSz1b7on38IuXfFNRHSbGszs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=nvTK2drfXJA_LmRdulkLsksw8YaToKtKceYAaiHMhmERM27coiDJAWKxmAfWeHPslkGi3zh61qkyWOujxgx8kkF7WCDSnOmWqKCz5_J2XhY-k2CF-V_NgtVJwprcsXYN0sTkr2TYy9ArLfkzq_CwsqOKrUh1Gcvj_5uUbfPAP20kIVBIrgphCqTcviOxvH6Rq1kCeK5Mm4ZtD0fZgXgcTNG5lVQy7buWOKGJ_tpJBfR1oUuywaWw5ncq02lLj45JDQUxcA2aoqZ-Cfzhn1HvN_1gk0alJQ3nSQPmoGHel2AuKfyga5MU7tFw5dDNtpPt9zIelR6KQzYHDS-HVGwLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=nvTK2drfXJA_LmRdulkLsksw8YaToKtKceYAaiHMhmERM27coiDJAWKxmAfWeHPslkGi3zh61qkyWOujxgx8kkF7WCDSnOmWqKCz5_J2XhY-k2CF-V_NgtVJwprcsXYN0sTkr2TYy9ArLfkzq_CwsqOKrUh1Gcvj_5uUbfPAP20kIVBIrgphCqTcviOxvH6Rq1kCeK5Mm4ZtD0fZgXgcTNG5lVQy7buWOKGJ_tpJBfR1oUuywaWw5ncq02lLj45JDQUxcA2aoqZ-Cfzhn1HvN_1gk0alJQ3nSQPmoGHel2AuKfyga5MU7tFw5dDNtpPt9zIelR6KQzYHDS-HVGwLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=crOd0BI3qKnhFbpecpt4cDDSd37f9yTdVuj51OF6gMZE_UXbuI7r85TAPHU6n0WC2CliIFNtP4AAC_xrHW9Z9huDkWui4gYIorkl4ZFdNu8Hg2AJQYVDthcEgCf_V2hNxEHVE7NmNm5y3wM1F_7-l8ypd83TbWAsJncZv76ejKAb6Apcfc1e96yxiWifo90c1ZeIyZhX3bpHreD_uqRUPFNHyCIRVdJEALtCery1thvaS8oWPxT4zf-SGJW1BNmR0Sk_USt-PmktaZLNJRAOVbimXs0a48sBDrIyKeyToIuE0IZduVqQfAo78dC_a62IrUfvFg1ELEWZzbwLQRGrNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=crOd0BI3qKnhFbpecpt4cDDSd37f9yTdVuj51OF6gMZE_UXbuI7r85TAPHU6n0WC2CliIFNtP4AAC_xrHW9Z9huDkWui4gYIorkl4ZFdNu8Hg2AJQYVDthcEgCf_V2hNxEHVE7NmNm5y3wM1F_7-l8ypd83TbWAsJncZv76ejKAb6Apcfc1e96yxiWifo90c1ZeIyZhX3bpHreD_uqRUPFNHyCIRVdJEALtCery1thvaS8oWPxT4zf-SGJW1BNmR0Sk_USt-PmktaZLNJRAOVbimXs0a48sBDrIyKeyToIuE0IZduVqQfAo78dC_a62IrUfvFg1ELEWZzbwLQRGrNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXMkwvwuoXnsmVJNtX12EZdOXjrTkUraWa7yqCMiLVlKpYksZbf1nDiSkWsSeHuqK0GnJQ1WLUtRoRyZf3G9DlY_xtfj2ib2xSlmB8g4DtAJYTyFUwG3vbYcKoaBvWF4B4f7-p7CZRK0ggT64KF6-PTlZvKStyEWn2Sex7C5WfzK5bIC6_MI493bHM3SOQzWzZr2cAjoDnscY1iY5LUe1GtHxd6pl7sTVximOB2N61u8BPD4pNbhBJHiKL5pDJb5jSzpmE35uEcWk8kR2DqDwxTyS06OFjh9ybN_rNAk8y90NJz7zaESyCRqwHGITO_CfVScHHuX_1G4rAuLDOvf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇺🇸
🇶🇦
🇮🇷
سخنگوی وزارت خارجه قطر:
تلاش‌ها برای دستیابی به یک راه‌حل کوتاه‌مدت میان ایالات متحده و ایران در جریان است و متن توافق احتمالی نیز تدوین شده است.
این پیش‌نویس هم‌اکنون میان طرفین در حال تبادل و بررسی است، اما هنوز دستور کار مشخصی برای مذاکرات مستقیم میان آمریکا و ایران تعیین نشده است.
تمرکز دیپلماتیکِ فوری، حل‌وفصل تمام اختلافات عمده نیست، بلکه هدف، دستیابی به کاهش تنش در کوتاه‌مدت است که بتواند راه را برای ازسرگیری مذاکرات هموار سازد.
برای بازارها، این تحول سیگنالی مثبت محسوب می‌شود؛ چرا که هرگونه توافقی می‌تواند خطر تشدید درگیری‌های نظامی را کاهش دهد، از تنش‌ها در تنگه هرمز بکاهد و فشار بر بازار نفت را تعدیل کند.
با این حال، همچنان باید جانب احتیاط را رعایت کرد: اگرچه پیش‌نویسی وجود دارد، اما هنوز مشخص نیست که آیا واشنگتن و تهران هر دو آن را خواهند پذیرفت یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hquRS21-Op6lz-LGiBGATEDU1NiE3XGQ8wX96D-4GkMQlaB1LiBqT0gdhtLlv2cFMxHP0iDlzPBe4L2NL73zUR1tPRmqHZTJk7ogTgoWW_w2dZKGroJAYWHD3OCiCK45uRUk2vQX_OvTzxzuLhoO2RngSWtyevwNjUcsaZwvKOfszFb8kQpB3Dl3KMGYmiOPT85RrpKJarlLvInqPkIskSN1NhJmV0BH5ZSykoNSFs4UARzT32SLsiPz6fEnVZbjI6SsV1cyIJdoS0S-gJ7Y3NSvpKHF_KBtHZuc9JOhvDyk3otXiBAFFKxcErYDlWZsyoQabj9JjIggEPraoEdBjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=fkFkkwgg2rALSVtjHpBqI_xdiKI3GnNSDIZDWiW6p7KdS-yGNPvywHo03pxYqGEU7IBhH3C_OVjWcEcTmtSuwJR_H5Gw4mfuMsBvy458e5RmINnV2Ac5_Md0GJdVZZp1Pn95DoHr_c1srYGTqzKWVBtilwKiS5qXqzQOdMV5snh1XOzRuTMeHl4dLSk2lkZ_O12AqcSHerLNpw7BK1cqs6mQ3FWTLq6mwt2AItKjWIvI0og64WowdMf4JLF0uwjPK4QR-ieGqUyza2ZcvE7K4OoroRWzkruQEaH7S56nstu2se9VHRikZQhSNfJcRKEMff9WmcGX4PZER3Di_JpdxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=fkFkkwgg2rALSVtjHpBqI_xdiKI3GnNSDIZDWiW6p7KdS-yGNPvywHo03pxYqGEU7IBhH3C_OVjWcEcTmtSuwJR_H5Gw4mfuMsBvy458e5RmINnV2Ac5_Md0GJdVZZp1Pn95DoHr_c1srYGTqzKWVBtilwKiS5qXqzQOdMV5snh1XOzRuTMeHl4dLSk2lkZ_O12AqcSHerLNpw7BK1cqs6mQ3FWTLq6mwt2AItKjWIvI0og64WowdMf4JLF0uwjPK4QR-ieGqUyza2ZcvE7K4OoroRWzkruQEaH7S56nstu2se9VHRikZQhSNfJcRKEMff9WmcGX4PZER3Di_JpdxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqL7IxY49S9H1JuFCohISMZQnBIyKZsChYnQwul_ntevuRm7JZ3PNf9cewfN7UGqjDxyiic3hYR8a6kFe3esJq5J1j1lY8Z_QiUOjAnW0tK6nRXrtoZBnUFLGJiJqbRA5PYvuXk1UDS_XF9QgW284Oa6oYvvEWYEls5uYgJxhyayI578fu4kPllO29rHOMKTAVGVw-GPZQDR69H04U6Jjfjes1-CpwNVUA72nAq-TDc_omt88ChLsleTH0TsVg2UV1lCc-HVFOczEPHp_Hs11r89Hp__h0QOKe8tu2Cxy4YoCgbmhnob54VevfA2VqYxBNDjVP40IxuLnenHZFzcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akveQtWQ7DN3ULPsHN7gEAPG5_WSWXuOp3ZQvbt1hNZ-glwW9rhrLy1ymNkzQIKmpwJra-LobrfFMi6hg_PcNV3su_meShndIBFltsL7wQT_ycF9AMOzOTveQD4cHBF7db50PDCbP9gz78kEL7RTPA0yebmf2rbyobGstd0Z7oH-NSW94Ih6ATK2THO9xrXuet_llGUJdmUUhMP6DWq7yYh5YG2XFVN35_HcxFU1KHB5AsevaiY-Lz4svlWT70wVdSbD790yVHebs-l4_YWv4v96MXSVs0qnMn8ypdt_y-VFHvsCBH-FVuj_svcD3FfxaSLmWU-4IbJF8AMqatCH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CA1HN4G8vDXoEroKY2-bhS64DPzIT-8gsKlBn2UuypDwmeFShqt2LXzmyYd8xwUVexdt4NCpdYLdMT2lfm23xEk3ztC3ScmrxYzn1D9VxMZfAH6b4-z8-YfwAW7TK65FWEkS08nhomBZK1IOpDtrqxq-IxvH1ly2b3GnJ5x_5AAlCtGV1zt2DZZlep6dyRC45L9vTCS9HJjIzyxI7gsNM9fy22yhAx1kzxhKlup6ngKX-TEyHvBP_psONxX_CpZX9_eEKBsb7bQMKe8p5z6mBOzC8RyD04hsVgGJbYSlTRNwv9ni26oX8_bZi5SfSlw8wjC0FOLgmjgNq07ThLDDgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PxsMedRJWA-6P0-iR_eF7KKXn4mhG_WF-q4-P3Am9ImdqNLf0t-MWRoZVeMrpaCWfmW4TgyfKY0xjqakDN06YQE08GInViqCjx2sHMGxUJy6M0A2u5-nTjAqCAmB6-xAQE_ir3DR4Ka-ub2XE62LMocZwDg8O6uusyw0ep7rJlsLGTsMOYbP-oXVKM-TwpCrMy6kSnuUBTjCJ4F6g4DkSzoXLa0KPQwPYbEHO-E1rJUaru_2nmaD4WDSGJgXJulneogldeR24BVDDiaROAG_7_DmURbFxemVoqt5MvmYSuombXWBe_t90NJrh-InLIn4lopK-V4REj-UyVpV7wLoMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRQy8TkSyZtemtynQThnR3EmZaSx3tHhfX_e4RYEWPlubPxkFy5R_pYn4UTmumPWztpx5XE9ozp-SzbMvT0b6OSHmm5WPX6Y0FN8SQKG0UR1uc39beKlfFtFgG93rLKy0vH9MYf3lM2Eg6kFGPuUQxh6_UG7b0nVrSHl6L1ao86mwGb0KscWRjWx8f2xVdyVQ_1uI975EIGnChMgqKFlyHQsEAUf2mLg1steS6q4JraRjQ_Wns1cIJ-5blK5-mVOPAsh__oXjrXN4WYzkwTd-WKDsKZtfDiWkw3QKo6eChldYOkxSrlNc-vcfoA3qFdmUW2H2rIetfzchjBjLVTu6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=i_xDjm2JfT0dObeuIJVJf0MptL3eXwGXA3A7rX4qSdFqsm2LLlFsIcW2-Vj876WS9V_RkRcYsgkykiH0w5Tu_qVHgr3PsRCnNqZybEX1FWzIckMM1nLfXjxraC-32bxGvyj5N-q4jzhZcD6f_wwsIWfj5xC2LZJHqaVlvIxRx-rpB1weqzRVu0IU0uuRECuUTHMHTbCuf0esdw1w2oFKDSV0T08t1SKrOXOtFFfRpfyOijrNQg-4XLgBxB69yZdOpS-lrqAoDG1tfuXU-8Y6f9rVtJW1L4vImFDGu6TJ4ug7K6tPR3asnxDhIvHBBjCGICeYM8NsT763KzbDZClxTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=i_xDjm2JfT0dObeuIJVJf0MptL3eXwGXA3A7rX4qSdFqsm2LLlFsIcW2-Vj876WS9V_RkRcYsgkykiH0w5Tu_qVHgr3PsRCnNqZybEX1FWzIckMM1nLfXjxraC-32bxGvyj5N-q4jzhZcD6f_wwsIWfj5xC2LZJHqaVlvIxRx-rpB1weqzRVu0IU0uuRECuUTHMHTbCuf0esdw1w2oFKDSV0T08t1SKrOXOtFFfRpfyOijrNQg-4XLgBxB69yZdOpS-lrqAoDG1tfuXU-8Y6f9rVtJW1L4vImFDGu6TJ4ug7K6tPR3asnxDhIvHBBjCGICeYM8NsT763KzbDZClxTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=r7uPy3HsDUn2rkr59TxRCjFuZPWqANkD0eQBTor13NMuq3XBpj0iEMTseidKUvGKiAJbSHaJmuqIbZxn38zmBbjjWimuVfb5gqgOz9w9CqSvR_ZSkPvSdQghBFqyQdQD4znVhoBtp2A1AEJ3TI7U5t08KY1mpnqKNQzPCM088jZqys9_OwFPocFub5LGod9dMHy5lpWbb9p08JyjnUgEkcJMVSh6yfFh5zpB8YEQi-YXUSnXaFqGmQ42_sVW-2_hiK0VxeVhVf_KZqXQTIvA66oyT9gddCNYJlH_0cvYJTR7ry9_b7w7EjC-gXxitKuGQhsVwgTuIODrHDvkiSHlHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=r7uPy3HsDUn2rkr59TxRCjFuZPWqANkD0eQBTor13NMuq3XBpj0iEMTseidKUvGKiAJbSHaJmuqIbZxn38zmBbjjWimuVfb5gqgOz9w9CqSvR_ZSkPvSdQghBFqyQdQD4znVhoBtp2A1AEJ3TI7U5t08KY1mpnqKNQzPCM088jZqys9_OwFPocFub5LGod9dMHy5lpWbb9p08JyjnUgEkcJMVSh6yfFh5zpB8YEQi-YXUSnXaFqGmQ42_sVW-2_hiK0VxeVhVf_KZqXQTIvA66oyT9gddCNYJlH_0cvYJTR7ry9_b7w7EjC-gXxitKuGQhsVwgTuIODrHDvkiSHlHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=HsUsL-KyJZdhnIhzVk88Mb9F9u7kJqCmqu8Oyk4mAGbLnyJAdmiU_PFeafqyKEXFXnDhsMyHMoIdFW2h6eVEPkEW1dDsdJyKu2esBxirCs3Y1bv7_nPnN20DlYqm3t_Yi_7XCP1JwxXV4zfW3i-CdTdCgxmQkOBy0FPFQJT1GayEUXsqbRV0jejqEU-Tbs_rDXT9zmzsoCrAyBySmlj1hRQyKlKgnU9Rbh3EPc6qLBC9It92r3zL1E84LanjoVrFPkhazlwey32FReWJak79xlAsRuidY13jYRRThWyhgI81Q6F0ND3CqWFq5Tbd_NNitI8NzbymqpNo2Vm5NhkI3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=HsUsL-KyJZdhnIhzVk88Mb9F9u7kJqCmqu8Oyk4mAGbLnyJAdmiU_PFeafqyKEXFXnDhsMyHMoIdFW2h6eVEPkEW1dDsdJyKu2esBxirCs3Y1bv7_nPnN20DlYqm3t_Yi_7XCP1JwxXV4zfW3i-CdTdCgxmQkOBy0FPFQJT1GayEUXsqbRV0jejqEU-Tbs_rDXT9zmzsoCrAyBySmlj1hRQyKlKgnU9Rbh3EPc6qLBC9It92r3zL1E84LanjoVrFPkhazlwey32FReWJak79xlAsRuidY13jYRRThWyhgI81Q6F0ND3CqWFq5Tbd_NNitI8NzbymqpNo2Vm5NhkI3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu5lvw0vEj3zlV7J74voJSYP6oyIYNutpS4AT9AAMm7-C3PN3F4aUH19z3mHQppKY_JyxOe4XVq3dFKE3q0rIzXF8Tp4UpmrA9_e00ds9JShtNU6MbwuWLRIuL11UUFmELON7gzDwI24WuC88Se7y04VNxh1r50tSu3wcKs7do5jN5kfOzku26tTryo_l1MJdbuKs9qjgWTroq1G9QgEJLE8bEalP869DFzWABQXEdrTrFCntq6qr73WjjOI7fTRIOsJu7w5LreiyB_1P792oU8A5OnuPW7WkgIQbIrNaMMKBCOQdQn1j_aZXEYMALcfj8oYr25JWb4eSUQEeZvxkH8o" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu5lvw0vEj3zlV7J74voJSYP6oyIYNutpS4AT9AAMm7-C3PN3F4aUH19z3mHQppKY_JyxOe4XVq3dFKE3q0rIzXF8Tp4UpmrA9_e00ds9JShtNU6MbwuWLRIuL11UUFmELON7gzDwI24WuC88Se7y04VNxh1r50tSu3wcKs7do5jN5kfOzku26tTryo_l1MJdbuKs9qjgWTroq1G9QgEJLE8bEalP869DFzWABQXEdrTrFCntq6qr73WjjOI7fTRIOsJu7w5LreiyB_1P792oU8A5OnuPW7WkgIQbIrNaMMKBCOQdQn1j_aZXEYMALcfj8oYr25JWb4eSUQEeZvxkH8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=YcWSxazxrlDlW1ffDkAINu1ZZNrBlPjNzszfl_dGq-iCeRoRwhhDVm0cxjZYhO97dgebM1euTYO8UnYrg5ZLv9__UT0Hx9jPUiEFVRr7jehIjAWhfWglqC2_FfxbxFEi6RQgfwMOaCa2p9Jcyn9XTZHckoOPBrJnNs__BK0SjjheXF8TBQmXlMfarCmj-8hotMJ9W0mERkopOHeFbK4LrD0Jl65zqxpKgGOa6tNJEF88Dl5MqhSTgAHyTdz5kBo_eu5UjQpsnNIwLz2kpLW0kT-YkjwEl96eqkyaAP9aMH_UC9Mi4I2FzCnym8a_sk9K5vjyKGKG-9qxIZM_3uLD6Utnfqh52KfEJzFwBi0xpWTTzN5XHwS_TW6zfkgweM8Jm_ZoUMreb8-B9Dssg9gfaVoOv2iO_CqTwoKyXq2wlA4224vuXQ3Z1eQ02QEz-5p_EnDdnlOiwxumzNwIIX1GCVWczJN0gtNo4pqOuM5FVVn5FIGnJaaSDwPlb46W-UKj_8w5HiBQFswHAc1h5BtDap5-0pkqXIaiJjVJVr0JsnvU_IYmrZobxqr1fXuING0YcAck5R9qD8u-gB-1YftQOEj6qYTwNKt8Il7CSKKw3ypUWTvtKj9dKPm32hhPZCv7EiEb-bRThzbH0WgbunoLo5qw8U_oARl0dStKi6-KbL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=YcWSxazxrlDlW1ffDkAINu1ZZNrBlPjNzszfl_dGq-iCeRoRwhhDVm0cxjZYhO97dgebM1euTYO8UnYrg5ZLv9__UT0Hx9jPUiEFVRr7jehIjAWhfWglqC2_FfxbxFEi6RQgfwMOaCa2p9Jcyn9XTZHckoOPBrJnNs__BK0SjjheXF8TBQmXlMfarCmj-8hotMJ9W0mERkopOHeFbK4LrD0Jl65zqxpKgGOa6tNJEF88Dl5MqhSTgAHyTdz5kBo_eu5UjQpsnNIwLz2kpLW0kT-YkjwEl96eqkyaAP9aMH_UC9Mi4I2FzCnym8a_sk9K5vjyKGKG-9qxIZM_3uLD6Utnfqh52KfEJzFwBi0xpWTTzN5XHwS_TW6zfkgweM8Jm_ZoUMreb8-B9Dssg9gfaVoOv2iO_CqTwoKyXq2wlA4224vuXQ3Z1eQ02QEz-5p_EnDdnlOiwxumzNwIIX1GCVWczJN0gtNo4pqOuM5FVVn5FIGnJaaSDwPlb46W-UKj_8w5HiBQFswHAc1h5BtDap5-0pkqXIaiJjVJVr0JsnvU_IYmrZobxqr1fXuING0YcAck5R9qD8u-gB-1YftQOEj6qYTwNKt8Il7CSKKw3ypUWTvtKj9dKPm32hhPZCv7EiEb-bRThzbH0WgbunoLo5qw8U_oARl0dStKi6-KbL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=TFj37kDSshM_ry0f9u1xiHOOaqTzQXv0GZ4l1036RmYLBTzMPketUJSRj_FTWL6kE_-AXDrgfn3Eilk0xy89eE8I-M2c4a02vCH4gIxa602ixBKfb8q39VR-uuzosxvbz49mBa29FXtivqklDl4HMCOGTcLnVHlubyNld7plDtnPCGNUxyvQjZXLmcNyu_Gzx6b2l2e1hfN38RivUxzXmHZNHK4mCRvcwekVcd2fU_pbKQhJlupG7XQMesOhhSsaLrCr9-NdDEBMMdReyEhwmCqNvmbm8C2eCQNYHPoKBxpAVhKiO_PdIqP_pp3Q-BuZWLhoeKN5kCsSl3eT8ZHC0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=TFj37kDSshM_ry0f9u1xiHOOaqTzQXv0GZ4l1036RmYLBTzMPketUJSRj_FTWL6kE_-AXDrgfn3Eilk0xy89eE8I-M2c4a02vCH4gIxa602ixBKfb8q39VR-uuzosxvbz49mBa29FXtivqklDl4HMCOGTcLnVHlubyNld7plDtnPCGNUxyvQjZXLmcNyu_Gzx6b2l2e1hfN38RivUxzXmHZNHK4mCRvcwekVcd2fU_pbKQhJlupG7XQMesOhhSsaLrCr9-NdDEBMMdReyEhwmCqNvmbm8C2eCQNYHPoKBxpAVhKiO_PdIqP_pp3Q-BuZWLhoeKN5kCsSl3eT8ZHC0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
محمد باقر خرازی:
اگه پزشکیان یک بار دیگه استعفا بده، مجتبی خامنه‌ای موافقت می‌کنه
.
مسعود پزشکیان تا حالا نزدیک به 28 بار یا استعفا داده یا تهدید به استعفا کرده!
قراره ذوالقدر رو از دبیرکلی شورای عالی امنیت ملی دربیاره و محسن رضایی رو جاش بذاره.
مجتبی به عراقچی هم گفته دیگه به هیچ عنوان حق دخالت تو مذاکرات رو نداری.
همه اینا همیشه تهدید به استعفا میکردن ولی از وقتی مجتبی خامنه‌ای تهدید کرده، دیگه فیتیله‌ها رو پایین کشیدن.
ماشالله مجتبی خامنه‌ای خیلی سفت و بی‌تعارفه ، پدرش یکم تعارف داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp677hiSeDl9R7D-1szpuUhdxp9Q3BcqH44K1uxXUe4XH_cA5mgW_6k5saP3CcqJIy9HYMd1mQ4m47U1J6f5H-8iRxKUpuprrWEprBld8Ur5rPvATHCLjbHNSf8kMPxEygjeFSgmOr4-A_e2vqtPNspyWWatSGDXqG2xgNd4A5v_lNK6fqJfILkyOgbNflIe4SdWC9UQ-X572EK01Ybj1gGlR3K7TkZP0WNKAoEvJbDvBDlleR4jIFTqj7I2lHFA6BwUxLF5abW9bHwgQKowwbZXeK7jD1WrpI-8RPgrxGuI0lV9lmwIHwguSOg9wLa_OUR9xv-jDVdQ-YnxtadHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک کشتی باری در فاصله ۲۰ مایل دریایی شمال شرقی «الخصب» عمان، از طریق کانال ۱۶ VHF پیام اضطراری مخابره کرده و مدعی شده است که مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69503" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69502">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های حکومت از حمله به یک پایگاه آمریکایی در شمال کویت خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69502" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69501">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=qBtlVdlC5kj03SXFx64txc8LaL_cqhi_jtDOAgA-Vbsow_YwxvduerUsqcRPnJjVzfgBT5UceEFtytZ81-FcAl8cg9J74a7nDh2-11krKdUWl4BmL2A6JGKR_SJbVbQx27GsCXaklM1UZ_Eqbd-GKVY4IyU-vepF0xIgaBBB8S8IL74b5W2V4j8PaOE6OjFbgifE7FmXOptn1h99iB4oMrS2A_V80aBADEmFO5c46ZK3o1s3io2_OyIJI5eYWBIVXnSZiBPIne3DTlV0hYUh_8wAoY12DMk6pRwD56QDS0B-M4Wjgb05S0_3WR4mULb2BCNKdep8xNfg3mC7eL7v6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=qBtlVdlC5kj03SXFx64txc8LaL_cqhi_jtDOAgA-Vbsow_YwxvduerUsqcRPnJjVzfgBT5UceEFtytZ81-FcAl8cg9J74a7nDh2-11krKdUWl4BmL2A6JGKR_SJbVbQx27GsCXaklM1UZ_Eqbd-GKVY4IyU-vepF0xIgaBBB8S8IL74b5W2V4j8PaOE6OjFbgifE7FmXOptn1h99iB4oMrS2A_V80aBADEmFO5c46ZK3o1s3io2_OyIJI5eYWBIVXnSZiBPIne3DTlV0hYUh_8wAoY12DMk6pRwD56QDS0B-M4Wjgb05S0_3WR4mULb2BCNKdep8xNfg3mC7eL7v6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69501" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69500">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
منابع عربی:
شنیده شدن صدای انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69500" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69496">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGMUZPm9MoxOydpqPwhFDZUFEw_yVuTh32lmdYGYGp7nK_moejBCppIO-2-v0c9le9MfOV_j9AM7YarZ7DbBKSImxa7rP6cbpAtuWYZIZMG--HpZsq_VnY4Q8FhrUZZMKv1d73Pb6_arCzF3sFEgt3hDzYv2q90vBVeQXHfJvnw5bow1yVOuXH6qA9mIpjXBO8XOc9jWDN0wMAa8rJZc1fbK65XpWidpkNFBMLgR9eiOmSfFDAq1kmuRvZq4bnqCLH1M6lXCcpZGRz26gCf9CB-kGSCslIi99eN0gGfmiIdFyJOAYARsXUrXB7vGLNEulM5ehPD_Sw4chOYHVDhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=CrHwstK6TQDYLMQ-dXEQ1FSmdvcxNAIXoYvO8sBaemg7rpunttYozR_fjPEWMmIoo-qYst0cvwQNogYTJi3K-NibXWQ0iS-rB8j7fCBLuK9ofaV-8RfYK--MnvJrpva81DPi9V8au4fusX85zjohI3MrMz0Ct8ar8Vjtm5V-SmZ7nX9fxE0S-srPS4NALbLPA0rf7JJwjYCpNNecqnsdy2Y-FKUfQG-qRgyGxm_GZ9AyiNNSzj_Tz3Tm0xlw1-cr4jCfyuaFSPDhIZPyp-0bEndc2IdBdsO3jivDYBSNJvfNd2l9LoJRZS7fBjja0yfj1C7OoB5cTlRFRr0BDi3qxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=CrHwstK6TQDYLMQ-dXEQ1FSmdvcxNAIXoYvO8sBaemg7rpunttYozR_fjPEWMmIoo-qYst0cvwQNogYTJi3K-NibXWQ0iS-rB8j7fCBLuK9ofaV-8RfYK--MnvJrpva81DPi9V8au4fusX85zjohI3MrMz0Ct8ar8Vjtm5V-SmZ7nX9fxE0S-srPS4NALbLPA0rf7JJwjYCpNNecqnsdy2Y-FKUfQG-qRgyGxm_GZ9AyiNNSzj_Tz3Tm0xlw1-cr4jCfyuaFSPDhIZPyp-0bEndc2IdBdsO3jivDYBSNJvfNd2l9LoJRZS7fBjja0yfj1C7OoB5cTlRFRr0BDi3qxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقای سیاه‌پوستی که تو تصویر می‌بینید، رکورد ویوهای تیک‌تاک رو جابه‌جا کرده
👀
حالا کارش چیه؟ میره به شهرها و کشورهای مختلف و دخترها، زن‌ها و دوست‌دخترهای مردم رو بلند می‌کنه و باهاشون مثل دمبل وزنه می‌زنه!
جالب‌تر اینکه تو بعضی جاها، دخترا حتی صف می‌کشن تا نوبتشون بشه که ایشون بلندشون کنه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69496" target="_blank">📅 01:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69495">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b93335655.mp4?token=hKIOiNEQRuOysG0m9ooh8PMXj_X-dI3CdNFMzZeY0pXO-6vjKAHuCt379hZn5romoF17on5vTbnFKtF-W_-u94WDwWO1ctF9Nn-davspVQr2jVAd4YFAdukGoIIjSi0fC-_hbfDoIKC7uXc2LmIpgxucKfd15TJxCmkM4liIKjvYbpnetuRDel18c5EKD0JK0j_J-nOjdt2iEtwo45io95qJZ2GvtvbVwKIFLfZQ8gmIvPmRX76_TE_OG7E8DCPO1v25VuKiVXTU10zJ3JFhwi31KIN_OeJvBR_HVxFiVDYMi2EKOxB531FymkEdEJKp_-pu14_mFjGurvX-KQzlNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b93335655.mp4?token=hKIOiNEQRuOysG0m9ooh8PMXj_X-dI3CdNFMzZeY0pXO-6vjKAHuCt379hZn5romoF17on5vTbnFKtF-W_-u94WDwWO1ctF9Nn-davspVQr2jVAd4YFAdukGoIIjSi0fC-_hbfDoIKC7uXc2LmIpgxucKfd15TJxCmkM4liIKjvYbpnetuRDel18c5EKD0JK0j_J-nOjdt2iEtwo45io95qJZ2GvtvbVwKIFLfZQ8gmIvPmRX76_TE_OG7E8DCPO1v25VuKiVXTU10zJ3JFhwi31KIN_OeJvBR_HVxFiVDYMi2EKOxB531FymkEdEJKp_-pu14_mFjGurvX-KQzlNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دست فرمون پشم ریزون اوپراتور اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69495" target="_blank">📅 00:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69494">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcWpV7EnIm7D5Rg-IRvRrH5PmK3cMThkh2YaExsYVLztuc7uMf5yjCyvkVaksXSRe73pe0vFsuQu7E5HBNWnKGrOCY1wz13WGSxwBsEo8yDfpXD8QemdYUnyfv6kVbORbUDXrn4u0oQxQcTWYGUme6y5epXDJGbuePpcniV8nr2Rnw7kTAdejy8AgBKXMkg7xyozz4Vg2H7JR4GHuJYTljCNmE-vPqaVVMgqYOVV-Qw03n3UkN-5sWIjYiyPyL4vbDpsX-67FRvEh7lGm9nwPDza5NCDlhuX4BrMedSwQO3b2ctygwALy2GJt2PgEwJnhlzw057pJOQvOu5khltizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
ایران هیچ‌گونه قصدی برای مذاکره با رژیم ترامپ ندارد. هرگونه اقدام تجاوزکارانه با پاسخی کوبنده و قاطع از سوی جمهوری اسلامی مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69494" target="_blank">📅 00:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69493">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=R4WzYM2CaEEPft4bHoztKMUZrLtuRFSzjybykS5J1Rc0Qy74pRH9KGQrwC6mUF2lbCLHkiCbFRdEIw3kP8iE9QHXLzHYgUDiecChVQHKO5EubHAQV-gZkPSryr8-9zKIQ608N_QE9ttpT1R1ugIzuFNojnezTd2MteqJNCEyuZIxCGR6FrAiFrcw0QJ6ic5OznZutU917tyxg93d78qO-PE5ntAuokdXFgg1qH2uFaUM2n7CLWOAgyoST2PohPJ3b53zIBlKlaWUbxKSJu7w08y0jwAsTfrYorZSw91T_--Sy7l9uIYzzqLw9jD8vFhhcuZzdAxd44wDemdC2jMWew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=R4WzYM2CaEEPft4bHoztKMUZrLtuRFSzjybykS5J1Rc0Qy74pRH9KGQrwC6mUF2lbCLHkiCbFRdEIw3kP8iE9QHXLzHYgUDiecChVQHKO5EubHAQV-gZkPSryr8-9zKIQ608N_QE9ttpT1R1ugIzuFNojnezTd2MteqJNCEyuZIxCGR6FrAiFrcw0QJ6ic5OznZutU917tyxg93d78qO-PE5ntAuokdXFgg1qH2uFaUM2n7CLWOAgyoST2PohPJ3b53zIBlKlaWUbxKSJu7w08y0jwAsTfrYorZSw91T_--Sy7l9uIYzzqLw9jD8vFhhcuZzdAxd44wDemdC2jMWew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
آماده بودیم به ۳ نقطه از اوکراین حمله بکنیم ولی عذر خواهی کردن کنسل شد
پل های منتهی به هرمزگان رو آمریکا میزد که حمله زمینی بکنه ولی خب طرح هاشون ناپخته بود
تو ۱۷ روز با حملات شدید موشکی پهپادی ترامپ رو مجبور به شکست کردیم
آتش بسی وجود نداره داریم حملات معقولی انجام میدیم
تفاهم‌نامه با موافقت رهبری امضا شد
کویت رو ویران کردیم و فرماندهی سنتکام از قطر به اسرائیل منتقل شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69493" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69492">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571743cf02.mp4?token=JCBpmKcdk-wHbwQuQY6HPnYj7HDUmPPgG4H_oX9MO2mxPuK1gNTS864qAkqNWjXNtd8vViK1Vug046Xwu97O-ASYaCYRK6ROtTEc4-_gdSk-8JQJcykixTlVulf6oVctGhEoN1Fu0O9hN95HpevNPsMThXuaSF080uy_6qkg0ZNMiHgk-GW7E29Xq0VaG3OMI9qmABfB7quGvFJM_uGx0FFqXSbsvg8_Tu9AIA7DXP19-rsYiLM_9qcwcQ29NBR_mIrcMcaq7W-8tAbShBWTx-WWNbT3lccpnl7dBhkZ3I8FUJCyYCejI7Hzt3yo5DgNXWU6QA2Wx36qrbcgwCcvMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571743cf02.mp4?token=JCBpmKcdk-wHbwQuQY6HPnYj7HDUmPPgG4H_oX9MO2mxPuK1gNTS864qAkqNWjXNtd8vViK1Vug046Xwu97O-ASYaCYRK6ROtTEc4-_gdSk-8JQJcykixTlVulf6oVctGhEoN1Fu0O9hN95HpevNPsMThXuaSF080uy_6qkg0ZNMiHgk-GW7E29Xq0VaG3OMI9qmABfB7quGvFJM_uGx0FFqXSbsvg8_Tu9AIA7DXP19-rsYiLM_9qcwcQ29NBR_mIrcMcaq7W-8tAbShBWTx-WWNbT3lccpnl7dBhkZ3I8FUJCyYCejI7Hzt3yo5DgNXWU6QA2Wx36qrbcgwCcvMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی وایرال شده از موکب خدمه ام‌البنین که به زائرا آیفون ۱۷ و آیپد و گوشواره طلا میدن!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69492" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69491">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTWcFfRhi3dO6Szn73-2rhq2VJyEQLteYRO71ogcsU6wW5MNduTMKKmqYnwLAkVGeoVIb_Z3s9OoEcp1TokSbFuXSdShbUTG3jtLauVbkUoup_Z6YZq-9sh6LzRkmjy84hl-ipFqBb8LSEKuZUT9sQeBRzwYsUAu9vnuhCF6zcPlfOk8TM9-7kiJzdOUUe2wC8KO9HRSTdU9TemiQq4TIiwlM_igEpiBQFcBJw6BaTTz_9UtZ5JYdM8VFiN1YfIBzXx9GfHJKMQAntHdyMQZln-aoMK7FI9DTD1YBzSlWVlPyHpqPD91BbUaET6WRRW-5zwcEiWh5GWxABOuGTWEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69491" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69488">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7ddVY7ZJdLy8RcgZlFpRtWDrmAd7cnsQdQqL0YNkaI1mkOI1B6FOYls0gluCL4prOWooWO6rQxeo6doeEMetYqKRY3N58JWxvnCjZeOlBzoTKfjo9QlfniyYS2yQcDQ8PYnCdzMpthmDLSRmJBstPS4lEFgUI7sMA3xngSZFgxm80ajRtXtc1MIFjQiD8EKpay01KW873lVdSVXlETE09S2nKBu_vG8oYjYyXYVhv-ilkqC-3JmrukMPQ3xPYSljMZoAOxrM6gMzbx95Vbra98yKQmGQh77Ifxkdhl8Jku1pcVqwbWQZ7VeSDGNYjGr7MQcOD_ayDZi-2ZwQ5xcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyNIA0BfKZJVCHdaTPfESDXW3JQHco-xSE31c208dfpDFH-mpusZB1WwrabQH7fF3toJDN5CAONWjgrNcfPKlmvhttqaUI6-iKXJlPJlV26Lk4OWIvp6zyUbeC7RPAPILIMgWmxOx6e5r77gYwHIktvzzsXa1QEXnBdQ3NNdaQ9cAQyyHQZypfE_FZBDgqtEHNCtJGWCX8QrqSfX1GWayhbriUb7bzBwqHd4ec-FGaazSyFFaRlfcAfAENqTrF2gmDFy95ft7latYBdsPj86vFi86DFkefUqmwVzqUI7X_8OlUS-RuiJ48EBe9GD0K8_nWD1VXHL_m2iSNZLUWKnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4O2mw44KvKrr9y3FKZhD0YzN8dogNJhMAZNpp7IjFB3bUpgkzrs6da3PWvnlhr62Adwk4Uq_k79y6lYjF0lDXrsWJbKQxCeSLloSIO5xv8pyRJyJa5SNFN1IOFL-HtvaJ9eNJK14xVc_oEuKLuE2S5wZ-mGjXThqsVqYKxOSneATMndqHgk6hvPm12rmhmq9KhQ4JAwZOEuN1GNh0I_KBRi_Yo9X5yPcLDJXKwMDr61jcHmBPFvk26pFfRt9nJ6o4cmelG7XuzHLCMo4h1ysCvVVn2SX7Rwd8MFjxXNAO5WnttG_0LPpmM3BhGnbbiBHkSo6uhd6pli2mUiqW5fpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کامنت های دردناک مردم زیر قیمت PS5 تو سایت دیجی‌کالا
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69488" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69487">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=GSd805bgNBHLfF_hQJKUV4HsQvEblMVGfR0QdJPPwIhL65thahAJLphFOyJtRDlE-neLyKWHUg-AZkeE00dSIpyxwQwD3f59znWVyefQeq4oYFyj3zyh5es3cO7yH-fM3kE2buSQSCJnfMGTqV29FA9JRUOhmLSkdCzBkrAJrWRZgAEcERHTt1optv0jmyG2NhuP1zXBTq7qMvnCfba4uflFAehFK0DT8VDXOp81vuTzaQ6VPn9Q02JDNsDEyL-p8X9VgpYvx9YTIRvcfsvMontZYG5Njp_SXotxl6APEmH07K2b5GVMRPngH7GWIybhtTm1OzsVbvoj7qsqP_QuWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=GSd805bgNBHLfF_hQJKUV4HsQvEblMVGfR0QdJPPwIhL65thahAJLphFOyJtRDlE-neLyKWHUg-AZkeE00dSIpyxwQwD3f59znWVyefQeq4oYFyj3zyh5es3cO7yH-fM3kE2buSQSCJnfMGTqV29FA9JRUOhmLSkdCzBkrAJrWRZgAEcERHTt1optv0jmyG2NhuP1zXBTq7qMvnCfba4uflFAehFK0DT8VDXOp81vuTzaQ6VPn9Q02JDNsDEyL-p8X9VgpYvx9YTIRvcfsvMontZYG5Njp_SXotxl6APEmH07K2b5GVMRPngH7GWIybhtTm1OzsVbvoj7qsqP_QuWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
✈️
یک جنگنده F-16 نیروی هوایی اوکراین، یک پهپاد انتحاری روسی (Geran-2) را با شلیک توپ ۲۰ میلی‌متری ولکان (M61 Vulcan) در آسمان اوکراین سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69487" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69486">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22887d7155.mp4?token=AEdBhmCQPPs11k6nmyI6Amryl2l3BH8ACBrtW56t0IkI8_02hsG6LAfOfzFSAR6z8eRdetqxmV3b2Rcb2EVaKEy_yWjE6oZkBhgP3S11sJasglX4B9HEsbcyLC-4uvfkEwbOErHdi9bu055RCXtsGmf0vJl8ax0crmbTHdRu0rez52IVNhWs0_YjIatQKTHJtnncV8qQwjDdXVPWuvNee0Eypk5vliYpHqV-LBCqbx01JqYNRDoK9klChtve6VfUA5pwkkOC2yPM6Vb6m-4Ph1dkGQz7ApupowHJB2UR3fTz8Ljv7eD3Lb_99NovIH_Kdsdxg3HpNYzzIcm7wSVdfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22887d7155.mp4?token=AEdBhmCQPPs11k6nmyI6Amryl2l3BH8ACBrtW56t0IkI8_02hsG6LAfOfzFSAR6z8eRdetqxmV3b2Rcb2EVaKEy_yWjE6oZkBhgP3S11sJasglX4B9HEsbcyLC-4uvfkEwbOErHdi9bu055RCXtsGmf0vJl8ax0crmbTHdRu0rez52IVNhWs0_YjIatQKTHJtnncV8qQwjDdXVPWuvNee0Eypk5vliYpHqV-LBCqbx01JqYNRDoK9klChtve6VfUA5pwkkOC2yPM6Vb6m-4Ph1dkGQz7ApupowHJB2UR3fTz8Ljv7eD3Lb_99NovIH_Kdsdxg3HpNYzzIcm7wSVdfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که میبینید ۱۲۶ سالشه و اهل کشور برزیلِ؛ در زمان پایان جنگ جهانی دوم تقریبا میانسال بود
این بدبخت نمرد تا جنگ جهانی سوم رو هم ببینه و دبل کنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69486" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69485">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها با من تماس گرفتند و گفتند: «لطفاً حمله نکنید. ما توافق خواهیم کرد.»
این حقیقت محض است و همه آن را می‌دانند. چه کسی تماس نمی‌گرفت؟
کسانی که اطلاعات را به بیرون درز دادند کمک کردند، چون شدت حمله را فاش کردند و ایران هم از آن آگاه شد.
آن‌ها می‌دانستند چه چیزی در راه است.
قرار بود دیشب [حمله] انجام شود و مدت زیادی هم ادامه یابد، و [در نهایت] چیزی باقی نمی‌ماند.
اگر فرصتی داشته باشم که به افراد زیادی اجازه زنده ماندن بدهم، می‌خواهم آن فرصت را فراهم کنم.
بنابراین، هیچ محدودیت زمانی‌ای ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69485" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69484">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20068f370b.mp4?token=MeHfw_ev7yBgzEg1YZyoyOTxm7pyh-YTw-dllG1AvqJ2xwjnw7cYt_kZD5GNoQ5_FszaKvw1uChTKISw1TBEHwUZ5IKRPVNihoE7wUjUJL93kWvclJ6UYglRRQszYgBdqaxP07d7fP2Vr1T5WbvwuXw0dLoqmwryjP2kMYNlCJQeuqvpec24fGAgM69vc7ghFPN8Hp80_56QmnG3uVLkV9Seq9BGeBr-tG5YbUZodl4memL1iZ9vMfzIWUobZ77INAJV-7Q7Maw03ZlxBZOflP_nefySzVOKWfEvrUXfjkSxn0keemT68F7CanXt8EhNHaeEvS3HXrwxysGkIU8FyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20068f370b.mp4?token=MeHfw_ev7yBgzEg1YZyoyOTxm7pyh-YTw-dllG1AvqJ2xwjnw7cYt_kZD5GNoQ5_FszaKvw1uChTKISw1TBEHwUZ5IKRPVNihoE7wUjUJL93kWvclJ6UYglRRQszYgBdqaxP07d7fP2Vr1T5WbvwuXw0dLoqmwryjP2kMYNlCJQeuqvpec24fGAgM69vc7ghFPN8Hp80_56QmnG3uVLkV9Seq9BGeBr-tG5YbUZodl4memL1iZ9vMfzIWUobZ77INAJV-7Q7Maw03ZlxBZOflP_nefySzVOKWfEvrUXfjkSxn0keemT68F7CanXt8EhNHaeEvS3HXrwxysGkIU8FyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در مورد ایران:
می‌خواهم قبل از نابودی کامل، آخرین فرصت را به ایران بدهم.
امیدوارم سر عقل بیایند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69484" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69483">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=bDmT9Fl4O9yO0y4WG0O2k9b-cjPBJ4voMCQgVoZbUEX0Pfmkd4oVwZBiIYilEXgb5_kPe9jFsu5RzgeXAO4aD-shDd0jBJsridT4c7_DAPGqMqf6g0oFLpNM6lf1NsgkYhcKjWj5PAOfpCcYsJuG-5g-fv-J9mg9pRQXacBFH5MCLblqGkv-08AAUlLN8SZYhdp3VWTEAdGZZmSkuwtw5gU19v8sRpz2mNfHcsA6U2kTSrPlxeCaQbXnU2e-STfhkWlxm98t0hnoxjQiBXExj77PJ1IRN4-nSBYv-R3UOBLWUstFYXlHtVusm2sPalSRfya1C4Fb-lsv0Hz5z_nB_6DcMikDxm9hOMoobyakTeebqgnqzB6oktEJ0abEVUt2-jKuLKWTVJzvewhCp6_vQE9BYt8SsBm4IJPVhQZSaLtVUre8o84mTnhSijdko4rH6gI0OG_qd9Lkl1LnQvbbQSzhzXYrUzXLcG8Vgt_qOunX8sCq4MQlETM3HOe0CUOIqohEGLaAv2bYDhmfshr3qmoBgWyFzBNc3Fc4d3U7o1ON4FUlQk1L8uxl1MUm4U3GWEvSRmVo8vGzJEDEO-OWIoSDJPSg-rk3Aj4OaKH_7uMTE1tF-DyH0l7JiCM7cJ0KZyvHZH0rmwFEdlBIZe0NtC8R3_TLPGCDKAVVMiBa2D0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=bDmT9Fl4O9yO0y4WG0O2k9b-cjPBJ4voMCQgVoZbUEX0Pfmkd4oVwZBiIYilEXgb5_kPe9jFsu5RzgeXAO4aD-shDd0jBJsridT4c7_DAPGqMqf6g0oFLpNM6lf1NsgkYhcKjWj5PAOfpCcYsJuG-5g-fv-J9mg9pRQXacBFH5MCLblqGkv-08AAUlLN8SZYhdp3VWTEAdGZZmSkuwtw5gU19v8sRpz2mNfHcsA6U2kTSrPlxeCaQbXnU2e-STfhkWlxm98t0hnoxjQiBXExj77PJ1IRN4-nSBYv-R3UOBLWUstFYXlHtVusm2sPalSRfya1C4Fb-lsv0Hz5z_nB_6DcMikDxm9hOMoobyakTeebqgnqzB6oktEJ0abEVUt2-jKuLKWTVJzvewhCp6_vQE9BYt8SsBm4IJPVhQZSaLtVUre8o84mTnhSijdko4rH6gI0OG_qd9Lkl1LnQvbbQSzhzXYrUzXLcG8Vgt_qOunX8sCq4MQlETM3HOe0CUOIqohEGLaAv2bYDhmfshr3qmoBgWyFzBNc3Fc4d3U7o1ON4FUlQk1L8uxl1MUm4U3GWEvSRmVo8vGzJEDEO-OWIoSDJPSg-rk3Aj4OaKH_7uMTE1tF-DyH0l7JiCM7cJ0KZyvHZH0rmwFEdlBIZe0NtC8R3_TLPGCDKAVVMiBa2D0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران حاضر است به وضعیت آزادی کامل کشتیرانی در تنگه هرمز بازگردد؟
🇺🇸
ترامپ:
اجازه نمی‌دهم آن‌ها [بابت عبور] هزینه دریافت کنند. اگر قرار باشد کسی هزینه‌ای دریافت کند، ما خواهیم بود. ما کنترل کامل را در اختیار داریم.
ما سازوکاری در نیروی دریایی داریم که نوعی محاصره محسوب می‌شود؛ آن‌ها به آن «دیوار فولادی ایالات متحده» می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69483" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69482">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=a9ME5bHeOpxDxjld53pqv9Ow4c3pMXw4N-OJRyzYPsU9wAtLo0-MZme3CKpju6NKNq4YLVMuR-LKLxOQ2AZWYOwbLEBpB3gYg3YT-HMUoVv6ejr9NYbsUanf77_256scIa65XcnHxoVuvKx33u64FL85clNrImIAiZeXTfv-6i3oPYZEsg6VY4nw5Too9ZGmU1Q5rv16Uy8C-S50UA67WpX2KVmguWDl-0QCCHhT9XvGoNbigyTQmNA074f9c3bQPv60rECM9n4fmKaTscXubIr3fDXnsBwULVW0afMUrnLokECQHo1lFUUs0UQPC5yMtbE3kKuLSh3nzAuJY8sdPw6BQAUq5fB04ifNp8udq68gwZAtTST-VplzGHtyg1eINzbr85v6QjgT7ipJk4qPnmFblsgnQ4F2KLqX4mhJ0TqkbNB8yvNcupTezFBam7AT6gFKIGQ3q8CctXorwmQChxMf_8iaXlaw5bwTuBHLAIH-YK1wbW_SvX63lLCFHo-EJ0j8gxGmtc2UFkJvg4WIqJn1LOvv5-NFNknvm-uGKO8fGvYVX1hi4vAjgb2xFGXeuHHZi6Wgz4LiD1ymeeK84oObE9mp_Psgppap9NQmvJTS3flvJUrj0IXL_9FANmlilbr42SmpMBQBs0FlRqBPhYphpN6-DjwH8EYkioFFnQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=a9ME5bHeOpxDxjld53pqv9Ow4c3pMXw4N-OJRyzYPsU9wAtLo0-MZme3CKpju6NKNq4YLVMuR-LKLxOQ2AZWYOwbLEBpB3gYg3YT-HMUoVv6ejr9NYbsUanf77_256scIa65XcnHxoVuvKx33u64FL85clNrImIAiZeXTfv-6i3oPYZEsg6VY4nw5Too9ZGmU1Q5rv16Uy8C-S50UA67WpX2KVmguWDl-0QCCHhT9XvGoNbigyTQmNA074f9c3bQPv60rECM9n4fmKaTscXubIr3fDXnsBwULVW0afMUrnLokECQHo1lFUUs0UQPC5yMtbE3kKuLSh3nzAuJY8sdPw6BQAUq5fB04ifNp8udq68gwZAtTST-VplzGHtyg1eINzbr85v6QjgT7ipJk4qPnmFblsgnQ4F2KLqX4mhJ0TqkbNB8yvNcupTezFBam7AT6gFKIGQ3q8CctXorwmQChxMf_8iaXlaw5bwTuBHLAIH-YK1wbW_SvX63lLCFHo-EJ0j8gxGmtc2UFkJvg4WIqJn1LOvv5-NFNknvm-uGKO8fGvYVX1hi4vAjgb2xFGXeuHHZi6Wgz4LiD1ymeeK84oObE9mp_Psgppap9NQmvJTS3flvJUrj0IXL_9FANmlilbr42SmpMBQBs0FlRqBPhYphpN6-DjwH8EYkioFFnQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره مذاکرات با ایران:
امروز یا فردا متوجه خواهید شد که وضعیت مذاکرات در چه مرحله‌ای است.
مذاکرات به هر طریقی که باشد، به‌سرعت پیش خواهد رفت؛ موضوع پیچیده‌ای نیست.
ما درباره بازگشایی تنگه [هرمز] در روز آینده صحبت می‌کنیم؛ بازگشایی کامل آن.
سپس درباره توانمندی هسته‌ای ایران گفتگو خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69482" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69481">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=WAMBRY56Wq7uPsSbSu_GBsJ_-OpCKf1oYGOKIEBJz2edK-HaGN0T4429dHaQFCrsee2uyrKREBMKegOV7ZPSo4gbIQVJl44JpHKdVgw7aZlFGx1r7Yf7tHrxazmHeM_ArgEQQNfn5YlWDMfzwHtg_bSG3lagw22oeE8V9slxR72SusTrEPOAwMKiVfPIp6YZr2itHlqCk8IUm0toK4Rh5W5k20rJ-09j2sNFo9xmoLXwDnA6tmFCLhtFs8yNy17oUTlpvqttXH2vGKhPHo86bKLmHtU2KjwXmh0JbMwL04kZsZDxZG2r-_xJV6mrL1eLcY0xCVzMewDs3pKV5ZIG9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=WAMBRY56Wq7uPsSbSu_GBsJ_-OpCKf1oYGOKIEBJz2edK-HaGN0T4429dHaQFCrsee2uyrKREBMKegOV7ZPSo4gbIQVJl44JpHKdVgw7aZlFGx1r7Yf7tHrxazmHeM_ArgEQQNfn5YlWDMfzwHtg_bSG3lagw22oeE8V9slxR72SusTrEPOAwMKiVfPIp6YZr2itHlqCk8IUm0toK4Rh5W5k20rJ-09j2sNFo9xmoLXwDnA6tmFCLhtFs8yNy17oUTlpvqttXH2vGKhPHo86bKLmHtU2KjwXmh0JbMwL04kZsZDxZG2r-_xJV6mrL1eLcY0xCVzMewDs3pKV5ZIG9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک سند خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69481" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69480">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=TqWJ2Hupsg_bbpPqdzupnWAIy_tnduV0w7A-_OuiqZSDWojx-ozSSpVCfu3PbRexxvLOARmsX8I1WKxMcxjfbptZat4MjA8gpmib8_v9j93gCwCQT-ssdtCWLsvXNclc0Jd8Ku1gAALPao9T6KDou1UFtf6tr_s8FpDBCYKdVbHQLPEzqqPsDlAXokzdiqbKMZlglj8MyhKZGcteMjfWoAMP5e7nJoiQPY2CFmSOQMn77qH29xWJBdVHOg5X52RgUAJ2ood5g_dHkBI1I4GkZ6giIg3G1PeN6-N8LmJpElB5UVTGj4Z9J6w_dp8imG0etaRYAbsCgIxlTkdkq3Zx3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=TqWJ2Hupsg_bbpPqdzupnWAIy_tnduV0w7A-_OuiqZSDWojx-ozSSpVCfu3PbRexxvLOARmsX8I1WKxMcxjfbptZat4MjA8gpmib8_v9j93gCwCQT-ssdtCWLsvXNclc0Jd8Ku1gAALPao9T6KDou1UFtf6tr_s8FpDBCYKdVbHQLPEzqqPsDlAXokzdiqbKMZlglj8MyhKZGcteMjfWoAMP5e7nJoiQPY2CFmSOQMn77qH29xWJBdVHOg5X52RgUAJ2ood5g_dHkBI1I4GkZ6giIg3G1PeN6-N8LmJpElB5UVTGj4Z9J6w_dp8imG0etaRYAbsCgIxlTkdkq3Zx3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
قرار بود دیروز ضربه بسیار سختی به آن‌ها وارد کنیم؛ بسیار بسیار سخت.
سخت‌تر از هر حمله‌ای از زمان جنگ جهانی دوم. این اقدام بسیار بزرگی محسوب می‌شد و ما کاملاً آماده اجرای آن بودیم.
در حال حاضر، به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و بسیاری دیگر، مشغول گفتگو هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69480" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69479">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=EVZSWbDtZvObvCxRdZaNy0Ruvce32GOk2dQ1zEUdqc4EMyRTHlr7PXXDuSyFciURe8Z2UltdnmUGiq6xWOCnyqG7XQTaukozqjiD2XnM4uqCjEgkHyJKLDfKmlr_Bd2xbhW9dnhqa7aMZh8nN8wlWnLcQMFl6HGaaIbGZZw0pOBnr6P7DmOzTLj_HGhLdBkhMDhR79upn8UkLM7iTvs2LF1mNntvP3DWtmo_47s33cp6VQnta7tlowl-dROsNv6P5HPdcKWkdoTtuUawhYNh5NeJEsBDj4Rb8PSeGLyIUWMQBFcWHzx7nER3DAvKO4sCXQqw9-LWikk3cT9T5_TmsbshLHwWWnB8sHIeH9NrBG4jIqU7MbVVq4g12rw27RQDBc8HSoZSfIR4BuO9NpC3JP__fua58orDdiFlKEGQeqwJ5oFoS1YyYL-ylGwUY-Hg85zA8-NGuVWQDku0M7nU0eQ6riD6o_mKqeaJtFaooF2aOFcru5lioep_vs3IgVxzRhWhrSixE45nEoIoDceUX6oXPJBSr2ZBq1-0IbeIRTV6krGcQVK3V6VnITXzY6AdcnjwYINfJtqVyCKcYJyKWng05nffpOqzD6fjFrca6oygUCfSBnbpz3ZM4qhUXZkd6bC0ZQzdo6gX6bsR2AG5RrULunGkK-96y6TChbOSEAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=EVZSWbDtZvObvCxRdZaNy0Ruvce32GOk2dQ1zEUdqc4EMyRTHlr7PXXDuSyFciURe8Z2UltdnmUGiq6xWOCnyqG7XQTaukozqjiD2XnM4uqCjEgkHyJKLDfKmlr_Bd2xbhW9dnhqa7aMZh8nN8wlWnLcQMFl6HGaaIbGZZw0pOBnr6P7DmOzTLj_HGhLdBkhMDhR79upn8UkLM7iTvs2LF1mNntvP3DWtmo_47s33cp6VQnta7tlowl-dROsNv6P5HPdcKWkdoTtuUawhYNh5NeJEsBDj4Rb8PSeGLyIUWMQBFcWHzx7nER3DAvKO4sCXQqw9-LWikk3cT9T5_TmsbshLHwWWnB8sHIeH9NrBG4jIqU7MbVVq4g12rw27RQDBc8HSoZSfIR4BuO9NpC3JP__fua58orDdiFlKEGQeqwJ5oFoS1YyYL-ylGwUY-Hg85zA8-NGuVWQDku0M7nU0eQ6riD6o_mKqeaJtFaooF2aOFcru5lioep_vs3IgVxzRhWhrSixE45nEoIoDceUX6oXPJBSr2ZBq1-0IbeIRTV6krGcQVK3V6VnITXzY6AdcnjwYINfJtqVyCKcYJyKWng05nffpOqzD6fjFrca6oygUCfSBnbpz3ZM4qhUXZkd6bC0ZQzdo6gX6bsR2AG5RrULunGkK-96y6TChbOSEAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: مذاکرات با ایران حالا دیگه متوقف شده.
🇺🇸
املاکی: نه، همین الان هم مذاکرات در جریانه. واقعاً اتفاق عجیبیه.
این بار دیگه اصلِ مذاکره رو انکار نمی‌کنن.
فقط نمی‌دونم چرا، هر وقت دارن مذاکره می‌کنن، دوست ندارن بگن که دارن مذاکره می‌کنن.
با ونزوئلا یه درگیری داشتیم که خیلی خوب جمع شد.
الان هم با ایران درگیر یه پرونده هستیم و اون هم داره خیلی، خیلی خوب پیش میره.
شما هم دارید فوق‌العاده کارتون رو انجام می‌دید.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69479" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69478">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=aityfgBQpLF1b3jJ8c_i7T6xUmtWoEHan1LawRR8Jg7YShDcnDCs1EwdMDwYKvMWe_X99OAxGhnXCbwT8TkQg2Ep2u9mZC7y4YSOgAypImSmS02XYXU_fNHK7d82PVUuap7OuBuzq8gyDiZLvS4_QcJSNnxME2r6tYM66w-0-UiQvrqc-aAFHksZ_bRIQJfOp_HavjIs7D4u7nJ6AkEc5CUuXxVcZ750BkLb-AYzsaG_dZv7r2vIgmPwRBXnhBPA4tg20gVOLuSdPeMi3I5Nke8x5R_Zc8uGzgEqn5nTU0tvsebMq3IHEn8xO3c2TIJU7jo4grjgxiF7rWWsqc-xVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=aityfgBQpLF1b3jJ8c_i7T6xUmtWoEHan1LawRR8Jg7YShDcnDCs1EwdMDwYKvMWe_X99OAxGhnXCbwT8TkQg2Ep2u9mZC7y4YSOgAypImSmS02XYXU_fNHK7d82PVUuap7OuBuzq8gyDiZLvS4_QcJSNnxME2r6tYM66w-0-UiQvrqc-aAFHksZ_bRIQJfOp_HavjIs7D4u7nJ6AkEc5CUuXxVcZ750BkLb-AYzsaG_dZv7r2vIgmPwRBXnhBPA4tg20gVOLuSdPeMi3I5Nke8x5R_Zc8uGzgEqn5nTU0tvsebMq3IHEn8xO3c2TIJU7jo4grjgxiF7rWWsqc-xVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
ما با ونزوئلا اختلافاتی داشتیم که به خوبی حل و فصل شد.
ما با ایران نیز اختلافاتی داریم، و این موضوع نیز به خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69478" target="_blank">📅 21:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69477">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=LOgUNCH7fdz9Vhk_hmZtMRlRPoGAFz5eWZ_zPwhTitbwFB7TZMdIqhupTfkgtMQL0tnJX903pUOvbI4IZoDVFiOtLOzqTg1Vlfwj9hgO55FgwXoM4BrD0pLb_J698Lrn6xEhBbiaUBi7GRAj3UbkSfDT_J8z7oRYtV4mVl6Sn2JYPp88aIeHCGcTcbOfW4n8uyw528bJ9DNL8TVhi43qF_2-fPzX9xCCKb_dZwULQ0idxsf6306y4fh6wrSfx5gaDlDZw260tynCNuzi-U_EJpaOWg61iWQuNtz9XX6nvogDZok8WTNALxI27jcfaajO44n3sv9RswAfA5bCHylPNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=LOgUNCH7fdz9Vhk_hmZtMRlRPoGAFz5eWZ_zPwhTitbwFB7TZMdIqhupTfkgtMQL0tnJX903pUOvbI4IZoDVFiOtLOzqTg1Vlfwj9hgO55FgwXoM4BrD0pLb_J698Lrn6xEhBbiaUBi7GRAj3UbkSfDT_J8z7oRYtV4mVl6Sn2JYPp88aIeHCGcTcbOfW4n8uyw528bJ9DNL8TVhi43qF_2-fPzX9xCCKb_dZwULQ0idxsf6306y4fh6wrSfx5gaDlDZw260tynCNuzi-U_EJpaOWg61iWQuNtz9XX6nvogDZok8WTNALxI27jcfaajO44n3sv9RswAfA5bCHylPNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فرماندهی مرکزی آمریکا (سنتکام) فایل صوتی مکالمه ناو آبی‌خاکی USS Comstock (LSD-45) با یک شناور ناشناس را منتشر کرده است. در این مکالمه که از طریق کانال ۱۶ رادیویی دریایی VHF (فرکانس بین‌المللی تماس و اضطرار) انجام شده، به شناور دستور داده می‌شود مسیر خود را تغییر دهد و هشدار داده می‌شود که در صورت عدم تبعیت، با استفاده از زور وادار به اجرای دستور خواهد شد.
ناو USS Comstock به‌عنوان بخشی از گروه آماده آبی‌خاکی USS Boxer (ARG) و همراه با یگان یازدهم اعزامی تفنگداران دریایی آمریکا (11th MEU) در منطقه مسئولیت سنتکام مستقر است و توانمندی اجرای عملیات آبی‌خاکی و واکنش سریع به بحران‌ها را در اختیار نیروهای آمریکایی قرار می‌دهد.
بر اساس آخرین اعلام سنتکام، نیروهای آمریکایی تاکنون ۴۴ کشتی تجاری را که به‌صورت داوطلبانه از دستورات محاصره تبعیت کرده‌اند، به مسیر تعیین‌شده هدایت کرده‌اند، دو شناور را برای اطمینان از رعایت دستورات بازرسی کرده‌اند و دو شناور متخلف را که با وجود هشدارهای مکرر از اجرای دستورات خودداری کردند، از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69477" target="_blank">📅 21:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69476">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY8xqDAgM83y13MTenpogO6pHkBg7hNKUQhXImtIlmQ0YcWmZdTuXTkrAPx_jQPpeLK-sbHkQRm4S5s9sGsTeGfWVJNQCHFMZSiGMR21zbuwLGvglOrXCS7bgeNV-xPvVTgZ0tOyLY_646HFx9O6fyS8GVAXPug2ILk2DvNhwABNUUvq87TJaniU-U-XiD6guOW10GK9biWE5aPD6MOCyt-j2P8E8-7PPjTRqyhjhwyD1Rs16uT_VuaRt6rQr_Vs8NOBhrtkeUQJcRPxAUN-8yVlZerYs2ezVZXruZx7iTKssdVa5i6NIREhF0Ex-WaanShAuV3q03AuHiNf9hNE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مارک لوین:
من از اسرائیل حمایت می‌کنم.
من از اوکراین حمایت می‌کنم.
من از تایوان حمایت می‌کنم.
من از مردم ایران حمایت می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69476" target="_blank">📅 20:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69475">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6Vxj4r8dfAY3WieL-g5N0DCI45H0b3tytaIuUHDmvtAE0weA6Egh1O_slZcInj-F-emUTrskqX1bjJhlb9pIjwe_QvvC-XZfxNm7xL_RQfRHwAr78GptAuYJifXxA44GZijLCS_6hCaDjGxGIyUkQbVLd6rybDZ7pJcpvx-Rpk7hwDMcEfkgINE3wDvg-aRMTla-1QgnUpKWEeqLBcht6pq5AmAbXYNj6_sg5MPXRZfOvWQEeKGz-2Epq_GIOxSgdVC2IYRBd2kcvRqm_EWY6BNd4BXIOatDC7GV9qK_EWV6MTNGY2FkoBfE0bZeg9sVki9b-f32JG_IRswqqugAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ : رهبری ایران واقعاً یه جورایی دو‌رو و ریاکاره که باورنکردنیه؛
خودشون می‌خوان مذاکره کنن، بعضی‌ها حتی میگن التماس می‌کنن، مذاکرات شروع می‌شه، جلسه بعدی هم قراره به‌زودی باشه، بعد علناً و با افتخار میگن که هیچ مذاکره‌ای در کار نیست، هیچ صحبتی نمیشه و فقط با «عمان» کار دارن!
بعدش هم همون چرت‌وپرت همیشگی‌شون رو تحویل می‌دن که می‌گن تنگه هرمز رو با قدرت خودمون اداره می‌کنیم، در حالی که از قبل کاملاً تحت کنترل نیروی دریایی آمریکاست و همون «محاصره» یا همون‌طور که بعضی‌ها می‌گن «دیوار فولادی ایالات متحده»!
هیچی به ایران نمی‌رسه مگر اینکه ما بخوایم، و هیچی هم نخواهد رسید مگر اینکه یه توافقی بشه یا اینکه کامل تسلیم بشن.
فرقی نمی‌کنه ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم درباره‌ی راه‌حل مشکلی حرف می‌زنیم که خودشون دهه‌هاست ایجاد کردن، خیلی ساده‌ست:
ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69475" target="_blank">📅 20:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69472">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4129d878df.mp4?token=awW9lNF48Y_leYmcoZR6RKeO9fuKgH40_EQUK7DQH9LqB0QsjVXoWYX2s8tQkIPMEb2ZlYkfaFALlMh_Cff9QmQK4xrVJ7wmn6rrEEWuhXjWyayjf3g4RsH7dcomejY3VxeEBg_NV1-yo-GSL84ZvCigVBFlwLBfd7T5e5QEuUpzzNs9fjC1_6n-26cmDNGkBfwVfnamoGC7kcpHOl-I8kE8H8f6-A-pAPihtByVyTImKp2agVXUGo7_jz2uKRuKeBVB-K1FSC5o2tWQEMDbX_6MitQJkaFYdlxkc996Ga3Fd_4jaeyce5dCsXUxWyMtKHOMkIjIXqVB2yDtzv_jdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4129d878df.mp4?token=awW9lNF48Y_leYmcoZR6RKeO9fuKgH40_EQUK7DQH9LqB0QsjVXoWYX2s8tQkIPMEb2ZlYkfaFALlMh_Cff9QmQK4xrVJ7wmn6rrEEWuhXjWyayjf3g4RsH7dcomejY3VxeEBg_NV1-yo-GSL84ZvCigVBFlwLBfd7T5e5QEuUpzzNs9fjC1_6n-26cmDNGkBfwVfnamoGC7kcpHOl-I8kE8H8f6-A-pAPihtByVyTImKp2agVXUGo7_jz2uKRuKeBVB-K1FSC5o2tWQEMDbX_6MitQJkaFYdlxkc996Ga3Fd_4jaeyce5dCsXUxWyMtKHOMkIjIXqVB2yDtzv_jdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
درگیری عرزشی ها و پلیس عراق در کربلا:
توی عراق یه روحانی به اسم صادق شیرازی، مخالف جمهوری اسلامی و خامنه‌ای هست، اون معتقده که فقط باید گفت لبیک یاحسین، نه لبیک یا خامنه‌ای.
حالا عرزشی‌ها دیشب افسار پاره کردن و هجوم بردن سمت موکب این روحانی و شعار مرگ بر آمریکا و لبیک یا خامنه‌ای سر میدادن.
عرزشی‌ها شروع کردن به کتک زدن مردم عراق تا اینکه پلیس وارد شد و با شوکر و باتوم عرزشی‌هارو کتک میزد.
طی این درگیری بیش از ۱۰۰ نفر به بیمارستان منتقل شدن و عراقی‌ها میگن دیگه نباید ایرانی‌هارو راه بدیم، غذای مفت میخورن و مارو کتک میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69472" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69471">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=Hwerb-xA10lfdcsh5ZKMD39Y5IjvUndf1txkYnS4J_PCElPWD6P3g2mBf_vX9uK4sw2-lJKr5et06PcqCvCWQYgXJANxkorhWLJaMFH7iTNMsvCme4glIioRWHWBXbV-AX10PrfVOB04Zxl1Q7Fv_IcX-OJmoiI5xqk2_tMflCwWbOJdj2uVKA_xbETsAIX4V0LqL9kTrEkiwChau8n1p6shzLRDgCUk9Aytf0nvxV138xwvnSWTHUC0PNFjMaRifFAKvF7W4jjSm7nIGR6v6kijcAxANzAoy3NQe8-TK320PMMvqqvo-cR3LCf5RLF0BXMje66lix9pv3OzCpqakphHfiLzelZbxgEajLZEMZNf-i8iIWhy_cNHpiLgbQSECLf3hRUjEMnU-OgH2wbb2PMk28ofrVK4KmIhQG5LyLEE0xh4DIBaYz9lXyCPNeKpxEOjrd1UcdW_6y4VWtjKLC7Bh_U2xG_gRNXzIQ_TqFQZ1xf8CJrPMMPPuwOjob_VLsA9ErHSR3nkcyI10tKTRLv6Ut2sl2I7QZZQCgGHNGceCq3K1sXhXTVFoQP4D82g0vnXhOY43i4t0nuzc9H5FjWJnQaqAvIb1Htt5ZgWO73mdj8GGqdZqXXa7YyAUQtvGo5zituyuY5R-CFaomogoJ_kYyGDcUMskuKLx-UKJ74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=Hwerb-xA10lfdcsh5ZKMD39Y5IjvUndf1txkYnS4J_PCElPWD6P3g2mBf_vX9uK4sw2-lJKr5et06PcqCvCWQYgXJANxkorhWLJaMFH7iTNMsvCme4glIioRWHWBXbV-AX10PrfVOB04Zxl1Q7Fv_IcX-OJmoiI5xqk2_tMflCwWbOJdj2uVKA_xbETsAIX4V0LqL9kTrEkiwChau8n1p6shzLRDgCUk9Aytf0nvxV138xwvnSWTHUC0PNFjMaRifFAKvF7W4jjSm7nIGR6v6kijcAxANzAoy3NQe8-TK320PMMvqqvo-cR3LCf5RLF0BXMje66lix9pv3OzCpqakphHfiLzelZbxgEajLZEMZNf-i8iIWhy_cNHpiLgbQSECLf3hRUjEMnU-OgH2wbb2PMk28ofrVK4KmIhQG5LyLEE0xh4DIBaYz9lXyCPNeKpxEOjrd1UcdW_6y4VWtjKLC7Bh_U2xG_gRNXzIQ_TqFQZ1xf8CJrPMMPPuwOjob_VLsA9ErHSR3nkcyI10tKTRLv6Ut2sl2I7QZZQCgGHNGceCq3K1sXhXTVFoQP4D82g0vnXhOY43i4t0nuzc9H5FjWJnQaqAvIb1Htt5ZgWO73mdj8GGqdZqXXa7YyAUQtvGo5zituyuY5R-CFaomogoJ_kYyGDcUMskuKLx-UKJ74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
عملیات آزادی عراق؛
در ۱۷ مارس ۲۰۰۳، جورج بوش بزرگ رئیس جمهور آمریکا در یک سخنرانی تلویزیونی به صدام حسین و پسرانش (عدی و قصی) ۴۸ ساعت فرصت داد تا عراق را ترک کنند.
او هشدار داد که در غیر این صورت، حمله نظامی در زمان انتخابی آمریکا آغاز خواهد شد؛
پس از پایان اولتیماتوم، بوش در اتاق وضعیت کاخ سفید  او در آنجا دستور رسمی حمله را امضا کرد.
بیش از ۱۰۰۰ بمب که بعضی آنها ۱ تن وزن داشتند و ۵۰۰ موشک کروز تاماهاوک را به سمت مواضع ارتش صدام شلیک کردند، بین ۱۵۰۰ الی ۱۷۰۰ سورتی در ۲۱ مارس انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69471" target="_blank">📅 19:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69470">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=EN70KwAAieWX1C8A7di4UbNWRCP-ZNvHB5uR8yXUf9AIcyjBOMk06kh5kyrBhSL5Uw67-acrbq9enPwCUFXVJqgNJXx_1jeMvcNGjIHYMqU2cqkfnesvMlaPk_ccqpcJRUw5FQCa1kcE4jZ7sTDgb_xu1mlPWMC4PjZmfX_CQBvNvLn48iM7FXRLvMRx9aQJlHSnGZ8lbfeeiQ_v3A0t9miROzIBsqcHIjziH9hALxhDT8kFN3HSIzqiYhjFdFV-6V6aFa8U2gD5xQ0F8U6vNGkp63lwHMHXnU-88ySDxWDtmf0hFvooXuz1VGBwl72ODPDzl7xd6FZ-iqx5nn_Z5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=EN70KwAAieWX1C8A7di4UbNWRCP-ZNvHB5uR8yXUf9AIcyjBOMk06kh5kyrBhSL5Uw67-acrbq9enPwCUFXVJqgNJXx_1jeMvcNGjIHYMqU2cqkfnesvMlaPk_ccqpcJRUw5FQCa1kcE4jZ7sTDgb_xu1mlPWMC4PjZmfX_CQBvNvLn48iM7FXRLvMRx9aQJlHSnGZ8lbfeeiQ_v3A0t9miROzIBsqcHIjziH9hALxhDT8kFN3HSIzqiYhjFdFV-6V6aFa8U2gD5xQ0F8U6vNGkp63lwHMHXnU-88ySDxWDtmf0hFvooXuz1VGBwl72ODPDzl7xd6FZ-iqx5nn_Z5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
اکثریت قاطع ایرانیان، اسرائیل را تحسین می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69470" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69469">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=p6oDcGScQNpz4Y52sjd0crAt6tZIrz7aty6z6MNQOheck7hgKo5qyEGREqRRS9t-0tA4IleXSwTdnheJ6zrAEP8EA-iCxOELCWxfABnSpSWtpvDHLMhvkrYvCsmAxVKrfQ6Y0GXmPD2fWPnVhSZuUmIQrALlDYqKmqePYCEZHkJeDDZqUISepf0_PBljoUwVi0curXZbGa8_bfYVNzx23bFtZ-yaMdXNHKCppl6C1rSPds5l4O8iOAh4yg0IcgeIG12HS6YfanbwFu0ygmZ4TxS4IapUQEWMKrV1vSXbGkM_hgVQBxhHcEa2q4Gy7Mh9HE_hNi6_a39RDoQ7dgtbzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=p6oDcGScQNpz4Y52sjd0crAt6tZIrz7aty6z6MNQOheck7hgKo5qyEGREqRRS9t-0tA4IleXSwTdnheJ6zrAEP8EA-iCxOELCWxfABnSpSWtpvDHLMhvkrYvCsmAxVKrfQ6Y0GXmPD2fWPnVhSZuUmIQrALlDYqKmqePYCEZHkJeDDZqUISepf0_PBljoUwVi0curXZbGa8_bfYVNzx23bFtZ-yaMdXNHKCppl6C1rSPds5l4O8iOAh4yg0IcgeIG12HS6YfanbwFu0ygmZ4TxS4IapUQEWMKrV1vSXbGkM_hgVQBxhHcEa2q4Gy7Mh9HE_hNi6_a39RDoQ7dgtbzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
خاورمیانه دیگر آن خاورمیانه سابق نیست. ایران هم دیگر آن ایران سابق نیست. ضربات سنگینی به آن‌ها وارد شده است.
آن‌ها همچنان توانمندی‌هایی دارند، اما به یک ماه گذشته نگاه کنید؛ آن‌ها به سمت ما شلیکی نکرده‌اند.
چرا شلیک نکرده‌اند؟ چون می‌دانند ما می‌توانیم چنان ضربه سنگینی به آن‌ها بزنیم که بازدارنده باشد. اگر به ما حمله کنند، متحمل ضربه‌ای بسیار سخت خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69469" target="_blank">📅 18:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69468">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=aFd-dkzxYCzkgmt0KixQYpjwQOSdbK7Lylo5vcNWjpur1WX1OfJTBYmdu9atFlelM6QcNMOniJk8hX9zRBX7eF0sbY8YIDNDRQ240pkW65hftZzD3Cl3VuZXkOqywOGt_adDV1kwU9s-PNOfoXV3Et0Nc9-6XOu7IBC1JJRxqfMw92NVCFAATvCDsZgu8KQl3eD2CxkBDEDBsEw3TAuxp3biPXNjv9PNWoIEGlEGP8O8MUoHDxpfPAG2Pnkkv8WLgbYAmW2MePWRaTQBDD2BBsAEeLgqnv-IfPvxrRAU4BwejYCarhZq1edZz9KSaYI4QRR9kjzrNp0ACDvn0vyaVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=aFd-dkzxYCzkgmt0KixQYpjwQOSdbK7Lylo5vcNWjpur1WX1OfJTBYmdu9atFlelM6QcNMOniJk8hX9zRBX7eF0sbY8YIDNDRQ240pkW65hftZzD3Cl3VuZXkOqywOGt_adDV1kwU9s-PNOfoXV3Et0Nc9-6XOu7IBC1JJRxqfMw92NVCFAATvCDsZgu8KQl3eD2CxkBDEDBsEw3TAuxp3biPXNjv9PNWoIEGlEGP8O8MUoHDxpfPAG2Pnkkv8WLgbYAmW2MePWRaTQBDD2BBsAEeLgqnv-IfPvxrRAU4BwejYCarhZq1edZz9KSaYI4QRR9kjzrNp0ACDvn0vyaVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دیروز روسای دانشگاه تو جلسه‌ گله کردن که چرا حقوق اعضای هیئت علمی دانشگاه رو با تاخیر دادین؟
پزشکیان هم تو جلسه کلش خراب شد گفت:
نامه نمیخواد، اون گوشیو بده من بینم...
📞
«سلام؛ حقوق هیئت علمی دانشگاه‌ها رو ۱۰ روزه ندادین. خداوکیلی این درسته؟... بده دیگه... دستت درد نکنه، خداحافظ.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69468" target="_blank">📅 18:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69467">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04343db3da.mp4?token=tHtprhbCS6jtPa-TjzPY6cTHka8zE6s2UyPOPqDc-kXbbIqkjMCEa6BbVOWuT_j-KctFWdbeNTthgnfTuM25_fZ7Pn3IltEWb3nuEKEkJwrbmfqo1scjJw4ZX-ACipi4HnODPkkw7JU7AWO-D7CyC1FLY3QeF2sXoTTu927wnDsusnZy9P3O0Fa-iYTH0yHdIuCh5mzvuHxpSd-HnUjvEwkfxOdD7rGW0ERkvDLJqwBXwD3JjrA_lkI70zQ9tdmlB81HE9D3d9LZRhp17XVO-mdVWw-O8cczgQ0KRipWD0-A0zY8dami0kNiD7wxAeRylJuVyuHvA7dcZauJACf6DIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04343db3da.mp4?token=tHtprhbCS6jtPa-TjzPY6cTHka8zE6s2UyPOPqDc-kXbbIqkjMCEa6BbVOWuT_j-KctFWdbeNTthgnfTuM25_fZ7Pn3IltEWb3nuEKEkJwrbmfqo1scjJw4ZX-ACipi4HnODPkkw7JU7AWO-D7CyC1FLY3QeF2sXoTTu927wnDsusnZy9P3O0Fa-iYTH0yHdIuCh5mzvuHxpSd-HnUjvEwkfxOdD7rGW0ERkvDLJqwBXwD3JjrA_lkI70zQ9tdmlB81HE9D3d9LZRhp17XVO-mdVWw-O8cczgQ0KRipWD0-A0zY8dami0kNiD7wxAeRylJuVyuHvA7dcZauJACf6DIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو ای از یک طرفدار حکومت که میخاد ترامپ رو بکشه:
میرم خون رهبرمو از ترامپ بگیرم یه دهنی ازش سرویس بکنم از یادش نره
از لحاظ دفاعی یا هجومی همه جوره دهن ترامپ رو میارم پایین
حرکت های رزمی‌شو ببینید فقط
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69467" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69466">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEXHGiavPHKyvtov0k7yMng2NEca6AQsCbYgELwGpcTMEiJhCHbLW3ir-CieYW7ZAmVBsUpGCHSEmTPrRwNh9o9YrCwXsj2dy4LcnS2vxRR7SfNbNX2LJi2lzjhyhKDP0cO4psvuEXFoEnV6KREeYVlNgZMOZVDVPHLUk5WZctCjrYfZw57ThwtIcDB99-TqmWiOQcoN8QP2ulM2nKsL8pESEk28fySt369fLfcaNJfbj22X_DbRjA6wWcwb368pc4LewGVmUmU5AtVYLpoPNpu6GWrUpbL2xP-cdpaMlb3YZYQVBQVzVSpPoXl9M2cGn6hvcMxWk_DeizoxrIQe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛المیادین به نقل از یک منبع ایرانی:
ایران در پاسخ به آخرین پیشنهاد آمریکا، با بازگشایی تنگه هرمز تا پیش از پایان کامل جنگ مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69466" target="_blank">📅 16:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69465">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnFhcgQOpt-exzU2YPLlzpKEU__aTfAI3ECt3aECzXE0hYjEhTrLt2HwdaieceYtvK5w_nHn1v1YiV71LRH3m01S5tAkR_JD5UOf6n1ouX76OBxyk1BH3ssVoYUsEa4KuM0eIxjSX0AEgB827QuwbXjpzu9KPCzafNjZUoBR0lhNpB1XOnYgnUwiMWMebddftNXiLHUw5hlZCN9BMqnMf8MaaoYo2O93XH6zMUctvdiQbYGPwVr37M3eldrwExwKRD8C_xWWIhvdWAeIhKsA-obrNrEtf2NvCImU6Xq3yQHTt7iVNHrcnTSRFIkBm9wObodqQG9bniFhEgaj8mHBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست میانگین IQ کشورهای مختلف تو سال 2026 هم منتشر شد
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69465" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69464">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863fff3357.mp4?token=Ppu2Zf21RnfdUv0wbPgJtKfB6e5r16KlTz0URRvfiV3uSYClRb66wEXr7BPaJdVj9r45OTdIvh6oof1FGDdmMj7CQLVANQPfPbcY_9-pep1QM1juEOF334Ri8QXKuUdiJWUOzSm7Vca6fkBOISje8fY2lsyPkbQC20IsEQWcpT3-FGWgqemI-vJm6q2zCEUnVSiCxhQWcC_0DpbqdSqeEiH3cvUsqjQxm_VBiXqV8EblQGM1iPDFiJWpexjNFfll2fyhGZPK8LtsswQcAaJ74wqp4pd51GklPIJ4YZVgCOE7NF3yGk7fpWr-MuFRKOxuuj7Qtaa_QibPFUJV8DlpJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863fff3357.mp4?token=Ppu2Zf21RnfdUv0wbPgJtKfB6e5r16KlTz0URRvfiV3uSYClRb66wEXr7BPaJdVj9r45OTdIvh6oof1FGDdmMj7CQLVANQPfPbcY_9-pep1QM1juEOF334Ri8QXKuUdiJWUOzSm7Vca6fkBOISje8fY2lsyPkbQC20IsEQWcpT3-FGWgqemI-vJm6q2zCEUnVSiCxhQWcC_0DpbqdSqeEiH3cvUsqjQxm_VBiXqV8EblQGM1iPDFiJWpexjNFfll2fyhGZPK8LtsswQcAaJ74wqp4pd51GklPIJ4YZVgCOE7NF3yGk7fpWr-MuFRKOxuuj7Qtaa_QibPFUJV8DlpJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مشهد یه دوره‌ی آموزشی گذاشتن برای افراد بالای 60 سال که توش مبانی اولیه‌ی استفاده از موبایل رو یاد میدن؛
موضوعات آموزش:
آشنایی مقدماتی با برنامه‌ی بله
آشنایی مقدماتی با اینستاگرام
وصل کردن فیلترشکن
ارسال لوکیشن
تماس تصویری
ویرایش متن تو واتساپ و بله
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69464" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69463">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda203069a.mp4?token=nIIvk56wK-KyhOl33ojcOxN7iS05vshl460e8MfPSum3LZ8JevnIlPh-G5eaSsH_KiZorInW17bIB_f-5vQc66vJ2Zf0RQpnnmCQOGwlAVR7LVDgdNCrzkR5FXTorr5AEsonyBVaVG2jkagQ3a7sde-h43WC3zAn3FuwcG5FQrLvC6wNpdmrCyXnAB18EwtSwBX1f0TbDg-NjunoqbBjTxOkrngrLnC0VPJRSGg3niLFEYMO6Wox-DZGg592ATVnlui77DxVlyTs9_DA7aPWuHGWquUQlaE_rr9Qx6oTHZskNJT-G1nP_xDnsYl_0sNhvKaNpcbHaiAyv5VZ8l0qYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda203069a.mp4?token=nIIvk56wK-KyhOl33ojcOxN7iS05vshl460e8MfPSum3LZ8JevnIlPh-G5eaSsH_KiZorInW17bIB_f-5vQc66vJ2Zf0RQpnnmCQOGwlAVR7LVDgdNCrzkR5FXTorr5AEsonyBVaVG2jkagQ3a7sde-h43WC3zAn3FuwcG5FQrLvC6wNpdmrCyXnAB18EwtSwBX1f0TbDg-NjunoqbBjTxOkrngrLnC0VPJRSGg3niLFEYMO6Wox-DZGg592ATVnlui77DxVlyTs9_DA7aPWuHGWquUQlaE_rr9Qx6oTHZskNJT-G1nP_xDnsYl_0sNhvKaNpcbHaiAyv5VZ8l0qYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
میزان شانس بقای جمهوری اسلامی از زبان مراد ویسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69463" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69462">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b293a286.mp4?token=XYcNfPPRiC9248CHb6AZiL5EjR2wZXCagifXWFttOmPUESE-HzcOHWuMyZ8KPtxwpsDahwl08_wtEYI6dqVFZWMuk_y1T10eDdjG7HIDVeOkBb0PfYD_19dyC5MoJcRMi_5gK-dGCbIuwny4jBsq8KJQqh49nmoLfCS6cu2z-LHyker5viLd9fwMQODGg7PtKF1VapFSoEG3RFOgoJ5Ca8KWC-lz6RhhBJqKtpo0_biCFe4H0KNpkQiLloqh0hgY-ndGiI1IL08xNE203s96xzwV3C38ZjwrKBocPDckk050yIhCoHV3uBTsyb7Y0i0aL4YbTtpsCkS09nq_uNqJ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b293a286.mp4?token=XYcNfPPRiC9248CHb6AZiL5EjR2wZXCagifXWFttOmPUESE-HzcOHWuMyZ8KPtxwpsDahwl08_wtEYI6dqVFZWMuk_y1T10eDdjG7HIDVeOkBb0PfYD_19dyC5MoJcRMi_5gK-dGCbIuwny4jBsq8KJQqh49nmoLfCS6cu2z-LHyker5viLd9fwMQODGg7PtKF1VapFSoEG3RFOgoJ5Ca8KWC-lz6RhhBJqKtpo0_biCFe4H0KNpkQiLloqh0hgY-ndGiI1IL08xNE203s96xzwV3C38ZjwrKBocPDckk050yIhCoHV3uBTsyb7Y0i0aL4YbTtpsCkS09nq_uNqJ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعترافات عبدالباری عطوان (تحلیلگر سرشناس جهان عرب) رو شنیدید؟ کسی که همیشه به مواضع خاصش معروف بوده، حالا لب به اعتراف باز کرده و از کابوس کشورهای عربی پرده برداشته!
عطوان در تحلیل اخیرش (مارس 2026 )به صراحت میگه:
اگر پسر شاه (شاهزاده رضا پهلوی) به ایران برگرده، با توجه به اتحاد استراتژیکی که با اسرائیل خواهد داشت ،ایران به چنان قدرتی تبدیل میشه که تمام کشورهای عربی منطقه باید جلوی عظمتش زانو بزنند و عملاً به نوکرهای ایران تبدیل میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69462" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69461">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=bfEh241y0iFY0YzipNZ6VRpFfqXKqwgTQoFTjFSW5pH_bOUZIUIIqjtK7J9gc7_9QJ_g9OI4ONfw9crP0-TXWfaWoKKOBhhKkp7HE8C9mqfNRlXo22qUJ0_WzL8BubyEXRFkoQdud0aDVg9zTkwNhAzd35m-nuoVQ5paT2Ld2-AyDZJQmGxxIF1_A2goY8ZRHM6gql6bkrrxoOqrkU1FGOmlTSpuNR7hp_8UxE33RiXnQ9lPB8VBpdWXwEkz8O4Jv75T6djMX6pa7vXN9Znb-3TBbocMKCAmt9IOZJ0dyKpfEYquSBsvogJ0hdxVF-aKZE1-1DtLkdqwIhKx1neaCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=bfEh241y0iFY0YzipNZ6VRpFfqXKqwgTQoFTjFSW5pH_bOUZIUIIqjtK7J9gc7_9QJ_g9OI4ONfw9crP0-TXWfaWoKKOBhhKkp7HE8C9mqfNRlXo22qUJ0_WzL8BubyEXRFkoQdud0aDVg9zTkwNhAzd35m-nuoVQ5paT2Ld2-AyDZJQmGxxIF1_A2goY8ZRHM6gql6bkrrxoOqrkU1FGOmlTSpuNR7hp_8UxE33RiXnQ9lPB8VBpdWXwEkz8O4Jv75T6djMX6pa7vXN9Znb-3TBbocMKCAmt9IOZJ0dyKpfEYquSBsvogJ0hdxVF-aKZE1-1DtLkdqwIhKx1neaCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
عراقچی داره میره اربعین و ماهم توی تهرانیم.
دوشنبه مذاکره ای نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69461" target="_blank">📅 13:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69460">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
از فرصت تفاهم‌نامه و لحظه‌به‌لحظه آتش‌بس نهایت بهره‌برداری انجام شد
در این مدت، واردات تجهیزات جدید، تعمیر و بازسازی سامانه‌های آسیب‌دیده و همچنین تولید سامانه‌های جدید در دستور کار قرار گرفت.
پهپاد‌های جدیدی که اخیراً از آنها استفاده کردیم نیز حاصل بهره‌گیری از فرصت ایجادشده در دوره آتش‌بس بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69460" target="_blank">📅 13:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69459">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08375903ec.mp4?token=mjatPWduL0T29qFDrA7T_P7GN_vSC42VFdI01wh4pqzT2OBo1pn_d2V6DCBVzwWeqK2wxcKkUCdvMjXktpEUIhtzeGYzjeB8G0C32EJzk8FxPucQGY8AqFAjra5U50QB2W55FVCXIOFKd45VvEaP277FfvBgqxAujo_arAblfphxo_wwgyM1Pkxtghk24szBjcJM1YoMYxD9EsIO5Dy6oI__MpKkmq86GVINVHEcHx3OcDUMaTgnubdcdeprK22AQD88vBrFAZh3QmDtJAk4YEXj7J83kUlQvYeA2p0sUjsGzjeZaSyYVR6sPZjK5u3DfmlLoQMI-aAf7zNMC8lHhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08375903ec.mp4?token=mjatPWduL0T29qFDrA7T_P7GN_vSC42VFdI01wh4pqzT2OBo1pn_d2V6DCBVzwWeqK2wxcKkUCdvMjXktpEUIhtzeGYzjeB8G0C32EJzk8FxPucQGY8AqFAjra5U50QB2W55FVCXIOFKd45VvEaP277FfvBgqxAujo_arAblfphxo_wwgyM1Pkxtghk24szBjcJM1YoMYxD9EsIO5Dy6oI__MpKkmq86GVINVHEcHx3OcDUMaTgnubdcdeprK22AQD88vBrFAZh3QmDtJAk4YEXj7J83kUlQvYeA2p0sUjsGzjeZaSyYVR6sPZjK5u3DfmlLoQMI-aAf7zNMC8lHhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نیروی تفنگداران دریایی آمریکا ویدیویی از تمرین‌های تیراندازی نیروهای خود منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69459" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69458">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8ovncL21y-7MrpptDmdnKPjxxrZ9bEFm1sGqBoOWajMZKFGYwchSVpLCT7WK5qPUMvWU95wHhC8s7J3WNjJNPgojPQfuM0GL8j888azVJqKXdXYhocNcL4aFBszJ71n1V2OWSDc6RvjY59OKJuzcyXdIbM8dnJyDpb4G5e5DJ9xZpMpyGpEvHe2Lo7_PPPALxu1cj2Tyt2WyS02z27AGlSnUwNTgl7F467FN04nRcxNyzkb8cxwUFDGosQSH9SjnESI5b6kBV-iIpjdIH3H6cjWQKC79Uj4zNICct3pnevOUUH_lJuCtc9SI-Fh-U6iFNwdaE-msVDgl8Bo8emjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی، سخنگوی وزارت خارجه:
ما در حال حاضر هیچ‌گونه مذاکره‌ای با ایالات متحده نداریم و مذاکرات با عمان بر دستیابی به توافقی پیرامون عبور ایمن کشتی‌ها از تنگه هرمز متمرکز است.
هدف، تعیین مسیری موقت است که ایمنی کشتیرانی در تنگه هرمز را تضمین کند.
تا زمانی که محاصره دریایی و اقدامات ایالات متحده ادامه داشته باشد، هیچ تحول قابل‌توجهی در وضعیت تنگه هرمز رخ نخواهد داد.
🇮🇷
اسماعیل بقایی، در واکنش به ادعای جلوگیری عربستان سعودی از حمله آمریکا به ایران:
اینکه همه کشورهای منطقه اذعان دارند که از تحولات و شرایط آتی منطقه متأثر  شد، امری مثبت است.
جنگ ایالات متحده علیه ایران، جنگی علیه کل منطقه است.
طی پنج ماه گذشته شاهد بوده‌ایم که حضور ایالات متحده در منطقه، موجب افزایش ناامنی و بی‌ثباتی شده است.
طبیعی است که کشورها برای جلوگیری از تشدید ناامنی تلاش کنند، اما تجربه نشان داده است که هیچ‌چیز جز قدرت و توان بازدارندگی ایران، مانع دشمن نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69458" target="_blank">📅 12:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69457">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=dRbfkGOiPZO8JcJRZmOufY9dHM1J3jvQDBi2PhTK9sc3qxByLHsIjH3Es4gJkmQB2Y7nwgjIzC08ox-3OGnihtqfXicMldeCOHTraoRJxWdB9UuDtAaPLLRmYViG50i5CXG1JZG6FB-uZmjp_HHAORLe7mf8qHk9MvMIIkuMbWBE5qzRtp6WzPIFzIUNDpgi2EGgv-9enhVBiM4QdwNK_erGe3Lf0Sn4ErubpR_yjP0yow3kHuiBqEcrkNQCZYuZyxhLBEwYJDLVFaZmozTP28JgbaOc5Q1cExwNwMC61xbLc_uCdmy8Tju1r6P2lwh2wkHbB6S2tzdg437ypQ5ARA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=dRbfkGOiPZO8JcJRZmOufY9dHM1J3jvQDBi2PhTK9sc3qxByLHsIjH3Es4gJkmQB2Y7nwgjIzC08ox-3OGnihtqfXicMldeCOHTraoRJxWdB9UuDtAaPLLRmYViG50i5CXG1JZG6FB-uZmjp_HHAORLe7mf8qHk9MvMIIkuMbWBE5qzRtp6WzPIFzIUNDpgi2EGgv-9enhVBiM4QdwNK_erGe3Lf0Sn4ErubpR_yjP0yow3kHuiBqEcrkNQCZYuZyxhLBEwYJDLVFaZmozTP28JgbaOc5Q1cExwNwMC61xbLc_uCdmy8Tju1r6P2lwh2wkHbB6S2tzdg437ypQ5ARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله پهپادی روز گذشته به مرکز لجستیکی عظیم شرکت وایلدبریز (Wildberries) در نزدیکی سامارا.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69457" target="_blank">📅 11:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69455">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO7l2okGzuttHGPyYVTR--vEw2miz5wZOhL0A3Rj8hvFDyrl7S2rF5-OB-gppNFHm1UYLEocR9lztYh7jAqmRQJ9veN-8VR5IQk9iOp9Aiyo2WShtyFD96RQWnwzU4ps-1DIA9YuyCn6wOtt9kevGNtBzxW1VZoogNZM1PlHcGkmIdkdqYlHVnIarsVd8-18EEJwRKKzhc-1CAiqHyER8IJ0PJrRAN7Zf12zXd2ODPZDB4hwfQAWKWNTBchtZiCHJUFHvTNbuLsHw4CCEBF8MFIQErW4jtL6PLLmxtmQUboqyI1sKyOi6PKU274t7bcsGF16_4nP70ZPRvkMNIpYQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=ktCrsPSsLdOhJ3ALVTYiUR_Xg8SKFtj0Mg7VvRrawKyi7GxrOprPVYxF3E80sVbV6rBjqqRbB2khgV7EAvG7hZ7cHcwsurHsy_m1GvEfd5-4DRTyzWF8oew7YjFRH_50Mx5-fNmpOAAhIAqvejtCWaubotiHf47vxQ48pNEDOGaWcF5FIHnMbQplz-hlwlQ5DvyhAWv3l4OuxEEGSgIOkHlOM7SvM4G3Vrj7f_J0cDLy3vRUdRYE3bx-Vsurgaa-b8ubtjNHqsscgbk0cexn3OWRBHwJyufkLmXGo8UEc5HXFDrRcZpiW5-mpeFhx9Wndqq3lfO5qTM866cyN8jrtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=ktCrsPSsLdOhJ3ALVTYiUR_Xg8SKFtj0Mg7VvRrawKyi7GxrOprPVYxF3E80sVbV6rBjqqRbB2khgV7EAvG7hZ7cHcwsurHsy_m1GvEfd5-4DRTyzWF8oew7YjFRH_50Mx5-fNmpOAAhIAqvejtCWaubotiHf47vxQ48pNEDOGaWcF5FIHnMbQplz-hlwlQ5DvyhAWv3l4OuxEEGSgIOkHlOM7SvM4G3Vrj7f_J0cDLy3vRUdRYE3bx-Vsurgaa-b8ubtjNHqsscgbk0cexn3OWRBHwJyufkLmXGo8UEc5HXFDrRcZpiW5-mpeFhx9Wndqq3lfO5qTM866cyN8jrtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده مردم در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69455" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69454">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=PwuBw5FTp_5XZoacyTSp3XCmDZt_pY-gSKuLYtv_YQO5u63yDDKyWDLbufcRHrXjDyai0BJZBZKRrE-wUROCQE73RAlv41fvyFmzb93Gh6QBBHbw45IDWeqU3RWaJXDU2JshNiPtbnm5Bb1aQ88_PvRPSgGkRk9S3jxq4Dg8YKAKwF_s2GzFrxX_uNIA4oiAjQe6h-afyXFzZd-syA13smVoawyImMK0XYEU7NCLYD-Mjtf-CZxT9E2XZ3fqkPDwX1IGooQQ0XuYGtEUAV_F0iZM1Rc1pNalkc7VJRvO4rl89LJH2l6PXg9k7obREDTSRm7UNBUuIQWMPiFNKiJABQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=PwuBw5FTp_5XZoacyTSp3XCmDZt_pY-gSKuLYtv_YQO5u63yDDKyWDLbufcRHrXjDyai0BJZBZKRrE-wUROCQE73RAlv41fvyFmzb93Gh6QBBHbw45IDWeqU3RWaJXDU2JshNiPtbnm5Bb1aQ88_PvRPSgGkRk9S3jxq4Dg8YKAKwF_s2GzFrxX_uNIA4oiAjQe6h-afyXFzZd-syA13smVoawyImMK0XYEU7NCLYD-Mjtf-CZxT9E2XZ3fqkPDwX1IGooQQ0XuYGtEUAV_F0iZM1Rc1pNalkc7VJRvO4rl89LJH2l6PXg9k7obREDTSRm7UNBUuIQWMPiFNKiJABQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای ازجواد موگویی که توی برنامش داره خیلی شیک و مجلسی جای همه فرمانده‌ها و مسئولان رو لو میده:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69454" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69453">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVB7BNxeGF8UQqwzCRc5ociU6rYzErAslJJ-F92gr6hbUvchtDHUNKVlqVlzakXLgekUC5bRapIbqKFkwqVr7e9P6EqrLftP49ZVsXDifBiG9oQ3YKBXRIZNJv8hyQ7mNg4Uh9CsRoq3THbjCRNel-239uSzJAZXvCHw-gxep-IlRxUJ5rqY8WPoNEhUjOYcHY0JqKVo2fGBBShOqLVme-pivbhlbHCcjp3rtZqTdSqd2_4V9_nmGxROwxY2zpaStFgBLdxdml3tkS7ODZQ2W1DTgB7UzMuMxAh8cUOYyJSHXx9ZjtL-YI0w-BesVTH6Wt850xsrP7eAPmOTTTqF5V_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVB7BNxeGF8UQqwzCRc5ociU6rYzErAslJJ-F92gr6hbUvchtDHUNKVlqVlzakXLgekUC5bRapIbqKFkwqVr7e9P6EqrLftP49ZVsXDifBiG9oQ3YKBXRIZNJv8hyQ7mNg4Uh9CsRoq3THbjCRNel-239uSzJAZXvCHw-gxep-IlRxUJ5rqY8WPoNEhUjOYcHY0JqKVo2fGBBShOqLVme-pivbhlbHCcjp3rtZqTdSqd2_4V9_nmGxROwxY2zpaStFgBLdxdml3tkS7ODZQ2W1DTgB7UzMuMxAh8cUOYyJSHXx9ZjtL-YI0w-BesVTH6Wt850xsrP7eAPmOTTTqF5V_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مارک لوین:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69453" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
