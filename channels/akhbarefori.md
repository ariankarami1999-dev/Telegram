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
<img src="https://cdn4.telesco.pe/file/PSwJLHpxesUkD5ih6mphrrBGB6aQkIzBiSYi8-xxfG0aSiwRDubvV7WnnLyzM6HpOudFGNYwIvNgsCTQ1vU4qBYBqz4DU6picqbjMRVFy15dYXR0hI1sfMCagDmQj1LiTlgVBvpfLbaJtc4TnR6JoyDoAmhtpI2FsmRBQhQ3yi-RjQzb4bH3JgUrUKvLQRV2Bky9E_0ZfrL2V259TukEu6wvRTBiqEYtTWLHD-M5-dc0Z9Hvjr5X4LGKT0pStvxPJ1OIMV_skH56flQiFJi5YSLg3giMgGCzyRVNCFWkG6io7U07YvV1USGb8GF3wao3X6kpg63b-oAb163aqCUoog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.06M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 03:25:38</div>
<hr>

<div class="tg-post" id="msg-678546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXQqEavAPlsKMe9tyiJL6zB0KknWT1nmuaPCNQcfnoDJgQCM0YYbx2OMKiGzN2bv_dlMXbzYzoNsTAB8QwlS2miQlM_3Me1Gw9SLnGlkwDIW1DRD-P07sQiLrQavZ5CKhScs8PH1xjIgP5gZSwM_44UEsk0WAIb8vnhEPFtxW0BEU-kOyksTK8BecHJ9gfzQ_C_FLXN9yHYE7pLSAjIEvT9GGvfKBUPGIyC0ECuwnEfPmB1ZC8_8CrAYP__SICcDEgJt5-gHTYXNCYm0hg-QKTCujkL6l-32J4SXtXCjgJe-fTdAxdQ4SrRL68W4kzuF0rLmpYaUHi5u4-x9biBGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخاستن ستون‌های عظیم دود از بندر جبل‌علی دبی
🔹
رسانه‌های اماراتی با اشاره به شنیده‌شدن صدای حداقل ۷ انفجار در مدت ۲۰ دقیقه، ادعا کردند این حادثه شاید به‌دلیل مشکلات فنی باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/akhbarefori/678546" target="_blank">📅 03:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emlOla60jvJIpylfVIzgpLE6aILAR2Xn7WpMYAGGl3sDlPewWedZSzZfVnJYNQMfQ0UppGKeRDMso7nOe2D8n5F0eeFFgppSmmF8L6Br6KEWWYWOyF8u_I0w8pPX3kGkIfHe6MgYx1cWQDikMmkv7N5s7M581gsVN94U8cpGG2uwvU3Zw_HXuWSD0D9KEJZCfgzqEhyiIB8GgzUfMAzvYXva17V6AYW_bFP8FMOQ_U5tz_tb_tvFSJy4V-r9qtyV_LTVvJjK5hJaxjNNFlyo1b2fRt43EIvOvdMgCAEj4EwCERTqQ-pfdDMD-vtRD81vBFZKTiqPqhHMhoK-uPNJUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8Mk9xj0ELRb5aKk6h9JVeqYK0O5Xs-MhC8mRLwzGBaYBiZ_gd9jYNTmig0H9GQQ8ugDkwzTIcceiN8DwTUQ0xc0htaQdLtqL6A70ldmdoZEdYc6mCwwbOcblv25Z7SEPr8mIsSnBBn88E9DXrgQqZYbnhsprdEqjoaaqKiJX5bHVO6Ti3GsIOMwV3Zu_g4fpKiuhFHnRtQxoRRM-sFUnw31EMvFLQsR5S7to_4PFgDw3MDgasSunlor39DPuAhQcSvo0KstGPuZ2AgK3Ga6y6oip0d-bRl8zgSS4-XCZsXFtlaDYrUClbZlaa7LntnVgSYRQjSa55KhOKdRENyoNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع خبری از حملۀ عربستان و وقوع چندین انفجار در صنعا، پایتخت یمن گزارش می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/akhbarefori/678544" target="_blank">📅 03:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
چند صدای انفجار در منطقه صنعتی دبی پایتخت امارات شنیده شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/akhbarefori/678543" target="_blank">📅 03:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
منابع خبری از حملۀ عربستان و وقوع چندین انفجار در صنعا، پایتخت یمن گزارش می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/678542" target="_blank">📅 02:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678541">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه نیک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5Rgv0tnED-tZvR_IzNzLcOjwqaY2nYkzXdD7q2CBczrWrd1PiLn2-fe_JvNbe-RJVXYUQC0Uo-wMiheMkyo1R5aEz__MJLSylRJx7urcjEO7YhSjRmA7rZtEraK8WIfC0tPcfyf8QvTsU9aB0YGdPlVGldQcdZ0Et7F8Xxcgf10DEna5GqzbgKwgeINEhIQJUHqPNL4YskAQwsIPkF9qy01iZ6AKTzoDT8vE2UMM9hB4U6mClLP5zDpGnSeS_K2eWBalieKfGOfpax-cmh7IZx6G3H5z8ba1T4Wva6C1IgjHEis3KAEqgmt6djryYFW8Fg0CzKDYKCISxMAzR6szw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فقط ۲ سال دارد اما روزهای کودکی‌اش میان آزمایش، دارو و درمان می‌گذرد
😭
💔
او پس از پیوند مغز استخوان، برای ادامه مسیر درمان به  داروهای حیاتی نیاز دارد؛ اما خانواده‌اش با درآمد اندک کارگری، توان پرداخت هزینه‌های درمان، اقامت در تهران و معیشت را ندارند
🥺
بیایید دست‌های مهربانمان را از ارغوان دریغ نکنیم؛ شاید کمک امروز ما، سلامتی را به ارغوان بازگرداند
😭
🙏🏼
🌹
شماره کارت/شبا خیریه نیک:برای کپی کلیک کنید
6037691990491185
6280237094218423
IR
110190000000216777746001
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام نیک
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@Pr_nikcharity
⚠️
مازاد کمک‌ها صرف امورات مؤسسه و یاری به سایر کودکان محروم خواهد شد.
💚
آدرس کانال ما :
👇🏻
👇🏻
https://t.me/+YQ8wu_Q7QahjNmNk
https://t.me/+YQ8wu_Q7QahjNmNk</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/678541" target="_blank">📅 02:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678538">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6Z7fT1DNxbBz4fqGMCzVDMe2GqJKeHCdJ9VSJROMo-KMvWv9wyQ2_YSFPU5WTgzr0S93CSvS9Pfz05gPCLeIlex9_-uVvR7Xz3VmzcKzoEdAlXXps8hr3_Tbj_MDUA-y2M_9-FhUaHI7DmGBqyPi149nmzBNdhZ13atL65LcA_q1PxlS4eqq7MPoO1pQrO6dkmDpihX3LPOBxzNIlAcHz4JDCPbZkSC_ebtPiCHppoiqqNjSKJpgBYAaL7WIuO4rTywcc1D8AnGwnAaI_qmvkOIfFDzokRDAIN5ym-UKVXMgKAr-uJa6cLthf58wp1ka7KgR46DGir0Rh2R9myASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObiJfyQ2cq1n7Or3Vi-KUGWoNwaDLJuzhJuGsyMhFtsYriZV51yU_Gelp0mCQgi5hp6HtbM8wFQVSJAmAVL7BgZVbKFrFf3xxGEG2CnTYWRLv5AQHdm2pm_hWAMnFWhXFAS9tG6Zyzklmn5wz1jDlQvh_0f4IccKQGPyoW9uNrPo3wTHCH2Qy-vkh4XDhlZRQPJF7vHiXYkbHD_dy7evbhCo6G9BbmirtxlcvPI_jYbLxWx7sq2AwbEcsk7MC6uy2x-wcEFEGcso10HfhVjtYZQcW_kSAip59VpOjYPBeLy05ovCd3z3qfQR9qFmQGps356jTdeq7eVhUxUKETxAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxXaHBRyQL3_YtmlnhOyXcvauiCBOtuiyhCtKmbnDQ_A3CkWI7Z5n3nJR4NAs2P_TOTxprowNB6EwVCDLM-FRSLZEWK0MaGPhUdbvgnyPSGg7NiYRGZ-8sTV_JKk8_PnzUIZwTIVNc8fQFOidZzkE3sPeDmegW15LIzup4Q1Wncbqn-oIXOC0ZzfWI1kgV76-Md2Xl-e74_K6tkIx8SsejH0L6q3_WzNNg9liT6hLazSp96ZLdE48iKsVQOwL2dIHfcVJ0QlgWC5ypFqvqHRaO1jBWbNejKO0Nnr_Xoi1gO1-ugN1BaZUoHWtAgpoghWEAH69AUx4MSF7PQOAfWV_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مشاهده‌ موشک‌ در آسمان اوکراین منابع خبری از وقوع چندین انفجار شدید در کی‌یف، پایتخت اوکراین گزارش می‌دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/678538" target="_blank">📅 01:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678537">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2830b3ff2b.mp4?token=EZtGec0vEM5yYe8rJIMMaU3wqOwm_FSp8C_KMFh8seDBrVvoAvK0X_5sflg3MwtmjXjWq600psnQP28AfzfLx815Xc4IUs3RDGiErCr2KRRKQom9fPAS0IBQyDDpzCy3HIYRGVdedLzFCEsSOi5DFxUu5Tr4fPqzQTZggdkmLbnVAsE09BfwCzLv5S_QqfghxW05wzGM0nBh3_FbF65nF22QugzO1VZTRaFkln_MMTvAYqbiKcwRgWEZsMI-Tdij-C0CkX6fparoVOuJt2zCe9aNiPv04ffxoiogp-ak51gxJr0rrIyUQ08_-6qRL8168ZxGBA0h_jhu1opIl9S5Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2830b3ff2b.mp4?token=EZtGec0vEM5yYe8rJIMMaU3wqOwm_FSp8C_KMFh8seDBrVvoAvK0X_5sflg3MwtmjXjWq600psnQP28AfzfLx815Xc4IUs3RDGiErCr2KRRKQom9fPAS0IBQyDDpzCy3HIYRGVdedLzFCEsSOi5DFxUu5Tr4fPqzQTZggdkmLbnVAsE09BfwCzLv5S_QqfghxW05wzGM0nBh3_FbF65nF22QugzO1VZTRaFkln_MMTvAYqbiKcwRgWEZsMI-Tdij-C0CkX6fparoVOuJt2zCe9aNiPv04ffxoiogp-ak51gxJr0rrIyUQ08_-6qRL8168ZxGBA0h_jhu1opIl9S5Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده‌ موشک‌ در آسمان اوکراین
منابع خبری از وقوع چندین انفجار شدید در کی‌یف، پایتخت اوکراین گزارش می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/678537" target="_blank">📅 01:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678536">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
المیادین: بیش از ۱۴ عملیات زمینی اطلاعاتی توسط ایران در اقلیم کردستان عراق علیه گروه‌های جدایی‌طلب انجام شده است
📲
‎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/678536" target="_blank">📅 01:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hn_-iUjhTfVHI81PPPai0AICDM10kRSYOhBJlvfj7qNEsgRReDmOXbrcMt2Mhqy9JCCXkhl4MKb6lRQdc82d84DgUtpEqonIcDKKFCCLCIiFteaG7uW60dc8hxe8pyx08X_p9oVxeULmWa0M_WVJ5Ewxdq7mnJNFDfNh-EzqqvVY_QQ1j3woyp5TbfQDYx_NL2-slzhJQQn5D_MtXvoonGKK7RW3nz45m224mSSTe9vmJ8x74CLZIxjPwMCFWeZZPtRWFdpgUmYQqjOQjPR74Me4WIW3o8PH3hnrDZJ3bu8RFAJ9-kKQAZ5rqXdqp-Lx_LYate37QL5AD82JEYzDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDLKM5NV3yLfYMRx3PpcZpfFOTcW1IJ_y-LHgn4rTlVpmGVu3cAmx4d6YxzL0qMTBhNq70R3qHN2fE304lKCQtSI0dZVgvkIbKAGH7On1FzzXVQsvXXjpXHgYdWnEi5Cfgi7SBPzGayR974hj6vq0cuvWqMjStepWd9_voor04AR5ClnOtEMTKjd71cbz_qMWZEBg_X-VB2lTjNzKdLneWDDO6kQE6L5slAZ0fVUeO7CsxFzsixIBF1nXBT2o-0MnanpwBGm5SaJWqR0zQUG4AqVk4N8ef1Sbld88m7tT7MfG-P1m76BCX7xdjYlOgSNk4cIRf0pA50Oi8KCZZjX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Whbf4vEG3IG5riYG_y8VyJUftJg6MHUbF56o64V-3dOgkQjkyptMivWNdPHUK7yZW0sDtg7nqrCCHm2a8H51Lico2DvYyHDnmzI19tRxtvdmHfrB3I4UEb0I09w7cO_lEz4ePPCSHtMHdAU_ar-ttorIl4NhEVEKMd_a5wMMWgvK3w8v54pxJnEPaluf5kX3zQjyEsd3Zj3iMleelQrauphGCrvA7Xxw6vK3S-42ywCZMZ9k-xRynOMOx4pSYtiUxTXl99LhWmqqeJGU0YAyz7_QAgn0fh96jezvAk6qn2BIPDdnV8ozXdZ8r6W1Mn5jqcQu5L4bDcztu_gXIXz_Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اسباب‌بازی‌های من
پست جدید رونالدو در اینستاگرام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/678533" target="_blank">📅 00:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای روزنامه انگلیسی درباره طرح ایران برای تنگه هرمز   روزنامه تلگراف:
🔹
ایران طرحی برای بازگشایی تنگه هرمز ارائه داده که به‌جای عوارض اجباری، صندوق داوطلبانه با بودجه کشورهای حاشیه خلیج فارس و اروپا ایجاد می‌شود تا هزینه‌های دریایی را پوشش دهد؛ الگویی مشابه…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/678532" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/decb6d0f68.mp4?token=qSB5AtUHD91sk6ot9y8N_kOJptW-RLOpZG5nDimg4gPs-vMKMblx-IyCznlRjunrHRblYAFqK0OjoMs8yZebu7Ch1kpjt5FO_d7pLq0ZPrIJ7Ba8nxhApqX3jJwhtghuDyR4VtScPIcXkWEm6A2YoigbvUksKCXWsRRRf-tI5sP_5Ts6eo1rPxr70sR4F2uI1LnNl5yaR1vYCIdjYbZhsZ4F-2RQGMkUMrpCyQM0D1H59sx5aSAuT7l5wd-ZaZwqTzlfD7QcZYVKuXkpJ8PDjG3Ncq2j-VoTIQqrYkFo0P8Rg2Z1zBi6z1vv19rLqiaFZ9yMuOPhOslIJXmIPWTPmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/decb6d0f68.mp4?token=qSB5AtUHD91sk6ot9y8N_kOJptW-RLOpZG5nDimg4gPs-vMKMblx-IyCznlRjunrHRblYAFqK0OjoMs8yZebu7Ch1kpjt5FO_d7pLq0ZPrIJ7Ba8nxhApqX3jJwhtghuDyR4VtScPIcXkWEm6A2YoigbvUksKCXWsRRRf-tI5sP_5Ts6eo1rPxr70sR4F2uI1LnNl5yaR1vYCIdjYbZhsZ4F-2RQGMkUMrpCyQM0D1H59sx5aSAuT7l5wd-ZaZwqTzlfD7QcZYVKuXkpJ8PDjG3Ncq2j-VoTIQqrYkFo0P8Rg2Z1zBi6z1vv19rLqiaFZ9yMuOPhOslIJXmIPWTPmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای پرچم من
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/678531" target="_blank">📅 00:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
سنتکام دوباره برای فریب کشتی‌ها در تنگه هرمز اطلاعیه داد
🔹
در سه ماه گذشته، علیرغم حملات ایران، به بیش از هزار کشتی برای عبور از تنگه هرمز کمک کرده‌ایم.
📲
‎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/678530" target="_blank">📅 00:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سی‌ان‌ان: ارتش ایالات متحده تقریباً ۸۰ درصد از موشک‌های رهگیر تاد و تقریباً ۵۰ درصد از موشک‌های سامانه پاتریوت را استفاده کرده است
🔹
کشورهای حاشیه خلیج فارس نسبت به کمبود سیستم های دفاع هوایی ابراز نگرانی می کنند که بر توانایی آنها برای دفاع در برابر پاسخ های ایران تأثیر می گذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/678529" target="_blank">📅 00:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ترامپ متوهم: بازار سهام به بالاترین رکورد خود رسیده است زیرا سرمایه‌گذاران متوجه شده‌اند که آمریکا در حال برنده شدن است
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/678528" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678526">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNA_nd4Xsm5zrUwUuTdiDK910_NnD9Xh1pdezI0_lCwd1iRfQyZA-ZgFJhvdeArnlijVfNP1fcFcjIy96LZfGkDBO6x3hYCskuF2f107s_PxufI2bTStWdYVtDeNHp7jFGbaB-MzpsSZjDisxUqo7DrPUIFOUu4v-KZ6SBnoHLY3c9LFbdkkXaOI2UvLzCTDEzCF-q3LAWlEhgXC0MleHwzI4YIC2KDBG23C7xShEm5OHYWb7EtchhtLQMwkekgiJ5x6Y5zHBsFIBGMEF19cuzTiCpqUEdFtLdEMTtKbaD5TZVo3UqkOkwfXtSPOSFc0B6y8ny77W9sdcSZw3gatww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رادار اصلی فرودگاه نجران عربستان در حمله تلافی جویانه امروز انصارالله یمن منهدم شد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/678526" target="_blank">📅 00:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678525">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
قائم مقام سازمان تبلیغات: تجمعات مردمی تا پایان ماه صفر برقرار است
🔹
در خصوص بعد از ماه صفر هم جلساتی در حال برگزاری است که تصمیم گیری می‌شود و در نتیجه با دستور رهبر انقلاب اعلام ابلاغ خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/678525" target="_blank">📅 00:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678524">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای روزنامه انگلیسی درباره طرح ایران برای تنگه هرمز
روزنامه تلگراف:
🔹
ایران طرحی برای بازگشایی تنگه هرمز ارائه داده که به‌جای عوارض اجباری، صندوق داوطلبانه با بودجه کشورهای حاشیه خلیج فارس و اروپا ایجاد می‌شود تا هزینه‌های دریایی را پوشش دهد؛ الگویی مشابه تنگه مالاکا که عمان هم از آن حمایت می‌کند.
جزئیات بیشتر
👇
👇
👇
khabarfoori.com/fa/tiny/news-3235497</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/678524" target="_blank">📅 00:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678523">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه نیک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ8rgODzJG214-7MLcvAFTtdoSZ7_VEuzPNYmqspu8vY5YyVy_j8reTrfO4LV2y5QKR40WucDOjAX7D2bblLcB02-qE6hZMnCvujjBqSrHerlDr2EAp4g8TlX1SjWVH6KCINXi0yQUKopZJeSL3f8aCJWlaMnXatGptXsAgr923gPkYk5aiLtiPBkrbVFIZGeZMStZlNsEJ6fQfCrp1diQBES9qRi93affOgiYpVfmdeRUaaCD6H3ND3feYj0k-HKobaRAGrWDCLvs70FHcT0uryZr6kvWbJVae2jm5rN1vKD3Wmqh5nDHPHtazzaQZ2nXq31d7_2A3Ob99S77ElyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فقط ۲ سال دارد اما روزهای کودکی‌اش میان آزمایش، دارو و درمان می‌گذرد
😭
💔
او پس از پیوند مغز استخوان، برای ادامه مسیر درمان به  داروهای حیاتی نیاز دارد؛ اما خانواده‌اش با درآمد اندک کارگری، توان پرداخت هزینه‌های درمان، اقامت در تهران و معیشت را ندارند
🥺
بیایید دست‌های مهربانمان را از ارغوان دریغ نکنیم؛ شاید کمک امروز ما، سلامتی را به ارغوان بازگرداند
😭
🙏🏼
🌹
شماره کارت/شبا خیریه نیک:برای کپی کلیک کنید
6037691990491185
6280237094218423
IR
110190000000216777746001
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام نیک
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@Pr_nikcharity
⚠️
مازاد کمک‌ها صرف امورات مؤسسه و یاری به سایر کودکان محروم خواهد شد.
💚
آدرس کانال ما :
👇🏻
👇🏻
https://t.me/+YQ8wu_Q7QahjNmNk
https://t.me/+YQ8wu_Q7QahjNmNk</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/678523" target="_blank">📅 00:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678522">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkUuLcfmUuwAuABtHkc4yt2wpimio8FvgBQkduXX4FAyPBGBtB9UBZcfYkEjgtdXpknZT_JoUuyDXI6mMTthsCYx1CSo50YXjS7tsn7cV0acwqYORHCmJ27g9uG3QiRR45OSY3crJERsvbqGYjbcAGpRfQHChJvQ9-muBnXwDL5BlTL8LnakRTVqxDl1TppnDKa6tUK95WTMiC6VbFYJvirBHhCn4JWwz_3o8cbp_aquoeFgUNnM3skO6CaL9Z6T5j-Dgric_qy_xdyR6TubMy2ShpGMekawJwwMMqizGdu6lT2s0KDOQpTMQvuFogvOhKdNaVTDWixiDkcceQcIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/678522" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678521">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
المیادین: ارتش رژیم صهیونیستی اقدام به یک انفجار شدید در شهرک حداثا در بخش بنت جبیل استان نبطیه در جنوب لبنان کرده است.
/ایرنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/678521" target="_blank">📅 23:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678520">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab59d1739.mp4?token=B_Y27YUlKWHmkBc7jkNuufzC0WvknDl3jpwSUM9tHYMQEjFaM3NWxhOFLBz53dJ01jpFdDHse3P8ihmQXcykwPUheudDLXr75XQIgzq68-cV0nyidt518mJqG8hK0vU1LfiLvUEzxu_RKoDmWeW9vnf5ZuUMRb0t6_Z6NxrOFcOxcK-Nrik_KJyRV5nLuCrPB5RLGOGtHh0AF0-FNLExW1vO09eBcZEA5BVB8DbF2X3u-6ycuyOVBHJkMa7EWEhh9WCjLCmEeN3nwSNCrAWp3ccUiLsIgO1gadvY-w3YFTp6gZnmtnNwALL5RrC6QKRE7DmHWzUPxqWmdXKO42Mmpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab59d1739.mp4?token=B_Y27YUlKWHmkBc7jkNuufzC0WvknDl3jpwSUM9tHYMQEjFaM3NWxhOFLBz53dJ01jpFdDHse3P8ihmQXcykwPUheudDLXr75XQIgzq68-cV0nyidt518mJqG8hK0vU1LfiLvUEzxu_RKoDmWeW9vnf5ZuUMRb0t6_Z6NxrOFcOxcK-Nrik_KJyRV5nLuCrPB5RLGOGtHh0AF0-FNLExW1vO09eBcZEA5BVB8DbF2X3u-6ycuyOVBHJkMa7EWEhh9WCjLCmEeN3nwSNCrAWp3ccUiLsIgO1gadvY-w3YFTp6gZnmtnNwALL5RrC6QKRE7DmHWzUPxqWmdXKO42Mmpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم جدیدی از حمله ایران به پایگاه آمریکایی در اردن| ۵ روز پیش
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/678520" target="_blank">📅 23:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678519">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تکذیب خبر شنیده شدن صدای انفجار در منطقه شلمچه
🔹
حیاتی، معاون امنیتی و انتظامی استانداری خوزستان هر گونه انفجار در مرز شلمچه را تکذیب کرد./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/678519" target="_blank">📅 23:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678516">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7duq5_VPWgIO4zTic_7FWGoO6O3v8xdKnY4uX931HI7A5QOqYGCM37asXLI_0CcE7uTJfcuE5_0N_d3Lou-jtbdLvcxcyGRjlkTpyRGSwu3ia-ZeSFqLO1RC6qJ7shijfngc_3FGS2_q1oy8wHNZwoZPZfJ_FNNB6HAK5ibAbnqSvUlW2dQ9VoLl5w9Ackvv8_zwTfW2AAVj5nWvBjO87Czo8U--malCwMGrlTzM7fDMR0iBF3B5E0i-bD8fROk44aOT17OZ8GEDwUNFzFIaRJaOKCDg0c2DUj2d6wmulODWj2t6rrfdhm_nzk8DcDUAyXYKcMSfEkzs1nYf3-MMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/McCb7dCiTBosp_6zNFmctOXM64CKnuJHsfY7nzdnJveZl3tnEdFFQBRPuSQKzM_xKE1-Nv_9S8EWtwER65Exq-bmR4aGP6dSXbNlAvTwqg7YXg5oDzGL1HLOZ6KZG_NRbPJaW2_j7UierczrvjSMhKe1QBeV1PSGUowgYPcjNFuKcdQkPqrmtlWjaCbPiqXLNHI2nsM37rLgIU-SxpHJ15i8lmx2Y36C2_52coK54tZmL5BXoa6DP8lSHNDNC2cnr0--gj0FglztcKpJ74DX20wbGKM7K0Fbedv6F5sLrAKKsuIMYJZ1el9lRvcTx1xsVvNq5MLyNVtFYNQLv_-m-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FiSoD6g_UvQSBtcHQuVQXNTc7gDXbe7kK7sJAfaIR0cgxojrCqDHM25tT-m63-js1Gehmrz2MXt2bzChvlsAgNMcVUKneCKUaZOAaa1HF1JXi7fFVbxjWtcRbNeiOtoBLNDnUZWCdwbShQ-KFj4jJmi7ShpwImdk4Msi9i7knZHyRMHtIvUtASX4FzowqkCnAofB7bqO7yNFF6YDUEOdNJ-PYroNgcS5n2k-rjmsCxGFyMfeVB4sJVxSmuqWQIzWI8t4mT6eWm5DeMKOQqixd2YtEeUBBpCGb4WXY_fG_4ou_6xjXTAUBWE29Hem4XAMWEtCCxUPDLm9YAIvyddwDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مدل جدید ناسا نشان می‌دهد زمین مانند سیب‌زمینی است
🔹
مدل جدید ناسا نشان می‌دهد زمین کاملاً کروی نیست و به دلیل توزیع نابرابر جرم، شبیه سیب‌زمینی با برآمدگی و گودی است (تفاوت واقعی فقط ۱۹۰ متر).
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/678516" target="_blank">📅 23:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678514">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hunqc9GlmMeGIzK4G1XWK9r_l16YbPn5q2CIBRmUD_0xlR7_sM8o1QqDokiXrCRBWIsdtzFKDQ231e9LCRNbspw-vLIxvgpu_us7Aq5oKazF2Fq7TsMaNbsWeUpJuKB1CuRTSP3eL_K4GbPpy_s7pmUigIekX8vVPGPoMdMkGWGEAM0qQ3BdHjCnKf99I1tAL_ogWGM7yFcG8lFT0UYzQil24gesBwY0DggVo2zd0V_LU-KmwD9G9D91BfxH7waN4TbZi1tYEnb6T5_GtZ6B_VVa-4jobS8sJTmbUB0SdhydD3IjYDM-8522aj8_cL9j7IIcabiL5COVfbQSG4mP0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWKEqPIPb9K_1HGXiveje-3Qme09AQ72OT2Dkm6wjeYsIZNqMnwsVx09mL3EQm-JgCHBKfBs3emW-JSxu3Z390FqvzUkJOWlKro5FdDu0_dlR1cBtJSVwM5YkjhDoaW64jF9DZrOg02r4Gkzpo1zrmEQBqozYAWl8I9BBi0yb5b78A0zAojQrgFEluxQGoIuY8QUxlDOwubu8h-06AvImZ00zujzT02PjRfsPRlIj4Arn4uNl33sYZSr5fzyoO_7NQuiN0o2MFFyqf2HvarwdbvI_l54nU2pR0jBIuKOQr4t6Tm9hckU-lhL2svy6csg16fnweXXxifajPacOIcFtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
♦️
حزب آزادی کردستان (پاک) اعلام کرد که در عملیات چند هفته پیش نیروهای ایرانی فرزند حسین یزدان پناه رئیس این حزب کشته شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/678514" target="_blank">📅 23:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678513">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ec74cdad.mp4?token=Jx-av-XhnoUeBT5Y3HpcCO-HE4WgsLIpkiQ3lwVjUcsrtZJRbRXc7-pBiU2nQK0mUXcal3JIefquYgtM0U6RTKvShp_t-25GoyylG2ZWOzdRAK0AV7fqLrmG434v9kevD-JqUk1A4Ae-bC7bf6dbfFVOpymfJ8JwmKPcneN_cVDbNY_apj5r6ItgxqCJwjjVfN3QmVSCsJnDpo8alKzXjxztW-GAx76cJaB4-nzVOsMTVFp9WlN67REgwWkV76q_oV508nkk-ArXNe_D-OVndWd0H5iE1_X6FiLWDHIXTjtb9p-XOOja7BAg9X5N6UPjecz6BHgjZw5b0x_kijoQwp4-Xe_edTYdEJYNg0lE5BHmtA2Azi559BA717Y0g0_81OhAdPlMRnmnZGM3zharDn9tLfppNp4eDic9Fjvjb4j7lIs5U3h7vRJo7J6JBPepqhG3zMseQgWVib9uf8sMbndUnuslqa-u8LzfATXPFFPlEIhUA8ZZVZVcCJ0a_M7W7Obm3LmJfHGME6K54h_SeJODEumPHD7W0-lA5dzg5_aG2Io8_REUqGpePXEkUU_XZIko18mFtr2eQMBXSiCJw65CatpA-otDc3wrCIDB6tON-S43Lz8PbphshDX8cwyz8aamm2xll-k3eqSN1-gV5s7x2KV1FivLDJmN36OScrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ec74cdad.mp4?token=Jx-av-XhnoUeBT5Y3HpcCO-HE4WgsLIpkiQ3lwVjUcsrtZJRbRXc7-pBiU2nQK0mUXcal3JIefquYgtM0U6RTKvShp_t-25GoyylG2ZWOzdRAK0AV7fqLrmG434v9kevD-JqUk1A4Ae-bC7bf6dbfFVOpymfJ8JwmKPcneN_cVDbNY_apj5r6ItgxqCJwjjVfN3QmVSCsJnDpo8alKzXjxztW-GAx76cJaB4-nzVOsMTVFp9WlN67REgwWkV76q_oV508nkk-ArXNe_D-OVndWd0H5iE1_X6FiLWDHIXTjtb9p-XOOja7BAg9X5N6UPjecz6BHgjZw5b0x_kijoQwp4-Xe_edTYdEJYNg0lE5BHmtA2Azi559BA717Y0g0_81OhAdPlMRnmnZGM3zharDn9tLfppNp4eDic9Fjvjb4j7lIs5U3h7vRJo7J6JBPepqhG3zMseQgWVib9uf8sMbndUnuslqa-u8LzfATXPFFPlEIhUA8ZZVZVcCJ0a_M7W7Obm3LmJfHGME6K54h_SeJODEumPHD7W0-lA5dzg5_aG2Io8_REUqGpePXEkUU_XZIko18mFtr2eQMBXSiCJw65CatpA-otDc3wrCIDB6tON-S43Lz8PbphshDX8cwyz8aamm2xll-k3eqSN1-gV5s7x2KV1FivLDJmN36OScrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو خبرگان رهبری: صلح و جنگ، مسائل راهبردی نظام، براساس قانون اساسی برعهده رهبری است
سعدی، عضو خبرگان رهبری:
🔹
اگر بخواهیم از امنیت ملی صیانت کنیم، باید بازدارندگی ایجاد شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/678513" target="_blank">📅 23:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678511">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_mABFZtTqrsWv7mQ4jukctZgDjLGadpG19NeehBVNNdrpz-HVf1Gq_82AdM_8lhOzKPkfjVjMlkGQOZo4-4WViHDb_hkHh4jjjZtdF5VrxXXn_R4n9Vti_Dbj4-J4i3_HHHO72K9kyYmS724wOI78geLspLqEd1Lf-RK0zd79A32Erv53zjcCWUSNIxmNVL3bIaFZpdfhdNyVfW1jBBd0p6VZwShO1jppfcFuEAWcfX5v4bktCXVYGzSA47u032V6yFO4jp-v5ni9riV65WXUMhe8nAzvFUE1du625PRj1NaKxFz32cHAOy924FX97USj0NcHy0AsaKybO8B8Gxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ زمینی ایران و آمریکا چگونه خواهد بود؟
🔹
واشنگتن سناریوی حمله زمینی به ایران را همچنان روی میز دارد، اما چرا تاکنون آن را اجرا نکرده است؟ در این گزارش به بررسی مهم‌ترین موانعی می‌پردازیم که آمریکا با حملهٔ زمینی تمام‌عیار به ایران با آنها مواجه خواهد شد.
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3235498</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/678511" target="_blank">📅 23:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678510">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سخنگوی دولت: شرط تداوم یارانه نقدی و کالابرگ اقامت در ایران است
🔹
مشمولانی که پیامک دریافت کرده‌اند، تا پایان شهریور با مراجعه به دفاتر پیشخوان، اقامت خود را احراز کنند.
🔹
اعتبار مرداد این افراد واریز نمی‌شود، اما بعد از احراز، معوقات پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/678510" target="_blank">📅 23:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678509">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5Ca-w3GtRIPkyCchpD0fYSmIqeDEKEZiYAQwEYQyqyGqNxRlqXgK2wKINtvOk8WP1yKMJzXmHGkUgUI_rzVvLW1AespIs1wBw0ZP3Xv9IptAI6y0_Pc9Cs9lH2OLC8g7DdeKl7Lp-uXBvJWAPV1hzPbWL5r-TyjftMNlu2BfHkOXcR56sY8JX3jfoswG5TV7ZJmnbyReJyqNq23fdy_kyAzZG2skJRSgKlf7oCJCo7wCtwN2qLGUEMciBLdANgpLK9CLY1zDgSsnk9Ng3pvcf-2B64kygXla3l7-ebCMNBYtRREZnueHT7_C2MY2Q2t7DHtCYheMnEvH67k6ON94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت کاهش یافت
🔹
قیمت نفت خام برنت با ۵.۲۶ درصد کاهش به ۷۹.۳۶ دلار در هر بشکه رسید.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/678509" target="_blank">📅 23:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678508">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/678508" target="_blank">📅 23:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678507">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
الجزیره: ساعات حساسی در پیش است
👇
khabarfoori.com/fa/tiny/news-3235497
🔹
واکنش دفتر رهبری به ادعای مطرح‌شده درباره قبول استعفای احتنالی پزشکیان
👇
khabarfoori.com/fa/tiny/news-3235491
🔹
«نوستراداموس چین»؛ پیش‌بینی جنجالی درباره جنگ علیه ایران | دو پیشگویی قبلی او که محقق شد چه بود؟
👇
khabarfoori.com/fa/tiny/news-3235477
🔹
انفجار در شهرک صنعتی شهر ری
👇
khabarfoori.com/fa/tiny/news-3235460
🔹
توئیت کنایه‌آمیز ضرغامی درباره جنتی و دبیری شورای نگهبان در ۱۰۰ سالگی
👇
khabarfoori.com/fa/tiny/news-3235499
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/678507" target="_blank">📅 23:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678506">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
آغاز عقب‌نشینی یا تاکتیک جدید آمریکا در منطقه؟
🔹
گزارش‌هایی از خروج نیروهای آمریکا از اربیل و احتمال کاهش حضور در کویت، بحث‌ها را داغ کرده است.
🔹
به نوشتهٔ الخنادق، این تحولات بیشتر به بازآرایی نیروها شباهت دارد تا عقب‌نشینی راهبردی، زیرا رویارویی اخیر با ایران، آسیب‌پذیری پایگاه‌های ثابت آمریکا را در برابر حملات موشکی و پهپادی آشکار کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/678506" target="_blank">📅 23:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678505">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8RM7zJPohiDh2a6AAZ_7Pfx_BIAxMgqoVuBSTEGpZTxLiCi9yJ50B0lRlg6ByDvCkhFbIBOcACiM-8KE27qKXnRXteGR5UU79kZArMmUcgGVYR9YDw79L9OqE6EglLfAUxDEPbGaEcNAiqf_zkVtt8QxZ8GN4NGsO8W59g1ztERQHx-98fHSzgSzUgkpzPBWldSR-qcnjfqxSwfjcCEzxOljTeGkzgevl210kH2426akY6ANnY6iwmto1f78AeOpmUL2dHWgHnpu5_CT-vCMSnxwgXt4fu8KcnZsS4SyiTFOjzxnIiovl6aYqwJVtn9Ov2OHn5_ZAeGEUbxQbTccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواب با کولر روشن؛ دشمن خاموش بدن؟
سه نکته طلایی خواب با کولر:
🔹
دما را روی
۲۴ تا ۲۶ درجه
تنظیم کنید.
🔹
حالت
Sleep یا تایمر
را فعال کنید.
🔹
رطوبت هوا را حفظ کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/678505" target="_blank">📅 22:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678504">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O--3aDmuUedYTHwWMRhrm783o-fdRU6QaaRi-8jOTZp3OqQsK3Enq3MULdb93NtTxKvvpLMIF4JEIASHwiMx0JF51zFd_NR3w8_GQLqsgAL2BTZa9Gu6gOj3gAX0FPGhORgzE5XxRWo7bVyMY6CBfVJiTJnahXDps6s8bSYbCKFWydffo4RnqtAi73v1JZApcCwtPImsUODqfgYNEHqyj7MRNw_dqCVGNDfU_ItdhhHUUd3lIotT7iQMSPF2cWBqIwzYmB0vhIVOMm0BCNhR5AUyEIhkhEOqMa2bSMLNxwZvMFju6wTvdgPV-1qVUR7zR_ts6csZyXjTGVhrY015Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
إنّنی أحبّکم...
رهبر شهید انقلاب: من شما جوانان عراقی را دوست دارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/678504" target="_blank">📅 22:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678503">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U98c0B6YDd8QW-z3B5y0hAVcfFtlZ7MkVwlBBj42poNz3i5F-hzFn3lVhyo52c20jFL4bPA27Qedc4VW3QQ06YPzd_yKakyTkLjy7vO8ySIsMnaV4098Mw_d1w62HPA0qdLcObAMdtosz5UE5bZqaGFvR9etFHDqB1ZJKDHqml9PetMmQpQIGip5hUwYaVAKOLTEkrk0aRb1Iy17AfiIfmztzAZ7ZngS8S-mZZ9WXzbSuPaQMM8uWmqJ54RJ_qAc_4gq3YSmEPniD1E0DBkhRMC_Y6Ui8kg53IDkGwq1VTdmI0jCxl7kTfQ9PrgAcDIn_dX77Ej9x4kkQP8_spr2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادآوری به جا اکانت سفارت ایران در آفریقای جنوبی، از توییت گذشته خودش در مورد نحوه کنترل ایران و ترامپ بر تنگه هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/678503" target="_blank">📅 22:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678501">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuPCmgewSdGCf6ocOjFeXAyya-xaQU4DF8UsgWFTi1jslW0Ahl_VvRO3gAKagIKzNL0g1HYRX5bD3S3cBKnFIqBjcKOe_N41JRVYQmcDD8xUFXYY2KsL03aj9PLo4hKWnX8LMBSWmBkiBnJAZrN7qZf-6zRYAOTtl1NCRD5fEg5XGu2_jHP0Nua-SykRjAi7OxvT3ooenSOU5Ky9zjcSR2pkEdcVlfxzH5K3knUqmnXcZ-EgZsk1i1aHuoOKqAEzYrwaXwDkMA4ipLKji7g-ECTWgqyAb2x2RVpOJynzyZGlYXOhLgFUCligCNtQG6xga-erYX34MYOcR4ByOhDcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9eec3cf4.mp4?token=j3BQqQBH27StBILuX-03oWb-rZe0LQ2a2js4nNh58uBTcfSruBaN9FZHvIA9HDv5EKpRy31qdRU8IFQ3F-wXbILkkW-0IWkgxMgYRjWxbbgilA0kWQ9Fq6-rbrmJTeY4xh2FH8LNOFNVM-1Pr9ULIWIfX5C4nf85umvq1lvt94He4aqdZLLcvIf79-XKoPIiOKXnorO04WRddKNFbmjwPu3OuuClKDqwop-744F-ddepiBsw0aFrj2r4xYlWXRS_nqLrq74zSMqXk_OdhpyVRLquGoz12jvzXE2mVpN8fhRRLlUhgl854wVTgjvMqaPCZl9URGNzsl-LMOs-Lvk6ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9eec3cf4.mp4?token=j3BQqQBH27StBILuX-03oWb-rZe0LQ2a2js4nNh58uBTcfSruBaN9FZHvIA9HDv5EKpRy31qdRU8IFQ3F-wXbILkkW-0IWkgxMgYRjWxbbgilA0kWQ9Fq6-rbrmJTeY4xh2FH8LNOFNVM-1Pr9ULIWIfX5C4nf85umvq1lvt94He4aqdZLLcvIf79-XKoPIiOKXnorO04WRddKNFbmjwPu3OuuClKDqwop-744F-ddepiBsw0aFrj2r4xYlWXRS_nqLrq74zSMqXk_OdhpyVRLquGoz12jvzXE2mVpN8fhRRLlUhgl854wVTgjvMqaPCZl9URGNzsl-LMOs-Lvk6ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا چین دست به تهدید اتمی آمریکا زده؟
🔹
چین برای نخستین بار تصاویر هوایی از بمب‌افکن H-6N منتشر کرده که موشک بالستیک هوابه‌زمین JL-1 با قابلیت کلاهک هسته‌ای (برد ۸۰۰۰ کیلومتر، بازورود فراصوت) را حمل می‌کند و دو جنگندهٔ رادارگریز J-20 آن را اسکورت می‌کنند.
🔹
این موشک هم برای اهداف ضدهوایی (کشتی‌ها) و هم حمله به اهداف زمینی قابل استفاده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/678501" target="_blank">📅 22:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678500">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2db0ae20c.mp4?token=bySAXCOPqUU-pynlCilvyeD58DBEu4NX9Oh1rMPn7qJqqbc3p4NDpJuclA8Z0Jpc1Wopgk1kl_0gJ8zllVFBcQOAjKr5fYuaB1F1kcpG3bEnlCR4kfRso6SZrPC963dayg55FK4fC0fdY0OreVIxyDKXcW3qRMfDjHxqAbKtHoCXnAl9rGjHInDhmLYplK5FpiU0XFKIpb1zl2fpF0wFbV1auCoufiSXS4ToOhVh-R5N9rYkZuhDH0FBgpEHqx2CO6EupyrAzkeUwVx77Z-EgF8hzKWG1ofLUaE3XOqE4I-1SpAXrkvOwBG_Ma9b1PcyXabfqrqc61eLFyzbUG8k2A9hjMa37aeZFaG2D3m_YUN8sTwnmctxnnetB3YeEwJ8ARiwny0dB7yJtePAUimYDP61Y4sQ_cTjjvzQqYdq6oCB7D-kdYuftg_Wux4JgnQCJ9yfbCVMgzutKZK5hFu24XgURbiYx4So0lAQA8ynFOyq1tRVOwF3vGnrQ41Rfr3K80Umrr-V_DyzVgDsHakKbpIF19ippNxD8e5IPK-icYcMn4jIvIIhIfw1ut9RQ2_aB9t4YAnAjA8BtrwgtJe6IvfQlWglO-djFFh9s8tOdXEhALoGTGecV5PeETQUKccJGQuj63shB-DU3lEwjlXv6lsVK_4RyX0-vIcfZyQfcOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2db0ae20c.mp4?token=bySAXCOPqUU-pynlCilvyeD58DBEu4NX9Oh1rMPn7qJqqbc3p4NDpJuclA8Z0Jpc1Wopgk1kl_0gJ8zllVFBcQOAjKr5fYuaB1F1kcpG3bEnlCR4kfRso6SZrPC963dayg55FK4fC0fdY0OreVIxyDKXcW3qRMfDjHxqAbKtHoCXnAl9rGjHInDhmLYplK5FpiU0XFKIpb1zl2fpF0wFbV1auCoufiSXS4ToOhVh-R5N9rYkZuhDH0FBgpEHqx2CO6EupyrAzkeUwVx77Z-EgF8hzKWG1ofLUaE3XOqE4I-1SpAXrkvOwBG_Ma9b1PcyXabfqrqc61eLFyzbUG8k2A9hjMa37aeZFaG2D3m_YUN8sTwnmctxnnetB3YeEwJ8ARiwny0dB7yJtePAUimYDP61Y4sQ_cTjjvzQqYdq6oCB7D-kdYuftg_Wux4JgnQCJ9yfbCVMgzutKZK5hFu24XgURbiYx4So0lAQA8ynFOyq1tRVOwF3vGnrQ41Rfr3K80Umrr-V_DyzVgDsHakKbpIF19ippNxD8e5IPK-icYcMn4jIvIIhIfw1ut9RQ2_aB9t4YAnAjA8BtrwgtJe6IvfQlWglO-djFFh9s8tOdXEhALoGTGecV5PeETQUKccJGQuj63shB-DU3lEwjlXv6lsVK_4RyX0-vIcfZyQfcOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعجب گزارشگر آمریکایی از پرچم‌‌های قرمز در دست زائران ایرانی اربعین امسال و فریاد خونخواهی
🔹
ایرانی‌ها میگویند خون در برابر خون و انتقام باید گرفته شود
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/678500" target="_blank">📅 22:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678499">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHumcFAURfjLZS5vHuglkE_yJ4QtzJcFLXld03ubgBu2w_XGqJWDw5wIun6fu72rsZi2cZKiCPuItgaKQXcjayoK7tE3G6oFZJ2UeKNPtTnem9PgkfG_ghif1couMZoo8XQ3XIVwf6pQGrF0njyZhtBShTe4JFv7pjmOQMAyt-vVZYELyd0yqFQKoVqklldp9tJBAEVW7mcUmU3pPmkQRvQo_vX4txCCpd68AB3x7BWezNdASjY1HCIZV4KfIhk4slB9mmtfum_FjIVxLwfSe5OwUhob5qlsGOz7uHglnYrPiKR0e1CKbkpYKvn3w0nvH27443Ye3zCc-Rw7rG_5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست اینستاگرام ایرج طهماسب: غمگینم بسیار زیاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/678499" target="_blank">📅 22:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678498">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09fcd91286.mp4?token=JRg1UPn_xGcfDXTavFwO4OfRFA8eSy6EdrtCY--eAfPva6Gmsxi-Cp_pCYj9fBVMUtp5B3DYsA0-NJK1Gom7fPCdmnJrnrirSl0KQ_VS50kycQH0_IR5ng7m2cYRkObCem2LPhUL8pR1fT9Tx0v0R52hyXDqw0kGjM7A-C2oyh105a-g8KBqFb7Yo6EoyeaMNSnShr6sWXmHZVvfPv9lphLSZaSOSRQSb41_-R6ELDoYjSP00SNuxFqNaVRCtqMmtk83h99KU1xC-jJDE2x19k1cQzmODr3tuQYmdEaXGi6bV3DoeKGTAlJDAsLxYp3_YGOHJvBDYpkxTInJqkNCDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09fcd91286.mp4?token=JRg1UPn_xGcfDXTavFwO4OfRFA8eSy6EdrtCY--eAfPva6Gmsxi-Cp_pCYj9fBVMUtp5B3DYsA0-NJK1Gom7fPCdmnJrnrirSl0KQ_VS50kycQH0_IR5ng7m2cYRkObCem2LPhUL8pR1fT9Tx0v0R52hyXDqw0kGjM7A-C2oyh105a-g8KBqFb7Yo6EoyeaMNSnShr6sWXmHZVvfPv9lphLSZaSOSRQSb41_-R6ELDoYjSP00SNuxFqNaVRCtqMmtk83h99KU1xC-jJDE2x19k1cQzmODr3tuQYmdEaXGi6bV3DoeKGTAlJDAsLxYp3_YGOHJvBDYpkxTInJqkNCDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی عشق از نیاز فراتر می‌رود؛ نگاه متفاوت به ازدواج
گری زوکاو نویسنده و استاد معنوی آمریکایی:
🔹
ازدواج در گذشته بیشتر بر پایه نیازهای زندگی، تقسیم نقش‌ها و بقا شکل می‌گرفت؛ اما امروز می‌تواند فراتر از این باشد؛ یک همراهی آگاهانه که در آن دو نفر علاوه بر ساختن یک زندگی مشترک، به رشد، شناخت و بهتر شدن یکدیگر کمک می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/678498" target="_blank">📅 22:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678497">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0127a6a477.mp4?token=Gze7lSU0A85skgY8ZPA37oqEWcKpeHnjzqeCtPJ5Xakufbdk0OUqdka_UJ8ICNtXcB-lUrCDSxrOGO8NoyYMF94F1GTFWgqxmLb6-kedqWK1d9iOMOfogro8v24IMLHZlQdrU4O3i-mqskFXZYTZiryxRDYV85VQvmfZXErP4Vjp71-DUjYjVdh5bdGrXIaeDSJG5fvsr9jYcz3jELmHUUIUgktUIiKUonr-352rtvM_ECExqu5mGEAmbtuNSXxiHjpawsiQxUk4VrUdAjqiRLqRpEDRETEsSVGAU8wE3EPz6ijmEqFz1M_MunEtH8eWCNEOBX6rvoSUM8eJV-aZGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0127a6a477.mp4?token=Gze7lSU0A85skgY8ZPA37oqEWcKpeHnjzqeCtPJ5Xakufbdk0OUqdka_UJ8ICNtXcB-lUrCDSxrOGO8NoyYMF94F1GTFWgqxmLb6-kedqWK1d9iOMOfogro8v24IMLHZlQdrU4O3i-mqskFXZYTZiryxRDYV85VQvmfZXErP4Vjp71-DUjYjVdh5bdGrXIaeDSJG5fvsr9jYcz3jELmHUUIUgktUIiKUonr-352rtvM_ECExqu5mGEAmbtuNSXxiHjpawsiQxUk4VrUdAjqiRLqRpEDRETEsSVGAU8wE3EPz6ijmEqFz1M_MunEtH8eWCNEOBX6rvoSUM8eJV-aZGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون، مجری مشهور و حامی سابق ترامپ کودک‌کش: ترامپ یک مدرسه دخترانه را بمباران کرد و بعد حتی عذرخواهی هم نکرد. دلم می‌خواهد یک سیلی به صورتش بزنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/678497" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678496">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
واشنگتن پست: ایران از تهدیدهای ترامپ نمی‌ترسد
🔹
بسیاری از مقامات و کارشناسان معتقدند که بیشتر تهدیدهای ترامپ فقط حرف است و او آخرسر عقب‌نشینی می‌کند.
🔹
تهدیدهای دونالد ترامپ دیگر مانند گذشته اثر بازدارنده ندارد و تکرار تهدیدها بدون اجرای آن‌ها می‌تواند از قدرت تأثیرگذاری این ابزار سیاسی بکاهد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/678496" target="_blank">📅 22:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678495">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGCcjLVvvLC6KPNXB0UrnnHIguxMpTjQbAsswQ5CYHMzoYHk_wp3Dhye3AilLc99wkXEbn9tDUCfge1bxPOSCzQngXbYx45pe0KB_bKACDMdiHhiB_PSwaVe6etWap17o251fh5xG1Lu4WFeWUqMzd6GAN_Y2Ppp5xxFXsIJsVWvO5Ezl-oFlFjTyQiOvB0Gv9zG-fo9lY2d6oAUSUo81u4pB5bUXAq4QpTjvuJ3fiRl7vJM5I06Cx-6yhrGuEgRxm3k3sUajd1psdgTP_HiWPfKA_RnOOCKCv6z4gNhcTwffEr7PJofcZLzDmohDZcEUb4hWFkCvwzwPspgN-t5xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی و سیاست خارجی مجلس: مدیریت شهری در مراسم اربعین و تشییع پیکر رهبر شهید عملکرد خوبی داشت
اسماعیل کوثری، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس:
🔹
در آن دو روز که پیکر رهبر شهید و خانواده ایشان در مصلی بودند، شهرداری واقعاً سنگ تمام گذاشت که جای تقدیر و تشکر دارد همچنین رسالت شهرداری در بدرقه از تهران و اقدامات فرهنگی و برپایی موکب‌ها در مناطق مختلف، نشان‌دهنده یک حرکت مردمی است.
🔹
اگرچه ممکن است برخی ایرادهایی بگیرند، اما باید دانست که خود مردم از این خدمات استقبال می‌کنند. با توجه به اینکه درصد بسیار بالایی از زائران اربعین را مردم تهران تشکیل می‌دهند، شهرداری با برپایی این موکب‌ها و پذیرایی از زائران، اقدامات بسیار خوبی انجام داده است.
🔹
خدمت به زائران آقا اباعبدالله الحسین (ع) و ابوالفضل العباس (ع) ماندنی است و ان‌شاءالله خداوند برکت چندبرابری به این اقدامات عطا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/678495" target="_blank">📅 22:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678494">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
المیادین به نقل از رسانه‌های پاکستانی: محمد باقر قالیباف، در دهم اوت آگوست، ۱۹ مرداد به پاکستان سفر می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/678494" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678493">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
رئیس جمهور شیاد آمریکا در گفت‌وگویی با امیر قطر، درباره راه‌های کاهش تنش میان واشنگتن و تهران رایزنی کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/678493" target="_blank">📅 22:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678492">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/678492" target="_blank">📅 22:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678491">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2593614ef5.mp4?token=M-uJAA4IJoB5SJpLDZQqE7UG4Pip_lbID4wMPo37SktW8Um7EqreLOeDsq6-Julf-ApIxlvb7i8QLALXJfpuE8fkldd4nv9dmlSG5u0fP6BMcMnJYjrEP_-KstKK4XlwXoWbnb4OUJB7n5Ull4fVsHpNuvF4I2XYH5c4kPiAUSLwrMAo6ZRvo_J-J4MXDwZgDd5MNX-k6nIpogeg08QtVz-6r3Zz0gjKgHOpfKSuno5WvP9KIL5h8wx3Yd-lgB6QlUlIS1RVKLggYwduO4podhftgKHqf5nOqRrnKy1jYiXD6OogNT03N7luKIFD3ktwFet1gHmUw7i4pO9z9OjLRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2593614ef5.mp4?token=M-uJAA4IJoB5SJpLDZQqE7UG4Pip_lbID4wMPo37SktW8Um7EqreLOeDsq6-Julf-ApIxlvb7i8QLALXJfpuE8fkldd4nv9dmlSG5u0fP6BMcMnJYjrEP_-KstKK4XlwXoWbnb4OUJB7n5Ull4fVsHpNuvF4I2XYH5c4kPiAUSLwrMAo6ZRvo_J-J4MXDwZgDd5MNX-k6nIpogeg08QtVz-6r3Zz0gjKgHOpfKSuno5WvP9KIL5h8wx3Yd-lgB6QlUlIS1RVKLggYwduO4podhftgKHqf5nOqRrnKy1jYiXD6OogNT03N7luKIFD3ktwFet1gHmUw7i4pO9z9OjLRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هجوم ناگهانی سیل به خانه‌های مردم در خیبر پختونخوا پاکستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/678491" target="_blank">📅 21:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678490">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
یک مقام مسئول در کاخ سفید به الجزیره: رئیس‌جمهور جنایتکار آمریکا در را برای انجام مذاکرات بر اساس درخواست شرکای منطقه‌ای‌مان باز می‌گذارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/678490" target="_blank">📅 21:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678489">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20441d4374.mp4?token=hCnWY2Pv5gDu8WtRyQYrysvdrpbq55AiWVjuqw8LSGVjzJbLphc2_w_3-J9sauXYdCBQyOD7nn_AZUK3UCOxd3_03HH428_Jd0VMFCGKOJTQeP7JpOP5GFW-ZIX5a10WEUiwknVkMGdaeTeQkphTRpD3mf_UuOG0GJZz8preNN0zGsINSBhZrunsJoKBurlh4xRZOaISV55_GZKuA8Enorxle07RbUml63GBnUDzOt5B0LcNv22_VtC8q3BI4GvekeWuZQzCTqOBjhn8B5fXIgPHE_AYBHBEy3f6cDHV3PrquglnQD1mQoeBSAQOE0KLSrM-csYUODI-TzX6dXZE1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20441d4374.mp4?token=hCnWY2Pv5gDu8WtRyQYrysvdrpbq55AiWVjuqw8LSGVjzJbLphc2_w_3-J9sauXYdCBQyOD7nn_AZUK3UCOxd3_03HH428_Jd0VMFCGKOJTQeP7JpOP5GFW-ZIX5a10WEUiwknVkMGdaeTeQkphTRpD3mf_UuOG0GJZz8preNN0zGsINSBhZrunsJoKBurlh4xRZOaISV55_GZKuA8Enorxle07RbUml63GBnUDzOt5B0LcNv22_VtC8q3BI4GvekeWuZQzCTqOBjhn8B5fXIgPHE_AYBHBEy3f6cDHV3PrquglnQD1mQoeBSAQOE0KLSrM-csYUODI-TzX6dXZE1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منتشر شدن تصاویر یک کشته آمریکایی در تجاوز به ایران
🔹
به تازگی تصاویری از تشییع یک گروهبان آمریکایی که براثر اصابت پهپاد ایرانی به هلاکت رسیده بود در رسانه‌های آمریکا منتشر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/678489" target="_blank">📅 21:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
جزئیات جدید از مذاکرات ایران و عمان برای بازگشایی تنگه هرمز
یک منبع نزدیک به تیم مذاکره‌کننده:
🔹
ایران تنها با عمان درباره ترتیبات مدیریت تنگه هرمز مذاکره می‌کند و
هیچ گفت‌وگویی با آمریکا نداشته است.
🔹
ایران تأکید دارد مسیر جنوبی ایجادشده پس از بدعهدی آمریکا، غیرقانونی و تهدیدکننده حقوق حاکمیتی ایران است و بر سر ایجاد کریدور میانی با عمان در حال رایزنی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/678488" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678487">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdElxUJ5PBGEkkiYckhVZCdJaXIGDYQItYbrBSknv7h4ixyWtzFrRs_D3M4-VO4doCEyGG4LEPsV5e1P2jlJpsb7Tf_OzVUOAPR3x_mLhAMOSCBV7A1JGAyqc1_ACQfn0Lwy-rHPodX0qaYEUIUHZg8Brf8PF908hn0zKPpUcRho-4ZPY57ArajKpbMr5V8i6adxbgI4EUv74v7FHtArAJN6H8qLHrjjgLRzrVI5cENd9oaiHVLsppArgomh8t1gQ8r8z9u8XosnaStLVz_k6zrOjrVZ_zFmBGxuuoH0aQUM_EsAQaFfqFD3Ky5LPTQTA1kbyV-SgUy6siJFigMOGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
نوین‌ایر از جوانان مستعد برای استخدام مهماندار زن و مرد دعوت به همکاری کرد
🔹
شرکت هواپیمایی نوین‌ایر در راستای تکمیل و توسعه کادر مهمانداران کابین خود، از جوانان علاقه‌مند و واجد شرایط برای همکاری به عنوان مهماندار مبتدی (Cabin Crew) دعوت به عمل آورد.
🔹
بر اساس اطلاعیه منتشرشده، این فرصت شغلی برای بانوان و آقایان دارای شرایط عمومی و اختصاصی تعیین‌شده فراهم شده و متقاضیان می‌توانند با ارسال درخواست خود، مسیر حرفه‌ای خود را در صنعت هوانوردی آغاز کنند.
🔹
نوین‌ایر اعلام کرده است علاقه‌مندان واجد شرایط می‌توانند برای دریافت و تکمیل فرم درخواست همکاری، از طریق پست الکترونیکی زیر با مدیریت سرمایه انسانی این شرکت در ارتباط باشند
hr@novinair.com
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/678487" target="_blank">📅 21:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1117d915.mp4?token=clloY2B8Gur1_uW2ZHYnqVW1w6ROG9Qe8Pi2cUZHbThghOPDkW0uCl45PALd1biaSTheCy2Bzap6HPT5-e7W4B95INPrE7IIwvuLeWKkmOBLQsoUFWzSnIyYfaPUfs24Ap3lzNWds452UXMcCJKwJFCjd-Hd3p-qGyebhSad110B_tCwdCpqu9z9mSJs8GTBJYQ8bOo8Xkvk75ydiK-BK1JT-yl4emYDSCGwzZkULUd93Lzf-exO6oYP91QaDNP7DmMrL0v6PT4a4KngqLzA2olvUKE7ct3y5GgLmuhsnIKpSakkPxIiIybm534vmmBg0X6Vo4aD8rg3WnTQjiFUnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1117d915.mp4?token=clloY2B8Gur1_uW2ZHYnqVW1w6ROG9Qe8Pi2cUZHbThghOPDkW0uCl45PALd1biaSTheCy2Bzap6HPT5-e7W4B95INPrE7IIwvuLeWKkmOBLQsoUFWzSnIyYfaPUfs24Ap3lzNWds452UXMcCJKwJFCjd-Hd3p-qGyebhSad110B_tCwdCpqu9z9mSJs8GTBJYQ8bOo8Xkvk75ydiK-BK1JT-yl4emYDSCGwzZkULUd93Lzf-exO6oYP91QaDNP7DmMrL0v6PT4a4KngqLzA2olvUKE7ct3y5GgLmuhsnIKpSakkPxIiIybm534vmmBg0X6Vo4aD8rg3WnTQjiFUnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیدا شدن مهمات جنگ جهانی دوم در فرانسه پس از آتش سوزی جنگلی
خبرگزاری فرانسه:
🔹
در میان خاکسترها، ۴۰۰ عدد پوکه و قطعه مهمات از جنگ جهانی دوم پیدا شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/678486" target="_blank">📅 21:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be3577ab49.mp4?token=jBjxwuuotbcePm4M7W8GIBn_2ktWFFfuxgVQ3XedoyjcLVydJeNVQ6KJ0kuh9-wZRJDqALubaMn_jD94Od5kt0w2A8zOByT-sp60EmaNuqBdu1-FYydMOlzl4BuNWuONL9qKPV3Otu0RCZk_dBzSwPpHAXGZxWdSzPGxjJf-NdWc30a677UxccM5eRMxZqHBsYV9tYClSTAn2hYWdrSklnNXwoy8huW1CnM7trFzEesltpWn1PJcqPxtMW-jR2b4H1QhesezmAt-qHMtKRqfcIMMDA6gP7XDu2AIC8uOIOhsDtMQYyv4A0X68MpNiu9Ubw0Gq5abk-y4d-2RxC0cgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be3577ab49.mp4?token=jBjxwuuotbcePm4M7W8GIBn_2ktWFFfuxgVQ3XedoyjcLVydJeNVQ6KJ0kuh9-wZRJDqALubaMn_jD94Od5kt0w2A8zOByT-sp60EmaNuqBdu1-FYydMOlzl4BuNWuONL9qKPV3Otu0RCZk_dBzSwPpHAXGZxWdSzPGxjJf-NdWc30a677UxccM5eRMxZqHBsYV9tYClSTAn2hYWdrSklnNXwoy8huW1CnM7trFzEesltpWn1PJcqPxtMW-jR2b4H1QhesezmAt-qHMtKRqfcIMMDA6gP7XDu2AIC8uOIOhsDtMQYyv4A0X68MpNiu9Ubw0Gq5abk-y4d-2RxC0cgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو پیشنهاد آمریکا برای غزه را رد کرد
🔹
نخست‌وزیر اسرائیل تأکید کرد که این کشور از غزه خارج نخواهد شد تا زمانی که حماس به‌طور کامل خلع سلاح نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/678485" target="_blank">📅 21:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678484">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: شروط ایران برای بازگشایی تنگه هرمز اعلام شد
🔹
ایران اعلام کرده است که مایل به بازگشایی تنگه هرمز است، اما خواستار حق دریافت هزینه‌های ترانزیت، تضمین‌های امنیتی در برابر حملات آینده، پایان محاصره دریایی ایالات متحده و لغو تحریم‌های نفتی ایالات متحده است.
🔹
ایالات متحده و کشورهای خلیج فارس درخواست هزینه را رد کرده‌اند و اصرار دارند که ایران ابتدا تنگه را بازگشایی کند و ایمنی کشتیرانی و امنیت منطقه‌ای را قبل از هرگونه لغو تحریم یا سایر امتیازات در نظر بگیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/678484" target="_blank">📅 21:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678483">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/678483" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678482">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
افشای هدف اصلی مذاکرات خفت‌بار بیروت و تل‌آویو از سوی آمریکا
🔹
وزارت خارجه دولت تروریست آمریکا مهمترین هدف مذاکرات خفت بار میان دولت غربگرای حاکم بر لبنان و رژیم صهیونیستی را مقدمه سازی برای توافق فراگیر سازش و عادی سازی روابط میان بیروت و تل آویو عنوان کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/678482" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678481">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ec22fe91.mp4?token=vED25Am2c3E10RYKpqZasPn7KLRiG2atnj5te523UXH7LHxMtOfiZsu8w3UInpY3XLhNUaH8y3AB4bHmjFIOu29crehJquQ0hj6e3b6g6Suiy17gnIplxNWoHhymHCNWB_03-AT8OhCSWyIfE08iJs9VT-_1Gkccp3bEhsQHrL7hvOCujdRHD_X1zexqKEkg4gRQKsvqvXk5-CA_WnyCI0yoyM8tywL7AHa5IgPAoj6Mn4mAcEgtn1vUTXqyCLAhhS9hdsikTS34RO9jbjtdGBSbZ5zTZpSFUORz_Qnql7RIf5H7hyp6tNWVoBMTbwM7FYW1kQtYmpF4OcZ9PjmChg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ec22fe91.mp4?token=vED25Am2c3E10RYKpqZasPn7KLRiG2atnj5te523UXH7LHxMtOfiZsu8w3UInpY3XLhNUaH8y3AB4bHmjFIOu29crehJquQ0hj6e3b6g6Suiy17gnIplxNWoHhymHCNWB_03-AT8OhCSWyIfE08iJs9VT-_1Gkccp3bEhsQHrL7hvOCujdRHD_X1zexqKEkg4gRQKsvqvXk5-CA_WnyCI0yoyM8tywL7AHa5IgPAoj6Mn4mAcEgtn1vUTXqyCLAhhS9hdsikTS34RO9jbjtdGBSbZ5zTZpSFUORz_Qnql7RIf5H7hyp6tNWVoBMTbwM7FYW1kQtYmpF4OcZ9PjmChg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سؤال امیلی گرت‌ویت، عکاس و مستندساز انگلیسی، از مردم دنیا درباره سانسور اربعین!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/678481" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678480">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDLk2WH79zWF9sFFkFPod58CpA9NRI9ON4jx4gZ1N9p4-XYD9MMq6lcjHt424vBUqAECU9WsLFDVmM1o2b0RiKecatZUBHex78kixs3FaMligBqSPktvY0Ua_pxlDJGe_osELnoBM6atKuNjVbd36-wViRt2w9J084O5WryeMvYjC1eiuYEvOYuyyVq7QSPRMN9fcQ-RGCC4gXcFtrs47YfW3ZG7hFJ_feuOyGtOpdmPsoSmMz5HJHbIiDfpAmTul5Vuko1eO_da2O0_O8Cs9SHx3ioZ9qkcKfQLoAMsVKvrFFd3Oh3XdXQxw8Axa_GLsCvKK22RlNvGbtMwUHN5DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عربستان به‌دلیل خسارت‌های اقتصادی، یک تریلیون دلار به یمن بدهکار است
فعال رسانه‌ای حوزه جنگ اوکراین:
🔹
آمریکا در طول ۴۵ سال و نیم گذشته، به‌دلیل خسارت‌های اقتصادی، پنج تریلیون دلار به ایران بدهکار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/678480" target="_blank">📅 21:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678479">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سپاه هرمزگان: از فردا احتمال شنیده‌شدن صدای انفجار کنترل‌شده در اطراف بندرعباس وجود دارد
سپاه هرمزگان:
🔹
از فردا به‌مدت ۳ روز در ساعات ۸ صبح تا ۱۲ عملیات انهدام مهمات عمل‌نکرده در محدودهٔ ایسین و سرخون انجام خواهد شد؛ شهروندان نگران نباشند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/678479" target="_blank">📅 21:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678476">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54678ab5de.mp4?token=H4wCoK51T5DPDTBIvvAIXvgPH16HwgiUSnYj-nVBdIIND118yK_kcM84bF-th4fzAlDMbdxscTIWNoPL4bT1qRyyC0KppunvILrmWVr0JMwTnVcQBanb1D4PGvf_AkMD3sPUm86Tq_mRpKp1Kefj1eHtYGk2j9MQDFw62SGcPUl-I6-9ZdOKzXLgeIw68HSAOeFLF3EPlGGTigD1McrbtX6TDjCZ2rm4_TWFujkZ4vyRvjxWf9beI8vNgdkr6IoRej1-m4C5uWdzbpThs2bwQCZhFoiMTgpScS25ahs_V3YhyRb-qlOQzMnOc0vaOrqSg_8JDOsbZTUllisf3hnjfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54678ab5de.mp4?token=H4wCoK51T5DPDTBIvvAIXvgPH16HwgiUSnYj-nVBdIIND118yK_kcM84bF-th4fzAlDMbdxscTIWNoPL4bT1qRyyC0KppunvILrmWVr0JMwTnVcQBanb1D4PGvf_AkMD3sPUm86Tq_mRpKp1Kefj1eHtYGk2j9MQDFw62SGcPUl-I6-9ZdOKzXLgeIw68HSAOeFLF3EPlGGTigD1McrbtX6TDjCZ2rm4_TWFujkZ4vyRvjxWf9beI8vNgdkr6IoRej1-m4C5uWdzbpThs2bwQCZhFoiMTgpScS25ahs_V3YhyRb-qlOQzMnOc0vaOrqSg_8JDOsbZTUllisf3hnjfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمد انصاری، بازیکن اسبق پرسپولیس: اربعین امسال را به نیابت از رهبر شهید و شهدای جنگ ۱۲ روزه قدم برمی‌داریم/ یاد عزیزانی که سال گذشته در کنارمان بودند، در این مسیر زنده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/678476" target="_blank">📅 21:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678474">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
الجزیره: ساعات سرنوشت‌ساز برای تعیین وضعیت تنگه هرمز در پیش است
نورالدین الدغیر:
🔹
طی ساعات آینده احتمال مشخص شدن وضعیت تنگه هرمز و
توافق احتمالی وجود دارد.
این روند به بازنگری واشنگتن در محاصره دریایی و تحریم‌های نفتی وابسته است و می‌تواند زمینه‌ساز ازسرگیری مذاکرات و تمدید تفاهم‌نامه‌ای شود که ۱۷ اوت منقضی خواهد شد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/678474" target="_blank">📅 20:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678473">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79aab0b359.mp4?token=SRwv1PmeI2UZ7wXVLBs0sLhuBfXnGEX8LPpbVbzr7waXsysBJCOI3Kk6nJcODL6CFLT0ykYYTd_s9a7RLCYJrBJhSACONuSqMYEY8ugY7eAY5WzJN4VFL_DguBv0Jh849RH1zhpY3DK58A0XJ8YOxGxRZuEPN1sff0LazMDZFvvdhjyPA7cq89XPr-NM-BrT96XKbGELJnt_2wU4Ai_33dTQKG0sq47IuZWqI7GQ387DrfiH3q-r97iZKOkRM_3tQ0Gb2z0amAYVVi2Lu-xZUXnXrlKoIJUZWd-Glu0H9K0pl9IjHAcekrbi4t3MXnz1STY4eYynbO5951J0KDuWJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79aab0b359.mp4?token=SRwv1PmeI2UZ7wXVLBs0sLhuBfXnGEX8LPpbVbzr7waXsysBJCOI3Kk6nJcODL6CFLT0ykYYTd_s9a7RLCYJrBJhSACONuSqMYEY8ugY7eAY5WzJN4VFL_DguBv0Jh849RH1zhpY3DK58A0XJ8YOxGxRZuEPN1sff0LazMDZFvvdhjyPA7cq89XPr-NM-BrT96XKbGELJnt_2wU4Ai_33dTQKG0sq47IuZWqI7GQ387DrfiH3q-r97iZKOkRM_3tQ0Gb2z0amAYVVi2Lu-xZUXnXrlKoIJUZWd-Glu0H9K0pl9IjHAcekrbi4t3MXnz1STY4eYynbO5951J0KDuWJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید غلامعلی رشید: اختلاف حقوق، سم نیروی انقلابی است
🔹
خدا میداند بین یک نیروی جزء و فرمانده در سپاه چقدر اختلاف حقوقی وجود دارد و آیا فرمانده کل سپاه نیروی خودش را درک میکند یا خیر.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/678473" target="_blank">📅 20:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678472">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/309a7e5446.mp4?token=pm6SuPrapSPBeLw_CCj9ZXz_H7htWaVcjKinQrspCsO2h25X9e4bBrXD0_i1OlNyuKntLsIpOteBW7l4PERxkDbn6oJGttUqnjAV6VtdXvEhFGXtrT6mh0G11FmKn2bkLbJ0uaBuS7_Fvj-AQyDTx_SoROQRhyLDxk_LGGnxftzHzGDS2CXWI6BQPtZwJ2ibBSeyGMa18yfTucMAg5FGIX6ANUk1hgPymLhgkA0qejW_99brUiLmyoPRvbn9zCBbtAazWLw-YnKSyzU6caF--q441qhRjNUaRRMk7Usx7HQof2onZgDPpBiGAUE9f1-kCjrO6gUR5h73AeSO0XPI-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/309a7e5446.mp4?token=pm6SuPrapSPBeLw_CCj9ZXz_H7htWaVcjKinQrspCsO2h25X9e4bBrXD0_i1OlNyuKntLsIpOteBW7l4PERxkDbn6oJGttUqnjAV6VtdXvEhFGXtrT6mh0G11FmKn2bkLbJ0uaBuS7_Fvj-AQyDTx_SoROQRhyLDxk_LGGnxftzHzGDS2CXWI6BQPtZwJ2ibBSeyGMa18yfTucMAg5FGIX6ANUk1hgPymLhgkA0qejW_99brUiLmyoPRvbn9zCBbtAazWLw-YnKSyzU6caF--q441qhRjNUaRRMk7Usx7HQof2onZgDPpBiGAUE9f1-kCjrO6gUR5h73AeSO0XPI-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز شربت زعفرانی که تا یک سال شکرک نمی‌زند
!
مواد لازم:
🔹
۶ لیوان شکر
🔹
۳ لیوان آب
🔹
یک سوم لیوان گلاب
🔹
نصف ق چ جوهر لیمو
🔹
نوک ق چ وانیل
🔹
زعفران غلیظ به دلخواه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/678472" target="_blank">📅 20:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678470">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3Rvu8eTWDeiJP8o914nDdt_rG5d1OMdjHYnDsdjtEf5BfUJmeSjV1Mqy761RlhpCdGlTp2wu5C2eS9-5X32lMqBcGlukpIKR7hUpapKTUFqn-Rdh_i5nplPMdZjR0bmjHSy3eMHSAKO85NHXSUGoE0ein7kxLMmq03-tMrmHTjMvwWpwVruXuySpU0lv5SP2cfaWbe9EQ_uHexXuh05FOIElmSpfZjGIlPpLS7WZxJuOW8zA4lKw5Ed-bjykmXl6ZzHshluWvWiOlITVOfnIMBVUv7-YTHU6PjZbuBVUDVQyT9NcqIoJfGLTqgUp8hTIrLrUdQkI2qtYOevhbcERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یزید؛ عموی جدید علی کریمی
🔹
علی کریمی این‌بار در پستی از «یزید» به‌عنوان عموی خود یاد کرد؛ اقدامی که با واکنش رسانه‌ها روبه‌رو شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/678470" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678469">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56502a6d.mp4?token=MSnV-psUTEfU2FqiFcQvHVna6G_zBey0W2LyfbB5fVg4Y7kFwGpiP_J_gT7v6Fk-OK0MiNgoBM0r1psurSd88wvk8hwPbfeD0TqgzDF4uHCX9vJPnFviGQV5JX58lEgO5LE-q8F9PhhCzVldZMzQdmiwq08cGm1C01_8-ZvpFbvBqZjLkbnMb7FyqQVfjBFCh7CJWajjKDbde-SpbgLfOh7SY_0oJVYh0gKGGMkrHXgd2eosOlEtZuGizq4EBwRrjymLwnMGDb6VOWmJpHHnx2oyI2rzvGYI6fySZU5BtxL4_48rFS2L260XWfs8uAO3IHB5P1pfcuoxmMdwthn-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56502a6d.mp4?token=MSnV-psUTEfU2FqiFcQvHVna6G_zBey0W2LyfbB5fVg4Y7kFwGpiP_J_gT7v6Fk-OK0MiNgoBM0r1psurSd88wvk8hwPbfeD0TqgzDF4uHCX9vJPnFviGQV5JX58lEgO5LE-q8F9PhhCzVldZMzQdmiwq08cGm1C01_8-ZvpFbvBqZjLkbnMb7FyqQVfjBFCh7CJWajjKDbde-SpbgLfOh7SY_0oJVYh0gKGGMkrHXgd2eosOlEtZuGizq4EBwRrjymLwnMGDb6VOWmJpHHnx2oyI2rzvGYI6fySZU5BtxL4_48rFS2L260XWfs8uAO3IHB5P1pfcuoxmMdwthn-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت هشت دانشجوی کره جنوبی حین سر دادن شعارهای ضد آمریکایی در منطقه نظامی
🔹
هشت دانشجوی کره جنوبی پس از متهم شدن به ورود به یک پایگاه هوایی و سر دادن شعارهای ضدآمریکایی، از جمله «بیایید نیروی هوایی هفتم آمریکا را درهم بکوبیم»، بازداشت شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/678469" target="_blank">📅 20:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678467">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
وزارت کشتیرانی هند غرق شدن کشتی خود را نزدیک یمن تایید کرد
🔹
وزارت کشتیرانی هند اعلام کرد که کشتی هندی «ام‌اس‌وی» نزدیک آب‌های یمن با اصابت یک پرتابه مواجه شده که در پی آن، این کشتی واژگون شده و غرق شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/678467" target="_blank">📅 20:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678465">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a241da0c1e.mp4?token=OqXel2s2KY822Vo9lF5kedisXD90lfoYiEDtQcqD6RPaWBTDwknAdOlvqW-MArCE_MvDCWG1uBTcK9P7O1FmwRSyAgnbLeg9bomQUUR3zpSGK3vKZemn3oBRZSZRG5jYmyLoNFn9hywDkTOWPkWWR5QkbX-kyYRxMgTOPEF3c5WPUBeHISNuURsEJHytxYxho0hJ6vXeEtu6-X0LDije8p2jqCF2IAbFkoesiQ3-lCFmyEn0Pkc3Dhaz-ljQM65TwWMegXQFC8Jh1BOmd8isMmnZmuVv2nItmLfs7pTBpzTGrIku7Pun8E3wFHsld10d3YRGvd8Q_H_g8dPoNgAFpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a241da0c1e.mp4?token=OqXel2s2KY822Vo9lF5kedisXD90lfoYiEDtQcqD6RPaWBTDwknAdOlvqW-MArCE_MvDCWG1uBTcK9P7O1FmwRSyAgnbLeg9bomQUUR3zpSGK3vKZemn3oBRZSZRG5jYmyLoNFn9hywDkTOWPkWWR5QkbX-kyYRxMgTOPEF3c5WPUBeHISNuURsEJHytxYxho0hJ6vXeEtu6-X0LDije8p2jqCF2IAbFkoesiQ3-lCFmyEn0Pkc3Dhaz-ljQM65TwWMegXQFC8Jh1BOmd8isMmnZmuVv2nItmLfs7pTBpzTGrIku7Pun8E3wFHsld10d3YRGvd8Q_H_g8dPoNgAFpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خطرناک‌ترین پدیده برای جامعه ایران چیست؟
فولادیان، استاد جامعه شناسی:
🔹
جامعه ایران خیلی صفر و یک شده، یا بر حق هستی یا حق، هیچ راه میانه و وسطی برای تو باقی نمی‌گذارند.
🔹
عملا هیچ وسطی را به رسمیت نمی‌شناسیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/678465" target="_blank">📅 20:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678464">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
از گودال‌های آتش تا بازگشت به زندگی؛ روایت تکان‌دهنده یک تجربه نزدیک به مرگ
🔹
00:08:00 کشش شدید به سمت یک چاه تاریک از پشت سر
🔹
00:12:00 نجات یافتن از میان دهکده آتش با صدا زدن نام اهل بیت
🔹
00:28:00 اقامه نماز جماعت با پیشوایی حضرت علی(ع)
🔹
00:40:30 حسابرسی توسط ۳ خانم و پاکی نامه اعمال به خاطر زایمان
🔹
00:51:30 درخواست بازگشت و فرصت دوباره در سجده بر خوشبوترین خاک
🔹
01:01:00 رؤیت وضعیت برزخی خواستگاری که از خودکشی‌اش بی‌خبر بودم
🔹
01:08:50 روی برگرداندن امام حسین(ع) از من بخاطر نیت و تلاشم برای سقط فرزند
🔹
قسمت بیست‌ویکم (لوح سفید)، فصل پنجم
🔹
#تجربه‌گر
: معصومه فیضیان
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/678464" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678463">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc72e04a0.mp4?token=qjByGsjHoolRutiaG3tLCB8Ot23qwII196HDzlqQIUxpsIX-G0BG9mqv6FDQ9_qd1G319O0GK2yrjuFZiQxY-4G7huiDxrwXQgpPsCTTowsUCNjX_1_LvAwZ8124yc4_JfSX-aF2-WIDu35sTY_YSrT7ITVf7dJczs5FFxn_yfBg7JBV8KVBu3v0cfGy4Bjyrw04oN7fZgiXI1Y0RLwj7vS3y-_0kUHJCDMWvwsuklv_biavei5-XFQgMrZTZesspSIKA22KtkDSbB1dEeIrn9psiZRGJLVDRsVEDLhqB9II1uOy7sM6AItiDro0vQF6v6Ok0Hlk-tGgWJHfa-O3mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc72e04a0.mp4?token=qjByGsjHoolRutiaG3tLCB8Ot23qwII196HDzlqQIUxpsIX-G0BG9mqv6FDQ9_qd1G319O0GK2yrjuFZiQxY-4G7huiDxrwXQgpPsCTTowsUCNjX_1_LvAwZ8124yc4_JfSX-aF2-WIDu35sTY_YSrT7ITVf7dJczs5FFxn_yfBg7JBV8KVBu3v0cfGy4Bjyrw04oN7fZgiXI1Y0RLwj7vS3y-_0kUHJCDMWvwsuklv_biavei5-XFQgMrZTZesspSIKA22KtkDSbB1dEeIrn9psiZRGJLVDRsVEDLhqB9II1uOy7sM6AItiDro0vQF6v6Ok0Hlk-tGgWJHfa-O3mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش احساسی رضا قیطاسی، قهرمان مردان آهنین به حضور در پیاده‌روی اربعین/ روایتی از حال‌وهوای متفاوت این سفر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/678463" target="_blank">📅 20:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dabb9ebf96.mp4?token=L4lK679fVtEg1daXBaT9VRpJhuj6y__kdU-FiYPGeEhJm1tNQi5F0ptlPWb2wy1iZGJzSsDVwW3O5b00J6zMo_o84fR75feFLI1zFlgx_NyfDGpB9U2n1C99oDpvSIl9gJmpe15ubvkU5s0RfBWhnPEdIAde9k6Asp7PxbOgGCuZ9wOT3VGUhKbqi1j9AqbH6MY4BtWB8afxX10pq5p_vfM3d_RYFPhdk0k_UUc5xel9txvu79b3JZMeiyUmjFEOzllqhO_fu4KT6JfWih0vpkM8JlHmOqcHcq-obAkQ0OnLSpZZ175obw4DO1vVvApMKNOZ_7KmHQ469fxCnl_Cxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dabb9ebf96.mp4?token=L4lK679fVtEg1daXBaT9VRpJhuj6y__kdU-FiYPGeEhJm1tNQi5F0ptlPWb2wy1iZGJzSsDVwW3O5b00J6zMo_o84fR75feFLI1zFlgx_NyfDGpB9U2n1C99oDpvSIl9gJmpe15ubvkU5s0RfBWhnPEdIAde9k6Asp7PxbOgGCuZ9wOT3VGUhKbqi1j9AqbH6MY4BtWB8afxX10pq5p_vfM3d_RYFPhdk0k_UUc5xel9txvu79b3JZMeiyUmjFEOzllqhO_fu4KT6JfWih0vpkM8JlHmOqcHcq-obAkQ0OnLSpZZ175obw4DO1vVvApMKNOZ_7KmHQ469fxCnl_Cxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معروف‌ترین سلبریتی‌های دنیا طرفدار چه تیم‌های فوتبال هستند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/678461" target="_blank">📅 20:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادارات و بانک‌های کدام استان‌ها چهارشنبه؛ ۱۴ مردادماه تعطیل شدند
؟
🔹
کردستان
🔹
قم
🔹
هرمزگان
🔹
ایلام
🔹
کرمانشاه
🔹
سیستان‌‌و بلوچستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/678460" target="_blank">📅 20:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAIYwb5aftteM5btwuIkxwb32NSJOSfiktwyaH5J4LbcHSDqSfsmfW1JAdfEgz0iZFxWEb3PqEZbeMMqwQ3iJX4hHSmnhpqz2HeO4W63w72IWz8rrkKV1cg2aU5gnIpF0XZUUfyM6b5iVXn00UNoaxZZ2668K1NPKpzmOB2APah7QCZC6f5yrpumb7GT_mMDkIKCWLEdllEb45DhnzNtlhv1hnPZIS0g5gybMyKkdOgL1jTkN5QI8NoaGFBBuhxFTKC0FjXO-Nh1kOygrxZ6OfIE8bo3q10Xq_QaR8itI_nYjVfaMBM9zkkbn7WmqVa4H2tbTxWPJ7YVtaF_exsDIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/678459" target="_blank">📅 20:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678458">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
یک منبع امنیتی به نیویورک تایمز: سامانه‌های پدافند هوایی عراق در امتداد مرز عراق و ایران، از استان دیالی تا استان واسط، مستقر شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/678458" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678457">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9ULhqX-pfROCM4JNjbbA_DbeqbKN6SV9jd50jj7E4lUvMjnGy-tZLBcLp7bfiHRaNmhxZqwvLjs_7tBgmUa9nX0b-7yUczaqyt-fD3inQ_4ZRtY9SXpQxs2OaT1by8Y1SWg4St5vwcAbpkyyKSx3r9zCndp0LvGKooZfeXDwlnDUzrs8z6dtvR5h9da5nV0F19e0WA23WFttrVA4t7x-VKAK4OPpNGPUj5dIjk34hfknfn0k5LL1paG1qhhtCBDUhUnFn31CDDoDYLxI4yhXpbz_UAQaw4x-vERgLSx2vOj52Ltt_3SQU1r2rRdkSTN0Iwn8dpBwMHLUPK7xzagQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقایق شگفت‌انگیز درباره بدن انسان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/678457" target="_blank">📅 19:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678456">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEA05I-GzxUl0T4M8pcxMTp8IxSJ1nnuf-8EWTIGxncPCVUM1JDEwgY4qzI0eaQ3-ZdTxBNL-_ENRzxqaot1RpQy5c6xgWlmhAgUBfafNXOBrBrvgua7f2GaU8Ku9E-pVrZLsnrz3zMs6_A7HZKAH2D_9TYB2zt10vBXWdzdAhFX8iG2L1I35YiYfRvkHDTUpGJwv994DWyQOt9Z-ZsZaXaXLuulI5oBQtdT_fa_1KrOeDFb2H4KW7wjl2oHQcd9VlmXS2ymCusSZ_-sSNcg_cb68gOWUtzg4cMILFAuchDXlOHC6YYynXlTcJh3UsFiwrrabrGGRP7I-1kdZOhPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش قیمت تتر به ۱۸۸ هزارتومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/678456" target="_blank">📅 19:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678453">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e805de888f.mp4?token=FSJIOn3EfO2Wexj0Phhi5dZLPypPeC43I1Tle4MJHBiPDoMRPuniSMAZOhfl2Xod-6hzcrw5XRG0qUnew8QbTfBbC3QFZQZPF2ggNzM4zQuFsLa4-tmGMVdiofOsk4442MNAMO-U5b5eD3na9hpzveQtdnUMp5wrfaw6FJ-9dIQzXvDoUzmaiMmENety0YFt_e6G1aG7rHBmfalA8ypr643eRA_iCp8uMEDRNgda7NtRJAlYXUMirBw6Aao1tZoeMiEkfgY4yYJlna5e3dQpWyKleyuC_VSsCxK_zyO8oP21sBqhZz6L7OIsvxostiwEynnIIP9YNHg1sYQN5mPPEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e805de888f.mp4?token=FSJIOn3EfO2Wexj0Phhi5dZLPypPeC43I1Tle4MJHBiPDoMRPuniSMAZOhfl2Xod-6hzcrw5XRG0qUnew8QbTfBbC3QFZQZPF2ggNzM4zQuFsLa4-tmGMVdiofOsk4442MNAMO-U5b5eD3na9hpzveQtdnUMp5wrfaw6FJ-9dIQzXvDoUzmaiMmENety0YFt_e6G1aG7rHBmfalA8ypr643eRA_iCp8uMEDRNgda7NtRJAlYXUMirBw6Aao1tZoeMiEkfgY4yYJlna5e3dQpWyKleyuC_VSsCxK_zyO8oP21sBqhZz6L7OIsvxostiwEynnIIP9YNHg1sYQN5mPPEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به ساحل تفریحی و  شلوغ روسیه
🔹
در این حمله چندین نفر کشته شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/678453" target="_blank">📅 19:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678450">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fed2c750b.mp4?token=jmAL4sc3F8vklBE7Lx0J9hjwQmcNu6U4pUeGyrQ_2Dpi2FVWMsex9LoXNSHAffUr4LQNRFHcpgH81LnV_fQTd8mfm9lEgy5a4bgIqWbZCA96IQagGznAuDcQvT3OHQzABmQFrGZ43DwH3JnUgMaBF_gf8w0O3YEBDop5MHGSYOpAQw4UHRwCygW6zQ_PgGAIRdYEGmFeqSfaBuBuNgIfYYqXU2QohUo0eS1Ox5jDoBg5hX6SSTsgfAAbee4ff-AcjUqxBh7qCf_LIEKxPhOTNPeKAx49xvjt-_gUISi5_LMnR5lBk-y_Hw5HtKkrVemcIODaO9A6AJ_A4KmjOx6kkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fed2c750b.mp4?token=jmAL4sc3F8vklBE7Lx0J9hjwQmcNu6U4pUeGyrQ_2Dpi2FVWMsex9LoXNSHAffUr4LQNRFHcpgH81LnV_fQTd8mfm9lEgy5a4bgIqWbZCA96IQagGznAuDcQvT3OHQzABmQFrGZ43DwH3JnUgMaBF_gf8w0O3YEBDop5MHGSYOpAQw4UHRwCygW6zQ_PgGAIRdYEGmFeqSfaBuBuNgIfYYqXU2QohUo0eS1Ox5jDoBg5hX6SSTsgfAAbee4ff-AcjUqxBh7qCf_LIEKxPhOTNPeKAx49xvjt-_gUISi5_LMnR5lBk-y_Hw5HtKkrVemcIODaO9A6AJ_A4KmjOx6kkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: تلفن همراه دارید؟ بخشی از اسراییل را با خود حمل می‌کنید!
🔹
گزارش تحقیقی شبکه الجزیره انگلیسی از نفوذ اسراییل در تولید گوشی‌های تلفن همراه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/678450" target="_blank">📅 19:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678449">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/babacb9d91.mp4?token=uos2uhMC_cIZIoLQl5GAn7QQTbSLBD4INFfQ8FhY1SrwsolZVKZMn1Ft29EWozeyx-uBLnRirJ0BHnSBdE0w_wYMoRRhtJiyfpyDBBs-jzkn7sm3f6KeqT8z_CLv6Pws7QWynlFJ2ibPsnNnvLRMfqfA0qlR2OQEwYch-bvTsuq5KDLqF4W4zA6z1FPu1qyPIglHblHxVCzKbU5VdZsTsAvXn7oGjEBNE7ZrPR9M_VQYmbl7nXc9AbCQtXG5gGJ77ofRfrVgXNV9CVh0L8BAFCcKq30d0f1om4CinTcy_PwTHbkRPHBA92GiHWlgG9TemBwzn4Sbzks7KqQcGymoGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/babacb9d91.mp4?token=uos2uhMC_cIZIoLQl5GAn7QQTbSLBD4INFfQ8FhY1SrwsolZVKZMn1Ft29EWozeyx-uBLnRirJ0BHnSBdE0w_wYMoRRhtJiyfpyDBBs-jzkn7sm3f6KeqT8z_CLv6Pws7QWynlFJ2ibPsnNnvLRMfqfA0qlR2OQEwYch-bvTsuq5KDLqF4W4zA6z1FPu1qyPIglHblHxVCzKbU5VdZsTsAvXn7oGjEBNE7ZrPR9M_VQYmbl7nXc9AbCQtXG5gGJ77ofRfrVgXNV9CVh0L8BAFCcKq30d0f1om4CinTcy_PwTHbkRPHBA92GiHWlgG9TemBwzn4Sbzks7KqQcGymoGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای حرم حضرت زینب(س) در روز اربعین حسینی
🖤
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/678449" target="_blank">📅 19:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678448">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np8qrfmLT007qdRm_WNao9sm12UbTekUuFIoD2icGm5lkoDjZQ93GGW8A5q_wSIo-tFiqfuqOoOIKx8-aXLXxPmgxQA4Ri8YlFbl_zSfP_Eyvuo2WsL-kdWGTo25yr5yxtGIe02LRDGew0y5b2EHCP8zVdfwOSJAIqy3Rl8hKh8QigJ_NP6PzJKVxNQIG4IXRnEJ1CaTAtJO6AKzQuYzhsSzvbqD2QhIoIku07MYTQVd4N012BVkgluYvXMeJgfUnZ4vYS6laCzuVlHtlwy1uk1Uvww_o7uIAYIL_tFK3wjpXY9XdvMYkConIGY4zRxYyoiy0oAd-GYjSZNKSuiXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش جورجینا به انتقادها از بدنش
🔹
جورجینا پس از انتقادها از بدنش، درباره تغییرات طبیعی بدن زنان پس از زایمان پست منتشر کرد. آنتونلا، همسر مسی، نیز زیر این پست کامنت گذاشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/678448" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678447">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5b9fc7a6.mp4?token=YLN5ha7EjfiDBHEZhrsNAjDQtgdQ7kD-mi6rj7WoSMW4A3XL_LJYT6vUJdGswXS6lraFOgQCS1Lvz2hnrGWLy2Vxj-xJar3qTAoJycwYORh_PU0GAqaDDeGnRrKKP2FGdfTgT4QmiyW5trd--wfBxxHSF-2tVdiFo6Fg9c1NEY6uFbRJw-iW8YY_fBtCNk1eN5k5Lbo3mIrU4wJqp-rD_5yMpAtc79Q12DBfY6Mpnirt-wc6R3KN0kd5DzYuC8qRrbSYFRbdPC7_QS-TCWjfrEwnX6E520Ddb6G0LxeNhWsn3sLATFJbvrFtLGuIteqkA8l-I0pDB-LKk4KhOoK6PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5b9fc7a6.mp4?token=YLN5ha7EjfiDBHEZhrsNAjDQtgdQ7kD-mi6rj7WoSMW4A3XL_LJYT6vUJdGswXS6lraFOgQCS1Lvz2hnrGWLy2Vxj-xJar3qTAoJycwYORh_PU0GAqaDDeGnRrKKP2FGdfTgT4QmiyW5trd--wfBxxHSF-2tVdiFo6Fg9c1NEY6uFbRJw-iW8YY_fBtCNk1eN5k5Lbo3mIrU4wJqp-rD_5yMpAtc79Q12DBfY6Mpnirt-wc6R3KN0kd5DzYuC8qRrbSYFRbdPC7_QS-TCWjfrEwnX6E520Ddb6G0LxeNhWsn3sLATFJbvrFtLGuIteqkA8l-I0pDB-LKk4KhOoK6PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین پهپادهای بیونیک شبیه پرندگان و حشرات ساخت
🔹
مهندسان چینی پهپادهایی با الهام از شاهین، کبوتر، پروانه و سوسک ساخته‌اند که با بال‌زدن پرواز می‌کنند. مدل شاهین با قابلیت شناسایی و ردیابی اهداف، در آزمایشی ۲۵۶ دقیقه بدون فرود در هوا ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/678447" target="_blank">📅 19:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678446">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
انتشار گفت‌وگوی پزشکیان با مردم عقب افتاد
🔹
با توجه به شلوغی کنداکتور صداوسیما در شب اربعین، پخش قسمت اول مصاحبه رئیس جمهور پزشکیان به فردا شب موکول شد./ دفتر رئیس جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/678446" target="_blank">📅 18:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678443">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeJ179GiawtyP-SqyCoS7_qGDC1Wzv9TsoJrmT7APRiXbPZJQQQ3qqF-MRASV5sfJmnjpwxZIokPG9eXx5kt54NvwoktpeAlkEETL9vmHkrJJW3t1tuIDycvIXS4StwW2WWqB1WsGid3avh4NQX2CS6vd66hO403wl_lD3GbMlKDbiBEYXxmTybLbgbZdp1Fl4r3cbRQL2SLPYwFQwauriGKHl_wD3pedV8LbZ0HInU-qkMbE8t2vooZ1OJQJc-7pH1guu2gBPzWf4WsdJiV1fDwo3lj6vBd2hWNo5lMpIU7FQLE4dl9ubxIkmAtXmCBpt-rWPWQoUIhl6j_q8V-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت ضرغامی درباره آیت الله جنتی: خودت استعفا بده و به نظام خدمت کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/678443" target="_blank">📅 18:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678442">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad9f5dbc5.mp4?token=f2KNr_XsMhn7S39v4yEdE7JpIE3GyOUFYJPd2Z87QD-48Qh0lTLGHnKEvyN1tUaB05mG-islp0WYoyZDyvnxanq4zH6_DR29GE2s6q3tRk4gAnQhlwOtPZKK4gA0fhwBCTcba8b6C53mvedg2y2fJN9qnfXYx_qH7cE7dbVRm9nKXIjhDpRx-QvNpD6rYE0wZxGGVOumuF_lcjZmmCvSryR7nGIjuq8b77TAfAeoLHhFrUkIj366nd8gSZSB84jW7lwjUlTmVvDZkIVvApNYQK60oY6aCVRlUpNcd_qoSYVebpkhT3o4ecqwBEVNlhydug1reIlZ5Db1s8LxdLXC6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad9f5dbc5.mp4?token=f2KNr_XsMhn7S39v4yEdE7JpIE3GyOUFYJPd2Z87QD-48Qh0lTLGHnKEvyN1tUaB05mG-islp0WYoyZDyvnxanq4zH6_DR29GE2s6q3tRk4gAnQhlwOtPZKK4gA0fhwBCTcba8b6C53mvedg2y2fJN9qnfXYx_qH7cE7dbVRm9nKXIjhDpRx-QvNpD6rYE0wZxGGVOumuF_lcjZmmCvSryR7nGIjuq8b77TAfAeoLHhFrUkIj366nd8gSZSB84jW7lwjUlTmVvDZkIVvApNYQK60oY6aCVRlUpNcd_qoSYVebpkhT3o4ecqwBEVNlhydug1reIlZ5Db1s8LxdLXC6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید میوه‌ها رو از زبون خودشون بشنوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/678442" target="_blank">📅 18:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678441">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcEJDwN1hgNJ-OyCWugAZiKSujGMVbQhgrhUguu3vtp7gQODqqUJoPABannUhR4F0gtNPjMSsEoRWCByqfJLUwoXTtMUURpyMsuXyyqIvAEopyWz_vYJVVlm7WB1u61wvzgskesgIkUg-hwCqD2MaiaK1o08mEnFyNrw2PJjKk5UkUhzm11Wqk24X21l0AENySIw30_l0ehbZu9AjF36Ljah6HxVmz1zqcMTTH7v3o97Qx-caDd-kYLaEyETf6DPEh-_N5vnZ5bEvEYQH5Sypoa1vQplP4YBNEniT7M2fIge-yU6boATxXwe2s8nGQncsVyEesDTENuuNYPfmD4ZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پستی در تروث منتشر کرده پیرامون توافق با ایران بر سر تنگه هرمز و برنامه هسته‌ای
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/678441" target="_blank">📅 18:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678440">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
استاندار کربلا: ۲۲ میلیون زائر برای گرامیداشت اربعین امام حسین(ع) در این مراسم حضور یافتند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/678440" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678438">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
روابط‌عمومی دفتر رهبر انقلاب: مطالب خارج از مراجع رسمی فاقد اعتبار است
روابط‌عمومی دفتر رهبر انقلاب:
🔹
اخبار و پیام‌های مرتبط با ایشان تنها از پایگاه اطلاع‌رسانی دفتر رهبر انقلاب و پایگاه حفظ و نشر آثار ایشان معتبر است.
🔹
همچنین ادعای مطرح‌شده درباره واکنش رهبر انقلاب به نامه رئیس‌جمهور را «کذب و خلاف واقع» دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/678438" target="_blank">📅 17:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678432">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T02O7Js5HP69lbOqE-2MLgPEUlkXSTZdTHzvuC0R8shFu73OYZVt3LuSo42EWw1wl-l4TcbnL-3_cmOXvQdPuFzyRce1I-rN6GErvUIwSErL9RcKZTTc2uAgDUFBPHobB9OPEbGB1JMaoD2a2Usec1DD98RzFge_JTeDYzCr8DZsN1tSJNCZ1MIAm4cVBjEz22LjRvO9cqHs3RC_cTKV4bjgF4Ck4bgTHmkmNQebbld2bmQv6WrCVHL-NPS6ZWhAbIIVgGbvGHaykfcZOdHgEcA7rweyH2UCm1uwAy8JZtzpfNuj2etXMThJeTUJ2K_qZYgDxCcHd1AwFW_C6PCQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOYKs1iqjVVzsx9_Vs1NU7Tmi5Dw86sVvRN1T58OUpcxHZgwvQPhqoWLEWwqxNHkZPc_SGbZzIFJ6h0y9edlbSZOPkDPKQWSANO9wPIj6z3nAqY0QSRZ4id4qGZPchGN7m2P_nbh_N5sGmGbTUFC1N_QycTG9akD9FQnAhs820gbO1JQI2Ezraip4CFUH7dnUd-I1ZUaay7SGN9WmLLMpreuAFf2jzexi2jwuiufVezoBIR-Sj89HYohkroNvKABOYxuwYEDSksAsJwa77ut6wVbsM68mlB9Zw3SR7PRNrff6Q7KpLZh63_iXFQ_hl5M3HWJ15HQpwH_HKApTUgcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSx0PKjLURYbQfkTNzBE63RQRTVBF9gSgn2tUvS-yOgAo-mufffyUzdtb53MY7YKbtSoBN9IcEYbiUtrk4v1xuT86mYJuhzAydy9jn50tON2oHw1e8H7A7IhIfauD_shPOxvyubOMLD01pg2BGA8azUq2vX67SmPTGeEeEStXGaJOq91C3EN1VjFGSy5OhGV-el5shmDuo_dQEr_GTWN8z_176Jf7KefKGbA7Py5FhrZIJDde804gzp3PwebsRixilguQIKMa94ktI5_4Td_Ti_9_wmImcDr7N4RGHGQvQNOmJLgOv97oLHZnqYn83uuEU-7imalaLU6vke8OVZ0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQC48IWNWXNUUg42EprH2UemYdhcXB7MArHZ4cTcSeNVpIexofoXQwY51yZh8qoKHsVHl29Z03lweVadMzNTn2VYfY0uY5R9pQaKjKfmOCiJZr9vuw9XCWhO_gVY6W-mVpbNIBICweZ6OCtqbKXCWiSVEQWS2ninD4nJ_F8N23N-9Va96b5pDr53IjzrxulwFdEOBUguHuA3vV2ok8EUFNnZecx1rSRrMC7j6rg0xlszoY4m3cDV8PRcPcV7cg67Ph4hanye4gBt_Y7AbcbX7hWZWOAq3AdS93h7CUZqqgQP3AgsEIt4wy3xL-iZO_h0dC2oaAWEClH5bITi1YKcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSjJGmzvu9XgbrqVfQx9_pU9hmM4dqCjOzppRt0mSPgO91-cEGGSfCCNG8h1pePfCOa5kS-4h35wTiSU2Kejpziuq8rKjtOnaA8Kgl0H87frjPOzjLbht7eMqgQqvjtceETjv2YALTVCzv6q5BdS9InMBC7x0ZDG7qSauuXxLW0QxjeUKYe76i3guVa7RQOIgPXLQyPuxCDnSC7WmOSmubBb11XQoCTEGm_p8ho4HvYgEmbO2R7axUIIMErKedM-RuPKz_DOo4iKnK0Ogt436vbI48s6cVnX77pQje9AVqowEpUU7Ffb1CkorjFKfOev5KwPsfU1GN27uIWI0nEEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6tlf7gTgmJcymlLWDqI8Kduwm9yaPsEnb-aw0OLwu4Bc0MtLyuxCY3ziCrkrOfCDxYhGDLmMZ6EjeF-H2f8eTGhlmHSErvc96qX2J63zpE8XZe8gcy4gYR1aTQFXPDzu-0LgP4IzNtW1CQKvZNZX6De82rHX7ae_iWG08XcYaYmMsKlhsmA69gIyHsJo4RRZoHn4_rAOeDOQTFT8zaG1FOBq6y2FwXmtWEID_uaPsY-_GBG5dOUqEGhQOBwcPfhMjzyKBSeS46jL3qADKNY1ZqjDs1Bbw77H7KxUkOuiiltljhJQMrxuUroNYTVhsytuatEWdbsGCiGhyBSkGreig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
«زیــــارت اربــــعــــیــــن»
▪️
حضرت امام حسن عسكرى عليه‌السلام می‌فرمایند: علامات مؤمن پنج چيز است؛
▪️
اول، در هر شبانه‌روز پنجاه و يک ركعت نماز گزاشتن (هفده ركعت فريضه و سى و چهار ركعت نافله)؛
دوم، زيارت اربعين كردن؛
سوم؛ انگشتر در دست راست كردن؛
چهره، جبين را در سجده بر خاک گذاشتن
و پنجم، «بِسۡمِ ٱللَّهِ ٱلرَّحۡمَـٰنِ ٱلرَّحِیمِ» را بلند گفتن!
@Heyate_gharar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/678432" target="_blank">📅 17:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678430">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای وزیرخارجه امریکا: امیدواری وجود دارد که در آینده‌ای نزدیک توافقی درباره تنگه هرمز حاصل شود
🔹
پیشرفت‌هایی در مذاکرات با ایران برای بازگشایی تنگه هرمز حاصل شد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/678430" target="_blank">📅 17:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678429">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای قطر: متن توافق احتمالی ایران و آمریکا تدوین شده است
سخنگوی وزارت خارجه قطر:
🔹
متن توافق احتمالی میان ایران و آمریکا تدوین و میان طرف‌ها در حال تبادل است؛ میانجی‌ها به دنبال راه‌حلی کوتاه‌مدت برای بازگشت تهران و واشنگتن به میز مذاکره هستند، اما فعلاً برنامه‌ای برای مذاکرات مستقیم وجود ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/678429" target="_blank">📅 17:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678428">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f565286a.mp4?token=HsA19i1g60BiC1R436Mnil3G19VhQ0j6cviX4o6lVqHyjkX3Dt8Z9j5UHPBmYdCT_SjyBnZcndY0dkypob0dK6Q1WT8GZglO3JVTtRBRAPqMe7f36EC6yo0Ja7rRkej0MWVzn3WfHbKBHeDmfn2WKxlAla3v-qQzoBb24KImBsvk9pRkgcgGLcCtXXzBnR_jcuDP4zQaC9xHBupEIrjXMQ3aNoxYiD314iL4yoNjdOoxWzVm1Wi7e0HL88N4vTrD3xcv2PHfF_6_v6zlKxAuz15OH8IcUwCwwGg7rMflfHSl7S3dmI08_qGufzndIaiokBeEbl8tx3npXqbbUnapjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f565286a.mp4?token=HsA19i1g60BiC1R436Mnil3G19VhQ0j6cviX4o6lVqHyjkX3Dt8Z9j5UHPBmYdCT_SjyBnZcndY0dkypob0dK6Q1WT8GZglO3JVTtRBRAPqMe7f36EC6yo0Ja7rRkej0MWVzn3WfHbKBHeDmfn2WKxlAla3v-qQzoBb24KImBsvk9pRkgcgGLcCtXXzBnR_jcuDP4zQaC9xHBupEIrjXMQ3aNoxYiD314iL4yoNjdOoxWzVm1Wi7e0HL88N4vTrD3xcv2PHfF_6_v6zlKxAuz15OH8IcUwCwwGg7rMflfHSl7S3dmI08_qGufzndIaiokBeEbl8tx3npXqbbUnapjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر بستنی اینجوری درست کنین، قطعأ با بستنی دبل چاکلت بیرون خداحافظی می‌کنید
👌
😋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/678428" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678426">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما بزرگ‌ترین مانع جوانان برای ورود به بازار کار چیست؟</h4>
<ul>
<li>✓ کمبود فرصت شغلی</li>
<li>✓ متناسب نبودن شغل با توانایی افراد</li>
<li>✓ عدم تناسب آموزش با بازار</li>
<li>✓ شرط داشتن سابقه کار</li>
<li>✓ سایر دلایل</li>
</ul>
</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/678426" target="_blank">📅 17:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678425">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای الحدث: به گفته یک منبع، اعلام ترتیبات بازگشایی کامل تنگه هرمز ممکن است ظرف چند ساعت آینده یا فردا انجام شود/ انتخاب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/678425" target="_blank">📅 17:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678424">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79f74b13f.mp4?token=ATgSUIAsc1mDITfJFIEAUtSOSFGSFQn4PsOvXrnSdiGrqb_vMJCVCBFpuht9hgUgIxDQHSrbSksRrdxoYiZWbZGlk6Gn1pWGnflvNhzIw0_ep67yd9-D1N91eVmFdTNFKuYdd3JsIWXRzd6NR7Nj9EQny8ohODY1oyltLX0JitAr3QHyuJLzMRuXVRgud81FV_xRNN5h1Mo22KAQ4Sjp28qU5jBNS4o1f5X5jah1nSm0AMmN2UUAC_jf6-tEl0nMZua4WtmyV8lAaaEvHsldzZNs1mxhshK9Nh0uP_cYRiuk9EJQM69VFDxpQ04T7mqx3dhwWwYFJfBXL0H6KqVCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79f74b13f.mp4?token=ATgSUIAsc1mDITfJFIEAUtSOSFGSFQn4PsOvXrnSdiGrqb_vMJCVCBFpuht9hgUgIxDQHSrbSksRrdxoYiZWbZGlk6Gn1pWGnflvNhzIw0_ep67yd9-D1N91eVmFdTNFKuYdd3JsIWXRzd6NR7Nj9EQny8ohODY1oyltLX0JitAr3QHyuJLzMRuXVRgud81FV_xRNN5h1Mo22KAQ4Sjp28qU5jBNS4o1f5X5jah1nSm0AMmN2UUAC_jf6-tEl0nMZua4WtmyV8lAaaEvHsldzZNs1mxhshK9Nh0uP_cYRiuk9EJQM69VFDxpQ04T7mqx3dhwWwYFJfBXL0H6KqVCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی در میامی کسی مزاحم مسی نمی‌شود
🔹
لیونل مسی در میامی می‌تواند همراه فرزندانش بدون مزاحمت به خرید برود؛ موضوعی که باعث شده برخی این شهر را به‌دلیل برخورد عادی مردم با او، انتخاب مناسبی برای زندگی بدانند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/678424" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678423">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUzyWY5BPBeBWsN2CCsSInUNpf8WrSmm6CJReosb1y8n4_aOA0Kw2aTEl3zkVz22vR80GFxCeI1TtSZBR0igNzS9ux4xV-72IwA6FsG9q9vk74uhQHykZW6OM30f-XP1zILiVsj7EVJ_G_RVKL9C-yovhysarYrClJwzBmB4Ei8-mT_paO-d51CuDztjqoHTTiLSnwHqqw9sOMFjL6R6-tNyIswjBVKBrW9zbEFUmgB9b9NMw6oQ4dxkpyekr06H2OpaIrlRVcceMJ2bPT9fHq3rYtlqAftlfl7fdFSho0JJcx1C1Qb8Mwko1ciHcnCUeZ9xjyUwYwS0PwxwBfhs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر وایرال شده از قرآنِ منسوب به دست‌خطِ مبارکِ امام حسین (ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/678423" target="_blank">📅 17:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678422">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای الحدث: به گفته یک منبع، اعلام ترتیبات بازگشایی کامل تنگه هرمز ممکن است ظرف چند ساعت آینده یا فردا انجام شود/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/678422" target="_blank">📅 16:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678421">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFqXXItJtgD7BRsM6hzzF1FBaI3hUJvbwfiIanXJa_3ynQlYn8YdjLSZ-CpMNskO_2Csf2P2_v5abwD0pWB91UHG09LvrdfOF7XbwVmZ1JCLgPMz8uDabZb5Io-BZLNA8cC5vS6PPrrA91HWSq1kEyfjMWZ9vE8ROnutmb7VJhco43Fn_c9haAPCMwo6u4otW_lvgDSDy93X-JRFWHWT3KY-yO1MXQadZ5OYO1Wx4nQlGf1-OXOMcyWmHOxCT34p3ftPL4hQktuLwEELu3d1xIy7X972W7JpnuSXeJJ_d-lWEPIvlmAmqKzFz_2ZzlnGLMvccd1gEF160aKOW97m2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: مسیر بازگشایی تنگه هرمز با ابتکار ایران در حال پیشروی است
ادعای پاتریک وینتور، دبیر دیپلماسی گاردین:
🔹
عمان تحت فشار آمریکا، اروپا و عربستان در حال پذیرش طرحی برای بازگشایی تنگه هرمز است که بر اساس آن، ایران همچنان کنترل غالب بر مسیر عبور کشتی‌ها خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/678421" target="_blank">📅 16:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678420">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfedd1510f.mp4?token=IF_yo8GI_rg3egVm4Yb-Etwd8DtMVPIA73u_dH33a8Lg2aGNG5FKSB2yvY8C4BQmE3ao3wcwmJa9Xb8D1KT6FgdOew15fpMN-w_-1Py4b8r9-439jzsk6N0j1kav7TMXatqLH1YADzu-NqEf-cRAi-sKqnQ-jESMKXV66DrZlyrJiAah4OgLeg8k5JrMdZe2uD7nQ5kXeNshrISZI1eaHpICiLMo0Obbv_SvcZUS9YHhMI0cayzka568Vd1LRAdNm5J13n65mzIBrCwnsFayy-qfygwozEavIk_R3gm2b0DFUnmzqz_rlwV7EQtg7DelZp08MwtiOtyFkm896-4Mgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfedd1510f.mp4?token=IF_yo8GI_rg3egVm4Yb-Etwd8DtMVPIA73u_dH33a8Lg2aGNG5FKSB2yvY8C4BQmE3ao3wcwmJa9Xb8D1KT6FgdOew15fpMN-w_-1Py4b8r9-439jzsk6N0j1kav7TMXatqLH1YADzu-NqEf-cRAi-sKqnQ-jESMKXV66DrZlyrJiAah4OgLeg8k5JrMdZe2uD7nQ5kXeNshrISZI1eaHpICiLMo0Obbv_SvcZUS9YHhMI0cayzka568Vd1LRAdNm5J13n65mzIBrCwnsFayy-qfygwozEavIk_R3gm2b0DFUnmzqz_rlwV7EQtg7DelZp08MwtiOtyFkm896-4Mgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیلگر اسکای‌نیوز: ایران در مسیر تبدیل شدن به قدرت برتر منطقه است
شان بل، تحلیلگر نظامی اسکای‌نیوز:
🔹
ایران با تداوم مسیر کنونی می‌تواند به قدرت برتر منطقه تبدیل شود و از نگاه راهبردی، کافی است بیش از آمریکا دوام بیاورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/678420" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678419">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ویکم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم معصومه فیضیان که با درد ناگهانی در قلب، روح از جسم جدا شده و خود را در میان گودال‌هایی از آتش و انسان‌هایی در عذاب دیده، اما با صدا زدن نام اهل بیت از این قسمت عبور کرده و با شنیدن صدای اذان در نماز جماعت با پیشوایی حضرت علی (ع) حضور یافته و در نهایت در صف حسابرسی قرار می‌گیرد و اجازه بازگشت به او داده نمی‌شود، اما ایشان با التماس و سجده به درگاه خداوند بخاطر داشتن فرزند شیرخواره، اذن برگشت خود را می گیرد؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: معصومه فیضیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/678419" target="_blank">📅 16:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678417">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE_J01-445Sbz1njMCvjg4Jw48J8tPpJZuN_RLmZ6uJWCMLcNkKVGRkee0jzgtND9n_RZXLSewNJ9oDc1BPXqNPRFzNR3A_7GkQvLugSd5uG4dx94TVR85BpSgTDDOI0MDWanKacXifV0NqW9_D78JFuosLJUGisxDd2xghDdDVR9WqYVxVqNC4-tbLc3Mln19TRxIV7-C6lenfBGt6pVvYqktZtE8FM5AoUpvc-ZTET1p1FsnAH-ao7aCwdcFsFcKIMCSxL9a5XimQNQjnTJ87Iy8Y_TtfVbs20iIbrfTYNjablnv3DePWCel8-hwuuzfRbHJu1XDFQY6H6pjKyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: صدام حسین ۲ قطعنامه سازمان ملل را زیر پا گذاشت و آمریکا او را اعدام کرد
🔹
نتانیاهو ۷۷ قطعنامه سازمان ملل را زیر پا گذاشت و هنوز زنده است. عجیب نیست؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/678417" target="_blank">📅 16:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678416">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcVFabQc4roTInqxzqYLNOx_goIaIzykwi3QjM95OP-2vz-rx8Yqb2anvVaWLWsk4S4szTZ9_7SOCrttLMpDUlbtP3XulQXiFy72GD1qdvKoNxMiJ6TPxOwz_rRQUa24LdCcTnPhzfC4yKUj2MlWPfbBES0qDdKAnO-E-6otvlMOehIL0eKaM43PfYJWWjB28-2e1Ias62MpH_rVKJ1aqC_swtZe6uznxcft3dEzPltRsSEtPWPnBJ_DVzKKuj6jtxfeQlxwYOEA3G9RG-MYC9nMu_gpvVpBx7BNcec3dft9Roe8cp6PLubs5lMa-RqHQiqogo1kOko3N_jVHvATKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگترین پیاده‌روی زیارتی جهان مربوط به کدام ادیان است؟
🔹
بزرگ‌ترین پیاده‌روی زیارتی جهان مربوط به آیین هندو است که هر ۳ سال یک‌بار با بیش از ۱۲۰ میلیون نفر در مراسم کومب میلا تا رودخانه گنگ انجام می‌شود.
🔹
زیارت اربعین، بزرگ‌ترین پیاده‌روی سالانه جهان است که بین ۲۰ تا ۳۰ میلیون مسلمان تا حرم امام حسین(ع) پیاده‌روی می‌کنند.
🔹
پیاده‌روی زیارتی تنها مختص اسلام نیست و در ادیان مختلف مانند مسیحیت، اسلام، هندو و بودا وجود دارد.
برای آگاهی از جزئیات بیشتر بزرگترین پیاده‌روی‌های زیارتی جهان، یادداشت زیر را از دست ندهید:
🔺
[
لینک یادداشت
](
https://B2n.ir/dz7708
)
🔻
@amarfact</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/678416" target="_blank">📅 16:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678414">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55efd5d312.mp4?token=mnTpmM9d9PRdOoehOQPt24fMx6MSjK3SgIud-kO233uSn5DcG9ixHialdfHKpMcqkvYAAw8ozNmzZyRnlDVdlGbiSKVMUSt2fBZ09LS3QhAU1MtUepLpIIjJ7DDRPlSmPYhkN-eRdL5ZS6iBIhKjJC-3V7HFwCjwfleoVoDv465G7nzCaWebWFhocvbk4E2Ot8r0-kS3jO5kXacVidhIFtRoloQMBnsDvN6ezkIT1O24rusKbGkMMRVm4AEL6XpLC38j-X98FMfvvxx9etIcnDlLVRPkL1MnF57cKN7k6b9rXlaZW1fzlk5UyvupGF9-fBv5cDQzq-DQmP3zZr7cGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55efd5d312.mp4?token=mnTpmM9d9PRdOoehOQPt24fMx6MSjK3SgIud-kO233uSn5DcG9ixHialdfHKpMcqkvYAAw8ozNmzZyRnlDVdlGbiSKVMUSt2fBZ09LS3QhAU1MtUepLpIIjJ7DDRPlSmPYhkN-eRdL5ZS6iBIhKjJC-3V7HFwCjwfleoVoDv465G7nzCaWebWFhocvbk4E2Ot8r0-kS3jO5kXacVidhIFtRoloQMBnsDvN6ezkIT1O24rusKbGkMMRVm4AEL6XpLC38j-X98FMfvvxx9etIcnDlLVRPkL1MnF57cKN7k6b9rXlaZW1fzlk5UyvupGF9-fBv5cDQzq-DQmP3zZr7cGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون: جنگ ایران پایان دوره اثرگذاری آمریکا بود
🔹
جنگ ایران قابل پیروزی نبود و به پایان دوره اثرگذاری آمریکا بر تحولات جهان منجر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/678414" target="_blank">📅 16:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678411">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@shervamusiqiirani-12</div>
  <div class="tg-doc-extra">آرامگه یار 2</div>
</div>
<a href="https://t.me/akhbarefori/678411" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
سرم خاک کف پای حسین است
دلم مجنون صحرای حسین است
بهشت ارزانی خوبان عالم
بهشت من تماشای حسین است
استاد  کریمخانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/678411" target="_blank">📅 16:08 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
