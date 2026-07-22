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
<img src="https://cdn5.telesco.pe/file/c1-UUzRPDMFrpp37Aitenah-07p7dfFkpTx1A6kUPIDn7JMtW6-bjggYRcZZXi85beImwQcNEQ1e8q76v7bf-662xcH5Q_IH2fEDp781lsSLpw6F9EUrPTj8H7xVj9fHtCE1v1S5LZCQD8Im712MoA2JZyjhRWq88mpcxG5qRY8Qf1zoQxUy1bsfbMzNkWRQG0Y-TzN4rDYsp8d0eZJS2ZBSfLY32FudILw2B4VqOrEVnHvH4J5AI7w46ENNiP63GhiN8VLUKCQ-x2xg1LUsWAL7zo4au_PF2GVaeh3sV4taxUZpFpJRrHQWC7U1Dk496tLjxxhSJUQMNPOM_EJ8sA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 544K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 08:41:34</div>
<hr>

<div class="tg-post" id="msg-101523">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obim39LVcCFd3Nr2BfyRK6W-Inhbbryl_67rMFSXm8EwqUD-l3a52i213tIFU-sMnlL7i67DPtryPvXrzeSoOsabe6P8yQZhZ9aUg5o-JdNSQ8DXNdKu0pxcPxH5p8bQJKCrYwZpCcWRZmLUmo3tUSRmD6-9j37JgZ1ybmLwUvaa9L0UGFQpNjeT9qa_wHcrJVjIO2P2zyWKGgAME-_VCm3nDK13aVVFj8qxmehXntj5K1ESUWavrzCOf1Ftm812BMAOqjEKKdtxPottOREXXT9qq3C_maOaQ7PQXL_Ucr9rk-F_QuyAWqoMYMAu-WIuQODkkmYoS3ZI6TzLbbDsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
👏
دیگه قرار نیست بعد دیدنش بفهمیم که 4 سال از زندگی گذشته و اوچوای دوست داشتنی بالاخره از فوتبال خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 520 · <a href="https://t.me/Futball180TV/101523" target="_blank">📅 08:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101522">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMZ5cfgwCf940Ov2GZHLynfGwQ-b3tLNSYFs6rvFht-58ELx9Rz2Qh_tWD6kzSXGK7nLDKA4jr-0r5BIzXiIAS7Md3U3bxaQF-GD7yWzzt01MAWdtHTtZiu0KVNZU9VwHoBbJePcnvoDOe5VYAq7Q0G5utaGBKzEFIqc8vksiklL2oOmF3r9h9VU-V3Nc6iHIq0yOrTggfYHCxPhxb0mR-XUqPhEyIw0MX-BzL1DQMSe8bRA_uc_wCo9YC2mi9N4fricZAs8ZgZ1nyvfldGp110NNBD1IXoydX-OJaOz4WKD1KrXVGRdg0Rik5HOOZ95BDfHW_qpebOC4nJ-QdELzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">-EURO 2024
-2025 Champions League
-2026 Champions League
-2026 World Cup
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/101522" target="_blank">📅 08:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101521">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
⚽️
ماريو كورتگانا:
🤩
🤩
- رئال مادرید در صورت ارائه پیشنهادی مناسب آماده فروش کاماوینگا و رائول آسنسیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101521" target="_blank">📅 02:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101520">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mklh6hrbvi3GEronsTOpq6TS5rYqwmaq7Zx5ntdWLitYMPEH7g6S2wu3v_orUkeFciXFtHNsGO4sIj_IWOBSWcROJ_B12ra9q0RtByZDvVo7pSWYplQw6lhn0Ayxt8Q-y4AMBhCk_tBQr0eleod9D3ftWf_XzXUM4hj2SLfFlCARe1sQaJbjI6tfH8FtFo_HZ7H4bL9LiUd5hvYP7PVi2cvpzgFcj0XGgvL8Fi7awQ3GV8hd2kfOotGR0vffFgkDxsU2aJicTxVM5cfGIJhv8vjpUgKpivnvS-PH3scbvWBmFVT0z9TzTqL7qasMLiKTTHB75CQGoCnrhIZMKK5ISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇳
دونالد ترامپ در یک جمع خصوصی به اینفانتینو پیشنهاد داده که در صورت عدم انتخاب مجدد به عنوان رئیس فیفا، نامزد پست دبیرکلی سازمان‌ملل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/101520" target="_blank">📅 01:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101519">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZoQC2h_yE4ZcWE_WVu1trKwz4A4apEz4euGFNSSgRHui64lkTPcvsmWRbwdHRXUm7KeRiMxN8TIPLxpAq-T8jx7fbbZaX7l4mKiufC_m3zrN-FBP_j668TsE2F9w-FV_K-CCC71542jm-XrdAxGB6VTEtqFW1JpsWHIr01uS6AxiMaPPtXR6YyceTDAlSOpgInR7CYAGL_ND9a-2f2z2XXhAD2tHNBlMc6aGPFOjU8hKhkKVYA5hR-iHfBzFWKvsLvU_I_t9EZxIVjVxi8Da0tjajqva0t-GQDZr-U5iSw0w1pYhkNy_19b0HShmStLD958AIADXnTvSmGn_q1b2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین جذب فالور از جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101519" target="_blank">📅 01:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101518">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL6znC1FgLjM6QpaCD2zoDcgZqHanLSScDqle32zIq361VeXZQXwV64JDavWO0yymYBvWv9IrdS1zxl21a_GtyEFyOMaW9SzaaQwcD3eZpo-LTEAqr-1vjl_7lJ00w_8LigUv1PAdy2lCdF-ss2zu2IG40IXhPtau9tqanAWw4gozarb4VyMF38Ss1X2VrWDqX-bEDxRTM4NnFFV5qlskqO23X_BTmQz9WxpJV3OdB3qz5FNKlxoTeSwrmEZmC0U1gy_9yXiHl8_S0ubo9EjCQf1g2jjh2WzLg_97Vyy-wU_E7_vI9tuvr6q6qG0eUqyuzbvXBZmO7mBiLHBRQSN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییییییی از متئو مورتو:
– فلورنتینو پِرز اکنون بیشتر از قبل، تمایل به تکمیل انتقال رودری دارد. توافق بر سر شرایط شخصی، به زودی حاصل خواهد شد.
💣
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101518" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101517">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101517" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101516">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWIK2oQe5MF1shfjF1DWHxa9bC_rHMSEjMgpXbzm5JoXMSHDU-SmqxzfF_H44Lr9CJ3ltXm3FzEohQAseXQvGBFv3NUYkl5tt02hOy8gvhas6kKaYFRPqsElKV_b8jRzLLFJs9TZu2ox56nimCekAM-J4HvTMr42TRlleZCsAJEmrOdg_5y2FCt0utJ9Tw0aHrgv6p0cX6ZCFT6zvxaVoDxqbaBsd1GDGiEN3ljLDTixK1MX04xXuXsc1OfmAePFDkdcPIg0Ithnil6Vq8yrJKU0ghdpO6cZH28oPcjCvviyRMvOEC1FTI8FBu0XYuVwHvWLnyTJLlwiNaOd9TvPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/101516" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101515">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgEvpbfwwkWI-ZSMgldNS5hnxOKY8tPF2XIv8X6Oj-bG7stb1qQgW_4ye11EaVtApo_mqNHkxx_uZnO8s4xSnsCuZeDIotk7TgKKv3ApACTMFKudztqAgPFkVRbdyUxrszIOoKwX5RMPIeSAmHpQ405hVETR1rA-vIAnde3c5u0WTv-1HIMrMCFSXKUxnggvyp-R3TxJFKuTORZXr5wRzb4EiZd_UF5QPig3UZDkM4K50qZP-vbb59FQbdJXnOcJ8Gp5HViN9QwkgHpQHKjak1oMv0gIXtUSfgdQSN9GttzavtWS1j1cSJsJJIXQUMoEvLJc1jktzDsWte8my8Pdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جدیدترین مصاحبه رودری و باز هم خایمالیش برای رئال مادرید:
🔹
رئال مادرید بزرگ‌ترین باشگاه دنیاست و واقعاً دلم می‌خواد برای این تیم بازی کنم. من و خانواده‌ام دوست داریم به اسپانیا برگردیم. اگر لازم باشه بدون لحظه‌ای تردید قراردادم رو با رئال امضا می‌کنم.
🔹
مدیر برنامه‌هام با رئال مادرید در ارتباطه اما بهش گفتم تا وقتی مسابقات تموم نشده، حواسم رو پرت نکنه. حالا می‌رم تعطیلات رو کنار خانواده‌ام بگذرونم و امیدوارم مدیر برنامه‌هام به‌زودی با یه خبر خوب باهام تماس بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101515" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101514">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=MVFTo7Qy-drtEOhZjCpXj85D7iD2uSIfmUBaIPrJqzOh-dxg85tK3tWFRS5OLm5s9u6744L8XGJKhh3D-wZ40NJrz40HUuAEHgC58XA55oGGtpMnlxY8upN2V6Tk68wu92yAx-vXJUXks9qp-wNUJSuTbzdm8yqIssF8tPKT8o3_WgYO5BvrAwiNvLXXep_AY5-guDJOL0vj8YO7CJkbWeJS_mHj4zfDcWQk7q33EBjXD2QnlI1hsDStT4_QvFi8ton5wLrnRI6DbimDfrd89yyEi3L7X80oiaI6S9v5TrqCXBGVZ9Pn2WNPETo9pBl62uY_s5yUgeUc657xqHER8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=MVFTo7Qy-drtEOhZjCpXj85D7iD2uSIfmUBaIPrJqzOh-dxg85tK3tWFRS5OLm5s9u6744L8XGJKhh3D-wZ40NJrz40HUuAEHgC58XA55oGGtpMnlxY8upN2V6Tk68wu92yAx-vXJUXks9qp-wNUJSuTbzdm8yqIssF8tPKT8o3_WgYO5BvrAwiNvLXXep_AY5-guDJOL0vj8YO7CJkbWeJS_mHj4zfDcWQk7q33EBjXD2QnlI1hsDStT4_QvFi8ton5wLrnRI6DbimDfrd89yyEi3L7X80oiaI6S9v5TrqCXBGVZ9Pn2WNPETo9pBl62uY_s5yUgeUc657xqHER8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی و فابیان رویز که اهل شهر لوس پالاسیوس استان سویا هستن بعد از قهرمانی با تیم ملی اسپانیا در جام جهانی، وقتی به شهر محل تولدشون رفتن، بردنشون روی ترازو و اندازه وزن بدنشون بهشون گوجه دادن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101514" target="_blank">📅 01:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101513">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO1LvhIZihDB1ShY30R_oczXqc2pZNECK0Kb6inSzvehjycsubEZbfQ_Ty3hNf1OX1K8nUeW-r2xd_FdwdxiKsu5S31xvimugj0LtTzEjycdFGKX4HUL8tuK40K8JN2pAJOHrlqSbX5MSqUBy5_ueCeSRvnPJzuqTEA01_OL8qGlrd_OZuoZNezI_qDy8UC-yqdIVmmSR_LEj_scOIs1TBq6AuHhUjjA7_bQBSorwzvjsSKUjLA3xC58T7PuZhtzVgyaSivSnUBlSxQi2IwR2PYo3Z-gkQsfUQvafg6dXTkrxE62X13tpJ813mGhB1pbcH1XnjqeZcPqiUqlOvWIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۵۰ بازیکن برتر جام‌جهانی از نگاه the Athletic
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101513" target="_blank">📅 01:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101512">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3M84O6JqK7eVXl78_6QA-ZomQRpkrLmkkTxgMDaE9ZIJgioUCTDahgysNe0hCcLU0ioQfKtrOl-M1hWcHYkHXLYdI2h_WQ4ixl55C-ht2WU7tpXnS4UtXYoCQzN900DWoq1_haRBgj4F-k97uRVT-aexMnzYPM3iO2n-UsMaRt8TwW9nGH4S6_wifTHLhD3AZ6yu3v0Q4Y2Fxew1qYJ4eR1ptpJr5iWuEB7ECAU9hhLl2f8f2_bMA5DO91YiB-GGAlbNBHcu67MqVIHsBSACdDP4KRMzPx8Hq2T2hFxDYJP1vhsCQQKeksy8c8p2nerZrS8YWRemM4xa7cigUI0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
از رامون‌آلوارز: دیدگاه رئال‌مادرید نسبت به جذب رودری عوض شده و احتمال عقد قرارداد با ستاره تیم‌ملی اسپانیا افزایش یافته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101512" target="_blank">📅 00:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101511">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
قرارگاه مرکزی خاتم‌الانبیا: تهدید حملات آمریکا به مراکز هسته‌ای ایران جدی است و اگر چنین اتفاقی رخ بدهد تمامی کشورهای منطقه آماج موشک‌های سهمگین قرار خواهند گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101511" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101509">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuweMksr9dQjH1dOUybDigkRZnOzy5q5WBpr2ogziLVryEbOorrPys1o0JB37rCzA_w6GYtuU9mlf7dEQd-_rPsrsX2DV_akgNtqLJZeA-v6f4PuVZiftzPOW7jU93-sA6rvRWAQ5I5wa-UMb4MIaTcmzjbS3xXGj_CCT8RDoZV4cy4x_3v0AUFJzYiTAvOUPMNmVlcP0tmxewnRetUmSQAT4D1BgAVDqCJ8ROTOGMetJEdY_p8YXgwF-YG7OCxBnZ2i-WSupWoi0P19EEg6W_qwLetQyil7Xseuhps0QCuHgbVKD4KnmocaXx-d40u6xiNVMu6WLY1zOHK8l3rNww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvryqQ3tAq-ex7rKZhRlKtGruYRbcagknVC4RDjUZx8N3r5BUDNTVzhDVeH__2FU7mYNmymPL7hyhokp-_Pg3PJCBRJv0nOWLZtec7j8cJw7vHMWAuZ0-Jti7fchRPmrWwOBqTMpOXmO1gVkOAcK4_MzLo_EYnxS-hnsbgMmTShNrmZ8GU-PV39RNsGyl_IIyuNGZs_A5zM_LblIT-D_XKIxOmyOW8tAIE-gvl9m5Sh_JzKnMH2oyprMwDSo8jZgiICROebRDCLZvyQEmU-zhXZ5QE_zWNDU_mT6JwsrM2w7-a5F5hqiEDiUWY1yjJjGpOQVEKQxAnjjMLN8tIBI1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101509" target="_blank">📅 00:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101508">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNTGBL0sP3AoiGK1qoEIWJPvIthZH5DlaL54Y_XyrMEX4PfDgEXyd1L162m8m-UvrIf_a6PJbDu727Ovoikx_1FdaWXRD2FMjTzeCsbu-kleDT52Qdw4kFdHoX37uW5lBiZlpCK-B7mCw-2i4lnbKPR5nmig4UK128y4OAlrAWDhFeyBopehzdDUtURPKekn2FVdaHu04cPxT5_1k4iJrTLMcNGHnFZFoeKxb8rLM8HhnDeiV7o27yMOPyOnKXk-5IonkmYr3mP0hWqMm4ZdjeAACIsccMIa9DXxUfVKB4_q4D-l4XwAoNbv0zm4MT4Hc-HWvkXFolaMceh1os24AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101508" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101507">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esC-wQZi9on3W2Ct_9rMpsEMf5VZ7RKxbmh_u1dXWMrYuSAaDBzAnJPxTSmbMd1Vv_MCMAIIo44IDwVIQGonkwjg2_9bv5dzoQVmzJJsvV7nXQMsBYyUkrRwXNQ2cYJ__5uj2RInrmZeVXIIve5G-r4mVdnzrqxYcglZ71w5ZCZ2obtn6MH4Yd5wzc1NRNsy3AjEbv7q56Fa0OlqFZj94nKKTzGBXncGFLL_X8uu07K5hcyvsQQzIA1WYB-DRuzW_6k1k2-sU9s8hc21NnhiFSZoHjo2o3VJf4b84siRldBDJFkgyJN0YDKaBijfKqkxw260Q0Sl1vVVr_8eYYv5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101507" target="_blank">📅 00:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101506">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm6eKwMBmOd_JX09xZchL5zFu29n-mfzfJ7SHwxVVUP6Muvfl5h3opT4DKa45rE9211tC4mFyac0KlKSqWBrToEHqaUi_772p8DVOWpfjuQalm0ttR28WPYqDTJYTv28bgHqGht-WwlKiNqpG_ttMNAYNIYlrQ0AwgG1nayh9U1m5JLTTcCPAVFmcfYq3AGst-7dquiNuP7e-qbz-AGqmh2PZjpF_RpFSzF8zwANiaIOaMMI-Tnj7HGQ6xoqS7hvRoqh4pEs90ihPozhAbZY-Zefazh-8eFyYF5uJLjdtI7K8bkTRoA6QyEad2UI6JqOZHYLlAGRrrwX9EoHayh7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101506" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101505">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">راجب پنجره
🔵
🚨
⚽️
امشب باز هم از علی تاجرنیا پرسیدم و ایشون خیلی با اطمینان جواب دادند که پنجره باز میشه و بر این حساب هم دارن بازیکنان خارجی رو مازاد می‌کنند و مذاکرات و میبرن جلو، بنابراین امشب دوباره تاجرنیا اعلام کرد که بهتون بگیم پنجره استقلال قطعا باز…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101505" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101504">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTLY3EhRyMaOlNekbt2A6jn0d_2W9FUaXDcCLiRP2XeJx5eDwFsxjZWjOB1MIEaAUiq2SU0CxNbpQshhg6KhWsxZQR_hlvDxRz80aLh0usp27Kr53QsKe9c7OMSNgsMSu8xhKT_rrBfCcFNVqO8wDqzYbO3kPZXIt-ReDeZ9zS7luEmxsYEsaYeHTnermfjN0JWefSxXoUm0mW7P_kaIIFDaat4vahq0r_Rrs3v-YBzkgBZjlcgDvaSXpwdaohBj7p629czWjdZuGsGcKx3rCWZWs18EyQeWSBRPkpyiK9huwVgKezCZ1WP_9Bq1XglCTz9aAIZVjxpTWgu_qUuRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان:
پارادس خیلی خوش شانسه که من تو زمین نبودم! وگرنه یه جوری با سر میزدم تو سرش که کارت قرمز بگیرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101504" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101503">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuDdECLz2pj18UmoZMHbOO2UR76N4_G0WeYsXlVZppre222s4W1A_9ytIebsUL_lQDh2pYF33oveqLnWZ0J-gov6-UTiQnEZHEGtUofq6THgJzxusNTN56ssv_34PjzzUpH2jr1L747DCxuDsuYB3dh34DY477mcwqflBXEfzkls9PimIbc7sTlZA3TKctV_cmFI1iceqzLmiMo0YHfH1FPVoiJPWcWnOmmONV8F9ykLwrGpuWQ_KtpRBGJEWcxmdbtjHhmxeOuURiL9FocclJHQmL1z47metLJdB6w64VL5E2UzvBed6xM44DEoqEZ793e9LH6kXOvvRw1JaMTpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا بازیکنان آرژانتینی که پس از پایان مسابقه رفتارهای خشونت‌آمیزی داشتند، باید مجازات شوند؟
🎙
گاوی:
به نظر من نباید آن‌ها را محروم کنند. میدانم که این رفتار تصویری مناسب برای کودکان ارائه نمی‌دهد، اما این بخشی از ذات فوتبال است، و گاهی اوقات خشونت نیز در آن وجود دارد. در نهایت، همه این‌ها بخشی از فوتبال است و باید همیشه به همین منوال باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101503" target="_blank">📅 23:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101502">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=iM1y829gr-Pd2hVsdT-E6UcHAxddYBytHOWxjHd3s9I-BbihTmTKxebGrfJu0s7l-YCE4hTgtTRAzpflFTJBgL8w2VKJ7UTDrduzeItHViG9w6xMcXz3RvcGiL9C04dxq-OeIC_HH5TJVwL54BYX29ZhNqTz8g5zlUK6TUB8VOQumEh596sq_zgiALEROmzbF_bAlgQ-pgi_wzlydgGMi-Bfq_Eh6z8txjan-efAAJrY1TFNNLnzzex4EhP1E7ci0neqgDX5chvhXUsOUxAH_KAsWS2EEBNLB2amXAGaQWnUKYo2sdsR0MEEKSHcUPIaPYEtYBwvNGSRk0ZbYBP7Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=iM1y829gr-Pd2hVsdT-E6UcHAxddYBytHOWxjHd3s9I-BbihTmTKxebGrfJu0s7l-YCE4hTgtTRAzpflFTJBgL8w2VKJ7UTDrduzeItHViG9w6xMcXz3RvcGiL9C04dxq-OeIC_HH5TJVwL54BYX29ZhNqTz8g5zlUK6TUB8VOQumEh596sq_zgiALEROmzbF_bAlgQ-pgi_wzlydgGMi-Bfq_Eh6z8txjan-efAAJrY1TFNNLnzzex4EhP1E7ci0neqgDX5chvhXUsOUxAH_KAsWS2EEBNLB2amXAGaQWnUKYo2sdsR0MEEKSHcUPIaPYEtYBwvNGSRk0ZbYBP7Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپی که از مقایسه اونای سیمون و مارتینز بعد گرفتن دستکش طلایی وایرال شده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101502" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101501">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DE1AcP4x4vP6VVyWJhi2Mp0AXAOQo-O0cb9RYyDYfJV62QAL3NE2CqnScjc130N4VKqzuCcrM864TJHKrSK3Ra-S1QwCKD93o9AorEaQPVsQI-fiQo50_sb-FG7ae5KFPv5Fe1pcxfbPzaR4hjWraEPyX5MgyT3C-Gw7s7bb_Cvz7YsNq7AqvvXGdmNa7RjcEkr1L_h2QwcI4IVImCspMv2W76UtFMq4MKwovDX3ZyhmfF0BPygWOvflcgBXQHF8i3Gwoaf1EKgGBeFoFFpOBwgl5TGJoJg7pukneNS0WucRRmhsN3mNZMjOM5LuVkWnQY9ovJKmTM62lpylDycLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
توییت جدید امباپه: من برگشتم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101501" target="_blank">📅 22:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101500">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9116787106.mp4?token=CiBZrsnS8uwXAlB_xublcCAkFWi0HxAMMHnO-KtcOcwBQOHapzsH4vSjwlWTjp9WlI7w3CPz-zOehVMoth53GWEWQ8HZXYeBwEvMWIHiwG--wdt9S_O4_jljfXUBOf_Jso0rHoOitQEWByUsytIdbFLBIBIfFxPP4imWX95-ELIAmUwSS4jcQ1enQj9O2Gi9T1jDBXDOdCEH3S_cq0Tau_851b1zmrtuBja9vNi-1Mu-EemP9ev7atWOTtCUoejKTY4fxpeaBnCiHbZbjQfThr9pju91awx0l4grNij2X5gkdv5MeI-Xuij-tfSut1_m8k5_RBtZ_YqeDWKYnnNef4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9116787106.mp4?token=CiBZrsnS8uwXAlB_xublcCAkFWi0HxAMMHnO-KtcOcwBQOHapzsH4vSjwlWTjp9WlI7w3CPz-zOehVMoth53GWEWQ8HZXYeBwEvMWIHiwG--wdt9S_O4_jljfXUBOf_Jso0rHoOitQEWByUsytIdbFLBIBIfFxPP4imWX95-ELIAmUwSS4jcQ1enQj9O2Gi9T1jDBXDOdCEH3S_cq0Tau_851b1zmrtuBja9vNi-1Mu-EemP9ev7atWOTtCUoejKTY4fxpeaBnCiHbZbjQfThr9pju91awx0l4grNij2X5gkdv5MeI-Xuij-tfSut1_m8k5_RBtZ_YqeDWKYnnNef4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👀
خداداد عزیزی اومد یه خاطره از اولین سینما رفتنش بگه دیگه جواد خیابانی ولش نکرد و دونه به دونه اسم فیلمارو میگه و اشک عزیزی رو در میاره؛ خداداد عزیزی میگه من ۴۰ شبه از دستت چی میکشم آقا جواد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101500" target="_blank">📅 22:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101499">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX_F8fvDeIN40DCmlMQ1jNsoEX-CpX1gbjYuhEtmGx7XbP9I25TzE2UJ6-RZEh_R-w549cqZ4d3ZAjaoyg0f8lcufxFMerEM7rcGXd59aOyEDnPdbNC818VF1ESHxy7hO7sEBPus_AONyCPJ0adSm2e_rKwi8SgLDvAwtIWgA8Y8gAKi9jCXPyn9HTAeQ5FfDuCN4yuqEdOmMwcQEXmNB-PwNWhSDpBi5q8uEYIaYhYiS9OSjQNNlCszR0RCm36Ds1-xNmBcoFazRGdSkUX0DWhFYGOLAQtaC-2S9lP5SSGyPysaJFm_P-CuJJxxNMAVTFD4Wu_LfcgK84JEDvgxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🥂
استوری جدید راموس در کنار لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101499" target="_blank">📅 22:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101498">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a3469819.mp4?token=njHCEZsNGDfyFvkYAw6bXa6ftulMa2pXnz2QIE-mm_eW4uKYC4ySmFRnYl5wkmmIP9Oa6MSyqXD8Vc7KpNdC3EQSvSnzV66wXeTbV3_KOMdyI639_vHLWzC-iREc7k1UfwiffmjI3DVX3DF8J4U2QwDgUfa-zs9OPRnbKBjF6otzr2AGjdJWwLm5Vv0egjyvHFAyf1_nnytWxPYh1Z_uuTSLII556VM_FNSIKxBebQIfDlZxt8v34eRccblZc51gDlfoH3dW0cvRZXZfCFFQswlxjNuJVA0Y_ESEQbjZ04P6qFxNODRrJsSZredJvmfEVS8CfneVT4IZGgycBU7Q3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a3469819.mp4?token=njHCEZsNGDfyFvkYAw6bXa6ftulMa2pXnz2QIE-mm_eW4uKYC4ySmFRnYl5wkmmIP9Oa6MSyqXD8Vc7KpNdC3EQSvSnzV66wXeTbV3_KOMdyI639_vHLWzC-iREc7k1UfwiffmjI3DVX3DF8J4U2QwDgUfa-zs9OPRnbKBjF6otzr2AGjdJWwLm5Vv0egjyvHFAyf1_nnytWxPYh1Z_uuTSLII556VM_FNSIKxBebQIfDlZxt8v34eRccblZc51gDlfoH3dW0cvRZXZfCFFQswlxjNuJVA0Y_ESEQbjZ04P6qFxNODRrJsSZredJvmfEVS8CfneVT4IZGgycBU7Q3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا حتی سطلای زبالشونم شادترین سطلای دنیا هستن
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101498" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101497">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGWcHyMV-CqVtoKDT43MhP4CMzimdu8qFfCkPVIZtwhp2wyfYPrqJ8mDnyEOQkFatPj4ss4diUqDQVoc6JL1cp6AAwuj1RlGdKJpJ4ebZs41zc_NAbyv7_1Xh85GemoGoiaTXipfhUf2hAj_7OmISsgjRFGaQ6LqL_N_pozlM5IzgT6g0KXJ0wXgTxZj7ztWQxt8pZYC9Jv6jvFBcZHXPu2xBigP-0fWJhYGF3ybNblRsGjFYJCcamMv08Z89fR-FLTFEdkTybKnLsBZKgzucx_v4sceC2-YqegMrrw28ztmhiZSSMZ0Bf8MAM4lvR_QF8TCKbHSec72FHLn6U1H2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاویه فکو که داری داداشششششش؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101497" target="_blank">📅 22:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101492">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UL1S5orZlB5sMP7ACv0S9IHN3orxbpVlGnBxOm4PTNpgJ-SGYi5RquiphuieZLSGvuOtzP662D6HFFlVYWd2cWc37cF1evAL2iJpqIAexfxRLlyxobiaQV-XocwNokygJJwzTztDHwrh6Moo-8YNXJRwiPIuAPD9tkoDlcN8X5dSRKXqwe1UUxcZdVfQpva6_8Kb1ytj9xqwpzD82Pks4r5ISYVnJFWZGr76dAqjxcJIslT70UD62gch7X9juc6rcp1rTLvSGk155NAF16fcrreiwav0RdWayMNiNxv521oahZ13I_k4BEDyi6chyMl77qcG49Hqiz2zG_aHPJOwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UeZqS-pTFMysKdZqheWR_3Jb6y57n7XBzDEP9Jmkb03eib4WKmznB7_NQfIbZgkfCQi86fUPKWYjTmaW9FeWRrFBYgsU_H8rfpQA6XgfkZR7l4A0A5f1JxmHEBtFOSijtzVK6GtVExaDSKGM84KGoz8qC-TW9v2fkYsgcLliMkuMEt79jiCysuU_kaN7OnsKGfAB2cyufe1LJlLo9mLevLrtxG1dsEoF_V_l3vrgbkKbO-NeqTVOujx3hprHhKCalVMeigXH0x3ubsZw2prUC2Lipe_qP-MwY8an1FtwgqiVuxdqFYr_vaxEqLgzALpCpBVZozeoL-JdvBYh7s-63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ds_iaW3R4-1vxrNgPzst3Z3Nb7DKlHSK-ullDn32gTmw9MCMJmWepXSA-lqOWVOf1An0kvydGYhqUltnbRskkzihn9x9vk7iypg4Bns3byRWSb3fns5nMYWY1IzxOjHCtf58pSbtZwP9tnMN1LMjgtpVLNAAIbfHo0sOJBOI5rG_CkokztgdRNhGR4VXKShCxX0Y8sKnkI8mGAwacdF2xmxgzuOJLAaa1VTa00kKt5Nw21VkapctcFeiCBcCIMv3BOreueT5UKRJr8cROr7Q0MJnEouAJ_wzy30z_BuyDcXNPsokgf0lif_tD7myfTzw_qLpxK0qM1o6o6sglFO_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbJxy90h3z7K5b6VR2N5m6FBi3Vamb83Rz_US1lNFtbMysxM5YAqlwpIymsEFJGar85FyHiN92-B8X6Tswd88Oyry2Ikn0xsLLv1bFFF-fTQDq7GS4daX4CpcOdL0jDHocWKZGTtroEBu2OgRJsraEovM7p9h8dZX09DIqYyKXeOdR-ZTPWNW0BMwr18FZY8ZRuykpUAuMz-NVnd0Dh1SbSBQh4AoCNCrkP3J04wQEY-km9IiEkIRlsWbF1CW5EOsBaRMEFOOGeS9NTa7FISr2OKFSyoD7p0tc0FNrV1vDea35jGYhlJgKWZYj_zobNHR13Q8id1E3Wr5VrfekLLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgDVfbi_kZc9EMzeowZ_qjuBacuQzMUnEZrgdTqr-BR1qLwAIV9pR09rOMVKfmbpTM58OBcdu8kQNcT1WFT-jwr257jUIJUYIpq64eSg3qpj8ns9Rd2fVkuMjZOoN5M-5mkB0QEPB3RaDJKfFTF9FU-bKNCh8x-QxsVuSNk-VViQCvcCma5fUl9vk2_JGoZOuOZoV4Kf7AcyFYrdPy1Ih4tpJuVgNNHkXh25g7dOoPJVYnXEmFfHvzHt3VZfxm3zCTufop5WFLdpWaltFFAxMTTY7yFAXLVtAmF1fS5G2FAN9hit8By1jicWkD6DQtqUqaq1HGcAYYbzly8PPBHzpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
تعطیلات تابستونی وینیسیوس و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101492" target="_blank">📅 22:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101491">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=A5kvP_4q8YgxveUWj-RHkj3dKfr26AblndL7K67DwJiHtg_p_2-SQaNYAzk22CQyabZQvUbX5w3oi7odz98Zt5O_TXkm96GM-bWT18QIHj4v-IpAkqdmYA6Wk8enGbm36FM6r_0DoMYyvoefSKLNoSijOntf4eIMpP4Z1iN0fRg2UiRRJY-3CheY2bRnzHC4qVgJAGOEYumoPmO59CVKdbY59_OayAecSmZVo1HarCIYhPnPlNFqny4NBVx3lROJHO9jZVQ3Tdrgel03cMdHCrD3PwDPNglW5htp7JrRYZt6bll2cwzLxlofqt4x95kZjG_b6bkwgJqe4fn9ylazyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=A5kvP_4q8YgxveUWj-RHkj3dKfr26AblndL7K67DwJiHtg_p_2-SQaNYAzk22CQyabZQvUbX5w3oi7odz98Zt5O_TXkm96GM-bWT18QIHj4v-IpAkqdmYA6Wk8enGbm36FM6r_0DoMYyvoefSKLNoSijOntf4eIMpP4Z1iN0fRg2UiRRJY-3CheY2bRnzHC4qVgJAGOEYumoPmO59CVKdbY59_OayAecSmZVo1HarCIYhPnPlNFqny4NBVx3lROJHO9jZVQ3Tdrgel03cMdHCrD3PwDPNglW5htp7JrRYZt6bll2cwzLxlofqt4x95kZjG_b6bkwgJqe4fn9ylazyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"اصالت یعنی به ثروت برسی، اما حاضر باشی هزینه کنی برای کسانی که سال‌ها از آرزوهاشون گذشتن تا تو به آرزوهات برسی.
بعضی‌ها با ثروتشون دنبال دیده شدن هستن ولی بعضی‌ها دنبال جبران سال‌هایی هستن که پدر و مادرشون بی‌صدا از خودشون گذشتن.
شاید ارزش واقعی ثروت، به چیزهایی نباشه که برای خودت می‌خری؛ به لبخندی باشه که به روی لب ها میشونی و حمایت ودلگرمی ای که به دیگران میبخشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101491" target="_blank">📅 21:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101490">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbXO0T5AnZiJHN2EWV3cMV4klhLXw6Lz67aa6eWnyjPrIrGDRU6vdeWLCb1HFKZOe80A_MRVrsBvCFcMEglwOS8xX3Vz3fsspe16Zju5wBTOAtnFkgtvI-GaCmyG5jjfo6acdmPNDEXBDvW28PNvaYi5lX_yj9owdmOgTcaw_jMab-5ev3_cm05wfi0xYWes7drJgMQt7_CP4P6V6mQfPVXTcMRVLQs4JJENV076boEy5Z3E8gG1sKwtCSQ_SFqIT87YsUr2OHPU5yr2eScmaC5EgD7QdPC00goFVm4TmSVZOWEiiePLg_PdO4HDqvPCbmYYq8BB5dIf9CWyB5QMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
تیم منتخب بدترین بازیکنان جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101490" target="_blank">📅 21:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101489">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II4kIKQvIPvvlbbnN-r67njtU2yH2RB-vVHvFXMqzpxw5RbXdwDghDXZWj3yxlkKIOqXkPA7lgfCQJ1AQ2SMinYt3sFjlY8zOjmSwQN-QqvbPuECcIKi_fSP_cr0vGmpVk5xFWKWeqnJKAj9ZX7J4GiwS19kzFtgI0SkK7utN0s_XBiAemg6X5BNqR7qFNaBiMMNbZEAL-jwd1uXKLrG6DU0ElVMkWVJRa5oZqwd6uYAB-MJQ_fwked7t-ljqUq2zgj-J4sMloGkJhX80lpY6xPp52RuIgAa40OzqgCV2Hm-DpyUoBlN2xnKljwThLcQoJ8DNr7UzfTL43Hqt4VCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید وینی با چونه جدیدش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101489" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101487">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEhFpFCZLQOOKX0MdYBezieU3pSbCMS9f_4XM5OBW9BPejh43OVqzjgBSHif0z4FPIk7PbPw_-Z4ftwvnsYXAT7LidybZ0TgZjXLqjCF_Me0Y0J10j-2gvBv9XAnKpl8FXbVQxXwnr0_yWHFADCfw5q4SF0ZQAhM41FlPNI4S89yRT99JSPdP-bwQrcAEn2EQHZe6Wk9XA8aa5RoPKHVIqbHahEDMevp2BFmHUV-O3gLbGrVKuT_C_OUiQQTxlgSxDD_mYVsHi4QopfA7EIl5oDKMfVdNDUekwwZ5Ng-8JX4dA1pALjIxY_PsJzaNop0irHMK_jaemdMkCu99k83YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان فصل 2025/26 در میان باشگاه‌ها و تیم‌های ملی در پنج لیگ برتر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101487" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101486">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjUMoFYzeTuFZ7b_PQWwza-vI4Hnis15MwOrrCeRGWBGfm5g9jawDYaNIaYlaF5J2nu1X--YoHlGxGodZ7Aw1oRd-ccm-7gGaaYA0R8rHM9juLB2rqKZNQNu4ZVfGracRkaefdbrPCIOzD-9lRMNIZPXtfz9IlwmoFMHE_n8fO7r76dum8y6-9ol1AQr2rOtdzO-q4s3EAVNjCP7aJCiTqrzvEBqPJYxiYgKToKCQzqAwg8j8_MaCqscPzPoIuu0XjHhEPZl3MsQZKqTj2gBSWG_aqmexjssAhj0ipSFaw0Hv97vRKR3BHv8ILz0wrNRBxCl5UitMuZVxCw07Z8FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رادیو کاتالونیا:
🔵
🔺
🔻
لاپورت جدیدترین بازیکنی است که خود را به بارسلونا پیشنهاد داده است. عوامل مربوط به بازیکن با لاپورتا در دالاس ملاقات کردند و ایده حضور در بارسلونا را مطرح کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101486" target="_blank">📅 21:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101484">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duvjz3_WyE6LyJ-uaQFPvNHvO1RbBv3RaNMBAk909MDBoaCmqlgrrbWSPQ-MhsfHHnMxIMkpkZrkP_522geXQVGulnpnvpL7ASbto-cEV5XIuer0saOgAxG0nZDWncN108fGPjuoY9a7_iGSuWgp3UCGg2pzHTKRyt-OjEsRN7DDb0Jk6MA6h8pACI0JWdEK42WXfntx91cBb54foWOhL7ctomOCRpiI5NHIEoUdO0YEc3zeyFK9k64LJZzmFdkle1z8xdAkq931qU-EsXmGayeIRlW8fY-k7IUV9rjPpkMFDKrh2Y1s1pOA5Nkbdj1oLiy5Cc02oHxR492KJ3pDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYteRxsCKP-aCCrHDmqfiKarcLulxm8anXv-xZtrqJFUWhp6R4gsMcKRbS_EgabiJoDt5BWGf21Ga4U3hRyHbxngCpMIkapvvpzboSv2YB7FRzxcFWTx1msVHFsPLqA8WQax4J_lJsONPgk7VISID1beHe-H2LejdZA2L6asOzfCXxrtDljdm2zgAjHiVzKqSH1zrFTPEPgnDnSRpCDXkkhU-WsEALEORupGc5pSMlEgfFAKNl9ycncrA8jro8oSX-Q7RrlE6rTbd6QVdAlnXcAzgPNgbmel5WTJ6mtEJgEFUl3hNGtTVnT4uAAnpplIFpZDyJd543__HiX8RLaI7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😁
زیر بغل شکیرا از آینده‌مون تو ایران روشن‌تره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101484" target="_blank">📅 20:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101483">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WebFrH-oYJ4ZY2rbwJgT59g1cZfXdaLg_xJFazj5jCdtzSxM6AcdLEY-9nzt9IyT-xIvSKLr_hqtNH_avQ4rEUuUgA2Hdnr4POCWcUSdlK3ELZwCMBZohHmKRbtbWf5k24-Qf1p7z9uvnhytfInCaf70Muh61MpVlVhHCHnU3VcraKim4vD3Ze4OQ7d2clDdqh9_DUbrCFbHKGRkKhbq7pux7LynOsFlfPyDn8nnviSeXCqSPUVjdd8K4qH42zzocRXstr8sEKc2pwGEiIaqNcR1E_syorii5a2drHj86-_cPrTTwQEqZmKqrKdkHxVpAG8qs84r7URrzmDS9cnf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
فوری از فابریزیو رومانو:
🔻
لوکا مودریچ قراردادشو یک فصل دیگه با میلان تمدید کرد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101483" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101482">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMPYEotr22u0ypxw143waU9IUAxJrWpBQ5qC5spBgQgxxqepvpC5jiPuRK0XqRIF5qftmFKHO8cDjEkoNIxBMtqCrsyAsfFYqD3eGDt7JQJavMW-D7qpkNOZu06wM8Vr04khwkLXsYq1CbCyXM1a94kjZI1m6JTrz10yxwDCNyd96mw61xKRr3Lbgr0iveHypWvfYXlT_vOaxAP29_zwDYqBVGpEadYMDsA5yrZ7bB6Bi4CeTdB2d6epbJu2du3jx-VGBLgelGJZVP0DP_WvyCJdAnKl_F74Hn0QeS6F5-kIF8cHq0OJiazkschKfom2neOGKKj_zAS3gyo9anorBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
||
بازیکنان جوان با بیشترین تعداد دریبل‌ موفق در تاریخ جام جهانی:
◉ 27 - لامینه یامال (2026)
👑
◎ 22 -
کیلیان امباپه (2018)
◎ 19 - جمال موسیالا (2022)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101482" target="_blank">📅 20:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101481">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it1XcWBp1cb0IyLBAZKqjmL8P-LQYcn5XNdeGV80SBXwynH62tTz_WGKrtNcgYNUmgNtXl7IC5hk_ittmOoH4Gs7LUSJHBKtS7BboK-0heRtvgbFvQMTZ6I1cSt7Yb3D2wC7uhJri3siW7YqVQJVchPJif01uOpcTWYwyQfc_0IUhPfj9vs1OS368JrA1TSABYJf4eV8AsxvEUUVzfwWYAa-wBkQncYzXYyv3IBa4SLGQKZyRxHfWRGzQvkDKfw_AFJe_JTPKS_LR2kbo_9u-ytmPFQgaNO6K6ovdF5Qzdn2nyLoRvzS8wyBDX8evkKliGYEwmqT4UjcRe3NvNbQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه کاور EA FC27
نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰هزارتومنی برای خرید این بازی خرج کنه. تازه اگه فقط بخواد آفلاین بازیش کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101481" target="_blank">📅 20:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101480">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFdSzR5A90hHtl0-bZgPMkC1cdnovCyH-5kc3hxM_FwzrR46yGT72Ws6L7yBqyoTVxmIUvYIC4WnrPF45m7rX9c-_UwlplSP1v_GinolZbKj0DWmCgF4sG0L27GsR9AjObW6I5RRJWsygdxlCpe3OrptJ4c4ppopCGRtsjWzDK1zjFawlX9zu7cLzhEFY9pkv2VtJLtMgxX_0KMaojohXrn8Iq3wBrLVk3iqPkTrzNAHpukBWNfpqU1LroK7O-0gzkP0zg27LOhMjYTs_2mtqNWVIHZ42RTiFvzv-Y5TMSsFwPlewllKu_5wyT7Qmy3zM-fmmJY7ot9xJzeEip6_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
گلوبو برزیل
🇧🇷
:
🇧🇷
• نیمار تا ماه دسامبر در باشگاه سانتوس باقی خواهد ماند تا قرارداد خود را به پایان برساند.
‏• در پایان سال، یا به یک باشگاه جدید خواهد پیوست (اگر پیشنهادی دریافت کند) یا ممکن است از فوتبال کناره‌گیری کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101480" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101479">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=aXC-dCy7iU7miIEiPF9dkGRQVTCW1UNAnQAlxNgOU0W0peGmfrjrn8rov-1bcyduw7BwyB-DX9tJTZDwDuigCwwjKxcZcR4dEv1Max7V0TMCJJibMZKjdEz3Des2c3O7oZ_WGxNrOn7n9hmnWyghv50touS84-Sf1r3cHUDJZYSq2-PBoIQSDr1RtoNwqp_pONU-nHp8S7wHLaRQbhLk2QwsBral3ZD_1A2To-o3Hi5whxXu7Dp-S3udVWlD8RtdAH2bbmslQXf356vI_8Q0Z0g9y8VKwOn1zl2F0thZXkxCtQyEHacbA4Y4ph-Q_Cye8hbDP5papOzt-msxxS29LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=aXC-dCy7iU7miIEiPF9dkGRQVTCW1UNAnQAlxNgOU0W0peGmfrjrn8rov-1bcyduw7BwyB-DX9tJTZDwDuigCwwjKxcZcR4dEv1Max7V0TMCJJibMZKjdEz3Des2c3O7oZ_WGxNrOn7n9hmnWyghv50touS84-Sf1r3cHUDJZYSq2-PBoIQSDr1RtoNwqp_pONU-nHp8S7wHLaRQbhLk2QwsBral3ZD_1A2To-o3Hi5whxXu7Dp-S3udVWlD8RtdAH2bbmslQXf356vI_8Q0Z0g9y8VKwOn1zl2F0thZXkxCtQyEHacbA4Y4ph-Q_Cye8hbDP5papOzt-msxxS29LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
شیرین‌کاری لامین‌یامال در جشن دیشب اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101479" target="_blank">📅 20:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101477">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=MPv5J6X7cqnX29PGW08xG36MqrwX7tDr-Ze5Ce_sg67ceTqx5xAijK8WV8RegUX_VKbiolglB4G5WwrFO0TX8iHnwJ2krXZiBN8ucYU_mrBZLfr9qJw-rPXkBujZ6Ucr3pdfzjb5PIorTHpLohT1T823RpsWCnPUZ_wguTUzsI3ZOcaEOQOybjrkwF2FJXdJE1px7Cxr4SQ4E4rubRYfVwEnLkmxl0oEJwm-wrO0CmjhpTFk8TKBvCHNqn5ybFAmpLUhbnNHbQk84PGoflfSQuzkojcnvZCj1_sbjlISSmak6pdmBwIG8IFNqDt75WH-3x5JXt_fxUTFQvccwOaE3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=MPv5J6X7cqnX29PGW08xG36MqrwX7tDr-Ze5Ce_sg67ceTqx5xAijK8WV8RegUX_VKbiolglB4G5WwrFO0TX8iHnwJ2krXZiBN8ucYU_mrBZLfr9qJw-rPXkBujZ6Ucr3pdfzjb5PIorTHpLohT1T823RpsWCnPUZ_wguTUzsI3ZOcaEOQOybjrkwF2FJXdJE1px7Cxr4SQ4E4rubRYfVwEnLkmxl0oEJwm-wrO0CmjhpTFk8TKBvCHNqn5ybFAmpLUhbnNHbQk84PGoflfSQuzkojcnvZCj1_sbjlISSmak6pdmBwIG8IFNqDt75WH-3x5JXt_fxUTFQvccwOaE3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تایید دریافت پاداش میلیاردی از سوی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101477" target="_blank">📅 20:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101476">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgBAhKjzdk3l1JHce5eUaI0UFzqOo00tDAAtciGWHA7lWztdBJbKQxfpjkhwTPKd_gyS7i0qaQXvXOf-c04BiLrLuhEqnTndcKW2qgk3iIx01n7RZMgrN8e90eJG_Cik3q6s0UKsZ1lokrdqjC7rLGy4p04Qu7NlE03PXz_SvaMJguZkq_mm6Ui-n6CMQW5E0iCXJdqbEQ2pJ1xw4ZFHtNwgTZi0c7knL8tsDbF61Y7gBM4wZQIOUNZwD4ACKgJjW92W8Pfh7HXJOfMaufJP865grMqYKK3IkyZvgjHVfnBVpMBefnI8IwWa7rJPa7wQg0VfJDYMGEKBzWrQED-Hxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بازی های پیش فصل چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101476" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101475">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=mn0FRZ6PmHsDv82ul5AP0tJ8NTXCPFkXrc9oZvVtgrpYnCbroM1iRe1MxHL67d02I-EJtBrxIYAIhcuYycqKfrSJLW_fLjmQeObsxYBOonXSCX-ZI4tbuYy8xb2egD3JOMAk0tVtpMaawZqcM1copcOVXUS-GIc_dgGSHOlfi7-IMP0BkzmbvsEqFtYqCMMRIbmAOFLk1XFyvZpShFkXgnkF096WVYKO534AWGIa6WPYaI7Calzh6cXSmws7xZIYQG4r02jmSMYp5dxVZyQCK4IkJK8nA2q_M3rS49Ec_uCHFjkm4P2GhvT7nwAeKuUwly9mPZ8zZwpPVegf2b9AmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=mn0FRZ6PmHsDv82ul5AP0tJ8NTXCPFkXrc9oZvVtgrpYnCbroM1iRe1MxHL67d02I-EJtBrxIYAIhcuYycqKfrSJLW_fLjmQeObsxYBOonXSCX-ZI4tbuYy8xb2egD3JOMAk0tVtpMaawZqcM1copcOVXUS-GIc_dgGSHOlfi7-IMP0BkzmbvsEqFtYqCMMRIbmAOFLk1XFyvZpShFkXgnkF096WVYKO534AWGIa6WPYaI7Calzh6cXSmws7xZIYQG4r02jmSMYp5dxVZyQCK4IkJK8nA2q_M3rS49Ec_uCHFjkm4P2GhvT7nwAeKuUwly9mPZ8zZwpPVegf2b9AmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفتم قبلا یه جایی دیده بودمش‌ها!
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101475" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101474">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101474" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101473">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_1XW61mLLOUWRSWfRaR-SlOmAhMu7Eado_h8paXapd7vcEz537gG9Ir84Q9ujxnrjd0UEOwqfhf21mJx71QXXP1dAXPaGW1m1pTuJopW44AYZuXPhgl-tbzhjvlZg99GG6xwvmJegSb2tCCReDE4WocdCpTPGOc2O7d4y4PCHw9SGmTYhxwC7eM9nMlztl9AD4KlEIGiLYjFgUqRuAe0eQ1y5UqjpDpPYBgt5xBeeAop2W4cnd12GDUK7mjxTjDs4Al1rH7c28hAF8ktxf7vMI6hTAGC3eZckLjgouj1l0RNhcC4aEfk3Xiqyeo6Q-b-9rqM0Z5NvyHwTf6bOatew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101473" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101472">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=i90N-d2zlHotlEG5IBb621GKVL4-ScLHmaqIp4M2a56PA-Na_Fy_NTpIX7FlMRxy4NrDcnlWKriIzl-LM8GJzTnR4N-dhzkcZor4JTZzdhK6fF2dgs04gSae0aw2rvYOXjYWyaqBCFTzcC3W8bU0awLX6ecQonkt6IUxPXQY4Ck5NVQ4oYZll41K6H0Df5hrp4YslwTTSQXtfa3FuNs-yBmhFOEJRF45M27eQplqwczEyaAXU-7DMPYnlnmhMKHIiuOR9QTLkbGef-KH6oWQqZCbb3Q5ChxplRpRO36XLKJUmVBHnSZ4SSCxYrew4mDkI7lCnU4iRk2x6Lg6-sFb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=i90N-d2zlHotlEG5IBb621GKVL4-ScLHmaqIp4M2a56PA-Na_Fy_NTpIX7FlMRxy4NrDcnlWKriIzl-LM8GJzTnR4N-dhzkcZor4JTZzdhK6fF2dgs04gSae0aw2rvYOXjYWyaqBCFTzcC3W8bU0awLX6ecQonkt6IUxPXQY4Ck5NVQ4oYZll41K6H0Df5hrp4YslwTTSQXtfa3FuNs-yBmhFOEJRF45M27eQplqwczEyaAXU-7DMPYnlnmhMKHIiuOR9QTLkbGef-KH6oWQqZCbb3Q5ChxplRpRO36XLKJUmVBHnSZ4SSCxYrew4mDkI7lCnU4iRk2x6Lg6-sFb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
حمایت رودری از فران تورس در جشن قهرمانی تیم ملی اسپانیا: "شاید بازیکنی که بارها و بارها، ناعادلانه ازش انتقاد شد، ولی امروز... امروز بخشی از تاریخ فوتبال اسپانیاست!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101472" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101471">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=IH9bXX4uz-pcJRhNbVMplZCg4VMcrGf_qpxvOs6saOMuU1eTjWb14sXdb__aJNGcaDu7cZxIWkVBvi26WWgIsuJTkEHvHKtOgqEKXyJxg2mT-8H2ZQW_HWeEUBxELM3m_W2Hi-Q_gv20sN0gDC7UIeBsPXcE3CN6r7GZGisshErsS3Cs7PNu4TDy5uQe_b1CRcwMiQLTWnbfwdAyFrzSHMx4D_xTMzO6_epNTYfs6-FT0MXmxFhzUNE3JxP5qpuWBAk3TP6XowaH3ehEe5Eez7UaTS4LXgPjlSALDJ2hbmmehT0TpZJqyCWelmC34SX1NlkWFgGnoQuxjUgAXCaNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=IH9bXX4uz-pcJRhNbVMplZCg4VMcrGf_qpxvOs6saOMuU1eTjWb14sXdb__aJNGcaDu7cZxIWkVBvi26WWgIsuJTkEHvHKtOgqEKXyJxg2mT-8H2ZQW_HWeEUBxELM3m_W2Hi-Q_gv20sN0gDC7UIeBsPXcE3CN6r7GZGisshErsS3Cs7PNu4TDy5uQe_b1CRcwMiQLTWnbfwdAyFrzSHMx4D_xTMzO6_epNTYfs6-FT0MXmxFhzUNE3JxP5qpuWBAk3TP6XowaH3ehEe5Eez7UaTS4LXgPjlSALDJ2hbmmehT0TpZJqyCWelmC34SX1NlkWFgGnoQuxjUgAXCaNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
امباپه و اکسپوزیتو در میامی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101471" target="_blank">📅 19:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101470">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1SJEK-AL9M5e3moAli5pPv9aCb8ceVu3LAmOCRP4_iUmlnOU3LODgZ0EeQpoWNtdSuVCJG4siuTuQ7HBTnoIn-Hzwp5_xpxqnxIhw8CasVSr4uo4QoFm96jvBqSWPbfY3650dbKQYnTS8nu3Bn4wSaYl0Ru-MJUyvozEKMfleBEnhrzZ5elgc0tL6UuDCJXXb16W92vSJSE1SF8WaMwPtQ3vthAKZPeakyUhFssgzF-lzuXQADE_MIgXoxiZqKVEVC57Os5Y1_6prN2AXSAHNpwayki25e93QGB1aZ3dmEeERRme_3EwQ3Qlq1pFPPbvYoOZuVeN8lS6nyUdMBq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه حدود دو سال پیش با دختری به اسم فاطمه وارد رابطه شد، اما بعد از جدایی، فاطمه باردار شد. اولیسه اول پدر بودنش رو رد کرد، اما بعد از تست DNA مشخص شد بچه متعلق به اونه. با این حال، گفته میشه هنوز مسئولیت پدری رو نپذیرفته و فقط از طریق وکیلش پرداخت نفقه رو قبول کرده. فاطمه هم پیگیر حق و حقوق خودشه و این ماجرا باعث موجی از انتقادها علیه اولیسه شده؛ تا جایی که کامنت‌های صفحش رو بسته.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101470" target="_blank">📅 18:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101469">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=Zp15kol6Asidzxm6N5-w2zbS2POil1FnT2fZyebRGEvgIFRSU_kdafvOwrl5xbqkEdtVxZdWryR_-1N0JIRaqiioFZqWKmJOdqKu2t43CPWiubsUC2nuf6MHZahgEzziPAOodj5If1IpB7RUQOaiX6sXhtYuubQJnVbZ72HhS1XxgbTVprtAROdwTCRaOIJsiEsrmPN3afICyiXklpuojKeYz6KQVCv6dLrcg8Z0SHMQOy14Dag9gzEjDkyVJEkbSvZLbZxANkK9q9QwCyZP2NtgVHTlMGvPgrO8_QgcV75gO6FkpUlWIVvdA3yaIgI0on8RNmnTtPOtYnFmJbbYlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=Zp15kol6Asidzxm6N5-w2zbS2POil1FnT2fZyebRGEvgIFRSU_kdafvOwrl5xbqkEdtVxZdWryR_-1N0JIRaqiioFZqWKmJOdqKu2t43CPWiubsUC2nuf6MHZahgEzziPAOodj5If1IpB7RUQOaiX6sXhtYuubQJnVbZ72HhS1XxgbTVprtAROdwTCRaOIJsiEsrmPN3afICyiXklpuojKeYz6KQVCv6dLrcg8Z0SHMQOy14Dag9gzEjDkyVJEkbSvZLbZxANkK9q9QwCyZP2NtgVHTlMGvPgrO8_QgcV75gO6FkpUlWIVvdA3yaIgI0on8RNmnTtPOtYnFmJbbYlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه‌ریز دیشب رضا جاودانی و عادل فردوسی‌پور به محمدحسین میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101469" target="_blank">📅 18:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101468">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3BeFVtf-s7bfqxMNtE0CtVx2sZ0-b5I4Uvk2Ikd8zznP4N2zbdxoAzxI3gEr0hlDaXecc2M8HN8Q5HvOf6B3c3uceWU7gpROKtUfePWqVZGUBuTZVY4jP9YK8V7lh_FDc9mtJLgTb9xkf5Hzd6QehXEVyx_ai8YsfLMiod3kPrKKt4G1EShENSAnKs9nJ7XyuQNAnWVfoUhZxmA9EAXwSLAXNU_B9SN4hzZlILe3Tbiw923ongD877o74xwKzWZSlQs97BPbdKElRUrTlWgWb4ipOuWAnutjvBWmVGTaCKAfuuwyoHfGtU_yiDQh8HfKTGxDmisjR4YPPVgXcDumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه روی جلد FIFA 2027
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101468" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101467">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk0L2h2lbKy9HVFpv4hLP0GD3I_upzTfFoHr0x6AFmQlwL31m6TVIKjY7LHuSj-2jJqkXxP1CXedOpnTHIj-Puasnz5AN6sMIDbiROCndtKYJCvRw7JGpkGB3nO5F0rb2zXjnGiqFD_19EKBup-uXwfSQ6TxRH5BINIyPbakyCLHOiXe1J5GIygxFELWJbpH7bPgBf5hjUlWbqlN4eEE19Vcc3W5sgh8e2Z_R3x-y7p1ynk6avpTZdrL7fa1CHlM9E9Gs7Or2nfZKzvV_vPSAn7hLx5rVe5H2U9s-89_X-JnzvPbbh7Hy5vpTWDIk4JGDyzOgnruFUufDWZfFGBkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتونی تیلور، داور انگلیسی بازنشستگی خود را از داوری اعلام کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101467" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101466">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhpWQxbCdqsUPqed0prjxvaGc8jNZoDPLpCDC1BMuHq1UNkOb5eeDvxP9RnckeWQhE7UOdIiY6eWPaPPi1sv45fOXO7g57xRoFHW-uarkQzEQLnBq5-RCqg6IP7gA-KwbLg0BIR089qbClux1IDOXsL7zV2EFoIUs3odytac0XnGOJvKOobzGCShwezxnTYscMI1zWdCYg4Mbg9A7pouHUbU9dV2PEpXCRVsfs_0YcKSq-QRF-0f2lEDs8N-DMUgk8jrXD13snj4Zvv2K_GBim4as-Gp1ZbHkM4GzRwxelQiDPTujuO-i6mD6r5gTl_wAY3BFEePlK8dWlu1WXB1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ماتئو مورتو:
الهلال در شرف تکمیل قرارداد سامرویل است.
الهلال معتقد است که پیشنهاد بی نظیری ارائه کرده است و امیدوار است در ساعات آینده همه چیز را به پایان برساند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101466" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101465">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw6d0w71nAk9EwNt9MAFkRjHGoUvD0j4aWdCW7zU3NTC4gNh-Ed8GBe_BsYPNRUgRPd0RnUCz_TV9C3nEK6Y1T9o2NTpiINAZWP5iHCACAKpxHP-naVLpm4Y_xlggb35CupEHIuKxBtmQmvWWieN_Y--GfQXGqKVzAqjON5nRJDlyvxs8M9J1JzMjrHkJvjwkiW6m7uKXX8_wbRtNskF_fPa-nHK_n2RV2A5_N3j9c6RQ8rt2WQxWKdBiNF4HPzzF2cKzd0jIsdX5KJMD1qB1PBoRmtH3D454tL6PVwm6A48MWAPKIDLdygeIixcuVE9aTIE4nxbqVVhzzT0tRgSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
تیم‌قلعه‌نویی پس از درخشش در جام‌جهانی با دو رتبه سقوط در جایگاه ۲۲ جهان و دوم آسیا قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101465" target="_blank">📅 18:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101464">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21557090e.mp4?token=Ym3-BB3BAoNrjzHaA2RBrbNGDi2A4ZYMgSMStmCz-6VLDBag_l_DiI_5ADsFyih2uUB2e_Rp7f6btjw4ndtKxc0g9ODkAZikes3JeHON4caAl9aJmUWGzvImt6kB4RSd4JwjaPwfnJ6msMO5nYYotUjEd6zuL86Hs5AYDxWfgep4HvlQG4MYAY7rUIGBMAAHvvDj1GVjhZg8b-ml9W04yxKkM8Y4z3FI8Egnybi17z0cFJ8lsHfb2NAd5KYPijS-Qav3JTB8E5g4CCbd9XHckuGpbBhN2XdBGTAnnmwGsLTbTbQSA0-T39XE2PgPr319RPK3Cn-UgIz915XjwblBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21557090e.mp4?token=Ym3-BB3BAoNrjzHaA2RBrbNGDi2A4ZYMgSMStmCz-6VLDBag_l_DiI_5ADsFyih2uUB2e_Rp7f6btjw4ndtKxc0g9ODkAZikes3JeHON4caAl9aJmUWGzvImt6kB4RSd4JwjaPwfnJ6msMO5nYYotUjEd6zuL86Hs5AYDxWfgep4HvlQG4MYAY7rUIGBMAAHvvDj1GVjhZg8b-ml9W04yxKkM8Y4z3FI8Egnybi17z0cFJ8lsHfb2NAd5KYPijS-Qav3JTB8E5g4CCbd9XHckuGpbBhN2XdBGTAnnmwGsLTbTbQSA0-T39XE2PgPr319RPK3Cn-UgIz915XjwblBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم چه حرفایی علیه مسی و آرژانتین میگن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101464" target="_blank">📅 18:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101463">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">😢
تمامی سفرهای استاد اینفانتینو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101463" target="_blank">📅 17:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101462">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4ba1VhD2iGzdlO0CD2YXypc_nsdiiCJkbqjPBecIb8SqS7tOpEuJPTnp3wgX65BSqQ27s6tfe5i6GOlNniG0pCuVgegRWvWV3pfzXTqiEgU66ULRTSSCh9j6uowFPlbmGJj0c3f0KyVDcvhqzQP2VQjmmfLoEK-ZOjbBPHQYK-790a745viBQXxwiqjol6PiL6pGtGfPVRx4pODBUd8O-fQjJPdBae-Q07nfe60mxdJLF5Cbn4yHs5dAIxZVHngWSL9c14UTsYw6GFOcJEanoekqeD06oy4iQXs1IfQ2ButBirZhuJX8T3zFPB9Orheo9_ch0wf2Me4bd1OsPDhRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: استون‌ویلا با ارائه پیشنهادی به چلسی خواستار جذب قرضی گارناچو با گزینه خرید در آینده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101462" target="_blank">📅 17:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101460">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-KWVnA2YIXGLDdul_ADCdunqTzLBt9jB3D0TxtkkTMD_UPRLSPSWkhwCRY_yhOhMLlnnntw_qG-IZJQBzUFFucZzVSzaFDqVk65P3v4RX9rwZxzBm0PK3RnPgO74nZRRY7l8cGCG0N4r2p-Nm7fOq0d3jLn-Tl9bijbJsqx7vHsu0B-0v_wRQSkTvxH3b2Jw3eFJvtQy03jR7rH35W4F0JLERajZsyni65AWSFR9X8-54ju3xzX-utwGHZUIAgEL9a1yJnWKxoTWDxqvENlAwEjf5tPYonsgZjDwp8k7wpDHrNgrRtcQCjM9UBanlX9k3PoYgWJfV83TiBsWXCq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJXjEuvfUFYWQIHhVj8Ev5JHBDfNBboq88zrHouifXYhGtT-qvZMVUtzmLPIgBMcVx0Off45NJGfsUQ3bKgK0KT40E5UmT_UfqKquOoWSBp2zTw-gplGoeCb1KlF8-W6lNd-wdCeK9UxbOgrUVG3wkCZTvXiQeIk0BUV1HJCyt284yd8DY4NErdz3R7k3dkIjmQIwwcf7xsMOeu88XrPEIpasN6GRmBumblO7R3GZRCV-Iv8R5EUWcChgl9R7kiAdxclbHYf68yOxSW-0Zcvqe4OaPHYkm0ZlP9bmpWE2Lv8LMlkhkpWcDdN7uIU4hp5H9HZj0RqhyMzOFXJ2nrgeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصور کن ۵ سال کنار یه نفر زندگی کردی و خاطره ساختی، برای آینده‌تون نقشه کشیدی. بعد یه فوتبالیست با ۵۰ میلیون فالوئر، شهرت جهانی و حساب بانکی چندصد میلیون دلاری وارد زندگیتون میشه. فقط دو هفته طول میکشه تا اسمت از روی صفحه چتش حذف بشه و جای تو رو یه نفر دیگه بگیره. چند ماه بعد، تو از پشت تلویزیون داری جام جهانی رو میبینی و اون، کنار همون ستاره، تو جام جهانی از کنار زمین لبخند میزنه. اونجاست که میفهمی پول واقعا همه چیزه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101460" target="_blank">📅 17:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101459">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=M50jPQS2gthJcitNI-ooSX6Da4PZPbR3VSV6KMuEqHAci5XHFwHuRN7TmRtoxkURdexW-8a1BxIrCQI6TEG08lO_1_QBwFxSwWknW1eU-uHcKodzhFPBf-OlSxPbgEeSFPoiId1vVQV3iIQDW4Wwbhw3hGN1KXrWGAFZLiLXGn6osaUquH9hVEmwOBbsameGXfmZPgwk3mSDHG2KCKnQTOXxvLgh4gdR0He0uh1XbPApfgmoz7FZ2wx_D_wq-F7ljOOYA5upWNsXw5yXekLC40041HjDJUk0r_au8WPmIRyQpbOOHOER9bBUYNUAB9nT3sq4i7jECEi6ZWhqMIphu3d1PnxHbDqmm-huUeIpBjQNY1QiXdUP9l5xynVn8v_FI7gaBL2WUPsIAvaz-ZYSnz9UCo6cuTJltEdAReNQYAoWsq4DwjpUXZMeW_RfIzT348q3TNu8XySFhMP-nV91cvLBPlqcGSf0R4sMWTvJMvAWb2ECy0bu9tO4QMvEQ5Gi8SCWwZC_WRwAQcsYCNIO3ZUBnCRUbZXtFOc8voAREBCPsuR1_6_YolUTJNV7YVdrj5H5-TjQ0jHEBeGM97GCSXI8V_Uf_OFn8iqM6RbpZSDGIV_vyEikSJh9YahSoea7JBzz8k607QCclUq2j5nMSWQWGIG4HOIYHsFtag_OuCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=M50jPQS2gthJcitNI-ooSX6Da4PZPbR3VSV6KMuEqHAci5XHFwHuRN7TmRtoxkURdexW-8a1BxIrCQI6TEG08lO_1_QBwFxSwWknW1eU-uHcKodzhFPBf-OlSxPbgEeSFPoiId1vVQV3iIQDW4Wwbhw3hGN1KXrWGAFZLiLXGn6osaUquH9hVEmwOBbsameGXfmZPgwk3mSDHG2KCKnQTOXxvLgh4gdR0He0uh1XbPApfgmoz7FZ2wx_D_wq-F7ljOOYA5upWNsXw5yXekLC40041HjDJUk0r_au8WPmIRyQpbOOHOER9bBUYNUAB9nT3sq4i7jECEi6ZWhqMIphu3d1PnxHbDqmm-huUeIpBjQNY1QiXdUP9l5xynVn8v_FI7gaBL2WUPsIAvaz-ZYSnz9UCo6cuTJltEdAReNQYAoWsq4DwjpUXZMeW_RfIzT348q3TNu8XySFhMP-nV91cvLBPlqcGSf0R4sMWTvJMvAWb2ECy0bu9tO4QMvEQ5Gi8SCWwZC_WRwAQcsYCNIO3ZUBnCRUbZXtFOc8voAREBCPsuR1_6_YolUTJNV7YVdrj5H5-TjQ0jHEBeGM97GCSXI8V_Uf_OFn8iqM6RbpZSDGIV_vyEikSJh9YahSoea7JBzz8k607QCclUq2j5nMSWQWGIG4HOIYHsFtag_OuCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
نیکبخت‌واحدی: ۵ ساله پارتی نرفتم و الان دیگه با وجود هزینه ها نمیصرفه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101459" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101458">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=DawvwROLCKLp6qQuJ8yyjuemLrm54RppkO4ii1Yxdsmpg9NMZwZqVs_s8z9Sq2sYC49FcYbhqB9L2-lBgI85Q9J8uNmNgYr_61wdSybbGOi6oUX87Lnv9itN5tN9jjpOsWEfq1bwL9C-T7xoyzK3RR2SDTOwedB0j8kslOAw82ffnSgSliA2lwETeaiFCbdHlJhSlq42_Gz1sgepjO2N1n0EcF5FjavSP01hqtvglh8izKwuZbjQd8BiMKgwJZCsB-POVq8zYt_o5JPy5S2bfPCqQBTwAbT4rKGg38pfK77ojjINn8fKAVlAWzin7tw1_dUL8x-KEwbEDvTnyY_gwL_xQOi2dZqRLSV90F0IDfjYfvuDGLH8UeXEf028TcmCkBYWZPvI9vr6cwMrZ260XllRryjP-Ox6HOxX7sU7-tPRQvPBtqAhTGgFjuF-08JPscpQaxlYZHSLDOW_Hrmdz19d5-NjvggvPZdJ16nc2lB378rEtq72LEeONJh0Q50c-wYRUsrC3Tpt7qU4J9SasspT5sgj5MecDJTafNnFax7vlqjwIVClgyQ8jDBSn99Sw8DIwf0KM7JGMUGMXRs0cFfrInXUKhW5rEK2nVAWYu3nVnWr-RRmLaQ0HkR9GKqnCM0QMrpaD6fyAO_rURmEntqwQwsipvgqM5kIF5J54Zo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=DawvwROLCKLp6qQuJ8yyjuemLrm54RppkO4ii1Yxdsmpg9NMZwZqVs_s8z9Sq2sYC49FcYbhqB9L2-lBgI85Q9J8uNmNgYr_61wdSybbGOi6oUX87Lnv9itN5tN9jjpOsWEfq1bwL9C-T7xoyzK3RR2SDTOwedB0j8kslOAw82ffnSgSliA2lwETeaiFCbdHlJhSlq42_Gz1sgepjO2N1n0EcF5FjavSP01hqtvglh8izKwuZbjQd8BiMKgwJZCsB-POVq8zYt_o5JPy5S2bfPCqQBTwAbT4rKGg38pfK77ojjINn8fKAVlAWzin7tw1_dUL8x-KEwbEDvTnyY_gwL_xQOi2dZqRLSV90F0IDfjYfvuDGLH8UeXEf028TcmCkBYWZPvI9vr6cwMrZ260XllRryjP-Ox6HOxX7sU7-tPRQvPBtqAhTGgFjuF-08JPscpQaxlYZHSLDOW_Hrmdz19d5-NjvggvPZdJ16nc2lB378rEtq72LEeONJh0Q50c-wYRUsrC3Tpt7qU4J9SasspT5sgj5MecDJTafNnFax7vlqjwIVClgyQ8jDBSn99Sw8DIwf0KM7JGMUGMXRs0cFfrInXUKhW5rEK2nVAWYu3nVnWr-RRmLaQ0HkR9GKqnCM0QMrpaD6fyAO_rURmEntqwQwsipvgqM5kIF5J54Zo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🔵
محمد خلیفه سنگربان جوان تیم‌ملی با عقد قراردادی به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101458" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101457">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=HmcYCyX8qBYWSg5h1cKUc-AdGuKv9FDW8OhafkpocWlE84a32XdjLr6hudz4iTwv1n9Xndghn-A6AV5goYDTzQPJbLeRdAUdFZX89TmzZ6Q80hhdKLWP44iAn_srfHZGAL2UHUwj_53OUOp4KEgTjvSlHzUW9sOgPw7aC3nTGXE7S3PlPdWGY6fvkbBF8rBxIGUiNHiY1OQQot5bAxME-R0gFQ9qMOXROoXdGywX3mmSDe-_Ig_H8ZyCGzZBXb-K5yPMuT5t6P7EgkjLLNxaQhTu14p2F7cjrey9AIxog1fIfbP5Zw8n3lQIcExnTKGXqc0mlDzV5dLbdLgTxoVK-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=HmcYCyX8qBYWSg5h1cKUc-AdGuKv9FDW8OhafkpocWlE84a32XdjLr6hudz4iTwv1n9Xndghn-A6AV5goYDTzQPJbLeRdAUdFZX89TmzZ6Q80hhdKLWP44iAn_srfHZGAL2UHUwj_53OUOp4KEgTjvSlHzUW9sOgPw7aC3nTGXE7S3PlPdWGY6fvkbBF8rBxIGUiNHiY1OQQot5bAxME-R0gFQ9qMOXROoXdGywX3mmSDe-_Ig_H8ZyCGzZBXb-K5yPMuT5t6P7EgkjLLNxaQhTu14p2F7cjrey9AIxog1fIfbP5Zw8n3lQIcExnTKGXqc0mlDzV5dLbdLgTxoVK-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101457" target="_blank">📅 17:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101456">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=c4kAwDKJJTHWbP7UP0nWNnv8cx4F0QNVlZJrPQ-BugHd2vZQxR90IoTzmeROJKzKch7JO7eLqZZe6IilCI5eb_B5ef8OZfpUoq5NUDlhpqPPSW_BxSvcFIri4ZMnpmowjpPYxJL9DrL0km6eUISCv2_hNzxInCrngQZJExvTcaYrXU3FDOUcB-WEZWlt0nnoiUJ2j3Y_XOnR9i_kmssjla5kuHYgTqaqe8Let2CGyvwpcmaUKMdu1GMX6KoFLspHr7k_esJwURedPTBCCTw9m3ah9Xyc_ay2hXPa6BJijmYiwjd4niX_9IT7TqcFhRab19DQyVwRVGi2sfxWclol5CEglGJRNVarfOmruDZ7aHJ0qVcsRR-6M273Jd4WgXGEJyK3wPS274qQtgKol05OsrqR93VbK02SF81mjfl2QU50ajHUZMSqDh2UE3F6N2co2dA69aORIeoNrmko24fUwZYGVrwtz0SY3VuUAR0DuiSLslcuPPtYg_ema1_pqxI0CdUx2b5I9qR1UIQ54TCMC15_dtjp9YqSDz9ZoY9YWB8ayD20ScAHJ4fzMsNVAvzyw2kqdtwL1-UnALr9j1kCmT7_q2lxQiGXNWCSGkFmKSLSqBodO_kieKRtLGD-otJiGHRO--gRs2YW5Hh0-VvrsZB8sc-aGMc-fc5WOWbN7No" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=c4kAwDKJJTHWbP7UP0nWNnv8cx4F0QNVlZJrPQ-BugHd2vZQxR90IoTzmeROJKzKch7JO7eLqZZe6IilCI5eb_B5ef8OZfpUoq5NUDlhpqPPSW_BxSvcFIri4ZMnpmowjpPYxJL9DrL0km6eUISCv2_hNzxInCrngQZJExvTcaYrXU3FDOUcB-WEZWlt0nnoiUJ2j3Y_XOnR9i_kmssjla5kuHYgTqaqe8Let2CGyvwpcmaUKMdu1GMX6KoFLspHr7k_esJwURedPTBCCTw9m3ah9Xyc_ay2hXPa6BJijmYiwjd4niX_9IT7TqcFhRab19DQyVwRVGi2sfxWclol5CEglGJRNVarfOmruDZ7aHJ0qVcsRR-6M273Jd4WgXGEJyK3wPS274qQtgKol05OsrqR93VbK02SF81mjfl2QU50ajHUZMSqDh2UE3F6N2co2dA69aORIeoNrmko24fUwZYGVrwtz0SY3VuUAR0DuiSLslcuPPtYg_ema1_pqxI0CdUx2b5I9qR1UIQ54TCMC15_dtjp9YqSDz9ZoY9YWB8ayD20ScAHJ4fzMsNVAvzyw2kqdtwL1-UnALr9j1kCmT7_q2lxQiGXNWCSGkFmKSLSqBodO_kieKRtLGD-otJiGHRO--gRs2YW5Hh0-VvrsZB8sc-aGMc-fc5WOWbN7No" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
زد و خورد شدید مردم بنگلادش پس از پایان فینال جام‌جهانی
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101456" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101455">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=q8MQhuBupB4LJ1VT7779XwkXGqYS7cWQLEJO3-DdMnfKcJJTfdPT2g94DjycQSuDHqlauOaEDjds3GHmw6dLFWCUleLMyk1Ff_4eHIMSBBdGV50BRT21CM4QPCY8ERpqRpEKqhpNHNcA36uBWcKcR1EuuMqv2BlHYNJzgOVAU1LiAGBvEXb4ggUz1FNbZYvpFAbFY6Do4akfxfVhSUB53FM_Zrnb2ax5OKhZgi5FOinVIvBkCEfUxwpWtztruKo4nlXTCRjr9i-ao1bowZQcBan9h-4kTjV0i3WT3w7R40IFW3hom2AyH3RCJSWF4y7DwIL6dk2-u18oBW9uF4bkjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=q8MQhuBupB4LJ1VT7779XwkXGqYS7cWQLEJO3-DdMnfKcJJTfdPT2g94DjycQSuDHqlauOaEDjds3GHmw6dLFWCUleLMyk1Ff_4eHIMSBBdGV50BRT21CM4QPCY8ERpqRpEKqhpNHNcA36uBWcKcR1EuuMqv2BlHYNJzgOVAU1LiAGBvEXb4ggUz1FNbZYvpFAbFY6Do4akfxfVhSUB53FM_Zrnb2ax5OKhZgi5FOinVIvBkCEfUxwpWtztruKo4nlXTCRjr9i-ao1bowZQcBan9h-4kTjV0i3WT3w7R40IFW3hom2AyH3RCJSWF4y7DwIL6dk2-u18oBW9uF4bkjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
سرگرمی برادر لامین‌یامال با نیکو ویلیامز در جشن قهرمانی اسپانیا بعد فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101455" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101454">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=P2QS8bXAME9NHxVNoKK824paV3DI7Zar0-GOwISxQtDT8xhIswZmyesarhiU7W97eL818HPDtWZTW5ahbz_mTZ3S6PIhRXsSACvcpGaCLq3tBD66E-s3MNnNmUD-B3B4rS-IHTFP2bRJmtCTz8MwCZJL6FnmzNXx3ReEeAno8Kf1eFGjWApg17lc1126GkxDfKzcK240OITbsAC0CXoSjRH0pIncMU-RRhuHBmun_uYpKtBNe4E-40RssvJGg3UQP0VGbLJkp7-tR2zepmtlNQv8jCauxcqhSRUgd3TGgw9dqWHDdYaBN41N0c0mA5z2Gv54f_NNGnDqbElNdZGYBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=P2QS8bXAME9NHxVNoKK824paV3DI7Zar0-GOwISxQtDT8xhIswZmyesarhiU7W97eL818HPDtWZTW5ahbz_mTZ3S6PIhRXsSACvcpGaCLq3tBD66E-s3MNnNmUD-B3B4rS-IHTFP2bRJmtCTz8MwCZJL6FnmzNXx3ReEeAno8Kf1eFGjWApg17lc1126GkxDfKzcK240OITbsAC0CXoSjRH0pIncMU-RRhuHBmun_uYpKtBNe4E-40RssvJGg3UQP0VGbLJkp7-tR2zepmtlNQv8jCauxcqhSRUgd3TGgw9dqWHDdYaBN41N0c0mA5z2Gv54f_NNGnDqbElNdZGYBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی‌کریمی بازیکن سابق استقلال: استراماچونی در حق ما استقلالی‌ها ظلم کرد. نباید تیم را ول می‌کرد و ناگهانی از تیم جدا می‌شد…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101454" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101453">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WH0JGNRiK548TZmqI68yKoOiNO-xNrVNCcA1PDHbGnvzvofeSgiNkxUbeCypBzRRCSF7dfBiPlNB4I35wZq3gUHjdAjqUJmQbjehdH6EZSYfK1dE71knSmyvW4B82MmIs6y8FMQbAVMkV4eyaRDmyKTtaXHYGa7gLWicvW_Y06KgQ03c14DRkYFciMk0h0fXqbkY7a1Dm7AeHYNZLjhcrRD3kTb0AgarNp9F2zkz97Cn4IesSvaMNnGf0UaiRtNzCLGoXzbzgAjoLZOJyvQ_Z4laD8lj7cII270cp6F3VLVt1dnCqnQvi3MmgFUcctxG6BrRmQdIuDEt2TC6Z9paHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بند فسخ قرارداد آیمریک‌لاپورت با بیلبائو ۱۵ میلیون یورو است و اگر بارسا برای جذب وی اقدام کند، به راحتی موفق به امضای قرارداد خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101453" target="_blank">📅 16:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101452">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Wg_XBjcSnlhSwLB0b4rDOQZ2AO8SLDSjWxSPV9pVG4kUstdwBTJwxT5bJUETmFL7YJtJMCC8z4KJ1dq98qFJlmzonUMCmA0j2Qv1-HMykNrxPszA5OdMRzfeQK-Se8SpYKenj9lLzFCqnqCKP3hjWfNCa5EzUmpgwzakUkjp8faHWaWrAhkn-MfoTGirqLiWZVedd0SSc6rXJejuNxB-Av9DvOMr0mZXtN6yDbO43jBacnD4Qj4kmj_8lAkA9-lrPKYQJs-fmMKPbrsjAQwzVR9rdZItH4lxorSj0JA0mQG3lJP2WgJTJe8ZtTPOXAuk16g1Qtkec7N7dmSpE2k1uBcXFeChCYPg-HdchDa_0bYcnoE6bR3sU367Cki5Of370D6PdCbyXCUUtfOFJLLL66hKLoIceKzoRhuhdHz5kPxq7xQYxL-y3EGP-D3Pm0AuwxBerW1tie5W83uZe4p-uOkSJCOKks6efq1v44ku8qvBwJLzq7E7xV-HQghrDhRMb7yd3Cpv4pCQhaalMJ4wPaHYAsLdLCPJG5TrvD3iCe9ksCMLQYRoAT0qajiCD8wt89DualntcfRyRU_diCb2dEQkdvDCE056JdGR9PnJRL-xSh4iAvKgXS4wgIL7_MW-yNEK0RkU_gtMa-Tb9GHm3OkLtZAYDAmUIBUtAkLFb24" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Wg_XBjcSnlhSwLB0b4rDOQZ2AO8SLDSjWxSPV9pVG4kUstdwBTJwxT5bJUETmFL7YJtJMCC8z4KJ1dq98qFJlmzonUMCmA0j2Qv1-HMykNrxPszA5OdMRzfeQK-Se8SpYKenj9lLzFCqnqCKP3hjWfNCa5EzUmpgwzakUkjp8faHWaWrAhkn-MfoTGirqLiWZVedd0SSc6rXJejuNxB-Av9DvOMr0mZXtN6yDbO43jBacnD4Qj4kmj_8lAkA9-lrPKYQJs-fmMKPbrsjAQwzVR9rdZItH4lxorSj0JA0mQG3lJP2WgJTJe8ZtTPOXAuk16g1Qtkec7N7dmSpE2k1uBcXFeChCYPg-HdchDa_0bYcnoE6bR3sU367Cki5Of370D6PdCbyXCUUtfOFJLLL66hKLoIceKzoRhuhdHz5kPxq7xQYxL-y3EGP-D3Pm0AuwxBerW1tie5W83uZe4p-uOkSJCOKks6efq1v44ku8qvBwJLzq7E7xV-HQghrDhRMb7yd3Cpv4pCQhaalMJ4wPaHYAsLdLCPJG5TrvD3iCe9ksCMLQYRoAT0qajiCD8wt89DualntcfRyRU_diCb2dEQkdvDCE056JdGR9PnJRL-xSh4iAvKgXS4wgIL7_MW-yNEK0RkU_gtMa-Tb9GHm3OkLtZAYDAmUIBUtAkLFb24" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ایمان صفا بازیگر سینما: با کری خوانی‌ام دل خیلی از استقلالی‌ها رو شکوندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101452" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101451">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101451" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101450">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMhcvN2AEcQrRqERBNiSBJX_JDL6uOBnPbX84oeGa6W8Gzvi6Al5te9nv1dDthpT7-q6llTdbB2zTYHKOBcMJ8fBVPp3p6O5mg-YdfgnGnYITs_idORATl9dTaydXhdTigY6ujOpS7fzrB7Sx7Cuxj4Iz3Ia7L26uSMJb1GuzXCvpEmEaxPQsy-QjKl3BKGsxmnLl7f_6BYKAxo6IZwwLVXGamaT_kD2_fK0VLZY1edFuNjpZccMDh3lsV5_AnJQ-BfMHRv4O0sCknoyCoCWsorTAG-sphpqhbueGQq27OXXUBklhzaSpOGQ82k-VRtsGZQRyomUG4hr5eHq0_rAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101450" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101448">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=RB8ECmZedva58a_el1z58PGKhpjNoMGZmn_t063VJ-0pryXAc33plj5q4k5hqjsRMmzJXDfS5GVXGI6fOtDvVE9MpYxEO5Y7oTBSk6fxrFB_RD1mrBKBeAWSQL6gemVuVFEIIH6xu4ZTBpNiyhtVlO7mRg491jHUEmBgzY_IhN39pL0QuS86L1Nm_3EoTT3EZ1BGp398dDOUA6ZHaBXzKLh7691LeRvkBGpBwF9Ogo0hmcp17o01gHlrtqiiL_rHa_8os-Dp6kF9-yHfIKW4--anuuo_dnLHujnmYClFS0iti9FiV167zUVYXF9mMn7K-T8cza1hbl_QuKoBKUk0bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=RB8ECmZedva58a_el1z58PGKhpjNoMGZmn_t063VJ-0pryXAc33plj5q4k5hqjsRMmzJXDfS5GVXGI6fOtDvVE9MpYxEO5Y7oTBSk6fxrFB_RD1mrBKBeAWSQL6gemVuVFEIIH6xu4ZTBpNiyhtVlO7mRg491jHUEmBgzY_IhN39pL0QuS86L1Nm_3EoTT3EZ1BGp398dDOUA6ZHaBXzKLh7691LeRvkBGpBwF9Ogo0hmcp17o01gHlrtqiiL_rHa_8os-Dp6kF9-yHfIKW4--anuuo_dnLHujnmYClFS0iti9FiV167zUVYXF9mMn7K-T8cza1hbl_QuKoBKUk0bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
خاطره علی کریمی بازیکن سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101448" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101447">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53a9000335.mp4?token=Y9WNl2bPk2zfzL3I46eI0XDi_SWFQOL6tvKCRD5cAmQI6yV9BE6IUh3W2Ggq3-QjZYT_S51VE7nK3nSN66c8mpWg9lCBBI7EqgoXZcTVgfWUXf6GI55t16_TD2MmSmnaXx8cASE6MJThABkofX8nzWbHfJZqRkWt-dZXjXhV-dJ6_JRzLQMA3cllOr-_3Msmy-1AYMjIJsPCaGVak8RREFWpVFuW6NNcbOt1G1AWe6WqmLNAZvw-e13iHzhyAoutSzieZG_0wQvHp4pyTpksN5E1Cd-lXcX3FMRBjc2fDQm5PCPBO1DTdEo31Og1exDz_el_Qv2Y-5-gEdviAUNVgaOt6YYGFT5HDy9UjfcZldhqQ-E24RN4n1uJocG30UWGvkoXd__kaj8dFpbXzlLTy-1g6UZqeuZf6ePD5d-ot2Zcv4XCo1yDXb57ZLlifKrMDRH9Nwh0j7V-b12_zEwR8ixcmkUh4MqBQifgwaP8f4fSf8u-wN4SKH_G9G-73ZsK5cw97fJeS8XeSUA-O3QM5VwDD9PscMzXPtkRYL1jbWOyA8UpLTwOv1QhsNsBANowim0R3xr8_ESmfEKoP-EcFABHOSbBFjMI5VkDZOsd3-GwK-g3lc_G6Kgw3EYP4AEkb_3cjEI3iZUVGywqMw2nqZGdPreQ7MA-bnmhLRUzfHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53a9000335.mp4?token=Y9WNl2bPk2zfzL3I46eI0XDi_SWFQOL6tvKCRD5cAmQI6yV9BE6IUh3W2Ggq3-QjZYT_S51VE7nK3nSN66c8mpWg9lCBBI7EqgoXZcTVgfWUXf6GI55t16_TD2MmSmnaXx8cASE6MJThABkofX8nzWbHfJZqRkWt-dZXjXhV-dJ6_JRzLQMA3cllOr-_3Msmy-1AYMjIJsPCaGVak8RREFWpVFuW6NNcbOt1G1AWe6WqmLNAZvw-e13iHzhyAoutSzieZG_0wQvHp4pyTpksN5E1Cd-lXcX3FMRBjc2fDQm5PCPBO1DTdEo31Og1exDz_el_Qv2Y-5-gEdviAUNVgaOt6YYGFT5HDy9UjfcZldhqQ-E24RN4n1uJocG30UWGvkoXd__kaj8dFpbXzlLTy-1g6UZqeuZf6ePD5d-ot2Zcv4XCo1yDXb57ZLlifKrMDRH9Nwh0j7V-b12_zEwR8ixcmkUh4MqBQifgwaP8f4fSf8u-wN4SKH_G9G-73ZsK5cw97fJeS8XeSUA-O3QM5VwDD9PscMzXPtkRYL1jbWOyA8UpLTwOv1QhsNsBANowim0R3xr8_ESmfEKoP-EcFABHOSbBFjMI5VkDZOsd3-GwK-g3lc_G6Kgw3EYP4AEkb_3cjEI3iZUVGywqMw2nqZGdPreQ7MA-bnmhLRUzfHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا جهانبخش: در مکزیک زیاد بهمون بد نگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101447" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101446">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👤
محبوبیت خریدنی نیست...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101446" target="_blank">📅 15:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101444">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO5FMTdvO3L0ROQAqH1coTCR40b5m_XelozeUBu281GRtLdO605xzIdJRX50q-d7SPs3kabBTpUobE6s2ieXjkxE_nfiZFL5dZupD3Xq6aeMfgYoDb1xSqBWYB1t-zeNSlCpOqJBBXKeWCJUZlZGSWUHLbhL-7q7rf6OjtjrmKWqRslKVDUHmv8SzQUUlnXN0or64HXQjnNnHxHQsdJfjFqHwiMfShoPyND1z8xUPq3sbbIcqtF5m0qbWezRrnH2uu1wMHFFnGHgeq3KkiOTY_WO4tZQb1_OOAlRtd0utekq4k7ru8ZyLhT09rtLJIDONmsP3wd71PpRr7VkGX3AGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
علیرضا کوشکی دقایقی‌پیش قرارداد خود را با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101444" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101443">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=sNPWR5MYTMor1uY13ON2WQ51x-XRMduKf8O1QSX9hOcpbqMRtlY1d4nxX5iLb5V_6AlogLi81fX1cs8q09WW6L0idgi_Kfj-cOEFFgthLDUbI6bn2IwgV4Nu-vivMuoA9Bjf2bO3HRamk5_EsaeAa8538ai-MfUJA8KO7fCsrpPus7mxJ_4fJ_2a1AXT5IcYKYYdutZmN383bdVjKQdagBY0D5DkIaiEpVMpy2ExjuTwKgJdGpRTnQZLe5OHAMAnTdZPAfM6E769O4-kcfiP1dUiZe5FIlhJrLBLjpj7GkTYIh66hz6UwW7LsT3Anu8O3T0nzgoYmBJXEi3_QBeUow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=sNPWR5MYTMor1uY13ON2WQ51x-XRMduKf8O1QSX9hOcpbqMRtlY1d4nxX5iLb5V_6AlogLi81fX1cs8q09WW6L0idgi_Kfj-cOEFFgthLDUbI6bn2IwgV4Nu-vivMuoA9Bjf2bO3HRamk5_EsaeAa8538ai-MfUJA8KO7fCsrpPus7mxJ_4fJ_2a1AXT5IcYKYYdutZmN383bdVjKQdagBY0D5DkIaiEpVMpy2ExjuTwKgJdGpRTnQZLe5OHAMAnTdZPAfM6E769O4-kcfiP1dUiZe5FIlhJrLBLjpj7GkTYIh66hz6UwW7LsT3Anu8O3T0nzgoYmBJXEi3_QBeUow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عکس یامال روی پهپاد انتحاری شاهد قبل از شلیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101443" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101442">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCSOFI9ho5_X21PfmkO1BeZ6KyULo39FRWrClMQ_nM7-W0tZBoUD9OpQYnz8OUzTtx_mOYSk6pgio_bxb5ysRPKJmgk_dTqG9dnka72FeyVXIsQe6PaJMDaQAF7qvaBFCDSqanE4_S4jzzrGoIVVnHHdzFtR6wlcYesVu_J0SJErFPt6Sc692qdeWlD5jFBKIOzaZtd1gCkRInEiGh3fFg3rJAYv9cpAlmjns4hbtOD7BX3DXuT-Cf_MdiYm-TLhs0pvQ4Ly616bKq-WTe0iGpEpG8kCrWwhcbhBs3N1Iwx7rMaJUp3VW2E412-7vccGBTNa1B0OLE5HG06LF4bZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رامین‌رضاییان با انتشار این استوری تقریبا جدایی خودش از استقلال رو اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101442" target="_blank">📅 14:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101441">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j05DVqCX0_4Qk-7_96jRrDyMR3ULg2SQEnCOh1INetIkwcJ4ZSA3qMg6pgww2UH7AOsC4QHTjWyv1hAF98LM4TPQePAdbkiIM3fYcFsHiKayuW_skiPMEDagMk_dZYi1nrd6ha4azsfdDfMfDWlaibgu4bTVEzg7pBSRkEsxPmKpcps4ZjNy2_vwTgMm1zTwMTRh3NEzavHxspaOa123pztI4NtEclyiDVrYoOjid5hO204yTp8rw9ldfLc6c49J8KJk7Gm8n35goVPdmOSGVNoqQt9lWgbhSryXO8nhOSx_A2jrKHrylVtfyK75mGCc818dwINfbPlUjgqDZKQPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🔥
لیگ‌های بزرگ اروپایی چه زمانی آغاز می‌شوند؟
🏴󠁧󠁢󠁥󠁮󠁧󠁿
[31] روز تا بازگشت لیگ برتر انگلیس باقی مانده است.
🇪🇸
[25] روز تا بازگشت لیگ اسپانیا باقی مانده است.
🇫🇷
[33] روز تا بازگشت لیگ فرانسه باقی مانده است.
🇩🇪
[38] روز تا بازگشت بوندسلیگا آلمان باقی مانده است.
🇮🇹
[33] روز تا بازگشت سری آ ایتالیا باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101441" target="_blank">📅 14:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101440">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=O6fZYLeKV_XoZ7oCsB-yjevA7388g9dExQyxnLlUkzwHp1Y7QW4Qv45dCnTQBDBF40WGZ7yPav1E4e4GldotXeh0uBcFlaFGuVdS8rhQYFoKvsg3T3gnMrAzGw4H6gUScVZC9au3K6mg405fPcLDHtWdxyc7WlVPcuj86qngI2iHEA00K0StkSkrCeBhAS7lQ3liRY1Csy50okaoODcNXombf-ZDdi4lLLzGUPEx5f9QxxqmjDbnJXnCykG1Wa5UHkGNe1V6EBnqQ6s-p25o5M-wLjt3w_BOpapZoLx3TvxPTdHTAIFjsB0dLaW_tA6oUopU-i4O54HXGN_tozlZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=O6fZYLeKV_XoZ7oCsB-yjevA7388g9dExQyxnLlUkzwHp1Y7QW4Qv45dCnTQBDBF40WGZ7yPav1E4e4GldotXeh0uBcFlaFGuVdS8rhQYFoKvsg3T3gnMrAzGw4H6gUScVZC9au3K6mg405fPcLDHtWdxyc7WlVPcuj86qngI2iHEA00K0StkSkrCeBhAS7lQ3liRY1Csy50okaoODcNXombf-ZDdi4lLLzGUPEx5f9QxxqmjDbnJXnCykG1Wa5UHkGNe1V6EBnqQ6s-p25o5M-wLjt3w_BOpapZoLx3TvxPTdHTAIFjsB0dLaW_tA6oUopU-i4O54HXGN_tozlZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
خانواده سلطنتی اسپانیا در مراسم استقبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101440" target="_blank">📅 14:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101439">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101439" target="_blank">📅 13:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101438">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e455125710.mp4?token=LZ1hzuykKcv0d8amk8hWeivY6eJHC6D3fUNSY7XGzCKCTmF584442gTnDBwhoID0N000SV75iOnUZAQGj2X0PVQaRug3mU67jjD2gE_hc0Fux0DX8696t_k9cwkv2N2qCBgvnR7HOTa-XWSk8iqUcK-OPcdmjMLk_pBIMqQ8apdmVORWDmB2T7Xn827-JwVLHK31aqWBit9BMo8pu185Mz7Ygugt6r3UXxElcDtV4dv0l4E_tdWMIp21PuzNHmRJuPYINNRer7-1g1jl9_pNBpfh4ACOxmlONJ-UiR9u8veg4GJFEjrEWVFJAthM4PM3WYzvdnwKWQuFmduYmMNHyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e455125710.mp4?token=LZ1hzuykKcv0d8amk8hWeivY6eJHC6D3fUNSY7XGzCKCTmF584442gTnDBwhoID0N000SV75iOnUZAQGj2X0PVQaRug3mU67jjD2gE_hc0Fux0DX8696t_k9cwkv2N2qCBgvnR7HOTa-XWSk8iqUcK-OPcdmjMLk_pBIMqQ8apdmVORWDmB2T7Xn827-JwVLHK31aqWBit9BMo8pu185Mz7Ygugt6r3UXxElcDtV4dv0l4E_tdWMIp21PuzNHmRJuPYINNRer7-1g1jl9_pNBpfh4ACOxmlONJ-UiR9u8veg4GJFEjrEWVFJAthM4PM3WYzvdnwKWQuFmduYmMNHyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
دیس فوق سنگین ابوطالب به قلعه نویی: ما تو غار کنار عادل فردوسی‌پور هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101438" target="_blank">📅 13:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101437">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjKC3kGRlEbQsR1zPqCH0E3ZmGAxpZEQl_ChZRpEngeybkb9d6gMDgJn8PzckwT5WE07xyg9v5OjB2IG52F9xr1QgXzXodENQ0D9eeqQLxKdjmhsKR7epTxchbR0FHyu5yVTpJd9z1iUoPrBx80OrCt60Wi8G1atYUOpyUiHliCsJJoMN8o4O80qGsq9TaksJytn8zMNcBeMxHsx2a6EmI3eO8QvmM7Idlr0HIo3BgXUrVSU7-Mz0T1bJoLI8rF19OisuZbKFSFvifXUYlDSKEuO7b-G1geIarMyoFT8SE2jUbfX48YSw6BHFCQtqTc1QM2hG66N7J-FQS-EAgg0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101437" target="_blank">📅 13:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101436">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH7yOc51ABkVQ45wzZWDJxGLFhrZP5KiTVEyeiexw1LAfUf7azrZI5aNOPO14_38TGhmuq_wTmwPq-aFAlX4MuvzUFySW7pum1rETLtB7Ia875vAJdorkC8QvXnAUAs6CZDFFX0q2UoTXirUziozbrW9yNMUHr7C6Chi4ZCnsT16OisBD2_HY4rUAKYpMtXZX4agXH_EWc0hFYjRbydBJwi0D_0Y527gH9AN_REYNluPj3inZsY1GJbooHA7t2UnncqHW2V8-ARObYMyMFaXbDPjygx35tXz0x7Dg01gKN4IPfGO18hpQsJGSwbasACZIdlh0MDttg_V68AO-3EJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
جسی‌بسو بازیکن جوان تیم کلوب‌ بروژ بلژیک به باشگاه بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101436" target="_blank">📅 13:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101435">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101435" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101434">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2mjVISI6wT5tVs_zkBSR5xU5hghfjl6icedz4ngc6l2b-LkqiwCcs9L2BHhErgQIEdPW4jVVfj9kpul1utD9FR5CpDI6czQ8ipLRKXESK1J8EyKaz3NqYVQfjlr7f4QgIipiCpzGmdqmWTFECvISa9qVwMOBMwJ85J2p0Xcr3UmsTO6-n8HWAUvrYHHljuneNplWhVEQUc6tBPqhmDXTyvyrYY_CddIslRFljPKu8KzTwEZolOrBhxrquMQxWGmz0nQRCoU2cN5TbnWTnAwyjkZ9C4uJhPivLG26iwULnp9kWcLmx5_yrZtasyCye0S9Ggn95WUiC5s3OJJKxE6zckk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2mjVISI6wT5tVs_zkBSR5xU5hghfjl6icedz4ngc6l2b-LkqiwCcs9L2BHhErgQIEdPW4jVVfj9kpul1utD9FR5CpDI6czQ8ipLRKXESK1J8EyKaz3NqYVQfjlr7f4QgIipiCpzGmdqmWTFECvISa9qVwMOBMwJ85J2p0Xcr3UmsTO6-n8HWAUvrYHHljuneNplWhVEQUc6tBPqhmDXTyvyrYY_CddIslRFljPKu8KzTwEZolOrBhxrquMQxWGmz0nQRCoU2cN5TbnWTnAwyjkZ9C4uJhPivLG26iwULnp9kWcLmx5_yrZtasyCye0S9Ggn95WUiC5s3OJJKxE6zckk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🔵
باشگاه استقلال با انتشار این ویدیو نوشت: برای بعدی آماده‌اید؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101434" target="_blank">📅 13:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101433">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIdNCJvcWgKC6SbqYfmPtHsLNsbKTP6qZgEa7OXFnzaLWdD7uB5TRs7VqhqZsUlJvlSPSsEUW9sP77z7l6zDKxgOu2VZZ4Cau3TMFuMiuArtzVD-te5_qIW_aI1eBSrhb9tiJi6rQzPsAK8pN704j6y1wylWL8ucAasUZ_UD0wWZ4Hhr_9hw08R3Bo6nI3hB5ftyeDznMQgTx5Ai4bbLHvPBjVXwDZiJ8MVYXdFuajHa5VCXzV39h5jcxwyFwjDuwbBzBvksn_r_FBWU3acmXeBy-2vzK4N7OCsCEGKzKB6XZkQiD-TLatFj8J3BRzdM9lMgoXdIr3gLxrhvUOkasQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🚨
نشریه(L’Équipe): رئال‌مادرید بدنبال عقد قرارداد با فران‌تورس ستاره بارسا رفته
کاملا جدی این خبر رو زده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101433" target="_blank">📅 13:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101432">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=WPHnWT_V-Dz37sUjRCf9v6tzX_6g1M10BheEcVtM49udMWCMsZY8eIjJKG9FCnq29G9t1eCKDGg0UU00SEfBOQBppZDkL1DAfOUhpdODT2U7FJwmxE8DQLkAlEaE76_2VYq--r1hKnZ7bR8GTafvae-KedDQXi2TmUeCvLL6mESGyUJ3E2TMf9V1B0TCwFDzREoBrEB2e1D1oNmQG0Qe0R4kkj4u_T0ko5rhrAVxfhPfXQNjP_-0x-_N2nkzBfws7VsPDywkBsJpReHhAXeUWaYp5-NliP0UR-rezlFI0jUUGc4C6_l-_W86XLcf0IMGwNdhZtBS7aNRr7Vn9ktuGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=WPHnWT_V-Dz37sUjRCf9v6tzX_6g1M10BheEcVtM49udMWCMsZY8eIjJKG9FCnq29G9t1eCKDGg0UU00SEfBOQBppZDkL1DAfOUhpdODT2U7FJwmxE8DQLkAlEaE76_2VYq--r1hKnZ7bR8GTafvae-KedDQXi2TmUeCvLL6mESGyUJ3E2TMf9V1B0TCwFDzREoBrEB2e1D1oNmQG0Qe0R4kkj4u_T0ko5rhrAVxfhPfXQNjP_-0x-_N2nkzBfws7VsPDywkBsJpReHhAXeUWaYp5-NliP0UR-rezlFI0jUUGc4C6_l-_W86XLcf0IMGwNdhZtBS7aNRr7Vn9ktuGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه نیکبخت‌واحدی به ممدحسین‌میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101432" target="_blank">📅 13:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101431">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=I0zIwLQeaZx-Eo1svb-5HtBZN8J6T6384aOMfqY1oIymA_PeCqhS7dAMG5eCMdrbZNORE0Hn1KvHPikYkmVS3Mf7Dsh6c-C3qvOevTx37jWcRHEIIXcvVY9qKmhU4RPHeKX1waCKo6EYPkIj4rHr1TalxZFMbptk0c-xtlpRVycNtjlC6AhLjG7fx9wwIUkygkjcRxj7KxirFEVp9EgPri1ClxqgBCTooJ3qhRsYfKTNY9ypJ1tllHUqZ_7LXOT3zGd3LsJXRX_7nRr2yqCTu1d5EAn7ivb4NxHNip8Ou2ezk0Qyjc1kDsqQa1-i7x0LQlfeVB7lWqAoNyoNPWXZFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=I0zIwLQeaZx-Eo1svb-5HtBZN8J6T6384aOMfqY1oIymA_PeCqhS7dAMG5eCMdrbZNORE0Hn1KvHPikYkmVS3Mf7Dsh6c-C3qvOevTx37jWcRHEIIXcvVY9qKmhU4RPHeKX1waCKo6EYPkIj4rHr1TalxZFMbptk0c-xtlpRVycNtjlC6AhLjG7fx9wwIUkygkjcRxj7KxirFEVp9EgPri1ClxqgBCTooJ3qhRsYfKTNY9ypJ1tllHUqZ_7LXOT3zGd3LsJXRX_7nRr2yqCTu1d5EAn7ivb4NxHNip8Ou2ezk0Qyjc1kDsqQa1-i7x0LQlfeVB7lWqAoNyoNPWXZFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
داغ‌عشق پرنسس لئونور به گاوی دیروز تازه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101431" target="_blank">📅 12:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101430">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=uQvclVxaFnQrhf9BeYxKGrdefZchGFYQN1xlXUfnGJD2zXOuf9cNoqBFMmM1v8tTQM79kmBJFPZk4H5C8Se1RIZKA-M72HvGhuR8jVtKQjuT2LGMAq53GFCHKZS-pTePUggkgLCWYb0ouYWvJT9JkFG2RtXjnyKDMXho8jmuyaOgwC1L_i4LowdPAzopUy9pJD2AjKxDaALTd6WmaP6b2Fw24gHgZ92UXGIO_T1vVif9lEDZrFWq5rMR8KojqiKtYTAfH9Uq22fu2k3olXLTCVzt2Xvbb5KSvCd271nG5San89xVsHBnE5M1CGGV-GlLH3JKNwB4IkmK2gcpPHir7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=uQvclVxaFnQrhf9BeYxKGrdefZchGFYQN1xlXUfnGJD2zXOuf9cNoqBFMmM1v8tTQM79kmBJFPZk4H5C8Se1RIZKA-M72HvGhuR8jVtKQjuT2LGMAq53GFCHKZS-pTePUggkgLCWYb0ouYWvJT9JkFG2RtXjnyKDMXho8jmuyaOgwC1L_i4LowdPAzopUy9pJD2AjKxDaALTd6WmaP6b2Fw24gHgZ92UXGIO_T1vVif9lEDZrFWq5rMR8KojqiKtYTAfH9Uq22fu2k3olXLTCVzt2Xvbb5KSvCd271nG5San89xVsHBnE5M1CGGV-GlLH3JKNwB4IkmK2gcpPHir7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇦🇷
استقبال مردم آرژانتین از اعضای تیمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101430" target="_blank">📅 12:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101429">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=fwDM2xlBdV7pocaDkAzpdAkcIoLid73fv-Iz1tNOI93Pe0yeMgNw-0vTLxtbQOsvIkDaFL9xuvA6EHOq9k7im_QuFirlNHUiykELR6-vB5pZWtWGKZPVjW5V2nw-E3rSYyKGDlsdSxhCCBtmL4HbDxoOuALNhui12oZuDWwHFoMkxYt8mduwrLrjkIlLePfHT6nHlOyTBz7VAA0awcSBntI_vHcZdx0bJ0tJoQtv7xhr9ydzQ3xlarIG-Tn_MUn5-Ir-oVAT0A1kkMrhmznysEB6-62xv2ibDfaJX09cLZP_SzAsn6p5NaI-XYXM5iYW__FbqD1K9kYtfbQ077cBpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=fwDM2xlBdV7pocaDkAzpdAkcIoLid73fv-Iz1tNOI93Pe0yeMgNw-0vTLxtbQOsvIkDaFL9xuvA6EHOq9k7im_QuFirlNHUiykELR6-vB5pZWtWGKZPVjW5V2nw-E3rSYyKGDlsdSxhCCBtmL4HbDxoOuALNhui12oZuDWwHFoMkxYt8mduwrLrjkIlLePfHT6nHlOyTBz7VAA0awcSBntI_vHcZdx0bJ0tJoQtv7xhr9ydzQ3xlarIG-Tn_MUn5-Ir-oVAT0A1kkMrhmznysEB6-62xv2ibDfaJX09cLZP_SzAsn6p5NaI-XYXM5iYW__FbqD1K9kYtfbQ077cBpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حضور ترامپ در فینال جام جهانی، ورزشگاه را به یکی از امن‌ترین نقاط تبدیل کرد! از بالگردهای امنیتی و نیروهای ویژه تا تدابیر حفاظتی چندلایه؛ همه‌چیز برای حفاظت از ترامپ در بالاترین سطح آماده شده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101429" target="_blank">📅 12:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101425">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eg9pQPmc16Gblf0kgskp_5PblxXpyDH0IwBKAfYjwc--LTnkGOSb0fgrzwZB3glLLA6Qi_MHPWQjvM-0mMs46Vq2ANCFkdwYKUEqZdiAl97swPAvq6LN6vJPhP0Y39sLvAgh9TCkwc0vPhHeJV8uuR6Ntzm63xlgYWR4qjwzpGoVKhtnzqTtyTjPIg-Pb0qK3IGefy1nUls21noLfPM6Q8VQf1xz5umISAXR0JyeMkUBjwVBRFqTCplXFd6FiMb5PX6--Ls7HNbClc5Y6D7w2L38wGwUJxrDLlMiVk9x6SIN4mb-bEVR8V8PMdxycyQZirPf6HE_rGB3T6vuSNXZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/il_eGszfgNtqb2v6z1s-3d2C7GGH-lJD6GH8WZ2Mxe96cuK1qHZ7wTz66g-vyBnFRfKnB-Qkz7GFlJIWsi3-xA6sXpeZolHH6uF0SrbCF8KpQywnZlHcavwa79ZTWHSmrhc4zc3L-sDSjc11_Khpk4VDHL8uJK3DqvwMpGUdwsgJc6UY6gNE7wmY1ERO0aITPhnPNJYt7iMwPc2FtGKdT_A0cFjYaeQcIBjW2BhmJOVXMyA-Xhbq10oJci2Iu-wR1oxYGpJDM_haxFZri8svX9svDsaZFRLEjDYYiBGu-NGv6wg9YVLY8V-nYzLE-C9zv_kAJFqkUokz3D6qAkclhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCwK2igNhwkNcOl8WXySmqfixMGRhRbRQl30dzavGRE1BcvE-TmDWv7hw1pD1gDWfMn4R9FZvjCrtL9a9WOHZxWbT6UVhGrKTYeyBZeSOWourLlmSrb9N5lU_ZwaY7iR5z5c0wYv-j5jblytjI0paQf1APTRXiELC7RJa42XOYFTsGNo48yPKz_6aSTpwe6y0-gyQB10n-54IaN6uIZJE2Z-LeguePJGj5g7bLRX-MXrF6nXZKZHol1gEtYuhxTqMef3Ghs0VTk8hCtIMm6rQf7HFG-5yQx429dhGW3yqYgVA1krBlRWNvSKZWc2u0LVQmG0d4gnpgu9g3fGAIsogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcKw5U-jYvB2IuHlxWq1WDNBdOzWi0NVY_tT4gQiK1f0u9aIe7lW6K1s3fQgSZqHsGoFyQjky8aRyrfKuzlqnD52T_pR68doYMglrerkZpgE9EZIQn9TWt-GIbDry0sT0rfca0rse006lQmR4vQI1NtFL-N9trP9p-YrCS9ODO7BIgDo_Yl9OQg4JcssJNeTT56nVbLLT2fixk8YrmDnOuZgHW7nukZJkkII5ESV0qd4sXCTxEKNHYqGckwTrXf9-tmsEZzBjuRY1tZ2htxT8c2ltXlrjRnXj4sZbwvqdcaK3yJbvYXgBcT1F-VOUFswHcPz2bmY6i2hxxGWhsmHRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رونمایی باشگاه‌میلان از کیت‌دومش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101425" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101424">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mO0UwfIwznKQHwXx8Vm2G--XgClE26ztpBWsSv4hFtG86tyDBuRp5pa24JEcOOB6qsqkkLL7aSF0Qg1Ugl4HIO_NTOg-KibSYzB8j_ymBUpDwaPaw6KKJ07pxH9_Zx28_rZE891YG520hWBXuzKJT7bff6ixZoB_E0rCr0lZXt-JilghUcCtLO5Z8beqcJEPci8zi5l4hveIweBpPbJ3KXzb9hmC1DGiY-ntnVrKF_ofcj41Sks6l5i45Jwe4tHaEMImyxOZpESWyjwXEu0sEcq2OTl7sGkHm3GuBm03FOTsfBamDxO1uN6wgs9mKJQoBEnYH6CvE9UvPi8N6xJGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
بهرام‌گودرزی مدافع چپ جوان آلومینیوم اراک با عقد قراردادی ۵ ساله به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101424" target="_blank">📅 11:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101420">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWYtzTFgLnXq7kfwS7yrkxYEyEFI_yrNyoD--m-HJOWFPDvIf1B7tf6LildxcJW8cw3WxvDkxOnDuj1o8VA9tIcItlcooUxb6BppFovlkvp-DOuxuMgius8Yl9Wn5hgrVv-qp9FM8JUa5tqKZHEGDln6sHLBqEPhd8DkO4Q_RVJbD2SajlBztCdh3qDQAbFsWd2c92rPFQQg1wE5TxWvhpk2D77i6Zb9utjccSD8gqugfH7Ix8KZ2V59Q0M2IobjBF_m-busXCdTXOP_beyrOmKmYXSCeDOTrZ3y4GxJutLkGJnwpsuOdsMdolbuZB2JMHmVnvhVhciaC7w9mHTF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gG2FARAES4YQJCUeBlAfcscc5vkuEJP4fsqjjmb1rNR0DDAMR0NHtNU5p-tuKvgXcCgLxRpVKQTZ163UOKn2dFqgL7NoJRXbYXUnxSyAPtgxrGoQcnx663E_pKANshmff1zHK1B4F9FwSF1mZxYEMRAHI_JX8XGxQVBnnC87shECR24OQnyL_unWQ6T2A8A9jaJ2tb3Got823YbGmZZ2ud5NTrZv5tXNiW1rmznDaLM53kxGYwv4RpDYAhqafyvEzfO0LByt0C9rI2AHORUgWd_sEzY4cYyXvOn0EgcWb8PZHD8dQlBRU1feN5HimBuvzxqFO5i1dtxAzGK9jNXrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGsLTsol-q77C0kbafmi2yUnvqkxgfLKiwEw0WzdBf33kM2lJJLPR0L9zLK0z0aZ7IMcMxuGsz4JD6F8j5khLJZAv8HzChjjsA_b04yT2onpnIOExXF3FPZLiLrm90cXQCbZEYXbTysVHLXMkzdJyZx2dmeXL-DwcGacQhfs9EbN4NByfwGOM7MpONTOui-T5mwvL39FlICeY61sbu5G2ia-4HiZ76QkFtV58ZFnFaSiWwpgW6aIbUFtXlRLA2KwBK-EaFTe_YkmsWDT0pmfFxsLcLxRC5AMQChUbiZhEY2rVXzxnOGxe_sVlJUAPQW4mxBGulQoSuAfDKZEGrZmzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8fYHrtYVviBeGjJopBai7LbxG0f7FU9jZZxiSqmqRj3-0yBogThxVuY9oVHUS0gaFOXTqK9RRNxOh_1xti0jGbs22bQqAfGjwyauIwbKOu9HQElUpV4j6zdo9RiLqvPNmYZretvBfJgptli1a75NwyJ9oChNKwQii6haquDhKt6qLvYEm_JMlT_F1VbTBdO4tY_bJCJeCH-RlIACOGtqCL9QeeiFo1PuPWv9Uo1YdgUFNsiXuGoKuSfmqXoV8HQBmiGp8EfpjA5PD-hENvHpH_Gyi-k7x9_mOkmqlJIozyldUuWejITtSaNnNjXdULtvBwgvb3efflCUapjKB156A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
رونمایی باشگاه یوونتوس از کیت‌صورتی رنگ دوم خود در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101420" target="_blank">📅 11:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101419">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjU81E0s8OqDqVW_3UGwVSZUiS8prPOdIEUnGz2doZa6bX7OdqlEkpQ0A87MMtRutnGcT99QLZNUieWYcig8N0gsrUeeMG_BxxGw4ohm_2-3UTOmh1WLiBM1AONwvJb8d7ioPFfI9E1r0BqC4I_eSczIJmm3UzuJ0w6K5mc31A4YlBqxoAiII_83iRhiV42EfNT_iWryzGHz1mMH4uxYEPOx3vXnyzyIZFGsIBH5za1QbliITi-bPK6IyCg-hlz7coGAtFuKYtmTjcf87pxdT-wGyzeWIKBlTM39xnrqGf-XIxTS2BllCu9GFQ_AzjG8P4vgT1KyyeP9G2CNOiOpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101419" target="_blank">📅 11:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101418">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1b98bea2.mp4?token=PqlN1gTgwxrKg8jVfaZ-ddyWO526S6RYkvF2XWxzRSI10oEP5IrPs_mFjKX_8vrR_CDJx-wb0TV3ynggWcia06cBnqXZwfTNKypdOMJ8aOfc-H9HaipwkWFXI_wZlS-NcJhn0mlp8_lG14n5bI4CSmAWvV-ZvOSdyv5CAvrhf3VWPDF1ohggdMVtGwxea7aw8BHXKlpC3xUlAXjwWAKUTHG6Y01gkxeRT78UipsueYJadTh09-ktvcEzVIzo1q1wJ8WNqJ1AKgCBFDVVLO5H9JK2k8mdwlVY8a_c4elFAFcoi4bjawFNKnMvoftq83ov1f5bUh6FaHbjRQeZiA6M7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1b98bea2.mp4?token=PqlN1gTgwxrKg8jVfaZ-ddyWO526S6RYkvF2XWxzRSI10oEP5IrPs_mFjKX_8vrR_CDJx-wb0TV3ynggWcia06cBnqXZwfTNKypdOMJ8aOfc-H9HaipwkWFXI_wZlS-NcJhn0mlp8_lG14n5bI4CSmAWvV-ZvOSdyv5CAvrhf3VWPDF1ohggdMVtGwxea7aw8BHXKlpC3xUlAXjwWAKUTHG6Y01gkxeRT78UipsueYJadTh09-ktvcEzVIzo1q1wJ8WNqJ1AKgCBFDVVLO5H9JK2k8mdwlVY8a_c4elFAFcoi4bjawFNKnMvoftq83ov1f5bUh6FaHbjRQeZiA6M7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پایان‌یک‌عصر طلایی از سه‌اسطوره تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101418" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101417">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c9a3d75e.mp4?token=ZJiJxk5dpSOPbjdecLGFeuNcyHQqIhJnUYYUu7Z7ZNjQdBZVbBqx2Eo8wg7JU4kHty_L296nOpoclaNw0hrUbFHhiQ-OR8OIrHZ44yBad_nQi1oae3DjP-oiIbLeedDDr7gAd3h0UlgbyGPausFoZXulsZIkPTyr3l8DcUF6q6HJIlkOSdr3-KCi25YKlCIMqfUMLDnoIT6nc5C31Oqr6zQu229t9tu4f-rNWipTf2hffbB4CcS5lFl0oLDs-Td_GsAOlKFOQJQw87CndcyTMLxTlffsJBBW9En3-dqC6-Mskes86tFros7ZjeW1PVg9bHrh9f0iuNry_SypdmC8fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c9a3d75e.mp4?token=ZJiJxk5dpSOPbjdecLGFeuNcyHQqIhJnUYYUu7Z7ZNjQdBZVbBqx2Eo8wg7JU4kHty_L296nOpoclaNw0hrUbFHhiQ-OR8OIrHZ44yBad_nQi1oae3DjP-oiIbLeedDDr7gAd3h0UlgbyGPausFoZXulsZIkPTyr3l8DcUF6q6HJIlkOSdr3-KCi25YKlCIMqfUMLDnoIT6nc5C31Oqr6zQu229t9tu4f-rNWipTf2hffbB4CcS5lFl0oLDs-Td_GsAOlKFOQJQw87CndcyTMLxTlffsJBBW9En3-dqC6-Mskes86tFros7ZjeW1PVg9bHrh9f0iuNry_SypdmC8fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تک‌تیرانداز‌های مت‌لایف برای تامین امنیت ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101417" target="_blank">📅 11:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101416">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=nVD1un6Ku3dtxZ_5S7U_o4Toc0Zkomut5G5XVhAzpZIRGfQ7KASyR97SWO2125V8vUixmVfmlUnLs1-Zai0_gmYgynbDTUcFkz3ZL4xus5cgoDJpoABxvnJrZxFqg2sLOV7KKEFdMP7Wre1eq83YKfzgkarvw4Yg0llSzKP84FgCNg9vzzHNSAigVgC5aEsLGv43R24ApEhSdxXde_NtqA0geQTu2fh9aOm9Gtuc3SfX6nVj82z9KSiqt-eZ3UlWebxDuyQwGlUm8RteNeJAB2ivVvqSw8PgWPVknv3yAyd3Q6wlTElu6sWvlB98pm0y0qxTN-k6rZpORRykiBvFwWtMWT3cY7V9CfWkd68N76S3yLJvhyt9z-ndC75AL6xgDBoFtiS2x0QmhIqvQsVfyVDqwGtajhXaO5qQPO53eyRiYMlpXEyHQ6sesUpUk3j-Hz4qu2rcNjNCmLS2QQLeLfR-O1_kioDFQPi712Y7GHkd23ZwlgZgd4UdSLJ58j7IwvrA7RxGqDySgLDSk2BKz7vpSPxJGcTYe-7k59yDN06sMEJKdovN6G25Vp6LMA-6oVASToz1vzl2t72qCAV0Y_KkPP3N68RZBgIX_q1BJGjgpLE4UyKBnbx1KCJLR96XINRkO3L9SzqBnG_M0W86DpdaE-RwSkAQpWcv83eUUVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=nVD1un6Ku3dtxZ_5S7U_o4Toc0Zkomut5G5XVhAzpZIRGfQ7KASyR97SWO2125V8vUixmVfmlUnLs1-Zai0_gmYgynbDTUcFkz3ZL4xus5cgoDJpoABxvnJrZxFqg2sLOV7KKEFdMP7Wre1eq83YKfzgkarvw4Yg0llSzKP84FgCNg9vzzHNSAigVgC5aEsLGv43R24ApEhSdxXde_NtqA0geQTu2fh9aOm9Gtuc3SfX6nVj82z9KSiqt-eZ3UlWebxDuyQwGlUm8RteNeJAB2ivVvqSw8PgWPVknv3yAyd3Q6wlTElu6sWvlB98pm0y0qxTN-k6rZpORRykiBvFwWtMWT3cY7V9CfWkd68N76S3yLJvhyt9z-ndC75AL6xgDBoFtiS2x0QmhIqvQsVfyVDqwGtajhXaO5qQPO53eyRiYMlpXEyHQ6sesUpUk3j-Hz4qu2rcNjNCmLS2QQLeLfR-O1_kioDFQPi712Y7GHkd23ZwlgZgd4UdSLJ58j7IwvrA7RxGqDySgLDSk2BKz7vpSPxJGcTYe-7k59yDN06sMEJKdovN6G25Vp6LMA-6oVASToz1vzl2t72qCAV0Y_KkPP3N68RZBgIX_q1BJGjgpLE4UyKBnbx1KCJLR96XINRkO3L9SzqBnG_M0W86DpdaE-RwSkAQpWcv83eUUVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
پشمام بنگلادشی‌ها بعد باخت لیونل‌مسی اینجوری حالشون کیری شده و غش کردن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101416" target="_blank">📅 11:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101415">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aorQHkk2Yb56wKu7ircHW_v3cDb8eH460u9MBJsEXw1Kl4X_56Re52DvSz1X-PN8X42x1k6hBMWvzu6YC83A1oFjscT999N1SIPZVJKut2IlJyrGfyvh-JMcKcy2MIkpQF5q77uWCt5l5IYvc3J2nCFnonZJcUZRvSNA88KVetdtXXDMD9_dwvYE7EIzHlUXlP85fVO1XuCdDDISAIMiOGZnNiM2QGcIC3HsiZT0UUjrvWdGmducBqFGPoggn6A8rsCFwAKN87WOwfVlLwj4f2hYyfeFih7XF3MeNC6YhUMFRvwu6bHZ6z9jSwDQE4LsvhDJz3-0JzHDp2KSlgV7pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استقلال در فصل‌آینده لیگ‌نخبگان آسیا در سید اول و تراکتور در سید سوم قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101415" target="_blank">📅 10:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101414">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=WFj6Sq3fg1mO3yS3orqYvwHwx4W7l6PrsgwfWiCahYBJEscxZ7jgJLtFgGSqhzjkf2QCfyPADFwwI-huZPLdDCAn09sexL2u9vHK1yQO5LYEX2ukvcoEufQ1Ysxt7fFOQGF-WDwykaIAWbz0YJjgN1tlj5B4jCTST77-PZOAlhXygXuIiyF-SMTx5EVkHSh4KlvTvdho14V4imd4Ebf-4bO7CPO0yl-XkXAJqPI1i98i_p1B6GQdrXUFYHkE-E9W_MW3rGrUySQdpDf88ND_cDhxkruFNB8YDlpJ63eyekaOqH-GYf7BcEtNcEc06JlDxEhSjjFZ5pHf6SqhRX8JUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=WFj6Sq3fg1mO3yS3orqYvwHwx4W7l6PrsgwfWiCahYBJEscxZ7jgJLtFgGSqhzjkf2QCfyPADFwwI-huZPLdDCAn09sexL2u9vHK1yQO5LYEX2ukvcoEufQ1Ysxt7fFOQGF-WDwykaIAWbz0YJjgN1tlj5B4jCTST77-PZOAlhXygXuIiyF-SMTx5EVkHSh4KlvTvdho14V4imd4Ebf-4bO7CPO0yl-XkXAJqPI1i98i_p1B6GQdrXUFYHkE-E9W_MW3rGrUySQdpDf88ND_cDhxkruFNB8YDlpJ63eyekaOqH-GYf7BcEtNcEc06JlDxEhSjjFZ5pHf6SqhRX8JUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مراسم ختم مردم ایران برای لیونل‌مسی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101414" target="_blank">📅 10:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101413">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZcFX7_L1GJm-4viq5qbhrilSBkOK_OrP9cGlFCorffwsuXcEc_0AOxYksx3K4uFiS2n4Xl273GrP7go0a_iavzEFdD7XwXyuLtozPQYa6W_PL9V8tfRbsPzHfB2xAZ_j3nP7AEbRj9HYKx7jPDEYmfshRMSkFz-OfZ30TGt8-Day14Eyvu0WdQ9GkX-GibDgejAmxxwUFV3CvLjTH5sS6FG7XeYWWKntumPpqziZpdzdCmtUnk3XbUjYAYDcBGKnfGJZOh4p2aMGawfBwHkQ1SnOG-q5AY3wb6uCx2SxYSaE5pUWxlWE3SME_DGPwWECeieUoK51duMVTjkWN8kGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لوکا مودریچ در ماه اکتبر از فوتبال ملی خداحافظی خواهد کرد
بازی اسپانیا مقابل کرواسی آخرین بازی او خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101413" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101412">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=lS-lG9G5V8Nm5k7NlQJoJvBkvN-r46nSHmAd5khzdpuBKlvbBAry6bWokLxY4P-SJXddsb9HQ6f7L02NkScUoScTgE4N6J0qZ-RjI0gycKzRXYtsJOJbR4-aNnhsnC00VRXmyuWGK6lsjB_5ntRlOn1MRm8Uj82h7oyyi5__0XjQninE6wgdysC0W0eKv42fk_SKbwMOW0ZuCcXeK97hucjoF-k7j9G_XAM_8WsT2JkYREnS2fdwr62VLyKB1k1-d5-XHjCphhOCMsQLPHcqizoMz6rqLmqxA894cj0bfEP-BahW7IiZ2PJpv4TA-vLK98W2TjqGSsPkoqGEsKrmFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=lS-lG9G5V8Nm5k7NlQJoJvBkvN-r46nSHmAd5khzdpuBKlvbBAry6bWokLxY4P-SJXddsb9HQ6f7L02NkScUoScTgE4N6J0qZ-RjI0gycKzRXYtsJOJbR4-aNnhsnC00VRXmyuWGK6lsjB_5ntRlOn1MRm8Uj82h7oyyi5__0XjQninE6wgdysC0W0eKv42fk_SKbwMOW0ZuCcXeK97hucjoF-k7j9G_XAM_8WsT2JkYREnS2fdwr62VLyKB1k1-d5-XHjCphhOCMsQLPHcqizoMz6rqLmqxA894cj0bfEP-BahW7IiZ2PJpv4TA-vLK98W2TjqGSsPkoqGEsKrmFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
همزمانی شگفت‌انگیز عصر مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101412" target="_blank">📅 10:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101411">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=FTYmVZzVTG5MYgAETT85EBfduCXnQUXRF7o8zedjSHZAyHnCTa39HJwbaPTa4s3FZ-wQDh0bFoPhv6HmElNb6ISCFQ7GxSZmTxohmQoTiY70_QAR-inXJCjNXdr3slRyDvUoI5XbM-vgAxNitK2EGWSB6lxZYozrzV0k-7CGCyck1mEm31EGnEGoIWz2t7wIiVXYv2CdiGY_lN73topGImw7zdVq_K2Wxv-B5K5D8Qec6dnTAryyo8wWFlbELsE6M8yCPqC5oSE2QVF87K8VflD1n2k2YmFImWUNa1KMtNiwCQe5U-aQq0_I6O9FlvltNaN-fjTRkcHPsUf4HOAF6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=FTYmVZzVTG5MYgAETT85EBfduCXnQUXRF7o8zedjSHZAyHnCTa39HJwbaPTa4s3FZ-wQDh0bFoPhv6HmElNb6ISCFQ7GxSZmTxohmQoTiY70_QAR-inXJCjNXdr3slRyDvUoI5XbM-vgAxNitK2EGWSB6lxZYozrzV0k-7CGCyck1mEm31EGnEGoIWz2t7wIiVXYv2CdiGY_lN73topGImw7zdVq_K2Wxv-B5K5D8Qec6dnTAryyo8wWFlbELsE6M8yCPqC5oSE2QVF87K8VflD1n2k2YmFImWUNa1KMtNiwCQe5U-aQq0_I6O9FlvltNaN-fjTRkcHPsUf4HOAF6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
استقبال مقامات دولتی آرژانتین از تیم فوتبال این کشور در بدو ورود به بوئنس‌آیرس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101411" target="_blank">📅 10:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101410">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔥
▶️
اجرای زیبای شکیرا از این نمای دیدنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101410" target="_blank">📅 09:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101409">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
❌
⭕️
سروش‌رفیعی با انتشار ویدیویی رسما از تیم‌پرسپولیس جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101409" target="_blank">📅 09:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101408">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agP5WNZmNZ03FVipE1FA5Fk_7X21X2kSHXqobL3KsoP87IY7Ssi3tnvQPrP-Qco96S177Bj7oirvSrI0VgWpS1sy7Dh2P-EVLiP-Xi6XYle4k94As2i4sUwtQ6xa_92_5SaNt5QRafanuzk9CcKUC51OljBEHPgR7tOir-5CdiKJrpaOoVkkiurfMn0h2kLpsGuUbVf06ln-1nkaco0kt0qV0CHrgrBW9Q3yl_S2AIJ6HKVVU4ETwiAGmzlJIyThXMKV0_Zcj1JUym_Q0U0YH2Z-_3TvLv8kgbzmKJz3E-B21yN8c0ne7vqYPSDA7_0tl_XmXz4J3aOAH4nefdVL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برندگان جایزه توپ‌طلا جام‌جهانی از سال ۲۰۰۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101408" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101407">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=bdI5DojQp3A2Wn47M6JXXiSSM3_t3Ap_H_-3SUzefFpcLgUVXtD2-lN2546HJlSstYqCuJTnr4F3MRypN8BIzH03hGKOuW0PuNVIUKJfYq5-485_SeEZbN9DG1rXPdgUFVy7YsVSNQ-NB2gyjqX4GySx3lI5cv36BKABr2owq1FGnMOLBttBDWXcNzHSUnYMo7Flr7Z5rbKBljvdEXfW8HuTQLkTxn6Os7goL4YzcNWGZzH8NQM4TMt6_by058htYk6h6IJuaPrcP7t0Owyy16M-dbLFhhDn1TUSioMoVP7Cglrol-Ueu7tEdAriMOV-i_7DQHIKHjOqzA-0KkdM1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=bdI5DojQp3A2Wn47M6JXXiSSM3_t3Ap_H_-3SUzefFpcLgUVXtD2-lN2546HJlSstYqCuJTnr4F3MRypN8BIzH03hGKOuW0PuNVIUKJfYq5-485_SeEZbN9DG1rXPdgUFVy7YsVSNQ-NB2gyjqX4GySx3lI5cv36BKABr2owq1FGnMOLBttBDWXcNzHSUnYMo7Flr7Z5rbKBljvdEXfW8HuTQLkTxn6Os7goL4YzcNWGZzH8NQM4TMt6_by058htYk6h6IJuaPrcP7t0Owyy16M-dbLFhhDn1TUSioMoVP7Cglrol-Ueu7tEdAriMOV-i_7DQHIKHjOqzA-0KkdM1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
بسیجی‌ها گله‌ای ضد مسی شدن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101407" target="_blank">📅 09:04 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
