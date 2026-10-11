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
<img src="https://cdn4.telesco.pe/file/QPDqdNK6_B69JK0GFe_xMSOaPkXXAY7bO3yekoNQsveZ8qva10AXwF6bBGa6SoxzX-ucHu6nFI83hnwYHea8PbR58iPyWQBFGF6RJ9NyxegVHZGLOwLWriwGR3NT18DNOgbd3V_T8_yGDIcE1AyJn3e_romHYbetIKa107iL5gwYEpz5yCD2q6TxXXaPu9QNKdCp0AxEsgx8lKdLuzfwEAmXsR2n-wtOyGXiKQy1KmVeMN9p7Kmv4GOvYMgh3MHwr_3TQmumq0DwRAC4aQcUfobuCy6RoAPM9VQUcDt9eHmpUPaunnAv-l1BC2EgHxLfMT1zNwbqsuTfpCQpJX0wqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
<hr>

<div class="tg-post" id="msg-467810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1Fxhy96X7VYsXN1b1YvV501p9ae64nML0aJoikLKrR9uPsMnbAeG6QcqRIWJIDNfMnVtsdLhegKSk-e7xXMUAxb_kikBuZurUj1oVU5zrQjh71mSKSQjY4mF7YN_ROFm1jtVSBQvTgl7OiGZyGpYZ3piGbeUY1zW5Ui-aNDvi8E500iEbIM3MtkXL6XEgV9u6VMAhB9kImDGId0AE9-Ez14Ogy2NyMU6xA8dBsNJwdFs8G06eH8x5kxWK1lQR_6ip3UHT_ecmz-5LPXbj6kx4bEdZUa7k0SQqOUo5LXbUS5zRqcrYeMWk1xNar-t3fzEpbdy7tL580p0cub-mXkqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: وعدۀ ۲ هفته‌ای بسنت تمام شد؛ اقتصاد ایران فرو نپاشید
🔹
رئیس بانک مرکزی: امروز آخرین روز مهلت دوهفته‌ای بود که وزیر خزانه‌داری آمریکا برای فروپاشی اقتصاد ایران وعده داده بود؛ اما به‌جای پاسخ‌گویی درباره نتیجه این وعده، دوباره از چاپ پول در ایران سخن گفته است.
🔹
واقعیت‌های اقتصادی را باید با شاخص‌های قابل‌اندازه‌گیری سنجید، نه مواضع سیاسی.
🔹
رشد نقدینگی در شهریور به کمترین میزان خود، یعنی ۱.۳ درصد، رسید و با مداخله بانک مرکزی در بازار ارز، روند افزایشی نرخ ارز متوقف شد و حتی کاهش یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/farsna/467810" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467809">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDCdJE3Vrg_jMVASi-e9GYHVuuHAFOE-19MdfwMUbMPFnzHoOi9io0ylGo6rQERUBR9kNlpuMizqyOAXA_mJfZseqI-MqBZR8yCwL9R7jzduqUUo61X8XmQrCBAM1daF2Tb-_yUHP5cw-x0eyVCwskllJryYFD_hF-NQI_qWq3gpNhqRQcB0aN7TqtW8AQo97FaNom6Q8RnQTanrFAOutPr0RAsHvQj7BveiZAzuNWh3gGdn56Ly_8JC3BorOdsYvbP8akqwir4YqiagO36_ozlvaL8wEXJGrjNXxDNEOjzYWfKdfwLRRiA_isJTGJ-lI3u_rDkYAxQVqUroEqyWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی در جریان آتش‌بس انرژی ترامپ نیست!
🔹
الجزیره: «زلنسکی در گفت‌و‌گویی جدید گفته: خبر آتش‌بس انرژی برای من تازگی داشت؛ اگر ترامپ دراین‌باره با پوتین مذاکره کرده، لطفاً به ما بگویید که این آتش‌بس چه زمانی آغاز می‌شود.» @Farsna</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/467809" target="_blank">📅 21:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4e4aef18.mp4?token=jPLY_uc5z6GEPpke-drF58J2lHDLA67qpv1xQSbDrttEUSOX2BGgWshn5sobQjE3jzeRuoKhrFjXnQ2w9hXOV0mj4JFFOxQlbWD_bARoP0hyqMk2STf_7Jy8tMLm1NaiHFMOf3Q1SMtllxATdGCSQHDYgppOuwqKtcVmczpBkhj3UBuYycqfoUcSglL1-3PcfV15Gcq4fQRqHfWE5KwMC7bZr3X3NLhVGyhPQtbG1pqaHtztyzL5tvQumOnwJ5khIuYFkIC5AddlQJId7epHPmM3CPa4ZWm_uM2I6zetvOjgA3JPPY7xSmFrhXWX6-7iL8wvypI11D3_lZo70sL3NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4e4aef18.mp4?token=jPLY_uc5z6GEPpke-drF58J2lHDLA67qpv1xQSbDrttEUSOX2BGgWshn5sobQjE3jzeRuoKhrFjXnQ2w9hXOV0mj4JFFOxQlbWD_bARoP0hyqMk2STf_7Jy8tMLm1NaiHFMOf3Q1SMtllxATdGCSQHDYgppOuwqKtcVmczpBkhj3UBuYycqfoUcSglL1-3PcfV15Gcq4fQRqHfWE5KwMC7bZr3X3NLhVGyhPQtbG1pqaHtztyzL5tvQumOnwJ5khIuYFkIC5AddlQJId7epHPmM3CPa4ZWm_uM2I6zetvOjgA3JPPY7xSmFrhXWX6-7iL8wvypI11D3_lZo70sL3NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تبادل یک جاسوس در دولت روحانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/467807" target="_blank">📅 21:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467806">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d40bda8e91.mp4?token=L4nt3g4fEGOHGzjTkTvd9MihqjTxLAlVmEbwEdO6zK1JrzUqRXaa-ibi5L6wE7zSDpc3k32xv_esbHOahQ_rvYN5GahMSSeAo7kUDL46iwA4jGf5kdWN3pSkfSeYh2Q6XnRRx4HcuffFNZSrZzXXkCTw6kMOvDLahYncGLT9vyamChmtsPQqYL2OtJYE8dvYNgQ0s0rP-ww_0Ug5eS-QQvH93FwoDt5fIkH2U94cniXx8y1orYDF1fPxpG0ossCS5BAa8PY5LUPkVYnGMR6hzKAV5_57EtNyVPy5o8cnZmhYpYe0yw84Wj_GhKWBIdw-OX1l3XOvyN72RODyxJ__eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d40bda8e91.mp4?token=L4nt3g4fEGOHGzjTkTvd9MihqjTxLAlVmEbwEdO6zK1JrzUqRXaa-ibi5L6wE7zSDpc3k32xv_esbHOahQ_rvYN5GahMSSeAo7kUDL46iwA4jGf5kdWN3pSkfSeYh2Q6XnRRx4HcuffFNZSrZzXXkCTw6kMOvDLahYncGLT9vyamChmtsPQqYL2OtJYE8dvYNgQ0s0rP-ww_0Ug5eS-QQvH93FwoDt5fIkH2U94cniXx8y1orYDF1fPxpG0ossCS5BAa8PY5LUPkVYnGMR6hzKAV5_57EtNyVPy5o8cnZmhYpYe0yw84Wj_GhKWBIdw-OX1l3XOvyN72RODyxJ__eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: ایران باید هرکاری از دستش برمی‌آید را انجام دهد تا به آمریکا و جهان فشار اقتصادی زیادی وارد کند
🔹
درگیری بین انصارالله و سعودی‌ها هم فشار اقتصادی زیادی به آمریکا وارد می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/467806" target="_blank">📅 21:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467805">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زلنسکی در جریان آتش‌بس انرژی ترامپ نیست!
🔹
الجزیره: «زلنسکی در گفت‌و‌گویی جدید گفته: خبر آتش‌بس انرژی برای من تازگی داشت؛ اگر ترامپ دراین‌باره با پوتین مذاکره کرده، لطفاً به ما بگویید که این آتش‌بس چه زمانی آغاز می‌شود.» @Farsna</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/467805" target="_blank">📅 21:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467804">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7fdbd4bef.mp4?token=vt9W53zFtDMZm3KVRZ48ZmOFzEHCgMPc7FpuFtEM_rMbdvDN7imP-ewuGh2dnTvtUmINwMoDfQkTtmRp_CfCc4SMQAbWpsP1P_xmm8A2mJX-cUrKR5zGVoQ78r2xw8rnvuhWgV9cFLxwg5RSNixeBsQzP3d1dagoUPFp_6dR2yz0nzHpAP2GA_rmwJs-xq1c_eCbmLSBRJdRg1MIZOdbPuj-6DoCVIsshw99K1oWpMK0_O_Zc-fw4ok1AMcmnPnS10qyuMcOcPKSzHh0obRvyQ12A7RnCvbA7yZRwjg6wr56m86xcKG8laaHUDjH8w34tnrJOv6iRB-ZvUyXt49HqQCsdlfNDrwjARWB8a_UhbSTouf1okQVKOjAcnilZVoua_rWSnXVZr2sI1BjBWFS_KpJKeHPFkVficSsJSw0mYvp0KaEgS5HVkJNyb2WVMhOKvunJswaoKJEthSUUop59XtuBYzU_WegEibLYa20nvLHA4xRTVhNcfaXbLPYOP3VC6PtFWtITthZro0VogeI5xnNzK_Ackzr0UA1lHjUBeflo5Eji1PVuA5UxL6RRFzXr0teeUdxi0GST44hJ7YaBwwDkbHaYUF88UFPmgNV86AgaWbnbMQdGYlabltKJuAoF2CqN-dtqse3m9mshPakrGDDwa8W_JzkTNT7fFNdrHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7fdbd4bef.mp4?token=vt9W53zFtDMZm3KVRZ48ZmOFzEHCgMPc7FpuFtEM_rMbdvDN7imP-ewuGh2dnTvtUmINwMoDfQkTtmRp_CfCc4SMQAbWpsP1P_xmm8A2mJX-cUrKR5zGVoQ78r2xw8rnvuhWgV9cFLxwg5RSNixeBsQzP3d1dagoUPFp_6dR2yz0nzHpAP2GA_rmwJs-xq1c_eCbmLSBRJdRg1MIZOdbPuj-6DoCVIsshw99K1oWpMK0_O_Zc-fw4ok1AMcmnPnS10qyuMcOcPKSzHh0obRvyQ12A7RnCvbA7yZRwjg6wr56m86xcKG8laaHUDjH8w34tnrJOv6iRB-ZvUyXt49HqQCsdlfNDrwjARWB8a_UhbSTouf1okQVKOjAcnilZVoua_rWSnXVZr2sI1BjBWFS_KpJKeHPFkVficSsJSw0mYvp0KaEgS5HVkJNyb2WVMhOKvunJswaoKJEthSUUop59XtuBYzU_WegEibLYa20nvLHA4xRTVhNcfaXbLPYOP3VC6PtFWtITthZro0VogeI5xnNzK_Ackzr0UA1lHjUBeflo5Eji1PVuA5UxL6RRFzXr0teeUdxi0GST44hJ7YaBwwDkbHaYUF88UFPmgNV86AgaWbnbMQdGYlabltKJuAoF2CqN-dtqse3m9mshPakrGDDwa8W_JzkTNT7fFNdrHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۵ خبری که حسابی در فضای مجازی سروصدا کردند؛ ماجرا چه بود؟
@Farsna</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farsna/467804" target="_blank">📅 21:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467803">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0414b153.mp4?token=t3xQheEUkHZDak0brZAGKroGTaw_187eJ3sK24oIcGnmnxlUWNhiNGinLLO2fpmyiucWDfZPPgR2KJERIXC7vge_Mh8mMzWOUMaj-3Es40AQbqt2PaokhHMZ9oBjK2f9A0oOq2Oi8DJ9SswS4pOQXSDKOXY9_QAqzEUn1104BCflD6qx0Cl81Bm-kdne2rVGeEKTINkJJVDiQS_RfdbnhT0igHxbnVWQSRDKb6X8xZcxX2BBv4cPFmjfs-iHYhS1mYSXnnIfxBuLhUmnoswioZOFYNP2dDKgT-qEYnjLvLAQSvzjUeVmxY82AxmTN0rhyMf5GXpXMGRs5opPPsePlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0414b153.mp4?token=t3xQheEUkHZDak0brZAGKroGTaw_187eJ3sK24oIcGnmnxlUWNhiNGinLLO2fpmyiucWDfZPPgR2KJERIXC7vge_Mh8mMzWOUMaj-3Es40AQbqt2PaokhHMZ9oBjK2f9A0oOq2Oi8DJ9SswS4pOQXSDKOXY9_QAqzEUn1104BCflD6qx0Cl81Bm-kdne2rVGeEKTINkJJVDiQS_RfdbnhT0igHxbnVWQSRDKb6X8xZcxX2BBv4cPFmjfs-iHYhS1mYSXnnIfxBuLhUmnoswioZOFYNP2dDKgT-qEYnjLvLAQSvzjUeVmxY82AxmTN0rhyMf5GXpXMGRs5opPPsePlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: آمریکا باید به این باور برسد که توافق‌نکردن با ایران پیامدهای اقتصادی سنگینی برایش خواهد داشت
🔹
آمریکا باید مجبور شود به اسرائیل فشار بیاورد تا به تعهداتش در تفاهم‌نامۀ احتمالی عمل کند. @Farsna</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/467803" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
نیروی دریایی سپاه: دومین سوپر نفتکش با مین دریایی در تنگۀ هرمز برخورد کرد
🔹
روابط‌عمومی نیروی دریایی سپاه: یک فروند سوپر نفتکش متخلف با برخورد به  یک مین دریایی عصر امروز در محدودۀ جنوب تنگه هرمز دچار انفجار و آتش سوزی  در موتورخانه گردید.
🔹
این کشتی با…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/467800" target="_blank">📅 20:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399ef09449.mp4?token=uq0JSaHZygHj-_8peaV_uxPaXPK53bp9iHTaFtCJBOMkLyX2STmdEpMt2MVrvvLgduMq5ejEdEqOY5sskt3GNzPdAe3auoX89IxmpETHzarl4-VMeY9rpLKHZfN6MVKijd96VCijn1CbB8-4HluNdTt4TnIpdERpoGRDrxyIDjrTSYsuYfgrzB8PowRoi6KG2_jiBQ1SPzTeskWgrXzwD0CLxj-lcQUF3lvlDCBEey3MWdQxDqMZeBnra17wxueLlXgxBcu0e80hlcwQAT3A_jSwkqIDRwqsRs1tGUs9ehpHiQz5_AGTYuOpBCtiu3lsT5cMyZGmaDGBNC-TvfBPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399ef09449.mp4?token=uq0JSaHZygHj-_8peaV_uxPaXPK53bp9iHTaFtCJBOMkLyX2STmdEpMt2MVrvvLgduMq5ejEdEqOY5sskt3GNzPdAe3auoX89IxmpETHzarl4-VMeY9rpLKHZfN6MVKijd96VCijn1CbB8-4HluNdTt4TnIpdERpoGRDrxyIDjrTSYsuYfgrzB8PowRoi6KG2_jiBQ1SPzTeskWgrXzwD0CLxj-lcQUF3lvlDCBEey3MWdQxDqMZeBnra17wxueLlXgxBcu0e80hlcwQAT3A_jSwkqIDRwqsRs1tGUs9ehpHiQz5_AGTYuOpBCtiu3lsT5cMyZGmaDGBNC-TvfBPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه: سوپرنفتکش متخلف در یک آتش عظیم درحال سوختن است
🔹
یک سوپرنفتکش حامل نفت خام که قصد داشت از مسیر غیرمجاز از تنگه هرمز خارج شود، پس از ورود به مسیر پرخطر اعلام‌شده و برخورد با «مین دریایی»، دچار انفجار شدید شده است.
🔹
این نفتکش با خاموش‌کردن…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/467799" target="_blank">📅 20:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3ea8efe6.mp4?token=DA6KSkOpq42mxRqjvdGiHm_B9CBoIMSUpdEI_oNsPNh2gsUafSHRuKV3XFcvbdFEQLZvVjh6SJTGdMWv-0lV_phtHqtQz_IX6cqVfpOoYJLilJbiOp-Dy7VeChYMHT2G0hxovEdGjSMTbtpmHYVyUmC3fg8wRWVISIgUf8QTQEdbE8Rd_1bqzU2qtIbIcHd96ueqzET4qV1uXAtbLeGztXW9YrT34MHAxm0jzQuswrErQEB4TfPnu13xPAnLU_pLxkhnpLQZmsAVT6qnRiNXMdgaY500Oj1WP21pfjuEBo01E3hYWSUvpiDd6yEncy9RBsYE6w9FtHUUYUqGwN1dGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3ea8efe6.mp4?token=DA6KSkOpq42mxRqjvdGiHm_B9CBoIMSUpdEI_oNsPNh2gsUafSHRuKV3XFcvbdFEQLZvVjh6SJTGdMWv-0lV_phtHqtQz_IX6cqVfpOoYJLilJbiOp-Dy7VeChYMHT2G0hxovEdGjSMTbtpmHYVyUmC3fg8wRWVISIgUf8QTQEdbE8Rd_1bqzU2qtIbIcHd96ueqzET4qV1uXAtbLeGztXW9YrT34MHAxm0jzQuswrErQEB4TfPnu13xPAnLU_pLxkhnpLQZmsAVT6qnRiNXMdgaY500Oj1WP21pfjuEBo01E3hYWSUvpiDd6yEncy9RBsYE6w9FtHUUYUqGwN1dGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در میدان به یاوه‌گویی‌های مقامات آمریکایی‌ پاسخ دادند
@Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/467798" target="_blank">📅 20:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467797">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd9c4b0eb.mp4?token=gSCUJX92Lm4sIUcKTvjCDj59_Pj3rZwdjSKf4L0Q8Py6ygTg7r9g1hYuxxjHOFxPksMvu78NzgH8zOuyoFHbPBOZNdgQhcuG69CO1b_VMvJYprAjPrJKwHKC7e_f9mB2Zsn503dIRhZB4AYRhmPd2R7FSeKT1UsiD2_p1BpxS1aCF0wrPFom2A2zGG26TJyhPRFrbxvkxULRoqED9me6pdY5zcnGP7DIQ6uUHBYISgtUPGduZbBY_TG8Ej3ncadojvNllP34fZmTW10HDYDL-sFyDYx8ACbJ9-8RoAepXOeY6Qaw-luF6Hb2S1pEKMSglmKS8NxQ6pkYw3FYV4INiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd9c4b0eb.mp4?token=gSCUJX92Lm4sIUcKTvjCDj59_Pj3rZwdjSKf4L0Q8Py6ygTg7r9g1hYuxxjHOFxPksMvu78NzgH8zOuyoFHbPBOZNdgQhcuG69CO1b_VMvJYprAjPrJKwHKC7e_f9mB2Zsn503dIRhZB4AYRhmPd2R7FSeKT1UsiD2_p1BpxS1aCF0wrPFom2A2zGG26TJyhPRFrbxvkxULRoqED9me6pdY5zcnGP7DIQ6uUHBYISgtUPGduZbBY_TG8Ej3ncadojvNllP34fZmTW10HDYDL-sFyDYx8ACbJ9-8RoAepXOeY6Qaw-luF6Hb2S1pEKMSglmKS8NxQ6pkYw3FYV4INiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: فعال‌کردن مسیر عمانی در تنگۀ هرمز اولین مسئله‌ای بود که نشان داد تفاهم‌نامه دارد از هم می‌پاشد.  @Farsna</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/467797" target="_blank">📅 20:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467796">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebfe86521.mp4?token=O60X0twTC5yCGtewybgnJA5qOznwGkU1U6apfSCv90FlPwJuIKSfYzd3Ofo_si05O59MbpfK0mWfXcFqTq8GQPJPnDgWA0_Hjnb_zmPyvFCLMdwUfcWguFtxqSHhIQ5ODtJGUHACzeJwJ-y_uFiZ2mdSxwbt1eGYm3DXEAp11X69WXHb1bGKaH88x9XkwoLvTYerhfVQFsYfjsZ_1MDiYKpfTzKWlZ2bI-VINW5ax7QZz6Hvl4TgqpBKkZJiEd4F2FKN44d7zFR2sko2KTwMGQK9pFtl0YcHb4qTwW8prbvpBrl3WdzM06fE36jmH_44-lNAjtje-05zGKf-R_TcKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebfe86521.mp4?token=O60X0twTC5yCGtewybgnJA5qOznwGkU1U6apfSCv90FlPwJuIKSfYzd3Ofo_si05O59MbpfK0mWfXcFqTq8GQPJPnDgWA0_Hjnb_zmPyvFCLMdwUfcWguFtxqSHhIQ5ODtJGUHACzeJwJ-y_uFiZ2mdSxwbt1eGYm3DXEAp11X69WXHb1bGKaH88x9XkwoLvTYerhfVQFsYfjsZ_1MDiYKpfTzKWlZ2bI-VINW5ax7QZz6Hvl4TgqpBKkZJiEd4F2FKN44d7zFR2sko2KTwMGQK9pFtl0YcHb4qTwW8prbvpBrl3WdzM06fE36jmH_44-lNAjtje-05zGKf-R_TcKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: اگر ایرانی‌ها مصمم باشند که به‌نظرم هستند، باید راهی پیداکنند که آمریکا برای توافق احتمالی وادار شود اسرائیل را مجبور به خروج از جنوب لبنان کند.  @Farsna</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/467796" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467795">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a086e117.mp4?token=MjuP1Xi9Q3I8FEKS_e3ES0Z7qYHNnXujPKJS6Rw3HCyFyo7fTAEiXqOr6H5SwWv_dJkrIrIJy3_hL0b-N4zodlwmlqIovlRf8iQ1Tq9b3YC2AMLh_4iBsskXSYP3d-LITjV4I35Eav8irfJ5HGzwws0a60rx0iHZC8smq0NfIWkqxZmxMRWkFMLA0k0fyC_i-tZzKFy5POyhtM5fC-hx8SwQVKnhF9ZKfZpF1krQN2ao1pAUi7bQQl3u18-QmJfRrw5NctfMkNbctKL0M9_4QIT4XUvCdSn2tHDCcsBOkMPQ_dV8n7LD368LRca8q9h4_W9fTBqk3yDoeNlLaKc8iTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a086e117.mp4?token=MjuP1Xi9Q3I8FEKS_e3ES0Z7qYHNnXujPKJS6Rw3HCyFyo7fTAEiXqOr6H5SwWv_dJkrIrIJy3_hL0b-N4zodlwmlqIovlRf8iQ1Tq9b3YC2AMLh_4iBsskXSYP3d-LITjV4I35Eav8irfJ5HGzwws0a60rx0iHZC8smq0NfIWkqxZmxMRWkFMLA0k0fyC_i-tZzKFy5POyhtM5fC-hx8SwQVKnhF9ZKfZpF1krQN2ao1pAUi7bQQl3u18-QmJfRrw5NctfMkNbctKL0M9_4QIT4XUvCdSn2tHDCcsBOkMPQ_dV8n7LD368LRca8q9h4_W9fTBqk3yDoeNlLaKc8iTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: بعید می‌دانم اسرائیل بتواند به‌تنهایی به ایران حمله کند و پیروز شود؛ چون ضربات سنگینی از ایران خواهد خورد
🔹
اسرائیل با کمک آمریکا هم نتوانست در جنگ با ایران پیروز شود، چطور به‌تنهایی می‌تواند چنین کاری کند؟ @Farsna</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/467795" target="_blank">📅 20:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467794">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0662c3fbe.mp4?token=lDEL7NsIoat1JBOBvD441nXf2toJV1r6iKT-6vnq0iXiMPiAg_4PyJX4ExixXpFTG0Agg4xGV2BI0kQzDN770F7Ei_NEa4h8TrZBbCovYIlfFhm9UVihVavcGSHIrURR2vYp8VQMfXRAp4bXGe9yRxdRBkDvuZi1eOWMrOwq7oDor7tIicL8V95makoiSIpdbiW6OeVohQl6KWurJpP2EBE6bWjhkZAhRbvthWTxJdyRXhOrlIziEZ_aWR1uZIT6HFLSl2kbdPXyw1OWgGFaJaZbu9lN_E6cdrmDJ2_acNLxiwp8yEO9poKFE44eWdebcwdVCd_ca3-xVoEjv59f_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0662c3fbe.mp4?token=lDEL7NsIoat1JBOBvD441nXf2toJV1r6iKT-6vnq0iXiMPiAg_4PyJX4ExixXpFTG0Agg4xGV2BI0kQzDN770F7Ei_NEa4h8TrZBbCovYIlfFhm9UVihVavcGSHIrURR2vYp8VQMfXRAp4bXGe9yRxdRBkDvuZi1eOWMrOwq7oDor7tIicL8V95makoiSIpdbiW6OeVohQl6KWurJpP2EBE6bWjhkZAhRbvthWTxJdyRXhOrlIziEZ_aWR1uZIT6HFLSl2kbdPXyw1OWgGFaJaZbu9lN_E6cdrmDJ2_acNLxiwp8yEO9poKFE44eWdebcwdVCd_ca3-xVoEjv59f_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر، نظریه‌پرداز نورئالیسم تهاجمی: پیامدهای اقتصادی ادامۀ جنگ با ایران فاجعه‌بار خواهد شد
🔹
وضعیت اقتصاد جهانی و اقتصاد آمریکا وارد محدودۀ خطر شده است. باید دید آیا آمریکا آن‌قدر تحت فشار قرار می‌گیرد تا مجبور به توافقی به‌نفع ایران شود یا نه. @Farsna</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/467794" target="_blank">📅 20:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhOb41KT-Gx7k1in-EyPH7714ujNFUe1eSm5goL3nyK3pNHSGzQtJhsq5sivCZ5ZhiGDaXN0NCCYtoammkVGn7vK1sgc2XaKkfwFI1TkBLO7xgIsUIUQwPLCOpvzanK67JsQ-pWKW2A4u0lThXI66USpQpPkk8g7dEUTBe0PcX5qfSHY8Qb1jjPtw1UA9pW467N9QW9JvG8PV03nK4lsYfSocgRxUQo6UXLGiOjo4yWs-Ov3df-tFPqCf79ONrIq9MOE7g-jcjNNjXmYVB0vVN50TGwQ8lTMCOXPNv3x6xzF-cQ1zPeaARUj5rsRUTdo56k1561Mn5eX23ASbUj_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2vS9PymB8vCAuaRkMbN6kyFXzJvd1uOZjkexo5KT1Wwpjhnre8XxNCTjpGWKyxco25jYCkLbEFm7l0AUgSpCuTJMn-Vz2JvlnybxZkfGeqhxCjj0UYBMraFMD3Lmd1rnoeFYfr9oLpZ5agDUdAy7b9hFDgOc6Z5jHywcfUaroKxgoguS9me1jzY_tulqbj266OZkS_JBWqSszJshI2rB0LSIl8x58zULwn_OOzLSPYOeidjZK7JZrALi7_xG6Jcg3fVsopI_5Hk5EBePSeramMfeixFGOPqCrI1yBjxkXCkoU_4NyOtZNt-QTd7xGtMgGQC6xlTRoSAVlh0a4183w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bckcV9I6skuq2lVuPaWBnDUOnS1AIvXy_rxv9KOKw_5OqHocdH7HhgvIT0VnVfwaOpg4ZpCDX7y3DdfBcqIINrGsB4u9Gq-QMpEANpYhLfJRCl_7Jd4yYK4Scn4AQFeuU4LI39Qym9wxh_vhhjVGzqbHjiPK9LqGmWRybYyBqPplrQeErJLKZaD2a9DH0BTUJY3KOAhB_1gGYw54fTmXno1Y1GBXajpe-LRHWIgzofsyvFmzgt17-9DCiAhdHZA1l6TwjdJjCr_2vSqtuhICGfl0odNNb0yn2ZXbJ8mDva0EZzN9d1RNgYrMVCY5vAhnBe0fVn0Pb4y2u3unrEfvfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عراقچی: مسئولیت واقعی ما ثبت حقیقت و پاسخ‌گو کردن عاملان و آمران جنایت میناب است
🔹
وزیر خارجه که امروز نامه‌ای از فاطمه‌زهرا شیخ‌آبادی، دانش‌آموز بازماندۀ مدرسۀ میناب را دریافت کرده دراین‌باره نوشت: نام کودکان میناب و لامرد نباید تنها در خاطره‌ها زنده بماند؛ این نام‌ها باید در مسیر دادخواهی نیز ماندگار شوند.
🔹
وظیفه خود می‌دانم صدای فاطمه‌زهرا و روایت کودکان میناب را به مجامع بین‌المللی برسانم و اجازه ندهم گذر زمان، حقیقت این فاجعه و ضرورت پاسخ‌گویی در قبال آن را به حاشیه براند.
@Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/467791" target="_blank">📅 20:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSwv3-XA0X_I6TlxgTZ1zFJk1CnyG6-MDkksYYv9bu89Vu6Hsr4hr1plOwTJrT2X_v2cB9mY-TyNmcc44D0A4ZKGPNOw-4DTv_-ztDIni4erCX7em7cL8gaITxjAfyBD0nWzLaojwajjb2jONXV8Y9Bp0gitFOEOuFq5_s8gJQIxGr4QueTGFWr_d2kFPCCBJ6z4ivHnClFSXMEeKCRItIZtNnS6_HG1BSE6pI5yeLMJYFtdxCPD6r4sm_5di6KMLgZ-2M8_eR5nA9W0WB7r2m4iiA31yC_OyavH6xu6oiypViNXy660TYCPpYNZXOAQ3I0PCrBy025v9nNJhh50uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان: مسافران با اتوبوس از دبی به ریاض بیایند
🔹
کنسولگری عربستان در دبی: مسافرانی که به علت بسته‌شدن فرودگاه ملک خالد در دبی معطل مانده‌اند، با اتوبوس به ریاض سفر کنند.
@Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/467790" target="_blank">📅 20:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5a9100aa.mp4?token=o9cbu8Fd0vp3K5_KclqBJOkY2URjQNCRFroqAKxNzk3mW16OBTbeU35rZN0uD_Adz2saB5oIlRYGw0RLlM39gIgOraM0b40oqfycY3iRhnJDLhwrcQEFEl8INP3XNWTO149e2V-TsEIDWQfJIMj9hJCW7vfJek58Oofnl3N9y2nXZg5-ljGWMX4t2QawIEJkhy6c1vpsg7zgjekbN4sCV1UJlw0D2k4dezao6OHk81tVykgkbx55FFfqMrmXx9bCTZo5hCCsUh-uF4tQy9I7EGZL9VLyL7eTjSFFNSHC6frN00zUspKTDgHCKgKriMxeNgojb1Fs8AKnzBYgbVwneQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5a9100aa.mp4?token=o9cbu8Fd0vp3K5_KclqBJOkY2URjQNCRFroqAKxNzk3mW16OBTbeU35rZN0uD_Adz2saB5oIlRYGw0RLlM39gIgOraM0b40oqfycY3iRhnJDLhwrcQEFEl8INP3XNWTO149e2V-TsEIDWQfJIMj9hJCW7vfJek58Oofnl3N9y2nXZg5-ljGWMX4t2QawIEJkhy6c1vpsg7zgjekbN4sCV1UJlw0D2k4dezao6OHk81tVykgkbx55FFfqMrmXx9bCTZo5hCCsUh-uF4tQy9I7EGZL9VLyL7eTjSFFNSHC6frN00zUspKTDgHCKgKriMxeNgojb1Fs8AKnzBYgbVwneQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر، نظریه‌پرداز مطرح آمریکایی: ترامپ وقتی فهمید هیچ گزینۀ نظامی در برابر ایران ندارد، تفاهم‌نامه را امضا کرد
🔹
اگر ایران می‌خواهد آمریکا را به امضای توافقی به نفع‌ ایران وادار کند باید به آمریکا و اقتصاد جهانی فشار زیادی بیاورد. @Farsna</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/467789" target="_blank">📅 20:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مهلت انتخاب‌رشته کنکور تا ۲۰ مهر تمدید شد
🔹
سازمان سنجش: مهلت ویرایش و انتخاب رشته برای آزمون سراسری، دانشجو‌معلم و پذیرش صرفاً بر اساس سوابق تحصیلی، تا پایان روز دوشنبه ۲۰ مهر تمدید شد.
🔹
این مهلت به هیچ وجه تمدید نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/467788" target="_blank">📅 20:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19508bd484.mp4?token=ftXhOGSSg2lpxdSM2XyrbUwXOfEFABnE1pWNEu8Ri_ImUNOgfhJiKUi557aGIbKZyHOi2ywwHkED4BsopmjSpGNdr-WSH1pvDZeoMzoCffKigkCWI--bCeP6wd9MVyMNmtqP6MbsaMVJpsMA0s5LRO7DXdMOjh0PUS2IUCRxbYkAejoVWrlYp9q-eVN6oAMFclvb-ykXrepdFjyohNLD9XeG1-dBqNWgEVlmagAYPPth5JsilYhiHcHlh7ogoQPfkqSC7bFQ3n94prSDimcHMFsJAyMtV0ps2LKySpLaHFV5-5TQWX4Xm51AgPMnPvCyD6G0SDPnMtUAZNCekUnE6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19508bd484.mp4?token=ftXhOGSSg2lpxdSM2XyrbUwXOfEFABnE1pWNEu8Ri_ImUNOgfhJiKUi557aGIbKZyHOi2ywwHkED4BsopmjSpGNdr-WSH1pvDZeoMzoCffKigkCWI--bCeP6wd9MVyMNmtqP6MbsaMVJpsMA0s5LRO7DXdMOjh0PUS2IUCRxbYkAejoVWrlYp9q-eVN6oAMFclvb-ykXrepdFjyohNLD9XeG1-dBqNWgEVlmagAYPPth5JsilYhiHcHlh7ogoQPfkqSC7bFQ3n94prSDimcHMFsJAyMtV0ps2LKySpLaHFV5-5TQWX4Xm51AgPMnPvCyD6G0SDPnMtUAZNCekUnE6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر، نظریه‌پرداز مطرح آمریکایی: تنها چیزی که می‌تواند آمریکا را وادار کند که به خواسته‌های ایران تن دهد، فشاری است که می‌تواند آمریکا را مجبور به توافق کند.  @Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/467787" target="_blank">📅 20:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbd387f614.mp4?token=IbIKrJDwTz-SEO1AqIgBKsxWoTgtb3kFLwhEe9n80XI1LWcWUibSYxizz_mMSR_9AZoRaG9c-4W-667pbouH6teCxFuWA0ELybuykrpluQXafDwAI26w9rHhlofnYNFF1LnPE0SFPXZzvDegxMbyVlohlgAl3uXiGnJWyICy5DY_V3JfYOZG3iADSU9iKiW_ObfY4uvvT3SPDYAnaNng321TiCrXZ89EXdGaVIUfCqVJSAnbzPVMKOGpS57HO2K9xASzla2tyrrOSC1gm6itZ3FdU2XYxO5-l7YtxgfnPgR5ZvRY_r82ETLmBqiIkF1dwmeVPOzZnao7RVNEz77IlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbd387f614.mp4?token=IbIKrJDwTz-SEO1AqIgBKsxWoTgtb3kFLwhEe9n80XI1LWcWUibSYxizz_mMSR_9AZoRaG9c-4W-667pbouH6teCxFuWA0ELybuykrpluQXafDwAI26w9rHhlofnYNFF1LnPE0SFPXZzvDegxMbyVlohlgAl3uXiGnJWyICy5DY_V3JfYOZG3iADSU9iKiW_ObfY4uvvT3SPDYAnaNng321TiCrXZ89EXdGaVIUfCqVJSAnbzPVMKOGpS57HO2K9xASzla2tyrrOSC1gm6itZ3FdU2XYxO5-l7YtxgfnPgR5ZvRY_r82ETLmBqiIkF1dwmeVPOzZnao7RVNEz77IlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر، نظریه‌پرداز مطرح آمریکایی: کلید موفقیت ایران این است که فشار اقتصادی زیادی به آمریکا وارد کند
🔹
این فشار آمریکا را باید وادار کند که به توافقی تن بدهد که از نظر ایران مطلوب است. @Farsna</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/467786" target="_blank">📅 20:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfebfb5d38.mp4?token=nR2Yjsg1xq2oB2ZDMdJkSLpJAAU5xbmzJ4VuqgH0JOzBqg-oDv2BitnkgEHDpsyavUnp_qMtx0GD9BRmDh3NQWfQmQ9kM_kKXV5xVSqlEJ0BWepRu-S5PnE1NMHO_G6UwadBKteTu538a1J7fDW8zczRtJVf5VAb43EetE4UVMv8ottPIZj0GLsAKxG_oSjeHePJCEts18D5bxoc1YfsKx0MW0slPfdxna7Ums58AfIkRxDZuBQotS2YFDF5BZdgufm3Go2wnz-kqlGV9dlUSJ2nkW10nRi5kMdpLvT9LeJyYNht3501D2MvnX_U6HupPdiDrB_YlfAqgA2FZQflOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfebfb5d38.mp4?token=nR2Yjsg1xq2oB2ZDMdJkSLpJAAU5xbmzJ4VuqgH0JOzBqg-oDv2BitnkgEHDpsyavUnp_qMtx0GD9BRmDh3NQWfQmQ9kM_kKXV5xVSqlEJ0BWepRu-S5PnE1NMHO_G6UwadBKteTu538a1J7fDW8zczRtJVf5VAb43EetE4UVMv8ottPIZj0GLsAKxG_oSjeHePJCEts18D5bxoc1YfsKx0MW0slPfdxna7Ums58AfIkRxDZuBQotS2YFDF5BZdgufm3Go2wnz-kqlGV9dlUSJ2nkW10nRi5kMdpLvT9LeJyYNht3501D2MvnX_U6HupPdiDrB_YlfAqgA2FZQflOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر، نظریه‌پرداز مطرح آمریکایی: کلید موفقیت ایران این است که فشار اقتصادی زیادی به آمریکا وارد کند
🔹
این فشار آمریکا را باید وادار کند که به توافقی تن بدهد که از نظر ایران مطلوب است.
@Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/467785" target="_blank">📅 20:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ورود مجلس به موضوع به‌کارگیری مدیران بازنشسته
مهرداد لاهوتی، عضو کمیسیون برنامه و بودجه مجلس، با اشاره به موضوع به‌کارگیری مدیران بازنشسته در دستگاه‌های اجرایی، اظهار کرد: موضوع استفاده از مدیران بازنشسته، از جمله در سازمان بورس، محل بحث و چالش است و انتظار می‌رود دولت در چینش مدیران خود به ظرفیت نیروهای جوان و توانمند توجه بیشتری داشته باشد.
وی با تأکید بر ضرورت رعایت قانون ممنوعیت به‌کارگیری بازنشستگان افزود: مدیران بازنشسته باید در چارچوب قانون جای خود را به نیروهای جوان، باانگیزه و توانمند بدهند تا زمینه استفاده از ظرفیت نسل جدید مدیران در دستگاه‌های اجرایی فراهم شود.
عضو کمیسیون برنامه و بودجه مجلس تصریح کرد: انتظار داریم رئیس‌جمهور و معاون اول ایشان در انتخاب و انتصاب مدیران دستگاه‌های اجرایی، از نیروهای جوان و باانگیزه استفاده کنند و این موضوع را در تصمیم‌گیری‌های مدیریتی مورد توجه قرار دهند.
@Farsna</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/467784" target="_blank">📅 20:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUTq-r_C4RNCr5wxVAbZBJ4mTp6_1aolyc0RxXHx0HbnSD45r2GGudMpVfQmrzQ6kaFYhChGmNED_0s9_hNXgHDzKZkgzJGOqJcJw3kQGEb-tmFlU00LxRr7QparPuvpQSUxG3lec133ZNzMyFGDfftSdUxhLtDQ3MqRUEIryD5EKsUjdq9okh8E-ZiY0XkywbZ9mz1MZCP7apn2cTxzjmV-OMgguuBEYVCDQE4AU3xarjq7kIp00GDK_9EvSOx9dHQYEXWXI94XiIzf6qbf8gPw-V0c4V7HegIcdrggg2-UNayuOig9KaBy7Olvon3YOMY4aES4PQTka5o39MxESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❇️
سالن مبله برای ختم
❇️
❇️
همایش های آموزشی
❇️
🔹
۷۰۰ صندلی
🔸
پارکینگ وسیع
🔹
تهیه بسته پذیرایی
🔸
هماهنگی واعظ و مداح
🔹
گل مصنوعی به نفع خیریه
🔸
سرو ناهار و شام در سالن
🔹
فیلمبرداری مراسم و صوت با کیفیت
🔸
دسترسی آسان به بزرگراه
شهید همت، شهید حکیم، شهید فهمیده(کرج)
📲
۰۹۱۰۲۲۷۷۱۹۹
☎️
۰۲۱۴۴۰۰۴۰۴۰
📣
امکان رزرو شبستان مسجد
📌
آدرس مسجد
🔻
فلکه دوم صادقیه،بزرگراه شهید اشرفی اصفهانی ره ، جنب بوستان صبا
🔸
مسجدجامع‌امام‌سجاد(علیه السلام)</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/467783" target="_blank">📅 20:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/467782" target="_blank">📅 20:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137513140f.mp4?token=OM-uENZTQtLiuDpzG6RXWoQh47nYGNEmfeSC-YHM_1c6Rgq2-vDgSxRAQ6sSS3gteWlfOtN2tz_9MLLGFp15YH8xmaGo09CtapxNIj4dZQGXuAmkBzZoOXEnPl7tgsk4MviKBj8lzIcKxsea5_cTPsxicKk_NisOrSkIzbHQxC-uUzYV3GyNnTw0f0a5tEQSQ2M1j8EoI6SM_56SSxhTH0EOS4nMrg1-I27b2Cc4Dz5vYvtJlGysRICMlJpYIaw6BHG6ggNbZbyRviD4BU7JEbEJKXmhFTJ-JPcuze7yjEc5W3w0FhmuIj3mIOXuhLxNAwCXm8CnAhFRsNfPg1y0hprcb1q02TsbMGNklRP55bUJORZwaHtP-D043gib4srpIk2x4tEXUrnwRpL4qrv_yP1A5dyUEmtsWZMkmDmMUBc14_YV8TK5aVPwMSNkUHkPocoxhfxd_D9qeOTEOSh7B3VFe6zjwXTXFKJ07b1c7zeBOL44l5GuVEPxEw0MohEd5RsLH-YvkTS84mLn9plwK8cb-ht7qYfQjKPzXVufISv7ukvy356fw8gXcuC4ajtoYkjpTjwYX4O783gGpqx9kvjG5S3cvFKCX1RZFH6KFh8OKpjE_VYwF3LSpIknjDtyd2K4S8WpYqv35sL2sJfexV1__1mqjXp1tZunYIoy0Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137513140f.mp4?token=OM-uENZTQtLiuDpzG6RXWoQh47nYGNEmfeSC-YHM_1c6Rgq2-vDgSxRAQ6sSS3gteWlfOtN2tz_9MLLGFp15YH8xmaGo09CtapxNIj4dZQGXuAmkBzZoOXEnPl7tgsk4MviKBj8lzIcKxsea5_cTPsxicKk_NisOrSkIzbHQxC-uUzYV3GyNnTw0f0a5tEQSQ2M1j8EoI6SM_56SSxhTH0EOS4nMrg1-I27b2Cc4Dz5vYvtJlGysRICMlJpYIaw6BHG6ggNbZbyRviD4BU7JEbEJKXmhFTJ-JPcuze7yjEc5W3w0FhmuIj3mIOXuhLxNAwCXm8CnAhFRsNfPg1y0hprcb1q02TsbMGNklRP55bUJORZwaHtP-D043gib4srpIk2x4tEXUrnwRpL4qrv_yP1A5dyUEmtsWZMkmDmMUBc14_YV8TK5aVPwMSNkUHkPocoxhfxd_D9qeOTEOSh7B3VFe6zjwXTXFKJ07b1c7zeBOL44l5GuVEPxEw0MohEd5RsLH-YvkTS84mLn9plwK8cb-ht7qYfQjKPzXVufISv7ukvy356fw8gXcuC4ajtoYkjpTjwYX4O783gGpqx9kvjG5S3cvFKCX1RZFH6KFh8OKpjE_VYwF3LSpIknjDtyd2K4S8WpYqv35sL2sJfexV1__1mqjXp1tZunYIoy0Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش برای بازگشایی مسیر روستاهای شرق گلستان پس‌از سیلاب
🔹
با وقوع سیلاب در شرق استان گلستان و انسداد راه‌های ارتباطی برخی روستاها، نیروهای امدادی در مناطق آسیب‌دیده حضور یافتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/467781" target="_blank">📅 20:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdBSlUvkEYp3ZZkoA8893gF1yH8hfisXrwZL9JvUoDlQHEmnFJaZ2mJb7BbU0wI249Zm9IXNBxDWhsx4qK-8aA2sKPG_khhzr_1jwvjqJvUM2ybti_bNh74NbSumUpAMKytRyP2VcMLOiHXgTclJDsxikJmRVD6YOYXZDgp5WIIcXfjz99bj2QxD97zEpzXJbe4QPU0W0DoRKhGR7xWTgKta9-IuABp3Pu23LprDmbphY7SEyQ2-kDZI0V0O7cGslIK6lkiktffUporcID1Klu-RELM2KLVT5QBPCurSSnptbigW8yOchwndYck-VgTofmpybT7umT1cYPrfiZ3gZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگهٔ هرمز یا وابستگی مالی به آمریکا؛ دلیل گرانی عراق چیست؟
🔹
بازار ارز عراق پس از تصمیم دولت برای کاهش ارزش دینار همچنان ملتهب است و آثار این تصمیم حالا بیش از هر چیز در قیمت کالاها و قدرت خرید مردم خود را نشان می‌دهد.
🔹
پس از حدود ۳ سال ثبات نرخ رسمی ارز در عراق، دولت این کشور نرخ دلار را از حدود ۱۳۲۰ به ۱۵۲۰ دینار افزایش داد؛ تغییری که ارزش رسمی دینار در برابر دلار را حدود ۱۴.۵ درصد کاهش می‌دهد و اکنون آثار آن در بازار و قیمت کالاها در حال نمایان شدن است.
🔹
گزارش‌های میدانی پیش از کاهش ارزش دینار نیز از افزایش قیمت کالاهای وارداتی حکایت داشت. برخی فروشندگان عراقی گفته‌اند قیمت کالاهای وارداتی در ماه‌های اخیر به دلیل افزایش هزینه حمل‌ونقل و اختلال در زنجیره تأمین بالا رفته و در برخی موارد افزایش قیمت کالاهای وارداتی به ۲۵ تا ۳۰ درصد رسیده است.
🔸
اکنون کاهش ارزش دینار فشار تازه‌ای به این روند وارد کرده است؛ بنابراین خانواری که درآمدش به دینار است، برای خرید کالایی که قیمت آن به دلار یا بر مبنای هزینه واردات تعیین می‌شود، باید پول بیشتری بپردازد.
🖼
اما ماجرای این گرانی‌ها در عراق چیست؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/467780" target="_blank">📅 20:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJKIVEcAIgpSe6QhZ9l0k24AuZ8k5lSkbTxBROKMFjeJSpceoBtIOPgiTrjPnSSfOeNFqQHILpz4wBfsMz3-RBi-YKVz5eG21kp3n4t8l8IotoFWIk5sN-vmQ1hmWoJKXHmBEc8hMLwSRZ_8KDUGN_otxqIEAwluLripXBI5XTicKPen6vOW8W1Duqzw1yFFHEhTyAqqvkPAPY1S_ZJjXihAx7oifY7P_euh2dZ8LzIdrGmAOLahoSLsSsX-pNN24Dt6sMPtKZvugE9UJ3_dxfUT8P_tGRxUY93eG-u-p_t_j9GzOuvaN_rsX9ChEI7cJqEnsltZpKn_IzOAwyfcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پلتفرم یلا» با پول انگلیس جنگ روانی در عراق راه انداخت
🔹
کریدل: براساس اسنادی که به بیرون درز کرده است،  پلتفرم «یلّا» که ادعا می‌کند رسانه‌ای مستقل برای جوانان عراقی است، در قلب پروژه نفوذ پنهان انگلیس در عراق قرار داشته است.
🔹
«یلّا» یک پیام‌رسان نیست؛ بلکه یک رسانه خبری و شبکه اجتماعی است که مخاطب آن را دنبال می‌کند، نه اینکه با آن چت خصوصی کند.
🔹
یلّا خود را رسانه‌ای معرفی می‌کند که نه کسی به آن می‌گوید چه بنویسد و چه منتشر کند، و نه پولش را از جایی می‌گیرد که مجبور باشد حرف آن جایی را بزند.
🔹
پروندهٔ رسمی این پلتفرم هم می‌گوید «یلّا» با سایر رسانه‌های عراقی فرق دارد، چون به این یا آن گروه سیاسی وابسته نیست و از هیچ جناح خاصی دستور نمی‌گیرد.
🔹
اما اسناد درزکرده نشان می‌دهد این ادعا با واقعیت فاصله دارد؛ چون در سال مالی ۲۰۱۹–۲۰۲۰، ۴.۳ میلیون پوند و برای سال بعد ۴ میلیون پوند دیگر از سوی دولت انگلیس به این پلتفرم تزریق شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/467779" target="_blank">📅 19:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌  سخنگوی نیروهای مسلح یمن: مزدوارن سعودی را وادار به فرار کردیم
🔹
یحیی سریع: نیروهای مسلح ما، یک عملیات پهپادی موشکی علیه تجمع‌های مزدوران سعودی در مناطق رأس العاره و السقیا انجام دادند که ده‌ها کشته و زخمی برجا گذاشت.
🔹
همچنین عملیات موشکی علیه یگان‌های…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/467777" target="_blank">📅 19:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">۴ عملیات موفق یمن در چهارگوشۀ سعودی در یک روز
🔹
سخنگوی نیروهای مسلح یمن: در ۲۴ ساعت گذشته، ۴ عملیات مهم با موشک‌های بالستیک، کروز و پهپاد در خاک عربستان انجام شد:
🔹
فرودگاه بین‌المللی ملک خالد در ریاض را در ۳ مرحله هدف قرار دادیم که منجر به اختلال در پروازها…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/467776" target="_blank">📅 19:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467775">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">۴ عملیات موفق یمن در چهارگوشۀ سعودی در یک روز
🔹
سخنگوی نیروهای مسلح یمن: در ۲۴ ساعت گذشته،
۴
عملیات مهم با موشک‌های بالستیک، کروز و پهپاد در خاک عربستان انجام شد:
🔹
فرودگاه بین‌المللی ملک خالد در ریاض را در ۳ مرحله هدف قرار دادیم که منجر به اختلال در پروازها و تعطیلی کامل فرودگاه شد.
🔹
ایستگاه پمپاژ گاز شرکت آرامکو در منطقۀ شرقی عربستان منفجر و دچار آتش‌سوزی گسترده شد.
🔹
پالایشگاه نفتی آرامکو را در شرق عربستان هدف قرار دادیم که منجر به آتش‌سوزی در آن شد.
🔹
فرودگاه بین‌المللی ملک فهد در دمام مورد اصابت مستقیم موشک قرار گرفت و درپی آن پروازهای این فرودگاه لغو شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/467775" target="_blank">📅 19:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
🔴
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد. @Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/467774" target="_blank">📅 19:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467773">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORhDTC719iOzQ15Zx4pb6P0nZZs-KVGse5b8gpgRRbljvY1JglVFdK41pDheD5erNWCzc1u0klnAKcd22ynB-K3371m3Nlq14ko2i_P7zmBQtau0s7zt49wDuvBeMB2Ko_ka-GrjdB2ULxGI5V1G54qtuyQ8tOzo21XHKG3gKqddeasL1mpbBlLo8eVv10gowU5WlC_VT42bnZpemEcI5kaR8xuTXPdz8RMLwLlU_Itc818cd9FVOfoTYYAEntc8nCroJFN5cOiBLXT6IArDcqWaqcob_LzcMSkuYplSRiR1nvJHdaRRtHPFUveUhkCoZKFKhzMqM7LUm_8WRhk6Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌اتم: واحد یک نیروگاه بوشهر با ۱۰۰ درصد ظرفیت فعالیت می‌کند
🔹
مدیرعامل شرکت روس‌اتم الکسی: در حال حاضر ۶۳ متخصص روس در نیروگاه اتمی بوشهر حضور دارند.
🔹
لیخاچف در بیانیه‌ای با اشاره به روند ساخت‌و‌ساز در این نیروگاه گفت: در حال حاضر، تلاش‌های ساخت‌وساز بر…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/467773" target="_blank">📅 19:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467772">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها در تلاش‌اند تا راهی برای خروج از این مخمصه پیدا کنند، اما شکست خورده‌اند
🔹
دلیل آن این است که آن‌ها قدرت عظیمی را که در ایران وجود دارد، درک نمی‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/467772" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: بدون مدیریت ایران بر تنگهٔ هرمز، خلیج فارس نمی‌تواند امن باشد
🔹
کنترل بر تنگهٔ هرمز نمایانگر ثروت ملی عظیم و یک دارایی ملی بزرگ است.
🔹
منظور ما صرفاً بستن گذرگاه و دریافت عوارض عبور نیست. منافع ما بسیار فراتر از این‌هاست. البته…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/467771" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها به ۷ شرط ما پاسخ دادند اما ما آن را ناکافی می‌دانیم
🔹
طی ۲ ماه گذشته، آمریکایی‌ها از ۳ کانال مختلف یعنی پاکستان، قطر و حتی عراق به سراغ ما آمده‌اند و از ما خواسته‌اند پیشنهاداتمان را به آن‌ها ارائه دهیم.
🔹
حدود ۲…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/467770" target="_blank">📅 19:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: روش دیپلماسی ما تغییر کرده و ما دیگر به دیپلماسی گذشته برنمی‌گردیم
🔹
ما ۳ دور مذاکره برگزار کردیم و در هر دور، آمریکایی‌ها مذاکرات را نیمه‌کاره رها و به ایران حمله کردند. بنابراین، ما دیگر به الگوهای دیپلماتیک قبلی برنمی‌‌گردیم.…</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/467769" target="_blank">📅 19:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467765">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: ما درحال بررسی تأسیس یک «شورای جنگ اقتصادی» هستیم
🔹
احتمالاً چنین شورایی تشکیل خواهد شد و ما به ترامپ و بسنت نشان خواهیم داد جنگ اقتصادی واقعاً به چه معناست و آن‌ها در این نبرد در چه جایگاهی قرار دارند.  @Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/467765" target="_blank">📅 19:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467758">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtLrvNWsnDLDHSzho821qNZguSYRyyo_VEHF08hs6H-uz0L5ui1TYPDooHUeBF6yMEaz92XKq74lqT_bnWRjedSg7rvEuSpOwmh8ukXjK1Aiqz_GLEw1D4qohmaswYojJ6Te93GyMqabz93M6wlx7hi2_ZF93QoW7fz460fe4RWW7FUDaiavCUiQ3Xeka-M43aBocjhX-760u9P0ET-yvoS_beF9nL4SHYUsxbmewmFQXwoL4flBZ6FL6k-Uz414SD03N6qxur-ROkdvVtf2xPc5aocIJuUFTXuTbGgHM-OrIxEZ8EecN2zxzaKszBcGT9t7Qy_1bbtGQU6ANKTi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rx9xDN8z33_geXLkU-meha4XT5-U0nrcOhRf9qDV6iuPNGPzYhkD8jcZMvU3UdbHyjwZJ6DCLEPSXBL8Y-tNbUecVz-iwY5tVCXoVja30mYbHwRF9AuHoNLlJuMVKakfGfWdyC7SIbsnBoAwj1LDTPeX3ZZ4rwJdTUO2tbFZo3qfYp_dwRqqtCHsht41QAPwc0Wvk_Jaidfypzo4SJ74PpggqPON4tm1ihoELZcCFqtq842Ajd9xnvaWHdccghXABaD2Y6TZDexHRC70KyLk_1UjoLZBIEAFgfBPk6yDHdctDGLm6eUQG1Z5qCK9OSekuyQ46BuH2xmMcF7gU04c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RED4UKfd-ialnVTB7fyYalESec1LlCo5ObZFy6t2J_T1QDQTlebqOnfOIR_7pS1CpUb-7gpokGKSWLMzNVN5BFa5MpbI1zOkWAPZtpEWNdQWHsjnWX0DGoJvF5eX0pyUAO9d52GI1hq-iSP1bBNWMVjUKHnFAVstk6Tprm4uYckfedSOWJsy3IoEYPeo9Lz2amhvABEpOYaL3BJhgTVOPeSsi7vbvU-SNNTMvJRWqAr2FHIUy9uJuqFZS98eilp9u4mCeu8a-042hba-YuDXb3LXbgrYrvTqNrypHd4soDuFBcgB0WpuJ9F9GdBg-brwWeu4O1qMPVsiNV0XUVctGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbiRrOEjc65UQTHATWwpSQofR9j9BqpWMiTpdXoUUkWZ-EpmOcqcEtECyMel3q-NYEIqtAEXXxLVVIiaJ1x91rgjO0aEa5E-v4mlFdqYfS53n4Z1LnXFyvh6iuyhv5xuybqTtK_t4p9UmAN6hlv7T2tBruCUkV0XZpzgDm2VfGxwJDIQy8hDTWDhcHx1_3q65v1rS964-_2W5vpdji4H9CywuSR4rrNUVQFl-9nQwbKvin1MsNvyHnKZi9_t9DbaijXE9ikIx-LbsGzWGWK-c3jxH4FIlp-EAg6dHmUe9PjknEk29EcyMGKOCw-ONhenSjlg-DzPm9RFKJ0Hs4lJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJs4ilTQjdALmT9oR_XLV2R8fJi-abDLifgYlq_2iIQCz3DRT5zrmnbd_hKo3Qw1SobDf6UaKUpNrsLYdFECW4zTXUoiQPgMp_Es6NsTemn2VkzK0VA3juHwzGyfO9bgQD0GgviDrT-qAdQD7Qb4bGZWv8WL2X7r2m1m9MXyrV7yeGqSsrRrcF0SS4LWMPBWrbxWZwMrf4Uo2v51boji7MgUMeR9-lT45d5Bwt4lA2R443zddeC-hEHfmleOEpKkIbvfr7WrxK-vdJXRKTrp_WBO_EJeR0_fc3EkJEVlw9kyeXgfrqqNIRt5nsxFwtSXlQUt3x2szXqJ57SjDGZthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0xfKd1_5VdYbaCPcpnxmrOuOv78Ejy88WfAn_yOXhRmasGu9zBjIEJCZJvllM4JEwhx7kJkalLecIzPmEXORXamoOR-bonRAtgmZxwfhWO2Igt06hfFjDRgPo0AKt56D_8a8FiCrvK9qnArGbYotmnNP81GDzXoYfmWVO0EAwL1jneKhrX9bod8Sn0rrD2eV60-rj7XwXs-LmQ1mfYmtoSl9vVEDBA28nhhJSex-p3irjcR4Xa40eIG9sCoz6hRgiEQgdRCpv-R37O7rhIcbiIt3AcaE4bcI63lCkBUN6yMsSepLu9PcjRD7X9M_9BpcoGs83nYl3s02Eam2Oj15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPX-hT6XThl3FFKp810u8MeYBq9u9PKC_uIKyht3qmHDuZUsJoVWflfRAQSZr16BOD1bp856Y4hsovGjy8zaRDfNe7HHr3GzPEiyamQWpmYAX-Acfs-P5cS42f83jMkyq1RnTeBsQ1rhTiLC0Rz1znPB3Gd20VTQtDgixYoRHE0y9I1eQMXknejRFeRcbZqHFa2VvuZLZbmXN9Wq5AK6W3iEMhzxTJ_4DhhcSiQXla5vA9lOln1Djhdndsg927-MYiHkRAQB9P6NIhT856JxDoEX1ZZOnRm0IzTocVNPsLpOjw3iY36AMqKVe99Ks-AI6K_Rc_qwx-13k4HM45iliw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اینجا کیف بچه‌ها کوک است
عکس:
محمدجواد فرخاری
@Farsna</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/467758" target="_blank">📅 19:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467757">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">زخمی‌شدن سرباز صهیونیست در مرز لبنان
🔹
رسانه‌های صهیونیستی: یک سرباز ارتش اسرائیل در یک عملیات در مرز با لبنان به شدت مجروح و با بالگرد به بیمارستان منتقل شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/467757" target="_blank">📅 19:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467756">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86149a52c2.mp4?token=BDBJGCDMALTSDBdpmrJDxhH0myOglX-DV3G9LuKu-rKURyrAKzibGAb2-x_wJq7GIAH5dl6myV59Fom-r-OMw-jQBTXPxVmFsW8kIX0-iLIyh51N-jQ6MFM4vM1duY4E5HtUcLjY5jGquShPVkky2Dl1IzUNdEDuegoeHuWP8wPUUVIG0FcevJU5cmuU5V66jDeNbmomfyl7RO-4F02HU16lHm_2FHOtGS8SSFrNs8zdNYVjAwBQbPdwwFmtU69ocmlw7iYWHyzVji214FSxsBVDTUQZEwE5i86MZzAKWN5Ut7row7YlQlbYhJY-veIG5FwuAiM9dXOvOAdPBikujB1SjHN3BRKkav3UC5pLp2KThrx2lQ98gbTYEgb8mg-1ux1c8mrUHJh3sOfRGE0gEw58fFiQD0NBDXMduEKKK7YzzIgr4-A_BMWCAEDoGZWLSJITFmplbT3dOI0DjJg_dZNKjxQxdg60vww5yRq4J00mo9GNXWnwqp1jhvvbaIm9no-RdxaRGWjWm1tCxe_ruqR4POR_zZGndOOJ2XgTVUcvc6V6nHNJIEtBdEFpmVkuwZJaSOd9Ps5ZOh5tEqBd69PQ8tOFo8JmlLFSS3KkN2OYTsTCGL94LlEj1sIOPSQImDkbeaAtQTvmdMYixrcquhlIOua0ngM3umT90tJiUjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86149a52c2.mp4?token=BDBJGCDMALTSDBdpmrJDxhH0myOglX-DV3G9LuKu-rKURyrAKzibGAb2-x_wJq7GIAH5dl6myV59Fom-r-OMw-jQBTXPxVmFsW8kIX0-iLIyh51N-jQ6MFM4vM1duY4E5HtUcLjY5jGquShPVkky2Dl1IzUNdEDuegoeHuWP8wPUUVIG0FcevJU5cmuU5V66jDeNbmomfyl7RO-4F02HU16lHm_2FHOtGS8SSFrNs8zdNYVjAwBQbPdwwFmtU69ocmlw7iYWHyzVji214FSxsBVDTUQZEwE5i86MZzAKWN5Ut7row7YlQlbYhJY-veIG5FwuAiM9dXOvOAdPBikujB1SjHN3BRKkav3UC5pLp2KThrx2lQ98gbTYEgb8mg-1ux1c8mrUHJh3sOfRGE0gEw58fFiQD0NBDXMduEKKK7YzzIgr4-A_BMWCAEDoGZWLSJITFmplbT3dOI0DjJg_dZNKjxQxdg60vww5yRq4J00mo9GNXWnwqp1jhvvbaIm9no-RdxaRGWjWm1tCxe_ruqR4POR_zZGndOOJ2XgTVUcvc6V6nHNJIEtBdEFpmVkuwZJaSOd9Ps5ZOh5tEqBd69PQ8tOFo8JmlLFSS3KkN2OYTsTCGL94LlEj1sIOPSQImDkbeaAtQTvmdMYixrcquhlIOua0ngM3umT90tJiUjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر منتشر نشده از حضور آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب در دیدار با علامه مصباح یزدی
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/467756" target="_blank">📅 19:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467755">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: بسنت در آمریکا به عنوان یک «وزیر دروغ‌گو» شناخته می‌شود
🔹
وزیر خزانه‌داری ترامپ بیش از یک سال است که بیانیه‌ها و وعده‌هایی داده که در انجام آن‌ها شکست خورده است.
🔹
این مرد کسی است که می‌خواهد با ملت ایران دربیفتد و جنگی علیه…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/467755" target="_blank">📅 19:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467754">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی خطاب به آمریکا: ایرانی‌ها هرگز در برابر شما تسلیم نخواهند شد و تا زمانی که حقوق خود را از شما نگیرند، هرگز از مطالبات خود عقب‌نشینی نخواهند کرد. @Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/467754" target="_blank">📅 19:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467753">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: یک پیام برای روبیو دارم
🔹
سرلشکر رضایی: من پیامی برای وزیر خارجهٔ آمریکا دارم: «مردم بسیار بزرگ‌تر از شما بارها در طول هزاران سال آرزوی آمدن به ایران و اشغال این کشور را در سر پرورانده‌اند.
🔹
قدرت‌های گوناگونی رویای ورود به ایران،…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/467753" target="_blank">📅 18:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467752">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: ما با مجموعه‌ای از افراد بی‌سواد در آمریکا مواجه هستیم
🔹
ما با گروهی از افراد نادان و احمق در ایالات متحده روبه‌رو هستیم که تاریخ را مطالعه نکرده‌اند و ملت ایران را نمی‌شناسند؛ در نتیجه به چنین وضعیتی رسیده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/467752" target="_blank">📅 18:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467750">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMPdetIDryVfnrdknZYmONtG5V46IEbL5lNQpmoQX8RI3orYH0-i0RsQlKr2M3seMopy6jydaC8kofKKz__nB3X1Agnqq9CDt8i99NaioPjxidtKnYDWtclZM7hpM4Lk6J3lvU0a81JkzWihCZiPzyMXKIxB2iH7J4udGWd3bURKnMQWO_Hk7nMzCrFEDBWkZMnIXHc6hSQ8nR0CEimA-9lZxsyBp1UeL-QTJVjV87lDT9uCNyyPe1TedBKR9OxhMA8Hew0TPCwuKEid2hPcrR8tnJ63nLnHqMoPSmCud4lyQ0mHMEy9Np975JF9HE6Xdt3gAt0GvRSRobXgkdi6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسب‌ها هم از دست بلاگرها در امان نماندند
🔹
رویداد پاراسوارکاری روز پنجشنبه در باشگاه سوارکاری ابرش برگزار شد، اما حواشی این برنامه از حضور بلاگرها و هزینه‌های تبلیغاتی گرفته تا برهم خوردن سکوی قهرمانی بر اثر طوفان و ماجرای برخورد با یک عکاس، این رویداد را تحت تأثیر قرار داد.
🔹
بر اساس اطلاعات واصله، اسپانسر این رویداد که یک شرکت واردکننده خودرو بوده و برای حضور در این برنامه هزینه زیادی کرده است. گفته می‌شود این شرکت هزینه‌های هنگفتی نیز برای دعوت از بلاگرها و تبلیغ رویداد پرداخت کرده و برخی از این افراد با پوشش غیرمتعارف در محل برگزاری مسابقه حاضر شدند.
🔹
در میانه برگزاری برنامه، وزش طوفان نیز شرایط را تغییر داد و سکوی قهرمانی را برهم زد تا این رویداد با حاشیه‌ای دیگر همراه شود.
🔹
علاوه بر این عکاس خبرگزاری فارس که برای ثبت تصاویر این رویداد در محل حضور داشته، اما با برخورد نامناسب اسپانسر مواجه شده است و محافظان اسپانسر قصد داشتند دوربین وی را به زور ضبط کنند که با دخالت عوامل فدراسیون، این اقدام متوقف شده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/467750" target="_blank">📅 18:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467749">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: تهران به رویه‌های دیپلماتیک گذشتۀ خود باز نخواهد گشت. @Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/467749" target="_blank">📅 18:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467748">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkuZgWrYpgu_nyBfchBiD3hi2uJVgQkaidS2eO9y54F2nK8DOxKdZfklEQYcihzdSrK-rW2O2B4A7hOWidHiFWpcG1imJxEtDTG43d4cZx6q79h-SMkGX_TsgjXN1wnXDhcyZ3sbB6Pl3B6IvyAdPLtyNYxXqRKwuH4eQSAY1gjEMJVz4x_h__0psA2y2Yat5ggaKfmQbSesxdKfqNx2QADklhdJ0QIOFNYO6kXHgbiKb90oN13_ltrxvueLxg1ixD5FqQLGqHvg07l3fdAkjwe2TtVSenjyQGiyFi_9oH6xBSnWxaU5p_4nx_JzdqSUevRxbZEahay5959NDFV-Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخبر: ایران فراتر از مرزهایش به دشمن ضربه می‌زند
🔹
ایرانیان، مهاجمان مغول را مسلمان کردند و فرماندهان امپراتوری روم را با خفت به زنجیر کشیدند.
🔹
مهاجمان جدید که با مغزهای کوچک، تصور غلبه بر این ملت تاریخی را دارند، این بار در تنگۀ هرمز غرق خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/467748" target="_blank">📅 18:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467747">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیشروی ارتش یمن در دروازه غربی شهر «تعز»
🔹
منابع خبری گزارش دادند نیروهای مسلح یمن در حال پیشروی در ارتفاعات «صبر» هستند که مشرف بر شهر تعز است.
🔸
همزمان با این مسئله، ارتش یمن بخش‌های گسترده‌ای از ارتفاعات راهبردی «هان» را تحت تسلط خود در آورده است. این منطقه،…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/467747" target="_blank">📅 18:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467746">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: امروز اگر رویارویی دیگری رخ دهد، قطعاً با برنامه‌ای بسیار وسیع‌تر و گسترده‌تر به استقبال دشمن خواهیم رفت
🔹
کابل‌ها، دیتاسنترها و تأسیسات هوش مصنوعی موجود در منطقه بیش از ۲ تریلیون دلار ارزش دارد. @Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/467746" target="_blank">📅 18:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467745">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtPx2KDGhE_1d4XOJ8x4wpqo9fZV8U0uOaiyQdJ-n2qKJ1GO3iO5o0EQi3TapUdTzANJo5JDQfODZIP63opnnGa82FMWOjD9evSkKwjwYbbU3RMo31dqBDTmw3A26m12xOVFWr1aEfREJgLMad8yUTSrKBtaI8pUhqvUZnn0HS5JpOy2Irn1X_qp97saVaxZGNTOiu2A3Md9R2mmcXEI_lbcWtBWaMYuNixmMmA6dR9TMrdIboICQ41EnL6kUxV_GMMaznBX9_fZYjP_Sx6iQ4iznXQJCg1kILfbtG9fL4KUSihbrZACc9hlFB7GL7WEHZcUwsnCvN2i4WuDCGsdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تلاش ترامپ برای کنترل قیمت نفت این‌بار با آتش‌بس انرژی
🔹
رئیس‌جمهور آمریکا در تازه‌ترین اظهارنظر خود گفته: «بین روسیه و اوکراین یک آتش‌بس انرژی برقرار شد و هر دو طرف توافق کرده‌اند؛ آن را نقض نکنید!» @Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/467745" target="_blank">📅 18:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467744">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: اگر دوباره جنگی در بگیرد، بسیاری از کابل‌ها، دیتاسنترها، تأسیسات هوش مصنوعی و سایت‌های دیگر موجود در منطقه نابود خواهند شد. @Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/467744" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467743">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: آمریکا دارایی‌های بسیار گران‌قیمتی در امارات و پیرامون تنگهٔ هرمز دارد که ما هنوز آن‌ها را در میان اهداف خود نگنجانده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/467743" target="_blank">📅 18:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467742">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌‌
🔴
دبیر شورای‌عالی امنیت ملی: ما کاملاً آماده‌ایم که اگر جنگ دوباره آغاز شود، توانمندی‌های جدیدی را به‌نمایش بگذاریم. @Farsna</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/467742" target="_blank">📅 18:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467741">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: فرمانده سنت‌کام کارهای قاچاق را رهبری می‌کند و او همچنین از ارتش امارات استفاده می‌کند
🔹
آن‌ها از ۵ یا ۶ شناور کوچک برای انتقال نفت به نفتکش‌های بزرگ‌تر استفاده می‌کنند، اما ما نیز هر شب ۵ یا ۶ فروند از آن‌ها را هدف قرار می‌دهیم.…</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/467741" target="_blank">📅 18:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467740">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در ریاض پایتخت عربستان خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/467740" target="_blank">📅 18:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467739">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aece21a246.mp4?token=oAq8iwHh_P-pE9_LJJgWgCdOmJkPvLQrPJSZopO_tRhvRZezJo6BfwSQENy8pHLUMxSFoPBl05m4XS-MXj-iRBUioB8t7qmJwOSGqmLmI44_S5nXvp4kbTBVLEGyTsL4pOJPpsfgieTDqNPU0riC3GIqdIZOUtDcMvomRp0Xi9zfSZxyJraGAn9Hd6s2XbuMPZKfdkAbfr1aKSLGLHrCNkQQeXiUwhxksBpXJl9z5BE0o0SbCAzEixIsUZ4miRHbLWOujQeXuC61MEgzLN8xJru8L24BrkTshQE812VP6s5odFDwVXtm3-BkNQqgeroRC00yPKjPYGisACTop39Ijw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aece21a246.mp4?token=oAq8iwHh_P-pE9_LJJgWgCdOmJkPvLQrPJSZopO_tRhvRZezJo6BfwSQENy8pHLUMxSFoPBl05m4XS-MXj-iRBUioB8t7qmJwOSGqmLmI44_S5nXvp4kbTBVLEGyTsL4pOJPpsfgieTDqNPU0riC3GIqdIZOUtDcMvomRp0Xi9zfSZxyJraGAn9Hd6s2XbuMPZKfdkAbfr1aKSLGLHrCNkQQeXiUwhxksBpXJl9z5BE0o0SbCAzEixIsUZ4miRHbLWOujQeXuC61MEgzLN8xJru8L24BrkTshQE812VP6s5odFDwVXtm3-BkNQqgeroRC00yPKjPYGisACTop39Ijw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت بی‌واسطه ثریا از سرزمین اژدها
🔸
از شنبه تا پنج‌شنبه، ساعت ۱۸، شبکه یک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/467739" target="_blank">📅 18:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467738">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎥
ترامپ: فکر می‌کنم وقت آن رسیده که اوکراین یک رئیس‌جمهور جدید داشته باشد
🔹
پیشنهاد می‌کنم که آن‌ها یک رهبر جدید روی کار بیاورند که بتواند توافق کند. زلنسکی می‌توانست توافق‌های زیادی انجام دهد، اما به دلایلی هرگز این کار را نمی‌کند. @Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/467738" target="_blank">📅 17:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467737">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr0sXwVnJLlUnKfWjGgkvJQX2xkpRKx5295h08zN_JeR9LjwzS2_To60VhynKBwkqyDnBR9x8QphzdXEO0uI_iUrBQJAqRUcVJPO6aG7BHNHPFSUZizGY0BOFe-2z1SoJu84YInb_B9qYMPgzrTO7xpAT69hv9ND4MNYhtYDl_YK_OYv4fptb4-prGr1aHfGCJbD6RA_vnBnuWQDPCIQqW1GX41FDGb1fFqp4FrazaCnJIJxANo8cmN-O92BfGH8gWmozXip7oEjGlVFG8H4dapTrjjpsUY9Ant8HDTDzKxFhfYtpMFLyAXgZZcntLT4E0Lpu7fJvUI1MGPsIdreCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن‌سلمان برای مقابله با یمن دست به دامن صهیونیست‌ها شد
🔹
روزنامه عبری «اسرائیل هیوم» گزارش داد که محمد بن سلمان ولیعهد سعودی از طریق آمریکا به این رژیم پیام داده و برای جلوگیری از تشدید تنش در دریای سرخ و باب‌المندب به دست انصارالله درخواست کمک کرده است. …</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/467737" target="_blank">📅 17:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467736">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: طی چند ماه گذشته، ما هر شب در تنگهٔ هرمز ۵ فروند از کشتی‌هایی را که قاچاقچیان استفاده می‌کردند هدف قرار داده‌ایم.  @Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/467736" target="_blank">📅 17:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467735">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: ترامپ با استخدام تعدادی از اشرار که در آب‌های ساحلی عمان فعالیت می‌کنند، به قاچاق روی آورده است
🔹
او هر روز ادعا می‌کند که تنگهٔ هرمز باز است اما در پاسخ می‌گویم: شما درحال قاچاق هستید، اما تنگه تحت کنترل ایران است و ما آن را…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/467735" target="_blank">📅 17:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467734">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: عاقبت قدرت‌هایی بزرگ‌تر از آمریکا که تلاش کرده‌اند ایران را فتح کنند، زباله‌دان تاریخ بوده است.  @Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/467734" target="_blank">📅 17:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467733">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: عاقبت قدرت‌هایی بزرگ‌تر از آمریکا که تلاش کرده‌اند ایران را فتح کنند، زباله‌دان تاریخ بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/467733" target="_blank">📅 17:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467732">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در ریاض پایتخت عربستان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/467732" target="_blank">📅 17:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467731">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/962b87eb94.mp4?token=R9Rpbxk2M0PAPPd3eQ-STj4k-UlraYw-qPxLNmn6y9MVo9MkOaAwcnTASdWx1jFIJ-dQZEGwK2BCXmZ6gdgucU2N09WEsiuq3AV2H_pHCUfnEKHURsJyfmxJGRwFzrZI5eUDXP6_hPX7nE0cdzjgcVEutES1F48hivqs9kqHDs-Mnk73w16cTf_kYoINhva_yZiLzuSB8rnJ4prmZLQMAwfn0NhIb3fGcWefG4Ef88hSOvnODXOowhO4VydRqYlOvPzoWAMSqozjvP1UlPw5fCF5Cn7M28OGRyU_VhOgz6ep14Fm9ay-icQI7oyVhdP4DFCVMc1U9oiMthyYPy7yjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/962b87eb94.mp4?token=R9Rpbxk2M0PAPPd3eQ-STj4k-UlraYw-qPxLNmn6y9MVo9MkOaAwcnTASdWx1jFIJ-dQZEGwK2BCXmZ6gdgucU2N09WEsiuq3AV2H_pHCUfnEKHURsJyfmxJGRwFzrZI5eUDXP6_hPX7nE0cdzjgcVEutES1F48hivqs9kqHDs-Mnk73w16cTf_kYoINhva_yZiLzuSB8rnJ4prmZLQMAwfn0NhIb3fGcWefG4Ef88hSOvnODXOowhO4VydRqYlOvPzoWAMSqozjvP1UlPw5fCF5Cn7M28OGRyU_VhOgz6ep14Fm9ay-icQI7oyVhdP4DFCVMc1U9oiMthyYPy7yjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساروی: حسن آقای یزدانی الگوی همه ما است
🎙
محمدهادی ساروی کاپیتان تیم ملی کشتی فرنگی در گفت‌و‌گو با فارس:
🔹
برای همه قهرمانان احترام قائلم. قهرمانانی که الان در کنارمان هستند، قهرمانان جهان و المپیک، برای همه آنها احترام زیادی قائلم. آقای حسن یزدانی، زارع و پهلوانان کشتی فرنگی مثل امین میرزازاده و اسماعیلی، از بزرگان کشتی ما و از افتخارات کشتی هستند. من برای همه آنها احترام قائلم.
🔹
این نسل از بچه‌ها واقعاً بی‌نظیر هستند هم در کشتی فرنگی و هم در آزاد. از بزرگان کشتی هم آقای پهلوان یزدانی واقعاً کسی است که همه از او الگو می‌گیریم و به وجودشان افتخار می‌کنیم. او خیلی انگیزه‌بخش است و ما از او درس اخلاق و درس قهرمانی یاد می‌گیریم.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/467731" target="_blank">📅 17:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467729">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL70ryJdFvE2Lr3lfT1dT3VcciTAhDT1j8Usp9pRLJSLBLmMxqxM8mdERlMD-rAs6QhvxueGzKXHsyuSFdRhLtMI14gI2PibwbcaghA-fZ5IITtSxJnkhrv9x0Dq40LczFoETNYrYaY-pzPmnpGwzCSLS_gZuu6QjhtX9qjlFU6_4GmEOcRgsVHBzeZmj7gbio4rY3vDfwhuAWt9MjIrDb_8hPi1S7u560nTLJfo6OYKZzUUAPSbWPTPpcoSeJpP7uLrJgR4BV1ccBKs8Y8UA5XuHSIZMDCvY5ccyyJjswK10ZrbD386MeVTQyYtfi7NbNJGiV6Y5WXzWqAZhLoCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
منابع خبری از آتش‌سوزی یک کشتی در مسیر جنوبی تنگهٔ هرمز بر اثر اصابت یک پرتابه خبر دادند.
🔹
برخی ماهواره‌های حرارتی هم یک آتش‌سوزی بزرگ در این منطقه را ثبت کرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/467729" target="_blank">📅 16:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467728">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueFci2ZyoljWythgUJCvVRVb0Yw0JzP6IfcyOEdNSsIZs8FZVoGbo7IDawJg69gk-6CDKcEQYDd0xltZlHA10QAanYN4uUtJZ33haiG1MutBhMzzhtl8-wuC_xvHsMamHW-M7YwCxgtChqK_HqhmW3EyGZsu3uiHyqoHvZz4I1D_UJFWwnrXqB7VcXkwJGvFD56vgmr-ATjPWb0yhuV7i2e7EqWGZwaajuJFQB8Qd7a7wYZf3XTYTK3uzsO3NOx1zoehgM9fxN75smW2_66-nroWrcuCuZZG7ScNA905d41uoCiZb9QbbKxJwdtiM-GBEGSWmqQN-23oFa4f4AlmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار پول از خلیج فارس رکورد زد
🔹
کارگران خارجی شاغل در کشورهای عربی خلیج فارس نزدیک به ۱۶۱ میلیارد دلار از درآمد خود را به کشورهایشان فرستادند که این رقم نسبت به سال قبل ۱۳.۶ درصد بیشتر شده است.
🔹
این خروج گسترده پول، در شرایطی رخ می دهد که جنگ، ناامنی کشتیرانی و گرانی تأمین مالی، اقتصادهای عربی منطقه را تحت فشار گذاشته است.
🔹
کارشناسان اقتصادی در کشورهای حاشیهٔ خلیج فارس هشدار می‌دهند، اگر بخشی از این پول با ابزارهای پس انداز و سرمایه گذاری در بازارهای خلیج فارس نگه داشته نشود، اقتصاد این کشورها بیش از پیش ضعیف خواهد شد.
🔹
براساس داده های مرکز آماری شورای همکاری خلیج فارس، پول ارسالی کارگران خارجی در مقایسه با سال ۲۰۲۴ حدود ۱۹ میلیارد دلار افزایش یافته است.
🔹
بانک جهانی گفته،‌ وضعیت جنگی، تجارت در منطقه را مختل کرده، تولید نفت خلیج فارس را کاهش داده و فشار بر گردشگری، هواپیمایی، لجستیک، بازارهای مالی و قیمت غذا و انرژی را بیشتر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/467728" target="_blank">📅 16:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467727">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d916f969ed.mp4?token=EuyxeEF1yDYtCPl_e4gTYQvJse3blddAPB4XFYXQ_fa84BAbHPlCLrXEkyCFnSVMsKvo8UOctNZOwhi5T-tt6BucRW-vjuXeXroQWffGRV4bT7hlHUgxr7-6vUCTFg5Vx83vHJpbr5GSvfcsOQkWB-PHSY5RhSAfkqtRWKY_D-eio5o5GFOEN9WmwvTsunx18PxiVuhe6kipoZnnVcf8kCKRDIsbrVXzBWSTN2Cft_Zvsz380ximDiw0HOkkFFKvoJYdeevP5Gyd3gqC5wXMzfuTSHNwhOAjMA8ps2SZw2PmNbtfcmCuy8MBaLmw0haqYbOumnCO_gZrWmpTAD4BdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d916f969ed.mp4?token=EuyxeEF1yDYtCPl_e4gTYQvJse3blddAPB4XFYXQ_fa84BAbHPlCLrXEkyCFnSVMsKvo8UOctNZOwhi5T-tt6BucRW-vjuXeXroQWffGRV4bT7hlHUgxr7-6vUCTFg5Vx83vHJpbr5GSvfcsOQkWB-PHSY5RhSAfkqtRWKY_D-eio5o5GFOEN9WmwvTsunx18PxiVuhe6kipoZnnVcf8kCKRDIsbrVXzBWSTN2Cft_Zvsz380ximDiw0HOkkFFKvoJYdeevP5Gyd3gqC5wXMzfuTSHNwhOAjMA8ps2SZw2PmNbtfcmCuy8MBaLmw0haqYbOumnCO_gZrWmpTAD4BdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: چند جوان بی‌تجربۀ سعودی توحش را بر سیاست عربستان غلبه دادند؛ این به ضررشان تمام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/467727" target="_blank">📅 16:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467726">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bInp_a-vDeP1Y4qnsqfll2TjBVm8WTFTJUAxKtvNa9aObL-99C43fMRuJXG5nS9u9saBLH0BgIqx9FusfE15WLep_7HQ-jHGPUR0dPppQt8Ep9TebZGKEcxEl1KPRyAcrtRaOcOXb0IjwwATNVQ4CqCOiihd_M2CJOESRiT25nNo5pnKV7q4uuUz7sdQ8x_Snm41y5M_KzLKpzXnakosGVuU-gDLssB5rk2uAQjgkgtR6pjhjwOAaPmCiJ4dlh3kMuk69kUbvmN212OHP3Ezj3epxxxVJbebyOwrXFDGbghVgJnpFpMlSge1jxLa6xtJGHpmSHKJYtUQp9Y3XBprQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
همتی به بسنت: از قول ۲ هفته‌ای که برای فروپاشی اقتصاد ایران داده بودید ۵ روز بیشتر نمانده و من به شما می‌گویم که چنین اتفاقی هرگز نخواهد افتاد  @Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/467726" target="_blank">📅 16:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XboHF2X3mecGTEF8tU_3IT0HmCSwQjqfcbbPdYsxvLwAS0-JFFKHXT0Y1wHZ1pYvH1G9sNa9dNz9o6vgoj5Lciaw3Uspw6wQu0XdI-XBqSxEpDNC1hHxZwGeSdiCAfbX76xQHYjI_yjKJgn6zZjSlSy7wNxQe1Vnz9PGh45394vexj9RB8KcHSXzfj9zVMUBldPe0gHaz3sSHQodeksj6GZscVuLqNCoFNqEJbFfJ_SVFDmtm5QWRDxCBOuqHhRwwyYiYGDNLijG0kJSIgYKD8dzS4etmrdJ5xfJeyFt2y9tJcSwpga5njygZ59xC9eWgtleeirP2k6VXyRLDkeIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oz-kXdpTVTQSt-E5E_tyJ-DoXyn1f_PTaFaB4ADzjdHe_AJ3fEywCeEK7-u3J-paEMw0q2j6nFkTqmc6LsfQmSImGigFdKNzCdVbfoOLCgPDmXWZJKBhBejRG2EcdapjXTWMX3h_89q4ALjOD5HSk7VlO9NiAB5cjNpE0R0vscaBzzgTOAMMP9WUevOmjObXdN4m98v0pMedaiG8Bu9mypVzdfNJez-n0PrTLHDcrMEedz5hrM7okW2PtCXfmERQwVbHxPZyVEKnll9FIn_lKGR8fPzTec-SgncdHq9K4lWlP2oNKc4y0_PIJvmad2lwmCZTono4WAdT_253PM9gGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHbLGTRfk1m4WVQeqq8u_dykrJVbZdjVQGgFVilwnvDZlbQDXbaPJjT6uBRdqS3hriwNMaDhTSI6f1i1KkZlTIPQ_MAYaPykRGK9jpLWydz1ms8m74nkqotWHoop8kT_8E-vXkz18AuJ8oZqaPIOXfmTkwsaYHQNuozp_JYzz1LmKthSfFrQkp8Zsa786J-K22fhN6F56usfVCIqP8wVWNlmXy4JYi3wNXf5i9i_iLIpC3552ia2ur6GTeHbJnwidlKGKzI4ulMd1SgAd16TrCVw222d7WBBGhEHccHXHG6VXW0CFlWbeYYJIyNNIF_KhBXyVp6vZqIYAkZPcATzHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0Y-KbITwo2KURlYeWTfTnPfbGc-UnvtxeVGwRQXeAGxzACHV7elr4zbcLmrH_kzP52rYdGF5QK8ZBUQ01BfD-w5iT6jPUFIUIOWyt65_UmBO_CB0fpAMPDmY4HKh0tfDxNzMa-JuJuGewf8C5Yy9P2Qk5w5FATjNddzc2cbEVLhLhaw_pFmhUSbLMB1z-Pr9Bc50pxUhJu08o6Aw-XLr_GouAw2AciUSCFvJp5ltzKnq0vjmbxMwUxIOUAo9PaxLoa_dPx95gBhYNVODTCGoLLPhwaXbNvcmVXImQkGUaH8xkgkPwdIOQSiFxsuX3SBslvC3lvcWgYWYtbkTFAYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXdp82-oSGoWJIcfxSGicZMLv0_vfgEp_KOWQAegTeafLd73F1wDNpnEHv90FbZAZR7SrpVNRfSLIliDVn68fxf5ziGPAJzQVGk0MQ1nUZncdFrvhN8DxF_wjEmhdIhroNJZGl0tnHWGd8aTl759jWc03lJ7C15xK6evifzyRzRTWxPDdPPBtrWIzxBSLGKYIRr3-St1NBZMFqDDMnzmDqbVL1j7C3iN_c3QBbdYvlqfWk_5pnl56IEgj4P-zeeWbd2V981fd6HcZTaD0DbDcxTeHNnDGofs2APSrFBDA1UXuLi8tRzNAWexY8XthoW98sY-vfcFQfH7XRZNNpAfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoS9Zmim9D7AxnH5JnuB494TK24IyOymSaOJiM0jmwkfHKpydRNw7IGqS2ezvruxxYnSZVC0q0Ts6QGNxx56AcVSnHiSyP7N5qibkeRAAvd8pLa6ir11YNRml_43G0-4vNOnx-8fnmqg7avEeWvK56_rogqE14Ai3mAaZiJAINtLg_kQG3yCtnzdwCGSbvxSJ_SFzhVmPLxTzQcvPm8gLFYnVB0Ly9aSrgb1HssbEwl4HV5owPo2ko8x0k6eOtohFDbT_tMCDrlWk_gZT34c9Fe2DAjrBz96zt5q8hqAdYxaHO9vzTZpqE5u1_Y1GFZ5O2uKUxueN6e2BIbvuVCI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gumbp27uOAOoXDA884QDZ1TKq2szsN6B5qmCFUHSBWYWHl1g33rJ9kFDnU4N4NMiaJya5ZKEOL7kEOdVG0g9yDy4SpEX96i0XCXl-ODUFkrVHGwk-LHivogMjk-3SxtMSKQHUTq_NcqBWvR6UmpWP-5wD363VuT_4Afc_KLBCe0ilYbfqyfnev2SHNViK-OFJj5yblM5Zl9iZMCCDBqCRY41GFfovgn5rftHLAR8NsDWcnEyZx8TdI0FSs7fwOz_44-BAdcZ6dXm1EKQmog4InR1DZxDWrJRT-zFI4f86bsC8OE1nk9Tj8oDKYJ7W-4pYJC60z4w6G13SZRpyQXlgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع شهید حملۀ تروریستی زاهدان در حرم حضرت معصومه(س)
◾️
پیکر عباس آقایی از تکاوران نیروی انتظامی که در حادثۀ تروریستی زاهدان به شهادت رسید، در حرم حضرت معصومه (س) تشییع و در گلزار شهدای علی ابن جعفر(ع) قم دفن شد.
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/467719" target="_blank">📅 16:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHIduOieLOeZ_gX0J7dF0rCUNhrpr9Ue3EoBEpF_Sn4EOys4i_1bjLhvEc4_UJToAzTKuLQi9INrDkrVfgdj9yjk1uCk_0_3WEk5LFEiqQAOFcwqoA3P4LauRsH97LsfBV9qbLlqIGhHYj86AbxCbuDUu-uruehXOEBXZZVWfhxsh-dDYAM6y2SOhl1fmj7XrSrucdroCSXIKAdnbMwmDHODhP8jPkjgphkju3LILIUXmwor93gbYnR6opVC6AsS4y-PHGIybDqgSgjo_bzpr0fkU16g_XEETUexgoZJYaj1SY2txZ14vSn7UBk9xXyd7KzTVPwWWpw0s5rdP--vCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
#نکته| فقط ۲۹ درصد موتورسواران از کلاه ایمنی استفاده می‌کنند.  @Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/467718" target="_blank">📅 16:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMDNODfNjqvHLHMGh3SvFffHEKfGCl_si6cZSF_Vr5lCH18WfUFHuK_Axob85srwwBTxjup18aWbl6oeimca4M445IHkQgltE9YJGqFprQ3bEZrMI-rH9xAJqAljXK5erp4bnZq_beNkYx3ZQPS_8FQ8vX6tHVq3EzT7cSvriMGslMyhkWtKVjD4ocyG9E56WnNmtkzqmlBtDeyviHbdpl9r7xN_4ONG-hBzjq6CJC2eEjM0djJp7VbiuycudkkGRrg9uflParYWL59aGz7sBZ55Cv_cZLJkExGx-NDkjUVklmsGRF_-DJpeAiHjHo90C-2SW61D-W-2OwgEBBj4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهر تخم‌مرغ راه‌اندازی می‌شود
🔹
مدیرکل امور دامی دفتر طیور وزارت کشاورزی: پروژهٔ شهر تخم‌مرغ که یکی‌از ۵ پروژهٔ برتر دنیا در این حوزه است با هدف ایجاد خط کامل فرآوری تخم‌مرغ درحال پیگیری است.
🔹
این ابرپروژه ظرفیت پوشش ۶۰ درصد تولید کشور را دارد و اجرای آن می‌تواند علاوه‌بر توسعهٔ صنایع تبدیلی و افزایش ارزش‌افزوده، بر تنظیم بازار داخلی نیز تأثیرگذار باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/467717" target="_blank">📅 16:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSG1g8EhUqVHDl2W29On3VYmZrr9261kRFTcxQdyunk_9_qOHqqoF5AsmWCrrsS1KU-VWDGtGRxu0kn-a75Btygx1qrQNubVMnH-XcwlAiawc4PxF12BMv3ktge7s0pyWOV6Zq3-zASFpof2740qsvRsN5K3SQyYmzZ6GmP4ZoXBIRvpv3lXuB8N94PPrcrg9VZQIMvCsU66aBrjCTZFDLfhqUK1URVnVnt74WRUDOlBe7zRHF7iusDTQiEwofhvwQTtBaU4XP_vRM07O3Y1WceJUxPnVHuhlLMq8A-EkB8DRXcp5HNVYwXgoX50QmYSi4_lsTJ0ObGCzTn7sOdicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد ۶ ماهه نفت پاسارگاد به ۱۸ همت رسید؛
✅
جهش ۱۱۲ درصدی صادرات بزرگترین تولیدکننده قیر ایران
🔶
شرکت نفت پاسارگاد، از شرکت‌های تابعه هلدینگ تاپیکو در شهریور ۱۴۰۵ با صادرات بیش از ۱۱۷ هزار تن انواع قیر، رشد ۱۱۲ درصدی را نسبت به مدت مشابه سال گذشته ثبت کرد.
🔶
به گزارش مدیریت روابط عمومی، برند و مسئولیت اجتماعی تاپیکو، مجموع صادرات شرکت نفت پاسارگاد در ۶ ماهه نخست سال ۱۴۰۵ به ۲۹۸ هزار تن رسید، این در حالی است که صادرات در ماه‌های خرداد و تیر به‌دلیل مشکل در تعیین ارزش گمرکی قیر تقریباً متوقف شده بود.
🔶
همچنین صادرات بزرگترین تولیدکننده قیر ایران در مرداد و شهریور در مجموع به ۲۰۰ هزار تن رسید که این میزان نسبت به مدت مشابه سال قبل ۶۱ درصد افزایش نشان می‌دهد.
🔶
براساس تازه‌ترین آمارها، مجموع درآمد نفت پاسارگاد در نیمه نخست سال ۱۴۰۵ با رشد ۴۷ درصدی نسبت به مدت مشابه در سال قبل به حدود ۱۸ هزار میلیارد تومان رسید.
@tappico1381</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/467716" target="_blank">📅 16:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgxUoG0nNCBeCe8KM7UE7LbyhLCiIr7MmFe6ddA6wEEUAwInad2TOOUCwZ8Rz6_lvq9bnY-ZwkmlQ01QnKkGhQqoYXjmQD1JjhNxHFVclKfaRoI8yELVwIzxIZFr2sXkKuNmHSKs8ihFXrIYzwNhoPBFDjtnBVJ19Z1f5fOPJS8RfMKi3SCB0Wp164Uh1-ardKTe16Pd9q3n9RlFN_C0aaMVrDvnwL-8uybAssNXPFQ6MXmpASiViyDs_RZBAcDbvdRGnCasiSNr8W0XWl-BHE_4ChGur8vS2ICDuglWSYtF8m67p_qKkgBGsLxGYlYd6j2upj60Cug_jJj8BmlKBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
برندگان کمپین خرید کارت هدیه بانک شهر معرفی شدند
⬅️
کمپین خرید کارت هدیه بانک شهر با استقبال گسترده مخاطبان به پایان رسید و برندگان این کمپین معرفی شدند.
⬅️
به گزارش روابط عمومی بانک شهر، در این کمپین، امکان خرید کارت هدیه از طریق شعب و پیشخوان‌های شهرنت بانک و همچنین خرید کارت هدیه دیجیتال از طریق برنامک آپ برای شهروندان و مشتریان شبکه بانکی فراهم شده بود.
⬅️
در پایان این کمپین، ۱۰۰۰ جایزه نقدی ۳۰ میلیون ریالی به خریداران کارت هدیه از تمامی بسترهای حضوری و غیرحضوری بانک، ۴۰۰ جایزه نقدی ۱۰۰ میلیون ریالی و همچنین ۵ دستگاه تلفن همراه پرچمدار به خریداران کارت هدیه دیجیتال از طریق برنامک «آپ» اختصاص یافت.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/467715" target="_blank">📅 16:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/467714" target="_blank">📅 16:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f263b498ec.mp4?token=WpSl_d6UU-sI5W2yqxZ_oTfAXdRGbnDjC7B8zCzjjQvMlV7N5gAP4cYfNUjwtN7KNVI1GIaVLf_74Vfd1T_jGelE8nvN2kdOYW-CpzQSV1Lzj7OAIdo4-6oZzgsQMVtJiGrd8j2j-YWkv_GOUQYGZ-Uwr6Xur-Rrj_0vDCkLP80sN3OGBBT27YVavOtOovz2wjD11y-sLWjZvAXY5wySw89D51F7hqk54-OobDPfvT1iNThWpUGJgLNjUKZDFbzuYEhJthfZtLKSPmssv6aEl3TrYd6nl-xjbf3_LP8J8kMEn83Lyie-aZf7vETw10yO2sSh0ZZFCJdv6QuLw4QeTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f263b498ec.mp4?token=WpSl_d6UU-sI5W2yqxZ_oTfAXdRGbnDjC7B8zCzjjQvMlV7N5gAP4cYfNUjwtN7KNVI1GIaVLf_74Vfd1T_jGelE8nvN2kdOYW-CpzQSV1Lzj7OAIdo4-6oZzgsQMVtJiGrd8j2j-YWkv_GOUQYGZ-Uwr6Xur-Rrj_0vDCkLP80sN3OGBBT27YVavOtOovz2wjD11y-sLWjZvAXY5wySw89D51F7hqk54-OobDPfvT1iNThWpUGJgLNjUKZDFbzuYEhJthfZtLKSPmssv6aEl3TrYd6nl-xjbf3_LP8J8kMEn83Lyie-aZf7vETw10yO2sSh0ZZFCJdv6QuLw4QeTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ دوباره در حسرت نوبل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/467713" target="_blank">📅 16:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467712">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromانتشارات فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afJDBiIYAGsxRbYVN63Mx4Jz_TNOvVPINFGzVxsyWCatAnSvUD9zWihujyqerUr8DEYJjuysdZzGlq55GSFH6qpySXT5LZDw4_sX2vBX5GLxL8_5FFMtkTBp7PrQyz9bpSfGVbzU46UbG6PLc7_ycrQ00JVDIXVrruXDjQYNKPfUwEEXA2fboWtJn6iFIfSlVo_tVKj-nEDuUGC7L3SqMOpeikiQN1_hau0hCctt6rcLhRsv3ZQ3XzUuWyCuEsomlvRozGGJKIUuK5dAdAp2JlhB5uXFuq9QZZbnwymlzuWLMYzabDPv-OPfQenwfPcu-yktoHsizKTH-t2bTKowlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
انتشارات فارس؛ مرکز جامع کتب رسانه
، جایی برای کشف تازه‌ترین منابع دنیای رسانه و فناوری!
نزدیک به ۲ هزار عنوان از حدود ۷۰ ناشر؛ از رسانه و علوم شناختی تا هوش مصنوعی، همه در یک مقصد.
🚀
🔍
برای یادگیری، پژوهش یا پیدا کردن کتابی متفاوت، اینجا را از دست ندهید!
راه‌های تهیه کتاب:
‌
🛒
برای خرید آنلاین روی لینک کلیک کن
📱
ارسال پیامک عنوان کتاب به ۵۰۰۰۱۶۷۶
📞
تماس با ۶۶۹۷۳۹۹۶ یا ۶۶۹۷۳۷۹۴
🏢
فروشگاه حضوری: خیابان انقلاب، روبه‌روی دانشگاه تهران، مجتمع پارسا، انتشارات فارس
‌
✅
انتشارات فارس مرکز جامع کتب رسانه</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/467712" target="_blank">📅 16:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467711">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcOqddvGfCpkAYxkAep4pOTvWbT2bziaun-ZIeDXOzUzf9EarT7o-FV7DwIj0r5ugLblBgFnU5wqLIbdt2scbPzX-_zu3s1HAka63G9OWQDxvf-Ac06ZHowC8GbQG1khwTOA2BIZsJis9W1gBLbS_wxiaH8mG182fWh1knGUHvpmQWEXUaDXqDASV40a95mPYA0anSY_i1M6sY0GWS1gZKRsLCKCIOgCHtoi51Np0sdXxNP50Q-R_F3-6ZpK9PKzE2C4bizgiVp5xURf7qecNzNYS-24yOBkSlrthcDGOGASDQstJVrxGnkuUCcWuq5pUTleWoMhw022To9ALy8J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عیادت نمایندگان رهبر انقلاب از آیت‌الله نوری همدانی
🔹
حجج‌اسلام والمسلمین رحیمیان، محمدی عراقی، محمدیان و حاج علی‌اکبری، بعدازظهر امروز با حضور در یکی از بیمارستان‌های تهران، ضمن ابلاغ سلام رهبر انقلاب به آیت‌الله نوری همدانی، از مراجع عظام تقلید، در جریان…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/467711" target="_blank">📅 15:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467710">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732a21f86a.mp4?token=KD2YPmvq1orXpptcAfGR2d28rYsYLF2Yx9OI4bEPYueS6nSAeVs5ISNeooH-SSGrq34C9ixpbIwfLZCRU-kM5iDKhYJOBy96rZ-EGMDH7UIa76DJjqV1GS8F6UIrc1C8VpMVjVRmTdkKDJAzp64God8B--S7fdHb4L2byyfnlFcULPPDh-B1yRaYb0TtGQb5A_6rMnS3mBvD67teJDn_wH7GZPKDWqWureQmLcVLS5jRN3-VbOS1A1rSUn-9Kwg_nJmkttbz6rKcgmA7IB_8WxvRW90eyMv5av00fcqRvZFVMR1C8ZnXEfdLXAJ4MqH4QaZsKeMYnUYadFsZNZW0ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732a21f86a.mp4?token=KD2YPmvq1orXpptcAfGR2d28rYsYLF2Yx9OI4bEPYueS6nSAeVs5ISNeooH-SSGrq34C9ixpbIwfLZCRU-kM5iDKhYJOBy96rZ-EGMDH7UIa76DJjqV1GS8F6UIrc1C8VpMVjVRmTdkKDJAzp64God8B--S7fdHb4L2byyfnlFcULPPDh-B1yRaYb0TtGQb5A_6rMnS3mBvD67teJDn_wH7GZPKDWqWureQmLcVLS5jRN3-VbOS1A1rSUn-9Kwg_nJmkttbz6rKcgmA7IB_8WxvRW90eyMv5av00fcqRvZFVMR1C8ZnXEfdLXAJ4MqH4QaZsKeMYnUYadFsZNZW0ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور کم‌نظیر مردم بیرجند در اجتماع بزرگ «جان‌فدایان ایران»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/467710" target="_blank">📅 15:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467708">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jr5RMyfCD0NN3KdUsxiEJF2oFGbEEKEoQg69NW5YhoxwZdgKcBIqOzbmON3ji99NkLOPoemzDHoIy82-h7NukZlFUv41Ti7-XRqGZi0FRJdALgJMAE1b4xisBDApqIuGnc2m0mhbh8obsWk3pxEKRsNaZMLDasI5PRrwfy_iQak2B1ET2eM5qerZDvpmfK1XQEAhi5OAm2S2N2OrDs7P1sFOj-uttq1wCoRABoel-CpHdN1K86n3RTv6cU0SB7z5Cdr5qd0Xl-hP34tSXK9bAf1DB_B5E08ixH6gKH1EJy-CH61xwXTfbVMvHVz3f8YUQ6ZWJsHIKkC-Q1CQahbgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3a90c45.mp4?token=G37ipfaYc1SIa9__bXQPJc7Bv8RdMG_kXcEUGi9O2Q7mjnsQ_MZrfap9xdUbnRowNc7GCvCZeR0QQxKz_sgUKav-_fIh1XdJu-CcFW48-RxWBweAN_FYv-5nvFcRzxwT4IdlNLKOifRmNwDoJKMaW56gKni4Hk0zybR2MA9bCHKZYoFMViTzDnR50NcWrXE34MxSu5M9q3RMOsd-6Gsw-TMguiG1uCr8J9UcMiMEJP48HyT-SsGVWPzb6JkGqXIDAoEy8nc4PqelSEK-wB4W2-stIO3LflA1UuJoHqpwRfPpEEjtzltg8dzZw7DzkNikYoJF6sNOqNJ5tXl0n7hL6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3a90c45.mp4?token=G37ipfaYc1SIa9__bXQPJc7Bv8RdMG_kXcEUGi9O2Q7mjnsQ_MZrfap9xdUbnRowNc7GCvCZeR0QQxKz_sgUKav-_fIh1XdJu-CcFW48-RxWBweAN_FYv-5nvFcRzxwT4IdlNLKOifRmNwDoJKMaW56gKni4Hk0zybR2MA9bCHKZYoFMViTzDnR50NcWrXE34MxSu5M9q3RMOsd-6Gsw-TMguiG1uCr8J9UcMiMEJP48HyT-SsGVWPzb6JkGqXIDAoEy8nc4PqelSEK-wB4W2-stIO3LflA1UuJoHqpwRfPpEEjtzltg8dzZw7DzkNikYoJF6sNOqNJ5tXl0n7hL6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع خبری از آتش‌سوزی یک کشتی در مسیر جنوبی تنگهٔ هرمز بر اثر اصابت یک پرتابه خبر دادند.
🔹
برخی ماهواره‌های حرارتی هم یک آتش‌سوزی بزرگ در این منطقه را ثبت کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/467708" target="_blank">📅 15:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467707">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b0995a8f.mp4?token=R_gzwzOdeW-3FHaWJOIFLgKFhRu38PW9HUPn_cIht7VyHNkPyqs8ol-Xu_9zLUckC6PBKQF4Wso-R70p5FlxXY0lZs2_yQosdp4F3GT4vdXYlxWZ_aBh0hdcdjdI_z2Nr_sCOIOblWKCc7ejYfsvNKSLo44VvdQWU98CbfRkTZcD9-KweejlMlZXlRoeU647j7s2z0hvjJ2BQm5e6FKhaio-hDEtp8I2DWyLzBkjTFpZ10M2gELk2GYm9jMYvY1j8MKVJ_8-1UXlcKf_fM4A5oNc9pZJwZblBTAYzeWDs7yHmCUTBkMVhyahhWaJ3GYvv_U9lp48mZ4-dK_g-PnMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b0995a8f.mp4?token=R_gzwzOdeW-3FHaWJOIFLgKFhRu38PW9HUPn_cIht7VyHNkPyqs8ol-Xu_9zLUckC6PBKQF4Wso-R70p5FlxXY0lZs2_yQosdp4F3GT4vdXYlxWZ_aBh0hdcdjdI_z2Nr_sCOIOblWKCc7ejYfsvNKSLo44VvdQWU98CbfRkTZcD9-KweejlMlZXlRoeU647j7s2z0hvjJ2BQm5e6FKhaio-hDEtp8I2DWyLzBkjTFpZ10M2gELk2GYm9jMYvY1j8MKVJ_8-1UXlcKf_fM4A5oNc9pZJwZblBTAYzeWDs7yHmCUTBkMVhyahhWaJ3GYvv_U9lp48mZ4-dK_g-PnMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استانداری گلستان: براثر سیل در مینودشت، مسیر ۱۴ روستا همچنان مسدود و برق ۱۹ روستا قطع است
🔹
مسیر گنبدکاووس به کلاله همچنان مسدود است. یک نفر فوت کرده و ۲ نفر مفقود شدند. @Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/467707" target="_blank">📅 15:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467706">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">علت فوت امید قانونی در خوانسار مشخص شد
🔹
رئیس‌ دادگستری اصفهان: امید قانونی در ۱۳ مهر حین توزیع و فروش مواد مخدر در روستای ارجنک خوانسار بازداشت شد.
🔹
این متهم ۲ روز بعد پس‌از انتقال به بازداشتگاه، ناگهان دچار ناراحتی معده و بیهوش شد که پس‌از اعزام به بیمارستان خوانسار، متأسفانه فوت کرد.
🔹
گزارش‌های اولیهٔ پزشکی قانونی حاکی از وجود بسته‌های مواد مخدر در معدهٔ متهم بوده است.
🔸
روز گذشته رسانه‌های ضدانقلاب مدعی فوت او در هنگام بازجویی شدند؛ این رسانه‌ها مدعی شدند علت بازداشت او نیز درگیری با نیرروهای بسیج بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/467706" target="_blank">📅 15:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467705">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524a2e3d5.mp4?token=AD8EFrkZEhpBHI8rsTIa2EE3w75smY05B1pPyJKFIAnYauwVGhe7g2c-6mMFgIOQBSKcWh_cneTtKsrPe2UzrxF9MNnkIeVexxbzT--IYyD88SksEkMVPMLH4ylc-L7ayxzInU3z6zQ1iQHrBYHqDSb6X3-5plmhXu9hXXmy4t5uI29dg7E6ufx4P3XzmZcJZINRMMjM8QFLf9DUiryyokFa0pR7sqYXlAcmXuqAA9yniiJhfJIIUnyIGNh-gTSd6BEx8bg_gA-7wK7UVjQi_GBMLzCkDK6Q1VetRr4gZT-TvaiFlcGjrUt-218CrtQLjAKGLnVubY_rtcRRQDiTAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524a2e3d5.mp4?token=AD8EFrkZEhpBHI8rsTIa2EE3w75smY05B1pPyJKFIAnYauwVGhe7g2c-6mMFgIOQBSKcWh_cneTtKsrPe2UzrxF9MNnkIeVexxbzT--IYyD88SksEkMVPMLH4ylc-L7ayxzInU3z6zQ1iQHrBYHqDSb6X3-5plmhXu9hXXmy4t5uI29dg7E6ufx4P3XzmZcJZINRMMjM8QFLf9DUiryyokFa0pR7sqYXlAcmXuqAA9yniiJhfJIIUnyIGNh-gTSd6BEx8bg_gA-7wK7UVjQi_GBMLzCkDK6Q1VetRr4gZT-TvaiFlcGjrUt-218CrtQLjAKGLnVubY_rtcRRQDiTAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کوله‌پشتی خونین آدرینا به رئیس‌جمهور رسید
🔹
فرامرز پگاه، پدر دانش‌آموز شهید آدرینا پگاه، از شهدای مدرسۀ میناب، در اقدامی نمادین و در قدردانی از مواضع قاطع رئیس‌جمهور در سازمان ملل، تنها یادگار باقی‌مانده از دختر هفت‌ساله‌اش، کوله‌پشتی آغشته به خون او را به پزشکیان تقدیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/467705" target="_blank">📅 15:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467704">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3UME_qwO8hdUXutrj1vCXcPSHy333Tx7RPO7Oy5goY6D_gjAWvpT6zHcBY0-pmKFSYSCq15TPzrYtOtT-t5yHME90ZaD5NhJbPgMnsayOUn700FvTyUGUg98eyL2I-k_lFkQj91ET3ozBpp8hO1tMyaiCm9gJ1LL2dkZvUGcRQPInSi0GamwbXMr99-Eo9gYqrloymIzokgKPR51Ix-vS0ohJ3htV1q0cqwYFRacf3mBewivAB4LF-KWq43jFZU8o834OnyV7kN9MrIEnL6GYotXYhVCrKO4O1usZb0MnEXEsAIH03Ze7Cs96-ETL_Yjb5Ux6p5liY69WeYvofTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۵ ریشتر در عمق ۲۰ کیلومتری، سرپل‌ذهاب کرمانشاه را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/467704" target="_blank">📅 15:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467703">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f1f7fd598.mp4?token=BISx9au7S396OpPek1G55Me5AnrbO1Kp4jCL1PLJRhsJK6_w_JK-KEKtv_nogGMNSLlxtuDBkBbFSW_YPyH7RWNM8mt2z6idi9MzguLrXzVlIleIExhL3jrESOE2ySwfRH2W-77mMZZ3MsPDzbcKKdvLCUGaL3D30AU7URPktoCKcyrnFEsOUv616969wwNagRF8tQnR2MGUbUPlY5p-062PtY2bgJO7cai37jFx3dDJwyUCeT9xYvLxHC9zJtZjFGC_h1V9kBcfXdqGmsmXfu1TxUM_e0uPYRM_q8qBd1bPO3fshz_PIBxWGtDa_jxZBMiHrjRZvotqFKiTfMHF7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f1f7fd598.mp4?token=BISx9au7S396OpPek1G55Me5AnrbO1Kp4jCL1PLJRhsJK6_w_JK-KEKtv_nogGMNSLlxtuDBkBbFSW_YPyH7RWNM8mt2z6idi9MzguLrXzVlIleIExhL3jrESOE2ySwfRH2W-77mMZZ3MsPDzbcKKdvLCUGaL3D30AU7URPktoCKcyrnFEsOUv616969wwNagRF8tQnR2MGUbUPlY5p-062PtY2bgJO7cai37jFx3dDJwyUCeT9xYvLxHC9zJtZjFGC_h1V9kBcfXdqGmsmXfu1TxUM_e0uPYRM_q8qBd1bPO3fshz_PIBxWGtDa_jxZBMiHrjRZvotqFKiTfMHF7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارندگی‌ها همچنان در سواحل جنوبی دریای خزر و شمالی‌شرقی کشور ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/467703" target="_blank">📅 15:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467702">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd9dcbb0f2.mp4?token=m13hi4_sCTkn3GCAJuQ8U3AcIz5N0Bc6Ax5P2sJiE-F2a1J_lAHOsMQCfx05gUyn3Qko-XCc1AhC61Ys61XxVnxxsU0qknkRpTnSs-Hu80WXp5wqyJ_ZSVsnTqTmi1scoV9b9_BluiA2rhRZ3_L8zpiXVuy47eCtIjrkSgYPFptdhM0DF-k8f4MIWcI1nCUQ6PIAotphlxjL-TKb00u7_U-rrwBbC12kcxcqcTu_m6SDFpnXltuqMC99BQVtzCgbsS73XaHtDGT3xbWTj9HcW12oOHMKt_vgxfeApfHBeibvqu4LiCBYNC8NJnSISYB1oLJ6KkcL3-Mn2xl1nlLwcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd9dcbb0f2.mp4?token=m13hi4_sCTkn3GCAJuQ8U3AcIz5N0Bc6Ax5P2sJiE-F2a1J_lAHOsMQCfx05gUyn3Qko-XCc1AhC61Ys61XxVnxxsU0qknkRpTnSs-Hu80WXp5wqyJ_ZSVsnTqTmi1scoV9b9_BluiA2rhRZ3_L8zpiXVuy47eCtIjrkSgYPFptdhM0DF-k8f4MIWcI1nCUQ6PIAotphlxjL-TKb00u7_U-rrwBbC12kcxcqcTu_m6SDFpnXltuqMC99BQVtzCgbsS73XaHtDGT3xbWTj9HcW12oOHMKt_vgxfeApfHBeibvqu4LiCBYNC8NJnSISYB1oLJ6KkcL3-Mn2xl1nlLwcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوپرنفتکش متخلف در تنگۀ هرمز درحال سوختن است  @Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/467702" target="_blank">📅 15:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467701">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1xixvxceK6F0J3v0OA5cpPrKm2CNx0MMu0wOM25UT49Df75LtW413VROD0Q5iSwLVdmomT8-V19eGBNT2LwTPCUezDyN-rVzGnP5Rc5sOaOdepDVMV2-8yUPxiRRLhhU1G9TMKUD2Z0BRoOmQF6SK9gQaKi_iLFgDa0TKO_WH1DadKoNa6PD5b5OxXu5PGjWuo5zx828iGzVR7M_YlzETKPcXGZc0feDLmqFVn8mBh1hna3YBE0Uq4QlOXzPg3MG5yyC15qiaaRmlnYFsYUvP_QQqG7DJeS0hG-FX8aJwRAUVXQt-GWyGmVJhYtx3dmGLa01eYjPOsHgxOyB5FKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تحلیلگر بین‌الملل نفتی: مجوز واشنگتن به روسیه یعنی تنگهٔ هرمز به این زودی‌ها باز نمی‌شود
🔹
ردیابی محموله‌های دریایی توسط هوش مصنوعی ویندوارد نشان می‌دهد که احتمالا نخستین محمولهٔ گازوئیل روسیه که به‌سمت ساحل شرقی آمریکا حرکت می‌کند تا ۷۲ ساعت دیگر به مقصد…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/467701" target="_blank">📅 14:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467700">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOtB6MKZQ5h2FEF9tH0rjrQ0iPtWzWwiO9i81i5aEbDbwBBOWntU7z2xELiU2pGN7VR0crFjiDXWqW_pq2YsMk_rGHhKrniYf4tSAupqHudKA7FwNs9xyEp0JGjBN19RsLGfGPCYiUoLm1MAf_KCTWhF4j-6B1Ivs1PSpe0pW-Rd2-dMJchzrt-9PY_gEfyiwj7CoZ6oa1g9uO7heUTfMO1UplUs3VxFqJqDGcUTjQ7VHV139vydKj8itkVwCR-Ctrh2M7iNxVukxfY0ouPAW6It_-dObakDDS6b44ohgDRLF7KUj5689S5teBzVoDaOzPXBerQg-BeQQR4PWgJ9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار مجدد یمن به فرودگاه‌ها و حریم هوایی عربستان
🔹
سخنگوی نیروهای مسلح یمن با هشدار دربارهٔ استفاده از فرودگاه‌ها و حریم هوایی عربستان اعلام کرد: این مناطق به‌استثنای فرودگاه‌های مکه و مدینه در معرض هدف‌قرارگرفتن و صحنهٔ عملیات نیروهای یمنی هستند.
🔹
سرتیپ…</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/467700" target="_blank">📅 14:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467699">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268bcae3d8.mp4?token=fzkAfGNfyKj8sJ8FoJZ9I-FJxoNQiqi8viOPDYaitR4hz7hXN0KuH-ibXyldI5GLbfvGPLG-vM9gemRZIaua7sEahdAcOds2OVfWAUJ5YnyhoLuKeEPcd59PUfw1SbDa3elbX-n9du0ca3huuLE6WIzYEzo2wzWwzSFLAxSeIwopuaNV4HwaIVEdURuwiuJwykR8xstHEwb11JED7KFloNy2u1jOfmE9MJAPQ2gAIWM4dX1jDM7CzJHL9MQ9e3n391qI-Re3GeWW8HjNG8j9W5DhvYmQu5DUlxnKkb0I6l60UcAaWuB-hBRY82cjeMIDVcY5zmXM6cHy-i_z7fgDwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268bcae3d8.mp4?token=fzkAfGNfyKj8sJ8FoJZ9I-FJxoNQiqi8viOPDYaitR4hz7hXN0KuH-ibXyldI5GLbfvGPLG-vM9gemRZIaua7sEahdAcOds2OVfWAUJ5YnyhoLuKeEPcd59PUfw1SbDa3elbX-n9du0ca3huuLE6WIzYEzo2wzWwzSFLAxSeIwopuaNV4HwaIVEdURuwiuJwykR8xstHEwb11JED7KFloNy2u1jOfmE9MJAPQ2gAIWM4dX1jDM7CzJHL9MQ9e3n391qI-Re3GeWW8HjNG8j9W5DhvYmQu5DUlxnKkb0I6l60UcAaWuB-hBRY82cjeMIDVcY5zmXM6cHy-i_z7fgDwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار نخبگان و مشاهیر تهران با رئیس‌جمهور
🔹
پزشکیان: قدرت را در خدمت به مردم می‌دانیم، نه در زورگویی. نام‌آوران و نخبگان با قدرت بمانند و کشورشان را بسازند.
🔹
وظیفۀ ماست که تلاش مدال‌آوران را که در عرصۀ جهانی پرچم کشورمان را به اهتزاز درآورده‌اند، بی‌پاسخ…</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/467699" target="_blank">📅 14:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467692">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEUUlLYd8vH-Rcw2KV_GxhK1DQppkRuT0-dOkTLPiEuyI6IzJ3EaLeGZ6iFvDZT4cp0yxGtJ2p-R_BhMA5_lX3cdoSaCKwmRDGMl85kZ5dnsXh7XOkUCIUiXUc_C23YAwcEsO7PX3k5-9F2RL_Ke3qmFFlD1V-mT_xjGSmBsfzi74gSeSwn7IWsZjjWRBURvL75Oihvg4DaDvj_1_V2j36KoJWM8jBVyRqrv14aywqCGeyTjYaVumtoMblK0G5kI3Das6saXf6kItQ3I1rMVn0Xqf-CmmooefxUFGJrmFryaYg7neCUrrB5ECPQCOBoOtq5Sb6ubRBJNZ_wEjwKCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3gSVFx6MN8O9x3_GpcurolPaJCMz6kcwnyPtUHhJWblVLU2dmbkAAra_KtIjhBJSzr8TaZoE59j8uihlSm739SMLlPzNJgBwzzBdp1kMt2Go1x-nPEJ8RqWd6ZEEcGETmhwWOh1_K3i9782g-u4JOSKeLIbGPt1WmJXhN0_Z4BsLnHzlHzpJa6yeHg7mRsBKfG_JBL1X7G8FfOb8Se4U1oD75iCjtPVFkljuAPNl9Gv8sqRLqaj0zwGOOHrK0DBbZYGP3mFqXnPH3rECCAopppr--_eH59uNk_8tSs69otzf_wTS8OCcYj30CnKZJxfJ8gUzebGM4b_uN73YW1tpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agZbbQiVfWzcBscOckbyesZFnUUODwE0tchX9HVgUUPYRndcK2K9I6ht9gOz7nRFN41wh6JOuH9-9OLDsIj40nuo_VOHPrQ3ibENi8OjpxfKZnSfv3vVUU1PkDhEHgVAgbwXG03Gxngr2FR-gWbIkVKLuOpOXhg8RYKL8fhFqjaGVSyYjkov0_qjGrTliVXiaTmN137suuLxQb4fFVtcBCprktJM3WZKB24V2p5jRfri6elYfmFOHHZvE4-qGdrGZNekwXEkYBfaV2TK9GpbmkcBCLk7i6FJMF7LhdVAPRj0pC2-SicKAI_ZukMFZ0lJAJl9rSzMFuipRC0fnx3_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHY_Gp1SvkC669y5y0qnoxLAfdTss5cyO58UQ1AAHUpgJ1JVcSgOalbkkIg3Oe7uoDRFLZ2y74C9-nmDJkEZryIW1FIaamUys3jSn6pipwZHYl-JjAnEJ7IBQJENq27YkQSNj41z-Hp0V94lGnoS_V7RkP1_8ftGAxOWqZDKPPGzH0xUMJst05fZ2oay7w0GfXHhqftUKkm-XYlxyMwTuM0KkASdok6iMoj4AhKMJcIQWXqHHYxRF-K7WHgfrGz-GJkoihh72EGhI1kJ01NTz0msOfmP4yoBFDjB7WEU3KGpDuRamcQldcfscGSQu-QuEBrCZQFOU-a2enmy3qzqhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2HplVJUCSnK-cmWVo4jmmvXKHi_axHfR6MCMok6xSTqjWJqxF7z-8yRFEcL4BSB6HS_d2Nu4_CV1F5udkx3A60e-JZPDhiXZe6MDd-QzAl8vR6KlbaZtp6n08fc5XI5b0IQ6rO89_688k-uGsTUiFpcJ2s3tpvAYKnpEgjG3AKtWOG8KkJadnakzJH6qgE3SADw_p5sh5QKtGEQ2PYugwfH-AH5757iAm7of00s6A7Ie-nzBWedc83BiY9N9ODAuJsdJlzImAkev_ODO776nWjM9aUHqbqZNOuUxBeAQC4roC7yGvuQsjVVDGgbgedl0Y4gB4sxQIqrjq0Egw7pLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGJGW5O7tW-ph0UAIIqMdiVentfPXmhYH2cCjh3CGE_YkzjACqTA9MBSjiULJy4ZtE1xiOH1dgjjk3ST70eD86PXtSgH7wbLeXaSb6n9rvWqIGWcli02Fr_GacU9azTqTSBivhfm6OC2Xgzc47MoUiFn67Taw7C2WUG4kwp9euKuoue-P7m6Jplp_R9dHn_dvGyVQZrpbS88feXP7gwcb0995lIKwmU6CvfNYPUMpp4GJoh7eVKok-daN8GGO3BhCWgsgdRnBBMxvAzfc4M4_YYcZMqxv90bZFzdJ1NKvh7dnbu_uccZ-eGxW-yh-6PrIuoXqcVHOZENSAVegEXiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCzi9mBQLYSo1OWJvPyB89oKMe3XRCrhusXefQ04rJHA5MD1h8EKckbr-LUqeXXJ9zBWgj7I0slQOQtIaTE0qg4EykBoxOyVB3iOwUkVeIqtCWt-Kjhgiwp4BD8uGob9tM27U-bs4LxWv_9aKAfef-IlppiZ1rt2T8bapCohKms4Hh1-nyLsvj2dEbkC5WDkpKITgCTwaOxztuEAifwS400eowReM1tGVB8qnXVJSo4Bu59J4yUKhAdCD6rOYq3TXJzKpblHvaOkLiX4UcuFYu2DYIE2YCg7tGVKaiXs9vdQFwmXw98v0CvsKsQdA9ygLiiCit1K6-tVhCt9Nf8AEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
همایش اکوساید؛ جنایت جنگی خاموش
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/467692" target="_blank">📅 14:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467691">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd521070c.mp4?token=aQXvT95PsjKvsc2fOs-QPq5QhTSrnnwRHK6HCYIP8O_coyESGRLxKefmR0zef7vbqJrs8QJ1pT-vhixOklL4Ym9wlSkSZYnpwSAFVnbXtmY-JCdfEvQ0dQLlN4lHVFPbLMxUyGhqmHjESrNagqg86z9yqVPO9Lm9jdw2bmF-yqlrXAbkbIVX_Sppr0k48JiLR-6EN5pfdlzuuBQjUsNG4tb4KYBl-RDxF9h2EjZT1a7tW5ZKC5YY0_8W25g9n4jHAy01SBwAw8f-wGHGoGVHPjdNg0zxM4LSY0YF7Lh3C5H50iYzU5Lz5JfsRhwtNWh9YWa_SwgK5SFRqwH8BYTCtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd521070c.mp4?token=aQXvT95PsjKvsc2fOs-QPq5QhTSrnnwRHK6HCYIP8O_coyESGRLxKefmR0zef7vbqJrs8QJ1pT-vhixOklL4Ym9wlSkSZYnpwSAFVnbXtmY-JCdfEvQ0dQLlN4lHVFPbLMxUyGhqmHjESrNagqg86z9yqVPO9Lm9jdw2bmF-yqlrXAbkbIVX_Sppr0k48JiLR-6EN5pfdlzuuBQjUsNG4tb4KYBl-RDxF9h2EjZT1a7tW5ZKC5YY0_8W25g9n4jHAy01SBwAw8f-wGHGoGVHPjdNg0zxM4LSY0YF7Lh3C5H50iYzU5Lz5JfsRhwtNWh9YWa_SwgK5SFRqwH8BYTCtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی: بانوان پرچم‌داران نبرد فرهنگی با غرب هستند
.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/467691" target="_blank">📅 14:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467690">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b9c41785.mp4?token=FNrhrCL10rcQJEbGn6OqKZQzJlL46XzkkW55YhmMFumIGWUvuU7WBNG0nwtinv-rS2pBRG3Pf2EVnNJrVW-jbJXtfgluW58o1gfXhOvjWUcuz6oaK7BZGblUzjKNPG43ZyCG_-47hX46Pkj8ZkokSTMybUjHxx_a1WaaFiT1oQ7_R42Seev485orLMq9aN_61DeEktwyQS9Mdj322i20rh7Pt-CRnkMrtvZw_kz4qez7MF1VFY78jD5Brfh2aoQCrngmWls4_IeyKOciqfB-VveTP-l8WA9-N7VkoCbSsjyRpY1YKEbyosTXkcK6rzSadFYwtIQ4V9HlAm3tIRK7UkBJfridrfLXZC72lTW1McVQ364ZgrspavoETOZ_KyEhj8KdTib_zGC-CPtqWtW8VU53cjSNp8UOd3IDs7cGwnJhKip4luHv8jI9UEf45KsxPpiV-dgpspac7IHiuQv-VUVUV9Is5PsChelmj4Z_iGuefZSiA2fS9haJCWXFcGEITLlyumKcHPAopRnTYLha6p-BgLBRodrd7oHQdUv6Y6EcoGQhKhb2vpKde7y2IAW0dWRLwb1k4yQhSE7SYfzL61fLgWGtSZ-pH_SayeXDlGZpNjrse-QHlEzbDVEVv5TV-5oBrfCqFNX44Dfhz04xP6hDuJRaWQ_KtTiQjL6ESK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b9c41785.mp4?token=FNrhrCL10rcQJEbGn6OqKZQzJlL46XzkkW55YhmMFumIGWUvuU7WBNG0nwtinv-rS2pBRG3Pf2EVnNJrVW-jbJXtfgluW58o1gfXhOvjWUcuz6oaK7BZGblUzjKNPG43ZyCG_-47hX46Pkj8ZkokSTMybUjHxx_a1WaaFiT1oQ7_R42Seev485orLMq9aN_61DeEktwyQS9Mdj322i20rh7Pt-CRnkMrtvZw_kz4qez7MF1VFY78jD5Brfh2aoQCrngmWls4_IeyKOciqfB-VveTP-l8WA9-N7VkoCbSsjyRpY1YKEbyosTXkcK6rzSadFYwtIQ4V9HlAm3tIRK7UkBJfridrfLXZC72lTW1McVQ364ZgrspavoETOZ_KyEhj8KdTib_zGC-CPtqWtW8VU53cjSNp8UOd3IDs7cGwnJhKip4luHv8jI9UEf45KsxPpiV-dgpspac7IHiuQv-VUVUV9Is5PsChelmj4Z_iGuefZSiA2fS9haJCWXFcGEITLlyumKcHPAopRnTYLha6p-BgLBRodrd7oHQdUv6Y6EcoGQhKhb2vpKde7y2IAW0dWRLwb1k4yQhSE7SYfzL61fLgWGtSZ-pH_SayeXDlGZpNjrse-QHlEzbDVEVv5TV-5oBrfCqFNX44Dfhz04xP6hDuJRaWQ_KtTiQjL6ESK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ تعطیلی فرودگاه ریاض ۲۴ ساعت دیگر تمدید شد
🔹
وبگاه «فلایت رادار» اعلام کرد که تعطیلی فرودگاه بین‌المللی ملک خالد در ریاض برای ۲۴ ساعت دیگر تمدید شده و این فرودگاه تا ساعت ۰۰:۳۰ بامداد فردا به‌وقت تهران بسته خواهد ماند. @Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/467690" target="_blank">📅 14:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467689">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3191d92d8.mp4?token=CVMX4S2B6H4d-E7id4rSDHbWCQpC6abOteHtiO-GLPTCEkmz92afAH4EHY-N9fWpcneJ7yulZo3RuIk2VsrRoMWzyskMosxmFKFzdD2jMTvlBrgUFPj6aE0Ccvu4_WDvGGU61eWXI4o7riE3Jtpc3t9LpYBa1PNanD4gmkPqD93izeFraR5GUrfsxK3X-KiD8q9pnP1Qv7McIZ1AVvFzVOKsEYh-klASdVd2fhC42DujXwKb9CGh4SJNnUrOR22eyXTgwKBl5E_y1PMQSZWo1aDife0oxiKm-vYCUQYYsjYZlYzvLrlsu_spOLGh-t1RY10Ibn-vMAfb_uXbd-PfDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3191d92d8.mp4?token=CVMX4S2B6H4d-E7id4rSDHbWCQpC6abOteHtiO-GLPTCEkmz92afAH4EHY-N9fWpcneJ7yulZo3RuIk2VsrRoMWzyskMosxmFKFzdD2jMTvlBrgUFPj6aE0Ccvu4_WDvGGU61eWXI4o7riE3Jtpc3t9LpYBa1PNanD4gmkPqD93izeFraR5GUrfsxK3X-KiD8q9pnP1Qv7McIZ1AVvFzVOKsEYh-klASdVd2fhC42DujXwKb9CGh4SJNnUrOR22eyXTgwKBl5E_y1PMQSZWo1aDife0oxiKm-vYCUQYYsjYZlYzvLrlsu_spOLGh-t1RY10Ibn-vMAfb_uXbd-PfDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی، معاون وزیر خارجه، در بازدید از مدرسهٔ میناب: درحال تشکیل پرونده‌های قابل‌پیگیری در محاکم خارجی هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/467689" target="_blank">📅 14:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467688">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab715d3df2.mp4?token=fKCMetIVO-3E0y6WCk6v9_nVAWjH8wfmfy52a5qFHj7X9lC1T8K-SLwuBOrjDrPxY55d7rTrPYR8qK0SYg7-IaCThxyONCs_IOyNtnC5y8aTotULAVHC7C7cxlCQbbV6ckpGgiN9Y22VItSNVFadL2LjEzA2ZWyEO-pxS_uRoG9XgYPb36BCiIwTIr3vJHWmryLs-YHaTVYzqKfakaFj2fYC9_yB7wdGNK-qRoBBC9FoeAryMTq1mTE6nPF9iwZdJSgUoG_AgeKqpaezkgUvyGVKI6npIOJe61u_I3PN9qXr6UuuHSKBEj_VcsOWzgnT0iXqBK3YjRFw8DwQKNBHRK8K8Lr3MJKgTMISZBNQTErHY_UaFK0boKy68ZL2AlTENzynO4yjECUQhVeInz0UpiFSHdB-mM8UJ8aCL5jnvbJC4mx1loGWmwOz6XVXCf1jfKHGz03zq69Tn4j8PXX12ygJ1D8LsOXD7Bna_1UurfEEPoJ3Lz_dPHjeyy2wowYBgmM38qSl3UaYvEinMsMzoPdGSAsWomt0T5in8_d296ryIv7u6OghZ2edglhMbdz5DkAqyZsBfjUwfwPlTnwysQkLg0GPttxvMxwRZbwQTsdniLvJxTILOoF6lft6U3y4F9KnyL0TF36fwJm-BfGLTVFKxdI8VoL9XHoBQNoxgug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab715d3df2.mp4?token=fKCMetIVO-3E0y6WCk6v9_nVAWjH8wfmfy52a5qFHj7X9lC1T8K-SLwuBOrjDrPxY55d7rTrPYR8qK0SYg7-IaCThxyONCs_IOyNtnC5y8aTotULAVHC7C7cxlCQbbV6ckpGgiN9Y22VItSNVFadL2LjEzA2ZWyEO-pxS_uRoG9XgYPb36BCiIwTIr3vJHWmryLs-YHaTVYzqKfakaFj2fYC9_yB7wdGNK-qRoBBC9FoeAryMTq1mTE6nPF9iwZdJSgUoG_AgeKqpaezkgUvyGVKI6npIOJe61u_I3PN9qXr6UuuHSKBEj_VcsOWzgnT0iXqBK3YjRFw8DwQKNBHRK8K8Lr3MJKgTMISZBNQTErHY_UaFK0boKy68ZL2AlTENzynO4yjECUQhVeInz0UpiFSHdB-mM8UJ8aCL5jnvbJC4mx1loGWmwOz6XVXCf1jfKHGz03zq69Tn4j8PXX12ygJ1D8LsOXD7Bna_1UurfEEPoJ3Lz_dPHjeyy2wowYBgmM38qSl3UaYvEinMsMzoPdGSAsWomt0T5in8_d296ryIv7u6OghZ2edglhMbdz5DkAqyZsBfjUwfwPlTnwysQkLg0GPttxvMxwRZbwQTsdniLvJxTILOoF6lft6U3y4F9KnyL0TF36fwJm-BfGLTVFKxdI8VoL9XHoBQNoxgug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم خطاب به وزیر خزانه‌داری آمریکا: قدمت آفتابه‌هایمان هم از تمدن شما بیشتر است.
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/467688" target="_blank">📅 14:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467687">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC4j5NMmSNIUyRETVVU1bXO_jPQhUx9rgjchZHwvhcyJp_EkrpNJcKvL_Rq37JaimmZ7q9V_o6ylRkzPOLKymDDaTnuqs1tYRvNjV44NktFTiNS0WloZUBZTz98cFEr-PuDe1QvRqErAENLvSqRf8FjGEhZF7GMjHaT1XjwX-YT5G-fEYU24vbNq79qtOfi5C6M3-hXQ2jwjqTpypX80goToFiU_9oxUGjYyaN4CDHFmdgJpQmo0gFu-wJNXSUSPWYJjEOd6CbYZOfQbIJiGH2hqiCgIfhX2pNcUpB38RsvJCqgobX2ieoeb3Mvw-SZEZrVY-nrrbi57Qyto0t9bOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غرق‌شدن قایق مهاجران در جیبوتی دست‌کم ۱۰۹ کشته به‌جا گذاشت
🔹
در پی غرق‌شدن یک قایق در سواحل جیبوتی، دست‌کم ۱۰۹ مهاجر از جمله ۱۵ کودک جان باختند و حدود ۱۱۶ نفر دیگر مفقود شدند. این قایق حامل ۳۵۰ نفر بود که تاکنون ۸۰ نفر از آن‌ها نجات یافته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/467687" target="_blank">📅 14:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467686">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTRFwYdXDDvoAUBC-qOk98RMXUHyJIrWqspCtCVgCIKx1AvVLyXPY4NGrBxoLMXi0Z3AT0pQIr3uEKgSwJnYSntCQ9FrfQrAWz8G3YanJkAidovakc2nT74EWmc2NchXgwlbF5qWalMjGO-q0kYUI47Bcp89VpID4MIV4yPTsLGEVxBhLWTs_NyLRPbbSRh4hQq1gfpXLg8-68otvSKWDFvZS5UaObII01-UUTplQefIP-6kE4hJq7uE8zBLTouhuyPyAH-I8RDl4vTJIMLZOcXM1QPIrUfQMr8BpueVWQIqXsTkG5OmYvH3sE-DWDRlLDq1b3ot5txfLPp5ZWkF-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز تخصصی احیاء امر با همکاری اندیشکده هیئت برگزار می‌کند
🔹
اختتامیۀ سومین همایش علمی هیئت و آیین‌های مذهبی
🔹
با حضور مهمانان ویژه: آیت‌الله عابدینی، دکتر سعید عزیزی، حجت‌الاسلام محمد قمی، خانم دکتر ناظم‌بکائی،
دکتر انسیه خزعلی و با اجرای: نجم‌الدین شریعتی
🔹
۲۳ مهر مصادف با ولادت حضرت زینب (س)
🔹
مکان: مرکز همایش‌های بین‌المللی دانشگاه الزهرا
🔹
جهت ثبت‌نام به
تارنمای همایش
مراجعه نمایید.
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/467686" target="_blank">📅 14:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467685">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8de2b8cf3.mp4?token=R98Fw_CrGsqVqm2nGBCrPb8CBMvJDnSEJAS3mztIr2J-ydcQNhOfmVjNMH1snpqCm1DZ511GJNZMP--TjW0Mc-os6b1OaSRNLDQD5QToPPUl8Bp3odeIdhhlzG-6nAi9bLMOcS46mlwz-96fzV79LTlozbzxfUUmALCdFrRaAD5ZufHvv1XjRJImdpBTyfz3QbIAU3SMTyfaDVrdId52ZEyJevQhyy6psg2OFZUpuDaL6ILxeJDdTyWU9zMMSnm2ycx_FGEoVEak68DZXuEtW_Qa5L3nIeNi8994Obrv6Hi8sQCJdrB6JK1iucc70gOGWgqPwv2gCyDQKISB_ThBRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8de2b8cf3.mp4?token=R98Fw_CrGsqVqm2nGBCrPb8CBMvJDnSEJAS3mztIr2J-ydcQNhOfmVjNMH1snpqCm1DZ511GJNZMP--TjW0Mc-os6b1OaSRNLDQD5QToPPUl8Bp3odeIdhhlzG-6nAi9bLMOcS46mlwz-96fzV79LTlozbzxfUUmALCdFrRaAD5ZufHvv1XjRJImdpBTyfz3QbIAU3SMTyfaDVrdId52ZEyJevQhyy6psg2OFZUpuDaL6ILxeJDdTyWU9zMMSnm2ycx_FGEoVEak68DZXuEtW_Qa5L3nIeNi8994Obrv6Hi8sQCJdrB6JK1iucc70gOGWgqPwv2gCyDQKISB_ThBRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فولاد مبارکه فراتر از صنعت، حامی افتخار و نشاط اجتماعی
فولاد مبارکه در سال ۱۴۰۴، با حمایت از باشگاه سپاهان، ورزش کارگری و خانواده بزرگ کارکنان، کارنامه‌ای پربار در عرصه ورزش به ثبت رساند؛ دستاوردهایی فراتر از تولید که در مسیر مسئولیت اجتماعی این مجموعه رقم خورد.
@farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/467685" target="_blank">📅 14:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467684">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtU_f0YmGu4nhNg8J33gBYR_CEXTDoGeiI1jkcrjvFnzfF8rVMj8ezk_EKTvYJGTn5Ayx2xjrRZU-K7U5MRr5DNvfc5Y6T-XzgK6JZj9pLPMyf7fuF__mMTp4k3BL29f8XlOoKN0bJMkxV57Vkf8y4ACSffs2g-N074QSnZz9md4oXUwnBdaeisdgDTwShfWDud3FmZcgmg1pfh6fsF5d6dFc6eaNECDp6l0t6iw0oUgw31gyt6Dy_tqkPjGPzsXwEUGiydiB8ou-tNe3o6igqSf4ek65EORMGCFpXDX_guJ1rL7x2S-rzGoY5hBVXUDpLzH1fWBfmVnlAQhQ8zWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/467684" target="_blank">📅 14:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467683">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/467683" target="_blank">📅 14:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467682">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf490e3aa.mp4?token=rpNa2UrJq9VRbwWtFKar0snon0ESCbsZbRC4Xd0ZCeSgFwjvCj6NoiFJJOEP6DexEFxOpdIqrWHSxW2J4mW0CI3lzujnukRGhBeZxS3t9w5vyOWahxV3ysYNv3a-O55nVbkxovWTwQli0oNuB2KRM-4l2L1L7C_x2J4DQOicGxIbpINijRgD0rP54g_9Cp3igxhyBKHXzCwyhK6bP1tuY7ivZ0odG1wt9vscFGPtpkNORuOZxhQtLoESEcp1gNhEqwLQaRGyaWmuQCu-nBeG-SAC1iM2fTtirrq1z_ZqT9zOunPkgcawBP6s17dTiJE3D1gssULucBncJOMa-iRiFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf490e3aa.mp4?token=rpNa2UrJq9VRbwWtFKar0snon0ESCbsZbRC4Xd0ZCeSgFwjvCj6NoiFJJOEP6DexEFxOpdIqrWHSxW2J4mW0CI3lzujnukRGhBeZxS3t9w5vyOWahxV3ysYNv3a-O55nVbkxovWTwQli0oNuB2KRM-4l2L1L7C_x2J4DQOicGxIbpINijRgD0rP54g_9Cp3igxhyBKHXzCwyhK6bP1tuY7ivZ0odG1wt9vscFGPtpkNORuOZxhQtLoESEcp1gNhEqwLQaRGyaWmuQCu-nBeG-SAC1iM2fTtirrq1z_ZqT9zOunPkgcawBP6s17dTiJE3D1gssULucBncJOMa-iRiFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رویداد ملی «جامعۀ سلامت، مردم‌یار و مسجدمحور»
🔹
دوشنبه ۲۰ مهر مسجد جامع بقیه‌الله الاعظم( عج) سالن صدرا
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/467682" target="_blank">📅 14:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467681">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64de53cead.mp4?token=XorxQojwNt70YN8BFiAWcEBDCS_Fwuut5kNnYC60W9EQRwhqgx14qev8IbQrWLOW08Hxd-WHrspE8s4ZIyHvZ77GMjWKX6bp0kQkZojIkDFNk7SpZh7b3DF717M1ta-qjDueFyNkb8JJhug5ocO1VmfcwW3X22WfQtlEDGSm4aRQTeMXViDvUwpdIjxHMTw6UE83RVTTwcugAI5aXUIIRdz1m-BwxWW0gsyzVNCUjj8tXA9Fdq9CMYg6TNugPV66QKg7GlDJ6lzqL8QnNIkR9HqdgNSL-2DjxPdpEclLGqnDhR9rDxsEqSfZ3i233B8Oexp8ieFi7NaXssdt3drOnhr6dvRxV6dj7zUOTdzwCjJnY93YNR9ne3Kq0QDAE-wONSe9GIkNT2UlPK9vPhVwsFlF63WNTMQSYbSaghM1o_BGVL84NeksM8EIXRWrilfPKJcUx5YAYlzzy1ZxjBrsEkF81G45sIOWBFE7Psq3-YfuKHGKCrJZMbkOIAFBLEbdIRwXrOObIwJzXs6DTbljemz2k9fnYupCrVmX5P_66jumgHE9YoRSxBGXg9-gIB8PWXhfwbVI6ml12bQjtmKEP--ZYVN70N3JEwunOLxk1Bvu_Z0QBS3gtL3iQWnks6OMrf67FDRT9CYzOL85XCV7uzMB_8lbg6xButiWIwdzACY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64de53cead.mp4?token=XorxQojwNt70YN8BFiAWcEBDCS_Fwuut5kNnYC60W9EQRwhqgx14qev8IbQrWLOW08Hxd-WHrspE8s4ZIyHvZ77GMjWKX6bp0kQkZojIkDFNk7SpZh7b3DF717M1ta-qjDueFyNkb8JJhug5ocO1VmfcwW3X22WfQtlEDGSm4aRQTeMXViDvUwpdIjxHMTw6UE83RVTTwcugAI5aXUIIRdz1m-BwxWW0gsyzVNCUjj8tXA9Fdq9CMYg6TNugPV66QKg7GlDJ6lzqL8QnNIkR9HqdgNSL-2DjxPdpEclLGqnDhR9rDxsEqSfZ3i233B8Oexp8ieFi7NaXssdt3drOnhr6dvRxV6dj7zUOTdzwCjJnY93YNR9ne3Kq0QDAE-wONSe9GIkNT2UlPK9vPhVwsFlF63WNTMQSYbSaghM1o_BGVL84NeksM8EIXRWrilfPKJcUx5YAYlzzy1ZxjBrsEkF81G45sIOWBFE7Psq3-YfuKHGKCrJZMbkOIAFBLEbdIRwXrOObIwJzXs6DTbljemz2k9fnYupCrVmX5P_66jumgHE9YoRSxBGXg9-gIB8PWXhfwbVI6ml12bQjtmKEP--ZYVN70N3JEwunOLxk1Bvu_Z0QBS3gtL3iQWnks6OMrf67FDRT9CYzOL85XCV7uzMB_8lbg6xButiWIwdzACY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن مهرگان در غار باستانی کرفتوی کردستان برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/467681" target="_blank">📅 13:53 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
