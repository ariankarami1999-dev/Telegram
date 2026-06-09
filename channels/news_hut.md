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
<img src="https://cdn4.telesco.pe/file/P2NsLXyJldXP7L6X52q6203ws2NgDAtTjUlDZDOvhVZp4P3jEiL8s9UoU4BgGCS9lJfUSqwQkmu99bIWLtFUHQlmj2KM0gDYQkRB5lO-_5RkoRy9piwaHHVtlInmpyi1c-1Dnzt8I62vuWlffNZve1VvuNgkOpViivJ_ooHG4fR_gq1eZbNH2Yveu6CReD2BE0U-ZpTYnsMC6ViX9EhM1qexogITrJirG1qssbu7B1A7Q8yCjrMfkXbpFUxPU6g4-9WvJPvmIsIYm63HHeUwS70W0stb9qP9Iwx5YydTnj0YrBGJRMUK0SJcMo-G2rOIgu8DYvhVEFFCvm_pxKvoQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 227K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 19:46:14</div>
<hr>

<div class="tg-post" id="msg-65546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
العربیه:
حزب‌الله اعلام کرد دولت لبنان باید روابط خود با ایران را اصلاح کند.
حزب‌الله همچنین تأکید کرد اتهام‌زنی‌های دولت علیه ایران برخلاف منافع لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/news_hut/65546" target="_blank">📅 19:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn-b1g_uaQHCP2unpjR9yrvz_EWVImhlZKxX8WGZNERe1lK2wVk6VMyZq_K9gvhxVpTxLay7lv6lhOC-kSSzgn38Td4sDS_3KAZ28_EwpINNkYO3iDsUKGE1QRANKHEWGdzzMscSZ_5yTHxbZlOP1z3zKPeEZkKIMI2BIYOGiJEruVDEI4z0WzzLT0KuDYkAi0uCfh89KzEf8lAXxKy2U5WoYGufF8blwmX76_nqP-hScVw1iorIsH5b7vPuZXf1xgsAGdC3C2L-0MP96vM-7MyWs4Yz-UWcLyTniIekgmvEI_NoF38LkfbApaF_t9Scp-i8akqkI-gwbjEj7Tn7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست جدید حساب رسمی کاخ سفید در X
@News_Hut</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/news_hut/65545" target="_blank">📅 19:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5-2uEF8KpZUyNsRPFCjTbx3iy7SdOXiocaslQro2YWlonnpeYIhbw2MQjGU5kbYbI0CAV4nPa_JGAyGrIBjSo3VpHiOpzjhnbY-VEJvPK3kbSf2DC-T5QYmjN11V4tjbGBFbmegvkD5uedfL5VaFMdD04YbDUrHiqaq9VzBOkzKSHPGbLhDLrgYH8yQnfXZ8jhE1UfJxYGKSXsL9bObfgvmxTyaGkQudGTniutBqGQvS1VDzgKjYMPJold1tKOv-GywvdNLuhpvkjJF8rs7lQUYAMJPuBGwWEb_fjebQnIys3gBI9E7i_MxVDeig6TdNNDPylTp5RvxO2AwhPmcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807b24fc4d.mp4?token=OGV_YRdssRKncwyaHhovSrCVIgODbH36Hz0uMUm-lzM61XmFD-SMeXO6CZGLDhPL48IQj6jK79Ztb9qk530uhAC2WrSBTAmvE86I58-RVC6Z3FLGpjsVLmMxhxGT6aTGn5JzVsNUvu1KgcLiKkOMpGitCknpRVZnmMKKh8MkaMgMsNUPBp5oFKR1x14KFuvHSlEndr4-PHBZ1oOg_A2DnZJXRPXLdu2zBQiVXEqpGYxKNEozYNpxTvT1UrRjpARuUxs3Rk3b_9Xh9gbOu0hrc6seodzYjH4aZpMrG-ZhxQFve097Yby1x3yIr0yy2ISVq4ZtiBJ1EXFzTWHKLBu2OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807b24fc4d.mp4?token=OGV_YRdssRKncwyaHhovSrCVIgODbH36Hz0uMUm-lzM61XmFD-SMeXO6CZGLDhPL48IQj6jK79Ztb9qk530uhAC2WrSBTAmvE86I58-RVC6Z3FLGpjsVLmMxhxGT6aTGn5JzVsNUvu1KgcLiKkOMpGitCknpRVZnmMKKh8MkaMgMsNUPBp5oFKR1x14KFuvHSlEndr4-PHBZ1oOg_A2DnZJXRPXLdu2zBQiVXEqpGYxKNEozYNpxTvT1UrRjpARuUxs3Rk3b_9Xh9gbOu0hrc6seodzYjH4aZpMrG-ZhxQFve097Yby1x3yIr0yy2ISVq4ZtiBJ1EXFzTWHKLBu2OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیروهای اسرائیلی در حال انجام عملیات تخریب‌ در بیت لحیا در شمال نوار غزه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/news_hut/65543" target="_blank">📅 19:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzaCheX66aYmYSyIFm8VDDdOpql2aY2Zpy_M0kcnvMdd3dLwraREDzxVUxPTEP55tjEknwIoP3FrfjnF8aQxzdxoIBHptdaI0f24fNqlTx9o6IrKnqBWr5T_-ptyhlmHGKs_b4Yv3xK3cO7NQ3d9NX2HCdsTbOLEs3mDnZX2oIogYmyEpcBkrL7zWd0tCHzG_i0Wd4tFSlWOscr3mGmGs2Mpx-Rtrcf7fha-TwMov5UrxltJx8gYrMweHz8DV5fkKBOSBw0xqylZ10xnzmSYVDmJtMdl2GUwV8mVcNjuIW3u__61rCdJn2cJTJ1ZtD6T1b-icL0Zrwqg2lshAUZBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوژه و اخبارِ موثقِ بدون سانسور روز رو از چنل [
اینترنت نیوز
] دنبال کنین
👇🏼
❤️
جهت ورود به بهترین چنل تلگرام کلیک کن
🗿
جهت عضویت در [
اینترنت نیوز هات
] با محتوای علمی آموزشی
💦
این (
مـتن آبـی
) رو فشار دهید.
🔶
اینتر نیوز گاد فادر
🔶</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/news_hut/65542" target="_blank">📅 18:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65540">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4KHnhwLRULKp3v9Ng5cvP9GF45ZMR5QUhFEYkgIA3yOHvfUrjqmX-WbZuaYo060zYSBZTLMhL7b-JPYLJTtROdH26Dm8ByrHdozbsvlj1i2HGxGV7NJZsXGlO3oSiIzhh6JhGH0BNcYisCvLmC3E2B2v0Mxxy123x9WY6xQHBF7N9t7xmq1f0KX4WUOTAYDMwDWRB-n4Mlfjyz2Df0BG1NAVQ4NESSuaGAgliGzveKAwAOyFU_F3KmCYUBDt2OveUTmfKNaHm7ry70JiWau2fLXqttJ6exXP2UZsZwbt4hw5725CCX0a2OkPe3KVPIyeX-sib2sYwSqTlxpcj2j_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f53e9fe1d.mp4?token=dM7D1y7r37nSZY2ZjxJoLxaEIAZhx05FRJc6bOk7eoIPGm2pg7xiEuc-8fQr0YfKGNpZ7x9PWUQy-HXCnjhfrSeQIUNXfXIglOIPc5fsX29Y7_TGDnTwa9suBotZxCdPXYfcn2VmIZXCtkBvIaEqq-hoO_tG1VDvm8BJbNfHaRuHFH6QByDtEVRVwJF615SML-C2DpuKXGOUc6QM-gkGCasPDosafYg9bd-ZwNxT9ld_FI7Mscw21EucSjJnZXC3nX0UMgA8OEWLw1IZzQM6iT211OWUbLCtfX5MTBeJDwMvths3tQyK8d9FWr37dW0RSS9yP7dZF4mgwRdZ-vGNjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f53e9fe1d.mp4?token=dM7D1y7r37nSZY2ZjxJoLxaEIAZhx05FRJc6bOk7eoIPGm2pg7xiEuc-8fQr0YfKGNpZ7x9PWUQy-HXCnjhfrSeQIUNXfXIglOIPc5fsX29Y7_TGDnTwa9suBotZxCdPXYfcn2VmIZXCtkBvIaEqq-hoO_tG1VDvm8BJbNfHaRuHFH6QByDtEVRVwJF615SML-C2DpuKXGOUc6QM-gkGCasPDosafYg9bd-ZwNxT9ld_FI7Mscw21EucSjJnZXC3nX0UMgA8OEWLw1IZzQM6iT211OWUbLCtfX5MTBeJDwMvths3tQyK8d9FWr37dW0RSS9yP7dZF4mgwRdZ-vGNjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر صور در جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/news_hut/65540" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65539">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl6u-Ds7n6UMyK_e4lqjNoFVzi5W9rTJb-25N0jB6PH52lurg0W-jxqPY6a6eoeOmRSner6QiV6FCIvhE_9IORTy0YAG37TejXgYPNSl5YbxNdpGnufFQBDqMnl1fwjcBXuWNSMNq0WkArTIv48sAMlZPIfTGpvWnxtgQyaSiCE-IIcGzx-Y4c4_tGhzoY-ZqDyiWRt70cGnhS-n2iT98AzcZj6wMqJNCnrUeA4ptpWA70uP_ZhJu26I2sfmCUwlfG59ooKYKDMH_ccPNazm0aLnOw8DQ-CXILnjZ45VvVAsLEUVAbFib5gygFNWosL23cnOcbTyemgaQfOz65TF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئیس ستاد کل نیروهای دفاعی اسرائیل، ایال زامیر:
نیروهای دفاعی اسرائیل هوشیاری و آمادگی فوری برای بازگشت به نبرد در ایران را حفظ کرده و همچنان حفظ می‌کنند.
تمام سیستم‌های دفاعی و تهاجمی ما هوشیار و آماده بودند. تهدیداتی که به سمت ما شلیک شد را رهگیری کردیم و به سرعت و با قدرت به ایران حمله کردیم.
حمله‌ای که در ایران انجام دادیم، آمادگی برای ضربه‌ای بسیار بزرگ‌تر و سنگین‌تر بود. ما آماده‌ایم بازگردیم و ضربه‌ای سخت و عمیق‌تر به ایران وارد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/65539" target="_blank">📅 18:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65538">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
شبکه الحدث:
نبیه بری،رئیس پارلمان لبنان به سفیر آمریکا اطلاع داده است که جنبش امل و حزب‌الله آمادگی خود را برای برقراری آتش‌بس فراگیر اعلام کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/65538" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65537">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv30-5M44R7FHgi2M0R4AuEPr5EH6VTWdcf8YDBLSl77LKcPLa7J3x2FpgW67DpWbGCAWdQCSZbKQ3Q6jJszueaI5jcx5GhzFPKRoVG3IpuReOsAmAfwOdFy4ow8ax6Hovfrm3dKgPFRoIUXQr1RkX1M0WFP-CaTgeiaYAe-_dk7eBqpLpTtsaG1cVV1IItBNtL8Xij_lkpvG0K7FFiXxMGOG8ju1MzEPO_05MRjj3gleQ_RT2IS28tUjRzcHawDquUGsmOk2eN00IeIy5xA2sBB1bkVWods3vW0rCC4XPXkS18zwck0CXCqs2uLChuHLsbbHmUj0OGkKkaGE-MIDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل در حال شخم زدن شهر صور در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/65537" target="_blank">📅 17:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65536">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
♨️
پس از اعتراضات اخیر دانش‌آموزان، تاثیر معدل سال یازدهم در کنکور مثبت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/65536" target="_blank">📅 16:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65535">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5vMd16IFSeybtqJZUKK6r-z-rADIZPVqG9QWSzOIwPq_zlIFQGMWcXR2QI2WarrErgeRKDazmkaqv13lY03l91b8tJAUA3GVckLb6ijUtPwGR1qYOUG98i4CCTkRD2zC0eZmEvfWqKhMONbrFKX5HQnZmIhkQJAePRCLi4Vy5QIQO341OOpfNpRf-ENTiO1r-nDbEOtMTYO-Cz_g0YYSpAHTvb6zIGDF2z7yBXmKkdUFq1pCZr0bjmjq4QyfxQS-OhnTQ8Z7frdz6KEUEkqMaGSqMXtlb2Bu3YwIhyLnWHsx6l0lKEir-yD0OzZ9dzLhQpZtVoVGSfEJADoCbvmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐸
خان میرزا بلاگر ایرانی در حمله اسرائیل به عراق کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65535" target="_blank">📅 16:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65534">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km3egB-XDG_WotW2KUlHjUMDTzJUpn-2dFPNuk7G0IsUwcV15JjsbAGKpErBjadSJ2-Tk-HGIxULnBxbGENjD64etvhJSvspVhTz5HWs3M66q4LKeNRaCsDaNE6ndsKdJqVmWz-jS-Gpl5DnTlKhLK9MySdPnE2YMwsS2xebSWjfJM3-uK35AmyorqFH1EoRL_cva-lIGlP1jWbYakn84AV3bhssWXmk6P4Zrrlg7r_x2_37S37SFtth4hi0w4_CB-qZFBbGB05SipQ7d7X7MTAlTs5fk11ncah7H7BNuOec4_qUfd0_fcuFgarFH8bvwWrCNdnFDvDcprgkMmf8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اکونومیست:
ایران و اسرائیل که برای دهه‌ها درگیر جنگی پنهان با تابوی حملات مستقیم بودند، اکنون آماده‌اند تا با شکستن این مرزها، خطر یک درگیری تمام‌عیار را به جان بخرند؛ وضعیتی که دونالد ترامپ را در برابر یک دوراهی دشوار قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/65534" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65533">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4903bc1d.mp4?token=f_sEOfA7e662wv_cj8TgBnCHG5c01mfl_2nH9sY_iQ7q8qqR1VrcdTbbI7LxyoNVbzmMtYoFLz8IbYV6a33BCMMAFuYCWf03ZUkMZnSBXz5OmzojrK29_gcziMk8UeU-X3cs9TR1Quc7gqC8vyuvPiQUOaJWNRNPj25ffAbCxyAeIkR5Px20saywVoOdmicm1K5F7Pn56Dqs0PJApcF1DslzHeCafoXiqE7D2aoKPpR59AJWQ9tHQML5AeMSmhXcfqTz4LF3TDUjkf3Y38X0Vp-yKBUFaayzL8KdXDjmbgrfoUX6codYkbjeAqotRQ0FLYyUUb808oP_PJpq8UaXRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4903bc1d.mp4?token=f_sEOfA7e662wv_cj8TgBnCHG5c01mfl_2nH9sY_iQ7q8qqR1VrcdTbbI7LxyoNVbzmMtYoFLz8IbYV6a33BCMMAFuYCWf03ZUkMZnSBXz5OmzojrK29_gcziMk8UeU-X3cs9TR1Quc7gqC8vyuvPiQUOaJWNRNPj25ffAbCxyAeIkR5Px20saywVoOdmicm1K5F7Pn56Dqs0PJApcF1DslzHeCafoXiqE7D2aoKPpR59AJWQ9tHQML5AeMSmhXcfqTz4LF3TDUjkf3Y38X0Vp-yKBUFaayzL8KdXDjmbgrfoUX6codYkbjeAqotRQ0FLYyUUb808oP_PJpq8UaXRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
❌
گلایه یک زن حامی رژیم (پرستو) از رفتار بسیجی ها بعد از آتش بس
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/65533" target="_blank">📅 16:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65532">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
نیروهای رضوان حزب الله اعلام کردند بصورت زمینی وارد شهرک های اسرائیلی شدند
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65532" target="_blank">📅 15:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65531">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
شبکه ۱۳ اسرائیل:
شورای وزارتی کوچیک تصمیم گرفته هر حمله حزب‌الله به اسرائیل را با حمله به بیروت جواب دهد
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65531" target="_blank">📅 15:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65529">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDR1AHo1D8U9D5ALJtMQptL1yw9Jj62QrAOG_fjL3nVN5D1YdiPzwK72zrQ7tkeUY9gDrYIN54tKIaq4XdRK9yPmNGHChzrO1-HdFo3_PacuOYQqzS0oPORlnmd1RZ7ESjB5Oj-17yVtCHEBTbluRAptDZGwk5JRsrl7qjXy1MZ74gQZPfvm2a2oUyMjiccjZnEXq2Bm-3YDKb6UQ1zIVTGn4OgEFmGnMdSJXmP3IWdQhw0kgLyW0TYzbUNuZ7qRmxLOzx27lONAotmj6VytNDEOnaQYp7Q8R2rAdAwcm6htCMF7jctxy4WTMUL3ceu1eqDF9NgDV_a0OYkQLfWb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHzXqbbY_k8iLZ7j73ooZpKBUFHsRSFNkAeE0qndpevylv3BdyQcR78dzzvjAlcKrqOBGbIlmn4OaFnzrTWW0ONStVvy95WaMo0ZI03i8l15dImOMQnYU96BS6duj6aMDHykEAoaRSAg9eRyQz8_ltQLIuwO0rl3HVQBxnhzbBmW9IvaY8_9OgjDMNFkebkUvNP9uVStpZ0fKeN9CJ8aaWgJvu07AxNJgupW1fi9Zx4wuRQ46gVpH_bGumJTHZUTaYh8AUKoqMzMTg8srzuHxn49jxmRebrQ7U_IWBcUO0L2oeHnC5rLMhwwXG7x3tt2WjbcTeDNUhBjjZj1FXfgSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
حمله هوایی به شهر کوثریه الرز جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65529" target="_blank">📅 15:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65528">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
ستاد فرماندهی مرکزی ایالات متحده:
دو خدمه بالگرد آپاچی ارتش آمریکا که در ساعت ۳:۰۳دقیقه بامداد ۱۹خرداد به وقت ایران در نزدیکی سواحل عمان هنگام گشت زنی دچار حادثه شد و سقوط کرد توسط نیروهای آمریکایی نجات یافتند.
همچنین علت این حادثه در دست بررسی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65528" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65527">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4b9120bb.mp4?token=Fom-W_bIVW0jlqbpwRINhgR6nWteUKojDszlJPDnxjgin26bAJYH1ZnS05RfeCjgGw0vbHK54lre8xl2kN-3aSZr6uPpJNdlFP0c0c5DVdFbk5HpqopjXSmGMuwL-hKGEU3JEFeQRjNrc1VT4TzbQ2lSns-tLhTX53DjM2V7rm5uFDI40Ww57ZtCWFY_C1vuQS7_6ZHVcBt0PRQ_mEAKCxcpIv5PUV_QPXFr3eBhbgEq0hK9hZZ-z9GWpluMOB1wNTYQRfFDvHUHWJJqOe4ebAgdGxrUlbB9E4poHl4T4EfLoNelvOUZtTB8bHtdJWY53ocOdoUW1SDvVJpZb98DuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4b9120bb.mp4?token=Fom-W_bIVW0jlqbpwRINhgR6nWteUKojDszlJPDnxjgin26bAJYH1ZnS05RfeCjgGw0vbHK54lre8xl2kN-3aSZr6uPpJNdlFP0c0c5DVdFbk5HpqopjXSmGMuwL-hKGEU3JEFeQRjNrc1VT4TzbQ2lSns-tLhTX53DjM2V7rm5uFDI40Ww57ZtCWFY_C1vuQS7_6ZHVcBt0PRQ_mEAKCxcpIv5PUV_QPXFr3eBhbgEq0hK9hZZ-z9GWpluMOB1wNTYQRfFDvHUHWJJqOe4ebAgdGxrUlbB9E4poHl4T4EfLoNelvOUZtTB8bHtdJWY53ocOdoUW1SDvVJpZb98DuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید از ساشا سبحانی حرومزاده و آقازاده‌ جنجالی حکومت درحال عشق و حال با پول مردم در خارج
تو این ویدیو به دوست دخترش یک ساعت طلای اودمار پیگه به ارزش چند ده‌ هزار دلار هدیه میده
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65527" target="_blank">📅 14:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65526">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
حمله اسرائیل به شهر ساحلی صور در جنوب لبنان  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65526" target="_blank">📅 14:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65525">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
فاطمه مهاجرانی، سخنگوی دولت: میزان قطعی‌ برق در روزهای گرم پیش‌رو به میزان همراهی مردم عزیز بستگی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65525" target="_blank">📅 14:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65524">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=rzrZ44NUsa55ziP7hUbDTmqgtlLo7dBvgyJm4D47uiPJLZjcGFRB97chKu4ee8iftBfzv8uCSoPDr32SJMzLZ3I4H_cLL9hgyVbyRNR916WTDd5eik94D2-1_T59D4g5Dxz3dLoXIUPFtUwjW1T2fiVJlth0piB2VvsM5Nee25rOeS1F-jsYVmzDON_d0anToM7KDGmjW9iLo5xYx_jnLOoEoFkpoNm-3M0o57S0m5sRODS_CSJjb2Dkh_QpNSjq9hGrb55sX6CDaql2uvHzqchHijLveylzxAS9OEzPhcrs9EGYTE9peOdVQRLgT8c2Z_DaRHfA7BZaqN2GN2DWO0ejYw8LgAE-_J8-uj9n7RfJW_pebnyZbr5-vMkWsQGiahcPKFLzLzqobWTdn_KVtzykusuGsznfOMP0YREkb0AnG3KpbhZbQYyIHbEyob8_yd-eLvThTbtBPgkYccj4t3k12QDWjFAanMaFXjLehl617ju4PZtIHllKL7ISwgl9NJhtvuKpCjaFdZ9lW6GBdjr9g8r2LIKUMtTIXdkeNvy4p1iSUp51NQ-hriaW2Op7n5tV4Bw5-zlgljc5NQyJnFEqSm5YfTch0qbdZviTl3-RxPXH_D5Z0tkmIeMdYVYOgqFCPznyKM-4ZuQIiBX_SZZsoI-KcsH6sATu0knP-j0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=rzrZ44NUsa55ziP7hUbDTmqgtlLo7dBvgyJm4D47uiPJLZjcGFRB97chKu4ee8iftBfzv8uCSoPDr32SJMzLZ3I4H_cLL9hgyVbyRNR916WTDd5eik94D2-1_T59D4g5Dxz3dLoXIUPFtUwjW1T2fiVJlth0piB2VvsM5Nee25rOeS1F-jsYVmzDON_d0anToM7KDGmjW9iLo5xYx_jnLOoEoFkpoNm-3M0o57S0m5sRODS_CSJjb2Dkh_QpNSjq9hGrb55sX6CDaql2uvHzqchHijLveylzxAS9OEzPhcrs9EGYTE9peOdVQRLgT8c2Z_DaRHfA7BZaqN2GN2DWO0ejYw8LgAE-_J8-uj9n7RfJW_pebnyZbr5-vMkWsQGiahcPKFLzLzqobWTdn_KVtzykusuGsznfOMP0YREkb0AnG3KpbhZbQYyIHbEyob8_yd-eLvThTbtBPgkYccj4t3k12QDWjFAanMaFXjLehl617ju4PZtIHllKL7ISwgl9NJhtvuKpCjaFdZ9lW6GBdjr9g8r2LIKUMtTIXdkeNvy4p1iSUp51NQ-hriaW2Op7n5tV4Bw5-zlgljc5NQyJnFEqSm5YfTch0qbdZviTl3-RxPXH_D5Z0tkmIeMdYVYOgqFCPznyKM-4ZuQIiBX_SZZsoI-KcsH6sATu0knP-j0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حمله اسرائیل به شهر ساحلی صور در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65524" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65523">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
‼️
مصطفی پور دهقان نماینده مجلس:
وزیر ارتباطات دستور داده یوتیوب بزودی رفع فیلتر بشه.
«در صورت رفع فیلتر شدن به دلیل تحریم بودن ایران درآمد یوتیوبر های ایرانی قطع خواهد شد»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65523" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65522">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c1be7dc2.mp4?token=vEoLhJe8LJWHiIM1ELQO-f5-KDkjCSVhzLWC4FAAQ5G_Cxna6zXfRTaAMGMWwPGoddPsw2yApm7cHRGQ8DjS6ssa6nwXcP7SXEvPqS8cDwDrFqmBPnIhFx2UkvIw-MUqMVsTcCRpW50A1nFPKuoMyWlB-FNy7qgvYIaaPT-Ti7_-QYkhdfqw7yd0eJ966GCXqRkhR9Jv7E2IXeYGjr9gdxQEDPM0Biv9ErJZ1ktzREr45j1Bk0X-kbWRHwYcaxafvP-WoNpUfk_tzDAo_iIZYWv8hD39uZZaglFuaCLbs6ptN2xIYcLnCQjl0c_JjzxOQabF231ewazABYllCo3k5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c1be7dc2.mp4?token=vEoLhJe8LJWHiIM1ELQO-f5-KDkjCSVhzLWC4FAAQ5G_Cxna6zXfRTaAMGMWwPGoddPsw2yApm7cHRGQ8DjS6ssa6nwXcP7SXEvPqS8cDwDrFqmBPnIhFx2UkvIw-MUqMVsTcCRpW50A1nFPKuoMyWlB-FNy7qgvYIaaPT-Ti7_-QYkhdfqw7yd0eJ966GCXqRkhR9Jv7E2IXeYGjr9gdxQEDPM0Biv9ErJZ1ktzREr45j1Bk0X-kbWRHwYcaxafvP-WoNpUfk_tzDAo_iIZYWv8hD39uZZaglFuaCLbs6ptN2xIYcLnCQjl0c_JjzxOQabF231ewazABYllCo3k5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون با کفن رفته تو زاینده رود و از پزشکیان میخواد وارد دولتش کنه تا مشکلات کشور رو حل کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65522" target="_blank">📅 13:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65521">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63397f42b5.mp4?token=b6Xeur1mtlxP1BbzxiG-RpvQp0XOZ9HdBJNzTtq-PysJEo3zrWyc9himyb4XtUYHOmdPV1zXQ7A0bEzYWfBrww1f12785BKlKJf8lihOwMxLCvrfo1Bm5K8iM2swONn0Rd7fRM6uQZmW23j0efO_p7WSWFbSPAe7Z3_FhyMo3GyZQqsBqKHVLu6quemv0MZGIPVBGw_u4w9WtiT59pDShvA5Otu3rL68vUckLPZu2fxXZvssQfRjjGc0Of5H_0nV5yIXQPChRWAKlwgd-NUfs9A5TtjJjNPrIWcirz9FG67_v9mdoZeyq3MhCBRzjfAGCcaKVffQsG4xNCtLOVLj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63397f42b5.mp4?token=b6Xeur1mtlxP1BbzxiG-RpvQp0XOZ9HdBJNzTtq-PysJEo3zrWyc9himyb4XtUYHOmdPV1zXQ7A0bEzYWfBrww1f12785BKlKJf8lihOwMxLCvrfo1Bm5K8iM2swONn0Rd7fRM6uQZmW23j0efO_p7WSWFbSPAe7Z3_FhyMo3GyZQqsBqKHVLu6quemv0MZGIPVBGw_u4w9WtiT59pDShvA5Otu3rL68vUckLPZu2fxXZvssQfRjjGc0Of5H_0nV5yIXQPChRWAKlwgd-NUfs9A5TtjJjNPrIWcirz9FG67_v9mdoZeyq3MhCBRzjfAGCcaKVffQsG4xNCtLOVLj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آذری‌جهرمی وزیر ارتباطات دولت روحانی و از بنیانگذاران فیلترینگ در ایران: اقدام به قطع اینترنت و فیلتر کردن جوابگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65521" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65520">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65520" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65520" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65519">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBaYm8qrsGgQr4YaVwUWw1pcmmhHcMUqdWHYVvX4t_MPW8ycwgCrTpqqM99YOjXrY1IbyTNZPFHctga1drP60cAmLLrVavRmvDLqO1uV49tj7ZefnCfA3AJ6HnPAfxlfOSGae9D_zSY7uVHuTY6Mv5_tZzIq5OUhTT1aoO5BpKLXp0t0YvHH2Zt4gOJQq-VkGoUmEnM9I41Y5csBCs0pX3saWVVIt5-PhXfcfKm-tQRnVY1m2MXm0hYrf73_Cth6PkE1iWR1_77pQfJ0Gs1F_dd-xrd7YwTncnza1QwFAmiUmReVH1_pzZyrrMg073XkbJcypcyuwfaCLQdKPIquEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65519" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65518">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd926c0a3.mp4?token=BbgB484KfhmoFwCTwMC-f8sjNlEygN9MnlxURApQlvHXUGld7uAOofCPp_QWQCJl4fBY6dHX7i1I3zugTyCurd1YwpUfkP1OwnhHYtEXq6tWOMmIHq4k9cSiPAObc8vT35aFUDGa7o073i4agwWKrtyqyJQcerfu_0khU_20OOM5mD6a4v172dOH-kiWAmJk--4aSXbtamLtZIkt2XHDny5cJlEr51BwmYZkNOwNwt35LFoz1BUol0UOhHNGSTZmTpnuC21ThDORO2BaoftFRS7SJpbrPDJ6gbnPeGyW_3vRL7eHIBDCdaMghJkFpyzi8llqVtC_Tb6yJdWIhmNF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd926c0a3.mp4?token=BbgB484KfhmoFwCTwMC-f8sjNlEygN9MnlxURApQlvHXUGld7uAOofCPp_QWQCJl4fBY6dHX7i1I3zugTyCurd1YwpUfkP1OwnhHYtEXq6tWOMmIHq4k9cSiPAObc8vT35aFUDGa7o073i4agwWKrtyqyJQcerfu_0khU_20OOM5mD6a4v172dOH-kiWAmJk--4aSXbtamLtZIkt2XHDny5cJlEr51BwmYZkNOwNwt35LFoz1BUol0UOhHNGSTZmTpnuC21ThDORO2BaoftFRS7SJpbrPDJ6gbnPeGyW_3vRL7eHIBDCdaMghJkFpyzi8llqVtC_Tb6yJdWIhmNF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
مقاومت فوق‌العاده یه برج ۳۶ طبقه فیلیپینی در مواجهه با زلزله دیروز ۸ ریشتری در این کشور
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65518" target="_blank">📅 12:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65517">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش باحال حمید معصومی‌نژاد تو ایتالیا از آخرین روز مدرسه تو این کشور که دانش‌آموزا اینجوری همو با آرد و‌ تخم مرغ و ... به کثافت کشیدن و جشن گرفتن
😂
اینجا هم بچه‌های بیچاره هرروز بخاطر تاثیر معدل کنکور تجمع میکنن که به هیچ‌جای هیچ مسئولی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65517" target="_blank">📅 12:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65516">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTwiLoIr7DO4cuszYNQUaNj4jMB3Polp0FcwBopFg0q_AWZPphyUKYGSmvqypcwdrZi1-rBg1lXg4_m8xsqNuS6wBKgUMBlO-6XhfbD6IZssXl8HwnbIUDd_St1IFTLU2PjDi42AO2shrhWWtBntPm5MbdHgLDtp2Tn7Gt4ueDjOGuOq5hH4XLW5JAr12bRd23vf07pzmGzfFsPcHn2U7cpgz6WEjGMZw7B8hSZiICy8wuCynu_gSyalHQGnZJUMHBZzTpep_BTyg4lJdef2Dnv-aAP0ivR9UN-99oZhdhgXDqFiZx7S_ezn3Qes3LjSa5AoyfWX56peDx8w4QPPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
سفارت جمهوری اسلامی در بیروت بجای مردم ایران اومده گفته که لبنان قلب ایرانه و خب گوه خورده
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65516" target="_blank">📅 11:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65515">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇮🇷
ستاد دفن و خاکسپاری علی‌خامنه‌ای اعلام کرد که مراسم خاکسپاری رهبر دوم ترور شده حکومت حداقل تا بعد از دهه اول محرم برگزار نخواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65515" target="_blank">📅 11:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65514">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
جی دی ونس معاون ترامپ:
مواردی وجود داره که منافع اسرائیل و ایالات متحده متفاوته.
هدف اصلی ایالات متحده در مورد ایران اینه که اطمینان حاصل کنه تهران سلاح هسته‌ای نداره.
ما می‌تونیم به توافق هسته‌ای بلندمدتی با ایران دست یابیم. ممکنه اسرائیل این موضوع را نپسنده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65514" target="_blank">📅 11:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65513">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد ایران:
اگر حالا ما برویم و بمباران کنیم «که اگر بخواهیم می‌توانیم خیلی راحت این کار را انجام دهیم» و دو سه هفته دیگر آنهارا بمباران کنیم، آنها دیگر هیچ چیزی نخواهند داشت.
اما شما تنگه را برای ماه‌ها «باز» نخواهید دید. اگر ما بمباران کنیم، می‌دانید، افراد زیادی کشته خواهند شد. چه کسی می‌خواهد این کار را انجام دهد؟ من نمی‌خواهم.
ما یک سند امضا شده خواهیم داشت که در واقع از انجام بمباران قوی‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65513" target="_blank">📅 10:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65512">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا از نتانیاهو خواستید که حمله را تلافی نکند؟
ترامپ: نه، من گفتم کاری را که درست است انجام بده، اما می‌خواهم هر چه سریع‌تر متوقف بشی چون آنها باید متوقف شوند.
این مربوط به لبنان بود و باید متوقف شود. ما می‌خواهیم کار تمام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65512" target="_blank">📅 10:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65511">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
ترامپ درباره نتانیاهو:
به نتانیاهو حمله شد و او هم متقابلاً پاسخ داد و من نمی‌توانم او را به خاطر این موضوع سرزنش کنم، آنها را هدف قرار دادند. آنهاهم متقابلاً پاسخ دادن و حالا درگیری را تمام کرده‌اند.
بنابراین، آنها قرار است فقط برای یک هفته دیگر یا چیزی حدود آن، یکدیگر را به حال خود رها کنند.
این وضعیت خاورمیانه مدت زیادی است که ادامه دارد. اگر واقعاً بخواهید بگویید حدود ۳۰۰۰ سال اما مطمئناً ۴۷ سال است که اینگونه ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65511" target="_blank">📅 10:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65510">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
ما اکنون در حال مذاکره هستیم و آنها می خواهند معامله بسیار خوبی انجام دهند. آنها حاضرند همه چیز را به ما بدهند. آنها حاضرند به ما "هیچ سلاح هسته ای" بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65510" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65509">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
🇺🇸
🚨
🚨
ترامپ اعلام کرد در دو هفته آینده "پیروزی کامل" را بر ایران اعلام خواهد کرد!
ترامپ: من فکر می‌کنم که ما در آن نبرد پیروز می‌شویم، اما شما واقعاً در دو هفته آینده که پیروزی کامل را اعلام می‌کنیم، پیروز خواهید شد.
این یک پیروزی کامل خواهد بود. خیلی زود این اتفاق می افتد و قیمت نفت پایین می آید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65509" target="_blank">📅 10:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65508">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
🚨
🚨
ترامپ درباره ایران: ما هر چیزی را که برای تخریب وجود داشت، نابود کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65508" target="_blank">📅 09:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65507">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=V2dz-pwYT9q2ABqzyU_k513A7fqrsbEsukPhC1eGZ3cS3uVq8Q-NcN4lOaU8ro_JCFELVzGi1Sy8Gl2BPDLwqoEwU1C6YqnXamv1IFkJHCiOxlQwe-mtq4thcml_QD98fvouctcePtbE5Tv4TSr143HAH5DVfeUUc1LfwTB01rvKW8wVgwl9kK2DIdkby0bRL3EzaAxG3kxrBq-TNqhHK6aVpiGqtTs-xYShCnrz8tlqWObibvyw-k55iLOhu8sSVboRos6Jdc7VU7Srr6o4Cxs2OeynTxpjICW-9NH7DXeIlWhqfNKhnQa9bRomBCuh_6e69tNQ2GU2WsqmA0_UGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=V2dz-pwYT9q2ABqzyU_k513A7fqrsbEsukPhC1eGZ3cS3uVq8Q-NcN4lOaU8ro_JCFELVzGi1Sy8Gl2BPDLwqoEwU1C6YqnXamv1IFkJHCiOxlQwe-mtq4thcml_QD98fvouctcePtbE5Tv4TSr143HAH5DVfeUUc1LfwTB01rvKW8wVgwl9kK2DIdkby0bRL3EzaAxG3kxrBq-TNqhHK6aVpiGqtTs-xYShCnrz8tlqWObibvyw-k55iLOhu8sSVboRos6Jdc7VU7Srr6o4Cxs2OeynTxpjICW-9NH7DXeIlWhqfNKhnQa9bRomBCuh_6e69tNQ2GU2WsqmA0_UGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چندین حمله اسرائیلی در جنوب لبنان، در مناطق اطراف صور گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65507" target="_blank">📅 09:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65506">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
🚨
🚨
مقام ایرانی به الجزیره:
واشنگتن در پیش نویس یادداشت تفاهم تغییر ایجاد کرد و این موضوع غیرقابل قبول است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65506" target="_blank">📅 09:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65505">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
طبق گزارش
نیویورک تایمز
، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65505" target="_blank">📅 09:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65504">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=Kmdn2Snyrn2J9NIoz71ifoUKnPaJ0iyGabyd6grE6zz_YzopbarVK1DUR_Tw_diri7bjhijp3spXoMOcGxP2iEvBFqYOanhGeYwTi3ODR5-XmfCnKTqPn-92ogZ9gtkx95uoP9yhfDvprS3e0ePcr4B_3tnSyy955cTbTr6wSrBIh7N1SsYsgJxPCptnlsqfN_J1B9I833PzjaLLlE37UbrWfI2-QN4Hq13mHRnlM437HwnNI7cLr49lITaoxOU1RmyLfbQCZOMg7aqa5KHxhiJ12-Wyqu-24qfoUMQJHe0euIjBL7AS6dvMNIp4PuNjP6wqCHfsSgIki0EAia6YvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=Kmdn2Snyrn2J9NIoz71ifoUKnPaJ0iyGabyd6grE6zz_YzopbarVK1DUR_Tw_diri7bjhijp3spXoMOcGxP2iEvBFqYOanhGeYwTi3ODR5-XmfCnKTqPn-92ogZ9gtkx95uoP9yhfDvprS3e0ePcr4B_3tnSyy955cTbTr6wSrBIh7N1SsYsgJxPCptnlsqfN_J1B9I833PzjaLLlE37UbrWfI2-QN4Hq13mHRnlM437HwnNI7cLr49lITaoxOU1RmyLfbQCZOMg7aqa5KHxhiJ12-Wyqu-24qfoUMQJHe0euIjBL7AS6dvMNIp4PuNjP6wqCHfsSgIki0EAia6YvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
یک کارشناس حکومتی در صداوسیمای جمهوری اسلامی: آمریکا در جنگ ۴۰ روزه بیش از ۷ تا ۸ هزار زخمی و دست‌کم هزار کشته داشته! کشته گرفتن از آمریکایی‌ها و اسرائیلی‌ها برای جمهوری اسلامی کار سختی نیست و ما به درخواست کشورهای منطقه خویشتنداری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65504" target="_blank">📅 09:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65503">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65503" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65502">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhmVmANRKti-GcOwZr7EwSxfG6X6606yEmTVm6rxBO6lU8AcO3IbYX-yFsGmFFUUNmgdi3ynDB0j-W-wrmi92FQlKtSs2__C_kCa7ChDVwB-kGQMO6YAW8-UXbvMqQ1-cp4fyhx5VAcDkPDokKEx6oflGI08UIP4qlbQExuuiDPm9hvLfGP8oM6dNBo5XrdsrxfdJTlbM6cOOszchWNrK2yNNBmkF3IWxMdPHl2F6R9bMfjt26mhUoQdSZtd0AZKQCz1YEBHuYY82Zi7LnAF2TSwtQA1Z8A2ssGWuhgxsix49IyE3jIzqFvOJVn6OdvAP12TMgYNldo6g7mqOH5ffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65502" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65501">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTLmvLE0Po-ykGoHbLtv5MBZYSI9Z--_u4EFjj9gvot3jcZ81uvLNMdF8KPOFnSau8Ysp4ZwUpRH5IZfn0n9Cx5HZIb-cWqleGPFl8vt1o_0TWJauW-ER5seAksnKNPyPksZGiED_qAl0tuASHwC61rOiLL1Ht7KbRdfxqIHTnTtTlcItd7uGXrXB-MyLKBd8jJgD8k_e_WT_tgFf-uzhW2vgvffjENHZ4Sm7t7DMVCUHFm6bvoDe6ozbidECC8ZGuyowG5zGy9QhRtnTfPrAoqQOKYT0E70gj34wfU1i8xRMy88ft1Wr0u2n6ArnfCuleuA_9uqJRbvOALN6unFUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
اونایی که
۵ ماه
پیش وارد شدن الان
۲.۵ برابر پولشون سود
دریافت کردن
دو فرصت
ویژه
در
سرآوا
برای شما فراهم شده که با بازدهی فوق‌العاده می‌تونه مسیر جدیدی به سوی
ثروت
براتون باز کنه
✅
اگه توام‌ دنبال یه‌راه میگردی تا بتونی درامد خودتو داشته باشی به خانواده سرآوا ملحق شو:
@Sarava_Finance</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65501" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65498">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
مهدی خراتیان تحلیلگر اصولگرا: در ۱۸ و ۱۹ دی ۱۰۰ شهر یا سقوط کردند یا در آستانه سقوط بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65498" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65497">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
♨️
🚀
خبرگزاری فارس: انصارالله یمن با پهپاد به سرزمین‌های اسرائیل حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65497" target="_blank">📅 00:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65496">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به اکسیوس: ایران می‌خواهد به توافق برسد و این اتفاق می‌تواند به زودی رخ دهد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65496" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65495">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7093313be4.mp4?token=AWXczFEfueWlF8WSeZdiw6b1T2RdGjcsX4DaN5X_KxYvvdo8KHQXrQguAoQRCANtRpobqbaRn_0jYaxd_WHM4dW2Exu_htjfgQdoBvURyJhpHjYB9Rb_nLcdHIWL5E4Ye_c5YqU_d5SwIVQkFXQpZtWVk4Ye0LM0HOwW36Ak-7wlen66B1_m6cklLwq7G7Pr2zVaSn-LZm6VDSDl6Qt_XvHhsINc8BBW4ih64unr5hYUYKcpGo-Oby2KS0cVB0bkaBmqQ6QvkgW_qZt2lGhovlM00YSBh7kIvFXsa33HBo5CslY8i54MuYbD5InVma9BRPq02K9fFbPxvhxBbXL6cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7093313be4.mp4?token=AWXczFEfueWlF8WSeZdiw6b1T2RdGjcsX4DaN5X_KxYvvdo8KHQXrQguAoQRCANtRpobqbaRn_0jYaxd_WHM4dW2Exu_htjfgQdoBvURyJhpHjYB9Rb_nLcdHIWL5E4Ye_c5YqU_d5SwIVQkFXQpZtWVk4Ye0LM0HOwW36Ak-7wlen66B1_m6cklLwq7G7Pr2zVaSn-LZm6VDSDl6Qt_XvHhsINc8BBW4ih64unr5hYUYKcpGo-Oby2KS0cVB0bkaBmqQ6QvkgW_qZt2lGhovlM00YSBh7kIvFXsa33HBo5CslY8i54MuYbD5InVma9BRPq02K9fFbPxvhxBbXL6cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سپاه پاسداران حملات موشکی و پهپادی به پایگاه‌های آمریکایی و گروه‌ های کرد در نزدیکی سوران، استان اربیل، کردستان عراق انجام داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65495" target="_blank">📅 23:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65494">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=ieWvw6SvbpreKnAda49taIFrnHxcSuUnIGtUcF9jztcFBkpLmd2uKfnEfHe24WyWMTo9owVO8h8pj0Isj4Xn8ygkXgjSapXm_IdqAHI9iIWPJt1DXYCs8q35Gb2QBv8iYkw3zLsztmr1K4qnOpDOSHvxbF_lrEUfItE0Fwo584W4460nOoduQIhiwWSRDy-BcnDbaW1FVfx_YV2hFiAtpxFEwOActw-a95Ig6zgQ1qtZtNLTEoTYIMpITc5rYPgGo-e2j6pgNJkhx8ZqhEppyZ0AMWSkX_xJIvOBSq67RafCvFwzXFUlS7uVe3UIzGrqmNhJSL1Ten-rv5PPDWiClw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=ieWvw6SvbpreKnAda49taIFrnHxcSuUnIGtUcF9jztcFBkpLmd2uKfnEfHe24WyWMTo9owVO8h8pj0Isj4Xn8ygkXgjSapXm_IdqAHI9iIWPJt1DXYCs8q35Gb2QBv8iYkw3zLsztmr1K4qnOpDOSHvxbF_lrEUfItE0Fwo584W4460nOoduQIhiwWSRDy-BcnDbaW1FVfx_YV2hFiAtpxFEwOActw-a95Ig6zgQ1qtZtNLTEoTYIMpITc5rYPgGo-e2j6pgNJkhx8ZqhEppyZ0AMWSkX_xJIvOBSq67RafCvFwzXFUlS7uVe3UIzGrqmNhJSL1Ten-rv5PPDWiClw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
رژیم جمهوری اسلامی با موشک به کردستان عراق حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65494" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65493">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
رئیس جمهور لبنان:
اگر حزب الله از تحویل سلاح خودداری کند، مردم از آن روی برمی گردانند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65493" target="_blank">📅 22:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65492">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
قالیباف:
هدف مذاکرات پایان جنگ و ایجاد امنیت پایدار است، نه عادی‌سازی روابط با آمریکا. ما نمی‌خواهیم از طریق تسلیم یا شعار پیشرفت کنیم؛ بلکه باید به دنبال پیروزی مهندسی‌شده با قدرت و عقلانیت ایرانی باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65492" target="_blank">📅 22:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65491">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
نتانیاهو به وزرای دولت خود:
ممکن است به چند دور (جنگ) دیگر با ایران بازگردیم، این پایان کار نیست
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65491" target="_blank">📅 22:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65490">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnriTGykiDe0B7te9kmZl4FGkMnpoWRRvDHsETggA1AukC4lJR_B2x6sSF0zyWMARy3EdTzxqf014_Ro_ZlHCOQre5-LIE_Do-EBofq8j7oAoAc2iiMIAj_xedu1pVp9SSLFBW3BPjSojr-AasSetxyzU00qbo-86JXtw8rpka7nTow-n5azuU0GuS7mVpbA-ySIWm1YBLdMUIp7c7tZcRKQXnUnmdpOq13vv6F3X80E9YCF2dC5f0hUS4HbCkminqobZCczigLeR7nS6zMRYsZzvpd4JGm11DTIB8RIIxTnFV1d3n3udu7BRT2NOCGm-UQf4rYu8TN8ykgBE9buzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65490" target="_blank">📅 22:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65489">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkdnSM57r79saKSvVWbjX-IzifwZqSdOuavSPalE2jWjbAGrIReohpe3hZPOtxnyLL57t4Lg2E7vSCvFU30-ckNwq8qyicbY0IgUJsewtUlhewgmt4Wrgz6arT0Zcaeh75bwBCp_MLAj5wtog3wOlIYPO3e0lMBQAvQaFrR46f0LrG0RA7jqa3A_sOQJn7Yh_QrDrml9aH0Ovv3V1SFHtSNCR-naMzO6pKaf0Rnx055UuTO5g7xmGCK9ZeeP3lqX70fALNXbpNqPEGizi-8Kvrq-cCt--J3NY4NDL2xQk5FxAjv6gFUpudb8K3Gm7PxdFnowQzwmvNzA_4ScJdLJ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
صابرین نیوز با انتشار ویدیویی از شاهنشاه آریامهر محمدرضا پهلوی سعی در مشروعیت بخشیدن به موضوع کمک به لبنان دارد
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65489" target="_blank">📅 21:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65488">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
مردم ایران بهتر از هر کسی می‌دونن که تا وقتی جمهوری اسلامی سر کاره، نه ایران روی آرامش می‌بینه و نه منطقه. صلح، امنیت و پیشرفت واقعی فقط زمانی به دست میاد که این حکومت دیگه بر سر کار نباشه.
راه‌حل، مذاکره با سپاه و مسئولان جمهوری اسلامی نیست، راه‌حل اینه که دنیا کنار مردم ایران بایسته و از تلاششون برای رسیدن به آزادی و پایان دادن به جمهوری اسلامی حمایت کنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65488" target="_blank">📅 21:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65487">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
این حکومت سال‌هاست مردم ایران رو گروگان خودش کرده و از جون و مالشون برای پیش بردن جنگ، ترور و بی‌ثباتی تو منطقه استفاده می‌کنه. توی این درگیری هم مثل همیشه، هر آسیبی که به زیرساخت‌های ایران یا مردم بی‌گناه وارد بشه، مسئولیتش با جمهوری اسلامیه. این رژیمه که کشور رو به این شرایط کشونده و هزینه تصمیماتش رو مردم عادی میدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65487" target="_blank">📅 21:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65486">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
جمهوری اسلامی باز هم برای حمایت از حزب‌الله ، کشور رو وارد یه درگیری نظامی دیگه کرده و بار دیگه نشون داده که منافع مردم ایران براش هیچ اهمیتی نداره
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65486" target="_blank">📅 21:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65485">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
ترامپ به کانال ۱۲ اسرائیل:
به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت!
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65485" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65484">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
ترامپ :
اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن.من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه!
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65484" target="_blank">📅 21:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65483">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
سازمان هواپیمایی کشور: حوزه هوایی کشور به وضعیت عادی خود بازگشته است و عملیات پروازی طبق اطلاعیه‌های پروازی صادر شده (NOTAM) از سر گرفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65483" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65482">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=t4SUEUPKfN4h6ZpQjKzvIqO67vLUeY2lfSfAzAu-Cj3tkYspPcAKf0wgHNBci_Y-TThTsDsM2liccb8Yvf3F2q_D7z63NN35mVQt0l9prCRCOXdo8z9nDJS_7AYrcEBiMROQA-aXWaeig0e9ZTbb1hc31B8J6KPb-PO4QSCH0Qum_oGhQCiN5odRxNRvBRRdE0JBCLWfGfD4i-u5P0GQa2H_5Tu6bZgbnymmNROtk3rttPntYiEMGeWrxElcZpKsCpJ7DzD2QNX-nN5wJ9OFTs5lUmVe9zGgELbV3JnU_-6DUQP2926hj0ONnkyAhqK1NTjFOwecIc7oKk9ZcJBHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=t4SUEUPKfN4h6ZpQjKzvIqO67vLUeY2lfSfAzAu-Cj3tkYspPcAKf0wgHNBci_Y-TThTsDsM2liccb8Yvf3F2q_D7z63NN35mVQt0l9prCRCOXdo8z9nDJS_7AYrcEBiMROQA-aXWaeig0e9ZTbb1hc31B8J6KPb-PO4QSCH0Qum_oGhQCiN5odRxNRvBRRdE0JBCLWfGfD4i-u5P0GQa2H_5Tu6bZgbnymmNROtk3rttPntYiEMGeWrxElcZpKsCpJ7DzD2QNX-nN5wJ9OFTs5lUmVe9zGgELbV3JnU_-6DUQP2926hj0ONnkyAhqK1NTjFOwecIc7oKk9ZcJBHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فیلمی از کشتی M/T Marivex که امروز صبح گرفته شده، پس از آنکه توسط نیروهای آمریکایی به دلیل ادعای تلاش برای شکستن محاصره دریایی ایالات متحده علیه ایران، از کار افتاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65482" target="_blank">📅 20:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65481">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUPwrb01o098LDA8fIgYxDlaWQBYlFZKyVA2cHbPuF_g0_XTsHcF2ZajStLV0RLI5xPdnkBxG1i2GHbY8N5FBdC88fMmXtZan-SQzK5GLF-HMzFSwXTU3jc-klmU38vhQB81UpKoGMHaGwKcc0kCbPA8KEdE3-cpmXyHfGWE4P0x9kbeEW89wFPAXYphkGTP2sVsQHQ_4Wu-tDX18ABs0YBSbMdOnXkLrusIiaHobtvPdJJrgW5frFdyne_dGjooWbkkDuODPa3YGX3n2O2LI3VwPbAgUK5Nsrdabh2n8Qnv3wEt7eq1rJ41T-H2m-IULOzJ7bjaqqXWTp16o2KGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده یک نفتکش بدون بار را در خلیج عمان، در 8 ژوئن، پس از اینکه کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، تحریم‌های جاری علیه ایران را نقض کرد، از کار انداختند.
فرماندهی مرکزی ایالات متحده (CENTCOM) کشتی M/T Marivex با پرچو پالائو را زمانی که در حال عبور از آب‌های بین‌المللی در خلیج عمان به سمت ایران بود، از کار انداخت.
یک جنگنده F/A-18 سوپر هورنت از ناو هواپیمابر USS Abraham Lincoln (CVN 72) پس از اینکه خدمه از دستورات نیروهای ایالات متحده اطاعت نکردند، یک مهمات دقیق را به بخش‌های مهندسی و فرماندهی کشتی شلیک کرد.
ماری‌وکس دیگر به سمت ایران حرکت نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65481" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65480">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65480" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65479">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL8cXvdl02CBwPmTItXrBAqYCVFuquQzcIDRgKdQvyS9XI9eppBl6ybt2XZ6zkiB_aq1R8PY8Cen8pR7zLx_Klx2_n4MCEk3AdSWHbKkm6XRt7y75QFlcyfzPlFxyGVJxjhmHpkOcNWbFXvj-haZ2kh_jVPRb_3I3hIZwBuygLLAWblJfVFExpyOqOkuPmZqbgXk6Utf5rb72QORfR4JDcJyn382hBc8KUrKR1wKfWPMBj0utnCZ8x3c3YV8W_1efGw3wkxYeR3lsq4yjUQKczkiTVXpAFwvQEjQI4LOvN7eESDRTjtomVIBmoYeOePVT2qgvSJz8s3OnmcZYQIMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65479" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65477">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
رادیو ارتش اسرائیل: ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
«این حمله گسترده انجام نشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65477" target="_blank">📅 20:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65476">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
فیلد مارشال ، محسن رضایی:
ایران از غنی‌سازی کوتاه نمیاد و در موضوع آزاد کردن پول‌های بلوکه‌شده جدیه. اگه مذاکره نتیجه نده، محاصره دریایی رو تحمل نمیکنیم و اقدام نظامی انجام میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65476" target="_blank">📅 19:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65475">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل تعدادی از فرماندهان ارشد حماس را ترور کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65475" target="_blank">📅 19:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65474">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران فکر می‌کرد می‌تواند به خاک ما حمله کند و ما واکنش نشان ندهیم، این اتفاق نه رخ داده نه رخ خواهد داد، دست کم تا زمانی که من مسئول باشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65474" target="_blank">📅 19:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65473">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2ukaoHWVsh6HmBEG6n82hTS-BNPJ90RHmJIfWixlmhXRRgsdP3z3S0fMXZcfXd2h8x0vpOkdRVD6k8tGmmGW5yDfu10RjyK-XOkQnYS3XusC_MVRq_ub-4LFRvuOV2gMYcnmnma0niPksKuQ-u5VxtGIn6Q6kSSxUSqsgS2AYKC59uUufvgKkaWMfB16aH6MwraU_RYVa75fh10ipRlm_t_knR8EubL5V3a60VG5Sbq0lUCRNwX7G4h-alJvine0USKOYjv9gboakZSm0w159OOskh8NEIebZpCqVbxgLs-BHiPoC2dtKh1VeglUvphWGzRJZ0mEOCFTlkmrVWM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروی دفاعی اسرائیل (IDF) دستور تخلیه محله زقاق المفدی در صور در جنوب لبنان را صادر کرده و به ساکنان هشدار داده است که فوراً خانه‌های خود را ترک کرده و به شمال رودخانه زهرانی نقل مکان کنند، به دلیل حملات قریب‌الوقوع علیه حزب‌الله.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65473" target="_blank">📅 19:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65472">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اگر رژیم جمهوری اسلامی اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما به شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65472" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65471">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
نتانیاهو در واکنش به اظهارات ترامپ: اسرائیل حق دفاع از خود را دارد
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65471" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65470">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اسرائیل فعلا از حمله به ایران خودداری می‌کند ولی ماموریت ما با حزب الله هنوز تموم نشده
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65470" target="_blank">📅 19:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65469">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=J9Ro6iXUN6Um6JtTxvZT_u0j3QIlD4zj-fHTwuYH5y6MGG1PMKCNQp1FJzI5xrnkSN3zywNbSxQf2Ww9mIrAfAnpXE-qOwWXNx9mhsykeLRwurX-BhG3X5K3r36PEZSAPziqw-OcaN4ICEkw0XoCVGh_5iOhCdFGp6DtxXLq0gOLN9_9fldvjkNa_mtl5HbkIYTn3hsTDANmvnnlT5325Lx87P2e3ol4M75Ia8Twtzx3y7--jrZ_mfqRRo-xi8OyRY2ZKZZi1B1AnlAq7Hj-Tw9240f6VEiSl2eKqBGmKW1zlewnsyxnDz2N5-o_NcpxRwwlrNMsnpegeSNkmQMywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=J9Ro6iXUN6Um6JtTxvZT_u0j3QIlD4zj-fHTwuYH5y6MGG1PMKCNQp1FJzI5xrnkSN3zywNbSxQf2Ww9mIrAfAnpXE-qOwWXNx9mhsykeLRwurX-BhG3X5K3r36PEZSAPziqw-OcaN4ICEkw0XoCVGh_5iOhCdFGp6DtxXLq0gOLN9_9fldvjkNa_mtl5HbkIYTn3hsTDANmvnnlT5325Lx87P2e3ol4M75Ia8Twtzx3y7--jrZ_mfqRRo-xi8OyRY2ZKZZi1B1AnlAq7Hj-Tw9240f6VEiSl2eKqBGmKW1zlewnsyxnDz2N5-o_NcpxRwwlrNMsnpegeSNkmQMywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ایران و حزب‌الله از همیشه ضعیف‌ترند و ما از همیشه قوی‌تر.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65469" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65468">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران معادلات را بر ما تحمیل نمی‌کند؛ پس از شلیک حزب‌الله به اسرائیل، به بیروت حمله کردیم؛ پس از حمله ایران به اسرائیل، به مناطق مختلف ایران حمله کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65468" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65467">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
نتانیاهو:نظام ایران پس از پاسخ ما عقب‌نشینی کرد و اگر اشتباهش را تکرار کند با شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65467" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65466">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو: تسویه حساب اسرائیل با حزب‌الله با قدرت ادامه پیدا خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65466" target="_blank">📅 18:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65465">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=DhuIzDziPEwPT1Dydx5m-YWDC8v-9f-5QLrL3iZrl_E6FI8eJwErG_CjgO-_aPq0jEzBCQiX0taVRRafg0wPo7v7AYG8W10jyk82xlTpp3XO2d-hQqbr7PGj1WDUAm6St78CLFnnTA_xiQ14w1I2CBwZkNCjqhPSwrngObpMnuhQYZCqHsXoR1aMT1hWLnCr-yi2ITq2VPQirVmhUXd9lfrI1JWeIBi_ji8AHCtd-rsVQPlfi8GgOdGVhsMHFVWzdBH_wWLg89ISmrZ33CoATHJRHkoMk80OV1qJr-dgm718ceLsNLtQGUjdhmxlHiTIXJOSkXLHawsW6C6x-fb_dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=DhuIzDziPEwPT1Dydx5m-YWDC8v-9f-5QLrL3iZrl_E6FI8eJwErG_CjgO-_aPq0jEzBCQiX0taVRRafg0wPo7v7AYG8W10jyk82xlTpp3XO2d-hQqbr7PGj1WDUAm6St78CLFnnTA_xiQ14w1I2CBwZkNCjqhPSwrngObpMnuhQYZCqHsXoR1aMT1hWLnCr-yi2ITq2VPQirVmhUXd9lfrI1JWeIBi_ji8AHCtd-rsVQPlfi8GgOdGVhsMHFVWzdBH_wWLg89ISmrZ33CoATHJRHkoMk80OV1qJr-dgm718ceLsNLtQGUjdhmxlHiTIXJOSkXLHawsW6C6x-fb_dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
سوخت رسان های آمریکا در فرودگاه بن گوریون اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65465" target="_blank">📅 18:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65464">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
بنیامین نتانیاهو تا دقایقی دیگر سخنرانی بسیار مهمی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65464" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65463">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل، ایسرائیل کاتز:
وضعیت در ضاحیه بیروت همانند شهرک‌های شمالی است. هر حمله‌ای به شهرک‌های شمالی منجر به حمله‌ای در ضاحیه خواهد شد. ارتش اسرائیل به عملیات خود در لبنان علیه سازمان تروریستی حزب‌الله ادامه خواهد داد. ما تهدیدات ایران را به‌طور کامل رد می‌کنیم. هر تلاش ایرانی برای پیوند دادن لبنان و ایران و حمله به اسرائیل با نیروی عظیمی مواجه خواهد شد، همان‌طور که دیروز اتفاق افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65463" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65462">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3210944dde.mp4?token=DMW9IJkJgTgUA8NhOPZFAL1eZn3HHdxNkonoeDgkJwQvOOLs8iqw6jOvWbsHdMtlwt8G5gbdBRodOaYYlwFwqvPGa3xq3hrH0Bp9MyEyaCxHb1_xsrCf4BLc8NJqEd-2biuvqyGrL4Too4JyMCXu05Vb_n44xEC21E2iH14AsogNV4qPTJ88Q3j4J29VC21P5gIKNOqNP1jlsXNZc_zF8kK7JZ1PKC9mPSY6ea6Q-_XV00-q8YZaCQg-SRSz6gnEwtakqJaqkrJagBeG1Jb_0ACeMcMVxQI5sXLOToDujNvv2i-Gi_NsOkV8PTLKslebDAmwza49JGwqneHH7elncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3210944dde.mp4?token=DMW9IJkJgTgUA8NhOPZFAL1eZn3HHdxNkonoeDgkJwQvOOLs8iqw6jOvWbsHdMtlwt8G5gbdBRodOaYYlwFwqvPGa3xq3hrH0Bp9MyEyaCxHb1_xsrCf4BLc8NJqEd-2biuvqyGrL4Too4JyMCXu05Vb_n44xEC21E2iH14AsogNV4qPTJ88Q3j4J29VC21P5gIKNOqNP1jlsXNZc_zF8kK7JZ1PKC9mPSY6ea6Q-_XV00-q8YZaCQg-SRSz6gnEwtakqJaqkrJagBeG1Jb_0ACeMcMVxQI5sXLOToDujNvv2i-Gi_NsOkV8PTLKslebDAmwza49JGwqneHH7elncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای از اصابت پهباد به مواضع گروه های کرد در شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65462" target="_blank">📅 17:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65461">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
اسرائیل هیوم از منابع: هنوز هیچ محدودیتی برای فعالیت ارتش اسرائیل در حومه جنوبی بیروت وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65461" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65460">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=fDxhkQqCoOQQDnEUlgbksCzHkkZPdhlYeingc7-Q0QoB2fQdDRUdVeb8MTqiVe425AppiMRphcJInyyE8FpadWR2mElXStIMdEAp2HRRYChNYg4EjzY2h8tHgeiYQ7e24Ssxav7G39DELupCs1zUPYwtnByf_1VrLpHn05JQwwbRgy6v8UbpuSb-2z04-iUCkL3d2JHfmyd6cryaFj06SIjawMM1E2T4IKq2prdNcYqBeuxvYR_dkOxJY5ankrj2YQzB1-d0v4FcBDO1B6eICRV3VfF8XsAiDSt7iMXwSByiTLPq3XMpd3lEbZtz2_JHDF5hOhGlbUIrZXmJ7jht5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=fDxhkQqCoOQQDnEUlgbksCzHkkZPdhlYeingc7-Q0QoB2fQdDRUdVeb8MTqiVe425AppiMRphcJInyyE8FpadWR2mElXStIMdEAp2HRRYChNYg4EjzY2h8tHgeiYQ7e24Ssxav7G39DELupCs1zUPYwtnByf_1VrLpHn05JQwwbRgy6v8UbpuSb-2z04-iUCkL3d2JHfmyd6cryaFj06SIjawMM1E2T4IKq2prdNcYqBeuxvYR_dkOxJY5ankrj2YQzB1-d0v4FcBDO1B6eICRV3VfF8XsAiDSt7iMXwSByiTLPq3XMpd3lEbZtz2_JHDF5hOhGlbUIrZXmJ7jht5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیویی کوتاه از حملات امروز اسرائیل به اهدافی مشخص شده در ایران
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65460" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65459">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5n7GQnm7njks5kyHk5fKiQJYl0-GeyLWiFBPCdxDgf-TeIoUXnthiNUv8za2pBB3qvl3bhPTB-WjejlMUbU6GTah0Pf4TkzTJ0fR0ZgsAsbHgBAQMGIBXgHFzK-Nja6eAHGQSCZENZdj9VAe1KYlSDJsiyT3jpwlA84RzEwEOxMHXBBPvYSP3Mf9ibbXfalPIG9Yr2ijFnYG1OsBLfpBrgD_1DVPQbs0ql5c8PI6za6dlvbJmyaDmaHdIEe9VRKbrQxe--POsIUmq93FOpN_7aG9_tob4V-9ImkDhVRSmIoKIEc98o51qW3V8NdW4oS7Hq-R17-uJtR20Aq1rKvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری دیگر از جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65459" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65458">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2BBl5kYgju6csnASPlN5HvpkhuSEu7EXVzmFYYjLz5nYBRyQp6fGdTCZuUtJ-7dq0bScupKUlZrchaoWzsYWNxYDpRFsourWQtX90_6TiuVnOohZ2earuS6BqdSLpGSFI3DIazQs5tgUma0ZhLYY3DLvwIgRs_F8owjGhnuD8tKxqkTTrFpjBbfpiiCQ4veGGo5qVgGVDWJW8BYO4RFug1-p7_wGiEXfKCm21PaQ6u701H8WpO9DzcAO0-lkO1Lwn5jEzke-Xq55IrxlKr65kRVQvUU5BckIk0LNqjS-n3FRahJeSHWAvohY8mq3xKJqEadvoAXx0xvMrgNTRjQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها حاکی از حملات مجدد اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65458" target="_blank">📅 15:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65457">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGbCK-lpeMt4FhS46uVv3IkjSxPxqPlHh9CzTxj6kU3expEorDpF2uaeijfOMW5rY7bjbRFSyQKlm53X5dpj0OmlYXyZw_OiCRjexmzm081B0IDqn-xsO2j7kaLpL8EAJzF2NV_tn4zuPDmos2h3mzj8dgdSKzv5_ZDSQzHPdrWV0UK63f1eGCuZxBHB7LBsTWLkF_y_1JOYnwz8i_Ty9aqn6yQb2zo_8ZC-bcEP-5xGlsyLJ2wmeYXsF54mYGMq7s5i3xcfIwUtkrqjpjN8HLQo96tOPbhfgKo88y3jmo7lY4ua8ADkVvP920jwku8rEiaz_vxcw7oWBOsDC5NJ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما پایان درگیری‌های دیشب و صبح امروز رو رسما اعلام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65457" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65456">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇮🇷
فرماندهی قرارگاه خاتم الانبیا:توقف عملیات نیروهای مسلح را اعلام می کند. با تاکید بر اینکه در صورت ادامه حملات و اقدامات تجاوزکارانه از جمله در جنوب لبنان، اقدامات قوی‌تر، خشن‌تر و قاطع‌تر از گذشته در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65456" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65452">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xg_XlgSnx3DNpNKqVx1vxFFHqiRe7OIjJwaExvWemtBdvbXLd2LpQY2bKJSfxWWPyAYOOr8_tmFnZRLNIuERileBYLzFFFw90740ajmrg_R2h4FR6Mzlj9MMtZGEEwT-3APDdO7hz5rW_OnIgP70Y7OCyUI4l1aCEPBHxFGmzQYGSUvwQoGLrROQ85KyGuARUcq43puF9IJ1RcqabajhTvK3ZAaO1bvUbi4D5ELelKVZaTfUiLkVVGSfrtI61Jwncah3ctWCSV3JfGMb1zK8f97U06VKIkCF3RH-IWwcOEdCSZT4O1EwmlnMEMRPyO_yxiwBMfaZZESEix2MhnTfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swa70tZtXh1_MzWHf_nRCwyPWVb2ISRfVEqiwndk8UdozbdVdOqFkvXXT_rmNnyH8SM9bA0TMNyVu3k4aTWaxvSNY2m2JyqgEBWdVwvUEm_7kkDIgERJXKDwhTB74Tk73_GgxJT-8blqpK5UM9ubfSG9HDBsti_pnrLf1aZczb-5k0CPKN2JoyG63NrpcPpWyZfg-AcV-CGOFQJaToQHO5kQKu_D_R_L_5KlfX6YH-NRS7kscL1xz2DOkoJmTlpP8Z4Aw8N2nm_qYLPSaf69MODCPsxsT_tI6MbWQar3Vjk7h7ZGRK7_x3JXJNz4zz6apqOk6BoRq5O3dNCok4wY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7tzpaOCixDqlpUy9yQ3VaXZOrLiVmPce6P6e-zFOjH2Xnk8vrMsQmdqwnDOqjDiEeOzp20BeMneDofw15MdBAALuuBrS9lDduUy-Cx_CeqRFY42LCEcRVqPnNuEjaeb9jhM-ApN3YwTXYgEMN20vJdDvoM39-I90PlTFbqJsHZ5SRCY8NKmP1dgeF6Gxkzf6Fc6GTTXL8YqkchxrhUke0nmtD6MaMN3rCIriUYhmOu6C9tWatnR76IjOqSkgWMqNF-Y9ojtFQnyq9fDTOASVS5eBLca63ZkD7kiithidElj0ulR22CI3xJdUevnEc0ryNs0HsMowt56Q_L86Gwbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSiIIx3i2XFTSwUe7ncQ4-5zfFdTKkcBHIGo_THF8TzIIvhLTyi1595e1qH-SLXHcFC8DPRQr00N8Y-0wvMaVAOQSzqm_Xd0Uo4JuPiy30Eo2kHOxfVgwZ7A9BrndomDI4z96GNYtfJWmR_2rGXLXIHpy9FwsBlKMUawdEBnzWeTJ0o9YEyzwsufITOty6sLuzBOCL0qcn7aVW-02W5PrQ06aJFYaUcgohJK6cGEsZWi_VKaDt3zwBkz7Z1W6xgK5PwQoEkTg6QYKkoMeAh3y3ZujwBt4gILFq6D4BvC0XkYTvHYW6LfvGfxSr88zCUYYgYcL4-OP1VR2GSDxMRsfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس
اسرائیلی
؛ رفته کنار یه پوستر موشک ایرانی که تو اریحا فرو رفته، وایساده و عکس گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65452" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65451">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگاعشون
⚡
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65451" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65450">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMlW3aChHMQltlw5_lB38Lwq0Yq9sD1sby4jb6ub5Auy6TeaG3pMNKtdUdg-MURQ-ihoa2YpsVpcZfcSWbQf7ubIMXL2cZ3xJYcBSrN-uHK9rDIJutTPjVQEV7m5bWtxfB8CSATXqV7qmk3fOdzYCkCxsFScYct79nEvPgPrp7O-rpHKip70wPCdSq6KAA7XyBuUq5nCFgg-N0rapMDCI3OzuErphO5114HeKO9aSblT_DeqFcEZD4bqbKefqQ8Bc2m5NmyESPKab1vtFEUZrLOl_7tYDxxD8M9URsGCms4f7Z_RdKXz2NOJ-eGDxKDDzuDQMRtpjWULZjNIdp4aGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبانی
🆘
کامل در لینک زیر باز شده است، برای دریافت آن کلیک کنید و عضو شوید
👇
👇
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک را لغو می کنم
❌
❌
❌
سریع بپیوندید
🖱
سریع بپیوندید
🎧
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65450" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65449">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8he3ARnAd7Y5DpxOBa6ZZgtoLdJPUrkWV2mdBX_L0VmV_6-wU4dJ8txh9_fGtjx_WCOH4G4JFv8QzvnYU0dZKLbCoDtkm68BL6nyLybWHvOB8tUNftUAp9UkG_8y-IUkPIm-4PSn0un8wcyaDEmiq8RNAUjQ_JgMtgpqmjtTtJBu-z2QdWVYxaW-Ch5pEx8bf4TytsVrKevF0T3-qs5yiU5tnNaH9cyiw2aSXwvjnGZxarjw8O2vLxVl0x0itcTudDibhi_CCrGxxQKkpr5NnAlQwwTLemORGUtpcg53vSJP7EK7NuOOQdJ_H2nTAWXCEmCO3K_pxhzjQE06zsElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره با قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65449" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65448">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65448" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJd5WcTv2PrpgtUxTt0uFqQMgvsulTcbOrvpTC_7vXyeiNYeX7A463UXXtkyyBzkt6Y-PI2tDrhNOpjDuQfQZSp3R39ebw468Bc1Cec5Ut7kiPynnIJHTQBs20-2rjwv7BMSna1e-wnSKmh5F_0YsJc4CpFaTZXZTxgy_SuI9HwJQ2_9_HbjBu94VD-ut22vZmRqqlInAZ3PFoCDb0ofuBIZaWCL8PFqICniJhNUDt1R62uCT1GPxyik0ojNY6aR087sHCVLS9uPHELgKL5KJf1gk_Fxk6D22ozx9zaVR0giz30CJopHOnm1rMEj13HxrLqy6UsUh0WGGQskIkKKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
دیلی میل| یک فوتبالیست بین‌المللی متهم شده که در یک هتل پنج‌ستاره در ترکیه تلاش کرده یک دختر ۱۴ ساله بریتانیایی را برای «بغل کردن» به پشت یک پرچین ببرد. پدر این دختر در گفت‌وگو با دیلی‌میل گفت که دخترش پس از این اتفاق دچار وحشت شده و در حالی که اشک می‌ریخته با خانواده تماس گرفته است. این حادثه زمانی رخ داد که او همراه خواهر ۱۰ ساله‌اش کنار استخر بود و والدینش حضور نداشتند. دختر ۱۴ ساله که از دیدن یک چهره مشهور هیجان‌زده شده بود، از بازیکن درخواست عکس کرد. پس از گرفتن عکس، بازیکن تلفن او را گرفت، اطلاعات اینستاگرام خود را وارد کرد و از طریق حساب دختر برای خودش پیام فرستاد تا ارتباط برقرار شود. به گفته دختر، پس از آنکه او سن خود را اعلام کرد، فوتبالیست او را هات خطاب کرد و درخواست بغل کردن داد. وقتی دختر مخالفت کرد، بازیکن اصرار کرد و از او خواست به پشت یک پرچین برود؛ جایی که به گفته او هیچ‌کس نمی‌توانست آن‌ها را ببیند. دختر که ترسیده بود، به او گفت پدرش در راه است. به گفته خانواده، بازیکن پس از شنیدن این موضوع به سمت دیگر استخر رفت و خود را پنهان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65447" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65446">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
اخبار جنگو تو چنل دوممون پوشش میدیم عضو باشید
😉
✌🏼
@Futball
@Futball
@Futball
@Futball</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65446" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65445">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-hjKxFnBmVJNF4E5YMrwbxcUY2_re1psIHUmqH4YXzcWnZ8nRpVlKOZar_uoB6UFe2VEkFe55k2fwmlf7X_QQ0zrGh0hVGmACjz9c0ftqaLmlcTdCe-gGtNy18A-tgRuHeVohnUZ2PrDKWvWxZNpxcSdwNpEVByjmNjc3cYZ-tN-dmHtsX65is7hQkf7CTp8_AY7t7WW0FT-qIEaQ7pB9Ao57mmRgMar8zh1MqhqLSlTer5QuBkOHrV2Dtf12nzT94hFHhkvz1m9-hszyb6e5u5SYTcn67AZY1zQNy_M-dP7biGce3cWZxbVWPQ6mY-yf4arn694qMxkhTrRdaXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65445" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65444">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
مارکو روبیو:فقط کشورهای احمق وقتی به آنها شلیک می‌شود پاسخ نمی‌دهند
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65444" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65443">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇮🇱
منابع اسرائیلی: حملات دیشب و امروز کاملا با اختیار و بدون دخالت نظر آمریکا بوده اما سنتکام در رهگیری موشک‌های ایرانی کمک داده
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65443" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65442">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=BnJpm2t3DN7BPlRjK1y5dd0g9M9osCyorqKIie_uWOxeKiUREUQWSjG_NvaBTNrrFV8b1pgZIjVonA8AjI9P6MrjRUjUin5amF2bhCMR9WZPT-ns3G7IVHxb-9ZLudIGTTEL-zlVVtw_NWhNv2xN61W7hE-6XUDiRmF9P80EyY-79r8VKXmRY80O9jfpYZLW4yD35DEWvuhggzALPfPDImlF6__JT6mAM1-a8oLY_FaOUqy11ZdVcn9T12ajCEUsUqLhFIB8fl98U5LDvxpeebocqhKnKTcLoqL3GFhKNR2hTOS_ztoXvG1T9IUyyPBNtus7OqabttNuofeTmJJXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=BnJpm2t3DN7BPlRjK1y5dd0g9M9osCyorqKIie_uWOxeKiUREUQWSjG_NvaBTNrrFV8b1pgZIjVonA8AjI9P6MrjRUjUin5amF2bhCMR9WZPT-ns3G7IVHxb-9ZLudIGTTEL-zlVVtw_NWhNv2xN61W7hE-6XUDiRmF9P80EyY-79r8VKXmRY80O9jfpYZLW4yD35DEWvuhggzALPfPDImlF6__JT6mAM1-a8oLY_FaOUqy11ZdVcn9T12ajCEUsUqLhFIB8fl98U5LDvxpeebocqhKnKTcLoqL3GFhKNR2hTOS_ztoXvG1T9IUyyPBNtus7OqabttNuofeTmJJXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
‼️
‼️
بدون شرح:
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65442" target="_blank">📅 12:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65441">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=XV0b3gWYayJETjfkSERw1Qf03MYymJpCvhp4ZsWsqrwqwPuiXbc3CM2xO45yrn_Ud9LDOHTWrmWJZw0G-_d8JrXTX8D6J6EwvJZ4yC3zRiJ7Qt2QshC5gSMmaWtix_7i6uvQ6q6SyCKMUvgnY4p8BiWERnAdzo57AQUhZWDIxJQXKTl0CNTDfAsqPKEDlcjbTpbXhuL9jq4pr3B2lYQWcYTChmVVnAlt_WtQrVQKC62VlMN4ilQAb0zPnfxVSDI9TdvEGlVaK3P2_o2b2fO_sJRIzVI0mKhRVCkx_HtNf2SsoHoa4kETX2bmXiY81Hsv2myMeqhS14v87xaaEKUqjKXx9tEUYPp6EAUwSCyNthGTa0yDhzqhZVPmdT4MCXAgWupbb1LtTdSdTmjy9-TSIQdyCXt_1b5bZCFXjcCHoEsKBZk8uM6h_JlK9X16iKvHtHQ9PBQJPlFdbWP252Iae-6DoDzVdRrdqZBi2lVdBHEeIVEasUqzFKtjH2bQ-3s1Eog32KApGHElIHE53tFsVxPB6kLvRUTfZMIsPcwREh2_g4fUEVvVfrWBLF2NvITIYElAiMgzVMDTZZ7LbJPgS4mda6ui8Yw4w21ne3RAmPjnyooL0h7nVqEiGPTn-31Omgntt1jDrxGHBSrn80MRgVq0bhtGZjYTG4xHKGqYu3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=XV0b3gWYayJETjfkSERw1Qf03MYymJpCvhp4ZsWsqrwqwPuiXbc3CM2xO45yrn_Ud9LDOHTWrmWJZw0G-_d8JrXTX8D6J6EwvJZ4yC3zRiJ7Qt2QshC5gSMmaWtix_7i6uvQ6q6SyCKMUvgnY4p8BiWERnAdzo57AQUhZWDIxJQXKTl0CNTDfAsqPKEDlcjbTpbXhuL9jq4pr3B2lYQWcYTChmVVnAlt_WtQrVQKC62VlMN4ilQAb0zPnfxVSDI9TdvEGlVaK3P2_o2b2fO_sJRIzVI0mKhRVCkx_HtNf2SsoHoa4kETX2bmXiY81Hsv2myMeqhS14v87xaaEKUqjKXx9tEUYPp6EAUwSCyNthGTa0yDhzqhZVPmdT4MCXAgWupbb1LtTdSdTmjy9-TSIQdyCXt_1b5bZCFXjcCHoEsKBZk8uM6h_JlK9X16iKvHtHQ9PBQJPlFdbWP252Iae-6DoDzVdRrdqZBi2lVdBHEeIVEasUqzFKtjH2bQ-3s1Eog32KApGHElIHE53tFsVxPB6kLvRUTfZMIsPcwREh2_g4fUEVvVfrWBLF2NvITIYElAiMgzVMDTZZ7LbJPgS4mda6ui8Yw4w21ne3RAmPjnyooL0h7nVqEiGPTn-31Omgntt1jDrxGHBSrn80MRgVq0bhtGZjYTG4xHKGqYu3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
حمله شدید پزشکیان به رسانه دیکتاتوری جبلی
: صداوسیما هر روز شعار می‌دهد اما باید واقعیت را هم بگوید
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65441" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65440">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65440" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65440" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65439">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_DDg5M9Z0wxZLzkyzHSM07RKRHh5SipHR3k7jpu2WcXrP1WJTlpi-pbiIdaLEdy-XfErzzzrEpOVz-rQC7mobYGeXzWJQwlUY-7YTiUAPCiCynju8HKnUdYg8aNP31kTPHiBVZF-58_jG8-GATRIsZlPe0QU6ttycK4HOvKvv5u12Wbl36Lw7Ym--Upe4pOCYatTp6YFCrlsOUOotW1V9RqieW7SSHb2gKfBwII4fFSpk5xIDvXpTh8MCmYBtJecpFTKxQmK_10MEq_3MkKFydJ_ny5TZs32_QfUEHvy82jU5jAf7XVhlk7S5ua58lwX-Uj9kcqCvAzYqtKErmV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65439" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65438">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری‌فارس: سپاه دیشب در حملات خودش از آخرین نسل موشک‌های خیبرشکن استفاده کرده و تونسته تلفات خیلی خوبی از دشمن بگیره!
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65438" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
