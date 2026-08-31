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
<img src="https://cdn4.telesco.pe/file/DpwU85WkkTHmIyBfLtCzPo4brBpvbgP3fZ-pkYF9o8no2I3h4w79Z23_9HDg87q2lu8aChM1QNjilYl0ez_efsZjHF1Ihq9x3BYQJIOKomEwnLg_MihA34yjV2Otzx6y_2oggQrFkyyA7yWhQRoQZwvMcjYUOLbLzQq1iIzQg7ZXoUh9WpeWiW-0awuCBklTq0iaYcX-6mqhVZd9FSs3s5GpMHqCGlaVVrODG5EeraxV4nAt-j85dwltDMa0VuREfFOXNWetRtbqRTE2843y-iEKRoKE3MVNRWIZfDARnSp7Lf9fKe14708Un0ShIr01wja48lJe99_tqrU7rTQOhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 114K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-70884">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⏺
🚀
فارس:انهدام یک فروند پهپاد MQ9 در شرق تنگه هرمز
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/news_hut/70884" target="_blank">📅 19:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70883">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f517057c.mp4?token=wBtnk8YviofleUf8iUMB_5EhpsROtRzHeXWWBKM5MgLs02_9hYg0xmaKnzZx0h11NKL9LHdifBiZIFQgdE4HghAP9LodAJNtVqatZz4C776nRdCKba5UYV-ynsZNaLlG81u8XljAh8x7E-JBJZqepfkCUQOdKAYFAYf1akqkgJ2W1EoUoVsq4JSyR-Ie5sZm6uMV95uXN3nkrjZ_ztAzHWpOcQHinBcq4OP-1foa9zpFMJBZa18mEdHbDLjXdkzY-4LkIpRY62V3Dcjqf9kOkREAg_D-Wl_cXAPWrRjfyM3518QJNBwWH88R2OCBhfZH0o0LzIG0mMrkqo1tMvinzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f517057c.mp4?token=wBtnk8YviofleUf8iUMB_5EhpsROtRzHeXWWBKM5MgLs02_9hYg0xmaKnzZx0h11NKL9LHdifBiZIFQgdE4HghAP9LodAJNtVqatZz4C776nRdCKba5UYV-ynsZNaLlG81u8XljAh8x7E-JBJZqepfkCUQOdKAYFAYf1akqkgJ2W1EoUoVsq4JSyR-Ie5sZm6uMV95uXN3nkrjZ_ztAzHWpOcQHinBcq4OP-1foa9zpFMJBZa18mEdHbDLjXdkzY-4LkIpRY62V3Dcjqf9kOkREAg_D-Wl_cXAPWrRjfyM3518QJNBwWH88R2OCBhfZH0o0LzIG0mMrkqo1tMvinzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
فرزانه صادق وزیر راه:
به علت از بین رفتن زیرساخت‌ها هواپیما بدون رادار هدایت می‌شوند و تعداد پروازها کمتر شده است
👌
@News_Hut</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/news_hut/70883" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70882">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇦🇷
پست جدید لئو مسی از خاطراتی که واسه تیم ملی آرژانتین ساخت
🩵
@News_Hut</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/news_hut/70882" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70881">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70881" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
http://TrexBet.com</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/news_hut/70881" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70880">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyZ7_Fhg2OBUZNVbg9B4uBtUt9TPf2MMdWyQJkoWEGijH3KpuViHC563AMjWZqFThl4FLHJlNIM5bkvpZYf-smbGD4YjIz_jcmqMfO9rNJ1jKcTuWrUorZNIBSU788STm0ZsIfEv1qD_V0LXbIEDBS-sYiQA2gXRu4Gd9eNeX-v0L91pzzGqcI6_9eGpUDDh9vasKgvk7QxUMYO-1gmuF4GzQ1GoEoOAcGfvvq_guEENZG-ALir4Nf88YIqs1kiJMgoCO0-YjVa1__POC2wWstxn4BtZ3WGlW81QCoX4esql4vO1kj69pkososmBpUrarOGE428hrb-pWGWzZNF5Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
میکس پیشنهادی ضریب
〰️
برای بچه‌های
TrexBet
🦖
Code TrexBet:
SKCU6
آموزش استفاده از کد شرط در سایت بین المللی تیرکس بت</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/news_hut/70880" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70879">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8uCQ53S67N_UCgJOQ0DsnC8rbFhp0EDfT5RHWOjGOjqCpvqqxpLPHvteQboZf6cgjaMzo-0bthUmV4RUxYiy-fnlsr9pQt6PKOTdc9fojpv1Jn7u4mKwZijQN__6bVflbW3EASU2MUMvmQ5x8VTeiLVT_1JdhtggfcJicjTnBTPgQSji6mMD1iQU6qFaNtDtb2vIvHpWfuHu_daSumNJSGoR36jH2q45H8A7yeYjBbPdE5HzTPeWazi8YaTrOlXlP43ZKeio1iQtAXVwWeUyhDSwStrTH7JiKX1t0SVeGm0j8P5OUaiewAm9kAwWRJ9ze_ViZwyxlB8qEYyINvy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💋
#فوری
؛لیونل مسی اسطوره فوتبال جهان از تیم ملی آرژانتین خداحافظی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/news_hut/70879" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70878">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=jTcPALFHQKmgC8xKM0gjnJ0FBRgA7DHMx5Qr7-7ONyLU9D0XDUQTmSdC1UhhW1CW0KknP9nmlcYmTljSfcJIp736NEn5iDKKkzH2afZC0-iE_Yddx_aV0eVsj5yZqm8f8M2V6G8swIsApJEl-7-RThc5otDv8k2VEUxcHePPUVFM_iqHjVI6OasdDBn1TGUE9dzLmcBWKi4gQu9Pq5pR16HQQ-oGksPyIaGwX0BwDWgnHpxbKAGbO84tzqYFTrZ-B8y2M0Gp8eaJu0nTBrMkxuVUD50IoEijLQOefpnhneRTbrKYD_mQ35EXfo8pXHzVeOQk-aitgzL7Hn7Z4JB2hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=jTcPALFHQKmgC8xKM0gjnJ0FBRgA7DHMx5Qr7-7ONyLU9D0XDUQTmSdC1UhhW1CW0KknP9nmlcYmTljSfcJIp736NEn5iDKKkzH2afZC0-iE_Yddx_aV0eVsj5yZqm8f8M2V6G8swIsApJEl-7-RThc5otDv8k2VEUxcHePPUVFM_iqHjVI6OasdDBn1TGUE9dzLmcBWKi4gQu9Pq5pR16HQQ-oGksPyIaGwX0BwDWgnHpxbKAGbO84tzqYFTrZ-B8y2M0Gp8eaJu0nTBrMkxuVUD50IoEijLQOefpnhneRTbrKYD_mQ35EXfo8pXHzVeOQk-aitgzL7Hn7Z4JB2hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدرضا نقدی:
ما انتظار پیروزی را داشتیم، زیرا به وعده و یاری خداوند یقین و اطمینان داشتیم.
اما انتظار نداشتیم که پیروزی به این آسانی به دست آید.
@News_Hut</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/news_hut/70878" target="_blank">📅 18:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70877">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=iLvM0IlrdilUfxcOoMHe5NJUVSQvfMi0DgU-kDL_hVmgJ1nMxUtQwgnbSSpHUtM7CgVKJ2xnIJTgo6izy8asFpQ8qk9QTp8yhebf__Mm7vgrO8aHKyYSnpzHDhr5ztZnXcPGIlXriNFsRpZsrfztKYMEPWuKo8UElh3bTWgq-ZpUJkgkUWBd2NgdTw4736oxiik634toLfDtwRXmTizE_P2HhVW8dxSHA3O66fIH0zrbgXbNuE_Z9UkwEo__wS9Jk9rrN6W3wWF71UXsvy6965RG4PNXmR6Woe7wxCLB9_ZWgCZ7lrHsRPuLpaG0bHPYoftFprudDQUcSQgCDUKHMoikgNsI3hX8wrCa4jUPSKQFjlZFwOUDKjTWXurnIJVlawp21ZJvZl5mYtFOaBss55x74UDPk2dWMtOD1DltSK9DRujtU_deH9eyfCDBsFipgxJjbz9yp3DfW5Al0IL1u3pmv4MlGHqLthaHDTuab4kQRE4MFQc8QRL28aIEPlbKrCmbDEUEpI1iUkt1oOdiutfcbLP-PIE4LXPjphpm5mNZ1fedHFmsvfnNDUiRLhuq-hjPTvGHzsN3NJL3YrfYQXp77Aw_wORo1KiiDyFeOEjrIvYkogmRS4RguEe2AjShBaeOQiSPD2jXvS5yHEuzhfJUtnLVoWDQCx7VZZ1YyPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=iLvM0IlrdilUfxcOoMHe5NJUVSQvfMi0DgU-kDL_hVmgJ1nMxUtQwgnbSSpHUtM7CgVKJ2xnIJTgo6izy8asFpQ8qk9QTp8yhebf__Mm7vgrO8aHKyYSnpzHDhr5ztZnXcPGIlXriNFsRpZsrfztKYMEPWuKo8UElh3bTWgq-ZpUJkgkUWBd2NgdTw4736oxiik634toLfDtwRXmTizE_P2HhVW8dxSHA3O66fIH0zrbgXbNuE_Z9UkwEo__wS9Jk9rrN6W3wWF71UXsvy6965RG4PNXmR6Woe7wxCLB9_ZWgCZ7lrHsRPuLpaG0bHPYoftFprudDQUcSQgCDUKHMoikgNsI3hX8wrCa4jUPSKQFjlZFwOUDKjTWXurnIJVlawp21ZJvZl5mYtFOaBss55x74UDPk2dWMtOD1DltSK9DRujtU_deH9eyfCDBsFipgxJjbz9yp3DfW5Al0IL1u3pmv4MlGHqLthaHDTuab4kQRE4MFQc8QRL28aIEPlbKrCmbDEUEpI1iUkt1oOdiutfcbLP-PIE4LXPjphpm5mNZ1fedHFmsvfnNDUiRLhuq-hjPTvGHzsN3NJL3YrfYQXp77Aw_wORo1KiiDyFeOEjrIvYkogmRS4RguEe2AjShBaeOQiSPD2jXvS5yHEuzhfJUtnLVoWDQCx7VZZ1YyPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمدرضا نقدی:
همه فوتبالیست‌ها با توپی بازی می‌کنند که طبق استانداردهای یکسانی ساخته شده است، اما همه آن‌ها رونالدو نیستند.
گل زدن نیازمند فردی با انگیزه، هوش و توانایی است؛ کسی که بداند چگونه از آن ابزار استفاده کند.
آمریکایی‌ها صد برابر ما سلاح در اختیار دارند و از موشک‌ها و پهپادهای بهتری برخوردارند، اما نمی‌توانند به‌طور مؤثر از آن‌ها استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/news_hut/70877" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70876">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=Ib33fc2xl3uSMWgDsHsvCtj6w_nGctCnGBcrVqxKEm0l420G5DTweR4nsRD3NWGcTOufnIYi2hEocsMGodh-HhuRY0lAxGda8bxbiC4n1LCfB4nq3_nxfeWNaqwtEqgMwVns70QksouXs1LyQs5btH_ktN9GH-xB_Feu1vWxkbdPm_5NYRhc6nW0pdNh4jbDa-jWCRWQOccgWX4hyNvRBBJE0xLRVHOeCU2sF61lzgnA1mrFQBKUUP3Ckhx_sMZEKuuvdK2er-wM4f1yHCyJkrHnkyJqmPZadqGlIHN-8xnGALOQc3i1UyG-QOZR7Q5W6pawUXuWKZ29Ptn-THUJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=Ib33fc2xl3uSMWgDsHsvCtj6w_nGctCnGBcrVqxKEm0l420G5DTweR4nsRD3NWGcTOufnIYi2hEocsMGodh-HhuRY0lAxGda8bxbiC4n1LCfB4nq3_nxfeWNaqwtEqgMwVns70QksouXs1LyQs5btH_ktN9GH-xB_Feu1vWxkbdPm_5NYRhc6nW0pdNh4jbDa-jWCRWQOccgWX4hyNvRBBJE0xLRVHOeCU2sF61lzgnA1mrFQBKUUP3Ckhx_sMZEKuuvdK2er-wM4f1yHCyJkrHnkyJqmPZadqGlIHN-8xnGALOQc3i1UyG-QOZR7Q5W6pawUXuWKZ29Ptn-THUJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماموران نیروی انتظامی روز دوشنبه ۹ شهریور ۱۴۰۵، به سمت کارگران معترض به استخدام‌های رانتی در پالایشگاه لیشتر گچساران تیراندازی کردند.
در این تیراندازی چند معترض زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/news_hut/70876" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70875">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbEBkEvhefNG-Ynw7mMf039yGDsZHYGZeM_NpHrxS2TDha6-1qkmx42KzgteP0O8A1RWCPv9gYmeHAv8hqQ9oGGXcpKvXX2Of1A2guZfWFzqnZS3aoEphmNXoEXltb0TT9s0f32Vjphn36_OBWv2-TQ0QflPFNvepTG9d5GRlrRVwL1uxtcuKhCj_eI5V53SNQXdAMItE9TkRIwnKyHATwn6oFQj4CrhrWbYudySrbzLySfMtf3IXZn3sQ6YIEYoUKE5RCc94iL23xpCewx9qYkvJzR7jHKc7xcM8vK_mHccWNGdas2wSBSknxWPU6p2CjvQHAUsmmiCG1HWDOzQEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضع خیلی قاراشمیش (یاغی)
وزارت نیرو اومده هشدار داده که مردم بنزین و گازوئیل غیرمجاز تو خونه، زیرزمین یا حیاط انبار نکنن، چون خطر آتش‌سوزی و انفجار داره و ممکنه با افزایش قیمت سوخت بیشتر بشه این کار.
گفته فقط اگه واقعاً لازم بود، مقدار خیلی کم و استاندارد با رعایت کامل ایمنی نگه دارین و موارد مشکوک رو به ۱۲۵ یا نیروهای انتظامی خبر بدین.
خلاصه مواظب جون و مال خودتون و همسایه‌ها باشین، این کارا خطرناکه و به نفع کسی نیست.
@Moris_news</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/news_hut/70875" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70874">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237073d371.mp4?token=sKPxXUhkNoYkYVnvTqOprXIm6MTCGGVbmhXsK6k5WoG9_gAmLzpD3NJ5DLOt5kZLeUFhWMEwCrt1084rlIvfABJqjkG6jUs6bc3do1ecwDmrGJsOgO1jtYBuAS4KXx1Y3mwGN6J3qmVIFhAwMaoFxgXf6xjgpP9yyv-DnMWhLdWpymhDS8Q9TkJRRZnnVSixLPC_0o-pnFoTPTfDExvZ0BZgT8tOf1d415NsZV7sv4En4ERe1sbBlTcj1TptaBgf6x2Q9zMDULNf7p4Rj94H_BbLZ0wsJV0U5MWEmIb_HtHKioNn6wmXNcCiQzmqWAgtPs19Vf10Zj4BfobhXn7Gmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237073d371.mp4?token=sKPxXUhkNoYkYVnvTqOprXIm6MTCGGVbmhXsK6k5WoG9_gAmLzpD3NJ5DLOt5kZLeUFhWMEwCrt1084rlIvfABJqjkG6jUs6bc3do1ecwDmrGJsOgO1jtYBuAS4KXx1Y3mwGN6J3qmVIFhAwMaoFxgXf6xjgpP9yyv-DnMWhLdWpymhDS8Q9TkJRRZnnVSixLPC_0o-pnFoTPTfDExvZ0BZgT8tOf1d415NsZV7sv4En4ERe1sbBlTcj1TptaBgf6x2Q9zMDULNf7p4Rj94H_BbLZ0wsJV0U5MWEmIb_HtHKioNn6wmXNcCiQzmqWAgtPs19Vf10Zj4BfobhXn7Gmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری دختر اکیپی قرار دعوا گذاشتن پسرا هم دوره کردن و تشویقشون میکنن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/70874" target="_blank">📅 18:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70873">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f793f615.mp4?token=MW-PZfV_gGbL1b7VaxSETmgLkvhhRyTdXjTOeH-WiEAPz7vtEOyqNOulldmxzh1R8MtDkiKxApgvqcKwVOCIDlBAqdTDeqDsEwkUqxJ9-lwDj4vcznLypEYRVu7hfBSu3rQq-yKHihKLa2Nz81DECt1M2c_4e_Jgwz0znQ2cIvFeJUylZrPHdox93bAHgpZTQDfaSt6FytyZp4tcS0ODF_KwbxVONtgmyCUIfGV3EMa0pnFXwBwJgQHMPEKm5fQ1TPzkep7p-gvpqTSH-7QITR-fFYtse8myocS5dR8f75z7DFWpQPvisURp1UA7K7H3wQYvbtzXh1gAGM2RfWIKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f793f615.mp4?token=MW-PZfV_gGbL1b7VaxSETmgLkvhhRyTdXjTOeH-WiEAPz7vtEOyqNOulldmxzh1R8MtDkiKxApgvqcKwVOCIDlBAqdTDeqDsEwkUqxJ9-lwDj4vcznLypEYRVu7hfBSu3rQq-yKHihKLa2Nz81DECt1M2c_4e_Jgwz0znQ2cIvFeJUylZrPHdox93bAHgpZTQDfaSt6FytyZp4tcS0ODF_KwbxVONtgmyCUIfGV3EMa0pnFXwBwJgQHMPEKm5fQ1TPzkep7p-gvpqTSH-7QITR-fFYtse8myocS5dR8f75z7DFWpQPvisURp1UA7K7H3wQYvbtzXh1gAGM2RfWIKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت وزیر خزانه‌داری آمریکا:
می‌خواهم از اتحادیه اروپا و بانک مرکزی اروپا به خاطر بیانیه قوی‌شان در حمایت از اقدامات اقتصادی ما علیه رژیم ایران تشکر کنم.
و این گروه با هم، به این حکومت وحشتناک چهل‌وهفت‌ساله آن‌ها پایان خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/70873" target="_blank">📅 17:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70872">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0baed51151.mp4?token=BhnEobZvrVNR4_wpZ_vAu5ND6bsKSCjSEzbCErigIQH1GCHOkf3XWJuqKJAkBH0-Gw0LV8p_SC4XmoUPELe14HWLbp7ehjrwt0QWziz2zr8LCRY-m_4t4jq63UorEqBW4iSsEPIvmLi6TAU813QToGt2ueLJ25Ytmw_P299urL1mcGZp1peuS8foF0EW7y5BMbsWU3Xgy_woc4pwcP7Za9b_cJID3RpvdiTulF8CQ_EXRNmBy83e5jcDLhuCWG1jpCzL0Qq8LsmJgmEfApSvMR_OQ42LKC9i4wFq9FshhYano4TXVCYfvvWw8FJL81Ujel_5y_9COlzibFlHiYnJig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0baed51151.mp4?token=BhnEobZvrVNR4_wpZ_vAu5ND6bsKSCjSEzbCErigIQH1GCHOkf3XWJuqKJAkBH0-Gw0LV8p_SC4XmoUPELe14HWLbp7ehjrwt0QWziz2zr8LCRY-m_4t4jq63UorEqBW4iSsEPIvmLi6TAU813QToGt2ueLJ25Ytmw_P299urL1mcGZp1peuS8foF0EW7y5BMbsWU3Xgy_woc4pwcP7Za9b_cJID3RpvdiTulF8CQ_EXRNmBy83e5jcDLhuCWG1jpCzL0Qq8LsmJgmEfApSvMR_OQ42LKC9i4wFq9FshhYano4TXVCYfvvWw8FJL81Ujel_5y_9COlzibFlHiYnJig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس‌نیوز به نقل از ترامپ:
همین الان با رئیس‌جمهور ترامپ صحبت کردم؛ او به فاکس‌نیوز گفت که ایالات متحده به حمله ایران به نیروهای آمریکایی در اردن — که دیشب رخ داد — پاسخ خواهد داد.
رئیس‌جمهور گفت: «ما ضربه سختی به آن‌ها خواهیم زد. پاسخی در کار خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/70872" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70871">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puq4Sy8Obe_gPR842Y40_eKzhnCqPViJplqZVjYAEmiXA-c1WTVp2ljft75JOvbaMDqlHe0PSvcRUvW7dsBieNmIHXWD6HdLq2gd5kL2YKma1uFr7QdnWex9vJe-4Qh95re62N5P7jZf1Z6jsOvFDzqtiJaOqBmeVfA242w_JMMltkxQ1hmT3JvSqxEEAQmHQbkWb3mlWNCcwaoLInPoaS76FgQMwHO51fZKml72IUa4ZNS7dPqjdyX3WeEuLPLeGgylKbNNJOLnw1ZwA6s7EnLEpITh-WQdUxU1Cyy46rrntkcfYU7W5cf4X1pZpMpeDhgqEGvNBd55hU0HoLyzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:ایران رسماً یک کشور شکست‌خورده است. کارش تمام است!
آن‌ها نه نیروی دریایی دارند، نه نیروی هوایی و نه پول ملی؛ حقوق سربازان یا نیروهای پلیس خود را نمی‌پردازند، نرخ تورم به ۳۰۰ درصد رسیده و رهبری‌شان دچار آشفتگی کامل است و توانایی نمایندگی شایسته کشور را ندارد.
تنها چیزی که دارند «اخبار جعلی» (از سوی آمریکا)، تمایل به کشتار معترضانشان (که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است؛ آن‌ها باید به جرم جنایات جنگی علیه بشریت محاکمه شوند!) و البته ردیفی از «چرندیات» است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/70871" target="_blank">📅 17:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70870">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا بدونید شما اگه عاشق ترین فرد دنیام باشی بعد از حدود دوسال هیجان رابطتتون میاد پایین بعد از رابطتتون تکلیف مشخص میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/70870" target="_blank">📅 17:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70869">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=luMTin1h13fPjuAk9CymWRxobqFvGxwWrE99DsmS-Lq5fEF2Jtmt7cIYpN-41XIjN3yHQBdGNXN3-dS5YrZM2q0L7OQp4hiu_YIjX_MW-Py1mthE7SCZ1COYgq6HkWbTox-6cp2wV0bLHV5rsAs5iNHidnKYYPx2jkxxOD7hKdsO7DiMmQVsrjwBycRkd13IUEM1EBakul1kRdbNwgr2TFz51tAjTZ2h_fot6IYShGX7_uMX-x9gtsHtW4IMij21LHZqrVd3glgyLRZhEKbwa09rJ-4qGvJq8xqvucSHgaJinNdMu-7LKQ-rEDkfOhrPM5wr9UphukLEXrKINlQOnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=luMTin1h13fPjuAk9CymWRxobqFvGxwWrE99DsmS-Lq5fEF2Jtmt7cIYpN-41XIjN3yHQBdGNXN3-dS5YrZM2q0L7OQp4hiu_YIjX_MW-Py1mthE7SCZ1COYgq6HkWbTox-6cp2wV0bLHV5rsAs5iNHidnKYYPx2jkxxOD7hKdsO7DiMmQVsrjwBycRkd13IUEM1EBakul1kRdbNwgr2TFz51tAjTZ2h_fot6IYShGX7_uMX-x9gtsHtW4IMij21LHZqrVd3glgyLRZhEKbwa09rJ-4qGvJq8xqvucSHgaJinNdMu-7LKQ-rEDkfOhrPM5wr9UphukLEXrKINlQOnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کاظم غریب‌آبادی، معاون وزیر امور خارجه:
این اقدامات تجاوزکارانه با پاسخی مناسب مواجه خواهد شد.
حضور بیگانگان باید از این منطقه حذف شود و آن‌ها باید درس‌های جدی بیاموزند تا دیگر دست به تجاوز علیه کشور ما نزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/70869" target="_blank">📅 16:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70868">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=Ce0hUCkJEBrenMu6mULfUkuV2Vd9qpy_EFqsj_xUTmTdVxgytHubDlx024EEgf0g5J9hnhpP-sZxZ-R4VLcHJQf1PvL-mXg4dTWXQ-bVLZzCaDYg9Fome5kuerQCcTY99zcNBJ6L8TmLSU2iDYtZIQAMTQ6KmLYbKtvbSY8yOpFy8qeWKi9_TcdOTOanL4FF984ewzAaNzmrEN_NI7oYmofZHAUqNrR0mDF_oyt4IUQZXKuNDtQDyDxlrNUMA8m_VO3xXsLBJp-2kSGvhrikraXYs-c-d6rMrr0ANqons4wxeSRPijq5Tstcjha8HfPRCw3VOHWYYnz7tfVeoktG_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=Ce0hUCkJEBrenMu6mULfUkuV2Vd9qpy_EFqsj_xUTmTdVxgytHubDlx024EEgf0g5J9hnhpP-sZxZ-R4VLcHJQf1PvL-mXg4dTWXQ-bVLZzCaDYg9Fome5kuerQCcTY99zcNBJ6L8TmLSU2iDYtZIQAMTQ6KmLYbKtvbSY8yOpFy8qeWKi9_TcdOTOanL4FF984ewzAaNzmrEN_NI7oYmofZHAUqNrR0mDF_oyt4IUQZXKuNDtQDyDxlrNUMA8m_VO3xXsLBJp-2kSGvhrikraXYs-c-d6rMrr0ANqons4wxeSRPijq5Tstcjha8HfPRCw3VOHWYYnz7tfVeoktG_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین شهر مراغه رفتن سر چاه فاضلاب میگن با یاد رهبر شهید پروژه رو افتتاح میکنیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/70868" target="_blank">📅 16:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70867">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUoTZ2ZYFej4Nn5RJfcqkHlI7ZFnR4FC0TRi6UVLJG2Ug0V3WmejJIxoOlbcDXDrGA4vgQwikuFgQEVwLkH8_gfg0qEPppZO1uUOv9n5aW2dYLWGBmClTQnASrYWehcM9hZtMzqmj2BTqIm-chwiNJ3ZDajs63NC4sXovwwFtu1fmJk5MLhrFD5TJ87JUJeg-2WJAj5mpCt10BDJS3EBeLJjQ2cREyK45Dh-p_2I1UfD-0VeYdFhY5BU53CRvsy1h7ytaCEUBTmzLP9kXX3BhqzGMbxAEbKxsMFfFkXVxU-AG2b-S9tv9X1AFyKWOdTiuaFBZuovOCIFpO3Tel_Y0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی:
نتانیاهو به زبان عبری آشکارا می‌بالد که چگونه دولت آمریکا را فریب داده و به نفع اسرائیل، آن را به جنگ با ایران کشانده است.
او صراحتاً و با خنده از این می‌گوید که چگونه با اختصاص ۱۰۰۰ ساعت زمان پخش در شبکه‌های آمریکایی، بر آمریکا «تأثیر» گذاشته است.
اما به زبان انگلیسی، از رهبری رئیس‌جمهور آمریکا تمجید می‌کند.
مار خوش‌خط‌ و خال.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70867" target="_blank">📅 15:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70866">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=r9r3gXl0Yfues-TOyCfm0bL18bNLO-E7sI6VZXvGEzKULQyjcinIxS4UGDKcdII7ruw9VXWG2WYDzszpeU7KLWhvq1QgBEkvZtRionnAhiNKsdyqac2e_JFr7R0iBdw1-p-d4apgeE8jEzHT4hHWdWnhYN61fgSN0S7qyN7fmZ-mnxvzAmWedXRU4i8hvswkA3XqfCKtl9YCwJlYUMBRyDlzRT-Q8-bJloezplIIAgtOMMgOuNCS9IrsniTJEO4OKRlQAmFzv6Y1qO3ol4aGK0pHfbpiKuvOlSM2BseiuQftBuKWKwOSxCpzAUBtLoxEgixjAKzP3TTTyUBFS_p5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=r9r3gXl0Yfues-TOyCfm0bL18bNLO-E7sI6VZXvGEzKULQyjcinIxS4UGDKcdII7ruw9VXWG2WYDzszpeU7KLWhvq1QgBEkvZtRionnAhiNKsdyqac2e_JFr7R0iBdw1-p-d4apgeE8jEzHT4hHWdWnhYN61fgSN0S7qyN7fmZ-mnxvzAmWedXRU4i8hvswkA3XqfCKtl9YCwJlYUMBRyDlzRT-Q8-bJloezplIIAgtOMMgOuNCS9IrsniTJEO4OKRlQAmFzv6Y1qO3ol4aGK0pHfbpiKuvOlSM2BseiuQftBuKWKwOSxCpzAUBtLoxEgixjAKzP3TTTyUBFS_p5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه وایرال شده از صداوسیما:
یه نفرو آوردن برای مصاحبه؛ بعد خود مجریه فکر‌ میکنه صداش نمیره تو میکرفون؛ به اون میگه اینا رو بگو اونم همونا رو تکرار میکنه
😂
آخرشم میگه دم غیرتت گرم به‌به چه شیرزنی بود
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70866" target="_blank">📅 15:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70864">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=uSQS0XWSmzWU-vypK6ZxPAtUlcvULBokWwUDwEUKc4SaAgbmxziriTDy66PsiVoVUFZQJ9qPmHue69dVe_ruWktvlX_OzNeIP-YZYUUmICuP7MZVFG6vXVVqH9uE71OUt5YFkSqj6Vr2FFKFfXCz_DG15bfOqJUs561e3R-baq4tELTsDdk95QNwJnOnKki6lmgHrnLG1B_CPTbRvxzfPAv7Fl_siIgXKAxuO6SAlHMIJ9FXg4Ik7dGl0Gv10WF14qerH1SF5Q6q2GqPKpIVEiaAt1jgd5_0-v4uvBMJfFA9CbpSjj87WvHmgQ6L7EM0hIZU_fvkpGWEsDna41L03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=uSQS0XWSmzWU-vypK6ZxPAtUlcvULBokWwUDwEUKc4SaAgbmxziriTDy66PsiVoVUFZQJ9qPmHue69dVe_ruWktvlX_OzNeIP-YZYUUmICuP7MZVFG6vXVVqH9uE71OUt5YFkSqj6Vr2FFKFfXCz_DG15bfOqJUs561e3R-baq4tELTsDdk95QNwJnOnKki6lmgHrnLG1B_CPTbRvxzfPAv7Fl_siIgXKAxuO6SAlHMIJ9FXg4Ik7dGl0Gv10WF14qerH1SF5Q6q2GqPKpIVEiaAt1jgd5_0-v4uvBMJfFA9CbpSjj87WvHmgQ6L7EM0hIZU_fvkpGWEsDna41L03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حواستون به دوربین مخفی توی ویلاها و اقامتگاه‌های اجاره‌ای باشه!
موارد واقعی از جاسازی دوربین مخفی داخل وسایل معمولی مثل ساعت، شارژر، دتکتور دود و حتی گیرنده‌ها و وسایل کنار تلویزیون گزارش شده.
پس وقتی جایی رو اجاره می‌کنید، مخصوصاً اتاق خواب و فضاهای خصوصی، یه نگاه به وسایلی بندازید که مستقیم به سمتتون قرار گرفتن. سوراخ خیلی ریز یا لنز غیرعادی روی یه وسیله می‌تونه ارزش بررسی داشته باشه.
البته اینکه «جدیداً بعضی ویلا‌دارهای ایران داخل رسیور ماهواره دوربین می‌ذارن» رو نمی‌شه به‌عنوان یک اتفاق فراگیر و تأییدشده گفت؛ امکان و نمونه چنین کاری وجود داره، ولی تعمیمش درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70864" target="_blank">📅 14:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70863">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=BEyPkiI-vGkA0HTEj9Mp_NQ2cjWI2Pwi-32ES9pucXcZXNPqPwd1Ms5Z82eVj6V7p6tAknx0hWRyPorL7zxfJIAfKAv2cTXOgH5_VvFCk21ifmGXYaUsaPl4ZfGOfn8nja0j0xaiCkosobKfilXF4ZcRrhn2kXs2dvcKWyK59A4o2XqdF9DlREyJUeDWXRJKhmjRSxycTlSbL5Q0EsZX32rru9STB1GiZQJB7kBi5zOSaFdN7ju9lZuRceARLIWu1foX1Z6m_1_MTqlOWVQR_WM_XmEjC7po3ktJjPhD5EADqGGxfRw7MvHDAUt-39Gd58r5zvRc7r5uj_EUfMKKZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=BEyPkiI-vGkA0HTEj9Mp_NQ2cjWI2Pwi-32ES9pucXcZXNPqPwd1Ms5Z82eVj6V7p6tAknx0hWRyPorL7zxfJIAfKAv2cTXOgH5_VvFCk21ifmGXYaUsaPl4ZfGOfn8nja0j0xaiCkosobKfilXF4ZcRrhn2kXs2dvcKWyK59A4o2XqdF9DlREyJUeDWXRJKhmjRSxycTlSbL5Q0EsZX32rru9STB1GiZQJB7kBi5zOSaFdN7ju9lZuRceARLIWu1foX1Z6m_1_MTqlOWVQR_WM_XmEjC7po3ktJjPhD5EADqGGxfRw7MvHDAUt-39Gd58r5zvRc7r5uj_EUfMKKZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
پست جدید اسرائیل به فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70863" target="_blank">📅 13:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70862">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K14LfXfXcwrMxX3inPHXYSaoRhvtPYyNC2lreEVGXbGM1SouODDp2UB4JFWjkFHo1qXv0eYJLrFq3ICFjlldwKiQzj4BB4BDz7k6XLsI9Z91Du07IcVjOYhKg2s1gcfIjfbQBfZt9U3CGnbmqWXYoRZ89OiZZQrVQNRIl2VPSnp622LjfsE6nuMmpqG8jxYh7AKLEezv_PEDlJ19nR8hZsS55bmRWxky5o3tkZMj4OBQN0908aiyfeJWPC-ZhXEB3swt4PSR3hOTwfUT19N94Ii7Eju_0a91nd7O7-YLm5c9bywB1ZAYyT2RbWTHtKGgw50qnPQUZkOGPoy8JNLd4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت، وزیر خزانه‌داری آمریکا، به خبرگزاری آسوشیتدپرس گفت که دولت ترامپ قصد دارد در راستای کارزار خود برای قطع دسترسی ایران به نظام مالی بین‌المللی، در هفته جاری یک بانک دیگر را تحریم کند.
بسنت اظهار داشت که واشنگتن به کشورهایی که همچنان با ایران مراودات تجاری دارند فشار خواهد آورد تا روابط مالی خود را قطع کنند، وگرنه با اقدامات تلافی‌جویانه آمریکا مواجه خواهند شد؛ او در این باره هشدار داد: «اگر ناچار شویم، این کار به مثابه خشونت مالی خواهد بود.»
انتظار می‌رود بسنت این موضوع را در جریان نشست‌های گروه ۲۰ در «اشویل» — از جمله در گفتگو با مقامات چینی — پیگیری کند. وی تأکید کرد که در خصوص اعمال تحریم علیه پکن به دلیل ادامه تعاملاتش با ایران، «همه گزینه‌ها روی میز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70862" target="_blank">📅 13:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70861">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=C5GoXr_SPnr5x5182slF-fmZBKQdog_X6TxbLS69AnsEvnVB1FI4HWqEtHH7gljUWNPqM_6beBcZ8oRohOUYuDTn_wc-q0e6n6nPemhprfKjTLLIFh69WFjMc3GDOLgiaCQqLdkqlNTV5lpKNCt-vQq_wpjYKKq-wUV6ktCoydYs03MezARNz2oGkCPVM-K6sBVER-4RxEJYZ25hhy4eKHWvTKnWdD7xpIR3lvKn9ZR-VDHVmlK4gm6GM80XlNsxLCxHDeF0RjSHLyFb3kal3z2pIxgqX23Fa7YARfMMfWKEOXEddGO3nrkE8mmWoDxSYGFoXRQ0_CiDgMl3mo-CpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=C5GoXr_SPnr5x5182slF-fmZBKQdog_X6TxbLS69AnsEvnVB1FI4HWqEtHH7gljUWNPqM_6beBcZ8oRohOUYuDTn_wc-q0e6n6nPemhprfKjTLLIFh69WFjMc3GDOLgiaCQqLdkqlNTV5lpKNCt-vQq_wpjYKKq-wUV6ktCoydYs03MezARNz2oGkCPVM-K6sBVER-4RxEJYZ25hhy4eKHWvTKnWdD7xpIR3lvKn9ZR-VDHVmlK4gm6GM80XlNsxLCxHDeF0RjSHLyFb3kal3z2pIxgqX23Fa7YARfMMfWKEOXEddGO3nrkE8mmWoDxSYGFoXRQ0_CiDgMl3mo-CpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇺🇸
ترامپ با هوش مصنوعی جزیره خارک رو نابود کرد.
جزیره خارگ دارد به تلی از خاکستر و آوار تبدیل می‌شود!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70861" target="_blank">📅 12:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70859">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=qnvHGszSqmNt9zXH-wWuZtH3y2mSYE5PqRkkfOF-DxDe_9YV6wEDEzzK7WXDDBIM10U1WhEtQMZfqwnAhmoI8c1bPHPZLeZyQf4kPIhRVNumAT1EJExvBjVpkWqiUDvVR37qkY3jEGheo85AQlwaBhQQlqzfVg3cf0oOGMHoBZ1wBgsi58sGG0gvpH7EbJz8hDi1x3_LxzRnn__r30WijwWRPeXfWsIHFhyvU8E7NsHPWF6eiFKrClQrHX2p4U7FDTBphDavzKd16EM1W4I0NMtX6ciZGlERQND6UrCZBdJbwzfqYxiQ3tZ5EzcdSJpeY5sQxkFAmwfnrnY9NYgZwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=qnvHGszSqmNt9zXH-wWuZtH3y2mSYE5PqRkkfOF-DxDe_9YV6wEDEzzK7WXDDBIM10U1WhEtQMZfqwnAhmoI8c1bPHPZLeZyQf4kPIhRVNumAT1EJExvBjVpkWqiUDvVR37qkY3jEGheo85AQlwaBhQQlqzfVg3cf0oOGMHoBZ1wBgsi58sGG0gvpH7EbJz8hDi1x3_LxzRnn__r30WijwWRPeXfWsIHFhyvU8E7NsHPWF6eiFKrClQrHX2p4U7FDTBphDavzKd16EM1W4I0NMtX6ciZGlERQND6UrCZBdJbwzfqYxiQ3tZ5EzcdSJpeY5sQxkFAmwfnrnY9NYgZwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آزاده اخلاقی همسر محسن نامجو:
بی‌ناموس تو که چهارتا ورقه گرفتی دستت گفتی دارم میرم همین سرکوچه تو آمریکا پرینت بگیرم، تو فرودگاه امام چیکار میکنی؟ چرا چمدون من رو اصلا بردی؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70859" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70858">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70858" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70858" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70857">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKrnFogNmbedFjbrtDR73zOHWi3J1F_8jbozpIqJ6oUVEmiuFrZtmGHErDhhcdVDkLLkgE7V7Qk_NlIwq-36wVn4XdmTdBB6pHvnHcr9-eeZzu11a98piLkLLGR0W2XBBQO-r0aGLuEeZkxJ6LjYze-gHMIA5fyqwTbIxoBmwLsx_Yqv9Q61U4aCD0L7cvs2_5MVQUCW1M_fplJRW5YqEFKZKNHciCL4prilbeHuicba5kQGav7qnAzqqnDa7sJ30MBiMRJznnWlWTro-vezOEKJfid10kWc--4Oc7uKnusl7tNH-JgxV6XV02N_MjGOzSP058EaekB3J-xfUcKNeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آرسنال
🆚
استون ویلا
رایو وایکانو
🆚
لیدز یونایتد
رم
🆚
لچه
بولونیا
🆚
آتالانتا
ختافه
🆚
اوساسونا
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70857" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70856">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=g7ii0e5HdcMgTcoTl0HsJ-b8Aipa2uX7QCLohtwyJYBZ3uMAEplRs_4jAWJCJsiZEnOjuPMqu9JV867z_nhC5LMYUTzL23YlMWvVF1va1MOwUFSXKDrMYfzPQlJqoHo_o1nfYh9MBn6zYZCMRXeZJAZIa_4sAp9cIbZboVFZ7qOywdrMt5gI2ob4R533rk0Zh-IsLJIeqE2LT9uMIniHG6TFGXZXuSrY2EVJJFNN4Iinia8NT9IyhVUns2WnE7JRuMCwOrmKTJp6hTuOG-h5rR9KH-qlzal8rSkALAIEDol6rWv84NgHwWInOJY6KYnfstCReLSIBdC_TRiMarGykQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=g7ii0e5HdcMgTcoTl0HsJ-b8Aipa2uX7QCLohtwyJYBZ3uMAEplRs_4jAWJCJsiZEnOjuPMqu9JV867z_nhC5LMYUTzL23YlMWvVF1va1MOwUFSXKDrMYfzPQlJqoHo_o1nfYh9MBn6zYZCMRXeZJAZIa_4sAp9cIbZboVFZ7qOywdrMt5gI2ob4R533rk0Zh-IsLJIeqE2LT9uMIniHG6TFGXZXuSrY2EVJJFNN4Iinia8NT9IyhVUns2WnE7JRuMCwOrmKTJp6hTuOG-h5rR9KH-qlzal8rSkALAIEDol6rWv84NgHwWInOJY6KYnfstCReLSIBdC_TRiMarGykQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای ایشون که داره وایرال میشه:
با این شرایطِ گرونی، هیچ دلیلی نداره که شما به دختر مردم غذای مفتی بدی.
اصلا به حرف کساییم که میگن مردایی که پول میگیرن پرنسسن و لَنگن گوش ندین.
خیلی از دخترا بخاطر اینکه حوصلشون سر میره با شما میان بیرون و یه غذا میخورن، پس دنگتونو بگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70856" target="_blank">📅 11:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70855">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=F2mR47k_Yc9rqhasQI-JABVAzpIaGOtxq0Vi4E6_Cm2050TPwp0HoCz34B4sGN6gN564NlcMpX_QKhF0uHiZMaQvY_LBXDjWLfElVnpICAmKjl_worFjiiLAZdUWsM9cRutfzXtBMQr6TcdpXOuMRNT_UCthuK9dxif4qvXMDMPoin6JqvVcYvcRgB1rFsXLk_Dx_nUzc-sF2MlRlkwcJmfSGGj5I6MCu_5JfoQmegqWpDP1X30HO9vV2st2D2WmFj3zARwG1E6MM-YTq0xyBNpRw4yor9AtypRNGCjVaeEpqgY2s25Z3FzP8P92zzIde1WsABuGwsmCzxYDX65KaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=F2mR47k_Yc9rqhasQI-JABVAzpIaGOtxq0Vi4E6_Cm2050TPwp0HoCz34B4sGN6gN564NlcMpX_QKhF0uHiZMaQvY_LBXDjWLfElVnpICAmKjl_worFjiiLAZdUWsM9cRutfzXtBMQr6TcdpXOuMRNT_UCthuK9dxif4qvXMDMPoin6JqvVcYvcRgB1rFsXLk_Dx_nUzc-sF2MlRlkwcJmfSGGj5I6MCu_5JfoQmegqWpDP1X30HO9vV2st2D2WmFj3zARwG1E6MM-YTq0xyBNpRw4yor9AtypRNGCjVaeEpqgY2s25Z3FzP8P92zzIde1WsABuGwsmCzxYDX65KaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وایرال شده از طرفدار حکومت با پوششی جالب که میگه:
آقا فکر کنید شعب ابی طالب هستیم و محاصره مون کردن
این محاصره از شعب ابی طالب سخت تر نیست که
ما مذاکره نداریم و آمریکا هیچ غلطی نمیتونه بکنه
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70855" target="_blank">📅 11:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70854">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=VVDoUQ4_kPe0M6R9_6Q5M8ub17qGxMv3tnLZhs4Lp4fIjzL81BN76PCTMG-zIzieYBrnSVWYKBg5jZB1BSO_pmRps3meEKmjXq2iwr45tEY3W1iw0CINYXZtaH9MJdEcT5IzEDbB7G3Jacbofd6rXRCDpMQoiAtYRjk3hegRdYr9H7YTsgefK_vdikEFQrK8FmGjpi1V_1N6oKn2t0TGx-DzfKu5YmY7cx1ywJdqPMRgiuQ83e6lVbZ4ZGITsBxOIW56tuL7nymKLVbKDyERSGkXAgG3f4nzKpFsC0J_kZkOLF57rrL4XCDrEKu-g4jfburPc4FOpnBZNpVKhPOoZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=VVDoUQ4_kPe0M6R9_6Q5M8ub17qGxMv3tnLZhs4Lp4fIjzL81BN76PCTMG-zIzieYBrnSVWYKBg5jZB1BSO_pmRps3meEKmjXq2iwr45tEY3W1iw0CINYXZtaH9MJdEcT5IzEDbB7G3Jacbofd6rXRCDpMQoiAtYRjk3hegRdYr9H7YTsgefK_vdikEFQrK8FmGjpi1V_1N6oKn2t0TGx-DzfKu5YmY7cx1ywJdqPMRgiuQ83e6lVbZ4ZGITsBxOIW56tuL7nymKLVbKDyERSGkXAgG3f4nzKpFsC0J_kZkOLF57rrL4XCDrEKu-g4jfburPc4FOpnBZNpVKhPOoZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
رهبرانشان از میان رفته‌اند.
تمام... خب، تمام تجهیزات ضدهوایی‌شان، منظورم این است که همگی نابود شده‌اند.
آن‌ها آدم‌های سرسختی هستند؛ آدم‌های باهوشی هستند. اما... خب، بسیار شرورند.
تا سه ماه پیش، پنجاه و دو هزار معترض را کشتند و متأسفانه، شمار بسیار زیادی را هم به آن فهرست افزوده‌اند. حتی سراغ کسانی که معترض هم نیستند می‌روند؛ به خانه‌هایشان هجوم می‌برند، آن‌ها را با خود می‌برند و به ضرب گلوله می‌کشند.
خب، این‌ها آدم‌هایی بسیار خشن و شرور هستند و اگر سلاح هسته‌ای در اختیار داشتند، اسرائیل نابود می‌شد.
اگر من رئیس‌جمهور نبودم، اسرائیل از بین رفته بود. دیگر اسرائیلی وجود نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70854" target="_blank">📅 10:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70853">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPfCcYgEIRcYtrizk69Z59gzpaOL8ODf1LTb7ZHpkrK5LiBgZ7JmiFr5o6MdJUdxGTDaAK58TI0yI21kX13lBooOVB0ILZudMgdtne4JCgTPYQlcmgNpGXQVfYLFfhpaEphXgSJqnJ7xbP-VmWQgMaD1947xBfz9oiMxQu738ppSLxgyQXCiQztfxlTF0Gs_SHV-H8YCHaWKmYkde9raXXUcyc_eD8H9N4JTL0R_jSX10uLxL6nzzCBKeIKQkfY4obDa9tvX7nHh6s8iAiBjfeltJliAr6-KGsZjD0ZmzHvI0fHFbe_CliipjHX6lUBFA979HwwAXvdmv7f3T9gkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
〰️
سنتکام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران در بیانیه‌ای اخیر مدعی شد که حملات نیروهای آمریکایی برای جلوگیری از مین‌گذاری سپاه در تنگه هرمز، «اقدامی تجاوزکارانه» بوده است. این ادعا کاملاً نادرست است.
✔️
واقعیت: نیروهای آمریکایی علیه یگان‌های مین‌گذار سپاه که در تنگه هرمز تهدیدی قریب‌الوقوع ایجاد کرده بودند، دست به اقدامی محدود و دقیق زدند. در واقع، ایران عامل ایجاد این تهدید بود و ارتش ایالات متحده برای حفاظت از دریانوردان غیرنظامی، کشتی‌های تجاری و جریان آزاد تجارت جهانی، آن تهدید را خنثی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70853" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70852">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=tXyfa9OggyhEcfN5dIVThs-i1IpR6d25tKuUbg2bFDfx8mf--L4yl8icmsTA5OTQIJOQjZtq0TlDhJkku1_cLhTqkhe8tBzOs6oAJYiGr4KUAlrzOG8rUXaPgWrXdiJ3tX6XIty7fJUT5cM-PeL-kzOB90dkpoGx9NcnMurnhq82enliwN6JOtZ39s5joY0EV0_FPrRDElELEWR0MHOb8q7SBnpnuVdsCn6Rwys5DqdBKMcOlaIKQXPFz96HtC88JU8D1XnkgD5kkmd68FFauKiit0cpCd9gYl-pttdNJnE5qqvCDTTlpFXsg8qgpJ_XesuXlEt_crR9R--ucNBIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=tXyfa9OggyhEcfN5dIVThs-i1IpR6d25tKuUbg2bFDfx8mf--L4yl8icmsTA5OTQIJOQjZtq0TlDhJkku1_cLhTqkhe8tBzOs6oAJYiGr4KUAlrzOG8rUXaPgWrXdiJ3tX6XIty7fJUT5cM-PeL-kzOB90dkpoGx9NcnMurnhq82enliwN6JOtZ39s5joY0EV0_FPrRDElELEWR0MHOb8q7SBnpnuVdsCn6Rwys5DqdBKMcOlaIKQXPFz96HtC88JU8D1XnkgD5kkmd68FFauKiit0cpCd9gYl-pttdNJnE5qqvCDTTlpFXsg8qgpJ_XesuXlEt_crR9R--ucNBIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سرهنگ خلبان بهمن فرقانی، جانشین فرمانده پایگاه چهارم شکاری دزفول :
زمان جنگ، آخوند رسول منتجب‌نیا به پایگاه ما آمد و پیشنهاد داد برای بستن تنگه هرمز، فاصله عمان تا ساحل ایران را با قایق‌های موتوری با طناب به هم دیگه ببندیم تا عرض تنگه بسته بشه
به ریشش خندیدم و گفتم: «چرا مزخرف می‌گویی؟»
زیرآبم را زد و از نیروی هوایی اخراجم کرد!"
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70852" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70851">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=rogiElkYfFCoTBZXpgg7XafJ6wxuLxQaubkAff1IhWh8XLlpTuvO2f7GHgHlNnUIHiLvYIyqTKH22MpL-_JhLZxkSTaCAgphYuruwRjTu-cUyOJPLfmo8zGcuYsOKIDOloN9SGYiocEd4Su_NYfOpksx3SJmGGv1nAho0yMOiTgWy8YIYZ6_6F1mQZbckluttgvnwDaJr8gqCe8iCMq9J5JicEIjHYMPB3hP4KPNdUB_EeerhJahbxfDhgF55ER4_CjKu65Kygobd-H8IWRvmE6C-pL4sny7m5wfRUPQRDasN2kdFty-0BnDjeJVorToPGVnSq3b6D0v843cSykELDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=rogiElkYfFCoTBZXpgg7XafJ6wxuLxQaubkAff1IhWh8XLlpTuvO2f7GHgHlNnUIHiLvYIyqTKH22MpL-_JhLZxkSTaCAgphYuruwRjTu-cUyOJPLfmo8zGcuYsOKIDOloN9SGYiocEd4Su_NYfOpksx3SJmGGv1nAho0yMOiTgWy8YIYZ6_6F1mQZbckluttgvnwDaJr8gqCe8iCMq9J5JicEIjHYMPB3hP4KPNdUB_EeerhJahbxfDhgF55ER4_CjKu65Kygobd-H8IWRvmE6C-pL4sny7m5wfRUPQRDasN2kdFty-0BnDjeJVorToPGVnSq3b6D0v843cSykELDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یک سرهنگ فراجا:
متأسفانه مدتی عده‌ای از مراجعه کنندگان و یا به تعبیری ارباب رجوع به ما مراجعه می‌کنند و در خصوص گرانی‌ها معترض‌اند و هر بار که به ما مراجعه فکر می‌کنند، فکر می‌کنند که مسبب و اینکه ما از دست ما کاری بر می‌آید و نمی‌توانیم برایشان انجام بدهیم.
آقایون مسئول، عزیزان مسئول، به خدا گرانی بیداد می‌کند. آقای برادر تعزیرات، آقای بازرسی کننده، آقای بازرس اتحادیه، به خدا با کت و شلوار اتو شده و موهای ژل زده و عینک دودی نمی‌توان با فساد مبارزه کرد.
آقا یه جای کارو درست کنید که یه جای دیگر را بخواهید گوش‌نظر بدید. تو رو به خدا، تو رو به هر کسی که می‌پرستید وضعیت معیشت مردم را درست کنید.
فکر می‌کنند به عنوان پلیس ما از جای دیگه درآمد داریم، از جای دیگه خرید می‌کنیم. به خدا این چنین نیست. ما هم مثل همه شماها از همین فروشگاه‌ها خرید می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70851" target="_blank">📅 09:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70850">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78504efb49.mp4?token=D0tqqYUv2OFx6J4u1GQttxPWHWcWlwa4iMYAH2JemX1uxmHUYEVszFt9T6t0erQduvH35pe67epwgEBYhokyE7kEKeGejSGOLnziZJcW2BHJ6e20snjLXBjLfhY7KIyeKhpGc3hG814aorGDxwqwhHVvnqezH8cteVNoHAnMizKwIpJKOaRP5ZZ1_keZgA7OnVFJ2tv-H5HLS83IDf1kEDeDpCupFZc1E-lOlCrFFdbzrGgNZ1HzUdg2pLlq68QyEtD3medw2U7h1iHU2Uqq-m_9kqV50cfG7F9EbGcbO8z0gUM1iDxBfpxKPPMlPpakzVcw4ibFl3qLxFc9g6-W5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78504efb49.mp4?token=D0tqqYUv2OFx6J4u1GQttxPWHWcWlwa4iMYAH2JemX1uxmHUYEVszFt9T6t0erQduvH35pe67epwgEBYhokyE7kEKeGejSGOLnziZJcW2BHJ6e20snjLXBjLfhY7KIyeKhpGc3hG814aorGDxwqwhHVvnqezH8cteVNoHAnMizKwIpJKOaRP5ZZ1_keZgA7OnVFJ2tv-H5HLS83IDf1kEDeDpCupFZc1E-lOlCrFFdbzrGgNZ1HzUdg2pLlq68QyEtD3medw2U7h1iHU2Uqq-m_9kqV50cfG7F9EbGcbO8z0gUM1iDxBfpxKPPMlPpakzVcw4ibFl3qLxFc9g6-W5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل به فارسی:
جمهوری اسلامی و سپاه پاسداران سال‌هاست که ثروت و منابع ملی ایران را صرف تروریسم و جنگ‌افروزی می‌کنند، در حالی که سهم مردم از این ثروت، ایستادن در صف‌های طولانی و بحران کمبود بنزین است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70850" target="_blank">📅 09:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70849">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70849" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70848">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC9f64ZE2kVVcnAq6jDHym69fh-jwbfABGU4qa8pWNXPPM6fpNv0FFFnaMuFe6BD8duzzfzonr-1cf2-OT-XAOWoDWrvJNpfMMfk3jB9xEMenryA0FmVfQgNIBEjXIuhhXOLSStRHtaKqziQTQ3aK2Zflm50MYf2cLDddHTyN8ODatZG9wP4hDSAfZ659JwihWOI43KjRTyXyLJ9544OQmL7GlJoKVeUw39qrfSobZkDEb0SOrXqxUVgk5f6l-y7RuBVhyo9duFQRnSHPxlfFD8RhOyq_e7c_8KhbCPVgl2lMhM7efojtugV5x1AuLNKO9kkl1PMQtnzMPI8cwbvYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70848" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70847">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
نایا:حملات موشکی به قطر.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70847" target="_blank">📅 01:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70846">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">یادآوری: علی خامنه‌ای، دیکتاتور و بزرگترین جلادِ وقتِ خاورمیانه در ساعت ۹:۳۰ دقیقه صبحِ ۹ اسفند ۱۴۰۴ توسط ارتش اسرائیل و آمریکا، تکه تکه و تجزیه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70846" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70845">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بچه ها بزارید منم این وسط یچیزیو یادآوری کنم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70845" target="_blank">📅 01:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70844">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr. NOBODY</strong></div>
<div class="tg-text">خواست پاتریوت رو با لهجله بیریتیش بگه اذیتش نکنین</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70844" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70843">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɴᴀᴢɪ</strong></div>
<div class="tg-text">امیر پهن مغز پتریوت چیه؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70843" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70842">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOYdN0jim4UElQedHAd9MblBgbMDHDC1Dfs_advetwBY8ykM971eRqNuBdSmMLGpPgP9iv4ZIYp_fgtlFcD5x4hpo_9HxqnX-jxQhnoWOGkOZkgN41rPBNOlJQMiCMpQzhGvt9M43MdK47me64J--fG4ufs0ysOTwQOCKQppcsZHnkiCxAwdG4lY4brQhN82xVGMChQF2LK6pPW02dYlDZy37SGWOOr2Fa4-t0N-gN92vUh4GUwJE7X8QiXB8Mgd-9hCd9bsAQVmFNGKZIg6hobHvSY_9LiReMDciMs23oyHV4gvqq3ST2TvBWUapnJAUGIzU5BaPO_lWzP8rRTmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا برخورد موشکی صورت نگرفته، اکثرا رهگیری شدن #hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70842" target="_blank">📅 01:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70841">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=pHlIIw8k4fYeTipU_MvEjri0Kh0OmTam3NvFo59Gv3gqZ25S0BHDi8e9_oysy0d_7alo8Ib055AmvuRU7MoCweoQn1riDLspsiqTJoHX0HQuICwmP2VBGQpOKTgagF9YB-x9tJh3li8IiY9FY3UQ81WosvNCPhJwW5eTUpX3IJLBHtuO9NH_mLY3nMyj4Y4NWETAgVzXPJw_WFwEJ0_zB5vueH03DnYGUI_yk1R30zVgnvUPDaZUgfM0sJKwOb_5xuLPbog094TMHBb5pux12-NWH5CCagMwsv4-pFIKzeDdLTHpt1BieLhHBW02VEMQUd8kJxvNBU7k2g9tSYoWDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=pHlIIw8k4fYeTipU_MvEjri0Kh0OmTam3NvFo59Gv3gqZ25S0BHDi8e9_oysy0d_7alo8Ib055AmvuRU7MoCweoQn1riDLspsiqTJoHX0HQuICwmP2VBGQpOKTgagF9YB-x9tJh3li8IiY9FY3UQ81WosvNCPhJwW5eTUpX3IJLBHtuO9NH_mLY3nMyj4Y4NWETAgVzXPJw_WFwEJ0_zB5vueH03DnYGUI_yk1R30zVgnvUPDaZUgfM0sJKwOb_5xuLPbog094TMHBb5pux12-NWH5CCagMwsv4-pFIKzeDdLTHpt1BieLhHBW02VEMQUd8kJxvNBU7k2g9tSYoWDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رهگیری دو موشک سپاه پاسداران بر فراز اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70841" target="_blank">📅 01:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70840">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن  @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70840" target="_blank">📅 01:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70839">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:  از خرم‌آباد صدای انفجار شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70839" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70838">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از خرم‌آباد صدای انفجار شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70838" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70837">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">صدای انفجار شدید تو خرم‌آباد شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70837" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70836">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44471a1938.mp4?token=bbgdHjxRH-90bqHnneR7d4l7q9ERKR4iel0RlvJVstebCjgSoQ_xGZGvSQPRT9ggksZ7WNT0A9shjtpY_z5Mii359BzKIk8SyPbA3HaR57UJTGlDLLPg8VUSKSgiW4o4eAsf9sBiMrzleDA9DUUz7Gjr31WIN6D3KJEYRKShPNuo4xH_gxiFaohVb0XA1ZaGl6zReK1Kgi6s0atE8cDJoni30w6xjUOC4wSihhg8wYKxhfrM9Y9Y50mZyP-1jwdJqm21OevyL0agcFmHfp7BaYykbP0t1yu58r0VuKwnO7wtBETWlBmHaM0Mp1jpRkYP2FK5brhFoSvWAMAo8QsgpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44471a1938.mp4?token=bbgdHjxRH-90bqHnneR7d4l7q9ERKR4iel0RlvJVstebCjgSoQ_xGZGvSQPRT9ggksZ7WNT0A9shjtpY_z5Mii359BzKIk8SyPbA3HaR57UJTGlDLLPg8VUSKSgiW4o4eAsf9sBiMrzleDA9DUUz7Gjr31WIN6D3KJEYRKShPNuo4xH_gxiFaohVb0XA1ZaGl6zReK1Kgi6s0atE8cDJoni30w6xjUOC4wSihhg8wYKxhfrM9Y9Y50mZyP-1jwdJqm21OevyL0agcFmHfp7BaYykbP0t1yu58r0VuKwnO7wtBETWlBmHaM0Mp1jpRkYP2FK5brhFoSvWAMAo8QsgpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70836" target="_blank">📅 01:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70835">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبر متوقف شدن پروازای فرودگاه مهرآباد هم فیکه #hjAly‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70835" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70834">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
منابع عربی:شنیده شدن صدای انفجار در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70834" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70833">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🔴
گزارش ها از شلیک موشک از نقاط مختلف کشور به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70833" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70832">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب  تلگرام یه‌پا شده روبیکا... #hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70832" target="_blank">📅 01:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70831">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-B3w8QP29Ay5uBkAw4iVAn-uw3Lf46DzibjbGqJ1RqjERD-S_eTVU6SibkIMAwUJekJGUhEkKkFvOxQA_EJXjOdxscKOTmkE-3dyykthywCEj2t5GHkWw95qZ-KSvNM08f3FmhcuE29T_YgYPDj6f1c6MHPbIvt7ssKsX9WaH1N6eeX7yXyHtg0QL7M9NoizvuZ-1Fdi82lR6sSRkdvHiHvrNrBiLj39Dlz2rnl1DmDMDoL1QEAuriY7Ma19sFujP7oFahBaRcyXgsgztTGToT-mojXJZlXsH4XTfDQzgD1fUndKiJJncpIEgEDL98GzWy9MUuFqfa0rOWZyeSKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70831" target="_blank">📅 01:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70830">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=obWvcKxaYwrZTyTuwWA8DTt04nT2GcnBXaBeMKz4oVO0mQDZuuMepw-Bpad8eGc8SSNUVxMlNWacZDwEmWRNBWypQ9whu1GncAMX3ORzov7GJE2F5GpRv3IuotFVF6G65iXhLhcW7pIBgHOEi82rAtEaCN_BFxC2XMne4BesMTnepi-F_hGPlV3s4ZHOxPbTKMB_YPmO77HpMFJST_iUYskNPuRiXE843BRVThy-LgEfO_g-l8atUiQn28QSRDE156YakjrowiGT3EsvZY2FCzv6j0fr0xLKeBJV4SYv0rAIQgLwgiqYeRPKs02ASmM6jII2_P4TC011S5Vtwe7p-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=obWvcKxaYwrZTyTuwWA8DTt04nT2GcnBXaBeMKz4oVO0mQDZuuMepw-Bpad8eGc8SSNUVxMlNWacZDwEmWRNBWypQ9whu1GncAMX3ORzov7GJE2F5GpRv3IuotFVF6G65iXhLhcW7pIBgHOEi82rAtEaCN_BFxC2XMne4BesMTnepi-F_hGPlV3s4ZHOxPbTKMB_YPmO77HpMFJST_iUYskNPuRiXE843BRVThy-LgEfO_g-l8atUiQn28QSRDE156YakjrowiGT3EsvZY2FCzv6j0fr0xLKeBJV4SYv0rAIQgLwgiqYeRPKs02ASmM6jII2_P4TC011S5Vtwe7p-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش ها از شلیک موشک از سایت موشکی بیدگنه
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70830" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70829">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب
تلگرام یه‌پا شده روبیکا...
#hjAly‌</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70829" target="_blank">📅 00:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70828">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDw-nn3cBZtthKFwoq3Y0lhivEeli4XoU7jK57i5PvOHabhjbDV5Jk_9QPoeBZj6rZvtzxHRa_SEq7-45U79qrHzjDTBLCnRi52EgFNvcezwphuShpIazBL9XOAzYOkVrigAGZkE0IFiYkO6pWRja4n4COeVE9fj5AcBODXSszSpU10okkgaxb135WLp4xL6uSQtwEI6Up5_Cb-GoFGftAbS9JwsP9XTQU1PzRp6Mj6Z-QoYoG2RnujQ01hdsDIOO5_bHGRi8pLp4qTrCY5XZ7RlX7OLWgOiOtPVZgqnORBJR4glt5Qh8p9MO6Rpa8mbNQv2lTlNS6RncE63hKWnOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
ابراهیم عزیزی:
یک بار دیگر اراده ما را بیازمایید و بهایی سنگین‌تر بپردازید.
انتقام در راه است؛
فقط فرار کنید!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70828" target="_blank">📅 00:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70827">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=KM1GH2q0gnOaWlkj-71aj6-Zo2MDcgdUcz5Q7oMAqsvLZtFu9lyu31jI_04UWnU-j4N5K_TlOQwRfRJso1w9Y7EPTBwyAE3J0IDOfy6TQQdgcIMIL2NQhng4y2MYA4GWPZuPAZs2InVCKiZ8_cGP04H5pwAdBM6NgVOARaM91zecSYxBoifrk5bvTtwvFlCxFCu-2X0ZvkfqIuDiCo2bnZ3aV3BbaRNnDzLlUz7-YdXq5GgFmbXN7tdee8injmKb3_XYypqba_VJaECceCeHDNsiGNyzWGaSXWJBeIN9M1ZwbPDbjtoSIXhaGfM0Lytf1lhqMWQB0_y-XxsoVyYjNjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=KM1GH2q0gnOaWlkj-71aj6-Zo2MDcgdUcz5Q7oMAqsvLZtFu9lyu31jI_04UWnU-j4N5K_TlOQwRfRJso1w9Y7EPTBwyAE3J0IDOfy6TQQdgcIMIL2NQhng4y2MYA4GWPZuPAZs2InVCKiZ8_cGP04H5pwAdBM6NgVOARaM91zecSYxBoifrk5bvTtwvFlCxFCu-2X0ZvkfqIuDiCo2bnZ3aV3BbaRNnDzLlUz7-YdXq5GgFmbXN7tdee8injmKb3_XYypqba_VJaECceCeHDNsiGNyzWGaSXWJBeIN9M1ZwbPDbjtoSIXhaGfM0Lytf1lhqMWQB0_y-XxsoVyYjNjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:
من این رژیم را به زانو درخواهم آورد. به این امر متعهد هستم. این کار شدنی است.
آن‌ها بسیار ضعیف‌تر از گذشته شده‌اند و در موقعیتی متزلزل قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70827" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70826">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
آن‌ها از برنامه هسته‌ای دست نکشیده‌اند. ما آن را به عقب راندیم، اما آن‌ها کاملاً قصد دارند برنامه هسته‌ای خود را برای تولید بمب‌های اتمی از سر بگیرند.
بنابراین، این تهدید از بین نرفته است. ما این سرطان، این غده سرطانی را ریشه‌کن کردیم. می‌دانید که اگر سرطان را ریشه‌کن نکنید، می‌میرید. این همان کاری بود که ما انجام دادیم.
اما سرطان ممکن است دچار متاستاز (گسترش) شود و در صورت بروز متاستاز، می‌تواند دوباره به تهدیدی تازه و بسیار جدی تبدیل گردد.
ایران می‌خواهد برنامه هسته‌ای خود را از سر بگیرد.
من پیش‌تر یک بار مانع این کار آن‌ها شدم و تا زمانی که نخست‌وزیر باشم، مانع انجام آن خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70826" target="_blank">📅 00:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70825">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngfDSc8aTlFFqSyEpv7JWFijTVVZITYsEYYUdPXu2A6EHlFXZdRtwj_m6WIGBwe9WRGEVccSrUIYlKPbIFWXX4fmBGfPzuewyriSvdR8Mg8n6N2II6IgggYnS4ASp74ddIApMJOIr1UqV_VGmsldVHQXfcxAs7QDsEuPbl6v55ThFgnPwi6tukYijKgcMmVrSWOGWrZHnRvgRoif_2yTtoJxjVXbiJ1py7PFHyLbscIm5mt5y0Bhj6mc2SsA15FQqv5sO-R4Goa22nQ7e0FjtmBgJMMelP9xWAGY5KdgMWVf_yPyLddJitKyfKjMMuh-zrFl5TtwRP_KOy5JlNDKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
سخنگوی سپاه پاسداران انقلاب اسلامی:
این اقدام، یک خطای راهبردی و مهلک از سوی دولت ترامپ در چارچوب جنگ اقتصادی است؛ اشتباهی که کفه ترازو را به زیان طراحان آن تغییر خواهد داد و هزینه‌های سنگینی در پی خواهد داشت.
دشمن پیامدهای این محاسبات نادرست را در هر دو عرصه اقتصادی و نظامی متحمل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70825" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70824">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
مجدد صدای انفجار در جزیره لارک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70824" target="_blank">📅 00:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70823">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری؛سپاه پاسداران:   تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد  @News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70823" target="_blank">📅 23:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70822">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛سپاه پاسداران:
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/70822" target="_blank">📅 23:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70820">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INFOo-MzkZduGKVcaRCyQPGdngScz9ccGFGjMHo3QXF402KY0RRHLr_v_WLeicSaelGmIqaC9RMdd6iHHRfgtJRny2JTcoQqs2jct8hAYytstaIM-IW56h8vTYePIogsQ3nOWobuYX1BaoP-VaMaIdtFjLzfns_Lba8sjkOXdjgJ7Ec6k0DknPXIatDPtFa2Fuk6DRSk0ERN0esi0UuDpttka9YxaBH4sIdHyTEfsKBZo93IRv7GwuzstA7Ab1h0tZCgKQrC-eBnvStPiQxtsEHb_G4CkpBCZ2_enM1qRTLNoEQu-xK7WVQAZbfeTOxVlvGSIiMJL-UUo3NP48Jpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d778b593.mp4?token=Dw3T-RASX2Yac0dOX1NBVzFrxojBjFBA3UTkZkNFcXkY9KODmGbPdme2CW9C94TeGDRLuPDCwyDmCdI_58cg2u8fdbI1FEn9JcN47jjxCtbl2WMHdChL5IOd1i8ZUlXImhjnCpZLgSxc1vWz09U6Wyi16Op_Gzh5mYFNgmGzVAZ914ZmQkkjUVl_qUkp_ZomWYzUCmFMeAo0D2j-Oj7KebVndrYxC3OZQ6IUsmGj_maOe4ZDQTyq_p6uULWV55VLJCr55ki7Ges8YyP3VzjoB0nq0HQ26clC1C9DIaflD391c5K5sNMPyzX2Cdp9gJolg_HiyBUA1xQyonEEYcvDrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d778b593.mp4?token=Dw3T-RASX2Yac0dOX1NBVzFrxojBjFBA3UTkZkNFcXkY9KODmGbPdme2CW9C94TeGDRLuPDCwyDmCdI_58cg2u8fdbI1FEn9JcN47jjxCtbl2WMHdChL5IOd1i8ZUlXImhjnCpZLgSxc1vWz09U6Wyi16Op_Gzh5mYFNgmGzVAZ914ZmQkkjUVl_qUkp_ZomWYzUCmFMeAo0D2j-Oj7KebVndrYxC3OZQ6IUsmGj_maOe4ZDQTyq_p6uULWV55VLJCr55ki7Ges8YyP3VzjoB0nq0HQ26clC1C9DIaflD391c5K5sNMPyzX2Cdp9gJolg_HiyBUA1xQyonEEYcvDrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
یه نمایشگاه عراقی اومده پژو پارس گذاشته برای فروش؛
و اما کامنت مردم همیشه در صحنه :))
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/70820" target="_blank">📅 23:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70819">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
#فووری؛ باراک راوید به نقل از مقام امریکایی: امریکا امروز به دو پرتابگر ایرانی در جزیره لارک حمله کرد  نیروهای سپاه پاسداران سعی داشتن موشک‌های حامل مین دریایی به تنگه هرمز شلیک کنند که قبل از پرتاب توسط امریکا منهدم شدن @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/70819" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70818">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/onzjeee3EXHNU7xWOy7WGvNUUoKjh8Wa6OWBm2ciAbea4C-D6u6rX1PSC782LiEnx1oGiwssgrZm9NGYRPLxEaOg2oeXgr9kKF4ce143xWzo8W0IQxXlDtCYka7qq6sZ5y9TeHWObK52QvUDASxhrH0fGeuYE8RMY8117X2WsRD9ceXOp8MRaMJA4V7NvPN5-1EMWfV1IrmdQ0aOrIFaugpUslldKSyTmbjpOrML6lqX-qIyyxBR7jsdgCNj6_qSbqkQNOKErlK8-6kc3PY6-CBbt56DxFpgWThS0BuwBPeLlRxDkTwxlThy2HwQZbK-FPEQyKAGXs_ygX-ACM2JvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووری
؛ باراک راوید به نقل از مقام امریکایی: امریکا امروز به دو پرتابگر ایرانی در جزیره لارک حمله کرد
نیروهای سپاه پاسداران سعی داشتن موشک‌های حامل مین دریایی به تنگه هرمز شلیک کنند که قبل از پرتاب توسط امریکا منهدم شدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/70818" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70817">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6826005e4.mp4?token=v3CwoLvQwR88hNsGVvKBG4y8elZqpU7cFbKdsiX98oziAxKrID2FkSfJmUUTeQy3vF0Ovq6dmxlzoD7hO6lw2dWzTgycL2BuWj0GPAwMGnrbaAVDUWAzvDrw61cJonViesUCuRwAVGQz9n8EbBdaDgVE-hOxqNVY2Ks7gL7DA2PfCQ21_eZnDJ39wVSTXzF_gOqoebw9pb6UrT9kbcOnGWT7ILmm6exLX2uJC7oU1pWZ3NvoVTr0rbCDBvkEDM0QS2dR7P992770DwKvT53q3LeX0AJLAaTLHKVUtt3THl6qH0z5zD1cB-YX40P9BY-UpX7pymaZkOeqL7Hets7bEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6826005e4.mp4?token=v3CwoLvQwR88hNsGVvKBG4y8elZqpU7cFbKdsiX98oziAxKrID2FkSfJmUUTeQy3vF0Ovq6dmxlzoD7hO6lw2dWzTgycL2BuWj0GPAwMGnrbaAVDUWAzvDrw61cJonViesUCuRwAVGQz9n8EbBdaDgVE-hOxqNVY2Ks7gL7DA2PfCQ21_eZnDJ39wVSTXzF_gOqoebw9pb6UrT9kbcOnGWT7ILmm6exLX2uJC7oU1pWZ3NvoVTr0rbCDBvkEDM0QS2dR7P992770DwKvT53q3LeX0AJLAaTLHKVUtt3THl6qH0z5zD1cB-YX40P9BY-UpX7pymaZkOeqL7Hets7bEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
محسن نامجو در کنسرت نیویورک، شانزده شهریور نود و دو
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70817" target="_blank">📅 23:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70816">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d075c961c.mp4?token=YL1NVXImroHUgfaDPkOMxh1SnSjDY8BbkHg7y3BsoWx0QKL-KNaOL7ZWwSYprSRpevcLFXc7T1oteG8QJFl_JZi9PHYpe3NL_bjoKrPYByA-yirTthIdT8dSbp8Scyy7UnwXJlhJTRbmOojggaU05zLkLefzwKPPtbIqx1ijYIfV2CKaJRX3WDir8Q3e4fN07DMphfQjgXwie5xCawQz2fK2CWVD-Brr_7pYpoPiz47ectzirlQV2XPIOKpSI9wf6MjZ7O_U1LMKSMhKj_t_l_9TdowcSAeSNpCEh4oo4lwlwjHkROiGPiE98_Buc785g4qn5kqtvIl1IDWJiLWybElATan8sUW0om0nuGnkqFdWTRM0NbftJypICxBprPKlDeqveJM5I8liIgKhz-QsXB7_VMxd8kxBOu9Fmse5GnOqRc35tJ8Iuqdfa-d3Bbvw3kpWGc2JuO6zrL-o8sFOB2HkM4BzF1A03LXt8fiFsgGwDCBu2UuBb_4_rd2DIP2UPvn-ip5kBAyN5qvgsQg_TvPL8wLkZzkm1E4jkHK9fPzpfp-ekH1s9vA2Bpjeo0W-WRSH8LOU3D4xJHMvCptC0Too2f1sA7L-ft2IYF6h1quzAdj8nBU5hKhMNh0zZgf20TwTuqNV_rmni_fYa1oWxCjm-5XdIJAu2PO3ersJ0kk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d075c961c.mp4?token=YL1NVXImroHUgfaDPkOMxh1SnSjDY8BbkHg7y3BsoWx0QKL-KNaOL7ZWwSYprSRpevcLFXc7T1oteG8QJFl_JZi9PHYpe3NL_bjoKrPYByA-yirTthIdT8dSbp8Scyy7UnwXJlhJTRbmOojggaU05zLkLefzwKPPtbIqx1ijYIfV2CKaJRX3WDir8Q3e4fN07DMphfQjgXwie5xCawQz2fK2CWVD-Brr_7pYpoPiz47ectzirlQV2XPIOKpSI9wf6MjZ7O_U1LMKSMhKj_t_l_9TdowcSAeSNpCEh4oo4lwlwjHkROiGPiE98_Buc785g4qn5kqtvIl1IDWJiLWybElATan8sUW0om0nuGnkqFdWTRM0NbftJypICxBprPKlDeqveJM5I8liIgKhz-QsXB7_VMxd8kxBOu9Fmse5GnOqRc35tJ8Iuqdfa-d3Bbvw3kpWGc2JuO6zrL-o8sFOB2HkM4BzF1A03LXt8fiFsgGwDCBu2UuBb_4_rd2DIP2UPvn-ip5kBAyN5qvgsQg_TvPL8wLkZzkm1E4jkHK9fPzpfp-ekH1s9vA2Bpjeo0W-WRSH8LOU3D4xJHMvCptC0Too2f1sA7L-ft2IYF6h1quzAdj8nBU5hKhMNh0zZgf20TwTuqNV_rmni_fYa1oWxCjm-5XdIJAu2PO3ersJ0kk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇵
🇨🇳
تصاویر بالگرد چینی از  سرچشمه سیلاب مرگبار در مرز چین و نپال
یک بالگرد چینی خود را به نقطه‌ای رساند که در آن یک یخچال طبیعی فروپاشیده و حجم عظیمی از آب آزاد شده بود.
این حجم آب با حرکت به سمت نپال، خسارات گسترده‌ای بر جای گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70816" target="_blank">📅 22:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70813">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HsdMBv7frPhr7dreIPrMn4ANMBA68ncS-5oKz0qA_qhiXFhdJrpPwBiU88YQpXusPp60fVqfLzq4W6rr2Q55ugoyR2R8c7S9DVZufLM8J4Hz2k01OYgRrKwicBPPUl5z7yfHTWGGWqdC9npufHVxmEiWcJaj3slDe29iaS-bC9VeglgfG_r4yG6hcDUF-mPBa1uI0QhnjkFu6RgVe_XlESfcTP5dVkv16AzNSDgT_RbaDgJrx8yOwXDPIs0QNrKs9JHy1W7m6rHffrt0G9063gANHWrva9jbJzPTAkHPxqvIsdW_lYarWFBj230rFoF2Tn_i0AkbBxICkylq2bnFEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aWj4PjulL7LX0fn7N68TR9z-gEtdHjNnDF_sd_olwTKyRg1meXk2pVgetKjtpobvUud58ndmnlaUH09Z6-GmsnYDCnYzIiHR82BgHBJIwGqHykl0HgQZfp-288ByCwfhQIPmsX2amGyyzQKrsE_b7JDvNXMePRMMocsiNK9UkLBL2x3QV1VMZoE63KKKM-_HzE9eiUDvCt2DrkNoOoQpEsRk5PdBr-xTs4VT3mRKys1OncTCpINxGayWWEKkb1ySbI0eijTXS5z72x-HiavHAs4s99UnS8Nc4Y2PAEXjV1tGgjsUrmbbaCO79SVvaWetGeLnWx8M1nRt5PDUTkF4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dF-Kr31O_K3q0zPsSTJASZ-U8s0zllnvCL5e48aRjzMlXIGe-la7611qEzSo7JnEp0vDyWqk9M_pcOO5nysLFj-OMVnZz9mkLbDw7A75SkF7M0Y5RcYFI8p0HJiYWmFq1n8lKVBCE0E6x4NVpRuDJf8lMXw1FuZ3v7XkRrp0qq2DN6nn12CWCfxxNzaUVhTDxRbLsAXCt24YfudQtsLePO1MvS7wd9aTjYvj05fvSXNfkqhJ4IZKC5oEYIa_XhylWsEK1FtLgSVZk1CmJTCfAMIWcqgdbG2_VvMdr0idWxjYcm1Pz-fdUoinfRy61n3LEH7buFHKhffKpEmKIm8XeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
از کیوت‌ترین عروسک ایران به اسم:
کون‌کش، رونمایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70813" target="_blank">📅 21:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70812">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedd59487c.mp4?token=jWUsatt5FVsOaAgdim5SAiVX2nm33NTf09iiVCw9nXwGsU4ZWVeqG5wQVZIi-VfcA2gwLBCPJroqfSCSO1e-HJhc96LEEMDfj82xFBktrEaEnpuJvso2JR_ACOkRSlrL_SJtYZO8pe0RX9upUJNhFhlPblA_yM5GYOPKX1DDhhOEqw85ONBgfWrDlu4icT7Xy7mugewcWNUyiEJBNw65lzjMlWyaCapa-uyfD4skF3E5cF0Yo3VV0HWSuOv1Y_kAbD3U7znM-41hs9xSCHcJ7q3O7BjTBRX6MKSiHPKcDTN-EU9_EMU6d51apaZIdArNZsuaKLNIE8cJCRAe5wWVLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedd59487c.mp4?token=jWUsatt5FVsOaAgdim5SAiVX2nm33NTf09iiVCw9nXwGsU4ZWVeqG5wQVZIi-VfcA2gwLBCPJroqfSCSO1e-HJhc96LEEMDfj82xFBktrEaEnpuJvso2JR_ACOkRSlrL_SJtYZO8pe0RX9upUJNhFhlPblA_yM5GYOPKX1DDhhOEqw85ONBgfWrDlu4icT7Xy7mugewcWNUyiEJBNw65lzjMlWyaCapa-uyfD4skF3E5cF0Yo3VV0HWSuOv1Y_kAbD3U7znM-41hs9xSCHcJ7q3O7BjTBRX6MKSiHPKcDTN-EU9_EMU6d51apaZIdArNZsuaKLNIE8cJCRAe5wWVLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر برا مراجعه کنندش تزریق لب انجام داده و از شدت ریدمان، خودشم نتونست جلوی خندشو بگیره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70812" target="_blank">📅 20:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70811">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzdcCzgH8YcIRN2U-iv6HBDjeHAzHQrBbzhvVTTUe4yndxa3uSrF2az8wAOZg4Vzg6PiZALt2r7MkJfCpFPHq0tsSqTv_T0IH3GI-TmshJa5_HCPlHXQdfgxxmrTaMpw8Vi8Wm9ub2OYoIsb-_fS5iiQiX6YPk227BA9i2ESgQsPX92JRHMnVyatC-6hLOLVwXJUa_6XyVsdF_wN7nmeTuEaewY0j80vp6PPdV5s2CQHleRaUj7ESoepC3fRUsloBaQC6ECEGr6_n7ojn6iT-MFjzV96x5cq28uJl3XVQptdJNQbYpt6sS0c-NWDNvcwIlY17h7IG3wC99wFeJZEcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
یک نفتکش هنگام عبور از تنگه هرمز در مسیری به سمت داخل (شمال)، در موقعیتی تقریباً ۱۲ مایل دریایی در شمال «خصب» عمان، هدف اصابت یک پرتابه ناشناس قرار گرفته است.
این حادثه هیچ‌گونه تلفات جانی یا پیامدهای زیست‌محیطی در پی نداشته است.
موقعیت مکانی حمله نشان می‌دهد که این شناور هنگام استفاده از مسیر کشتیرانی تعیین‌شده توسط ایالات متحده در آب‌های عمان، هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70811" target="_blank">📅 20:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70810">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIx1VlLX9RDZ2KaFlL9rPGTGMYfrlw7FEPPPQGqx62jKrayzeT6-1rgAEBAG8i6_WiQm46LC_mcGoI09npuOrKzO_5fO-zA48jncTvaYrQ3mXMQc2bskON07OlZfwkzoGo5-M6lUKvANnlcqDkWaac6_xU_S9qqmlTl89Ys__UowaQou-T_Lln7sisPhqgGyGaRAh3-MJ1_5h243Q7uHUHP8Jy0H_WDvcLebCCf5Eo3WHP6u_wC5IOVZs4c4ztpHVplgxPxXgv8aHhL7OgbabwE8x4knxiSkWTJ_J556j3KWNqZJ-qKujbflZ9BP4xSYtiLQpEzDtDtkw_beKV_gDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ برای اینکه لج کانادایی‌ها رو دربیاره، اسم دریاچه کانادا(Lake Ontario) رو گذاشت «دریاچه آمریکا»؛
کانادایی‌ها هم کم نیاوردن و از لج ترامپ اسم دریاچه رو گذاشتن «دریاچه هرمز» و تاجایی که میتونستن این موضوع رو تو فضای مجازی وایرال کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70810" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70809">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ce04d5d87.mp4?token=mf1zBRyaFYCRu0E8s6oBQ7ztZSjuldy-p5VMyY2FKTWeX10GmPkN0ATsuKCwxzIq__joEn8lXyEAQ74g6V1JGrgeqbKUWbw1MoUbe1mKmf7OisY7T-YoqOzmDr4ZZogYBR-frmHtXgA9DlPm3SxPUjIVTZKUdbPnRimaF51Au1xLeaNVUsKgRay2HW6cytIoSghWoc6URM0rxFjmRsCvnJNACpp3vpqYwJXuQdaf6pbaGTkfw-ozDWYRKyzhoEzWc_eXEsrbuT7Z7Z6lKiIfBggtPXQiwWCfLWDqNMbLORNlwVm-3scR_MBtTp4ce1H-nXkvodJty47k-k-IYhGBrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ce04d5d87.mp4?token=mf1zBRyaFYCRu0E8s6oBQ7ztZSjuldy-p5VMyY2FKTWeX10GmPkN0ATsuKCwxzIq__joEn8lXyEAQ74g6V1JGrgeqbKUWbw1MoUbe1mKmf7OisY7T-YoqOzmDr4ZZogYBR-frmHtXgA9DlPm3SxPUjIVTZKUdbPnRimaF51Au1xLeaNVUsKgRay2HW6cytIoSghWoc6URM0rxFjmRsCvnJNACpp3vpqYwJXuQdaf6pbaGTkfw-ozDWYRKyzhoEzWc_eXEsrbuT7Z7Z6lKiIfBggtPXQiwWCfLWDqNMbLORNlwVm-3scR_MBtTp4ce1H-nXkvodJty47k-k-IYhGBrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
حمله پزشکیان به صداوسیما:
مسعود پزشکیان، رئیس‌جمهور ایران، از سازمان صداوسیما به دلیل سانسور خود و سایر حامیان تفاهم‌نامه با آمریکا انتقاد کرد و این نهاد را به اتخاذ رویکردی افراطی متهم ساخت.
پزشکیان خطاب به جبلی رئیس صداوسیما: «این روزها دیگر اصلاً تلویزیون آن‌ها را تماشا نمی‌کنم. آن‌ها مایه وحدت نیستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70809" target="_blank">📅 18:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70808">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b978362a.mp4?token=kTBnL6jr-7XbvriwKZhionsI1yGHGt7qnswAcmJBvGB2bbxMsU9LSImQ2AjM9khyy6cbt2xGeJRmwEL1o8zs5RJdSqu4vK-v4AUfwvL66PaQrV5bf3N_rL3dXytN_1BY93LM4smK4ctvn0SgKzOmXyJrElhCBaxJ1Pymv6fZgpc9qax-eUlX1mkuieZ7OwWk2XaoGkva7VVpw5zqqjtFnOXxJIF1F0tV7c0djDZMODTbnNznGmFNHcETMu88FqmsPEzX0if3w2g6LdOv-hphxXjrfKeJaCTZAu_pt6aL7If8bhoIoU6HvMYs5yOMTpdZQzkKmfwHSJNubDuHGiGzgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b978362a.mp4?token=kTBnL6jr-7XbvriwKZhionsI1yGHGt7qnswAcmJBvGB2bbxMsU9LSImQ2AjM9khyy6cbt2xGeJRmwEL1o8zs5RJdSqu4vK-v4AUfwvL66PaQrV5bf3N_rL3dXytN_1BY93LM4smK4ctvn0SgKzOmXyJrElhCBaxJ1Pymv6fZgpc9qax-eUlX1mkuieZ7OwWk2XaoGkva7VVpw5zqqjtFnOXxJIF1F0tV7c0djDZMODTbnNznGmFNHcETMu88FqmsPEzX0if3w2g6LdOv-hphxXjrfKeJaCTZAu_pt6aL7If8bhoIoU6HvMYs5yOMTpdZQzkKmfwHSJNubDuHGiGzgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر ابراهیم رسولی، دستیار قالیباف:  ما تا آخرین روز خون‌خواه رهبرمان هستیم امّا پوشکی که من برای فرزندم قبل از جنگ می‌خریدم ۳۶۰ هزار تومان بود. امروز همان پوشک ۸۶۵ هزار تومان است. باید آرمان و شعار را با واقعیات جامعه تطابق بدهیم.  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70808" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70807">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsmtqdrWt8jueLsbxHFIJEyktYzPK5Eqvoxw_l_KinyoK0u0pdJPwavPgk7C0PQIToYVG8e5pYsWdAgt8Vy5XlUVPanBjVVmmKQNl62CyoDwyfXpK2V1BLo4wKW9VhftK0pRR69f-mflaU5HnnfIzFavBMMgYUTDGlGpriV-87UuhIqIdeG3R04ApT4dlVd2a855fI82pfUdf7KhLFiBpD2ElhCMc-Lciqpot-oiDz8lD4faKuH851tkIWKBhfjpCpt34jYGRHuLQcIMgPtUT3mt2Z3Z7ImPd5bllrM52RmWSpzWEOyCDFm0E6ZsMGrecIeaKIszyfz1qhgf0lbD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70807" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70806">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اوپراتور های حروم‌خور ایرانی مشخصه رو بسته های اینترنتی ضریب می‌ذارن، من صبح یه ۴ گیگ هفته‌ای گرفتم الان تموم شد، آخه چطور ممکنه فقط چن ساعت اینستا بودم
😐
از سال ۲۰۱۳ تو اینستا بودم قدیما با مودم یدونه ۳ گیگ می‌خریدیم تا یماه می‌رفت، شما دیگه مرز های وقاحت و خارکصگی رو جابجا کردین خدایی
#hjAly‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70806" target="_blank">📅 18:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70804">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2-wKjfCmKjj3nGyNuzI0YOnvBPapfgJrcmwetUg7p8QrD7rUZLlGYnNUfG-DeO-p4_ye0qVgu4PbIS-Q0hUZ_bNknFEemec8jM-S60s1oERy6KkIjxA95BT8d72z_VwJAQRMc0PZNZEa-oe96eZGrvItGZMynHCMHEFo9r0h-VtcHz_HTQ00zqDDc8tE5OXnnEUFXeIo96oEjM0pN4ES02zivM9ZMJKXEPi44ioRBfbFt1pJA8zrNuRsYnvEJX4vug5i5tKPcMs-q66JcQrlkol_HA8HwLDe9Ck0W-osL-WYX3WecK43b5qQBhsrNvyzpkXGB-APIlNVR-ZwTsL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBZQmuof103IrGoJ92iIf1_QZy60jnxJyBI0lS-mUFQuuhi_XBw0EPfG7GwQH47KA-tcfkQRsJsq9sTZwoTUlI1yUi5HWVI5gN8SonFNiYY1MMo4XTlgTRqtoDch9FD5Pvpa_wYtm9goniN0wFnydxex3NEw0uerR8TyezDEpJuCzuRG5vSk5KThiQ3NpsHFDiirDt4wv5x5_E4NfJp7i7Ucafoy1rT2lwtI_RnfB_saCxbjkvyKmrQzXWEEO0DtYSgKQCEi_4UY0qHDZ9sTxothE8LhOYZnb1yPvlmI1BxUjKIly7n8za4iqp02Sf42mDH0p7neMcwtNHzwSA2pdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصاویر جدید مادورو در زندان های آمریکا که گویا در اونجا از ایرانیا خوشحال تره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70804" target="_blank">📅 17:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70803">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc84ead5.mp4?token=jW142kLHNZ-ChVAcM9juXn9GHNB1NmzIctUrEJNo_NgPjTsCmEgRM12CgiqVq8iPHlVzscwr8N-ZW5KzdAG5Al6TWNlSz3DJ9y0ke1DSls_00vby3Y5HuIU7JWdYdKXLAU8y1M-av-mD1cNqvw9AXvURDsIkJT_flZSaut-28xNc7KliBKOIf-_AfZce9q8f25DT5miGkRP_1DesC-NNp_sE8ApfWKtJMzEp5q1xglfo2IC40w7ug3-YxaytusmY7uDf1tQn3ZmOc9ZeXxPclwLHPqmqBEyRXOHqQ_QtVMgDDFYz1sQevcohF26NIebB5KxGnSY0sbw3TDEtT2zJtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc84ead5.mp4?token=jW142kLHNZ-ChVAcM9juXn9GHNB1NmzIctUrEJNo_NgPjTsCmEgRM12CgiqVq8iPHlVzscwr8N-ZW5KzdAG5Al6TWNlSz3DJ9y0ke1DSls_00vby3Y5HuIU7JWdYdKXLAU8y1M-av-mD1cNqvw9AXvURDsIkJT_flZSaut-28xNc7KliBKOIf-_AfZce9q8f25DT5miGkRP_1DesC-NNp_sE8ApfWKtJMzEp5q1xglfo2IC40w7ug3-YxaytusmY7uDf1tQn3ZmOc9ZeXxPclwLHPqmqBEyRXOHqQ_QtVMgDDFYz1sQevcohF26NIebB5KxGnSY0sbw3TDEtT2zJtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حرفای وایرال شده رحمان و رحیم پایتخت درباره ازدواج :
ازدواج نباید دوقلو باشن چون ممکنه این وسط اشتباه بگیریم اونارو
آقا کاره دیگه یهو دیدی در رفت دیگه نشد جمع بکنی
سارا و نیکا هم خب اون زمان تازه بچه بودن کلا نمیشد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70803" target="_blank">📅 17:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70802">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5696dbdc.mp4?token=Hiz0DLA1pDAp95RON2Vd9bvL6kUlp5D4VRZKidZ6-f95jConYMi9c4r8c1WJdAtoLrNm8McgPB2z2gpFutbjNNcl1Nr2c9j0XnlaadoN5Be_xJD5WOGF9vIYKhwPHldoQ4c-szr-1Tph0p4wd6wAUOqlPL7sCBgS9QdXkydWBiQ8YBktpNJS9eVuCQCp2hx3Bl48hyKrQp13-aj4u2w0CMS9gsumTKnO8epwzzwlT1Zxq7R4UHhkqmUOaTiEs8zH1telD6JDTUHI4NRcT6x38pFTTqknz8HQvpmdRraMtff73BnCpa6W64NWH3NaTA3mMit8kjFsqpEKLuWU2nETaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5696dbdc.mp4?token=Hiz0DLA1pDAp95RON2Vd9bvL6kUlp5D4VRZKidZ6-f95jConYMi9c4r8c1WJdAtoLrNm8McgPB2z2gpFutbjNNcl1Nr2c9j0XnlaadoN5Be_xJD5WOGF9vIYKhwPHldoQ4c-szr-1Tph0p4wd6wAUOqlPL7sCBgS9QdXkydWBiQ8YBktpNJS9eVuCQCp2hx3Bl48hyKrQp13-aj4u2w0CMS9gsumTKnO8epwzzwlT1Zxq7R4UHhkqmUOaTiEs8zH1telD6JDTUHI4NRcT6x38pFTTqknz8HQvpmdRraMtff73BnCpa6W64NWH3NaTA3mMit8kjFsqpEKLuWU2nETaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صادق الحسینی کارشناس اقتصاد :
کیفیت بنزین رو جوری پایین آوردن که تا ۳ ماه آینده تعداد زیادی از خودروها قراره تعمیرگاه صف بکشن و موتور تعمیر کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70802" target="_blank">📅 17:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70801">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1befe3460.mp4?token=kWD6xqlqmfIpA4Uy41vsne_GuN7KL5Vv1L3YV_F9wtMMQUUgTToNs0v2vIAq3o-XBp8K7XX4UStiOlxSVZYBEEV2FYfTM5jhALggXXVWXny1zMR3N7BTsnMDqOxAeez5si8lWasZ5uJd0n1VWuHAHzQWj-7zsxFRqOoCtRZ1Wt5EqbjgpRMiCIOy7kDVaQjolvBjKUZAx6k3TO_Co7vHAD9_z7hVLYdRI9-mS90QQm7v9Tw0rVip3ffUuzfyWR28uQTPoiO3MfKv_2gubL2MtGJteJc7YXh-ZqSJpG9566ajG5G6zJf5xF3xRiBgMF0RX3mfYG1iU_EdD1XvJtCdZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1befe3460.mp4?token=kWD6xqlqmfIpA4Uy41vsne_GuN7KL5Vv1L3YV_F9wtMMQUUgTToNs0v2vIAq3o-XBp8K7XX4UStiOlxSVZYBEEV2FYfTM5jhALggXXVWXny1zMR3N7BTsnMDqOxAeez5si8lWasZ5uJd0n1VWuHAHzQWj-7zsxFRqOoCtRZ1Wt5EqbjgpRMiCIOy7kDVaQjolvBjKUZAx6k3TO_Co7vHAD9_z7hVLYdRI9-mS90QQm7v9Tw0rVip3ffUuzfyWR28uQTPoiO3MfKv_2gubL2MtGJteJc7YXh-ZqSJpG9566ajG5G6zJf5xF3xRiBgMF0RX3mfYG1iU_EdD1XvJtCdZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
پایین کشیدن تصویر مجتبی خامنه‌ای در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70801" target="_blank">📅 16:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70800">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c5ff11496.mp4?token=v6NGRcSOj0YytcaSsGLVyv50vP2qJ6bvfyiHnlcoF_D57CJvJZFiGTjf6Mnz9rYUa2vAFPxWJeUdOpG-lFgIGmuteLJsfwnVK833-usPBKdQj12x1c71QZfYpO4FdgUm1e4no1oHCH-RbUt1J1mpXELPMWAl28xRIyawHWsUHzDghv53A0DK52qOgGNVnFBTOAfa5mikBzpXJPVx3l3b2pUAf-yI7dIfPlo9lykMKkQbpCq45KWzjUAPRBl_nQSzIP9eh-EL9Lx0A9s0NA3lJK1aQ3sGLe3tUUT5RSNgzMTCvAjTczjFLWkpGnl7PQyLBkV7boE4l4zWzzi1UZIS9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c5ff11496.mp4?token=v6NGRcSOj0YytcaSsGLVyv50vP2qJ6bvfyiHnlcoF_D57CJvJZFiGTjf6Mnz9rYUa2vAFPxWJeUdOpG-lFgIGmuteLJsfwnVK833-usPBKdQj12x1c71QZfYpO4FdgUm1e4no1oHCH-RbUt1J1mpXELPMWAl28xRIyawHWsUHzDghv53A0DK52qOgGNVnFBTOAfa5mikBzpXJPVx3l3b2pUAf-yI7dIfPlo9lykMKkQbpCq45KWzjUAPRBl_nQSzIP9eh-EL9Lx0A9s0NA3lJK1aQ3sGLe3tUUT5RSNgzMTCvAjTczjFLWkpGnl7PQyLBkV7boE4l4zWzzi1UZIS9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دوربین مخفی و تلاش این خانم برای اینکه جلوی خفتگیر رو بگیره خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70800" target="_blank">📅 16:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70799">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fdd874dd6.mp4?token=now0XGrOTTZPieqbXcegEdbZGfkne9SCi7Tf4xiCUKwVjhleezuOQvJTEnDjNieAUYkhaBtp7G4PuDbjElLEOaKtB3k40ocHVpxp4ulxCcShVJA9T5cvXxgZpgvZV9EfB6z1YtrWFnOIiJyQiEQ-3Px2Bj7mMkQEIyt9Gfmyhu-ewtobJGJxjRmlFMNEolRVaw5igNknIkq2jcmRcFqLAcURh7KmVZ0KSTJlc2il7szNLbTZp68qUBimzQrGwsz0gHzB1qKIthUQHxcmmNycshWThedjLJ5P3s_CXRDz-bTEifvF8h562LNgri-t65l5jQX6F_lOQZ_0EJ-HDwCTMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fdd874dd6.mp4?token=now0XGrOTTZPieqbXcegEdbZGfkne9SCi7Tf4xiCUKwVjhleezuOQvJTEnDjNieAUYkhaBtp7G4PuDbjElLEOaKtB3k40ocHVpxp4ulxCcShVJA9T5cvXxgZpgvZV9EfB6z1YtrWFnOIiJyQiEQ-3Px2Bj7mMkQEIyt9Gfmyhu-ewtobJGJxjRmlFMNEolRVaw5igNknIkq2jcmRcFqLAcURh7KmVZ0KSTJlc2il7szNLbTZp68qUBimzQrGwsz0gHzB1qKIthUQHxcmmNycshWThedjLJ5P3s_CXRDz-bTEifvF8h562LNgri-t65l5jQX6F_lOQZ_0EJ-HDwCTMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره کسایی که میگن تحریم هیچ اثری نداره:
نمی‌دونم چی به اینا باید بگم فقط همین رو میگم که عقلم خوب چیزیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70799" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70798">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036dee7c15.mp4?token=K-HJxS5OPavvrbNlGpQ7968KDzjr3IPaB2tc7Oh6gCuEuH21u57vpqI8mFMNxrqgCiAYeKoaeS6Cwl_FFrKbPy81UOjCpGxcKSNsD8ONfmEnhkdBE7EnYOUYmGuLp44qLv7jCQAi6j61nj8oxE3r1A-v3cvOKzO88Hdr5kdT5nixKMAf00IJBUlqXu2UM6fpa_nuxCMMf66OsyMQoC6FX4Racqy20X7Oy87YHUVcZ71DrfKiA1KT8p23_BoJwR63jT9JebJMdD9vqKouN3q0ZvExDPidaCCZDtc8niabW1noZlgoqS14WuVe35ridfQrbUUNRoBoY9aXE47SY7WoJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036dee7c15.mp4?token=K-HJxS5OPavvrbNlGpQ7968KDzjr3IPaB2tc7Oh6gCuEuH21u57vpqI8mFMNxrqgCiAYeKoaeS6Cwl_FFrKbPy81UOjCpGxcKSNsD8ONfmEnhkdBE7EnYOUYmGuLp44qLv7jCQAi6j61nj8oxE3r1A-v3cvOKzO88Hdr5kdT5nixKMAf00IJBUlqXu2UM6fpa_nuxCMMf66OsyMQoC6FX4Racqy20X7Oy87YHUVcZ71DrfKiA1KT8p23_BoJwR63jT9JebJMdD9vqKouN3q0ZvExDPidaCCZDtc8niabW1noZlgoqS14WuVe35ridfQrbUUNRoBoY9aXE47SY7WoJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنلاین شاپ های اینستاگرام برای ویو دست به هرکاری میزنن
مثلا این ویدیو با ترفند شیک باسن باعث شد میلیونی ویو بگیره
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70798" target="_blank">📅 15:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70797">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0459b57f2.mp4?token=JGES3CjTzuHuK_pRZL-rSWemXuDojJWba6iLt7mOcpJAN-P_-VTLXlGoUthVfKiEMGDT7a7EvY52STJenSw5UMS6uOc-XVQsZf1KyDFJIcG1v1GK4J0TUoMzdPwMJQLvRBffEnbywZ8aEXzPr_zZ3qKllfllAD7lZZo04HNmMvCmbuvdRlQMciBtAKZ4KSoB1J5XdnEor5-AblRywc5VtLrWyx-9GowDG-P_WUexswAd7Maf8docgzIcbMFVKRuYnBdzd4mN76xXX5FdQcbiPaUnSVUSFNoG4VgvdG7FL-us48A62Tng5JUrdjGyTzofcIlz4hc0RB6F5zQeUIq4TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0459b57f2.mp4?token=JGES3CjTzuHuK_pRZL-rSWemXuDojJWba6iLt7mOcpJAN-P_-VTLXlGoUthVfKiEMGDT7a7EvY52STJenSw5UMS6uOc-XVQsZf1KyDFJIcG1v1GK4J0TUoMzdPwMJQLvRBffEnbywZ8aEXzPr_zZ3qKllfllAD7lZZo04HNmMvCmbuvdRlQMciBtAKZ4KSoB1J5XdnEor5-AblRywc5VtLrWyx-9GowDG-P_WUexswAd7Maf8docgzIcbMFVKRuYnBdzd4mN76xXX5FdQcbiPaUnSVUSFNoG4VgvdG7FL-us48A62Tng5JUrdjGyTzofcIlz4hc0RB6F5zQeUIq4TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
آیفون 17 پرو از ارتفاع ۳۰ کیلومتری سقوط کرد و سالم موند!
آیفون 17 پرو رو با قاب محافظ
RhinoShield AirX
از یه بالن، از ارتفاع
۳۰ هزار و ۶۰۷ متری
زمین ول کردن!
باورکردنی نیست، ولی گوشی بعد از این سقوط وحشتناک
کاملاً سالم موند
و حتی یه آسیب جدی هم ندید.
🔥
🏆
این اتفاق توسط
گینس
به‌عنوان «بلندترین سقوط تلفن همراه درون قاب محافظ روی عوارض طبیعی زمین» ثبت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70797" target="_blank">📅 14:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70796">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7GWKhe_31E7JkUq9GuvGYZW-gCQteRVEmalhVH6vA0dW2X5JuBvrEU3EA6ezlIMkH7O8I66bV2DB2CxsaCETGRt1Uu0jXemlsZzpaVRBszW7nNghe36IIlaJXhthP9y8UOeJg9mAMcqv0oNIKlsp5KSFHcqMMUEa_3rSxIKpg1rE2cgPLC9R8I7aeTBwKf49DV_R0Bi-MkG_DzRextyP547Yer9LY_4uw75TyIZ4PAaOw4oygD651840iDRpfhVDvYTKQw0QBDMTZqPxBp-Tt7_b_vV3Say9Tn9R_CGwnY4de3RGx_mt7I3S3VIOc7mQHSUH2AMhz-oNwpcHgotGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تصویر ماهواره‌ای از بقایای شناورهای غرق‌شدۀ جمهوری اسلامی:
تصویر ماهواره‌ای تازه،بقایای ناوچه‌های جماران،نقدی و بایندر را نشان می‌دهد که در حملات اخیر آمریکا طی جنگ ۴۰روزه غرق شدند.
در این تصویر همچنین بقایای احتمالی یک شناور کلاس دلوار و دو شناور گشتی کلاس هندیجان دیده می‌شود.
محوطۀ پیرامونی نیز آثار گستردۀ تخریب ناشی از حملات را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70796" target="_blank">📅 13:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70795">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45caa5a649.mp4?token=b6Id9FS7UyHZ5d7hIEAYsqsW4tJIlbaQuZ92SSdiHj34LlTwfXlPpGVcpiVQAXLKl76KdLSCsmueu1XOVO8RdRkJEs3gsdaJfqKgntXuKYUYq24S8ekYmEYshmCXWMyCSVPjKqfxq93ftEzuHEFvg5DmV-ljXRMSX_4I4IplzU3Nori4sl8GFMJaFigCjrzAji97l5sPP8Bw5SiH5GstBgx0uM4b16cOp6A23hUtKz4UYM6RoBdYlkuD56B9mF4G6D0iwybamnZylxzjOYKf8RjHIIUUIuHimm0QjnWW8N-R6DAgq02ueuK5r-EqLBrR7OfVbZu6wYlVUcL46lv0fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45caa5a649.mp4?token=b6Id9FS7UyHZ5d7hIEAYsqsW4tJIlbaQuZ92SSdiHj34LlTwfXlPpGVcpiVQAXLKl76KdLSCsmueu1XOVO8RdRkJEs3gsdaJfqKgntXuKYUYq24S8ekYmEYshmCXWMyCSVPjKqfxq93ftEzuHEFvg5DmV-ljXRMSX_4I4IplzU3Nori4sl8GFMJaFigCjrzAji97l5sPP8Bw5SiH5GstBgx0uM4b16cOp6A23hUtKz4UYM6RoBdYlkuD56B9mF4G6D0iwybamnZylxzjOYKf8RjHIIUUIuHimm0QjnWW8N-R6DAgq02ueuK5r-EqLBrR7OfVbZu6wYlVUcL46lv0fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
تاکر کارلسن، تحلیلگر آمریکایی:
در نشست‌های پنتاگون درباره نحوه واکنش به ایران، گزینه استفاده از سلاح‌های هسته‌ای تاکتیکی بررسی شده است.
روسیه، آمریکا و اسرائیل در حال بازنگری در دکترین‌های هسته‌ای خود هستند و آمریکا نیز این موضوع را بررسی می‌کند.
سلاح‌های هسته‌ای تاکتیکی با وجود قدرت انفجاری کمتر، همچنان تسلیحات هسته‌ای محسوب می‌شوند و استفاده از آنها علیه اهدافی در ایران در پنتاگون مورد بحث قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70795" target="_blank">📅 12:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70794">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=ssAcKvTpQ2QTJc6nxfM_4sb6CGUiywEZolXD4vasqSS_FqGOY0aVYIPZ9Hx-iFgoG5uxyog5dVBtmoKSUrxiBlh10hcgFELRZe2n_e6J5xWy0dULHwPhuV5Zli15U6206_idFYsbvbEMLUwWll5nJ53hWbLbFoCz6DXPJSbrmzMiRgLxjxfGD15sGjJP6sqiZLSqRt70BenBtL0KsY1eYre1JtajgwTmECj2gbuu8LD4IQ4eEzzxMPY_5-FOBI_IX2wA4ZzX2UKendLWmynjMW61y1CbJoEKD3MtSPpiqGsMO4Yi3nRA3rJSj43EpkMo1bZV0pbM0p9pJFQWM8jGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=ssAcKvTpQ2QTJc6nxfM_4sb6CGUiywEZolXD4vasqSS_FqGOY0aVYIPZ9Hx-iFgoG5uxyog5dVBtmoKSUrxiBlh10hcgFELRZe2n_e6J5xWy0dULHwPhuV5Zli15U6206_idFYsbvbEMLUwWll5nJ53hWbLbFoCz6DXPJSbrmzMiRgLxjxfGD15sGjJP6sqiZLSqRt70BenBtL0KsY1eYre1JtajgwTmECj2gbuu8LD4IQ4eEzzxMPY_5-FOBI_IX2wA4ZzX2UKendLWmynjMW61y1CbJoEKD3MtSPpiqGsMO4Yi3nRA3rJSj43EpkMo1bZV0pbM0p9pJFQWM8jGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدویی از روش جالب روشن کردن مشعل گاز با فلر
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70794" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70793">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70793" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70793" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70792">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECO1pPDTg0uTEMdOvSWkvTgWpiRSxl03kNJO1jD-eHlyrfc_fYZseUzpCvGg9nok9dEmsMbfBULpW8Jrkg6310iGWZJaVYvvos9_--o_IgeMZOCaL8ynHcu2p8ifCGSq21rjWA0GdSnqOAjyhKIxQdr-JQ4xnvEyiEnvBFnPXk-JwWdHOrKWm1sTG8_s6HtnID3PJOsc6aR9ldxiz4gWpw8Y-I4Z-MQz1tIsZ2qv7J39142SxYq_RdpswbGRTlyfZkD-YmTZW7uG-2LWJ12XwP6v7FFNFh3-rC5HyTPZ8cDMGU2pp1F6qi0NH6cTGSIrYN8m8taL1Hk5NpXLWaNyBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN
.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70792" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70791">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b95ccb0b.mp4?token=eW2bJAyU4wrFW7JTWH-07C65OQ5Za_hgDMBDfC-8cTgBU0CgYlRtd2tB-T7BUEpOEbSACPXqdT9LuQXtOkj2jCghZLckBUhsXTetNin2xgIARp5wtGsRhKraKe_QoavYwuLiDXztBAKEI8lKvW1MXrpaNuu6h8mKTTuH1FeobhsgJnWlgjR6avo0TxYa29oQAE7E2Czul7Q3zWIEGF8g2GsFS6MCXTgTpcER6hI0c7OZ0L5vWrMdYKMv_ytGGjGAkYVa_RVylaiDd-i836ltEbKLv-2rnjzQQfP0cnUWtvWKKX0GZg-kDUdTLQlSjTz3Vo_YkQzdpfPl9zmQOr4RL4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b95ccb0b.mp4?token=eW2bJAyU4wrFW7JTWH-07C65OQ5Za_hgDMBDfC-8cTgBU0CgYlRtd2tB-T7BUEpOEbSACPXqdT9LuQXtOkj2jCghZLckBUhsXTetNin2xgIARp5wtGsRhKraKe_QoavYwuLiDXztBAKEI8lKvW1MXrpaNuu6h8mKTTuH1FeobhsgJnWlgjR6avo0TxYa29oQAE7E2Czul7Q3zWIEGF8g2GsFS6MCXTgTpcER6hI0c7OZ0L5vWrMdYKMv_ytGGjGAkYVa_RVylaiDd-i836ltEbKLv-2rnjzQQfP0cnUWtvWKKX0GZg-kDUdTLQlSjTz3Vo_YkQzdpfPl9zmQOr4RL4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که کلینیک بیماری زنان داره تعریف میکنه که یه خانم 56 ساله بهش مراجعه کرده و گفته که همسر 67ساله‌ام از وقتی بازنشست شده، روزی چندبار باهام رابطه داره؛
قسمت عجیب ماجرا اینجاست که جدیدا یه فانتزی‌ای پیدا کرده که میگه سرت رو بکن تو ماشین لباسشویی تا از پشت باهات رابطه داشته باشم!!
الانم این خانم سوزش شدید پیدا کرده و مجبور شده موضوع رو به پسرش بگه تا اون بره باباش رو از خر شیطون بیاره پایین...
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70791" target="_blank">📅 12:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70787">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=fA8gN32CIiE42H88UDjWevJyKI6ZdbyrRHsYLG7vWpV26qzzC0FagxmH36RWmZuKYd4_d0mQoKj1uPrF0qNCuBjuAhX0_nCcyuOE3rprUq86n_fbRtfTuZIHfTMa5vNXXP7nO897BOXgz4tuM2cYmF9z1SQ5Mkpltzss57Xhuwy01yl7HjTcODsRON9MVE7F11o7vnGfi3fjfYCjvPbKymGsKnBJm2ulXEUssoYioo2_bQv0FycVVW9wSkR-hH_z7N3rGZJhi4u7mke3E-S-hDkg_fkyQzErl036sognI47AHruv3WCKfB5NAUX9V7FrJqDWFHkggKEK2FXX4sz9tw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=fA8gN32CIiE42H88UDjWevJyKI6ZdbyrRHsYLG7vWpV26qzzC0FagxmH36RWmZuKYd4_d0mQoKj1uPrF0qNCuBjuAhX0_nCcyuOE3rprUq86n_fbRtfTuZIHfTMa5vNXXP7nO897BOXgz4tuM2cYmF9z1SQ5Mkpltzss57Xhuwy01yl7HjTcODsRON9MVE7F11o7vnGfi3fjfYCjvPbKymGsKnBJm2ulXEUssoYioo2_bQv0FycVVW9wSkR-hH_z7N3rGZJhi4u7mke3E-S-hDkg_fkyQzErl036sognI47AHruv3WCKfB5NAUX9V7FrJqDWFHkggKEK2FXX4sz9tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش توی باشگاه انقلاب تهران مسابقات و ایونت تنیس برگزار شد که حسابی سر و صدا کرده:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70787" target="_blank">📅 11:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70782">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f98f823a9.mp4?token=dq17XAmRD5Tv950jsxxIeoDDJjyRm3MnWTMmlY1b4FnCjNgU_qr6iWYN0q3F_mH_cVLfinTDEDfXGQEfUcjdZk0_LvM0jbeJ8qz04A-uvb2qkazPeYpaew1nQjMNzDvfrjARGU_o4jIxZwP5VR8XypOZZpvGFPT1aX96qVaYIMTShCXfRiZOsXb4c1LN3oDqDDGdDw8sWrgTemXGdh_-2ib8CYEBwz6CbDUgA6Twutmd8t0UQicktv1SYcLom6btHJWaMHb3fiJvkJWxVQr-AFZTJ9k47MYCuwW5YLnLLW0natwS0tnwihQ_5EhnNtjHqHqXrAUcAzZeQWdTHdFqZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f98f823a9.mp4?token=dq17XAmRD5Tv950jsxxIeoDDJjyRm3MnWTMmlY1b4FnCjNgU_qr6iWYN0q3F_mH_cVLfinTDEDfXGQEfUcjdZk0_LvM0jbeJ8qz04A-uvb2qkazPeYpaew1nQjMNzDvfrjARGU_o4jIxZwP5VR8XypOZZpvGFPT1aX96qVaYIMTShCXfRiZOsXb4c1LN3oDqDDGdDw8sWrgTemXGdh_-2ib8CYEBwz6CbDUgA6Twutmd8t0UQicktv1SYcLom6btHJWaMHb3fiJvkJWxVQr-AFZTJ9k47MYCuwW5YLnLLW0natwS0tnwihQ_5EhnNtjHqHqXrAUcAzZeQWdTHdFqZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇳🇵
🇨🇳
ویدیو اختصاصی جدیدی که توسط نیویورک تایمز به دست آمده و تأیید شده است، واضح‌ترین تصویر از ریزش کوه لانگتانگ لیرونگ در ۲۶ آگوست را که باعث سیل فاجعه‌بار نپال-تبت شد، ارائه می‌دهد.
کوهنوردان قبل از اینکه یخ، سنگ و آوار به دره فرو بروند و ابری از گرد و غبار عظیم را به هوا بلند کنند، صدای ترک بزرگی را شنیدند.
فیلم دیگری، آوارهایی را که بلافاصله پس از ریزش به سمت پایین تپه حرکت می‌کنند، به تصویر می‌کشد - آغاز فاجعه‌ای که جوامع پایین‌دست را ویران خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70782" target="_blank">📅 11:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70780">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRcTbP_IUqwpR8ZAfNbDveoRqZU7H4qzXuPJKxWO2nb-Ydrc2eX7vqPYo1hZQ1u3ZFJbzq-EOLQgfg4A9KRmUg-OxJy9ibAo_585-LVW65xgRX6YHvNCLusirBvvg1M2YpsWOJTmbeMRFEAC7GT9fGPhmGhbPIEO3S73F-I38qgzUBYmT2wlrez42KxcjMhJKEpe3sYVCC4tRhmTHaqUyTo3WxfiGpf4jasUK7DitLGo9CGXXrznC9MUVJUL9No-fFyCYYRGIAEnorM4p4BQJaB7yhgdRk4bORgJPLTsOo4GnlGbk0KOFa7OaN5J6lH5YDJ9j1Byh1uBoFRPoxPJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3cOQcbl-Nc7AXYPmLZtWcNY-iB5iXNThQmb3G4A95YbM7B8YdlBSUlvVxKdkaNPzLI0XsERNLwpevYWRF2YKGNo47alz9zDRwkin2MmenkaG2tRzHV7A9JSNH1cjPlSqFW7jkDtoO1MA_aT8tuYrHp6YFrS4kPItWzpyhfLcozjbeYYIQEo_nzWw4cqvmV4YyE54cCYpmahczAG0KFs1YX1jIvDNa43EN7QoBJHnWwA7wkAdkG2_Cl3xTIE7nzPuUr3cbNtOh1NgDxpXGNlK8QZt6DPcX48LMe85Y6S3iqFv3-wV4pW_V_f79UbONgT-mgQ2COF_tRbm_nZHxfg0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
استوری یوسف، پسر مسعود پزشکیان:
مسائل رو ناموسی نکنید که هیچکس نتونه درباره‌اش حرف بزنه!
اگه تو غنی‌سازی منفعت داریم، دنبال کنیم و اگه نداریم، متوقفش کنیم.
اگه تو داشتن توان موشکی و پهپادی منافع داریم، دنبال کنیم و اگه نداریم، دست برداریم.
اگه بریم سمت هسته‌ای، دیگه فقط آمریکا و اسرائیل نمیان سراغ‌مون و اونوقت یه اجماع جهانی علیه ایران شکل می‌گیره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70780" target="_blank">📅 10:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70779">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ffa3e78b.mp4?token=i-TjXXoEE-WT17fExYtjJD_gSwZtQP-JJd8G4d46jKCqMQU2GkDsFBmgV04J7g4gdY0KX1sw2khlVyAX9uJ9Bb7F7DqfkwE4L9-ViN-AltWo3pMMF4jtDNwvais-qPWTRUmeCyNIH0qilg0GEMKyj6SNuJilWkOTp9JREKPD2ERgWV20hy2DmAOCTSqK2XMapFBjXAPwk4cz1Ig1GbZevIQCqSVDk6rZadq5_rU_Z4IzQzdXoR472WGZBwYRqrLwNhJhicbWeV-jNUjSpUk_bwbWgikDaRZcPOo2kGxWlQ9pVTeQWzvSl9pRPj0gKox_kDh_jtGUeNpmPhhHrcC92g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ffa3e78b.mp4?token=i-TjXXoEE-WT17fExYtjJD_gSwZtQP-JJd8G4d46jKCqMQU2GkDsFBmgV04J7g4gdY0KX1sw2khlVyAX9uJ9Bb7F7DqfkwE4L9-ViN-AltWo3pMMF4jtDNwvais-qPWTRUmeCyNIH0qilg0GEMKyj6SNuJilWkOTp9JREKPD2ERgWV20hy2DmAOCTSqK2XMapFBjXAPwk4cz1Ig1GbZevIQCqSVDk6rZadq5_rU_Z4IzQzdXoR472WGZBwYRqrLwNhJhicbWeV-jNUjSpUk_bwbWgikDaRZcPOo2kGxWlQ9pVTeQWzvSl9pRPj0gKox_kDh_jtGUeNpmPhhHrcC92g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت بندر شهید رجایی بندرعباس، بزرگترین و مهمترین بندر تجاری کشور بعد از محاصره دریایی آمریکا؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70779" target="_blank">📅 10:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70778">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6d1be5bb.mp4?token=anWP7qxFP-Fv0Y36YxieaNffR-9fh8h7U-sKjKdU2SLJ720M7Zh-Ztx80i1pj49i7bxpJ2UQKCyyYK_DydqxesTbZrBQbPRaq31O-_jF-N79d5MpmB2FE3YNU1L3_EkSd8-NTTzzO8K6tA3RnPrPpN8ZZuwlp4GsEHOcvgH11xPTkp93ybSRtgMxEzwN7ZuRmou0OfjtaDuiK-k9MmvBWzgDc0WSEVePpm44_0fKrOwzYX6XlrHhsH3DkMZbvXg94bssuX10h4k4k0qOD2vdFgM6eiWTd2CinoQC6sVTHTx2Ht41wQJMoO9zs0HeAjoU4HEFEit8XSfJKn2TOFxTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6d1be5bb.mp4?token=anWP7qxFP-Fv0Y36YxieaNffR-9fh8h7U-sKjKdU2SLJ720M7Zh-Ztx80i1pj49i7bxpJ2UQKCyyYK_DydqxesTbZrBQbPRaq31O-_jF-N79d5MpmB2FE3YNU1L3_EkSd8-NTTzzO8K6tA3RnPrPpN8ZZuwlp4GsEHOcvgH11xPTkp93ybSRtgMxEzwN7ZuRmou0OfjtaDuiK-k9MmvBWzgDc0WSEVePpm44_0fKrOwzYX6XlrHhsH3DkMZbvXg94bssuX10h4k4k0qOD2vdFgM6eiWTd2CinoQC6sVTHTx2Ht41wQJMoO9zs0HeAjoU4HEFEit8XSfJKn2TOFxTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان بعد از بیانیه مجتبی خامنه‌ای که گفت ضعف های کشور رو علنی نگید
داره پرقدرت به حرفش عمل میکنه و اومده گفته:
صداوسیما هی‌‌ میگه‌ آمریکا تورمش ۲ درصد رفته بالا؛ خب‌ بابا مال ما ۱۰۰ درصد رفته بالا.
همه چیز به تحریم و واردات ربط داره.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70778" target="_blank">📅 09:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70777">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5638aa725e.mp4?token=GusvWoIK10DQ7EAT6yb6yPKVZPaEx_cU5uo9BkBjg6kdbK5jPaQup3Oe5Vi9tpWsWal8tny9xW6eNqUJeEKaZF8Loe83fcdDFpueSgVNwja4RtmQ_MEE15Mlm4LqNsFUCf4tl83fqXSUJMsCojdV4Wzw9fulZg1r8BUdZZpuYBfqeV49ZK-2jW7yDrActToQ1XyayzAwHoqO9BX8GbzHZHCpQAwIsEGwJQmP5tiE8rlVEG32nFn1yiBgZ9Zffedg9k-NYkywIMHOXSBg-Z5yOeyvSrR0SuT9roLYyMXtSDbhAg85Ldlsu0Ly5lLCcNvtLFPQMAzupPX06nbw5j2I8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5638aa725e.mp4?token=GusvWoIK10DQ7EAT6yb6yPKVZPaEx_cU5uo9BkBjg6kdbK5jPaQup3Oe5Vi9tpWsWal8tny9xW6eNqUJeEKaZF8Loe83fcdDFpueSgVNwja4RtmQ_MEE15Mlm4LqNsFUCf4tl83fqXSUJMsCojdV4Wzw9fulZg1r8BUdZZpuYBfqeV49ZK-2jW7yDrActToQ1XyayzAwHoqO9BX8GbzHZHCpQAwIsEGwJQmP5tiE8rlVEG32nFn1yiBgZ9Zffedg9k-NYkywIMHOXSBg-Z5yOeyvSrR0SuT9roLYyMXtSDbhAg85Ldlsu0Ly5lLCcNvtLFPQMAzupPX06nbw5j2I8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات اولیه حمله پشم ریزون آمریکا و اسراییل به انبارهای نفت تهران در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70777" target="_blank">📅 09:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70776">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzM8OEkVYmNocR1PAs2EoNEC19YFUOeyz4INaJidtI9JS8_pFlXBlQUdGr6K3QgMy3iciWIi6Tg5wrv6lj40CD6ZxPwNyOuFpGZNGph1U54zxZQJOfuTI7zX4Okc6KpH8VTnACfM113cpZY6Rq-8cmPSeL_YrbFgBuGtCX7VRP0-4afyFLyLvryouotSsh6Saq4a1atPCbel7Syxovu_TwtuoQ1hQw5cd2BetXAjDjwqmR27mSowufT1ERz8qyAYEng94WQS_xBiwtwG0ZVkk8oyhQ0Vu79gTyEmyGUKK6-8Ix6-1qKQ0ZwU9eaAaEjZZlK_wnBlWgbshrzglWYzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70776" target="_blank">📅 01:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70775">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26b389410.mp4?token=jmeJMu4MU1D-0x-TfRXwllc2cXcwKwhwnOVY6-2J8ra2PFKYyiiCMKjjQCUC0d3UeqYyx2gmNL16jUaApE_BpEfPCn_Z8ZOadIsNZcbCGCARvENADduavoZKdprpBrfi-L9NYZFNRKM2bv_uZCIE8XSuX0kjrr__-muqkfvBp_uLR67_d4jqsSQahKZ0wUQ4X48RwerZc1EB3S3663ytE7qPLhU34yK7_MLGOfiyspTz3Cp5d8az1D3sBAtKouX3Ok62QhOUO5mETnVrK-N_JCCSt4LYvXZi_IHqke6Bq9rsfUXZYEBxHMgClU46lwaRavHFYc8GzI_YQD2tLS4tww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26b389410.mp4?token=jmeJMu4MU1D-0x-TfRXwllc2cXcwKwhwnOVY6-2J8ra2PFKYyiiCMKjjQCUC0d3UeqYyx2gmNL16jUaApE_BpEfPCn_Z8ZOadIsNZcbCGCARvENADduavoZKdprpBrfi-L9NYZFNRKM2bv_uZCIE8XSuX0kjrr__-muqkfvBp_uLR67_d4jqsSQahKZ0wUQ4X48RwerZc1EB3S3663ytE7qPLhU34yK7_MLGOfiyspTz3Cp5d8az1D3sBAtKouX3Ok62QhOUO5mETnVrK-N_JCCSt4LYvXZi_IHqke6Bq9rsfUXZYEBxHMgClU46lwaRavHFYc8GzI_YQD2tLS4tww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپِ هوش مصنوعی، تابلوی «دریاچه انتاریو» را با تابلوی «دریاچه آمریکا» جایگزین می‌کند و سپس با آهنگ «YMCA» شروع به رقصیدن می‌کند
😟
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70775" target="_blank">📅 01:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70774">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf25SKbrDD96AldMc4JGtZ31pKPPefyfqh_c5bn5cIWeSNJdEJl978gtkiGVPhWbuK0MJokRs2Lyi_Rvd1bAkQ85-qmbsa_fdlKMbdy95E9m1eaGDxlH3GgYmUad7gn7mtnr71C1FGD0SCFHjzCpFEqT_YzaBa0s2QpGffdezgcENAKLxpFuXx4FYd4Ux7NDuExFOW8nDqoViPDuWyk1A4VjGzBQrnsUCfp3WGu_oHz-Ph9tkvwshOzlJKiAWJbylAIzte1Sx0Zq9YbCKWzomLznkb3FBsC2Ty_kGKxPz2EuRTOrR1o2q5LYx7MCvBNTcyLsdUO05u8ETMXLH_EGVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
⭕️
باراک راوید:
دو مقام اسرائیلی می‌گویند که تصمیم به بستن تنگه هرمز توسط فرمانده وقت نیروی دریایی سپاه پاسداران انقلاب اسلامی، سردار علیرضا تنگسیری، اتخاذ شد.
در ۷۲ ساعت نخست جنگ، ایران اعلام کرد که تنگه را می‌بندد و هشدار داد که به نفت‌کش‌هایی که قصد عبور از آن را داشته باشند، حمله خواهد کرد.
اما به گفته مقامات اسرائیلی و آمریکایی، تنگسیری در پشت پرده دستوری صادر کرد که تنش را به‌شدت تشدید کرد: استقرار مین‌های دریایی در «طرح تفکیک ترافیک» (TSS) که مسیر اصلی کشتیرانی بین‌المللی در این تنگه محسوب می‌شود.
تنگسیری سه هفته بعد در جریان یک حمله هوایی اسرائیل در بندرعباس کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70774" target="_blank">📅 00:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70773">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7d12414fa.mp4?token=XkZlZkDwwWlIcqD0Vb0e0loeJx6eNWVFvnb37BznFU57d6LI1Y_ew_lLVop9RPVk0fPqGafXCyDQ_vp5vJJjOy3-NQPmo46JHjvhFIS_KtzDQmCl14tJUJQKn3x28ZTmP9xOJtp7fiUo0i5bxpUk52EHNheLBjVs7v7kA9N3S7LmYDATqpFahBRqUy6K8m5pdP3gHgZ458EmZsF7ZVQMZ1nRj5YMoM-5-eiVNfl1zkU7njCT_HJ5xvVSrpXokKnpPDMCrA80WevReNOP5bLOtOhmIjRjudvY3okKdEjBCgIXMHhFrqBph5_PZzr95f35VCUXM5BGOzfcVsTCIVwLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7d12414fa.mp4?token=XkZlZkDwwWlIcqD0Vb0e0loeJx6eNWVFvnb37BznFU57d6LI1Y_ew_lLVop9RPVk0fPqGafXCyDQ_vp5vJJjOy3-NQPmo46JHjvhFIS_KtzDQmCl14tJUJQKn3x28ZTmP9xOJtp7fiUo0i5bxpUk52EHNheLBjVs7v7kA9N3S7LmYDATqpFahBRqUy6K8m5pdP3gHgZ458EmZsF7ZVQMZ1nRj5YMoM-5-eiVNfl1zkU7njCT_HJ5xvVSrpXokKnpPDMCrA80WevReNOP5bLOtOhmIjRjudvY3okKdEjBCgIXMHhFrqBph5_PZzr95f35VCUXM5BGOzfcVsTCIVwLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارتی شوگر مامی ها توی ولنجک تهران
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70773" target="_blank">📅 00:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70772">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051d44837a.mp4?token=I-qIIDuX97UUPiKOMgbXuP3XXPCe2EohFSQAUa4Ys98Z0ZXuvPJfEDWWZyXBIm7MoXqfqpawKnFS5MdRy4TE5C4BbfWr7XnFSlblxHShwuuj7wKtqbKcvIj14hBuI9Nad0uPKcEK-V2VVzaPLsdbGkTnbJgaXLh1N5z0lj3GyCBvujXZXzmPZ3JRcH5Bzx35NSitsvZBTHCmEvUNUA_9VLBhU3avj93SvXnVSj-FAl8xDIRFqruDqdAnFN_wjfWHjALoo9NCE6lh_hsOyob3KZ0dD7Iu15kDAOGi6D9GWNVi3BDE9jSAk9-YXNp56ZIcySAzBtgjnqzS_Yy8-YwqSyeU4n1b6fgU7Kb6S1gpM6xV7SFYxouuBFhCYUctuv_gPTYFScLJ20pjyYisxjKKbge1ceWVH_vnuiO5NQffC-rl4ARdpO9drZ8EDL0qTof3ZwFGKbzjB59P8xbuxYh-k3WTtPfZsgNIQ_SQ_OrJJXS3DpG0xr0FyDrDnq_yziolbtcZ2ql6doQ8T62MB4oveGheXMNoEzpZOWliAQCJZH5v5ercywbMmT6Y4oIEgSznRr69DJ8tb0DwJWVnrXnE6xuFKsM0_bbAe1wIm97a0SIlzraNC8WZAhHplglmEuuDLnuvESOcE8rsvTlCjMZED6vtQXgplVJFD0sjPY-dw4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051d44837a.mp4?token=I-qIIDuX97UUPiKOMgbXuP3XXPCe2EohFSQAUa4Ys98Z0ZXuvPJfEDWWZyXBIm7MoXqfqpawKnFS5MdRy4TE5C4BbfWr7XnFSlblxHShwuuj7wKtqbKcvIj14hBuI9Nad0uPKcEK-V2VVzaPLsdbGkTnbJgaXLh1N5z0lj3GyCBvujXZXzmPZ3JRcH5Bzx35NSitsvZBTHCmEvUNUA_9VLBhU3avj93SvXnVSj-FAl8xDIRFqruDqdAnFN_wjfWHjALoo9NCE6lh_hsOyob3KZ0dD7Iu15kDAOGi6D9GWNVi3BDE9jSAk9-YXNp56ZIcySAzBtgjnqzS_Yy8-YwqSyeU4n1b6fgU7Kb6S1gpM6xV7SFYxouuBFhCYUctuv_gPTYFScLJ20pjyYisxjKKbge1ceWVH_vnuiO5NQffC-rl4ARdpO9drZ8EDL0qTof3ZwFGKbzjB59P8xbuxYh-k3WTtPfZsgNIQ_SQ_OrJJXS3DpG0xr0FyDrDnq_yziolbtcZ2ql6doQ8T62MB4oveGheXMNoEzpZOWliAQCJZH5v5ercywbMmT6Y4oIEgSznRr69DJ8tb0DwJWVnrXnE6xuFKsM0_bbAe1wIm97a0SIlzraNC8WZAhHplglmEuuDLnuvESOcE8rsvTlCjMZED6vtQXgplVJFD0sjPY-dw4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصویری که صداوسیما و رسانه های داخلی از آمریکا نشون میدن:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70772" target="_blank">📅 23:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70771">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006e88a7ee.mp4?token=jbzRZSVqqT4Lci7TMk4Yo9-wHuzI1STe5PrBvaAPzUjbu_-U68K5a24E3zHfX8l_F4fLRFp6WqDds8xMTQixY9pU_mLDaxCstRwnfeQOTqlIfqqEeSx7elfToYeN3wIvVEwENkyrWPEXYtA1942oXDhz7qKbBPIoP0OW4WELl8CzPLU6iKXUNn57ZVUqQto5cWd1dAN9uuoK_kaVzuVqbQakTgTCD10dbmnbG8VGSAyFLdivzSm2TPfcAk_PipNUeNSpOGzlUMq92x8AqleFqamNuTVnJUEKvZOthf9UycBAdHbEatPCWyFnYrFOmP6I-uz-ibN0Jcw1axbjoVvadw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006e88a7ee.mp4?token=jbzRZSVqqT4Lci7TMk4Yo9-wHuzI1STe5PrBvaAPzUjbu_-U68K5a24E3zHfX8l_F4fLRFp6WqDds8xMTQixY9pU_mLDaxCstRwnfeQOTqlIfqqEeSx7elfToYeN3wIvVEwENkyrWPEXYtA1942oXDhz7qKbBPIoP0OW4WELl8CzPLU6iKXUNn57ZVUqQto5cWd1dAN9uuoK_kaVzuVqbQakTgTCD10dbmnbG8VGSAyFLdivzSm2TPfcAk_PipNUeNSpOGzlUMq92x8AqleFqamNuTVnJUEKvZOthf9UycBAdHbEatPCWyFnYrFOmP6I-uz-ibN0Jcw1axbjoVvadw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
«میزان، رأی ملت است»؛ اما ظاهراً نه همیشه!
🎙
روح‌الله خمینی در سال ۱۳۵۸:
«میزان، رأی ملت است» و حتی اگر اکثریت مردم اشتباه کنند، باید به رأی آنان احترام گذاشت.
اما چندی بعد، در سال ۱۳۶۰:
«میزان، آرای ملت است»؛ «البته مسائل اگر مسائل اسلامی باشد، اگر در رای هم مخالف باشید، باید تو سرتان زد!»
🇮🇷
🎙
سال ها بعد علی خامنه‌ای در پاسخ به پیشنهاد رفراندوم در ایران گفت:
«این چه حرف بی‌خودی است؟ مگر همه مردم قدرت تحلیل مسائل سیاسی را دارند؟»
⁉️
اما همین رفراندوم را برای فلسطین و دیگر کشورها تجویز می‌کند تا خواست مردم مشخص شود!
پس چگونه است که مردم دیگر کشورها قدرت تحلیل مسائل سیاسی دارند، اما مردم ایران ندارند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70771" target="_blank">📅 23:02 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
