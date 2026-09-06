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
<img src="https://cdn4.telesco.pe/file/owYgKxKuqoNcZY837-ABTugigwxsGISBjY9Uekqv55EB-fcKMUJem7429-6Me-8hNLLe72enfdvL2sbw85ouQlxAVyVBM38D-plZBTTn2krfFzBp0km-0VP0j2esGJM66TL1HxUOw9cAHF7HU7YAtX73rYmsGVuoXyEgxmRHBBuMKngMY8MCyw2YGUQWHzNUz62_NXy7I8R1d3XqYZEhVjZ9jfq5Z1OyFkaQSAa5b_3GmrG1Z3xj4p6lCmv5XuYQgigU2AGNUEddWMPrOz-JUMuuDuq1yCX-vjlZCDMcg0giqkczpb4F07MayJNFxzGXvzduMwbMYKXfq54-nlGfyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 19:31:23</div>
<hr>

<div class="tg-post" id="msg-20596">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS1vKMLGBjimYvoQ5oc-8Vq-Pw8D33ejtwhPjOHuM2Yp6QYPReUo8aK6Bkibae8yhNwhAB4jQPvgzTlasG4Ex721QYbhmIByS96aMzm4EHvRog34mJEAnvZTZeKS6TlO4DPj7N8rc-p1iHHzNBFm14ZlW53qqsnJbdb_yiLViXNm-inv2Ow3KZsTKEZ2DZfEtDuHRDkPEXmeyWZ3rDNCQaOvtVrCrtdwIYpEmilGP8FGzgotYORbnXtCYbEJTKujp-syyS8n9kaGE0rTRxaN7CTbIGEWyS7r95YDnoLd_ViaP2qeSSFg7wk9xqCbHZuVtbsbgHY7MbwcPTncNmMZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هیئت قطری به سمت تهران حرکت کرد</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SBoxxx/20596" target="_blank">📅 18:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20595">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک هیئت قطری به سمت تهران حرکت کرد</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/20595" target="_blank">📅 18:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20594">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سنتکام:
نیروهای ما تا دیروز ۹۲ شناور تجاری تغییر مسیر داده، ۳ شناور از کار انداخته و ۲ شناور نیز توسط نیروهای آمریکایی مورد بازرسی و توقیف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/20594" target="_blank">📅 18:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20592">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gknar_ZYBd35adkKhv4M9BNPyBQbDTA7CrrpJqpLcRT1f-07lrN57Bx7uDPyhdFInqiLsT2zGB51fpdu9bi1fYUANXwVGHvbdXB4EIxsbGoRwpwFY44UL4OGISEArTxG8hiZ2ljiGU5IFH7blOplALWJ58WBQ5cpHIAT6x1QUZzV3dfnRiWXiPfg1KnlBP5JVc7evgbLtypz_pqgwSSYfXeFPGnal-tfKxMgfSm3bv5Fe24w9d2vdR-x09gUc0SZNkdQLyaRg31Cdqa6PJcBi78j5p90jfnAfhc0DDhhZ65h0g13hqJjusO8gFcQWw6H319O6ukyb3fS8O4cNPfd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار سوخت گازوییل در آمریکا وارد تنش‌آورین دوره سال شده است. موجودی جهانی گازوییل در یک سال گذشته ۲۸.۵ میلیون بشکه کاهش یافته و به ۵۴۲ میلیون بشکه رسیده است. در ایالات متحده، موجودی‌ها از میانگین ۵ ‌ساله نیز پایین‌تر آمده است.
دلیل اصلی، کاهش عرضه از روسیه و خاورمیانه است. ممنوعیت صادرات روسیه تا ۳۰ سپتامبر تمدید شده است.
وضعیت در خاورمیانه به دلیل اختلالات در تنگه هرمز پیچیده‌تر شده است. محدودیت‌ها بر ۳ تا ۴ میلیون بشکه فرآورده‌های نفتی در روز تأثیر گذاشته است. در نتیجه، نرخ بهره‌برداری پالایشگاه‌های ایالات متحده به ۹۸ درصد رسیده است که بالاترین سطح در ۸ سال گذشته است.
بازار از قبل با کمبود مواجه است: بر اساس تخمین‌های CERA، کسری ۲ تا ۳ میلیون بشکه فرآورده‌های نفتی در روز وجود دارد. در ۱ سپتامبر، گازوییل در نیویورک تقریباً ۲۰۰ دلار در هر بشکه، یا حدود ۱۴۸۰ دلار در هر تن قیمت داشت.
اکنون، خود ایالات متحده در معرض خطر مواجهه با کمبود سوخت قرار دارد. تا ۲۸ اوت، موجودی ULSD (گازوییل با گوگرد بسیار پایین) در ایالات متحده ۹۴.۱۸ میلیون بشکه، یا تقریباً ۱۲.۷ میلیون تن بود. در یک سال گذشته، این میزان ۱۲.۲ میلیون بشکه (۱.۶ میلیون تن) کاهش یافته و ۷.۴ میلیون بشکه کمتر از کمترین سطح پنج‌ساله قبلی (۱۰۱.۶۲ میلیون بشکه) است.
تا ماه اکتبر، موجودی‌ها ممکن است به ۱۰۰ میلیون بشکه، یا ۱۳.۵ میلیون تن برسد. این اتفاق در بستر اوج تقاضای فصلی رخ خواهد داد.
اکتبر و نوامبر احتمالاً ماه‌های دشوارتری خواهند بود، زمانی که تقاضا برای سوخت برداشت و نیادز به گرمایش همزمان افزایش می‌یابد و برخی پالایشگاه‌ها برای تعمیرات برنامه‌ریزی‌شده تعطیل می‌شوند.
در آمریکای جنوبی، موجودی گازوییل در پایین‌ترین سطح فصلی خود قرار دارد یعنی حدود ۲۱,۵۰۰ تا ۲۲,۸۰۰ هزار بشکه، یا ۲.۹ تا ۳.۱ میلیون تن.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/20592" target="_blank">📅 13:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20591">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یک جوری‌ مینویسند دلار را رنج منفی کشیدند ….
به قول امام خمینی (ره) انشالله خداوند همه ما را آدم کند!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20591" target="_blank">📅 12:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20590">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خشم روسیه از تغییر الفبای قزاقستان به لاتین!
این دقیقاً در راستای تحقق رویای توران بزرگ ترکیه می باشد که من آن را به عنوان حوزه بعدی تنش میان غرب و روسیه (و احتمالاً چین با توجه به جدایی خواهی اویغورها) تخمین می زنم.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20590" target="_blank">📅 11:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20589">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:   سه فروند شناور آمریکایی را در مناطق دیگر هدف قرار دادیم</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20589" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20588">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Off1K54TpE17kj-QQdAEg1uMlODUFbmqN4zIphPpufyjKtgHf_zKQaKKm42VF6snGa-o0UnQ_Mgulr80N9Dl0HvQQUFm_ARxHg35YU8BEpP4S1a7paigNvSkwu5l-3DsCwg2978tusEEkxendsCr455oMR1oEA2jO1K9fuTO8mJd1qR1WCNv0beFzuNVdK8VIY2CET436_EiMGq1wLZCl6T9DE7WyPOk0tdQkWJxgvBAZkezz0WkoZW519oHzLfrIdGaM4FA_tfgInEmWuQEyECaMk5L8M_RkxsBy07PnVV90ImJp3XM6o2c8fTckW-Jx6LIzLIJrDTPNNFCg_q9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر فروش تسلیحات آمریکایی به متحدین نظامی اش از سرگرفته بشود واقعا؛ یعنی گزارشها درباره فرسایش ذخایر تسلیحاتی ارتش این کشور تا حد زیادی اغراق آمیز بوده است.  نتیجه بعدی هم این است که روابط ترامپ با روسیه و چین دارد تنش آلوده تر می شود</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20588" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20587">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:
سه فروند شناور آمریکایی را در مناطق دیگر هدف قرار دادیم</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20587" target="_blank">📅 23:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20586">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20586" target="_blank">📅 20:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20585">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرگزاری ریانووستی (RIA):
پوتین وضعیت پیش‌آمده در مذاکرات کرملین با ویتوف (Withoff) و کوشنر (Kushner) را دشوار خواند</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20585" target="_blank">📅 20:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20584">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20584" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20583">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دو ایستگاه برق دیگر در آلمان هدف قرار گرفتند و مواد منفجره کشف شد</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20583" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20582">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ادامه انفجارها در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20582" target="_blank">📅 19:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20581">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ گفت پس از آنکه بایدن ذخایر راهبردی نفتی آمریکا را خالی کرد و از پر کردن مجدد آن خودداری کرد با نفت ونزوئلا دوباره پر خواهد شد!  این توافق مهم شامل بیش از ۶۵ میلیارد بشکه نفت است. این امر آمریکا را در مسیر سریع بازسازی ذخایر خود قرار می‌دهد.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20581" target="_blank">📅 18:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20580">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نقشه جدید کشورهای جهان بر اساس ابعاد واقعی شان!  طبق این نقشه که ابعاد کشورها را مطابق با اندازه دقیق شان نشان می‌دهد، سایز کشورهای غیرغربی افزایش قابل ملاحظه ای داشته است.  رنگ آبی: نقشه کنونی رنگ صورتی: نقشه جدید</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20580" target="_blank">📅 18:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20578">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromExciton Computer Missile Program</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUi34EZy_-bkwjBeB4ZtgZlekkwcRmrXpuEEFcyp3sk1tFrtAjEYG14mqdlveWmStS-iLKeLBnVuQNZzJtzNDTqLR2b4ZV6kSRIuNfD7_ci9hxH-RkoyeOWowMeU7pGyiLKo_lAdOOYI6N5p1w8utSE_KjZur4s0ZKbYyRa-cSk2NTOREwZjBYae_d2BnSEycK717cXAR1IgX3d7Yp8FImqbj88eHNgHryUXXBUSM6rvFPH2P_OWOww-Pqtj2OGImNoFXU1KxLb9fmK_3-yJ0zm3Hb7cU0mj_o5MiHQi1iR8eW3DiACa5MB-pc5otom8bWlSeBS1jqp5OoOkOwsvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1vHqeegnxgbmfo2zTS7q_tNYJOlsb-C1eObz2ib_Jfoz5YkaxGbZB7vZPS9ozFeU5hfBFdOmiR5eWOc1uJBGs_VrzhherVOxI5YxPG_9zgda1S9xTUk6iPrTqKTo1xf3KHIR7s9XUxk2bEpIcJ3xap2-gh3SkQW3nghF4Yoke3dX6chCOnhTe8QxEjJwcp7q-U4ZiaRyHuZaL3GnXwyoHBfFJrAzKW9DJ_ilnQNtC1WSf50qfX-X33Fa5N3_BX2wvVcbz8P7gXnIk0nS97H5RM6eUE2CJTInME35ZUrqvlofk8H_XGmI8PCUtCF0bmD1sPLF9yZhuwP7_C_VgGGKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه دیروز حداقل 3-5 بالستیک ضدکشتی به سمت دریای عمان یا تنگه پرتاب کرد تا شناورهای آمریکایی را برای پر هزینه کردن محاصره برای آمریکا بزند که به نظر اصابتی رخ نداده است. شناورهای غیرنظامی بزرگ در فاصله کوتاه عموما حرکت ممتد در خط مستقیم و قابل پیش بینی دارند، مگر مسیر خاص باشد. اما شناور نظامی میتواند پرتاب موشک را متوجه شود و مانور خاص انجام دهد. شاید یکی از عللی که حوثیها در هدف قرار دادن شناروهای تجاری حتی در فواصل دور موفقیت نسبی داشته اند همین مورد است (اما حتی هدف قرار دادن چنین هدفی هم با بالستیک بسی پیچیده و مشکل است).
اما مانور شناور شناورهای نظامی کارایی مطلق در برابر هر موشکی ندارد. یک موشک پیشرفته میتواند بخشی از این مانورها را ناکارآمد کند. در هر صورت موفقیت یک موشک بالستیک ضد کشتی بسیار وابسته به اطلاعات دقیق از انواع سنسورها میدانی است. وگرنه شانس اصابت جدا از طراحی موشک کاهش خواهد یافت.
🚀
🚢
(
بحث آماری پیشین در رابطه با بالستیکهای ضد کشتی حوثیها
)
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20578" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20577">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سنتکام:
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20577" target="_blank">📅 17:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20576">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js6e816m4r3EVpHjay1hqRMSZgJLeth7YMzd4hjBuxwwLnDWmyo9Ejgm3Z3kUIFGHi44Z1PMLLw1HwP-Q4yUwLVrtV8yEsmwZu5TGf5zPE2Khlvh8oGQjlRoDZyS73Q5UFqzYpR1ZBrZ1XtXRPC-TZuCz61MEvfj-hRLNa2HVVSxXBa-LEaJD8PoMOqj88gv3TwKD5vQiQw9H3Tbzp2aWgfxRqyMlP56Pu201ksMcUigkVfT0ajTlSjOvJgzThk7gf6qmmy7ba09n2KPYy_sRjOODTQpIE3Gq--0Auhe8udfUMogBIfcMIIGxvgG8twr6Wg52KCY_VoTURFrglyffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین کشورهای هر قاره جهان  بر حسب مایل مربع</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20576" target="_blank">📅 17:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20575">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">انتخابات اسرائیل</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20575" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تمایل شدید نفتالی بنت به سرنگون کردن حکومت ایران را باید دقیقاً در راستای صحبت آخرش — از دست دادن آمریکا و حمایت جهانی — ارزیابی کرد.   یعنی اسرائیلی ها چون فهمیده اند حمایت جهانی را از دست داده اند میخواهند خاورمیانه را بازمهندسی کنند تا دیگر تهدیدی برایشان…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20575" target="_blank">📅 14:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20573">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">راه آهن کشور اعلام کرد ترکمنستان و قزاقستان با تبعیت از تحریمهای جدید آمریکا مانع انتقال ریلی کالا از چین و روسیه به ایران شده اند.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20573" target="_blank">📅 14:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20572">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD6ijsnuF0Ws6BWRYZpqDnfzsK8HSORD-rlLcGgFijKutgCVD3wIS_J6wxLKX9QS7fc6KU-_25HdJ0DQtmJsuTFqPY01Az5U6QmjSwPfmsaolJ4PBh-kICJ1gPA3LzPjSlEMZaNxJk-NTbWr2-vpLf7qIVx1UDH8l56itX4vOFmGhnk6e_Mcpwby7CDzc6ROU0XrIzfR-jIltfIO_hZPeLUQFqLD_N9-fYyMWzXbPGSGIuIdix0QhmpM-QzytYSyfeN59vO3z3ohMYSAwLxITI7Be0fUTREvBxHyplyRC890BjqQ3GLIkD5N7hwjpsJmHc2WxkIXyPeOWQgtjhp6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپاد تهاجمی جدید ژاپن؛ به اندازه یک چراغ‌قوه!
ژاپن برای نخستین‌بار تصاویری از یک پهپاد رزمی بسیار کوچک را منتشر کرده که ابعادی تقریباً در حد یک چراغ‌قوه دارد.
تصاویر منتشرشده توسط NHK WORLD-JAPAN، پهپاد را درون یک محفظه لوله‌ای و با آرایش چندروتوره نشان می‌دهد.
با وجود ابعاد بسیار کوچک، این پهپاد برای انجام مأموریت‌های شناسایی و حمله در برد نزدیک طراحی شده است و می‌تواند به دوربین‌های شناسایی یا مهمات مجهز شود.
از جمله اهداف احتمالی آن، خودروها و تجهیزات زمینی عنوان شده است.
ابعاد بسیار کوچک
قابلیت حمل در محفظه لوله‌ای
آرایش چندروتوره
امکان استفاده برای شناسایی و حمله
مناسب برای عملیات نزدیک نیروهای زمینی
این پروژه نشان می‌دهد ژاپن نیز مانند بسیاری از ارتش‌های جهان به سمت پهپادهای بسیار کوچک، ارزان و قابل‌حمل برای مأموریت‌های تاکتیکی حرکت می‌کند.
#ژاپن
#پهپاد
#پهپاد_رزمی
#پهپاد_تهاجمی
#نیروی_هوایی
#فناوری_نظامی
#دفاعی
#Drone
#Japan</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20572" target="_blank">📅 14:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20571">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">زاکانی:   به دنبال برق اتمی برای شهرها هستیم</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20571" target="_blank">📅 13:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20570">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">زاکانی
:
به دنبال برق اتمی برای شهرها هستیم</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20570" target="_blank">📅 13:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20569">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسکات بسنت:  چنگال مرگ اقتصادی را ضد نظام ایران فعال کرده ایم:  ارز آنها در حال سقوط است و صادرات  نفت شان به 0 رسیده !</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SBoxxx/20569" target="_blank">📅 12:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20568">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20568" target="_blank">📅 10:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20567">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki5W2yfPQbb1oKG-fPOUKK__6r4iZZbCFQlimFYSUpuuqfb0RGOl4F2rbZr6GEShtswYFKEq_24Thhh1u9eIqbJHtlibgdAQ1k2ef2pCS6wAypIiqWifhI4RvXXxU8A_g7ZRdYZVorBLVDBC0evf0VyRbsrDK8VbFbBUACelKcB5t5BsmvVmTMs5cG5fVI9WQwE0iuqpnfpisPNoe0SXMchuzNLJncLOm3QesMkNGxaqAFnSECMz7_8wjFiW0CcJEaZfgPWeMb8S5Zs0AVo3NspfEmH1fuf6k6-oDokhNzaJz2PqTOrSxrFfqSyAQeIzOsCoy4GgoLsiPljLiEGUjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20567" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20566">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWMwHR9eO_LbK5g6r7s3C-Tl_fH0Th6ryHdkvMJTJ7CK4Vn5-EVXN7cBGoWsZNoy2eG-hJFEqe_P7RWoEtKhKIkWoNaINvuss3-UssnXwSToG74V5TbVSZl7FQb50aHWju2MYRD6OqUBjAJcAwUND7HmiRxRFXQ1AtFfulH33j05eZ21wKxaf_hf5-JE4puPCJBELmoxTbjsEF_JYmNhliBpWk3a-MVJj7ikYyhk9IdZYWRb10ppQ37x_LSkF6GsBfAEHK1va-Il3hjnHnvFn7O8H2-8CRkd2gvvjPDQr-772RFTRWBmasjlg2QeK0p_tzm9T5d-DU58D7iIS9xeOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دوباره هما خان سعادت در آسمان کشور مشاهده شده....</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/20566" target="_blank">📅 00:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20565">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">— شلیک موشک‌های کروز ضدکشتی از سیریک به سمت تنگه هرمز.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/20565" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20564">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVOKmV519y7EjZdt1_qV_FsZU9GKDLO4W4DQxS6p6nggoirZGYMhasjByKNr-jn5wK5xkp9TRVsuojGmWA53vbUdw0RjrluHMrhumv0qCZNIadBzgpbrOpzcUWGyvk469JAPqkLzy4NEWai-7GLzRmrclSISpTTXTG8Ei2lY5cJXirWiGr3EpVrr4yXNVssvgjEDBeJeyygQ_VUAud0cZKZyRJ0DOOcU3S_-I0dx_Qd3ho2zWgGZ5MnYy2M1DnaPH0co1iL5_JiNA5xl2UePR6-54j1dpgrPA4ZUp3Vm_SyBVT9R5JshxSOvgG4XjDDiNGADGaKDKn84ELYWu6zXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما تکذیب کرد!</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20564" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20563">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قرارگاه خاتم الانبیا:  حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم.   |</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20563" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20562">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ
:
ممکن است خیلی زود کوه کلنگ را هدف قرار بدهیم ، چون حس می‌کنیم آنجا اتفاقی در حال رخ دادن است</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20562" target="_blank">📅 22:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20561">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq6Lj8VJ1DaXP6-eAuJOaHbuaKMxLh9YYBu6eWFZE0UmdL4vZ6L6ULqmCV3gQgpatemVZ60ZZE0atAKMojNhEKb7hGXcTu2Fym1OXUCgAFXXDUTwzfKnCIsx_VCUx__gf13VEghj4WmzhBNX_aU5QdnK8o7hniudkpI0u1HKPa4mqmOX00vSqerbQ0JHjzEVx7WS0QvpJp2vQ9XJOVEir071nVkl45kqpcjT59eJTxxyhW1_vqLNJlyUUWoE23Ql5MEcWq7Z8ZxiSM32SVoZZPFc7NkRNFQmtYLj33MhYFnZYO71_UFTTuhuzJmvlK6H0wz6zDhFSPfkxDW48ZSalA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش حسین پاک از تپه های علی الطاهر!  به گفته او، تپه های راهبردی یادشده از دید نظامی سقوط کرده اند</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SBoxxx/20561" target="_blank">📅 21:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20560">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">برخی سایتها و منابع خبری از حمله موشکی ایران به پایگاه‌های آمریکا در اردن خبر می‌دهند</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/20560" target="_blank">📅 21:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20559">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اسکات بسنت:
چنگال مرگ اقتصادی را ضد نظام ایران فعال کرده ایم:
ارز آنها در حال سقوط است و صادرات  نفت شان به 0 رسیده !</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20559" target="_blank">📅 20:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20558">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">از نبطیه چه خبر
نتانیاهو راست گفت که مسئولیت نخست دولتش‌، تامین امنیت کشور و ملتش است و در این باره منتظر کسی نخواهد ماند(به خصوص امریکا). شاهد، رخدادی است که از ۱۰ شهریور تا امروز همه خاورمیانه عربی بدان چشم دوخته اند. خبری وایرال شده.
ارتش اسرائیل کنترل عملیاتی ارتفاعات علی‌الطاهر نزدیک نبطیه را به دست گرفته و زیرساخت‌های زیرزمینی گسترده حزب‌الله را پاکسازی و در حال خنثی‌سازی است. این مجموعه که طی دو دهه با هزینه مالی کلان ساخته شده بود، شامل اتاق‌های فرماندهی، انبار سلاح، ژنراتور و امکانات ماندگاری چندین ماهه می‌شد و به عنوان مرکز عصبی واحد بدر عمل می‌کرد. در واقع هتل-قرارگاهی چند ستاره.
موقعیت مرتفع آن امکان پرتاب موشک‌های کوتاه‌برد و پهپاد به شمال اسرائیل را فراهم می‌آورد؛ و مساحت و تیپ ساختش ماندگاری طولانی را برای نظامیان فراهم می ساخت. ولی از مدت ها پیش، با شناسایی دقیق ماهواره ای، هوایی و تجسس زمینی‌، بستر برای تصرفش مهیا شد.
این عملیات ترکیبی از محاصره طولانی، شناسایی دقیق با پهپادهای حرارتی و ورود مهندسی بود. برخی نیروهای حزب‌الله کشته یا مجبور به عقب‌نشینی شدند و تجهیزات مهمی به دست اسرائیل افتاد. از دست رفتن این گره راهبردی، توان فرماندهی محلی، ذخیره‌سازی امن و پرتاب محافظت‌شده در محور شرقی جنوب لبنان را به طور محسوسی کاهش داده است.
البته این  ضربه به معنای فلج کامل یا جمود نظامی حزب‌الله نیست، ولی موجبات شگفتی کارشناسان خبره نطامی را فراهم اورده است.
حزب‌الله سازمانی غیرمتمرکز با ذخایر پراکنده موشکی و پهپادی در عمق خاک لبنان، تجربه جنگ نامتقارن و پشتوانه ایران است. نابودی یک مجتمع، هرچند بزرگ و مستحکم، توانایی بازدارندگی کلی، عملیات چریکی یا بازسازی تدریجی را از بین نمی‌برد. نمونه‌های جنگ ۲۰۰۶ و درگیری‌های اخیر نشان می‌دهد این گروه پس از ضربات سنگین زیرساختی همچنان توان پاسخ‌گویی نسبی خود را حفظ کرده است.
اثر واقعی این عملیات در تضعیف الگوی «جنگ پایدار از زیرزمین» در جنوب لبنان، افزایش هزینه بازسازی و تقویت فشار سیاسی برای خلع سلاح یا عقب‌نشینی بیشتر نهفته است. اسرائیل خود اذعان کرده شبکه‌های مشابه دیگری هنوز باقی مانده‌اند. بنابراین، آنچه رخ داده پیشرفتی واقعی در خنثی‌سازی نقاط کلیدی است، هرچند حزب‌الله همچنان بازیگر نظامی فعالی باقی می‌ماند و سرنوشت نهایی به واکنش‌های آتی، وضعیت آتش‌بس و توانایی بازسازی بستگی دارد. ولی حزب الله دیر یا زود ناگزیر به مذاکره و توافق است. دقیقا شبیه حماس.
#یدالله_کریمی_پور
#Karimipour_K</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20558" target="_blank">📅 20:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20557">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارشات تایید نشده    از شلیک موشک از اصفهان</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20557" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20556">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ap2CMLWxirm-pAOTD4CX68xJL2wUKwE9CarUyeEQu4e9hucKxTO77ZSWoBEWpAJF0HkLx5k0IKihKOg9immhgddtDoczeojThFSbiSRapT1F-jnxsXnr9LZoIfzct63UVr5QndNmep-bUic8BKjJYw48LrHg4sknBs4NGros5jHTNrap5SnuY14mc1dpXV-za7tdUMGC2L55o-gDE2-95ehF96ycCa7dTI7okQktpv0kUWDm9Qy1gr8xnYiIrptOlPRANHF8MQrFc1OLeGKYqFuZy3EC8W6AM28NSWBCRfwqpWz9Y884lShcdxtcv5oBKLDorJpGasTkEg8Un60tQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20556" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20555">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3fppzlkKIvGmhDpIXDSFfcC0-XEzF7X4btUQszyCNZwfq6TwzF8JOPrvMrDAbqaNLQoSwRGjsnMq3PAI3WaZV_DP3KQoj-UzAmMyggp_EwD1vwqC99gSmiz0IHfPDCuSIKOpXgh28xaazyTxJ9RDAc5Fx4bUkXDGN2dOb9dQC6ePr0DDNwlUdgRCOLULzBCJIFXR9ASuyHp6Wh2rC_wWz9S2CNdiXDW2k3Mk3QEpxxbAkWwrv6RULccR0GAU6jMfeNykiz0G8w1LNTfuj3SM4PDu7mYGskCPg8QTkjyFbPWRm0M7uAEj9b4zYW_Qj91wLXHEnahGNwsxkfJi312YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20555" target="_blank">📅 20:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20554">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارشات تایید نشده
از شلیک موشک از اصفهان</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20554" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20553">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">از اپوزیسیون هم شانس نیاوردیم !
این قاضی زاده تا دیروز فعال سیاسی بود از امروز شده فعال بازار شت کوین !</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20553" target="_blank">📅 19:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20552">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ایالات متحده تحریم‌های جدید مرتبط با ایران را علیه بانک ترکیه‌ای گلدن گلوبال (Golden Global Bank) اعمال کرد</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20552" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20551">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مثل این است که یک مرد مدتها با یک زن غرغروی منفی باف گوشت تلخ زندگی کند و با کلی بدبختی و پس از سالها صبر از او جدا بشود و بعد در ازدواج دومش هم با دختری با دقیقا همین مشخصات ازدواج کند و همان فحشهایی را که به اولی میداد به دومی هم بدهد!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20551" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20550">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مثل این است که یک مرد مدتها با یک زن غرغروی منفی باف گوشت تلخ زندگی کند و با کلی بدبختی و پس از سالها صبر از او جدا بشود و بعد در ازدواج دومش هم با دختری با دقیقا همین مشخصات ازدواج کند و همان فحشهایی را که به اولی میداد به دومی هم بدهد!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20550" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20549">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این ترامپ رسما دیوانه است!
رفته خودش این کوین وارش را به جای جرومی پاول آورده بعد امروز وارش را تهدید کرده که یا نرخ بهره را پایین می آوری یا تجارت با کشورهای دارای مازاد تراز تجاری با آمریکا را متوقف می کنم!
همین هفته پیش وارش گفته بود تورم بالاست و تمرکز ما روی مبارزه با تورم است و شاید نرخ بهره را بالا ببریم!
جالب اینکه همان پاول فلک زده را هم خود ترامپ در دوره اولش آورده بود و بعد هر روز به او فحش میداد که چرا نرخ بهره را پایین‌ نمی آوری!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20549" target="_blank">📅 18:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20548">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش مشابه</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20548" target="_blank">📅 18:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20547">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش حسین پاک از تپه های علی الطاهر!  به گفته او، تپه های راهبردی یادشده از دید نظامی سقوط کرده اند</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20547" target="_blank">📅 18:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20546">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حالا اینقدر بچه ها نگران این تپه نباشند؛
ماشالله اینقدر تپه هست برای فتح کردن !
مثلا یک تپه ای هست به نام امین الطاهر که کنار علی الطاهر است و هر کس به آن نگاه می‌کند طلسم می‌شود و فیلم «تپه ها چشم دارند» بر اساس داستان این تپه ساخته شده.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20546" target="_blank">📅 17:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20545">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d58b19c9.mp4?token=s2eMT1UhLnYfmShyoAH0D833xxXdPtLtFo9A3guBCJIyQbcbLzCPMjUBccVLtJtzDpWSqokaQfiWxuhEbxouVk5d_ZOq7o79x1XosntHXrzjhOAr4CJw05EDv2mqZVE1_w-7Hf5Mjac9j1UBIDHVQgr9amirszEk_wL35nEZQMy_rHNKylgvRFUmEljHjoINM8y27qEpp3mLU_JbRXJzXxjxHab5B4aQFZqULzvTVKBJtH5q3Ciykhgk2CrIaYSuHegzomU_92o8Oj-ImyKqyZOi3iV54GrmRxEe_San1M8Cu46xAproEd3HMJ2AGYRJKAE5o3IiOPEKdN5CK3YTRmepnmKYyuMfN-ZJ-2xeNfFimxuK9FDS7xZ9IWd-P2lZG5uNiusgKduQ2noIlN8OVr1FvUaaU8WVldh1eYoRY-8T5BC1bX2iBkqIojcuaLBlr1u5i6Cyqw9fJ0b9v2WnBdgiTHLqtq1wU5hcGxxk1hMsaGmwccAKqdEeyIm_6TCTVrqUCh_0reME7xOHK7hMhd61OrL7WsNIO2P3JkmI7Xn-0uZ-KKT9DK2v5-oLzAc0VUdFdEiwWW-hSSMjT3qGCzBmGlWmhgIhOZVXjW3c6f4RqjFmrunDcHHwWg3oOOQr-B3JMoVyq55UHsBdU55YJZc9Pbyp4dvTQW-LBqMJ50k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d58b19c9.mp4?token=s2eMT1UhLnYfmShyoAH0D833xxXdPtLtFo9A3guBCJIyQbcbLzCPMjUBccVLtJtzDpWSqokaQfiWxuhEbxouVk5d_ZOq7o79x1XosntHXrzjhOAr4CJw05EDv2mqZVE1_w-7Hf5Mjac9j1UBIDHVQgr9amirszEk_wL35nEZQMy_rHNKylgvRFUmEljHjoINM8y27qEpp3mLU_JbRXJzXxjxHab5B4aQFZqULzvTVKBJtH5q3Ciykhgk2CrIaYSuHegzomU_92o8Oj-ImyKqyZOi3iV54GrmRxEe_San1M8Cu46xAproEd3HMJ2AGYRJKAE5o3IiOPEKdN5CK3YTRmepnmKYyuMfN-ZJ-2xeNfFimxuK9FDS7xZ9IWd-P2lZG5uNiusgKduQ2noIlN8OVr1FvUaaU8WVldh1eYoRY-8T5BC1bX2iBkqIojcuaLBlr1u5i6Cyqw9fJ0b9v2WnBdgiTHLqtq1wU5hcGxxk1hMsaGmwccAKqdEeyIm_6TCTVrqUCh_0reME7xOHK7hMhd61OrL7WsNIO2P3JkmI7Xn-0uZ-KKT9DK2v5-oLzAc0VUdFdEiwWW-hSSMjT3qGCzBmGlWmhgIhOZVXjW3c6f4RqjFmrunDcHHwWg3oOOQr-B3JMoVyq55UHsBdU55YJZc9Pbyp4dvTQW-LBqMJ50k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری صداوسیما:   ادعای نتانیاهو مبنی بر تصرف تپه‌های علی‌الطاهر هنوز به تایید شورای نگهبان نرسیده است</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20545" target="_blank">📅 17:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20544">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20544" target="_blank">📅 17:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20543">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbzOJx3oE6PilvHeeXGdNj8ZHqXXgwiA5TmshiP4wRUzl4EKmTb_LUycauvAtFpJhZQUA52ACXQLhPyhYwp6zq9jFlf1J7T4-bF4AlVW0jcCuOczGxu43LriaPEWNwa39PBxKYRLx3RNSxSB9DFRUwa9FG9FDeRKYVxiawcKl9MkweBoEOmFnZQtoNTLZ0Agiu82DnACkuVltCJKJm0UtwsUXRXlaB4tV9upFYI7BEefbA4Gym_Bgyy0KhtDgBYuw-iO4kquLXKQcZY4QyLc7-Q5B4MoVE87C-rhzKAl_mCftObrS0uXBPAM4P-jK4ZQRY6XSspK6K2SqnqHF_OGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20543" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20542">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">در‌ روزهای اخیر باز اسم عاصم منیر مطرح شده بود!  سبحان الله !</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20542" target="_blank">📅 15:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20541">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/20541" target="_blank">📅 09:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20540">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ظاهرا آرژانتین با حمایت ضمنی ترامپ به دنبال حمله دوباره به جزایر مالویناس (فالکلند) است.  جالب است که به محض انتشار این شایعه، استارمر بحث تروریستی اعلام کردن سپاه پاسداران را به جریان انداخت تا شاید از امتداد شعله خشم ترامپ جلوگیری کند.  اخیرا بریتانیا تصمیم…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20540" target="_blank">📅 09:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20539">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0YrqpX8Tl6gYoNBNhsDvPR81Ux9JQtavZC_lmZG5-jEzHvT-R2BNDW6bFaoQtqP8g72uBrFWsXOuhBvpL-cXJj0rwW42d3hJjqPx7gQvZdvVd9ROxLrMKpS21Twxum8pKyGBu_Ml0TxpJxnBe-rWwD7S40zgldlm7e2PRYwRZoQxDfAepDlt99QCJ8dJMYWGaTjeBTpTVPcZ7_00if42lNe_YO86_mJEKww_A3FnGWEJ2m8GAlXxAy3BqeLhBGw25YEDXolfy_twK7E9NOQgOuFm4QT-EL_mPhRANz70YodHbwndHma19qffafaQH3pkXpctMi5p5l1OzHzgXhYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش خنثی سازی مین ها از راه دور
این روش عمدتا توسط نیروی دریایی بریتانیا به کار می رود که تخصص ویژه ای در مین روبی دارد</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20539" target="_blank">📅 01:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20538">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB8a9AQ8MPi720bv69yjDeMMndhE48ooaCRjlhPIRkDwMmixgVbcWGQMuqsTLUMbWmQ-DMruIuZRlYeOj9wXVBkbxn_W49ZB3sBOi8w1QBQr1SRY0n7kMCHGTsF1aoxcKfx_j_SX0LFzoswCZWLEGKjxzYdd8qQAbTj7qrBuQkXFGWi7__FJ4n1kZOe_4aIhWa0LFnNfXwALJlsstG9YZfD7RhhpazokMNqCzQt9CNLmAbNoAmyd-12ICbwpxBzDSuqkLf96VU7T5IviZ5WXtZ7kiGXV8LgmmxBWalev2euszDU1E9v7fik_WBk8vyhyaKQ4uKQ9rJmaeDqj_Xomzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این گزارش های آژانس هسته ای و اظهارات تند ترامپ + نتانیاهو شرایط را به صورت قطعی به سمت جنگ می برد.  مراقب موج‌۳ باشید.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20538" target="_blank">📅 01:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20537">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20537" target="_blank">📅 01:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20536">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5fc46a9c.mp4?token=vdJw2oHdyeRxagp00AbB8z6XjRAyCfnupIZvznn2F40MCY_5Ph6ypt9gAQNiZ0wRb04aOBX36nWqaPgfJ0FOFv3dtBbAlXszgDb79_U9W5VUu-EKTOfykHrYFlOXbunMu773AD9_Pi0XTMgAuQ9P-NcdLWfPQJCAY3YATUuqirq4SvoivRSVyxcLgRsVcUpHwOCidxYigjegEAQbHqqgVQ_VXgt2Tj2Qa8MUfLBDmdpgZUQdnd0P7KWjaIhYDWwFQ4jgbO03zMUQOWaf4iMWpRHHNWy3xl1ZZORHVTroJWQt1SupORPvpb3_JnMz31ojUrDTp8KJcG3SmCXRrCNggg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5fc46a9c.mp4?token=vdJw2oHdyeRxagp00AbB8z6XjRAyCfnupIZvznn2F40MCY_5Ph6ypt9gAQNiZ0wRb04aOBX36nWqaPgfJ0FOFv3dtBbAlXszgDb79_U9W5VUu-EKTOfykHrYFlOXbunMu773AD9_Pi0XTMgAuQ9P-NcdLWfPQJCAY3YATUuqirq4SvoivRSVyxcLgRsVcUpHwOCidxYigjegEAQbHqqgVQ_VXgt2Tj2Qa8MUfLBDmdpgZUQdnd0P7KWjaIhYDWwFQ4jgbO03zMUQOWaf4iMWpRHHNWy3xl1ZZORHVTroJWQt1SupORPvpb3_JnMz31ojUrDTp8KJcG3SmCXRrCNggg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20536" target="_blank">📅 01:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20535">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار سوریه به فارسی 𓂆</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f5a76c78.mp4?token=L_sxv2QpxOItkeYgwnABjt7mAEp6dmGMn2mXKWKp0_hlHZLBUmCLNBWJ1z558asQg5hzV7nl_QbCDSJEtVMVKTRNCb3quqCh0ZbciOd75NEhfVTd0czW6HTLXWIpG2fiNk_8rp48GY3L8l5iRWzcp_rbLhF5Sj_HUnRRtYRtPmT8FZOqOtetDixLaw-MkuDNCltTnD5NZSQN4P06Qdo7qfCpvw0kcc_k3nnKGs6Xat-g4sID-WAOqNyGG0ai6ZJzYKVq2U1V2SxI5LWrVddEmSaKzZVFdNuBWExbbo3hGavlvdQuoXkZ-CDGzzhk8jPL-TESrjib8ir7iXQFOyEpyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f5a76c78.mp4?token=L_sxv2QpxOItkeYgwnABjt7mAEp6dmGMn2mXKWKp0_hlHZLBUmCLNBWJ1z558asQg5hzV7nl_QbCDSJEtVMVKTRNCb3quqCh0ZbciOd75NEhfVTd0czW6HTLXWIpG2fiNk_8rp48GY3L8l5iRWzcp_rbLhF5Sj_HUnRRtYRtPmT8FZOqOtetDixLaw-MkuDNCltTnD5NZSQN4P06Qdo7qfCpvw0kcc_k3nnKGs6Xat-g4sID-WAOqNyGG0ai6ZJzYKVq2U1V2SxI5LWrVddEmSaKzZVFdNuBWExbbo3hGavlvdQuoXkZ-CDGzzhk8jPL-TESrjib8ir7iXQFOyEpyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حالا درسته اسرائیل علی طاهر رو اشغال کرده ولی اینکه ترامپ پای یه کاغذ پاره رو امضا کرده به شما حس خوبی نمیده؟
@SyrianToPersian</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20535" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20534">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فشار اقتصادی آمریکا بر ایران در حال تشدید است
رویترز
کارزار آمریکا برای محدود کردن صادرات نفت ایران و بستن مسیرهای دور زدن تحریم‌ها، فشار قابل‌توجهی بر اقتصاد تهران وارد کرده است. کاهش دسترسی ایران به ارز خارجی، محدود شدن کانال‌های مالی و افزایش هزینه شبکه‌های غیررسمی انتقال پول و کالا، توان تهران برای مقابله با تحریم‌ها را کاهش داده است.
مهم‌ترین ضربه، افت شدید صادرات نفت ایران است. بر اساس داده‌های Kpler، بارگیری نفت خام ایران از حدود ۱.۷ میلیون بشکه در روز در سال گذشته به حدود ۲۶۰ هزار بشکه در روز کاهش یافته است. این کاهش، درآمد ارزی ایران را به‌شدت محدود کرده و همزمان با سقوط ریال، تورم نزدیک به ۷۰ درصد و افزایش هزینه واردات همراه شده است.
ایران همچنین با محدودیت ذخایر بنزین مواجه است و یکی از مقامات ایرانی ذخایر فعلی را حدود دو ماه برآورد کرده است. اختلال در کانال تجاری امارات نیز فشار بر واردات و تأمین کالاهای ضروری را افزایش داده است.
از منظر سیاسی، واشنگتن امیدوار است فشار اقتصادی تهران را به مذاکره وادار کند، در حالی که ایران تلاش دارد هزینه‌های اقتصادی و تورمی جنگ را به مسئله‌ای برای سیاست داخلی آمریکا تبدیل کند.
برای بازارها، پیام اصلی این است: اگر محاصره نفتی ادامه پیدا کند، ریسک کاهش بیشتر صادرات ایران و فشار صعودی بر قیمت نفت افزایش می‌یابد. در مقابل، تشدید فشار اقتصادی می‌تواند احتمال واکنش نظامی ایران در خلیج فارس و تنگه هرمز را نیز بالا ببرد؛ بنابراین بازار نفت با یک ریسک دوطرفه مواجه است: کاهش عرضه ایران از یک سو و احتمال اختلال گسترده‌تر در مسیر هرمز از سوی دیگر.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20534" target="_blank">📅 00:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20533">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شلیک موشک از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20533" target="_blank">📅 00:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20530">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4SvTST8M9yF2GkQGyVFZm62Z-PMDgVeVOBoUpHEwYWufPiEXpS7W9eRb3sGR6-r-oqEiAoe1zpgTTQeEtHjFF0F0VimgSa-h7y2KkJMwDJMc7m_wXEDgsBX_NlHSAMGYRBv3S-3UfVJa2LvouXtxuAWNHaqhDsaT9cW_Ld35vI8iKx19eCFy3o4m_POKXYwSS6vlZjcqbEp1ZyEBcf6AsbFwXEWVy80T0WR_mNoz5wOHdG81k6Blul2HTXl8goP_ve7AqyH__1XGCNGFqCgDfxrJCrcqFgZy20QirjeiVckQqywXafug58C-mOej6BFbUccb84nWxM1dq7M9EFcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20530" target="_blank">📅 00:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20529">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20529" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20528">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBGvlO8XguvWgeHeou_FXZTESwIkiDDZWi1RAIF9kiuUamJlbt3W_Nyr9Kd7k1YJN2VIdn-vLhhUrMzm-sJssuDbqsyL3VHTT58XmxmkbKfR0NjFj3SzmQWvMpuJX4SCl05sI1R8PCfs6Up4gqa6cw__Xpyc2RzthUtJkABhGXh7QmUwhAnYCO0bFzUUVRRvhcsIOHA7G6-zSBl3zKmoJfoJRLDqiZsLNttSOCK72kz9seTuOqD938k0IQR0yGc9tKVZR_jf6xJdVsl6w5CNVe6oA3k1GxsgLjPRXZ7BCnKbVqtXNXmISVqZb6G8F8U6EyBEEw6omxN83obZuQ1qrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۸ سال بعد از حمله هوایی ، اسرائیل اعتراف می‌کند که مشاور اتمی ارشد اسد را در یک حمله شبیه به سبک مافیا به قتل رسانده است
در ۱ اوت ۲۰۰۸، غواصان اسرائیلی به ساحل سوریه در نزدیکی طرطوس نفوذ کردند، به ویلای تعطیلات سرهنگ‌کل محمد سلیمان، مشاور ویژه رئیس‌جمهور، حمله کردند، او و مهمانانش را در حال شام خوردن یافتند و سه گلوله به پشت سر و گردن او شلیک کردند. این موضوع را اهود اولمرت فاش کرده است.
«در روزی که سلیمان حذف شد، جنگجویان ما از آب بیرون آمدند – تیراندازان چابک ماهر،» نخست‌وزیر سابق در یک خاطره‌نویسی جدید نوشت.
«او را با قطعیت شناسایی کردند. با وجود اینکه تعداد زیادی از افراد روی ساحل حضور داشتند، هیچ‌کس متوجه آن‌ها نشد،» او  مدعی شد و توضیح داد که چگونه کماندوها به‌صورت بی‌صدا به خانه سلیمان نزدیک شدند در حالی که او و مهمانانش روی یک تراس باز نشسته بودند و از فاصله‌ای حدود ۱۵۰ متر به او شلیک کردند.
«سر او به عقب افتاد. بلافاصله پس از آن، جنگجویان به سمت آب عقب‌نشینی کردند و راه خود را به سمت قایقی که آن‌ها را برداشت، باز کردند،» .</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20528" target="_blank">📅 22:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20527">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">امروز چند بار تتر تا ۲۰۰ تومان ریزش داشت!  به نظر عده ای دارند نقد می‌کنند   تارگت کماکان ۲۴۰</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20527" target="_blank">📅 21:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hK4H9D4PKO0if9npzxGYsBkdeZ4EpMjJCSlvR-7prAcd4Y57-c_BZ85JYfGYOGXrO8-oAFt03mZ-Qg6pqNkoEPIAkDvYXhxa3xp3FtCZcDkSCVJ5xwOUyKq1lqYSGRsBcUCPTORjcuQRbXV96sIjqg0bAzww9Y3wzdsrAbvxul_NZl3qE_FuLdkgbl7Zeyiby4DMce_sraRDOq15-N8tPMQ3swb8AOrSyrsAK1JxD6lX_Dsa5zWhZ9cBPhugWruiQN3olyDQtzjU9KHHo0oGLuBKO9DYNl1VrXNXWxUJ2Er1q1vh6Ek7CodJvPvpwSBfXTzjUEbzQ1IvMczap9F-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا یکی به نوید ممدزاده بگه  وقتی روی مواد هست  گوشی دست نگیره  مرسی  @PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20526" target="_blank">📅 20:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20525" target="_blank">📅 20:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سبحان الله این محمدسامسینگ ما چه انگلیسی اش خوب شده!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20524" target="_blank">📅 20:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20523">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قالیباف خطاب به وزیر خزانه‌داری آمریکا</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20523" target="_blank">📅 20:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTisJk-KaYV9UXt2G2TXBlMsTBtqXnuG92oHqrX88tkFy194lJz3Dz8EAFlxSvcsrVhKltndrvpue1iBR5ycCiO0OI1E9fx9wOsUf9-8DnEXBcvVeY3hIe2GIFs7LFOrNjUglAhASiq3fcfYZ1Iitbe-GTZw0jXs0OzSq0zKTnPTj33Buo2FmKDjwIoOhBZaHwBQ2WxMLfs64tcVolO2BXw-QaYIpoycmDJE_qBVVgS8aME6qCwmIIPkgRWm-lCu1JHOagYfp7D1c8-cqxsKAZgmO5lyF4xSxKx-9FAjhaRG9TkIFBLKK7NdBw50tTCepCq22qOOF01xmwhPpyYVKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف خطاب به وزیر خزانه‌داری آمریکا</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20522" target="_blank">📅 20:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20521">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">موشک‌های ایرانی به سمت کشتی‌هایی که مقررات تنگه هرمز را نقض کرده بودند، شلیک شدند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20521" target="_blank">📅 20:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20520">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل، در مورد ایران:   ما با تهدید نابودی توسط رژیمی روبرو هستیم که می‌خواهد از بمب‌های هسته‌ای برای نابودی ما استفاده کند.  من به توانایی خود برای از بین بردن این تهدید برای همیشه، یعنی سرنگونی این رژیم، اطمینان دارم.  این ماموریت…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20520" target="_blank">📅 19:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20519">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل، در مورد ایران:
ما با تهدید نابودی توسط رژیمی روبرو هستیم که می‌خواهد از بمب‌های هسته‌ای برای نابودی ما استفاده کند.
من به توانایی خود برای از بین بردن این تهدید برای همیشه، یعنی سرنگونی این رژیم، اطمینان دارم.
این ماموریت اصلی است که هنوز پیش روی ماست، اما نزدیک است. غیرممکن نیست؛ در دسترس است.
آنها بی‌دلیل از حمله به ما اجتناب نمی‌کنند. آنها به همه حمله می‌کنند، فقط به ما حمله نمی‌کنند. آنها قدرت ما، قدرت بازوی ما و عزم ما را می‌دانند.
من به طور کلی به دشمنانمان می‌گویم: با ما درگیر نشوید. اگر چیزی یاد گرفته‌اید، با ما درگیر نشوید. ما قدرت، عزم و وحدت درونی برای غلبه بر شما را داریم.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20519" target="_blank">📅 19:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20518">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۱۸ سرباز پاکستانی در یک حمله چریکی در منطقه زیارت بلوچستان کشته شدند.   گروه BLA مسئولیت این حمله را بر عهده گرفته است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20518" target="_blank">📅 19:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20517">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">۱۸ سرباز پاکستانی در یک حمله چریکی در منطقه زیارت بلوچستان کشته شدند.
گروه BLA مسئولیت این حمله را بر عهده گرفته است.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20517" target="_blank">📅 19:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20516">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بفرمایید:  پنتاگون آزمایش کمبود تستوسترون را روی مردان بالای 30 سال آغاز خواهد کرد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20516" target="_blank">📅 18:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20515">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ولی خداوکیلی این آمریکایی ها ترسناک هستند؛ شما فکر کنید هوموی مفعولشان اینطور خشن است وای به حال هتروی فاعلشان!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20515" target="_blank">📅 18:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20514">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0y2B7jpnVJ-unu8GY8xmnzBUo9Mm8RPE_dM56GthqlhnH9Y_Sq2miOfpd2wwjKtlX6riN9rg-jAIebWq0VvfWPyvZWbL1gHEo8GjLqnwooUtw2zVKNRS-XEJh3L58_mUoM_7UI8y5k8P5QSEjO8sOLeGElPLWFnSd4zF74qbhq7GO8lverBCjGBU9EJiKKD1ZxItWqPtgTk0ppaX6yRpSu5H3OtoNJWnWPDBl1IBhbordZLAK3h_VkZ2ib4glZ9U2kwNgnusaqeX9VHJKureMSg25JqG-Og7y98aA3WHxw4FS7mP8mmboaIZT-y5zo3RJvRzk9xlc4EGdxyt6BEFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل دقیقی است. تمایل جناح تندرو تداوم همین وضعیت است تا هم فشار برای بهای نفت و اقتصاد کشورهای منطقه و نرخ های بازدهی اوراق بدهی آمریکا حفط بشود و هم هیچ تعهد جدیدی برای خارج کردن اورانیوم بشدت غنی شده و برنامه موشکی و .... داده نشود.  طبق این  دیدگاه، نهایت…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20514" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ :  برای آن آشغال‌های  خائنی که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کند، ما عملاً مقادیر نامحدودی مهمات با درجه متوسط ​​تا بالا داریم، بسیار بیشتر از آنچه که می‌توانیم برای این جنگ یا برای هر جنگ دیگری (که بسیار بعید است!) استفاده کنیم،…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20513" target="_blank">📅 18:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ :
برای آن آشغال‌های  خائنی که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کند، ما عملاً مقادیر نامحدودی مهمات با درجه متوسط ​​تا بالا داریم، بسیار بیشتر از آنچه که می‌توانیم برای این جنگ یا برای هر جنگ دیگری (که بسیار بعید است!) استفاده کنیم، جنگی که به احتمال زیاد می‌تواند رخ دهد.
علاوه بر این، ما در حال تولید مهمات در سطوحی هستیم که قبلاً هرگز دیده نشده است. ما در حال ذخیره و آماده شدن برای هرگونه احتمالی هستیم. ما آنها را برای خودمان، ایالات متحده، به جای فروش به دیگران می‌گیریم، اما فروش به متحدان به زودی دوباره آغاز خواهد شد.
همچنین، لطفاً اطلاع دهید که دولت بایدن مهمات بسیار بیشتری را بدون هیچ هزینه‌ای برای آنها، نسبت به آنچه ما در ایران استفاده کرده‌ایم، به اوکراین داده است. صدها میلیارد دلار به اوکراین و ناتو، رایگان، داده شده است که اروپا می‌توانست آن را بپردازد - اگر فقط از آنها درخواست می‌شد، اما ما آن پول را درخواست خواهیم کرد، هرچند کمی دیرهنگام!
از توجه شما به این موضوع متشکرم. رئیس جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20512" target="_blank">📅 18:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20511">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSEZIjpraXWkrWPLQunT_FbytmZFEknNZ7sLiKb9VQ_PQk_AoMZbuRq44cft4dOgxWhslvz20GDUqXsuxrmWSPmYjWzD2I6dcEA0BkGT5Yqa50LJr62OnF-d6xqgF_QZQjHCdKP6Z6q3QVq6_UAN-qCS4Sr2A_NaO4UOuZaW6Zt94jYUwEKnL9No2QSyKzrsfxXjt8oIWaLVmSqdEC7kqrs3qGvQ6XkXyl6bkNTqb58cru3Vs_a0W6Gu9vEHthGbikuGK28DRDnu6X4BrXQ55Wqyrs06ADv_Ni8PDBMMDknyWqnoRTalaMk8jZZU2l_0PHd2CFrKzY92Zj6ZNo0Sng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار باز دارد پارابولیک رشد می‌کند و من خوشم نمی آید  فکر‌کنم تا ۲۰۰ پولبک بزند.  تارگت کماکان ۲۴۰ در گام نخست</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20511" target="_blank">📅 18:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20510" target="_blank">📅 16:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20509" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#سکه  عیناً مطابق سناریو ترسیمی رفتار کرده تا کنون. شکسته شدن خط مقاومت مورب یعنی سکه دوباره برای بالای 200 میلیون تومان خیز خواهدبرداشت. (برای موج نهایی صعود)</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20508" target="_blank">📅 15:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">در حملات هفته‌ گذشته آمریکا؛ ۳ خلبان و ۶ افسر نیروی دریایی ارتش نیز کشته شدند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20507" target="_blank">📅 15:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20506" target="_blank">📅 15:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار جنگجویان حزب‌الله مستقر هستند.
— رويترز</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20505" target="_blank">📅 15:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20504">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2LL3YhitsrwTTz9WLZtxaHpvxJgudx5ciZfsU6ka2I9ti9UKJ7KJKVEzSiW7jU7fvRczeOa5hU7ZOTim9nOJE_pO5iUjm8W4-YOsltFkqgFRv6T90v6UbRvUmdUaJPpyjrUomiBsNB3oxsWO5vlcA0i-72RtlwMiFfEVFcJV8ukdk2PIqzRWTjmTqYATxv3OpF_7WypUOQBWLwPXSv2MZFVoM_vQJqVUjB0xvlIoKdTPB-hn_zuz5mUhSkma782pOErR6iiwkB7mCzAS-WwNcNuWKH-1caO5e6xbpomBbCb0mkq63QW-twJVwoMxGiis1iGDn5FSA7WemB2fmY2Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستایش ترامپ از نقش آفرینی جدید سوریه در ارائه مسیر جایگزین برای هرمز !</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20504" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آزمون های  pte و mcq  هم بعد از تافل و GRE برای ایرانیان مقیم ایران لغو شدند.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20503" target="_blank">📅 11:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آزمون های  pte و mcq  هم بعد از تافل و GRE برای ایرانیان مقیم ایران لغو شدند.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20502" target="_blank">📅 11:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حمله ایران به پایگاه های آمریکا در کویت!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20501" target="_blank">📅 11:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📌
نرخ بازدهی اوراق آمریکا در آستانه ۵ درصد؛ بازارها آماده یک شوک نرخ بهره می‌شوند؟  افزایش بازدهی اوراق ۱۰ساله آمریکا به محدوده ۵٪ می‌تواند فشار مضاعفی بر سهام، طلا و دارایی‌های پرریسک وارد کند و هم‌زمان دلار را تقویت کند.   اما اگر رشد نرخ‌ها از نگرانی درباره…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20500" target="_blank">📅 11:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkYuxSuTbr8iCD_2SR4KPPLu4LrYzCv0yj7wB_s0kBBAwJj3ubGECCJlMJFQ8tbpxC3-5_8yTBnaFumv1t4h2-PiH-rk_15Cme01UFQEN7iWEGmp_MI6CoI1gNfmSJMVMHzeTb4vN_Pbcyx75kXsDFpmdH7-r9KCWxSUEUScIGdzASQwEHssqjev2HMeK_mI0KScE4xjpPQ8CJB1uQPhzL56Bc5KwRQnCwY82tG3qMfkk5d9kFhrYx4RmFVReGzjtkNKkQqMfMtTO-GxqLiQaKns749omarsMLvAVuYiVRUrRIqlap2oTtV_y2YRgMjCQnGgcpf8StP9NbQuNsc4cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20499" target="_blank">📅 11:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFRrcz1zMS5V9fXZbKVUk0OKstSgU3fLs6-eIRM71iipMKBircPMwtskY7yxaZFQFA4UNk0leycDDMAwjHfVl3HDMsv-TRJRoNs8hMKXLwMMf-17EozsFKsKkVlmkBB97zWYmHVWwG_pYBwXjrWHLjYU9sqwqjd78dcg06LLaSflq8n_-UnTDaC4OIyguPViWcfOj7I9s_bipRJyzlbliWsEbk_Nz67fXiN5lRnOj0oxwdbUxIDXwjEQdRXgiZrsiVJsS-Fevif5lxUdTHgjINw0YUZXjRQ9FWG6Z7AJukcGSvcQSKs91s4mYulo-r7hc6oUAhzNHJA11JIfioz1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نرخ بازدهی اوراق آمریکا در آستانه ۵ درصد؛ بازارها آماده یک شوک نرخ بهره می‌شوند؟
افزایش بازدهی اوراق ۱۰ساله آمریکا به محدوده ۵٪ می‌تواند فشار مضاعفی بر سهام، طلا و دارایی‌های پرریسک وارد کند و هم‌زمان دلار را تقویت کند.
اما اگر رشد نرخ‌ها از نگرانی درباره کسری بودجه و پایداری بدهی آمریکا ناشی شود، معادله می‌تواند تغییر کند؛ طلا به‌عنوان پناهگاه امن تقویت شده و بازارها با ریسک بازقیمت‌گذاری گسترده مواجه می‌شوند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20498" target="_blank">📅 11:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVA6BndWvp6-qLBmINsMlFWFoB7P9V6E8-Llwgh4icffENR2bNX0heJatc2-7UTNlq9qgMAUlreDlUuZ9oqrsmSZAFTbNGRgpkWytXhfabvRaGshhI9L3Tkrr7HWzkVoQ0IFKyFxy5_TzYgyCNB9hlcm2kZ6sU8vu5KaXnY4nzFeUXwliHlhSmJzCGy-k4R5ynOYATKrkKecLCakw9ksGh81fGFseq9CX125Ab4C1SQmrfGzAjstEMS15QFsGNxPYklzqw61TwBrHdjsvqoOcE7YsRdsO3ewYVDsdxtts2xzmPkSu46NhZFL9Yuo5WWbKIoEefX7JN7NxhQknyztyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20497" target="_blank">📅 10:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0447727037.mp4?token=CYgSB3bZrdBciu7FyVtZG5TnASum_fyVvf6T_biDUnIYd7ZvkIUZuxI2kwov8Ek54fTuHSH5lMmN5aqnghKkgeVfisN3cvctCRXY0v_QNHbL6fVQgKTBeejheOxFa-ydfyAa2bEvEUdFwiiZ6q7tWVfN-l5AAAzHlVqZIbkbkBAkrBGnVhrHCV9bZF3Xco2-bSxIFuC5PMeVXRfdDyMNokgopg3WxV50SUcRd3AzpY4Y-exU9ZAYoOA6vo068TnCIhwqDMgec2RUkktpykteOvDKbiIKaFk0Ry87TQJ6-IjV4I1OmyHsy6K4xBeL-9ZCcqLX4hJv7enV8MtdHub1aZ-Mtwh8y2wRIbRmcTfm0MRpmbug9dyFP26vrJJnCVmqUUvsVdkSiTJeGT6gxnag8RKhRyte9qjUm_m6G2FpNRlXz3lKGLZd7Pk9g0js_CRJHF3B6kOZ-wy4GFyESMgUD83_v6RKC9CyHOx01AN1F6yd_NjFy7i7jcy38NJ748F7hUz8UbxJ2Ba-DNJTkv0rMqT9wncElzI84_B2MyNKJLVE8LrwAsCHomRFnp76PZ8E2dD8ODAGZGBu7ZsxgKI5_EuJFEzfUDL0oEj1RoU1ShyhyhZHp4IUux_THGiP544b4YZlY8p6k08iaIKwePlHKc7_azrgfV07SefTywmJNjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0447727037.mp4?token=CYgSB3bZrdBciu7FyVtZG5TnASum_fyVvf6T_biDUnIYd7ZvkIUZuxI2kwov8Ek54fTuHSH5lMmN5aqnghKkgeVfisN3cvctCRXY0v_QNHbL6fVQgKTBeejheOxFa-ydfyAa2bEvEUdFwiiZ6q7tWVfN-l5AAAzHlVqZIbkbkBAkrBGnVhrHCV9bZF3Xco2-bSxIFuC5PMeVXRfdDyMNokgopg3WxV50SUcRd3AzpY4Y-exU9ZAYoOA6vo068TnCIhwqDMgec2RUkktpykteOvDKbiIKaFk0Ry87TQJ6-IjV4I1OmyHsy6K4xBeL-9ZCcqLX4hJv7enV8MtdHub1aZ-Mtwh8y2wRIbRmcTfm0MRpmbug9dyFP26vrJJnCVmqUUvsVdkSiTJeGT6gxnag8RKhRyte9qjUm_m6G2FpNRlXz3lKGLZd7Pk9g0js_CRJHF3B6kOZ-wy4GFyESMgUD83_v6RKC9CyHOx01AN1F6yd_NjFy7i7jcy38NJ748F7hUz8UbxJ2Ba-DNJTkv0rMqT9wncElzI84_B2MyNKJLVE8LrwAsCHomRFnp76PZ8E2dD8ODAGZGBu7ZsxgKI5_EuJFEzfUDL0oEj1RoU1ShyhyhZHp4IUux_THGiP544b4YZlY8p6k08iaIKwePlHKc7_azrgfV07SefTywmJNjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف طولانی بنزین در مملکت دوست و برادر روسیه!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20496" target="_blank">📅 10:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حمله ایران به پایگاه های آمریکا در کویت!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20495" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYdiDW7gWmVgNUOSB5d2X_YCgfTz6z_8Kd1QwYL-QHcINuQBuD25iJOIWxGuGnBMG_qZeI3gATEEJUYsEBhJRgc9eCLpGvGd1LLfZHvC3yfoYTD5nXm-UjfG5zsnqGPFLpbmDVd2-M5Gij_fgd2qER29IEFIbvQPDr16E2v6Y619BdRkkBNjcRF_CjulbKDUH4knnVDiBxmOphigPIxtFw5T-I7sdVVSBGugLnFvw-fY67dHkyCzOKXzVfQjGQnac8tj99kjIp9JaQD9UvlO55T4Xr592Cxcofm4wQDtu1ZysZOEYY9gSOj_0-SPMcuNT6-hB3_Dy6E1F5S8QfbLhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20494" target="_blank">📅 01:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انتشار اخباری از انفجار در میناب!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20493" target="_blank">📅 01:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انتشار اخباری از انفجار در میناب!</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20492" target="_blank">📅 01:27 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
