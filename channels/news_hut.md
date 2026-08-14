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
<img src="https://cdn4.telesco.pe/file/gTOIanrsI1ly7AImjH5l-r6-FiuqlGSWtyUP-KWSmLmpESTfDeIUU_WzlR_MvKBmvBBmBwBy9xFJ7v71dLMMexw5kA9HTQRqfXcEf0BNjETyOWpYgIFhpX4tMMySIxYbfuzBh6jgtnVgCHIhVkJo0sKI3CT_Sy1hj2K7D7VIQEK0o9TdJZ21y67VmWlwW0GrlS9arBAT4R4yGtrcC3RHzDpxXoIIFC86RQhfcw3YzIZ8VwOuEEhgKeXbqiGeO3eS6ASTD2-VxXfY_fQfjmWwG9jOM4qGMSlZjMSfkzXMhBoERHPML90RNP8K4gpXV3MSwrpvNaQdTYCwwmjUBBMGnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 125K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 13:02:44</div>
<hr>

<div class="tg-post" id="msg-70032">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
ناو آبی‌خاکی از رده خارج‌شده USS Peleliu (LHA-5) با وزنی نزدیک به ۴۰ هزار تن در جریان رزمایش RIMPAC 2026 و در آب‌های هاوایی، در یک تمرین نظامی به‌عنوان هدف مورد اصابت تسلیحات مختلف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/news_hut/70032" target="_blank">📅 12:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70030">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hoGK87DEGDVR8Sf8TKAMSBrNzp96wuK-xwax3IoyNHGnaWT0wooMD0AzUDCvw3Oh59aXQxmuZDfWEAD_SllMu4mV1clJs1AGwSqwfDTkXOcyGA4xH4BWMKuNHDNo6BjzUkT130As9S8MrXLXotR6JzVCv60FBL1oCxA4kvvXn2SLHYhNXFm7wd2h9qB9gfOLZWCd1E1Go2DRirQjj__TFkvhH6FCBe_nKEWVTe-T9Bb_3vBN3IPDP_lFAzuVq_ttxNBl7yCVSsVCBleVCEqU7pVmlFDZxPIAQBB_tzLGarpm9hwTj6BsFVNfOjGADezoOE9PRLabTnU1KbtMdzPu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fIXKXHyGbTNDu0TVvDG_2WGq3ic2Jq_EFyFdZ-82iCI9rPC35eQ0n5WtrJvAvgzMv9VCLbR1OG_ff8A1VVtiYixPBUjjELaMCGrT1k0uVGOpOBSkr9NGk_Pyc8-v0M0QbED_gDLP0i5XDGSEpfJCI35lMj53x7rlsHJXV-5XziXKPpN7Pe94P40XxXcgPvcQT6-Gt4xd4cFPd_G6D5L3zADttRqu-M064hs9ggY_MY2xduzJ20FJatQpkk7GAqpW-jdUyuCwE7xSSHB1HLP6prr_jqV7ueV3d6qVcC3v_Judk5ziI7ySJY-o7EznMO047O74IeMU0q-61DxG8K-A6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇮🇷
شبکه خبر صداوسیما رژیم، عراقچی را خوارج نامید:
خوارج ابتدا از یاران امام علی بودن که بعدا به خاطر افراطی گری از مسیر خارج شدن و به بقیه میگفتن منحرف.
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/70030" target="_blank">📅 12:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70029">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRknMQKIkBxeR5YsC3E3PJFIVg38RpoCh0GV4AXQ4GZsSvdDfrBCABK89fEO7BP5hA7ABa73pfzBjeBeR4_EFMfGYqwP-16qcpJOlFWiA4izq7lCT4dXMpGQQXjzT-OCa0dGM-jb22AJBfMOCjwy3O3IRiKKqnq184PjfVDyLTpUr2oEMLgl1O56pUrVSb6ti_33-aZWa2J7Rh6pbHJpmb2PydsZYD6-ZY9U-9eKSbdEvGcdU0m0O_vjd0t-LUx4LeJ18f7p3hchWiiSNn05XPRPy_YqlJXUTe5bbjiBQQLCr0OIqH7R9vBzHceGdZGk4WQGt-7sYTSGHV1IaXQcgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش حین عبور از تنگه هرمز هدف حملهٔ پهپادی قرار گرفت.نفتکشی که در تنگه هرمز مورد حمله قرار گرفته بود، آسیب جزئی دیده و خدمه آن سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/news_hut/70029" target="_blank">📅 11:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70028">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc0cc5ccd.mp4?token=LPT7qFulEtn4LBj8XRiOUmlwX73BNw8DvI7PKeKneWeysMXOItuds57By_63a3-W6u5VKkPx3T7SDqNsZ5UUhH89992u6ywlohIuBM0yoe2wAaABR4-y_JxZODxUJhflo3LIlHr7VadaOTSe3kQy9BawjjYsWautiz6nDc_wPzQq-ICBjuS-DbloKdJfO_xL8hclJmG1I3neTKHwUrBCKc82bfKpQg0VB7zuJ0JkCrhll0lmdWuU8FwKUX0E8-Xr7HHbKy2Ooam4nVn1GEr1xifn91EHuoGDDtxAD4018hL1WYZItLmTAtzpL42qf29QGInbjEVjURZmxP32BuetCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc0cc5ccd.mp4?token=LPT7qFulEtn4LBj8XRiOUmlwX73BNw8DvI7PKeKneWeysMXOItuds57By_63a3-W6u5VKkPx3T7SDqNsZ5UUhH89992u6ywlohIuBM0yoe2wAaABR4-y_JxZODxUJhflo3LIlHr7VadaOTSe3kQy9BawjjYsWautiz6nDc_wPzQq-ICBjuS-DbloKdJfO_xL8hclJmG1I3neTKHwUrBCKc82bfKpQg0VB7zuJ0JkCrhll0lmdWuU8FwKUX0E8-Xr7HHbKy2Ooam4nVn1GEr1xifn91EHuoGDDtxAD4018hL1WYZItLmTAtzpL42qf29QGInbjEVjURZmxP32BuetCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تهدید نماینده مجلس به کسایی که اعتراض کرده بودن:
پدر ها مادرها بهتون میگم دخترتون پسرتون کشته بشه تقصیر ما نیست ها
هرکسی نغمه ای بزنه بیرون که به نفع دشمن هست اون کله اش نتانیاهو هستش و زیرپاش تل آویو و حکم تیرش صادر شده
تابحال با چنین صراحتی کسی باهاتون سخن نگفته بود
دوس نداریم فرزندتون کشته بشه چون جاهل و غافله و هم میهن ما هستش ولی مجبور بشیم میکشیم
🎙
📺
حالا سحر امامی مجری صداوسیما:
نه شکر خدا این تجمعات نشون داد خونواده ها فرزندانشون رو با هر رده سنی طرفدار این نظام مقدس کردن
@News_Hut</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/news_hut/70028" target="_blank">📅 11:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70027">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
رئیس سازمان بهینه سازی:دولت برای بنزین چه برنامه‌ای دارد؟
🔴
روش اول: با قیمت فعلی تا میزان ۱۲۱ میلیون لیتر بنزین در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش شود.
🟡
روش دوم: ۱۲۱ میلیون لیتر موجود با سهمیه و بدون افزایش قیمت بین خودروها تقسیم شود و رقم مازاد بر آن با قیمت آزاد فروخته شود؛ درست همان چیزی که قرار بود در کرمان اجرا شود.
🔴
روش سوم: از ۱۲۱ میلیون‌لیتر، ۳۰ میلیون به حمل‌ونقل عمومی تخصیص داده شود و ۹۱ میلیون لیتر باقی‌مانده به‌جای خودروها به همهٔ مردم اختصاص داده شود.
🔴
از مردم هم میخوایم که نظرشونو بگن که کدومو اجرا کنیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/news_hut/70027" target="_blank">📅 11:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70026">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مصاحبه عادل فردوسی‌پور و امیر‌ قلعه‌نویی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/70026" target="_blank">📅 10:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70025">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeHHUvKLrhq9WTjzg5yio_JyenDrcLupoIvbnuHTdWzNem-z0EIlr11elE01vcELd4KckEGIHa9_LxPg2zhm_WZ6Yx30sO8wMG5awCvB7vHPWIVgSHCcjRn9qP2FxUsesZrkgKNIeuCcs4FyXgaaycslG2U8IMUQE54B-E6cXg8jtnUM_Wi178U6ewSsMhytFNW_wK_jCa89yB0ucAK2FOHCNq35rxAt05elHLxwpcJ3k5W7eVBeF_diT-Tz_CDt-yP9mvTqSyOigl5rSlWcovSEh61q6rfsdQk3huBFNq9nNja2tluFSRElCffLrSO-jqtN2u3suUIx9r35flDEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال استریت ژورنال:ایالات متحده در حال آماده‌سازی برای استقرار ناو هواپیمابر جورج واشنگتن در خاورمیانه برای جایگزینی ناو هواپیمابر آبراهام لینکلن به عنوان بخشی از برنامه قبلی جابجایی ناو هواپیمابر است.
ناو لینکلن بیش از ۲۵۰ روز است که مستقر است و ۲۰۰ روز است که در بندر پهلو نگرفته و رکورد روزهای متوالی در دریا را ثبت کرده است. استقرار غیرمعمول و طولانی مدت آن با تعداد کم پهلوگیری در بندر، قانونگذاران را بر آن داشته است تا نگرانی‌هایی را در مورد وخامت شرایط زندگی و رفاه خدمه مطرح کنند.
مقامات تأکید کردند که جابجایی ناو هواپیمابر جورج واشنگتن قبل از بروز این نگرانی‌ها برنامه‌ریزی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/70025" target="_blank">📅 10:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70024">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70024" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/news_hut/70024" target="_blank">📅 10:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70023">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0JDXlECQwqyk__6IPToai119v77LlGS7PUj3e_6eDDgxz4VicnWwIkvGrRZKiBBKZmF9pO8YEueod82rWVOu7lgVMy__lrXRiFfxCEO9UZ1i98u4Af12Zvtq3_l4etksIUBHaTmTXIplA0EgaY-VPyFT4QKiUJEqoWODkWuqDhmwZn_QTmM4vBkmlTuNpg-37Xf_HJHFcXZNEnAtS_PGp9lQqy8f3oabLN-huWwS2wC52gbdEN7BYyv3Rx8URKDvoAaOFihZ_Z3cL2ukJ4onyvJiQ9EfN_2tRjRNRYJKm-oYthHkqt8o61aNYguKU19XCQqEJ_ieTT77ml84Xjlww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r23
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/news_hut/70023" target="_blank">📅 10:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70022">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aefb92b64.mp4?token=DQNe8W-2TTqXs4rMSyjV9I6t4Fc5hSTkwKc2M3lsmvAO9p9bJAXCQmvNd_rTsZNTosCBdaZk0aaxPV7C_LJsKfhWfOsBjQPf4ccsur475VJBObCMQn7_0a5YFhWxfaXTFAxNqBv5VaZCvioaTwZ3E3M3FZUOIP_B2F51XoXepZlhHHtm_L-e2ZSukB3zZrTPZt6_0deJYeGlhXTvRU00gwdAW9NjKpBxYyuUOpwVjCWuQseHvI8bEr5UflMlKm6f75i1rGgp3wT_c05kHUjRH6fh6fZOBXMd-VRsc-WYRLN3ZV10rkoPn2C1Q14pO48y7g0OqxVlV4BJKSRdjZxDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aefb92b64.mp4?token=DQNe8W-2TTqXs4rMSyjV9I6t4Fc5hSTkwKc2M3lsmvAO9p9bJAXCQmvNd_rTsZNTosCBdaZk0aaxPV7C_LJsKfhWfOsBjQPf4ccsur475VJBObCMQn7_0a5YFhWxfaXTFAxNqBv5VaZCvioaTwZ3E3M3FZUOIP_B2F51XoXepZlhHHtm_L-e2ZSukB3zZrTPZt6_0deJYeGlhXTvRU00gwdAW9NjKpBxYyuUOpwVjCWuQseHvI8bEr5UflMlKm6f75i1rGgp3wT_c05kHUjRH6fh6fZOBXMd-VRsc-WYRLN3ZV10rkoPn2C1Q14pO48y7g0OqxVlV4BJKSRdjZxDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
اسکات بسنت، وزیر خزانه‌داری آمریکا، از اقدامات «بی‌سابقه» برای منزوی‌سازی اقتصادی ایران خبر می‌دهد:
«یک سال پیش، در ماه مارس (مارس ۲۰۲۵)، رئیس‌جمهور به من دستور داد تا سیاست "فشار حداکثری" را علیه حکومت ایران اعمال کنم و وزارت خزانه‌داری نیز چنین کرد.
همان‌طور که گفتید، ما حساب‌های بانکی، کیف پول‌های رمزارز و دارایی‌های آن‌ها در سراسر جهان را هدف قرار دادیم و جریان‌های مالی و پرداخت‌ها به رهبری، حکومت و خودِ دولت را قطع کردیم.
در نتیجه، در دسامبر سال گذشته (دسامبر ۲۰۲۵)، یکی از بزرگ‌ترین بانک‌های ایران — یا به عبارتی بزرگ‌ترین بانک آن — فروپاشید.
بانک مرکزی ناچار به چاپ پول شد و تورم عظیمی ایجاد کرد. سپس در ماه مارس یا فوریه امسال، ما جنگ نظامی (کینتیک) را آغاز کردیم. آن جنگ پس از چند هفته پایان یافت و ما از مرحله خشم و غضبِ تمام‌عیار نظامی، به سمت خشم و فشار اقتصادی حرکت کردیم.
🔴
بسنت وزیر خزانه‌داری آمریکا:
اکنون نیز به دستور رئیس‌جمهور، سطح این اقدامات را باز هم بالاتر برده‌ایم.
منتظر اعلامیه‌های بیشتر در هفته آینده باشید؛
چرا که ما قصد داریم اقداماتی را علیه این کشور به اجرا بگذاریم که در تاریخِ اعمال انزوای اقتصادی، بی‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/70022" target="_blank">📅 10:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70021">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5c4dd610.mp4?token=HYJfL2JzCXznGeRB5TpMr16FG4p_Z87_EglhI6XufpFVAuvxiJuLsFUT6_vzmaTHeRj1XmUst3pl6AB3NHMUgQYdmZtbWbeGdNMTiAFdgdm7qhc6sN1-jfFKiaUSTm6obEc5Hd3AzRSAcutxl_Sgak5LhFuOUblyLPjS7mTPJpjZHz9-1fEOzipVLkhOrkPGkp-hQOnErjJKaYDlz_Xcn40dqwpxh3m3lVGY1EsXolZhqgsJXG5WMgo9QhNsH_r7cn9K8xdEDtVHXpjbwsllIX4m5HfzHwZsHhBMW2ncVxm76hnKsBZgu62EPv3Ifd4XbDaoQSkW7_Ts9m9lN1H-zwkcZYtnunfm1s7DJUIbfLtyJ1ymY2MmB89FasNuK4LC2e2-RACxjDUpkXHp41wqT1KrY-gOGnIL4YZRCB3TSqkwAyJN6_RaxVoQSPu34X_b4pmyxLMBjiV0Wz7IBGg_S3ithwZEttOsmFCgeWLhZtqezL19X-CxJ2LvT4D2veUmKBo0j89WzlKsEEtIiSsI3h0TdtoI2kBQbaX0wbYMN-Bhh17JiUcEeDJ3shdPk-HqnDj9Yx_XErrv70zOKoDrl6jakul9cKR2KfJsmNWVBcRmv2TYqK9IBt0TqRTvjLIbILmzojw911e44V3iUkVSTQVKkKNK5f2CKWbC93AE5Ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5c4dd610.mp4?token=HYJfL2JzCXznGeRB5TpMr16FG4p_Z87_EglhI6XufpFVAuvxiJuLsFUT6_vzmaTHeRj1XmUst3pl6AB3NHMUgQYdmZtbWbeGdNMTiAFdgdm7qhc6sN1-jfFKiaUSTm6obEc5Hd3AzRSAcutxl_Sgak5LhFuOUblyLPjS7mTPJpjZHz9-1fEOzipVLkhOrkPGkp-hQOnErjJKaYDlz_Xcn40dqwpxh3m3lVGY1EsXolZhqgsJXG5WMgo9QhNsH_r7cn9K8xdEDtVHXpjbwsllIX4m5HfzHwZsHhBMW2ncVxm76hnKsBZgu62EPv3Ifd4XbDaoQSkW7_Ts9m9lN1H-zwkcZYtnunfm1s7DJUIbfLtyJ1ymY2MmB89FasNuK4LC2e2-RACxjDUpkXHp41wqT1KrY-gOGnIL4YZRCB3TSqkwAyJN6_RaxVoQSPu34X_b4pmyxLMBjiV0Wz7IBGg_S3ithwZEttOsmFCgeWLhZtqezL19X-CxJ2LvT4D2veUmKBo0j89WzlKsEEtIiSsI3h0TdtoI2kBQbaX0wbYMN-Bhh17JiUcEeDJ3shdPk-HqnDj9Yx_XErrv70zOKoDrl6jakul9cKR2KfJsmNWVBcRmv2TYqK9IBt0TqRTvjLIbILmzojw911e44V3iUkVSTQVKkKNK5f2CKWbC93AE5Ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حرفای مجری صداوسیما درباره حکومت پهلوی:
ما از دوران پهلوی اطلاعاتی نداریم اجازه دسترسی به آرشیو هم نمیدن
چون تو اون زمان بچه بودیم تصوراتی از پهلوی داشتیم که شخص محمدرضا پهلوی فردی خنگ و ابله و دست پاچلفتی هستش
خیلی از پهلوی صحنه های اغراق شده و کاریکاتوری تو ذهن ما ساخته شده بود
این بازخوانی تاریخ نبود بلکه فحش نامه هایی بود که علیه پهلوی نوشته بودن چون ساده تر و راحت تر بود
الان وقتی ما می‌بینیم که انقد روان انگلیسی فرانسوی حرف می‌زد محمدرضا پهلوی میگیم اینی ک میگفتین خنگول این بود؟؟
اون کشورای غرب رو تهدید می‌کرد با سواد و محصل بود و روزای کاری سختی داشت
میگفتن رضا پهلوی یا همون رضا پالانی شخصی نا لایقه ولی اون هیبت داشت ابهت داشت و از کف جامعه اومده بود مردم رو می‌شناخت
کسی که دروغ مینویسه یعنی از حقیقت میترسه و متاسفانه آرشیو از پهلوی نداریم ساختن برنامه با حقیقت خیلی سخته.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/70021" target="_blank">📅 09:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70020">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2h1OWI3sIpChgMnugW67Jh6QgUrEFagnynRTt3QT97G-1mDWroF8Iq_zdtnJ6YVr7M05TLR9Oi6eJ5Ffa56rNEYNYKcP4rSzqFRLFp0lRDKL5TqVockbbXyUIN0MfAIEydQwy2ZEKc_VQoWoHJKC0ZT295d1Gm403VvSUm1r-msp6_H0xI78j9kiv4teyBO53rl4otYqfSFcpL_SzRrEqrsWHvAYzc6iuT4tMZAY0aT4osgEc-dpT-DFNmac8cGHpVdU-HgIyRgst22wFpuJdjv-4-Z2vQWts5y8Gj4k5YXYMEnpaBFKI8wgCQOpRaV8M5ujjnrCRSHpH2I37bXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇱
شبکه ۱۳ اسرائیل: دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، به مقامات ارشد اسرائیلی گفته است که او پیگیر انجام حملات مجدد علیه ایران است؛ چرا که معتقد است افزایش فشار نظامی می‌تواند تهران را وادار به تغییر موضع در مذاکرات کند.
کوپر در جریان سفر آخر هفته خود به اسرائیل، خواستار حملات دوباره به زیرساخت‌های ملی ایران — از جمله تأسیسات نفت، گاز و برق — شد و اظهار داشت که ایالات متحده ممکن است در نهایت چاره‌ای جز ازسرگیری نبرد در کنار اسرائیل نداشته باشد.
موضع کوپر به ژنرال دن کین، رئیس ستاد مشترک ارتش، و همچنین دونالد ترامپ، رئیس‌جمهور، نیز منتقل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/70020" target="_blank">📅 09:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70019">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/70019" target="_blank">📅 01:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70018">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=GZ-BQqJubhi7EbwL2979754gvGVsudG6JM0mShYliFBJpIfwDJv3dpRBUYcvqRat5zeM_IxLbzewUsw0BpCJyssi_0qtlp9Jix7LTDuBAeNkQHpOvEQfU8A8W6GUMtzt4P1VXLxvhOWaEeeU7QGebyk0j_98NsbLrb9nEia3SUygX3MQo7aDVeZt5tfX3VctDWYysW72Y7YBimo_Kp4FMZ_H00ILAGMytRRmvp0s_rjjpwrVPYiJLnnXKkSMhsUmwXAh3gJHFTamlcJ6f0XHk-1hAShaBIVdzfcfUmFyBa71G7OB9vsqux5NepQExQmgDSHW51xFfnKI17JURrfiMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=GZ-BQqJubhi7EbwL2979754gvGVsudG6JM0mShYliFBJpIfwDJv3dpRBUYcvqRat5zeM_IxLbzewUsw0BpCJyssi_0qtlp9Jix7LTDuBAeNkQHpOvEQfU8A8W6GUMtzt4P1VXLxvhOWaEeeU7QGebyk0j_98NsbLrb9nEia3SUygX3MQo7aDVeZt5tfX3VctDWYysW72Y7YBimo_Kp4FMZ_H00ILAGMytRRmvp0s_rjjpwrVPYiJLnnXKkSMhsUmwXAh3gJHFTamlcJ6f0XHk-1hAShaBIVdzfcfUmFyBa71G7OB9vsqux5NepQExQmgDSHW51xFfnKI17JURrfiMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a22
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/70018" target="_blank">📅 01:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70017">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0J8Rq0PlguRrEgYQpHQ1xOjn13It-87v4Ipw87Qlq5KpL6c7UIwrB5neTetkUlOcNRlB9ERRYkc-ZAGVbVWtjEYbBIG21PfFseOP6rKUDF9jKslbAyGQq8HUvI54ey9Vyv-rgazyWVRlZlXRNLSg_q5mkas_PTqs-VFB-0ZuUoXtgIP_oosj1M6X87X0IyO0jKSkhvpPbxpweQUp2web2SZmF6NY9FtgL1hrUQMNFf5T002_1xHhn9E_9JbJb06dHYI3OWEV9P9WzdtPARDl3IY7bn7XnBGKG1435nmV6PRUY35O4RJnHxlquxqoEbiq_aargbr1TZi5avWnH7wGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
محمد مخبر، دستیار رهبر و عضو مجمع تشخیص مصلحت نظام:
راهبرد قطعی رهبری مبنی بر تغییر وضعیت به حالت تهاجمی در صورت عدم تحقق شروط ایران، بی‌تردید موازنه قدرت جهانی را دگرگون خواهد کرد.
با توجه به اینکه ایالات متحده ناتوانی خود را در حفاظت از متحدانش در خلیج فارس به اثبات رسانده است، پایدارترین مسیر برای دستیابی به نظمی منطقه‌ای و جدید، پیاده‌سازی سازوکاری اقتصادی-امنیتی برای تنگه هرمز است که مستقل از تضمین‌های نظامی واشنگتن باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70017" target="_blank">📅 01:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70016">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ed6d62f0e.mp4?token=PqY8yhTzDWw-DtEYuYHnzyswRrVHuOGoWC-3BerP63E9pAKNm3OdIO11CX3YXaoUGkdZyPG5tYnn3B7BlQedws5GC_tPThQlREyprMeQZViJaxU3fjkn8AorfYG_aKbATf-Pbgj5iS2C_PYl1OQWHEN3Lu8v4LzJpGi-BkzCnF--0-WTJSpbjWisgvQbi-35rNTOdug3XY64kMhojR_IcuYfUbXYazXhP4mA3Y9KouK6KY38DXJthW-rVz-9p55oF-c8mblc2pgCqikIEhFFs9irm-42s8j2eiftvAT2ha8nbfL6wjrfVP6Xw7HXf2jEPRaGvuI1ijMr9FnN-i5pgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ed6d62f0e.mp4?token=PqY8yhTzDWw-DtEYuYHnzyswRrVHuOGoWC-3BerP63E9pAKNm3OdIO11CX3YXaoUGkdZyPG5tYnn3B7BlQedws5GC_tPThQlREyprMeQZViJaxU3fjkn8AorfYG_aKbATf-Pbgj5iS2C_PYl1OQWHEN3Lu8v4LzJpGi-BkzCnF--0-WTJSpbjWisgvQbi-35rNTOdug3XY64kMhojR_IcuYfUbXYazXhP4mA3Y9KouK6KY38DXJthW-rVz-9p55oF-c8mblc2pgCqikIEhFFs9irm-42s8j2eiftvAT2ha8nbfL6wjrfVP6Xw7HXf2jEPRaGvuI1ijMr9FnN-i5pgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
📰
آیت‌الله ونس در گفت و گو با فاکس نیوز:
قیمت نفت امروز به شکل چشم گیری نسبت به روزهای ابتدای درگیری کاهش یافت.
ایرانی ها غیرقابل پیش بینی هستن و گاهی به تعهداتی ک میدن عمل نمیکنن.
این بحران با تقویت موضع آمریکا و با جلوگیری از دستیابی ایران به سلاح هسته ای پایان میرسه.
ثبات تنگه هرمز یعنی ثبات قیمت نفت و گاز شهروند آمریکایی.
ابزار هایی داریم که ایران رو وادار به قدم های بعدی بکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70016" target="_blank">📅 00:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70015">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ef24fbad.mp4?token=GAG0m2DOeZ_M8uNz5POGNwxjFtzfhj2HmWZB1DJkWRJ0hGLgj2UrbT6yCkcBqnClcv5F9cEYnjb0EKqYbOSSj_k2HT5ddU6AJX30LF8gUCZpy6hktXH748vZQWAD2ildkGa3T281tKeKMXOfXAZaa_zMcJxX4dEhTAw7tk1GLjeHjFw1RKcKBdhERVwcVjQtQLKN0KZofgBwtpKbjaTxHdBn7Frhb6QrzuF08VaupN5bYB1MwJ7auuM4TNP0ykDr4SuKGvA0UqHoJL_uLFiCVbHnRiitM3xkB-hx4hnYdX2271Ytb6CebnBqN4wmSbNkgtgj-Td3xcsn5FVXN0K3Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ef24fbad.mp4?token=GAG0m2DOeZ_M8uNz5POGNwxjFtzfhj2HmWZB1DJkWRJ0hGLgj2UrbT6yCkcBqnClcv5F9cEYnjb0EKqYbOSSj_k2HT5ddU6AJX30LF8gUCZpy6hktXH748vZQWAD2ildkGa3T281tKeKMXOfXAZaa_zMcJxX4dEhTAw7tk1GLjeHjFw1RKcKBdhERVwcVjQtQLKN0KZofgBwtpKbjaTxHdBn7Frhb6QrzuF08VaupN5bYB1MwJ7auuM4TNP0ykDr4SuKGvA0UqHoJL_uLFiCVbHnRiitM3xkB-hx4hnYdX2271Ytb6CebnBqN4wmSbNkgtgj-Td3xcsn5FVXN0K3Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خورشیدگرفتگی دیروز از نمای کابین خلبان هواپیمای A320:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70015" target="_blank">📅 23:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70014">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c94cf4401c.mp4?token=grueWc6SAv8CE38LBLQQhkP9ub_qWcRYoGzBAHG23RoeDje-s-Ky8vxeYCZzSmjmdbE1yjxrDrW5q9IaXE1V20VWZuoQ6VL3kjWoN4PzLTABHBZjCyP-Nun5qe_dCEJ_CyOQObJxUT-TDkxcKT0JqwqbJTqr_LZDGQCVVruWweVtTCYI72TqvGblhMQGAkNqfgJ9PlcMkxGdWGOZBWo-nk1eXk81XVrNrtbHu55wQu7SWKhSffI4Sz7-sfXPfLY8RRJ9bxaHfnqwxUXXz7B5BnMihA6u-18I7VX7zLECMWOM-8wQrjXCalFk-j-nmQ0KI_-_YNL6FK32hsR2Sle55g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c94cf4401c.mp4?token=grueWc6SAv8CE38LBLQQhkP9ub_qWcRYoGzBAHG23RoeDje-s-Ky8vxeYCZzSmjmdbE1yjxrDrW5q9IaXE1V20VWZuoQ6VL3kjWoN4PzLTABHBZjCyP-Nun5qe_dCEJ_CyOQObJxUT-TDkxcKT0JqwqbJTqr_LZDGQCVVruWweVtTCYI72TqvGblhMQGAkNqfgJ9PlcMkxGdWGOZBWo-nk1eXk81XVrNrtbHu55wQu7SWKhSffI4Sz7-sfXPfLY8RRJ9bxaHfnqwxUXXz7B5BnMihA6u-18I7VX7zLECMWOM-8wQrjXCalFk-j-nmQ0KI_-_YNL6FK32hsR2Sle55g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه وایرال شده یه زن باحجاب با یه دختر بی حجاب توی میدان علیخانی اصفهان:
زن محجبه: اینجا همون جاییه که معترضین، مامورای بدون سلاح رو به قتل رسوندن، نظرت چیه؟
دختر بی حجاب: من خودم ۱۸ و ۱۹ دی کف خیابون بودم، ولی اصلا این کارای وحشیانه رو انجام ندادم.
پهلوی مردم رو تحریک کرد بیان تو خیابون، خودش جرعت نداره تا ترکیه بیاد، چرا باید طرفدارش باشم؟
مشکل ما داخلیه، اصلا ترامپ کیه که بخواد دخالت کنه؟ اگه یه اسلحه به من بدن، با اسرائیل میجنگم.
آخرشم یه دفعه متحول شد و اشکش در اومد و باحجاب شد
🥹
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70014" target="_blank">📅 23:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70010">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONoBqcWRYNG-eMu3ie1Zd1asoX15_ow2AlVHLC37S_fJ7k_ZSDHu9NniJlBZ8Wj_O28D9G8B4OW2TVSDxzjHW4oW1VDemPnHEl1fROcdrCyru1N6eKnLNjJGSesNx47kD9CMAtEuQVZNgFXS_gCl8ju-B8bo4XtSOrRjRKk23LB8uxILK_fM86cFJcGKITz1OyVBnHy7MiW8VyhR94E6ceFRDbi45k6coBdAJQkBrQNeX-EXgtpe3kYmKGnyGNBUeTYKBtCFYm2a7MF7x5z8fTAaa0Nyw8743OcBeE2v445OW7fGVzyMv2c6ag8O2fhKvxf7nguP2WRE7N5-utceBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LM9e-pn-n8QohzLnh1pQPMtE3cmuLY2TRlQKON6RzCL0zvkKmNuhpiVpHrwzdoW-cwDLTEHc7Zfk0AqpCX9CsGWUgzNP8QxR7u-Hu27NO_iapu4Gc-ojbTw_3azx7yuNdE1VyJ9ZouLAiqouy6eG9NZFP5cYbCeb-1MljO7oVWbDIQfcN_-zZ2FHkYzDhI3XWGr--o0bdG60K2Ln0rChvHUa7fcjaHv29z2gwwRGm4sHS3-zrd6bmvcvLiM-XHWOJUewRXeKUf9Mbi9QS0dYh4eo5EdnR2Xv3FAljHF9QEvbviYMhzpma9VLt7TNT6xLU3NXbQEkrvnpPvu9Uh0yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T__-2BUel3DqUwAmE1q7A-zzOC2PseFUlQhiJBOVdYxsbfwRHWP78LspM2v3SnrxXrCli_FZ4xm7COP_kOV7Qw4TMnk9l1X-6IWVU1R2TT0QYg16yPAPtdoXhazSp9a_XPGCd-6hofS0GvFDadtRbO4ZTK_EGBuhbFc_r4e-NKxOAzL6ydyRL8oVETeGVYd0P8MBy5hTsYi7kOv0xIh0YFcnEeFgVE_yPa1VvLpIpqbgMK6uQ2SCrzzNXHwdre1yOswXs4lty0WVW_j4GXMVtym1CeM_AnNW7ZUnXypkEEm68SwndKAGj9kmrQJEhzMpeq2rkThR2grEB9GU5X82QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f63b04c02.mp4?token=M1nkmh1wz1ejtbWOGyHytu7Q2Ty8ivyYclpFYVFQ5uw1yJ7VpZKrxW1NRClqwsTllW76P_4DAieBGgC9yjhBj00f_gxYnwaFvtCGnn0Z1v-AU18lLwkTyQp2WJmQuI17u9en4dybms-qrrN3mpjwYPDPpu8BE83T9dQBuEOwwn1vnwzVrHB5JZLrXrkBCXsUFHuulZ22eI6pKnIdEMoyy7KV-4cQEF74HFwuYiaT1lBy8G8gNWN3AQyLgHc8dUnNwyqGRJ7X4GcJK6BkUuEMCENgHNpFd_2msV9j_WhQrR5LOv6JrX0KwoacDMiJZz9i7BPaF8HXtnTKNFqmx_X66g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f63b04c02.mp4?token=M1nkmh1wz1ejtbWOGyHytu7Q2Ty8ivyYclpFYVFQ5uw1yJ7VpZKrxW1NRClqwsTllW76P_4DAieBGgC9yjhBj00f_gxYnwaFvtCGnn0Z1v-AU18lLwkTyQp2WJmQuI17u9en4dybms-qrrN3mpjwYPDPpu8BE83T9dQBuEOwwn1vnwzVrHB5JZLrXrkBCXsUFHuulZ22eI6pKnIdEMoyy7KV-4cQEF74HFwuYiaT1lBy8G8gNWN3AQyLgHc8dUnNwyqGRJ7X4GcJK6BkUuEMCENgHNpFd_2msV9j_WhQrR5LOv6JrX0KwoacDMiJZz9i7BPaF8HXtnTKNFqmx_X66g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🔥
🔥
🔞
با انتخاب کاربران کوماتزه یا همون Comatozze اهل کشور روسیه به عنوان بهترین پورن استار برتر سال 2026 از نگاه طرفداران انتخاب شد
ویدیو های کوماتزه بر خلاف دیگر پورن استارها، فقط با همسرش ضبط می‌شه و بقولی به همه نمی‌ده!
بخشی از ویدیو های معروف کوماتزه:
🔗
پارت یک ویدیو ها
🔞
🔗
پارت دو  ویدیو ها
🔞
🔗
پارت سه ویدیو ها
🔞
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70010" target="_blank">📅 23:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70009">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=E-ioqqTQXH6XiGbgxW2tA3FwRJI7ahgwSz3XDtM8x7uSsHGjPca2-RZefHYwNxPXvJePNb4yekavvUfMcg8gebNK3JFVnliX6gV6eN6vNZlqvPlw4IjQWhDn2ohg9AEWfAgaC4g0yV6p4d4bFeTOQsw7JkxNULTe888h52QGTDeVCmSjlcT_m87xPe3qYmb0s1Nl_oHTyhkXGumdpehdgVoJaX9DtsqXeLnuzuUnTm5SqKQ7mafSKYSk5Ef8H3QOLlpzrInTe7iH6SyESeAsv0VdA5rk31rfZtpNEY7UIJBpU7DPiLJ-JzlFjO0qitLF4gCejYT4RJZ6f1hODZflxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=E-ioqqTQXH6XiGbgxW2tA3FwRJI7ahgwSz3XDtM8x7uSsHGjPca2-RZefHYwNxPXvJePNb4yekavvUfMcg8gebNK3JFVnliX6gV6eN6vNZlqvPlw4IjQWhDn2ohg9AEWfAgaC4g0yV6p4d4bFeTOQsw7JkxNULTe888h52QGTDeVCmSjlcT_m87xPe3qYmb0s1Nl_oHTyhkXGumdpehdgVoJaX9DtsqXeLnuzuUnTm5SqKQ7mafSKYSk5Ef8H3QOLlpzrInTe7iH6SyESeAsv0VdA5rk31rfZtpNEY7UIJBpU7DPiLJ-JzlFjO0qitLF4gCejYT4RJZ6f1hODZflxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه مرد روستایی در چین با استفاده از تکه‌های ضایعات فولادی و فقط با کار دست، یه بازوی مکانیکی غول‌پیکر ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70009" target="_blank">📅 22:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70008">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⏺
🇺🇸
پیت هگست، وزیر جنگ آمریکا، گزارش‌ها درباره وخامت شرایط و بروز بحران سلامت روان در ناو هواپیمابر USS Abraham Lincoln را رد کرد و گفت وضعیت موجود «کاملاً نادرست بازنمایی شده است.»
او تأکید کرد که در این ناو، «هر چیزی را که در توان داریم در اختیار خدمه قرار داده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70008" target="_blank">📅 21:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70007">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
کانال13 عبری:
برد کوپر، فرمانده سنتکام، به مقامات اسرائیلی گفته است که برای انجام حملات مجدد در داخل ایران تلاش می‌کند و معتقد است که ازسرگیری جنگ می‌تواند موضع تهران را در مذاکرات تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70007" target="_blank">📅 21:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70003">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7qtNuN1XxPxIgpjGKtit_nD2ltwLhnG-0xL-NKDhv_IKM9ZX40nC0c6LBcF4VJXfyNzo4CRRxQ6s103ZvHWfn8T4Em8_G2JTWWmfdPVqRER5NqOEc6ZPpAJw-EMvrl8lWzR3mr4BLoeOMAKGWmnc1KhURdvnE_JFaTe5CgI4c0n74Wm8l4K4jVGfchLOrKfLPqAMbLDRDqktoZT1LBiFK2ZXSSHZOUKa9vKAjeC1otRDT_uRuo1S0aIBto0E7-_AejGnt0iX5NPrnxaoLQJ7L1FuQABfukaoWtI3czOxcwJctMbCGT4Lhp6b3c4a3HkF8XYnTlNC5B_v8kEblKzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c5b26c54.mp4?token=UpfcJSxWtMvJdg7K9HsUySPfoSJBEpHTZt6cAOCg-zCY7fL-FNVSh8hIR4IoIr3NR_tvresomAGyt9506ws0PXioxidoM_Z2OVQidjuHr_itXB4RN9try-djtc4JEXN5qEjzcm3_jKL2EvYGtRUAaMKIquAWujFW5YPAiPWU8x2b7lwR4qgPonuczpnVoURwyFqiUxJx5vSuAuVxTh8vJ85nf47Ap9nmiza6lRwCyPq0fx0CwRWxMH01O0sEEVb4IlicpcqNrq1p8Nyqb-Pn4dCtYtjo0qZHp2dayhG8-bbkc1LRfd1s6rzziz0qBSc63kict-HeuIKmeNDWYwqAvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c5b26c54.mp4?token=UpfcJSxWtMvJdg7K9HsUySPfoSJBEpHTZt6cAOCg-zCY7fL-FNVSh8hIR4IoIr3NR_tvresomAGyt9506ws0PXioxidoM_Z2OVQidjuHr_itXB4RN9try-djtc4JEXN5qEjzcm3_jKL2EvYGtRUAaMKIquAWujFW5YPAiPWU8x2b7lwR4qgPonuczpnVoURwyFqiUxJx5vSuAuVxTh8vJ85nf47Ap9nmiza6lRwCyPq0fx0CwRWxMH01O0sEEVb4IlicpcqNrq1p8Nyqb-Pn4dCtYtjo0qZHp2dayhG8-bbkc1LRfd1s6rzziz0qBSc63kict-HeuIKmeNDWYwqAvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
این شما و این قوی‌ترین دختربچه جهان؛
🗣️
لوسی میلگریم دختر 9 ساله‌ای که تو نگاه اول خیلی ناز و گوگولی به نظر میاد، موفق شده رکوردهای زیر رو بزنه:
- لیفت : وزنه‌ی 81.6 کیلوگرمی
- اسکوات : 67.5 کیلوگرم
-‌ پرس سینه : 33.5 کیلوگرم
لوسی پاورلیفتینگ، کشتی، جوجیتسو و MMA کار میکنه و تو کشتی هم جدیدا داره پسرها رو زیر و رو می‌کنه...
نکته جالب اینجاست که این بچه فقط 27 کیلوئه و کلا 127 سانته، یعنی چیزی حدود 3 برابر وزنش رو لیفت می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70003" target="_blank">📅 21:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70002">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_cEJxL_bMYVKaIIbWLp6n1Rh2x3U3S36RlvvUVXsMeBEI1DK37x93HlWYu3fnzBnIWBlM9yyk0U7chIXYlOlHBxLF6EGlOJ7AfbwPuGo92NzxD178IGGVEA4_VftHLWK3mor6tlJ7XBvyQZsw9VWzpslDdU82UTbX4Ovx1RUYQ3wPDfBnhK7iO7PmHnVb9QnkqjAS_kanaBFTV7TfYeVYtAwIjUVJtOFFRnim2g0LBIoGC77xCh5BI-A9Iw1bi-U-OWGlKsXXfQYGZgkpGXBphZIQw5krDT-Ddy3dhSG3S1Pfmh_dOOZwR_pOeuPPBV3x6QuN1cSMm8odfmDyKqbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
فرماندهی مرکزی ایالات متحده از برنامه‌های خود برای ایجاد نیروی ضربت فالکون استرایک، اولین نیروی پهپادی تهاجمی چندملیتی و چند دامنه‌ای خود خبر داده است که پرسنل آمریکایی و منطقه‌ای را برای بهره‌برداری از سیستم‌های تهاجمی یک‌طرفه در هوا، سطح و زیر آب گرد هم می‌آورد.
این نیروی ضربت به رهبری فرماندهی مرکزی عملیات ویژه ایالات متحده، بر اساس نیروی ضربت اسکورپیون استرایک، که پهپادهای آن قبلاً در عملیات علیه ایران استفاده شده‌اند، بنا خواهد شد.
سنتکام اکنون رسماً از شرکای منطقه‌ای دعوت می‌کند تا با هدف ایجاد یک قابلیت پهپادی تهاجمی یکپارچه در سراسر خاورمیانه، به فالکون استرایک بپیوندند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70002" target="_blank">📅 20:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70001">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e87ab5b1d.mp4?token=ESw-GoFk_MWD4hAWEraJeCbrZdfyuO6H_XsbMN0psoA4vcmP4_MMKbMo8f3RTBXvWKROrEGHWRROBIMdVdAjmEksHmjTG7wDOOr-2NEYOp8SmA3ySLyMk-qF4jxxNBh043THWQ5yewf-R1EdR_TYW8ENsQmkIwrXzG2RgvBX6NkIEpxLX1g4AM9mobEMVEJkuZTosRN7eb86ci_nBRc4zEAz4TyvY6Kcuh2_lcKi2a_odKQMP9n12n05iEz5cFqtbP3PnuRDXPPiA0p0HNp2V_s_fFFsJ_10zciJEIZ71nRtX5PJS3HmZbq-s-ZvXw3GL2UOw0c-MsaVcKcTquQhvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e87ab5b1d.mp4?token=ESw-GoFk_MWD4hAWEraJeCbrZdfyuO6H_XsbMN0psoA4vcmP4_MMKbMo8f3RTBXvWKROrEGHWRROBIMdVdAjmEksHmjTG7wDOOr-2NEYOp8SmA3ySLyMk-qF4jxxNBh043THWQ5yewf-R1EdR_TYW8ENsQmkIwrXzG2RgvBX6NkIEpxLX1g4AM9mobEMVEJkuZTosRN7eb86ci_nBRc4zEAz4TyvY6Kcuh2_lcKi2a_odKQMP9n12n05iEz5cFqtbP3PnuRDXPPiA0p0HNp2V_s_fFFsJ_10zciJEIZ71nRtX5PJS3HmZbq-s-ZvXw3GL2UOw0c-MsaVcKcTquQhvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
چرا ایلان ماسک ثروت تریلیون دلاری اش را نمی بخشد؟
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70001" target="_blank">📅 19:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70000">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a534ae94.mp4?token=PvPBz8ol60_nXIElsMbjjCJfEsy4IeAV6fB76nCzVPOnJUUtKx4Sn7eKqNMfoEJxrP0DrTFajdMbbe0eNdMAR7H3zABstv5ggU42cUxmqDLtUnmPP5gXgFQVGBu_2NrlDWBkYZpEkhNzWQ3AkYoUxgSS7d_4eRKQs-fGKbyFZrYEJgRlv0_-BfEJ6wT6VKSslyM1_I0f2vMyBMTpVczYM7llOTUOkZooZumPdSWGb9Ul3TVotlthZImw09ZvErn7WJETIfLmjGED6Ttt81biN1kC1Yho2uB0Xa1rJ-zfR13HHyIooqXKigTvuESrDkjtIJQrbVApr4GhBqQwtRQ8jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a534ae94.mp4?token=PvPBz8ol60_nXIElsMbjjCJfEsy4IeAV6fB76nCzVPOnJUUtKx4Sn7eKqNMfoEJxrP0DrTFajdMbbe0eNdMAR7H3zABstv5ggU42cUxmqDLtUnmPP5gXgFQVGBu_2NrlDWBkYZpEkhNzWQ3AkYoUxgSS7d_4eRKQs-fGKbyFZrYEJgRlv0_-BfEJ6wT6VKSslyM1_I0f2vMyBMTpVczYM7llOTUOkZooZumPdSWGb9Ul3TVotlthZImw09ZvErn7WJETIfLmjGED6Ttt81biN1kC1Yho2uB0Xa1rJ-zfR13HHyIooqXKigTvuESrDkjtIJQrbVApr4GhBqQwtRQ8jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش جانشین فرمانده انتظامی به قتل حمیدرضا رجب‌زاده:یک اتفاق فردی بود مثل بقیه مواردی که در سطح کشور رخ میدهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70000" target="_blank">📅 19:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69999">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:ایران به کشور های منطقه اعلام کرد در صورت مداخله سوریه در پرونده لبنان، به سوریه حمله گسترده‌ای خواهد کرد.
خب ما بهشون هشدار میدیم که هیچگونه دخالتی در پرونده لبنان نکنن.
اگه گوش نکردن 100هدف در سوریه رو ویران خواهیم کرد.
این اهداف استراتژیک خواهند بود از جمله کاخ ریاست جمهوری سوریه که میتونه هدف قرار بگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69999" target="_blank">📅 19:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69998">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69998" target="_blank">📅 19:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69997">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkG2da5xKHyZKeI25eJe4g91qx_NcK9ainNoTocVPH9SBW4QWlVgqNptSH16HJ8d0jroC4XT3i2twpGRSHAeXXUU27cOMo-rhob1D3P-jXnHPFsvuuHfUmgvALNSZZ-UZkQkwZ50ASynCB71Y1I0orC9W58xvJdnFDINOUK-UfkjT4Gufn0jjwbnPf-de4KvQVLhj-V_oJT-yQZcgF5R3wi_iFDrfIbopoAoP6Lz4VP4xc6A4knwY7xvm5IbNm1t3jvX13wsGI9LRXb1mKy3C5s-6VCMcI9O4NaHQHovjaNLQKDCi3a0vDZtMhoV0kjkjaqgsfVng5v4bRwbSZ2R-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g22
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69997" target="_blank">📅 19:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69993">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd8b0a970.mp4?token=ZDaK4ZOKFPpuyfivpgutrb-PMNWMXBWeiP3L4Mfctd9oSDwYPCRToau6xD3AlYEh2fTbegy_5dFXOEOhpE4fO846vQ-C37IKAtkkc6zwNQZ7UdczVwFfCzJfeIdt0TdtI02ZqpAvp9L87IV98iZR1bMfVLbfDH2LjOJ_lmB7HJOlc21QceXKd77uaUu5lAlriMSxUw3ZEp8wIz0Md2YkX9B7AvLsqvcx5_FPXanPEqQz5xFxqHMgT3FDzQ5nxWOj5l76ylgr5DiNZFTe66CixVHCs77fv6hIBzkQxCHkrZGvvdNv-BK0TsHEatcoa1ypATNyLklcS3XiVI-7r26EfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd8b0a970.mp4?token=ZDaK4ZOKFPpuyfivpgutrb-PMNWMXBWeiP3L4Mfctd9oSDwYPCRToau6xD3AlYEh2fTbegy_5dFXOEOhpE4fO846vQ-C37IKAtkkc6zwNQZ7UdczVwFfCzJfeIdt0TdtI02ZqpAvp9L87IV98iZR1bMfVLbfDH2LjOJ_lmB7HJOlc21QceXKd77uaUu5lAlriMSxUw3ZEp8wIz0Md2YkX9B7AvLsqvcx5_FPXanPEqQz5xFxqHMgT3FDzQ5nxWOj5l76ylgr5DiNZFTe66CixVHCs77fv6hIBzkQxCHkrZGvvdNv-BK0TsHEatcoa1ypATNyLklcS3XiVI-7r26EfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طغیان آتشفشان در جزیره سیسیل: بسته شدن دوباره فرودگاه کاتانیا به دلیل خاکسترپراکنی آتشفشان اتنا
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69993" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69992">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
تو برنامه عشق ابدی ورژن صربستان یه پسر بعد از اینکه توسط ی دختر رد شد سعی کرد دختره رو خفه کنه و بکشه که در نهایت نیروهای امنیتی دستگیرش کردن،بعد از وایرال شدن این حرکتش الان مردم سراسر جهان خواستار این هستن که برنامه ی عشق ابدی بصورت کامل جمع بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69992" target="_blank">📅 17:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69991">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766cf940aa.mp4?token=ehNHtC1BjmPS47JkS0lCLZxV_O4VcPBtAs7t_72ua40vNaXV5GWp61QEKSz3nDShb3aiFT9HCrDHzNzQIAYWK6PzCdk_Hw4ScKqdo71hqqTfwVmUu4VsZSV6hhFVF__iM4bUGKctKX3Ay-4qhN88U6M93zuqrlgeAhSnPx6oeIqFAhbOAvtw5CLfee4oK8orUgheTkODCFdH3MVSyh9oKl2d63rMSOA_sbOCq9D4MSdgz6t_XVNOQqLaO6jpllWwz2j1rL0DctiNrzu0xrTKaQjugL60ooauNBDDMDpuruYFNPoSBcfh0igKZr90BLzofDZxJ9PTFoqThU2BovM77Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766cf940aa.mp4?token=ehNHtC1BjmPS47JkS0lCLZxV_O4VcPBtAs7t_72ua40vNaXV5GWp61QEKSz3nDShb3aiFT9HCrDHzNzQIAYWK6PzCdk_Hw4ScKqdo71hqqTfwVmUu4VsZSV6hhFVF__iM4bUGKctKX3Ay-4qhN88U6M93zuqrlgeAhSnPx6oeIqFAhbOAvtw5CLfee4oK8orUgheTkODCFdH3MVSyh9oKl2d63rMSOA_sbOCq9D4MSdgz6t_XVNOQqLaO6jpllWwz2j1rL0DctiNrzu0xrTKaQjugL60ooauNBDDMDpuruYFNPoSBcfh0igKZr90BLzofDZxJ9PTFoqThU2BovM77Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
تهران نوروز 1356:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69991" target="_blank">📅 17:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69990">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f015c6551e.mp4?token=u2T4Obxv79ZxSbcq8dQ56ZQrQJTX4bgCcNH6Mf8cr8RHEy-DOXMk1VCzsPM2Vpk_bp2q_X_DLxYK_l0mKl6wf8Xl3fZdYQVvWnR2AbkW0BcNHC1McMz_NaJVbVM0sl3ud-IC0cB_ie1FvapP2P_WDs5WgQXWwzTXjilrP3sr3JrIkCtpoCGtgJCg1iN5hduI20Is0_zyH2ywJHgOtfXFBrJTB7Du8m00_V09RqaOLeXdj9g31XVFffzoAkGb4hdw53cwx2P3TP3DvS47zZWUTCIPd4-ccgo5GNmLV3T9Run77Jt5DveLJTQKThkMM_qc6clnbFlEROS37hYQlROqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f015c6551e.mp4?token=u2T4Obxv79ZxSbcq8dQ56ZQrQJTX4bgCcNH6Mf8cr8RHEy-DOXMk1VCzsPM2Vpk_bp2q_X_DLxYK_l0mKl6wf8Xl3fZdYQVvWnR2AbkW0BcNHC1McMz_NaJVbVM0sl3ud-IC0cB_ie1FvapP2P_WDs5WgQXWwzTXjilrP3sr3JrIkCtpoCGtgJCg1iN5hduI20Is0_zyH2ywJHgOtfXFBrJTB7Du8m00_V09RqaOLeXdj9g31XVFffzoAkGb4hdw53cwx2P3TP3DvS47zZWUTCIPd4-ccgo5GNmLV3T9Run77Jt5DveLJTQKThkMM_qc6clnbFlEROS37hYQlROqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سامانه پدافند هوایی خودکششی بسیار کوتاه‌برد گیبکا-اس، که بر اساس یک خودروی زرهی اصلاح‌شده تیگر ۴×۴ ساخته شده است، در حال انجام تمرینات آتش واقعی دیده شد و پهپادها به عنوان اهداف اصلی در آن خدمت می‌کردند.
این سامانه از لانچرهای سقفی استفاده می‌کند که قادر به شلیک موشک‌های دوش‌پرتاب ایگلا-اس یا ۹K333 وربا هستند و از موشک‌های زمین به هوای ۹M336، ۹M342 یا ۹M39 استفاده می‌کنند. این خودرو می‌تواند چهار موشک اضافی را در داخل خود حمل کند. لانچر آن دارای قابلیت چرخش ۳۶۰ درجه و برد ارتفاعی از ۵- تا ۸۰+ درجه است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69990" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69989">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">📌
فقط ۲۴ ساعت عضویت رایگان باز شده از همین امشب چک کن ببین چجوری میشه پول دراورد
💵
💸
🛒
این فرصت محدود رو از دست ندید
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69989" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69988">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=Wq5U8hsquDI-u7VdiLCP1eTI0H2FfQ5-YgpJO4ggxhQezmblp_f_V0Z9Wwf3LbNugDqqWJVx7EMY5ERYoCxv3CtiQ__MyjoMFFBYzRvbYfF514VxIr2k3k99dAydamdC90BkP4HW6IPq395aCEzze9B2oCRoxdepjDKc9XLQPuS2Mmn8lPA00YMIgvX_pbGEB5erAoTS7fUgQ5E-QQjIx9E-oPFs5-i0adHfrhyvfrClOwLUMIVO4S05_MA0g3PHwuWlEAqOZDrZ8aOGG0c789BGSEEk-EPKGCmIb022T6hFpxjDTi86sKQg0iuh1gWyz_eYWQj7k1moCLH3_V5ZWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=Wq5U8hsquDI-u7VdiLCP1eTI0H2FfQ5-YgpJO4ggxhQezmblp_f_V0Z9Wwf3LbNugDqqWJVx7EMY5ERYoCxv3CtiQ__MyjoMFFBYzRvbYfF514VxIr2k3k99dAydamdC90BkP4HW6IPq395aCEzze9B2oCRoxdepjDKc9XLQPuS2Mmn8lPA00YMIgvX_pbGEB5erAoTS7fUgQ5E-QQjIx9E-oPFs5-i0adHfrhyvfrClOwLUMIVO4S05_MA0g3PHwuWlEAqOZDrZ8aOGG0c789BGSEEk-EPKGCmIb022T6hFpxjDTi86sKQg0iuh1gWyz_eYWQj7k1moCLH3_V5ZWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💯
تنها کانالی که حتما باید توش عضو باشی
✅
چون راه پول
درآوردن رو بهت نشون میده
📝
حتما آمار کانالشو ببینید فعلا به مدت محدود عضویت رایگان باز شده فقط تا پایان فردا شب
🚫
⚠️
نمونه آموزش بازی Apple of Furtuneکه سودش تضمینیه رو براتون گذاشتیم پیش بینی های معتبر فوتبالی هم دارن
z22
:
📶
https://t.me/+MT03hkV78q9kMTc0
📶
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69988" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69985">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcmagH-lRxxRIzXaBUeFnmvYSVcJXHxQpTYYqYqD8h8dLz_VhAFKP1rK4TTk5bwuSUSZ9zTUFCDNfOiJVRj2tUp29vM3gDK6TWAtUOOFFsa99zlJfAjBva7X5Pu1bW8Z3u8uF9GPbSpu5lHY4hzQiFiiU0zO5du0npCdaFcj6Sj656iQLO0QAaNaohkAoPFsXmA08IUvlQ8AgE2E0Lv_XUeY0B43-nWWmuMORKmxVrKEKi_kUuRDjk6gNPttWPXiWgRMVS7eEtOZKiOtBrvUkTQ1ik9qqnMnHgz0_lTBG9cdtY4fNESWxe-Tfl1EJSrN5ABM9VicRXAIKvvce-r67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKVc7WUlW5pNAtLXCWu6dRBFCDqZaRPEziUd4HyTs4a6fRALj2V5gcmaiMbXdEBq5MkQyKG-iiTTub3D7nK6D0_N_ofOUVNBsythzfH_XrFCvUvlddMQnscWIOCrH-LEkINUC7QlFGd6xca-IxB1OnXf_49HGKyZvEYheQkCjbvpLIu4VEcJCEqi4Cf3tFgcO6ISlIwKiSvEr_qZtuTgkBncXsyWXh9jXCty-Zm6Jx7Bdruk3neSu4m5AY7C9_iqyWFpxWeevp9aaPL20In_-NNhTJagyyHSbaPZUM8JXcpLwJ8kPNpaHpAY-Qq33uQbh_s5dk-liB6z_CE20JEeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWUg_NKvR8EiV9oDsAnTtPLJB5Wq6O_o6EZYYrz9TomxDZJFCAXqNcYx9xgsjhcsAITga4hnEDy6H4uBfLx4xW7IyhNLzzGE7UlmNjFrefNWAUHSxg5KG73484abzXGLFLB4d1pcLXSHYcQjzRedKWNptCwbdiLpBZkYFQ9PONumNUmelzOy3nSHKdVTr2AwAtkNOswb0EWxihvKtfRLtcxqs42kKe-odLXj4zTtSTsgjybo0h9ahmGlfOae0Kt6dNbobbAnE5gWtfsmLg1Y6qrE6TGm3qUgkR7skE69-7vp0_wcLNJJZQiUfBbwBkhHccsAWMA6hwDZtZgJ2brDYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
❌
#فوری
؛ناوهای جنگی یو اس اس جورج واشنگتن (CVN-73)، یو اس اس شوپ (DDG-86) و یو اس اس رابرت اسمالز (CG-62) از تنگه سنگاپور عبور کرده و در حال حرکت به سمت خاورمیانه هستند.
ناو جنگی واشنگتن، ناو اصلی گروه ضربت ۵ نیروی دریایی ایالات متحده است که به طور دائم در منطقه هند و اقیانوس آرام مستقر است.
عبور از سنگاپور به سمت غرب، این گروه را به اقیانوس هند می‌رساند و مسیری بالقوه به سمت خاورمیانه را بدون نیاز به عبور از شرق تنگه مالاکا در جهت مخالف فراهم می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69985" target="_blank">📅 16:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69984">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961a7bc8c4.mp4?token=lyenlJF_hcD7GOT6hzaRDtCahuMniEISSWl1sWZG9Lqh1szjAz2Tzl_OQ3rk4ALiECnRW5nV3bT0s8MdS4GmPC49PJ-l4CSdbmMlwj8ujDlk_nIBd-TfvTRUQ_OvJujaMewX5m6AgOg2NQieT4mbdeiLDGWWBbEtr4hveGj7LUgI7gd7daNW7JYhPsw5a1C1Pa8dtIa3AjRUnzDt8wgrJSs9TxhjeN5koZGhQfFRPzuUfGv-Efyxpe_N4OIqmnWtu91I9zDSknJvkrdwYYXorsY64QsJBi_BUBi4jWuc4ICfHCw-Oa5ZUqm22_SNnZ6vm24NcSD0KJSCNTR66mQGDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961a7bc8c4.mp4?token=lyenlJF_hcD7GOT6hzaRDtCahuMniEISSWl1sWZG9Lqh1szjAz2Tzl_OQ3rk4ALiECnRW5nV3bT0s8MdS4GmPC49PJ-l4CSdbmMlwj8ujDlk_nIBd-TfvTRUQ_OvJujaMewX5m6AgOg2NQieT4mbdeiLDGWWBbEtr4hveGj7LUgI7gd7daNW7JYhPsw5a1C1Pa8dtIa3AjRUnzDt8wgrJSs9TxhjeN5koZGhQfFRPzuUfGv-Efyxpe_N4OIqmnWtu91I9zDSknJvkrdwYYXorsY64QsJBi_BUBi4jWuc4ICfHCw-Oa5ZUqm22_SNnZ6vm24NcSD0KJSCNTR66mQGDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بالگرد آپاچی ۶۴ در تگزاس آمریکا سقوط کرد و خلبانان کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69984" target="_blank">📅 15:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69983">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b49c38bef.mp4?token=k93NLyokREnYbbFyvUPUMT8nAD7wdSOrqqU37034RC6y0YkA8752yMvDxIzDy9Z5Upyq3vIb6NNkvRzw0k9B2E44HhyafnNu4jyKKPr2wTgtt9YfrzWCUKQQVRL3CBCowqhx5v9XDjG3bTK-XmujQuo9OAbkpIXvSaGZPybRceoOHKptosT2cRLNKkD7rQxN1EXvNFQ4QC9ayFD28mcHpQWZG5D4B8JE2fqX6KpRgBzVY0MLEuAwCqBnFm0sacd8RAAMlaHzKWz1awJSU0ONnIYWOMBped96jeA5KdikAD3qapK94HwcJsn0ASuV_LzeWo70qKQrJY2c5PZU54a-fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b49c38bef.mp4?token=k93NLyokREnYbbFyvUPUMT8nAD7wdSOrqqU37034RC6y0YkA8752yMvDxIzDy9Z5Upyq3vIb6NNkvRzw0k9B2E44HhyafnNu4jyKKPr2wTgtt9YfrzWCUKQQVRL3CBCowqhx5v9XDjG3bTK-XmujQuo9OAbkpIXvSaGZPybRceoOHKptosT2cRLNKkD7rQxN1EXvNFQ4QC9ayFD28mcHpQWZG5D4B8JE2fqX6KpRgBzVY0MLEuAwCqBnFm0sacd8RAAMlaHzKWz1awJSU0ONnIYWOMBped96jeA5KdikAD3qapK94HwcJsn0ASuV_LzeWo70qKQrJY2c5PZU54a-fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیکی که قراره برای بنزین اجرا بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69983" target="_blank">📅 15:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69982">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62cea94911.mp4?token=v7wWXJFkCf735lNmQqIlUirBpQITuTvmxmb0HSvMuYtDMwhwGPyG0I-nMsZqrom2ykSsSZAgdfAd6Kd142VS-CwSm72C50T7aqqhmH_bBPc4ujcsHnTa6Co_V_43fOXPVr7AILNAWH-nM_OzQXVCSIXyDHYfpH4uRbR80pXY3_DVANpAai5GMJyNX7iBhfUYLC27LVSzHq7rWY__NousbLcQmwfEVNECzbmF_E2LJaIW4vBkczi_s9sXIIGO3LWAVX4b3Bpl0_gaTOby-e5aMKCHqKxOIqbsq9bzxfsgzf29MX-C1iJUItWSytgSZVFylLCsf5EirdhXAyU-6c8DRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62cea94911.mp4?token=v7wWXJFkCf735lNmQqIlUirBpQITuTvmxmb0HSvMuYtDMwhwGPyG0I-nMsZqrom2ykSsSZAgdfAd6Kd142VS-CwSm72C50T7aqqhmH_bBPc4ujcsHnTa6Co_V_43fOXPVr7AILNAWH-nM_OzQXVCSIXyDHYfpH4uRbR80pXY3_DVANpAai5GMJyNX7iBhfUYLC27LVSzHq7rWY__NousbLcQmwfEVNECzbmF_E2LJaIW4vBkczi_s9sXIIGO3LWAVX4b3Bpl0_gaTOby-e5aMKCHqKxOIqbsq9bzxfsgzf29MX-C1iJUItWSytgSZVFylLCsf5EirdhXAyU-6c8DRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره بریتانیا:شاید بتوان بریتانیا را «جمهوری اسلامی بریتانیا» نامید.
کسی گفته بود که نخستین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
ما اطمینان حاصل می‌کنیم که مورد دیگری وجود نداشته باشد؛ می‌دانید، در ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69982" target="_blank">📅 14:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69979">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2XH_lCAApFhQXOZ-z3_3xipA7IYIKRSzal_7EmAh0LzYU5UDMwEqDKsg-QEPEB4ktFrlN19NvQ_NL203rDZbfdcNMpFN91AgiQKn50IVQZZZnuqrOF8spI4BoZAcWxWBBRM2QccNGu3kCKvMEKtC80OShu7K36x874Qs0Lg44RtOnF682L6ugVymyoPs1vgMdg8voJsw5h9J9koW9qGSbV4nTf8KaVoslgjL4F5PkSG0_vx4sj1-WEdXrTSxSAl6Bo7jfc6zE30FlX74BT73pK1JkydiqbpCMRSadFgTJjsuM4gEC-Mfzh_XgV11SnJx5RGfirqGiJuRwXnYTm5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohuBpCvW2IfxdCgC-w9-AVJdCsBA5ijutWN8yFScQu_OI01FnI9wGeo9IqKLHsK7qOTPC0EGix1TGYXvt2d8U2HpUBiK6brsJH98WfiDXf0FP3JqyW2KLV8HvWm5ZY-W0Hy6JG4OdIMA8HS8IU-JMNE42jWQBSJBMJ5M1F0CzQJ4CnaWsqQKUrqWumJNXplD7EdlkYWH7qv90nHhFYonW_iWTVQ0ToKdwQxmDPsvgQ7pXT0YCd_HKr9C7v2YvCSs0HBGtpMvJSOseGXsoiGhlytvcxHSyM8D17hQ_6iWynxMIQTAk5fHDg7HElmx_JtPNrvPlBjBZcOOXVBi2LRTeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=FXZuK87lSP5UOHyfAPKcx9tBsDhEU9xmK5zrucIAAJV2vHvPQKh1hZXodh87Etk3UKZFBm5tNKnqa5pDrEwz-EXwGCh5JCFDtXSpQQm3v2UpiTpFjyAZm1AibXPi-hjPOhTu381MNXa1uFoGTitxLDQgzdLFGOON8OpYK9RG0qvxzNnrYzBZ3-5wzGMAYRti4cW-cMYSdXjIG3DkAztvC3pbwxKtG7ADRZ9NGDqrt24eSUuWU4vDbVD4c8rgZPvRnTrf8ZwZWE483L8A1MYi4_HkoUcx1f6EFWXMB8w3NXzfzyj8dOf75O-ERAsCqMCbIGXFOA9JmOE08uS7jNoEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=FXZuK87lSP5UOHyfAPKcx9tBsDhEU9xmK5zrucIAAJV2vHvPQKh1hZXodh87Etk3UKZFBm5tNKnqa5pDrEwz-EXwGCh5JCFDtXSpQQm3v2UpiTpFjyAZm1AibXPi-hjPOhTu381MNXa1uFoGTitxLDQgzdLFGOON8OpYK9RG0qvxzNnrYzBZ3-5wzGMAYRti4cW-cMYSdXjIG3DkAztvC3pbwxKtG7ADRZ9NGDqrt24eSUuWU4vDbVD4c8rgZPvRnTrf8ZwZWE483L8A1MYi4_HkoUcx1f6EFWXMB8w3NXzfzyj8dOf75O-ERAsCqMCbIGXFOA9JmOE08uS7jNoEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
صحنه‌ زیبای خورشید گرفتگی که امروز در اسپانیا و آلمان رخ داد و لحظات زیبایی رو رقم زد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69979" target="_blank">📅 14:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69978">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b397a0c033.mp4?token=DeYLib1Ai3VOkdJitqon0Tpwa3zYRaROIVAupsBT5-rVXfk8dwyScGH9psm5UgSQV5pgvP4E7VySDYkk_jyeMJ5xRa1_WB3mcA7G2oVZTKzz9-N9NYo_PdaIwnjXxKwI74yWPnWN0sVkGGx0NUnWPwkP_usGvHL3R6WlESugfUgJnjyK3H31Rq3ri_IYZlDK8tRlIjn4YpKF_OepvwdN2LboZDSe3LqtcafVinMsWMYpjyUxADVK8PSj_Sgog8mFWMUP2Qu-uFPPtqqqdcAlyrDwa4vW5IyV9a_txZs4qrm47wgV4O2sPYNzr0F63LMWhiMTy6cEYUYGk4OX53IQ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b397a0c033.mp4?token=DeYLib1Ai3VOkdJitqon0Tpwa3zYRaROIVAupsBT5-rVXfk8dwyScGH9psm5UgSQV5pgvP4E7VySDYkk_jyeMJ5xRa1_WB3mcA7G2oVZTKzz9-N9NYo_PdaIwnjXxKwI74yWPnWN0sVkGGx0NUnWPwkP_usGvHL3R6WlESugfUgJnjyK3H31Rq3ri_IYZlDK8tRlIjn4YpKF_OepvwdN2LboZDSe3LqtcafVinMsWMYpjyUxADVK8PSj_Sgog8mFWMUP2Qu-uFPPtqqqdcAlyrDwa4vW5IyV9a_txZs4qrm47wgV4O2sPYNzr0F63LMWhiMTy6cEYUYGk4OX53IQ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی اصفهان، چند تا مرد عرزشی، یه دختر تنها رو نیمه شب خفت میکنن گوشه دیوار، و اونو مورد آزار و اذیت قرار میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69978" target="_blank">📅 13:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69977">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlkncYt4cUW_up4WOln3uczgukxh53UdXulp-ISqovVSOHXA3JUIE4Z00yxzw4LmCGIrmQHwLfF2QXPxC6gKWKfbz5fbCSjxWVmSRrweV40vHu_TfzsjbiiYHNICGMVmSqGcBhT6wzkPhgu7Dq8uOgNu7NU-cZSm_8vH3pfwnF9yHy3-Xld2N56bwu85kOGvET86rvhxi9tpNsOetYrZfAcxTOJZ_vNBZYMkUXSpkb2D-IMDMKy08ngk6ENXTQgEbKOEslTofjMt7dk6ZYFFaqWc4GZRtszWNXSjqsuzaRNFZhx-8Sd2BmS5rgAaCG1aEQGUrnsNOQ9sQFSLgr28PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
به گزارش نشریه "آتلانتیک"،
دونالد ترامپ، رئیس‌جمهور آمریکا، رویکرد خود را در قبال ایران تغییر داده و به سمت یک استراتژی "منتظر و مشاهده" حرکت می‌کند. او به طور فزاینده‌ای به تحریم‌های اقتصادی و محاصره دریایی توسط نیروی دریایی آمریکا متکی است تا تهران را تحت فشار قرار دهد و آن را به سمت مذاکره سوق دهد. این در حالی است که تهدیدات و حملات نظامی نتوانستند به پایان جنگ منجر شوند.
اسکات بَسِنت، وزیر خزانه‌داری، استدلال کرده است که تشدید تحریم‌ها می‌تواند در نهایت ایران را مجبور به سازش کند. در عین حال، کاهش ذخایر موشکی دفاعی آمریکا، گزینه‌های نظامی ترامپ را بیشتر محدود کرده است.
بَسِنت همچنین به ترامپ گفته است که تنگه هرمز ممکن است ظرف دو سال آینده اهمیت خود را تا حد زیادی از دست بدهد. او ادعا کرده است که تا 70 درصد از انرژی که در حال حاضر از این آبراه عبور می‌کند، می‌تواند در نهایت از طریق خطوط لوله زیرزمینی به مسیرهای دیگری هدایت شود.
در حال حاضر، دولت آمریکا بر این باور است که فشار اقتصادی مداوم می‌تواند به دستاوردهایی برسد که تاکنون اقدامات نظامی و دیپلماتیک نتوانسته‌اند به آن دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69977" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69976">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e944d4e8ac.mp4?token=ZrN9UiKQh9uvkkg7h-L6iZmIxbHiEWXWgbFRksoU_C_EAqAvXlCzGTg06RblftzXYQaQB7ZBoIr15HwijALPLtAMwRVBYkfwe93hqwWAYwvIauEWl7QdB_SlXpAM18R7_cbDfNihf580wBDtXrC0T9JBdtNAcqg7BeTap9r3HoIvrORY-V9KDFkrXIizJ-j_nemRupBowPsrCf7b2hiHWTNrmqhffgld8jPBviL6jqU4wjI2znxo_N6XlSuLYRYsvQXnZlL9sYUTp1MiCWkYUVNUu2rolCEaYV0d1H_Cn_ZnIz45R6hmQEFX2v34vVmq5HEMz-y_a6kW7gDIvWvPXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e944d4e8ac.mp4?token=ZrN9UiKQh9uvkkg7h-L6iZmIxbHiEWXWgbFRksoU_C_EAqAvXlCzGTg06RblftzXYQaQB7ZBoIr15HwijALPLtAMwRVBYkfwe93hqwWAYwvIauEWl7QdB_SlXpAM18R7_cbDfNihf580wBDtXrC0T9JBdtNAcqg7BeTap9r3HoIvrORY-V9KDFkrXIizJ-j_nemRupBowPsrCf7b2hiHWTNrmqhffgld8jPBviL6jqU4wjI2znxo_N6XlSuLYRYsvQXnZlL9sYUTp1MiCWkYUVNUu2rolCEaYV0d1H_Cn_ZnIz45R6hmQEFX2v34vVmq5HEMz-y_a6kW7gDIvWvPXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال های اخیر با ۵۰ هزار تومن چقدر گوشت قرمز میشد خرید؟
سال 1390 ؛ 5 کیلوگرم
سال 1395 ؛ 1.26 کیلوگرم
سال 1400 ؛ 355 گرم
سال 1404 ؛ 64 گرم
سال 1405 ؛ 28 گرم
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69976" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69975">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f12d9ffb23.mp4?token=KsW1DInHL8WAnSj8gCc5Pw6yjuUwKua2WbGxViEGfDD-Qbab5aGJMOGr5OfoyJn5K5ibZA9TlEeYGQwvm-RsSfJjDujTKVqL_Q4rmaQ9TjThk18lEtE0sNp6YlMncnH-IVpzhlcuYr83oA_gu2FSEx_eqvWgONqB8U0qsaHE1CbhCYBL3dTBgT4-eybfholBYMB5M9RgVmCi4lU-Tsu7X1YvGKPlsY_mHXXsa0nwT9cCtqa_vM0jaxHWs7_il7TwRIGsz9-xXC4wc_GFTqS3vd4OcXs6tQIyg-q7rjlgrJw3rcEzuAQrUu39_fRTuZNWRIwUiLyvB4vWNFnLJbvcQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f12d9ffb23.mp4?token=KsW1DInHL8WAnSj8gCc5Pw6yjuUwKua2WbGxViEGfDD-Qbab5aGJMOGr5OfoyJn5K5ibZA9TlEeYGQwvm-RsSfJjDujTKVqL_Q4rmaQ9TjThk18lEtE0sNp6YlMncnH-IVpzhlcuYr83oA_gu2FSEx_eqvWgONqB8U0qsaHE1CbhCYBL3dTBgT4-eybfholBYMB5M9RgVmCi4lU-Tsu7X1YvGKPlsY_mHXXsa0nwT9cCtqa_vM0jaxHWs7_il7TwRIGsz9-xXC4wc_GFTqS3vd4OcXs6tQIyg-q7rjlgrJw3rcEzuAQrUu39_fRTuZNWRIwUiLyvB4vWNFnLJbvcQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لعیا زنگنه، بازیگر:
سال ۱۳۷۴ که سریالِ «در پناه تو» در حال ساخت بود، آخوندا و مسئولین میگفتن که دخترا با زیبایی پارسا پیروزفر به فساد کشیده میشن و کارای بد میکنن!
برای همین دستور دادن با گریم زشت ترش کنن و آخرشم ۹۰ درصد سکانس ها رو حذف کردن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69975" target="_blank">📅 12:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69974">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcm5PwDhG5EBHvMfl3mwPqEn9sB_YCVzwxR2T6EbUvJAb6Xuc8qArh5oUOOBAt4piHAgXGB4tLAM9mvU6rVLsEWZjIOWEhXWeLSoAuNBJpHtKQZ_j42ngSjRYrrrIDHYjnS3a-uMugLzogr-V5JP4yxa6vummy97Denbo_vtDsbMDPQMG5NhdI2nwxcp9DmDZBUE2itKCwPER6nZEZy9gb1tydT64Ioe8a5NcU_OS81DNnJRsSY92lzxEdHmujbaUYhpkARUt_i8ZQCJbRAABaR9oxoLOu-EsTJMG7Gy1jc0Rn1uXhiGq76rBKlQTJxIO7yWh36G0n5r6M6bfBlMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
ایالات متحده مدت‌هاست که به دلیل ناکامی‌های اطلاعاتی، محاسبات نادرستی انجام داده است.
مثالی واضح: جنگ علیه ایران. حالا، یک محاسبه نادرست حتی بزرگ‌تر در مورد تنگه هرمز.
بدتر از اخبار جعلی، اطلاعات جعلی است. مراقب باش.
الله بزرگ است، بزرگ‌تر از هر قدرتی روی زمین. ما به الله اعتماد داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69974" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69973">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69973" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69973" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69972">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AntLlZ70rDLze9HhuZgr2ffdO4t2CwmUuSQs6JSSDETGWBG2nbFV16Mn8sC0xobiea7kYqyJS78PHTvoN2QF9ubLGwoOjzYbOSruITDZPo8gfEm6UXonJjtl_qVEIzM0Hn0ledeYyE5Fh-3_O1TNqkU4cOsXTgoWtoIidRoYuncAo7jelCdKf4mnfzVd_7czLjEmqnsXwtu9EdXli_lRy-Krdpdr1NvPTclyW_Lp7GbmojYEsj6K0HXAUEzlj4aPp36paf4OXb6664z4IQ7FXRlhl5O3Z77ZoUXSgu7O_zXkgyrIKxBefUn2d4FQ_9x6J5VWckM-ijQ_7zi211a3Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r22
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69972" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69971">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77c4997c0d.mp4?token=rNS-DTxjryPXyw1knm2DKpzVA3n_2yvfMji3jqSzdPFtKM6mjh2baq2crD1bLydOKeZ_Bj_XsoYB-H7oX2Ba48Z5MIvCHvyL-Cc4Wl3RFn_Jy2BgfkBtYeTFpUCcadLON_wmyH_wZbLuHUOc1we4mYu8rUYvYrF7pL_rQdb7tNphTfUV1d6bZAwXirwiG18VA5LC5fYI9XAgD5FtqQRE0R5oeUaOrJihQLLMhUCH3LhGWS0kxc8lYvI5xbg5UItGEjDi4IO4pJboDUe_5tzm3wNLToJI27GoG5aIaS6QINCVIflRZP1pKc6BGstu09SAOIrpKMtvMJZjoozQooDpOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77c4997c0d.mp4?token=rNS-DTxjryPXyw1knm2DKpzVA3n_2yvfMji3jqSzdPFtKM6mjh2baq2crD1bLydOKeZ_Bj_XsoYB-H7oX2Ba48Z5MIvCHvyL-Cc4Wl3RFn_Jy2BgfkBtYeTFpUCcadLON_wmyH_wZbLuHUOc1we4mYu8rUYvYrF7pL_rQdb7tNphTfUV1d6bZAwXirwiG18VA5LC5fYI9XAgD5FtqQRE0R5oeUaOrJihQLLMhUCH3LhGWS0kxc8lYvI5xbg5UItGEjDi4IO4pJboDUe_5tzm3wNLToJI27GoG5aIaS6QINCVIflRZP1pKc6BGstu09SAOIrpKMtvMJZjoozQooDpOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی کره شمالی اینترنت قطعه و مردم فکر میکنن رهبرشون خودش میره با قطار براشون غذا میاره و تیم ملی فوتبالشونم هر دوره قهرمان جام جهانی میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69971" target="_blank">📅 11:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69970">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJNeVXnA0Ssofz3XqDi4GTQZNHlcSvlF7wuuat9tmH_e0TCFIk2MIjru1YKmFhauQCcc3XJbfA7x7I1bJTJrD59gEDTK3yBWU45zYkbkWHwkjLN8NHI7YNOjQb2fINfQ2L-8yv4Kd-_zzMb7pStKu4cqwKcZXKJW7QofNYE4Xremq5ZxR4-U5rhciDul3kR0WEsr3ioaECp62N7QTjl_k_T7Ox1nkW3u6lcf-qpUtp8mkZE9rxuCfynDMw5vZuYIbqyM_68mhBljRaqxvhHHv-_uFbNeIibHQVonJpp00P3kfeqVzhwAbga_TBMdaCgg_T9FDVg33Iz3aYl-ll93wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نشریه گاردین: چندین ملوان حاضر در ناو جنگی "آبراهام لینکلن" تلاش کرده‌اند تا از عرشه به دریا بپرند، زیرا خدمه این ناو با فشارهای روانی فزاینده‌ای در طول این ماموریت طولانی که برای پشتیبانی از عملیات‌ها علیه ایران انجام می‌شود، مواجه هستند.
حدود ۵۰۰۰ ملوان و تفنگدار دریایی حاضر در این ناو، در ماه نهم حضور خود در دریا هستند و رکورد ۲۵۰ روز متوالی بدون توقف در خشکی را ثبت کرده‌اند. خانواده‌های این افراد نگرانی‌هایی را در مورد فرسودگی شدید، شرایط زندگی رو به وخامت و حمایت ناکافی در داخل این ناو ابراز کرده‌اند.
گزارش‌ها حاکی از وجود مشکلاتی مانند سرویس‌های بهداشتی کپک‌زده، توالت‌های خراب و امکانات شستشو، کمبود آب گرم و محصولات بهداشتی اولیه، و محدودیت در تنوع غذایی است.
چندین تلاش برای خودکشی در این ناو جنگی خنثی شده است. یکی از همسران گفت که شوهرش پس از تمدید مکرر ماموریت دریایی خود، تلاش کرده است تا از عرشه به دریا بپرد و افزود: "او می‌ترسد." او پس از اینکه شوهرش از عرشه به دریا پرید، با او تماس گرفت، اما از آن زمان تا کنون هیچ تماسی از طرف نیروی دریایی نداشته است.
در یکی از حوادث متعدد، یک ملوان که در حال نگهبانی بود، متوجه شد که یکی از همکارانش قصد دارد از عرشه به دریا بپرد و با مداخله، او را به عقب کشید. در حادثه دیگری، نگهبانان از پرش یک عضو خدمه از عرشه جلوگیری کردند.
این ناو جنگی در اصل در نوامبر ۲۰۲۵ برای انجام عملیات در اقیانوس آرام اعزام شد، اما پس از آغاز جنگ با ایران، مسیر آن به سمت خاورمیانه تغییر یافت و زمان بازگشت برنامه‌ریزی شده آن بارها به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69970" target="_blank">📅 11:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69969">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a118468ed9.mp4?token=ZwVScKil91QnVL_2md-__Y0LOhc6Ci4pFY_F9uCsoUud-pVDrkwTa3PYLDktsdAjiWYaWKUCsKp5xf_-JTgNBBQGMfwKDJQ2Cw2UhFiPLbLALmk_BFnt5d-dlI-mQXduqBH1i2-aedLGjjXta45ugpQwX4HuELefT9M1b9EBZHr5tV1qGBdeJF-8JDKSjeskwbFA2o_pknMaGc6ph3AcGXOLZ50C8-sPwxx88iYUAZjC5en9wgrHm5i4U7Qy6Y2wQU7nV1RpmaZJh50LnD-617p3T6J0RtqQ4r5Mgj70JwghvI7srhTnkAhza_nfHM1S-RofxwNmjHHedQDo3xjYlA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a118468ed9.mp4?token=ZwVScKil91QnVL_2md-__Y0LOhc6Ci4pFY_F9uCsoUud-pVDrkwTa3PYLDktsdAjiWYaWKUCsKp5xf_-JTgNBBQGMfwKDJQ2Cw2UhFiPLbLALmk_BFnt5d-dlI-mQXduqBH1i2-aedLGjjXta45ugpQwX4HuELefT9M1b9EBZHr5tV1qGBdeJF-8JDKSjeskwbFA2o_pknMaGc6ph3AcGXOLZ50C8-sPwxx88iYUAZjC5en9wgrHm5i4U7Qy6Y2wQU7nV1RpmaZJh50LnD-617p3T6J0RtqQ4r5Mgj70JwghvI7srhTnkAhza_nfHM1S-RofxwNmjHHedQDo3xjYlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستانی از زبان یه دانشجو-معلم در زمان پهلوی، که برای اینکه مخارج تحصیلش رو بده، شب‌ها مسافرکشی میکرده، تا اینکه به محمدرضا شاه برخورد میکنه و...
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69969" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69968">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=S1YoSW8AV8wDkoQOadqR3Ki2FziQWEzREOjynOPduEe98Np0HBGNxh8YVeG53VMK2B7cEAaNBYxRFfwFhKpTrD4dVAIhFXic0XlFXcgx0ULlNC2sPAowi-iQvm5VpRwc5yY0rpdGgBRspLLKzYN-gxQIwJ9x8OYiWhz_EiJN1jMtOaaaEmFpdzZUlPMy5qH6wNsGpvpNKeAHHqOZbz5NllqVM_oDEbAWOuMszYRLygilSE_O6CHgjyZlpieegesWK8xaN_Jc_aOA6vovWCGdr6fY1wriz8LI34Fofz1LB8IMo2Lt6hNDW4_khpBTui68XeNJzmhDE4tbPDNm2F45VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=S1YoSW8AV8wDkoQOadqR3Ki2FziQWEzREOjynOPduEe98Np0HBGNxh8YVeG53VMK2B7cEAaNBYxRFfwFhKpTrD4dVAIhFXic0XlFXcgx0ULlNC2sPAowi-iQvm5VpRwc5yY0rpdGgBRspLLKzYN-gxQIwJ9x8OYiWhz_EiJN1jMtOaaaEmFpdzZUlPMy5qH6wNsGpvpNKeAHHqOZbz5NllqVM_oDEbAWOuMszYRLygilSE_O6CHgjyZlpieegesWK8xaN_Jc_aOA6vovWCGdr6fY1wriz8LI34Fofz1LB8IMo2Lt6hNDW4_khpBTui68XeNJzmhDE4tbPDNm2F45VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زاکانی:
موشک دقیقا خورد تو خونه مجتبی خامنه‌ای. زنش که معلم بوده اون روز سردرد داشته نرفته مدرسه که اونم شهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69968" target="_blank">📅 10:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69967">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcec26005.mp4?token=go3B2dc7vVHTsZ2BwlMLmh-MXvcEXfUsZcU63Uby5GelLlRoGhe7ncsZc8GO44tvf3ZP2An6GYAxWDcyH3MIXN0G-it60sHyGh5LuTFdJbFcanIcC7SaRk0fbGon1U2UgLciwqIXp2XPUJn1_l6IjaT4a1Ua15QTJ-yq_lnaQ--4cVhe1MZiV90DWhb7LaQ21SLXuGrI6lvz36BqUr7KPN5M6UpS0Xfw9gNeYr2u-J8ZHB0Sh8nIcSSe6QzZqdTd6Awldpgb7DvTQdZbxTTiSo-_5R0AbfGljVty9daoRWjNlZG_RLMQ9OrnmufOVAb-5YwOgE20hx88Ct8ugNLZ1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcec26005.mp4?token=go3B2dc7vVHTsZ2BwlMLmh-MXvcEXfUsZcU63Uby5GelLlRoGhe7ncsZc8GO44tvf3ZP2An6GYAxWDcyH3MIXN0G-it60sHyGh5LuTFdJbFcanIcC7SaRk0fbGon1U2UgLciwqIXp2XPUJn1_l6IjaT4a1Ua15QTJ-yq_lnaQ--4cVhe1MZiV90DWhb7LaQ21SLXuGrI6lvz36BqUr7KPN5M6UpS0Xfw9gNeYr2u-J8ZHB0Sh8nIcSSe6QzZqdTd6Awldpgb7DvTQdZbxTTiSo-_5R0AbfGljVty9daoRWjNlZG_RLMQ9OrnmufOVAb-5YwOgE20hx88Ct8ugNLZ1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید فک کنید هوش مصنوعیه ولی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69967" target="_blank">📅 09:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69966">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39fe0991d.mp4?token=CS4CrTdRBf1MvREtPCkMaFPfrVLD5_3oJ8KsVls9hLjOBfd0XVGmxoBihb0kswrCYPQpXy93-Sf1mh83x-xsjtrmkacV8kdgZ2pj5eRrC2mNlemE4Eh6kQLTMRHx8oKv6FzHu02izrhJ1HQ9PA64j-6KXhnJW_Jg_JcWNUaAfKXMMVzx0YX7e4xkWgAXth1C4LR7prBVW0O68XHKLZ3jsUvZEpmQUygJG6QM5Pe1HCU9WpgVPxNzXftO8nRqe3sBqfc46ErkOv4LGTcdo8A1UPnlzKbXhYSX12mbf1kTqwvBTcs5cef4uF_usJR6-fGfd874Tje67Kn_PFZEsVdPPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39fe0991d.mp4?token=CS4CrTdRBf1MvREtPCkMaFPfrVLD5_3oJ8KsVls9hLjOBfd0XVGmxoBihb0kswrCYPQpXy93-Sf1mh83x-xsjtrmkacV8kdgZ2pj5eRrC2mNlemE4Eh6kQLTMRHx8oKv6FzHu02izrhJ1HQ9PA64j-6KXhnJW_Jg_JcWNUaAfKXMMVzx0YX7e4xkWgAXth1C4LR7prBVW0O68XHKLZ3jsUvZEpmQUygJG6QM5Pe1HCU9WpgVPxNzXftO8nRqe3sBqfc46ErkOv4LGTcdo8A1UPnlzKbXhYSX12mbf1kTqwvBTcs5cef4uF_usJR6-fGfd874Tje67Kn_PFZEsVdPPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های داخلی با انتشار این پست اعلام کردن که کامنت گذاشتن و لایک کردن پستای رضا پهلوی و اینترنشنال و... جرمه و کسایی که اینکارو بکنن دستگیر میشن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69966" target="_blank">📅 09:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69965">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69965" target="_blank">📅 01:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69964">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=j0qSpNJCvmwL59HnNQJAQxTT47VNL8E756zv-POePEtgqMxRx953niX4QwP79N4HXGIYBbPBMzQyqJCSioSdLys-xWmEXszCudkJZ4XxPX0CrVucT-DH5L1TVIRh78cEalT7iITmHulYex-qfB1SWmD2baNKWIwTrITIbOJ-9xZZFaiTp0ICn4G_tJ-RCkqCsmeSf0jfc8qO2I3OZY2mBCxlBJhO-uu0xs6fc0471zcUSGFx932eDJuq4mKn0sDhAipWxfWTYnGPuvKSivfLIMSIYDJ7i488sVH9zYSMguumwVWUxdbXlayMherVwpU0byCRZc3veP8pgF7585jvGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=j0qSpNJCvmwL59HnNQJAQxTT47VNL8E756zv-POePEtgqMxRx953niX4QwP79N4HXGIYBbPBMzQyqJCSioSdLys-xWmEXszCudkJZ4XxPX0CrVucT-DH5L1TVIRh78cEalT7iITmHulYex-qfB1SWmD2baNKWIwTrITIbOJ-9xZZFaiTp0ICn4G_tJ-RCkqCsmeSf0jfc8qO2I3OZY2mBCxlBJhO-uu0xs6fc0471zcUSGFx932eDJuq4mKn0sDhAipWxfWTYnGPuvKSivfLIMSIYDJ7i488sVH9zYSMguumwVWUxdbXlayMherVwpU0byCRZc3veP8pgF7585jvGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a21
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69964" target="_blank">📅 01:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69963">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=BPluoKfIpCccSbOrS2bRCBeYM34p-NkfyTrulQE96hxGwWD9RCJe4wos0npYMAFiRxoXIH8wWNZQ3_oPxc45gFdHS6uLYsRA7ysFacN7cNjfVAoaB-Lp0_mt91d3iPk9lrCfUWjkeFnfHIf6txRGb3KXnv-ye-En1uQXC6UvUfDSQxLY9IuNn32lpkTcPQ5Ain8JTLzOkuA-MBzSJnUHRFKETJD5_pmIqohscQBS9xQ2fpP-dInkhTy9u2ztpSycUMHPeLejgTiAL6d-Gcb07TmWQ5cUUYTL8jn6NmwmzpQx7Rurx-vbOx1bj-DxNGg-csY7mEIJ9LC5V1HTxEPRZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=BPluoKfIpCccSbOrS2bRCBeYM34p-NkfyTrulQE96hxGwWD9RCJe4wos0npYMAFiRxoXIH8wWNZQ3_oPxc45gFdHS6uLYsRA7ysFacN7cNjfVAoaB-Lp0_mt91d3iPk9lrCfUWjkeFnfHIf6txRGb3KXnv-ye-En1uQXC6UvUfDSQxLY9IuNn32lpkTcPQ5Ain8JTLzOkuA-MBzSJnUHRFKETJD5_pmIqohscQBS9xQ2fpP-dInkhTy9u2ztpSycUMHPeLejgTiAL6d-Gcb07TmWQ5cUUYTL8jn6NmwmzpQx7Rurx-vbOx1bj-DxNGg-csY7mEIJ9LC5V1HTxEPRZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنر نصب شده در تهران:
پزشکیان راستشو بگو، مجتبی دیگه نیست و فقط وحیدی بهت دستور میده؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69963" target="_blank">📅 01:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69962">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
#فوری
؛خبرگزاری فارس:توقف اجرای طرح عرضۀ بنزین با نرخ پالایشگاهی در کرمان
مدیر شرکت پخش فراورده های نفتی کرمان: پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضۀ بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
تا اطلاع ثانوی، فرآیند عرضۀ بنزین در جایگاه‌های سوخت استان مطابق روال پیشین ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69962" target="_blank">📅 00:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69961">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184379545b.mp4?token=UUUo_Enb59_88OF5eEvXXZk-9W_SdI1ZMSCRk8zCdHkMSXl8s3D1O1BHt1qE95vJUXTHiNwiLRorZnDhsfu-CjPrW4FfRQLYsk_Y9FsfrJlw1iaZ-UwnTPMD5wwP_bhLz5T30_YO5dLdBuz6hAgh-R-Frmyojiz-TPkVGJJcA1dYrl64BmvibjkrozqCPV8u3EPR1HIpKJ8QmPa0puzC3p42boY1zazsMPvL5h6EhFCcjd2739Qyma_kGJGjb8Zaghbf7YvnYDB7humbZM8VJaF6bAsi8h93G8nOQytOpQrNpmmZcBXfm-s4nO1pUor79iX27EijtwyaTH2HSj8JNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184379545b.mp4?token=UUUo_Enb59_88OF5eEvXXZk-9W_SdI1ZMSCRk8zCdHkMSXl8s3D1O1BHt1qE95vJUXTHiNwiLRorZnDhsfu-CjPrW4FfRQLYsk_Y9FsfrJlw1iaZ-UwnTPMD5wwP_bhLz5T30_YO5dLdBuz6hAgh-R-Frmyojiz-TPkVGJJcA1dYrl64BmvibjkrozqCPV8u3EPR1HIpKJ8QmPa0puzC3p42boY1zazsMPvL5h6EhFCcjd2739Qyma_kGJGjb8Zaghbf7YvnYDB7humbZM8VJaF6bAsi8h93G8nOQytOpQrNpmmZcBXfm-s4nO1pUor79iX27EijtwyaTH2HSj8JNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خانعلی زاده کارشناس صداوسیما:
افزایش نرخ بنزین و گازوئیل بالای ۵۰ درصد مردم آمریکا رو شوکه کرده
زندگی اونا فیکس هس یعنی پس انداز ندارن وقتی بنزین یهویی از ۵۰ دلار میشه ۱۵۰ دلار ورشکست میشن
مردم آمریکا مجبور شده ماشینش رو بفروشه خونه اش رو بفروشه بی خانمان شدن از گرونی
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69961" target="_blank">📅 00:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69959">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7326381213.mp4?token=UraAWwI_sZx6bqf2L-XUnxmgIQK2hy8XWCQESYC0enWw1WEEWY2enQZ3EfFKSHp-697gakw9bhNs7Z7zOUy3Lu31yT9GWZG_CN6QjaGdtfVWwWPmxIviKZe4BQ64VoMROzTnuBl_Wxw9AywBzfE4Ys1qdz1Kj1ABAI2t7ZKp6VcKfHGU4nBJPnp3nQWgKWhdg7UiWELBT5QpoBUHTNMlp74HYBxjr9-Q6i9-se8nJqA_TTsHM3ozZ9mdPy3rFnbmCwgg3ofexlNxIsun7w2SalCN9n4Iawd51hv1pgLwBoop0VamfFMmMTWjITTdRs4wubCiM-57Rh0qRAXUIuWDsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7326381213.mp4?token=UraAWwI_sZx6bqf2L-XUnxmgIQK2hy8XWCQESYC0enWw1WEEWY2enQZ3EfFKSHp-697gakw9bhNs7Z7zOUy3Lu31yT9GWZG_CN6QjaGdtfVWwWPmxIviKZe4BQ64VoMROzTnuBl_Wxw9AywBzfE4Ys1qdz1Kj1ABAI2t7ZKp6VcKfHGU4nBJPnp3nQWgKWhdg7UiWELBT5QpoBUHTNMlp74HYBxjr9-Q6i9-se8nJqA_TTsHM3ozZ9mdPy3rFnbmCwgg3ofexlNxIsun7w2SalCN9n4Iawd51hv1pgLwBoop0VamfFMmMTWjITTdRs4wubCiM-57Rh0qRAXUIuWDsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🌓
لحظه زیبای خورشید گرفتگی در اسپانیا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69959" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69957">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRdLzSzwBaxM-cFTYSGe1yOI1y5UlBir_QJ0EVaDxqK0GvvPVRyN-Vxz87V9zj5k97Uro1qRFqzDemslXmT2QZ0kbl9vIwOzD_WwnFGpgp1bOn50a83_BsZcRXjWX2aQDS8eXSUHKY6c007PkmkhYpmQ3hy6AJs3e6_W93ZzG-IPzMJ_CuBTJdgzS6jf3sHE7hWezx5838bmyRL6iZjAWoWFGzMjZyu72_ppqoeJtUNGH_89oIsXSXzU2wgSBdN3w7Con7qmSURZYnRUgmdIryKKNZa3Vfy3zeYQZTkA7CTrViXIZ-IJwsQNf3hZFpLEAJDpRzBG4DCNO7sWl3UzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJGAlMH2iQD2Z0t1-nNVX3yJ4EKCr2Vd4EFK_wJb5kI3JDVhuM3F5bsZTCBrFCkMQnx84SivlbZCE1sggYHBhSOqyDpqFuiBAyZNp6aCf8QWTHbs6MGzoY1C7QSYOJkIqZDIom-PdNTMSuZLluHtvJ0vqnxEik--grWmKsyHVRwOHiwM4ASU4yPKVKQQ8tt56xHPtxRkASCZJMkGwvq7BoPLpoMn7uXqbf9fMMkD1IUfT-A1R5tBM_zd5yYNxs81YTqWkni9wQ__4AEueLhhIHZ-S_quhE2XeYKZnkRVbZtJId7RefMp3y5AfcGIS24SjMvlnsHjFTp5Tgefag0SQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇺🇸
🇺🇸
با اعلام ترامپ کارولین لیویت سخنگوی سفید کاخ سفید این ماه بازنشسته میشه تا با خونواده و بچه هاش وقت بیشتری بگذرونه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69957" target="_blank">📅 23:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69954">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rraL96QwAbwAyYGfsKTr6Rj6Jtm-2kTaiF1nPEJJIaXg4gJYyaooZ1KcdPjEyGvW6kkvoKVjEIN6789dpMiiLp8wpmSMVF0JYE__wdfNZVu1-CjXW0pcoa9k03VKM0FHlRI8ibtd62Kk1mWJxMDWZZrBM0mf6k7iiBDgvziD6qcT4TbfIjPD3KBxm5aYpN_j6s08hH-FzGyzCEok9BaTQujJSCp_Ogu-0ZXIlFkdL2v_PbIHi7fdxPFjeS7JxwoSuK_mRgpZSYWvDtRDx90aEgffuiDR0-LYrOOtBMB5TfgLyC587PL7NOWBtByEJ231uHIVP-rRUeVRpF2KkkVNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqZbwrDBYHU9a3pgyqpcp3U9USSmOYdKNiol_qKDVtEavytW9U6NvQFSwXKci6pMh-1SZAFw2kg4MK7BGXTeMUY7hDCT1McfvC2J5bBOYSAcXirvKxY9Pn3VrQJ17zKBarGeO9TbWC2OyvEWrZ6GpJfme9WgcU893z--8tEZwzi1YIJWSSsmiuqwrHgiDmnBh4PJ-OoTBC4L6MpymjYsnKrOjfAD4MNemkpGV15YxSrHvBaIeoGvaMfu3zI7SK6Dz7yG_KH7kuvN56ka049CVQt6Qg-TIHRD9JYmOgOw4MYpo4uL3niXcMUFFe3SWtY6dl0jBjuTn9WFt-HBs_mtWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewnCLvII8xr1dymIg5UUKmDC1bo2_KEZJQh-QtlutlgD8vqhdvb_Jvu2C8aOfKNkYwgDw1wGVKrysLaczJheoMtPpIQzRcPG8ESzSWkZQdZ5nJKHeNPv5AN-amp9Kw9cD_mLFKahrD76FbGy05haKROUjJedmFCCNfx6N31VC2lru2W4AAHBGiefTgJleXe90kuf01ZxwvfK5fJFc7ASISImiPva1AjXojh6jCM9ZFXaKr4W8bdHvPO-jO7GJk4efRKLwd6nn_0jubyQRBDJ1sGzRDwmFbeq370Y1fwWBlNfgqx3qUkJNfMdW84k9Yn6ph6JyWfjAziuQXXvLM5hng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69954" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69953">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpV841KNzGccQtkdluHbJQWVEh_-x31J20HKtAyYUgSkMxH1n04sqjoJK9aokp6-2nMEDpAVRlq_dcZezIpQwLSWmmRx07SZgpWfbXz31aiojM8E_LlArjm95iC5ZPYdnYu_4vaa2Bydf6gt_G2cN6kRBmTJkHZYEpUOhMJKge3KdENb6FujeMKAdOJfeNtaipK48wN0jqWZdHrMJzDEIbRKhTo_m9Jfua2VvwOSDT9zMkBq_BhE_VzXJjYDiLn-N2d_-h8ZC6oQnr-nk0leE1fF56fsfzJT80aMEZrmtWpEcgs5ODL4t7r24bC7LQIV3nJXSGdBVVXY5L-HRo0ONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
یه اکانت تو ایکس:
ایلان ماسک باید بریتانیا رو بخره و آزادی بیان رو به اونجا بیاره.
🏴
ایلان ماسک خیلی جدی:
[بریتانیا] چند
؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69953" target="_blank">📅 23:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69952">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر منتشر شده، مجموعه‌ای از حملات هوایی انجام‌شده توسط نیروی هوایی و پدافند هوایی روسیه (VKS) را نشان می‌دهند، که به شرح زیر است:
• پنج بمب FAB-500 علیه یک پایگاه نظامی ارتش اوکراین در منطقه نووژوینکا، استان خارکف؛
• چهار بمب FAB-500 علیه یک گذرگاه خاکی در منطقه مایاکی، استان دونتسک؛
• پنج بمب FAB-500 علیه یک پایگاه موقت نیروهای گارد ملی اوکراین (NGU) در شهر دوبروپیلیه، استان دونتسک.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69952" target="_blank">📅 22:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69951">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69951" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69950">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mo6U1koR9m_8A6NJl2NtYGgDs2LJD8qA0_FbhpQP72OsKQOn4mt05_d2tGwTjPizRF00UXHArrYYlPVahyAjoFi_-ySnwgUI-_Qu4251-eEX63W5JvPVMEsCw0jCSduxnnMN9PhgmnHmwHZMAovN1AWKbwpJ3-eFyfaf4v69vEKahRd80pj_OMbY4Hw58RZqwXUZWJYZ63LooWyFekbBH6oL-HNMBflL2rWO2L1l4juLmpW2zsCglbGhyGAfN-HhpxnOq4NmaDGcFGx-KcWen91R8Mmkbhf1IHLHc86RedIoFEnTQTkb8Sv-VM35J59WFUbHcAAUYgrSBPvGQNf9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69950" target="_blank">📅 20:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69949">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=juAldvgChnSFMrBDecRH8BM0i81foKoSZDcZ3-6Jg7OwA-adBUkOEAOxM-ewBBgClGfU23ySQlj1AGv1UzQm5Qqg6EP0stJ_05GQCY0LXzrIgckP6FYgNY248aJiKs7uR9x-JBjgxG9OmIzdBJeXlfoUjkQogEJK8ubWn9lPEEZ7fZNfPpICDgdMrjaOSKn3Om8g3eD_OjboFTD7Kdfr84dA96T6CHtkGwVABd1alr06kmC65OLP1PX_-ieNk-McQgFYaltoteAfH-Y-mMIvRtavbVyX7nOuB2fdGagY_Wpr-t3fabTrfTANwQGqrT9z_O0iaRCWOHfA3mwSbFPGRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=juAldvgChnSFMrBDecRH8BM0i81foKoSZDcZ3-6Jg7OwA-adBUkOEAOxM-ewBBgClGfU23ySQlj1AGv1UzQm5Qqg6EP0stJ_05GQCY0LXzrIgckP6FYgNY248aJiKs7uR9x-JBjgxG9OmIzdBJeXlfoUjkQogEJK8ubWn9lPEEZ7fZNfPpICDgdMrjaOSKn3Om8g3eD_OjboFTD7Kdfr84dA96T6CHtkGwVABd1alr06kmC65OLP1PX_-ieNk-McQgFYaltoteAfH-Y-mMIvRtavbVyX7nOuB2fdGagY_Wpr-t3fabTrfTANwQGqrT9z_O0iaRCWOHfA3mwSbFPGRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمود احمدی‌نژاد درباره حسین طائب(شهریور1392)؛ «مشکل روحی روانی دارد»
ایشان [طائب] تعادل ندارد؛ همه مقامات کشور می‌دانند.
اصلاً کارش پرونده‌سازی است. از وزارت اطلاعات انداختنش بیرون چون دوبهم‌زنی می‌کرد. باید معلوم شود ایشان بر چه مبنایی در این کشور کار می‌کند.»
❌
حسین طائب به دستور مجتبی خامنه‌ای به فرماندهی بسیج گذاشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69949" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69948">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=re-rjUjA1V89IzBhBLzaidtP57kuX3WufaXALl6mxA-pXNIs17u_TNrJ5wsr7fYiA2LSJ3Dtw2nI86Kd1hHO45yo4yvK6AJ8NFTbLTEW4DaO9b9EXuLCvZOqmMsg5htzSshd6QYVGCvF0xKcgp31Woj6-gEJW-SvCRQI8W1YIZUOMKsai_s2gGeJWM8ngKWRFyU0Ngc-wMN38QBX3yZi7pavT1mTU_xHdUhhGSHf06R4hm1fiS2BadYH-VtYWnnKedu9ADpzY5HxtbuN1YIiNZxUJ2O-4--VkF4l2Rg1nfiRFHifRLY0S4m8pgDG_F9q4efcwEFafSTcTp2b0lqSrXYutMxBxMIHR_KmvKPN-YQI-b0kG51VSo3GGw1-HUd2d7no12XhJ0ux69StLgU5YOhcYkXJpTen8-pxG69aH_fCuTgLbVjGWCVJkpXvbQHgnQaNhk8bIaHXXCC0YDRHhPbL7SHTW38l2x4ON_8Fl9aQH517zzH6KeY8HA7u8I_CaKSb86t_EolZPtc_seD6rvqDsWY4fkkR0f5vKK4yhh_TC2kqvYGQo3GH52i10YVNxpUfwEmu1P159qUUjI1A9pRkc1crcnMZ76fdKPUlXdGrG06aZovJAEr7Tc32Vy8G4b0JjtaXh4SD-Lc8khJ8UTl8xfx7VaMuzCIPfnqojuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=re-rjUjA1V89IzBhBLzaidtP57kuX3WufaXALl6mxA-pXNIs17u_TNrJ5wsr7fYiA2LSJ3Dtw2nI86Kd1hHO45yo4yvK6AJ8NFTbLTEW4DaO9b9EXuLCvZOqmMsg5htzSshd6QYVGCvF0xKcgp31Woj6-gEJW-SvCRQI8W1YIZUOMKsai_s2gGeJWM8ngKWRFyU0Ngc-wMN38QBX3yZi7pavT1mTU_xHdUhhGSHf06R4hm1fiS2BadYH-VtYWnnKedu9ADpzY5HxtbuN1YIiNZxUJ2O-4--VkF4l2Rg1nfiRFHifRLY0S4m8pgDG_F9q4efcwEFafSTcTp2b0lqSrXYutMxBxMIHR_KmvKPN-YQI-b0kG51VSo3GGw1-HUd2d7no12XhJ0ux69StLgU5YOhcYkXJpTen8-pxG69aH_fCuTgLbVjGWCVJkpXvbQHgnQaNhk8bIaHXXCC0YDRHhPbL7SHTW38l2x4ON_8Fl9aQH517zzH6KeY8HA7u8I_CaKSb86t_EolZPtc_seD6rvqDsWY4fkkR0f5vKK4yhh_TC2kqvYGQo3GH52i10YVNxpUfwEmu1P159qUUjI1A9pRkc1crcnMZ76fdKPUlXdGrG06aZovJAEr7Tc32Vy8G4b0JjtaXh4SD-Lc8khJ8UTl8xfx7VaMuzCIPfnqojuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش شهروند اماراتی به شلیک به پرچم امارات توسط مجری صداوسیما در پخش زنده:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69948" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69947">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d7922013.mp4?token=g4bP6zF6RnrJZKLgGXAvBlb2esUSyiUxzgOKfe4lCwMOiJx8_G9uATOmciUAoOm4x4hzQVAzuK-zo232Q6Z2f_wPZzkf1hJoCdRAYZOInVPxdwDAjaKeBinCs7SrlpY9KFGVWusYAyyuLLWjbv9x9iJkxwvyK5A-HXkQb42U2jzORjcJFXi_1h7R-c9T3YfOX0iXCND7xzyH7QcIFSETFEvyaJYVpbIarsdciysm-TWikTv2JpSmJ6Shw7b7t03W-VRam0BN7S2H56rHt2oBsqSNiETqlViPg3pqz74pb5-bx48443TX3kK-DJIql06B4iyAnBdlESWW-jE15VEQZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d7922013.mp4?token=g4bP6zF6RnrJZKLgGXAvBlb2esUSyiUxzgOKfe4lCwMOiJx8_G9uATOmciUAoOm4x4hzQVAzuK-zo232Q6Z2f_wPZzkf1hJoCdRAYZOInVPxdwDAjaKeBinCs7SrlpY9KFGVWusYAyyuLLWjbv9x9iJkxwvyK5A-HXkQb42U2jzORjcJFXi_1h7R-c9T3YfOX0iXCND7xzyH7QcIFSETFEvyaJYVpbIarsdciysm-TWikTv2JpSmJ6Shw7b7t03W-VRam0BN7S2H56rHt2oBsqSNiETqlViPg3pqz74pb5-bx48443TX3kK-DJIql06B4iyAnBdlESWW-jE15VEQZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه کافه مذهبی با آپشن‌های فوق العاده توی تهران راه اندازی شده:
نوشیدنی‌های خارجی مثل کوکاکولا حرامه.
موقع اذان، توی محوطه کافه میتونین نماز جماعت بخونین.
پرسنل قبل از پخت و سرو غذا و نوشیدنی، حتما باید وضو داشته باشن.
کافه، نزدیک مزار شهداست و میتونین دیتِ خودتون رو اونجا ادامه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69947" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69946">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69946" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69945">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e51Omui-cN9fep5iJuDv4fe6IEsPU5jmVK8qOgmJeTddEHR_YW2dgQ4513FSMQVaUiYGB12zSx92Si68AvoZdDo_eyXBlCe1kSxv4-N0njedezqKVY1rFaqgDDahmtRoFuLP6g0Yi_q4iKaVCJhlKF5HziT7pWbmiNdI389BGH0jv37LLZ5p6zEBZhq0E_c9jl9arZO3zNXIxjuV38-b0Wd47F0pwKeaGZ6ioD_Ww8GgjCgXCOh2xHZAqSWP8LLZAgaBPEf-bTGqZBkRkCCIxQk6RtWOmsIXTeTtLxhvEZFh8F1KACSXYhEvxMlSRPvzxgeAhAGfs8UjPYc2OO1CYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g21
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69945" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69944">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq-RTAoL-1WVNY_1Wzoxa-nbIYjUSsrm5eF_ONoC5NKlwpLqgbCiSCIyWtvCFx8pCQVnwG2qqLlAEijrUeVB8UDWqOIcO4MfX7r6h42SbwPbkFMoWH05lxrkVS6q5b-y2uOxN7UBBeiUtKU9V3Vt_MGfo4IhZ74T43jB9YPvyY1etkAxOWt2u6a6ATPxQmWO_hh6gWxi-A0ft9MLhyMvEdcZOQJL7sJncuDB-pRFEjKXDLGhBgNo2YsOleqFAxzLMd49ACpHZ4klKrMrzUZrRW26ba1tn4QD0ae1DtZZPkWltnTygqy46H9_WtyloK3rn5YZZd-ZqzT_MUkxIi1H2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
همه، محاصره دریایی ما را «دیواری از فولاد» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد.
آن‌ها نه نیروی دریایی دارند و نه نیروی هوایی؛ سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران درهم‌شکسته و در حال فرار است و وضعیت «رهبری» آن‌ها در بهترین حالت، نامعلوم است!
آن‌ها پولی ندارند؛ کشورشان «از هم پاشیده» است. تنها چیزی که دارند «اخبار جعلی» و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر هم می‌شود!
ایران فقط حرف است و عمل ندارد؛
دیگر خبری از آن قلدرِ خاورمیانه نیست.
ستایش از آنِ خداست!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69944" target="_blank">📅 18:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69943">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=hZFDnJASfVNJztuyP1NYz9DwQIrPZ7JyW2m-RAo4dop-7L4aGftalBm72Bs_b0Q7IQaszbVvCycAqXYMwhzZyHBp9bZKb8nF_kR0UA18WL_O6uaklGXV5lXO1fECGlCbTxDbLcW6jOY3qyoNeTvlHnJtmL4zH8C5FN8X1oCoRfPshEdatA1BLPV3pVQlDcppYILQnC1nANvco3zq-tLya7c4B_B5rN6_4O0vKUxZgwMHvp-SCTqpBBMU_gmImnhySLqlcrsKFblzUymXCV6TZtGX_py5_lMAAuwHnSxjd34NtoW_yXx_2h8QyXUtuaNgeI3U4Ntd2CINFTb3X6BQMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=hZFDnJASfVNJztuyP1NYz9DwQIrPZ7JyW2m-RAo4dop-7L4aGftalBm72Bs_b0Q7IQaszbVvCycAqXYMwhzZyHBp9bZKb8nF_kR0UA18WL_O6uaklGXV5lXO1fECGlCbTxDbLcW6jOY3qyoNeTvlHnJtmL4zH8C5FN8X1oCoRfPshEdatA1BLPV3pVQlDcppYILQnC1nANvco3zq-tLya7c4B_B5rN6_4O0vKUxZgwMHvp-SCTqpBBMU_gmImnhySLqlcrsKFblzUymXCV6TZtGX_py5_lMAAuwHnSxjd34NtoW_yXx_2h8QyXUtuaNgeI3U4Ntd2CINFTb3X6BQMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
روایت دختری که در 13سالگی به همراه مادرش از کره شمالی فرار کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69943" target="_blank">📅 18:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69942">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=U8eSdcOVOjKkTzG9Iuo6i-Z7YBRlxS6uccLvB2CwhewrK-1HUS7xGJRt4Z8Sp7-oWBZs4do4tQ55oexjcskZSh52FrRyc6dJM6PPU7uOV-3PRWzMsBjNUdah290CPegalnf88YIizZOCyQjM0lKsGUB8SC0IKyvF_N10lXU2UjbYdaGbx8PuFuhmVG5y3HM_9hYTFKLVq5tYItcT26jaJZBi-d9aNh5eV47gLTt9_9293xnK_RRwdSF8vKZKpB-3fh45sZeLwTsAkeeAPGtWNjUOvwDok_qXzf5T8plBLiHamziYnnU4C4-_jcbfDt4PXUVCBdJdrhb6WjrRWtkkNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=U8eSdcOVOjKkTzG9Iuo6i-Z7YBRlxS6uccLvB2CwhewrK-1HUS7xGJRt4Z8Sp7-oWBZs4do4tQ55oexjcskZSh52FrRyc6dJM6PPU7uOV-3PRWzMsBjNUdah290CPegalnf88YIizZOCyQjM0lKsGUB8SC0IKyvF_N10lXU2UjbYdaGbx8PuFuhmVG5y3HM_9hYTFKLVq5tYItcT26jaJZBi-d9aNh5eV47gLTt9_9293xnK_RRwdSF8vKZKpB-3fh45sZeLwTsAkeeAPGtWNjUOvwDok_qXzf5T8plBLiHamziYnnU4C4-_jcbfDt4PXUVCBdJdrhb6WjrRWtkkNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه روش فوق العاده برا تقلب در صورت آموزش تصویری
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69942" target="_blank">📅 18:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69941">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⏸
صحبتای یه فرد رندوم:
سوال من اینه؛ چرا بعد جنگ 12 روزه خبری از این تجمع‌های شبانه نبود، ولی بعد جنگ 40 روزه شروع شد؟ دشمن که همونه؛ پس چی عوض شده؟
دلیل این تجمعات شبانه مخالفای داخلی‌ان یعنی مردم خودمون؛
مخالفای حکومت هم مردم همین کشورن، وطن‌فروش نیستن. ممکنه با حکومت مشکل داشته باشن یا طرفدار یه مدل دیگه حکومت باشن؛ خب حق دارن نظر خودشونو داشته باشن.
اگه واقعاً می‌خوایم بدونیم مردم چی می‌خوان، یه رفراندوم برگزار بشه تا نظر اکثریت مشخص بشه.
سال 57 یکی از اعتراض‌ها این بود که مردم آزادی بیان ندارن و مخالفا سرکوب میشن، اگه الانم مخالف نتونه حرفشو بزنه، پس دقیقاً چی تغییر کرده؟ مخصوصاً وقتی وضعیت اقتصاد، روابط خارجی و خیلی چیزای دیگه هم بدتر شده.
در نهایت هر ایرانی می‌تونه کشورشو دوست داشته باشه، ولی در عین حال منتقد یا مخالف حکومت هم باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69941" target="_blank">📅 17:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69940">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Swxm8SmVv9lNpZ7VgBHzYtEbcGYt4oAOZWClWV59l86OqhXJJScObs_Fdw02PVF7Bkss5WpuE-aIPQAayEb4GncyztbWDOrjggl61D-MqUpgwkhlZDPtozQa2mI-a6TYOU0tO8TGVmoK46V8J64r07P59GeEEn6JLi4NMfc9N0UMzj9tSOAJVTAVmOfHiGAeGeREECEMoMiLT_alhAJERwGEINALvibr0IAyJlg89VsKuyNzewv7ouypbQxU5Z5eyv5SByjzLfEfYhrvU902tR_TmcCXHYuwn5sSZKrA8alLHh63-he4xUSy5esXtEXHLOd1knDubVsRa_PHv75rMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا، یه آخوند به اسم  "شیخ ‌احمد " چنل آموزشی با موضوع مقابله با غریزه جنسی فرزندان راه انداخته
😶
مادری که پسر جوان تو خونه داره، نباید با آرایش و لباس آزاد تو خونه راه بره، باید چادر بپوشه چون باعث تحریک شدن فرزند و راست شدن شومبول وی میشود!
همچنین پدر نباید با شورت جلوی فرزند دخترش راه بره، باید حیا داشته باشید.
پدر مادرا جلو فرزندانشون همو بغل نکنن، وگرنه میرن جهنم
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69940" target="_blank">📅 17:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69939">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oFk3SLm1P3IiPkCLw7RtL6LoTzrjq7Q9vekMiVjc1_OH52gZ7D5tjyvniHHuh68ERVF-l39A8j1C9ZGRXi9D7yH2MvSSOwhRqIYYATItuP7bLyzpng9vDsqx_RDeZljVAaItas7bABXG-jlglOxXoG4K0IKxND4IWn4f78QNQyOnRO2bJ5OgK9ALhQehnmYst3OhuWKsCMJctYLxMoXUygv3uI0UgJJcslDa2YswIHHXyhBUQT4hdiLxQ5RdXVAudGJdxyp_oqNiYsJv8qH4QNt3VEWORBKsZTUVHPC6C8UZCvUt481DgJ7IB9qH3LiQ67UsOf7mo4vk1wCVB3d3KY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oFk3SLm1P3IiPkCLw7RtL6LoTzrjq7Q9vekMiVjc1_OH52gZ7D5tjyvniHHuh68ERVF-l39A8j1C9ZGRXi9D7yH2MvSSOwhRqIYYATItuP7bLyzpng9vDsqx_RDeZljVAaItas7bABXG-jlglOxXoG4K0IKxND4IWn4f78QNQyOnRO2bJ5OgK9ALhQehnmYst3OhuWKsCMJctYLxMoXUygv3uI0UgJJcslDa2YswIHHXyhBUQT4hdiLxQ5RdXVAudGJdxyp_oqNiYsJv8qH4QNt3VEWORBKsZTUVHPC6C8UZCvUt481DgJ7IB9qH3LiQ67UsOf7mo4vk1wCVB3d3KY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کلاس درس «ریاضی ولایی» با تدریس محمدباقر خرازی:
«شما اگر ولایت داشته باشی می‌ری زیر خط کسر...
اگه شما به این دکترای ریاضیات رو بخونید اصلاً این‌طوری نمی‌فهمن...
حروف قرآن از راست به چپه اما انگلیسی که زبان شیطانی‌ست از چپ به راسته...»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69939" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69938">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
🗞
رویترز به نقل از یک مقام ایرانی:تهران و واشنگتن در مورد تمدید آتش‌بس گفتگو نمی‌کنند.
این منبع افزود که از دیدگاه ایران، هرگز تاریخ رسمی آغاز آتش‌بس وجود نداشته است و بنابراین، چیزی برای تمدید وجود ندارد.
این منبع ایرانی، ایالات متحده را به نقض توافق‌نامه همکاری متهم کرد، این در حالی است که این توافق‌نامه تنها ۴۸ ساعت پس از امضای آن نقض شده است.
این منبع همچنین گفت که مذاکرات فعلی بر بازگشت واشنگتن به توافق و تعیین یک جدول زمانی برای انجام تعهداتش متمرکز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69938" target="_blank">📅 15:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69937">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e246580c.mp4?token=m1NHS7AypvnrjNFervCvnFj52XX3kArYJZgkTaH5yc_1_0eDUWrxePDHFe3bpjbziGlPFZquGbeqAIHreeFwvQD_vUkPQvmJGQSk_6uwDqZNVh5hb1SnMAWwCljKVicRHr7oVRIMSQh2GjZYHylT0fcgjoxfp2cYUBtRs6hjItM246SjllhUUsjZ5ZQIF1qbLA_l5G17wyGxb2V1ACWMtHtui5CB_pPpW7PPFjlsr-j1ZpnMvom49DvgPLZM5_SsmTb6N3Q0PLU6witjUOZK8o24r83Jccpotod6C09B-r9VwawjyKp6fIZ9My2vCxk_SSz1_rmB5o8l9-3Gbk9IdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e246580c.mp4?token=m1NHS7AypvnrjNFervCvnFj52XX3kArYJZgkTaH5yc_1_0eDUWrxePDHFe3bpjbziGlPFZquGbeqAIHreeFwvQD_vUkPQvmJGQSk_6uwDqZNVh5hb1SnMAWwCljKVicRHr7oVRIMSQh2GjZYHylT0fcgjoxfp2cYUBtRs6hjItM246SjllhUUsjZ5ZQIF1qbLA_l5G17wyGxb2V1ACWMtHtui5CB_pPpW7PPFjlsr-j1ZpnMvom49DvgPLZM5_SsmTb6N3Q0PLU6witjUOZK8o24r83Jccpotod6C09B-r9VwawjyKp6fIZ9My2vCxk_SSz1_rmB5o8l9-3Gbk9IdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حرکت عجیب مجری در پخش زنده
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69937" target="_blank">📅 15:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69936">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMo031n12AHsRO78pIvDlLta1CDdlvWSXp3kSz5wp2YywxV8gT8_0NcHI4L_gxSPHiLZ9tuvRYFG3PzhVwJqo2nZasxaf3Qr1KU_Ak4RGccV2ioiinWGrHVN9t0eBW-lYuuWkGBnN3A_4us38lX13v400HBRG19CQYkvFqUXhEj2okAHBra-QkshAMN_LsqmhSGqHM5vj8dZkxKGOiKawcRa5fWXuAgC0dIwA-ACovNPpFND6tWroelo63T6pzcXfCm_ivPULnLcxSGmI4Duio8PuUZFM9fU-0B6yA1eixg1wFi9NZiHnLob5Ra9Wl2_XvZLZxKa5Y6cToCRrZNdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
🇹🇷
🇺🇸
نیویورک تایمز:تهدیدی که از سوی ایران مطرح شد و باعث شد رئیس‌جمهور ترامپ ماه گذشته به طور مخفی هواپیمای "ایرفورس وان" خود را تغییر دهد، زمانی آشکار شد که او در آخرین روز حضور خود در اجلاس ناتو در آنکارا، ترکیه، در تاریخ ۸ جولای، در حال عزیمت بود.
اطلاعاتی که توسط سازمان‌های اطلاعاتی آمریکا جمع‌آوری شد، نشان می‌داد که یک تهدید خاص از نوع موشک‌های زمین به هوا علیه هواپیمای "ایرفورس وان" وجود دارد، صرف‌نظر از اینکه کدام هواپیما حامل رئیس‌جمهور باشد.
همچنین، فردی که در نزدیکی محل برگزاری اجلاس ناتو حضور داشت، در حالی که یک موشک قابل حمل روی شان خود داشت، مشاهده شد. در همین حال، عوامل ایرانی دقیقاً می‌دانستند که ترامپ در آنکارا در کدام محل اقامت دارد، از جمله طبقه محل اقامت او در ساختمان.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69936" target="_blank">📅 14:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69935">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=qLlUMCd2FnBOjy0MiTmgXJdC2VvzFFFJ912GxifRw0ONZX0KTVxQEmXnht4rqsFuUFBHHgMaB88cFPbivXmJksVMv5h3yDsrVY4Si1Fmv9ndXArO3ACrVMEqCNEjVzbAwxvQxl0Lp1083nItYTiG1eBqqP_wVPLmTYS9Bjv2fVP0IQ21i54wQLUegQsU8rDCfFWA6nG1RS02LNFXLYRuKwwMFM1dsj_4ulojLNfvdQBOLl2YyNzYxNV5tO4Z4XvvO0K3AzDMi8ntFAcidCvawHEmEz_siAik5lXxCVl0LZq18Y867NPNvzc4Qls7uKxsuTB5qv38duwxxCA-K3JB4qceBeOQswvqydeN-2Tm5l_-rGUQWkkcyOIt0WkC7WzIZcFKhU-K5a6nNSHAArXqp3FzCOViFOPs7Eh2BHPaZ10tjJLxNzw3LSd64aFCutOCwwae5X-fDky0f8f1h5b74o11CgTH0md0i2x8JVIg3H5UcYDiNdkh8l09i9b285GdXigsYfoEr5J3q83ykW0jTvY8NDTzabk8ZN3nYgcsBp1jmuxcGJwM1ako2BG0_6_uqtwXoJ63dbCyUWbNiI2kmD3_42wJzehPRdQkpS0Q-EyYtytRj0xJ7E3S8VtaBzDmTp251ePeIv1OJMxKzEOmwh3B8HGoUfpVeC2Ukb7qEj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=qLlUMCd2FnBOjy0MiTmgXJdC2VvzFFFJ912GxifRw0ONZX0KTVxQEmXnht4rqsFuUFBHHgMaB88cFPbivXmJksVMv5h3yDsrVY4Si1Fmv9ndXArO3ACrVMEqCNEjVzbAwxvQxl0Lp1083nItYTiG1eBqqP_wVPLmTYS9Bjv2fVP0IQ21i54wQLUegQsU8rDCfFWA6nG1RS02LNFXLYRuKwwMFM1dsj_4ulojLNfvdQBOLl2YyNzYxNV5tO4Z4XvvO0K3AzDMi8ntFAcidCvawHEmEz_siAik5lXxCVl0LZq18Y867NPNvzc4Qls7uKxsuTB5qv38duwxxCA-K3JB4qceBeOQswvqydeN-2Tm5l_-rGUQWkkcyOIt0WkC7WzIZcFKhU-K5a6nNSHAArXqp3FzCOViFOPs7Eh2BHPaZ10tjJLxNzw3LSd64aFCutOCwwae5X-fDky0f8f1h5b74o11CgTH0md0i2x8JVIg3H5UcYDiNdkh8l09i9b285GdXigsYfoEr5J3q83ykW0jTvY8NDTzabk8ZN3nYgcsBp1jmuxcGJwM1ako2BG0_6_uqtwXoJ63dbCyUWbNiI2kmD3_42wJzehPRdQkpS0Q-EyYtytRj0xJ7E3S8VtaBzDmTp251ePeIv1OJMxKzEOmwh3B8HGoUfpVeC2Ukb7qEj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران:
«ما بیش از نواخت شلیک موشک‌های بالستیک، در حال تولید و تحویل آن‌ها به رزمندگان هستیم.»
«ما فقط ۹۵۰ شهرک صنعتی داریم به علاوه صدها مجتمع صنعتی که خارج از این شهرک‌ها هستند.
اگر روزی برسد که ما هیچ موشکی هم نداشته باشیم، ما خطرناک‌تر می‌شویم چرا که دشمن با تاکتیک های ناشناخته ای مواجه می‌شود که می‌توانند منافع آمریکا در جهان را به آتش بکشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69935" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69934">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag1KuYeyKwCWzY9_eT-sUuo8qIWOWCk2MKnL3FuhdwTGP2PtuCzvZIqAdoWFQ7nHJiL02a3pHMf-W7mqd-zTTap4sNjnCe7pqMoDsvAZZ85-PU_eBmvKY63ycKn8_CSnzHR1st89qh5UGwKcTR9vWH2oeuToP1lmvUqmcMa0prUeZHTw5oEzCvYACRZ7PCbdr7Ou4FOE1--gOdjfZGvbMeUBdkjctkDH_SCo2OvTdxH6h29zxmQCw7CjqWgVK3DoxN4Fc-vIvDOUVnLx6bkVsCqhN-Mgumf98YDwq_Grp1FZyJ2C2HUV_LX5uMaa5TmPFa6k77_-r0HbrIxE_2kFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69934" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69933">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=V0JA7-sqkdKCswksnzigd09-fIadIqZRkWI650pqxSaSjWfvmFX-I7y4TFRABVXmuda5vNQ0zxWZg4zJgfxHfoaBrfeqfniP3kgH5GoVqane5o_zEEEALoRsK1Bp_j5js3pKKHd6POq4iFEcXC7QVSOgrU5hudV1yOkGz4wVIwi79FO8vBzdV_ZCaLUcvhM-MFD_xMk-jz7G1p6SyyjsXUBOUCW0ztAgbtBo8C-PBlxgohyzlvVFxzVTpZ-NMjofSVBD2L1Bx1PV1P7WHGdblJvaR5cARADiGf0RA6avZGUmfXxVcLOmPSlM24yhYTq8OL1N9Kd2ruoBwiS6TLeY-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=V0JA7-sqkdKCswksnzigd09-fIadIqZRkWI650pqxSaSjWfvmFX-I7y4TFRABVXmuda5vNQ0zxWZg4zJgfxHfoaBrfeqfniP3kgH5GoVqane5o_zEEEALoRsK1Bp_j5js3pKKHd6POq4iFEcXC7QVSOgrU5hudV1yOkGz4wVIwi79FO8vBzdV_ZCaLUcvhM-MFD_xMk-jz7G1p6SyyjsXUBOUCW0ztAgbtBo8C-PBlxgohyzlvVFxzVTpZ-NMjofSVBD2L1Bx1PV1P7WHGdblJvaR5cARADiGf0RA6avZGUmfXxVcLOmPSlM24yhYTq8OL1N9Kd2ruoBwiS6TLeY-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سفره‌ای که واسه عرق‌خوری تو زندان پهن کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69933" target="_blank">📅 12:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69932">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=f8D3ZG_cE_pYHn0PaoYqBzE3eDqnGk8ypb5k4zcSHcyQcpjK0oXTNpz-ir07zDS8T1jbvRftCcS7zLgySp_VYnwfR7CBIZOkTPsi8bpNSq20svO86UvSMZ91I_9zfUNDC6SZ-M12B2J3mnndQ0oGNEDs_vFlVKP9-qsIcQPlieyNGW0QTHMMm6nwBgo12asvOqSHM2nCK3h5o78PikVGi84G28MP7WUd4WpL-RRbkWjt6MeeaEzy9-5xpM2I-kHdNjEsxjh8LZSBakTdhhpM08MdQWQclYdJeuDrW85FbYudRcJNM90qtvslL6CuLPeTfAyFbTbW2wvKH7JXvVJBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=f8D3ZG_cE_pYHn0PaoYqBzE3eDqnGk8ypb5k4zcSHcyQcpjK0oXTNpz-ir07zDS8T1jbvRftCcS7zLgySp_VYnwfR7CBIZOkTPsi8bpNSq20svO86UvSMZ91I_9zfUNDC6SZ-M12B2J3mnndQ0oGNEDs_vFlVKP9-qsIcQPlieyNGW0QTHMMm6nwBgo12asvOqSHM2nCK3h5o78PikVGi84G28MP7WUd4WpL-RRbkWjt6MeeaEzy9-5xpM2I-kHdNjEsxjh8LZSBakTdhhpM08MdQWQclYdJeuDrW85FbYudRcJNM90qtvslL6CuLPeTfAyFbTbW2wvKH7JXvVJBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تصاویری جالب ، از تلاش ناموفق یک تیم آتشبار سیار روسی برای رهگیری یک پهپاد انتحاری (کامیکازه) در حال عبور را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69932" target="_blank">📅 12:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69931">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=uPowk23Z9AoFIbCVOicVZjnjBbTkUMKOl-U7xn58SHUKRLG3RclafWITpYBVB6wFsD7LNqSq2IuoBYNflVsHts_3IJlAoU4_rXtnZapNXMpZ-eQ70kZ4WWECe7U_St85FnVYA6Rt31wc81cd8Yx1u5c4nt6pWW-ZCGrHYeAGXbXvGVaKSvj97YKktbVT2ZKS86yKnEfmTQlxGneORmxMByhbLM2ifWZVA_JKs_mSiKLAVOkHbMUPyTCqFgCHeZvMUJvq8iqrVz2bz8WQfleSFzkJIpyvm1eP-9syK1bn1aT-541JpGbqmuewUwCL-aTLCL9hpDFHxsAY_pSiseE9MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=uPowk23Z9AoFIbCVOicVZjnjBbTkUMKOl-U7xn58SHUKRLG3RclafWITpYBVB6wFsD7LNqSq2IuoBYNflVsHts_3IJlAoU4_rXtnZapNXMpZ-eQ70kZ4WWECe7U_St85FnVYA6Rt31wc81cd8Yx1u5c4nt6pWW-ZCGrHYeAGXbXvGVaKSvj97YKktbVT2ZKS86yKnEfmTQlxGneORmxMByhbLM2ifWZVA_JKs_mSiKLAVOkHbMUPyTCqFgCHeZvMUJvq8iqrVz2bz8WQfleSFzkJIpyvm1eP-9syK1bn1aT-541JpGbqmuewUwCL-aTLCL9hpDFHxsAY_pSiseE9MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از هجوم انقلابیون به کاباره های تهران و نابودی هزاران لیتر مشروبات الکلی، در سال 1358
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69931" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69930">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/69930" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69930" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69929">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FcxjLEHE-W_9ybtUfS1RzSufF_xTOezEYaSUT9eygmnw8bdDVqOHrVqaYMpaCX6UBduJkH0V7pVjtjJZCEAyuIk7LM2ByNph3wsWZwBk8NpAztnNRIcrI2o2FB3FALcZJYd20DAoB6F3jq-Qhuujf44o8fRj2EA_lh5rPJSsZIMu3e5wJ5j0OYfvEif3dsqyD6_TK_sskMGHOvNRBvebsTXueVegpVJ3Gay0L0i6imfZG6cGMxGQ7LgjU3fVRoP3_8TS6W3vWDDPRyljVCl69kE6ahkaDRSP6Ac-crEGNmnU5xJ3vlNn6MnNmhI0G6kHpSZlQcu_aPO58jtHAYuHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69929" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69928">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=qgZU00m-NJj4FPwOwy00QC7vFSToES7YyefNuyxiruaf2zOQ0RdHepN9aP1wnbr317LoJ_zKdREgbc1ksprJYnUYmuny798qO7zk-3SOlWWn2R7Hs7RvyIBRc0m7zG8Ibt7p6KB5earI4ADomO5NUY38LiG1si8fOGVL6g18VOv0LSr8LtatBdtK1TjaihF6Xnyyd-UPLbS86dRPRn3uEvWpP1vNvMxTunf3dNk6T-NOk2FLxZg9H5DMulI7ka_j8R7uxeqgvdDO3Pcs5L9E18lSPkGgVZ5Lh7E99KpG38fUhp9OWhH5GLe9OZXefQIUHdqXzG4Zti9gNtiAjutLjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=qgZU00m-NJj4FPwOwy00QC7vFSToES7YyefNuyxiruaf2zOQ0RdHepN9aP1wnbr317LoJ_zKdREgbc1ksprJYnUYmuny798qO7zk-3SOlWWn2R7Hs7RvyIBRc0m7zG8Ibt7p6KB5earI4ADomO5NUY38LiG1si8fOGVL6g18VOv0LSr8LtatBdtK1TjaihF6Xnyyd-UPLbS86dRPRn3uEvWpP1vNvMxTunf3dNk6T-NOk2FLxZg9H5DMulI7ka_j8R7uxeqgvdDO3Pcs5L9E18lSPkGgVZ5Lh7E99KpG38fUhp9OWhH5GLe9OZXefQIUHdqXzG4Zti9gNtiAjutLjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قیمت های پشم افکن خونه و برج توی فرشته تهران بعد از جنگ که به متری 2 میلیارد تومن هم رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69928" target="_blank">📅 11:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69927">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=ipw28SwwPA1LHzQtpkgHSL7ElMRPgKksXOjlGj9gKTDOD2rqNGP8Pvea5xP2qF9318y2TN2u3lTBQfazDOmXtTX7ZfSBbNFMGcRy9hJdljL08PfVbE2sxxPqVT-xbIYae68MwME7Yqs1iR_JgxACRY1h6muzfuaHGNMFSdpezu23XpqfVO0_YGxseoYGcm715T_1ztPc3206wQ5VNZBbexBsh5S9emOve6rl0BUgyCnApMtgZOoHFlPswgXs-BnCky6D8jxvzS7BgLfaQ_KVPLBRyjV8TOLobshO3IAit3mRohdb9v1jekc9clXFHU9fM6og8XIw_Kc0uUqeBz70nyVpcWwU61AaBrv1F1h6dBZSIjHzRtsonDonEbafM42zZqYWFtui6kCMhxOWw44ay4nXvlJEF9FSdXHl8hNzQ_tsh_xAf-74S5iI8bBZNvVvCGwa3HXyRkWNgEDTOddsqM8qlJsYmvTzLSmQ-d8fZhEJdEv41-SD6frLH48R8iNT1dps55XzRNcG26iVg7_sHAEkIiuReZmWBgGTje5TzZr00FgJR4q7H02c77zHmyYdqIilhAUnDRMzGlAY05iNN1GtJjM73qDAseVasIYcN-IDalqf6Jv3AFZIPIhsGMUmUmlCo2iNIlxUK_vKMLlZhQYtNq3umiiyf50ysYLhoBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=ipw28SwwPA1LHzQtpkgHSL7ElMRPgKksXOjlGj9gKTDOD2rqNGP8Pvea5xP2qF9318y2TN2u3lTBQfazDOmXtTX7ZfSBbNFMGcRy9hJdljL08PfVbE2sxxPqVT-xbIYae68MwME7Yqs1iR_JgxACRY1h6muzfuaHGNMFSdpezu23XpqfVO0_YGxseoYGcm715T_1ztPc3206wQ5VNZBbexBsh5S9emOve6rl0BUgyCnApMtgZOoHFlPswgXs-BnCky6D8jxvzS7BgLfaQ_KVPLBRyjV8TOLobshO3IAit3mRohdb9v1jekc9clXFHU9fM6og8XIw_Kc0uUqeBz70nyVpcWwU61AaBrv1F1h6dBZSIjHzRtsonDonEbafM42zZqYWFtui6kCMhxOWw44ay4nXvlJEF9FSdXHl8hNzQ_tsh_xAf-74S5iI8bBZNvVvCGwa3HXyRkWNgEDTOddsqM8qlJsYmvTzLSmQ-d8fZhEJdEv41-SD6frLH48R8iNT1dps55XzRNcG26iVg7_sHAEkIiuReZmWBgGTje5TzZr00FgJR4q7H02c77zHmyYdqIilhAUnDRMzGlAY05iNN1GtJjM73qDAseVasIYcN-IDalqf6Jv3AFZIPIhsGMUmUmlCo2iNIlxUK_vKMLlZhQYtNq3umiiyf50ysYLhoBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداشمون در یک دقیقه به ۱۳ نفر پیشنهاد رابطه داد و  همشون هم ریجکت کردن و تونست رکورد ریجکت شدن زیر یک دقیقه دنیا رو بزنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69927" target="_blank">📅 11:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69926">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
لحظه نابودن شدن خونه های مستحکم و نوساز توی کلمبیا بر اثر زلزله!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69926" target="_blank">📅 10:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69925">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=CezoQv84dXhjcmNEQ75P1z77gwcU00OBE25iOcUlZCAwqZCMH57yAyd8AcLXECTu5mwtWtKXVV5LR08tGOVaeTWPAwsKsi1QEJSbHZLu_1O9AEWkcd6IIW3Rmema-dkV6VY2lsS85J58CxGrYZiBMhkms8cAMv6n3TPj_t01SAj6y7c6iv9KUDXgkM75gG5FqaAIydEAocR1xQSZfvSU_ME3Ka9Yuq4T7qFeLzEQ5HKFCe0x02WuOdjvz85cPgf0DpvhIF3xeBhiiXU58rgY-tEk751RUPQQlG1HbCejrfQirXjzf399IpaqVEoUU1E_S-qROAITsL9hekBNYvu_BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=CezoQv84dXhjcmNEQ75P1z77gwcU00OBE25iOcUlZCAwqZCMH57yAyd8AcLXECTu5mwtWtKXVV5LR08tGOVaeTWPAwsKsi1QEJSbHZLu_1O9AEWkcd6IIW3Rmema-dkV6VY2lsS85J58CxGrYZiBMhkms8cAMv6n3TPj_t01SAj6y7c6iv9KUDXgkM75gG5FqaAIydEAocR1xQSZfvSU_ME3Ka9Yuq4T7qFeLzEQ5HKFCe0x02WuOdjvz85cPgf0DpvhIF3xeBhiiXU58rgY-tEk751RUPQQlG1HbCejrfQirXjzf399IpaqVEoUU1E_S-qROAITsL9hekBNYvu_BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های یک مقام حکومتی رو ببینید که باخنده درمورد شلیک به سر معترضا صحبت میکنه:
ما به پای معترضین شلیک میکردیم ولی میخوابیدن میخورد به سرشون
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69925" target="_blank">📅 10:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69924">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=pO6GSUBgR4aQlBf32XgYgeeNNtFCwx_B7HdpELxtVwLk9l5nbKKccA9s6u3PIc7qP-dIAf_yygmwL1YhgRukaIWhNQn6g9cbPp-bPjsyC_xdfir5rsJlfuOVtUYNCkHddhpqT2qN2S77v_5VTCZZAttqMy9g3O7SBbiwYNalLHVrGVP422-6G2Z575N5XKRalFGVvD21WGMrAezj_P9fvTaLkuzISSbRpoTO8H6c7S0-DrtoB4puxLN8UYPdZOcZU-0UA8pkkhmE7-sKork1XrrKo-Jo9CXwoJcEsbZYpu-VSDy19aCjfpmeAmm2YDGIbuS4_zIS7jR9IcGhzF9zLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=pO6GSUBgR4aQlBf32XgYgeeNNtFCwx_B7HdpELxtVwLk9l5nbKKccA9s6u3PIc7qP-dIAf_yygmwL1YhgRukaIWhNQn6g9cbPp-bPjsyC_xdfir5rsJlfuOVtUYNCkHddhpqT2qN2S77v_5VTCZZAttqMy9g3O7SBbiwYNalLHVrGVP422-6G2Z575N5XKRalFGVvD21WGMrAezj_P9fvTaLkuzISSbRpoTO8H6c7S0-DrtoB4puxLN8UYPdZOcZU-0UA8pkkhmE7-sKork1XrrKo-Jo9CXwoJcEsbZYpu-VSDy19aCjfpmeAmm2YDGIbuS4_zIS7jR9IcGhzF9zLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:«بازندگان و برندگان انتصابات جدید در جمهوری اسلامی چه کسانی‌اند و آرایش جدید قدرت چه چیزی به ما می‌گوید؟
🔴
انتصاب محسن رضایی به دبیری شورای عالی امنیت ملی و حسین طائب به فرماندهی بسیج، دو پیام مهم دارد؛
یکی رو به بیرون، درباره مذاکره، جنگ و رویارویی با آمریکا
دیگری رو به داخل، درباره مهم‌ترین نگرانی حکومت: خطر خیزش دوباره مردم ایران.
در حالی که هنوز درباره زنده یا مرده بودن مجتبی خامنه‌ای و میزان سلامت او تردید وجود دارد، سپردن بسیج به حسین طائب، یکی از نزدیک‌ترین افراد به مجتبی، یک پیام روشن دارد:
نگرانی اصلی حکومت، خیابان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69924" target="_blank">📅 09:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69923">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=KjPmeiiDjlu4HKtCwq1Ke6K4aod019au3jdMar9U7zWGNreAX1YS5AGmSeU96C8Qry62D0lSEdLvslfhHKj1CKbq-bj5ScMjN8cQArCgJ6TEoAHzHOvYtCj96gjiSTb7z-jp55Kj4HlNiG7jl6Zw2bo1vMrOMHspXJNb2S1SmA1PGrNc3cbBh4Qp4WMSjoMn0NiQMR0BXzailhUQaWG6hz2UiGBcrW2OOWPw_EWkC7mKzdrUf2LeJWCViokOjf1Vcq4lEUWIoRdv7SPTSOHwz0rQk2zWGFWoaLq-FartCD3FQjztneZP-Wi4V3ahdbw9V8eD9YudQSFXYk5QUX2xdrk-BSahzUECp9NnmuojYvIS2ctvTTl9gJ_PHDo75jdIR-HiXQ_Hvhr_qqXU05gcZ35BCEP6kp617Okhb5FY5wrKSREm8svHXPlxe4jyCHibisnyO9ODZwPKWR0biBEtfM8ZT2mzn_HEhj7RMY9z__G8sUdPKHQjQfeLN2pJ2amAtvvB-pHu--nT-cjCc5D0GmcaGWtjio5KjOphbfI_jkq0ubrjfBe6qUwFtJNTz8XpN8xuGKuIyjMekFuxAUuzgBVUbY6pxZqcK2GsTa_09Jwv1nXJfnjJTNmCAzo_r58u116dbzHyp4xrCk0s-zyUr-mRQYi6JpChQBWcwIwhlr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=KjPmeiiDjlu4HKtCwq1Ke6K4aod019au3jdMar9U7zWGNreAX1YS5AGmSeU96C8Qry62D0lSEdLvslfhHKj1CKbq-bj5ScMjN8cQArCgJ6TEoAHzHOvYtCj96gjiSTb7z-jp55Kj4HlNiG7jl6Zw2bo1vMrOMHspXJNb2S1SmA1PGrNc3cbBh4Qp4WMSjoMn0NiQMR0BXzailhUQaWG6hz2UiGBcrW2OOWPw_EWkC7mKzdrUf2LeJWCViokOjf1Vcq4lEUWIoRdv7SPTSOHwz0rQk2zWGFWoaLq-FartCD3FQjztneZP-Wi4V3ahdbw9V8eD9YudQSFXYk5QUX2xdrk-BSahzUECp9NnmuojYvIS2ctvTTl9gJ_PHDo75jdIR-HiXQ_Hvhr_qqXU05gcZ35BCEP6kp617Okhb5FY5wrKSREm8svHXPlxe4jyCHibisnyO9ODZwPKWR0biBEtfM8ZT2mzn_HEhj7RMY9z__G8sUdPKHQjQfeLN2pJ2amAtvvB-pHu--nT-cjCc5D0GmcaGWtjio5KjOphbfI_jkq0ubrjfBe6qUwFtJNTz8XpN8xuGKuIyjMekFuxAUuzgBVUbY6pxZqcK2GsTa_09Jwv1nXJfnjJTNmCAzo_r58u116dbzHyp4xrCk0s-zyUr-mRQYi6JpChQBWcwIwhlr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
من به ایران اعتماد ندارم. من آخرین کسی هستم که به ایران اعتماد می‌کند. آن‌ها مدام به من دروغ گفته‌اند.
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آن‌ها کنترلی ندارند؛ ما کنترل کامل داریم. آنجا در اختیار ماست.
و شاید زمانی آن‌ها دست به کاری بزنند و آن‌وقت نابود خواهند شد. اما فعلاً در موقعیت بسیار خوبی قرار داریم.
ما با کشوری سروکار داریم که ۵۰ سال قلدرِ خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال می‌شود، مگر نه؟ ما چهار سال بود که می‌گفتیم ۴۷ سال؛ و حالا دیگر آن‌ها قلدرِ خاورمیانه نیستند.
🔴
ترامپ درباره تغییر هواپیما در آنکارا:
این موضوع صرفاً به «سرویس مخفی» (تیم حفاظت) مربوط می‌شود. من فقط از تصمیم آن‌ها پیروی می‌کنم؛ بنابراین تابع نظر سرویس مخفی و ارتش هستم.
آن‌ها می‌خواستند که من با پروازی دیگر و هواپیمایی متفاوت سفر کنم ــ که از نظر ایمنی تفاوتی نداشت ــ اما چون خواستار انجام این کار بودند، من هم پذیرفتم. من هر چه آن‌ها بگویند را انجام می‌دهم.
گمان می‌کنم تهدیدی وجود داشت؛ البته من خیلی پیگیر جزئیات آن نشدم. من با تهدیدهای زیادی مواجه می‌شوم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69923" target="_blank">📅 09:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69922">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69922" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69921">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=i7iyDmh94i8o8XLMuGp_ShnFx3r4p1iAG1czI8ZJ3Fcb6jkFTOixxTI-vGrVkCS2sqsneHm8Yj73c7iB_4U6CuFWlo8xztWYF39FWxqwCNOAaX8U9kXQjdGyVq2-cvpDIdXwCDs3TTRfwbKPNp-1MOwVJphAul2cK3-AHDmOnfl_kaXF5CkOGQtY-aN80m5Icf5YDPbQ-FFS8BLMhEfxjt-Fpdu_iSDgrp42cbNhWJZl_y1_rOppBjIP_SC_thM0jJJHI6QzOwFjH6HA9wTMqwANQW1V41P6McdVge8_ZbMBI0gIhDqsadnbXz2gGPOjF2wGn4dI6Fa6KAh1yoKS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=i7iyDmh94i8o8XLMuGp_ShnFx3r4p1iAG1czI8ZJ3Fcb6jkFTOixxTI-vGrVkCS2sqsneHm8Yj73c7iB_4U6CuFWlo8xztWYF39FWxqwCNOAaX8U9kXQjdGyVq2-cvpDIdXwCDs3TTRfwbKPNp-1MOwVJphAul2cK3-AHDmOnfl_kaXF5CkOGQtY-aN80m5Icf5YDPbQ-FFS8BLMhEfxjt-Fpdu_iSDgrp42cbNhWJZl_y1_rOppBjIP_SC_thM0jJJHI6QzOwFjH6HA9wTMqwANQW1V41P6McdVge8_ZbMBI0gIhDqsadnbXz2gGPOjF2wGn4dI6Fa6KAh1yoKS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69921" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69919">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=pAhSsm9bm18VvsRyME66Np3vV_Tc1MaxX60Vm2tpv1OvkkQv0MflNmRn_GFii9LG1247ewF9XJJM2v7vG_TZhpIJCrZuFTcH9rv_9NCOhoy4tQ-BOy03bN3kzobwqbMeqnO23d5Ktyb5zMD_wTRpmLasgKLhTSNQg5iZsKNUKRTovIUB2SJ5VyDhp0YfEF4W7Dib0WmYx9G8fEYTHMOB-Nzc4fIUaIj-AOVg_qhYHyOIa3B0Hr82mE7D6i6vVeyYzvdMo8uVfQM353ihfOWlx-jRkImxUeuLUxtH_hIyS18k3iCgvgaGUQJe4PjEiN9bUV-FWHB_XCvzFulHvvQRfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=pAhSsm9bm18VvsRyME66Np3vV_Tc1MaxX60Vm2tpv1OvkkQv0MflNmRn_GFii9LG1247ewF9XJJM2v7vG_TZhpIJCrZuFTcH9rv_9NCOhoy4tQ-BOy03bN3kzobwqbMeqnO23d5Ktyb5zMD_wTRpmLasgKLhTSNQg5iZsKNUKRTovIUB2SJ5VyDhp0YfEF4W7Dib0WmYx9G8fEYTHMOB-Nzc4fIUaIj-AOVg_qhYHyOIa3B0Hr82mE7D6i6vVeyYzvdMo8uVfQM353ihfOWlx-jRkImxUeuLUxtH_hIyS18k3iCgvgaGUQJe4PjEiN9bUV-FWHB_XCvzFulHvvQRfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی یک مخزن در اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69919" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69918">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=Kr2A32Q5Hx_zPhZudOnNFWC71qkfxSeZu4RhWZQ0j-DRYaeWEmFVwyp9cdPIDh80_L3inslxVC1EoFX5iV1OaAKRG_SY0ML_56wFD8GrKo69J1rp_h4gC0m5ZkjBubXhF7bFruxVfWjPtGLuitrQulbuusP_98MND2N1OsrbxZ6Icyjca4lkt5ZsfIBgcdZ3P1DUa5s1TppDaIIA30O1ZLcP7pzzfTgE8atNFry6E_2TX2SKAntQh34A5dvorMv7T41Dtbs-4iAGvSwVZyB2y7r0jfpCt18FquBP2uRwZBC80mY2rtRbi_Pp_l14CVoEDOk5sEg7QNIYo1DKK8sl2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=Kr2A32Q5Hx_zPhZudOnNFWC71qkfxSeZu4RhWZQ0j-DRYaeWEmFVwyp9cdPIDh80_L3inslxVC1EoFX5iV1OaAKRG_SY0ML_56wFD8GrKo69J1rp_h4gC0m5ZkjBubXhF7bFruxVfWjPtGLuitrQulbuusP_98MND2N1OsrbxZ6Icyjca4lkt5ZsfIBgcdZ3P1DUa5s1TppDaIIA30O1ZLcP7pzzfTgE8atNFry6E_2TX2SKAntQh34A5dvorMv7T41Dtbs-4iAGvSwVZyB2y7r0jfpCt18FquBP2uRwZBC80mY2rtRbi_Pp_l14CVoEDOk5sEg7QNIYo1DKK8sl2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اولین ویدیو منتشر شده از عروسی رونالدو و جورجینا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69918" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69917">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=RjGQLk8qno1kwQ2BFlKmr3OPPJRGJp3b0243rP1sArIn9IVcX02NFU3D-Z7G3KB0gBfDLhlrg-GionDTEPbc1b_asY1djBRZRSRLaLsos-Ua9tJBZkj9sGtUTx8fRsykzxyDMtTsAoeDH5qW5VcTaHnIff-5SrTpOS5_dTwsloiw5VPik6zTRYdHD6cMr4r7APvR2xo7LVPmkL8b97G8_sc7RXZuZQRxQzSOWDHtHX3zaMCdNfszBrNyjizTVg2zQHui-IDQykHOmbmmcL4P2hsDwGt4FofwNgL4Q-LSCDp5cwesPXvnYwD_temxIHXJAranm4urXyRm62Qtfz0t-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=RjGQLk8qno1kwQ2BFlKmr3OPPJRGJp3b0243rP1sArIn9IVcX02NFU3D-Z7G3KB0gBfDLhlrg-GionDTEPbc1b_asY1djBRZRSRLaLsos-Ua9tJBZkj9sGtUTx8fRsykzxyDMtTsAoeDH5qW5VcTaHnIff-5SrTpOS5_dTwsloiw5VPik6zTRYdHD6cMr4r7APvR2xo7LVPmkL8b97G8_sc7RXZuZQRxQzSOWDHtHX3zaMCdNfszBrNyjizTVg2zQHui-IDQykHOmbmmcL4P2hsDwGt4FofwNgL4Q-LSCDp5cwesPXvnYwD_temxIHXJAranm4urXyRm62Qtfz0t-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر محمدرضاشاه پهلوی درباره نفوذ لابی یهود در آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69917" target="_blank">📅 00:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69916">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzepRmyqmEn3eMhkcEfppzhAjvevQA_49eDertt9ejuJlCig5OW9h9qk7YHaU0CMs3JclBvVGgD1ebHoK6Zig_ctFZqwX9ZFQu_2YORYshAx_oy2E4kPE_5cqsB3g4NInlvVxdPE1hRcuuaIwFED05QSxuUsEjVFZE0A6ijjS7L7nhHbpLzEVF-nllo689yaGmN4Pv-lbdJW27QuoSZa73ctfklUO2FDA0xVIK8TsXPa3IJyNpWrXy_OdL0PSY6tCMJzIn51OKr8azlyh3xY8Q0oTiHesPQ-maER4A37kkc-DN_MlnsHOMkyaaI943leQlLa1IIHcR06Ws9bKPrqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو و بانو جورجینا رسماً ازدواج کردن.
رونالدو هم گردن گرفت بالاخره، دیگه وقتشه تو هم گردن بگیری
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69916" target="_blank">📅 23:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69915">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=sT6oflNvm4Uudt2r0qHmmwEGpMYdRwufC84_DZu7X3s6dYvtdJcz-jPhZ8Za7-r2yGe39vcZvJcZsONxnBHQqgNO1ucUorUBULB3N8xm7SoW62SVaFWXZ8DCNntn7GtIeEyvgTL9mowCI--VMDPkKv0Q15pSTj-vZYRSGg5l-YbF2RZYtuKPIkFsRaemEqDs5QXvBHKqP9QMOva_MeY7_aKZGK8_g9ccwPwQff6LJZOMb7bmeGOppfIuxqadvguafKDD3iWHvDUjL8veKfcN3X4L6b2uxK0763YYCZLtd-Qhj6ur8AfZURZNOT4zz7bNFS8Rfy465JZTM3LznbhSsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=sT6oflNvm4Uudt2r0qHmmwEGpMYdRwufC84_DZu7X3s6dYvtdJcz-jPhZ8Za7-r2yGe39vcZvJcZsONxnBHQqgNO1ucUorUBULB3N8xm7SoW62SVaFWXZ8DCNntn7GtIeEyvgTL9mowCI--VMDPkKv0Q15pSTj-vZYRSGg5l-YbF2RZYtuKPIkFsRaemEqDs5QXvBHKqP9QMOva_MeY7_aKZGK8_g9ccwPwQff6LJZOMb7bmeGOppfIuxqadvguafKDD3iWHvDUjL8veKfcN3X4L6b2uxK0763YYCZLtd-Qhj6ur8AfZURZNOT4zz7bNFS8Rfy465JZTM3LznbhSsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روحانی:
صدام پس از کویت به دنبال عربستان و امارات بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69915" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69914">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇺🇸
سنتکام اعلام کرد نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۵۵ کشتی تجاری را بازگرداندند، ۳ کشتی را غیرفعال کردند و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69914" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
