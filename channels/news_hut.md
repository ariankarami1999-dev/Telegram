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
<img src="https://cdn4.telesco.pe/file/A30rNUImDgbZtrdOEwN72fCZhlVSAC3wdWgGmZ7NZiExaSq_rHFn25IQnVS_19CDI_IloM-GFhqATBKOJ4REVyLgL_t4aVRnKrO5G0efEKaPCkMs9xPZ8pa9byzR-yC8F0VA0ypehS36FKpfsZlJhQWaBDF1E0yRqN9N1kfKB4ljtxavlSTEXcw5g5uNZtWAYo6xQWlVB_QXt-jCKgWq_WMo7NUvSRxiV6SkRmipEydCq1skjoxRcxiBuUerfGOKYCr1680l0VN6SBnJ4Yeh2ofaa8KuJmn87BObUInvQvZeBBWu-6iug8XnjsyJ8WQtt-sWDTKnkWouc2Loh_5kiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 173K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 22:34:32</div>
<hr>

<div class="tg-post" id="msg-68107">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/news_hut/68107" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68106">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMani</strong></div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/news_hut/68106" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68105">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2TwhJzFnrRxG1L6dE9n5BAUPAW-hDPW86LCrEDuPiJzzvKXk2PMGqlMJ9jIPiNRn2fhNXHOVYJpsYWS-8uTvw_EJTOGGlgD9TK-3_t1hqDP_C15eSzf12BGFx0CqUwqLa2MM9MeHpksv6Ijo0qQ_cNze62wwgugNPiAVUobBzCruY4LGtXRXbAxLpVygQCQZKB24Yr7Wxus2cd7CTkDz05rWbCL0mIHqQNiPTDxPY8Gya6YXmJkVm918l_8zSlIRVB61HLC5RTCudvZzxm-RJMz9-8qwf7SP0i8GLcyCgPNVE8bMuloHxqsHDDZ0c-eKEPUWmcxyWIawIuFbBnLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخه من چیکاررررم
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/news_hut/68105" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68104">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁪⁬⁮⁮ᴹᴬᶻᵞᴬᴿ</strong></div>
<div class="tg-text">مرسی که تک خور نبودی
💙</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/news_hut/68104" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68103">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNf8gMM58uwy33PJQdDUwUUWd9UwQp29MiOHnETvu1SUNlcYxWIItD6uq0CDZfIWdE3s5f10ZnmK095J2REX-KuCnGSkOzJreO8RQcoewuC_DmiJG8H-Tv1wMxEfLtD_HnMhhlpV-oEGTnTu1n91HSM2wDx30HL_qK6ipF_Tfi1u7jQfJrl6r2gZ9Q3m87iUmmDhUg-yEIyQiX5x9LkvD6ziJdRQ1BtmIgnqribusBAdhzu96rIOOsQJKzzFz7NxJRJC-xS6jtMlE9ZgLoFpnweZGLHraHTqMUxrIt9GGmaTiHBxXTWJlLpHf7x89XoKUTTKk3CrbalVdR27Q5a_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/news_hut/68103" target="_blank">📅 22:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68102">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⏺
رسانه‌های حکومتی:
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/news_hut/68102" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68100">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m81fjI_D88be3YxCJOwOCgWPLo3g5fYjak95RZi2JMHe4i2iTtD7Y9sis2q8fuJkrIatrSLdylFMTDgi8KxV4CZ85yaQuzg82QnfUqQHrUtevcciLTElP2Z9z87RUQp6bMPXi1dxEOnzQZ5abWV6tKjsRmUtMXJl0W3MeYyu73jo31J-EWDw-ENHuk4tcX59npZcy4yIImqtnUuNbky9BOGLx_TAWaMADUftbMGM1-f9GtIYTVCKIBjZp-bGr-DlIJMi8kq9dVePbcNU6w8L-75VQTjmRK2FUnTU25ccmtP41Y4mpsirs_8njT-uJnASpEdktTh8Q-vkPN3y4pEnaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHt9I5gaWtQOlfCQidwsxATO1nzhwzvNlBe0nzCiV22aR9APLCilbcaTLKadkQZK9aSKU1LzaGbvhj16Xwtn4NJjjLhESIoElEUEgY2cWLDC4jctDWNye4UHlXTO-zd1jTs5jAT0_Xs6Rofd1dyqgFJq9qkn3PAGAf98jm-4W4OGdoIolen3pMci4EBoDDA1OzOZV2oNgGuQu3CLFshYe9Ov1hBzzeRF12eFWJ-OWlDqh5oDRwdSzSNqWtzTdLDhbWKSfbF7ZKFGjrqAIQcjemVNjEUYN12MTT1q3EK1iHqj9nlxmxMe3CcmdwbtSfsNrcVkOqWgX2j_Zdi-A47B6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/news_hut/68100" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68099">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXv4mrfMfTQDc59oJit_G4rkeZ1PpwLdJbk5P4lsGq0roblAhp3WSFE0RULEnhDhj6oG7UhxZKcSj9_MplNZMH5J9fstdUOgq-DnQ0kyCwUMmwU8NBIwzxWav5keMuhdclIGP_ewQCoYIi4jEJvaYOeb5NZQS8xLHqwAf-zc7Onv4tAgHp1RA3FX3zMNW2a23uWeHrII0gZmNwySR66emuli7s5bD6veQg6jFcBKXL32Ic7m3hpSyYgNJql7l8YznGXKtviDv4DjUok4E8uaQIva7tfAVlhOrBrmMv_0x-U5xKdj2h0lMqNelFYriH8vD4wIki_bo_-ka3z3L8A8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پزشکیان:
‏در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است. امروز نیز مردم نجیب این دیار با صبوری، ایستادگی و پایمردی، روزهای سخت ناشی از تجاوز دشمن را با عزت پشت سر می‌گذارند. در کنار و قدردان این مردم وفادار و مقاوم هستم.
همه جای ایران، سرای من است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/68099" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68098">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnnBFoblak4eTOWAx2GcRD2FmPuA7awHBK0uMNK5y3Lcjb1OtYB7nC-cdFJC-EurFEqUJWwJWsIk0ArMS2K69I3735hqvWmyZSB2PQEDOLmS4nQdevoUARh3n_MBciYgDdI-q3l50w4QKJTOjLrQdz6wG8hnEEFtm-T60W-oDDmwvFqDQhXCAYyScBGeDqFdMQxwCC24yl8qssEGmdK9Z_kpUmJlITGvdM4Mzti8aZIZ3VdeSHo84Mq5c_A1OCvp8OWEy38aEbsx-X8nWSQUAA4jZG5Fm8pGW5VZk6fxMEdLhGw-IGPhWhZvZmxuV7byZ4aW6rsQU9YDVRRs-jwQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/68098" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68097">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=kWqwW64a_LJBebhhCOh0AS-VyripCbLoJb9_AHYRD8bs5GoVLk9Vk2JKUJCU2octsRvV50TP2JzOH2Lxn_aNywNB4-wQ_0IBersQ8Kz9QSw5rD7FeBo9PqbnFJ3WqZtvOcZNCypuUHSgYn8YUCjnvMg80qIjVOtfnoQZHa4R_UEqIdZzb3NVnqG3LY9mLu_oi2exXOGJYQxPQg6VRzlwpJ8hcpap8wOV7Q6gu9Kc1jfpaUL9vXlgXReIDSyRxhxsaXQzlaJNkjoFzYMsD1ZdKnE35lJjMUn3DjkQWf9yLHonZQFXpKUVKUi9QTO7BABlg1r2Qau0uWyZJOPIGztkJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=kWqwW64a_LJBebhhCOh0AS-VyripCbLoJb9_AHYRD8bs5GoVLk9Vk2JKUJCU2octsRvV50TP2JzOH2Lxn_aNywNB4-wQ_0IBersQ8Kz9QSw5rD7FeBo9PqbnFJ3WqZtvOcZNCypuUHSgYn8YUCjnvMg80qIjVOtfnoQZHa4R_UEqIdZzb3NVnqG3LY9mLu_oi2exXOGJYQxPQg6VRzlwpJ8hcpap8wOV7Q6gu9Kc1jfpaUL9vXlgXReIDSyRxhxsaXQzlaJNkjoFzYMsD1ZdKnE35lJjMUn3DjkQWf9yLHonZQFXpKUVKUi9QTO7BABlg1r2Qau0uWyZJOPIGztkJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
👈
مهمات خوشه ای شلیک شده توسط سپاه در آسمان بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68097" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68096">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سپاه پاسداران به بحرین و کویت حملات موشکی و پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/68096" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68095">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/68095" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68094">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=aFup_udgQ2t__XVB_VNQXXFvEjclru8urH7ctWXtE4G7MnltSWC2VjS5Bgx9lrivPJXE8-IIsQ9a7OPbL0UztGX6B9oTN-clKSGua4uNxW0FwGop2yBbhSw8PhzCc2ANMz9hIx-1uhIZGstpWbvo23KiPgXdi-gNOKRYY8aYNC3qjNHZMJTZZ97Vj5DqiFDLrewWnQ0ixe_K4qTZenVpRhp0NXCkTUAWq61RPA-ZjiqP_DUth9rEx6NQXBZyUFutYp0PQYhT_kxBiolchU-LQJaEoLbDEVjXYtfhR7Ww1UHUGMFY5TrKJeC-RPMvM53GGteapap1PCbdcc27lIpumw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=aFup_udgQ2t__XVB_VNQXXFvEjclru8urH7ctWXtE4G7MnltSWC2VjS5Bgx9lrivPJXE8-IIsQ9a7OPbL0UztGX6B9oTN-clKSGua4uNxW0FwGop2yBbhSw8PhzCc2ANMz9hIx-1uhIZGstpWbvo23KiPgXdi-gNOKRYY8aYNC3qjNHZMJTZZ97Vj5DqiFDLrewWnQ0ixe_K4qTZenVpRhp0NXCkTUAWq61RPA-ZjiqP_DUth9rEx6NQXBZyUFutYp0PQYhT_kxBiolchU-LQJaEoLbDEVjXYtfhR7Ww1UHUGMFY5TrKJeC-RPMvM53GGteapap1PCbdcc27lIpumw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سر دادن شعار مرگ بر سازشگر در مصلی تهران
صداوسیما هم چندین بار صدا رو قطع کرد
🤣
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/68094" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68093">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=Xx4Yv0hUksA2qSM0omHTBuQeFXYsZsLeMJ5IJaYaobIVYv0mSBS2-inR8sTbmAtPPPN5-htNuJf0VxdU1kioGuuyTUavDPkoZceMAKgCK8etuJv78KRdVcHlbYIRelpdAeAX7gYv65KiAFw-bJzmJy385D5YCGZKNjFBOeFX75_6YPdlgQ6BDeAdCPetc3OlDeJ4vCxgO49tmHsmHeEpYaMwYOQ3m2ACEQHfRhrFRGq3qKZQ_WInZ_oxXdCePAAf_pDbIpv_Xi_fo29Aotx9kBdFGPmaAUiPYaMQ0OzudUFh-L_EVwErbnnInwyA5KDyqR0ESfPCTwWBm5j6iiplDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=Xx4Yv0hUksA2qSM0omHTBuQeFXYsZsLeMJ5IJaYaobIVYv0mSBS2-inR8sTbmAtPPPN5-htNuJf0VxdU1kioGuuyTUavDPkoZceMAKgCK8etuJv78KRdVcHlbYIRelpdAeAX7gYv65KiAFw-bJzmJy385D5YCGZKNjFBOeFX75_6YPdlgQ6BDeAdCPetc3OlDeJ4vCxgO49tmHsmHeEpYaMwYOQ3m2ACEQHfRhrFRGq3qKZQ_WInZ_oxXdCePAAf_pDbIpv_Xi_fo29Aotx9kBdFGPmaAUiPYaMQ0OzudUFh-L_EVwErbnnInwyA5KDyqR0ESfPCTwWBm5j6iiplDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب ترامپ درباره تحقیقات اف‌بی‌آی درباره مرگ لیندسی گراهام
⏺
خبرنگار:
«آیا می‌دانید چرا اف‌بی‌آی در حال بررسی مرگ سناتور گراهام است؟»
⏺
ترامپ:
«نمی‌دانم چرا، چون فکر می‌کنم او مشکلی داشته... من شرارت زیادی در آن نمی‌بینم. می‌دانم که انواع و اقسام تئوری‌های توطئه وجود دارد. فکر می‌کنم اف‌بی‌آی وقتش را تلف می‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68093" target="_blank">📅 19:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68092">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=sz2CxIVdZk-jvvNX0CxgMjs8eJhJ-74JDChC1w4oXnDPlW2tDBYuUWdhhLvOddtdyf8G8MnfmcQo8zG65xEN_IhXdiuV_WG0ppzr4dheGytJrOwZQ1Hd05FubqRVusdIOeIxP6XzsTDtC3NYQdIHE_TnV2VQFQV6XoCI5U28VG4BMKqiOI141ZZTbYAvu7tf18vbAEzvahxhlwuRa5yHQ-WjhK9thwncyEHHzVEGEkrGouTvH-RLjUjNFA_VgGsIgmeoMF5x2TPXNnVsDIedDcwcSZzzfq4qkRGUHyEn4dTEh2aVMDvMQ10-1YHE8zBlhmHWO98XNKvhEZW2ySp5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=sz2CxIVdZk-jvvNX0CxgMjs8eJhJ-74JDChC1w4oXnDPlW2tDBYuUWdhhLvOddtdyf8G8MnfmcQo8zG65xEN_IhXdiuV_WG0ppzr4dheGytJrOwZQ1Hd05FubqRVusdIOeIxP6XzsTDtC3NYQdIHE_TnV2VQFQV6XoCI5U28VG4BMKqiOI141ZZTbYAvu7tf18vbAEzvahxhlwuRa5yHQ-WjhK9thwncyEHHzVEGEkrGouTvH-RLjUjNFA_VgGsIgmeoMF5x2TPXNnVsDIedDcwcSZzzfq4qkRGUHyEn4dTEh2aVMDvMQ10-1YHE8zBlhmHWO98XNKvhEZW2ySp5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره لغو عوارض گرفتن از تنگه هرمز
:
«آنها (کشورهای عربی)گفتند: "ما ترجیح می‌دهیم سرمایه‌گذاری کنیم تا عوارض پرداخت کنیم." و من این را دوست دارم چون هیچ‌کس نباید بتواند برای تنگه عوارض دریافت کند.
«در مقابل این سرمایه‌گذاری، کشورهای حوزه خلیج‌فارس مبلغ بسیار زیادی در آمریکا سرمایه‌گذاری خواهند کرد. این در واقع خیلی بهتر است!»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68092" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68091">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
شنیدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68091" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68090">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dhts4byZApzyz9400K9OWEBmh3Fnf100wCl6lAVCcl3juOm5kriy6JMeIt-_C-0MlGghkWevs7DmIDVxmsPSawMPcJLINkk5MLc5fLgb3f-xvdDxPViFtOUHX4k8zoabZuibN4i52MAQITr2M1hzbWlLH8Bo4g6QgeKmcODlUObiTdQeUo2oKziMM4cPQxuIxpJvGYcVYnx2lc67Y1ntmOEHQVsdWHd7ajSYu7PV1Pg8RT8YEM1sY89OI_EBBB4A85LsS_EStk6A9A-ysE9I9-gaKMO0c4abeZ1YWyRK4xTT2TMFRKVRXBYx2lZdR45LOoKxEAp8tGELtQgqFvva4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
به لطف قدرت فوق‌العاده ارتش ایالات متحده، نفت بیش از هر زمان دیگری در جریان است. درود ویژه می‌فرستم به وزیر دفاع، پیت هگسث؛ رئیس ستاد مشترک ارتش، دن کین؛ و فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، دریاسالار برد کوپر. به واسطه تلاش‌های آن‌ها و تمامی اعضای قدرتمندترین ارتش جهان — که بی‌رقیب است — تنگه هرمز برای تردد تمامی کشتی‌ها باز است، مگر برای ایران؛ و این استثنا به دلیل رهبری دروغگو، خشن و بدخواه ایران است که کشورشان را به سوی نابودی کامل سوق می‌دهد. بنابراین، ما یک محاصره کامل اعمال خواهیم کرد، اما تنها برای کشتی‌هایی که به بنادر ایران می‌آیند یا از آنجا خارج می‌شوند، و یا محموله‌هایی مرتبط با ایران حمل می‌کنند. بر اساس گفتگوهای بسیار سازنده با رهبران خاورمیانه، تصمیم گرفته‌ام که «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌نامه‌های تجاری و سرمایه‌گذاری جایگزین کنم؛ توافق‌هایی که کشورهای مختلف حوزه خلیج فارس در ایالات متحده انجام خواهند داد. این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان فوق‌العاده سودمند خواهند بود. همان‌طور که همگان می‌دانند، ما در مقایسه با هر کشور دیگری در طول تاریخ، بیشترین حجم سرمایه‌گذاری دلاری را در ایالات متحده داریم؛ اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهد کرد. ما شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطحی بی‌سابقه خواهیم بود که میلیون‌ها شغل جدید و پردرآمد برای آمریکایی‌ها ایجاد خواهد کرد! آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای که نظیر آن هرگز دیده نشده است. دوران کشتار صدها هزار نفر — از جمله ۵۲ هزار معترض — توسط ایران به پایان رسیده است و مهم‌تر از همه اینکه: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور
دونالد جی. ترامپ»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68090" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68089">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dp7PA4WsdFzgeslThhYSt4x1X9kt_sQx_ETW4ATUHst3OGV20tfPtQOnN01CgwvrEHZ99Kj-Km8CoAYdvZEHWbWDLQTx1hAQUVaIu4xDfdb_uGva9TqxBIOoMysvtHI4TpnL4SdkpZst1zNyLJIghI5XQqJPy139WFWYlVx5zAvuLdEH7A0htl6Ar2eVtuoe-L0m2ECILieGFTnG3XG7rV7WsKbMW8yXHxJ1Xer4K6Dq5aO3psFx_Aj0QKJvUXpWjqwaEDweD1frtW0qfQNngEt9nz7zv9PLcfVgP0bJUHLL3GButfSQkiTXnl6B8SXu8SPIdvXI-mbH4NP9pFuUdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ پستی از کاربری که متنی از مصاحبه او با روزنامه گاردین است را بازنشر کرد.
کاربر : «وای خدای من!
اصلاً نمی‌دانستم ترامپ این را گفته است.
آن هم در سال ۱۹۸۸!
جزیره خارک را تصرف کنید!»
متن مصاحبه ترامپ با گاردین ۱۹۸۸:
«اگه من بودم در قبال ایران بسیار سخت‌گیر می‌بودم. آن‌ها از نظر روانی ما را شکست داده‌اند و باعث شده‌اند مثل یک مشت احمق به نظر برسیم. اگر حتی یک گلوله به سمت یکی از نیروها یا کشتی‌های ما شلیک می‌شد، یه بلایی  بر سر جزیره خارک می‌آوردم و وارد عمل می‌شدم و آن را تصرف می‌کردم. ایران حتی از پس عراق هم برنمی‌آید، اما ایالات متحده را به بازی گرفته است. حمله به آن‌ها به نفع جهان خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68089" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68088">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=cfBcTKO2xzq9Aq9B5NwXC_FLAZi_zpGukTHHfVhMhHL5nl11IEX-YbyItABA5rv3vhFapIzlRC4TPEAIgJ4u0Evn-ZUBGC6tBd4GaQQY54k92yRv_cgMuv7ZLRRz9Rej5jHVE1ZwX5O_00NbnC_k5T9iqK1UpZVqKwHJIjmc5v_OSEYnMaGTdx_WB8VpLcTKZrU1JeX_xok3J_XTHs5ki9bFTFVUGUBSYqlqEbolKfAXj3CUwfPSzwpJFUxHfrlWwNg58MGKebGfuHaFSJh_gushhpAAIGwWvb0vmAN84Q2UAVGCdK-Qqv811yMfFibAObYpM-OFPoQgISXaqsjHeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=cfBcTKO2xzq9Aq9B5NwXC_FLAZi_zpGukTHHfVhMhHL5nl11IEX-YbyItABA5rv3vhFapIzlRC4TPEAIgJ4u0Evn-ZUBGC6tBd4GaQQY54k92yRv_cgMuv7ZLRRz9Rej5jHVE1ZwX5O_00NbnC_k5T9iqK1UpZVqKwHJIjmc5v_OSEYnMaGTdx_WB8VpLcTKZrU1JeX_xok3J_XTHs5ki9bFTFVUGUBSYqlqEbolKfAXj3CUwfPSzwpJFUxHfrlWwNg58MGKebGfuHaFSJh_gushhpAAIGwWvb0vmAN84Q2UAVGCdK-Qqv811yMfFibAObYpM-OFPoQgISXaqsjHeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نظر مراد ویسی در پاسخ به مخاطبی که گفت باید حرم امام‌رضا هدف باشد:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68088" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68087">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به ۱۱ شناور در دریای آزوف — شامل پنج نفت‌کش، پنج کشتی باری و یک یدک‌کش — حمله کردند؛ اقدامی که نهمین روز پیاپی از کارزار حملات گسترده علیه ناوگان کشتیرانی روسیه را رقم زد. نیروهای سامانه‌های بدون‌سرنشین اوکراین اعلام کردند که در بازه زمانی ۶ تا ۱۴ ژوئیه، به ۱۱۶ شناور روسی حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68087" target="_blank">📅 17:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68086">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=GFzSpVhTRYMSj-goHjL0X1Pjacfgn_o41nI-dMO-zVx8IcV2gE9BRbTxWJG5zYz9mLbeb82hRZn4A3kP9wg7UhHa978ixJnCxKZJh8aLmxKTi5Tk7UKJ19GNZ3yzuxMBsL0AVLRxmIBkBSJVHTiAAVyicIKMq-VF914-Ti6GTqT4hpMcwnCU4EPMab0zyFR75bExHzs9VKJ-caqKKMDZMvg5vxJ6ixPupIUKvntvJT0lH_8QnwAuKM37L9qp0itjIN5Oqphc4BFPoxJl3we3kLEFLjXPTxArPGS5hYMwyqyJzD6baPYlE_i7xmcHl5ZdfRcjgUINg-DJCJuca9EOvXbVd0k_KrzKG4CM7IZFqgYH3ZdhWaa1FM23bKqmk-ET7gYqtuVSoNDd2QS9nlxMzBcWgV5TwroZcpLVZpIjVmmNIJNuZxiqBl-CRu7BbdEwxqvPTya-7iP3TrPvtscskI1UNKSpzulQJ-x2BTEK8Q2D7DnFS9CMCUgVjw3TRmNhDqi8uYiOu4LBpvDJ0NI4FWGnP6pkCH8bnBfI8Cu56t5ZILZ-hpPwe3n8ZGh9rOa4pidKsFhDyQGDfl1VOp4K0HpaNwFC4ierrpLMtZmAsLCr_laAIX_E_-7w7DJfHCvMAyvXivSR2XwfgTCWtOctiE-SK0qC_xRCaNt2cwm40TI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=GFzSpVhTRYMSj-goHjL0X1Pjacfgn_o41nI-dMO-zVx8IcV2gE9BRbTxWJG5zYz9mLbeb82hRZn4A3kP9wg7UhHa978ixJnCxKZJh8aLmxKTi5Tk7UKJ19GNZ3yzuxMBsL0AVLRxmIBkBSJVHTiAAVyicIKMq-VF914-Ti6GTqT4hpMcwnCU4EPMab0zyFR75bExHzs9VKJ-caqKKMDZMvg5vxJ6ixPupIUKvntvJT0lH_8QnwAuKM37L9qp0itjIN5Oqphc4BFPoxJl3we3kLEFLjXPTxArPGS5hYMwyqyJzD6baPYlE_i7xmcHl5ZdfRcjgUINg-DJCJuca9EOvXbVd0k_KrzKG4CM7IZFqgYH3ZdhWaa1FM23bKqmk-ET7gYqtuVSoNDd2QS9nlxMzBcWgV5TwroZcpLVZpIjVmmNIJNuZxiqBl-CRu7BbdEwxqvPTya-7iP3TrPvtscskI1UNKSpzulQJ-x2BTEK8Q2D7DnFS9CMCUgVjw3TRmNhDqi8uYiOu4LBpvDJ0NI4FWGnP6pkCH8bnBfI8Cu56t5ZILZ-hpPwe3n8ZGh9rOa4pidKsFhDyQGDfl1VOp4K0HpaNwFC4ierrpLMtZmAsLCr_laAIX_E_-7w7DJfHCvMAyvXivSR2XwfgTCWtOctiE-SK0qC_xRCaNt2cwm40TI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بخشی از مستند "عمامه صورتی" که در سال ۱۴۰۲ تولید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68086" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68085">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=pD0DYNc8dfaNUHP3l_C-Z4_o9A69ZIqB-myf0zNcfyXLx-PVlVHyANTJ5L1fMmhYVZz3j1ZglL1cfOTl6yGW6uGMgbscE5Hr9ZBwY4JiIY78IkO-5KbfHkhu3GPXxU7di34JkXVRLnMVQoO2aCPEkj93Q76Ct8m9r3giEEMsytqEJyFL1-mcRf39uzCweEcJ9N1nL1YGKCjzqlpBY8zacyeOAGCAhuo-xmbvmYFWcWtSze8kBBKFukENZRydczdO-P9fwXbnhfjB0C1eUofihabcI5az5FXkS_4Tz89P07jJ9L6sRzneW7J6EuFaTdPK_UP36lGNczQ-2atcs-u1Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=pD0DYNc8dfaNUHP3l_C-Z4_o9A69ZIqB-myf0zNcfyXLx-PVlVHyANTJ5L1fMmhYVZz3j1ZglL1cfOTl6yGW6uGMgbscE5Hr9ZBwY4JiIY78IkO-5KbfHkhu3GPXxU7di34JkXVRLnMVQoO2aCPEkj93Q76Ct8m9r3giEEMsytqEJyFL1-mcRf39uzCweEcJ9N1nL1YGKCjzqlpBY8zacyeOAGCAhuo-xmbvmYFWcWtSze8kBBKFukENZRydczdO-P9fwXbnhfjB0C1eUofihabcI5az5FXkS_4Tz89P07jJ9L6sRzneW7J6EuFaTdPK_UP36lGNczQ-2atcs-u1Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام ویدیو ای از حملات به ایران در طول شب منتشر کرد.
در اواسط ویدیو نشان میدهد که لانچرها در فضای باز هدف قرار میگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68085" target="_blank">📅 16:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68084">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdI6sQNg8c9l8npIlxZLOwyJLwcAFqR7qEHebaztYVJl4aJdjvcp8TLdhlFwIjwykE0bkkhxxLmy09wvpK9hA-CfRVNFbudqoqJzK4dnXq1OKmT-9cHvoyVGPzctO7W5B1xwygFw713AWQYCM2Z2zTWmJy1IovSYiQvJZHc03CrT6f1fuoEb8NAfODxIMeXxqCeSE0SuBZum8CkniOfnE9KItk3p4KgienAFO3JJO2EO69bFqDlou1KlYSKExyyw1Nrq73C7Du2wxNgdEfxP3eQtnzdzmou-aWHoiGmjhvR09xqKICwQXH_ASBU6jeA3etamyliirK872E_OGEgilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیکتاتور قالیباف
؛
سید محمود نبویان نائب رئیس کمیسیون امنیت ملی مجلس و ابراهیم عزیزی سخنگوی کمیسیون را که از مخالفان سرسخت توافق بودند از هیأت رئیسه کمیسیون امنیت ملی حذف کرد.
عباس مقتدایی نماینده اصفهان و از حامیان دوآتشه عراقچی به عنوان نایب رئیس اول و حسن قشقاوی از دیپلماتهای حامی برجام به عنوان سخنگوی این کمیسیون انتخاب شدند
.
بهنام سعیدی از نمایندگان نزدیک به قالیباف و یعقوب رضازاده نماینده سلماس که اخیرا در مناظره‌ای با ثابتی از توافق با امریکا حمایت کرده بود نیز به عنوان دبیران اول و دوم این کمیسیون انتخاب شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68084" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68083">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=j2tllj09FH1F0UR21kFQlXCM6r8raP4SoE81IzUZQdKXxbqG_pSVNXWSgD5bH6cdTnoxFr_8OnVi7dwW1PG09e7-yY52-X1J6Tlsdc0KVQ_wb8NEg3CTJlxtNhIt74zNMJdaIuyZW6n8V_qAuWSUrSuWfZlhYQcR0RayCMWT_y7mJPHkEtjJQdcyGERL7UI0-FK1DFpUgn1AzpE_KOlU38tU6b5utqia91U54b4e5cf8WOm4DnpkhveVcIQcuVnob8EEgstQMvUtF0Htdunagz49_Nan2g4TDX5aX3JH-_2CoegB3qK4EZOHjtkOGAlooD3woRMPpvVVMzxEj2vAmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=j2tllj09FH1F0UR21kFQlXCM6r8raP4SoE81IzUZQdKXxbqG_pSVNXWSgD5bH6cdTnoxFr_8OnVi7dwW1PG09e7-yY52-X1J6Tlsdc0KVQ_wb8NEg3CTJlxtNhIt74zNMJdaIuyZW6n8V_qAuWSUrSuWfZlhYQcR0RayCMWT_y7mJPHkEtjJQdcyGERL7UI0-FK1DFpUgn1AzpE_KOlU38tU6b5utqia91U54b4e5cf8WOm4DnpkhveVcIQcuVnob8EEgstQMvUtF0Htdunagz49_Nan2g4TDX5aX3JH-_2CoegB3qK4EZOHjtkOGAlooD3woRMPpvVVMzxEj2vAmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده(سنتکام):
ملوانان آمریکایی بر روی ناو «یو‌اس‌اس جورج اچ. دابلیو. بوش» (CVN 77) عملیات پروازی انجام می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68083" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68082">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXTap9VgC4JfqwDNhOrltsVIHBdcIanzBfW9exqMz4L7liDNqWJa3-vsptbmylmamve9DLiEcNyFPy56Lemeuk8_J3wLBQDTctXW3iufQp8P1m3kW0iqZMYOUMDTe5WhTUmbwJ3WKNtEUnTjdQWo1IITZt_3nTpeLyifmvF7fS1jrzHPEzr_w1osLfvp56zM4wKwkvhvNcg_i3LI0RpzVc7Lh5_wJK1CTzFhlDOjxEfljdRr4hNLNvqYq2Tgq9sCD2k60ivZstiXH2YpBn9loIw10_KsLiMIp7FzZse3D8nVtQbnLdFz9VjjHbnBiv467cs34nGnaSZR_7CDlwguTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لبنان و اسرائیل مذاکرات خود را در رم از سر گرفتند؛ در حالی که لبنان به پیشرفت در جهت عقب‌نشینی ارتش اسرائیل و اسرائیل به پیشرفت در جهت خلع سلاح حزب‌الله امید دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68082" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68081">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=dTVnRD-k-inLNcnWaE2Sj3_jgifxlcg_uHRpuAZwA-jPnWtQy2UFhUBtal2zYGKxv9FuT5Z1N_5J27YMtymKFRQdxEPZJamEv1Hh8gS_Nqt0Y-qoMlDoY1RB_HgOucLskczrrlNFrml05KCVaIvL0zCvcZc72lCxyNITuVZUWuLFeeQTR3vvN_2J81uhlZx-m9ynm7TxqmlTaX2F-FQi7lC3dsVVVAhS8ij9s4VOCFeUfeWilZh0IptMXyzf4HyZcDs1bd7hZU3L_3VlbDR1icTJgnwr0qbJuly7BRvsvJsQQXJWjLa6N-a89eP3jYibKdoV--T4pE6qu4mPmgEMWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=dTVnRD-k-inLNcnWaE2Sj3_jgifxlcg_uHRpuAZwA-jPnWtQy2UFhUBtal2zYGKxv9FuT5Z1N_5J27YMtymKFRQdxEPZJamEv1Hh8gS_Nqt0Y-qoMlDoY1RB_HgOucLskczrrlNFrml05KCVaIvL0zCvcZc72lCxyNITuVZUWuLFeeQTR3vvN_2J81uhlZx-m9ynm7TxqmlTaX2F-FQi7lC3dsVVVAhS8ij9s4VOCFeUfeWilZh0IptMXyzf4HyZcDs1bd7hZU3L_3VlbDR1icTJgnwr0qbJuly7BRvsvJsQQXJWjLa6N-a89eP3jYibKdoV--T4pE6qu4mPmgEMWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:  اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد. در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68081" target="_blank">📅 13:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68080">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
معاون استاندار بوشهر:
چهار نقطه در شهر بوشهر مورد اصابت بمباران آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68080" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68079">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Szc0KHvvpEMER4Yb6nqgoaAo1mQpXZhPruviNxWMaH5PYxFrCo7r_m55mU9JGq-ySjVtnhd7X--HSkSsLGCxO0brQy8bNJBnVa5yxiDauIXB6nv6ECmTerDtj_1bZx4qwUxpJ97dktFzt5-VeuRTY5uTmVi4l1MUfyoPUFIHC08MEhCEk9fSFLyto9nzQwqddQUGcJ_mTRJ38Pu6xKSc6b9c9ZLVmfjT_tv-TGzncDcUgBJfvA120j4FAagvFrP73R6SlDwUgBawF6P3FlE5icsr136Two40XYWdF8Jap44HWFdqUp1okD8_0RxVs46S4NLjzVhuqEzYbf7Q6zKJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نمایی دیگر از بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68079" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68078">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJUIOEMoN6Jp-DX4XEq_L1xZhP3HJyvfqCOaPBnmsLQ-XYvIR_Oiz1kgIjzqMySP5wHfTlhiMoTL6CTqJecDSBPHhGjPd8cv6Uc0g000XyEdNT5p0U0bvRCmc8JeOpgbOGa_8NE6V5xZgJaw4w34Ut_L9QOuYjRXfZSVUJvz52I2Dlb10N999rAAEEQM5Xa8HDCzGJ4a6XUlemvYKErAd38w4fnZr8FC6adxOOFAGe2svqn5xRFLhs-A13AzMp76SI3KBHydc9BMTyKKdUDdpVJvFlKSv5_5pK9kM0V5m3zod3XfMqTiIkt6xZkzpcNtaclqml-VPb8yKbizHwzTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68078" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68077">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68077" target="_blank">📅 12:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68076">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
پنج انفجار در بندرعباس
@News_hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68076" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68075">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید در بحرین
@News_hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68075" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68074">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ گزارش های اولیه و #غیررسمی از حمله سپاه به سفارت اسرائیل در بحرین  @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68074" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68073">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
#مهم
؛ گزارش های اولیه و
#غیررسمی
از حمله سپاه به سفارت اسرائیل در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68073" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68072">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=aUds1vC2UWKvKWBpSvVqgJaVqrHe9cjmXU7DAseTAC85DmL6tcPZzmtiYB7tWoX61wR7S6v8jHLwaYIUJ-Cx9g23yU___U_B2kcA0oOYORMOuypFXiGUr4uhLAUWsNIWD1Tdy6CGCpsNc0RrFZfnUZd6RqJHsTCWFgt1jRg4jBWB88aDh8ZVhyJkkKdml_lNp0r6UQ61kTf-uCwRk2YW7l-dCKtNt7bTjI22k-ez3oC3TKpKwWFcEkXRyDsnChryZ-8CGqpfXkM6WvhZPCiLxa_S-6ZGuzzSG5FTNRJ6yAt6yMyfjz-Wcg4oIP8vqpESPljInkAxkhFuOZIgTLpPoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=aUds1vC2UWKvKWBpSvVqgJaVqrHe9cjmXU7DAseTAC85DmL6tcPZzmtiYB7tWoX61wR7S6v8jHLwaYIUJ-Cx9g23yU___U_B2kcA0oOYORMOuypFXiGUr4uhLAUWsNIWD1Tdy6CGCpsNc0RrFZfnUZd6RqJHsTCWFgt1jRg4jBWB88aDh8ZVhyJkkKdml_lNp0r6UQ61kTf-uCwRk2YW7l-dCKtNt7bTjI22k-ez3oC3TKpKwWFcEkXRyDsnChryZ-8CGqpfXkM6WvhZPCiLxa_S-6ZGuzzSG5FTNRJ6yAt6yMyfjz-Wcg4oIP8vqpESPljInkAxkhFuOZIgTLpPoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداسیما داشت خلاصه‌ی یه سریال رو پخش میکرد که تو یه تیکش اگه فقط صدارو گوش کنید، فکرمیکنید صداسیما در حال پخش پورنه:
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68072" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68071">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=FO9mF45-ozmA6u3oJaSv3VPM0qo3T09hlokq0yMatQJI_Rt-2XWmFXpL6LneqIqb6TDdDlxYAzuVd6daks9VoKtbPPFrAkfevw7TloLn6UTlfeuR4ldA7W6U6gvnkWRqBzANf3eur-zBwSbum8j_elUDRpHqqzfKIcRD2JMbTjmkfy4-4can9auLygAYYAijCdVLx7dNY4k4PN55yRkc0i5AjZ8GVvlxj71OPGn4gUPEVxgYQoazBrwIRw-25SsmgzdXcmZEfdrNEvGlhWtLMa7rGUG3vokgf37FmvDRE_ZE7ivtL7aeDT6LRTX_jt__mWS5v0ma-Ta8ORrR9Bje7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=FO9mF45-ozmA6u3oJaSv3VPM0qo3T09hlokq0yMatQJI_Rt-2XWmFXpL6LneqIqb6TDdDlxYAzuVd6daks9VoKtbPPFrAkfevw7TloLn6UTlfeuR4ldA7W6U6gvnkWRqBzANf3eur-zBwSbum8j_elUDRpHqqzfKIcRD2JMbTjmkfy4-4can9auLygAYYAijCdVLx7dNY4k4PN55yRkc0i5AjZ8GVvlxj71OPGn4gUPEVxgYQoazBrwIRw-25SsmgzdXcmZEfdrNEvGlhWtLMa7rGUG3vokgf37FmvDRE_ZE7ivtL7aeDT6LRTX_jt__mWS5v0ma-Ta8ORrR9Bje7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمران رئیس شورای شهر تهران به سوالی درباره قطعی برق بدون اطلاع قبلی:
اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68071" target="_blank">📅 11:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68070">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkhuhpVdcvkN2FqoyAAy0728Lnk6bktKQoqrsjO5c6sWNCETMdJulLfW1C0cNv9dJ1ncAcxNzBraRrQvPUvNLiq7YYYFLfz0ipADk8se6I2DexY18kF-nqo516ftyAKIIVn_coyV8S_NiugS2lpTMS-eWGnaumKLCCnSejmaBW_OiK3oxW8aeWq66bzmXVPkntswctzSMjL5K7kRsBCW1z_AOsbYNqLvj8y2MzXh78jgFZcwuv0bTmBIM35KQsuojhRu32Uu00cHP8gMANg2OIEqDqFdxHlWjv1pIrME_gWm4JZOnAX07oLK39tLfag5dnX-n7spd8UaA69XUM9Kcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی بریتانیا:
گزارشی از یک حادثه در فاصله ۱۳ مایل دریایی جنوب شرقی لیماه، عمان، دریافت کردیم
یک نفتکش گزارش داده است که هنگام تردد در مسیر جنوبی به سمت خارج، مورد اصابت موشک قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68070" target="_blank">📅 11:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68069">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=m-tyVeaTyy8WeVvp94Dbaem3h4xbxBz2BqHqWL654pqqJY9XmewYJ6-9mRsYcTx9BBnOv1gLY9Lkl4_osHvB4oewz8AU-gRaqdOKoNy7UYGMEMhyXeFa4_U2TIGrpqWXg7qHI5-3ON7dPuI3KxqnsPqfCmmHDK7YIEyWjWVHbhuoo5XbgJRHw7vq_Ro_lolOFYakpQ5Ffut_pd5_-JqQKxVzFjOzx15mHhFHYZnEZzHSsj7AKl1bmtiChcHW08f37kc6dsHteBao6ih3MhxvhY5TJiFsp0eYoq-lx6EnkwtEb4Y4hdISCsvrePj2MpeMMDDBbm2qieSE0Z6RCEWb_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=m-tyVeaTyy8WeVvp94Dbaem3h4xbxBz2BqHqWL654pqqJY9XmewYJ6-9mRsYcTx9BBnOv1gLY9Lkl4_osHvB4oewz8AU-gRaqdOKoNy7UYGMEMhyXeFa4_U2TIGrpqWXg7qHI5-3ON7dPuI3KxqnsPqfCmmHDK7YIEyWjWVHbhuoo5XbgJRHw7vq_Ro_lolOFYakpQ5Ffut_pd5_-JqQKxVzFjOzx15mHhFHYZnEZzHSsj7AKl1bmtiChcHW08f37kc6dsHteBao6ih3MhxvhY5TJiFsp0eYoq-lx6EnkwtEb4Y4hdISCsvrePj2MpeMMDDBbm2qieSE0Z6RCEWb_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی،تحلیلگر ارشد اینترنشنال:
چشم انداز موجود تشدید جنگه،پاکستانم دیگه نمیتونه بین ایران و آمریکا میانجیگری کنه.
جنگ سوم بین دو کشور تو روزای آینده شروع میشه.
اگه اسرائیلم وارد بشه یه لایه دیگه از سران جمهوری اسلامی رو حذف میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68069" target="_blank">📅 11:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68068">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdbTWQbQWRmZnT9S61uaRPlTPv_uvchP-giGxKZGf-J0SCtKcQsd4MASyZd9FFmUNpjwklVb_ACo9Le290l0pVoGBVZpJjTjwGD0MFumeR_kZ9qo6c9UJdmRjDH4o-_cXekzKgrFFcZnN9rOkR_FqO_99icrHP6HLfu6EO3WXKJLR6T7LPkdgMJkKLSSjTisZY63kWZzTPhUWBP7OEEas9Fnitm9tEUiKQqbEbRQelQuYAprw-6j1KDOhC8MK7T9U2VfoYKndXCnRIyntJ8Gw8bjCFIGLkGoI0K6RafVDbDPJLv7DkeB_V0T1-gb9AWhLlvIQag7vfFLaEgo28gRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) آخرین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب (به وقت شرقی) روز ۱۳ ژوئیه به پایان رساند.
در جریان این عملیات پنج‌ساعته، نیروهای آمریکایی با هدف تضعیف بیشتر توانایی ایران در حمله به کشتی‌های تجاری، با موفقیت به اهداف نظامی در نقاط مختلف ایران از جمله بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردند.
نیروهای سنتکام برای هدف قرار دادن سامانه‌های پدافند ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران، از مهمات دقیق‌زن استفاده کردند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند.
نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار باقی مانده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68068" target="_blank">📅 10:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68067">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=pXnIG1Prr-Yi5VFB5ks-evRxo-LtLsdgSFPTKBs0spbyZG1izBsB2I0J9LjRNb9zEy_OtrDxp-n4dAz1tNkdC9Uf51NTAiOBSqyg8PuaqYWemZeZSQGb_s2kc01YtJvDTc3Zy4z10HlydESULQV37rLaDABOZfdjuYcO716mvBTMagw_Sx8NY11oT1YJM--dUNjZOP3EKcVNct-EG1DKP_LnqB6jkS4UT6umnsQo0IJ63eK0YggobMbJv1fUEbwk2xD4gXN2l-bC-CQP8KmSbMhK_DxTj0prugyzzVe_GIbaumN5UEYBghUIIqa35MQjp3feKzygrtHcjDcqp784Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=pXnIG1Prr-Yi5VFB5ks-evRxo-LtLsdgSFPTKBs0spbyZG1izBsB2I0J9LjRNb9zEy_OtrDxp-n4dAz1tNkdC9Uf51NTAiOBSqyg8PuaqYWemZeZSQGb_s2kc01YtJvDTc3Zy4z10HlydESULQV37rLaDABOZfdjuYcO716mvBTMagw_Sx8NY11oT1YJM--dUNjZOP3EKcVNct-EG1DKP_LnqB6jkS4UT6umnsQo0IJ63eK0YggobMbJv1fUEbwk2xD4gXN2l-bC-CQP8KmSbMhK_DxTj0prugyzzVe_GIbaumN5UEYBghUIIqa35MQjp3feKzygrtHcjDcqp784Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخطار پلمب، مانکنت نامتعارفه !!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68067" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68066">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AidDyfRlCLd7noFF5qyL-PeqsY5i7h562-Hxdm_nmla2Uoq41i6WHYuK1EuTcYnyhSzf0418XgYy3U3uVclC9T-7hoAnHQb5KNKPlVlWxKEu0EnXBHhOjb9XplWVtU3TnsviOq2RhK5wzslx1qGkUjP_Q0TShvJEgGWaM51YJIIgqIfGnS5zcSg2L2HbfQmYl1FetiEW_0a-tERqnSXQOjZ8TSnvMJDy4ZNSOaTgCW1Uq1sQwHTK5Mt5S14AoANuuQw5k1jKdW9LWTd5307qws3Zb0Gr5xofCgJdPdpwCUdaxPb1ZnoMXL0nXY1ifyaESFTXsWhaSIqL9fUMYDD4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:
اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد.
در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای خارجی، از جمله در مجارستان، با احمدی‌نژاد دیدارهای محرمانه‌ای برگزار کردند و از رویدادهای دانشگاهی به‌عنوان پوشش این ملاقات‌ها استفاده کردند.
این طرح در جریان جنگ ایران و اسرائیل در سال ۲۰۲۶ به اوج خود رسید؛ زمانی که مأموران موساد پس از حمله هوایی اسرائیل به محل اقامت احمدی‌نژاد در تهران، او را از آنجا خارج کرده و به یک خانه امن در داخل ایران منتقل کردند. این اقدام بخشی از یک عملیات گسترده‌تر برای تغییر حکومت بود.
این عملیات در نهایت ناکام ماند، زیرا احمدی‌نژاد تحت شرایطی نامشخص خانه امن را ترک کرد.
به گفته مقام‌های ایرانی، او اکنون پس از آنکه مقامات از تماس‌های ادعایی‌اش با اسرائیل مطلع شدند، در حصر خانگی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68066" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68065">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KspMF-b6hfGalArDJ8pXKJkps4Mv86AjnTp0nanP67TF5cVLJJCOrF8Z25QTyYcfkZkleMaQgkIZVa_KSrpfXZRpek2CLpVo7C_za6PLLShKvOkPU_XakaN30W_K2OxZZdb8N4m2-9aMBmdospMvuQ4uZ3ZLQxUWp7tQmU_T0w60za7qK8m2xUOpGzYi3kATZRZHLpQRkqbZCsgSAOH4C56AoJKbt4cEp1aYVu5_L5BfBQVsOM56pspt9ePhSDQNbYc9ObvI_sr_bBrYqHSO6eX_DPgAdGT5c8CViYtl_CkrDJZV0cOz7kkUd9KcnwnVmlCSO3yKuGdUlq96Neddxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
وین ریت 80٪
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇳🇴
وین شد
✅
🇦🇷
⚔️
🇨🇭
وین شد
✅
حالا هم دو تیم فینالیست مشخص و در کانال تلگراممون اطلاع رسانی شده
⏳
🇪🇸
⚔️
🇫🇷
‌
󐁢󐁥󐁮󐁧󐁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
t.me/bet__gg</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68065" target="_blank">📅 03:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68064">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=uC2BMCfMGxmtb8Yf4k5CL1EZVtU8qTOfbg_QSZDWHNrfCEsLHbGxiwkAzegR9PlwNNyRYgwr09gca1mmUnCLYGOK5NX62GzpWgnSw4GXJ6cj_-6ky5mMdK-lueg2xjwJ7COVRBsJYvs6eC-5O8NUWkYA2JVtTeXncA5f7p4-xT0XzMQ_BXBM38aSTpGzPalfep0tFGtCZAJJG7xEWswKphfJltvy5GNjh3T6hNgZp1Dn7F8iSnYRTjsjsMtWsAB6qE95o-efRslySFi9oScmwk4Xcp-38s1VuTFDxae16bxDopj4zPaYSoZLlnF6Ij7-1aCdt3b-uNlhKun5H7z0FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=uC2BMCfMGxmtb8Yf4k5CL1EZVtU8qTOfbg_QSZDWHNrfCEsLHbGxiwkAzegR9PlwNNyRYgwr09gca1mmUnCLYGOK5NX62GzpWgnSw4GXJ6cj_-6ky5mMdK-lueg2xjwJ7COVRBsJYvs6eC-5O8NUWkYA2JVtTeXncA5f7p4-xT0XzMQ_BXBM38aSTpGzPalfep0tFGtCZAJJG7xEWswKphfJltvy5GNjh3T6hNgZp1Dn7F8iSnYRTjsjsMtWsAB6qE95o-efRslySFi9oScmwk4Xcp-38s1VuTFDxae16bxDopj4zPaYSoZLlnF6Ij7-1aCdt3b-uNlhKun5H7z0FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو ای از حمله امشب آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68064" target="_blank">📅 02:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68063">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=RdUIOhGBH6-zWHgwwsF5KfD2omqI-o9aP0sBURaFORYw6Li1gW6h75k_bhtGYNufGfvEXJw2ZK1WdkBhv6_TaqiY5CsU9cYpktOBJDgQHhpIFPykxcUWOrVaRrozciJeR5TH43r-H-sLu4XDBJogUTRa4w2bn4j_8cgE8mEqft-gLtsR13WJRMtghoZQ7qvE7mMgpV9E5BwllefbZ4l_0qim3xrgyR26wguoaitLsefCEvksav9cxAp_P8wrhq9kDc2aOLaMbolW5fxB7btMiEai0Xsqn96C5Efr9GWJhkP01Ry39q6VBmlO7kRlw5xVBHPoA6G4NIqnSUuO57yOZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=RdUIOhGBH6-zWHgwwsF5KfD2omqI-o9aP0sBURaFORYw6Li1gW6h75k_bhtGYNufGfvEXJw2ZK1WdkBhv6_TaqiY5CsU9cYpktOBJDgQHhpIFPykxcUWOrVaRrozciJeR5TH43r-H-sLu4XDBJogUTRa4w2bn4j_8cgE8mEqft-gLtsR13WJRMtghoZQ7qvE7mMgpV9E5BwllefbZ4l_0qim3xrgyR26wguoaitLsefCEvksav9cxAp_P8wrhq9kDc2aOLaMbolW5fxB7btMiEai0Xsqn96C5Efr9GWJhkP01Ry39q6VBmlO7kRlw5xVBHPoA6G4NIqnSUuO57yOZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انفجار سراوان سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68063" target="_blank">📅 02:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68062">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
انفجار امیدیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68062" target="_blank">📅 02:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68061">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
حمله به سپاهِ سراوان در سیستان و بلوچستان
@News_hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68061" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68060">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=NlpS8k_qyF1AsDyG51RVT8xSFD81UXYJgzsf_utTJHQMGknBsYRSVuGjdSlTXtCk9gYgwJTsHUQ60hU8OMbTP4HRCaU0tGtSfu1sFZhPysuWXXh6UWLUw-StXgvvw-Hm305xTRpgHX8RBaYyAhwjCKFUiewyysu54YQBfQipTg8EwlPkbrrwWhEq3Qiho8NMSdXSetd4-Umkwn7wefB9IGE9hxrWrjWenjtexH3Xx2D-dhYMKWJHP0A9iujNrmYmVmg7nnyAWN0CkBG6-mwLl9ptpnd9JPXtwdwcKAHFRPlvTcaW_DtdngdS4KOBtq-3g0TIpiYiE0HBBxdkxaAwpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=NlpS8k_qyF1AsDyG51RVT8xSFD81UXYJgzsf_utTJHQMGknBsYRSVuGjdSlTXtCk9gYgwJTsHUQ60hU8OMbTP4HRCaU0tGtSfu1sFZhPysuWXXh6UWLUw-StXgvvw-Hm305xTRpgHX8RBaYyAhwjCKFUiewyysu54YQBfQipTg8EwlPkbrrwWhEq3Qiho8NMSdXSetd4-Umkwn7wefB9IGE9hxrWrjWenjtexH3Xx2D-dhYMKWJHP0A9iujNrmYmVmg7nnyAWN0CkBG6-mwLl9ptpnd9JPXtwdwcKAHFRPlvTcaW_DtdngdS4KOBtq-3g0TIpiYiE0HBBxdkxaAwpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیوهای رسیده به ایران‌اینترنشنال نشان می‌دهد شناورهای تندروی کلاس «گلف» سپاه پاسداران در بامداد سه‌شنبه ۲۳ تیر پس از حمله آمریکا به مواضع جمهوری اسلامی در بندرگاه و دریابانی کیش، در آتش می‌سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68060" target="_blank">📅 02:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68059">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=Savb-u-aBuR_Y3_NLiSQr8kPc265cXmqrWQHxCO2brGwvydzxJbo5vHijmKjMOwPXP_FaKzXtCBudmqIhNq5p7As9s7X-iIb2aVx0B77eT6ds4coqXJX5MPywvW2vNq_lTV4CVy0wdeYwx-lL9ET_e865voet75-fxaF0gaJQG76XVUC20-q8MZ1bWlK76Ha9VuiaY82fW0-0fHAu6WlWmXkpJ_hSbG0XywcOVyPjvrK0z91xLlGaMC_anlq-C_RagyHLIzPi6Q5byai_XiPd67mcCzJN6nEFwI7jmxqBAY7hWhwjEHAozmXU-MVD-5spRsPUjzhyryy_oVlXSkkzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=Savb-u-aBuR_Y3_NLiSQr8kPc265cXmqrWQHxCO2brGwvydzxJbo5vHijmKjMOwPXP_FaKzXtCBudmqIhNq5p7As9s7X-iIb2aVx0B77eT6ds4coqXJX5MPywvW2vNq_lTV4CVy0wdeYwx-lL9ET_e865voet75-fxaF0gaJQG76XVUC20-q8MZ1bWlK76Ha9VuiaY82fW0-0fHAu6WlWmXkpJ_hSbG0XywcOVyPjvrK0z91xLlGaMC_anlq-C_RagyHLIzPi6Q5byai_XiPd67mcCzJN6nEFwI7jmxqBAY7hWhwjEHAozmXU-MVD-5spRsPUjzhyryy_oVlXSkkzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا فکر می‌کنید دستیابی به توافق با ایران همچنان ممکن است؟
🔴
املاکی هزار‌ پدر: بله، فکر می‌کنم توافق ممکن است
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68059" target="_blank">📅 02:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68058">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
ترامپ:  سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68058" target="_blank">📅 02:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68057">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=jNEpkRXBiHNPl90bX4BxH8okTLcF_NgnEtcVrYwkIfj24t3xLBrvCQ-ffQTG8ZedmeyBMIdGKmaQV0tJh5ulwlDWveFbA9XfiB0n6uBFcRpmvOof_eBQEXfotuTJ3XMUjuiCsr0BFDwqDyntLGn4wqZIc4qrII8_PG2j_WEHQNYtq9pGxecsEM5sVajPPg0oqE-7vWumF2BRCWi9gYhy1WZSzxO8hKPZszFtYC6yQO_-kET2FzIA4NRXlMW_bESM6FE2LIkkxqlZeFToHPuRyZrez7tTDunGZJ4uGNfVx-bSkp1BOQZh4_oPr_v19I7FNk7ECsM4zZlD2SDiV5pTlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=jNEpkRXBiHNPl90bX4BxH8okTLcF_NgnEtcVrYwkIfj24t3xLBrvCQ-ffQTG8ZedmeyBMIdGKmaQV0tJh5ulwlDWveFbA9XfiB0n6uBFcRpmvOof_eBQEXfotuTJ3XMUjuiCsr0BFDwqDyntLGn4wqZIc4qrII8_PG2j_WEHQNYtq9pGxecsEM5sVajPPg0oqE-7vWumF2BRCWi9gYhy1WZSzxO8hKPZszFtYC6yQO_-kET2FzIA4NRXlMW_bESM6FE2LIkkxqlZeFToHPuRyZrez7tTDunGZJ4uGNfVx-bSkp1BOQZh4_oPr_v19I7FNk7ECsM4zZlD2SDiV5pTlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ:
سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68057" target="_blank">📅 02:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68056">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
وزارت دفاع امارات متحده عربی:
دو نفتکش ملی به نام‌های "ممباسا" و "الباهیه" در آب‌های منطقه‌ای عمان، در بخش جنوبی تنگه هرمز، مورد هدف دو موشک ضدکشتی ایرانی قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68056" target="_blank">📅 02:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68055">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=rjjfevixZMbz2pMjob8D9119EVk9NORmn3NYW9Bu_AjDYaZCZQ7fKq0dWjScN4DOJrKrATHqvTQE_RnQ9MDbSSpTKfI8rFSDyHOIs4vWoBNyONUSbxc1J0PfyxEDlqvOKIUsooZ7ifSymDU0x2ejTIb6czS1pfvMhVUrkKsRTTVhAyKxSYfjYD9PdWTTleY3FRKTbIftNt72qcRQ6pKYx8XPHXRHVodXkKdq7EbwwBnAnwrifnc__OZGsqqBN_xn4InfXKhHjvBbiVq_a0I12ZYrwvQ3DCFRkUwzDh_lTKFRK4XYSaypEM-qpe0Kdmzbnep9SlG6pWrzt5bXxpKFsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=rjjfevixZMbz2pMjob8D9119EVk9NORmn3NYW9Bu_AjDYaZCZQ7fKq0dWjScN4DOJrKrATHqvTQE_RnQ9MDbSSpTKfI8rFSDyHOIs4vWoBNyONUSbxc1J0PfyxEDlqvOKIUsooZ7ifSymDU0x2ejTIb6czS1pfvMhVUrkKsRTTVhAyKxSYfjYD9PdWTTleY3FRKTbIftNt72qcRQ6pKYx8XPHXRHVodXkKdq7EbwwBnAnwrifnc__OZGsqqBN_xn4InfXKhHjvBbiVq_a0I12ZYrwvQ3DCFRkUwzDh_lTKFRK4XYSaypEM-qpe0Kdmzbnep9SlG6pWrzt5bXxpKFsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: محاصره دریایی فقط مختص ایران است.
🔴
خبرنگار:
آیا می‌خواهید هزینه‌تان جبران شود؟
🔴
ترامپ:
بله. چون ما از بخش بسیار ثروتمندی از جهان محافظت می‌کنیم. قرار است هزینه محافظت ما جبران شود.
🔴
خبرنگار:
توسط چه کسی؟
🔴
ترامپ:
توسط کشورهایی که از آنها محافظت می‌کنیم. عربستان سعودی، امارات متحده عربی، قطر، کویت، بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68055" target="_blank">📅 02:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68054">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
خبرنگار: ماه هاست که ایران را بمباران می کنید.
🔴
ترامپ: ما 19 سال در ویتنام بودیم. ما چهار ماهه اینجاییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68054" target="_blank">📅 02:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68053">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=SH6RKSK-XdEfJG80qyebauxTmPs6bii06f1Wmzm7X7zvMwyhC3eacq2Y7PJ2ZKg89LfcZhZ4-7g1cEuOr5uu7ecweRmGvFTBs_uqORvdLQZv1mDhKXI9jpl6Sn13RoyczM-Xp7IPvVrO8Jq22O6J1zLAgepLXYssyIL8Yli_isqNK5CqyQi8V0kcG68ZRvVccyzJQlRq9afpTbn-xs2zBh85R89074oXZ4esG154hbDK5c0WsYoPSU3YHKLWeYW6kAn4-XCFZhK86qekR8TuTGoC1sUOAMc22CtSf936ChiSbJqWPCC4GnFYvCdeGXpoQa9M2FYIPXY8gEUK1Mjfmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=SH6RKSK-XdEfJG80qyebauxTmPs6bii06f1Wmzm7X7zvMwyhC3eacq2Y7PJ2ZKg89LfcZhZ4-7g1cEuOr5uu7ecweRmGvFTBs_uqORvdLQZv1mDhKXI9jpl6Sn13RoyczM-Xp7IPvVrO8Jq22O6J1zLAgepLXYssyIL8Yli_isqNK5CqyQi8V0kcG68ZRvVccyzJQlRq9afpTbn-xs2zBh85R89074oXZ4esG154hbDK5c0WsYoPSU3YHKLWeYW6kAn4-XCFZhK86qekR8TuTGoC1sUOAMc22CtSf936ChiSbJqWPCC4GnFYvCdeGXpoQa9M2FYIPXY8gEUK1Mjfmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آنها را در موقعیتی داریم که هیچ نظامی ندارند. هیچ کاری نمی توانند در مورد آن انجام دهند.
تنها چیزی که آنها دارند اخبار جعلی است زیرا آنها اخبار جعلی را دارند و ترجیح می دهند ما در جنگ شکست بخوریم تا اینکه در جنگ پیروز شویم، که واقعاً به نوعی خیانت است.
ما امشب یک حمله بسیار بزرگ دیگر انجام می دهیم. آنها می خواهند معامله کنند. ما دو روز پیش معامله ای انجام دادیم و آنها می خواهند معامله کنند.
آنها 47 سال است که مذاکره می کنند، اما هیچ کس هرگز آنها را مورد حمله نظامی قرار نداده است. ما خیلی سخت به آنها ضربه می زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68053" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68052">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=SemMgUzPA8bLxGdUVLfoB6JJMgbOSvGwizR3gQiczUw9cAy_iLaqP1SO89LF9shgqMxy8DPIHblWl0dIt__-W6jM6GyNxf5oWn7ME5mweiHEBB7-x_zGb6Oo1ntK9bTenbU9ZErgLIpaKcyXnn5oaK4sxa0fhjAvr3uoE9jdJRh4spCZ3rVBcQSpFythI1zQg1Fa7nERrtkaY09ZUBPetMSVYPaYAvtpU-rxCY3dawME3j4ymAptQg0hgnbRdxEAmwLgVGmTxDiGvhlDKgWaFsPlWWligafdGlvuxZnhuQPP5JI2tl0V7hXIRHPnLCNfqD-l3VUfovYQ2GWh5E98uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=SemMgUzPA8bLxGdUVLfoB6JJMgbOSvGwizR3gQiczUw9cAy_iLaqP1SO89LF9shgqMxy8DPIHblWl0dIt__-W6jM6GyNxf5oWn7ME5mweiHEBB7-x_zGb6Oo1ntK9bTenbU9ZErgLIpaKcyXnn5oaK4sxa0fhjAvr3uoE9jdJRh4spCZ3rVBcQSpFythI1zQg1Fa7nERrtkaY09ZUBPetMSVYPaYAvtpU-rxCY3dawME3j4ymAptQg0hgnbRdxEAmwLgVGmTxDiGvhlDKgWaFsPlWWligafdGlvuxZnhuQPP5JI2tl0V7hXIRHPnLCNfqD-l3VUfovYQ2GWh5E98uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چهار ماه پیش، این‌ها نیروی نظامی بسیار قدرتمندی داشتند؛ بی‌شک قوی‌ترین نیرو، احتمالاً در کل خاورمیانه. آن‌ها را «قلدر خاورمیانه» می‌نامیدند. اما حالا دیگر نیروی دریایی ندارند. ۱۵۹ فروند از کشتی‌هایشان به زیر آب رفته است. آن‌ها ۲۳۰ فروند هواپیما، یعنی هواپیمای تهاجمی، داشتند؛ که همگی از دست رفته‌اند. آن‌ها سیستم‌های راداری فوق‌العاده‌ای داشتند که همگی از بین رفته‌اند. پدافند هوایی بسیار قدرتمندی داشتند که آن هم از میان رفته است. متأسفانه، رهبری‌شان نیز از بین رفته است. رهبران رده‌اول و رده‌دوم همگی کشته شده‌اند. حتی برخی از رهبران رده‌سومشان ــ که کم‌وبیش با آن‌ها سروکار داریم ــ نیز از میان رفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68052" target="_blank">📅 01:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68051">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzbdKcyg03qUEB5dj-iKQUXJaSl-OTxOfsQBxJ1Kh8mfOHFBRGRbWzRmMKIgcjQ3QBx3VvJilPXK0lfkpBlNRNHml11LA0XMHvSBz_691NKXcV5vxlPlbiDq1nRrDDRmRFjsvNa506Kyq2Y6yOBHpzUeE4o5kzw5xiV8zi6vSeg6LUBnQLdGXtNZsbpCQEEJEtRcG9TFb8xDlzTLweD3rPjpyGabWiYYCfQOMxYLClpJB9dUTnOTZxUvSN6XOwO7isgSVkzleq6mDkeyZstb8hLhrvnXjcSBl6wVTg0DA27DPdotbqZRvH0ka58nIbRgHvvo0eS28ADipM6xBKT09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرکز عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۴۰ مایل دریایی از منطقه قلهات در عمان هدف اصابت یک پرتابه قرار گرفته و این پرتابه به اتاق موتورخانه کشتی برخورد کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68051" target="_blank">📅 01:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68050">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=o2i7tPdnBBr8QHjI8SH4djKK3SSvrSY4hXx-5335dHdjGIgm8tnQE2W54rqNY-Zd793cMe-GXnGPqPU7eHc-pVuNj1J51L_YttcM5FH_kvfYssDv9HB04UCRq-C50TbkJglAHLqfWV4R_jParVroMA1jxGFhyXWHk3OoxGImJQzZGDe-HmcUCb16swe8iK2Qvyen2qWSO79lAVDzeD3NzR9n0xs1vDzUMgIZFFQYt3hLUPT1LEMofy8QV1p_0uD_9U-zqkZT72lyo_GaF5nW2GqDIhqUQS93TC9kErXH4ODt4tg7Z2tCtkboVcfLB455h8Hp9NHM-LZeZqdKlOlSsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=o2i7tPdnBBr8QHjI8SH4djKK3SSvrSY4hXx-5335dHdjGIgm8tnQE2W54rqNY-Zd793cMe-GXnGPqPU7eHc-pVuNj1J51L_YttcM5FH_kvfYssDv9HB04UCRq-C50TbkJglAHLqfWV4R_jParVroMA1jxGFhyXWHk3OoxGImJQzZGDe-HmcUCb16swe8iK2Qvyen2qWSO79lAVDzeD3NzR9n0xs1vDzUMgIZFFQYt3hLUPT1LEMofy8QV1p_0uD_9U-zqkZT72lyo_GaF5nW2GqDIhqUQS93TC9kErXH4ODt4tg7Z2tCtkboVcfLB455h8Hp9NHM-LZeZqdKlOlSsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
همان‌طور که می‌دانید، امشب ضربات سنگینی به آن‌ها وارد می‌کنیم.
ما حجم عظیمی از مهمات در اختیار داریم؛ موجودی ما در سطحی است که سال‌ها نظیر آن را نداشته‌ایم. ما ضربات بسیار سختی به آن‌ها می‌زنیم؛
این روند ادامه خواهد یافت و در نهایت خواهیم دید چه میشود.
ما در حال نابود کردن تمام توان تهاجمی آن‌ها و در کنترل گرفتن تنگه‌ها هستیم.
ما دوباره سیاست محاصره را اعمال می‌کنیم. شاید محاصره مؤثرتر از حملات مستقیم باشد، اما به گمانم ترکیبی از این دو روش است که واقعاً کارساز خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68050" target="_blank">📅 01:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68049">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=gIKa8IjVBJPKqTiJAO5P5VFmodtx23qVamLmU7mgU6vefMPWkk62fJugkWjXrHSymO6W538M8JP2ndy8udE4jQMvJzEvv1F5HgKpA8kQAusdNuoe9IZpW8-GU35jZ-Z4Ver8PB2F7tvn0Ta15wp9b1jUHcOEzx7Y_9Caq_hswNk6WPabc1e-rT5mrBvcnta_9ZhPfjp-5VWG4eTxLKqOYpaPTfXR594KD8uGyGo7vDRy4JIt5-E60lHoRQKaHnYUxjxRBKxRV_B_2u_b35NgaELrlo_w6O9rL7b84jazWusDUF-tRDVJbxwvY6mswrLxi3n-hhxJqAuHG7nyAXqEGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=gIKa8IjVBJPKqTiJAO5P5VFmodtx23qVamLmU7mgU6vefMPWkk62fJugkWjXrHSymO6W538M8JP2ndy8udE4jQMvJzEvv1F5HgKpA8kQAusdNuoe9IZpW8-GU35jZ-Z4Ver8PB2F7tvn0Ta15wp9b1jUHcOEzx7Y_9Caq_hswNk6WPabc1e-rT5mrBvcnta_9ZhPfjp-5VWG4eTxLKqOYpaPTfXR594KD8uGyGo7vDRy4JIt5-E60lHoRQKaHnYUxjxRBKxRV_B_2u_b35NgaELrlo_w6O9rL7b84jazWusDUF-tRDVJbxwvY6mswrLxi3n-hhxJqAuHG7nyAXqEGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ارتش آن‌ها را درهم کوبیده‌ایم. ضربات بسیار سختی به آن‌ها وارد می‌کنیم.
ما همین دیروز یا پریروز توافقی داشتیم. کار تمام شده بود، اما آن‌ها بلافاصله توافق را برهم زدند، چون متوجه شدند نکته‌ای در آن وجود دارد که باب میلشان نیست.
طرز فکر و رفتار آن‌ها متفاوت است و ما چنین چیزی را تحمل نخواهیم کرد. ما فقط به پیش می‌رویم.
ما امشب به آن‌ها حمله می‌کنیم. ما تمام توانمندی‌هایشان را در هر زمینه‌ای که به تنگه هرمز مربوط می‌شود، از بین می‌بریم.
گمان می‌کنم در نهایت، کنترل کامل آنجا را در دست خواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68049" target="_blank">📅 01:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68047">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RYw71Ii5qey1i6XXnUbgw_TZXAltoCGRr5DtSGmVIeAEeCnLJcZ1ff6ReAZQR2LupiYiq52X-FFp1LiXWtzIjkxMAlrOOpobnMP0E3-KqxWOEY9A2k5bDFqSLLywMWUBxIM4GjIC8NpNpheLFeSyeUXaKcdcQVzzXHKfdgm5bRfKcIUNb-kxA9Hj_GB63slTNSNnOIQoWVOK1atbbfmXNlTUAId8CxXN96P7KNFxXRlWWwLghQRtJb1ZaMcblTFDPQpfAhkuA4_sJxLHmS21eejxrfJVQNKXHNyeVumEUuY_8LlJgllulx45lliRiV9VJ7NfT34OaN9nkp64-Xip9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RRjFZfw9mQ13fbbHv0mCaXkaEkVCpfhh4dkNKcZ1p-_42pwTVPbFaEeOqUFOPOmH2TfxAuf7tZAKgiTwFe4uh0RAkY6l14NVtnVJlDp6HBUQ4eFkGd6MBy-3EDQHdomZ60CDkWVP0Ec9C4c9PiCvDv3G-ccDufPUWcC8efTub50VaBYVzVaxRWN6zZu-EII94_Ia1ybUPj4OEuCT_7HjmjK3s08ZwCoAMmMayBH_bzjr3jQnUzzWLqGZbK4MUsXB-iwHwm2mC85CCrFcaJ91q5YlebSLWtfwZiQvJ4vugGb3QUVhcmu79hEKYQYBB4NC_ckbztfKjjzeB9cmRP3c1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویری دیگر از حملات آمریکا به جزیره کیش
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68047" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68046">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد  @News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68046" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68045">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع چندین انفجار در  کیش
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68045" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68044">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzDQcnVHyn60OsIGnlKxoY4EOfdGXTT6njmxgpBv7AwNkxkD6cEcCB6ckUzGHeP4Z7n4iuEy1uKlkhP9pks8ToClNE6_ovjb1MtAIWb2tisxmN0UmcnnCsbjGTlTfcUoccRsIZpEW95CRmFbfeWEha5-ppIN-IxgO51yqgAolqbK18p22u954H_phr-NRua8n9xm2fS32NI29CQ65QnOIWGz5ePz0GQAkWhxWk7zD4IsqQ5w6pQk64KFAb8qYxY4aCNc17Lf0EJdLWA-HWlYaYOymCqrrR2gjr_XMBzqW1EdJCBuJCkjqAQuWbelp38f0uf4gGHa_lnuLoGZLfV7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68044" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68043">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9jB3kT4CnvcV6FqYtso32qIC2bXAifHJl8JTvz6afeH7gDJpmeadp9-cyksNdXgqoHj5N_DpnwSJgkHtEj5tjYGUd-c9OURwDQY5I0v39mMVCRU47pseDzSxwaRbxZ0zG_mxAKbkZz6X5MTQpdHC1cyqh7aukFaYpjQWEOKDodWx-XDtYgV4Ec6RX9r3QMwhuEWnqhxcAUb99WPNvWATmlV_hbfee78MY9LikethmTETj06Fz08xWXcjUe3UkdJmgyWno9xFHW9v_4FoD6g42OKDllPKLKznCEnhZ9T2iUP3eo-8SjMYV8h2YtcrsJS6GNkJPXRUVNNiCyO4eAF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68043" target="_blank">📅 00:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68042">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a423066bec.mp4?token=Y5hZc9ep9xYkM23gxdgagGhdVbtqwet6VLTbPm2-vvsTjY-10Q7nYYFK6R0U6UGAuwHcphQgl3J7VxVufOU59kmsAWxuDfLZJHU0hefxPGhpncQWsBCSIM5bCQ6UZh4DWMvo-mXtOWOToGXGnE2c9OpjVnvqJl1FkQE7GOHzTd7KbxNb7wsCwUaw0g3EAh3OLX-NsJI1wDkvr6p8rALDaGrdc9ht0C_i_z0NNlBIEtqbZs4IWpDfq4zM-neDEHhccnzi2Oj0xUMZHE5a0HlzdV6KbG86L5HKpZ61yqs5n0yz4jsuQcEpJtPERuVlMXovdBn4TLaoRuiO75hKnrWiQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a423066bec.mp4?token=Y5hZc9ep9xYkM23gxdgagGhdVbtqwet6VLTbPm2-vvsTjY-10Q7nYYFK6R0U6UGAuwHcphQgl3J7VxVufOU59kmsAWxuDfLZJHU0hefxPGhpncQWsBCSIM5bCQ6UZh4DWMvo-mXtOWOToGXGnE2c9OpjVnvqJl1FkQE7GOHzTd7KbxNb7wsCwUaw0g3EAh3OLX-NsJI1wDkvr6p8rALDaGrdc9ht0C_i_z0NNlBIEtqbZs4IWpDfq4zM-neDEHhccnzi2Oj0xUMZHE5a0HlzdV6KbG86L5HKpZ61yqs5n0yz4jsuQcEpJtPERuVlMXovdBn4TLaoRuiO75hKnrWiQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
منتسب به سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68042" target="_blank">📅 00:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68041">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
انفجار ها در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68041" target="_blank">📅 00:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68040">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
تپه الله اکبر زدن بندرعباس ایستگاه رادیویی
گزارش ممبرای چنل
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68040" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68039">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
چندین انفجار در کیش
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68039" target="_blank">📅 00:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68038">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68038" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68037">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lwr75F6P2cPLn9lKzDLH5G9HVSyYcbqkf0Yhj2JosjWyfWCKSiEz5coml1o29Mvsor6t2hJ2HAVBBK0Jg0tiTi02-0c1AH4HLvAS4ZqztH-zLl3ZgEmd2prss8_GOKu__vmfkLeqjaykrDFtnVUb4AWJYoKLF6ACYkQlKh-LPYZxvkjDKeqjvYs14KQI2gqHa0wAS0au_ZWYRrpvNOg7QD8eJ3Ksaq5oGE-yx0hmv57a0rH55hucfM-3pBSujwmmAzs_Py0I-EGqdaSnH18iuVOy_xVqLy8XRQ0ckVWeNk8iZsadED5O90lpaQ-F0qdmiUBZWkUnDYf5oVynLK3yPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
امروز ساعت ۴:۴۵ بعدازظهر به وقت شرقی، فرماندهی مرکزی ایالات متحده به دستور فرمانده کل، سومین شبِ پیاپی حملات علیه ایران را آغاز کرد. این حملات همچنان هزینه‌های سنگینی را بر نیروهای ایرانی تحمیل کرده و توانایی آن‌ها را برای حمله به غیرنظامیان بی‌گناه و کشتی‌های تجاری در تنگه هرمز تضعیف خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68037" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68036">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های اولیه از وقوع دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68036" target="_blank">📅 00:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68035">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a4e2ce60.mp4?token=SeF9fWEuqOgygqaxTa8T5WtGe1QzhBXGDYXlYS8MkFSOiohXQWk1g5d_n5paUb__d3fUNi09nvzKLhewSeaaVXyE2RmTGwl5rCHL78WGXL1XwDH-SOJUT8GeKYMCgCXGetkQarJRvOqROA0fZwqd2jHrSJGxezeA1Ph-AVhvVi8PwiIKHTNmxMMv1NQ4F7PcYiwYf_Kkna-x_TMEreOCaH3Hq-NaxqXPOJyeuOjqWLQ91hxI0s3JvRSeb4jzBDdr8rbL3acDDO8XN3n4DsYPnpr9iObiw5ulytgTZhAdgfaGHA6SSjmYl9eZluif39BhsVyFBukMhBsYGdoMy00wcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a4e2ce60.mp4?token=SeF9fWEuqOgygqaxTa8T5WtGe1QzhBXGDYXlYS8MkFSOiohXQWk1g5d_n5paUb__d3fUNi09nvzKLhewSeaaVXyE2RmTGwl5rCHL78WGXL1XwDH-SOJUT8GeKYMCgCXGetkQarJRvOqROA0fZwqd2jHrSJGxezeA1Ph-AVhvVi8PwiIKHTNmxMMv1NQ4F7PcYiwYf_Kkna-x_TMEreOCaH3Hq-NaxqXPOJyeuOjqWLQ91hxI0s3JvRSeb4jzBDdr8rbL3acDDO8XN3n4DsYPnpr9iObiw5ulytgTZhAdgfaGHA6SSjmYl9eZluif39BhsVyFBukMhBsYGdoMy00wcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ :
«کوه پیکَکس رو از بین می‌بریم.
به ایرانی‌ها بگید که داریم میایم.
و هیچ کاری هم از دستشون برنمیاد!»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68035" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68034">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5e2a3c36.mp4?token=ZUGo41gduBhwmbt1ekLGoFgrgKP8e9oDRd3wViSUIX0rdYnNGHUeYhUZS3Te8R8aq-1Sjv64oQ8Xhz3TDheVpMGA6iaSYzn9MaOtMoX6JQirlFdRLk_g-9vnQre3vLm_ycMqyqrHGObqHb-uNqjsC_NIdtr-9qAy4X2yHm9k8bF3mikkbbz893KwF-QefpiGzEP3pTIe0lIqgXxx_DciRLBhvTczzsP-SvzWQuonYgR5ik1Bu16FYe8NPNBPe83EU33PKJbatluaI-IDvalP0_TeelZXJ6DnU6TuDOkw-bPYNTP3uYGxnfUMyiTzRWQketksUx_zth-pLpa79J49Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5e2a3c36.mp4?token=ZUGo41gduBhwmbt1ekLGoFgrgKP8e9oDRd3wViSUIX0rdYnNGHUeYhUZS3Te8R8aq-1Sjv64oQ8Xhz3TDheVpMGA6iaSYzn9MaOtMoX6JQirlFdRLk_g-9vnQre3vLm_ycMqyqrHGObqHb-uNqjsC_NIdtr-9qAy4X2yHm9k8bF3mikkbbz893KwF-QefpiGzEP3pTIe0lIqgXxx_DciRLBhvTczzsP-SvzWQuonYgR5ik1Bu16FYe8NPNBPe83EU33PKJbatluaI-IDvalP0_TeelZXJ6DnU6TuDOkw-bPYNTP3uYGxnfUMyiTzRWQketksUx_zth-pLpa79J49Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره صالح محمدی کشتی گیر اعدام شده :
«اون کشتی‌گیر یکی از بهترین کشتی‌گیرهای دنیا بود.
فقط به خاطر اینکه درباره حکومت حرف زده بود، اون و دو تا از دوستاش رو کشتن؛ حتی حرف خیلی تندی هم نزده بود.»
این ادم ها خیلی وحشی ان!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68034" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68033">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
خبرنگار:
«آیا تفاهم‌نامه‌ای که تیم مذاکره‌کننده شما از ایران آورد، از همون اول قرار بود شکست بخوره؟»
🔴
ترامپ:
«نه، اون برای آزمایش بود؛ یه تست بود. نمی‌دونستیم نتیجه چی می‌شه.
ببینید، وقتی با یه مشت آدم حقه‌باز طرف هستید، تفاهم‌نامه ارزش زیادی نداره.
البته حتی با آدم‌های قابل اعتماد هم تفاهم‌نامه خیلی ارزش حقوقی خاصی نداره؛ چون فقط یه تفاهم‌نامه‌ست.
من هم گفتم اصلاً چرا باید اول تفاهم‌نامه امضا کنیم؟ توی آمریکا معمولاً اول تفاهم‌نامه امضا می‌کنن و بعد میرن سراغ توافق نهایی.
من گفتم از همون اول برید سراغ خودِ توافق.
ولی در نهایت، اون تفاهم‌نامه یه جور آزمون بود و اونا توی این آزمون موفق نشدن؛ به تعهدشون عمل نکردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68033" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68032">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره هدف قرار دادن مقام‌های باقی‌مانده حکومت ایران:
«ما قطعاً اون‌ها رو زیر نظر داریم. آره، اطلاعات زیادی درباره این موضوع دارم، خیلی هم می‌دونم، اما فکر نمی‌کنم الان زمان مناسبی باشه که درباره‌ش حرف بزنم.
باید ببینیم چی پیش میاد. مثلاً امشب حسابی بهشون ضربه می‌زنیم و فردا هم همین‌طور. هیچ کاری هم از دستشون برنمیاد.
اونا هیچ چیزی ندارن؛ تنها کاری که بلدن اینه که لاف بزنن. و فکر می‌کنم کاری که من انجام دادم، کار خیلی درستی بود، چون باعث شد بیشتر باهاشون آشنا بشم...»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68032" target="_blank">📅 00:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68031">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfd8c6550.mp4?token=C8QmxBTNN9voCifJFwgVMgP1TcspvmBoDU0O0DB4oFdLro8E9AW1FPlb7wMAolWtIvgw9bGAAUi7N0u3lap_1jAsqZ94V0JgTMxt_cTLNtN9tXT1Yz-Ti93WgBLYcM7u0KKLiKuiL17brXLfxg_MUuesTHsOA-aGVqeUIfK1fOcDNfMvqR4G3MMa5EeZWfjurZlFEzuvv9ue5cCyMkdiu8HPHD9v2GfmQJ4Cw0SVRev_-x2E6wwS9uimplvfXAUSd427r8t8Mb8HPeHm7RVfnMQZl3fVjTL0TABCg_XWd3z76w6OJdMqw3nNyyMHTBnXARlikVQtIM6PLrV7tJkHOUJrQP3iDFA8w887oR-O_qh4wtKGrrQrx1rN8upv8TmxiUTAsnTUqKVxZ3KQoGJo42zr_Y8hU1DJyVJjMJGhmsWU8nsItAweZ7g-wM4Q7PuIp3kAAff88h27OiUDezHTrAc30RQLFS7jwdEn5TwxNEHQIjUH6YqwrFh1rOxxg6RFk0pdhxGXZ2Bbawgatha8mHOuoqcihiyMdsAECa4zCKfkpjogKGJ08IoBssfS-VxB_4jwbAZYU_fDEWuvGiqdkP-jfPi8r1hITDplLuu5H0hSKbQUp-L0uxoe3PV_YNxNauwcwmttKXsrbhae4aBAaOvwRpqL_f6DB68rQa4rJnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfd8c6550.mp4?token=C8QmxBTNN9voCifJFwgVMgP1TcspvmBoDU0O0DB4oFdLro8E9AW1FPlb7wMAolWtIvgw9bGAAUi7N0u3lap_1jAsqZ94V0JgTMxt_cTLNtN9tXT1Yz-Ti93WgBLYcM7u0KKLiKuiL17brXLfxg_MUuesTHsOA-aGVqeUIfK1fOcDNfMvqR4G3MMa5EeZWfjurZlFEzuvv9ue5cCyMkdiu8HPHD9v2GfmQJ4Cw0SVRev_-x2E6wwS9uimplvfXAUSd427r8t8Mb8HPeHm7RVfnMQZl3fVjTL0TABCg_XWd3z76w6OJdMqw3nNyyMHTBnXARlikVQtIM6PLrV7tJkHOUJrQP3iDFA8w887oR-O_qh4wtKGrrQrx1rN8upv8TmxiUTAsnTUqKVxZ3KQoGJo42zr_Y8hU1DJyVJjMJGhmsWU8nsItAweZ7g-wM4Q7PuIp3kAAff88h27OiUDezHTrAc30RQLFS7jwdEn5TwxNEHQIjUH6YqwrFh1rOxxg6RFk0pdhxGXZ2Bbawgatha8mHOuoqcihiyMdsAECa4zCKfkpjogKGJ08IoBssfS-VxB_4jwbAZYU_fDEWuvGiqdkP-jfPi8r1hITDplLuu5H0hSKbQUp-L0uxoe3PV_YNxNauwcwmttKXsrbhae4aBAaOvwRpqL_f6DB68rQa4rJnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
«به نظرم اینا یه کم دیوونه‌ان؛ در واقع فکر می‌کنم همشون همین‌طورن.
اول رژیم اولشون رو از بین بردیم، بعد رژیم دومشون رو زدیم و بعد هم حدود ۲۵ درصد از این رژیم رو نابود کردیم. اینا طرز فکر متفاوتی دارن.
دیروز به یه توافق رسیده بودیم؛ تقریباً همه‌چیز ۱۰۰ درصد نهایی شده بود. اما یه دفعه یه تماس تلفنی گرفتن و همشون از اتاق بیرون رفتن.
این آدم‌ها واقعاً دیوونه‌ان. ما به توافقی رسیده بودیم که همه‌چیز به نفع ما بود، اما اونا دوباره زیرش زدن. از نظر اونا، توافق برای اینه که بعداً نقضش کنن.
اصلاً نمی‌شه بهشون اعتماد کرد و راستش رو بخواید، اگه یه روز به سلاح هسته‌ای دست پیدا کنن، ظرف یک روز ازش استفاده می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68031" target="_blank">📅 00:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68030">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
خبرنگار:
«
آیا شما یا ارتش آمریکا، یا حتی ارتش اسرائیل، می‌تونید به فرمانده‌های رده سوم، چهارم و پنجم ایران برسید؟ می‌دونید کجا هستن؟ می‌تونید اون‌ها رو از بین ببرید؟»
🔴
ترامپ:
«آره، می‌دونم. ولی نمی‌خوایم درباره اون صحبت کنیم. البته که زیر نظرشون داریم.
من اطلاعات زیادی درباره این موضوع دارم، اما فکر نمی‌کنم الان زمان مناسبی برای حرف زدن درباره‌ش باشه.
ولی... امشب حسابی بهشون ضربه می‌زنیم و فردا هم همین‌طور. هیچ کاری هم از دستشون برنمیاد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68030" target="_blank">📅 00:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68029">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
تاسیسات اتمی  خاصی در منطقه کوهستانی موسوم به " کوه کلنگ " در جنوب نطنز قرار‌ دارد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68029" target="_blank">📅 00:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68028">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ccfca9a7.mp4?token=GQ_atlqY8O2KMQaaJvzU4TE8OIpwuUIaXiBmiWZnLWbVQSwFraSKr5Bf9BBkU1KdvJH4mCX99A2mT5alkXePy5BXZqDMy8mwvXfaPjIUPpvTS7aWxhXk9tSP1vU8FiGe2vua55BUa9KJnP6My4p_yo2dnMUCd-Nz_nfU-d035iuI8Vofz1ldGFIQwxYVuCelwd-PKm_6lHMzwuGMJDgqu0V2osp4rdh6btuu266040MX3l7dxF7DO68B-Qn0-9cSF1QNypMSPhVLZMt_iNZdT7N5h4lTGf8SV3W3OOegF0_h-eZJ7D-S1_8d07eK4e3ZsehnKhZT6XeVmj0zvYCad1KiKV3foDNTmSA0s2pV3b7Y4XPLwN9wRmbfD99zpVid-6OZ-AEd0PVu2Oe2uzUFQxXrhmkq_So7Tl2ncCZE-NvfVjMmAC72slFDKxb-4a9bYlXhQ-l7zAUEyvFhm09W-eSAjucNf-sAw9UlHHr8FGqoyZoG_goWQXqdjvbNXPbkApbjqMYe7i88MuycQOvn6sDbdQ3fBMQmaDKMCr5U-wDHN9xIwmUjlnVI5pVETVgnvOdYS6J5dA61EOveEKkCsBMrXjr9aZJ93wWVokjSWnHAedh5EjT8U3Z6SClTfrqgbSBsbk0t67BSEmVqEVrJP4FnnIhJuvLrpylMSJ7Ewf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ccfca9a7.mp4?token=GQ_atlqY8O2KMQaaJvzU4TE8OIpwuUIaXiBmiWZnLWbVQSwFraSKr5Bf9BBkU1KdvJH4mCX99A2mT5alkXePy5BXZqDMy8mwvXfaPjIUPpvTS7aWxhXk9tSP1vU8FiGe2vua55BUa9KJnP6My4p_yo2dnMUCd-Nz_nfU-d035iuI8Vofz1ldGFIQwxYVuCelwd-PKm_6lHMzwuGMJDgqu0V2osp4rdh6btuu266040MX3l7dxF7DO68B-Qn0-9cSF1QNypMSPhVLZMt_iNZdT7N5h4lTGf8SV3W3OOegF0_h-eZJ7D-S1_8d07eK4e3ZsehnKhZT6XeVmj0zvYCad1KiKV3foDNTmSA0s2pV3b7Y4XPLwN9wRmbfD99zpVid-6OZ-AEd0PVu2Oe2uzUFQxXrhmkq_So7Tl2ncCZE-NvfVjMmAC72slFDKxb-4a9bYlXhQ-l7zAUEyvFhm09W-eSAjucNf-sAw9UlHHr8FGqoyZoG_goWQXqdjvbNXPbkApbjqMYe7i88MuycQOvn6sDbdQ3fBMQmaDKMCr5U-wDHN9xIwmUjlnVI5pVETVgnvOdYS6J5dA61EOveEKkCsBMrXjr9aZJ93wWVokjSWnHAedh5EjT8U3Z6SClTfrqgbSBsbk0t67BSEmVqEVrJP4FnnIhJuvLrpylMSJ7Ewf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«آیا الان وقتشه که مردم ایران دوباره به خیابون‌ها بیان؟»
🔴
ترامپ:
«نه، اونا نمی‌تونن این کار رو بکنن. چون سلاحی ندارن و فعلا وقت قیام نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68028" target="_blank">📅 00:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68027">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c72608b58f.mp4?token=kVkKq1xreOQf_IG0RfDvCSTxcT5L75E3serpBa193aanI-pQQSoxGokYqLpMFrkVSEqeFCS2ncmxPDu65ohCgh0xTM_EppLY2o7hLImz_Z213dZ8j9rxdNJVEU4yarOTjG2f1HvZcLKYvXQyTge3Bu5wjm8NEopxoY2xsh8B8Vk78Jer4Y2Ou72otDZtyzt-kS7QB3iBHmrGQdzPcOZRzA5AXjwQDVFMrIP0HOk35Yxdniv0RMNXbBbuasSeXPs9UoaBs0MqbWY_Bzyz53LCbFwJAljfxw_T0WhBJc6zH6WaC16Ts7QJ0GgX-k-HMWUeBqhoB51qIN6QhZkU07HOdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c72608b58f.mp4?token=kVkKq1xreOQf_IG0RfDvCSTxcT5L75E3serpBa193aanI-pQQSoxGokYqLpMFrkVSEqeFCS2ncmxPDu65ohCgh0xTM_EppLY2o7hLImz_Z213dZ8j9rxdNJVEU4yarOTjG2f1HvZcLKYvXQyTge3Bu5wjm8NEopxoY2xsh8B8Vk78Jer4Y2Ou72otDZtyzt-kS7QB3iBHmrGQdzPcOZRzA5AXjwQDVFMrIP0HOk35Yxdniv0RMNXbBbuasSeXPs9UoaBs0MqbWY_Bzyz53LCbFwJAljfxw_T0WhBJc6zH6WaC16Ts7QJ0GgX-k-HMWUeBqhoB51qIN6QhZkU07HOdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند تا از حامیان حکومت توی آلمان تجمع کرده بودن که یکی از مخالفان حکومت اینطوری یکیشون رو سورپرایز کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68027" target="_blank">📅 00:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68026">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3b137e2a.mp4?token=fO_apA2xiW90WHT-LjR4esbRNJq9myH9iBxpCVIFLi7sXbsqTWzOLmrJNbjS0iI--fdh1OlD-oJnwohTlamwk0WwYZKa0qmMk-DKAaS5e_WW_byqHg4UX6r_Ud-wORj2AswZjWqofbJtvCcY5u3XXtbVYdSsRKTMXw-NIij_hYg7VVfJPIxUEKu0I-6JNch2Y3WaiKhIjSLS__MwKhUrwZxOrSVSVO9mk_9KF2fLTK2hvEJhY7d7I9Gl1My4Sz9Rko0N-gNwrzKShVp1Gn2QiDr_q9kWP9UieADU2TeID0UdcjFeUrgWvm-WNwfldRUuL7qEbxsNFunZP0pSCBIe3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3b137e2a.mp4?token=fO_apA2xiW90WHT-LjR4esbRNJq9myH9iBxpCVIFLi7sXbsqTWzOLmrJNbjS0iI--fdh1OlD-oJnwohTlamwk0WwYZKa0qmMk-DKAaS5e_WW_byqHg4UX6r_Ud-wORj2AswZjWqofbJtvCcY5u3XXtbVYdSsRKTMXw-NIij_hYg7VVfJPIxUEKu0I-6JNch2Y3WaiKhIjSLS__MwKhUrwZxOrSVSVO9mk_9KF2fLTK2hvEJhY7d7I9Gl1My4Sz9Rko0N-gNwrzKShVp1Gn2QiDr_q9kWP9UieADU2TeID0UdcjFeUrgWvm-WNwfldRUuL7qEbxsNFunZP0pSCBIe3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ خطاب به مردم ایران:
«کشور ما می‌خواد به شما کمک کنه و دوست داریم همه‌چیز به‌خوبی حل‌وفصل بشه.
افرادی رو داریم که آماده، مشتاق و توانمند هستن، اما اول باید بدونن شما خودتون چه تصمیمی می‌خواید بگیرید؛
این انتخاب با خود شماست.
ممنونم و خدا نگهدار ایران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68026" target="_blank">📅 00:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68024">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یکم بالاترو نشونه بگیر املاکیِ پدراشتراکی، بیچاره جنوبیا خسته شدن #hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68024" target="_blank">📅 23:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68022">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:   امشب و فردا با قدرت به ایران ضربه خواهیم زد  @News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68022" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68021">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
یاداشت تفاهم با ایران یک آزمایش بود و آنها به آن پایبند نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68021" target="_blank">📅 23:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68020">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
امشب و فردا با قدرت به ایران ضربه خواهیم زد
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68020" target="_blank">📅 23:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68019">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
صحبت های امروز ترامپ با زیرنویس فارسی
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68019" target="_blank">📅 23:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68018">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
تسنیم:
چند کشتی متخلف در تنگه هرمز هدف قرار گرفته شدند
.
منابع محلی از هدف قرار دادن چند کشتی متخلف در تنگه هرمز خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68018" target="_blank">📅 22:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68017">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c2989693.mp4?token=OHsyduQ4_unTHCSz-jeZYeZhyBvpkpx2tbY40odSLTHlM0C8wqH0s7nDXIPa_bRN5tZrpjiPnWq90g9zCV-KvKa1auRzqmm4jiq9kPeJk8wrauD8twh3bQyFqHhyQXvd_GRruUbVbbF-WhFiQg17PgbCbMXEr5HTuYDUXEyDRB2yBDA0uB_dn4ApysEpwKyTd1yjT9Hwj7c2IB5jVitFuYJdy5958gzOLpp8ItJCVf9fXs-uoUj4sHKuZNwRvR5nfFUDp3C-QHQV7RevH7oQMKZDPUBhnuvfy-aiyOJkc2RFfnPaPJ3Yxy5oBMJoURyrpU7bxwqypm1GkB61PhKpYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c2989693.mp4?token=OHsyduQ4_unTHCSz-jeZYeZhyBvpkpx2tbY40odSLTHlM0C8wqH0s7nDXIPa_bRN5tZrpjiPnWq90g9zCV-KvKa1auRzqmm4jiq9kPeJk8wrauD8twh3bQyFqHhyQXvd_GRruUbVbbF-WhFiQg17PgbCbMXEr5HTuYDUXEyDRB2yBDA0uB_dn4ApysEpwKyTd1yjT9Hwj7c2IB5jVitFuYJdy5958gzOLpp8ItJCVf9fXs-uoUj4sHKuZNwRvR5nfFUDp3C-QHQV7RevH7oQMKZDPUBhnuvfy-aiyOJkc2RFfnPaPJ3Yxy5oBMJoURyrpU7bxwqypm1GkB61PhKpYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
انفجارهایی در شهر کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68017" target="_blank">📅 22:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68016">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
بیرجند، چابهار و سایت موشکی لار لحظاتی قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68016" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68015">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQWTWdTo3i8B50WaKpz_CEHEAMFZVIItKCuulHWBV3DSAxdENnhATJoUZ9mJvjlD7R-9vlUKMVSo8fFIt7vbBm0vo8qu1APlVXpaxpK7XQRrx-1USOF7UqWKvTukJMHOd0Lh8nwPHxPLfV2J-f5ZoyyGcz6jj0Y9R89wgx289lpFVvym6493dr5aGsapDJP--TyT_IvC-OtBO2FJFF9lWEYz9fI2T61tKJ3bt7_agYWHjXSyq-FAhJHnTrHJ-9QoWVk4U6MBWkvZYbVrYrQhCHC1fs7YzQpY3HWXxeDS1kZa5fuLd3e0YSiLOShh2JxXvgdVtONH-B1WXCfe_P7mMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:
رئیس جمهور ترامپ پنجشنبه شب، ساعت 9 شب به وقت شرقی، خطاب به ملت سخنرانی خواهد کرد.
از توجه شما به این موضوع متشکرم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68015" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68014">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5DnXuwi4lKInL4OE37kVlsnIc4wWkmUK05FFw9fGcFB7DSxJODIlGPZFwDIERnnN6gnTeQxWTve4ed3-yyZKILW5Eb1C3uyNBGcl_hBfceA6VnJB9oy7FBP2wKYxcOjKvuupd8Sb5MSezNsH8TzPbpTQMn6xXLlHkkBkQYhoQvVt4MsiTrUTE6FwWvlVIpBxFXftPEV2vZfcTWJa9wf8f6gAyMvko4DiKBCL9A4EdXy_clB4QJlKkXPpgF-Uis6hSiPGN1osdDku6KDBFknao4VAEnkMSOI82Cm4cewW_qjc7jZmtk6PsbjR53XO-Txhp_9MeePjLTGplPnt6W3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عباس عراقچی، وزیر خارجه جمهوری اسلامی:
رئیس‌جمهور آمریکا کاملاً حق دارد. هر کسی که عبور امن و ایمن کشتی‌های تجاری از تنگه هرمز را تأمین کند، باید بابت این خدمت پاداش دریافت کند. ایران همواره «نگهبان» این تنگه بوده و «برای همیشه» چنین خواهد ماند. البته ۲۰ درصد رقم بسیار بالایی است؛ ما منصفانه عمل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68014" target="_blank">📅 22:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68013">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار سنگین در بندرعباس و کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68013" target="_blank">📅 22:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68012">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxHdb9CLXRIR2fDOvpJNK5vqMQvF-PSAHVKrg-5qNKs4SfVDrG_Cq5rBp7aKLZmtbAo4oBwnocCY8wf-V7l1mbzdoiI0kQx9s4QEv5FyQhsC3eTBnLOO7_62oKClFtzldMJ1pCnLSgYMCgoWuf5jSI4EfJudJ7meX6z3flOLZQsIqrXt21eDbQjTxn1SBaEOlZRTdNShNccXagiTldWg0kICo7QGj7EKUYu_2ktOejwLpQX-DkRThp8vDY1Fru3B8gLQTb2n5cTelX4I5cgbiG9TaHFvwt3GKtoGclZNU5nw1k9UKYoKa4FTPjEJ_uROphCf1lALASeVibMsRK5bBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
فووووری؛ نیویورک تایمز: ترامپ به کنگره رسما اطلاع داده که درگیری با ایران از سر گرفته شده
آمریکا و ایران بار دیگر به لبه جنگ نزدیک می‌شوند. ترامپ اعلام کرد که امریکا، محاصره دریایی بنادر ایران را از سر گرفته و قصد دارد 20 درصد مالیات بر کالاهایی که از تنگه هرمز عبور می‌کنند، وضع کند.
پس از یک شب دیگر از حملات، به نظر می‌رسد که آمریکا و ایران به درگیری‌های شدیدتری که قبل از آتش‌بس وجود داشت، بازگشته‌اند، زیرا طرفین با اظهارات تحریک‌آمیز به یکدیگر پاسخ می‌دادند و رئیس‌جمهور ترامپ اعلام کرد که محاصره دریایی بنادر ایران را از سر گرفته است.
آقای ترامپ همچنین رسما به کنگره اطلاع داده است که درگیری با ایران از سر گرفته شده،
که اعترافی به فروپاشی آتش‌بس است و این موضوع، جدالی بر سر اختیارات جنگی حیاتی را تشدید می‌کند. کنگره به رئیس‌جمهور دستور داده است که یا جنگ را پایان دهد یا برای ادامه آن درخواست تاییدیه کند، اما آقای ترامپ اصرار دارد که او تنها کسی است که حق تصمیم‌گیری در این زمینه را دارد. این نامه که روز جمعه ارسال شده بود، روز دوشنبه توسط روزنامه نیویورک تایمز به دست آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68012" target="_blank">📅 21:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68010">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joOglEB-9evc5o9abnVCnUnloXMqFxofCacqcyunMcaqhQn_18GoNwulFcNLKWQgRKaJMnD9jnBLNQlMwUZWb5fXXKxV08Ge_1kd0vABFBWtethT8XkwZYDJ0x_gFGEM8VwhsyiTtV1YfgYDxXKWqtan5QUXiFtn2Hc4DWzB1bKmO7u2xE7ICDdv0jnli4zPmqsqT3wtRsPIqh3fnEc288gHuOi06omj7nfKn375oG9ZcPFF8LKiqM2PcvhK2NMSHPaeRhixfn7haSY-tG0WIbGu11hHzfqXIW62ewy27QG5U6LhBebyJ9SD1l3Sm-RSMMNuh_dJIqGQnUgJk07Cfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛ایالات متحده اعلام کرده است که از ساعت ۲۰:۰۰ به وقت گرینویچ(۲۳:۳۰ به وقت ایران) در روز ۱۴ ژوئیه، محاصره دریایی تمامی بنادر و آب‌های ساحلی ایران را به اجرا خواهد گذاشت و تمامی کشتی‌ها — صرف‌نظر از پرچم کشورشان — مشمول این اقدام خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68010" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68009">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma54qQ2JGF41oNuZx4bOLe_VVhedz0afC6tls3VaJXgFa2kay4dybo0-SzyZTftXLG9T0aA48ceGsZTBapjUaOyLucVIbieTMNHvWswM7NzVSqnnevZz0-kc858G5Im3-GSIuMsKBThOGiFCIJu4BTXaILQ5avukKaCCQ-mYVkf1nGjSUBFKXSLdgO1wUXBUNkselQ41sms37S3yrBX0Ch_S1x8g75OrBUPnIzJIeoq9vRYmCrpGCAohAe3N3vQG_tVISBs6ShVrTh3cC-GZdXjwvRdkr5anCgweGicf71Q9k6H-ioSfWX0ZC975FSVmQs6d5A7CH7k4505s4WWqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/news_hut/68009" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68008">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
هواپیما جمهوری اسلامی داشت میرفت سمت فرودگاه صنعا، این فرودگاه بلافاصله توسط جنگنده های عربستانی بمباران شد.  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68008" target="_blank">📅 21:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68007">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33092f28c9.mp4?token=nr23JTSmajIK98DbJPzNJcN6IYxgYWN5WL7BG1yoIQguH9J3Vzb1Yhat4SRXkYrjXjs0lU1v0oteLl32aspyEui-VSHkcXmgB0CMs9yJaajrsvF1_OJyxW31Lzk3I1gNjdWeEvcwTJKoI_YlY2grJIInxiwK6i_-rDDT8m1ZOywcGVeVdT-QY9puClgVsogPme4CzuohQei9c3FHIk4DHaE-ghzpXD8h88tOtwzg3brfu1xUoQTvK2apE0UrfP2ASyOLXX5Q1fxZZbQViVHP2rqyrtKQYaiRWGUoeG5wF15MEsttTSEEt2vQqLOIq-HXrniIdYejBTpzyXmpryui0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33092f28c9.mp4?token=nr23JTSmajIK98DbJPzNJcN6IYxgYWN5WL7BG1yoIQguH9J3Vzb1Yhat4SRXkYrjXjs0lU1v0oteLl32aspyEui-VSHkcXmgB0CMs9yJaajrsvF1_OJyxW31Lzk3I1gNjdWeEvcwTJKoI_YlY2grJIInxiwK6i_-rDDT8m1ZOywcGVeVdT-QY9puClgVsogPme4CzuohQei9c3FHIk4DHaE-ghzpXD8h88tOtwzg3brfu1xUoQTvK2apE0UrfP2ASyOLXX5Q1fxZZbQViVHP2rqyrtKQYaiRWGUoeG5wF15MEsttTSEEt2vQqLOIq-HXrniIdYejBTpzyXmpryui0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی اقتدار و وطن‌پرستی محمدرضا شاه پهلوی و قدرت ایران، جهان غرب را به واکنش واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68007" target="_blank">📅 20:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68006">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c93097e540.mp4?token=bVixjQxEYXtvjpakQZctrdtKfYKa7Z-9Wa57uGbkaZHLYfPFi_o-d71VhKUkb-KfCb-_cX8CAMYBf_EJhawZt3dZDb-gLWDDkc1_ynmXctmxBQoV5LuElABHyF7oO2i1hpGl2gOHCmfceh_lpqq9JhsiPVaP4mSJvEJes-hgiPQgOKNMtYUuR_KgWTY2bYT-psp1Ni0an7jj0qLUd1-_7dwu8YvrIVwuQph1bqK-eGzpQoyJ3qG7NIY3QHBEvQU8Q2wxTzbnfMqTKXVz8PQUdNGl4D7_yr636sRS7SmAWearR3qBh7i8v4xTvLwPVlisLgRoGKy3qtwRz16W9JMStHJ6_yTVd7W2K4CG0lgTq9QfFGPRjnuHwahGdPxpREk0YF2vWzQuCrG9xHIs2PJctLXt8zZebrHDzwozEGpNYDSL0FRCEWr17W7DoLT5rRqB0o4ngjLZjkZ0QR7l6_177FcXW3VVBZ3ed744TUE6HnwzeDpHINMPEo3zebeSoY6ddpPB8RQKplxvKExLeKmqDcm9drfSmngj4CJARLYC723RDo-JsIQK9n0cWUL9qmvIhgFsLjaYtdz8bs2euOHSMufTES93y8YKCPl4VEDuGl7ptH5n-bd5HLwe0U42qyKBgDNWniUD-CC-E61K0nMwXlnjcJ2iMkPjyDryYyArNsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c93097e540.mp4?token=bVixjQxEYXtvjpakQZctrdtKfYKa7Z-9Wa57uGbkaZHLYfPFi_o-d71VhKUkb-KfCb-_cX8CAMYBf_EJhawZt3dZDb-gLWDDkc1_ynmXctmxBQoV5LuElABHyF7oO2i1hpGl2gOHCmfceh_lpqq9JhsiPVaP4mSJvEJes-hgiPQgOKNMtYUuR_KgWTY2bYT-psp1Ni0an7jj0qLUd1-_7dwu8YvrIVwuQph1bqK-eGzpQoyJ3qG7NIY3QHBEvQU8Q2wxTzbnfMqTKXVz8PQUdNGl4D7_yr636sRS7SmAWearR3qBh7i8v4xTvLwPVlisLgRoGKy3qtwRz16W9JMStHJ6_yTVd7W2K4CG0lgTq9QfFGPRjnuHwahGdPxpREk0YF2vWzQuCrG9xHIs2PJctLXt8zZebrHDzwozEGpNYDSL0FRCEWr17W7DoLT5rRqB0o4ngjLZjkZ0QR7l6_177FcXW3VVBZ3ed744TUE6HnwzeDpHINMPEo3zebeSoY6ddpPB8RQKplxvKExLeKmqDcm9drfSmngj4CJARLYC723RDo-JsIQK9n0cWUL9qmvIhgFsLjaYtdz8bs2euOHSMufTES93y8YKCPl4VEDuGl7ptH5n-bd5HLwe0U42qyKBgDNWniUD-CC-E61K0nMwXlnjcJ2iMkPjyDryYyArNsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه از هیجان پایین جنگ ایران و آمریکا خسته شدین؛
پیشنهاد میکنم این شوخی معمولی پسرونه بچه‌های بلوچ رو تا آخر ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68006" target="_blank">📅 19:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68005">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e510433ba3.mp4?token=Qae8f7-1MjGvUkRiWB9I9Z9CKOsiD5QfRgD_4WqsAc9XYFaWhWJRQvWe4HCdAyqga-3pceMycyKjyPBUMYQVJM05OA0XeM0mNPj0gI6a6ACTtYuy-fKQuG-fOa9-TjzkrLouTcKSUBD6BqSOlktcfUv90N26CWNF8HaqSHyUYY38W1NNLPJqv5sAHG15s97yuu2AaHFx2DNloK_fvSdaeCdLXRRV-X0RZT32c2hl1K_t4AuKg7Ab7PNaYKsjbLbhuCh-FXcJC06pflaTo1A_Khf3K9rm9CrMRPII03FyrlO5hzDpKUZ_zdLdhfG1-pa7SdqmceZSPVq8WHHeNow4O6O84LbQ5KREHgsqfLNlElZAJ5EsVFYE6PWnndIpRABXtMg5fimW37GeXHzPeGOJFHGw985n7MZfLNOsewpBw2pbhhf-eiv6QLerm23UBiZb84xU_vph47qvfQieUS1GQFxo1x03kj1tJ0tsc8JHiKkdhFQGUO3JFpWmyGigZWUdclATKRiTeqXAMZk0fgxLfCLUh6fpfwrs2vIcFwCB5dcg_BVVm49gBta4ozDx0nu07iRj-Bw9ToPynZuG1DKgpX_wudv7JKcyMqPSSDZTcRTm1KlzxM25PceDWMz52v-xEbCne26RcyNnonDdXIGYtXbiy7rNriVH8uZ5yCDRpAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e510433ba3.mp4?token=Qae8f7-1MjGvUkRiWB9I9Z9CKOsiD5QfRgD_4WqsAc9XYFaWhWJRQvWe4HCdAyqga-3pceMycyKjyPBUMYQVJM05OA0XeM0mNPj0gI6a6ACTtYuy-fKQuG-fOa9-TjzkrLouTcKSUBD6BqSOlktcfUv90N26CWNF8HaqSHyUYY38W1NNLPJqv5sAHG15s97yuu2AaHFx2DNloK_fvSdaeCdLXRRV-X0RZT32c2hl1K_t4AuKg7Ab7PNaYKsjbLbhuCh-FXcJC06pflaTo1A_Khf3K9rm9CrMRPII03FyrlO5hzDpKUZ_zdLdhfG1-pa7SdqmceZSPVq8WHHeNow4O6O84LbQ5KREHgsqfLNlElZAJ5EsVFYE6PWnndIpRABXtMg5fimW37GeXHzPeGOJFHGw985n7MZfLNOsewpBw2pbhhf-eiv6QLerm23UBiZb84xU_vph47qvfQieUS1GQFxo1x03kj1tJ0tsc8JHiKkdhFQGUO3JFpWmyGigZWUdclATKRiTeqXAMZk0fgxLfCLUh6fpfwrs2vIcFwCB5dcg_BVVm49gBta4ozDx0nu07iRj-Bw9ToPynZuG1DKgpX_wudv7JKcyMqPSSDZTcRTm1KlzxM25PceDWMz52v-xEbCne26RcyNnonDdXIGYtXbiy7rNriVH8uZ5yCDRpAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری ۸سال پیش روح‌الله زم:
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68005" target="_blank">📅 19:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68004">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97484f7b84.mp4?token=rkb262V8ymwDGVtFi5ffFlC1ueVgDBjpY4CBt-FFCV1Qq-0f1EQuBsCsaBprX_JxsdsgacWFiPcQiOKDLiALD1IXl3y8WNhB1zKGIuy0DreHnQV5wNnZngjIhK59k8f5BMJ8JTrdN9dQo8HZabaf2seIfWs5FuYu5Pk2WhWMU6eWBei2YRTT-f38j6xtk1fM1ff-8C0xYdUE5E037NExITUdKFnrvT1jogD71vUb8tw4-6VM--d-IXN5IlU3KetG-G4MiIUZWmqw979Ub7NeGypItK622cmi5yUZan8GsHhTUa4GmIlIWMdE1LGKlgMtcY0FToM4kGKggspABgYH8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97484f7b84.mp4?token=rkb262V8ymwDGVtFi5ffFlC1ueVgDBjpY4CBt-FFCV1Qq-0f1EQuBsCsaBprX_JxsdsgacWFiPcQiOKDLiALD1IXl3y8WNhB1zKGIuy0DreHnQV5wNnZngjIhK59k8f5BMJ8JTrdN9dQo8HZabaf2seIfWs5FuYu5Pk2WhWMU6eWBei2YRTT-f38j6xtk1fM1ff-8C0xYdUE5E037NExITUdKFnrvT1jogD71vUb8tw4-6VM--d-IXN5IlU3KetG-G4MiIUZWmqw979Ub7NeGypItK622cmi5yUZan8GsHhTUa4GmIlIWMdE1LGKlgMtcY0FToM4kGKggspABgYH8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💪
سنتکام: برای اولین بار با استفاده از شهپاد (شناور هدایت‌پذیر از راه دور) یک تأسیسات دریایی ایران در بندرعباس را هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68004" target="_blank">📅 18:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68003">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2EWNQ3rcGFvfeI_QHYqloULovu-_jq6nMBpCnQkubpTa3t5Umu9XQ_aAsJsZzSWPfsKzq0-AzrgDYesY2bn858mtGR98SSlxabHzJkYlMhzBfYV6IuUkjWmOFiWz19s3vJsO4OMyUAIGPd8OV6Cdvo5mbSLTiau1QUP--gHLJcflNgFfs9rGT1xs6y4vXjNos8xcqzd9ZBCg1TO1u_ecf5TbUl4f8vK5EjaI6bpQe_3CrkwqFQoCSBOT-ppimvbi-G2O_roby_CG5_-ZAlHlVjc4CMCPjBsOiAbhAKUgUAmLO5f0re4B6mUIgZfy4uzEAzIzvQ9WVFyEMGuHYC1tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ تروث سوشال:
تنگه هرمز باز است و با حضور یا بدون حضور ایران، باز خواهد ماند.
ما «محاصره ایران» را دوباره اعمال می‌کنیم؛ نامی که بدین دلیل انتخاب شده است که این اقدام صرفاً مانع از ورود یا خروج کشتی‌ها یا مشتریان ایران می‌شود.
سایر کشورها از دسترسی عادلانه و آزاد به این تنگه برخوردار خواهند بود. ایالات متحده از این پس به عنوان «حافظ تنگه هرمز» شناخته خواهد شد؛
اما در همین راستا و بر اساس اصل انصاف، بابت تمامی هزینه‌های لازم برای تأمین ایمنی و امنیت این منطقه بسیار پرالتهاب جهان، معادل ۲۰ درصد از ارزش کل محموله‌های ارسالی را به عنوان هزینه دریافت خواهد کرد.
فرایند و سازوکار اجرایی این طرح بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68003" target="_blank">📅 17:58 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
