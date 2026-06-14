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
<img src="https://cdn4.telesco.pe/file/ByJo-9dl89Khdp4gk2KH5hMFuiT452PcrZi90zHfIs75IwHbZB6rYJgkT6DzNhuVUQoDv832gkclwpTzaX_cysIlIBR8AIPACTNcGXlJybR-IsGuR3Xe3ti0whTYux6uUjSzM_lIfb5wacgCk1lC7CbfBBSBG1aIXU4iPCbFZg9mwI3QifZAYkNM20cAViU1OOjuFS_VXvdHPPtJ0leyyzOWpPPBNcDr3DCxXfqRpYqcgJPFWZBhRBgnVBgF3RyNVTuOt9jCPuheSRZJeM3isMkzZeklhwwGCjVg5NVQfu2iuTiS-3XFjc08PfKdr-V7Cpv8labVVcMU1yaJz1p-Xg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 244K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 01:32:36</div>
<hr>

<div class="tg-post" id="msg-23477">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-opPYMbvEDcylL2qmIyi3nUqCkOEx32OnIR40Ix5LBtLJrBxS7XV77H6FAnqVvcSvirVY8hswaB6b6kNP1O2canzg23MvjHnRh5bnsjIgu7svnVuLorZEMLyUwI_5LrDb-5W8jjT7uXCPxsIHef12p_eLhJGeKMh52Zi0hxHNQu4XFX7CwBft0lndnBLUOpsaq2l5hdnYvZDfiepr-_wKUDG1Hm2_1Dc4ncQEpYly9lzEEfgToc3Z3l7TNdvkB47cT6Gg2vGtMen3QEsUQqPOc5b-Gs-PtwG6UvfYAiXn3tf3EUfiRyUnCqCQzKA--ZToQi6P2HWhSGHrZjdTuzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/persiana_Soccer/23477" target="_blank">📅 01:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78498ffe8b.mp4?token=laQc5Yh9obgBrym833Ha8Ic88LARdUqxPo6QYAP_8wxoD7aHNG_Wk5QtmLV6WXD7BAhQVbY-vpH2xlwHkHCThLn1i5OqXRsohBg4a1nW3gW6PtO5llPCmSdORuk-OMgjxAVTdVF3zw9g4vP1N-Qsocc-7ge0kDHSKDfP6L58ZLLKeDPWYFVu__7IOjrIxSMIDB_NtD_kEJ2sX7AF0Rs-edB-mChux7fv_dgEtNxd81zYTHXxKsp_WS3x-mVhjzPqrO1qTqqUoSj8NcnvkdUmPziFx0vvYFvGv3yLZrB1OVjZo5hIgarMdpefm2GH4b5mJnZSw7VDOSKxOfly0J7a7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78498ffe8b.mp4?token=laQc5Yh9obgBrym833Ha8Ic88LARdUqxPo6QYAP_8wxoD7aHNG_Wk5QtmLV6WXD7BAhQVbY-vpH2xlwHkHCThLn1i5OqXRsohBg4a1nW3gW6PtO5llPCmSdORuk-OMgjxAVTdVF3zw9g4vP1N-Qsocc-7ge0kDHSKDfP6L58ZLLKeDPWYFVu__7IOjrIxSMIDB_NtD_kEJ2sX7AF0Rs-edB-mChux7fv_dgEtNxd81zYTHXxKsp_WS3x-mVhjzPqrO1qTqqUoSj8NcnvkdUmPziFx0vvYFvGv3yLZrB1OVjZo5hIgarMdpefm2GH4b5mJnZSw7VDOSKxOfly0J7a7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
عادل‌فردوسی‌پور در ویژه‌برنامه امشب جام جهانی به این‌شکل‌جواب صحبت‌های میثاقی رو داد: اصلا حرفات ذره‌ای برای هیچ کسی اهمیت نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/persiana_Soccer/23476" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fa8e48e0d.mp4?token=UTBrYjEQsruN2B9TGV6FsxHS7O1JDtWD76bdTuNgqnlS-O_1LGYVbOLN7qcirq85w7CP0Y_7yALV4AsJQulJ-IrJs07-_gUgR3PNod29YKOYFMNpHHehP3IXRNs7ERsTVa81FX8x4qk4w9zdzk-_hfRhWEeIDyDaL-iHymu58_9HWBHD63UtmAdmeSF6sqV5Dx_Btb5BQSC6y27QAk0giJH7OmgmSCIUYxIU1TebxhvSK41vsFN8ZNEaTlcZ5gB6CxkDNzPes_XJf22aI-GEkaIW45dJew947x8oi-a0krMNLDrIA0xsA4pOy6mVH6DKy_rYXfUjm2N-ztjog5Q4BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fa8e48e0d.mp4?token=UTBrYjEQsruN2B9TGV6FsxHS7O1JDtWD76bdTuNgqnlS-O_1LGYVbOLN7qcirq85w7CP0Y_7yALV4AsJQulJ-IrJs07-_gUgR3PNod29YKOYFMNpHHehP3IXRNs7ERsTVa81FX8x4qk4w9zdzk-_hfRhWEeIDyDaL-iHymu58_9HWBHD63UtmAdmeSF6sqV5Dx_Btb5BQSC6y27QAk0giJH7OmgmSCIUYxIU1TebxhvSK41vsFN8ZNEaTlcZ5gB6CxkDNzPes_XJf22aI-GEkaIW45dJew947x8oi-a0krMNLDrIA0xsA4pOy6mVH6DKy_rYXfUjm2N-ztjog5Q4BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسپویل‌ازصحبت‌های‌امیرقلعه‌نویی سرمربی تیم ایران بعداز دیدارفردامقابل نیوزیلند در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/persiana_Soccer/23475" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23474">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdZOfutJj1LAyX-6LdYcRN419jrvWIOKoB1WfxXIVU0WTiJSzfBt4QmeKf67A9JTjhYt0sauj7rEu_ydDM236ZwxT8syMw_wNIOuI7hwNo_7tAHru1c2k6sJSaxEMyvBD55XS7146nU-2t8EJs-ZMsthHdiMSCha6SzhAuvmNTYAFKnN_X8h10okCh43a_OUbFvcIsHADqpD9l9FVGFobAC_lkFkaUgLmX47cA4Go_UaBl-nAJFZnIKgSFCr8thY7oY3n3BWIZ2KcfH1QFJEICuOwy9fgx6VQaTzW9t62XVLtPZ3j1z0zaE_c42_Ue_tPVwKRBw2G3KCrLSQGL29hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
میخوای‌ازبازیای‌جام‌جهانی‌فوتبال‌پول دربیاری
؟
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش‌بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون e24:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/persiana_Soccer/23474" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaP-LfvB5s4AfAlnNSNQ0azsuk6JeQFM3Us4j_wjpjyJeH8HV-V32bUwOQ074JVP8WAInX7VfAnRcwaIYzqt7GtJ2QBtw6zCEi62fAB0VkEpVQbgQ1Glm30jRAxwPrcPgMemZUVbsicwzd98jsLTs-2NfheqcKHAygqqwWBQfQXyltdU8JXI7cRQumYNkUX3kBysfxzGb_Hr2y8ttiGR0K05DLzfeiPNqPW1JbzQWbSB3y0FdAPPI3J6W_CMIIIfdLubeWW2tOGZkvuEPNOcikGVwiANr_HS33oj594yDOVgRSRySMGUAong0SrfV8xp4BFPff29H38v8LW-LW_dTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ نخست‌وزیر پاکستان رسما اعلام کرد:
🔴
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد؛ جنگ در تمام جبه‌ها پایان یافت، مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/23473" target="_blank">📅 00:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX5KysDQXtzoEB0gfaaDvLAziLbAYApI7cpapFOmtRIaZp11_WA7CDZfVgqwVMx_u-X3bu4ZzQdg_Hkf4wxva8V0yax9MMwJwUKQ3GkCSPQorfVBppVlmSwSoA3KqofU5dm9syNhUGNIWh-2jl1HO5CmxPtdmol9zCgM9PFlaW3NCljkEZXlevXKLFhMfPd1XzwAtpeQXHtbw90YoBbQphTyYM9Gn1aDB3AKSByMbZQoWfkviflLWYmgD849bFtZlRYgiQ90YZ0PuG9k2Pd6DTDSMmvQR6PJQHz6IWxXJGRotrNybKXmgqrLFl1huH-Wp8Y3najhFHyhe6YmJ4toww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
#فوری؛ گویا دقایقی‌قبل توافق میان ایران و آمریکا رسما امضا شد. ترامپ درگفتگو با وال‌استریت ژورنال: بزودی بیانیه‌ای صادر خواهم کرد تا موافقت ایالات متحده با توافق با کشور ایران را تأیید کنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/23472" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23471">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfDDjXaCObsHk5n4PFssXkv5LbCbm7HX_9Zh10uITlKSMvQYSj_yYe2Jw2zZ40FOF7kw8HPRStU0pBfbbfUzy4v_9CHMSPoCFpTogOCK9FfX-EtFp7n-BnZnBsW8WRfa4MzMGBrJiem8CMxkOUqTvPpMCBpkwfqjLwWMHi3OpbOTB67YfbNrT64DihjGZSWgmRo3ATcQsDLKhkPlLNTMmOdTyiazwBJn8_hrwjW1MlXYnOKu4ZngaTqQfrEHuvPhpGu9tJqBHIgdyEihWjBQ9hKbvz1KkcRZ6arEpxrPhSvf-dYVD0Y8GdJrOKn10P1R3iIqopdfv7iByc1BUh56iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
انزو فرناندز در گفتگو با ESP: به سران چلسی اعلام کرده‌ام که برنامه‌ای برای موندن در این باشگاه ندارم و قصد دارم راهی باشگاه رئال مادرید شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/23471" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJH9x5GgOp_BSwaaTFkKwz6C_9k2LefSQikoQsXtJyKiFS1lqCqXH-lBTfbBVDpxnUogSsfKeOUG414I3smO29UDd81qKp_JyohtabXqrByCnw1CU1oFElmzlfqypLvKypP9t61qierDYjSqlo518Fx7kW8dS5Zc9k4NITYCNKAZoitU8IFibz8EbkLmFpu0ZK-aZ-mfa3Q3Wy3UIKieLEX97lTBY9V3QX1wNkoPMXjPfhoLRcn5H3Ywy6UqP1tyvjjG3xOYViZ2ws8HFNKyggL4avnI6g61nW8I4OrHFiQfdRAmAmRerWdRqvseVew5Y3vR91YyfwqrLi9UU1mh8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#تکمیلی؛ رومانو: روبن آموریم تموم شروط باشگاه میلان رو برای سرمربیگری پذیرفته و گفته با هر شرایطی حاضره به این تیم بیاد. سران میلان هم گفته خب باشه بزار حالا ما بریم دورامون رو بزنیم اگه گزینه بهتری پیدا نشد با تو قرارداد میبیندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/23470" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDn5avfzB5kdz36xohNC6dkU352tRybQCxVxsSCFFxN3VWUz-tYQJtiMQOu3t4fXxtMpDpcn-IW2S9UFeLUn6QYgnN74-KrXSLplCzoq4MV0kDudqvc5XzS55TOmqfW3xp0e2C8ApZ1I9j3y8ryE8uMWLZ9f-K1xpyaLW9x8sUpvnrwpGpz-rwItHFLgeckgwcnxJvcktjDo9TCxEwG1KU06OnwEAW1-tc1fVxHMRGycQkSDVFRvleg9JMWkhR_i-YSy9UEgpUkKbJNxPNwOPc2u0ABdBHIpRbkqXt2chip43J9ylUlkbs4ulsGP6-ZEOO-Wfa9Dci63-eGCQY7OBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/23469" target="_blank">📅 23:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23468">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8H_gPz-66xG75eo3HHD6nnx6goSs8tIRDmT1HMjxM--06BTEx3Fu0rWYfi_LoZ4kzOJw3wWSHAdP_ZFMubq0i6__jLSUbcyhVRnnEbrAjb9f_r6itAFNqfmp0_dnEveeBKnwttgxoETCC6LrtYCEwOP0xswLm9k4gTHuc-N0jH-0lizHpWiYPW8l16UfCFv7bajxEBlxy9G1hxHxQQroGTA5ruFdgDCVdyHDd7l-RG70GFlWVYiOVac8KMPe0DI6ELzm-Hc2oAlK3igTinG1TBUSupaM121NhQr-lbAnQ2YGfdhQBQ4gSEUVAybU-IKTISBscJeodlc00-E9Sd8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاریخ‌فراموش‌نمیکنه بچه جون؛ یه زمانی برای یه صندلی اینجوری داشتی خواهش و التماس میکردی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/23468" target="_blank">📅 23:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23467">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmNLS0NQ7OP495AZdi-DFq5nTswnzJ4PJAGOPTUWtz02VBcAB5cTe1N5qegENye8vKTRg3VNUwi8jpifIuGq8JS-BzBmxkvAsgM2haZca9iV_JULP4BtczVuL6Q7E8Z8Ww7PbYPbOtoB8kMwIWRu4rm3c5eP6E0GYlAU8M4xB0f8-rFl3d2Yf-MHGuOP4mC30WZCyWOciisG9kRKUQ-rY3z8OGeCy_Lj4XkFa4llwyNCaBcGzgYeHMWMzt9Z-AmCfyYLT4g8C5eKtHG_QOo-isfHkL1RzBeB3vIwJroP4DlX9QBQ4xEUzjAzWJj4UidkRqKh_CWRPngKOK4refvkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/23467" target="_blank">📅 23:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23466">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=jGBqK1Fvvq3cAkXD7OPWm6o4y7JzaOGCP26fABGwsr9PXi3ZX6VFkDS4Cwp4Z60PI4KS6_uPTVmHDDLqLeBR1Kp4WawMHEh9fvJmjL2fVqGHBC6vCcL93H6y0ATDLVOTWqzXwwG50zJl1O0zpPQL4SHwC9y9NkC_NV9ZkYOALYxNz0mczmnSdUQLwqTus7WLEkVKxZBXV87w7g27sh_plY5xAkY1efzxJKKFmZEWZ_VEHshQyTVawp04uEFVpn87UOGLuAaury04hqGHjPZaNZ_aKHQ39U28TTNHJVA00OYSda5sCfApp4Uh1xokO9A0SeUrlqJdMZWPhE4RdmmryTOtptd74jmnRdIq1ljZagwtcUJDTczFpSv7EIrwLV5npW1iKGQ-WUzKPKlPI6BCwzeQ1r9v-7dZt3Bj_UHL2rlmgQlDhjw6JRlnCp0rtPl_aVw0KmWtgwtKdFEsJ5DzL7Pa9s2ja1ijtoBvXuCgSZAjvaXfU-PkfMOW_WRfQ0ux0DWdA88JuRA--9Yk8I8Ebd_-3H7MZB9EkBTtxYPQ_UIWjwJq9Ws9Agcdm9zT_Mt2Pzm6FM7vf24b3K8Lfb_0_Q6f_zr-xc73K5sTKWLRiPqbBPHfdDKYoA0VfMHYDeWTAjDwIrnYwiFBORcizE17EU0vf4-gl90Yj4u7gY65y_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=jGBqK1Fvvq3cAkXD7OPWm6o4y7JzaOGCP26fABGwsr9PXi3ZX6VFkDS4Cwp4Z60PI4KS6_uPTVmHDDLqLeBR1Kp4WawMHEh9fvJmjL2fVqGHBC6vCcL93H6y0ATDLVOTWqzXwwG50zJl1O0zpPQL4SHwC9y9NkC_NV9ZkYOALYxNz0mczmnSdUQLwqTus7WLEkVKxZBXV87w7g27sh_plY5xAkY1efzxJKKFmZEWZ_VEHshQyTVawp04uEFVpn87UOGLuAaury04hqGHjPZaNZ_aKHQ39U28TTNHJVA00OYSda5sCfApp4Uh1xokO9A0SeUrlqJdMZWPhE4RdmmryTOtptd74jmnRdIq1ljZagwtcUJDTczFpSv7EIrwLV5npW1iKGQ-WUzKPKlPI6BCwzeQ1r9v-7dZt3Bj_UHL2rlmgQlDhjw6JRlnCp0rtPl_aVw0KmWtgwtKdFEsJ5DzL7Pa9s2ja1ijtoBvXuCgSZAjvaXfU-PkfMOW_WRfQ0ux0DWdA88JuRA--9Yk8I8Ebd_-3H7MZB9EkBTtxYPQ_UIWjwJq9Ws9Agcdm9zT_Mt2Pzm6FM7vf24b3K8Lfb_0_Q6f_zr-xc73K5sTKWLRiPqbBPHfdDKYoA0VfMHYDeWTAjDwIrnYwiFBORcizE17EU0vf4-gl90Yj4u7gY65y_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی وسط‌پخش‌زنده سرودملی آلمان رو خوند خداداد از خنده کم مونده که پخش رو زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/23466" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23465">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی2026|جشنواره‌گل ژرمن‌ ها مقابل تیم کم نام و نشان کوراسائو؛ شاگردان ناگلزمن در ایستگاه نخست رقابتا حریفش رو هفتایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/23465" target="_blank">📅 22:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO_-L-YpaDK-QWcwmXTQFcejECtsmMAPAvTk1CbBUXdCTxIqJP7ZNfkSUWL_GUI9JHx71UxKDPrHt8_tE_9Lc7ZjSfwQrhw2tbAFb9zSEBe-BUf-b7q_t0o9M6IlmNV1mjOu80Wlor8PGeEAeBGaSKeHDXjojTV1coFA4-Bfvae2uRjyoZKyPaW1OmmlT9_4mx9MU6YSY_SjqO_b-S5FdrQUEwIW80x3KfjJPFykoCcnxYePiplSBpoZXy3peqhv_pvGvDXbNZ7dPnk-347OgRqODz0orczIyuVFzEaVFlx2dx7p6sNjw61KneVZ9u9RUCT9qalyKfSWXSUGpSdSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23464" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_bVHfdUM2rypNlgEMX-NEvfVFZf00WuhDA7kELoFzxA8H4BTbFnGUKss71Lf_AAMw0IlSE1ilcFqrTDCGR2mesHFiiBx6xBjRaIy4H7vGuBk9mMY8MRlHrzzfdlHYHtxAnivvXnThXC6_g4p8NS2NUMqaFo3gLRCDVqqXkgvkoEZMZYRFlIx-FKCa-oW5vAA0XUO0LVqHseZjwexgCzLd882ON8V2c2A6yEuntncQb-K8e41ajSSJ0ck5zOuWpix2Ci4cCNM8kJZJ1Stz3Rx2RUZ6Fpd2-YnAv7f94NbYU5usFpuGtxyKRI3vJewBzADOEoo4fLqDbvoyUVmoEjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nw41JFDT7y69H6K7NI9MFzbjnkBgMV4J3vVdy-1DimgmXGNzzlr5G8csF3n5YtGIXpI2rtrdbzfzC2FZooX1wUb8UBdS2LPohb-seJTiOR991XhKIAhonar_tLydWCOfDozXWb77HD9bs0jY8-xbrhAWsa5CYRlnT48OOYxJbQOFzKdz-SN5_cGYqdZ5fMdeRz7JWlOQy52oXDDo8vwht63PoC3UReBJvPJQWZYMkkKgm3EW9nsccfBIVBZmCtIcYeGz2EKrDYylJCBtD6_30XeOHde0nXcKoA0jPKWj6AoN2AsYZRlvGolLCIdekB4-AuCwjV1VyE4NWA4lgsPnmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی
؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23462" target="_blank">📅 22:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4oaCp0L7ezMBTrKgdVDvcnf5PG2O3e9-EbuLGioRT5ZgzdbBq4uf2bNkhOYovqhhn5U13RJIgQyYKAvxXRxe_OKpEx7Y_TJt-ImhsNc1Fq1YxmjRS05mBLsqhED5A43gYub0R5fABI2tU0gxsNfV4y4vjV9SUKwyhjrBZeUf6rw3DXpDxfCB2BwbeE4wM66mJJkAwx78_SManRh5wA91D9ouFJ6fO8LO7UHbk4X-9XNa2buVyrxyGqkoMWNmDFikH-VYVTv3uY2LJrmZo60_oQleJn11xtuu1z_Eg6F8Xu0RTcSz-iDGXu9S802AoBT1CkkjR4gE73sn69gE1xcqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23461" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=iESBe4mTYHNyjKbAAwUUOLS2x5t1X33GsGAiZr0KL41A0OmASQcpeuR0vcOfhWjmMbnB97PzLR9H3BcHkaB0cfwvU9BIe1ZyA2aLDmPTCS1avV0PKEOPNlZuQyym-txXFJ36QEpL2yEMkZnEKBeD9F9rh-QqkrfBfGA7sQCElBGCt1FGbrP0wd635wEZO5IVk4IyVJ4f1R3PwhmI0K1nLE3r1mNBVdsuqHTdf0dhDhUoOfCIcbE2pC2HSNSI2iaU2QtBdqK2H_AGKla6U68-pyXKw6cHppmF-rA3VmZOnNiAHuePreca07BA8vGOHww7cppzuKYxETS0Cw3Cbq7aEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=iESBe4mTYHNyjKbAAwUUOLS2x5t1X33GsGAiZr0KL41A0OmASQcpeuR0vcOfhWjmMbnB97PzLR9H3BcHkaB0cfwvU9BIe1ZyA2aLDmPTCS1avV0PKEOPNlZuQyym-txXFJ36QEpL2yEMkZnEKBeD9F9rh-QqkrfBfGA7sQCElBGCt1FGbrP0wd635wEZO5IVk4IyVJ4f1R3PwhmI0K1nLE3r1mNBVdsuqHTdf0dhDhUoOfCIcbE2pC2HSNSI2iaU2QtBdqK2H_AGKla6U68-pyXKw6cHppmF-rA3VmZOnNiAHuePreca07BA8vGOHww7cppzuKYxETS0Cw3Cbq7aEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های ابوطالب‌حسینی به بعضی از مجری‌های بیهوده،دلقک و بی‌خاصیت صداوسیما فعلی مملکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23460" target="_blank">📅 21:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8GDHVyMSwB0WaxHyAe3A98BVZl8XsuMYSno4R8oWUJZrNAPTG-aZSU1hs_GnZKUArQ45HinPGz9meyUjVx9RDsZ2e1QSdA-Wnc-rGhtGtwFRW6-eeGQpP65AzdEFzgcTYc8W6f5LMywJtGL6-QSD7aGJk9XPqK6Jr38Z6VLdsdiI31MPXEYuMstCjKwZr0sCCVx_cVAhSdAhAMojV2DVhPjmbVsousvAN1knxc6sYJNEvU68banakZugdmebx1wFdp3XDrCfP2ATsjG_d0FRGwfioZZa7WVGPmAf2pomRrUJcqeU015f6X85Nuvm5LKcU6sf71JKqNIiIla9dcg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اصلی‌ اینکه اکثر بازیکنان ایرانی خارج از کشور علاقه دارند به لیگ برتر برگردن اینه که چون شرایط کشور خاصه و ممکنه در هر مقطع از فصل جنگ بشه و بازیکنان‌ خارجی تیم‌هاشون‌رو ولکنن برند لژیونرها قصد دارند با رقمی بسیار نجومی تر از دستمزد فعلیشون در باشگاه‌هاشون…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23459" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeXlkJvKbMl_KSpxzqHjbinfsmTO2LWnh8elmyd6a60twbbvOExWK8dmnD67Xo59gbqnq3uH5lhBZZLAgD2eJX1upDMgdvzkeClJxA2Gb-hZ3r9WXG_QtzRW7pdvNHcxSl04y8Uod3JjtdfVxJkj3ZHijJUW6zI9PPJkZdD1Gg58ujMFFHMuLlLyK778EmDu1m_PEwDA56-igZoYdk_jSBlJ_LwZQ-Ng0VU3N9rgEQM9vMlx8tFarpnvajsDNzhrGDV27kFFiedYVne_1CtDgDubXW0kget4PGTSN2mEau__sYJuF04KrUkBco5pUTTipHxohzsj5TEaqZmJUo4YPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ اولویت اول رضا غندی پور مهاجم 19 ساله الوحده امارات دراین‌تابستان پیوستن به باشگاه پرسپولیس است و درصورتیکه کادر فنی سرخپوشان روی این بازیکن نظر مثبت داشته باشد جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23458" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-9mrTb4rS8JGwe1eYAkWQYsJHodWhqqyQDb_TMn3crB9_qaNX7h-N3pSy7L97zfE5P5s07suH1_NxCi2JwxGEFBKGOilNMV9PgGjmni4PmWfmZLCHYrIrZV0kOOd4r0IKkR9jW4MUXvvil6bTcdJWytKvnTDq4IlOTTN6XzB8MwmntHGE2umgwZi2EASpf6ePmeYlMAC38phZbqdXKu1zdA8dfCmIwv4WXxNNTxH16vLtarA3A9ltf4NPtN0EjS3FqET8QEfNi6c9DFZs9Rrq-iQhG1P7OnSCiy4AdLWaUQGl-MA1B7y3coBgAxizMzfj4XwfOT99dHaLAaqHC-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23457" target="_blank">📅 20:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvX9BJ7OjLLASqYWuqI4uYPEDyf5qHOM7IscyyL6QzqElCEzBAt-TRSxA0mNYR-QwhVVw2ZRhYyOTKIU3cHckrZYQ_R1cnbLGjJ-GNWwoX8RsFCn9LGKpI1Wobuk2Q2lscuc9V2Cv1a_E2WILnkKOmwkaN2uAgMhMGibIN_V9YNs_BMyr1bVQaxoTO_8nucZ2DST0yENj6rQPKPkBqOeVEtelI6TNymlntjwI-Kug5DkMpQKcI_MC9EvqdyA6IZwQt7xsUFjP3K0PovEF8cG9TbAee-_IhSSwxJzB52OCs5MkjLwQwjn93hb2d4mnUvHRZQT5Wxzy5dhbtAGeB5VOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چهار خرید باشگاه رئال مادرید در این پنجره تا اینجای کار؛پرزبرای جذب‌کوکوریا 50 میلیون یورو به تیم چلسی‌پرداخت‌کرد.درحالی کوکوریا جذب شد که اکثر رسانه ها خبر از اومدن کالافیوری میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23456" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=kV6i-q5JqATGC0EGqHNCunlZF9NtThqVHazTGADyuExm0f8yEFosO_iFqdECUyV44mmAlesD5B6icky9Xj5zyCy1SlhvR3uvSo-ZqIPnp-1zkPaA9pF3qqPbg29e0kixZ_u7Gsz7H5CZQ0UoaWulJFKQjszDPBExYXXSsU__XJKLfe9kmkDuisJr2pg80NZCixGR8bDfMcOLHbeQxGy_ft5WaYLCIf3_mJEfMbBvZjxsOamfcPXOaR1Ve1OJE5kS6V23LRSpP7N8eV-iiH8hObXt57klTTsLwgW-IrsZaVJu-XaJ4UBTBLXDJJ8uYC8ao7FWv1qQc8qfQZn1T5t8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=kV6i-q5JqATGC0EGqHNCunlZF9NtThqVHazTGADyuExm0f8yEFosO_iFqdECUyV44mmAlesD5B6icky9Xj5zyCy1SlhvR3uvSo-ZqIPnp-1zkPaA9pF3qqPbg29e0kixZ_u7Gsz7H5CZQ0UoaWulJFKQjszDPBExYXXSsU__XJKLfe9kmkDuisJr2pg80NZCixGR8bDfMcOLHbeQxGy_ft5WaYLCIf3_mJEfMbBvZjxsOamfcPXOaR1Ve1OJE5kS6V23LRSpP7N8eV-iiH8hObXt57klTTsLwgW-IrsZaVJu-XaJ4UBTBLXDJJ8uYC8ao7FWv1qQc8qfQZn1T5t8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شهاب زاهدی درباره عینک خاص‌ش در برنامه عادل و عزیزم گفتن‌های عادل به شهاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23455" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23454">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMsenNJOXQi16lOUTOH0rIG7tApGWIZ-N7kiPRZKfQUAI06clP8xiWKJz4qPVzxmEGjeRsB-vCoQtUsSYMyXfMNqm7sl0Agb5GXOuhmsKSFPg3NiVw0mBlgzQLQqmlwAYkE-geDj6hjZ6xolH1-h_lQKopn_LZHkSIVUsa0fBHNs9PVLY--8TXneana2P1fpe5qtD7WtVnpoPw2KXD6KZEXH-7zXPmRuAv4jiA3dBI_sgdmIiX9oGcD3ZIJBjLImNEBP-vUvOrDD2RWGPK06GSNsmiWqOhTN_glp9e8UJJ6w28Keyk6bXVgaRJlQZPJpOaV0DjqjZs7_VlVCb73wrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های
#جام_جهانی
رو بدون استرس و کمترین ریسک ممکن پیش بینی کن.
⭕️
⚽
آلمان
🟢
کوراسائو
⭕️
⚽
هلند
🟢
ژاپن
💳
حسابتوبرای‌این‌بازی در
#رومابت
با ارز دیجیتال شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
24
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23454" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqUmJSjyb7lPvxyYQ1h5ooQmSBGr_2s8nP354ThiP65nNQiBpJgHxJ-shlzMHavSHSUM1GgkA_9YkpHJ60JAAsCY0PEujEQOyXBFvHeShaJ1frW863L52Rs0TTyI-aHGAO4D8aEeT62Htx2CcS6pXVQK-HM79uGR08LEjoanlnRbq5eOskE-FD8W5VxknHA2i2ZS_nElVRNs3z6FrSj-bWebdAlfRZivMrPqIa_ANnCZIYKM_9frH7Bf77DWozVmIWDflNaq83iGGSboEmf3Fbx78tgvVntsqsONB8SO7dNfm2dSKgDQLITWviwsFNl3sKaWp-YtNG0qLr_F8XdiUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏐
میانگین سنی تیم‌های حاضر درلیگ ملت‌های والیبال؛ ایرانِ مدل پیاتزا دومین تیم جوان این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23453" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23452">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyg-ANUpF4uk8wiV-UCKktRsRftZLjExTni_sYL2ww-bT1zpQAdanhQeaG8bpqtvC5dAqdBO-V4wqOc-UJZlkr_ygK1lCKnjkusMOUe6kXl1X3PMHX8mcO4FC_BeFYm9X9wduHeoLVbob8KZjS2hQI8OTvhcno_rwWXI08Ugppz1IyziMTii5aUVg1crdAqsb5hX4AnKlf71QgVjFg15QqIYjAadWD6LBMAZPCPgdwOxHO8Eh9QVkJeRKDZ4_WVb7hQRsFurcDL59NSDhtj0wBqSJN-gi-7IWl0nd1KYHFfHvJM94qvlC6MhEeK25pLkZ8iiILyyHRXvA6BtreAPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23452" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u77ejBKK-aFHkMc4a2NzaUyJZzfyypEbmLt5AbdlcXUR3emeICktC50KZiepqkukf2A8k9EoRxNGpgigZOMG3C2fgQgymSizCgGrzH8rc3bPRNJeFv_aQivQPONoCThfsfy_9oT5TAPwwnH7Q60oF2N31SgaZRXnHsaH4_OqOYQrC-3YAxESNOO1eJIQ9mqx01d2zrmO-QWiMMPsXQFWZ7ddt4zoMXmS80RKfYqthDOV0KcGkjU-x17V6WzYaa9qge6895k4whRi3zCDNADdW8MsfMxGrpWEv1Hz2G-oLNlHW21vhirijuF-aWOlSQSVkpay4Ol-Hnhmlb-kvFSrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23451" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGlXIDj9e2ls1zwsFITN_AJ0JF4ywLtEDemxFakQ3V7pJle6R0D7ZvhU1nJWIl94TBiI9GOFOtY2VbOXTdhWN12_clzlsgc91o87NcSyI4b3BwJ7TkAkigQHWkHcd-veLXTc7Wn-muTM5XDV98ZX2WAlYBu_OF4oyHQFatLDzudtwiZFeNDXfPO-7btCYPRUVZo_XkjdaNcxdxRohACwoQhKK8v-0ta0GIcV1nAdDMiKi_ymSnUlFTGuu0zpCTqaKQlfwaQoSj5fCFAJv7U3MvKo_TWFNNkX_vwlGOmZI0Z4OLcFkxmU1iH97vOCTLcajRVZCxlzzA3o-XRHLaBbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23450" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=g_rV7nU8NVUImbhZPrisGP_3mv9Yh2SI-31bBRjK5j5h0NLMzqb1nU7XxsjqPJahhquLWbzDFxG6wjJKqp0NnH7mSs3mhla0O0R04ZfknoupMCky5edbw522E967VFBG6KHtxXL3khdlKliFFFqpJgeK7JhUrLe1MF-Cbi7mN6QTW72FdUIJWQA6kGvZweO239rOy1pbejNjXI_0qjnR-K45xOZKlpzqNX3PtlqFt1ZT13fXCJfCQ8jluT8cTEKQyHezPM5GC88zhObxMPCkhYnTjdPJLR5ErHNGXeF1Ony4OHC5Y2e-aEbUxrQrV8SMSNMS-0Ktkrl2lxfQCQ_vTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=g_rV7nU8NVUImbhZPrisGP_3mv9Yh2SI-31bBRjK5j5h0NLMzqb1nU7XxsjqPJahhquLWbzDFxG6wjJKqp0NnH7mSs3mhla0O0R04ZfknoupMCky5edbw522E967VFBG6KHtxXL3khdlKliFFFqpJgeK7JhUrLe1MF-Cbi7mN6QTW72FdUIJWQA6kGvZweO239rOy1pbejNjXI_0qjnR-K45xOZKlpzqNX3PtlqFt1ZT13fXCJfCQ8jluT8cTEKQyHezPM5GC88zhObxMPCkhYnTjdPJLR5ErHNGXeF1Ony4OHC5Y2e-aEbUxrQrV8SMSNMS-0Ktkrl2lxfQCQ_vTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23448" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23447">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcELFcoRh49nZSUSLgjWXQlQonRplflk6zN56jUJDn44qRQ0eOmRHGGhKx1MqDHiPPX7EBixcSHpLeaea6CMf6_Sf1aaL3Ae4ykdmjAY8_wE0AgJ7cz9ss8VByJEUvHJWzcar5y1lyMJEt_woSKtfnYESNFjAajkwJucSIC0_XaI_dX418rr_MTZpx9q4ZXGs8NcsG7N6gbfIgkYwc_6cqf6KAJvOMGfVgTIbE3A9LNcCIEeAFKHlF8mzaeZ7S2YxxS9HQ7vwYNG4HQA7fXwZJQRF0pn08PXq_jeE_KBirv7XsGGX2WsRCpQfr_1qnuODG0CWcs4IP5V6htbKHs9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23447" target="_blank">📅 18:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23446">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔵
👤
هایلایتی‌کامل‌از عملکرد درخشان محمد جواد حسین نژاد درفصل‌گذشته‌رقابت‌های‌لیگ برتر روسیه؛ قطعا‌بازگشت محمدجواد حسین نژاد به لیگ‌برتر یکی از بزرگ‌‌ترین بمب‌های تاریخ فوتبال ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23446" target="_blank">📅 18:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi6fiw-NMUSzJ697FiGtKgmC3rgluRaxtzKnJ4ek_NNcsRCn4rZb3EI_3WjetPo0hnvXQhYTfbX-Y_0goHzJ7LOYDj7lLoMxyHUPp5AJ1Q1Q7c4o8xhwX7FEuUvuE33OTx1towBQxUHXKSnZZm4P1xmvghLSrDsvLe2QHmspnL0jMsxuiXwz9dIiwsZ1zbOaBbZHLbcHRFwsfUj3TXr0RJkwezMCe3bP_es1JVoQjU2Vx03iZ62wZZLI6n5zZ22PO287Ko8a57NnxGmYLTmi8HyhV0WUMHcyJGMdURtKMyU95ygxIOMQURekonWNoNMhdY_wro1yH4mClNz_WNMEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ ایران میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23445" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdZZoChf1Ca-He2BFs2z73MhOfFaM-50CzFgBJHR9QLiSlCF_44Aj5rnxNj-awLj6eqkQSmtn7INEOdH_l85ea61Ea9qA2NJWGWdLBxmiYGrfXrh8kllMiz27gfTvNmrvg0p0TxdsolInyf8t5YW6AHllncrMzZFMarXe_8-T_zJD1I-oM1J94Q7ceN4qWBzu3BqT6aMXaZpEojG-d8U1dcaybI_4733g1Hf9a7H85o7yqLUcvwjcKp5YniXmIoVy-9f1c1IoNYX_Siwk7vvHCuHI45D85o7jlcSCZrikV31IgS-WWIr_hkFMR8frhvmMVpel_IWW6QFVW4dykrH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت اوپتا پیش‌از دیدار ایران و نیوزیلند، شانس پیروزی‌شاگردان‌قلعه‌نویی را ۵۳.۸ درصد اعلام‌کرد. در این آنالیز احتمال برد نیوزیلند ۲۰.۴ درصد اعلام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23444" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=drx-KvI7Tbbm-Yxhl4fLjrKMw-bPm7gY1GxwcSIX4_0Toc8N6SthlphoZEsqW0gPvZpazNoMhntYwFQO8O33g_ZqNB-avbUMWo9AKAgjI6MY-Sr5YesYGUt5U61Ro4bsqXV9bdxWJo5mQ3OOtm-a528HL76lWSNpuSvfINKGQr4FgGv1-6WfGj08QADV-kYSvuSzsjXspoCHm1X4EfdvFjkCb421nEoNC56GYOgO1f1K5V77lNlRk09xEYUaxe7dtMtDbfRfDi7o5dWwVY-do0zVqnscxtT5Lu03OXXxeuuQMAVbilfrVnAuCb5MKuwKQJY28-SdmSUFss0BhAQEFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=drx-KvI7Tbbm-Yxhl4fLjrKMw-bPm7gY1GxwcSIX4_0Toc8N6SthlphoZEsqW0gPvZpazNoMhntYwFQO8O33g_ZqNB-avbUMWo9AKAgjI6MY-Sr5YesYGUt5U61Ro4bsqXV9bdxWJo5mQ3OOtm-a528HL76lWSNpuSvfINKGQr4FgGv1-6WfGj08QADV-kYSvuSzsjXspoCHm1X4EfdvFjkCb421nEoNC56GYOgO1f1K5V77lNlRk09xEYUaxe7dtMtDbfRfDi7o5dWwVY-do0zVqnscxtT5Lu03OXXxeuuQMAVbilfrVnAuCb5MKuwKQJY28-SdmSUFss0BhAQEFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برخی از حواشی مثبت هیجده و جنجالی رقابت های جام جهانی 2026 آمریکا از زبان ابوطالب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23443" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzRgOx3yTfZ7pKJrUodTfwdK-1X-8tC54o8XvR9G3psfkRKz1VET4SgbiqqN75rLpijA74_GFwQX1LJv2cKBfb23FRKnGhCnl1_vCnO_cjLgO61fBIarfQKrmV6Pq9bCPfQN5Hkva70KAAqF6WSrpBlsnYTITCMC2tLYn_KhNALg80VDjYwVck150K5CDjN0C9sIypE3Z-dxb1IhKeAqon6-DKFPHO0KGUferL2ZRC8LkyEt0NQ0oq73qCXAf96VUubEiWCa9x-AtMwsOxIJ_vP2uXEsTZVGXCxwVlYrX2lT_MXnPfeHu9ohFs0rIolxMeUI7J8OkLGXJ_ULImdrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
صندوق‌سرمایه‌گذاری قطر اعلام‌کرده که بوعلام خوخی پس‌از گلزنی‌مقابل سوئیس در جام جهانی 3 میلیون‌دلار و جدیدترین‌رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23442" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SduDmkcg0ETonGIE3gJ6n_r3v7rVizqekA2eksh_FpZI2VHO7pT5tkfN_OVx_uJuAFV4XAuHgPQ58JNiv5eaounzAh79D-o7Q16NCWI2DyWoIjTkJEvhy9x7yeGAQyjniWJFsvPBxAb3UYfXkpwoT18FyzMDDxe6Q2Xmg0PCeQwnO50CLcmnx6Yo17SfKQiyShioiIRDwqcncsrsbMpthjoi-jMLqyA-nkUuneDL06tDeeK4JD8H1o_kRsulL8uDYysPT-vUsxKxp-b4lgnML8TH06XGf62cBvPuzFIgwOdFrYe856PZ35FK27wuh3HOJ1jfAZzU8xlMtC0gYQyqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی قطر
🆚
سوئیس در هفته نخست رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23441" target="_blank">📅 16:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG5Zt57rO3Dp0cezsb6xn-Tabg2H-y0gZxQQOMfIRCKOw9HJeAYKQHrlN62ORD-A1--DEQfXsoSXRtZyv8EVU8Pt9AzfeqY1-T_3vbYrI0c7GNsVE2_ykk-TIHULKUKtXlxHHp3YzJjGE275rafs971kHJ952qyOdcgzq7LBkyNRxTWrNhTUgvR91FmbuaCUa5zxmi77oVjTvAD7wGZH9tkrvV8C5NxzDMJkEvdAs5zZZgXbjGnk71fUownpATsHD2OgPBVa8HPOI18jED8bwRs_tnXDMXJlmyg-lP1AyeC9uoO0UR8dLwX4oHjrCKJq4tOB19X95LwU1ycOGG1N_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شبکه‌های‌رایگان‌که‌مسابقات لیگ ملت‌های والیبال رو باکیفیت‌بسیار بالا پخش میکنند. امروز حدود یک ساعت دیگ تیم ایران مقابل بلژیک بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23440" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7jbQC3gr5qMIpjrLigEcgj2wI7XWNMKVDV3oOeS5Kx071aNaobWBIBUc4_9tUrOk3FSwkA6S-G4j2BM07teUIrFQEtYh2acgnYiTO5G9OLOfBtiLF1Do5icFII0kqGK2OdOKo3yawyNLrtqH6PE5PYTEb7PkcIx-hIayYRafVS1S85gLG3SSqKSn44a_Vvl36lQpNj9DjGmcDpCymQZdE2ggxa1jyoVSiH3dQHNVrwhkzuBJwL-fVQQYD_FUxVloLCAitRkevfZV24VAPaAKgyIF3q0qFjMcmHsDEWCpSEQRRdGvR4g4BOo0aKHDLK9h_I0trY-M7KRVBT3kW9ukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23439" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZELBJBh_sES5pLDlAnYIEoZmIuhyqDMPAD6RQLLUWq5cys_AE8FfwucbYDzYXq9PzfqFjGTcW-0jGSA0WrGFH68ceCExJPRbH7szI4gJmA4NOMN1n_NNnYAJmgrzSVCOqXoY1I3NFUcsTClSM_ZiDwgf4501Y_vEtmktD9208PXIu05uRLLGkvZKmdKsAde2OA61EKyUvimYaPCvdg8adksw9Zq1GDYWbRcjgRLNaoTU84AOpl0gN_vWLAN5EEX7qY7FgOwMl0mBWaAj4FSoXz2epir6bPXPRnlcx4jwlGbKG1NITPxhMHWIBg5VWGIxB6jF0QrHp7rq5QHuPz4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23438" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">▶️
قسمت‌‌‌سوم‌ویژه‌برنامه‌‌فان‌ جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید. شیت و محمد نصرتی مهمونای این قسمت بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23437" target="_blank">📅 14:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=Rc0nnvTo9dtgqzsbzbm50FwsAuoLnvv7XpV7Fkvya4MUYUtU4PXWR8fGu20JKefM65ayR9pWyxUYjaW1_DJTC2TiLNXPu08_mz1g-6uQ3GOX0A3BpjA_MeLPkaBaaCH57CzNMp229bvWbgvxIk-9TlcPsdbY0YNCU6TNc_rgdBJK9DdgimFNr6_5E88aQFuOk_VSgFhkstKUoP4JFxdM-Ho4x5uZ-Mkn1fc0AkUJ5w2_SMLloan_KVe5-fWck9Gy9qhQ9yjSGZ3MYfGTeE8AxyfhE-Z98dPzZNIgFldZYVCUOp3xVfFztwKN8SZKcXWBaiucCi7BMta8VjThcDOQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=Rc0nnvTo9dtgqzsbzbm50FwsAuoLnvv7XpV7Fkvya4MUYUtU4PXWR8fGu20JKefM65ayR9pWyxUYjaW1_DJTC2TiLNXPu08_mz1g-6uQ3GOX0A3BpjA_MeLPkaBaaCH57CzNMp229bvWbgvxIk-9TlcPsdbY0YNCU6TNc_rgdBJK9DdgimFNr6_5E88aQFuOk_VSgFhkstKUoP4JFxdM-Ho4x5uZ-Mkn1fc0AkUJ5w2_SMLloan_KVe5-fWck9Gy9qhQ9yjSGZ3MYfGTeE8AxyfhE-Z98dPzZNIgFldZYVCUOp3xVfFztwKN8SZKcXWBaiucCi7BMta8VjThcDOQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وکیل تتلو گفته‌تتلو واسه‌ماه‌محرم درخواست مرخصی کرده که بیاد داخل هیئت‌ها نوحه بخونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23436" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=vruYEvu4tDysh_iZPeX8-6Jd7jTZKJW6GFne-N-9gvbzRdx9MkSrLbxObLyX2dCgDAJ23ey8r9wiPvqs9dWtnEYMBsCHhSndS93XOuqv35RCOourB59bF5LNlf9H1ugPM9WfJtnR1wPtz27oVpFYn6QQH9m4jet03YDsR9EVScZWktGnDQHfsT7QoTbLoo2logWXb37GALw1RkK5EDccE_yATC8hYjwLUuXaM6PfGyapIJCUYP7HnqzlRJw32JbaSGhXTJ7JVaPEarF9B21HlwfVpzLhXH21iSV90zwdsi73iW3-omVBTEWWnpJfq-nDL6V9ZOS4QE3FI3nW6wmhkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=vruYEvu4tDysh_iZPeX8-6Jd7jTZKJW6GFne-N-9gvbzRdx9MkSrLbxObLyX2dCgDAJ23ey8r9wiPvqs9dWtnEYMBsCHhSndS93XOuqv35RCOourB59bF5LNlf9H1ugPM9WfJtnR1wPtz27oVpFYn6QQH9m4jet03YDsR9EVScZWktGnDQHfsT7QoTbLoo2logWXb37GALw1RkK5EDccE_yATC8hYjwLUuXaM6PfGyapIJCUYP7HnqzlRJw32JbaSGhXTJ7JVaPEarF9B21HlwfVpzLhXH21iSV90zwdsi73iW3-omVBTEWWnpJfq-nDL6V9ZOS4QE3FI3nW6wmhkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23435" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s50BuxGp4rfeC3Fn8LDPMguN2ORdM0jnFWXxmbDhHuOIOMq86_Oek7Xlbr_zv5QBOseiW8DxNj24Onn9Q6o3qfHA7RbM7bXoXTWg-fMAw7DV-wAKzPSZHac3EcgQXaqoG-oF9u6QLL-CStKsiwFDSvh8KMMKZw6qscFhuMbDCt0EzsEPquISBMQof2nB0HlXInjkvl7GElJ4hmqLRMGNz-JGD3ZKwl6p6nX0XdSRgSm_HOWUjpgYRXcEmS2UpkRjL8UIiAusHh6RRltggndBU2KxvsAIOdJO8yGfMwIl_rxalYJ3JpBXmreJ9YCL7CHkBxI-BpYUGK8ZH9NlZaMElg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
با اعلام فابریزیو رومانو؛ سران باشگاه آث میلان مذاکرات‌رسمی‌خود را با روبن‌آموریم سرمربی پرتغالی سابق منچستریونایتد آغاز کرده تا درصورت توافق نهایی بااین‌سرمربی جوان قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23434" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=V5jrBShSYe0JNJLAxmx4P9sn_GV2J-FrHwaqbBKQayi6t9OfP61m5lnuEfFXnik0xIHRMttV0DfYOuf-jqPkI6Jfhd5e3xShwXJCteeT940Dhm8EOw6hnRpOxuOfriiaRzFaQtlGSc49wD_x2UnGSL8SZr9MMxEgbGYWGAAkP8erzxRVPm5nPJrW3yF_HwDr9ByIuga7Sles1i5bPuqey1FFL1Mx1TXVWZoxgxgJl6ghEpRvpbpZE3AQTbfA-72aQwEetf-01AOXeta-Wsn0nnC3vgpFdz7p_KLIdalE2XtQ2shAqYq5WfxlEhPRMTWXcEU-ZxLr72Z_wzCv7nEF0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=V5jrBShSYe0JNJLAxmx4P9sn_GV2J-FrHwaqbBKQayi6t9OfP61m5lnuEfFXnik0xIHRMttV0DfYOuf-jqPkI6Jfhd5e3xShwXJCteeT940Dhm8EOw6hnRpOxuOfriiaRzFaQtlGSc49wD_x2UnGSL8SZr9MMxEgbGYWGAAkP8erzxRVPm5nPJrW3yF_HwDr9ByIuga7Sles1i5bPuqey1FFL1Mx1TXVWZoxgxgJl6ghEpRvpbpZE3AQTbfA-72aQwEetf-01AOXeta-Wsn0nnC3vgpFdz7p_KLIdalE2XtQ2shAqYq5WfxlEhPRMTWXcEU-ZxLr72Z_wzCv7nEF0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23433" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=uT5O-975BTC_yEi6vkEozPo5aGJHTBdQuWwSFPEUlNTgVg8AKiqOB543UKpoFx2MEnI9E5MEYCuD5P4gxigZ9YDyH_DCVl40Z-T8FRBlzyvejlpGqnjZmSpR1tkIc67Z_w_rrmbSMuQTIYjK3a0rISo9f1zHMsDIyTbZ3Cx-BFE3n7xTcCwDsN9nUS7h7HjDM6ourJzMORGZuy3foJ3iHpado_CFG-NU4eVqL8FpWa-PSm7084XuL_vWtvAsFhHZRj0odbCrDTlLeBhgYAtEWymhwH65G9cc_YnOa12NoQlD4vT7n2y7WaXfbAcfwyrTrAFS4kar6E5ajwVgWpswtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=uT5O-975BTC_yEi6vkEozPo5aGJHTBdQuWwSFPEUlNTgVg8AKiqOB543UKpoFx2MEnI9E5MEYCuD5P4gxigZ9YDyH_DCVl40Z-T8FRBlzyvejlpGqnjZmSpR1tkIc67Z_w_rrmbSMuQTIYjK3a0rISo9f1zHMsDIyTbZ3Cx-BFE3n7xTcCwDsN9nUS7h7HjDM6ourJzMORGZuy3foJ3iHpado_CFG-NU4eVqL8FpWa-PSm7084XuL_vWtvAsFhHZRj0odbCrDTlLeBhgYAtEWymhwH65G9cc_YnOa12NoQlD4vT7n2y7WaXfbAcfwyrTrAFS4kar6E5ajwVgWpswtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شهردار شهر سیاتل اعلام کرد که ورود پرچم‌های شیر و خورشید ایران برای بازی تیم ملی برابر مصر مجاز است و از ممنوعیت‌فیفا پیروی نخواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23432" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-KOmlorYf8NEoBUgJmEnD_fhH8540VPAshjq2PyT92yuxQ4_HoMMY9pRqxRCLNZuhLRIXCBWNeMaFOCa13b2Me-Is5KMaKDppm5FswMyshpqhJxPoayEDwPhx_ySRLaiZhtWTsyvaxT6_Ai59tNwONS0AJQRgQyzaHB_BzQj_kPW6PSOyoWikohgsEwPFyG_bHs2JpWmuO-Z6CJlCrlaZtvHF9GCzm0Dq-CgstTKOMkOMXr8D2987mvEo_Pyh1hiVH-jfvIe2DcNk1iANcbQ6Sw_gDHUKSApw6_axFRfpBHYTGlBNhqATSjiI-Ia5k-eMLJ1cvt-SfA4JvKZnfZEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
حرکت‌ جالب‌ و زیبای فیفا برای جام جهانی؛
تیم‌هاییکه‌سابقه قهرمانی در جام جهانی دارن، لوگوی طلایی روی لباسشون‌دارن و تیم‌هایی‌که هنوز قهرمان نشدن با لوگوی ساده وارد زمین مسابقه میشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23431" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9uoVUQY-qRtEfMHCOMJ4AwcHTdRqIs0-VYjq9GKxxg94mGrR1lKUnnTNLvuSQRZmjejEb0eqWbCDYWn19TTL-mIveQsBn4zh99TlXCz05iUpHXkeaAbJikMuTCxTwVnDr_wARivgYQcqBeawWpCNL4V8HPv28WjVJMl7ry7WUHZgvL3QOIEplYT8Se7a0j9SDGRJAgjS41409-zdqUDa1Rz-o3jGsSWAzOtbDG2rX9PrXJGp2yx3Sx9m-7MAsKjUQWwEhXAQvd8HZO4QJgOjzXSYf5eYtTwFdUcVvsaMCsgK2IVHvniG-yozxBYDti2jsuODzvHZunzM3ZExROFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23430" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=LV3pTDTnbC6TDebOl2MKvKEmXzaNbhkCshSrgK8eTFtGbejmNyerQRt5qVHMWwpGR9EaCIUlxKza79Vebx3sD_kgo2wYpo3TqxgRAAMwu5SmjtVxYfoU81UQOCDZfYDDX6KKKP6M6QVUGfMIAxr00XTmxKIXWazSKn2CV5KMdm_Dnn4w0T68YQHv2sRcc1H-a2ahUdRQoxbPfNNjZudULcSR6MtxkNTFpVLHGCwjYOC3wbr-md40Eh_J-jF1X6jzm-v7KzPfJhLEHIXr2LT2zpaAio_eQebRv6_zPyrqugCYDNQ_p8Jc-tvzwKvQ03Ea4Pi_MwcYXwFi1iAV7nUL-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=LV3pTDTnbC6TDebOl2MKvKEmXzaNbhkCshSrgK8eTFtGbejmNyerQRt5qVHMWwpGR9EaCIUlxKza79Vebx3sD_kgo2wYpo3TqxgRAAMwu5SmjtVxYfoU81UQOCDZfYDDX6KKKP6M6QVUGfMIAxr00XTmxKIXWazSKn2CV5KMdm_Dnn4w0T68YQHv2sRcc1H-a2ahUdRQoxbPfNNjZudULcSR6MtxkNTFpVLHGCwjYOC3wbr-md40Eh_J-jF1X6jzm-v7KzPfJhLEHIXr2LT2zpaAio_eQebRv6_zPyrqugCYDNQ_p8Jc-tvzwKvQ03Ea4Pi_MwcYXwFi1iAV7nUL-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های‌ابوطالب‌و‌قیاسی؛یک رولکس که قلعه نوعی بهش وصل‌شده؛ عروس‌دامادها میتونن با پول این شجاع خلیل زاده رو یک فصل داشته باشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23429" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNks1oqHRsakdlsupcAorXBOAd5sLfy95uQGfv0UZN2dyygmJwG1M5q2rSm_Di6TbKViQ_qQX94N2oNBMihTHICEkbOwGfyP9Pm-OwH8V8A3vBKRB9rx6mTokAzf6d4TKyKoGCE7GmiP81yvlFqCNXbsGsjYsd9IASXyRpSoyy4bKMip0p0iDcM-TMx8ZQ4rq8QaaVsJEwL20rQ0pp3Gdt2rQWF_j7HbGFoDKHocwl9IVxVmz7aNXoPsbbGXUCDm3K6sBt9XWa6kXLKJFXhL65Z1pmd8u6pde2eaJUo2KMHWuM5QNl3d9m-IemEzGkW7foWMi748R-qTGUqLJmac6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23428" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkOE2weGcna29Za4v5KbO-zLL4Abw63dLAwvfwRN7c2G2AxEALKZMIE06MGrgsTRrE102OMYVJRLod690tfuLLsDil3D6nNFH3jmcSygVvSWOb0HiN24LsKMk1g4BlCOtVMCDHDpC9sl89bZK9cu5PAMlGGaXrSn_HWUsfKNl5JbkdBWBT36bGIjRQzY5gAGr5qxVpG7rs5zQ6Toif4dz8vDD43QFJv45ecby8M6gqjwRRUWVyV4mU-JksKKVCB6yB7CylFhOhX3rd8xpNfQ6yjGL_Wt-Jnd1rb48Wv1I3PIALyxghZ3w6_LiX13ituPKj_Wl65lzwANs5MIoRLUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇺
سرمربی‌تیم‌ملی‌استرالیا در حالی تو ترکیب تیمش مقابل‌ترکیه ۶ بازیکن با ۲۳ سال سن یا کمتر به زمین فرستاده‌که‌سرمربی‌ایران در لیست ۲۶ نفره‌اش فقط به ۲ بازیکن از این رنج سنی اعتماد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23427" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIrhyCEcum3_w0jzoBS2pICOThXoJ_2DESTUpvcIeZLyjx39zR-Av8VXBqcgtpXBejJPb9GQ_Hs0WCGo9YpcS1b79M89_PduClAaAs4odN26Mb1FGCGvJQdM2yw30zFNavYIEMglyumMhejOS7un4469tzEbrQfhjagCm4pXh9-mb3xFBq_SaBTqhdx0lb0ziG_H0jL027QTuC8GRZ7927aJANwCMD__aBWJvMQ-sNyp3oFvNM1c8F7SQBEoFEpBbbrfykaAGYHD1mz5lzkitxZHmsvkExSoRxfKN5dlc9LJvcS7ZEMLHHiYxhWn5Tkc8CjGvyhaNIz9NJD4qQPUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23426" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgJ_H10h6rjvjQryeASue7idIdieaWIRcEz7GgaF9BN35xgW0nIRwQd3zHAQNBeT2kGmgF5XqyJ3QXndckKdc-yEqQ1AYXyJi_wIKIdfsrMyQgDFl1GW4UsnpNR85_Zsfgpi1r1ZyXFeM0QprvIaYTgAjyLsXjKiAcWWEK0df_tjsmc1yajJibWzuKqjZUopeoV8HwUOlY7yqM7xgxbNMa6RZIGwzWBcwSUTSxmQxYjb1FCvaYRxLIaqQAcR8QrbrcOxZ8jMJSa-fcGEWu8vHMonduu9DiOybqTeqde_Ckz7CoVc6AoQzAA7AVpqOukVRCIxFJDq4PF5_fIBZdpUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
⚫️
#تکمیلی؛ روبرتو مانچینی طلب 15 میلیون یورویی‌اش از السد قطر روبخشید و رسما قراردادش رو با این باشگاه فسخ کرد تا ایتالیا رو در یورو آینده به جایگاه‌اصلی‌اش برسونه. مانچینی در یورو 2020 ایتالیا به قهرمانی تاریخی این رقابت ها رسونده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23425" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMIHiW5T1xRZCr1b8Pk316A7FlPuyy_Ex9KpNKtZ3_5YKHg5JZSs3295kM6SJStpgTjuNICLs0rHnHPPC48nmU39Sbae6KXU0Bmc-sr0ZTnYyD8T7QcbZohxGM--z3NHXTS18IHvFPzCwp2Au6dRm5n0eqc58I5oO39hrauygXNxMiJWj7bVmJVn7j_en-j9SuGWpNVNhYqQqvxGlFYBIVr958RJcPHrCr8ujwN5aiGzYFrDVXy3agEbAUANHiLQNsJd781xhtrwBsUEvMX0eSo5HbaR0ewW4k0MhPI8FAm05M1tUchvtjjioackhZyCD2lWTHNmGZr773LldXrNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23424" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MaFHNuK0XF7P9FsI7KY7xwh1Z16F061gzPmPMuhqVQx0DVNEzYo7CaneQPpSBxxUN4OrD7Q2lpFFVrzR5F5kG4rVZayGTTPvBPl7A7ZhO_XTm5uw4_YRU0Wbnlr7y65VjaP_LYIyOUG_KKYmsZDlNnvOzseIFVo64LBkqx_86_kYHt1I98YbostzOG0XKOlx7-gYYkQpumecoSMkAXxmgaopQQigh6-mccgELbNxhU343I7F9fAUG610o2eH-fvjvqDU2qb0HwNPLs2Z70fz39XvLMemvV3ymWxsP7rlUX6azmkQyXLxlTB6w0rbdJ9lNFtw5FgGHGeKAxx0MR_jMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MelBet | جایی برای پیش‌بینی‌های هوشمندانه
درجام‌جهانی 2026 هوشمندانه قدم بردارید و روی پلتفرمی با اعتبار جهانی پیش‌بینی کنید!
🔥
امکان شارژ کارت به کارت و هات ووچر
اسپانسر رسمی جام جهانی
پشتیبانی از زبان فارسی و کامل‌ترین برنامه موبایل
قرعه‌کشی و آفرهای ویژه جام جهانی
✅
حرفه‌ای،مطمئن و درکلاس جهانی پیشبینی کنید!
📌
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌ Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23423" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEe8TEnazLwx9rIKSMslSjan9ijqkaiF_ICUKh3aV0TI1OvFe-BALjBJjs5YahgRcYWQxU3hPG3IN5gih_Cu4afr2DvureQtyVfQsb17ImTwJ5u40slP1Ij5jh9Kd1rTtqNm9_uK4bF8N8snTgtNLeRV_OPQ3Q61Tg_IzGJyZXUwR6t4YzBJYotgQsKQqpx8d7gWzQ_RRIojRPiYLKsc37nXC44HGgyLARXuKyql0SMILChcUfrUw1aqwmP_LfxLtFbPY1aZtkIteBI58sBxk0nxb2N_FDdYuGUaUwf5q2TXvH-QrbvJKs3LuHGRb5IlNO3RE6LTkwhHgkNQ9TgKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23422" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVOAPm0PcXdeNND1UhAYRKLx8_6fBBAAMT9HwhpihvLaTZW2ulbg8cTMTZF0sY1ZRWXl9HDuRLMSu-bxP1fy_erMZQp7Bg-F2vGJytyIGSS0s71a9LV9rNW4iYgSl2kY-V4ne8G9hHWeHruPbLCyMo8KlMXCOqLodcUWDks21XUHdrptXtFFBqmHFgWmfl_4z2tkYlevQWOvIg1ZEoOG1epLbguWHDln7DpSAhlqHtQUpRSVilVpJ2tzzIZph60rts1_nXBJfQEN8idpyl5kX2hgpt_1zl0gCL6xhoEyaAV0ri37QZNAyfdrV7686duFf_8MBGFvjDE2OXNWTJMKEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C و D رقابت های جام جهانی در پایان هفته نخست؛ استرالیا قاطع و دو هیچ ترکیه رو شکست داد. اسکاتلند هائیتی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23421" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhzxzLzUStdhuIU2zopZIUoul-Emw18vZIZ-3tuoBKyMxXlZrPI-vBdwE6YrqkvWHjRcNfU9k9f7GQtHbYxIoz6wGVJdCctSNuvWNRPy7iu5gxFH8_e5pOvSHdCbB_zpwWtSciwAAH8EJxidnGapyvs7wjA9TRHrBsJ4-hvLyAuY6Y8WbQVtg7GBkKTA9FFaMsmKIP1quCTHPfj76RDspOVGxl6SDPFF3MS6p1h0iMMItHFeCrdLxL7rh-Lf0hulFKV-hDpKfAJQDJN9aMNW5BT2BWTmgBTRVYPz38C1LSbHYB5v8gcF5fsYVC6S88OvJdoNNvReOKV2rtXBtYMYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXOGNos2UGJ5_6KQ3hh-kwCae03yQevOkyHmz2ZJ0qCECjNSNBhtDoLk7h4ebzEimTBM3okheUfSy_-afecvoruTp-l8ajYVXxh7LC0z1VTSqxpiZECsOb3cn8ZctT6t807PYCT0Dte_HegwsGxxdAzay-8PwS7NxgUP1tDZjw_edMxTEk4gNCvo458ADU5lWXT8gqB1qtUy8hprlN7u-Id2Kfea3hV_f8Mt1K7NU4WG_HooHIHaD1Q9CLxm5Xq3X2-Xzebpiy-5GhD93H0m6bYcSZx8DDIuQBFvNafaCG63P9aSLhdMD9cHgYdl_aClA8Cgs66S_izmKssD1TAmOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی کاپیتان مراکش: اعتراف میکنم که در نیمه‌اول روی اون‌صحنه باید اخراج میشدم که شانس بامن‌یاربود و داور ندید. لیاقت‌پیروزی در این بازی رو داشتیم. هیچ موقعیتی به حریف ندادیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23419" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTbtfOorqdYX3CAc6ROhRpVzEFHN8t3ytU35ilMpgw2MDBqJHLOJClVw4yMFabSqKcH5VvZm6dZI_G1z-LJQtza_2_8DGBUNWChhKj9LHXJrOK71UPE8YYQeum8SzF6kabL3pWGqxDx7aGtguYhc5mrlr7v_7OPLHP-Y9CufSZ30OWBoxdsHOQYH_l2yt_eux9mSSrdwPVL_eATifS268Qs4Yx_TF9LieomBTrwK-HEuTbIl3mgHTvIjyd9pBwS5CUq8VWVPRKpo8R9T4xlDhfVjWZW7sTL3wNBZyyLqnVU3ehmLcUHgqbMNGkpmOx2g2Kxx5bctO7_HqASGUoAHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=j2U-lsSUNhU_0g3Jjn1ihwftmE2Yy9LeNypxk4Eq9wcfUbHuboYCh03dscG2gJvK9MMz0I-u3Gr_1SC3fKJre1qsZLrsNTIvS51c4zplWSyRzNHot9_9cvaC9jFy-ZkSE9YuvledVrCnwWq0U-11Kn7DyaEA7MeEarehV8Uyp2UFVG1979OvZC9jHJnN1ytbwOPg6Alfd5WszuM-9ocBWlivNzXeQswjM7nE5AbuNrr25pIUlcvjghM9f14Z1qiVE6Txg1JkMBo6fodZ9JYfxTjZUOZPEi5dukDdoXaV0UEa4aziUMFt9fBg-J1U7bStd9PHQVw9TclMD8me63GTSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=j2U-lsSUNhU_0g3Jjn1ihwftmE2Yy9LeNypxk4Eq9wcfUbHuboYCh03dscG2gJvK9MMz0I-u3Gr_1SC3fKJre1qsZLrsNTIvS51c4zplWSyRzNHot9_9cvaC9jFy-ZkSE9YuvledVrCnwWq0U-11Kn7DyaEA7MeEarehV8Uyp2UFVG1979OvZC9jHJnN1ytbwOPg6Alfd5WszuM-9ocBWlivNzXeQswjM7nE5AbuNrr25pIUlcvjghM9f14Z1qiVE6Txg1JkMBo6fodZ9JYfxTjZUOZPEi5dukDdoXaV0UEa4aziUMFt9fBg-J1U7bStd9PHQVw9TclMD8me63GTSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برونا بیانکاردی پارتنر فعلی نیمار جونیور و کارولین لیما اکس میلیتائو در ورزشگاه بازی دیشب برزیل
🆚
مراکش درهفته‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23417" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6gBD_TJLokByOxvvN-6qV4CNGcp-zGkK-dRIA8bjAgU689czR-wsupzUXqKHJonCJQ_rrd1kyHR_x4VtCW5caE4OBDtu9j3ISFm_MG46ZzgtE9miQkUWLIwNQvCBVm04WXgly59Mg0KQL-9VrueYvvLC48Z8eColJJ3fe-KalaOB3MbZnjDW6_R-aXVRz0pDoZQxejShQQtqeunGH8Epa1d1_EH2XM6QAaqbaIMTPaj95iIE5a6L-tzylRgCFeE-SAJj_XvdnbdRTT_SDjU5kRU-TCS8W2J--KhGJHlocKNeIxrhstJ3Nd7tgKKJxZpleQLQKAG8oK1q-KB5NTuCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ازکهکشان‌اومد زمین بی‌بال پرواز؛ مثل شهاب از اسمون اومد با یه راز؛ خرید اونو قصه‌مون شد آغاز، امیر10؛ ابر قهرمان جدید ایران و جهان
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23416" target="_blank">📅 09:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=YBZ9i73BMxI-ctCf0OvWin9xboXPLHAqgqoS_fqJyeToEQFaHbB_xhKWypQPnr7-Y71lEQDVrklUxdVWitFbGTGmddhu3meRBvi5Pz2On3WnmdSXpzLx6aGfaDVC8qPGwG0tmtWKZxE_ISyUVGJS29NYRXohjV-pENLFpPWHt26XP1pmjkmj_byXcMTnI7NqZUeylhmY1TluRQBe6rS72j4YphJEAhJZsTgBgqSTK6D3X_oTrlG11RHKxJleULXlc6R0kBRqLpw6vu02D-e-fQNyqf3Rx3QjEjG7AKnVPPE7MRb6DRFZFTNLwLH_mzh3Ir1LwjUDq6uJGuL9XdWhmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=YBZ9i73BMxI-ctCf0OvWin9xboXPLHAqgqoS_fqJyeToEQFaHbB_xhKWypQPnr7-Y71lEQDVrklUxdVWitFbGTGmddhu3meRBvi5Pz2On3WnmdSXpzLx6aGfaDVC8qPGwG0tmtWKZxE_ISyUVGJS29NYRXohjV-pENLFpPWHt26XP1pmjkmj_byXcMTnI7NqZUeylhmY1TluRQBe6rS72j4YphJEAhJZsTgBgqSTK6D3X_oTrlG11RHKxJleULXlc6R0kBRqLpw6vu02D-e-fQNyqf3Rx3QjEjG7AKnVPPE7MRb6DRFZFTNLwLH_mzh3Ir1LwjUDq6uJGuL9XdWhmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نگاه عجیب ویکتوریا همسر دیوید بکهام به تام کروز و حرکت عجیب‌ ترشون؛ درسته ما فرهنگمون خیلی متفاوته ولی‌همچین‌چیزایی دیگه مورد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23415" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMojGuM05UrcbHq5nZtvrMxkV4RsdmxO-hrZ524rmz8QXiN2pPuao4KygcQC233q5UMvMi86RBaxhe4NRYxiper9YkeYUDgicHSQShBqU1-MUrmhr9z3jzMNfn9-_1sP0pfbIL5RIwsCokj8JVvMwTjrSjfgKg_0CdlvYLZZ3Jf_3pAEeU5KgV00lky-ycNiN0qtZbXq7dvN7rUrNIDYtWANKOpyvnVBhZL2gWzG6XucrcZgfi4oo3LQIODxFd7kdM7fzNkN__KcK8mAph_okNTwcr-K9Kpwz-G_tfD0EXqLVw-dnAjY8SI_hG9R3fdUcBMyNwYnA2htrfTXBKqa0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
درحاشیه‌تمرینات‌دیروز؛ بازیکن‌کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه‌نفر از کادرفنی این‌تیم اومد گوشیشو ازش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23414" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da531b194d.mp4?token=HrTnBnZS4byVaPhPRHwEaBxZAQKjesZ-Yq6G0qzt7IDVfQu3AMGnyz0iykVLSti5ajIPPcVNC_h7a4VMfawmxLczj-wdTIHZSOPUdg_ODxTLf0UtfnYjIx0lMbFI6nQTzxBCSzdNbNZEluba4zcZETC6F9C6gg-J8Ik1GNjMTeyLff6tu4afPlSjLf03W-Fb0yDNu4IH6cNX8NX0x2O2us8NBtiGvDTHVRh02BYqc07dIe1JfT-LWwNIWk2KBZBJVhwY7L2JbGVlQMssnCm910wBmS95wWXpiHFVmaF0T9Rry2yWztRjkd2NQesg5cNFw5moQjcycDC5lAFDi4Xqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da531b194d.mp4?token=HrTnBnZS4byVaPhPRHwEaBxZAQKjesZ-Yq6G0qzt7IDVfQu3AMGnyz0iykVLSti5ajIPPcVNC_h7a4VMfawmxLczj-wdTIHZSOPUdg_ODxTLf0UtfnYjIx0lMbFI6nQTzxBCSzdNbNZEluba4zcZETC6F9C6gg-J8Ik1GNjMTeyLff6tu4afPlSjLf03W-Fb0yDNu4IH6cNX8NX0x2O2us8NBtiGvDTHVRh02BYqc07dIe1JfT-LWwNIWk2KBZBJVhwY7L2JbGVlQMssnCm910wBmS95wWXpiHFVmaF0T9Rry2yWztRjkd2NQesg5cNFw5moQjcycDC5lAFDi4Xqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23413" target="_blank">📅 04:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MslG_P6V5TKPkxo7r_QwV-780pdpGEb18VBoCeeTYcc1ueTthRtdTyPrF4jhqxk69f8gr8VODE1QB2wEirUFFj6GM-rPKUOZIUouuJvVgYtHwi3Grj89pVd7h3PQeK4rhPzjLF1Jms_o4swDaR0QVmXatbMSN5Z3bC1Z8U3rG8hPkZSxVf49IoAUpJhPB7IM-0ehHdcAHLJJ7OoPWOnzQlNPwWP7pJRabwD03ks1ZulziK0qAsoDhWAumbvL2EtxvTB6iEKodDSMX9KuiXQjh7fX1KSy1GC2m371r3YJ-R1he_F5MJgyVY28r97GMCKRyvmNlNt3xUv5Sn0npk5U3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23412" target="_blank">📅 03:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی برزیل - مراکش در هفته اول رقابت‌های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23411" target="_blank">📅 03:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23410" target="_blank">📅 03:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOnbZC0AxEGHvMjX4n50nx_HIxMY3ZaqymmogFTEbqlqj-qEEQPmNDccsp8SCBx9w19yDp8Ws7Fq6oV2dF6go3FvL90lnIwilmWUexhtSIT1VLU05Uf-oc2fTfv559a4XMF4310vnfTIKjU4Z5Xo8ITOfFgwCEWL-uXxVKypUr2WzoWRhMtjbFfg5FWd-vhtuoFufVThu_4RTYtRRoJ-pRXT_0YC4ZpPxsidHL5m4PeOBBZt0Dr7u6d74ry6jTTqKN3rfWCo3hKdDRd0wBa8w0FAqTNBx_uuSR-fAuY9AHp7f_moH8p32JaRJUxgjrxakE8h75sQTD1bGSFITrTjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23409" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=FIQvNzjG1CJ732dD6af25N69RVprZZJOhg3Z7ZPwnBVWeXAW1JtSlsjdd0dPWlenKqK59VNLJqPbXbASgYn7fV_hCT220fVZqB2okGNd0GgEXtoN57UcnfmSKvWpIUoP9BrcvHYPUi2Rk7mtU_ktxYBgteoYkfp8ZPHouuDPK0X7rXdtXwR2bUzMxE_YghdL5Sx-ghxyhAdZ1PgBshU9s-teUzfdc3Wp_Uyti6Bvn3sxOjge8PA4F-feu8wNfFk3Vhsp92zcjXH7DOChrmgZ3G0y4DzYeIHxmE4QDTda0mVkNF3n3hd1HWx7FchI7EPRT_oKA7JxZHivLBRDbrua1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=FIQvNzjG1CJ732dD6af25N69RVprZZJOhg3Z7ZPwnBVWeXAW1JtSlsjdd0dPWlenKqK59VNLJqPbXbASgYn7fV_hCT220fVZqB2okGNd0GgEXtoN57UcnfmSKvWpIUoP9BrcvHYPUi2Rk7mtU_ktxYBgteoYkfp8ZPHouuDPK0X7rXdtXwR2bUzMxE_YghdL5Sx-ghxyhAdZ1PgBshU9s-teUzfdc3Wp_Uyti6Bvn3sxOjge8PA4F-feu8wNfFk3Vhsp92zcjXH7DOChrmgZ3G0y4DzYeIHxmE4QDTda0mVkNF3n3hd1HWx7FchI7EPRT_oKA7JxZHivLBRDbrua1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs8-5-AyYc27O8Rx0XgS_AldmUeAQ_M_kqxxQFzinoNzMWd0TOFL4XQuPxvkCkaqSs_9cpch7JpJnF2Xod1uE7ZMqk_Yw1fDQ5L4KuF04jcb6_LPYG-1xXF8gp7mYPOhKwDUmM3WZ-SNngcxK3qpC92842iTLHYUTJJxkgdO_HtC_bX-ZiMwwZHofFgjKIa3MGne6nBgJ1rUB4DzD2KzEF7njCAw-kS3RERSITNOi1bRoQi-sxnCgEekbofJNXf2mCYhj9J95n4_9t8kVTaaxvQqQ3k4MXgB4yvmfGkS0q6iwxQgQkqS73hM99ZDPoK4-GfUeEMxnbQU_m5maJgGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw_Dqm49D2imCAOSB9_Fb0UgbPU0tw2moE2b7rIn7ed8rffK9GEIDEsmf8PFSh6zN9OEfhdolyXr7DUL1VWuspBsV2zesp5__XwScK19zZmrXTBCrdjaduGc-CrQ2ClkoQ2sWAX_DEkREfHrTa_HYYHUHLuvevILmb37svco5ltEAoDTN6bB7b6i_JIhlXWlLffVZsSlmeNUn-o5JHzO-bvdYTUUZMjXArdMjuIvTow_6YsVI8DIXLfLlLRilrK58Th3sI1q3I5Ts-6BolDBVCd_GzpZv_NRdSlnRv1aDdtO4bO1JuasQM1J39DKiNfR0ZG43MTdkDl3QDqAbwJgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az4n5yFPNQxJ-J0l5hrvojjd9xQ4qxeIIF_Q89haACNYs4MkCGIzk4vwKDM627YNFcisg0a1wFVGFmtRAi0axVF5nQZSg5L9tYaXN7Bv6ANRXYkQxTwLn0nwBmF9xL02SFxHQTaUC5AaJU2alBBkUGvRhqqCQzAwibJ1xf0qYlR6oQzgto17GoET5mJ5qkmv6aVJSJctTgcLVflmdZfSWxGmlCSSMV-xwtA9S-2oC2_Is-flfC6rALFLXCEvW6noM1xTToq1YLYQbKcYmKTZgNJzCZzPKAjuTsGd2OyRrpNaoLu_Mx8732Oy7663hQJ7uMo1bMoND_ry6PcmOahQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=lWPbRSql9csR99etQlCaOB2XYRKkxFH865Ri3BMW51ZcJWFDwv-2p3lKN0-cgsDjuRePyXZ1mPYiyDF3DruDzN4S37emnMJtUOni_qyHBUBu5kJxS9nYJoDXzvxSn-TEo73rwFU8MnLbD24RfDvHBScw018ljhz1YNfpE-CaO87DF7I_MUuskhGALmvr9w1OGfHfbRZt_OtLFdaDM1UDEUqP1sViFkui621Hfjek0Jc0WffwbWkRDyRAaxXmIYYnpmpxPXDo84medHMoziEmtLj1mLPx2yh13rHr5x8KRWaOkn2t8VyhokmsVvoQFgz-kNJ6vcmpB1g1AEeG-6fRHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=lWPbRSql9csR99etQlCaOB2XYRKkxFH865Ri3BMW51ZcJWFDwv-2p3lKN0-cgsDjuRePyXZ1mPYiyDF3DruDzN4S37emnMJtUOni_qyHBUBu5kJxS9nYJoDXzvxSn-TEo73rwFU8MnLbD24RfDvHBScw018ljhz1YNfpE-CaO87DF7I_MUuskhGALmvr9w1OGfHfbRZt_OtLFdaDM1UDEUqP1sViFkui621Hfjek0Jc0WffwbWkRDyRAaxXmIYYnpmpxPXDo84medHMoziEmtLj1mLPx2yh13rHr5x8KRWaOkn2t8VyhokmsVvoQFgz-kNJ6vcmpB1g1AEeG-6fRHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2qs76X5WjGCiNaFNLevF1-rrBOI6JqxfsZyH5jzwa63ehf8_0DfIPk0eO0kY-jwWXUL6GLsEzPLJVyn9thxN9sIE0lOAOSaHaW8_uIJEjL8bvl4-rV7bYH103thHUckOL-WoM37jCtISVAKeQkIQUYfb3En6AuRxPuESp1HiQydKJRAQ2hLApBYrhu87sM-m3rixeCSJl49C49S3ELv8XAamTHNBRxwhsWtJtwxH2tU-IPxAZTsuyZ5-Q2QDgdPu9a6XsZVWPiVnImKTchSgEQhgI2Zpmu4rSq_HE4qgJQPs_v8pygbem1QtE7nu1mQws5BSh99e54r99djVTzeCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=h7ptuGuM9mv45a_r06792Zj69meqOPkJBq0i8WuDrA9D29vbryMKESS0K_wc-SYwtLkQmKPpPdEgWAVLOH9aQmZllLW07O3mRtFl9fP_mejvm05U4COSBXeeH9ENd-bqjyOmN4VVYryVAXodaVSLW-QHItJpfU6v7ki3zVP4hhuSR9BsvOvHcrsGeQ_4y1j3aDtjkDjY58YSSpYFSxiuVUEIFyNAHVaOn0vqPefWqpU9G_SeQC3uCDEXhw9Yay2eaZydYp8dDY-shb97M9fTrTijQGLqmzsk3kLCHBIoX3s5RGall6toOpKvYfCzGMRXP7UtWg25OgxOABGtzP7PH3vF0-Nf4O90eENrSrtxahjV3SkNHVXL4pcaBZ-y5yyIx77sypQ8qmTOHIU-6HFSFbJziTp7wc_HaZHbifOrI9CyHaPHP_G_FE3kOFUcV2uQ_ghPuAW43qdkruljPdQ4_Isgjl_bbDxzZlJI-ZYOcn_-U28O94t6astV-kfraDoPWcLksozeDF1zfztSm6zqQkczPjtgYBTb_QAQ1BtyGf0qNkWgunmTTROUiaKblyp7gl2S4P2cO_-cK5wIAkiLfq30O_IPbSiBrCP6WqhR6sGPzR_VT-APXbiXdBP4gbupIk-vRH7in2baLtoMr_t8lAkq2bubxYalh1xqdBgX9Z0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=h7ptuGuM9mv45a_r06792Zj69meqOPkJBq0i8WuDrA9D29vbryMKESS0K_wc-SYwtLkQmKPpPdEgWAVLOH9aQmZllLW07O3mRtFl9fP_mejvm05U4COSBXeeH9ENd-bqjyOmN4VVYryVAXodaVSLW-QHItJpfU6v7ki3zVP4hhuSR9BsvOvHcrsGeQ_4y1j3aDtjkDjY58YSSpYFSxiuVUEIFyNAHVaOn0vqPefWqpU9G_SeQC3uCDEXhw9Yay2eaZydYp8dDY-shb97M9fTrTijQGLqmzsk3kLCHBIoX3s5RGall6toOpKvYfCzGMRXP7UtWg25OgxOABGtzP7PH3vF0-Nf4O90eENrSrtxahjV3SkNHVXL4pcaBZ-y5yyIx77sypQ8qmTOHIU-6HFSFbJziTp7wc_HaZHbifOrI9CyHaPHP_G_FE3kOFUcV2uQ_ghPuAW43qdkruljPdQ4_Isgjl_bbDxzZlJI-ZYOcn_-U28O94t6astV-kfraDoPWcLksozeDF1zfztSm6zqQkczPjtgYBTb_QAQ1BtyGf0qNkWgunmTTROUiaKblyp7gl2S4P2cO_-cK5wIAkiLfq30O_IPbSiBrCP6WqhR6sGPzR_VT-APXbiXdBP4gbupIk-vRH7in2baLtoMr_t8lAkq2bubxYalh1xqdBgX9Z0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=NBXsqwrPEXhIrByMlUoJ_K1bTGZbU8HcP5PS_tJv209TmESnZ_R08XUrXv7QPgWHGZyM5-z5drV8F1jbnIhT37CKPmrYJkqomxpJalyKhscWBZJLiXrXyTOiLfbVvpa-ERselh0WLxlLvA-vQr_CY9ki57yy1AiqvrcIYvtMMt1lYWHM84EWSq9I7bNfgfPhu70iLqmpvhI37sEPjFL9vwQMueYncYqFa5MMYJpkR4yXGSAPBCTjFhuCZWfpHc-HBa01K02qrljh8lQfLF3GVWLTPp9HX0-OfS-UPc4ZSOfndEekCB8PO01nMDAPUHBXvfxhqKJV0DENtUJ7ODOzp1NVgUhOsRgNlKeAcVyPQ0WnBBzYMHaH5HugZP0ajgMz8cJmtsBDRVWyUevUcNdQSZFWqwb00vhnXA1TNwtjWKnrvS3FuyfW5VDYkzKNcRqYbMXAg-8gyNfxtgnUJLFz3abctNATYEu7zsdBZ4Ufd9CsWqjOeGI1fi4hbVkzP3tiyEHsvz9sDcO-XOCNPxFCWioCvEjqEO5c2exqpQHIYyPj5iUKTBzHjcsSd8PDz6-G4z1e7jJK-l6nZ7p1Pdq690f97sbGD-RDEb3lQ7xB2HJBtiJvBaGgWvMdKETt_gfB1zUpHPifJ-aEt-8u2rE872YcAABJPuJfnkLyfYCEKqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=NBXsqwrPEXhIrByMlUoJ_K1bTGZbU8HcP5PS_tJv209TmESnZ_R08XUrXv7QPgWHGZyM5-z5drV8F1jbnIhT37CKPmrYJkqomxpJalyKhscWBZJLiXrXyTOiLfbVvpa-ERselh0WLxlLvA-vQr_CY9ki57yy1AiqvrcIYvtMMt1lYWHM84EWSq9I7bNfgfPhu70iLqmpvhI37sEPjFL9vwQMueYncYqFa5MMYJpkR4yXGSAPBCTjFhuCZWfpHc-HBa01K02qrljh8lQfLF3GVWLTPp9HX0-OfS-UPc4ZSOfndEekCB8PO01nMDAPUHBXvfxhqKJV0DENtUJ7ODOzp1NVgUhOsRgNlKeAcVyPQ0WnBBzYMHaH5HugZP0ajgMz8cJmtsBDRVWyUevUcNdQSZFWqwb00vhnXA1TNwtjWKnrvS3FuyfW5VDYkzKNcRqYbMXAg-8gyNfxtgnUJLFz3abctNATYEu7zsdBZ4Ufd9CsWqjOeGI1fi4hbVkzP3tiyEHsvz9sDcO-XOCNPxFCWioCvEjqEO5c2exqpQHIYyPj5iUKTBzHjcsSd8PDz6-G4z1e7jJK-l6nZ7p1Pdq690f97sbGD-RDEb3lQ7xB2HJBtiJvBaGgWvMdKETt_gfB1zUpHPifJ-aEt-8u2rE872YcAABJPuJfnkLyfYCEKqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLzKwv-gPTVk4MlPKqrL_m_-FSi0WXctT-0SWAY9Hpr5FUVgaZiFtZSFJEx7B44-6-ZYvZjWHqrePd9rSOv3vnZGzCP7ziGODdXtqtCX9KpAjvkyZ_S0b_ZjUEyJ9SehVwR3i4q8gWalzo_dIPXNDorOWzBB4wMeuQ4urZGDSBL2BNbh6rVHEWQl2aLXMeGgE5AbBYss5bdoFU5AyiB2BFCOcBbg5HTQvwwGB2Cc4RFpUl62s3rwj4oEKbJdrAPFjzlwL9g3jEKleqGfWwysNN69VurmNkxfxy9c6R3G52UZXSw4ds1hCgpvwQGZiq92WXFfhL51Zwn7Z0IoFcLCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScTFbcwvKhvDEXjKfhg3D_4j6rF68BYP8In7zoXoFn-DG11uy0OY0yvYlSZYP1n799ZmZL0FmAuYVYBYM4V9-UxWYqAnPAXxKdhGl5OhGdDhh1tdnFMZabJxjgU4r-Pa6SpLnzkV2ZC1GZ3uuCMygDo_6ZBI67wXpboQ9mgN5H2mCbj0kshftusTUylvJPPsa8EPadeO_rsPDGjdD036860j5urbyWGtRw2Y16OGDtUwnvy51u_zwhYady8hf4wEa7e7t7QLrpy30AmXDJOQqCWq3DbduZ-_sf6Rr2hMKYCH5b-9lNkJmbI0e1eFPQ0RqUHOjH2SLGTQ-_W8sdR4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGZwEFIm_nj0Rkc0y2Wk2jDGZ7BdSYCmxLe2T5kAOwa00lsu_HkrjNoDkL_FC-pRcFVAMpQMpYWvxiZ-hP6X7rD_m0ZvXjaGdCd6r17bk6RTLhJesifJZyoPrwymtJmownqpnJRLOBCNwmZ1iYqPpUUqAYUwc-W8V345gPSJk-GN7Zs3Tf1Soooz5xG2X_akSKudV4pFyt80Co4o2HKWUEkvvbG_8_z6STUvz4h4yvUNZn7JuX19kyKk6bmhzvVAx-E3xMEH92Ncf-WYAKtvG0vi-DLsM4TduQj8KB8GsP37LBsklGxb3Jbz9fBpdvURsSag2r796MPsBYGq5RumFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FORmLxPEz_qQeK9_Auh4rvAzlJJQMg2koBZ22Jbkp4LDwFAKZD4K3ktarJSAhuEm4eipPcfOokIV-Avq68FC2c71j1DtHFWboXAXDze1lvfKVMV5P1ljtDSsIhm36VceojrNwe84R2p_SZeAIDj_li9JVFHX7IpJnnhKKlCaiLAi9HUM_J--Lk6k5FwsqZ9JxL963Bjn1kPnLFwxNWqJ5rBsByUrlZbnkC9IYaXT27VVVuW584Xlk3KyCiIQ4F4kkDMl5vVldVSbpCADC5qzoAastVSw6x2auzj5Z2XpJHDLBmtSvmkcrJAsaHhet_j6mkwPRUJKfBBFUIaYF0UIZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=icmMhkhm6B2jzRL8KJHP2B5edAVN11vUrc_m1hBVnkPM4ZeCXC00wxL21HSmWC_uQu1qhI-btzczlIgGaBc9m05zeZoF2NslQYRRjiYgNYBjnR_NFg_PTuIdVMOHpK6lhJWxJBVjOoLFpg5o3QP3qxt5f9gBkmweK59mcRmHtkjE0kFNEmWjArE6JOZ0qaEPdBx8NTR6D8nlWZ7r-f1WnoRK4hbcGEh4eD60KvnC7upotYV_iXXzpUnP-S7DwBzCZaPFpM6noB6sjPOMxaW71f_pKtfvBn9zLQjuBiPPV9pXRRKe3FNo0Yabfg1EMDkMvRjjgkzYh10Yw3bGP_9jZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=icmMhkhm6B2jzRL8KJHP2B5edAVN11vUrc_m1hBVnkPM4ZeCXC00wxL21HSmWC_uQu1qhI-btzczlIgGaBc9m05zeZoF2NslQYRRjiYgNYBjnR_NFg_PTuIdVMOHpK6lhJWxJBVjOoLFpg5o3QP3qxt5f9gBkmweK59mcRmHtkjE0kFNEmWjArE6JOZ0qaEPdBx8NTR6D8nlWZ7r-f1WnoRK4hbcGEh4eD60KvnC7upotYV_iXXzpUnP-S7DwBzCZaPFpM6noB6sjPOMxaW71f_pKtfvBn9zLQjuBiPPV9pXRRKe3FNo0Yabfg1EMDkMvRjjgkzYh10Yw3bGP_9jZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOy_UHluiQToq_A0H-wxtBhvf8GntiXAxFZjsDQgSR4VgzmlsDV0VpSTkoZQReYsJSkQRv0sMsLbxzRZshew_T3l3Eex2d3j-PLJL-i8-5YXr-6rEfz0QpVAearm4phRne-VEDB5cqIJmZxDzYRQ1mL_P2wib-wRv1gUixH4K4Q5kc-c8bhO3TjgEOtjPLVSi9znMkxhuBMPC08QZxJ50x_R8WlAXRfTKmx4TC6vhvBGwwh6ctP2TdvBrsSaXQccwjgDUtYCEGvvodb7mI0GdcEiZL0reWYrsOqj9ZR_K6WpXU14QMPGFJKLtIaAbGBkq_7mtXVaqAgRVteoOOUHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/torhTmhqWcY8ae02cpQzYwWG-QC6VRZW8XQ6u9QCMezLSw_Qdk3urkd0fddYacfMPtOXmnByK9J67QMTDLdtIRMyJALY5qWd6ExjXhSW8aTnlNMBevifeFtmmUz3iG9GUoCHuTYDR18X31j2FRHiV7eglrupjwD46okk364_TfA1eN1YuTsNVk4iczpVT7CJSFAuJDrJhFBpTFGXFsuWLOMNtLcavZ84xG-UvzpDTKXyDkaZBAr0zvh_CHxpSxoKT-Zv8Atm7yT0hVjDBcBGj_wk4v80k35fEMHNyrFVzrabXv03DIzDT2n0TV71ARbRXAkHwIkbRvPhvOiAoCR1-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWaKRBD30cS1Fzm9ym4f1AWBC1srDcoyb34hHY4syvmpKDz1vzgz-3ZZcCSFliWGWciL04Cqovgr_5FOb_tgQP9fFeAgz0PbLTFRkZGto7CAK3yGTnPO8nNhpyfGEceiAz79nYUfXY2E4-ZSGoBjAdhL1Mt3T5wnHElPf0VNl6B3mlsm0dlsVTehnBaI13CeY4aKL-GDQk_ahHFs-rskaNpKKY_fV4KmnCAeBhry4Vk2J_rI8hZJwD7CzdfGr-1aeMFFrqOTJAXHWMokK0w4fwpShdSs-AvvJVe9t5h22zWDg083_ZVHwivHXBmJt5ctGLNPxDxCFIBw-TyV0fDk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=HbjyMsYT0FzqeXdDOLryJt1e967g01JslU1GSJgSt4d8mOTpnmJEgctW38xks0MTyjxSpTaNTbWIafJe5J7465Un7Xb-8mYiYjCtO8q6hV9wcMc9DTmF4eozsDF6QnR0JMKwnOQNy5ejd9yYE6L9mEj8QhVeeY7Ttu8LQR_iEXc4yMv3ZiiwcAfZ7B_1Aw9HwZJsODuRCqjMjP6tZgoLbHxDCnMSyFFgCptK_rv-_Mtzw57JIfys8au2mBdKUdydaLT_vNC76ArIFOZHa5nBJXWcllt4eUlFXXcy7JtMsBPybgqy8v3ICwRbMtHAfxzqR-h7foUQWkKAkbL7ip3_3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=HbjyMsYT0FzqeXdDOLryJt1e967g01JslU1GSJgSt4d8mOTpnmJEgctW38xks0MTyjxSpTaNTbWIafJe5J7465Un7Xb-8mYiYjCtO8q6hV9wcMc9DTmF4eozsDF6QnR0JMKwnOQNy5ejd9yYE6L9mEj8QhVeeY7Ttu8LQR_iEXc4yMv3ZiiwcAfZ7B_1Aw9HwZJsODuRCqjMjP6tZgoLbHxDCnMSyFFgCptK_rv-_Mtzw57JIfys8au2mBdKUdydaLT_vNC76ArIFOZHa5nBJXWcllt4eUlFXXcy7JtMsBPybgqy8v3ICwRbMtHAfxzqR-h7foUQWkKAkbL7ip3_3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVB0kkSdMtzoLlV-2-VmMkrkL4VUqnDsEVhaYJgqbkU4zR9ZROYr6WT6OZWMIulTxchYTLhX4I1c6jKZ_aMn1O6sZyK4hsLS6q7Pm_2fIocUl6N1Jpyx1Vfyy2yu2hQRfcAdW-6OBlUlk7jx66eSYn7KBQ0nQIJ_88PWLZmfsaoEdYSvYmvJhTGZ0dN7bQFlZW8A6-fVyypuV4Ea7uFfUajzcEHuhayLcQ3oICTSdSwJtGr2LUHazRYc2yh-c3gN5GeDZ4_PhGFAH_P4qFzPM16Of9blzFt77HGzo0U9ATruYbFuOUHQZ5J_QzK0jZuYToBecvYHl9G0-U4DnrFwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=S8Rq-_9XD587vnsQWh54VCyVziwMIjTU8NNKLWqczvlfuYVVg0qF3cpA6DYJEhIzzRnnzTBzru_LQocRAIiKs93YP_BcXmQtAWBhEeW8VUAIiiMwi_-KCIo9BObCFtwOiSFKiJmAR7NChatdXRe0GWUgeub3eP9JY-08m4ZUgRor8WrQiG44oKh2k_qH51W-f0QCFqD9ohTQSwaj3k-xfpgRC-Ecm1YArTwv-Th2Kk6BfEBrqlKS50FYFQnL5bKAaSRPIp0Iy3FVxTgOe_2-5Mm8GbTMKd3CfTZ-paS3jCH8WOWbQvRl00TvXnQsZwZFqDHvPOkFKCoNIxj19FYuTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=S8Rq-_9XD587vnsQWh54VCyVziwMIjTU8NNKLWqczvlfuYVVg0qF3cpA6DYJEhIzzRnnzTBzru_LQocRAIiKs93YP_BcXmQtAWBhEeW8VUAIiiMwi_-KCIo9BObCFtwOiSFKiJmAR7NChatdXRe0GWUgeub3eP9JY-08m4ZUgRor8WrQiG44oKh2k_qH51W-f0QCFqD9ohTQSwaj3k-xfpgRC-Ecm1YArTwv-Th2Kk6BfEBrqlKS50FYFQnL5bKAaSRPIp0Iy3FVxTgOe_2-5Mm8GbTMKd3CfTZ-paS3jCH8WOWbQvRl00TvXnQsZwZFqDHvPOkFKCoNIxj19FYuTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuuszLIMYJzkBXXA5J23T305wZfnF53tOg_RIUS8rEOz4XpTgoaUtTuxd0wgxGY7Q1DvkYEFtt8x3YNjXwFUAJMbYe_R_MHH6BpGmYtSKr51EPvK93FJM2AGI8mi6ye3LEcATdYsMOdfxJs-5yJtvdm1_Qjz1RoaWidWCgnONviPNNnjgF6Is-8Hzb2MQmgV5LYcXjFpBbrgDhu9Pv4c5c514HMDBmn00-7d1h0D5SHcZHlr1PiHl8wQt-ERYFTtzsV0_376drQxCd1XE3XGD7n1FO6qUuvI-cpgdx5gLPdxYsLiFy7kO6HBaOHVAY3OUihkEPvJTNydnpgrKYBllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzup_Cf98xYV25dk0sgGzpQPEhEokcLMDeO7324x-_SZQGU9eK0pWCE6noeyKjp-JkWx4ije31T47BXLD2I5q6vv1h-Dbrdch9eD54C_Q_P4YzC3MdxYuAELD4p1lxpu4btk9kyru-Tq0LnexUyQg1CY6WanXSoVNDGOBc2NKfIu5ou4Uqr1Gy0jKLfjVORaCT1UfMeSn3Ueelzb9b-Ih1tz5eG6FGYlUjv5gj6R8tqmWCv_U5hsOfixCMuMlrPNET47y_bQ-Y5r02RSwN9KO_uGnHTg9Ia-QaPSYy0nym-TCsOOKQGe6veqVZXjX-rqQJqNn-RX1YAh5OjH6QAH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBFbugthzLOeYodivM2aifC5wSXPA4oBeQeUCOyVIlEGMAKFRe1mpzM1QhrYiiN-cycJqVL5eNAajyYRKUgY3Tt3biFMnAJo8WXLjvr1KDYqi-qt-OgFy0bRs3Ggdu-_MdufcX8yp2C0-jBsmU_xP9Kkg5_RsJmjY19AqY3lSq9qkzo8Rg9MA6yujQT3apEu2RUlnretj9R7bHpgbaMnMBXY2iTo6dSdOVTUO5YDQ-3vw_Q8Va8JeW343HAmevKxe47oINwemQ2fB1d3cr39q1paKEYeNWVycuIHIwtbb04BafoddQyP6GtRWS6DzRlhoAAHEhL7370jc0E6D9x2t1cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBFbugthzLOeYodivM2aifC5wSXPA4oBeQeUCOyVIlEGMAKFRe1mpzM1QhrYiiN-cycJqVL5eNAajyYRKUgY3Tt3biFMnAJo8WXLjvr1KDYqi-qt-OgFy0bRs3Ggdu-_MdufcX8yp2C0-jBsmU_xP9Kkg5_RsJmjY19AqY3lSq9qkzo8Rg9MA6yujQT3apEu2RUlnretj9R7bHpgbaMnMBXY2iTo6dSdOVTUO5YDQ-3vw_Q8Va8JeW343HAmevKxe47oINwemQ2fB1d3cr39q1paKEYeNWVycuIHIwtbb04BafoddQyP6GtRWS6DzRlhoAAHEhL7370jc0E6D9x2t1cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBlvQ8GvRP2qvgyiZvHSy0Uk2AcUQd0a2XGWnXuD-bxU8U5QUFViwWxLM6U6ROEXAsIUU8jevXTYE8mHrpYmBlFvJxbuioFRMKmxPIVKTUmANoKVbHERKp1uhACdSHBZKjhobvtnSsf47vE4s7IDqiCzZZashT5QfE_8Q-SL2dTWwiqW0W0GhBUlC-9feCWg7EuP4aCcbHJt4TryxYMyt9TjUjadFJx4QQSPh75zMEtJ6zq2PeRLLxVq-x9y8JtJ68SVb_bfe1kMrMJ7lBvSAq4HIfqbm5vplTdB9qLGsXmwvWMqpT965Za_S-wpjU_OszAg6TmMfwYkXR5xSnlRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nleQMlYrdxmzWU6u_z4PQM2i-dnETIpBf9OcrJjY00a0UmZFhfk9lqCosH_AuVjzNGCHFX5aDZQVSvXaoRbYtTe7WA9ICuGTatykApqUAK_frshrE9ePgXEh4uSGDUv7Szx8oCS6ErywSGyDnSlGMMcYzCcweEa9fBypUUmD93hksQPtg3vgUPiUvzGJR_ednCRjtqrJ5fiYw-KMVXEPtO0BkDpsJlWkhVaknhEMFfND2taCy32SxvlP5XQQsAzRIeQNqjWY7AMoFnk1XErDB9uk3qcq_pYiJuE_3YYKW7preTEISWuWiiEM0EKAx2PCp18oGsVvEFjyuIdrYc3q_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=rmCP_EwDfhlFZYutdDPYrr2sfA6XxgLU6-LwD12_3OPhMZ6AOHhTSi4LJ4k9F5WR5aneoRhmp4DSOixLLzae3TOYYDBr_t8iEKU35XK1Xb1GA8qv8PwUQXaBuWz0zod8i8UuxomCxIkDdIGIesO3bMJe-mI09iPWvhWcmRlGcNWwynn540t-NeY5K5zabZtVzA3zhJnCCMwy2EbuOLjx-UeSKUsLMl2vSm2YXQ0xlDQXeFguET9n2pQ6oBfUeZxYsIWfqWP9_Pd4l3jxj7vvNUiU67LrD1avqIUvDOofGqpdnnTzl0XQI4KtfqrYpPzJWhPz04t6OZyANr8fH3I9Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=rmCP_EwDfhlFZYutdDPYrr2sfA6XxgLU6-LwD12_3OPhMZ6AOHhTSi4LJ4k9F5WR5aneoRhmp4DSOixLLzae3TOYYDBr_t8iEKU35XK1Xb1GA8qv8PwUQXaBuWz0zod8i8UuxomCxIkDdIGIesO3bMJe-mI09iPWvhWcmRlGcNWwynn540t-NeY5K5zabZtVzA3zhJnCCMwy2EbuOLjx-UeSKUsLMl2vSm2YXQ0xlDQXeFguET9n2pQ6oBfUeZxYsIWfqWP9_Pd4l3jxj7vvNUiU67LrD1avqIUvDOofGqpdnnTzl0XQI4KtfqrYpPzJWhPz04t6OZyANr8fH3I9Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=Fni5RErjtOuPMnk7AwvtrWRCFn71EzlfiwYtObt0fXDSEFvLkIzoV7QOJHD7FErw4rfvZbUQAGCgtBXKOA-06WQXL0Mu60WWYdzmqh9iaSuFlNGOnZoZ-M5b1OHRxwEwbArdmtqXgBlezs9ZQcqZUmabZGImXf7-YNsdxOjsz54zB_P30NB2hCzNAcx54YgxHVVoApecf5siPjB6ChFRufcsn_pgtfUOR__Qdd8SJokj12LxGrAbLzqhC6wAX5SyVfw9uP6_-CXUcMJUbkCUtAYZaJRA6KWJ-BsalvvZQUNZXKASoWmxj194Cty1_Cs-Q-OFXdAQxzhNpZcjdgNjgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=Fni5RErjtOuPMnk7AwvtrWRCFn71EzlfiwYtObt0fXDSEFvLkIzoV7QOJHD7FErw4rfvZbUQAGCgtBXKOA-06WQXL0Mu60WWYdzmqh9iaSuFlNGOnZoZ-M5b1OHRxwEwbArdmtqXgBlezs9ZQcqZUmabZGImXf7-YNsdxOjsz54zB_P30NB2hCzNAcx54YgxHVVoApecf5siPjB6ChFRufcsn_pgtfUOR__Qdd8SJokj12LxGrAbLzqhC6wAX5SyVfw9uP6_-CXUcMJUbkCUtAYZaJRA6KWJ-BsalvvZQUNZXKASoWmxj194Cty1_Cs-Q-OFXdAQxzhNpZcjdgNjgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
هوادار تیم قطر آماده دیدار حساس امشب این تیم مقابل سوییس درهفته‌اول جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=omafs-cQd_lnI5dBwSu0Y0QgCybUlUm10zhzJF_ewklThws3qy77Af1ZLelL6iai02OsXO2VZ7Q1KqJi0fz9l7rvLJ207uOkX7wzYlP-nRjAzqojQd1TzZCGcQzrrJ5prX4HwXJSh98aRYxRUJDWhhLV8a31eXdq8bAnsOZvv94D2Dppthas9NfxCF6Fhwq9SA2oD9nG-bWN2QcTvy36mdl7M8yb-shiN9nNaNEcmIKusF55LhQ8yjXf2LxXwKEVJ9uPCnGIf2p3WWtZmJgXLL8VXH3RFxcSLUdxoRTI0OFM5Un2djWY-5pUv5gDToqLYGox-l-ybLYvsaB5eMvS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=omafs-cQd_lnI5dBwSu0Y0QgCybUlUm10zhzJF_ewklThws3qy77Af1ZLelL6iai02OsXO2VZ7Q1KqJi0fz9l7rvLJ207uOkX7wzYlP-nRjAzqojQd1TzZCGcQzrrJ5prX4HwXJSh98aRYxRUJDWhhLV8a31eXdq8bAnsOZvv94D2Dppthas9NfxCF6Fhwq9SA2oD9nG-bWN2QcTvy36mdl7M8yb-shiN9nNaNEcmIKusF55LhQ8yjXf2LxXwKEVJ9uPCnGIf2p3WWtZmJgXLL8VXH3RFxcSLUdxoRTI0OFM5Un2djWY-5pUv5gDToqLYGox-l-ybLYvsaB5eMvS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهمونای قسمت اول برنامه های جام جهانی
🔴
امیرحسین قیاسی: رامبد جوان
🔴
سایت ورزش سه: خیابانی و خداداد
🔴
عادل‌فردوسی‌پور: نکونام و کاوه رضایی و دیبالا
🔴
ابوطالب‌حسینی: علی‌پروین مادرقحبه برو دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=ZLkybubKnU_5Y-V84DJFPtTH2bMVBYiFhk3gJt76T8g8ergBNbPnV23oOPpCx5hyacc--rtGeRhgaF4TrPwTiqyeCD5jBGs14PHXfcTN-JYk03J_4yM0tTwKl667dfE3h91BpMqPE8IgyqsXART23rxL8ga0oI0jrghuhSLKu5C-Ce6U-R8NAKlUu76JnfjJ1bmbmv7PoftjQvkczdFL7PKzEU8LfGYB9eepW646U_uv2pVmTUGUJO8qVzjh-nep6LE4GUmx8oKgGoAGSjYtryj1Nquo7Tv7F1NbjlEuUuMrJPCGzJaD3dODsM3_ob1zxYmg73DbmjH256XvnXNFs0Z7jQ0f_TOep88lhK7R3Zrd1ovH0207yiyajvSmOqX7xz0ymnrUoL2uBSVvod2saFewH1sDARLYKfWfM0uy5A30Dqd7tEt1NuOHtLt0u6eeYKFBey00bonSFzK7NAmxzzxO1iZ7re-_ZhBInor1-eiJuN_yGfRy0qnCvZhVixDPDcKaGOPe8mGmrZ24zazbaFMY_NfxrA3vtta3jnLHHabTmWtPdm9IXzoRABk54xj7LgccZlqVaRhMHt2F9_csXyV9SiRDxgneCOEsaxhV9Skp-eRjpKbSpQahpUs1dzmc0dU4gcX4BI6AB66CVgYa9zK9LL13JVxRPtlVyLyhlfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=ZLkybubKnU_5Y-V84DJFPtTH2bMVBYiFhk3gJt76T8g8ergBNbPnV23oOPpCx5hyacc--rtGeRhgaF4TrPwTiqyeCD5jBGs14PHXfcTN-JYk03J_4yM0tTwKl667dfE3h91BpMqPE8IgyqsXART23rxL8ga0oI0jrghuhSLKu5C-Ce6U-R8NAKlUu76JnfjJ1bmbmv7PoftjQvkczdFL7PKzEU8LfGYB9eepW646U_uv2pVmTUGUJO8qVzjh-nep6LE4GUmx8oKgGoAGSjYtryj1Nquo7Tv7F1NbjlEuUuMrJPCGzJaD3dODsM3_ob1zxYmg73DbmjH256XvnXNFs0Z7jQ0f_TOep88lhK7R3Zrd1ovH0207yiyajvSmOqX7xz0ymnrUoL2uBSVvod2saFewH1sDARLYKfWfM0uy5A30Dqd7tEt1NuOHtLt0u6eeYKFBey00bonSFzK7NAmxzzxO1iZ7re-_ZhBInor1-eiJuN_yGfRy0qnCvZhVixDPDcKaGOPe8mGmrZ24zazbaFMY_NfxrA3vtta3jnLHHabTmWtPdm9IXzoRABk54xj7LgccZlqVaRhMHt2F9_csXyV9SiRDxgneCOEsaxhV9Skp-eRjpKbSpQahpUs1dzmc0dU4gcX4BI6AB66CVgYa9zK9LL13JVxRPtlVyLyhlfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPgDaOj98HDYbZ-MWJut77fZZPPIctz3yewn2FYewleKS_hmGqJ9GPu1K2CV9IipZANzsK4S1NupMg03SlTL04nxA7WNKUMCJpcJS1vVUR-WPzpifGdrlr1PaFzz4MJ3v5ntpt2qgZjrQD7fS34v-SMxrRy2RMWjTfqob79dU-HVP8xCdwebA58j-ZTofwm3B0F_20qZ1eR4I6zEp4XYtgRP7WBHQx4KgRAxp0wbZO6MAOVM3xnCLD1dVTvj54dmBqYSXBeYDaEJkD4O0n-9RK10Xp1gParNscwXTxbuGIc_xnTbebbLQNorl5D23_j3nbqmoyEtK7XlZ1j6oFphCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvOjHrUF23emb1EM1f6cxgorzvL_5FoNZQV-41ZNGj_C47CzS6jcaHpEd5d5yaRFd87lDIyxwsM8rTtVAjIMVmoUYsg__IknXZaAB6VUCrEJNvgrgg7tpa45rrA8TH0Z4OVr3jq99rbB1p8Ki7v2VXYkAao4IGzXF6ZJQxfwPH4z9Eyxlpu04FrxsDGFLerU2xtsK9bK1iOVzkh3YY_lsy5ouvSrfSrMOSxkJPv5VM0KNVnCFhQFnOnIsR2r4JEZ_2LT6yD6_Ua0uppsdrUfml_F-H4Xjwj6XTkXubW2X-wsmDAWWtSNNWuKfpG8YO0Fj2krJiPmUNAamIDngGRpnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0VXbVY7Uohlo-_UC-EKZC-iixtq3jfiGc6JRYJLPhTjke31lbPzqT_EIxsgvdWGutgxBL1I86PICcKK9yghipZII6OX5QKJ5UY4-S7m4BIvj0pU6nJWHyELPWzIjHHa0aeGfo-hrhcEiN7Yj12xxjz2ZRu6pCZhORa2KJKgwLxiduAjn6SyoxD0PKOcosiuMPLsd25fIi-CDX5Fp0yl40yZ-SbEagb29jUhdHTXnm7j4UodpCb9Ief4xNstArBbRRJ4l-fA8tyI5ILLQIcq8UMmOSoqT8WPGfIj-8MAOJ9ucv1c6nC0RplT6E326xsQTHO6NRXt69m3iVetoHa3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23370" target="_blank">📅 19:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIchvYsKov0a3QmGMrkUO6_y1L8E03YtEMmpK0kaav3VvEiBNDHMFElx0B_XP1kFZl2XOv1P6fldgbZg6Xq4Lp5UngGy7BxKAzlRZimJUuFojjIO21Qq0g_ahXsRT1XjwrEQNhKDuauLb-2jJ50X4jLSUmb7qomV0RtTxxtacsMnhkXTNczuHPxvjseB2lvB2del6WrsCKD2oPFJgIJaZ9FRUp1t-Fz8w0H-cI9LScUkv8Is-jnPbZr3cg_bjjA2HNgf1vTIZO496xTTDEJpfK-Fky9PlkUpuWpYDbURyEYiAzn5d1XFwHWXEW1grNzCfijgR9L5KEG2D2K3IntjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23369" target="_blank">📅 18:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHlUfvRFHq1OUAGQzksouOBp8IzTdG71AidggWboNe5QAHdxE3EfPvnmKB0FTTliOYZV74iY34a5mi1IwzRJ99IEivVhQhtmqZvXHCKfNnF9JfDZZw4UTIjAt2a2cvDA1vO1nOaBOLECYYZNEo2trPtzO8Vsde6PO7uLIJa8XHpKIi2HSt9oDfnYKKLvliXiNmHBHiJSXO0Dl7SPxIhvijRf6xDG1b-0UMcnZDq0UKLbYCN2tTBzuKPHqmuOB1QUZQakEN29ZA5_kr1AL0Oh6T0c5GsYqOEtCGcOFGbf8pLLoDMHrTdBcFQGXnCQosVJuaF6gOhKWJ-hLC1CKzFc2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQi2lF9lEBoFNzOEkjlvYWFFO4h2B7wENUT2l-DcFgyqtCQHckwkx6FOEU4T8qPKFtX2JW77JPwwJhv2JLOJ4-eKs9gt2ICEksSlWjE2DBzIa_SkItsaA8opfyqnqC7wd_avR6IhJABtcxww-7A8hNAvVwwgCWLbISL2ta7HTkbXKVi1ChWDYWcLnEUUwmfPzeHZDYjRf_y2v_sOwT5pHqlnateopWJUD9oado1A10qrCyFfV-XXUdKhMTwN8cljh4WW01DgG9FaSSVREUxczhedR5HRPIJQ1w--5RHO0nRovQTHR-CekhDkqq89mJHe3ksvrRBxQ1A9_l12Fe_NWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23367" target="_blank">📅 18:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy0UBUM7eplg-Gc_jugHySMdC8K7ShXjH0ZQEKJ07OAtb-KyJFyxZRQmL8HvWzoXDTDAuOiJ3RJcyDynnoLmaxN6wR46sHHtzMfVF2UTfS1ZFZHY6c15owOgi4FIrnESUtk2tKFyIOHQDwYi3u-VBkOa7C4rl2v2N2C5Ff6QNs-DBlGPLms-2wzqka402l7Q1NnF2ZzMucvd56iN7-v7pAiH296Q03DbpF1dpyh7EV7NTSVyyNYYPIuM6TsPL73DcZ_gedD9glXIV_r6jfZ7HwSKMvTC0VX6GlRcLDQZsXftno4wM6lZQs_XEt5Bu13ZmCgdD6yGCIWdM88mcxyFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23366" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=KkUeGaMEqyvAN42dxgZYMwHJKglS9XBDvu42p9Xlo_qV1LTAL7C-e5HKJ6VXqprJ2BvhSdJjuk7gLYZWWYP7A8TsMKet2pygtJf5bTaOIEhBjiir9_1WoDYfPOAL5jO2TeCZ8Fkj833XGcPDskZQDvsgiBCWOZzBLqDMSOjfTx355KDtLDoshw4r6dp__KH1tYmNPRTXh_KeX3n7aDR-E42VJTu0bNvaTapZBNvQskBMNpRHePwwHxIWq0kmAfT-T8kq7bvLQrQ01OfViTGw1ywZgNnOlJRWHq2ETs79rKhcuKHw9zVkQB1Aq0nzCRqj68rXUbyvmPKWM9q4zaKA1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=KkUeGaMEqyvAN42dxgZYMwHJKglS9XBDvu42p9Xlo_qV1LTAL7C-e5HKJ6VXqprJ2BvhSdJjuk7gLYZWWYP7A8TsMKet2pygtJf5bTaOIEhBjiir9_1WoDYfPOAL5jO2TeCZ8Fkj833XGcPDskZQDvsgiBCWOZzBLqDMSOjfTx355KDtLDoshw4r6dp__KH1tYmNPRTXh_KeX3n7aDR-E42VJTu0bNvaTapZBNvQskBMNpRHePwwHxIWq0kmAfT-T8kq7bvLQrQ01OfViTGw1ywZgNnOlJRWHq2ETs79rKhcuKHw9zVkQB1Aq0nzCRqj68rXUbyvmPKWM9q4zaKA1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23365" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIVfJdOCdOf5h3D7oZIFGGQuFpVIRAsLCo49MJ1oNZWCu2wltQfKunSL7FGBmThIKtiBM9u8eRzkZAG2ixVLG7kaP2vU0MGsZdiEvDN6q73OtTsUy28FXmezPcDg2oCWC_N4XSV9qfu3uBN2tROC_9Mxthj7wXclyEpG1UcjC7giNE27JuLzD-kW-COF8sLJyk1w_H-ZRpghqW26Kx9ESDX7U6Tl90hYyPh1k59Z_-30ksczUMaTv7durZOq2OhsCTDzbIiACpwdBci6fsiDenuDNN8vtubigME7hhlexLpnir56oAU6p7SQPzryDUfEkWIHYtQYSzZbo2aPrpZLdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23364" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O78URVJU34zulxtOKjaGL-kD5S8mI5T7pB7ukdsSbtMCyzxPPWEwlVsnaiqNilsW6nqTlFb98hjbIYKfDpHgpdMHDynpg5kW7TmoaNyUirsUK_FZRPU2-V4jmNsIhMRHMNF9RgEEU5xBpeZOt8jrI-wiuJdmQyiZlanAXE_aBfYY0tNsewN_Z_l04nyXdc8RgNpHi7W-TPQw14RJo0kmdHvPI1YSrT9MS1Th7yltAJEgdfY6lUIpqSMpC2uWIJc4OdJJ86uSs_Q1ZpvOg7KhyKMyvHsSWeNZgR3LhF-89dxrLpxhKZ6LCxQMux_rAshMehyF0jTMdBiW2qAWhAbvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
