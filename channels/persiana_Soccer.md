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
<img src="https://cdn4.telesco.pe/file/toKjM-XBPhDFdEauepOrDFZtFiRmSSKY1Ia73S-DVUMkT8h6XVwtNbqIREdD9ppRQZ3SPvv30rj0u5TK7xx13gX5Ew3ksiYYYoxUIS8FiPZK56nOLcSzDIxBQq1eYmZYPpGk0PrERePBGh2US24sunf28O4B_QfVoNmDLgEOnjFm9WDCwl8YACgjInKkX3GIOJGBs6vdHzl8gTtgZCjKuS-Y0lKPOrqT2BbGvNbT_0IZbe8fzmOsoSw08enfUGpE6GdNhr6Ju1DJibp286LdYws3igD4LfQq8B1pdm0flYe4C4lkp20SsT3fdRlFZLKFvU7jjUBjCS7NbV1mG37SZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 528K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 05:21:29</div>
<hr>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بغض‌عادل‌ازصحبت‌های حاج‌ رضایی بعداز توهین های بیشرمانه امیرقلعه‌نویی و فیلتر شدن پلتفرم ۳۶۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=UlQrDwEj42bilEpGFmy52tjcLF98sPfPuXhnzlxwcYa2Dlmb_rUwQHMQrcM-a6PYAQW7zHJUL81ROsIvHrfPthb9r1NbalGqZ9GiOV1FJwUh5sEz3lNdQzkhk4fqcaglHPR62mqyZkf5f3e2-BqXz9UMExkSoTBmLF5riGztJhlZzRzWhWMpH57jVvZEOspYAWAIvY4S4jPQRGQyii7xAd5V5JvQ1YN9hZp9vY9pg5c6nupB2cGaV_EkUoei1SykvjNX5OPYJEztapmwLmjg3VPfoVsQnwmHb5xLrXK54ZfQCdo_oZluHn0o_xe3AM1oD3iDIcwUT7eRe2bAQE09vnD4gJEYvjY7xETJGo33ZbXHlqbaAYZb7npUla4_kpW-hOc1YPGeXAUjRiurNgPyusWhyfFg_KCwchGD6o_vXOr7nFPqWjDAyFbJBB0UauGIqZcv6weHHyGTnbQMQIBow0UY2b7EbK1b0uoUlFxtv4YXGOSLr6nWrEKUuDHWGZbuqosQLBDsEUAoiEPHyOtHW5fUeF5pzoYxLSSdakslyxgl89hIPwoWmezazrNECvNPdlEbPjI4bJqUlISh9r13VP8Ycc8hhggwF7SEOCraEeoDA2df3NxVo8YiNdGYGHnlSvDNlHuinTPtpXTpzlnNbBIJ0y56_P4YWwdYMHhc2GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=UlQrDwEj42bilEpGFmy52tjcLF98sPfPuXhnzlxwcYa2Dlmb_rUwQHMQrcM-a6PYAQW7zHJUL81ROsIvHrfPthb9r1NbalGqZ9GiOV1FJwUh5sEz3lNdQzkhk4fqcaglHPR62mqyZkf5f3e2-BqXz9UMExkSoTBmLF5riGztJhlZzRzWhWMpH57jVvZEOspYAWAIvY4S4jPQRGQyii7xAd5V5JvQ1YN9hZp9vY9pg5c6nupB2cGaV_EkUoei1SykvjNX5OPYJEztapmwLmjg3VPfoVsQnwmHb5xLrXK54ZfQCdo_oZluHn0o_xe3AM1oD3iDIcwUT7eRe2bAQE09vnD4gJEYvjY7xETJGo33ZbXHlqbaAYZb7npUla4_kpW-hOc1YPGeXAUjRiurNgPyusWhyfFg_KCwchGD6o_vXOr7nFPqWjDAyFbJBB0UauGIqZcv6weHHyGTnbQMQIBow0UY2b7EbK1b0uoUlFxtv4YXGOSLr6nWrEKUuDHWGZbuqosQLBDsEUAoiEPHyOtHW5fUeF5pzoYxLSSdakslyxgl89hIPwoWmezazrNECvNPdlEbPjI4bJqUlISh9r13VP8Ycc8hhggwF7SEOCraEeoDA2df3NxVo8YiNdGYGHnlSvDNlHuinTPtpXTpzlnNbBIJ0y56_P4YWwdYMHhc2GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26186">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luzSWFY2JG0z_Nt_BgwJET15XzIBfju75CoHj2huMW6nFJm3oCKDAyyP0_Dy7ShvflcfhIGsD2LTliPhy9N_Bx1t1veQD6C-gTncjRZ0ipzxUqs25Mr3y9MQXkq7MRrbGMjtdZNDwcBeMX3fu2JPdzvZJB85egUeMrv9xsI4Ae9ZXqIVOHgqo3KqwmebYcz9wnxlBfim6vUwmAMsjx1x78G3VtGRprn_H2SJw4jBVDbKWcgaaxnrblY7O_U2_4V9_Rwha6o6ZZtOXgcbjasnWtht6HZcExQ8CZlh5XmeJ1qbQm7XdVdAx4RDBgqkAjlQHoFXE2aZJSEw6xITH3MHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/26186" target="_blank">📅 01:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=TNXxm74ADis0l-ayyRHVj96-jmh_Qzc-0RR0PgPtgBAhB3PPVUAZFGPem2BXfBqTXvdYA2jGptcVgpN0FVmwsUx58DHAaKnDaBbtknn-KqdfXDWyAeodfFYAajD1tUCXw3FjENQYWM2PBfuznshvz-9mDo2mwjpD8Mfl4joBpD3bX0h0t8QLE6ohpbo5im9oB-Lu0uzWoFSBcaXIPZSsbQernl8M-KNybz2N1LK6WHC9Ot5bzw_WcRLZDLA2KLQAVi7BDvcbwQMS9Nkh0ckisrMGxFzj0fniZyX0ExzWWnDhVw61L63_lpEZ3lQ2SlBpULhvn7pgAZYWvg73vx056w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=TNXxm74ADis0l-ayyRHVj96-jmh_Qzc-0RR0PgPtgBAhB3PPVUAZFGPem2BXfBqTXvdYA2jGptcVgpN0FVmwsUx58DHAaKnDaBbtknn-KqdfXDWyAeodfFYAajD1tUCXw3FjENQYWM2PBfuznshvz-9mDo2mwjpD8Mfl4joBpD3bX0h0t8QLE6ohpbo5im9oB-Lu0uzWoFSBcaXIPZSsbQernl8M-KNybz2N1LK6WHC9Ot5bzw_WcRLZDLA2KLQAVi7BDvcbwQMS9Nkh0ckisrMGxFzj0fniZyX0ExzWWnDhVw61L63_lpEZ3lQ2SlBpULhvn7pgAZYWvg73vx056w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی2026
؛ جامی که اشک سه تااز بهترین و محبوب‌ترین‌بازیکنان تاریخ رو درآورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/26185" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26184">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=NUMt8PIPUdjqkCheSIIk593_ltlAYZyH-8ziz1Fq_E6o9Llvvuq_ZVNT0Zwa7WSRrhOouXmQjOk0023xVuxVpzUk5RwmDLuOnrD7XpopGLmMgpTmB58GbB46ck-rdxfKl2hfmPRo9ko18Eag5rDge1CVWpNvIUBfuMV5VXIC8rx8oeVql1svVCHhiX9qok_9bUuKAVizQ2Ukrgo5bkz6aBYcNR2-YTrufX3GCHBtEUiy_JlCqTYTrhlPP5sfjwkafIxaiooJB7CSUbBhO73v3JbAjGID5C6ZqcfWJ2R_5lUnD8ZVdacCD_r13U7gVyo1CEwxi2U3I9r9SfChJqoOOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=NUMt8PIPUdjqkCheSIIk593_ltlAYZyH-8ziz1Fq_E6o9Llvvuq_ZVNT0Zwa7WSRrhOouXmQjOk0023xVuxVpzUk5RwmDLuOnrD7XpopGLmMgpTmB58GbB46ck-rdxfKl2hfmPRo9ko18Eag5rDge1CVWpNvIUBfuMV5VXIC8rx8oeVql1svVCHhiX9qok_9bUuKAVizQ2Ukrgo5bkz6aBYcNR2-YTrufX3GCHBtEUiy_JlCqTYTrhlPP5sfjwkafIxaiooJB7CSUbBhO73v3JbAjGID5C6ZqcfWJ2R_5lUnD8ZVdacCD_r13U7gVyo1CEwxi2U3I9r9SfChJqoOOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های تامل‌انگیزومعنادار ایمان صفا بازیگر سینما درباره‌شرافت‌دربرنامه‌شب گذشته‌ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/26184" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26183">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای شرطبندی هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/26183" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSH-weX1okAfvwDYUnJNTsTGABon821ptqRPm2fD6fdx1cLLsi_dDZsBU35LV3d9vr3tZZQmtrDHQAgngq6_l4piJEaqxtDUH0p9LoyKZ-_GICuCrAK0nf3tnjQItwxf_rv0q72WD28i5E3bTunXA0IlCAE5Kpg_LCVRCZ5TqMk3uVpsVQ4rSdrXAsS7rkIVK8_kLJH4oHQdE_erxnmPx6uuG3SRvUfJBXkCuBd3JT0uylfRoXq9BNT_cyRVc29-CC0y_uWoa5FT7jdYrUV9eqdLfFeyF5cFMtTdsUtGpll8kN9BuCmhJP3WppZag-EEG5HvT3pKCQnoxbn6BR2-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26181">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XihLpvqfgyx6ev2gL9MZQCDKvpxEI2J5u_8yfPZ4COYj5u6s8kKsK5grUnoN-jF4UeUimwKyPnLlgPoWlXGGFAku0w1ZpUamUVRN-DgE61pVOJ2TNeqmT_4_e0nanstsUVfuqpTqOB1-vZvdKJ7VmAuCA2o79Z_pcz66RcH5-j4WQdnBLCWOf8opYfeWVBGJixPVJF6qRiMdvMyxjs6o5jf014PU_KPesCgjvI2FjFTpiSrrjsv3gAsa4bCYtVrph6wCK4uEilJ8eaV-dg73GbiZeqB1vEs9pJHBtE5o-nscpL2qBX7hEno9Jx_SRNv9eVVQwoArcmKwUc7_UDNwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوه اوه اینو داشت یادم میرفتم بگم؛ با پایان جام جهانی 202؛ تنها دوتیم‌دراین تورنمنت شکست نخوردند. یکیش‌اسپانیا بود که قهرمان شد یکی هم تیم امیر قلعه‌نویی که از گروهش بالا نیومده. قراره صداوسیما مخاطباش رو با این افتخار باردار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/26181" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26180">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=PYcHv0ZA8kQkcd2lgO9ifQ0jTzdMoNutbkj6v21N_bj-b1zNrwZK0iMQ1aWfRtdChlPRCvP46Q1XfCmJYC4F0PsZOU-QoP6I16eaEIBbr33vJtwQoMpBZj1b1wnaBMIhpPCoocTLH7Mqxc1TZpH2E9yEa871khm1w1MISXQSEuatg_S8kln06jVR6EyfAo7Pff992j3kLrKH30RineuZ_7Mmhmren9fMdHlHif5c8DXbBQ5itfXtSHcBzevAQajsdQxEjR3v6qMyHlLG22cruJq5nnsO0Ag2NwL0gX1GqcLiNYiYG_ga3omHyzil7nvT3emO2hUGbYll6wm1sheHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=PYcHv0ZA8kQkcd2lgO9ifQ0jTzdMoNutbkj6v21N_bj-b1zNrwZK0iMQ1aWfRtdChlPRCvP46Q1XfCmJYC4F0PsZOU-QoP6I16eaEIBbr33vJtwQoMpBZj1b1wnaBMIhpPCoocTLH7Mqxc1TZpH2E9yEa871khm1w1MISXQSEuatg_S8kln06jVR6EyfAo7Pff992j3kLrKH30RineuZ_7Mmhmren9fMdHlHif5c8DXbBQ5itfXtSHcBzevAQajsdQxEjR3v6qMyHlLG22cruJq5nnsO0Ag2NwL0gX1GqcLiNYiYG_ga3omHyzil7nvT3emO2hUGbYll6wm1sheHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگام‌داره واقعی میشه که؛ رسانه‌های نزدیک به امیرقلعه‌نویی میگن سرمربی تیم ملی ایران میخواد بابت صحبت های شب گذشته از عادل شکایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/26180" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26179">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=mxFNvYPYn8YEVx7WgDZGHOWnOmvmEBMmrJ9I-ka_AluM8jrW0DIoPT56Qe28kkpfJ45OsGkJhd97D5TfDmFmp06o-F8JJYEOhv8tStMIWkQDrvMdc3SD1pn75UmEZ82z6KiRfL0hqcybKNcusFzUM5cNmvMEBW_AXFUlijOfhyTD19s5_dgFlDxHZK1ZpF6bYg9qaNmP2dXS-kuQNe2jWnR0oOErnSXSDSl7szqmby_mHUabcrj02MGWFiCbPqI6j4sqvAt2kgcwt_42DVr70if2f5Dpm9GyP0a04pSOJddCvWb1-J2VWg8XYRMANpt6VPWAiK81dUYJIPaHpx2sDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=mxFNvYPYn8YEVx7WgDZGHOWnOmvmEBMmrJ9I-ka_AluM8jrW0DIoPT56Qe28kkpfJ45OsGkJhd97D5TfDmFmp06o-F8JJYEOhv8tStMIWkQDrvMdc3SD1pn75UmEZ82z6KiRfL0hqcybKNcusFzUM5cNmvMEBW_AXFUlijOfhyTD19s5_dgFlDxHZK1ZpF6bYg9qaNmP2dXS-kuQNe2jWnR0oOErnSXSDSl7szqmby_mHUabcrj02MGWFiCbPqI6j4sqvAt2kgcwt_42DVr70if2f5Dpm9GyP0a04pSOJddCvWb1-J2VWg8XYRMANpt6VPWAiK81dUYJIPaHpx2sDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/26179" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26178">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc3fTur2v9XL1cNaHTZYx9NsMA0RzXlFYdJaP91RuAqL43Q2cMCfKmfMHSlvmcnUTZscTmYUXYdnIEGL7RoBfmhATT8roTmZm7vGirjatCD16hddRYBllaIpRz0pYMZMpMfSfuciTYx9Na66xOq9us84ncm7rEa6Us4tGJgMxzoz6ejgZrXicbz2GbwFaQs7uBUWKkJlCCAUORF3cRnCncujVpj7apdeCa_gXwrin7i4wYsmzKr-jEZkRaYo-e6JcW4ox1CeHkoiMivY724LVGyBRd0Vj2qY1zeNEBuEeW-DTBpYLYR3yHHoh2qrNQFH1AUrP8JNFPuA4SWK5zxyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26178" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26177">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlrglLG8qoyOSLXvunmfm8KG2ADR3IJVfZMyLHA46Biw3xcXtqIekwTVuCiW5fEfeg05bWVLkhjRE8QLOtJgaBqOikZpp-eKyEPppjzAy91qUNGknjLiUpgdrL8R3EN0zBrNbHOvC2fqC9eNvG90tFMycZ-rYwSJXrs9kEFdgMM72wDpn0M8drq2g8ZZEEdGUeJlrU47dJwZ4iBGC0JWYeuIN0L0NkfGztW_x5r5CZ_HOD_AVUU6NU2wsknG7_gNwYQrQq5pabqK_l9AEbBwH_TKkLLuJZaOK7HrZPNlewdQtPssE2gHF_govjgV75W2qb0qBawNeliyIdVEbVpDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26177" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nij57szZSS_wfrN3GmkLbdDEdcCxJNtBN3Qsa0Dis5mAufuaNk0btVC0zvc51JlW84r1XHvgg46iAJhsVVaao46jPXGWQf0RU81buuxbf7KYX4U2ULM29VbIPZoBNldBInBaq3VebPOalPqkihxI_G_pXNdd9IhHiaC-mAasIDrMdYpVoR2DIg9kijLdmavWLA_b595P6IROkLapmJ4C5OiNzBLOsimvSfNbpBQcsxSAE5JJK429rNFFnvkf01pAPPXBS2nfYG-EkuVcAd4EwRh9eJsHlGF6rBuhMGLOWfHkDMXGfzWJNUXUEZroN5bBVfJNXPhidxx5wO6tW_-2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1L9CQqfd4KKVxWto8gwiunoFcCfoVIHwwor-_7Iw_yQNN4ogCuRyUOTM3dgY6YdYW0BlJGT4cDXNAxNgPceCAjkZuxAaFbb8cyCD0gnWVvPeoVxYNC-jA0N67n9VA9HbaiKES2o6h0_yblnL5QglRNKld7YPSwaVfwP0o5kzl9G36ClslXvAFAq3j6Uo9f32RMBjQVPlrCO5sOnljG5eX2O2EO6iXVV0MCQqAb9NCYTBx4jlZyj9sgMLq5ja3eEqLQatw2HlcrVr7QUc6iAExP0nImGnNLQvFgpMDxG0o3PsGuvCxTpby6CGacVKih7j9Rruo-PN3xY-vktLaugpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26173">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=JfFO2IDj6yTXoTKrBDBfXeQxRDMaJfMCW76xdg3rgJj5WOrZ4wakLNFR2UDoxdOl8RwHb2IOutFabP-7fEBbMjzqwTR9m01h70V3ZVVuL5oOBwGql8wudohNiIDR1oUEDmTnZccj0tWbx50hNbg8o02T9Pi-u3mLgwut4GAiA7kKEsapEJbjH0tb118IRN_MmzIJYndCa6UXzfG2EJ_cu1_kg9bC03Q5DMfR8-QVKfLddC8fuPtSFII-2z03BTUK5G0cXZfA3r6mm29DE90mAvklmYV4gdzgBb0B1oW4iqX_VnnHLb3KXqPmlEYJ7bBRPMOFcJNdURHMgkRJWfdTew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=JfFO2IDj6yTXoTKrBDBfXeQxRDMaJfMCW76xdg3rgJj5WOrZ4wakLNFR2UDoxdOl8RwHb2IOutFabP-7fEBbMjzqwTR9m01h70V3ZVVuL5oOBwGql8wudohNiIDR1oUEDmTnZccj0tWbx50hNbg8o02T9Pi-u3mLgwut4GAiA7kKEsapEJbjH0tb118IRN_MmzIJYndCa6UXzfG2EJ_cu1_kg9bC03Q5DMfR8-QVKfLddC8fuPtSFII-2z03BTUK5G0cXZfA3r6mm29DE90mAvklmYV4gdzgBb0B1oW4iqX_VnnHLb3KXqPmlEYJ7bBRPMOFcJNdURHMgkRJWfdTew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
دیشب‌بعدبازی فینال؛
یه خلبان در حالی که کلی مسافر آرژانتینی داشته روآسمون گفته آرژانتین قهرمان شده درحالی که فینالو به اسپانیا باخته بودن و اینا از خدا بی خبر اینطوری خوشحالی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26173" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26172">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=tklvLyvlJy2F7CjrnyscXI4XnugHIQCDastqQ-etBGBHswr2Phm4fndiycwBBj_1639MaVJq7cP3HzzUMXolIffi1e6RGZML5Zk0oNOWi2QnWCz7et5s9bCp3eUcCk-aNL5vVE3pFW6NJdBEpCe-IUHo_zqxMmpyvaix2UC__eVdloyg5kDaZKDOr_5DYdwSXAkU1lnPaloDvwqIkcYKOKDr0oINR5r8hMzCWOQ24r3OwB0NrugHgnBR6qsZrRJEQcFIHqKldNmT9V6IyfAczkjvC4PExuk4NuGOJiWLVwWKrSOurHepeL5ctm82QPNBrUrWN6VYyN5DgxDCpYnzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=tklvLyvlJy2F7CjrnyscXI4XnugHIQCDastqQ-etBGBHswr2Phm4fndiycwBBj_1639MaVJq7cP3HzzUMXolIffi1e6RGZML5Zk0oNOWi2QnWCz7et5s9bCp3eUcCk-aNL5vVE3pFW6NJdBEpCe-IUHo_zqxMmpyvaix2UC__eVdloyg5kDaZKDOr_5DYdwSXAkU1lnPaloDvwqIkcYKOKDr0oINR5r8hMzCWOQ24r3OwB0NrugHgnBR6qsZrRJEQcFIHqKldNmT9V6IyfAczkjvC4PExuk4NuGOJiWLVwWKrSOurHepeL5ctm82QPNBrUrWN6VYyN5DgxDCpYnzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌فوق‌سنگین ابوطالب در برنامه ویژه امشب جام‌جهانی به‌قلعه‌نویی: ما تو غار کنار عادل هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26172" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26171">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=bmws2XDO-X3KebalC0dE4CGaUTV4qXv7RANo3TK-mOV4GQgr7b-LR4HNqtzefVdKl6Xpmwf0C5kusUINAr2aX881oVd2sJzKJAxsnFi9ywLaA6uIE4c-pGjfNVEIcvEO1DiKDDspG1d4cqL7LmKPBMX0QuK3E0IEhgr3NsxBDPx6B_E0DNTYTmP5UUeg9F_G0CwQ9HXFwI7qZuCNsbdIJp-A2T4UpFEWn-TYDHHbIlb4zxXmj77V1FAkeMKnpjJgHwMoNoskelqWU-Rf5vu3brz-hc2vwmS0miVbO5mBIstr_1IlKW1QLIrnDQZei6Xh2is7GAxTq2CgE4PE7wC0fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=bmws2XDO-X3KebalC0dE4CGaUTV4qXv7RANo3TK-mOV4GQgr7b-LR4HNqtzefVdKl6Xpmwf0C5kusUINAr2aX881oVd2sJzKJAxsnFi9ywLaA6uIE4c-pGjfNVEIcvEO1DiKDDspG1d4cqL7LmKPBMX0QuK3E0IEhgr3NsxBDPx6B_E0DNTYTmP5UUeg9F_G0CwQ9HXFwI7qZuCNsbdIJp-A2T4UpFEWn-TYDHHbIlb4zxXmj77V1FAkeMKnpjJgHwMoNoskelqWU-Rf5vu3brz-hc2vwmS0miVbO5mBIstr_1IlKW1QLIrnDQZei6Xh2is7GAxTq2CgE4PE7wC0fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اینوقلعه‌نویی‌بشنوه‌دیگه فکر کنم شکایت کنه؛ تیکه فوق سنگین عادل فردوسی پور به قلعه نویی در بازی امشب: آرژانتین بارها تا آستانه حذف رفت. فاصله‌اش با حذف5سانت و 10سانت و 30 سانت بود اما خدا کمکش کرد و موند در این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26171" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26170">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=FDNdKfkdze7_1u7bWrG958_huSmR8S5whHuF7TreFK8ELyvX1SytRKesDGSg7fzSd97Fds1v6EKgZXi9jDRK0oVyOkxi7c0qmRdISndeNfYUzrAOm4eOcg3VJ0oGn8F_xrGlM6ZinfI487AmotjM7st5Eqe3EZCkymwBaxcx0u2ZuWpGRS7UlHUL3ilnv_1Lxd4KxCmZUECWuaKBqyVUvOGeNCmshmBTnXzfzFBNtszLYesMNIJnv80jRx4ekBFiQ727D0uH3xfXPGYWh9ncPNz26OcP3-NvH5NAqh8Io6AzOFjhszSum4YccbEzR0605fWSuoM2xz14ZSZnrb1YhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=FDNdKfkdze7_1u7bWrG958_huSmR8S5whHuF7TreFK8ELyvX1SytRKesDGSg7fzSd97Fds1v6EKgZXi9jDRK0oVyOkxi7c0qmRdISndeNfYUzrAOm4eOcg3VJ0oGn8F_xrGlM6ZinfI487AmotjM7st5Eqe3EZCkymwBaxcx0u2ZuWpGRS7UlHUL3ilnv_1Lxd4KxCmZUECWuaKBqyVUvOGeNCmshmBTnXzfzFBNtszLYesMNIJnv80jRx4ekBFiQ727D0uH3xfXPGYWh9ncPNz26OcP3-NvH5NAqh8Io6AzOFjhszSum4YccbEzR0605fWSuoM2xz14ZSZnrb1YhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه سنگین و کاملا مستقیم علیرضا نیکبخت واحدی به میثاقی درگفتگوامشب خود با ابوطالب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26170" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT5wport7fUSbDG9z7r2y8C4IJ50wYHv9zgcFj4ty2cgHjpPIdzi0ggNtxW8IMFXEqGz8oZ83IdVAYLR439dV4-lVpDzqholPZN-wQV0svh3bNhOgI_kDuCyWrL20BW8IWQ1u27GbJa9ymW7us_X_R9vJ0F9nU11eMSdrPBGeXDfeliVpbnTbGaj6uni70SGc9OPdazAAhr2S7mDKk4Hz1E2wfFUaDIQUwlgeg4zoJhidqF2NNkS8-olefTpJizkk6x8KKQ-_WjI49SU555kPwGYguG74EPdBPK_Bf0QhkDGSgIRq2v1EWqy4_SqQXPMrbcbYtfGJ_aLfyrFpMETHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26168">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=WNYvxzFgTVEOA_VpMe8kX8k23vaixagMTafsAy8sGEE8_0Hzlrsdj_lGgL-pSYPmh7eK4wF5ewbaUwrJIhyWQPy1EDotjriEPuHH9hgmbikU2cwHY10qqDZax0rqv8t0kKxDTZ8Mdpm73hb-LrsAhHea6CFUE-McMLS_wpQFCJGAnHHE_4PyR6gum8d-NmwzezE0_BnHfYGHT4RwoWFH64oWFVCwTfOzAM0wpaxjOnKbFT1HEADVOXjnq_KPhkWaBKwpxPScqTQWq6bXAFHZLrmcKpMEb_mOgGdGcMP47FvY_SFOrlA9_SFwBi-tsCjS8yiUH5seDV629rP-nNPdI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=WNYvxzFgTVEOA_VpMe8kX8k23vaixagMTafsAy8sGEE8_0Hzlrsdj_lGgL-pSYPmh7eK4wF5ewbaUwrJIhyWQPy1EDotjriEPuHH9hgmbikU2cwHY10qqDZax0rqv8t0kKxDTZ8Mdpm73hb-LrsAhHea6CFUE-McMLS_wpQFCJGAnHHE_4PyR6gum8d-NmwzezE0_BnHfYGHT4RwoWFH64oWFVCwTfOzAM0wpaxjOnKbFT1HEADVOXjnq_KPhkWaBKwpxPScqTQWq6bXAFHZLrmcKpMEb_mOgGdGcMP47FvY_SFOrlA9_SFwBi-tsCjS8yiUH5seDV629rP-nNPdI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26168" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26167">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4HeFeBtzhQBAWW2mfKv5TM3hhhN_keeUPeN-z_8DBci-6O8CuVBK6CZnEJ0WUt6QBatQFVUP2Lrby7QBAG7kgxXbNXU3WClEzpL1InDb_xvXTmHZ3hiFEGtU-V91w6VrerA_DbWnSK1s3nPsV_DZ8P3DoEHSBISw5-wvAwxPqhjIDke-NAN3pGYWa18syEPBAIUezn2FoSZMMbhm-z6rMscIxBwPq6l1iXpKAraaKk4vd_SyraJyx77aUNGTrvsaGmj1WqHUrroM1PA0abvrD1K7RGphdcUYlhYU3CC--6CY2z2F79bYMmqb_yG4GVtuaf7pOy1_l00WZt67Td2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26167" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTDEG-_-1ckq3-P6urZ2KnwbYNW6gN4isMWa_QGBM9-GXX8Cq5sf2VKkoe6rpJta-S7L7mGVqKJ90hjJOzSIXRkdr7pq5V6Y3DzyH5bVAFoAr8oyl-kbSdHwHiaHG44MU8Wwi21_Jbd26vQFjwh5KL1ZIMxcz6FRyjG6YQze0CdsouAr2N37wMLHlxqjcfUEwgR_q1bTJf86JbrTr6pjTAIMQcqYif5IxjKLLHeN21-4z1c1GYy_PIkhcnn5HA8bzpZrTwoUjhv-Ka0KQSccmswAJeq9JsEVsn7niLuHx51_QnvSoNB__aI1glgtXbq42OL9pS46ZZwvLKFcQHrN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLBQwS9JAplo0wbukOKW0DqSG2TNrn9ijOkl5KoGNMwAbUOLNSI5Yh7tvjawUH-nHDW-UnbI_8D_82oUjydbVmSOGa0gOfkXdPwsFPaNbUo8rMI7nmjk9VgvIC2BMRKPIyLJZclO7ELbM5WGNQJFocZVq_HZlUaLvzM2pmC7dp1_TeUgtfpOanVvNieWuZkfyMRT-PNb3CjGikY6JaFrg24vgvZiiOgL9Bs3TpDoBGv9vSvzYKo1mEtwnUZCp9MAVNWr07-stf_X5sc5jxbh20qJr-cF2LT4cBaGGIikYXKSpQhXD-IW7p32jAy-UY_q_C2CuLeVvr_r8rMqqeG2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebqqgFHZl14cDl_aQYn8j2DV3w9qpJP1Oh2r6maDOzMM6G__zwfFrkJR6fjVPOck3RKYRfsAtg-24kZ4Q6ye_ItpeNGSkocq53b2RDivaBdc1chYnpaFaEPGLMtMiaqemlzK4ANsywnENMSnemPO8-3eAIfkybUTOaA1-JM91qGVmChBva5B-LnvfHkV9UNgzSgLzRypEq6vx8j7HNgXqnQNsp7Rc2hyPrPUTxrqc1aYppPOQktiI8Aaq1-KzrnUCQDFakbKSo3hfvuNAGwCvp9AeZ7QEYmBUL5T-IuMEbCr5WloFs53ZIwo2CWegZdNPunxlS1z2ERzkXZiOwVtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM0MSqsHGFLHU3HWnJxrlC8LzXq22zgqVqZ_mNLGIWwSg3fYVo6gPC8fLyIIbc1qXzSsOinwPTMM8eYlWsuR46OL9cFyYXxLWzccUoP2rRm4XVKExUSahWNSY3NDq5SjnT-uG2PwoZ5QGKZK58ApH4oRRlEPTBzQ0vhj4xOq1UxneVaWcodZzdbOm4Pgh0L95DGyChGM8-dVoxtwtmkHNuqpbRLnKjamUIyW8DBQQfSnD45ui-7FDGq01_NJKTY-IDQYJvig5_JHLHoRnO5EsHLiShqZBnx22sKAq462woeysKArNAabl6Pbz-fQrreEfWo45d0TZ5ODhEKjBz62Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmfRnNJlIPjIdV5eNBGgB-XzM9NnRfUQHKxDP1r2-jUszIumufn6tS7ADKEF5J-dfcPmQpWQrdpPemOMzw_mUs2Y--K2DhtHJ4meZKSDxCXN9FAHKdxgMXrLFwHVcXUC4FhBU2mtYlDQ0u1NcM2GjhohWzn2hdec-W4cLT2fT8K2zqBwrJUltkOuNnc1vqy-oLzDdL6PqeHXLgKLpkgDN_t-J7M75iVRZnDlaC0_xBNxD_Yjy3qsEHS56kpLGR9TrdbEIHMivsBehX3MuHMHstD42uQGZskjZ8UP74Pv3zLwmsnYcFjLFyyXgZoG0DTGb8CgiPrGxJBmKtUtEafSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL42G3bSjK_fsHQspJafKyh5mHUb5ht0UJB0Fn7Ukwz6NIIAnFPFXcaFaMHsW59IQCGCPKNKhBJupticnakp9H8FZ0XcLKazL5xhXDEV4KtmV5oFeduwXP6upLYYKfVhUTdUh-gEPzG8wxZU2S0BVCFslkMJBtvYIb8AZoTi4yi8JSaq6DGKltXH1niv8gwW3J-QNiL8NvvPys_QRzq2ukEfx1fkmpxxTAZKiy2yhat99RDVdaCYDcK1iEwjcVgb2cICWv22O4nSjURyOvXYriYibxmOiU8NvqsTvEtnU43vMHIS7P5ew5DEyhEvILqcOwaDwN71guBzMviHgJEwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=TJNSZ-HJV__vYKDv9jUgD6Vld3VUC33oDD68OoWTeLTtYnq_zgcS2VGoOjiP9YmWO9i3v1mtAoEKVfIGGzo6VLsDLy-uBU7TUpQsmVej8_nGsAR39Op0sPlEB-N4Ia3Hv4GtwD3VnQtNKJdtZYw4toZ39-EFvI4togQ_oRahTK8ijX3V1EYJtnZhg6Q18jZN3AWc_GVmt-mI9uyBYb-IAUm71HYYUDDPBu2meelI8J6oEzpHAM95_kZWmDyDYp4xUFfzi_GVjMGhCCUhwRf6yrxQ_a3waoq1ehgyaUd9OoOKjqk96_9QqtN3Y_knR6j5auePW7hayyHvvTdkofR4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=TJNSZ-HJV__vYKDv9jUgD6Vld3VUC33oDD68OoWTeLTtYnq_zgcS2VGoOjiP9YmWO9i3v1mtAoEKVfIGGzo6VLsDLy-uBU7TUpQsmVej8_nGsAR39Op0sPlEB-N4Ia3Hv4GtwD3VnQtNKJdtZYw4toZ39-EFvI4togQ_oRahTK8ijX3V1EYJtnZhg6Q18jZN3AWc_GVmt-mI9uyBYb-IAUm71HYYUDDPBu2meelI8J6oEzpHAM95_kZWmDyDYp4xUFfzi_GVjMGhCCUhwRf6yrxQ_a3waoq1ehgyaUd9OoOKjqk96_9QqtN3Y_knR6j5auePW7hayyHvvTdkofR4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26152">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh8D0RhyM7T1cVHNzHw0RKkbI6GnNhSA3_MbqQtpkeop2w02JrWoj8XBp5MA-oNLD7T93Mea3mroHvQlKNaU3AXpDceYIQodg7lPSZYynR-WTY3NrQN-zQKerBeKgEVAHI4azHqNINO4SnzWr7v0w3nLAuVX0NRrVXsj3wz_cecIhy8tAiKWdbpSSdLMs9-BpPd2dUgcUbsJ49TVZofkLd758JODhagAmzs9yssWcPTW4kNxPqrsb0SvIq753wjKEjJ_Pm18UbxX2a47rMi1p6ZNxAaWbcDOlUPsVETtNe4ctx9qKuCvfgCHGUNkz_HkqMk_fQjI_Ioh5ZrEY8btyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/26152" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdoGvj5IrWT1KXq2ofkh5j5dpmLCVh49R5RvCosjLtqCN2dJfbeOWxksQOLHk5AqTvWEcIYPPVr6XP58b_li5SjcXnzK7zEueTrW7XvVEaf8BadVPBy3TUYBHNXeMCow433h7tY_n4in9JYCP_GywZPrXDQWJvCvhRh0vrgOryyKUCXY72PU7o-H___zRJd6A9o-jl9XOQiTsoC6tF9lPvKK04dbnKmDtTILcY7_AooPgRfS37Oxj8MsEi46tYDVPLSJUkA7N9i7fmPwCc02GWR_FItgPZFS6OoEVfghH0BY7s8tt6XOHVSNR36lghesGH815sHZj-pj_9pLoQM8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glHYNpIqR3njFztDM8EDvBQIPTLfCag4EJDomIw8ecXz-AV88yGD4b74ywGLyyml0817KhjtkygV5x2erya1DAAgMxb7-Ln0rPst7mPctp3s4mi9--inbXJkkxrf89lNqAK6Owf-QVEQ-eSWFIi_AZgPVcwmGz_2NcEJ55cLpOQOGt-uC4JDYGgLYNAgNhB7TlzN_UxsSNmtemfwqJdS2I4Pu3lE5QzbHbosZDcXTzKpE5-_7yxuaa_qVRaapnzA3YoW8zkpvPMKXZPZyl8PML-KR91f9hHyhm6DMr8u2VYkUIGaSxV6RIu8qN728mk0aLoupMSNQB1Gkt9FRea0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=A9IR0zoICqYs4Z7s4CWywwWzk3sF0fqe9JBPGK2PMS-IGIBE--Lio3PSneI1bbSDo4OTlHmdNSJjMV_SLTLWxtcvwiipr4EdYhacoBgm5qwvhln9HWSJr9nhmeL9O3DG6FTgVd0YJFFNtPq9fpUzu4cH8EZHGUVz4tuhGTyZzhBdK2QSY1aXub3CnMi5J8CvmzSXQ8Schayd_FcSfX5bvDGoKDmY9Tdf1xmADGC2NdANiNZZex6isgg4NXf952oXvhg8wjr7CBYO6jH9bW9chAYddP7wlbexnhwr34G5Jp2AFK5b1QzQpu1LSyYEuFsCURHjdlo_hvxtMYSJodbtpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=A9IR0zoICqYs4Z7s4CWywwWzk3sF0fqe9JBPGK2PMS-IGIBE--Lio3PSneI1bbSDo4OTlHmdNSJjMV_SLTLWxtcvwiipr4EdYhacoBgm5qwvhln9HWSJr9nhmeL9O3DG6FTgVd0YJFFNtPq9fpUzu4cH8EZHGUVz4tuhGTyZzhBdK2QSY1aXub3CnMi5J8CvmzSXQ8Schayd_FcSfX5bvDGoKDmY9Tdf1xmADGC2NdANiNZZex6isgg4NXf952oXvhg8wjr7CBYO6jH9bW9chAYddP7wlbexnhwr34G5Jp2AFK5b1QzQpu1LSyYEuFsCURHjdlo_hvxtMYSJodbtpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqTemamjNtuDoUBDjNyEeJypuksXWx7qNS2GbCpUGawVQoBhXN8FCc9zPwF_aQJIqg-QEi0Db0b5sPYecdnVNCs8Ykl8demX-5jsOYoWN0tcVBdY9EBi1xUHmHBfv4Al6SMwCfKciVX7BK4r0bw93aXXOtd6Jmh58axa21hFKLwnKvlWC4Dca5YxGvFHfzDMjCpCRoT9K5MfGqIxyfy7WI-ILsXm-WpduvOdPDDeXtTbDn1Z23-5v97JTpABbgKgj_QgHY8Yq_90TyhtY4m78JVgo4SjDeXD1dN99GwggZqGzWzPsFMBDBqKanclK35IhWo6gpWIpymQJ6QO4HdwfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dykkBHNQ_r16kXuc7KtbPyJCMUfR08kz2kv28spPR9ye1ULerRhj4FUORVd1Ur5ypA0IUXv15ctGSK2CQP74XTq6cAbPfjrLPm7ItselFEKH9GQLKW2VETtZNpT1ppyd7prYbGwuYtMbDHjgUh5jy74sr-5SywvNheFo_hc2pffErqztfL4s4VMehy2MaiKLD7M9BUfr9HnyHIFP-htciTfQe8EqiVlfGQOfirkNukwC3PDMjpSdgsiOyTTHJ8lWgUwJt34-7tL6YIvBQZQq8QtS70Hk1da6QQwrYHFXaO62_KDsTdPj5f7taZJ2CEbQVQo1GWdeoutnZa-bfYEX5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTjGHNqhWOeeI3A6b6i6FHhDVUkdk4ijHhtqI_wQIJKhE4ZVlcQhkcd-yVuYHH_NNE8lzGhiK-yEKFBh9wDHXz8cVHC6w0ECMdt6d4kLvH_tWoq_6FyLJwnMemZoGxbu12pfVSSmjaU6UKab-gjy5xdbcKe_UdFFCma3r6Jln0eDsBOvR-26aSFLiVxpbuM2tuVYLaUVkG5QODkK-KWnwMrgAzTRv68QRRAetbvCvlm5cir98ImR2Famh12m-BzQv_yFan6AKtv2AH4w4GTP1DqHBlvY_9SjH737Ao2sJ36Cpkt8d2TqZhUDydcEcJQrpBBGpET3MnhUNhq5aoQcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bb2R08Ru8z8zez54BKyAn3EpmONCGw2HzE66VkhSJ5hi2umn3b3Ig-fsztD5aC4nilYO5s__MiAdeNrMxiA7BGnkePVd8XtnEhS-qd5wn9Z-wU5ifxZkiqGlWCwjE_NBIvZNZVg_c-fdnuGd-cMsUYs3GyLM1ZKPLMT_4r4f_u3gjwSwR1x954oBjtoST_qjGZMD0YcfDt7i1TfCe2rKhZAV_sfDHvLwpB7Km0A1wcUQqDl6xRKeXnQWxcbn6O0aJraq7HGOOTDtKXojQ6A4n4iPHoRgU-5QnUEP2WDOfZVlBUJp7KtHw6dOvs8F0Fy1dKFqV4QdrYkigV-woFTS8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTj2dIaFGvHDVyfQo6AyeqT5EL3x7JryaoVHhpUdYfNmJJdw1esdfE35S4tuirIdRUtWBlBQJRBaijOZ9rFKS_RVv9-Exe1P3AmZAYuDYtVw9iK8rpNRZh_DlTjR6BcG8Lf7KQQvscK2AQFDTBDPBmtY8U2SA2TN9ojW18uTdj2pN_yyd7zcumOBP2wzcb8mbYXs9-mH9XvEyz7NcyeOZBHSYSKAPhaQ5zZUiQCQWWWed1X9SuHTgS_ekUPtNBXj_4a8KksBdXpiT7udP1bqri8NqYCQm2Tgc8VgifLLBhl-wB34Nl0XzGu2ojbl5P_9_5X7Oty24zks1W1dFXdYEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0uTaeHKH0BBcQno-o1TsyjAV3vGQSJIduWSk3G3nyC3ddPdYhT5WJiQ8XOEfOrnWsq7tHCt0DPxndY1SUYCSXeJ7te1k4YdM_IdYz9vkIqxNKft6dSsQ5WJlxRy4vkN4VPR71iePAy23GUtffNcui5uykWaa_BZfekCwt6Zn4i12OZ48M_Bmzmx4LSpRcKtLIlk2LG7elGIl7NLs1Y8RIBh2wnyjs3TsELZmMFuiI1NSoqUTAhjBUvMzeCv9ZL-8jA5oOu2VqrNKHPiZ3TzvUaA6E8a4p32_ye1TE-KkE-jMzKA9thm0sPAqAPzyyvXBqz9OuufYKlm4dLzxAjfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDutMnTkhFW-Ir1aQPQBn9YX_dtLX_cNfVE-OvmCWhsogcfQakmuURxxzuwgsCIigX-MPSFHUVP6GHDto6Blk6CurAWiFhi4kXZoEO5w1xVDoQKUkJ5TIk2bIvT3cdG7Fv-YNtIzcZJDt3CJkrTFpIsQzs9lkfjunHWG8KjEHYg1zlFHraw5ikCwya3IS1bHlQqUyj-8E_Zmuy5ew8ARfXFMDQjTsmZ1lvYLjXJxCGraBkhXRCCwqlUEsn3TmOEfn-irH8Ks6EB27s1JYasd9VArdnV4-Mth_XoETAJqICr1ycAVhQc5H_8CGwhBfDZ7XJFOumjT50tUTHkhi6uNsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYp1lBTSOaqTGM8JlCev4fDc7roz3JUGlLKMBIoQzNdgaZUzw4hlnWVRJJV9ersbxzC-AW9nKHCipt3SNb1k1ochWjm4-XuwnwyIoKaeK9ZosQ9-DHqu0z86DaIYC8hQPBTlA-HsBPQTYJFbo0-T3JIHUrHVZh7yVpkl22KYgMH4GEuyYnCsAWg0xmf4mdMjk7MpVXrglVftcxd-lCCdnAb5c2drIBhmpRrHnqKe4bWdmGMXO2I8lX3Br64tYYAbtrPZzFzPfBotRXajNsbKXkS6ecmaZtuLnH-gbTXY_JNG_bHV4dwf8loeWX4nw-fl92dRrzCcs4xvMaQnBRfRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=Lw-B0vZFUtIAMBS6ekHCTZdMlaXqVT_XB4PhhuEWjEXYAA3SeRRmC9xpTSFHtvvjY_CH-SlNideL3A9HhWJj4UqKh1irnLDE-JUEV_i4U18JhK1bDagMmCJPl21zNjv9WvguW1qTETV8dwLjrPMPMYvTsgxVLTx8ffBgh-ytHeq5bCeLnQJ5dsMymvmWecdfxxuG_G5A53ERlk6Up_ue0OSOiV19S6cSa2_CDABSNCOXUg8EthiQr0qOSmyyDaRqCRg-Gu5o53XcGjndaDPbutp9j4kDVhedgcPqYktocSFxWV2IyhMN03XanjX4nBWNRNcsTB9U86PLC0WwLJhjIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=Lw-B0vZFUtIAMBS6ekHCTZdMlaXqVT_XB4PhhuEWjEXYAA3SeRRmC9xpTSFHtvvjY_CH-SlNideL3A9HhWJj4UqKh1irnLDE-JUEV_i4U18JhK1bDagMmCJPl21zNjv9WvguW1qTETV8dwLjrPMPMYvTsgxVLTx8ffBgh-ytHeq5bCeLnQJ5dsMymvmWecdfxxuG_G5A53ERlk6Up_ue0OSOiV19S6cSa2_CDABSNCOXUg8EthiQr0qOSmyyDaRqCRg-Gu5o53XcGjndaDPbutp9j4kDVhedgcPqYktocSFxWV2IyhMN03XanjX4nBWNRNcsTB9U86PLC0WwLJhjIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKqrd6RGPcrD2DyHJxAr2s8quitL4TiNFlLdei6TMlNN7B4q3pE-oyj-lhYE5v9y7_p2Nx_mFVuzg5IiCSXq0l1L2ytR6sCsV5uoYugc98UOiwZBkgOJ9V5vyPBpuZGiTMpaeywz3WNuqI5wDaDhPr_SsWyvhKaMaYZb0NkV2HsPb-xgMY53PhpUWw2xxX7I9DRFOM6DpLmAnTWCZTRj2KgddvfOBYyRrCjIW-Sj4fUomJ-vWlEj05-XUdrzO83P9Srf5VYFzS_8pFsK0WlBO6NRpCM7rxCEqhnlBk7Kre2wppikUSnePN9-m7ZJ_pzRMPlMkwE27LDFoit5EtRiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCwkE9o1RKfS6CpYeomCc4Zv3iaYykDzBXzHWvuUCbb3zcdT64tt4t1gOFFMr8HgnV74OYtp3B99ggrpJuvod46aKZsVJEOfE51BZCZlga_H_EyFu_x0fD_4gYn0a65XA3CZre003IwayNHv_2DjPdkmNSmDphvvgpKlu2_UOY-TX1-pZLM-p2t5QGAIDTfqF9jmMAxO9S4BOLfNkhOWc4nfRhK_ZdcbVHipPWg_hGHdVYQQ9jvDClT5wTs4mhh5AEBHMEx5BhxROHy6Rfch0NE0CkhGOzB1GSxZFMnGPSdlRyWaXeRz37NSSI4kxq8pRy-rQLawQDl-sESCCLFR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG3Hz6lVmz6TSXHGwtbKRo0zFdAFRAd-iMwS_iSPAq0fhDv1IjRtJeTyYcIzKS00DRLEwyb_SkbD-YP2fGfuO4JAgg4ZoYPENVxOkXFo2973xKd3E9H5crWEeDnpxGjmst3AImimvCeL2A7NvcemdlL-RqjNGc6Yw2b3yrRcB4Jtw1ssQo7JZIAoi6okZytuqi7Nt8HGs_q77KI9RGFKgAUYWKntRrp4Gb4XPfBqeTVLCAmN_-AznabnwIG7IO_aFDwo7fxU-6ic3A4_AxioqAaI2FbDOnML1FSjKAM-1vTSL95Yqt4a5dftB3uSIG2ew3BB5w8HUCdVnWwpOgz9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEDBJ-oCU5sYNjUMVTnpujoBWo8p6uX_kAObK4wZK3XnMXFnO27FyJKtyrH5t6KG81Vwm6-tczWxDHZmpQUazo_XemFxODwvYCN5D-g9T0yq5AYo6aV-t3mOt5Fd4iDPeai6Ny6lxYONGtN8uD1sTgfmaJ8_Ad_-mM6pdF8qk8HJmMu-ofEonBiQ6UinP19GYOAF6qTG448mfWOMShBI7JdnPXDkULklp78C2LjxxjkWiOrFnUnHJRmJGy_rnhWkHBGKQesMWi5G9XjZUEd82Z0ZxopH9Ko_Oc99PJZl-2G2d8ffyBfL40hx9VCvrzHk9nZeKUSl3VJDYZUDp8aGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTcbQ4TUgguaqMMirVPLTOz2oa9NaDfjxzUEUdzOL_dvCpy7rWHtLWHNvmPpc6qalgNvIqOxbC3NSLPpYXRVcRQx7Bk643izIIqITUwg5GuZVgcVFWg0R_6PSbIklnvimCFS9CNAPw8LPNKYgxfnZLVPtRlBM4XTZ0bkEbt7M9_Q1x1dSBZR2eHyJOMaikx4qLlr4DL973b8YtkFf_1ZbUJVdXI-4YlW7vWkucSbV2-T7cOimzZy3kBASuHmfIQPPmr9tdKjCrY3gjOC_BaiIG84A_YQy3If4aNzUX0ea1EX9BA2dsxFdyYMXxAE65CERkMKixSaYnHlQPX7GdSlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7NFXvRGolZ5GS19B9n3z8BL9ogLeJb_uxZaqw5b_mrdXTcuoqv80LKw0cLwKo5z4ND_Zhinc5Z6QkUrOKhXsbi2ZwEeqbGqa6Q15fTrkolTFC3EvKc4l6SiPWUYxGw-lFUuBw8zTny3DRR8Uo1gtOifNvMfddt7Q_2XzGhNbl-l6Wuh-hryhwJAA9mE66L_n4KEiYnR7sVmKxc9c1IG8_fMF2oSWCtFoccYDeKuhNDI3JWNBoYfgAHILWS2OJDGWwYK_sYFKIsOnFwlfQaNNQyQU944TsrX0Ro6BAS3pGNFztmIlxpSgUcXROH1ZM_n9qUPgyJ-aXV2xcydIFTbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2TixUH4_rYXIeBjMVD8zJVc4kNxJvpY1wVTVwLNAPDQLZT_bEgd_DidmoatKJmJhHn5462kOh64kOiCB_Vol00-r7Wl9rTJDKvxCPaQAKPXWbhC9vCoUPhBcDzab43S9UT7la0qI5lNilwInRIwlwStJOju6xSEe-U8wiXPN0n71TQatFw6o1TBcaafnP994dmMtgwuzqPjF1u37pmX2doBq9n7XDFPiXCoQbZf1VNC5_YyYeKLHoRXEqhTOhXlPskkpOAnSIKMl6UAl5_Q4DeeIBCMxmkF7MdJSz8akXbbwmKyLvi8EyC1KPR0VUeO0zwbf8aoh9lZfw2zz38c6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-BR4sYRMhtvM5i2ncle5jLQJ2cdfp-XEnlK6thXwcLmwDHu1rxPIg0v2JKjbn15Y4ku4dclasmG2pVTz1IGgqqwGDH1uG6NbM0_ccPSvkR4RA_Jh07NGgfPgN5oMxSYhECJ6DiuAcrBppB1qxz3wRGoYf_Ysw5xN2olTPUwR3z7o8kNj-TCfC3ZG_myfeMBZO-p4wDTLVYe5vJYggzZc0fUk7bKweIPqqX2dOpZDkCvBFdq83_uqsWRCVTpHT0gzruR07Bei_0Pys6g0M4L4DpBCY3kMnP3KPSud2qjMxtVocgSuniInryNWGB8pQUcfwMVlqlzMpl6mvny25rEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLR1OtcjTSslbO6saso_jGleUf_KDlMQUCBUGrpkTOPp-fH_dlIOjJ6LZBe6ELFXxDOIODmUiwBUKDQRYY1zZj2qtZQMStzhqpMonFlM4IdUIoydNPWPIF2Pu0NmNuVHxT24_jf8kSpJIg4oVHNLZ2nNhBc2I9nnPJEWiusxo__JC2DRhmk1iyG4dtRTlLI-Vsvcs0EU0Kj4F68qfOcUkHlkxvD4NULvRSAO_W0-jzYpDWPkvXYt2yXyCqbm1lrd-COOVDe2z21trxqtvz9-07MBbBymb9v4fz0IYGkBfExxAkDEswzyPDNX6UVnQMqYb9ZLPrLMpBD2E6ubAjMgww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2hsEQopD1xHqFTtWobsLdXPun9bclHcwRIotK8lSr7b3AJm7NZMyqsLvJ_LQgO5xuFYgfhWB2zcS6ilfeDTyP6eiHjXQkgHvu6NEvduEdrT1Y-BNuBhndbSdFH9-B89TLeJKKhNRX1OFcXZFC1iqelVCdGEfXVzmsRYBbHDLr6l-yfVxjYkjxyFmEJoieoaH5qkGYA4hQ3jaHDJHTlN01Au_cdlrg_Djcy_8in3X9_xiWYEFVhhIAr7y0Dfv8pMCs6JUxcMIf6OyB50kYZN8yeFXXfEtlbPjjDV4vuYLyGrEZT8slAeL6eIxISkEYHaD0hfkvE3QdLWo_Ssbkdsv2bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2hsEQopD1xHqFTtWobsLdXPun9bclHcwRIotK8lSr7b3AJm7NZMyqsLvJ_LQgO5xuFYgfhWB2zcS6ilfeDTyP6eiHjXQkgHvu6NEvduEdrT1Y-BNuBhndbSdFH9-B89TLeJKKhNRX1OFcXZFC1iqelVCdGEfXVzmsRYBbHDLr6l-yfVxjYkjxyFmEJoieoaH5qkGYA4hQ3jaHDJHTlN01Au_cdlrg_Djcy_8in3X9_xiWYEFVhhIAr7y0Dfv8pMCs6JUxcMIf6OyB50kYZN8yeFXXfEtlbPjjDV4vuYLyGrEZT8slAeL6eIxISkEYHaD0hfkvE3QdLWo_Ssbkdsv2bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLBteqmAbIJKGL3csrVzbsV54k-Wyq80el6mM3D9FJI-M67Gl1tjHrBNfBO1nU8J2ArNoopN4bl0KbFRYvPJwpyAThozO2e7SklWTwPfVDxOSFH94LEaDw_YtmXNCz8RLjOUhz_hJOPOXOLTxqTQAJWMOE1sgjcbE7hW5ViiNtacScNqS4HX43Rr8dPjC9DsNv2Bi5FkQs5lrSfVzQ4093-SDy14vB_ro062WLgvyb_wF6FiPf7VZyfFnwV7D5ChsyE-a9zCm8EdygimuD5xbkiXWsrGOaskKW_U4KwcVvBW9dT2VaJqHyTZwUVb0vcXFLHnvlB5-34MeyFOWIYcqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=BatjpRam30fxFvn4gPZHa7HKFvljjVJsUcG4CiLswyUCYIbmJ0ie90sX-sgv6CA6Umi4i7WDvKPl9DoyYqCr3vjHAjye_Zrp2-EtiNIVdEOSG2yQBi_WheixAe98be4TLXhfylve3hamsnJVigzZQ7cDuvyBIsjPYJ0O0cooVPtS8e1AffkuPaXfzF253is4GYhAXB704G6RHCplvYLucPCnYLFAo4TbIAEnMHeku_2dDCRZ6W7zRnSV9C2m09Ivppyfzy5IwkFy9CpqgCap81xDImfVngml1KD2iQ1wVkSATGDSt1YAEgX0GzD2ZNjROzAQrsqcKIC2hbV53pWbPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=BatjpRam30fxFvn4gPZHa7HKFvljjVJsUcG4CiLswyUCYIbmJ0ie90sX-sgv6CA6Umi4i7WDvKPl9DoyYqCr3vjHAjye_Zrp2-EtiNIVdEOSG2yQBi_WheixAe98be4TLXhfylve3hamsnJVigzZQ7cDuvyBIsjPYJ0O0cooVPtS8e1AffkuPaXfzF253is4GYhAXB704G6RHCplvYLucPCnYLFAo4TbIAEnMHeku_2dDCRZ6W7zRnSV9C2m09Ivppyfzy5IwkFy9CpqgCap81xDImfVngml1KD2iQ1wVkSATGDSt1YAEgX0GzD2ZNjROzAQrsqcKIC2hbV53pWbPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=hAM2FWjiJEavQXdt1LcPZBoSk522S2DManHX-SnDpxZCE7IDQWuh4aS1bpCtvjgazlBIwD9zACifap2gl6zgSiCZCY18ga95fEGPweMeNpcmte4SDBBLkaozaEIp2zPAE0yKC9RbhBf5u1zh-QdaV_T8Ro2kmbPpa8ZuRV7pGNqk3q8_dYWtcSLinKlsns-cECghQTvqX25XrdbWAjQtQWqwzMF7duhaiI7krv1YgPwvC_tqb9qMApqSVNrhEEvHwmxIIst0A3z4YK1-_lQULUOxp-3Js9l_Bp0lpleiU28RjmWvAL_d4jAiR4XQr5SUJmYW_o682IHev6crUEiizw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=hAM2FWjiJEavQXdt1LcPZBoSk522S2DManHX-SnDpxZCE7IDQWuh4aS1bpCtvjgazlBIwD9zACifap2gl6zgSiCZCY18ga95fEGPweMeNpcmte4SDBBLkaozaEIp2zPAE0yKC9RbhBf5u1zh-QdaV_T8Ro2kmbPpa8ZuRV7pGNqk3q8_dYWtcSLinKlsns-cECghQTvqX25XrdbWAjQtQWqwzMF7duhaiI7krv1YgPwvC_tqb9qMApqSVNrhEEvHwmxIIst0A3z4YK1-_lQULUOxp-3Js9l_Bp0lpleiU28RjmWvAL_d4jAiR4XQr5SUJmYW_o682IHev6crUEiizw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=KWzj6jk0k7TUK-KYJi8rasoDpabZvUOwvPk5quC_YN-1re5CWNrRmicLyq2izli0iKco3mrSHBFLMM8-OxuvwYeAFGTNB5FpBLJrNyZ2yEGTxRza8wRSQtEUslrWjulDhcDDMljL1HwnNAhQOOH5Hjp-dS8P5NxAQapFKCYJjYPDYkGg55h8yA65owa5CHaNGFEPUjYWNwUPgxtppMB9JtTkpyzP0MFknEX4IQv5QpX3XxsrDR314Q1by54LA6Kgyl7RqUiZER6FV-6lheostUjcNEZqXmVnYqyTwzIp2WJpzyhN7ZcO5tAuoUtAnoleqpUNBX3ruoQUnX4jxuRzcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=KWzj6jk0k7TUK-KYJi8rasoDpabZvUOwvPk5quC_YN-1re5CWNrRmicLyq2izli0iKco3mrSHBFLMM8-OxuvwYeAFGTNB5FpBLJrNyZ2yEGTxRza8wRSQtEUslrWjulDhcDDMljL1HwnNAhQOOH5Hjp-dS8P5NxAQapFKCYJjYPDYkGg55h8yA65owa5CHaNGFEPUjYWNwUPgxtppMB9JtTkpyzP0MFknEX4IQv5QpX3XxsrDR314Q1by54LA6Kgyl7RqUiZER6FV-6lheostUjcNEZqXmVnYqyTwzIp2WJpzyhN7ZcO5tAuoUtAnoleqpUNBX3ruoQUnX4jxuRzcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDddOYjhOBKiRlOVHo24SAer0R3ZuDhzeKPY_UoYTdnuXD3H8z9Z1qgTsxO0E-FslVLo5K-mGKimfiUrkNYg84IB30Oqi_Oay9xdsTRYABzKrRq_Niexemp1rHhDUj59lP0t_Qe1jI9GSJkYj-8C_RWQso6DCGl0fWo4uGnbcNgjsD1wrBI-JRqOsCV6JPenoci5YAkvGDNocz4CFNwPE-nUePU-oJmL9yF1nYXLkC3NL7tlTRT1k6Mgwpcu5Fiesy6djJnW1MIBPs5OiKD_MdlUHaA2L03NPaiO1OXm1-OUsKFjvEp76VMpf8KfXdut6BHhOL6jaOpiomnB1VjqEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezbbq_xBGwkIXuPyI4PoDV0T3h5gkhOCIk2cyY4rjP-j-beNCEuXPFj3OyuktFj8Skkx1L55WJ_JA03dU4SQPLyi-HABxq1S2iCp1sCCX3TPoL7076ypM2IGbdjTIjqmmow9h6YWV3Gevx1SV-C93-GguLOYYOOD0cGATQMmkxPSnwIcetyYEVmVUl4KgmSmUerbURx7CRPaBizjooqGXTmLtujegjsA7pZ6mXmaoVlwNxImTVBmx1r38b185fO7ckOijOOrDsZDuraHq0b6r-URvnvmXbjV45YYpnlH5kwc3DkThriYWMPfxU6UBMPOUZODmEtSNE7goFL9jvvS8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=sa85HC5jcu2mHU86ExA3FOdg6D35H9Hrqg9oRWR038luRvUmEeNHZg2xbfOhC019sGGLn6X8lueX8rIP2pGttqehu6CabbCYf99UL4gR2Mnp3BcxED7JLWhGfqvyHir1jLOE6qjwHP2B2_RbF7nxdw745MR89YjTDaptEp8KRsnjH8wKlzx02tmRZitVXd13uqZJq5-XodiqmxsPiTS1hVaTIi-laoRBQ_BZSxdskdu1lAv9peBO6ft0UXPskO8vg2RDCnyvKsuP3RV5-UlY-T1FWXCnVFjIrcNLd-i5jnKP3KU0K6aWRLNt1ODfsmAVaOYblHPxFiapIgdHFtSzhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=sa85HC5jcu2mHU86ExA3FOdg6D35H9Hrqg9oRWR038luRvUmEeNHZg2xbfOhC019sGGLn6X8lueX8rIP2pGttqehu6CabbCYf99UL4gR2Mnp3BcxED7JLWhGfqvyHir1jLOE6qjwHP2B2_RbF7nxdw745MR89YjTDaptEp8KRsnjH8wKlzx02tmRZitVXd13uqZJq5-XodiqmxsPiTS1hVaTIi-laoRBQ_BZSxdskdu1lAv9peBO6ft0UXPskO8vg2RDCnyvKsuP3RV5-UlY-T1FWXCnVFjIrcNLd-i5jnKP3KU0K6aWRLNt1ODfsmAVaOYblHPxFiapIgdHFtSzhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=taSnXuMbcnqT5CMh14g1lSAl9ZKxv6DYAjB35Ksz5Oey1qM3Fg58KPf0UJ_YLypPTB7ZqqBMkgenJlWNWg2W0cw973e5jxgLa-VJcfbyaQpz8EyaGBA8_3JaG9eNfyOJ8IfKp-l_RVsUWuTvgP1DCiwnJZ4DQKZfmbstxp_dxO10XyoBed6cPJXYtgX-tkZJEEXnW7Jp18Gpq7AYW-EokeQVdozJL4SA6wbFhiHdula_UV8INCVrIA_hSEO6g7lHGuf6waOWGVuGPcPuumxZCosVwDRLg39WL96cSS22ZHqQTgaLcNAIkX7rW_ILzggBqjQ9VS-VYKA5Fplw8ieCUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=taSnXuMbcnqT5CMh14g1lSAl9ZKxv6DYAjB35Ksz5Oey1qM3Fg58KPf0UJ_YLypPTB7ZqqBMkgenJlWNWg2W0cw973e5jxgLa-VJcfbyaQpz8EyaGBA8_3JaG9eNfyOJ8IfKp-l_RVsUWuTvgP1DCiwnJZ4DQKZfmbstxp_dxO10XyoBed6cPJXYtgX-tkZJEEXnW7Jp18Gpq7AYW-EokeQVdozJL4SA6wbFhiHdula_UV8INCVrIA_hSEO6g7lHGuf6waOWGVuGPcPuumxZCosVwDRLg39WL96cSS22ZHqQTgaLcNAIkX7rW_ILzggBqjQ9VS-VYKA5Fplw8ieCUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=eS74ephkPYt2RGGkEpmNQIdrKqoBJa-PyOUbXS_y_QfG4sLw1otSWrAXADv4lg75OBm6IoZC1Fj1GbRmSAQVZSRIl9hLfNVae5g6lg4dLPADBdIGkL712R8Qdtz0t5C7FxqTVaqFbLRvR1MrcrMU6zeCQ8bYikGvGEowjeby92DYp-jopg4UMWxJ-8qbXZAyDqnpZCO3HR3-cJIQ1f4JwQgxrOx464EsDbyA856ji6GCZedkmsyNl0QaLHaX8g7V-7rdjZ_H2OnBGyM9EpcrN_c_MuSYdEf2NUPwsD_7_G2rGb09c0dxnT-BN6Q3YMWEK9IL6gI5S-MAxzQ8-2Lc5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=eS74ephkPYt2RGGkEpmNQIdrKqoBJa-PyOUbXS_y_QfG4sLw1otSWrAXADv4lg75OBm6IoZC1Fj1GbRmSAQVZSRIl9hLfNVae5g6lg4dLPADBdIGkL712R8Qdtz0t5C7FxqTVaqFbLRvR1MrcrMU6zeCQ8bYikGvGEowjeby92DYp-jopg4UMWxJ-8qbXZAyDqnpZCO3HR3-cJIQ1f4JwQgxrOx464EsDbyA856ji6GCZedkmsyNl0QaLHaX8g7V-7rdjZ_H2OnBGyM9EpcrN_c_MuSYdEf2NUPwsD_7_G2rGb09c0dxnT-BN6Q3YMWEK9IL6gI5S-MAxzQ8-2Lc5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=kUlYnTU7fGj4iblCoAkOhzXNTVjebgfnX1DsNUnL2yhGc2RProdS4iLeMZb6N9oCKUSN6059ekJhTN9jp4uo-SqY3LoaY9MZ3qNsmMdQy76G49jWIMv6qf89X5hoaC9IU_Uw7o0reF-dIc91smO3sLzivNm9VSr7_-Kw84AmdscS1Mt_GayL50VhFeWD8bqbcnfIwk902YuPGGmHpf8PxzeJpmO0_cXrrMfNh_2ydp77aw5mzcDtrXB96xDEb9YAVJCu3xaLdkgcgEwocLyJecOv7mCZ0zovmWMypcu76iWT18oC3FZneUF2AXsNISNG7JFDiHLardsij0QfTAsN-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=kUlYnTU7fGj4iblCoAkOhzXNTVjebgfnX1DsNUnL2yhGc2RProdS4iLeMZb6N9oCKUSN6059ekJhTN9jp4uo-SqY3LoaY9MZ3qNsmMdQy76G49jWIMv6qf89X5hoaC9IU_Uw7o0reF-dIc91smO3sLzivNm9VSr7_-Kw84AmdscS1Mt_GayL50VhFeWD8bqbcnfIwk902YuPGGmHpf8PxzeJpmO0_cXrrMfNh_2ydp77aw5mzcDtrXB96xDEb9YAVJCu3xaLdkgcgEwocLyJecOv7mCZ0zovmWMypcu76iWT18oC3FZneUF2AXsNISNG7JFDiHLardsij0QfTAsN-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=XH-PC9PMMiUgIlR3WAQi_4qQ0EfPEYb1s6RQEwNVXcys825AoloCwZEqfcKEpjVkwO8JqjI7207LueA0Rj_lFp9diGyZ3Rs8g8q6G-S6EXWVtZS7_XX7EEd8V35s6RSZyK_P1umzJo8IVT1ax591FkQrkVKfR_gegKoh8qvadZBLUQHk-NCEOhOsSqnlT0qkM-r8aJBpKfSDk0UNy0LplLVKUaI7NQ1XzJzIZuso5U0qa39OxtoeZWK3S38kuimHpv5O1YIqcQXr56eW32zZUCuLP0qWNrWL_AUqSN3QJpOnNhUy7ofJR5Pkmm4bhs7o1aRJ4F_2KaZVSUR8UneCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=XH-PC9PMMiUgIlR3WAQi_4qQ0EfPEYb1s6RQEwNVXcys825AoloCwZEqfcKEpjVkwO8JqjI7207LueA0Rj_lFp9diGyZ3Rs8g8q6G-S6EXWVtZS7_XX7EEd8V35s6RSZyK_P1umzJo8IVT1ax591FkQrkVKfR_gegKoh8qvadZBLUQHk-NCEOhOsSqnlT0qkM-r8aJBpKfSDk0UNy0LplLVKUaI7NQ1XzJzIZuso5U0qa39OxtoeZWK3S38kuimHpv5O1YIqcQXr56eW32zZUCuLP0qWNrWL_AUqSN3QJpOnNhUy7ofJR5Pkmm4bhs7o1aRJ4F_2KaZVSUR8UneCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=cz_d4XKUCie8aqY3RCdTKDCf8narP8CyquXDVmGuUJjJUIF5WtWgZ9SaleRauRnxrPtKydxR1l1cekNRrPmDN97zFvaCJawbrrdG46n0BRFT-f4Wxru26-Nebea1iu8WXnMl-RDPHTzpYJVIMSFyTj1CLUFTMUxYpnV3iLLw5KjyALXBtpglE_ShfbazCCg5JLHO3OYuoLGznLIWiu9-8VWryJpDIXeS-deujAWdY1ilyVB158vTMUElSjd8To-kyviXtLWa9wk4YxWTb1aNLdIstVxVMEnF_eG_PRw4IS3EJa9_NZqMnG86PnMe9h3fjoJp0tgcOP_Uz60Ap7utSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=cz_d4XKUCie8aqY3RCdTKDCf8narP8CyquXDVmGuUJjJUIF5WtWgZ9SaleRauRnxrPtKydxR1l1cekNRrPmDN97zFvaCJawbrrdG46n0BRFT-f4Wxru26-Nebea1iu8WXnMl-RDPHTzpYJVIMSFyTj1CLUFTMUxYpnV3iLLw5KjyALXBtpglE_ShfbazCCg5JLHO3OYuoLGznLIWiu9-8VWryJpDIXeS-deujAWdY1ilyVB158vTMUElSjd8To-kyviXtLWa9wk4YxWTb1aNLdIstVxVMEnF_eG_PRw4IS3EJa9_NZqMnG86PnMe9h3fjoJp0tgcOP_Uz60Ap7utSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWMPuR9-PXLp0DQY_Ymn8iqfwL51r3fNnC4MiRWQYSTKh1Sq_8F0DuhNHgTEEvNIfFjfrfqbAfxRyB7LqQfx-VbjguY5uc7FzkI6jRzcBLM1a1zGXUJz6yH83Vwcm-qg_34zTbD-zSJMMglu4mdSpmX0i8HQYcUGWq13ZpNpZvkfhrOZfsOZrVVVAPeOvEn_wu90A1gXqY_fzMviP6cpNPDb1HVcZBhWFUqdWYUdtH2DUjdQV75hjyZxO5xyavzro-qYYPopDPIu_g8QkqN1PylyHzIgBUl5H1jo0rWKt5CePOehB_Rwwf4lEnRyrsEvZbltF5T6Nj6kkIVBXVLQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJw6eBfnByB46YILiXDdfLCpht-bd7rSJuToYpRfUT0EnJGAZJDFUKqEMrZjGmBKoLOYmni1GTnY_DTumolJ3TxC4FRQ98vzyI_j5uQVFywAijjpRPheoFQ1e7K9PEBhPeM-5wk_FSMuY7c2N6UWbnIMpw7mYBvOONZSf3iD9B0vBTbDQTPB4YtafepEtbE3zuSpHL9MFi-5c8Caj-Xvu0TZkdw6Ll3FYo0w-tEoZejJJXB8pNTqX8plkbs-s1Lt2yKMK1PwTKz__Pw50XfyHGmqyl6lmO7p1B8XoOc0p3nT_i9KKGeIrV2CQj81WXvd_2oaMiENCY8JnztbSzlgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkLhyvMGgEcxd3pCMpraF9zsykGsp6i9yO2X1VHMcW2PthNUWrDr2scQWT-N67DEKby3gFgl5Flw8lvyl9tiCiN3mO0EZf6gCMuG7QXfcvy7W5yKcX1ErlDZ6QMu4e-325PflBCKB_ED2JB73KHEKivUpkXSgil7Y8Fxse6pWbn42oMhxkfi7rdY2k821rgJ8QJqw39wSQ3UlLRaFoPQ-6Y8ecwZi-lxHdC9Uv_ebT-ald7fiwVfBWp7l7G8IUggE2NvR3thA3NeIeW2-v2gjcL1UIz0a3gJs7I1-MLJWXWL6jXzyb6BWCnYSEwzNc4Abisl2uC4QCvsYTXoB2V8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbisL7b2U4M8Yx8V-bdJAUCWltsIsFaLhmkMo7P_yk19e7qndwpEY7AmpPo_rsy9a1v8auZR_-08mbHIeRT8-RR6i52MRCOdZmfqT27oOSLxjqmR-xL9FyzEMJB-hf5OWxwfVBSIXqyuhtrpWF7r8x4tX5ELxpurGi_HzYO1uw_72OxpCgrEyY-G8O6Pew211GuVJMK04jXM3ac1oyOgQmJcV7JDXAH6rVd8yuNAibVXCwg_6JQETuR6uxofIOSopTRnWyW-gsq_aG1cOOXlYFdvnLx0TmGp9OT8SiOCPW9RKsP2lJNxTDkW-k-0ap6P8RzfCaOJaGIsmmHToWZbKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6_xSG0AqIoXDRweEcDtwHCHIG2p_eRbgvmysAqhqTAJqFw7j0Gb1JZwD-0zP_YEBbD25gIlxdIHv4B01oIk5TUwdG898-G1jGi60WoNDT--uX0QWeK8c46bJN2Mvc9yDqD_KRYgPjl5CSUegTnn9IwmWKTd4Ab8wPb0sOLkST6CF8JH5Tg3Sh7QmT1bBBf1F_Y_vvtrZ11ArEnHOLRYVL1B99DOfAwyArDev2UFpWx6Y0NO9aRh10S9cjDFhmOmZ7NOOnm_f5B62F3GTu67V2xxM9V19PO2a_5IZQOihgWiRW7KBuFTdDMSw3ElVlT9LZqBjEr2hmbMfTq-gNIDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEFo0mS1KA1pI7xqiB4Qsigy9-JpRsZTaOc9RUFXkrv87tfFdfxwsOB1_8rTacFKbmu0GGc3vHehnVTf3wvayINZRjaBT95jt5crEwSeZV3FIDrHUlrtZkyUE47nZrHDZIaHjtbSyZ5_DGfSXQsXTUp5X4JOzNrim0F_8azob0mZ7lYhX4HJYMXnBFe13iDvHXPWqMFS0nzIFPQYmbnkDfzkhN2oKAgUwfByRNiFyH0-_9DbT-1S8_RxSbkXBaUK4168luMGizX3OxhyE_T_WFjlSPijuj8upc-vvCqtRAANR5cDLiK-TvxSPvTkCCuEr7YFy1rdk9y4KRWzwOCwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWKiKBQtdfLjpZpU_5XRGyDKAzIhXWV91IwCwkkbaUdz5QJF9a_CqQDCu-iZ2MrhNODOD4roTJWejDQJYCGVVOf4DjyWExczybMMBpNF9aMDOaFXO9cF7C4ZYauWom5LTJ-SR5vSKZSva74Wa9kOmmdb3pdEbZ5dvnuTHe2chAmJSbanxbAs2M6lCAH5FuvIh9k_X-3emTH3tPna6m1vzc_HHePAA2tbvX-NOvEcxpwppuPAh6bS-HqEoVAIKziCdsd528V2NzKjtVu4U5AMqdo478xp2V5kG7LmT8gMt-2xOQbPp8htJbJ6WuEFyjOA_PNBLsLeDt245zz9ecK3pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBY33kZjZ2PXZeJO3uG3DQagJimJe5lehHmwPBoMinY-33Gnb9gAGYm2gQ1w0y05-IXKMmB9WQdj6stvWvtcunOA-IEsc_bFohCo70VMuNbfcq0ZHo0YH9mz3nFM1kyS_y0dcF2ZPaVxH2FWlSvf8NZbaWkzuclCKKKzQmkJ1DeJiaQtFtvCKKrTsDc6tj7tg_TNAxLpDDR8LRWreqo7sdU26lHmyCnxYy6A3ntE253pwoKgoM9p7PZitesaPNnmNQbx3hNF6mDuFRv85DWNRSJgE9ZqfYfTeOgoejRykOkFPX4Lb2emWsXL4nva7ZTcOyGgSY0GEEwB5q0nEJ7lmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMdfUhvt_KFU9eF1NxQ0PSdZlJ4BCWIVUzdoqU4Cut4K-xj6c1ss2VqhMuUoHFFsawE5NS-n9VPFqdBB5yr-E5drBF8JgeyWSBiN-hy-uVhYUUst5bSo95biW8Cct8wLoaecR06MFOxeN3k1wDgCRWuAVU_wZrUonTNlTHZLw7hGZoibWy7rPnku6EyG71Ulsg9Bj_6llNolF-_O1gVmIsIJTqdGMa0ooabwqOU0IG3s2k2C4QQF-61pLQGldvbswKj3kR48aYSYKiiFKCXADRxP4hSa_E_0WBQ81Gb2Up5pJeJxyW-qg3DrSl2NhiFk92c7Ddad1CY1iyGHEzBEpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDpytXJe3iwonhhbjmCpr8b3onJq2CY-K505cdzp77yLFhMQ_4IKFtOiqUplMtYwNYdnTCVJuP65NiCIWtdo3MJBoaK7gcZWaE08An_0euiAGiezPB79Y12YgD494VJ40a0oWW0owFjeI868WXwHv3GLxy1vDyD-8jo0qkFxLuXpAZKj7AJKEOoFihMjM2hX-nja1h9IlRaxcVksJo6kUI5qAUUoW9uBUkm0UOMBOkgGW5lo455LAsDVAz6Re6OgjyEDXYRdIRNc0foJ86LRkx-kjl_WykUyTxPQf-WYvrYpkSKp_AhRCk_FowalweFkgAX4kdicN7gzAmBrnIOChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=Tbul4xACab_ofLuCTT-FW0Fj-Qcdffdi9xxn0S_yugJAYFYERhVo-qiFjVEIT4CZBiMxVeIDS8y0ECG6-JI7a6MTcAvcvY0VHMRhIwrU9I3DQpX9ilfErpquBsWX5Fo0s6W6tE6yEtS1pFWYWSgTosCHrvv59g83C-loG5f7ywDA29LfTO2r4tc2ZuSDiI4BqwaF3kZbwtEO7RClsD7eeyslx0e02wlwUITMSjHXvepHSEbDqyPvNJp0FDq-zKl4CuBxWocq_boEGDuM26uy3Lro3x0RIgTLZfooa6bSI_cA0PMgUWVcD0k-faWQdgjk8hk1dDco1DRi6wjwNYpHZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=Tbul4xACab_ofLuCTT-FW0Fj-Qcdffdi9xxn0S_yugJAYFYERhVo-qiFjVEIT4CZBiMxVeIDS8y0ECG6-JI7a6MTcAvcvY0VHMRhIwrU9I3DQpX9ilfErpquBsWX5Fo0s6W6tE6yEtS1pFWYWSgTosCHrvv59g83C-loG5f7ywDA29LfTO2r4tc2ZuSDiI4BqwaF3kZbwtEO7RClsD7eeyslx0e02wlwUITMSjHXvepHSEbDqyPvNJp0FDq-zKl4CuBxWocq_boEGDuM26uy3Lro3x0RIgTLZfooa6bSI_cA0PMgUWVcD0k-faWQdgjk8hk1dDco1DRi6wjwNYpHZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyAk074ozYWoXCUoIaxQ7s8mgNnsE8kP_HDd_PTCxCnwh9sMXOyffCRqx_blMMBfzYFEiQaGq0pTsZdSyuSqbWWS7sgqtFuN82kPP_xxk5rCNTaPQ3NELDb6yb-TDWiXaCl2hy9s3fYYsM2BDhUr3WdqVlJqsVF9UJTZ77hSyn01PlpGedDevYjka4ms2C1V2E7yJPmtgmzTrpCpjW7w5mZsCercYtBv2v9r1gxXBMQpU2rW5AbxE14ONDA7qdUTmxi8aScSimhH8gm_6WNOC4PSUQgXb0HEm0UNG17Qwfr9ev0IEUGTIRB1RNejYtI8q5Dz8U4boVtTtjtFKxjz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKj4BW96eNjUVMQN7onMQBKOlUZwaGAr5unFHmc2ldPOSuyFXZ5WgJXyQ4XRPpwrAN2carHWKZDqbY2Mdqdh4uDDWwgmZPU0Vq6doTgRGxV0TDCrSjfH1HRrDWb7rheWGDVLykJlnzxrXQtzOEeF_wHS3KsL-mUsM589EfwcvrmHbz7rwL-zJkFlf6RhGPoREE4M7DitVgxCIQEbKQU78eEYY_DozKSt5t67FQqNYq81Lu4FRTwCxjS1nbPEd4b-qm5yzBAy-8D2CTqQzI--mgfS23W01Yru5XdluCd2IDrxR8WjbaliLOOeldcZHUBPKmwpu3dDTLofAmEygk94Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2wY-A5RfqB-OJAyPPtfQYvT7nXnqCcw89FTcIUi2BF6SqtPBgu6iQRctpyA3lRlDaLCS-AhPJJI2fQZeMppoOSmqHmGy5-AsmBzulyTcUXudHh0cjm6G4uFiql8ZpOouUQ4cpiRt94MvadyEVRXifr44OGT99I2NIMMzkDZMa8eQXGoR7EFegGSKI5Bjqggu4lvYy9LRrSZSgFG3saUFgbzm7PZkIFGXy-D5dlYkmfNe69kix7PvX9J_9Nuhfpcluem9jof3UHh8gIK2G31sDGcc3s5Lah1wBXM6ZREqYxSogFsOqcvtUwo7BnKLdkpDMRhooSvXd2SsZ-qt50EMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bY-ITi2ktxXAQdO9jQGWZ0pQLjrwByzWXAXbjQpQFGEIJE-6brponA-Q5KbIXtdSpkDtiKBXyE2lzFa-h0z-aFslRBkDTGmbaoAppjM72Jeo6h-k3Q72F4tr0KPxPrvdQx8SrjIQBUx1LNxAOSNZVEdX0bvVac-XuTwGmDs1IOM8H8zrpCIlFjMISSYrwiHr2Q2byCWg5y-cpCMCnQuGORuJZrDbot12c991ljzyVof4ys9JCEnFrLg3602flGHIbqqUhnN2foJcCc7BZcPNcL_y3ujx9NNN6di_xWPpQP5cpQL2iF76mb9qhjXJo4sfFoBNsmu7hHT00N62j8SFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLlWupslJailEkMOHZ6lR3-RiFQu5XjBm2RJXJTgBfaMO0Hoi6CcwsVmaYoQWPY2yjbE5HqC7-33y1PorUgNY3AA-7aPgK1C6eKRTzmAHQvSD0vH1PHfBco59clmcm8N8dcUM72jrcr65fnlV9Ph7nINN3FeA01ww7hXJoXMdlO7dmGi9EiL2Hd87Ai1HFu-HZvECq_YWX9JGXZBKXDzi4y9g2u_Zxu7e_6jpzTsNkOjpNkNnjMKDCfBNh7z10QsvGQyxxpLx9eRnrl3desyvJLkayjyMcqtsB3zzjtQBSG-EECyhQZvmb_aTlCo5wX4vU2scQCkOMNnTsIyt-ZlPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeGfxrMbNWXTXeL0QSV2YESQpkTGFjzzLz8F3OWwS1suyP0LO6nwEu3mSkZi4VZVx6CMBvRmiaeVPAAwhQVmjkp-4RnElx2GvF2C6hK1zo31nRTbIXXn3amIXEdaFLEy6n3J4wYcy2IdXBTcmckG6pTwF_apjZEaUrZtJ_ncLFhQf3uGFtI6JAAfxVPP7hfjrXzr9CoqbrMOf7tWQMuym5PDRYEHx7i8wMfctOpY00NG72jbR1TZ54OEoxs0DdguwzNS5Cw6SMzRG0MgurJZPjfgsEnCKhPHzpaG5Q09RTbj78DSfd2_WKHTcKfTWQdFekhF_NGeJyuVMu25_LlehKVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeGfxrMbNWXTXeL0QSV2YESQpkTGFjzzLz8F3OWwS1suyP0LO6nwEu3mSkZi4VZVx6CMBvRmiaeVPAAwhQVmjkp-4RnElx2GvF2C6hK1zo31nRTbIXXn3amIXEdaFLEy6n3J4wYcy2IdXBTcmckG6pTwF_apjZEaUrZtJ_ncLFhQf3uGFtI6JAAfxVPP7hfjrXzr9CoqbrMOf7tWQMuym5PDRYEHx7i8wMfctOpY00NG72jbR1TZ54OEoxs0DdguwzNS5Cw6SMzRG0MgurJZPjfgsEnCKhPHzpaG5Q09RTbj78DSfd2_WKHTcKfTWQdFekhF_NGeJyuVMu25_LlehKVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=j9FOxyjcwTo0GC1REyexljTfD8AeeePomsxEJNECtxsRWN95_XxuNzg07d1f3CX6c_g5jH1HorFxMXBI3IE7C8yXaEFPRE2A1Mn1YxxwuTRSgAMuU3KaM7UJteHC9-veMUROuG1SzfYisgupSCc6cBM69w8SeNuYKSJB62FKyc0uCZ-tfF9sNvOCtw7SAY4JO1S1-aRgTGBWVSxflQVfJzqG-GJnjt6LlSQ6KSzHNMIOKdOIZtJVMnssHz0Dq2xATbRDgP5NABezZIWbBEJdcAq4GSOKck-yhtf4YaGMy-Q1qEgtXXQq--XyAEb16vAVXjd0llMB4U0Gis6ym2_CfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=j9FOxyjcwTo0GC1REyexljTfD8AeeePomsxEJNECtxsRWN95_XxuNzg07d1f3CX6c_g5jH1HorFxMXBI3IE7C8yXaEFPRE2A1Mn1YxxwuTRSgAMuU3KaM7UJteHC9-veMUROuG1SzfYisgupSCc6cBM69w8SeNuYKSJB62FKyc0uCZ-tfF9sNvOCtw7SAY4JO1S1-aRgTGBWVSxflQVfJzqG-GJnjt6LlSQ6KSzHNMIOKdOIZtJVMnssHz0Dq2xATbRDgP5NABezZIWbBEJdcAq4GSOKck-yhtf4YaGMy-Q1qEgtXXQq--XyAEb16vAVXjd0llMB4U0Gis6ym2_CfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frRY9LQgzqiO5YwlQKEmVNvZU9usNifvCWaxJYo-7DCtqizS95mbVkPDg-vigdOLHErG_2dRL3q8vS1W4Fy5AvBVf5Vba1bX4o9jLXCIB0q3WNC36zRhH8vcpUGTSdIkKTtgq4UcUNfjsP0WF9abNAXeEQSEpKWRLrE-wIZAfj8zPxttgIHNdvsmmp9VB4IpAdRXxCJBmJwk5DzcgsrfZandAjn5QV2bQv9Yb3btpFkOr0Sdtuj0sdPWUzESSScGDIJVn3AAdkpTmha2rlhZXjh_7i_7XZfH5ULVrnV-4F3cMxaiFQO7QxjiD4QLdai8Z5EgWLMCQnSJq-6ymsZjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=XKvc1PymgED-hP1WmAa9kf1ojreyEElK45zBkD08kGS36yLe-lSPFDa0JEBY3GovgKSyme9_QAt9OQKnWrUFjkVn5hqsze7KOjQ44HJqMqrTPb0J8L0sDw7Z8VBPDPo-medR3fuLaesownqDNQIwcHkTdRrVlAUWXAKdIlqLc-4fRua1mH-OhQbUqDapaHNTKrrnADfpHCNITbuce24PFPxQuMi8WMDfE6BSpw-_KUEV72BqITRdOhwQaHTA5r_ECpQh-laJfh16x8ZLQnGTTYKGnj7EkCjQATOlrqRmXpXuL6Bax3t3c3cN-jqWmxAMtBqWhaSXolO2yDNM9qmLow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=XKvc1PymgED-hP1WmAa9kf1ojreyEElK45zBkD08kGS36yLe-lSPFDa0JEBY3GovgKSyme9_QAt9OQKnWrUFjkVn5hqsze7KOjQ44HJqMqrTPb0J8L0sDw7Z8VBPDPo-medR3fuLaesownqDNQIwcHkTdRrVlAUWXAKdIlqLc-4fRua1mH-OhQbUqDapaHNTKrrnADfpHCNITbuce24PFPxQuMi8WMDfE6BSpw-_KUEV72BqITRdOhwQaHTA5r_ECpQh-laJfh16x8ZLQnGTTYKGnj7EkCjQATOlrqRmXpXuL6Bax3t3c3cN-jqWmxAMtBqWhaSXolO2yDNM9qmLow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smRGOQH60Zw0y9rI-fWfLW-OPlGQVqx_ePJeyvaN41fkGZWTI_Fz4kFPIZ9J4q65iXRlRxDg9vsJ-c1PH3-wxqgYBzMyJp7hBJtv0qRr0cMKFC5b3q4EWRspwo1cZbRENn2Ziax6RUtGr8n9N3yva8QDa9iinVnnGL7cHPmMvBM4-vehkhACJoxUu7AwNwIAKUfkF5J5O5YAjbLD2NsMp4eEHmn0CiSVc6dGSA-a4H4IAo6fpGDbPLvOIYoEi-em9mQeHfnoZVLlJ8cPyow7OdazRMzMaPnRm6qwFuk_uL6ult96s6MpaMQhG35PoNXCRAzaLa9-rkMD-8ou_hAZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohRfUjenBbuPW0NLkuYciNgHm1OdNvfVYmeUanXqSNqatfQ7_kk8S9jVC2J0WYERs38HX8ws5l-2q0YLP8EPoekLkoFUvhCFXbo8K3v1d2zZNL2Lfu65DbrqJYGWD91-6ECoDjay2Xour0UdjSSMWSsF6hQ8IprVRdHkNyCLrGtwVipporZumutk_Ogb4fNW3dBLUGTD9aCF5qbR-fX8MnpvXvQnWmBCNPOtxgGGclc4eMKYCHJvDoJoIYeP_m4wggjM6ZHX5kXiMHtPQXGI7ttUVDT_gOGnGjMO4b-VHBHG-xHXEgv9qkjrC37B5TBLfXsorL9eZnGBYcuoo5l3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=MzgtgEkMCTO6IgaIvmPNZntTtg_xbYV69GeJCtnNgJfWeo76FZdWJdpp22pG-ayVKrmwOjappMSJLVktHAKZCdiJw7RxuIehuIp068-qCclKfysLKqRr0Kj73xvc5RWT5zjD3jaU13XbYIYhckJTOgewxWIouIROJilvxiTwI1nfJ70dWMBOKkjNAUHEzgywTt5qabueQXnGmXMpZ6PJz1csDCCoKZ9WpdsHAsiIdrrM5ppHkh-TgQv0_WrRL7nx_hh7-q7QT4co_uN07n5ofhGv6ZdqbsVDlZ4z1w0IN-pmzbFYcAt-bjh7TvqpaETSOPypv1mMIu9w1fX7LjX8Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=MzgtgEkMCTO6IgaIvmPNZntTtg_xbYV69GeJCtnNgJfWeo76FZdWJdpp22pG-ayVKrmwOjappMSJLVktHAKZCdiJw7RxuIehuIp068-qCclKfysLKqRr0Kj73xvc5RWT5zjD3jaU13XbYIYhckJTOgewxWIouIROJilvxiTwI1nfJ70dWMBOKkjNAUHEzgywTt5qabueQXnGmXMpZ6PJz1csDCCoKZ9WpdsHAsiIdrrM5ppHkh-TgQv0_WrRL7nx_hh7-q7QT4co_uN07n5ofhGv6ZdqbsVDlZ4z1w0IN-pmzbFYcAt-bjh7TvqpaETSOPypv1mMIu9w1fX7LjX8Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu0oQtHqDjeoHgqmQZmRU4G0gdkTILzap78iqfw2aASZBRi7FjVQKN4NbKeLkVve4g8sCrjuvKWOB25YtXdG-7WgkwAJX944Mq69ZablR0gllhJd8Cy0A-6jj3MTb1v2ipJTAladZoUvRUclwmwlk51cl7gb--YQOhWP77kS5HtY29RnIKwewChO_LZssWVnvm__FM4JBUDJZ2rdMObc7VmoDwNcWPPLqpxfXMkMVc4gJszJ5xB01zyfYDebneqOPcL27LdJ3zrYD2FoKsoh3ytX_D0VAHL6o49EcL7bUivJDaz6Zph6mK6MRCepBmPChsAYJVyJ311Ouomp7eu5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=bbbqKL4BRZ6wjJXMjs7A4iBxK5ktAfeiebwbhB5CQD2TyLG8w_hOcgza7Xbag6Wog3vzZEoLjG6wHbX-Z4EGHnC7d_m2glAN87XVei37v4jx3rt6h_ryr-Jn6GmFkCKG_89R94_smLpR_bZydf9MNSyaUaZVF7T1qeLmXu59A3WjHAUcuvnDm4Qwm4l_vyVtDgcjLgPKxQCc78v3pg1n--xsl-4vjaqBq6ljkSU7lZzbqZ10QVbIFSuFiZUgCpulKDE_M9ClcBu4wnxf2Cz5HiEBmPH_zXSIq3kgUYXCgKLg0wcNB7VJTu7zS4wONFTfxqAc-7k6ujqBerGz_MkyXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=bbbqKL4BRZ6wjJXMjs7A4iBxK5ktAfeiebwbhB5CQD2TyLG8w_hOcgza7Xbag6Wog3vzZEoLjG6wHbX-Z4EGHnC7d_m2glAN87XVei37v4jx3rt6h_ryr-Jn6GmFkCKG_89R94_smLpR_bZydf9MNSyaUaZVF7T1qeLmXu59A3WjHAUcuvnDm4Qwm4l_vyVtDgcjLgPKxQCc78v3pg1n--xsl-4vjaqBq6ljkSU7lZzbqZ10QVbIFSuFiZUgCpulKDE_M9ClcBu4wnxf2Cz5HiEBmPH_zXSIq3kgUYXCgKLg0wcNB7VJTu7zS4wONFTfxqAc-7k6ujqBerGz_MkyXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=W4OnOpkQnYrsiVpxUN4u3twRzPz0SpZ8hE-AcTYshrynlwC3EyYTsbrxXpo04gFB70ZGO__RKfFkKeRlByDIZvqZDtML4-hsBuJSdhl4_p2Fwyf3Pb1exwsxQCORqfZWnlvSsYpzn_tZATxlxNxUeRojwx46Q6c7-P2rCzYVUiKUl8T64o8n50XHjjDU2CP8FOXwMxEnmWYdiRHMWa1LMchS_xloJBJSxtmJ4XzI8mbX_u18GsZIU0tStz7_gf2pxlq7lVoSh7ppldXHBrSania9w8qpOG0-tawq_p5as7xpPWr1b6BMhMAMEc7l7oPa47XoPhOLNKHWAaC3cqwr_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=W4OnOpkQnYrsiVpxUN4u3twRzPz0SpZ8hE-AcTYshrynlwC3EyYTsbrxXpo04gFB70ZGO__RKfFkKeRlByDIZvqZDtML4-hsBuJSdhl4_p2Fwyf3Pb1exwsxQCORqfZWnlvSsYpzn_tZATxlxNxUeRojwx46Q6c7-P2rCzYVUiKUl8T64o8n50XHjjDU2CP8FOXwMxEnmWYdiRHMWa1LMchS_xloJBJSxtmJ4XzI8mbX_u18GsZIU0tStz7_gf2pxlq7lVoSh7ppldXHBrSania9w8qpOG0-tawq_p5as7xpPWr1b6BMhMAMEc7l7oPa47XoPhOLNKHWAaC3cqwr_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhY-11D8Vv18pCCW04P6af3mfQngvrqDLKTA9RMcwnsVoHue1PpeLYU72Rc_j7mfqmpyJ_32TAElrY74s5sVe3NLgmePvL4ILYdSfa1Uaj4XVvzOlLcT5AYO0SbSu9zZQs7Xb3xZYOHN36EBtHqmm8Sd6i6hQiGiXcouzNFjnpQo1tXjFPJPQ9m3suYQ_71pYUbTxdgswnvrnYDtIWl5iOikxjyR7wB0FkWdTUJBKJY5Nv6vUmKxTO-H5-Q6RK4Eezmr-BJr20tDMcvngbwyeYgWqL_DR1h57qv_ZCUW_xdSR90ID0ppYLh0SLqr57y3Lm26UJJlB1BObHAuGaRTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=fjlbYLYIBAHAg1pbAnkR-SywpT4lSUOHRSlN_EUgDShTS_IFElubeHu4ExIgflVi7wHhVceWSoXjcPPhh9jVGRLUgngF9ZPJZjxE7DboxQw2eBfbHf9uDkgk5CJJ5Dd13mTYZYf9sc4fLNXPdI4-nPGsmpM0FC16BQutDuW4rHiJ0qUYMkNBGat5PPUPxKJsIwyJK_N5eXCeD5Koi0csTFsdUb5HOXSRt3d1DRkPgHTljkcvfPOoJ0OyajngoPIQPSq8BT2XhD7qtRmvoYMmTOvA0IOLNVBUmBPadl0iQ4ebkPzb7OIcP5j4A5ZaKCF4rr15-qm0Kxx9O1Nlpw45Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=fjlbYLYIBAHAg1pbAnkR-SywpT4lSUOHRSlN_EUgDShTS_IFElubeHu4ExIgflVi7wHhVceWSoXjcPPhh9jVGRLUgngF9ZPJZjxE7DboxQw2eBfbHf9uDkgk5CJJ5Dd13mTYZYf9sc4fLNXPdI4-nPGsmpM0FC16BQutDuW4rHiJ0qUYMkNBGat5PPUPxKJsIwyJK_N5eXCeD5Koi0csTFsdUb5HOXSRt3d1DRkPgHTljkcvfPOoJ0OyajngoPIQPSq8BT2XhD7qtRmvoYMmTOvA0IOLNVBUmBPadl0iQ4ebkPzb7OIcP5j4A5ZaKCF4rr15-qm0Kxx9O1Nlpw45Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEvsLqeAHNfB8wSZOzwr7qK0kiAp8qUX9Qf3wJ3NpUA9ujetg5qPseFI8H9sPoRGrNGeF02FTHc4vMEOTG1hxvxr7CUXQ79pVn9TcObKXjYoPeWyGNYNfiMOlmPQcTNjRThU4Wk47cLJ93FWWQXpaNpspYWZrW5ky-0Riio0cAjSqKq7BCsWqK2HI9YjvLRalNpVVWXwEFlXuFtXkws-03lHl9mjrIz-e4tFH251qEFHEJRu9bKjI2JIpQrQbf5yRUzi99Wy_rqgWMOEXakMNNAuDe9zz-_sAnJiqBlZqUxPiFfN25f8Y50eJZSkIJR7Fbp0vC8t9_eTMIeJ9Sr-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8f-bzlH6-raIuz48H3HpUIecqyFk_oUpjm37bhtnoNyeN6x5hkezFSrJU5p4UBUmyfMWbM2M499s0xxvfguqYj1R5rJQ-4zMUg686d9Jutc_GV85PK0p6ULhQfA5HMBPNAd7lSobFBeWjafr-B0gPM4rVC1b120bRzjojQzZFF7rESH-MDNOp9KjTh0fYXqpIpp3sh0JEYL_3Fs2OfWU6JLNGCklv3TOp5u_WwNo8UVlRYjZiQKn3h-XJXgJrRzJu_NOVELrAUSG1oeG1naTwtilyB2GKIVRVQeqkls9LQLMsucsJBl8STq0Vn4g4MMNKWeJO4ZgOl3lmtFC0ShKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDPiJZyUJHzkVMvLURClOginabHCO1xKoiOBDSCWwmJy-OC2OE-tLA142UAg85QXFHP5mLmcoh-N5pikv49Z_Qib1hxMlH67NljXr3Uru3dwuX3VzwkQ4iQw9C48nvDtyLWhXoM58C2vRsY7e7S1u-pNvzvc8gzUuzGROX0Hh6nK9xPDh-n2inup7nOkWTakIuf6_CMVaU-1y-rThoHYpHjC1vtwb9Eu_kBK73VktrpMshsxSO1hmNOZG5KeeTGgC6Sd5p0ip2x100KGyFf4xRlKynhUKo469ivU7NvrtyBhiSTdojLZ5Af2JuJYLURZrcZSFxWJXkdnRYjGsh630A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKTBQLn5m7JFqP4UB12k_qo_2q9aTw3I6v5XnDu7bkWoEHzf_1uL2pc41NrShXLW2Bkz17NCguyiIr4sVU5dO3hAfGdJ1Z30cUdvW0g9gh036RJrs6uY9ldewS7j0UVs0nTOys0TQNMA910fZxzpdLlSz6v5GkPTzRlzsiYIJaSJukqKtz80P8kXL0OcrXEaLeIEeV5_cD7esspuzj8wbnOABgPVhRX-o-_rueXYZx-hv6liAB7_fTlzPHEyE-dJ-HA7reCpv154XhGnC9cAcyPogmzlzcQmthf2JokeKFNJmU2A39w-zYGIugb-Flbq0wYtKArf3_yvbAwTvGWvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZLZ1Ofrkz6R3iABCTW4EHXDex_07sOeNY2qyS2F7jFAztj_xMeTvoGYvbvOAjDhzxap3rAW5JX5Kha8ycvvdbWnGiDg_ZwL-5e1b70i8Y3g-hVLNz-zZCNM0NWj7y9-QaAOnitB_HNs-lSCCcFaC4aJD425kIr-VZGGqzJW4dgKVrzihZbvjkSuHFha3uSCob3424CFsJl10lB8L4lcrmvaaNjaSKWMMVjvHJJffZkG45BHVBW3e-hlZK0mbWNHcq45i7zh9A_FnFrH4Ty9XREur155WwF1mfghxhwgD7Fk7CnEfoT64U8a3S0Z2_w1x2KJF2EwS7xKQXnNx_D0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
