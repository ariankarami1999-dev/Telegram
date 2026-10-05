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
<img src="https://cdn4.telesco.pe/file/mGbi62DMHpc2Xv3XvVe9665kE3YYSNsnxaA502byat4ODDRvX-BdW6BflB6rNYZJKR4r4Gge0qDxe_TOfDA_-jcp1RD3RwussQQv3pzVf1DoqnL_4I1wPF5Gd-MLvSXBwq-dNcYjRSLfBPriv4nSsJlVeZ9uMREa-K1yQnuKjaGyFwZWHd1zElidrAbLnEwt1ufBHSKwhrQzyMY0fQcUlpba9J9yBplKSycPj3-wQM5HG92CrYetM-A-H7Bz8vVqsQWJyU2iqpK0HZq885t2ynh5I8uBG6Q40X31RRrHTCTmf_nFWf_-ZYn8G-Ugt5UBRD-mNK0b1gnh-9aTyqp-Ng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 470K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 12:49:28</div>
<hr>

<div class="tg-post" id="msg-31015">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TT4anz9JMvVO1F-lGyLcqpFdar5Az106SVLUcBUmyQFqaSBSg4G8FhCTiNqt6E6lvwp_NmNfMKK0_HIga6Vzc8lDCLVXG10TUnl_ZyHCsMCllUuqItSfytUUU27R8f33I-jmiY8XA8dNZbrDRvJ1xh7N7OCfIy9aityCzZLgFW15Inc4QrIAfbFxDtQdMxvASaun8IpcwpPqhii1a_NinizKwtPrpl7Xz9JEq12QZddiFlF47PqFlUVyGab1wRPrjhvbgXxDtHhW63HuWxu-Qhe7hPqaI8RhZLT02r5lbpAdA8R-Lvnut0Pq90qCIUq1ruAtQleCEtAmqsT3-oQE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcNajzErtTqGs3NGHURYIt2Yvb5p1oKPmFjaiXgJwmAgAnRtJAzEjLDmVE1fdqRCFYxNADZX7ifR9ZhD84juakwCcouYKxAvKJO4Ia1T5c2pUD9ddmA1S3bwpF3oOMteBpgUR0bPNDsgGeZzleHk3_xMExYyl4mVs_TC0o_MqcM_5fGudcFuWvbIbmo1BgGM4F04TE35V3g9A3pHgeTdio6a2uZeTXoMcFc4UVD3jg8IflDdBtRMqIjb-VX5AcRFnBYvfBGo0Rx3OVFB_3mk8eGkogdsM2J7MptfxGWbk4RfpRIfB4gd08CaiROTMRnOtk1fzjRbStNuTzSSvnviUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تکمیلی؛ هفت‌گل‌تیم‌بانوان‌بارسا به رئال مادرید در بازی شب گذشته؛ وضعیت دفاع رئال مادرید رو ببینید. قشنگ میزارند بازیکنان بارسا هر کاری که دوست دارند در محوطه جریمه انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/31015" target="_blank">📅 11:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31014">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiIa34SmIP2zYqy8TA8apS__fH5Y9L1MxXH5oHBRj7SAB3Da4V50sSEeNzVtuGJhYNLepetdTKIIflUMrscyEbyfkWY3FT_ZDxPj9ofsRltAM1Q4bClB-Yd43YlwOGPHW2pUDY7VpZiNr4wUVvz7RmP-pU6EZF47qQiJ8OFxqp_B0U-uG5MmI6dHyuwd2rOFk-QQfxbrbTdSYuDN_SH9pztOE11H6RNHZ_7aYFAgFWDSP210bOgBtWTwMy4QZapMKiJv2V14ryE73hAWpAjaGdnODHqHb0poTo9hfAo2DTloY5IqvhnLCDNiS0We9Cj62eQpGgzns0_iA8bN-EKjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تتلو آزاد میشه! پست‌جدیدصفحه یوتیوب تتلو: امروز دادستان و رئیس کل دادگستری با تتلو صحبت کردن. درصورت‌ارائه‌گزارش‌مثبت‌تتلو فرداآزاد میشه!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/31014" target="_blank">📅 10:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWPhZdgGF5XfV0aG16i4kr9C0w4SCAC1RSrEsuAED5XClLzE7Iq-wtVdl4kDNhYa3TTa_GXkHAORZwzjpr6ykMflyzwLak6YHIgsTQbejac4OK4HxyZH1JheF8enoIaDZBE3iQ67gLStnp5Pe1KGpr8-yibidq1_17rML9eemhyNWPpR3lV5EIKll8TWzdTw-dpSUgCvsm14aoqJFU2MMIkqQencencHhvhsaSMnow35YLnv-GC6Z0K4h970XVT_jbro25q90AyiKtxe4pZN-zk9y-T6nJfTBcfys8Tyng_N0ASwBsiMr2wXuoBJixpptw99dZQFWjVyavwAVSTk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق جدیدترین اخبار دریافتی رسانه پرشیانا؛ کمیته استیناف فدراسیون فوتبال بعد از برسی کامل پرونده یاسر آسانی به درخواست باشگاه پرسپولیس مبنی بر غیر قانونی بازی کردن یاسر آسانی آلبانیایی برای استقلال پاسخ منفی داده است و بزودی سایت فدراسیون دربیانیه‌ای این…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/31013" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8ITAx0rrdK9WuR9eBJQ2bIIFKPXCgUUReh5pXfzBnvKRelHSCLJYfi0MdAByUe8ucfjCzV1d48kND4A90wssis-kWomUTUYDCWRDhB68qbvnWDrUsLsL5fO82nAz0c37YTo-oQ1CedHXP2BqLrUBCnjWLYvxV1TTLCeUKgyleIJhmQHo4aEzienDEvAIlnoia_CDZ58UUvvmHYEWxuLERancQdDRtwMBN8K_MZNjJHE6FhBhAyZm0PTFWX_sWGFJQeauD3UmPG3viAc1Akc499KtcqzA60Jz0vdKRki_5TUMX0Ra5_bIG81H23BblshGDmHoRe2MhM9kAmmxH-8pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/31012" target="_blank">📅 09:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31011">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3A8hkP_M3C0bZzTWJDRV3-326NokpQnb2mrvzoPI-YuIVZl0d7trz0U8i1o5FKKp7bLfFgfQRhLHxWZ4lPGdOj9P1xhXC6ouHcVqX5HQVWJ-yw18Fur_N1pjK6yUGykXABtO9cdFF1-Lxs1oreT0Fg0U4ZrqnhMVtFPlr4p-Xy_srzZ67Flbk2cs392ro_66JcjhQTkMjJbZqgUsapUkK97tHqydYNINQmdbMk0OA3iAmkUGBxy1dyXvO_44xh5BrxKOKpDbrDZXXHJORCGRwsf5lPUWuERAh7tnOZbluEHeFIcg4sBVRCYZCtjYHaeLpaUpegETRT9Uwovqez16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه آاس:
بعد از فیفادی رئال مادرید قراره از وینیسیوس‌جونیورتستDNA بگیره و نتیجه‌ش رو با هوادارا به اشتراک بذاره تا بشایعات و تئوری‌هایی که توی شبکه‌های اجتماعی مطرح شده پایان بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/31011" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31010">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=fHzin24BdRe12_S5pcSJrL4cH8X0NExcP0LG2DbIi6Qz6BqvsmgvPwnDq5yvxRyDfsxJflq_TjdykFsQP8Jgr6lhCQg7Od-B8phyYzC2DpFzD2zSrfDIirdQwSh-HdU6beZe5xoPTzm5mrP5yOusDq0SC_G2O5QW8J8p_nJbpllCLXCFLtiTlEtETmAGZXGVBxwgY0NQl6c_wN9ze8I--hiaVUCa9yilL3xJlANl9PRZQW9BHzguMK5Kdp47Y2WOM7XZarjPMWy6PTQ-u-nFpBda4IzgYhu8ZxS_zO7RWuoZnvqrVUKdaNuy_rqLuUj8-0aRx_lCr5gVXo8JjztB6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=fHzin24BdRe12_S5pcSJrL4cH8X0NExcP0LG2DbIi6Qz6BqvsmgvPwnDq5yvxRyDfsxJflq_TjdykFsQP8Jgr6lhCQg7Od-B8phyYzC2DpFzD2zSrfDIirdQwSh-HdU6beZe5xoPTzm5mrP5yOusDq0SC_G2O5QW8J8p_nJbpllCLXCFLtiTlEtETmAGZXGVBxwgY0NQl6c_wN9ze8I--hiaVUCa9yilL3xJlANl9PRZQW9BHzguMK5Kdp47Y2WOM7XZarjPMWy6PTQ-u-nFpBda4IzgYhu8ZxS_zO7RWuoZnvqrVUKdaNuy_rqLuUj8-0aRx_lCr5gVXo8JjztB6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
تیم بانوان بارسا در هفته ششم لالیگا؛ با هفت‌گل رئال‌مادرید رو درهم کوبید و با شش پیروزی پیاپی در صدر جدول رقابت‌ها قرار گرفت. تیم رئال مادرید هم با 13 امتیاز در رتبه سوم قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/31010" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg2EjZN75HwfsiYHpuh4eoeP0pFsogMkLJFBfKoHbs4JmOGb-yBYN-QOaGgDEhbUiFIGgH7unjllLj_Z6KhHWv_qOs6nmtC4JjJh6iwUHYWNwpbflLhmplKCOl5cdIjvGuuA040ka_gelKCZze8cLur35YIQKb1WvDYeetGMwKLKMPi0dWMiFNuQ5uPEW4Qs79svokv32sA52pmChcKiJ_JUsJmdd4fTzlMpfRPkx4g2rWFzuUV--MaPokjwRJIvDfmvy4aknJYBaiKfPDNcECI75UhklkD1uIT20u4iRoOUIOvyPQURAmaKMfcnXfdW8L5YvxEEgDTDQnkRCFQEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/31009" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3HCvQf3i93YM_2a5hRUKOX6HUQ2o6tBQMTxezn-69QHbVkG92e9CpmkTMlcSQZtr_vffNQlysj8I8N1imDR_9TQ1MQWDJZU3_6TJBrXgGBgs2V1RRNL926PLa4Ii9cGaRu1bjJt_CjIXh6OXkj1IW_56W9OV7ZE_2TIB1LTYFzcUT1k6yrG1z83fLyUfHBdbVnyNxMLSCufvL1Jd0bdTlcKySwAMorKyU2spu3xJGq0E6ooO8U8MvkOTmTompK-nrjvbqvbhsQ9jEpIPlCQrgXnwuzvVkdyn4Cq-7MXf9CEIksNjG2GHKYZ_eehjNMcRw3X1MeQveEYS9hIeoQPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/31008" target="_blank">📅 09:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-PfdQug0NJlqhLB8wY9jGPKKiB8g-4EtAE6YKs79yQIiP7U_WdKqz0Lln1f-t2LeKEhsDtCoS3pL3UgBp451KvWm4MbNTiBAW6LW6-I92yWOXxdPkXK4wjk-VrDFtDCIUcEU-n22599DFvpCONrsjgDNrjyfrR0AooGk3ph2i46fJXQjESpQ8ihN9R26tpYvZRMLO2heLUkbLxH83tYDSRz_PtAoPpeFI1oJA5chh2KyI-aIRHWGDba3lT4CIj-WJInI0Pk6SL9BjpZnpHyDTx9Wl9agL21wX7EhfjDVOp6CZm8Kuapmx1PJGEOJYG0pBXZjk4QqHCpOX3fbgJM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/31007" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31006">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=twG9qVDaW-a112ZGCb1Yr7YJFKCdPAKOitgfcrFVnUPQcMynQAeB8W7jrbYtw99Ck45oQ4_y0ET__hjzKQqFWk1zcxzSbUj22wgQkqlOKyFiUXEbIaywyXtZUAGIfoh4r8bLZ0fNyqTfhmzgL3rl88-nV1GK1DJ1jHlRKu-P43KuBp1A1kz08r4Eq39T62ue7R1-zZ0N2r6O89LM8TUbxFQgscFZUK5mtQ2kBc2v4a6lB-fjs-han30idvfrdi6aFncKAE8xEls5-__nS1bBVgRN0tWC3iu1zVaFt5LvcrI5yw53HvZI3sBdI8ZKDoPyLnI6WW7LzWLvu_ys1Bllmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=twG9qVDaW-a112ZGCb1Yr7YJFKCdPAKOitgfcrFVnUPQcMynQAeB8W7jrbYtw99Ck45oQ4_y0ET__hjzKQqFWk1zcxzSbUj22wgQkqlOKyFiUXEbIaywyXtZUAGIfoh4r8bLZ0fNyqTfhmzgL3rl88-nV1GK1DJ1jHlRKu-P43KuBp1A1kz08r4Eq39T62ue7R1-zZ0N2r6O89LM8TUbxFQgscFZUK5mtQ2kBc2v4a6lB-fjs-han30idvfrdi6aFncKAE8xEls5-__nS1bBVgRN0tWC3iu1zVaFt5LvcrI5yw53HvZI3sBdI8ZKDoPyLnI6WW7LzWLvu_ys1Bllmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی اسطوره‌آرژانتینی تاریخ برای انجام آخرین بازی خود با پیراهن تیم ملی کشورش دقایقی قبل به اردوی تیم ملی فوتبال آرژانتین اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/31006" target="_blank">📅 08:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31004">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFTceET7WxaSc9k4Uufspte33bYmla3ZupzJClrtYjT0NSOQBkJbEYUGlybqNG0KPs19ggnMMYXspszux_mJZNUS5axJTG4UhoYeSf3-_NaExFK8dR1lfsJ_65_K2h3ngtpPWicMvidU6Tg_xuGjmlP4jlR82IXtHXXvmifjlnEaT0BUCJnFx41wmQfaI-lZQSKbqYFdExgBRpAIzPYOE-hqiW6Fztv8Gmq-w8mY83rQ3coJ1ZPnMMKCF66gPsN80rqklZJbk-SrwTru4b9zf3G2FM7OMWcZsoiwYcU1EDhUVT7q8GxfzyBdUqKEbNCg3ogmpqa3df4lGNRnI881Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/31004" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31003">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2OuS4j9ED8x63KHpfX0NU86oAVkR0R8t776ZAtTgoHPIs2qksNmnyWH8KXWbl_wPh0T3Ggat4BQEZA7hB_p-id7twaRsRcHLTygnsAK-fEqjpFLKG_T3hp4TIAk57aML2ZDhO2gvyQ989nn6Mp1fR2nCha7yl2tW01C_JDZSstZuZDixX5VvYXQAe5ljIPzMSBFQ1KQdbGMAL5lLm8o5bGXM-s8b0yrQLZke68WnTUpxLNjbPLTVq9nk0wlWYGuX0nlUBb1ST0cwcb5tNG0kyxUpvuynvj_KpEbgv9tCrRYMn6oTaXBqqS95kvIrgUocJmFHbbgB1A_F_6nTzVxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدار های‌‌‌ دیروز؛
چهار برد از 4 بازی برای شاگردان ژسوس و تساوی بدون گل ژرمن‌ها در یونان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/31003" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31002">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906c18ef7c.mp4?token=aXyuZezMsFJx4n1-z2xJDfOxoyXfKtCcip8LKbxjzuTFW0wX7r8B2PeC5FKTQVO51PsHt67AKwyxLtiFPkDQKtlyM82SS2XUL-aTi2HZY-DxS8Vjo0XQmepkfb0dFCj0Liv749qk8HSMFykunM_XBMLCbpD5NQ-27jqEzNJXePG5DVNaCFaQFTIfz9g8iHYNH4GP0z237Zsq_jBY_QZqxyOfVsSOtFHnqoQ8B7W6D5jYoMWGdYZiiNnyKqJVHn9Uy_UONLmL-SMsWyVxWPuToOJ-4rB60n4i4z4ic3FV64g2pF251zcr-XEXRSMxL1XU9gKQgnB2Th8XGVbHtnGASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906c18ef7c.mp4?token=aXyuZezMsFJx4n1-z2xJDfOxoyXfKtCcip8LKbxjzuTFW0wX7r8B2PeC5FKTQVO51PsHt67AKwyxLtiFPkDQKtlyM82SS2XUL-aTi2HZY-DxS8Vjo0XQmepkfb0dFCj0Liv749qk8HSMFykunM_XBMLCbpD5NQ-27jqEzNJXePG5DVNaCFaQFTIfz9g8iHYNH4GP0z237Zsq_jBY_QZqxyOfVsSOtFHnqoQ8B7W6D5jYoMWGdYZiiNnyKqJVHn9Uy_UONLmL-SMsWyVxWPuToOJ-4rB60n4i4z4ic3FV64g2pF251zcr-XEXRSMxL1XU9gKQgnB2Th8XGVbHtnGASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چرا باید عضو ما بشی؟
🔹
ارائه فرم‌های دقیق (BTTS، Over/Under، هندیکپ) با تحلیل فنی.
🔹
رعایت اصول مدیریت سرمایه برای جلوگیری از ریسک‌های بی‌مورد.
🔹
گزارش شفاف نتایج (برد و باخت).
🤝
نقطه قوت ما: گروه همفکری اختصاصی
علاوه بر کانال اصلی، به
گروه همفکری ما
دسترسی پیدا می‌کنی! جایی که حرفه‌ای‌ها کنار هم جمع شدن تا قبل از شروع بازی‌ها، روند مسابقه رو آنالیز کنن و بهترین‌خروجی رو استخراج کنن. اینجا هیچکس تنها شرط نمی‌بنده!
💎
همین الان به جمع حرفه‌ای‌ها ملحق شو و استراتژیِ برنده خودت رو بساز:
👇
لینک ورود به کانال و گروه همفکری:
[لینک کانال]
https://t.me/+-M99R2qSbdVhOGI0
[لینک گروه]
https://t.me/+M_YAiGu22l05YzM0
⚠️
هشدار:
شرط‌بندی ریسک است؛ ما اینجا یادت میدیم چطور هوشمندانه و با کمترین ریسک، بیشترین سود رو بگیری.p12</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/31002" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31001">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgTPjdDTMamUj-DHvrNqsp-B2FMGSGwS-YhsAW72Oexap2MowONfs9DAD8ELJUZ1FpRkcDuszSwEQthOw5L60_8aRqjBMj6_G6Msh-KyvTE8hkrLm9U3KTE68-SQd2oj0Jlw7muccejjp_wFsufZ0AVbIdYMh0Va37TasZkTfTUI3QXEZfDPI1xxyrUZcwaIe8QCdYej1EN_yHIQsN5KoEaIDJj2T0W2Cr9x2hCKyhAbUetRUVLKV6lZ6dLipWV9vCJS4QenDGDSU4o1Vb03cp9Iz6BFknUvzzoXQD0xBBM6ddNLlnZGEJOKHF_sZh8lnWJHmu7SZFk3ZwGV1uWYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/31001" target="_blank">📅 01:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31000">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAdv78xDcGqEfUlKLRq1E-WNEFgIP-DtG67jzxdKTRUczQL9BtVp5MpG3jF7UNJ8Q0ZesFYUMk8O4dCYfl6_x7X89FMCFvT6JcuDb24AnrkDmCtR7f6FjAks6U6Lpx_QSuGBFaeeqXFg9AMi1l6H8sQIM5JSiREEjPEfF9Q3VYk2ehhDxBE2QpU84qfSp4Ty-Iv8nT8SVi3GSRuiZYoHQChlhW37o5ByNSZ_3DLRKDfC2YYv2P3ljijXlAL8KKypD76uyDniiXcBO1A_243HFtXHUMstcISYimiJjql6UuMmqQdOp0GAMYqxoUYou7U8vQcZyzz6xuZE5qVQzJxhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/31000" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30999">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇵🇹
چهار مسابقه چهار پیروزی؛ تیم ملی پرتغال به عنوان اولین تیم رقابت‌ها به مرحله یک‌چهارم نهایی مسابقات جام ملت‌های اروپا 2026 صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/30999" target="_blank">📅 00:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30998">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afh0l_4gk47WaxHhc3mA_VFyLZ33QWpSrVDGbs9M-lGVdAeklCRKoRBQwTuIUphUdZ4B5hxnz_G3dfzrcMalduf5lstJUQSC21sE-foO_2LN_4ZmTtMs-ZFsrq2ofLNpmN9InTHhTX8FP0waUM9FE3j88Xukc7dY4VGbFp3SxGscXxgHoA0iTskzxxAWHmhjnAOV-75JbblwX2PDh-zsLqC4njK1eRnzvQkPl-jfU3yv4iytdGex2F2fPu0Z0eGDXngR9OWpLDxOlhKAi7jlLFOatvuoz7-l2qjOfr13GdIf-3QuNedpdqlzXTI2Rgp4mKsWPLGaOFgLNhmaksSfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/30998" target="_blank">📅 00:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8HpjfgG5QbPAxrWOSU0QGn8CO4wnOPluZ-CL3WOeHYt74SMntqFX2aGITIxMvWCrr7GcTNaVfJuJveavnM8NJmuxJEJBT4U-0dQM6CbFgHLfFmPF6CHkGP4I4XPXNDIAI14gitfWBgXRRhvPZbcHiZACGUPkPUM2yxuP2U0yTzubnNp9Vqqw8s0PQpagaDAFxU5su838_tyPvE4QDIgXHRnWRUrGDkQKuOPuhwcRT8eiiYNoZGZcmq4gPkySBrB5B427-i1Sn-jmXMPeSbgBebd89hRvywi1WpOM4gD9RHuLWKfzmY9MbwJBDoJ18Bfcos3l0uwZjQV2hjPzjGI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/30997" target="_blank">📅 00:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30996">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8Ficu-SbVIo0BdDL81yAm0gxd0BI6lq0dhl7QkM9TUv-bgPBOXIvo7e7MHEu2ORnmlIgfRiLHikfhk1Ja-MqeTL6Oi7s8eHL2kzsDEaXPGCESVE-Lpph89N8-rbYp7jg9nVBcnHXdYsr6f-iUmKhqrd7xE9ZQUd707E6Boc7X4wZYW3tlNWnO_7FeAXmg0jIYqhJgfOGIn4wHyDKQSVxY48LHb2x64Ho9hx2F9_GmVddQCUIVJvw1H80R6Kao77d76nexSsDtEJpr8pyljZgWwnyeXwb4J2qSbvvQCmqRJri6QDfjfiHUnVR1Xwz2ZAEkxWATCFGYpWwrcqy6q5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30996" target="_blank">📅 23:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30994">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9256e00306.mp4?token=KKT3520e7KEpcY7a4q61ykPlYlcSbQLsnDh0rs4AgMHojJMq7kWpiF-ZZm-d6Yl85O2T4TgXqK_7mQUANQuDJ6XJSckSOqscWUN8uziRRROgrImS6oR-pYb1kD6XNq-fvl_B_47V7X4KrYnBcP4Jql5xbPuvVqJbbM2KRA23o5I-RmACxb-PxiDCZb8y6UIw1d5-iRc1skHdrn5qi4djiswX8URQNsvPNpKlgrQhjpIPiIYA93gGTOcTuvf8xSuNb60WC7_myHmo0rcWQcTib17kyp2wgdPePuwRHngEap1b8uxWDrknJb0byfQ3Tn-Sm2CmhESR_ZWgoYTjRujpOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9256e00306.mp4?token=KKT3520e7KEpcY7a4q61ykPlYlcSbQLsnDh0rs4AgMHojJMq7kWpiF-ZZm-d6Yl85O2T4TgXqK_7mQUANQuDJ6XJSckSOqscWUN8uziRRROgrImS6oR-pYb1kD6XNq-fvl_B_47V7X4KrYnBcP4Jql5xbPuvVqJbbM2KRA23o5I-RmACxb-PxiDCZb8y6UIw1d5-iRc1skHdrn5qi4djiswX8URQNsvPNpKlgrQhjpIPiIYA93gGTOcTuvf8xSuNb60WC7_myHmo0rcWQcTib17kyp2wgdPePuwRHngEap1b8uxWDrknJb0byfQ3Tn-Sm2CmhESR_ZWgoYTjRujpOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شکیرا همسرسابق‌جرارد پیکه: برای‌اولین باره که این‌موضوع‌روبیان‌میکنم‌ وقتی‌از پیکه جدا شدم. یکی از هم تیمی‌های سابق او که اتفاقا رفیق صمیمی پیکه هم بود به من‌ گفت که بهت‌علاقمندم و در این سال‌ها علاقه‌ام روپنهان‌کردم و الان بسیار خوشحالم که جدا شدی. یه لحظه…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30994" target="_blank">📅 23:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30993">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCyumyKyKJulzB-nNs3NUxU4fXr0zzF21h7SuD35ryaqUiU6-YP7DOcy7oBFO5Jbhld-zSbwE55I1wxZTm4vHe0b4Pdk1uwqmDkdxohZ2w5nfg5ppsN41g3OXiD4a3Kp_GavMNiETttRtJFWypWiEH-SvehgtTmrGxOU-EUl0yESmRhoBWrU3WePLgOnFbakiYep0k3f36wJR5zrg1J6PXHswzFcQL3ycCurIlUP8nLsEYvHtrgQWG6kcnb8sCQhfYFg7HRwEvLdzpUb6NGsGbNHqlb9foCfX70b1uQVgEyvLlQkXeM-HUfqWV7onjwNXIgcjbsteROiKe22cAtHIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30993" target="_blank">📅 23:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30992">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=RG1FxbTcMTEBKrF1QpFu7hzOHyw8UaXwssK0mh-htyJOiw1_8JL1ZCpK8XU1Bln7AkmqbzvylDWdPcPBZyqAI41aXkg9_cwU5koQV3qE-gKxC3QYFg8YijXfNZETFjO3lIMkq8WZPdh9Nu4D-IVjAdmRVonzY8y3reaQ9YvfUmyGFtdozRmC3n4luG09pJD1FUvsjSnJDj4By_nSbWGkmyJSgKWYlaaDikaLOBV7t5Zhbqb_lb9P-lV8emIbI_IlLAoLd7A_606u2NtiVcq2PemMPeilW0p64Q-lvVzQD8So1HgtbnNAYxgsLedRBgy5sk4wv7oPjIdMovsoJkklKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=RG1FxbTcMTEBKrF1QpFu7hzOHyw8UaXwssK0mh-htyJOiw1_8JL1ZCpK8XU1Bln7AkmqbzvylDWdPcPBZyqAI41aXkg9_cwU5koQV3qE-gKxC3QYFg8YijXfNZETFjO3lIMkq8WZPdh9Nu4D-IVjAdmRVonzY8y3reaQ9YvfUmyGFtdozRmC3n4luG09pJD1FUvsjSnJDj4By_nSbWGkmyJSgKWYlaaDikaLOBV7t5Zhbqb_lb9P-lV8emIbI_IlLAoLd7A_606u2NtiVcq2PemMPeilW0p64Q-lvVzQD8So1HgtbnNAYxgsLedRBgy5sk4wv7oPjIdMovsoJkklKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صحبت‌های پیمان حدادی مدیرعامل باشگاه پرسپولیس درباره شکایت از یاسر آسانی: مدارکی از ستاره‌آلبانیایی‌استقلال داریم که به کمیته انضباطی ندادیم و اون رو به دادگاه عالی ورزش داده ایم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30992" target="_blank">📅 22:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30991">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3CrZrngqj1tywV4Y0D52IOCK5pTlhYEBVYqY6uUC32Bga_e22QPf0m1qbwypuz_3sQaHCU6UyxMGTRfHPyzvC2ws8qf4EeqR4hT-jbZuKeh5Z0g5xU3ddBjW4wUMi_FI7A9fuFItn1XZWRyoRS004ix5AoeyA8TduOR3vy5LGRyNUvn-6ocF_3PAHUWhRt6AKGdGh0oldL6QNWPernU1uj0vGn_6WePYFGelgZ4MqBPZ_uQk59hTpQ3FoVO4cJhZ2hS_-CR9nRDjJw3nO_a7VExWWXTtBUMLlZmMKzkHKOlg_Yl4f1_kN450dihfkH_Cz2G-q-OyStNjh7vHdEVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ادعای میگل پریرا خبرنگار پرتغالی: کریس رونالدو مصممه که هزارمین گل دوران بازی خود را با پیراهن تیم ملی پرتغال به ثمر برساند بنابراین احتمالا درسال2027 به میادین‌بازی‌های‌ملی بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30991" target="_blank">📅 22:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30990">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iypxhvB64SQB9oqGwDS20zs7lpHQgIDnYH8Gpe-WB9E93Iip4CQNHVVjT0TDcgkBmIvYqNmFr_C2N7IkASSncAKnTH_6I2sU79N6Jo4JHMAvDsMN1x4E1WghtfGKcjS2cYrI_pB7QlyeOhVIQdsRKucZGI350SxSGuHn3VwVq7rImxFLd7GhLw4PtlCLYLcl5XUdnTDOCq6zTuCM3TyT6Nsnh_OAhd6RvzMSvv3huBMdv4qhisIagw5TzRA3-t3qyZFNNhLgnGrHw7bESP0KrF9oYJuU_iLyC_ladzRGbBRhgCzToFwW1Ptf-qv2fpLqb5UqZK5fevmYN-Nd-c5bjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمسابقه‌ امشب الکلاسیکو زنان؛ بانوان بارسلونا تاپایان نیمه اول چهار بر صفر از رئال جلو افتاده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30990" target="_blank">📅 22:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30989">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOHcdqUQgFXziCvTp9LPvIMMjPSezF5gD9k_n0ATg1-xFQ0TksnJyiyEqrwlS22w_FYCSldWLsrGmYQ2FXc2007xrULUAksQxdyfQLl9KQQSDNQdMdKUj1qF_UqyS2QX3QAb1o0DCcfOu12zBuJjUC70CApoUWIHxvGEVGAa_BW1Ce7YxlcIZ5Y5kW_ZkM61VA6b_QF2wk7AM8hjJ2Avx9kyjG8F-28PrE6kPmkJnCcsWzpx_uYt0Rz1EFbi9SWBYm4nJB83htRXXOzT3SOOD76QnM5fDoAW5JBiniWNbPxQzXO89S2Hh4MD2Mr1qC48EmePUU34uBc4t3J-GSSrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30989" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30987">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTEIUAa9oMrYbVcqYiLQJnpJGptjweCb8lBZZvkcwauwGyZJ3s4QUXAgHGgiYC8vJFfl9POBrCWS7dlBjaTPLiswPCx8LmqbgNWaFDNrJP7Od_msNyDa94IQbcCCrQ8-my81zQNxUZYZPCp91Nh6_vVS30HzKIjx8gn3VJsCu4ckXf8ecB7KUu8QPhY0zR4HrGXiMlNdYg8sWb8TSxepbQ52eKazDfpizO5xBkrN-olIc16mbO64qe5893qvcDG6z8XAxvKjE9sYWbY2JlVVNt8tlpLoVVPWZiFwRKx52tm_02dilPd0alggEXlZxmSJDyx35wmP_ahu3Y0vgcYe2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=s_s3d6X5kMTcW0Ji2hDYvcavtkn6pzXZr91y5uT5ZY3_LfyuvvEAfTrJjs_f03mcpqkpolDXTCNTWmo354P4GWM0uPtX198RpARL96K_AXEQqDMs0qYU1ZjoExKSOjGTJBMjL395yed0rZp5ysoEOeRQSiNZubb1jB18bJqIyXBZs_AbITvpjHrXUKQB9WItl9JbQeju30MHF4_BRN1om22dHiFq2Et-IklYnjSeJQMRa0SUnD7FRj2QCPjJ--tqTJJlJAJh9yoT7SYaTrEn_hMtq3dMp-uY8TXuK16p7hUrntAZBg_YfBQddG0xPC5kVZ5_EH7B0xmCcaY8MBFqeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=s_s3d6X5kMTcW0Ji2hDYvcavtkn6pzXZr91y5uT5ZY3_LfyuvvEAfTrJjs_f03mcpqkpolDXTCNTWmo354P4GWM0uPtX198RpARL96K_AXEQqDMs0qYU1ZjoExKSOjGTJBMjL395yed0rZp5ysoEOeRQSiNZubb1jB18bJqIyXBZs_AbITvpjHrXUKQB9WItl9JbQeju30MHF4_BRN1om22dHiFq2Et-IklYnjSeJQMRa0SUnD7FRj2QCPjJ--tqTJJlJAJh9yoT7SYaTrEn_hMtq3dMp-uY8TXuK16p7hUrntAZBg_YfBQddG0xPC5kVZ5_EH7B0xmCcaY8MBFqeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیوکامبک‌تاریخی‌پرسپولیسِ برانکو ایوانکوویچ درورزشگاه‌مملو از تماشاگر آزادی با گزار مزدک میرزایی؛ اون دوران الدحیل تو 51 بازی فقط یه‌باخت داشت که اونم جلو پرسپولیس برانکو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30987" target="_blank">📅 22:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30986">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA-qOt-vfzmVhU3WfFM10r6oOD6pnOdbaRI9DUl9iUma3S131-oCJn2-3QXJMthC8PxnZVr_v7BAD-F_moyDB-d8my0VV6UZqL8VRx5fhs8BaWflUllGInhxX2V0mnQLMDgvSYxb6skBkEKrvdyAmrFH5qKYb4QAUR0hmm5lX0QKE8jdfrROAdCrlTvGAsb__wQB_SP4JPFniEuP9palzsBx_PqeuxZ5CipFMdSzSaqGz5bG3U9QO9KpCoFzY2h6eD1XoFMm00U1zHVQweIfvIFJ_rbVBXKsnGjoy1IZv2cgEqpdBpRxV6n8N3PwUbgVzEk6nU5KufvXsU68ejsDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خرید جدید تیم بانوان تراکتور برای فصل جدید هستند؛ نازنین دواتگر مدافع میانی که سرخابی های پایتخت نیز بدنبال جذب او بودند در نهایت با عقد قراردادی یک ساله به تیم بانوان تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30986" target="_blank">📅 21:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30985">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=dj64RcMV3p5mxzCDDaMHQmbQRfdA-KSOjab-kwlESwQB0Do62hPw_8oQOTXurLHlniWEt3tcRuF6-HpmWjSMqwAzPjeXPS8SlUFIQq3NnugTxp6eZaDftMQtlidkXCUf4mi4nbWf0fe4jnhQQku7TrppO_mzggSvSoafL-yI7txoqTcVhhxLmSgriDLAjp4zLlQF6NmWTNkqA8_SSxmYr9uR_CVCmXBZitudV8gP10-LrMsujGDnvigIWjNSG9zwPl4lrXMCsagbOCaBrTXobTTfh9tRfAgLgBmCdTBjGOyc7QaCDt5Wd3a2ItpDs5y-Y7NDnGFF20tGt09jB0yIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=dj64RcMV3p5mxzCDDaMHQmbQRfdA-KSOjab-kwlESwQB0Do62hPw_8oQOTXurLHlniWEt3tcRuF6-HpmWjSMqwAzPjeXPS8SlUFIQq3NnugTxp6eZaDftMQtlidkXCUf4mi4nbWf0fe4jnhQQku7TrppO_mzggSvSoafL-yI7txoqTcVhhxLmSgriDLAjp4zLlQF6NmWTNkqA8_SSxmYr9uR_CVCmXBZitudV8gP10-LrMsujGDnvigIWjNSG9zwPl4lrXMCsagbOCaBrTXobTTfh9tRfAgLgBmCdTBjGOyc7QaCDt5Wd3a2ItpDs5y-Y7NDnGFF20tGt09jB0yIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا به‌امروز اوستون اورونوف، سید پیام نیازمند و محمد حسین کنعانی زادگان بازیکنانی هستند که موافقت‌خود را برای تمدید قرارداد خود با باشگاه پرسپولیس به مدت دو فصل اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30985" target="_blank">📅 21:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30984">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-JXWBkCxmPAGCY8YVAuznJQPVcuNL6CT2UUA_7JKlvVBZeOiL5AYSaERxU5bhXbyw08EXpIR8AQOJf7q_nIY6ibyCUfHpJ3nLCyKFXWHj_y3t9iO2JuhK_yhWOSObdJrBpQYkGDCocQzo-cI2_EgWGnSKDKtw-DHVn4GqXlmbCQIR0MhDWilOEp3ICG7wTGPvvLYdEQmiT7XaYlvxE6k_XDQ1bSEGrQMP8R-UFD1d0VRefUirQJxJLj1HdVOMy9TlHvvJLN17fr0dMW0GILHQjujwjnUJps8ouXNeNSEPZFTQRqWRmuw-yySHvPeQ9wgoyaa_2GcfXv8yQdp-esrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد کریس رونالدو و لیونل مسی زیر نظر کارلو آنجلوتی و پپ گواردیولا در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30984" target="_blank">📅 21:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30983">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdncHOBWIBghy2f8AyUNAasSdkGaGjQCuP-_XY1ENIhvtS2ElDSiVpvSQjBTL3v4S8ovgcaqqyp_ymnb7b4gHMh3S6puRbbDNeRDq4Hfxu93htrzss8qOSD7fraO-iEKZz3wKoyjr-nAbPcGgaPM-jdRJfjUW0t0_DfVLlTmMsQtFYarnYpvOt83TAs3yep-iE729GNs_ZomsV24b9CGDyMDCNMyqNkxSGng2WfdWoAy3OfjLQnGx3gfqj0-o7S9qfzCMTXnlrmAE3W-7C1B2u_cRYDR-zI0Z79d_TtzM_rbIJlgCnBoQlOD3mi5zrsPF51RRk9qENrkjhIPXwbbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی و زنش درتهران: متاسفیم برای فضای مجازی. مردم در واقعیت خیلی به ما لطف و محبت‌دارن و هرجامیریم یه ساعت باهامون عکس‌میگیرن. مردم‌ایران خوشحالن!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30983" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30981">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=sgjkRF_9yP8Hg3tb8n5GR0UtTRjn5wcg5avNXv9tC2qIH21Khykd7jsKURJrWvLg-YbvYfQXMSYavDDYXuWCwTUJIIrK62PwVzwh3un68PWk5tZV8jEdzX83eoQhn24Ln-2GY4ifHnxOmlLpyl-J2E4pnV9KpSaDLMG3GKq2PJXcGMrGHo5ho2lFnjHYRdnqejw2bQE8vleH6dyfu137L-dSRmrCq3mNhEQu3REdtW_LeZtZP6_m1D65X3L9MKTGiteDUyzWdfEmMI6bOUDGWFbg9g059wKmErggBs59heXvsdjR4NhjX0aajPT198WXcx_XWfec4BbX0t38da45tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=sgjkRF_9yP8Hg3tb8n5GR0UtTRjn5wcg5avNXv9tC2qIH21Khykd7jsKURJrWvLg-YbvYfQXMSYavDDYXuWCwTUJIIrK62PwVzwh3un68PWk5tZV8jEdzX83eoQhn24Ln-2GY4ifHnxOmlLpyl-J2E4pnV9KpSaDLMG3GKq2PJXcGMrGHo5ho2lFnjHYRdnqejw2bQE8vleH6dyfu137L-dSRmrCq3mNhEQu3REdtW_LeZtZP6_m1D65X3L9MKTGiteDUyzWdfEmMI6bOUDGWFbg9g059wKmErggBs59heXvsdjR4NhjX0aajPT198WXcx_XWfec4BbX0t38da45tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توییت یکی از طرفدار رونالدو: تو امتحان امروز به سوال شماره7جواب ندادم تا به رونالدو و میراثش احترام بزارم؛ رافائل لیائو لعنت بهت تو چجوری دلت اومد اخه شماره کریستیانو رونالدو رو بر تن کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30981" target="_blank">📅 21:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30980">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUvZjPdou-NHY2M6mERuX7HKctX5PNSPQqCRbRutqTeG8Eaq0q0BtiWFDyJpMce9Oi7GVjCgRGRDoH3ZY5dz6UEzc86qNx4r_o4AXVyv_c2n1KMs3d4B8Olk_u36aahjJe8GOKbcInPoORJE_J8EJiB4VFcLaDTeatkFxgjEAJtuk-8Xn_p67bvCMPSEhBEVmyBj4r_HTClO_8_HWdARhDjnoOP0bjVFDHJIwwq749HwIKAMwkTQK5GA7Q9AHkkKCR7YY0aaRRLTLfuUVs4LWpN1oaAmWP6WANTZ2yxz9upGWhDTHt3TEyXASBTu2xQsVBfVbE7Tf4cVuj3gpVkggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30980" target="_blank">📅 20:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30979">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVkXu_MDYaXN850sbnNZCW0ze8tb25A79STEQM8diplbZdKH9zaMACSzWJVWcZ9OqPEvK11b1y2O8pArsKStIsGOvJ-nwxdUaF0kUjZT7O8lBUOapkyvM_Rxf6Oh7_06rzU5vs815YeD2TLaB1vnkgdrVhSCkg5D-xvWTAbO0YivGmJgnHqcQ-zyFNqyxdyRoi9IMD-sGuyI-ZTRjsZ4-vyE2bU1drxfiZ5CEd6WUo-7FXsB3Xgcljwke4BycpjJxG2tVd75K1QNn1MUSx-BiR9MTzaN_HLIwM795Sk6basHEhPhjffPAnAWj7PI-TnKzN4B8z53qEqi4DdI1gxsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ مدیریت باشگاه پرسپولیس میخواد تا اوایل آبان ماه قرارداد سید پیام نیازمند دروازه‌بان 31 ساله خود را بمدت دوفصل تمدید کنه. همان طور در پست ریپلای شده خبر دادیم تمام توافقات‌لازم برای تمدیدقرارداد این بازیکن با باشگاه…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30979" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30978">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hI_OmSFlE2EOabP1K4PX2We_Vkgx38qw-CQdmHKbIp_uDp608yRaS4abhfiLXWh7Vcg819yrSlLLyc1lcxD3bBoe4bicM8n1eoUkKKn4Rj4-at45KNLKw3rMoqeDPZqvh5G1GwwnHLlrYn8nMVAkpGWIUGBI_wVIUo3p32-ZGzXeKf2xNGkp5KyWiz2UgEGpiHOUPw9hYgXjDjbBakazxZLCQgjEc0rMywEi9fFKNuC3A1ggBT28YnRgzz7dc3fVS71wOd8jnftInzuBusyL1gT5PTtJMz4a52_hdOnyZlNVJa6HrkVNTOVihWIl-_49o9MGZwhkwo_FinzpDy8_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس با مدیربرنامه های سید پیام نیازمند برای تمدید قرارداد این‌بازیکن 31 ساله به مدت 2+1 سال به توافق‌کامل‌رسیده‌است و باشگاه قصد داره بزودی قرارداد دروازه بان ملی پوش خود را تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/30978" target="_blank">📅 19:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30977">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPwdEptZRWa9oGTgr8KyPMIB3xsZzJuGxiCASxfgTXwZ4sL1ITpvupCbtdqWjNuxfcbh3VeOH0kMtuDZN3gQXbs_rhaAZq30iOTW0kCTgR_x5vIR7cbZfokFx19NgHMxGljDQXwo6KSmk1rrbB1RbLKPU4maeUxUly-XmlymfBCD7uv1LZIj1S58Gp69dZ3zvbKkkk9OZpLRugrnH5ijT82IyQhYI1H6q8TPtnglKgWs8mMQDjaAOEduDwQEftWMF5Y4QU0rIKrk76uk2ibdMH3KGyE8Qjqua89BvHqTEUmAornNY-SWRFfvqOvbAlYezr-14Q-KlqX2ue2kylRpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/30977" target="_blank">📅 19:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30976">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30976" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30975">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITq5pSosaJXmV5Ef9FDxFk43vunUS_qIUSnum9zdsay1mcB03J529-Uzajd-Xj170h9hfNoYN_JMARMCgnoUYphccJ2U7Gb3kv1VOd3MnFn1vwlJj523NgJkR9qgquqappvSJe24P3Q1Oz8B_-OZXmxE-0QDec6dQ6EZGlRPRSTAfU_6CwNdPPmPcuXFOkYutIWMFfW3DdyzXD8zm6fvTacNnWi8UVYT_4rirCqu-0jAetfFYkLNXg4GOcZht8pGQ-xL4I7nwSn81e3fRb4fqFOTldhWfVFyvTimXEnU6b36sIFsMCRNMLO4iIYvEynnEBWc81csA3ThMNITvuvUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی بازی‌های آسیایی 2026 ناگویا؛ چین با اقتدار در این مسابقات اول شد. ایران هم ششم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30975" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30974">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUp_jHOrWH38QnQXU69uPJJhDKbH39yxbvALx1DEk94Vs7TGHxCRPcjhTJNiKcfoRGRh1iou_QlKCoZ_dAMws7Y1q7vL0HQFBFo44n78SL2oa4UqUPM2q9g-4aejddFUGWTudizq4zG730l4VEKEKBjb6imt1T6bP14meEqFjJOlL6BzSPc-QkKzpL3qEXxl6UMJ7vJCtTypGCC2w7-fjEP-k7GxKac3443saPFGHiZkHjPYKqdWZY7LBcI1MClRD50p_Wn_RnWRas7N64UQBUbJ7XIg58ZuQO1N8LHdQIxMfokiAKJLhhguoK5QDIxCpwneVKMyav4Mx1bZJEZLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/30974" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30973">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cREZCqqV-tjLoMWCy7JwBj5K8ccX5VOeBFrC7P4GBCvQ_pQ2PY14MxtBYwxmjEaL9s0RbjFLpHCLFzHBRvYjzzwfrVXWLdpkTOL5Ob7RTWyyFPh_a-PA-0H36JNomfSEr8C1aZrT15HaG9hmo0B46rks0LqA6wWg8qvmFFRraR-pjV3pqECSb6KCILRDgJy3s33ccG3s8I8NOR2zJytBEYUGaoBXNlM_VfN-kMhPVrC1m4Mk8xnND-e_qocHkqdE0QeKPI9H5XGtC5v6t9exnFVQDYf54Gw-jcmsSGM6q2ngV681nvszGIkHFcmF42vKjnEBdV2kAInoDoQ5gcVUlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30973" target="_blank">📅 18:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30972">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30972" target="_blank">📅 18:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30971">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4mUBmP8ie7RqpzHPNJ39oRmutiQ68ZmE8raTpHoIvb764NK50O0WG-t7J-kE1zSblBGzQgiAVoWzrBSHWEvySHiged0XZCtjvvDd5PBOSx2G2N0waDUyxJ8T38JqQYatEnxr_ZXuUGQwX3pyWx7LMA4EsPZgjgIhzKKMdq-9UR4FViiLjMqQ7Y2C6g38zOTTUEET_t-QAbdfVpofpmRHY6camnwG0mDJ3VuBO1wyeM_bQzbS3ltLf8Kl1kKykNui1Hlil6IL1DnYcLjdrjgI5uaK0bFT9uT85PqBB6Xm9Y_smGwpMUH1uioXe_F_VZqAbD5Rl8rN55ZqvR4ABbnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از شکست شب گذشته دهوک در لیگ عراق؛ مدیریت این باشگاه عراقی تصمیم نهایی خود را برای قطع همکاری با یحیی‌گلمحمدی گرفته اند و نهایتا یک بازی دیگر به او فرصت خواهند داد. یحیی رو بزودی در لیگ برتر و یک باشگاه بزرگ خواهیم دید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30971" target="_blank">📅 17:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30970">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZhVln3dffPBTfjiKx4oM-VycafFHK_JHMadMVTFkO9HwigEsr4GW19cj6uTBEZNtsT9GtwKeTUXf911kytxozULQFmUqQTsUrO7oYUE70QWduze6Kn0gai84rZ6PAG1XtQPpwzs_jwAyIO7cqX8pt_C6egEmqY5hXh5rjwUx2EplBlf7DfdS6kOFmY0CRoc4a4SlMR7clw4_ipew_ewd3ywLj7BrcCzuuhR-HKdxsZkB1B2cWnDf0NDrVG6I3_88xH5R4QWjlOcqxGlV9bhxN3Q8LGXJkbufP5xHAh7hR9BmHfTjDCXjSoJnhzKTGipcPWqbFMWUK6DKvgG_gEvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارتینلی ستاره الهلال در مراسمی که اخیرا برای پزشکان در عربستان گرفته شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30970" target="_blank">📅 17:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30969">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4UZm1qUYSNbTW8BtxBfOi7MVi_7hV53PPG-u9L6z65UnaVu6dOfEpVfUrRkhMrhc5a65gr7aAT3k9ZwLmLM0etF0YZVLojLZ-8xOlpNmPpeChW6O57GqYd52k8gNkbnjBUKzCOqzVM5oCiTgA0_E1_YrE98oc8kp-aQ9BL5XNK-Z4E_XRTmyl0DDkqFhew3gv6opR5SUZpkcf-qqZk4GIMMphW3EtBEYp8fktjrxEZOhWzI8lch0mR_MVc6Y9keqRJ4QEQl_qaA2qXymGmUertJauxj9Mk80J2R0iqLmZyfv20UpbNjEFy0HL3gd4T4cCs-2sA0OyvKfg70KdxsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30969" target="_blank">📅 17:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30968">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNj-frW71SkMrBBebiceMYHMpPN1G5897xLEr3A2fgXZH-VqSEIgkvnvSidFBYhS4Sge2xCmabEJ_76G6auU3YQE-jePDlkHBQMLXHBK2ZX718CRxQCgH4yLIKOLc_5YkGTU-x7KNeXP5nD4gfiduW6wG_SyO0GvwiDkQQnqCJgTXDauEqhllnWVYalCsVEyfVdPx55aiZEBNE6gv7K7DABUBbiA_7snem_1JTcASCgCySuoXu9SM5ojcFfLYYs9JitIJzDGZJC96yHKDTLSEUuA4p-5Es23lHy4xUXbSpw-rShLRUMLMo9azCYkkM42XMtno9EWiIBrt0KoGkKAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30968" target="_blank">📅 16:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30967">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv81zs23J0uuR71pixyNkuhO65hYLznU8Q1n-ivbJxxhsg4riuTFPo6A9xgyt7bUwh3OUGWh6SJRiaFpzK9wN4d4oqnnjfda6oNSd7bQJMtywoLKZTIGM2zHiTTZuGwnq9s5pHBz6OzL8ApqYeBZhXAul5XTJEXKMGcMutJseDUX-bZY-GhFoo0zw0ppnFGr5AZlzOfa3BPrdMHOAY5K5_UQ0AdQOC5sRB4DbzkxTuf8zhEhhQjlRWgqiYEQET3ltw9HdJg5LMMp_tnvoLW74KuiHn1EV4hRLizgBeuePkMjuwzwFiU-d7fUwLl0X1kIeD0ikyp_-mFvu9cH2nCQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فدراسیون‌پرتغال‌میخواد این هفته یک جلسه با کریس رونالدو و خورخه ژسوس برگزار کنه و مانع‌خدافظی کریس رونالدو از تیم‌ملی بشه. البته خیلی بعیده رونالدو در جلسه حضور پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30967" target="_blank">📅 16:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30966">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30966" target="_blank">📅 16:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30965">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFB3eiMf1H5s4Yeq1JcA2pJY5w58H8unsEtfuJ4BpRq-oVidQ6L2vk756d5f1eo76YDt53pslXZd6MHUcX2RojwyGWZ264jc_-Tl27d6lhc5Fr3HTAcGUJpe8NNPUW-GyuDGqr1TyzYnPKQsc0YSbDgQ4caLbVQZm7vEM9TYcSWh6wV-9l3IArghGnvvLIUORte8Jr1K5NQ1Z3XclVjzbJiIqJYqROOhdX6LuJ4dqcsrZyNGf6ARWjGqeKFVV5e5WuSCepNEcgSfPRujk2W4pn9WMO-q2wQw1AMita4XBby6SxI15LrDw88T0_NePxGY-ezEpKSnWHoFSYJSnRl8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسین نژاد در گفتگو با روزنامه همشهری: باشگاه استقلال رضایت نامه‌ام رو از باشگاه ماخاچ قلعه روسیه بگیرد در نیم فصل با این تیم میبندم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30965" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30963">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLHJODTTLPweNs2x0o578ZELBV9L_qDiq6tdic8hXgcMdp2Zmzho7pKnEv8kgINSMVB0mQojASywwYjufZNGM6UJM1-BoG2egUdh7MAnneIqY-M0LTPXiO5iJ_dMtLYMQSKzVLsCGJRHhuUnX8fOWUT-YYLXLpAVdpt6NRgCjStKuUBiHdVM8XU8BVJG35od5zCALEKuNN6dpXk5WJneh2xUYtb7juebjEJIso72E7yJDyPNIuI6mffGHa2jZFR_h-lgUzJ1aIxQ_nNTURGeGUJ7G5zxyBp8lZTKvANaWakr2-ibWqULqQC_-wodwYwt0MVPjMDeXYAuzGt2ENwyJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHHioIv-rn1MRCcya4XrQpvdE3sZsL3UgYTMjRcZKaAmwG9DoeL87yA1hBKaIw_MykENxZ1KfvSw1Bf1DUesqP2O6ZFW_0PsnR1W8n2Yu_qUVPFD-kuH6r4EysL2ewu9ocWNzbO7ByW-0dsubxjPbWYpZ6lqBHGnaV_yY8Sxqql5f-EDumyWbuOEe9ZYglb3jho6fWeHP6uLv-5U2wjBuO5rEg8euxXpuO5xHa0lyJvmcfRAIl3k3Qp07iMVIWAn6eBone8iBmAZ0rGQTzSsIZOM8YW8pQiySXsc4c-sUGnLimPoVrtJjORBz0w8JR0F7WUgSb_By1c4LitFG5IGPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30963" target="_blank">📅 15:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30962">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N74II5e_NUp12hZVNuNS5PD0k4vDaGP8BC6gsa68WDOGM3QAH47JgbJvbqj6CuZJ95gJEcAM3IPXy1WR19AZD8IBVyuq3OasYAAys8MSX1QbaG26ySlnkrUChEbXNXaBlB1lXhUJTYuwsEayVaZk0Klh8SSbCkuPwPY8e3lrg5DE3CqnK4cMVQPJRsArsdxnOUWWNewgeyXwto5tY12C0LnLyb-EXtNz1xZky_z3VyKg4G0hey7pnBFBqxydGsS5pxFoV3K-LVKLOuf50RbTOWXuL0famiRpXVcJxHnrekkZagSOIMzZWGbvDpBhECls7KmwtZRFJwmwaO08uPQxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30962" target="_blank">📅 14:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30961">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=iY5Fx7CO2OBO1EuMX0kagDeUprA7p33IrKWXg8dT3U7ln6etXcyKZHkKv6GD81HLgkn4pLSl6gUSc0_ONyShk-7iS8M8wDa1lYVTvyLy6wLSSTClZvsUSTiCUTfIEd0qF7Qx50jUhIFw45-JRV_3jRsNZMwn0GKEXxmLz6Hz9raSBoI7IGGNppBZzT4cf2d5fRzsHqbh1ogziPeak-KJu5M00edokaCPcIaqaMnBfMoknbc4gjan9aSpWGXLsTjM-YzahZ8RYLXJMsJ6XmVFC0SpOP1ydn0tdPVgH7UXLoUBXWTflwn_b3X4a-v5swAXC3Wx2fMPhiGMDkmnjF0qCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=iY5Fx7CO2OBO1EuMX0kagDeUprA7p33IrKWXg8dT3U7ln6etXcyKZHkKv6GD81HLgkn4pLSl6gUSc0_ONyShk-7iS8M8wDa1lYVTvyLy6wLSSTClZvsUSTiCUTfIEd0qF7Qx50jUhIFw45-JRV_3jRsNZMwn0GKEXxmLz6Hz9raSBoI7IGGNppBZzT4cf2d5fRzsHqbh1ogziPeak-KJu5M00edokaCPcIaqaMnBfMoknbc4gjan9aSpWGXLsTjM-YzahZ8RYLXJMsJ6XmVFC0SpOP1ydn0tdPVgH7UXLoUBXWTflwn_b3X4a-v5swAXC3Wx2fMPhiGMDkmnjF0qCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30961" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30960">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1iACx-3Ngjs1wApMBeE4AQ1ulkX_bUVxANH6E7Sku9dJTbmQ17fk8b7xaEpvQItBRGgdYfbQFrXTeNUfrGlTAkzHUqGaptpIkkZSkJSNTYt5_Iuoojag-U4vLqvCV-SM82Q9akp62rm4rtPIsSCW4IJ7tW-Cgst6M4dkWTMqhZHdkzY1cBs3EtOLlavSUY6-reJlNjwrBraq8B--2gWKjr5fiN1Vib-a81Wdoymv35FTGgoyvrvKruiQaBo3DMcB2YHk2JB8RDO79IUglj_wwTo-UCNfIK9jhO2JwT79lMoEjNRFH1ZxJjhSVVviYNAKsiv5w9sKwJBt0El7PTM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با منتفی شدن بازی تدارکاتی سوم تیم‌ ملی ایران، هفته هشتم لیگ‌ بدون تغییر و طبق برنامه از پیش اعلام شده از شانزده مهرماه آغاز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30960" target="_blank">📅 14:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30959">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZKBQRrw7L1zCqzOAd06UcpQIj2ysztBmpPxo1Qop-QzXkRw226MKmG043HTrwA7QT47oNueJCOuSlaMyHGyHzm9nv6KvSpcs07Wah0Twqkcctm3elPAoQQ6srfpanwNKqTerPROssffyt28TFOLBwUGg7n_9UonvE9cbaBLTuzHC822v80hYPz3YKUQ6ltHGguBMck9LXswE2F0UKCDetKci_6ttbbzIKtiHAQrAags6pKgZjfFwMO8ytbtaKi1mNWVWrbRemlSfSwEUQzdAZnHODGSmh5SsLo2ncUdIW5Wm-fCCG0ynE12_LO4QvCLVylvMIOXcRYdDVi2M-zAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30959" target="_blank">📅 14:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30958">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhc8gPV3Lab_mlwEtq-pW3RNaS8ZGOAnNaUzEFp1jeImsJPgzvoYNiEagx4cxNCRtaGwvvdwlkTYYbpPclMBSaHidUbnoyBJ14tO4ga1B3gndATyqa1ks4j3fUCYZbb-vkprcpkmKdIXWrJts-ZlMWXATodALN47OgYf4WZT7BAw-8ajssmAYFFjrBkh0XH3at_xAwWMjz00PD1-VLC1eHPQDvoTRKsNjgl1AyztRXCNPcmvkUz3hKF55eK1uLG5OSeODgkR3jxw16KiBWtD8AfJCU_5afkvSMvp4_Fh_ZvF5n2l3GS9QmbLHvpXDp0Gz4MBLZwFTxFXEh7zFux8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30958" target="_blank">📅 12:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30957">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=XuyADo5GkqtgH4TflZfrCXsWMhb8AT1GCg4Yn2Moci_HQdwKM1-aLPhqnvl-MDsza2GQHmXXXrqKDp0WFpCI_fLdSorKuGD8f5CxVaar9IbZcUehY9_kGK4LJu6hs9gWOlkzWNBrmkR9s-2NH_56XCkfSgOB9pGqQ-5dVtDZinM9MghpX3x8Tz3rmj8Z1pYObeeiktErBoVTswfy8W7HerTdMBimy-266SQTlhQC_KCUfDkgIUxpvZXc0janwHQMdL19EPOKGfXhVz-h4ttOggJwQ7Hif0juNReoYKCMmkwfJfMwQglteZrg2hhf8CqwmcuZw9EADfIQLt-7O38F0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=XuyADo5GkqtgH4TflZfrCXsWMhb8AT1GCg4Yn2Moci_HQdwKM1-aLPhqnvl-MDsza2GQHmXXXrqKDp0WFpCI_fLdSorKuGD8f5CxVaar9IbZcUehY9_kGK4LJu6hs9gWOlkzWNBrmkR9s-2NH_56XCkfSgOB9pGqQ-5dVtDZinM9MghpX3x8Tz3rmj8Z1pYObeeiktErBoVTswfy8W7HerTdMBimy-266SQTlhQC_KCUfDkgIUxpvZXc0janwHQMdL19EPOKGfXhVz-h4ttOggJwQ7Hif0juNReoYKCMmkwfJfMwQglteZrg2hhf8CqwmcuZw9EADfIQLt-7O38F0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
زیباجوی عزیزمون با این وضعیت بازی مقابل تیم‌قدرتمندهندهفتگی‌حدود180 میلیارد تومن درآمد داره. انگار وینیسیوس واقعی رو کشتن تموم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30957" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30956">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2LeEJnGbGUdBLVwrLB4wIbqThFNZr9F3lmjU_7-DuR55FJZjjEoBWokSEYZ0RPKzTVHbqXJujfInwjxQqEAAGaaAgoBQTDfUhM4NLVCBRXlF8GPuJYfeCqRIl3mm6Qcnqs9gykX8VkQJyuyL6BXRnbmfs-Bi7ZYpY__HYyyyw0KVLQfes4yxpu4iXi2mzJn79VqqV1sACo2nUNFpq--UoBwnvwOwekjagESA2X7l2MH86ExiaOb4XsLrTwlivzqfZBf_4lTtqy--YpcU_foM3qZ-_EybvC0Ii0nBXxjnlGQfyuF5stjs__Xnoiq0uX3GU8PpQQDaExbVMH-xzxGPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ در صورت موافقت امیر قلعه‌نویی تیم‌ ملی روز سه‌شنبه ۱۴ مهرماه در استادیوم یادگار تبریز به‌‌ مصاف تیم ملی گینه بیسائو میره و بدین‌ ترتیب مسابقه تراکتور و استقلال لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30956" target="_blank">📅 11:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30955">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3QODHj_ZoQc46AK5c5-Z3kGLTio9gyqFubdXXcwkeh8DuVKLbWcjmRTwJfsYHeiYpNj6OAUaess7naUotsJGqHT1JDheT-WAxgAcZe40WVT3zttEldPtbOpHn0YYlnLlgeR8gOppNK_c6Gm2Is6qiSx5hmJydrBX427u5ZSLjNUiGOjmBZWF_r8OJrnk2OgjMtOeZKLMpSZ2-9oO25AA-JO1duQXvVUbzukfIcsXmPEWMGWE8KI2MjKr0eLVovN_ZINL9IMDXj-797XE8VtpJOwb766TlCMF5kEIQ3CUkaAhLzhFUaWS0DVJdB57FdYI1AmEf6kUc-LiR829wWVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30955" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30954">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56284423e.mp4?token=A1ijedLF5s7emhclz3uwVDsck-WageyRIPdVhD0-Wm0jcfgF8Cj751k9-uaEEHp0vvpQbkkdUhT6B170Tw9gkm9MJxBzSSKH4tyy-_C3thRF4l7e16KA5H4-ftvisFvvJTNQQADtHtfCPTi7XmJhvLnbhMvdLB-tfJrkdev2xRwcXpzcSYqbAzEX7n3xxnRg30VlFEOSPrq2jLxlpE9lgbWHOvUsjuB89zTf6f4-Vh31Zg_-mNf0W5r1zQzzcjpha86FkLKTPM8-5TSUqza44o1nBgFIaHKfn0mXUQGvJRk_JJos6FT9woZU5ZiYFFPjqToarvXm92Ciimx5ofGo4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56284423e.mp4?token=A1ijedLF5s7emhclz3uwVDsck-WageyRIPdVhD0-Wm0jcfgF8Cj751k9-uaEEHp0vvpQbkkdUhT6B170Tw9gkm9MJxBzSSKH4tyy-_C3thRF4l7e16KA5H4-ftvisFvvJTNQQADtHtfCPTi7XmJhvLnbhMvdLB-tfJrkdev2xRwcXpzcSYqbAzEX7n3xxnRg30VlFEOSPrq2jLxlpE9lgbWHOvUsjuB89zTf6f4-Vh31Zg_-mNf0W5r1zQzzcjpha86FkLKTPM8-5TSUqza44o1nBgFIaHKfn0mXUQGvJRk_JJos6FT9woZU5ZiYFFPjqToarvXm92Ciimx5ofGo4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از سوپرگل پشم ریزون ستاره‌های فوتبال درمستطیل سبز؛ گل‌هایی زده شد که هم‌تیمی هاشون هم برگاشون ریخت. عالی بود واقعا. از دستش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30954" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30953">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMmeRWpJkyyitGbAGFnlCpOrwcw-HJRv3UjZxwgsqProI6rQlCyHjjzwgG2KYbFlh1nLSf7kNIPXQpkmWOPfL-5VvYosfG_F9Ryd9W_adpBMKWchMMLM928qB0SeFwqOU5W-Q90euPqMMlyZeOGYd21mOByUt4fwaDoN-FNdN9zmCkEYJsKTijL8e4Bk0Wc79uk1q54K7-t2QsljxDjgRWQBd-PbZvr4b6vfit1dpQO_xTE2qMdWZs_vazYDv6FFQTjTmKK1C_9955NKnEsevHJ-_uHeuAgw4KjHmkVsQrbHMtrPWvfYgBT0uVHb2rPTlz67mZQVFiGY6Kd_-Xv0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اگه دیشب داخل کانال بت ما بودی می‌فهمیدی چرا همه  دارن درباره‌ش حرف میزنن
😂
🔥
😃
تحلیل‌های جدید  امشب
سیف تر و آنالیز شده تر از دیشبه
😃
♨️
آرون تیپ=
وین
⚽️
✅
💵
😍
فقط یه کلیک فاصله با وین داری؛ بیا خودت ببین
👇
😃
JOIN
JOIN JOIN JOIN
😃
JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30953" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30952">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=uhhHWsY5--ETzL6ajfwQFQz3hFIbGZplBXry548DYlBwrPmge4sUhbRxy4QZvTnUub55C1vNI_lfn0nVrWlGqqYI9_cVpLElgC2n-N-lwlHStF7tfq5mdPa2cF6qkF-59T-xcwhnBWmRP058IRJrERBE3xSPWSj-zgDwgJz_Vy9dAh93wR66S1P4gt-XSGJZTYaf4e_pJRC_fg3xd0dAfH6fi7aFMWbNEnUI9eZcba-iFmbzh6xxXGI79x7aS5zma4lQ9z4GAR1tcizdGva7sQmRtnla0QUtl1Tzk-80USiXO2fMGH1co3d0oUueIQEZWD-Gnk2ZAcSyNqE3knS4ZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=uhhHWsY5--ETzL6ajfwQFQz3hFIbGZplBXry548DYlBwrPmge4sUhbRxy4QZvTnUub55C1vNI_lfn0nVrWlGqqYI9_cVpLElgC2n-N-lwlHStF7tfq5mdPa2cF6qkF-59T-xcwhnBWmRP058IRJrERBE3xSPWSj-zgDwgJz_Vy9dAh93wR66S1P4gt-XSGJZTYaf4e_pJRC_fg3xd0dAfH6fi7aFMWbNEnUI9eZcba-iFmbzh6xxXGI79x7aS5zma4lQ9z4GAR1tcizdGva7sQmRtnla0QUtl1Tzk-80USiXO2fMGH1co3d0oUueIQEZWD-Gnk2ZAcSyNqE3knS4ZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30952" target="_blank">📅 10:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30951">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=tbDaM8iZzbC93CK0RxfPPSOkrYZYedU5tx9WNYAMisS2C1DSrrtdecvbX5d-Ni2zQOKIv9YR5sxHUx2KMTlaKkcHNPTolpyjhS-5DIJ9Ewf2IpusEGOViYcW2BHAGrOIoyPKt-139Vtp0j4MBr-Orx4RwKJ1k-BEGvrOBbfR4PVUAkrsaezqpesNtujIzNk6m5MSLPcATHsynQ89e_2yqHUlyoSItUs6s4f1HWo7OfbhRVqxzGpyiCVTy-VQe2aeGtL2gmFKdyDqqHqfaJ8Xyf4SZMikgvffc1SSpSMjlnAQHMc7H1P_sz7JrgzdDhNis3HImLaV47XlVaBefGgEKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=tbDaM8iZzbC93CK0RxfPPSOkrYZYedU5tx9WNYAMisS2C1DSrrtdecvbX5d-Ni2zQOKIv9YR5sxHUx2KMTlaKkcHNPTolpyjhS-5DIJ9Ewf2IpusEGOViYcW2BHAGrOIoyPKt-139Vtp0j4MBr-Orx4RwKJ1k-BEGvrOBbfR4PVUAkrsaezqpesNtujIzNk6m5MSLPcATHsynQ89e_2yqHUlyoSItUs6s4f1HWo7OfbhRVqxzGpyiCVTy-VQe2aeGtL2gmFKdyDqqHqfaJ8Xyf4SZMikgvffc1SSpSMjlnAQHMc7H1P_sz7JrgzdDhNis3HImLaV47XlVaBefGgEKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30951" target="_blank">📅 10:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30950">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=WbCvssN0mBItn8aC2SupPNKIzqRl9S0I7rClqGJt_zpG8cvy4Q2SCo3G5547R9L21N7sf1VlETEpOspViOEqn4m9neghBBObjhHqRmO7Y14-wsV5p-kC0qbaVrgfDxtXB2bmvXQW_w9GoFB23Wr5-K8N2lykTKMsN2RFtONzCF1koNbL2i9G5HXQFpbfvr8_hgix4f24kmULuqrm-Tu1g8Tys9x4XaN-qQQi9Yx2aBEHDSNFlK9KiEPylwPBOTBnlPl6g1Ox4x0hmOcekJqvwYjkTYU4OgKJbWNkCQ7-klO86BewNTuURanIs8NxzdnGDuZwD0Ukc7DQCS_qWM-Qjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=WbCvssN0mBItn8aC2SupPNKIzqRl9S0I7rClqGJt_zpG8cvy4Q2SCo3G5547R9L21N7sf1VlETEpOspViOEqn4m9neghBBObjhHqRmO7Y14-wsV5p-kC0qbaVrgfDxtXB2bmvXQW_w9GoFB23Wr5-K8N2lykTKMsN2RFtONzCF1koNbL2i9G5HXQFpbfvr8_hgix4f24kmULuqrm-Tu1g8Tys9x4XaN-qQQi9Yx2aBEHDSNFlK9KiEPylwPBOTBnlPl6g1Ox4x0hmOcekJqvwYjkTYU4OgKJbWNkCQ7-klO86BewNTuURanIs8NxzdnGDuZwD0Ukc7DQCS_qWM-Qjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون یارو مجری بیهوده یادتونه که چقدر راجب فیلم عروسی سعید کریمی بازیکن سابق ملوان گوه خوری میکرد؟! دم‌ از شرم و حیا میزد! حالا در نبرد دیروز تکواندو این الفاظ مثبت هیجده بکار برد!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30950" target="_blank">📅 09:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30949">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arXxxhZZ-Qtaw9jtFMwJNbh8-PcUbBT2dMf_gVkMCP9140gXCVg3FnXXTgCS9AB7T9oG_TMU6wdhucag2WINcyQNFNNwsX6rPrgyZe4qDrfkhBT8JpoUWI6eajMwSiJKppqd6jtOdsx7Y3yGrCTJPPhjtS25ymVP8CZUS31tRuLHGiZuaoaohd7n_CAMRueQpXoblqXPYqMnR9eVr7DTIsrBKiLFShXZa5x0uo0UfNqs2nhW-FtAZrb5DoYnYYlqUY6snVZCgH_7yQ64-W5fNTzMytDAzUJEgoiIye1bnhZ4GZH-iV4UpSCIUN9SfZtFqnj6n54pTsho8y4fE0JW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای خبرنگار لیگ برتر: یه خانوم در کمیته اخلاق اعتراف کرده که با رابطه جنسی با چندین داور، برخی از نتایج فوتبال ایران رو تغییر داده!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30949" target="_blank">📅 09:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30948">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRKMQs7sybcyzx9SoXw_53rv8mqftwiEpt3KioWdpWDaJQ8Cjly7oyliOS8DmLyZB3y-DI4V5FBSmnGkOKs4CmpIMXloHTsRc8N0wb0AWcHkVD-TbyOPXJVrhfzsph5a8njIIwnOBgDj-38-iWqcKeOtLA63hg9uPU_lGNMWh2KYDyNoH2DaQu0ZWdBH24G8r-L-k4X1tcB5kLlltLgwbCeTOqmWd1BSQVuWin1kofVE_HU44nc_S0hAI7exlwTHUs5F9ZH2pbuf1gUhk2tqmFQKp9gytjY9WwUWtDNqpQDVk0R8A0jsruunwsJR2nVXCGZmSqyQ70ff8uE6dwphig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30948" target="_blank">📅 09:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30947">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzO-7KupaXH1IaXYelWFy5wcUtzuOMQiD1-N_TNyJf0mDmF2ryLSACG4-jld6LRjf4QM7d3szHCDxlOKE_cZcrR7ySJP5rITnNQE_TYRtXfds3OqCdGzIlaAnvKliXS19oUI1ULu2qgFkfmU-VKtALF-OZRCAq8brJ6eazRfX7378ZmlvyIlnO8yfKMZfrXV-UjECoCHmSszeIqC-fqO0twhFQBxKb-BjP7ZWfj-T_S7r2KGN707zfDttOM-Ezz2W8jd4OUCyj9E-tCic8SYiGzMAPQ-yECA7dc3jLu4nRa5O_rd_6oVn2wfkmlVokrtlVwChCwH0ZUADczJv5-rpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه روز پانزدهم "پایانی" مسابقه تنها نماینده باقیمانده ایران در بازی‌های آسیایی 2026 ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30947" target="_blank">📅 09:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30945">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOzjIaVqEZEy2h4LgavWQpI8gSAVIP_SeU91I_ESpcuw4yctuhqZusPaHE5iTGBwTXDsKD-kuq7d5TVQHE5eoHBacBJkp6B1AC5FLNzp_NR-yeQK4kNwqy-EqMaDiARGBfqL54Y0Srxjx0nrlA-tqtp9Q8xXxozwtFMM_LByBHHNhFP7W7ogmBad4wlO68w9HlT1ecF3vgTK9kKTgkNXgV_9ICeWVxL9UJ1V3lKz9ti1XG96ID_cYGQhnSFchNvNL8cSc10iwEZ-nHdoecKDnTpF5mpJS7Gmcgs3UkgcEAFCR0NhAMeyxu_1kYtuN9R3aT1vbSkVv9FDrxFN47zjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز
؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30945" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30944">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdrxEWlEQjJLx3T17tIburpaeR44czwt788_9SDp3njFANDdyp5LW8f9gbOKdMck6xgw0t530BZCJMSI7q6vXBBYN9FT3Tyu_NtFNkrCU5lKLseOmoaY9FxFUPk4yTHL8yLv-bKlaSTjclLRRbJKm8Cfh8XAgC2e-T7oF_P3sW9e9gijyU0Y0egG3Cnhpw9vgFRBc6JDV-JhGKYtZkK7sw-UiN3TX8h4PlmqkecpsBN7H0SWEJmauUCNue_3vxtNJ4JGfgq9GReGL6SkC-OaNpYAe2ChwevnGiDOhrbHuTz4yRsOng6cLnQFX5VA5dBwNKey9FZim5K3mNjsNkRggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
تحقیرکرواسی‌بدست یاران توخل و ادامه روند فوق‌العاده اسپانیا با دلافوئنته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30944" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30942">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=u-5X3xtiq3MEsKmUq1GMFCy_rCLWmnBb3gcC97BF8EnHzBSyyOT-2f4jRrAf52hj0FinxP2Bjs_YmDxaFnsFsqtMphxuuRFkNMIoVC55-aP1pey6F5D8sg68TMiXgPA7a8NCeDCRmxEONpIf6peExVVAyqHWIZzCuXysgS-9XvcW2h6og1Yz4eUE5XKhVv0zLQsToesux1cwMGfiGcuyF_EmJT7IAUolyFyh1sqqgd3ZL7VmZe_4nM5zpJQZiPqsLhFpLSDkrkQvSSTxjPbJkL-AoLB0QR8zPdv3P9emT81zT2vsy9ksZYpsrBotCsVR8BD9i_jr2U5M0wSglGu9Cr1wll9mWge2aT_wxfqjfBwqsn82UgJHPfd3fZDJsu8NKc_EYNAdl5NbgSHiLjBDy46QIgOByvzLFCX5AoQpFI_zquRMRt8ZpYTuszqvxp_9T0r8j3obh7aATXIWC6zzs6UajW72M6oJoJhqPc2nRyDdkV1ml82F89HL83yQX2jvGyGOaH959GtmYvhEdV3dJ7JnXxEtZPTU084wWt6-0Eg3CO3ucijaRxUV02jnFeu9ctZ2Y776DRphjj7ESx7-NGFAq_RFP_ijsu8iYTWQPP1k4zovLoBuJaBrRxD8j9Sn0qPFGEPNIj5eX4HWEmgP17l1EenRVq_-bbydmdqeodg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=u-5X3xtiq3MEsKmUq1GMFCy_rCLWmnBb3gcC97BF8EnHzBSyyOT-2f4jRrAf52hj0FinxP2Bjs_YmDxaFnsFsqtMphxuuRFkNMIoVC55-aP1pey6F5D8sg68TMiXgPA7a8NCeDCRmxEONpIf6peExVVAyqHWIZzCuXysgS-9XvcW2h6og1Yz4eUE5XKhVv0zLQsToesux1cwMGfiGcuyF_EmJT7IAUolyFyh1sqqgd3ZL7VmZe_4nM5zpJQZiPqsLhFpLSDkrkQvSSTxjPbJkL-AoLB0QR8zPdv3P9emT81zT2vsy9ksZYpsrBotCsVR8BD9i_jr2U5M0wSglGu9Cr1wll9mWge2aT_wxfqjfBwqsn82UgJHPfd3fZDJsu8NKc_EYNAdl5NbgSHiLjBDy46QIgOByvzLFCX5AoQpFI_zquRMRt8ZpYTuszqvxp_9T0r8j3obh7aATXIWC6zzs6UajW72M6oJoJhqPc2nRyDdkV1ml82F89HL83yQX2jvGyGOaH959GtmYvhEdV3dJ7JnXxEtZPTU084wWt6-0Eg3CO3ucijaRxUV02jnFeu9ctZ2Y776DRphjj7ESx7-NGFAq_RFP_ijsu8iYTWQPP1k4zovLoBuJaBrRxD8j9Sn0qPFGEPNIj5eX4HWEmgP17l1EenRVq_-bbydmdqeodg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30942" target="_blank">📅 00:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30941">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpSd2J0ws4dd8PBoHiCl6bNtdadgu2lhIvR1sLyMtZN62k8QuI89mx1pdUlIJLJQi5ff4l7dKO_QYqtEWpAjw2WtyEwDWcHYh_hBdumcG5wmcb_gX4B3G3HIgs4h-u9rPSk3eMh0ElgvMuhArxwcagGGmecPCNt8vqvTxy2etQ_GrZZKh2dLACxTqrZrbXD6z16o0M6dNJ2BwKM_VXz6bXhFnVk914kPE3xtyh5YP2oF4VSmg8_XRnQoN3N6BgyM8Iayq6GyBTA3GUVfYF07frZDVo8He5LYxgZqjufBpAQRubVoaF8-P10rPjUAWvgVKdyUs3cgntACS8Rm1dkrvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌‌سوم لیگ ملت‌های اروپا؛ لاروخا در شب درخشش‌لامین‌یامال و گلزنی‌رودری با نتیجه قاطعانه سه بر یک از سد تیم ملی جمهوری چک گذشت.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30941" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30940">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30940" target="_blank">📅 00:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30939">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndriu7EF4Oj_alCECxiY8n5anq4ngELcCVA-ppNoP6GgFGdSD8gEVHgWlxNNAX4BsuNyGMBMK9mQyxuXOj0a-OWcd-t_0SNGdBRjlYPrBBFfKAyXKZ0srgbhOriIIWzAHu3pK6xx78W7QuAlvR7ma3aQ79UE7zRildKdXsZ6HzMzcGz_v59SEUKUblGnFmuEgS40piIp64MVxeFBWWPXc0uQkLFHvaJXwpsvhLphWkRTMWzw8QgEhPnXawWbka9TsnIWDLP77q7MugFproanSy_IYJkRA60G9LaspNgj3BVAQOflfwcDhWuNY3eE3CJpjYakLsUb3FxVTTEloupZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30939" target="_blank">📅 00:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30938">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAPwzqAIgd041i1P7QUUIEBkF1zUd2nyQiqAdfmybX3Kuz6EOorbzZCT0df6yBsdb_KRkrVPaffTNaJSv0uSqCI-poSWuWR3esf6wIFeGHk8pO6eH66iS5BS17GsLjIs-YBDVFO_3qgNr-nLnQXB01kBU9GmigRHv3aBngQN1yGYTh2losx7vCaCrgjm8hk8NSDs-MhhXwOWV9v49O7PXYuE5GRyPMZRuDLv8tBEurU-kjdAesDdziEqjxTMa2w2okz07xdQLaTWug4nlxOVG1WnMPCwMYOdB5Fee6vxk5ZFIObbe9bEzEOzu1KXJh2000pdPI9dOrSJLxDcpn9Cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30938" target="_blank">📅 23:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30937">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRXnRhzLv_tk8EJ4gHIyZmuJF9KU1MjMVzHaYk5hcZdSgjh8k6OBFr9LN7XMMWenPUcHeA0Jxly2r_OsydIsOSJFsvwv0dzPyB0NfyDhDwsJ9MVWKH34XHpX9491tjtS07IhRsSMZG7hYuf2nsn_NKIhZYcePVl_XSc_Rg8k-GFd-iAdKo8EH9AqszA44PK-ik0axffxUCBohy51ZXCN1rNVsXFvYCnLHCkT-3mrlHOuTT3926QvEjLvyD4ZeGYMgomFrPT5h8FgtZXP13J2yZYiRbN8jALylSGtbyEEquUdB63Zj4cp3IAueLb9M7RvRkh0q-WCli8FNVLncYG4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30937" target="_blank">📅 23:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30936">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOZPZi85_AmFvkwbVQBoMZaJL2XuadslzTwgkXIJcsTbVbLLJO8Pa54hL3vXtWfFX57_nMPM23xzhgO_8fz4nKtiiWjkOZs7NbbPHYlpppaMKCUYOetbRjieLcL85osmdiNUXPkKU9xFY8JW62x911164Q-owSVJC7HQ_7hL_UmP2GePsyb-FqXkZC_XqJrvhS7o1Cu1HUGjUoarIzeCxHH7TEdDFbxCeNRNZPGzsIIRZD-P211SioYo1-NszGiQnNCgsAJDnbbd_4HrU-xrYb27uKyNSqBBYu9iJFXgXEuhsPCrNgsS58jRPLI0bi4kWKRp8OC1SuGunIuJAYgKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30936" target="_blank">📅 23:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30934">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=A8deMLu_8bpVon2HphZvBOmG-QrDsMsCbvcs1oJJS1e3ZAoh8QHMYuAst57fiWIr3K-iF52NrR5jAH5HHo9_PkGz9OciDE7VDp9mGLBfrnG42yYPk6fxKREqqReZ2lqymUMnNeh7GTiVr67e9PaI4tNZfyvKQJV78TpQ_hzGp8cQpsOEdrX5dLdYt0FHnDAYkl72hlmYWnQ3gQaQk2rEcBkWOLaQ6-f-Z6PohXZ1yxE3tx5hE3LJ-C9johmyUe-Wp-SztPU_yuzSVnPE980BlsTli3Tw0WTbDthrzEWjAbjSCStY4fF6epRn7Yi2jWC7Rm_HDI2k9m0ggx4xtOCxCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=A8deMLu_8bpVon2HphZvBOmG-QrDsMsCbvcs1oJJS1e3ZAoh8QHMYuAst57fiWIr3K-iF52NrR5jAH5HHo9_PkGz9OciDE7VDp9mGLBfrnG42yYPk6fxKREqqReZ2lqymUMnNeh7GTiVr67e9PaI4tNZfyvKQJV78TpQ_hzGp8cQpsOEdrX5dLdYt0FHnDAYkl72hlmYWnQ3gQaQk2rEcBkWOLaQ6-f-Z6PohXZ1yxE3tx5hE3LJ-C9johmyUe-Wp-SztPU_yuzSVnPE980BlsTli3Tw0WTbDthrzEWjAbjSCStY4fF6epRn7Yi2jWC7Rm_HDI2k9m0ggx4xtOCxCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30934" target="_blank">📅 22:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30933">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=M0EYhCyZt6pzBtWiIkd8e5dRrM1EzqkA4q047jwWG5s8PqJXjQGID_4wX7KBUH2aCi84lSi_thwo-2CytNPZN-YXWStNl29WTHVsbVpzm7wP8P_S4IJ8hb8lfeMx5KaQdV20LVV4TNiMlwBbmQ0ad1HL2E25lVwYuuLbbwFA7qcGktVe4PbO-ZgSBj8XvoCcEX-WIV3A7C12iTfcLnHNFqgpndcNMVzx_2X4nHQKFqigTybrrS9uG6jkj9QO6wlCjJA13w8yosBu-zOxXJdWV7ThiVr6JOC525A3-YVH4h34iOLNJuqSYPlxstjzQpI1CoVrvaKUctMqyQFa_oQ-nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=M0EYhCyZt6pzBtWiIkd8e5dRrM1EzqkA4q047jwWG5s8PqJXjQGID_4wX7KBUH2aCi84lSi_thwo-2CytNPZN-YXWStNl29WTHVsbVpzm7wP8P_S4IJ8hb8lfeMx5KaQdV20LVV4TNiMlwBbmQ0ad1HL2E25lVwYuuLbbwFA7qcGktVe4PbO-ZgSBj8XvoCcEX-WIV3A7C12iTfcLnHNFqgpndcNMVzx_2X4nHQKFqigTybrrS9uG6jkj9QO6wlCjJA13w8yosBu-zOxXJdWV7ThiVr6JOC525A3-YVH4h34iOLNJuqSYPlxstjzQpI1CoVrvaKUctMqyQFa_oQ-nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30933" target="_blank">📅 22:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30932">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnAk1PNaeEOJV_E8ibnUkNYd9izVzv9sx58-NfZ_6eBzogKWvHqNfPbSriPUPh2rfZAfFv89GCcFleTMoo2xsA7awOT_UhjTllIVJ41FgnVrf5GQOB24F4P3ww4S0PMbp5C12FHHv6e1IQ8XnvZ0C2OA8tepmZayFKbzJ8qhg59B391GD1vGmqCQ2HB67baMHgCQCk2CiC7MKKlY-anQvSObN8_FSC-9SNlDANEfcNpKkeAQqfn2Qhm0ULL70rUuj_dOrgQMJAQ8havfgpHj08_XKgTxI6K85ZOL6-GZqiud9FA5-bJ8d3cMLXiFC_qDwmcj1nPS-2ae6sV1dIGZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30932" target="_blank">📅 22:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30931">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30931" target="_blank">📅 21:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30930">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMZvK-y7k58MPCrbC6IDp2QJdcrejUsxs-Mie0JmSoJQ1m_Ak1wopKsQZBDaCv2tdNjqRlaWIaqbSNH8Tzi6ZP5jxSnbtFBQlC3nFHnFpHDO2EAxqdSzGes4DfgI8198G4Tt6Q3stnVQmf_3PG8QN8M-o5dCxlbj0HJrneLK3Jk-HQjyuT7mN_nUhM7OHorxnWIenTG_J5dYK4vhTsTfTTgMIEEj_x6UCvPvxSjso-JDtdaA7F22T_xHHhQConBkwKieYCN3E5y7MC_w8bcunSXMX6GEf8WAlHaRviZQYHe5rCaoOvDZogdQ_GtgDVurvj_EzcQq6A2ZCIWSIFYpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبرگزاری‌تابناک:گلشیفته‌فراهانی‌بازیگر سابق به زودی برمیگرده ایران‌وکارای اداریش هم انجام شده.
‼️
درروزهای‌گذشته‌آهنگساز بیژن مرتضوی به ایران بازگشته بود و رسانه‌هامدعی‌شدن که شادمهر عقیلی و معین نیز بزودی به ایران باز خواهند گشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30930" target="_blank">📅 21:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30928">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIq8P1PXDDA-dawljp2TgVDAmHpYQrBrgDmLbyy7enE0fooFe-2kwVztW0KOubLUoJiEzn_cQg9oD2vVr80aPjxbrf6OwTvQ8rTPrARMohOik1Ig6owGCqU2kWa_VvFvHb5RvY87Pdzh9QE7aE6huxwNcZB4pem3XBu_tFShieHSgaL5mlwVqs6O8YjoDEI32pYOSD5f14hrwuoBu_SkzzZw5ijrjBiTACu4WheuiVhzr786kw_dfwdgzX81Ndw8wQYxlK5TXY7CWwzvsdyaHXcOXK1KN58yOLmDIVUOa5CZ00je3JJvrYaoNwColFo8O_JpAIgrsB0AMi3Z8Ik2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8ykic6Si6m1EI6k-8i_Q_Fm-Il0rKYVBmn2KsQHjBFDQ1nvVJBuYHTzzWlQmGMucrCeBmYpnvUxq1sti_RhUNpCiyrIsX49rA2ZwGF5fA8FxgSoO8-YIZyk5p6cjXYSzghkJIPzNESDsUZ6Bjq5eqlQ56WozvetPP-cbN2uhgD2fEaOeI7InffxnKdDSk6CHG_cTGVd2AUvXNF4GXykHQNJT9jZqwnGo0Hgk1HSmogmRQQGJvngi-pwxEEn_yTw3aufT6r-lCIbzprj-8M5zaxvK8_ss2sK3UX3q7OIsKP6NTixlZ5dWQ1nTAtOZPraohrLD0azFSE8N9plIp0wiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرنگار شبکه اسپورت اسپانیا و هانده ارچل بازیگر معروف ترکیه و فن شدید منچستریونایند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30928" target="_blank">📅 21:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30927">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=BvI3UYp19x3WcY0MS7Ikbp52KuU8wsgg7t7k1m8J3scspJwYr7EAlvTHvgd-FzbKqRCgQirVxl_nuydmEPj9qJqfPAFj9G__zxFgeOQTvCUGoaPBjURbf5jWNAJ2q2N_6E6AtNWGiRyiJuISdgsLw-s-9rH2Cz60iAJIG8lPPvD30WIOfS1ai6sZdat1_0_cuKPJESv613FoTa1zErsJuNM8jkDEto_AjWt4ljkmli4AJrYvOq8-soJdD9ywz620xHGTHG83Nu0vuk3XudRSrOhMPilgEWBgPwuX_4rChJN05WHsq03qxmhWMIlRnY3eStrp6zrRqXkC_UUz8eHkkjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=BvI3UYp19x3WcY0MS7Ikbp52KuU8wsgg7t7k1m8J3scspJwYr7EAlvTHvgd-FzbKqRCgQirVxl_nuydmEPj9qJqfPAFj9G__zxFgeOQTvCUGoaPBjURbf5jWNAJ2q2N_6E6AtNWGiRyiJuISdgsLw-s-9rH2Cz60iAJIG8lPPvD30WIOfS1ai6sZdat1_0_cuKPJESv613FoTa1zErsJuNM8jkDEto_AjWt4ljkmli4AJrYvOq8-soJdD9ywz620xHGTHG83Nu0vuk3XudRSrOhMPilgEWBgPwuX_4rChJN05WHsq03qxmhWMIlRnY3eStrp6zrRqXkC_UUz8eHkkjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30927" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30926">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=gZaaEIvH871eW3JuFz-feN2tH0unHxJieJTWzDVCzAlbMbMGIT1qjU3Sbq9UtQaDtwYoyuwrqJ8Ph5PittmbGv3Gsw-PS6iF46X3wWc4PUQs4fTmFimX9B0BEgJQb1gaJLXBO0RQ4Ssx9uMoURgcaQkSZ0uS7xTKF7gTJF1A0zTrg1LmJCVu9tlC9-b6UpdVkmzcXghZGvYJkvxgrN7Xg6ghS1gqX6z_GdYd3V3ciHMMZFmKJyiX_OCDplT4CwoL-f_qHs3cIWbml8ULEAWcyIz80lt-UQZDb3Cs8rNtAm1-kVErxXR1WUbqLWg_P20cONwzUkJZVgbr-1DKY2tgDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=gZaaEIvH871eW3JuFz-feN2tH0unHxJieJTWzDVCzAlbMbMGIT1qjU3Sbq9UtQaDtwYoyuwrqJ8Ph5PittmbGv3Gsw-PS6iF46X3wWc4PUQs4fTmFimX9B0BEgJQb1gaJLXBO0RQ4Ssx9uMoURgcaQkSZ0uS7xTKF7gTJF1A0zTrg1LmJCVu9tlC9-b6UpdVkmzcXghZGvYJkvxgrN7Xg6ghS1gqX6z_GdYd3V3ciHMMZFmKJyiX_OCDplT4CwoL-f_qHs3cIWbml8ULEAWcyIz80lt-UQZDb3Cs8rNtAm1-kVErxXR1WUbqLWg_P20cONwzUkJZVgbr-1DKY2tgDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حمایت جانانه و قاطعانه فیلیپه ملو ستاره سابق تیم‌ملی از رونالدو:
یه‌تفاوت خیلی فاحش بین رفتاربازیکنان با رونالدو و رفتار بازیکنای آرژانتینی با لیونل مسی وجود داره. من‌میبینم که وقتی بازیکنان حریف مقابل رونالدو بازی می‌کنن، خیلی بیشتر بهش احترام می‌ذارن. تو پرتغال هیچ‌کس حتی به گرد پای کریستیانو رونالدو هم نمی رسه! تو نمی‌تونی بذاری بهترین بازیکن تاریخ همین‌جوری بذاره بره، انگار نه انگار که اتفاقی افتاده؛ واقعا اصلاً راه نداره!"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30926" target="_blank">📅 20:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30925">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30925" target="_blank">📅 20:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30924">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjSkZJR4bBLHw2LGzOQRHPKCUkyQ7ovjz_KS4BZuCP9kKCFOV5UmUElf4v91D50ixixkyrn2LzU1NUWpeAcsXDvCaoQcu2-UNpYcUYSE8_9XzQSTblUvgQPZjNCVvtoa51jVdCeaQU1elavwAY580BaQi-89FQZ6Sa4I8icXzQQG13Bg9s1nKKJ63EQwJTkkTh83WxHivWOroMNRZpBOIlCPnPrLF-yVo7C7uXytbI9IKRqlejy5cdf8Yz7obT58afvrtbVEWuKUG0k5cek32p53rRKnu-aD6vS6J-NT0NIjMIJpTLRo7niDRfTLLafXyOdjNsqSVRfD7UljxcIgIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برندگان مدال طلا، نقره و برنز فوتبال بازی‌ های آسیایی در 20 سال‌اخیر؛ ناکامی مطلق امید ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30924" target="_blank">📅 20:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30923">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2e3a0sCkNLdk-ThxD-mF3DInQEptEaVp2Mcnldikto6a2icTyf2_EHT5mypb40V3NgrRWITiQXatc0zi2StuJmCPj8hnnkMdTv1Iq96YqY4x7KM88G91dWQdOTU_wpdCbmJ4M964a0SdvxThR4ThWBUNCQ3lg0Zlif7VHx2lvgSLUdG7XVpZ4350d0ed4zmiak-LLqTGpE2lnwcutqcsDX0XyGi28KaX1E4DbMjN9mZ6U1GLlGDpCvEep_uJZHbCmFMYeSf-w8EJae2kyu8ULTW52-M4CP9cVz1dL6sZgAhZR2QjxDPR5RUjf8i0phNzz2Utv0XqgSZzJfwfKc7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30923" target="_blank">📅 19:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30922">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7o4P1kS_R2wSOy9uyps_d0YJ6zBUMC_1RRfPJGEMhGn_XlI2Gr-PtX59bKkKmLbeRdU_em9Yd7aTcsj5yWECuogj60YQbHywbUprvRch9MXy-vtMvPRk-mDvIRugJhYehPPpCfU58Tb-QIeBPqBuvI3o37NW0KrK2Z9Lra7L8HfDderrILIsU7W3SS-GB_LJ8DjrHYdayqMbHIYrzoep8lhdgns4QdBa_CAJ0Vy6I5tEPBm0SkcLJsVsB9XEht_GBKkoRjtq3Vil21BHK-pNFzKMwxCSgeNQ5VuO0-MTk7eY3d_6SoxrGFM0G-AeqNEGGuixfBKlyFiqDZJwUa2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30922" target="_blank">📅 19:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30920">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atB2fEfudmm36yJ7t6CM_5qevI68DX4FnA6akpwxG6DT-EW4FJMwBXJkjPyVEABJh7-gP6RDbic3ZnauNF9B1KzoAqJ6-y0f_V7Ac6ZPgLFLMV3Kua-vM49I5Xw0Ka8C8wGVsd8hKYx5aSIGmjm4fIWifEatLl7N7SuiqzJxOV8CcItyaOU3XTjxB0oVkcTsLDQfgGF6tu-IWOaa0TTxFvW_a-zDb2bqPF6olH50TDb0PeWbUpRUZgcx-RuGaMTqH3e9jYA1WNy1P-_xutcNNu4sJOYKykyxMEb-qx4MLYpPLzhM26FabwN1Z_glGwK9Pqyx1rC8-PPrVgrn3InZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KpBlM1Rm46_3aVru9uyF4X55osXFwv32j3oAoxtA5B3ptZwRrJE4eLNmrfZVhS1Lc8WzE-NCBqgfl-5nat_jkW0URakjvtCsv7-0TBpO0FpiZONqANbH_wJ9sMiqriwBmX-72X-Zd5bEHjpVCDQgueFU76VrUERtPIfj72GdaQgnGGLUXGYWl2D24xqfUidxYr7fG90dv6WpQzXSi47hV-_VXORkKnm9UhkjVxlM_DKQIJqi24h9GOsSJa6EmpOAqUf26PXcLR_nSg3CSmG-UL2kg_tg8PMY9HRu9WfepZU4ouWwQQayR2hZ37_3yc2lR6LaiPIYU8ms4YAJVeVBnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشک و فیزیوتراپیست تیم‌ملی‌بانوان‌ایران؛ روز فیزیوتراپی رو هم به‌همه‌فیزیوتراپ عزیز تبریک میگیم که‌مشکل‌بازیکنان‌روسریع‌برطرف میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30920" target="_blank">📅 18:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30919">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BshKBOw6YHmmshqNMIsjaiNcvTVzvUmlL85HlEMLs6mXjFUni4h65qeSBm9EPD-7khC7IY3E2qM7625LRm2zCI_0MPsLq9N2RmaIESpC4aP0DVqUVL1eTOxO85xD1RRdJfej0sGKxmDKq4Vrhpv4tyIdPTeZ-C0jQjSGpg2BtXoeuy-7njUkhX0TdZ2Tu2Ip3gEytuBlb9z30mTPIAMZwl5uwXZoHXppk5QJEqy5GRmnUpuiObkSlbJbNCD6yoI6FgkKjy7V2vTyMh-3VUwsJEFnYWfpk3NnYqyk8T2NrYxjiVKeUg9r5Rzz5sfJ7uZtPpgYqJbncfGFU5oORpH7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
عملکرد خیره‌کننده و فوق العاده لیونل مسی در دو نیمه دوران حرفه‌ای خود در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30919" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30918">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWUdWcOO7v35Ysx0nAgyiRBJtS7EtSS6MerWNGiItKazuvLYU0lhXRMUPOJBR0J6-zQR3Xsh-C3WdX6bDB5TGBb042nX8MH6x2CMW2OuwzrIevIft3XCNs5cESQ_xAa0Oq2amoel4htJaVMpZXt4doEFXs6tMzQn_M4ZNX2u_grUi-1sy7LKbYbZYgZH0cM5dq7qTxgBDNkfyO7G5_wdKHuM4LDsVduIi9stzj9BhPeKouISsxtdWN_8ghQh7VqcQ-qu8E9Eie-O0rassyAIdkZyDZVr8lZjXXaJTalXCwU07XdoTvDVvXfo7bYI0fXseH7DJKw2qSxgh9ZfVyGxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی کره جنوبی در فینال مسابقات فوتبال بازی‌های آسیایی ناگویا یک بر صفر ژاپن رو شکست دادند و قهرمان این‌دوره از رقابت‌ها شد. دولت کره بازیکنان رو بابت قهرمانی از خدمت معاف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30918" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30916">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz_k0A2WbQq3GxS-4r5Mzau2NvmdiiBNKcOqcALHH6-y_ZOPd6Ru37UbxlmLrY7portkHVYfIXErwrfhrZkBwoQnnn3WFTGZYhQ7DTw2Kem9Ut83pe1Iz3qlYTIc5fAwhO1VV3oKKBb4Pz1s5A4TJpVd2TLQJb0JXIXB3dEz8i1EraUswbT6H6QUc-XXLo_SkCJSPeHur_3Wusx6F0eUrH0wv4ru8oq2eLhrEneeF9NcDASVCRVH5elwmzxfVV4hQSQeyWrqjILJGj-Ci9cFD4pKiibrH7OP7gZ8EjIXre9ftLjSeWiI692Sxy3AAyCNVzZX70jEwpDeGITzfcqTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فیفا باشگاه کایسری اسپور رو به دلیل فسخ قرارداد یکطرفه علی کریمی محکوم به پرداخت یک میلیون یورو به هافبک ایرانی سابق خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30916" target="_blank">📅 18:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30915">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuIOqHpZUHko9nJDon_-fYRASUJz0LRjR3_cOkGuN2eULjXIugnK9iDiqw2DlJDV1LM4w6MP-mFOx_oQfLjHJkN-49a-xGtT3q_KI6jFjz68m80PyC44V9cVhrGcTov8UWdOVkADw4mikMWjOc8U_bVhwLmtI8JRczdwq6PGC6jcmJMBWZIKnaMh9e-TYtUC2gc009Ewk4eHRmdXN1x6xE005qgmu8zqLkkMtkEA8VCKuEdTvAJbKGiAKzAnLo51CA3YCNX1d0VcDXxin-VlzVe_QIxZer12a-J_tH6pKrGt417Q9Wrb78VGIY_o66kQ_mu5t2WlM5z_gvNSKaZR5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رائول آسنسیو مدافع رئال مادرید بدلیل مصدومیت تمام مسابقات رئال مادرید در سال 2026 رو از دست داد و از ابتدای سال 2027 به تمرینات گروهی شاگردان ژوزه مورینیو باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30915" target="_blank">📅 18:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30914">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyzywGK0ccB6DbOzm7r6ZZLX8QiFZOvq4wabvv0BSqMUk_zZQr6nV5GqXgkdk9t2GXNKRxJ3R9FFwTtDbnXAhPczhXyP9RaWPCJ-Sqw9Wx8PS7ZpdBGtPZl534MvefPKs0X1jJpxaoyjIXchIwmBddbjK_wZgLfGMEOR5y2yGFr3UsfWZf8Q1GihkiSKRAZq4cse6RLU2Sy654Zh5KlF_CxzExJRLd5ZNEr4IAJ_l6OEQ4Zd5iBcN8BdA40EgJVpJvDzHv0ae4BX5Vchy9pfVZo76WvukvGPqI0MHqj8jijkP--3ZnAjN8s27iXS25MOJApkCRXuQTTeLr9q6z5Jdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دنیس اکرت مهاجم 28 ساله تیم ملی ایران از طریق مدیر برنامه‌ ایرانی خود علاقه‌اش رو برای عقدقرارداد با استقلال در نیم فصل اعلام کرده و درصورت تاییدیه سهراب بختیاری‌زاده احتمال آبی پوش شدن این مهاجم ایرانی الاصل بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30914" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30913">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOg-vOv28pbpxsjuG9gGTYoOWFS7hdKMP1LNrd9TpoDL7ugELNLM0DUs4vqzBepVXgr3Oto9xLRPtyE0NjxLokCiSDr_L_vx-qjieW38JjRQ7NfHoQDiNKPchjX7tA5c3QwLVdmHDQkxLugy9HhKPrvgz2wustAHR8KfRLjgXHxfdTycY2lMqLGjOxPP7qpSMa59HXgykta-duPE1Mnov5tbrxkDj6YtvYTpPxMGl3fNbuE11tkeRSoFz6I5XYNV-__mbNxDsBYai6v2_wR9diyZWM2E7w7543Wi3jvCpmjdtzJjG7R1HZWubjmoBNMG5sGSKrByx1VQAncZ-k-1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه فلش بزنیم به این صحبت‌های تلخ ابوطالب حسینی درخصوص قیمت دلار در آذر 1404 یعنی کمتر از یکسال پیش + دیس به امیر مهدی ژوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30913" target="_blank">📅 17:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30912">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ty5rUC_lALzPyBcgFN1QLKaFdKRIjxgMUngaMQGhSupoPNsPuYYlbdukNhL-8vRrHQo1ZDkq5EoGEmUnEOwQO_RJ7gX6hScN229guSrUejuRsmYijEkSnumfM2hYu80Xm9GYRqJNjCa2OrZKRt5TulZM6FtTXJtOYumB9uQ3cGsBGkeAB6XPirQx95tRwSC-lKF6CIh0MXy0_UHN51hBK41g5V9kfDqCF6Dies9bS30IBtDx6W5FhOGjQgwJsTG_MU3Y-bq1-L5TmNPgYvdB0SHvk4hrKIdJfqeENO17-jdm9lEQvpIQ1QX1IP46Z6kTd9vqc2VbpbeuYgK5T2iF6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هر ۳ جام‌جهانی‌که مسی فینالیست شده تو گل، پاس‌گل، دریبل، خلق‌موقعیت و پاس کلیدی نفر اول تیمش بوده.‌ توتاریخ فوتبال حتی یک بارش رو هم کسی نتونسته انجام بده چه برسه به سه بار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30912" target="_blank">📅 17:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30911">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shUI8B6c_nk88Cg0Pv7duD0oVDisUjZbmXtzOh3JoAkMl4OtIlxKvX_jrLgGRZeWToVurmLZrbKadam6pt1Yu2ijR3jnT47nKAxmj6tGMKstd5UxMAzsrSZvNER9haeWHXt1u5zbR4iSPI2M97YKlDr8OAgri0o6PM5F1h3_iGyQnKngcv-meiiS5NvVi1aIA9cSocnkQX9MgC63UhTTrwo0BijMtK72lcH-Ybyw8yfy7k1X3n9R3RWa2aDOQjy-Na9wq7ePmpkDhsKa-Om8xK_60kSAkhECe7UELE-A0FgNqHNziBacq8J8KgHn6T-E1w8xrB9c1yuHscNjXULxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
انتقام قهرمانی آسیایی از ژاپن گرفته شد! تیم ملی والیبال ایران امروز بابرتری سه بر یک مقابل تیم ملی ژاپن قهرمان بازی‌های آسیا شد و نوزدهمین مدال طلای کاروان ایران روبدست آوردند. البته گفتی است ژاپن با تیم دوم خود به این مسابقات اومده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30911" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30910">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=eVBZUZnlSXszTUMAzx4Xjw3lYsoQ-uiKDdGsZ6gQuA8_1TJZ5CUFq2T84jVUZbwfSexYbmZH95Sz6wa0ygdnbz2THIvLGoJMWPLCu4Z_w74DC5x1X0aw-ANXl1yD5M8xmPDTca3K9z-UbCnpq7-fBJFVKF8cVvLGMpvyuHGnuFHqpJeaRVWScFYq_GftwjdQ_GAL7itzWoJEBDhIE0VtQRfPuB5l3wt9vKGXD3k7DqKahrt66dp45PU0Ao3yX8JKl8-xL3gngmD-54Je2OShk6JgWUz3Fl6yX7PLIdWCwa6QGWTrNFwehhDwVt-X6BMDwLyOLCvdk7XnMUnbA8azNRIf6s7CUanQx1GyQIXk3FPqgwWsYoSSvBnSNskYK26xSbMUX2o84qKwv5yFWNb4Q0EtQ6vTwreavnh-vCgc-0N0nfV18Rk6l3MgoTn1J77Drf9edItbGHHqVFXgUEzpqtq9vadyjRTjR3WTx1X-Y0CFoHmqr3S8flKHmcqK2Cvtgoht7T1xQh7xAzHG5936vAKV2C5YVkr_ivOh9efcpcXaY9-bT5I6afakgCWgUZZf7ePLJWhfinfG18hFqY_Mq2FAbG1jfBhyIxQ7gqL7_exxXTc29G89_wIJYvKKbG1yAS6miWPPfBLoBl2E6rgilSAJH7d_vgeCuVy9_2YQtuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=eVBZUZnlSXszTUMAzx4Xjw3lYsoQ-uiKDdGsZ6gQuA8_1TJZ5CUFq2T84jVUZbwfSexYbmZH95Sz6wa0ygdnbz2THIvLGoJMWPLCu4Z_w74DC5x1X0aw-ANXl1yD5M8xmPDTca3K9z-UbCnpq7-fBJFVKF8cVvLGMpvyuHGnuFHqpJeaRVWScFYq_GftwjdQ_GAL7itzWoJEBDhIE0VtQRfPuB5l3wt9vKGXD3k7DqKahrt66dp45PU0Ao3yX8JKl8-xL3gngmD-54Je2OShk6JgWUz3Fl6yX7PLIdWCwa6QGWTrNFwehhDwVt-X6BMDwLyOLCvdk7XnMUnbA8azNRIf6s7CUanQx1GyQIXk3FPqgwWsYoSSvBnSNskYK26xSbMUX2o84qKwv5yFWNb4Q0EtQ6vTwreavnh-vCgc-0N0nfV18Rk6l3MgoTn1J77Drf9edItbGHHqVFXgUEzpqtq9vadyjRTjR3WTx1X-Y0CFoHmqr3S8flKHmcqK2Cvtgoht7T1xQh7xAzHG5936vAKV2C5YVkr_ivOh9efcpcXaY9-bT5I6afakgCWgUZZf7ePLJWhfinfG18hFqY_Mq2FAbG1jfBhyIxQ7gqL7_exxXTc29G89_wIJYvKKbG1yAS6miWPPfBLoBl2E6rgilSAJH7d_vgeCuVy9_2YQtuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ امیر قلعه نویی به فدراسیون فوتبال تاکیدکرده که افشین‌قطبی بعنوان سرمربی تیم امید انتخاب بشه. درحالیکه جایگاه خودِقلعه‌نویی محکم نیست و ممکنه هر لحظه کودتا علیه او آغاز شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30910" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30909">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=FDtCevm-t2ET52wUrs7JMmuiY42TDk2hGxDomXkl-0gPHrm8n2SUtkTwkM_PWZkvE11JqaBT_yZZkcElQXoAZkRHbieAsKDeh-ESPau9Zso0QEys7VonC0dzo3XDW7fFMpRnvBoccd20l8nCflSVnDYVg08M4FNqslFO1osYGAfPjaUZ4ngM68dY74vnb6dNoyUF6z91N_68X9QFgsLi5hhuGxtDNfYtCvIrkTkaP8BPg5LfhglpFBgz0XIvjVNJD0t8XVTW72Hh-1Uxj4jYK0aUREvGhXPFxWXMCDvQwYK7v_NQ0YpzzwwZYjPyfjbxmrqAGL3Ojj1UOlf_68-xRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=FDtCevm-t2ET52wUrs7JMmuiY42TDk2hGxDomXkl-0gPHrm8n2SUtkTwkM_PWZkvE11JqaBT_yZZkcElQXoAZkRHbieAsKDeh-ESPau9Zso0QEys7VonC0dzo3XDW7fFMpRnvBoccd20l8nCflSVnDYVg08M4FNqslFO1osYGAfPjaUZ4ngM68dY74vnb6dNoyUF6z91N_68X9QFgsLi5hhuGxtDNfYtCvIrkTkaP8BPg5LfhglpFBgz0XIvjVNJD0t8XVTW72Hh-1Uxj4jYK0aUREvGhXPFxWXMCDvQwYK7v_NQ0YpzzwwZYjPyfjbxmrqAGL3Ojj1UOlf_68-xRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30909" target="_blank">📅 15:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30908">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEaZ0bo1bzYw9fsEbx58_AjqG4MAguvvxPhbnuT3IeKsKvVCTEMj02vDkvQT4j9o1FZpPb1SggjFiCvPx3Cl5t06sBb5tqAOlNP12Ua4_9yH0z8lVzkg03ziHybxwpTqVlXWPOSAZxwi4fPxkPtZGMnijfSa3kHu7arwPBLnE6VDgNwLPzNIc9RtSuxFeTo851V8VEA83FpUi0rwkZ7oyF1Br4enTnMMw-JEgoonNjD2c-31ugomq6r9G2KAzWzubAk-rbzbBH420Xe1TNqsHtnWzwWcfimGHvmpScwI1Bclgs768GERggDp31gLNsOmVSKZ9EDmOmjkbNSdBbMJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30908" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30907">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA4A4IttDgB9VNw4N8bW-e0yED0kX_IFKaJGlE5mADO6QMoWIP-T7BKXp86CCfjaoRiH1v3EKs4MWW4fMwnWprPHhPRXIx3Hor-uvpDEUMCfz1p7kOQ5rMwbE2db7KqSrv7KJvuOrSK0_NKSFVfhiob31_kHK7-zm7YdF59FcPTho_itDB0TtXwne3_N9XMOohkc8S6iWFT6R_omNBV1-Qa1poCQ4HDShuvNNMhFheAR_Q49-NLYohpRg4eofezD_A8xe9KHDtYd-PiK9QTbxKWZdhvgrQT85rGl2ODaaS23w4s2W2l5lZ5OLTjd5bbze-1vci_HFQvePhlND6oNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30907" target="_blank">📅 15:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30906">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiOkR-w27C_khEdigurW_TQ-fyTT1jwLbX3SfFeQQOb8lq09MyW4tXk7FZdNuSrVXPgyk0VpdZzVtu9tbs1W7sZpgxnV6A8B71UO2UnqTBW8P6CyRwM9uZLoCinKjxVEwjas9u6lh-Fk9WOkWVHLTXSJLXSOBCWlP2Z1WjnQYbUoPlSfFhnUSu-AzEF3OwBDO0AyFBqGccDFMLJBcYLjydSqEYxb0vjCV4ltwK1MajFXBnx-f17aXiCI5IwjRhjEorzqOKaJycCQJkwRDADPGWCcvHnOhuHPvtYbsMGGtRNWXOp5WaMc8pvqc33qU9UZfPoIL1fQ7B4UBGYsXOUCsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ 10 گلزن برتر تاریخ مسابقات ملی؛ کریس‌رونالدو و لئومسی اول و دوم، علی‌آقا سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30906" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30905">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=huyGf9Ssck0PzVpHks0RFFX2izUy0eRKZQTqqFlFqNUPNYP2j2mNsnT-RTcK9rcBbbjJUsyHeCl7z-m1PqZaRVTTtNveDCh0h9_r6FBvHTmal7rRO5yhOemADt8ktYflNoUxWwnmUv-5ypd9LWo_Gf5z24-61LAMu924D9NiMtuYwG8an_XMH-OqCbnWSS6zpC9Hppmlz_A01dtbn1Uuuh18JJCrRzR_bKqP0Ch-UXbepBBHNDVS65PRDHeYBTSgMAWh6YBA04r39Ygmq3lWfR4hvnx66Gok7JbWgeAwcVrYui9KW3UPaFcq3NO9jjPxOdiW2K3eLTePPMXIfRsVPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=huyGf9Ssck0PzVpHks0RFFX2izUy0eRKZQTqqFlFqNUPNYP2j2mNsnT-RTcK9rcBbbjJUsyHeCl7z-m1PqZaRVTTtNveDCh0h9_r6FBvHTmal7rRO5yhOemADt8ktYflNoUxWwnmUv-5ypd9LWo_Gf5z24-61LAMu924D9NiMtuYwG8an_XMH-OqCbnWSS6zpC9Hppmlz_A01dtbn1Uuuh18JJCrRzR_bKqP0Ch-UXbepBBHNDVS65PRDHeYBTSgMAWh6YBA04r39Ygmq3lWfR4hvnx66Gok7JbWgeAwcVrYui9KW3UPaFcq3NO9jjPxOdiW2K3eLTePPMXIfRsVPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح بعد از پیروزی مهم آذر پیرا مقابل یوشیدا از ژاپن‌هادی‌عامل‌حواسش‌نبود میکروفونش بازه و گفت: ببین یوشیدا با همین خستگیش حسن یزدانی رو چیکار بکنه تو جهانی اگه بخوره بهش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30905" target="_blank">📅 14:46 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
