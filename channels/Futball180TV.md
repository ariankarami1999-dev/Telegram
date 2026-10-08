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
<img src="https://cdn5.telesco.pe/file/CBhBu_JPh70SSe_q3tj9nA8r4BprJ77OFkfgr3vpDbZcSl6K8HEMx6-hogzVkvcZP08XG1wr0qykUTSd8JqpqcaJf3wi3iM78jyFFpx6_bPp022x7Pi5YfsFCXn8XEmC7t3sU9m6S20FT425TGgGOI0uVuHHxKsEoYh-gxwnr6dLS-sACzyfpBnbIwmKE1M7tooYXnpAOvo5rfmjH5ccYKIvuEqgXJZfsNdQPT6S2UfCKXsPiKnwm6mWbR9UyqFdd6aiIqLuiLGtjjxJF0JOXBxGdNsui-iJDRnLFJU0-SEenTfOSPKryXbrP2dCsNWJBX9Vrc4YJEtHBmH_wk14qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 389K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 05:37:29</div>
<hr>

<div class="tg-post" id="msg-108043">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/108043" target="_blank">📅 01:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108042">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/Futball180TV/108042" target="_blank">📅 01:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108041">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/108041" target="_blank">📅 01:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108040">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ceb61fe00.mp4?token=LLGd1hhjPgEVqmKPofqqb4QsZFAm1KZz0FyYA4zu-dd5-KeF_Cdkn1_y7zx0h8TJ-KWaYjQsbevFMQfWJuEX2PoQGQuAS927DPk9NyT3vrM-fy3S6MHwJlxI-0ouVUjWUg-xpSyeqlyNPCK7eB4JJRvWvyW42IdmmIvV4bHacaUSZX-d76Qifrxmc4Mtp0p41FqqbvpY06hLOOV5UQ0_HUvR4arU_9pP3K2eCbsj_Nwwr9J3u01R8-vLp4z85-Y-a63CKWXvyHeDzqp-Na8k2eCYUo2-JRhx-VidU6O6asSIvhg6rQHpitlqRwed0eZI71UvauhPcxpMWMzPnTLd9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ceb61fe00.mp4?token=LLGd1hhjPgEVqmKPofqqb4QsZFAm1KZz0FyYA4zu-dd5-KeF_Cdkn1_y7zx0h8TJ-KWaYjQsbevFMQfWJuEX2PoQGQuAS927DPk9NyT3vrM-fy3S6MHwJlxI-0ouVUjWUg-xpSyeqlyNPCK7eB4JJRvWvyW42IdmmIvV4bHacaUSZX-d76Qifrxmc4Mtp0p41FqqbvpY06hLOOV5UQ0_HUvR4arU_9pP3K2eCbsj_Nwwr9J3u01R8-vLp4z85-Y-a63CKWXvyHeDzqp-Na8k2eCYUo2-JRhx-VidU6O6asSIvhg6rQHpitlqRwed0eZI71UvauhPcxpMWMzPnTLd9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اشک‌های تلخ امی‌مارتینز حین تماشای مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/108040" target="_blank">📅 00:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108039">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">احساسی‌شدن دیشب آنتونلا‌ و فرزندان لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/108039" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108038">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11ce2c532.mp4?token=SY7ZxPnzFr-M3O9BVE_MiPQa4R2mC61FEKbfJxq0LcegyxwvcWTEQXrNUlr917S-Hf_hQx0mf31iVCXK4UMqPi964jxWP_Je44orgWwomM3ZcDXgEgGpiVnaabRQrVSYCanA0-COC285uYL8aCE6eK07Y8MKZB2yycy1nhmQqL37j5JNCLzSv-vUMn4gL1ElV33vpqjF8Zm7Do-_Nwo0ws6wcc7xeuJmuPQaya2L6PGSAzHUSd4sVagwn3J88bbmY4wxnzvxEca8lS4t2KDkbpvWZ4raJvS8Y6QUvSlzjxK6iic6IRWbtjaTSDaIfA0BxNJk3V3WzZXKZm8Q4K_ucQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11ce2c532.mp4?token=SY7ZxPnzFr-M3O9BVE_MiPQa4R2mC61FEKbfJxq0LcegyxwvcWTEQXrNUlr917S-Hf_hQx0mf31iVCXK4UMqPi964jxWP_Je44orgWwomM3ZcDXgEgGpiVnaabRQrVSYCanA0-COC285uYL8aCE6eK07Y8MKZB2yycy1nhmQqL37j5JNCLzSv-vUMn4gL1ElV33vpqjF8Zm7Do-_Nwo0ws6wcc7xeuJmuPQaya2L6PGSAzHUSd4sVagwn3J88bbmY4wxnzvxEca8lS4t2KDkbpvWZ4raJvS8Y6QUvSlzjxK6iic6IRWbtjaTSDaIfA0BxNJk3V3WzZXKZm8Q4K_ucQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
میانگین نمرات لیونل‌مسی در ۲۱ سال حضور ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/108038" target="_blank">📅 22:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108037">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f285b4a4ed.mp4?token=jmRZNKXr7chjGPJO23Hsl0xiTbuB1U7qmOpqxox58dVwBdDwuVmAeJerKB0DZL0uBsRdR2ireFY--CdGQ04QdNVTVhyFV5vmewQumOpNPvbxeX849BzBgm7zm9eNWQ1sF1eAbcG2penO3JMJCpmutOJL1B21gqa3bK6_g427rrqA-uIJ5I5_3xG4x2-NvNS4yXPpTYkADJAObUyngE0aGUpJR1Fj29ZRnC5WvsFOVnf3qyOFOgjLJ5Gmlhn8PZJRWhBiknOVPjYpCEI7mrxONr6bBiFSn5dTgkHwesOGLcua5TS7IlRLM_XtjEa1yT_BTOTHQJF75wwPjCjiwGXnMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f285b4a4ed.mp4?token=jmRZNKXr7chjGPJO23Hsl0xiTbuB1U7qmOpqxox58dVwBdDwuVmAeJerKB0DZL0uBsRdR2ireFY--CdGQ04QdNVTVhyFV5vmewQumOpNPvbxeX849BzBgm7zm9eNWQ1sF1eAbcG2penO3JMJCpmutOJL1B21gqa3bK6_g427rrqA-uIJ5I5_3xG4x2-NvNS4yXPpTYkADJAObUyngE0aGUpJR1Fj29ZRnC5WvsFOVnf3qyOFOgjLJ5Gmlhn8PZJRWhBiknOVPjYpCEI7mrxONr6bBiFSn5dTgkHwesOGLcua5TS7IlRLM_XtjEa1yT_BTOTHQJF75wwPjCjiwGXnMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇦🇷
فریاد بازیکنان آرژانتین در اتوبوس برای اسطوره مسی فریاد می‌زنند:
🔺
‏لیونل مسی، ما می‌خواهیم برایت بخوانیم،
‏تو جاودانه هستی، درست مثل شب قطر.
🔺
‏رفتن را متوقف کن، یک بار دیگر به این موضوع فکر کن، ‏این چیزی است که همه در استادیوم مونومنتال از تو می‌خواهند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/108037" target="_blank">📅 22:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108036">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa857c27d9.mp4?token=Spr1BO4ELk8kMBb8m3C7Xv2VBvQehhdFxyZtOof8WM78fLYZHfCwSBKKUFY_yfRJhvNz_9tSWWvWqgWC-RKmV3Ltln0Gb6wSPX2d8XxyqSuSG4OSCeirHcQjj7MMAg14GvXVZI3uu9zfjtWIERTfog90aLcw47ApVacCFyXzL1zwOW6VBpxlQLZcTVw0yaU9dOYDQ7ag5TDFLW4ppmN7YZDjEZoU9K4kIfkhF0rxws2tzL-QEwt5IfWmnbKWT7QH3mOzTmlaxi-WmTa0GQleqOhRbfDpWmgHktSjY7OkEj6XkYvymq69MvDViee6d3daSrMz6oI2PbrJ4CuIkeF-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa857c27d9.mp4?token=Spr1BO4ELk8kMBb8m3C7Xv2VBvQehhdFxyZtOof8WM78fLYZHfCwSBKKUFY_yfRJhvNz_9tSWWvWqgWC-RKmV3Ltln0Gb6wSPX2d8XxyqSuSG4OSCeirHcQjj7MMAg14GvXVZI3uu9zfjtWIERTfog90aLcw47ApVacCFyXzL1zwOW6VBpxlQLZcTVw0yaU9dOYDQ7ag5TDFLW4ppmN7YZDjEZoU9K4kIfkhF0rxws2tzL-QEwt5IfWmnbKWT7QH3mOzTmlaxi-WmTa0GQleqOhRbfDpWmgHktSjY7OkEj6XkYvymq69MvDViee6d3daSrMz6oI2PbrJ4CuIkeF-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خوبان‌عالم وقتی راجب تیم‌ملی حرف میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108036" target="_blank">📅 22:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108035">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOWD6_ghEz8OVLo5nwc0uZhZrz-UFGSBmAcUv7tV_NW4DUtg7Z7CuwJitrVGk0L5V3Gc_3XLq4HCfRVTtUX-fUoV6cdeJ_Ddd-rs8jLcC9GbyljCJi59tD7UZD6R5ah0Kn-AWsKx6qVQtC3MT3v-Pb_H41nJghtp8banQ0Q4b9LcWcqVNxSbfP9hVVFg0jE51gNNaNtE4Uoez69eaFih_V29KunehZE7vg8Hl_fqWWNHWRHvwmO7y-4ATLDXa2bk4BNJItDgYw1byQfQVnvuRcD_zAHRdw39kjDoshud6BK80BpRy3a5fvURyR4h4UR_Ij7qSmDXt0WzzmdlPG01oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇪🇸
کامنت رونالدو برای مسی:
لئو، سال‌ها برای کشورت جنگیدی و یه تاریخ موندگار ساختی. بابت همه چیزایی که با آرژانتین به دست آوردی، دمت گرم و کلی احترام برات قائلم. بغلت می‌کنم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108035" target="_blank">📅 21:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108034">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb4f97376.mp4?token=TWY_LcZcQyjlWWeiW31AhIFVrR_GJ_AMiIcnk_jGN1zAnER6auFk-C95B0KQgiHxI8ykhDZzH3iqNbXgEz5eXUc0bURaOpDZrinrqGDHLyye2GWgR9GnDZPZTCR92DDVfNjKGvqchEoSPxWZVhxwDGpFHxr0ops7yMbBnSMgX_d5OuX3lBT8E7XCpmBXhsWJIPvoVmTUIg6IHtAMNyCIc_PYCjhSR9Fm9R7imA-7NwAOmOrChZ73zzLe0hAINAbxQbItudQjgMgdbOhUlph34S6eVCzPTUqud8hJrlStYhl2PUJdgLh2-sMIZ_5UanbUyMl5gPgmpUJx-pQ3VCSYkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb4f97376.mp4?token=TWY_LcZcQyjlWWeiW31AhIFVrR_GJ_AMiIcnk_jGN1zAnER6auFk-C95B0KQgiHxI8ykhDZzH3iqNbXgEz5eXUc0bURaOpDZrinrqGDHLyye2GWgR9GnDZPZTCR92DDVfNjKGvqchEoSPxWZVhxwDGpFHxr0ops7yMbBnSMgX_d5OuX3lBT8E7XCpmBXhsWJIPvoVmTUIg6IHtAMNyCIc_PYCjhSR9Fm9R7imA-7NwAOmOrChZ73zzLe0hAINAbxQbItudQjgMgdbOhUlph34S6eVCzPTUqud8hJrlStYhl2PUJdgLh2-sMIZ_5UanbUyMl5gPgmpUJx-pQ3VCSYkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره ابدی تاریخ فوتبال
❤️
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108034" target="_blank">📅 21:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108033">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c820a58fa5.mp4?token=rgmegkVPQ2ej-9p04ggkAC84uXu19TlcWxArJ-1ih0EbnpiywUhats52Z5z4zQjKOKtuIEfboXjqmwv_S0BHVUgnnOnxcpR4oizpxts3Xltz1htxPuvIqH66ojIQxSWOZ1ztUmGqxa1HFGaOS0aWPimnKiooMuXJG7M-Kl2HHt7CYahQb7n0qIoMfITzi1JShX6Uz3PNmWvUIbJK65Pc2UEetZsFuOeOT_1eITBaYWhrV2byxQpg4CTSabSaB9cy2aej3pZM_ugMwWRbg7_Cr__lzH4lHQ5saqbXER2XrWEkf1htN9-1SzdpSjBB4pjwnzEW54bv5He2rGjfF8fGzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c820a58fa5.mp4?token=rgmegkVPQ2ej-9p04ggkAC84uXu19TlcWxArJ-1ih0EbnpiywUhats52Z5z4zQjKOKtuIEfboXjqmwv_S0BHVUgnnOnxcpR4oizpxts3Xltz1htxPuvIqH66ojIQxSWOZ1ztUmGqxa1HFGaOS0aWPimnKiooMuXJG7M-Kl2HHt7CYahQb7n0qIoMfITzi1JShX6Uz3PNmWvUIbJK65Pc2UEetZsFuOeOT_1eITBaYWhrV2byxQpg4CTSabSaB9cy2aej3pZM_ugMwWRbg7_Cr__lzH4lHQ5saqbXER2XrWEkf1htN9-1SzdpSjBB4pjwnzEW54bv5He2rGjfF8fGzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیجان آرژانتینی‌ها بعد از آخرین جمله لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108033" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108032">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0de5ad43b.mp4?token=VuNHsF2-lmVcMj2aYANtXVJAH4WeP2ziEBgt2DPk8-RTHxD--WpuS-LVJ0w5UWd8AVvRDLyCjaHiEDKWjB9ZAKCcIy8Jt88bhOgzkm1-_VDwUVZD16RNJL0U_EOuP1wcwkl6Eqn9XdPigOv3JlwODZYtc4R5bwCBmBw_dC8mHeWwSJepqcwOxcjgy7vXw0JSwNJcw9-FcSeWbcZ1Szuv6Iqeto9ic53mI13ExmT_Plo572k059qkYs4cK35Reux9xlbQ5EPYjuEtpYRI7niIB-dG7hC3vGlX8kTgZ5B3M22QM2jPKMv7L4UN4C1EJw_Cofr8OlToLVc4aDb9sWn1pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0de5ad43b.mp4?token=VuNHsF2-lmVcMj2aYANtXVJAH4WeP2ziEBgt2DPk8-RTHxD--WpuS-LVJ0w5UWd8AVvRDLyCjaHiEDKWjB9ZAKCcIy8Jt88bhOgzkm1-_VDwUVZD16RNJL0U_EOuP1wcwkl6Eqn9XdPigOv3JlwODZYtc4R5bwCBmBw_dC8mHeWwSJepqcwOxcjgy7vXw0JSwNJcw9-FcSeWbcZ1Szuv6Iqeto9ic53mI13ExmT_Plo572k059qkYs4cK35Reux9xlbQ5EPYjuEtpYRI7niIB-dG7hC3vGlX8kTgZ5B3M22QM2jPKMv7L4UN4C1EJw_Cofr8OlToLVc4aDb9sWn1pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🥹
لیونل اسکالونی: "اون «جذبه» یا هاله‌ای که داره. من تو تمام عمرم چنین چیزی رو تو هیچ‌کس ندیدم. اون شور و حسی که مسی ایجاد می‌کنه رو تو هیچ‌کس دیگه‌ای ندیدم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108032" target="_blank">📅 20:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108031">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603077e1bb.mp4?token=DNqgndSH6XyMET3KpCs8htkhqpt0mjN-v_Af3ssgzGYqGhwuoLQTxhydDQNjDzEF4vadOCtSPbhxX8-cl-aCKCX-1YIE7bougNMqzihc9Yitd2Dn3qYOtTvAodhO_Bwc0m1pKjqFzN8vdLLffAtsD0_ugrn4y4tKCPeP_ITAhAOWAUyHzmw1xTQmR3S34iTof8Q_yyg-4zizbKEp6La-rvbBmBifZ-sDTdmMuS8rem_momMfqhvIQmWESrsitVamKQ_nVvokdAivcYDelGWbB_g2EHuikRmxLxs2Iu0APxT30HartBurm5KghDjPc4KP0wIeOwGsN67_nSFW-HYhFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603077e1bb.mp4?token=DNqgndSH6XyMET3KpCs8htkhqpt0mjN-v_Af3ssgzGYqGhwuoLQTxhydDQNjDzEF4vadOCtSPbhxX8-cl-aCKCX-1YIE7bougNMqzihc9Yitd2Dn3qYOtTvAodhO_Bwc0m1pKjqFzN8vdLLffAtsD0_ugrn4y4tKCPeP_ITAhAOWAUyHzmw1xTQmR3S34iTof8Q_yyg-4zizbKEp6La-rvbBmBifZ-sDTdmMuS8rem_momMfqhvIQmWESrsitVamKQ_nVvokdAivcYDelGWbB_g2EHuikRmxLxs2Iu0APxT30HartBurm5KghDjPc4KP0wIeOwGsN67_nSFW-HYhFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌ویژه ابوطالب به قشر دانشجویان عزیز
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108031" target="_blank">📅 20:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108030">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98248b467.mp4?token=Up069H89FIaUN40yMqwrMAcPT44jy6Yz3C6goLuaK7uOajMGkRInIPSNvfik8WWo9wI6vBEw-Fen5IUPaN4WRYQAU-06RcZkqVOD8l-VhsJS4NLHusVpBWyW1PqChFPQPk6mfupG8QUcZVD-T_f0QBOzosu-EBSBhVu5GjnCekf6qmHOz5iqv4tE5yxEeAnu_M63ky7p0wCHQKXFcyu8TVGyjJlZMLVS3of2QXysz717Bgz-ntekfRJVtWRNmcTGts0kZLAJk3K9b7_GUC08Qk3aCE6gBCahq74AJEdrFztbKfGytuaUa9ZKl-ckREaunOcfq8gowNUkubaorLNJ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98248b467.mp4?token=Up069H89FIaUN40yMqwrMAcPT44jy6Yz3C6goLuaK7uOajMGkRInIPSNvfik8WWo9wI6vBEw-Fen5IUPaN4WRYQAU-06RcZkqVOD8l-VhsJS4NLHusVpBWyW1PqChFPQPk6mfupG8QUcZVD-T_f0QBOzosu-EBSBhVu5GjnCekf6qmHOz5iqv4tE5yxEeAnu_M63ky7p0wCHQKXFcyu8TVGyjJlZMLVS3of2QXysz717Bgz-ntekfRJVtWRNmcTGts0kZLAJk3K9b7_GUC08Qk3aCE6gBCahq74AJEdrFztbKfGytuaUa9ZKl-ckREaunOcfq8gowNUkubaorLNJ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«یه روزنامه از ۵۴ سال پیش…
تیترهاش حسابی آدمو به فکر می‌بره!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108030" target="_blank">📅 19:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108029">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmE41YSpFjO26sF25YbSmdAcvo2kMauVi9gnlKS3U8-ZgIWlHZGsLmXvaHgfAjNhkvvfigwic-bMtM2lt_pIOe-KGP4ZaZN_Q0XaxdJhOgpXKkcv4h0D8bl9AjvIawtnSTISrW6qkopmaFZLXxOP37bS86hPmXDRqiXPpGzSoWslPHnvmPimU1wLJgIPGAyae43shP37ysYJsmcYXVD5IAiF2iHTcSr3eueT74KM7bmvhulUHGOt26jxC8WXkfWos-RhGz2ZwR_asU0X7aVzqqEawGAeiyDjO05a4plDKoaaWzzQHsoNXGk5fhGrNOrFm-t7TVZRw15XirpkawtpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
تمام 126 گل ملی لیونل مسی به تفکیک هر کشور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108029" target="_blank">📅 19:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108028">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ad568bac.mp4?token=IliJ3Bx6thOUszqpSFZEL0H-gch9fWxKlYJ088e16CUUr7cbVAz_peMMXuHR2YR_MyMH_a9j2Bn491owOuj7M7x5xgTgxYFURG2A7v4nxJZ8oBmhaaZfhPM04DMZCnZ6SCpt8nWWa6IR3R7oEeDjN4rCgzAxuyrDf_ILZhnpgOX73bZZrLa99f1LTpmv9TDGvyvqFab-PAp73NdwfKP-Oma9TVSJFqRfCsGBKmETPjizjzQ5UPHtsypVA4I8jR9LtIJ6sByRyKRif_OpMW2CeoUk88E85nx734NnuFEPnp1Nbt_8K5bOLbB6ABxuCARFse5cmDvDhtQob_FFYaPrZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ad568bac.mp4?token=IliJ3Bx6thOUszqpSFZEL0H-gch9fWxKlYJ088e16CUUr7cbVAz_peMMXuHR2YR_MyMH_a9j2Bn491owOuj7M7x5xgTgxYFURG2A7v4nxJZ8oBmhaaZfhPM04DMZCnZ6SCpt8nWWa6IR3R7oEeDjN4rCgzAxuyrDf_ILZhnpgOX73bZZrLa99f1LTpmv9TDGvyvqFab-PAp73NdwfKP-Oma9TVSJFqRfCsGBKmETPjizjzQ5UPHtsypVA4I8jR9LtIJ6sByRyKRif_OpMW2CeoUk88E85nx734NnuFEPnp1Nbt_8K5bOLbB6ABxuCARFse5cmDvDhtQob_FFYaPrZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اهدای تابلو فرش به صالح‌حردانی توسط تبریزی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108028" target="_blank">📅 18:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108027">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8ce218ac.mp4?token=YzfgMJgLKevEsaXtz7mRK1a80bTPZRKU1nAtUP2OBbU5AgZesRXkCntSbCXqLLhS0-XnvUFVEG6ya9_3foDUI-nz2o_y-lOkRg0zjlhCqTLPa8lr8DYlBlLYkocw4xZpplQyQSiYjpaAJpo2L73WtKZSGwXMrSGgVqdj5muxQWzHMRauVYxC-do0jMZsWqS2JvkA7Q7DmqZN9Z6S-2471FIhvb08-z36nJ3lNgvLZLnpsA1X7fqwV9XR3m56F6P36pQWEEv6ykMX6lrd8XeuHyib22FV4C3fVZ3kM7hAPZuHpLHfWOquLpL40051cdC4dE4kJvX4lM8KW4MMurW4Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8ce218ac.mp4?token=YzfgMJgLKevEsaXtz7mRK1a80bTPZRKU1nAtUP2OBbU5AgZesRXkCntSbCXqLLhS0-XnvUFVEG6ya9_3foDUI-nz2o_y-lOkRg0zjlhCqTLPa8lr8DYlBlLYkocw4xZpplQyQSiYjpaAJpo2L73WtKZSGwXMrSGgVqdj5muxQWzHMRauVYxC-do0jMZsWqS2JvkA7Q7DmqZN9Z6S-2471FIhvb08-z36nJ3lNgvLZLnpsA1X7fqwV9XR3m56F6P36pQWEEv6ykMX6lrd8XeuHyib22FV4C3fVZ3kM7hAPZuHpLHfWOquLpL40051cdC4dE4kJvX4lM8KW4MMurW4Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
🇮🇷
استقبال گرم وصمیمی مردم تبریز از اعضای باشگاه استقلال در هنگام ورود به این شهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108027" target="_blank">📅 18:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108026">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17e60dcfb.mp4?token=A-n23ljqUVAuHkMDJ65fsADC2ylpVCb5HGiJK9fzxsTzZTqX2SD_JVx-2PJEoHyMwlsCNFSCCbxDoRiY2ZnkVjunWj96pQaQji7WMroGrfo2NFK_q-KXUjiDn55gdD1rptGHmr4VfweeJkbQ6NX-6wBXukAeOSAgfOKgEEWQZ1cfrvubAe864HR26LfSP-Z6mQIGF_bkDhtF4s9tCTbp6uPIomoTs7SJOpjqiLuVfUrVX3FSOQJrx4SpZlRj6v6R4GUXCs_B-J7k8J0XYCUZ7jHRpQj3OCCcuKdbNhL2hR5AsPgJXmCMSnadgDpfRri_HHxaEBtwXevXmZ1YO02b0JmQomKIjHW0gZizxAhA_7w_MKiMQByMTTBKrnpuJwXVM8IP_F8yMNtmVudptnxTGJ5_4AO4r8pRRguAPioHKwXgGwROAzyI4LKuvrHWhjooDpeeA56Bd5G5FjRY2ZVnxn0PFLY_PZx5oSG6w_x8EMXOVcturXw_RfRAeSqK6to2eqcQ_VLzOUvg1hD-C9DYPqDJUuE3j5WzXSwa1hSqGZhuC0GBlD95JQ4TJ952GIYOLo8LxtXfQeOVlw_FWkHieTbtT1RGoJ5zjB3zP6CdtDZDeAM9VxxTRQ_7UKo8yl72vJpBbcG2V6JhoVQIK8WpuAQ2uA0h28TtmTK6X_T3FQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17e60dcfb.mp4?token=A-n23ljqUVAuHkMDJ65fsADC2ylpVCb5HGiJK9fzxsTzZTqX2SD_JVx-2PJEoHyMwlsCNFSCCbxDoRiY2ZnkVjunWj96pQaQji7WMroGrfo2NFK_q-KXUjiDn55gdD1rptGHmr4VfweeJkbQ6NX-6wBXukAeOSAgfOKgEEWQZ1cfrvubAe864HR26LfSP-Z6mQIGF_bkDhtF4s9tCTbp6uPIomoTs7SJOpjqiLuVfUrVX3FSOQJrx4SpZlRj6v6R4GUXCs_B-J7k8J0XYCUZ7jHRpQj3OCCcuKdbNhL2hR5AsPgJXmCMSnadgDpfRri_HHxaEBtwXevXmZ1YO02b0JmQomKIjHW0gZizxAhA_7w_MKiMQByMTTBKrnpuJwXVM8IP_F8yMNtmVudptnxTGJ5_4AO4r8pRRguAPioHKwXgGwROAzyI4LKuvrHWhjooDpeeA56Bd5G5FjRY2ZVnxn0PFLY_PZx5oSG6w_x8EMXOVcturXw_RfRAeSqK6to2eqcQ_VLzOUvg1hD-C9DYPqDJUuE3j5WzXSwa1hSqGZhuC0GBlD95JQ4TJ952GIYOLo8LxtXfQeOVlw_FWkHieTbtT1RGoJ5zjB3zP6CdtDZDeAM9VxxTRQ_7UKo8yl72vJpBbcG2V6JhoVQIK8WpuAQ2uA0h28TtmTK6X_T3FQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
🎙
چرا او آقای خاص است؟⁣ وسلی اسنایدار در مصاحبه اخیر خود با ذکر یک مثال به این سوال جواب داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108026" target="_blank">📅 18:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108025">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/853f3c2c34.mov?token=QE9mjS9IYEBvRnWc4_gCWEZ0hZtfiTzsOCSw0pbdFG5KTfv6U0ER2iWq2QRLkqPggnQJFlyDLXKRXAALMx2n3KqmpV5VKbvDvQHSwhK5FmCWtthzdMWP04Wt1C0PfEo5rf8CBa1cmsk6DJuDPIn03iaWrR0d2jDt2xnalOHHH1HuZGwcaR0Vx864lWJR8Fuwdq1IfwhJenjy2AR63h3-xBHHJ75klsx_zKxZunu-myLQQEjD7O3NsyXd9F7lGL3b3MGTDArQygAzwn_GP-ks4nXZkyeA2JflfExTQLmH6JRl6Q-7TN6P9MkeuYWygYFnqlIHL8TS7bb_pZXjknAC6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/853f3c2c34.mov?token=QE9mjS9IYEBvRnWc4_gCWEZ0hZtfiTzsOCSw0pbdFG5KTfv6U0ER2iWq2QRLkqPggnQJFlyDLXKRXAALMx2n3KqmpV5VKbvDvQHSwhK5FmCWtthzdMWP04Wt1C0PfEo5rf8CBa1cmsk6DJuDPIn03iaWrR0d2jDt2xnalOHHH1HuZGwcaR0Vx864lWJR8Fuwdq1IfwhJenjy2AR63h3-xBHHJ75klsx_zKxZunu-myLQQEjD7O3NsyXd9F7lGL3b3MGTDArQygAzwn_GP-ks4nXZkyeA2JflfExTQLmH6JRl6Q-7TN6P9MkeuYWygYFnqlIHL8TS7bb_pZXjknAC6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🔴
دریاچه ارومیه پس از نخستین باران پاییزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108025" target="_blank">📅 18:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108024">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/babe4c4985.mp4?token=KxRtSRakLy1d70RnXKCjCiZKyEw0fDj3e_J92pNszf4iirV_Qvz18ASum5SICswUWSbXfnOmTff9cGV60_UFIkg8bZ30dhq2hj06nTnnryDp5LUWTdhzkNcw3MpTfA027kl_OLYHhI89QSWLIddpCJuIqRIZQuxNadbtNDlo3LRHRJtMs6pabLS4nj_QqAYwaZA9k2Qtrvm4im-XMgoIdu2y9nKqjFxdab8vZCKJhq4vLZ3fLrjKY4TCDfnARlYRX9C2jS4kjI4B8cCgzYBre5SKN0KZ2MCrkfDyFKtac9YGoAHlw5OIKe06sroDSGrQ5vm_Tp8iYHNi6EgocPfp9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/babe4c4985.mp4?token=KxRtSRakLy1d70RnXKCjCiZKyEw0fDj3e_J92pNszf4iirV_Qvz18ASum5SICswUWSbXfnOmTff9cGV60_UFIkg8bZ30dhq2hj06nTnnryDp5LUWTdhzkNcw3MpTfA027kl_OLYHhI89QSWLIddpCJuIqRIZQuxNadbtNDlo3LRHRJtMs6pabLS4nj_QqAYwaZA9k2Qtrvm4im-XMgoIdu2y9nKqjFxdab8vZCKJhq4vLZ3fLrjKY4TCDfnARlYRX9C2jS4kjI4B8cCgzYBre5SKN0KZ2MCrkfDyFKtac9YGoAHlw5OIKe06sroDSGrQ5vm_Tp8iYHNi6EgocPfp9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
حماسه ای دیگر از آقا جواد؛ آموزش زبان اسپانیایی با لهجه ایتالیایی‌فارسی توسط جواد خیابانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108024" target="_blank">📅 18:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108023">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ewe4a4PkkAtYLJJnNd4j5ywvujW3JRJgnsgD96tiffHndaAYUbdL1rWXT-cZEpwp7XNZVKzqo7F5XDZ0kUZdW_08e9pinafaMblVYSgTPWM4leOaY3YQhluHqL8KYGEqvpaAQCemWUo0twGk_9m7588pOdC-JStpzdp9u9Djatb6wTUSnld1fd5T5Cb1Nd7MxtMN-p80-I0jBg7ZehBIgh40vVxriwjX00-3ka4VtuOQkvbjqix3KnMpCjKdWfyS9UEmZR3U0EkZFn9KNX6-_vGF4jz5gA3IEj3gd7iOEweirYdFkQsA7qpKlFXm7yGOea9hyBcyADSxKRbZvON2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🎙
لوکا مودریچ درباره مسی:
لئو کار فوق‌العاده‌ای با تیم ملی انجام داده؛ او جام جهانی رو که می‌خواست برد و یکی از بهترین بازیکنان جهانه.
تماشای بازی او لذت‌بخش بود هرچند که هم در سطح ملی و هم در رئال مادرید، مقابل او سختی زیادی کشیدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108023" target="_blank">📅 17:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108022">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef62a4022e.mp4?token=Q3hq8vnQLCSHIg9918gtwPAUY1T8Z5As0P4n7MuKXwavskvnxybwV7bG30-JhGKCzBe0TOTT0IzUxG5MhOqK_38AfbUrVwZD8p0Y3z_KHJjSJ9mQE_IQLLpMpruYH3OyVL-3CfC5Gsumx9eYaN69GiCYYNo2FRSu7gBityu2mQ9zywcAfdVKR_nCiFWtUTAMUhyTD1KU8OGmJAoQKHo1i5DP3xUTbSJnGPOlTpdKKiscmxUndWf9RoTUwESiaC8QMk-QsmpYOIIh9AnaOWDTR6t7ZLKEC3ylLwfEsWTGvKQ7xvcdEpif9uo0e8M1diGqkDQmf2YKlWvMfM0126qiGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef62a4022e.mp4?token=Q3hq8vnQLCSHIg9918gtwPAUY1T8Z5As0P4n7MuKXwavskvnxybwV7bG30-JhGKCzBe0TOTT0IzUxG5MhOqK_38AfbUrVwZD8p0Y3z_KHJjSJ9mQE_IQLLpMpruYH3OyVL-3CfC5Gsumx9eYaN69GiCYYNo2FRSu7gBityu2mQ9zywcAfdVKR_nCiFWtUTAMUhyTD1KU8OGmJAoQKHo1i5DP3xUTbSJnGPOlTpdKKiscmxUndWf9RoTUwESiaC8QMk-QsmpYOIIh9AnaOWDTR6t7ZLKEC3ylLwfEsWTGvKQ7xvcdEpif9uo0e8M1diGqkDQmf2YKlWvMfM0126qiGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خواهر تتلو شایعه عفو او را تکذیب کرد
خواهر امیر مقصودلو در ویدیویی اعلام کرد خبر‌ ادعایی مرتبط با عفو تتلو، صحت ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108022" target="_blank">📅 17:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108021">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108021" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108021" target="_blank">📅 17:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108020">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVp2nv51IYLy6HSHqPFmvcn_jZfsAq7yHX4jqUR3B5ioGIyRzIPTgWa-rMYURh9ejDkTTDuLnNvVQXmWx7Woy2ZuWp0c2LFr2cwiZYuN7SLl1m3-YuEmh_N7mh4TNLBOEokeJAfN6Ji8yno38LmM-jIoHAxZuA5k7B9biUV4OocFsQOgvcNSQSEwanUTryxNWjlRY2cY8o0tcI1nKQYoDfc9YNP_kjsUKa_GO2mCjcnUc1who4CVaDl765120nua7hy-L8OPYF486Afbt0WZrRjp-3MFLnvpdhvpcj2tmJlss7GcMZD7OnCKBJtCNfMRBBaLU1XqA6AsSm5IjO_CTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108020" target="_blank">📅 17:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108019">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c636032d.mp4?token=ZN5jAWhUp7GE8JjcxZVUyrwjDWfyfNAjef0moBfAceEULWRspnrTY-yZcBkpGT-xBZ0Ch5gl_Exo4SfwYyO5obNR2mCdaA0BEp5eTixM9w_9LZ5V-9_MdNuCAivB_tH4eiME4Bi9sjCh-zCLVjJ0qaq5oByw0q3pBdHGQEvBa8RYoXZglEBxCa5YF8oOhR10mVW05rCHEVIr4KnPzacXpP0HquQ6GkFiceB0ikhq_Zk2rbkfzwnMZ2nVekWq_PAYcSamIoLaxfyWKLuhK-ZMF7xcQOk5lbypign6zbi9SSSTg31od0_SsU8vA8gWRR40r5Iznr9qN0FDaoCm6DuEmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c636032d.mp4?token=ZN5jAWhUp7GE8JjcxZVUyrwjDWfyfNAjef0moBfAceEULWRspnrTY-yZcBkpGT-xBZ0Ch5gl_Exo4SfwYyO5obNR2mCdaA0BEp5eTixM9w_9LZ5V-9_MdNuCAivB_tH4eiME4Bi9sjCh-zCLVjJ0qaq5oByw0q3pBdHGQEvBa8RYoXZglEBxCa5YF8oOhR10mVW05rCHEVIr4KnPzacXpP0HquQ6GkFiceB0ikhq_Zk2rbkfzwnMZ2nVekWq_PAYcSamIoLaxfyWKLuhK-ZMF7xcQOk5lbypign6zbi9SSSTg31od0_SsU8vA8gWRR40r5Iznr9qN0FDaoCm6DuEmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیگه دیره! خیلی دیر جناب ماله‌کش اعظم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108019" target="_blank">📅 17:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108018">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922b32f940.mp4?token=h-hq27uA48-S6RmC4GqZnoSSGUmsB10wdXK3Paq-mUCnyjcd9ctCo7F2tz_jivU_R4Fo1sEsco_uwRiS4I8iOu7MZkDKCoulyuAx59MXclHMIkTih9pcQGmx79P6pl9jU8G0P8R_4k7rymN9u4HAT-BJuerWkYIdHo2-QA9dsnG0S-INaFs9oXGr5vb88ULRSJDlnFtJXQ66Tk47PuZny7X4TZCs2Vj9RGHmYdgN3zTP4E7ZwFIHCJ-Zis4Ic6H6lh0raaiqaa-gCbSSpXW5-ZYatdMc819WuNI-2qZLn-F0lYhQKDk7g9Vvmd3-CKs7okWFG_xxSJmCNXal_kz2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922b32f940.mp4?token=h-hq27uA48-S6RmC4GqZnoSSGUmsB10wdXK3Paq-mUCnyjcd9ctCo7F2tz_jivU_R4Fo1sEsco_uwRiS4I8iOu7MZkDKCoulyuAx59MXclHMIkTih9pcQGmx79P6pl9jU8G0P8R_4k7rymN9u4HAT-BJuerWkYIdHo2-QA9dsnG0S-INaFs9oXGr5vb88ULRSJDlnFtJXQ66Tk47PuZny7X4TZCs2Vj9RGHmYdgN3zTP4E7ZwFIHCJ-Zis4Ic6H6lh0raaiqaa-gCbSSpXW5-ZYatdMc819WuNI-2qZLn-F0lYhQKDk7g9Vvmd3-CKs7okWFG_xxSJmCNXal_kz2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
کنایه امیر ژوله به لغو بازی با گینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108018" target="_blank">📅 16:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108017">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d567817fc2.mp4?token=TCaUUheFlvr-Iu6RlIatqVw_wOvuOneWEjq2DaR5W8jV3eTUsPK9j11MYAGbId-S1qBoVS8-HxJXP3UMvzBT7Ec4iCt6xLGig2d9byq0AB57hhq1646WEyjKbEcJJJwcjGwQr0Cg8uvzKecE7lHFjogl8aMBVE40MihyHRhmTINfhc8RQRazEAVa-mLlemFjYUq5hQxXzOSZg8EsfwfbwY3GsS362UfS7MOqVRaNGPhDjggtaTFOljBX3njCH6juEe-VSwrhYKFUEQiMdgc38DQ38Blb211JTnc3m_bzVhaJwlg9YEdZGxueFC9HGHwRghkDpzVxgD2atjwmxQ2TmiaI7BsQ4vtl0ePUk52FBE90Aoq-IrOSrqemxhAPjfLERZh2JlghqkPwhcg32_a_ngaZLO5O5hOwVJY-kt2AvmWcH73qWwe7Y6-OMDB6dry1eRRsKHOSire6NoJl0ncO-vYwB6_gBxtOJaAvV0LwTKeqkLuPfMKAXtQdOHUOL5IVzWNQIUb3-JV6Ydrsf_8t9eyMrJD3XgnIqlCngOuyfNDwbx25udJlhn7bqcvdxZhxKeDtc29dkA8bsBH0x6_-cvnxvBt9BdVFyK0r9Uazft_eM3b76ZYML9wVRgL868BTZgw05afQ8o-016mYISxuZ56VALUfVs68bTmPvKs5xxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d567817fc2.mp4?token=TCaUUheFlvr-Iu6RlIatqVw_wOvuOneWEjq2DaR5W8jV3eTUsPK9j11MYAGbId-S1qBoVS8-HxJXP3UMvzBT7Ec4iCt6xLGig2d9byq0AB57hhq1646WEyjKbEcJJJwcjGwQr0Cg8uvzKecE7lHFjogl8aMBVE40MihyHRhmTINfhc8RQRazEAVa-mLlemFjYUq5hQxXzOSZg8EsfwfbwY3GsS362UfS7MOqVRaNGPhDjggtaTFOljBX3njCH6juEe-VSwrhYKFUEQiMdgc38DQ38Blb211JTnc3m_bzVhaJwlg9YEdZGxueFC9HGHwRghkDpzVxgD2atjwmxQ2TmiaI7BsQ4vtl0ePUk52FBE90Aoq-IrOSrqemxhAPjfLERZh2JlghqkPwhcg32_a_ngaZLO5O5hOwVJY-kt2AvmWcH73qWwe7Y6-OMDB6dry1eRRsKHOSire6NoJl0ncO-vYwB6_gBxtOJaAvV0LwTKeqkLuPfMKAXtQdOHUOL5IVzWNQIUb3-JV6Ydrsf_8t9eyMrJD3XgnIqlCngOuyfNDwbx25udJlhn7bqcvdxZhxKeDtc29dkA8bsBH0x6_-cvnxvBt9BdVFyK0r9Uazft_eM3b76ZYML9wVRgL868BTZgw05afQ8o-016mYISxuZ56VALUfVs68bTmPvKs5xxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇹
اینتر تحت هدایت کریستین کیبو با تاکتیک خاص خودش یکی از پرس گریزترین تیم‌های اروپاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108017" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108016">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c192951a7.mp4?token=AtzqAM1RKgD6OpUHvH_y9R3I9CUjeiq2Kqt-jquf0F_yCtjmkbA7epnJ-IXXV4EoH7R1-P7HIDExK5c1cISdelUvG9l-4GzXNtZcUQE75p9P7HWIQqJ0riY084_H5M9JBphELKQrBsC68SXZANAwjhm4WnFTePMqKhoGu8b6gpLisiLR5V71vYbqse927cLZLoGf9dvafA2kLgu7clkMreptj27YQ53b7YfcMst3Ebk9gmbIQhL-c49iq0uDK92jqmNdmuqlV_vB-g2AzHLOU6i8rRFEty6Xlpf7f2szC01z7XBIhmo9ebGXQBw22ohu28rPYBOztcnb8wDEyf_I0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c192951a7.mp4?token=AtzqAM1RKgD6OpUHvH_y9R3I9CUjeiq2Kqt-jquf0F_yCtjmkbA7epnJ-IXXV4EoH7R1-P7HIDExK5c1cISdelUvG9l-4GzXNtZcUQE75p9P7HWIQqJ0riY084_H5M9JBphELKQrBsC68SXZANAwjhm4WnFTePMqKhoGu8b6gpLisiLR5V71vYbqse927cLZLoGf9dvafA2kLgu7clkMreptj27YQ53b7YfcMst3Ebk9gmbIQhL-c49iq0uDK92jqmNdmuqlV_vB-g2AzHLOU6i8rRFEty6Xlpf7f2szC01z7XBIhmo9ebGXQBw22ohu28rPYBOztcnb8wDEyf_I0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سامسونگ از اپل گرونتر شده!
🤦🏻‍♂️
یکی هوش مصنوعی رو از مردم بگیره، رم یجوری گرون شده که شرکت تولید کنندش به خودش هم رحم نمیکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108016" target="_blank">📅 16:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108015">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8260fe1faf.mp4?token=NSW7RA-C-_SJ5OSbTJ_6sqJfD7y4JwbhghHMlA3XjpHwIzfYj57If88hA2yjyeFCWDeY6XoVmqTJ-ovFP_ZxC8GswnJi2CqOUdH2CQNkZUJMmvVzloUaVS_ZL17corrvnGMItvYNUUOoB9jx_7GymeMSsB4kYG3BTCYUv5jeKNkXU_rOFh-AZ3cwt_ndZ2pp7zbVyYZKSwvNnilgGVau-oF0kcw_fW5AYJiEihF7zGZ11dIamStlzz9aTZaOSG-35tE-GgvWX7h9cK3F-FNBzAKlYrDs95oYQIuUX4FtX_XMPIRO8jPXyt_8gAkVJJPBHoWJOSqHCmNrOu92zPDOeFbOQDO-ZDn4ifuCPsmHm-mnN3sc27doSZePQryW7P1aBKP9KPxNwl--JF3vA1Apc3a5Aba6zu6g_pWUu_8CDKuKle_1rt_RtgzfwO1r8wytNXXYbQ0kPWHgfKYz6t8zd-f2PGwvB8__hh5hDHVExtiz_GE69LP4du7fhYozjirveOoHDoT5EE8CujJvhAdZyyfMGIiHTEoF268AN31WJhyAS3jGI4cl-3qUDWjNK4v9zMHF4lEoKhqYqARnyQ7ayOe6-tx9G0aB5mdzTtGKhx8MQwa-MNsAYL1zDmbG5U3axIb7X0ZXORq-UR07w8Y6NQP3aGwVkb3mCbIix37VWOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8260fe1faf.mp4?token=NSW7RA-C-_SJ5OSbTJ_6sqJfD7y4JwbhghHMlA3XjpHwIzfYj57If88hA2yjyeFCWDeY6XoVmqTJ-ovFP_ZxC8GswnJi2CqOUdH2CQNkZUJMmvVzloUaVS_ZL17corrvnGMItvYNUUOoB9jx_7GymeMSsB4kYG3BTCYUv5jeKNkXU_rOFh-AZ3cwt_ndZ2pp7zbVyYZKSwvNnilgGVau-oF0kcw_fW5AYJiEihF7zGZ11dIamStlzz9aTZaOSG-35tE-GgvWX7h9cK3F-FNBzAKlYrDs95oYQIuUX4FtX_XMPIRO8jPXyt_8gAkVJJPBHoWJOSqHCmNrOu92zPDOeFbOQDO-ZDn4ifuCPsmHm-mnN3sc27doSZePQryW7P1aBKP9KPxNwl--JF3vA1Apc3a5Aba6zu6g_pWUu_8CDKuKle_1rt_RtgzfwO1r8wytNXXYbQ0kPWHgfKYz6t8zd-f2PGwvB8__hh5hDHVExtiz_GE69LP4du7fhYozjirveOoHDoT5EE8CujJvhAdZyyfMGIiHTEoF268AN31WJhyAS3jGI4cl-3qUDWjNK4v9zMHF4lEoKhqYqARnyQ7ayOe6-tx9G0aB5mdzTtGKhx8MQwa-MNsAYL1zDmbG5U3axIb7X0ZXORq-UR07w8Y6NQP3aGwVkb3mCbIix37VWOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
نکونام: از پرسپولیس محبی و بیفوما و از استقلال آسانی و کوشکی را بگیرید، چطور می‌توانند گل بزنند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108015" target="_blank">📅 15:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108014">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b905343406.mp4?token=oeYHWlk28JQRV6ImtDmFH0L631C-5Yj1CCH6we49jBSS6NArHQcasG2ydv2u9o0rls0EukOaIwAMlMgm_IarFtCERUlCbrfrjlohfHB-XvIEGWea4bisO30vpvT59ONgc5xrqhPYpfZED7eC_7641fyH5KTLl7Zz7x6HL8jXBLzvj5hkQAFiS-2_bXD96j3YWxZ6GVxh4KCrPtcgwCxOcNZY8RQItiaV3PMhoukJrZJy8KSd99oIoveFsnypxDWQ2zHnCtQTel5-Nk_si1MBsf-H_Rto1T5Rq-Wxd-Te6Nn29zl2zrzzApron8pWnW4Mg2mVxS3A0SVvceuZcP24vFx-3-_M0r0RhbdoNYRmLCXVyOW91HWQEU11g3NAe-73QbQFwtRwDB3h3UcoYDtOGcbgeIHZNlpVllclhHO_nekzJybXGGxfRiraRQu85Mo3j0QUEaWxexdEJCUlpiJ9wayiuNkiI6QwUVzRYtG3AZoz0m83Gq_4PKYyW07TZRqARznh4WWc7EBLpft_xm-PMkOW_bqg4InFNw6WjephRmkGCdEVkh8vZ57r9au5bzPgZhciUj-BxGmhF9VGZT-n17ZJAb44qHdTzleSGtsKwImyDY97TvVsA8PRLmrcPi33IETV1fqtbqFDumjTgLe0-5_JLkcgWxJklGQCJEB7B8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b905343406.mp4?token=oeYHWlk28JQRV6ImtDmFH0L631C-5Yj1CCH6we49jBSS6NArHQcasG2ydv2u9o0rls0EukOaIwAMlMgm_IarFtCERUlCbrfrjlohfHB-XvIEGWea4bisO30vpvT59ONgc5xrqhPYpfZED7eC_7641fyH5KTLl7Zz7x6HL8jXBLzvj5hkQAFiS-2_bXD96j3YWxZ6GVxh4KCrPtcgwCxOcNZY8RQItiaV3PMhoukJrZJy8KSd99oIoveFsnypxDWQ2zHnCtQTel5-Nk_si1MBsf-H_Rto1T5Rq-Wxd-Te6Nn29zl2zrzzApron8pWnW4Mg2mVxS3A0SVvceuZcP24vFx-3-_M0r0RhbdoNYRmLCXVyOW91HWQEU11g3NAe-73QbQFwtRwDB3h3UcoYDtOGcbgeIHZNlpVllclhHO_nekzJybXGGxfRiraRQu85Mo3j0QUEaWxexdEJCUlpiJ9wayiuNkiI6QwUVzRYtG3AZoz0m83Gq_4PKYyW07TZRqARznh4WWc7EBLpft_xm-PMkOW_bqg4InFNw6WjephRmkGCdEVkh8vZ57r9au5bzPgZhciUj-BxGmhF9VGZT-n17ZJAb44qHdTzleSGtsKwImyDY97TvVsA8PRLmrcPi33IETV1fqtbqFDumjTgLe0-5_JLkcgWxJklGQCJEB7B8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
و این شب دارک در ۱۴۰ ثانیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108014" target="_blank">📅 15:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108013">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79183c9751.mp4?token=mudPLqx0c8dbXqmT9SVAEYk-ydN119gQgxVaCBuotDZtlIsjpFaGXQBOPmAiSeGOb4fn0IzpxDkgBHSAPkpCM5E-_ipH7UnfT6AEuqrTMi3evEMMTqHhocdlefJD4dXj4JdcAKnNi3a0KBnSa4WehT94OL_A-D1lKzhFOepbarxNYXUSEQgaAO77VhA8UMr1IkkHFRNi27mIjB91wPM-d92vhyMok74u6VBcr-DoKD4EoxesvWVHuY68i3J-cNpYHbAVq9RGDfy_18RWefw7kjuzN5toyqejBhxfcVWVK2SYHW72As-psMkQxloIsW9HT4vucRiN9ZahcLhtL8Vu32OGDGGY7NYAjXrlu_4-T_KcJxujkk7QvRIM-CnOKa1FOa8iggZrI-fRfMgpyxTTdbS7G1C09fSD5WdgjlJsC0fPoJ7jcgUJrEkxGZNjDBtWN0YoXFuqKwW9yqaMmRUVOHpGmhteOIgUksrU8IFYwoRLikTeVvUh8VxAa5TJZE5IGydRlcz105bMrH2odqMSrzmQrY_HE3pjQqZidR_zLHTuzuBMDUGzlpFAsFluNzhjplwlkPCJG7tJHE2TsJo11yXzIx-BCqTKcYmwDfnsq7TlJYA113oc0aYD1a5WFZiBKmp4qETc89rVSDlAawvKck7zCN10f2OF-mYZQkVQ1R0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79183c9751.mp4?token=mudPLqx0c8dbXqmT9SVAEYk-ydN119gQgxVaCBuotDZtlIsjpFaGXQBOPmAiSeGOb4fn0IzpxDkgBHSAPkpCM5E-_ipH7UnfT6AEuqrTMi3evEMMTqHhocdlefJD4dXj4JdcAKnNi3a0KBnSa4WehT94OL_A-D1lKzhFOepbarxNYXUSEQgaAO77VhA8UMr1IkkHFRNi27mIjB91wPM-d92vhyMok74u6VBcr-DoKD4EoxesvWVHuY68i3J-cNpYHbAVq9RGDfy_18RWefw7kjuzN5toyqejBhxfcVWVK2SYHW72As-psMkQxloIsW9HT4vucRiN9ZahcLhtL8Vu32OGDGGY7NYAjXrlu_4-T_KcJxujkk7QvRIM-CnOKa1FOa8iggZrI-fRfMgpyxTTdbS7G1C09fSD5WdgjlJsC0fPoJ7jcgUJrEkxGZNjDBtWN0YoXFuqKwW9yqaMmRUVOHpGmhteOIgUksrU8IFYwoRLikTeVvUh8VxAa5TJZE5IGydRlcz105bMrH2odqMSrzmQrY_HE3pjQqZidR_zLHTuzuBMDUGzlpFAsFluNzhjplwlkPCJG7tJHE2TsJo11yXzIx-BCqTKcYmwDfnsq7TlJYA113oc0aYD1a5WFZiBKmp4qETc89rVSDlAawvKck7zCN10f2OF-mYZQkVQ1R0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فقط از خودگذشتگی مهدی مهدوی‌کیا رو ببینید ۵۵ تا بازی برای تیم ملی نکردم تا به جوون‌ترها بازی برسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108013" target="_blank">📅 15:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108012">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d16bdac48.mp4?token=S2gR8dMEQ4yCFg3BVvsoR5K6Nrd2iJ5w408ugB2IUuSATqcrMfjLJvEKoPZo0B4Kt6OCcOtDl8_QkEHLwLM1BKJ6mKHGDVQmCcmLR_lqn5W7bkw3WFu0_tY-94QOMAwBG4a1EJtfZU1HPI7DZjb0Bzl0JULkSOgRTHxRVnxucei3eIarLrHeHHWN3BFZciuc-P0_JCmLWaI3iybYRFzfN50mbR9wkZxX-kiy_DTfVV5HMPYRNGlqdq4KckCfscS6_OXrXZFLYjLFgDJ50pAZZPFp6pd1F0NVjoQkCwizasNhps5yOCMMqiUdK8nk4erDufo9rTstPsyBtIWd_GSWbIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d16bdac48.mp4?token=S2gR8dMEQ4yCFg3BVvsoR5K6Nrd2iJ5w408ugB2IUuSATqcrMfjLJvEKoPZo0B4Kt6OCcOtDl8_QkEHLwLM1BKJ6mKHGDVQmCcmLR_lqn5W7bkw3WFu0_tY-94QOMAwBG4a1EJtfZU1HPI7DZjb0Bzl0JULkSOgRTHxRVnxucei3eIarLrHeHHWN3BFZciuc-P0_JCmLWaI3iybYRFzfN50mbR9wkZxX-kiy_DTfVV5HMPYRNGlqdq4KckCfscS6_OXrXZFLYjLFgDJ50pAZZPFp6pd1F0NVjoQkCwizasNhps5yOCMMqiUdK8nk4erDufo9rTstPsyBtIWd_GSWbIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Goodbye, Leo…
💔
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108012" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a871b4e8.mp4?token=VHNzhOh49JprZYHXh54LMhKPV-DOKdQow4GeSR8lvONmvVlBAZsTAMz9k5yIcYKgu1O-f8uFkAs30dya-o9oJFDiHBBVdcTZh5SkJfGso4OL7E77V75EOlkp5NV50egKMlQrL32tHnf586MmoyjsjYw3zKcEBuqRVnodea6ix7yVxljWR5GmbP05kj9U5N38YoTWANugxT9E19XZxeusWt85QJp6uIG-VynlVvzwBAmSim4N5pHFTWSpNB-p076qsTa4bh7Oo6p2b_KkVIFUumGsy9ZXWypRLK2X_2t6WiYBVHxR2mFAk65lB_UpmvxSU2sH5SJcF2L0obESq6X-tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a871b4e8.mp4?token=VHNzhOh49JprZYHXh54LMhKPV-DOKdQow4GeSR8lvONmvVlBAZsTAMz9k5yIcYKgu1O-f8uFkAs30dya-o9oJFDiHBBVdcTZh5SkJfGso4OL7E77V75EOlkp5NV50egKMlQrL32tHnf586MmoyjsjYw3zKcEBuqRVnodea6ix7yVxljWR5GmbP05kj9U5N38YoTWANugxT9E19XZxeusWt85QJp6uIG-VynlVvzwBAmSim4N5pHFTWSpNB-p076qsTa4bh7Oo6p2b_KkVIFUumGsy9ZXWypRLK2X_2t6WiYBVHxR2mFAk65lB_UpmvxSU2sH5SJcF2L0obESq6X-tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
💔
یادگاری‌دیشب داور بازی به لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108011" target="_blank">📅 14:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108010">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBxcgHyVniVC1elGAdllEkfIduPpkOkO81g1aWlekQPUhNfcd3L31ABSB8d93Aa1s0ny2yyZ_IGKZC3HcKv9cSgX4NGCZf3mNUuhdfshywV7-o4fq900tjlWvTdbF6cs277EAp8BbXnppkU3CMpo0QOc9RaSM6FTKkN8sCueUeeiBbCHhwXc_YdGOO0tKHrXXhKZuyEYGpCp7iZYxEj2-PU29oWM7eOd7842wfEWhBXP4wbA0Czwg6Teifiq-TLhJAobrP5elJJdmiiy1bTQARfA7zFs5cj1YXO73z1XD3GnwC14CdNDz6vp8-PnHMrrV_KEJz3h2M-KqhuqHuv1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
هفت‌بازی اخیر پرتغال بدون حضور‌ رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108010" target="_blank">📅 13:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108009">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMolvcvT6z8kaxIVdr0gWsJsNfTi9UE0EMJf2nH-h2hdc4ZVqpUqlG1d7ohqsS42p7OAjTRxIpJMv8t_UQgKU20BNAz2AMPeriypoLFo2AqtqwqbWZpVfQrrdrU8Uwztv5k0TtrumD2AS3g1_Aa3IPrjqbQWrAmb-YLDhvDcdyg_gGGwL1Yray7TfzPCDM3xzPRp3mIGl1PD6xccs9qVXwRSSquP1_S6bxR1pHc7FXq5kKYiBdkYWVrmIAZeoTXzoSWBQsJPwj-29u88rt-K1kBk3EHdJtLwwXd1zuG8ijQYBzkdu_0tLDyHy1Cw5OdtcEY6uxVLnQkwxhLwsgw-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
خلاصه‌ای از بیانیه کریس رونالدو:
🔻
رونالدو تأکید کرد که مربی قبلاً با او توافق کرده بود که در یک برنامه مشخصی برای بازی‌ها شرکت کند، و بازی با نروژ در این برنامه نبود. سپس، به طور ناگهانی از او خواسته شد که برای بازی 30 دقیقه آماده شود، و در نهایت، با وجود…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108009" target="_blank">📅 13:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108008">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsN4TRNmSd8lB1_Tj6TyMMzuIoh1d2g3InJD_usKrywqlhkm8BbQ_REAVM1KGdGcCsCghL0lbjOPKJ4aRRfi93FF8NRMhxkYdHKHWcXHaKwUxFeN01YUhZI_XUkvddG1VDBEVbccWCXdUjKxZ8n4n-XbJRP1mfh9MbOJfuH9xWdRKs3KUVBmfEPegI_-e_qLHxRt9VV47fsVrGHxnQ556IIzOYhr9l9UHuBaGAI43GnV86LYtuPTNnW-mbNPVTP6OFcL_LcBKi7JlwJWBOAySAC9tCVwGucENAtCbeJoegnu5v_WGv8B5YDP_MQUllKMMK1qCQ1k0RAPvLJVqdw94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
🇮🇷
فرشید سمیعی مدیرعامل سابق استقلال و کارشناس حقوقی: هیچ خطری یاسر‌آسانی و استقلال را تهدید نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108008" target="_blank">📅 13:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108007">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bba5e1d5b.mp4?token=BQ6d_9dEOCmzQjEjOcPgP2rTMYBDlvKy3vwKvrN0lVZzhEr4zv-7iILtbNBoLxMN_wHNDeibb46a_RgeHjqemIZu95wyAN74S8SIXTUA4h0tbx_Ybyy0HH15ZEO1ghIc4z4iZ1ljhvGcWrLdnZvMYAApCjryqXlxc63vh7u6OgyOgIrCSO-sEEEWmncM3RpqyNiAx65h_TIu-KiOrPpQhC6PXytaxCjDyds-tguAeKiIMSD67R7gXsndplNorxUDE1mbcqyYnxu1PsXsa_7DLuvYP5RP6aYNbLe45GS8yyfmqIV81ZNyUSds7R8-5tmrBL45rKTkXF1ePhMpP9S2Zj5qevV7h2f6Pr03X_b7e-gNK5EIOxY38vUYkRte9kNW7H05eHf0uVuB3W50A6fQw7ZEaeooLYJC-lZB9rg6aE-Y0HygddnSPqRpaJC8pIxLhq28NlwYoHfrUag18_IIHtb0eGKoz8sjrsU7CUClm7niUeQH9FrhhOiWZrlYEL93LIfd_RoXo-i4Nr19iTqMtguYUN7ew4ZOIYekHPH6Ma3ifC6CBu5jgWgRH5Q-DuR4nxJ62EHtNJjWWeglRWIrfzwg5oSazFYWH3Y--pnjrF1Fr0-_9DOEXX54hB1ye-TV1C6GVlW0_w0eSsRTDQBG43AQOW12s0FGwURV5-GZ0IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bba5e1d5b.mp4?token=BQ6d_9dEOCmzQjEjOcPgP2rTMYBDlvKy3vwKvrN0lVZzhEr4zv-7iILtbNBoLxMN_wHNDeibb46a_RgeHjqemIZu95wyAN74S8SIXTUA4h0tbx_Ybyy0HH15ZEO1ghIc4z4iZ1ljhvGcWrLdnZvMYAApCjryqXlxc63vh7u6OgyOgIrCSO-sEEEWmncM3RpqyNiAx65h_TIu-KiOrPpQhC6PXytaxCjDyds-tguAeKiIMSD67R7gXsndplNorxUDE1mbcqyYnxu1PsXsa_7DLuvYP5RP6aYNbLe45GS8yyfmqIV81ZNyUSds7R8-5tmrBL45rKTkXF1ePhMpP9S2Zj5qevV7h2f6Pr03X_b7e-gNK5EIOxY38vUYkRte9kNW7H05eHf0uVuB3W50A6fQw7ZEaeooLYJC-lZB9rg6aE-Y0HygddnSPqRpaJC8pIxLhq28NlwYoHfrUag18_IIHtb0eGKoz8sjrsU7CUClm7niUeQH9FrhhOiWZrlYEL93LIfd_RoXo-i4Nr19iTqMtguYUN7ew4ZOIYekHPH6Ma3ifC6CBu5jgWgRH5Q-DuR4nxJ62EHtNJjWWeglRWIrfzwg5oSazFYWH3Y--pnjrF1Fr0-_9DOEXX54hB1ye-TV1C6GVlW0_w0eSsRTDQBG43AQOW12s0FGwURV5-GZ0IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
💥
عملکرد تماشایی دیشب لیونل‌مسی جلو‌ بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108007" target="_blank">📅 13:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108006">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbfbf7f72.mp4?token=ko1u10dNglNa2MMoO2Qlc9zUwIf_rqx8vXTqOPqzkSDC6ZY-AULi1GkS-CjgWPL4Oco21k5dlUwLDLPBkpT8fXNYwdUrJmBP235am1rZQlEo08UqsnEGa6kDhdQ8P3cpg9PWdVSRqA6Tvz1lkLf8oLzpzXHctmKN-hxR0SUD7mQOl7guCYW-WRtgzbnFhh8GbOj1JdE58VkdL5BzgQtYsVX3vQS3gm_fA0GftdQcnoZ0Tw8Qnmvz346J6tFdjFUpn4Dso-Ko6f8nr3bVN48nK6E6gawI9zKuRShAjL1ZSMdr4kFeeUC84bF_tz5DJDtBR2X9ZUE6p2Qh9TMoq9bQsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbfbf7f72.mp4?token=ko1u10dNglNa2MMoO2Qlc9zUwIf_rqx8vXTqOPqzkSDC6ZY-AULi1GkS-CjgWPL4Oco21k5dlUwLDLPBkpT8fXNYwdUrJmBP235am1rZQlEo08UqsnEGa6kDhdQ8P3cpg9PWdVSRqA6Tvz1lkLf8oLzpzXHctmKN-hxR0SUD7mQOl7guCYW-WRtgzbnFhh8GbOj1JdE58VkdL5BzgQtYsVX3vQS3gm_fA0GftdQcnoZ0Tw8Qnmvz346J6tFdjFUpn4Dso-Ko6f8nr3bVN48nK6E6gawI9zKuRShAjL1ZSMdr4kFeeUC84bF_tz5DJDtBR2X9ZUE6p2Qh9TMoq9bQsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
کنایه ابوطالب‌حسینی به مصاحبه اخیر مربی تیم‌ملی: امیر خان ما رو بهمون پس بدین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108006" target="_blank">📅 12:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108005">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaDvYeVyKt_ZiWA7H_Mvx9xhLvUX81e65GMoGoQsVJ-TTp8OX4o4LpoZmYlnJ1myEruniWA9-YPoYINq7ZCpgZhJc0pnfDSnKnuyR4mRzIzT1KJZXvN-BnXCb9d4AUvfV2f4LEqptbC6JFQb9d1CQteWT_udwkCLhaXLKstxtEDjkT0Dhv5ij7U2PdF966kironcXSniXG3ZxkPApaALMNA5bj0sGi2U7GNHtQcVyxDGdJkX5B8v8tpgXgbntqQP4Lpr34GA0a3grSPUeyEUBmasWHM3_WknjYqKypWB3qYJsly8OY0LK2CzpHLN9G2CG39Hb7qjz41ppEJHmbhsGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر باشگاه استقلال برای بازی با تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108005" target="_blank">📅 12:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108004">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e310d4f8.mp4?token=LRgH8kXkgoA4oO4XR8eGRxdQ6i0DerdApwlSramM1j8ooDLnk_B8Q8Rx-T4F02xgh3SymGbjQBx-wS4EVgj--5S42gxogFOVSJyRGCb-0GxXVaiMDP1IUnueFYevQTD9bkSjqCqsC3k_sorT4ZGBwEwWugIPFq64b8ynVniRGcvX4idkCFPlx7GXH53t0CKTsVwqNl1mY_7RlXs12RZ49gXCfWshGjMijz9vIVHvR7CrAFiruTgyCemZm9hxcbUhmMvFbOqPQbulKrgbCagmBXfwS1jGA60ksn1oh2qHjgTPEAI_0jrCfK0rN6Aq9F7fNvMF5Vbj_jn233k2bz7qcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e310d4f8.mp4?token=LRgH8kXkgoA4oO4XR8eGRxdQ6i0DerdApwlSramM1j8ooDLnk_B8Q8Rx-T4F02xgh3SymGbjQBx-wS4EVgj--5S42gxogFOVSJyRGCb-0GxXVaiMDP1IUnueFYevQTD9bkSjqCqsC3k_sorT4ZGBwEwWugIPFq64b8ynVniRGcvX4idkCFPlx7GXH53t0CKTsVwqNl1mY_7RlXs12RZ49gXCfWshGjMijz9vIVHvR7CrAFiruTgyCemZm9hxcbUhmMvFbOqPQbulKrgbCagmBXfwS1jGA60ksn1oh2qHjgTPEAI_0jrCfK0rN6Aq9F7fNvMF5Vbj_jn233k2bz7qcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دبیر: اگر اسم قوه قضاییه را می‌آوردم باید می‌ترسیدید؛ خداراشکر فوتبالی‌ها دوم جهان شدن را برای کشتی شکست می‌بینند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108004" target="_blank">📅 12:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108003">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b7671e0e.mp4?token=q_VePgiJKJEdMZhHG8UdMWw0MFyDMGVVwV0SQ4UTzM2xdcFkYO6MN4qUuAHiei8a5RdT7YGf3WFCZv8pVLFcTfFT4EmkGQPAVHVp7-vxxPQfCSM1L-mGy0WjXv5C1q5UyF6xh-J5H0vlHpwBrpXFXEmYpZOmP4qIkOdOFagH_WmOmGXnr23kJ2ev1YkfBlG54fswNDIzuoxH76riaP68kqxzTbSwNUQezL5qy9I62pr8ulN1oxynQDdHgztzqv5SG7SIuOJe9tjk9fgee6VKF--iKFJp6iCqGgLppVMAWK6Mm58257kj2gF0YxKNOe5SvjyJ3AuuK-GEfW6bkuLn2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b7671e0e.mp4?token=q_VePgiJKJEdMZhHG8UdMWw0MFyDMGVVwV0SQ4UTzM2xdcFkYO6MN4qUuAHiei8a5RdT7YGf3WFCZv8pVLFcTfFT4EmkGQPAVHVp7-vxxPQfCSM1L-mGy0WjXv5C1q5UyF6xh-J5H0vlHpwBrpXFXEmYpZOmP4qIkOdOFagH_WmOmGXnr23kJ2ev1YkfBlG54fswNDIzuoxH76riaP68kqxzTbSwNUQezL5qy9I62pr8ulN1oxynQDdHgztzqv5SG7SIuOJe9tjk9fgee6VKF--iKFJp6iCqGgLppVMAWK6Mm58257kj2gF0YxKNOe5SvjyJ3AuuK-GEfW6bkuLn2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
🎙
👍
لئو مسی: از همه کسایی که کمک کردن آرزوی کودکیم برآورده بشه ممنونم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108003" target="_blank">📅 12:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108002">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbb5ac04.mp4?token=mvj5I6G20s2HuKeG9oqTHtJ0WBeHBUu0Js0ba-7JkaApAbGvlcKYeNPMPsIlUnAtVaif2U7a7W0WtjzJu9XD71xUS9ARnzJOTboej30o2GebWdUdakAw7eUrbM84SZtZZyl3qqNhArXfsjeSRU3U125rIL5FWFr5oQJMQ-K2hNNK_0M5-L4Og5MJD7ZD1tTw8Ph6p-WgnZtODSOcVBfunsbwQbZWvoAlr5ncfiDzecFchn5pzRAzbbTbizBkbiBo--w2MNJI-Mx7gVAxfXKkCTysYmYMgZZNkF0ntUHwQqA83r8YBTs-u7X0Mj4EmVgUgetTHd8vfj0DZK0sCLwkpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbb5ac04.mp4?token=mvj5I6G20s2HuKeG9oqTHtJ0WBeHBUu0Js0ba-7JkaApAbGvlcKYeNPMPsIlUnAtVaif2U7a7W0WtjzJu9XD71xUS9ARnzJOTboej30o2GebWdUdakAw7eUrbM84SZtZZyl3qqNhArXfsjeSRU3U125rIL5FWFr5oQJMQ-K2hNNK_0M5-L4Og5MJD7ZD1tTw8Ph6p-WgnZtODSOcVBfunsbwQbZWvoAlr5ncfiDzecFchn5pzRAzbbTbizBkbiBo--w2MNJI-Mx7gVAxfXKkCTysYmYMgZZNkF0ntUHwQqA83r8YBTs-u7X0Mj4EmVgUgetTHd8vfj0DZK0sCLwkpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚪️
👤
طنز فاخر ابوطالب؛ ۸۰ ثانیه تلخ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108002" target="_blank">📅 11:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108001">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇶🇦
🇮🇷
الغرافه قطر اعلام کرد که استقلال بدلیل تحریم خطوط هوایی ایران حق پرواز مستقیم به قطر را ندارد و باید راهی جایگزین برای حضور در قطر انتخاب کند. آبی‌ها احتمالا باید ابتدا به عراق سفر کرده و سپس با پروازی مستقیم عازم دوحه شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108001" target="_blank">📅 11:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108000">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19eaf1307e.mp4?token=RtDTM5vvC_MzOmO-V7ZaAiaYsodhBnXqrvk_5oVR9YGrSqLviz7HlM92DnPviPcjPjZbXWcLzpB9rlKja7uyrWv3EX1dMF8umVfdWu4eDUthxArsSK4JgcLQVsLfhTwhrYLPksrolIPSaO4NUPAr0nIvlRAIjbYcj3Sr5z3HW1IpOQK9qTNLHRKgqiO-GBomPWQ1Jcd1XGY6zr0f9HXiqNSgMf1xuy_cfY2rpTjea95qgn8256rV6lZtgWcjEElK6lIJKfJypVuNdBfk6Aez6ojY__FpuEjUO-A-B71HT80X4ROtnz-GNFJSHjsxebRvCIE6T6T11o5NxPMFmZSyLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19eaf1307e.mp4?token=RtDTM5vvC_MzOmO-V7ZaAiaYsodhBnXqrvk_5oVR9YGrSqLviz7HlM92DnPviPcjPjZbXWcLzpB9rlKja7uyrWv3EX1dMF8umVfdWu4eDUthxArsSK4JgcLQVsLfhTwhrYLPksrolIPSaO4NUPAr0nIvlRAIjbYcj3Sr5z3HW1IpOQK9qTNLHRKgqiO-GBomPWQ1Jcd1XGY6zr0f9HXiqNSgMf1xuy_cfY2rpTjea95qgn8256rV6lZtgWcjEElK6lIJKfJypVuNdBfk6Aez6ojY__FpuEjUO-A-B71HT80X4ROtnz-GNFJSHjsxebRvCIE6T6T11o5NxPMFmZSyLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🐐
پیام‌ویژه یک مادربزرگ ایرانی به لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108000" target="_blank">📅 11:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107999">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFsU2eywaa5lQ1aYfOxI54SMkRVtObGuGVbcP4XaH4FF-4vTTTgowZ6xt8QLyk0i83rv_vPF_IKq8irRpFp63i2e4_DXjsqAehpSlWUhsFQtd7IzFRtYUOVD0uVZ61mjJEEKqFdB8GAT47vA98iJ04YS4UD9zdp2pUAphUBs6IcmewjufICLU87ijqeqX2OJmT4zzamJi4zsqkBdc-c9GX7Veq7SNK9xSOR1Mk0OTPOFsEbYVrQMsXPRZi5tYybJnptkCrm7ezqspj9UrwoKpM1rw1TeSsyVSpajSxmznA2QICFzmvFZC0gRTP-wa7Zy99HVF5R4CsivDz_gdEwa_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🐐
☄️
لیونل مسی با همراهی استفانو دی کارلو، رئیس باشگاه ریورپلاته، کارت عضویت خود به‌عنوان عضو افتخاری این باشگاه را دریافت کرد. همچنین یک پیراهن ریورپلاته با نام مسی، به اسطوره آرژانتینی اهدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107999" target="_blank">📅 11:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107995">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R36X50Cks2u03SyfhChA5dEYOUkj2E2IlRUcTQ3ESItBlhC1DvsNJ60lKBQuXivNjXDRUZWf-012PenQCdnxgDaAbs3MTez6p8OnpjNchcVr1G6vuGroOWZCzPU60j_txBOYeIcHjIWlWdxIoYb7takT5lmmXh2QQGjZ47BddZTh2vfA73YsnjFWDGLsa2CTrdoBcGbmLRHsVbixqyONaIFwzkBOIOmVBrj4tOLUGMO2rNg09hsF6kBjlUgDhR2YwClK3ODYSAVJRdl5LqaSncJwEm1XqP-lriZDz0oz-XJmZdX4BUjn_G7TF7OegO_BwLL7Ww57FFkZs8cQymw3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kghIR-ZmaQgw6_o44uDwgG0AKyM1pUTY7Nl6uT42BDsfpBVy35gXytu1abbAKKrFy03VCNxp9vptOPkBAhpApohRnTnLAeepwoxvtRlF1_6F4mxjJl4cQ_y5kjrTM6JtBLrF41dpF7IHZBcpEofCTpQIrte-ho3BcydR7Ip_4-VQCqOiYrH-a--lEPZMmRzjZ_kGJqhI0V0juMvWn6uAGm6R2obrslQOubjIP-iLL7TvzysKZ2y0kRp5pytZrB0lCrtyLi0Oys35SADzyTgzGTujYzCBixXXToGOJaPVN9X-gnTd3k-Y-36HGai8tJUdWJ7vfhgXrNtDIKT6JfcS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUFt6GsHZLtjZ8p89WJZszZ50OGKDNKSGXks7IqplazYg_3soVLXBCQN2AyoJhs5hKjxKyPoOSe22ee6Htv-nrW0Xf755jrsMeLwYLD5_uAVEC5LaAx1J85Wbda9P9XxWHE1sxgPmEfyuks8_XXqcOsgVYDFOJgKXvjsXfQO_Xoffl6Jh3v-ryz7sqKb-EfP-7_HN6VkNv5ZlA6FSyRcrptn158q1jkf8_ZziMPxLLIgkKSZuq1naMTA1xjBMnFubiO2A3iDw5IrtN_g9Wh8oUrxPmtK3mwpjsc03blv6NgssaQCrRrg03tFhq4tdmsJrqFvir3vjFIn9sUe4sblqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9trBph3UrAvERBPpOuR2T_GjT8MOr_wi5wKMe_Y5uUV9vIo2Pnv7RnFzLR4iejVxEzvuNOd5mHjlySLqbbOxbPjI9b9qDUGdcn3LFj_kK2sfSdHMgon06SgZyryFY4mNog6BmD05LPvAk8HpFEqjDpyBwnQfaqTYrUO6KFlmdiV7VDLj5Bq4rNBDt6iXd__40AvKiVL1h_1iMjmeR4mPpp-efOb0iY5dFeco_ZA5Tmv_PIMreSmqGEtqUJtx4ERP2iRrg5-CN_LVEXtPzrJqYTNEdopcHRBJk8KN66pHDiX8KHN-KJz7GcEXSuHEi63_6vRGcUFmN4JRy_NQPEwVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚪️
کیت دوم و فوق‌العاده ملوان با الهام از تورهای ماهیگیری و امواج دریا رونمایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107995" target="_blank">📅 11:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107994">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎙
✔️
😭
لحظه گزارش آخرین گل مسی در آخرین مسابقه‌اش برای آرژانتین توسط جواد خیابانی، رسول مجیدی و نیما دلاوری⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107994" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107993">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107993" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107993" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107992">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnFJ1-opgG4u2WZj82GwT8w58a06x9VOYj0tT00gt40a7mEaKYcbIBfPLpLejXvUHFrdFidfUJ9XRtWXpklOHump3d9_LL52NctqByFuI8vZtmC5ay95N7HBbZ8hFE-toDZAWxvIPA42YaFRS9I28uySKbNlNj9Te7K-qXNT6un0L8arwpw1-Rt_L40utWKIV4EEmpqvrnvtTIDx99VB6GoaAXBg9OC-4AOi4LNe1_jX6TazffOzK7k3u5kPTHm6U67ek36kdYsfZDTGlR0T4gj9rqLH79pjba3uaRt0I0JC8ic_BUvBQeC0g_auuHM5swQ2idGHjELF02GEED3jDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107992" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107991">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4e8b514a.mp4?token=F_9zWMCNA00s43G-VpveLVY0w2C2ihNoFMKO6oQ1Cv1iK3WeIOPXAtLhuMMBfE5mHfCxKojK3GM1K0toiFlbBlq6kLD1z-NBhUNPMgrG0qMELkQq3fmuU7ve-Qtcl7Ytx3WS4n6P8JdlBf2b4Nyq1aKNyjvrbuG_rWwCh4J7ZE8YK711OQvMFfyg4ZHrAJrBWBTB9orgA3wBL3MKXERWzvXU6rnzseXdU3zukcKcDeD0P2uCVAspO_20PXzpWojQUuXAAwaEbzYc_j2C29GlkCCTDlkiSjt91lfdJSkgY-ZQL3yIMlqzft6zXJWiS9aggp2Oj6vZIs9gJP2000E6R0TMvTzLC_q9lnL9cTO1b4aBZolzViyRqb2oWxgnEj6k3CPOxoNaAosAEeBlF2eb3Cd8M4BsKmCHnQ3kl4Q4nmyW9rREptpELc9HUUAF-pxj5dXYhewzz0L0WFXByPIrHoET12bFCNUdjq5rmvKYHbergndcYTPPAb6FbJfIyteZEWe3L3DsBdcPkS8LwWR7XA4Ay3WTInLAPXwCHmJwvlc6_OfGuzbToLPTy94vWVmx07UaE5s4d3JeM-HGBDeESYOOTFT5g7zqBKxOWDRVJ3lCk_SkO2A96pavskNYrOGdk8LRRBjfb2-EIXT8OlXI63TRsjClAEeVHEVE0Cfc5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4e8b514a.mp4?token=F_9zWMCNA00s43G-VpveLVY0w2C2ihNoFMKO6oQ1Cv1iK3WeIOPXAtLhuMMBfE5mHfCxKojK3GM1K0toiFlbBlq6kLD1z-NBhUNPMgrG0qMELkQq3fmuU7ve-Qtcl7Ytx3WS4n6P8JdlBf2b4Nyq1aKNyjvrbuG_rWwCh4J7ZE8YK711OQvMFfyg4ZHrAJrBWBTB9orgA3wBL3MKXERWzvXU6rnzseXdU3zukcKcDeD0P2uCVAspO_20PXzpWojQUuXAAwaEbzYc_j2C29GlkCCTDlkiSjt91lfdJSkgY-ZQL3yIMlqzft6zXJWiS9aggp2Oj6vZIs9gJP2000E6R0TMvTzLC_q9lnL9cTO1b4aBZolzViyRqb2oWxgnEj6k3CPOxoNaAosAEeBlF2eb3Cd8M4BsKmCHnQ3kl4Q4nmyW9rREptpELc9HUUAF-pxj5dXYhewzz0L0WFXByPIrHoET12bFCNUdjq5rmvKYHbergndcYTPPAb6FbJfIyteZEWe3L3DsBdcPkS8LwWR7XA4Ay3WTInLAPXwCHmJwvlc6_OfGuzbToLPTy94vWVmx07UaE5s4d3JeM-HGBDeESYOOTFT5g7zqBKxOWDRVJ3lCk_SkO2A96pavskNYrOGdk8LRRBjfb2-EIXT8OlXI63TRsjClAEeVHEVE0Cfc5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
اشک‌های تلخ انزو فرناندز در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107991" target="_blank">📅 11:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107990">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb06960e3d.mp4?token=ULnuGYp9J1lGhp_CnL_1xmnYmQhjJPZvbr9lUBnaeMDp5qXa8KXrp7-mkkon9BRXmJXcr8dbApIKk0AsMUbf_3PVXhoTuXsY95qKsTlRgsUFttBKmwkekB85jmenwL7H_iWLoatU5gRLlxtQ8KD_CEBxbUBP_RJGSFI_vyhIePxPjuin7odicDb4ercW3AWDxRL1sB9_gkJjPhK0eNSMThBeohNhnF2tBPVMyPWDUjcE8Eakc8QtzBLN26iVPxnj5JkdBcVBLHwFzvxNJrcowFkhgXIVLUs4Nv3lAhZ_j4UinUPSZVkzOAHS6D_UnAX5Di6MGuE9sjCjhq9FzgRQAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb06960e3d.mp4?token=ULnuGYp9J1lGhp_CnL_1xmnYmQhjJPZvbr9lUBnaeMDp5qXa8KXrp7-mkkon9BRXmJXcr8dbApIKk0AsMUbf_3PVXhoTuXsY95qKsTlRgsUFttBKmwkekB85jmenwL7H_iWLoatU5gRLlxtQ8KD_CEBxbUBP_RJGSFI_vyhIePxPjuin7odicDb4ercW3AWDxRL1sB9_gkJjPhK0eNSMThBeohNhnF2tBPVMyPWDUjcE8Eakc8QtzBLN26iVPxnj5JkdBcVBLHwFzvxNJrcowFkhgXIVLUs4Nv3lAhZ_j4UinUPSZVkzOAHS6D_UnAX5Di6MGuE9sjCjhq9FzgRQAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
😭
خداحافظی یار و اسطوره بچگی‌هامون
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107990" target="_blank">📅 10:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107989">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvdWFuv5_XRf-HpXnqf3xEfTDIoL4Q3BH_tbLtFinpN8Aa10C7K_DYqU4hLYAk_qcrsdBuNjMFC7vvvWb9mNxAl6vJkLS9-NyOBxAQs8UgXOy63AKIEqFoHddVrHUWaViw3CxjK4cjw3h_HiU_D2jPBrBC5kZ2yx0KvJ3u6RFFZkKC8j5FyxU_u_6IP5XoTHGzWR-h_7dQNk8VFHR7A2jIzZ2Em6TGyCZi-npMVIreSjrV-lScJLc1Rnz9_KVEu_Gc7GT5B1tpZCwIxkCofSzf0whUZyvzk_nHBX7ihXXAGTtOnuAcAmKosDa3Se-uZiJIFpr2K3KnC2LnOK5RzMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
🇪🇸
🇪🇸
مارکا: هرناندز هرناندز داور ال‌کلاسیکوی پیش‌رو خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107989" target="_blank">📅 10:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107988">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951062ce8d.mp4?token=lbOKMBmhg4OraO6ci1_OYVo54wYxF2oVBF5W8hyNnpoUDvRsCjwrX7mjXYF0AoxpmX2UwZx6sBr1Skl559N6VthclKoF50RuSkzgeeu76kJsRMDN_ShQzsR2hRgmTSB4OX3vtRs5JSQ2Jh3P6RHswKOdk1lAmk4rgBh4npqJTUfGhQTykxkA8qq_9-o_VcO6TICyv4Z0m5n8cYZe6lUTyKz2YunrPDeiaX7NTyxPYmXHZ9KORzU8ZrjBvJxVAjUOSYlEOI3PuioR9bselx8a2L93RS9K7Js7J_IB9AQi8wc-fBk8Nl5Hv4Ev_Vi40vMo0hP_Hdn6ou0DYcqCtjAqug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951062ce8d.mp4?token=lbOKMBmhg4OraO6ci1_OYVo54wYxF2oVBF5W8hyNnpoUDvRsCjwrX7mjXYF0AoxpmX2UwZx6sBr1Skl559N6VthclKoF50RuSkzgeeu76kJsRMDN_ShQzsR2hRgmTSB4OX3vtRs5JSQ2Jh3P6RHswKOdk1lAmk4rgBh4npqJTUfGhQTykxkA8qq_9-o_VcO6TICyv4Z0m5n8cYZe6lUTyKz2YunrPDeiaX7NTyxPYmXHZ9KORzU8ZrjBvJxVAjUOSYlEOI3PuioR9bselx8a2L93RS9K7Js7J_IB9AQi8wc-fBk8Nl5Hv4Ev_Vi40vMo0hP_Hdn6ou0DYcqCtjAqug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
😭
بازی تو دقیقه ۱۰ به افتخار مسی متوقف شد و کل ورزشگاه مسی رو تشویق کردن. همه هم گریه کردن و اسکالونی کنار زمین همش داشت اشک‌هاشو پاک میکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107988" target="_blank">📅 10:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107987">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea54b6fd5a.mp4?token=t1rTJQn_-eevXYTfci5TVASv5Qbi47lhOE51JLWq7MWAi74a2JA8MX4ljqxtVMf1lT_O262dmVUpRyxM5OpH5t_nWTsL8HnlNBeHs5My0tStIe0qAynRZKZZyqNmrGY8gL2k1Du8yBunnsWdnZOvoGy4-HQDlKoTrDdKsIe71F1p88l-q68jHDFQJC_nsv-FSP0oTJ5BOu8hQ_Q0fM6U7oc8lbwLMZ3ZDQsEdQPmbhUxqMOA9_N2L67JCvfa5hMhRhSS5InWo4IDFo-4bo9gohVbGg9ZQksu97gm8dRAHQJwbdpmw5xGLTXp_Bg9KGE9vmsw6xcroiHJ_sE1aNYItA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea54b6fd5a.mp4?token=t1rTJQn_-eevXYTfci5TVASv5Qbi47lhOE51JLWq7MWAi74a2JA8MX4ljqxtVMf1lT_O262dmVUpRyxM5OpH5t_nWTsL8HnlNBeHs5My0tStIe0qAynRZKZZyqNmrGY8gL2k1Du8yBunnsWdnZOvoGy4-HQDlKoTrDdKsIe71F1p88l-q68jHDFQJC_nsv-FSP0oTJ5BOu8hQ_Q0fM6U7oc8lbwLMZ3ZDQsEdQPmbhUxqMOA9_N2L67JCvfa5hMhRhSS5InWo4IDFo-4bo9gohVbGg9ZQksu97gm8dRAHQJwbdpmw5xGLTXp_Bg9KGE9vmsw6xcroiHJ_sE1aNYItA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گل‌دیشب اسطوره از نمایی متفاوت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107987" target="_blank">📅 10:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107986">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ce0c64ae.mp4?token=ndXrhLdB40gLJrUOrTp61Su0rtHKlstk0So4UZ7tPZiOMj0n7CGieqcao_wk-tNuMAlryh81SdSis_46nr4uzRTQkdxOjD486j1L66plSblHJnNqvXkJXo6L-9QeCSvjHrQ32pHdH-WjoskBWPAAQvHMhtPLEo__DfwbrRd_3htxGNUzjl4G4eRfSsZaWTC2P4P5eoX2gX7S5LTiQuvJYTdZkVNhxApARlx4vaCLgvVoHl3OG6k__7MYDm6LFpzJ_cyMJ9KOHaeHTlwC03koL42YwaPKFgN5aH-zCHzkjxTu0uFBTDG6P6jIgoHM-ufjToQLwP4tWgdsWGaqr73j7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ce0c64ae.mp4?token=ndXrhLdB40gLJrUOrTp61Su0rtHKlstk0So4UZ7tPZiOMj0n7CGieqcao_wk-tNuMAlryh81SdSis_46nr4uzRTQkdxOjD486j1L66plSblHJnNqvXkJXo6L-9QeCSvjHrQ32pHdH-WjoskBWPAAQvHMhtPLEo__DfwbrRd_3htxGNUzjl4G4eRfSsZaWTC2P4P5eoX2gX7S5LTiQuvJYTdZkVNhxApARlx4vaCLgvVoHl3OG6k__7MYDm6LFpzJ_cyMJ9KOHaeHTlwC03koL42YwaPKFgN5aH-zCHzkjxTu0uFBTDG6P6jIgoHM-ufjToQLwP4tWgdsWGaqr73j7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
فوتبال ما شبیه شوروی است اما در مناقصه باید وعده اسپانیا را بدهی تا برنده شوی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107986" target="_blank">📅 09:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107985">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd225b786.mp4?token=NeN_uIrAKOitxNPURO5hAcXCnnfo5lC1dvMvLXm_ye2ZMr3u8lm3Iq9RjtHqesnilux3ZhNVGDOXlv0URYR2duLUr2jS9S7vJf9RBs5n8ZC9fJnoSqKg9DnLpGWr2KhEHH2KL2AjqxerSpi_1rJrKOGqiNGx1BSvx_6v0ar-Rs7EFqAgv2bIezgcy8zN3D9Y1-nvk9-sgI_SQXKz3JQ8yzZIMs8a-oSyhwtxPZP9yjHnlWPNgmzIuKeb98Uv6VCxet6X9ZNrjSUFYpJGeHS2YaTY7QLUB9wCTaPP3i7sOupnpFw01RJPJW5pmOihwswgyzZNDkvecR34CkGrBXBcLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd225b786.mp4?token=NeN_uIrAKOitxNPURO5hAcXCnnfo5lC1dvMvLXm_ye2ZMr3u8lm3Iq9RjtHqesnilux3ZhNVGDOXlv0URYR2duLUr2jS9S7vJf9RBs5n8ZC9fJnoSqKg9DnLpGWr2KhEHH2KL2AjqxerSpi_1rJrKOGqiNGx1BSvx_6v0ar-Rs7EFqAgv2bIezgcy8zN3D9Y1-nvk9-sgI_SQXKz3JQ8yzZIMs8a-oSyhwtxPZP9yjHnlWPNgmzIuKeb98Uv6VCxet6X9ZNrjSUFYpJGeHS2YaTY7QLUB9wCTaPP3i7sOupnpFw01RJPJW5pmOihwswgyzZNDkvecR34CkGrBXBcLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
خیابانی: سه ماه دیگه صبر کنید تا بفهمید اسم واقعی من جواد هست یا جمشید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107985" target="_blank">📅 09:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107984">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce8d64d12.mp4?token=ZNsZL1yvnrGCmwOKTtxdaFKyw7EN0HnWkoNhBOamgED964zL72aAyqnj07kfg_HNsZGcHQO_eovuqxoJTFNd5JxeBCjrsiJSrb1325dNpd5tsxzbGEsN-sc8z-YBfRZTIfVsq21Yvqy5MufCQrk3fEaZgwEXfnYKorqAsT4i_EoiTGp83FAX4zHcCubxfNKea17Gr2rB48Z17RsDj-BOS1DmTE78p_DNzPdMh1_20E7tMi_47f8ECt24QXZFRO67BE80FXg5p-DaA9KSDi2EiGkKh3k4_XK-OMXg8Q47cO4yDRcOSkvFDqUTVKNbRB80NNTWy0w9wUqddQgZH63_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce8d64d12.mp4?token=ZNsZL1yvnrGCmwOKTtxdaFKyw7EN0HnWkoNhBOamgED964zL72aAyqnj07kfg_HNsZGcHQO_eovuqxoJTFNd5JxeBCjrsiJSrb1325dNpd5tsxzbGEsN-sc8z-YBfRZTIfVsq21Yvqy5MufCQrk3fEaZgwEXfnYKorqAsT4i_EoiTGp83FAX4zHcCubxfNKea17Gr2rB48Z17RsDj-BOS1DmTE78p_DNzPdMh1_20E7tMi_47f8ECt24QXZFRO67BE80FXg5p-DaA9KSDi2EiGkKh3k4_XK-OMXg8Q47cO4yDRcOSkvFDqUTVKNbRB80NNTWy0w9wUqddQgZH63_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پاسخ جالب حمید محمدی مجری تلویزیون و برنامه فوتبال‌120 به دعوت ضیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107984" target="_blank">📅 09:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107983">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نورپردازی و تمجید پهپادی از مسی پس از پایان بازی آرژانتین و بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107983" target="_blank">📅 06:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107981">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHryLQfRSiXrDhJYi47NpiePk-FTuZHXCyhPmcXiqgcZ4IkxTyeZ-e9ebVKvvKdJO_EjlQnf0XjLd7vxI8eHiOd5Z1yKAUthU-OLh6A0v_9A4gJ2Paws4BjU1lJR7FGF8tm7k1FT9STVkCXHXfwtXyrzib3kTS8Wmte8jUwZ6A_5309xGAIG23h2IAMmthw9xY6LEZ8HKjw6JmaOU_aob_KHTlvg-FXhflBuVe7yli1M1WWGySxVdbRj0rMpmXRYu_tAe3bsG7rhEjii-YuMFnKIDAV7RXzmvvsxuod_yjDcDwtoLY03IhNhy7T1S1XBDQUh7vhUqGmBtVa1FL47nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RajKbtycX6XsiY7aCVdmZMIAnNka7CGL0hxDaydF-UWQM61D4dQAs53KQis5suk1mjaQiAZ7hI9o6GAVYVD22UWz05-Ca_CNLphirWYbbM5tSuj_Alz2-tcWoSmLR5FdOjDdy7daqhUePEQoOmSWHK9cbeuevtLK4CyHCFPgjkwdWTaye-mKUqjiqJbFy7nQAgnnxA-YhFFss2LIkh70G9jg42lT-86SDrn76KtcMLMdUFpEBVvfbMAVsFG3ZRQn12ZmzDTf6SjX_PzHIzhS9g8qahdZrWfCPPhjf-CTv2OFOTVL77WEDfdFCrgtWT1XJ99DkB7jioxVv1lW4D0PUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😭
😭
😭
اشک‌های دی‌پائول بادیگارد مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107981" target="_blank">📅 01:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107980">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf74e1898.mp4?token=EBNDB5TxbWzKWgw3TnG2PPMvOT-cda5cobFkaRbNA58NX4SIgUTLjHfnIRYgNICPSTiYmOLMxio8-mlkDgTEsJ6A9XG9mecSDyCBJiM2p41Jr7gmsf2aJSgIVgDM77Uw56TxpXYfPJF8zlY1auamC3OoqKg0rmexFtJ0WRpnVbyoVN23xivtXvy0f4V6Zk6Q2rY7Wik4IrU6EJb2jgzOARBGY7xWZ09Y-2aLdouPa6HAKBZy-eVzelIejYxKyXsIKn9q7kAe70-WXvMa3BoANNjW9-eqTDzi-Q46cgey3Khy5QvduVz8WxbaJtO1SlTj5usCjt91LlFqz0UU36cLug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf74e1898.mp4?token=EBNDB5TxbWzKWgw3TnG2PPMvOT-cda5cobFkaRbNA58NX4SIgUTLjHfnIRYgNICPSTiYmOLMxio8-mlkDgTEsJ6A9XG9mecSDyCBJiM2p41Jr7gmsf2aJSgIVgDM77Uw56TxpXYfPJF8zlY1auamC3OoqKg0rmexFtJ0WRpnVbyoVN23xivtXvy0f4V6Zk6Q2rY7Wik4IrU6EJb2jgzOARBGY7xWZ09Y-2aLdouPa6HAKBZy-eVzelIejYxKyXsIKn9q7kAe70-WXvMa3BoANNjW9-eqTDzi-Q46cgey3Khy5QvduVz8WxbaJtO1SlTj5usCjt91LlFqz0UU36cLug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
آرامش‌خاص و لبخند‌های لئو در حین ورود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107980" target="_blank">📅 01:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107979">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUIXlKgRsrSfG8-P_5xV7PUk2LFniH2QuJmWWjxpFlb29kO6HAtSOLCk5zhjsYgGdRHLPhavyIflecg6FvyTyYgDyV6bb6JvzWRuv6YaBR4d_7nuCvGrpihcNIJzcT6BA-e1rN8gaE1UFQ4QUdCTP5--AdHk0kFxROJPvMCZpuhFfeyngjJZo6Ii5ioXq8YqfdGa80UH21BSQh2pACl4KjJBUirefMn2c_jTtLp3iZHJfiCswYyVmyTYZoKnfIbX9FAw2LNi27Ba19zlytGIMY4h0qkDBelwQWwwCDI1bBeJ2gW9FywKBqgcwJGe4dON-iMwvmqPncSL4UzSdQANoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لبخند زدن هاشو ببینیم
🐸
🐸
🐸
🐸
🐸
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107979" target="_blank">📅 01:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107978">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIYQNxq2FQby8tEbyyQiosPt_hmaEozCCPVcNwlHnXd7YanyyZOzBB4T1VDpXkpPrdMluEeqAmdNf2033FwRQfncH2Tmc9jSOG7r63TGTneRx7Fa6umG-RiyT6Uhdk1eii8XstqOwvh2xJvRk5mJQunVWSMkG_qTiwe03flr9ush3MlhGpujgZffhbYSUrpMj2oSAi9sf_hvrV7UaRdqwkRwmEbSi3mEvAfpEupA_m8DWXUgUFyC5y_s2KLt_6hO8exY-NavYY-OrkNQiIwdpT8aUwhLFmMfjHNkwEzgEU221EHIqQG9al3_YSxhcdDOt2nb4-dYB_c63wBb2hEzrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐸
لحظه رسیدن لیونل‌مسی به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107978" target="_blank">📅 01:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107977">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7TngECvOWzUO-YhCCPD4ishhkBekadHCG9LQsQMhF4c0qf7qw6XrRYfjg5JK7gr4VTYa06OnCLgpvPpaeMW5SZe1Cbvr2yuQxn8c7_WXXpiwi9_fdg-9stmBqLMWTy8TesMtbLyMUbkp3BiwSea2D_M86AxviJw3_cazuo1HtvdL2KkB2anzZL1WKB4EFgehp96GYs9jQjB_gaHlw74qZhzI1dUcHZiLfohvCFKWswP8VxOYBgaS6mgFIFtqlJeFlMxgN_7jc1FfbegZt-ML5l3QzXLzQ3TU998uTZj4ijVHbfRmD1vJkJQM5lXL4aywY6Xu6_PaxjwIywih_45RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
نمایی از استادیوم مونومنتال آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107977" target="_blank">📅 01:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107976">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64dbdaf83b.mp4?token=Eg0TCE-2JUZRfDDUit8j0IhpmWMzNQhs__KSf2BelUD6CipU3NSUszhSGJuxKqi0TcIt2uQX7dC2Am5hFACSsN-P_B1euGvVkWQL1OPehiEHqpwL6xRDY81_yrOB2u6UZCDpWOfOix-cW1H14gW9dch35cJLfX9Xub9PEmAAqs42N65EPXhrKBDy05ONl13gAguVBqihVSyvx1YIOHDDaoswkTJp2r603XU9wQ1VOCHuH1fPsao0xZ4f2lxiB9gkXvfHZrmTtkV1y-hQIoWVNjGaOgWS5o6Rgl_rFZYqaPp4LYZFXNX_TwlyyqY1OvDDLWikEYkO1vXSPPI7pFmesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64dbdaf83b.mp4?token=Eg0TCE-2JUZRfDDUit8j0IhpmWMzNQhs__KSf2BelUD6CipU3NSUszhSGJuxKqi0TcIt2uQX7dC2Am5hFACSsN-P_B1euGvVkWQL1OPehiEHqpwL6xRDY81_yrOB2u6UZCDpWOfOix-cW1H14gW9dch35cJLfX9Xub9PEmAAqs42N65EPXhrKBDy05ONl13gAguVBqihVSyvx1YIOHDDaoswkTJp2r603XU9wQ1VOCHuH1fPsao0xZ4f2lxiB9gkXvfHZrmTtkV1y-hQIoWVNjGaOgWS5o6Rgl_rFZYqaPp4LYZFXNX_TwlyyqY1OvDDLWikEYkO1vXSPPI7pFmesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😭
استوری امی‌مارتینز از سیل‌جمعیت اطراف ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107976" target="_blank">📅 01:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107975">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbdff94ee.mp4?token=VN4e2I1uDpuiCBCnVS7uO8eLMuyPnAA28TDuSyc9bcGEBwQb5KxXTQZK68ALfQq-uGQymb3rhhCQMGQsGgpi-8M-uZwKsTT8nFbLAL1fl4y_hhpf6Lv5Y1zFW5zTrVLEo0-PIM-YBIxUi9SSeq_jrJNrXwfJhmkWIld2TAOGdLy6x-4rRMS1XilUETUHV-VFJBR_qhTXnsKjdx6uGqHKoR9yGwSA2LV4G9GtGO7FpPp8Dwu4ncVbPlOeAymXxDkinqV7sRjiUGzPEWfgUy5bsDHxd2P8u8WXUEu6ZxnZXvUOy7tt60X3yNmOtAj07CXPhkC7ym6Hrhno5qNSkUBG4gWRO78l80D6jZJILzPffkxoKTvJ44P0bHVXTtjrAA4ed6tDca1xiIcw8nbzohzp1_Bf-YZlyc5KE0ugclZLXDmy2BTtyKxlvtJXdqLU_mEgxWzxbkh5t98khV1RPjk1CAe4VI9fRxcsdYY1-_cnpaaGcNsWoAsEG_3iT5067PMh1rRP2_d-7KcwoziyJkPHX-z7yR47gFEkXVKSNO5_QfKwVDrjUJtbkwP6PnCMNkRZQh56cFXfK1d_aO8dF6-lJimBfcgovstQdb9xxLuQ9nSEOV7KLh3JFwLW6_cwlDlFeCg-I4O-8crQ-Ah8PTDIE0RwIVYZnQRfzkXLLBGNP10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbdff94ee.mp4?token=VN4e2I1uDpuiCBCnVS7uO8eLMuyPnAA28TDuSyc9bcGEBwQb5KxXTQZK68ALfQq-uGQymb3rhhCQMGQsGgpi-8M-uZwKsTT8nFbLAL1fl4y_hhpf6Lv5Y1zFW5zTrVLEo0-PIM-YBIxUi9SSeq_jrJNrXwfJhmkWIld2TAOGdLy6x-4rRMS1XilUETUHV-VFJBR_qhTXnsKjdx6uGqHKoR9yGwSA2LV4G9GtGO7FpPp8Dwu4ncVbPlOeAymXxDkinqV7sRjiUGzPEWfgUy5bsDHxd2P8u8WXUEu6ZxnZXvUOy7tt60X3yNmOtAj07CXPhkC7ym6Hrhno5qNSkUBG4gWRO78l80D6jZJILzPffkxoKTvJ44P0bHVXTtjrAA4ed6tDca1xiIcw8nbzohzp1_Bf-YZlyc5KE0ugclZLXDmy2BTtyKxlvtJXdqLU_mEgxWzxbkh5t98khV1RPjk1CAe4VI9fRxcsdYY1-_cnpaaGcNsWoAsEG_3iT5067PMh1rRP2_d-7KcwoziyJkPHX-z7yR47gFEkXVKSNO5_QfKwVDrjUJtbkwP6PnCMNkRZQh56cFXfK1d_aO8dF6-lJimBfcgovstQdb9xxLuQ9nSEOV7KLh3JFwLW6_cwlDlFeCg-I4O-8crQ-Ah8PTDIE0RwIVYZnQRfzkXLLBGNP10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جو فوق‌العاده استادیوم یکساعت مونده به بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107975" target="_blank">📅 01:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqMQy1S-0WFRf0vKgqr9KzqkrFBZF2qywLJrTJVPF3Kk3VqdBq4Dyz_2Vei2ZzQGOJVHqimmovfzmvc8gM5HSpvWSNZJlfURipQADlmOBHL7omWhMhFQkjqlmrsWr4HRkOj5JdZwHdyujpPoGbHO74bLU5AUgJ2kqWSypVfinuMwnWO9Zu6FRAE-9MsJxcMa2MtvpK4ztRUH0swYYYp11QeTzpY0TMBCMN3AcdWqO5oqn2GT2zKkyYqDHqO-SHbuIE7T4SSp_rx_f-EJN_ZS61Gs0rV2fyIfvdO88TN8dEftQlgQD8etAL4kHxsKMrlYoUFvumAqEaTOQSPWmoRAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRwT55nTRGRkzgIqb80_y8WW_eXqxJMBM6EsoDlBmTRbWetrEIbcTonhJw28BnO6b-N9HTnmEsDgFezhSgpfqZuYJwidk8kTzc4tWYFe-dKVwqOdcl4-AtlUw2AzKjZGEAy6WnfaLIKfBf8w8NRg2IhDxXZb9Mo_VmkL-VUO_jYn1vefYyVLUVaUY5Lx3lYfwUdrA6GigkI9hIElrBhWmCs_-bDbRTGBFYXKHmtutiygKGFdWYAXzjeD4StQS0L4y5G4xhuZKHV_r4SOq_bxiCA6yAKE0oO1VrKLXB54cG89tus09LeFUteTdisRGRPzZBODBlrqVQiFsa1yqMsF0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تغییر عکس پروفایل آدیداس به شماره ۱۰ آرژانتین
همه اکانت‌های آدیداس در کشورهای مختلف، عکس پروفایل خود را به عکسی از تشکر از لیونل مسی تغییر داده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107973" target="_blank">📅 01:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اینقدر غم امشب زیاده که آدم رمق پست زدن نداره
😭
😭
😭
😭
😭
😭
😭
😭</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107972" target="_blank">📅 01:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LvG4LdCnBX5VfqZK6QkHU7uZmoHHOKbmDO2_u07t-CCAcs9CpRI3tZ2nnoTNMug6CqSGEGFr4lNSibR_NBbf_zn3ZfojTNUIulFAJZ5mIgjvVTGKtX_vM4blFytUEtQtfUn7RNbLpnV99VsDFQlBOUNkB3TRBOup12KvVsxZggtu-fcoNSFvY3gSwS0YgVgJukcTNUq7YyBJIcMZvwk9cGHoz2kGM6NYPwyIJQz_yZM9u1iRVppA-y5EbXfwHkHW-I2eeNYzQHBxDby7Y7OAjtJLd-wAYRobV-sxPSRBJkEmo90ybVOHrHxDHqXP5NupHChdjAG_vnTzLsgZs2XfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
⚽️
The Last One...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107971" target="_blank">📅 01:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHBCP-Hzo34uFMDamFlXAuBVhdvK6DglY-sHflKSxde__F27sweG23g77zvGzmvdYgMI7KepShTU0isVLFvcGh2uChXj5bi0CJCmMIlDCCSKWT2F1RlJOoZC6YBSY6mgQ1M4-ItX_T16XNdGZn6EGh2HGz7LHFKBoGEikBF0sMPZXf4Eohc5MkleWtNJEtcSaBGH-5od8UNo3La5SNYv2iCmXo4A_A3OpdutSt8oyAxf9JudOtBksqPwtpkl0nvxijntdaSTjyjcLXPr2xSC5X9QEMg9P3tFy4E4sTfAXPZgrdZhUNTRBjhAJZvaXYuwoLuGYeL02SplGdOU-8vHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😭
گریه‌های لیونل‌مسی در بدو ورود به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107970" target="_blank">📅 01:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107969">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hotZSzBOIkghZhYEEhOyBIbk28FzuXzgRfMj1PDss1IPBKArZMtckQaNinU63rW0hJVhhwJF_H4WFyaohkODrVlBgQP3er2Eqt_sP9FyTgJIHo7JFSYnpcaBppUDqdYsRJul-1hSdKSpXbRN79ZK8MYcpJLxOMcdRXt_HwiykCZWayHs3833Xh6gWCtPC4VzC3Z4BAKjAwc4aBxfNFlxCrmVMYuXk-riuEr6vq3ClUtbsR4UzFi_OtUNHdPbQ4VWT5p5oMFWkLJ8tIpiPGsNmU1dF4E6aCb365_fA2FpTN1LHweJ4GVyA0Oe2qKfOyUs5lLfQTqjvJYpnEGNvqb8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😭
گریه‌های لیونل‌مسی در بدو ورود به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107969" target="_blank">📅 01:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107968">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozYNcpXHy1fwGk5nQHfpkxUbJ2cD-zFmb5GBQhw6xgBzr_vfKj1SodFeL5Mx22Rtiu5Ua974AiWV7ZoMdm_9SrV5fUOAZ7J2lx4ii2YZYLPdY0sBlU4Cy37Ny3wnlBHFCkHcjy4ho9eqGnUddBCcui70Bbp2qvhIkfdjy5Nu_KIB-AXbbALUbEwLg8PuiicaV5VuowbOhhd11OSq7dIGYv6YxddFwZE3UoFq_hSZ5VVaIVf7MYhG5C--vnY4WrkCoH0oLcPKgP9R96bK5Qs0k-ts6qvYXYj76LthhfQr14LvPPfAZDHD96ZoDyT46TwZ6oCEsIUuLJAlMODtYeMhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🐐
آمار فوق‌العاده مسی در ورزشگاه مونومنتال:
29 بازی
⚪️
19 گل
⚽️
11 پاس گل
🅰️
30 مشارکت در گلزنی
⚽️
🅰️
✅
هیچ‌وقت مسی در یک بازی در ورزشگاه مونومنتال شکست نخورده است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107968" target="_blank">📅 01:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577bffe68.mp4?token=Ov_djYuWuFiJk0-x4jqz3seXxtq_ZimVX9Ip3B7jHxj2QuZOuC0vuNdADlnT2MPH86JZI3E2tvOw61ecjy8G14RNNfnlUYO_N9MOERbju6gKqXcEv1-8f3xbielfEl81QQPCmYN_f8EkBXWn4esvReBjYexGMDxk5GCIoM3CYEHi4QPNEBdIJ-BthK4FT7psgznwRnvbTfneSHy2jL6H1Fi7X6OLYe2K973oR-z3kjb51bkwuvXodpBpElvpfEakcfpvt0CUMPKIPR0mrdvok9Pnnb07Rgq5G7jrws6cKGozzgQaesgOUs48NZ-Rf4LpmweaUfnz0IXTWy04fY_Klw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577bffe68.mp4?token=Ov_djYuWuFiJk0-x4jqz3seXxtq_ZimVX9Ip3B7jHxj2QuZOuC0vuNdADlnT2MPH86JZI3E2tvOw61ecjy8G14RNNfnlUYO_N9MOERbju6gKqXcEv1-8f3xbielfEl81QQPCmYN_f8EkBXWn4esvReBjYexGMDxk5GCIoM3CYEHi4QPNEBdIJ-BthK4FT7psgznwRnvbTfneSHy2jL6H1Fi7X6OLYe2K973oR-z3kjb51bkwuvXodpBpElvpfEakcfpvt0CUMPKIPR0mrdvok9Pnnb07Rgq5G7jrws6cKGozzgQaesgOUs48NZ-Rf4LpmweaUfnz0IXTWy04fY_Klw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
زلاتان ابراهیموویچ برای تماشای بازی وداع با لیونل‌مسی در کشور آرژانتین حاضر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107967" target="_blank">📅 00:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107966">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b38517c17.mp4?token=kpGP2iZ4cUc6DNkmaMe9bVyYCFrNzzIV7QzOP3_GPn4IfQoSHo2iRref7-zjZz7ZNCZ6UhJvRXHa-LWR3CJ5IYVB75hb-auJUE_mqt8e9ZZzQYfICKjShCvoBPe4zy39XJxBDspJGXfZCaddDN-7MzRnOrfFj1FIhBJ2qvaBlLf-CjsrzhUtUHJNVMEPXJtRJn35XM-h9lmOtK2cV0SCIZxViVQQ47tKn2Eilpbb6gpQKqKdaP3Z-gha5vu8814a1anl4apyWL5IBl5nv2JLp2GlLVBzTIwJwWXQSiN-WCnMp2LCln27ltTWNM1ruVm-aKaGUqcYWOG-ZkU6hArI_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b38517c17.mp4?token=kpGP2iZ4cUc6DNkmaMe9bVyYCFrNzzIV7QzOP3_GPn4IfQoSHo2iRref7-zjZz7ZNCZ6UhJvRXHa-LWR3CJ5IYVB75hb-auJUE_mqt8e9ZZzQYfICKjShCvoBPe4zy39XJxBDspJGXfZCaddDN-7MzRnOrfFj1FIhBJ2qvaBlLf-CjsrzhUtUHJNVMEPXJtRJn35XM-h9lmOtK2cV0SCIZxViVQQ47tKn2Eilpbb6gpQKqKdaP3Z-gha5vu8814a1anl4apyWL5IBl5nv2JLp2GlLVBzTIwJwWXQSiN-WCnMp2LCln27ltTWNM1ruVm-aKaGUqcYWOG-ZkU6hArI_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دویدن مردم آرژانتین همراه با اتوبوس لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107966" target="_blank">📅 00:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107965">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd4CO3rAfcAQpeNsf6vP2CZ5JKFbKq-LR1d6Tkr6SQWygLs3LKUvzdIlRoG2ufVgJRbxg1OwrPYTw0NEOA0cjFstB3ktbo8UM0M_dyYuileq07IAZj6KYE1f513R8MbVJpAM6sajoJ3jXhzHzTACiEJ8LrWhPgfLdExUBIDYA9vMJ6A0aH2Ep_6Pg1cJm7AVE5I5YOPcNWenRi2r31gQJFIl9lLypF1sW3leyE8pNqyEFtfE2JZAJyABmcnotx_0-8ca9qfRp1ybL2pBwRQDvBfidj4mTY8p7Ucxwk9PhVkQCPp0XmEfU6amgGP9Wys_I-weXXh4f_Mcl6h9VHGs1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⚽
رتبه‌بندی گلزنان لیگ ملت‌های اروپا پس از پایان هفته چهارم:
🥇
هری‌کین — 6گل
🇫🇷
مایکل اولیسه— 4 گل
🇪🇸
لامین یامال — 4 گل
🇫🇮
لیو والتا — 4 گل
🇮🇪
تروی باروت — 4 گل
🇸🇪
ویکتور گیوکرش — 4 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107965" target="_blank">📅 00:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107964">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fB4jxJ_V5yOY-1sgn9Paw-yHTMkTxjNYw5hIxn-P6Ez-h5uWN0FOn0qKZoELbLSRun6b4UgTovppqkPoLsFFSfGGOhfXD563JPG7cVFZ4VNX5KY9H5OulKVhiwJ43bcUFzRW3uAhD_EUrETSMesDECbnEeWzD6J1GGl-PvenRoAH6-AUDcdnLK6I9YNOvRVXnrrr3gNc_8GYE_7dcb-G83uAwocc9LHA6QB9rZBQLia59DsagNl5UzljEC22Qa7CB2CQa_W0MiWmy-fwp34nUYWdzvYZDzDBZL5WmPQMwWz5AKOMgNWe4hDdv2zj94STGD6fB3d0nhd-kcWdgg13sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره در راه ورزشگاه
😍
😍
😍
😍
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107964" target="_blank">📅 00:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107963">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=mKnk8xvOPMhiZNjsD8vCoISqlFFoofdCv8M24YonYGRFyCYNkpoP2Njp-3tVdHp6LF5fu0AOHmVnbknyzx1xpzn2r1lt3nF9kj_A6sGmqtum_yJnG4OJD4dA_aEXkPMhLNKURS9au-iBc2LrC5WSENJ6vE0e6nZS938nvOP27_CdEdzniBDjhm1qzzd0z_T8QXMKLofihRWKInGqiQu34kRkNdrDWjALTAMJDBrCDYou9va_OVMW0YJbsD0g1zAuRTkpDhdOY9l5sEK4THM7J3WvfT-_nN8_ePaqgw8bD7nIHoyhnIrv0pceYdNcr0OWoZBhqvUs-eqRNqyUIAtEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=mKnk8xvOPMhiZNjsD8vCoISqlFFoofdCv8M24YonYGRFyCYNkpoP2Njp-3tVdHp6LF5fu0AOHmVnbknyzx1xpzn2r1lt3nF9kj_A6sGmqtum_yJnG4OJD4dA_aEXkPMhLNKURS9au-iBc2LrC5WSENJ6vE0e6nZS938nvOP27_CdEdzniBDjhm1qzzd0z_T8QXMKLofihRWKInGqiQu34kRkNdrDWjALTAMJDBrCDYou9va_OVMW0YJbsD0g1zAuRTkpDhdOY9l5sEK4THM7J3WvfT-_nN8_ePaqgw8bD7nIHoyhnIrv0pceYdNcr0OWoZBhqvUs-eqRNqyUIAtEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه‌ای از دستاوردهای همتی در بانک مرکزی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107963" target="_blank">📅 00:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107962">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MARt9_x-sKnm7kLlr5jESLLLuLNynqQl1kp1nbxngAST5w8HqHRIUkIEQP1k-2sBvgwjwBwFt7S_LF9FyirTtM3oIYQbQQzmeupLOAbOpmciu7Z8WYIqpS0DyS_LkLgwcKMQCDn2mwprZ8woRI6k_jdvHSHz5POUoPDS-bPR3X01l6GVLq4ORSTAZA5NF00PuWX5J71ho3FBp9x4R7frayxEC2J43Ea_IlxJbAskgjossBNFGTj9-lHmLfFXWWu4kLHQTRDWdFFSVshKibdPazFhR8Ch3R4cgiF4vrf3UDfXzsD1R3FvF8bEWnXu-wVqFo4EpqNNqDJIXzwkuLdAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب تیم‌ملی آرژانتین مقابل بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107962" target="_blank">📅 00:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107961">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5uLRowWVYa72W6iAs6cbne4sMTBMnk_BATsj-S26RDlyltL5pVLfR_8Sk2gn56I6_5zN_47RLUiljrYBIqZbaWjO7iMwGB1XIA2a6jj-rWfPLENdLl-ErxNReNGh7pYOtlP0NCdXooYO0TDyZzJaDbtnt_Y0rlqtnmjfLXhl9xKpYf1TFP77KHqYXSSCVEODh67r5JXDYJJ5-GWmvxs-WCKrNR_tlxRYfKmqbBAUhPPutq5N1HuwtFWkr5A0TeNlL_izD0lPFWUAn6UN0FkU7Ko6AhkLaLV6x0CACxzuDDMQTr4wJU1X8X8lkkEVC4S3xlWPDZsPXvJaElENOJg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی اسپانیا به مرحله یک‌چهارم نهایی لیگ ملت‌های اروپا راه یافت.
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107961" target="_blank">📅 00:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107960">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107960" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107960" target="_blank">📅 00:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107959">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
فیفادی کسشر و طولانی سپتامبر و اکتبر رسما به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107959" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107958">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/580bfb3d91.mp4?token=hPG0dXp7Jt9HU1JbLhNFJYWN_hSGU6Ix0--FGhtPbGQ-OQVT8kmWgR8gBmvgz8IrYHM2PmmrH6kJsJJo74shKmfjI-fsyx7odf_nuD-KvIFS3dz1GFIIbs5-5geYamEZ2bW-PL8dsD-qRuTq_tuUE1gVtYPj6Rn1f3JD2azq9KpGOggbTCpzrp6MSbIg2DnTikGF-aCVNkmlhqj9zJgQ03nKk4Y9Fr-FT1FjKsUAOfiFaz9jAeGL14NRQMP2JholiYfzSzoK7nRReK4n5DNdHmDTx1Bw6mJZiTsaM7ZMz9rfhIXEvztkztH7n89SYCwddYFAJ2kkH_lG9IAJb4UEbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/580bfb3d91.mp4?token=hPG0dXp7Jt9HU1JbLhNFJYWN_hSGU6Ix0--FGhtPbGQ-OQVT8kmWgR8gBmvgz8IrYHM2PmmrH6kJsJJo74shKmfjI-fsyx7odf_nuD-KvIFS3dz1GFIIbs5-5geYamEZ2bW-PL8dsD-qRuTq_tuUE1gVtYPj6Rn1f3JD2azq9KpGOggbTCpzrp6MSbIg2DnTikGF-aCVNkmlhqj9zJgQ03nKk4Y9Fr-FT1FjKsUAOfiFaz9jAeGL14NRQMP2JholiYfzSzoK7nRReK4n5DNdHmDTx1Bw6mJZiTsaM7ZMz9rfhIXEvztkztH7n89SYCwddYFAJ2kkH_lG9IAJb4UEbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اسپانیا به کرواسی توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107958" target="_blank">📅 00:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107957">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0272b88.mp4?token=C0U5wF38dYGlHiBlrgQ1Lg-fdTbZ7t4ievpy0BIcP-Q7df_vmPsnpe19Z2cp3VpiIeP3zZEiUR0bBMhjo99ORPBQvtWzQT_wzbUYzDr3r0ZBS6LEnfsF_st13911Nz2NCVrIeMF-xtca1zeC8BxV-uJvdthUpa9KKqaYYE7HrCShjgxYbo8p7tThkuPyEc6Hu0UrZZrHy-kBdzQT6V9xNzyIz0ezuGBsZit-qjhuk-1wEUSBxrUV6AQENEgWGXLhSmjMS8TrFNTXaZn7urz1jRMopWhrJ8AqCPykEStsb1PGEeetAI7kG7f-ymgRbY1UwTulM133D1Dc9ao2dgtA0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0272b88.mp4?token=C0U5wF38dYGlHiBlrgQ1Lg-fdTbZ7t4ievpy0BIcP-Q7df_vmPsnpe19Z2cp3VpiIeP3zZEiUR0bBMhjo99ORPBQvtWzQT_wzbUYzDr3r0ZBS6LEnfsF_st13911Nz2NCVrIeMF-xtca1zeC8BxV-uJvdthUpa9KKqaYYE7HrCShjgxYbo8p7tThkuPyEc6Hu0UrZZrHy-kBdzQT6V9xNzyIz0ezuGBsZit-qjhuk-1wEUSBxrUV6AQENEgWGXLhSmjMS8TrFNTXaZn7urz1jRMopWhrJ8AqCPykEStsb1PGEeetAI7kG7f-ymgRbY1UwTulM133D1Dc9ao2dgtA0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول اسپانیا به کرواسی توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107957" target="_blank">📅 00:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107956">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa7164783.mp4?token=r3jlGmpP7aFkfemsmBUxGTaw79CoY5lXRntNJdG3YuCcrSqbr17XxtPdqEH1fJTJ8SJqY-RH2ZAnMS9EfsC4-l3eyWddsvCZwK-PtWjJ10_cQ7KGQIfAFoiWOBndXDNK36j8fTo75iqQV0EnG1lQFIjqkvix1wTeEibKy6S9qSAENYwNoQ_nFMlFMRYrU3zdMNh86cA_X0pY95P8HUrLGuIA1pB8Sl141YYgzo7SiBVmtypr5Sq-39BFDhrErLnhPJvvBnCH9xOBLTBY0Kr04Lq6-dCyRtiQPhnu4-ZKmFCFLhKAeMQ2cBiDnkMI9bqPIjx8W24V8ZBp0IpGP92iAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa7164783.mp4?token=r3jlGmpP7aFkfemsmBUxGTaw79CoY5lXRntNJdG3YuCcrSqbr17XxtPdqEH1fJTJ8SJqY-RH2ZAnMS9EfsC4-l3eyWddsvCZwK-PtWjJ10_cQ7KGQIfAFoiWOBndXDNK36j8fTo75iqQV0EnG1lQFIjqkvix1wTeEibKy6S9qSAENYwNoQ_nFMlFMRYrU3zdMNh86cA_X0pY95P8HUrLGuIA1pB8Sl141YYgzo7SiBVmtypr5Sq-39BFDhrErLnhPJvvBnCH9xOBLTBY0Kr04Lq6-dCyRtiQPhnu4-ZKmFCFLhKAeMQ2cBiDnkMI9bqPIjx8W24V8ZBp0IpGP92iAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تنها سه‌ساعت تا پایان افسانه لیونل‌مسی در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107956" target="_blank">📅 23:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107955">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0fbc6d16.mp4?token=HE0hpel2YrHEMLwZFGQAsUO4O1jzc8d1EDzja0YpDP_Tg1QjCm61cjs4w7XzebCRpXHMTTSFd5wajjVpyeEmLVpggjl_KC1S77E413mg5Hsk6z5g8xhZgBji5HDCH-Fb4-k3BZHc6FJBmAfC9hKEd_kEJx0-o_Q1LCnp_rhjrBTt3vRfHWOZM3RsZqUIj_3-W87F9Y6zoUtDdbiLQc5Im1AlVIIRzR94cR5uJcNKOzgh5GjRIQGfp4PshRbbNQouH-cVmxTXje-l8K7xqrySUZSoJg3E35ozQYZYZj1rt6xkG8Mr8ljhFly7bexzbSe22tzHDs8SYA-WBRUoJIHrfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0fbc6d16.mp4?token=HE0hpel2YrHEMLwZFGQAsUO4O1jzc8d1EDzja0YpDP_Tg1QjCm61cjs4w7XzebCRpXHMTTSFd5wajjVpyeEmLVpggjl_KC1S77E413mg5Hsk6z5g8xhZgBji5HDCH-Fb4-k3BZHc6FJBmAfC9hKEd_kEJx0-o_Q1LCnp_rhjrBTt3vRfHWOZM3RsZqUIj_3-W87F9Y6zoUtDdbiLQc5Im1AlVIIRzR94cR5uJcNKOzgh5GjRIQGfp4PshRbbNQouH-cVmxTXje-l8K7xqrySUZSoJg3E35ozQYZYZj1rt6xkG8Mr8ljhFly7bexzbSe22tzHDs8SYA-WBRUoJIHrfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
💋
پرواز لباس غول‌پیکر لیونل مسی
به کمک هلیکوپتر بر فراز شهر زادگاه وی ، روساریو ، قبل از شروع بازی خداحافظی لباس غول‌پیکر مسی به پرواز درآمد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107955" target="_blank">📅 23:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107954">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2d316bd4.mp4?token=ihUa0jH9LmrIpQiF3Gs7Ziq11t9udXvytlLhgVwYaAoBSnReE53gYP9u0oR1BTSnxDU91gX2mtypYXjHVJdBCDqi5H-iVMzEbKEGZDiUcmfduBFy2DQTG8mBvXu-TerX9nTGO41Ah2HqYRekMmr1DwNBT4cbU_OzCM8ciLTs2TaRAbDD0FrbPK0OQyGaSvbCUF9XuzcteE4BLczx_pItVorwC4cDAeBiRTLtn0npc567bJB1iQQqEs-ITMILKNmp7wFA3bMC0Jxc-6zvgOW2IS1izfvDM1Ja4QtD_Bcs5sSMLqNLvDE-fwAgFpAEqshn1VdglT0FErHjlJGOpoQQE5pwQOmJU6VPeK3yiTeeW5chY-2RRENjsbaTXfsuHGGiSrTL9JqP6wqPQfed3D6V84emOSlg67ltEAi4jTNIycBfPUBEFswzqJf9uJOrjiRsNhlQVQZmETu2PdoIHrvBy1HuH7V4Biu0vclU3311l8zS0DrW7i32oZbRho6LUXdzQ9oYSnfzGHlaTrpd-SIi-9KGvvFQU-wEyFko9D_oA046kxJcmfrgEjNTHU39ZIDvCwInaAfVdAP_LJiWtlYwSC2Fqzb8G9M4qA79u53nvuOIlDhFK224BvCXoaA4gyDcchG0r3e-4PY6e7DwNOIlFUkge8UCQsvZUbb_nuIaK5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2d316bd4.mp4?token=ihUa0jH9LmrIpQiF3Gs7Ziq11t9udXvytlLhgVwYaAoBSnReE53gYP9u0oR1BTSnxDU91gX2mtypYXjHVJdBCDqi5H-iVMzEbKEGZDiUcmfduBFy2DQTG8mBvXu-TerX9nTGO41Ah2HqYRekMmr1DwNBT4cbU_OzCM8ciLTs2TaRAbDD0FrbPK0OQyGaSvbCUF9XuzcteE4BLczx_pItVorwC4cDAeBiRTLtn0npc567bJB1iQQqEs-ITMILKNmp7wFA3bMC0Jxc-6zvgOW2IS1izfvDM1Ja4QtD_Bcs5sSMLqNLvDE-fwAgFpAEqshn1VdglT0FErHjlJGOpoQQE5pwQOmJU6VPeK3yiTeeW5chY-2RRENjsbaTXfsuHGGiSrTL9JqP6wqPQfed3D6V84emOSlg67ltEAi4jTNIycBfPUBEFswzqJf9uJOrjiRsNhlQVQZmETu2PdoIHrvBy1HuH7V4Biu0vclU3311l8zS0DrW7i32oZbRho6LUXdzQ9oYSnfzGHlaTrpd-SIi-9KGvvFQU-wEyFko9D_oA046kxJcmfrgEjNTHU39ZIDvCwInaAfVdAP_LJiWtlYwSC2Fqzb8G9M4qA79u53nvuOIlDhFK224BvCXoaA4gyDcchG0r3e-4PY6e7DwNOIlFUkge8UCQsvZUbb_nuIaK5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به جمهوری چک توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107954" target="_blank">📅 22:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107953">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f36f54f3.mp4?token=SFE-9BPjzJpyAMvXmdSQKFGFv87rHAPBVxzzTWP-2ZgGP8KD5mMiv-Be20P0Ej9lcFwDnHOKxth1zk3Kiv3gHS8p-ugSDxTJqN-mnGsa2EYqk3slA2g9gjGEPp3Z01NW9MFxXDjbD5ONc7kE1_J9ipO6XwXYssLdldx9GHjQclEEcLuVAnM42tRIlXfJgtXZJ51oMkbrJ5bbAK0affuoR7ACiVtVzBy9J1D09ZoqhpPMD3EEgLHEkdU3Dd8EwYQ9zxchga4Longbifom5YU4NRml4k3mn5IsuJTvfAqNhfxqMPx91srBV_TX3LbfecNNDK9ogxpO0KYauI6lPCQR0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f36f54f3.mp4?token=SFE-9BPjzJpyAMvXmdSQKFGFv87rHAPBVxzzTWP-2ZgGP8KD5mMiv-Be20P0Ej9lcFwDnHOKxth1zk3Kiv3gHS8p-ugSDxTJqN-mnGsa2EYqk3slA2g9gjGEPp3Z01NW9MFxXDjbD5ONc7kE1_J9ipO6XwXYssLdldx9GHjQclEEcLuVAnM42tRIlXfJgtXZJ51oMkbrJ5bbAK0affuoR7ACiVtVzBy9J1D09ZoqhpPMD3EEgLHEkdU3Dd8EwYQ9zxchga4Longbifom5YU4NRml4k3mn5IsuJTvfAqNhfxqMPx91srBV_TX3LbfecNNDK9ogxpO0KYauI6lPCQR0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
مدل‌موی مارتینز به احترام مسی در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107953" target="_blank">📅 22:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107952">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7217759036.mp4?token=OIXBZblj1DluL8qYMawd9KV-BzvsLGhwTgpxs0KQjiS4raSZSjwh_3Pw4Jxx7NXO6MSshRq_y7jt9MqM6nu6gdR0j5yvBK9sqqXejmCdHl15rqR5MXRV8NYDftU75cKXIt9qwHcjbxH_Rpr0EefvU6G-E4K_Z-dqusMcE7tBCkwYqAxwFGAFi8V7snpBWoubG4OgUAY9rSLvnZGIEP43z5B49-fXyCPx-2vBhVqhnd1YZ0bOD8Tl43iOwecS18BorZLmcpCMAVkHj4sA1WBYjmKPeGhi-OiwXT23edqfu4JDGooczlbpmIgvly2CMqBkDTZW-XpjL072d7vaPrzdvEXxfNIJM1oAEHXo_urOts81MzaWVwcnSqpSyzFEUnPLkHaAA4GhcdUjKpjx9eoK3lJr5EaUI-R-WUWhKxU4w1p1N4yYJoD4opxxVj751Cp87V0J0pXhrwXGlV8Xa5qCK4I8C_iZyJsmY-pnyTdY9Jh5IL-1dvhTlATCUzVAWtAqfJcYNseXTchID83JmwPyKMN2JS5Yl_QHPpnFQ0Y6bPZpXte4OyJAR3xGce60eNw1PmZpgLFbsRqf3oG3SF4eLH7u7XMDWWf8bezE7un8H3PX1ozhOXS8eRwlhJdnZgrEscV_bYqw8cqm2OaIh4MUcgFSvO4aVwgqjSbWpFC1CaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7217759036.mp4?token=OIXBZblj1DluL8qYMawd9KV-BzvsLGhwTgpxs0KQjiS4raSZSjwh_3Pw4Jxx7NXO6MSshRq_y7jt9MqM6nu6gdR0j5yvBK9sqqXejmCdHl15rqR5MXRV8NYDftU75cKXIt9qwHcjbxH_Rpr0EefvU6G-E4K_Z-dqusMcE7tBCkwYqAxwFGAFi8V7snpBWoubG4OgUAY9rSLvnZGIEP43z5B49-fXyCPx-2vBhVqhnd1YZ0bOD8Tl43iOwecS18BorZLmcpCMAVkHj4sA1WBYjmKPeGhi-OiwXT23edqfu4JDGooczlbpmIgvly2CMqBkDTZW-XpjL072d7vaPrzdvEXxfNIJM1oAEHXo_urOts81MzaWVwcnSqpSyzFEUnPLkHaAA4GhcdUjKpjx9eoK3lJr5EaUI-R-WUWhKxU4w1p1N4yYJoD4opxxVj751Cp87V0J0pXhrwXGlV8Xa5qCK4I8C_iZyJsmY-pnyTdY9Jh5IL-1dvhTlATCUzVAWtAqfJcYNseXTchID83JmwPyKMN2JS5Yl_QHPpnFQ0Y6bPZpXte4OyJAR3xGce60eNw1PmZpgLFbsRqf3oG3SF4eLH7u7XMDWWf8bezE7un8H3PX1ozhOXS8eRwlhJdnZgrEscV_bYqw8cqm2OaIh4MUcgFSvO4aVwgqjSbWpFC1CaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول انگلیس به جمهوری چک با گل‌بخودی عجیب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107952" target="_blank">📅 22:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107951">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=ioMqzq32e7t1uE--ASLqHgtDUka5GfG3s4Q6xheQYn44gD6tm2SGv41GhGR--PELueGRdOGyj5J4XVQA-kMowyGtwu41AnB-YieYGXyQO0gCunxE57nXUqsa-gY4BD_2-ymAenG3kZDr8uGj9zKeiUW5fs6ZtPwrEMHl8HPDJoyFqTu6tRqBx2So33G7X3OeiQRA-qNVrhU0WTjLITjZjYomoPAU31F-SMoFdIXeplYp0LYeW28PQbRjYSVEtHc6bZJF4gi274hGbm3h9x3E0Lrlqu0daLH_m_5SnNCTyjxoL9XP5gTeJcabovodYIh9W6mmbLMnUD3BhtvK6nGWFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=ioMqzq32e7t1uE--ASLqHgtDUka5GfG3s4Q6xheQYn44gD6tm2SGv41GhGR--PELueGRdOGyj5J4XVQA-kMowyGtwu41AnB-YieYGXyQO0gCunxE57nXUqsa-gY4BD_2-ymAenG3kZDr8uGj9zKeiUW5fs6ZtPwrEMHl8HPDJoyFqTu6tRqBx2So33G7X3OeiQRA-qNVrhU0WTjLITjZjYomoPAU31F-SMoFdIXeplYp0LYeW28PQbRjYSVEtHc6bZJF4gi274hGbm3h9x3E0Lrlqu0daLH_m_5SnNCTyjxoL9XP5gTeJcabovodYIh9W6mmbLMnUD3BhtvK6nGWFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤯
سیل هوادارای مسی برای خداحافظی در آستانه آخرین بازی مسی برای تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107951" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107950">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d806496fdb.mp4?token=wBBAZz-DfDAkpXqSY6M43fcAdjNee5QaFKR_vBly3s2Spqjw4Kkv1SSaIGe_8bdhJhe2JHN32tNvSY3dIiRApy1J-D3e8_dQXirRLYgdj6PiTKWTL9EUy1wFj73E-P5e8OM9vw8iBbsfmIWaYPiKGYjWhPKpQO1upb1u8_vwSli3mqv3qHgBiR84Q08Ia48GLMAlqJ05VDODU2PLtwiR_pzi1dmD1V-MH__XcGE5gfrixSwTVLuYrFia0lHAqo1bCa3mhpJiKSAXbelg0NzDedOWbHIKg0NgODbS5J7HmagR2mzjjfNW-54VSEmY7SFSX8IAIb6vm344n4OhqUlpTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d806496fdb.mp4?token=wBBAZz-DfDAkpXqSY6M43fcAdjNee5QaFKR_vBly3s2Spqjw4Kkv1SSaIGe_8bdhJhe2JHN32tNvSY3dIiRApy1J-D3e8_dQXirRLYgdj6PiTKWTL9EUy1wFj73E-P5e8OM9vw8iBbsfmIWaYPiKGYjWhPKpQO1upb1u8_vwSli3mqv3qHgBiR84Q08Ia48GLMAlqJ05VDODU2PLtwiR_pzi1dmD1V-MH__XcGE5gfrixSwTVLuYrFia0lHAqo1bCa3mhpJiKSAXbelg0NzDedOWbHIKg0NgODbS5J7HmagR2mzjjfNW-54VSEmY7SFSX8IAIb6vm344n4OhqUlpTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول کرواسی به اسپانیا توسط ایوان پریشیچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107950" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107949">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گگگگل کرواسی یکی به اسپانیا زد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107949" target="_blank">📅 22:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107948">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNGFZpDBYHieExcYM9cDkGTveQu5qvhldbUH9bC5i8zM6HW8BTpTcm_SMczECQC7NyAiGPI27qMR2Wtmf4g8S9OcXpSvLjxCq0dOc82Q7jmns3C5XEfNDRGyts8HpiK8Ift0AcVPxZGY1wWjwky_uC9HK3kxzdGMfW1tQl4DUO_TolgB_hqr9r3NGwtVYORMTg_YMZEVwetHmTh7gnO7bnhAdImR77C8fxw5JdacVvXwvXguAc_gv7qI-_Gf_aNHuWCaZxlOtoUJqcHEYOGiyUz33FDsW8Va2w9KKtp0Tj81sIORoANTsTqY1Y6Y8JozyLgk1wTOGRvlDuj0a1YNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
خلاصه‌ای از بیانیه کریس رونالدو:
🔻
رونالدو تأکید کرد که مربی قبلاً با او توافق کرده بود که در یک برنامه مشخصی برای بازی‌ها شرکت کند، و بازی با نروژ در این برنامه نبود. سپس، به طور ناگهانی از او خواسته شد که برای بازی 30 دقیقه آماده شود، و در نهایت، با وجود…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107948" target="_blank">📅 22:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107947">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🇵🇹
اسطوره رونالدو:
🔻
بابت ترک‌ناگهانی اردوی تیم‌ملی از تمام بازیکنان و مردم پرتغال عذرخواهی میکنم. من به عنوان کاپیتان تیم مستحق جریمه و مجازات بدون هیچ تخفیفی هستم
🔻
همچنین به مردم می‌گویم که اگر شرایط ادامه حضور داشته باشم قطعا دوست دارم برای کشورم بازی…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107947" target="_blank">📅 22:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107946">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VL-4wJ_x0eGhSP6Ta4Bm3yFFY93PnBpWoLoYoKjyX-NUk-Zq3oF68kK96JkPvg8b3riQ0MxwhtA_kOzfwmVcKnSHc6eDg_kBPG4RVRmX2TIysVreVmPLr7HHYlXsuEvY6WDUSHC8xa12Je1FPiYZWSg_Tv3i-9z04LJReYe58GvAgl-6hFNByl-r_ZOF_gf71XwzT0FGH1ZIxIJ3rVhkzRuM4T_V-PkTmcUwDKF2OGRAStkJLIBM9fpUlsOwqcYmvy_cxCPbrPJXknL3UWn0Ws5Ib_tlYtlAxL88Fs_-fBToC2ImZ-Xq7dWkCflO3j9vFPwHbU9IQiDzcMo6fjw_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره کریستیانو رونالدو:
🔻
جورجی ژسوس برای اولین بار با من تماس گرفت و گفت که مایل است به صورت حضوری با من ملاقات کند. من موافقت کردم و قرار گذاشتیم در پایان تعطیلاتم با هم ملاقات کنیم.
🔻
آن روز، مربی به من گفت که به من اعتماد دارد و حضور من برای…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107946" target="_blank">📅 22:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107945">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
بیانیه‌ کریستیانو رونالدو:
🔻
بعد از جام جهانی 2026، من پیامی برای مردم پرتغال آماده کرده بودم که آن را تا امروز نگه داشته‌ام و آن را زمانی که به طور نهایی از تیم ملی خداحافظی کنم، برای آن‌ها ارسال خواهم کرد.
🔻
بعد از مسابقات، رئیس فدراسیون فوتبال پرتغال…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107945" target="_blank">📅 22:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107944">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
بیانیه‌ کریستیانو رونالدو:
🔻
بعد از جام جهانی 2026، من پیامی برای مردم پرتغال آماده کرده بودم که آن را تا امروز نگه داشته‌ام و آن را زمانی که به طور نهایی از تیم ملی خداحافظی کنم، برای آن‌ها ارسال خواهم کرد.
🔻
بعد از مسابقات، رئیس فدراسیون فوتبال پرتغال از من خواست که با تیم ملی به همکاری خود ادامه دهم، و همچنین از من در مورد انتخاب مربی فعلی نظر خواست. من به او گفتم که این انتخاب، گزینه درستی است. بنابراین، از انتصاب او خوشحال بودم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107944" target="_blank">📅 21:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107943">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ9nRtxDO_ebBffHdPY4QwW9sD_yJjpWRmjcRLHti3L0n1S_CcAduFbm2RyB_ptc4T9QmybF1j2eQ8Hbr_O_DNp1g79hVJ-sUXRmeZMbUWvt6dC9V79KuNH8-eJRff-nMdzAEvh3jG_dgcNT1jBMZJ135PDWcX7epzoj-p0e4mtruWCATeXMLiWMaD3_AatySU-A8a655lUr88dA4twrwFleayj9IF8n7D8rPChp03Dhhhpj9if0a6fYa3Fq4QwOTxmKp2ytY1CC_PXc6qCICekJa5TZiczvFe9x8bVoop3qt5cLe9mRTXUylPW4ZyEDaG5Fu8rnQ1wR3c378XFFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107943" target="_blank">📅 21:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107942">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8036043b2b.mp4?token=sSZFhUOApH179LxkQ4IBtWQFSJFd2elWzvisAPotM-4eTX1XCAWJbS1pC4LekPgbD-k-GpG3VGhJnp_l55F-KFgM57p3eEbRlhkRs8QtFyxuEPYtGpG4UT6K6qIDc-PN53Gq82I24dqMpcLM4b1fomHVhkIG_iOirGrdCP_nnd5hhnSYrZTQ7EZIHXo4JJh_L15l3bTk4XpUc-NVVL5QmCMKFTnbGFW1p6Zrbo-AZGN_8xcG8FZoA9HoIj_bLN2peJffTifPUvnq3Ra7_VBYnxPVooFJarvEbxNn2cHo7IrHmZh9uqp4Mf-LIXGOPIVwnNWYNPVfcztwbimnU_11ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8036043b2b.mp4?token=sSZFhUOApH179LxkQ4IBtWQFSJFd2elWzvisAPotM-4eTX1XCAWJbS1pC4LekPgbD-k-GpG3VGhJnp_l55F-KFgM57p3eEbRlhkRs8QtFyxuEPYtGpG4UT6K6qIDc-PN53Gq82I24dqMpcLM4b1fomHVhkIG_iOirGrdCP_nnd5hhnSYrZTQ7EZIHXo4JJh_L15l3bTk4XpUc-NVVL5QmCMKFTnbGFW1p6Zrbo-AZGN_8xcG8FZoA9HoIj_bLN2peJffTifPUvnq3Ra7_VBYnxPVooFJarvEbxNn2cHo7IrHmZh9uqp4Mf-LIXGOPIVwnNWYNPVfcztwbimnU_11ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
حمله تند خداداد عزیزی به مدیرعامل تراکتور حجت‌کریمی بابت مصاحبه دیشب در فوتبال برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107942" target="_blank">📅 21:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107941">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a98f55b4.mp4?token=lu9i4X20f_ZeTE394fJlY2-RlEoS9dt3lFKQJhY3lqYHj2RG87K0bEC0hR6uw6LjA1sPLEwFy-OwtLMyBW_k_AJIBMQNaQyWkzngFMQKYrte0EvkDLWV7Gs05ia1w6Mlryobbst8VTzbjeX_mPd1jpZtR34tD5REXIbPFeLFxci_LZlP4CyxB6UGAs48toEdEToD_PaWrMKhm6lmlJheJy7QNiLagNV-JNu5mvB-Heau2F4L-Mont5j0XpQwdV6qQCg79uhzdt7HBkR3tiX38Kbxob7yQt-eTr8ziuw3jaE2DCYSzY9QLKk-iyzeYwLGIFfD58_KqQJthUOg9dhKRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a98f55b4.mp4?token=lu9i4X20f_ZeTE394fJlY2-RlEoS9dt3lFKQJhY3lqYHj2RG87K0bEC0hR6uw6LjA1sPLEwFy-OwtLMyBW_k_AJIBMQNaQyWkzngFMQKYrte0EvkDLWV7Gs05ia1w6Mlryobbst8VTzbjeX_mPd1jpZtR34tD5REXIbPFeLFxci_LZlP4CyxB6UGAs48toEdEToD_PaWrMKhm6lmlJheJy7QNiLagNV-JNu5mvB-Heau2F4L-Mont5j0XpQwdV6qQCg79uhzdt7HBkR3tiX38Kbxob7yQt-eTr8ziuw3jaE2DCYSzY9QLKk-iyzeYwLGIFfD58_KqQJthUOg9dhKRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
افشاگری بهداد سلیمی از ناداوری در المپیک ریو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107941" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107940">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8dd97c34d.mp4?token=k089iV8TwRDrevGFjsIqeV_T8b4ykj7U3T8z_mICuYCh0TztTzWm_6l5EWOzhV9ETBZnvJxZdD4E02ZRGNUpxKMWr5MyKwrbhBjeqP3HO68CGrs3sSTVc-S0zrfKYzp8vX2PC4iwlxOgMQTa9g7zBk_M37cNjgBTdmWMJjuGThX_lLErOOwT72GtUNJF4ay_HSgB2nHBfe13Mt148GsCVQeQeQTLeFkglvz6Lf9MJqDzvSFKztKStOyjixvG_XzYn-UJ2Rvg8lPV8EjQ0_TRKiUubG-nSIZ5WU36-_18-g0Lv7t-8tiZCmFDQWBLRO0052ZsNseHjazdUV7VS_WTmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8dd97c34d.mp4?token=k089iV8TwRDrevGFjsIqeV_T8b4ykj7U3T8z_mICuYCh0TztTzWm_6l5EWOzhV9ETBZnvJxZdD4E02ZRGNUpxKMWr5MyKwrbhBjeqP3HO68CGrs3sSTVc-S0zrfKYzp8vX2PC4iwlxOgMQTa9g7zBk_M37cNjgBTdmWMJjuGThX_lLErOOwT72GtUNJF4ay_HSgB2nHBfe13Mt148GsCVQeQeQTLeFkglvz6Lf9MJqDzvSFKztKStOyjixvG_XzYn-UJ2Rvg8lPV8EjQ0_TRKiUubG-nSIZ5WU36-_18-g0Lv7t-8tiZCmFDQWBLRO0052ZsNseHjazdUV7VS_WTmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
علاقه‌خیابانی به گزارش بازی آخر لیونل‌مسی در تیم‌ملی آرژانتین که بامداد فردا برگزار میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107940" target="_blank">📅 20:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107939">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e0f6c80a.mp4?token=AH9cqJXifhcf3oiHTegLVRB4wt-Zmeuvgkgeslu-0T4kA2zzt5JqFS_fYSRj_h5A59JJ6dD1_ZHk-dIphy48k7kvWEXVj2VM5yb2D0FQ_4q-orbouzon1DJ3UProuWqZut3BIlZ_KHAso1HN-KwaW13-T8c5-cJAED0_NwzypB_lmMzexjLkUwfkfh6VH-nGdEKNqIXnDT2WzGsob-B8VD6Hn5PPlL2aJknQUoU0nfG9mrfkJtLMhaRYilgEGHTpFFD9fGbBBXDfv8DIE3Rq-4V2IzLPiFWXSedMICqh2jkNp2d8qzU8oRLjs4rMPmV6IZn8aLeWZ9aImw0CdFc66Az8aNGD5eW35AKC5ceQBNm6opt31GHP7VfEDjmaXe9d59ELIDpC-U9LO1mUtdLBZdFo7m5mOo8hhJ4ALZwUzQpePACAyVUMkia1IkFn64TazwsSmtxnB0Ms4f5PtdcOMFPUmR-Pi3ilbFbLZUPaC1jEqTBS2OMdOX-7x6CrjEM9nCEUfSNK2Wape2OXp4ZKEY2TmCqr8uLCM11tm2qUMk8vKq2qAlG6Jwe6u1ASsa9-nAeoPrlxoKqCdMOBd3sC6o5aTgjHO_MgRasOi6iQtrStNqmv3cdL7mxBYuEvPwJ9QzWpVUasahpB2aWPB7dlU0NC1Y0C4s7BeTk6uppQNHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e0f6c80a.mp4?token=AH9cqJXifhcf3oiHTegLVRB4wt-Zmeuvgkgeslu-0T4kA2zzt5JqFS_fYSRj_h5A59JJ6dD1_ZHk-dIphy48k7kvWEXVj2VM5yb2D0FQ_4q-orbouzon1DJ3UProuWqZut3BIlZ_KHAso1HN-KwaW13-T8c5-cJAED0_NwzypB_lmMzexjLkUwfkfh6VH-nGdEKNqIXnDT2WzGsob-B8VD6Hn5PPlL2aJknQUoU0nfG9mrfkJtLMhaRYilgEGHTpFFD9fGbBBXDfv8DIE3Rq-4V2IzLPiFWXSedMICqh2jkNp2d8qzU8oRLjs4rMPmV6IZn8aLeWZ9aImw0CdFc66Az8aNGD5eW35AKC5ceQBNm6opt31GHP7VfEDjmaXe9d59ELIDpC-U9LO1mUtdLBZdFo7m5mOo8hhJ4ALZwUzQpePACAyVUMkia1IkFn64TazwsSmtxnB0Ms4f5PtdcOMFPUmR-Pi3ilbFbLZUPaC1jEqTBS2OMdOX-7x6CrjEM9nCEUfSNK2Wape2OXp4ZKEY2TmCqr8uLCM11tm2qUMk8vKq2qAlG6Jwe6u1ASsa9-nAeoPrlxoKqCdMOBd3sC6o5aTgjHO_MgRasOi6iQtrStNqmv3cdL7mxBYuEvPwJ9QzWpVUasahpB2aWPB7dlU0NC1Y0C4s7BeTk6uppQNHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ترویج دروغگویی به دستور فدراسیون و کادرفنی؛ لو رفتن ماجرای تعویض زودهنگام محبی مقابل روسیه در مصاحبه احسان حاج‌صفی؛ ناراضی بود، گفت بخواب زمین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107939" target="_blank">📅 20:15 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
