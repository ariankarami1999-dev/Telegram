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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 10:08:38</div>
<hr>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=ieDvUzXc23lKRmLJtLKYIhGNbt4QY4X4yAe2oOD0yzCWlVeojdB5hagbMYs4nU4ZoTzOWdyeZYCBKKoCx3V0Fo_q9ia57kZap-MUpqTs-Y9dXz6n6Du8FXV5is5l9ghNFA7thnYMtK43ParbW8bJ2JxiZq0FFl9z4cefwYvip2xI8qhKapUFld5ncoIgQradKtq1isdEUdcw2JxM6k1YGNSealtZZLAalhd34kG-Kd8Lkr3O7GULmzhv_ILWBW29ISQV2s9unP3VFX1FPRpZNJMnA-6H9fb-cbVVwA0nQ-toKT6BFIstherGq_N458fNNu0wD8xQCs2bYeHrnxi6hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=ieDvUzXc23lKRmLJtLKYIhGNbt4QY4X4yAe2oOD0yzCWlVeojdB5hagbMYs4nU4ZoTzOWdyeZYCBKKoCx3V0Fo_q9ia57kZap-MUpqTs-Y9dXz6n6Du8FXV5is5l9ghNFA7thnYMtK43ParbW8bJ2JxiZq0FFl9z4cefwYvip2xI8qhKapUFld5ncoIgQradKtq1isdEUdcw2JxM6k1YGNSealtZZLAalhd34kG-Kd8Lkr3O7GULmzhv_ILWBW29ISQV2s9unP3VFX1FPRpZNJMnA-6H9fb-cbVVwA0nQ-toKT6BFIstherGq_N458fNNu0wD8xQCs2bYeHrnxi6hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=A-wg9iGdavXIKXH-GzzucsFrjgg06Jjpx8mBzToC_oL4F3V01tkNXNWl9dnLwgJoXXA6ChLvj6fLqf5n5ll47EclryC61O6m0hCBcIB8hvAl4r8lQ_stEmIvLQONvudJGzBxKUlacArDGDcpcKS5-3R63_Gr6gBFibEQYi1VBU5vJgWDf5WCCvoXAFklod9qc6blzwxU34_dN2q4nKfbHuDwn0MCjr-RRN6rFoNh9bPxDpfqbbe6s3cwYhbXpPJrJOpugK96QxkU7ACGmeUi4iI0Txnk18VV9mYlIQmbngwWSC_zD36HZpyHO__aWOzwbe671lDv7DPP4DIm_vTzZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=A-wg9iGdavXIKXH-GzzucsFrjgg06Jjpx8mBzToC_oL4F3V01tkNXNWl9dnLwgJoXXA6ChLvj6fLqf5n5ll47EclryC61O6m0hCBcIB8hvAl4r8lQ_stEmIvLQONvudJGzBxKUlacArDGDcpcKS5-3R63_Gr6gBFibEQYi1VBU5vJgWDf5WCCvoXAFklod9qc6blzwxU34_dN2q4nKfbHuDwn0MCjr-RRN6rFoNh9bPxDpfqbbe6s3cwYhbXpPJrJOpugK96QxkU7ACGmeUi4iI0Txnk18VV9mYlIQmbngwWSC_zD36HZpyHO__aWOzwbe671lDv7DPP4DIm_vTzZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Y0nxJqA_NlJ1R3Ob-O2hqy9G6GITVzImM2R76mRjkrJMl9BFohc-Nps8H6tRE4Nn83lGxG5nRO4hyOiefZ0ZGgZaN2VGdJkQKCubx8ChLttI5AQeeokS8SMtHfNJhIj6yqqhvRW2p_NBKbaFMn54mSRbxUbBnEdY2WsvzJ3_9u27vHLHxIoC0vtfFG-ryID5IdkQD0fdcwH-kJza8DhXH-nk5KHB1YWe6wtbSnkQs-Uxh6wLPX5KHPtst03w9ypxSQl71QE5e4lfR28gztcGF7iRzxqavrUrk096N888S6wPLQE4e1qSULjK3JvSWNeducYu_hJdFCdvaINGPiXbHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Y0nxJqA_NlJ1R3Ob-O2hqy9G6GITVzImM2R76mRjkrJMl9BFohc-Nps8H6tRE4Nn83lGxG5nRO4hyOiefZ0ZGgZaN2VGdJkQKCubx8ChLttI5AQeeokS8SMtHfNJhIj6yqqhvRW2p_NBKbaFMn54mSRbxUbBnEdY2WsvzJ3_9u27vHLHxIoC0vtfFG-ryID5IdkQD0fdcwH-kJza8DhXH-nk5KHB1YWe6wtbSnkQs-Uxh6wLPX5KHPtst03w9ypxSQl71QE5e4lfR28gztcGF7iRzxqavrUrk096N888S6wPLQE4e1qSULjK3JvSWNeducYu_hJdFCdvaINGPiXbHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edbt87X-xpZjrPqv2Rcm23gD39bSlkA0hUDky6JxRlwfDQvcInzBhm5lzKTmzR9loh9ExVethoIwZzcdeltJIef6MlG78i3xo7oAw-YCKhJEzvvk1K7i0Y9xDvI-Tiyd6vbZBfhqBtStOT_2L3faYks1D6qrL3TK-hOKbChwFqlmrbqyYVn6cR0w2JSZ59nGBXl24DS9QHsGbddtH17UGXVdaJaGNhmMmCTz6zoHrqT_LE7tgtpAa0cx_DNs54q2KKE37vKOsrdRPud2GRvzGiyUaHDzo3lp3OyF22ptyHCaJ3k3kA78sKDQXci7o26d_6_XeKnoLEwaAs6R7xhnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=BZC3PqS7ll7kV7bodRJVowZ5xlQy5oXDjiy1dVgCByQzurChPlAa74et6GgAjUYN5mLd88EbNVB6APTAVDjO-kKTuPwSJK9pGLbwrYJf2H5VCXr_8EdrUApKcWAKxqBFWzocY2JKoDTa83i_oPIHkgvyvEN6ncPtFQrBv4lWtKoNa9rb-CnM768szSEUaUrtWE5D0s3szF8YfCUN8e53lqu4SRAhCVZGqC1-BNxAC41ZWpjKPVLVa0A8_5XSI-AnJTnWc_zTlzcIQPdzmVwbQKLLN2QWZ7Z-rOHTiEKZ1xsFE9qVkM9EnqMeb9URxaV6bOnDehGvjpWUgLRcBO7Yiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=BZC3PqS7ll7kV7bodRJVowZ5xlQy5oXDjiy1dVgCByQzurChPlAa74et6GgAjUYN5mLd88EbNVB6APTAVDjO-kKTuPwSJK9pGLbwrYJf2H5VCXr_8EdrUApKcWAKxqBFWzocY2JKoDTa83i_oPIHkgvyvEN6ncPtFQrBv4lWtKoNa9rb-CnM768szSEUaUrtWE5D0s3szF8YfCUN8e53lqu4SRAhCVZGqC1-BNxAC41ZWpjKPVLVa0A8_5XSI-AnJTnWc_zTlzcIQPdzmVwbQKLLN2QWZ7Z-rOHTiEKZ1xsFE9qVkM9EnqMeb9URxaV6bOnDehGvjpWUgLRcBO7Yiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKY_A96mbRFZL_ZsHKmNYQqz26o7QJhu3sosszGc73ZU96eYzogjJJM2r7dBcebK6dtb0VWl1v2YMtKTp7BWRVo4sh9FQHINHa6-J0DA6MCS-buWSMm1342UmG9DEvEguwVT0tXRsso0zq95W2aZqhvmzyAj870oJ0CpYR9fNyIHkmFdwvk4K0cAXxFuohZ3EdHzbUZTZIVE0jnkAzzGhJzZFWwvWP3KKaO5VmJRwK17NvgX6kZMOo5POC9fBF64r6mK1C2G5Llt1BnNSCbGwiTiTgcTURB7uDfMLdvyKzoYIWcRuyyhY4nzeCmMy30ooJ_DDPC-ByCUBDOTp-UIhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=m3hsukpZE6yu0E7V5PMmraC03voR4Kwy5nKTre9FujRyvwGMuXduT40P0P6TGLDju6sGd515YHU8mCsJVcj_XYiyzqtSa9Tb40XtSTzO7sfWnyvSfd1Jf970e1S3DBQewbd8fZuSy7UepJ324mNd2d03RHxn-sXQWXTSsPlzhUJhOKq6i-Aaq1QUx5W59-LKcLcgHzJ2jnlUbNhA24tkiaN42Bt-yM1JUHTeDZK3qqcFKxymowm8zfQ24EKRGdUoeuzcSyuBjxHPHdJWjhskqMHoL9lXKWTzV1U0sqQnk170hQWrRYlVfIzAFdMTJ6YkrpTxsFqAPXr3OOvB8HBVrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=m3hsukpZE6yu0E7V5PMmraC03voR4Kwy5nKTre9FujRyvwGMuXduT40P0P6TGLDju6sGd515YHU8mCsJVcj_XYiyzqtSa9Tb40XtSTzO7sfWnyvSfd1Jf970e1S3DBQewbd8fZuSy7UepJ324mNd2d03RHxn-sXQWXTSsPlzhUJhOKq6i-Aaq1QUx5W59-LKcLcgHzJ2jnlUbNhA24tkiaN42Bt-yM1JUHTeDZK3qqcFKxymowm8zfQ24EKRGdUoeuzcSyuBjxHPHdJWjhskqMHoL9lXKWTzV1U0sqQnk170hQWrRYlVfIzAFdMTJ6YkrpTxsFqAPXr3OOvB8HBVrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkJ8CHRFBAWvEd2TAQAYZNpShabxRdJcaVbVVKakRuLNuHK2DedtIWLLwmYCixnkjt4-jSUWhFY2j9vPWKqWrK5Pvy46abVT16XsIYLcftttkK9SVPywPUeWvYSxvqatp8PmsXt6BDnj3mZIOe7iDjS0onR30hQ_0HAgDS2DHkoFI2JwWhUcvbPI6Q11MP2A9aUbWERdSbwd6P_m-h_nofwmtf8OA_rBFy-zIB_5YaRTOQO1NRkzogoCQ_Atc9CFk9RU5hbvZaPFYcwOVYJ2XdCypTFmLHRzXaaQuZYbnHDUSLvVSt0Ge5GwK1epHs-08HWUw690B0tBmBBkK7K5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTX7abO_HBWQHB5OHCn8fQ0fVF5Qt47vGKBs4RZ-ymc9Xv0K0QuIbbghgvxfHtzGWNJuRXDgQ3AFpJ_uZVZMndKziOMAWkDrw6vEBI83EWi9vH0nPHW5V2lhwLkbB82jiV0SZKtiw-R7ycJCQRGKa2Y1qFfJHmh7oFsqvks_oAwQE-U8LcZRohEvA32P6e_79MdC48q0pVHlklseHPmR6qN-anF14e5SCY9kmxxE2hUsjNcaLUbta1w4JWIcjw2LrPWombTlfStTNIndvcpF5_Ce2ZDzAA1eozhEg51-9exRYnkrkmWC-SbC4eLXDQY28whBgv0FcbmdkOhb-0ukWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu5t2BLXmfUN9Z_0cuGlJEAhw7htdh-qKYCQG8aOVy-d4lxYOs0PQSw_BvLgkbIQzmMYl8N22_1GzZqyRVkhYAscHkwLvC0vE47N2UvMGWrrVn6d1qZwSOlGMuApAKdA0jUEbWjbCEr_YY_rorD5jC5rQzINBeZYux8tjkon4lkePuih4gq_wYe9G4mjnsdrjsgcchsX6Kfrq3hnjvGnefZHpAP4NebWYFISKb849WDRmR_Ks-w2JVGhKcVzt8GCDIX112Av58wG5OluvOCKLcwW2_xjSRaLei19i4qonjk4FRGlpCMRHEZuwLEA2-KSIumC7UriJlgYdONmvV01LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbRE5gRinXXmQmQD-T1zZM5TpV7632vwngNEJ_g4vuZMbVDxgQYaxu_eL544XcA_f7yymaOeXEy-hdeKl0_MlaCd_Qi78cqXFcVwkQDEfVfTylYaKiJ3Lq_cnfF57hzoY2ln_VCJvm2yGV0AGfAGxJR515DiXsE7y6R__L9Tv3HfpwBsu-NjYP0TTJXwA1NtfshUyyOdwu8pFShAJJrKuSzAZ49joEmAa8rhulO3AqjuvcrbbcNEGuJGSABR3SDmloJXKTJVLKZtODR_QHzj7DxGt9qD7DYfUeRZnOsiucAopyUcrmLfkcJbZ0JQw0AjhmWbfD_5Tj8vttnm7Pr82A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCcniK29Pqm0yNKU3T0DN5AqXW_gP7mDhbjFXI5M9eb-8ENiFdbM7srb-v_Sn-SkqS-f01uNfJcVnWobYxU3Fbl4_CpWc4E1Kho8-q1J7w6371ZtfOdh_v1d2O0KhfOiVte_uvSkRvb-Yau_aOmdT3nxsg4OBAe35OAymJ5_UEdRuWZcJWg2WVOcW4APUi3EP7iyK6W5tnvMsqtF3MQGA4XpPCKF6Ly2eVDe_qPRMJ5GRj4sDpIr14tZMlu6Sz2LOAroTVkiDTs4sppRn1zj_1Ane92iwyJBE6oHVY2CjjOgh9cFLco469MjNanquNW_blodGVl_F_6-iYzUBwtYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tynDbFAumzgxFsEIOK1pJ2po0TRzcI53FPaBGsXKZNx3eJbG8YCcI2E6WLXWN5-SO3mcNb_CXLeLhztbkJ0FeSGPPt_1s3DZU3sdsBrGdK0nqtyZ5G27L9V55pIkLEPeqt8LNJqnagYArsXS0BogyXQjAdkIX5e0uoUni2gTvYRtRmH0vVG2czliXNndFxJ-bXC-wgLa71yERBDa4xBky0d7Ry3__Ijq1Q59ChZ-plvp2Y1yhNDh94Ozexjbinu2AOHh6d9C-f_thNXe4C3b_2csAGUrKRRS3xWI_xWV0ZvorENS8GX1tfkNb24R9vRA4PYZWWvAxIkwwa_KzOJeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccH6zTEVsz7pEeYDCMCrX1hwWVWRLatk2xWZ9D6iwz8-l3Rn4oqoNlmHa-hh63VHtnVeV783bngFD1yro2tihbbhw_1bZJeKMEsxtHO500RUBy-MJMJYGh45Pndmkk5T575LQio0LkVxXWyeqMkOT12agp6zbo_9sQeA3XsY9Q-0KZqCx1K1c_PDUp4R_qGaU9RlmGooyizKWwc23k4wAMV-ksGm3g5IMCRQueGqPuFUY-6UjmLC2F3lDErTwrDByIRTJj3PC4hXCLuOmBX1S04owNB01xsb16EiEof69VmWlYYp6xcdDHmQg5zy7Z1MiwXFl8JAdDbxmJAgFI3rTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErjTe89-VeiZANiG0D2Y1GXJnpTGGPo-NVTTwuxC5MvYHUT3r7TSvhbGTI1KE7rpU3KsGGqY2Uuqnb57YGT5LDtgdyPrPZtR_Pf1550kA1aUnNbrlU5EpPPJM-cA3BtJiJVi1Qep1yi9NnmP08-kCvD_45kHC_wA7grgozn9YYBLcwm7bvWuVZpMfR78Ied2E8_qbhJCbV23MV9Iebkefn-Ee0jR1-9gFf7dHlBSYnvyZTOECIS-8xTpJPiPxh1Wf_8y182xgRVfnA1jTOnEEKHVAVqUxSbUEF9UT7YNsc4hAa2ByHMSAsQteWBFPmWxmja56txpshq8eyA78iqlBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=B0BvaAWjJzbgN32LMq18p7ivnFTTUsUVBruJACcnDSDUHXXufSNwWTb0bTSNtH_EhKvI23u1lL9pcylYVKX7CmFcnupZqvqazvPluXBwSySpf6sNJQvvEq2PJnnxNAQmu_7xZfLKu4T0uiubpQd62xIGbriKQYfUUDLABMNidqjtwe09BScHYbaAoMrbU9wwKA_JVY0bhSrBjcLfGHaTOwY9MGk22-MAjIW3wp7qJlky29jgCDke42Jrg7A1ZqgvF1W6vvQ61mIvWixiVUlg3MbzIINGPLIAm7tOqnM_JoretbcB9Tx7bo78l32ZcDCz0CDJZ50o3wqNTbYxINMJjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=B0BvaAWjJzbgN32LMq18p7ivnFTTUsUVBruJACcnDSDUHXXufSNwWTb0bTSNtH_EhKvI23u1lL9pcylYVKX7CmFcnupZqvqazvPluXBwSySpf6sNJQvvEq2PJnnxNAQmu_7xZfLKu4T0uiubpQd62xIGbriKQYfUUDLABMNidqjtwe09BScHYbaAoMrbU9wwKA_JVY0bhSrBjcLfGHaTOwY9MGk22-MAjIW3wp7qJlky29jgCDke42Jrg7A1ZqgvF1W6vvQ61mIvWixiVUlg3MbzIINGPLIAm7tOqnM_JoretbcB9Tx7bo78l32ZcDCz0CDJZ50o3wqNTbYxINMJjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyKeRyq864ek4Vq479cRimvhc2qdNcDbA1XqitpsjsiVF_R4z09jr1ZX5ifx2jazvax5PS2ZQk8VoFsELZGCzHXXzBYMbKWb9RvYlTpVyFhyxPioHLcIwyznWlmXP2qeDJI_lEcl8ifWIWQx4ObQN8mNguC5nkMQhJC2YJOLnIETOpMKNcesA59gHy84k4_j2MYH1AA41fjIGKoFQCH3fw048cM57-9FplWMd4RS8bPTH2fGNZCHlwfEUPWRU2QUSytF8belXVqkuuTEptWU_FvMSssAuh3kVJr5JmXHI3dyZnxYSMWACfqHSmIRPNnCHNpPNH4gzIwtt6uXc_Q_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2RkraEHa9iDtLluVC9ZoxyItZ85yH13KhiOeQO6J7XAUQS0eVko6hfaAUtPw5FyqptrHhWbp4nQnF7ntcY9DwyUf7CGBvWaHy6KN5t1tOxAeyTDeuO_yRbzchuxziQ2tIsCZTFihT-J__-6GZ67HwCMnzCQQdmRezcuowpRfjS6ht-2XHSpHIcVJQcsWYEnwp1szVe9wNJsl6vs2VbG3w5oQf0miUlopeW3u1MaaH-TyFWcRn3Gfu14cY6HkPqyDAoa31Y620rtmmaeJk24GSjxubLaozcbNEo9rt50z0cXuO3jLorjc_AlGHIbmNMt2dOh7HzAnF_48isGoLxCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLzWqAmFIVyabRJHnDTj6sTysSu1dGMA05PscnhC7lA9fAzBRy6pWvW6vowVcPNzqUH_UxJJDOEAB-AuIAG-EQIG_gqnlSDccfWKVTRKnBZiQkBX3AkGRRgeD3sF9KkldOBpV_MF_eASEF9R5cOxWxSKJr0_1Uye-bM8cWVymp7ksQBxGwcCim1O8aB1GM2L5fBpTGX11-k60FU2zRyg1ujT-rj1hUp_XGd9VBH5RjNQqe6hSXOkeSgwSzVmGuab_RYfwzZ197DRFt65Mea7UUGkiuG2vEwklV9aE98CuNIWrELjCLu4NbbrwGL0YPWiKM4d8boUxd58ehO5CBI4hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhjEwk1IV3u_lyu_UuE-IXylf05T2hi1fSpfe7iSDy6vNHqN8a8464790JUougUTfJTs2wcFbJSQqxmKbbl1qRR094MWYgZrmlplF2d8lRuB-juWvcvgICHgp9HwBezHbecu7lZbrR1YbBsHpBHkWuxAgScqw8LzhC1ek-_Xrpq1CfcXpennuQd-aEm1GwJrv4-23A5K9WxfuU-c_490QuG7QfIRkUTN-xscFp_ec6MH5HylGyPOdwh2pcwA8Q67K9d-ktodNQdWr2THRbJ0qACaEy0mTZdQ5HyVVXyTzKw6sopQRUgQagK3Rd_Ne294OUJXGiFVkxXDOpiF42jALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej0pJXArvkac9FNMCnI9LqLaZGQqb1Z1Kwm8feS4kw3rAiOjfwYelPudeXzVrurGZDy0h9d21zbz_1t6dBnDqVMqXkQS6S-TuwRnSMkw18vnyzbkQdySqKDF7_27PjxfN2g9FrmODn4h3QLqDuxAabjypYVWSL46dCFHwBghmzu3oc8SLq_-Bmc79ukOzwzCpV7pJc_R2Cl355Qh0UNF8xCtnRPp1namgJpNFMfFpZ_1L5GRc88L9kDJ6V5B0cDFL5Sb-Zjutuixd-37HpUYL0wU4Qn-_AHW1U0XoXuGLCXTGTbdhHfqYYw2LOJG4fi3LOs8jIezDSZARnAhHNH_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=ve2keH0cO4VFufkr9edbOO3MyJrazVEPVEG5sMJHEYa-ZInitN6aRJOrjyqeFU-apzYjHARs-PQw7-bCrWOFmcQQKSQJ7FaeFCA7zuksu0sE3FhTjiPR5jR8euhfWU1RXizfPFFuyDNTJQ5Eyefv5inAP_OrU1hCNvI2bRXkTA3GA4x__5AtDJBMmH9ehpP8d_Vhir0n8QzHVmIsxqvrwlVmITL9zFTGqjEPplTgA0e7N2czx3LcqLZ9q871KHqFsbsrtg7dew61n7KXQv5DvrngppHpaGTlapZtUXfg5Waf52flwrHUfEOhHqBkgpCgKNNaTVNDqmX9DpSeJG2XfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=ve2keH0cO4VFufkr9edbOO3MyJrazVEPVEG5sMJHEYa-ZInitN6aRJOrjyqeFU-apzYjHARs-PQw7-bCrWOFmcQQKSQJ7FaeFCA7zuksu0sE3FhTjiPR5jR8euhfWU1RXizfPFFuyDNTJQ5Eyefv5inAP_OrU1hCNvI2bRXkTA3GA4x__5AtDJBMmH9ehpP8d_Vhir0n8QzHVmIsxqvrwlVmITL9zFTGqjEPplTgA0e7N2czx3LcqLZ9q871KHqFsbsrtg7dew61n7KXQv5DvrngppHpaGTlapZtUXfg5Waf52flwrHUfEOhHqBkgpCgKNNaTVNDqmX9DpSeJG2XfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_5kMIsA77aS_7GE-p1nmV6aL_-EyDUAwtCmdncz3G_0O5-0vnoKJINMMg4NhZlnG717GjLKXx4C3DRt9anP6ZQEecZ9Kmp8yRLqFDZ1ZKYqeXVOguDddfiwNWKhxUzlPmaclTaUiNV9NeUf6Sbg_19mDYyqaTQOoJLp7csXP14ezZDJGhvccCjNX0L02KJMZHYwTs7PVC-9MlER27sLoeoX9WAshZG0Cd8J1zTM-nxJQMSUXhcp3g0fIHSw1mOa7rq0WNyH_rCgWj5JItDbDOKZfW1VqQVxnGmTbm0EJtGAUQ8KhR6uCHKMjJtW-2gzWaBNNSR1fHS2sfPFZoCxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=kXxwZcOaHc5SOszYQNm7MDcP8xCiYmQ3GRQIa4MrhmEgUq90wXS59j-6dFkHMHFkJAKzMbam3CkOOLXd3lwYfgJxdr6OeToQVGbZIXBzUlFCagfV9pYfAhpZfsG18PnfTpoTr5QPOqP0tSH_L9RWhr1U_WEEA_-6CYxrfhl9G5FizmvBmS0pgmvR4q9uOhkCo3rSALJhixZOa8qygks9r-yauzDKpwSsGvwTm1IlA_58EwEVnwVhc2JgTa8bBzSQKxNLimMQOyIn7xrdNAf1SufvbskhDGifm_K7BrWTndkUSHGVqqfBTGBLwVVjIKI-fDmubWp63B8xDJ5hdfXOxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=kXxwZcOaHc5SOszYQNm7MDcP8xCiYmQ3GRQIa4MrhmEgUq90wXS59j-6dFkHMHFkJAKzMbam3CkOOLXd3lwYfgJxdr6OeToQVGbZIXBzUlFCagfV9pYfAhpZfsG18PnfTpoTr5QPOqP0tSH_L9RWhr1U_WEEA_-6CYxrfhl9G5FizmvBmS0pgmvR4q9uOhkCo3rSALJhixZOa8qygks9r-yauzDKpwSsGvwTm1IlA_58EwEVnwVhc2JgTa8bBzSQKxNLimMQOyIn7xrdNAf1SufvbskhDGifm_K7BrWTndkUSHGVqqfBTGBLwVVjIKI-fDmubWp63B8xDJ5hdfXOxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=LbPSjA0uXLE-miM7gBA-gjgNl2OXYYaCwmDd-gZEb8bWIsYA1rYfK2CpmkKZ9vBDDmfsSv9v9n77q-ecdYiuaRp2LIDUrM1jD9eI453rbxtLjWPbcwdw8tfT_4J8XFkTlqVVROKosE_bs0nJT3cUtAELkEQ0OGjHA382t_GgSjn01Sl-OJphQ0pcQHKlHISMTrrSDoAe8Nh3w39VCX7bJt887g8qvOZr0hk7I2rKJEjTkkjhawdSPc6lQxlqKDz69ca468VTv59AfEe1smS9bPn1z6k_JqmO0-0H1BnMRIoyVLp8mZrE1FYOFcb0a1oT78UNd7OhGlFDaE9Fmv4HpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=LbPSjA0uXLE-miM7gBA-gjgNl2OXYYaCwmDd-gZEb8bWIsYA1rYfK2CpmkKZ9vBDDmfsSv9v9n77q-ecdYiuaRp2LIDUrM1jD9eI453rbxtLjWPbcwdw8tfT_4J8XFkTlqVVROKosE_bs0nJT3cUtAELkEQ0OGjHA382t_GgSjn01Sl-OJphQ0pcQHKlHISMTrrSDoAe8Nh3w39VCX7bJt887g8qvOZr0hk7I2rKJEjTkkjhawdSPc6lQxlqKDz69ca468VTv59AfEe1smS9bPn1z6k_JqmO0-0H1BnMRIoyVLp8mZrE1FYOFcb0a1oT78UNd7OhGlFDaE9Fmv4HpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX0qDB3xcFarynpc_UiL9O1xCKDv9XweXGug5LEKqF7_IyJWDUWNefa8wzhZYcQmfAu68AV41hWR5z_z_CQ5Xdsw5eQbdjI_amKNnBvc9-5mb8RWTYjzC-86SovY1ExIcNmDfTD2GoUct4eZ_9chgRDek_LTQMHx4zP3ywYGthdg9pQVl35YsyZl9jmWYPFJuC03piyb4Kv9QEoOUCvOlv0MQzEgqlLaCcO6Kt1RMfgLgfhVeC5CHpkkeiMbyIdso1wEak5xfX8Qgc4Wvz1at6bGnYjnGo4eu_KKATU-u-0ij2mRxHuyG3qb9HaJTVaJ-PprPtCjaCcFR73lZVD_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cluuknOTCDrps5h171JoYf5H4kt7b3CetM0hRvwGGJ-AjYIf5YwacBZffpT1Li_yRR62X0aPv_r7AIi2peUa8SGIC94pJGv2imYPWC8hacQO1ujrx2-wwb0tX6WjWwueQF1TRwl5KIN7zXKDKkDPBP2ec-UBiWjP7r482ArlKATD0z3xaxY8On7gRA4wvlxo5cw6NwJVcamJmuZ26RW9bJiSiTEQZ18GR53OlbYnIfc24gEbsNbzP9Mpo1Ijop8gV_y_UmKbrhx5hEfkVgeUvy_xrbk37EohzO2dpFRUhtGUZ6iWxAHg5yclRTl3CMytyuIsblvlUbAQuxlK6iZGGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=eMkTIg6jjaCa618hHwpSJnUPVldvvztxtJrKQqX-00D98KN4S59pjfcJ5vvVDy-_J_w_GiZ4Lj-QH6UJ6N7Qp_aKa7E8wSw5CZmQrk2xy3VNfz47Tu0wLUp-TiPpF90MvSC7arzzKf15K8xkamG1HYYhcpmbb6hbNxfDMfxOFPpG8-cMD1J_5LyARHexa4k0XPgqgkUoXH9Q0jrAA0BlfayUHnRxhZm84OfhaFCaIR2QAhnXb8ORsEuHzQKHZUT_dV3JCvXpN1FkRlfUhuLFuaLEnVbRgJE1azahlGeEkLdsnT-YCYvWyxlw9m6VTS9bJwO_OAMuNlbVRNeA3GA1tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=eMkTIg6jjaCa618hHwpSJnUPVldvvztxtJrKQqX-00D98KN4S59pjfcJ5vvVDy-_J_w_GiZ4Lj-QH6UJ6N7Qp_aKa7E8wSw5CZmQrk2xy3VNfz47Tu0wLUp-TiPpF90MvSC7arzzKf15K8xkamG1HYYhcpmbb6hbNxfDMfxOFPpG8-cMD1J_5LyARHexa4k0XPgqgkUoXH9Q0jrAA0BlfayUHnRxhZm84OfhaFCaIR2QAhnXb8ORsEuHzQKHZUT_dV3JCvXpN1FkRlfUhuLFuaLEnVbRgJE1azahlGeEkLdsnT-YCYvWyxlw9m6VTS9bJwO_OAMuNlbVRNeA3GA1tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOOt2x9WMwFU68mhPV6I1S3rGb3yxif6jWlZulKBhyYRqEpEGt3lzDSD7nFkdjYpeN0ukYDe61tOMjRWYduzMFTsbqddtAo-qMOJuvTYOZIvr4VN35FscvAkQl40MLEllW57z3T2Q4nNbX0x5Fa9NCq6ZimkIVJAe3Q6P92Z_xQJmXg-umOYQWdgR2AJF9e69db4nGq4-eeMosc25qiON-_Cv0k9HKoYnrgJ-fWy_3C04VdpctrMmeYB_uqh7hLf_uBf6jt9kIZEU9S4HV6AVykcraOm0dS_WbVejh2jHE7yvlQndWuyuGAjiy4Y9aj_PTuXmt8YTQ3TIJ9gs_efLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ddt5laXvchZATBHIibxpUZlmgOhmyWaLB3KrsSdrv9foWGOSvXgmLQpIqrTPGvdAeZt80vuie0w6-u5m5MiEfS-Hh_wFTHEMzrlYt1jvo2aI7OdUl6KQtr9NZ0aVc-cp-k4P_n9UHQBGlDwXH70vEmKwJktX-f6Td-XljWx4cz7WlAfgv3magSJuBww_13Ejco-nSUhil_fPi8h6PJygiJi1EU3rEQRS3-fSU6fj5eywfdw5oKtigh00XAVOMZVCBW0geM2H0qBqAE_IKtDUiWLq4tpWDLJ__3GFO3Dgp_uyf_9RQKzCAMqMNXmGlUHwMgRAvNari93oHCGuuLa6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti5DkG9XIDOHx0j9eaS19QLmrm60Xb7uSDEm1R7PjweLcOg8aeUW73GHmdC6bN29_IWwzjx0vygmKaQrWUL9AgUXxSSxKmzs1WBqottoBrqVcCh5LdYMDvvctCUqMZ85ttzCSrmkiB1AW1VtM0N41RjTigAeeGVyZ1B9KyQpefwot_P4DXMthjLX41olHIKsRAndqNbwZUTXEnnDuuo8Yu5nw_4OnNspsr1MwczuVpOiW-3JsCDYxlXKACAr9iPytbDq0YujTvPH6B43X_2OKc8_W1wCgI3OtJNfWsj18nduJ5oURONNfMALsS-XznpR8eOjcQc-M439pBRn7OeBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5AW9v-B6VReWqZZX-TbRqDUK1RdxWmR9wyZIPpBAxfj9B9ITuKHi59DAv6KBAXY9bUCf3h6NMHMqwXqJ5aHT4AmOS0K6d3OwUfkrgmiNpTFKjPlu9xC3PjE3qAyUmR0Zgg74-AncISNuHW9bFgyg-dJrMsPTGbfWcO0mbOLGwt-UGgmSTTV4agHNIqt9_L_1O3Evh6BmFcVKlIO9nPkVjeg-yiBp5DXCwl6PhQfvsIeZ8cklNn0gLcUvy_6euy5fWQCrnyWSBuFljFPSwKpyb819GNeReYzv30V3B_wnutmwSiI8qx-GbdWwHgwMYDIJ53_yZS5sNOn4oL6IRkWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rldg35TpcoPPSiKViNdCbmZ4qvF8Te0uykrkDncyizZ8tinzbLb6IDyRkbLIjc8AAveTp6n7_pJUUZHltcx3cY2RnxfxY4lwpjS0lObhfbwQtts73d1nF9HNPb4wJI8uqhnImX4jCNZGUPhtC84OovOv201HSnRvA74-NZ_TxYGNV6KPftLJT85vxit40qbSn07irLs8x8EbmtOacz1ATpVzEuzHyvLCHxKmyK8BPN4g_LEXqvoRC33QFStGKQo-DDFKmLjcdyhLoZsApSq1gMARKABZ8xHDWa2FXxnZV4A96ysDlEA5hNVHc2T9ufMdKt_fTwq0Dwpu-07DipBqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkJI5yL5pwBC-FCecvQ-JQzJnmf38J8vjXYLLyEdoNSD37qSWpuwGvb6CqIPIa_6TNSmssnpyEwp8Jqxm1UbbUNMI3IaoNgavZ5h0o24Y3aFTIvLXvqearkdJbnmFw31Vqt3oNiR-GkBWDhnC2LcpsCA16XA9l23xyRBk60hPCyHskmfMFtAKOH5BMCGkYjDeTRwZ6QIYYt1IVHrPreUEvVB4OCSnBR6kJ5MLGRqSWk4Nywnul9WqtVoy8fCOzT-9IgpCoxyT4kgcxE5a9gyTUa6TbjtWdnyl5wMMv9ZGwsM6HRLqFJ86DS8YaANfH2MNzvUmhngbFGpCWWBX9MVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZGEhc4e-WlOQN7MdGUOKrvxiAiLHLsp9wvpuX3fiAzFO6Xa-MQULAHNResuVgUrMk2SxGCsLyv3qg6BkbVUnLQLfD4EUJSryrzYW6RHEhZ-5JtsvN7tyMJeVPbpMmWzX5BYus7Z1gieJ9kvT4HW8vldy6dkR0CglMLxqgByWrlWZrP8kKd0-evQVaeTfpUn-Jk6-xMB7XjpW8_IebMN11MfpdQLDQE4HFGSTcBENYG0smUtKwybFuXcLJ49CRyvweCHZGsPYhX8UROruAk7M7w-cWeXy-eryaECyFbKEuRYiRCgH4ZuCd2X50ne-GbiW4X-Tgy4iwy3D4VJ9sWy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hm7OD3NqwVtBD2-9VIyIInOi20BjljBwP2JMQxtSIf6QAOKy4kDy_nBYyFoV2GKJCy2xG09yv1IhzAwU650qlm3vsjQ_p16rwKW-RG1tvcESDoxWPpzCnrCQ_YAU82hDYTEXs3qyqKGPV47brwUyqvpQQaoMvwF_Tc5JD9C7MXODnFTbjL72NpfiMvxOpAJ4jB10sttZWhWpJQDcMnI9wlKSfGbQ0zhR_Bj-MUR3LzfxxPUfET5nC6SEDdDhxvjdQwU4Ikh37yMhNhZIygSGuU44inDSUD6bYbwmwxPbOF7Dh8n7yvg6tT0DQ2tQXPwQBMG2dYxDKVjympMhT-eIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj47ZuOkDAPkQ4aF-fMxd71X54E4tTRmIPOm0p7-KMIXHGOD6qQHJHCbzLsNE7F-gNK6eFRLnmmOdHRGY_zxKAm95Kc2lc4P9N2VyS52YuZDDMIa0KtPZCFXmynfrr8DJ-fiZzbSeBKJQTUX5Ez-sZpImgijnAtdH8tTXDD8ZncMmwI5HWHQzCfK-RKvGNKeY3tt1BZXoWS5AQlMGWBRzvpHGW6OFhRnIRu9mzk9VZMgtt0od71fZ0bfMU9YQLu4k7nvWOAnGDFjZQ9tkpq_Rvo_4Oj_SdiCGkkomNzxfzV08JHVZL4l80xqjYpipVWXNeRZ7Izkt4zYXuaZCdCl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQq1rZg8xYJ5L2vtorLpFCNxElhBs8OxUb4DIg8Lk6Pn98pUjvY9T32CNrfdrnp6enpZHyihNNI9lBZxL4Z7nSdZJwFSbQeuex65toHQuVdxdBZN79WD4COTVmfTaZYJCGsTkar7SaYSHgZcw-CUSHtyZDbGVFdGWNUx2Rw5WQVDoEpB2zbj0eZeQUuYDJZPGLgWUtbYrzlqE4oLQmAgXWJOPi3n8jjIKeoLlSGWVYhm6rVsYjdILj_-cM2_8cJ65PCvpXDSuIQmhmydDW69-An6kSQgbXgaKAc7OgV16UXXw5T4576B8v11n6LmGhyNkscOIZuF93WLkItK99qwEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoQAma8Ebe2lZcg7Hs_Am9aU0h6nhqE5s0KZj-eLUoBlAyM0ssfRPRYpaVZjbFwt5l9-ESACssQw1qZ-425YppJ4PrAkCbic8WM697r59idJe4ugNJ0dKoZh3vdA0vtMDSB0K-KZTttZoJZFTADNYStH1QxsWuYu-HLuFDYdj9KGqCAw4Mm9YmqVtOeuXymHpkJ8078p5hrSc6eTiSnnECO7jTMMSiJ6NbdWihpu4voYan_98dB0QEbSCbv95kN_M0dwLn3qobbeqooNUFv6Ktw6--J5Y_HbV_IYNQDyP8stqQpBkN8bGOdZ9SMu_Hx5SwYFF-vR2xXCyJP7R03uEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=pq7d0gC3CLMAgvdkM6IY7n04GcFaZI3zZ0sMkohDOIivNsJp90yRGf0wGknwyftAfl1j3J0z9XwaCbGgigWlj8T1aZmgJldAcSrA-6rPhrt9Rxdb2060JBOdQvT-ZUUz29f62GshWramoEFQ6E6KLmQwM8eghHi_vMmglheTQsrWQmMaHPkPyJNlCuUJzkJam1Lp6H2Mkzy8PNNJWM7jAWWiMBp7EhWU9OmiqOfEGXogg09ZuSZ_CAvixW8sPlih6HMEfC07IOsMmJ_SfbwdfPm22WFd4LLK90X4DvdgVl3puUK7aYV22uR31LHbiXDJJ4gPt5cYTM4tctw1qxs7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=pq7d0gC3CLMAgvdkM6IY7n04GcFaZI3zZ0sMkohDOIivNsJp90yRGf0wGknwyftAfl1j3J0z9XwaCbGgigWlj8T1aZmgJldAcSrA-6rPhrt9Rxdb2060JBOdQvT-ZUUz29f62GshWramoEFQ6E6KLmQwM8eghHi_vMmglheTQsrWQmMaHPkPyJNlCuUJzkJam1Lp6H2Mkzy8PNNJWM7jAWWiMBp7EhWU9OmiqOfEGXogg09ZuSZ_CAvixW8sPlih6HMEfC07IOsMmJ_SfbwdfPm22WFd4LLK90X4DvdgVl3puUK7aYV22uR31LHbiXDJJ4gPt5cYTM4tctw1qxs7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=vVfK49UD3sU547qNLGvMkT0RfzTt76IhaYvBzBYqhxBw53bHuYd4bpV7fgS7jVX61qceQw_Y46LzTYAKSFrXoG-gyuJgk5rUwWLJELFOlMZMpVyUkQfI7R7YkffM_TtU8qHdtbOTMambi179bOs50UO3lfOblyN7mODNKZKWAUaDoG75zDohoj1AAN0mRmi-w0mn-fuDICRouWf_nOumdZLcvb4CeMG10zEZ77v4Fcv5vGDMu5I67CRcDqI_rC59IX8ZDaCG5bZR52SfLcCvzRJH-ESqB13QtSj9c0II9WhbJaa3NzB-wFAhKaLT8-K5YhKUMatePpGXashzN2GbTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=vVfK49UD3sU547qNLGvMkT0RfzTt76IhaYvBzBYqhxBw53bHuYd4bpV7fgS7jVX61qceQw_Y46LzTYAKSFrXoG-gyuJgk5rUwWLJELFOlMZMpVyUkQfI7R7YkffM_TtU8qHdtbOTMambi179bOs50UO3lfOblyN7mODNKZKWAUaDoG75zDohoj1AAN0mRmi-w0mn-fuDICRouWf_nOumdZLcvb4CeMG10zEZ77v4Fcv5vGDMu5I67CRcDqI_rC59IX8ZDaCG5bZR52SfLcCvzRJH-ESqB13QtSj9c0II9WhbJaa3NzB-wFAhKaLT8-K5YhKUMatePpGXashzN2GbTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPHp-tUwILw68jzGHgZXcc5qN18o7j3387LHsXGotuaKYiY7K6lqVrbmTiw_MBGOfWmVZ4JGvnZC8s4cfHjygnWgiqUSfrezfnOuu_PruVIADD4CXvE426B7MliVI5UYY1vsCWGBxrGBhcvS-cn77a5lLHq36d8pDjLkjkjsOZyWEAG7tGdu8eBe8J1qRn-t5gPcTYGD4D7DPEkJIryplbQL_gYs33-I4S3WHS7Ymk4vYwK5HaH7_7XbIQpS3yrYvondV8Ga4dNA7Gbx8cOMW5hbX99cdY6dPBsTEXS7d4fnnWhbHXiEeErCpRA4BSgw0pCfl9sP0MRPzRcZtFhG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi1avAJqpczDsenGhotnwVATQ9aVUJewmhkHulbTJTlYyDjfdSrG4yXha0xp0ZrqR4KFbK6lrCzZZRnYd5qAruRgGDhr4f9DWrY2VZYY7M6H5W79TTC6tdYj8rgH7GprhWHbqiBWI2iXjyPxRzbvcUIi3itjUgkGtbbKsyFKWtCNTiET0CkOdNyXvorUtaLdBPeAUOekHcXodcGNThvdffrfYjn7byTMrzZztjyIuL4m9-QHcUkwuAv8VxzHSRKQUnGpyySq-SMeto4A6ERBkBHrhfh2hEoc0BPEfB7sUHSyNkDyufv2jcZGG5ihymv4bzeEfkp8z8q1eLnRrhSKig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAyqE8pxcnmUHScIbZ5cS04944Xh2ueyYuYmXQ1PK4D58nvc59KXME4nz0BN09gt9YNH256-xaPTCTvPUNUmsJWPv2h8uVN8ZzLdZlWaFjsbt04p3-yBOxptEtyGE0jZBhU5DYCWVgZB8if-5uwywLjdSMkxMW8Db10w-U5sviy9Jd0ajVeiGyDdyya661AT4tJOyPVDosJWZJDzBWXYVJ_E0yB4L4rxjNOvkGqLZEKk_xipZBZ96CG6sYX6rwkOPGlsZfoi5wZMKcRQjS6Sb-jFJcjhLkW_hKjhXlk1pElx7tB3iLc3WI5pFz35iOe8wQ6HTikzVEDMx0gNeVED1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=vYumTUhvKsAz-3X1PtygRNRSTXJWxvRlhgxi1jugQw7tCbIdLgQCz1XDehGEA0-rEajGA63QAjPU6IdmF-ytFNdhUGoih8muRh1Iv7DMpwCai29BNYKvHEmVKRaS6RTgFEoNWo-9NVXzaJnggokxhvu4p3ky7WzW_IZBWzw1Gr42O4aw_SFAqkjLdh53MWiVtihTOGEgUiMrI3_zdZ46V6hwWFhwfZRMXLkMksP6Jv6kjh9CLmCN76nJcUV_C5O_ESrOcfzmZ37Qb87Xcr2f5-zdlkLhWQYGKbPmGdjq1_5J8Qwid50sCNRnjxlPseuMmwEb6jTNv0r6VBssAHupng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=vYumTUhvKsAz-3X1PtygRNRSTXJWxvRlhgxi1jugQw7tCbIdLgQCz1XDehGEA0-rEajGA63QAjPU6IdmF-ytFNdhUGoih8muRh1Iv7DMpwCai29BNYKvHEmVKRaS6RTgFEoNWo-9NVXzaJnggokxhvu4p3ky7WzW_IZBWzw1Gr42O4aw_SFAqkjLdh53MWiVtihTOGEgUiMrI3_zdZ46V6hwWFhwfZRMXLkMksP6Jv6kjh9CLmCN76nJcUV_C5O_ESrOcfzmZ37Qb87Xcr2f5-zdlkLhWQYGKbPmGdjq1_5J8Qwid50sCNRnjxlPseuMmwEb6jTNv0r6VBssAHupng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1L6oC1iZMSB3ZDPzfaJ_39MwFvQNPhvZTg-hSiv78J3ECeWzBtjuNmpjjPLa0hTO1xBX9b3E_5pza8P8DjQOhghOYvg8CufH1Vt8Lg48Gm1nvmf3Bi2SmC5cmzwY7dUmGyhdkkpfjiwQkrDna9ZPZh9J2Ge0ilEnxUMXmc0Ybwu5DqbZnSt6A-nAyb0exC-RHFvo0K33l91lT9vTx_CDp9uM-t55ks8IdTaRp7AAVq5MtafCnCCd0Lv5pYNkwXdU_RC60OtfuTRT3r9oPM41baZ7LUmRzcwav2YNkRO5gGBWfm6nlgoTOTMZuS6t4xyyK2beORT7YMyueBMzKCptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZvP3Xt52ss2bZx2w_qU9KoDfmBEJtBW_kTeUHjvNWrYCRy77_M0-kClfPiVTam4xD7vqfeYM-VX7MjZKvlyMSPe6MaSFEfeIYBppawrSeBCAOi1hHeAvoRu_c93Q150oj77kzOXMlktryiYdDPIh_SUmboKjQMLFlEwskAaCqmPgCYaNWxbIPVEbS4a5DlM7RcdROF8jHQY4CnFCAUjwYRGi3IE6HhqMMwaCZG1Q_ZptahWc21up1g_eTKrHJATPsFL9vDrtSAo5mOj6zDYq9jaH_QbHc6N-JTQJG4eGweZOhWPEIObh7ECSBiB3qCshJ66DLHUkkg8uZoblakEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6QNRqNVUalIXHnSS4ry3AlzPpobirDTPGBYzdL-6EbEKNZufUuLvcJFtsilKzDY9JTjerbShaD4ZOzpjJlnesVxtc39DErQWbj-c92oRvXCLD287K66IUC7qsnNq8DYxXOgXxAZLhauSxQn3Blf4gTYITdxVq0r_FiMbjRllAONd3R8CY1yK6k-qpVGGVVxBcSkjSq5IZ8QuVqqD6tt-DYmJdPmhkPP-pOdp8yS46a8V3P8FznT0c2L7VewBiZlyPuNnrNMsXlUHfSSulq8bxudcm5_zm93K-VNCGnWVHlayEDyIBri6vMdy5en3hYiYLTCP0S8ugUKIuxVjYPDSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb23TEfpWff5jaUjExcc0WE7AwuOPujkk-sF55b7DJFUZmWA1MnM0i44TPmZf0hfIjonPQLE0Ec6-FMJNlBC9wZ0Fl-Jf8hER0BgIHtPExY7_ForcJxSNkjL46p8EujI4BCNwBnfpqWL_jeGe6_Pg5ePDBAlGx-SOVWeUB1-JW8Ab98tAtv9_IZ7TWT4ANPR9xZzrNFcDNAJHopu-Q65ibUNX8_zxDEkNpQJ8R0plp6pZtXwfnXCocthxhYqzmOXDzBH9u5rMRKGtcxIj9UbXEvlVh2HuGow2shQnYa72QQFPrK7pXqZNlYfdg0JhrdrSjyVM28NEFACbEsJk3-NxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXTXY9UL64FBL7fNzQi1ZrPf0pyaO__I2f3VqQgBD2_qXWKkez_lfO1OYdt4rM4UYLwbEmzNQUx8og93QCQTAI6Crg0eiAhDJJJzxWU1EqziwPeEnYjZDLxB3wRaAmwGaqVo72zOpZBu_yN8M750XwaeqZ5IA30t315X960DbHV27_biONyPFzXFdwM-Pu5eqEp97sMnkMoMKGa_i97BWJvCnmPe-8r5NNaUlYVgqCXqK5NjaWGDiwmS1e4m9xQ0TSZlDBnoYPzYzb9fDwSxJq1JNbB2ozp7bG03C4mt16Gbc4LMRNxmB18pRWIzXTZWY5qKNMEY_62b6xcodznTBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEp2Garpd-TnU4N48Zf99yKD8I_F7Oq5yivvbfTha1-sBnuLbFwKWEQbpCj9Isuun6xyQeQq_6ZjhetOXJbLrv8dfIwebJMGAnBQRgHnvErEFuWU2jj6Elc91LoHA9YO3qBV832kDWkQwKyPNpw3GoOPEsM-qBPpqUhuzsy51gK6dU6lL1E_PgSjphSH0wi-JIozbV4NqX2e2dNHBSGKvvUEpQfowUzuvMjCHwe5CEeVfS-MMHS2DMWU7zcgW8oxzqM5mAmv0pZ9iTOLJGwKFTxEc0TK5rhHy-sWhfVTHd19gwwJqZIhvAy_NzF89Ts5DQptEKpzwJ5tYCm91tr5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eB6yCWvXpulGcitqlvsRJOyFAYWWTwHn0IH4nGQOPncQ5UNA4KV8RN8swXOCy8uIP83ta6dzaeWqAY4dyHTTUCsu5KsjHlqLEhzR4as3YT5wb6pNI5FHWMLNC_d-E6pAEK91XCVpMFeUd6UNVG6VuHMmnDdzfLKw9rgWxs1r5EktYbE3lZfHFkWZ0-qmA2zdP4kGAlkHF4FQPCK37ADHYXeXP4X3KWlAThJ9aVK0q8FjnkIOwLh-P7sUdRUDd9ZDPewsTJqV2d0T6xmFep95v3CWjcd70fX8-AVfHFhMZ43CSixkamExRa6HsV3eEcdJubCEepTGXvC2HQu5oqBWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-aIZOsse4gn2jVqJV6rbdYxijhxOKT5YYUqg40HQ5_XbUmwE40u5uEzjR5ho3ZaT4N_uoeJ5BfXcZq_w_nTSQP08j4pSra7uTCp1ATIgL8X4cf7shEKqdd2wFQnxfBxY9BUQtiKseplUh9xRgViCf2J1lG95lraUoFtRdrlkrtS_9lWHHkGEXdiS5AtsPCf23PxK8xbdbmzLj3WjiYL18nI_6aNHPG-Lo9CkkTURc6PZyOAx6g2IMYPK-rauB-Gg8ja_gaCzhJf_tw-5hR3TctHmWPtsl5nVJ6m4qt8dkRrGvcuA-8xI3JvLopt_FfUiwUHZuKtE_DkIcw1Gs9UyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIbQelYWBRnqIKp31Im7piFkd3moL-9LHqRCnNUs1ppK_uD4CCTP4PGF1_9WY140DnBLbFd0u8MXdXpv1QRvE871xnnJA282H33TzOn_zoXom2HlT4xR37nH9uLu6zO_hmCFy9Ri6SZ30UV5fR7uFmhNgfRi4Fsl9ODx-xp4EA5Q0kuL7DNdAFTwgHmbZ-LIfrBdd3C1XM0L7LcdzvDKJRhSgo16Bw7pcvGn3sKX09T9ez0x_nhvhk2kCBcVyY7B6V73UAniozUknW1y5aJkCBn7VoM4PACOkB9ow5Svo10rhS-ofBrpNgbfkBzPvQfl8Tk6_TS0PqrAWjsr69T28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VYxVwxOFiPMnqhaf4Z_kq9beOnG2Gvr4nJkacHmyuzLgR8sFWegHD8JtHJt0kK6BiBB_b3njbbafXcOLo2bfddSIXl-TyrdRa9gXhv82IPRDgkK19eUnLcHcM3kkJnEAqN1i8K5pt0pG0huwSM6r6a6xwPX-JEsOsLbX-Thu3v8uJfafpyeoL4XkhbM9tUOZJPYutm_VZUtmvBkYn-0Rh-9gFsoPayK7-wGJ-hziO6qolmkL0Ypjt3rHBWzOg87v4VC92qgbM6Hk763mVxYPQ7AiaOzn8524BXlie0yhpLHhVAA53_jmtKPh_yyzD823pAzxjfjUHNr7v8njXDbH1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl68QK6P1ZwIa1cIuCj_gc3pe2HTzI-3F_f9SuDAUQxykhN1z9reXC12zXey0cRif6JocQwyYv8FEUBQvbzBc6eKre0mmijJwcScri6e2TdPBCKtS8ZYZ2MVFhmhfrzweU5oXPFjn96Zytol_O6ZHUFWCkxKt-5-Knp_ztMW41ARurHiGIWosoQ4ztnNuWlgPuWnoJxJuAQDI_iYH0WgUAzzqrX0l_ckcCJgM99R7jHxDiRM7oCe1Hkpb863WTgZnRorROfU-cFdaGlmAaatCFnQL8CJo-DTT0z8CjOLsK1sawvLsEKvUJSjLvjZ-6uMcraICeljT1zruXsbE6Sojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=ZgXN4z6jAX0kxm8g9dg1wbKb4Qyg_U3kk14n0DVJ0i5_iyPaO6opnrvyVSJ-E3Ik4i6uXjeqQKshJwRspSiCNHoNlq1fu_0Y8wWJ6fmUdIs0njxt3hLIJ1vkQs2j7vOFdzdOaHr5GCzesN3Rh7pul7B9xJgrCjVc_04vyoA0rASHwezvfLPlnFSN59ELra_cz_RiKJ3413kOp0EihienwcwLQ8gMh8_GTN6iRlmUtntqgJIT7tdF0rNGM5zj2Xlrp-T5QSF1d426OD-AZXh-efpUcQ_BA4oSKED5GfHpNrh2xnflAA6TKpLuV8Kh4hZGN6K6vs8Ew7vmk-zCZ3pIZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=ZgXN4z6jAX0kxm8g9dg1wbKb4Qyg_U3kk14n0DVJ0i5_iyPaO6opnrvyVSJ-E3Ik4i6uXjeqQKshJwRspSiCNHoNlq1fu_0Y8wWJ6fmUdIs0njxt3hLIJ1vkQs2j7vOFdzdOaHr5GCzesN3Rh7pul7B9xJgrCjVc_04vyoA0rASHwezvfLPlnFSN59ELra_cz_RiKJ3413kOp0EihienwcwLQ8gMh8_GTN6iRlmUtntqgJIT7tdF0rNGM5zj2Xlrp-T5QSF1d426OD-AZXh-efpUcQ_BA4oSKED5GfHpNrh2xnflAA6TKpLuV8Kh4hZGN6K6vs8Ew7vmk-zCZ3pIZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=K9966h9tC7Lo59_CV6O0PYS51S0gJy506cV0PAQCaYR4agCsWNFuhgzc4XMCLqYYkp7AU8b3Y_D-lfh19kPYuE08vis_53Wen1YXytT0hm3o6JN4s5T7vYaO33CQgnarcsRddYRTv28JYaQ_L6XddI2Sml2KCTGHDnar5Ly8ue-xWVLIipazvS1vbcXOAGqifIZV6bdFJmdtJ0IVfWJU_0a3hTvzO0Zy4L8dZM06IADaP0gWUWxEf18w0G7Z_qBikfA34tdgsm2MRrZvL4NSOxgkly161ZqNJya35dpky3f5qeEANUN8N8j-zaSzMR-lYhk_k-vrbWNmvVcwW574WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=K9966h9tC7Lo59_CV6O0PYS51S0gJy506cV0PAQCaYR4agCsWNFuhgzc4XMCLqYYkp7AU8b3Y_D-lfh19kPYuE08vis_53Wen1YXytT0hm3o6JN4s5T7vYaO33CQgnarcsRddYRTv28JYaQ_L6XddI2Sml2KCTGHDnar5Ly8ue-xWVLIipazvS1vbcXOAGqifIZV6bdFJmdtJ0IVfWJU_0a3hTvzO0Zy4L8dZM06IADaP0gWUWxEf18w0G7Z_qBikfA34tdgsm2MRrZvL4NSOxgkly161ZqNJya35dpky3f5qeEANUN8N8j-zaSzMR-lYhk_k-vrbWNmvVcwW574WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=Ks3x3U4dQw9pLkVOaqVWGt3DEK_F2IOnc1ZGftbWTbomSbO20kaPMZou0it66tnIYg2-J5HGKjOb01VPikpOgaBgEAE_k-zHhci6LZdwftRuLR50-K_8hvEpZeFc882noW9BJVVGrLIGPDg3LrQY2zTP1Z17auHAlEQx_wOxJp9ele_2ckDq9b2B3XjsW8YGYQlHW9r23pgzk8udr6NWyGNul8tJqOqSoV6mBh6OXHyjlfH2ZZUxDwNY1j9zj24MdWdRvvf7EQlbgfW7iMpfsB9LgEvzBk_VO-F9sNL60SHjhjzO_S5u2YrOdShDaR6HS1e6ysiIYakmyEetbxyMmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=Ks3x3U4dQw9pLkVOaqVWGt3DEK_F2IOnc1ZGftbWTbomSbO20kaPMZou0it66tnIYg2-J5HGKjOb01VPikpOgaBgEAE_k-zHhci6LZdwftRuLR50-K_8hvEpZeFc882noW9BJVVGrLIGPDg3LrQY2zTP1Z17auHAlEQx_wOxJp9ele_2ckDq9b2B3XjsW8YGYQlHW9r23pgzk8udr6NWyGNul8tJqOqSoV6mBh6OXHyjlfH2ZZUxDwNY1j9zj24MdWdRvvf7EQlbgfW7iMpfsB9LgEvzBk_VO-F9sNL60SHjhjzO_S5u2YrOdShDaR6HS1e6ysiIYakmyEetbxyMmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH577J6F-oKr1jXAiVhcdPRPolfF4rqStcBhWMTb0crT8KW4vDOX18Bmt5j45q3w0adKy6OyfFZZbHfUpKJykehiPORZLV-fvzzU09UgZI7Qujnkp46MfMoZ4jgn_R946-mKNGDcRRCCIfaKwJchHicQIH-51C95hJPrI_vF8LlusZzhsjS_y4dtMNXGmhjF4fNyLL1sBGRicWllJEoGSn9PG5I5HiLzyKWKVBhUVCwlinYYY-AQgWF5hNwOqbbeQslYwuxbFNQJtfqKMW8tO_NvWdwSjM9IoDSH7SDB1YOB21CZ1WjJdjU88vqNMRxi2k2xDaIw-3wikm7Ftv_MxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=lRfL1BsPcPZyyphdMLXJnezUH9EtLC7vVriDcvpgxto0vsRWBhRkf4K418dfUqIb43GqS4Yyizye5UrSYKKAhtMb6TnCbiYUw4Dw23kqvoGLnsm0bNRfH_sMKd_3XvayHMYMLzKCjz7i0mD4Oim0wk4Rzryzn6BIuBqmVUdiNh1BSrfOzmZT6_jcWtcaPPJGFgXr0XoyhO7ufClexqRTjwVfVDq3cy-1y58X6cOwUmAhgJvCjU5ymnwAaeYwqhDruAcFtkslxWuwNCEl2G-jWojoolgBdrCQ7Gdo_Sij-sWRxWAs3cD5lvwuACff7ZbWeGi9aUTLNFkTIuA9JMBbGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=lRfL1BsPcPZyyphdMLXJnezUH9EtLC7vVriDcvpgxto0vsRWBhRkf4K418dfUqIb43GqS4Yyizye5UrSYKKAhtMb6TnCbiYUw4Dw23kqvoGLnsm0bNRfH_sMKd_3XvayHMYMLzKCjz7i0mD4Oim0wk4Rzryzn6BIuBqmVUdiNh1BSrfOzmZT6_jcWtcaPPJGFgXr0XoyhO7ufClexqRTjwVfVDq3cy-1y58X6cOwUmAhgJvCjU5ymnwAaeYwqhDruAcFtkslxWuwNCEl2G-jWojoolgBdrCQ7Gdo_Sij-sWRxWAs3cD5lvwuACff7ZbWeGi9aUTLNFkTIuA9JMBbGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
