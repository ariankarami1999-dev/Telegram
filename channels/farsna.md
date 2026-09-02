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
<img src="https://cdn4.telesco.pe/file/U3aLflqBG6NJyk7q4Vg-PRRqaGwhBzWGwAynLeJHYFY9Kw3iEffaHLjBQbid81CsF7SFK8N2_EREOAPaTRBrwk6yuae6gJ8WmTiQC2HRZz4eCLNAA1KCf0KZDxe3rJ-_RTXQO57AHJ7lf-JPGHzR5desY-6g-h9fu5gWXYq4p029jBNT9oJbsSzsmM0IWHIBHJ_c7fax5WQm-azkknRZWY_ZNCihxadIdLpHqIDahZ76gPnpNylNMPAUhpSf2x81ed4rYkYOgKLd9rlVBj76ZMthsjrCW2vJ9h6DzrU-2QpssMmP6Pyiwf8gYzkJJlGNusvcGneDfP-MqRp4mkLeWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 10:41:44</div>
<hr>

<div class="tg-post" id="msg-459678">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شهادت ۴ نفر از رزمندگان هوافضا در کرمانشاه
🔹
روابط عمومی سپاه استان کرمانشاه در اطلاعیه‌ای از شهادت ۴ نفر از رزمندگان جان‌برکف هوافضای سپاه استان کرمانشاه در حمله رژیم سفاک و تروریستی آمریکا خبر داد.
🔹
اسامی شهدا: شهید رضا محمدی، شهید شهرام جعفری، شهید علیرضا شکیبا و شهید جعفر کهریزی.
@Farsna</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/farsna/459678" target="_blank">📅 10:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4757fca8b.mp4?token=VrAgMukXSjByak1_Rmr1cdmswV_dqnoFeIF1VLVu5theP695fP4y6sbwZ--8xsHPt7H26X5xb5OizDEZBRxFhSBztZJWd81UYFMI0ChEHSNKrJ3A4k1s-lFi7lYT_fOYlOs3gUy01o7NnEyLqwoO3D12o8UwvnXOVasyyQj-iIIe9c2FrJ0FWVrQMoLNdF67PVkOgJTOL-mtnk7ffzcewqBvLSrbY5WXkg50vqU1Bo1PvUhcYqDZg82A2RCkyTIk24DSr7SMtAO_yvhQaEak3PSHdtv0qMLh_CeElKyQEqSo8NFdL8ieYW9ZMnB7TUw3FxVTDzk8uKSt5Sw0ETcaFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4757fca8b.mp4?token=VrAgMukXSjByak1_Rmr1cdmswV_dqnoFeIF1VLVu5theP695fP4y6sbwZ--8xsHPt7H26X5xb5OizDEZBRxFhSBztZJWd81UYFMI0ChEHSNKrJ3A4k1s-lFi7lYT_fOYlOs3gUy01o7NnEyLqwoO3D12o8UwvnXOVasyyQj-iIIe9c2FrJ0FWVrQMoLNdF67PVkOgJTOL-mtnk7ffzcewqBvLSrbY5WXkg50vqU1Bo1PvUhcYqDZg82A2RCkyTIk24DSr7SMtAO_yvhQaEak3PSHdtv0qMLh_CeElKyQEqSo8NFdL8ieYW9ZMnB7TUw3FxVTDzk8uKSt5Sw0ETcaFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویری از اصابت مستقیم موشک آمریکایی به محل عروسی در کوهستک سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/459677" target="_blank">📅 10:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459676">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4Etg0PKUDcA8fTs9w1p5hIOECY6iSkzxmDwqkuAbFz-oUGkyjR8K2G1PhBlvw-7qqLD-pd_JAUMSVzwM3oVPmESMCDQZUnMZJP7n2XvadAj_k-vMAfvZHSDi82ceP2FZHhNV80oZCHWvDXRZquSDMG7i2ZorWcrcC6QWhFAp3jgNO-_bvudpw9thNXiENEPfB2rxxKYYqAM2zF_5OaM3_djl0zzHn4MgeLf_Ew0v8n_y6SVTrYf2_TpOGnJDmk0ZlrIA0jlhK-FKr-Ipy_MYeBqS3QLuhM1Wwsnh70nvzdLXhHete676l48zNQJHj9sujhw0oUcooC1J7no0ULChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔶
رکوردشکنی مجتمع فولاد بردسیر؛ تولید فولادسازی از ظرفیت اسمی عبور کرد
مجتمع فولاد بردسیر در ادامه روند رکوردشکنی‌های تولیدی، موفق شد بالاترین میزان تولید یک‌ساله خود را در دو بخش
فولادسازی و احیای مستقیم
به ثبت برساند.
🔹
بر اساس آمار تولید، کارخانه فولادسازی بردسیر در فاصله اول شهریور ۱۴۰۴ تا ۳۱ مرداد ۱۴۰۵، با تولید
۸۸۵ هزار و ۲۱۲ تن فولاد
، رکورد جدید تولید یک‌ساله خود را ثبت کرد؛ رکوردی که با
عبور از ظرفیت اسمی کارخانه
محقق شده است.
🔹
در بخش احیای مستقیم نیز تولید
۹۱ هزار و ۶۷ تن در مردادماه ۱۴۰۵
، رکورد جدید تولید ماهانه این کارخانه را رقم زد. مجموع تولید احیای مستقیم بردسیر در این دوره یک‌ساله نیز به
۸۷۶ هزار و ۵۳۷ تن
رسید که بالاترین میزان تولید ثبت‌شده در یک دوره یک‌ساله است.
🔹
ثبت هم‌زمان این رکوردها در دو بخش فولادسازی و احیای مستقیم، نشان‌دهنده
بهره‌گیری حداکثری از ظرفیت‌های تولیدی، افزایش بهره‌وری و تداوم روند رشد تولید
در مجتمع فولاد بردسیر است.
🔸
این دستاورد با اتکا به ظرفیت‌های موجود، استفاده حداکثری از تجهیزات و تلاش و تخصص کارکنان مجتمع فولاد بردسیر به دست آمده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/farsna/459676" target="_blank">📅 10:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459675">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofkiLCmm4OV_CFiVL0MMoWvXdpQMlhnN__ZLOlmAiJagISEd_WhxGz7ryeXoTaga1Ut-XipScuqF-wZwvSrbupw26nszXLaeKE1o6NVFoxIORQLMaRdbzyYuw1BaGZU8z1xoDUviHYYmQYuDBcAtV23rIx_pRpIcTKhXbvfbtw3tZ-xVI5fddQUKSW9N9IkHwsK7JNIPyqzTlVl1waT66urlNLkqNDHiFKxyr7D0I583gwXdbNLkj-vp8xbYgla8FQwv7Ukvbla9ZALAayyLnKW-Qip39lLVhaRQNTjhUJTGAmGE9Wb_YXr3CcKm6WFuoYdbUWQcEaaVUD9rG-WGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
رونمایی از کارت اعتباری گردشگری ریالی و ارزی بانک رفاه کارگران با حضور وزرای رفاه و‌ میراث فرهنگی
🔹
در راستای رونق صنعت گردشگری و با هدف فراهم‌ کردن امکان دریافت و استفاده سریع از کارت‌های اعتباری گردشگری ریالی و ارزی، بدون نیاز به مراجعه حضوری، سامانه صدور آنی این کارت‌ها، توسط بانک رفاه کارگران رونمایی شد.
🔹
مراسم رونمایی از این سامانه به عنوان نخستین سامانه رسمی صدور کارت‌های مذکور در کشور، با حضور دکتر میدری وزیر تعاون، کار و رفاه اجتماعی، دکتر صالحی ‌امیری وزیر میراث فرهنگی، گردشگری و صنایع دستی، دکتر للـه‌گانی مدیرعامل بانک رفاه در محل این بانک برگزار شد.
🔹
این سامانه در راستای تسهیل پرداخت‌های بین‌المللی و پاسخ به نیاز کاربران برای خریدهای اینترنتی ارزی و ریالی، پرداخت هزینه سرویس‌های آنلاین و استفاده از خدمات جهانی، توسط شرکت دانش رفاه پردیس از شرکت‌های زیرمجموعه این بانک در بستر پلتفرم Payval راه‌اندازی شده است.
🔗
متن کامل خبر
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/farsna/459675" target="_blank">📅 10:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459674">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/farsna/459674" target="_blank">📅 10:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459673">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMPvJYU8LX-if7qs2I3ApbbodLU80LP_Scaokb2qHeJFOc8Pc3mpbl4YfZH3HXtB5IiA8bkFkUKv1ZAQlehdNlExvt0wT60tFlnLWRz727Xqa1WMrwivqFFPBgk1ncLwxZeYuxavj9xNa2ucfbIoxsrdHBVUqvM5whZiVkToc2Yql2dQhXDqU-24u0Z_Kh_RcVUdOdsROEfDpE_ihokE6MsBk_UPlvasHEX2pjGB-SQIfavISguepeHqv3nQQVNPVz43WP9jZ_IRSPCR-lNs_4aoKjdPFFhRrX5nTaFQXnjdMRRVNVbfIKE3JhU9u-DrQNe-MHiOTwXvM1iTZpu4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بقایای موشکی که دیشب عروسی سیریک را به خاک‌وخون کشید  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/459673" target="_blank">📅 10:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459672">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac604a2ddb.mp4?token=GS4S-RuSFpQL5U8kN1FYDXOBUlFXIUrFptdvDFki-xh1DbA7oqieZ94r7rXj0cf764mfSMB7wUIYGtN1hVZE4tgH7NjyI7wibs5f3jGmcNeRc8TOqkic2ZSpPeWJ_XR12mFwor47mqMUg5UbNfxlCvsDTk3-m2cc_uXdR0a-9MwUHVbA96rTOOcsE8zaHyaQQtSXWu8rSEfBylIsZV6YfLh5DEF2qzoTZzfkiKeyF9xnLyFKTNaH1KjYFolKvcTFr-EtzjueESD-itNuF2CYJ2F9t0E6WC3_15op-j-EFXNN3wC3Ar-BkTD1qj1MPqGvrAjG6Cf7oDPTI1vTR3fsXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac604a2ddb.mp4?token=GS4S-RuSFpQL5U8kN1FYDXOBUlFXIUrFptdvDFki-xh1DbA7oqieZ94r7rXj0cf764mfSMB7wUIYGtN1hVZE4tgH7NjyI7wibs5f3jGmcNeRc8TOqkic2ZSpPeWJ_XR12mFwor47mqMUg5UbNfxlCvsDTk3-m2cc_uXdR0a-9MwUHVbA96rTOOcsE8zaHyaQQtSXWu8rSEfBylIsZV6YfLh5DEF2qzoTZzfkiKeyF9xnLyFKTNaH1KjYFolKvcTFr-EtzjueESD-itNuF2CYJ2F9t0E6WC3_15op-j-EFXNN3wC3Ar-BkTD1qj1MPqGvrAjG6Cf7oDPTI1vTR3fsXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عامل درگیری در اتوبان ارتش دستگیر شد
🔹
در پی انتشار تصاویری از درگیری و ضرب‌وشتم یک شهروند و تخریب عمدی خودرو در اتوبان ارتش، پلیس محل اختفای متهم را شناسایی و در عملیاتی ضربتی او را دستگیر کرد.
🔹
متهم در جریان تحقیقات اولیه ضمن پذیرش اقدامات انتسابی، انگیزۀ خود از وقوع درگیری و رفتارهای هنجارشکنانه را عصبانیت عنوان کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/459672" target="_blank">📅 10:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459671">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiwgawsUN3kiVB0BthbFUzANbJ79LURoLG82yLnA16ZQAQs62Gt03xAZ0cy5V9fpENECH9H019MVC9GsP0kmiyShT-w05G43w59lPL5h7kAk4UMC5AVnQB-Q8HSDEbcoxXwFtwmFh6YjxU7FX6hMz0B2SwIXxMdLZ3V3AxuoaEzyv_meq5ialvKx-meiNtxGsRNKVNPj4AqruUqfZT93DjfuNyLZYu7WMQFef46J5rH0tRMYR0uVikOJr1-hLafM5vfPer9egnPeugwQjV3suRYJpZIA6MZEIy47HfkLjeikORbk6goxyKA4CBJoeoyz-EbKf33GlRAPiSG-_1OFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌ جزئیاتی از حادثۀ خونین بلوار وکیل‌آباد مشهد
🔹
رئیس پلیس راهور خراسان‌رضوی: این حادثه زمانی رخ داد که یک دستگاه خودروی هیوندا در مسیر غرب به شرق بلوار وکیل‌آباد با سرعت نسبتاً بالا و غیرمطمئن در حال حرکت بود.
🔹
این خودرو با یک دستگاه خودروی چانگان که در…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/459671" target="_blank">📅 09:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459670">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbhYjTna-yZ0GPYKmHGDffGmV0jeEJk68lazKkEkcxy8zgKHOJ3aUjaknKKKp02dtPOK5fsT9AZncu9G49uz_KZlIeW9PrHO4tzjc0dcar7o3joFyoFmLYnkOqB32cLvrESjvVWVN7drJxD7HWlum6ES8xPCKuBl0mPshsrQ1U0WweDNEERs4_OcOXBFYOtE0raNfpOxjfz4gnDS4icfnj63v9UCllRxBVQxijKSyE-gSpP16vhRRv52ijUTbpbIYEfTeCtTvUS1goh7ryTnz8E8yxmjI9oN3TX9eQ5-eTSmQyBvSUUABUilre_14d9nvpx4RLtTLdzD88h75xddZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/459670" target="_blank">📅 09:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459669">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adbfffaaa9.mp4?token=OhDMfDimzUn1dyQM12Ai0PDi6Q7hK27-s9YpPpYttTXXnfHVbwaAR-f3--o2q9FlE2_eZQRPZ3-Mf2sjrX5Qn7cdyGq_8Bx6GO8fXI8xZndqdx5x2WkDNCetjN67SlCXxzS1yNAia2zyCHSz467rBEbO9MuUXIfr8HlFebW6psiUXZgGKybOQipziwbyyfnEiC4xf2eoWTImPX3d26k1P1fNe1a8LP4RB5YmIARpp3O6qdtBDGLviVAimIjA7np1NQSaReVdxjOPqDtbn_5S7D-ZwRrMMYouQlCZmo1sUvYQL-GwC7g9OJiikBIuuvznzdxCi6LPDu5kqcGLwiL6yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adbfffaaa9.mp4?token=OhDMfDimzUn1dyQM12Ai0PDi6Q7hK27-s9YpPpYttTXXnfHVbwaAR-f3--o2q9FlE2_eZQRPZ3-Mf2sjrX5Qn7cdyGq_8Bx6GO8fXI8xZndqdx5x2WkDNCetjN67SlCXxzS1yNAia2zyCHSz467rBEbO9MuUXIfr8HlFebW6psiUXZgGKybOQipziwbyyfnEiC4xf2eoWTImPX3d26k1P1fNe1a8LP4RB5YmIARpp3O6qdtBDGLviVAimIjA7np1NQSaReVdxjOPqDtbn_5S7D-ZwRrMMYouQlCZmo1sUvYQL-GwC7g9OJiikBIuuvznzdxCi6LPDu5kqcGLwiL6yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسامی شهدای حملۀ آمریکا به مراسم عروسی در سیریک
🔹
محمد ملاحی ۱۶ ساله، زرخاتون طاهری ۵۰ ساله، کلثوم ملاحی نژند‌نیا ۴۳ ساله و امیرعلی کریمی ۴ ساله در جریان این حمله وحشیانه دشمن آمریکایی آسمانی شدند.
🔹
۶۸ نفر نیز در بیمارستان‌های میناب و سیریک و درمانگاه…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/459669" target="_blank">📅 09:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459663">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLANrhxEGrZN4WOSik1-QhsIfe5x905azU0gVnhadvN3yfbZ5hxd-2_Xq-nLLtQduRB-HfpoTO54McyT2r9gOrhAQ6vIcN8gyyt90ZbZvuPv-c1TJZ0I4Hi09aUmCsS5S7knmFQZQEVGGJ1nItD9s2B9oIbLI4t6k5hNOXtT1yriDx1LFTJvYXCr7fFt3JCilfxlv4LP5TanzMHLRR9lxSga9abAD-mfP1z416z0H2NNxGsaC_pJivryADJ7bQORxaheTA5q2hmy6iybnIowuP7dxdF_NlsTNm5qZGdl3zHGgB3c4Kr39m7WmkoXLP7mi0oEMPlXqmtleObS6Ntb9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voeObhCYqgkKrjscodMrdP5ZRzeq-qEhze956eT45RQVeEZXO3VgqMHsulnC1K9ghiIefgXd-7Aa1BeDCGSXqAoAKN83gRIghvPbF5WkrVr-QpduN9MPzS5cj4kSMRBa1YOrUxkWUKf4jgnvqgepJ1fiLIhf0KvppcJQk_ZE65J4_DSlnHkHID-5jaYGcN0sQO1mI-BFkVfMSlDKcgyqevP_K7sWeHxzthe-tTErJwyrxSH7HMKM4to--lD6cbW-lwNuY7vkPJhNtw3XG1dKzl1wAEbYejv4Hjs5JA9idsOBdOB0yLjzIHn9WVCsw8jGyNDu_8WCwhMLCI-qUz0Qtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkqNTugr0gQJtrMgSvyXvMHPw1up3fpthbZVkRB5OlgT6c1uYpwK1Z7XFKzyjRrHJrv3m82LyFBGD8HB6rzq9bZA9ZFIBNMBkpD9Ra3OF7iMBh93aZYnkr7rG3z6nwi_Q4tInK1sCaewKYNeqWqqyykZN79Y19txqSJmJnMU8yOmefNdv9mDKbVgfG-WssRCLdutGAeIAg6wpZojuo7lAKdx6t-cIoIU4ZvWAEVCCyB6mJEq9P7hm81bzZ_MaZMC0uKcYm-8FLFyCyGuMt3t8XZcbrcroqedlMeiJixXXdwHWlysJ1qCN_WT2avm7flhu_7L4Ji4-eJDTAn96-p5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcWHy2520MOwCUPmIjGcbSdEDTlQKD8fyxaJ0Zd0OHu_GGk7MeJCIZzFX3NgjhVfL0jwE8I90Z30q5gA-04hguohAkR_bmD2KNeSW66dWblpmO_zB88ypCueSAx0wRP-P3uoR-sT7w2v1WygPucfUoiQO0-ov2kq3Q9R_Fcizq1hUKokaGg4gkIYOTNsn2U1mUyYO9T5A6a9mempJSZD46LVsDO27acrdmoPBrgtjL79UHf4IrqGHdbzMN9utcZMsr8ffLbZaw_9o1o6Y98H6vC_XT9EKYy3YhIlPUu6fPhfMgcM212oc-C5z88WKYGspHVG7K2xRwK44L8bQp9qDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcSYHVITXPsMXbPy0mKMIORPLKy32lVDYFJjgzKWQjnIROfnj8u2j_sJlLqrz8LbuQDn7g6heLk7cQiyeRabrsEeI38lJOc1t3iG8o6_8lYR6bIYflkSdpcaxKR5mtQT6Yf3f5sWQy_G_IO0-zUJdxm2xBjP0UKadIYDZilFpzgK-2lw0CKFWsEAwR-Hh_ywIP4b_RbhIuL4hoTcd0BCHFWVWogaELj4VYlw4Qj2-adS6KLHSRs1OUnOOEtcXMnQX3-WuIJ7ML8smLr0-qGMtTOlz93XO9RBoIAb4REgh0DoCfPLCn3VpYuY6-vH07aiDmCoyk5ryimzJwr32XJvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCFQHV8n9OovI65zI89eY6pO1dErk7mPqfz5jjfJAiI_j1Uj6Uf7x_YZ096ngjuZPbwEZ-kVCI6i-Q_dMmwnqoLJ8QHo9mvCfVjAeG5BMkUQwqCbl3FlfSMPU7yXvBoAgD2Sh8zzQLVtwzJRdR07vAY0e8xvKvG3uGd0MmU-UJr_yM7JvtT6zvAIcHM6O0kDWIPbIoGHIFt8hcMNQVLFJFYn_QMkjcjYCLmosG94aWdJFLx2XPFF1Ux44RB0BXKbrZhcRNyCbaPv4AhP4TPaLKOZ3IhLjIgwutp07JSaWS4_PgkQlGY7Kaf0ioog8EMWVl0ToF8SQdfhUJW3ZhRcJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بقایای موشکی که دیشب عروسی سیریک را به خاک‌وخون کشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/459663" target="_blank">📅 09:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459661">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmOKPS1xG_akRrku1YIwsDIG2RKPRzZpWE3uL4TwVYRl2vSv8TWT-FMjGEgOpwkkGIJ-2WlUtvFwqVhJv4k_1A9OQuRi9Wo6mRVd_w0eSyZmrI8_UT-dwg7h_4Bh5L8e8UTj8ShcvfZ4B4tOkTjJxfSs7DaG1bAAGHMu-2b4HMdpmqUJGzqrpq_A63fwPDLy0HsnghYkJK552NUP-MGTxMZ3gRTO_sT3GdDZp0mDdAEPJD9j39OyNBOcuqf5NN3zLbkBAXCVxUSKPSIURhwo30Q2SedvdysWokiZDr9pc2fXBSYhtcq93Zf47sWY9X0eVuQTRuZohuNBpmEaXpuE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85a443f91.mp4?token=PA7A6mPq2zekb3taZxHPPentvEwkg1H-Mlg4tMPGP4euEbtcgKajXxa4LBsd52AuJdamMMAVxLZ-LAaYPNqEHmAz-lpuC4e_3QrLmxJa7SfTPHnUJrcRi9jvwP_zuhfeePqRpMMxUQbYfiMBKat74SD74_gI6Jha5JvxzMeHpi1q2rg4Ino50LezG-cdd67A47PQLT02xlijhBVYru0hYuuoqI6gRqGGnwNExDpVQK2hLy_xyFJvYdh3cYGX_3zBY1E1asx-S3oKE5WsKanqNcEZCQg-bVm6t3PPmiVj3WAEJyELB5NXauNKRbZ1DwQyJT-5nzygNwOuPK-bPL_Xcbf6obtHAymecPZ5qEgc1-s3IfcsHz6Z31nSAWgDVN0kjzDjcus7yH-Oph_VpdD7_bUGzG7ElQPVPEp2J9IOHUscGfDpmWYGAKRTJUrXLukegmCiPYREr2Qka89HbBuToLJvWBVPdSrX5kteANUv0a2Yo2KEVkOgFcIbhNccB_shbT1jdddw9Lc3nQuibTf7ca_Q1729p173m4NqAapd52RzftlHAss8MTy89lw3m_lT6d8MVIB0cWPFnKnmDTVM6TrxePYYbUrG42yy7XVvqDtcY4yxHwKh9b4bAagG0Kjh3jdj4YmY95uM1s-Rr9YRJ2HMUboEP0ZMx7J8fRErTFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85a443f91.mp4?token=PA7A6mPq2zekb3taZxHPPentvEwkg1H-Mlg4tMPGP4euEbtcgKajXxa4LBsd52AuJdamMMAVxLZ-LAaYPNqEHmAz-lpuC4e_3QrLmxJa7SfTPHnUJrcRi9jvwP_zuhfeePqRpMMxUQbYfiMBKat74SD74_gI6Jha5JvxzMeHpi1q2rg4Ino50LezG-cdd67A47PQLT02xlijhBVYru0hYuuoqI6gRqGGnwNExDpVQK2hLy_xyFJvYdh3cYGX_3zBY1E1asx-S3oKE5WsKanqNcEZCQg-bVm6t3PPmiVj3WAEJyELB5NXauNKRbZ1DwQyJT-5nzygNwOuPK-bPL_Xcbf6obtHAymecPZ5qEgc1-s3IfcsHz6Z31nSAWgDVN0kjzDjcus7yH-Oph_VpdD7_bUGzG7ElQPVPEp2J9IOHUscGfDpmWYGAKRTJUrXLukegmCiPYREr2Qka89HbBuToLJvWBVPdSrX5kteANUv0a2Yo2KEVkOgFcIbhNccB_shbT1jdddw9Lc3nQuibTf7ca_Q1729p173m4NqAapd52RzftlHAss8MTy89lw3m_lT6d8MVIB0cWPFnKnmDTVM6TrxePYYbUrG42yy7XVvqDtcY4yxHwKh9b4bAagG0Kjh3jdj4YmY95uM1s-Rr9YRJ2HMUboEP0ZMx7J8fRErTFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویر کودکی که آمریکا دیشب او را در عروسی به شهادت رساند  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/459661" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459659">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SkLihmgA3BKTeNR2Q1x5uxHMm48qTIaZtQ0Fsru-c3SxKe2E3HpTvElBIEjQN_047iYIsStXdXsux4_ufzw082jmyeLLS9bqQQrqnlSQt8H-UPg5b3qzYaB0ZoDcUkpsmwMgkjQA0F8Uk6xw-Bniat2yyqFxUnqu3tn6uXRQxKNMpraZWDDpNYrGaBRyESQUv3WXu4kqt3in3oQpinOfF6C4zWzQJG_lWh6hFmwfQYSHdnFGFdDbtYnAV0uuWHSYGwtTkeNN7KOP4C2gn755bfto79KnBVqmf2M8LjjR9eETKvJf4uLXkAFeR0SZZHNmIc4ET6RqC-W-kqJzjJCx4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq_gQ7yZFqno60cusA7M8T2jyxrTRh_bM4bDMq79W5mAQYDgpu-sTSTGiN2wd334fvThEjTSs3V653qjUqYoSe4QKBfJEbFr5F-CSlRj_RuNR4-IJ22fhAaw57GMKjITXX1Dgs0QhUirvZ9dZbO3LBe35HXFi-do5iEZF5edpRpHawYfp2RBnBzGaga6zkM13DKQdGxr8GB43YrxuAECDX2tqJbJzZFJykgpbYNeiSS02ffZLGxe0MLm6LzEV2_CXEryp55kTqlI_RWST3z9dsqxG6FSbx7bILKAOgZoKQfKrR7YnXwSa56Bdpj7vUIuvbVXWhfjlkSaeExhgT5tww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عروسی که با اشک تمام شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/459659" target="_blank">📅 09:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459658">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea12086aa.mp4?token=f-UE7LFYCbXKcDJIN6ZlIDesmnPN5lUivbvIxoE8y1Wtl6ujpRa9-L7I3PVtuRXF_sPC2Xzj0tOfxkyfCx-84URXyCpNBlJTFNSP3v4-mNqL1eu2D_c5477v_BNj1YQ2Q502dLPQhYTCZ-_Ej4Y_hXqOt8vr-3gIlZSnIH5fqHP2wRv-KheouZVosp4sMpDUutXNVNiDl8-KDLRL6woafDLN9Yb9-e0PQbmIL3nVC0LI1o1DrtrVvPAXgKF4Db-QwAui7WO7n2MCtMAyLEJdtRSgiAFw45yYsNa6Imhmaz27lTiAdIfg0hZKRBeCLymsZ4hnuTBTAzhkry8bnfHJ6Qnuh5Q-8TdqqHcd_mZqbShmFlTG-QbpZrRSkAJ2GX2u4Fq8hcdds2b8u3CdrusMuos-i4RabDZB-BUb2h15VPS9tHgJDhT2fwLRu1cBYqGLWsLTyK5KH4EA_xipVbPv2R8HlF96OLX6d9HVNfPZjhmx28YKNuDiz7JkLXFb85AB6mPDIOSWIcppPQo6GvLKAiJRol45Bj3DYPA_OCgTwgGHlaSx_4V8ukxlDuG18mAsjb3HG1GgWLo5FLLkVJjGgnbO9v_HLSG9aVDQQPcnWjO9GLLf1JcAWyB4Xi1_YM45cpTiT24u3xNqh-BaHUKyj8XOXTbhvpl4nzIdx9NyQuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea12086aa.mp4?token=f-UE7LFYCbXKcDJIN6ZlIDesmnPN5lUivbvIxoE8y1Wtl6ujpRa9-L7I3PVtuRXF_sPC2Xzj0tOfxkyfCx-84URXyCpNBlJTFNSP3v4-mNqL1eu2D_c5477v_BNj1YQ2Q502dLPQhYTCZ-_Ej4Y_hXqOt8vr-3gIlZSnIH5fqHP2wRv-KheouZVosp4sMpDUutXNVNiDl8-KDLRL6woafDLN9Yb9-e0PQbmIL3nVC0LI1o1DrtrVvPAXgKF4Db-QwAui7WO7n2MCtMAyLEJdtRSgiAFw45yYsNa6Imhmaz27lTiAdIfg0hZKRBeCLymsZ4hnuTBTAzhkry8bnfHJ6Qnuh5Q-8TdqqHcd_mZqbShmFlTG-QbpZrRSkAJ2GX2u4Fq8hcdds2b8u3CdrusMuos-i4RabDZB-BUb2h15VPS9tHgJDhT2fwLRu1cBYqGLWsLTyK5KH4EA_xipVbPv2R8HlF96OLX6d9HVNfPZjhmx28YKNuDiz7JkLXFb85AB6mPDIOSWIcppPQo6GvLKAiJRol45Bj3DYPA_OCgTwgGHlaSx_4V8ukxlDuG18mAsjb3HG1GgWLo5FLLkVJjGgnbO9v_HLSG9aVDQQPcnWjO9GLLf1JcAWyB4Xi1_YM45cpTiT24u3xNqh-BaHUKyj8XOXTbhvpl4nzIdx9NyQuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بفرمائید قهوه یزدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/459658" target="_blank">📅 09:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459657">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c1dbf088.mp4?token=WW0ClftM6GUISpjLYyM47E5V0psl__axE7dIEoRMN30uWy2lWc8_6p2nn4wxBzAaTC_WiM_pUsDrYsbiflEkAqewGL1E4FFgD2ua5_rfc8Uc5fflGTFosbVgpdgqB3GpAOZbVWqK2iSOvc3AQ7PiugmGqy2vy1V6DfYNGmM4d0zea5Kh-rK5gBDI3Slt-on3dfocPvjfb8FpUJEqtr77oZ6Fad2S_0J44SAuIZx00pmjbL5wMNtWCZR2GBlfKlPQEeCFfsrVNRefb_2MQMXY1wR9ldxlqEuJxa52GnLnatQdg-RKJDPvgGyhCRcDDhEk7C-FXYUPGeFC4UTwW8K1sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c1dbf088.mp4?token=WW0ClftM6GUISpjLYyM47E5V0psl__axE7dIEoRMN30uWy2lWc8_6p2nn4wxBzAaTC_WiM_pUsDrYsbiflEkAqewGL1E4FFgD2ua5_rfc8Uc5fflGTFosbVgpdgqB3GpAOZbVWqK2iSOvc3AQ7PiugmGqy2vy1V6DfYNGmM4d0zea5Kh-rK5gBDI3Slt-on3dfocPvjfb8FpUJEqtr77oZ6Fad2S_0J44SAuIZx00pmjbL5wMNtWCZR2GBlfKlPQEeCFfsrVNRefb_2MQMXY1wR9ldxlqEuJxa52GnLnatQdg-RKJDPvgGyhCRcDDhEk7C-FXYUPGeFC4UTwW8K1sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکذیب حذف شارژ کالابرگ؛ زمان‌بندی جدید اعلام شد
🔹
معاون وزیر  رفاه: زمان‌بندی شارژ کالابرگ از این پس به جای ۱۵، ۲۰ و ۲۵ هر ماه، در تاریخ‌های ۵، ۱۵ و ۲۵ ماه انجام می‌شود.
🔹
شایعۀ حذف یکی از شارژهای ماهانه تکذیب شد؛ شارژ ۵ شهریور مربوط به مردادماه بوده و هیچ گروهی حذف نشده است.
🔹
همۀ دهک‌های درآمدی در سه نوبت ماهانه، شارژ خود را دریافت خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/459657" target="_blank">📅 09:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459656">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌
🔴
حملۀ موشکی و پهپادی سپاه به پایگاه‌های آمریکایی در اربیل عراق
🔹
روابط‌عمومی سپاه: رزمندگان شجاع نیروی زمینی سپاه با حملۀ تلفیقی موشکی و پهپادی به پایگاه‌های آمریکایی در اربیل یک مرکز تعمیراتی و انبارهای تجهیزات فنی ارتش تروریست آمریکا را نابود کرده و…</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/459656" target="_blank">📅 08:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459655">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf52083b1.mp4?token=Zj6pEeYN9f6tvI0oBno5EklWIwBAceZmZFslUnUvDS2kHVp36xrTaHRz-jFx4Sy7A2_0Mr9ESnKVJfILsXj_3ZxjhNknCmqeeRd-_eLTQPOR1ruZvj-IaBWGlajkalH5jpHrZ7cxHAWIrye-7dellGHxIpoA9ja0ndVQ7Q8JqP9Xt_drPoFh6iWMcJG1X6qv1A6We_x4u-WUxrjY3JkgbcGJJXkzn9UG2rFjp5wRt2EikcPTRpDHH5WqEBFmxrFF2swzyHwIpwoxymqlRQJ9qpvwP-w7D-BEkNsV9E86mB2k9Rrm4OzYgHbtFm4rG0_8kqKSCY5UspRPdO0ydM2GEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf52083b1.mp4?token=Zj6pEeYN9f6tvI0oBno5EklWIwBAceZmZFslUnUvDS2kHVp36xrTaHRz-jFx4Sy7A2_0Mr9ESnKVJfILsXj_3ZxjhNknCmqeeRd-_eLTQPOR1ruZvj-IaBWGlajkalH5jpHrZ7cxHAWIrye-7dellGHxIpoA9ja0ndVQ7Q8JqP9Xt_drPoFh6iWMcJG1X6qv1A6We_x4u-WUxrjY3JkgbcGJJXkzn9UG2rFjp5wRt2EikcPTRpDHH5WqEBFmxrFF2swzyHwIpwoxymqlRQJ9qpvwP-w7D-BEkNsV9E86mB2k9Rrm4OzYgHbtFm4rG0_8kqKSCY5UspRPdO0ydM2GEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ادامۀ حملات پهپادی ارتش به پایگاه‌های آمریکا در بحرین و امارات
🔹
روابط عمومی ارتش: در سی‌امین مرحله از عملیات صاعقه و در پاسخ به هدف قرار دادن مردم بی‌گناه، از بامداد امروز، ده‌ها فروند  پهپاد انهدامی ارتش، سامانه‌های راداری و محل‌ استقرار نیروهای آمریکا در پایگاه‌های الظفره و المنهاد امارات را مورد هدف قرار دادند.
🔹
همچنین، تاسیسات راداری و مراکز تجمع نیروهای تروریست آمریکایی در پایگاه شیخ عیسی بحرین، مجددا مورد هدف حملات پر حجم پهپادهای انهدامی آرش قرار گرفت.
🔹
پایگاه الظفره یکی از مراکز مهم عملیاتی آمریکای جنایتکار در منطقه است و از آن برای عملیات هوایی، شناسایی، مراقبت  و پشتیبانی استفاده می‌کند.
🔹
حمله به مناطق مسکونی و هدف قرار دادن مراسم عروسی از سوی دشمن، مصداق بارز جنایت جنگی و  آشکار کننده ماهیّت پلید «حقوق بشر آمریکایی»است و قطعا پاسخ رزمندگان ارتش به این جنایات دامنه دار و گسترده خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/459655" target="_blank">📅 08:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459654">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teQf6Yrhb11fR1et1gplpryQC7xolVi9GQkIXHPBxaGR1-2PFkY939o8kn1uVV7Rr8cZ1K4eIDNUzbBE-vJZ1jRkbIIdaBzYZC0Lz4USkAzYqaCcS6OzlkQ7JdjQ9277fIBtVmYFh5OO1j9j9W5fjyEc3A42P2_qyZc92DCkYye4pE841W2VMSQIYW8_Vt5-lwJ6ofdpsI8-9fReNYKp27KBMDTg-2Tc0ye8I9l0f3U3GSr8fJcW-6WwpP_xGUV_zFIbDa0rLjktCAuV6UZTQLNObI1pTbZaufrfAJhGiroQ5_3zcbxY3NcoUnR0AcT50g6DUVngunfs0cWtJnR-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری کارشناس رسمی دادگستری اردبیل در حین دریافت رشوه
🔹
رئیس حفاظت‌واطلاعات دادگستری اردبیل: درپی رصد و اقدامات به‌موقع و عملیاتی منسجم حفاظت‌واطلاعات دادگستری استان، یک کارشناس رسمی دادگستری حین دریافت رشوه دستگیر شد.
🔹
رسیدگی به این پرونده در چارچوب قوانین و مقررات در حال انجام است و تمامی ابعاد آن بادقت بررسی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/459654" target="_blank">📅 08:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459653">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biuyhGXr3LeeF0t3AK7iCh2-_ahAPy0xg2mDpkhIua8Yy1phkrqPdWcyboQ0yAA92_eJsHps3mYevUUDcWjUpq8MvPKjD5_yXeHCRRzTjgNz54skSOL4Nfa773rscZ9LUAfG0aUlnEeAWNoM-Hhb_rG4eEN__9UxdKZyZCmsSiisGMUing3DpPeN60ZbYoDpwTHohcwEEUarmRsX-p53K3flokHXCoBXs6x7gf2clJDnPjQSpl2_YUrlufNZXdSWixWSoX4yljuEhFq8o9j1-Q4RKgl_larowMgVuoBQaTZmncupYSTYmpkeXmIeBERhe3jn1S1Kid8v-YR451KN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">٨ میلیون دلار برای صفر بازی!
🔹
سفیان الکروانی بدون یک ثانیه بازی برای القادسیۀ عربستان، ۸ میلیون دلار به جیب زد. او ۱۰ برابر درآمدش از کل دوران فوتبالی‌اش را در عرض یک ماه حضور در عربستان درآورد.
🔹
این مدافع مراکشی تابستان از با‌شگاه اوترخت هلند راهی القادسیه عربستان شد، اما تنها یک ماه بعد از امضای قراردادش مربی القادسیه او را در لیست خروج گذاشت.
🔹
حالا او قرار است از باشگاه القادسیه قرضی به بنفیکا برود و برای یک ماه حضورش در عربستان بدون یک ثانیه بازی دستمزد ۸ میلیون دلاری را کسب می‌کند؛ بنفیکا پولی بابت دستمزد به او پرداخت نمی‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/459653" target="_blank">📅 08:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459646">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_3YvMVIYRbxPyvs5YyDfEAzGTQLQY_asYZbEfZrJNexoJT2_eko9n1Y_0bDtF4M4pAQrIGhpPjjGjAtUMoJmaA92i-CkdXejlfUizr8Urp3O6xaWXFqmHFdOJSrtW1huBYFtblI74XV_WiAb6UtuvWws_ruUmT2T1OvoimgdS5BL-f0T4gb4eHyRzNmz41iyrCyacH_uNiQ5bJXiqrA3S7SbT7jBbzkBNxuVJbzsDnOf_yHNTSuegPaV_SnbNDHFBcmPFMWxBUPHVMvW7KjhmvBNF9V4PTgOF1JHgB74Q5IjNcwOItssN39oHZK27ZVTrKqo6R6XrdwD4V2ZtZYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R73toUoKKqDxdz4950OFVI5plRaVhTh4ZzI9LN7LkSPwbT8DKCUrSApb_ePgMlNhArHjcRm1PJM2__FKRTJiNq1FFIdV5vqkkOTuQ9UhvXUKfTSOc8VNld-jbKMa92eezr_bpsQouSdycw5LaH0ROHDTv_agPbANmrsRn9QsKyXCNWGPjzAAHG7dw27jhQybFczz9J7GmAl_dXzypIbS8Hr6slNbxRLqYpODQLYGm_5cGN_gzVB5GuzJYDK6Mk89AQT5fCVTu1ZR5Zf-O1erQH-UtYolJPf-o8CKWCrsCO5IABQdH68gYMx2ZPnQSG-mRvMuR4QW2Zwms4yPTL0WEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DK16b4o0Pmc-w6o8xXMXrj2aEV9x6uKNzD8lJcdTuzEZihugmPc8-r_mIxYvE5C6EBeaJlG7_Dx9Me4JkGfx94omHZmx8ET_i0KoaJYL92IifHsuzHN6cJxBI2j-ZWSjD3ed7UnEHsv7R9cwwBEYnZrpThOy2v8Co-YQK0dTbYmVxyXzHK3kFTwBEitU6GCyB_3WY9UGhcpLpsFjoFMtQkDKuVEmQLDvv_L9VS_3cNE0BSqB7TBUFSE_btIXxpPJ2jNw5RMYguZ5ReDahvphIOAGY4cUySFByAw4UWEARQel6F7cPpPqQmFceONWtM-64tfPzEG7Ph-m3sEUwXGLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nm-KzowKPD3DkxTu4r_mgDktBLHpACEuZdMjH9b40YjpIB25g4DN7m1oS1pJbog7YHlHxOD9yT5FVAYm9Tg_NWV7Y0K-X_bzgxotGOrXD6D1ogaeizXA8S8ed_-dfj6jZe04eiwgfv7EARps3G-XpbLlCDLJ7Kdx6NzPIdcZOVQU5iqpeqvEbzR49LWUAwBlg5mEYF0Exdwg6OmntLbYzmez_l7WlltWsZl1q5PD5soA-vciQbQagYWqFXaBTHeq_TYreRtAlIdqeW_IFxtNlPPaEx-Rp4CYie2MZLfEr8nBi5xvtCaZXBn02EkFLiLt-WrA_CDUXKAduz-ugves9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dERmt0j9vcm1ByggOZBTZK68awuuZWnMToQ9jz2kNpcG1Na_BzPaPKzsM70-XU50VpOJSE7R1t2AbCTlzKj1n8Cp7YZumfEInTiYkh-ZM_U7vItD4W1j9HincTtAruNUoeZOk00yLrQmGrkNswKxjpy1pAap6nxdjCYKUyy4MmcUdnU91kCwXUwiFl3DYlFpg83Aifsu0XldQq_kr9AHlYgkUvSAqzQe9UhF1jpu0XjWazgZ71r8Pycyh6x7ssDI2YJkbdZ3HDTwIb1aMIasbtvRzLlBY7JL1FUeYAShc3DXBZqqrmOXa8sAILyXPsFG7DaMKASOkTiqlIhzG7-HHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9CHOtDUieBD7bPWOAiJPPHHB1wCdqfcAkATJw-kbJS8E1v-GDost8XwcT9EXpnKBQTOHJxIfN8v97n64NTljkvkQj04_S5f8fuNfNoqIl-RhtZNH6HGrLuPOrOvg7B1Qm0Hri142xfxhpLKIGb-SD_s3NMwY58UwVmz3dcUxr-4oXqVi2SnRg5vYMUum4YMckavHYyKZlZDXeJx8Q1w8PJqiNxTQRR7JPoS-Nnxy00Tq1HBTIoHGQ1odQz9BEOSnLM5uCanWE2smd4oa6R_U9X4ctTlIkVrw50zoOdnUM3r7I_bFfp6g5nXa4wlRCvYOXl1uQWs0y3s_uyJJPrLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyPkh3_cVgaXt1_Kinh9yNAnYpfo6wQMkdvPiL74--JnYc2iyP9qYINO1koUJjXY31-m1ClLZ1X56nyMMZi9SEQZY8HjsH7Ty_oGrmxdjOwyS69rjwI-cIsTQ-Aw5VYQLqy-a2Il9E65XDhA2GSHiv-m0oknj262vse5oZ7rzT4uPhKxFVjcuOrgeLSFrUHIPWtb0FwWQmN0bL4qiF9dMdL4qGlEh_njgyTuLSZ9CwMN98npLTAIyGHCT2M2xlpF4ZXM4PaM6lXpO02wbSInBdSKMcFOWvwqjsmCtvEVSNNOrG7azUReHv5Y5c-axPj4rD8Rl9AWh3hf_oUO2BorbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید اصحاب رسانه از زیست‌بوم منطقۀ میاندشت
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/459646" target="_blank">📅 07:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459645">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
برای ثبت‌نام دخترم در دبیرستان با مشکل مواجه شده‌ایم. با اینکه معدلش ۱۹٫۵۰ است و در رشته تجربی نمره لازم را آورده، مدرسه می‌گوید ظرفیت رشته تجربی تکمیل شده و آموزش‌وپرورش پیشنهاد می‌کند به رشته فنی برود. دیروز اداره آموزش‌وپرورش بجنورد به‌دلیل همین مشکل بسیار شلوغ بود و مادران زیادی اعتراض داشتند. دخترم آرزوی پزشکی دارد و نمی‌خواهیم برخلاف علاقه و توانایی‌اش رشته‌ای را انتخاب کند.
🔹
لطفاً پیگیر این موضوع باشید که چرا برخی مدیران مدارس خانواده‌ها را مجبور به خرید لباس فرم جدید کرده‌اند. مگر بچه‌ها سال گذشته چقدر به مدرسه رفتند و چقدر از لباس فرم استفاده کردند؟ لباس‌ها هنوز نو و قابل‌استفاده هستند؛ چرا باید دوباره هزینه‌ای به خانواده‌ها تحمیل شود؟ در شرایط اقتصادی سخت، هزینه‌های مدرسه، شهریه و لباس فشار زیادی به خانواده‌ها وارد می‌کند.
🔹
بنده یک سال پیش خودرویی را از شرکت سایپا پیش‌خرید کردم و در قرارداد به‌صراحت ذکر شده که این قرارداد با رعایت مصوبه ۴۷۳ شورای رقابت است. اما اکنون دعوت‌نامه با قیمت کامل و بدون لحاظ مصوبه ۴۷۳ ارسال شده و عملاً شرایط قرارداد یک‌طرفه تغییر کرده است. یک سال پولم را خوابانده‌ام تا با زحمت یک خودروی ساینا بخرم، اما حالا ما خریداران به‌شدت متضرر شده‌ایم.
🔹
مدت‌هاست عملیات حفر کانال و نصب فیبر نوری در روستای زنجیره علیا از توابع شهرستان چرداول در استان ایلام به پایان رسیده، اما تعداد زیادی از خانوارها همچنان به فیبر نوری متصل نشده‌اند و منتظر اقدام مخابرات استان هستند. از سوی دیگر، تمام کوچه‌ها و خیابان‌های اصلی و فرعی روستا که پیش‌تر آسفالت بوده‌اند، برای اجرای فیبر نوری حفاری شده و پس از اتمام کار به همان شکل رها شده‌اند. این موضوع علاوه بر ایجاد مشکلات برای مردم، موجب از بین رفتن بخش زیادی از زحمات انجام‌شده برای آسفالت معابر روستا شده است. با وجود پیگیری‌های فراوان از فرمانداری شهرستان و مخابرات استان، متأسفانه تاکنون پاسخی دریافت نشده است.
🔹
چادر گل‌گلی که بر سر خانم‌های متهم است، لباس رسمی زنان مجرم است یا چادر مقدس برای حجاب و ادای فریضه نماز؟ تا کی این رویه غلط باید ادامه داشته باشد؟ مطالبه جدی داریم که نمادهای مقدس حجاب در انظار عمومی این‌گونه مخدوش نشود.
🔹
تأخیر نتایج نهایی آزمون مهارت‌آموز دانشگاه فرهنگیان و شهید رجایی را پیگیری کنید. ما داوطلبان ماه‌هاست بلاتکلیفیم و به‌دلیل وضعیت مشمولیت خدمت سربازی، آینده‌مان به اعلام این نتایج وابسته است.
🔹
لطفاً پیگیر واریز وام‌های ودیعه مسکن باشید. نزدیک به چهار ماه است که هنوز وام‌ها واریز نشده و واقعاً به این تسهیلات نیاز داریم.
🔹
از مسئولان شهرستان فردیس، شهرداری، شورای شهر و شورای ترافیک درخواست داریم به مشکلات شهری و ترافیکی فردیس رسیدگی کنند. بلوارهای اصلی، به‌ویژه بلوار بیات غربی و بلوار تندرستی، با مشکلاتی مانند آسفالت نامناسب، روشنایی ضعیف، لاین‌های کندرو و دوربرگردان‌های بلااستفاده و رهاشده مواجه‌اند. وضعیت حمل‌ونقل عمومی و ایستگاه‌های اتوبوس نیز مناسب نیست.
🔹
شرایط آب‌وهوایی شهرستان مرزی هیرمند، زندگی مردم را با خطر جدی مواجه کرده است. با وجود این شرایط، چرا مدیریت بحران استانداری اقدام مؤثری انجام نمی‌دهد؟ مردم هیرمند تا چه زمانی باید در این وضعیت رها شوند؟ آیا مردم باید زیر خاک دفن شوند تا فکری به حال این شرایط شود؟
🔹
لطفاً صدای ما را به گوش مسئولان، به‌خصوص مسئولان سنجش و سمپاد، نماینده‌ها و رئیس‌جمهور برسانید. امسال با وجود شرایط جنگی و دور بودن بسیاری از دانش‌آموزان از فضای درس و آموزش و حتی ترک خانه به‌دلیل حملات هوایی و موشکی، آزمون ورودی ششم به هفتم برگزار شد. بسیاری از دانش‌آموزان با اختلاف بسیار اندک، حتی یک یا دو صدم درصد، از قبولی بازماندند. در برخی مراکز استان‌ها نیز فقط یک مدرسه سمپاد وجود دارد و امکان انتخاب اولویت‌های بعدی در شهرستان‌های همان استان فراهم نبوده است. لطفاً با توجه به شرایط خاص امسال، ظرفیت پذیرش را افزایش دهید تا دانش‌آموزان شایسته‌ای که با اختلاف اندک قبول نشده‌اند، فرصت ورود به مدارس سمپاد را پیدا کنند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459645" target="_blank">📅 07:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459640">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRIBijN_uxi_uncCiNOOZMAuSXgo3P-1jmtMGlHRPfmOEgM9TZOriPtVhT0QGhme50tsfHdCTetvg5SUTgq-FX9UuMtJKZUwZgh10qapjMIPBqOq3gzp5wkl-bxiJIsTiDm1cKkI_Vb5pDryXiyf5bziH7nDR3SAyEiz20VsB7y2UWUgRpnEYTC6l2tPy8R8IdfIeZ-XPh4ejjb3vAmw8jj7IPxCfzwPH6drDvO-WKcN6aCW5b4tcKXZRH7HQQGfq7anVhEul8gaamjHXq5-8xCdOjByW2EqRVhixG6_qn_ReZLsPNTCy3jU34cJ9ZuAbKe0uTXegvzBwqMnXZkUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F5LIxXOc0b0Iqi3T0Oixa6YSJ2HkBc14-ps4DU0YQrtDM31uWHJp2T8usdsR86W-da2nFdVnOJg8_IMMY0MxB1AWRR8iwHRssGhC43qPsP7ZxC3IgCOv-x50mX5ao0cyk0dUmYMli1sQxPuj5U6209tNBKjQw2hIWIMpFNYhpsA5WFCcRWZZ9A4OZKG0FKXy9tRCBK24wXHRYHCnS_weZFKc3ekJKo1GVyS7BQuSRDTkKw6srb-e8HBRCrCy53eYPX5Gq6wuvfiXmuONNq91gIzGcLNX7HLIa14l3lrnoH4H7n-6kdHCbjGYKn-F_PJCp27qrnUlYxq8-r_vjLmwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJTN9to3lYrldL8W783Bu_JYJZoqTkcHIhd1BCTJ-GHDG9mAPj3uqEpTTOjLoGeS0KsCR8MVImXOyTX8AHJlb_UUuL41JbjdAoyLNKaMAvnRKBugOi8cA6U6sdb8lk_J8VXxEnGEJ-tWO0kDOYE1UTyEh3ttTLtI9WDO91LEkMbKWOsWgA-fMzTSb5ta4yeU8E8ooMG_EGG2M62JzErIKAR5vzJP0Zufbf07x30lp_tLB7JWIVeM8p43SwfvPew5DgFuU3Ifwu60nvFgP-GcO0xz2N4q7ehoqmaEYDH2D7jyxAcha2w2TOWBKCdIAjQ-pSMuUWNdBJJLQNnmS2Vheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puAIppGsrRdsVXMJIAFxesGp8cEhqkuGNVkzkBC4JmRlxB_ND42JZgOe7b5O3yQ0XLwTfaOsmYrvdpfGj4m_2I6m7QyeyljGe-isK0NDvC0cbUj9epJtcytottRL_Cb7KR5pesKZ9aISXda0gsJivIWZOdSzNtubY8izsZTxWgd75XeX_AtBMdJH_PtY6qcjPizfV4VoaehjDlAOAqSERA6xYQgyU-L3pPhUIE9yDAqsIw9oyWMH3q90r9D-9TKfdH7xdZw30dWYRaj1TMhIPOdcYxyMp5LB0h-b4p1YZpHlgBMGC4-Vkl5_NoLV7bEo26moxrauyoQNudlPsKYomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1ZgJGD1_v3e7Vsr8v_lOSKuoI123fp107c2QRzwDn3qgt7tcgdvBSJmS3n-sUZAtEvVKcWsD0XC9ILT1KNlpnryHFWklR18gf8uzsuooPHWGQEnP5KXOYcb8OReu7L3Go7CmEEaxjtvf9U9YCw7ERqUU4-Vjad1Iy3rOs-3DeJrwYv6hISShgj9RfaW95NTepH1W5MHfzy_scGWy2e6mvv7LfPO6RlIRTjGn6cAVPcw9y8lHwUKgKkyCndQwm5OB98N5jiau37LHH4sEY1naNO389ONWoN8uuRb_h5sRjiLAHunoa8AeaMlHj1qgQhnECwFVy7fsF7ZYR5RrwBuGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سفر وزیر کشور به قزوین
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/459640" target="_blank">📅 07:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459639">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هوای پایتخت امروز هم «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۸، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/459639" target="_blank">📅 07:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459638">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۷ شهید و ۸ مجروح در پی حملات آمریکا به خوزستان
🔹
معاون استانداری خوزستان: در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/459638" target="_blank">📅 07:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zca7kvL42emhCtdxnoMspvficdSWk2EJNw1dvXEQCT_NVMRDVHxTnlw_9DEMndGpXwzfTyLsUE_h6nwfXqJH64d8DEprCgnIuaoAoK9AnrlXqf1TaVPKgRbtfrWaFX7EjOrNR6bqxjvMk-_J69IcGyE7JVoWePuD3BgYWRX1Ji6BkEy4Iec0YFw5RNiwaRoFAzdrT0Xo-98RQFvwEXygiaLHH6gDO_hhNwwSNEiYwib4LkCHX6Qxfh3lcXMKIW4lwlYgGBx-3JtnvZnZRlcn2wK_5iOFYNsWeMgfAHSXqjeQG3_ZDmaMeWU8wzncO_5uash9lkIBCYejQpt3lPLEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1nTIxA_qE23iQy5kqHr6Vg_r7ZgwVtBZzXtuefGgvP-erKsqvKUqdB_IEDLDsf5QLTPLxKh2z8byZj2WtRClvWcySXOlV5H-EmmP42l8PAGxtkuESCCuMMEVKF4rsZaZOdoxW6Ir2ZXF7hlcWNQG566JLwN16JOmUs0DA2Q21QVDjwfrSePyyo5MHBCfGJ11z8oqRurrlA8Vxm2gLr9kPJ_XemMAvZwuebnVBw0DCsldTxJjEk_XY8dT_4x7dMVaDfAgjXU1w0RQLOgrZF3IPqGIpQf-WBxZJUk7CpgtHPCl0NRcWi8fiD1CU4XadsDzxjdKPtpQ97Nwwpmno0v9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QW_0pX_OjBmOQwUvzfWCGzBABCJuz9ktMrr2Pl4-boR2CrHUSgjxDc7WcQKL8bOpbWaKsPo6Vw4ChS_I9qDabu1uf2BFJL_F4eUxivEMJvHPzAtFQ-4PMZ2TuRR1DJX5cRWPBD8ykuYwBRaf1R3lgR_dWmTJrKGijgGKiQHIEGZGyUePP1dA1FHx8X7_M7gq_aOeLSy7kSnvgeFnaCpMGXg9tYJWE-gXkAe4w2EalZxSWp0qjoupzvYftzpoL3VTc6O9DB_uujiHnrWHAXsPBCcbmefwoKkfgRZxWmg3qh8Kqc5_5c5l26wUPc8dGXCvjvQ1HMEC7674gfM863AdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/my3VxFtC2BzTvWp_D9Vs7RbXKwTVhAS68CxYOcJhae13qS6Go_HYH4bKCqJIFppFI9tCilJHcgQCYAlgv7k4nkM57HuxC02w_iZeCxPGedxSXLSsidcWrNcvav19zDyiDj6o5LF4oPND01zr9GFF76xV7jPw-cfx0gAT302CZXnv9mXJ-WeuzE3Cw3ejaLwb8FhF4ySi5TjtzSb6KK7PAlh5s6Ts2GnmLjfTPa73ZFwhkvRl1yUUfT3tc88CX7XQDy_-lR1-4nRubVWIy8QXUB8WdDFeIZLJq_d29Z7zEEih8TyJMRemg0Ttrb7Jd5ujPwLdEte-UoGFoy1ZttSwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtLx2aagc3CnPlJF7Wgf0zeq9nl-cYmhNYRfdO7Y9rfdtB1hJxIoGVhM_d3NDt8mSnV8yFc2BmGAtNegn3VeUuDvN-Qgn7bwAhKN-QukjvLBalIFcDyf9fs4kBo9HoPWzjXS0uiUDBHsnbc3yLpABBlmh4Urge-A5skY3Ud7JwYgOErh0NaHa2shYSsXYC_pwtC7GZajLybOPQgtL8-4fBBq6w-qSy3Zd61AXCS82au3hJ_bXxajw96_eN-SRqG1uW6hNZJ6N2EOa--CzUWVBJpvPVFaxT_Hn9WansalLugYs7_Nczv5asLjX38D1sW2ENcAjgYJqPAcVYAa6EKsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gewIwHy_Y3p5QgszL_JNzD5wjraH2CoYfj8FIdWAdAB7hPOibGRcSPnxHjUHrzELKTsVKhxVTrVmMXHSjcWTLCk1aZNRy2dnSS8bZoZ0bVziazQ_WrPXbvViYjBnSlQZqKCSW0zedspCUp1ybr9ofxzb3SMRcke8gRQ753L5gfqmjE1_0HewrqCRrVMHhlU9_JlYJOJ3WzAbnDgW4J8SaqxccySwookWmu2EriMB2YtE5hewdF2-s_SWBapej92X4ilwQSJNGG9UFuVBynzIne7FjfRBBzwp0SyN1ihka-UPHmmA-n4LAI_nucG-lb_gMKZ66aRKwhaERR-eHq_pyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cucRpvaaYs1hDJbPI1xMHuVdtLYXR_bXFxgU-K53B3DZjGghsU-sUJdGbLLnww858rPfzioBmVZIb8SUudTeUBd4KUhmSGD8ZbWBNBxcWv11MRH8ZkKl3XzxrHolra58iduoLXfJ4O9aK046gI780AUWMa-rY2SoyZWdsgkRINQ18OdYU7rbwolinljcRsJZUgZX9ahybZ4Vznf7DEIHn5DLPMcwoKPIt14zb4mXdXaDOuI3C7l4CIrNzwfYeXJzda6_2OtssvAIzjoO5tP8piugt9lgMBJ4sI6xl4MmkXyckWn6SF0pYGiGacz24Cj9h62nEte8qQpLLeCOEqsIcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
📷
رقابت پاراگلایدر سواران کشور در آسمان مرند
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/459631" target="_blank">📅 06:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef3e53a1a3.mp4?token=vnijdnVoinJTLNCM5pdNK7qOZXQiA_BDvkQk5QyAfT00KAmHbGy_1XgbepeqTNSdrlbb18CGS8ablpGGrGt2Whh7lwOcxtHqIVs3Uz7S23R8iGV90HJCBNtUOKNM8wXcuxq0XF9dHgJHB7QK1fYpdFTtIjBMvCGIAmGgZnj5BYasV75I8-u2JwE1UwW4IGUJ6eiJWjv5MUhkfayT0Puc09cv8cFfgj8_wRKjxYm_PkkN3Z7hAiGbxxcLyDKdPWaNSI053mwNBULp_B3TrXhLBZ1_VNLGo9KS6BGvVAB3tDs7w3F0qhh4iewFXoPhPNf3yZUhn6F79gtKbtDPtdGlHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef3e53a1a3.mp4?token=vnijdnVoinJTLNCM5pdNK7qOZXQiA_BDvkQk5QyAfT00KAmHbGy_1XgbepeqTNSdrlbb18CGS8ablpGGrGt2Whh7lwOcxtHqIVs3Uz7S23R8iGV90HJCBNtUOKNM8wXcuxq0XF9dHgJHB7QK1fYpdFTtIjBMvCGIAmGgZnj5BYasV75I8-u2JwE1UwW4IGUJ6eiJWjv5MUhkfayT0Puc09cv8cFfgj8_wRKjxYm_PkkN3Z7hAiGbxxcLyDKdPWaNSI053mwNBULp_B3TrXhLBZ1_VNLGo9KS6BGvVAB3tDs7w3F0qhh4iewFXoPhPNf3yZUhn6F79gtKbtDPtdGlHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا می‌توانی فرزندت را در خانه ببین
🎙
هادی زینالی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/459630" target="_blank">📅 05:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459629">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WB3oxZEQ-A0UH5qo2ZylVIdpd5cpyuRfJ80A0YDJRzsd3AdBoAD38us7zih3qnUmLYGQ-mdjR9gEHd9PJhl1OLO-lRvAx0BEC_xsjHjVUfoZbUcDmgmhpT0gzx9v-lx3KwhdSaiH8dYuRPb-UO86574HW_Kpq6xbewjW-iMKTFbNQwB8Qn3hKau0a07xu5QGZZf_kjrvyYbG5pAZLOiN30k88Z-mlMdsRHQJAI4AUuqgojNb_4xfgrgGQYW2IQLlwbREdPWRxNfZ4EqwNZvJ3N1MKZwgbUyC5PttzMk_Qr8acEUm2r086BSmYZIo9RWfzMfPhEewIrWRy7O1-FOXrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از کمپ تیتین چه می‌دانیم ؟ | شاهکار سپاه در عمق مواضع آمریکا
🔹
آمریکا پس از افزایش آسیب‌پذیری پایگاه‌هایش در خلیج فارس، بخشی از آرایش نظامی خود را به سمت مناطق دورتر از تنگه هرمز سوق داد؛ اما حمله موشکی سپاه به کمپ تیتین در ساحل خلیج عقبه نشان داد که فاصله جغرافیایی نیز نمی‌تواند پایگاه‌های آمریکا را از تیررس ایران خارج کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/459629" target="_blank">📅 05:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459628">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHZhwBpChCzG1O71vBJwVi35YJPMGqRrxTe5rDJCbYbmhLDQJMn9nOiRzpSbrMzkyo5EGP666bpFlE5yzVTOfSjASiHHUIxWZZF54Sgn40GjZ9JgiJlWRO2SqnHdsJem8DzCrqtY7PD8WjhqphX7V4HCk-kndyrCIe0S44tuU71-B5TOPsbTnJhXHg65N9cDD-5_L649qJePjnphdnJFSdtgK5PCvypIOCUPTWeyfq3eKddudHAGlm7XsbjCLoKVZxFwk7a7jqgipbMHa581DKkZZ9shAtSqt8EnWbIWoDQD2ZHuFzAMlH_ckq3e3GIeStnEcwKAntBOpif82cOZfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نمی‌خواهم ایران را به میز مذاکره بیاورم
🔹
رئیس‌جمهور تروریست آمریکا با تکرار توهم کنترل بر تنگۀ هرمز، سعی در تشویق معاندین به ایجاد آشوب و اغتشاش در ایران کرد.
🔹
وی مدعی شد: برایم اهمیتی ندارد که آن‌ها توافقی را که حتی از نظر خودشان بی‌ارزش است، امضا کنند.
🔹
آن‌ها فقط دارند اتفاق اجتناب‌ناپذیر را تعویق می‌اندازند. مردم ایران کی قرار است قیام کنند و مبارزه کنند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/459628" target="_blank">📅 05:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbNp0-mCim9SnTF-J7sh70GIl8w_Pbol06uPxlM_ag8NqSIh2TiPWwoGgs62dxmsH9ilFgPSi3CJ0C3jLt3bzMugieCX5F1u_zbnV-UP80VMjfxQkovyvNDs3dEsxqnwwLJLKSnMoTHY4pt3J927kgutA6AUKdzB6GrvMjhKgyaRRwbXmGJcrp7Nfhlog34OfHxpjDeQtJuipPmvBEsmNy3Qg5tmuu73s0XBaJZnZj2GP_G1eTW2_ZtdYcgWiNFGGMS3R3sHc9U2dDxWbEIhUBscQU0Wq7Ro2CN68InbXs01y4poVdHEr_fR9iWf9dY94XIVM1mIy07-zCND1oaJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژیر هشدار حملۀ هوایی در شمال فلسطین اشغالی
🔹
رسانه‌های صهیونیستی گزارش دادند که در پی حملۀ پهپادی حزب‌الله، آژیرهای خطر در شهرک‌های شمال فلسطین اشغالی فعال شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/459627" target="_blank">📅 05:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qktbI7pKz7MW-dWivPZSWZWo9sO6W7x83YaPOEZhDqGIrvXRH39cRTknZRV1PFD6Tui9HKh5JbYIfE72NXC3dDMrMGpzZ_Bz-MUdWqIA-BzKeF3mUy_dC_OgWa4wLvlL0n_miVGph6UjQOE4xR83P3jplakeqbqoxbIkozRSaRVTqE-a3rFpuIZchgVIsEWel-5xaVj-kQyv8B_JMVErgfpdw-8M_Xf8dpuT_dck1AjxUeAsT6bvfNDXocVkvyX7ipeMkM9-ABBppw2WF15oxBBRmhWwThPsbTe8C8qgGNeZ0n8FagzCItvrI2lzOwEB-AJ6UBDPPm0HPuU7Nu0ueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۳.۶ ریشتری در شنبۀ بوشهر
🔹
ساعت ۰۳:۲۲ بامداد، زمین‌لرزه‌ای به بزرگی ۳.۶ ریشتر حوالی شهر شنبه در استان بوشهر را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/459626" target="_blank">📅 04:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یمن: رژیم‌هایی که سرزمین‌های خود را به سکوهای آمریکا برای تجاوز علیه ایران تبدیل کرده‌اند، باید هزینۀ اطاعت از آمریکا را بپردازند
🔹
وزارت خارجۀ یمن: ما حمایت یمن از ایران و جمهوری اسلامی را در مواجهه با تجاوز تکرار می‌کنیم.
🔹
پاسخ ایران به تجاوز آمریکا حقی مشروع است که توسط همه هنجارها، کنوانسیون‌ها و قوانین تضمین شده است.
🔹
آمریکا، منطقه را به سمت تنش سوق می‌دهد و به همراه کسانی که در کنار آن ایستاده‌اند، مسئول عواقب ناشی از آن هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/459625" target="_blank">📅 04:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459619">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWBmMfv3YLGYbY59a5MU2yBoGcWjOguxWOJ3uDXK_t9Fgzt-t81LFjJaaKIgNNLu0QWpHllQFwIM38FR2sNgpQxzIO4gYg4vRU1e4Yhdy-9xKMMQvoWSB7L7GOye7S1ELlLcRkchQy9aS8i1klAobXzCoilGPE-w981gOGqzNmEC1E97PxOciODvDokAgOZ27U9Emndn9LFkMIrm042t1AP3vfPr4IMgp2RvEQJ59q1HqmEx4SEi0uxeqbvg9gDRLAB1r1VUirNfRx4w1JvGNPeXlQNX2xHMFe4Puw1va-IMvvVhUBCAe_qGzc6dGTrbwknuj2kPcWmEgyMFkCQa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHDw1ZFmAM3HbPePgY4PL9pH466I5CmSbRSqFgQQ1jWFbdKQfLR943lBtmCgMneKBt7BcbbPxRcd4Uuzo9g0pyQQbxA9tCngjoBulhpLCishzwm2fwbJeTosO5VQStUdni_QpSdlQttg5iKhIFR7ZvaoUNgA3f7TEYSchOyX4OCiRomNLGBqzFFPMpTD9-zoa5atWql5mrAhqLj5xP9o2gzkBiAAsI7HQ7ZmkfdK_w3K3s1iOgJvUBjzW-MmOs2WzPdrXy8sugc2FcLwLW6aTC9124NANsATZ8nLJGwRudYigpoEYIzj8g0IjMJBfmvjErUJIed13CSieZ837D9eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bX3csgYTmB5bZzHH31W-xtYcIf3mzdHRBujVAAP3R7gDENW4C0UgA9R2zXa_DAF3G-237fFZBmDSAz0x1EZ_dzPURUbxztKNUpzs_ljX2FK839Z3fewOMzpkMB8q1Ipwwc6UAjAU8Y2hV2E5I7s5r3epeVMB_g3_cbMzAzucgtPVJEYIXE6dKNle8VzPSecPW91p9oIqLEmIBCVl6v02as40XRma_gfYREsf06Js0-AjbT0pYPyu8RqbWye8i6YeH7Wllw745uAi_kANc8KigxtV-LpHJBhlSFAlrWweHzuGFz2cYv-iXVvtOw1B0qQbKJsisp3x1ykkj1tPagKGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFGZZU3VdD6Ecr81dJIrhLnv-tqalvP1Jee4g3Hh3Zcwb5lfVyALbIZZbtQFoHuyO_LqHTWg0UJqEYeOEzDO7wVqLt_WH588mxBldaiMVnK_h6R1CmEe64smsYHH14IrnfyvgK_IwQT340Pmo_EpK9UFvuu39L3G_n6P5n4OIqP63R7n63hdMEW-kdLmGYK_uyhRzIAsyXRrYrRuYS2DUzEowz6CUhPXyLQYk4uvGixK6vaYVHV94F6ZUbEGrjAmTeYLfeEzMvaOYCcp4HLV4Rmo0iqe3GRyhVaXFSswirtfhQuLXKJGuIzx5vamVaFy-PgTnRfZacL4ZZ3ua_MO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdMSs09DCueymEWq7PIDQnnX9wbGQCvoygNm3EGzXaiL2CoxFXMw1p8qy6ppEHdzSkjwvkyiKYvVqQ7dBAH5AzleifOeKxqWaWbJszArkAdVtEkqV8Ss7_3R8OHQluN1VluQS-2rMfPN861Xs3xQpxt161azkfsDXcoY1A1V3iPoMy4tqpA0q3QcSMLOSKrCOb-SZa-6iRGOylC0_5WBI-v5TnkOPHwKs0F6-33Ybjnc3jlAe5f_w2Br5Jsh9tECtfKDOK915gtRmN5f6UWrjlT1Eg8Qg8Gecjoka7D_Yk3CPmyTTnUb6NxrAdfBS2-sZntafJOwYzJTx9AwSsvBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dIHWb60z08ppvOoZx1arVWh-9rUiqdZ4eP-Uxxyh8NmFCpr65WxOivVdj-gdKyVsgFns6CRRwhbccd-Q2w3-ZcUfiyEgXyYVcvI0d4lbhGYj61So06sxkgB8vGATJ2zSeaegbOmuBbHWLBDwLjX6jh4kt8u3hVgw7fqmZ_nsHg_VMIcborL0nFQc39-rCeHMEDy1cfKGJLTslqFrPwQcsJFA1wJx27Xf5hhzhUQG4EfhGxHzfklglEIVwCmC3TbXUUO_nIqGUQ8oSn9a04EJJnSJHFGrjMMSLdp5CdWq6UeP__UPmak-JsjAAACjrHxMYMf1GLxWhpJMIvWib4PkfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۱۱ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/459619" target="_blank">📅 04:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459609">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dPYNBvrcmq_CDEhCRXGpB454UGHdFQLcMz85-HIugesmt39zxgQtIC-7mH_gaEQh_5bqN7pL0-h-8ulSgbBEWBc37mLJtOxbB83A7TbOQblOxPG05sA0CZf4XAx8mcgHTqo6AjHM-GK0q3KKqKb2_KP7-X1aar8Lg_0YvQyqO_01aWNf1CpqD_KAyYPg4PdQsiwE_FCyzRD4cCdPn4JhlZHPz9k6a35pbYLF3_94P8Poh6XrcSTLZqXz9Uc--MG-NwCtbqbKP4pFOCHjWnf_vcekSFQ3iBV3Ef72kuC0nAQbebtmzgJkV-4xEUJCvtjfXt9I9Fj2-4hc_9BFsJgumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUmlgKnwgjdAU8PVUTiCMuSsfOZtV0GlshADUOYXXDxfgHpQtZPnSQDXLxQR3lhvk9Wzn7nnwExCnnaz6DFeSaAN_Jmoe8bZtE5aGxlQWXU_nILJrRU8gaUHQBxXPw6mGv6ci7GSWtFj4Q6nuSXT1M5NFYntrkXRmCk1NgZuPC3q9iUboabyHL8F9L5k9b5BXqyBFIGXVskKehFe7mj49uNM3aOnGd3b4RNi-yxgHsTExQ0nOfHtQqBL9kThr6XB_BleG2ULB3Mg-UT548LRRoUoePc2liKUnZeyQZSZUtKOxfVX25YALv3EgGFXd5ucH-Pq2WjSYODMH-qDurFtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lehs9-TmIlWLwZklr0fAptLiqBOTCcL-LF0BaGGlkfGzHg4SHwF4ntRKG1FEJVY3G5PHaxzGIKY-dwCGqmr-Zp9_np1zew8MQnrqcJyjJiyBNvYCRziE0KAWAYdjDC2-7lx57dyie8YLJrK0-D1xS5q5_IcisXDUugtBgdUqCg7jtsYBxe36lt1MLAG6ZFPm2_4lH3ySAe1PfKIecgPgIsxuoAk1iYBI6p_YDsVRwuAnhE_eubD1XsuP55jmr4alE_lkXeaMAktFpSy6ZN75kFV1BN-tMrEXkvYU9WvkHyUhqvyiTF-0ymMyolg3Lwr3ddD8-3WdGwpsTZeNHLnU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eINj0xSZwPGihZ2HtoNJ3qYygwEySUGciGGb_aNiUpgnT6MUObWymguyFxjhwC_Ud52WRnFMSwvOcscDf0lEcMo3AxgGQZJTC6A58TjhOUpLSOWJKhUZbMlV14efZ6GMlGPPpdI-vAN803Z88CCaBxIAirRtvZVCRoILy4hd0CnAO0wg5JeTw2wmyswYONyca004D11UFrYeN4Qw9tg3VBf78EHcgbfWvn32c-K_7rjsN3cxVOBu8md5gmZLcyWOyRUIc92kcuHjnS4iG70bSTaK4fnmX7uOUxA6t5N15GeMiRa2yMZY6tAx3xDnwf3xFCSW305cg-16pJ9SvtVc-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chBMxe74YWeZqQ4gbALDhIt9LsLq9GECYSZCnZmJ0mnL1Y1YqGeoPxS1j-oL7MNgeq3Ozwwo68dPXqVEpqVUnsrC6Z_33fEZvHmaU0SRBa0PXQI3pVwEMHiuVTPscEdPAG09m2nAc4UqxDWlQbiabAU0Bb1ruBOH1zjD8cy1_NF0fEARJP8cwDwuHZkEYULamDBUaLJ4NZ-esBRxL0gFDroKqARX5_8ogL0PPk9KnbItjPNK2M0iyJuMH7Z-Yqi4QKRVuTTHxrOriB5Om-o5gBKbyMkVFzlKQlRo3MNPEw4qhl2MjRDVgYrXXp3gBRvV1ptxqeYtS4RrCNJr5U_dPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzPne0ddY7scYGHXasffz8Qt4W1D4VGJnITdycLj9BzE5n13JW_phwxHe__PHj-cPRDlk_a3TBrdWFy5vnLHsVTboAtDURCw9CTmewMWoTjBFVxHUokoq3QXtAd0ZnrM474gUoT6lpr-lrpgwlbuTKbYRrPkfCNS6U0n-ca55dWXPcud6j5bNwYGK_FZAMlH1J2yDyIyv9VMAqM1pnmYT-wFSy8FhXbaG0NvFIj6gg08lQW7Rd3cV1WS7go-5pySv_cJ31jpGLIFuKv1dpOlLXSpgBT2LwC4dkI8fU8r_LhL8Y2I_o-MVrrr7shJIyGZCVEbg4mgqGiNR1agFALu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipl4b3pnSJk7FeZC0UpSHg099cfTX4wUReXJE6AmEmlc8qv1tW5MgD_B-9nSuvNtR046p5mUnZNr97xgngUMI5W22VJIZguqnngEsWQNOHi4K8RAfLQPDVx-reUVglGYywKHPrMAPKLsLsdZll3td6h7zBnpe2PrWrfaPq8wz1zBblWWu-ZYXBI-kcuskgAQmFaPhYwRcoS-cwTMkPTNSDxyqO_p0llWiLvws5XiNXB4Uo-R8lDAehEuXOWUnj96_wY_cGOfJIArCnY6t_8QWgdBmid-9bodjo1NkzwZVzO2p4y0hYrJ_t_rt_2GS_LnngaiYUELT0O4j4a0c75muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tECsfk3oGeaVzAHbCcUvOkajd9EbMwZ4hhl4xkq9MWVkM8DFEZS4CEyoS2hc19b5Kw9_hPmHAOUWUoO2bd_1okOAWN1JfR_K2Cw9h1zOT5DZrXFJ31BvC4nlxCBHu9rEX2cb9wrRxWcPs3nKH_hgetWByT8pq6me0KhzoLR4Mza0wy9Yj8DWONENSWhXUtzbTz565eTwZmAAIN-SCw4M1vaFaYSFVTnUt3XwQcAIbex7ErNnxOyDWitbKEkpld4Ab1yGa_TE42KbAVICo6f-QeGsg9yauAQNW1ZIjr9ftSDyCM9KlqDah0d1vmdlbW2GREOaCMlPNVJDKEYDbud8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvskoriLD5OHnjScGrjnfV4p042Nt-1j3ke65Paz_aRHX42p_Dtmz_T55E8Pv7TVuGfBJPPsO3sePjtyQSb07u4MAw3X2A2bFMXrZ0USZLNzpMpAfuwj3Q6BruuxvPj_GJagyrBmh9xrr--nZA8uswFSeoFft6oemXq_0iJtmkbJ1m-HeibypHScO2xPiCaeYF470-Yr3iTKePBNfLJFJXPHc4akIIgZfzYcnZygZguxlQIG1sUPtGsaEO0ApcM4ZlMDg_Pdpk6ly1gGcv0q0Na-t0iTS9fJj0qawAnBsU6aCGgcT3U229VIjFsD44UgqNm5OvYsSOohWhsxc8VKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZ9Uo-E_j8IpfZcRxeHgAvpW0dddf6jVmUrvFdAPCBt0EVQz1C50nz8BsVtY9lF9nO75AKzNSq1w_pqaTdbwnh3SinH_s9GGqN0ggdaYg9V2ToOy8DWugqd_ThrYnaJyIm4pogUuP_dlFrJ3Qre2Zy_yb5JmaclBhmgSaL-VE-YvezMQlve7Yc5NdhF98V_33Qbyt7QIdoXJZwDrdGcicRDfr66f0uu429bHtZOYhSrehRobhrK6PKN5pIG7DIFa8iWF2GFAoKseSi7FlWPCGo-N5_-UGnB9gYtvoxDxGGdVWhS_H1LE1F-Rcx4R7kKjLWge7HOmEluubinLgopLgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/459609" target="_blank">📅 04:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459608">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">منابع عراقی از شنیده شدن صدای انفجار در سلیمانیۀ عراق گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/459608" target="_blank">📅 04:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459607">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پزشکیان عازم قرقیزستان شد
🔹
رئیس‌جمهور به منظور شرکت در اجلاس سازمان همکاری شانگهای، عازم بیشکک پایتخت قرقیزستان شد. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/459607" target="_blank">📅 04:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459606">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016f993372.mp4?token=O4iqW0igvireMMWCXThN6x5AZ8yRJpUm4A1fpyPGJwmjDr4wECn_Pa-C_it_sKE06BHWcXETKJM6ab35or7NVXPOujPiIUCD0MuIMHly5ELAloW6bVUzaE1cymv3yscCMMcdlI8vESKX6l8IsPIyhSiym_us-9q6s4GqUqVjjtUV24EiBd4_zx_JHqjV0HlHqktm_AbKGKZK8TApbCU4vplL1UltmNeXZRSAzYdlYyXBc2bSQz_14v-hL66XWqjs5TC4VFBz_Z-SNjav4-7xVHI_QHMcbfTsfpvj9Yo5fZnUGpYzDLXFo536vPcgbFHHsDpmUy3d-05a0c4xnXlJQkghz6h9-OukmqNZYzbeIeqoqLN_w8jA_38c95qY9nuPCG2PMem8gaa-QxtlN2tXFkYjIKVZl0GRV7-jXHQ0mKVGuPhG8yG5u8l0ifXn0LrjXiMbJbpYNyHnayMCT7kGw4Wlh0lVFHvszERToVTnyAAyb1TOEPVk8Mr-feRYWEurVXHW-q8t5zYfAg3nkCE359xdx5xoNcBvU9DVf0trzJsJnt7octTLhiThRKDE5bS7s3Jrk3yqrm8xn6bk02XQMALSnPV9uDPx8-Z7QIP0LUd_a6SGbtUCPasXEyUt4_GhNsFegjdVx6bfeRQST0toSAKLhz3npR_I3RUbFCZ-p9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016f993372.mp4?token=O4iqW0igvireMMWCXThN6x5AZ8yRJpUm4A1fpyPGJwmjDr4wECn_Pa-C_it_sKE06BHWcXETKJM6ab35or7NVXPOujPiIUCD0MuIMHly5ELAloW6bVUzaE1cymv3yscCMMcdlI8vESKX6l8IsPIyhSiym_us-9q6s4GqUqVjjtUV24EiBd4_zx_JHqjV0HlHqktm_AbKGKZK8TApbCU4vplL1UltmNeXZRSAzYdlYyXBc2bSQz_14v-hL66XWqjs5TC4VFBz_Z-SNjav4-7xVHI_QHMcbfTsfpvj9Yo5fZnUGpYzDLXFo536vPcgbFHHsDpmUy3d-05a0c4xnXlJQkghz6h9-OukmqNZYzbeIeqoqLN_w8jA_38c95qY9nuPCG2PMem8gaa-QxtlN2tXFkYjIKVZl0GRV7-jXHQ0mKVGuPhG8yG5u8l0ifXn0LrjXiMbJbpYNyHnayMCT7kGw4Wlh0lVFHvszERToVTnyAAyb1TOEPVk8Mr-feRYWEurVXHW-q8t5zYfAg3nkCE359xdx5xoNcBvU9DVf0trzJsJnt7octTLhiThRKDE5bS7s3Jrk3yqrm8xn6bk02XQMALSnPV9uDPx8-Z7QIP0LUd_a6SGbtUCPasXEyUt4_GhNsFegjdVx6bfeRQST0toSAKLhz3npR_I3RUbFCZ-p9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار سخنگوی قرارگاه مرکزی خاتم‌الانبیا: اگر با ارتش آمریکا همکاری کنید باید منتظر عواقب خطرناکش باشید
🔹
نیروهای مسلح جمهوری اسلامی ایران در پاسخ به شرارت‌ها و اقدامات تروریستی، با سرعت و پرقدرت پایگاه‌های آمریکای جنایتکار را در منطقه مورد هجوم مقتدرانۀ موشکی و پهپادی قرار دادند و در هم کوبیدند که ضمن خسارات سنگین به زیرساخت‌ها، تاسیسات، تسلیحات و تجهیزات تعداد قابل‌توجهی از فرماندهان و سربازان آمریکایی کشته یا مجروح شدند.
🔹
این عملیات تهاجمی به‌صورت درس‌آموز علیه آمریکایی ها تا پشیمانی آن‌ها از جنایت ادامه خواهد داشت.
🔹
هشدار می‌دهیم تداوم شرارت آمریکایی‌ها در منطقه با پاسخ‌های سنگین‌تر، گسترده‌تر و ویرانگر روبه‌رو می‌گردد و هر کشوری با ارتش متجاوز آمریکا همکاری نماید بایستی عواقب خطرناک آن را بپذیرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/459606" target="_blank">📅 03:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459605">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">برخی منابع عربی از شنیده‌شدن صدای انفجار از پایگاه‌های آمریکایی در اردن خبر می‌دهند
.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/459605" target="_blank">📅 03:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459604">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5589409306.mp4?token=t3GkfvjnSPeTKBOQ2wm0s70y9B-cASlWBo_yNdYhAndjrEMN1GcoQDF1Xnc5jQyDNSJ_R4PdyIgDRgJ63r1aUIsBDyLdgjTvECrZ3a-ec5eA0oBq84I3V3MIL0uD_iaJKotRX2mDWsxsuVzy4FqAdBu6446Je0R1WfL0wHZ0WgRBVk28NyE3epPZfh0NmOGM4exMqbkO6BlFVc3WdSSFupIzHxv-xRYEtle2lyMUNZJXfJjXUa_3JkiwT_j-XrCmORDkKpVaUMPatumPJtiKjGNJgNtgCcMWrfhoItwrH-IhhszvQvz00l3VQIu81DPpESz4tTbCuPzwxV0zlgpH4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5589409306.mp4?token=t3GkfvjnSPeTKBOQ2wm0s70y9B-cASlWBo_yNdYhAndjrEMN1GcoQDF1Xnc5jQyDNSJ_R4PdyIgDRgJ63r1aUIsBDyLdgjTvECrZ3a-ec5eA0oBq84I3V3MIL0uD_iaJKotRX2mDWsxsuVzy4FqAdBu6446Je0R1WfL0wHZ0WgRBVk28NyE3epPZfh0NmOGM4exMqbkO6BlFVc3WdSSFupIzHxv-xRYEtle2lyMUNZJXfJjXUa_3JkiwT_j-XrCmORDkKpVaUMPatumPJtiKjGNJgNtgCcMWrfhoItwrH-IhhszvQvz00l3VQIu81DPpESz4tTbCuPzwxV0zlgpH4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر بیشتری از جنایت آمریکا در حمله به مراسم عروسی
◾️
ساعاتی پیش محل برگزاری مراسم عروسی در کوهستک سیریک مورد حملۀ دشمن آمریکایی قرار گرفت که تاکنون ۵ شهید و ۶۸ مجروح درپی داشته است.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/459604" target="_blank">📅 03:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459603">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
سپاه: حملۀ سنگین موشک‌های بالستیک به آشیانۀ هواپیماهای بدون سرنشین در اردن؛ تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمۀ فنی پروازی به هلاکت رسیدند
🔹
روابط‌عمومی سپاه: رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/459603" target="_blank">📅 03:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459602">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌ انفجارهای مهیب بحرین را لرزاند
🔹
منابع محلی گزارش دادند که پایگاه‌ها و منافع آمریکا در بحرین هدف حملات موشکی و پهپادی گستردۀ ایران قرار گرفته‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/459602" target="_blank">📅 02:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459601">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزارت کشور بحرین با صدور هشداری از شهروندان خود خواست به نزدیک‌ترین پناهگاه یا مکان امن پناه ببرند. @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/459601" target="_blank">📅 02:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459600">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزارت کشور بحرین با صدور هشداری از شهروندان خود خواست به نزدیک‌ترین پناهگاه یا مکان امن پناه ببرند.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/459600" target="_blank">📅 02:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459599">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/404c7bc669.mp4?token=TUzaRIT7GfaBQ2O4KAgzTGuKTFPKVFdIWDB6znhpMXoawRDNCTAUYGEN6gaNHNakvL-VbbUZAiSyU0J-r5o9elhdq5MXVy2ojrdWhWtLd1PicATAGdLE3SyEHhHogxDopbOEze8axHfTBPs7U1EUcGXZu0abXZYWvERfOlaTFHhrOWNwcA0Q8ahaH1s3Tfr6k823Vy30FNiemiMUspVJaaPJ0XnSq94prerskDTNRb7a7AJDK7IVvvhopuDIorWoHXvQRDCKgzyrAYG4YB37aPYTUlCRB3xv2EQokQAIToO6KxYoIlyVYIuns6cczqpt1BpE36DtLz3f6ZmXHCyXHEuOaz3h3vBRdOJ4qM-YRJm_NxdcWEjWETqEe3bvwxZkujlMdNUnc-4viL6-83V4IIto3cGpLA3j1i82Jnm1Uq2cghq6r89A8WQEnaKd0drL4sbcBRvD7MGgFEpVtVlGzQsB88zblsVM8KFEdyqAVTuYhvKnp88mYg8G4fLlSSQVFjs_7o1QYA2dylYUiBiuRGi9qp4Ky7nRsf0unpDCNOp3ITHVYO4cxx3ByhC8h6kGVN9wv-lLaIh-aYQC9hWck7doWCepsRGB-SGCsEgakQyRfkiH3TxMIpkS8nXS9TDl42N0HDPWWYCVSZ20Wtf0DxhqUSwiiSownjUtnOiZgiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/404c7bc669.mp4?token=TUzaRIT7GfaBQ2O4KAgzTGuKTFPKVFdIWDB6znhpMXoawRDNCTAUYGEN6gaNHNakvL-VbbUZAiSyU0J-r5o9elhdq5MXVy2ojrdWhWtLd1PicATAGdLE3SyEHhHogxDopbOEze8axHfTBPs7U1EUcGXZu0abXZYWvERfOlaTFHhrOWNwcA0Q8ahaH1s3Tfr6k823Vy30FNiemiMUspVJaaPJ0XnSq94prerskDTNRb7a7AJDK7IVvvhopuDIorWoHXvQRDCKgzyrAYG4YB37aPYTUlCRB3xv2EQokQAIToO6KxYoIlyVYIuns6cczqpt1BpE36DtLz3f6ZmXHCyXHEuOaz3h3vBRdOJ4qM-YRJm_NxdcWEjWETqEe3bvwxZkujlMdNUnc-4viL6-83V4IIto3cGpLA3j1i82Jnm1Uq2cghq6r89A8WQEnaKd0drL4sbcBRvD7MGgFEpVtVlGzQsB88zblsVM8KFEdyqAVTuYhvKnp88mYg8G4fLlSSQVFjs_7o1QYA2dylYUiBiuRGi9qp4Ky7nRsf0unpDCNOp3ITHVYO4cxx3ByhC8h6kGVN9wv-lLaIh-aYQC9hWck7doWCepsRGB-SGCsEgakQyRfkiH3TxMIpkS8nXS9TDl42N0HDPWWYCVSZ20Wtf0DxhqUSwiiSownjUtnOiZgiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: حملۀ سنگین موشک‌های بالستیک به آشیانۀ هواپیماهای بدون سرنشین در اردن؛ تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمۀ فنی پروازی به هلاکت رسیدند
🔹
روابط‌عمومی سپاه: رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/459599" target="_blank">📅 02:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459598">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/459598" target="_blank">📅 02:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459597">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f143426d42.mp4?token=vhaPUrSG_6svMm4LDfE9GYASSATcYT1PmGMIxL5TiiyBDMXJ_MRUitxDNF8MMKcAHm4XE8JZg8AqTzLrMm3CQuYCxHrce7u1pWK113wcOIIT0QR7i6eHgN4tGsHx5Muvoy6TXt5FzuEJO-8GHT_QdrBWeF2URkNQWealf-KPDA9R7uIoqMKHofOD3U_3T1Oeg09Pl4jfadM0cQcRmF80kJhK3UgVmEDaojTqI9R58VQcWZOUiYnrWdm-qc7Wi_Fvk1L0Nim7d_u2RSD3trlI_Wxjkxr9rjhK13PSeRtPCePMk7D52PBg4RjBvEHackmW35S0M8ZIdvGOoE7zXvzRnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f143426d42.mp4?token=vhaPUrSG_6svMm4LDfE9GYASSATcYT1PmGMIxL5TiiyBDMXJ_MRUitxDNF8MMKcAHm4XE8JZg8AqTzLrMm3CQuYCxHrce7u1pWK113wcOIIT0QR7i6eHgN4tGsHx5Muvoy6TXt5FzuEJO-8GHT_QdrBWeF2URkNQWealf-KPDA9R7uIoqMKHofOD3U_3T1Oeg09Pl4jfadM0cQcRmF80kJhK3UgVmEDaojTqI9R58VQcWZOUiYnrWdm-qc7Wi_Fvk1L0Nim7d_u2RSD3trlI_Wxjkxr9rjhK13PSeRtPCePMk7D52PBg4RjBvEHackmW35S0M8ZIdvGOoE7zXvzRnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شاهد عینی از لحظۀ حمله به جشن عروسی در کوهستک سیریک   @Farsna - Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/459597" target="_blank">📅 02:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuMprmcBrmuJz4p5AO_LXhKXdchCJ4FY4qa1rWuf3wG2Viryzf-anaUXCFod-ZOae6_y2BlhcUUvQ8FUWIqd62Hid1E8oHPIlfrMsSoOdo4LB6FXzZMLXjbhZ0ZTJPQ85y0QxvvdsVWDysd9hybeawf3oqhTrcfh_6xg_5CqTiKAwm1UY7u2NyadzJb3F13V3amkeB38zbXRa0yuLKCyxEuM9hAIAGRKQUp_k96uHaoz2guwEz5K3apnphhEpi_W1WdfiyLH60Tmjau1idCaMQwdyJIAvzCkbvMB3zbdeKr3-oDliJb4NJrx2-X8t4Q6HXPeOD_dAE5TvPox4iit5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی سپاه خطاب به کشورهای منطقه: یا آمریکا را بیرون کنید یا پاسخ کوبنده بگیرید
🔹
سردار جوانی خطاب به کشورهای عربی: بهتر است آمریکایی‌ها را از کشورهای خود بیرون کنید و پایگاه‌ها را پس بگیرید.
🔹
در غیر اینصورت، نیروهای مسلح ایران ثابت کرده‌اند از هر نقطه‌ای در کویت، بحرین، اردن یا هر کشوری که به ایران تهاجم شود، با پاسخ‌های قاطع و کوبنده مواجه خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/459596" target="_blank">📅 02:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
منابع عراقی از وقوع انفجار در مواضع آمریکایی‌ها در اربیل خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/459595" target="_blank">📅 01:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459593">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5PbBo8C4chXRviYGG6JcNzGS6BU2zutGlWY8EBzG9Wnlf2xNusVbCxNXzIx3BNlft-FTUtAmwb2SKg7y-4JPgt-Uw0LoRt_ZMTCX02VXc8xNWn1zGZqQOpY57ruOOTYPeZxYu905G_aI447MewRRc_RlCzJtyXzQ6dXh4HQNS0NHT5GgTjEZaddzmHFI1vicdlOydDPt3d3KWBHMqq8EIzMX3uyr2mf7LZzR8BvDt-Ijb1WTbX7HqUhK-kEL8Jv3Niu-Zm6-RtOUyOmCurLD6K6c4Z7OUyYQ-KFiOIhF-iYcyYklPzjmmtJo50PwbKXqArxF-qfRuvyV9KvT8EbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخابرات هرمزگان: در حال رفع اختلالات ناشی از حملۀ دشمن هستیم
🔹
اداره‌کل مخابرات استان هرمزگان: در جریان حملات آمریکا به مناطق غیرنظامی و زیرساخت‌های خدماتی در بخش‌هایی از مناطق جنوبی کشور، به تعدادی از دکل‌ها و سایت‌های مخابراتی و اینترنتی خسارات جدی وارد شد.
🔹
عملیات تیم‌های اضطراری برای رفع مشکلات پیش آمده و وصل مجدد شبکۀ مخابرات و اینترنت درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/459593" target="_blank">📅 01:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459592">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
منابع عراقی از وقوع انفجار در مواضع آمریکایی‌ها در اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/459592" target="_blank">📅 01:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459591">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7sGQu5_erQkkVD1x9lrayAiQQZZYGRJ8hevTedudG9VFGV2WIPhxQFhp_MxYN5fQ0Ews9EF0kpLQoMcopwUJcHm9G7U6NYhMofswtL0SRxgAEKu7303XjfmJ-FVJx5t9Dl2-V97rkl5Qj1BWGJM54tqaPWzywUL2E130AdXhBCg2ZP1l8EReXOX6oYZFF_rCvxmiVfyQgsxqsryZd5dTkvp0PbwttJo4UdbXnDHokii1HrKTdUKFlXllGHlUOqcqRtFHaEMBdSq5exMs2ITILUo_u3CpEB9IYQJdjBHjR7s-jPSFcMZ1Zcit12P5k98hCEirikQ8Y1Gn4fQZnD-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش بقائی به حملۀ آمریکا به جشن عروسی: هر روز بر سیاهۀ جنایات آمریکا علیه مردم ایران افزوده می‌شود
🔹
سخنگوی وزارت خارجه: فهرست جنایات آمریکا علیه ملت ایران اکنون کامل‌تر از همیشه شد. امشب یک منزل مسکونی در کوهستکِ سیریک، در حالی هدف حمله قرار گرفت که مردم در آن مشغول برگزاری جشن عروسی بودند. بیش از ۵۰ زن، مرد و کودک بی‌گناه شهید و مجروح شدند.
🔹
این قساوت را نمی‌توان از زنجیرۀ حملاتی که پیش از آن در میناب، لامرد، قشم و دیگر نقاط رخ داده است، جدا کرد؛ همان‌طور که نمی‌توان آن را از حمله به اهداف نظامی جدا دانست؛ حملاتی که با برچسب‌ها و توجیهات فریبنده پوشانده شدند.
🔹
خطرناک‌تر از خودِ بمب، عادی‌شدن بمباران است؛ و خطرناک‌تر از سکوت، آن است که سکوت به معنای مشروعیت تعبیر شود.
🔹
ایران به این جنایات وحشیانه قاطعانه پاسخ خواهد داد. اما دولت‌ها و سازمان‌های بین‌المللی که در برابر چنین بربریتی سکوت می‌کنند یا در پی توجیه آن هستند، باید بدانند که سکوتشان بی‌طرفی نیست. وقتی حملات غیرقانونی و جنایات آشکار، به اقتضای مصلحت سیاسی، تطهیر و توجیه می‌شوند، مرز میان محکوم‌کردن جنایت و عادی‌سازی آن از میان می‌رود.
🔹
کسانی که امروز سکوت می‌کنند، فردا خود نیز از پیامدهای این سکوت در امان نخواهند بود، چراکه چشم‌پوشی نسبت به ظلم و جنایت آن را مهار نمی‌کند، بلکه مرتکبان را در ادامۀ جنایاتشان علیه همه جسورتر می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/459591" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459590">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
برخی منابع عربی از شنیده‌شدن صدای انفجار و فعال‌شدن پدافند هوایی در کویت خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/459590" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
برخی منابع عربی از شنیده‌شدن صدای انفجار و فعال‌شدن پدافند هوایی در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/459589" target="_blank">📅 01:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9849737611.mp4?token=QOt8jiRJ-zvAYzsfPZtAQI5-Nbrjfx_BaVWoo2S5osuwIa2iH-1nqpt04v-X5YxnEiXq37Ui_lbxUIFONyQvry2g9vadKGz1CzVbzKTPNoicgzmVzs8hSzx6Q1O3sc3jBIKkF-S7RedcRxZ7gN2bNRokjgAcaq5Clz5Ghi4n2lR262N7oOavkPVOyt0l4K2V3HguJyzYhJ6um5VuP0mIYoaMRJqjeuwRT9stsMje_YwHvfMCLtgaNqz8ZHaHX78vhksyYKyJZzfRZttK-UyKJaqB68zPRXHtXvoicys76zpWDrYLMZ_NwmxzRx94_G99evFbfjQKkC71QcM-Tw-nTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9849737611.mp4?token=QOt8jiRJ-zvAYzsfPZtAQI5-Nbrjfx_BaVWoo2S5osuwIa2iH-1nqpt04v-X5YxnEiXq37Ui_lbxUIFONyQvry2g9vadKGz1CzVbzKTPNoicgzmVzs8hSzx6Q1O3sc3jBIKkF-S7RedcRxZ7gN2bNRokjgAcaq5Clz5Ghi4n2lR262N7oOavkPVOyt0l4K2V3HguJyzYhJ6um5VuP0mIYoaMRJqjeuwRT9stsMje_YwHvfMCLtgaNqz8ZHaHX78vhksyYKyJZzfRZttK-UyKJaqB68zPRXHtXvoicys76zpWDrYLMZ_NwmxzRx94_G99evFbfjQKkC71QcM-Tw-nTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ اولیۀ حملۀ دشمن آمریکایی به محل برگزاری مراسم عروسی در بندر کوهستک سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/459588" target="_blank">📅 01:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459587">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3969eedd.mp4?token=urxPRzo8G7jRK20Aegf0Pm16teTD0V16-y0yOcb-tNZglFCRaOYFJAwlNNgNOjMxECCI9UVGcyiKe6vzi7Ided4iowpsdJoRD6gvGT6RqQh1eUQgLBuMmo3ZC0utEO65OVXn0QfDlU5IZJ62w1OergxWvB8Ec0Bnu7uwp0SvDPLT2GulDdRaAwD4CxafDtS8aa1xkSFViUAvdSJu0gIy7D2zHZUNUa9WHDLGjeNfoGJcjIVyAEQDwxb0SwI1p8BpJ6qrNnVHj0j_f-FwGNHWGkzZO5ccoqJExV-hWXKyx_sup0-Xkghb0JHIt9htCeRHRECwSP8a2sK2PeDe6vpAHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3969eedd.mp4?token=urxPRzo8G7jRK20Aegf0Pm16teTD0V16-y0yOcb-tNZglFCRaOYFJAwlNNgNOjMxECCI9UVGcyiKe6vzi7Ided4iowpsdJoRD6gvGT6RqQh1eUQgLBuMmo3ZC0utEO65OVXn0QfDlU5IZJ62w1OergxWvB8Ec0Bnu7uwp0SvDPLT2GulDdRaAwD4CxafDtS8aa1xkSFViUAvdSJu0gIy7D2zHZUNUa9WHDLGjeNfoGJcjIVyAEQDwxb0SwI1p8BpJ6qrNnVHj0j_f-FwGNHWGkzZO5ccoqJExV-hWXKyx_sup0-Xkghb0JHIt9htCeRHRECwSP8a2sK2PeDe6vpAHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌شمار مجروحان حمله به عروسی در کوهستک به ۶۸ نفر رسید
🔹
بنابر اعلام هلال‌احمر، شمار مجروحان حملۀ دشمن آمریکایی به مراسم عروسی در کوهستک سیریک به ۶۸ نفر رسید.
🔹
شمار زیادی از مصدومان کودک هستند که به بیمارستان‌های سیریک و میناب منتقل شده‌اند.
◾️
همچنین تاکنون…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/459587" target="_blank">📅 01:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459586">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI-U3s7BiQA_GyiUN-SkQhPrrHilQNC6QXOtrSAhI2oSXmIDplHH5S2M9ZDavgWeEn8fpfyzr-NzX6gMpoBosBoM95YLVK0W6EYGkzNeb_geKSg7u7S1btuOmWDGlE2MIFCv-vS0OCoiIodbbCKCtxASvqlFlB3Q840TVoZIgkDh-sPGK0jqoyIk0gWJrQIzEYRqpEGsIWOeyg5xDZH_uSWeYPicnQLShsOhSzI23o-SaQh4QdNc8SugPBFVmhVgg2VmvO7BlEoS8mDUJuBPE0CctvVMWwbaOXgpaYD0simYerlvTrzHozlsvZDZX2YwTsqsuBAg34ru0W3m_AFiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت ملی: هدف قراردادن یک عروسی و قتل‌عام مردم بی‌گناه در کوهستک، گواه نهایی استیصال مطلق مدافعان دروغین حقوق‌بشر و تکرار جنایات آن‌ها در میناب و لامرد است.
🔹
این جنایات بدون مجازات نخواهند ماند. هیچ‌چیز آن‌ها را از ارادۀ کوبندۀ نیروهای مسلح ایران محافظت نخواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/459586" target="_blank">📅 01:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459584">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk99dBMYXzve1hT4bTH676PGERmjHebB2xin3myBvtyTP4E-GW0KwRFncoAUuLAQokc4nvJUNchbz9sIxIkSS4Hr-UO3zk64_7pcxhwCT6sLe1sBPwv4zmBJB-asFcsH_TAQkYvst48UuhkahsEifYyx72GVTN8DbnFhTSxIlc80x4Wy8HA-NMtjB_HWndecv-E0rL6XadRhKeofrHECu9rHidia6KZXMMVWmEr7N-TBM5ml_SRUblU6_8M3vUZqXgb02Ufqf65awQncoW7JviuZTw6yF4Tt5etgvulJbxDnrxIZYw6VzPuag2sSCmdIzErl3pxdld-ORK6_1BPhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-Hns17GPu2EmA7SIs11Spp5yppsRtr3E_dTiecDjjR1S1lZ5k-LnRddVYgsNe6CM6kkUmpVcZ8lZXUUB9WkZoHa5yWls4l16WMbpECPsUil9xBxVzfexnmdAJBl10PVH9vge9WGZkRrl1Yfje0aPi7EweifHr6_93N_Nvm3E0pLiigrMN6O-NOIU79Tcx1cT1TosjD9H5dSMZDYYbtTImqHMYbtnTdj1mpPaUuPz7PsXnVg7PBrkd7l9-hynpcMhKA47soOcVJLhjUQPyzjJqTwcLVuh6q5UZMrU3HSd6cuQXCTgyHsCSOZEjLYjcp9Vl436JOpB_df43Lo8Bu-fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ شمار شهدای حمله به عروسی در سیریک به ۵ نفر رسید
🔹
هلال‌احمر: شمار شهدای حملۀ دشمن آمریکایی به مراسم عروسی در کوهستک سیریک به ۵ نفر رسید و ۵۰ نفر مجروح شده‌اند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/459584" target="_blank">📅 01:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459583">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برق مناطق آسیب‌دیدۀ قشم وصل شد
🔹
فرماندار قشم از رفع قطعی برق در مناطقی از این شهرستان که در پی حملات شامگاه سه‌شنبه آمریکا دچار خاموشی شده بود، خبر داد و گفت جریان برق اکنون در تمامی نقاط قشم برقرار و پایدار است.
🔹
همچنین عوامل شرکت توزیع برق هرمزگان نیز در تلاش برای وصل کردن برق مناطق مورد حمله در کوهستک سیریک هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/459583" target="_blank">📅 01:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459582">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0635efc59d.mp4?token=eV7VpLejfnDu5uWbbFbZU2x2MZ3IH95acvuA01Hbaoj3AIUJSl9MxvGVCaNpfdPpT2Ok2B0u2-wNwJb-pgbMxMWeZSBf4D-dOli8ES8Ypx1cirfGhR-M2Q0shixkoXnFm7Kzc5nA74-5CTGywu0abNvL95VuoMbQqk5prCMZudpTRYLPhaEBtbazsF9xVx9tD-D3gIr5RaTlvBZsZyTeAW_oufWChWlCFgdChQ939F-8amvtJK0YIj7bRkgRAGUzkrUBXM-lh6Z1_XZgD_0QLX5duotFZ0GXy0q98wZkhXqwhp18CPZoMyWk5X2KAExP4UxkuZo1PZlI1Mww-MkyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0635efc59d.mp4?token=eV7VpLejfnDu5uWbbFbZU2x2MZ3IH95acvuA01Hbaoj3AIUJSl9MxvGVCaNpfdPpT2Ok2B0u2-wNwJb-pgbMxMWeZSBf4D-dOli8ES8Ypx1cirfGhR-M2Q0shixkoXnFm7Kzc5nA74-5CTGywu0abNvL95VuoMbQqk5prCMZudpTRYLPhaEBtbazsF9xVx9tD-D3gIr5RaTlvBZsZyTeAW_oufWChWlCFgdChQ939F-8amvtJK0YIj7bRkgRAGUzkrUBXM-lh6Z1_XZgD_0QLX5duotFZ0GXy0q98wZkhXqwhp18CPZoMyWk5X2KAExP4UxkuZo1PZlI1Mww-MkyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ اصابت موشک به اهداف آمریکایی در اردن  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/459582" target="_blank">📅 01:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459581">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۴ فوتی و ۱۰ مصدوم در حادثۀ برخورد خودرو با تجمع‌کنندگان در مشهد
🔹
ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد مشهد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و بیش از ۱۰ نفر زخمی شدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/459581" target="_blank">📅 01:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459580">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93e2b5cb22.mp4?token=VR74fYM4HtbCaEhw859FeHnewlMHU4eoJpcAfmm1dZ_dHrCfK5Z9B4KagWoLkZ4KNrWZ4BWElNFXG2J-QoK0hpOVYfMjLlzFHKeoBDzELiv2ukgHpn2mPJ3CXeyaoK_brGfymfzDuRXty7ZVbIj-9DhV5xiBcgb27l0Cvw5PTg7OcnXdCMZyNccMTuBPHQuINNcaNsmtrR5O4Wm9R38II1FDeEGXLHPKpQVy7iZ_M6DIHjAOyrOvudJii1ztBDgUNEngyv7GBZVjp4x5isnXqOkM8nn3epM9dAnn9CteIPKE6LAsgAXRqqy990NtorGkzJIVKkazzxuZCVsLZc3kzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93e2b5cb22.mp4?token=VR74fYM4HtbCaEhw859FeHnewlMHU4eoJpcAfmm1dZ_dHrCfK5Z9B4KagWoLkZ4KNrWZ4BWElNFXG2J-QoK0hpOVYfMjLlzFHKeoBDzELiv2ukgHpn2mPJ3CXeyaoK_brGfymfzDuRXty7ZVbIj-9DhV5xiBcgb27l0Cvw5PTg7OcnXdCMZyNccMTuBPHQuINNcaNsmtrR5O4Wm9R38II1FDeEGXLHPKpQVy7iZ_M6DIHjAOyrOvudJii1ztBDgUNEngyv7GBZVjp4x5isnXqOkM8nn3epM9dAnn9CteIPKE6LAsgAXRqqy990NtorGkzJIVKkazzxuZCVsLZc3kzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملات پهپادی ارتش به پایگاه‌ آمریکا در بحرین
🔹
روابط‌عمومی ارتش: در بیست‌ونهمین مرحله از عملیات صاعقه و در پاسخ به تجاوز دشمن به مناطق جنوبی کشور، ساعاتی پیش ارتش جمهوری اسلامی ایران، تاسیسات راداری و مراکز تجمع نیروهای تروریست آمریکایی در پایگاه شیخ عیسی بحرین را هدف حملات پر حجم پهپادهای انهدامی قرار داد.
🔹
پایگاه شیخ عیسی بحرین، یکی از مهم‌ترین و حساس‌ترین پایگاه های آمریکا در منطقه خلیج فارس و از مراکز مهم تعمیر و نگهداری بالگردها و قطعات پهپادها و میزبان هواپیماهای شناسایی است.
🔹
رزمندگان ارتش جمهوری اسلامی ایران، به شرارت‌های دشمن، پاسخ کوبنده و گسترده داده و انتقامی سخت و پشیمان کننده از متجاوزان خواهند گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/459580" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459579">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
مجروحیت کودکان در حملۀ آمریکا به جشن عروسی در کوهستک
🔹
بیش از ۱۵ کودک حاضر در عروسی کوهستک سیریک در جریان حملۀ آمریکا به این شهر مجروح شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/459579" target="_blank">📅 00:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459578">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شایعۀ حمله به کرمانشاه تکذیب شد
🔹
معاون استانداری کرمانشاه با رد شایعات مطرح‌شده گفت هیچ نقطه‌ای از استان کرمانشاه مورد اصابت دشمن قرار نگرفته و وضعیت در استان کاملاً عادی و تحت کنترل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/459578" target="_blank">📅 00:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459577">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a48d0c20.mp4?token=epBb4Kyh2UsTtaAUM31-VH2Rh6CRh4q_moGFxL6ZF2G9VSLbZIAv_pCSmVm_OUyYj8MXueVoLMgsedcCxDRetB0rK6nc90epECLalDLQVvK9RNmWLf0P45mx1nEW4MuO5z4hV9phOy01fResLfN2p7jRrD8lQLyG-6twK9lUggWpXeL-UgEs9TiDucR_VXkbdaNsPcPe-CTqUYooD3bWwLNq9v4pJLMMKMi7eryZPGpQiJqom5g2UObuc8soHSoCZ7CcH4D-8bNckCr5bdKw3eJnB0tzyAQ8TT12PqH1oNa8SL7MAjtZlbDKqILR4Wets93eT61KXVNtLIV7CjzpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a48d0c20.mp4?token=epBb4Kyh2UsTtaAUM31-VH2Rh6CRh4q_moGFxL6ZF2G9VSLbZIAv_pCSmVm_OUyYj8MXueVoLMgsedcCxDRetB0rK6nc90epECLalDLQVvK9RNmWLf0P45mx1nEW4MuO5z4hV9phOy01fResLfN2p7jRrD8lQLyG-6twK9lUggWpXeL-UgEs9TiDucR_VXkbdaNsPcPe-CTqUYooD3bWwLNq9v4pJLMMKMi7eryZPGpQiJqom5g2UObuc8soHSoCZ7CcH4D-8bNckCr5bdKw3eJnB0tzyAQ8TT12PqH1oNa8SL7MAjtZlbDKqILR4Wets93eT61KXVNtLIV7CjzpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری از جنایت آمریکا در سیریک
◾️
ساعاتی پیش مراسم عروسی و دو دکل ارتباطی در کوهستک سیریک مورد حملۀ دشمن آمریکایی قرار گرفت که تاکنون ۴ شهید و ۵۰ مجروح داشته است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/459577" target="_blank">📅 00:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459576">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd0f4552b1.mp4?token=FvscptrOTlNv1G-i0n24BMYZvrhaJO0fmBGKK1C_wnPW3bD5_1MNAhSJxlyvdARtEZyknnHXTL6QlbO13WK2M8m8DmFTdTOF0tzqG-SbIh1IKdAdbdnusKKnJBK-k2ZR2CBPMDyuftE1CDqr87bcXPHb_3bHZu3kVPqr55L9EzHo3thJWs9rWw_2r19epbQ-I0uniUIBb4C3CEBiqqvmqhwYHaEqQGa77O0WaYVsYb7DJAVZejA4R3fUBy674CZt9Gk1lmZ4C2jgAqUb4dtiSitbFxbX_OU7tpqw9KW5yL9Y4NuSCNmxYZiEge4-4Jopx3DVESBUw82SKDVxF-Te_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd0f4552b1.mp4?token=FvscptrOTlNv1G-i0n24BMYZvrhaJO0fmBGKK1C_wnPW3bD5_1MNAhSJxlyvdARtEZyknnHXTL6QlbO13WK2M8m8DmFTdTOF0tzqG-SbIh1IKdAdbdnusKKnJBK-k2ZR2CBPMDyuftE1CDqr87bcXPHb_3bHZu3kVPqr55L9EzHo3thJWs9rWw_2r19epbQ-I0uniUIBb4C3CEBiqqvmqhwYHaEqQGa77O0WaYVsYb7DJAVZejA4R3fUBy674CZt9Gk1lmZ4C2jgAqUb4dtiSitbFxbX_OU7tpqw9KW5yL9Y4NuSCNmxYZiEge4-4Jopx3DVESBUw82SKDVxF-Te_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/459576" target="_blank">📅 00:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459575">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۴ فوتی و ۱۰ مصدوم در حادثۀ برخورد خودرو با تجمع‌کنندگان در مشهد
🔹
ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد مشهد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و بیش از ۱۰ نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/459575" target="_blank">📅 00:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459571">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_PW4mVC6m3ahKunGnus1L9rpYkeybq0gr3-Bl-qeam2Qj9k0S-G6A8OpaBH5SifUrPQhjltm16_Ys7TIZtthf1sBprH_4IQYMrXzeGmSXtIyq43BtUGX_uVTCbqc4DVkWoFkSblhuXlSsx1Seqmgokeitx6WQX-0v6tHIxs5xFS9M5Vj9Bz2NoFujjfcRpVaZBxl8Ad_vZmN1oc5kw-AW4bYA6ORys1uXqp6PapP3X-EK_g2kCWW2rTzWHCNjC25QjThdbRpqclO4vVupISagHQP2xq81uLT3QCltJkJgeXU0AbbA-Q8CNkeZz1sP52xVbjW5EyDfV40bp2OpIglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S37qn6SVsAMrjoZ4yonlD-8iALhbJiiV7QkiOZJREJgxnMxeJRTjOEiXXchFSntL3SDq82BeGGkv1RA0gKczgctPshIWkUODnw7Cy0cvIl3yULTTy2F4MTXs-9fQ-pfj1FCHSjzqPWNU_fIPra5o5v8NnxzeOPbXXvT0oqH1MGQVvA3OJbs4C4rORWIQd9trOPvp-OKxLJn8k8fXO8xFeqtuSmZ5uk7IjhnpTDXeGCU9DVTOMPTRAh5MKo1ukkblOOs09Vrx7f5Zbbl0aafXkzfXxXCVcvgAN-rmRbtOoHdoVd6KLDjTFXGspZ7CsEgVtsT7hINEjnEnN7HyrDu8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6-xIbTEdw9VLyx7rzqWTOjuL6SD363BaQ8Vyt1Kqaxwzy8phCRPl88EGQ567X2wDPFG0Pe5I3U0FvWcZtsYZNcFW5feVZX5y7hPBgJN6BRf2X5SNo4Rp1hfJQDVVeW_4cj8dNWu915QVInJmY109dCe3HfZ-I9TBKqBSB3zvLhXNvbq-e2BBmj5fAu7Z0BTeIfwz-cbOD6roMtQmLRKV2AXkWJQCHwPOb28OE2no0ULBXnaMXqMaTjLn2KZM6Uj4Mo1VBhCpVG0uzLoJROiLkx6d5QmBXB2NJvwszDN343EMrUi-FzPrBpn71GOVJkoCgwB2is5-AmsWkxDHnUhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSvH4GHANxufwKTLcIW3MaAhfF5LyoY7bYfWL2DlZI561ixRF338Qa1K5W8hA6jxpiJp6aR1yTK_LgQwArQVdBVQ8saRi0GsKhFMmWROnYhx8XbeLx3JQxgTuJvpgut6lwTIzDjWf1xJXqf9qjVVJBMlONG7oO1gj0M20H6FX4aptHsmQ6wO5F27WRe7Bf5sDUM2sJEDPw2n-cttBCdmFTReWmTomoDe9KlwIoV9mc_0SfHJov5azuU0mo3JH2dVciot3lTtxs5Yv7GrwybmZwBMkTY_LDcbvY44DmKPpRzGJRZJPR5DyeF2FUxmfq3y9M8F8aBNsDsudriaNBVPmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تصاویر دیگری از جنایت آمریکا در سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/459571" target="_blank">📅 00:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459569">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69d034784.mp4?token=KErlguA7UeE1i6NPo0LPFJu27xMA-J65d8ic16MBGx3hKGmZIbB9tWbRRikEAWvLbuFIJulwITsevNTBuDoiXgBo3by56lxSSJVr9J-oJ2HEx-evr7htvX2GFz2xHXdbmPlTqHCs8qaCOsHsYR-PMLFNoxy58bAoaDmPhx3etl1R5yIbw4s-jlUrVxOJmuUllcxgPSlk-Mpxoh6PZ98DBnkNWbuOATKeKllZm1Klo8s0NwpqzpVlU15fm7MdEGI8ZDBae69zuNBZB_eGHAYNtFzhIkSdpFt3oMl3taRq8i3HqEeiT0gOgpD7EZEHYtPQ4vz21lHzpFogL-mj2V3OFhDVCJzhbI6JeTVAiGV8rgIiYRkYtByG_-ystHVUdm-fUCN8fdVLYdTa50aCqmji-vq2cZJWXWp1MXHVuYyHi2ozgLB6DZWo6sAmLOT7R4lybep9n9EvoB1RX3vQKG-lRDAVfR6xCzGHEgkQCk7wj7j5Oj6gFWfMwYLcKu-8lqpgAj1YF8o3GOuUrVkkYJFA-yPgTOKtSlmkkpTkjzImifQAn0RQPTUeXG1YDQ3yqrH3wT0G1zv2UOn27AVlaO5sQgq-wQ7B9IlIL1G65ChO6Ff6qzpziOKFaVJyVkDTicsWty0oDZs46LgUcIUFWhEu9wN1680Rgxzj_-6zqu-1-Y4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69d034784.mp4?token=KErlguA7UeE1i6NPo0LPFJu27xMA-J65d8ic16MBGx3hKGmZIbB9tWbRRikEAWvLbuFIJulwITsevNTBuDoiXgBo3by56lxSSJVr9J-oJ2HEx-evr7htvX2GFz2xHXdbmPlTqHCs8qaCOsHsYR-PMLFNoxy58bAoaDmPhx3etl1R5yIbw4s-jlUrVxOJmuUllcxgPSlk-Mpxoh6PZ98DBnkNWbuOATKeKllZm1Klo8s0NwpqzpVlU15fm7MdEGI8ZDBae69zuNBZB_eGHAYNtFzhIkSdpFt3oMl3taRq8i3HqEeiT0gOgpD7EZEHYtPQ4vz21lHzpFogL-mj2V3OFhDVCJzhbI6JeTVAiGV8rgIiYRkYtByG_-ystHVUdm-fUCN8fdVLYdTa50aCqmji-vq2cZJWXWp1MXHVuYyHi2ozgLB6DZWo6sAmLOT7R4lybep9n9EvoB1RX3vQKG-lRDAVfR6xCzGHEgkQCk7wj7j5Oj6gFWfMwYLcKu-8lqpgAj1YF8o3GOuUrVkkYJFA-yPgTOKtSlmkkpTkjzImifQAn0RQPTUeXG1YDQ3yqrH3wT0G1zv2UOn27AVlaO5sQgq-wQ7B9IlIL1G65ChO6Ff6qzpziOKFaVJyVkDTicsWty0oDZs46LgUcIUFWhEu9wN1680Rgxzj_-6zqu-1-Y4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/459569" target="_blank">📅 00:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459568">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMoZYnWSoe_62j-M9j-uAimEK5xZ5U0kPYpgxtnNJjoQ3jbIHWNk0731DJK6rTkY5xgxNGndGOFq8Lbn5cl8wDeG_zs_kJ-1reRqVqUo-eNiVK56-Wh8xGLEtxs9q6LwV0cw1Ya_-pxgj9219chgQrT65gdd8WQFgByjEmBKTo6Dz2BrsCQZ3EBpLckG7ZFC1UFMZk64QUim3391wCvjZa2CfCLyOJ4WBMm48yI8N-qK7pjj_FmuC9whfUSeGQPrNGuOQ8yzGM5NOBFhdrtAtfMFTBIFG0aZ91B7Lbc2VY32m4xLFVn-J3nl7KZNwtaYzxmehvEMjHvCX2D0ZEaC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رهبر انقلاب: ملّت عزیز ایران و جبههٔ مقاومت، درس‌های فراموش‌نشدنی برای دشمن آمریکایی دارد.
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/459568" target="_blank">📅 00:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459567">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام با حمله وحشیانه به یک منزل مسکونی در سیریک، محل مجلس عقد دو جوان پاک را به خاک و خون کشیده و با به شهادت رساندن و مجروح‌کردن نزدیک به ۵۰ نفر از مردم عزیزمان خاطرهٔ وحشیگری مدرسه میناب و ورزشگاه لامرد را زنده کرد.
🔹
رژیم کودک‌کش آمریکا در این حمله جنایتکارانه یک بار دیگر با به شهادت رساندن چندین نفر از جمله یک کودک، عمق کینه‌توزی و دشمنی خود با مردم ایران را آشکار کرد.
🔹
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز با رمز مقدس یا رسول‌الله(ص) با حملهٔ سنگین موشک‌های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
🔹
عملیات انتقامی نیروهای اسلام ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/459567" target="_blank">📅 00:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459566">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ad153b05.mp4?token=fBTdem3wQ-e8_upsofxDbR4wLfFiRV96kFsrtqNMdZDXlpxjfRs_ZNKXmCVcyqjK7eL9xYgA3fox4LWrgWasQATEhWj3qRel4Pfv7gFkSnPtUKRzlfVAML_qHiCBSHJjbibDe-BPnoqk7KUUUCnh_4DvdF8GquKmaTBwFr1086i78MaXCBWCKbfpZ2cEjLWTBtXFSl9sJHcn3W1t3_fOvebMCtr8BNcTPSucKdqQT1i0xhNdJ_NUEoiWIgFxYs0WzSfn2f15PTWUBFqn-QOXVf21XSo_32fJscf6a8Cmg8SaRXr5r562jpKRCOh_5ToJiN-BR9acaqjCUXD4-TSnRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ad153b05.mp4?token=fBTdem3wQ-e8_upsofxDbR4wLfFiRV96kFsrtqNMdZDXlpxjfRs_ZNKXmCVcyqjK7eL9xYgA3fox4LWrgWasQATEhWj3qRel4Pfv7gFkSnPtUKRzlfVAML_qHiCBSHJjbibDe-BPnoqk7KUUUCnh_4DvdF8GquKmaTBwFr1086i78MaXCBWCKbfpZ2cEjLWTBtXFSl9sJHcn3W1t3_fOvebMCtr8BNcTPSucKdqQT1i0xhNdJ_NUEoiWIgFxYs0WzSfn2f15PTWUBFqn-QOXVf21XSo_32fJscf6a8Cmg8SaRXr5r562jpKRCOh_5ToJiN-BR9acaqjCUXD4-TSnRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاین در شب ۱۸۵، قرار عاشقانهٔ مردم را رقم زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/459566" target="_blank">📅 00:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcD3DgACwGkXx29_2fELfzKoymcQfFXTamkR0xdiAopSpNIFAP7pWxqaKEjndKQ-p7yfD43c4WRc-1mf87U2fnSujH0Zj0shwY7P5DDTct5GAKOmuSrkjhCDfifis4MC2yA-LTd94zMAW8fOV9ZB2lIvtJh00gzhJEBhMM2-42NL2rJv6C1ErEmed4EmhChYdrcLzJq7kxFN3cX9r4y1i7DCjw7w4vuAAiPLpLtqRbgBfAkmXnvQeYQfwLh5bWkZXJR6c6uoLPvXWv3t9eJwW880Ahhcz51U4ZIdbsYBAY89xfLcDduvt05qjGJLs0cfHCrcaOqj-MkVmMLkjEuecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AngxF6Dc5x6VzVKaX1n1e5pvEyKcy_iWvw_FiMqsVHZwlSx1Ti-39btKt61oONrk3j9eH7duVg4Ity8jn-RReucZsZ_8RzV2ipmnIT3oTQruu_4yO7zyWwgsUYomc5lEKgQaqyyRNa1Q29X7T4ihmP421jgcQGfcv9E1TZDP_h9rWiprIfEiIuYKJb7ID3Dve-GGJkG8URnMW25Nr--5HGqzor6uAiaKAnNwmhmZLvJOVW19PGjWIleq4Xu6rowtDJbJ_E6YFxlxE85uV-N6OHmuhBSKbl7OPS9ds7S_CmgwdnA9OfbOAgDFzaB0LLD2XM3RCEYu8VIpHxdze78BiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
افزایش شمار شهدای جنایت آمریکا در کوهستک به ۴ نفر؛  یک کودک خردسال در بین شهدا
🔹
هلال احمر هرمزگان: در پی حملهٔ موشکی آمریکا و اصابت ترکش به یک منزل مسکونی در روستای کوهستک از توابع شهرستان سیریک در استان هرمزگان، که مراسم جشن عروسی در آن در حال برگزاری…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/459564" target="_blank">📅 00:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861251ffab.mp4?token=eityLSgihF0ZtI294-0bgSFK15qIoAJw0viD5SnVztH3Xyp31-cRswWdSszyn1tweYs5o0JKaPvpXpbfv7bfioDjDq3Q3uHhOgraZFnOlQ0zVpCt3bZgANr_9bElQqcac2-q2SvVv1ZpP1RrDpoEgLao1fjRvwfp7TAPs6cSjO5Td_Oytru5sWlOduEjnpKTianVOPldSDDmjB7Wus8b0vxDB0vt7uEpRPjK9mNmtOciaXNrKCp06cPTmYVC9WlecPMuFdin8FSAOJ96ERks-jBY3d62Q6n8vtvg_X7hzphOY6R0COzgefIuNapphJz_QeEjQmuJatfndHKL8jcFAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861251ffab.mp4?token=eityLSgihF0ZtI294-0bgSFK15qIoAJw0viD5SnVztH3Xyp31-cRswWdSszyn1tweYs5o0JKaPvpXpbfv7bfioDjDq3Q3uHhOgraZFnOlQ0zVpCt3bZgANr_9bElQqcac2-q2SvVv1ZpP1RrDpoEgLao1fjRvwfp7TAPs6cSjO5Td_Oytru5sWlOduEjnpKTianVOPldSDDmjB7Wus8b0vxDB0vt7uEpRPjK9mNmtOciaXNrKCp06cPTmYVC9WlecPMuFdin8FSAOJ96ERks-jBY3d62Q6n8vtvg_X7hzphOY6R0COzgefIuNapphJz_QeEjQmuJatfndHKL8jcFAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خرم‌‌آبادی‌ها: ای ارتش ای سپاه، بزن بزن ماشاءالله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/459563" target="_blank">📅 23:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d9ddf473.mp4?token=FCQmX5nnPY9Bf6uFZnLLobL94k5Q2TtUsxdBhwjSQsNCsj0x0jxOhNoNa00RGjBUxMRdLEt4laYu4NONXFpqdRKFD5pgk1LazTQPCn0r9Aqd7_e1XMK9fv-c5fb8Vz_7BHAvK_1vO9V6PzYdQEj5Yzlk0AVm-mAsXuE0i7PcNJvVTDq6XeUl8OBWA992ZZmfvcopRx8pyxti5cY6KKcRRHXnxBXz2MAnHgvsIt40PnMLMlJmdNtenkOHFmnZNDI0Elr0e774hAficTd5ieEz5zMMV-1ll2ODZAykZOD2tjdTIRcFyG1ISENHiSGXh2coadjmU6mse72_-N5lOMjBFTDfj5rlvRzJvHwFX2Rx2InjRyOb4xO5b52p68bmcbGXsVTx8IX6fsHYpCV-3hacDeyORzm3nodavk03dcJd6MInj90BJ4BcytAA_ahrqL6BnUB0IbQaiVddHrT4TM_6y8BHlVM9w8l8bUJf9uQYV3glohFdqJCenQUNaPQbXovG1nVazAroWQlxbyurkDYAcsOhTe04E-5-3qz4wJdBPzs6qzehlAmUlhLBMYn29WOa5_IWrJ6LUGXYsjSraoRdj_wH50a7fsAragnx-fkbp83wwYbshLz3EAxg_UKXvuQd33FKTa3Tkeo-Kxusu4LkXPKTIZaJsK6iDiACNFW4sOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d9ddf473.mp4?token=FCQmX5nnPY9Bf6uFZnLLobL94k5Q2TtUsxdBhwjSQsNCsj0x0jxOhNoNa00RGjBUxMRdLEt4laYu4NONXFpqdRKFD5pgk1LazTQPCn0r9Aqd7_e1XMK9fv-c5fb8Vz_7BHAvK_1vO9V6PzYdQEj5Yzlk0AVm-mAsXuE0i7PcNJvVTDq6XeUl8OBWA992ZZmfvcopRx8pyxti5cY6KKcRRHXnxBXz2MAnHgvsIt40PnMLMlJmdNtenkOHFmnZNDI0Elr0e774hAficTd5ieEz5zMMV-1ll2ODZAykZOD2tjdTIRcFyG1ISENHiSGXh2coadjmU6mse72_-N5lOMjBFTDfj5rlvRzJvHwFX2Rx2InjRyOb4xO5b52p68bmcbGXsVTx8IX6fsHYpCV-3hacDeyORzm3nodavk03dcJd6MInj90BJ4BcytAA_ahrqL6BnUB0IbQaiVddHrT4TM_6y8BHlVM9w8l8bUJf9uQYV3glohFdqJCenQUNaPQbXovG1nVazAroWQlxbyurkDYAcsOhTe04E-5-3qz4wJdBPzs6qzehlAmUlhLBMYn29WOa5_IWrJ6LUGXYsjSraoRdj_wH50a7fsAragnx-fkbp83wwYbshLz3EAxg_UKXvuQd33FKTa3Tkeo-Kxusu4LkXPKTIZaJsK6iDiACNFW4sOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اراکی‌ها در شب ۱۸۵: خلیج فارس تا ابد خلیج ایرانی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/459562" target="_blank">📅 23:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGCaMzeXXx8regOr9ja4W45r-IhZyTKtpIgoaT4NgOlfQ_x8qDhMKflfGdNPxXaEpIjsWOxNLkqkVK2vgSPBdFTz5CmPZzJwV5OVpeJ9KiILYr7tTju3L9u8Dk4Uh6w9TftSQFeJiexlnTMqEfU8lyiy39bio8NCVRBRw01OY5Tr9-cMkg5mpilxyOk8-xtts8o0cOaS9SY3n9zOsyH-_CZtTRqEXp5r5_fgZ2Phmcis2kvb_3F5p02d9TrCaRenBYadG2XQCWFn1Smqeya31COxRy4_EsYxoxHr5Q0dm6Gns4rQvGE2yXHZ7yEuwr0sCaKdkA9AsoDb8ZbGIE9ppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت گشایش‌های تازه؛ از دارو و انرژی تا زیرساخت و حمایت اجتماعی
🔹
روزگار ما، روزگار دوگانه‌هاست؛ از یک‌سو موج‌های ناامیدی و از سوی دیگر، تلاش‌هایی که بی‌سروصدا در گوشه و کنار کشور ادامه دارد. در کنار چالش‌های موجود، طرح‌های مختلفی در حوزه تولید، انرژی، فناوری،…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/459561" target="_blank">📅 23:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1042a89ac9.mp4?token=dBLqer4E2ktc5n9kXmeuBNqCyqNQoyqEidrclmEWH1lWRMFCX0KgPMSVIxGSYmNpaLmM-JslxEV5rZ2XkqKaoNq4cNtqPpNMPnWiOgFvcRpsOLleb1vBc8upGJBQ1LpThy_zvB99pimywdXKA1-9EgX9RHTboRZjdyx6vgljuOpxJ1LQRUInDwYwNeXN86nvZkvROvft8JFhshL8eZQ00I_RekTY8TD2g2Z5Gx993g7FD6scJKBaSsmDu7cw_ucWER6_JQRkf7rt57u13iq50OgC6LN3QAxOUvRPG6hx0oWgWvsUqB3oLXEQNZpQduv8NOUpFrera1A7LB5Ta9mLLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1042a89ac9.mp4?token=dBLqer4E2ktc5n9kXmeuBNqCyqNQoyqEidrclmEWH1lWRMFCX0KgPMSVIxGSYmNpaLmM-JslxEV5rZ2XkqKaoNq4cNtqPpNMPnWiOgFvcRpsOLleb1vBc8upGJBQ1LpThy_zvB99pimywdXKA1-9EgX9RHTboRZjdyx6vgljuOpxJ1LQRUInDwYwNeXN86nvZkvROvft8JFhshL8eZQ00I_RekTY8TD2g2Z5Gx993g7FD6scJKBaSsmDu7cw_ucWER6_JQRkf7rt57u13iq50OgC6LN3QAxOUvRPG6hx0oWgWvsUqB3oLXEQNZpQduv8NOUpFrera1A7LB5Ta9mLLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از محل عروسی در بندر کوهستک که هدف حمله آمریکا قرار گرفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/459560" target="_blank">📅 23:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار از پایگاه‌های آمریکایی در اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/459559" target="_blank">📅 23:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459558">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
افزایش شمار مجروحان حملهٔ آمریکا به مراسم عروسی کوهستک به ۵۰ نفر
🔹
معاون امنیتی استانداری هرمزگان:  در پی این حمله تاکنون ۲ نفر به شهادت رسیده و ۵۰ نفر نیز مصدوم شده‌اند.
🔸
با توجه به وضعیت برخی مصدومان، احتمال افزایش شمار شهدا وجود دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/459558" target="_blank">📅 23:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484a9459e9.mp4?token=hvlnpcOn6hNBOmD1dN4_mkenVkA8Kee6oWBSK6M9FGFxUeNDEafmhpMQXB7mzF5vKDdHuvSmEnik753Z5XOe6CZLUmm6i21uX2z9J4o3qJZ07gJaFQeze3a-IeW3vym-M5tpsLQWsJi0Q8BfbdJzExGK_6N8Oeb9zo3QYjEel1E64ADzwXxcmbnOlS0ueeZ1K0n_q0Pv30XWbZaOJ7fVQSReCUh4IX3lwAt1n2lgrRQv8JMLouvMFrB-qjjVAW8uarZxeumMGfmzIMTO6DnDKCh_0miNJUNNuA6anK3cD9fYMIDI72re_o4ZKfhIr7K9FxT7sCX2HSmHMzRjCL7mzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484a9459e9.mp4?token=hvlnpcOn6hNBOmD1dN4_mkenVkA8Kee6oWBSK6M9FGFxUeNDEafmhpMQXB7mzF5vKDdHuvSmEnik753Z5XOe6CZLUmm6i21uX2z9J4o3qJZ07gJaFQeze3a-IeW3vym-M5tpsLQWsJi0Q8BfbdJzExGK_6N8Oeb9zo3QYjEel1E64ADzwXxcmbnOlS0ueeZ1K0n_q0Pv30XWbZaOJ7fVQSReCUh4IX3lwAt1n2lgrRQv8JMLouvMFrB-qjjVAW8uarZxeumMGfmzIMTO6DnDKCh_0miNJUNNuA6anK3cD9fYMIDI72re_o4ZKfhIr7K9FxT7sCX2HSmHMzRjCL7mzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بافقی‌ها هم‌قدم با ایران قوی به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/459557" target="_blank">📅 23:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459556">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39bd610791.mp4?token=NKv342M1U3ZQdVAgfdG6401sYdhC2mSZVn9ETIoy2t9TQtabRx0zhxZ_X5jaaxawTKRvg7fc1QQK1kOH2hBANTSBCoWyECUWEwKYnDd874rz1CffkuSqU7WPz5gplpoVtZm_47AGLrdkVUqhs0u3oa29J4i6DmfPwyBTfh2ps1iEszUuor76u90j6QX5bR7JUUG-HOqVgrDohr3yNKMP9BD-xzgJtSw-7dQ0nX2Yi7rvNtAT1iKuDM7eKhYJtgErH18fRy0mfyMHCAiYLFG5Q8J59qSdZarxcelpQL8DXgeToFWGZU5qEB0gSx6zZFjZdMZ3Ru4OJIN-zJ15hlT3Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39bd610791.mp4?token=NKv342M1U3ZQdVAgfdG6401sYdhC2mSZVn9ETIoy2t9TQtabRx0zhxZ_X5jaaxawTKRvg7fc1QQK1kOH2hBANTSBCoWyECUWEwKYnDd874rz1CffkuSqU7WPz5gplpoVtZm_47AGLrdkVUqhs0u3oa29J4i6DmfPwyBTfh2ps1iEszUuor76u90j6QX5bR7JUUG-HOqVgrDohr3yNKMP9BD-xzgJtSw-7dQ0nX2Yi7rvNtAT1iKuDM7eKhYJtgErH18fRy0mfyMHCAiYLFG5Q8J59qSdZarxcelpQL8DXgeToFWGZU5qEB0gSx6zZFjZdMZ3Ru4OJIN-zJ15hlT3Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم همدان امشب با شعار مرگ بر اسرائیل به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/459556" target="_blank">📅 23:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459554">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9740e69e4.mp4?token=SDksmspTStUG0fJ-LxRSL5NOrRn0gSlvesnUU28FkAo5LXOfVOyNPKlOOczhhgFrjFSM2xZGdvVxAF4jpum6XnRlmxVcH6e0DFXwhCAO5NtBdMrfdtupNQMkwWOSPEeGUmgNu0v6IVkuAyyrP36Q431FoTsvZWXillTSqetZ158AEekQXqMbQXqn7wYEX-2xElCYwBjpfTtoSV7qR5PCqf4L3ddm6qmW3VbW66EjWlLOFq44SXYa9c7kSkF9fXdAEdYYCJbwKBx2YeWGKNKy-26TwzDcr7Ioe7HXisV4fW6pQ2Cm-mt7GNDZ09krwcEbpM1VKJlx06WaZ_z2E_kMag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9740e69e4.mp4?token=SDksmspTStUG0fJ-LxRSL5NOrRn0gSlvesnUU28FkAo5LXOfVOyNPKlOOczhhgFrjFSM2xZGdvVxAF4jpum6XnRlmxVcH6e0DFXwhCAO5NtBdMrfdtupNQMkwWOSPEeGUmgNu0v6IVkuAyyrP36Q431FoTsvZWXillTSqetZ158AEekQXqMbQXqn7wYEX-2xElCYwBjpfTtoSV7qR5PCqf4L3ddm6qmW3VbW66EjWlLOFq44SXYa9c7kSkF9fXdAEdYYCJbwKBx2YeWGKNKy-26TwzDcr7Ioe7HXisV4fW6pQ2Cm-mt7GNDZ09krwcEbpM1VKJlx06WaZ_z2E_kMag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
افزایش شمار مجروحان حملهٔ آمریکا به مراسم عروسی کوهستک به ۵۰ نفر
🔹
معاون امنیتی استانداری هرمزگان:  در پی این حمله تاکنون ۲ نفر به شهادت رسیده و ۵۰ نفر نیز مصدوم شده‌اند.
🔸
با توجه به وضعیت برخی مصدومان، احتمال افزایش شمار شهدا وجود دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/459554" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459553">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgR0zPexpb2LxzPXI6JtZP_ZwSLN-h15l3bps1uqAxDL6TI9BcF91JOfZVs7LEFpSVj3D87MjW2e8mC2dj07dP1t3WJ9fwrFQJcIf9ALk3HsL65LPgirCp9NHLO-TG1ONq2kt62sV2r_hmH_AiEAisenvlFj-crVQydCdmWRJXDnIq3s1_OM7FFUUtJetOiWjdvahMEJY5xEMVK-yeqq6iXG25PH5ACASqvYRiI0yBRaWWXwGLRtgZlvKy9a3VlzsROtC99vhsqnPCaNKvFK0_gVP62gllktwWWBpDU-vWUNrKBWwA48rR9YIeucWJeUMMGcDDnTTGQYoMYLSn4Z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی ارتش: انتقام شرارت و تجاوز از دشمن گرفته می‌شود
🔹
سریع، کوبنده و گسترده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/459553" target="_blank">📅 23:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459552">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌ ۲ شهید و ۲۰ زخمی در حملهٔ آمریکا به مراسم عروسی در سیریک
🔹
معاون امنیتی استانداری هرمزگان: در حملهٔ آمریکا به یک مراسم عروسی در کوهستک سیریک، تاکنون ۲ نفر شهید و تعدادی مجروح شده‌اند.
🔹
مدیرکل هلال‌احمر هرمزگان نیز از انتقال حدود ۲۰ مجروح به مراکز درمانی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/459552" target="_blank">📅 23:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459551">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار از پایگاه‌های آمریکایی در اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/459551" target="_blank">📅 23:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459550">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
حملهٔ موشکی آمریکا به اطراف شهر اهواز
🔹
معاون امنیتی استانداری خوزستان: نقطه‌ای در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/459550" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459548">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
🔴
تکمیلی؛ حملۀ دشمن آمریکایی به یک عروسی در کوهستک
🔹
معاون امنیتی استاندار هرمزگان از حملۀ دشمن جنایتکار آمریکایی به یک منزل مسکونی و مراسم عروسی در شهر کوهستک سیریک خبر داد.
🔹
بلافاصله بعد از وقوع حادثه نیروهای امدادی به محل اعزام شده‌اند؛ جزئیات حادثه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farsna/459548" target="_blank">📅 22:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459547">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960eed7922.mp4?token=NPcBUly8NYzu_iF1d2LGe-LRHR2eDOXueDbwX7-nzpUF-Kgfb6ZQQx-q1fecfLBM2mg3Ka3fOS6jSwIqk11cxPNoelq43aTkWaLljU4SwG8yG78eHZDhIG3po8v5Y3W9Pp1xrPBQJTdqFdQatqjI7XxkMT4obv0dp5X-O4h9nCm06UGRr6oTSkCHpy7xsR4r06-F8huqH-DqxHqTpK0fhe-F__lJJSqDGsVRZBnlP3WGncQbS020cmgN5H4vVtdGBSctkKYDz_8874dAKeVxK6gALQf0JlGQVt-A3GFGMIhq4NrcVv3xjyzg_pObuL2IlAI4h9GK5EWmcjPo1mOihA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960eed7922.mp4?token=NPcBUly8NYzu_iF1d2LGe-LRHR2eDOXueDbwX7-nzpUF-Kgfb6ZQQx-q1fecfLBM2mg3Ka3fOS6jSwIqk11cxPNoelq43aTkWaLljU4SwG8yG78eHZDhIG3po8v5Y3W9Pp1xrPBQJTdqFdQatqjI7XxkMT4obv0dp5X-O4h9nCm06UGRr6oTSkCHpy7xsR4r06-F8huqH-DqxHqTpK0fhe-F__lJJSqDGsVRZBnlP3WGncQbS020cmgN5H4vVtdGBSctkKYDz_8874dAKeVxK6gALQf0JlGQVt-A3GFGMIhq4NrcVv3xjyzg_pObuL2IlAI4h9GK5EWmcjPo1mOihA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام مردم شهرکرد به رئیس‌جمهور آمریکا در شب ۱۸۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/459547" target="_blank">📅 22:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459546">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38c8c8a60.mp4?token=ne9s8PxKefd1JR_h40lWpdMURoyefVFnxM8hzssK8Km0XtaZfX0uUzhAS9Xb2alPgM7GMKT2iek9w-eUQay_Mu4Z8qaKA_9KhVuGd8V0q86S8MnCzcr3XesSLFaCcbPEJtxS2FutflgjWnJRxQlquTIcjwvSCGqhae7J_hL68jhkFi9ufV3FztQ7BpoQQQLWiwziaHz1DgbT_bU8FFhDnapFCSrot2fJxtpYrbxEcwbBjLc6dU0Y27ajhrEJxBIFaqLJnab1q9t7wsjgzZzXBoq-ubjfnlZQ-EhkA9G8-kchbGKeojaKN4jh_gNvtsHrAujFUqejmA5BOgyIcjhUblpMnTFIW_npg4l4SK0en8kPHwMxTmV5YpootlTfkv4UGsMwiy_hpSJeIF69maG9ZZSkrNt0z_rmqXhW0JmZBbwkIuoKohxNvVDPN4kW3kybt4NLbzFN4xdaFs_YJnF4S2OqvcvE38GKDnD6Wj2oHJVio86stdbuEjmUxIHQC7u0WK6Bf7Uc00zj8N-RXs9BC1NTip3P1GAhWlAT1xnMpDuHnNBp9hVWHyKSE5ymFD4U7YhbAbnDIvkxZ6yLN5zp0QE3zsBk6TxlNlIu-QbzA92iOWMg1XTssSlp9DGkn36DaDV3rvig1FaPckjeiQWJ9BmPyqQQ9TeyC6mqgVCyw6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38c8c8a60.mp4?token=ne9s8PxKefd1JR_h40lWpdMURoyefVFnxM8hzssK8Km0XtaZfX0uUzhAS9Xb2alPgM7GMKT2iek9w-eUQay_Mu4Z8qaKA_9KhVuGd8V0q86S8MnCzcr3XesSLFaCcbPEJtxS2FutflgjWnJRxQlquTIcjwvSCGqhae7J_hL68jhkFi9ufV3FztQ7BpoQQQLWiwziaHz1DgbT_bU8FFhDnapFCSrot2fJxtpYrbxEcwbBjLc6dU0Y27ajhrEJxBIFaqLJnab1q9t7wsjgzZzXBoq-ubjfnlZQ-EhkA9G8-kchbGKeojaKN4jh_gNvtsHrAujFUqejmA5BOgyIcjhUblpMnTFIW_npg4l4SK0en8kPHwMxTmV5YpootlTfkv4UGsMwiy_hpSJeIF69maG9ZZSkrNt0z_rmqXhW0JmZBbwkIuoKohxNvVDPN4kW3kybt4NLbzFN4xdaFs_YJnF4S2OqvcvE38GKDnD6Wj2oHJVio86stdbuEjmUxIHQC7u0WK6Bf7Uc00zj8N-RXs9BC1NTip3P1GAhWlAT1xnMpDuHnNBp9hVWHyKSE5ymFD4U7YhbAbnDIvkxZ6yLN5zp0QE3zsBk6TxlNlIu-QbzA92iOWMg1XTssSlp9DGkn36DaDV3rvig1FaPckjeiQWJ9BmPyqQQ9TeyC6mqgVCyw6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بر‌وجردی‌ها در حمایت از نیروهای مسلح: بزن که خوب می‌زنی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/459546" target="_blank">📅 22:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459544">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سپاه: حملات از سر استیصال دشمن قفل تنگه هرمز را محکم‌تر می‌کند؛ رزمندگان پاسخ پشیمان‌کننده به متجاوزان را آغاز کرده‌اند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی: ملت بصیر و انقلابی به پاخاسته ایران اسلامی؛ تداوم حضور شما در صحنه، دشمن آمریکایی را خسته و…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/459544" target="_blank">📅 22:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459543">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpUwB8Evwyz8pymgH1PdkkLtHwBCsXm_DS3qu51q7qR0is_ZEGc9OFfQTFYizPUPCor3tgsXmyTtPmlT7B2ATNDTTqD8lsPgWDZN8KK6vrR7QxP_aZ89lQoDb2ZuiYeSdUaPYEr3OhMgrENB6vs84wI8B6HX5pdnwday0P1b2jKUt_wkVT_ppm4nSakScX4Sk9CEJ87-RI1SVup1FyY6zKgMYePoPHInbwp2WrvTn6kUh-cK8JG_lrUM7eRJYN3e3PWi9HBIt-Q7Za0duiqqtp0Ut6WUkKlF-aEdJdS_21nrTNLhCwSO7s1FkHk4CC7FywfjQL3tQTOTeT7I_OXhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: حملات از سر استیصال دشمن قفل تنگه هرمز را محکم‌تر می‌کند؛ رزمندگان پاسخ پشیمان‌کننده به متجاوزان را آغاز کرده‌اند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی: ملت بصیر و انقلابی به پاخاسته ایران اسلامی؛ تداوم حضور شما در صحنه، دشمن آمریکایی را خسته و مایوس کرده است و مقاومت و اقتدار فرزندان رشید رزمنده شما در تنگه هرمز، سردمداران کاخ سفید را کلافه کرده است.
🔹
ساعاتی پیش در حملاتی کور و از سر استیصال، ارتش متجاوز آمریکا نقاط متعددی در سواحل جنوب ایران از جمله چند مکان غیرنظامی را بمباران کرد.
🔹
حملاتی که قفل تنگه هرمز را محکم‌تر و عزم رزمندگان را در سرکوب نیروهای اجنبی مداخله‌گر در تنگه هرمز را راسخ‌تر کرد.
🔹
گزارش نتایج عملیات رزمندگان متعاقبا به استحضار ملت شریف ایران خواهد رسید.
و ما النصر الا من عند الله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/459543" target="_blank">📅 22:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459542">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تکذیب حملات دشمن به «جم»، «کنگان» و «لنگرود»
🔹
شبکه‌های اجتماعی از وقوع انفجار در ۳ شهرستان «جم»، «کنگان» و «لنگرود» خبر دادند که مقام‌های استانی اصابت هرگونه پرتابه و حمله دشمن آمریکایی را به این نقاط تکذیب کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/459542" target="_blank">📅 22:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459541">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
حملهٔ دشمن آمریکایی به منطقه‌ای غیرنظامی در کوهستک
🔹
استانداری هرمزگان: دشمن آمریکایی در حملهٔ وحشیانه به خاک کشورمان یک منطقهٔ مسکونی در کوهستک را مورد حمله قرار داد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farsna/459541" target="_blank">📅 22:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459540">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e810f08972.mp4?token=uVUbGxhM_GgwUGAZWSNt62mzMI2wBt-ckiBzezAs7h6pgJEeAV3SDrqcoueaBIhwU7CgbSyqy1nHUtKc0qN5KUhN6V2i6A23BTTqe3Yjww7gF8XBwqiu4jQjlvZItSU1nT3fCSEqhMYxbGCZS8bm5uQDcC9LiV2bWfKIrJl-XNrSNB6N_VA3Ub9NfcxnXSNQvtSXvZZ-jnZaEZGot3YGU3GUutI-V7Ci07N2tSxYs2aGDe0sYBJJsuZBt9iE9nRW7Ka9wLVPratHuIID-Gi-KVJw0xnyfpKwOrcf5sDIwDTvM0xCXAnowStmIycdLjaSp3l2G5Mhr9t-ohL9cje1rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e810f08972.mp4?token=uVUbGxhM_GgwUGAZWSNt62mzMI2wBt-ckiBzezAs7h6pgJEeAV3SDrqcoueaBIhwU7CgbSyqy1nHUtKc0qN5KUhN6V2i6A23BTTqe3Yjww7gF8XBwqiu4jQjlvZItSU1nT3fCSEqhMYxbGCZS8bm5uQDcC9LiV2bWfKIrJl-XNrSNB6N_VA3Ub9NfcxnXSNQvtSXvZZ-jnZaEZGot3YGU3GUutI-V7Ci07N2tSxYs2aGDe0sYBJJsuZBt9iE9nRW7Ka9wLVPratHuIID-Gi-KVJw0xnyfpKwOrcf5sDIwDTvM0xCXAnowStmIycdLjaSp3l2G5Mhr9t-ohL9cje1rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۱۸۵ مردم کرمان با رنگ‎وبوی جهاد و حماسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/459540" target="_blank">📅 22:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459539">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اصابت پرتابۀ دشمن به محدوده خارج از باند فرودگاه جیرفت
🔹
معاون امنیتی و انتظامی استاندار کرمان از اصابت یک پرتابۀ دشمن آمریکایی به محدوده خارج از باند فرودگاه جیرفت خبر داد.
🔸
این حمله هیچ‌گونه خسارت جانی به دنبال نداشت و به باند و ساختمان‌های فرودگاه آسیبی وارد نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/459539" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459538">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/459538" target="_blank">📅 22:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459536">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
حملهٔ دشمن آمریکایی به منطقه‌ای غیرنظامی در کوهستک
🔹
استانداری هرمزگان: دشمن آمریکایی در حملهٔ وحشیانه به خاک کشورمان یک منطقهٔ مسکونی در کوهستک را مورد حمله قرار داد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/459536" target="_blank">📅 22:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459535">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqYuC_o0h1b2fFD8gTDSMPb6qVdCKVm0iaWTO-TGEMYusTnnlSrmI2Lv9zuof_DONY8YChnE47HoUZq_G7bw5kBaLxZH9mzW9LUtztEZqZf6BIu0sCsERBmLw4RbW34J0ahzceKvxCIoT2QedqGToysEAry_jjTxKopbdiz81Lv6YDoy1H3HP83QkMMY0DMlwxzd_nLoZ7WPLcHOgO4EcH79Si9SuSGZ3uJiDI4MKeekeOW3DKfO19COgpSJAy-M1X_9m90mKcWF4-b683TEcsAslxzwpHG_zEc23iPFSR0QeuI5xL7JVpKeDhCZSrnZyseGZJS7eianBx6OlSPl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویب دریافت هزینه خدمات از کشتی‌های عبوری تنگۀ هرمز در کمیسیون امنیت ملی
🔹
سخنگوی کمیسیون امنیت ملی: بر اساس ماده ۳ طرح اقدام راهبردی تأمین امنیت و پیشرفت تنگه هرمز، در قبال خدماتی از جمله خدمات دریانوردی، محیط‌زیستی، سوخت‌رسانی در شرایط خاص، بیمه‌ای، ایمنی…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/459535" target="_blank">📅 22:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459534">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/623c890cf8.mp4?token=cxLjYV_fJbwrg2eJ--fBut_n0dO7JCWXcWDHAHKlg7XttwMVjTN8Qy95phDdyRxdDOEYewudPKDVQ_nz6spVZNAkeRaxF2ZFoFFAFUmoeEP_8rDP0wGwXH1Z9tJz9ZVmBqfJJzFjNAU5Es7EpMaSv8Zv37Icy6u4WiJr8C2emoj5-SdiYQ_KkMFVsEOT7zi9v-p2Ax8d3YkGMLrV-g2xCJfW5sXPsHDJV9ix58mVqxMlFE89DK_6HqnBVPoFyBkxNNYIRqIiZH2VEJjhM4yGpI-OM2B_FUQBSBk5dvKePcWR4MlFEOqAsdIowkBMIfIBsGAgKOMn7cRh-QIAxajGaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/623c890cf8.mp4?token=cxLjYV_fJbwrg2eJ--fBut_n0dO7JCWXcWDHAHKlg7XttwMVjTN8Qy95phDdyRxdDOEYewudPKDVQ_nz6spVZNAkeRaxF2ZFoFFAFUmoeEP_8rDP0wGwXH1Z9tJz9ZVmBqfJJzFjNAU5Es7EpMaSv8Zv37Icy6u4WiJr8C2emoj5-SdiYQ_KkMFVsEOT7zi9v-p2Ax8d3YkGMLrV-g2xCJfW5sXPsHDJV9ix58mVqxMlFE89DK_6HqnBVPoFyBkxNNYIRqIiZH2VEJjhM4yGpI-OM2B_FUQBSBk5dvKePcWR4MlFEOqAsdIowkBMIfIBsGAgKOMn7cRh-QIAxajGaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان در شب ۱۸۵ هنوز با حضور مردم روشن است
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/459534" target="_blank">📅 22:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459533">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در عسلویه
🔹
فرماندار عسلویه از شنیده‌شدن صدای انفجار در این شهرستان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/459533" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459532">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3xVs2nf2lIaNgXVGwG3nLDpv5HytRmQjY1a5sLfp23XnD-8ruSj1XlPG4BTsgPD2UKEkset5pIT32_n-79tRGxQIvEv96Glj9EAbZ5uRDUl0fI8egYJSZdhqrSPeYEsPjbtrlznuMoGdIUlZAe54cBsPMrrYcWLqlC3souqAa8H8tRAjkLi9xdQLysGEWCt7_wLFIs8Iy9DKEh8STobYK0pwkG8lKo9hgY4_pqHCY87CyPN5WOObAvYYgTFmH9K4BOvYLM47X6rVmrbgbHD8fs5hX0LTA6f-UPcnBzBuGiUHwhxpSkepixlTovyxCauTluUGv29DshKhwoxh1Hacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل سپاه: هماهنگی پدافند هوایی ارتش و سپاه معادلات دشمن را برهم می‌زند
🔹
سرلشکر وحیدی در پیامی به سرتیپ الهامی، فرماندۀ پدافند ارتش: هماهنگی کم‌نظیر بین نیروی پدافند هوایی ارتش و سپاه و شبکه‌سازی یکپارچه، به‌روزرسانی مستمر فناوری‌ها و اتکا بر توان جوانان دانش‌بنیان ایرانی می‌تواند معادلات دشمن را بیش از پیش بر هم زند و بازدارندگی اطمینان‌بخشی را برای کشور ایجاد نماید.
@Farsna</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/459532" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459531">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
شلیک موشک‌های ایرانی به‌سمت مواضع دشمن
📝
مشاهدات میدانی خبرنگاران فارس از شلیک موشک‌ و پهپادهای ایرانی به‌سمت مواضع دشمن حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/459531" target="_blank">📅 21:52 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
