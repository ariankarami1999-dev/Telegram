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
<img src="https://cdn4.telesco.pe/file/CiZGMBNWMltb52ip6FFVQ_MdPlrw446EJCS2fInK8He-cmh35qVVrv5qRFzT8dRUXgf4nxKz5EcQJ942ev-oQpn3Qd67Z9o__p7n5FUUHZ0J50uXGBiufluMo-bYUE1v1Y2DSghfpZIVXEiEU7reW0ukZzq09n34joeapxxJthATJPyvJ235-Wtia9gtDbFLgJhhnRBqsSygkCCFfExnmUtko5yh6YUtffsTQKQeB_UD34qlP_3qG-365qp924abFFBfp0xKrzcweyHx1Od-TEyVY8jDvdbVaVzKME6G4aFrjOkGj23KYzm_hfvWCbNXfSs154KaG3t7d7MC9PGnpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 00:30:37</div>
<hr>

<div class="tg-post" id="msg-25313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlJSqugpUamUCVCBy4iJfw_WkN-XSlwbaU4_lCjtLYh_hC34vKQbTWPuH7vTsUsweWzUmySOr430fwGagOz1p6ItO3tn5Q4XfkEuT4T0K9IJOR4800QyES6CJjrdO0lH9UyV8e17bW0ctmDGbNVwjawc9OQGVd9avvgAF3ebUAMQK0o3SGjZHLbzQSFaKYy14ie7aBtHkZqk3y0LNi_qYvexJiv9JUNe1pJeasc3TK4kgM7v-NCz31-eAIVcSaxs58tDDZ5JE_6KkUFpzF1TRmYlwxTeTdpOy1NnUKQ9okc3uv1a845XNhmEfNo36xtyBRYNcKBV5_MVwjvWhK9hdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/persiana_Soccer/25313" target="_blank">📅 00:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwsQQdTyPzE-PN1-cnwCJjcFSIl1nBSZkfL2cJ1y82E2IYXH6e6Yma1C7M8C6H4KvNvw-AEhNCOvzjlR6ZSAP3gGGz_4ALA251vUegacMmkuWHjcjCi1MwtRvEBqSevhEwBkSVjiPMWDIXKe-6qT2V8ICU9VJcmJYroBE1rybe-nM1o9-mTIo3_LKVCLC7UBs6hccs9ZXm4EehskpAJVk8AP9T2mUr_166gtKJ-zoxI046UYmdWK1fS-cyujG1voGCDofaeievvLlvOJBpTivnngULGrhhgARIbrl_zciygnvXazCWhkN-HCYlbp69ZcCHiRBbecp1NAR7HlkrKyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=U7cUt8k2P3zUosnVn1t61AVBb4NVlXROcalbtXtWfFpOaiLzDfrvpk6SzPjCR37XJAIGg0Wwd4mnXch0dtN3Hbni3TQnCp86M12EcmBKcXvO5q6MQE4-j2NtIvDAw5JLqwFyBz6WKCnUqWtYW09ohWOZjMO5XAQhEDEPNmWLXpfKXCLFu4YtlKiMQZl6x9pHThBN9EBlYY3xBPughp12lZbpVaBT9pPhuRp4ns2uXyPM1qBS4jCquXSS6wtOqIRqECZu6-7boNbevyO_hvZp7qEwoWP8KPIhvdhECGRYpDDcM2NHTUorJrrVtTKcTiV0K7p8rrQRiC8XTENJpRdxqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=U7cUt8k2P3zUosnVn1t61AVBb4NVlXROcalbtXtWfFpOaiLzDfrvpk6SzPjCR37XJAIGg0Wwd4mnXch0dtN3Hbni3TQnCp86M12EcmBKcXvO5q6MQE4-j2NtIvDAw5JLqwFyBz6WKCnUqWtYW09ohWOZjMO5XAQhEDEPNmWLXpfKXCLFu4YtlKiMQZl6x9pHThBN9EBlYY3xBPughp12lZbpVaBT9pPhuRp4ns2uXyPM1qBS4jCquXSS6wtOqIRqECZu6-7boNbevyO_hvZp7qEwoWP8KPIhvdhECGRYpDDcM2NHTUorJrrVtTKcTiV0K7p8rrQRiC8XTENJpRdxqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6Hn21ybijLjbJZk9Oi1tj4H5Cis1Qs8mnk7KuNKi2npNSJBvfRhOC-GQhBIYUjyOi7Q0qd0g_XUAoTeNAxUQKwnLKfglj6bfzPlpnY_AL_JooqfCJfIHOFnHNTJZKqP-ol1aPFQQdLFqfH-OVjaI2guwf8Az5Uoauo_8yCgumPKpgVgeZIvTWKfnnp9hsB-rl-eEHNyMoWjy4GmBzHxWBRhqlPDI8Rtedbm3-ILaigEnY4qN1625qOUxvwK0SUM7xnSSFIgS5u-gJFykYZssMC4fo6I8ua1zYoFaVTSSKC1sx3J8Lm_Oa0HbfUoWSv2sK8gG8Vsl4R13_66zNt1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJWN4WHzvvpTJ2RM72kMEU55xrjMMr26mXfxCOrCLSTW1cOvXCefK1xs6fDMXHyShcIR74BOeGucpLrRaJgy3lvMBfv8azgK1ctpoMxp-gF9T4bRAfKZPKsV8tnuxH8j8GRh4nZf9GWZBSNt5RHyQQeufUdTUEOdWvV161DDm2USvXXQv47xUR4WHhgV06p8fB0oKEVrGMCtUuwngfewS-wApfqamsE2nJYxggKt9W9ZKBe9jReXBxrOeQcNS6fiwotIyCoUSOQ-crmIXKz8ymwzqdiKoMR8z_MJJwg1YaXthBiR5J8QKHzG3KbRMndbYfe6y0_TRAq7_S5mL1utkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de7wR_IrWchBMTkLJMj8QwG5_7NuUg3CL3CDwySq71eRAeoNxL4FqtV20vCWGxw_meIjxBwylZxRlA7avO4VC1eSeEWX9VrRqWZaeY5-WDmDXvG9-9O9nadZyjVWmVr8RDCnQxslvzDzvRQy9nOp2Rko7bPHppoKXX_IfQP_pzmFyiGhWH_RABwus664DjMX0Eml8m3i82NVgF6yCQJ-P2_z7RQTBQPRGUzBPARQ4fbtnyWQXPTJhHk2HYqao1EBEylY0MNb4zZxeATSGmxBbox0NtqBp11ekF4uUNB84TQ5rsmdf0YiQtebEeN9Q_F9E8quJtoSM544Abw1AqKXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNfv7QzKRzban2yYHvKUatcDI1DjjXXrTS7WbtljXfVbWCAxj2I0874C-8FSzq2UP9SeC9YotqwcoBk3Dh9br125OEIHDwdpC8lJ0pvNDUZccA1T_clJXMsAFHD9TJpbZ3GtC75LzkCyS63pNsflOrKiLxX5kpTat_JntND77Axut9bJPuywSzEBOiga4Vi-GWqvqkSRe0NpOAnPvho_cIgqmVtlLqRDTGVtFmRzGXQYQzz3PX_K61F1YHBLizEjcNPv0jDkRi83eRliAu3yM7zi5F5Ne_brI1JIxkEkh2AaqCmNRM1ZrNbj0JkFxr_bQmDsytvBZDN8yvWoHbBQXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6FHZbkjaVy9f-MP4dDAqpvWIZAO3gZFshi91RZ0EXdNxN_dVaMnhSJ0JlBbHhCF8kGY4YtHJkxxQ-7y3chUracNR74vrUyjFTUUzzqZHR-3KL8qtDkX_IV-1qTvBg5TItZHZtti--2IXfwl6gZG7a2bo6Djitv7x2cD3RtLr__sIc1F_txL3sRHaT_bMt-AYb24T-8wCdNo_KjRbexqxhKi3n0kSsbmRvqf76zrp1lYwzGDnt8qAUADV3RoYaau3Ks3EpVirmJ3m53Vu3q45-BjDvZqncCqKFHIlPvvIhZMk9mwVRVGo50tsVvyoiRJvOaU7bO-twL88aaAroeqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeKkTxiQ5sIWuaXxsOD-4MmgVJ--kZKHPwP0OZwP8U4OJkHBBj_FFhX6do9G7QtAPmz_T9Xq30qXawyMFebV7je65nQ_0N_Ep_fzfwkCd7OINQQ5jO3RjM_514Q19c9L0N54PqJaPkCat9LseaLKRvzCfT_EYmQ4UfQX8Uzm97FwdGeRQxbjFd5IszEutvZ4PfakNEJ53Bqrm-HLMfvAWun0W8xK2inAlv8ddExsvPN4421f70XbvlVgmvJbzk5q2wxgV0vh1IFus7LYgfsts264AQoOfrfCPsqtslb7EMeVX0t2LVCsVc5oxwmLICVTUbeHTdhdtopabxsqXpxIug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfWeZEDLvNFsVMItx_vTD7eqIUSb6dwRnoiIqVAcBIxDJ_i1rreo1MReJ0INp59qOTIFNqNFNq0rZ7MSEEfhvVLAntO1eF_hmh5SMNSDyR6VOoH_NfM0I7leyWZTkoG30LDGSUWW8XQZy9YFY5s64FDCGwGMzoTtzMfTB_0t5CIFYlOsj5WXwKk-fphc5pqDQIEWR6MYOuZyLfgFdo1aaytJzRSHPO1rrgb7G7GcJbxFybX-yI0mZOJOdd78uBm15709pQJpFvHhb-b_i2FxY-Qg44FO1tzQqbNoFKSZwtLZDFvfrVMFvjzvTdwVHgZo-tmkgX6-chXVJsUkjpCbBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ازترکیب دوتیم‌فرانسه-مراکش در جام جهانی 2022 فقط 9 بازیکن همچنان در این دو تیم باقی‌موندن. بقیه‌خداحافظی‌کرده‌اند از بازیهای ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxfK14LyCWj9xZ0O0_yNeksymMnzVde7uZVENjG5uq1vROR4lk0poY7IzuqHz7UMLYJwlPHvO-lfo1DoyDSg7huHRepzPlVFI0qe3NFvBrlNShX5Jnh7b8tg97q7HCib51G24Dc3yxaKH9WQ4ntPXv7kIPAvVo2zueAzHuCf3x0R6ZnzmbYLzcT0UCV1e_IETJNPfNvenUQovVoS8kgG8MJyC7I9X3dPgBy341Eb_lQy0Olg53NjONObYARQhO3V_R7NdbxMKS_lWMUAlEfEpD_Gln5efa5VRtG22yeg_gjF5Udpc7O2f-iJ8W13BVBxw6kDBIgBtj5HJMhY1Ws2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZjg-bepTUOBdNybqIBPyh0r9CB07lBEpN7vO7mF4q0dv8daKIIcYlhrHXZ_GNy5GV3PkUPPWY_bsxjKlX-cG6cOU4KAspWBo0761VuwN6qPLjJ3DVPW-lfNVVBRCrSxu5fSotLTYSiZdbX4na06C23HmLaiAtpZYx79IRbwJSsqnb3ceE7ptcoSx4wJPa-kG3_yZ9MAVz6Bkf0A9UipWItdRCTO77IkaVjVQ0NHK20EhgCGdUIJ_WJmVsdJZ-MtrkVqgthWFZCbk9lU9YYOA3JwUa9po691I6dkTMGWqyRxZYbBes0pi1kF_4i5HzJeUHj9D67ddmcr4BPx6WDizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ6zhttKK9k0v2r6KUDd_HVDl0FbgEZ6ySjesXfUL2Njx2TL2GMMCP4TyWWdDUxxa1gawCoXYAhfSQ8m7LSQOQUf_zXvoORzAID6DqJ73Ne-EfdC1M16aG4aQRmNjPUfv84mAFjsrjLZ6WUeUb0B7_nYW5d8mK2KX97R58-TlPpS23LPiSm7L3x7mOt-ASIhv2JCIsirfX0e5-dtbKzViIdRxn-YKd8yShkUqwxU5UqR5DLEJdQKUCS-4d8HISugZDQvdE68HVpxwT8Jo1f-wehAzVwyo-x41igIYksNlYpbfyC5WddMtiyofuDR7Uw48bv1moHlRQZBOrl7A7nmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxkjPg3ijis11g27MYenI-XglC70WSRUdRmvlDhX_MeOBCoxB3ASsYmCW7sdlhWpae9Y_arQ-K0hoc-uGsSuT2P1ERtd2pnCjyVLdaxldGa1ePWKkuB6Ovygi9U79Z9g41Q5CyMmSxbCJ4dcDJIkSXNHJYzLc9DMDGTHatDTAJE6WOx-K8-nZNhdHPbgna_Kfd0WGkRmS32ClchDo1OF7jxzcyBAQMbX6fUL25K-N7kEoqLRQgr02PuQBNzpL1irLSZJtdcoiGHooembfd60gswtMZ1_uLNbYByWZzRWAdpwmVyuxqy_kG6bKwNPrEkKcKJhiCwOTBw4BwRh9T216A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb2pG7iZEzqYAvzj-g_C0CSwGHBQ3aqueK8qO73k2M655S_ZtahGFSVgz4-96KJPmF5PW2TDta3oERZy5A6XDh9aZByujWMEVyvJRR6OnBcN3aZVpi1CNh9zQsD_AMXGshTSdgf-9CE2gU2V4KW_obGUezpoFAsfhPVA0lkfCP8Aahn289wbCmfapcf-Q_ZXmL2_5TUgO9xT495GCEq3PX9l3c6Tu1KgE-oOhXr_2kN7Po-f9qDTCYnCqRu5od8Sf72idM_XktgdXdt_OOhM0KesYrtqMN8hJ6W9A6YEDh5jTNl0YSmdLH-p34db0KKi0ddNN-O9guJJxJHlZRQMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKnKHpX-Ez0o1GJH3PyfAVOWTs5b16TFeyWS3AQ1oMGbtund922Fh_0TlN1QLv0PdXRUqf82NKFfigi516x8oxK1wT26O2ZM0k75JpMLXoLt-y1tkjuc_vNJwwe1UIN-tq3-bZPjVJoz9xaAiV2AMNzAa8XeD4BuC82oOOslXed3Z2mmXteBEZebch27dPejHRndzp8z5cytAPDbxkKkQKmwo5omseHsw3a0o8W4v7e9zJ4ldcaSnxY1LAP78zZkKbqy624BT9h_Yx4i99SBotm2V2aOdQtK9YiFDFcr3PIc8E9DZ8eIQaw8CrRU1vzZ940MoMtHA3DKTsZDPLVo1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYpcqdD6ByE2owceYe1wNzOxdzz444wBctYch08YV0HCGWUvRf8ThqzWaQ8kskHyIYiwTuMc4P978FaDP8GZxhtkHT2ZEyzNprm7A0SKsBfkGDbHyA_RHgxdWiXLQEfh6pWchlmEOCS7fXdpWuYOmowRFceLXo5AYznldtZogceyJCkOvewidk4DhoSZ5sP6ERQi7sSDeNgKiyUIvp5RZ5tcOaRRe_7g7ResM4GlpDVdIx6CtGxyvtquML4ZApQ8fTnpZOoI5CSvrLlWJozNXyh8hv-dAYu3c34uaTLn8xA5JFrzjB5ABGc9Qg5aYFHrg-39LDWDsFBI-jUCxYCNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/25297" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ_ynT7dHsY1H_jPrZHJmTGp40vv7kJxXS94y2Rv3bA0N2hDGjvudy-TT3oPgbZf1HAKvXAsf_o0VzgwnJmcR9mpow1F-Os9DTxBGtJy-w69wMyXU2zhdbtMiUK05XULeweG0nUOKgh72mDZ9B4ZynTa4E9c9iEuZmwN2jwHIqeuJEPK-bQoUsQbosgcjWzAB20Oz9_B2y0TY0515idxU5A3n6w03q0mTrAWLOCT0KNstgZ4WgeA2LKly_P6BoHOjgGgJG5yFOFh45OBwxqRAFQxXIHkNPTX_dX2-R5oSXRUZu5bg5iyNPDXCx3gqTfz2-73Xse3rfb9uUcsWY6-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بنیامین تانیاهو
: راستش‌روکه بخواین لیونل مسی 39 سالشه و اون قبلاً هر چیزی که میخواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی‌خودش‌رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم؛ حالا از فردا بازی های آرژانتین از صداوسیما پخش نشد تعجب نکنید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECd2-Pof3kcXpG-i23OY2bvcjPl3FbAQj0_5QxHpCep4qDI-Z_Kx-u8i9M3FA2ro33s5_oGNE53P60ORzjbz7Kio_wExNQjevN_ntnQssSMmfo-MIpNGCaYtegdiewnfj2ij0mBqgc2QCZ1molzjPgfMHnC3yFVJ1Pdd3wI3nXBCVYbsZ-RFdKJvh_wJQ5et1BE3t10MLQzNP6xHtFjGp274BQkpFX_BQVw6v4-5rJJoiK1mgdamm2qJ0ZlK46b6ZW9Efp6D0MxgeM6E9gniGlgy-WO7YRFGqzI63V6S7CavU4yufo0R5v2wlmXWJVisdm4mCjLONiCOklrsHtXojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwJtQXhRUnaxSviHcTJX03SkE_yNj5BZso64tzdBD2NVYRlTJ7XovnQ_BIahzVGET2GPPhXc_FiY1SVBHhoW_qfqZcqxxWFHnuFTp8kL8Fv_gXrpFIFb1U2DUhOvt0JKHLUITEqd3xBiAa65JqNPlaeNTmyeSZDejwHuiRHlMOisIkKc7g6CMhnLQ6nEJZqDGd2nyRA0_aq0RDheq2sZEgHXLAgtnVNVMtU7VPMyBA8CctWX8D10Qht2H8cjZj3d3Z2J8zDc0_Ta2YA_QhYB7t6viYE4TfQks8LkUdXkHzdm9a4upKLLSY_9oDtAtDIKiez1QybxdoAvQ6CCoR06SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Twp7h1DuVPA6pLVwCcMJjOrm1MExBxmKWcwMFDh-vJS4v3bw7X0RAU-qPXQR2nS7OYHD3k6G3nENhGD-lgJ-xSryw0GtXeDt5dFuBQPYEQmVO905Qm144yDfB3uPR23Pecd1AHGgaXJS2yRcuEKLAP06I3jIxv376y4OOUZwXCiKNT1D3YiMoJYPw2gyGVMKguBpYGvnZQh-MqVY14iUQyq_LBS2IS_Z7s33OPE-m0zQsRdfiiOEBrYvNUhTHbBxRYXLqbvZ7Ky6n9BbrOm04YqwIETbM9K-b0ClbcLAforuFLhJSAFQlbdBI45YKs0b2JLFbL-LLNv_D-fH_qZNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG3lpBbPg5Eabq7dm82zdkMHcsf9I1hijuCJCHVtCNu48oIZcKlc95jokyaybFV1wRFW50osw2bjLwV0DZA6sx9gDSHUTPQYTVbyafqbjF0qst5Nn-39N32k8B9VfNvzxJlkpRenRdSLWmd0cpuXm24fHCoXwfFghQj-b3bsWC1uN_20HT2KO026l9cpPTSWKRIGXmfyJMnA5mq3bLK5emWL9Fr0C9G4Z_t7nV0XSPZgmk8KBE6zW3J4PjmWg4wHIIyadSnZjs4_Swl8vk3braVMeCHiHgtS7SpXztVkt8Bqwv5fF6tp-FlS84vVWUQg8LOJDhDniujw9MdbnOy1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HavWvbD-7j9z9nBFSi3S1GUfKLXcTp2jRECb2gGfE7ZaS_v4I9lXp1bOsS73b23X2QkU29GQeN5otSSo1tpLnQWZ-2j5vGzMjQpMjYragn2ovRryt6fA9V__twAv-psD2TryLnEFwFp7NBV0AIQ-eqJr2jSEnLc1ToiGHrS89lSDaoCdBXEjaPl8zbJlUUOEVM9P3EmX_CNrSyn7xQJD3dAsP6RDbxTxlZVzpn4giE7gARYNJPe9LtqarZr8okUZ4gUW-vILGqD_emudcUpYsABgswDhe7mB-o6TzqBX60QcccS0rtJBo0RTbRPqlfWLAJJyr4Hf2fDcuK0mTWulYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrGefmGesUiEcK49O9w7IJBkqFLp3qX_4lxmqh_7sfpHUsP8SEh773lcDLgCT_9uh3TTSt3IuAZ2tp-WpR0EXduqP0t-elk6EfGRC-uHX4j0BJuUq2YsPZPBPxyADVzVyfKIrAPxztCFIOwlOVYTL4l65L2FWfNufa9VXXZSj9UsD7lFUZ3UQfaErqZD4FmHKsr5Tu5Tc5EMmPkPstEXuu5YfH_vrfavGuJjc4B0NyM483N8E95IXKhrUrvH0xXL3D2KWYz6_tng8XfL4u0XMCnp2rm2h6K9c53qqZDKfCAmKiHM9mnmvH565bIJ8Vlh53JxzJbNeOY7WgeuBXzy5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXQw1D0zfdhMqPoFIhM9L8bCxtQyYVioWs5YzbjQRNbsYUGxLiYSJn166HRMXc8KlKJtm-kwHlviPIFH8pNbVtjAH1HO_nRRVFKZzBiHEOAD74N2vSbxYAxO-U28LCLVN1TSjGSGoOWqSIZRqn1JKUe-BOKPoSujsmi9Knw3xr52kBkLkOK9N5GqB06RVLXc8pbgM0V3Fu9_d2aoa2177tjzdbU_O3v_CNiQ17KlN6faT3__o7qwshiezpmbLxoOWz5bAPGOs8OCXUOHXsUWIe5DfdktS0MLSeU759yIZKcKu6XsbRgIlZbcRLM6o-SuQfxNEY-5Hq2b4wyXIDgyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgDGydNJCcvO4ErEBejToy4PiqyKecJXxdjbSDb2hpP2NmOO0fmbfKbaluBFKxFDcw27o-341mvyWsdKaFcC_qGRBGuB3Fakpy8oTiku3Nh6XA2w_CBuU0CdT1gUqqBCZmZMeTofckcgUEm4Zehizaq1IPEAAcBVJTx1mui0UIeRfdEuVHEXShkGF12bY5TfJt3XpgAiQSqokno3Hy5A-818BHWBwTju8wMPhPjnsCJT0jIy68CAufsqKvi4qGDheEt4IrAq8rRq4yUiagxTO1OCOfutG56dqZ4_5aayMVIsNlqFNm0ybxlOztpqKocou7xqnth7Q6qK0wqih-QAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم
؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ توجیهی برای اون کار ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25288" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAj-l2Bt2FkSorCP7NLtlgscKiK8riFh20ItJQ4GMyTbmpvNPG_av77G52qcPPSBr5da-HLG-T1wrw0dKczP95Kyk-0UM8GFq3c1GXq5bW3S-1K8koloij-3eYCOjAnF71sn3rJYA-QTN1OsVpLQjVafdE0HyV5X8eJs3Z4ImBkw9gsgmD7hcFKjqLWJKsQnfSmUp-w-_8JJ5_EeThm5J9APdIGHQcZjw2Zv2bL0bcWeM9Geda0Yeq12yQa5OOVaOJCBRXNNHI-XuK4fBp1s7nAE7-pLlkawvUpTEC920UkA2YwOWk_DG0Tdr7214h4NsrBjOKpUnTmbKtrEGU1u6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4Btb80ne3590zhoMtVqwpiELq_oeSdFhrMCBiPINbAHut_KA8WAcL6trl6ZZ7ai33aVr0DwUw9NGAEzZ1v0LLeInzIw_u1DIAGWXS5CM0fqEO7X5UAjveVD4-Qpu0Uo7VfkuBDdEp3RmtWMDfmGVTVQMMzrT7tVTJptLjh9uG-z-efwLQ8aW4MEnYvfuTse5fH080jmcD3WBe2eSSVH_WmpXlrU4sSyEzhBTwzlkBpio3MbEs2uZYh5n2kIVNwxg_ceogb8YBJ8myR5gY0OiuRwL4hFPe73GmUu_h0gEeRMDa9iLu5DpsX4HwW62tXz4IpJQfayIiCAE9nx93ZvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCdkOmd_Q3Z5bKvsEUmANVAvzHQ3SbTKRZd1zAm5f9jcCyVgSW76Ohn8o1mWnPLvT98fOh_687u2pAp8-Wwz5vPZt2x633dWIvVTDf6llv-xjQsV9cmaSZmg0M6SUJsxvRfAkRChRVdc0GT7Pe071uvTGJLlozlv39H_22uDNRIXul4RyG3Kk2OeYt05umIxdbWT6_9uXVa9ewAD3ufAcqE_fSho99K9zLhOafePZWFGrp4ybTohnSS398ayTLV_vwJlLY5-mUYbT2hgq2MS_G-CbEZ2qOANSOzCePE1CG16TmNNW6WzRtoltQOg_05A5mWKk4Ag7k1Q7-uMZPE9KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25284">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25284" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC00z27goK4g5gf7FI7reJlntqrY-rxGq4Mh0QzkZvDW2wKalxwFh82DpdPpG5PQY4EjR9iu1d8PTTWiCuxowG1d62iHJ2PK4mEGdQbLujhcbc-pjvdwRHGbK2wHLmzXAKWaGpwhssiEgzZWrXMAnIr1ruCNAg1URejjz62EanAramLFkON9JQwNeSAeO6_YllKqxEoPzFj3ccCxSjRZNCxV69GH9VLFjUYM9ALzsJjsXVxb_KDK7ED3VDq7Jfe7CWBpYhT5iwHriTLfF8qYBtYqjWQWiZdac0Bw-mTm8DmcBdC7548UoGLfmq85R5mDYnHrF-psMAxuAOF9oUk5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25282">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT1YkV4P330oq4-9mvtHyevIii-tObMBEn9hPoTC8ApXfgNzZkvRZDlopHZsLDIkbWtcdnOX79OzkfsTuPHZyxezHu-H3Z5H6VBCBFzb1uZZpcKTATjnMy-EmeKBhc6L_FmZxb7twwH9yaYN3yNchVhFr9pDFPUUs3_wJEuY1-I7K-rhovv-8DvDmF_MaIqh2hJ43xUgME-rVj8e7Z5oAA7wErhnAXsEbOC5t4jvgCR5qhUmpGmmik51GQG7YILDDYaO5Jn0EsRoOerJnCidxf2UQjB2D5jeQkTLhHCdg_LsV3nV_MKTDqRClJh2OLXob0z_k8gUkM4AbBVVP8puvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUNpWBKwecjFe1m4_AyHp7umMEz2eaA2RFRmPxZ3bShTh2IASqrHvYZ2zRchlM6z8AyQ6JUT2fiHz3QcKmrIfxYfBYaEsBgpHKA_fIcOx764Sx66u6i0zLhNaGHZXKoUMEzg0UOuPYGZctM7HMsPoOZzW6rAn0nybWTaJbs-0sc_L3j1t0qFNvCjni_4OdedatyzcG7D3fPP494iT5azie8zAB6ML2od-vR5WHhG_ghMx0VUib9SG6sBEWJexKOvIkoK-jkFPW86hVM_ExrT8rLGauqXBFd62uP2D1ompA6srzNyUP7HffLmya5VOHvIJ-mnIEGFAqTtfaibWGGCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7QHzCOVmH2YzFvNggK-Piyi8ZPfuqfKYErPxnbjSsKVwF0_LdFI3wYLI4NosCS7PVfSN7ar56yiRIV9IATPmPK0aI2__EVHB_ONep5BP8duiwZui3dNZTXytvUDwjjFOLRvQbE4gqwTSjqrJRu9EhaPRvpGxI9jNaVlH2MPPZjptZ4XI8tqlkMfAMLREqLshUaoHCqwPKi_YAPoNAPZ0mWT0R0-RyvbXIbkCwI8DQrVEd3ag6VHTs_VT5puOvCQ5XaUZJBTFcS-kXajBYOxbg0eFrpa448astT6fsAcXTDR0GXP5r4OkAxaKxYW9abCGm4LXgpX5sisx71yKf53bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_liKjs4iGyhWa_apgo91ofu6HR2Ru8MCz8DnT7NCGm0A6n4ZZS7AVx1FMY-Qr2KK0peciwXIuj7W1evKBpURbFUTeHR7ipM-h6faSfnCqYNdn--v0X1OlayaLHI8COsLmg9ehCFEcXxdaMlFHn9Ubx5ny33HWO6bnbR4OsxSjNO9QIJXAsqVcFADgRjJUe2vMee1jPQvUCDI0qLWCbEdEqogum3YAn8SBL53P7dz-ak6cPxOY7IGobnV99iVlnmUn2KSvJJEthbr0NjG7jHdojQuGPux1-HXDCWEADZbSRLyovq8ffMtuHKuG47lm_2m9WG8Z3JyPO-qkGZFey5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛مدیریت‌باشگاه‌استقلال میخواد بعد از تمدیدقرارداد یاسر آسانی قرارداد رستم آشورماتف مدافع 28 ساله خود را نیز تا سال 2029 تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25278" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2IQ7kcaah02utE5G9PQ2YYxXxXauN-uPEIDLpEnnjq8aySMuDEViF1lruZzW4y41hjhVK-Hl64AolcTzNJkKPEAzPYConU9herP7oie0DLbEqt8y6PD3XvMYDT3ltgOxj00yqMk3xInY700IIhC0d8nP5qzoRNvewfwU4uuQL0n9mAUqpx27PfChY18eLAW27gMQjxCPklYcpurnMuyfwFESsLFq9_7dtIj7cTitYUKY4cUie9EmKb2vRJfqtPRNd3QQ79XmjkdgpWHC55nv4AQ6QhfJjL_TnvtC5Y5K-kbg3ahl0XzhsGfKcLkHqIp418Nu1lLUd6GwOp-g-LSlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25277" target="_blank">📅 15:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/en8okEzYzqUA1fabbnwDh4Hmup3yEyg8ol3No8uAsRZE9ktMvSfgBtEnYvqRzkvRBcnNi7Yyj72QdrwLdmxBUCbwJi5WUcRth2ErX4d87XnKrbioUBLFFA2CEV16X6w1DZnZQk_H3P-fVZs0teXBrjzCzpMimKfgM7rfUYz9dye35o7KLxBtGK9xHdK96H9xTiJNSRvOuyvKS2LUh1YE4dB6oX6Rky0DOVSOS8Yb1c8pzx3rP3trA1GER1s9mnPkSeTDuTgOk6utb3M9tLB-U1wEvy0Oo9R3Anjcq_W5_1h2oyPPNayeZo33OqKUAhI9si7F6v_pZ0i8CLiRpKdctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbK-bwRdWWlykPv1PC9NYBp8YU0hNcOhfDoLbKeE27KgYHRCVbcsPdPKLIa3kjXrAiUxZBJ86yejPFrw5r7yUBUYvFAehZCn7sGh92hEHsvU3lySgF5_kojIB--7wRgdZG6kvxvrQsHaytZ5X15XvzMLW-GzmvZfzKqTY1zhJ0P53D-hRJz9j6pbXaL-5em5YPc1NYwEVdokxlA1OBekMsIiAxAXECY34iiS0f3ABdzyho9pOIcCTRW7vWiWZgjWZcNbzK4Ylp_cKNWhQeNzSEyfNC4yLQSrJcE6Wb8joGmr7yAgbc3dq5XCG3db7IwsWS1dagxnTxMdQd8sp9wHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M48fgnvBdjidgtLH2TjaRZQYlI5itVPwkji9xa5tnVVEREb0T0Ij_hlRBYZEkf8WoD-C9n6t7jw-tPvx9N5Z7ONpUx8IpbGh3mWmfM4bnZLQFSJlbPDcJBRQ70doOqrLRuY5ULPdN2vbXO2-oPcR3aE5jn0omYpRmkJmQlvVHa_knE6HfvxraGptTHFieyY1eEa1cPKYVnglLz0uoXo4q5ttaSHQz_zGxErPgreLOu6pOJDhq62gVDPoatb3q5ct3P6phOWnWmgsXItMYcIpzT7ygwroJTMWW_eQmUKZ50mRhXf2Z0lGpdEbFHQ6xDl7LeCzdqdiwfMU_D5gcGg87A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmfSUaDa6a1eCp_e4TJU0evMISd4Op2uBl9t21BnhwZA3z60wYKVRWN0ArLECNAYjaDQN7qmCdrLTfsWeivWfdqzGLm1QgRNm1rYKvqi7BDl8s1ekmgW-vMFrCN1rTTcJinjQAQX0NbN2uDTuB5zhALGaTmQA5dSl9m8aCMHSRsyEX2YSL-6JoWF7_s4-wMi6jsjlMX6veSqMazL6tBkjhCYzfKSAlgKPdvb4pjA4q5nte-DUNCebwJL4YjAdnwrSsPKbHHMIGug8NHxULkjExacnNF7JStIgeZKvs0KC5nudSFaw_7ChDSkyyJ7l4uI4lgeBIahS9kLO49pSLiAow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAjDERw7wD6QipExwmGnvu8S50eIIz5LM1NbFj2QK2Cefo80IzWanKpPul2-aw_3v8skYEzeJ7ybSsjO4fKD_fdYcxFZ-3Nu_AM3fqR-vOE44MC4mefz5EbGBIyn0oDFHOEPkjIex7OIG7WJ_WACBjOhgCp-hT9MmyypIbMOF70hfVJogEqlCwlul1mk9Vxj7oNzWaiOAYLla64TAuks1KO_WTgPdn_72uhIsjHuIi-h-3Oqmf34h4kVbKP2awZQKWuGYgRNwPRP0vjXn9ZY_6jaC688N1uN5tInyy9RFhEaN1CtU4wAZ9ift6o874RhiJ_d9IjRCv_CJESI26ROPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjeIafOZdOI3ceAleeXj1dDyyHWmIIAobo6lJuxdC7kGwRek8bySvtQS3wSUExDGOEmEb-ATIp73iCrOj-xaZUV-YgL0AqJq_qM9_yPmr7ljOdT79IPbKPa9Ek3qHEbJf0d0BUWsuPVhkXDqyL2cCkkavIYZJSEd1LjXXbPoInb5pYfqPHXyQeJrDn5eieZuZ9zlCHeepPzyH5bkAb6sJyTuUehfDssMbOJ64102HcMI-6pTR-4or_KjLk_xYQ717HHzdWDNy8fViEolV6ZJhNQRaYSGAMEQhM1fPNSBMty2FaoAk_BFzIDPFexsRw8Sz43jh9c4qoQgegl4s9VgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqzfFgTRwlxMWfEa3csAHYmvLIfxjXaK2l0D_9qRVfAhaOuOGzw6WRbkXVyubdpqU6RU2FDmmahzj_SmN5UDz41XYBRNh8_37KrSyCTcnH4dE18UD_64i3XDZo-9M6c6LI5l004OVm-p3sWTcmFnabo7gAN_J1WV1nY6rZiSrlpN-_0htCxB7yhIGWIKhVz50Fo9RwERk6TPCJ003c1uPpbu-N4T-AKMc3rQEIyIf3bIb7fMFluEYD_X-jdEo0CT4x0BqvUa9GUds7VZ4WnHyYlHugokZdW34dA_79DY30Jhb4y-pegrXvNBhFtJmGEZukELECKHSeyixHDckr72qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25270" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25269">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR7Gs9-jBiBUoelOY_AbHm9LIHa5x5aV0IE25BTC1xRIQ1RG9k5yP0Hc85AgRVtN9RqFYBz3tLLC-cH91zNd_ISx5apItJi9ZQBMIxojRjVUnjlTjJWeLlnguUcD0grkfitQjx7U9hehrN9XAKItFML3qGP5DH81oEgNf6rMrPlkTo_pPKuX86mKvI_fGdeOXyIo2jhYNWopIY5rGx1s2H6pNqce6CGFO4GywwVYbXB837v4HjWeXFuzvGTSg1GDn7vjbnBcbTDH-7548naji6PfGj0FfepH3cBZs5ekg6QdSS4UW6Iamv3W4Fy9tpNJJIdWD5F0LI0w_trTRc1_Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کریم آدیمی‌درسال۲۰۲۱: بارسلونا یکی‌از بهترین باشگاه‌های جهان است و برای من مایه افتخار است که‌آن‌ها خواهان جذب من هستند. در خودم میبینم روزی به این باشگاه بزرگ بپیوندم و بدرخشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25269" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25268">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4ZwXb3AguZmBRg0_hwJuqqq1ubRHbIQkId7Py7QlbaiAEPsvZu-hFoohkPKqaHelfGN-bd9lFcF_KuT2Dh3alVTgFx70g18tUBCPykBIGK8UIzEo8BLKmnQmzzOMk5YBsU58pFwUUnHULbbUqQPdiVwhm6sNG3K4gG99QgJaPS4L_NiBZeGAscs-ECYwbYu0aSWqRnWy1zhZcxqVuEPGe-EZxLUyUb6XpELhlZqT9Q0JMKJV5RTVjezajrVDbNKrc5jvSLqvbS0Y5mFbMT-cEQjlKpzYpRFe58UxPcBhgB1lmZsJGDHpwz1qH-vtjeT4hAo31lrAC9YqqxxBZkn_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت‌عملکردکلی لئو مسی فوق‌ستاره آرژانتینی 39 ساله فوتبال جهان در کل دوران حرفه ای خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25268" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=tzjVjAwZUxtxvxYQCOeCCC_u04nvsn4PuLyClroataVs-gXbqCNdASPISd_zvXKtlC77Vp01bXTYPAnES7OFGIqt34T88aQiRXwjE3oZpszIk8hV9PqTsm5_6JAM4HlfRPMngaYI659xgPvwg0tQJ5eJ1FI6om2bY0lkLXWyoP39Y4cgVioARlKew-7X8FI-RYItp1rd9TneVDKoAOsF-xBdLVdwNw5g801hvat1ZlXogrwNcHxUsM1WE10sDafDmbrjvh3u6eOeCzVtcpvv0ZcUebqEkhi8wpWwU_b3q4GVKHffdUB4RySdRHCa5KljrXYbsNG_zrgYOHyzTeTZRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=tzjVjAwZUxtxvxYQCOeCCC_u04nvsn4PuLyClroataVs-gXbqCNdASPISd_zvXKtlC77Vp01bXTYPAnES7OFGIqt34T88aQiRXwjE3oZpszIk8hV9PqTsm5_6JAM4HlfRPMngaYI659xgPvwg0tQJ5eJ1FI6om2bY0lkLXWyoP39Y4cgVioARlKew-7X8FI-RYItp1rd9TneVDKoAOsF-xBdLVdwNw5g801hvat1ZlXogrwNcHxUsM1WE10sDafDmbrjvh3u6eOeCzVtcpvv0ZcUebqEkhi8wpWwU_b3q4GVKHffdUB4RySdRHCa5KljrXYbsNG_zrgYOHyzTeTZRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25267" target="_blank">📅 12:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qO7oMicuonh-j6NxecyCasJTtAx5mmKT0khYAU-yhxQekvvvhoPAvY8DEjYALQA4gzuywVzaJfC9wZ51Wwr0z8voS8Gg0cNUf89oW1fe4yrsY4jk2wuSBM8WORh6iMuypIJPfhRSaDeM8aFKikCPgl_Sx950xeotC8tmioJZ-BcV9Dt8fSVbLwc8jNbUDuFnylC-pjO1Ef_kbzatAGILlOZNMbBhtc545ff40zNhtHre5jvrIckoUWxQ2YGy3lkq6zwvKaiNhe7asFJern8LlimTemWb7nDfhAC9na5Tr-MKGFmjzdtLfRHEWh99WKzJQcDVVfaja6RFY5SCQd2CdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN4eygRPQ5HfgMKGpo3dU9JrHEuwNqJzcSi6tHZLI-7HCTXbElwRJPI-VeuVB3jKpZt5ZtAZc1MIAxZ5650rNT2IwQ74EjczzVM0b0QViLKz5kykXPlZEFZY2Rqg_lji9mR6fMiP81egeI4blxzRX1bsLU60X9nAeWaddxvZBH9TRmBKEFW0nEUZNcmGqp72bjHCX3nEm4BFfsaySe1y-J7DxXT82gy8RXLyMmT0GPE1cHsA5y-tOBrN2zNv5NYZJJ7bsy7Bm6z3bC4ZVOHzgiXbmsSeitQZUnvtdZHEmzwF551dGVDl-uGxcfzRtiL5-HUJP6fS_0oEuLij4OYyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0a9aD8zB9D5dJl4zdu3SD1Y5JSg71ipRouvJN_81oBLYS4-mE_V7Yw0miqiFoQP83Ctll6DwrvTS-cBUJX7Yvf5xQQZjaOxg91wHJgG6ZCfCabBWVkNB3woOpRHkqzyhkuaSrkPkIpwE_CfX2FtxFu2h2g0scip7rKhLdv5qUUjiR48Yql4Mu5Dljr0xaRxqP82CZue7XzKfUQJnG3ZdvguJxjWru2-FtXexy2-gK1nolQq6-HiwputNbm3gLd5PmnAuxV-ejNNDav9hbIHZNTQ2OTd_weD2XwOXVyKno8T3K6nUDAzurjgnOgOIoqRegqYZiGxUDsDVBDVhQaAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=hcbbNUQoKWEr8NXP41_KEfvrRGOUterpwCKjAaotvE4maZqIvrDNPmdKkE8r2rHTwZ53f2O4DkTVLM-u_hW8qIf3UEyh8Hh9doTlU5PLPsmSxDYpjuISY40yo7SOEffJiVyQkX8PAlwSJCta6vDvmbR2miIaEeyDZTWRZjdIFTp8eY5nrNAaEpw6jztvrLsmLYaE8sHcfgKgMDm-3c53aMOUAeoLiDqGTdLE-24iqnScy2KLxBuA8IgPfWZIBR4_M6p_grOm0pv--dUOoHipCuKey-DHsI4k9F1vfLlpkICSfVClojlWeW2OSSrVoGCma2a3RT6Vl7Oj7xM-vyyUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=hcbbNUQoKWEr8NXP41_KEfvrRGOUterpwCKjAaotvE4maZqIvrDNPmdKkE8r2rHTwZ53f2O4DkTVLM-u_hW8qIf3UEyh8Hh9doTlU5PLPsmSxDYpjuISY40yo7SOEffJiVyQkX8PAlwSJCta6vDvmbR2miIaEeyDZTWRZjdIFTp8eY5nrNAaEpw6jztvrLsmLYaE8sHcfgKgMDm-3c53aMOUAeoLiDqGTdLE-24iqnScy2KLxBuA8IgPfWZIBR4_M6p_grOm0pv--dUOoHipCuKey-DHsI4k9F1vfLlpkICSfVClojlWeW2OSSrVoGCma2a3RT6Vl7Oj7xM-vyyUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6-T4Nboa7dbq6S6_JieAVPsAp0aoWirlj-o94B121M3JQOmrkLo3MoAtsh-c7qe4PRKjWWbMl9ln1baQ6sSar4qK6r9HD2HvWIcDAUf9iS8AkxG_Gs3w3QXXLugzC1X_4VoWNhN08L7IKnLMk_IaoE9vGUXEtcl10PQgUUz_cpKQ_a7OrgsGCPnLO-Nq07Viioa9S6YoA2c6uAfoxo4yxLvldOmHBKFHiF00qijLGvWcs_0m6VnnGpVA25Lvjzx2bl9rV-k7e_8Cvw1SotbJ0rcGveK9AKfDTl0UPqxzFB0tELLMMY2tIx_DHzpYnhghEfnS_oChjCVxQ0sPP5c6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نوع‌حکومت در ۱۰ کشور برتر و ۱۰ کشور پایین جهان از نظر شادی و کیفیت زندگی؛ منبع: گزارش جهانی شادی ۲۰۲۴ و شاخص کیفیت زندگی ۲۰۲۴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25262" target="_blank">📅 10:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngqt3so-9-jE3DQo5dR48DcSUpU4a85_zows7aIqzb6eDl6bw1B2-IzgTR1mzZ4kuwHoBiO2MrOh6nk9PUebMZrRS7tY6FHCCgl75V_euDCl1l4dO8LK7OrxeTuhu8Z2boo2rkl9-0yd32lV0BMUphsxoxOfsolL1x-a44PIsezFK-qZbXI2nrJssgiy0pXZV8QrG-xHk-K5SDCHOFKRJVhiO1pTDmrnLeMz8LHN55H39bHadhRVKLl44QztyQB17gDoHy2JIl2XhS5VlMzUY7pvAkWsuvxLkGX_wuRBjPlUX2iSU-qSQjdYsHc9-QKFPOC0uS3dhQZg3trwENtP_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25261" target="_blank">📅 10:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz8btdQAbhLjH2O5Nk6NTRRdrkObEcbFtdqH31BnTHavnyF06XLU3qOPxKOTrhb4L1gE19UL0KnDB5jBVoK-A3lOgiZqc7V5d_-Wm5b_WZg14xi0jtcvjYpN4uO9b75ltzCIvWxiYogG3UNR9NfOfDCv0_pLpvwI1I1POQ5TOjmhUsDpMWWi-YPsoZavAg4k80OZpWYnK9PqXNK9bcr-Uj5B9nUmbBroucLrODe07nvqCQRU_wnCyXRemgSYkEam4TIe2_MQt6cE44dCSTPnE5PvWgrifylH6Xc0n_SvTa49z3i_s2-6-BYIOAbm0ID139Rn3dovPqXPuTX8jq_k_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25260" target="_blank">📅 10:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jA1lR4fSbNbZ9NRo9p2g4iM1D1kvBAjIJ6Rf_AB5WDOEo2AX-EKpoA6FqBjy9k-OSghpVkqlC2W67gPolqpWtlUzZDzjX0F_1DLVAbGUWYeZWEmcVajqbJVwrht-5yE_S2uU6NJT2T0S1mcXmarYrd9fjhnpJk7bvie27QDG4mNc-sG5U8hwDUkLexVxNMoH7VzlU48Zvrw5FU4eAP6eqdoaIpDLUg0XQdV-ZXKwZ_OVFCx5FwSWxcg2RNvU2nyfUcmf8Nj3UxvvZhvz5qoHfOb7JfSwDHVYW8a8e9XDj4tjMCOByJ2gTeWw7c69jSR0Z_BpNj5hlQjuQT6FKKjvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25259" target="_blank">📅 09:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25258">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qg0ZFZCN2h7-5xiMWjO5msb5GJrzsglEK0n19ckoWluXAT5UpCIxJKSH1-OIAE_XWHWn0V3RL2LMAn6ZKU4zv6Uu86Y2d4kRR8wh-cWdTZre3Zk6ZyAz5Eeqpi178BYlEvSwT4w1uPLlRHtrdgOAn2fd88iCdr3XT8q9a8SrO51HExmgC_P5Yh18Apr-rXlOkrdFMaUismb6ZU4m1q2NTsEeqFG_h8Fmpb5rgUU99UQzqUiybnVs-spclS5sI4DKmPDm0XiSIO7GSeDFRYP46ffCz9WgiACyutROMBd3qtzgCqzOQ-Dfr_A9MAOw7YLWRkbJjY9x9dMmsC98-TiHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25258" target="_blank">📅 09:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tps8pLG6qNhKL6LD3iQitVqaZ5leDkoVoQM47Gu-4-AEo0WUnk9Oy6iK0HUxF_x238wiI1VcXXXAboShWQ4pc-DJO38g7hru7Egd2hnuOQwH4o-GKodkL3nhvqr2Aio5YXco_7o39TQb816vle1tVI9EZXyy8NwLT7WZSPZpJCR9riGAADj9kfG5fHMQFI8MmvVpD7pMfHWmtFYF-bQB4nI3KLjDHpQHjz4XnS9RDeLaC7lCBbpz0Bt5x6_HveEbJiCEZuf5b6jS3TvNkULHyMOACsdlkIIOWetIegq6IbOLg3cJBBvj7WYVLtsaoRw5LIKbmYFN5B29MmtRQmZpHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25257" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnOkzRNNlJKn1UTPmqa0zeeQNglIOUJB5answnxaZqHUDxr_vM0N8kSuufrsh1jX_lmtBmvc721jBinqW4sQN8O384nVtnOuMZwYCy27hWuZ1v1g2_QuGReO2eKVHuvsgXmiXn7o3xbWB1MVwOLVBDLeTVK0lh13ZUyh7BkMy7Hx3HL9kTHi-vTAi_FJlaFtt5F989yh8IUr4wE9NmqlRk1utx0sYJi4kxAX5JVrSQyjgwsZMmklogyuo2MZP2XwuCNrRtlu1w4W4IeCiUgBakdpXqotXrqCBG7UhQoyQUd2PnR3rLNr8nJ9gPoa_FpiO-J3deZStyiBBxAjmzOXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25256" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=LHj8uH_p8OCt30W6q2dcuUIX03sGmY9gPiupfnjKCpGYqLFhPDxqRz3kggsJPsTjjMRFNGjGp9pU5KzM19IOV7gXE7554Tn-Kdx7KJ4MLsaXZPCswNuNFJ88afIeNpaP2LXAoZZPHRJXK9x9bCok2WeZiPtAUH-EEWK_HUYsVotl5vmL10ctuF7BNywro9kNY0H3N-mtAdx9EmDI1_-iahkrTZykBaxL503wDATWz3SyHHf4QDPi-VcjfnqooKRNbGqs-0sAO3V4RE6lwnNJlOngSrNMfuhY61bTiL64D_ttU9gW0hVDr8CW9rfZ8Qzexp2nJWGMj-WnUuT8ooV-vIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=LHj8uH_p8OCt30W6q2dcuUIX03sGmY9gPiupfnjKCpGYqLFhPDxqRz3kggsJPsTjjMRFNGjGp9pU5KzM19IOV7gXE7554Tn-Kdx7KJ4MLsaXZPCswNuNFJ88afIeNpaP2LXAoZZPHRJXK9x9bCok2WeZiPtAUH-EEWK_HUYsVotl5vmL10ctuF7BNywro9kNY0H3N-mtAdx9EmDI1_-iahkrTZykBaxL503wDATWz3SyHHf4QDPi-VcjfnqooKRNbGqs-0sAO3V4RE6lwnNJlOngSrNMfuhY61bTiL64D_ttU9gW0hVDr8CW9rfZ8Qzexp2nJWGMj-WnUuT8ooV-vIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMrp_I5VwsBh_vxwvuh5nVO2Ijq5UGaxjgFnwZ52kPGWr4sCrzr2NMyOhUGxZjcaQsZKEJjyKMbTubEDuYAshGQUTnvtIXYYn8Cu9z1dYS_J_qx1Fle5hGCpqkyLEhqY8e_TabkmPnLCMEEfgZ3_EIzfy_2zlWdBONh6bgi7r1yegDLNva0AKMICbtICdwxrl5FLPU6jr1cr0HNKnzp0-lOB6nrudebL0jabD1N6gQH_7Yyds4NtNa-aSbRssXe3Hzcm4rD5vvazDcQP93ymL9rMEZSDlRXiPre20vcWItDy_vYrpHmYlNXS5cRJaga598NUs_RPl3Rv2K-YYS68yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ_ml6G4-Xc-9mYi3uC_NOiwFp9mzTJ240PuqSfNstyrioo6b3MeY181-qcC0zCjUnLefxf2sHuEnQ54puLJI1zaSi4a5e306Vxa58JqEiU2ryaz6Z3SRax8_XYpNLFsOh5fwXfx8964qlbhfuqIgcz8aEIXvUNL5VUw5q4GCzOqJet9BiFfB8da0YBQyC64l9tPtg8JHMlt-hpckRm-gsdEjjEMnTrOGGeHyrX5r1p8uvOHOBNLZcuZH_i8DgajMX9MWBsdd-tcJIFaUZeq1eB2AdWtMg46Y_miJfvsVw1ddbO2KGaZX7QWXMHdsHlMajC9JBvwAMVFRoAgT91gMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0QcO79DQVs85pDMd38FBDY6ibPh7nOStxk-33o_UDDK9UN-pk5kqw251UXRk7eAGh4tmsw2JvDZD4P7iKi6LeutA1SR-iUvNWY-qJ8BQPBAx9EIK56tX1ykDcH8lY9NTNVAYTpZpwPMh2QrEyCQg8XRe4BbU--YjKCmlYwm5bNY1qvlZeA9ayqT-W6wXtQAxRj2jJJKL0G5_GtTI-nd7O46424l9zJAJfAfMBbi19dZMU1Em4EoipqQytr0Usrs1iWocSVRE0d-vW12euYvHl0hBG7APgiF3q1oVCUL15dt-qHhvl9tdv1aMbZZpFrhFAIw6BpK033OYkk6N1_npg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798637471.mp4?token=PP4qXUfVx3bX5MeEKJxNTAXDjkHJYyE1H0mbQ34UO_oeLoJ0oskvqwS1cahDCU9zCuAg3rhZm2LUzzOutTU2R7NcoZ5lzmeMA5zroBLeo5DloWYx6OBR8Y9p6wBchFTVga0O4kxdpxy_wKXp9e0Mpt-tzjAmKMrCXvAcEa5DO7jW1FanC3FisOgbqwMFe3sIaRSSEb5b9fdXylgAsCNwxma4uEQbO8I_Jv6-ufS7GCRyeXgsbcHET5vYQ0OpsL2tZr2ObPokQBVuf1OltdA7Izq4MBtXSQBcCwZmWCf9myz4Rw46MBuSijC96yMfEqHVGVUbrDJKq0ISYQzPn0rmCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798637471.mp4?token=PP4qXUfVx3bX5MeEKJxNTAXDjkHJYyE1H0mbQ34UO_oeLoJ0oskvqwS1cahDCU9zCuAg3rhZm2LUzzOutTU2R7NcoZ5lzmeMA5zroBLeo5DloWYx6OBR8Y9p6wBchFTVga0O4kxdpxy_wKXp9e0Mpt-tzjAmKMrCXvAcEa5DO7jW1FanC3FisOgbqwMFe3sIaRSSEb5b9fdXylgAsCNwxma4uEQbO8I_Jv6-ufS7GCRyeXgsbcHET5vYQ0OpsL2tZr2ObPokQBVuf1OltdA7Izq4MBtXSQBcCwZmWCf9myz4Rw46MBuSijC96yMfEqHVGVUbrDJKq0ISYQzPn0rmCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی‌ تو ویژه‌ برنامه‌امشب جمله معروف
"گشتم نبود نگرد نیست رو گفت" خداداد هنگ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25250" target="_blank">📅 01:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfB4qxI4hkYIj5CSI7X5dAW0DDQg2daz2qBhEvkGvbIrtwuQ23Mxm2YLaWPMx-vtR_uKD7mVLvCaW4qa6DG4I9kRgFEAKoOoQrREp7DUJdZ5yr2VEyIRCN8g3LKVP8FPtVgodMX79ZRW8cHfzlSiGiJCdQGcqWSZvK3DyE36QZBRg0hNiBu6zjkYmbzLA_5jVcWbUEwZ01rsVEigoDalCcIRae1tmy27lPEO_aYBthg6VLYNMwVRaY5kxgjCrYIXWoWHUtrkB44d9l34RRW8hdBJNd9qUjtcjcG8TpMYT52KkU8KCbjsFQLc1HHPbCBTcjv3D8hEMWmQnGcvzWAoaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خوزه‌فلیکس‌دیاز:باشگاه‌منچستریونایتد برای‌ جذب‌اورلین شوامنی هافبک26 ساله تیم ملی فرانسه به باشگاه‌رئال‌مادرید نامه زد. کهکشانی‌ها برای فروش شوامنی ملی پوش 100 میلیون یورو میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25249" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSB7GoIRXi_Rtr6nCwWK2CykPgiWXqLMghw9iyZpj6GqOQ_FtkUaeXEY8k6fzQopT46DfnKaD47o9x07nIPKqjSEjWCHnHafJ7nAEanJEZDmPQgqQ1DDY7lbf63npf58L2CZDRwx30Umn5RCUlKvSKlbjG7MDwLb_l6Ftq4bIAMQEWIbx6wlXndixA3N7L59At5NgjaCswpzr9UMqql27-anLsoIK0Xf9a7cpbpdstpqbxHBuXpBRFPhSaK_XFomU4jBSoejZQct40cAOQDBva13fivNdgvu7f70Okzg789LZmjizsPA4_XcLOcPq9QttC5CJHQBQD8XRXit2EFBMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛
آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25248" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpVUsGs9sJRPLd2DjUWcdnRS-jgksA8uh2QEC-2545YmZspcyMgYn3xgDLaIoCyxbFUdp1Jn-f0MYFf4ccMXoY2xQ5p1MAGh6mvQWjIRdn93Yb185g02kM1Tw579q8H98fdG3Gcrpy_sabLZVzc1z4WfQlythoY_Xr5iCjIDnkE6k6_11ka3EOG60Ri6sGmubmQ6bg3tvYqwth0jSA7kG9d_SlbuKA4rZj3dm5T-YgGVSoRB3g93vRoI9YNcmaT_aFnRylDQANMud1UFsXR6K9YheB1DEY3GUjbp3J5mGQN2H0YVkVBd4zn39iLlphkvRns4o1KgLLZFMX41e_C7yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس‌هایی‌که از وضعيت امشب بوشهر داره دست به دست میشه: یکی به این ترامپ احمق بگه هنوزجام‌جهانی‌تموم‌نشده دهنت سرویس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25247" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVKjZjBmWzQQ7yRZpzEgpR0F6Cqdjqi6-HCbDL6q-25CssBGjU80f-8MBWPZggdg4DutVzC9-fD0Gddw-ZAhSrZn4PGI1vKv3Axs3A7ogu0f5CmjbC7kAKo3eFqAbFu1fqhKSSP2UZ3vW050WRETtKG2ItBLAVF0zQBtntmedoAxfrILLSekY8P5VSd9QstZQnDuLWNaTy0AzMDQNWviyGvSWeAJWiK6yvrKiAHPcafMKnoxTMX8C_m0KzspwQ5XNDuJlikLLBx-LMj9Uny2DVAAcQCQsaFafHGKvp16bhfP7QlIc6ytS42FzLPCeFL4i8Gw6TYOJSYwVUVL30x1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdJo8E5Kj6BjtY-JQE6D9WaTJ_iUMj8ZNW4Q8RyKoKqOPHBukFRP_ij8_g5t586_9i1tV59mfA0raLrr_4Eprl_Sb5pWY8wIx7iCPeLHb-aecPOMhHtV3R6Fa9cljz-GjmbQVUSxAj54JadRRk3fkz2dKyHwWtvm0cnUJ3-KK0A0lLe3qmHmaHjK3Kh-AZZlgW2EE4ptJqqukXewKz3D7YMbCqvcfk4sA_api2R9jhsVpNK9NghBlPc37p1lllQhAtB6hgSR2SE0QTM11Qnxr6_NZmnGSwxuqlPSQ4ToPaAdelXRuQe9pXkB5buhDae6JeuH-QEo0cIlLB0-r1WIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiEnPGQs_QY5C-IEg-j5VG0zHBFOjJg8VV6p6DwIHcZCQB8HlDJ7zzdnc3uHF8Y5R4man6BCpUFyy0cgb0hCj2WsSg7E1e323L0XjZOqiKfXUkjWPZlxouUXRHXFajg_NzuZr8jVqcb002TiPCHllTM-n-GBW4WznqFfN4OgEqtjvDdrTN30DD4isVsCaCXjWaxf6Lqpw0k9XBbCannNcrmAjzmV0f2TTeLtOehbj3bSY3Ew-KWkvAFrZPLbNlvLSfuel-3Qcn5LDAG19E7zEVaZQlVoNeUngSVCX2FZrEpUyCZrxK0vJBzRfCYZsEm1AB8TTuO927JW9PNL_Y0Y5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJi3_zU_IW5NLa-V9fsVoEAkXn6XHvDD-BD0PUqwMKwxyr4z7oxT7n1g92DeTsMYJVQmPfzzC9sXom6WvWbhYVKg8PG32f6nbxTzxrIcT2L1blZcedLyZNAnQs2a4NV1bflUVYXoKUcy0n30wHjr5y92nftZHAR0ZvFDitHaVngjXLhrsFsUDD9f_i_thBtzpcttxh_APZE-UNT5j617YfpSiuEeF5ZDT1Dw_yDTakVhdxUEnyU8ecPFdzrdCLIFvjbzbPmDh3TRMxMW25XhM5V2yjckcePu16mXnO_iStmwLkYuM77aKoyREG8zIWBktTLS29BzKw_jmmBvSRznyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vdgd_8OrmimK14-ou2eKy6P__nawy0KwNtOYG7qeLKmpqRmK7OxS7pfNsTPORoQxrpPdsZTF_rxwsJeFe892cRkXQpIVzwbZMXhDU9ax2-cNWRAgy6R-XDv34jiwwcPPSQ7dOoMdli521nQ10P8anSyoxgRav16XEi4tTdoVuEjBAmu4A3h_OdoyraPee6xjxcStrxwmuyuwnxHgNKZxQxR4FpcohkWEe2CmYQzAWUcwuJFrSc-L6IBe69yNIzYWruDS_ciU5WTOE3Dm8JI-ibYTgbaBFL-j-B5Z8dPFjgX65IasVKz3OdszejLH1DgbQVGlDDBhaz90W_-4vc9jCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UG6CiB4hcvRscJ1RzV11oMHgxmfXGt76_VAILPX_whsr0AeWWLrwLtAHOI9z0DSKAr6FsKGg_33zJDunDclVOocC6Cd-hvz9enkDoWnVpUzd2TG6fB2jZuTD4-shP27EICZ08DWkm4lk87hIzWzi6p51YjczY-yEszDaKvweAc5fuX9eIemtpTWrhj48Uf2Sy_0uB1v_Y0Q29xCfDFJi8HSeGfvfAL491aSq4Etr8-bfzOabzd8oB249Pb__JDMmLbyag7VLht2lGp_PZrHzh95zr2aI6yFacf4nNLcmolWGoNeX9jRccpJYstKJ4VlrMXGKg-W7YEZn5B0ZjstDeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=ETgCe2QfeQE1UG6-6Z76s8IPV1GELOA55D3TIY2cqz06aLo6sVeR4vZwNJaeLPdICsRN99eGhBZNKYPe5o5f81fNQoiD5OZy5F-ToOelEn6XUsnY8j7T-D1cbpVgCdlBWWnuWyuIRlK-_tfXiq6R3FgRlM5asVXkwsegqw98zktXMb29WJfpDVSLcqsrIP7la9yrxRKc-JoCQF905TktR4O8qpHLcGlRGiotxxm8u4IHurJrY7t-FzihFKdeMQo1ZDd5SsyVcAWZo1WUO69QsxRntCP_rQU3MCtBBYOvFtxK8x7pcoiWnV_Ex_SlJTK071mJPUxKpsoiwOrRH9cMFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=ETgCe2QfeQE1UG6-6Z76s8IPV1GELOA55D3TIY2cqz06aLo6sVeR4vZwNJaeLPdICsRN99eGhBZNKYPe5o5f81fNQoiD5OZy5F-ToOelEn6XUsnY8j7T-D1cbpVgCdlBWWnuWyuIRlK-_tfXiq6R3FgRlM5asVXkwsegqw98zktXMb29WJfpDVSLcqsrIP7la9yrxRKc-JoCQF905TktR4O8qpHLcGlRGiotxxm8u4IHurJrY7t-FzihFKdeMQo1ZDd5SsyVcAWZo1WUO69QsxRntCP_rQU3MCtBBYOvFtxK8x7pcoiWnV_Ex_SlJTK071mJPUxKpsoiwOrRH9cMFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران: کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-ulnCmf6IPO7Jt2PowHr259L4btadO2oj4fsqTBJP1B1iGforM6KiZ6zYpFh2mBcDlAtWXW78kVTOYkCZKb4C80lLV9lSctSEzxYjyKnFU-gIUy8TR1B5v97V5pgy3cGy7m9MxvBn39w5R8fj9B_n_Wqea5GkllkSFfToBPNOF39kD6n411F210yA2q3NkM-r_n0TYh4jSmbSdy2Y3N0OoNFCqS-T5fEuA9o1AZRCpoSpTzi6IUVLwPnBWLx66DeeIuos15h-ZTzKC3IyA5HC592FVHO5iMZyOO7MIpMnNeHNJiLxGvUl1ZM-Rzy5z2rdjGf9WEPrlMzK_kBTTiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lunjHlI0cBPl5v8loJn9uzvkiIJ9Xg4JjacSUhCp7ivHp-MAxGn3Yz5TE6WWcLa9B8U75OmCNlAMYpKkywNhU4JjLnUrqAtAsG8_cye2j4ljrcbkZAAs7hPIWpU2WIe4HdMvaoNd8iYilEEwQDYxNnVLOE3dYQqLYOvMysb5BspaIXJwyoWYfEMQi2ijJmfkTeXmjD70OOIhwhu5KKv0Tx2TSr4od1LE7zkLa8MAt_nRc82f2GzUN0vqdKRNP0uoOcBH2-ibT-cricX55ywyYYQbg-FWHuY88l24C7mgmAGCYzWEQAqyCWJnTKOq38bbdLVFnpuOhtzzDkQLkzLw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOE5NABguH43rbvG_eFdJDxCX6Ep0qPDcPtc2p2z8j-zXpww_coVj2dJGKKZ98gkZGrYwopAV9zD15oADCYNqByD8JLxtuUvplgmX7qazkprPz1HKnapLGlFT5wfPZeKfMujtyRyJVE-GksYbghvgqMAxnG5m_6xnEnqw7isXReMniTOpeTLiFhLj_47pT7nyT1R3nrJ--Mnp32aG5k9fTic0HNqt_mYFmnubsCGeE0192FRwcG7CfndawxS2zhFcvp6RDvG1ORPp2O-8QgbFPstNyCE6Th1CI6QyKwWGRbHwlJ1G_dt6_aNzvKCJ_Or44GFOmz7xO25uwWFMUJOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMx3EzBllpI6h32N9VDXf0KimEkml0yXXOLwZ_eGxKLhk_RS6qO3M3rc-6uAcJcDHWyntzD-U94cNS-J6th2HaUHxkg-jmqf8wtBlQYsasqJjmcEzdfNFDW1fSUG7EnamPUj28v4QHU1LTef2H60hhLKPNBeIqNVsL7J5Q1doUemeVJGq_3ur319VQnF6U0jvzO2HHV3UlNt8H52-q_zNnbfuem1WtshxprMagYmLbOvuWhNdmogGB_Gwa38bFAR1bIkiv-1r8lg9nG0KI-jBwHr6gmiprkZLII7VGjSxtO7NE591i73BRQSlKUUXxsk8XHs8q5BcOCFjDk1adsPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVUDjBt9hcT_3bB-hZhtdEie7qmFRtp1Ulmleiu8M1GmMb37fsAm_2dDqusFdQCWIJ0nHcZ1OxiT9EY7dmMCPBVj7Ij5sFpJ49tJZr9352T_SykZHKQsEMomBZ1eWVTMfG9E1wb4uqti7J4TaCwV_U19u2bxeo9ar9hwyD8URaPzhtbv89vA4Miyxy-xlzXR8l0dhsIp6kOkUt2RiMfr7qRZPsevQ60WDPXtcL0EbvpEW4SMWQTs3efi2evZiVzaudS4kORngStolztYAkz5bGa8R-um-xkZkmjdUZwNAw3FBs2lr2y2GNJ3OOgm4sm1E1DtSZ2tDYeJ6FufhsrnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbX5LsFurN59jRSwCCAMEQqQWC5DyWUr4l9r5wAFmcCgzL4oVmTaemVdG09AvR_35EpNN30DyphIkGaR0qywN5xRacqaInewF2aKJgKO7NLLVRpfS1dT0a_qa01YWsNxUK9lV_TOsTZ2V1OEi7DbLz1NUDjf9iE8IEW9uny1U-Yx_B5k-vB1sk6cAO8c36yzK0ORKnRybbGteECnM724kJkDRIZ8bIhvHqEK_7-mYO9t4_xpX1ksvPVT-u4YSy-E2o2ke4W7tMJKbbEerORptXwhBOPxLUajsbzEXfSdUHNB_oexvfdxRIdQblBu8b5FLk4qfrHdd6YPKm-LP0uN0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3Eu4GO8B-7aAkzOR_0-KGCXkrEtpir5jQpOIgDSB053Tp3YAFh47H_nX2weJ1-B7onGMNUw2n7VlCRE2IxhEqjiRtfW1B-tSYo0gpjLktS0PE7iNo-eekL3ho87pq1pWX4MJzG-v_g1irpRzOr4IqkaSSpUh6V9r6ojVgJ2psymS5ku4kVYifkRGhau0Y0qdkv5Kz5ZYrKXJrEtXgtchAhwLQlwFXtmSIqBwrF2jv_RY0ZOxMGBtsqM9S7EqxxHtJTCO6pVaVA5S9Tks__efGCXoal7aCWPEJ0gIlJbtb6g1D24Sy0qul_ZkezR5PZTA1EMIBYlB31u27mvJo1DsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5RjCSpFQMAGdrW3hXjjsiHxCC684xpoMG84zqoDtofvQi5bCpBiQngVdF4MDm0YeB_CZQPdYixvG7p99jYOfcgZT5mStbwL4lSXE753aiwyie65ThvkdRVEdmaWKKaa_3Stkp-sJiJi0kvR8r-2ROhIw18nwMWDfQ_HQOkVdwG2u6zEJT-hH0_Zc8fUWjnAkQLd8-gtgfZZKjgs7kIW6BMcuZO5712nYiTh2Q8SKy6b94i4Rj6A3K2X3mYEaHlB5CxXyZd9H5sW09X7kjUEHupaL1pGamOBkXuUjXsFhNrOW8U9BvKzJmrqm3A5i5cKWkx6_AcgkcyMkwAedHGyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw59fZ7uXkrvPq1eISZCyU0bulvY3bIPJ7fmkpvlkljdHQcmLTQzVpBPludPHnNKFO0l87GusfgmPkLGR8BKJ3CgpOlKEGFOFI1NCy3ROON3IAMsk9yClDsYiCCQ0kBFz_H5cRhRPrJQvrLZ8xOi6VMxhb-zlKPiUd5er6BEnZvh0CUT4z2WLS-Azm2RXfcufVvUEeKvLp04IcbHSvBdFe-Hv0DgBuBgeYWT6Sn0WTV3sIB7iXUoU1GJ75zH9gHJYqIxOXpEqyeNfeA3LUUBVZMQG2yDLypiLVozoWxQMABXyiaqs1im7qiBBLqTirNODAcIVKCsx-5YKVF6GXXoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9nc4q4fo4fB7FpqoHyUlMWV-dU5euGG24gFpUEkn8cBIRx7WGb_CGBN6CTOSFM_o8PHqvBrMJVUu1LyfvBQGwS9zuhQgWj2GCFVmE5LkeJITN6nOFVmiXaySGvwQcqCyhfptyXDZgPvqDQSlurG96kykaqzctv_9QCHCOQY0D3XxIkGERO6UB-nBRq7lhm_psdDv_MnAk3LVvsGGFfN__NH_olNOC8rqokjdoqyMIXqtJvnLTjZOsf4JESOIJ3jBvY7pCMznIoSWBr1BtU2UEhnB4GSfbJuVwMBnkMi72sEnsn6iMe1etCuVBYN9Bgf-2yDnboQ_FlrdGhbmiJ5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=SHMnBnAQIxmBpJj_dNBCJifXjHOCIhD6_kz0IwVmoDJJ65IhNDSmwjYXX87ChpvqHvtRIklRxi1Dhxm6USQ_XY3VM3vx2pKZzo3RBZ0Xko9LcagJTQEDMx3xfHh2lEjcB7US_6mibmw2xch8vPd-vhXBXjPxeyBcN3A34eHiVKZCKoFkR7Ox4lFra2gGchNsAmWg9EqB7S7JWrSRSkZhd3e54CGBKuu_fhP5INMxbMkIYiF0qlEQXzPQWXYPMq7iHAAnqFM62HAP5x37x3visiOIp8QwojqUstjy7NI_n8Mi-XMLhd_QhgCSdta31cROsEG0tqJdxnuj8MLJmxJB2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=SHMnBnAQIxmBpJj_dNBCJifXjHOCIhD6_kz0IwVmoDJJ65IhNDSmwjYXX87ChpvqHvtRIklRxi1Dhxm6USQ_XY3VM3vx2pKZzo3RBZ0Xko9LcagJTQEDMx3xfHh2lEjcB7US_6mibmw2xch8vPd-vhXBXjPxeyBcN3A34eHiVKZCKoFkR7Ox4lFra2gGchNsAmWg9EqB7S7JWrSRSkZhd3e54CGBKuu_fhP5INMxbMkIYiF0qlEQXzPQWXYPMq7iHAAnqFM62HAP5x37x3visiOIp8QwojqUstjy7NI_n8Mi-XMLhd_QhgCSdta31cROsEG0tqJdxnuj8MLJmxJB2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-t4oeYO7qEBzmQ-r8ZOIo71cQKRNVvdIgsjTbmBH8mtPaiG9O80946XWZpJTWvYXjVCB2wxUm_2ZNkxDj8adfo4F6sFOO-Dx6HhL2BbLcc8KD3KFIAtOZqosDekYWNY-2g2UsfbQLFGd-mu0oBdWEVCnhk2DCnzxIRafRCpaSUaaHU5nGwMMp-3m-evuBsUHKUAftbxaBxtr5IaDO-jVgaSSWFfMr7uz8PG4HQ-OYC2PMTpQ5ulJkQz9Zk5nztyy90gml9cqTgNM-IFH38ChAtcrsd7Ns2Uy-tA4kCHN7UIIc4V_s58uTkDaIq_Oh52bG_aZlMVxKdqZjjG4E9Sxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbYtaAhlTuXWcUVmnltd3GUn7cy2xCHBST8iQVzmuBZcj_pKGpUUYPBC109YQALqlgamV23pcEA4vi-8vJo4R1NyPwF3ccLKwxUEAmrgKbvYyaCNoWGNmyPUGNGgtAPsegO6zJmg5ZuXCCQv0snMMYV5cLaxzYMgeoNXKHaWTModtWoza_aTCSK6A3urLh8DCCfjHn0kkaz1lyaC76KNDAIb5n4Gb7KOAc-O3rNqLqA_5uRaynTKpBwBMhsbMGhHySEasrAhNIriLpCDHVUx6dNibC9rzpL48I-vAZa8SF-ahz06jZb3ol2NNf_l5i1nfya5aIdhBTzltLapG6NfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkBo8qEISbRj4B58VvA_a4EMsTbscey6YSyeZoxIy3EgJTrFJ_zTXHh4LnSfjL1seVjqB0eCjFS3iAOZTY_Ewly0Sud5cRzZv2UOIRIlZBLH6szYQhMaqR80kR_lZftlcmFwm5WdDIFMwiBspAMXv8Uvc-M6rBM-cASMZFKiLKcL27EoXSvr1GkTK3EIvIWAChlsCmnAV8uUH9OGuMAgpxTLADAzsAsIjuoVF4_zIMVCpU8_fysjUfqlO-XYUmVk-o2T7RlwEu5ku-11N-ZEVSg5Tgb60PeHSVYO7YgIaRc-S5jGHGWGV8KfyMSSJvrNkME2v7YzuLTD2DqZRG7r4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhWmAPyCeNuUgxTt-HtSaTK_EN0VC-eJRMoyWUM7At2q9dMc8AQr3-Z9GxxmWcLYducbkLbEJ3hUpnqq6CLN0CeIGDJagRUE2N9k_TyQAwnRCBlbK9CtVcXEzb_zTZL3xhLVQ990i86-Gqt5_Qb9NLnWVMnF3puUldhkDwxQRSycBM6KxoqQM0mHYB-PdAUvXGpHIQ6LBWNh0i-r_pkftvh6XkgpspORt9ID7EhJrtufXSkwHBgop6dlDFoXo5DwF-3QR4Oa4xZKBrDYKeX44QtyjW4OOqwW5OQ4t5gx5-o5mu2JPcPUeZK3pHSTsWSP9zUTMrB0zL1OjLLm0jzETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzuNYBL3HiYs1RgYE3P9LVfz3_pFPv0eHjW2U6ExT8a2gQ1MkYMHjV_ToNUkaRVf0qDOuDqzEL5j2GoR8LaPw61FP0DPeJU4fUSukhiSBTVDK62iV4HjHNDEq84nGJPQCRaPq4mynL5OvyEWM8GSc1e-iIs1xT3vtYN4tNy9zeVAsj7k9UQRj_GmTgpHVUAGTeADPW1kn7mjdbR8hcRZG8SWTTGGfdu2-iA2vJ1jK-RBAlLikyfrDxZ_h4KiDcKptELqGktUShaiYEhIpbjNolnASju7bVrHeptPLNBGtsC242ZQ18sYSjHaGU-zWOxQvtMVzxRxLOhR7Syisnn95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fznOg_r1wf457MR-c_Fv7TcQ6mKunaeElcW89JezsRTmN27ivn-w6uBdn-QCTncQrrWhwwLnR9Vy0ognDpMqBDlkJRCq0RzlEMwGPfhzBq9TC114006ad_wLUi54q1CRzkpe8BSAXPV30dMWR_yhvfEcE7Y-zZU4C-aN4tBUjb7wWJtt9L41-i6bPAeRMu8XYSAMyC2_4c2qjrwS3biN5fx6MtiTlNkEe74DxPBpsHu0xIiGMl1arvzvHvFhSycpUB3seoaN8yLJVIYsXrbFoNPUfvlyOa3QaBuniXNR-1jWGYtDftr8g4C_zLJ9ZGqhXippdPVj3oc3xbAsZxQ2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a93VWKAypAXkNc1d4c0og5X5y5BFD1LXTCdnrc0ZE2mmoPiGy4h1QhSjTzHJoLI-WioStbkGIwoBEcZSqRK5U584MYBefHbRCnRhqynhsmSJkku02CY1bWh2iIrlOHZFNMB4IzihKJIUYZi9jrlMrYghdfVx7QQbAYy9IydLFvmHSyhEqzDweKiG3igrDbKqgISFNkSfhVMQetWZeQGnsMw7SlJp80ENaTV7DgLwloidfVhCw07P39n4fiWCooc85sug3UuDBIWOWK6UVmn-aEzY5Ol1xG5LTJ1UaQHI9OZ_m4FnwXaJbzaSaC7b2YoXJyRUjpP9HwusBazcJ61QUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EK_gYufaRCPo_KQ_ovEZxOIPgSx9lcF4LoSlprOzMlU4wk0Q0Z7_OXVxBiUcSIei8Z8rTuG710j_qoBRPDolnv295YKt34sGJChe_psK9GHjTDyup5hQxxDIpuJNP3MohoJj7fa7M6dXgnEKl331Zy62O20PcXjiLRiKLg-er8yRuBNrDwwVIM1AOmef9iJ2WcPhNTfHn-8xDmf-rWFE9xgXLKcEqflQIWeu8VnIwr63wED8mNSzeypLZsMZ-gDgrXKtq5em83uE18HjXkZiGsWY5_95SgRA-eVPuF_ns4tNKFPST_umko_2Dnp_hcMzmBMI3_vI2neW_FZghWOOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f158271b54.mp4?token=OWSXnANBPdtT2w-0MM6ZgHoTrhRTH72LFhNZFmishef1woYlIs3uTI720xSfJi4DoGDXLC6g_Ne0hz7xe_cDDhxim9Ml0MUa5E7cTqciqQKvcv7ORtvvIyLrWFpampHDYS80YwPP_9efF6yImtVsti9Bql4EvvlF-brlNNr18lBOLamxAzyFeGeHcqfYlZDvHaqcnfwVdUAV4UjKSGhQRupV8jx3ahmxcZWCeLOJtfoV-aTy-_tpAxIRZJXIztOTkUoZQnTrUqQFcs5JXZsXEvq2JomI_CnoeoWLGJImRbBB5Twb4v1EFkQa8y6U8EmAcc0XnPT_0gFepQXm1Xzhcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f158271b54.mp4?token=OWSXnANBPdtT2w-0MM6ZgHoTrhRTH72LFhNZFmishef1woYlIs3uTI720xSfJi4DoGDXLC6g_Ne0hz7xe_cDDhxim9Ml0MUa5E7cTqciqQKvcv7ORtvvIyLrWFpampHDYS80YwPP_9efF6yImtVsti9Bql4EvvlF-brlNNr18lBOLamxAzyFeGeHcqfYlZDvHaqcnfwVdUAV4UjKSGhQRupV8jx3ahmxcZWCeLOJtfoV-aTy-_tpAxIRZJXIztOTkUoZQnTrUqQFcs5JXZsXEvq2JomI_CnoeoWLGJImRbBB5Twb4v1EFkQa8y6U8EmAcc0XnPT_0gFepQXm1Xzhcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب‌مهران‌مدیری‌ازدرآمدفغانی؛
علیرضا فغانی سال ۹۹ وقتی‌ایران‌ بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNUU_MHqfRCjShRIzld3Vb2O3aktkmvcvnpO_2s5l4UOT7MClMLzKi1kEBkRJ7Oji6HC72IbP2qVyNeh49qrcF2AtbdoRyDeEVbfIzO93ONhFA0QXvedLg4C8V_-ZSFW7amYkiQsevq0Q5YzQatmvSQ6Aqab_rzJ0SrmxovjV9iH_JYym6GCUClulBXxQKqZv8O5sU8BE20oySFCnoAzbG4FFXowVSRQL23mUzx-P_ftmdUViNKrduDGWmjAcv7RaDM5H9-53JJZB4Nxylmz8XnkxNSwA6iBiILk8uZO_TtYw4H2dsCxNrtz-M38g1i-bWIAtpg8CpBgg5SpjQuoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEN2x__M2i1FZnfY1BbMujuPlCotalVdkj2ErPMerrQG0h9-z8kChfXGOC4x1yfez17SsePyChyYHLPGmRgFXKPjy2vy8rya5WMGtaYhTp135qXPP0hgI3j-5ixSEDDZbW5rKkHR3lwVZXq6SCzZI_Vk2qrAP8SsrYlpBjoJostt4en9cPTc6sJnDwERvAUDHJ0ocpDF8PMOd0pkt1QI9W4lkDkFiTTTIfrTHQIHWpI5O8NEPN0cBkqrtr0UkyO_htDgrDyNZ_nEnKBZJPgQ2xcn-jwXSI3klyaHB8L9VgjTLbRjHRltLKEL-mCNVkQtK-s8w-1vD7_rAZ3_IRmxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-H-OddxgS0MS6a8QqFDkffo__Zfc-m6ccj6XdEk0Pg8XDahjtl4T_blmNI_ZIqUU7ShY449oMeqhOLGX4PUsSkVKZQCFBQzT9b90aDLTYeLF84Br4uDoTtl3niTZXu8tyOed9FJhFtUHopKuprS7cAzEDB5dK-raFv49IqlQ6avUKwudBrun6qQIz9cF1kcUDSo_HPod55aMr8aF7i7BCxHrdE_PBz5AhzFkZmvF4SpUBrr9HXlnWFHbeY-zSQGygprTztHULI-fPRQFzXV-6sGAaLGdoeUG8-iy8BEuO_DazcjTjnSw9Rhe5APizimT4LJEfnWHuUpfZ04pydQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZUyTCZN_0rh8jCALUsF4snKaWLjnL2HcvvSvRAh-XKSqt4QktNoY9y1IpzuLIrbpqJLDbIBYqfdmleIBgOEOmatL_tOIc2pXy3yEhDgh8McEs64NOdiAHBvH3m7kzvV1ovYp64_UvcT-w5llevUsoSa5YY3Nb5us4oZSEtYp_94HmTPWrZiOo4HeOfvpwENsnucQjqYgDpSWFu7zRQOJHbmz6yUgM25VkqeT-pFXQ8W5QsqVuNbxZIQ9UZtyrlB63I6p2UQ5zOnWWgQrhyTlcpEBlGaCn-tpwBzMAYbDwOeYlOSwzTUG6iuKQcY7G1nj7sDiQIBoT6oNnIPO5uLjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=Fy15klcKD27bSf7ur6je62e3P-I5wVCzvKqjaqniJATahwrAB_QfltbUC1m0M4TaU8C2_6zOC6CFi_Q5Evs5OJYpHXUh-PF-B5lG0YmdMKhntD7pjzGtMH0VawxVmx9TaB6HDAZoYUAUtXuBPEkZbF-jHn8BQg8BrUBpoAYPZyV5o-_cyehp3aidfvWLIh68XWKGdoMf_3rfTTgrO9SPPLXg65E18y92Jp0RnYstOgkED8QJzv3Ez5AHrTki9pGIfvMdgF8liCD9bwlxo4HY1TSAGMwJp11w9wz8CW3d15q80rWjEdkykLmx-q4xYaqX9VF59fZyXGlCqoc3QQPBiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=Fy15klcKD27bSf7ur6je62e3P-I5wVCzvKqjaqniJATahwrAB_QfltbUC1m0M4TaU8C2_6zOC6CFi_Q5Evs5OJYpHXUh-PF-B5lG0YmdMKhntD7pjzGtMH0VawxVmx9TaB6HDAZoYUAUtXuBPEkZbF-jHn8BQg8BrUBpoAYPZyV5o-_cyehp3aidfvWLIh68XWKGdoMf_3rfTTgrO9SPPLXg65E18y92Jp0RnYstOgkED8QJzv3Ez5AHrTki9pGIfvMdgF8liCD9bwlxo4HY1TSAGMwJp11w9wz8CW3d15q80rWjEdkykLmx-q4xYaqX9VF59fZyXGlCqoc3QQPBiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPcrXDB_TxinCjreOpxsQb-S-qhlkQRUhUx4vmg7_et-nl7eRtkEpXYEvZblWGnE5OkzWnt-fVZTaE4nrrWlP8JYPY81QGszuBWjlJcU2bajyhdhpLm62M12WhXopu2Xk2bLUJVcxd6tihiVRwAjM8CepVW9yNLTeb5BLQ47UqAK2zSKL3KK_nalw1BmJMkDwHj7wWEcZW2ufWjfv25GztKy8MWNxnTYNhxyfD9hixD2waFrYbUMzQZSvfk891U68xhcM0MkU9o2Fe1tdC1TQsAI45yh-UQf--LbQOolqYGBEWhG0pzCuM4EXqVxurHHVxL9fnnUTA6fNQSy6Q2XwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVXUxwawA-dLn_lV1xJ6g5C6fNKLaHdu9W2J1L2Y2OH8VW7qGAyY9TvqoeKBnsoxYfVty2pFON4AkqxxdjdpLAQM70MCiYDDxIOOvPzvXquswX6UrJ-v0BzcLh34jcB-8HLw0PrG2Q0AoXvQtIa9Lq38oydDQ0Tybv9P2igHTIjvkio44FEeUskN0oL2mPXFtCtCWMO8rhLMl_pEVnYIuvbeYBQfcnFmQ1KnD7JxGn-iU6sjQFzDZzEYSNLzZNGS0v6Fj4b5e8ed5RbIDRkIuPo5gIkFRV_dN7Gw7741O-qHzJquaHwxuceKEXRrPBQ8bl-9iZrgqJ44ZhI1EUhvvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_vdmW-Hnb-sekPgXSDRp1T9bw_I9E1OmJGSpLT3nnohoDzW4BBOAi4U1bJ5TLp2k90sHhr6RSSmYkwxCEs2ht1yipV4ReZf51GDzRtqsUs14CTi1X46NwuIhKL7u4-urF0L0fH0Sdt2BPFeEcL5Acurd7-dsxF0xcRMEPzoOjHxh5NcNPUgZLH58JeHMVv-mXLGtGfdb-9sFemvMoXgYa4NbwpoeMrGXAIa4At2MHwKF9Iast563GhCQ3deIo8M_Lqu30ey38tqLKf22vTJCLogDG8keoB4BwTHpYTv6MqWfm-0lmM9MZcrgjTT5pbHqs1LUK4M5ZSEsTZOp4Ca_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxhQFLSMz8bVJw1AYDx2Igo4KlBEFj_jWTOxOHQpXDV06LYMMsV7ea86sptvEWYsoSguUH-30NIOGAJY9_tK7v8xiniKc7adZZuIgx0wWARSGULU3ElKPmLYwxxcxLf8CzgwGPsSWTeLbC3h7vqX3rbQ3zbKx0WKtXD1Zg95jPm066n_-18Z0EaKwF2uwW-iDnBzEa_r-AMb76O3-o4MTbH2z-vELuSnvSow_6vcEQpcxH8LRymy2PZRVxxpZoOwod8kiGcVn5-3mf4zt0heou-uEjEtqZt5QEQ7hKTYemHymTVnbegCbECKt9CLApslkZRLHlXqsCj_UCzLH07pVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=cZ7xrvNcJTVthStGEUaZsK12Z3U2sfotZGG66vvDc42J6C3zID7e57n4bKDDlc7oqtlEKEPKDH9iACQU8mnzYmvnJr25MSHUz2EDtq6yGhFXujjBHG-DJzh09cYEMiZbYv00A7DkheNYwjRoF8ai5piDOaKOTkQFKJ-KS925raEFUVd3DT_B-zLIEzjIrI5RCagViwlqplfFXRMH9ORT_0kWG3rRa_sz5ChnBtZHKkVprbzkaEqSgb4HinzvRCqIoXc78CqlmjUxlHjCN9yOu0o8-mHNs0-V-_taN05ZT71kPtmpW0ghvN2HWSS5dvmof1fzQhcWb5DOYQJ5m8ImJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=cZ7xrvNcJTVthStGEUaZsK12Z3U2sfotZGG66vvDc42J6C3zID7e57n4bKDDlc7oqtlEKEPKDH9iACQU8mnzYmvnJr25MSHUz2EDtq6yGhFXujjBHG-DJzh09cYEMiZbYv00A7DkheNYwjRoF8ai5piDOaKOTkQFKJ-KS925raEFUVd3DT_B-zLIEzjIrI5RCagViwlqplfFXRMH9ORT_0kWG3rRa_sz5ChnBtZHKkVprbzkaEqSgb4HinzvRCqIoXc78CqlmjUxlHjCN9yOu0o8-mHNs0-V-_taN05ZT71kPtmpW0ghvN2HWSS5dvmof1fzQhcWb5DOYQJ5m8ImJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
