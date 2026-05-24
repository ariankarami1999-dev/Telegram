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
<img src="https://cdn4.telesco.pe/file/Uq2P7yqrbh__jOzt-ndwWLWjF9Zlu94hTsHp3oDaDl4nLIJA6_IyVweLcBQu8s78gN2T7qTa5q1YS5m_39V00bsyDVQO6Mcb5dFUCJZ3GGU5cY4APi7scDhCEdPZMVx3J-do8IXwhopqQg3wyalRPpOw9O5YD8kRrX_zHrfzCgpWAbEehI3GDwAXhYEi4VR1SXvfYLmxIJ1BHlZplc8CfQy-rF1Z4V3_XvHunjhjYy_7eWovMf_ok3Gurm1Qn0-NuwPvg_arfEpBWIz5mEpB4VKqvr720W9UlLgJrqTNhMkLaF-N7AB7bHtPl0SXy0RfkJ3_k04AvSuB3mVAny_-EQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 09:05:40</div>
<hr>

<div class="tg-post" id="msg-437612">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWVRzPREOzQyNPBnODDS9xBJH3Xhz5mZmZVLaCOfjD7op-C0fE6Bk68kDLZStliLg3jHphdw3iendZBOKDOVsy4xj2_J-J_H7aAI2NwD8xbPrBL6-AodTOTf9pNOTbfpBX2fOJaUSCSIVzpL2oUYzTHr2K-jN2v6juSZf9Ri9ZdyMBbRmXmB_pKN_4oWh2v6GwGI_H28ueCwjID6BZ0sQco4No6yiFm2NR3zrQGImvJsD-BtigZUgOn2fh8aMzEpKxuUSORppJYHi9dpAFB_wUuu6BQT7KKr00wW3yXV1pneSQ_K9ajhBUKvKkwj3NgG_LFKma0dWFCZ5OB820TK7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام مشاور رهبر انقلاب به‌مناسبت سالروز آزادسازی خرمشهر و تناسب این اتفاق بزرگ با رخدادهای اخیر ایران و جهان
@Farsna</div>
<div class="tg-footer">👁️ 487 · <a href="https://t.me/farsna/437612" target="_blank">📅 09:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437611">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIZGMvnF4jQV1xoDszGNntuFMUJQSlhpckJ7_vltCf03BUIEjUqbl0qGkrcKt5R-z-WjKZUjryGzwQbR79hxYiOcbyb_gkUkQQ0jcFy-hCj0w6DhQofmP2i_v_4yiejdXNcbAYrXmayIy3vZnulJQija8FY4KpSOjysbpWIrylcxLsK7HWvy-KMukqAb10bOMoAz_A-_JYaIuMO2lEuFxeeZyRro_ntsd2Clf0ELWkVNsWJzoZOShAT7YqR6Z_6ObE_7PySZA-HvJ1ksjVtCqNvrBd0JjY6iodXKfEVZUFfyDbaH57s9uYo-nAZ5b2OO5ObmO25o21jF8FPgzZ_R-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فرمانده کل سپاه به‌مناسبت سوم خرداد
🔹
سوم خرداد، روز ملی مقاومت، ایثار و پیروزی، یادآور حماسه ماندگار آزادسازی خرمشهر پس از ۵۷۸ روز اشغال است؛ روزی که فرزندان غیور و غیرتمند این مرزوبوم با ندای «ما می‌توانیم» خرمشهر را از لوث وجود پلید ارتش بعثی صدام پاکسازی و کلام امام کبیر انقلاب حضرت روح الله(ره) مبنی بر اینکه «خرمشهر را خدا آزاد کرد»، طنین افکن و اراده الهی، وحدت و اقتدار ملی برابر استکبار جهانی در یک رخداد شگفت انگیز به منصه ظهور رسید.
🔹
امروز نیز ملت مبعوث شده ایران با گذشت ۴۴ سال از حماسه تاریخی آزادسازی خرمشهر و پیروزی در عملیات بیت المقدس، در سومین جنگ تحمیلی – که با حمله تروریستی دشمن صهیونی‑آمریکایی و شهادت مظلومانه قائد عظیم‌الشأن انقلاب و جمعی از فرماندهان نیروهای مسلح و دانش‌آموزان میناب رقم خورد – بار دیگر سربلند بیرون آمده است، و دشمن زبون پس از ۴۰ روز مقاومت  کوبنده و پاسخ قاطعانه و ویرانگر نیروهای مسلح، با ذلت درخواست آتش‌بس کرد و اینک نظاره‌گر خروش ایرانیان در خونخواهی رهبر شهید انقلاب اسلامی است.
🔹
فرماندهی کل سپاه پاسداران انقلاب اسلامی، ضمن گرامیداشت یاد امام راحل (ره)، امام شهید آیت‌الله خامنه‌ای (قدس سره)، و شهیدان گرانقدر دفاع مقدس و شهدای اقتدار ایران اسلامی و جنگ تحمیلی رمضان، و تبریک این روز خجسته به محضر مقام معظم رهبری و فرماندهی کل قوا حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای (مدظله‌العالی) و آحاد ملت شریف، قهرمان و انقلابی ایران، نکات راهبردی زیر را اعلام می‌دارد:
🔹
۱: جنگ تحمیلی سوم، جنگی ترکیبی بود اما پاسخ قاطع، کوبنده و درس آموز سپاه مقتدر مردمی و نیروهای مسلح به پشتوانه حضور حماسی مردم در صحنه، دشمن را در دسترسی به اهداف ناکام و آمال و آرزوهای او را بر باد داد و ترفندهای  اهریمنیش را خنثی کرد.
🔹
۲: عبرت خرمشهر، اتکا به قدرت درون و بازدارندگی فعال است. پیشرفت‌های هسته‌ای، موشکی، دفاعی و تهاجمی ایران، دشمنان انقلاب و میهن اسلامی را را به محاسبه مجدد واداشته است.
🔹
۳: بزرگترین سرمایه راهبردی کشور، حضور مصمم و پرشور مردم در همه صحنه‌ها است که سدی محکم و خلل ناپذیر در برابر نفوذ و توطئه دشمن است.
🔹
۴: نیروهای مسلح مقتدر کشور در بالاترین سطح آمادگی و بازدارندگی فعال در همه ابعاد "موشکی، هوایی، دریایی، زمینی، فضایی و سایبری" قرار دارند؛ بر این اساس بدیهی است هرگونه تعرض مجدد دشمن، پاسخی ویرانگر و جهنمی در ابعاد منطقه‌ای و فرامنطقه‌ای در پی خواهد داشت.
🔹
۵: فتح خرمشهر، الگویی ماندگار برای پیروزی در خرمشهرهای پیش رو و آزادی قدس شریف و نابودی رژیم پلید صهیونیستی توسط محور مقاومت و مجاهدان جهان اسلام است.
🔹
در پایان، با تجدید میثاق با آرمان‌های بلند امامین انقلاب و شهدای گرانقدر انقلاب اسلامی و دفاع مقدس اول، دوم و سوم  و اعلام بیعت مجدد و اطاعت از منویات و فرامین رهبر معظم انقلاب و فرماندهی کل قوا، تاکید می‌کنیم:
🔹
بی‌تردید ملت بزرگ و فهیم ایران در فضای مذاکره برای پایان جنگ، با حفظ و تعمیق وحدت و بصیرت، و رصد مواضع و رفتارهای دشمن حیله‌گر و عهد شکن نقشه‌های او را خنثی و نقش بر آب خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/farsna/437611" target="_blank">📅 08:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437610">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDVpIKqjLgUqEGBDDIgCLbXsmAZVPB0xghjJtUbcTD78N2sqaXcYO1BnGcbQBqkCM6B6atc3ejWRY8iMqRUDQwEJBDuqsSM-c29IjcuBhgMzlnC5xfiwJcv3m538jDW9Kn6vyIRTOkN9TXSEvgwsca1LME8zCm1UNOf85ZaWaBaj4pLffSyh_NdGUBmEx7SDV_r2hoIedA309Ln0qBScl-o0NhcQTZkyu7GLvXNAoSKurdiPpIAA27t4A_KKOdVZls_dcrV_dGCevzQBCEbT-6wEXvXZ0XblrZboX6T6HBQIf7PSXgjkptwxVrIVwebntpk0w5fPQokFeGwSfHW2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عامل ارسال اطلاعات مراکز تولید صنایع دفاعی به دشمن اعدام شد
🔹
مجتبی کیان فرزند محمدقلی، از عناصر همکار دشمن که در طول جنگ رمضان اقدام به ارسال اطلاعات مرتبط با واحدهای صنایع دفاعی کشور به دشمن می‌کرد، پس از تشکیل پرونده و رسیدگی قضایی در دادگستری استان البرز،  بامداد امروز اعدام شد.
🔹
نامبرده در طول جنگ رمضان پیام‌های متعددی را به شبکه‌های معاند وابسته به دشمن صهیونیستی‌آمریکایی ارسال می‌کرد که از جملۀ آن‌ها، مختصات و اطلاعات محل واحدهای تولید قطعات مرتبط با صنایع دفاعی کشور بود.
🔹
محکوم‌علیه در شرایط جنگی، در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده».
🔹
مجتبی کیان در اعترافات خود عنوان داشته: «پس از ارسال پیام به شبکه ماهواره‌ای، شماره‌ای را به من معرفی کردند تا اطلاعات را ارسال کنم و من نیز اطلاعات را از آن طریق ارسال کردم.»
🔹
بررسی فنی پیام‌های رد و بدل‌شده میان محکوم‌علیه و عناصر دشمن نشان می‌دهد ۳ روز پس از ارسال اطلاعات، محل مورد اشاره هدف حمله دشمن قرار گرفته و به‌صورت کامل تخریب شده است.
🔹
پس از ارتباط‌گیری مجتبی کیان با شبکه رسانه‌ای معاند، نامبرده بلافاصله شناسایی و دستگیر شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/farsna/437610" target="_blank">📅 08:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437609">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwILAKum3DyD7vRpkKmLWmNZOffkz8v0e4xxd1X606yZxUFmNB2zb3OqWbbXuKW4KbCUThPxQVX-qS5Cqi0A80BR9LLlRS5ocR7ohNgL2efIyc8HcOJ0mkSRUjwaDFBzu1f8ufgyP-dNfRBGmod11eegitT47v1niF__FjKLEMF-2tQBJwpNjwtTlvYsRF-Vd7lBSGKvao9bvf-tWX-PZFJKIFiwDYNWAy4uAF0ofd1DjKwTH4jbSoKh2st8tfd1ydYtiXXmdHATq5io0a23X9GxY4pN6aRuBmbhKYrSK3WAcS8Ro3pBXujBFCViR4MeofP_y53SH8DtLMHPeTHSpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: خرمشهر امروز ایران، خلیج‌فارس و تنگۀ هرمز است
🔹
ملت ما امروز هم‌چنان مردم رزم ندیده اما دلیر خرمشهرند که روزها در مقابل ارتش متجاوز ایستادند تا قدرت مردم ایران را به رخ جهانیان بکشند.
🔹
مقاومت، ایثار و دفع تجاوز، ریشه در فرهنگ این سرزمین دارد.
@Farsna</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/437609" target="_blank">📅 08:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437608">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nshl3T-vkhlCZyMbugCGc1UNS2GMgdpGYkNim-3U6rNADKKInhC79aqentLnI-WOllz4sBJ6EFIWguucqGqeIGmpS1CstPoOGKTdGWmcOP0VBWCePYjrQ0BMJCxxDOGEhomOLwTZM0w6uQdccHeRn_J-VxP8MgExBabUDb3vW55E7_8aTEu79NnpUU-xyCy2qX02e4mnhudaI79fy5232poZ8w-MoCTcQiy_AtVA1tigs6f3OeSYoRACsNfY7mF7TvKyKG19jH0rsWyvgY6vtQRBVb3WF4NlF3toPZWzKJXGLM-8GhHXLymDvIAcy4rst3PwmFGTHNnmb6kvV-gbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: با همان ایستادگی حماسۀ خرمشهر، دربرابر دشمنان پیروز می‌شویم
🔹
معاون اول رئیس‌جمهور: حماسۀ آزادی خرمشهر آموخت با مقاومت و اتکا به توان داخلی می‌توان از بحران‌ها عبور کرد.
🔹
امروز نیز در میدان دیپلماسی، دفاع و سازندگی، با همان ایستادگی مقتدرانه و تبعیت از فرامین رهبری دشمنان را به تسلیم در برابر ارادۀ ملت وادار کرده، تحریم‌ها را شکسته و بر دشمنان وحشی خود پیروز می‌شویم.
@Farsna</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/437608" target="_blank">📅 07:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437607">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-TH1GTrzRT1XmNHJcR5nGUJm5-CPC8KMhGnSWIZyz2F3E_Jl1UVAYH1N0Ol9UUGZqQy3VI_GkwTe-OWjy6LFXCgE4gdYaJ3nnB6gRSQwjfNq2CWGyPlYWhkcC_r61krHGp6M79OuPYFRFg09ARnlr5fnfrKNja5Oc5nnkLNoXphwerkf1ZWVkVcpj_9jiKnGon9_y8l98pdmajotMST5oNvTDXCYFPvJUqJvX9SZyj63cShMePTk745wAdgkQ755rqGcl00Qxq6qpxadLXhGyKvfFl0qlMdM5H1cguqBpxu2JXqBK37YmvELwpv3tfkqX_KO74YRrbjilXoiiSpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با دور زدن آمریکا سوژۀ اول جام‌جهانی شد
🔹
بعد از اعلام مهدی تاج برای انتقال کمپ تیم‌ملی ایران از آمریکا به مکزیک با موافقت فیفا، این خبر امروز در رسانه‌های معتبر جهان به سوژۀ اول جام‌جهانی و بمب خبری تبدیل شد.
🔸
خبرگزاری AP این اقدام ایران را دور زدن مشکلات عدم صدور آمریکا توصیف کرد و نوشت: ایران با انتقال کمپ خود به مکزیک مشکلات عدم صدور ویزا و تعلل دولت آمریکا ٢٠ روز به آغاز جام‌جهانی را خنثی کرد تا راهی مکزیک شود و تنها در بازی‌ها در آمریکا باشد.
🔸
نیویورک تایمز نوشت: ایران با موافقت فیفا کمپ خود را از آمریکا به مکزیک منتقل کرد تا با کمترین مشکل تمریناتش را انجام دهند و در آخرین روزها با دریافت ویزا در جام جهانی شرکت کند.
🔸
شبکۀ تی‌آر‌تی ترکیه این اقدام فدراسیون ایران را نوعی ترفند برای به حداقل رساندن کارشکنی آمریکا در زمینۀ عدم صدور ویزا توصیف کرد و نوشت: ایران با انتقال کمپ خود با مکزیک مشکلات عدم صدور ویزا و بلاتکلیفی را حل کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/437607" target="_blank">📅 07:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437606">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7LWloLk1wIOAFRlP0Qz69_10jSK9yJ-1_BSH5nBweJbo67Q7MbYv51xrkBqj8EH8S5wajjJWBOKYgftIkRzyQBq8kpsrmfqFfxilxFyLGV1QJjyLGCI1NfBNg2NruBszKvZ4VRXFgVnB5BoYcaMgDmy4y4niwjyL3AWEWX3KzhvxPrz5r0RguXXQpTuhvCR7HbtYtiLZjDzCOTrEEZznQYLnzP6iz7iAkqYSJqpXvv6tfGQvsRanrHO-b-01h38BAlaqlpg-6YUfrhzcEgUF9GAWImAhS1Tk8ui059VNhQBlG9HWbpO-qadm6zR-iUuJodUIJ3PgSV29YPUkpKnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژۀ تازۀ واشنگتن برای خلع سلاح لایه‌به‌لایۀ لبنان
🔹
لبنان این روزها در کانون یک بازی پیچیدۀ قدرت قرار دارد؛ بازی‌ای که آمریکا با سلاح تحریم آن را بازطراحی می‌کند. از افسران ارتش تا معاونان ارشد نبیه‌بری، همه در تیررس واشنگتن هستند.
🔹
اما هدف نهایی از این پروژۀ امنیتی-سیاسی تازۀ واشنگتن چیست؟
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/437606" target="_blank">📅 07:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437605">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df3wc9mAKBbvm10lWYtFogLpjtknDNAgzhcAcZXAqxeXx1zjh6s_l_w4N7OsYvnu5dChtIuT6ymotgqLYtjBbosXxUl3Kb0-67YJ7f2V-C90Iz6t9ZPXEFuOO6ktFzsWNE_TodR-Lmk9hoCDw-_pR3jGv5JToJo3Ajl00uSoSGPLoNz7atYs4M9cebAT37bIBhyl6Mk6Qr7jr_0xvFv0UgJgZG98zcUzX-eSRltbPgDxNicCdzTvAPi38QYQVgDIlTyGqRh8AtWDk5GlAjWQHNbysjRZfsEz5pUJUuk1qL7aczDJ7ft0mzaQZUH_h9UV7JLPyX-pPBA0z6B5phXTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر خارجه: ایران منطق صلح‌طلبی همراه با قدرت، دیپلماسی همراه با عزت، و دفاع قاطع از استقلال کشور را دنبال می‌کند
🔹
غریب‌آبادی: ‏۳ خرداد، سالروز آزادسازی خرمشهر، یادآور حقیقتی ماندگار در تاریخ ایران است؛ حقیقتی که با اصول بنیادین منشور ملل متحد نیز پیوند دارد: ملتی که قربانی تجاوز و اشغال شود، از حق ذاتی دفاع مشروع برای صیانت از سرزمین، استقلال و کرامت خود برخوردار است.
🔹
خرمشهر نماد پیروزی ارادۀ ملی بر تجاوزی بود که با محاسبات قدرت‌های حامی متجاوز آغاز شد، اما در برابر ایمان، ایستادگی و خوداتکایی ملت بزرگ ایران شکست خورد.
🔹
امروز نیز ایران همان منطق را دنبال می‌کند: صلح‌طلبی همراه با قدرت، دیپلماسی همراه با عزت، و دفاع قاطع از تمامیت ارضی، استقلال و حقوق مردم و کشور عزیزمان ایران.
@Farsna</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/437605" target="_blank">📅 06:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437604">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdRHQinkD8hsarjqdpH0HcoBN7_suSAVXv9Lc2nSXVMDJDikXw80BfO_yuL8NA8SopFWaCbSYwnomsPCA1o0csCH22hErQ_-uF_vM-HCupPxlUIgyLEVJb4mdV9dUmjC3CtUdo4792ivqjAJhrFtDbVd90YrM1zTFPgSy9Sc9HcsLAUolSApp9-i_phSgVfy8FlzLDJellzwlLqxtn0ptMKgFiOHafZdqSlA4Lz7fjDUYeDZP8Sf1d1TfJalEHMJBzBGQ0JalQWEQHBFvDRhRIu_2725Z7sI7jWpOHc1Kw3JehE4hVtHouh1ytQMBY0sFE3EF3kw-xng9174-TaR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم بیمۀ کارفرمایان، و محل حقوق بازنشستگان تغییر می‌کند؟
🔹
وزارت اقتصاد و وزارت کار به دنبال تصویب لایحه‌ای در دولت با عنوان «لایحۀ ایجاد نظام جدید تامین‌اجتماعی» هستند که بر اساس آن حق بیمۀ سهم کارفرما از ۲۳ درصد به ۷ درصد کاهش می‌یابد.
🔹
طبق این لایحه سهم حق بیمۀ‌پرداختی کارفرما و بیمه شده برابر و در مجموع ۱۴ درصد خواهد بود و ۱۶ درصد مابقی از محل درآمدهای مالیاتی تامین خواهد شد.
🔹
همچنین کلیۀ منابع حاصل در خزانه‌داری کل کشور جمع شده و حقوق بازنشستگان از خزانه‌داری پرداخت خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/437604" target="_blank">📅 06:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437603">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx5kzuOZ0uH86ONTkwgD7ynyz29boOHOV0J2NCVOAUOzziWX0U8y7f25cPsdiW_RpYvUHdtWaK4dVtsmuenJnCmPb-Bsmz2pt8svULpIqq2sAgWuZ4I-l7mbCoZ9JU0v3XwSys0cHPi65-yTuIOfIAz2KxFDJpd2XALTSVRNOSe9kcUqFaaaQPKx2Pra1rAD2bOZOnabGDWZPtxnKAc3KCC1cFNNPFmyJZ7BskOK8bVzcKWSfSbTASRrH1LTDtBOz9q7o3I8SVwHrCubZUEs-FO1JUG9vL1xdD2q9ocD2S0wor6J1vYUBRNQvqi2Gimx53zl3r7OD4wMTKQMGsAKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رسانه‌های آمریکایی: فرد مهاجم کشته شده است
🔹
رسانه‌های آمریکایی به نقل از سرویس مخفی آمریکا، از مرگ فرد تیرانداز در اطراف کاخ سفید، براثر جراحات وارده خبر دادند.
🔹
هویت این فرد هنوز نامعلوم است.   @Farsna</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/437603" target="_blank">📅 06:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437599">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a0ddcf87.mp4?token=TkOlxl9LcQG4KGCXVRi0yPBMPsKepLZkuB7p6pNNli7cRI5Sd12rZ3DSYOnSGLbAHu_xCaBiRexDYuYbSqLY4_trt6kGqzMqJr8dw_5DgHYH7uIa1M1EhOvXbn5yDV-KzeoDTBUsIgHC66GSO14mgv0RZWKGnKsKWhi3fvp-ejjsThqqlEgZ5jZcBChLytL_ZXYd9l0SbbcFFkZqcl-7JbHMR9YXP_Mg65Rkq35oOMHpGF3nS52h3vS8n2XVDiARXsCyeJslB911mQOYjAJrgKCEhobUkUz9e-onWKBzrxCHLz3sYdZlm8L2vts23-GWDi1JI_ujUSrNTtUYuKTV_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a0ddcf87.mp4?token=TkOlxl9LcQG4KGCXVRi0yPBMPsKepLZkuB7p6pNNli7cRI5Sd12rZ3DSYOnSGLbAHu_xCaBiRexDYuYbSqLY4_trt6kGqzMqJr8dw_5DgHYH7uIa1M1EhOvXbn5yDV-KzeoDTBUsIgHC66GSO14mgv0RZWKGnKsKWhi3fvp-ejjsThqqlEgZ5jZcBChLytL_ZXYd9l0SbbcFFkZqcl-7JbHMR9YXP_Mg65Rkq35oOMHpGF3nS52h3vS8n2XVDiARXsCyeJslB911mQOYjAJrgKCEhobUkUz9e-onWKBzrxCHLz3sYdZlm8L2vts23-GWDi1JI_ujUSrNTtUYuKTV_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روسیه با موشک‌های اورشنیک انتقام کشتار دانشجویان را گرفت
🔹
ارتش روسیه بامداد امروز یکشنبه، حمله‌ای گسترده با موشک و پهپاد به کی‌یف پایتخت اوکراین و مناطق اطراف آن انجام داد.
🔹
نیروی هوایی اوکراین نیز اعلام کرد که حمله ترکیبی شامل موشک‌های بالستیک و پهپاد بوده و برخی از پرتابه‌ها توسط پدافند هوایی رهگیری شده‌اند. منابع اوکراینی از استفاده روسیه از موشک «اورشنیک» (موشک بالستیک میان‌برد جدید) در این عملیات خبر داده‌اند.
🔹
این حمله گسترده موشکی و پهپادی پس از آن انجام می‌شود که وزارت شرایط اضطراری روسیه شامگاه شنبه اعلام کرد شمار قربانیان حمله اوکراین به خوابگاه دانشجویی شهر استاروبیلسک در اقلیم خودمختار لوهانسک به ۲۱ کشته افزایش یافته است.
🔹
ولادیمیر پوتین رئیس‌جمهور روسیه نیز روز جمعه اعلام کرده بود که به وزارت دفاع این کشور دستور داده است تا پاسخ این حمله را بدهد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/farsna/437599" target="_blank">📅 06:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437594">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKLPSoZGt6Xxvlpb-pJ9oa-v2Fp_oYSMehdwCodeA8aDgPTG0ueNkBmcgVmoevJsDil_bWSNA6tlZiwUCCIkT0oY3BUBdc3sJjqgB9rxMLlUEZW6j7Y-0xPrc0XdwYIKHk5_h2vJ2HmSsVK5SytPRnZfU0vtrHhPU1drxUC6s45GooKCuoij_428X-hLQrk5uLHBhlCSJ35iN13bM2AOdpdkxfAYFmzQ2jNWF76fVGEsNPvmq26Ayq7o06zstflgfhVSScat0yEiqneo1iDlayjA9wyBP4B0ennPaUv8QMrMufof2m46qkERJzFphU6Z89ZMZQhLXACJi30aioPn2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرضۀ جدید شاهین در میان معوقات ۴ ساله
🔹
سایپا در حالی دور جدید عرضۀ شاهین را آغاز می‌کند که هزاران متقاضی این خودرو، از چهار سال پیش تاکنون در صف خرید هستند.
🔹
معاون فروش سایپا دی‌ماه سال گذشته گفته بود، از مجموع ۴۴۰ هزار دستگاه شاهین تعهدشده طی سال‌های ۱۴۰۱ و ۱۴۰۲، ۴۲ هزار دستگاه باقی مانده که ۱۲ هزار آن «معوق» است و تمامی این معوقات تا پایان شهریور ۱۴۰۵ تحویل می‌شود.
🔹
با این وجود، حتی در صورت تحقق کامل این وعده و تحویل خودروهای معوق، همچنان ۳۰ هزار دستگاه شاهین از تعهدات باقی می‌ماند که متقاضیان آن همچنان در صف انتظار تحویل قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/437594" target="_blank">📅 05:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437593">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2hxH46AiOyAN2HwmJ0deMT5C6TJZO1RFehE0dz4ilh-svnZAAnH5QdupNk19mVBl24hpkxd3ucsuNhxVvdE6tsFaCppKD-J4y1jQViaGukoMqSrNZ4-DXmhYjkQ9ZRc-LxiAZeGw-IOvYHBkCFF_-2Q2jaBDzJlY7YXeo-vRkyADgI7XtYnkL7EyXsRRW9FMeHC0f3SZnCSiPqOvR4FhG4iCED1mPzGbkRBJFXcWEoX6q_s1x8miNYeg4aFgsV5E_JC6Fm_CdgJrTI-4tiR3WlH-gTPn-_O_HhxteASx8yDotccuMVWEKaN7jO2xpzt2lXlBgTVhTlsQZv1-oy2Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاس اولی‌ها تا ۱۰ تیر برای پیش‌ثبت‌نام فرصت دارند
🔹
آموزش‌وپرورش تهران: پیش‌ثبت‌نام دانش‌آموزان ورودی پایۀ اول ابتدایی برای سال تحصیلی جدید آغاز شده و تا ۱۰ تیرماه ادامه خواهد داشت.
🔹
پیش ثبت‌نام از سامانۀ
my.medu.ir
انجام می‌شود.
🔸
اما شروط و مدارک لازم برای پیش‌ ثبت‌نام کلاس اولی‌ها چیست؟
اینجا بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/437593" target="_blank">📅 04:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437592">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">عضو یک حزب اصلاح‌طلب پس‌از استعفا: تحلیل‌های ما درباره آینده جمهوری اسلامی غلط بود
🔹
علیرضا اسکندری‌نژاد، دبیر استان تهران حزب اصلاح طلب «اراده ملت ایران»، با انتشار نامه‌ای خطاب به احمد حکیمی‌پور، دبیرکل این حزب، از تمامی مسئولیت‌های حزبی و عضویت خود در حزب اتحاد ملت استعفا کرد.
🔹
اسکندری‌نژاد در این نامه با اشاره به تحولات سیاسی و امنیتی ماه‌های اخیر، اعلام کرد که دیدگاه‌هایش نسبت به جریان اصلاح‌طلبی تغییر کرده و دیگر خود را در چارچوب این جریان تعریف نمی‌کند.
🔹
وی در بخش دیگری از این نامه تاکید کرده که برخی تحلیل‌ها و پیش‌بینی‌های رایج در میان فعالان اصلاح‌طلب درباره آینده سیاسی و امنیتی کشور، در جریان جنگ اخیر محقق نشده است.
🔹
این فعال سیاسی ادامه داده که برخلاف تصورات پیشین، ساختار سیاسی و نظامی جمهوری اسلامی در مواجهه با بحران‌ها دچار فروپاشی نشده و نهادهای نظامی و حاکمیتی عملکردی فراتر از انتظار داشته‌اند.
🔹
این عضو مستعفی حزب اراده ملت همچنین با انتقاد از رویکرد بخشی از اصلاح‌طلبان نسبت به مذاکره با آمریکا، تأکید کرد که تجربه سال‌های گذشته نشان داده این مذاکرات نتوانسته به نتایج مورد انتظار منجر شود.
🔹
اسکندری‌نژاد در بخش دیگری از نامه خود، اصلاح‌طلبی را جریانی توصیف کرد که «ارتباط طبیعی و ارگانیک خود با جامعه را از دست داده» و در صورت ادامه این روند، به‌صورت طبیعی از صحنه سیاسی و اجتماعی حذف خواهد شد.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/437592" target="_blank">📅 04:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437591">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فاکس نیوز: نیروهای امنیتی فرد تیرانداز را زمین‌گیر کرده‌اند
🔹
شبکۀ فاکس‌نیوز گزارش داد نیروهای امنیتی فرد تیرانداز در اطراف کاخ سفید را از زمین‌گیر و اوضاع را تحت کنترل درآورده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/437591" target="_blank">📅 04:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437590">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b584ab479.mp4?token=RD6dP-vhlTdwH9NGV_b2M7VP2XtW39aUGgoqXKh1_v05D_vll7wcihTI7uUMPNP2kBcnr3R2XByNWXnu5m5GBwtwn5DBLHckgRC02V3_na1PsgnSSkywEM8zSzkXMxiEP9axrgYoZYOcvMnx2tu4WvLQ7ZcV11X5doxGd3jbE6n2wzSHK7mY-R24JDfkg0g0A5Y7pkGD_epenOBVTQWgYszvYqTCUUnqSf1Ew5rUVwArg0ZS4R8J10JIHUgY_1uodcldN3YoJGuiH6ugrIgA-yN99lMnXancGzuuJ0lQBNUciC_7508m1mqb1LB0omehRPxiz9Q0EsNemlo_75AfMVn0r8W5lNAi3D8Fp-lmWDUx3n5z90bklkH8pT-F47ZUdibRCKTrHgeyNpBYikZdSJqYbCPtOEVsU4UZdlOVdHS4xaUAQeiBVV5odZ705I5J3tXpxcA86xx9DFzThHFIlKlGcGwM-bB_gIhYnvniZKl4MPUJPSMgBnLRaTjnE4TqiWz3YikJQlirfC0Pi1EQXnYLvfIZWO5ATnIJG2aSH9AIZVsrL7996HbR2bgp3EULySknlgxzaF61C5NEn03UXRsPn1T5USEo487YgDTPLAzSV6mvvktLn2c0WedO_BROE8PDDMkPWWJAS5DzsYMaW4BJWqXfQeu3IaH0rjWH5lY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b584ab479.mp4?token=RD6dP-vhlTdwH9NGV_b2M7VP2XtW39aUGgoqXKh1_v05D_vll7wcihTI7uUMPNP2kBcnr3R2XByNWXnu5m5GBwtwn5DBLHckgRC02V3_na1PsgnSSkywEM8zSzkXMxiEP9axrgYoZYOcvMnx2tu4WvLQ7ZcV11X5doxGd3jbE6n2wzSHK7mY-R24JDfkg0g0A5Y7pkGD_epenOBVTQWgYszvYqTCUUnqSf1Ew5rUVwArg0ZS4R8J10JIHUgY_1uodcldN3YoJGuiH6ugrIgA-yN99lMnXancGzuuJ0lQBNUciC_7508m1mqb1LB0omehRPxiz9Q0EsNemlo_75AfMVn0r8W5lNAi3D8Fp-lmWDUx3n5z90bklkH8pT-F47ZUdibRCKTrHgeyNpBYikZdSJqYbCPtOEVsU4UZdlOVdHS4xaUAQeiBVV5odZ705I5J3tXpxcA86xx9DFzThHFIlKlGcGwM-bB_gIhYnvniZKl4MPUJPSMgBnLRaTjnE4TqiWz3YikJQlirfC0Pi1EQXnYLvfIZWO5ATnIJG2aSH9AIZVsrL7996HbR2bgp3EULySknlgxzaF61C5NEn03UXRsPn1T5USEo487YgDTPLAzSV6mvvktLn2c0WedO_BROE8PDDMkPWWJAS5DzsYMaW4BJWqXfQeu3IaH0rjWH5lY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲ عملیات حزب‌الله در روز گذشته
🔹
مقاومت اسلامی لبنان از ۱۲ عملیات موشکی و پهپادی در روز گذشته علیه مواضع ارتش اشغالگر در جنوب لبنان و شمال فلسطین اشغالی خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/437590" target="_blank">📅 03:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437589">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYmVdzaV2qQ78pevTQGFCEvUC-5ibUhzsWqAEeUI-Cww90oUz-4kyuaPJZvQyYNYVc2_ATqbxoN-nO3Fr4yk4dN5X-fpC1lQP2dgyKcl5iby8spC1OQvklemGPJSgqxWLglDrPtAxZQmUW6v-l4LXPrZzhVhiao_3PAtqPL7mUW_kfFIffgNkYvUzArf4CB3ZG04XTGPNytWWs0LD917SlCG4t-85tX_NX7DLLVTKrdvOzS34WREAg32bIw6FtnQ4xhdZJNpdwbCD0QWJW2AQPfv-6ixMkaoqZRNm46k9tLR91zrfr8CpDzDoVEx50_8GyLRs6C5knCTjkkIjHaNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ سد جدید در ایران افتتاح می‌شود
🔹
جانباز، معاون وزیر نیرو: تا پایان سال ۱۴۰۵، ۱۴ سد جدید در کشور به بهره‌برداری می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/437589" target="_blank">📅 03:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437588">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32243b2ce7.mp4?token=vsPctlBKFpV1rhyXOwVwK_5msiyFNBzdHQ7PyU-dABpGGkyu_F0ym2SGsGzTsgVzsPMeFocEimFkHcjgk0mulQKEmR8PQmy9JqpU-myJZO1IXIZtoAaiPrGJmLmjIrNgihZCyXnZCcJf0x5Vnn0_su_YZ0QIDa4W2hZOp0b-6cVn7ulANE2lg5o43x5sQ0PV0VycZCm9AcccBo3kVk_J7swuh-WZlylnkVSCmACqrkovYx4nDeTyw0hO0GeNs1PxMDoLEKxloi4n2w3bJs9qHjD0lwRVqxI9L2CHue5U0y1Q3bRRYW5gH6EGW5T_pJxv3JNeuuQzi-8ZP4WAES0Grg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32243b2ce7.mp4?token=vsPctlBKFpV1rhyXOwVwK_5msiyFNBzdHQ7PyU-dABpGGkyu_F0ym2SGsGzTsgVzsPMeFocEimFkHcjgk0mulQKEmR8PQmy9JqpU-myJZO1IXIZtoAaiPrGJmLmjIrNgihZCyXnZCcJf0x5Vnn0_su_YZ0QIDa4W2hZOp0b-6cVn7ulANE2lg5o43x5sQ0PV0VycZCm9AcccBo3kVk_J7swuh-WZlylnkVSCmACqrkovYx4nDeTyw0hO0GeNs1PxMDoLEKxloi4n2w3bJs9qHjD0lwRVqxI9L2CHue5U0y1Q3bRRYW5gH6EGW5T_pJxv3JNeuuQzi-8ZP4WAES0Grg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه تیراندازی در نزدیکی کاخ سفید
🔹
سرویس مخفی کاخ سفید به حالت آماده باش در آمده و به خبرنگاران دستور داده فوراً به داخل اتاق نشست خبری بدوند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/437588" target="_blank">📅 03:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437587">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
نماز شهید رئیسی در کرملین چگونه مشهور شد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/437587" target="_blank">📅 02:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437582">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFvgB4mAnQRGrj3qoyczfaj9qDwE9DZLq0QL-yia-DGX313_L65tIcZq-m5_8m2Dl8VHaaph5B3UN2U3jsSWV2Z5N_8CbYeYmk1krxWGPNdRKZb_2dLcrpHR3YTB8kgjzTJE9XFCvquX1zYrad_0414aLSvdG9SyJ8JBiIC-frUPwCaJWi-siVZpPbfJTgJ7aG69DwzP7axyrJqBv0Z3Kh4eTGiEihd1ionq-Y-dsFABRo11jUyqmNB469WbsMfyIPIYzg8uJ2eBricgBwxYS7XSZ2kLhpRQPik3B95HM_Wse87NtBqmCH_h-yVdOdSCAnizqBiqJL00s40ktp-vvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDECXCS20wbyvK0ei8Y1LlF5tAgj5OAqrjUAraNkjdzrasq2Qe10b4NC5PvoE7r7jL7AvvcWIXj_Uwx5Ksns1W8-0l4XJIK5HzvLCGGl6SSxFJnWSYw34pHeMj3RDoa6h51F5Xtf163rTcGmkz5UsJ0YjIb_1AOLtLmTGvGHmpGQpHaFROp-IhcNQgQfepL1gLzzv2sI9lVVpBJfzT4Xu8DGdH0nTP-5f5sMV8dyNQpNr7XpjrNHl2o4Vt5a6opqfq0TL3S4lkHAuxqvrVhJrT_FVVfp6F3bMFrGdaCiAlPeKxj1KIzyRQwXk5gAOKr9l-FfFGzNsCEXMwEb6ZTrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYb1IrizyrRAKQ5oXLmATfLh8qrXiK3nSMfe_CIbUS23ZxsevnMy5e4FtxkIzFMgnVqgfX7gXuRNJUPmxp8wWpEUWYDXxpEcjF4LcBOQMZ15MOeNoznWdo-Su0psBdvY1oAe7bZKhnrEz6Ij6PmR1FdHzfUOpIMVMKWqZleTdSHpfISHnTgkzIcBXqU4XS9bRmrPXl9Lk0L0cZ20RS8XNOdhm4Yw1zJUpRusxJXq4ZLEEIR3-3Ck7SXLl2sZcqoEU3SCaYIP4C3FFQOwwKdGjKEEA5h4wCeuDp37ki7DgXs5E9WSbY8Z8DB3OVxPdIg9c59rKtV17a9V-k_fOE1aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsyHjmvP5hqeZ1ndPtIyo0_Btgla1Fdj2OhyUSgrWRp3RxM2QgHO61E51DJZN3MdT0e5U5fXDnVNaeMF5wrjOqgaG6LW1cM8diiIgLmYX_H_qH2v_yZVtvrVZkDID1lxt8fpx29U8WmIyKX4gQNeeUWiW0WguatB99cPh7DGFK_YImzq9r5jn80D__T3bTgGGGl-x2U3qt0nhAD3EmBkbE2tj5NSdhg89sEAeDY32XfmsNLwdyBO0rKUUJwFLKlrn2G9OCDsQLTHezEucJd_-gCsPfAFbzCsoYrZZqN9-xJH5eZISDy4wMIkWjwKSk_HUO87xd8bJqj1FJLMmOv14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjsFhdfmU4hRRSwyojS2xV5HV_pqQiyRT-HH8ZhsaCslx8PDvJS5LSSC3Xj45QVjJSuMttzhLyvQweUMxGglTFqYki4JiJpcvtTbbuSMWnsVFPtLqN-FwQL9XgbOsI9BxKqi7pA8Em4ngiFoibeVnP69Pfq77nIXTmlHhGr8ghM3X_si0Mw91wLudUPTGar2vZjhn07yg9b46dboYOINDGYoUdsmJXGSVgpiERSQ_ONmZUJROgLh1p13zfQjv3ZwVe-0MmzIJYvrP3fLlfRVb23l-BUP-J34AHQWO86gbj70hWpEtXfs_VUY2FtA_Nsm8t2-JoQCcZQFEJ6HaofY7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی به‌جامانده از تجمع شنبه‌شب در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/437582" target="_blank">📅 02:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437581">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b76dc06698.mp4?token=tGCsetrS2bJByNVHxGyBWUIJmUzsCXXMROwgs4rq3thOeRfAy-ECOYWwu7fRkh02_cP0CrqNf0Ad4EYRn5ijI7cwtaZq4ZgYW9V8_41shwKGVn7mQFkUOUm68Fh1Z42OJ58cFjZhm3NedkG0c6xjRa3koxMFSc265L0AGnObb_KubrdBi4ZRxMKJEu5aa_ftck_CdKfjDEBd8jIHkJsmux8k696dbifmGg6CeJGtU3WCqUrMM35G-cmOZ-S4lI9j6Zk90LjbZItpH8JYeTz4aSoqbAw1MK4qzYYLZv_xv2kfXD7kJnKA9ypQ0OYVM_JbYJTUhGWKAcPtqeBq-shUGGDs8w4EqsuKvl_-1-_hfkcDA_GHXIEbIl52Xqkwrg2Wy3NHskSQ0_J5UPrkxeE62skOEl7SOqydjSw_oHNIa5dILKYZqhhL6OBlkc3-SgmS7poTxjPQl_Xdem3T0WeIIwvlCyETCvOCvyxcCyH7HrmmHWXmxKzNBrheshaXny3w5nF0gZg7s06g76Z8_BXYpugeVa9oRGkuZYE_l5OiHgsQwpS6diNKiaThKmi8LmyMaZ-7-IaKiVoG_zbkYZLV3iyrCrp2LRfCv9K01zfbGL0wVkiVHD72OPT6BqAg_XsdDcFnRAYo0iRPR0tOlaZ-G85lHZW_on8KhNMRtKyTD4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b76dc06698.mp4?token=tGCsetrS2bJByNVHxGyBWUIJmUzsCXXMROwgs4rq3thOeRfAy-ECOYWwu7fRkh02_cP0CrqNf0Ad4EYRn5ijI7cwtaZq4ZgYW9V8_41shwKGVn7mQFkUOUm68Fh1Z42OJ58cFjZhm3NedkG0c6xjRa3koxMFSc265L0AGnObb_KubrdBi4ZRxMKJEu5aa_ftck_CdKfjDEBd8jIHkJsmux8k696dbifmGg6CeJGtU3WCqUrMM35G-cmOZ-S4lI9j6Zk90LjbZItpH8JYeTz4aSoqbAw1MK4qzYYLZv_xv2kfXD7kJnKA9ypQ0OYVM_JbYJTUhGWKAcPtqeBq-shUGGDs8w4EqsuKvl_-1-_hfkcDA_GHXIEbIl52Xqkwrg2Wy3NHskSQ0_J5UPrkxeE62skOEl7SOqydjSw_oHNIa5dILKYZqhhL6OBlkc3-SgmS7poTxjPQl_Xdem3T0WeIIwvlCyETCvOCvyxcCyH7HrmmHWXmxKzNBrheshaXny3w5nF0gZg7s06g76Z8_BXYpugeVa9oRGkuZYE_l5OiHgsQwpS6diNKiaThKmi8LmyMaZ-7-IaKiVoG_zbkYZLV3iyrCrp2LRfCv9K01zfbGL0wVkiVHD72OPT6BqAg_XsdDcFnRAYo0iRPR0tOlaZ-G85lHZW_on8KhNMRtKyTD4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشتاد‌وچهارمین شب حماسه در سمنان
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/437581" target="_blank">📅 02:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437580">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0321df321e.mp4?token=ZE5VLlFP5V4ls4BzsIyY6JqkKLJ_FvrGMgqj97Em5wm81zQ8sVw58AmRCEGFSaHVoDFjaS3inVaUdQwIitkTJ41hi3-VBpBBQTsz35BVMBgxXaafX6aRjbohEmzDEtQ_6afZw6LeWbEt5rOv87gW0AFnKbKKxsEFuJ1b5wdz4B982XZgcfZHE6uQh8n46z6ojruO5ZLQDAMfWU1CClnPAqQ4zDTV8G0C-gJeWUrcZ2a-OGdlJbz9ltpc8kdaoI9SGIOnzrg8FII55aV4KXpA59sgOA4oyYuQB28vdluizTcx3K23916kQ7o5-xu4Mbh1zShnU-5VqigqApLb3cwu9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0321df321e.mp4?token=ZE5VLlFP5V4ls4BzsIyY6JqkKLJ_FvrGMgqj97Em5wm81zQ8sVw58AmRCEGFSaHVoDFjaS3inVaUdQwIitkTJ41hi3-VBpBBQTsz35BVMBgxXaafX6aRjbohEmzDEtQ_6afZw6LeWbEt5rOv87gW0AFnKbKKxsEFuJ1b5wdz4B982XZgcfZHE6uQh8n46z6ojruO5ZLQDAMfWU1CClnPAqQ4zDTV8G0C-gJeWUrcZ2a-OGdlJbz9ltpc8kdaoI9SGIOnzrg8FII55aV4KXpA59sgOA4oyYuQB28vdluizTcx3K23916kQ7o5-xu4Mbh1zShnU-5VqigqApLb3cwu9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه تیراندازی در نزدیکی کاخ سفید
🔹
سرویس مخفی کاخ سفید به حالت آماده باش در آمده و به خبرنگاران دستور داده فوراً به داخل اتاق نشست خبری بدوند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/437580" target="_blank">📅 02:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437579">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
تیراندازی در نزدیکی کاخ سفید
🔹
منابع غیر رسمی از تیراندازی در نزدیکی کاخ سفید و شلیک ۲۰ الی ۳۰ گلوله خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/437579" target="_blank">📅 01:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437573">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlFeX8CsHlJoZshHifWwocNMiteagsjIvn_J7za2eWeeNZ98MrqaI7iK99pLtOnYlzhWhll2kkBj1XdE508G3hTSWfjDPLbfWeJKocg6iohumKrEOB-IXoi1mfCu-Ap5kKcOZMFBCfS3nUyGX6arZbWsT2tCl1GPJh_4aXtlDLugbQD83A63p4DwL75lHHsOwxN6I_IrzjwT-J0ko1ro5ZcGHZbluMiH5NW9_ZyNONU_l4uT6yJiPowL66N176pCfRglBFZCVaADAd_hVxYt3166sp2nK8H7nGATzNsgfRUZ6hyx84dIcaKc8CN7Ar09lrXq_Lc6j0iC2UMkNONE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHuM6wKxk7xmWgHAmNpnKNCq1NJaI3ABq3IYL6UR3Pg8OEYRBBYWjwWzrTyW5KcPm2yDQ_42-PYbNpHeqgdR_UHcefvbD1OBw0vnoGJbx8I0EMno8fXwS40JBmrmRFaE_dMQ73ckIq2MFnAF0yRehExChhDXqtHUXkAL7v7mmWy8kwpUysjHNn4Msa_i9If00vG6M0uqcM4mbbhvNSwG79O_2Th6_SUOEUMzNWs8yAkwCX8O9tgvDC8q0P_5jkDO0PyYQCHIS_aWmwgGVKrm2Vh5s6AitrofuxJw6-laYA-xcZNoBWKC6WTBP1RFuy8PzqZ6fG2XplYYu9kZBqujzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ChbtV-3qca8TmOvPcGyj9l5cTGYHRPS3fYYVuvnQW4IjU_v3QR7m6j5DzF4H5zvlhXuyz_1I_2trySsjgX_gZ_c6rPfSK2vFwtxlTuGMwJd7pj2trbtUR_VPqdXiWxGpoNLf4yBZEdgdFLpPtpBX8IFx9vqr3j2ihpu1SkLs4dnYqFX1fwNsdK11h5OwNh5tGgTT3CLiQIL5cyMhgBYD7v5D77c6ZKGMa80o_h5Cwa8nuIZQdxJPCZDxg57EyPxrW_-gN0BMXP2gllrfKsyK6l9Mb0YTIjikJ458Bv8Bk_DmegMfBCyJgQK1P4xb-wPhllej01Ki4V5N_8f8wtHGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pz-a0WgtkNXmxZPX6uSyVnCvoTDtwovQIORM8jv9CtJp0QdeZeVjwX4qDbP1a4dUiwOoqjSB6TLS0xf6hk1yS7GBJQVoXstKEkFmgnEuKoYYTJlKih1th_DflQgYybfocB3X8mUz050slURiFvKoyx2YCLTeaoiWguG5j0wNe-XIlP86VPu2MYmDJndpQmRlgo5_6iHr-NdY1GDrffcHQPiFeK7PVRQBX21yAI2d1EyuEEzizVPYcTM-wimcHu9TeXzu665gxExfYA7UnOZoxf3X3m-QSAqmwiwQUeHtnPkddsn8A13256POGjsBOPYTRAuHjXEziuJ_6rywM51dBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TewJVvs9XVyYeziKCqooXZ5eBAiP0Az1cH0Bd2BhlcbpuB0sxiBPB8PNCSW33bS_PT6StWwpt3a71F4isnYfYkaLz2Vpb9TcCtEDidS4qsB6Xhtc---QIl77D5ouSqx7PJNntXCY-m355pClCmApeCulAYoruxxOVvtTtv5N5x-koCVEe8KvAHo5Ou-4Cryc510Tiy58l3jrqzRN4INiuPrCw49N7IzS94C2S8fpkglZ3eL12d3kGVqoee3X5bCty7IdEvoks0XyaKw90YVm8nbw8o0gMUkMFkJyBeYekfOVXXJ_L5ig_3I9iwaHQHNJOUTOYBIeflKgWKBD4nxT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzKrSz68Sh90Nb5IzHGx8ubOylDVmURbETkhUfv0rVwOSj83cNQef1NWVK9rX_R2H7EvYQWxYxvgjoHW3CPVYrhXyNtu1CY0tEhRHq2f5J2IPjbuMjL2CcrzjKSYulS5yqqYXggVEgQEOzAgJro1T5DMM1NUdm686Q2shsb2jiWNay2PcDbFVW3t6nrxbumyqYHcDluXQdHQEr3TUqddHmZmQEKFAt8UtwfVojQ8Ca27fENi15rQR7cZuBOJsRMIygPcmL8KBJ5nd98jkB-Wikma5uu5Z0AGOHz8C5JT5kIAD4VCD1okCiGrjSAKtOsnAHdxy7hgjUHL16scpb_z9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۳ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/437573" target="_blank">📅 01:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437563">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRg9wC5sqcrkqyX6ufbI1Oz1I7gM90Gmu_fWJvCnrSJ8WfvVouEg2QnzaI7_VM8xZLbQbWNtnDoKD1VDyfD2yGVAo50sKmpMYJQ-96voH-EPGnVAKl9CFXkcfOLpoNSxvYwHsxdl3YVEYZLfLQnkPvk1zRPs_SEIViD10BQT9m6bXlCpMF5LCOXwzbuhKwnFZpuwGxyZJMYD3JYeiSooJ89txMBKInZi6mG1Vbp-HBIFNkMfLk52nkRJcGKyhveXNOihbN_zHagdsN_npR_dJ-tqmNbkB6yzWlFV32f1FCel6uJA-rcIdqBIn6Yx_bU9UZVQPDD60LevPERmijAA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJiE96GI3ufyP9S5RmGe_Q3hTnhiiU75oAEIjuqbSozEvmIGd41Ify1S0etNE5_TYaMQCDRQKhmsLli-oZMHc5Bm5n-qBJbdi9BkaPW7tVwXECSEQtrPji5khQW-wOofIJuBgmnC6CqduYFOqzyphbMVFWTTsVcZu-7A9SoVgDj8iZNbHut5CxPFDUNevq0N8GVoBeeRDavV0si_HcZpEdugLhBW4uNBTpPXgXrZ3uxQQXAc3aNHBAXmfUeQJQ7Ban_4Y0-5AC361XhPS9WvRApX5PFZ4KF0_hGS_ZH9k319Crtdms_rOCS_sIaCf1hl5BtUew0PPiIuyHRRGyO0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SboIuJs9hwXwe3mX947ZrElQSbX9xAZYuvEkfa5Xylzwd2BGDfMpo_V0MEc0T9GWUBenIMSQQwCgAX8pEkL4T83y1Y-ZJaKMyfb3ti6qmGIP8TinzEllZa3mS9BsL8AZRPRhJdlaLdqPKyMVV1cqzbi-kMGfpZ4gRQawJwFvSeLWYe0Wi7MCj-rEY46MIgTKvjta0cfjOD9_cy_vO792T0jNhukJ-E9dZrQ8_J9YPCfvD-lqWPAQklxj530jh_xjHILcB3AhD_LO7tmrxCPrV0RdMhKDq5a5HaTCI5Gb-p7foXK-PpS6CxKT6Cy--E7dN0gJJdV8Z261bieh37AUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTwXEuWdH0DZLET_vtiTK1fgJl0a_5eY7QUeIduI44gULCPHUMUh6GQJPLz4bwbC7pRh8xghURwVjUyjBDUXw3xLYUjwHOCKs5AWJ3TQCglaEgPAiFRV2XAcBLiEuDptLO8bfjRzhc7JniWUBOkhnzN3t98WxQP2fx7GXGp3nlyj4jA-wKg-sWphSJkImMFnMnBIcj7gquEKf8PKtdDVK4LvguylQabwW-z3l95Fbyw-4Edcku19I_PQX_k_MpTqHy3LJHnxCZHLKq5EqW2Atf1oTOotoyB7bpUJO10PhBORUEvtdQ2kyj6uVEBDYIz_ZHYqGFwnotA9JEWJMK4-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IR4-QHM1ZoxNCv5goIlKJNLqprzKCAtex1xsVqOIZttLE1ufstjCWbhDWmb7PhhV7LsQ6IncO95wFhd3RuxGYXpCVeOTCpoTl0LO9UOAI_JUvQzSksCaMePjRUuworjzjQw-oK7TyTdJeir9qDgYHv_rL0QMqIbYIyEasuJlZASMdHAEZUeSSfZzPZ41Pir8xH4os5SKKTT1x-mFd8v6d55xYfzevVcGX2VJD_l77vP7D9hDodGbzmTsI4qoeTdj46n9UYaHqjcSflUbGGGbkffSnIuF9qJWwgWyxCdiyAHQTQ2sgcGnK4E1qojslRXQntvGhrcoQp6gZJJ_9S0BIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YsLZpPQSMBArKTgJ8h9_1Xyix0vEkiUsbjIdC3KqpVy74-DD_MMjRJLArRDHX9jgyE-bKRCjosJvlP-6Ksl6DLJyGvjakrvfPQIyzZuBEx6sLREfzGv7d7UgD1lz5HKEXjYGOXBzVn7px8ZC7oVbVHbQq3aAopXqmigq1s556qD0O2S8xP6uRxUG3-4jy1UYEEiAhMxuC-vZ_bTpBk78dCeY5XlgX6ca37yzXbDlzP0T5g7Ut2pG7zbxdok-AB-1_Pkhq-juuM-pQf2obgyr0OByGjn3TVNmOzxSTBf_MJFZ2l-eNwByouoNPOg9ftwdkyAID2Q6ZLTX3ZUFJMWcWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6FAYBjonHic9Pk_3mJSjSg462uOQzd-wSSDTMadXGNHu0zcJUv4IJEPBd9l-zcEPig1UVaTTfU1FyErZM0QQNaBvNtoTRjU8uiQUgs_sDuU6HB-sq67hwciGCxb7Rrm2ojPY00Wo83-XHBJHDGZBGlqvi4akWcet-dm7xteDTjXaZBU53ThuB0TkN2XLKOPpudkJSi6m9oKmJAh900Klkej7C2Fu0AR8cDf7sBnY0p-4BMndjcRjbNB9lvlUCU_U1O6InmFbd4QXk23l5I4iR9XlEfS0LqMpYPD6R9mzuAxSlBxpmLmzwFvGCDS1EHppebuW3QF-51ic73ZEwcN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-CrhVhaZxT27dVF9ho22_1BS_UcgCwFiUdbE-sWCHpbM2wX7xau_Nyj7TG7qwBuKz9HtxJEdMhmNfc4XOMfl6k22feGFbuMM7bLbyrUV-XqXv5QfJesaI_OUnlParqwo-69gihPHbSnu69CiWj5yRTJr_2mqJi3ZPlTjcypdnbxWF5jn4oTsK5J0gHIYOe5PnbgMVre2oJIGf1jloUqcaPLGcP6eOH3w8Cieg-HhQaZeVMDT71ccmukzqUEzj0oIs8QbPs-I-cVBk82_zVFIL8X_J5x5GXrrnX3l1yHpOxzOxliSn9gmvVKujaVdOx4pawo0kd7BBUigGRiuODVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLPm69oHQ9y-I8MGCGoyeXRlGCUSNMM9kkWGShDWT0YTzI_M1Xw8A89689rXsZzU6RBzSb_KJMG_fSgRmpUJM1DDG8kOIrvPssbTDiwtOc1ZwueARv3pwVmjQOUU_62RzLeqtr--XQFNmdoD60FGi0Ly60qqNKkaT0xeNdFAFfG7pI0POVyOm-MQroDppfbRuAJxEdstFJWKC2VkmBp1z4vH9wUTYiKfEpjrrR-r1dphilwmtlu1u-28MKLPe-Vrs6nacYDIpLiGNaET_Mnr4etWy8RPUiCMi0NvYF23-Rm-71z9Nren77b5vBC-3C57aiEt63B2cUQKcP6IBxWV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqIIU62O0h5uCN7135TvJBgXYwIcPm1MFLi8Pq1qJ9BoMZTpbbS8LLBP0ywG3H5RAlRXXOQGOTcQXABAtAc38F5zLCy1c35pISUUYjSJEZLsM2srDBpyUoc2c7_fx_YSL9IkQCOIa39o7BYaschXFDJIYEKVRro8qh8OLKjlOa6Jd7ncRX6yzVkDK0bdA1S2cZONPksefJSbsUB3Rong5uZozFsySQ7Fmg62I-3Jz5iKuxlR8-pifjCJ7xn5zC7t4071y9wQTt-MupFAWtNRlpc0XVFmBEmxdUmLrW_bEclkylH0RWP1xT_wZuxpmj_cmJ-J686t1OaAoaY2laneyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/437563" target="_blank">📅 01:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437562">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5nxQmgTwkdbGkVebfqBYIhb_O73BWT9pVX9gnvy8Mqo5nS_6eMMOrgcbm531i8KoFHEHBCpBzocBfGeShFKSKjgxO60KORqOD_YhHVskv577PJFUckaJo8qlLNMdSaCOf4Ws_g4F9JODe3nKaR9fJOxQYFG35RUzj4zCnoWE6qptlNduP5W1pInmRJvVPdzoIaRAtiONEMLNcOhJmhKrUnjRFSE4UGa9sFKGYh-w6dLzQtYsRGNPgXSrKXuYIrDvWlNLfweBEN9sqkWanESXro9hmwB_2UlDhAVnTT_VlzQFvmmxBLXm-SP0jZnIrG2VLSMovdN0M8wS61I4uvdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصادف خودرو ديپلماتيک جمهوری آذربایجان در محور مرند-جلفا؛ راننده فوت کرد
🔹
رئیس پلیس‌راه آذربایجان‌شرقی: در پی برخورد یک دستگاه خودروی سواری پلاک دیپلماتیک با کامیون میکسر حمل بتن در محور مرند-جلفا، رانندۀ خودروی ديپلماتيک که به‌تنهایی در خودرو حضور داشت بر اثر شدت جراحات وارده در صحنه جان باخت.
🔸
گفتنی است، برخی رسانه‌ها به اشتباه از فوت دیپلمات جمهوری آذربایجان در این حادثه خبر داده بودند، درحالی که فرد فوت شده رانندۀ کنسولگری این کشور بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/437562" target="_blank">📅 01:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437559">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: جزئیات و جنبه‌های نهایی توافق ایران به زودی اعلام خواهد شد
🔹
دونالد ترامپ مدعی شد که درباره بخش‌های عمده توافق با ایران مذاکره شده است.
🔹
او همچنین درخصوص تماس با نتانیاهو گفت که مکالمه با او به خوبی پیش رفت.
🔹
ترامپ با ادعای اینکه «تنگه هرمز طبق توافق…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/437559" target="_blank">📅 00:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437558">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MK0m_1606I-DnLD582VKRN0edzAxRjMYHdQKqyxQwkef2E6coAittKf7Uj8noov2qdJOEbvmtlTPQHFlR_sPBdh8dMahgeGcuWwyWCtekRzhp448kok6zstz4S1GfI0YbbGbNC_l2IgiS8XYdJmY7JwEFr76dwBFO8dJCqPnsed-w9FKEcFx3qZNsOM6lWlnfGDqmSTwDmS4iWauNbAWXLeGwg24fcKYMcyU8hX6FLhSoEEDVW8_KFmhOtOnBF2WjvGjFE8es2e0GP0U4LjR_3u77X-tpFPSwcAe5pDlv5_RfkgKx089AZA_gcwMrxMDrdY7M1yGVKS6jThL9pXIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری گاردین از برخورد متا با مخالفان سعودی
🔹
گزارش جدید گاردین نشان می‌دهد شماری از پلتفرم‌های بزرگ شبکه‌های اجتماعی از جمله اینستاگرام، فیس‌بوک و اسنپ‌چت، حساب‌های مرتبط با فعالان آزادی بیانِ مخالف سعودی را در داخل عربستان محدود یا مسدود کرده‌اند.
🔹
در واکنش به این موضوع، شرکت متا اعلام کرده که در برخی کشورها ناچار است محتوا یا حساب‌هایی را که طبق قوانین محلی غیرقانونی شناخته می‌شوند، محدود کند.
🔹
این ادعا درحالی مطرح می‌شود که این شرکت حاضر نشده تحت قوانین ایران حساب‌هایی که در کشور باعث خرابکاری شدند را محدود کند و در رفتارهایی متضاد اقدام به مسدودسازی حساب‌های دیگر، از جمله حساب‌های طرفدار فلسطین کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/437558" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437557">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ: جزئیات و جنبه‌های نهایی توافق ایران به زودی اعلام خواهد شد
🔹
دونالد ترامپ مدعی شد که درباره بخش‌های عمده توافق با ایران مذاکره شده است.
🔹
او همچنین درخصوص تماس با نتانیاهو گفت که مکالمه با او به خوبی پیش رفت.
🔹
ترامپ با ادعای اینکه «تنگه هرمز طبق توافق باز خواهد شد» افزود: جزئیات و جنبه‌های نهایی توافق ایران در حال حاضر مورد بحث است و به زودی اعلام خواهد شد.
🔹
ترامپ افزود: با رهبران و مقامات عربستان سعودی، امارات، قطر، پاکستان، ترکیه، مصر، اردن و بحرین در مورد ایران تماس خوبی داشتم.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/437557" target="_blank">📅 00:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437556">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KU8HjAnFDT0t5wWgNejG6t7c0vvdmux38r7noBYkizDaqDBkWip49i_6Tz7rJ_kbjUuBmobyUxwpgyU76GUOQSP2zIs8viNS_NTg0z5BsuRDaKKlNIBOflR5A14UxDnjfXRNH-5oLrHEzjGbMiy0tiZ-fZ-JRxi30dkK_1QF_I4iM7mSfjBJCLBhltE9D54b2tHXi5PCCN4mAts_Us6l4_iV-hPJAro7NgbmPlH4fWToWuNk0aECNkzAFul5aMsz4LPE9ueKXPm8YNOSzyfGwpK26dUcg72iByoU0aqJ29b6iIIXj66Ej871XRVw74NkVzkrpANW4M4eO1SFe3DcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ ماهی و صیادان
🔹
در آبگیری دوردست و سرسبز، ۳ ماهی زندگی می‌کردند: یکی بسیار عاقل و دوراندیش، دیگری نیمه‌عاقل (با‌هوش اما کمی تنبل)، و سومی نادان و بی‌تفاوت.
🔹
زندگی آن‌ها آرام بود تا اینکه روزی ۲ صیاد از کنار آبگیر عبور کردند و تصمیم گرفتند با تورهای خود بازگردند و ماهی‌ها را صید کنند.
🔹
ماهی عاقل به محض شنیدن سخن صیادان، وقت را تلف نکرد. او می‌دانست که نباید خطر را کوچک شمرد؛ پس بی‌سروصدا از راه‌آبِ باریکی که به رودخانه بزرگ وصل می‌شد، گریخت و خود را نجات داد.
🔹
ماهی نیمه‌عاقل پس از رفتن صیادان تازه به فکر فرورفت و با خود گفت: «افسوس که غفلت کردم و فرصت فرار از دست رفت؛ اما نباید ناامید شوم.» وقتی صیادان آمدند و راه‌آب را بستند، او خود را به مردن زد و روی آب شناور شد. صیادان به گمان اینکه او مرده است، از آب بیرونش انداختند و او در یک فرصت مناسب، خود را به داخل رودخانه پرتاب کرد.
🔹
ماهی نادان همچنان بی‌خیال ماند و دست روی دست گذاشت. با خود می‌گفت: «هنوز که اتفاقی نیفتاده است، تا پیشامد بعدی خدا بزرگ است!» او هیچ تدبیری نیندیشید، سرانجام در تور صیادان گرفتار شد و جان خود را از دست داد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/437556" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c853019a85.mp4?token=c_cqdA8OdG4u1Apdq6NVJ808SJ5i5mR4DD3I5Ijfo1qyrm541DxY3qQdIT457z9GeADu7i4mexlKlP9b0y6fkniZRPaMWfpGzGGCvnQmJ-EdmmqCTG0wR1Uik2ronz3eTFyd3mSaJV-lbBALQoJjuzzQhwvAcC_v_HSHG-vSaNz1S_ksq3T7KmhxbD2luX3eoyc6foiMYpbJQI9tmWK0P4Jh9cbwWecfMG9lmZersY-FO9Upoqk9peIGBDQDKxc4aR3S_ngGQyjjEWehZHGRDtTO2hiTYlmPq3y6ZYaH4C6WBg5jwqmUk-xnHvzEvTKTS2eLsvzDMTZ-72IhU5A1IWbS-pPE9mbFoPSwwKqc-stSgRBTE0w9Abm0ikv0LOJ-oMz8qgHSE56jW5TDatU_cinEf459Von-9A1CjH1eV4i77i0RHJrYBit9htEwcCALc8406KL5nmVopc7B_6zgpaG4n8yDACNjGbYSroHCBJZmiisLP0otI3yEn_cCoztmqUUjHqRVdjCLA_3hfrCVy-qAKG9bTXJLrx3DXnVT-Cc58Ffr1H26W_QDsyNR4z_bDY92cp_b4eX4CAcPYALUV1syvlgFvVFYQNQQ5N31PHiHA_yNgrE6S6JjNgxjKYtyxGw12aZ6Qr5wF23VCP1hYPsVSANoeiG4FTWsl6Vg2b4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c853019a85.mp4?token=c_cqdA8OdG4u1Apdq6NVJ808SJ5i5mR4DD3I5Ijfo1qyrm541DxY3qQdIT457z9GeADu7i4mexlKlP9b0y6fkniZRPaMWfpGzGGCvnQmJ-EdmmqCTG0wR1Uik2ronz3eTFyd3mSaJV-lbBALQoJjuzzQhwvAcC_v_HSHG-vSaNz1S_ksq3T7KmhxbD2luX3eoyc6foiMYpbJQI9tmWK0P4Jh9cbwWecfMG9lmZersY-FO9Upoqk9peIGBDQDKxc4aR3S_ngGQyjjEWehZHGRDtTO2hiTYlmPq3y6ZYaH4C6WBg5jwqmUk-xnHvzEvTKTS2eLsvzDMTZ-72IhU5A1IWbS-pPE9mbFoPSwwKqc-stSgRBTE0w9Abm0ikv0LOJ-oMz8qgHSE56jW5TDatU_cinEf459Von-9A1CjH1eV4i77i0RHJrYBit9htEwcCALc8406KL5nmVopc7B_6zgpaG4n8yDACNjGbYSroHCBJZmiisLP0otI3yEn_cCoztmqUUjHqRVdjCLA_3hfrCVy-qAKG9bTXJLrx3DXnVT-Cc58Ffr1H26W_QDsyNR4z_bDY92cp_b4eX4CAcPYALUV1syvlgFvVFYQNQQ5N31PHiHA_yNgrE6S6JjNgxjKYtyxGw12aZ6Qr5wF23VCP1hYPsVSANoeiG4FTWsl6Vg2b4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد یاسوجی‌ها: این آخرین قماره، جنگ ادامه داره
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/437555" target="_blank">📅 23:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69febc6574.mp4?token=H3eVeHY_LOOXHxaNLfVzTqhi5xL0Jfya4FsTu_ak6SIJx1xRmPVIokKWN0xHwpTFllkMW2FnZxJl7Hkh8l59oRoXgAxNU3M_qOWnk6jOTtP931p_nZNgIIDCTqH8M0oZcpJots8j7iqsa86zHRMiMwSQ_dYLvNUlNvrY8SKU9elvMHBYhTKZtVbb3lhbIP5s7uEPvVSfv7QnsX5L__hp4LTUAD2QQ2LE-0tNeOCuIub1b8As-M-y0974ecpYXsd52uVLBxE7Maf--0FTCE8GsMnI7Tw-2401a7T9GKxHMHpGyqr9TFjFBqqzYcfEHrzBUHgAWTK4PXYRdu6n2aU0UDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69febc6574.mp4?token=H3eVeHY_LOOXHxaNLfVzTqhi5xL0Jfya4FsTu_ak6SIJx1xRmPVIokKWN0xHwpTFllkMW2FnZxJl7Hkh8l59oRoXgAxNU3M_qOWnk6jOTtP931p_nZNgIIDCTqH8M0oZcpJots8j7iqsa86zHRMiMwSQ_dYLvNUlNvrY8SKU9elvMHBYhTKZtVbb3lhbIP5s7uEPvVSfv7QnsX5L__hp4LTUAD2QQ2LE-0tNeOCuIub1b8As-M-y0974ecpYXsd52uVLBxE7Maf--0FTCE8GsMnI7Tw-2401a7T9GKxHMHpGyqr9TFjFBqqzYcfEHrzBUHgAWTK4PXYRdu6n2aU0UDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
«انّ معی ربّی» فرمایش امام است
🔸
در دست تک‌تک ما شمشیر انتقام است
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/437554" target="_blank">📅 23:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5327365d67.mp4?token=qVzQWD7taXtHBB0GiYJR4GXoIpuSvxB7vc9mYuQYynAK1tx0w4Ar-5rzEvRK_a9-mORWN-ZxVaCPhvC-fckmSpQ90tuouYZNPbwqRX9PtDJg_PKCwT93L87B9HlWTaTyGDDmFqY9-HGC4fBZAatLbaxt1kimkn2OBhlmpYg6K9j7OYrhYf00VWLe-pN42rrP_M6OZLPIVsBCXRUrCjEIptPohzfTnlPdsGZppt-r1Q-PlsJP2uXiiplsP9kOsnAlOeXAb11zdRNTOQzWqt7HrAE668JxrFzUvGKhcQ84nIiVrLKRrkCOiWsRo6k-ruXF5GwFQIrf5yTzczEBEIKFcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5327365d67.mp4?token=qVzQWD7taXtHBB0GiYJR4GXoIpuSvxB7vc9mYuQYynAK1tx0w4Ar-5rzEvRK_a9-mORWN-ZxVaCPhvC-fckmSpQ90tuouYZNPbwqRX9PtDJg_PKCwT93L87B9HlWTaTyGDDmFqY9-HGC4fBZAatLbaxt1kimkn2OBhlmpYg6K9j7OYrhYf00VWLe-pN42rrP_M6OZLPIVsBCXRUrCjEIptPohzfTnlPdsGZppt-r1Q-PlsJP2uXiiplsP9kOsnAlOeXAb11zdRNTOQzWqt7HrAE668JxrFzUvGKhcQ84nIiVrLKRrkCOiWsRo6k-ruXF5GwFQIrf5yTzczEBEIKFcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از حضور مردم در شب هشتادوچهارم
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/437553" target="_blank">📅 23:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f9598ef8.mp4?token=tgolUtR1ukIyf8IrT2fIgovhfBeQcZixTEnjtGGkgZZ5srUlc-Fk6Q3KVM0DYatl70CdQBR2K9hZmz-4I7TJX1mjGIyFm7z8mpcFBzRDXxkhdgg2FH5oJFIfz4w83xV0KoPqDsXn8cYXFPXVcjAn2v7t1DbQate0TLAhgCTYpIlRvP8w3JKC1A-xfAsgc5sU_bw3rMtOc3q7a-IDfBCD2FGxe0bIlW3qndWMNdsP4ebeDR4QXzQdw9Y_1jae0_PdDVj7rSix2y7mEDTPWHbQE2gfJvQXvBOgjTMhJuLlgJNVz68N7OTshtKwGQmLc3K0TmVSjbDAWr6Ob7m4yfsmP4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f9598ef8.mp4?token=tgolUtR1ukIyf8IrT2fIgovhfBeQcZixTEnjtGGkgZZ5srUlc-Fk6Q3KVM0DYatl70CdQBR2K9hZmz-4I7TJX1mjGIyFm7z8mpcFBzRDXxkhdgg2FH5oJFIfz4w83xV0KoPqDsXn8cYXFPXVcjAn2v7t1DbQate0TLAhgCTYpIlRvP8w3JKC1A-xfAsgc5sU_bw3rMtOc3q7a-IDfBCD2FGxe0bIlW3qndWMNdsP4ebeDR4QXzQdw9Y_1jae0_PdDVj7rSix2y7mEDTPWHbQE2gfJvQXvBOgjTMhJuLlgJNVz68N7OTshtKwGQmLc3K0TmVSjbDAWr6Ob7m4yfsmP4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه ایران شده جان‌فدای حسین
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/437552" target="_blank">📅 23:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437551">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61c8c0629.mp4?token=JRhs_wJ6neqSPV6eZMOHlabBQqDUvHrxDjZoVJ1T3sn2RTS8VVQHlQwQNjzFZm8iS3bi0qqJv-o5i9bxm8Xo5WQD-3OYuahLCieBcca58Mf61IJPYn7h0WmNWiSM31pyt9uQAxb_W8x7UcwCudtyPJ8dBn5NvBDtDQqdLqWiPhfMyjABRDefWjpD3sFq6r3IZ6HYYdPxtJwzTl_h6cDxhaArs3FI4lTuugdRQ6b6y5hNpz6EJKiD3ihNeRY0-uu4rUK5G8hjocHbPUu9m-Ka824AtecEyipaoO0zTP6WSv596pOyUP7Za7epa-a_4OKmJzDcLDilznz9gipHzdi8Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61c8c0629.mp4?token=JRhs_wJ6neqSPV6eZMOHlabBQqDUvHrxDjZoVJ1T3sn2RTS8VVQHlQwQNjzFZm8iS3bi0qqJv-o5i9bxm8Xo5WQD-3OYuahLCieBcca58Mf61IJPYn7h0WmNWiSM31pyt9uQAxb_W8x7UcwCudtyPJ8dBn5NvBDtDQqdLqWiPhfMyjABRDefWjpD3sFq6r3IZ6HYYdPxtJwzTl_h6cDxhaArs3FI4lTuugdRQ6b6y5hNpz6EJKiD3ihNeRY0-uu4rUK5G8hjocHbPUu9m-Ka824AtecEyipaoO0zTP6WSv596pOyUP7Za7epa-a_4OKmJzDcLDilznz9gipHzdi8Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سامانه ثبت ادعای مالکیت املاک راه‌اندازی شد
🔹
تمام افرادی که ملک و زمین‌شان قول‌نامه‌ای است، ۲ سال فرصت دارند مدارک خود را برای دریافت سند رسمی بارگذاری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/437551" target="_blank">📅 23:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437550">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd89a3dae3.mp4?token=hMTV3Al1vuWwDkc7KStQwId-tRH7BRat32G_KCD7F-DNHg23r5nD8VKVxe0V8uqo4pPwzQigVSrrv4ukOKQWJfMmaOXmJJhdAzfRdLrhfg8lq7H0RgyCqtn1B6frehyWxwLAsmKrTSmbE6fdLPgPYTb1Xlxvt34qM9wdqqvoMnpWlAnnNyoZZ25L7cccmEsmWnbG2v5oe5JRtNIrwfvs6lm7Z0YrePE6_WTtnG6Al089UkOg7_21iElGlOWFOoQugszqP6jTpbv5WhoyCh3vr7g8PLi5GtQi9SAm-UJadNARqOy8F4R-HOLnO0jPMPG6-Yb_37u9G9kJqMm3E-GVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd89a3dae3.mp4?token=hMTV3Al1vuWwDkc7KStQwId-tRH7BRat32G_KCD7F-DNHg23r5nD8VKVxe0V8uqo4pPwzQigVSrrv4ukOKQWJfMmaOXmJJhdAzfRdLrhfg8lq7H0RgyCqtn1B6frehyWxwLAsmKrTSmbE6fdLPgPYTb1Xlxvt34qM9wdqqvoMnpWlAnnNyoZZ25L7cccmEsmWnbG2v5oe5JRtNIrwfvs6lm7Z0YrePE6_WTtnG6Al089UkOg7_21iElGlOWFOoQugszqP6jTpbv5WhoyCh3vr7g8PLi5GtQi9SAm-UJadNARqOy8F4R-HOLnO0jPMPG6-Yb_37u9G9kJqMm3E-GVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار لبنانی در شبکه سه: حزب‌الله بر روی نابودکردن گنبد آهنین اسرائیل تمرکز کرده است
.
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/437550" target="_blank">📅 23:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437549">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58b5e1b46.mp4?token=YWjHhp18tz10WvYWSWX2aQs15cxhRiU1sRCSGnlr36lgJsIwZYzMk44SRnptHJ6vE6ljBWxxGYFVBifU20p-Cmal1XUxqasO_xsL6QS1KluM6zo6HgovETw3_rjpRc8fStDtb_HaX3qnXN11JAZa5y_-_FbF-PAwYzemsKpBAmgGn0du6r0tm_943hep8RfRDHCxoJJUywZEd6NXFjlRaB7T30Aj6QwhE_Tekjl8OfCZ-mMWovehEEmFr6dfBgwDg8cZj2d9N6NTQ_VEzwnqLvwIrR3dtDoUV3WKBH6hvpqgJPylgCN2jOl4T9aVQyP0VTiGEzyQ2FGaQwjOU0wj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58b5e1b46.mp4?token=YWjHhp18tz10WvYWSWX2aQs15cxhRiU1sRCSGnlr36lgJsIwZYzMk44SRnptHJ6vE6ljBWxxGYFVBifU20p-Cmal1XUxqasO_xsL6QS1KluM6zo6HgovETw3_rjpRc8fStDtb_HaX3qnXN11JAZa5y_-_FbF-PAwYzemsKpBAmgGn0du6r0tm_943hep8RfRDHCxoJJUywZEd6NXFjlRaB7T30Aj6QwhE_Tekjl8OfCZ-mMWovehEEmFr6dfBgwDg8cZj2d9N6NTQ_VEzwnqLvwIrR3dtDoUV3WKBH6hvpqgJPylgCN2jOl4T9aVQyP0VTiGEzyQ2FGaQwjOU0wj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقی‌پور، نماینده مجلس: شبکۀ حیاتی کابل‌های فیبر نوری جهان از تنگۀ هرمز و باب‌المندب عبور می‌کند و ایران می‌تواند این کابل‌ها را قطع کند.  @Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/437549" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437548">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9662ebde8c.mp4?token=tEbpBkXes4uoCAI8YiN2y3agu1QczNH9x-7cyzORZY8LuLU90N7evmsXdy5L-jKvf_kp-bPuCLawqqqAcytej2ceOoNK_-ZmmHbJ87FBe6iaUCeIp5Joz0XY3kbz8-M-NoRiZL1k8U0Ls2BI0BCJvO8ei4uDYfFbBQDpf5r2fdKd97bQaifJI0uBEWk5ruwNBSMCaf6MrvhYm6k2A_lo39nzhT_vEFGyWV2A4njC1p8y_M049Nl2Qd3iV714muxcP7w0JdAvMY2BNbMohqZuhEvnaV2mChNGd7pnx-voJxULcy1th2aHcZMqRHNvoKaMNT-KMEwfAsk-4OQgK1tp23NlwcldEjCj7oplgg8eubWTl5y73hiQaWQxJCl9CYONkhAEzU4t9-gnDn09fC1-3KyV65eZFR3bIo12Nps2VSfgYQ7y9fJThdTWeQSmrba0CDlX6ZoRs3m3Oi54v3LPa9lNAueCMiLrQ0eQ6JfSTJ4gEBjyJ1PB8_nWi-DpCltBjN2l8FL1_Lt06dNYDqXIOhOqkIFgkH4xGRyiSfYpBRP4hKOeFzmIHfnpjPU3E9Il1cAGPLC9N2SkDAzxwh1VCAD0PuwOyRRmhowyHV2qlQuBj7K7Zq8rg0j8uT0uw_oFF99CiN-cXo6e7nWICg5iNj1VudQrjYI3PN9Dlxw_1yE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9662ebde8c.mp4?token=tEbpBkXes4uoCAI8YiN2y3agu1QczNH9x-7cyzORZY8LuLU90N7evmsXdy5L-jKvf_kp-bPuCLawqqqAcytej2ceOoNK_-ZmmHbJ87FBe6iaUCeIp5Joz0XY3kbz8-M-NoRiZL1k8U0Ls2BI0BCJvO8ei4uDYfFbBQDpf5r2fdKd97bQaifJI0uBEWk5ruwNBSMCaf6MrvhYm6k2A_lo39nzhT_vEFGyWV2A4njC1p8y_M049Nl2Qd3iV714muxcP7w0JdAvMY2BNbMohqZuhEvnaV2mChNGd7pnx-voJxULcy1th2aHcZMqRHNvoKaMNT-KMEwfAsk-4OQgK1tp23NlwcldEjCj7oplgg8eubWTl5y73hiQaWQxJCl9CYONkhAEzU4t9-gnDn09fC1-3KyV65eZFR3bIo12Nps2VSfgYQ7y9fJThdTWeQSmrba0CDlX6ZoRs3m3Oi54v3LPa9lNAueCMiLrQ0eQ6JfSTJ4gEBjyJ1PB8_nWi-DpCltBjN2l8FL1_Lt06dNYDqXIOhOqkIFgkH4xGRyiSfYpBRP4hKOeFzmIHfnpjPU3E9Il1cAGPLC9N2SkDAzxwh1VCAD0PuwOyRRmhowyHV2qlQuBj7K7Zq8rg0j8uT0uw_oFF99CiN-cXo6e7nWICg5iNj1VudQrjYI3PN9Dlxw_1yE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم بروجرد برای امام باقر(ع) در هشتادوچهارمین شب تجمعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/437548" target="_blank">📅 22:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437547">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnvP8-bGkpwiFbGvKW0LJXvkPDPT4OpQTpbhP4CDmij8R7_SNPP33OmajuTlf7G5ra-UqHO4MKwK3v5JkUKU1KvipQjClMLSP1eY78vN9C2sSU2K8tXop0pm1iRLO1kWpG3rnR1RqbT3xEb7xwywaM8kgkxNbFOsMxGvo3YbxgVnnYPiExVopP7dfyWmhQhG9MmE7WziscjLxEhtZWE0TdkakrTQ2OhkkEWIstUIS_OX4Yl4qB2XoFHmysrWpxquiHLlv5K0faKJvzYTky11J9GBUmmdfEtZMmZ9vBXBIZwSk5wiQAS4k_sBbN74n-t5Cyg4arrT22VY0ZBk6bsjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار امنیتی سفارت آمریکا در اوکراین برای حمله احتمالی روسیه
🔹
سفارت ایالات‌متحده در کیف: اطلاعاتی دربارۀ یک حملۀ قابل‌توجه احتمالی ازسوی روسیه به خاک اوکراین دریافت کرده‌ایم؛ شهروندان آمریکایی آمادۀ رفتن فوری به پناهگاه باشند.
🔸
ساعتی قبل زلنسکی، رئیس‌جمهور اوکراین هم گفته بود به اطلاعاتی دست یافته که نشان می‌دهد روسیه خود را برای یک حمله موشکی سنگین به اوکراین آماده می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/437547" target="_blank">📅 22:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437546">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c759e7ed29.mp4?token=Ec5SqxGYn9mLytIIsEz5F5ahxiCslI4NyU2A3AEbiSXZxoVK0xFusO9CPLrUdEB4Ef9YKgjOinBSkxAIBN0_mXuiOmY6KFj1Xrig2h7E_ecEmvQsDYQCHXBhclJdDANhkP-M9qqoRqXor-pYfnoaQMJYHN_zjyO0ar_xIm1SJAckoM58TwpHlyr-WWjXKgYmD6N_zYZs4DW_PJVvgusGbxDDiqe5yEGMM3U5fBhiZA7oJUtrKFHlLgWPB3yJMQ9XmaGH3rwSLHqFVL9YaDAu_W1I3Ze6Znw_bHAA9PsLUdW4E4hc1i318rcs66Rv7WdUeCokFQjYxkQmWr5WyglD_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c759e7ed29.mp4?token=Ec5SqxGYn9mLytIIsEz5F5ahxiCslI4NyU2A3AEbiSXZxoVK0xFusO9CPLrUdEB4Ef9YKgjOinBSkxAIBN0_mXuiOmY6KFj1Xrig2h7E_ecEmvQsDYQCHXBhclJdDANhkP-M9qqoRqXor-pYfnoaQMJYHN_zjyO0ar_xIm1SJAckoM58TwpHlyr-WWjXKgYmD6N_zYZs4DW_PJVvgusGbxDDiqe5yEGMM3U5fBhiZA7oJUtrKFHlLgWPB3yJMQ9XmaGH3rwSLHqFVL9YaDAu_W1I3Ze6Znw_bHAA9PsLUdW4E4hc1i318rcs66Rv7WdUeCokFQjYxkQmWr5WyglD_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور  آهنگران کنار مزار شهیدپاکپور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/437546" target="_blank">📅 22:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437545">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c03480e0d.mp4?token=VFJPy30CLENoNE7wVcZyutHSUkxoQhkzry4nT2HIoA59_AkOq470l0mVAp52rfgZUJ_XzhddTlCjJt7hmfgul_Y1OOiDIi3r3LGBwz5H6oWxdn8Q6TTJybyKbfV21rTBxeoRLXj_q_mkYcG3PzirEWdyq95gT9PS9IfKa02SJEQVZZgJYagXbWgM_nI-SFKPtvQkdIgOW2aafWYdVTwYzx2JwImpaD9Q3wFJ85ltej91ph0uSBoUE5PaaqnmNt-KfCTQ4fo4H7XUFDWrsvXNzoJHagCReNHlJeAtWR66sspHWRDP4xdBlUOpNvepjU2pfVnIdib6ycXzJ1C1oKo6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c03480e0d.mp4?token=VFJPy30CLENoNE7wVcZyutHSUkxoQhkzry4nT2HIoA59_AkOq470l0mVAp52rfgZUJ_XzhddTlCjJt7hmfgul_Y1OOiDIi3r3LGBwz5H6oWxdn8Q6TTJybyKbfV21rTBxeoRLXj_q_mkYcG3PzirEWdyq95gT9PS9IfKa02SJEQVZZgJYagXbWgM_nI-SFKPtvQkdIgOW2aafWYdVTwYzx2JwImpaD9Q3wFJ85ltej91ph0uSBoUE5PaaqnmNt-KfCTQ4fo4H7XUFDWrsvXNzoJHagCReNHlJeAtWR66sspHWRDP4xdBlUOpNvepjU2pfVnIdib6ycXzJ1C1oKo6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: موافق اصلاح ساعت رسمی کشور هستیم
🔹
تغییر ساعت رسمی حدود ۱۰۰۰ مگاوات کاهش مصرف برق را به‌‌دنبال خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/437545" target="_blank">📅 22:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437543">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c92e8dd2a6.mp4?token=WFb0GWro60603dg60EiENYnPQ933q3JgJwoeKzHrghmVxlfE-NjXqq3i04ujGB_UGwiMy5ICtLrCUza9O96kKytM6fGCHuo2bZurVIcD-2OgjUzf2dMTB5vPKt6E2q2zprBC0dVohPualk5Y5dKT3NJcQxnUL8IWQpXfEAQ0kVK7MbhczviPeRHv-xm_A3uBOKOXXC-lVqvbPsWXJ5I0aA6bE5tkTEhgP3AEIBHVsLYzU5DLl1kqOtopkHuwGmRIMe-y0c78NeXFxYrjj3eClxL79qrarZoGcaRAGu9S3YP0DsZTSW0_ESrc4wHnFnnBI2XbcYlvbO86E3d9wbPQiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c92e8dd2a6.mp4?token=WFb0GWro60603dg60EiENYnPQ933q3JgJwoeKzHrghmVxlfE-NjXqq3i04ujGB_UGwiMy5ICtLrCUza9O96kKytM6fGCHuo2bZurVIcD-2OgjUzf2dMTB5vPKt6E2q2zprBC0dVohPualk5Y5dKT3NJcQxnUL8IWQpXfEAQ0kVK7MbhczviPeRHv-xm_A3uBOKOXXC-lVqvbPsWXJ5I0aA6bE5tkTEhgP3AEIBHVsLYzU5DLl1kqOtopkHuwGmRIMe-y0c78NeXFxYrjj3eClxL79qrarZoGcaRAGu9S3YP0DsZTSW0_ESrc4wHnFnnBI2XbcYlvbO86E3d9wbPQiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از وقوع انفجار و آتش‌سوزی در مقر کومله در اربیل عراق خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/437543" target="_blank">📅 22:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437542">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21852932b1.mp4?token=TdLu_E19NXZHw47ERxt9wW4JXLwbd9FZZjSUl1jUGagE9u6F5jefkz5iQ4wnwtP0maQ7ZYPzD1gfXIJuv0gFO8gc5cVJqKbqtfSNvV61D-dAVYMGveOV1Eq7Kqtni1kxINFzIlqqAoQoU895X8syQ0vlid_N5oXaittO6eAyiZrxR6BPyNc6LW2sjQmS-eQdweGWtMs_LGUqz3JU8sfbM8ecdzLKZR6GAxfj3ks2AdC1afUPP3mBQjRcudL9MRh8EnVgqjFm8oJU53SDBVx1Jx4lwVRCegQm0lb_uGpRUbm7MVm5MwNOl3SlO-5NToDQhypZgJga_lDxInEWdqzEPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21852932b1.mp4?token=TdLu_E19NXZHw47ERxt9wW4JXLwbd9FZZjSUl1jUGagE9u6F5jefkz5iQ4wnwtP0maQ7ZYPzD1gfXIJuv0gFO8gc5cVJqKbqtfSNvV61D-dAVYMGveOV1Eq7Kqtni1kxINFzIlqqAoQoU895X8syQ0vlid_N5oXaittO6eAyiZrxR6BPyNc6LW2sjQmS-eQdweGWtMs_LGUqz3JU8sfbM8ecdzLKZR6GAxfj3ks2AdC1afUPP3mBQjRcudL9MRh8EnVgqjFm8oJU53SDBVx1Jx4lwVRCegQm0lb_uGpRUbm7MVm5MwNOl3SlO-5NToDQhypZgJga_lDxInEWdqzEPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: هرگونه تجاوز دشمن با ضربات جبران‌ناپذیر مواجه می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/437542" target="_blank">📅 22:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437541">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65c39bae.mp4?token=iDS91fHnyG78KeTVYeWzt20gSZR-wKuRY1ORf8GWwERx1SpJztfS7uzkBcGxf92RBkHU_lg3ENtvkKom6uE0nFpLK-ooKyEsDxY24L05P9ntWSoROlqr21p00asdfF83Gzla1_s5l3QzcKs39K1kfhDyBbn_MMjS57TkGb4sikijcBVtB9nByv7_8S9iBDqirvlX-kVGoZHrUJmkzgtk4AsKkifkdEVuc20NR_5EndpNTfrPj1ATCRB5XBlWq-c3nVvMy6yEM7S00ajtig9wH71A326rhLSdXAtDkTN2Ntkfe6D55EWJfnMjzSObTO_M2694OKPIkKXVanCwzG3EYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65c39bae.mp4?token=iDS91fHnyG78KeTVYeWzt20gSZR-wKuRY1ORf8GWwERx1SpJztfS7uzkBcGxf92RBkHU_lg3ENtvkKom6uE0nFpLK-ooKyEsDxY24L05P9ntWSoROlqr21p00asdfF83Gzla1_s5l3QzcKs39K1kfhDyBbn_MMjS57TkGb4sikijcBVtB9nByv7_8S9iBDqirvlX-kVGoZHrUJmkzgtk4AsKkifkdEVuc20NR_5EndpNTfrPj1ATCRB5XBlWq-c3nVvMy6yEM7S00ajtig9wH71A326rhLSdXAtDkTN2Ntkfe6D55EWJfnMjzSObTO_M2694OKPIkKXVanCwzG3EYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار ۸۴ مردم بجنورد با بزرگداشت شهادت امام باقر(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/437541" target="_blank">📅 22:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437540">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">۷ نماینده کاندید نایب‌‌رئیسی مجلس شدند
🔹
علی نیکزاد، نماینده اردبیل
🔹
عبدالرضا مصری، نماینده کرمانشاه
🔹
حسینعلی حاجی‌دلیگانی، نماینده شاهین‌شهر
🔹
حمیدرضا حاجی‌بابایی، نماینده همدان
🔹
رضا جباری، نماینده مسجدسلیمان
🔹
علیرضا منادی، نماینده تبریز
🔹
پیمان فلسفی، نماینده تهران
🔹
انتخابات هیئت‌رئیسه مجلس دوشنبه این هفته برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/437540" target="_blank">📅 22:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437539">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyrS0d-rTyiXFqFSzCdx-FOZcsx5uOhQwnUDZp6CbNF_A9G1PQKWaNj3h9UT2nyH6ZL3jJ03ucZVWiRbozOYMATERZUh7AEENsbfHZzKbeT6DwTRItMFNRrUDuKtyINI3RzYPU1hZWN0FCO0A_Yy7y74zhClkW6deTHnhQ9AJzGGti5mfkmLzwBZC1tAnVvwf9KLKJTiL5VcnsOBgmGCxySC0hptdM2YApQWckfNnTT77x5I8lolfUMwmTck49CcXtwKv8yrvhkVtwG5V-SiDrlXyTR8iHTIW7IA6u3TbDCvDE_2x8X_YuVt8aipB4VHd_AYxxl2vmI4FEHlK0EkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد پرسپولیس: تورنومنت ۶جانبه برای انتخاب نمایندگان آسیایی برگزار شود
🔹
درپی مبهم‌بودن وضعیت پایان لیگ‌برتر و انتخاب نمایندگان ایران برای مسابقات آسیایی، اختلافاتی بین باشگا‌ها درباره این موضوع به‌وجود آمده است.
🔹
پرسپولیسی‌ها اعتقاد دارند نمایندگان ایران…</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/437539" target="_blank">📅 22:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437538">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0151919d.mp4?token=HUazb3UZnAVXjCYK9HG1n1Yy5BSSy79Na08r932f-SEhmw5-N6Md8UfEvKefIfgnYdd252dKxHqLi7WUBoIxkRLGVlxBck4lQFGlIjbzFf8ECY3GVyEH3aKT2hcqk02Es5iDMpPXy4Jk1XDflk2EWz0D1De9bDj0kkLOwcaepiCmNUXH5P33yPc9ybYJVSJ8iVvK8RYUaXFPhYvBO-S1EraC2iJx1C6SsFA_3Qwh15DKG2qhFHoQcLmjUF6HFGIYtaMjBwYTOgpoiDldoww9W4OwF-N3CkwU9inyxK4iHdi6sgwII5ovtRy4KRGHRvN2FvlkMYLtG8ML5fVuyjdHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0151919d.mp4?token=HUazb3UZnAVXjCYK9HG1n1Yy5BSSy79Na08r932f-SEhmw5-N6Md8UfEvKefIfgnYdd252dKxHqLi7WUBoIxkRLGVlxBck4lQFGlIjbzFf8ECY3GVyEH3aKT2hcqk02Es5iDMpPXy4Jk1XDflk2EWz0D1De9bDj0kkLOwcaepiCmNUXH5P33yPc9ybYJVSJ8iVvK8RYUaXFPhYvBO-S1EraC2iJx1C6SsFA_3Qwh15DKG2qhFHoQcLmjUF6HFGIYtaMjBwYTOgpoiDldoww9W4OwF-N3CkwU9inyxK4iHdi6sgwII5ovtRy4KRGHRvN2FvlkMYLtG8ML5fVuyjdHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار تجمع امشب بندرعباسی‌ها: ما هم ابرقدرتیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/437538" target="_blank">📅 21:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437537">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbc0e5dea.mp4?token=FYVi9y3sjWBPvI2icbSAKxmyjMN_UFPuCMACBFeHT4Q6Kddk_TXfKDfzl8tA3oGHr3M2Gi_cM1mXqYUYG2NBNkjLYuQpjiipZbfwk7JleHSFkaou6ivZVvFZNSuPJggeBUb9lh9QwCxUbD-Vf3GUY4R4Lm7XUhsi8TvdnB1qwOUugcKbuFOEI5cS-VJEBnWxIepVEAsR9N5hmRoFPXmB1YniEewGGyNUIwBeFb-13eVtZ4HEU_T_H0-KrPbVpFFIiLxl-JDlJiGUnC-YbEpb9y9o-0GksFbs9-wQ-EwDv5k_1CZOlOil1T1cImM7nyPnV-Ey0RiqhswKB5vUM_EpGnPBcOsSxlA_TWdeqDnWrU_fXt_0HI9IdAo051ohFxHNVSGvEsd7-ZENinzqI-sxyYJD9QMtKCs3xKhzyfmR3HWcNagT4vSbMy3ObUbu0b4HdHTPTjI3UFxNLYaHuhaTksBSxpNl9m9Hquj-M2t7OJDBSGTR_7R7zUCWMXF9a4M44UJeOAe8SFp40mChTRZHV0ouBPfscoSp5A0dwlu4_dAzmzoVJO3-Cyt9X9wugE2fuAGJgFpfx6UMYvl0MZtxSlT6J1kLbXbYbdxL9kLfz0yvU3CEHpeEvOij44mCEUkzYunx_U_vcq8HvYl9W_wGheKPsQFEHa5Ww2_Ejk0JMes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbc0e5dea.mp4?token=FYVi9y3sjWBPvI2icbSAKxmyjMN_UFPuCMACBFeHT4Q6Kddk_TXfKDfzl8tA3oGHr3M2Gi_cM1mXqYUYG2NBNkjLYuQpjiipZbfwk7JleHSFkaou6ivZVvFZNSuPJggeBUb9lh9QwCxUbD-Vf3GUY4R4Lm7XUhsi8TvdnB1qwOUugcKbuFOEI5cS-VJEBnWxIepVEAsR9N5hmRoFPXmB1YniEewGGyNUIwBeFb-13eVtZ4HEU_T_H0-KrPbVpFFIiLxl-JDlJiGUnC-YbEpb9y9o-0GksFbs9-wQ-EwDv5k_1CZOlOil1T1cImM7nyPnV-Ey0RiqhswKB5vUM_EpGnPBcOsSxlA_TWdeqDnWrU_fXt_0HI9IdAo051ohFxHNVSGvEsd7-ZENinzqI-sxyYJD9QMtKCs3xKhzyfmR3HWcNagT4vSbMy3ObUbu0b4HdHTPTjI3UFxNLYaHuhaTksBSxpNl9m9Hquj-M2t7OJDBSGTR_7R7zUCWMXF9a4M44UJeOAe8SFp40mChTRZHV0ouBPfscoSp5A0dwlu4_dAzmzoVJO3-Cyt9X9wugE2fuAGJgFpfx6UMYvl0MZtxSlT6J1kLbXbYbdxL9kLfz0yvU3CEHpeEvOij44mCEUkzYunx_U_vcq8HvYl9W_wGheKPsQFEHa5Ww2_Ejk0JMes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاشیه‌نگاری فارس از پنجمین تمرین تیم ملی در ترکیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/437537" target="_blank">📅 21:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437536">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8lSDENN7ZfHB3v-5e2ZvQMtF1yH-1Ek-E0hhzI4VjBOUvRB129W4Q93BSDqVLQKHYIQfoJEvQVyKfewZq1_oPw4dUvoUgpY6kq1SX0IysgYeyFZBP-WzfTj6T33Y1v0ifv48BegoQyq84czc7-SgxbxDtFmCeJUhQCwqdgdpeW3ML792RrQ8HN4DjoHT2T1Ud04SNvVnualR0NSnKKJW_1DMF2-9DWNqNSwJ-F9cg10TVpBgSZ96aD8pIumUjYh8GDvlPS1sBNwkzCWUaOHZy8NYdBAZU6dw2dFhisxgKieRFI0Xjjtgk_qZcdtM056x2bEek3zVdyY3ZSsFr1JSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال صهیونیست: ایران در جنگ پیروز شد
🔹
گیورا ایلاند، رئیس سابق شورای امنیت داخلی اسرائیل:  سناریوی بهتر برای آمریکا، بازگشت به روال پیش از جنگ در تنگه هرمز با رفع محاصره علیه ایران است.
🔹
ایران در این جنگ پیروز شد، شاید پیروزی با چند امتیاز بیشتر اما این یک پیروزی آشکار است؛ آن‌ها می‌توانند از نتیجه جنگ رضات بیشتری داشته باشند.
🔹
آمریکا در تنگنای آشکاری گیر افتاده و در نتیجه این امر، اسرائیل نیز در مخصمه بزرگتری قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/437536" target="_blank">📅 21:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437535">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
آمریکا زیر بار هزینه‌های جنگ؛ ضررها ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/437535" target="_blank">📅 21:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAYQFYaCw9MSMD4uOaDTWT0hQ-bS_NKcAZyydRSEdsyp470TVUFZgDNRT_yfe4Ipk1vfYmmMqXTyjcEueiXw33wvNamLKLUpa4HmK7r5VdRss9iRG0GdtlIvesU1EENXMc0VZLHBTbM90DjDwvifRsiVtiUsSVPVGOS_TxU6V-4MjK2Z36X96lWjkA1CFQmm1SXWc6ouCk2o_EeDOtgVFVA6ri84tsz5Pf3OMpYYZ9uyrJFp87c1sv43-EAQ5Geh8-zTRgXwGKP8vl6ufJFYvzvbUqr5VhbdfOOS9SI1kcXZP-I5N9e5cPkZ7lDD0y8LuhebVhmnydM9V8rse5QS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1sJoGPvQouELgC7YNo2g3QpG5UsomRVzwswoE_W8fRgJAF7cHb2mrETEhXEPOuLkBsXQdI46-2rcCbkUz_wOTP1lzS7AXMq5cvLfqLnlor4FsGK5kMyU7HVfnpDUjCGc98XwsBGdSvI7qg8KUAF48acvaIOMAzLx_kOCJp9RW-8hjcd6rlW9DCCsMBSVga0HC4ju4x85BTBaWdy3GvOXdhGh4RA42TzzxchyeIMadcU0oONnvqT0iU5-kX1A2HBvP2TcJA97pUgqZ9m1p756MQU16jsbBgtkOsKBuMybDRGMXfpg9GeRMdl0RrO5CC1-cU_HSQQGZt-odVpeOckyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9ebEWu4TiD2C2RUbxf8NNQ2HOYVr-G_Mp7gIB855yNmx9Ws-q7LWMV4VQ-qNIpBNg-A5Awwps2sPLNxgPpIqkIRMoQfmTxGfjmihK-vdUvq2aw2Wy62QAcADHdT-epPVpXoGdgQ-eZqXYTXNatohiLutwaVRusj7uUkWECrLoFkTOfjiYT8ZTytiWANByhHPCBBkNd6lYAbYF_ZSL29E4wF0PO4BBcewH7VFXhBH29WzC3QpgOtMLWW_70TEvNJAOVUrtpZGLy_0aQUcnmWss7nz7ge_UHkk7pNEEqNakoaamM4RXtmhx3-52BHsUXig2N5C1T3IfeXPAtFq3O_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNpAoiiBymldUaOHNMgypqD6qysfCb2QqmLT5UrHObILHT-UEHCYLrZqXjLLmc4mZctMnpFJO45djVmYuqWU6goa0mlu1UxF5biYPhX85q3CJx6dHTajVKh4K1g3ZF-8oXutQhhhsmcFvuDVNjiQs2tQfAOMF9Bwd_3enHiecmrNu6dc4UBnN0xJMkmCTA1GzQAWu-te3HFDLwbXBApEMZh-bRZf83eGKEhhOTbG9Oag71okrMp29eWMEQTKdeIuS3dgl1kQtxn04C-rfp-gpYTNZA6rvfFOS_sBd_YenTZu5BQkBtgW9OT8c8I5QMlNaz8NHS3GqP23kvBExje9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ln0w_zv94OFsEN-c7-GObYREY_RGkrrtq72EfpPHO2B76_YADt_B-QDQe7L2HCuiLdm7SxH44A-nk5T3h5d8jckQfuT7dm8U17Ni2Z7cWAh-F_yEE-l0RfmAXY8rXUQP7Vbd2Odzx1CGrADduDfV-qIizUQSUScCGRImzNSVxaq1WIciqJrkhRupzpyya8ZHKp9daKVgYiR4-Zq_6gJq663f392T2dF5L09k9Pd4D54tC-QTORuCJm-zR7656kg-uAqCCPwxoO4sIvSC1TSsVM0fzYP8yWmtsVTS2wgF589jusigIRFxf54ttyqv0ds4Lcgl5zlx7iGS5r1uC_pGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtpfGI9FSGabCu5WMcpjaKpWGaxXc9wTpOT5kqqGuswicEu_oCsowxy8ozsa8HjzHTaFTuA3bSfR3gniaeKJh85A_F25XjrMbFE9AbI7T_i4wAPFSFYi8kuyqAz92kgiVHvC87lX-N1j5aXYUWfOeTvOdQgy0gVTe-osLjE4PXIBPUXx3s6kkdeRWQe606EkxpmLSN1KtBaGdhPTPltnYgThHxz5BQ53GL268QRsiNYo4P8p8R76SX1eLDqExoxKMc7iPUM29dw_E2HAsBcSbqFiX_oDdHNo6BUB-Hki4nIyuMpZegTgKpYS6iSSRjxLPEVc7V4T-8nWkRomYKaFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPZg4rijt__HSToI07e_R9e8v77FHg-0lVoUJa3vbtHiuIzq7U2SJQZwq71pKykLqz3dVDAIdPs8B_CsJ_Ndk0_1HQkNizhSRFbqkPLijUnTa_jA8-KR6V6KFPov4MBm9H7rVXOACYmaKL5j_33cMmyKfvd6DYq-ryHIa1uwtQ5geB2JzJrhDc1Hx1qv1IKWhwmEuXSBGYTccjSyFOoegbxEoVheKIGNmbOdkpHQVhkD1aTvtzXjDqTffmYaESjMGu_JmmMphBPNPOxVUfYVhAwsd08jykKmO45GV4gxk_Ypc_fQTHEpezHROsTvqPBEwpziVyvTRDlMlBg9PJCdKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازسازی
کنیسۀ عزرا یعقوب
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/437528" target="_blank">📅 21:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437527">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTEHsNSXQZRl5E8Qdrr8tq2dGjviwWP1K3ZB9xVue1JE6lcp-9fWSilJINFxELsZRq8u6643GN3H9KUWpPz0IwRsThfNFsStPwDCa1RGFZjRZ2Wp1A3qjdHGiKGOuNbapDFEO8gyhjlOC5bIXXErDhbghNhBO8AMu2SNilQyh_7X_5aBtbIEjxGYScM5cyR6pNQbNm8T5Tgzh1Z4IGdARNfj9D9rRqhCRQuceigMUma8sd87b4GUFIKnqjUj3OlLLFlR2-yDC5DT8ScpUR_6hozmKV2msWJIFMvqZyWGk3B9wHRr8yUX3y3sL59ZoxJLqLhaxpCOcUjh6ZRSXzbkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ملت ایران، تجسم داستان‌های فردوسی
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/437527" target="_blank">📅 21:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437526">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0m1aFlFUXAGXhtMKHf04cPayYknWRCKXWgdnKkzXPA_yETfK6OC2Z3yMmv1xfahAvvs0MCUqjk-SnptYbwIkg6KkD45FY2o25umwf9wasHCtkCWBTNyRJKou0opHBCfYpYLxVemk-qGgm2Nhfjp49PiH5tDIwvpUgf9ni1Rwp39Wl6GiQKcNwRnB8sElCkc7e0lxO-j8QoIm8BOnPOfmdwF0GBQ-WaZySaymolMeTm7dIgRPxPZIEYQCoMq6kldEeJJfD9fuLnmT32_sfgMxJEjuPCCG1GkkdQFIMtWtyEG1Il44YGfYWwEClDq0mxL5aCOpEiABXbOnF1A7HTISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در مصاحبه با کانال ۱۲ اسرائیل: اگر توافقی برای اسرائیل خوب نباشد، آن را امضا نخواهم کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/437526" target="_blank">📅 21:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437525">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رسانۀ اسرائیلی: تفاهم میان ایران و آمریکا به ضرر ماست
🔹
شبکه ۱۳ اسرائیل: صحبت از مذاکرات پیشرفته میان ایران و آمریکا درحالی است که مسائل حیاتی برای اسرائیل، در این تفاهم‌نامه وجود ندارد.
🔹
اگر آتش‌بس بین ایران و آمریکا به مدت ۶۰ روز تمدید شود، این کاملا با آن‌چه اسرائیل می‌خواست در تضاد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/437525" target="_blank">📅 21:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437524">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
امسال صاحب‌خانه‌تان با شما راه آمده است؟
@Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/437524" target="_blank">📅 21:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iglnke4HmFiwHkoel9i28sQSg7WbLFIvTXsXxcXngWiuVnSnx7fySAtbZmjpQ2Ap7cZdSstBPYn46LH4gIUXTMsd6r5oTzMP1aJmYZMR3WnYS0jfe-MLHc62t-s7jXE8Huf7BjX6ZDVwDHNeETd1V87BEN8Opdd5y5q07llMX45rQNpNZMsvU7ix41XTLiarDUY-mUUyNrgP2PdnXjLnuJ0AqkRe2F9H5IITyqySubuUM57ZJbWjY5gHxqrmnKIiPWRd7ghMZfRL_Zb9ZJ_bgBIFB-2p9UNjkuRF2IGDQ7gmrYdSI2g8l28qDnFJjtw-citjr820LloRiWGSbCZNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گام بلند بانك ملت در عرصه تامین مالی با عرضه محصول جدید «تیما»/ ۵خط كسب و كاری مهم كشور تامین مالی می شوند
🔹
بانک ملت با عرضه محصول جدید خود با عنوان «تیما»(تامین یکپارچه مالی ملت ایران)، گام بلندی را در عرصه تامین مالی زنجیره تأمین برداشت.
🔹
تأمین یکپارچه مالی (تیما) به عنوان یک زیرساخت جامع برای ارائه خدمات دیجیتالی اعتباری مکمل فعالیت های گذشته طراحی و عملیاتی شده است.
🔹
تیما پنج خط کسب و کاری را شامل تأمین مالی مصرف کنندگان در عمق زنجیره تامین(تیما لایت)، تأمین مالی غیرمستقیم پروژه ها (تیما پرو)، تأمین مالی از طریق لندتک ها (تیما لند)، تأمین مالی در عمق زنجیره تأمین برای صنایع سنگین (تیما پلاس) و تأمین مالی شرکت های توزیع کننده و پخش (تیما پخش) پیگیری می کند.
🔹
تیما با تمرکز بر نیازهای مختلف زنجیره تأمین و با هدف حل مسائل مرتبط با زنجیره های تأمین عادی و پروژه محور به بهره برداری رسیده است و افزایش قدرت خرید مصرف کنندگان، کاهش تأخیر در پرداخت ها و کاهش ریسک نقدینگی در عمق زنجیره تأمین را به همراه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/437523" target="_blank">📅 21:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437522">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">#ببینید
آنونس معرفی منطقه آزاد ارس به ۸ زبان زنده دنیا
همزمان با روز جهانی ارتباطات و روابط عمومی، کلیپ معرفی منطقه آزاد ارس به ۸ زبان زنده دنیا با حضور مدیرعامل سازمان منطقه آزاد ارس رونمایی شد.
این اثر توسط اداره کل روابط عمومی و امور بین الملل سازمان منطقه آزاد ارس و با هدف معرفی ظرفیت‌های اقتصادی، سرمایه‌گذاری، گردشگری و ترانزیتی منطقه آزاد ارس برای مخاطبان بین‌المللی تولید شده و گامی در مسیر تقویت دیپلماسی رسانه‌ای و توسعه ارتباطات جهانی این منطقه به شمار می‌رود.
منطقه آزاد ارس؛ دروازه ارتباط ایران با بازارهای منطقه‌ای و بین‌المللی</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/437522" target="_blank">📅 21:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437521">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/437521" target="_blank">📅 21:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437520">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee30731dcf.mp4?token=QnbeV9Gt3e8geBeTQRlkzDJVLyMJhX4yRgjs7FjYOeQhY0dgxx9z6qE9Q8WDpjpBX_Q_lmU_4qubzwgjI0LrxzX8ZROFDaIVdjDYdnthDAst4Aac7ttHi6bVb9fJqhcfw1vFNoyx7TZA7mx1xtC93AS7mxTrNrR-2Jql6d_VCFePaP_F-OmZeNjRS0Kdu1IVcF1cv48yl4UD8YSAmOjnFn1aZY08Dnn2GcZBXYuZ8sgtuxpAhYaEyQ_aEYka5CiJIuZ7H4FKojnm-rnNSDdkf1tJp6M8j52D2kvhxHp89SYZuqx6m_pJWqY73Ht8WHpITQ8uJ9xa0cBB-nMnGvANAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee30731dcf.mp4?token=QnbeV9Gt3e8geBeTQRlkzDJVLyMJhX4yRgjs7FjYOeQhY0dgxx9z6qE9Q8WDpjpBX_Q_lmU_4qubzwgjI0LrxzX8ZROFDaIVdjDYdnthDAst4Aac7ttHi6bVb9fJqhcfw1vFNoyx7TZA7mx1xtC93AS7mxTrNrR-2Jql6d_VCFePaP_F-OmZeNjRS0Kdu1IVcF1cv48yl4UD8YSAmOjnFn1aZY08Dnn2GcZBXYuZ8sgtuxpAhYaEyQ_aEYka5CiJIuZ7H4FKojnm-rnNSDdkf1tJp6M8j52D2kvhxHp89SYZuqx6m_pJWqY73Ht8WHpITQ8uJ9xa0cBB-nMnGvANAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس فدراسیون فوتبال: کمپ تیم ملی به مکزیک منتقل شد. با این اتفاق مشکلات روادید حل می‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/437520" target="_blank">📅 20:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437519">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎥
محمد قربانی: به‌عنوان سرباز باید برای ایران بجنگیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/437519" target="_blank">📅 20:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437518">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
جشن تکلیف فرشته‌های ایران در میدانِ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/437518" target="_blank">📅 20:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437513">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IckWyR1f_f37vLIswlhdFbeK6SdUsCa8d_I6qKgvxX-gRYJme7DfabGWXDwsZxqQxTD96_1w4PGZ6EC68xOD5VYubzDRnwVPsr2BKiIPHdMRVVfmbZ5g9Q1fxuyfBFxqJQE3nHCFD4igJihkBMPK6bWOdVA-NS7DUOX96W3IMNa7L89Yk0nwfvh6_CYF_iUTPNFHEDAIQUpF2J5f9KQk_Jg_CxwNSfzKyqlQQdOz_Lc4S8H1UGDmbI4N6G3cJLxuI7yvmrlfj9FVyLm0aTZkz7pXoNpqX8Pd2Q3rrq2IhPhBq_AGWfz7BEZ_oTQNdFM4CwsQBlDz7eQ3rqCLgiSITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avEut572d2-NLFoMj4O8fGmzldRUEo0cbOngACF7L9UfaRNiu-ubdawAH6sSAY5q4wi-8QnHiAWuyIWYQDnqXtgBiPiFxigbwEUy4nL6a2pP01zoSJYRodafGC2WCgNOXivu88-nt1sGtzIMuczObEpmn5hbR-Fb8YmSyJkieb8OAKSEELj17VzTFz9f0gaM_YLXyN6J0zQ_Qp7FjW8JqFeK9WvGSAAo0fl1JrkqR4OVHQ2lCDgAj1O73HN0IxMmRI-dqD0fgorS9VpTsVH8RcFks2irWh0kQ5_zMpBdiboFZy7JKkgBOg7aDeSz9fZgdAwV55j_GfGVabQmL9hlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgfSGRgzsW3ydTb_jk5zbpyJGS6JGh1Uth9Tti3sdKEfX3leNol2ZzZU9dfB3L5Op9fQSW1bymnL-DHAMEZvz0R2mATJIobpxWlaTqfR-TIFH7er_hKYR1PboE09u3M8fdI6XJRKPbJyB4GvAnx2o-tU16gLlCr2ZUpXwlh5Ze7zWD70-WwNypQ_VPUhtbhy1q5OClFX04hdH0tsiQONtpQWkSyyzwLvyl7kh848xEgYcsh8W4CsW84EnuI8E2gXXQLKnufL9k6AEl1eZJlNol7DOpRNNXJLKNwY1CEpLQ946Ee3xusGRUHmeoEAXe6BjdWOtUFS8Nys8th97SlrtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tno35a_gwGcIUMcvtr98uy63lNvNNWDzNisjqlIB9iQukqLCfMDz_KoZPhi36D_MEHtJqf1ucvCEKEZDgNsLjUuxrGSZeXM83vFlGRwHSQZsMv4SnoOrwNOCcuBIWC7_1K7Vcd5VMTjCSwAFmTJi-Q-RelVHBfr6CViKKjWS1ZfW8zTrQw6YuKER1RoxK8cydE9JThDSzFPShACwVWIAuxRxbygVC8W0VRe1uPzutRf4fISMn5yryXhtXuYcN_NZ9Fh_lDngQlU-pU5HLc3P9DY6QoXF1cTiSmcwNOYUcrToILqJIvsKT8jBTSCUZm8GpJL8dCjde3AmGm71Nfo07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsskEcJ5oEn3BcAsC1RhGNbGzVjlcp5sJPOL0PoTIU4QJZu57ScpjdtSnWzaXw0iunpjWF6uyLdYRbkUXfKIxpB3XpIcd1hbadrlsHYGCcL596M0WqkxA5513Cfko_IvC7fkF1Iy20s-kukXTJsRt3Y2-EeGPhiKLYNuDTYVvJUrDOpN2X99oWxL4BTFZh-Bcr2nQUpy6-w-CYB6d254tDv7uAKSHDWGhOEtlBWYjZnbmgNCVcAh0RLXUWNb1gk2W3Lg1XOZHgfoN_JJ7YW1NyeHgNu3UCtuoTEMCDcpXC8aZ12WspcvDo8noIpztFhHEerR7Tf4E2lMo-mTbrrfCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت حماسۀ سوم خرداد در چهارراه ولیعصر(عج) تهران
عکس:
محمدحسن اصلانی
@Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/437513" target="_blank">📅 20:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00dd641236.mp4?token=Ix-3tjzt1S2OFy0FYIIyb11pQ0flhkSD2TZtiIPHBU3taNXSTM0dO22Pl4EGYTt45JUEpy_oR_-UnfGlCJziv5Ysgpv6RHiewTf_yx2XWvF6PBWYeX1eCvDMPv5m3HTnz2zDupLdYm0mCJGb3wpjmt42GdaIolgyuUnT_I61OI4_-7-ejue3v80loBsC8-7WnsM_qi8ijav3ohCOdBPZ-1uzuzU2nEK5zJ_T8tD10htI0mJSppzlaRBCXXY9MtMnWplysuogfQMbJ_o53nlBT0thkkohf9az3cfRPqY4OMntgzHyd6xrEklIioA2BwBe3VNKZbW9bunQOhOFH-jv5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00dd641236.mp4?token=Ix-3tjzt1S2OFy0FYIIyb11pQ0flhkSD2TZtiIPHBU3taNXSTM0dO22Pl4EGYTt45JUEpy_oR_-UnfGlCJziv5Ysgpv6RHiewTf_yx2XWvF6PBWYeX1eCvDMPv5m3HTnz2zDupLdYm0mCJGb3wpjmt42GdaIolgyuUnT_I61OI4_-7-ejue3v80loBsC8-7WnsM_qi8ijav3ohCOdBPZ-1uzuzU2nEK5zJ_T8tD10htI0mJSppzlaRBCXXY9MtMnWplysuogfQMbJ_o53nlBT0thkkohf9az3cfRPqY4OMntgzHyd6xrEklIioA2BwBe3VNKZbW9bunQOhOFH-jv5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف‌قراردادن خودروی فرماندهٔ تیپ ۳۰۰ ارتش رژیم‌صهیونیستی توسط حزب‌الله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/437512" target="_blank">📅 20:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Djymox14ks9KyXG2Ql3J6dkdp5vcVvE8LsRG3tfVqhaBfPKMnAhTNlRAdjg17mVgynCL8OZTafMgrTMRkJwL3HBgTjk8TRHkO5w-h2TjkZrykD2WEcU-I1XCB-7YdJ6mCZHvMikLWAi1_4XoLMaEJWyoVmKlA-nNUcmWIWWOcX7QtmUPBfgjdf5Hilxam1EuS5GCaGWa_6zTtSNb5f9bKJ-Xxnwf3KhjBK7vWKx0GwQrJvv3hA-KUXV4yhm6leOrO8ks4Tp-KgkR--fXBPJepStLGFQ4ziQSJgcKn9HYgVKkMekZ8dg_h3PZSplwCnjwxGyTw6sUUY8lHh2rcUw1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات آمریکایی در مذاکرات با ایران: به توییت‌های ترامپ کار نداشته باشید
​
🔹
شنیده‌های خبرنگار فارس حاکی از آن است که در جریان تبادل متن با واسطه بین ایران و آمریکا، برخی واسطه‌ها و نیز مقامات آمریکایی مرتبط با مذاکرات، با واسطه به طرف ایرانی پیغام داده‌اند که «به توییت‌های ترامپ کار نداشته باشید».
​
🔹
این مقامات تأکید کرده‌اند اظهارات ترامپ در رسانه‌ها صرفاً مصرف رسانه‌ای و داخلی دارد و موضع او در پشت میز مذاکره کاملاً متفاوت است.
​
🔹
بنابراین گزارش، ترامپ گاه‌به‌گاه با توییت‌های تهدیدآمیز در تروث سوشال سعی در جوسازی و گرفتن ژست پیروزی دارد، اما آنچه در مذاکره واقعاً دنبال می‌شود با این لفاظی‌ها فاصله زیادی دارد.
​
🔹
در همین رابطه یک منبع آگاه به خبرنگار فارس گفت: موضع اولیه ترامپ در بیانیه موسوم به «پانزده‌بندی» اولیه، حداکثر مطالبات و آرزوهایی بود که حتی در جنگ هم نتوانسته بود به آن‌ها دست یابد، اما آنچه اکنون روی میز مذاکره قرار دارد کاملاً با آن مواضع اولیه متفاوت است.
​
🔹
به‌گفتهٔ این منابع، ترامپ متوجه شده است که ایران اهل باج دادن نیست و موضع ایران را درک کرده است. از این رو با واسطه پیغام می‌دهد که این اظهارات صرفاً برای مصرف رسانه‌ای داخلی است و نباید به آن توجه کرد.
​
🔸
گفتنی است یکی از ویژگی‌های ترامپ، استفاده هدفمند از رسانه در مدیریت و فشار سیاسی است؛ مسئله‌ای که مسئولان ما معمولاً در آن ضعف دارند یا نسبت به آن بی‌توجهند.
​
🔸
اما این لفاظی‌ها و ژست‌های افراطی که او در مصاحبه‌ها یا شبکه‌های اجتماعی خود مانند تروث سوشال انجام می‌دهد، عملاً به مرور اعتبارش را از بین برده و اثرگذاری واقعی خود را تا حد زیادی از دست داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/437511" target="_blank">📅 19:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437509">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71bd7a603.mp4?token=OySjp1YZDYi_lSGV88wbWBEgXSieaTyu8_yh3Rxa2Xsjw60go6KwducpjMbePNa8KY7qKlRdb_1Sd0RBveadKY3mhKRkZcaDq6O0L7pHJTsJqMg9spwz20Ly6f5Y9-u1eAkBjgEqgCZQNoFOdk_tJsunkPyydVHcc6rWI1NpVPfZ9RyR5yRsi089tJOQK_TUg2FGbZZ0CXJjmLXUkVjcIBCnpbUw1r3HW8SGwVuy2mkeE-r3deTmwVhm-xrJghCDrQhQh09ZiDipkArAaBnDAl71wJmVtHDYd5BNxCP304ug5qMBjXxvNUrt6OYL43GFe5KJ6k58HXo6OwinPZaMfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71bd7a603.mp4?token=OySjp1YZDYi_lSGV88wbWBEgXSieaTyu8_yh3Rxa2Xsjw60go6KwducpjMbePNa8KY7qKlRdb_1Sd0RBveadKY3mhKRkZcaDq6O0L7pHJTsJqMg9spwz20Ly6f5Y9-u1eAkBjgEqgCZQNoFOdk_tJsunkPyydVHcc6rWI1NpVPfZ9RyR5yRsi089tJOQK_TUg2FGbZZ0CXJjmLXUkVjcIBCnpbUw1r3HW8SGwVuy2mkeE-r3deTmwVhm-xrJghCDrQhQh09ZiDipkArAaBnDAl71wJmVtHDYd5BNxCP304ug5qMBjXxvNUrt6OYL43GFe5KJ6k58HXo6OwinPZaMfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار ۲ طلای دیگر در الجزایر توسط پسران پاراوزنه‌بردار ایران
🔹
علی‌اصغر ابارقی موفق به کسب طلا در دسته وزن ۹۷ کیلو شده و با ثبت رکورد ۶۵۳ کیلوگرم به مدال طلای مجموع دست یافت؛ مبین محمدی نیز در این دسته موفق به کسب مدال برنز شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/437509" target="_blank">📅 19:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437505">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تازه‌ترین اخبار از جزئیات مذاکره: آمریکا انعطاف نشان ندهد، مذاکره شکست می‌خورد
🔹
یک منبع آگاه و نزدیک به تیم مذاکره‌کننده: آمریکایی‌ها اگرچه از رویکردهای اولیه خود عقب‌نشینی کرده‌اند و بسیاری از مواضع ایران را پذیرفته‌اند اما همچنان ۳ موضوع اختلافی جدی پابرجاست که اگر حل نشوند مذاکره انجام نخواهد شد.
🔸
اول: موضوع هسته‌ای
ایران اعلام کرده که در این دوره وارد مذاکره درباره موضوع هسته‌ای نمی‌شود. تنها در صورتی که طرف مقابل شرایط اعتمادساز را اجرا کند، در دور بعد درباره مسائل هسته‌ای صحبت خواهد شد.
🔸
دوم: پول‌های بلوکه‌شده
پول‌‌های بلوکه‌شده باید واریز شود؛ شرط دوم و اساسی برای ورود ایران به مذاکره این است که پول‌های بلوکه‌شده ایران ابتدا واریز و آزاد شوند. بدون این اتفاق، اساساً وارد مذاکره نمی‌شویم.
🔸
سوم: کنترل ایران بر تنگۀ هرمز
اختلاف دیگر بر سر نحوه عبور کشتی‌ها در تنگۀ هرمز است. آمریکا تأکید دارد که تنگه باید کاملاً به شرایط پیشین بازگردد، اما ایران می‌گوید فقط خود را متعهد می‌کند که تعداد کشتی‌ها به وضعیت قبل بازگردد. معنای این حرف آن است که ایران با مدل ایرانی خود، تعداد کشتی‌های مجاز برای عبور را تعیین می‌کند و تنها به تعدادی که خود می‌پذیرد اجازه تردد می‌دهد. این بدان معناست که کشتی‌ها باید تحت مدیریت ایران و دقیقاً از مسیری که ایران تعیین می‌کند عبور کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/437505" target="_blank">📅 19:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437503">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ستادکل نیروهای مسلح و قرارگاه خاتم: برای فتح خرمشهرهای پیش رو آمادهٔ جانفشانی هستیم
🔹
نیروهای مسلح مقتدر جمهوری اسلامی ایران در پرتو توکل به خداوند متعال و با حمایت مردم غیور و همیشه در صحنه، بدون کوچکترین تردید برای فتح خرمشهرهای پیش رو با تمام توان در برابر دشمنان آمریکایی و صهیونیستی آمادهٔ جانفشانی هستند و تا پای جان از ایران، ایرانیان و نظام مقدس جمهوری اسلامی دفاع خواهند نمود.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/437503" target="_blank">📅 19:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437502">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f382a16c0a.mp4?token=RXdRnfTk_Nz5KznlwHuKn_7g6vg2M8nJAHdlP8vQSA0OWY234cE23TabO_2KIlJTZ0tQ5iNW3LCDJSAn-Jj4TZyT0Ck41Ab1VREn0bTVn_OwPbE7eb_JOz4LNOY6nunao2GHYqc_sLncBcH739wCNM2c0OErKOYzEYcaa0pZ1iok7k648SwU07z18PDHrJqmGvgskocTww9AP_idEaO39Cip5G0oTNKRQ1hAP5rRb_Az4301eu22vQUFHGOqni3jSeHxGsn6ftDBzm6yW3JMQR36ghKzsGaJ8hrq5ej98J4Ccy9roqN0KXK2lcJ77ynMLD_c83b8curpQBIaqDxIqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f382a16c0a.mp4?token=RXdRnfTk_Nz5KznlwHuKn_7g6vg2M8nJAHdlP8vQSA0OWY234cE23TabO_2KIlJTZ0tQ5iNW3LCDJSAn-Jj4TZyT0Ck41Ab1VREn0bTVn_OwPbE7eb_JOz4LNOY6nunao2GHYqc_sLncBcH739wCNM2c0OErKOYzEYcaa0pZ1iok7k648SwU07z18PDHrJqmGvgskocTww9AP_idEaO39Cip5G0oTNKRQ1hAP5rRb_Az4301eu22vQUFHGOqni3jSeHxGsn6ftDBzm6yW3JMQR36ghKzsGaJ8hrq5ej98J4Ccy9roqN0KXK2lcJ77ynMLD_c83b8curpQBIaqDxIqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آذربایجان شرفدی، پهلوی بی‌شرفدی این‌بار در میدان انقلاب تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/437502" target="_blank">📅 19:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437501">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
ترامپ به آکسیوس: شانس توافق یا از سرگیری جنگ با ایران ۵۰ درصد است.
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/437501" target="_blank">📅 19:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437500">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c39a99ab7.mp4?token=Zl2Dal5zz_2CEHDRjo9O9r1ov5eHbpQ6AatAXiozwc9YZ0NxaVP_6OqE2KlG-mHp8a4ztxSc2CIwPyUkFAJaGgu4DLtamUogHGW_JNqZIeGvqiDmq7WeMfrvMuoJw6I000W-mBfvWM5Q25iJf3gLdGgP6xj1_0C1qj_FBuysvV8B-quNN0g73JAN_DV3VMYVL4fDFlrkHRI30WXKYkbDAYs7ckdTOhTriXzeji6eVIlkgAPz8KUkzafqc16gz8Xj-3iU8o6XaIanCPYOPjwgrvnH3UJXaFTskbPndLdIpg0WYxGVibZMPQczyT0qDgyGuaPwsTuHelrTrmblFyQDZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c39a99ab7.mp4?token=Zl2Dal5zz_2CEHDRjo9O9r1ov5eHbpQ6AatAXiozwc9YZ0NxaVP_6OqE2KlG-mHp8a4ztxSc2CIwPyUkFAJaGgu4DLtamUogHGW_JNqZIeGvqiDmq7WeMfrvMuoJw6I000W-mBfvWM5Q25iJf3gLdGgP6xj1_0C1qj_FBuysvV8B-quNN0g73JAN_DV3VMYVL4fDFlrkHRI30WXKYkbDAYs7ckdTOhTriXzeji6eVIlkgAPz8KUkzafqc16gz8Xj-3iU8o6XaIanCPYOPjwgrvnH3UJXaFTskbPndLdIpg0WYxGVibZMPQczyT0qDgyGuaPwsTuHelrTrmblFyQDZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش سی‌ان‌ان از «ستون فقرات اقتصاد دیجیتال جهان» در تنگۀ هرمز
🔹
سی‌ان‌ان در گزارشی توجه‌ها را به چیزی جلب کرده که کمتر دیده می‌شود؛ شبکه‌ای از کابل‌های زیردریایی که شریان پنهان اقتصاد دیجیتال جهان محسوب می‌شوند.
🔹
در میان این مسیرها، دو نام بیش از بقیه…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/437500" target="_blank">📅 19:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437498">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMrKWPSSjkW1oNhRQxaWJC8kSVVoI84BP1L1ltsVNVFaZHGgcHCc_S9YC4J--etmautEfEWGBmhZJmb7Sk1n4N4NSLiD380RwWU3hVMfCgb4vAjOGF9jTqX7Jx_wB4wt6EcbEpDtxYIPTafKLfNwHBTgKU9_oVTt_Q2tCbOMYZ9XAPC5O3MEORxRyDVbhptQIBiTZ10wzNmFAY9g-Ys3SQeFrgKWeA1NO3NHwWeEZ0V5PTq38KTkCcVy1M_heSa1DiCZaihbU90SuA2Oz1o9zmT_CsuRCaKnriXyd_4scoy56HHwmuMGtFie3cd9CbXLMoOQ-F5JAE3qpd3tPsksSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامهٔ هنجارشکنی‌ها در موزه هنرهای معاصر
🔹
انتشار ویدیویی از تک‌خوانی زنان در رویدادی در موزه هنرهای معاصر تهران که یکی از مکان‌های رسمی وزارت ارشاد است، خبرساز شده است.
🔸
پیش‌از این نیز فیلم «تهران کنارت» با نمایش علنی رقص زنان و پخش صدای آنان، گامی را برای قبح‌زدایی برداشته بود.
🔹
از منظر جامعه‌شناسی، این اقدامات طبق نظریه «پنجره اورتون» انجام می‌شود.
🔹
در این نظریه، جریان‌های ساختار‌شکن رفتارهای ممنوع و تابو را ابتدا به بهانه آزادیِ هنر به سطح «رادیکال»، سپس «قابل‌تحمل» و در نهایت به یک امر «عادی» تبدیل می‌کنند.
🔹
برخی معتقدند این رویدادها با اتفاقات سطح جامعه تفاوتی نداشته و برخورد با آن‌ها حساسیت ایجاد می‌کند.
🔹
اما دیگر کارشناسان می‌گویند «قیاس ناهنجاری‌های پراکنده خیابانی با اقدامات ساختاریافته در نهادهای دولتی، یک سفسطه آشکار برای خلع سلاح حاکمیت است، رویدادها باید فرهنگ ساز باشند نه مرعوب اتفاقات خیابان.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/437498" target="_blank">📅 18:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437497">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poEm3GUWwom1WI3MHnoO_97jkKuoMXqcmLnmVyvmT9-Kox7UcoOsV030tFrqvNZdhujg1fNM-X5mKJOhlm0gkCzeINkuGmtQ96vlL5tg-WcpDuWImyQTzaRshaqs519kHMU7iCQw126bMcwvC6JMagOhOoArqUtCS3OojJUpHU6-heLcpjxiQOdBQnrqGcnwr2SCEllhr743VPJRJM8UcB4gQ0zXFbsTxeB1Atqr0KaCXeDjK4mu1C2uM1sP0bvUi-9VNGtXxEEU0gkXpmYZyReZyeMQBjLB8WvHiVYt4-tW5BCp5oVd_8UxPcwAyM-knpWVwYLEi_WZo8nRQq_ivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف لاشهٔ یک پرتابه در چهارمحال‌وبختیاری
🔹
محیط‌بانان منطقهٔ حفاظت‌شدهٔ قیصری شهرستان کوهرنگ چهارمحال‌وبختیاری لاشهٔ یک پرتابه در ارتفاعات قیصری را کشف کردند.
@Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/437497" target="_blank">📅 18:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437493">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در بندرعباس به‌مدت ۳ روز
🔹
سپاه هرمزگان: عملیات خنثی‌سازی مهمات عمل‌نکردۀ جنگ رمضان از فردا تا سه‌شنبه در حومهٔ بندرعباس انجام می‌شود؛ مردم نگران صدای ناشی از این انفجارها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/437493" target="_blank">📅 18:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437492">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WduLIStrIju6YxZgBGnCYiEo3kHHtukmD7BcNWZxpv38BgU7QZIzC4I7Qo87CdPOPB2I8l6TAgC3rEcYspBfWfzsPA3A0s9F1xbMifydHjVDjdzRS06utf0-8UjYB2dqZ0NW_qG3Ay9kmy5xVh2eSCIw7uXNpwlMv98vHMGfCH22dgcZw-FrspVqKHOz41YeTR_nAtWvfluH59ZAPQEDmxNHOwYwyYkaKmbb_N-xKliabDeyFxc5XF9QbgrnGQ5GVvl6SJWG1toSHraAowZZhKpEXDxk4UPNQoXaVXRKxu-j-YFwUDbeEZgrDfUbqfZ3RpDRQ4GneulV19QBTkslgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۱۵ پرواز روزانۀ خلیج فارس هنوز به آسمان برنگشته است
🔹
بررسی شبکۀ الجزیره از داده‌های پروازی ۷ شرکت بزرگ هواپیمایی عربی حاشیه خلیج فارس نشان می‌دهد این شرکت‌ها روز گذشته تنها ۱۶۸۵ پرواز انجام داده‌اند؛ این در مقایسه با آمار حدود  ۲۳۰۰ پرواز روزانه پیش از جنگ علیه ایران، کاهش ۶۱۵ عددی را نشان می‌دهد.
🔹
قطعه قطعه شدن مسیرهای هوایی خلیج فارس، افزایش زمان سفر، لغو پروازها و کاهش تعداد مسافران از پیامدهای این بحران است.
@Farsns
-
Link</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/437492" target="_blank">📅 18:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437491">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-44.pdf</div>
  <div class="tg-doc-extra">5.9 MB</div>
</div>
<a href="https://t.me/farsna/437491" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-43.pdf</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/437491" target="_blank">📅 18:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437490">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8gv0NkzrR7cMfY8cn87hV-ifBiEROxvp1zTnklJIeJbW7jm3Tgp8lDVeHu_I9DrpAjDU6qZ0j3sjCRzPXz_1KlJllDpOsGM2pcZDLXr30QAu_TtOSqirZnAKiFTd1JzTyyY0X9cYcHDtxeO4-ASYLlVAD0_IJXyH8hY1GCpK496TvOUTZg914vWcjmnRp5gwMdQc2pLQZqkMnZakVOGCPwBin3B4FkHt4jHAHtVdcchJTYOjHndan31EAA-YLE-0GixMX0-jOH_OSFgatFexcUhMuiKKT4OM3Puxl7_rUmnpO5o0uUIqJrzHO0t6X-M-90EvCBRwZeN9wllnXA8gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله یمن: مسلمانان نباید از سلاح تحریم کالاهای دشمن غافل شوند
🔹
زمانی که ملت‌های ما برای نیاز ضروری خود به غذا به دشمنان متکی شوند، به برگ فشاری در دست دشمن تبدیل می‌شوند.
🔹
آمریکا و اسرائیل به اهمیت سلاح تحریم پی برده‌اند و آن را در میدان نبرد علیه امت ما به‌شدت به کار می‌گیرند.
🔹
دشمنان از فشارهای اقتصادی و تحریم علیه ایران، عراق، لیبی، سوریه، یمن، کوبا و بسیاری از کشورهای جهان استفاده کرده و می‌کنند.
🔹
بخشی از راه‌حل‌های اساسی برای وضعیت معیشتی و اقتصادی، حرکت به سمت خودکفایی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/437490" target="_blank">📅 18:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437487">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iU08ZahGt7NL4Fw_2dBN7X7MYFhuge6MVoDUHsFgTrvQPXks-p_CFkPpec13JaLu2hSSoAGwtdHdubxUavW0SHN3axnrJeNVbEMFvm-mu5ildWW1PA4ApNO8DsoRm0XbI6KHqoYlzG-q17dPa01DqeHC3amZymYtcEsB7Te3BDTUTYkCpO8We0aFf98FE58s-1sAGoD5DQlLHdnhl-fqXbQgWTHNyMW1D613uKzvQD48f7wi8ikdT-Vr6m59auGXL8gUDbwOasGnCPQxvUOsw-xCq9Uf45jeSlAZepKuaBPC7HyMvj_3yQqRu25oqtxOdI75BML8mrxNBEBiT3oY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7ySf1a0W9fN-oloEZOxTRNeARG9RWQT4wj-OqvvqWeotT-EcIgVsmaf2pmej3qLlQXy2oPsymN6asOd8FJarNntwKfzmzImaj6YY4o_qY4okcIBQHaK4s0mnmBwAHjxke5l9F1sgPQEE3aIouTmKS9J6t0Bp0gBMTvDTdnpzvwIleCvfYVgXUStvgT-9RJJU4tV2-7rUj3HIYstFlL4oRMPDoptuWM8ygKaiOa5_5Lfk5lkvAVecM_dmk0gvmYc-k9qkl-YiggSWSGBPuQIDuHKFCd7Y4RmP3F1u2JHo68W9JJY5368igElCxXigiASgnhHSS4K-6qbxCQMmZIPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plHH86HIfKOznULaww3tXOGO9CDVrqy2UD_7jSmX4WXnzxXnH3si2EDG_bGHwy_V2JeiYBiX1_mIn3dP56o71TRMy9ump96qzVPlzvH_Vs-wK0zzKpzZ8xiC3nX9LSRuxr0kC0Sl2ii0iQjfoO2vUq0MxifGETb_CM1t1FhMi1uKwz3hxkV6uRowPxmu0s3jclNhj8e_xKtntoYXRRhS6sDc7Le9bS_RBtr86mmnsbjahXHlkApmS_Tt_BWjo8RYiariA0mI7DuIGBNzs4NlTY1VY95UiWdJqUIw4rCLEuAuuN9rl2xvSxAZ8BNlnpvt9Brw6K_tQh5MYHALPsHMiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حرم امام حسین(ع) در آستانهٔ شهادت امام باقر(ع) سیاه‌پوش شد  @Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/437487" target="_blank">📅 18:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437486">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">۳ عملیات حزب‌الله لبنان از ظهر امروز
🔹
حزب‌الله: ۲ سکوی گنبد آهنین در پادگان رامیم را با پهپاد مورد اصابت قطعی و یک خودروی مهندسی ارتش اسرائیل نیز در شهر بنت جبیل هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/437486" target="_blank">📅 18:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437485">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp2wXsXzgGudFZSYPVC3JkBVfjYN-t7SKJ9U2XtCf2SF5lnG_zstgD7eFMjdPY4VdSd6EdG1MXKuiQzXHq-2eFutBkRpXdQAZS7Mm0AsAiSR5QfgIAkNLFwKulLOyAhe69sPt7l769z-hnPFXPgjFgrZTwO7EZ7y1HpYqGX-7WpuJ8qPoWSNLEslOZNqCEECQiQPSqAuMg2URpeUidxKalW2s_scqjgxU4PrWDU63N6LCTg2E13YbIPWWZ45cYam-9U6rBazRE7KoiDSm6Iq4x1zZcPoaey3q9_j-3pcEXi7Ml0m17CG63Dv2K2XsWbehQNSZYmXYTRwz7qP3mpmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر ایرانی ۲ طلا در پاراوزنه‌برداری ضرب کرد
🔹
در سومین روز از رقابت‌های آزاد پاراوزنه‌برداری جوانان الجزایر، عطیه سادات حسینی ملی‌پوش پاراوزنه‌برداری کشورمان در دستهٔ ۶۱ کیلوگرم با کسب مدال طلای این وزن و با ثبت رکورد ۱۹۱ کیلوگرم موفق به کسب مدال طلای مجموع شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/437485" target="_blank">📅 18:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437484">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jbh4VjZKIXJVMYcgtLMZm6ZYl7R-N4x6dLXZh1QCAscsj_yOTbP6qbFfzU_y3ty2oaWVnd2eLwjvu88iCFQnzLfbcw9Z-GEJCCIA5SBHJcWHq8z_h1H69MHFevSEBGOVLT5ykCYeNcpmnTh_A5Kz46BJNelhbllfA7nBUbmHYj9VCGIiROKrNV4lP2M0juIHKozEN1z_nuX26OIr1Mq6jwmtD0MxC-llCo17ZUsMlKzRsO68dtPNWG4Af3qrK2Y5rsb9kWYFbtsn-z1rJPJMjYPhB4CcrQmZRncX7sMo6QQCIf0egM5_-8cBIxhKGcwq4U_oK6vfVB3UsPTBoopuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فائو: تنگهٔ هرمز بسته بماند، جهان با یک بحران غذایی مواجه خواهد شد
🔹
سازمان کشاورزی ملل متحد: ادامه بسته‌ماندن تنگهٔ هرمز آغاز یک شوک ساختاری در نظام غذایی جهان است و آثار این شوک طی بازهٔ زمانی ۶ تا ۱۲ ماه آینده ظاهر خواهد شد، به‌طوری‌که یک خانواده ۴ نفره در اروپا برای خرید یک قرص نان باید پول یک وعدهٔ غذا را بدهد.
🔹
افزایش قیمت انرژی، قیمت گندم و برنج را نیز بالا برده است.
🔹
کارشناسان پیش‌بینی می‌کنند در ۱۲ ماه آینده قیمت نان در جهان ۳۵ تا ۴۵ درصد افزایش یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/437484" target="_blank">📅 17:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437483">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6f158d4c.mp4?token=lPLv66iMdLujPPl_H9kSWEqH4XgRk1hCrYBO_RBTj8qsYs9g3vVNA3b0ViCm6v0w2duaDzJsyLisLZhni4ovGSVW8OIwfHs3KVeb4VYsMuwQmcY5BazZMFIwQg_JNKDXjFUImtom5y4Ud5CtF5hoXYF_Fyq3j4vCWhULnYfNbtM8sbIULNN6EmsQEjP97YLFbsdTFdmgbUMH3FPyrMu9DStqWtl78_ouMS__ujaiVQ6R-7f0hbf0QmKoosk0k-XPnITBFA0jJHKV4oQjqkDinHOffiPaI07RfeENnCjIv-yKlcTHvwhV5dfuMSghkqPL7P3nc404Al1rOAxkwYiqoo3a9_Otgnz9ewTvfQHU65ybcdMLjdsg0iNjjC-YKyVxx8pDee19A0luCVfmw0NxGpkkPNxT_6Tgj_2Vx3cJY7Oe5u75ZJVfz7WnTz_-ntGgRrVW1bdoROHSat-IaPFGEednafTj85wSmF4gx_a4nrfgb08DDI54ZUMQoqfBrd9KdaWn29Fzh90cab9VC5yyFW3EyfHcDjM9_GyqSCa9utE9QNget4q8vk-T1_NS-PGV-ZNcm8ROQXbI6Ems4BSg1pkl9-sUkh5GzUD86P83K4mUQMT3dLWH9ccGuutJ1mRK4wnGpQeoSnjfeqkvJQ4dmBLAwYkQlyREPRn-H5QJ9J0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6f158d4c.mp4?token=lPLv66iMdLujPPl_H9kSWEqH4XgRk1hCrYBO_RBTj8qsYs9g3vVNA3b0ViCm6v0w2duaDzJsyLisLZhni4ovGSVW8OIwfHs3KVeb4VYsMuwQmcY5BazZMFIwQg_JNKDXjFUImtom5y4Ud5CtF5hoXYF_Fyq3j4vCWhULnYfNbtM8sbIULNN6EmsQEjP97YLFbsdTFdmgbUMH3FPyrMu9DStqWtl78_ouMS__ujaiVQ6R-7f0hbf0QmKoosk0k-XPnITBFA0jJHKV4oQjqkDinHOffiPaI07RfeENnCjIv-yKlcTHvwhV5dfuMSghkqPL7P3nc404Al1rOAxkwYiqoo3a9_Otgnz9ewTvfQHU65ybcdMLjdsg0iNjjC-YKyVxx8pDee19A0luCVfmw0NxGpkkPNxT_6Tgj_2Vx3cJY7Oe5u75ZJVfz7WnTz_-ntGgRrVW1bdoROHSat-IaPFGEednafTj85wSmF4gx_a4nrfgb08DDI54ZUMQoqfBrd9KdaWn29Fzh90cab9VC5yyFW3EyfHcDjM9_GyqSCa9utE9QNget4q8vk-T1_NS-PGV-ZNcm8ROQXbI6Ems4BSg1pkl9-sUkh5GzUD86P83K4mUQMT3dLWH9ccGuutJ1mRK4wnGpQeoSnjfeqkvJQ4dmBLAwYkQlyREPRn-H5QJ9J0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریاچهٔ ارومیه با ترک‌های عمیقش خداحافظی کرد  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/437483" target="_blank">📅 17:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437482">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🎥
تشییع پیکر مطهر شهید جنگ رمضان در بروجرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/437482" target="_blank">📅 17:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437481">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431f4e1b52.mp4?token=JRoPPuWp3COEG45kgR0F7-7YeOBEQw43ftSvWq4Cu73eHTNmiAoWRZW0uPXJApsOfPvA6OjVo8yefC9JrvtF6EKvYfcg-2X9OAEw4L53vPQCE8baMM_uRYo40j0-myBKxUc7JMorNwB1uh3dH6QfvmTrsN1Jv2eS2sSDyjV62hCGoe0jE5878BQXMToKpNTAv6TK1X1vaYm7uww944TxcinnG7LfCguAkseKdnWKzHyZnOvolgkl3AITSGqY1HPLlc6GQvym--NfLXIqdijtIjmnohauOORwGEhnnzDYzcD6R-e2t9EXh8wMvM-04-4q3DYWi0S1wzytRvlPMd_S4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431f4e1b52.mp4?token=JRoPPuWp3COEG45kgR0F7-7YeOBEQw43ftSvWq4Cu73eHTNmiAoWRZW0uPXJApsOfPvA6OjVo8yefC9JrvtF6EKvYfcg-2X9OAEw4L53vPQCE8baMM_uRYo40j0-myBKxUc7JMorNwB1uh3dH6QfvmTrsN1Jv2eS2sSDyjV62hCGoe0jE5878BQXMToKpNTAv6TK1X1vaYm7uww944TxcinnG7LfCguAkseKdnWKzHyZnOvolgkl3AITSGqY1HPLlc6GQvym--NfLXIqdijtIjmnohauOORwGEhnnzDYzcD6R-e2t9EXh8wMvM-04-4q3DYWi0S1wzytRvlPMd_S4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: در این مرحله دربارهٔ موضوع هسته‌ای مذاکره‌ای نمی‌کنیم
🔹
اینکه در مراحل بعدی در مورد موضوع هسته‌ای یا سایر موضوعات بحث کنیم، از این مرحله جداست و تمرکز ما در این مرحله بر اتمام جنگ است.
🔹
تحریم‌ها قطعاً جزو موضوعات مذاکره است اما با توجه…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/437481" target="_blank">📅 17:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437475">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTUjxCDTrW1uY54_88u2gNIagR-LWMU8FktLh21zK3bqXgeXfnFCrAVJrKcbXIgWVxglVK8NUco910CoYf8SDrIVqPWGJXn0-5X5wHvCYdDiYzf63g_xCZgpTAUoQiU1eu4Se_ClBU3soODyO4tNqwVWkJc1xXhasKdsZSgZFZg0Mf1iG9SUfbGjc2Db8Jf87TVHhn3OeiITBvw0YY2UZSrdzmRkz4OBMmpxOzoZX7bCg2GBpn-Mkz1HMzf_L07CfO0Nc23Rs_m8RoaL0WD5br5Cgz1ExP_-tGYeGvxNvOIp3BBaX6VI6kJmgn4Wj0dq421QM_Eynoz9q9Ym8nH6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShKtnzM9KjygaPKXELDJptssue_bfu1zTWJdrs7mjXu-kKUPk8Yehm3fZVy2Y8YKiClkRAS9uHGysuWfqi_ywBa_os3MNu1Vi0yEoGCy-aHQtB1Pde2bGi4xY0wWvMfpZy3OacvjtWXq1tYEsWsV5m_WMSoRI8jwIc2HzvxAsRuDVq3N-Z5DsA9wEIhnNsAPp8Qc8BQhXCLz-h8qOKRm0mNxxAkVAQo-IaLdd_7hVU5qhtDMgtOICg6QiLzhg-OQHunWDnAadK7o2dhl5umhntTiVprh4H6mg437F1JzPmn_z1F_x7ZU9lBl2W9bjVWMR8bi74dR1f1HrRKk5bIGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBJAULocxWtC5cVJ61uGCQdSqYyKpx4AZKh2fnMzFSwOm3RrG2yxAjRt1rkRSlywV1Ec5NsFwW1XNz2PfGghwDlr_nlD4RIcEPF20VeEExwAjQncBZj_JgFmuUcuCztGjOopzGE6HFa6vyjMgKD1et_ZPGl4LRRXxbV8MtEd4NkgaMxiSuW_UlLRUQdg2ze2YC71iYu6frdI-rJMyGqd2zYie6J8iatuPacCM_ip8GDf_x_udaO59-t_2lVtYoclv5APY_fFN550xYfvyNqBFupAeDy1OhufXEJX5lh8OpOf3M-4Bmy21LQ9lPJQCwYaUpxMbHQqIegh2QlPZVYTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYckG2Zt7Uk5BRUJgDA2ructdq0CVwOvsdQdmlVyMULtR9yVzH0aRfcDDx-ClTqf6E053yzOHlOhDqBtZjrKFa7ahomDLlvz2x2biIK8Fcto9t-35Enu7v7-pt7wDf8oCINggXXnKDbppVNzwfNeumb6cKj0L88DIlusYBRfZAIdP5jMaVjc3dA0icHx-h2IoryEmenAc6N-eaYv-cM799GQHa1zVricOf1NLMjQzcCPxL5U-CSUOhLGYMLRLp2b_IOMoTCuhM5Qajz0WRVE0OGkQDfGU7eR7yHNMDOG0qNxIXF7jD1yd3Ao-NMWvNh7_ywh-lVk4YfrU_RuXW47hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6ml9v-Q-TC1RCp-sOZJQ_5jMwx5W2frlnOZXc8HacGqykcize5apBJVYAvrsYGvYZP7cTFUwx3vDbbBD8nCgoyxGoDJze04rRIg2IisGw_qbrjK49tCsNkpviuzNz0KhNx1EAWte4mqI4bMzdrpdmFC1bTEAMxwEgio738VAbSu-LtyTyvEda78W3X2EQItHZeiQ-gzG93AMxtJHrnORow4CRJ8WrazBuLwhPFDwO1r8BLCedR9LubfoRpHhq5-AgSEKY6JMM9PHZmv0hsYJbn1MHFjk-GscK-kkTQtIKiAzhK-IiKE7Xc9OgJUtc4KUjvnOXHX34gXPQWOgtNhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4TQ8-eq560O14Y-C_uD3Ef-zJvw5x9331eYhiC6PLwBD6muM91Do2YFl_B67RJkNDs-ZRqGylUOYXPd7AVySTyAh8f0xKFgKfBUFea1QcTz-Z9Y5o4em7nHYojBd3bTlT7gJn4CxFSLaX-gLAH80sWxO480KANfextLIJU1o6atAoRc_rcSV5hdbNeu16YaPCQ2gEAkkKM8fcPTQXtvfdsoePH3F2J0A7dtIEEBsRExErYAphBS9PvDLBIQ7HFs7b3XVwfXALnJd09r5ggVYLd42y2CQwE29pVfVRN6--alb-tAf5W143Dvu4jm8z1gS3Xp9JMqOGio-xHPxQT0XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
محفل القائد المعظم، یادبود رهبر شهید امام خامنه‌ای در میدان التحریر بغداد با حضور میزبانان برنامه محفل
@Farsna</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/437475" target="_blank">📅 17:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437474">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b2f025d5.mp4?token=PB2qA1tT36gWR_mxtiwbCwzj0w1ulZLEwEZs-RaHM0vooab2oGw7jVxtTsGOicIgsFDRI6zYhzNByZ_tNh4Gb4PK0c9z43ORjZ8jVcALFVb9yHpv56iytlx4kSNIdohrnqZantkuktzy06VL0JoZZbX4vf8REe_oQPrQ-2CZ6TbSFOAcrUrUZbxQrxVQk4uqvDXHL-OXUNrY0hQhVkYEyvcF7pAAoQCKKSFSj-o11K5gPJQNBpI19Pgdb_A935UzKTdJa_7uHo8s-bGBGsYT2ROCDyb_YBYMyDQUcOnfE8C9RRWAozrBHt_RGua0Tksd5i0xiIdnwlLPd710VmrZ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b2f025d5.mp4?token=PB2qA1tT36gWR_mxtiwbCwzj0w1ulZLEwEZs-RaHM0vooab2oGw7jVxtTsGOicIgsFDRI6zYhzNByZ_tNh4Gb4PK0c9z43ORjZ8jVcALFVb9yHpv56iytlx4kSNIdohrnqZantkuktzy06VL0JoZZbX4vf8REe_oQPrQ-2CZ6TbSFOAcrUrUZbxQrxVQk4uqvDXHL-OXUNrY0hQhVkYEyvcF7pAAoQCKKSFSj-o11K5gPJQNBpI19Pgdb_A935UzKTdJa_7uHo8s-bGBGsYT2ROCDyb_YBYMyDQUcOnfE8C9RRWAozrBHt_RGua0Tksd5i0xiIdnwlLPd710VmrZ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مسئلهٔ تنگهٔ هرمز به آمریکا هیچ ربطی ندارد
🔹
در مورد تنگه بین ما و عمان باید سازوکاری تعریف شود و در این مورد چند نوبت جلساتی با طرف عمانی داشته‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/437474" target="_blank">📅 17:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437473">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/717ef30b5c.mp4?token=Ww7RZKE1guPi_tQvIV6IGlRyGrI_qWwWSw1yVl1uFwEqax2bod4CuxBDcd1PyOkk4V_RCy0q9PE9pfy4alJiHS1MxCik7sx_8adbR6skovfWlVgC3xQm_FaawCCtXnVIsKqDsy5eLjbKGjUZXre2DmI4nf7Ga1JeIQQmu6RYAuPGMmh5H1tLE8redv6N8ElT5GrkF_LOO0tLdaBl7rshfo-g5jC3Y7MMsEHv8tI7Alv7Deo3COyTUiVAGUu806DHGr70MHuTQFz-gkVZ7StJFr4lxQMzlGAnerZyUhAh2Zj12mPcvTcgDPldjXc3DI2HIfSaeunn9blSmBf4d5fq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/717ef30b5c.mp4?token=Ww7RZKE1guPi_tQvIV6IGlRyGrI_qWwWSw1yVl1uFwEqax2bod4CuxBDcd1PyOkk4V_RCy0q9PE9pfy4alJiHS1MxCik7sx_8adbR6skovfWlVgC3xQm_FaawCCtXnVIsKqDsy5eLjbKGjUZXre2DmI4nf7Ga1JeIQQmu6RYAuPGMmh5H1tLE8redv6N8ElT5GrkF_LOO0tLdaBl7rshfo-g5jC3Y7MMsEHv8tI7Alv7Deo3COyTUiVAGUu806DHGr70MHuTQFz-gkVZ7StJFr4lxQMzlGAnerZyUhAh2Zj12mPcvTcgDPldjXc3DI2HIfSaeunn9blSmBf4d5fq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: بنای ما بر این بوده که تفاهم‌نامه‌ای ۱۴بندی تدوین کنیم و در آن مهم‌ترین موضوعاتی که لازمهٔ خاتمه جنگ است و مواردی که برای ما اساسی است گنجانده شود
🔹
ما در مرحلهٔ نهایی‌سازی این یادداشت تفاهم هستیم.  موضوعات اساسی این تفاهم‌نامه چیست؟…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/437473" target="_blank">📅 17:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437472">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32041f34fe.mp4?token=q65IdA3IKgaz-vNOFDpe-IZRFyP2qukB239n5JrsTzYgsKQug2GOhqcx6yLwopETD05-5NS5oWIWvTU0ZYxPs6sMd22CToKsOB2npSFj-pH00sPG7reICLXXPmySxopzcqFL_E0dfedLGLkYc-MB7DHY7YPkpjgKF2hwwTGKIRgtSK6hAI1bFYNbK0iIQtsVhxkJeyU1rIJKgXIK2eHSwZ6fSsPzIzZnaHRjOCZmeQhRX57caUvCJ5dnS0U0Y9N9q3_QeRCyQl7MLV7GVrBwzdYXAH6GLB85tHxvplxZ7anC1o3KuqINVVkSWF-YdoaKQFK0ff8A-w6PR_vAGwPnBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32041f34fe.mp4?token=q65IdA3IKgaz-vNOFDpe-IZRFyP2qukB239n5JrsTzYgsKQug2GOhqcx6yLwopETD05-5NS5oWIWvTU0ZYxPs6sMd22CToKsOB2npSFj-pH00sPG7reICLXXPmySxopzcqFL_E0dfedLGLkYc-MB7DHY7YPkpjgKF2hwwTGKIRgtSK6hAI1bFYNbK0iIQtsVhxkJeyU1rIJKgXIK2eHSwZ6fSsPzIzZnaHRjOCZmeQhRX57caUvCJ5dnS0U0Y9N9q3_QeRCyQl7MLV7GVrBwzdYXAH6GLB85tHxvplxZ7anC1o3KuqINVVkSWF-YdoaKQFK0ff8A-w6PR_vAGwPnBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما تجربهٔ ضدونقیض‌گویی طرف آمریکایی را داریم و نمی‌توانیم کاملا مطمئن باشیم که رویکرد آن‌ها تغییر نمی‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/437472" target="_blank">📅 17:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437465">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riOKBXP_PuenD27xlA3C_2PE4VDhldHwA_QA_ZHJ12h_WQ5JJ_3BRpRc_Fo4lOE-B7bN-30JbJ1esXMecSsS4JpnuDxD64vuzBV8Y28EdzXBV6TlP2jk3l6gHiJFNbm7HACvjKDlrKkAXZVZkqYpkCgYrgwenwHtGzuOzgwZreIe97DsG_69J0My0-kK0v2AizdUWju5nAJgB2HFZ91zhaNpW_zCM7f_sCQQg80u9VmWHSk7Mid833Yr1C9Zcb_80ENMW1ALf-GbT5-RzCWimaZnWjgLFLZORcs6aLjQazirtDWtUNqrBaO3XSkLJIZo5P4Zl_y4Pn8qytz6qMPYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcmyvieL3pzpFOs3v0w4Rg2r03S0MaJm71v1IiWWHTM5Fz1QF1nh7cHB_oVxQs3NuiFlMsEsp4cK-5FTqt34OV8gPPmscAUdSWnswp2UEyp2zH6xQFsCaUETi5vEcGg8Lk0iCfgjTYBQN9NVd0HYM7HapT2_MqErggtbbWOISrg6etuGMKpJbF5cJAAFu4Csbl5jZ1SCILPbV_kiXHEEVWwrb6ccN6BSmuP688razXmbkC0BW9jaienat6AF1A6D2P4EvOT2oDmEu5P6h6K6_BB_5XL9BUhKOikHNSBE810aWPxyOdCjnOhagEHj6nQnoLrgBbZ0z6cBgs9zJuRwuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWsuzA-ZEqom1RDjNlXMa7tN86zq1PldRpU7fvmWvAdVEVMknqIp_-VHONcSkkd1k550QJtT5gBoxGCi3rKOMr-IUrfyGhT8RZNYEFyPRDqEEJgEbfaeLo4H9xbRpBVSeou6QLXiwGZNGz-eYdhUpV5ixt2eVChookHXr5Qwo0J_YSOlq-T9MVgTYNMZD7KfjGj-qcnS-bR40t9RwdUUYSU6DKv71qBm8-TboSWvYyXjMxSwW4OFl8xG-yD3S6TB0FFbMh6Wupa76y7kLSYLXEq6xrez5Faz12dsyo0__AP4aVnn3c3dFEMQl92i46sLQmQS_xhTkKnvoGcMPJwndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xq43-t4DB5xfrNRBDND0lTdxO8uKQlr5EV-AMGyM7H5NX-iZMZSIqmU7836QjmIx8Ky5BDFLOILAgSH9RdFxDb8fVS_XEqc1RnNbBX7nEyvNMAnNeg-bouNLwFQf3wVnsw6XoQLTi9aTHpOcFWFmd8eJj3Dvz3usTMm4zQ0umyFijYFyeqgpFp-hG0NfE86iqiYocBwrFHVgy4YyWwwfdcFAWnfYNVLBM6HSSEttKzepvAunQkb3l1d4cYD71GzZnUWqMhnZ9yw-IKq0p8fFMH1FJ-zQ5CCEVlhSjz5eIcAcCLYRrCRFBU2tE2DRxO0M4iJ5uIvuRbtU5TcX-N_76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-PDZ3hn9UB0P2r-_J_2UbZBtiN14dMiHK_giHaqQpLgzFa3Y-m4cg67ayE_nPhzXwHQGnJ3wvob2BPLwCW8c0Kd-KDUaGx8MqK9stIw3kIXxhLFWxLBc5qlU3zKiAV5CcKyUil9lsaSHwOczrZTx-0yLvA8-2hqZ-mfXoBQYeOgucEWlCZkkKZjqCIwNL23Kc7kMfZUhGMIG1e7hRnKsvQx407RWG9r7cU85UHdFO23fXNUwg6kR51RReSo4SfJ0wx-ECPAK-ydOd9dAqSDbRiYjp4E_kASBp96dqIlf9lse6zoNMogTiIN7lWnvOf8WCI0Gb09PVR_-yQcRY5UWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mo5RT8TsSCjwIESkAlrHt0WrYCuy1flX00StbYy4OeFrOfQjqO74l5eY7i5BEAyIW0pCWfe8879nwZIM2Z6L8vvXZ9llDiklPpPx5s8Xg_DtZTlpxDvhcByAxk_F8u4obDsLizFwjiqPzdnFaDQuYt3o66CKPZUsmFwZDeIVC_WEk1C-VDkAIpbIN7WaOVTlg_PgYyvg1rWAigOJCjcweZ5SSGrnXRzs7qQo67qMa3r_BxyWjRn9BF7cuqySIq6SwAbZxWSjSsw0euSJTXmk2EBQfaHNVX3uZQnSDzblDVkABudex1ZdACfwRjqLpXKD1_7GXGKWWF0LAVjf-EP51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyBEuTYP8QX78aX-4nxzVAfQ0xI_KcuB1yppEn3piIWCm7rcCSJFuqCpgP5ZYT2t3Oq5YYsqhqu3Lz_caaYc-Mx_zWHKVAms2BZitOKtt3vvrqu4E-oStE-v0eYjjpdm37M9tqz9GhTGvfZejjCy2HLUP9WLvexuJ_s6xigxRMh7BS94wIBlgOLlgcenazc52IygTLoI0TPh5l3hArHU3G_je9iC9_1EC0nu5vpbFMcahtuUGVWVZUOMu75MmYugbkkNtF5_8PNLfHMlw-KSuA_yNUUpo-A-2UKE5Fu95b_w73kNrolbEpmlg_FGWkgJ2zc951vNtscfVkrDWjZBfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌عاصم منیر تهران را ترک کرد
🔹
فرمانده ارتش پاکستان که عصر دیروز برای دیدار و گفت‌وگو با مقامات ایرانی به ایران سفر کرد بعدازظهر امروز تهران را ترک کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/437465" target="_blank">📅 17:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437464">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni1hsUTc588jTGuVXBKeNJg5Y3osPqs5BEprZ2GLkzJkMR2OfuxPMOACeF0ZFlt_rirerQF_u-7DeRw_KnI3JJp-e-4FXBNY8NwxOyTaI5_tRNIliyoGZK21rHlK-V2aoTAoAO9FohKG88jC2M4-ZgJ9j1ElcKXZfUFIZRxDz0JL48Y5B0cwg-WFUI1PU_AfcBrgq2W3timCq14DtGA8haFhqf-3Dr54OngFAhAAFq5G00nmtsT_L2mcGOKd2cE7ZiMqnAhyBLSsYF3_q_zpEStYz6SomqNJ37IYg5MVaIah06fGURv6k6fczSjs8GOpIrTI-yzaY-WEQScWvc37wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوران جدید آغاز شده و پویش جان‌فدا وارد فضای عملیاتی می‌شود
🔹
شرکت در پویش جان‌فدا با یک پیامک ساده برگزار شد. همه تقریبا شرکت کردیم و جز یک کار نمادین وجه دیگری نداشت.
🔹
حالا پویش جان‌فدا وارد ابعاد تخصصی می‌شود و قرار است به صورت گسترده آموزش‌های مختلفی داده شود.
🔹
وارد لینک زیر بشوید و اطلاعات خود را تکمیل کنید چون ظرفیت این اتفاق در مراحل اول محدود است و باتوجه به شرایط مشخص نیست تا که چه زمانی آموزش‌ها ادامه پیدا کند.
🔹
آموزش‌ها مربوط به فضای جدید جنگ، مسائل درمانی و در مجموعه توانمند سازی مردم و استفاده از توانمندی های جمعی در آینده جنگ است.
🔹
همین الان عدد ۲ را به ۳۰۰۰۱۱۵۵ ارسال نمایید و وارد فاز عملیاتی جان‌فدا بشوید.
@Farsna</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/437464" target="_blank">📅 17:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437463">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a911ceb49.mp4?token=F5gcbuk45H33fglYnSEjNOgpOSrrKUHMPRRUJdGQJFqyZXxsLLHUjU3DIapBVL9DKFk0dyyHqlRQEQSEaEbeZBXyIuDbNa_ABfw55qwj_1XXWEcEZcZc6KuBMZRWE9oREyNaj99QKKuZ2wnLQqp1BQUECIG7Dr4Y1-EN_y4V9t9q2GCJskSu9MJOuLJ-7HDVO2ttJCderEmOufyIb9tg5rmlKND-YJe5BMMqkepvgEJM33b5QwdikwWpoZhhRIdmSjzDWrTdOBVFRHVUa4OTZXfZv0iztbV-8qIc5fce9DZOaqgDMSU027G1HYqZMlOCNxnrsw_K_BBCnZccSY25og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a911ceb49.mp4?token=F5gcbuk45H33fglYnSEjNOgpOSrrKUHMPRRUJdGQJFqyZXxsLLHUjU3DIapBVL9DKFk0dyyHqlRQEQSEaEbeZBXyIuDbNa_ABfw55qwj_1XXWEcEZcZc6KuBMZRWE9oREyNaj99QKKuZ2wnLQqp1BQUECIG7Dr4Y1-EN_y4V9t9q2GCJskSu9MJOuLJ-7HDVO2ttJCderEmOufyIb9tg5rmlKND-YJe5BMMqkepvgEJM33b5QwdikwWpoZhhRIdmSjzDWrTdOBVFRHVUa4OTZXfZv0iztbV-8qIc5fce9DZOaqgDMSU027G1HYqZMlOCNxnrsw_K_BBCnZccSY25og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ نظر بقائی درباره توافق: خیلی دور، خیلی نزدیک
🔹
سخنگوی وزارت امور خارجه امروز در پاسخ به سؤالی درباره اینکه توافق نزدیک است؟ گفت‌ که خیلی دور، خیلی نزدیک و افزود: ما تجربه ضد و نقیض گویی طرف آمریکایی را داریم و دیدگاه‌های خود را بارها تغییر داده‌اند.
🔹
اسماعیل…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/437463" target="_blank">📅 17:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437462">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WraiHr5or8jvjLYlS8goASSj1NiGHPaCYx10U7S9fPNbq62OZ90ZpCs_YTyckfLW8Na7mAypMwo26nJ-xJb9e9cs4fSBSiFLgE0OLxgl3YkaiZ7267lgCK9aFqD1uRcOnVVWozcxED0ppyHvlJAeLF1w_fwn0maw8moRbmNvejqPBrrqe5FY5oswCgDbVw__jafHeYEkCBtqaHDze-kA8nwtjJZCPigt_Ha7GVJse6_kUjHAEKQkADCHqEWQqBlktJOnqiz3hhLNs8X0KAbCcPG-bu3Y2BhYamuqURfHbQdci3GRJnPEsapF9L2k6neE3saN7eJOq1bFkZQ44HQW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نظر بقائی درباره توافق: خیلی دور، خیلی نزدیک
🔹
سخنگوی وزارت امور خارجه امروز در پاسخ به سؤالی درباره اینکه توافق نزدیک است؟ گفت‌ که خیلی دور، خیلی نزدیک و افزود: ما تجربه ضد و نقیض گویی طرف آمریکایی را داریم و دیدگاه‌های خود را بارها تغییر داده‌اند.
🔹
اسماعیل بقائی درباره سفر عاصم منیر به تهران و رایزنی‌هایش با مقامات ایرانی گفت: هیأت پاکستانی غروب جمعه رسیدند و از قبل وزیر کشور پاکستان چند روزی در تهران حضور داشت.
🔹
پاکستان به عنوان میانجی نقش مهمی را ایفا کرده و هدف از این سفر ادامه تبادل پیام‌ها بین ایران و آمریکا بود.
🔹
تمرکز ما در این مرحله بر خاتمه جنگ تحمیلی است با مختصاتی که کم و بیش اطلاع دارید براساس پیشنهاد ۱۴ بندی ایران که چندین بار رفت و برگشت شده و در خصوص بندهای مختلف آن دیدگاه‌های طرفین تبادل شده است و در این چند روز راجع به برخی نکات و عبارت پردازی‌هایی که راجع به آن اختلاف نظر کماکان وجود داشت بحث و پیشنهاداتی مطرح شد که همچنان برخی از آن در حال بررسی و اعلام نظر است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/437462" target="_blank">📅 16:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437461">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rs0o4HlzyyMU0HnRbA6jzeiI0v6VRwKFRxyOA1H3NxmF9_PvEce7hsxgOBPEOUWYVf2B2udRQDYW7jEkCjnrSz4cSRQ8BxoYgeEq_ozg89_IBWVDMEaWZhI5xB_fSNS6-7doz8yFfBLf3EeJcJjqw5utbaEvFghcHGtwN8F3m0ywcSgAmW6YkIYtscO_mMgEz2TJrMJrl6ZCF8Fed3WlopbbaoM1jO6Nhe5VCJuLgpnYlP-n-hn-miyasUSfKBXlb7-U1nnXtxogFLBfk8H7MQbaGS5_P5ktdZ-PSflzB_F7g1mBGk1PoOCQqcCXMiBrrF0_Kb-1tIadGG7073ha7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر کشاورزی: امیدوارم سازمان برنامه و بودجه زودتر پول گندم‌کاران را پرداخت کند.  @Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/437461" target="_blank">📅 16:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437460">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5724f03e5.mp4?token=ha1pavFmi7r4XTEm9AoljuM4YoTRaR7lhNbk3-nhQCwWaJTp1PQUbTwd_RzDUbWb0Ob0TKSsmGQPE0R2tHX9U0YvE0HKvT1rLafgeTNtGQm0F0MJmD-yZDoJ25OiUGzaWsAVsj-zuQGpLI3ySJF0zwCuB9ze-gys5pIsX0tSfgNDS1ywIktIhve72XpXdD9yrTpp7kCm5IH_UjR-S8cLOP76RE9h2g7w1bGMRpbhLgLGB4gPs3wQdjrU6iuoQ2cUCTjfbKw7SvRXcJ3p_sG_61DuKYWVT38nW7YQdUOo1DRcHmsZ0mZ_2RmCfCjtly4kR8qMyhj2ArRFKj9eA8P7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5724f03e5.mp4?token=ha1pavFmi7r4XTEm9AoljuM4YoTRaR7lhNbk3-nhQCwWaJTp1PQUbTwd_RzDUbWb0Ob0TKSsmGQPE0R2tHX9U0YvE0HKvT1rLafgeTNtGQm0F0MJmD-yZDoJ25OiUGzaWsAVsj-zuQGpLI3ySJF0zwCuB9ze-gys5pIsX0tSfgNDS1ywIktIhve72XpXdD9yrTpp7kCm5IH_UjR-S8cLOP76RE9h2g7w1bGMRpbhLgLGB4gPs3wQdjrU6iuoQ2cUCTjfbKw7SvRXcJ3p_sG_61DuKYWVT38nW7YQdUOo1DRcHmsZ0mZ_2RmCfCjtly4kR8qMyhj2ArRFKj9eA8P7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت‌هایی از کتابخوانی رهبر شهید انقلاب
🔹
«من در دوران جوانى زیاد مطالعه مى‌کردم. غیر از کتابهاى درسى خودمان که مطالعه مى‌کردم و مى‌خواندم، کتاب تاریخ، کتاب ادبیات، کتاب شعر و کتاب قصّه و رمان هم مى‌خواندم. به کتاب قصّه خیلى علاقه داشتم و خیلى از رمانهاى معروف را در دوره نوجوانى خواندم. شعر هم مى‌خواندم. من با بسیارى از دیوانهاى شعر، در دوره نوجوانى و جوانى آشنا شدم. به کتاب تاریخ علاقه داشتم و چون درس عربى مى‌خواندم و با زبان عربى آشنا شده بودم، به حدیث هم علاقه داشتم.» ۱۳۷۶/۱۱/۱۴
از کتاب‌کرایه‌ای تا کتابخانه آستان قدس
🔹
«نزدیک منزل ما کتابفروشى کوچکى بود که کتاب، کرایه مى‌داد. من رمان و اینها که مى‌خواندم، معمولاً از آن‌جا کرایه مى‌کردم. آستان قدس هم در مشهد، کتابخانه خیلى خوبى دارد. در دوره اوایل طلبگى - در همان سنین پانزده، شانزده سالگى - به آن‌جا مراجعه مى‌کردم. گاهى روزها آن‌جا مى‌رفتم و مشغول مطالعه مى‌شدم؛ صداى اذان با بلندگو پخش مى‌شد، به قدرى غرق مطالعه بودم که صداى اذان را نمى‌شنیدم!» ۱۳۷۶/۱۱/۱۴
کتاب‌خوانی در خدمت نهضت فکری
🔹
«در دوران مبارزات، کتابهایی را میخواندم به قصد این که ببینیم به درد چه کسی میخورد، یا کجاهایش به درد چه کسانی میخورد و یادداشت میکردم. جوانانی که با من رفت و آمد داشتند - عمدتاً در مشهد، یا در دوره‌ای که مشهد نبودم؛ تبعید بودم - من اسم میدادم که این کتابها را بخوانید؛ این کتابها هم متنوّع بود. الان هم می‌شود این کار را کرد و مجموعه‌ای را در نظر گرفت.» ۱۳۷۷/۱۱/۱۳
ساعاتی که هرگز هدر نمی‌رود
🔹
«بنده چند جلد قطور از یک عنوان کتاب را در اتوبوس خواندم! البته قضیه مربوط به قبل از انقلاب است که چند روزى براى انجام کارى از مشهد به تهران آمده بودم. وضعیت و فضاى اتوبوسهاى آن روزگار براى ما خیلى آزار دهنده بود و نمى‌توانستیم تحمّل کنیم. دلم مى‌خواست سرم پایین باشد و خواندن کتاب در چنین وضعیتى بهترین کار بود. ساعتى را که به این حالت مى‌گذراندم احساس نمى‌کردم ضایع مى‌شود؛ چون کتاب مى‌خواندم.» ۱۳۷۵/۰۲/۲۲
🔗
شرح کامل این گزارش را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/437460" target="_blank">📅 16:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437459">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvDLH3XWQmGJp4s6EF3doLvfeoSjTMpT1yKZFV4pPa2mtdSdv8OO0ZemUwptCnftGs7gEnCtcJmaC68EE9DZoZknb--sGHNaEaGHGa0EGlOr1NKzrUAF6pGtejPclpQDhpaNJCgmwEGxc1lOHYR2tWk2g-qafNwOCEBde4obMPCBLYGlMYpvTA6w37CojpUPD-xT9vbzsVKfLD2bEbMmcuiGWy1OCBHd_c5tj24bYvJa69flETExwz7Ou_IcxxYn_9r6wrCHTp9jAJC26rj12oQ51O-IqDm18gYEStL9lE4V-mdl-XMzcG0zjpjS_wgHqbWCdpB9VZpXlZ1b_Vds0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: سابقۀ مذاکره با آمریکایی‌ها حکم می‌کند نهایت دقت را به عمل آوریم
🔹
رئیس‌جمهور در دیدار فرمانده ارتش پاکستان: ما صرفا به‌دنبال احقاق حقوق حقه و قانونی ملت خود هستیم، اما سابقۀ و تجربۀ مذاکره با آمریکایی‌ها به ما حکم می‌کند که نهایت دقت را به عمل آوریم.…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/437459" target="_blank">📅 16:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437456">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awlSa19VU9oyBsmDSJyVY--jvCqnfi1PNAKCEt7tgQXoRSYZdCgK9l67try_Hy_qPZe4V9ljWa_kj2L9I_A9mtknaqH4tXf2bkowsqkswQ-e_d13w_F4B5fr1Li6XBmEAcW6r5f1O3InYu4AZEd4cm4PyKNO8Rpo-J2uBr4bW3J32JcK44es1mlvADLhcig5L1tbh_3mAL0i5s1rnczwQxeMUwFLMsDNv97sLW6DVlqIdzYDxklvOl2spr21VT4MHQUeFbYQXjcbCdP5Y2bXs4jMm-lFKgFQBzzdSXCWt2-ImYjFzTKkFsao3BixlpGBONVM2C_C-itcd_PTEQ-YbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8snhKgxfrVfxFjQZ9DgpkOe6e7xvatk00uCLCgOoBtCS3AsI3fazQoB3YC22WmqIb93ifDM3ytliDkvKLV3CyfDBKyET5NIs0f9ce1kN2ypGHtJdP78ppzIzim6f4kKu90nuJsgbfVNVGzkKZy6Cd0XMOojF6EzucQ2JrhsAX1FDUxQQDZO7TgeJhF3XPOI76balVnqAzna8FOJwHeRvVPi2lOcw_2X4PL-BVlM93mF8clD1yKI4fI_rVr8XGqVtiBgodGSFMAKdkN1KXaamhxydaD6HIL_-AKu7cqHgN14XhrY0HAupof7HjVkOretmTuDOIQfALEVFK8IXS-L4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
فرمانده ارتش پاکستان با پزشکیان دیدار و گفت‌وگو کرد  @Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/437456" target="_blank">📅 16:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437455">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ارتش: آمادۀ مقابله قاطع با هرگونه تعدی دشمنان هستیم
🔹
بیانیۀ ارتش به‌مناسبت سالروز آزادسازی خرمشهر: فتح خرمشهر، ثمره ایمان راسخ، مجاهدت خالصانه و ایثار بی‌بدیل فرزندان این مرز و بوم بود که با تبعیت از رهبری الهی حضرت امام خمینی (ره) و با اتکا به قدرت لایزال الهی، توانستند معادلات دشمن را برهم زده و مقاومت و ایستادگی ملت ایران را به رخ جهانیان کشند.
🔹
ملت شریف و نیروهای مسلح ایران، به‌ویژه ارتش غیور و سرافراز ایران، امروز نیز در پرتو همان روحیۀ جهادی و با بهره‌گیری از تجارب گران‌سنگ دفاع مقدس و جنگ‌های تحمیلی و ناجوانمردانۀ ۱۲ و ۴۰ روزه، در راستای تدابیر رهبر انقلاب برای مقابله با دشمنان، آماده و هوشیار است.
🔹
ارتش با تمسک به آرمان‌های رهبران کبیر و شهید و تحت فرامین حکیمانه رهبر معظم انقلاب، با عزمی راسخ و اراده‌ای خلل‌ناپذیر، خود را برای مقابله قاطع و همه‌جانبه با هرگونه تهدید و تجاوز دشمنان آماده نموده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/437455" target="_blank">📅 16:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437454">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Okt5xWWw5upUwfAOXsZL4d8dq3LPRptPJCoHfn8pjjmIQinI0Dr5_ceMPFWDG-0VRuN0fLWrCcuPWtK0dPSuQOiriZ7wYRPAgzAY2FegCTGkfF51JaYGrxeL6D-_yg7CXRW_-d7yskvmYIt2jpdIMaotLCaRu9qe7iTZRg8kDjD-p-7M3fiivCqBKTTwCsVwuLngQa23v_4qUe51vV1S3D2TQcMylszk9aySKAyiCRBBHO0qLSUJcCpiP5mkbAl0frh8w1EhPOd_LZuUws-PGxTYUH20n6mmvx4hjtRdTPRXSF1y-mDn5VRPUqXHZZVfB6AVA5Uw9teOiYwPiM1ZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه ورود بن گویر به خاکش را ممنوع کرد
🔹
وزیر امور خارجه فرانسه: به همتای ایتالیایی خود می‌پیوندم و از اتحادیهٔ اروپا می‌خواهم بن گویر را تحریم کند؛ وزیر امنیت داخلی اسرائیل از ورود به خاک ما منع شده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/437454" target="_blank">📅 16:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437453">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PilOIhelNczQDb-aj_2Mqxba-SLYm7Wjxr3LaZX2BZGzEvebd5zwJtw2t3UhVhOb9RrEcuX2nKrwJlJcJQK3vi4xE_Axezg9iKQ482tJgaI_gNs5Hb_56cbyM4fCXmQorc1cie_wPq1oa5LyxREECAPm2RZuWhy5m3zrDgTvoths0LzfUe-zfPfArUaODn2EBmIh3KC8pNmS_60V648sv-m6T6tIoCbQfbTKHEGR4AlcwC9R3TEjr3Lz8OnIQQYQwQ5oHvXGZXPhC6yK6tbe-U4Isp2XSN3fi2IAAax5orewoASPArFRZxOAR1Cdv60ByiYaxVWu-Jr6lHmAJN1nJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجهیز ۱۲ هزار مدرسه به نیروگاه خورشیدی
🔹
سازمان انرژی‌های تجدیدپذیر: سامانه‌های خورشیدی با ظرفیت ۵ کیلووات در ۱۲ هزار مدرسۀ سراسر کشور نصب می‌شود که سازمان انرژی‌های تجدیدپذیر تامین تجهیزات این سامانه‌ها را برعهده دارد.
🔹
هدف از اجرای این طرح، توسعهٔ انرژی‌های تجدیدپذیر در بخش عمومی و ترویج فرهنگ استفاده از انرژی پاک در مدارس کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/437453" target="_blank">📅 16:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437452">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mlw0vKlPBYDJSgiinzVy8kVtCx4NhOE5K7iqL1uWVhdJgLXmuo8ZTbTZoNRGBsMpXBVEesx7KX8Z1VLe8KfwHSfp5NzzfVDJo1cfL6HflpZAMWuz5kJcNfJDXJcAu9fLEF4zwEvXRgD5XSaDA4HyCb8UuMIFqVHY9Pna-j0Ho5Onfrsokmj94j-ExKK5yEcUGQ31PgAY28vyAwL9qC6DahaBkZwy6rg2ZO0EzLmHC5UxWnONV2a8vqjxcV8mA3LTJjVUlF071A7FsrS36CsMFfUlAdcd3PGp_BQH_nDnGNU7eYeZdSDKLbHwVtxRg8yeQ1DFtdiZRcLRtuULV432nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عاصم منیر همراه با عراقچی از محدودهٔ تاریخی میدان مشق تهران دیدن کرد  @Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/437452" target="_blank">📅 15:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437451">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZlZo-JL8G94gYdD7TulQPG64cpqNqmOu0BfMl2YyyW68tZPkffj1v9EoJeA7uQs1ntsR-Shhr99HTDeb8NbiLPQcsRMHd5GE8paHYFkA92RJgGAmXHlGoKaramSclo9JwFMuBN7lLWjlfEnS7CCLi5Gjz2n9kOXLT6VWn4VQpQhO5HAj9tGUHN-Kq349_4GwbN2b5UJft7gyh5dI2wjaWzuUlnbhzIvjAiDX0xffIJHRaebjS_IGraJUxLn4dCk6A6zOf8JsbwA2XPhw9B6MaFUv8GX8Q8Mc1kzMNPpBsLAFlxQJSYKufRYQTiJAq8v5qTor6vcoH3i9pJ99N1Exg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۴۰ کشتی در انتظار اجازهٔ ایران برای عبور از تنگهٔ هرمز
🔹
تصاویر ماهواره‌ای نشان می‌دهد که حدود ۲۴۰ کشتی در آب‌های خلیج فارس و در پشت مرزی که ایران آن را به‌عنوان منطقهٔ تحت کنترل خود در آب‌های خلیج فارس تعیین کرده است، جمع شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/437451" target="_blank">📅 15:45 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
