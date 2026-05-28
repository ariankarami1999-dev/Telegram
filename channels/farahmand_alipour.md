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
<img src="https://cdn4.telesco.pe/file/Dw1AilgJ_FRxENPIlB6tVWroH28sAouOItMFS3iYOqXJvQy63Nz04bxQLTw6Wceif1q36LCnvqU_A1rGYDKVqsf5D5vB8hDrpBrYgVFlOxpYC_tvlhsc0c_CoEvh9olg5WvX6DRoCDvOD6GPPRFlkiinXnPz2TXK-hc0fagi6n63JKfdVDiiVtRLEEdrCjQan6JBa_sPyAFFqJZohq2-6rrkcH0ckR5W5nhWAFnqOcQgU48kmdq6YZ05jylW8P0Nzf-z7DcQoYVkkq54JDsduY5uh_MUyD6OZjI1SmiXuW7Ra5_zQP6neqJewkL-yfBepjjp9VD_fWBOWGELQKLd8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 23:51:25</div>
<hr>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=A-wg9iGdavXIKXH-GzzucsFrjgg06Jjpx8mBzToC_oL4F3V01tkNXNWl9dnLwgJoXXA6ChLvj6fLqf5n5ll47EclryC61O6m0hCBcIB8hvAl4r8lQ_stEmIvLQONvudJGzBxKUlacArDGDcpcKS5-3R63_Gr6gBFibEQYi1VBU5vJgWDf5WCCvoXAFklod9qc6blzwxU34_dN2q4nKfbHuDwn0MCjr-RRN6rFoNh9bPxDpfqbbe6s3cwYhbXpPJrJOpugK96QxkU7ACGmeUi4iI0Txnk18VV9mYlIQmbngwWSC_zD36HZpyHO__aWOzwbe671lDv7DPP4DIm_vTzZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=A-wg9iGdavXIKXH-GzzucsFrjgg06Jjpx8mBzToC_oL4F3V01tkNXNWl9dnLwgJoXXA6ChLvj6fLqf5n5ll47EclryC61O6m0hCBcIB8hvAl4r8lQ_stEmIvLQONvudJGzBxKUlacArDGDcpcKS5-3R63_Gr6gBFibEQYi1VBU5vJgWDf5WCCvoXAFklod9qc6blzwxU34_dN2q4nKfbHuDwn0MCjr-RRN6rFoNh9bPxDpfqbbe6s3cwYhbXpPJrJOpugK96QxkU7ACGmeUi4iI0Txnk18VV9mYlIQmbngwWSC_zD36HZpyHO__aWOzwbe671lDv7DPP4DIm_vTzZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=YoRJfa8-hh6enTJNW6Fpl9pzZtq_eLNTGXM7DM6KU3SEjM3W6M0XsFxfa0KO9a_b5jl-gMoydEPzffjhkiDd5eTmN0GGocrv1hUJCF5T-4CUDDteDn_0e4Co0Cdq5lPN1n8NAf0C1wDxgeluFYjTKCq9f7OsDuxrRcxeQxVQmLGEJiWLoOkJjCdVoXyqZ_T7lvK_VzuPVtaGLeX_0H57nyXAip_SH67bGqiM4xowtP0H3wjlkDEgBMz9i35dsIOdObWyB95JPlBo-f4m4IfT-_WPriMWAj8FA0TIaf6rNeapAHgMfx7MEk0KGCoN5AJHJU8_pa8VitJ6XG__B_ynIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=YoRJfa8-hh6enTJNW6Fpl9pzZtq_eLNTGXM7DM6KU3SEjM3W6M0XsFxfa0KO9a_b5jl-gMoydEPzffjhkiDd5eTmN0GGocrv1hUJCF5T-4CUDDteDn_0e4Co0Cdq5lPN1n8NAf0C1wDxgeluFYjTKCq9f7OsDuxrRcxeQxVQmLGEJiWLoOkJjCdVoXyqZ_T7lvK_VzuPVtaGLeX_0H57nyXAip_SH67bGqiM4xowtP0H3wjlkDEgBMz9i35dsIOdObWyB95JPlBo-f4m4IfT-_WPriMWAj8FA0TIaf6rNeapAHgMfx7MEk0KGCoN5AJHJU8_pa8VitJ6XG__B_ynIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=vGy21I5eWikfRf7Cexx_1tzN_1pLESg7P4gb3hTPuDvSAhmdsvODwrMy0RraXQG581daWIc0Vv-3OlhDJ3_SOVbO35a7lZF0MW-rST8w3v-A2j3zERCIqx-U5l_6qRv0uWObuIXuwhwzfW-HH5jtCpqYfFnSQq8TvkLxiWMs4QDnHbhg7oWjNSf_GA1nLU2xb1RKyRTFpy_PrhadUl0iZFm3ITNZHqS7_yji4F4fbhthKUdijHDWf-0qRk8xZcb5FDNwUNSoxTxbn-oZMKii5263QvnEJmRP5dTubl_80hta6FLeetLrny5TRhYtTuC-ooQIUQzg8KXN542L4JS7PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=vGy21I5eWikfRf7Cexx_1tzN_1pLESg7P4gb3hTPuDvSAhmdsvODwrMy0RraXQG581daWIc0Vv-3OlhDJ3_SOVbO35a7lZF0MW-rST8w3v-A2j3zERCIqx-U5l_6qRv0uWObuIXuwhwzfW-HH5jtCpqYfFnSQq8TvkLxiWMs4QDnHbhg7oWjNSf_GA1nLU2xb1RKyRTFpy_PrhadUl0iZFm3ITNZHqS7_yji4F4fbhthKUdijHDWf-0qRk8xZcb5FDNwUNSoxTxbn-oZMKii5263QvnEJmRP5dTubl_80hta6FLeetLrny5TRhYtTuC-ooQIUQzg8KXN542L4JS7PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Y0nxJqA_NlJ1R3Ob-O2hqy9G6GITVzImM2R76mRjkrJMl9BFohc-Nps8H6tRE4Nn83lGxG5nRO4hyOiefZ0ZGgZaN2VGdJkQKCubx8ChLttI5AQeeokS8SMtHfNJhIj6yqqhvRW2p_NBKbaFMn54mSRbxUbBnEdY2WsvzJ3_9u27vHLHxIoC0vtfFG-ryID5IdkQD0fdcwH-kJza8DhXH-nk5KHB1YWe6wtbSnkQs-Uxh6wLPX5KHPtst03w9ypxSQl71QE5e4lfR28gztcGF7iRzxqavrUrk096N888S6wPLQE4e1qSULjK3JvSWNeducYu_hJdFCdvaINGPiXbHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Y0nxJqA_NlJ1R3Ob-O2hqy9G6GITVzImM2R76mRjkrJMl9BFohc-Nps8H6tRE4Nn83lGxG5nRO4hyOiefZ0ZGgZaN2VGdJkQKCubx8ChLttI5AQeeokS8SMtHfNJhIj6yqqhvRW2p_NBKbaFMn54mSRbxUbBnEdY2WsvzJ3_9u27vHLHxIoC0vtfFG-ryID5IdkQD0fdcwH-kJza8DhXH-nk5KHB1YWe6wtbSnkQs-Uxh6wLPX5KHPtst03w9ypxSQl71QE5e4lfR28gztcGF7iRzxqavrUrk096N888S6wPLQE4e1qSULjK3JvSWNeducYu_hJdFCdvaINGPiXbHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=aOrt1PPpCDGvER47f29w4hAOf4Ltz933NnDIBRm8YPMXWv4pAlOWBWPcVDKct3hbNAlV-qx7tiydAZ7s2Sm9iQHkrerIZrLg-T7JQybiZtMaDz2dVqh_T6iHhS1c3mO4zdHXv1Wo-3EU6ugU5ilI7njySdiGLcOcY8eOUvziAuAqtGNrTgwVwfQ_AQbdFKV-1iPUi7jGs1hh53oiZDMTZcx8Fm69ZUC1Fr81osOX5HoBGIclCc_0WLeeadgKgLBuACJib_6YO1A4zeOhN58ttHvByYvcCg6IEGe7kqz3h1h_eQCPtj32w2opyn3_8__qcECDpcRdWRc5h1_yA2Pcnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=aOrt1PPpCDGvER47f29w4hAOf4Ltz933NnDIBRm8YPMXWv4pAlOWBWPcVDKct3hbNAlV-qx7tiydAZ7s2Sm9iQHkrerIZrLg-T7JQybiZtMaDz2dVqh_T6iHhS1c3mO4zdHXv1Wo-3EU6ugU5ilI7njySdiGLcOcY8eOUvziAuAqtGNrTgwVwfQ_AQbdFKV-1iPUi7jGs1hh53oiZDMTZcx8Fm69ZUC1Fr81osOX5HoBGIclCc_0WLeeadgKgLBuACJib_6YO1A4zeOhN58ttHvByYvcCg6IEGe7kqz3h1h_eQCPtj32w2opyn3_8__qcECDpcRdWRc5h1_yA2Pcnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edbt87X-xpZjrPqv2Rcm23gD39bSlkA0hUDky6JxRlwfDQvcInzBhm5lzKTmzR9loh9ExVethoIwZzcdeltJIef6MlG78i3xo7oAw-YCKhJEzvvk1K7i0Y9xDvI-Tiyd6vbZBfhqBtStOT_2L3faYks1D6qrL3TK-hOKbChwFqlmrbqyYVn6cR0w2JSZ59nGBXl24DS9QHsGbddtH17UGXVdaJaGNhmMmCTz6zoHrqT_LE7tgtpAa0cx_DNs54q2KKE37vKOsrdRPud2GRvzGiyUaHDzo3lp3OyF22ptyHCaJ3k3kA78sKDQXci7o26d_6_XeKnoLEwaAs6R7xhnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Kamsb2-u7jEVPLxiN2ZXRjgHqbC_p6Vr4D9PYsgrmq84Z-BQ4mxZRbdnDxVfAlw_jm8-MDXwwKB9zSgxLAkGEkDZOsN7UMTuPpgt0y3rKnPVV_otiwF7SNmN-ZRgaBc3Y8ZPZ6dCguBWoyM7nhJZnv7JYT5vvpLoI360TFS-kzOugG8DuruPT3SmjBBTjqDGQEEpZZsIDe4xVpxRKXXLSUyVfDQf1KUtFHFChe9eskswFW51_HXhrxEFiOA4Qy9UtxG_47xoFJ7q4SfGomUZQXdYbsDyVdx-ixnBCpcHhcMnyZahFmhcN84-HSe2TbwMMN5QCAta9V6x312JKmYQ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Kamsb2-u7jEVPLxiN2ZXRjgHqbC_p6Vr4D9PYsgrmq84Z-BQ4mxZRbdnDxVfAlw_jm8-MDXwwKB9zSgxLAkGEkDZOsN7UMTuPpgt0y3rKnPVV_otiwF7SNmN-ZRgaBc3Y8ZPZ6dCguBWoyM7nhJZnv7JYT5vvpLoI360TFS-kzOugG8DuruPT3SmjBBTjqDGQEEpZZsIDe4xVpxRKXXLSUyVfDQf1KUtFHFChe9eskswFW51_HXhrxEFiOA4Qy9UtxG_47xoFJ7q4SfGomUZQXdYbsDyVdx-ixnBCpcHhcMnyZahFmhcN84-HSe2TbwMMN5QCAta9V6x312JKmYQ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMeB-HsSjq2YMMHj5WyeZ6XnGy7ZmrVuSAOhAM4FBXmvPJ31JMCmlFSo_g-xT84MunDxCSgvEi0Xap3R8kzA1GscHwstWvFVfvFgdrp0tgI04lYEakY9Hyx78YJPAYOMAtRKl6740QQPJIbCHi_3D6-INOrirnBbbikTBWOW7Ygu2jqD8uVCp_tvljvTIAXdzYjpDjhgQp4GPvpKkx6d9PA5tdSRMb34ORI9dSHZWiu6e2aFEOElHp9tyON6o3YdabSABBgZNIbOFa2r0GRWTmD-NoUpWekg3GRcHIOGcZ9LYo_kBLuaNJadHtOVjSHSr5Ozh6ytlBufI3SM-gNK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=j4zXSEvR05j0TPU7puX0Vh9G_hHEgehH_HrluI4sCIgo6YynJhmQzYDbH57mUN4FaymZu4OrXNIjFh1rCDLMxYCefmZRSRg2LNQY-HcGarcgRYLJNp-RiEkeb9q4AN5NT05vNlT4bAlk5I2mghbPqZqpD_6vCyfOY-hVZWBmK5736xALM1zwiKj8mtRtzVgUr9yaA6w_r7V3csVbSHt0yiobVGRK5o5KJr8e8tjCkyLq6Sv_O2hWUM9hedHzYs-H7wj0ZNUHmLzAT3M8-BoOxU2SbZWnzz1zY96BYcfJ42BHSiCQwo3yv1Vwi8miyyhQddfdQLTGpPfFg3mPuK8XFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=j4zXSEvR05j0TPU7puX0Vh9G_hHEgehH_HrluI4sCIgo6YynJhmQzYDbH57mUN4FaymZu4OrXNIjFh1rCDLMxYCefmZRSRg2LNQY-HcGarcgRYLJNp-RiEkeb9q4AN5NT05vNlT4bAlk5I2mghbPqZqpD_6vCyfOY-hVZWBmK5736xALM1zwiKj8mtRtzVgUr9yaA6w_r7V3csVbSHt0yiobVGRK5o5KJr8e8tjCkyLq6Sv_O2hWUM9hedHzYs-H7wj0ZNUHmLzAT3M8-BoOxU2SbZWnzz1zY96BYcfJ42BHSiCQwo3yv1Vwi8miyyhQddfdQLTGpPfFg3mPuK8XFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkJ8CHRFBAWvEd2TAQAYZNpShabxRdJcaVbVVKakRuLNuHK2DedtIWLLwmYCixnkjt4-jSUWhFY2j9vPWKqWrK5Pvy46abVT16XsIYLcftttkK9SVPywPUeWvYSxvqatp8PmsXt6BDnj3mZIOe7iDjS0onR30hQ_0HAgDS2DHkoFI2JwWhUcvbPI6Q11MP2A9aUbWERdSbwd6P_m-h_nofwmtf8OA_rBFy-zIB_5YaRTOQO1NRkzogoCQ_Atc9CFk9RU5hbvZaPFYcwOVYJ2XdCypTFmLHRzXaaQuZYbnHDUSLvVSt0Ge5GwK1epHs-08HWUw690B0tBmBBkK7K5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTX7abO_HBWQHB5OHCn8fQ0fVF5Qt47vGKBs4RZ-ymc9Xv0K0QuIbbghgvxfHtzGWNJuRXDgQ3AFpJ_uZVZMndKziOMAWkDrw6vEBI83EWi9vH0nPHW5V2lhwLkbB82jiV0SZKtiw-R7ycJCQRGKa2Y1qFfJHmh7oFsqvks_oAwQE-U8LcZRohEvA32P6e_79MdC48q0pVHlklseHPmR6qN-anF14e5SCY9kmxxE2hUsjNcaLUbta1w4JWIcjw2LrPWombTlfStTNIndvcpF5_Ce2ZDzAA1eozhEg51-9exRYnkrkmWC-SbC4eLXDQY28whBgv0FcbmdkOhb-0ukWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8omnbdlXorNlxVYpRAuo6P7rfCZcbQPZEHGoSaLRJyF2ozz9KVqz81ERap1vzQBCNbgalcoj-SExDRR5549WKas3P4RArERIjYTC_u_DFcyu8jZDGyZOPtiuKDuDzzO0JyJrqPHIAGO7nrog8ak614KlurVqZV7fNgfPR__MlYjCdxMe-LoP4U1Gv-3q4HanIe0LbLsBnHtcw82KMIDop7Y2qgGiFBIicGrjWyJjSEZCVsqGiheHY5WQRvd4BTFlBE7g_RzkKIlCBawDF4FlXGbxToD6oXfW5n3t-I9IamhRrhRQw8RtM8EufMYhg8s1aMOkRPn2dqYFypSidPIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijEOeEETvZ-GNeuJElr77oI-Lwvk3-SY9nS83vxHkdCfr2BRgTQudXsrfPxneQhZwvKyROyidOnBgdyZ1n4FmC8k7rUK-jceWdiASxp5rq_MQa6BvwZIrezlZnPVJmjDuUgffd8QJOBrEL13k0d2OmPibQEOIK5kYWcpe0Qmj6TTFpZt5Rh_gFr18ZCByLffJ_O1KuMPvycWm0OmO0ayLdKjI3s8xf0yJCwE6uvESsy_43fHu0Zad72LQlgsZGFggPMOa-4A_2L8Q1-DOPi8yQSpX24_7yWf8bc501UKCh9UZy9DgkyT7COxgiYvj99Hcep8WvZ-IUMXa_UUeUyU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vknurSUj5MKClQsp4e9AqoBwUsqXu8sqRxI85EzmfpvHX0nkezi34cfC99d7CUYTRCL2nhK9xgmnSedZI6qPPqqbBUDfOBthbiHKjLlW2Kf-HjLXVTughig2xolNUhOiB2riv1H2jcmGRWg7sy_sFDC4exoPFmlpEz3IlCgpcYMk9ZAhEUBHb3DlJoV2W5YPC19FyvURheZy3rp3q8c2RJDBHzd7jPw6KBrVkx_bEL430DHCXg3pnd03thWphZo6qyDG3yZ6SBCPi-42sS6J8cfOFGTAgv_hn2AmlGh7EB6Rz_srLI2JMVwwhjbe8UqwpcM7djQvbde5Oh1nAjM1BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIDPvvCBsjwjzytJq0K8TavZNpU8bC1pt0knmRzaJGx7dng290phOpqudGh8jeYaNsrY8qqjdBQGTNjott-pzjtcOJt2a4zJN1M8zZCTnrja3992PgC04oqkVZJ8XDqihSzAurqnfetKG_asgPPIn1v8b9ZxYr-DefXv7LZGtr4z9Kr_E5hLB7TtvYkqURaKSOn1Ye4Alf4ToYCO9EIlBhpB2iypOGOPNcSbDDv3xMAEvWfre64Md1ONOiftIr9ynFJvQrWy-5JNxPhF9JtZxbbxWOlHSE5wl44KC7bwd8iIF6YuN-AA-GNeOEj0UCseGU9s7kkHo0KGe3vGFfY9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quASYbv6tYX18IfIEwbFxG_cGUqpAF7cDfcAE9rpWj7yUNXQa1UlkeaaZM8FoqoiZmIGbx__swPb_zNHIQ_MxcZBPE_SbS5IZDH1kHTAHo60uNi6o9WxB1j71E_UkT1r2eDFpBP9jqY5eGoS5VVbHVzihmzJMe_2fsSMh5UDgwYqNusC4fdJqWSZWtvDg6VMLGhifUSphxGT3hAjNUHstBTSIdF0l_X1TJa9fOaJ688XnwjDvljrK7AL8aNAnx0D_eN35JK4hNRrAnzf93ON4w-toi4X7q3Qtb3BJnnz-KOO_y88JpYMQ3avxJT-McRggZoJR9w5eDAiehYZGhrquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK9CC5T_AMRC8TxCBrWsYjvKnoZ-sm36fkc2FAaDPkhp9l6L1XCEAsNgdaBy9Gh_VIAXTYJzQZiPPBkN-1zGi6Si1_jrzORrYUgwwVw36vl99bbsD11J4FtVahmD7Nbr3Jh4brOeMgh3m5WN2bnWhBjq9vCmNDVzEeiucdraQxFfJPDI_588LeJ2tsGYZArOQVMYDyoeb0XPTBNgwci4v2ovp75fVCTt7kpWrOfaWg7AZW-S6kDPVdNUqHEGZMVgTAjTynvFAwrThoaESNSN9zuVJ0UKZEaE9jU4uUhbhLaBZwtFN0pSFXPJ5AOV8QkhHaGRTM4KGATMNzr4dsJNOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=akZd1vAAmuQ6fNqLAG0InEyB-mBLoLbZKACweoCLY5WVz7m4TbHuuQTUoy0lKWuLMVfW1RKXvHF6puC6xn3VOUStRy_mwFF-YOv-zoM7lcVvJm0MkdtWrhRFZe6mk2nZtqAul63V25Kf6X53a80erJ9PeAwh6jMi4DkBaXLZOiMNeCW4AFZwUuxbSehwaE4Ntqmwuhoc-KFmYtdvNsuCk4dV2R6CiG9QFlySw4R-ojrmFKsXIt1oytMYK3AF5a_HgOuamdMcF7MzbIf5jrhiJc0MRc_FGrkfnX4FgrMn12AIPEYD0jtOFU3CdB_O0-5iv64gcImTU29qSjWjDJKxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=akZd1vAAmuQ6fNqLAG0InEyB-mBLoLbZKACweoCLY5WVz7m4TbHuuQTUoy0lKWuLMVfW1RKXvHF6puC6xn3VOUStRy_mwFF-YOv-zoM7lcVvJm0MkdtWrhRFZe6mk2nZtqAul63V25Kf6X53a80erJ9PeAwh6jMi4DkBaXLZOiMNeCW4AFZwUuxbSehwaE4Ntqmwuhoc-KFmYtdvNsuCk4dV2R6CiG9QFlySw4R-ojrmFKsXIt1oytMYK3AF5a_HgOuamdMcF7MzbIf5jrhiJc0MRc_FGrkfnX4FgrMn12AIPEYD0jtOFU3CdB_O0-5iv64gcImTU29qSjWjDJKxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRSmM73Kj-8OBb8MALhQ6Rz6f6msPqh2uhrVGT5nkFkDn11L3iNstf8tXKEa0YU-yM8JPxBwBHMk_bX2b6gd5jFyT356-chLca9c1h-CyDdN-zR4gqGI_oyPp-RFpi0yLMrBNUpPlyGsWUcRGoy29_eU3a4cex58B6da2kHIi526LvVh5P5rPUNNgEOFwxeUow3SujSvbh_BZmsvCn_37hQY4MiRTQhXssp1678LziXwBzGZTwHVRb4OjLL7370hVod1IUP1NmTWnQp_kQkYj_a6xbIA_381TrZtmWRDQ-oG_YuzwDuoTyYrVNCjEXY91NIbVi_DDtGIp-2Q5wgIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2RkraEHa9iDtLluVC9ZoxyItZ85yH13KhiOeQO6J7XAUQS0eVko6hfaAUtPw5FyqptrHhWbp4nQnF7ntcY9DwyUf7CGBvWaHy6KN5t1tOxAeyTDeuO_yRbzchuxziQ2tIsCZTFihT-J__-6GZ67HwCMnzCQQdmRezcuowpRfjS6ht-2XHSpHIcVJQcsWYEnwp1szVe9wNJsl6vs2VbG3w5oQf0miUlopeW3u1MaaH-TyFWcRn3Gfu14cY6HkPqyDAoa31Y620rtmmaeJk24GSjxubLaozcbNEo9rt50z0cXuO3jLorjc_AlGHIbmNMt2dOh7HzAnF_48isGoLxCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwp4BHv33LsIm_UhCqQbT37o4Ai3x4fBS5NsU_I5SBfT-bWYsxMjFHA_cSEoQ2XtmaEsbPnwXyMIVK5SJL6V2m8Ij4yOBw22y-qZ2SL808eVr9UspFJNuCz8nv-6ntRb5WFOh0C5RiDZuUkezt9eoGCcubLfFr3NZpzBTYiQWva9QU-NS_dgKm-4Mvwcqseu6qKGVbsdxc3tN9YWcE12RpdkC42-oP58CNarY42ngXGb2xnZi4xngT0SoW5s9IzXi0VMmRV04cGyVLJHedQYI8uUr_-T_kMrkMDlsagszp1KDfxI0yJzdYuS6gApMTac0o6XxI6JW01TAQGsLqGWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA-K3HAj5mX4ZXkQ9ZE3TybG6yoPGoQ1QeLVZORrtW6V4x4teehsBeJzBhyDeRfLPk6byA9P6R9s9Kg49yo6I-DabZTKl3jfQUQCSQIwsOGHE2ZzShnHIJ_8reyLara_xPEmXWozmXX9WFS8Xh8avgoYYdDTzpqtSxqgBAT8hsgl0BQHbFAS48c1rLhXZn5UvCLb-py7MgM539Y9e7LCYdi2VyDQ1L_mEO8JcXMx6yTQ7nhWnHx3d8u4rRhLqyHfswi5HsgemDfVu_YOjgERMYEGtoRTvMNMOVshP4jg_rZfwIyYVTqLzvve_wda8P6lnTaQJewWK3G_CM7qVbuDbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCnOUAtHmQXfwlUkF84N25AtNQJltVLt_WssX7AFU1h8KljUhy5_PK6xLcje17TRnkrP-xPfxEpu6WKioRbrNM6ck7_8ZCfp7J4iImB2y4AdYwqt02KNj750L9A0nn-E6cU7zhQbPYn6vAvomYcW2nzshFvGCwmE3mzTexqbKUkE3XYdF6LasW56ppp1d0uFA0jHT_uqhuoMh-VdamvmzEFepj0iL2bDK2uCf1u9jz9rdYplljUuiWZ9RyAQME11bSV7gKDPgKFfz06CzsEZgXd7fUFCpp1FSyKcsNKvqCz6Hui7bD8uVudR7qaxtGctB2RKecRP6amLsiC-xoSbKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=V1nqyVL-IiqLPvnN96yo4HbV98D-PH3msFuAYZSEDv0ECZSo9KhsoPwVHsgRztl308NfZPFLHmRisJnPGUu5xIgHExCV_KIE9cAk8gUl8LgLh-h1SbwPoX3Iwo6SEWp3vemhiS_WPY8nKoUxyQpiz0IpkgRcGG50svr4m5kQ9RPguHAk2IX-8TmzIOu2oykA1Weaw4btq8VnI6e4Wp0AqfVDqx0-a11jY3k6QLgehNSOCRlPMweiVjXoP_9Lgdz9WnyJ24KSCrRz3PcbxlqoczsX-fAegJqSjVKsYyYkGLQ1x-q3tsrLsHPSuHd_XuM0sgu5Xl5MsWCr9A01ozg2Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=V1nqyVL-IiqLPvnN96yo4HbV98D-PH3msFuAYZSEDv0ECZSo9KhsoPwVHsgRztl308NfZPFLHmRisJnPGUu5xIgHExCV_KIE9cAk8gUl8LgLh-h1SbwPoX3Iwo6SEWp3vemhiS_WPY8nKoUxyQpiz0IpkgRcGG50svr4m5kQ9RPguHAk2IX-8TmzIOu2oykA1Weaw4btq8VnI6e4Wp0AqfVDqx0-a11jY3k6QLgehNSOCRlPMweiVjXoP_9Lgdz9WnyJ24KSCrRz3PcbxlqoczsX-fAegJqSjVKsYyYkGLQ1x-q3tsrLsHPSuHd_XuM0sgu5Xl5MsWCr9A01ozg2Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgD3XHxuJ9eX_cCNgoSN6wlK1_fTlCtoqlbTRPJiDsPKZF_XoRVIRnut0zAP1ARHi5wb6w0ir_Ac81ZXCmeVZdcJ6J-IIlSCIJK51MsA0zzvudt7XKxY09ic91r9_ppdgdjzW2vrd0UQXOJpf-r0-ATKLyKWllsoY-o_0GVM9apzaklEB1cO3ABxC9LXVW-MJd4rESg9Hn1JBqAleI3nLIAyb6M_BAcrleqnWptZN1EYQ_Za-bGCrpxJ1glqvgjUVugKOUOaOlbhNez-U5XQn9_362f615wh4MIPG_lS9Weae-XPwmx3ErMlXvxelTIFF5KTVWfidiC-yc8VljQVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=sYmMYuxfn9SdmeVvyLZ84Qpc9kx1wXnN5Y8cV_mPxyXJ5F3De74DscHQ14oLqNRusM4iImjeQYk3EUJfNSHXQLXJy7KDvQsM69zyziLqYyE4Fqr0wN5dXNwxIe1Y3H39GtLTRvnvlsYpPmKbzsiNnXRyy47CT_1Qx6-XuQTnpVYB3wGC0kyumYUADFuGOXcStfMNSXIhqMk83rBouaiXgYCF7Amp6sixIqm3oZeHrVsH7hgOYHx2QUHic-Pu8vQm0mnkF_CysO02wLbu0tVX-iYV69GeGiwgPB--LLxV_sokdeDh3CGZs_DTBSnMwXgTX4dzdDcmU8met-7Jj_Ed-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=sYmMYuxfn9SdmeVvyLZ84Qpc9kx1wXnN5Y8cV_mPxyXJ5F3De74DscHQ14oLqNRusM4iImjeQYk3EUJfNSHXQLXJy7KDvQsM69zyziLqYyE4Fqr0wN5dXNwxIe1Y3H39GtLTRvnvlsYpPmKbzsiNnXRyy47CT_1Qx6-XuQTnpVYB3wGC0kyumYUADFuGOXcStfMNSXIhqMk83rBouaiXgYCF7Amp6sixIqm3oZeHrVsH7hgOYHx2QUHic-Pu8vQm0mnkF_CysO02wLbu0tVX-iYV69GeGiwgPB--LLxV_sokdeDh3CGZs_DTBSnMwXgTX4dzdDcmU8met-7Jj_Ed-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=RV2xAZbHYCFOT53SzLf2fmF4WPCUSf5zu4LsiPjwoj0B5YXKq6HSBktFyad-GNG3A3bmPYAJzcsuW_uWVHNhKmJ56lAB7cXJl7dxJi9zgRayhid4JiF9WAzdKBmffXRkA8z0PgJWbmbWdlKice7ej-ISkAAFcF0-A9CZ2oLuTkZ47plvA7C0ZvKfG8Umb6-Gj66rVvcInkwRn3-IV3cs8dbrqUqEcDX00zFBwY4XrCy7vSBeiJwPLUhibNLj4s1kjl7SLs04USKScMODgopBNUF4pVtYsUEf5FqqhQXrbZFnG-XeQN-HUWxdgEMFWcKhBjlhYHBXIGggPzXWCvJeqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=RV2xAZbHYCFOT53SzLf2fmF4WPCUSf5zu4LsiPjwoj0B5YXKq6HSBktFyad-GNG3A3bmPYAJzcsuW_uWVHNhKmJ56lAB7cXJl7dxJi9zgRayhid4JiF9WAzdKBmffXRkA8z0PgJWbmbWdlKice7ej-ISkAAFcF0-A9CZ2oLuTkZ47plvA7C0ZvKfG8Umb6-Gj66rVvcInkwRn3-IV3cs8dbrqUqEcDX00zFBwY4XrCy7vSBeiJwPLUhibNLj4s1kjl7SLs04USKScMODgopBNUF4pVtYsUEf5FqqhQXrbZFnG-XeQN-HUWxdgEMFWcKhBjlhYHBXIGggPzXWCvJeqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJXAdorZJkNculg06zPanPuch7o_63wKuPAhBL2AAvy6Cn7E58TYzVAEUhgdqVptOrlimdSzXQyR5hJirLK9GtW7bvKTeDp6-tSIr6xVCK87E1gjeuYKuvUFtZTwHll1S005EHfrhFzVHqDGYYru3mRYkqqLw6ee4uzigLpYKxtM7CQxUyRFwOmij4GgnnycKSBXsKvuvZmmnHilpam-aqaeTox5TRll8zPDLqVPcEjmz8vt4VLyjTj0tFctt06YfVpho5NuEwHl981PER3w4u6neKv51ystOI_CXPyampexAeCPOSejFWXlYM3_nc_6OLMC0cO7UV1ONq1SfK3eLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIyF6QhWlryEy_TgbIz2GiW6DgsFK6wWcL_sktwDGsC6yjbYVzsnwK5c2AW-sm4yXMyAaegDp6yEaTocudmzbBioVonI1X8u3Nv5QB1EeXKT7oqLS_fFd8siZHH20S53AGL2sb30asNS4_thvBJrZeMJfDCR87F9kBMpcjIoy2V1oxgtRvRnyGpeoGSFPCvqNF4Sg1ktOCgDGs6_vcLTQELpH3RaWzZzgm4twJE9iKTDiZWzQaqWvMU0vr1MwfN-o6e4cx6zePd5jRe0dvzA7Jl--H6rHm2E3EmnKHqyhZPyRfbqIFs6waVXa9Cbiaq4s2YwJS1oprlLB3Opn05sZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=qHgxxlccEcX_MkFykVcFt120Lh5Gn4DBJoHe7YW_RYAaHWK3x-WXk0nk_YjY9eqKXDttdWjmnLzwUxJ8q-qRwIU8IMSJUPyF4korhTNTmHBvnRFIR4eodmeLGRKxIo7qYFpRdQCHbda4RcbeiERzg7dQ8eaTL_C7MIw78eEWclfn1NUrMbzqwgAtAFYhhDd0p6GDL1lumHFBavf2nZSXCTUR6gLDQOOpTzurzuIzUHyyoOrSX_55Iyf4GVJSmUor0Okn9OUWXBwmVu0d1loV9bhID2w_YbZQJwqWR0joSykr7dtOXGxqNiQcW__XNQe_pGik0IizLyuVER1xqOt-2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=qHgxxlccEcX_MkFykVcFt120Lh5Gn4DBJoHe7YW_RYAaHWK3x-WXk0nk_YjY9eqKXDttdWjmnLzwUxJ8q-qRwIU8IMSJUPyF4korhTNTmHBvnRFIR4eodmeLGRKxIo7qYFpRdQCHbda4RcbeiERzg7dQ8eaTL_C7MIw78eEWclfn1NUrMbzqwgAtAFYhhDd0p6GDL1lumHFBavf2nZSXCTUR6gLDQOOpTzurzuIzUHyyoOrSX_55Iyf4GVJSmUor0Okn9OUWXBwmVu0d1loV9bhID2w_YbZQJwqWR0joSykr7dtOXGxqNiQcW__XNQe_pGik0IizLyuVER1xqOt-2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7tPL1moaCm6IHc8KIjQhgXUcCFFF5kUB8UjO5D6oD4a00oQOWSc0jPrYnDjktzfL7N3zp1neKvXP26zzSOiBqWEy5SPlIPVXFOmwwGhW2k1l58bxDPSO4_D9fjNuTIb0fEmZ4qqroyaRXh-ytsG-tbaScnKQHsAbrMCnJBlLFDvtR5zhnFrtTDd91MsgKqps5GGNUM2e_85x-N7HTBAWgzM4cNUhmY4jDKrIqOOCOAbmV811umKSqnKN77kUNdGECy6PsspznUuhozM3yTwFlMe_A1cmNby3cisCx46EpeQgo2JJonMyoJxvPWK4P8ymMyGwuVUYI276fBStcNdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_3_cCwcBPDqu3aSOMD9RoOffGfz-ioS8HswjX2IygpP_oFGwbOEMD6OvIuyERHkl28e3nBRLr5UycIIvNDX4Ob7Tm_9yEis-DLtkyZUmzEyoLa2lLMCGQLBwSTwaEDgtUye43MwhfS0NIrYNGXs3m_TAtzo8LbfiD16HVOUYNuN-qfHV3iU0JAg4E16HoZQSS7WizxgmPdZJ_ymAqJ9hwBxFRQVKwse86FUrehvF6sAb7c0W4ad-A45AlcxE_Q4djNCCnRy6HDeojERDnKnv8ve7LHV7Z5UUO4cp9Ds7NJN2ok5p5-DZiDHAo_p3HrpuGPPgty8bh9hIhiNZL15ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAt6faSl49Z_J07fhaSB8It9kqOYoSXsMCnHrPXPttA_zObvxijhwqQrhJpus4Yt-i1_SeSrlV5aGmOrgMcHNxabc68RP2xnZHQoQvNSzcCBjOkeHBEoG1i4g7a4clqops-LlzQcFWpK8EUy91xt9cqw7JEcJutIefj3LpBF-iF-2R1GWIC_N9qCTWOvcyBZQ-y1K3YwtOk_2vMuEH4ZZKqh2pgNE8ySwuAcMHJEgrQl47RBvLnBhzNHXQuReEF_Y_89a8D56kCC7_ct1ZN8jQKn8AAN9RRsHG0kB3e-uv0bHvd5eDCPwVasxXyMc2mXLUA6nFSPNxSKGQMo7rzrrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWQ6QzsOMepRpDeJOO1hyVrMd3-qgBrxmVxIf5vAWbg5a1mrOxLOP2fbpaBb-hUYGXn2k3A3RQerAGMPL2pTt-TFqSHAEdzI7NVC_BtvoR2GBBVVc-1C3f8ZLkkgrm7h0ZFZ8TnyAADKurbpaV4n4kwy1y5yuCmt8bOciTHkq9N4UsrII9OQvLHZtgg55HJEdYJIQv4zcQ__7oC-VGXnkATbfkBEQNoxbB6VSSfph-yT1BUDGlnXkIDVHWBc1-eYacPNocF6ASNcGkY0UaT3IbQJhi3MrHM-v5e8OPFYkeKCseEPtZAmruW6DAK--s8w7UUxWKJy2ZZhoL9hP8PJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAIykDgRRl2DBgrRqEHEKmEinXHq0E623aDuyLcISUo4SMWvYm25QvmDzQS2HXmpnalAOkvvD3F3FEc7kO9V47HduskdzkUUn2yc2ipwHEWpkUwaJvUCCXO0-AYGPyLlYWFzZPTsZwJNCRhWxG0h2XnA2Qu7kL7W2TxJloU86D63X6RJmk3iqRKG1hAKnwo7aFHhXlg6iaKCUHbM5bw8Gd1mFdmhialiUvS78SvQ518qUspuJdzOmuM7Y3JJWFkUN34uTnTg6AUv-i0k3USGFR3r4NSM4JS1SM0jsX73RZtT86uyL8JiHWE4ehL_ixYGf-htcfJLSg7idXGQkegeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1Op_I-_PysSA34H7AkVACDxvAp4_wjSHKn3C2kjjJrKPTfJvU106mAbxQnNdO-qcJYl-4W24lSzwlXeAqatfIT-Jo6YhhrgB70E5v4foU9recbMJNusWxy6BLNOLZCqIYlLjwCT8v3Kcbn8VUlnmPRC-T3lhIrodCQ1phhJ8IAtkWF-Mb3C8x8o3QIyciFKoStOIOE8EUDWV9UMSng-AYj9puau_gwC_byTRalcjYyQrSzloqXQaesON0Rq_9m1W0zRJwZasBtIuyylbjeIqKOHEttWisWgD75QVeK5eZc2DTk282epFdIPhcojHNim6AbJAQvo1hcsp-PPKpORCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZGEhc4e-WlOQN7MdGUOKrvxiAiLHLsp9wvpuX3fiAzFO6Xa-MQULAHNResuVgUrMk2SxGCsLyv3qg6BkbVUnLQLfD4EUJSryrzYW6RHEhZ-5JtsvN7tyMJeVPbpMmWzX5BYus7Z1gieJ9kvT4HW8vldy6dkR0CglMLxqgByWrlWZrP8kKd0-evQVaeTfpUn-Jk6-xMB7XjpW8_IebMN11MfpdQLDQE4HFGSTcBENYG0smUtKwybFuXcLJ49CRyvweCHZGsPYhX8UROruAk7M7w-cWeXy-eryaECyFbKEuRYiRCgH4ZuCd2X50ne-GbiW4X-Tgy4iwy3D4VJ9sWy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjaqkquGwdAeEL0kG2dLD7I-ttAa5Fe-TFXF3_uiGwAz77OQmTgyQzCfHAF-F04L8lymnkql9UklZGHcg4N-OVZZq_PNxQ5WqyxHXlWVp1sE1UHS_iRvHbs-cbPhlMvhfyMZNpg_2x46_MOY306X1Mx-ZEj4g_9jMSsifjPiB_95ixBDLV0MaRqMgmBhNFheGedYSGQzO6VXpv8pt4xm_weizrR0UaXYtOUb20hDDqKdA89eoxHwmT-h-be39vl0zKJHf_xhKpHeY2m0o23d0qeAkUNALd4cveWFl6QqD3OQ9BPxcOtp6X7v0gWxcLGx-vvTX9ENN872RTqwkqColQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj47ZuOkDAPkQ4aF-fMxd71X54E4tTRmIPOm0p7-KMIXHGOD6qQHJHCbzLsNE7F-gNK6eFRLnmmOdHRGY_zxKAm95Kc2lc4P9N2VyS52YuZDDMIa0KtPZCFXmynfrr8DJ-fiZzbSeBKJQTUX5Ez-sZpImgijnAtdH8tTXDD8ZncMmwI5HWHQzCfK-RKvGNKeY3tt1BZXoWS5AQlMGWBRzvpHGW6OFhRnIRu9mzk9VZMgtt0od71fZ0bfMU9YQLu4k7nvWOAnGDFjZQ9tkpq_Rvo_4Oj_SdiCGkkomNzxfzV08JHVZL4l80xqjYpipVWXNeRZ7Izkt4zYXuaZCdCl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5T3GwW1YTwcSKSXNYDnfRfeXo547UiVIaScnCIXJdfwxGn2vn3YVuD7Z5ULP5mF5VyliK4fl9VZgijICC7bPSYMQY3jAuWS--Bj8RgN5qiJb_6kpP1dymLm0FcNx74ffKphsBj2HtPSQjqlNtCgpUtMDnrq9Qy3djqx1hbQb6n8uzs-G1fQwUPp68TAaxd02Wm039tEh3LCQl41LhSp1WmG42LvQejZZ6CITkXf8KbudKvQIogFN5QvMfY84-nlJCKDwrx3i1D_WILR3H99sOohP1Eshr9D8U45xN14yTyhSD7c166vrJpqZ515T_aHdbwX5rm358-9-iEmNqn-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bei41fMgWNkQnntKcRFUxg-o-roB0qJOrw1JloaQAXMm9OX0ePZ7ikszo3aeyVM_ZpAiv6_TQLSBUZxO4IBuap4KuZsZ6XGMAivYQBFygApL0I-y6O3VV0P5iKkdhb-iiE5ITds7q1szddwDQnhSgiovK9f5962r6X9OVHBmWFG6ybe_hqqohjAKeGULgSueWGkQBpiECwxuQ4_8JpazPCHT7mHCMriWXj0614on70DP1n-bUoqv31_QdH1ZBUXqm9R5c9kcYgOPld1rFtS2A7h-hQ4dxc0XHagOm-KyRtIhafTwU5IJBVE1X0ZAiGEPdsG4YPszRjf89ueZWhK8nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=d_mxIG0jaT05n-oq_3yusLK-Da4Yp-jvidx36mIFzkkaBh3L-XcdolTG8wRWyL1ovYhfWWLdggiIPXkBgyOOgz-8ipBOIp__qgbiKXX4-qE_qkNixrdcAWlaBcYHXwO0sR8aoENUBrIEq1jeDFIlXnQiJalvFs9MjaRj378iJ5-yAZP6frSlBjiU1B4Wah4LQaw5leKEZy_UAyJtjO3tub7ZJ0ttyviEz2wU_agnpMxaV2z88P2En4VcbrlvQ2NPYKGzJOLsog94FCFaEeFGw0hEYkFjAdjy0EaExARljYjZQ5aAqD22E7roxvnSVIe7xkipZXqX21GMo4jPm4-bEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=d_mxIG0jaT05n-oq_3yusLK-Da4Yp-jvidx36mIFzkkaBh3L-XcdolTG8wRWyL1ovYhfWWLdggiIPXkBgyOOgz-8ipBOIp__qgbiKXX4-qE_qkNixrdcAWlaBcYHXwO0sR8aoENUBrIEq1jeDFIlXnQiJalvFs9MjaRj378iJ5-yAZP6frSlBjiU1B4Wah4LQaw5leKEZy_UAyJtjO3tub7ZJ0ttyviEz2wU_agnpMxaV2z88P2En4VcbrlvQ2NPYKGzJOLsog94FCFaEeFGw0hEYkFjAdjy0EaExARljYjZQ5aAqD22E7roxvnSVIe7xkipZXqX21GMo4jPm4-bEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=BpfzeLcRNwGF5ua118oMrK3mkFSjfTQeAdmFCLcMnJU5i98M-ruh4EnjVVTin6dQCiD19Q0aClMqSe2MEykcBSk1Vw41yofN9Ru_QM4SORbElrgYnPrtiBR4xlrErlbfEnfI_PST_cCJXoogP-C4GTaTE62tfkNC7Fh-LwCRB0pvODbWJf7vMquSUFyacPTKwhUn59kD4mKqmJeayrSmmFvb7ZP7ivZuqilcs6yFqhb86YWkaG6vkSnQzgVs9EL8mDZbCxRY1fH5ydivGuMc-KxLqP3Kx5-E-eh64frtdHB4CLZaFOC6lutV12iDXwsrmykvuESQnip_DeOa7l9cBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=BpfzeLcRNwGF5ua118oMrK3mkFSjfTQeAdmFCLcMnJU5i98M-ruh4EnjVVTin6dQCiD19Q0aClMqSe2MEykcBSk1Vw41yofN9Ru_QM4SORbElrgYnPrtiBR4xlrErlbfEnfI_PST_cCJXoogP-C4GTaTE62tfkNC7Fh-LwCRB0pvODbWJf7vMquSUFyacPTKwhUn59kD4mKqmJeayrSmmFvb7ZP7ivZuqilcs6yFqhb86YWkaG6vkSnQzgVs9EL8mDZbCxRY1fH5ydivGuMc-KxLqP3Kx5-E-eh64frtdHB4CLZaFOC6lutV12iDXwsrmykvuESQnip_DeOa7l9cBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr3TPVh_utIDRvJ_voDF2k89_aulB3tpYkCrINwVDAo2Gd3X_RnRgPEVnVAo8zUVjtTsfscNSYrTseaymFGGek3VW0zbruTPpO7YNunIFiU7KRWwpNT4sFDkAQq6XSyT5GTRugECKsMd9giMnKVSpI0Oo40GBn1oUVE3WOLgahAgrEZD6N2t62KJH0QCj8AezkZ2lMieZ9kvOrvU65MedSULRHXNUvwnGtX9HSxzdRS6tDsaGW0hYwFCSoWUdeKqI2o6Bg67BHK7QtdRqI9B7cLlbLEg-0Ye86YpBN2REvikUqgDxoiSx6xsD9LkvY_I-Iczf6mY2Fo3ZO6CjH6jAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGF8hLXj1ZWO9taDdqGn9UgqVcZJBYne3tT6sWPSA9JIdNdV-aIIwGyHhqZZEzBPylFbWY8aMysAlOmydu06GPd_-4JlWNM8mhBW-zMyv7w6sydE2jl6Gq9USmJgtmjMIHOIhspBwdUJCYmVWLuQIPqLsHG8YkMuwipYi3NCnurxSAv1Yxi2e3PeoOYLhRQvGdbl93Gobw0bmw42WF-uLt1LMlipPeaJNbshe85zbZfgb2UnYslHW-cR9c-HOKOrqgOboBsRhA0ZTVusOCuDBnfoYzHA6RwD0MgTEM0G7hBomHUhkfkqpu49NT0ZeUQt0eIJsdEPuKb9Pl7GP2IaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whon9cWsEFUV6FFIZcyk3G0v-RZTvowqwQBXmAMyBlTGG-vyCtBSnyZmJw_4Ox7uCwl-Eu5veW-lW51g6dn1Q690YjXF6p4syHrQ5TpMi7pS0RnuC0OxcH5WlQx4mAaIk8XEAbLDTjVXDtyKz65lYeuaFCRXbFg8TATWB4eZuziwOQ_7ImKsEhRDymX_Z-VkbK5y5Wy0qPEIxs-Wb7K6lEERux5Ka2VKesPL2kYKturncQm3fJm4mPDjMVRFsGjD5omi7-7WZM2uhXeZ-S1NZpR-KWp_6CDiJMAvLAyQscKfVveZZdhvIonAH1P1LoLRMuuqXHtfyBYcQmf0LxMEQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=s_YxoJY1H1boswgBEHEW_X16mkGcNuxSBX6J_bbzvxe-crLWPad69MzO9ReJDdZAdHUtHk87uvBy_79TYH_s_3cwm56o6HsAe23sA_yT8Uw2jj8gt928zfezoKRkmYK4EDfCFCjqTDRiGTDQRTzfOtGRHzsVad8vxosEm_c6r0opKj_tE2EkjDlBwjOnCcJdnYvhSgNxxAD2T6oRJlgnthRfQw7rRkxE1m7_TX_ZAU3SkOWRcSz6rqz-4ZrZD19aNkO_eZfjs3N6M7rTtA6axRHGKvq0fGVmg_jQWEVbDADPToerjJfq1P1z8Wc3OGWZk8EWyq2Gu7fw_yhqpia7BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=s_YxoJY1H1boswgBEHEW_X16mkGcNuxSBX6J_bbzvxe-crLWPad69MzO9ReJDdZAdHUtHk87uvBy_79TYH_s_3cwm56o6HsAe23sA_yT8Uw2jj8gt928zfezoKRkmYK4EDfCFCjqTDRiGTDQRTzfOtGRHzsVad8vxosEm_c6r0opKj_tE2EkjDlBwjOnCcJdnYvhSgNxxAD2T6oRJlgnthRfQw7rRkxE1m7_TX_ZAU3SkOWRcSz6rqz-4ZrZD19aNkO_eZfjs3N6M7rTtA6axRHGKvq0fGVmg_jQWEVbDADPToerjJfq1P1z8Wc3OGWZk8EWyq2Gu7fw_yhqpia7BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انترهای جمهوری اسلامی
یادتونه برای حمله گروه تروریستی حماس،
شیرینی میدادن؟ یک‌ شب شیرینی دادن و ۲ سال
به سازمان ملل و به دنیا فحش میدادن که چرا مداخله نمی‌کنید و متوقف نمیکنید؟
(شما چرا نرفتید متوقف کنید؟ و البته میگن
پیروز شدن و نمیگن اگه پیروز شدن
چرا خواستار توقف مسیر پیروزی‌ها بودن)
حالا هر شب میگن «بزن و ‌دوباره بزن»!
فردا که «زدن‌ها» شروع شد، بخش «خوردن» که رسید، مقصر میشه دنیا و این «لاشخورها» میشن «کبوتران صلح»</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgxVj9DntEIcrq5xWTyCjio7D9GfxLeXs57UB2C1Cny72BaCJec35TYDU6oBocxmPZ-qRXdaNPTwc24_hgPPVsr7fgZD0CCenB9CQj36EkBiAmFX0dEQf_yiIqzIV46L-tIOdzMM827DUOppvTMmQhMyJcwyedAiVUfe7HjOcBAYjHADfCT7jtRKVZy7VtfR2Qj6tCV4B3gfmrDlejw9TLY2oyISmQaE21vN9doYDJYIxnDJXXZpseOV65dEzGFIWF06FTpDmyix3NkHQ3X1N3QiK4l1O438OOqhP64QMh4ZoZw9e_IFoXn-rWkX95Olf4uS_TvInNMsB9an_4vABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrQWrQCbg1KNMX3-2PXRAjCjrwU01nFfuoMqrtFIxLJotufIYT7j0sSQcbkiqTzjwyK-rr_y5dB90rfis_4M8_T41gaxCSVw6_UD7oouXoBPyevnXKH1nWMt91Hnum4fJPRzh7cxz2NF_W_gr5zxGzO4LIxxkK6W5HWhqQNXWqmMqTbKWnG5Y-cbP5Y1UIT7f99ObcmTRTtB_09SsiLGYSZluuf9rvW_0VILZFIbKHrDe8hSPRKTg-BWb6K86mH-9ucZYhxIFsQxanhxM8ZOQQDYcBFWgd8M-FLrNUFIYYOw6HwMNpJVPnH3F43q6KEmI-R0_0K3V66E4t3av4JyCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiXXd3PafdAKPUaJwzo35dbPuwzOYcJI1jBelY9zZlzIcA3cn1oFlTNAz_jNqYUBMh23b91wpxLZU2rW1dMPBeyBOreBJ8YEAheBJMpoNPEOGpjCMDIV2ZmapX99Q0KYT89rSxueO10gAbUjp7r9qEJQDWviXQYj6zhF3AkTRfk4eZBlixfu8mL-Ni_8UcJK1pW14EVDmlm97-xP5iSRm9wN-bhAwwhzJmjvJvTIvQ0W9bqyQ_poLqIob5QUDrWzR7-EbM8yAhcwUOjWHghJDpGk9KxzXZqtK5d1bHYjcsoEmBX8PkWvtt5yUue0NmRvZ97Jr71BO07iQgd6raGnVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZbzrKECAKwMwnQsxlJZrow9sm2AOyxOpkQ0azXnn0DKDN6YY9L4SBzwKeLdhHugFG8u6rQi7FqykDiITXPKIHp62y7u2PeyuQBaeVfGFFzPrM3grdVorx6W5wpJ_OPB94nS_zbSaQovScOjKUNqyRjV258qzrD6UDf4dUsT_ssx4YNjw2JB6vqbzeVDGQm8TMCVxVr74tkBdPLKIDa3LPeK79rOmRGAVmJRfaYw0AXWidqPoXGY4B6vXJwXnPxOVB2IuJ3e2PvUNWAbNy85gdKpDybwc5_QJ0XQtWmyF-l31UcDYcL3fWRxNHzFn_qI_w8x2IlU3eoR5SOPsLy6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rvpul-JqHFCMAjLTd3qAggRLrP8WKJZDIYXS8oZhDy4uBa2W0td-jvD7Aq7MCZY6pASig7fwxcLvMwZHOJA2nPK9dzbEv1yjeSdMTNoBmwn8tiu0LGhPuy_EtLuWU8YmzsGrQqMidm7az555goD7kS3WLEuTSegk0QgLhW-omZrvP5tiisTk5u1aI1piWRQO5jvaRzDjG2tVqc--Mxwb6-V7MV4m7JOSpbUXKocw3xed2me7wbHnHttL4Av0ZBOwinwkDfu3pkt3BKXhsA5VtXhbdAaLkgUyMiUlAFfOiQQScDlCpxyaRj7wI11aU_LbbPJDPcsItCWf6hmQNP8bmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMkh8g3Kpc2kAUSejVId3TU179fK9i7aISoKD9KXnzIEpE4sbr5L-2aJNKodJ3eoS9WO_q2tDWpkndeJqRj1Ieix1dhH1nwfPZjH69J3Tr-VIhKWw2CmQ5YYt0pMMq7n3mxT-ii52GdYEEvnUaXtAJZ_EcG4omn4lIYhM-a7yrV4vntMeDJkpTeNCs9dV_jBKmd-1UmGIE-Mqs36rULOk2DmW-5Um46QWC5llFAq82ZU4Utx-Ijn-yFWFFt2WcJmpBb8OzsLQKu2SVWNS5_KyjIXEAmgTfA2jjIiypwR31TCQ-BGfD04qizs1x6mmUnKsToILJ_9ap-N8NA2Sv2U5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSgJeSwu696mqLdG_FyJr78Kj3tAgEUYDhNSnApLAE8L4sSYd6oJ0dyrxUgJyt0yfLaNica-l8xvaxR6aatHeTuQjeNOeWHcdhjFQtVZpOjcEjGl3JrucK5oowQXNgV0VBKFA-W56V6T92uHSTj2-R8G_CbeGaEgDci7sv3hYHpIKXy9M16v7OhDGbLnujTuKPs9oL6gBDOIZB1GJ9ljp0r0iYzOv2J5TXevni5bvbPY0rBJSsjzdJLklmkJpgySyQS-1w7tqCl33-k28A5I6ygiVcr0e0Ov8yqWxG8pq87sCKH2ZlrNE5wsvGrWiU9QURJcOy__Z1ohDyXfkZ-Y-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCm6haaoU1d36kRJzQkwmP3M_kUmhCIpzSutcGjpts2Hap3iY2fnWqlqjOV-ygUvABRHvdUpcNO8rWlcz4cgdfK2doHgSzzXSpNPhg-DY9EhWNXi6rU-ciI0c9_eMvuc33VRama86MAbHwUwKhnAFY3IssyLlGm8VnWC2qSoH55oQFsVk5b_4iLrG6V00sXdYuSn3Epmoxv6enAkMiSbJ4urU3lap_2xMC6W418w3lSwaAev_SE7sUiGQ_Y2gZ87E3twku7JYKUGvTAqS2pYVxZQ5e_aYjPx-6cDNcdqQ9iFxXyiVCUDa6ou57Tn9fwI9oi2A1NIvBKvwno3j_zLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oN7_9L9Imoi6ZZd4VOVi5WvxRPR0-RcUSdcMu1kHk_g42IuZnrizDneyxK1yv3gVNemIIfUJRxzsR28YYxUHoundK8zDQrVOORKdrtZrjg_WdfMHQgRvrqOdx7XVtoi1o6YAsOiJXb2GfvFvFX77cfs3d0vVaqeYJNYBtd-1nYMHbSWurXkbXM1vEo2OeMsDF_UACWz1H26GkLlXZqp_2btKMziga1FPuZ3jUbSPFJYEe-b4LpfE8FcqsYoMJhciG5pQ_R6SfWFEbBZTE1C05qjxe8pfLpzFWNaeA2oGEO_uRuw8b6xKgEN_SqygyWy7MH8xvsSJx71bWuVnj7C-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUtCaVi8lXd36dNqu_XDaIDClJkJ7a44ZfwyJzcVDoQsT_GqD8b551_38qcZalqLXjyrzbeGvmpEFkleXDp5MVteQpeFh1f4_y11h5vptq6eDYAahQmCwRokQ-BiaNvak38ZshECtQjYTY4a-IBicBEJcrB82k3UZ37taFTPKLGFzkYhg902BWdRESFYulLgO92UDMRGg6_bOvk2ruvfS5P1LdvCaofLggtyRpk2yMQEFOTARo2gxChjeOIKzO4O-N3Bjn2r3qYQjNkteP4ztTH7OGDn5IFGAzjaUxr7z-trZvflQBvJNvy706S-6vdLUZAAtKnnjuaHUxVhosoNzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGnWgg5GP1pAM3lzzo_IrAiDWnRThriQZKY9f7zONxGtss86rg-eP4Sx_CPsX-PQDhzE6Kcwf-iYc3ZZh58cwnkH8iqZZkiIrm_QBs2_upqhoHFeq088_Og3AAds1b5qu9N6zkje37Y3jwmJpmMJ1p5qBT9YVV6lPy3VQaTUtpP5Nr0W5YcKSFKncUHu5O2PxulhsJdANgL1OTUJDDmzF7PxFJxOG5WpBJkWZrMRuZiOqA1ScxWj0B4U3zR1P4NArG9q3IBf3ndunQ6xx8oYgNCytNXxssMsiHnbDlWcx4vRaqqO02xuPzpnsk0YpJZ8fIMB9nyZndTS5BSCtnSomw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=Y3xqlK7U9DCVLzeOHvPvqXWGKi7m28-ROHtiN9qFnuCaM22_bln7iSt6bNOAa7YTtN0WegZTse91GZR9dASSoQhYEosPdSD_ZN93BREP61dbcPWfq8wmhxgyClQYbnM3DnNHA_cuPTd_sw_kL305WR0y5CP9tSLFxbZbCiGYY4k09xfTOswT1d7PsX1FpXbSneZjUpaa3AbOToDrKjtN5899RKZmBHQG7kAuSPp5JFp6I2neLswqzzQCrukshAnugeGm2Y8UzsalPHTpB6B8PIjnIbKSVKKjsadePRQh7_O-MbKzsxK8lEh9FZlX4KD_gkqJTeQ9MhfmXAjvc1O8WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=Y3xqlK7U9DCVLzeOHvPvqXWGKi7m28-ROHtiN9qFnuCaM22_bln7iSt6bNOAa7YTtN0WegZTse91GZR9dASSoQhYEosPdSD_ZN93BREP61dbcPWfq8wmhxgyClQYbnM3DnNHA_cuPTd_sw_kL305WR0y5CP9tSLFxbZbCiGYY4k09xfTOswT1d7PsX1FpXbSneZjUpaa3AbOToDrKjtN5899RKZmBHQG7kAuSPp5JFp6I2neLswqzzQCrukshAnugeGm2Y8UzsalPHTpB6B8PIjnIbKSVKKjsadePRQh7_O-MbKzsxK8lEh9FZlX4KD_gkqJTeQ9MhfmXAjvc1O8WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=CdJlwp_OGQYZ-mpWjScNmK7gNM-vgHe2OtAZYObPqj8Bbnh_iIBczlm4WiZbaHLV3fDNP39SUCEuZQiFg4TvUz2JC95XfDOMmKY903Ws_3TWphrWBrhTYDzohonM9a3CJfuQKwoCeOvJr3rJzMzj5YhpFqYbWxGnJVHkAe62EmTdXKR-fp77q1y_45QVqJP2z1-TJtb8t9KF21NOPiMZ4eiSR7tPF76BQsx9fsx5ZovhJmuRBKKPu9qDt7ZgZP26i34IYG2BXanQ8FN6ohaZCyPY8ZF7NJ4ar1vPG2l-fkqe2hWD35pEBmRTLpAWc5ZT0cFlfTNf-KCkpx8XZBHTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=CdJlwp_OGQYZ-mpWjScNmK7gNM-vgHe2OtAZYObPqj8Bbnh_iIBczlm4WiZbaHLV3fDNP39SUCEuZQiFg4TvUz2JC95XfDOMmKY903Ws_3TWphrWBrhTYDzohonM9a3CJfuQKwoCeOvJr3rJzMzj5YhpFqYbWxGnJVHkAe62EmTdXKR-fp77q1y_45QVqJP2z1-TJtb8t9KF21NOPiMZ4eiSR7tPF76BQsx9fsx5ZovhJmuRBKKPu9qDt7ZgZP26i34IYG2BXanQ8FN6ohaZCyPY8ZF7NJ4ar1vPG2l-fkqe2hWD35pEBmRTLpAWc5ZT0cFlfTNf-KCkpx8XZBHTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=n6lssOoHkWGow3FJxD9TKLocKWDUROJAyqN3hk3a06TmztPezJ8wrKqG47MXRF3F_Hwe8fUldp1XmKQs_LcLokka0njp4ao4mIbO_ww8Y6Bb86xSBCb5LVS-53tIUQYTKA0v1v4ncTPKBNTi6NWvGHhFAZLrIG8tgiuLW3uSEkPwtRlZb1HvIT03Oc9HkU7i_SB0DKhUO_Ns7PkTu0fHnI7wHtev7aEAhUEuVDXX1kuP45fLtC_Ic9imZbXUBRBRb1a8fTY9rvEgN3E4gUuVv2mYlLZ4pC4ft6jLiT0C3agHIN4HpcPf69mahHS4qIc_yvvrOuvHL6nAJrv-usgq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=n6lssOoHkWGow3FJxD9TKLocKWDUROJAyqN3hk3a06TmztPezJ8wrKqG47MXRF3F_Hwe8fUldp1XmKQs_LcLokka0njp4ao4mIbO_ww8Y6Bb86xSBCb5LVS-53tIUQYTKA0v1v4ncTPKBNTi6NWvGHhFAZLrIG8tgiuLW3uSEkPwtRlZb1HvIT03Oc9HkU7i_SB0DKhUO_Ns7PkTu0fHnI7wHtev7aEAhUEuVDXX1kuP45fLtC_Ic9imZbXUBRBRb1a8fTY9rvEgN3E4gUuVv2mYlLZ4pC4ft6jLiT0C3agHIN4HpcPf69mahHS4qIc_yvvrOuvHL6nAJrv-usgq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLJI-4lgTB7FwVK4bvVP0fudE7A1e4LH5O6AYxz7a9J15vC5Ym9r4ztpQiLwyd8PXdzpFkr3CaP69eO4gQKQ57G2o4kATGEdB-YLGkfFQ7iYXv6MlppLOmLFnsh184y1ZR4Gwhu1NyH1ted_pB8FMfzU4voFkWW9PIhd7o_Cav8SB8cZJH45WuZYYAcy1HfyCmIzwC4VPVr0F84WLwiT-xxj_JZeYefAgCqi7muijHgvAQ-MX3KI2-TEWrPPM4cUain3z9uCzWbfujb3sBF30fnp_ieNRKXtjbQ5R_MKSnGgHZkIS8ZthuNsyThRp5MazkEgePwZxnBkFXTJf_-mNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=VF069xdfQ3eyNwyACq9gb34PNwlMsKDbxNZdFt5plIPOAKdsNPGKR0XFbr2Z9lt6sANnZZU7EmFbdwF81KXEqpHT9gl5v2EM-IA57x6BITc6EPeV8E4bPpU90IESp_MrRRXHx0LUArGKvpKoULi-kM1XibObJDlDiTsxGQiPH7XxTR29MCYBmrbz3rwuUHd0_WNiFEiJTpK8DnYPHUDz2JethbPHI2DSdM_MsFitd9_mf05cNaPipYFeWE4Tx3TEPUJL_o2NuPsXtJHOjVoPbuyvKnrEW9cQdLRSAtLSXI9VyJ9-ToUtHx4yWbfGKZF6DGGQSgjzxwgCz8UI9FgX9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=VF069xdfQ3eyNwyACq9gb34PNwlMsKDbxNZdFt5plIPOAKdsNPGKR0XFbr2Z9lt6sANnZZU7EmFbdwF81KXEqpHT9gl5v2EM-IA57x6BITc6EPeV8E4bPpU90IESp_MrRRXHx0LUArGKvpKoULi-kM1XibObJDlDiTsxGQiPH7XxTR29MCYBmrbz3rwuUHd0_WNiFEiJTpK8DnYPHUDz2JethbPHI2DSdM_MsFitd9_mf05cNaPipYFeWE4Tx3TEPUJL_o2NuPsXtJHOjVoPbuyvKnrEW9cQdLRSAtLSXI9VyJ9-ToUtHx4yWbfGKZF6DGGQSgjzxwgCz8UI9FgX9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=Acu58TXxi2R7TMMwDIX7a3ySx_u2atu4BiQQp4LfzrEkGF-Z1hgFMrTeMHQh5UkAd8q6aNP2uOTJuSFGaBVAJX99rA25VRL7EzLOAXADs50a8yP0VM5uteDoF1UfDyyo9_yKVYFB_TPieYYQIvDvOgMdrDoxBgrAAaqUaXRUzvOmVz3p_kx5tBGl2syCQPZJHsQstoNqLjyJlrdm1FeaaArxePVVxDQp8tU2oDj64px0YZ-m2iX-vL7NUNJR73dDQ0WrjP7D_84ZvKxZifsd68GHFE2G8YmjTwaKGm3EhYhGwcY9vJy9Ljzi5q3xCwcv3yLplARsT3vAo2waM1DlHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=Acu58TXxi2R7TMMwDIX7a3ySx_u2atu4BiQQp4LfzrEkGF-Z1hgFMrTeMHQh5UkAd8q6aNP2uOTJuSFGaBVAJX99rA25VRL7EzLOAXADs50a8yP0VM5uteDoF1UfDyyo9_yKVYFB_TPieYYQIvDvOgMdrDoxBgrAAaqUaXRUzvOmVz3p_kx5tBGl2syCQPZJHsQstoNqLjyJlrdm1FeaaArxePVVxDQp8tU2oDj64px0YZ-m2iX-vL7NUNJR73dDQ0WrjP7D_84ZvKxZifsd68GHFE2G8YmjTwaKGm3EhYhGwcY9vJy9Ljzi5q3xCwcv3yLplARsT3vAo2waM1DlHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0aMtGBRoZb3YiKz6oTgKVMuWqEtdsfCkuA23TlOSs8YT4bkAEK9jxM3WZ2-sCXp_2G2p3oVDtRIqGXyIweuIAK5Cp7cwc-PL5z4OBRfmUjki0L2kEReOOCWWmBSpt2dcVlwrOByDLNTdoTsmcwWYr9Jct9YeBEpUIhGnprURj0mLiGXxRnd7yW8k5Eaze3lwJKwrAROr5_QOsn9uw0OErdWa2Ebd4YBQdskE7aMQPCrSKZ3LBGLXwAk26wQmUwlVjn9XYBU2PrCR4dvHAVs__eYb8Cq0nk-CEGozJhyNvLOcmqK5RXSXgrPr0ntUaRqj7V1CiK1wWoUqzNOv8iKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRRfwExvMAMqqRvyG35HAPVXXZYxtf3mraghsPZZFYcAoRZTtAc_T83RmOz3b8VXH9IrTmdeofqNdduOFfY9jPkI2d_xQ8-eS0CBenOfATSDxwRW1oY7rEitWJ3DAI5aKD6HumjZiHamFpGANSMMj9Rv9_B1Ii2h-fAfEdx_Rfy0ZBYHOmaq8dFzrmUZNRcdRYZw2bTWRpzftGw_5jHoluDBvWu--3vAMnuRH4r2ZtXwmSmcKfqPXjeL05OhLYzbXFOiGFhwHKx6MISxWWHs2pFxkPxvpS7Z_NwPZ8gNVNTwHV5rYmmpz_LT57nT0Z5KyByS0dQCKqpB6sV3kQBcKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
