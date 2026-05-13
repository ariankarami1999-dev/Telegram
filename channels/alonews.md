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
<img src="https://cdn4.telesco.pe/file/lowYcSn0XK7aIQbaTOU1ed5wfYafMkO27kNDECxkMbv6mh8EZ5ryeZX-3U7fH5gC6JuobQ1Ntxbo2hHKcyMLQfa2nHd6TD8KmqzGZ3ZHxYditFOu57loIvQ8pcTPNUJsqwgn7MbbcZiXoxHbHSGuNK3mN4RcBOL2IaTaCk2oYlSB2lH4IfNYmwzNBRfUISgEzI1ZBugwf1XeUqpsRwdkIk6sAb3-vFOXQ5fOzeEBpZC8OrK_G5lFImwXeQcK4CDy5naXQiXnOnsfgarGoDiWsyIuKX1bAyQ8JupI8BKQlHSP-FbRGfr8VNXorcfN_T9t_7mQdWxa-03kCyC8oRSLkg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 961K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 17:39:47</div>
<hr>

<div class="tg-post" id="msg-119750">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MDPVuDsPqbdcbIGD0KG-TfEA20zemN_CFJdLccfGnTDuM1wq1VAjZwssvJsYhx2C5izZBcYe4NMTWnZF8gcCKXB-0bXoyGUiES3Un8BwFVrOqhc0a1fpwife7DaGbDnPc_hIH2oKN4HozR3POzvY8QfUhgk-KpYDOJlhVWHJIFR4irkXPIejXQ4d_8fqnOc0nosLEYGnjfyx6ziJCbwdMsgo13do7EiU8JjBF9aZR8axOwJRfYNwFDw7K-FpkwWtqpVgUQ3ZuSXKYd59A5aB7fgfbMMYf9-fXbCQ3LAy-e4hB9C4Q-6cQ-BYOjAo6L6Gq0Vfzdtnf5P0C92P3EJHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZqT7VyBhwTjbmbb9nKTONuw1QjLE3L-K7uiAmjZQ2MDtzbN-aawqYY2f21OCs3jxbQOEKOzSToT9CbPyIP6-vfvzCIsoAIAGCMOC0_VzJyiTLTh6HfWpaaPlvRwFe1BELFlyPUgfbloBMm2ivyftqIpqxwn2ech2ObDrpnsKRWXEbiJupBV_xrcigmp5V-CWkToMqGErKTkEVbQHCpdSjEHtlMe7_n3q4Z011WnvR7_wg6rZK50oQ6krT70DHqsx3I_92AchMNEPpmV7IU9euJOz0d5f1BX33MpVAcrRyqk6B9zm1HeX9ghwOj8pv0PAc9GYp5S59WOOad8SMNOMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af69a990d.mp4?token=gjvHi3j9JR6WkWjYUi118utodwCRQnf_5gGYxED-lVh_lvM06MSOFTPy4xZVZSKfp2NI0bSVEiQKTiUT1CGWrkwtVwA88QU52MnhwpeLJvvd9Vv3ukY9y1HcEe3HpjigzBbzynC_qBUEgFSsS_F6OcwoG9hYZrC7HpiOR6FwvCZv2wqJYbTE-KYfI5F9OM2dkOvSAwTgnyOo3uml_rN0xBZsmXS0eI9b57kSxc4Ic0Lmd0XzqhjSyMgqIXlulJBGMxvQyUtKet5BJajyUrhLURMttL8U8C1qcWruv6b_ua833F7fWaFsjVXukHC2iT0iDSynYvHLI-MzPxzcbbWwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af69a990d.mp4?token=gjvHi3j9JR6WkWjYUi118utodwCRQnf_5gGYxED-lVh_lvM06MSOFTPy4xZVZSKfp2NI0bSVEiQKTiUT1CGWrkwtVwA88QU52MnhwpeLJvvd9Vv3ukY9y1HcEe3HpjigzBbzynC_qBUEgFSsS_F6OcwoG9hYZrC7HpiOR6FwvCZv2wqJYbTE-KYfI5F9OM2dkOvSAwTgnyOo3uml_rN0xBZsmXS0eI9b57kSxc4Ic0Lmd0XzqhjSyMgqIXlulJBGMxvQyUtKet5BJajyUrhLURMttL8U8C1qcWruv6b_ua833F7fWaFsjVXukHC2iT0iDSynYvHLI-MzPxzcbbWwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کتاب جدید یک خبرنگار مجله پاریس مچ ادعا می‌کند که رئیس‌جمهور فرانسه، مکرون، یک رابطه «عشق افلاطونی» چند ماهه با بازیگر فرانسوی-ایرانی گلشیفته فراهانی داشته است که در آن پیام‌هایی از جمله «از نظر من تو خیلی زیبا هستی» رد و بدل شده است.
🔴
حادثه باند فرودگاه ویتنام در مه ۲۰۲۵ که در آن به نظر می‌رسید بریژیت همسر مکرون به او سیلی زده است، در واقع یک دعوای زوجین بود پس از اینکه او پیام‌ مکرون به گلشیفته را وسط پرواز در تلفن او دید.
🔴
کمپ بریژیت این موضوع را رد می‌کند.
🔴
فراهانی در مورد این ادعای خاص اظهار نظری نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/alonews/119750" target="_blank">📅 17:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119749">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suHyejSsrESdRrzv0T7ljBph1sU1BI6BQKk-lLD_TL_jrIIUapIYRpza7-luKelZkscvc0leqI_cNFE4_DjnmCrwjcr61Flo6ud4VAwZKHIQxG33Sd56b7UgInfUU0sUIgfKy5qZxo0cfvvWX2hgO38J_8XlT1wdfEHLPrE1XLDKIeoLlDjJ0CwuIYx_xLagLw60aqzAJslyvBxiT3FaDneg1XpTKWqhHKpK9dZqtcx6G-q-cFufGxKLmAR8oizHrwiv1n4xgOAD7PonzicdlGJTYDCj7YytAzPX8Ei64c_-6YqLXm2DGqBpVStjYSyMJTbo8MLcz8c1o2JEcefTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بروجردی،عضو کمیسیون امنیت ملی:
دستاورد تنگه هرمز را از دست نمی‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/alonews/119749" target="_blank">📅 17:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119748">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3813de281a.mp4?token=RpXUKh-f2BLeMW_dzy5Ik0W_Z5MencDNU2YEMTlvt-QfoARXBS2IbvieujRGOSRHGLga3T25c7wvfTNl5RJNfC56XmkkaxaMdC8Pygn67e-qLdURwXSW0Sr7tWM0t3X3AvPaxoxTxkZIBERt1gUwZc82ZmgRXn8QEZHTBTorgNv-OQCYQRzFnFqSw-w3eiKePtXFVChYmtc4HbadYR9rUnhLR4MxWRi6hNXT6-J9rsPBfX5LiuIInP4FIKFjcYsMqUgpcbdWX0t5onGRcAMBsL3ICTQd9RT6OzTlM9Re0sr0DfRu6kxNiaiyGstKDCT0zMuaHjGXK9_LmSoEl9rxGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3813de281a.mp4?token=RpXUKh-f2BLeMW_dzy5Ik0W_Z5MencDNU2YEMTlvt-QfoARXBS2IbvieujRGOSRHGLga3T25c7wvfTNl5RJNfC56XmkkaxaMdC8Pygn67e-qLdURwXSW0Sr7tWM0t3X3AvPaxoxTxkZIBERt1gUwZc82ZmgRXn8QEZHTBTorgNv-OQCYQRzFnFqSw-w3eiKePtXFVChYmtc4HbadYR9rUnhLR4MxWRi6hNXT6-J9rsPBfX5LiuIInP4FIKFjcYsMqUgpcbdWX0t5onGRcAMBsL3ICTQd9RT6OzTlM9Re0sr0DfRu6kxNiaiyGstKDCT0zMuaHjGXK9_LmSoEl9rxGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من خطاب به بابام که میگه ۱۰شب خونه باش
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/alonews/119748" target="_blank">📅 17:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119747">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رئیس ستاد ارتش اسرائیل:
جنگ با ایران پایان نیافته است،برای از سرگیری جنگ در هوشیاری کامل قرار داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/alonews/119747" target="_blank">📅 17:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119746">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: نتانیاهو امروز با رهبران امنیتی در مورد چگونگی مقابله با تهدیدات ناشی از پهپاد‌های حزب‌الله گفتگو می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/alonews/119746" target="_blank">📅 17:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119745">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SexdJy0pS3Ot71Gm6XKjWHSPnxEsMI0DBaq-eW-Ry42vesJxiH4FebQlPMUgbNxhwWn5BjriW3bhpmx5RfXYL7MPTyf5FGGtzzuWmi4QkmqOKNVAS6aDgAAPlGGsRlTKl5r-ACiqTKX1djkuQHwRzMmLYbywgkY01bk4hqSM91FT3nBgdK8i8MpguPPmr8d6JecJmDOgGVfRuNljVC2yidwgySC-P8AfaC_WR0xpOCsqhIrjwEp_hcU4RtHaXu0EbL-HE8zdQNA6yTWp7iCs7zLKiX_IPBy1Y5_P-guj92TnVah-jFRFDyh3OJ1gIGhPjk23Is_-5udE7MqGr0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس منتشر شده توسط سنتکام از یک جنگنده F-35A نیروی هوایی ایالات متحده در حالی که در آب های منطقه ای نزدیک تنگه هرمز گشت می زند.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/alonews/119745" target="_blank">📅 17:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119744">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5116963d4b.mp4?token=VuADuCvQDEX2y9ENDVlNlCR-PgChxZfGMEuP5FqRf9ymay6atbmXcxtidmmyH1Lo45BF8dzrjkn3V_fxH0QBGWQ55XFW8MYyalbu-xiTMQNSPgVSWHv4mL-u8bswmIhz3h0IAJSPxyG22a3wurvs9WtuEs7QZw8sqXB51elQkuZn3moVfxtlZR5EdlsgRiJ9zaMBiyVEU19ucMI2D1mVGoKtq6eAEe8MRqSAocY_c22C_qojr1I13ZwwqZEq3q73tb8FX8lm1Z3XpfzKtWZ-wcZvwLH9PaDeCJwUWHQKPYSRvB35CV1wIQOhxC5vGJgqcLgnaf2uQwhV8WlzMOORAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5116963d4b.mp4?token=VuADuCvQDEX2y9ENDVlNlCR-PgChxZfGMEuP5FqRf9ymay6atbmXcxtidmmyH1Lo45BF8dzrjkn3V_fxH0QBGWQ55XFW8MYyalbu-xiTMQNSPgVSWHv4mL-u8bswmIhz3h0IAJSPxyG22a3wurvs9WtuEs7QZw8sqXB51elQkuZn3moVfxtlZR5EdlsgRiJ9zaMBiyVEU19ucMI2D1mVGoKtq6eAEe8MRqSAocY_c22C_qojr1I13ZwwqZEq3q73tb8FX8lm1Z3XpfzKtWZ-wcZvwLH9PaDeCJwUWHQKPYSRvB35CV1wIQOhxC5vGJgqcLgnaf2uQwhV8WlzMOORAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به جنوب لبنان همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/alonews/119744" target="_blank">📅 16:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119743">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea1c5ae6b.mp4?token=dGWGtSFInapJD-XqqExPMVxT6o-FhL34OzDU1ORhf3LJGcvMqYXNEqw6B1Qw1L-wzp5dy-5v9Y8xlyW3X3bVLwE4gdzp5kvvJwnYwEmJuDgi0OHStURxpFVJA17uIqAKHWVvFquIBFeaVWaZiliUU_2QVHcFjiM1y5UEo_Z4JyebxCLSD5C1ba6KNpwphAbt-tUL8VVK_ot8a1twyZagoOQd6UR4jay7jbB6a_4z_XgPrEjl8o2fr1Ud32B4V6g6rjvC0XVyQFAsUTnJfoBBTd0ERqxpU8JdTgS8ET09q7KZMnGSOr-WYj6L8tHHEIJNqECYTeT1JjPhYWPaOfaW5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea1c5ae6b.mp4?token=dGWGtSFInapJD-XqqExPMVxT6o-FhL34OzDU1ORhf3LJGcvMqYXNEqw6B1Qw1L-wzp5dy-5v9Y8xlyW3X3bVLwE4gdzp5kvvJwnYwEmJuDgi0OHStURxpFVJA17uIqAKHWVvFquIBFeaVWaZiliUU_2QVHcFjiM1y5UEo_Z4JyebxCLSD5C1ba6KNpwphAbt-tUL8VVK_ot8a1twyZagoOQd6UR4jay7jbB6a_4z_XgPrEjl8o2fr1Ud32B4V6g6rjvC0XVyQFAsUTnJfoBBTd0ERqxpU8JdTgS8ET09q7KZMnGSOr-WYj6L8tHHEIJNqECYTeT1JjPhYWPaOfaW5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌ای دیگر از حملات دقایقی قبل به لبنان
✅
@AloNews
خبر جنگ‌‌</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/alonews/119743" target="_blank">📅 16:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119741">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uut7ZdMSlCwmdQ1pu_2NVc2atR3LAZOAunf_MHmgJJDLn5Oo6dK13B-IlaA7qsi7dQ48u5unUrX-yYPTZ94pPRun1PsMnBiKW1naEAp_yBkvT1pcM-CTPP54HHIB-XrrEbRVz2R3KFsL64yCUFnET963sx-bEzUf4pvj7Og4PouW6RbH8bMIRtfNhL_7wR0zvDc-XIlGQ5FjMJQSxQhETpg2GpLk-AU7LHYDphBgxOckIY905VpkUN10SZ7X2QdaevldXV-apvWvcM9rnn1FzF5v_CjN2t6hkUomgoeBYIkiKaU_BT6-kevByo9hbx6_l5tN-a7om7jvczVeS1riwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gDThbu1nDpIA1yG_spPnIjlMZBrdx9WxfsBLQtD7hFFXxlcptyEDiToXUHui3tKLq8WLyth7LVIYAIdVNRfRbDYyIAhCSvqLGbxT9lJxvIWlrN8sLSoleTJDgA8ohmWzUoFPwV77_EhseyFgquAIUndTCcKGAT-6nVaixFv8KWAqYH0h1BRpU58mLbmDgn7XDs41nlOyWvgxrGH_RCxyccsdTjMmFJmxjhNjDL83af100Ou517YdEHcUDt-bauel5aFJ6LDDor8JAE5CyBrC_K0BmEsalxj7uF1-OcFYEtVxpIrQil2jyr6eiGg31nfQgTO8bhTg-MkmlccTpipwgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات دقایقی قبل اسرائیل به لبنان.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/alonews/119741" target="_blank">📅 16:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119737">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd9109b4be.mp4?token=nGI5ZJ3YaqtEgalDKwy9Pka8Z59QstRhxUNCQpwFwaZlpfBFsnwi75b3qxTjY8dUUapNFXsI5Bt-bw714dk80mQcCvjLvhQaWnuRDppdvyl6ayfIwBetWsUypnLqaNZUEiTREvEI5MpmwqDH2Nz7hXeuB9gi17B_QHXW7FibqIQOZX2r8C1pfvXdFqDTGzLxl-Az1yNzq9PI21RzW7E7K44K-XqzozkJ-RkVEPnJsjMduuhG1WeB-vfe8yMnJz3OZoh4DwuCGBfHw31ZrGnWTPRUELFcEE_DfcgMwvRHY8w88Vd5VbLiikfiKo5aStxGhoZ68TWxs9_Szd1Mj6IOEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd9109b4be.mp4?token=nGI5ZJ3YaqtEgalDKwy9Pka8Z59QstRhxUNCQpwFwaZlpfBFsnwi75b3qxTjY8dUUapNFXsI5Bt-bw714dk80mQcCvjLvhQaWnuRDppdvyl6ayfIwBetWsUypnLqaNZUEiTREvEI5MpmwqDH2Nz7hXeuB9gi17B_QHXW7FibqIQOZX2r8C1pfvXdFqDTGzLxl-Az1yNzq9PI21RzW7E7K44K-XqzozkJ-RkVEPnJsjMduuhG1WeB-vfe8yMnJz3OZoh4DwuCGBfHw31ZrGnWTPRUELFcEE_DfcgMwvRHY8w88Vd5VbLiikfiKo5aStxGhoZ68TWxs9_Szd1Mj6IOEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/alonews/119737" target="_blank">📅 16:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119736">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزارت بهداشت لبنان: از دوم مارس تاکنون، 2896 کشته و 8824 زخمی داشته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/alonews/119736" target="_blank">📅 16:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119734">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YgEfcsnHr5QYp8imd7fi-YFrg9cKNVONLz-vKnkg6zLzxdxo9PG2H9elstiF7bh9y7QdNl5KMrsKmpQePn0LSVDrilCXVUPkN6J9gRi4XBUbnYj0qlG-2JK-aw1RrUxFK78Kb1R8a02NAmIG_J0G_qtZJSG68MM4hl9jjmySxBFpqH7GXK1FRBRyy_q7E49ESrAk5TmUszZyCtQ5M8FXzf5ZOVGL2-H5crnorCj3__bYHejsQ160jYNoUQsOAFh_2W4z4QhA4TaQnbnEcsD6SEgud0ylYs8Ab0iQyKu0RiINR6um2tSroUjlcTquq5X-6pncCLIQxuWoEhJt1xUCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ویدیویی از حمله پهپادهای FPV حزب‌الله به پرتابگرهای گنبد آهنین اسرائیل و خدمه مربوط به آن‌ها
🔴
حزب الله اخیرا با Fpv خسارات زیاده به اسرائیل زده زیرا این ریز پرنده‌ها به سختی رهگیری میشوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/alonews/119734" target="_blank">📅 16:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119733">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بلومبرگ: طبق داده‌های ردیابی کشتی، یک ابرنفت‌کش چینی حامل ۲ میلیون بشکه نفت خام عراق از تنگه هرمز عبور کرده است
🔴
نفت‌کش یوان هوآ هو اکنون در دریای عمان، لنگر انداخته است؛ این سومین عبور شناخته‌شده یک نفت‌کش چینی از این آبراه از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/alonews/119733" target="_blank">📅 16:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119732">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faba46d214.mp4?token=lDHt-p5Bhjnskkc9OidGT5HWKIbFTzzjIxrYmnPIPb_ZSScc2GdO6HbV-_zn0IO8eOBvdcGbuKM1rY6J7LsEUdAcP57NG7UoIOLSXVHo445CZfd60B7BpYOe-grJPdWZl89eHQiDKKRqwuqMJbmfZa6luSlMP-KOXZVWlPePyk3YQwbORpSMvBStowyHmwhHdLdv1irmb-ca78umE6jIElOoEN328dh2R1KMx5EvilBya5j0XrqiSixto1OWVLkM9FvNb52yXaiIPe58aMUR8mS47-1gURgL0xADGvhZeFSXESPgYm3cORqrSNr1dI06-SSmEWGLjGmplZmRV0idPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faba46d214.mp4?token=lDHt-p5Bhjnskkc9OidGT5HWKIbFTzzjIxrYmnPIPb_ZSScc2GdO6HbV-_zn0IO8eOBvdcGbuKM1rY6J7LsEUdAcP57NG7UoIOLSXVHo445CZfd60B7BpYOe-grJPdWZl89eHQiDKKRqwuqMJbmfZa6luSlMP-KOXZVWlPePyk3YQwbORpSMvBStowyHmwhHdLdv1irmb-ca78umE6jIElOoEN328dh2R1KMx5EvilBya5j0XrqiSixto1OWVLkM9FvNb52yXaiIPe58aMUR8mS47-1gURgL0xADGvhZeFSXESPgYm3cORqrSNr1dI06-SSmEWGLjGmplZmRV0idPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدویی دیگر از مراسم استقبال از ترامپ در فرودگاه پکن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/119732" target="_blank">📅 16:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119731">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f225f616.mp4?token=vgbQV6uDIHDvYo4aW5ZXXduY7g63GQC-KTDoLSQFGcPvxW94DXr5gw8ugAsaVOUt1XBMTXhJTe4Ii4qjcZYL3zJbbG81OkDV3Ka6zReCpGDIAOxWZfdqOUDUKc_hKpURlOAyMdUFeAppIb8OaKx7PL3YQbaWTXc2zNZeEUanxBUfMiJGWRMk8gFJm70aQ8u6s8tYKIrljoxQ_kSRbuBGrY0TzHZi97rBYshRbI5mCr5w76rOg88GDg5VBLNsyG-D_AWOlvfDzmwe66mRmtbdenlf42NjGvYjl-xUmOZyLwgv3qecS3p3wzlGOHEg-wpBptbjKfqiUs3lnak2waEOpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f225f616.mp4?token=vgbQV6uDIHDvYo4aW5ZXXduY7g63GQC-KTDoLSQFGcPvxW94DXr5gw8ugAsaVOUt1XBMTXhJTe4Ii4qjcZYL3zJbbG81OkDV3Ka6zReCpGDIAOxWZfdqOUDUKc_hKpURlOAyMdUFeAppIb8OaKx7PL3YQbaWTXc2zNZeEUanxBUfMiJGWRMk8gFJm70aQ8u6s8tYKIrljoxQ_kSRbuBGrY0TzHZi97rBYshRbI5mCr5w76rOg88GDg5VBLNsyG-D_AWOlvfDzmwe66mRmtbdenlf42NjGvYjl-xUmOZyLwgv3qecS3p3wzlGOHEg-wpBptbjKfqiUs3lnak2waEOpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال از ترامپ در پکن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/119731" target="_blank">📅 16:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119730">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjqGiUDD2Rv83hjQehVbqfFYxW2Gg4Eunu_qM5mQ7M_I3OvOHdYdDwtD-_swD0azdHhJWOBKVTWlusg725oM0LwBNynjg3wSNFvVBvEBKfV-_FObpj4DpN03w0gbsIBZr6ly6_jy0nJ-WRphquGs6ix7VMZ6mTgW9hzS0snS26S626CEmLng__Qa6WtLLJQcMECvU2KN0qKkrh79U2YvDvnmS7m9dp45rVts9PaMomLIWbtsqo6VgtoEbs_cGsn60Sy3RMvfqeoFHn9wPheLo6YhU-w3gU5ZMHK2g160klvhtdg1sqHSZ38DIupFm7qAS70t2Eji3QcAN7ALhJGYgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پالایشگاه راس‌التنوره عربستان بعد از حملات ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/119730" target="_blank">📅 16:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119728">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9SZvGGwKVbDIMqBhEuHJJvja0tuwvFnxotzQhI-_WioqWvmTrkWk7MoZ-JfyPZk0PoPCNQXuQYWspMEPNiEfCOV9pHYty0J9gU-EfKWcovcV4lRGbe645w2W9DX9Z3V6bkqmdlBR9SKwv7Yjz4RZyBQUAs4xgURrGa5Fy3yRuBk1vv8_0yPtPZWEXdvSZbs6piJASFu8HsWuTucCqaULNxm6pIhIuMS-1_5AbcJKeZoX-e_s1wN--blyot4acvrT1VPuddiP8iFvReyyEz2NFlsDmZ7PtaocfG2p6K1cKJvkDv1q1g2y_mIFI3V6RzBnFIPYPndkLDSU4f0kVz5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفر عراقچی به هند
🔴
عراقچی  برای شرکت در نشست وزرای امور خارجه کشورهای عضو بریکس، عازم دهلی نو پایتخت هند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/alonews/119728" target="_blank">📅 16:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119727">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTjlbJQwRF4Ar0v765AtHMHWImM52TEWrRtkD3IE00lR_sFWAhEr6QsDiZO6xjUc0ftYs0TVty68Ib09a0ifqDsb5c3nX53YPTwAUSjwqq5aPU53YsvPnAt-ggv3BTdWC3Bnt9J5LJK6hO4jjYUERiQYT6XNe7HDSE4HR4H3nNuwLHKhWJfOVnpm76b70wOYyPJ8QPl_0z5qCHgnwuXSUf6WDsZnskkS_PEk4lVdRKRrSfr6k9DM-OoTcRjLZdqQH0BnAjou3JI25WnV0tb1a1NSLmkW4NMScjwTQqL7y4ZK0J9ADpn6VqjI18V1SdsapzEZqTTK-LMOEbqb7XuiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نسرین ستوده آزاد شد
🔴
نسرین ستوده، وکیل دادگستری و فعال حقوق بشر ساعاتی پیش با قرار کفالت از زندان تهران بزرگ آزاد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/alonews/119727" target="_blank">📅 16:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119726">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSqkcVz3ZQTWi-PYQ6DpMsPWHb9q7CNIxdcxsm60npojxjAeBruRJJqirCXlp18Ss4-ain-wggPufg2VEG4D_GROft5WDK2qyFNTBCxiQ6C7G21jEHpWttoLQ4ih2kC44KwyqZC9YKQ2OaXPK8eBaKb37JXQ7Jv56tbgmxnyfD-IkQl3VlFg85JKF-c0YhGMQQV7fmkuzds9MbZypvobKngLqaHSSsz18e568KxebTiKsfJ7HMSRx87SE6pvASLRjH0w41J5-AjC7rE0iD_iLnGmo76xfoCKoP_KZRiOfMwWW8Jkgsy0N4hgo9BMJapTYkzd_IKMNNKXzgXUDOVs1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇸
تشکر فدراسیون فوتبال فلسطین از لامین یامال درپی برافراشتن پرچم این کشور در جشن قهرمانی بارسلونا
@AloSport</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/119726" target="_blank">📅 16:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119725">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
عراقچی  برای شرکت در نشست وزرای امور خارجه کشورهای عضو بریکس، عازم دهلی نو پایتخت هند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/119725" target="_blank">📅 16:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119724">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ پس از ورودش هیچ مراسم عمومی دیگری ندارد، اما قرار است روزهای پنجشنبه و جمعه چندین بار با رئیس جمهور شی جین پینگ دیدار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/119724" target="_blank">📅 16:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119723">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزارت بهداشت لبنان: از دوم مارس تاکنون، 2896 کشته و 8824 زخمی داشته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/119723" target="_blank">📅 16:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119722">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7CiRp4QHU_ucBcvD-Le1ZCCJrWCDygsxzSsk2wmtHL3xPZRFD38zwWesMlCXoOaVrLv7aU-IgkdZqkSFhkgM-XuvEZlXfYd8FCOaDLJU7TTqcvE7viywSU3zt44G_vzfST_1C9VuNnrUfwELqcV9TlMQ_vKiHRO10P4TxjQb_UDZ05BukxhXkqTTV3CdILaLLOVK3S9VyP4fcxcA6naV-FvR9ITHQnHUWIH5rRQu5oF2m9vlt2vnBDzVZkxl-Lys2GXLRwLeaH0CtMTia0EkPIpNtohbT9Ahmh_daAcoGmgf_Ei_oh8zHUWBGhc6MlNCa8flBLYT79SdOPQx82ukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین عکس از محسن جبارزاده، ۴۱ ساله و متاهل در محله سلسبیل که در 18 دی عازم رزم با دژخیمان و ضحاکان روزگار ما بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/alonews/119722" target="_blank">📅 16:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119721">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
علاءالدین بروجردی، عضو کمیسیون امنیت ملی مجلس: آمریکا باید این واقعیت‌ را بپذیرد که ما به هیچ‌ وجه دستاورد تنگه هرمز را از دست نخواهیم داد و به هیچ‌ وجه وارد بحث مذاکره درباره غنی‌سازی هسته‌ای نخواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/alonews/119721" target="_blank">📅 16:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119720">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE5-nNIxhbo4SZ-o3Xfxi8qYzkpZARAUlQzRWgCf0eUI8w41bH8hHsX9LbO0twjdcbbleNATwj24r98mahdCzWMX9xP59A8nZG5Pwlfw5IPs73-voYjRCk9v2mWXQRUx6gs5HiltEgZgbvT2A1GHgJD4rJbMRKoXt1hUZGsllbYESPWqhdOxhANoRmtaqEVOj2-NvblYAzSUkBZ4IjIifpgvryetKbBWPLaGYMfNEH5LGmUvoTXviqkfRQDvn-XU_yLROKAXYqXelXe6fC5D7iN3TMMZuSjcfv5ZFqptSHTZSzOcINVQrSfRijnXEuOJdcJWhSpByi495vtzstCZtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امارات در حال نصب شبکه‌های بزرگ ضد پهپادی فلزی در اطراف محل‌های تولید و ذخایر نفتی اطراف فرودگاه دبی است تا در برابر حملات پهپاد انتحاری آسیب کمتری به آنها برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/119720" target="_blank">📅 16:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119719">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
این وسط تعرفه پیامک‌ فارسی و انگلیسی هم گران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/119719" target="_blank">📅 15:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119718">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نسرین ستوده، وکیل دادگستری ساعاتی پیش با قرار کفالت از زندان تهران بزرگ آزاد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/119718" target="_blank">📅 15:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119717">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d281fea04a.mp4?token=aHSoUvptJ_UVgHZS5dIynAqcSyFJBqI3kKkYDXhFdp_0QbZ68zKMfpM-f5-JRJ6AOmes5DwMTY7mp8iP7rp88TYL00j18Z3mQ6oPfYOIhcP3HvyrsVPR3RFMgwWIpkw9z92l1LBdLZUHkMGwi_6STxZ6Wcn9yRdFELdkNIIKtkYR9S28UbTHXYpOgeEY3Caf59-34xNheaEwDefKQRUYm3whlvRdKcojhMdRwVSsimzEo5H_-35cdX-2KQjCfAwMyrKE-b0r_hzMngTG1HkiIMaQSkwZYQOYpWetBavvn-ERBj1-lRZzwGai-A1CcsVvPLETx9I6SsgRfpB-3fdsn60GxIQsGeg94rPMZWqgYQ4DtgCfUcnlr4UYSz7GVFvvCmIIR4873YELO44y7ZczRPhRVKSaV9no9x-l-3VcBEhiaI4Zw_xKcuifwwz9z2DbO0xcVovh8xGJkEHtYkmhZ5LN9jv1OvAWrjklzq6C27HxSw_6EvMdkJBA6I-T-0lBGxubE07ThJvkTSSIwDz0fShm1Bdd2m2SDThqBY27dNa12iTgRNQla1xqWd_L6HDTIpp_do_xt1xX0oL6hA10B-kUAisFmTCmxDM7N-vC6NNKjmJzydf_9Y0vHQpxjm8fpiwFi-8P0lqZtgPSeBkKR2S3e68aLfU930M6wEeSCII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d281fea04a.mp4?token=aHSoUvptJ_UVgHZS5dIynAqcSyFJBqI3kKkYDXhFdp_0QbZ68zKMfpM-f5-JRJ6AOmes5DwMTY7mp8iP7rp88TYL00j18Z3mQ6oPfYOIhcP3HvyrsVPR3RFMgwWIpkw9z92l1LBdLZUHkMGwi_6STxZ6Wcn9yRdFELdkNIIKtkYR9S28UbTHXYpOgeEY3Caf59-34xNheaEwDefKQRUYm3whlvRdKcojhMdRwVSsimzEo5H_-35cdX-2KQjCfAwMyrKE-b0r_hzMngTG1HkiIMaQSkwZYQOYpWetBavvn-ERBj1-lRZzwGai-A1CcsVvPLETx9I6SsgRfpB-3fdsn60GxIQsGeg94rPMZWqgYQ4DtgCfUcnlr4UYSz7GVFvvCmIIR4873YELO44y7ZczRPhRVKSaV9no9x-l-3VcBEhiaI4Zw_xKcuifwwz9z2DbO0xcVovh8xGJkEHtYkmhZ5LN9jv1OvAWrjklzq6C27HxSw_6EvMdkJBA6I-T-0lBGxubE07ThJvkTSSIwDz0fShm1Bdd2m2SDThqBY27dNa12iTgRNQla1xqWd_L6HDTIpp_do_xt1xX0oL6hA10B-kUAisFmTCmxDM7N-vC6NNKjmJzydf_9Y0vHQpxjm8fpiwFi-8P0lqZtgPSeBkKR2S3e68aLfU930M6wEeSCII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیرعامل انویدیا جنسن هوانگ و ایلان ماسک در حال همراهی رئیس‌جمهور ترامپ در پکن دیده می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/119717" target="_blank">📅 15:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119716">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
میدل ایست نیوز : یک نفتکش حامل گاز مایع که پیش‌تر محموله‌هایی از ایران را جابه‌جا کرده بود، از خط محاصره‌ نیروی دریایی امریکا عبور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/119716" target="_blank">📅 15:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119715">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رویترز: پاکستان و عراق از ایران مجوز ویژه دریافت کردند
🔴
به گفته پنج منبع آگاه، عراق و پاکستان هر دو با ایران برای حمل نفت و گاز طبیعی مایع از خلیج‌فارس قرارداد بسته‌اند که نشان‌دهنده توانایی تهران در کنترل جریان انرژی از طریق تنگه هرمز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/119715" target="_blank">📅 15:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119714">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
بلومبرگ: صادرات نفت ایران از جزیره خارک برای اولین بار از زمان شروع جنگ متوقف شده است و تصاویر ماهواره‌ای نشان می‌دهد که مخازن ذخیره‌سازی نفت تقریباً به ظرفیت کامل خود رسیده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/119714" target="_blank">📅 15:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119713">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ به پکن رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/119713" target="_blank">📅 15:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119712">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سوریه به‌طور رسمی خواستار استرداد بشار اسد از روسیه شده است تا او برای پاسخ‌گویی به اتهامات جنایات جنگی محاکمه شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119712" target="_blank">📅 15:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119711">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
حزب‌الله فیلمی از برخورد مستقیم یک پهپاد FPV با بولدوزر کاترپیلار D9 ارتش اسرائیل در ناقوره، جنوب لبنان، در تاریخ ۱۱ مه منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/119711" target="_blank">📅 15:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119710">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
لهستان : به خاطر حملات روسیه به اوکراین، جنگنده‌هامون رو به پرواز درآوردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/119710" target="_blank">📅 15:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119709">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ارتش اسرائیل از صبح تا کنون ۷ خودرو را در مناطق مختلف لبنان بمباران کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119709" target="_blank">📅 15:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119708">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ac712632.mp4?token=S4-PU84vJJHWEDrmuDK8pPTPmC0VAZkah4WeJCXvS76agq9bxBVveDV6ZV24KWCNI-WrVi7u6jY73oTYAy97dVlDcrLDi5wA0xiWGdrvnatx0hak1CyIkER-9t3kiuBA1-j5wMtY07lJ8xgH5Wz5VDSJKQtDkHR2OrPNY20jGpUrgCILJQ0h1zpS2DRDnEGgBl4URiyDXFQ1QCxXy4p2RrMcd1XroA0UUOSt-j8iRTzPBTAu_v2pidLnUd_m6o-MVnQvBdVFaXzM7sV-WpQ1y76Dxfn3QTWAH3ZWkCvqThDsNxWGbCVwkjxMGpiIqpjRAIJMatt8hkiN9keKFd0aww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ac712632.mp4?token=S4-PU84vJJHWEDrmuDK8pPTPmC0VAZkah4WeJCXvS76agq9bxBVveDV6ZV24KWCNI-WrVi7u6jY73oTYAy97dVlDcrLDi5wA0xiWGdrvnatx0hak1CyIkER-9t3kiuBA1-j5wMtY07lJ8xgH5Wz5VDSJKQtDkHR2OrPNY20jGpUrgCILJQ0h1zpS2DRDnEGgBl4URiyDXFQ1QCxXy4p2RrMcd1XroA0UUOSt-j8iRTzPBTAu_v2pidLnUd_m6o-MVnQvBdVFaXzM7sV-WpQ1y76Dxfn3QTWAH3ZWkCvqThDsNxWGbCVwkjxMGpiIqpjRAIJMatt8hkiN9keKFd0aww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دولت چین اتوبان رو برای عبور کاروان ترامپ آماده کرده؛ دو طرف مسیر پر از پرچم‌های آمریکا دیده میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/119708" target="_blank">📅 14:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119707">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
پزشکیان خطاب به کارکنان وزارت جهاد کشاورزی: می‌خواهم تمام توانشان را برای کنترل قیمت‌ها به‌کار ببندند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/119707" target="_blank">📅 14:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119706">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
برآورد می‌شود که در کف اقیانوس‌ها ۱۱۳ میلیون بشکه نفت در داخل کشتی‌هایی که در طول جنگ جهانی دوم غرق شده‌اند، وجود دارد.
🔴
این میزان تقریباً معادل حجم تولید روزانه نفت در جهان در حال حاضر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119706" target="_blank">📅 14:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119705">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مدیرعامل بانک مسکن: وام مسکن را به ۱.۲ میلیارد تومان افزایش می‌دهیم با اقساط بازپرداخت ماهی ۳۰ میلیون تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119705" target="_blank">📅 14:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119704">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4vzjSIPCl2m9mdB4yRKEORvolRTkCODUdsUZwdWKyZAk5mDZ6WXq99Mf_2ugBvjorCqDQMQjzEa0M0COq7q5dSayLsIRX_ZpUqLTPXrfh0I6opkGrsQGYNBuGgh8ru8MN51ATyGOQoht3ZF_tdLaFHyNNN2I3nahchgsAsRI7oyQgUsQvPuzKGv3ECvzWLpTVHYEJoRHgr9d1fzXVxGtzfYdFgl0AxmsZyGLCoi-xsP31u_mK4XmhiQuyffkIocFJYBywR8oPQKt2WTZiokLtkk2fPSxJTZFVuy__5bsi6iXlHrw0iYGPOgjzq1zmddpErfeRVFqAWLkm5O8cj-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/119704" target="_blank">📅 14:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119703">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
همزمان با کاهش درآمدهای نفتی و افزایش شدید هزینه های نظامی و اقتصادی عربستان سعودی، کسری بودجه این رژیم رکورد هشت ساله را شکست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119703" target="_blank">📅 14:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119702">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVhurP1gzNSw_1JzcuRDMJLiY4DhpAOXcCFxg4BN59nZ-ebcmRPV05psv4dmSxp12DiK2Lb_04Z8pM3uxmeTTzXIJgaLrzdwo95sS0WI1LAPQmfaChTGYKkzH4e8311V-TKfQwZc8VOOw6To3LL-ToZ8mZPSZrC37dZRU6gwIMMKMnuueBkcy-38o93TVMmUKbKgM3SoEo65LfLF43XGZ-E3d5tv5cNsTZgk1i8AUCDldczuazVlCP74bcnLPsb8T4FGWT8AF_p7unUwCuK4SWk3TkYbiyYd_k0zMawX-08mRadUCT9sHURjUnZZ0ueX9V2c5a_d8pmWz9ZzTEzaOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذوق‌زدگی معاون جبلی از حکم عجیب دادگاه علیه آپارات: از رهنمودهای شما برای صدور این رای بی‌نظیر قدردانی می‌شود!
🔴
این نامه در شبکه‌های اجتماعی منتشر شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/119702" target="_blank">📅 14:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119701">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa10db56c.mp4?token=et5WkJm-LOdHwKZa44QsV6YM1hPtftStf66gGynk9X8jKKeXQMqB-0oU5r0eYNOIJS-h1K1wZsKeMWEozO8P-wXV87WVAhW2QWBPozy1GMa-y-1ZUvRQUEksr_6mvZIzBheBwAao84IEwAo8WD4wLKxnxG2DMTmi0vjS0K7OSehvrUVR9cQ59TQkbFo47jqI4X5oGjaUwKQYHgA--sKf1fYMdAT8l0K3G9RZcixjG1ZgxHND2jBpB64c6ICGGCbS0raxSzq1aXx5Ik4SyXOHTZeoi7xaYnlO1dkoy5COv7R4e_pPDDQ58CxRo5I6ZBeir88aq-rQqP-kISishMpNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa10db56c.mp4?token=et5WkJm-LOdHwKZa44QsV6YM1hPtftStf66gGynk9X8jKKeXQMqB-0oU5r0eYNOIJS-h1K1wZsKeMWEozO8P-wXV87WVAhW2QWBPozy1GMa-y-1ZUvRQUEksr_6mvZIzBheBwAao84IEwAo8WD4wLKxnxG2DMTmi0vjS0K7OSehvrUVR9cQ59TQkbFo47jqI4X5oGjaUwKQYHgA--sKf1fYMdAT8l0K3G9RZcixjG1ZgxHND2jBpB64c6ICGGCbS0raxSzq1aXx5Ik4SyXOHTZeoi7xaYnlO1dkoy5COv7R4e_pPDDQ58CxRo5I6ZBeir88aq-rQqP-kISishMpNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رانت و خرید مدرک اینقدر فاجعه آمیز شده که طرف که مدعیه دانشجوست نمی دونه کدوم دانشگاه دانشجوس !
🔴
در واقع نمی دونه از کدوم دانشگاه قراره بهش مدرک بدن!
مجری حکومتی: درس می‌خونی؟
ـ امیرحسین محمودی بازیکن تیم حکومتی فوتبال جمهوری اسلامی: بله
مجری حکومتی: چه رشته‌ای؟
- دانشجوی تربیت بدنی هستم.
مجری حکومتی: کدوم دانشگاه؟
- حضور ذهن ندارم!!!
@AloSport</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119701" target="_blank">📅 14:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119700">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گاردین: «اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم اعراب از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی از خصومت از سوی ایران ایجاد کند که روابط دیپلماتیک ظریف کشورهای حاشیهٔ خلیج فارس را تهدید نماید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119700" target="_blank">📅 14:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119699">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
بیش از ۱۵۰۰ کشتی خارجی در دو سوی تنگهٔ هرمز منتظر دریافت مجوز از سوی جمهوری اسلامی ایران برای عبور هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119699" target="_blank">📅 14:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119698">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فرماندهی مرکزی ارتش آمریکا (سنتکام) اعلام کرد همچنان به اعمال محاصره علیه کشتی‌هایی که به داخل ایران وارد می‌شوند یا از آنها خارج می‌شوند، ادامه می‌دهند.
🔴
سنتکام مدعی شد که در جریان این عملیات، مسیر ۶۵ کشتی تجاری را تغییر داده و چهار کشتی دیگر را از کار انداخته‌است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119698" target="_blank">📅 14:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119697">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNmVwtbcNPTj4N9RRPL_Ng5y7d99PvtuV07kx7LIS6IbpeFzNs0dQ48SGzijrPVLoB7SaYAZxBw3AFWDC2gnHe44yFUft5rV_c7cs_murwcrgnLtY4gdk9LLti3wiPr8BBpMPtEaF4mOvwx-F6N6UDiu4U0RhuHLdOOVmxDqJq8T8Df_uSpgKUuOE-ODDO5G8YiPUTS-_UXfUqEz1EEnPY3IDPIBcfmvd3js1z_FRQ9nB7JyeG8h-xNNX4PH8dQcq55YLCMHHJe7-_Qd328CY2eG4LAZK_2wur0G5piQpjD_MK75verfV-ztyFlLjil9tYC7jRGvkLDHnH9xYEYy3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت ایلان ماسک داخل ایکس : تو راه پکن با هواپیمای ایرفورس وان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/119697" target="_blank">📅 14:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119696">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی مجلس: ایران با وجود ۱۵ همسایه عملاً محاصره ناپذیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119696" target="_blank">📅 13:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119695">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رئیس موساد، دیوید بارنیا، حداقل دو بار در طول جنگ به امارات متحده عربی سفر کرد تا هماهنگی کمپین علیه ایران را انجام دهد، طبق گزارش وال استریت ژورنال.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119695" target="_blank">📅 13:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119694">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: احتمالاً سرپرست فعلی وزارت دفاع برای تصدی وزارتخانه معرفی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119694" target="_blank">📅 13:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119693">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان: پیش‌بینی می‌شود ترامپ از رئیس‌جمهور چین بخواهد تا بر ایران فشار آورد تا تنگهٔ هرمز را بازگشایی کند و با یک توافق صلح مناسب موافقت نماید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119693" target="_blank">📅 13:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119692">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
بهداشت لبنان: 8 کشته در حملات به بیروت و صیدا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119692" target="_blank">📅 13:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119691">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رییس سازمان ملی تعلیم و تربیت کودک: کودکستان‌ها فعلا باز نمی‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119691" target="_blank">📅 13:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119690">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119690" target="_blank">📅 13:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119689">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر دفاع ایتالیا : قراره خودروهای مین‌روب به منطقه خلیج فارس بفرستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/119689" target="_blank">📅 13:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
شهباز شریف به روسیه سفر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119688" target="_blank">📅 13:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما آماده بودیم روی نوعی تفاهم‌نامه توافق کنیم تا این اصول که مبتنی بر حقوق بین‌الملل و منشور سازمان ملل هستند، به‌صورت مکتوب ثبت شوند و هیچ‌کس نمی‌تواند اهمیت و صحت چنین اصولی را زیر سؤال ببرد.
🔴
پس از آن در ۳۰ روز بعدی، که البته قابل تمدید هم بود، قرار بود درباره جزئیات هر توافق احتمالی صحبت کنیم. بنابراین این چارچوب کلی ماجرا بود و باید ببینیم گام بعدی چه خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119687" target="_blank">📅 13:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c21f4b9c98.mp4?token=tncLLOAKviLWLGq0qmVZTf8a7tEX13ywg3L9hFVeXfj5TykQDZGQroP9hzpQ-1NPwQsgBJ-X60dNH5ME_uBfz-LEW_WMGg8bFb3jyZRRAxdp-U0HIUSaiMrrHMo09CtF7W1p3X_70ViOlxaryOb2sUNrJBqPW6yL-rZsNGskiVNhgiIcxWGZVu63s8arHYCw7MPpRyyUX4w6YEXrquw3kIa_kMZtOTFbfvlNighztydijHnKW1bMzWP5Mhbmlt4W8QlbhDfqQg3hNnGNOgFIAKNXfrjxcnOW7x8GSF_cj13ClGijS1Ny9UhqdEl_zDTUhSM5R7d2mx4zVfGiTWO9fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c21f4b9c98.mp4?token=tncLLOAKviLWLGq0qmVZTf8a7tEX13ywg3L9hFVeXfj5TykQDZGQroP9hzpQ-1NPwQsgBJ-X60dNH5ME_uBfz-LEW_WMGg8bFb3jyZRRAxdp-U0HIUSaiMrrHMo09CtF7W1p3X_70ViOlxaryOb2sUNrJBqPW6yL-rZsNGskiVNhgiIcxWGZVu63s8arHYCw7MPpRyyUX4w6YEXrquw3kIa_kMZtOTFbfvlNighztydijHnKW1bMzWP5Mhbmlt4W8QlbhDfqQg3hNnGNOgFIAKNXfrjxcnOW7x8GSF_cj13ClGijS1Ny9UhqdEl_zDTUhSM5R7d2mx4zVfGiTWO9fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل به بیش از ۴۰ موضع حزب‌الله تو جنوب لبنان حمله کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119686" target="_blank">📅 13:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119685">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
دیو دی‌کمپ، روزنامه نگار آمریکایی: شاید ظرف یک هفته آینده شاهد بازگشت به عملیات نظامی بزرگ آمریکا علیه ایران باشیم. جنگ تمام نشده است، با وجود آنچه مقامات دولت ترامپ سعی می‌کنند بگویند. منظور من از «بازگشت به جنگ» هم بازگشت به یک جنگ تمام‌عیار در سراسر منطقه است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/119685" target="_blank">📅 13:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119684">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سی‌ان‌ان: هزینه جنگ ایران یک تریلیون دلار است نه ۲۹ میلیارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119684" target="_blank">📅 12:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119683">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سخنگوی کمیسیون فرهنگی مجلس: تعداد کاربران در پیام رسان های داخلی از مرز ۱۰۰ میلیون کاربر عبور کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/119683" target="_blank">📅 12:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بقائی: تا زمانی که عضو ان‌پی‌تی هستیم حق استفاده از انرژی هسته‌ای را داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/119682" target="_blank">📅 12:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نائب رئیس اتحادیه مشاوران املاک تهران در برنامه صداوسیما: وام مسکنی که همین الان در حال ارائه هست آن‌قدر ارزش پایینی دارد که در بعضی از مناطق تهران نمی‌شود با آن یک متر خانه خرید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119681" target="_blank">📅 12:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/razsjHCkt3DOAtCaY_kIFzzZXzJO_pIEqiCyKBy0Fz9OEK76q7hjbFrsEaymYL908pGE68r1lpgQjDF0lXItL6eCTl2bHuc-x-vRgejkcY4BHXHQkrSJsStiMjwC1tksQS9mZx1Yo2c1GoLNmVP6STR1LwrgsliHzcFoY2qmoQUr12I0daRXhMMlEzEdqAyJkhv_0rbXMUl4xaS5xi9vkFQJrcYyton2rhAhYvYuvXEH6d3mAPrRxFHQVwccOKeA_XxmZxGe93IU5IOKhgJZhoS7uIOk97LB2YKqJg1B9y6yX8miaV7TZsXwyFbUrGEz0SQP6ZBrMZ5FCwfCIPFJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تهران تا یک‌شنبه خنک می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119680" target="_blank">📅 12:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119679">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزیر رفاه: داریم تمام وقت تلاش میکنیم که مبلغ کالابرگ رو افزایش بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/119679" target="_blank">📅 12:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119678">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه ایران و جمهوری آذربایجان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119678" target="_blank">📅 12:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119677">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
الشرق الاوسط: چین نام روبیو را تغییر داد تا او بتواند وارد خاک این کشور شود
🔴
مارکو روبیو، وزیر خارجه آمریکا، روز چهارشنبه همراه با دونالد ترامپ، رئیس‌جمهور آمریکا، به پکن سفر خواهد کرد؛ این در حالی است که او همچنان تحت تحریم‌های چین قرار دارد، اما به نظر می‌رسد پکن با تغییر شیوه نگارش نام او، راهکاری جدید برای مواجهه با این موضوع پیدا کرده است.
🔴
روبیو در دوران عضویت خود در سنای آمریکا، از منتقدان سرسخت وضعیت حقوق بشر در چین بود و پکن نیز در واکنش به این موضوع، دو بار علیه او تحریم اعمال کرد؛ اقدامی که آمریکا نیز اغلب علیه رقبای خود به کار می‌برد.
🔴
چین روز سه‌شنبه اعلام کرد که مانع همراهی روبیوی ۵۴ ساله با ترامپ در سفر به چین نخواهد شد. این نخستین سفر روبیو به چین است و همچنین اولین سفر یک رئیس‌ جمهور آمریکا به پکن در حدود یک دهه گذشته محسوب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/119677" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119675">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlLqVwyIOq5Lrj8Ay_4uovsFv85YJ_q4u1zWtkegeElerg1XycSW3qmQXKspTuCUGwG6u7tqS8y1JnM3cOK5GuvBpf0QW6ZzR97OPrFnLnGZMPkWXMdB_s4vYzXLf30PtAszXa1Dmo30gNzxnoZ1vTnI8Lfpv_5FbDVQm76eXqM5mB_IcdYDO-_IpTLdP4_5SNyCxsZDGoo7gkTSGhUGsNFtnVAjd0n57Kk0MqXMYqOPachC14jqiXafSMXJcXlQ09krARIvsMaWImU5bgPUyOSHE55lzMPqYl2rM1zW85YZj5vNTZY09eJapGqm5Tc6yTg1_uqO74HK3nKw1Ns-LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kp2qS8nraJ63o6Glw-zL8wcsWAIPcCupBOK7AzTSsGYNs4mXNWRUtlShV2KpuXLE6YhkmOjmLFqNA7FqmxsRGx6GtZ8S5rsVPAcw_XzriTLRnh3fn2BwqEznz3Eza6z4jXBpX3T5VIymoU5kOyJhZWo9X02Vfwq8dliFVaudrqp30IRAHb8FCFr5dLZSSqu4IGL98scAxhnbCXTHj1QGWhQ_2hYmVRvE9Z1Xga2fWvVrJoLtWxNum1oa_jxF2UlgHZAE-eQxn5svAiw6A6ciLHVZz8Ngtnxax7lyUcR0r0Gy4Bga5Uyt9BLK3CPOVqcqRZzMIMssxhOz2DfodoWfdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله جنگنده‌های اسرائیلی به دو منطقه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/119675" target="_blank">📅 12:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119674">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
الجزیره: وزیر دفاع کره جنوبی اعلام کرد ، حمایت از تلاش‌های آمریکا برای تأمین امنیت هرمز را بررسی می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119674" target="_blank">📅 12:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119673">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سخنگوی شرکت آب و فاضلاب استان تهران: مصرف آب تهران به مرز ۳ میلیارد لیتر در شبانه روز رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119673" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119672">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نیویورک تایمز: قصد ترامپ از تغییر نام عملیات «خشم حماسی» به «چکش سنگین» این است که یک عملیات جدید ۶۰ روزه حمله به ایران شروع کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119672" target="_blank">📅 11:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119671">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: جهان ذخایر نفت خود را با سرعت بی‌سابقه در پرتو جنگ «خاورمیانه» مصرف می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119671" target="_blank">📅 11:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119670">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رویترز: قیمت نفت روز چهارشنبه پس از سه روز افزایش شدید، کاهش یافت، در حالی که قیمت طلا ثابت ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119670" target="_blank">📅 11:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119666">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cRxq1jAEXcQXsqS4QKIdHl7ucLEeXeAj3V0qsFIj05CHY0HaNkqmmUZJRir9jvyd1TQLK0F3n4cjZnyxxdyBAWtfba5k_U4cfrCK1Td6e996kJfu7iGvooKhVi8KVTTSKj1FU71mLlIhcORAR6rB0sZ8R1Ep_2XuBtsKW_-v7kfpgzZZ8gLtQTwqOZJi1jDVmlvgb2O4ZQNSaOiPtfKBlk2nGabedpXIcBzNNQ4J6kM31tgtBZEcvkS8M9m3xObu5YAqZtdOtQ0ntiuyXAHwCHQ3EVVX35OPY--HbM51THDYc8KizrO0_CcwmZMSHw3nZ0YHD7WkF8Rxx7-cdX_Gvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rYZ8aoz7ZFFaq3ePTIaKqMR19c6L3GYgAT1Tyj4hnjsKSLwiW1rblCVz70jkKC1oKd2oGzJvfOjwgXimaWkP4kLz9vjilne9xVMIx6721oLbO8OlA7stnQZLCqYDIP3ZrDq4tldD31vtokPqpB7El6JPFJVPAejiC0qe-4TUql9rIK6JHwp7zL2LCes9tMPAlSalE9sl14QBsCM5ZOGuvJa8m180CE0CgeMM8GX7rLB-qWSdnb-HYge4JGBFEfsR3aXLA4FcoPN1sd0sY4QsO5YnSgTx0Qu-5pr1EpGFLYQK-yMyVzq6GKP9qMAPRgoqJfRPK3cKrOlYx4k0tVsTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PzgGZzX7OAY6FYN7JICHSDrz6ruhoqD0vnbhQJdNPdIwqynAjrdKDzom7htUIIidZfQgRSOxs4aBSQoOayKlqYY3ykBS_xZkLGrJsGcc-F9dmG8jqgLunqXywOR3EcDCv0SDn849R-SGPtFV56R4c8w68ncRK857Yl0J_vSyu_Z3_3Bv4lkTsvmL8b8NfpnaNRwKZI238optW0L5RQW7xNCWJbc31HFNWu99nzFNH3Qng5LqD-cbgac-EueUyOAfel7wsy9RdxF4jUH0JsHW4D8xPWo_EfEMi1LubsV0bn48rXxotVOoEyd_n-tbEI3HZKoENpctFeW2TgCA-aKG0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cTCFGWKhrrzki7Cqy3PMp-PIZQhbkXLo5QSw2ggfEEwz8MQ9PAu3QIXI6lnYXg47CErUcsKzAl0pwwmdXhG_wQQVN169SzY73uC9lzUuXnsKJzBaFdSZRSpTPI4e5bpG3MjjvgnBLMd8Erxkg3tM6IJG4Uwcp_D7FEcEm6-Vhox314Y7GmlXBknb2Yz9X06KV9BAzv_YI5ejNcqtarHhqqaRcBzmJdTHs5Tu9oDWQU1cGoCrbd67dM-bN2Eq-lLbUjqiXuvJ_QSUWbC7u7wEpyrxUd_dIXDDfSA0y5sP8rM0qPE9oyQmc678JKF9RIGfptBjPV65j0ppOnAFx2ptew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
یک اعدام دیگر
🔴
میزان خبرگزاری قوه قضاییه جمهوری اسلامی با انتشار تصاویر بالا نوشت: احسان افرشته اعدام شد
🔴
قوه قضاییه مدعی شده که: افرشته در نپال از سوی موساد آموزش جاسوسی دیده و اطلاعات حساس کشور را به اسرائیل می‌فروخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119666" target="_blank">📅 11:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119665">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
به گزارش رسانه های عبری : نتانیاهو امشب جلسه‌‌ی امنیتی محدود برگزار میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/119665" target="_blank">📅 11:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119664">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رویترز: قیمت نفت روز چهارشنبه پس از سه روز افزایش شدید، کاهش یافت، در حالی که قیمت طلا ثابت ماند، زیرا سرمایه‌گذاران در انتظار نشست مورد انتظار ترامپ و شی جین پینگ، همتای چینی او در پکن، در بحبوحه تنش‌های مداوم مربوط به جنگ در ایران و بسته شدن تنگه هرمز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/119664" target="_blank">📅 11:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f7e26a3b7.mp4?token=Gf21CFFRq1evufanPnhEODjb-NaYB1JvX1YJacDICmW6ITyb7XiGwmEFCooUjO5AWzWuwvkePgX8dAZtonTcQIEDuJ7CGZ1_STIqVdbf0n9EdmwqoJCgG3qk-_TJ_35Rm_TCCIE6Mf5OqaaGFNM_DHWF9p_jvaTMy2cB0exrPbNDryJus2LQJZb3uVoCerItMvQQLhWR8U2YE7Sf3sm0FLC1obgKiexRwS_nMMW1YjG_8qGkJS7kWB7dw90B0u9_uhzl_11fBx3KCYPeH_pGLDro_YzPxXW1cxqTK4ZXXeSFAAP2AjfOXd7t2fVqtDoqDBWR8kJzFLyG_WPJrhqkhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f7e26a3b7.mp4?token=Gf21CFFRq1evufanPnhEODjb-NaYB1JvX1YJacDICmW6ITyb7XiGwmEFCooUjO5AWzWuwvkePgX8dAZtonTcQIEDuJ7CGZ1_STIqVdbf0n9EdmwqoJCgG3qk-_TJ_35Rm_TCCIE6Mf5OqaaGFNM_DHWF9p_jvaTMy2cB0exrPbNDryJus2LQJZb3uVoCerItMvQQLhWR8U2YE7Sf3sm0FLC1obgKiexRwS_nMMW1YjG_8qGkJS7kWB7dw90B0u9_uhzl_11fBx3KCYPeH_pGLDro_YzPxXW1cxqTK4ZXXeSFAAP2AjfOXd7t2fVqtDoqDBWR8kJzFLyG_WPJrhqkhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرودِ هواپیمای ترامپ تو الاسکا برای استراحت و پرواز مجدد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/119663" target="_blank">📅 11:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119662">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
با اعلام قوه قضاییه جمهوری اسلامی، احسان افرشته به اتهام «همکاری با اسرائیل»، بامداد چهارشنبه اعدام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/119662" target="_blank">📅 11:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119661">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بلومبرگ: نرخ بیکاری در فرانسه برای اولین بار در 5 سال گذشته از 8 درصد گذشت.
✅
@AloMews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/119661" target="_blank">📅 10:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119660">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
بلومبرگ: یک نفتکش بزرگ چینی در حال عبور از تنگه هرمز شناسایی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/119660" target="_blank">📅 10:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119659">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iCRQ7yNUq3ZPIv7tM4hDiZVx6aIN5WW4Lw9EdWxGlb6RM93BoBwRhupuqH4nl36olh4JZW7WTvuYxSV2cLUNWAfoMqEt_YYJ5nK31nCClJxQANUeUvTJoIJtNa4jiTn9TZuvv57a-FkfUOujeH0AIJu64aYswlMX47ygPsu0zCDAi2oFClaxEATRs6sHIFxk6lCQTpq345g7dgg6o0TqkTp1rJ4cqAGsQWPM8ZkmQV5RVa9MBlzY1t91AWi8oXnmMypMdICKUbKolTjRiFWOxaVT4AvLo5EH-IZTSdecSn-xJSnt4-fqn8_P6ohJWAeq2je3bicgLfh8jWPcFNv_6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تشکر اصناف و اتحادیه‌ها از پزشکیان برای جلوگیری از توقف کسب‌وکارها با اینترنت پرو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/119659" target="_blank">📅 10:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119658">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر اقتصاد: انتقال کریدورها به بنادر شمالی و مرزهای زمینی در دستور کار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/119658" target="_blank">📅 10:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119657">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
المیادین به نقل از لاوروف: روسیه پیشنهاد تهیه پیش نویس بیانیه ای از سوی گروه بریکس در مورد وضعیت تنگه هرمز را ارائه کرد، اما اختلافات ایران و امارات مانع از آن شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/119657" target="_blank">📅 10:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119656">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRXlgfbmTb0AEI4nH-nhHWECqp1D_f5CV8-XjHIvJfgCQIeQALATyatV2JH0eKBxV0dAm9FA2hFR7__DBt3DYBJpjaJcq1jtbHJ8cnrR8I7ChuvP8-6G1Cqet2i8N3cFpAKmOmqYHBXBmIdRt5Xq4EMRAacP5VcRR0IBFZ_2PEc5GNz3W4ntxA7vuKNBN1PkZUag2cScmnhddRJbFeOTDhKsaCI5eoX2lCkb8eknc2p95hMtwOWi6LwJuziIzMbQGWbFqfrWAfuCCBJzijeIwPj5GXsWFr30G93RVwj5cK01B4mj9FsF9zS0vQj4lijnXawyh2j3SYIfcho2xzatpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه NDTV تصاویر ماهواره‌ای با وضوح بالا (تهیه‌شده از شرکت Vantor) منتشر کرده است که به‌نظر می‌رسد گزارش‌ها مبنی بر پناه دادن پاکستان به دست‌کم یک فروند هواپیمای ترابری نظامی C-130H نیروی هوایی ایران در پایگاه هوایی نورخانِ نیروی هوایی پاکستان (PAF) را تأیید می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/119656" target="_blank">📅 10:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119655">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
روزنامه نیویورک تایمز با استناد به ارزیابی‌های اطلاعاتی طبقه‌بندی‌شده آمریکا: ایران به بیشتر سایت‌های موشکی و سکوهای پرتاب خود دسترسی مجدد پیدا کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/119655" target="_blank">📅 10:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKJIdBtI8J_7IqdKINe2e5UVg52BPuE32QjlQnElCX3ggGB0BXrQ0HYooAnm_HBAzGSgPeHi-gK_Xxvax_36jH4M0F6VL0l4qsfOYlAuMraupwph4aeboTiug8IaZMJ7E1P6DILGZ-O-bqlwOurwiwUMUiyCsGh0sR2iGFV-NGbVgkAD96oMAFdYJD01RY5GJO0eK_RfPX7Jgbp0cOZfk8oFTXC_-dnk4jArM2ZC8mONBpnIu-vveESCeA21FOnEBQOf6qaCU1B_16XLBzCfjTG3qrmwpdrbo77Zn_8wYenSR7iH2Bya1y6jHoQmUAezIrGMNNZz7bSi2_hIxm9lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q141jBEWtSJud9c3TgJdlRdNHWcwd2sKKmYyfFkUrZgYTW1N43W1h4xurCoX6KMlnIRC_0p1G2PMj8WqWSSLgF7R5yrCBGUuDejp9PUBPAvLrbK-t1vhMMwtqjUL6TFiidnGA0hQsEsBOuaC7pEr7nHADqlQcsuXIchvhm3SRpoIebx1jZsX-ccEn1rM5lRWvkpOVe1srFU5YkVWoeDrbehjjwOnUaVfTCZD4Aecul_XeeaqA61Kik0MnHLOuDMTGPz6KBA18_3grN8jaSCL7a-OudjvVLagPAmOoi1Bws7yxWw6qghM31v_uK5z1iURdqY-oG1HMIfIK02LQSxWhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مارکو روبیو توی هواپیما برای سفر به چین مشابه ست نایکی رو پوشیده که که مادورو هنگام دستگیری پوشیده بود
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119653" target="_blank">📅 10:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119652">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nak3EhiLMIpgWZ-4LWX0cAFDpRpPaoiJsP98HPVUJvbKTkhHJh_tCG_bGNCNbjIi1cgVuQvZ-AGEiOTkUZqH6ZIrjooEVhtMlUrCDkKd4bNxLOsbzA2CxxjOivMgfhq34Wa7E0WEijbuMr1nCBpT6F0f7jE1tkG8EGcAgLFzCf-tbpft2LHmjq2_OrIO7BqgnOKQ63LmDaakI0uFC1ZRUG6zwgdjtyQCnKzraY0Eu_WJqxvRuUqZmJVGOyPXSFR54p9p8fdngxg0Q4SQgfk61mEBcSM89ilhFhbLrSgYNRSGloAQImwc8xUo02z8UKn7y2MzIFoefi_T8cXvkkxhCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله پهپادی اسرائیل به یک خودرو در جاده ساحلی جنوب بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/119652" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سی‌ان‌ان گزارش داده، یک کشتی باری روسی که دو رآکتور هسته‌ای حمل می‌کرد و احتمال داده می‌شود مقصد آن کره شمالی بوده باشد، در شرایطی نامشخص در سواحل اسپانیا غرق شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/119651" target="_blank">📅 10:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119650">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
دلار هم اکنون 182,000 تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/119650" target="_blank">📅 10:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119649">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
لاوروف: اگر درگیری در تنگه باب المندب رخ دهد، بخش انرژی جهان آسیب زیادی خواهد دید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/119649" target="_blank">📅 10:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در محدوده بهارستان اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/119648" target="_blank">📅 10:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119647">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ژانگ هان‌هویی، سفیر چین در روسیه، اعلام کرد که در 7 آوریل، شورای امنیت سازمان ملل قطعنامه‌ای درباره تأمین امنیت کشتیرانی در تنگه هرمز را به رأی گذاشت.
🔴
چین و روسیه به دلیل نامتعادل بودن سند، به آن رأی منفی (وتو) دادند که از تشدید تنش در منطقه جلوگیری کرد و شرایط مساعدی برای دستیابی به آتش‌بس موقت و آغاز روند مذاکرات فراهم نمود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/119647" target="_blank">📅 10:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119646">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tldv8fo59SONA6Op6SN63QrhJGE663qvrp1XlIeKQnXECbBKYDl5BUpjvy1lwtqyGUxLnvvyvZYkAC9Rh-5gVaZzIcuGOlLFXLinCyKBt6e6gPWBNO9lPcTKtC-F2jR3t4A6XQQOWrHX7O-p02yc_pfrNzMHyO_jP1OB9RIb6BPLUhBdASMm0Rmo0h2mG9AnVifvsK6MBnXrdKTHaxeg0eJUlcMF4NyDYWYcJTiYMIH_pGZznKtMNORSilEZELWUng_owIJ9njKWyH1uc7-82K7hUulyGooXt3NTr0vXYzBxnCACZu4rwpLRMfnmPmdJge4ERADqW3pSxmXOQaCQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ نسخه‌ای از پوستر نمادین جنگ جهانی اول «من تو را برای ارتش ایالات متحده می‌خواهم» اثر جیمز مونتگومری فلاگ را منتشر کرده است که خودش جایگزین او شده است: «من تو را می‌خواهم!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119646" target="_blank">📅 09:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119645">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941b50d546.mp4?token=Qgxa6XqccpkTFJUoT0s6WKrbCcKxvZKp8E8Rs4MeIpmWUZ3yC_Q4E_PpVCnct6fulmtKD0HhiXAsihbsNBdeT6XmhI3_WZ5ffgH0-H6nO_IddMyf_U5O4obJ8G18UW5HhLaEoOxLWsjI4KTOk4vGzpvvsNrAKBboGswmSPWUpLdUGf8q3ZBJvo-vh8EA5hW-OHqyGqhNLXNEco4el9LvhEXipVQcYkQGNMvCvgL5A6Mbu0IJxDDWu2YkIIyA-N4sYAOPpxrp1hZD_SFVAacJ3YpZM15j7iowS5jcsPt5xsMHXRCd-2DQo6KJ2w-jj3WbpkJMzy9zZjWYpSBDHG7GBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941b50d546.mp4?token=Qgxa6XqccpkTFJUoT0s6WKrbCcKxvZKp8E8Rs4MeIpmWUZ3yC_Q4E_PpVCnct6fulmtKD0HhiXAsihbsNBdeT6XmhI3_WZ5ffgH0-H6nO_IddMyf_U5O4obJ8G18UW5HhLaEoOxLWsjI4KTOk4vGzpvvsNrAKBboGswmSPWUpLdUGf8q3ZBJvo-vh8EA5hW-OHqyGqhNLXNEco4el9LvhEXipVQcYkQGNMvCvgL5A6Mbu0IJxDDWu2YkIIyA-N4sYAOPpxrp1hZD_SFVAacJ3YpZM15j7iowS5jcsPt5xsMHXRCd-2DQo6KJ2w-jj3WbpkJMzy9zZjWYpSBDHG7GBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
براثر بارش شدید باران و وقوع سیل در استان سامسون ترکیه حداقل ۱۲ نفر زخمی شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119645" target="_blank">📅 09:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119644">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
احتمال شنیده شدن صداهای شدید انفجار در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/119644" target="_blank">📅 09:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119643">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
الجزیره: ۱۱۲ کشور از قطعنامه آمریکا درباره تنگه هرمز حمایت می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119643" target="_blank">📅 09:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119642">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64e8e7d0d.mp4?token=UqF84YxFXtk-vuTOO6LZWx7_3ace5AseJku3xpmu2mUFZV150UKtAnpVU3yKk7bmJYQgOZ_fByo-sMxJdJimjF8tcFQtmlz6v_cH9IbXhm7-ahxCJNnEGT2MQgeUXTknMQy5a6Uh9IryKFWLeEuA7VFRSczTmRvMrdBvvl8aknwH_D6i3URNs5BUepELGpy4-8cwcPYEgH-_6AzbCAdt0ofhCI43EiqT7VNowpoyQp4CgbB3GM3uIOVoKjvbir62J3zkfXUHS-dMjTco836bKLOgznd1lO3iLVToJM7LYbCAclt_10iGYWRP7zCeCNT2x1N7lTHaTin74YZhVF-fog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64e8e7d0d.mp4?token=UqF84YxFXtk-vuTOO6LZWx7_3ace5AseJku3xpmu2mUFZV150UKtAnpVU3yKk7bmJYQgOZ_fByo-sMxJdJimjF8tcFQtmlz6v_cH9IbXhm7-ahxCJNnEGT2MQgeUXTknMQy5a6Uh9IryKFWLeEuA7VFRSczTmRvMrdBvvl8aknwH_D6i3URNs5BUepELGpy4-8cwcPYEgH-_6AzbCAdt0ofhCI43EiqT7VNowpoyQp4CgbB3GM3uIOVoKjvbir62J3zkfXUHS-dMjTco836bKLOgznd1lO3iLVToJM7LYbCAclt_10iGYWRP7zCeCNT2x1N7lTHaTin74YZhVF-fog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل فیلمی منتشر کرد که در آن نیروهایی که در جنوب خط دفاعی پیشرو فعالیت می‌کردند، یک شبه‌نظامی حزب‌الله را مشاهده کردند که از تجهیزات نظارتی علیه نیروهای اسرائیلی استفاده می‌کرد و طبق بیانیه رسمی ارتش دفاعی اسرائیل، این فرد با آتش تانک هدف قرار گرفته و از بین رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/119642" target="_blank">📅 09:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119641">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQl6Q286MICoPjuUbwHWAfZj_YNZVCG7dzPWZ0Hg3W3NPszMr2CUNvueKXWgNfTrE0d823ti7g6i6FfjI3o1fcyRFMZEdm71hgxuvhnZqDh6BExVNgCZic6xvP28wfYQ3y1uLkc7tPTUevRZU3PVMIPZssVCvVL7DT_YmrNZkfTugB-GYDgXuaHTdPNpVPCinzQ5BiYV9G1V38yD2LcsRv0cG-OvBk4QwupKXndn4K7PkaUJEi0DQ_o6SOykOK_fkH8PqpP9MoshmIvcL0piQrL4JocA9MZfWwQ4ytUnI3Qh7qGvvtcOBzasa3ev09jJqIOiyXrDSYM9nAn3Z7JnTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید در ابتدا فهرست مهمانان رسمی را منتشر کرد که مدیرعامل انویدیا، جنسن هوانگ، در آن نبود، اما طبق گزارش پولیتیکو، رئیس‌جمهور ترامپ در توقف سوخت‌گیری در آلاسکا دعوتی در آخرین لحظه به او داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119641" target="_blank">📅 09:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119640">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb6_1CIuHNcSharyiZ7zZMnRl08avDv1zgw_ycKsf08nXoFjvvMTcN8rf8e4cNr7eATtaIm9e2I5IftLhvqRtEgLXTbb3Y_FHn4EMVANVrh-3zu2lmGpzZWRFsD58a28dUy6XbU49P073T9EIwgtAROFMDA73cCHIJk3hUiLx3nI8RcNBrKdd5oUSAGQIfXGG2Hrhpbk8adZ8DrZbGHs-LjRQ1gKmouW2FtFDqkdtBZKeCpF_6H557GQTXqsVg3g-4gJNl7LD-CNl7ET2jPoyvXupXV_AqC6O1rfPRM47z1vVzd8DRsTSrMxx7aXxCgY_MIC-yEZ6aYfW7RJ8Lw-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی
CIA، لیز لایونز، گزارش سی‌ان‌ان مبنی بر اینکه سیا مستقیماً در ترورهای هدفمند عوامل کارتل‌ها در مکزیک درگیر است را
رد کرد
.
🔴
این گزارش کذب و توهین‌آمیز است و هیچ‌چیز جز یک کمپین روابط عمومی برای کارتل‌ها نیست و جان آمریکایی‌ها را به خطر می‌اندازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119640" target="_blank">📅 09:37 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
