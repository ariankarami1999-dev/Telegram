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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 03:12:55</div>
<hr>

<div class="tg-post" id="msg-23484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X57w7ZqpmfSsBr9l6tpNBdBQym80fZHdumgVIwImhFRbzUDvYUjYVPqnYEaL1ZXsLUEEUig5eVOK77CKyGjVkt-ExxAHcM7XsYwEZMB9XF1blBD3bWA8wvOR3bMRcW88KqhxmxR_1iu_McuYoUEyvFnhbR3qCeuJ9peIsUdGIXaF4uXl68W83T5xNo7S3gZ42kl-TQCZ-YMAkzvIZTVEAXehhQO_2qQbS1SquAl0itZhuUE962Fv4EVTQgqWTP9oCgMGLwDr3NS-lc5bymgkGnZARTMhg_JuNgE3Az83YAO8cnLx2tQsOl_48xXdfrtXssvx7TYhUMSytbR0VGK5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌چهارم‌لیگ‌ملت‌های‌والیبال؛ کامل شاگردان روبرتو پیاتزا کامل نشد؛ سومین شکست ایرانی‌ها در لیگ ملت‌های والیبال در چهارمین بازی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/persiana_Soccer/23484" target="_blank">📅 03:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23483">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh5_y7ZWQc5HdcOnaf44h9M-EtM0vaYixgfWhhwDptUZ6XAFMr2qStCaCWKEaK3q7ibH1vYbEUXrkDHBhtosR6c4jUgKqAcrsvaRTeoyeiNO6Q5Hhsx4TrnTJ5HqT4vpW57TqhAivyetEUm1CPsQZfjUMUkv8LNxAs7nZZ3PrUr54PgEeJPvAWjE1lQr2RjlO6TCBZThz_UMRvvyi2daCze7egMBGKSiCwpEyP7q12xrDCkfB173wMAHVN-GVMKaqLPKKUxSHyt6qOh9lEZbN6QZPebF_LUTDuLuuEk3mYBsUuPVQKR4p-MKih3ynJzkG0a0qj4Id5S_ExJjzhDzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نماینده انزو فرناندز به سران رئال اعلام کرده که این ستاره آرژانتینی بسیار علاقمند به پیوستن به‌این‌تیمه و حتی‌حاضره دستمزدش کاهش دهد تا بعد جام جهانی شاگرد مورینیو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/persiana_Soccer/23483" target="_blank">📅 02:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23482">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxfN5_n2gEJD_CA7qnqQ7qYlSTCkWnQRVumviGxiI_bQ-kTKDDYtmz46ZCDLgB_3wjc77SMiPLCvq3DLet11ZP2l3nc3ysVwxVnvfSz4P_RUIjlt6z3kd53Uq2FKLMAGIHDJu3EtPP2DYzgW49WqpQM1ftUeSGza2TaSDVOkZD_v5a3aYJwBWFQ7W4ogk4fCfmrcEmbeysPCLcHNAVtpPFI2f9g5uqYGl4I5P9Z5512Heo7tPkL5jS3ds_wufH6Jqd25EYnIgX6Kb6R69vgAUg9oxyqx_Eh72GDXHkGxbPGadpJ0iiak2ll6crv8cIiobd2n3uPQKlCOb8FQqMzwLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف لاله‌ های نارنجی مقابل سامورایی‌ها در گام اول رقابت ها؛ نماینده آسیا به شاگردان کومان باجی نداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/23482" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23481">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/renpx7ADW9ZQCdeMHsJmC8Qu7aAgibktLoPmNgaY_is3ba5lvjnjPmfkrEzeE0iKiY2Pg_Oa4WYl0h9OrEzGOHnhWT5--SBTCfroDL1MKHx0Jx_Nk9bBjfMfPKpeRH2C7uexo5W19LT_eMym4DNp3RQZqBY5oNyBdPrv6rSdj50MnafPRnJW_5-0bGAXyJPgAj0NZBCbqFNLI-1R5JgKhYT-OYaSQJR8ix7T5HUiPz5dJQkNUZ4vOhqRdZMfFCYXLuGFQyfToHPYDpwnC0O9u5jLhKVB59qBCsjTGXAlcDoJwdmI1v0Nm2Xy5iEUyFdsaxbNN0Abc4Whuy0XO4WkJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/23481" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23480">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD8tsEVO860FnwsocAEkiIFcBOFuZVuBuY65yhXLkZc0-XJyGBIBVGXb0i1NcDhwfL-5YAdNQa2F4IvQVlRBthOAEKus7Fw0W4YgHoyg4Okpua-8_Zt6ZyucmxqnRcanD2DghO04XoIFEjBvVy0tzIL0G3tabr_HY59Mjkvin-vLi6uo0tKZaUjC9bxFmHmXp2ghpirT4_VpKHDdgG6aZhzE6O3kW7E9iIc8g11h-pyRFF6GveBzCuFfz263WyMdFs7NlgygGeKycjI35Z0FUyofs2-7a9OuwK6i6vf-NaRoyGCPvfk0sbvXK_Wte2WxophfYaT8zlovx5LCzX3eOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
‌جشنواره‌گل‌ژرمن‌ها درشب دبل هاورتز و تقسیم‌امتیازات درجدال هلند
🆚
ژاپن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/23480" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9b859a0a.mp4?token=C1vAL4xESfGs8klJIS7cSzANfqnRu3pqni_FI7T97gQKcI0lNBpWAP6eYhf1_JENyEcb-1V6P4PNToFh5BDofJtPkUHjC-5TLWx_kXmQ2oFuahMdeHG_Xaz5Zrx0EHD_dZZa0VF8Tn21YiU20nYy10n3SvUByFXReT72ZuURs-0Xa9LB9l5XCCaMKK85xvZpIWGve6WHAWkQASNM7Rba7uw3W4M-0Js0sdDEVgfdEePkKL0b3spCze-UfiHf774l62WA-AWdpjaTidQfeJ4w8HPTASMF3xPw3MT8ldmcKFRI5rHF4DRuJaDt7gmSNzSm2ndRfbX-LLkZtc22KAi4IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9b859a0a.mp4?token=C1vAL4xESfGs8klJIS7cSzANfqnRu3pqni_FI7T97gQKcI0lNBpWAP6eYhf1_JENyEcb-1V6P4PNToFh5BDofJtPkUHjC-5TLWx_kXmQ2oFuahMdeHG_Xaz5Zrx0EHD_dZZa0VF8Tn21YiU20nYy10n3SvUByFXReT72ZuURs-0Xa9LB9l5XCCaMKK85xvZpIWGve6WHAWkQASNM7Rba7uw3W4M-0Js0sdDEVgfdEePkKL0b3spCze-UfiHf774l62WA-AWdpjaTidQfeJ4w8HPTASMF3xPw3MT8ldmcKFRI5rHF4DRuJaDt7gmSNzSm2ndRfbX-LLkZtc22KAi4IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌محمدسیانکی‌درباره‌درآمد گزارشگری؛
سیانکی: هر ۶ ماه یک‌بار ۴ میلیون‌برام واریز میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/23479" target="_blank">📅 01:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف لاله‌ های نارنجی مقابل سامورایی‌ها در گام اول رقابت ها؛ نماینده آسیا به شاگردان کومان باجی نداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/23478" target="_blank">📅 01:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-opPYMbvEDcylL2qmIyi3nUqCkOEx32OnIR40Ix5LBtLJrBxS7XV77H6FAnqVvcSvirVY8hswaB6b6kNP1O2canzg23MvjHnRh5bnsjIgu7svnVuLorZEMLyUwI_5LrDb-5W8jjT7uXCPxsIHef12p_eLhJGeKMh52Zi0hxHNQu4XFX7CwBft0lndnBLUOpsaq2l5hdnYvZDfiepr-_wKUDG1Hm2_1Dc4ncQEpYly9lzEEfgToc3Z3l7TNdvkB47cT6Gg2vGtMen3QEsUQqPOc5b-Gs-PtwG6UvfYAiXn3tf3EUfiRyUnCqCQzKA--ZToQi6P2HWhSGHrZjdTuzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/23477" target="_blank">📅 01:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23476">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/23476" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23475">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/23475" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23474">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23474" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23473">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaP-LfvB5s4AfAlnNSNQ0azsuk6JeQFM3Us4j_wjpjyJeH8HV-V32bUwOQ074JVP8WAInX7VfAnRcwaIYzqt7GtJ2QBtw6zCEi62fAB0VkEpVQbgQ1Glm30jRAxwPrcPgMemZUVbsicwzd98jsLTs-2NfheqcKHAygqqwWBQfQXyltdU8JXI7cRQumYNkUX3kBysfxzGb_Hr2y8ttiGR0K05DLzfeiPNqPW1JbzQWbSB3y0FdAPPI3J6W_CMIIIfdLubeWW2tOGZkvuEPNOcikGVwiANr_HS33oj594yDOVgRSRySMGUAong0SrfV8xp4BFPff29H38v8LW-LW_dTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ نخست‌وزیر پاکستان رسما اعلام کرد:
🔴
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد؛ جنگ در تمام جبه‌ها پایان یافت، مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23473" target="_blank">📅 00:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23472">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX5KysDQXtzoEB0gfaaDvLAziLbAYApI7cpapFOmtRIaZp11_WA7CDZfVgqwVMx_u-X3bu4ZzQdg_Hkf4wxva8V0yax9MMwJwUKQ3GkCSPQorfVBppVlmSwSoA3KqofU5dm9syNhUGNIWh-2jl1HO5CmxPtdmol9zCgM9PFlaW3NCljkEZXlevXKLFhMfPd1XzwAtpeQXHtbw90YoBbQphTyYM9Gn1aDB3AKSByMbZQoWfkviflLWYmgD849bFtZlRYgiQ90YZ0PuG9k2Pd6DTDSMmvQR6PJQHz6IWxXJGRotrNybKXmgqrLFl1huH-Wp8Y3najhFHyhe6YmJ4toww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
#فوری؛ گویا دقایقی‌قبل توافق میان ایران و آمریکا رسما امضا شد. ترامپ درگفتگو با وال‌استریت ژورنال: بزودی بیانیه‌ای صادر خواهم کرد تا موافقت ایالات متحده با توافق با کشور ایران را تأیید کنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/23472" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23471">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfDDjXaCObsHk5n4PFssXkv5LbCbm7HX_9Zh10uITlKSMvQYSj_yYe2Jw2zZ40FOF7kw8HPRStU0pBfbbfUzy4v_9CHMSPoCFpTogOCK9FfX-EtFp7n-BnZnBsW8WRfa4MzMGBrJiem8CMxkOUqTvPpMCBpkwfqjLwWMHi3OpbOTB67YfbNrT64DihjGZSWgmRo3ATcQsDLKhkPlLNTMmOdTyiazwBJn8_hrwjW1MlXYnOKu4ZngaTqQfrEHuvPhpGu9tJqBHIgdyEihWjBQ9hKbvz1KkcRZ6arEpxrPhSvf-dYVD0Y8GdJrOKn10P1R3iIqopdfv7iByc1BUh56iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
انزو فرناندز در گفتگو با ESP: به سران چلسی اعلام کرده‌ام که برنامه‌ای برای موندن در این باشگاه ندارم و قصد دارم راهی باشگاه رئال مادرید شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/23471" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23470">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJH9x5GgOp_BSwaaTFkKwz6C_9k2LefSQikoQsXtJyKiFS1lqCqXH-lBTfbBVDpxnUogSsfKeOUG414I3smO29UDd81qKp_JyohtabXqrByCnw1CU1oFElmzlfqypLvKypP9t61qierDYjSqlo518Fx7kW8dS5Zc9k4NITYCNKAZoitU8IFibz8EbkLmFpu0ZK-aZ-mfa3Q3Wy3UIKieLEX97lTBY9V3QX1wNkoPMXjPfhoLRcn5H3Ywy6UqP1tyvjjG3xOYViZ2ws8HFNKyggL4avnI6g61nW8I4OrHFiQfdRAmAmRerWdRqvseVew5Y3vR91YyfwqrLi9UU1mh8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#تکمیلی؛ رومانو: روبن آموریم تموم شروط باشگاه میلان رو برای سرمربیگری پذیرفته و گفته با هر شرایطی حاضره به این تیم بیاد. سران میلان هم گفته خب باشه بزار حالا ما بریم دورامون رو بزنیم اگه گزینه بهتری پیدا نشد با تو قرارداد میبیندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/23470" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23469">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDn5avfzB5kdz36xohNC6dkU352tRybQCxVxsSCFFxN3VWUz-tYQJtiMQOu3t4fXxtMpDpcn-IW2S9UFeLUn6QYgnN74-KrXSLplCzoq4MV0kDudqvc5XzS55TOmqfW3xp0e2C8ApZ1I9j3y8ryE8uMWLZ9f-K1xpyaLW9x8sUpvnrwpGpz-rwItHFLgeckgwcnxJvcktjDo9TCxEwG1KU06OnwEAW1-tc1fVxHMRGycQkSDVFRvleg9JMWkhR_i-YSy9UEgpUkKbJNxPNwOPc2u0ABdBHIpRbkqXt2chip43J9ylUlkbs4ulsGP6-ZEOO-Wfa9Dci63-eGCQY7OBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23469" target="_blank">📅 23:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23468">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8H_gPz-66xG75eo3HHD6nnx6goSs8tIRDmT1HMjxM--06BTEx3Fu0rWYfi_LoZ4kzOJw3wWSHAdP_ZFMubq0i6__jLSUbcyhVRnnEbrAjb9f_r6itAFNqfmp0_dnEveeBKnwttgxoETCC6LrtYCEwOP0xswLm9k4gTHuc-N0jH-0lizHpWiYPW8l16UfCFv7bajxEBlxy9G1hxHxQQroGTA5ruFdgDCVdyHDd7l-RG70GFlWVYiOVac8KMPe0DI6ELzm-Hc2oAlK3igTinG1TBUSupaM121NhQr-lbAnQ2YGfdhQBQ4gSEUVAybU-IKTISBscJeodlc00-E9Sd8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاریخ‌فراموش‌نمیکنه بچه جون؛ یه زمانی برای یه صندلی اینجوری داشتی خواهش و التماس میکردی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/23468" target="_blank">📅 23:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23467">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmNLS0NQ7OP495AZdi-DFq5nTswnzJ4PJAGOPTUWtz02VBcAB5cTe1N5qegENye8vKTRg3VNUwi8jpifIuGq8JS-BzBmxkvAsgM2haZca9iV_JULP4BtczVuL6Q7E8Z8Ww7PbYPbOtoB8kMwIWRu4rm3c5eP6E0GYlAU8M4xB0f8-rFl3d2Yf-MHGuOP4mC30WZCyWOciisG9kRKUQ-rY3z8OGeCy_Lj4XkFa4llwyNCaBcGzgYeHMWMzt9Z-AmCfyYLT4g8C5eKtHG_QOo-isfHkL1RzBeB3vIwJroP4DlX9QBQ4xEUzjAzWJj4UidkRqKh_CWRPngKOK4refvkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/23467" target="_blank">📅 23:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23466">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23466" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23465">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی2026|جشنواره‌گل ژرمن‌ ها مقابل تیم کم نام و نشان کوراسائو؛ شاگردان ناگلزمن در ایستگاه نخست رقابتا حریفش رو هفتایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23465" target="_blank">📅 22:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23464">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO_-L-YpaDK-QWcwmXTQFcejECtsmMAPAvTk1CbBUXdCTxIqJP7ZNfkSUWL_GUI9JHx71UxKDPrHt8_tE_9Lc7ZjSfwQrhw2tbAFb9zSEBe-BUf-b7q_t0o9M6IlmNV1mjOu80Wlor8PGeEAeBGaSKeHDXjojTV1coFA4-Bfvae2uRjyoZKyPaW1OmmlT9_4mx9MU6YSY_SjqO_b-S5FdrQUEwIW80x3KfjJPFykoCcnxYePiplSBpoZXy3peqhv_pvGvDXbNZ7dPnk-347OgRqODz0orczIyuVFzEaVFlx2dx7p6sNjw61KneVZ9u9RUCT9qalyKfSWXSUGpSdSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23464" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23462" target="_blank">📅 22:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGqGozDbbH_xGb8kVTmRs5c-ZPETzr3abqYVAasUgVeZSiiBlvOU1B5MfoRCciniXxPEb-fQn-yl0EhYG3VGJ4QH1XaGBxbqaz86nCue7cRdLhIZ0-ShGkQzVqcWH-xPE7fyfEDHvIOEzkp96qJTcAXCcPV1ONgXvUmujW-brmbwQseAD8GZfCIUelAMrqV3uSwWEI-NhCA1T0KbrFWMLZyeozjkrW-DN8LDfNcBYhrPrnc0b-Qe1l1ujkr7J4E9Zapd-eQutCug4dzXF40AjopqGZoSRGGLx_B3QbisPoIe-pWteEbMaQafAHhnJNrqnufY6A6dHyvQjRgY-49UJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23461" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23460" target="_blank">📅 21:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8GDHVyMSwB0WaxHyAe3A98BVZl8XsuMYSno4R8oWUJZrNAPTG-aZSU1hs_GnZKUArQ45HinPGz9meyUjVx9RDsZ2e1QSdA-Wnc-rGhtGtwFRW6-eeGQpP65AzdEFzgcTYc8W6f5LMywJtGL6-QSD7aGJk9XPqK6Jr38Z6VLdsdiI31MPXEYuMstCjKwZr0sCCVx_cVAhSdAhAMojV2DVhPjmbVsousvAN1knxc6sYJNEvU68banakZugdmebx1wFdp3XDrCfP2ATsjG_d0FRGwfioZZa7WVGPmAf2pomRrUJcqeU015f6X85Nuvm5LKcU6sf71JKqNIiIla9dcg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اصلی‌ اینکه اکثر بازیکنان ایرانی خارج از کشور علاقه دارند به لیگ برتر برگردن اینه که چون شرایط کشور خاصه و ممکنه در هر مقطع از فصل جنگ بشه و بازیکنان‌ خارجی تیم‌هاشون‌رو ولکنن برند لژیونرها قصد دارند با رقمی بسیار نجومی تر از دستمزد فعلیشون در باشگاه‌هاشون…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23459" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8YLKwlbOqiTmfJKQ9PqmNqTXD3IVmsioKuPdFNneWKg9yIUZqNyy9dY0peirQfbTE7HbeejAZyROtsJPYiJ8AVa_4RmwgYH0hBS7_sLBMqaYC3lQIGu4n3eKqrN74hbj1dstI68GSOVt00WqP5HoE_tM0p9NPwwKk4o6nE5x3ZwTW2c3Ws1L-uaiMtbLboMWeXjlSjRHtuwcYJNXdUSNp9yD8G2FlnAI8t8Ynm0-ZcH5NKrbFLksKOL1cjBybnuFJgS6UATNTSlShjO4VZ15KDdp_H0rzqlcu26O2bPIzxbJuW8yAgsltoaj1Paa5yyVHM07xpKgHfQUmcZTRopjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ اولویت اول رضا غندی پور مهاجم 19 ساله الوحده امارات دراین‌تابستان پیوستن به باشگاه پرسپولیس است و درصورتیکه کادر فنی سرخپوشان روی این بازیکن نظر مثبت داشته باشد جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23458" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-9mrTb4rS8JGwe1eYAkWQYsJHodWhqqyQDb_TMn3crB9_qaNX7h-N3pSy7L97zfE5P5s07suH1_NxCi2JwxGEFBKGOilNMV9PgGjmni4PmWfmZLCHYrIrZV0kOOd4r0IKkR9jW4MUXvvil6bTcdJWytKvnTDq4IlOTTN6XzB8MwmntHGE2umgwZi2EASpf6ePmeYlMAC38phZbqdXKu1zdA8dfCmIwv4WXxNNTxH16vLtarA3A9ltf4NPtN0EjS3FqET8QEfNi6c9DFZs9Rrq-iQhG1P7OnSCiy4AdLWaUQGl-MA1B7y3coBgAxizMzfj4XwfOT99dHaLAaqHC-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23457" target="_blank">📅 20:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvX9BJ7OjLLASqYWuqI4uYPEDyf5qHOM7IscyyL6QzqElCEzBAt-TRSxA0mNYR-QwhVVw2ZRhYyOTKIU3cHckrZYQ_R1cnbLGjJ-GNWwoX8RsFCn9LGKpI1Wobuk2Q2lscuc9V2Cv1a_E2WILnkKOmwkaN2uAgMhMGibIN_V9YNs_BMyr1bVQaxoTO_8nucZ2DST0yENj6rQPKPkBqOeVEtelI6TNymlntjwI-Kug5DkMpQKcI_MC9EvqdyA6IZwQt7xsUFjP3K0PovEF8cG9TbAee-_IhSSwxJzB52OCs5MkjLwQwjn93hb2d4mnUvHRZQT5Wxzy5dhbtAGeB5VOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چهار خرید باشگاه رئال مادرید در این پنجره تا اینجای کار؛پرزبرای جذب‌کوکوریا 50 میلیون یورو به تیم چلسی‌پرداخت‌کرد.درحالی کوکوریا جذب شد که اکثر رسانه ها خبر از اومدن کالافیوری میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23456" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=aKY4Y6MivsUygZOCVEekDZo4Ju79Pvgu8BjSZFas_itFP-L2Js4h5W2zPSt-VqMgmVJTSRRDZIGcEVNpA_2KAS7CEVxml2sy_c66qu_gRNI9KDv-T85Ehx5Z4Ag4HdU1oXbAvAqemscsqXgvga3XZ-0nAfR3MQtneGXkukF3ijsBU3V5M6-ElegQdCPY0K32yKDKzr95kpIH_wKeHpXY74Jd_nhC3kNKFGDzP23WEu5jlk4WJ6ZKzmcXSWTA618LnhCvOZe-QiuqVEjb9sVm1EGcXS5-lkHM0pr1xSm7No9z32FCsqJA3cz0FZfiuKIX1mm5oeQnqiQ10gsM-doVeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=aKY4Y6MivsUygZOCVEekDZo4Ju79Pvgu8BjSZFas_itFP-L2Js4h5W2zPSt-VqMgmVJTSRRDZIGcEVNpA_2KAS7CEVxml2sy_c66qu_gRNI9KDv-T85Ehx5Z4Ag4HdU1oXbAvAqemscsqXgvga3XZ-0nAfR3MQtneGXkukF3ijsBU3V5M6-ElegQdCPY0K32yKDKzr95kpIH_wKeHpXY74Jd_nhC3kNKFGDzP23WEu5jlk4WJ6ZKzmcXSWTA618LnhCvOZe-QiuqVEjb9sVm1EGcXS5-lkHM0pr1xSm7No9z32FCsqJA3cz0FZfiuKIX1mm5oeQnqiQ10gsM-doVeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شهاب زاهدی درباره عینک خاص‌ش در برنامه عادل و عزیزم گفتن‌های عادل به شهاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23455" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23454">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23454" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUxBTm55nczY_m8BxWf1QZBB1rkObc20VvH8O5Do1F4RbK8gJWYmKw5LmUtOF8m5ze5110G20aAcGvuHwGOYOI9MYGe0bZ8SRXhcZmRVpw8uEDuXs8oCi8x_TOGONgJJmPSmKozyIHs_FMeRQ6w0sdbKEW21-aNysyZxwlYpJqgDyKIem31UYEa1CfrM-aLaoSWjyEMBxcbJf2wIUxtkCK6k0qvhz6H8TE6e04DDOE1rHTg77AP_cUQ2QL-jUfE7MSOFhfqyc9XtuV8TjWTm_43y3ZP0lM5R3UaP11LV9GRaOiBfe0RbdMjAv4JdTfRgtaXpxRweVSpbtLj2gEv3zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏐
میانگین سنی تیم‌های حاضر درلیگ ملت‌های والیبال؛ ایرانِ مدل پیاتزا دومین تیم جوان این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23453" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23452">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9ckDlGZvCNULN9smEJtShskyMcwnGD0lxS3bb8Dbc5Hy3Ci0zMX4lJN_RQLWCOODXCFGbCu4pJlPVpTCKMiqSB1PMOqGnKgzf9dH9QD7Z0OBoWkg0L5go2auMf5gfTTv60dMB9np32sVmiE42-J3Peg6ecUzRQZJ9mL9d361rj0vl922yy6huj76FroCARMJDjvgdGb1liboncnG2zGk55oOYTRfBSIwWoEz_cJOIH27OaO-ppd7LUID4WRmlxDqRhMKt0NYlGTdS-BPdUPnuAGqXPG_kd2tkBtEsmNzR1vhTJj6MY7nybm6mvWk1b6lXy879C017JABXxgPC2NsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23452" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u77ejBKK-aFHkMc4a2NzaUyJZzfyypEbmLt5AbdlcXUR3emeICktC50KZiepqkukf2A8k9EoRxNGpgigZOMG3C2fgQgymSizCgGrzH8rc3bPRNJeFv_aQivQPONoCThfsfy_9oT5TAPwwnH7Q60oF2N31SgaZRXnHsaH4_OqOYQrC-3YAxESNOO1eJIQ9mqx01d2zrmO-QWiMMPsXQFWZ7ddt4zoMXmS80RKfYqthDOV0KcGkjU-x17V6WzYaa9qge6895k4whRi3zCDNADdW8MsfMxGrpWEv1Hz2G-oLNlHW21vhirijuF-aWOlSQSVkpay4Ol-Hnhmlb-kvFSrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23451" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQQj_Jc0LRrk-z9GbnRLKpDmOkBXMFKc-KdsuFBBDnJHd1bt2QLrXXkbuRRzHiuXZVya0iD_6RjTS0IewOGQ2EDLVECup_CsGShoxwX4XRA7Qc9tlD4cUAmP1lpnEoPgwvQUmkXwrTFhyc6DEe5XbAjGyWeTd8_mkPQ5VTFY4cO8WyI5gj899gYcrg7HCR58etMQCYq3Zlhl7ZWpN0xQC3nrbntg8d6etiMETmLYFkegaqHqTDbXzExDDG_oHkbTv2LX4hfFU6Pqu5IDKaFmYXPWU1aE6bcTo3l2_nzYu44lxkncPFb0Txt0XQYTHx__9V4GnsYzBFHHeCnb8LV7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23450" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=rl-9CwuFedRdc8lYGN6VE2IYn9to04NVuZtpXTEz7dOSYXEYtCzpMCaG44BfxkUZ4Y5o6mCsE9aC1g2RS6G4MB4UQGxPshKMQCWPdg0PWE-GrhA4NanDIKi5-3I63ZCJR3WMamDliO-jXVm0L0sSqF5lHzjjIOIgdRB3MofCZByqTwrF43tH2DepVOWG2YPE8B3LU6251cvMajKhe5bkuriSyRjC0ru5T41Kw_eDdrM_m21tYq0D7qj_pGxzj1HazTBqr36pr4vhDfBZkQjTYp-gBHAArLa3lEgi4VARaIdp-vxQ6s1wca8WdaeWQ9tEBO1DKqLJZqt0YbIae0Iodw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=rl-9CwuFedRdc8lYGN6VE2IYn9to04NVuZtpXTEz7dOSYXEYtCzpMCaG44BfxkUZ4Y5o6mCsE9aC1g2RS6G4MB4UQGxPshKMQCWPdg0PWE-GrhA4NanDIKi5-3I63ZCJR3WMamDliO-jXVm0L0sSqF5lHzjjIOIgdRB3MofCZByqTwrF43tH2DepVOWG2YPE8B3LU6251cvMajKhe5bkuriSyRjC0ru5T41Kw_eDdrM_m21tYq0D7qj_pGxzj1HazTBqr36pr4vhDfBZkQjTYp-gBHAArLa3lEgi4VARaIdp-vxQ6s1wca8WdaeWQ9tEBO1DKqLJZqt0YbIae0Iodw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23448" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7bH_5qcDzgOmfMjZsgy4BKznv9NpmfXIvUchXIAgKx4O_2Z6zLiBqX6ZMJ0S1Lbm761QsbLNR2xdbxzgfHOf7sMyBUHw1brt1VR4vd-4G07WrpErFzYtEstE-oBoRKJ_NmssxBtjx37wMDWsR6JYCyr-mRQgvsnw1AUvIsmfd--sSghDBoQrtLH17GCHy8OUvYTBhsRCjhFsdMGAKGs2ZVdh48Rs_KKopoRZ2pFukzJxXySI-zjIP3TnGA2KOHChWrnD7duiiKZvbjtdm_HG2iAZF68jS2xkXxQgE241qBAsH6HdLrlUKSmGgQKwBuJzdvKB5fV4c3Lu62FSZppBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23447" target="_blank">📅 18:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔵
👤
هایلایتی‌کامل‌از عملکرد درخشان محمد جواد حسین نژاد درفصل‌گذشته‌رقابت‌های‌لیگ برتر روسیه؛ قطعا‌بازگشت محمدجواد حسین نژاد به لیگ‌برتر یکی از بزرگ‌‌ترین بمب‌های تاریخ فوتبال ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23446" target="_blank">📅 18:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4RhIYxpK547RE2j2UNbohoDNfX8iPzaL41rGzrSM94Gs2kF4Cb5RTnUh4rEJaAj-xDHHFpNNQQZl-qNLvHpWr6wld7cjlgPPE020FVbuN_gr9nN-OLAsOOZ5i4oHgHWRIvL0nlcnvSUcQ8pMKY8aOvnJH_DF7WIGEc9FSH472c4K4B6vQbB9nvwciHwb8WUpi_WhsMVvDUF63MJifwUrBsku0LXfnC4NzfEOHQ5JisrEFjXmPxddnPfLtw68xKoZh2wElm7ZW1oKbVh9160TQGSwkUHt6Qa1WWUP3OD0X1YoEcuyEyIS3oh4v5IdP_P9KeLs7Vf4QIKVaImEqdO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ ایران میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23445" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-hQjlmeRiq690FQvY2nFph_5cu0cLwbRaDG0d-6LSg2tpGwQ2euKRGrtyY_4QYHpobOp4ezi6UO6ZsJuU-tthBK5jQu68YBRXlsi-q3WAuBD_bBqTsDn1fGT4FkUb103oJOfD5Ku5oMOELwf6H5Qrm2_Zk92fRlzdFi21yEjK_-oJCRNm_MiHsIJ6zHk580rh-YbMWe-pa-JHOAbLxXayUHgXQgXtFx5lsJnB2KFYu4CNO05BMSPC-1XsYH-zXzuzLZpDL63s9tZd4PMcRLMc46aWigzeIoiX2MZoRq5DJPo1Avz4KehDy1bxj9UdixuCZY_K181i-W8dFYjRnbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت اوپتا پیش‌از دیدار ایران و نیوزیلند، شانس پیروزی‌شاگردان‌قلعه‌نویی را ۵۳.۸ درصد اعلام‌کرد. در این آنالیز احتمال برد نیوزیلند ۲۰.۴ درصد اعلام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23444" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=W6xu5SVJtrtwOuGxJ1ClwAmceaEQ4lV0KxUQQHQbLIwt7Nu6NZuR9aVf09l9Gl12rAMEIMkGbOmlPW6LokOrFUGoxg_Bpj-CpOYYrzT8kAE-Y9rBK6i3R-0ty70JThPZbbRnYOiROuYnjnNMGPn6zZ2VA9J7mZIokuFTSgtiY4jZpoWPuPh9hLlptruXNhjB5pSfcd4kq_TH_H7s9jVF0QB6ONhJRfp3nS3nCujs3cgJxTeNhIr_npqCSdz5xLEyRKpJpnEzZVYQ9PSPJ36RZ2WY0fCdHm5BP9pRWNWl6QoVQBEsvLXzQsEAnPLfSNP57NxMiw6ZFq1D8uJcqAh8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=W6xu5SVJtrtwOuGxJ1ClwAmceaEQ4lV0KxUQQHQbLIwt7Nu6NZuR9aVf09l9Gl12rAMEIMkGbOmlPW6LokOrFUGoxg_Bpj-CpOYYrzT8kAE-Y9rBK6i3R-0ty70JThPZbbRnYOiROuYnjnNMGPn6zZ2VA9J7mZIokuFTSgtiY4jZpoWPuPh9hLlptruXNhjB5pSfcd4kq_TH_H7s9jVF0QB6ONhJRfp3nS3nCujs3cgJxTeNhIr_npqCSdz5xLEyRKpJpnEzZVYQ9PSPJ36RZ2WY0fCdHm5BP9pRWNWl6QoVQBEsvLXzQsEAnPLfSNP57NxMiw6ZFq1D8uJcqAh8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برخی از حواشی مثبت هیجده و جنجالی رقابت های جام جهانی 2026 آمریکا از زبان ابوطالب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23443" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngUpxwNHKu4Nv4WMOupRPVYJsEcZkPeq3I2j6y73RbIluXhWWpzpoRQhcRegSLujR7ALgdA1AgWLurlqeFvFhQuqQ86vum-JvtWQn74ocytNZsMvuuXYIwMUeJgzSquue6HgL1v0Lx85WtjCKqhABpZiEVx7qI_zYACiWoNXY_BH9NuQFrxLvzW2bUqWuHm6rXRJxwXXji5VPbCp-rDcBhmA7oYKSqNoO3HgC6M6mRPowbVCk61GzEWsey5ADODUQPHrgq6pOJ2H8ARX3xRs9S906DnJNpoAkax5qF2-Sb4X-yDVBav512p-Uu4ynj2YjGEE2_rHNAz2tAqcEL8NEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
صندوق‌سرمایه‌گذاری قطر اعلام‌کرده که بوعلام خوخی پس‌از گلزنی‌مقابل سوئیس در جام جهانی 3 میلیون‌دلار و جدیدترین‌رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23442" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SduDmkcg0ETonGIE3gJ6n_r3v7rVizqekA2eksh_FpZI2VHO7pT5tkfN_OVx_uJuAFV4XAuHgPQ58JNiv5eaounzAh79D-o7Q16NCWI2DyWoIjTkJEvhy9x7yeGAQyjniWJFsvPBxAb3UYfXkpwoT18FyzMDDxe6Q2Xmg0PCeQwnO50CLcmnx6Yo17SfKQiyShioiIRDwqcncsrsbMpthjoi-jMLqyA-nkUuneDL06tDeeK4JD8H1o_kRsulL8uDYysPT-vUsxKxp-b4lgnML8TH06XGf62cBvPuzFIgwOdFrYe856PZ35FK27wuh3HOJ1jfAZzU8xlMtC0gYQyqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی قطر
🆚
سوئیس در هفته نخست رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23441" target="_blank">📅 16:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IotnsxGwxF-2UpT0TvVPejhjo_TIOzQ2NBs05EwoXZecknQL8GM7vDwAfB68kFU6UKPWlER6KiU2yZyMzpGpyXmeWI4h5rd9ohIFU62U0M_BQArt3CKl0XORYvz_mu6ffrqPLpj9_Z0mYoWk9s8lyDCJRnfLML3Vn0raLbWOH1TaY9KO4gprn3S0qEi4mzs0OCRfRIIe1z1eXdHxlpCjKdb_gCdo7GtyHUEhElB2EecWwi6LUBK47TQ467baxyNQ7L-rvoADgpcse5Gnjc9KdMbzQ50qp0PUJEuCZJMvGJYxQDJf5zzPudIWEIAQLwoK46EDTSb2on5bb9UDkhVhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شبکه‌های‌رایگان‌که‌مسابقات لیگ ملت‌های والیبال رو باکیفیت‌بسیار بالا پخش میکنند. امروز حدود یک ساعت دیگ تیم ایران مقابل بلژیک بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23440" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7jbQC3gr5qMIpjrLigEcgj2wI7XWNMKVDV3oOeS5Kx071aNaobWBIBUc4_9tUrOk3FSwkA6S-G4j2BM07teUIrFQEtYh2acgnYiTO5G9OLOfBtiLF1Do5icFII0kqGK2OdOKo3yawyNLrtqH6PE5PYTEb7PkcIx-hIayYRafVS1S85gLG3SSqKSn44a_Vvl36lQpNj9DjGmcDpCymQZdE2ggxa1jyoVSiH3dQHNVrwhkzuBJwL-fVQQYD_FUxVloLCAitRkevfZV24VAPaAKgyIF3q0qFjMcmHsDEWCpSEQRRdGvR4g4BOo0aKHDLK9h_I0trY-M7KRVBT3kW9ukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23439" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvPLYILdOmTrpQxFbHvqj2o6rADFZj1XPwNFom2GOHMRs_NpXF2DS12jXppNdg6RTcHWHKf-_AdqXim_DCfuKZmMwE1_vOgGtE9LHqSmYyNjoFej4fSMuWPhULusu_1I9d79J3SCBSSjxuEA6FWhNKXP9xy73Z9oZr57LaRv3aR7pqsolDUjGi3folN61sDEZcaG1w9xloZ-eYNSppvhHT3kBQgjleKlMu-v3u4KfuCGymqt87MKbKo6AwpvVxzyzdiuYzYnhDLwFxobw-fMaTkD1yQGXH4HVGUOyoFX-hGgQZheB_cQz93SMPXgyx6BbgVlktfuMNIUKOjaxJVh4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23438" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">▶️
قسمت‌‌‌سوم‌ویژه‌برنامه‌‌فان‌ جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید. شیت و محمد نصرتی مهمونای این قسمت بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23437" target="_blank">📅 14:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23436" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=LGKqdKWsc4ifhqDBghZijzkALJBvN-zVPs26ri2hYvse2KGydj_8_kXFqxdBi-tTgz7B0a_1IxPw8YsY6phbVdaIbIYE7OzDrSiVDQUyfXryuU5bPoxjDz_fRbFRfQsb5VytR32vYqISVNfUcClsDCBmxiaO4Nh0vtLQEH_RKdwXAayE_2Fj0NNcrl8gmUpsIFlNPPvxZJ41EvkDpmcS-c3FsaT9JQK7Y3vvJnG_y9y7byzGlZtuXggjbxC9vhnU90c7P0M30fumWHgP5ErF2KTdehXUzBb76kv3AJyzqF0LgYJW657Lcz-RDc1PulXa_WqwWLHpVwrmtOihOmRQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=LGKqdKWsc4ifhqDBghZijzkALJBvN-zVPs26ri2hYvse2KGydj_8_kXFqxdBi-tTgz7B0a_1IxPw8YsY6phbVdaIbIYE7OzDrSiVDQUyfXryuU5bPoxjDz_fRbFRfQsb5VytR32vYqISVNfUcClsDCBmxiaO4Nh0vtLQEH_RKdwXAayE_2Fj0NNcrl8gmUpsIFlNPPvxZJ41EvkDpmcS-c3FsaT9JQK7Y3vvJnG_y9y7byzGlZtuXggjbxC9vhnU90c7P0M30fumWHgP5ErF2KTdehXUzBb76kv3AJyzqF0LgYJW657Lcz-RDc1PulXa_WqwWLHpVwrmtOihOmRQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23435" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s50BuxGp4rfeC3Fn8LDPMguN2ORdM0jnFWXxmbDhHuOIOMq86_Oek7Xlbr_zv5QBOseiW8DxNj24Onn9Q6o3qfHA7RbM7bXoXTWg-fMAw7DV-wAKzPSZHac3EcgQXaqoG-oF9u6QLL-CStKsiwFDSvh8KMMKZw6qscFhuMbDCt0EzsEPquISBMQof2nB0HlXInjkvl7GElJ4hmqLRMGNz-JGD3ZKwl6p6nX0XdSRgSm_HOWUjpgYRXcEmS2UpkRjL8UIiAusHh6RRltggndBU2KxvsAIOdJO8yGfMwIl_rxalYJ3JpBXmreJ9YCL7CHkBxI-BpYUGK8ZH9NlZaMElg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
با اعلام فابریزیو رومانو؛ سران باشگاه آث میلان مذاکرات‌رسمی‌خود را با روبن‌آموریم سرمربی پرتغالی سابق منچستریونایتد آغاز کرده تا درصورت توافق نهایی بااین‌سرمربی جوان قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23434" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23433" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23432" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWXhcqY2cJxhTiG9GIM8v1PEKlGx9TV_eqNHq84czLKCg_3ccuWvUaI21CND3SkaR_9kb8Zm7lKYfCFy5D4l6QTo7eo7q8S2DRGllmJhca_AFwSNcQ8MWTqU14MN0x2nH3pG_iqlinruyjXY-8mScxk4hWiTg_7LH5DU_uGw9AodxUg371pJk6Om-iMoPbbuNFJB8m1pVm6nGnIg4xuvQ9CbNdDBmfpTVg1xrcl_SH5C8TSvx6inVxdlnF5V3z_Yd9cF9GVwt4EBNA3hRMh8C4hnCWtifxtfQpMITihoX56JeeeFYMrzbqsUtgU3lvOiyeNCobpd3oXJ7_M2m2jlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
حرکت‌ جالب‌ و زیبای فیفا برای جام جهانی؛
تیم‌هاییکه‌سابقه قهرمانی در جام جهانی دارن، لوگوی طلایی روی لباسشون‌دارن و تیم‌هایی‌که هنوز قهرمان نشدن با لوگوی ساده وارد زمین مسابقه میشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23431" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7UkHxADMNrEO-1S6oQV5_TjNmJzEnbK5VCMxxRTJwbDu2FwzS_U06nwWqp62sHPHpevbtyuacST-iwXfaFUCgJcktGzXS2i2reGjwvESHVwAAbuT7_Yjssq3AqU4BGuBd1-ay27Gge5f5cjYRHRfQ2lDAtIPk8SZRP6kdzV0RgNH-eCo04X5_K6F5Jw9L3UTTu70rI3NTQUtR0SYX6KOCeIMz82przFGEtiYt5F9r9yOQHQxYLAea1RUZ4U2tF0_mntwaTSycYwoA98OwHZPXUVlnnIQG-caoH2JUYXFdR5FPoBWvl9_r-uI4glf0_nYCo5puRqWpkQ2vGLdNKGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23430" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=HCStLaN9QlTWbM6D7Yy43XbKEiXTadRn1yPvAjuKuKwHi23rU16KtS1arNjX7zSLW-aH-KuwSNTelqhNyQqCPO_UPhPreFsoleZ9PMPlL1hGPNW1E7pRB69GG6uz_yzrB9LEA4W5xGgB3puTAoCuz85nf3HqLd1K_tAezIWqEDDeyM2VkdQlhvlXXVD2FRK4_hIMxDJXBVYh_J8j8BegWdtCCP3UoB_pdxdnLa_fAuDsdqpZxzz5-UVprsshf3goqRVSdsKrSe0rsWwtv2kgzrZfjK_zXTxlbf3-wwLTVUb7AT131_nMJYMXl1lF6FeauxgMwNzHydN-ZbmKVvKgFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=HCStLaN9QlTWbM6D7Yy43XbKEiXTadRn1yPvAjuKuKwHi23rU16KtS1arNjX7zSLW-aH-KuwSNTelqhNyQqCPO_UPhPreFsoleZ9PMPlL1hGPNW1E7pRB69GG6uz_yzrB9LEA4W5xGgB3puTAoCuz85nf3HqLd1K_tAezIWqEDDeyM2VkdQlhvlXXVD2FRK4_hIMxDJXBVYh_J8j8BegWdtCCP3UoB_pdxdnLa_fAuDsdqpZxzz5-UVprsshf3goqRVSdsKrSe0rsWwtv2kgzrZfjK_zXTxlbf3-wwLTVUb7AT131_nMJYMXl1lF6FeauxgMwNzHydN-ZbmKVvKgFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های‌ابوطالب‌و‌قیاسی؛یک رولکس که قلعه نوعی بهش وصل‌شده؛ عروس‌دامادها میتونن با پول این شجاع خلیل زاده رو یک فصل داشته باشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23429" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCXHMVp0HYVbcaw_yc5w4_0rV7M1Av0jO6sniFcmmwHXAgSL_u43rESsoE6O6-VlSJyDTrYusBSwdkgyFUNny9qXN6Id3MgI_mLH3eNwxhjN53yVhYwHl43zuCaWn7Pd-dczHLyBuDO3F8ALp14-viTcqwDUqDTMAk1vY2psLtyZLg4_UvT4IPdx06DiSyb1zY2QtFZkkblruPMVglzuvWA2rj_Q8K4AQNDHAAaqywLl_ayTrJu49n8bsjzvedyg130QvRHi46NJSvO4fBjy3LdmKWZzz6OOOV2Qn30s7nekWEB2oTPO4yxDmcpIjWsIXMoQZt32cXiwbOB7GK6sNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23428" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkOE2weGcna29Za4v5KbO-zLL4Abw63dLAwvfwRN7c2G2AxEALKZMIE06MGrgsTRrE102OMYVJRLod690tfuLLsDil3D6nNFH3jmcSygVvSWOb0HiN24LsKMk1g4BlCOtVMCDHDpC9sl89bZK9cu5PAMlGGaXrSn_HWUsfKNl5JbkdBWBT36bGIjRQzY5gAGr5qxVpG7rs5zQ6Toif4dz8vDD43QFJv45ecby8M6gqjwRRUWVyV4mU-JksKKVCB6yB7CylFhOhX3rd8xpNfQ6yjGL_Wt-Jnd1rb48Wv1I3PIALyxghZ3w6_LiX13ituPKj_Wl65lzwANs5MIoRLUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇺
سرمربی‌تیم‌ملی‌استرالیا در حالی تو ترکیب تیمش مقابل‌ترکیه ۶ بازیکن با ۲۳ سال سن یا کمتر به زمین فرستاده‌که‌سرمربی‌ایران در لیست ۲۶ نفره‌اش فقط به ۲ بازیکن از این رنج سنی اعتماد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23427" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTV2L_sRQUCFiCiRUKYxdAAwcKtBQTflPFDqCrN6obYyF1Llv2TkO7CfeZZIboUC9MhPbfsQFdKyXnqd8DR97OF8jlHZYFOhJ-NudeWWMomTjU7-0mup_oDbZ1CfY8H0QQVKHSmSS-gkTQcqV87ZLwmENvRzMTXRhMgG9tJDaqVf6EA2n-JMRumCnohtRSMC09adpc8cFo5H8LwZtQWLocBOSAuMu3TVIGJu_pocT_TyySRaVyFbisR2jAmEiL4cB1ej8hZzz12Q2rQQAYiy8_Q5R_26P9GdxUBQaUu6G8Ip3aCoOc1-xuRYFm5kC6tIfbV5qguvUGEwPePgprm7zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23426" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clHIr8R4pQ59vOQY17W7FyBLUUTSaYzrgYsL8bW8qPl1IOphtusNp81tGKiyvNKJdIvVgGZW0I2wTdT8SElLln94ZdAYum_dFpiUzxorvql6ct3QxB-i8Iv2xEyPshFTtxl6URrO-fh6AwAKLq4xFUfjT2eTK1hPQe8eP9wCIiUDZxGTuhZOgUezqsn2AFE4CtLnq6Kw2Cl0nPh5VkhWCuHaBzwp-i5Zmjsyi9wtdKCoRrrkJWDhiQscBFcLrhGDXH9ykwyH_OJMyU4k9e_FRmxGx8n0d0T_dOSXU92YE_LBmiCr3uvCbMbQ1WTthGCe0T7QiALxr5g5obzdn-dy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
⚫️
#تکمیلی؛ روبرتو مانچینی طلب 15 میلیون یورویی‌اش از السد قطر روبخشید و رسما قراردادش رو با این باشگاه فسخ کرد تا ایتالیا رو در یورو آینده به جایگاه‌اصلی‌اش برسونه. مانچینی در یورو 2020 ایتالیا به قهرمانی تاریخی این رقابت ها رسونده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23425" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_RzQKtCaN7-i7o_8W9r8uVIjyJP9_l0ktWVdA8N2LQCTeVhNMGW8u8vaPg4-jMxbY5f3Pa7DDdaf3aD-J04AoH1Wm4NtsGcRYA-Wkty2Czl3Anji3BiUsqIDY_ptm2g0J54SVPb_duvDQc-aDQfpADDPDbqrqxACHWO26oYvbJn4i_Dfrg8dWuGk37SW-elfzo7jDArgHXiwNF9QnHCbyYwjMY-bEFDHD2f95qVl8IRIULIKC1Yfpn4EhGnu0P-0s5rFJ6bVvXh5C5fjdZPeIrpoqipsf-P-dHKQ-pbKxw6yXGaPUj1b23uqYTgCk-T7MLGlYK2_xcke74QLtGyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23424" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lNbCEZ3LVmxxt7ljj9SgUbi82DMy9j0j30i9T_-UE1lBogq77uxZuve049nWVVucXgiOlbartkRVT3ZB850wHDQBeSAvt7V9G26UEOEi032V9chHIfFiVfETW0fDgqnNbrM31HOOA6W9ErYNFSISwVqjjTAg8Vt5hgvnng95iMZ34VzuFXPxYpvY2pDvJajk7DNVil14GaqJzdUTkwymcpm1E9_JhlIL0D84gk60ROjj5TiVAqJZCKpoY6h7iFUA4i0GQoGIpcBHYk_bN2ZAnHFzrnlpkpc8LX6WweSATDQTmxpobuYC6Ngx3dSB08KZ6jeLKwCS8O3EDOGXjxLc3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23423" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu9oIdEmqv8D4X5K_8fykl8ivqrd_2Gv63z1SqhbxlDaWP-cfTqjtyr99Yu_BzQKwYeSga8NJ_XMCMkyP_BdyDVxyBZ5w_susB_iquiJoKvCh4s0PhXerFXm9qpvE1_Vy3Nb8kGWNSB8EDfm144sAFmhfTxdvoyY4-WasBSitflyhrklX_pTIG97MVIVb94jqtezTmBONZvTnGLNFtmQajq-Xu9Nk-LbwpZ-lTJTYLJeeScGUzg8lHjrb8NFDg0V4Ch8j2_gSQ3pgijxtrX5E3sz9D66HEW9_sZTaR3koLvjYhWoDrsPMApD3uiabRIkm3XwNw0XLdP7vw_V6NgHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23422" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1CG3rMo_nJXc6jGq1V0v5ued2d7Un56mUindxy6dCT3r7bRIoQnugSTpgItvmw1xSC5zQPJCv9VRzvekwLzoDaz_v-f1RKa3ndUgncvKXnBhOtQs8WqoKdSX2__i-r-IdVLKE8CQMz_rhKtCx__LNHNzxrK81uDBfq9j1CoQyyOjZoS69icrRtdvE0T0FqH6YX6nXhdZaaTF2SYq-aggNN7pcK-SsnXPhCzO4XALTpr0BUkWt_bbP1k6lWCwifSJGBas7oK0RUP7UcA_8y5k6OBd41V6mU0o_B3LkVjzATune55Y6iZsS8xN28CPo04pwWaQZ4kf_6paFCv_cQz2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C و D رقابت های جام جهانی در پایان هفته نخست؛ استرالیا قاطع و دو هیچ ترکیه رو شکست داد. اسکاتلند هائیتی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23421" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uT_8YkYOD6n2vG3UyKTvGP8Otp4bm78lfmticIqYPkKdsj7vBN6PcBx07PfeFFQAjhDcLEoT21jh6x_IPf50MQ8CG6MthQf63Km4C0mhkcnidWbLYcaVlP9I_kw3Pt4HRBEeeAH79esrDPPPX9PVqo_TlRf848YsG8oraKpadpcZxYDsnEjfcLABovW3iNVrxN-LDASCe8frTjEHgXhF1Di5m5odLmDF8hBD0494mTCijXMH4tyEJoP3KyxVrzNsqgucj70aAqWHxQ8APvtr6tC44rE49YwopKf26B4B4xPsqsrgTblcUc90Mfnr5bvpz2SHUtlL3AyJvrfhgyi_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5GmPLUlkIGaeaZFCsAXiZjUupKVdk7rH8lyKaWcgS0igvr_WMLyYpx08laFLlDq4bWOBk3I2UznU8oiPTcT3oBcWQttUeZfwsug6fVC7-2lL-tDD7_vQyfIeIy_TwEzdcs2P0MO61XQXB81x-WLMwGyQRw8x2fiaOTzNFbwfdS1QoKQ5gVle0iYtcwqajFMHGGIj4GKXJQOVHlZgYEBXPe4Kteof-LXOughcwYxSZ9vgftVtnLdiUvulcpW4qWVgJnMCwHhFUyqTa4BRG0d_Lg2jHIqkQAQOmskxKsbL0HMdpU9AtVDOsh_V-pacYmPRSrlim5WxSeQipWHnTVIOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی کاپیتان مراکش: اعتراف میکنم که در نیمه‌اول روی اون‌صحنه باید اخراج میشدم که شانس بامن‌یاربود و داور ندید. لیاقت‌پیروزی در این بازی رو داشتیم. هیچ موقعیتی به حریف ندادیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23419" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj-OeGqXMHpC2c_Z40EWo_GMcTELQsZ6n_qeing8YiT6F3nIHomrRZf8MoVBQtKpzL2VwtLwfhJcr2wT_UcufbNRYqaBDuUlynMCTdle5Z3SLncY-noty3vV0Z0B3SbJSQ8a-IHJSv0xXtpTSV6fsMVZvm7avRMIvQo7Cxfo-5vfsUqw62tdSXlKTfziJ_dTLw18sIZ3efwDlf19_MEygso-VBNIUCZTcqXBVKZ8NW9tgIEyDJnzOmZo_z1FA9O1mp2jc1h-U6yYBYqy4xaXpy-T8p_ElbiCuhaqP71g02Qr7KCb2xh4EuMuM4XfLyKVsZcjl8BFO_bKalP9PrNRqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23417" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzrWZapGgVTeG2i38BM336eVnylHltWnOLjS40MfXZ9Zp551XY5Cf6ebgr7DABFCcCmY2qle908eRZinpQdv8fvvdpbejH_iXbnLEXnaoz96R__NdZGQPK0xtA3a4_9AFlYtNZG3vZ5F68D6ENSedE9zqkLnN-88KhAxS6YWcOkpvoaY1MDr8FV-EBp7b3v5IypDtiQoiHFSf0IVcbciu-tvvyEmwy013eRIXyTdn_JYYBnmN8i8gdFHlF7gJqDi5NCe5Ks--SUTJlwDmYP3BUNHVmjZFgh-5u6zrp-AwRUlt_0EHzJBztGDpAgsDhUO-csLMkLlwqKXFdJRbGuE5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ازکهکشان‌اومد زمین بی‌بال پرواز؛ مثل شهاب از اسمون اومد با یه راز؛ خرید اونو قصه‌مون شد آغاز، امیر10؛ ابر قهرمان جدید ایران و جهان
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23416" target="_blank">📅 09:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=r9Rm5X44ZrQo5twl2bQlrNJIqQ5_qubExXdCnA8qsWiISp_n89TquAuWPUNogEVz6vy2WZ0zbOb7tDfObsLdnlAEgd4PUz-VJGb-6CjcpNg4DDmcsFwlra8FOrGyj6pKVSx2rDPEQMC2K6FufBcDVxXxEHGMQoNnNxGbhHsxkWwihvCMCgia-G4GHYBx9m9YPp2HuyoH4z9hr_HCjcNKQVp5Cpa4P2RffCW4oUePYRbdMgv1E2Q1awt6ahZONILcLgUxszBhECFkuRseH9E_vLaR_XydxIDXew2aD5MX4SXrIaRFyt_rR9vh42DmepqIwYSnVOHrsL5OB1HnbKHsRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=r9Rm5X44ZrQo5twl2bQlrNJIqQ5_qubExXdCnA8qsWiISp_n89TquAuWPUNogEVz6vy2WZ0zbOb7tDfObsLdnlAEgd4PUz-VJGb-6CjcpNg4DDmcsFwlra8FOrGyj6pKVSx2rDPEQMC2K6FufBcDVxXxEHGMQoNnNxGbhHsxkWwihvCMCgia-G4GHYBx9m9YPp2HuyoH4z9hr_HCjcNKQVp5Cpa4P2RffCW4oUePYRbdMgv1E2Q1awt6ahZONILcLgUxszBhECFkuRseH9E_vLaR_XydxIDXew2aD5MX4SXrIaRFyt_rR9vh42DmepqIwYSnVOHrsL5OB1HnbKHsRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نگاه عجیب ویکتوریا همسر دیوید بکهام به تام کروز و حرکت عجیب‌ ترشون؛ درسته ما فرهنگمون خیلی متفاوته ولی‌همچین‌چیزایی دیگه مورد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23415" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu8CuAEr9R2VR0_jNEGOXxhVuukee36Z1MhSuFkQTF9YC_evmyUdpNsMqEJDUiT8adTeoH9X2QfnZX1yY-H0XO-Xf2L7oVqWzMtOmPqef91qGgMKWwu0EdKeCWy14nZTeZkxOOkVmdjLNBaTlPJmSYOUXucIcXkrRCKf9mRZgWk_w0ijRzGf9bO2EI1CaTxoI4vD4DSKa31PM8ubXeXOX0S_5OGkg5kxp7bS_bHTmBviVaa1pd_28QAmeEXWya3UfF8pgq_rO9a6Ji_Xz57nNWKYPSHRbBq5GYghixXCBIN9G9ITUVMswwdEh7-GzCdh0l9SQsxo4tJ0EauKSkEMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
درحاشیه‌تمرینات‌دیروز؛ بازیکن‌کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه‌نفر از کادرفنی این‌تیم اومد گوشیشو ازش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23414" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da531b194d.mp4?token=dlF1_yfaN9urSARhzXkG4h0DVU-A7nPFOOLH57CwTbGLiWEjWE_YpHcBGYJUTA-9aUrk8RlW-O62s5A6XRGcwpaSgZxDZuN9Yxxr1q8li-oJy2RjAyOG-0-HkRI0J351eJI_bkUFGnIchuTyriSieFfgR_819hzNb0bq-ECWcte39X4zrc3FQ40Dsz-PrjHl8Py5lz0PobdcOW3Te7MZ5zV2gp2TXlgNMvDxMSO_juOL4ebiZCZsMAOj6VgSNlO_Aa-O3AdOlmRzNsUhZ3trutsfqLaWmmzm13F7kVvD7Z3xoyhSGYalwA6E9J_zaErvIRJwS0DBM8NCucvEsM50hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da531b194d.mp4?token=dlF1_yfaN9urSARhzXkG4h0DVU-A7nPFOOLH57CwTbGLiWEjWE_YpHcBGYJUTA-9aUrk8RlW-O62s5A6XRGcwpaSgZxDZuN9Yxxr1q8li-oJy2RjAyOG-0-HkRI0J351eJI_bkUFGnIchuTyriSieFfgR_819hzNb0bq-ECWcte39X4zrc3FQ40Dsz-PrjHl8Py5lz0PobdcOW3Te7MZ5zV2gp2TXlgNMvDxMSO_juOL4ebiZCZsMAOj6VgSNlO_Aa-O3AdOlmRzNsUhZ3trutsfqLaWmmzm13F7kVvD7Z3xoyhSGYalwA6E9J_zaErvIRJwS0DBM8NCucvEsM50hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23413" target="_blank">📅 04:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5IXTXz5lPeUUeJ-_TrImqaoTJHqe0qLWzqBQXvY5xZ0tM6oyA4L9MDCYAvaWU0JRLkg4TFfIPZEdGJLLySfbGwQwVuJjqT03tZqrLf1qmmRcHVPDIY2UKhPJUz4FmIv-JVg7bkHjQ4CsOGuWwf943NJZ8gXaN1goAMU3seTsctw9mPPLTgmsbvQ2Z52MXTewu9qjxeQLXHbsvicsMYavYs8KBeGXH8n4LYs4xJISnKzI2BCiMobKLb6ecrNOLqSaDPHe2fI6IPECoTt6DmHPXSH6f1a_fgo-rumU7B3BPIRVT50_HmJIoDjGsICHJz8AbO2PpQbPVAPUFTzJMa9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23412" target="_blank">📅 03:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی برزیل - مراکش در هفته اول رقابت‌های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23411" target="_blank">📅 03:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23410" target="_blank">📅 03:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOnbZC0AxEGHvMjX4n50nx_HIxMY3ZaqymmogFTEbqlqj-qEEQPmNDccsp8SCBx9w19yDp8Ws7Fq6oV2dF6go3FvL90lnIwilmWUexhtSIT1VLU05Uf-oc2fTfv559a4XMF4310vnfTIKjU4Z5Xo8ITOfFgwCEWL-uXxVKypUr2WzoWRhMtjbFfg5FWd-vhtuoFufVThu_4RTYtRRoJ-pRXT_0YC4ZpPxsidHL5m4PeOBBZt0Dr7u6d74ry6jTTqKN3rfWCo3hKdDRd0wBa8w0FAqTNBx_uuSR-fAuY9AHp7f_moH8p32JaRJUxgjrxakE8h75sQTD1bGSFITrTjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23409" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=vv8QNDXEVKWsv2ceKXspWBHmErJ9r6c5XoofPJdakThG9otd4TsNW3e40tV4IuXtsgtDfxiI0h7TU58Q-reZMFb_vKva9_J2I4QtgDK7aEiKQ1Ic0UJPD1PlfFxKuJiI7tFJVjgj_1_nGSo2DXOratxGlGFPew4TBLTF9DPtW3ieXlsHlC3ghH4aZDF3-5yy8868ImkVTIgDtA5zYfbuDH9bKtz5TbiH8eZLqD4QjYYfG0Zc63N62C44F6Qd6jNCPxXQSwKbAZndj0hQN7htH6Q93by7wsm7u5t6OKB4-s5kx5WPzby4xPAICxMU-65Gp32ROyehrls8CCzaPK-HUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=vv8QNDXEVKWsv2ceKXspWBHmErJ9r6c5XoofPJdakThG9otd4TsNW3e40tV4IuXtsgtDfxiI0h7TU58Q-reZMFb_vKva9_J2I4QtgDK7aEiKQ1Ic0UJPD1PlfFxKuJiI7tFJVjgj_1_nGSo2DXOratxGlGFPew4TBLTF9DPtW3ieXlsHlC3ghH4aZDF3-5yy8868ImkVTIgDtA5zYfbuDH9bKtz5TbiH8eZLqD4QjYYfG0Zc63N62C44F6Qd6jNCPxXQSwKbAZndj0hQN7htH6Q93by7wsm7u5t6OKB4-s5kx5WPzby4xPAICxMU-65Gp32ROyehrls8CCzaPK-HUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrZ-WyagpXM97tNy9SHu_panafRccZcXJmefsDyoNpF2VnWQ5-xNNXW6HpEQjEW0ODnovsGmjhvxtAvZkIAZ4Duwp2pJyMYyA302V1s3GMQKyt5-vHMVD_fdyTOgqTDnW0SQM6e0xQ2m-QYvVe8zWlrj5EA2hDDVBYn5j4dp41x-22NsnVC1qljuB8ASwBHbWa1VUXN7UD3EItwq_AW4gwQllsWjVtnY7fV29kEl2MR4ExafPlkMIeaqL_S02Lb_Cpmfurgfqx7nGWDz1y1AJ882zTlPHnZt6OFzgCBVPL44h1FVAbfEftimDY7oIrIt5fb__PItLcWUCu72V33bLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw_Dqm49D2imCAOSB9_Fb0UgbPU0tw2moE2b7rIn7ed8rffK9GEIDEsmf8PFSh6zN9OEfhdolyXr7DUL1VWuspBsV2zesp5__XwScK19zZmrXTBCrdjaduGc-CrQ2ClkoQ2sWAX_DEkREfHrTa_HYYHUHLuvevILmb37svco5ltEAoDTN6bB7b6i_JIhlXWlLffVZsSlmeNUn-o5JHzO-bvdYTUUZMjXArdMjuIvTow_6YsVI8DIXLfLlLRilrK58Th3sI1q3I5Ts-6BolDBVCd_GzpZv_NRdSlnRv1aDdtO4bO1JuasQM1J39DKiNfR0ZG43MTdkDl3QDqAbwJgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az4n5yFPNQxJ-J0l5hrvojjd9xQ4qxeIIF_Q89haACNYs4MkCGIzk4vwKDM627YNFcisg0a1wFVGFmtRAi0axVF5nQZSg5L9tYaXN7Bv6ANRXYkQxTwLn0nwBmF9xL02SFxHQTaUC5AaJU2alBBkUGvRhqqCQzAwibJ1xf0qYlR6oQzgto17GoET5mJ5qkmv6aVJSJctTgcLVflmdZfSWxGmlCSSMV-xwtA9S-2oC2_Is-flfC6rALFLXCEvW6noM1xTToq1YLYQbKcYmKTZgNJzCZzPKAjuTsGd2OyRrpNaoLu_Mx8732Oy7663hQJ7uMo1bMoND_ry6PcmOahQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=S2KtEtxCKLmqJnELMS4nqx4Rm4Jl3N4L2-3URQyM7_vbLakloTdnjhmQLz9LVn3BtHgORDIKvd_z8jiSJdwB92M56-7AKZfP91fTbyNGvP8R90A2KEz6gX5zzLNywpiR4jn1NRLkIiS1xhUy0url1pmMRDX0Y1VuY2k2otLqqehhTJYevZdw5d_-gW4dh-AXZXHRwUVgHmtKG6Z9Yn_ZHbBbjUdG6PlAop6p4JxebQYjuICZ9EvcCV-tSL472ZXqWWcHDxPJPgIosBdYDlZV5rj7Lq_nqQFPFLY0HGbkrtLs5XjO0NYrjCLY0w9HVkNLA5TidcOIhkP3s1dl054SPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=S2KtEtxCKLmqJnELMS4nqx4Rm4Jl3N4L2-3URQyM7_vbLakloTdnjhmQLz9LVn3BtHgORDIKvd_z8jiSJdwB92M56-7AKZfP91fTbyNGvP8R90A2KEz6gX5zzLNywpiR4jn1NRLkIiS1xhUy0url1pmMRDX0Y1VuY2k2otLqqehhTJYevZdw5d_-gW4dh-AXZXHRwUVgHmtKG6Z9Yn_ZHbBbjUdG6PlAop6p4JxebQYjuICZ9EvcCV-tSL472ZXqWWcHDxPJPgIosBdYDlZV5rj7Lq_nqQFPFLY0HGbkrtLs5XjO0NYrjCLY0w9HVkNLA5TidcOIhkP3s1dl054SPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te09TlAqsGIjx2yBb-DSthBqymo6XH5Bc5VISGRI7goBQB7o80e8nRpT-74ZhdLYDyDPaQROC0ueRz0iMItssmf_KGk9-h_fqJWA5HVyh2SN0R_Y4dF4boqj2umF3PqiZ_zmiuVnks5ps-FEWG9OA9tNY7H-WxM-tHYOk_tbHpNbaUl2K8VaLzoj7QOidEt-etJF19AfHyHEM_2Qhe3KzSf2OI6Lkc1KDT1SgEwU8j0n_mUSU_BK9ZFy8_GoLm8wQu7avBLKfcYptIE540bofgiJEkEGILYPOvfUH0fxZlEIr_zvcQBg3fBUnAdUk5tzxR-dRSHpbCZy_9LtDm-UKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=j41GqhdAnsrw1JU6GH6zxw1D7DJauGC57Be4PPlVWV8uMQhUFnTHlys5NTzh4jcJR3K49y7ray8jr6Ccwr-UA5z-z_2HLcEZQBlOKcv2l12OMSDoEfI7KGGQwx9-05mjVQl27nIXUnxFFCPdCW-S6TJO_Hhf_KDPgzazwO78CKvGqzNmOXN5YNWKKyNhg60z5qrnCSkgvXe18bapinnu4J3QlzqM3HefL2TRceinvZeNzCcTb6C9OhAtxGQ1_e23xthLQnSeW784Rb54KhJlg38MvzgrIpxGxeTVZGPuPuLWs0FD1NqjeRkitQjCdeYcMwqCx22mQ4tXrNKbjopcWJPkoB_tVuDxFeWUAOq5lx4Qs4ziacFH5c6D0lw0hnVAxAmQXXRLfqL5XNkmXPoZVuNW24dcC_7-SZb3ar-y91BRKFD9HdMSaCkrBXvDnNB5ZEwC6twYuVW1_0eu3XXaRg_1T_JqYnJ4e4V9WH0EhdPM4EeyDFu80KdJziEh9_0Uv6g4F6jP9b3doBwtGW7MzJpGW0FJ9ciql9qwD9q3sSgu5L6qxU547-dNkNhPFUgBPcbFiSAzJ6fo5FXoPFtQA3AqcZeLT1l9jR3da2k_A2ruOg3QDWL7yiEfQJO_wqAWuI1qfl7fc9_kWAb5e1z6HuSd-XLPIkim6kK4TA0mg9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=j41GqhdAnsrw1JU6GH6zxw1D7DJauGC57Be4PPlVWV8uMQhUFnTHlys5NTzh4jcJR3K49y7ray8jr6Ccwr-UA5z-z_2HLcEZQBlOKcv2l12OMSDoEfI7KGGQwx9-05mjVQl27nIXUnxFFCPdCW-S6TJO_Hhf_KDPgzazwO78CKvGqzNmOXN5YNWKKyNhg60z5qrnCSkgvXe18bapinnu4J3QlzqM3HefL2TRceinvZeNzCcTb6C9OhAtxGQ1_e23xthLQnSeW784Rb54KhJlg38MvzgrIpxGxeTVZGPuPuLWs0FD1NqjeRkitQjCdeYcMwqCx22mQ4tXrNKbjopcWJPkoB_tVuDxFeWUAOq5lx4Qs4ziacFH5c6D0lw0hnVAxAmQXXRLfqL5XNkmXPoZVuNW24dcC_7-SZb3ar-y91BRKFD9HdMSaCkrBXvDnNB5ZEwC6twYuVW1_0eu3XXaRg_1T_JqYnJ4e4V9WH0EhdPM4EeyDFu80KdJziEh9_0Uv6g4F6jP9b3doBwtGW7MzJpGW0FJ9ciql9qwD9q3sSgu5L6qxU547-dNkNhPFUgBPcbFiSAzJ6fo5FXoPFtQA3AqcZeLT1l9jR3da2k_A2ruOg3QDWL7yiEfQJO_wqAWuI1qfl7fc9_kWAb5e1z6HuSd-XLPIkim6kK4TA0mg9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=aoVB9th_EzTzuORLaOro99ZzVGeaHPqdbGmtwpUeu8jNTURqs5bmFu0pOldZqoAG6Aow12v5gBs6db5Z2b91aJRLs4d1-i8JtyPvwVXF4J9MNriod69B6caFpNqH7coH1Ta89lKbYss3JHnOlAszIacWvq7rH5tynyXAfazuBvNiFqUxJQcM1KA8WTDv35-9TN9xxS9Ju9HcZfTXwgWniZztn7-MiH5fUSEgya17JlawVCLS6tz3MBFAhTTPhNLBCCyIzkOHmB3w8cBUvWsVtutOxRJgY2FzQwg-Un4i1W3zviGFhoicvSvX660PlfVtnua-JYBuk_7cWcjrcwfx_hQLS260mdZmfmU8MkElUoOM5NUykIVpBXFfFY_LZaCDUBtOjZXRsZy6GmPsl5nwD4TlprI6disBYnRADWT0CV8-Zv_LSCnrQsUYu3LpujHpmz1xR92BVCkUQhRgKzxwj4tii_6T_kt2HiiEjxbxqBFaZpI4A65vpPxCW6NLsAD0pDV5k-aVmUmKmNE9_bX6LqymU8G0-mAqic5l7f3C-CvSl23xZyjo6NCijzYa-5X7VHCOPcuZDSstIOAv1IYeWMdLOy2DF9dGc7gLskph-bf3BN7CzAdNqR9hZ5pT2DC_018rQMSNelGiEp2kImI2ypjUptIewm04pDadOHicxs4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=aoVB9th_EzTzuORLaOro99ZzVGeaHPqdbGmtwpUeu8jNTURqs5bmFu0pOldZqoAG6Aow12v5gBs6db5Z2b91aJRLs4d1-i8JtyPvwVXF4J9MNriod69B6caFpNqH7coH1Ta89lKbYss3JHnOlAszIacWvq7rH5tynyXAfazuBvNiFqUxJQcM1KA8WTDv35-9TN9xxS9Ju9HcZfTXwgWniZztn7-MiH5fUSEgya17JlawVCLS6tz3MBFAhTTPhNLBCCyIzkOHmB3w8cBUvWsVtutOxRJgY2FzQwg-Un4i1W3zviGFhoicvSvX660PlfVtnua-JYBuk_7cWcjrcwfx_hQLS260mdZmfmU8MkElUoOM5NUykIVpBXFfFY_LZaCDUBtOjZXRsZy6GmPsl5nwD4TlprI6disBYnRADWT0CV8-Zv_LSCnrQsUYu3LpujHpmz1xR92BVCkUQhRgKzxwj4tii_6T_kt2HiiEjxbxqBFaZpI4A65vpPxCW6NLsAD0pDV5k-aVmUmKmNE9_bX6LqymU8G0-mAqic5l7f3C-CvSl23xZyjo6NCijzYa-5X7VHCOPcuZDSstIOAv1IYeWMdLOy2DF9dGc7gLskph-bf3BN7CzAdNqR9hZ5pT2DC_018rQMSNelGiEp2kImI2ypjUptIewm04pDadOHicxs4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMS2bTFQtfXKgKvelluauGuK5Fyy-noY1scA8n-JuECPYmfHFsu_5E92l9fTZQdFlvCX5jRTrQMxbs5sQXJ7rWzC99lc62IuYLluk7dZcqS69mvnrq9r-f1PDrYtksJLYAbHge22_y43NE12oiMqzkhs9EjxRBYzkOeGs56YDSmuS74OfYKOTl58HJK27oo16zI95eioRHKUJDJljBIsx7g8ab5aW4jJRAnkZPfvVaJm7Hwi_6JiJ8RYude1p2xD8YOTQym_XgoZIzJMThLrjspOLRXWzJ56FvHLwJ7yJ34rmnRL4fKbluuA155YwBHWikt36MGsk1M-uSzsDwx2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfakli8Z3LpfiKzCv3z-lIyklBWKhmC-nnIveQXUYIfOY9fuDAb3ogol6p4LjkauSLx3e9n09DVBPvEzHl9WsjeqxfbMIU8xrnBmciPpbhnMTcGysZ2vrH66xLYl4GXJomnvytpY21QpU7xPFofsoO15hT2hoBES0sDKgoe0XIaI53zMjGjC6r0iRMQKdwgcHl5lncu1nyXWsFN0cWOte8JkLcvr2_y1PRdXUFFI5uctu1dpGDWIRE5YfkvO6SAlnhPli2xvihfMpsk-3gtBsiFmGJzU_3hFhsTd9BiKriSxyXRhyfCzZvUTTjdH_UIfmVghT7vByd-8tGu38VMKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGZwEFIm_nj0Rkc0y2Wk2jDGZ7BdSYCmxLe2T5kAOwa00lsu_HkrjNoDkL_FC-pRcFVAMpQMpYWvxiZ-hP6X7rD_m0ZvXjaGdCd6r17bk6RTLhJesifJZyoPrwymtJmownqpnJRLOBCNwmZ1iYqPpUUqAYUwc-W8V345gPSJk-GN7Zs3Tf1Soooz5xG2X_akSKudV4pFyt80Co4o2HKWUEkvvbG_8_z6STUvz4h4yvUNZn7JuX19kyKk6bmhzvVAx-E3xMEH92Ncf-WYAKtvG0vi-DLsM4TduQj8KB8GsP37LBsklGxb3Jbz9fBpdvURsSag2r796MPsBYGq5RumFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FORmLxPEz_qQeK9_Auh4rvAzlJJQMg2koBZ22Jbkp4LDwFAKZD4K3ktarJSAhuEm4eipPcfOokIV-Avq68FC2c71j1DtHFWboXAXDze1lvfKVMV5P1ljtDSsIhm36VceojrNwe84R2p_SZeAIDj_li9JVFHX7IpJnnhKKlCaiLAi9HUM_J--Lk6k5FwsqZ9JxL963Bjn1kPnLFwxNWqJ5rBsByUrlZbnkC9IYaXT27VVVuW584Xlk3KyCiIQ4F4kkDMl5vVldVSbpCADC5qzoAastVSw6x2auzj5Z2XpJHDLBmtSvmkcrJAsaHhet_j6mkwPRUJKfBBFUIaYF0UIZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=KUqwrJWZxmM7UYOLx2no6SOIaBhQL-fyEGs5wWRVr5160T5fvpsUkJbbc9q-1KGKnRSwUy61VBJ3ljQeQtourxs0xZjZ3b_8GartjceEeRnNKiZdOgay1efq3Yd9NAZSaK7CbH2neNbx2EWQfA1CMgMbJCL3ssqqr0gs4Ii2Cvfm5Q75WhLbSJd2ADxsxR1cHY4U7JkgMxH9yl4zPSDjKxoYMUFBuZSsB4JbmCveBCWVW1hzf78L5U2mMRetg4rSLHsO0FrlEDAh-IPqbJDRejtvJ6ci1PywO-fzG5l_xicPxHLPT-QmxvpqMSejzwdx7t86nDfx7R6LfFQy0W6r8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=KUqwrJWZxmM7UYOLx2no6SOIaBhQL-fyEGs5wWRVr5160T5fvpsUkJbbc9q-1KGKnRSwUy61VBJ3ljQeQtourxs0xZjZ3b_8GartjceEeRnNKiZdOgay1efq3Yd9NAZSaK7CbH2neNbx2EWQfA1CMgMbJCL3ssqqr0gs4Ii2Cvfm5Q75WhLbSJd2ADxsxR1cHY4U7JkgMxH9yl4zPSDjKxoYMUFBuZSsB4JbmCveBCWVW1hzf78L5U2mMRetg4rSLHsO0FrlEDAh-IPqbJDRejtvJ6ci1PywO-fzG5l_xicPxHLPT-QmxvpqMSejzwdx7t86nDfx7R6LfFQy0W6r8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIMtxjW0hixwRhZTVR8zw_LGDB8jjYObSxgzdA08JDPLU-rRU_ZanGR0GyLm2fMQCvIivHVWA3zUFlomRfDcxrsxu8Jcm4H-c4IsKyumq5BrhNidfzaaw3nrlWTTwuJfbw6PfszSqR89_dpPTogmEp6j52YKv6e4V4ek3h0hgihKWM9MKIUPIqqKlWS2uPJyg9vP_aIA1Ji_4aknvlH4CSwc_VFbiogPh_BJBNWyaN1nTHOjhzEKYrIWsJoTzvYC25JK5J5-TS9wp-XbYMqa0jVmwLSWbpZH3WThYYwCP79iXt4jUbuaV-Y3v-JFCfNHyh9QJEmHcH1Ag3CRpvwFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgbrUvaf6oeOV_qsCKC0qRqxpkuCvrHXX3SyqPHC3tn3T--usZ8vV7WUOJ9ptX8MsGZdiXnMrCkuugUjxATnuV7gMroYaRMOX_jT_xNL9LiJ6Ghft7mfIngACo9Fo-CZ_1WOFtmMjMrMyK6xmkiRUd6piTqA-NkU48sHQXlODX8Sk3jZc1myKLhLWyV6Q910-qT4rllOTbJQumle3Qj9OGVhfxNAZDtJUpCma3nfMaXACUsvo53756uE4RWEq7_7mP_ZIQjIM2k5QdhD9kEjAi5jYLgReMxm0yTSDU24hSYePb8Lz0YnQAgGWwh74zquCwAMmhEHJXxOBhiy4cexQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goTinr5A-S_A42qka13fhMwV_34nFWhHpEtZaWJiJguU-QHZejANX2To3PCN5aiLn_nRYUM7Zg_3wmRlZv9GtbU-3RFdwvCpzygg11pkPO-2yDYj3ObqjBvwm0bQitNrAfOXSYgzhRNnQNHgaCQ5RPvNrm_l2WA8GyMqRPNIwtAP-aJdJwLrI64yuwvxbB2cdJsPhaVOWQGFkSVyO1EHtRw0jvTBDYko8VyIutmaPrIUUksn4zeNiyRNzQ3wLkZ2bhl_daDYh8R2sP6eSJagM-bjT06XTMiC9W8fYhbCrb15eqh4qbQdB6AVxdZzmV7IeV3YzQ11TlDlj6wld2HGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=YpzRYRTY7iouRhqeulpf-8n2Ga-JDM6JTiP1ST4Rh_6I37v_WEiu8iQljfdNONHDhscaley0v6bwWEWePT-NkI7ug897UBrddEHGARTbtn0VwtlA57iR538YtK7BSDnD1SGuXsAIBz-NgIlEEJoIPaeDhSvnn4DWP9oQNJSdeCZX7TMeRhpJtqGqr4UlCUC8L-MYHO7p8OelzCDaGd8Bw9LetIFBALmVz1uBVjbI5uq_xhKh5xtHhW-ixgI7IitJ-nd0maqzoZOdVUgA9M0yQxwvLq4IXnFjXxiK-t9zXINxG3ok23z9yRU_GXRUIUAHOi2r4IV10ODOIBfSpbQRrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=YpzRYRTY7iouRhqeulpf-8n2Ga-JDM6JTiP1ST4Rh_6I37v_WEiu8iQljfdNONHDhscaley0v6bwWEWePT-NkI7ug897UBrddEHGARTbtn0VwtlA57iR538YtK7BSDnD1SGuXsAIBz-NgIlEEJoIPaeDhSvnn4DWP9oQNJSdeCZX7TMeRhpJtqGqr4UlCUC8L-MYHO7p8OelzCDaGd8Bw9LetIFBALmVz1uBVjbI5uq_xhKh5xtHhW-ixgI7IitJ-nd0maqzoZOdVUgA9M0yQxwvLq4IXnFjXxiK-t9zXINxG3ok23z9yRU_GXRUIUAHOi2r4IV10ODOIBfSpbQRrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO-Gk3md8WBr2jJF65yRPcim1PKWsYhjoZz1ImvgFfY1CLvtN6GVDhXGpb-tTHieAQz_N684-OdiP40U_M91XBMjhOAruyeS2vKvNLWclm-gPySAHJjmlloESJe0pd7xKdzCckCIcIxeMIw0IASi3Mtjk78pHV5hJ3yoiW9bo2EUwnb-9m3Q76Qo3nNgAoPXJ6JgdAphbDJzOW6HairHUJs-HYWH8cqzW7aswoJ2J0ljYESMg5ORNJ6L5cdomtjrXecn63ODJqCpBveKEhVFQJxHRSN-d5Y0tT0fd920eKMrzyYwnnpD9IdSXMlHCVtDZvyrNW44iZ6ATEDLRIT-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=HSCCWkDPmo1gHWCrvuo9Y2i7OWBsNW6AFHrw3-YdCKdVTD1DNgI6KQCCoO9aJ0lMFGFtPAMAmpJAcOdvtPuQcUsxisUo6EOLiUtK5NflHYjaYeS6hIDnA0ugScS6VLQnxdZbL_aQsjkg9bU6dABAPWA440HOsgBOhx1A9ebhAWSZylUbLNkhfwXWXV28dYZAQyRBsPNj2lp25IxUhPc8r7WxNBHeGQNHrnDUngDswFEnmmPDNa9AgL96yvcE5JPghEhtj9fJtncF7VSztwC7005uc2Mk7pE_Fjk0fA1_SCxNaTThgPDDjHdADdQ1k-cD4OoYbazA1PabeqOLpBLXDZeTSolHmU3yiYpNJc4ojwB8iNkSN1p5ZZNmeI4FG9Ga_eh8KB8DzEgsuQpGkHjz-46BlkShn_rIaU0uwpJIaHbUrw4ZjbGKlJiIHhuUz_8sNtCLHKq__Kb8gBls_GiF1RTqhE3P1wREdKpQXBHM_LwL6W0L2C76tqn1Sg7e_2qIabbMxw_fPBI07S3P46QozF3kv5Kel0tYgNQZqOe1Ag6MTY9nLv1DqwnsztuWD2R1Ya3qtiu-f6tlneLbOIqDPo08nHK-2xLkTA4COoOaYPFXj96DLusProd4yH91rZngG1t5SKomBmrEeKimaFNXbn5oo7EsfyUf1t7pDsD0W48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=HSCCWkDPmo1gHWCrvuo9Y2i7OWBsNW6AFHrw3-YdCKdVTD1DNgI6KQCCoO9aJ0lMFGFtPAMAmpJAcOdvtPuQcUsxisUo6EOLiUtK5NflHYjaYeS6hIDnA0ugScS6VLQnxdZbL_aQsjkg9bU6dABAPWA440HOsgBOhx1A9ebhAWSZylUbLNkhfwXWXV28dYZAQyRBsPNj2lp25IxUhPc8r7WxNBHeGQNHrnDUngDswFEnmmPDNa9AgL96yvcE5JPghEhtj9fJtncF7VSztwC7005uc2Mk7pE_Fjk0fA1_SCxNaTThgPDDjHdADdQ1k-cD4OoYbazA1PabeqOLpBLXDZeTSolHmU3yiYpNJc4ojwB8iNkSN1p5ZZNmeI4FG9Ga_eh8KB8DzEgsuQpGkHjz-46BlkShn_rIaU0uwpJIaHbUrw4ZjbGKlJiIHhuUz_8sNtCLHKq__Kb8gBls_GiF1RTqhE3P1wREdKpQXBHM_LwL6W0L2C76tqn1Sg7e_2qIabbMxw_fPBI07S3P46QozF3kv5Kel0tYgNQZqOe1Ag6MTY9nLv1DqwnsztuWD2R1Ya3qtiu-f6tlneLbOIqDPo08nHK-2xLkTA4COoOaYPFXj96DLusProd4yH91rZngG1t5SKomBmrEeKimaFNXbn5oo7EsfyUf1t7pDsD0W48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuuszLIMYJzkBXXA5J23T305wZfnF53tOg_RIUS8rEOz4XpTgoaUtTuxd0wgxGY7Q1DvkYEFtt8x3YNjXwFUAJMbYe_R_MHH6BpGmYtSKr51EPvK93FJM2AGI8mi6ye3LEcATdYsMOdfxJs-5yJtvdm1_Qjz1RoaWidWCgnONviPNNnjgF6Is-8Hzb2MQmgV5LYcXjFpBbrgDhu9Pv4c5c514HMDBmn00-7d1h0D5SHcZHlr1PiHl8wQt-ERYFTtzsV0_376drQxCd1XE3XGD7n1FO6qUuvI-cpgdx5gLPdxYsLiFy7kO6HBaOHVAY3OUihkEPvJTNydnpgrKYBllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKcdpsCFKDQRJW1jJTsbxYJwsnJRPehjswsaNsS87fxAoOfwAxH8clOdk6_8B72UpRySeM5ex2mxMhr5hMoGTcMLGdVpCL6jcNJ3r0x84qQTAapClWGGb-VThUULPWJ9_XV3gYAul75FGcobieX21cNc8V3f3d4M0_7lIe56hbkkYATYgnIDZwyfzTP3-AOgnhDGHg7Qp6vxIxFfoXmXNUgkUw-4-7Mtxm263tvaF4YnhLgRXfxBFEl0ZyHpkbBcpdV5iViz1kK0IDQu5_ZgLm59ZT4oFUiekO28z4ljoNC-E3P-hHaxvh6P_W1THhW_yvHGWbKoAvm5VyI2TDN3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBEYX8RbOtcAYFgxtbaLUtVLb50B4bhqoe5YVOokRHq9fQJ0063KnYhrC0tdxI_EuKzdSL3Q7JT1SxmFhDUYoLOIW2YheVisokRcE3DtMZibBBieEb7uWGRAR3GoYdAfvTWVqmspTC63X9-Htf9-2TpV2dzLX5maVEXd2s8k-2eKQoH_aQHp8IYuqd3Ey4djUzQULWE28mHIQKfi0fK4xpHr6MRJx9WOmtnFzJHpDOrslJ4q_Y2NtXmEy_7hs32x3pPTeLUyD-SPmNCk6Vd0ipyou9NpoFP3cg7rMYoYvv1vIHay-qXKdAixWZQRSzqVCNsCIbk8dh4QPeB0kMjLgSrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBEYX8RbOtcAYFgxtbaLUtVLb50B4bhqoe5YVOokRHq9fQJ0063KnYhrC0tdxI_EuKzdSL3Q7JT1SxmFhDUYoLOIW2YheVisokRcE3DtMZibBBieEb7uWGRAR3GoYdAfvTWVqmspTC63X9-Htf9-2TpV2dzLX5maVEXd2s8k-2eKQoH_aQHp8IYuqd3Ey4djUzQULWE28mHIQKfi0fK4xpHr6MRJx9WOmtnFzJHpDOrslJ4q_Y2NtXmEy_7hs32x3pPTeLUyD-SPmNCk6Vd0ipyou9NpoFP3cg7rMYoYvv1vIHay-qXKdAixWZQRSzqVCNsCIbk8dh4QPeB0kMjLgSrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aW0iBhajNe4FdJysgNtdzRO9RPzaMZYqC1JQy-JmfEXSIgeQ_1n8q_1_nQGkXramITzlkJ-lFTNyLyhQpIl87A0YW0sDoCIRudPqfkhSLI6YpeD2BFyvDl3JPofBYzFHaUPi9h50IakWCoZryXe1cZa1rVqVbMJtrbHIslP_HrN8splrkW1hpi0-hifcp1RtqDieRDAV2YA5L18THhzcIV-HOydTWNW02cmkLfFaA84xFlwFcqwjhcR-G2QmZohfgwV_PQmS_nKRFFnL0C4dxt--bY8Jv9WxwxM1HXYh_aGe9_-UKtoU9VGzwyOlCPSoAuAuiFex93uQlQZeSS5iww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LiuhpDONETAE_Tiz0aHVhiryh5R84fc59ux9w6nBGOecxBlG-8zfViTlJ8nkBX1Q6fc54v27K6wmZRA64AG05Z1LUkQJ-TTM3TPw1aPStypcRzh_wk5v9E4pkDUj-ZTc0CDJBWxjxaS-535b1UnKtn6KUNaQ5FXUHTRxZJcv2Du-XAbirEhw9PZl1GbMhhxo2HWpIUu7o3cGYKLJikwOd4VMaJ1jSQLO5ISDAPMyFHLIn5pMNALO4Wk6-PdeuVTW9VfVVLrcDUf57qlP8JCV8snoE4tevrHKZWjtjhIgEUtWCxpnnIa4sTWaxG31KTc5QOOdr3lFWqTbCF4rchJ9lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=P3xERYdxuIoJGk_FntV5N9lYPRLzS9Haet9Hb_iY9ds94JH49WYS4UKznko3ADGKaOw51ioNXk6oaOIMMz3U0MU9bqsCczVAPygU_eGsmRE3DGU8TNoJLsravoNn1gX8tbNna288yCsIKh2Hhbh0qJ_7USEt6uF3z1qB7ULuQFQ1X01BWKXKI5MFXIiv0e8PUKF7Qhqp2ZiNU5RqjIgCv_j-36oQsWwOeg9lgRnPBSIktWYcMXaH5-3TTj_PXFtPWGORq9IMyLYdwHO7ItHBrP8lFxPkMJdSBnnm7G0NFIBlDqFNiTQ5GMg9z7hmaN_BLh8dMD5T39m5QMED0cDRpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=P3xERYdxuIoJGk_FntV5N9lYPRLzS9Haet9Hb_iY9ds94JH49WYS4UKznko3ADGKaOw51ioNXk6oaOIMMz3U0MU9bqsCczVAPygU_eGsmRE3DGU8TNoJLsravoNn1gX8tbNna288yCsIKh2Hhbh0qJ_7USEt6uF3z1qB7ULuQFQ1X01BWKXKI5MFXIiv0e8PUKF7Qhqp2ZiNU5RqjIgCv_j-36oQsWwOeg9lgRnPBSIktWYcMXaH5-3TTj_PXFtPWGORq9IMyLYdwHO7ItHBrP8lFxPkMJdSBnnm7G0NFIBlDqFNiTQ5GMg9z7hmaN_BLh8dMD5T39m5QMED0cDRpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=LO6nzyccZPVAZad5HYPZ9aPu9VhcJvJVlOyo07TP_tp-aiI27XcDnmPjCZuWh6DJWl4I_WsWdFlfErP_YdudjtLNW-rjxYefUuLuYPx-Ok8N-J23Meer70f6WI5hoDbRw_uv3DIu6cjTRPPUrmlcVpDRZzAlGT3hRen9e-X6GfXh3YPIhkp9v83tph73rQTg7KElohDyoO7O_DD2L1iB6BIJZXQqlDsThgtmwJL6x1BUQ260S_6KTOGYYL2wkk4ACbcE8qUpPCH0zDangvb8Cwmj_7dBTrXrMzvwTE7k-bjwpBZsEl_Jfqi__fw8lIa76zVjR8gJ2tHF2gXJyM-VpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=LO6nzyccZPVAZad5HYPZ9aPu9VhcJvJVlOyo07TP_tp-aiI27XcDnmPjCZuWh6DJWl4I_WsWdFlfErP_YdudjtLNW-rjxYefUuLuYPx-Ok8N-J23Meer70f6WI5hoDbRw_uv3DIu6cjTRPPUrmlcVpDRZzAlGT3hRen9e-X6GfXh3YPIhkp9v83tph73rQTg7KElohDyoO7O_DD2L1iB6BIJZXQqlDsThgtmwJL6x1BUQ260S_6KTOGYYL2wkk4ACbcE8qUpPCH0zDangvb8Cwmj_7dBTrXrMzvwTE7k-bjwpBZsEl_Jfqi__fw8lIa76zVjR8gJ2tHF2gXJyM-VpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=HjQCrbKt8td3ndGZ4a6InU1c7vpYTauYjTg7Sh_mPvcaJtIdP8FDzrOJLy-eDH8DnL9MXlRFgHoNofzEZHxVvzU2lAAgKiPos92iHlCcP9tVFnmTd5HHP2jLaOI4AMLXFG7DE_LZhIvCC1EZsxOeTyOpKE48CODPsLBkARzaxzCIctjZ3BIiiLskgrliB-xGngnkXcGUA-EfcE3evY_QnjqWRxq9Zd3iGzdXgEDSw5KOUEm_Yo7zHFpussUER9DJJpPGsSGBo2XuvsnHoXrxGxgE6y53gr0c16ngwZJl-PMlsjM649URGE99b6a-y0EfnuR33XMlzg2dy24jX33pJok0s8SofoxKae-BCc67HcDseH9MlAKu7SyP4k6DsH7hcgZynsDOnRAEAiYuVZRHleWp6zaw4cM2u5oA3j1mDG9G1MuwsguZIWCT8hAhwwZrkZFBoBCfqg9RBaL8W0Itg3c8h9CjnGYqNIoruxoeAVuKgYi1Mtt-nSKN4hHkEc0cm51UN0sxABDrYkRiT-7Ics6wJIrLzPd0qiMJ1Ft3e7MmN_fYCTKUYowAXdvw-BA4S7cLdBFwxWByeR2CuE3GsD8KtWxT0Bcuf3tL52yZrT1Gl2SE8lt_N7k7zgGR_NOuro1uR_FH-SqYQMrK9NY-3ZXyWqiiIdxZv71vYSwcruo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=HjQCrbKt8td3ndGZ4a6InU1c7vpYTauYjTg7Sh_mPvcaJtIdP8FDzrOJLy-eDH8DnL9MXlRFgHoNofzEZHxVvzU2lAAgKiPos92iHlCcP9tVFnmTd5HHP2jLaOI4AMLXFG7DE_LZhIvCC1EZsxOeTyOpKE48CODPsLBkARzaxzCIctjZ3BIiiLskgrliB-xGngnkXcGUA-EfcE3evY_QnjqWRxq9Zd3iGzdXgEDSw5KOUEm_Yo7zHFpussUER9DJJpPGsSGBo2XuvsnHoXrxGxgE6y53gr0c16ngwZJl-PMlsjM649URGE99b6a-y0EfnuR33XMlzg2dy24jX33pJok0s8SofoxKae-BCc67HcDseH9MlAKu7SyP4k6DsH7hcgZynsDOnRAEAiYuVZRHleWp6zaw4cM2u5oA3j1mDG9G1MuwsguZIWCT8hAhwwZrkZFBoBCfqg9RBaL8W0Itg3c8h9CjnGYqNIoruxoeAVuKgYi1Mtt-nSKN4hHkEc0cm51UN0sxABDrYkRiT-7Ics6wJIrLzPd0qiMJ1Ft3e7MmN_fYCTKUYowAXdvw-BA4S7cLdBFwxWByeR2CuE3GsD8KtWxT0Bcuf3tL52yZrT1Gl2SE8lt_N7k7zgGR_NOuro1uR_FH-SqYQMrK9NY-3ZXyWqiiIdxZv71vYSwcruo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ABOQ2I6NgSMYWly2o9LTeg80VnbMrGWRfLuZc7rtooz-DMMKLEzzNU8LhntxPtkQO-KFrqnR4ao7DUhiwvrpHlXrD2E-Zh4bFpLx3pjbDhoON5dPeyD4-rWKVwQK6inwT8oiItQ1dwiJfZxgZdmmyDZ_JYw56ypnwyWq1VCVsV6kHoAzH3fAe_Het_2cD26fTkVK3Iay9pB072dq25AnJFQif6RmJdimGb7MpkF8AzZUGzzlIPb5vptoR51S8Tzcz6Cny-doznmo9IcWA5UIe8MR28g-DcE_wS1bx6-oYygYwVdXR8QtQ1ihU3H0rgRZAhOUsRqG4UM0-fbomH1NNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAB83QYHwebs3RAWgNvCyRkpjN_L9CbKnxacqs7toxCauHY3gkeW0P8EXcShr_w2rc9swwxqRDZWkm7obUX6jfU9JQTJTjLY3ZWt1L596-6NMGteGv2v3MW9b2HTgJ0fZlgGf7CTaupEQia5mA629aebMotH8_-T5Quu5SXX4vTg86P4VgpQnxPaF5LLc7cmNCGEV5JBJ3iIOcaREf_jZaDBCwYb2Yc9peq8hINWJ-lkzN_gt8JWoaXVv3DwJ8PYHCTidIG27q0uBzUNzrk0e2wwnUGNMQTFAJ2u9v7WFQmBKSM0F4qPcotpi5yX7y-uFfyse_IQB3nc8GLO-msMCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
