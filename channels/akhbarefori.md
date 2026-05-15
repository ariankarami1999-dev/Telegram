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
<img src="https://cdn4.telesco.pe/file/EIbChDLiprBGLeWi_AjEm5HQ_VSD-ntUMeY0GIrJl5tsx6PBtSc168y4XQYn6zN4IbEpNCd84QiUKhAuvmipc-6ce3gUzizyleju6c4Z4XU_Pc6HxhWTQ5kaP9euYhPYG8nbCKYwOyesP2K6yeE8UOUuNvlls7t_xoRgj6zk-kWYzzMDuEyEK0vhTvuB5fEM7Ccc8Lds0sGloNUvOAMfEa1D5lHb3xn5qWbLkw0webzTlYVz5WpI1yUHbw4eidn4N3kumT48J6JBs2nVW21WKZ01qrf-ziG2DMvGFxVDrMlD7paPML3d5DpYMX2QZO6Xgiqhvj01EPHPxn4zBkazFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.03M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 20:37:23</div>
<hr>

<div class="tg-post" id="msg-652425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7NkECgrIT_XNJem_rBsqJFc9UkRf31_RitYnjBmCuSqbWeebsdb27hctKcqFxLMFDbCHIkMyTGV_KsBhBkcsXVOyt8lVKB2CKAU18AYl8GB8VCcnpCIQnH61zLCVU3prEH-e4DHs9EU0CwfkuJw4GKSYxv_REQsJFdV-3i-TAXl2SkYSS7azSSBGgUEd4p-CHfaTdtpRf_1G6MOAPkR0UVxRLYzoHZL2F3vpot8_jqr65LeBPrJRp1KJjLbU1f_RUc1AOyqG7sjpKeMTs8oDqhAYfkHX6ZCas2EEHv-psmBRtJIaKiN-v8Z6PVepBV5VfdrWc0XxV6m-UeNgf9dtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش بهای نفت و سایه رکود بر اروپا در پی تشدید تنش‌ها با ایران
الجزيره:
🔹
سپاه پاسداران اعلام کرد از عصر چهارشنبه تنها ۳۰ کشتی از تنگه هرمز عبور کرده‌اند؛ در حالی‌که پیش از جنگ روزانه حدود ۱۴۰ کشتی از این مسیر عبور می‌کردند.
🔹
هم‌زمان با بی‌نتیجه ماندن نشست پکن، قیمت نفت بالا رفت و بورس‌های اروپا نیز در میان نگرانی از بحران انرژی و رکود سقوط کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/akhbarefori/652425" target="_blank">📅 20:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPRdGIGrxRyl5uFiinWLQaFmSEZcTr9XR9zbCUylYW5vDFXEzJo9rcYojnWA-SAyKS2P167WP0sceHlXsuJe8NoPRQaD6cOicJLZeW_WVxIg0awwkygkbuk96Qtf640Tq5tHj7JDjT62luxRm-p0iXGLHOHogCZZI_IlKDAU7FIgkmrFxWCJL80q4EUzXlmOprQK_dxOny2dxBmDlf2k7JpQKTcX5NaVaTIpKKCvJHq0WqqISkg6YVWgjIBJ4zmPcjxrhfwfEwoV5YyizrpiXZVna-rnNTbU4hCc1GEdyTO9xzvQsh2pZM5I8U66vjyMhF7hrs6GePrPyoe9qnKtzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا برای این زن در ایران ۲۰۰ هزار دلار پاداش تعیین کرد
شرح ماجرا را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3215122</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/akhbarefori/652424" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e91b011a6.mp4?token=NFJ_AQ4kzJ5RyiwXqX_wjf1pdj1t-RfVL1dAko8hM5Ca9uBHELEOMpGhPz06mI1x7N0vlBFr0JObRIHZik37zRiE9HrId3kkyK3lb29S0qI-UnrzIxZvHQrcrGVtlhhnPkI9Hr9aJZW4YSBY-iuaidtWNQxMLOxU8k5UgfnMipAFG3rqSstr8ueqBd5GC0wC6smxavqYeqVI0hlltsZlk-HgnnarOiYRFuNcMQPCSRUu-0f3gyzeCMgTMg0CxnDQ7eJT8pOkXSn6kdKQGbSNulIasnK6kSqWwHLlqLO1rpIX2SkUjoxfENNRammk8kQ_CoclfK4G18LsqfdTkQAaPyfgZEwNPny69AWJ9NiwiIbO7f0abQ9Q03CYyG5VZxmhUSyl870W4WWhNcz0Sjd1_8oRGe7Is97-w8pMv8PDhrdHom55VPfJsGgnyV6JcVOB6J8rBHq1y64N6IuC33RRNTC7h-jLJqA69H0ULrBzHBukMKLMd15igFA5fAgGRjYfZLhKntvNaL2-X3X-OqEjovSdvIUHdn5sYCmxYgpvH6StcWWn_hgWYNAb6yCfV1XEMs0HlMPahA9tz5h6wgBZ1wKXb1ZhSMCVjfHYK4pQ9pB1El4z0gvoVg2ju0_8cgLnxGgqXr2YLZuJYDHvWSLOoFjUd0v_gG2RK1w_uvhJKdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e91b011a6.mp4?token=NFJ_AQ4kzJ5RyiwXqX_wjf1pdj1t-RfVL1dAko8hM5Ca9uBHELEOMpGhPz06mI1x7N0vlBFr0JObRIHZik37zRiE9HrId3kkyK3lb29S0qI-UnrzIxZvHQrcrGVtlhhnPkI9Hr9aJZW4YSBY-iuaidtWNQxMLOxU8k5UgfnMipAFG3rqSstr8ueqBd5GC0wC6smxavqYeqVI0hlltsZlk-HgnnarOiYRFuNcMQPCSRUu-0f3gyzeCMgTMg0CxnDQ7eJT8pOkXSn6kdKQGbSNulIasnK6kSqWwHLlqLO1rpIX2SkUjoxfENNRammk8kQ_CoclfK4G18LsqfdTkQAaPyfgZEwNPny69AWJ9NiwiIbO7f0abQ9Q03CYyG5VZxmhUSyl870W4WWhNcz0Sjd1_8oRGe7Is97-w8pMv8PDhrdHom55VPfJsGgnyV6JcVOB6J8rBHq1y64N6IuC33RRNTC7h-jLJqA69H0ULrBzHBukMKLMd15igFA5fAgGRjYfZLhKntvNaL2-X3X-OqEjovSdvIUHdn5sYCmxYgpvH6StcWWn_hgWYNAb6yCfV1XEMs0HlMPahA9tz5h6wgBZ1wKXb1ZhSMCVjfHYK4pQ9pB1El4z0gvoVg2ju0_8cgLnxGgqXr2YLZuJYDHvWSLOoFjUd0v_gG2RK1w_uvhJKdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری شبکۀ مرتبط با موساد در اردبیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/652423" target="_blank">📅 19:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بن‌بست جنگ ایران؛ ترامپ دست به دامان کنگره شد
فکت‌چک:
🔹
رئیس‌جمهور آمریکا پیشنهاد تعلیق موقت مالیات فدرال بر بنزین را داده است. این امر قیمت بنزین را حدود ۱۸.۴ سنت در هر گالن و قیمت گازوئیل را حدود ۲۴.۴ سنت در هر گالن کاهش می‌دهد.
🔹
اما این طرح نیاز به تأیید کنگره دارد و هنوز مشخص نیست که آیا حمایت دو حزبی کافی برای تبدیل آن به قانون وجود دارد یا خیر.
🔹
کارشناسان می‌گویند که حذف مالیات بنزین، حتی به طور موقت، می‌تواند به افزایش بیشتر قیمت‌ها نسبت به حالت عادی کمک کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/652422" target="_blank">📅 19:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scu2T8mav7ogX-tt1VLbXAojNQSiKppZ8dXoW6Ov2_drPSPx1gbY_cTef4aoDfe0v-Y3ykoBhvMjMSvCrAdTo_uXoJlRb-8bvQ6jLi6vEwQC9VySrqTfBRMH9LM6sVM2uuehQTgVnB0MvMyJevab8ySHf7MA9qw5i7dwpdACENwRtKl_3t4A2PDnAmUjfESA0e-fjSTI89goEyn7HlTTmXzF7Q6zAjajOqdCpE0GVzoU6cV6x89brGHEP0uy_4dyrr0VMUfPSV_NoOyKilPDs6FWvbBLqOrnPepryVOv2itPKNBprOzRHjUJfpwE555siw-sBbX4ssPXmPnsZr7tkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا ایلان ماسک در عکس یادگاری چهره‌اش را تغییر داد؟ | هراس از اسکن چهره + ویدئو
🔹
در جریان سفر رسمی دونالد ترامپ به چین تصاویری ازایلان ماسک در کنار تیم کوک منتشر شد که در آن ماسک هنگام عکس گرفتن، حالت‌های اغراق‌آمیز و طنزآمیز به چهره‌اش می‌داد.
بیشتر بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3215173</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/akhbarefori/652421" target="_blank">📅 19:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
یورونیوز: ایران به دنبال اعمال عوارض بر کابل‌های اینترنتی هرمز است
یورونیوز:
🔹
ایران به دنبال اعمال عوارض بر کابل‌های اینترنتی هرمز به عنوان اهرم جدیدی علیه غرب است
🔹
رسانه‌های پرنفوذ ایران از تهران خواسته‌اند تا بر کابل‌های زیردریایی از طریق تنگه هرمز عوارض وضع کند و ترافیک جهانی داده‌ها را رصد کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/akhbarefori/652420" target="_blank">📅 19:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652419">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a02fdd912.mp4?token=pmwBKyKUzYUwTLIKL_-4LDVGzafIPW6qSyaqPZGcmOODf39F3ObhOzanM0hvEtbJdZEwJJ1oSyQZj7PfqFI-2kSOLv1vabSgYR6KZAckOh-BMHiMDrK2XEyZmO2lNdN1QRkZ82LPT4aIGNFULMI4-XP00G11qzKNimHtCXVUlDHS0amqIsFyTNCvYFIW40-FL6CvKRVhfJaO2UTdSX2-m0ywbU-KMyJlqxLct-ZCMttx8_IM26zaS4cqYG0NYbu6zglsOaw5H42HkpY3Y-5IEGRRy3Ad_WInv1ximD9K-EMc675SkgNWzwaE30mJoBVDpDLGIa75XEBAHPdThN4NZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a02fdd912.mp4?token=pmwBKyKUzYUwTLIKL_-4LDVGzafIPW6qSyaqPZGcmOODf39F3ObhOzanM0hvEtbJdZEwJJ1oSyQZj7PfqFI-2kSOLv1vabSgYR6KZAckOh-BMHiMDrK2XEyZmO2lNdN1QRkZ82LPT4aIGNFULMI4-XP00G11qzKNimHtCXVUlDHS0amqIsFyTNCvYFIW40-FL6CvKRVhfJaO2UTdSX2-m0ywbU-KMyJlqxLct-ZCMttx8_IM26zaS4cqYG0NYbu6zglsOaw5H42HkpY3Y-5IEGRRy3Ad_WInv1ximD9K-EMc675SkgNWzwaE30mJoBVDpDLGIa75XEBAHPdThN4NZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش‌‌‌سوزی در پتخ‌تیکوا در شرق تل‌آویو اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/akhbarefori/652419" target="_blank">📅 19:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652418">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0c9844d7.mp4?token=JMqoHvxVazyoriqJBuX09yrFUzoIezzezUXGSNB6K6OD3V3df2AlZRM3vraz-NVdRRZxAY9cgGXdKoxAL3yAw8GS2SebI4UxL6zAtk8QPAU0TJ4gT_MMHx3ZmekiM1HuethTabfwfutrmWDrzFSK3pcgkmUeJmxc72nrV_Dk9uHhmtGDGQj-sA18DJ9EXUZj71YR7WZ5DX1zWWK-ABcokIZ_8KgXzXgBRCuToJ00530QyVW7T4xjalC5aIJF3GECwIiT6yxO34XkifHbkyfvfGoIpwGmtX8ObOOyfXj1BaaAWb_h8lbKZ8iqJVVQBetoQXouqH087Bi5mrN4PBCw4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0c9844d7.mp4?token=JMqoHvxVazyoriqJBuX09yrFUzoIezzezUXGSNB6K6OD3V3df2AlZRM3vraz-NVdRRZxAY9cgGXdKoxAL3yAw8GS2SebI4UxL6zAtk8QPAU0TJ4gT_MMHx3ZmekiM1HuethTabfwfutrmWDrzFSK3pcgkmUeJmxc72nrV_Dk9uHhmtGDGQj-sA18DJ9EXUZj71YR7WZ5DX1zWWK-ABcokIZ_8KgXzXgBRCuToJ00530QyVW7T4xjalC5aIJF3GECwIiT6yxO34XkifHbkyfvfGoIpwGmtX8ObOOyfXj1BaaAWb_h8lbKZ8iqJVVQBetoQXouqH087Bi5mrN4PBCw4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قهرمانی که ۳۰ سال برای ایران جنگید!
@TV_Fori</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/akhbarefori/652418" target="_blank">📅 19:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652417">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlOTUWI5O9TAivPHbuwRwZA3c2dxKfkmLWqFRCUWupPhy7ntSulG2G2c8rHHoT1snUhj3nml6UyiRqTx00KWmgXNbZWQH0k49ylNz0W9RbDYgPwxCPpuByfeZWGq4fKxdSAm2Az6u1L2k421w50YfyNFjwBIiURYhR4cT3tXptaC0FAPhBfGsd5GQXIgjRabffNdiPc1T2PstFMCMQEKz5QhJ2xIORAbZFvTLglcyMovJaKzna3V5cmC9YsJNJYLKQLjAMmr8mYXk0MhiNQ7d3deD6cOk-xS7PSgrs_ai1cxEuO4xsyEuE_DbBfrbxqQrOyNY9DtiegBNkz9hSjp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میز کار هم می‌تواند سبز باشد
🔹
هر انتخاب آگاهانه در محل کار، قدمی برای آینده‌ای پاک‌تر است  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/akhbarefori/652417" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652414">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJCjQ32AZ5XlW1Ho2CLwbX1cSLWs1MnrRndWtq1ILYC7eHOE59s-iyC3xVvvsM-0ss5xlfT3odkCaUws8-a080YEf5VFqr8oPtuyZVmWWCtPj64_t92lAf0hFqhXeEQ8ZDdTnXZsDxaGRvxt8W7tE_JczSl7D9tHIVxNF7-KibGM9uz7AqK5P4WqI409eicpH_0M6E6dwi4tugoACM9usaAQdmrLuAt3wSMi9zCvd10u_DRV_8lHea0vnO6GCc1jU8HcirKaOT_xDKC0rcSeSDI5ExW11EIrHl4NT-WMpZegZxXzLrdTx-aVOVPNqDk_J743d_dUSSgI6mYcJX-rOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: با شکست دیپلماسی، ترامپ با مجموعه‌ای از «گزینه‌های بد» در قبال ایران روبه‌روست
🔹
ترامپ در میان توقف مذاکرات صلح ایران، با افزایش فشارهای داخلی و بالا رفتن مخاطرات ژئوپلیتیک مواجه است.
🔹
گزینه‌های تداوم درگیری نظامی، پذیرش ایران هسته‌ای یا عقب‌نشینی از مواضع قبلی، همگی گزینه‌هایی هستند که نفوذ آمریکا در منطقه را به چالش می‌کشند.
🔹
نارضایتی‌های فزاینده در داخل آمریکا نسبت به هزینه‌های جنگ، مانور سیاسی او را بیش از پیش محدود کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/akhbarefori/652414" target="_blank">📅 18:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652413">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR1KuiH7TJp-7d4xrIUOGkrCxuBwAEQGX-7Q1A0h66MOoTi8M6kf0skhv9fGv3NZGRt4DoNHAjPIjIqzYKMQD0gh8hILOgm6qnXiTebbB9Jg2bSR6k9NT-c4_emS5-aJtZoHqV70Sg4VBrwQeRDZ-PkSTjAI_z0ehw6KfaqahuLEs_a-QdqLUH_4XilaAUjxdFNEPP-4-zjOA0RjaytRYBIyQcaxeY_i1SFwcEcBlSHRJFmI1Lu1LzIUFuuUVg6M4M46VrAM_emSr6t5x-uF6VazsjG2v_JM_cQkBaovmXtrXLTM20DYiCxQYNB0J6DQ6kYkk8eVET9l9XwGXEEanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ تاکنون از چین در مورد ایران چه چیزی به دست آورده است؟
🔹
این که دونالد ترامپ، رئیس‌جمهور آمریکا، بتواند همتای چینی خود را متقاعد کند تا برای پایان دادن به جنگ آمریکا با ایران کمک کند، انتظار بالایی بود؛ جنگی که بازارهای جهانی انرژی را دچار آشفتگی کرده است.
ترجمه گزارش سی‌ان‌ان را در وبسایت خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3215152</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/652413" target="_blank">📅 18:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652412">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e9f34e9d.mp4?token=upSS34nkM1lmSQQgLwcmyZPPwzuLXGWeiv5F_smEd1D3dWu3XeNluVSVMwtBtC6Jr30Q9GdmrADg8KqKFlQzquKbZm2hhpzK3ZIgCeiZKk581lIm54Hkv400ESDN8C2DoPvKMiVdjEabCMs5icayHp2knG3PFDEow--WPXvrVzy5q75Xgnnju7rh6myEmRcX2KHGdDSaHEpCQgQIv_EbvUA4FwdCIfkURTugoWHoxpWMbS82tr3swcFYzVMsZ_axGLtaMzwr9fg6danQeqWPLl9LY5sdMUva50xDS_DnjUKpr7et5Y07lFXxozRwnm7TzoQqgxclybZAvLe0ru1YuS84UlwsvhaURlN1DovvpNL9DcmnNbhWQkg9y-49tQ0XU10lX69y-AAjPkYze4YHmPeIwb3Xops4vCdIO6q9t1yPESBb8wpyT4dHkQsWcTVO245eusXnIAqQBlbv3c5glaVNeRrU93mmUg7aOUIv2GDAgRK2XGp3xwogWPTm7prCiB9ntmb89Or6wpvPBBKG4BKc4q6Hcqxd3IZrQL5GbYw0tA49SJn1NRu4Xrc6ldOqwA-Rk3NA5UlwF6buj3n1H3_LhWqrvC8jVphNVG6YXf0nPcRf9fJrSM7VtNkT045NNGBlxtRg8JNK--kXSBVHejfx-3sAcMXI1p-sN-fSLos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e9f34e9d.mp4?token=upSS34nkM1lmSQQgLwcmyZPPwzuLXGWeiv5F_smEd1D3dWu3XeNluVSVMwtBtC6Jr30Q9GdmrADg8KqKFlQzquKbZm2hhpzK3ZIgCeiZKk581lIm54Hkv400ESDN8C2DoPvKMiVdjEabCMs5icayHp2knG3PFDEow--WPXvrVzy5q75Xgnnju7rh6myEmRcX2KHGdDSaHEpCQgQIv_EbvUA4FwdCIfkURTugoWHoxpWMbS82tr3swcFYzVMsZ_axGLtaMzwr9fg6danQeqWPLl9LY5sdMUva50xDS_DnjUKpr7et5Y07lFXxozRwnm7TzoQqgxclybZAvLe0ru1YuS84UlwsvhaURlN1DovvpNL9DcmnNbhWQkg9y-49tQ0XU10lX69y-AAjPkYze4YHmPeIwb3Xops4vCdIO6q9t1yPESBb8wpyT4dHkQsWcTVO245eusXnIAqQBlbv3c5glaVNeRrU93mmUg7aOUIv2GDAgRK2XGp3xwogWPTm7prCiB9ntmb89Or6wpvPBBKG4BKc4q6Hcqxd3IZrQL5GbYw0tA49SJn1NRu4Xrc6ldOqwA-Rk3NA5UlwF6buj3n1H3_LhWqrvC8jVphNVG6YXf0nPcRf9fJrSM7VtNkT045NNGBlxtRg8JNK--kXSBVHejfx-3sAcMXI1p-sN-fSLos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا: درباره بمباران ۲۲ مدرسه در ایران تحقیق نکرده‌ایم
🔹
- سناتور آمریکایی: اگر به ایرانی‌ها هشدار داده شده بود چطور ۲۲ مدرسه را بمباران کردیم؟
🔹
- فرمانده سنتکام: هیچ نشانه‌‌ای در دست نداریم که این چیزی که شما گفتید را تأیید کند.
🔹
-سناتور آمریکایی: چند مدرسه را بمباران کرده‌ایم؟
🔹
-فرمانده سنتکام: درباره یک مورد مربوط به تلفات غیرنظامیان تحقیقات در حال انجام است.
🔹
-سناتور آمریکایی: پس این اطلاعات علنی مبنی بر اینکه ۲۲ مدرسه و چندین بیمارستان بمباران شده‌اند را چطور توضیح می‌دهید؟
🔹
- فرمانده سنتکام: هیچ راهی وجود ندارد که بتوانیم این را تأیید کنیم.
🔹
- سناتور آمریکایی: درباره این ادعاها تحقیقات انجام داده‌ایم؟
🔹
- فرمانده سنتکام: نه انجام نداده‌ایم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/akhbarefori/652412" target="_blank">📅 18:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652411">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3f626cc5.mp4?token=jNK967fFETnXC0Iq8csREQM22r9FOTiH8nli0tyBfd8gf9kbQTGtVrU0AdS_KQWCJ6-3Ta9hvVHnyx3b1QvNmqd0gJ-TYeN6sRyIET4gwPWzCZ4SIVW_h3GsEJvG-3pNUrMQg8wKrwUqPDVJ-0ij3eFm0u0SXkwXHYbxgUw7NDwLag8r632TRVus8LI191Cgsh-corYo_kc5RQBMNJExDLWVUHFXydanUrE7RBjajC1K_M1VGEBq1bfU8yBt5JADnY45yCtSlp51_83bV_SPo3rk0F_Sd0qaJj3mHXcVwMnlbjTS_p_mATNPIheSjsWRVxFJcu0kdQ3-YOuY27sRfr7qhGcqmGn53vYyE6-21gCJvGeoMhBACQMllsBAYGFaQT1PJlSNP9vxWEufziSUiPvL0rlN196edPOYrMuauhdVpDLewQPaUDfp6L7bLs85xHkHyJmgPiFKFLoeavKlZf3LJQSTWZqZr1SOkMoarmBMSGo5mwfze0fZbidcrqhV-vTha4ovXRkBXqqGdvOJV_hTcfKnPuEP4tkIIDthPQ3kIbKcD6v0umav-193uG32y04IwnevfNUfQDFLFCJ7ZblKclCfGwD0IYht3cLugUGZXw6LFRmWj13GbXLcmnury7oSkh_JLaA31CMhpAHmpiQOfGMr-UaOQJpuFTrPI1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3f626cc5.mp4?token=jNK967fFETnXC0Iq8csREQM22r9FOTiH8nli0tyBfd8gf9kbQTGtVrU0AdS_KQWCJ6-3Ta9hvVHnyx3b1QvNmqd0gJ-TYeN6sRyIET4gwPWzCZ4SIVW_h3GsEJvG-3pNUrMQg8wKrwUqPDVJ-0ij3eFm0u0SXkwXHYbxgUw7NDwLag8r632TRVus8LI191Cgsh-corYo_kc5RQBMNJExDLWVUHFXydanUrE7RBjajC1K_M1VGEBq1bfU8yBt5JADnY45yCtSlp51_83bV_SPo3rk0F_Sd0qaJj3mHXcVwMnlbjTS_p_mATNPIheSjsWRVxFJcu0kdQ3-YOuY27sRfr7qhGcqmGn53vYyE6-21gCJvGeoMhBACQMllsBAYGFaQT1PJlSNP9vxWEufziSUiPvL0rlN196edPOYrMuauhdVpDLewQPaUDfp6L7bLs85xHkHyJmgPiFKFLoeavKlZf3LJQSTWZqZr1SOkMoarmBMSGo5mwfze0fZbidcrqhV-vTha4ovXRkBXqqGdvOJV_hTcfKnPuEP4tkIIDthPQ3kIbKcD6v0umav-193uG32y04IwnevfNUfQDFLFCJ7ZblKclCfGwD0IYht3cLugUGZXw6LFRmWj13GbXLcmnury7oSkh_JLaA31CMhpAHmpiQOfGMr-UaOQJpuFTrPI1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ به منتقدان جنگ ایران: خجالت بکشید؛ شما خائنید
🔹
دونالد ترامپ خطاب به «دیوید سنگر»، خبرنگار روزنامه نیویورک‌تایمز گفت: «من [در ایران] به یک پیروزی کامل دست پیدا کردم. ولی فیک‌نیوز، یعنی آدم‌هایی مثل تو مطالب نادرست می‌نویسید.»
🔹
رئیس‌جمهور آمریکا گفت: «تو یک آدم جعلی هستی. ما به یک پیروزی تمام‌عیار نظامی دست پیدا کردیم. من فکر می‌کنم چیزهایی که تو می‌نویسی نوعی خیانت است.»
🔹
رئیس‌جمهور آمریکا اضافه کرد: «باید از خودتان خجالت بکشید. فکر می‌کنم واقعاً خیانت است.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/akhbarefori/652411" target="_blank">📅 17:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652410">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
امام جمعه زاهدان با انتقاد شدید از عملکرد مافیای اقتصادی در شرایط جنگی، خواستار برخورد سریع و قاطع دستگاه قضا با زالوصفتانی شد که خون مردم را می‌مکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/652410" target="_blank">📅 16:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652409">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d04831a3b.mp4?token=s2cCXrIJWH51aKuyhUripp9_5SfWNKtKIUBw9C__fpmXgAAKmYkd95qA9HU4sf3VSc0BRGTqtrLOdKmhXjIwxPPLfO4wQLmY5CJYGZhcRyf-BfV53881fMO9h23vZKgypB4jIxV9yKDRFcNnS2v2HOwpt4xgsiMwT_u_nixTs2kZZLtae0GMwQOT-hMg7sncOgXA1ANjcHiH6aCWOIvdBK5DCu4nJrRTdNiecwRSFf20qY-f2Doex7HfBKfUwVuFwtHsjd0FRQMLn5rrG9wElQfyue3ilLF04yp77vfyMWX8NRSCwe_rqJE-rdSAeOI7lYxtimHGgoGG8CxMp5iRzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d04831a3b.mp4?token=s2cCXrIJWH51aKuyhUripp9_5SfWNKtKIUBw9C__fpmXgAAKmYkd95qA9HU4sf3VSc0BRGTqtrLOdKmhXjIwxPPLfO4wQLmY5CJYGZhcRyf-BfV53881fMO9h23vZKgypB4jIxV9yKDRFcNnS2v2HOwpt4xgsiMwT_u_nixTs2kZZLtae0GMwQOT-hMg7sncOgXA1ANjcHiH6aCWOIvdBK5DCu4nJrRTdNiecwRSFf20qY-f2Doex7HfBKfUwVuFwtHsjd0FRQMLn5rrG9wElQfyue3ilLF04yp77vfyMWX8NRSCwe_rqJE-rdSAeOI7lYxtimHGgoGG8CxMp5iRzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنایه محمد منان رئیسی، نماینده مجلس به عباس عبدی: یک ادم وقیح است که خودش از همه رانتی‌تر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/652409" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652408">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owk-5cmBVPi3Y9YtDHVsUzwjH75s-baXemdgoB6Y-fi9idyRSZqsjWQFyvQE8bgtcyKdnFLuHm-UhinQ1gdm4VKFJFKj0BWSShk9rbw4XmHv4dQV5a89DmI6GynY3FIIXuQgYqOWzMivCk-4fJH5jUOkr6mtIRaooF-FVoK7EM1vljHIrYyPq5TAIYKBGdO5JZVmuAGn9NSuNKZ1eruLeCaiN-W9xGR66iR0Hi1K03qCR6pQrwdKLg-XZctadXG2e-ns4458upKcMHTFKncYxBpZs4W94o3BaqvBv_PZVyAezB1JQAGyeFj4oCcVRNEP5oISrIZ-_DYjjMEt6Du-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خرید هوشمند، زمین سالم‌تر
🔹
هر بار که پلاستیک رو رد می‌کنی، یک قدم به زمین پاک‌تر نزدیک‌تر میشی  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/akhbarefori/652408" target="_blank">📅 16:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652407">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Igdl8VHeBQMjN1kfMXTku3izTf6eUDIVUsRF_paSumWYw309KEczQ6i2mekloPt1gF4VmwqryrsBSOw0McG53juSg3rGEvQVq13LH7zo-ZLwFMHDPk0h9L5J58Lpc1WyAs8mFZCOlLF6b11cNDeuJnXOilYcW53HLR5LKATvvl-KTDo3lULCVE84JzKP_g_jRnFyqoSKRYJ39KMqlEykFviNAUTAglfqYucIokIPc37hl2ArWyD9gdS7NPBHJ_QJ9vma0m_DaOSlPSS1GV8QwpZXOlwN11zZCRnMill2Y8iNo0fw3SYiSMyQf5C3YbT-1A7Q5-BDn27GThcI6_yQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفتگوی سران آلمان و آمریکا درباره ایران
🔹
«فردریش مرتس» صدراعظم آلمان امروز به‌صورت تلفنی با «دونالد ترامپ» رئیس جمهور آمریکا گفتگو کرد.
🔹
مرتس درباره این تماس تلفنی گفت: «من گفتگوی خوبی با ترامپ داشتم و ما توافق کردیم که ایران باید همین حالا پای میز مذاکره بیاید».
🔹
«ایران باید تنگه هرمز را باز کند و باید از دستیابی آن به سلاح‌های هسته‌ای جلوگیری شود».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/652407" target="_blank">📅 15:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652406">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zixaooe92l74C8HK8qE-MPV2CZAPVqOHVmmlWe7TjrPhJA_oaZwUE2xG1IQIbdqhRE8661OQGXztBlUw-zynoKlXGLwDbAVyQYfsnt7Bd4t22lVk6uWCwRLQBP8Ua-Slrg3xfp3uIQwyY6FNFHCqDg8Ebspg2tD95RrZn-1PzCGQQWZfCfluCHYyQcHcTSoTVFfwjjvR61YHP46WMTyLp41xedShbQy0BWnY9t9bQgf4Nde7Qo4Jxfq-A_hEWLjBrl6JncN89gtjOQkTAwCwrhzim9R4aTvQTkPBMP8hnPSPXnWntf4kOPSDpaSeDLCurJe8I9crVrzCamL4ecYi9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رزمایش غافلگیرکننده اسرائیل در امتداد مرزهای مصر
🔹
روزنامه عبری معاریو اعلام کرد که ارتش این رژیم سحرگاه امروز با مشارکت چندین لشکر، مانور غافلگیرکننده بزرگی با نام «گوگرد و آتش» را آغاز کرد که هدف آن آزمودن آمادگی نیروها برای سناریوهای عملیاتی اضطراری در جبهه شرقی به ویژه در حوزه استحفاظی لشکرهای ۸۰ و ۹۶ است.
🔹
معاریو افزود که هدف استراتژیک این رزمایش ارزیابی سطح آمادگی و رزمی ارتش برای مقابله با سناریوهای اضطراری متنوع از طریق آموزش فرماندهان و نظامیان در تمام سطوح از ستاد کل گرفته تا واحدهای میدانی با تمرکز ویژه بر منطقه مرزی شرقی که لشکرهای ۸۰ و ۹۶ در آن فعالیت دارند، است.
🔹
این روزنامه عبری تصریح کرد که این مانور شامل اجرایی‌سازی سناریوهای متعددی است که رویدادهای اضطراری را شبیه‌سازی می‌کنند تا نحوه عملکرد نیروها را آزمایش کنند به طوری که این رزمایش برای سنجش توانایی ارتش برای حرکت در «زمان صفر» از حالت عادی به یک جنگ با شدت بالا مشابه آنچه در ۷ اکتبر ۲۰۲۳ میلادی اتفاق افتاد، طراحی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/akhbarefori/652406" target="_blank">📅 15:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652404">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b764854cc4.mp4?token=qheIUBRanFAAnT7D6QzKxK7rzKqnDYGJ6OVPxK-1us0X-vTnzuF3MYnOQX4D6-Mp6CtECG_qS27DyhZB_JECf4gST2R3PEYP50bVd-8u-S2uLy2Jst9lAmJJI7WD48XVC-Rtxa4mweCJcPf2AQWFl_Bx6JVpQmFg3a6X3IJWkWg9abG-UYunTqqBxTo7YFs1qGj13LTrrbl0kKGbBu1IozVgurXyo8MZhzvH3ARodA8lDOiw54elP8rM9J_4Q2qmX9a1fA9O4fQGlxGA2rLjgV7TWtZZKa0T_T9fufRNIssnC-IiAmJTvO5gW3V77KRdCtakGs9U8dSLiQ6WiUjVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b764854cc4.mp4?token=qheIUBRanFAAnT7D6QzKxK7rzKqnDYGJ6OVPxK-1us0X-vTnzuF3MYnOQX4D6-Mp6CtECG_qS27DyhZB_JECf4gST2R3PEYP50bVd-8u-S2uLy2Jst9lAmJJI7WD48XVC-Rtxa4mweCJcPf2AQWFl_Bx6JVpQmFg3a6X3IJWkWg9abG-UYunTqqBxTo7YFs1qGj13LTrrbl0kKGbBu1IozVgurXyo8MZhzvH3ARodA8lDOiw54elP8rM9J_4Q2qmX9a1fA9O4fQGlxGA2rLjgV7TWtZZKa0T_T9fufRNIssnC-IiAmJTvO5gW3V77KRdCtakGs9U8dSLiQ6WiUjVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره ایران:
🔹
ممکن است مجبور شویم یک کار پاکسازی کوچک انجام دهیم، چون یک آتش بس یک ماهه داشتیم.
🔹
ما واقعاً آن آتش بس را به درخواست کشورهای دیگر برقرار کردیم.
🔹
من خودم خیلی موافق آن نبودم، اما این کار را به عنوان لطفی نسبت به پاکستان انجام دادیم؛ مردم فوق العاده، فیلد مارشال و نخست وزیر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/akhbarefori/652404" target="_blank">📅 15:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652403">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btb9GGT0SjNcInudfuX9jv52Edwb8InavdvWu_khp5gzNWJyC1Akwi_mRgFik3ZOYgCYvZHEmVRmptKuXKL-6U5F8uKcpewPbDLrIuGB5lQtODYIol_32SfriaHeGv9OrBnC7sr7D-ZPopE5xMLfcuEdzYLbtxgZla4YPifblK1HhE5p_4C59eNcerHIwpfNTsdf2UG5feGbaQbYZ0qcSuDXjlr87vTR4_jBFcsPBpYIYaHDG0aJyMnksr28KkzsAcEjr_tmP5xcH2qL18jfaNJmA1U6V5CDr6SbXILWeeuEuslVqdFUd8XlSsdexqtKjS-hT4uVX5eWr5PBJGJAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معجزهٔ ذخیره‌سازی ایران مقابل دسیسهٔ آمریکا
🔹
وزیر خزانه‌داری آمریکا می‌گوید بارگیری نفت در خارگ متوقف شد اما شرکت همراه آمریکا در فشار به ایران می‌گوید، تهران تاکتیک عوض کرده است.
🔹
شرکت کمک‌کننده به آمریکا برای رهیابی محموله‌های نفتی ایران، تنکرترکرز می‌گوید، اگر ظرفیت ذخیره‌سازی جزیرهٔ خارگ پر شده بود، نزدیک‌ترین نفتکش‌های در دسترس را می‌آوردند و آن‌ها را پر می‌کردند.
🔹
یک ماه پیش ترامپ گفته بود خط لوله‌های ایران منفجر می‌شوند، تنکر ترکرز اعلام کرد، بدون درنظر گرفتن مخازن خشکی، ایران یک ماه و نیم زمان دارد حالا ۲۴ ساعت از ابراز خرسندی وزیر خزانه‌داری آمریکا برای توقف بارگیری نفت در جزیرهٔ خارگ نگذشته است.
🔹
این‌بار هم این شرکت که پیوسته در حال پایش نفتکش‌های خالی ایران است، توضیح می‌دهد، هنوز هم نفتکش‌های زیادی هستند که ایران در آنها بارگیری کند اما تولید را کاهش داده تا با افت بارگیری نفتکش‌ها هماهنگ شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/652403" target="_blank">📅 15:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652402">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msz7cGRz5TAprdZs3jQ0IMEqLGGf0l-FcEKvWzdQ7aVwHLxN8dfQYFOTGpUKLACA_bB3i897ZDuFwF0RcivztVZ8k55rAdXLFPrXPkg11j7Y02HAM-u2kkkFMMba6rVAtVq1WQBa5PS2TvzGSDw7ofVnP6afF0Lu_dAMU_5uU5eie0K_9qpjwvl45xY42UFol9w_t2VAWvNsiN5N-QxTIjMAIi5W_lPF7Pfwj6JwC18ifCcR2Nh4Nm-CDZ-LVC0uJ0kXdZmfXT7Lp8iIXaEVHqQBFmyZGFqHdRqUSHlOwfZU7NhOGydOPG6QHKY6pehKYV9twmd93ar1lT6tc5Zz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌ها باز هم مصوبه دولت را پشت گوش انداختند
🔹
کسب اطلاع نشان می‌دهد از بستهٔ ۷۰۰ همتی مصوب وزارت اقتصاد برای تامین سرمایه در گردش صنایع بعد از حذف ارز ۲۸ هزار و ۵۰۰ تومانی تنها ۱۰ درصد تسهیلات پرداخت شده و ۹۰ درصد پرداخت نشده که به توقف تولید، کمبود کالا و گرانی اخیر ختم شده است.
🔹
اواسط دی‌ماه سال گذشته بود که دولت اعلام کرد برای حمایت از تولید و جلوگیری از شوک به تولیدکنندگان درنتیجه تغییر سیاست ارزی، ۷۰۰ همت تسهیلات سرمایه در گردش مصوب کرده و به ۴ گروه از تولیدکنندگان پرداخت می‌شود.
🔹
ابلاغ این بسته به شبکهٔ بانکی اواسط بهمن ماه انجام شده و قرار بود همان زمان به تولیدکنندگان پرداخت شود اما بعد از گذشت ۳ ماه تنها یک دهم تولیدکنندگان موفق به دریافت این تسهیلات شده‌اند.
🔹
مدت اعتبار این مصوبه ۶ ماهه است و بعد از اتمام آن بانک‌ها دیگر الزامی به پرداخت آن ندارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/akhbarefori/652402" target="_blank">📅 15:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652400">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EiwB4kuqbji51TfeqmDx6DuhstqAQKEBTal_D25LCfSuTbXOSgBjCm7CKDRoNCmvJWfyYTnm6XqgkB2UFjBL78603VGxZ1AZxEg5mpSNUf7k4RYdaqJz4x5JGoTNEHIgZZQ79zp5O0HoU3I8qQd12_e_09B_9VpR8FMU4N6ITuE-IHDMRurgMVJwy1weSx7UXTd2aMgK8sbJUfixO2aZsxccUOMvEugvd3u5idms00KrziStk50_ijJEJ-O4cL9O_Y7QYhfzBZT9ZSJMYvcddBl1xFc8JXEr3p-yn1Vg1-08V1ULAZD-dH7I-FL6XJgfK8lRcFSs2mFtdNE6iiUmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJq6CDIvIeytTU4JxuCoN4oUZPquBY9xX5puVNVDRgTepNsPEhcYQh2-HkWvYUgHSUkExXEeV2exeughVVSV7I-N6jBhKTtKCrFCyB9rwvveh_Y-jPDy9dOB64y_RsOxO48-OnmD43oIHfxMTv9i4mheLYNAMour43FZKD2wVCzu_IhpSXCamcJPQefZQx5NxeOB-JfFfLE-K6syXupcNnANIw9F5Femo_3KIGY4I-hM7aSNW6Ypxqa2kqlfWQsRLStdvclwhHvvsoh3I4Ph5kVGvqoUpLAPYv5zrBJimdzu8-WD0hxp3QrChCDWOTkZdW4o_GKIU0pI1LP5nmS96Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اعلام سقف ارزی جدید برای واردات برنج و نهاده‌های روغنی
🔹
وزارت جهاد کشاورزی: قیمت‌های جدید اعلامی در سامانه مربوطه ثبت شده است.
🔹
مهلت اصلاح قیمت ثبت‌سفارش این کالاها نیز از یک ماه به دو ماه افزایش یافت.
🔹
ملاک بررسی ارزش ثبت‌سفارش واردات برای مباشرین و شرکت‌های دولتی، تاریخ صدور کد مجوز موردی خواهد بود.
🔹
هدف از این تصمیم، تسهیل تأمین کالاهای اساسی و هماهنگی با نوسانات قیمت جهانی عنوان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/akhbarefori/652400" target="_blank">📅 15:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652399">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
امام جمعه بجنورد: هر قدم عقب‌نشینی در برابر خواسته‌های دشمن مستکبر، قدم‌های بعدی را در پی دارد و باید تنگه احد زمان خود را حفظ کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/652399" target="_blank">📅 14:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652398">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ترامپ: تحقیق درباره حمله به مدرسه {میناب) ایران ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/akhbarefori/652398" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652397">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ترامپ: به‌زودی درباره لغو تحریم‌ها علیه شرکت‌های چینی خریدار نفت ایران تصمیم‌گیری می‌کنم
🔹
ترامپ گفت ظرف چند روز آینده در مورد لغو تحریم‌ها علیه شرکت‌های نفتی چینی که نفت ایران را خریداری می‌کنند، تصمیم خواهم گرفت.
🔹
من از رئیس جمهور چین نخواستم که به ایران برای باز کردن تنگه هرمز فشار بیاورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/akhbarefori/652397" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652396">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af5ce4b8cb.mp4?token=ie8cdS4GzbmbM53WrjzSscU7txse2eeVkpdlISfA3SekijW03G79gGczvrtggVyPjliWgc2oWimMDyvrXAfRa-d923GflhV2K9NNL-yr27esoiiFZJyET7OgoxccJF5vKgnx6skvzKK4-XmikOsZW46c3raECjA1JU1fMivafqOumiff-AxmBKSPeA3m_4F6t41TWNInu3knxptfDJmmMzwycDEPXcpBBT6Gen5rllmAwtFdee5iB4J2riu_vUve-tZpVg5Lu3aa2OcuKXzVYHggi5z8TOJib8q4MrDQiQ9Wn_iVEUYDiLZeN-fTeOzkCDFFdcxDWa360wzMZ-_DXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af5ce4b8cb.mp4?token=ie8cdS4GzbmbM53WrjzSscU7txse2eeVkpdlISfA3SekijW03G79gGczvrtggVyPjliWgc2oWimMDyvrXAfRa-d923GflhV2K9NNL-yr27esoiiFZJyET7OgoxccJF5vKgnx6skvzKK4-XmikOsZW46c3raECjA1JU1fMivafqOumiff-AxmBKSPeA3m_4F6t41TWNInu3knxptfDJmmMzwycDEPXcpBBT6Gen5rllmAwtFdee5iB4J2riu_vUve-tZpVg5Lu3aa2OcuKXzVYHggi5z8TOJib8q4MrDQiQ9Wn_iVEUYDiLZeN-fTeOzkCDFFdcxDWa360wzMZ-_DXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: همزمان با دیپلماسی، امکان جنگ هم وجود دارد. امیدوارم به دیپلماسی، فرصت داده شود هر چند برای جنگ تمام عیار هم آمادگی داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/akhbarefori/652396" target="_blank">📅 14:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652395">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aynws7Bbz7Be73M0qATsB0rMnw0j8MtoWxxIk0X5hAIj1XcQRee4tYBELPjF-bqMxnfr_T-ENgzh6ul8VOq6_97v168zIwIXx79Fsm0V4uoJNuu_0_XS6VeKHRYYT4qcl2Fty3WRzO36MrpWZMajP-DtopNbw3qpfGk9_s-Qi_rmAecNuF1TlvkQG_h-cJXSW6UJCpDioDa8R8wCSDVADqmOGhhHxTkDBbhK47ewqr-dLc330RvKTBbBSfr9apPPBcBCm2k450_1qwsUUIZSo7pi_6hPMpNmXh9HGdL7VBAW5E7zQr2Zq58SQ8qzY1rRLyGnqyFUet9JHn-MAlnutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: من هیچ مخالفتی با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال ندارم، اما این باید یک تعهد واقعی باشد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/akhbarefori/652395" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652394">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad8617c6d.mp4?token=T-XZ-191VFupIWcARIIRO1lmW9Mc9UrPbqSwmjE4rbcLIxSJwat7KpLOiyEbQLUoKplNj4qNNNbZdVN2gUUjTB4ZWV05a5_Mbiido993XyD3AeSqtzu50SePl2-Otyb4173oWKaCtP3ymgnf9puE0mqvBIlgMw-Oo6Ll_yT6HFweQmN9MgCt05DWXH88yJdbgoZJKVJetSUNu8Gc25fLp8L62RkoVoZ07BNxnqf6vLwt3U8r7BVFgP3k2aHm5KvsQ8y65Iug-qbBLoWhzyHO7DzYduBUQLm7SiIiLMUsEdTqcJe_74Q1blgGIBkQo_XRIFONxMX3rsreXZGi23CNGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad8617c6d.mp4?token=T-XZ-191VFupIWcARIIRO1lmW9Mc9UrPbqSwmjE4rbcLIxSJwat7KpLOiyEbQLUoKplNj4qNNNbZdVN2gUUjTB4ZWV05a5_Mbiido993XyD3AeSqtzu50SePl2-Otyb4173oWKaCtP3ymgnf9puE0mqvBIlgMw-Oo6Ll_yT6HFweQmN9MgCt05DWXH88yJdbgoZJKVJetSUNu8Gc25fLp8L62RkoVoZ07BNxnqf6vLwt3U8r7BVFgP3k2aHm5KvsQ8y65Iug-qbBLoWhzyHO7DzYduBUQLm7SiIiLMUsEdTqcJe_74Q1blgGIBkQo_XRIFONxMX3rsreXZGi23CNGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: احتمال بازگشت به یک جنگ تمام‌عیار وجود دارد ولی ما هم برای جنگ و هم مذاکره آماده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/akhbarefori/652394" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652393">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d206e144.mp4?token=mUL1PhMsaxUqRTyr3GAaGAEoZENVYpqcssDDPcB4Dq4SfzV1DDhQqzZsnwo6EBPHak3SrdOwZVQV15i7aK1nzmnU12FoH6QKzfpotRdNJA0ePBFtNhbzsyq09ifiqVtASQxMe0comteptmxQAAKM9rzWNy6rdPeDXrXT48nfgke6E1AIBBqBr8oV2HoHVQFIVpVtxi1DEsfS4SD6_LN_lvXuQ2Lc_xOuZALj0a_2bB9couaScy38AuRDlK1DCfjXW6amaW8-Zs8UmCF6FdaAPXfbjyXQXlEmpQWnM2bqWHmHyl7c_wSb5pYs6_xbXgiZl3sKhvE-Ae5MmiGKyTyvIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d206e144.mp4?token=mUL1PhMsaxUqRTyr3GAaGAEoZENVYpqcssDDPcB4Dq4SfzV1DDhQqzZsnwo6EBPHak3SrdOwZVQV15i7aK1nzmnU12FoH6QKzfpotRdNJA0ePBFtNhbzsyq09ifiqVtASQxMe0comteptmxQAAKM9rzWNy6rdPeDXrXT48nfgke6E1AIBBqBr8oV2HoHVQFIVpVtxi1DEsfS4SD6_LN_lvXuQ2Lc_xOuZALj0a_2bB9couaScy38AuRDlK1DCfjXW6amaW8-Zs8UmCF6FdaAPXfbjyXQXlEmpQWnM2bqWHmHyl7c_wSb5pYs6_xbXgiZl3sKhvE-Ae5MmiGKyTyvIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: کشور هایی که به اسرائیل و آمریکا با اراضی خودشون با حریم هوایی خودشون کمک کردند باید پاسخگو و مسئول باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/akhbarefori/652393" target="_blank">📅 14:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652392">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
عراقچی: تنگهٔ هرمز در آب‌های سرزمینی ماست و مدیریت آن نیز با ما خواهد بود
🔹
تنگه در آب‌های سرزمینی ایران و عمان قرار دارد و میان آن آب‌های بین‌المللی وجود ندارد؛ بنابراین مدیریت این مسیر باید توسط ایران و عمان انجام شود.
🔹
اکنون نیز ۲ کشور درحال رایزنی هستند تا سازوکاری مناسب برای ادارهٔ آیندهٔ تنگهٔ هرمز و تضمین عبور امن همهٔ کشتی‌ها ایجاد شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/akhbarefori/652392" target="_blank">📅 14:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652391">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c515097104.mp4?token=IzIz5a_dqUtI0zZI4lR9EaOynZEZPSiwvKUy-yGKV9FuH-V8rkxJVtEba__jdwGpNe_xzJMleCiM8kJDVtGny1mJqyzJ0UYyEAxwdAWXn2Rww-ABMvT5BkFvyKeOBwmsvk6NRbmyJNsHKsjNeKM8Nt7Wm_NOOv6fY66nERw79ZyxT78Fp1dX-ti4cibX93WJcaxh7MXp3POUh1zR5Kpk0mSHUxbwm3y6o9VGii0-oHgnvhQf88oD0-KQzHyAtYw1_j6ZpDtnUOsi3k3W2IhYH0T4-btbuBn5qfwsHg6J9ZLmYpweqGEKnhBaWKja3XVA8hAQXksxaWDYU8nSEKRsIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c515097104.mp4?token=IzIz5a_dqUtI0zZI4lR9EaOynZEZPSiwvKUy-yGKV9FuH-V8rkxJVtEba__jdwGpNe_xzJMleCiM8kJDVtGny1mJqyzJ0UYyEAxwdAWXn2Rww-ABMvT5BkFvyKeOBwmsvk6NRbmyJNsHKsjNeKM8Nt7Wm_NOOv6fY66nERw79ZyxT78Fp1dX-ti4cibX93WJcaxh7MXp3POUh1zR5Kpk0mSHUxbwm3y6o9VGii0-oHgnvhQf88oD0-KQzHyAtYw1_j6ZpDtnUOsi3k3W2IhYH0T4-btbuBn5qfwsHg6J9ZLmYpweqGEKnhBaWKja3XVA8hAQXksxaWDYU8nSEKRsIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی:  خبر رد پیشنهاد ایران توسط آمریکا برای چند روز پیش هست/ پیام‌های از آمریکا گرفتیم که مایل به ادامه گفتگو و تعامل هستند
🔹
وزیر امورخارجه کشورمان در نشست خبری:
🔹
اینکه مطرح شده آمریکا پیشنهاد یا پاسخ ایران را رد کرده مربوط به چند روز پیش هست که آقای ترامپ توییت زد و گفت که غیر قابل قبول هست و ولی بعد از ما مجدد پیام‌هایی را از طرف آمریکایی‌ها گرفتیم که مایل به ادامه گفتگوها و ادامه تعامل هستند.
🔹
اینکه امروز چطوری دوباره این موضوع در رسانه‌ها برجسته شده، من اطلاع ندارم ولی قضیه مربوط به چند روز پیش هست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/akhbarefori/652391" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652390">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffeede06a6.mp4?token=aMYs94Ptl7VMpp7ym7y35cWzx8aUx4SiEpi82baBJzUuawN41JOVx2fRfj8U4U5QGYbjbDSuoRJgyOkrl64bFihJq459_79sx6IU0W0arwstUA3SAeiVCtg7OH4Dgg_hnKUtAXh3DUA-Wmd1w_EZmB5WTNFvdFMTcVbu_fSHKjLhMl6oegpn0KtNJqC4H92iuDElGI-uYSdCR6_xQRuALkyFZVeg0OwbCyc47u5LgxMMS_neRLnUTrMlI3MSvrGNK93MI_InUEEce2e2GIWeCNDjVrvvj9hw2RCKeMl0Z_vUY9uHId4ByIEmk-_C20oaf5jqENvAEdbTZuHuRoLFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffeede06a6.mp4?token=aMYs94Ptl7VMpp7ym7y35cWzx8aUx4SiEpi82baBJzUuawN41JOVx2fRfj8U4U5QGYbjbDSuoRJgyOkrl64bFihJq459_79sx6IU0W0arwstUA3SAeiVCtg7OH4Dgg_hnKUtAXh3DUA-Wmd1w_EZmB5WTNFvdFMTcVbu_fSHKjLhMl6oegpn0KtNJqC4H92iuDElGI-uYSdCR6_xQRuALkyFZVeg0OwbCyc47u5LgxMMS_neRLnUTrMlI3MSvrGNK93MI_InUEEce2e2GIWeCNDjVrvvj9hw2RCKeMl0Z_vUY9uHId4ByIEmk-_C20oaf5jqENvAEdbTZuHuRoLFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: به محض مطمئن شویم آمریکایی‌ها جدی بوده و آماده یک توافق عادلانه هستند، ما به مذاکرات برمی‌گردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/akhbarefori/652390" target="_blank">📅 14:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652389">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25be2c076c.mp4?token=rpUg6pO-hby6vvWvK9_drCOHVhtc6tczhnUEhPHo4MkOZ3_c3mCDmt4l74yf1BMWf0RrjE8hNEsewNfoKUHLONwSmyZgUx3P8Za90KGaI4jlB8y6ntnUdq0Mj2L0E3I8UGXD2P77Y9aJ8VK5hFy-Vgn35x6rgDC2qjm_TIXmc-t3yGfxVKBGbqTqkW8iOVFpXrAX0RY6j354GEA1ZbD8S3tpnSdeBboiS9GLVFu_b3qfl51axrWP_nyUvsffRtc6D0nawN_pETqq0TB8Xh2-I39bACHEYEd_RYvkDHygKm041ThL1M8I77mSdvwc0pU4O5j7caFw9HPAoPvbBXTf5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25be2c076c.mp4?token=rpUg6pO-hby6vvWvK9_drCOHVhtc6tczhnUEhPHo4MkOZ3_c3mCDmt4l74yf1BMWf0RrjE8hNEsewNfoKUHLONwSmyZgUx3P8Za90KGaI4jlB8y6ntnUdq0Mj2L0E3I8UGXD2P77Y9aJ8VK5hFy-Vgn35x6rgDC2qjm_TIXmc-t3yGfxVKBGbqTqkW8iOVFpXrAX0RY6j354GEA1ZbD8S3tpnSdeBboiS9GLVFu_b3qfl51axrWP_nyUvsffRtc6D0nawN_pETqq0TB8Xh2-I39bACHEYEd_RYvkDHygKm041ThL1M8I77mSdvwc0pU4O5j7caFw9HPAoPvbBXTf5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: تنگه هرمز باز است/ به جز کشتی‌های متعلق به متجاوزین، همه کشتی‌ها می‌توانند از تنگه عبور کنند
🔹
وزیر امورخارجه کشورمان در نشست خبری:
🔹
ما یک برنامه صلح آمیز هسته‌ای داریم و همیشه آماده بودیم تا اطمینان حاصل کنیم که این برنامه صلح آمیز هست و صلح آمیز باقی خواهد ماند.
🔹
ما آماده‌ایم به کسانی که شرایط ایران را قبول می کنند کمک کنیم تا عبور ایمنی از تنگه هرمز داشته باشند.
🔹
به محض اینکه تجاوزات پایان پیدا کند مطمئنم همه چیز به حالت عادی برمی‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/652389" target="_blank">📅 13:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652388">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74d2591b6.mp4?token=LjDkMs2bmcvW5FDs3bGyYtgjL0pqnzZiR7_6UmeLRBmK7_4coV6-pyviMCs1Jq3OrLY2P9vaBJkNDujvCF5N_SBe900M2Kx-Zi287IGgQ8M_TtaYKf87tQA4plK6PYQ4OsDcE-aG4P3KgDow8qh4m0Aih8NQt_5qmMWQl0hrJDAbqPebRtb-yPf0KHOzcJ31tXKYpzfL_qNzlM8kouYQTK4MP-H_zuJZAjG6JEgkS3hn4o6dQaXJBxc4R7_jyp48e7DRRj7dnpPeVZXDaOLII9lc8j7wcg1G-LWKGBCokBqKsanj92Vb4uUOl_FV-vEWZcIUyVx2heaMm30vV6BaIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74d2591b6.mp4?token=LjDkMs2bmcvW5FDs3bGyYtgjL0pqnzZiR7_6UmeLRBmK7_4coV6-pyviMCs1Jq3OrLY2P9vaBJkNDujvCF5N_SBe900M2Kx-Zi287IGgQ8M_TtaYKf87tQA4plK6PYQ4OsDcE-aG4P3KgDow8qh4m0Aih8NQt_5qmMWQl0hrJDAbqPebRtb-yPf0KHOzcJ31tXKYpzfL_qNzlM8kouYQTK4MP-H_zuJZAjG6JEgkS3hn4o6dQaXJBxc4R7_jyp48e7DRRj7dnpPeVZXDaOLII9lc8j7wcg1G-LWKGBCokBqKsanj92Vb4uUOl_FV-vEWZcIUyVx2heaMm30vV6BaIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: هرگز به دنبال سلاح هسته‌ای نبودیم
🔹
وزیر امور خارجه: تنگه هرمز باز است جز برای دشمنان ما، هر کس می‌خواهد عبور کند باید با ما هماهنگ شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/652388" target="_blank">📅 13:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652387">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLdU-rSwS9eRMh5BlYObJ_4apAEvSV5Z3L80Kb8miDwaPi2igo841oT1iWlBxR84LSjLrHsSY6AgBSeXE4R6n89HoBiTLxDNDUVrpzObk-foUi--X36kYiWO2CRtcTVpsffWp0t9U9ISO9BpUQd4Jy8drLB8CfBgKjtmBkHt1lVUhG3Y-HFOde7t-beAAoppGWQwVx6tc28aBgux0eTOAg12ZNzZtmPWnGNa_vQ7BD1ziY12vbU-9Ru6huVD_59Jf7uJ09_UHetYbaRNMcF2FZRJ0VS9nXh0_RizDs4KxERmM1UkGw4vSZXGchAj1VOXCCK_w4ruVqlMuFoWQliWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکمیلی /
🔹
عراقچی درباره خروج اورانیوم از ایران به روسیه گفت: مذاکره خوبی با لاوروف داشتم. مشارکت راهبردی با روسیه داریم. با پوتین در روسیه دیدار کردم و در خصوص اورانیوم هم صحبت کردیم از پیشنهاد طرف روسی متشکریم این موضوعی بود که باید در حین مذاکرات به نتیجه می‌رسیم. موضوع غنی سازی ما پیچیده است و برای رسیدن به نتیجه با طرف آمریکایی پیشنهاد دادیم این بحث به تعویق بیفتد.
🔹
در حال حاضر این موضوع مورد بحث نیست.
🔹
نسبت به جدیت آمریکایی‌ها شک داریم. آماده توافق منصفانه و عادلانه هستیم.
🔹
رئیس دستگاه دیپلماسی در پاسخ به سؤالی مبنی بر اینکه آیا در زمان اجلاس سران بریکس امیدوارید به اختلافات با امارات پایان دهید؟ گفت: ما مشکلی با این کشورها نداریم. آنها هدف ما نبودند. پایگاه‌های آمریکا در این کشورها قرار دارد.
🔹
امیدوارم در اجلاس سران به فهم مشترک برسند. ما قرن‌ها با هم زندگی کردیم.
🔹
اماراتی ها باید متوجه این موضوع باشند. اگر به مسیر عقلانیت برگردند می‌توانند ایران را به عنوان دوست در نظر بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/652387" target="_blank">📅 13:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652386">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5517ce1975.mp4?token=XFFaQGRTH_ikN1FgS9A5UGSK4zxlss-LdxrxroHqa-4SdzaIN6AzgDjmDPFrjeN-gCjBd6qqolssKsAtO0eJi2FlU75W7e6B5vh-3RgzpEho7hVDKmagm2gPqHITRkjruYDjCu6Yspe7W5AhPjjvrEEFY9tNX9cBa207NJuvwYWH2ooU2LDqPX6BcQNEgzJa9g-Yb1HpC7XhZXlsbRPCHVKvmw1Wmo75etxM4xDZ2HzNZ6xV8r8R3zgBYdhI_JcyU3K6TDIMvmwDBRCjW8iBrm3wwYGIwYUm8Q5s-9JKrk4scxuJDcqnpGY-PsCJ9P1zoyOMLE3qDMKNd72s6tbJUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5517ce1975.mp4?token=XFFaQGRTH_ikN1FgS9A5UGSK4zxlss-LdxrxroHqa-4SdzaIN6AzgDjmDPFrjeN-gCjBd6qqolssKsAtO0eJi2FlU75W7e6B5vh-3RgzpEho7hVDKmagm2gPqHITRkjruYDjCu6Yspe7W5AhPjjvrEEFY9tNX9cBa207NJuvwYWH2ooU2LDqPX6BcQNEgzJa9g-Yb1HpC7XhZXlsbRPCHVKvmw1Wmo75etxM4xDZ2HzNZ6xV8r8R3zgBYdhI_JcyU3K6TDIMvmwDBRCjW8iBrm3wwYGIwYUm8Q5s-9JKrk4scxuJDcqnpGY-PsCJ9P1zoyOMLE3qDMKNd72s6tbJUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه: پیام‌های متناقض آمریکا مشکل‌ساز است/ توییت امروز مقامات آمریکایی با توییت دیروزشان فرق دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/akhbarefori/652386" target="_blank">📅 13:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652385">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر انقلاب اسلامی به مناسبت ۲۵ اردیبهشت ماه، روز  پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/akhbarefori/652385" target="_blank">📅 13:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652384">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036c33f3d1.mp4?token=XYJtc2miu_toLs_VjcI-70gaYZMOSWUiw-zIRrjDT3Ltdw2lwYlm1lH_mDWKkdGsL2JUfWx51uBQKUogslUHHvXRE0pi0tdZeR5CM5XVs4OtkFtnBjapSh_08JO5LjsxYibnmItNacTYNmGrTnRM4MP8peP_-PoggTJ_aHpfuWC5Angycc1Ht-AZ3DkAwY7vh8RGTJW8_VtfQdZXzwtut9Hj9tJeqZ-SD8aNJJCF9n0ygRYRNZ0WW7d6YW4erBQvinttp5LWM605NKorjxtkRhNlI2hlAEMD3yb5A0Jy6lqZY8d2l1Oia8aOwxD-J_xyWxJdCkOwz0BWbe77TsY-IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036c33f3d1.mp4?token=XYJtc2miu_toLs_VjcI-70gaYZMOSWUiw-zIRrjDT3Ltdw2lwYlm1lH_mDWKkdGsL2JUfWx51uBQKUogslUHHvXRE0pi0tdZeR5CM5XVs4OtkFtnBjapSh_08JO5LjsxYibnmItNacTYNmGrTnRM4MP8peP_-PoggTJ_aHpfuWC5Angycc1Ht-AZ3DkAwY7vh8RGTJW8_VtfQdZXzwtut9Hj9tJeqZ-SD8aNJJCF9n0ygRYRNZ0WW7d6YW4erBQvinttp5LWM605NKorjxtkRhNlI2hlAEMD3yb5A0Jy6lqZY8d2l1Oia8aOwxD-J_xyWxJdCkOwz0BWbe77TsY-IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ما به هیچ وجه نمی‌تونیم به آمریکایی‌ها اعتماد کنیم برای همین قبل از توافق باید همه چیز مشخص و روشن شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/akhbarefori/652384" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652383">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3abba85efb.mp4?token=epRJvUArw6OKBFFfjHtyaI0FN6nmGq6GvXchTo2kfkTSgjfHTXgJtWHGMsXOhYrESNa5G6_sDxDvkfFh5jWePoZ_SzHEf0Hh6vg8b__SaI2VJpry2qkRVztuYXySIR-r6DDhztWubgoo7xtEwn6GJXdBPMrVdVi1MNLnSq81ieUpWJ6v8uDRjpSQOxna-CtxJ5agmH7WM01XQOEv9FmDs6Qo_HeIMWZwD-zxTDsPS20SxLcnwanaW9LEWBbacFWgxuEuTk55eR4jdOyuvl9D13I2L-HBiWMTkveDiTPRivpaIs1gQEthMn6eb5V309DdNNVKRLao_L7Ph4CIL_PCEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3abba85efb.mp4?token=epRJvUArw6OKBFFfjHtyaI0FN6nmGq6GvXchTo2kfkTSgjfHTXgJtWHGMsXOhYrESNa5G6_sDxDvkfFh5jWePoZ_SzHEf0Hh6vg8b__SaI2VJpry2qkRVztuYXySIR-r6DDhztWubgoo7xtEwn6GJXdBPMrVdVi1MNLnSq81ieUpWJ6v8uDRjpSQOxna-CtxJ5agmH7WM01XQOEv9FmDs6Qo_HeIMWZwD-zxTDsPS20SxLcnwanaW9LEWBbacFWgxuEuTk55eR4jdOyuvl9D13I2L-HBiWMTkveDiTPRivpaIs1gQEthMn6eb5V309DdNNVKRLao_L7Ph4CIL_PCEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ما در آتش‌بس هستیم اگرچه بسیار ناپایدار است؛ اما در تلاشیم تا آن را حفظ کنیم تا به دیپلماسی فرصتی مجدد بدهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/652383" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652382">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_IIAtcBVB2d6WRQ3qlzRYd7oE9WJ98QJ8UGchRiY4jQbLHre6ZIR3Lldg9Nj0Z1V9SlnfZTuLezVSbfgTNhsuOdxwW_Yoc0BD3zWMSOg2Eyr5e25HCIjcYNNrqIjv3u28ckHS4rm9UNire38y3DesJCd43GBP_V-VY_0eVco9Iatb1-fAdK0Qn5L2qBYqQlnhZqXD9_ExVKP_j-CbxmW2Mdxuub0lSl_rTdQvQAEq2Y-cJDHXE-h868yhVwrgVqVTdUizOBOkmDGMJ0QJmm8gY-0zE6Pzf19EjhbyX8BtAD6mQgzdV4WbYE-eKV4ea--MoLpqi_NOKD2TiThXqPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اژه‌ای: امروز آزمونی دیگر در راه است، مبرم‌ترین نیاز در شرایط فعلی، اصلاح الگوی مصرف است
🔹
رئیس قوه‌قضاییه در فضای مجازی نوشت:
🔹
مردم گرانقدر ما بیش از ۲ ماه است که میدان را تسخیر کرده‌اند و حمیّت و غیرت خود را در ولایتمداری و میهن‌دوستی به رخ جهانیان کشیده‌اند؛ هزاران آفرین و مرحبا به این ملت سلحشور و وفادار.
🔹
صرفه‌جویی ملت در منابع حیاتی، مصداق مشارکت ملی و حضور مؤثرتر مردم در میدان است. قطعاً ملت ایران نیز از این آزمون سربلند بیرون خواهد شد.
🔹
در این نهضت ملی صرفه‌جویی و اصلاح الگوی مصرف که روی دیگر جهاد مقدس ملت ایران است، مسئولین و نخبگان باید پیش‌قدم باشند؛ مسئولین با اتخاذ تدابیر و تمهیداتی که مصرف بهینه‌ انرژی را مقدور سازد و نخبگان با ارائه طرح‌های مبتکرانه و خلاقانه در راستای تحقق مصرف بهینه‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/akhbarefori/652382" target="_blank">📅 13:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652381">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZGwWq49As_WLfCAYQkXjfQiMXb-hpPQwOEOMDfiQr4i3BfPkUTQCcvS-sm--PszCBBQOWitN-RcsOjgI1aOi_FgXI3Ncyqkb0fY5sb8r8kqVq7i3r8Kcc6bHiuYgMidYSaRhNAgvxZPkL_7GDAV5J_-MYwk21aX7dHALSFBU23bNz1oBr6aK2Iz6v55fwZXxyjzEPrasVSuZtZPXMLlY5FiA7kEP_9TBYjNpCzNhc_feV4DLoun5LQ-gcPu2KPSvjSlLq_p-x7WWl9WB7rZO2dngdckrIwbmZHwxnZxoZOSpkSGWb4Pz6SucLznyvafGd07twZwjMONNsLC27xvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهم‌ترین نیاز امروز و فردای کشور تحکیم پیوند ملت، دولت و حاکمیت است
حجت‌الاسلام و المسلمین ابوترابی در خطبه‌‌های نمازجمعه تهران:
🔹
جنگ فقط میدان احساس نیست میدان تشخیص هم هست، در دوران جنگ جامعه‌ای عقلانی است که به استحکام دورنی قدرت و تحکیم پیوندهای ملی، دینی و افزایش سرمایه اجتماعی می‌اندیشد
🔹
آنچه در این نبرد مورد تجاوز قرار گرفت بخشی از حافظه تاریخی و تداوم تمدنی ایران بود، آمریکا خواست امروز ایران را محو کند ناخواسته دیروز بلند ایران را به یاد جهان آورد، این روزها ایران فقط در میدان نبرد و دیپلماسی اقتدار خود را به نمایش نگذارد، در میدان زندگی هم ایستاد و حکمرانی جوشیده از درون ملت را عینیت بخشید
🔹
مهم‌ترین نیاز امروز و فردای کشور تحکیم پیوند ملت، دولت و حاکمیت است ، تحلیل‌های سیاسی باید بر پایه عقلانیت، دانش، گزاره‌ها و داده‌های صحیح ارائه گردد، ارائه تحلیل‌های نادرست مبتنی بر داده‌های غلط و تحریف شده زمینه‌ساز تخریب سرمایه اجتماعی و فرسایش اعتماد عمومی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/akhbarefori/652381" target="_blank">📅 13:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652380">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آمریکا بازهم دبه کرد و پیشنهاد ۱۴ ماده‌ای ایران را نپذیرفت
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره شروط پایان جنگ را داده است.
آمریکا با رد پیشنهادات تهران، بار دیگر مواضع باج‌خواهانه خود در موضوعات مختلف بخصوص در بحث هسته‌ای را تکرار کرده است.
گفتنی است ایران پیشنهاد خود را مبتنی بر مذاکرات دو مرحله ای ارائه کرده بود که در مرحله اول منجر به پایان جنگ و انجام پنج اقدام اعتمادساز از طرف آمریکا می شد این شروط شامل برداشتن تمام تحریم‌ها، پرداخت پولهای بلوکه شده، پرداخت خسارت‌های جنگ و غرامت، به رسمیت شناختن حاکمیت ایران بر تنگه هرمز  و پایان جنگ در همه جبهه‌ها از طرف امریکا می شد و در صورت تحقق شروط ایران، مرحله دوم مذاکرات با موضوعات دیگر طراحی می شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/652380" target="_blank">📅 13:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652379">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3FRjqpeccCUdR4sA1_OZjUOapOwVQ2cj-cAl9viW2YEFWe_xvfbBV71OxbNtFstpXRTXZNKGwTci018BBUGEInULTW0ZjcK4YPPCPKTwnc1BchzZ73qZFfB24RR7PuYCYzhLmByG-fcjfzoIcIG9FrHDkzgjOQ4wzrgaiygrD5FFR4N7qnHS0WK225El90I4ruxHwaeYQTIri7Fkqi-vvJn5CP92i3N1DM9mjvvo4jyz2lBuH8s5m8uF6YGGf--mKX386m5_WVAZGb_tNIG8bF4Ldokpi2q8-z47luW4jKage9HlJ_b1BGt-KIQmTHeUUJLvsvmJ3vbsiVGB-iwjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حماس: هرگونه صحبت از خلع سلاح مقاومت همسویی با اهداف دشمن است
🔹
جنبش مقاومت اسلامی فلسطین (حماس) اعلام کرد: هرگونه صحبت از خلع سلاح مقاومت در حالی که اشغالگری و جنایات آن ادامه دارد، همسویی با اهداف دشمن در تحکیم تجاوزگری تلقی می‌شود.
🔹
جنبش حماس تأکید کرد که «مقاومت با تمامی مظاهر آن، حقی طبیعی و مشروع است که پیمان‌ها، قوانین بین‌المللی و آموزه‌های الهی برای ملت‌های تحت اشغال تضمین کرده‌اند.»
🔹
این جنبش عنوان داشت که «اشغالگری، هر چقدر هم که طولانی شود و فداکاری‌ها هرچه باشد، هیچ مشروعیت یا حاکمیتی بر سرزمین فلسطین ایجاد نمی‌کند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/akhbarefori/652379" target="_blank">📅 13:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652378">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcr_lgrp0M3nZyVaqFbr65-Ikvy3rBT5zu-FakRgkhTEFCb3yu6Hm0c5sSyT9TJWQ2leRdW6a9Cerx7K50_JZsmcpn7KNMakTozfH1hqt1IITKVU5zRURojaxjX2b6D5Sc-b6pTY9tyPkKKI8HJJGYq9C2BbPz9Las30r3dgh7LLVC2NcnOD7ZeaK7O1Htbfq5AkaamckuB6EyXrl17e2KjfMs6r4-JjgTHs2-zVvAgjlL90m6mKeGMjns_aV8-kUG76fWMXHL6Wwx41EDd0jFcJ2_yLX1feEWGYMjOJ_MG7PzWcWnrh6tLIn2lXkVgTCITJGiy4otQUDwRMxIYRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش تند قطر به یورش وزیر صهیونیست به مسجد الاقصی
🔹
قطر با اشاره به یورش وزیر صهیونیست به مسجدالاقصی اعلام کرد: این اقدام، نقض آشکار قوانین بین‌المللی، تحریک احساسات مسلمانان و تلاشی خطرناک برای تحمیل واقعیتی جدید در قدس اشغالی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/652378" target="_blank">📅 13:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652377">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ایران جزو ۱۰ کشور برتر جهان در مصرف پلاستیک است
سمیه رفیعی، عضو کمیسیون محیط‌زیست مجلس شورای اسلامی:
🔹
متأسفانه ایران جزو ۱۰ کشور برتر جهان در زمینه مصرف پلاستیک است.
🔹
با وجود اینکه مردم ایران دانش و سازگاری بومی نسبتاً مناسبی در زمینه صرفه‌جویی و مدیریت مصرف پلاستیک دارند، اکنون در بحث تولید این محصولات با چالش‌هایی روبرو شده‌ایم.
🔹
باید این تهدید را به فرصت تبدیل نموده و استفاده از محصولات پلاستیکی در زندگی روزمره را به حداقل برسانیم.
🔹
مصرف بی‌محابای پلاستیک در سال‌های آینده می‌تواند مشکلات متعددی را در زمینه مدیریت پسماندهای پلاستیکی ایجاد کند.
🔹
از آنجا که هنوز راه‌حلی قطعی برای مدیریت این پسماندها وجود ندارد، از هموطنان عزیز تقاضا می‌شود با کاهش مصرف پلاستیک، به حفظ آینده فرزندان و پایداری کشور عزیزمان کمک نمایند./جریان
#نه_به_پلاستیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/akhbarefori/652377" target="_blank">📅 13:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652376">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ثبت ۲۵۰ هزار دادخواست و شکایت علیه آمریکا و رژیم صهیونیستی
🔹
معاون قضایی دادستان کل کشور: ۲۵۰ هزار دادخواست حقوقی و شکایت کیفری در رابطه‌ با جنایات جنگی آمریکا و رژیم صهیونیستی ثبت شده و در محاکم و شعب ویژه دادسرا‌ها و دادگاه‌ها درحال رسیدگی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/akhbarefori/652376" target="_blank">📅 12:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652375">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای بلومبرگ:
🔹
امارات متحده عربی در طول جنگ، تلاش کرد عربستان سعودی، قطر و دیگر همسایگان را به پیوستن به یک واکنش نظامی هماهنگ علیه ایران ترغیب کند، اما شکست خورد
🔹
منابع آگاه می‌گویند شیخ محمد بن زاید شخصاً با محمد بن سلمان و دیگر رهبران منطقه تماس گرفت ولی هیچ‌کدام موافقت به مشارکت نکردند. در نهایت امارات به تنهایی و کوتاه عمل کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/akhbarefori/652375" target="_blank">📅 12:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652374">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a8cdcd60.mp4?token=IASU1b_b8O4nE7qC5keeyAmGzCOLISjXJJQbSbEb3s9V0jOmE9XSNieCkzgpCFH4Z4usKN_4eEF2gA1DdGXIPO6F0f6Vvxb3XR1zQ27QSBmvvnSXw55L_jzCYqGBvhDppuoVLeJL1B3EPGqdVYABoGPaE54h7neaQuWjJcuKLJ0ygtEpZmiEGP19tzUYhHW5n0O9AQyIfoYT9W1RtBAao79i3NuWh5abnOSRajEDxOz88AT_bAAlOUIHclgoofOP31EgI2iXzXdXEUUy82iO6k0ROjtTubGTkmDURwR-GQyv1otD4RR3JUBaoIhOcgLctht9yyyFIszFRouOSmJoPJRJ0zSSWFS_RySSR8gMJ0sbChuxYrk0yoyNJLYQLg8GVY1WIgnh4I7rYkLuGaNmzFGnxflj8FDa4xwC_nhnEgWDnhXyzJQrndSm7CFRK7BfuHMuFVIEqbisHXH2Cei9eWxblwlBIGhWtc5AkRKVJcn6cBiBHF7E6Bjw9PB-YgNeH8eMtV_YLlI64zPrFFY5oaKXzzKK_WELHEDiQ5slBgH_2gmjLei2Ax4zBFgNvNOM0iqRMgdbt85Xo6_ZUF0ELicuKvW9qpm8WGRG5ZJGFzLEHKQImHNSbuV-e3YYYDpvDLxSHBjIAOLXgsVhz1I25pGRME-B6y1q3l9LAfs7Ooo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a8cdcd60.mp4?token=IASU1b_b8O4nE7qC5keeyAmGzCOLISjXJJQbSbEb3s9V0jOmE9XSNieCkzgpCFH4Z4usKN_4eEF2gA1DdGXIPO6F0f6Vvxb3XR1zQ27QSBmvvnSXw55L_jzCYqGBvhDppuoVLeJL1B3EPGqdVYABoGPaE54h7neaQuWjJcuKLJ0ygtEpZmiEGP19tzUYhHW5n0O9AQyIfoYT9W1RtBAao79i3NuWh5abnOSRajEDxOz88AT_bAAlOUIHclgoofOP31EgI2iXzXdXEUUy82iO6k0ROjtTubGTkmDURwR-GQyv1otD4RR3JUBaoIhOcgLctht9yyyFIszFRouOSmJoPJRJ0zSSWFS_RySSR8gMJ0sbChuxYrk0yoyNJLYQLg8GVY1WIgnh4I7rYkLuGaNmzFGnxflj8FDa4xwC_nhnEgWDnhXyzJQrndSm7CFRK7BfuHMuFVIEqbisHXH2Cei9eWxblwlBIGhWtc5AkRKVJcn6cBiBHF7E6Bjw9PB-YgNeH8eMtV_YLlI64zPrFFY5oaKXzzKK_WELHEDiQ5slBgH_2gmjLei2Ax4zBFgNvNOM0iqRMgdbt85Xo6_ZUF0ELicuKvW9qpm8WGRG5ZJGFzLEHKQImHNSbuV-e3YYYDpvDLxSHBjIAOLXgsVhz1I25pGRME-B6y1q3l9LAfs7Ooo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: مهم‌ترین مشکل گفت‌وگوها، پیام‌های متناقضی است که از سوی آمریکایی‌ها از طریق اظهارنظرها، مصاحبه‌ها و مواضع مختلف دریافت می‌کنیم
🔹
در موضوع تنگهٔ هرمز ما مقصر نیستیم. ما آغازگر این جنگ نبودیم؛ ما فقط از خود دفاع می‌کنیم و معتقدم حق کامل دفاع مشروع را داریم.
🔹
تنگه هرمز برای کشورهای دوست، بسته نیست. این محدودیت تنها برای دشمنان ما اعمال می‌شود.
🔹
کشتی‌های متعلق به کشورهای دوست و سایر کشورها فقط ملزم هستند عبور خود را با نیروهای نظامی ما هماهنگ کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/akhbarefori/652374" target="_blank">📅 12:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652373">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YInWaibOOUuvITj-DeS-lGlPc5j1-o1vTPL3Lh__qUnzX7V65ILzKDtG2AxNd95LvG6Gr3CQRfzNYkuhz6kIM5M89xXvQFKlKt79DgaPQ1y4CX5oOAF0O3kXIGN89A1veiGcJdYGsWLQ0IgL1pxdI2dBn7Uh7AJyN92H6nf_ETUOoI2lKVs7Rg_2h7vgBeO9LstrIZezu-TqLHMCB-1F44CbJSmOZUR4uKhBlQzjuz55DPH7cvjqxXW0UbNtlpFLEZ8wjDAIkKYxA-UPEpsyVIRZHSN4Ch0QhxgwWm91U7qI9__J45x7QtfpLecDmwGWH_pz4XvCqyee_umRzXVO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال‌تایمز: اگر تا ماه آینده تنگهٔ هرمز باز نشود، به‌دلیل تخلیهٔ ذخایر استراتژیک شاهد موج گسترده‌تری از کمبودهای جهانی و افزایش قیمت‌ها در حوزهٔ انرژی خواهیم بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/652373" target="_blank">📅 12:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652372">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwHuWknrBP6aiRCk2CydV20KClBX-IIx1gzaq965of6BY9p3K6UCM149rxGhhl1_ejQnpcSN14wi5ltpnt8-zRP_B9KhNNlsqfIh1GhNDL6z9eZm9W3zW2KQrd2DUDM0YwVkjH5S663l3r_VXix8G0Kontkuto0ub07rt69FTwhKCDaoV0PWs-roMG10Ynha0NJ9H1G6ecXKidXCaOTnD0_JeO2jj0ZrGfdqKa9ay4Wt-ZmDLN91d7_vGBKnif2zyUv1mKFHqApjgUc0JHtDk8ZW1oyECUXoOUuVgpRi_JQp8QtQwkp2g9w1QRQA4oBJvKBuPSym8jbjmjMpI3q0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بن‌گویر: طرح‌هایی برای شهرک‌سازی در لبنان داریم
🔹
ایتمار بن‌گویر، وزیر امنیت داخلی رژیم صهیونیستی در سخنرانی خود در جریان مراسم «روز اورشلیم»، به مناسبت سالگرد اشغال اورشلیم شرقی در سال ۱۹۶۷ گفت: «ما همچنین طرح‌هایی برای تشویق به مهاجرت از غزه و یهودا و سامره (کرانه باختری) داریم». وی در عین حال تمایل خود را برای ایجاد شهرک‌های صهیونیست‌نشین در داخل خاک لبنان ابراز کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/akhbarefori/652372" target="_blank">📅 11:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652371">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmb1tSWTucxM1hDpUyMImyLE444_dI5Q8oH904pWzOq6uJF6lgSunpXIv8xGBwcXOIkoOTo5AHjqZ601a_SXbjY_ba7B4vBaPoqfu4830T8eCP_8l03DtxwS8n4O3KACmMZ658eKK434I5YwGou9FhgeGe6fsaZ6rJtCk574zLMY-Ca3LcQL4EONrV8wCiQUGXGnNN2QW4o4xDR8oBWD7MnBENas3qGyLbUQ0XKdPXNFIOqhHWyoxVfAIXiSFsH4iI1aQ6ZJ5wN_buPaexzyIsPuQvuZTMg1ruT58YHvpLRaj9CpZBLuTRr47oB74z6p05bAlTTS0F5Lug0zGky1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده کل ارتش: تا آخرین قطره خون از ایران دفاع می‌کنیم
🔹
امیر سرلشکر حاتمی: این قدرت ایمان است که می‌تواند یک جنگنده اف-۵ را به فراز مواضع نیروهای آمریکایی در کویت برساند، در حالی که آن‌ها از پیشرفته‌ترین سامانه‌های پدافندی زمین‌پایه و هوایی برخوردارند، مأموریت خود را انجام دهد و با آرامش کامل بازگردد.
🔹
نیروهای مسلح با تمام قوا از تمامیت ارضی، استقلال کشور و نظام جمهوری اسلامی ایران پاسداری خواهند کرد.
🔹
ما به مردم عزیز ایران اطمینان می‌دهیم که با تمام وجود، تا آخرین قطره خون و ان‌شاءالله تا تحقق پیروزی کامل، به این مأموریت مقدس ادامه خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/652371" target="_blank">📅 11:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652370">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsDPtCiihq2ldi027HGOnvc5G1LDrD3E5h2o_7nJJYY4Ngh3OQUW5Otn57UxSpCYaJfF3VTs2Plpui9DR7xQXIuXoXuIoFhbz_Jeay23OlfKLgEQrPHzN5E5E0Tu0Q6QIe4xNTS8A8tvlrCPYUPWwTCTXn5dE3mmEepCU4rZzuALypCEb_vJUcNK5NMFKpSCOZR9W9PtrvvLnXD4eQWgNlMFq0z5hXdOu_KXXfjFyH5d-uqCeEu6KRxKfQY-euLV4zC1v_J3PdYNzIEUVkfuxTn25wi91OdqAB_OjF7tkz2bBAHI3mX82gJP9L-3AfoGm212_-z2QibfdwBPn-gh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاوروف: جنگ علیه ایران باید فوراً تمام شود
🔹
«سرگئی لاوروف» وزیر امور خارجه فدراسیون روسیه امروز خواستار پایان فوری جنگ تحمیلی آمریکا و رژیم صهیونیستی علیه جمهوری اسلامی ایران شد.
🔹
لاوروف در گفتگو با خبرنگاران در نشست اعضای «بریکس» در هند ضمن تاکید بر لزوم پایان هرگونه درگیری نظامی علیه ایران، خواستار تسهیل عبور و مرور در تنگه هرمز شد.
🔹
«وظیفه اصلی در حال حاضر در رابطه با ایران، پایان دادن فوری به جنگ و دستیابی به یک توافق پایدار است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/652370" target="_blank">📅 11:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652369">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJw5jbdi2yLyt93JMBrSPr6MmOVKJmmReOAa0EnhjN-OM9q5Otc5r0_SEhQa3BnvoahIM5ThihZADpIFRpBAyUWOkujBRr19H4UxzlrsBExTaWUiulb4BqyT1JvgWFgHddYq05AnZqjG9ugpGhWZtf6PJJJuS7wvgHiRccZSeLdh7oFj3AEkCXJmV2HCRNRleHZeCN5ETAie4kp89zgW1jKrOjS66cZLSSV_NTutCrdQX4lIUE_NgvmLOm_NaIfcOZpmGw17k3SssEXPfnDSI-25rze684iKQNI9eYICJ8_L3jT7AxEIbSZsmWNj2NDBguLnsryMcKAHs8C-CWpbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح تامین سرمایهٔ در گردش واحدهای تولیدی از خردادماه
🔹
رحیمی، مشاور معاون اقتصادی وزیر اقتصاد: اولویت ما برای آینده، تامین سرمایه در گردش و حفظ اشتغال و نیرو است.
🔹
با تامین تسهیلات حفظ اشتغال بنگاه‌های تولید، در گام بعدی، وام برای تامین سرمایه در گردش واحدهای تولیدی است؛ این وام برای سرمایه در گردش بنگاهها منهای حقوق کارگران پرداخت می‌شود که از اول خرداد اجرایی خواهد شد.
🔹
در این طرح معادل ۱۰ درصد از میزان فروش سال ۱۴۰۳ که در سال ۱۴۰۴ حسابرسی شده را به‌عنوان سرمایه در گردش به بنگاه می‌دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/akhbarefori/652369" target="_blank">📅 10:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652368">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqnbkgWkiNSzMSKLAyYAamx03DW9JxOra6XDUrR8ILxIFjIRZwYYk0SVhyeI_Yr9J3EPZxSVk3lh09TI5bfl0eh1OYcnypdtgoqW9hp8VX4NXbvd9gx_gsv6UYnhGBFsuVOFsZnV1lqgCaT2fLIKpkuCgTWr5UyS1kjsWRqrsMv4hG5tesNDHRZBXuRAiqXu70NfjHhoKja3iB5wnP9kAOet80xjYvHe0e8sryxL1jI3H6bogWL-6Mb1kA-UiuOXZlU5gvIuP4ERL34i_SP815THJ0wGg-ETkTOQiPgt5tzJI_edCkiFbd2X95QeOOvA291rKzWP0hZr54iI6L73BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز بدون پلاستیک از صبح شروع میشه
🔹
یک شروع کوچک در صبح، قدمی بزرگ برای زمینی پاک‌تر  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/akhbarefori/652368" target="_blank">📅 10:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_tfZ1DMvPzlVnGihrTcdsc5dm6j8vXmPACq_D3-nIpmqIh-5NULSvUfZUmTAm6JkqBtIT-80qJQrkiEj9oTy0xgrSD4IfpLopMQEhaJaV0AdaYdbczArdW0Bn3Gp9fW-BZFWvPVRwR_AXMI5n1WzQSzNirbhx9DZhbbBdpPyO_u3PlKlXBbGt4_dwDDe-BSfjuPpv8Eqq_f-KnjqNGrrvG3YweNp-_h6p2kXZjbnVKw5I3FzWYiiZpK8ydivop34w73bqE79llHCJaL6jGbbzTlVi9DcKDgWc5mcOmumkxbse_Kf31J9xQRzBOviMyFPJDeQMoD3d8pweDulH3rqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از اعدام جاسوسان تا مصادره اموال؛ قوه قضاییه در این ۷۷ روز چه کرد؟
🔹
در ایام جنگ، قوه قضاییه با تمرکز بر پرونده‌های امنیتی، اقدام به صدور احکام قضایی و توقیف بخشی از اموال مرتبط با این پرونده‌ها کرده است.
🔹
در مجموع، ۱۰ جاسوس حرفه‌ای موساد و سیا در این بازه زمانی اعدام شدند.
🔹
سخنگوی قوه قضاییه اعلام کرده بود که تا ۲۳ اردیبهشت ۱۴۰۵، ۲۶۲ فقره ملک در سطح کشور توقیف شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/akhbarefori/652367" target="_blank">📅 10:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZXV54Ahv11Y2LHCMVT8YxdZVJr3vfFN7-AYkMryFPYS-0KeiwMSPpeWtqnj5bHimisdHQVghKA3QTC7HyngiHjQKsTiv7On0emcdvZMLFiVsLtET5j4zS-9NJukP_Df2iMYSfwRkaKaSd2mM-ng2ga4njwMxEynaEFXGxv-YDK-IVEJiV6CbgX4nMMlo-5-nZAXVC_abtZYvsYOB6FtmaaC4kAOYqDzbnbCfta-El8cgcE8NfulguW-YU6nlFF8W86N_zu5L-FsLNHApzal_kkOTlX87SQnkH4q9e9JMBTZ1O3aQ-YzPSM7Gj505SDPtjmqhgvHtYMj7I2WUv1eoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چین: در مسئله هسته‌ای ایران، استفاده از زور به بن‌بست رسیده است
🔹
وزارت خارجه چین: استفاده از زور درباره مسئله هسته‌ای ایران به بن‌بست رسیده و راه حل نظامی پاسخگو نیست.
🔹
درگیری بین ایران و آمریکا هرگز نباید اتفاق می‌افتاد، نیازی به ادامه آن نیست و پکن همواره معتقد بوده که گفتگو و مذاکره بهترین راه است و بايد يک راه حل فوری پيدا شود.
🔹
وزارت خارجه چین خواستار آتش بس جامع و دائمی شد و تاکید کرد دستیابی به یک راه حلی سریع برای پایان دادن به این بحران به نفع همه خواهد بود و پکن به همکاری با جامعه بین‌المللی برای حمایت قوی‌تر از مذاکرات صلح بین ایران و واشنگتن ادامه خواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/akhbarefori/652366" target="_blank">📅 09:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAp-80YoVYoIw2sRaFqKhzJ-i_MEPOcumFcZQgNan85x3kBM8-s8g10cPRiHPLFmqCRU5SMHo8vc1HnLEjJK4DtgvbsTJR9Yrw1lmfRlJvjyLUZ6sRnu8Ob9s6MyeUS_18AwL3ySKKm47A6pLuIlUREzKCoz2HFBcsUFE1wH5RHsTrsvX--jp5k1ULtrJQvu98zPDyY8uFgf3dEc2yVQ0XuI38i_tbBE7KDwQ6BLsfFXI7OsupfCLUUKL0Trd2K2BE6fLmlx7grxDDUIVsQFSmdDaQRzxSSQNRJhkETMi_BUGjqqxPz8AUdcO7ESIW_SuTy4Xz8t8ReJnWLRJQ2zhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: شورای امنیت نماد بارز ناکارآمدی و عدم توازن است
🔹
نمونهٔ آشکار ناکارآمدی این شورا سکوت در برابر جنگ تحمیلی و تجاوزکارانه آمریکا و رژیم صهیونیستی علیه ایران است.
🔹
در این جنگ، زنان و کودکان به‌صورت سیستماتیک و هدفمند هدف حمله قرار گرفتند. این اقدامات، نقض فاحش کنوانسیون‌های چهارگانه ژنو و مصداق بارز جنایت جنگی و جنایت علیه بشریت است.
🔹
فاجعه‌بارترین نمونه، حملهٔ دو مرحله‌ای به مدرسهٔ شهر میناب بود که طی آن ۱۶۸ دانش‌آموز و معلم در مکان آموزشی به شهادت رسیدند.
🔹
جامعهٔ جهانی باید معیارهای دوگانه را کنار بگذارد و نشان دهد که جان یک کودک در میناب، به اندازه جان یک کودک در هر نقطهٔ دیگر جهان ارزشمند است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/akhbarefori/652365" target="_blank">📅 09:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
قاچاقچی‌ها بخشی از گازوئیل صنعت را تامین می‌کنند
🔹
اطلاعات رسیده از وزارت صمت نشان می‌دهد، سال گذشته صنایع مجبور شدند ۶۰۰ میلیون لیتر گازوئیل مورد نیاز خود را از شبکهٔ قاچاق تامین کنند.
🔹
سال قبل نرخ گازوئیل قاچاق در مناطقی تا ۱۵ هزار تومان نیز بالا رفته بود.به عبارت دیگر کمبود تامین گازوئیل صنعت سبب شده تا ۹ هزار میلیارد تومان از بخش تولید به جیب قاچاقچی‌ها برود.
🔹
در سال ۱۴۰۴، ۳.۹ میلیارد لیتر از تقاضای بخش صنعت توسط زیرمجموعهٔ وزارت نفت تاییدیه گرفته اما تنها ۳.۳ میلیارد لیتر این میزان تامین شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/akhbarefori/652364" target="_blank">📅 09:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652363">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohebqCtZTqXJMpyRwnjX-ToLwlyHuXbFBOQkU0MsUp8DFUw-0ae8dSLPMarzRhIIfvLoNLlVd40t0q2sGXCxPcyz4qFevE8CT4CCgTr_y8y9kg-yweF_TgfRTJGy32H1Y-f-IG99nI2DRd5HmlstUJMOrUgzBGu0ccLUwcR8bV4-Xx0vT6Ti9XImtsxHW2V8sR6RZN8qu0SdTUQpwtRuGRCrnSPWWaYGU6CGaZAHX-BorkESr6_yeOS2Oeh8aAqz_wBV4IkSNoNj3p5I1ASBXvuaWWMmUVqXKB8Jrm2vMXO8e_nvheu39Tgla3Txj2umLa6ar_JpobqOhavokY7YRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکو: روسیه با اوکراین در جنگ نیست، بلکه با کل ناتو در جنگ است
🔹
نماینده دائم روسیه در سازمان امنیت و همکاری اروپا تصریح کرد: روسیه با اوکراین در جنگ نیست، بلکه با کل بلوک ناتو در جنگ است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/akhbarefori/652363" target="_blank">📅 09:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652362">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
«تامی داکورث» سناتور آمریکایی: ترامپ تنها در دو ماه اهداف نهایی متعددی را در جنگ علیه ایران تعیین کرد و از تسلیم بی‌قید و شرط و تغییر نظام ایران صحبت می‌کند که هیچ‌کدام محقق نشده‌اند
🔹
رئیس‌جمهور در ارائه یک هدف نهایی روشن، شکست خورده و هفتگی اهداف جدید و محقق نشده‌ای را اعلام می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/652362" target="_blank">📅 09:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652361">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2Wa_sh0pPAoxijncXx7J0DRrqZrcMkvw-AboK7oL03elYDNcnntmmHG-PVsDvYLw6FjaZV6vnd6Bp4ownrjx5AD-ZHTVs8zrGh8hQTnEuNndsPNdZVF7qe1Y2-T5x9hs0buu0KUDRGmKO5yn1VY309QS_DugE5KazW7CB3hg7LDFRrqWEORfiEewtnE5PB6CgFKf1YrdcJsDYy6631zZEgAPuw-gLiUtw6EYdWDqvfkqEZGtvT-quH6U447ViKjoI2TT1p_zD0ZnhdjucS0sJM2g4eZxbzZKPN6u0VYOWlakK2V9KgkrT9hz3mW7SnOqX5hKTlRaq48ehHdUOzWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرط جدید دولت برای متقاضیان یورو با کارت ملی
🔹
مرکز اطلاعات مالی وزارت اقتصاد، ثبت مشخصات دریافت‌کننده، هدف دریافت ارز و محل و نحوهٔ هزینه‌کرد وجوه نقدی درخواستی برای متقاضیان دریافت ارز با کارت ملی را اجباری کرد.
🔹
بر این اساس، بانک‌ها و صرافی‌های مجاز موظف‌اند اطلاعات دریافت‌شده را در سامانه‌های مربوط ثبت کرده و سوابق معاملات ارزی را مطابق الزامات نظارتی نگهداری کنند.
🔹
بانک مرکزی به‌تازگی اعلام کرده به همه متقاضیان بالای ۱۸ سال در هر سال، معادل ۱۰۰۰ یورو با کارت ملی خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/akhbarefori/652361" target="_blank">📅 09:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652360">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0xU57vqEy-9S_V5B-WxWW9U8CJerStncRNZwHYCMf3ZeGeT_OsvSCkWi0k6F2uLuP3y5qsbMIs0Y_PhZroOrAR3_f9gQo02rDN4s72Kp87z_5PVlM9yufqc8grPrio0fCGv1x-wvAzGwsL5RVbqHeRSZnoVjTWuRuw5PSbPyo0kBmTh-3oGu853SRIj8MK8-415m2kSIV4esUO8UIXuwJmIDrmxn3ddOC5xhKEBESZy-U_9Kcu5N3pohWw6fSUETyp_XXnS-QcyR6V8udWRBMD1eJd7xYPP7NjBVUHNyJCvEYvQDZbSDehZxUNQtrxg-UfZhYYsgBOqi0oTxVW6TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳۰ روز بدون پلاستیک
🔹
تو امروز انتخاب می‌کنی، فردا زمین ازت تشکر می‌کنه   شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/652360" target="_blank">📅 08:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652359">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
سخنگوی ارتش رژیم صهیونیستی از هلاکت یک سرباز صهیونیست در درگیری با حزب‌الله خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/akhbarefori/652359" target="_blank">📅 08:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652358">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5Ek8EJIFCzXMbNlWgrTLrhZapzsf9VSEXxxLW9FgIvBlzpqiP41Tf41O6Z01747UWV-jyUau0eUXJlViesZffgCIGhpI9fdjjNtBZBGaB0-SdE2NOKYp5nsCBmS488_IoVxgNUbzTXWsa3uMsDnHIQJKGEJWYfqttpIckdT_-M_ndV6mD1GYGIM2mXWPj9_J75L8zguLWOGfV7oA6K4zvTACjBKa4YM-wvsgQHIyK3q3O56jnVuQ7-IeF_QQon8GaCJisdtgwUJXtCpqQPqXB_-bGS0T4Af3PLx9f1yrhCc3MkGoXRM1nypN_Sr-T7s3i6yX1hy0JPFSOQlXGX3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهر بررسی کرد؛‌ احیا یا افول؟/ چرا برآورد غرب در خصوص وضعیت محور مقاومت درست نبود؟
🔹
ایران در طول جنگ رمضان نشان داد که برخلاف برآورد غرب، در موقعیت ضعف قرار ندارد. تاب‌آوری عملیاتی، توان پاسخ‌گویی مرحله‌ای و حفظ ابتکار عمل در مقاطع مختلف جنگ، نشان داد که ساختار قدرت ایران همچنان پایدار است.
🔹
جنگ اخیر نشان داد که محور مقاومت نه‌تنها دچار فرسایش نشده، بلکه توانایی هماهنگی عملیاتی در چند جبهه را به‌صورت هم‌زمان حفظ کرده است.
🔹
فعال شدن جبهه‌های لبنان، عراق، یمن به صورت موازی و تحرکات دریای سرخ نشان داد که محور مقاومت قادر است در شرایط فشار، الگوی رفتاری چندلایه و مرحله‌ای ارائه دهد؛ الگویی که از وجود انسجام و مدیریت میدانی حکایت دارد.
🔹
جنگ رمضان نشان داد که روایت ضعف ایران و محور مقاومت، یک برساخت سیاسی بوده که بیش از آنکه بر واقعیت‌های میدانی تکیه داشته باشد، بر نیازهای سیاسی و فشار لابی‌ها استوار بود و میدان، خلاف این روایت را ثابت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/652358" target="_blank">📅 08:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652357">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be64a7f7c3.mp4?token=WSmGaz2AYQJRzyIxFIm8v4SGKI7kPPMJ6HjVcGnwpz27lQmzQ3zyeUxYpEpvpXjPyTf8I5YiAXtN5t2noAC-Pda-Q3VUsW1nwDS-ECtgMUE737LcfQpEkMugajuyRcSaIRrA1_-SKQS_bufm7K3FfXw1yP0NDiqmMYJssPg3R2omoiT0jl81Tz2Gy5xUAGhMyJ7UMcLNe4lEWgbJ17o-PDBAkixFm5xkAeq7f5RWCWWAkO_qQxnT4XgAOExXA2zyaT4JgTVyfk9RMJCxYc_N2C6lzVT0wPFhsbJTTlcTHYPBEZA9_93vW6L6P63hhfo5GDa4pvqAbinMn60NAjfEBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be64a7f7c3.mp4?token=WSmGaz2AYQJRzyIxFIm8v4SGKI7kPPMJ6HjVcGnwpz27lQmzQ3zyeUxYpEpvpXjPyTf8I5YiAXtN5t2noAC-Pda-Q3VUsW1nwDS-ECtgMUE737LcfQpEkMugajuyRcSaIRrA1_-SKQS_bufm7K3FfXw1yP0NDiqmMYJssPg3R2omoiT0jl81Tz2Gy5xUAGhMyJ7UMcLNe4lEWgbJ17o-PDBAkixFm5xkAeq7f5RWCWWAkO_qQxnT4XgAOExXA2zyaT4JgTVyfk9RMJCxYc_N2C6lzVT0wPFhsbJTTlcTHYPBEZA9_93vW6L6P63hhfo5GDa4pvqAbinMn60NAjfEBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجۀ آمریکا: در مورد ایران، درخواستی از چین نداشتیم
🔹
ترامپ هیچ درخواستی از رئیس‌جمهور چین نکرد. منظورم این است که ما در مورد ایران به‌دنبال کمک چین نیستیم؛ ما نیازی به کمک آن‌ها نداریم.
🔹
ما مسئله را بازگو می‌کنیم تا موضع خود را به‌روشنی تبیین و آن را شفاف کنیم تا آن‌ها درک کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/akhbarefori/652357" target="_blank">📅 08:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652356">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین - قسمت بیستم</div>
  <div class="tg-doc-extra">سردار عیوض‌خان جلالی</div>
