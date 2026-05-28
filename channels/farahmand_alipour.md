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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 03:17:43</div>
<hr>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=A-wg9iGdavXIKXH-GzzucsFrjgg06Jjpx8mBzToC_oL4F3V01tkNXNWl9dnLwgJoXXA6ChLvj6fLqf5n5ll47EclryC61O6m0hCBcIB8hvAl4r8lQ_stEmIvLQONvudJGzBxKUlacArDGDcpcKS5-3R63_Gr6gBFibEQYi1VBU5vJgWDf5WCCvoXAFklod9qc6blzwxU34_dN2q4nKfbHuDwn0MCjr-RRN6rFoNh9bPxDpfqbbe6s3cwYhbXpPJrJOpugK96QxkU7ACGmeUi4iI0Txnk18VV9mYlIQmbngwWSC_zD36HZpyHO__aWOzwbe671lDv7DPP4DIm_vTzZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=A-wg9iGdavXIKXH-GzzucsFrjgg06Jjpx8mBzToC_oL4F3V01tkNXNWl9dnLwgJoXXA6ChLvj6fLqf5n5ll47EclryC61O6m0hCBcIB8hvAl4r8lQ_stEmIvLQONvudJGzBxKUlacArDGDcpcKS5-3R63_Gr6gBFibEQYi1VBU5vJgWDf5WCCvoXAFklod9qc6blzwxU34_dN2q4nKfbHuDwn0MCjr-RRN6rFoNh9bPxDpfqbbe6s3cwYhbXpPJrJOpugK96QxkU7ACGmeUi4iI0Txnk18VV9mYlIQmbngwWSC_zD36HZpyHO__aWOzwbe671lDv7DPP4DIm_vTzZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Y0nxJqA_NlJ1R3Ob-O2hqy9G6GITVzImM2R76mRjkrJMl9BFohc-Nps8H6tRE4Nn83lGxG5nRO4hyOiefZ0ZGgZaN2VGdJkQKCubx8ChLttI5AQeeokS8SMtHfNJhIj6yqqhvRW2p_NBKbaFMn54mSRbxUbBnEdY2WsvzJ3_9u27vHLHxIoC0vtfFG-ryID5IdkQD0fdcwH-kJza8DhXH-nk5KHB1YWe6wtbSnkQs-Uxh6wLPX5KHPtst03w9ypxSQl71QE5e4lfR28gztcGF7iRzxqavrUrk096N888S6wPLQE4e1qSULjK3JvSWNeducYu_hJdFCdvaINGPiXbHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Y0nxJqA_NlJ1R3Ob-O2hqy9G6GITVzImM2R76mRjkrJMl9BFohc-Nps8H6tRE4Nn83lGxG5nRO4hyOiefZ0ZGgZaN2VGdJkQKCubx8ChLttI5AQeeokS8SMtHfNJhIj6yqqhvRW2p_NBKbaFMn54mSRbxUbBnEdY2WsvzJ3_9u27vHLHxIoC0vtfFG-ryID5IdkQD0fdcwH-kJza8DhXH-nk5KHB1YWe6wtbSnkQs-Uxh6wLPX5KHPtst03w9ypxSQl71QE5e4lfR28gztcGF7iRzxqavrUrk096N888S6wPLQE4e1qSULjK3JvSWNeducYu_hJdFCdvaINGPiXbHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edbt87X-xpZjrPqv2Rcm23gD39bSlkA0hUDky6JxRlwfDQvcInzBhm5lzKTmzR9loh9ExVethoIwZzcdeltJIef6MlG78i3xo7oAw-YCKhJEzvvk1K7i0Y9xDvI-Tiyd6vbZBfhqBtStOT_2L3faYks1D6qrL3TK-hOKbChwFqlmrbqyYVn6cR0w2JSZ59nGBXl24DS9QHsGbddtH17UGXVdaJaGNhmMmCTz6zoHrqT_LE7tgtpAa0cx_DNs54q2KKE37vKOsrdRPud2GRvzGiyUaHDzo3lp3OyF22ptyHCaJ3k3kA78sKDQXci7o26d_6_XeKnoLEwaAs6R7xhnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Kamsb2-u7jEVPLxiN2ZXRjgHqbC_p6Vr4D9PYsgrmq84Z-BQ4mxZRbdnDxVfAlw_jm8-MDXwwKB9zSgxLAkGEkDZOsN7UMTuPpgt0y3rKnPVV_otiwF7SNmN-ZRgaBc3Y8ZPZ6dCguBWoyM7nhJZnv7JYT5vvpLoI360TFS-kzOugG8DuruPT3SmjBBTjqDGQEEpZZsIDe4xVpxRKXXLSUyVfDQf1KUtFHFChe9eskswFW51_HXhrxEFiOA4Qy9UtxG_47xoFJ7q4SfGomUZQXdYbsDyVdx-ixnBCpcHhcMnyZahFmhcN84-HSe2TbwMMN5QCAta9V6x312JKmYQ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Kamsb2-u7jEVPLxiN2ZXRjgHqbC_p6Vr4D9PYsgrmq84Z-BQ4mxZRbdnDxVfAlw_jm8-MDXwwKB9zSgxLAkGEkDZOsN7UMTuPpgt0y3rKnPVV_otiwF7SNmN-ZRgaBc3Y8ZPZ6dCguBWoyM7nhJZnv7JYT5vvpLoI360TFS-kzOugG8DuruPT3SmjBBTjqDGQEEpZZsIDe4xVpxRKXXLSUyVfDQf1KUtFHFChe9eskswFW51_HXhrxEFiOA4Qy9UtxG_47xoFJ7q4SfGomUZQXdYbsDyVdx-ixnBCpcHhcMnyZahFmhcN84-HSe2TbwMMN5QCAta9V6x312JKmYQ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMeB-HsSjq2YMMHj5WyeZ6XnGy7ZmrVuSAOhAM4FBXmvPJ31JMCmlFSo_g-xT84MunDxCSgvEi0Xap3R8kzA1GscHwstWvFVfvFgdrp0tgI04lYEakY9Hyx78YJPAYOMAtRKl6740QQPJIbCHi_3D6-INOrirnBbbikTBWOW7Ygu2jqD8uVCp_tvljvTIAXdzYjpDjhgQp4GPvpKkx6d9PA5tdSRMb34ORI9dSHZWiu6e2aFEOElHp9tyON6o3YdabSABBgZNIbOFa2r0GRWTmD-NoUpWekg3GRcHIOGcZ9LYo_kBLuaNJadHtOVjSHSr5Ozh6ytlBufI3SM-gNK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkJ8CHRFBAWvEd2TAQAYZNpShabxRdJcaVbVVKakRuLNuHK2DedtIWLLwmYCixnkjt4-jSUWhFY2j9vPWKqWrK5Pvy46abVT16XsIYLcftttkK9SVPywPUeWvYSxvqatp8PmsXt6BDnj3mZIOe7iDjS0onR30hQ_0HAgDS2DHkoFI2JwWhUcvbPI6Q11MP2A9aUbWERdSbwd6P_m-h_nofwmtf8OA_rBFy-zIB_5YaRTOQO1NRkzogoCQ_Atc9CFk9RU5hbvZaPFYcwOVYJ2XdCypTFmLHRzXaaQuZYbnHDUSLvVSt0Ge5GwK1epHs-08HWUw690B0tBmBBkK7K5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTX7abO_HBWQHB5OHCn8fQ0fVF5Qt47vGKBs4RZ-ymc9Xv0K0QuIbbghgvxfHtzGWNJuRXDgQ3AFpJ_uZVZMndKziOMAWkDrw6vEBI83EWi9vH0nPHW5V2lhwLkbB82jiV0SZKtiw-R7ycJCQRGKa2Y1qFfJHmh7oFsqvks_oAwQE-U8LcZRohEvA32P6e_79MdC48q0pVHlklseHPmR6qN-anF14e5SCY9kmxxE2hUsjNcaLUbta1w4JWIcjw2LrPWombTlfStTNIndvcpF5_Ce2ZDzAA1eozhEg51-9exRYnkrkmWC-SbC4eLXDQY28whBgv0FcbmdkOhb-0ukWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8omnbdlXorNlxVYpRAuo6P7rfCZcbQPZEHGoSaLRJyF2ozz9KVqz81ERap1vzQBCNbgalcoj-SExDRR5549WKas3P4RArERIjYTC_u_DFcyu8jZDGyZOPtiuKDuDzzO0JyJrqPHIAGO7nrog8ak614KlurVqZV7fNgfPR__MlYjCdxMe-LoP4U1Gv-3q4HanIe0LbLsBnHtcw82KMIDop7Y2qgGiFBIicGrjWyJjSEZCVsqGiheHY5WQRvd4BTFlBE7g_RzkKIlCBawDF4FlXGbxToD6oXfW5n3t-I9IamhRrhRQw8RtM8EufMYhg8s1aMOkRPn2dqYFypSidPIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijEOeEETvZ-GNeuJElr77oI-Lwvk3-SY9nS83vxHkdCfr2BRgTQudXsrfPxneQhZwvKyROyidOnBgdyZ1n4FmC8k7rUK-jceWdiASxp5rq_MQa6BvwZIrezlZnPVJmjDuUgffd8QJOBrEL13k0d2OmPibQEOIK5kYWcpe0Qmj6TTFpZt5Rh_gFr18ZCByLffJ_O1KuMPvycWm0OmO0ayLdKjI3s8xf0yJCwE6uvESsy_43fHu0Zad72LQlgsZGFggPMOa-4A_2L8Q1-DOPi8yQSpX24_7yWf8bc501UKCh9UZy9DgkyT7COxgiYvj99Hcep8WvZ-IUMXa_UUeUyU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vknurSUj5MKClQsp4e9AqoBwUsqXu8sqRxI85EzmfpvHX0nkezi34cfC99d7CUYTRCL2nhK9xgmnSedZI6qPPqqbBUDfOBthbiHKjLlW2Kf-HjLXVTughig2xolNUhOiB2riv1H2jcmGRWg7sy_sFDC4exoPFmlpEz3IlCgpcYMk9ZAhEUBHb3DlJoV2W5YPC19FyvURheZy3rp3q8c2RJDBHzd7jPw6KBrVkx_bEL430DHCXg3pnd03thWphZo6qyDG3yZ6SBCPi-42sS6J8cfOFGTAgv_hn2AmlGh7EB6Rz_srLI2JMVwwhjbe8UqwpcM7djQvbde5Oh1nAjM1BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIDPvvCBsjwjzytJq0K8TavZNpU8bC1pt0knmRzaJGx7dng290phOpqudGh8jeYaNsrY8qqjdBQGTNjott-pzjtcOJt2a4zJN1M8zZCTnrja3992PgC04oqkVZJ8XDqihSzAurqnfetKG_asgPPIn1v8b9ZxYr-DefXv7LZGtr4z9Kr_E5hLB7TtvYkqURaKSOn1Ye4Alf4ToYCO9EIlBhpB2iypOGOPNcSbDDv3xMAEvWfre64Md1ONOiftIr9ynFJvQrWy-5JNxPhF9JtZxbbxWOlHSE5wl44KC7bwd8iIF6YuN-AA-GNeOEj0UCseGU9s7kkHo0KGe3vGFfY9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEkigqJru6t8eAsa9XFD5llNiFJXEIV8OEhCIWu3AWl5wg_nqMK3Va1jX7dxAIVUP8Ly9L2tL_dA8fXyDw1gF9sPvQNwJQfIIaumnqnEHL5ASo4NO9dd8vWbW-Qdxahc8vXw5nnDOaNwEORW0mCKmTCmOLlr-UPI5GtJlpkNeHSgBZ1QAaOx7wGSQeZLN4-RmSyDlcQkRGdqGDCyOFQlIPFPYjL9OA7fuMXWefZqFANS-Efe3Ku1TVpDEf6ooh3CKdcSQhgM8UXJrSHhFqqUFmyqNv96nqOdj_rO6SletRXBAedpom-WeR3rkIvq77Pq0LrWHpBNtG7m2fjUjE6W_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK9CC5T_AMRC8TxCBrWsYjvKnoZ-sm36fkc2FAaDPkhp9l6L1XCEAsNgdaBy9Gh_VIAXTYJzQZiPPBkN-1zGi6Si1_jrzORrYUgwwVw36vl99bbsD11J4FtVahmD7Nbr3Jh4brOeMgh3m5WN2bnWhBjq9vCmNDVzEeiucdraQxFfJPDI_588LeJ2tsGYZArOQVMYDyoeb0XPTBNgwci4v2ovp75fVCTt7kpWrOfaWg7AZW-S6kDPVdNUqHEGZMVgTAjTynvFAwrThoaESNSN9zuVJ0UKZEaE9jU4uUhbhLaBZwtFN0pSFXPJ5AOV8QkhHaGRTM4KGATMNzr4dsJNOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRSmM73Kj-8OBb8MALhQ6Rz6f6msPqh2uhrVGT5nkFkDn11L3iNstf8tXKEa0YU-yM8JPxBwBHMk_bX2b6gd5jFyT356-chLca9c1h-CyDdN-zR4gqGI_oyPp-RFpi0yLMrBNUpPlyGsWUcRGoy29_eU3a4cex58B6da2kHIi526LvVh5P5rPUNNgEOFwxeUow3SujSvbh_BZmsvCn_37hQY4MiRTQhXssp1678LziXwBzGZTwHVRb4OjLL7370hVod1IUP1NmTWnQp_kQkYj_a6xbIA_381TrZtmWRDQ-oG_YuzwDuoTyYrVNCjEXY91NIbVi_DDtGIp-2Q5wgIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2RkraEHa9iDtLluVC9ZoxyItZ85yH13KhiOeQO6J7XAUQS0eVko6hfaAUtPw5FyqptrHhWbp4nQnF7ntcY9DwyUf7CGBvWaHy6KN5t1tOxAeyTDeuO_yRbzchuxziQ2tIsCZTFihT-J__-6GZ67HwCMnzCQQdmRezcuowpRfjS6ht-2XHSpHIcVJQcsWYEnwp1szVe9wNJsl6vs2VbG3w5oQf0miUlopeW3u1MaaH-TyFWcRn3Gfu14cY6HkPqyDAoa31Y620rtmmaeJk24GSjxubLaozcbNEo9rt50z0cXuO3jLorjc_AlGHIbmNMt2dOh7HzAnF_48isGoLxCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwp4BHv33LsIm_UhCqQbT37o4Ai3x4fBS5NsU_I5SBfT-bWYsxMjFHA_cSEoQ2XtmaEsbPnwXyMIVK5SJL6V2m8Ij4yOBw22y-qZ2SL808eVr9UspFJNuCz8nv-6ntRb5WFOh0C5RiDZuUkezt9eoGCcubLfFr3NZpzBTYiQWva9QU-NS_dgKm-4Mvwcqseu6qKGVbsdxc3tN9YWcE12RpdkC42-oP58CNarY42ngXGb2xnZi4xngT0SoW5s9IzXi0VMmRV04cGyVLJHedQYI8uUr_-T_kMrkMDlsagszp1KDfxI0yJzdYuS6gApMTac0o6XxI6JW01TAQGsLqGWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSROtDQZdryyDb4sJp0IV74ZTmt5W2K34q0cks2UhffLvJrLYqdjaYL1BXrDqdtAXfQeOXE82IgHvQSJRikL_Kdg7VJAvRmMDsiCdv1ff2ZzHK0ORmJW_2tARHU6NP4c4-lenfVmCZwUk_PIvaIgEEz4X5oyJtNF7NbnleyJepEFo7TTPZHoMThXsawkX9r2aC_2ZRNW3y7_LOQ3WqCKYh90fH6iW6Qe2dobv6YfdwgwFdcBWZJeeDBEWeMP4x0Cqoyo1BSYQAh84LyGWsuC4xh93-egcpWbydQPsuO5PPiIyLqH9HGmJ5PVL7ElgYEaMrYiNGki-C3qJ116xWVltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok6aGbgItrCio1xho6-znEV_LNuYKr2LSUbA2ur0upVw8OG_AFXV_p4-6idAEgaxOyGVAEGBu8b3HPTqvgQq4WrX6UGMkpaQyh8K5Mk42u0heEbhADXg2ZCDNWdrAe3Juk8BwVEiZvNjJGO6Oo9zSdgteLXvAnNhirSIPvs0u-dMjweUXFIziM56zl3HmZHi63M78vt7XCl6X7vJHXNQbFkvuUFOHkHR516taAGSVw70DBRwPUsuIBKh5u-UFCOII1n7_7YBidKuNURFsXNCNpvBny0JzWWZsbrWlYsYjNZD-ufg1Z8WCjanqnf0pFrhshL5GEXbS7vZHxGJf6ioYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=V1nqyVL-IiqLPvnN96yo4HbV98D-PH3msFuAYZSEDv0ECZSo9KhsoPwVHsgRztl308NfZPFLHmRisJnPGUu5xIgHExCV_KIE9cAk8gUl8LgLh-h1SbwPoX3Iwo6SEWp3vemhiS_WPY8nKoUxyQpiz0IpkgRcGG50svr4m5kQ9RPguHAk2IX-8TmzIOu2oykA1Weaw4btq8VnI6e4Wp0AqfVDqx0-a11jY3k6QLgehNSOCRlPMweiVjXoP_9Lgdz9WnyJ24KSCrRz3PcbxlqoczsX-fAegJqSjVKsYyYkGLQ1x-q3tsrLsHPSuHd_XuM0sgu5Xl5MsWCr9A01ozg2Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=V1nqyVL-IiqLPvnN96yo4HbV98D-PH3msFuAYZSEDv0ECZSo9KhsoPwVHsgRztl308NfZPFLHmRisJnPGUu5xIgHExCV_KIE9cAk8gUl8LgLh-h1SbwPoX3Iwo6SEWp3vemhiS_WPY8nKoUxyQpiz0IpkgRcGG50svr4m5kQ9RPguHAk2IX-8TmzIOu2oykA1Weaw4btq8VnI6e4Wp0AqfVDqx0-a11jY3k6QLgehNSOCRlPMweiVjXoP_9Lgdz9WnyJ24KSCrRz3PcbxlqoczsX-fAegJqSjVKsYyYkGLQ1x-q3tsrLsHPSuHd_XuM0sgu5Xl5MsWCr9A01ozg2Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tztSO0ZxnhSnvHXm5CAxUHjtjFFcM3e-OS-4ZMBUZNlSpdYzJD1k_I6VmcvUypVSMVlyLA48miucP8hFnjiXmDdNSqyufClYbyt_b-nIKXqMOQM7csZDi2nZfhkj2EBXLPTtubyQHO7jGNSsccq6fnMTMuWzrCX_sj9KSAXJsLu5nHEb8PeYufmor1bzEsdUAhy0qLpIJ1TxtUEnG1FfdbMmGZydM_p8LKg3LMIgblIHc8plyQlgL7rm49TP2EgJSPvM-Lk0e4bL1-Um8QkzupjuOc_w7Zahj1N-xbkAgVJhLVOfjm9Yd0sRZsjuGrAfT_GF-EGNlnzDPQyeqCAY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJXAdorZJkNculg06zPanPuch7o_63wKuPAhBL2AAvy6Cn7E58TYzVAEUhgdqVptOrlimdSzXQyR5hJirLK9GtW7bvKTeDp6-tSIr6xVCK87E1gjeuYKuvUFtZTwHll1S005EHfrhFzVHqDGYYru3mRYkqqLw6ee4uzigLpYKxtM7CQxUyRFwOmij4GgnnycKSBXsKvuvZmmnHilpam-aqaeTox5TRll8zPDLqVPcEjmz8vt4VLyjTj0tFctt06YfVpho5NuEwHl981PER3w4u6neKv51ystOI_CXPyampexAeCPOSejFWXlYM3_nc_6OLMC0cO7UV1ONq1SfK3eLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIyF6QhWlryEy_TgbIz2GiW6DgsFK6wWcL_sktwDGsC6yjbYVzsnwK5c2AW-sm4yXMyAaegDp6yEaTocudmzbBioVonI1X8u3Nv5QB1EeXKT7oqLS_fFd8siZHH20S53AGL2sb30asNS4_thvBJrZeMJfDCR87F9kBMpcjIoy2V1oxgtRvRnyGpeoGSFPCvqNF4Sg1ktOCgDGs6_vcLTQELpH3RaWzZzgm4twJE9iKTDiZWzQaqWvMU0vr1MwfN-o6e4cx6zePd5jRe0dvzA7Jl--H6rHm2E3EmnKHqyhZPyRfbqIFs6waVXa9Cbiaq4s2YwJS1oprlLB3Opn05sZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_3_cCwcBPDqu3aSOMD9RoOffGfz-ioS8HswjX2IygpP_oFGwbOEMD6OvIuyERHkl28e3nBRLr5UycIIvNDX4Ob7Tm_9yEis-DLtkyZUmzEyoLa2lLMCGQLBwSTwaEDgtUye43MwhfS0NIrYNGXs3m_TAtzo8LbfiD16HVOUYNuN-qfHV3iU0JAg4E16HoZQSS7WizxgmPdZJ_ymAqJ9hwBxFRQVKwse86FUrehvF6sAb7c0W4ad-A45AlcxE_Q4djNCCnRy6HDeojERDnKnv8ve7LHV7Z5UUO4cp9Ds7NJN2ok5p5-DZiDHAo_p3HrpuGPPgty8bh9hIhiNZL15ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAt6faSl49Z_J07fhaSB8It9kqOYoSXsMCnHrPXPttA_zObvxijhwqQrhJpus4Yt-i1_SeSrlV5aGmOrgMcHNxabc68RP2xnZHQoQvNSzcCBjOkeHBEoG1i4g7a4clqops-LlzQcFWpK8EUy91xt9cqw7JEcJutIefj3LpBF-iF-2R1GWIC_N9qCTWOvcyBZQ-y1K3YwtOk_2vMuEH4ZZKqh2pgNE8ySwuAcMHJEgrQl47RBvLnBhzNHXQuReEF_Y_89a8D56kCC7_ct1ZN8jQKn8AAN9RRsHG0kB3e-uv0bHvd5eDCPwVasxXyMc2mXLUA6nFSPNxSKGQMo7rzrrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWQ6QzsOMepRpDeJOO1hyVrMd3-qgBrxmVxIf5vAWbg5a1mrOxLOP2fbpaBb-hUYGXn2k3A3RQerAGMPL2pTt-TFqSHAEdzI7NVC_BtvoR2GBBVVc-1C3f8ZLkkgrm7h0ZFZ8TnyAADKurbpaV4n4kwy1y5yuCmt8bOciTHkq9N4UsrII9OQvLHZtgg55HJEdYJIQv4zcQ__7oC-VGXnkATbfkBEQNoxbB6VSSfph-yT1BUDGlnXkIDVHWBc1-eYacPNocF6ASNcGkY0UaT3IbQJhi3MrHM-v5e8OPFYkeKCseEPtZAmruW6DAK--s8w7UUxWKJy2ZZhoL9hP8PJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twYbwthu0t80fqR6IzypIJ6hySnwax7pMCV8YE8jkZkQzEfrGSAM4jvd68IH2hTHRCo2LdvT9-AipGaAuLu9rf-v-gKxtclQvorB0kWm6p3uFNk-r4QnctNFNVN5g9x_TYOCSQ110ePPAkh-wU-J2ZeTv8DipnetgwDjt_pJPwfytk0fDdzjbVP5BcsZOMC9jEKF5fGt2t-38H-TZPYtF8w9DVEWCrK0E4a6R2IcJ88igDkti9tp1tFVztc31fKfwM91EihBpIPE7Ey_OgY0k5-1ZCzK1slTFUoltrKjJQOvQxsIQaZc4f8P6aK8qsgU0KSDhQnIQzg0b1IpKlPyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwRTzQ8Na0tm1MJ7YZkuLxyxK6-iR023BBV1EUWtFeFyViiQslSmzU9Eguc7ERRL67aRSm1-nMnBsyhFzJGWbPthKXo2Y2uMIQB_S9wOzGCj9qTAtGCmrxYkP38vGoa-AsWwzo54rcnolaUy6a4HIJq0-AFjMerjC_zoCXdhozE5kjtLEw30hsiWSdyvQ2MvIMKwvJdZ5Brgy-Iu0QLnXBqPJWvbFKF2H5omCjfALnCT2DjjMyMFegS8Aq7cosGhlmR9cnXH9WjRmPpqcQ6pMuWuLyyLO3fZWQ7ece7BkfN6fUBZ2sSvsowZH8TvRqOuPpd6kenLYaIAF1yAFc0YJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZGEhc4e-WlOQN7MdGUOKrvxiAiLHLsp9wvpuX3fiAzFO6Xa-MQULAHNResuVgUrMk2SxGCsLyv3qg6BkbVUnLQLfD4EUJSryrzYW6RHEhZ-5JtsvN7tyMJeVPbpMmWzX5BYus7Z1gieJ9kvT4HW8vldy6dkR0CglMLxqgByWrlWZrP8kKd0-evQVaeTfpUn-Jk6-xMB7XjpW8_IebMN11MfpdQLDQE4HFGSTcBENYG0smUtKwybFuXcLJ49CRyvweCHZGsPYhX8UROruAk7M7w-cWeXy-eryaECyFbKEuRYiRCgH4ZuCd2X50ne-GbiW4X-Tgy4iwy3D4VJ9sWy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hm7OD3NqwVtBD2-9VIyIInOi20BjljBwP2JMQxtSIf6QAOKy4kDy_nBYyFoV2GKJCy2xG09yv1IhzAwU650qlm3vsjQ_p16rwKW-RG1tvcESDoxWPpzCnrCQ_YAU82hDYTEXs3qyqKGPV47brwUyqvpQQaoMvwF_Tc5JD9C7MXODnFTbjL72NpfiMvxOpAJ4jB10sttZWhWpJQDcMnI9wlKSfGbQ0zhR_Bj-MUR3LzfxxPUfET5nC6SEDdDhxvjdQwU4Ikh37yMhNhZIygSGuU44inDSUD6bYbwmwxPbOF7Dh8n7yvg6tT0DQ2tQXPwQBMG2dYxDKVjympMhT-eIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj47ZuOkDAPkQ4aF-fMxd71X54E4tTRmIPOm0p7-KMIXHGOD6qQHJHCbzLsNE7F-gNK6eFRLnmmOdHRGY_zxKAm95Kc2lc4P9N2VyS52YuZDDMIa0KtPZCFXmynfrr8DJ-fiZzbSeBKJQTUX5Ez-sZpImgijnAtdH8tTXDD8ZncMmwI5HWHQzCfK-RKvGNKeY3tt1BZXoWS5AQlMGWBRzvpHGW6OFhRnIRu9mzk9VZMgtt0od71fZ0bfMU9YQLu4k7nvWOAnGDFjZQ9tkpq_Rvo_4Oj_SdiCGkkomNzxfzV08JHVZL4l80xqjYpipVWXNeRZ7Izkt4zYXuaZCdCl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn5PHoWAoVRsvroLNFIVQWXHM3eiTqcRoe_vUgrXpVhGtkEkozfA2HrLhih-H7rqnYyIUEgmiD4vNY-XngutUQ4qPhlZm6FbZYk6-BJ7v9ETnfbImiYU6A3719gnYPJIwzDZQrmc7ZK2gzvoE9u0c0oi7sFN0hcBjX08yUjy7bxqS7J6Sf87TTbpJyE0x4kSM1SPSJhf61FAKR8j4XFBmXx5yki9rSBZMWvkURsszzGG64WKrUbCvXt4VHFShQ12nK2zaWtx3GuhjDpR2lDO0SgiCp3zDA3eNEg8L5OrkdWKGl03ZkEx3pQgpF8eMlOwMNeQmxIAu_0zM2TkLxFhUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHv29MwEGcSD3KYyrAaNuPP1DVVkWu9lComQwm0HESddX7vD0AnqCOyDSznSxxUVmGiiO4yeAdmqWVPfOmXCaT6NmGeLT600L2GF8T5hhzsK9mHB6qiJiPFXaKZzgBXyGz9UEc8UbSDf9VPtfalRiyZCgiGDTfh5509ZPfyHo9qg5wBdFzhSLTZfACP9A2MgNwtFvwWvbTKwwhENopq8ymK7hZrjOgt58o5UsH0U56pXLS7QBGWhePgdiI6F6nYwXWJkFg7P4Mr_XR9sTinBQyyTro9C7JBtQWnYOwsJSgyWmQ0sLhf82miCt-0Gm62bBgDFgxhV65q7AJ_lygc2Ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=ct18rzYNdteRZmLr78YROJOFYfdaXi55PDt9H0petOvka2Mk0AoJni_KuaYJo1aTpVDnMhbeRFdZsrqxgRBCj_gX3eNAtBQb7G2QC-ccEv_o78IiCzOW1a_vkVy4TBndJRy49k7oTaZI9tB8N17eEMEOZW84loAgHz1jAB1rXXEJSJxE3eTPpv8dDUxK8z49_K5eJ5QU4IdIGDJOfAlxZ5uN94QwcjGam9dE0yfe2rOxBetVzQXANSt1nqpiKlUSNdaQ5kh3z1YeAtKs-Q1I9le18MBJo3dAQRViSwTMlYV3pAxeYYlyaAGvemLK5BW-KBELNr9n2zwGOMhfSk-UOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=ct18rzYNdteRZmLr78YROJOFYfdaXi55PDt9H0petOvka2Mk0AoJni_KuaYJo1aTpVDnMhbeRFdZsrqxgRBCj_gX3eNAtBQb7G2QC-ccEv_o78IiCzOW1a_vkVy4TBndJRy49k7oTaZI9tB8N17eEMEOZW84loAgHz1jAB1rXXEJSJxE3eTPpv8dDUxK8z49_K5eJ5QU4IdIGDJOfAlxZ5uN94QwcjGam9dE0yfe2rOxBetVzQXANSt1nqpiKlUSNdaQ5kh3z1YeAtKs-Q1I9le18MBJo3dAQRViSwTMlYV3pAxeYYlyaAGvemLK5BW-KBELNr9n2zwGOMhfSk-UOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=Am3FRtchjQgKMr2LneYfODKWBdm3VNbi8sldZohHQIRCo__MvHFknPpzZ77A8aPqvReB6vbdusz4K5_2oX321mAzsgd-71E1yTAzSNG-2jilZd5fU6Mi63fEbuuu9C7tT0PJBI-YcW4jorn4VyWxq1nhw9sKb7yQJKyShXzq_0Bhui3IaHgRdTAIyE6cKOCrVfzYiMrrdSdAgw_2YnXNZNhdUUczBaDalb_xcBnm57KzDjAxsCKLDcGjWoIpIWqxYihzLcJWfICAwMOelGG7CMpJR6R-CX3-9siHPpf09aop12Qpeijg6Ipbm4WxwZz7CGVFssu1KAFD-0HkawW-WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=Am3FRtchjQgKMr2LneYfODKWBdm3VNbi8sldZohHQIRCo__MvHFknPpzZ77A8aPqvReB6vbdusz4K5_2oX321mAzsgd-71E1yTAzSNG-2jilZd5fU6Mi63fEbuuu9C7tT0PJBI-YcW4jorn4VyWxq1nhw9sKb7yQJKyShXzq_0Bhui3IaHgRdTAIyE6cKOCrVfzYiMrrdSdAgw_2YnXNZNhdUUczBaDalb_xcBnm57KzDjAxsCKLDcGjWoIpIWqxYihzLcJWfICAwMOelGG7CMpJR6R-CX3-9siHPpf09aop12Qpeijg6Ipbm4WxwZz7CGVFssu1KAFD-0HkawW-WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DH-q-U7zRZsD-8vE6NKW61qIijZcB2oWBLcQexfxplckeFdOzJfG99c2sRuOsDKmxsUa-rglu0NpGJ-SsBrjUDgh1Zxr1UK-dv9xUAlmawaWObgyd6DUrejnE4p383c3M2XAlJf-RwBVJdzQaLdGX4xw0NAuHYrH0nwMXDuzFe7EFaOKmAVfzV7pwP17bPdbVXNAoHBuWByDeW-jWtimHhzSld_fbHWFnA6IaebkeRbVRVw60qlSfKetfyGAtRVJKG4MSPZ3_qYYUzRt43SNVkXKW6sVcjjqvdgrNjguRDoF6Y8PXQcOu28M_1-pFxCKwX2SXkknKYVILlbl7hypKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtrq-fgX3PXLuLXwG2jrLWPV9a6nCcsYjWq_GCi_V3iPlhEiT3ajSglVxf9inEVv8_j60kgm7PgqfdkF4Z7psXJh16vaied-X24hAECLKWpqM2OoxMCjhActBFIgbKbHeo4yHcvV-oqJhiBKYDoT0-ui7fFWU4HbeeujsmPi9nI-DzSojTZPEPzq0CEYNGCTIJ5vgTbBxJ0d930g26kZcUyxE2EhQmMIowVuruDyt0KOP6FmCSp1iaOSH3uXhj1czTHUkVbnIJhbt8E-_YXTfZcHlzYyVFH3n0Dn9cx02oltaV2Ax4W4Hj1yGVSKIuVlxOMWHPAW0ZyFiD43YhdVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5mpZ2YG1FB2IlHnQunyEy-wCkOUmpOkcyg4QyPOol4mUg_l9vyl_lUbhZln-5jQIVo9BrAyONQWHXKGYkNfci33957EfmKmXQydg3fjz4vc9qbxO0PgJ0W4VNkxK0kM5js27ToLNplLYaoxxr07jjhW-f9oyzySFA4l4HkVgim_an2L1LFYlk5sxRkO6PbWPGiSNs8_HOPjmNfM2g2mBtcxhFyJ4RI0CQ6ZwbrD4PfyaIfu-piVv9vQ7vf41zxIcv5oC-cx-t_DpQCmdRveKPBA84FRplIcZjNuv3Ey02aUAIKDFeYwIjuzJFt-Xd6nYGHMQX3pmrDxETjnXctJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=aL4y77TlRtP1oF9NLR8PSvR4I6YIC02HDUFvf-x79FNO7o331JVrbRaIM7CIAuFtoMuP_6BqO2P-_oypkOK_NDAvkhR3LHIdYFWjpDJOr7uJDjsNTHZpT8rNTJr1krB1B9yCaDZ79BLMxGfsj8tqA15giC9hDV9v4YT7Vc1CNEhZ6BCmV-vnlZ1pcwWjOW7LBJL546hAhZ-mnHpPpttdQD5_38vQTZ-tSkNp1Gl3XAI_NkjCLGmdpQMVBoldju_mtwFA7_-bo87OF_gLaVHEyq3scFsbYAo0Y9a5kmuxyvphH85aFXsr1bmzsLatqtheXZHRM17BfedKDyD6Si1VfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=aL4y77TlRtP1oF9NLR8PSvR4I6YIC02HDUFvf-x79FNO7o331JVrbRaIM7CIAuFtoMuP_6BqO2P-_oypkOK_NDAvkhR3LHIdYFWjpDJOr7uJDjsNTHZpT8rNTJr1krB1B9yCaDZ79BLMxGfsj8tqA15giC9hDV9v4YT7Vc1CNEhZ6BCmV-vnlZ1pcwWjOW7LBJL546hAhZ-mnHpPpttdQD5_38vQTZ-tSkNp1Gl3XAI_NkjCLGmdpQMVBoldju_mtwFA7_-bo87OF_gLaVHEyq3scFsbYAo0Y9a5kmuxyvphH85aFXsr1bmzsLatqtheXZHRM17BfedKDyD6Si1VfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU-K3Ho21gMpQxm_9wOVA0P0VqB_Nkw0NzmEKEKA0rRuTlCm0ofa9t9QIfwMOCMktp4GR6MxUi9hFHF56b_4FvmnQR-uzOB5K6n-n0qdMbKwESmB8fhn6ujqLNPscis7sGWjhu-6M-baoK_l4jjkMsWdP-RtzNcCHqDO2IfVUDQp-CEAtPWBj5HHNnD1wb7HTnr3w03XdtTV570JEYS8GCgEuAjqjOEko7ivWAHbh_jcnMeVHZe8P3_SRYNe-eNA6muLmNicDPJa-Z_A-94gr76aiFQN0tziRfrSbDJ3NaXrwgO2URRFK3mxhAtxxNmpacZWxjRVDr0KHaEbHIPIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UG-1h6iAat2Va9D2chK5AqOv580byD6bgJvyD6rcHDTQOlhpwmAWU90Uj3-0UyItwiZiNDCxylxPEHrQ1pn62YLW-6znaHlQu6o-uMyTKJYLPZBjE223JOmBm2RFzC9In0-31pxKZlYnKXSVDAe8UJqBqZDPgGXdk0OSkfuZMOsFNzDImGF-L4_q9si_8BHfzrawYGnd3LCBltqb-PAd0l1PbqMtRTX8JCr0jWW_UgpDs5KH8dn7sDAfRVtE9rZgM0miiMIxHxRlaNON712T_hZjLRROoRSjSK5e4dp7k0OA517DJLJ79w4pVqOuU8uL034ML46XkCnqsF9lrc3zkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3to5P_qEumTdQGsTuVA71c8xP22ZrwMkt8cBfwrlaed7MahXknRVg5IfG76LgdDu0rG98CDpInQYVNXx0UlJ-L91to2PcFOjY6mboJcdxw3uUBMNyL_Y5WuAZ_qX3-K1frA06RuI_I6oT29rnN301hTCq5Coe15rJMUv4H1vtfISUUAJbGLTo9hcb0RmOBwrLAJ6uEsgSCWv8k7l1xxZ3tmmL0yWNyja2y0FNj7hi2PRO_-WhBLAUzPuSN86_-GnJ9x8cGDw0L7G6SfzenTGRthBXoEK8HFYRSJ4pnisAIlPu0MupHJwXo800hiH3re1JypU4KfdR4iW6bay-s8uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZbzrKECAKwMwnQsxlJZrow9sm2AOyxOpkQ0azXnn0DKDN6YY9L4SBzwKeLdhHugFG8u6rQi7FqykDiITXPKIHp62y7u2PeyuQBaeVfGFFzPrM3grdVorx6W5wpJ_OPB94nS_zbSaQovScOjKUNqyRjV258qzrD6UDf4dUsT_ssx4YNjw2JB6vqbzeVDGQm8TMCVxVr74tkBdPLKIDa3LPeK79rOmRGAVmJRfaYw0AXWidqPoXGY4B6vXJwXnPxOVB2IuJ3e2PvUNWAbNy85gdKpDybwc5_QJ0XQtWmyF-l31UcDYcL3fWRxNHzFn_qI_w8x2IlU3eoR5SOPsLy6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rvpul-JqHFCMAjLTd3qAggRLrP8WKJZDIYXS8oZhDy4uBa2W0td-jvD7Aq7MCZY6pASig7fwxcLvMwZHOJA2nPK9dzbEv1yjeSdMTNoBmwn8tiu0LGhPuy_EtLuWU8YmzsGrQqMidm7az555goD7kS3WLEuTSegk0QgLhW-omZrvP5tiisTk5u1aI1piWRQO5jvaRzDjG2tVqc--Mxwb6-V7MV4m7JOSpbUXKocw3xed2me7wbHnHttL4Av0ZBOwinwkDfu3pkt3BKXhsA5VtXhbdAaLkgUyMiUlAFfOiQQScDlCpxyaRj7wI11aU_LbbPJDPcsItCWf6hmQNP8bmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4vsR36jidTkSvVEb3HE7J4Gx6fl_JRorTBJwWQN7Kgc-JKdPpveP19r9MJPEBhsujFDLpKbzzuMYKpTjbcPuTdrfhxrtWU32YHVLXjF7sJDZFbb9LKEN05DiRl7eEC2mPJBRWhV3ufOkClyoygMnAZ0_CE43MzkvsCs-MfwN7LyIMVMVcg40ScvMEL0nijrh1CUIBFx8WoqD_DEzUAfR4b6cS0ReuMzPP7kocEZ52Td3WAjInuj0fCitKeNRTS3Zh3u3ApfXLmv37WKCXM4KbdZJhyql8OmCC6f2JjYz1w4qPdVMf55UHckS2WImtImA9Y4am0ZdySH6ny9HEbjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ma8WrB4EgS3NtFqdgx_VfRcg7vxEeqE3CAGZYoxbnZ0JhZxcgg5W-gdr946YafWUyOsZI5rO0AzmYmhZ_Kd5ekCkIeB1rY-GmIsBl6YFpQBrS2IwD84d5AUUhYyrDMvMeshYstegax0TvQ0yg9KH9ze29EANvd6JL-KOMknXYb19Y3pU4MaWcch49gOPgI69u945jk86ReubQvg2a43_36wxGlXoFcwv-DZvPtQ4GvY8_SWiUAEJM2JE4katfamw_3W6h2xmo8tRYTTnJRaf8tLBJklVPJtNVtsNYOWW6ATti6egdPJ59B_tFwPhFDEU_MQbz_ihih26fqyRq0RF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aevq909TY_dhpyIG3b9HoMZPiTjKbO8I72xW3RVnUjF3JxfuMgCjZ2Z5Vwp7k_fFBQzmQpo0_gjmz0QyAirekNPDBV0hnzuX54vTEQK1bBh0Fl5dEOYZB1rEl3yE2DST6w_IdNitI5M7_1RXhtqmoFC6rNq2Mn2trleLqOK2AF0p9T9XipkoLKy-JtLVhp4zPj6MlYM2i6x9pdHthRMaUH2rzrtiIdhSIylRUu9ytf19eR6ItQSfmL-T7E4ouf6ScgwwWexgDHOY9W0VCGDTh5Har3xWOy1cRhbtpB12BZsOq69f3_W-S9BFLNx5a1iSfrkdGlghL0V47bQoUZ2NlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oN7_9L9Imoi6ZZd4VOVi5WvxRPR0-RcUSdcMu1kHk_g42IuZnrizDneyxK1yv3gVNemIIfUJRxzsR28YYxUHoundK8zDQrVOORKdrtZrjg_WdfMHQgRvrqOdx7XVtoi1o6YAsOiJXb2GfvFvFX77cfs3d0vVaqeYJNYBtd-1nYMHbSWurXkbXM1vEo2OeMsDF_UACWz1H26GkLlXZqp_2btKMziga1FPuZ3jUbSPFJYEe-b4LpfE8FcqsYoMJhciG5pQ_R6SfWFEbBZTE1C05qjxe8pfLpzFWNaeA2oGEO_uRuw8b6xKgEN_SqygyWy7MH8xvsSJx71bWuVnj7C-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlVy6WAt8BQhHNsKchzRydEqLpkbfoB_W2E7ELZOO7SDH8bqrubmXtoAv8M3FCy0MxcyVdQg4KuUHrdHljOv82GMP4Q2B79XCGDlieRTnikDKE1cO7LmnMkW7SeSW0rw5mpNZIHvc0x4uV-x2H9UOcZiNGBL-tHMUowi6UUwwFaC6bx3FFZ2QN506LF0RCTNVKHgLE2ryu7x25OHKdh7PzGgiKpWNLkpNBTgQiXaakP-9-l7TB4Wi5KbHzNIhsNScrfueuwkBMiCmVblaWQTzo6DULxkMFgJx04hn9QB1RQeIPlY6b2Dsdl9OcFu2tHWZ-Z9GmBvT3DwGSLQEj8EdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZC0JgAs0LaFC40zulIbQXYg2NHRJZFe0zFD_iL2v82gqV-mwyowj1D4qMa7YXV0x6C484zTCy5cIga6_31IVkyZPyPOOS8hZ4uH3lFGboaKRFfSjM6hGdxJniLo96ZZEJgVFIMAJXtexTX2CnJcBaWXAmeOfB6cR8e1rHIQExS041ZTYDipstijFP9vOcQXUiwDBmvxeNjlzuRpn_oK8SbrYHwsvkvZDjU25ir7NP7zX922hy8eHSOPhSm4ny-T946Ve1x49UDnZAafJZaFWPjU80C6dnP-InsQRj_xiKPAPaqHApaUFBMg00aDAylzBQLcdgtk2CiofMSJoBho2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=pwowQ_FvGn5CNmAqWt4NZtyKvo-eat2TnVEdOWjBgrXV74OLyU2_qrPsbfHmCy0XRvKcwrlbsLXzK6NRuVgU1ktv_uj4_2QuSE9fIHiGgTRNumCDbxxLe4dikyX1PCDWojx5fpiBifAxoRnRLVxprrSmXJYWaUP8I7fwuZwrKUU4u3YfNlUT6eq_nAq0q-oZKDB4SsorXd6yPK7JYBF-m5nJnB6egafjqgVnJEepac2DNLxwZZRBKUU7k_CdUdzB6ryItgSnSSVt0Zk2Mu8-zNMRkf1_NMWFBWGf_Y7XrZiosTmOx2xfXHVpmJY5I0fh2jj-dlDTvAacMfbPu9NUBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=pwowQ_FvGn5CNmAqWt4NZtyKvo-eat2TnVEdOWjBgrXV74OLyU2_qrPsbfHmCy0XRvKcwrlbsLXzK6NRuVgU1ktv_uj4_2QuSE9fIHiGgTRNumCDbxxLe4dikyX1PCDWojx5fpiBifAxoRnRLVxprrSmXJYWaUP8I7fwuZwrKUU4u3YfNlUT6eq_nAq0q-oZKDB4SsorXd6yPK7JYBF-m5nJnB6egafjqgVnJEepac2DNLxwZZRBKUU7k_CdUdzB6ryItgSnSSVt0Zk2Mu8-zNMRkf1_NMWFBWGf_Y7XrZiosTmOx2xfXHVpmJY5I0fh2jj-dlDTvAacMfbPu9NUBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=rb2aCIHkgJevG-G5qdtFhRKOspgpLLWCQQY0J9YvL6Qyzc__u7OGoWCq6VmOi_gyrc4lmTU_T-bSmoP6pkAbhZTKLJsy2GG0b5vKKNAMvdhmi_PWlCWHaP-pk0eHtRiPLVHBBLYCGK_o26oV6sBprWeSIu9g1aBlif61LB2OGheKO8a6ebU17UpcmEavhmRjrHcrtpmJQjLa25iAl5PwlVfo7cHULK59aeWeO-67bDLmGH3FebbakXICQoag8F744CJWCzIfx87Ba1oI1CcWp3CVNlYOeoH5BdKf806WOjXYL1Y8_aDjMqJXQroGRKOxiFVQEaZ9-6fKtokaXTTOlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=rb2aCIHkgJevG-G5qdtFhRKOspgpLLWCQQY0J9YvL6Qyzc__u7OGoWCq6VmOi_gyrc4lmTU_T-bSmoP6pkAbhZTKLJsy2GG0b5vKKNAMvdhmi_PWlCWHaP-pk0eHtRiPLVHBBLYCGK_o26oV6sBprWeSIu9g1aBlif61LB2OGheKO8a6ebU17UpcmEavhmRjrHcrtpmJQjLa25iAl5PwlVfo7cHULK59aeWeO-67bDLmGH3FebbakXICQoag8F744CJWCzIfx87Ba1oI1CcWp3CVNlYOeoH5BdKf806WOjXYL1Y8_aDjMqJXQroGRKOxiFVQEaZ9-6fKtokaXTTOlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=kFhslLaC0hKKtfEicvs2b9ZsVOISR-UdWPQz0hbPONc1TbMpNqvJ6ZGqspcE0h2TilgDax9_vW0IcEfgVhbnk1NrdJfguqvTI662BY36lH8I86WFxsDltHI_YlhcxnnAZSbQn389lJGmlKElyOI6oWzgsyoa02oZ9Lu8nlxbTvW2D3U4aUMx-fJpmIOfV1-eU72sQTtR0HzSHYKhVpTu7i1-MqU78WO3tIKd03D0ryMktouUXl3bo3mutvhDKj9lXlVSPZRFJAlzux9W7zZjEkQcUbSl5txlJGQltN3ytxsO-WVVIJUb8z061-Y6mUGIVN_HbeVhmPEdXJb_qrywsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=kFhslLaC0hKKtfEicvs2b9ZsVOISR-UdWPQz0hbPONc1TbMpNqvJ6ZGqspcE0h2TilgDax9_vW0IcEfgVhbnk1NrdJfguqvTI662BY36lH8I86WFxsDltHI_YlhcxnnAZSbQn389lJGmlKElyOI6oWzgsyoa02oZ9Lu8nlxbTvW2D3U4aUMx-fJpmIOfV1-eU72sQTtR0HzSHYKhVpTu7i1-MqU78WO3tIKd03D0ryMktouUXl3bo3mutvhDKj9lXlVSPZRFJAlzux9W7zZjEkQcUbSl5txlJGQltN3ytxsO-WVVIJUb8z061-Y6mUGIVN_HbeVhmPEdXJb_qrywsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH8Q2rSCb0GqENIe3kHhCjw-ZzNBDTgOVGFWjmIfWhRjyR3yL-44IkjF9ylxZWVHGGbNGspmvhR-CYSdbeA1iTs8JhWhObLN12_2eUWJWyj4ayKFSqB2RknD8y_39-_mUyMpB7K4W7gmDbaA9MeAUnJ5PRRiy_Vti2rKK3RajQkGb7fAHvXve_U5D8wpfEjV4oHZkc65ZpOcune0fzPpybaNJwJSZmQgXLRVqz6Wrg2OeuKruL0D_KpFOjD9ClA27F6YckdTTuMra8z1CjjQxEm0bBM6ASKh9YjB1kq1Z8zQXFnkqBfhmpIp6zBVkO3Ey2fTeWtdvVw7HTTOTSVjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=obl00HLZ_VhR4u29KJaiKs8xtmGYu74hl0T9nkTcMWV49swtBtBIKU2dEEdrBH3A71BjRjeTZnTzezsV5Bofqe8ImnYUQqXNJyJbujfU_jzQlBdw6TdxPar15l9TCNG8qcw6q6vDIWf4mvwqj7wFIVkbGTzqrdSpgvTU2hGh6gKMo1GivC58tDTu_2FwVP0uL7CfIZ1hRTtoqhyWZl2pfyRmhUpfhKXttPWegUXW_hNYQa-x1L4m4Ck74dRt3agXV6WKlF-IfiMTWBtSd7dQN0ljAfoBW4zlJ3Eq7hSEyftfYVlbiI_KnVBM19iU6Fkc3w24ifKXGc6LvJzi3q5d_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=obl00HLZ_VhR4u29KJaiKs8xtmGYu74hl0T9nkTcMWV49swtBtBIKU2dEEdrBH3A71BjRjeTZnTzezsV5Bofqe8ImnYUQqXNJyJbujfU_jzQlBdw6TdxPar15l9TCNG8qcw6q6vDIWf4mvwqj7wFIVkbGTzqrdSpgvTU2hGh6gKMo1GivC58tDTu_2FwVP0uL7CfIZ1hRTtoqhyWZl2pfyRmhUpfhKXttPWegUXW_hNYQa-x1L4m4Ck74dRt3agXV6WKlF-IfiMTWBtSd7dQN0ljAfoBW4zlJ3Eq7hSEyftfYVlbiI_KnVBM19iU6Fkc3w24ifKXGc6LvJzi3q5d_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=BaX9HzrdvHPFVfsqs08g0gnEvKpYJQErxUU93OdamtP2NtzkMGGQ6xEy-OowA8TMbJUXJAUPaokQJp0mb-4Iw6WSTNWDH75QSS6e4lYhw-ZtFI8gE-IhYOGlMeUnZyzQI7FBYkIEinvZoHeKuzjGZKLPWYCZdWG6wmye19WN6KOievFhajseQy2GhWBnIAL6oA-V0XupgG08o5uArifT5RBwrUcsCYGFJDpkoJOHWUuGVdYllfCXCg8Nwy81UAbuHiWHYWlwFrjmOPyrvfBXOf2jHtXMUWIpJuvgks_Tc6X8qbosErZmaqqfY6AaYuJ0oFiHhtGxPDACAGNAba4arA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=BaX9HzrdvHPFVfsqs08g0gnEvKpYJQErxUU93OdamtP2NtzkMGGQ6xEy-OowA8TMbJUXJAUPaokQJp0mb-4Iw6WSTNWDH75QSS6e4lYhw-ZtFI8gE-IhYOGlMeUnZyzQI7FBYkIEinvZoHeKuzjGZKLPWYCZdWG6wmye19WN6KOievFhajseQy2GhWBnIAL6oA-V0XupgG08o5uArifT5RBwrUcsCYGFJDpkoJOHWUuGVdYllfCXCg8Nwy81UAbuHiWHYWlwFrjmOPyrvfBXOf2jHtXMUWIpJuvgks_Tc6X8qbosErZmaqqfY6AaYuJ0oFiHhtGxPDACAGNAba4arA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
