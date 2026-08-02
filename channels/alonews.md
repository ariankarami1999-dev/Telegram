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
<img src="https://cdn4.telesco.pe/file/jhWrHEXaDTewVdE73FgELzETTSfQ3LI-ETZeGK3gNg4Pi0uP9yal59u1pPDFG9oX_lpbn0ofCgfaFVyHfgUZ-r3K_x7XPF1FXToEJcWtHpvL_GIS7jLwFi82wz_uQ_n2PoHKb80ZP83-wdFm6Ba_jXYAs6XhOGrOEB2xssd4ulb1O2Ek3J4co0O53SMaScyRpwa7XDKEmGOdF7qAu4qwR7w5eI-T35odgi9RrOnAlVuPX1jqbLFp5cxDSriBQQocha2NZ3YMvDz8Z5PzeK5npMO70OyrE5wJASwCQPY--laJRE2eeAm3Ku0prJeqP6InbzFlwRI91l-oQ6XIs0Mr3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 991K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 10:57:27</div>
<hr>

<div class="tg-post" id="msg-139318">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری /  باراک راوید از اکسیوس: ایران با طرح بازگشایی تنگه هرمز موافقت کرده است
🔴
به گزارش باراک راوید به نقل از دو دیپلمات آگاه، عباس عراقچی وزیر امور خارجه ایران، بامداد امروز با طرح مصالحه‌ای که با میانجی‌گری قطر و آمریکا برای بازگشایی تنگه هرمز تدوین شده بود، موافقت کرده است.
🔴
بر اساس این گزارش، موافقت عراقچی یکی از دلایلی بود که دونالد ترامپ را به لغو حمله برنامه‌ریزی‌شده علیه ایران ترغیب کرد.
🔴
طبق این پیشنهاد:  ورود کشتی‌ها به خلیج فارس از طریق آب‌های سرزمینی ایران انجام می‌شود.  خروج کشتی‌ها از خلیج فارس از طریق آب‌های سرزمینی عمان خواهد بود.
🔴
همچنین میانجی‌های قطری همچنان در حال رایزنی با تهران هستند تا اطمینان حاصل کنند که سپاه پاسداران نیز از این توافق حمایت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/139318" target="_blank">📅 10:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139317">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فایننشال‌تایمز در تحلیلی نوشته ایران با عبور از واکنش دفاعی و گسترش درگیری به پایگاه‌ها و مسیرهای حیاتی کشتیرانی، ابتکار عمل را در تقابل با دولت ترامپ به دست گرفته است.
🔴
به باور نویسندگان، هدف تهران فرسوده‌کردن توان آمریکا، افزایش هزینه حضور منطقه‌ای آن و سلب اختیار واشنگتن در انتخاب میدان نبرد است؛ از تنگه هرمز و دریای سرخ تا کانال سوئز.
🔴
این راهبرد پرریسک است، اما یک پیام روشن دارد: جنگ دیگر فقط جایی رخ نمی‌دهد که آمریکا انتخاب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/139317" target="_blank">📅 10:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139316">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
روبیو: ایران تحت فشار واشنگتن، بیش از هر زمان دیگری آماده توافق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/139316" target="_blank">📅 10:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139315">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
الجزیره: ایران یک پیشنهاد از سوی آمریکا دریافت کرده که می‌تواند به کاهش تنش‌های کنونی منجر شود و تهران با جدیت در حال بررسی آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/139315" target="_blank">📅 10:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139314">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
روزنامه عبری هاآرتص: رئیس‌جمهور آمریکا به مهارت‌های خود در ساختن معاملات افتخار می‌کند اما در نهایت استاد لفاظی‌های توخالی است.
🔴
او مسائل را تا آخرین حد پیش می‌برد به این امید که ابتدا طرف مقابل عقب‌نشینی کند.
🔴
سپس پیروزی بزرگی را اعلام می‌کند و با اصرار سایر طرف‌ها به ایرانی‌ها فرصت دیگری می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/139314" target="_blank">📅 10:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139313">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
یکی از نهادهای امنیتی هلند در گزارش جدید خود اسرائیل جزو طرف‌هایی که نگرانی‌های امنیتی برای هلند ایجاد می‌کنند، طبقه‌بندی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/139313" target="_blank">📅 10:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139312">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf749ff64.mp4?token=KUMtivegGWefPc3eFW7c33ag2RtWnTsdRvA0rYhr5xPJbJbZikkaR1yabvnLBr2A1pC-Tf4qqlGmV6TDzHBFrzFIyxyy9qCEngk3SeTCgeEUOCdn_A-eNpqTZlbvGKwZC93wU2asVfrOiKiflSek8_jMFk18ykruz40E9vb9-ZO_Kb_S-a9sBi-1HjQVktaeXS6Nhty92IkuwdwDe4msMH-fsi0lda52yC81C91JK0JLIMrR1S3_etsuwOlWxx_AyHfA7N8ABGm6JbVWhEqi8xIZmg0e_a9yMjMcJFMBvkc117Dg-0XopsuBQDAa70zvDpiMnocHfiiNbYzXrI0mOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf749ff64.mp4?token=KUMtivegGWefPc3eFW7c33ag2RtWnTsdRvA0rYhr5xPJbJbZikkaR1yabvnLBr2A1pC-Tf4qqlGmV6TDzHBFrzFIyxyy9qCEngk3SeTCgeEUOCdn_A-eNpqTZlbvGKwZC93wU2asVfrOiKiflSek8_jMFk18ykruz40E9vb9-ZO_Kb_S-a9sBi-1HjQVktaeXS6Nhty92IkuwdwDe4msMH-fsi0lda52yC81C91JK0JLIMrR1S3_etsuwOlWxx_AyHfA7N8ABGm6JbVWhEqi8xIZmg0e_a9yMjMcJFMBvkc117Dg-0XopsuBQDAa70zvDpiMnocHfiiNbYzXrI0mOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: حکومت ایران باید تغییر کند؛ ممکن است سرنگونی رخ ندهد، اما خود حکومت باید تغییر کند؛ آنها می‌خواهند انقلاب را صادر کنند؛ این موضوع حتماً باید تغییر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/139312" target="_blank">📅 10:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139311">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نیویورک تایمز: مقام‌ها و تحلیلگران غربی معتقدند که از دیدگاه متحدان آمریکا، جنگ با ایران ظاهرا به سمت شکستی راهبردی پیش می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/139311" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139310">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
روزنامه نیویورک تایمز گزارش داد که هم‌پیمانان آمریکا نسبت به این موضوع که جنگ با ایران به سمت یک شکست راهبردی سوق پیدا کند نگران هستند.
🔴
هم‌پیمانان آمریکا می ترسند که ناتوانی در ایجاد تغییری پایدار در ایران، نقطه‌ ضعفی را آشکار کرده باشد که روسیه و چین از آن استقبال خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/139310" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139309">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ایهود باراک، نخست وزیر اسبق اسرائیل:
توافق با حماس کاملاً اسرائیل را نادیده می‌گیرد و شامل خلع سلاح این گروه نمی‌شود
🔴
حقیقت تلخ این است که ترامپ به نتانیاهو توجهی نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/139309" target="_blank">📅 09:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139308">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302146c665.mp4?token=InaW20he6voybdPohebN05vbakGebFbI8OpCFn5YtAFWT1D11VojljSuxdLgi1i3kk1NZU057msiSM3pfyM0Wa7SrQPK4cVa5RL36LvbJN97dsqkVbEv8NbPX0audDvGefKPAwRIM8skfwzOfsdglTGbaHOUJkJC_xrumgbo102LcUtWiXaQzM9531EohfvZ2tJwZkMN6kvqYTMq30ymWkb8hgwOR_PM7DGoI9Cid1T2oEr-ML5p3M3iZu43AIhGJbsEAwt8Vny2lvg-RoYzOjXxtT76sNAENZPRyr6oo-bDCtP3HIbCldZkIcZ5NaLVMQjiUpOD5lf4eJ2EhIsgRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302146c665.mp4?token=InaW20he6voybdPohebN05vbakGebFbI8OpCFn5YtAFWT1D11VojljSuxdLgi1i3kk1NZU057msiSM3pfyM0Wa7SrQPK4cVa5RL36LvbJN97dsqkVbEv8NbPX0audDvGefKPAwRIM8skfwzOfsdglTGbaHOUJkJC_xrumgbo102LcUtWiXaQzM9531EohfvZ2tJwZkMN6kvqYTMq30ymWkb8hgwOR_PM7DGoI9Cid1T2oEr-ML5p3M3iZu43AIhGJbsEAwt8Vny2lvg-RoYzOjXxtT76sNAENZPRyr6oo-bDCtP3HIbCldZkIcZ5NaLVMQjiUpOD5lf4eJ2EhIsgRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: ما تصمیماتی گرفتیم که به کشورمان آسیب زد؛ مثلا گفتیم «برای ما مهم نیست که کالاها کجا ساخته می‌شوند؛ بگذارید در کشور دیگری ساخته شود، مادامی که قیمت‌ها برای آمریکا ارزان‌تر باشد»
🔴
این کار به صنعت‌زدایی از کشورمان و از دست رفتن میلیون‌ها شغل انجامید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/139308" target="_blank">📅 09:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139307">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سی‌ان‌ان‌: عربستان به عنوان یک متحد کلیدی آمریکا در خلیج فارس، نفوذ قابل توجهی بر ترامپ دارد
🔴
وابستگی دیپلماتیک واشنگتن به ریاض در خاورمیانه، تأثیر زیادی بر تصمیم ترامپ برای عدم حمله به ایران داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/139307" target="_blank">📅 09:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139306">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a01601cdd0.mp4?token=Ms-B0LqIqDTlIOGDXrgrm1BNTT7P5HlaV41pLfsctOhKvSLvMEit5piYXJorNrJzoAfb8BpHHcEPEfrIMuAyzeFYWq5p5-aIjU1fDXz9Bso5SSp9ZwSK56ATfddNTb8JL-HCZusI35pQCmcZ8lYrud0gzw1F2GXA3pjVKJz-nfII_pEqTITF55p5c04jDvjMkKKdJ83W2t3e-2TxnZk4Jdh9_g7_LV74HITRZ9jfdPntvd3agx3OkFjkJMj9rYZRw5JU4NsItJ9Texjis2FYJDAadZVVM5mDRyYzCbCElvNu6MxDmOIpMvJeiHvy9AfGMmtiHIYo57k2M_N7RbK7TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a01601cdd0.mp4?token=Ms-B0LqIqDTlIOGDXrgrm1BNTT7P5HlaV41pLfsctOhKvSLvMEit5piYXJorNrJzoAfb8BpHHcEPEfrIMuAyzeFYWq5p5-aIjU1fDXz9Bso5SSp9ZwSK56ATfddNTb8JL-HCZusI35pQCmcZ8lYrud0gzw1F2GXA3pjVKJz-nfII_pEqTITF55p5c04jDvjMkKKdJ83W2t3e-2TxnZk4Jdh9_g7_LV74HITRZ9jfdPntvd3agx3OkFjkJMj9rYZRw5JU4NsItJ9Texjis2FYJDAadZVVM5mDRyYzCbCElvNu6MxDmOIpMvJeiHvy9AfGMmtiHIYo57k2M_N7RbK7TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط مرگبار هواپیمای گردشگری در پرو با ۱۳ کشته
🔴
در پی سقوط یک فروند هواپیمای گردشگری در جنوب پرو، دست‌کم ۱۳ نفر جان خود را از دست دادند.
🔴
این هواپیمای سبک که برای پرواز گردشگری بر فراز خطوط باستانی نازکا به پرواز درآمده بود، با ۱۳ سرنشین دچار سانحه شد و سقوط کرد.
🔴
تصاویر منتشرشده از محل حادثه، تلاش نیروهای آتش‌نشانی برای مهار آتش و خاموش کردن بقایای هواپیمای سقوط‌کرده را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/139306" target="_blank">📅 09:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139304">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0109ff6de4.mp4?token=Z3bFvAOTr3fyqXnZDVR1YDsWGwCr1aieQLKzd1xuR7dYYYAQXsQ1R0lnjwmL_wAzUoOFQywajCwmj5t6zFCFjN5KopHDG3JV9ouyPo27vcukmGC_rK0YbR2R24Qi_wFXRio-Dn4kr9NT5PJ3Hv_8ZC8xjm3VLlVJ8GKgZ_oPd-YLLOAaCOTtEV9qYpahIJHhOvSukGbf8eiKYaxJTMwGcuhl2SUB4PDmuR5ZObJ8DZkeECRL1D0ZNTnaHemmzGin-FJQpro7jERRBV9OsLeGiHrNSL3rl7BQoEZKLjpeXcjzCMOgWocBoRQuIuugkXK80DClcR1iHJ4hphOe_0o8xA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0109ff6de4.mp4?token=Z3bFvAOTr3fyqXnZDVR1YDsWGwCr1aieQLKzd1xuR7dYYYAQXsQ1R0lnjwmL_wAzUoOFQywajCwmj5t6zFCFjN5KopHDG3JV9ouyPo27vcukmGC_rK0YbR2R24Qi_wFXRio-Dn4kr9NT5PJ3Hv_8ZC8xjm3VLlVJ8GKgZ_oPd-YLLOAaCOTtEV9qYpahIJHhOvSukGbf8eiKYaxJTMwGcuhl2SUB4PDmuR5ZObJ8DZkeECRL1D0ZNTnaHemmzGin-FJQpro7jERRBV9OsLeGiHrNSL3rl7BQoEZKLjpeXcjzCMOgWocBoRQuIuugkXK80DClcR1iHJ4hphOe_0o8xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای حمله‌ای اوکراینی امروز صبح به یک مرکز توزیع دیگر Wildberries در نووسمئیکینو، منطقه سامارا حمله کردند و باعث ایجاد آتش‌سوزی بزرگ در این تأسیسات شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/139304" target="_blank">📅 09:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139303">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6667d80879.mp4?token=YXM8wTxcJQ1ygqhSzfuWN7sEc539_AWq2WBCQMRxf2a8QYhLLWBdqgVFrxBaiYA7zgrR3OTtzA56fQ5s53RwRfBilrfBo7WD1nZK_4PN_di6lp8dOUy-z3uv_q5u5U5ymNMjD3PbVb1ehfbivKXWduIgtRpui4MYSFFi3duC5UpB8QT_eXfHwSKUod1RMpegU1c00WPiUlKD1l9TCWxwYFqv3K9UhzGLx9K07yEAwusls5pKZawBkrcNt-7eorVAFC23oQg4DFCGqm9xsccGDV6qqbIcbB6X5y4pgUGNZaKnmyY_jxtSI4LHUqeCgYX026rLBgK290hoSnSl-gA6ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6667d80879.mp4?token=YXM8wTxcJQ1ygqhSzfuWN7sEc539_AWq2WBCQMRxf2a8QYhLLWBdqgVFrxBaiYA7zgrR3OTtzA56fQ5s53RwRfBilrfBo7WD1nZK_4PN_di6lp8dOUy-z3uv_q5u5U5ymNMjD3PbVb1ehfbivKXWduIgtRpui4MYSFFi3duC5UpB8QT_eXfHwSKUod1RMpegU1c00WPiUlKD1l9TCWxwYFqv3K9UhzGLx9K07yEAwusls5pKZawBkrcNt-7eorVAFC23oQg4DFCGqm9xsccGDV6qqbIcbB6X5y4pgUGNZaKnmyY_jxtSI4LHUqeCgYX026rLBgK290hoSnSl-gA6ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل شدید در شهر شی‌آن واقع در شمال چین
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/139303" target="_blank">📅 09:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139302">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزارت دفاع روسیه: از دیشب تا حالا ۶۳۵ پهپاد اوکراینی را بر فراز شهرهای مختلف روسیه سرنگون کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/139302" target="_blank">📅 09:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139301">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWbLkPHBpfMmZZhXGmipSnZc0JiYfkaaj3nxYB9WwHONAN2VeD111lAMzJFhtSN_Bacgo-cfVkoJ7JHSVYvSvHw0tlI--ukR4D2TTd6yZE1RbGW0Al2LyGBdiAJjE4k02-3LIqA7DSpu7q3uOyXZUrNm-u-md8FqFgeG0IxVRWv91hOfFdWDE7DR9zReC7K61inDOdI89Val1EC5KWxcz9YtrxP4PaXdrywNvev4kiq89h5oaqhBMaK7WHBtRwgcFLqZJcOdwNbh3X4cU7Uj5Q2Kv02BvxnxfrCs1xxOd1MqMlF6iQxVtOgkhfzR6dV8xiruXnSXZcbBU6TXhh39UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی، مشاور تیم مذاکره‌کننده ، در واکنش به سخنان ترامپ گفت: همه می‌دانند که این یک خبر دروغ است، ترامپ عقب‌نشینی کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/139301" target="_blank">📅 09:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139300">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
اکسیوس: محمد بن سلمان، ولیعهد عربستان، امروز پیشتر با ترامپ گفتگو کرد و از رئیس‌جمهور خواست تا تنش‌زدایی کند و از انجام حملات به ایران خودداری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139300" target="_blank">📅 09:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139299">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ارتش کویت اعلام کرده چند پهپاد ایرانی را در شمال این کشور رهگیری و منهدم کرده و ترکش آن‌ها در جزیره بوبیان، نزدیک پایگاه‌های نظامی آمریکا، فرود آمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/139299" target="_blank">📅 09:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139295">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b32c7f4d.mp4?token=OXgSa1mO7HmDj3ZMuXHU6Rlon3Z9GpavUEJyDSihhS4vC6HuypZHUY2E5f2GDUVknw_iksqsmyw12B2o0bbHEIrxrhkffEpY0Xq8sOwsLArfEGGyENK7hZw8NmtaqTwNzfDoLZfILBMeSMYO4ix_1A77mIKvuhRDmLBMGAqL-f5N4u2ciWbgHWt7FmJyVqqwCiWPQkESPXcdwhQ3xtIHhJ_yqSrvzORHXCeeg88ud12qLWnfnvrqYl8zWE46SmeOT7FQgZ_tkZsfROl-PV_QKZpx03Mk3ctNXQAKhGWYPjDrMMMI7I818sedVJQY9ypTykRyTI-8zKFZRhzWKwsNDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b32c7f4d.mp4?token=OXgSa1mO7HmDj3ZMuXHU6Rlon3Z9GpavUEJyDSihhS4vC6HuypZHUY2E5f2GDUVknw_iksqsmyw12B2o0bbHEIrxrhkffEpY0Xq8sOwsLArfEGGyENK7hZw8NmtaqTwNzfDoLZfILBMeSMYO4ix_1A77mIKvuhRDmLBMGAqL-f5N4u2ciWbgHWt7FmJyVqqwCiWPQkESPXcdwhQ3xtIHhJ_yqSrvzORHXCeeg88ud12qLWnfnvrqYl8zWE46SmeOT7FQgZ_tkZsfROl-PV_QKZpx03Mk3ctNXQAKhGWYPjDrMMMI7I818sedVJQY9ypTykRyTI-8zKFZRhzWKwsNDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان آتش در شرق واشنگتن؛ هشدار تخلیۀ فوری صادر شد
🔴
در میان وزش بادهای سهمگین با سرعت بیش از ۷۰ کیلومتر بر ساعت، آتش‌سوزی مهیبی شرق واشنگتن را درنوردید و هزاران نفر را مجبور به فرار از خانه‌هایشان کرد.
🔴
خبرگزاری آسوشیتدپرس گزارش کرد این آتش‌سوزی حوالی ظهر شنبه به وقت محلی آغاز شد و علف‌ها و بوته‌های یک محوطه باز را سوزاند اما به‌سرعت به‌سمت شمال و شرق و به‌ سوی مناطق مسکونی گسترش یافت.
🔴
مقامات محلی، با اعلام بالاترین سطح هشدار تخلیۀ فوری، خطوط اتوبوسرانی شهری را برای خارج کردن مردم فعال کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/139295" target="_blank">📅 08:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139294">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
کیهان: دولت پزشکیان «آرایش جنگی» ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/139294" target="_blank">📅 08:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139293">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: سال تحصیلی جدید، از ابتدای مهر و به صورت حضوری آغاز می‌شود
🔴
اگر اتفاق خاصی رخ دهد، متناسب با شرایط درباره آن تصمیم‌گیری خواهد شد
🔴
تصمیم‌گیری درباره زمان آغاز فعالیت دانشگاه‌ها در حوزه مسئولیت ما نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/139293" target="_blank">📅 08:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139292">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
المیادین: تعلیق حمله آمریکا به ایران پس از تلاش‌های جی‌دی ونس، معاون رئیس‌جمهور، و رئیس ستاد ارتش آمریکا برای منصرف کردن ترامپ از این کار صورت گرفت
‏
🔴
موضوع کمبود ذخایر موشکی عامل کلیدی در تصمیم ترامپ برای تعلیق حمله به ایران بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139292" target="_blank">📅 08:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139291">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
روزنامه جمهوری اسلامی: برخلاف عده‌ای جنگ‌طلب، مردم و نیروهای مسلح دنبال صلح شرافتمندانه‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/139291" target="_blank">📅 08:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139290">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6b-TnWfZYfukdRqnXovnehTNnqdPiveQUHoarFQV4Iq8dU63Af4zugxneNrUmdB1x10Ao18a9x_k-KIKYfJhgYFCtdQ7XdjGnQjWbh2omm72G78vJ6cccJ19vA7VAgbAHKbMHx749T-OhZlgK7k4-qt7bFKWdK2LC0VUbEiaUiH90f_kk8TWKKl4B0E1grCTxdnS4SYcZ0bKs5fDYGJQH7_SckBrQgLbdKxDPf_vf3U8jNesfqyYNq1xQuI_dIgN9U2MT56Hc6kqUJlJQqMuLfKvBgfCIpvD-zr-mxLiuylaP267VTtdzUPPR5RQLTU-P5FHFjBXzGfWePFxkl-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ پس از تهدیدهای مداوم: با لغو حمله به تهران موافقت کردم
‏
🔴
ایالات متحده آمریکا آماده و مجهز به سلاح است تا علیه جمهوری اسلامی ایران، در سطوحی از ترور نظامی، قدرت و صلابت که از زمان جنگ جهانی دوم دیده نشده است، اقدام کند.
‏
🔴
با وجود این، ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب تعهداتی که مورد توافق قرار گرفته است، متوقف کنیم. این شامل بازگشایی فوری، کامل و بی‌قید و شرط تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران می‌شود.
‏
🔴
بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافقنامه‌ای دست یابم. کشور اسرائیل در این تعهد به من می‌پیوندد. همه دست به کار شوید و آن را انجام دهید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139290" target="_blank">📅 08:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139289">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60057c65fc.mp4?token=t2j8ZzWtTRRgI0QhjS3h_sKYL4kbMmrNOVSyEqCnZMQwDnjvJaZhDi-i4x790kIjy_t7VV1cmqsTtU8JYoRO6zn7-8qE_nsRRAlyx3XD4uYS20FSf7s53zDiBbA7CCfZb-dUT0N_A8tP8zWsOMSQ_uB98i0Ky3DOwO218ql6DV2zzxECW-eiKV4TXFussovwCM9r8hi2c-AvBqPaxUgfacApxI5zDu4xwwV5JYQxBtK9gWWQxYO2VMge1b_5ZzZ87yy-G7GgnlwkfyqA8zqfdM51TbFEy6MnodSMNW_ihopsY_NgQxc3wrh2Ol-ZStJMvnDUC3I7G_Eve-BOtPh_fyOQWFnBcpKOCIIbeH6TTjSicdB41tUGcwhRPgX2GyE42VHGvOL8CDSzGE82Zr8u9RLUlKOLVnsU3lc-kgQlS8FgwubX7c5wXT3UsifqyRNYDlcZ77oVksMGrW_ICqeQ394GWdzeSL2ZMT6eMvMe6Otw5zKLOv4vf43p0Q8cE-oty-GPvGA_Pf8IaXMJrmX6niul5SrV2d8ZAudLaawr_QJfzO3StBA-ApJ8A2EMDOQhysOqshDy8Twxo1zAj49hyir-9Z_yvRiTFyiJvAdZHoEHRXnS6UOaXvgRQ8nu_dP-hSqUVwyWDdY-BDGxrVVR5C3RmCrVLGnUh4KAbRaz7uE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60057c65fc.mp4?token=t2j8ZzWtTRRgI0QhjS3h_sKYL4kbMmrNOVSyEqCnZMQwDnjvJaZhDi-i4x790kIjy_t7VV1cmqsTtU8JYoRO6zn7-8qE_nsRRAlyx3XD4uYS20FSf7s53zDiBbA7CCfZb-dUT0N_A8tP8zWsOMSQ_uB98i0Ky3DOwO218ql6DV2zzxECW-eiKV4TXFussovwCM9r8hi2c-AvBqPaxUgfacApxI5zDu4xwwV5JYQxBtK9gWWQxYO2VMge1b_5ZzZ87yy-G7GgnlwkfyqA8zqfdM51TbFEy6MnodSMNW_ihopsY_NgQxc3wrh2Ol-ZStJMvnDUC3I7G_Eve-BOtPh_fyOQWFnBcpKOCIIbeH6TTjSicdB41tUGcwhRPgX2GyE42VHGvOL8CDSzGE82Zr8u9RLUlKOLVnsU3lc-kgQlS8FgwubX7c5wXT3UsifqyRNYDlcZ77oVksMGrW_ICqeQ394GWdzeSL2ZMT6eMvMe6Otw5zKLOv4vf43p0Q8cE-oty-GPvGA_Pf8IaXMJrmX6niul5SrV2d8ZAudLaawr_QJfzO3StBA-ApJ8A2EMDOQhysOqshDy8Twxo1zAj49hyir-9Z_yvRiTFyiJvAdZHoEHRXnS6UOaXvgRQ8nu_dP-hSqUVwyWDdY-BDGxrVVR5C3RmCrVLGnUh4KAbRaz7uE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اختراع عجیب یه گیمر ایرانی که وایرال شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/139289" target="_blank">📅 08:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139288">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrFAPJMpD0BkjV7jrjm8IHFgieB6QlgMo1tM7PF18Q_DvzGWGknTa7jOl8EAmSkOr2eaePwCZcnzYC1FEXjQPeFfjJJfX3S-xN3m4xRYvpfPHX0xIijyEZpupMf0DxKOalzZMxjYcGsSvE5a2zJz0R9yvoLSR-ds4qxPCaY8i0KPfJIAUPZA88ruXsENH7n4Dfsr5MkAObc7nWiAfTyrzsgqWF1qBTPr5IVfgC8Kx9gEHbBmfEmnxLw3tfeO-7sge0LqnDBSnSzp0gxmV3Ql-v1rwxA96rHwn7et1k48u1_SiZI8Ek7CLKsOSaty3w2VRTA-HDZgadmx_dBEdW6-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس
:
محمد بن سلمان، ولیعهد عربستان، درباره طرح ترامپ برای حملات گسترده به ایران ابراز نگرانی کرد!
🔴
بن سلمان در تماس تلفنی با ترامپ خواستار جزئیات بیشتر درباره این عملیات شد و از او خواست این حملات را آغاز نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/139288" target="_blank">📅 07:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139287">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gokUSl47mFPUwRPbC_ICrbhiEZDd5Oo0jVIPjRVFv5EC3nXyWHZCiwIBLchGh0hCPyepmj8s-XzFE5MeePgiHGGI3sWqUAgCfUGP3cngbn2cDu7yfWyfc33QZCMWKu24kafxKlidSfl0ZURnBMEKKkZanGtKzWvsxsgP0IpYrrGH_Kk1nrX4VBt20hSfsmzFYLDDFfccyX8FeSI6DcLqh8bGAZ0m7_HlvhmtXag7kAbEYImb1uI5Fbp5ALg7Lzd6s-_2OCsAfj1a0ES-c7yzoAqoCb-uiYGe9oqBSiRQL27a3mHHo6GXXRfprE2tMFLC7DDa3Ib5ohbKAOr1omvsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : حمله کنسله و مذاکره میکنیم
آمریکا مسلح و آماده حمله به جمهوری اسلامی ایرانه، با سطح وحشتناک نظامی، قدرت و زوری که از جنگ جهانی دوم به این طرف ندیدیم.
با این حال، ایران و چند تا کشور دیگه خاورمیانه ازمون خواستن حمله رو عقب بندازیم چون چارچوب یه توافق رو قبول کردن، این توافق شامل باز شدن فوری، کامل و تمام‌ و کمال تنگه هرمز میشه و تموم شدن تهدید هسته‌ای ایران.
بر اساس این درخواست، من موافقت کردم برای نفع آینده کل دنیا و همچنین بقای یه ایران موفق و آباد، حمله رو لغو کنم، به شرطی که بتونیم سریع یه معامله ببندیم. کشور اسرائیل هم تو این تعهد با من همراهه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/139287" target="_blank">📅 07:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139286">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbefa49090.mp4?token=GtK3oUbzdWGINx9UnM2nDBesk_3ZbdFi_FAmOtaUqCU1oR74em750CvyqB7c23moNgnRxkD6PPAwUtHCVTQS9nmuM3hjY45PiszicJX1UfjShtw73Rv36UlpAJqLX4yFv7xGnHyXvZAidSp6EaIwxLDozA-IFu6OgLkOkfxxVQgPOPCoCGlQE-Ea7_5WX3oHMfku53tcVd5Yl0JYuRiTx3G9sInit3O9NxJlISWE9KjHMqz_KNckmPd-QQZREnq3t7Wv-T3IDNlWwWqFs1W08JVU1ol-EMjElGgRZWhSrcip659YZc_lOg3Uc-mJ7OycnyMvLn5h9eG8FdSsvsV83Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbefa49090.mp4?token=GtK3oUbzdWGINx9UnM2nDBesk_3ZbdFi_FAmOtaUqCU1oR74em750CvyqB7c23moNgnRxkD6PPAwUtHCVTQS9nmuM3hjY45PiszicJX1UfjShtw73Rv36UlpAJqLX4yFv7xGnHyXvZAidSp6EaIwxLDozA-IFu6OgLkOkfxxVQgPOPCoCGlQE-Ea7_5WX3oHMfku53tcVd5Yl0JYuRiTx3G9sInit3O9NxJlISWE9KjHMqz_KNckmPd-QQZREnq3t7Wv-T3IDNlWwWqFs1W08JVU1ol-EMjElGgRZWhSrcip659YZc_lOg3Uc-mJ7OycnyMvLn5h9eG8FdSsvsV83Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت سیستم دفاع هوایی C-RAM در اربیل عراق برای مقابله با پهپاد های شلیک شده ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/139286" target="_blank">📅 03:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139284">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5db8baf5ba.mp4?token=LwN8T8sH6MhYIQ2XNfFNbcHMqNEfNaa46nvGG3q0FkoVWUWWB546nO_gcDQ0NqPqp6sANX9hS5kL7iuu-n3KptZjsMQx9gDlYrRMLC6r1QkktecRb3GS4Y4GK8iK3Ox7qzYXPGCoBjufXcOUF5TDs3-1MSnZOEMsT72wUMwMVcYJoSBVI4StAU-0njLBZgvTIFWbdG_Ny9Fwgr1-3SFLe2LcbmGjCQrNRlB9Cw6AkedN56p0DkTcbDLVvSGCXi9Sl4viGX2tfGxFoHi6NuLTOIlsqDNBtkVH0fuukAVxZVAPPn_96Iqv2K0XVzWSu2QpjTq0bIjgk5wE_t9lkonNyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5db8baf5ba.mp4?token=LwN8T8sH6MhYIQ2XNfFNbcHMqNEfNaa46nvGG3q0FkoVWUWWB546nO_gcDQ0NqPqp6sANX9hS5kL7iuu-n3KptZjsMQx9gDlYrRMLC6r1QkktecRb3GS4Y4GK8iK3Ox7qzYXPGCoBjufXcOUF5TDs3-1MSnZOEMsT72wUMwMVcYJoSBVI4StAU-0njLBZgvTIFWbdG_Ny9Fwgr1-3SFLe2LcbmGjCQrNRlB9Cw6AkedN56p0DkTcbDLVvSGCXi9Sl4viGX2tfGxFoHi6NuLTOIlsqDNBtkVH0fuukAVxZVAPPn_96Iqv2K0XVzWSu2QpjTq0bIjgk5wE_t9lkonNyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل سه نفر در پی یک حادثه تیراندازی جمعی در شهر Twin Falls ایالت آیداهو کشته شدند و دو نفر دیگر مجروح شدند. در حال حاضر، مظنون (یا مظنونین) این حادثه دستگیر نشده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/139284" target="_blank">📅 03:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139283">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
محجوب الزویری، کارشناس الجزیره و مدیر مرکز مطالعات خلیج فارس در دانشگاه قطر:
🔴
ایران یک پیشنهاد از سوی آمریکا دریافت کرده که می‌تواند به کاهش تنش‌های کنونی منجر شود و تهران با جدیت در حال بررسی آن است.
🔴
به نظر می‌رسد این موضوع با رایزنی‌ها و تماس‌های فشرده ایران با چندین طرف بی‌ارتباط نباشد؛ تماس‌هایی که بخشی از آن‌ها، از جمله با پاکستان و ترکیه، به‌صورت رسمی اعلام شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/139283" target="_blank">📅 02:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139282">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ اخیرا صحبتی نکرده و خبر اینکه حمله به درخواست چند کشور به تعویق افتاده سندیت نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/139282" target="_blank">📅 02:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139280">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
۱۰ فروند هواپیمای سوخت رسان آمریکایی در راه اسرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/139280" target="_blank">📅 02:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139278">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P63TB6y06C0OvBPuoZi2icmWYZSdi0BMI6Caelp-e_Bnj7zBMhlTaRJimpE7lPYEUhqV9Qvju-UzIJOsRoxUkQVCBNisawuFf8Nk1O93OIM3_j36o7Cm80NojzdPHvrX0te_a6ptKefzr8FkyQTlm8DxY-6DK8bGVLIrMredPnC4PNSMIsLXdYz92iVHlGJRdr5wwDe3YYuSOfioBrgi-rKZ2XaPB3SaFjIBVB7JXYEWVcxQa4CuJK4fxhNZz8-DvCausV7D1TapBXfN2NMFBY8Y5qMVSKJfVyqrifkVQ_fMVZDNp3i7xye9Eu9-z4lRRjbQXhaoPI6K9NmWYtrMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4d6ba904.mp4?token=FP4dpKNgcCV90NJTeW-GCgxxV29BnYNRh_8nzjoxBIP8HO3WyQYygpiIR58bSzqYs49DdxGvF_pcPQCpRYZIEwhWp4xjUiNQH4GPCk3W0f1qUU9uQeXzE9Rl6q_-kIMwRWh3ek5uK7yLXCCdZI77HR70GMlUoEHD6zq9njkpCb3y12-wvomJ2dsaaUtGPWMnWlEhxZMLHX9R5G0RzV69yONVPufcSKkUVGOpKmZGz6KDWh7lBIjs69K1HBX9CNocpDy5T_kbmnoKhL4zbI1I6QgITKW3yOuF5F-U44bun3m5fMSAELdM1JCyfhd9LqQqTdPtJJhpz9v1OURVkZ52Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4d6ba904.mp4?token=FP4dpKNgcCV90NJTeW-GCgxxV29BnYNRh_8nzjoxBIP8HO3WyQYygpiIR58bSzqYs49DdxGvF_pcPQCpRYZIEwhWp4xjUiNQH4GPCk3W0f1qUU9uQeXzE9Rl6q_-kIMwRWh3ek5uK7yLXCCdZI77HR70GMlUoEHD6zq9njkpCb3y12-wvomJ2dsaaUtGPWMnWlEhxZMLHX9R5G0RzV69yONVPufcSKkUVGOpKmZGz6KDWh7lBIjs69K1HBX9CNocpDy5T_kbmnoKhL4zbI1I6QgITKW3yOuF5F-U44bun3m5fMSAELdM1JCyfhd9LqQqTdPtJJhpz9v1OURVkZ52Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دعوا در صدا و سیما:
نادره رضایی که سابقه کار در وزارت ارشاد داره و یک تایمی اطلاعات هم بوده در واکنش به اعدامی‌ها استوری گذاشته بود که اعدام فقط بذر کینه میکاره در دل مردم
حالا واکنش صداسیما هرچی از دهنش دراومده بهش گفته که چرا همچین استوری‌ای گذاشته چون اعدام کار درستیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/alonews/139278" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139277">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02089f299.mp4?token=rhJH00irsvFOiwMnvc6Lpeo22FVGj3gxWBAKCPJBldEByOJx4uHhdGmrnQBh0nTskGe_ast-RDWlBRRwgSePVZ6k9LO3wRx8nzRfqwiVgfoPEjUQc-yxxmkfkrAM9BEPrJ3KiErGI0eqYiUoWDaMvU48E5x_9r1KPJGYlkoi011wiYm2uVNyF4JSWPrV5VFoLZeAU6N614Z7OoL6-XxXKIWAw1ghbY77oBPQVvcpJ0ILJXvKFqW15rdWH_20ehmC-YdBjt0wbZ7CaMZWnFzI2hrrC4yN4mTo91zOS4jOqkMGLpjaxoW4SBJKio9D9e969r0jSVtRnEYEJ2MNwabmqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02089f299.mp4?token=rhJH00irsvFOiwMnvc6Lpeo22FVGj3gxWBAKCPJBldEByOJx4uHhdGmrnQBh0nTskGe_ast-RDWlBRRwgSePVZ6k9LO3wRx8nzRfqwiVgfoPEjUQc-yxxmkfkrAM9BEPrJ3KiErGI0eqYiUoWDaMvU48E5x_9r1KPJGYlkoi011wiYm2uVNyF4JSWPrV5VFoLZeAU6N614Z7OoL6-XxXKIWAw1ghbY77oBPQVvcpJ0ILJXvKFqW15rdWH_20ehmC-YdBjt0wbZ7CaMZWnFzI2hrrC4yN4mTo91zOS4jOqkMGLpjaxoW4SBJKio9D9e969r0jSVtRnEYEJ2MNwabmqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به سلیمانیه ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/139277" target="_blank">📅 02:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139276">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4645f6ca50.mp4?token=RpT2izB6LkpEpsSFdkNokUu5Fz42c9ZVeG9e3juy9tIO7h_6Ek9mHm19OD4UGPm1S3q2CI_y2fGb9b2UVnJ3KIzeu6KUeDJdQBAEpALY46teYeQ7H-ENTrgdaojXBnzoPhO9fJsUG7LVoEYgttRXbb4j6QAaHxAB7nQUALokICMXudKbJd0Ch8kP4iaYrdFNxMv3VpY1OGOnlMzgoM3xH8gnYpK4TejcmQbEtw_EcgGuNEyfsaR_CS9FlPOHWH5YH1sMO01lB7oJ__5C7KOEf_TkClIcl4ekHeTdKFITY7c9G5p5_j63q2ihBZHXOsbQ1G_B5kyVayeWpx7_J3N15XuMjaU5AdYfE5jcwdtoOVdfVp6BOA5AaQA0Wzv0QDci4xO8JCjBDk60yyU0BL76V7GPM9FSj3HC9Gms4YWfRnQIbaF0MgFWubrTA43_EmvhnMm1rDxEGXJ1wdMwirRBT5x6ENyjpaXMzMkAFrdQfo7ssxIzLSjK6fItr8idtp_b-wfxBCf7IMIq4tSd6D8BAbDJaPTGjRbmvKKfMh92uQKtEolvEa9fGZTf_7_bj2E5kGPQcHyBrZXwqwtGvILtqF8ZUyE9TpAVlUO-tz8Fh_3Nm1JjtOCup0iDNTbjsaWyqAQIXOayKVn_S_7QRt9noi44M-XL0Od_VzwbTgAQORQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4645f6ca50.mp4?token=RpT2izB6LkpEpsSFdkNokUu5Fz42c9ZVeG9e3juy9tIO7h_6Ek9mHm19OD4UGPm1S3q2CI_y2fGb9b2UVnJ3KIzeu6KUeDJdQBAEpALY46teYeQ7H-ENTrgdaojXBnzoPhO9fJsUG7LVoEYgttRXbb4j6QAaHxAB7nQUALokICMXudKbJd0Ch8kP4iaYrdFNxMv3VpY1OGOnlMzgoM3xH8gnYpK4TejcmQbEtw_EcgGuNEyfsaR_CS9FlPOHWH5YH1sMO01lB7oJ__5C7KOEf_TkClIcl4ekHeTdKFITY7c9G5p5_j63q2ihBZHXOsbQ1G_B5kyVayeWpx7_J3N15XuMjaU5AdYfE5jcwdtoOVdfVp6BOA5AaQA0Wzv0QDci4xO8JCjBDk60yyU0BL76V7GPM9FSj3HC9Gms4YWfRnQIbaF0MgFWubrTA43_EmvhnMm1rDxEGXJ1wdMwirRBT5x6ENyjpaXMzMkAFrdQfo7ssxIzLSjK6fItr8idtp_b-wfxBCf7IMIq4tSd6D8BAbDJaPTGjRbmvKKfMh92uQKtEolvEa9fGZTf_7_bj2E5kGPQcHyBrZXwqwtGvILtqF8ZUyE9TpAVlUO-tz8Fh_3Nm1JjtOCup0iDNTbjsaWyqAQIXOayKVn_S_7QRt9noi44M-XL0Od_VzwbTgAQORQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگ و دعوای یه خانوم از طرفداران پهلوی با یکی از طرفداران جمهوری اسلامی
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/139276" target="_blank">📅 02:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139275">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ee3d85b0.mp4?token=PBBj5rBZ-SBtVVddX8bA455dcfL-jX1mS8YGpTJCaIyUZ1LXCF26ZNiktp_lv3wLxzFpJWTj64oFDz_WcdkwBcLmt_7q3bKPbCgPDgugOS2nxSsTcTCcYMjDLxi1LebxOsBNrbTMBaNr9D71XRHQ1muL4Lihj4oEDob825NiBpereMox9iEoW-7Cgu0qMcrNUQjukhOkMbIFebHGRowfh_gzNaFQs4gkKsVXyfHCCZCHwGWWWTmIKk226Ubh4fY96piBjPApYNm2j7lrMaVmUrBfVSlxupsRoC2AqC23pmDFgzaTKjy6PDz4wU-mjWvoLpQBSuwpM-NHz09pKtbocQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ee3d85b0.mp4?token=PBBj5rBZ-SBtVVddX8bA455dcfL-jX1mS8YGpTJCaIyUZ1LXCF26ZNiktp_lv3wLxzFpJWTj64oFDz_WcdkwBcLmt_7q3bKPbCgPDgugOS2nxSsTcTCcYMjDLxi1LebxOsBNrbTMBaNr9D71XRHQ1muL4Lihj4oEDob825NiBpereMox9iEoW-7Cgu0qMcrNUQjukhOkMbIFebHGRowfh_gzNaFQs4gkKsVXyfHCCZCHwGWWWTmIKk226Ubh4fY96piBjPApYNm2j7lrMaVmUrBfVSlxupsRoC2AqC23pmDFgzaTKjy6PDz4wU-mjWvoLpQBSuwpM-NHz09pKtbocQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی که هم اکنون پیت هگست وزیر جنگ آمریکا منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/139275" target="_blank">📅 02:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139274">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
انفجار در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/139274" target="_blank">📅 02:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139273">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d31d8e0b0.mp4?token=VgZ7wy45NImdpzfDl3X_A34u6KwOUqDhsFTU_fCObiI-qgMv1q6dnyVIr_QX49ZWkhO573RfN9bg0c_swcoeSuLxOHOqTUbxbIPYA427yQnhlGq7KqDlHqPdn-53DbOjbCo1WIcyh455CDXHxSjieOc6jTsmrVE6MB7wWEjZCA5DRQU3yTTcCrR9s4dKhIwWUF1x1KAIdiHf3QVqwKXbG0KLWYT1t53dbejlzUyUNXIW0269Dg8K9vNbWRXieVJqYGh01m9wFcAiCArgTaVI4Q35jZocTK-80cx9bTtzE-XvhmzD9ovQtDMcNVCUA4AHesElGBNak0IRxezL0d9MjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d31d8e0b0.mp4?token=VgZ7wy45NImdpzfDl3X_A34u6KwOUqDhsFTU_fCObiI-qgMv1q6dnyVIr_QX49ZWkhO573RfN9bg0c_swcoeSuLxOHOqTUbxbIPYA427yQnhlGq7KqDlHqPdn-53DbOjbCo1WIcyh455CDXHxSjieOc6jTsmrVE6MB7wWEjZCA5DRQU3yTTcCrR9s4dKhIwWUF1x1KAIdiHf3QVqwKXbG0KLWYT1t53dbejlzUyUNXIW0269Dg8K9vNbWRXieVJqYGh01m9wFcAiCArgTaVI4Q35jZocTK-80cx9bTtzE-XvhmzD9ovQtDMcNVCUA4AHesElGBNak0IRxezL0d9MjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات موشکی مستقیم به پایگاه‌های گروه‌های کردی در شهر سلیمانیه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/139273" target="_blank">📅 02:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139272">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c5bac489.mp4?token=RXuIktkPlJvcM6QkoVQTcJfD6DunV3rag7mv3lnrp6d4J4_M5Y2vLr3-B-47tBeAfHm_4TMOOU7DuPKmt7OPb1V5wOrsWaeYHqKWAUVok1ZjWSZRlJikEKHpg6ntRie06EsBmN0nyHUJ_ICpf4ojkPOAI4zaAQYLAZpxrCfLw2rqhyuDRRNNWhBwIHUtBxbnGGXlEPjc6STNrkyN78bkTF5tVxUTrBWZVEmWtGxVsTnICQTgrLgcJ9FMfb27YwqemUdrYccoKu79UBuW3-6X8gM4iH019Udo01gn_B0AeLYydRCI7BmD--tmDrRWQbfgrSJ1IQLKJYI69Bz9vUQ4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c5bac489.mp4?token=RXuIktkPlJvcM6QkoVQTcJfD6DunV3rag7mv3lnrp6d4J4_M5Y2vLr3-B-47tBeAfHm_4TMOOU7DuPKmt7OPb1V5wOrsWaeYHqKWAUVok1ZjWSZRlJikEKHpg6ntRie06EsBmN0nyHUJ_ICpf4ojkPOAI4zaAQYLAZpxrCfLw2rqhyuDRRNNWhBwIHUtBxbnGGXlEPjc6STNrkyN78bkTF5tVxUTrBWZVEmWtGxVsTnICQTgrLgcJ9FMfb27YwqemUdrYccoKu79UBuW3-6X8gM4iH019Udo01gn_B0AeLYydRCI7BmD--tmDrRWQbfgrSJ1IQLKJYI69Bz9vUQ4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارهای پیاپی در سلیمانیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/139272" target="_blank">📅 02:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139271">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a6713f7a.mp4?token=AC_jHTu5s_thcN3E19B5ChIg5NzuTuz_T6_92O8ZmNCIZhDG1fmboEwMqJJ76mhhOLWLMzz4P1zbVyDQ_Fl5NNETTli7q5viDbM8D0BDZsBtSX-9zGoJIgYPkMuarGFG-wPm2h7BxEZ7Ey7PtfpAtX1T7JRPv0bVC_egBa0hZHcY_Oi9pRUXiZTTaBz16Uv6fQIeUpVElm_0NhxMpI9092RsyCgN4S5x_z_wpjfpW8Ad1izJZyW1HyrXstzWIaCSKtLm9Ztfxv_NE_ePco3zztkF-jc8dMBRthdGsI1EJ3A5fIflxxEJjqNaELCD71vFiX_Lj2lMrKxBsRzTHVGN5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a6713f7a.mp4?token=AC_jHTu5s_thcN3E19B5ChIg5NzuTuz_T6_92O8ZmNCIZhDG1fmboEwMqJJ76mhhOLWLMzz4P1zbVyDQ_Fl5NNETTli7q5viDbM8D0BDZsBtSX-9zGoJIgYPkMuarGFG-wPm2h7BxEZ7Ey7PtfpAtX1T7JRPv0bVC_egBa0hZHcY_Oi9pRUXiZTTaBz16Uv6fQIeUpVElm_0NhxMpI9092RsyCgN4S5x_z_wpjfpW8Ad1izJZyW1HyrXstzWIaCSKtLm9Ztfxv_NE_ePco3zztkF-jc8dMBRthdGsI1EJ3A5fIflxxEJjqNaELCD71vFiX_Lj2lMrKxBsRzTHVGN5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت پمپ بنزین های تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/139271" target="_blank">📅 02:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139270">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
پروژه جدید مجید واشقانی سلبریتی حکومتی
🔴
اینا فکر کردن تا یکیو بشونن اونجا روسری سرش نباشه بی حجاب باشه ما قراره فراموش کنیم که چه خیانتی علیه مردم ایران کردن
🤔
دوران بزن در رو گذشت سلبریتی دوزاری
#پروژه_حکومت
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/139270" target="_blank">📅 02:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139269">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c26747e9.mp4?token=rkraDlYa1YlJD40at_x9q3-1ZzojUUZrRU_ZczE9gqh2OLrAmkC9KcblhEaeNF3rcb4ZtNxDkWTynALyRKJ6YxNS21VWI_1x8aF9KZ6o7ErlXo4sXXf6bLWtvijf86Jj4UeeXv5LXfn1tP_ssSlkl0ZbCUfhhLlDe-yCQr8Ihul1HlAcOG39HWHBFpOqpbdPApGO54csxXzjenPAhK3pLeMuSUy-MrXs33OUakoIAiDMvXKKGb9MJT7bofXuwR0bUJVERkSyUcGel3agn4EmIyFIOvsJKB9gf9ry1643dlukvMwWNlPAWXSr-ichBWHDC1q_M2KOmbhTmDUdN6JbVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c26747e9.mp4?token=rkraDlYa1YlJD40at_x9q3-1ZzojUUZrRU_ZczE9gqh2OLrAmkC9KcblhEaeNF3rcb4ZtNxDkWTynALyRKJ6YxNS21VWI_1x8aF9KZ6o7ErlXo4sXXf6bLWtvijf86Jj4UeeXv5LXfn1tP_ssSlkl0ZbCUfhhLlDe-yCQr8Ihul1HlAcOG39HWHBFpOqpbdPApGO54csxXzjenPAhK3pLeMuSUy-MrXs33OUakoIAiDMvXKKGb9MJT7bofXuwR0bUJVERkSyUcGel3agn4EmIyFIOvsJKB9gf9ry1643dlukvMwWNlPAWXSr-ichBWHDC1q_M2KOmbhTmDUdN6JbVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
فیلمی از حملات پهپادی شدید به سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/139269" target="_blank">📅 01:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139268">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0687a51d47.mp4?token=X9QyAED4cXSrFrDvXeWqve_hVmM1cnCKn_eU4gkCTQgvwe5qbVAKq92lx_a4zo04aNH7kicMIwSQO-nhAT3UFTG3OAzdQRb3Ugd9Yr8cTb_6x3_hMOZ6R7UxWmCd4gi0UDP_gEUvjvzEydD4_auWf97Un3qXWPahMbgm9TBdiGGRJ0yvVg03WX__AoDTQBTSWkLI1Jn45FsGklb_dA86trX-6ywBigjhJQEDKAPunWf0QmGEY1HmrfDH-c-oK489l6a9CO1EgX5TyV8RNxshWMWBXz4YRYuwcEuCP6Y-QF2ZTWP93QiMlTAju7XZstTcQJE_mHbxnzCLEpjwVT3QrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0687a51d47.mp4?token=X9QyAED4cXSrFrDvXeWqve_hVmM1cnCKn_eU4gkCTQgvwe5qbVAKq92lx_a4zo04aNH7kicMIwSQO-nhAT3UFTG3OAzdQRb3Ugd9Yr8cTb_6x3_hMOZ6R7UxWmCd4gi0UDP_gEUvjvzEydD4_auWf97Un3qXWPahMbgm9TBdiGGRJ0yvVg03WX__AoDTQBTSWkLI1Jn45FsGklb_dA86trX-6ywBigjhJQEDKAPunWf0QmGEY1HmrfDH-c-oK489l6a9CO1EgX5TyV8RNxshWMWBXz4YRYuwcEuCP6Y-QF2ZTWP93QiMlTAju7XZstTcQJE_mHbxnzCLEpjwVT3QrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسیب مستقیم به مواضع گروه‌های کرد در سلیمانیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/139268" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139267">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/261b2bbe98.mp4?token=ZkCaymL2Q9s4XCVqtRmM_Mcq-YxypO7Z1QJA3rYWb9xlMbDwtibFkq6WUj-OwrwumFqkwqc4HKg2hbhNNWFrbte4JGxKHAelhHla_YZOxhFMMCcJwMZwSRnZtXFqKlKPeZR2FBLOetq1bLPOydbz07PjL2suZW5bSsULJEaB4rQMiZ3JauJ2GShMx2zrOlwiP9cc_wW3zdVHTM-K6Px1hLT08_kevo2WJTl6me-TsAYk4TstYtDLGTA80mmLzd8oJ_DpnntsYubKyfhcpHfpcbUMfYpY7pfckJrJN_disbrFWd2UWPXYVb-dcmKK5krERLQRI0aBXprMHiDzSVmcUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/261b2bbe98.mp4?token=ZkCaymL2Q9s4XCVqtRmM_Mcq-YxypO7Z1QJA3rYWb9xlMbDwtibFkq6WUj-OwrwumFqkwqc4HKg2hbhNNWFrbte4JGxKHAelhHla_YZOxhFMMCcJwMZwSRnZtXFqKlKPeZR2FBLOetq1bLPOydbz07PjL2suZW5bSsULJEaB4rQMiZ3JauJ2GShMx2zrOlwiP9cc_wW3zdVHTM-K6Px1hLT08_kevo2WJTl6me-TsAYk4TstYtDLGTA80mmLzd8oJ_DpnntsYubKyfhcpHfpcbUMfYpY7pfckJrJN_disbrFWd2UWPXYVb-dcmKK5krERLQRI0aBXprMHiDzSVmcUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی:
اگه آمریکا به ایران حمله کنه کجاهارو مورد هدف قرار میده؟ آمریکا دست‌ کم به ده دسته از اهداف کلیدی و استراتژیک تو سراسر کشور هدف حملات هوایی و موشکی انجام میده.
1- بمباران مداوم مراکز نظامی سپاه پاسداران در جنوب
2 - شهرهای موشکی و پهپادی در عمق خاک ایران
3 - تاسیسات هسته‌ای "کلنگ گزلا"
4 - مراکز نظامی در تهران و بقیه استان ها
5 - سامانه های پدافندی و راداری
6 - پایگاه های هوایی نیرو هوایی ارتش
7 - مراکز و نهاد های حکومتی
8 - ساختار های سرکوب
9 - مقامات ارشد باقی مونده
10 - صدا و سیما
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/139267" target="_blank">📅 01:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139266">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رهگیری در اربیل در اقلیم کردستان عراق.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/139266" target="_blank">📅 01:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139265">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کانال 14: بیمارستان‌های اسرائیل در وضعیت آماده‌باش بالا قرار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/139265" target="_blank">📅 01:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139264">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjqHnjcR5uf3oIy3GygNTD3QC9LwLiODWH5U3Uy05ZUY8iLR2pxjltYulc5UU2KxxO6S9e4iIAN5q8iqIvF2IMj2T9HIkp9eGZegLPtdb5c_9c3j7KcSs6IznPrb6MMfeEoKxAOkqwu_QfDOTKHhLLHMcLeaZt1mSE7Ak3mPPGfChd-l9UN3-ep_xu_M3_ZF7XSqLwP0b6IySZ8j-NzOSbJw2Qn4FQ_QH70Tiw0oTiLji32B9zHoXXe0Q0pYtde-uBa7Mda65MEkLw2m3_5BDoWueD3LTUaLtwb9dYJtpsThlzpvhoLOnY5VExqXAdzTAALNakY_oaxaFSIsA20snA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
سخنگوی وزارت خارجه به جای استفاده از نام «بحرین» آن را «رژیم جدا شده از ایران» خواند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/139264" target="_blank">📅 01:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139263">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQMX5QtQ8UTRTRE4mQyKD46-H5Nav9Mthuy1EJMI97ZtZTQMgnL5zuWwkErIrOhK9QU5vFg2b-zbk9mKZAAwu5INd-j5jz3MrrqNsfGXo9AOZhYHYbdX3PEfHYlpOOQsh0FXAzBeLFSuI_XY-k_S2qk_hilozCqW5d9wxu4s4DEvXosfaFe9VXjFluQ2r7RDjt-guboij3hXEn5dewsz_442W9Wuyc0KV-Rfrk8TYjNXXro4BX__yrRUtwavmLAQGpuSZ58rw3RLcVoNUozOqnK5E-EB8Lv9j-mKwq3B7YDP5SJ0Vlx67zyS6tACcnlmciV_4lXkvgEDgrH0ZvDLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه فروند هواپیمای سوخت‌رسان آمریکایی از نوع KC-35R پایگاه هوایی شاهزاده سلطان در عربستان سعودی را ترک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/139263" target="_blank">📅 00:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139262">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=rYDwWhsqGL22uSR42A9COlt7Xf8Oupon_YwyXNZZ95Z44Pvli4o4o1vI2LNs2HhrQx0y6qehVFqYDaPBuuvtWvCMKuv7O27iLJUdzAw3wOvA3QBUDOC5xw2dv_r_fiFfKhQ5DYIM6VVDmsJ5lOAZWBYE2_khIxZsg5khYOaIO3xl2Mbc8WUZooHFta0gXWtKmBQt_rRQlznQwsQ51EKrchsy2XfXkUT55gfhGzFy9ZPRKQbTU1CvtGfilTnX4Y1rZa4Za2IjgRDk3ooCYt4fubJDDwX2vXgaivssV0aFTtZMmpUcbAQmqMYMVLZ4qOqWEJEZKYj8Xwskdj4pIbEZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=rYDwWhsqGL22uSR42A9COlt7Xf8Oupon_YwyXNZZ95Z44Pvli4o4o1vI2LNs2HhrQx0y6qehVFqYDaPBuuvtWvCMKuv7O27iLJUdzAw3wOvA3QBUDOC5xw2dv_r_fiFfKhQ5DYIM6VVDmsJ5lOAZWBYE2_khIxZsg5khYOaIO3xl2Mbc8WUZooHFta0gXWtKmBQt_rRQlznQwsQ51EKrchsy2XfXkUT55gfhGzFy9ZPRKQbTU1CvtGfilTnX4Y1rZa4Za2IjgRDk3ooCYt4fubJDDwX2vXgaivssV0aFTtZMmpUcbAQmqMYMVLZ4qOqWEJEZKYj8Xwskdj4pIbEZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداسیما:
مسعود رجوی (رئیس سابق مجاهدین خلق) فرد باسواد و کتاب‌خونده‌ای بود و قطعا خیلی باهوش‌تر از رضا پهلوی بود.
رضا پهلوی یه نادون و کودنه، بنظرم مشکل ضریب هوشی داره و اُسکل بازی درمیاره.
تنها کسی که لایق این صحبت‌هاس رضا پهلویه، تازه در اوج قدرت خودش، چهره‌ی خیلی ترحم برانگیزی هم داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/139262" target="_blank">📅 00:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139261">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس: جمعه گذشته، جلسات مهمی در آمریکا درباره قطع برق در کل شهر تهران برگزار شد، اما تا کنون ، هیچ تصمیمی اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/139261" target="_blank">📅 00:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139260">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c122b721dd.mp4?token=JMTrahZP5k-gCvCNMLno8EzB0YMxPAL6rMbEfdv9Uik9f-I0D_FJH8GYbhOii-wtkGOPApLOgqZ632PTVuYSgIldXcJRZ46ZuNQaS-RrHYbI-hWvNAsu6OgvG7gybhlDYbl5pa2mEVCx-UJcwVaQwxsH7VZVllShuNxV1-8eqye2g9fMATtHYAzLoHcAKNpoNGL2PhwEYIbunZxLoittSa1woeBQiO9ROFgpZD3o2tqxAmn3cB322y5lkq7aMwNu7fbxHZpZdMW5PwlHkS5aGH4BitSQx5uhdI1fqyvJ1Xm-Ox99XykeHfs9tVwlqYg6nAU3v2PFEj651gcqblCii4pXz_1VYPLCoa5V95AaNRnpoobAyXA_kqt4IUGEeYC_A-H2DH-TM5UeQmxANX9S772vPypMEf2drTihMpN1RkbeEZQkBKykoEfqdoif60nqMHBZJ1vTNPXW0Rvy2nH-1L-4S3F2hQXvkFulYWI2qKD4IbRdgqkkixkCvKVCGZCW4ZmNNGVRalX_7ouPEuhyar0U6IU0NR5N4FbXWDvjf6DyXlcHKVydDcxR23d0weuQbMXvhXKBzxVZuAFF3V1l_kZRKHh6o2IhoZBsvAlbQhdzmcQjntHkE7WfaV8fw-T4fxAO6E7k8cDVIBcXLMC-MG4GI3JJjcEKnSODlQ-DJo4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c122b721dd.mp4?token=JMTrahZP5k-gCvCNMLno8EzB0YMxPAL6rMbEfdv9Uik9f-I0D_FJH8GYbhOii-wtkGOPApLOgqZ632PTVuYSgIldXcJRZ46ZuNQaS-RrHYbI-hWvNAsu6OgvG7gybhlDYbl5pa2mEVCx-UJcwVaQwxsH7VZVllShuNxV1-8eqye2g9fMATtHYAzLoHcAKNpoNGL2PhwEYIbunZxLoittSa1woeBQiO9ROFgpZD3o2tqxAmn3cB322y5lkq7aMwNu7fbxHZpZdMW5PwlHkS5aGH4BitSQx5uhdI1fqyvJ1Xm-Ox99XykeHfs9tVwlqYg6nAU3v2PFEj651gcqblCii4pXz_1VYPLCoa5V95AaNRnpoobAyXA_kqt4IUGEeYC_A-H2DH-TM5UeQmxANX9S772vPypMEf2drTihMpN1RkbeEZQkBKykoEfqdoif60nqMHBZJ1vTNPXW0Rvy2nH-1L-4S3F2hQXvkFulYWI2qKD4IbRdgqkkixkCvKVCGZCW4ZmNNGVRalX_7ouPEuhyar0U6IU0NR5N4FbXWDvjf6DyXlcHKVydDcxR23d0weuQbMXvhXKBzxVZuAFF3V1l_kZRKHh6o2IhoZBsvAlbQhdzmcQjntHkE7WfaV8fw-T4fxAO6E7k8cDVIBcXLMC-MG4GI3JJjcEKnSODlQ-DJo4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک از حامیان حکومت:
از دار دنیا یه کامیون داشتم که روش کار میکردم که به عشق رهبر شهید فروختمش ۱.۶ میلیارد و خرج موکب کردم. اشکالی نداره خدا روزی رسونه. قبل از شهادت خیلی بهش فحش میدادم انشالله حلال کنه. الانم پیرو اقا مجتبی هستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/139260" target="_blank">📅 00:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139259">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGWEO9s4fTTuTn49SdTwsdcxLAgx0WxhaLr7D7SR9s8kT9_sNRM957iYWDIJzriCO4r6vHotHXHZ2FLW0A_cYPjFhyJc1q_QEH8zEZt_BQqu4hABilBY15OZgByt7n6yaJlTY3WF62fb_y0EnlKg-AgIGBfSYAJ-tq0s09MsJmSJ_k3IkDRDTVEEJa6nvTuPa6y5kCFmo2w-HXxOZilQ01vsek-E7dKXkf07UrWO8891kSNjmjTmLlGimPPg9b-tUCnCKThdaw2TWMHNRKpZxxAT5WOZr2WBtgBcKxeMtgmQkOrJwQHDCaRK6RfteZDQl2tyRileCM5iN_h2Q2oxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیا رادار اف-۱۴ هنوز در برابر جنگنده‌های مدرن کارایی دارد؟
🔴
اف-۱۴ زمانی یکی از پیشرفته‌ترین جنگنده‌های جهان بود و رادار AN/AWG-9 آن در دهه ۱۹۷۰ یک شاهکار مهندسی محسوب می‌شد.
🔴
این رادار می‌توانست اهداف را از فاصله بسیار دور کشف کند، همزمان ۲۴ هدف را رهگیری و تا ۶ هدف را با موشک فونیکس درگیر کند.اما امروز شرایط تغییر کرده است.
🔴
نقاط قوت: • برد کشف بالا • توان رهگیری همزمان چند هدف • عملکرد مناسب علیه هواپیماهای بزرگ و اهداف غیرپنهانکار
🔴
محدودیت‌ها: • فناوری قدیمی و آنتن مکانیکی • مقاومت کمتر در برابر جنگ الکترونیک و جمینگ • پردازش داده بسیار ضعیف‌تر نسبت به رادارهای ارایه فازی • عملکرد محدود در برابر جنگنده‌های پنهانکار مانند F-35
🔴
رادار اف-۱۴ هنوز می‌تواند جنگنده‌های نسل چهارم مانند F-15 را در شرایط مناسب کشف کند، اما در نبردهای امروزی که جنگ الکترونیک، شبکه‌محوری و رادارهای ارایه فازی نقش اصلی را دارند، دیگر در رده رادارهای پیشرفته جهان قرار نمی‌گیرد.
🔴
برد زیاد به‌تنهایی کافی نیست؛ امروزه کیفیت پردازش، مقاومت در برابر اخلال و توان ادغام اطلاعات، تعیین‌کننده برتری یک رادار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/139259" target="_blank">📅 00:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139258">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db38e025b0.mp4?token=BQhLcf-eDb3HeAJdwHcRz4PFeGxKGQVRsQ4Y7p99TmO_AKVkuKn5jLpMXhPi6kSgi_4Og6D0McC9TnpaIri5tj_K_ct7iGRpFU_aNBJQ1iHJQZAjzqpHwh3tELLs3vLb7NcXKnAlewJcHYvJN-XNVEHwz8RSrwvDlqEV5pgoec0NhuWZN9GVogd3bCt4U6BdaMM5S5VrHSS0DJNtv9HV57CPS8fxPVcumswYhgPIYE4EL6pd2BvuQLV09ZOYMMbnX8XTBpcWxLlpOh9E7QWuF0_hi46l-oWc0hN792GohApdb86uPtHj_5jh6k1uN3o4g812SFXWVZhJW5iZE-JgzjW2aEtFqMLnXDkJfhimexLeExHS7UhQEbfKuj9QJJIqHpC40Ph5unmYAvDA0g6jMz5IdzKm-Hx4CUfCsh1ISSsspdqCuRWLrlODw3Lx60xeWjSMqv25_YdAhD8lIVg5CM-Pgh6UC617gFq2QP2o3ez8dH6e1GEN--1v7ww6rJFyrEwoMSb-MBjGUu2E1STbvISpEhDwBQmyurNqudF2n2H23tsDaLbkbyimH_d7hkA5JIO73cSvlTG8qm6sNMnLHsa2ouFJ8KM-s_mlxIo9Q79vS0CMxdNhB7Gv-DMLL05Hzd52rrDGcxpEO6rNBY6E9c-xfeDpjXK4AZPdehbhZQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db38e025b0.mp4?token=BQhLcf-eDb3HeAJdwHcRz4PFeGxKGQVRsQ4Y7p99TmO_AKVkuKn5jLpMXhPi6kSgi_4Og6D0McC9TnpaIri5tj_K_ct7iGRpFU_aNBJQ1iHJQZAjzqpHwh3tELLs3vLb7NcXKnAlewJcHYvJN-XNVEHwz8RSrwvDlqEV5pgoec0NhuWZN9GVogd3bCt4U6BdaMM5S5VrHSS0DJNtv9HV57CPS8fxPVcumswYhgPIYE4EL6pd2BvuQLV09ZOYMMbnX8XTBpcWxLlpOh9E7QWuF0_hi46l-oWc0hN792GohApdb86uPtHj_5jh6k1uN3o4g812SFXWVZhJW5iZE-JgzjW2aEtFqMLnXDkJfhimexLeExHS7UhQEbfKuj9QJJIqHpC40Ph5unmYAvDA0g6jMz5IdzKm-Hx4CUfCsh1ISSsspdqCuRWLrlODw3Lx60xeWjSMqv25_YdAhD8lIVg5CM-Pgh6UC617gFq2QP2o3ez8dH6e1GEN--1v7ww6rJFyrEwoMSb-MBjGUu2E1STbvISpEhDwBQmyurNqudF2n2H23tsDaLbkbyimH_d7hkA5JIO73cSvlTG8qm6sNMnLHsa2ouFJ8KM-s_mlxIo9Q79vS0CMxdNhB7Gv-DMLL05Hzd52rrDGcxpEO6rNBY6E9c-xfeDpjXK4AZPdehbhZQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤴
رضا شاه روحت شاد
🔴
یه ایران مدیون این بزرگ مرد هستش.
🤔
تنها کسی که به خوبی میدونست ملاها چه مفت خورهایی هستن که هم زندگی مردم و هم دین رو به گند میکشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/139258" target="_blank">📅 00:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139257">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👑</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/139257" target="_blank">📅 00:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139256">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAzgFaaxNqfTm0W0tAMJC1tjlL0e_zCO8u6eKG2j0t5AoJ_gFoB8L_xeOHxEGipBc8uWK96I4HaAyTecvyv568N_4gItF9JQoBR3wYY90qxKxVT7EUjAmkwO-AOo50skC52KJa3pjYPZ17emc4ElT7HUkDXWknkiFEyfpF6p3ezygQUHApCTYO1zyD8eQrp1o43Mvkjx_fjcXp8Uu8BonFvNqfYKWWmPO_zVJlVzoquqHXLxMfdk2tMa5ioM_Ju1YbqphiRQhge-h0P8PZ1Pbob8mkRmd32GF21tZlO7FneG4sTiO016uJD34XrmUGlSVT9L2y9JSajugqTAXHOKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق اعلام برخی منابع پاکستانی، فیلد مارشال عاصم منیر قصد دارد به تهران سفر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/139256" target="_blank">📅 00:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139255">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏
✅
‏فوری/گزارشات از پرواز تعداد زیادی سوخت رسان به سمت غرب آسیا  @TitrDaily</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/139255" target="_blank">📅 00:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139254">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
مرندی: پاسخ ما به هر حمله‌ای بلافاصله هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/139254" target="_blank">📅 00:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139253">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">یادتونه تو مدرسه همیشه یه بچه بود که هرچقدر میزدیمش باز بلند میشد گنده گوزی میکرد؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/139253" target="_blank">📅 00:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139252">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d1c0174.mp4?token=nbu9lBkMOSMEZxpzt0FBcielwOECaEz24pg9BXa18L7DQ1qhxep2yojU8GhOpFLI2Gmm0ijU47lXnMaqbFesxmeo2xAL1LScKwFYVl-sBK9hP4ZYWx7c_crQGMNiqDqXV5LQ6Th7jnk-C7nrw3wdgshC9D76FGL9T9pkJdnB0kbUB33Ogbew3S7jotwGqHDw0OuEAxmDnbs5gzTOqR3Dq5XYhF3HVchsYJlyJ98dYb2iaF09x67A__V1TSprrB3RL6gbpTnXTdMAYoK0zj7eLBsvyCS9jAnkNZ0lpvZ82z981riXDPwImsjAtgTGSKl81hvPwUAbb91F_8XOAVINrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d1c0174.mp4?token=nbu9lBkMOSMEZxpzt0FBcielwOECaEz24pg9BXa18L7DQ1qhxep2yojU8GhOpFLI2Gmm0ijU47lXnMaqbFesxmeo2xAL1LScKwFYVl-sBK9hP4ZYWx7c_crQGMNiqDqXV5LQ6Th7jnk-C7nrw3wdgshC9D76FGL9T9pkJdnB0kbUB33Ogbew3S7jotwGqHDw0OuEAxmDnbs5gzTOqR3Dq5XYhF3HVchsYJlyJ98dYb2iaF09x67A__V1TSprrB3RL6gbpTnXTdMAYoK0zj7eLBsvyCS9jAnkNZ0lpvZ82z981riXDPwImsjAtgTGSKl81hvPwUAbb91F_8XOAVINrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی ایتا و روبیکا رو باز میکنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/139252" target="_blank">📅 00:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139251">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
المیادین:
اطلاعاتی وجود داره که تایید میکنه گروه های کُرد دارن توی خاک عراق خودشونو آماده میکنن تا از غرب کشور به ایران حمله کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/139251" target="_blank">📅 00:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
خبرها حاکی از اینه که آمریکا، برنامه گسترده برای هدف قرار دادن نیروگاه‌های برق داره!
ناترازی برق۲۵ هزار مگاواتی، سدهای کم‌آب، نیروگاه‌های فرسوده، کمبود سوخت و تحریم، کشور رو وارد بحران مزمن کرده.
تو گرمای تابستون، حتی فشار محدود به شبکه برق، میتونه رادارها، پدافند، خنک‌سازی و ژنراتورهای پشتیبان رو از کار بندازه.
سیستم های موشکی و خنک کننده ها که وابسته به این شبکه ان، از کار میفتن.
و بعد از اون، فشار روانی شدید به مردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/139250" target="_blank">📅 00:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139249">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/139249" target="_blank">📅 00:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139248">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
عراقچی طی 1ساعت گذشته به تمام سران منطقه زنگ زده و هشدار داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/139248" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139247">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifZ4f4APhnqH2tL7B0YS35j0MyoGAUww4ph9zx3gPbn5pNfxThrwF5lBCZu3vmifjh9Q8gG9dXtt6oPIEgQeJ8uJEtZtS6bk-srvFpOHzna8bBdMNWASmtW8Eu4mQpolwW26pmhPFfiqEniUUTLnduB1SjY2ft0Pe3pZ_BsJYiwVzjQIu9wsJl6w4_2mlc3N_JNTfm04Wuhx3YPLGOBSHHnYTTn4N35jl_TR69YQWpAuKwg549sIMj4Y9xuWykvZlVNRGM7t0QGOHkUOSl_CFlwAUfhMb6nmQLGFbh65-p3XqmVmCRf3RKX2E6jPkzs9HYL0e-G1nUXffEsGZscDIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت ترامپ مدیا: میتونید اشتراک 100هزار دلاری بخرید تا توئیت‌های رئیس جمهور رو دقایقی زودتر از مردم جهان مشاهده کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/139247" target="_blank">📅 00:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139246">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIGA5PkkRBNYXxHm3h737ZKt1nzmvQnVnB7iAKBBM4XjDAX2Vb9dkMgYye9rTKGugIYEHSThnewJ1RBSE5Ngj1rayX9mgl9kP9fTw1QzvyD4zD89QAxndUnLXa810ovIFND_c7P8iv_yoymhLL0z-GYIJpPMXGnlM4F2KjZyloEiPKVPJyuaWkLIPbD9ii5kTWSrtcqd1MHnVV3hSZ_KSijPdNWtsS-S52-r6FeKcw53qERnW56O8qu4xdmhd1lwjdI8SffhtPpGRV241MMCli5ZEEY9FZ1huxCak9145cUvuEmBJ6mJLWHd7Gviz9FvuEpieRO9yxh0_hvCI2wcFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
قیمت‌ها شکسته شد!
🔹
🎁
قبل از خرید، ۵ گیگ
تست رایگان
دریافت کنید
🔔
دسترسی همزمان به کشورهای :
🇮🇷
🇫🇷
🇳🇱
🇬🇧
🇫🇮
🇨🇦
🇺🇸
🇹🇷
🇮🇹
🇧🇬
❤️
برای دریافت سرویس تست رایگان کلیک کنید
👇🏻
👇🏻
▶️
https://t.me/V2RayMizbanRoBot
▶️
https://t.me/V2RayMizbanRoBot</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/139246" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139245">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
هم اکنون تحرکات شدید نیروی هوایی ایالات متحده در سراسر منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/139245" target="_blank">📅 00:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139244">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری/کان نیوز: نیروی هوایی اسرائیل در آماده باش صد در صدی جهت حمله به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/139244" target="_blank">📅 00:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139243">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
زمین‌لرزه‌ای استان کرکوک در شمال عراق را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/139243" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139242">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0d50aa445.mp4?token=RN7HKk8oookmFYKWR48UfZWK7WHRzhUtBUa5_wj2--5zwAfUDVaJqzliq3M9doOZrHuj34iMLtmN8A2u03ukVxs2P98unSynzkDhnb8OQwLjsRwyViUvegxs6AzSyaJieW853pVB9hJUNyBThStz1GrCG8RfZCHnmwOvfGIy1CHzX2YLLpY0sphUX_GOLca2ZxmU47JmaebDE2vxr0PxXvbNKeDQy1iEmZp0GpNKq2Dxxed4fuaXqhcR4I_E8IBMZCoO-wzf0NGvp5fYq5Pyt0DtWclNpo1Mce8VPkeUGxh_V04hlzofyWRmXW7toGfO1f-1eSXTLUC8p4tEtIaczg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0d50aa445.mp4?token=RN7HKk8oookmFYKWR48UfZWK7WHRzhUtBUa5_wj2--5zwAfUDVaJqzliq3M9doOZrHuj34iMLtmN8A2u03ukVxs2P98unSynzkDhnb8OQwLjsRwyViUvegxs6AzSyaJieW853pVB9hJUNyBThStz1GrCG8RfZCHnmwOvfGIy1CHzX2YLLpY0sphUX_GOLca2ZxmU47JmaebDE2vxr0PxXvbNKeDQy1iEmZp0GpNKq2Dxxed4fuaXqhcR4I_E8IBMZCoO-wzf0NGvp5fYq5Pyt0DtWclNpo1Mce8VPkeUGxh_V04hlzofyWRmXW7toGfO1f-1eSXTLUC8p4tEtIaczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کمیته ملی ضدتروریسم روسیه: یک زن با حمل وسیله انفجاری دست‌ساز قصد ورود به رستورانی در مرکز مسکو را داشت که پیش از انفجار متوقف شد؛ در این حادثه ۳ نفر از جمله عامل حمله، یک نگهبان و یک مشتری کشته و ۲۱ نفر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/139242" target="_blank">📅 23:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139241">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
الجزیره به نقل از منابعی در وزارت امور خارجه ترکیه: هاکان فیدان در تماس با عراقچی بر تلاش برای پایان دادن به درگیری‌ها و تثبیت صلحی پایدار تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/139241" target="_blank">📅 23:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139240">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
گزارش ها از تماس تلفنی اضطراری عراقچی با فرمانده ارتش پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/139240" target="_blank">📅 23:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139239">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr4O6ikwzUXWuNSaQw8Zq_OCsJq4-SEIvRcuYI_YwQ80eHZZCsLYjJhH0ifwBm64WJjHccSmDsuw9CA1CsvR9ePQqwi2TTL5xpAGWPbvL6ekgLIWEdEd7LjRosfFsuRCMW0tk3FQlWqdxwCoeYp6l1jZaKGvRyXL9YF8ejJ_rh6stfq1YeQXueGSrExzjecmGI85wZTM2K6hiXZBFKmvCzHQ2mZ5EglRHlZx32_Tpi7u9Jl1ZXOfGFN5ggRoda7Zu3b8Ih9mBQkp1a0LfS80dfmUOeyTtOmTdyv-oxDn4B-v3Nyb6pvdu5t0E5ExO-qnza_HbFF6YbAr1crE9abD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علاوه بر این، هواپیمای آمریکایی E-3B AWACS که وظیفه شناسایی و کنترل هوایی را بر عهده دارد، دقایقی پیش پایگاه هوایی شاهزاده سلطان را ترک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/139239" target="_blank">📅 23:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139238">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhqXm2eTbkoUWYLxvqCFzWSKS9hRIpY8cIR1ZXDiGMprzOUYn6i4h8rVA6Ot5ch1KeWDxDTCXy0jIq_SMg0mBx-BMH2I5DilWeT2MxfXSkTbXIUS7si69My1yT1bQWZDRYN4KQdjmNRJdLjhG92G8sPzjRLZMonIKwnAJDM3rBubmuZzCzuijQcmRJRVEjwnW0qgsgHa3XjuMxyPwe5OOqXhZqTpzkiNTqyzcFprWvmGGLgDmVfZih12dqMvp4UyUdcoMTqiKBoHPQna1QJpQC96CAnTDwDcDGELmcz_HCXMWgsFsmF-ERMeT2u36tKWl7gujLqa52WMy3DLK7KvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو فروند هواپیمای تانکر آمریکایی، فرودگاه بن‌گوریون را ترک کردند
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/139238" target="_blank">📅 23:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139237">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a70294dfc.mov?token=Z3wdU4cT4zoVpDIvVG-rQKXoXkBM2AYhEIdzmOu4MxAUORvIkSO_xYzD7Bbx8crp05Ti6r-U_-sNWaexgh97Ncp9fya_qhebAdk1Sfg8rv6SE1UdW9aDZa9S0HgzDAvfeN8cOtWzGN0VnYMnwEFKrfhube2D5RlJLNU5csxXPNw2mx_yKGfKJf6BFFLLCtadIdgt_VimKprNJfZ6ZN_r6vobltC13hnS46FdnN4A0SolEnDLqzsfVX3vXoEhyhXTSaOWaeW9vwgTWoLwiuWYhG9fkFQAIDHAe57Dkgf4R4GpzJy6AGQ9l-4ZdZM6MK8zs9C6HO1W45ZElhJuH3Eh_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a70294dfc.mov?token=Z3wdU4cT4zoVpDIvVG-rQKXoXkBM2AYhEIdzmOu4MxAUORvIkSO_xYzD7Bbx8crp05Ti6r-U_-sNWaexgh97Ncp9fya_qhebAdk1Sfg8rv6SE1UdW9aDZa9S0HgzDAvfeN8cOtWzGN0VnYMnwEFKrfhube2D5RlJLNU5csxXPNw2mx_yKGfKJf6BFFLLCtadIdgt_VimKprNJfZ6ZN_r6vobltC13hnS46FdnN4A0SolEnDLqzsfVX3vXoEhyhXTSaOWaeW9vwgTWoLwiuWYhG9fkFQAIDHAe57Dkgf4R4GpzJy6AGQ9l-4ZdZM6MK8zs9C6HO1W45ZElhJuH3Eh_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظاتی پیش گزارش شده است یک بمب در محل جشن تولد ژنرال الکساندر چایکو،فرمانده نیروی هوافضای ارتش روسیه منفجر شده است و چندین فرمانده نظامی روس کشته یا زخمی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/139237" target="_blank">📅 23:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139236">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
گزارش ها از تماس تلفنی اضطراری عراقچی با فرمانده ارتش پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/139236" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139235">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
العربیه : دولت سوریه به عراق هشدار دادیم که اگه هر حمله‌ای از خاک این کشور انجام بشه، پاسخ متقابل می‌دیم
🔴
همچنین بغداد رو از تحرکات مشکوک شبه‌نظامیان نزدیک مرز باخبر کردیم
🔴
این هشدار رو مستقیماً به مقام‌های عراقی منتقل کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/139235" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139234">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
شنیدن صدای هواپیماهای بدون سرنشین در آسمان سلیمانیه در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/139234" target="_blank">📅 23:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139233">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
اسرائیل هیوم: اسرائیل در صورت حمله احتمالی آمریکا به ایران، مشارکت نخواهد کرد، مگر اینکه خودش مورد حمله قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/alonews/139233" target="_blank">📅 23:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139232">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBfaHuc5T725TnVh9NXbHBsLUpYFfN81h3-ERveA6eL1zPmZFItYcGqt9Rl-RV0pPZq9835OgeII-mwoM6X5AplVoHKUv61m-YFKoL8ofkPSmcfcbpJ6PhOkaiH-pRt_HCPydbknWMx0PUXNJ0f_unt6jjQC7rPsZhHuXkkpZiXMX-KYdSSEKTG4ebS8oJAReeyzvY4L_bfIuy2AhQ6fOJqXuAH0mMaaQxVj57kAXMmIRspLNAHFwoh74j88oMQ6pDkvAbuncLAexycjku-wxr_TH_d26B8M8a8y2NZ4Pt2qKpe9N5MCkFCYChE1W_Zd6JhctcuH7tyl6BVHI2M9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در منطقه کونین، شمال شهر بنت جبیل، لبنان، رخ داد. به احتمال زیاد، این انفجار ناشی از عملیات تخریب گسترده توسط اسرائیل  بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/alonews/139232" target="_blank">📅 23:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139231">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/112c8c980c.mp4?token=omfuR8Zvyp-rJYw5xOOlu8Yvw0-fJazYTGoZ8ACamw-hH9LWUieKB-TDPycMvAFzbnjuV8nibw3iceNFrlUqZ3G0IGqwbdMADhDhJqs1d7Y73w17l-O5g01S_ngt9zogqJMFqS7J933nPBvqIcfL3ZIRRFvMuMmGBc-ydXlHKio7_LqlBDly0SS1CfpzqoMnItAXeskF1RbqOTRVS0IzleDDyie8VxCuNgny6Pa-cXm3m2cletanjXm2sFswvxQ46smSlQShZltzUaWZiO580HnNlc6P6Y2QrP1jFQiCiBBjEaY-U28X0fUJq5kMjZfG8lZK7yGYMrWOkgAc-N1QAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/112c8c980c.mp4?token=omfuR8Zvyp-rJYw5xOOlu8Yvw0-fJazYTGoZ8ACamw-hH9LWUieKB-TDPycMvAFzbnjuV8nibw3iceNFrlUqZ3G0IGqwbdMADhDhJqs1d7Y73w17l-O5g01S_ngt9zogqJMFqS7J933nPBvqIcfL3ZIRRFvMuMmGBc-ydXlHKio7_LqlBDly0SS1CfpzqoMnItAXeskF1RbqOTRVS0IzleDDyie8VxCuNgny6Pa-cXm3m2cletanjXm2sFswvxQ46smSlQShZltzUaWZiO580HnNlc6P6Y2QrP1jFQiCiBBjEaY-U28X0fUJq5kMjZfG8lZK7yGYMrWOkgAc-N1QAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) با تیربار به سمت منطقه حداثا در جنوب لبنان تیراندازی کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/139231" target="_blank">📅 23:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139230">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjpdbzKivaeOA59ACxDPPVOy_qZLCG8KmgAFkSR9iE7pWxOGyOXNnEtWkp3ryZvueyOBEtHbXGXcZu9X7JMRAQ4v2XlpJibrGKaohFBUPVYQB1bODA_bwqQe880WS579LTagR4jvYocp0hkyhk6x6K9a5jzTKEJJH-bBJgI19gAWZ0x6Ic6Sun_FdUddOf5oOEzNebVg0edDiRdWa_OAJD3BiFkL2UZmUAeUTj-kGwY2KLnXVQofmdLsrYMt1jj5SxRUMu-ZoKRZ3oxo9g0NgwPRHMxg_WOCbmf7Jp9g5qS3IqKO3FCTG_VsPgRCFrjBJl1W47fzeTEQ5X5qCObHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: با افزایش تنش میان تهران و واشنگتن، تلاش‌های میانجیگری منطقه‌ای برای جلوگیری از تشدید درگیری و تسهیل گفت‌وگوها همچنان ادامه دارد و تغییری در وضعیت نظامی آمریکا مشاهده نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/139230" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139229">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
هم اکنون حملات ناگهانی و شدید اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/139229" target="_blank">📅 23:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139228">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNu2O7OUefsZvt0bQnErZzB8-HK9IkooiLcB00O4LdjxCOBZ1uVHPvZyyybGK5-yWkG5cNGJtjvrmkrfUqz3sbY8mGToPKya0F3FGfQ6Gapw5NIj8CJy1ArXNqJN6R9bDjcPJ5AJaJIZYww8fM33zzuwCl2HCaPAV9fxCIYlOM0lfx2Jdfgm8fDKt0watzkW1EXZcLtFU_vDuCKqoE7NpJYmRFJPzicTk_bMn3ATgJ1H5Ifs7pQzIYHw31IxlXRkQ-pwNjT3Z5QQ1jdOzSgwZv_o3qoVZEltKqHnApu7HaV3fKmw9GE7BvI-EY03JpyboAdpf4ZDbDVkhRHvj-mAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جواب خبرگزاری های داخلی به کاخ سفید: خدایا، حافظ رزمندگان اسلام باش
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/139228" target="_blank">📅 23:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139227">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4QpTK6X5CO6yKfJaJpACL9B9mbsvS6OqXmOsVtaJ-tWrMMd37q7MN3CSxGZC7IUv0NyAgoqhbJjhrid0z8LZyI8uIa4JGzmqiYEscu5G-CNtK--pok9hCzJ-unIRsnBddiHECwxHFL29caKKnDVQ89y6oNqSFqwV91XKTslumLakohBFo-y6FuC4QHdkQjUF9Dgy-M5gt8pV-JvST4bxgQQ76XJ9C5Fo-jTO4xeXGSjQZytFimQ_Ri5l7p7RXgkPBFuc14MiJw6ePjJkqivN4b6yYL6ZgD8TX9Jou45_Q9XfNTyS0bXDqBGNh8GJZlUpngm1RORNM7eRiUakdVlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موسویان: شاید میدان آرژانتین تهران به میدان اسپانیا تغییر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/139227" target="_blank">📅 23:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139226">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpAiN4YvAoIydxE515NTRiWybKZ5RyWb9z-6CWimC4iDFGYqAfh9gu973u60LdMUcewVx-XhVORQZgjAxSMQ_BdzxyHCj9-HsAa4qhitP2nCMD9a4bC5m0HI5RawMx_AtRSBKVJUm2j_KagtflhYNmq80XNJ1Gnc7DjD2GOtNkitYicvGeMv_Y-tDt2ngeSdyCEC4KAfANw6Zlbk7kjpCzuYIq3EqlQeRLXjvWNYH2pusVIPRzWnfcsnfuze8aMeLN2s4YAM4mYpzz8WqjAAu1gMXQuNKUxbaTdAWgrMYbMfxAHH6Eq4qk1hRp6VdDDtIVXs2x_bHkzi4VS49Ow_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
ما به سوی میدان جنگ پرواز میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/139226" target="_blank">📅 23:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139225">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/awA7a4hJ6Vr7Wb0QWZJopsAoD5eEz-2HDd44HyRNyY_jyf21Z-xJTQQ0jw3djMovk_EvO6cR2qqS0LbsaK0Yo7MEFxRD2wgdAhixywt-DkLOka9ZopNfgmvBgO-rCfWGsdCzWzdHREPse1gPuhXsPaX6fscDwL-pLsSQu36ACLiOtnjGplQnEqPCBa3JFSccg4fZVENgOabLhxzhGl0w7H51GgY0qbVIsvKEFZWS7E5GBVZ11Nv98jU9liM9iG8-b1GnGWD2Yjr_ncEHZ8E_tMg0Tcice0hrGOmeJTA5Qb6KOLBxwCSd8RSO2Oi0sGyX8QbTyd2rlYHQMgmKFXWZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید حساب رسمی وزارت جنگ آمریکا
:
مرا بفرست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/alonews/139225" target="_blank">📅 23:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139224">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">امشب میزنه؟
👍
👎</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/139224" target="_blank">📅 22:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139223">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWdwnqB38mXwB23LPktmEtO0U6wiZHFGvGigZHxej6D-h0I6KM3fTTfg1G4CM_92nSTocQYBmJCFe4Ee6YdS73p7HWCtkvIg43IoF8kWqJm-JdgbROsiNU0ZdnDhh4Vt7W8bLXlMzUyr09qCsuDazEM1WNKEDdAARIGQhSgHGk45fXHxHcp3MeuiBgOfM2lh4PrGXZu1UezUmV5102s3xH5dZ8b5Rp0r4jXnFuv4HaHBqX2baBzlY0E2bRUPisLWrxD5ypdgm1Z75D4g3frUPJYffSU3lDRHzeNt4p6FiYhq-nkgUsdWzPOPVBGCILdpRU7UGyFy6ROD_WSq7QNZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: آقایون بسه دیگه! کار آمریکا و اسرائیل رو یسره کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/139223" target="_blank">📅 22:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139222">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=kYSsu_LFSeaG_TyciCJs_zZehJcDFPq9-JEAm-73-ZGmMLDcRNtR01ZzwWI3oB-WsM8blCRSCZsNnfSlS0ZIvLq0Dd8gNnmwP0Kr6tPzYWWbtQNvwmXMTFUcOQVM8UhrRAc5g8PG9ZCazRCJpj-90vghxSu7CPD-mZKGm5XCuxe4ABqRopFc59-VQgKZZWcPbPLt-1fJ0ITftgdO0jqmykBg14UusyRL-dzjopLPolCG9yeqac3nkDVM8exYKcgHeXYhdGhw3WdM72SfRZfSoSgsACAbN0RlXc6Mplu-ZxAjkRXqnuz6uEFqm9BqP09YyXy9dvaybCuOCIGI3c3TXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=kYSsu_LFSeaG_TyciCJs_zZehJcDFPq9-JEAm-73-ZGmMLDcRNtR01ZzwWI3oB-WsM8blCRSCZsNnfSlS0ZIvLq0Dd8gNnmwP0Kr6tPzYWWbtQNvwmXMTFUcOQVM8UhrRAc5g8PG9ZCazRCJpj-90vghxSu7CPD-mZKGm5XCuxe4ABqRopFc59-VQgKZZWcPbPLt-1fJ0ITftgdO0jqmykBg14UusyRL-dzjopLPolCG9yeqac3nkDVM8exYKcgHeXYhdGhw3WdM72SfRZfSoSgsACAbN0RlXc6Mplu-ZxAjkRXqnuz6uEFqm9BqP09YyXy9dvaybCuOCIGI3c3TXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کانال 13 اسرائیل: ترامپ تصمیم خودشو برای حمله گرفته
میانجی‌ها که آدم‌های خیلی خوشبینی‌ان و همیشه میگن راه مذاکره بازه، حتی اونا هم میگن حمله‌ی آمریکا از هر وقت دیگه‌ای نزدیکتره.
آمریکا هم از طریق سفارت خونه‌هاش به مردمش تو خاورمیانه هشدارهایی داده که اینم یه نشونه بزرگه برای حمله مگه اینکه ایران همه رو سوپرایز کنه و برگرده به مذاکره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/139222" target="_blank">📅 22:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139221">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به جای خرید طلا از پلتفرم های آنلاین که اگر مملکت به هم بریزه نمیتونید برید طلاتون رو بگیرید، توکن XAUT (همون انس جهانی طلا) رو از صرافی های خارجی بگیرید، زیر سر خودتون هست.  ترفند امن خرید طلا با پول کوچیک  تتر که خداروشکر همتون بلدید بخرید ( ریال رو ببرید…</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/139221" target="_blank">📅 22:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139220">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
روزنامه والا اسرائیل:
در ساعات اخیر، اسرائیل تمرینات شبیه‌سازی اضطراری را با حضور نیروی هوایی اسرائیل برگزار کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/139220" target="_blank">📅 22:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139217">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jl3NfW2Gs_whiMLeFIw6qTqVxz9jk7mREV6AvUaNPXZ5RlobsiNyUPEVvx2pcDNjg1jO2mqLM1rKtOdNjCdfHTK-DDVWHfXYkIchNky7UNdZZ5HTY0rCRbpJKuRU4xxoIQRGZIh1thrJebT6kF7u1QH5u0z1ujGV-LZyWS-jFDpvwsV6fntKPmw4avHmnMxuCwji3AAbGGDlgKtY7fK7VPVOwnt3lqUiZd_izKa5ODq_Y7dftFUIlWE79H34oPQtl604Or4DZ2_PgYzQdXRNzrhOEPyVGJjP4gDqRoaxmbUJvkpwSSrTuaeGBfk_ajTaLubpyGn62TU8nYIsoFv3Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoLnG9H1SAXA-sMLMa-0H8gBKkqr-O0-bw39_G6MdkMtDy2whW5DlSF3njrdsYLpj8Pjko5bLhE6MPiF2qHbLZyxvyyHcByj9u66BBSmhgSyTRbEGJAWbDz8hszb14gviugefH7OohZ0jCxkiFWF5kSly7ndK03HKp0fCoZQ-bNOmJpbpg82glGLyQPvAxprSliqgtT1G7oi37PfViKEaWdnbiagsnFzn17sJjyWKHv0uo1m4_-8UvVpoSv8ylSxbURhswZI2PUUnWeENt8Dt5ScmdG5cgPDtprTbmHhtZbPxmaZaSf7TdYBJ76E1L2JJS-6G-GkkfzJ6Ma3ChqJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mm07OFWTJDJYjfs-rFz--S6SVCnr8--_usRY73sTYlR4VXBtdJIQ_PBAIDAMxRpH_fu97Hdc1IbAEc514Cb5l3lSAPx6EoNpvPLh1KOmCEyHE5_qUGD6-UqVR9RWSumAkKyMM4emxV9G8Gs3VxaPaZYGIPkwOiaJ22ici1ha-OJTnz3TjD-y61bQbpfz3bvudd10eMEIyYeZSB6qRsU0h_028mu0Id0ALl6YTxamy-pitmmslrmJT_0SsmrhIa7IYx28WWU_SEQlTnECacGVqyW_J6-YsvWBWA1T7lQhvF7062tZe1Ba8i-jqpLUAEn-AV_xSJm1ymq8fw2RH1ZQrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وزارت خارجه :
- برای دفاع از حقوق، منافع و امنیت ملی ایران، از همه ابزارهایی که در اختیار داریم استفاده می‌کنیم
- اقدامات آمریکا و اسرائیل رو تجاوز می‌دونیم و در برابرش کوتاه نمی‌آییم
- در عین حال، حفظ روابط دوستانه با همسایه‌ها و دفاع از استقلال و حاکمیت کشور رو ادامه می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/139217" target="_blank">📅 22:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139216">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
کامالا هریس درباره جنگ علیه ایران:
این جنگ، جنگی انتخابی است که ترامپ همراه با اسرائیل وارد آن شده است، بدون آنکه مسئله روشنی در حوزهٔ امنیت ملی برای ما مطرح باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/139216" target="_blank">📅 22:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139215">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPsVg5VhBkxCJx8SEiljabBRQhc-VhflSPn4pQE1OwRrKm8NGr8sblYkTxgnKLzj2jHT7wt4BJxaVEabj1xLQoYT3FWFW9pJRlyjBlrmhLpdMd9cy2mXliB3x88b83cJtS6Eeko_1SqlY7bXjB464Zi7jSprlDA3ZJAmV8-LGTzYD_hAwDs_TJrq25bIhea_cH7GNPuUeNIWOSu0HKZ47N-f08JiKp5slWKgMRZWpTT1hvOUgA4Mx_SEOPlGXFzrAMBfwqGp-zScFmjCTilofr5QT2kx7TRdBwU93xwLdKP19bx2HxzuzbNDc7N8UCGDWQV9lhxcNz3XgJupO5bb8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خضریان، نماینده نزدیک به جلیلی: باید بودجه فاضلاب شهرها رو قطع کنیم‌ تا هزینه جنگ دربیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/139215" target="_blank">📅 22:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139214">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/139214" target="_blank">📅 22:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139213">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R25gQCRABMI1WvWiV38L1TdL77OWZ2z5EFFhs6kWCmHpQioq5LpphH6lDhVCyj-SsmDfMyHl4L4CSRq_k5k6VM1NSD_89oT7JPtKAd6n-3dvS8t1SV428dAKkiMjbXpUSoaBiwo_wxMpK-WtlTg6IyVN5158U3PLe5kuOPBB2kylB5C-HzL2eSY60lI9L2DI6dzh03JubxC2pYzPiTq7QgLroWaXbV38j0SlCe6qU2dC0dHifP9PKp0DfS01tUjtRy8f2Qif1RKFsGSW6Tl2UXlxAd93vEZjsrhteFo6fpRg3w7I5h4OiDA_8L27zuNROfbhR91M1pG11pB667GTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کوچک‌زاده، نماینده:
با لایحۀ جدید مجلس، مجازات نتانیاهو و ترامپ حبس و جزای نقدی می‌شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/139213" target="_blank">📅 22:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139212">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNEhRLwKa5JoORi7L4GaQXl_EZXHyH9oeSO2jhIQk8pmAj-GEzLcEdX2pr3Ko2wBca9BvctmpcJA4EMwElOV51p3cnlnckU6z8YJvofylCzq5T2Fejotl9LtUGXo5AWLsg2BAjRruZGG0n2y6fDhHTkb6vHSqqPw3vpjWSJnniBzLXwFIXKZnjWeiVARsJhnKWTMOMbGFcVrZRC9d2dJk928cPtWqQrQ0zTGlUeVbfDoAQd9L0-R4NS4zT0hS_qJcl8c8OqQmVpOhIyG6HTR2GdmETSAh5pENIIQRy-UhRXpxayMxecGDkK3KN2WyNTfQyVG56tTgMmu-3E_QrMFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: هیچ هزینه‌ای بالاتر از زدن آقا برای ما نبود و باید تا تهش بریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/139212" target="_blank">📅 22:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139211">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAxmDveAN8gzw906diHS-60plNz-aC2vXGnTqPA_YE3f_nVX-xe_MlV4OM3j5LR1gBIzEgCgIbRlNgMiXCVqbsYWh32t6k943-5svongkBI51CpGDnEm5pk7vFNnxYFKlth6LeLmnRvoXF3gHPV0zRC1tjZQ8s5DKbM1tWAK6w6_lX_us4-d714H1EMRzxWf3mTyyAeHwLwP_kQ-moSq3nlJHrCi8ohx6PZ7A6D6rZ2p15hkxa6IgjowXOvLHmVvT6J7J5JZDxXZ45Cq0o32DUmbux1Z7FducTlmSgh7y7Z-itba2y-DTnK9K9SGEuXIje7nCxLQoUCogl0AI2aBjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اهداف احتمالی حملات آمریکا و اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/139211" target="_blank">📅 22:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139209">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRMNIh3uz96fthbr4nvKhA6nELY0inc6yiCpXY0eZ6bBsQuDROSiN9AF16S8xMKBaIyrnxV3GUgf63cAaGOVDYLNXKlj5WsqpMVSLnH8mRM5skaRckxqtOtfhNPa0HipabHAgfAUPrjlYnKa3zyuqpu7UjUAioR24WQvbv7iAdnyg2oC6vUAGDyIuB7Jv0XetUsI7dwNZ5gW68Zt-vTMAJ3rsTzE24k9G89lRvUGo6DqwX5AyN0deWFCTGBswpfOHaWlTTb7AhFKC5riF2xrMCWSPkDZof-Ve9D9kYW5zAFpNTqKzVc9Rh2aWiFVmsMiM4TJ5QAduYagcM8AhtMFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ: ترامپ برعکس عمر میکنه! (یعنی هر روز جوان تر میشه بجای اینکه پیر بشه!)
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/139209" target="_blank">📅 22:03 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
