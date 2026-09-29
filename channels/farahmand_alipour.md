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
<img src="https://cdn4.telesco.pe/file/j34SWsMMNKefLB3l5HeGNx17rMvueVLzFfC3CwHbpjYKBRVpMEQZ0SV2iEn923mYO0SI3SHJjTfc61byDDq7FCFOpYKtLvqIXIPWMMnwh22GF9UuRTA7Hg9VpAjrePLkoEI44JY_X5hd9HmhwR1_UuFzF3HSxRu7SPBBlbLhNUR40h2dEKow6BDIb0Ytj00yWyGDkUGsWG0KjiySDoOSzfzTTjwcA8SgLSq-OU-djthPc_28knxUg0vkpRaig8QegXP7CtPm_YEqVL6MqeHzv6Jl381fp6xDT1Sy0exyPMucpSVgG4cmbFo_uPmdgB3lwy879aivTvSubp8ZX86SFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 12:18:18</div>
<hr>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=oAMkPH_jW-HyV82SKxPnQROJzac3XSsMp2hk3zxTNimotZTJjJq9LtZbL0JryBl3Jw_mcEtLVwfeXfxMrvWh9Pl3hs7jisjg3XrW9gNIVZ3OqGg5kMKdU0zFVhrSD7c5vipEw1ID1_uzgScP7b8d7xEqOP36L8b6dBhfu4wSOSlHL-7qVTiawK2l5276smkRFRz7jkElNyXPIe_UeGctONIx_BqM0u1_PjYd6_j8fm7oEe1b05n34t0yJ4yogG_5x0yHPzwj8dEnZ3wzqzYLwzcnwsQEMsoOTDRWxmyJHlK2_kT-_oIIIrHIMMsZv8YShzBeaXy4llT7727VY3ObOlXvIxbK3zGO3ybJ9etEm2j33En6n_B-vWQoTHlXhoQNGdOgnfeprVWniPzB9uoIStFJp_mQkGgTkV0K1qZm-lImrWfSM6mfBfQkVRXetXvL7a5BptfQjcpqr9t_iOagdWi3id3Z81y6qZL6euy9Kdd-vfC8xJP4NB5z_mqBoKnswdppZIzTmgSucvRpyuNVmkSrnVe_2ng3J93C-0PBkyLcgvgSj2OWVsUCYQPniT61j2QF5LXOowxY7Ik_rUt20G5f_qZXtX5ZljUfHSU_gnqjnU1xlRutOPz8iu9mzU1apogbZplkiYuXazAtvslA-QZxhtuBHxUpAzwv60zmOGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=oAMkPH_jW-HyV82SKxPnQROJzac3XSsMp2hk3zxTNimotZTJjJq9LtZbL0JryBl3Jw_mcEtLVwfeXfxMrvWh9Pl3hs7jisjg3XrW9gNIVZ3OqGg5kMKdU0zFVhrSD7c5vipEw1ID1_uzgScP7b8d7xEqOP36L8b6dBhfu4wSOSlHL-7qVTiawK2l5276smkRFRz7jkElNyXPIe_UeGctONIx_BqM0u1_PjYd6_j8fm7oEe1b05n34t0yJ4yogG_5x0yHPzwj8dEnZ3wzqzYLwzcnwsQEMsoOTDRWxmyJHlK2_kT-_oIIIrHIMMsZv8YShzBeaXy4llT7727VY3ObOlXvIxbK3zGO3ybJ9etEm2j33En6n_B-vWQoTHlXhoQNGdOgnfeprVWniPzB9uoIStFJp_mQkGgTkV0K1qZm-lImrWfSM6mfBfQkVRXetXvL7a5BptfQjcpqr9t_iOagdWi3id3Z81y6qZL6euy9Kdd-vfC8xJP4NB5z_mqBoKnswdppZIzTmgSucvRpyuNVmkSrnVe_2ng3J93C-0PBkyLcgvgSj2OWVsUCYQPniT61j2QF5LXOowxY7Ik_rUt20G5f_qZXtX5ZljUfHSU_gnqjnU1xlRutOPz8iu9mzU1apogbZplkiYuXazAtvslA-QZxhtuBHxUpAzwv60zmOGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol7lceJ1P8XC0E7DmUvWkV_mzPEFyQmV7Z19fI5vsLr_MJw90QP1Jm_ENhf1UBmOhYike1j5X0HnNcYJ91wy7LSR439p90zVdfnfO-STYedjHSaxRNW39CUbRspLcIjHTIDiz_oWuQPDid6JSdTUjA7jFY-CLX1TSI40lxEIPzBmhq2XEZB8vyE2x72d-Tfg7k-oar-Kp5QAipB6vKruzT-mPpnAhbJDqzfYSjvPg2nwhiQ8qtSTMETCtrx_YZAncPzMDE3gKYp17fIo401rqTWpCwwTw7iUl3Nqwjj1fO9OhwSKTMXSW6uymuWh69f1z7ycIIa8vnCg2EuuAJ9yvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keG9GU51WSFWKKYGYmba9kWD6kxVcUAH1xNdzWh9cnvjA926Mo_rxff-1u320uY4Cu4v6KUK56JSAJXyo47lVNKoqJoYZsu-Q-SMjC8N4z2BTS83xzsg7icr9IzlsUyG7d6RFN-WPEqayzloPWN-h7aCFVA83M6ym_gN_T6VcsoeeeVJvFgZVwQxhSnM2xYsj2ABxzEK33AalFEGFNeoLUxUyruKPbnnYEgerJGVKEDVfPhXcpaNlDR132ZGpjn8GpLnoTsEJm2i1cH9wx4i7BYjubWbHKcXLVrIwtT1-cmDZrMEyYoj8p-4OhENtKaEsHE_wjfU0Cn48yYNpTN-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnagLuuyrnbRQOCQu0GP3QNYW_KFarKZg0RKh2nroarhOCpj7sz0uRQJH9TyFcV97g-TWbnEj81r1Ko-Yi_N27I4U5pGf95ptY7EbG8e4L_EEfWJIE-R7GVuglQh4qLy-qQrVEf_01ur4Dok4NJhY3ACmwVolDdMWNsN-6Y0G082HGtMgSN_W5bzTdbayXwaAWptySkNAY7T3EKdgd30XJONLRojgLrxMWnOVdJiXu-HCpJRosu2bMo0aeAz6o95VTuQkiiUp_jyvuEbhAYOvEX5emkYwNPbdFmjTSRCqt8jHGcP-iFfCSs5xbwtAhUda8Yr163c4RI2lR2EYrxdlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Jh_URKdTKR2kEHtfpyZo6fCPk6fz-OM9Kt2BfmghqS1dHWH0ozaz4KoNVOcWU4zQtDjC_vdkXBKstUqyZsnKXt3A9IWuMQlK6qv9e6cUMbuQptoqEDHhCMfMPMXYH3OGRFWbyaq_hO5aODK-4d-bAg3gtZPL0UcxGGoXq3vWQAlkph8gXEGyIPezUHpRMNiIInKaK6WDK6e5b-Tjj6aroYacoQQOSNNrdkgxH08Q6GwSp0QFhpVkDWj-JAZ6u8Q3-duWZhDVuC4Ivllqjsu5IryOzqEvUfJwUGDAAkmIwcYkhL3A3qOq62gA_igSNb2mUQ_OfkJjRpR9EdC635WF6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Jh_URKdTKR2kEHtfpyZo6fCPk6fz-OM9Kt2BfmghqS1dHWH0ozaz4KoNVOcWU4zQtDjC_vdkXBKstUqyZsnKXt3A9IWuMQlK6qv9e6cUMbuQptoqEDHhCMfMPMXYH3OGRFWbyaq_hO5aODK-4d-bAg3gtZPL0UcxGGoXq3vWQAlkph8gXEGyIPezUHpRMNiIInKaK6WDK6e5b-Tjj6aroYacoQQOSNNrdkgxH08Q6GwSp0QFhpVkDWj-JAZ6u8Q3-duWZhDVuC4Ivllqjsu5IryOzqEvUfJwUGDAAkmIwcYkhL3A3qOq62gA_igSNb2mUQ_OfkJjRpR9EdC635WF6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=dD2L3piOWdltF_NX0ujYwHNyUMZgxfXWlobBV3QWdgKyTv2RDeNdI1IPKXunL3li4LynY1OJ3yjZrDMBBhW5b4n2ZvPLvaSb0bsfY_G5T2BDYk2ypyI43PdZjQvs3geMN0BkvUJrB6N5n_tE55g8GKhlLe7Hy8uxzkHaevnK4dpNsdh_c_iHgqQNIAN1P-jVdOkqxxTVfa71uc9lCUZnJds-JRoHeWydoqI-JHWoLJo7KAuToR1bnfQBsqNMHuV7PA14bAhboiJ9LpJd5yiD6y1V20WASunJezNfy8O7mOSRGl_Uq-wxRb4hIDYoeLTFUsVhGNzRLA_og1Kh_DZCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=dD2L3piOWdltF_NX0ujYwHNyUMZgxfXWlobBV3QWdgKyTv2RDeNdI1IPKXunL3li4LynY1OJ3yjZrDMBBhW5b4n2ZvPLvaSb0bsfY_G5T2BDYk2ypyI43PdZjQvs3geMN0BkvUJrB6N5n_tE55g8GKhlLe7Hy8uxzkHaevnK4dpNsdh_c_iHgqQNIAN1P-jVdOkqxxTVfa71uc9lCUZnJds-JRoHeWydoqI-JHWoLJo7KAuToR1bnfQBsqNMHuV7PA14bAhboiJ9LpJd5yiD6y1V20WASunJezNfy8O7mOSRGl_Uq-wxRb4hIDYoeLTFUsVhGNzRLA_og1Kh_DZCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YE9BVZBJoWkUKTtdpCjZhRL7b9xujfoiT6ReQ7yhHUrIz58uCyQihGHa7JOl8c-ASkucBMrygvRbDGb4QkL7aNhllH0Ql-XhQYWRUyTafnwZqbkQ_rlmCoCBxRJHvK5dVOXYcGB0wH4zPhJeqoQCxPi11WHTdbh1d7FzS048vXHJ85tydxLFVu7lT3Vp9Vye81fYj_h6zEfu8GCRplqLmsVbrxwuJTrlYJXBZvdl_PM4tBHF9iGptSbPtNMEOSlGrBCWn36mfdP-Roky95TL5sCdS8hARWsm5VZMSf-8t_yK54h0BrOKjoPMec4i63ChlhKSnM3nKo-dWibmAzWO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=c_FnaA0DjY0IDTPCYLdiJ3A3XJMGp0SZQ8fxrN5lKLHBCVyHxrYDxvohQF37fP7xFqvS7wywLxxXsyw1vQlynnWOZlld0HrSFJactoN7-0Sfo_BBQEg2O6HfFSmu-XCCeopISSSskMZJJ_4iPpwKsYMOybrmHU0pwc0pSkGw_C0nF1XvmIbKI9Bsklke6bQIeFeExDVncmz2oBa8OSJJyBQKqYa8arqpWop79QB_Yio-xfqfj3BUuiyAJUb60WIxKQUfoabBKRyR5srDY9yLxEhaW6x1G-1KQKbsM0lC1p3V1WPQGasyQdTlrXjzgOhi-19kOzp-SwV3p96VF7RySg55UWZL7AzAB6i51PhyeP8Us16iAf9Vbtf4MmeahHEf3LyCYh9i4l_16xd3pflAajFzDwJw7k8A7tg9GOle7JC9RUVHH-51N4FyDKTryZtKdKbig0zyUohXUYKUViffAuxG18aTk5HQq8ivjZ9zeM2tSKJqQurkTRM3qSFMvvyYcnrd5ZCDZqNFG2qD_ttb6ZLUDbrNrxbG24nKWK7Zya3FTCQM1PEhTAgnF3tf4B3UPI-7fksHtl2JItquiLEGb4KfmZRbNcKMvWctG4OYOl3S7ZJGmu37e3RTRfRpUZdEV6K5OlibFxO9r6j3lqsQ8Jb9wB6awrbIBLU0Ux8Vf3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=c_FnaA0DjY0IDTPCYLdiJ3A3XJMGp0SZQ8fxrN5lKLHBCVyHxrYDxvohQF37fP7xFqvS7wywLxxXsyw1vQlynnWOZlld0HrSFJactoN7-0Sfo_BBQEg2O6HfFSmu-XCCeopISSSskMZJJ_4iPpwKsYMOybrmHU0pwc0pSkGw_C0nF1XvmIbKI9Bsklke6bQIeFeExDVncmz2oBa8OSJJyBQKqYa8arqpWop79QB_Yio-xfqfj3BUuiyAJUb60WIxKQUfoabBKRyR5srDY9yLxEhaW6x1G-1KQKbsM0lC1p3V1WPQGasyQdTlrXjzgOhi-19kOzp-SwV3p96VF7RySg55UWZL7AzAB6i51PhyeP8Us16iAf9Vbtf4MmeahHEf3LyCYh9i4l_16xd3pflAajFzDwJw7k8A7tg9GOle7JC9RUVHH-51N4FyDKTryZtKdKbig0zyUohXUYKUViffAuxG18aTk5HQq8ivjZ9zeM2tSKJqQurkTRM3qSFMvvyYcnrd5ZCDZqNFG2qD_ttb6ZLUDbrNrxbG24nKWK7Zya3FTCQM1PEhTAgnF3tf4B3UPI-7fksHtl2JItquiLEGb4KfmZRbNcKMvWctG4OYOl3S7ZJGmu37e3RTRfRpUZdEV6K5OlibFxO9r6j3lqsQ8Jb9wB6awrbIBLU0Ux8Vf3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=GgKbsD5yTLeNEDEBMc4ZvkxCLQ9vAfKur7r2fK7geHIkkLIpxw5r2UOksD-nCNuYiDYQuDHWsotIm-wFOqxCr0mRARhtZGkCHS6wD8ecU2WLu7yWr7OWRcAOQixcYd1h4Wq9bv_iD8wU-y5Ap1oyElE-OcgUFWhXpLHWZNrai0fx-dftNYhyG1BIHK0rTqeDmJTLatiClN7d7s7hbOS9fCV84LvdzAOJHnBdzteFO2nJFIkiuO5Xqzz2gvxHJJ9KS61_vfjAzfcb1VutI0wnkWQFoYIl3tGdW8m1Nd2-KKSGAfwM3TdFtZP9G7BIT-IaFmDqY4WjlhsV_DuDUAhDVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=GgKbsD5yTLeNEDEBMc4ZvkxCLQ9vAfKur7r2fK7geHIkkLIpxw5r2UOksD-nCNuYiDYQuDHWsotIm-wFOqxCr0mRARhtZGkCHS6wD8ecU2WLu7yWr7OWRcAOQixcYd1h4Wq9bv_iD8wU-y5Ap1oyElE-OcgUFWhXpLHWZNrai0fx-dftNYhyG1BIHK0rTqeDmJTLatiClN7d7s7hbOS9fCV84LvdzAOJHnBdzteFO2nJFIkiuO5Xqzz2gvxHJJ9KS61_vfjAzfcb1VutI0wnkWQFoYIl3tGdW8m1Nd2-KKSGAfwM3TdFtZP9G7BIT-IaFmDqY4WjlhsV_DuDUAhDVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgCqLA_DdIPrnizY3P1iylZBLxJO721Xw8cVeA4V8w3CwZStumvXfQkYwdf43jgGZtJBsJS5XJ48BEd_7xeRdXGWRQBydXXCtFYZ-tAcWT-BtneYlSs3pc7FtNNtnycX-SswNQmQ0ZUTbm1Q0dKSVtWMGxVrtvDIulIP_9ZsSxW8VFxQx36uXvRLvuz_wmn77O-KTgwGgwzep9cSWmGQLvXeTA9nhq_8O-SCDOxfhML50T974xKV1R4Y1IdcgOUJ_BNTQHVBlod4XuV7THNdyBTIptZ-mgUKsqDeaMUCFY3oHnVjLlK4uHSfUZZrjTuCOOeSwWGayWpkVCSc0H1LJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=u8VWF0PVNgISfRNOJC-iyznPkxCBDf-mL89GP6uZMh0VP1RjaJRJm_p7zjd3xPFv7uDSRIcaM8Y7beOPtq8Nx_NR8WdplJerDIY27APcJBnfYRej5S2SIc0tf2gPZHw_32NVw9IzZsuhShqpIhmo2Chcwf-DmXWxdWD-tva7mnaeefRS9WB9mbnQXERdwM-3AU57BIArG0GOMqTYA2aA6qOMZgOKVemq-MVI5CWG_yF-yvn88Z2pJfYJJHg395KlerQhWya_hGN8Eq7ODTRoFict-9exzZqjVlqHlhW5BUgDv_S4K9iF_JglMoyuFnMmfr4PyCgWlvCFuG0y_0bVgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=u8VWF0PVNgISfRNOJC-iyznPkxCBDf-mL89GP6uZMh0VP1RjaJRJm_p7zjd3xPFv7uDSRIcaM8Y7beOPtq8Nx_NR8WdplJerDIY27APcJBnfYRej5S2SIc0tf2gPZHw_32NVw9IzZsuhShqpIhmo2Chcwf-DmXWxdWD-tva7mnaeefRS9WB9mbnQXERdwM-3AU57BIArG0GOMqTYA2aA6qOMZgOKVemq-MVI5CWG_yF-yvn88Z2pJfYJJHg395KlerQhWya_hGN8Eq7ODTRoFict-9exzZqjVlqHlhW5BUgDv_S4K9iF_JglMoyuFnMmfr4PyCgWlvCFuG0y_0bVgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gcwe6u2j0vunHd4bFAIX-wyJKNNjg5HdIqfNxSdW4Jw4irGkjCz8ZpkHPO6YOJtHq6yWsiGPwNS6fFVEveIUkNUqG1jCLoTXOyQ4Sf_dbAxe2rxomn8hutqZYhrllc_FtvNsj6-w229exrZO37vU-4fBd9rIBCjE10Y_ULdUlaKXAB51cLN7s_DSHnuCGYa7DjXB2motv0qHjNLIHeU2Z7I95lW5JVIqqk9CoHDpMwYuiVOp3ZqnBurILqBLtxiVDBdZlQJ6LiplYwJdlwQOqMbPfntYwJlpCaoBWYMW033r3Y5im73x0fp8Dd-tqraJB8QivvrMWidR3gw57tyIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADHJG8NxrpoivTOGon6hQ4vrLH8s1bJoREucEo_f2EXmpFI2Cu4E6cRzQAmm1E7o9seXS3_stPx9sSHrXQHIBdhyfS5QWLv69aV0sBLs0uEbphy3lXYpXZm9YQBHc63kRepZaOhmUtDSQuJgzy9qzZ3M_wfKOakdeU1mNG_TPvJlshGvF4IN9Yf_vXrAeGjRybENmhpyfyrH-RNLSO19qrCGa4k9dJs5paavvx6whDqvk4QLEz3hrUJ-Tu8f3kqkDSjd5XjEaDskFBNJnKjifY5oaiGxTgbYE2lRewjU9KGS6aneRHqDEnb0iwMEpf4dKjc0N3Ngh9Y85KelnLByAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=hiTLlYSx4LbU8qTKBqOPcO3lvHWIN_vFYhxfCFC6mnUfMH_6gQEhIDZqRnAUoNXJVGRM4UWldJkcm33LJ8ILPt4LUWZaB1hx7O8QDEIFMQXX6EALJG3nXcWqu2igcaQ1JtgaBmkZPpwUCGB33q5MRw_jIFwRh8Xc9p_LxXOVSJz-YxTHujtH4e7azgZycsS0XuTOr-jA7VEvcLpFu7cdEj_DzH1_CygrX6x05Eu-DQmgNqaLPIQ_34GaUNYcdEFc92DKB6hDVVwjyGm4LQnM5l0Q1wSilat4ou13qyl8aeP_9K9lQYPykpGLqpMU-ovqOIWl0gVtuuGpE_Yc6vLCHgVzG362BDVe0_z7TQDh9muALyK4XHv9kNU-dt7J18_phx-MYfQWeXm8H3xXd99q4Zk0NIGNQnOGMwVUVL63Qo7YrLjJ1BNzluC48SYlktKCLmRSaoMLUiibeQzJquCEqB6DZz9v2Mc2GGeERducdviDIlhmh9S1NHZu_PfRkEMJCGp4VJ6h7DL46GT1PRYF4_2vFUKLyuDScS-4rD-mpbU5SiMsLO9EQvAyy1-BL0_fGivTqfh2SAFgZRfI10JmAvE9tR069sy8lX8i-xkBlK5mFWo_PmXoHfAO4A8Bk_Da1RuVtpAk_a7bf3bXAx1Vl9TWvwLbS-uSCBHRQc30k0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=hiTLlYSx4LbU8qTKBqOPcO3lvHWIN_vFYhxfCFC6mnUfMH_6gQEhIDZqRnAUoNXJVGRM4UWldJkcm33LJ8ILPt4LUWZaB1hx7O8QDEIFMQXX6EALJG3nXcWqu2igcaQ1JtgaBmkZPpwUCGB33q5MRw_jIFwRh8Xc9p_LxXOVSJz-YxTHujtH4e7azgZycsS0XuTOr-jA7VEvcLpFu7cdEj_DzH1_CygrX6x05Eu-DQmgNqaLPIQ_34GaUNYcdEFc92DKB6hDVVwjyGm4LQnM5l0Q1wSilat4ou13qyl8aeP_9K9lQYPykpGLqpMU-ovqOIWl0gVtuuGpE_Yc6vLCHgVzG362BDVe0_z7TQDh9muALyK4XHv9kNU-dt7J18_phx-MYfQWeXm8H3xXd99q4Zk0NIGNQnOGMwVUVL63Qo7YrLjJ1BNzluC48SYlktKCLmRSaoMLUiibeQzJquCEqB6DZz9v2Mc2GGeERducdviDIlhmh9S1NHZu_PfRkEMJCGp4VJ6h7DL46GT1PRYF4_2vFUKLyuDScS-4rD-mpbU5SiMsLO9EQvAyy1-BL0_fGivTqfh2SAFgZRfI10JmAvE9tR069sy8lX8i-xkBlK5mFWo_PmXoHfAO4A8Bk_Da1RuVtpAk_a7bf3bXAx1Vl9TWvwLbS-uSCBHRQc30k0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4xQpLylnjD35tKHL0jOetLd6Tjl5tjEF8Fyg_IdwmNFNR83CmqNH-BVJM3JSSpbOB4bszn6LwGLBxXDW1FEfbfPCqKCqRzktoCkJFz50dDMoSjjqtT-ON4iDDOgCRJFRnNueqEnUvPntvGNjyNGtxTC0PzXhroz1BhLPEbt7TDy4wS7qNwlyLcdJP_jzVLovgmT95wm_7dLNyZIV9fTo_gt0OSVAbHe3XOglbdOnjW9lU_3lVrzYaiKhkT6jGBm-LF7Pm3GwMBrYliAgUSqgvMG4Gt_9kLzqB7oQwUCFeLIVWRMRcC7-E-mTXPb7i1mrSdNUItFxkB3NV2VFBnP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qF3-g3e1agODtTDysxmphWsvsITNOdL4atCiy12UeIv_hV34ugftvssceTiWpCvKKQXjjDlYdH74oHrIWBvTBlrPAop7534aGfXaLwhGF64B5x_17j2pQkcXeu5InEZynBXTDG7OZYN5WHNfQ5HK5hYlNZU9q7w9z8zzGCTYpN5gmmeMz_4W0yNtdd9OHtZ6tq7_0ZwtvKLis2Ec4SqJ8-gW5yYSjqHCR_dwkFCZsXoqYOTdZwz_SJ1kN-sGf9WU7xlQwTdKcH-cJmNG49QAaRPRRijrx5C2DW_sKLdMDY91SRIyO1pQOJp-qnC5s7p51L-Bk2nqp2e3yrPL1_v6iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=kzoun5T-u3kaSAMvXuVzXPQkyAoqlPzTRh8A1hIpIUuZUrSFIGn5AvNoQvtSK8nCBV84uC_87DNJLjd-Wg1mcC5nIjy0r8Qi-Gyh421wIatTtU00xFMKn5fFuzj0JSAWvASmJ9eLckPogaEF25Pm8GUOMQUJgFtkVAn40yX3qRVQlpyrFAPViTuC7zlXda1b8GKRFLGfEKz8UdOZB5FCTcJMdO_2cYgltdU11otXJc7RQnzWfZy8-AhrF2fIJJYmLC-1gdq9fkRXNhekoQH30TFewHeJuOiyXiArYsPNhkbR-aN9VW5n4N9fzg-aoS_wjQQ9CdoZViw4LiR91HbxNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=kzoun5T-u3kaSAMvXuVzXPQkyAoqlPzTRh8A1hIpIUuZUrSFIGn5AvNoQvtSK8nCBV84uC_87DNJLjd-Wg1mcC5nIjy0r8Qi-Gyh421wIatTtU00xFMKn5fFuzj0JSAWvASmJ9eLckPogaEF25Pm8GUOMQUJgFtkVAn40yX3qRVQlpyrFAPViTuC7zlXda1b8GKRFLGfEKz8UdOZB5FCTcJMdO_2cYgltdU11otXJc7RQnzWfZy8-AhrF2fIJJYmLC-1gdq9fkRXNhekoQH30TFewHeJuOiyXiArYsPNhkbR-aN9VW5n4N9fzg-aoS_wjQQ9CdoZViw4LiR91HbxNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=rCHwxL-iiDqoa0aWLl8PfGuR4zQBH-e0yWH5N_3Yp0V38XfqeYty2jlg5tZFSZ6Pv8YyRcW2DmDRah627jiwp0iRngaJKU02BlDByu_ZxQWSk_vw4Ty1LrliBn6ZEOlkPLqRRw7qN7lXlT0pLYA9eGKugN5I3aADVKVGh6TjzKxcwDDdZt-FYXiYxoC8qKhA36rQEG43Hb7FiZpE-HulIcUfrhbxiM-QpDI7B_kq3B8LkUt1KwqMA7lLalFfa-E03PytNVAEftIWvBWQ90vRBLsPhTElCJ5maGpyQrodljmL4Suors0BNnG8ynS-aSdNwW75iLoN8ZBFCmzCcZUz1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=rCHwxL-iiDqoa0aWLl8PfGuR4zQBH-e0yWH5N_3Yp0V38XfqeYty2jlg5tZFSZ6Pv8YyRcW2DmDRah627jiwp0iRngaJKU02BlDByu_ZxQWSk_vw4Ty1LrliBn6ZEOlkPLqRRw7qN7lXlT0pLYA9eGKugN5I3aADVKVGh6TjzKxcwDDdZt-FYXiYxoC8qKhA36rQEG43Hb7FiZpE-HulIcUfrhbxiM-QpDI7B_kq3B8LkUt1KwqMA7lLalFfa-E03PytNVAEftIWvBWQ90vRBLsPhTElCJ5maGpyQrodljmL4Suors0BNnG8ynS-aSdNwW75iLoN8ZBFCmzCcZUz1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=bz5w8fmwZ49fSJ4msBQ-lyFhEHTVFA63wx7JaAhsCub0iOMhmKuzh4WckTiM4mUPIRV5jVwerK2Vqs2pNh4UkH_ByDkDUlRhxUKwTSLwaAMWFEi7ahprHPIF5Ju-v5uUmVCLLVvxROuN4DbxEe0l7SFdAqTlJZ167nI35JyFc0aH_aa84iqVpwUD4-BNliGlVSLJf_KkM0EnPlG-EIN-ejNSDspkV3RaolvDMZdVCx7U8jC4TZkiEFsjX9vFm3z1GiYtilzkMtgb750jYCosHIOzmSGBJ23Spz1If1Zp7T4-9N9ol1ZTRTdWQBbh93pJ4u681a5voJJIilDXuU_-4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=bz5w8fmwZ49fSJ4msBQ-lyFhEHTVFA63wx7JaAhsCub0iOMhmKuzh4WckTiM4mUPIRV5jVwerK2Vqs2pNh4UkH_ByDkDUlRhxUKwTSLwaAMWFEi7ahprHPIF5Ju-v5uUmVCLLVvxROuN4DbxEe0l7SFdAqTlJZ167nI35JyFc0aH_aa84iqVpwUD4-BNliGlVSLJf_KkM0EnPlG-EIN-ejNSDspkV3RaolvDMZdVCx7U8jC4TZkiEFsjX9vFm3z1GiYtilzkMtgb750jYCosHIOzmSGBJ23Spz1If1Zp7T4-9N9ol1ZTRTdWQBbh93pJ4u681a5voJJIilDXuU_-4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUs_a4rzTsI685DfZEWHejP9o0FaaM1UvgAVAw6mO3sLaqIDnv7Kj677nlfsN2-AiKeApsiqhrnX_Km-V83sCssBMcx73oIEenY9fMVW2CsjgmYqmKGPIhSYwyS_C7Vd8bIODCHu7Phptk8sl4DAA0AWX1a4DzZSyjqGdtiGcGrou8sdf_x5b-bo11anCtnSmCJ0NuraAxoDqjsPYAzKOZCTFvXQTJD2bi6DDKsglJF880y9tlTjgstFv5RNbDUanwQ5DgDL78RWsMHG82zxOgZtAC7Hu-H8pG9FzFz9YUFOvKP4uj1mVvsp7S8E8qf3cMzpUrKfx9gOSZ8KV0mUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsrCGxCFSA0ZsRpCZ9pX5Ub4-spVVd0nbmHDeqrYFo6aNQsQLXdL-oeL7IyGRxHmpdRLxPHG8BzRq9eRBy1xcTib-X7Dx1nzlEeg0dltvt43OOa1wredBwNuvtWLmeSXJ5AaydAC7uZX79755xUkvNF6YvLOsv1x-n13Kc1xKoJTvZgat1vea-4GoybcdlFCujKiGtk4Vnf_p0M1jnBTM9u2FyJRGpoNS5fLMwb8x-DhYCM4oQZqW-d3qBdr934sYr5V2rNQhb3o9uBxTj-SW0Ks_PElt6OLyaLYtnQRwMYxzEh-jqMcYH7dLVEBYjXglTtfhKt1kIkczcxz8KPHPuzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsrCGxCFSA0ZsRpCZ9pX5Ub4-spVVd0nbmHDeqrYFo6aNQsQLXdL-oeL7IyGRxHmpdRLxPHG8BzRq9eRBy1xcTib-X7Dx1nzlEeg0dltvt43OOa1wredBwNuvtWLmeSXJ5AaydAC7uZX79755xUkvNF6YvLOsv1x-n13Kc1xKoJTvZgat1vea-4GoybcdlFCujKiGtk4Vnf_p0M1jnBTM9u2FyJRGpoNS5fLMwb8x-DhYCM4oQZqW-d3qBdr934sYr5V2rNQhb3o9uBxTj-SW0Ks_PElt6OLyaLYtnQRwMYxzEh-jqMcYH7dLVEBYjXglTtfhKt1kIkczcxz8KPHPuzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=nNY_PEUkr0FjpoP3jpDxrw7_IMGHvdqzNH9cCL0yK4zOUa2dCobPjOlY2VxESrQ3btwccjGi-j4WiiM8Pk_hdKPhu9LoG60ASpo72Uo9Av8v7sJ1H_2NWaJfzFbwvTrpsBFziwbIJEvQsGCUticknR5O6ISTdjNVCvIT8iwgO5jalsKGgfqGIeAtyFmjn605heVbd82WxxX3XaLEwRFMZdmbsBytuE7uA-ywzWHM7-kJG0Asu5y16pDA5yoeMG6PJXLid2R0NiWwEPIwMXeY1rlQeGaTowbmw469AdS24-rBU5UWY2ionVahB4w5dT6RHvduPFZHp2Ps-xcmT6Cf-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=nNY_PEUkr0FjpoP3jpDxrw7_IMGHvdqzNH9cCL0yK4zOUa2dCobPjOlY2VxESrQ3btwccjGi-j4WiiM8Pk_hdKPhu9LoG60ASpo72Uo9Av8v7sJ1H_2NWaJfzFbwvTrpsBFziwbIJEvQsGCUticknR5O6ISTdjNVCvIT8iwgO5jalsKGgfqGIeAtyFmjn605heVbd82WxxX3XaLEwRFMZdmbsBytuE7uA-ywzWHM7-kJG0Asu5y16pDA5yoeMG6PJXLid2R0NiWwEPIwMXeY1rlQeGaTowbmw469AdS24-rBU5UWY2ionVahB4w5dT6RHvduPFZHp2Ps-xcmT6Cf-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nozAudy7zcz3SRMULZvD0Y3kreGVL5_CnQ1UcndBDrWnPYxE4OpGmoCLPYJ2fpUjoCaS_mBdGsUjQVpXWjzzC9kgdLtvVyQpMcFbm4DxQ9DQXn7amSrhPcsNUuxFULLKAV4UE-gX4bdLLnzkMWeliK9zcZiE4vIaTbyS8FCDh1Yy46eyf53OvjwpdyCYxCV2luTo-w2GhDACYvPUG7E84YNPVlL4vCZ7e3jHdFiYBX8f6BX_6cr6LuUOCyw75CYOVYhJAritd_8TWG6abXalT6W9UkpGZL_Xus8XW3_QIcstjxmFX_R47i2rcP6b8Ny9EOZWqXDBlf7kY36uHkVJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=bFjwo3fzhkY64U81bw0PPKwIn9MCj_OSw7SCKK8PoiKMguhbQxcv2ZnSlaFkPRK-YPNeM1izHioSJU6WrHvlqji0jNhpJL5UsOIceML5JCICTf9dZn9nKJFkpq_3sA2Eujme8TUpSKGU_Se-o_joLKkHh1QuMNBtVS1AyvX2DMiPyeAeP3TiZoUyGgr06NmXXEYKLWMWNGlLjw0dCZ6_DvLXOa9ZcAOmd5zTx1PBZ7hbQSSHQRoaXIFW48reWn9zvNJJNHZam-UVT8U_m2By7KmLgoSpw9xjF2njK5kY_g_M5GRasj1nErHH6gXn7UcK3uQnqyM0wdwN-C-wVmFf_LY2z7osaPimm3JdmwURakBUYg0y3hXtJ22kgZEUp47lm1bgE550uOTgl4eUwunSkZr2Cl8ORL9MZKNnZA4neIQ5RAe73HF3z7qeyM5HLIaZ-oviKOK28wWWaQApENmpTGX_Q9HSmiQqTvvMr4GC86W8LZNDyPNvpggEi4rRLA1hX82CS5vxkVIJcri3C4eBiQSYUAz69CbyN2b8yIdMvNUvPTMI26zYdg1rSwBoJaNpGJBNiFH4r7KgPwDNxCNmGF9rRHzJMh4HntmxPdtrcg52CiTHMpH6_faVAHQlvy4eAy-9WMmIKWpNqSIo3bq5wLZ7d1RTcgW2NgBjY3nIPKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=bFjwo3fzhkY64U81bw0PPKwIn9MCj_OSw7SCKK8PoiKMguhbQxcv2ZnSlaFkPRK-YPNeM1izHioSJU6WrHvlqji0jNhpJL5UsOIceML5JCICTf9dZn9nKJFkpq_3sA2Eujme8TUpSKGU_Se-o_joLKkHh1QuMNBtVS1AyvX2DMiPyeAeP3TiZoUyGgr06NmXXEYKLWMWNGlLjw0dCZ6_DvLXOa9ZcAOmd5zTx1PBZ7hbQSSHQRoaXIFW48reWn9zvNJJNHZam-UVT8U_m2By7KmLgoSpw9xjF2njK5kY_g_M5GRasj1nErHH6gXn7UcK3uQnqyM0wdwN-C-wVmFf_LY2z7osaPimm3JdmwURakBUYg0y3hXtJ22kgZEUp47lm1bgE550uOTgl4eUwunSkZr2Cl8ORL9MZKNnZA4neIQ5RAe73HF3z7qeyM5HLIaZ-oviKOK28wWWaQApENmpTGX_Q9HSmiQqTvvMr4GC86W8LZNDyPNvpggEi4rRLA1hX82CS5vxkVIJcri3C4eBiQSYUAz69CbyN2b8yIdMvNUvPTMI26zYdg1rSwBoJaNpGJBNiFH4r7KgPwDNxCNmGF9rRHzJMh4HntmxPdtrcg52CiTHMpH6_faVAHQlvy4eAy-9WMmIKWpNqSIo3bq5wLZ7d1RTcgW2NgBjY3nIPKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6EkCvWssGsQyjmDIqDFVJPJEIK4Nz6raKlkVH7PHu4LvdMqo2I9Et89qAl_TR1PuU2OUOhHcw6LzJ5FgHDbmVr4xI0f54n004p_LUfHn3q1izk6OBEMmN20EfWalIxG-YA3OORfvmctquQnadoaJ0E2WLtQg2OThFC2VhrThJQ7Zoohgd-92RaB4v6N--aMGs9m1PjQ0WKrEwVHGcfu6kgnGVboIjJWe24BcxbzoErBGKsJjGtbERUmVKJIEdyx0wsaOEaBiCNihCBdTMLYR0-4WQqEeeAuHQDKK2K1d_hPg5XpMA9nEmhSkBRGEEVPHLIkZyJ4H6TPiQ532_8Hzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=tg6z3c8fH8Tj19k8K-YxcsLd82ubSk12xV994USe4UMWhfa_YW7rEsjgJD3nHDJrUmFSskgKGj77t-iq8KyTXWpMYc7gr7W4MJt3C1DUIwRLSnAsh6KZJosIUNee0MDmIC9scYK_t_ygwr0iI4Wc9v2DMgY_KGNwSVtkm4bD3D7wwQ8w34a3l4k8W8uDFtbECKjqDwS9InfC5-db7PFbqT1v4SvkLj6ftjzbq5LpZKlXK03bT3P04iiPQOm-rnJ4irY2fME_7OsUJCdZfZaAcOkVnBQeQlYjlzWeTNlcaGJQeXrJyspWEinNNq85cuZ67AT80xZr2D-vU-ZKpnPMRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=tg6z3c8fH8Tj19k8K-YxcsLd82ubSk12xV994USe4UMWhfa_YW7rEsjgJD3nHDJrUmFSskgKGj77t-iq8KyTXWpMYc7gr7W4MJt3C1DUIwRLSnAsh6KZJosIUNee0MDmIC9scYK_t_ygwr0iI4Wc9v2DMgY_KGNwSVtkm4bD3D7wwQ8w34a3l4k8W8uDFtbECKjqDwS9InfC5-db7PFbqT1v4SvkLj6ftjzbq5LpZKlXK03bT3P04iiPQOm-rnJ4irY2fME_7OsUJCdZfZaAcOkVnBQeQlYjlzWeTNlcaGJQeXrJyspWEinNNq85cuZ67AT80xZr2D-vU-ZKpnPMRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0kwqCK_mRo3ZFb5R9T1cG0mno8pjD6QRapqaAsbuXvuQJG3Ds49SJL43kXSTGhn6RASoFa3ndf_OGSsCNK4Fn0Azc9uli4EfpaZAJcX7rhM--wfXta_AxvK2Y8rRLx-lrIB8glvVritoIEsTYgVNoP1Vuhf3f-kVWJ0ouRGQTPZum7cfa8tSMt8GNXV7tUWN2g3lMwzesGbTUZnp1xngiNjEIe6rTZ5XePOe3j0WLZTb3hydPylduu7uxbgS_v9xyc9rJLtD52uZyihwxY85TXnDahWCQSyPJYqkWytaiRLu_lJiBHgOmmna-CDRBZVa0TFWsJc4T83IJEFkTdzXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qip894Oh1BGXYJSDeNSV9UNln0tZnPISP6sBxMsasyw0JLweu4kVL26cW4q7J8vcyD8U7MwIIOM2iHBvkZdaSssMRqyj0_Y9yEifUfEaCAaYzZLt4BrCZAj5tU9IBx3Eb8VRaeu2TuCwakobhF_kKN6sfJU8DiK4h1ytTpAmbWjhFWGSwB79GlCYudQLRJfV6j6y-rJc0ZPkl_0hDrJjyMie0CzFkkuJTbZ8bJ81LgC9Gtg2HsjG9s2MTwxOk1LN-kL9XsJzYk7ked5OZUqYGr8M_4C_9mX-Zv_uHzcLgxepsevnT4arUhFEymp9p4QRpZ0euav-i6866kom1FNNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ulqn2Xq4fHWXx7rZ7gPA-ITck8FS33rUJbL0xwJhbmT_GfTV817UOQQ31eWJC1x6sOMpjGyvtSB1HrHkOUbN5IMmtsjhli-jwTPoHdpeY_3OJu0wwlEnodYoQ61AxQS2W98L5cs5wOGZeU5o4NZS6wvQV4t_FSDD7CdqscvzYLlfJYuDurMED4-ay6PvPJW0Pydw_IuRsttu7POhYSP5_qM3mjcdO1yLXObm_cFQEP152J-8fO2vfIJRpUp_A_SyxJTyiMcjRE-l5CpjkW2MtLSCdo4xSrss1lkah13KL1Qcg2khN1rvJ3Y5QDNjkiVok3_tYqfZ2RVpi0fYLSHQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Lru8DlRece44wutcGsbbLu23h_GKxQ3iA43COsFlgIoiycnpLcAvvQ9F0awNPU8KJ7yAgum6TTRIVMfgOhj3wpZBCkvRWgt3aWS-QL0k9Ld4CItVAm5JUJnLLmnpnNiQHc_VuOEi3exEVbOO9IqVt24_Ozl7RQYtrCJ251uI2MggL2065ijMLYppZ36xRjL_nQdibe7SDvHBgbiGrEHAJzhwBJ4FW6J1gq2wHC1d-HfjcvBdkY56qFuvOMyPIbl2zyLKlgklfNGtdLCFN4buXtf4JOZzkJ37J1K9oBMnd6N61QVPx_BxGclcA9X1pediNWjyyA7yy2fNXryf1WU4KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Lru8DlRece44wutcGsbbLu23h_GKxQ3iA43COsFlgIoiycnpLcAvvQ9F0awNPU8KJ7yAgum6TTRIVMfgOhj3wpZBCkvRWgt3aWS-QL0k9Ld4CItVAm5JUJnLLmnpnNiQHc_VuOEi3exEVbOO9IqVt24_Ozl7RQYtrCJ251uI2MggL2065ijMLYppZ36xRjL_nQdibe7SDvHBgbiGrEHAJzhwBJ4FW6J1gq2wHC1d-HfjcvBdkY56qFuvOMyPIbl2zyLKlgklfNGtdLCFN4buXtf4JOZzkJ37J1K9oBMnd6N61QVPx_BxGclcA9X1pediNWjyyA7yy2fNXryf1WU4KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWIzn9idS-8q9a9atecgyOCWAC99townE81uSYYSuqbb7mzB6MqeRcuJOSTtnBXUzvpduJ4UC4ceb1MzMVh2bOEUTUjW-INcLcbUP8_WHZ8zHBrRBi1BGOU31fZTMJD7Li1gEK06ysOMkbGHlb0DmPgb4LPnF7aWedA4jINZRjk6GmyGLL6rSBXTqxMVhcmIUtld9GIpl5N52-3FJYqUvI4cp9-zpSCTYDQuJIoi_ZGCUy_vyL58Pw8Ik0RAB36_LWrKEpd5-PGrTcJM9mApTExDMA75b74bKJCkwrhVrXk5ISllwNxY5fh3zPO8Q2ZRjw6KQvkJn6tLxKJmhxA9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2JanQtVUDqJfQC2HD7DSCAVAKp-AMjxnJCIZtDuQzY_b2oHRvAExQY1tlvIW3Sc__4IHzuJIskM7nZLcKqCMi99cjAtgT7WdGHV9awV_Iq3kkXVCDQbWFyj5KS3AaT-3vHfLHp1eu8Hc857bfzijF20qzyG6d3LwLN8vKL7c3tJWBdHFocHvoSmf933xDvgJyhtT_b_TdVb4YYE6jGcq-mR_ecIJyRpGVReJHJYkTgxTxXla1vH1GptQvLu0uMFzp9u7Zsn3yhpH6EuIKPCM5yal8haioCmgStMyuxuwivdMNGiMaQPZiZl_hrC-pc_dNnjbWtOHkWVuv-OFQjeeKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2JanQtVUDqJfQC2HD7DSCAVAKp-AMjxnJCIZtDuQzY_b2oHRvAExQY1tlvIW3Sc__4IHzuJIskM7nZLcKqCMi99cjAtgT7WdGHV9awV_Iq3kkXVCDQbWFyj5KS3AaT-3vHfLHp1eu8Hc857bfzijF20qzyG6d3LwLN8vKL7c3tJWBdHFocHvoSmf933xDvgJyhtT_b_TdVb4YYE6jGcq-mR_ecIJyRpGVReJHJYkTgxTxXla1vH1GptQvLu0uMFzp9u7Zsn3yhpH6EuIKPCM5yal8haioCmgStMyuxuwivdMNGiMaQPZiZl_hrC-pc_dNnjbWtOHkWVuv-OFQjeeKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=dGgRPcdKO5muB92P9b1D0JX3UexE_PsQ8NoXMwBLVeH9nUZD20cQCm8mUiq5j1A0nyqscImHG0URQ7ty94rQ_AN1zJOQipGQHdl0SzUL7umTz5OiYtO3x91fLSpYXozCbmhEHGqiHN2AOAZlNosQcfhoNSj2Ulo8klbsM2ZiieJoCq3E7W_46dX9GqWHu7JXxzICPxNnZhjIBcJQ_tD5FCE0xfZdwNNBE7mFr5IODyEGB3cOy4mvCybv7ITpxsV8rmHSBvMMTqzecMi0mddTMISYAno2iz3aVmDOZ0ny2oymRTGyxRIXXB-ZuTtqsRi8N87Rxth4ASwUQD9kDwFdTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=dGgRPcdKO5muB92P9b1D0JX3UexE_PsQ8NoXMwBLVeH9nUZD20cQCm8mUiq5j1A0nyqscImHG0URQ7ty94rQ_AN1zJOQipGQHdl0SzUL7umTz5OiYtO3x91fLSpYXozCbmhEHGqiHN2AOAZlNosQcfhoNSj2Ulo8klbsM2ZiieJoCq3E7W_46dX9GqWHu7JXxzICPxNnZhjIBcJQ_tD5FCE0xfZdwNNBE7mFr5IODyEGB3cOy4mvCybv7ITpxsV8rmHSBvMMTqzecMi0mddTMISYAno2iz3aVmDOZ0ny2oymRTGyxRIXXB-ZuTtqsRi8N87Rxth4ASwUQD9kDwFdTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=RW8lQ0t19pyqnxGmpT9lrZ29LL7t0_FYw53q_3K-dchaJc6IKRJwUVoHTznqIHbMm6wOrV3zBDGUVc0n22m1mppbxRy82Imh0VoyxuJ4gdexW6DleX3iz_L2tklh7fNBDHiy54aLrPP-l5-9jc0Oty0n94pe3KBOBvFCPjVhbnrzM76QPO9IbbedtrJvY8yh3py-6xiobw4xQ0VC46WvdBfa9IK0zv85BHdRFEdqET0qKkcu4_EgGH2973s_yU_yXGjBDTmYwlEkeJ6mLQE9C-ueqZEc88RnF2BfIKPWhL1PcQHkk-HotRAQpw5YMXPz4yn2COhlJMR_xb-KyzzPSIeGbfOCeybm8F_euklAgI68Z1BKpghIhvPJ51xfIqATcK4uFtbNltGqdyrfkYAdVoKdhNfY6BA1aoxPzlGfpS9SH3kVrtmsrEKEdthEGSHapP9you4ioxUtvNyk1MRoPOJtKXLFMj6vgNdTnX2ERRb3m9uWQ-1P0WB5ynSVwYZmKV1x0pdNivN0Wn3AL-8-o3mD-DFb4-ItjZlRrq5xNlh9qjjNjSX1ygmMwgF3vo6Yr4O5RmLAZGZcUGnmKbKCFF20KDRJC-vsO010SrCfPLGgFv2cPzX7ng59F0lmbyZeKDY57GGxpXoIXpDidWF0V9ZQPnaOdSx958XhPNDWmBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=RW8lQ0t19pyqnxGmpT9lrZ29LL7t0_FYw53q_3K-dchaJc6IKRJwUVoHTznqIHbMm6wOrV3zBDGUVc0n22m1mppbxRy82Imh0VoyxuJ4gdexW6DleX3iz_L2tklh7fNBDHiy54aLrPP-l5-9jc0Oty0n94pe3KBOBvFCPjVhbnrzM76QPO9IbbedtrJvY8yh3py-6xiobw4xQ0VC46WvdBfa9IK0zv85BHdRFEdqET0qKkcu4_EgGH2973s_yU_yXGjBDTmYwlEkeJ6mLQE9C-ueqZEc88RnF2BfIKPWhL1PcQHkk-HotRAQpw5YMXPz4yn2COhlJMR_xb-KyzzPSIeGbfOCeybm8F_euklAgI68Z1BKpghIhvPJ51xfIqATcK4uFtbNltGqdyrfkYAdVoKdhNfY6BA1aoxPzlGfpS9SH3kVrtmsrEKEdthEGSHapP9you4ioxUtvNyk1MRoPOJtKXLFMj6vgNdTnX2ERRb3m9uWQ-1P0WB5ynSVwYZmKV1x0pdNivN0Wn3AL-8-o3mD-DFb4-ItjZlRrq5xNlh9qjjNjSX1ygmMwgF3vo6Yr4O5RmLAZGZcUGnmKbKCFF20KDRJC-vsO010SrCfPLGgFv2cPzX7ng59F0lmbyZeKDY57GGxpXoIXpDidWF0V9ZQPnaOdSx958XhPNDWmBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=m3wd_ziGu2eehfuZ6H4CrUuWvsYBSwgZOYzkyjIns_0OwrA7tdq8yRtDktLkWFLtHRkDgVJsbJHXvDiNw5DHXFrNV4VuJQhS1qScq8hBvLhWDt8jttpNpcAkY5rb4UuCfnZ5bJHo7MoxehqrgSPzKAxUBKFhjlb_cFPtnPit-K6xQLQlooDCQy4M5jG12PjzhQedGvbfdbIWAmww5QV0lhFAKulvR0bxKsAiTRPFFQeayf753x84KjR-3TvgGDPO5F_vDYZEAMjMgolUNYorVzPPwTqHcUcC5QCfGFkeEgwZrRednQdiGn5HGu9uwTxpLFNiFnHdHzzF0DOFiiPz2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=m3wd_ziGu2eehfuZ6H4CrUuWvsYBSwgZOYzkyjIns_0OwrA7tdq8yRtDktLkWFLtHRkDgVJsbJHXvDiNw5DHXFrNV4VuJQhS1qScq8hBvLhWDt8jttpNpcAkY5rb4UuCfnZ5bJHo7MoxehqrgSPzKAxUBKFhjlb_cFPtnPit-K6xQLQlooDCQy4M5jG12PjzhQedGvbfdbIWAmww5QV0lhFAKulvR0bxKsAiTRPFFQeayf753x84KjR-3TvgGDPO5F_vDYZEAMjMgolUNYorVzPPwTqHcUcC5QCfGFkeEgwZrRednQdiGn5HGu9uwTxpLFNiFnHdHzzF0DOFiiPz2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiQjpaG4E00iNhMQWJZJHX8JLzc6kK1fPL0SUkyL5SPpJ4L-zqsK-JcON0oNlunSUNbJ0THFfWpYIrIFpEEg9IrNE5ytyAIE76G9ej2hZxlh13QxlfLHsQ5gXd7KlF1eKNA7eTNMxQXBAFePJC0qSIx5f57udHj5Xz3g5kMEnUhCaz1reNh9PkryfZ7nit5XI33pLaqFuhn_ccbzyX-FbBaaKWgukvNkFYyWkCIdsTocwmFKVQoQOISUR9edpb1MyhLHMkhV2iWcTupQ9e0CUPqrh_9Cwscm9A0FLRgl5g7WZXoozHnLie8rfPWBbBjf7nKVBrCKMQjbsVY0ZQuTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=NxrI7Khubil9KfEqadgpnD_-cvpqlee3c9YFF_DNUMMtQ8H9fbJ5aR-s2D2JVjatj_ZdalEEMmnuFNzylvpw1MT3P8cKN4yFWxEkk0VUvxbvY0eGbsWiVIdhDURkw5PoVdoMp-fi_hr_UE3LBu_Fw27MePrieIQ2k74yupzPQ1mQXWMn3_GwsvgOcGOPpoFRGPhqu3K0WMdXaKaJd6bFTSKSfYdA2-2WQ16OA11HKaF3GABzG2Ki7aMLmDPsMfjrfqf-2LsWnKVETknac_564R-MGA4Op7BcG1oL8zlYmUGPHt_jb5jA8GghJbFgZ94MAUS1JxBPduHBNilObU4MXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=NxrI7Khubil9KfEqadgpnD_-cvpqlee3c9YFF_DNUMMtQ8H9fbJ5aR-s2D2JVjatj_ZdalEEMmnuFNzylvpw1MT3P8cKN4yFWxEkk0VUvxbvY0eGbsWiVIdhDURkw5PoVdoMp-fi_hr_UE3LBu_Fw27MePrieIQ2k74yupzPQ1mQXWMn3_GwsvgOcGOPpoFRGPhqu3K0WMdXaKaJd6bFTSKSfYdA2-2WQ16OA11HKaF3GABzG2Ki7aMLmDPsMfjrfqf-2LsWnKVETknac_564R-MGA4Op7BcG1oL8zlYmUGPHt_jb5jA8GghJbFgZ94MAUS1JxBPduHBNilObU4MXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=ublcLkFYYebZURLRRFRXDhCdu4KXful1cdNoZf3KAgi7P5L2r9gQqaF9-Uh13Ol5ZdK-y2j8nhbPduBZqC0-4Ruf0V0A1F1RIaKWB01xHWqttiJDW9lx04mRbz-kvc54vXyVtF3y0DlH_wS3gLnzD3YYlTj49NOnql6BV5qjmxUI21zP6jZW2G5qcK_YVl99FrMNO8JLQniUdIMYyqNkJUX7gzWE9ZOIIWSoSX3tZiZ3nt8UmRc_kNB7ur8l6cXAr41_s7idvWnLcgKsjyFFAR4cCRWtOzP3621DqUZ0fa7guHMpUO4ww5K8b_nGsxa_S_-Ty_IZKY7nDTStX6o1RyIpftRFQBmdfokh36unBB_9Gmgva4MX5OfZSF8QNmuibOei5E8vi0y_eSGIU47rj-BsWNXcQj56pxR_TMCMjLkPCoarnTVjPef6KrkDXoPMfAwulxMaC8vmx9QFoBAaXZaLai2e5a9mXgfqTESso3hN23EFkeVz8XBQxke4iEwx2666rbYHnW1GZPgz2bMO7N3WfM7kRpVM6iCLTeFYenE8WECc6yDsojns0xvGowKIVzy886kQcZ5hJt0_Krw3V8pYN_DiPl1Dd_lM-7UnKb5nxqteNxd_kcIdtvH6EAZYbsahIW9IMR5IJdFHI4bdjmo5u2_-FsOoJDiSaiKgpSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=ublcLkFYYebZURLRRFRXDhCdu4KXful1cdNoZf3KAgi7P5L2r9gQqaF9-Uh13Ol5ZdK-y2j8nhbPduBZqC0-4Ruf0V0A1F1RIaKWB01xHWqttiJDW9lx04mRbz-kvc54vXyVtF3y0DlH_wS3gLnzD3YYlTj49NOnql6BV5qjmxUI21zP6jZW2G5qcK_YVl99FrMNO8JLQniUdIMYyqNkJUX7gzWE9ZOIIWSoSX3tZiZ3nt8UmRc_kNB7ur8l6cXAr41_s7idvWnLcgKsjyFFAR4cCRWtOzP3621DqUZ0fa7guHMpUO4ww5K8b_nGsxa_S_-Ty_IZKY7nDTStX6o1RyIpftRFQBmdfokh36unBB_9Gmgva4MX5OfZSF8QNmuibOei5E8vi0y_eSGIU47rj-BsWNXcQj56pxR_TMCMjLkPCoarnTVjPef6KrkDXoPMfAwulxMaC8vmx9QFoBAaXZaLai2e5a9mXgfqTESso3hN23EFkeVz8XBQxke4iEwx2666rbYHnW1GZPgz2bMO7N3WfM7kRpVM6iCLTeFYenE8WECc6yDsojns0xvGowKIVzy886kQcZ5hJt0_Krw3V8pYN_DiPl1Dd_lM-7UnKb5nxqteNxd_kcIdtvH6EAZYbsahIW9IMR5IJdFHI4bdjmo5u2_-FsOoJDiSaiKgpSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnxG0xUnR-bpQWp9M_3-Y4tWz7L-i23ckTMZRIewTgB-gdD_2JN9C0xx59mTs9cWgs5gvcGVhLrwOSA_OLd7xqg3dU1IFxjUotKkyDZgBe2S_bpdc5mLgBcj1Hq8P-pbB56WNPF6qMKObcwgwjt_lEqjLm3bZwH0EDhQU_etrCAhx8ydoNLxt9PXuBG9oh6n4hTsRu7v5fTLNwKvhrD265_3WMyAuTCEX1ONpWZ_d6TNeOV5aqTa7HwoNDgTvv1hyxmKiq9_zrQTuwUi8KSaq8aAMshoBV7MRmsuh1kgzTWdhcBMwr5hXW0hPAp87N9mV-oRs0hD_mTQjG3hdh0UoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=VGHQEwH6gqpRKvIzXR986xLL4S8g9aYmcitztpe8XP3g4onvSRM9Tx0mM4UYMkzS9vmxS88pqYZGbr-KSkOgi3Dtq5v5rckuWiRetlhdCwkCPD5RQnjk6npsOnp1dV9qAr2PM9zOC4iWjAkjxbxTEENFJ3x9D4wTOnfZh_HSzLgfSer13FJWpMrENR1Qs-fhASCjGBLCIk5LuZhtO6tuUz_ALro1b9JMWGHNgOBMnHjNeBfk0ajxVgp9ZneYRF9kcm-aR6C0SjXuT1QA_VXSPzk2K3pFNIntEkVhwlqYDQIS1rTP33aRWmkLcJQgUAc3C3ZMDK5TAisSgssiGlNi0UuCkuf7cLL23gk-W4sr_YTzZOjVmYAjqenWltGTcv5J34klr4g--uWuxj9ilqXLjYvYvFJZs_Bq_aWtpHddiGbmKmRbOav9bpOg4V6_3MY5dcrvJxTv9byffjyvEYuZk2mpaTF19Gy9m5_XaVWRVNoxf7LeK2U76Go2DZMjDQQ9Ihsa5OHYgBYjLPlngU-pPZGZS1st602NLx36-08hr_oI3I6GHrF8svNedEDA4MMLOqwy0RXWlgBkrGkJrpuLOY0vGunm-P8-JIWjmdXfSN_fhNoFz09IKU8XwzeLa6YEd85EKFTB8MXHrXJBY8ZGOzfNMY4pHHv458Offz3PF4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=VGHQEwH6gqpRKvIzXR986xLL4S8g9aYmcitztpe8XP3g4onvSRM9Tx0mM4UYMkzS9vmxS88pqYZGbr-KSkOgi3Dtq5v5rckuWiRetlhdCwkCPD5RQnjk6npsOnp1dV9qAr2PM9zOC4iWjAkjxbxTEENFJ3x9D4wTOnfZh_HSzLgfSer13FJWpMrENR1Qs-fhASCjGBLCIk5LuZhtO6tuUz_ALro1b9JMWGHNgOBMnHjNeBfk0ajxVgp9ZneYRF9kcm-aR6C0SjXuT1QA_VXSPzk2K3pFNIntEkVhwlqYDQIS1rTP33aRWmkLcJQgUAc3C3ZMDK5TAisSgssiGlNi0UuCkuf7cLL23gk-W4sr_YTzZOjVmYAjqenWltGTcv5J34klr4g--uWuxj9ilqXLjYvYvFJZs_Bq_aWtpHddiGbmKmRbOav9bpOg4V6_3MY5dcrvJxTv9byffjyvEYuZk2mpaTF19Gy9m5_XaVWRVNoxf7LeK2U76Go2DZMjDQQ9Ihsa5OHYgBYjLPlngU-pPZGZS1st602NLx36-08hr_oI3I6GHrF8svNedEDA4MMLOqwy0RXWlgBkrGkJrpuLOY0vGunm-P8-JIWjmdXfSN_fhNoFz09IKU8XwzeLa6YEd85EKFTB8MXHrXJBY8ZGOzfNMY4pHHv458Offz3PF4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=ibXdpB9wqqKdBFvzgd4BsB8OdmrXhhzViYsc0V3HfjraszlSQ7Z1iPVOPMZA9A6EQI_9oQiFPwt3tdka1PT6rep0RmutAaDyudyGqZhXNJTF9PNSmtplCmyoBymOPlgRLoofo-uboQbrnUehfApOZj-JUygFvvqLS_o34xnZDmyuQsMfBnv5VwRysRINQs-4Cv2pyIg3Fsr5Tln12fOzTAHgRBUA6Z7NmkKivNPrj0hltT5lQP26FSapd0bvDI2iYP-NTwj403iYQGNT7SZvHvTroWAxA9USI-0JcZnqkZ2UsxLcX2bUgJSk7Fd7LDvH6XdLaJoQMW71IXGWAF1TH402C7JlzW5gQlgz5ZpZE6orgc1JHmzpM5CG8LYUau1m4vciNTUUrEys8OkZa8IUh3LjesFTQeJuao7hARBxkmDp4UvCmG4j2L8o5OVWZhdQR2ye52DJgFjLC1dl2niQS7H0SoBeIaldcOFVTEwdhuuhXjqYtYKY__r5Q6ZB0Lx2IHDfpMGdVEqHe1GQfyGx8JaziApNrKzfIVu3hFJd8bx2P7T5J64KuYuYgOrLvUzM7XadadctuKdeQjZznlJWBASYokca8Yq-AbP1ccsBp39uxhuFPS0kFppXwoGL97S0YCb3GyQyhKIGxnr7Ujt4upjJbfWPZNwwWi_wvUjYQJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=ibXdpB9wqqKdBFvzgd4BsB8OdmrXhhzViYsc0V3HfjraszlSQ7Z1iPVOPMZA9A6EQI_9oQiFPwt3tdka1PT6rep0RmutAaDyudyGqZhXNJTF9PNSmtplCmyoBymOPlgRLoofo-uboQbrnUehfApOZj-JUygFvvqLS_o34xnZDmyuQsMfBnv5VwRysRINQs-4Cv2pyIg3Fsr5Tln12fOzTAHgRBUA6Z7NmkKivNPrj0hltT5lQP26FSapd0bvDI2iYP-NTwj403iYQGNT7SZvHvTroWAxA9USI-0JcZnqkZ2UsxLcX2bUgJSk7Fd7LDvH6XdLaJoQMW71IXGWAF1TH402C7JlzW5gQlgz5ZpZE6orgc1JHmzpM5CG8LYUau1m4vciNTUUrEys8OkZa8IUh3LjesFTQeJuao7hARBxkmDp4UvCmG4j2L8o5OVWZhdQR2ye52DJgFjLC1dl2niQS7H0SoBeIaldcOFVTEwdhuuhXjqYtYKY__r5Q6ZB0Lx2IHDfpMGdVEqHe1GQfyGx8JaziApNrKzfIVu3hFJd8bx2P7T5J64KuYuYgOrLvUzM7XadadctuKdeQjZznlJWBASYokca8Yq-AbP1ccsBp39uxhuFPS0kFppXwoGL97S0YCb3GyQyhKIGxnr7Ujt4upjJbfWPZNwwWi_wvUjYQJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ophgg5MOccIpSa_9btdyep5CsKyMmW_-yh9gm7hQFFX3D-L-MxVzY6jPgPeKp1ys8RMS5e0PN0Q7YIyIQb5fkw-z636cCrfFMAM0GLgCZtk0gzMERb7ieX9mKbxby_3zAezAhFxxayOJT0KylOTuLLKfZk36RaMZZo-Zh4gpXZwNql3CwRBC4dDQv1rtNAeroULe0wswdbb5ou7Sm7FM4eqlYGIzsddWw-WIhYyNpeTClgKJhZeO7ZJbYVDUTDXm88adBbL5KfaWde4_hIQ1tWik4ek9jCg5aMJm9ckZDXqynp4yHhVtWnDz4lhfxvvezWqWMYpsfRTtXGvhkjzocA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ophgg5MOccIpSa_9btdyep5CsKyMmW_-yh9gm7hQFFX3D-L-MxVzY6jPgPeKp1ys8RMS5e0PN0Q7YIyIQb5fkw-z636cCrfFMAM0GLgCZtk0gzMERb7ieX9mKbxby_3zAezAhFxxayOJT0KylOTuLLKfZk36RaMZZo-Zh4gpXZwNql3CwRBC4dDQv1rtNAeroULe0wswdbb5ou7Sm7FM4eqlYGIzsddWw-WIhYyNpeTClgKJhZeO7ZJbYVDUTDXm88adBbL5KfaWde4_hIQ1tWik4ek9jCg5aMJm9ckZDXqynp4yHhVtWnDz4lhfxvvezWqWMYpsfRTtXGvhkjzocA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=uOLImnBXgrqDZBx2LjXmzjnranX4qZAcX0-zJTI6Qr8VABUjP1idPLtsDwnPnpshlakHkGLe3XmH4kbc-03-RXL3bq0chUCfzWcL62E_IKEFu4-NTyR605uuimfe_zb9Wi8Iyye53N8qsZixbMM1x_GcOG0_cr-falBjowLPEWjJvawZwcD1z4weAZmkX3cVqK2nJAfo6169mCDysvJXP9e9PYRMx5b1tnsnyaQf76D7PLXmvRqLfVhRyc4CdH46p9TjRRuxlPB2yUQXm0DdllbsOaf7BKTl3y1ViHpP9j9B2FGmdmRbtMwdBkD3xIc9RD7MU9Jvrsp08R6BhZyCbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=uOLImnBXgrqDZBx2LjXmzjnranX4qZAcX0-zJTI6Qr8VABUjP1idPLtsDwnPnpshlakHkGLe3XmH4kbc-03-RXL3bq0chUCfzWcL62E_IKEFu4-NTyR605uuimfe_zb9Wi8Iyye53N8qsZixbMM1x_GcOG0_cr-falBjowLPEWjJvawZwcD1z4weAZmkX3cVqK2nJAfo6169mCDysvJXP9e9PYRMx5b1tnsnyaQf76D7PLXmvRqLfVhRyc4CdH46p9TjRRuxlPB2yUQXm0DdllbsOaf7BKTl3y1ViHpP9j9B2FGmdmRbtMwdBkD3xIc9RD7MU9Jvrsp08R6BhZyCbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=mj7d_81opUH-ZDlpzKjlZnHimcBfewvml0qX6rJUBDNbcM09fupKQBovAOvHpWgXcSF7cR43KCf0X1coHQvWnRvLzs8iJxHO8BoFeh2eisfPVsZvsE5dPdBhevYfKTh0HvSLN1LK2CANknDASYd9THKgu4qy8jV2YmNa3LShhA8PGRouC8aBFIBtCXx4z9HxAdfZLlMDGRLMTMsZp0uUjpxA0N5-v9k0yXPyHrAR7qbkF5B4slor9ACyX3N-0zmj8HiSSlkI7wxTub9H8YlqTk3YAqoGZzIqEYhmEHK5T29FNYIGHbzLgvRzb6C4x6VRgqmIMJp0mwpvr9qb6W4tSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=mj7d_81opUH-ZDlpzKjlZnHimcBfewvml0qX6rJUBDNbcM09fupKQBovAOvHpWgXcSF7cR43KCf0X1coHQvWnRvLzs8iJxHO8BoFeh2eisfPVsZvsE5dPdBhevYfKTh0HvSLN1LK2CANknDASYd9THKgu4qy8jV2YmNa3LShhA8PGRouC8aBFIBtCXx4z9HxAdfZLlMDGRLMTMsZp0uUjpxA0N5-v9k0yXPyHrAR7qbkF5B4slor9ACyX3N-0zmj8HiSSlkI7wxTub9H8YlqTk3YAqoGZzIqEYhmEHK5T29FNYIGHbzLgvRzb6C4x6VRgqmIMJp0mwpvr9qb6W4tSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=GIaCrzKA4gAmCeSZl9UCLTLUCOwNXXyCgLdqmAbIEKXhV7XziHdylwRCtg_wBqkf10lypbfZI_F9_wMGjXF3FkrQsTATlakHwZ9dq_icQ3JLHHgQui0lgRehLmRoJDRRef2QiCL3PC05LRmbz6a-A_o9l6-eENVzljQAExOfUUtugGtHQ6p_b-sg6-38B2vC-0Ordybv2Ew9UTasueHjv1N66NZwDh5uHCcSbGqgv9VCd_rMmZKDokruIfdy9MYa5WU05vAGJ-cvxy2V7-vK9JVa1T26fh1nIapwVeXMJA_ai9V0R-E7WpXe2vHPszmT2fL8wLRKqqJKHuMS0JSAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=GIaCrzKA4gAmCeSZl9UCLTLUCOwNXXyCgLdqmAbIEKXhV7XziHdylwRCtg_wBqkf10lypbfZI_F9_wMGjXF3FkrQsTATlakHwZ9dq_icQ3JLHHgQui0lgRehLmRoJDRRef2QiCL3PC05LRmbz6a-A_o9l6-eENVzljQAExOfUUtugGtHQ6p_b-sg6-38B2vC-0Ordybv2Ew9UTasueHjv1N66NZwDh5uHCcSbGqgv9VCd_rMmZKDokruIfdy9MYa5WU05vAGJ-cvxy2V7-vK9JVa1T26fh1nIapwVeXMJA_ai9V0R-E7WpXe2vHPszmT2fL8wLRKqqJKHuMS0JSAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=mPCxauMEt16iFC4arobxe-3jRy76baOjGDeL_17W0c5hArzJy1malI2hKUfpPeWs-6a4H4Zk7RNgBNXytD4G-eZOL3b4IEmLPJe9yjPHdJhjKNp7DMDIeqtEz1GyF0UKogpq97amayUfrVsMTXUzlPEEYRBLAJhAlJEfyQFcHnbFhRBNJsySHh_sat5ZA87EOqwit64CkaAF2kNvZUF3_ToZ2s7MoIgz3l7UE5TAGEvnE1VP499DVbPIKBdIOBqgzpFFZ3eAzAvsnlg-44r3IUkusaBnJOMDBdEPuXKqjotRRWndyGKsowvyU8zgTOHEv0t4GhRiURpI2BsWIXFgdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=mPCxauMEt16iFC4arobxe-3jRy76baOjGDeL_17W0c5hArzJy1malI2hKUfpPeWs-6a4H4Zk7RNgBNXytD4G-eZOL3b4IEmLPJe9yjPHdJhjKNp7DMDIeqtEz1GyF0UKogpq97amayUfrVsMTXUzlPEEYRBLAJhAlJEfyQFcHnbFhRBNJsySHh_sat5ZA87EOqwit64CkaAF2kNvZUF3_ToZ2s7MoIgz3l7UE5TAGEvnE1VP499DVbPIKBdIOBqgzpFFZ3eAzAvsnlg-44r3IUkusaBnJOMDBdEPuXKqjotRRWndyGKsowvyU8zgTOHEv0t4GhRiURpI2BsWIXFgdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Q97wSFDnFeCYcUB0taAEcjqYEH4ukmZwj6M1M619xYC34VzGG97EQAHj30BgtL8Yhtc_1Xsp23IatAps4dpzK2BE0hMFLKtJOrodGqSFqmdMelMc6rEfvarOJpawCV5SN7pWi0t5lTVJycGHfythWsY9jaf8KXDT_qY41W15AvMzbhDDOaPvMnFjGSfHfGerSupPiD3FquDQueMa_TTwKmFbGJmquhhMzpKtgpfxJxUor7cpMTvkFcB14UURnMqj8RV7IVLwgWHFRS04-CD7HVltW-b7PS07BkYuGnhEWsPlQvR66FEK-3mp07GqtqDztweu3fyo7J6cGLS0EJ86GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Q97wSFDnFeCYcUB0taAEcjqYEH4ukmZwj6M1M619xYC34VzGG97EQAHj30BgtL8Yhtc_1Xsp23IatAps4dpzK2BE0hMFLKtJOrodGqSFqmdMelMc6rEfvarOJpawCV5SN7pWi0t5lTVJycGHfythWsY9jaf8KXDT_qY41W15AvMzbhDDOaPvMnFjGSfHfGerSupPiD3FquDQueMa_TTwKmFbGJmquhhMzpKtgpfxJxUor7cpMTvkFcB14UURnMqj8RV7IVLwgWHFRS04-CD7HVltW-b7PS07BkYuGnhEWsPlQvR66FEK-3mp07GqtqDztweu3fyo7J6cGLS0EJ86GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ipds2FhleP1-2bxvnEYB3c5onhwJvfnBEwq2nOisW5uLTVZJPM6KsyhK_owYtU8zmMWLKDzdKEHjf1qmid4-BkYUxh_--551434Ipz7MiNtttmVedsqwXd7PhjohMkIB59ube-HlvrK1_VYhrd-4SZrVhzc6JGZUbfEz6RKrcpMqTpqjrJJeUcYsbYSj2IJS0EReTicVe4sKyWD2AH7q2nL7baCXyBkaj8iyXiN6zJ7SaAjHfgvS8KUUIHOJlJ9XbErlQgu8L2obCoBUnwUB-nhR76ALhPF6vOcQUqyGiSu7U2ApW_o0fhh8_9tpJ4UiNSAqg3K9cM2qQToBGpIh7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ipds2FhleP1-2bxvnEYB3c5onhwJvfnBEwq2nOisW5uLTVZJPM6KsyhK_owYtU8zmMWLKDzdKEHjf1qmid4-BkYUxh_--551434Ipz7MiNtttmVedsqwXd7PhjohMkIB59ube-HlvrK1_VYhrd-4SZrVhzc6JGZUbfEz6RKrcpMqTpqjrJJeUcYsbYSj2IJS0EReTicVe4sKyWD2AH7q2nL7baCXyBkaj8iyXiN6zJ7SaAjHfgvS8KUUIHOJlJ9XbErlQgu8L2obCoBUnwUB-nhR76ALhPF6vOcQUqyGiSu7U2ApW_o0fhh8_9tpJ4UiNSAqg3K9cM2qQToBGpIh7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku2Px1GoB6Vb_DkZ11jVw-O6wA4agugPjhQbHCv-uOB2gcidodvZ_U6XPAcanKhP6XIveA7vXVe0egMEDgFubi9ISkDi_55S8pcaXNUoq7-buAbsgRQZXP8amM_O88U24Dpf7EX047N_WkWet5vl7XwwYatIPFHI2wgYbmnEXBqkqMeK3Kj0yZvG5v-Lt_RX_LnJRdFL4095BzP70pAxhxemUQ27ueOsq4__xL23RzBOGTF5zb7bvcZLCcJT8xv--r-cTpwUVOtKr9ggeu7PrsIHIbS72UbiL5kvKVP8hTKx6cVh3Hn7EMqC64NIe1MPX0dXXUxyValFLTVDuWEEzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=L1sV-X2AtTOMwewi0eclINHAiCLZKIbY-UmvJC3Vk4bBDlNXIKLdqb19DcwIHKuRMxoIkvHnoseZ3nc2gXiBf1gBCU_CZVmsULEBieN1jh5tHWvEm7l4MV7M87LaPLslQvwaKYzujbYfcSunJ2Wjmhovg1WJUZKV_8UI-VJ0d-iQnuUJIIPOpJoErA0kYelqc0Uqyc61V68BH-vYVdyaYqh5WAdluQcHHwZ9reOMOzyoFCDn4UoxdRtm7_CFLkwlniv0QA2Bu4xWMfSDA4R2els0HwMVk_UNTZtJuA_Nu4MLA05oh70AgCCC7M0UUoY-Wzh4v3h2Uv77hhqv8zOJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=L1sV-X2AtTOMwewi0eclINHAiCLZKIbY-UmvJC3Vk4bBDlNXIKLdqb19DcwIHKuRMxoIkvHnoseZ3nc2gXiBf1gBCU_CZVmsULEBieN1jh5tHWvEm7l4MV7M87LaPLslQvwaKYzujbYfcSunJ2Wjmhovg1WJUZKV_8UI-VJ0d-iQnuUJIIPOpJoErA0kYelqc0Uqyc61V68BH-vYVdyaYqh5WAdluQcHHwZ9reOMOzyoFCDn4UoxdRtm7_CFLkwlniv0QA2Bu4xWMfSDA4R2els0HwMVk_UNTZtJuA_Nu4MLA05oh70AgCCC7M0UUoY-Wzh4v3h2Uv77hhqv8zOJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=aSZ1v1qRs2wMUhX27e7aPxWv2LrbgdrLtTg6IumtuNECBdTlCrTrLyB1Bp7p8Kp8HKkULUXvRpOegdaVSOo93p5BelmlYByOH0yPHnDDGgCsjQ9dFXAm29uXkZpjTOFKt7_kIXxkTYX6vZgtCgAAGv7_C4-LAL15z1Jzj3vOSqG1LL4XjTBakxNBI7ki-791H2QpA75HWJEokvK_LWU8WiZ3S3gpvJ8DrUlobprK8XvAynd6NrhB0lam31wAadUfT4GqWd9Quu2bKTTk8elusw9HMn2c_22o88C-e_0ftKFMzwEd4-rPW8rMs8d1XOvHcQ65dqyQ-o2t3Z2GJdKFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=aSZ1v1qRs2wMUhX27e7aPxWv2LrbgdrLtTg6IumtuNECBdTlCrTrLyB1Bp7p8Kp8HKkULUXvRpOegdaVSOo93p5BelmlYByOH0yPHnDDGgCsjQ9dFXAm29uXkZpjTOFKt7_kIXxkTYX6vZgtCgAAGv7_C4-LAL15z1Jzj3vOSqG1LL4XjTBakxNBI7ki-791H2QpA75HWJEokvK_LWU8WiZ3S3gpvJ8DrUlobprK8XvAynd6NrhB0lam31wAadUfT4GqWd9Quu2bKTTk8elusw9HMn2c_22o88C-e_0ftKFMzwEd4-rPW8rMs8d1XOvHcQ65dqyQ-o2t3Z2GJdKFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=tkvms2WN_Q8aBMzb9Jf4OfLwBzDP1Ayh6XyPDRCI7KGRD-3eyEwLvXwxsO68i-TpdwYp8wF10IETR3BAnCbeeQARvnaplsKwXg2xFDyryS1cjsK2FqEjFfohLlmbbv7XQoxSCJUY3eBg2MdkDFOxfRfjDYcqe26jcAlmdQCbM8tbYqrYvHnlebfM3FYN_NkneDUhO6hryN-NZ8k_0GeTu1ZvI8c3Q5Wxa8jqBoUVXYPd9r4ZrqE-nYN7k1R7FTduzL8CKZ-lHeqAPQ4ESZaEHPV2qPMk7DwiJDFwl1tcT36b-xuBgcjPkxWvZ5nXmVAO7MxC2LaNg7kb-eu2mVVMZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=tkvms2WN_Q8aBMzb9Jf4OfLwBzDP1Ayh6XyPDRCI7KGRD-3eyEwLvXwxsO68i-TpdwYp8wF10IETR3BAnCbeeQARvnaplsKwXg2xFDyryS1cjsK2FqEjFfohLlmbbv7XQoxSCJUY3eBg2MdkDFOxfRfjDYcqe26jcAlmdQCbM8tbYqrYvHnlebfM3FYN_NkneDUhO6hryN-NZ8k_0GeTu1ZvI8c3Q5Wxa8jqBoUVXYPd9r4ZrqE-nYN7k1R7FTduzL8CKZ-lHeqAPQ4ESZaEHPV2qPMk7DwiJDFwl1tcT36b-xuBgcjPkxWvZ5nXmVAO7MxC2LaNg7kb-eu2mVVMZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=qnp_nqZJ2YNvpdmQXDZNQHmmSiKm7LOixW6z2IGAKdAWNxXozCL4A3tgJwkvSTp6kvENqGWSl64Kobv77GnP0Vzxf92PChuVaUv8FvIZnb-wQj_dk7p9gxu9bo2xoPuZb5E0UcKXL8AdTdakGi5J_Ol8u-PVksA_8NTwjyYkmLWBunqSjTI8kSldlU0ljNv2pbzlP1pwuA4AKoOqY_OAHaoNY6svtYYDUTCL6y238D5sWgavGUMN3SYLJ8mStYOGC6RoLo_2Fy7wzHUmbO0Hx4zRXWhrP5Gr0F6rn1WfSbAkXv4KLOxxkHnlfDajrMMpeXZJ6IStSaEv9F8ixcAYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=qnp_nqZJ2YNvpdmQXDZNQHmmSiKm7LOixW6z2IGAKdAWNxXozCL4A3tgJwkvSTp6kvENqGWSl64Kobv77GnP0Vzxf92PChuVaUv8FvIZnb-wQj_dk7p9gxu9bo2xoPuZb5E0UcKXL8AdTdakGi5J_Ol8u-PVksA_8NTwjyYkmLWBunqSjTI8kSldlU0ljNv2pbzlP1pwuA4AKoOqY_OAHaoNY6svtYYDUTCL6y238D5sWgavGUMN3SYLJ8mStYOGC6RoLo_2Fy7wzHUmbO0Hx4zRXWhrP5Gr0F6rn1WfSbAkXv4KLOxxkHnlfDajrMMpeXZJ6IStSaEv9F8ixcAYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW4ciEk4y8DwY9pwELpohdIDPJMjmUGKq7hm_s7uraLl0J-cfQEzpNl54wMXtyOE2W8UAZUYpjnrTxupk9i7WrSYwzvMj24ZAAc0RcDHRzCDJMmXWVGS_-hBFToC9FWZi0w__ebvSSA6RlYHJJcTcelOmEhUqmq4cnVcR7fEPWlVDC3EhhNe7zxiLuPEGeioSl-EkbepiuSHrSXprp83M3LllPrRTWRumNbnVWe3dkZTBTeGxckVSmUnakQfSYo6uOd6banCor1WbNfSHzYjGIfw8G0VdNDiDjedvmaYNZURZHIWK0OpUvDYgd4pC3Atcc__ctaGB2Cxtq90136LTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=CvvoT8PutbOwk02ldSukA2N30IhMQ2Skx_V9GVDlL0PsFzxQVQR-LYCIpFTT-9P_db_sSRlkiNeOf-36xpyA-M01r_Cf7w8P6vroGDubqdbXl2TfzbI-qP04X8VlT8mg4qS57wSlJD93XXAZPJ07kSZAzOGqTPD0mcFWq1JU_kclSy6m3JqveABt0MlucQxXcQBGS14Wb6__48jS_CMFUZASuguOGG4O1YpGGDEKaOTzYk67FY8P8-6iWmwoEwWzvkoEYjq_L2mQn0rWxNGO4KRMijHCsse9hXvgK8_A2RK0hV2B3TEGDpXEqkCJTaJRBynHdT8g1VpfSosecnaLNjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=CvvoT8PutbOwk02ldSukA2N30IhMQ2Skx_V9GVDlL0PsFzxQVQR-LYCIpFTT-9P_db_sSRlkiNeOf-36xpyA-M01r_Cf7w8P6vroGDubqdbXl2TfzbI-qP04X8VlT8mg4qS57wSlJD93XXAZPJ07kSZAzOGqTPD0mcFWq1JU_kclSy6m3JqveABt0MlucQxXcQBGS14Wb6__48jS_CMFUZASuguOGG4O1YpGGDEKaOTzYk67FY8P8-6iWmwoEwWzvkoEYjq_L2mQn0rWxNGO4KRMijHCsse9hXvgK8_A2RK0hV2B3TEGDpXEqkCJTaJRBynHdT8g1VpfSosecnaLNjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=bI1yje7Dub0gzude3trKN3DrgzmZem5F1QJXpitabUYSV03m8E5BAcU-axhG7cqXAThaQk5tMxTzRhbpzbfiZU94Jm7P5nekadzUUGqvkQ0yrPpcKcEUNc6BdMBbaU4gQfowPdFnel9pHbRiMyrJmPVwj-2cdd2lthBDIysYaSEl4YVhqv6nI6kYgb4z-iZ1Ct_hjtpR9UPJ9t_66zenbQ-k02R-fSVMKkEEh_FRgFSxFFtmhTul75zp0iEaBeNuEXHK4RAA-4arlBpXf18bnmTJt5ihL6Y8ZxkF7y6RnOPcPwHxbACBgkoUNJjH5L7VHp2kSuT04UVuSrqMVv8Sxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=bI1yje7Dub0gzude3trKN3DrgzmZem5F1QJXpitabUYSV03m8E5BAcU-axhG7cqXAThaQk5tMxTzRhbpzbfiZU94Jm7P5nekadzUUGqvkQ0yrPpcKcEUNc6BdMBbaU4gQfowPdFnel9pHbRiMyrJmPVwj-2cdd2lthBDIysYaSEl4YVhqv6nI6kYgb4z-iZ1Ct_hjtpR9UPJ9t_66zenbQ-k02R-fSVMKkEEh_FRgFSxFFtmhTul75zp0iEaBeNuEXHK4RAA-4arlBpXf18bnmTJt5ihL6Y8ZxkF7y6RnOPcPwHxbACBgkoUNJjH5L7VHp2kSuT04UVuSrqMVv8Sxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJmd3qDyngiuqc-k3QOignsvGrjisB4r0c-c_BemfjdTAX0QBoy9ymN-9HiCx72z9R4xQhc2qWwQstwXjXx31o4XRvPrYqQ1HCiguTpcJtPoQ3ey_F789ViP7JSTWpyQ9_6OUS-FZhsfN6veFkOWvT3KjaJIWnS-EdtjTvZXCZ8UZV6CeXJIEgVV5NnS9FBbOKl3AXQSD56ybfVBUyL0-SKOU_t2cWkz7B-CKy2qXCZBVlcNsjOOBjWkYmUc5CA7_fcGUujJTQ1wdP2rb9aJXIhD75IbnvzXu1OwgVazHi4nEyvZ28MJOEP7U5MOh6IoCOFrFaFBrnUWmiwp5GD8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thjC86O4rzbLdCl6WFtjt_08jp4ls53AvGU8V3aruRnSBpIjokJ96rX9H_Jt-dXvv2K170ajwNk2P6apQ03fnNuuwFX0AQimmkpGnT1UO3IjqgMhqr0oMvbqsh53gvSF63cztfw6fSnO-fYlcLA_6RszfBTfzz1tECyAXn5Q4lH-BUbziPzchif0X-a0Shu63RohqdB6rfAjaxr3XFo0J3pbknbAa6CjVvFeFCSURWs9uKCFlOvTSMQq8PpIqP-WhAGcdBDMKCd0e48oavpYzKghHU54O83FDzCyMsX0i5ijZgkqfd6oN5w0w3wqTS4pe8w4lsXutWTsIrdk3x5clw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=nW_yYK23Nf93pCxUwtxDaNbCGnLXBvttbxbxLbcY3kcJHgTHA-rbyqg4dn5ak_-lZzLyhVB2b2G8jXfHkYZICS9vX3YFPe_4-VEvEGz2uVaU_6fbfQW5wdAda--uJ3xTGqUwj3CfuKTK_mFfQAxYOhLJgK0kY5zZ7fQ-cT_35ycKmovu5cp49rfzmgDAmxbM0OGPTnW_Jbb6cV3T8d57TRJ6fyEFTenutW3iYZZbRNfRbYB4Bt_jnmCYnTqszfQo4245qXrqPpIH0MFG1hHWHpZhdBMJPy-bxXoNEqkQZGGMG_Obp_xio2opOvXMTdBbNZHnJ5Soczkw_02ClL8XMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=nW_yYK23Nf93pCxUwtxDaNbCGnLXBvttbxbxLbcY3kcJHgTHA-rbyqg4dn5ak_-lZzLyhVB2b2G8jXfHkYZICS9vX3YFPe_4-VEvEGz2uVaU_6fbfQW5wdAda--uJ3xTGqUwj3CfuKTK_mFfQAxYOhLJgK0kY5zZ7fQ-cT_35ycKmovu5cp49rfzmgDAmxbM0OGPTnW_Jbb6cV3T8d57TRJ6fyEFTenutW3iYZZbRNfRbYB4Bt_jnmCYnTqszfQo4245qXrqPpIH0MFG1hHWHpZhdBMJPy-bxXoNEqkQZGGMG_Obp_xio2opOvXMTdBbNZHnJ5Soczkw_02ClL8XMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr1kpM83Esq4GwkYpm2jX1DUZFv1Bh5gxVKeT07TqAhbl7P69qLFzfmudlSuTDKhawIz8kegCvfRBfjx44tJkpN7uGWRyrMLA3-IDtut7c2-0uLxIv-DSsu6_wv05Zh8-Al4cqs1QTLGcwJDkpLkiqjuScx5tHvd4dwutFZXZsqFa01NswABsEHZRgO_DLyUBZsRHTkRNub-gBdVl8yR2R19pa1tBfOMpUE3sEGyBZYAYHwDJvs5BypNhKs3iBeHeHQDb3SCCt_a-UbTPmRdwRK_hdYY5530U5iKcZ_DNU-4__w9PTfh890wzxGrMKOtwPoxrG8cODVgRVa4SHITQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJyJr4f6El5rUiUKbPCcD0vsw5pgP4VYPMITmoV_R7OeVSVoLS_lup2V44YZ0x8XoLEaVR54XK8kO7RaoFf3MoO2zzU_g7CnZDRxxySX_zm_ZRU2OvtUDF2HAIPlgM_rkMVf_POv7tPPp8tSGKhTJlLOrz6L_YdUb4fi62VAewivyDWbFQTxWIqfuuwub3j-7oJQYwE0_3CmsGw4wzLZaczdJbVcADOPKRJdAD76xcQjFP_EZ8oZuVxRc6236ANYgLNz7h-uz_y0plFwAC5Guqz_YIDKZzIsBbwOZDaiCrS3TUqU6TTFSO9ceYsjhWZoBHAhGukbz8WgqVo3vf9S1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LW8HtPqgOqRfC9PRdoaR_bfA5lvuY4JbEuLmX3Ad52C5XyOIF5tW_I10TH_TjfIpsI7UoJe4HC28N1peIz6VvVnw_yqOEkFT31_nUGoMZJ6QNYNVJ7pnr1yBnNM1ESPKYOmyci99FgUBn4hJffLR345qFBCUxCpqqWzLtoBGAaLnXdh49ko3BXgeWius-Razu1o5m4rFQYE5HdLDbAawZkO8wocGXvM0LRKktyBy42mw8yaZM7IMvtWrgCHyDPdWwf-HnC8M2lqBw_ZxAbMufgZx_4kGp48uEv47FRLhsWVwCWKI6Imi8oKlSEWybwF2HsEI8_vKAKG67YI0k2905g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=moQbsuLap4PwZ07Y-_4QH4GjJ6DEtmOayYhqyL6VRPeXQusTHm2G7mNiJZfLEQ3l6vbGP88xH52JVe6yY31KvOxwnxaJDsivDd2sRLVK8BNMze32U9wq8tlY_8XLzMukQy2a9D9eApJdUiGkyk5xoF9ZdvxAqrMVWUcgMk1tLde4jtcKtIobE1Ay9sNWHfYD_H_tvQTfyTGOWH8VTo50npXKqEJy5Kv9tWYIu3W7n0Z8vw1R5ReU_-kQd-brgnm7RinW7E9HHyIC5n6iBIULtlkdVVIQzmBsqBhuwrWQKZvAv-vf8r5dcMs2erHLjhdwZBUZhVsjZ_TC_xc8TBy8Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=moQbsuLap4PwZ07Y-_4QH4GjJ6DEtmOayYhqyL6VRPeXQusTHm2G7mNiJZfLEQ3l6vbGP88xH52JVe6yY31KvOxwnxaJDsivDd2sRLVK8BNMze32U9wq8tlY_8XLzMukQy2a9D9eApJdUiGkyk5xoF9ZdvxAqrMVWUcgMk1tLde4jtcKtIobE1Ay9sNWHfYD_H_tvQTfyTGOWH8VTo50npXKqEJy5Kv9tWYIu3W7n0Z8vw1R5ReU_-kQd-brgnm7RinW7E9HHyIC5n6iBIULtlkdVVIQzmBsqBhuwrWQKZvAv-vf8r5dcMs2erHLjhdwZBUZhVsjZ_TC_xc8TBy8Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=M37JqxqQCK8o-FKwkBVKjbMcFhn_7dZvI-1TuUUMeNcv0LL3dOIL3iMjtQKqdSapautA7VR2t6jFDAYRMyRjEp61Oho3ncQwRaHuFNvg5jGBFHUzLgv7oubipdHkXBS-t7GjwRuxI7t8mTS-eoEJxrSP8FxwIoTEIK0vz0tBaUHHuTqVQomkqKMYPrDHvMbYcLO5mRUbHXotf2Kjuzk_kAXf_OQBCd6Nqw5NfkFTNGpJI7VDklt_Z4FmNGVFkWCTea9ulxsmJV5UWS9Eqf9dQTgj78ZvvEtODZWjb2ophQOf2erapySP9p_f7LmuDi2pN_PmSxcvZy_I8SYlTx5HSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=M37JqxqQCK8o-FKwkBVKjbMcFhn_7dZvI-1TuUUMeNcv0LL3dOIL3iMjtQKqdSapautA7VR2t6jFDAYRMyRjEp61Oho3ncQwRaHuFNvg5jGBFHUzLgv7oubipdHkXBS-t7GjwRuxI7t8mTS-eoEJxrSP8FxwIoTEIK0vz0tBaUHHuTqVQomkqKMYPrDHvMbYcLO5mRUbHXotf2Kjuzk_kAXf_OQBCd6Nqw5NfkFTNGpJI7VDklt_Z4FmNGVFkWCTea9ulxsmJV5UWS9Eqf9dQTgj78ZvvEtODZWjb2ophQOf2erapySP9p_f7LmuDi2pN_PmSxcvZy_I8SYlTx5HSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=FyQr5SfJG3r1fdYwIPM7eMNsHp55ie-zmabBOQuqhTj9xgUlNUDJeGD0GNJpK_kSSdL2bIcEYd7bjjcUlNsjlus7O7nesDZLYK-HiQym6BW0E54atZ-ApivwOcrRYmy6g7d7k11vM772Wv3xAVY6fNDfVqwqidmlAc5vIy90c5q-q5UQzSn-_1HzDMmlwrwSK2FFk34X6fc4FaciLu0RcDyiplTjKYs7EIfpms833z6uUj9l4yNbh8q_h7KFO84N5NCT-TTit4nXnqvEyZ8x2z9qphVnpeQ3eM2L83bp2-GI9ojkEYSxiyL-lANBHdU970tOB5TI7BjgbG_iVwqrBbM5UtFxVHVqGhude-S2bd_byYUO9YQZKyxo06bdu9OJcqkBWp4SiU1m0ITNP5k0ReChP6sW8JhYEZ4DBXCX7ieUJWoyEkzvZGqKm9clEn8H2o88CeYRbonPQoZzJadAXqgofKfSmRlJ9WxGl4uAcilXcEKVndbWr_mCvDD1ac2OKTCN00AwLmS7Uho7GUvh8yLJxiRPLl4IsVpbNTCPH4vH5IYS-9RLjjO_tKfoFphyJoj9g_EDN0RIoRGFAEyynZVLzGOoAPA2El9U9ikZhtAGdFfeh6_oukXtbjrtRvFHdEy-AZnPZrDEzE0U4i_S_W-seJhCeSwlRMrvthR-mh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=FyQr5SfJG3r1fdYwIPM7eMNsHp55ie-zmabBOQuqhTj9xgUlNUDJeGD0GNJpK_kSSdL2bIcEYd7bjjcUlNsjlus7O7nesDZLYK-HiQym6BW0E54atZ-ApivwOcrRYmy6g7d7k11vM772Wv3xAVY6fNDfVqwqidmlAc5vIy90c5q-q5UQzSn-_1HzDMmlwrwSK2FFk34X6fc4FaciLu0RcDyiplTjKYs7EIfpms833z6uUj9l4yNbh8q_h7KFO84N5NCT-TTit4nXnqvEyZ8x2z9qphVnpeQ3eM2L83bp2-GI9ojkEYSxiyL-lANBHdU970tOB5TI7BjgbG_iVwqrBbM5UtFxVHVqGhude-S2bd_byYUO9YQZKyxo06bdu9OJcqkBWp4SiU1m0ITNP5k0ReChP6sW8JhYEZ4DBXCX7ieUJWoyEkzvZGqKm9clEn8H2o88CeYRbonPQoZzJadAXqgofKfSmRlJ9WxGl4uAcilXcEKVndbWr_mCvDD1ac2OKTCN00AwLmS7Uho7GUvh8yLJxiRPLl4IsVpbNTCPH4vH5IYS-9RLjjO_tKfoFphyJoj9g_EDN0RIoRGFAEyynZVLzGOoAPA2El9U9ikZhtAGdFfeh6_oukXtbjrtRvFHdEy-AZnPZrDEzE0U4i_S_W-seJhCeSwlRMrvthR-mh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=RWZrlQ0Dmfg4W3iRBGSGd6L8gxkqxP_vZOklyr1FrP-6ll9XASai0LumxHjxOt7znUd7COvFHvKt2Z07o1jANNjHfLa17rPc960l_GQL_vNH5D3yIoEIRfZv_VEJwRpSbqI-Eg49iR3zxs_SZ4fLUtbF27ZGVZ_ZnNV_1dp269wKUU-BLHzgF1cnwLKkXvFX_Ep1Zx04st-yyCZ-dkfcPUAJUprYCTXDBIoqGIb_g8Zu-IU4yROVgHB2BuGtrL61ZlYQdtGssbaO5j9JkmksUxONun4d8kA2woBqzv2T4vS1U822vEjU-8snJhxCFSUqipJcVWrn2_ZdZKQQ1jmWRzVvjjbo3nFSBrV_CWe-uqSF0ciqNz_aWDY_yiQTsSndM36Nbxc6PB2I11gdAed9SHvjmGKfzmm4GtsP3H1iAwvVpnTFhpr6togcuxXLPMRofbTcz-dS08jqoDi9VaVg8m2xecZQ7kxX9zeF98PXTYQWNYN-Ozh2mBtbpVMv43MFY2nOhTEPyASzEh6J5EKie07GVDgDTStWGCDlhqiGDDIBt55Nddu7rYtUT5Mu7La0e7OFlCl8dKiSDR0BZeJZZJ3HJvygCrK5QjSC4CcrOovxJmw4wKiuGu2BaUqFsGqqlxB_-Fp4d0SSNXLBi6zcSfy5PYecke19420jbmM_q0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=RWZrlQ0Dmfg4W3iRBGSGd6L8gxkqxP_vZOklyr1FrP-6ll9XASai0LumxHjxOt7znUd7COvFHvKt2Z07o1jANNjHfLa17rPc960l_GQL_vNH5D3yIoEIRfZv_VEJwRpSbqI-Eg49iR3zxs_SZ4fLUtbF27ZGVZ_ZnNV_1dp269wKUU-BLHzgF1cnwLKkXvFX_Ep1Zx04st-yyCZ-dkfcPUAJUprYCTXDBIoqGIb_g8Zu-IU4yROVgHB2BuGtrL61ZlYQdtGssbaO5j9JkmksUxONun4d8kA2woBqzv2T4vS1U822vEjU-8snJhxCFSUqipJcVWrn2_ZdZKQQ1jmWRzVvjjbo3nFSBrV_CWe-uqSF0ciqNz_aWDY_yiQTsSndM36Nbxc6PB2I11gdAed9SHvjmGKfzmm4GtsP3H1iAwvVpnTFhpr6togcuxXLPMRofbTcz-dS08jqoDi9VaVg8m2xecZQ7kxX9zeF98PXTYQWNYN-Ozh2mBtbpVMv43MFY2nOhTEPyASzEh6J5EKie07GVDgDTStWGCDlhqiGDDIBt55Nddu7rYtUT5Mu7La0e7OFlCl8dKiSDR0BZeJZZJ3HJvygCrK5QjSC4CcrOovxJmw4wKiuGu2BaUqFsGqqlxB_-Fp4d0SSNXLBi6zcSfy5PYecke19420jbmM_q0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=FAhg9xlFenAxbbFmOWEbySKXjUVugBL6ASrklJm64RP4n4PfzuOsd9JdQmp4cR1CVodc2Bbq03PyyrBIOI9oJpT0NLT6xskCv850MxqulL6DL2Oe7YWtYdaf6qJodUdTBlkGEHrAWGQ_rA2DkKyFRj-pGN_UJvSIT9Cgx-BEGM4mmmM1kMGKr_1tTDsrAem3_JRmymRXskWlM942mHISOZSMf3kwAyZLV5MAahwnBJspPpasP2__0k-Yk7R5xASdLFEkX4BNCRttPXHOIU_BlhixFHh8aJJqaC8Rvmv_mcWpE4OfiHx6MpMZ5Hni4fWu4CE6b41R6XKJylE8C0tkmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=FAhg9xlFenAxbbFmOWEbySKXjUVugBL6ASrklJm64RP4n4PfzuOsd9JdQmp4cR1CVodc2Bbq03PyyrBIOI9oJpT0NLT6xskCv850MxqulL6DL2Oe7YWtYdaf6qJodUdTBlkGEHrAWGQ_rA2DkKyFRj-pGN_UJvSIT9Cgx-BEGM4mmmM1kMGKr_1tTDsrAem3_JRmymRXskWlM942mHISOZSMf3kwAyZLV5MAahwnBJspPpasP2__0k-Yk7R5xASdLFEkX4BNCRttPXHOIU_BlhixFHh8aJJqaC8Rvmv_mcWpE4OfiHx6MpMZ5Hni4fWu4CE6b41R6XKJylE8C0tkmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfOlIkXbLOdtA7naxxYtzCNEwA9gItVc8FE6N51eracwLjI1sYxdcMCRiBcVY4HXCo2QQ2z6rBSQJW_3Agrv_hb3VaQBeLEoakGkpTp7XK92lh_6_gnTsPyYBZ0bwGqyi_NxkaCVjrVcqD4S6frh3l4XobVTFrWsBQBBUe1F2EUFY3r1_9n6z9PG-hZPkXXyy9SSJHQ0_ukcLoMmlFe4pMqjpH7nQoaFcLo1H61axXFgej00gwmG1kMv0gEWTIenf4KgPUFjrkApHJVz0-FEo0dxhF2Twe4kROt0T48qusKAoSWIQq8TgwVrz8vFtqS5fuLd3hPvpFcX0e5vxSJ2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ojp4v_Sc2M_tsAdUQZltrE9Jgcy8yqN9zW6vSt7Z0Z2WZsggH8OiQuCyxCFbRh31VlMl5ogGaFujrIuU1LLHZU6etoT4Yl8Sv_T2c6O61Nl-PHRi2aF3UMkBrScjs884eQhWgimktjOgGaeLIuiWTzN_VdSBBvOa14Dx9u6ylR-Ur_oK-PluHkNWUJcP4miw2aWW7IKlN1EpMgUiRz_-8llZ0BZbmskbg5TEuNA2aavM-2WlQwAYbgptwrTePlL-iuLkFLziXTJ4Mm0m-FDsTy4FR1PLV9PWrr5suDaQJqENuu8DR9mG25yk6vjTIgsSadweCya2pLxJAEsOGzMzRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ojp4v_Sc2M_tsAdUQZltrE9Jgcy8yqN9zW6vSt7Z0Z2WZsggH8OiQuCyxCFbRh31VlMl5ogGaFujrIuU1LLHZU6etoT4Yl8Sv_T2c6O61Nl-PHRi2aF3UMkBrScjs884eQhWgimktjOgGaeLIuiWTzN_VdSBBvOa14Dx9u6ylR-Ur_oK-PluHkNWUJcP4miw2aWW7IKlN1EpMgUiRz_-8llZ0BZbmskbg5TEuNA2aavM-2WlQwAYbgptwrTePlL-iuLkFLziXTJ4Mm0m-FDsTy4FR1PLV9PWrr5suDaQJqENuu8DR9mG25yk6vjTIgsSadweCya2pLxJAEsOGzMzRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=jVro4iutE5I-9uXAB6hDsMVsnRWnurlJpINxxfgzD6wChrtMKeL4gjsW7-Let_1u7v8JoEJ__plx-SDZhb_YciXr-oSUK-uCR2sNArBQQXu1k_ebeIK9xQoHZdBxe62U-Xr8Qv6FUvb_cQg-cIxJqJBL-fb0cOxFmUYmImwmMd3bv4JIhStN6TmgRjnAM6R6qJD9Zj8_e0y7r8S0AiGSWVBBk7QRuZf-XT3jeWt9kiqVhLqrH_Z414VVrqewkWL5VjXvYEgTaSi_juC5elgh0xzTLgQ4yco0fpnBktWvS4BJDyG6q1Ci_kBnmC91UlqzEoFdR05g2cDHQuEOL4STag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=jVro4iutE5I-9uXAB6hDsMVsnRWnurlJpINxxfgzD6wChrtMKeL4gjsW7-Let_1u7v8JoEJ__plx-SDZhb_YciXr-oSUK-uCR2sNArBQQXu1k_ebeIK9xQoHZdBxe62U-Xr8Qv6FUvb_cQg-cIxJqJBL-fb0cOxFmUYmImwmMd3bv4JIhStN6TmgRjnAM6R6qJD9Zj8_e0y7r8S0AiGSWVBBk7QRuZf-XT3jeWt9kiqVhLqrH_Z414VVrqewkWL5VjXvYEgTaSi_juC5elgh0xzTLgQ4yco0fpnBktWvS4BJDyG6q1Ci_kBnmC91UlqzEoFdR05g2cDHQuEOL4STag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR-m2UiIc2x3hKmUsmvNO-i7YxpmQh-QSIYVbAkHcVX6K7vdeg-jKPf8-MsxOozp53jSNq6nn3hJHNUAhQa7W2hQ-Y41QE3WQNTpHwj6DuMLaZCJQ5-g24tZgAqsbs3pr4wQ7iwB-UuLbZzsppjvZRBT-NnK0altXgGQtruF3qQUMrhimgoK-66Eqq2RgfxC7S0iFSZm9wBa6nZ4xyyjEPiVAvrzb0GYS5vFRhKAx3dzp4iUDS9ZeV1CLcMJRrOx4WJXg30VTZZ2oesOhtSKDx4G-wq9R1jkKLBFdnjpJbVQJAUNNJsf65wCrDSZKpuurxiSFqnkljxJCRWdDFEeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J65U-QTHxECAPDlb5rWn_4SCE56cMTCwDMK4Xaklw1WaAnECFKizsZPfkcxwhYxt_3btDUMztlld4KP3TE94fvQvLooh1TJ-4NEvY2ck6iFRm1k5Wuhgj56M4EXibsaVlwfb7R0iuqtSYkWB4xVpXvRviMaVCfH9jsLvY1hwuALTANOni1ub2EAKUZHLFmMFrTtFL0vSaD4kh4HrGIpbOKf8Gcid6LUxBLuWfQ5Tc8Nw02udiK30pdoIjoN91g4ODE_5SA4o4SWrNQjTc3DzMEo3Oa0T1IVlqnc72aLunbd32pbSTer01g9Kngxi8MWrGBGWAzFIhuNHuxgrdfSBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTE8lZWE3qGGsXXJ3tOGgIr83SpDhtYaPKLeC0oKUFcSAoBhuPWdrF7ZZcFjhf_A8a0O65A1P8GHvvWHLDtp4GOyjruMG4q3Tn9ojrL_2thw9qvGjd3xsguhbzgV8FOl-PaZkOX1oZYQ7pdQ5W0a57A1CZuSJMDeeewV4SR53DGLE9FaX2tKFXpswV2mgHFncopRF4JqN8Vitl6KUJ_Gh3OoEKuLS5xzzzGfYrsYvU9Ybt7G8WCWXYYIzmz8HA4yvmac_a2t3zNVpYPosUhku3MDd5eCVRGSC5ofGRzeVcfg0at0nnB2fusrUOHAnYcVzsqj8fNd-DSckDp5Nkiv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8Irjye7Ol1oy1q_mo86kufr6IdeYyiBJEH5P4UTb7k4YIFlNcUSohaRABZfnOL-tTQjGbzSp35thdE_fn1hA_UwbY1Y3adNkEjmdYA5iimVlRDLP9PTekr_7Z9goQ3QP856z-hXRdwSXLFx0pBprJ0WPx47EIuIbWCXN4B-z8rIcsZ_KSOMLXJoIv3uiYr1QlHWo3BmNlqET9nkVQ0mkZyL13ifUMCRKDKIeRiGO6icZeTmA-140mdGrVhKViPInNhS88MwHBbBkFaRAPhNRW-wtki5A_oUEe7zg3pDjIuqvZw0xl9McU9NByXovsZ88cUho3erO5LvQasr5AG15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1MI835IXomNyh03RI0IEEau4xM-wCG_X0MRF6gzf1dm4ed_e5kjnsd0kDuVlsRKQKGsEYqdaudhkbBJrIqpliQb6AqbkzIuce_9gpf6KfganZVbwQHGmj466aFFiV284MCaP1q8R1RBVZ4ZLUgNFk2aW_eJ_5xDUtNCrsonrEqo4IMA16b3vQgWxU1HRNaUwrM2bL3AdxjOqNyuWRClXjCfCFTnTbqvTshR7sJl0j630adtWfpRw9j2UIgofBH9Z0ID7GFJInKWTuGr9pQ4v-IVw8bqjjP7wi7FbykyZjjZ2o-rFA-34bIwmFBvfA-8ubUZwaUbNogzKj18qqEuYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unn35sbocioszG8wyJLlA2Bh-v5Sj8mCcbTm4we996CMGwDSw0fygoPE5jSp-rzWKPYpSrk0FtCQ7pfSbykUVe6mGFAgo2dnF2tzBYc2xj7nLo5SI_OZAxN7bTqfR_4ISuVaOglLr2ESJOg44JLj8c55UpJBbB7EwZA74Uf08aOwtLuC_HtvC1ErqZQ2i2-z2dR6H1NjjCHYT5e23RxqJmaTZolE4jvz6H2MHTrUw8n8kQuS8apo6JEf6aZLI9F0_XgkjVRnvRSKta8vOdEsQgqxZDfEXQkGTHc1GxgSi1vFwa6Et5lp2nnJTMf3OgckK4hnSkRvlDjy0eEX60W7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSYQ3bxsDxY6gHfxT-Lc2ENLPzbGQ8x8TuIAXDy6-11Q2evKkGgwsb6MekJmOcJblacFXp4FE37ZpSoxYse4zjnV7zkp7XMgAup5AgWE0iTQZ890nf1PGzPafMGRlDZFo3LRXJ8BKXu8mmj0d6r5s3iq5EtCjhO63g1mthhdUejSq4NupAvqFX1hnbWGqYsvmcO0nJ0_0GslXda2e8Z2kjCN0_QrHZmkHyLIb83m7evDyVZKBeAWMF0e-Jgf2NOkb_3tKMLGPWECMxFpBar_ZfQttQn-JxrSMZetaVZHO42oWP3ip95r2hsgMnPlmUCNFyWFjMV0FexV-bMaCXs6dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4IQ6xDlEPhfpHuxBIXPfEv-z-_tbRul_2vk8Sl6whUFrJVwE5O56l-1cyKUXHiy_a_IzvuZjlhfNdRoNry89Kfs_ytk84MieZljV4JaZjVOXHvhz6aBGtCHr14gtjr8hRtAFY6JZ0kaPu_jwsj2p4wGS9PoHou4Bpx5w8QxmCT-w7xKNzTaQcdtcmYUh7b9MLmR_5txSQy0AkZFb3jvhMO0CVI7OmTo4nPAVwka5rKLOh0zZBySeQQ0ugjv-LZxR5xie9iG8IKqMLeMfN0-WpfweoO-mWKJw1NplaCtMJJ4PsZ1arhT6pcdu2AaXHq22mAXemomnx8pQZl_wtaTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjmDV3djg2fsj07rldeLsw7HTQTsARSeLQN-d9PDnOwUeRjopJuXBeo28HCrzGmdzqNfznAE1O_3OqTi9TnAd_zYnu1JD3YZ-5ffwe3Rv8oON8Amny37-PuwQo5a_EFvG8LdpXH2EHhkaR0fK01iCxIjYIYR9-xhNzSzzfpMAanmayv4859pLCzbzQRUN2q3sKKZh2uGYEDdkq43jI5_puyw3wlLmVDVYGxiKO0bu4SL0fMYTYA_nd29p7wJ7XzuBu2Uk1yNp1LsJChpqRVk2UtMmVJ1LcJAf9F5q7Nvqp_-KYD4dFLSgzPc2kwHpt0jE76ET5zZ6SiHJjFCFwrbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXnEeItzFcbkWeULLTz11ptaJwAMyfsMQayMb5zkRJnR2g17Dy8G8TuhPrJAL-FSwCsKtkZWm9choV7iJTxpIXrgD9-_NCBnYxF6un2ZKGHMl7jViNS6cUea-aY0jaI27wxy8HkveCyecHjTWG248DwUO5-NodIS9FbDHMV-l1L1Q6gB9XSrgJIN-bvO-vQk4FeYaa11alvG3LTIokxdokf2aqM6edPTJ0hraDVgAk4EeD8-eJYLgNiRM-zY6wRSyfpqxVbut4mT6sCQMqYuKvu7eEVd5TSUWCoGGngs5xbtg-mBykRaNNonPYnpVVrNlNsiyNDPQdWg2ljUTcK10Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