</div>
<a href="https://t.me/akhbarefori/652356" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
«سردار عیوض‌خان جلالی؛ مردی از دل قدرت و توطئه»
🗓
این قسمت روایتی‌ست از یکی از چهره‌های کمتر شنیده‌شدهٔ تاریخ؛ مردی که در میانهٔ بازی‌های قدرت، جنگ‌ها و توطئه‌های درباری، نام خود را در تاریخ ثبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/akhbarefori/652356" target="_blank">📅 07:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652355">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edecf976c1.mp4?token=UUpaRWCbrzc8JJfv5y-g_li1xbFgigZ00APhdPGUHbVOlTZ4dnTA19HWy2C3JGF_kJFL_CE9jbNFuBLtbkDiVJcKJy51gDKTPsYm3eH5U4knw0ESP6Sm-_qCQvcX0I2JaIx1lC7mXEPWHSw48LCXSFBm83X4TqF7c-H6-R8kMSBGy4RFAY-eyiWEhTr5p05sXY0YmbcfGmKn3NTk_byF-E8dOPzjddnrB0lZ1u-mrWX39KiDUEO7bfxCz96QwEzJAPrxipNPVK4lP7db8LnG-Xxz4JU-6X2tHYtmAY10Li9suiVxk9Skj6vpDN65wFpmAXCh7Ll2_W2CQRT1-9jCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edecf976c1.mp4?token=UUpaRWCbrzc8JJfv5y-g_li1xbFgigZ00APhdPGUHbVOlTZ4dnTA19HWy2C3JGF_kJFL_CE9jbNFuBLtbkDiVJcKJy51gDKTPsYm3eH5U4knw0ESP6Sm-_qCQvcX0I2JaIx1lC7mXEPWHSw48LCXSFBm83X4TqF7c-H6-R8kMSBGy4RFAY-eyiWEhTr5p05sXY0YmbcfGmKn3NTk_byF-E8dOPzjddnrB0lZ1u-mrWX39KiDUEO7bfxCz96QwEzJAPrxipNPVK4lP7db8LnG-Xxz4JU-6X2tHYtmAY10Li9suiVxk9Skj6vpDN65wFpmAXCh7Ll2_W2CQRT1-9jCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادای دینی به کرمانج‌های ایران‌زمین؛
به آنان که در مرزها زیستند،
جنگیدند و در تاریخ ماندگار شدند
قسمت بیستم پادکست کافئین منتشر شد
☕️
📜
روایتی از زندگی عیوض‌خان جلالی
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
🎧
https://youtu.be/IpMt8R6uBX4?si=5ppbO4oz91FFpq6i
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/akhbarefori/652355" target="_blank">📅 07:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652354">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
کالابرگ سرپرست‌های خانوار با ارقام پایانی کد ملی ۷، ۸ و ۹ شارژ، و امکان خرید فراهم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/akhbarefori/652354" target="_blank">📅 07:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652353">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4NPeuD7Kp2uG1SsYvu3HO9lsYkAkOhPfzvqXZl5dJeayPpya8we0pCgapCNFJyeFr8EJSwcPRumKSS-FnP6W-GJzhVt6QuxAkXqxf7fS1u3XgIvmOaMYGFl3LEArNja5cmjgi88S3iuyoLrYMRFmYZTP45B5GStLgD-fXyedNG0fzc2rBkRN8aP_q5oiF8IcL0Re1TyTWpxKaVUOjngkChHAroGkG9cTnJz10FNVuBnWfwidLnS7Xo28sKFivngH6VXPogigszi3tH1O_Nnk98Ez5BnvMBsQXNJ7ofXjiGukx9aXHZ2VxGCvAi9QfnmR7vA8reaO77fErv-GWl5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۵ اردیبهشت ماه
۲۷ ذی‌القعدة ۱۴۴۷
۱۵ می ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/652353" target="_blank">📅 06:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652352">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
یونیسف: ۲۰۰ کودک لبنانی از ۲ مارس تاکنون شهید شده‌اند
🔹
طبق اعلام صندوق کودکان سازمان ملل متحد، از ۲ مارس گذشته تاکنون، در پی حملات رژیم اسرائیل به لبنان، ۲۰۰ کودک شهید و ۸۰۶ کودک دیگر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/akhbarefori/652352" target="_blank">📅 06:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652351">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ترامپ: ایران از نظر نظامی نابود شده است
🔹
رئیس‌جمهور آمریکا در ادامه ادعاهای ضد و نقیض خود بار دیگر در مصاحبه با فاکس‌نیوز مدعی شد که ایران از نظر نظامی نابود شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/652351" target="_blank">📅 04:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652350">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2e84f307.mp4?token=fXXw-oUlIUATVIMSIubXCAb9MjDit2ATJKH1subVYximDmOZD5uRJG52jYEO_HdN4vJbzSIM8EegXqLuTzH2AAmEaUjxOthVjDsBj36vbSAlkgfm2cM3y7bGkuaCpYyyep-D_wqk0gqRbXPUt1CcjtXcyY5A6AVAs1EwuTSL5BF0G4LtxKWIX4okc5yESAx6m7tgjbviMjKKJLqbmEqTqYMkPpGzQ7QaCNWOaxiUs51cbm8RBnTy_apRf-BXmx5GmyKrKTWxPCVFC_Deb6znYJkFdU-owlAUuu7cvrTHoSOtDBaxGmZyeojtmWPYW3acRYQzXCrhc_4tVteTt6uUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2e84f307.mp4?token=fXXw-oUlIUATVIMSIubXCAb9MjDit2ATJKH1subVYximDmOZD5uRJG52jYEO_HdN4vJbzSIM8EegXqLuTzH2AAmEaUjxOthVjDsBj36vbSAlkgfm2cM3y7bGkuaCpYyyep-D_wqk0gqRbXPUt1CcjtXcyY5A6AVAs1EwuTSL5BF0G4LtxKWIX4okc5yESAx6m7tgjbviMjKKJLqbmEqTqYMkPpGzQ7QaCNWOaxiUs51cbm8RBnTy_apRf-BXmx5GmyKrKTWxPCVFC_Deb6znYJkFdU-owlAUuu7cvrTHoSOtDBaxGmZyeojtmWPYW3acRYQzXCrhc_4tVteTt6uUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجلس نمایندگان آمریکا با ۲۱۲ رأی موافق در مقابل ۲۱۲ رأی مخالف به قطعنامه اختیارات جنگی برای محدود کردن اقدام نظامی علیه ایران رأی داد. این طرح با توجه به اینکه برای تصویب به اکثریت آرا نیاز داشت، شکست خورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/652350" target="_blank">📅 01:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652349">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423faf9ee6.mp4?token=IfogXBV1bUF8suxoGCSnn-zsr1eJvejc0n3y04hJ25QFpTKaJIxGZImJnYlSEU9ffUp1V--EjKH5ePLjJhv51qWkNlmdtDlfJfGkkhhHhGB56RNdllnnbTHAWnQdiaxcJAxxij4WwNbravWPH4vE27u3kpleTLl-3omOn-smxsd7Mzk5r0bikiX92p7XVJskYOTvH-H8v7_DHUC6ptwVRwZqUOGzVY0wV2T6bah1sY5sKmWENc_okF8Q_HfTKX__-QC9k17lVM-E0A5nxYCCHULHdf7pDi8V2jshyqyH71mZxf8K2GyUeHD3JcUmfKGa0TuqDIdGpOa4AERsS53OCiKR50eESBjeZTjrSMhD2orMNC8V07LFTDoYlguz6IURB-bNHPFvT6ChdcNtaiwQFl8pVcHXCZSyepip8M5VS9UcvsmPBpQGukl3h0ocf5veJNeScDP91eJjPb7j1G_nAMdw3imuJ7LvBXyGif-1DTAaQaxLCxMySn0EqsoQpKDvS0ETWZoODEQK0_QFj2-zyzLX2BMDuD0n5t3ezhbuzBcv18oLTCJXccvBPV6n6vV2bQcMuskvSCMuEtJWtZP8ZbTXcYr1OJo2ExcS1PQd4piaBD3V5Zuj2_FRLWSg7GAAXQnzV6ajoitotgQ99bPGPAcXhfH036ewG18CcYAKv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423faf9ee6.mp4?token=IfogXBV1bUF8suxoGCSnn-zsr1eJvejc0n3y04hJ25QFpTKaJIxGZImJnYlSEU9ffUp1V--EjKH5ePLjJhv51qWkNlmdtDlfJfGkkhhHhGB56RNdllnnbTHAWnQdiaxcJAxxij4WwNbravWPH4vE27u3kpleTLl-3omOn-smxsd7Mzk5r0bikiX92p7XVJskYOTvH-H8v7_DHUC6ptwVRwZqUOGzVY0wV2T6bah1sY5sKmWENc_okF8Q_HfTKX__-QC9k17lVM-E0A5nxYCCHULHdf7pDi8V2jshyqyH71mZxf8K2GyUeHD3JcUmfKGa0TuqDIdGpOa4AERsS53OCiKR50eESBjeZTjrSMhD2orMNC8V07LFTDoYlguz6IURB-bNHPFvT6ChdcNtaiwQFl8pVcHXCZSyepip8M5VS9UcvsmPBpQGukl3h0ocf5veJNeScDP91eJjPb7j1G_nAMdw3imuJ7LvBXyGif-1DTAaQaxLCxMySn0EqsoQpKDvS0ETWZoODEQK0_QFj2-zyzLX2BMDuD0n5t3ezhbuzBcv18oLTCJXccvBPV6n6vV2bQcMuskvSCMuEtJWtZP8ZbTXcYr1OJo2ExcS1PQd4piaBD3V5Zuj2_FRLWSg7GAAXQnzV6ajoitotgQ99bPGPAcXhfH036ewG18CcYAKv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد منان رئیسی، نماینده مجلس: خسارت مستقیم جنگ به ایران فقط ۳۰ میلیارد دلار برآورد می‌شود در حالی که درآمد هر سال عوارض تنگه هرمز ۵۰ میلیارد دلار خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/652349" target="_blank">📅 00:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652346">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9Zk6rST7UQB7gnFonX8VWuIWTOlZyholRD5WEoR6m6SovOOvLlDwGx8lnZJb80MK19acwzL4vogacPsJWmKDslC5Gv0m7RqT5pZw_ZmzEW0wntXmcimkLTO7DHSAP2l_Xo1ZFHcHaagtkVA9vkcbcD7Iik87NtT7OP3BKRDaHCcOdUScYooGbnNegi0OyWmalDvhbarWXZ3uiKMzKAVoV54zdANkBm9HJVyGf5vRZMiF0-mVSii779vjNQO-xcINx1LRK2YbYWIFEyhHvtkZT8Lhmav4OP3DUfyaGib0ol99gT9RnqpexUEDEui-nX4JYT99S0HP6e_BjdAVAAvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMaRjkbm4QEkYap3vo0EFhS2c-JjNnC_j_j_LZrRdKCPu9aBcKDIZOm8zCR0Q4_-6vyJK4cXIBLd7OY6wmAMs_XX40MIiu389ry1DD9XpGZtjrpWub65q596wWTCOWO9PBwSprdL8_mHDQjZhFmwqzJ8X57H_cY9mJke9awUafCWj_L35bf5P0M-kWxPuaBNYz_NSd8cLjbr_ZLkTef4qgiVn_dB6XoVmdnumKWXQY6qubXBuN-akaQ-pxsLXmsrlWteH1jp6xpunPMKUbsnu_wjUplklA5RKpeSrAf8iShMZgqi6i59RTNehZrctchPBrRAjWKOjm2ELGQfIeBpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-d67MEeZwdhLCxWK8KfCx0mqmeSREsulBv4ml67Pi-AjW-JEzg1N_26zVfjfBfOZec7hbONNeYfMYZ5Sjp10JQb30ZGJ16vUsfb6Yd7G-nvPAbfAEEaB4TS9HvkGagymMf_9BGSlQNB-66dIUga56glaZmy-8tOjtjs3OYrPuEbmN58IIm-JTeOtHwLjck9fQ71Bl1QsAfM8B1iupEF_eI0EmtrXnuhy0Yy20wJS-zvm0CvolSQCyb0leSp8dt8g8rpwa8jcpQ1B0TNuVSESJrXQ5CPnIe-5DRyYoeIub3UJBhMRi61bLbCPF-RZY9k0DWea8WD3tQsGk___WBTZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حنظله: مغز متفکر سفر نتانیاهو به امارات و معمار اصلی توافقات ابراهیم هک شد
🔹
گروه هکری حنظله اعلام کرد که با هک «ساموئل شای» طراح سفر نتانیاهو به امارات و معمار پیمان‌های ابراهیم، شبکۀ مخفی او را افشا کرده است.
🔹
به گفتۀ این گروه هکری، شای نه‌تنها هماهنگ‌کنندۀ اصلی تمام توافقات پشت‌پرده میان رژیم صهیونیستی و کشورهای حاشیه خلیج فارس است، بلکه تسهیل‌گر کلیدی روابط پنهان اقتصادی، سیاسی و امنیتی میان تل‌آویو و ابوظبی محسوب می‌شود.
🔹
براساس اسناد منتشر شده، شای، اپستاین را به «سلطان احمد بن سلیم» معرفی کرده و از این طریق بسیاری از حاکمان فاسد امارات در شبکۀ اپستاین گرفتار شده‌اند. موساد نیز از همین مسیر برای وادار کردن آن‌ها به پذیرش خواسته‌های خود استفاده کرده است.
🔹
گروه حنظله اعلام کرد امروز ۲۶۵ صفحه از تماس‌ها، شرکای مالی و ارتباطات محرمانۀ شای را به طور کامل در وب‌سایت خود منتشر کرده و تمام اطلاعات مرتبط با شبکۀ مالی او در کشورهای مقاومت را در اختیار سرویس‌های اطلاعاتی کشورهای دوست قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/652346" target="_blank">📅 00:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652345">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVSBzQOCZ3xwMTMbbYoVDKp4QPJeENEMKI2kpYaKkg_7OgtLBo5_ZuhHT6jgvqs0JSimE9qhOZUHff7S8n4gNrwGmxlm3M8KSnS3j7wUdUnzH125z8kPt65KRqujCyyjA9gJsUPqvQ8E8BYG-e3ry660dxLOUcsillzLDcCcXYVcQjQCQ9AU0pAHT5wp83IfWfJ_34gBZbEwwy2sBpXLbH3uGVdQhglhvZBY0oYnJ1AlH4MwPcXhtqMF5eWKe_sxzraT2R7h3LsgTpXoKRfC6nNwA7d1imBj4df1U7tokbSRQDKIiCRe3aJonRwoBzu0XQW_kU5IGHkmt87UrIH3gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منوی شام چینی | دیپلماسی خوشمزه | شی جینگ پینگ چه غذایی به ترامپ داد؟
🔹
در ضیافت رسمی که روز پنجشنبه در پکن برگزار شد، رؤسای‌جمهور آمریکا و چین، پشت یک میز نشستند؛ مراسمی که فراتر از یک شام تشریفاتی، نشانه‌ای از تلاش دو کشور برای بازتنظیم روابط سیاسی و اقتصادی خود تلقی شد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214964</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/652345" target="_blank">📅 00:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652344">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf56a8776d.mp4?token=lj-c2PxXfTiMGsIjlDuE6jm8Tyv37pcTxxC3EpTSW4dc-q2IvfRQ5gCPDePSqw1iwFn_M676OYVpGFE3KrOarxgNCXtCAk5NEQKQujwJlK6kOMbCjLQxiM4Akf8Wr6OSmPpjr-py_QMzmXOjPGugckUSe5Ho_PvGtbmxyTsaQbRwm-LHs-LAGYMpBgTI-KSZ6gl3Mfclmo3hE_KWYX-ZDFAulmzenuAlsCYsA4eec5q-dJdivje86plsE_IOrPSPPyBULGMxz_TKDxKRkIbpg5L6PPXulLCjxnxp7MIZf675bBE-ql1GZe_Hdt-RMZwfZIwfPzuW0UykAmCahsBZxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf56a8776d.mp4?token=lj-c2PxXfTiMGsIjlDuE6jm8Tyv37pcTxxC3EpTSW4dc-q2IvfRQ5gCPDePSqw1iwFn_M676OYVpGFE3KrOarxgNCXtCAk5NEQKQujwJlK6kOMbCjLQxiM4Akf8Wr6OSmPpjr-py_QMzmXOjPGugckUSe5Ho_PvGtbmxyTsaQbRwm-LHs-LAGYMpBgTI-KSZ6gl3Mfclmo3hE_KWYX-ZDFAulmzenuAlsCYsA4eec5q-dJdivje86plsE_IOrPSPPyBULGMxz_TKDxKRkIbpg5L6PPXulLCjxnxp7MIZf675bBE-ql1GZe_Hdt-RMZwfZIwfPzuW0UykAmCahsBZxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طفرهٔ فرمانده سنتکام از پاسخ‌گویی دربارهٔ پیش‌بینی بسته‌شدن تنگهٔ هرمز
🔹
هیرونو، سناتور آمریکایی: پیش از اینکه به ایران حمله کنیم، آیا این فکر به ذهن شما خطور کرد که ممکن است ایران تنگهٔ هرمز را ببندد؟
🔹
فرمانده سنتکام: فکر می‌کنم صحبت کردن درباره اینکه آن گزینه‌ها دقیقاً چه بودند، نامناسب باشد.
🔹
هیرونو: بسته‌شدن تنگهٔ هرمز توسط ایران به ذهن شما خطور کرد؟ بله یا خیر؟
🔹
فرمانده سنتکام: تقریباً ۱۰۰ بار از تنگه عبور کرده‌ام. من تقریباً هر روز به تنگهٔ هرمز فکر می‌کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/652344" target="_blank">📅 00:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652343">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: به دشمنان هشدار می‌دهیم اگر دچار خطای محاسباتی شده و به امنیت ملت ایران خدشه‌ای وارد کنند، امنیت آن‌ها را در هر کجای جهان که باشد، سلب خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/652343" target="_blank">📅 23:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652342">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
اگر فرصت مرور هنه خبرهای امروز را نداشته‌اید، داغ‌ترین‌ها را اینجا کلیک کنید
🔹
ترامپ پس از سفر به چین چه خواهد کرد؟ | بازگشت به پروژه آزادی یا حمله به زیرساخت‌ها؟
👇
khabarfoori.com/fa/tiny/news-3214896
🔹
وزیر جنگ اسرائیل دوباره تهدید کرد: هنوز کارمان با ایران تمام نشده!
👇
khabarfoori.com/fa/tiny/news-3214942
🔹
بلاتکلیفی درباره ترانه تیم‌ملی | معین پاسخ تاج را داد
👇
khabarfoori.com/fa/tiny/news-3214908
🔹
بحث داغ مخاطبان خبرفوری درباره حمایت از تیم‌ملی | نظر شما چیست؟
👇
khabarfoori.com/fa/tiny/news-3214858
🔹
ماجرای رابطه ایمانوئل مکرون و گلشیفته فراهانی چقدر جدی است؟ | سکوت بازیگر ایرانی و تلاش طرفداران رئیس جمهور فرانسه برای انکار یک افشاگری
👇
khabarfoori.com/fa/tiny/news-3214881
🔻
ویدئوهای جذاب هر روز را در آپارات خبرفوری ببینید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/652342" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652341">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKMDiMa0Gw51tR8RREesTMB0sHA3scl4LC-Vjywx-P4hPxKoH5gxkpzQkf26OnHQK2xNsTOvUA3d5VcVAoZcEepT7P2wV5hHKt4r2bUbOTQ4vQHfao1dI7Kbc431y9tNLh1frjpVs0t4BFxDotvaDsrNEjLASi46OAK-2Ys6E69l0P6cYY96rprE4-xRq_55wwFe8xJ6XwRrWfsee2G8vhSw5PnyY2jBep42YpZUzcSollKu7WpIyVahEAhwY1MMjjJlxWl76sAJ1tuTHDYgJ3XpKfYX10rGR8xO4Vv6II3bB_ALXFb4wQxIcYyiBIlxPMXfAgT0kfKu5ktfY3rSOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مورد عجیب یک فرد متهم به جاسوسی برای ایران در اسرائیل
تایمز اسرائیل:
🔹
یک راننده کامیون ۲۷ ساله عرب-اسرائیلی به جاسوسی برای ایران متهم شد.
🔹
ادعا شده که او به دلیل خصومت عمیق با اسرائیل، با میل و رغبت اطلاعاتی در مورد مکان‌های حساس ارائه داده و حتی خواستار حمله موشکی به زادگاهش شده است.
🔹
دادستان‌ها ادعا می‌کنند که به احمد داعاس برای فعالیت‌هایش پیشنهاد پرداخت پول داده شده بود، اما او از دریافت پول از تعهد ایدئولوژیک خود برای کمک به ایران در طول جنگ با اسرائیل خودداری کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652341" target="_blank">📅 23:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652340">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKIsGzJv7QXd2Adi8QvCZCOu26GPQ8sizDnI-KtYqCXD8tmLeLLfhq5lC0m0ZH__8NxFrPyl13SsCdRVbHFEbM1re9JQZtuGQQnou03kmLL0fdoIGz4T_lU2W-jHXupmWPhZxlB_1Wppipr6sOwrFNhqeBWjkzyPrT_swtBMwiBm6VOoARUM0JAMCZILzPKcYE9esqLDo3-UoHmFx9o_GBU5_Kuo6IJ7F5FodDEqUfb_vGvVsE8xgNajBarWt1vxVGzLkPUCYjVQNHgP5lAaus1C52thtsCDJWS1ZcZuWiwFuoXJzsyM5Vx5aRBUi00nPG8TxfXfbRkNEbmWE_cdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای رابطه ایمانوئل مکرون و گلشیفته فراهانی چقدر جدی است؟/ سکوت بازیگر ایرانی و تلاش طرفداران رئیس جمهور فرانسه برای انکار یک افشاگری
🔹
ماجرای پیامک‌های ایمانوئل مکرون به رهاورد(گلشیفته) فراهانی همچنان فیصله نیافته است. با وجود عدله‌ای مبنی بر ارتباط بین این دو شخصیت، هنوز بازیگر ایرانی عکس‌العملی نسبت به شایعات مطرح نکرده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214881</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652340" target="_blank">📅 23:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652339">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
حملات موشکی حزب‌الله به شمال فلسطین اشغالی
🔹
در پی شلیک ۶ موشک حزب الله، آژیرهای خطر در شهرک «کریات شمونه» فعال شده است.
🔹
شبکه ۱۲ اسرائیل اذعان کرد که سه موشک در اطراف کریات شمونه اصابت کرده است.
🔹
منابع صهیونیستی مطابق معمول ادعا کرده‌اند این موشکها به «مناطق باز» اصابت کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/652339" target="_blank">📅 23:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652338">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uih4MmyjezqaRnFKCi1k5Jkd6hxYk7LSYEoemBwaLAEs0nJZENuloHoHZdZVk0w8ocMjgJcMww9PGHzYlKhk9OEJ0k4xTxokIGgP-x1B2rUrgqpNJxL241pGvBvWeZ-2dDyh2SKgvxUaGnvcAtf7xhtwe2NASPPYwhl7r1r35XIZvcNDXjLEg5JCVtDQGyHMroWwpoEfD5AGcZnDVvJ-58pMeHIM0Uhkucqv5TTq6bNPJ3RLIbYv6z_Orq7q-3QHRq0IRKxxHww1fN5ARjr_5Rt6JJoUQaOS5ZA_KLSmL5-u1uhOyyY0JrFSzj89RBZZ5G8cQquI5mYE1bv9mQ3N7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک روز معمولی… اما با انتخاب‌هایی متفاوت
🔹
از صبح که چشم‌هامون رو باز می‌کنیم تا آخر شب، بارها و بارها انتخاب می‌کنیم؛ کیسه پارچه‌ای یا پلاستیکی؟ قمقمه فلزی یا بطری یکبارمصرف؟ ظرف شیشه‌ای یا پلاستیک؟ این کمپین داستان یک روز ساده است؛ روزی که با عادت‌های…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652338" target="_blank">📅 22:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652334">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6yJw-qBziafyphSNX8CJ9Z29zSIHCFVlDFvQKA-5pCGUdcEFUsP1dfzr2XAj95WlLMZx22OK_wE4dww_nfQfxSHrXbNw4DOYVBrgufI63_FXpLBGLh1tqh_lBogDJV5yZ11vtmoN0zXsogBN_bwiscK1dzDNdDdlIwgQlApgSKOn8jSyQVuYvVPPE-2zcQJVLVetoTdQWun7PGzSZw8HlBUP61arrZruTusbLSNV0eEB-JKnAc8-X9SVQ6u2GjG3mMXx_QlzBOaykPixp5rhwzKaXFXuIDnkqfkt-YdWvuwwpcyvrZSo3bYe_eBm6E66VDR7xr0tZMYOFRHLqzCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/culsHchWLyXDpTfnAtJPs8olU2uUrcdg5mCo7EAhSzgruWxe0PLIl4aQQlqla4O-2Tr4oP7UX1Fo6nWZ5DD4FKAxecboEf9CJPFFeZZOJ6g3gcz4BAxLhhJDqsMv11sHSZIhiVsg-mHsHvbw6j7WBU4gi8zoxS6mxprqESXXh2X5G8Y2Lbk2bJ9FE_j6GFjgBCqUX7pE1YIfWyf-hC-NUuf3Ye-J64U2rou_OXYS71NKwedd1hSc2loxv7TggVcLXDSCMqz3ib_9I_vg_IJurWcn6BwfKKJFPtH51EL2VIFlN-l2VJ0Xk_JLCs8qN802KAXqWthYSOva4k_BjdTMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNom6YfB7HKUP8gEgIwZa697t7lmp3VGy3M9UdVb7RWhJUTwrfdFqqlEaq2h1C75XwxD7fJzEo0Ay04ePydbqTr1hLGlNjUXnJIR9Z3yPbpj8emVV6kVHtDE86ZeTg2dEh3SMWsa1EkQeDGyGzTg6VF8XNi6F4px-GJBbDwJini3f1YNGSqWixiaua8rrMzh1LEOm43A8qlbNzlu_DRfKw4m1LsnBGqvfoYu-VmhzZnnMds_QItLRhB1TivnK4Evqdn4JMZ7i1dxPovfb4Ns5t99aa9A3fBXas0uAolUndgVLhSsTuBDQ4YKVPrW2JyZbYxWvDVkMgxC5Xvt0FNhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elzFMKMc3WlqdaH2rHbKKAFDJQwcuVJPNyA13T0fbi4x--YmfhGYC2_qcB_Faltbm2MuTcHNGFSWXVyTGAyOqui7PuMC4jvMgWx_s-TnnfiyBWdGOHo3xBvs0Lj_XjCK_7nsm5FPd-JG5gapryCATNR6g8KEYxde5mj7M9XfhykgljOrE6wBseyqMDaWoHY4J6mur0DtGHaQkIhP17Xl58pVQFdJ3218deF7YPQo1KKOmsuZAMA95ZXn4Go9uhxEXnSDOa6UGnaS8O5WyGvZZIcPs7zqPIoTQM2nww5BJjpFYnW3i5PShggQudpMa4tnw8XLYw8QVVO-HaldV5msrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تداوم نقض آتش‌بس | صهیونیست ها تأسیسات کشاورزی فلسطینیان را در شهر الخلیل به آتش کشیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652334" target="_blank">📅 22:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652333">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82aaf1c68.mp4?token=UfkDL-0k5FVTpI65J7QruyXp1sFv6TMUEApfLYVLsHVxMbUh3mb4tXvuWJKcmwiSEHe9zKwwoecJl0IQYHjkRvdyvutFx3YWzBQgvE99iHSivLT6qAIPUZSx553WchGQ50rBo7UkXMxuTTyM_SAj11CFNngojoaWZ5xLfX3WbM-uzF7lowqe6iya8Ue-e9C7yyRdGSqlvOZ57vU11pRj2Otphoi6SgY5dpcFE9jaKt60MvhOPX5m3xbuBGQ360jCz-4ygOWCA-XTywjNTsG2UMSp3i7jzJp6bkJTZmH7hWf7ueT-8XK8xLIw1S6pKraS6NOQdBFKJs8hy3ETYBmLYYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82aaf1c68.mp4?token=UfkDL-0k5FVTpI65J7QruyXp1sFv6TMUEApfLYVLsHVxMbUh3mb4tXvuWJKcmwiSEHe9zKwwoecJl0IQYHjkRvdyvutFx3YWzBQgvE99iHSivLT6qAIPUZSx553WchGQ50rBo7UkXMxuTTyM_SAj11CFNngojoaWZ5xLfX3WbM-uzF7lowqe6iya8Ue-e9C7yyRdGSqlvOZ57vU11pRj2Otphoi6SgY5dpcFE9jaKt60MvhOPX5m3xbuBGQ360jCz-4ygOWCA-XTywjNTsG2UMSp3i7jzJp6bkJTZmH7hWf7ueT-8XK8xLIw1S6pKraS6NOQdBFKJs8hy3ETYBmLYYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقب‌های سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/akhbarefori/652333" target="_blank">📅 22:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652332">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b008f364.mp4?token=svIGOabiQoi453jZlv9EkzoOpISW5fP6yhcqSY04llarIw-DONYBowB0_F_POLJJJYkdpo7yHD2HtOKT1JmAV3BUNHdVW1b8Fo0n8_smzJx-_dCdiHhemqpI8ePAyj0sjCUxBVYCvb6vvolc7GbpI0mVVOGX7Ykv9id5nl9csdU6JAnPG4lkloh0kDJckirDynngb0aoLcexifTyy9DbYMyGjGEIERU4OTgx9uVsdqSbRgCdnD5ngsWZ_yEzgadKKPvMHLc4coweeVte1meBvxeAVI1Xa-wXd3pOVzh8hNR3d5bstPqbNHBhxKaJ220EngxE8dRSuGP-LFyubaC72oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b008f364.mp4?token=svIGOabiQoi453jZlv9EkzoOpISW5fP6yhcqSY04llarIw-DONYBowB0_F_POLJJJYkdpo7yHD2HtOKT1JmAV3BUNHdVW1b8Fo0n8_smzJx-_dCdiHhemqpI8ePAyj0sjCUxBVYCvb6vvolc7GbpI0mVVOGX7Ykv9id5nl9csdU6JAnPG4lkloh0kDJckirDynngb0aoLcexifTyy9DbYMyGjGEIERU4OTgx9uVsdqSbRgCdnD5ngsWZ_yEzgadKKPvMHLc4coweeVte1meBvxeAVI1Xa-wXd3pOVzh8hNR3d5bstPqbNHBhxKaJ220EngxE8dRSuGP-LFyubaC72oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهدید سخت کویت توسط عضو کمیسیون امنیت ملی مجلس
خضریان:
🔹
کویت فراموش نکند که تنها در ۹۰ دقیقه توسط صدام تسخیر شد و امروز هم حد و حدود خود را بداند که جمهوری اسلامی بسیار قدرتمند است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/652332" target="_blank">📅 22:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652331">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3f2d6c8e.mp4?token=QZoGnEWQBPyfnjqt61KlJMvb5PI7PkOCHmtwmQT2YFAdxNrl5urOkEx-lcHRMifiEK1k1Leh1ds2KunVTeaSW_fp5ivhuOTvTGDKn_Qwx1EdaLv06TgGkdFKc5zhDe6aoXP8QVy3zOeZ6Ae2XjW5glh-J0d9Kza7q1qviP19E3IM5VwB8SfLvQCKlLRpRYkKMhZOBFKBPAUXipElTb_s8Nxa9Xvqs1-XxCora1mJDc5jfgnJVF885Eg3M2QjTKYZh6W5oe-_cbZ5OxdYM5woZFLzgnTWa60k8M6HSQnk09rvCkWSHvNccGSABju6cbUXQFv7_8aicGDJqYe8-RyavjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3f2d6c8e.mp4?token=QZoGnEWQBPyfnjqt61KlJMvb5PI7PkOCHmtwmQT2YFAdxNrl5urOkEx-lcHRMifiEK1k1Leh1ds2KunVTeaSW_fp5ivhuOTvTGDKn_Qwx1EdaLv06TgGkdFKc5zhDe6aoXP8QVy3zOeZ6Ae2XjW5glh-J0d9Kza7q1qviP19E3IM5VwB8SfLvQCKlLRpRYkKMhZOBFKBPAUXipElTb_s8Nxa9Xvqs1-XxCora1mJDc5jfgnJVF885Eg3M2QjTKYZh6W5oe-_cbZ5OxdYM5woZFLzgnTWa60k8M6HSQnk09rvCkWSHvNccGSABju6cbUXQFv7_8aicGDJqYe8-RyavjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طبق صحبت برخی افراد نزدیک به مسئولین و مقامات، در صورت شروع جنگ مجدد نقشه اسرائیل چه خواهد بود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/akhbarefori/652331" target="_blank">📅 22:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652330">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKk4OjTdi-qSYj59YkXjRH1tmVo4QLf225Zz2SmZ5_qMNOx_23VlsCoErpPxJAWLPJwF4WMihliDhl6XhQDMt_bvdY3Hy8G7d-Tu0ibJntGOLA9zrovk7vugDj9u76_Dsj-cG8X-c7MbWByFv8cQCeqrrGxHpgx0cg3BHIQwU-c93JU-Yl7h7iD28Vf7sSeYcPmeajU3YfcZ-AAJBAYTpgRKbt7epOQs7ot2d4DXW-cUbLVacFCiBcCNS9Y0-iRtr77Qj5PjZJar54Exv92HLZg19Y_V9U5nOZbNz8KpcCWVrtQfqiSRWQFgWbIdjjJQqrxi0yMn0Y-u2YPjDQLsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر مدیرمسئول خبرفوری از رسانه‌شناسی قالیباف در میانه نبرد در میدان و دیپلماسی
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/652330" target="_blank">📅 21:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652329">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آمار ناراضیان از جنگ با ایران در آمریکا بالا رفت!
🔹
طبق نظرسنجی جدید مرکز تحقیقاتی پیو، سهم آمریکایی‌هایی که معتقدند برخورد نظامی با ایران «چندان خوب» یا «اصلاً خوب» پیش نمی‌رود، افزایش یافته است.
🔹
امروزه ۵۱ درصد می‌گویند اوضاع خوب پیش نمی‌رود، در حالی‌که این رقم یک ماه پیش ۴۵ درصد بود. تقریباً از هر ده نفر، تنها دو نفر (۲۲ درصد) معتقدند که اقدام نظامی «بسیار عالی» یا «خیلی خوب» در حال پیشرفت است.
@TV_Fori</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/akhbarefori/652329" target="_blank">📅 21:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652328">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8421f0494.mp4?token=Le6ISYTb3zKkxa5utaklst5t_usRVdkn4b8STtTDnERZs9HQVCYCSKVdQ5a0Lx_B6T0nHzcGst1TEftU0qOYLQWC_BIBy4Eoa7JeoVWwXbhA1LQ1xP8QlriEKoJG90VDOyzfKXhzjYVAI1y1GXEbYRHeCYfA55CYUWDvZHln-cphf2zIujo2Yzd4OkhcJ3izxN4jD9Ht0UIL-dgxQcWYEpjJ2KwTDSWEnkpUhfVwtH3H-7VRDObKLf7y5s0x3ujgmmx9PZkRJix0G2K8yQygxj89gYa8fj1hYF18R4_b9eVHwEpBu6aVlkCB5_0VAkqEKAzfzXn11MsIxLqQ9UmZdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8421f0494.mp4?token=Le6ISYTb3zKkxa5utaklst5t_usRVdkn4b8STtTDnERZs9HQVCYCSKVdQ5a0Lx_B6T0nHzcGst1TEftU0qOYLQWC_BIBy4Eoa7JeoVWwXbhA1LQ1xP8QlriEKoJG90VDOyzfKXhzjYVAI1y1GXEbYRHeCYfA55CYUWDvZHln-cphf2zIujo2Yzd4OkhcJ3izxN4jD9Ht0UIL-dgxQcWYEpjJ2KwTDSWEnkpUhfVwtH3H-7VRDObKLf7y5s0x3ujgmmx9PZkRJix0G2K8yQygxj89gYa8fj1hYF18R4_b9eVHwEpBu6aVlkCB5_0VAkqEKAzfzXn11MsIxLqQ9UmZdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت کارکنان بیمارستان میناب از مواجهه با انبوه دانش‌آموزان مجروح
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/akhbarefori/652328" target="_blank">📅 21:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652327">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQp_hy6GvezYXo_npN23uydFb2kiEVLOuoO5YfejbVByhAYM0wF3NnUAMrbBt0V21IVgnw0IUHleKQFsD9DUuK9YKQqNNf8IhYRj2EAQV2S4VKf23FUjBMRhWM7yDmA5vncBk7_aeg_rVw4LZMNpM__fOsNg9lOIKNmmZNza6aQ3EfjLme7OUc6tN9P8MrYFM5kkD2CmzaDaGl8xli1Sfwr06sVCF9WHYmEqcIDn2c6eHhfDhvD86iIU-y-GYEA64y6dV5F9DtBe48EwIoSVq70Fno9RSRAwFv1J3MB3EcWOnmq61C5Xa_3XfKKKt6FFXiGLnXcLCTdLVNqm5KndJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان سناتور آمریکایی به مشارکت اعراب در تجاوز نظامی علیه ایران
🔹
عضو کنگره آمریکا جونی ارنست روز پنجشنبه از همکاری گسترده کشورهای عربی با آمریکا در طول تجاوز نظامی علیه ایران قدردانی کرد.
🔹
ارنست در اظهاراتی در کنگره آمریکا گفت که کشورهای متعدد در منطقه به تجاوز نظامی علیه ایران کمک کرده‌اند.
🔹
وی در این باره اظهار داشت: «عملیات‌هایی که علیه ایران و متحدانش اجرا شده، بدون وجود شرکای فوق‌العاده در آن منطقه ممکن نبود.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/652327" target="_blank">📅 21:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhQZ-BmL5ZQhZBVrBjXXRC3L6icsvqz_nbcgwPjTeRorCk0l5JGCg5YwxY02T_8YgQGnuX9_qKwv49WUk54Ex4f44iqy97T78HmyHVpaS-g1Z7bvzkWoZ0RLwoJIJRojGq8lBY_ygZVznF3GrQkF9Rbnuzedttq_d93nc9cdRl6YDv9yuF4sY-T09gkj3gDSrVyVn2BftRopfbSb89Rq1JVoQWO4XpbemQiWNQB1tkfWhkXU-ImktLUEuqspGbu3wj-qn6EOx83PPEp0ZZBourvBQ6ONm-SzV4D_uL7Oa6HiIP8CCXTaP0qqfGa_I8sijjTIg-qFw1FuJOROzJ7kaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOCpnq5esvUoadXQ8Iw1wfslUH04p5wkfOIqXfW9itqA2KGdSYgCYELUgWW0F7coYTlLlO0SiiP8QHQRoT8JgWsOps9FP_pYQb3kbASLsUmHpfb5MhCnOAIpAsmrLFNSXs8EwoFbfMQUnIjJQ1t8e7vNK4iEqRQd4S4uDVixC30BTKCT_86iufijKXw9zulTdJE6FTPa-_qy2ZoN0wUKXogCq67T8GqhNWW7pVQ7nkT6Hxowz2vi3yNVzru7aeWv0DuXFsW9FYeuxL1Iia8CDrhzGN9rMXnOe0DnvKE0lAZpVwvuZjqhz_-q7Eji0KCKsYWtrFWlactP5E2e2bHDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJ9oXLp0NCcaMzWYpy3Ubd_fLz02iKv1XuHB77XBdrO8cC73NX2hhnK3E7uj5HOdiqJJVBBe8Zldgzc0GsGkH8ABL0-H5EMn6k_thhnvDYNexadSibsWX6e430h3r8juf7qOTb3Ql0rca7pTnFwjPG_64L44Si1cUV4ytDT1yhJBsmcdUVuiigUTsBKxPzzrb4CQd5NHiH8Nour_FIoJkXE5CxCoEuHlh3GIxD4mdiQF7txqbpbIrMUXCGjfPE1VM3nU-CuR8KIlnPLmm2oE9NH36C55sgH2thnIJ0PDJ-o9ux2j9qT56FOPrVJc8u6xPbfj9tdNRo14ZfnIXZ4sXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUN3HgZ2Lle7Q_RgSz0PTNRImfSv0kt8j0EZjGv2TUD9saDIkeZMGW8J7VqJ-ZNB8IyeWhTtoEkwMR6vlCgCI9oA8WJjg_SXlP2lCHTKUJ-MrednpD9kH-L38RQKJaQT5DxlzZcuSdFIk0gYw_TPRWuh7_jnIqGlJcYrqmx3WJ5kvTROJzwXM7zNAkwe8A5cl6qHJEqoFITk4dCbo9J_FlevfUgDebmcmop3cuEn5wjTO6AeC-zDtlsyPuL4sItpYljnlfm3HUVEs5tpo-bSBHNsF3h4fOGu_tJof8Ste3nVa8qOAOkKgKejhdyV4EgFzzyPznijKWTUpPFd0Gwjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAfAc9u6Jzh1CJrlcaAWtCM0ljaGPOu13js_7Z_Q8GVrf7kFBi63GvgKpIqhdWTY8nlOFP0F3ykd688ygSm9qu03mJWQPcaBUIw1UVx09rCxww0UCIc8akojcwxOMez2rX6_Cp0torX8gbjvaTK71ex9xSlVx8pb7W_7i45wsZpL00v0ksu8kuNEkbTH8u4Zai7ZvuoTUko_9Lo2TX4wtjFYHzeWzLZfzQc1Pa1ICO-3TuhIDQhR0jUtjPxSaINVgCtRgiHVAYdL5pvD9NP-G_lgoVoFvoPqVqaoJOi_dhtt86r41kT6bEK8ruXTCrLhEFzIAryENKtsw4bQNbd2FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AF0GR8H9tbo0xoEXQrmlu2yxcXcxcEKlVtryR71inLy9twHSVYRzIGxIwNo12VCYzlRBHYG0Ybv7oQqz_lBzSCi-EPqvEPi-vUsaHEn69h-XLpSEm1V7jehEsQzUPMFjVd8ujjJGdbFrRfIVswrqHePeQEDWoDqEisWxwAsBX7zd10q_AzNa0pqP6kAadoPpLjRmUc2DCtlC_Z9g-1ajH7zxFBDymbeXAGQ4KOVGVgm9QBHSMOot1bBHYfl_mPxibrleylXWU3BYnR4MSdja2PI2Mg3acGV30UVUaUw4xPASiHAhLcwyLvUscwiQhw3zq_BRby7yX0W3VyrsxpWSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfMcEA9QE7U-8HDaCUupShj6STymw-Z4cj-KMPd6y2NaUc-gpIimoN5YhAp0sN9tekQVn-vG0ATJ95XqABt17te0aJ33XfXKQURMmgth0_DlB_A34BRAfsdeo7LBleAJEs1YgyXnQBphmFw2ozMY3fwhSqLX7Ju0NKGxgDxqoPk1NUidhnZWFmWiJIr2c5V5tDoVvOuAi54jzhUt-hFuZwZuh2jP-pvWLx3N2o5jiNKM__MoHmThENoeaBs3dfSnQoee7UPO3nCkI95_o80YbQk_2g-r0LNp-8QkDIKzFo2D2ZgG0OXCurqgFQtGGCoD5ENxX26SLZtF6DXsWotY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jB-BCqzeW4vqDZeMHqSi9RSvS5dAWO06dpQwMIkpbTiCG7-ekyWsibAwKjdRPgog8BN2CZ2vOksGpAjkAaFsq40urf-HOQnJBIgozIQSURP-hT-MAn-lS4t5hljlEZechTdsDGID3SMl3SxWi67WQ0P-zTHaHkW8ncY1J1eAQ1MUK7otkluUNNFf22NX_glE4q8yTG9o8z-JS1Qt-QZcupKUd6hUwZYcs1V2Wqtk-4ZrDCkAgTu9yFaLwI6KP9PKV3VY_4rEUMxRUjJW6vw2a8mfEK5VjKgbmtdFlLLmgaD4ylmuxr-iDxpM_nzGZ3fMi40nP5aXjuksHh6TZ0IuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DowIZQQdRomJeC1Lt8mnP6kZMmHFAsBd5yyft2fBbtsqkolnU0rCh-yQpp1L5LVO6EkrCkLVzF2yJqxBf9sKgP6h7VKhUAWFJFibHFHFagxaRdsbPSM5PIJlQfJRk3Qfq9sflyHdw18qf-FbfdyayGr4jbgyaS0-nihPOm_FIdnyfdMiwxnEW5pqy3jR6Ku_S_EmIk9IFH4xhs9H3QJNU50V9z8ai8jf-htPgBMyoZCnlwNVs9_I6AiLhUu5H6YpkaFEhssGH5IWt2B2xPf-mJgkJfW8rJAnm1sfsEHmhLuRGUL7ncdA8N0oCjqkzBn7lN3EfJBmDER-D9PWZH6TQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازیگران موفق در دو تجربه همزمان
🔹
فیلم‌های شبکه نمایش خانگی این روزها بازیگرانی مشترک دارند. بازیگرانی که همزمان در دو فیلم ایفای نقش کرده اند.
🔹
در این اسلایدها بازی آنها را در دو فیلم ارزیابی کرده‌ایم.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/akhbarefori/652318" target="_blank">📅 21:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5004c897f.mp4?token=aASBQye5GuUaTfAtk_-MoT3uokvUlc4bYtqpByZGAJ2CeaECYIBPs2_PCy0WaEudivKMjoW5IRw-n0zYdxjRq5Kk65prAYNX3omJvdifILqprd9jZhVm9MTEy1S2eWdGOYaKY0dTAtBYzJgkiBQxvWv-waW7eprXGeLffcLaC65q8oPM5-PZ6Y8ANgw5ZFauDa9DhLu4vSEeUbL9FiWiqAbPbEtDl-RsgFFCPp7_C_Up_SUlFvyefjmxuj3hSTuZTz33X6EvEVJArZ_5I2cTMPu6QFSuZLiHWbxsfRDlipdKHaD0rjubRJtabGlW7-91qB2hF3su8xvNiu5xiLh7rUccrrdHuds_14VaeWt68U_i4IXCHZ7up6iN2Ksb-I1h28wCMYq5VqGppqYbAdl4OJKFNaf-kK3WJpk7EafugAlO8-PTAqoK9gw29vTBEv3rUqvknMGkawsIS8WdvuxCxvkVZz1TB06J3cZFGy07tmPr7Tzei54lQEo3tZHeG7lTaZDIKO093HiVexw4eLn5vcDgukfhJcxW3vqKo9s73lcFta26ohTK9OistYMHnM2Npax3kbRkuqe1mrFJtuqbW8jv35xb95ZiUcxBPHfL2lH8nhzCdsFQki-lVakniQyP293annS91hnHRKtB-NKMWSj0y0ERHzfghqqkbz1kb7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5004c897f.mp4?token=aASBQye5GuUaTfAtk_-MoT3uokvUlc4bYtqpByZGAJ2CeaECYIBPs2_PCy0WaEudivKMjoW5IRw-n0zYdxjRq5Kk65prAYNX3omJvdifILqprd9jZhVm9MTEy1S2eWdGOYaKY0dTAtBYzJgkiBQxvWv-waW7eprXGeLffcLaC65q8oPM5-PZ6Y8ANgw5ZFauDa9DhLu4vSEeUbL9FiWiqAbPbEtDl-RsgFFCPp7_C_Up_SUlFvyefjmxuj3hSTuZTz33X6EvEVJArZ_5I2cTMPu6QFSuZLiHWbxsfRDlipdKHaD0rjubRJtabGlW7-91qB2hF3su8xvNiu5xiLh7rUccrrdHuds_14VaeWt68U_i4IXCHZ7up6iN2Ksb-I1h28wCMYq5VqGppqYbAdl4OJKFNaf-kK3WJpk7EafugAlO8-PTAqoK9gw29vTBEv3rUqvknMGkawsIS8WdvuxCxvkVZz1TB06J3cZFGy07tmPr7Tzei54lQEo3tZHeG7lTaZDIKO093HiVexw4eLn5vcDgukfhJcxW3vqKo9s73lcFta26ohTK9OistYMHnM2Npax3kbRkuqe1mrFJtuqbW8jv35xb95ZiUcxBPHfL2lH8nhzCdsFQki-lVakniQyP293annS91hnHRKtB-NKMWSj0y0ERHzfghqqkbz1kb7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ چین به ترامپ: خرید نفت از ایران را ادامه می‌دهیم/ آمریکا می‌داند که اوضاع دیگر مثل قبل نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/akhbarefori/652317" target="_blank">📅 21:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3669d8d576.mp4?token=sJY54EWcWfT_EqapFYl1EgSAl5bGlEqdkaeEZx4eA3cEJktSHUF6-nMXhIA_lBEksi0cI1Hj3iKolcnBtsG53nX5BpRVU1zjyag5PvhEkY6lrSte-Suwl5LNy2pdbAXFwIzQk9V0AOPq7FpZ9HlqejxJiFB2dIPTNveAB4fhNXlJxVFJO-AYN6cpvOKEsvy4PQDX3zj3wPwPtv2WKM_Ls6uaWY_n-QZuoqdQ5SH5hStwuA8OndxfYBA8s16V3yjTD5ma341HZ69TlEuDiaphpFgOf6_VP_q30eIWJDP0h2GlsQfTa55TA5CqufL4H4eLHdhAKQbkHzWVl6MV51q_foi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3669d8d576.mp4?token=sJY54EWcWfT_EqapFYl1EgSAl5bGlEqdkaeEZx4eA3cEJktSHUF6-nMXhIA_lBEksi0cI1Hj3iKolcnBtsG53nX5BpRVU1zjyag5PvhEkY6lrSte-Suwl5LNy2pdbAXFwIzQk9V0AOPq7FpZ9HlqejxJiFB2dIPTNveAB4fhNXlJxVFJO-AYN6cpvOKEsvy4PQDX3zj3wPwPtv2WKM_Ls6uaWY_n-QZuoqdQ5SH5hStwuA8OndxfYBA8s16V3yjTD5ma341HZ69TlEuDiaphpFgOf6_VP_q30eIWJDP0h2GlsQfTa55TA5CqufL4H4eLHdhAKQbkHzWVl6MV51q_foi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناتوانی فرمانده سنتکام از پاسخ به چرایی بمباران مدارس و بیمارستان‌‌های ایران
🔹
گیلیبراند: ما داده‌ها و اطلاعاتی داریم که نشان می‌دهد که ۲۲ مدرسه و ده‌ها بیمارستان در ایران هدف قرار گرفته‌اند. شما قوانین حقوق بشری جنگ را رعایت کردید؟
🔹
فرمانده سنتکام: بله. جلوگیری از تلفات غیرنظامی یکی از دغدغه‌های شخصی و جدی من است.
🔹
گیلیبراند: پس چطور ما ۲۲ مدرسه را بمباران کردیم؟
🔹
فرمانده سنتکام: راهی وجود ندارد که ما بتوانیم آن را تأیید کنیم. نشانه‌ای وجود ندارد.
🔹
گیلیبراند: راهی برای تأیید ندارید یا هیچ نشانه‌ای وجود ندارد؟ کدام‌یک؟
🔹
فرمانده سنتکام: نشانه‌ای وجود ندارد.
🔹
گیلیبراند: خب، این نشانه‌ها همان مطالبی است که در منابع عمومی در دسترس است. آیا شما درباره این ادعاها تحقیق کرده‌اید؟
🔹
فرمانده سنتکام: خیر، تحقیق نکرده‌ایم.
🔹
گیلیبراند: چرا تحقیق نکرده‌اید؟ این با ادعایتان در مورد اینکه دغدغه‌تان جلوگیری از تلفات غیرنظامیان است، هم‌خوانی ندارد. من در این مورد یک گزارش می‌خواهم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/652316" target="_blank">📅 20:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
به دلار چقدر دستمزد می‌گیریم؟
🔹
حداقل دستمزد در ایران طی ۱۵ سال گذشته روی کاغذ رشد چشمگیری داشته است. این دستمزد از ۳۳۰ هزار تومان در سال ۱۳۹۰ به بیش از ۱۶ میلیون و ۶۰۰ هزار تومان در سال ۱۴۰۵ رسیده است.
🔹
اما وقتی حقوق‌ها با دلار سنجیده می‌شوند، تصویر کاملاً متفاوت است. حداقل دستمزد دلاری از حدود ۳۰۰ دلار در سال ۱۳۹۰ به تنها ۱۰۵ دلار در سال ۱۴۰۵ سقوط کرده؛ یعنی افتی بیش از ۶۵ درصد.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/akhbarefori/652315" target="_blank">📅 20:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5e2d40117.mp4?token=PIcIc0u7HMtRXNqybM1HzncVZ3k06QBz5X5tMxCAmvmqKHQ78eHW9J1kE7C8hcKDcvZz9u6yDRva4INHuuQgejOawomzbmius2vuSfmElCxhmf-LiwSIf3TOzHdoj3B3EjZF-DHEH7U01u8ixdMXbhzcPbaumPaw5B3xNrZfqzV_hnGKeiTHfcmf-nIazJEGB4Gn6u_xLSWTvN4rPnkvOk485gVztcwPe7HzPrff71BSSEyzj1pBF_EqVO-JtXraFchXRD5pPbMiPTbpmq6Fk9dtz4nZZmOamXX7CCQR2yv_S54xU4OH89G84q7swxtJondudeaBnpVpHJtRbIWrZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5e2d40117.mp4?token=PIcIc0u7HMtRXNqybM1HzncVZ3k06QBz5X5tMxCAmvmqKHQ78eHW9J1kE7C8hcKDcvZz9u6yDRva4INHuuQgejOawomzbmius2vuSfmElCxhmf-LiwSIf3TOzHdoj3B3EjZF-DHEH7U01u8ixdMXbhzcPbaumPaw5B3xNrZfqzV_hnGKeiTHfcmf-nIazJEGB4Gn6u_xLSWTvN4rPnkvOk485gVztcwPe7HzPrff71BSSEyzj1pBF_EqVO-JtXraFchXRD5pPbMiPTbpmq6Fk9dtz4nZZmOamXX7CCQR2yv_S54xU4OH89G84q7swxtJondudeaBnpVpHJtRbIWrZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی باقری: سازمان شانگهای تروریستی نامیدن سپاه را غیرقابل قبول دانست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/akhbarefori/652314" target="_blank">📅 20:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65f2ab3c19.mp4?token=Z9P0BgzGd-DhlTfTzdJefBZFIfTsJqbMTZ0yWpgz9ULRFiVLoOHMLu68VJrlSLt8uWLKY03OGmhnkdkHW_vq1SjEaE_hDmTjdd8NpEtQPIXHvnJ47koc9CJNDjerB6eWiezuYOeXi_F6W_dHqGbgzUh9ACaEaLvh1ynHEqqIqcteYF7AtWVcuTNgDedPjh7regqzm2ebti3m4Ym9DjP-v8GLojfxRYCKRpfCimuoEEwq013OGZguSnxnNi5tb5ch-6W_U8Ct49KV_6-y47HX0ojcmnEbawkFKLbaGl9Gnr-3KGKE5y3ZBmHS7hmjDqduUAA6ZCw8TxTgjCvkCjmEFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65f2ab3c19.mp4?token=Z9P0BgzGd-DhlTfTzdJefBZFIfTsJqbMTZ0yWpgz9ULRFiVLoOHMLu68VJrlSLt8uWLKY03OGmhnkdkHW_vq1SjEaE_hDmTjdd8NpEtQPIXHvnJ47koc9CJNDjerB6eWiezuYOeXi_F6W_dHqGbgzUh9ACaEaLvh1ynHEqqIqcteYF7AtWVcuTNgDedPjh7regqzm2ebti3m4Ym9DjP-v8GLojfxRYCKRpfCimuoEEwq013OGZguSnxnNi5tb5ch-6W_U8Ct49KV_6-y47HX0ojcmnEbawkFKLbaGl9Gnr-3KGKE5y3ZBmHS7hmjDqduUAA6ZCw8TxTgjCvkCjmEFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض سناتور آمریکایی به هزینه‌تراشی ترامپ برای مردم آمریکا: هنوز هم روزانه یک میلیارد دلار صرف جنگ با ایران می‌شود
🔹
سناتور گیلیبراند: قرار است چند روز، هفته، ماه یا سال دیگر با ایران در جنگ باشیم؟
🔹
فرمانده سنتکام: ما در وضعیت آتش‌بس هستیم و مسیر پیش‌رو توسط سیاست‌گذاران تعیین خواهد شد.
🔹
سناتور گیلیبراند: در حال حاضر، ما همچنان روزانه یک میلیارد دلار هزینه صرف جنگ با ایران می‌کنیم. مردم از این موضوع خشمگین هستند.
🔹
این رقم می‌تواند صرف کاهش هزینه‌های مسکن، کاهش هزینه‌های غذا، کاهش هزینه‌های درمانی و پایین آوردن مخارج روزمره‌ای شود که به‌دلیل جنگ در ایران مدام درحال افزایش است.
🔹
معنی قیمت بالای بنزین و گازوئیل این است که هر چیزی که آمریکایی‌ها باید برای خانواده‌هایشان بخرند گران‌تر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/akhbarefori/652313" target="_blank">📅 20:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl1YOZ01IsIgZzImUgwfpP9LmGZQUWTbpqaFzhuQOKZ_EWY54glvjwKyDZS9Y39x9Prdeg6CVKnMXOpk0n3L2vrHXO1ApbWcSC66ANBC2LlDtR3arKSc2tLrUKykcxkIgCoCPZ09Cm4p8QnM0Zu-YBdYEArohlwt2HMa2N5YBD4ci_aIMYis97XfkYX87Glf2S_jpcqBFd4XIXI_W8TlkKV4Xi0lejC7sGiDnR2FLYUlh5ruCdsKMdvP_-rki2Y1T5r9kFcfRWdx2w7omUCCp91g6SlSbQh9BwDF-C7RsmryW7ZaAxAo37Q8TWPVNyHfk2pRxeSb83crnDBuI86IpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منوی شام چینی | دیپلماسی خوشمزه | شی جینگ پینگ چه غذایی به ترامپ داد؟
🔹
در ضیافت رسمی که روز پنجشنبه در پکن برگزار شد، رؤسای‌جمهور آمریکا و چین، پشت یک میز نشستند؛ مراسمی که فراتر از یک شام تشریفاتی، نشانه‌ای از تلاش دو کشور برای بازتنظیم روابط سیاسی و اقتصادی خود تلقی شد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214964</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/652312" target="_blank">📅 20:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b68453adda.mp4?token=Kl6lGdOmJ9zs48ulHGV2Y_2D1FnAQ3r_T4BnFyNu6spQwVVjmu-9xsxV7KkjfZrS5acyxpeocmxnQ13zKhlwi00cJ3FOEJ9MoClOcLL9BvHle0UkYEivnkk9yPvZTVnS7oW38IBVTPQ32ARvN7QxP_27VQRcabs1MEw6q1OcZZotd5QoHMfuWb1iFPAseBjWwKfrfUH85mLI_41S54Xui0LxABdfV8K2t2Q8aHfwV2FBdOo3inORyO5AUOCPmWhCPCHLbDi2axHEyqzx37FVQZ2fWGEDwmLt8BNwXpou5aAJ7CdA6Xnedagc8Yd_FpYu57Rykkm8apDfNwoL6GjSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b68453adda.mp4?token=Kl6lGdOmJ9zs48ulHGV2Y_2D1FnAQ3r_T4BnFyNu6spQwVVjmu-9xsxV7KkjfZrS5acyxpeocmxnQ13zKhlwi00cJ3FOEJ9MoClOcLL9BvHle0UkYEivnkk9yPvZTVnS7oW38IBVTPQ32ARvN7QxP_27VQRcabs1MEw6q1OcZZotd5QoHMfuWb1iFPAseBjWwKfrfUH85mLI_41S54Xui0LxABdfV8K2t2Q8aHfwV2FBdOo3inORyO5AUOCPmWhCPCHLbDi2axHEyqzx37FVQZ2fWGEDwmLt8BNwXpou5aAJ7CdA6Xnedagc8Yd_FpYu57Rykkm8apDfNwoL6GjSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف مهم فرمانده سنتکام به مشارکت حکام عربی در جنگ علیه ایران: ۶ کشور عربی در جنگ با ایران کنار ما هستند
🔹
۵ کشور خاص هستند که به معنای واقعی کلمه در کنار آمریکا درحال دفاع هستند: امارات، بحرین، کویت، قطر و عربستان.
🔹
هر آنچه انجام دادیم بدون اردن و همکاری نزدیک با اسرائیل غیرممکن بود. آن‌ها فقط مأموریت اجرا نکردند، بلکه در کنار آمریکایی‌ها خدمت کردند و از آمریکایی‌ها محافظت کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/akhbarefori/652311" target="_blank">📅 20:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7VEjvOae7_zDCxWNLWJtbFrV8F05242lHq1cDDqGMLojvtlV-pDKKZKU_j43mWHtVkJD6eP1IIsidBR4BjBt4tVwRA58ksPpuEGRk87HSzL_gBOWH0WfKI1qWIfdhQyzLIdjDQNydA5afo_sKU8jvZlc-bo52EwPUqtn788ThuqHEAe437AwVOBCWE-z8nETsWC50lU_z5sJjea4E5guI6Gf2PqzZMiaLiyYRDcGjXj5-tytypPXzCqg6XwUGCsbr5kV-f_XDGYoZ43AQo93k8kqULmHKaeWf2Ij0O4pYgP-kiDaSxfueMGmQtq9WvhCZb14d9burOvBUtmkzirVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرایش جنگی اقتصاد
🔹
اقتصاد ایران در سخت‌ترین روزهای خود پس از جنگ به سر می‌برد. عبور از این شرایط دشوار، تنها با همکاری هوشمندانه مردم و مسئولان ممکن است. وظیفه مسئولان در این میان شفاف‌سازی کامل منابع و ذخایر، توزیع عادلانه کالاهای اساسی، حمایت واقعی از تولید داخلی، کنترل پایه پولی برای مهار تورم، و ارائه گزارش دوره‌ای عملکرد به مردم است. مردم نیز باید مصرف بهینه را در اولویت قرار دهند، اسراف را کنار بگذارند، از کالای ایرانی حمایت کنند، از احتکار و هجوم به فروشگاه‌ها بپرهیزند، مالیات خود را به‌موقع بپردازند و با نقد سازنده، نه دامن زدن به ناامیدی، در مسیر اصلاح گام بردارند.
🔹
هفتصدوچهل‌ونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori
,</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/akhbarefori/652310" target="_blank">📅 20:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652309">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScFNi-SS7I83gjLEUoXeyb46ov0UefG2-KC4FS0UUuypOfIN7a1Cbb_Z0Q1rA2kYESAHSroUXKHXsGQ7qQjYxpEbAo-6TxxwKkosShF4EZJznYYeu6NzJQWRz6shOoqvO_uwHW_kVg4AbDmAtD7q-kC-eJ2uVQoI1-Eybar0ipIFxQ5V3Fw1qU2ZTPTJqnip_qLMFzRGANRPcS4JyW3F9aBwKWjY6qbOv1XZa9jsNdweI8MhcQtNU_fDLadHyNNc3nL2crhWEjasAJl1FXkDW6VzTYLr_CNlIdze5amU7-ewRrGV9cZ50ynmnApD8dA45XePdDWtsoG09D9O9Gidcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین، انتخاب تو را به یاد می‌سپارد
🔹
هر بار که کیسه پارچه‌ای را انتخاب می‌کنیم، یک قدم به زمین سالم‌تر نزدیک می‌شویم  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/akhbarefori/652309" target="_blank">📅 20:15 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
