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
<img src="https://cdn1.telesco.pe/file/vFaeBZljXZQ-hGm2VpQVV1WelBdc3kemvoy2SD6rDtlKrTLl3jyehWbzXGI1_QmfziYx5XD7q0yYFz9raoumcd86j83SuvbwglHh4EF_oNj-mtWJ7oFbAL_jKchKqtq4cIkXlaxW0r75-97YbgXkhL8LrbfOcFltXtwo9OdNchtfYr25R4wkho9tmKfhl7KfYkvDIEpCMVf6czygwnvb3V0rR2pS4_X-W4BH57h2o3f-eXhpiasaBJ7wNhL-Iw__eDOiJDk4Nce6RRJ7MfAlfLJ81LSBPAzCTZWjif9_3tmnIRvNDsRztRBxsKgg6b_Tyqf1tLvEeoPlz_CiKe7a2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 15:41:04</div>
<hr>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/miDyvAE_0ePfu2X0a1A4CbrnWztALdE-dwLb3lHd68wqhOEsI0G8s_y1XCDwvR-HjqpseG-9flQPkg_Ocg2aZnMQW1KZfuioc-VRPR17CC36xW0Gt97_dWTYXsV0xNhoF4Lcd-PRJ_zQVfQx59J9zaMHRW7378fLNN9M_8pTwgrTiAyUsKSuOjji4ozKTPTmAUCB8DczqWBLUKBEa3xKz7H5XM84RTeGR6VhdeKaybnuR68zBVWcNmEnwhvv70yRwnKcH60H4-H3EamDOW6ZT7LaZYNSGDkkVMHBy9EIF44--uzbLfb59Bko4qrXua7YUNY17ACJ7hcWFFLpNgGPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار در کویت هم‌زمان با پیام‌ها درباره پرتاب موشک از خوزستان
آپدیت:
ستاد کل نیروهای مسلح کویت در بیانیه‌ای رسمی اعلام کرد پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی «متخاصم» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/77265" target="_blank">📅 10:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پیام‌های دریافتی:
صدای یک انفجار چابهار اومد دور بود فقط موجش بود
09:42 بدجور زد الان چابهار رو نمیدونم کجا بود
چابهار یهو صدای انفجار اومد شیشه هامون لرزید
🥲
قبلا تو روز روشن نمیزد
چابهار یچی زدن همه ریختن بیرون ولی نه سمت اسکله نه پایگاه امام علی اصلا هیچ دودی هم نیست به شدت لرزوند
آپدیت: منابع حکومتی
فرمانداری شهرستان چابهار: صدای انفجار شنیده‌ شده در روز جاری (۲۸ تیر) در حوالی شهر چابهار، ناشی از عملیات امحا و انهدام کنترل‌شده مهمات عمل‌نکرده بوده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/77264" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RSSRY5QKG2eErTTq-E4TR8kEOQALdN8055_u62l5n-dFS2PcYWukeHkd2BuCQwEEuzm9zz9DPP3jI81lQK9M_QsXLIYwzs7TBbawbSntTz_lTKbTQnzEUTWs2fDh6yUcUG1jt6U9VYRho18Uqv85QQeJyLy-XPvh7WIJf2-F_Mco5t8QZE-q-tF_MWwI-UXsHQdSv9JX8-0kz3hcuX_EuR0EcDEsM3psWR2yF50MfPV4e8_BGF9JscAPU2RetdrYVnUWYUHgGmMp81395rfHkm6zhILWwig6ktGk5lGyBonckymvwghO46o4rT8g3mIUNGt9TYbn_r8geRLCuyeI5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های ساعت ۹:۰۹
سلام وحید همین الان گرگان زلزله اومد نسبتا شدید بود
آقا وحید گرگان گلستان الان ساعت 9:09 صبح هم لرزید، زلزله بود
سلام گرگان الان زلزله اومد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/77263" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOzP_i9PRU7oGxxOzGXDGVEs8WLuGYLNeIC9295WUIUSXOBS5jSzhBPnQTKmIaElkq9AidKihHg8zZ2lKozSEiV6DMbujrEMk3WLgZfiiONhHIRBFj8WZpmqQV-L1EREqYJTKFFsq41hyexEeDsghdB2hZ0y5xxseEyNinV2eOBDnBLczFIxBQwAfKQRUuqiGmXOCuCCKd7gNVh_0n3pZnkC9R5wen1JHRuzjN4rU34jtHFCEVd8UP1fgfRUo7JLhWJh_fKTBzcXplEtQMayvYiKuSkl0VGJdETGO2tW65vzaWbaMlKnZU_ViEWtZsvbfe_DDrIvgkCHz6WnKFuO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت: زمین‌لرزه به بزرگی ۴
دوباره
در سالند خوزستان
پیام‌های دریافتی:
۷:۵۷ اندیمشک دوباره زلزله اومد
دزفول لرزید دوباره
اهواز دوباره زلزله اومد
دزفول لرزید بازم فقط شدتش خیلی کمتر بود
زلزله ۷ و ۵۷  دقیقه باز هم دزفول با شدت کمتر از قبلی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77262" target="_blank">📅 07:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77261">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj8qZVOnhx_nPxJRrGXBoKkBFTO_ppsFwJFO_6jxeW9cLFvHJ_gEG-KuT5s_pUnIukWSPOiVFEFQiqFf1uH77mKYuXeT1lXbVD5kUstMD-eqmFn5YFcOFstV9dIbtI0wCRqKGKrnN7BRRDmHrgCC2AWAa5Vjkz3qEeGg3vp0Y08zQ7m_-pR1He45KZ5DrIW0BbsCUMbiOb82GJ1sD4i02tVkgqP3wbgpHKRx98dDzKRkgZEH7Vyn6YhcwSOMMqET_HEPtYKtLs64WJZRlMIyCULnBon3Oa7hCxQsxccstZYh01m0WHTEO_Xa8qQlWzz95Qe_SjMPNsou0eFO9fTQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با ادامه سقوط ارزش ریال، قیمت ارز، طلا و سکه در بازار ایران به سطوح تازه‌ای رسیده است.
براساس نرخ‌های ثبت‌شده در روز ۲۷ تیر، قیمت هر دلار در بازار آزاد به حدود یک میلیون و ۹۴۵ هزار ریال، معادل ۱۹۴ هزار و ۵۰۰ تومان رسیده است. یورو نیز حدود ۲۲۳ هزار تومان و پوند بریتانیا بیش از ۲۶۲ هزار تومان قیمت‌گذاری شده‌اند.
در بازار طلا، قیمت هر گرم طلای ۱۸ عیار به حدود ۱۹ میلیون و ۱۳۸ هزار تومان و هر مثقال طلا به حدود ۸۲ میلیون و ۸۹۵ هزار تومان رسیده است.
قیمت سکه نیز یک میلیارد و ۹۰۰ میلیون و ۵۰ هزار ریال ثبت شده که معادل بیش از ۱۹۰ میلیون تومان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77261" target="_blank">📅 07:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b791da5472.mp4?token=iAJxzbnHTr6IRN4Kqk5F3Dro9m-w0rtIqQQt3fGOpt_yoov2JxaXs959_L6GAiVR6YbhRP4E5-ZcwF-4g96WkXf8qOzW0WUo7l9RIRkKHFTslAt63tvp7I4zALMcU1keitH82AwMsar4IuVXKeklfCzxfp3NGDHtKGPt5D069CPXwzaZDXGGDKycD62GzAv1MrmYoOrCaFuDxRRJNEw347ehmA0cZPObE6ZvzUqvcifQrC5dZzzPC-OANII8UGB8PBMlmtT4xP_WK35BbGNyzacUaNsiMkeVnVS2A1qJe7jNX7hZdJeYTihzj53LmJd7IxjaQ4DgL9dUKH8V-kbetA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b791da5472.mp4?token=iAJxzbnHTr6IRN4Kqk5F3Dro9m-w0rtIqQQt3fGOpt_yoov2JxaXs959_L6GAiVR6YbhRP4E5-ZcwF-4g96WkXf8qOzW0WUo7l9RIRkKHFTslAt63tvp7I4zALMcU1keitH82AwMsar4IuVXKeklfCzxfp3NGDHtKGPt5D069CPXwzaZDXGGDKycD62GzAv1MrmYoOrCaFuDxRRJNEw347ehmA0cZPObE6ZvzUqvcifQrC5dZzzPC-OANII8UGB8PBMlmtT4xP_WK35BbGNyzacUaNsiMkeVnVS2A1qJe7jNX7hZdJeYTihzj53LmJd7IxjaQ4DgL9dUKH8V-kbetA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا هشتمین شب متوالی حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) به دستور فرمانده کل قوا، دور دیگری از حملات علیه ایران را در ۱۸ ژوئیه ساعت ۱۱:۳۰ شب به وقت شرق آمریکا به پایان رساند.
در هشتمین شب متوالی حملات آمریکا، نیروهای سنتکام با موفقیت تأسیسات نظارت ساحلی و پدافند هوایی ارتش ایران، توانمندی‌های دریایی و محل‌های ذخیره موشک و پهپاد را هدف قرار دادند تا تضعیف توانمندی‌های نظامی ایران ادامه یابد. تجهیزات نظامی آمریکا همچنین نیروهای سپاه پاسداران انقلاب اسلامی را که در ۱۷ ژوئیه به نیروهای آمریکایی در اردن حمله کرده بودند، هدف قرار دادند.
بیش از ۵۰ هزار زن و مرد نظامی آمریکایی در سراسر خاورمیانه مشغول عملیات هستند. آن‌ها همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77260" target="_blank">📅 07:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">منابع حکومتی:
‌معاون امنیتی ‌استانداری خوزستان: ‌جنگنده‌های‌ آمریکا ساعت ۰۵:۵۵ دقیقه یک نقطه در اطراف شهر شادگان را مورد اصابت موشک قرار دادند.
ساعت ۶:۱۰ صبح امروز جنگنده‌های آمریکایی بار دیگر مناطقی در جزیره قشم را هدف حمله قرار دادند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77259" target="_blank">📅 06:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77258">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام‌های دریافتی:
الان دو تا افنجار بندرعباس ۶:۹
اصلا تا حالا این ساعت حمله نمیکردن!
وحید جان ساعت ۶ و ۹ دقیقه قشم صدای چند انفجار اومد باز
وحید ساعت ۶:۰۷ دقیقه دو بار قشم صدای انفجار و لرزش
دو سه ثانیه قبل از زلزله،صدای بمب سنگرشکن اومد،قشنگ از دوران جنگ تو گوشم صداش هست
بندر عباس ساعت 6:09 دقیقه مورد اصابت قرار گرفت دوباره
سمت پایگاه هوایی دو انفجار بلند
یکی دیگه هم الان زدن ساعت ۶:۱۰
سلام بندرعباس رو زدن ۳صدای انفجار پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77258" target="_blank">📅 06:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mz65I-ibq1SYPjxM3t-W9mZRgH6efEUCpnQJmEgcvUG3lVPJVk5TShs0NE0nPNShoVTRd7MSPQEo9u1y_80El_JRqeMMi--lV3XxccMDA-mpNkSmqeWoWzqBPA3bnmZHix5_wrxSW5oasErUJl34mhKXGDvRGG_dwcUkxax9PbuXuGxDY9wQX2iOUjRlFhGLZqYbN6688RgobVfbW-Wg97kVIcPWiRg7E_zZdvgEgpPGevgTiKhQUL5zx4FksuiGxVO-Temi4V84gYxMsFNDnN082rjqrIhdw7wNQ3WL1i1_V2tzKpZwGxZmEVroH8IvgTe9Dsvts7gKms1q2-FTmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
زمین‌لرزه به بزرگی ۵ در عمق ۱۲ کیلومتری زمین در سالند خوزستان
پیش از آپدیت:
پیام‌های دریافتی درباره لرزش زمین:
وحید جان همین الان زمین لرزه شدید شهرستان شوش
خیلی بد بود
دزفول  رو زدند
همین الان تکون خورد همه جا مثل زلزله بود
زلزله اهواز
خونه لرزید بد جور دزفول چ خبرههه
همین الان اهواز زلزله اومد
5:55 دزفول
از توی خواب پاشدم،تخت و خونه و تمامی وسایل داشتن با شدت بالا میلرزیدن
اصلا نمی‌دونم زلزله بود یا جایی رو زدن
اقا وحید اهواز همین الان زلزله اومد 5:56
اهواز ۲ بار پشت سر هم زلزله اومد
ساعت ۵:۵۵
یکم ترسناک بود
اهواز زمین لرزه اومد
خیلییی شدیدددد تمام خونه لرزید
سلام اهواز زلزله شدید ۶ صبح
همین الان اهواز خیلیی بد لرزید
زلزله اهواز ساعت ۵ و ۵۵
اندیمشک هم زلزله شدید امد
ماهشهر زلزله نسبتا خفیفی اومد
سلام زلزله اهواز شدید مثل اینکه از دزفول بود
سلام آقا وحید اهواز الان زمین لرزه حساس کردیم،ساعت ۵ و ۵۷ دقیقه صبح
وحید جان دزفول همین الان زمین لرزه شدددد
زلزله اهواااز
از خواب پریدم کامل تخت تکون میخورد
زلزله اهواز اومد وحید کل خونه لرزید
ساعت ۰۵:۵۵
از خواب پریدم از شدت زلزله
اهواز چندبار لرزید بدون صدا
وحید جان الان اهواز زلزله ساعت ۵.۵۵
سلام زلزه اومد اهواز‌
وحید از خواب بیدارم کرد
و طولانییی بود
سلام وحید جان ساعت 5:56 دقیقه زمین لرزید ویه تکون خیلی شدید خورد خونه دزفول
سلام وحید جان ساعت ۵:۵۶ صبح زلزله فوق شدید اهواز همه چی داشت تمون میخورد
همین الان اهواز زلزله ، وحشتناک بود
سلام اهواز زمین لرزه بزرگی اومده حدود 10 15 ثانیه خونه داشت میلرزید
زلزله خیلی شدید اهواز ، ۲ بار تقریبا پشت سرهم ساعت ۵:۵۷
اهواز ساعت ۵:۵۵ خونه بد لرزید انفجار نبود انگار زلزله اومد
اهواز ساعت 5:55 دوبار زلزله اومد
آقا وحید زمین لرزه شدید اهواز در حدی که مبلا از جاشون تکون خوردن
سلام زمین لرزه اندیمشک هم حس شده
سلام شوش دانیال همین الان لرزید. انگار زلزله بود
دزفول  ساعت ۵:۵۶ صبح چند دقیقه ناجور لرزید
اهواز زلزله اومد هنوز لوسترها تکون میخوره
سلام وحید خوزستان لالی خیلی شدید زلزله اومد۵:۵۵
مسجدسلیمان هم زلزله حس شد ۵:۵۶
درود ایذه دو بار لرزید الان‌
سلام ساعت 6.55 شوش بدجور لرزید اما خیلی کوتاه ولی خیلی ترسناک بود
سلام ساعات 5:55 گتوند خوزستان زلزله احساس شد لوسترا تکون میخوردن
سلام زلزله سمت دزفول خیلیییی شدید بود یکم دیگه ادامه میداشت من خودمو از تراس پرت میدادم
اینقد طولانی بود که موقعی که بیدار شدم رفتم توی تراس هنوز قطع نشده بود توس عمرم اولین بارم بود همچین چیزی حس کرده بودم
🔄
پیام دریافتی به نقل از مرکز لرزه‌نگاری کشوری:
گزارش مقدماتی زمین‌لرزه
بزرگی: 5
محل وقوع: استان خوزستان - حوالی سالند
تاریخ و زمان وقوع به وقت محلی: 1405/04/28 05:55:21
طول جغرافیایی: 48.61
عرض جغرافیایی: 32.58
عمق زمین‌لرزه: 12 کیلومتر
نزدیک‌ترین شهرها:
23 کیلومتری سالند (خوزستان)
27 کیلومتری اندیمشک (خوزستان)
29 کیلومتری دزفول (خوزستان)
نزدیکترین مراکز استان:
103 کیلومتری خرم آباد
140 کیلومتری اهواز
📍
آمریکا هم
میگه
بزرگی زلزله ۴٬۹ بوده در عمق ۱۰ کیلومتری همونجاها:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77257" target="_blank">📅 05:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77256">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیام‌های دریافتی:
بندرعباس همین الان صدای چهارتا انفجار اومد
03:33 سه تا پشت هم صدا اومد بندرعباس ولی فکر میکنم دور بود
همین الان بندر عباس صدای 4 انفجار
الان وحید جان ۳:۳۳ چهاتا انفجار شدید بندرعباس
همین الان قشم
صدای ۶ تا افجار پشت سر هم
خیلی بلندو قوی بود
کل پنجره ها لرزید
سلام ساعت۳:۳۴ صدای سه تا انفجار قوی اومد بندرعباس
سلام بندرعباس ساعت ۳ نیم صدای ۴ انفجار شنیده شد
بندرعباس ۴ تا الان زدن
#بندرعباس
28 تیر ساعت 03:33
صدای 4 انفجار سریالی،محدوده پایگاه هوایی
۴ تا انفجار سنگین در بندرعباس
بندرعباس 3:33 تقریبا سه تا صدا اومد
🔄
سه تای دیگم زد 03:35
مجدد انفجار ۳ تا در بندرعباس
دوباره زد ، شدید داره میزنه
یه صدای خیلی وحشتناک تر الان اومد۳.۳۵ بندرعباس
دوتا دیگه هم الان زد
سلام صدای ۴ انفجار به همراه لرزش از قشم
بندرعباس وحشتناک صدا انفجار میاد مشت سر هم داره میزنه
بندرعباس صدای انفجار 3.35 شدید بود
وحید قشم رو الان ساعت ۳ و ۳۴ دقیقه دو بار زدن
بندرعباس همین الان 3 انفجار جدید3:35
#بندرعباس
28 تیر ساعت 03:35
صدای 3 انفجار سریالی دوباره ،محدوده پایگاه هوایی
وحيد جان قشم هم صدا مياد
٤،٥ بار پشت سر هم
همین الان ساعت ۳:۳۶ چندتا صدای انفجار شدید در قشم
الان ۳تا افنجار دیگه اومد، کل خونه لرزید، خیلی بد بود ۳:۳۶
تسنیم ساعت ۴:۴۵
گزارش ‌خبرنگار تسنیم از بندرعباس:
🔹
براساس اعلام استانداری هرمزگان، تا این لحظه ‌بر‌اساس گزارش‌های دریافتی، هیچ‌گونه اصابت موشک یا پرتابه‌ای در بندرعباس ثبت نشده است.
🔹
در حال حاضر آرامش در منطقه برقرار بوده ‌و با وجود شنیده شدن برخی صداهای نامشخص، طبق آخرین گزارش‌ها تاکنون هیچ موردی از اصابت موشک در بندرعباس تأیید نشده است.
🔄
ساعت ۵:۳۰
صدای انفجار اومد همین الان
4 تا پشت هم
وحید الان ساعت ۵ و ۳۰ دقیقه قشم دو بار صدا انفجار شدید اومد خونه لرزید
بندرعباس الان دوتا صدای انفجار اومد ۵:۳۰
ساعت ۵:۳۱ دوتا صدا انفجار اومد بندرعباس
دو انفجار الان بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77256" target="_blank">📅 03:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77255">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پیام‌های دریافتی ۲:۱۷
درود وحید جان همین الان بهبهان اگر اشتباه نکنم سمت پالایشگاه بیدبلند رو زدن ما تو حیاط بودیم  که اون سمت آسمون سرخ شد
سلام بهبهان صدای سه تا انفجار اومد
سلام بهبهان چندین صدا اومد
صدای عبور جنگنده در بهبهان شنیده شد ولی تا این لحظه هیچ  صدای انفجاری من که ساکن شهرم نشنیده‌ام.
خبرگزاری مهر:
برخلاف فضاسازی رسانه‌های ضدانقلاب، تاکنون هیچگونه حمله و بمبارانی‌ در بهبهان صورت نگرفته است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77255" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77254">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iPMK1ZpAeyHr4mXpsCTGZDonk7L2wb7bHEGZCHXFAREmCRYaONHFkW7MiZmF1124_O5aENsB4Lc46h7vSQVnqqtyF3SfIO6YxuMsiQjlElwb8HISeTEFuRlJsXpjCqtm778LadTvcfwvpR9EP2rBIltGbmz2dKzrQX_FF2m6VDAY0ZkQwddxO0wXU5mEE-0I9LapsgIm0Tj1UHtLripclU4xusmLTEGQy68uxRqNPyqvIH_FELcYYL4rRWIS8r-osGPDfpgdVUumTxIyogh4lpXMIWkpXdHHRBoumZgTpsXvAAKzpq2lWxdhtvBMiKKjv5XO-Y2NjRlpgX3SBLIrQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۶ عصر به وقت شرق آمریکا [۱:۳۰ بامداد یکشنبه به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور تازه‌ای از حملات هوایی علیه ایران را آغاز کردند.
این حملات با هدف تضعیف بیشتر توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز و مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی انجام می‌شود که شب گذشته به نظامیان آمریکایی در اردن حمله کردند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77254" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uj1_ZRVsLm0Q2ImLhOEtD9ihKZRdEu1Z-aCFDbeSP7JDa98_8m0W7LiROm-7fAJiGDksus11ey2FA0I9yFXcMkwc8z4M56eEyk4M1EZPnNBmnyc5HSSs_KJWfqn7GmiL675Is3xmzeIWH_7TPg1rh70-HSCJEwNGjQx-4Fkmn0ArOCIcA5Dc-EoCNFZdnN_FhEfz9Plgdy8b0A21cU_3AU2cUeGfQb_unJ4BWnR2NIUO-jM0W-jb-4uyB-YrfT1mYxJd-ct1u5riz3ObwosuHvx7gzlia2mS9A9GZphCxYFPH_uR2yV1YDmy3EIH_TRMznd2hTdsDgVhbdUNLPD1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d99_lFgXJxc0GYm-OhZjCgjSFhK4nwWRdXOZR-Kqv1nhf6ejSUkSzTzS0OWlDC4YM-aSxoNS1Z5qMHkjAf9jz3o9CwgFIt4J770cHXxNi3FJz5-XImg_WI2FX5m3FQcy0wYdCMnuUh4LPBY2VCe6cku1hED2Z0eO85fOlz9ZoQ9hGYexZ8VtfyZwdcAIRPaI91Tm8nbUqp6ebTXRjxGd5f_EaQPv9AST9OfuX7pKs5B6mRVSZMP1VUvvDoPjyyT38BfhszkDqEsEOOY36EAq5pKENYHnky_bv6Q-jwhzEqom-Url7Hk7wRgZSyGnHvx73gNsw_Hp-gKkK2W7a0veSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری ایالات متحده، در واکنش به کشته شدن دو سرباز آمریکایی در اردن به شبکه «نیوزنیشن» گفت: «بسیار غم‌انگیز است، واقعا رویداد بسیار غم‌انگیزی است. ما از دیدن چنین چیزی متنفر هستیم. آنها در راه خدمت به کشورمان جان خود را از دست دادند.»
@
VahidOOnLine
ترامپ در بخش دیگری از این مصاحبه با مواضعی قاطع، بار دیگر تأکید کرد که «ایران نمی‌تواند و نباید سلاح هسته‌ای داشته باشد.»
او همچنین در واکنش به اظهارات مقامات جمهوری اسلامی مبنی بر تعلیق تعهدات تهران در قبال توافق موقت یک ماه پیش، با بی‌اعتنایی کامل اعلام کرد که اهمیتی به این تصمیم ایران نمی‌دهد.
پیش از این، کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه جمهوری اسلامی، شنبه ۲۷ تیر، گفت آمریکا همه تعهدات خود ذیل تفاهمنامه اسلام‌آباد را نقض کرده و ایران نیز اجرای تعهداتش را متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77252" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMUFBn7sZKKZiAThI_WDVVWZVJMa3qqlV12iy-A7_UZWKHE5jyV880QJbxTj3rJZp1XrRiwxyPSyg-xTX6dv_flg32284AdZCWqYNa8SD30x7VEVDR3bfpwwzv7r-TL5yNpEdjRZNym-rZpLw09eP9uoq9GnGfuI_T8nBhFevzJqMcRiutzhGkeeVgSAxnQ3v3R8ElG4UK6QZhMOX7aGEtxYNTZ7fHmiP_sIrdaFnX-zD-JxVbHD5fruaS1PcoluTjQ_n9wbZhspuyjvHelLDUFbBxNMxh2aFdcpAJ4ozG9pA8zl7zf1zb_yzFBDXi05RTXvaHS3qpXDllf7a4OcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز به نقل از چند مقام آمریکایی نوشت حمله جمهوری اسلامی به اردن که جمعه به کشته شدن دو سرباز آمریکایی و مفقود شدن یک سرباز انجامید، چهارمین حمله به نیروهای آمریکایی در این کشور طی پنج روز گذشته بود.
به گفته این مقام‌ها، این حملات در مجموع ده‌ها سرباز آمریکایی را زخمی کرده و به تعدادی بالگرد بلک هاوک آسیب رسانده است.
این مقام‌ها گفتند حملات و خسارات ناشی از آنها نشان می‌دهد نیروهای جمهوری اسلامی همچنان ذخایر موشکی قابل توجهی دارند و در عبور از سامانه‌های دفاع هوایی آمریکا نیز ماهرتر شده‌اند.
نیویورک تایمز نوشت اهمیت اردن برای عملیات آمریکا افزایش یافته است، زیرا پنتاگون پیش و در روزهای نخست جنگ، بخشی از نیروهای خود را از بحرین، امارات متحده عربی و قطر به اردن و اسرائیل منتقل کرد.
به گفته مقام‌های آمریکایی، محدودیت‌های اعمال‌شده از سوی برخی متحدان منطقه‌ای آمریکا برای استقرار نیروها و پرواز هواپیماهای آمریکایی بر فراز خاکشان نیز نقش اردن در عملیات واشینگتن را افزایش داده است.
پنتاگون از اظهارنظر در این‌باره خودداری کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77251" target="_blank">📅 01:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeDjQirylhoaoHUdFSGUe9TdBZZcA0oMkcRTNnqxnPvSgBsfHNioN01nj_8XcDeMw9lDFCbos5KWLx9sCRFc0PfPWK8VRzuJHymVanPmSGV-RcGxZMriqi1_xeA9ttWx-_q2eoWpC4lDj5fDf28bG3opVGAR64sC1XVbzjxQKzq2dEle5QUohwVGgejTzpy43_-VYmWeh87c3oJK5LMEcwX_4Hqw8pi3OuH9J50StMtsYBfSATNP0N73hioV0zRxjuVzZ2GyzGaNp6X8hkOMPU-BtBtHbtmkVwoMJWcdcg4ZEUMncof9bXdGWunVzQ8KA6hCNWbjqet8kSudKnqaxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری مهر، بامداد یکشنبه، ۲۸ تیرماه، زمین‌لرزه‌ای به بزرگی ۳.۷ حوالی سرگز در هرمزگان را لرزاند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77250" target="_blank">📅 00:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">چند پیام دریافتی در ساعت ۲۲:۱۳
بندرعباس ۳ انفجار
اقا بندرعباس رو زد
۴ الی ۵ تا
زدن داداااا
بندرعباس
اقا وحید الان بندرعباس زد صدا اومد معلونم نبود کجاس
[ولی فقط همین‌ها بودند و انقدر هم صبر کردم که دیگه پیام‌های دریافتی بعد از انتشار این پست فاقد اعتبار محسوب می‌شن.]
آپدیت:
گزارش خبرنگار تسنیم از بندرعباس:
🔹
از دقایقی پیش اخباری مبنی بر صدای انفجار در بندرعباس منتشر شد، اما مسئولان استانداری هرمزگان ضمن تایید این صداها می‌گویند هنوز گزارشی از اصابت موشک یا حمله جنگنده‌های آمریکایی نداشته‌ایم.
🔹
از سوی دیگر برخی منابع خبری به خبرنگار تسنیم تاکید کردند احتمالا این صداها مربوط به هشدار نیروی دریایی سپاه به کشتی‌های متخلف در تنگه هرمزگان باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/77249" target="_blank">📅 22:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/77727bb200.mp4?token=nO4CXIbA5rqTJ5Rfi_tEr1uPhW0lI7IXOtNEG88Zbs-l1mVQUjW1yWa2hxFnPl8aJivvl4-r0OX1re8zTTEorCod5rde1nWXuUifiG_5u9gRCi5MXaxieriZU4KVJTPHlWmV1lVrj8xF3zLP2VNYhFlwY70LU0hLAlVfcXJXLh14f--KlcVLGsPOt_j-G7LHwtJSPpgBdTMSrlVwqUxgZotCPM87XdeOAnawUzQqxoRMKW1k41pwUbGTNXCAo9wwLt9kn6t18JVwROvo4So5mZ-cF7WcJ05OA7msMWXCt_X_SSoMKXaFT72imw-lT73m7q6_CvWBgQeKHrjjYa7ChA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/77727bb200.mp4?token=nO4CXIbA5rqTJ5Rfi_tEr1uPhW0lI7IXOtNEG88Zbs-l1mVQUjW1yWa2hxFnPl8aJivvl4-r0OX1re8zTTEorCod5rde1nWXuUifiG_5u9gRCi5MXaxieriZU4KVJTPHlWmV1lVrj8xF3zLP2VNYhFlwY70LU0hLAlVfcXJXLh14f--KlcVLGsPOt_j-G7LHwtJSPpgBdTMSrlVwqUxgZotCPM87XdeOAnawUzQqxoRMKW1k41pwUbGTNXCAo9wwLt9kn6t18JVwROvo4So5mZ-cF7WcJ05OA7msMWXCt_X_SSoMKXaFT72imw-lT73m7q6_CvWBgQeKHrjjYa7ChA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توییت، ترجمه ماشین:
این ویدیو لحظه اصابت چند موشک بالستیک ایرانی با برد متوسط تا میان‌برد به پایگاه هوایی موفق‌السلطی در اردن در طول شب را ثبت کرده است؛ حمله‌ای که دست‌کم دو نظامی آمریکایی را کشت و چند نظامی دیگر را مجروح کرد.
sentdefender
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/77248" target="_blank">📅 21:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E2HpnAbRiqEx3c0H2E87kwZJHUDmftJ-DCUqKZRYqq37lb1AjgqO_QyRJePJKPoULFzSLV4D-46Y1fySwkPvyssFkb5uX92VQPGlu-iGshkDtWbgDZWSfxbMNMdz74_923NJyJPCAs3y4qtcaQ_zN14HdCyjqVmpLS6G-u7sv-AV4LIKIC91kRoMSJprVeOwQVgVq7RMhDUBLL-hp9WfaHxbuz1WxMY415c_OwT4fDAXy6L5O6EkYCVwS4_s0dPPdmclwE_8mRxPmrMl_UidFerVXRtPRrErdczso14cfIOpReYJdkH3MocI4rr2kNqILvpQ8Z-m2WUELtAmHVuyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: دو نظامی آمریکایی کشته شدند و یک نفر مفقود است
پست سنتکام، ترجمه ماشین:
بیانیه سنتکام درباره نظامیان آمریکایی جان‌باخته و مفقودشده
تامپا، فلوریدا — در ۱۷ ژوئیه، در حالی که فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای شریک در برابر حملات موشکی بالستیک و پهپادی ایران دفاع می‌کردند، دو نظامی آمریکایی در اردن در جریان عملیات کشته شدند. همچنین، یک نظامی در حال حاضر مفقود است.
چهار نظامی آمریکایی برای دریافت خدمات پزشکی به بیمارستان‌هایی در اردن منتقل شدند. آن‌ها از آن زمان مرخص شده‌اند. سایر نیروهایی که به‌دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به خدمت بازگشته‌اند.
سنتکام از سر احترام به خانواده‌ها، تا ۲۴ ساعت پس از اطلاع‌رسانی به نزدیک‌ترین بستگان، از انتشار اطلاعات بیشتر، از جمله هویت رزمندگان جان‌باخته، خودداری خواهد کرد.
CENTCOM
پیت هگست، وزیر جنگ آمریکا، در واکنش به کشته شدن دو نظامی آمریکایی در حملات جمهوری اسلامی در اردن در شبکه ایکس نوشت: «خدا نگهدارتان، قهرمانان. فداکاری شما فقط عزم ما را راسخ‌تر می‌کند.»
پیش‌تر سنتکام خبر داد دو نظامی آمریکایی روز جمعه ۲۶ تیر در جریان مقابله با حملات موشکی و پهپادی جمهوری اسلامی در اردن کشته شدند و یک نظامی دیگر همچنان مفقود است.
سنتکام افزود چهار نظامی مجروح پس از درمان از بیمارستان مرخص شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/77247" target="_blank">📅 21:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/863eecb938.mp4?token=pKmQXrU4UyjgVkTlTG4RHqArqaHgUBLebwz-6yrU6pjeSutAQXIc_vRiSy-uIvp9U5a0JiPoNTZMZZQSWL6O_9NE4nSlAm0qMghv4dNJBtTFpvTc0G9OC_aWrRYux22L5vARE3DlMwCsGWoGRXppaSG-fFyPxnl1qB-iXHRashGodyHLgfg6PUt9BISnWJs7Gw67Abnfcde-6UK1Ck5M0-hlN5oADnT1MIiMcZ7akW5O5quabRfpJmwetUAYL6JbgoBNVBTEFREZM5_qPy-nHiufLGupmLRU76tWqnWgej6n1XDxyIZdZFYujkpkpga4Lhnt_2RN0X-fT8zbF0YIg1x5hKYFxVHxadnm3vL8x8sA_bGkoJS7XGU6IykqJwxYGdMjdFW5Fii8cXUnPu1cryxYH46Nw7mh21l3BQzor6eCKxNxenDViX6iFSrUAKLbrwfUiGV5Zh8ALQPhDn3xT4EVrbzSt7q5GQOLvwyvghSs9sCuuuI_Ius9rZIQxx3s-jpXZ9ATnE48KyrB7ZylFKymZVZgtnEP_qQfgtRLhO7KM4Cawk9a0Lnyzz4CIlmXyxPTM4j8cz0XQEZVAnKjLxJwRo8E60DTparX24ZOHeRMyQxgtwfjYFMSxRdyFI2AEb9iHFeRkbsdimmtsopKVJVwWIK3DJkxBazhaA5oeAM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/863eecb938.mp4?token=pKmQXrU4UyjgVkTlTG4RHqArqaHgUBLebwz-6yrU6pjeSutAQXIc_vRiSy-uIvp9U5a0JiPoNTZMZZQSWL6O_9NE4nSlAm0qMghv4dNJBtTFpvTc0G9OC_aWrRYux22L5vARE3DlMwCsGWoGRXppaSG-fFyPxnl1qB-iXHRashGodyHLgfg6PUt9BISnWJs7Gw67Abnfcde-6UK1Ck5M0-hlN5oADnT1MIiMcZ7akW5O5quabRfpJmwetUAYL6JbgoBNVBTEFREZM5_qPy-nHiufLGupmLRU76tWqnWgej6n1XDxyIZdZFYujkpkpga4Lhnt_2RN0X-fT8zbF0YIg1x5hKYFxVHxadnm3vL8x8sA_bGkoJS7XGU6IykqJwxYGdMjdFW5Fii8cXUnPu1cryxYH46Nw7mh21l3BQzor6eCKxNxenDViX6iFSrUAKLbrwfUiGV5Zh8ALQPhDn3xT4EVrbzSt7q5GQOLvwyvghSs9sCuuuI_Ius9rZIQxx3s-jpXZ9ATnE48KyrB7ZylFKymZVZgtnEP_qQfgtRLhO7KM4Cawk9a0Lnyzz4CIlmXyxPTM4j8cz0XQEZVAnKjLxJwRo8E60DTparX24ZOHeRMyQxgtwfjYFMSxRdyFI2AEb9iHFeRkbsdimmtsopKVJVwWIK3DJkxBazhaA5oeAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پیامی منتسب به مجتبی خامنه‌ای، سومین رهبر اعلام شده جمهوری اسلامی، او با اشاره به نقض تفاهم‌نامه میان ایران و آمریکا تاکید کرد که این اقدام بار دیگر «بی‌ارزشی و نامعتبر بودن امضای رئیس‌جمهور آمریکا» را نشان داده است.
مجتبی خامنه‌ای همچنین، آمریکا را به «جنگ‌افروزی» متهم کرد و نوشت: «اکنون که دشمن امریکایی به دنبال جنگ‌افروزی و تحمل هزینه‌های سنگین‌تر و بی‌آبروئی بیشتر است، بداند که ملت عزیز ایران و جبهه مقاومت، درس‌های فراموش‌نشدنی برای او دارد.»
@
VahidOOnLine
متن پیام بنا بر فایل PDF منتشرشده در منابع حکومتی:
پیام رهبر معظم انقلاب درباره‌ی حماسه عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور
بسم الله الرحمن الرحیم
ملت عظیم‌الشأن و شگفتی‌ساز ایران!
سلام و درود و سپاس بر شما که با حماسه‌ی بی‌نظیر و تاریخی خود در رستاخیز بی‌سابقه‌ی بدرقه‌ی آقای شهید ایران، نصاب تازه‌ای از جلوه‌ی بعثت و اراده‌ی مستحکم هویت اسلامی ـ ایرانی را در قدرشناسی، وفاداری، بصیرت، و ابراز محبت فوق‌العاده به زعیم امت اسلامی و رهبر شهید انقلاب ثابت کردید.
گرمای دل‌های گداخته، چشمان اشکبار و عزم‌های استوار جمعیت ده‌ها میلیونی و ده‌ها کیلومتری در تهران، قم، مشهد، و سایر شهرها و روستاها، دوستان ملت ایران و مردم آزاده‌ی جهان را به تحسین و دشمنان مستکبر ملت ایران را به حیرت و سرگردانی و خشم و وحشت انداخت.
همزمان با این حماسه، نقض عهدهای مکرر شیطان بزرگ نسبت به تفاهم‌نامه امضاشده بین رئیس‌جمهوران ایران و امریکا بار دیگر این حقیقت را به همگان ثابت کرد که امضای رئیس‌جمهور امریکا چقدر بی‌ارزش و نامعتبر است و زورگویی، تمامیت‌خواهی و وحشی‌گری، اجزاء لاینفک مرام و مسلک امریکایی می‌باشد. امروز شیطان بزرگ بار دیگر چهره‌ی واقعی و بدون نقاب خود را آشکار کرده تا این تجربه‌ی تاریک از جنایت و بدعهدی، سند محکم دیگری بر دروغگویی، غیرمنطقی و غیرقابل‌اعتماد و پلید بودن امریکا باشد.
اکنون که دشمن امریکایی به دنبال جنگ‌افروزی و تحمل هزینه‌های سنگین‌تر و بی‌آبرویی بیشتر است، بداند که ملت عزیز ایران و جبهه‌ی مقاومت، درس‌های فراموش‌نشدنی برای او دارد که رشادت‌های رزمندگان اسلام و غیرت مردمان شجاع خطه‌ی جنوب در این روزها نمونه‌هایی از آن را نشان داده است.
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدس در همه‌ی سطوح مردم و مسئولان و در تمام عرصه‌ها برای تحقق آرمان‌های بلند انقلاب اسلامی و تأمین عزت و استقلال ایران عزیز خصوصاً در برابر دشمن جنایتکار و حیله‌گر امریکایی است. همان‌گونه که پیش از این مکرراً و مؤکداً تذکر داده شد، صیانت از وحدت و پرهیز از تفرقه و تنازع، اختلافات سیاسی و برجسته کردن تفاوت‌های اجتماعی وظیفه‌ی همگانی است و البته نقش مسئولان و عناصر دلسوز و دلباخته‌ی انقلاب و امام و رهبر شهید در انسجام و یکپارچگی کشور، مهم‌تر و حساس‌تر است.
بر این اساس ملت عزیز، با تداوم بر اعتماد به مسئولان دلسوز در هر سه قوه که تلاش ایشان برای رفاه و سعادت ملت، مشهود می‌باشد، همچنان برای تضمین صیانت از منافع ایران اسلامی، هوشیار و فعال در میدان خواهد بود. ممکن است کسانی با اخلاص تمام و از سر خیرخواهی، انتقاداتی نسبت به عملکرد بعضی از مسئولین داشته باشند. به نظر بنده، در عین اینکه این اهتمام و نگرانی ایشان برای نظام همچون اشخاص خودشان، سرمایه‌ی ارزشمندی به شمار می‌آید و فی‌نفسه امری مطلوب قلمداد می‌شود، این عزیزان که بعضی از ایشان از زمره‌ی پیشروان بصیرت هستند باید مراقب باشند تا این رویکرد، اولاً ظلمی را بر بی‌گناهی روا ندارد که آن خود منشأ محرومیت از برکات و عنایات می‌گردد. و ثانیاً موجب شکست در وحدت و انسجام اجتماعی نگردد؛ که با حفظ این جهات، انتقادها موجب رونق و شکوفایی امور خواهد شد.
دشمن نباید هیچ علامت ضعفی و از جمله این ضعف را از ما دریافت کند؛ که هرگاه ما این مراقبت‌ها را به طور کامل مراعات نماییم، او به ناچار رو به هزیمت خواهد گزارد.
بار دیگر از یکایک مردم عزیز که خود، صاحب عزای پدر شهید امت هستند و با وجود دشواری‌ها و برخی محدودیت‌ها و ناملایمات در رویداد عظیم بدرقه‌ی آقای شهید ایران، حماسه‌ای تاریخی خلق کردند صمیمانه قدردانی می‌کنم.
همچنین از مراجع معزز تقلید، علما، اندیشمندان و نخبگان، فعالان فرهنگی، اجتماعی و سیاسی و از اقدامات و تلاش‌های نهادهای کشوری و لشکری و نیز حضور مقامات و نمایندگان جبهه‌ی سرافراز مقاومت و نهضت‌های پرافتخار اسلامی تشکر می‌کنم. امید است همه‌ی کسانی که در این حماسه‌ی تاریخی به هر نحوی حضور و همراهی و همدلی داشته‌اند، مشمول عنایت و دعای خاص سرورمان عجل الله تعالی فرجه الشریف باشند.
سیدمجتبی حسینی خامنه‌ای
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77246" target="_blank">📅 20:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAZAOa8mVlAdiQ92Me6FKe_kbkBssgGCDnEXMVpuvsMvstBd8X9gOwStT4J3WvTKTKYs7T8ZeH1o-qb--dcI7RPeCVrzXCJOUrDmwh5wH7PnlehO04JkUsWj5vOSpcNO2DYGd4CQ7t2WOcv6pSuElKMlNTGKoPgI2ulO21ctW63hLInAF34h09sD3UPMFt1kvyKG3SfIBSSFkd0C5J2Hf9Qq5aQhpNRqntHa9tTOoTDQJXG-9Lt5dWWuVOHZN-GXN4QQ1gyCCXeQoZolwwaWPtF71Tu7SOK0kVkvt0DeZ7NkGwHI-SmcKfDI0ocTIXp3ugWMdt7seb5U-n3rUqHL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران به نقل از استانداری هرمزگان خبر دادند طی ظهر تا عصر روز شنبه چند حمله موشکی به حوالی شهر سیریک در نزدیکی تنگه هرمز انجام شده است.
استانداری هرمزگان اعلام کرد: «در ساعت ۱۲:۳۰ و ۱۶:۳۰ و ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت.»
در این بیانیه آمده که «هیچ مصدوم غیرنظامی» بر اثر این حملات گزارش نشده است.
سنتکام، ستاد فرماندهی ارتش آمریکا در خاورمیانه، درباره چنین حملاتی به ایران گزارشی اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/77245" target="_blank">📅 19:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XQzRFlDYQFEoe27xcxhMHHEpX0WRQ54Yp0AYtajV2kelqyJ4XW_wBP-6hVNa-VGlL6LW7Hi8sbKIlFV6qzw-dzAv57hPZ4zKU_VnG8usnn0NFqMJVeWrvDLWJ5KLdKgWtDD7iiCksxf45z1XaJF3R7BG21Pg2deEqqkWWy8aclBQqYtlyl1jayGazVLaQPzTkjbRV9yvbca6DE6k_rEXRx154e-v44pxJ4_5JSJK8zaktRbtt2DwRZfpc2f4vxJnJR-tJWIiHx6Iy1H4-_wAVYySOBWwC9zM8ZCM6m-ZUNjTDIhadLDLJCgCqakGmOaBYs6NICvnZ-x8FyeCSkEiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/au3TVm9LdsrA0v3KM8H6cxnzMnSElxkHgb121sE2PK_XNACY9qKBSvsz64yqJYA4V6U4g79RKhNIMIKlMPkCHQEhJDCmbDSbXiHvalx__cmH8Gqxo4z645Jr2RnEKyEOjdXX1td2lpVWJY7PmmKoouX1L-IHFgobTZI7SaAw9GwzKLGQzP8jxvs4unsLtpdZuBJSsaHy6heydF_gBORyTh9jvBlLdgt9Chk4tXgbyt2NoCVn6c2e506CC56JSKa1G38uLa5SqOIa2xcJwYHR2Zxq6F5XJVvAdNzYnE2kq-Vyce6lBQja9bxvaGLywQ24_rrk6p1xndhaXaLeLF9O1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tX-ihXa6CEot_yCtEXIXMc2CkLe33NWPrmsSQ6svRKMdqGh5UTPGNwfW05dzc0fjH9f7252VUc-ElxS-fZTmiHJlUZTbF26vrHWcYE87f7cmAXw0oU2yU5G1IqaJHF3cucALVAf3Y_Ifk1gHaHkozPlCk2JpJvzT3m7YmiCkGYjfTvhInJ9E8bq3oyMqanzRbWiZmLMQn_iSNsQiOGcVRhAGi2nKCE13HRSL3tSU1t626Rej_jjuCcgW87AzceO2IkhI38TwY33cbTYda4cYQEx1DUo3ndRUuGzIvQkBKx4U0mHg2hAsROV_14_wJ-eonemQw0qEOgXue6G1XL8gQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/enCGKocbt0P0MUFDf-U6Xr7gnDzBsY-57x4CfUJgDyQJn8Hc2s-eZjNNq1tWbXvzKfVabmRfoTUrYcOd-1o_NceApUkMXX50TAr-2tY6gprulBqy8fwD8UP_WyERAsLnp0mRmeLToB5RFxpEUmhGwhLDdGijaX6rGSaxeRXBK5p287ftbxBeUbIT1YbdnPkW7yAT2HNr4aOU0Fmnki8zZpHX6fkScxvxWYLb5191vh-ar0oMvU90QuldVDxgdGu9vJPZ53933vPDmnO7jkn9Su1YNMOiJiaJktztkmIFD7elpEpJROUam4Y6xOQNtPK2RKSXEtMMVYfCPTyP5DEP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sqncJAZI7d6O1j5IjHfdSpnbIgQrE8Ylkd8y9NUBiM4WiunGNu5jCjcfGjbFiuzjfOTO9_IlKGts53AM9M9VK0JJH9fVmHQCxnRxmdDcqveSjf1R0_QvrNspLBVqdu4-DF1Ho0t9-qU99xIloO1SfYJ4DzkGw6czzng-1FyanbNVeBF0e88d1hvLkw6Yan3Z8he2CwAMGxxFqm6Yn2lh-M7EHeF9CfQgbcyCctw82nXXDpedxz9tFU253aMlzoxK0o0nFJzPYLQZjRpgEfH7AbeqyusCKkbYsTNXEDI2dAC1nXoZnBliToExX-S0OduLaLilPUrAQCisIYQYseamMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jm_F3v58PbaipSyCHVIdZTU_Td-Z-HsZRvteyWqiVuAJa-6KylJLMWp1JB_LsUcQ4HPA9f3WARq6lggl8PQAHDJ5d18JvMGqYygXoAJgp34AOrWpszJbmImzblbK7aNhr7yKJmasLrzYYInV-RzCJ6Xw6YWxyBIRjv-wWwtXw3x9A6F5f57SvD8nfEeHKN45hn2WBd_QQsYHKNfmSxvPoWx4gJkdZ3MkyP2TeT1Uej-CELwYCPd0RJ1x1z8x7GGvUyr3XI6IDQhx3TY8okxGIv_qCXGIy0H_eOVPyYIGm0lOljWH8UT_r62b7STS8MKiMblv41lvnpIuUadVJ_pr5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارتش جمهوری اسلامی ایران اعلام کرد در ادامه عملیات موسوم به «صاعقه»، پایگاه‌ها و تاسیسات نظامی مرتبط با آمریکا در بحرین، کویت و اردن را با پهپادهای انتحاری هدف قرار داده است.
روابط عمومی ارتش در بیانیه‌ای مدعی شد در مرحله پانزدهم عملیات «صاعقه»، پهپادهای انتحاری «آشیانه هواپیماها، محل استقرار جنگنده‌ها و مخازن سوخت» در پایگاه شیخ عیسی بحرین را هدف قرار داده‌اند. این بیانیه همچنین از حمله به چند پل ارتباطی در بحرین خبر داده است.
ارتش جمهوری اسلامی ایران پیش‌تر نیز در بیانیه‌ای درباره مرحله چهاردهم این عملیات اعلام کرده بود که «چند پایگاه و تاسیسات نظامی آمریکا در کویت و اردن» هدف حملات پهپادی قرار گرفته‌اند.
بر اساس این ادعا، انبار مهمات نیروهای آمریکایی در اردوگاه العدیری، ساختمان‌های ستادی و انبارهای مهمات پایگاه علی‌السالم در کویت و همچنین مخازن سوخت پایگاه الازرق در اردن هدف قرار گرفته‌اند.
ارتش کویت حمله به چند مرکز نظامی و تاسیسات حیاتی این کشور را تایید کرده است.
ارتش اردن اعلام کرد سامانه‌های پدافند هوایی این کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده بودند، رهگیری و منهدم کرده‌اند. به [ادعای] مقام‌های اردنی، این حملات هیچ تلفات جانی یا خسارت مادی به دنبال نداشته است.
@
VahidHeadline
روابط عمومی سپاه پاسداران انقلاب اسلامی، روز شنبه ۲۶ تیر ماه، با صدور بیانیه‌ای اعلام کرد «اسکله پشتیبانی سوخت ناوگان آمریکا در بندر الاحمدی کویت» را هدف حملات پهپادی و موشکی قرار داده است.
بر اساس این بیانیه، در این عملیات «محل تجمع پرنده‌های جنگی» آمریکا در پایگاه شیخ عیسی و «مرکز داده‌های اطلاعاتی در بحرین با عنوان باتلکو» نیز مورد اصابت قرار گرفته‌اند.
در بخش دیگری از این اطلاعیه آمده است در جریان این حملات، «یک مرکز سیگنالی و مخابراتی آمریکا در کویت» نیز منهدم شده است. سپاه پاسداران در این گزارش بر «کنترل قدرتمندانه تنگه هرمز» تاکید کرد.
پیش از این، نیروی زمینی سپاه پاسداران در بیانیه‌ای ادعا کرده بود، مرکز پشتیبانی نیروهای زمینی آمریکا در منطقه عریفجان کویت را هدف قرار داده و این حمله منجر به کشته شدن چند نظامی در این مرکز شده است.
@
VahidOOnLine
وزارت برق، آب و انرژی‌های تجدیدپذیر کویت، روز شنبه ۲۷ تیرماه، اعلام کرد پس از حمله نیروهای مسلح جمهوری اسلامی به یک نیروگاه تولید برق و آب‌شیرین‌کن در این کشور، آتش‌سوزی در این تاسیسات رخ داده و چند واحد تولید برق در پی این حادثه از مدار خارج شده‌اند.
وزارت برق کویت روز جمعه نیز از خسارت و از کارافتادن یکی دیگر از تاسیسات تولید برق و آب این کشور در اثر حملات جمهوری اسلامی خبر داده بود.
@
VahidOOnLine
ارتش کویت در بیاینیه‌ای اعلام کرد از ساعات اولیه روز شنبه ۲۷ تیرماه، موشک‌های بالستیک و پهپادهای «متخاصم» را در حریم هوایی این کشور شناسایی کرده و آنها را رهگیری و منهدم کرده است.
سرلشکر سعود عبدالعزیز العطوان، سخنگوی وزارت دفاع کویت، در بیانیه‌ای که نیم‌روز شنبه در ایکس منتشر شد اعلام کرد «تجاوز» جمهوری اسلامی همچنان ادامه دارد و شماری از تاسیسات نظامی و امنیتی، همچنین زیرساخت‌های حیاتی و غیرنظامی این کشور را هدف قرار داده است.
به گفته این مقام کویتی، این حملات تاسیسات مربوط به بخش‌های نفت، برق و آب را هدف قرار داده و موجب آتش‌سوزی و وارد آمدن خسارت‌های گسترده به شماری از زیرساخت‌ها شده است.
ارتش کویت افزود نهادهای مسئول عملیات اطفای حریق و تعمیرات را آغاز کرده‌اند و در جریان این عملیات، شماری از نیروهای آتش‌نشانی و کارکنان بخش نفت هنگام انجام وظیفه مجروح شده‌اند و تحت درمان قرار دارند.
در این بیانیه همچنین آمده است رهگیری موشک‌ها و پهپادها باعث سقوط بقایای آنها در چند نقطه و مناطق مسکونی شده و خساراتی به اموال وارد کرده است، اما هیچ تلفات انسانی در این مناطق گزارش نشده است.
ارتش کویت در پایان تاکید کرد نیروهای مسلح این کشور با آمادگی کامل به انجام ماموریت‌های خود ادامه می‌دهند و تمامی اقدامات لازم را برای حفاظت از حاکمیت، امنیت و ثبات کشور در دستور کار دارند.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک مقام امنیتی جمهوری اسلامی نوشت اگر آمریکا به زیرساخت‌های غیرنظامی ایران حمله کند، فرودگاه‌های دبی و ابوظبی و بنادر فجیره و جبل‌علی باید فورا تخلیه شوند.
این مقام امنیتی گفت این هشدار با هدف حفظ جان شهروندان در برابر حملات متقابل جمهوری اسلامی، صادر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77239" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gv6dZnbszm5ZnLudLu0AMeXIuTOQL85dUQ_zieNaHr-M2_p0i5U1k-Cky-2k3WmQIeISIZqBwOZ6x1OZQYnsVQu-a1ItAS4TRGT343aGLwLAyCtgyjLZiRc1F-qydW3M-VbOf_c68Nhu9bo1a4SvWDK8vIPEc39c5IwNPl2v200ggCPZioNkpLjhqfjH5m8VTqaPy4GFShBjhcLogEc7MJRa9IfAmE2tBhRPTh3F47iWbFqSexAS6UwKq1x4IcgLCB7iZZzdiFyQ0rlf_hGY66Y3xlZk4QcpRNlKEO8CwX_L8xi97Fm8CJ-h-vTIpk2TqIUr4BLuW6Ug8xt89Kt9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v4txm2zsO6eUeWjWlCRRY0178-CATLr5dPdOccPcUd2Ac3jTdn4eD7J1NaEEK_V6-DYdXZOBUAojgMiag2q1cGIhrzwpLY-1uyaQ1LiZkzM9tQdXe51UgtFfolhMBJbGwJlly6I74aCGNNIFx29JkG6SJelxay7p_l9GGjUnTCbb2l24yXTojqBHiAaycqrjh7-86QU3paPTBLRhpJqEqGUxuIIEnZS5XSTNj_KolxqXQlPpjzEV1NHw7pk5hUPMEpohqzpKLqZUWurBM21U_gLsYLytqgy8stxPmnN9Uq8k0vXYQqJMMmlhCmmKIJhr_TaDXs6k64x3EDmxV5U2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VYVyTfmHJbNd5AtRMv9PSZ68zm1Ro_FRhijqRPIkHHQRUiq4y3FRhFt_Im77CJbdjmjU9cOpMlnb-oDZ2R0kv0ArZvc8Le83eVHk9PUklWazaYxVLT8uIby4JCCcAI-wQl5-OZTVsV9TBiXK_sDOHmR_0F9f5P2rHgcC-nxnbHFj2VeuYtwRbymhnstnWpXY4Eo5n5qhTnkm_q1vRRRJPLsFmqVHW89WoH0nsrLsrjLzF42MFxOysOMNaR55N3dIRuBVUa8xk6NaM9QjrSARTT5BR5t-cCamP5BEi1pP2TbN1hYncbvj2bvP26JYd65YU8Gmipk8mweBT37I0m-utQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VKsxBlhI3IePxYTfI9hIo-KXuvCeKrWzWgxigI1r657ZWOF-iI1hXMgG9e4c9-iWkwIaPZRI8rQrtLn06BgIOecv6QVjJ-OcnVlHlGmY2qiMrJG_S8uREd6mTcRVQWMdWkhP_6_xSG6_Dj99E-OJuMMPvsHPVtyAIPJU2h-UwgOeUK4K7b0gozlF2YenfZRu-8goWvfymxBG50sNNTNy1ic4NR3RXtFR3rRjMTOm41PgbQdnvOnvuSiMPL1mXDvSovlgLnkPu5ZJo0mvprjairjOHF5FLU-rnb19nmYCNEFzGXLYhGd2UPORmsYeYgd_xTig84qMX5CjK0s2EyN35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sr9cU-YNOa7hyOQqRxmQJo28-bYdeBxTui-JNnoffD-QLvgfWodZn4gE6agS7NuaLvwbPWJ37vKkQlsP5uAmJUMxgFC0dDmzRHXXqFFOh7bLLfOR92UOXRTtmLRZhub9qGnwLO7N9FxtYXIR5GRXMxteyD0imdeyKPBciAhsp0t19Q6vyceCGYJt1XJpe0zjCSrdatFoDSczfJTHhPA1DDi2Z-P3R8cbBDwH3zKHaj6mkKa9K6kls6d6tQRTLfYV2kfRkwwJwgqNpKutCMEhygWjcF0yUBzoL9ApD_A1CvPMdhEGVNmiyC_7jKh-EaKMRno9Rq7mghM15lKaabDUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KsSIdnL6qPI1bCuEdhNJHdxADd5Xsca_SZnVfjRPqnSsrUwCJqZ91fGGxGh2DMImf-X8LfIrv4zJ7r8Ob-_r6eDzEk8VnLZR6JZvJrtwDQuMuDGZPsRiElhdRyjoEm8eQmfjsURXC7ww8oyJZCEg75LjJZ6Rdizl6RrM58AUMWDIoJwn0hFmzn2M5_t4xJNROxhUWZzn7eErSPb-iO3bw4KmxW3d5XsGvBKYtlphVEyU69VIPUdcQlQOAmbVBMFqQqouFOkukTW9rfQDcs9HuqCDFEvd1DwMDYGB-CRDy49ExyFgjqWlNursHojyoPzGuQGvvBVRUcolcCQrU7CXyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم‌زمان با پایان هفتمین شب حملات آمریکا به ایران، مقام‌های جمهوری اسلامی از وارد شدن خسارت به بخشی از زیرساخت‌های حمل‌ونقل، آب و برق استان هرمزگان خبر دادند؛ حملاتی که به گفته مقام‌های محلی، باعث انسداد موقت برخی مسیرهای ارتباطی و اختلال در خدمات‌رسانی شده است.
احمد کرمی‌اسد، رئیس پلیس راهور فراجا، اعلام کرد در پی حملات بامداد شنبه ۲۷ تیر و همچنین حملات چند روز گذشته، بخشی از مسیرهای خروجی استان هرمزگان به سمت استان‌های فارس و کرمان به‌طور موقت مسدود شده است.
به گفته او، پلیس راه و سازمان راهداری در حال تلاش برای بازگشایی دست‌کم یک مسیر عبوری هستند. کرمی‌اسد افزود در حال حاضر تنها یک مسیر فرعی برای تردد خودروهای سواری از بندرعباس به سمت فارس و کرمان فعال است، اما تردد ناوگان سنگین تا اطلاع ثانوی امکان‌پذیر نیست و بازگشایی کامل مسیرها به پایان عملیات ایمن‌سازی و ترمیم زیرساخت‌های آسیب‌دیده بستگی دارد.
استانداری هرمزگان نیز اعلام کرد حملات شب گذشته به چهار نقطه از محورهای ارتباطی این استان خسارت وارد کرده است. بر اساس این اطلاعیه، تونل شهید میرزایی در مسیر رفت و برگشت، پل رودخانه شور در محور بندرعباس–سیرجان و دو پل در محور سه‌راه میناب به سمت رودان هدف حمله قرار گرفته‌اند. استانداری از شهروندان خواسته است تا اطلاع ثانوی از تردد در این مسیر‌ها خودداری کنند.
هم‌زمان، معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از اصابت چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در شهرستان جاسک خبر داد و گفت در پی این حمله، آب چندین روستا قطع شده است. تاکنون گزارشی رسمی درباره میزان خسارت یا تلفات احتمالی این حمله منتشر نشده است.
خبرگزاری تسنیم، نزدیک به سپاه پاسداران، نیز از آسیب دیدن دو پل در محور بندرعباس–رودان و همچنین هدف قرار گرفتن دکل مراقبت دریایی جزیره لارک خبر داده و نوشته است که در این حملات چند نفر کشته یا زخمی شده‌اند، هرچند آمار دقیقی از تلفات ارائه نکرده است.
@
VahidHeadline
مدیرکل ارتباطات هرمزگان اعلام کرد در پی حملات دیشب آمریکا «۱۱۶ دکل مخابراتی» در این استان از مدار خارج شده و ارتباطات مخابراتی در بخش‌هایی از شمال بندرعباس و شهرستان حاجی‌آباد دچار اختلال شده است.
احد قویدل روز شنبه ۲۷ تیر با اعلام این خبر افزود در حال حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان با قطعی مواجه است که علت آن آسیب واردشده به مسیرهای انتقال ارتباطات در محدوده تونل میرزایی است.
بر اساس این گزارش، «مسیر انتقال دیتا که با کمک فیبر نوری از بندرعباس به سمت حاجی‌آباد می‌رود، شب گذشته زمانی که به تونل میرزایی و پل رودخانه شور حمله شد، دچار مشکل شد».
@
VahidHeadline
سخنگوی وزارت بهداشت جمهوری اسلامی اعلام کرد در حملات هوایی آمریکا از ششم تا ۲۷ تیر، دست‌کم ۵۰ نفر کشته و بیش از ۵۰۰ نفر مجروح شده‌اند.
حسین کرمانپور، سخنگوی وزارت بهداشت گفت پنج زن و دو کودک و نوجوان زیر ۱۸ سال در میان جان‌باختگان این حملات قرار دارند.
به گفته او، ۳۲ زن و ۱۸ نوجوان نیز در جریان حملات مجروح شده‌اند.
سخنگوی وزارت بهداشت افزود ۳۷ نفر از مجروحان همچنان در بیمارستان‌ها بستری هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77232" target="_blank">📅 19:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77231">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ui7zhNUqcOA6CtDDUUc83qVieIHj1MmOxrV00_GXb-jqp-_lnj_JjjC4XWlsemCjA9eYV-NTdFgmundQNmweMDlYUXtUXtUX2JcFh-_p4h0V7RXZrx3X4Iw5d5QstHiPphK8blnZjdGtQGQGpaye3qPlUuCtIa4JsPbSe-zQbTmrNpykSUFA2pWHmzWxUf79968KR0iPGw2PwmtQvcyH_txxOHdXAgKdYZUQrY_kloml2RPMEgQJjzpEcGss3Z73Blc2q6Ew648IHkdA6SBfCe_RSzB0M58GumIVcotMqAseiC0-IzuvgVkJSxM7vhP8-VO2FxHPD47MKBhFUrj0Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت آموزش و پرورش اعلام کرد آزمون‌های نهایی پایه‌های یازدهم و دوازدهم در روزهای یکشنبه و دوشنبه، ۲۸ و ۲۹ تیر، در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان برگزار نخواهد شد.
این وزارتخانه روز شنبه ۲۷ تیر دلیل این تصمیم را «استمرار شرایط ناپایدار در جنوب کشور» عنوان کرد و گفت زمان جدید برگزاری این آزمون‌ها متعاقباً اعلام خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77231" target="_blank">📅 19:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cEsdmYC8Pyt9qZi9nYFUCtlP7smAdGHbrz4_K4XgiOOhM3wrJsBR3jHlI8a_aTvt5k1fM0SDz-lEXvtEC-CGX1Mlb4IuwaHYSl3DgHge8Soi5eC1vdjy7fxismgO7EXTXjCz4XHP7eWuEMEVO9ChAAbFzKTGJcz8XwBQjQgDLn-k_70AVLM-NQVdoROFHi-OGRfwb8Fv9y16ex7Oi8RvkDMeZbBx4qGV5fxX5gu3ayZxeBwdaMXzaoW9CD12b6axN2_dJSu7R3FSnAcWSVCJFUUg2qWMOCrwmPDFGE2xJkuVb2rJ5-GEokh5IXmB9bCpHH3Gacprhm0jaDgTIgmmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: پرتاب چند موشک از استان بوشهر
شنبه ۲۷ تیر حدود ساعت ۶:۳۵
Vahid
آپدیت: ساعتی بعد هم کلی پیام و تصویر از امیدیه اومده بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 481K · <a href="https://t.me/VahidOnline/77230" target="_blank">📅 06:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f9ac6ccc3.mp4?token=BrVeeLlSOU20qKwdsydaSjjjSDtXkYgW0BhD-WSjBIh_2HCXAbWvxGJfWreDPDKX8HUug95rwSIxEXRNyVRuzeT97BOoJCUGNXxRDhdPEvOV_O433SA4e0a3eHQ7oQ43FwZp_fav2U91MhwuMjI_jXWdGiJo2MK1_Ou2Rn_F2WGUNqZ3JMPtf2gM7d9oRaQg-ghzWpVtz_5ZoNDjf4qgNLBwxlctpwxPAMfHe7MLz_Heoq3xKM1CqTEPMCB1cKO9iEZUe1abCkfbamOiGaBTCpaPmFhcGAiExt-AlR1HwV9EtOQ6Sg7OCvzPIU8DDX-sEySu0-vT7Kt0jHgP1TTiAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f9ac6ccc3.mp4?token=BrVeeLlSOU20qKwdsydaSjjjSDtXkYgW0BhD-WSjBIh_2HCXAbWvxGJfWreDPDKX8HUug95rwSIxEXRNyVRuzeT97BOoJCUGNXxRDhdPEvOV_O433SA4e0a3eHQ7oQ43FwZp_fav2U91MhwuMjI_jXWdGiJo2MK1_Ou2Rn_F2WGUNqZ3JMPtf2gM7d9oRaQg-ghzWpVtz_5ZoNDjf4qgNLBwxlctpwxPAMfHe7MLz_Heoq3xKM1CqTEPMCB1cKO9iEZUe1abCkfbamOiGaBTCpaPmFhcGAiExt-AlR1HwV9EtOQ6Sg7OCvzPIU8DDX-sEySu0-vT7Kt0jHgP1TTiAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم با انتشار ویدیویی از محل حادثه گزارش داده است که دو پل در محور بندرعباس–رودان هدف حمله آمریکا قرار گرفته و این مسیر آسیب دیده است.
این خبرگزاری می‌گوید که در این حمله شماری کشته و تعدادی نیز زخمی شده‌اند، اما آمار دقیق تلفات و میزان خسارت هنوز اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 474K · <a href="https://t.me/VahidOnline/77229" target="_blank">📅 06:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77228">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A0-uvfE9gjmHiTce_V7R-Toq_hKR8-D740c7uEVK5hc2qysjDqtSko3rJNQ1SJ_A0im669PPRyJiEnu6O1uFLsE9yYbNv6gLw5QpMqrs_vEH9cNqusaPCF9l43h25EvXuKB4DuC9mvWxd_t5za0nMyyMrOwS9ADi4bmdiyCr7gfprXdT4t_NSGqbX3y6bgU_1cpaUeTr6FjSx9OAWiXNY_cd2p_Vs76KFtU2hzciW-KqqmLNYoNSxZF8RcDNHQ93si7oqH4NAQYd0xlpTP8_Lw4C7LaS8DKBB_lwO1zljc6UpDJKqvt44eGlXZjhoGOESdoKbsnhpBTj3ZzhwOmA5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت: نقشه «راه‌های مسدودشده» در نزدیکی تنگه هرمز
شامل دو پل و خروجی تونلی که در حملات هوایی امشب آمریکا هدف قرار گرفتند.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/77228" target="_blank">📅 06:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77227">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c159c5a2e1.mp4?token=FoqnACHPOfNEp53F3K5W6-RgyvZP0dOyVvxYtENyitGfEU4WQT7IEGVYMjCg7i4y5bPff4nSwUimbe8Znc22_rK6F_63KJNRVw7fY1hTK8v_EBf5JsWQu6JMaXLNoXJwveqigfNMVKAVGZhNc6GQYbF2IEyxGFjWZoKI8wShsw7ZkcndTmNhfYU_IhjfTC1iCm3gJLIVUlGWFOUy56xbc730F3EfXAOiOmEFp0qoPYYWeJP7MYVzxb2IqQdQVrLcl7zM685-TwH9Z49I2mTBxllHtNQsg3RkBovmj8alFr0uPzIBNTg9FQxCKfNl0g6JJ9C0fYNj-WqApQs75kUTIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c159c5a2e1.mp4?token=FoqnACHPOfNEp53F3K5W6-RgyvZP0dOyVvxYtENyitGfEU4WQT7IEGVYMjCg7i4y5bPff4nSwUimbe8Znc22_rK6F_63KJNRVw7fY1hTK8v_EBf5JsWQu6JMaXLNoXJwveqigfNMVKAVGZhNc6GQYbF2IEyxGFjWZoKI8wShsw7ZkcndTmNhfYU_IhjfTC1iCm3gJLIVUlGWFOUy56xbc730F3EfXAOiOmEFp0qoPYYWeJP7MYVzxb2IqQdQVrLcl7zM685-TwH9Z49I2mTBxllHtNQsg3RkBovmj8alFr0uPzIBNTg9FQxCKfNl0g6JJ9C0fYNj-WqApQs75kUTIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام تازه‌ترین موج حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — نیروهای آمریکایی در ۱۷ ژوئیه، ساعت ۹:۳۰ شب به وقت شرق آمریکا [۵ صبح به وقت تهران]، به هفتمین شب متوالی حملات علیه ایران پایان دادند.
فرماندهی مرکزی ایالات متحده (سنتکام) تأسیسات نظارتی، زیرساخت‌های لجستیکی نظامی، انبارهای زیرزمینی تسلیحات و توانمندی‌های دریایی را مورد حمله قرار داد. نیروهای آمریکایی علاوه بر دیگر تجهیزات، از جنگنده‌ها، پهپادهای هوایی و ناوهای جنگی استفاده کردند.
سنتکام به دستور فرمانده کل قوا، همچنان ایران را پاسخ‌گو می‌کند و هم‌زمان محاصره دریایی بنادر ایران را به‌طور کامل به اجرا می‌گذارد.
بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه در حال فعالیت‌اند و همچنان هوشیار، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/77227" target="_blank">📅 05:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پیام‌های دریافتی:
انفجار شدید همین الان خرم آباد
خرم آباد لرستان ۴:۵۷ بامداد صدای دو انفجار شدید
سلام وحید انفجار در خرم آباد لرستان خونه لرزید
خرم اباد دوباره صدا اومد ۴:۵۷
خرم آباد دو صداي انفجار پشت سر هم
همین الان دوتا انفجار  شدید خرم اباد
درود وحید جان خرم آباد همین الان دوتا صدای انفجار خیلی زیاد بعید میدونم اینا شلیک موشک باشه
خرم آباد دوتا صدای انفجار
سلام
داداش خرم آباد انفجار نبود
دو مرتبه صدای شلیک موشیک بود
[پیش‌تر پیام‌هایی درباره شلیک از استان بوشهر دریافت کرده بودم.
آپدیت: پس‌تر هم ساعت ۶ از داراب]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77226" target="_blank">📅 05:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mH783LUSnHCZt-7zY_gOO2ZqNwAdHhePusT0LqdAHv5sNFr43YgN1Yr5cZkBa3hzl5imwL4gSTnjoWaGck9-RMmnMGuEsbVa6dAq-DdO5K_1RQmHmPzN0jlKEAPFnJ0VXeRNlqtnZkK-KnimvkIU8CRvNtwSUmvjoRj-d3OOZ2vEt_gPr-fpWM_6Obt2jdVZEJndjojfKIQUCvzDVLs0Xl2nnjkUmRIm57IsRV-Aned4OTK0jm6EmEeiJKzURIjAuUNbz-PGhPXy7snLddQXpGH3vD3M69OcpNDN-WdEx0rzBrfWHOXcaZ04_OJpiLK30fJClHFHN6ffJPfZr3hy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش تسنیم، خبرگزاری وابسته به سپاه، بامداد شنبه، در جریان حملات موشکی آمریکا به جزیره لارک، دکل مرکز کنترل ترافیک دریایی اداره بنادر و دریانوردی این جزیره هدف اصابت قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77225" target="_blank">📅 04:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77224">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S9xu6FmxRW8wnhUAECg-TykrKBloLv-Y4K3MmC5XNPGhYajCtiNpz78W4yXWIQMUIfuxoy402k18FoXR-Lo7dMNSMx_OH32xA57VIVTGnSJ1HTq9I1fmbyCZfgs5LbLkY6EfHJsqUXVxM8ABk4uXBfJ4e7uhTpAI_4LCpNKw6_otYvtfU3UNKUwZdCNMXPzxtqSR4FlgHvrBBajDCEbkM8TxwPhj0gXdETnRYy8fbL2blCFeIF4FWjwrLedO-XbfCPEkOTrJV-Q0D9Gc8IfhCYjaFRLuvkZRTSGH-vu3EoIKIbcy1p4AiN7wKjhdY5bHvIC6dvcXVBKbzT0TFS4vEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است دو نفتکش پس از برخورد با مین در آبراه بین‌المللی تنگه هرمز منفجر شده‌اند.
✅
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران نادرست است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77224" target="_blank">📅 04:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77223">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پیام‌های دریافتی از ۳:۵۰:
بندرعباس دوباره چهارتا انفجار شدید بود
باز داره بندرو میزنه
۴تا انفجار پشت هم
هفت تا بندر
بندرعباس کلی صدای انفجار داره میاد
سلام بندرعباس
از ۳:۴۸ تا ۳:۵۰ حدود هفت بار زدن
همین الان انفجار در قشم 3 انفجار پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77223" target="_blank">📅 03:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77222">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرنگار اکسیوس، ترجمه ماشین
:
🚨
مقام آمریکایی: ایران یک موشک بالستیک به‌سوی یک پایگاه آمریکا در عربستان سعودی شلیک کرد
🚨
چرا اهمیت دارد: این نخستین حمله مستقیم ایران به عربستان سعودی در نزدیک به چهار ماه گذشته است.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77222" target="_blank">📅 02:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77221">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oCbnDv3WopPfvUiqnVPWmdKzavL8trMqLIdfY8piIak2sJCWWZ3gE_MgRLJsL8ArloI9bC4Kdvo-BAgCtz6O8s9vi0XKKTFC-2A5wlEJm1Nyu2amzGslJMYOS2pWG4joO6QMoKWfhZHK9pB64-zV_g-4dgBwYvFq9p0r8JG2O4L03YqFeqKj9t-k4BWSbmXmnGjIdf5S94iBTqNbbyys-ns305EHZIzM0uwwFlfqdyCZjkaLVPgSkFvJonzrUtj-pCwygBV-U8CshilodGU91rFpez6iKdrAUFIyGLtMRN3hwjEiwA9iYoKTULOGFOasiuZwMT2PUCECvf3yKrePsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی با شرح: پل جاده رودان به بندرعباس
شنبه ۲۷ تیر
Vahid
منابع حکومتی:
حملۀ دشمن به ۳ پل و تونل دیگر در هرمزگان
🔹
استانداری هرمزگان: تونل شهید میرزایی در مسیر رفت و برگشت به دلیل حملات دشمن مسدود است.
🔹
پل رودخانۀ شور هم در مسیر بندرعباس به سیرجان مورد حمله هوایی دشمن آمریکا قرار گرفته است.
🔹
همچنین پل محور رفت سه راه‌میناب به‌سمت رودان بعد از دو راهی سرزه مورد حملۀ دشمن واقع شده است.
🔸
مردم از تردد در این مسیرها خودداری کنند. تلاش ها برای ایجاد راه کنار گذر و راه‌های جایگزین در جریان است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77221" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77220">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/daa140a498.mp4?token=pbGlOFwFfBk-upge8DtfP4hZIRNpQaG5vegFrKAHOaXjZN8ol6scMavPx3Ob3LdT7WB-2ZhmBHbCAaOQgcGivOWj3itCoNrPwC0JkZTAxpdE3fr4hoQ43G_1pquVdlzA3GMkvdnegZ5xC3V82VTuWncAXUTEIYLf5FW-jeMEvkBE_4qhq_k-XPAAHU0iSC2EhGJyniYTQl0hvAFEkPpJCeapqPkXOXwGJ4bfq1oT5c4u4zja2br7kjDU_LHLgd1wux1rL39D2anumBLwzmRn4VE1_S3KK_mLpHWTa9N8AX9R_KrQmNGKDvyGCsVm5EG0PY6TbeW0SEevvLfXD_t8EA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/daa140a498.mp4?token=pbGlOFwFfBk-upge8DtfP4hZIRNpQaG5vegFrKAHOaXjZN8ol6scMavPx3Ob3LdT7WB-2ZhmBHbCAaOQgcGivOWj3itCoNrPwC0JkZTAxpdE3fr4hoQ43G_1pquVdlzA3GMkvdnegZ5xC3V82VTuWncAXUTEIYLf5FW-jeMEvkBE_4qhq_k-XPAAHU0iSC2EhGJyniYTQl0hvAFEkPpJCeapqPkXOXwGJ4bfq1oT5c4u4zja2br7kjDU_LHLgd1wux1rL39D2anumBLwzmRn4VE1_S3KK_mLpHWTa9N8AX9R_KrQmNGKDvyGCsVm5EG0PY6TbeW0SEevvLfXD_t8EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
شلیک از خرم‌آباد و زیر ۵ دقیقه بعدش ۲ تا انفجار
وحید جان صدای دو انفجار در خرم‌آباد
زمین کامل لرزید صداش هم مثل ترکیدن بود
تو کانال استان زدن شلیک موشک نمیدونم صحت داره یا نه
خرم آباد زدن
دوتا شد دوبار انفجار ساعت ۲:۱۵ دقیقه خرم آباد
وحید جان خرم آباد ساعت 2:15 وحشتناک زدن
سلام وحید همین الان خرم اباد۲ صدای انفجار اومد
همین الان ساعت 2:15 خرم آباد دوبار صدای انفجار اومد
خرم آباد۲.۱۶دقیقه انفجار
۲ و ۱۵ خرم آباد صدا انفجار اومد
خرم اباد چند بار صدا انفجار اومد
سلام آقا ما خرم آبادیم مارو همین الان دو بار زدن صدا انفجار اومد
سلام همین الان خرم آباد صدای انفجار
سلام ساعت دو پانزده دقیقه خرم آباد صدای دو انفجار
۲:۱۶ صدای انفجار خرم آباد
خرم آباد ساعت ۲:۱۷  دوتای صدای انفجار  اومد
خرم آباد دوتا انفجار پشت سر هم ساعت ۲:۱۴ صبح
همین الان سه بار خرم اباد صدای انفجار اومد
دوتا زدن تو خرم آباد لرستان خیلی سنگین بود
سلام خرم اباد ۳تا انفجار داد ساعت ۲:۱۵صدا خیلی دور احتمالا پادگان امام علی
[ساعت ۳ هم چند پیام دیگر دریافت کردم.]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77220" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62a2ad38dd.mp4?token=WK87LnmMFxTkgqaz-6ydKwVgSkjgNIkKXx547HXAL0OrP0VvqIHNWOJjl31vyPDaY9zjx6tyJWXjP9L-Bn3q97bt0B-AeO1lTObXw-kLIJQXJyfTRiw2-KKdILHG7Pc5OWTnCLrAZdjOEaoWBtLKmCMlKg_SIDpbWxCdBt9Wqk-KT-GwsNyZwR8fJ6ZuAET8OFl76DE1kq1l7NcJc2opgL89lMQJJxO3EopuZamwOBrGJPNYtJEiqgEWJ8FbZ99kuylQqAV_pzZq5WNbUtPfmu1-q00r8dzqnwWCHt6J5lGAWysLc4j8OTssXGHaZUJQCPwLRmk-9vBGKMc6rCAb9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62a2ad38dd.mp4?token=WK87LnmMFxTkgqaz-6ydKwVgSkjgNIkKXx547HXAL0OrP0VvqIHNWOJjl31vyPDaY9zjx6tyJWXjP9L-Bn3q97bt0B-AeO1lTObXw-kLIJQXJyfTRiw2-KKdILHG7Pc5OWTnCLrAZdjOEaoWBtLKmCMlKg_SIDpbWxCdBt9Wqk-KT-GwsNyZwR8fJ6ZuAET8OFl76DE1kq1l7NcJc2opgL89lMQJJxO3EopuZamwOBrGJPNYtJEiqgEWJ8FbZ99kuylQqAV_pzZq5WNbUtPfmu1-q00r8dzqnwWCHt6J5lGAWysLc4j8OTssXGHaZUJQCPwLRmk-9vBGKMc6rCAb9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر پیام‌های دریافتی گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند: 'پل گلوگاه بعد گنو
#بندرعباس
و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
شنبه ۲۷ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77219" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/087c286f67.mp4?token=AbBR1N5xRKsvMf1H7PyrjySMFDlynPn_njKiKWyGVjlBRtXHcBfy7N_K0v368NmJzFDMAbApk9aIA40ozZIRfGLM5sTZNQWD8el1XuydICQYS0eb-mh3V6qRO5vSqr_rNTIlhZD7eiD1qIAjm5pdM1tRh3mQRcE1up0SR1ZrMRdKbd70IMw8f0sQ76vlh0Cy0FdMzusBjxioi37WHhg2yyiiSKTtlBNf8AcBcb-q3Vd8qVZ65kUzAwoS63s1ZkaQjyIGZcUAwEkfpkNI8h576Sd39bqpsvyWRqouwTjT6lKQoIvZXxxb5SehKsU0quApjOCcUfRoPfSt9qphydb3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/087c286f67.mp4?token=AbBR1N5xRKsvMf1H7PyrjySMFDlynPn_njKiKWyGVjlBRtXHcBfy7N_K0v368NmJzFDMAbApk9aIA40ozZIRfGLM5sTZNQWD8el1XuydICQYS0eb-mh3V6qRO5vSqr_rNTIlhZD7eiD1qIAjm5pdM1tRh3mQRcE1up0SR1ZrMRdKbd70IMw8f0sQ76vlh0Cy0FdMzusBjxioi37WHhg2yyiiSKTtlBNf8AcBcb-q3Vd8qVZ65kUzAwoS63s1ZkaQjyIGZcUAwEkfpkNI8h576Sd39bqpsvyWRqouwTjT6lKQoIvZXxxb5SehKsU0quApjOCcUfRoPfSt9qphydb3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از تبریز کلی پیام فرستادند که دو موشک شلیک شده.
و مطابق معمول از ارومیه و خمین و خرم‌آباد زنجان و داراب و... جاهای دیگری هم پیام‌های مشابه میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77218" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77217">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر سه تا
شد پنج تا صدا
بوشهر زدن الان ۲؛۳
بوشهر - دو انفجار مهیب با فاصله ی زمانی ۵ ثانیه ۲:۰۴
سومین انفجار مهیب ۲:۰۵
چهارمین انفجار در فاصله ای دورتر ۲:۰۶
سلام اقا وحید بوشهر ساعت ۲:۰۶ صدای انفجار شنیده شد
وحید جان همین الان بوشهر پایگاه زد صدای سه انفجارپشت سرهم
سلام وحید جان همین الان چغادک را زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77217" target="_blank">📅 02:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سپاه: دو  کشتی نفتکش با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند
منابع حکومتی:
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
🔹
ملت قهرمان و بصیر ایران اسلامی؛
حضور شما در صحنه و حماسه آفرینی خیابانی شما، همانگونه که قائد شهید امت فرمودند سوخت موشک‌های رزمندگان اسلام و دعای شما تضمین پیروزی‌های درخشان آنهاست.
🔹
ساعتی پیش دو فروند کشتی نفتکش که با فریب سازمان‌های جاسوسی آمریکا قصد عبور از مسیر مین گذاری شده جنوب تنگه هرمز را داشتند، منفجر و دچار حریق گسترده شدند.
🔹
نیروی دریایی سپاه با قاطعیت اعلام می‌دارد تنگه هرمز به خاطر شرارت‌های ارتش کودک‌کش آمریکا به شدت ناامن و به طور کامل بسته است و تا زمانی که تجاوزات آمریکای جنایتکار پایان نیابد، امکان صدور کود شیمیایی و حتی یک قطره نفت و گاز از این منطقه وجود ندارد.
🔹
شناورها برای حفظ سرمایه و مهمتر از آن جان خود فریب نخورند و وارد مسیر مین‌گذاری شده نشوند.
و ماالنصر الا من عندالله العزیز الحکیم
پیش‌تر:
🔹
سپاه: لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77216" target="_blank">📅 01:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58eec30bb8.mov?token=aM-hagzwT9jMLtm281V21gukO3LRZdt8hFQCiAFMC4rFQFt0Cgs1WA3Tvt1lm2D1_5LP1sDEDCvgWErsECANNA7fPJMw0B-Y8R9X3XRM3PIL47WC7bKAjgq9itvZ3NheBEeV6RcXgsy2d9kgXgshcfV9lZeebt1dgRsUVATbmR4LSRoLvQSQ87hzm72exizmVitXRx76P-mYSmLLMEltWLrbqXKm_Y9HQDA4Kx7A0WOiS2IQDthcpbIRQpEu79h3iLRmKN54nw9agyH-x_n4X4eDEbDbu_ujD3UPimmVbAqlkHVNbqZOIVtWNwnNsZKGq6OyqLuphLv9YT_RqLLuuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58eec30bb8.mov?token=aM-hagzwT9jMLtm281V21gukO3LRZdt8hFQCiAFMC4rFQFt0Cgs1WA3Tvt1lm2D1_5LP1sDEDCvgWErsECANNA7fPJMw0B-Y8R9X3XRM3PIL47WC7bKAjgq9itvZ3NheBEeV6RcXgsy2d9kgXgshcfV9lZeebt1dgRsUVATbmR4LSRoLvQSQ87hzm72exizmVitXRx76P-mYSmLLMEltWLrbqXKm_Y9HQDA4Kx7A0WOiS2IQDthcpbIRQpEu79h3iLRmKN54nw9agyH-x_n4X4eDEbDbu_ujD3UPimmVbAqlkHVNbqZOIVtWNwnNsZKGq6OyqLuphLv9YT_RqLLuuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پیام‌ها میگن در بندرعباس صدای پرواز جنگنده و انفجار می‌شنوند.:
صدای جنگنده بندر
لرزش و صدا انتجار هم  میاد
وحید جان الان سمت بندر رو زدن
بندر عباس دوتاشو شنیدم
۴ صدای انفجار بندرعباس
سلام سه انفجار بندرعباس
صدا جنگنده هم میاد
بندر داره میزنه
سه بار پشت سر هم
4 صدای انفجار بندرعباس
ساعت ۱:۰۵ صدای انفجار بندرعباس
تا الان دو سه تا دیگه اومد
تک انفجار با صدای کم، شاید بندعباس بوده، توی قشم-طولا حس شد ساعت ۱:۰۸
صدای جنگنده بندرعباس
بندرعباس ٥ تا انفجار جنگنده خيلى پايينه
بندرعباس به شدت صدای جنگنده 1.11
ساعت 1:11  صدای جنگنده اسمان بندرعباس ارتفاع پایین
صدای جنگنده میومد بعد از ۲۰ ثانیه صدای انفجار اومد بندرعباس
سایت موشکی خورگو بندرعباس رو‌ زدن ۳تا انفجار بزرگ با جنگده
بندرعباس ساعت ۱:۰۷ صدای انفجار شنیده شد
🔄
این بار پیام‌ها رگباری بودند نه پراکنده:
بندرعباس همین الان انفجار وحشتناک
وحید جان اینجا رو وحشتناک زد بندرعباس
بندرعباس ساعت 01:16 صدای انفجار شدید
انفجار سنگین منطقه ۴ بندرعباس ۰۱:۱۶
بندرعباس دوتا انفجار شدید الان به جز دوتای قبلی
سلام شبتون بخیر آقا وحید
الان صدای انفجار بدی آمد طوری که پنجره ها لرزید
همش صدای جنگنده تو اسمانه
بندر عباس همین الان چند صدای انفجار ۱:۱۵
سلام بندرعباس همین الان صدای یه انفجار شدید خیلی نزدیک بود که همچی لرزید
😭
این شدیدترین صدایی بود که بعد از آتش بس شنیدم
زددد الان زد بندرعباس
سلام وحید جان همین الان ساعت ۱:۱۶ دقیقه ی انفجار شدید  بندرعباس نزدیک پیامبراعظم که خونه ها لرزید
سلام وحید بندرعباس ساعت ۱:۱۶ دوتا انفجار شدید صدای جنگنده هم خیلی میاد
بندرعباس اول صدای جنگنده میاد بعدش انفجار ده دقیقه پیش اینا سه تا با هم زدن چهارمی رو با فاصله ولی شدت خیلی بیشتر زدن چند دقیقه بعد دوباره صدای جنگنده و پنجمی
الانم دوباره داره صدای جنگنده میاد یه بیست سی ثانیه دیگه میزنن
بندرعباس الان بالای ده دقیقه چند جنگنده روی شهر می چرخند
🔄
همین الان ساعت ۱:۱۹ زد بندرعباس
بندرو رگباری میزنهه
برای بار نمیدونم چندم صدای انفجار
انفجار دوباره پشت هم بندر عباس
بندرعباس الان زد وحشتناک
همین الان ۱:۱۹ دوتا صدای انفجار شرق بندرعباس
زدن وحید بندرعباس ۱و ۲۰
الان دو تا صدا انفجار اومد
سلام وحید جان دوباره صدای انفجار دوتا
بندرعباس ۱:۲۰ دقیقه صدای خیلی زیاد انفجار
قشم همین الان صدا انفجار شدید اومد
سلام  وحید بندرعباس ۱:۲۰ فرودگاه انفجار بزرگ از سمت فرودگاه
بندرعباس الان ۱:۱۹ دقیقه صدای انفجار بلند اومد. قبلش هم جنگنده داشت می‌چرخید.
بندرعباس دوباره زدن
فک کنم تپه الله اکبر دوباره
خیلی شدید بود از دیشب هم بسیار بلندتر 1:16
زدن وحید بندرعباس ۱و ۲۰ پایگاه هوایی
همین الان سمت مسکن مهر طرفای بلوار هرمزو زدن صدای خیلییی شدیدی داشت خونه لرزید
سلام آقا وحید من از داراب فارس پیام میدم تو آسمون داراب هم امشب مدام صدای جنگنده میاد
من بندرعباسم صدای بدی اومد ما محدوده بهشت بندر هستیم
وحید صدای جنگنده در بندرعباس قطع نمیشه خیلی پایینه پشت سر هم صدای جنگنده
دکل مخابرات رو تپه الله اکبر رو امشب یه موشک خورد توش همین الان
برعکس دیشب که ۵تا زدن
منابع حکومتی:
استانداری هرمزگان: در ساعت ۰۱:۲۰ نقطه‌ای در بندرعباس مورد حملۀ نظامی دشمن آمریکایی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/77215" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77214">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3939b6f6d.mp4?token=UX38Dz8yaWZdA2e9wcNtmV5SgeYKQ5bgJbSDbxglwN6KQmLG4iZPLCtEIKuaJMYhwzWkgiJIe-XHrrDlUxDPY9zxpqPcAjzbeFTD29k1x5hYYzxCaifq_O11-EWGkPbXN9EXBGLV7DMHpZHJaHI2xIZO_i889Ze4XkwxutkqvnKqRykWwBkCVq_Hw9Y9xIKcbO7fKZF3Dk78etKPHCYqSv6XhreKiuLnyosL_z9tmGrD6Mb-e7eM893-AoF16dxIAVDDmgO3qXoWRJ9CX2lmmzvfY3AhL9Pp-qyAWrpGBs6S9ANqz-mo4TX529ouxl4kXoId2z7CvRBPjrtcNjhaRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3939b6f6d.mp4?token=UX38Dz8yaWZdA2e9wcNtmV5SgeYKQ5bgJbSDbxglwN6KQmLG4iZPLCtEIKuaJMYhwzWkgiJIe-XHrrDlUxDPY9zxpqPcAjzbeFTD29k1x5hYYzxCaifq_O11-EWGkPbXN9EXBGLV7DMHpZHJaHI2xIZO_i889Ze4XkwxutkqvnKqRykWwBkCVq_Hw9Y9xIKcbO7fKZF3Dk78etKPHCYqSv6XhreKiuLnyosL_z9tmGrD6Mb-e7eM893-AoF16dxIAVDDmgO3qXoWRJ9CX2lmmzvfY3AhL9Pp-qyAWrpGBs6S9ANqz-mo4TX529ouxl4kXoId2z7CvRBPjrtcNjhaRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: سمت نیروی هوایی
#لار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77214" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77213">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O33OTY0AS8O-l4_4vg7ksqWX567gpiHIa1roFUcTZymyh1Dfk1JRcQTDfdeLJbN0X8rZm8LlB2eQrfpg2xdYK8bLiqhBz8DgdGQXdGRONqtbEJz48etcPQ1n7RdsYmDge-a1fz5kJHGE7TFGoq75yFrNdRzQC0PN6gTea7l1tI_OljwYfJUYBoqB-XxbkxNiu98tcRlvgTsHtOU0sdm38ZvN_CbNS6pW88DJthyA1Khvjjdg-vCTaHAa_BGGgiVqULjhlpkZQXGkZmANVbTvJ13TIiMx5QM-iblv_5icQg_JdG7v9ewBrkjCtkR9av_4z0PU-9gM0BVsghQnwkH3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
۱۲:۳۰ اهواز رو زدن
صدای انفجار ولی زیاد نزدیک نبود
اهواز رو زدن 00:31
اهواز صدای انفجار ۱۲:۲۹
ساعت  ۰۰٫۳۰  اهواز  ۲ تا انفجار  پشت سر هم
منابع حکومتی:
معاون امنیتی انتظامی استانداری خوزستان: دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77213" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77212">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=pwvldNnS1NTSnAGaOEjqnUpTS7E-Dtbl9J6RFx7NrDsqxrOHZZx5QIOfNxGsgYUW_uKYY7gT6vsPDZln04CGWTXPpAc4-1H1F6kAT75m128PsyzjbrucSJ0ttE2Nuxo5pEX_cjhAkwmVUMTwAe30g4vPBad05plm7E-vO1sXWIFwqQxJrrqweSyq7-kJRtrdr7W6W3fzvNMPbUlMQQP9LPEn4PmDBFYuVeusSQXcr8-PoHmsxXjrtGHp-bl2Lgi5sOwpe8-b0LTVOURfOyJmNKdnIKHwPqnp5de_x1ikQRgh7YwXOuFl_fyCaHahk5kBrffAZZBdE7BxbQTT78Zguw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=pwvldNnS1NTSnAGaOEjqnUpTS7E-Dtbl9J6RFx7NrDsqxrOHZZx5QIOfNxGsgYUW_uKYY7gT6vsPDZln04CGWTXPpAc4-1H1F6kAT75m128PsyzjbrucSJ0ttE2Nuxo5pEX_cjhAkwmVUMTwAe30g4vPBad05plm7E-vO1sXWIFwqQxJrrqweSyq7-kJRtrdr7W6W3fzvNMPbUlMQQP9LPEn4PmDBFYuVeusSQXcr8-PoHmsxXjrtGHp-bl2Lgi5sOwpe8-b0LTVOURfOyJmNKdnIKHwPqnp5de_x1ikQRgh7YwXOuFl_fyCaHahk5kBrffAZZBdE7BxbQTT78Zguw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
وحید یزد الان 12:30صدای انفجار میاد
5 مرتبه صدا اومد
من تفت از یزد هستم
تا الان ۵ تا صدای انفجار شنیدم ولی دوره
۵ انفجار شدید پارک کوهستان یزد
یزد الان ساعت ۱۲ و نیم چندین صدای انفجار
وحید جان یزدو بد زدن چهار بار
سلام وحید دارن یزدو میزنن
وحید یزد چند تا صدای انفجار اومد ۱۲:۳۰
صدای ۵ انفجار پیاپی در یزد ۱۲:۲۹ تا ۱۲:۳۰ بامداد
من 4 تا صدا شنیدم
یزد ساعت ۱۲:۳۰
بیش از سه بار صدای انفجار اومد و زمین لرزید
وحید یزد رو زدن، ۴ تاشو من شنیدم، اخریش شدیدتر بود.
آپدیت:
منابع حکومتی:
معاون استاندار یزد: حملات آمریکا به خارج از شهر یزد بود
🔹
نیمه شب با حمله جنگنده‌های آمریکایی، صدای پنج انفجار در خارج از شهر یزد شنیده شد.
🔹
پنج موشک در حاشیه شهر اصابت داشته که تاکنون هیچ‌گونه خسارت جانی در پی نداشته است.
🔹
اکنون آرامش برقرار شده و دیگر صدای جنگنده‌های متخاصم شنیده نمی‌شود و آسمان یزد کاملاً امن است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77212" target="_blank">📅 00:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=fp1iFweeZOP7keO11NhAyLZfEl8_XeZBCSzj-DemLXl1wTTbv_qAELuOKw6TPOlOb-1wscDJDH0CUBSAElbiipm_ImwnVw5z0qEZWmuy_KTlRrpBVgAgmr9rrh28IAwWSRLFP89EPZz1j1clcnatsK83I1yQ9yQUlZ5nrHt-fGurTHtopEDV2mLbhgVkE9GzzEd2_PFVOg_NQKMKW5kd1u0h0i4NfRs-CH-g426-RldKXsD-dC0CsgqbIn5ikNkHm4iHx3cCxh7EbBzccPIMbmWRMHenEILZGkSACiNHWLnbD6Od16oE93nVKb5jgsh9WdA13LutPIvx1wHs3RfS_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=fp1iFweeZOP7keO11NhAyLZfEl8_XeZBCSzj-DemLXl1wTTbv_qAELuOKw6TPOlOb-1wscDJDH0CUBSAElbiipm_ImwnVw5z0qEZWmuy_KTlRrpBVgAgmr9rrh28IAwWSRLFP89EPZz1j1clcnatsK83I1yQ9yQUlZ5nrHt-fGurTHtopEDV2mLbhgVkE9GzzEd2_PFVOg_NQKMKW5kd1u0h0i4NfRs-CH-g426-RldKXsD-dC0CsgqbIn5ikNkHm4iHx3cCxh7EbBzccPIMbmWRMHenEILZGkSACiNHWLnbD6Od16oE93nVKb5jgsh9WdA13LutPIvx1wHs3RfS_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'حمله به سایت موشکی در جاده گراش
#لار
'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77211" target="_blank">📅 00:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
پیام ساعت ۰۰:۰۷: لار داره پشت سر هم صدای انفجار میاد
سمت جاده گراش
حدود ۱۴ تا صدای انفجار
سلام اقا وحید الان لار دوبار صدای وحشتناکی اومد فک کنم سایت موشکی رو زدن
سایت موشکی لار [رو ] ‌بیشتر از ۱۰بار زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77210" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
سنتکام امروز ساعت ۳ بعدازظهر به وقت شرق آمریکا [۲۲:۳۰ به وقت تهران]، برای هفتمین شب متوالی دور تازه‌ای از حملات علیه ایران را آغاز کرد. این حملات به دستور فرمانده کل قوا و با هدف ادامه تضعیف توانمندی‌های نظامی ایران انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77209" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ae40102b43.mp4?token=AAQlorqTCpS8b5BlKw9yCVzhFOdI3b6t4n1l_DEM5hQszVtW4TaPdYzK-8BNqt0a0QIYtyFEYqr3rJPFi2FTXQE44u3z9TfhNwexULOmWKR8ba4B3GR21FSp4M76HlDABNWcuQQBBhn5gO1s7aM-5BkzaM7GHB5Oww_lw67cwsHjT3ny4KYOJESQPUkXUhTO5ktVBs5q9A9lgrEPwb9GocE56X1nHtVn288JhvfQPPc4gOtzUpmSRJsIGIKJjHqAOFm-RiOpF2MUtNr-ySzC38ibRxm4yzzR3IlUQQSHNWOtJLMyF8HSAcGi7nKnrW5RgkB_aOXuFZP53JCkxfs9og" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ae40102b43.mp4?token=AAQlorqTCpS8b5BlKw9yCVzhFOdI3b6t4n1l_DEM5hQszVtW4TaPdYzK-8BNqt0a0QIYtyFEYqr3rJPFi2FTXQE44u3z9TfhNwexULOmWKR8ba4B3GR21FSp4M76HlDABNWcuQQBBhn5gO1s7aM-5BkzaM7GHB5Oww_lw67cwsHjT3ny4KYOJESQPUkXUhTO5ktVBs5q9A9lgrEPwb9GocE56X1nHtVn288JhvfQPPc4gOtzUpmSRJsIGIKJjHqAOFm-RiOpF2MUtNr-ySzC38ibRxm4yzzR3IlUQQSHNWOtJLMyF8HSAcGi7nKnrW5RgkB_aOXuFZP53JCkxfs9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، بهمن ۱۳۸۹:
حکومت وراثتی بود. یکی می‌مرد، یکی را به جای خودش معین می‌کرد. مردم هیچ نقشی نداشتند؛ می‌خواستند، نمی‌خواستند، ناچار باید قبول می‌کردند
hafezeh_tarikhi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/77208" target="_blank">📅 23:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d59582925b.mp4?token=dg7Pa5YaLDc-yBP-Ro3sA7IwkH96LKItck3-FqL5NBoUJsp2pokRIDTnf_m8-indjS9PGgXIS26noVP1OxnkUAmiNBc3ZCAa44s6igeYBkl8FD4OtwUHbQEMAWAb55fwlcjMlKoIcNzrUW3KBseYfvTw5Bf0v7BkuLHQW0zD1sXZZIuB0SjBJHR_L5Qmn1Y2DPVVuWA2sNwteZqm2iQbVrFVXcbwRHXTMboxP3G7eLHmXYwsRCXZl2VSgI_wHIARZTIFY6pUp9tofLCrS9Q9msloEoGRV0ezlUsUtgg1ApAuvdGH1hVHh_4xZPSw5osqXPjajDAXWZagsdccrlSdFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d59582925b.mp4?token=dg7Pa5YaLDc-yBP-Ro3sA7IwkH96LKItck3-FqL5NBoUJsp2pokRIDTnf_m8-indjS9PGgXIS26noVP1OxnkUAmiNBc3ZCAa44s6igeYBkl8FD4OtwUHbQEMAWAb55fwlcjMlKoIcNzrUW3KBseYfvTw5Bf0v7BkuLHQW0zD1sXZZIuB0SjBJHR_L5Qmn1Y2DPVVuWA2sNwteZqm2iQbVrFVXcbwRHXTMboxP3G7eLHmXYwsRCXZl2VSgI_wHIARZTIFY6pUp9tofLCrS9Q9msloEoGRV0ezlUsUtgg1ApAuvdGH1hVHh_4xZPSw5osqXPjajDAXWZagsdccrlSdFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، در صدا و سیما گفت: اگر آمریکا دو سه روز دیگر به حملات خود ادامه دهند، وارد فاز تهاجم و انهدام کامل خواهیم شد و هیچ مرز سیاسی‌ای برای حملات خود نمی‌شناسیم.
او ادامه داد سیاست «هم جنگ، هم مذاکره» به طور کامل پایان یافته و اکنون راهبرد ما بر پایه بازدارندگی، مقابله به مثل قاطع و پاسخ «چشم در برابر چشم» به حملات موشکی دشمن استوار است و ما موشک در دهان دشمن می‌زنیم.
@
VahidOOnLine
مشاور نظامی رهبر جمهوری اسلامی می‌گوید هم اسماً و هم عملاً چیزی به نام تفاهم‌نامۀ اسلام‌آباد دیگر وجود ندارد.
محسن رضایی گفت که پیشبینی می‌کند که اگر مذاکرات شروع شود طرف مقابل قصد دارد «اصلاحاتی در متن ایجاد کند و در واقع تفاهم‌نامۀ جدیدی بنویسند». او در ادامه گفت که اوضاع تغییر کرده و چنین چیزی ممکن نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/77207" target="_blank">📅 23:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c044eb7a7e.mp4?token=vJqZcmHUSO1Wimo7KUWZy7Zl9yMNW7bBZ5LnPHFaJIkpJ_Y3ZpYu2jS2EqEejcwXaJ9ut7o7dPH04ajHrOYPrvsMdXUVnPTan2s9nGn6_mKevF1mTZRl0G7TKGuOBbrAdZzLqwnhgJnAIFlpYLjZq-Pzu7jDVlaYpjKF6jTNFtRa8EJG8HB3G2gIyIjG9wfVaCrZBqLYo7IRBZVVe1YUVnkKET-ggD9OVs6bsa3EuNpEfe-rLO2J3bHOzUM-mU0K7aueOx9fBjiUnOA-BvkRtBnQ1NrLvoEvv_O27tdNwWb8bKP-gouBC1U70lL4dB6w0Hp5Ffx8nQSsX34LW3peZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c044eb7a7e.mp4?token=vJqZcmHUSO1Wimo7KUWZy7Zl9yMNW7bBZ5LnPHFaJIkpJ_Y3ZpYu2jS2EqEejcwXaJ9ut7o7dPH04ajHrOYPrvsMdXUVnPTan2s9nGn6_mKevF1mTZRl0G7TKGuOBbrAdZzLqwnhgJnAIFlpYLjZq-Pzu7jDVlaYpjKF6jTNFtRa8EJG8HB3G2gIyIjG9wfVaCrZBqLYo7IRBZVVe1YUVnkKET-ggD9OVs6bsa3EuNpEfe-rLO2J3bHOzUM-mU0K7aueOx9fBjiUnOA-BvkRtBnQ1NrLvoEvv_O27tdNwWb8bKP-gouBC1U70lL4dB6w0Hp5Ffx8nQSsX34LW3peZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار ویدئویی‌هایی از قرارگاه سپاه پاسداران در راسک نشان می‌دهد که در پی حمله هوایی آمریکا، سقف یک سوله بزرگ در این مجموعه به شدت آسیب دیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/77206" target="_blank">📅 20:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HP400d-Kd__EfwPoWXQ2OLTdJdjcnxEnhtIZnnzKkkJ7ChDZqutRLGvf_ycJz5MELXkxVBiBFAQUauRfX-0LwVAV0B5CWBgmCOpGtszbSyRG8cRRgAd8tasEiKjkS1MIkus3RpGyFXfcaxP2_DQWKTXndTrjrd3dLxTnjH61Z6bemer_M0iFDzTVsntx9p-Ju27pR56pd2et0e8NbIwuZ_AkYbR-JYQkN0F0cVB0tK306gsl3ToOQhH0pj-sE-OBXnI0_4ubRi_X9Q33jHdjMTSmM0PmGPTa1kiM4zbWG39ugqv6N1b7pUeqcJ6BJe8nLYeHdhSbHLpih5wj-Lpzjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس روز جمعه به نقل از سه مقام آمریکایی و اسرائیلی خبر داد دولت دونالد ترامپ به اسرائیل اطلاع داده که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند دیگر هواپیمای سوخت‌رسان را به این کشور اعزام می‌کند.
بر اساس این گزارش، سه‌شنبه این هفته در نشست «اتاق وضعیت» کاخ سفید، چندین طرح جدید نظامی به رئیس‌جمهور آمریکا، ارائه شد و او در حال بررسی اجرای یک «حمله گسترده» علیه ایران است؛ حمله‌ای که دامنه آن از حملات کنونی در اطراف تنگه هرمز «فراتر» خواهد رفت.
اکسیوس می‌گوید «زیرساخت‌های ایران مانند نیروگاه‌های برق، انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف دفن هرچه عمیق‌تر ذخایر اورانیوم غنی‌شده، و همچنین بمباران سایت زیرزمینی کوه کلنگ‌گزلا که گمان می‌رود یک تأسیسات هسته‌ای در حال ساخت باشد»، ازجمله گزینه‌های در حال بررسی در دولت آمریکا است.
دونالد ترامپ روز ۲۲ تیر در یک مصاحبه گفته بود که ارتش آمریکا احتمالاً به زودی به کوه کلنگ حمله خواهد کرد.
گزارش اکسیوس در عین حال یادآوری می‌کند که ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد آماده تشدید جنگ باشد تا خسارتی در حدی به ایران وارد شود تا جمهوری اسلامی تنگه هرمز را باز کند و خواسته‌های او دربارهٔ برنامه هسته‌ای ایران را بپذیرد.
در حال حاضر، ایالات متحده حدود ۳۰ فروند هواپیمای سوخت‌رسان نظامی در فرودگاه بین‌المللی بن‌گوریون در نزدیکی تل‌آویو و تقریباً همین تعداد نیز در فرودگاه رامون در جنوب اسرائیل مستقر کرده است.
مقام‌های اسرائیلی به اکسیوس گفته‌اند آمریکا قصد دارد طی روزهای آینده چند ده فروند هواپیمای سوخت‌رسان دیگر نیز به اسرائیل اعزام کند تا شمار این هواپیماها به سطحی برسد که در آغاز جنگ ۴۰ روزه وجود داشت.
به گفته این مقام‌ها، ارتش آمریکا ترجیح می‌دهد هواپیماهای سوخت‌رسان خود را از فرودگاه بن‌گوریون به پرواز درآورد، زیرا سایر پایگاه‌های هوایی منطقه در برابر حملات ایران آسیب‌پذیرتر هستند و امنیت کمتری برای هواپیماهای آمریکایی دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/77205" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3253e7746f.mp4?token=gFhnCU_u5njXo6vMOq8I1P0KLQl996Sd0lLayYuxxytdfHLcbd2nsYzngwpY9SYlUgh4lxXhJUriU5lRD7Ei2Bt9u62XxHNKybkLJKYQybKpgH0CflWP2tH0i7cil9_leqK-ZZL0QQ-o2vF9bVd3KBF1rzLVBdtLIjzhX66h9P9JOUDrSuHSW92lH4Eys8zGNdr9pbViS_SVG0I5ITZTGC-QW5hATJg9cYnyS_izPmkcIgeMiAsl6YUv95KOHepW6xMFcCW8EzfzeNo5QnxDOGCL4hUZGU0KdHqseOHhBKjp6J-zqgeZTKsyExVLGQy9g61P3W7QmZMGpi9_hk3Ppw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3253e7746f.mp4?token=gFhnCU_u5njXo6vMOq8I1P0KLQl996Sd0lLayYuxxytdfHLcbd2nsYzngwpY9SYlUgh4lxXhJUriU5lRD7Ei2Bt9u62XxHNKybkLJKYQybKpgH0CflWP2tH0i7cil9_leqK-ZZL0QQ-o2vF9bVd3KBF1rzLVBdtLIjzhX66h9P9JOUDrSuHSW92lH4Eys8zGNdr9pbViS_SVG0I5ITZTGC-QW5hATJg9cYnyS_izPmkcIgeMiAsl6YUv95KOHepW6xMFcCW8EzfzeNo5QnxDOGCL4hUZGU0KdHqseOHhBKjp6J-zqgeZTKsyExVLGQy9g61P3W7QmZMGpi9_hk3Ppw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا: برج مراقبت چابهار را منهدم کردیم چون سپاه
...
پست سنتکام ترجمه ماشین:
در ۱۶ ژوئیه، نیروهای آمریکایی برج مراقبت بندر شهید کلانتری چابهار را با موفقیت منهدم کردند. این برج بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود که سپاه پاسداران انقلاب اسلامی دهه‌ها از آن برای ردیابی و هدف قرار دادن کشتی‌های تجاری عبوری از تنگه هرمز استفاده می‌کرد.
انهدام این برج مستقیماً توانایی سپاه پاسداران برای هماهنگی حملات علیه خدمه غیرنظامی بی‌گناه را تضعیف می‌کند. افزون بر این، این حمله از آزادی کشتیرانی در آب‌های منطقه برای همه شناورها محافظت می‌کند، به‌جز کشتی‌هایی که در تلاش‌اند محاصره دریایی جاری آمریکا علیه ایران را نقض کنند.
CENTCOM
پیش‌تر پیت هگست، وزیر جنگ آمریکا،
این تصویر دریافتی
رو بدون هیچ توضیحی
توییت کرده بود
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77204" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XgrZ6hbOERyTNBBswGMDiLJXkWWDoDAU35GJxAHbN5rILwVdoNabY0lt1D1sxuAW40Rv5IMLOPkscsQreOkjVexnRN98fuSesrMAqOdPvrcxgbUHy6FPYvT9dVBhYQZj_7hVXkXIJXzWq4Na9PKLU8uHU59i7hhAklD6ETOEnanXoBzm0Ry_mQiHPDlAAiqzIu85FSHEbRFXy3tFhmIifrYUrO419TKp6NL-5FWRZvUu7T7U1MGXF3QyxV_SApmtXsYxEM8uvkl7XbiEzCUaElzBDwzgqfv6jh0VLOoQgKyFwKuD2_X5PyVix_rXfAY96qy1CgRBBqMsyy6FcmQFJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: "پل و خط تخریب شده دیشب ایستگاه انشعاب راه‌آهن
#بندرعباس
"
هم‌زمان با حملات آمریکا در بامداد جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77203" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77194">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fkejMNKNWMJ0jSgngEiChhcoXaYBWLgmz62tnH0AL1AJYGBVBcx-S-JvOoqlnfIqGvDvqm5SwvlgXDpShf1mLxa1W_6dVsrG6SPOOowmTXVB-9mkDGnWOrdtYRZsPbyQaBG3Wp29Dk8DnvUsTVr53A4n36WwTm-78Y-o4oA7VqFvgwtgLfzHbvkmYsQWZxtvI6Ro8PguHNy5MKLkwVFCYLBFBAA2NwWUMmXUIpIaDmDiQwgZrzYyvIXUmiGRnor8v2zPSJHdO2f2UqkZ7QZzKschpRxmKq8PSLhBx9iyJUXI2iBP8l_W3bDwEAnFqzaIFh1SGIV_rc1UQyBazOaPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t6BJyyCrnCBZwPJnODGMqhv07MjfDunljw688tz_3BjiJqwJhez6bYvuxXpVZs8q_SZWTPfHBzvsUzzcQhILDHyb0O-QjD33RyeVHl3ugmcXM_arUIv9uD6OfazzczzqbUprVsOY1N3XGF75xLUYVXpASdHnLRku2K-Lw5wxOWgbJ_Ey28AkfrhorFfajcWnMH7LmGcLXMWfbtKRX9JpCvscZoRMGiVJg4c_z-OjK7JpDrnJ6tzlsZ71GXb6h1-OXKHHkxzE5wMr64XAKeK4BGUuWAJaaRbNMMQj1AB_ht6EHwbggnab1xSyaxd3bLLAMU81tl4JhUevZUvZt6_NKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gw_-jTBtn4oQ_OGNajA28gugXxe8CiCw8N32n4cmx1w_rjGVnlxId5k9DbPLzW9R5MKt4ibWHX6gnwoOnz_GdW-ySdX12VeoqVgQz2tlww3cxD6zEgJmJABP5phVdRJZi5U0tm2qXPM4L5NWDBLa9rHRsPQiH2x84V7S3VcksVby8ZxKDvqKx0paSDvPaJxYjrP8NX6KbgCRWPhqqOFMwo6MmA0iyxQXnUdA8taN_-SMZrLCuz9a1sBl20PZImf-j0WOa3ku63Ts7BoT71WQI9JwlRcGe3TCCbSbWm0xi5-QrWetZE1XLgVEmdv6CIyJSwPM6dcUN0Mrj_yZjFjWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZLFT0wrx1FZpw8tAY1M-rwyIps6OSJ95BUN1g3YB0I8mNgI152V26zXl7RgmnuhCnJ8dmBPo0Fprfhh5L-qWBI73AjbFLEh9kmPzmEUo_6tdk7PmYXLsVDCkXeAadGXPBPHIG34ybDTdUcizitmR6sXAXTNhCYdcajCXJ-fgg1jPMflac8SWFcxxShV74NkpjXKJeG1YOE4Y5OR2jTGVlkInIWwkb5wQBIhYRNqcp-h_JDLbuGFoeXWBGVhO8KzSM1viZkIbl2YOv0iuJ1nQr5EMCS3X1ooiO_-LqkNBlx8U7eBTHiNYDnExRdYzFwLdpjPLvj5_4yBorjMnCJFpAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fg6mIuemZUihDG9pSlEdu05v7pkZMG2-o7sU-d-hXbE48vmCjvjCaJwz6jGeaplJK04y3_xhAOH2Uf8w0_ooo4e_UkCDfxM_CN9xEMFi5wxw6K3g_Vqkm9yLTr_y-HxqtNNU3f2XUESK1D6_rbK4eFD7PiyIbdnfH1LhtgdCAnldaU3tGCLiR3pXIr5Gkq8MOgLuarSYGbHwfwmJ4xecjO4sf1Ov9NdraAF2ZW88WN3KQ2eR5XRlCGlnR_wvTr0yBOtS8Lq13lBwCpY6p0JGOmtmhnygw_Ny4qOp83uHGbj-gtwZ-SoaZ38y1-1DiBjPQZzm08juIaB10K4dbbjG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pnx9EuIcnQv4jTFm3jF1FHz7vSXcuoSn9WW4CEvvPQ6VDYmoszz_4zo_IrKJhzwGor3QJb2qcmV-v5EoBnK_H2WA2foIxA-iFwWKKBbraFzePTYFkBFF09tB2XELXy6Frws6wKRA-L6A6FUt1lVB4sgpZuF3HWJRpmNT_GFb9KKPCFeu1HxMZQ_NEIJa5J4OaBcqX5lcWVuClrZ9WNF7Du145Y-JmbJV2SzPl2LbD2Vn85XANDAuyQxui5Yeme4SfblOw9AZbKKb8SHfYzHfa92EXIQsvOMnBxxqh6adhGPtMKYSxK2MpzFauTjRofl-vEDkE8_sLWIFLc37jgbyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pka9QfEF7VWwqz1EWNEZ_JwXaiC0Xu2EB_fgAyXKwm6466lNnm7hFYkdHusW-ttC0VN-32yEK2hjCPTmKg1rftopDMgKh694ZbNaRag3HSPbLJXqxIsMod4HZ4x1T__L2V-hScrPIFrEMGu-nol88puq-TCynU2oROH6yzxHhjyCqrMsWRcTFiHtBWu9-JGztC1gTVisIb6uLRqbX9TnPgjkVK1HuyND79xvYS51aNT8rUtrTVdg48cAwvs1BogrfaDnus-kt2qa1d_Uae8D_sB14IQy16ylVYDDZpotRwr_jZ5tjRGorZCQlrtYR91mNwUzV_QJi0C6ryFSePnzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M-kxDPIMTkfxEm-ho_Tsuck6tCY8U9ttHlNF2MbQBJsxFZSB0NjdMq6w28n8M3Gp2XKDC_uzoEnniDBP2d2-Nn6EJ_U3XYjM3_ktKYosM_6j80e7Sphr7qAeCgNeSRpaJqBvXBjfD-MXykEdqUssXBFskCb6N7bjk5vkJAI1uhKW1fxkaNAPZENaSdMGAQdLtjacd7tEYhvDbWFWbnNVf9H0-QRuGF6nJcmBtue5OIFvU2Sb42VHvldyIs0c9P2X3SAmgZ_EHwGKaBfYF7ov-YgpqfuMkN2DPEwWEJ0sQhLH026eFCt43ARuH-ekc8qYTVtoZ9p-JtT8Ykt0J08hgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MkmpZcIpsPcmifMySYvgRa4VE3h2QLTaO9mj5-yd0-EoNMK6NQogu1qSq5u82MdUmcYi38uTEJxw7saPEzxp64BNFfNrA_aErAgS5ymnoKSP9_24U9IYZbVNBUh1Dj3ZZUyKePXCp5IykcGW9AKZcwaBUDTDj9jZTuQmovk7d4JlqXl6QbA26zSyEHlXWyG2ppuNbB1l6om_WEpsd6UI1m-_RPdfZsCNIt5GkjjKUurEdlbq73M45BHeTx1rqb9RjdkSeV2ZMXTKCgu15Pta9El48yREXM_Fnz1jGCXQcoYkbiA5cZUNeZMQn1uv1Q_6j7VJcDRagdANTFJDeDCH7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده در منابع حکومتی با شرح:
تصاویر هوایی از حمله آمریکا‌ به پل‌های بندرخمیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/77194" target="_blank">📅 17:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77193">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: نیروهای ایرانی مدعی‌اند که به پادگان التنف در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را کشته یا اسیر کرده‌اند. نادرست است.
✅
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در منطقه کشته یا اسیر نشده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77193" target="_blank">📅 17:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77191">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUw89vY9CkJdBFd9a5Bye12EkRk-O0KQrSVDeApDbhqdkgT-62dtDjrqFC2MavBR9UrgB3VvIFU2kl_St0ZllibBRsTqCc0P01xen_d6FFTyA37Ce8qy2rJAYxlTYyatsj1bMC1iXGVuo5vwpjEq3J4b0qack3pFI8B3fQElfN8r53iDfGQV0WCl2POt0lUKeAS5j8xU7wVAyZluDEXolfe4vrZTHTMdnUTc7sbs500BIqyukQRstZ5zr4qy-7qZrqu71SgBC9aJokML2lQI28GqrG2qU8Bzjulj-6JppSkvggEa-zBmA3XVRBDI7xefgwpbeMgRH0E-C5ay5tUKDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه دور تازه درگیری‌های نظامی بین ایران و آمریکا در خاورمیانه، روز جمعه ۲۶ تیر قیمت ارزهای خارجی در بازار آزاد ایران بالاتر رفت و نرخ دلار به ۱۹۱ هزار تومان رسید.
وب‌سایت‌های اعلام نرخ ارز همچنین قیمت یورو را بیش از ۲۱۸ هزار تومان نشان می‌دهند و بهای پوند انگلیس نیز از ۲۵۶ هزار تومان گذشته است.
از سوی دیگر، قیمت سکه بهار آزادی در روز جمعه ۱۸۰ میلیون تومان و سکه «طرح امامی» به ۱۸۵ میلیون تومان رسیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77191" target="_blank">📅 17:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77190">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_lxRpOocWZSZsMP-E4KIKDSsEl6X1kujtfPuKzrQPyKxaprJ3uuD8dsesRYzsZkO_GRYpTO5D2nBGyK-xRCwBPrQVIhq3oYHyXzwgvhyl2Mu5cMWeW-5cQbM40JVmgvW6LxGljXRtZsYaHonL1MIb_KWE9O3qHAFKYHaiAuLQG_jXeWQnYGLLsF-jp4-OwtQTeiGJH4JbxFihc8XyQUpY35xtQXCrWEiOxR16GTBbYHYO-O9PVDhsZ5mPiuny5qpZUcVV62p4pu93HiPKj00lYdY2UNtQOGxdsMXPhEdpAQm8yRJyub9dhBU3OuNzLxf7bzFgxNXijmYtA963eHTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت برق، آب و انرژی‌های تجدیدپذیر کویت اعلام کرد در جریان حملات جمهوری اسلامی به این کشور، یکی از نیروگاه‌های تولید برق و تاسیسات آب‌شیرین‌کن هدف قرار گرفت و در پی آن آتش‌سوزی رخ داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77190" target="_blank">📅 17:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77189">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBGG2eHgRDBXJAFWO0NbYMYBag9wLJMFN0r2yVhts84-fqnfPZRk7eQIuGzfpcYOoHCZP55cyFLE7wmwXlA5F2rgeHISdpmYNWmRTmSw00p3xNYbPmZhGmKmLAJuuWji7XPVf3CwVHsG77MaD1mcMoXsdMf650wo9B-KhkMXzhv7m0Pu7CFDaUk0fnMWtJZJHTC0d2Qlz7lL3LHN67lpR2rXqDZLVeKAhPBK-4NhPlJAs-VSCmuvCvq1IdsXdvjMsjIbzZFXp-bhBopG5kt41OBDkgctS4gqwyWhsIRaU-3XcYMZdQd_dPQdec2wGF6Apyuzcx88zUFdvBelpuKzKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی و امنیتی استانداری هرمزگان می‌گوید که از شب گذشته تاکنون، هشت نفر در حملات آمریکا کشته و ۱۹ نفر زخمی شده‌اند.
پیشتر وزارت بهداشت ایران اعلام کرده بود که تاکنون ۳۸ نفر در ایران در حملات آمریکا در تیرماه کشته شدند.
بنابر این آمار، در همین مدت بیش از ۴۰۰ نفر هم مجروح شدند.
دور جدید حملات آمریکا به ایران از ۱۶ تیرماه و در واکنش به هدف قرار گرفتن چند کشتی در تنگه هرمز آغاز شد؛ از آن زمان، ایران هم حملات تلافی‌جویانه‌ای را انجام داده است که می‌گوید هدفش منافع و پایگاه‌های آمریکا در کشورهای منطقه است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/77189" target="_blank">📅 17:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77188">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=D6_AYOhSNLApnk0MRevHymErJwTQ2AqTaTX7BTs5LrU-wq9AODIa9mrrJsffVpb6R6RboHOMAJAQZN2tqxeVCJG6rqMVpSYn944gcvhZ62yzIhiUphPY9wGP8ky8M6hZOfZ7-z7qjWh3tPaBKPNysSND2mG1j0vwytpsR8xfIfGV3vi0R--WlmVW9oFoX92qryRmHvOHXwElVAArnE_w50ZTC15nLJEBSyUP-mwuXg0zGB_L7tazF-JS_mCGQkufBf_lHimwPjZpLi7_FL_yPNPQoq7n5XngAjji07AtFJVXQL7CSbpoJAqZNEKTWN43iYXO7FshI-MLcZwJFOx8Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=D6_AYOhSNLApnk0MRevHymErJwTQ2AqTaTX7BTs5LrU-wq9AODIa9mrrJsffVpb6R6RboHOMAJAQZN2tqxeVCJG6rqMVpSYn944gcvhZ62yzIhiUphPY9wGP8ky8M6hZOfZ7-z7qjWh3tPaBKPNysSND2mG1j0vwytpsR8xfIfGV3vi0R--WlmVW9oFoX92qryRmHvOHXwElVAArnE_w50ZTC15nLJEBSyUP-mwuXg0zGB_L7tazF-JS_mCGQkufBf_lHimwPjZpLi7_FL_yPNPQoq7n5XngAjji07AtFJVXQL7CSbpoJAqZNEKTWN43iYXO7FshI-MLcZwJFOx8Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: پل تخریب شده در کهورستان شهرستان خمیر استان هرمزگان
بنا بر گزارش‌ها شب گذشته، پنج‌شنبه ۲۵ تیر، در حمله هوایی آمریکا هدف گرفته شده.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/77188" target="_blank">📅 08:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77187">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">استانداری هرمزگان:  ۵ پل مورد اصابت قرار گرفتند
خبرگزاری فارس:
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
🔹
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
🔹
پل گریوه؛ مسیر بندرعباس، خمیر، لار
🔸
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
🔹
دو پل مسیر کهورستان، لار
🔸
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
🔹
پل روستای مارو شهرستان خمیر
⤴️
از مردم تقاضا می‌شود با عدم تردد در محورهای ذکر شده و مناطق مجاور آن، راه را برای تیم‌های امدادی و انتظامی باز نگه دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/77187" target="_blank">📅 05:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JjeekrlrYWytODML8QHarmuOwWXbAdIDjr7B1RA6SNmZksNNMp-eLGchsUD_z_pMnip_sHSvN6kjMm_b95zVfej7-8eTiKfpqdKWOj_XONMtY2OQ8KMOu_9tFKhSxcoxuIakUigvvhiFwMYap8Gm_RYa0-ZRYVqzIfUm9UilNV3mLwKfUFWZKSQ5yOaUCONitYv1PCalhRFK0WMjurVeJCcJ1F_zXUk_-9LD3J3tdai5FNQwAyj7TwE88CPtnXHNR10IWlRVsSlCPY0TKp7PGpta6XjWQtp0fLSgy2CZOOF6t3gAOecywNSD6Vkq_f1cX-LknsfvxFJV6wi4JxJ7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/907635e197.mp4?token=H5zWyqwp8jYeXZ1tHeSS8ve64h-6SeYql3tndwU8Qo_11DiNWNM-yTmzoGigPjXsLImWfzfWqgCzPNZ8Rqu7s1s_DOp1CotyMuxMON6Xl0KTuTMxfom2uiUX2n5M5xLrtOwHW932xHdXEJFEpxom4e5k5wcunx0psVrwIH-48cahcJh51Mj3sFU8mW78-S2DIxb7GV28Sq2BthYAXl_pwxAejaCR6QByaL1ylGb8vqqRDHo0uPldX4FpvYu58IoWSx_Jz_Lcr_6WX274eMFbAJsRY-O6eIm3NveWYC6joAQ54RjBn-8Gr2jzwmdbWLBoMAyQf6pboWp_aQsGhNfUiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/907635e197.mp4?token=H5zWyqwp8jYeXZ1tHeSS8ve64h-6SeYql3tndwU8Qo_11DiNWNM-yTmzoGigPjXsLImWfzfWqgCzPNZ8Rqu7s1s_DOp1CotyMuxMON6Xl0KTuTMxfom2uiUX2n5M5xLrtOwHW932xHdXEJFEpxom4e5k5wcunx0psVrwIH-48cahcJh51Mj3sFU8mW78-S2DIxb7GV28Sq2BthYAXl_pwxAejaCR6QByaL1ylGb8vqqRDHo0uPldX4FpvYu58IoWSx_Jz_Lcr_6WX274eMFbAJsRY-O6eIm3NveWYC6joAQ54RjBn-8Gr2jzwmdbWLBoMAyQf6pboWp_aQsGhNfUiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از 'پهپاد دیده شده در آسمان
#چابهار
'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 485K · <a href="https://t.me/VahidOnline/77185" target="_blank">📅 05:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f0b92b95e.mp4?token=aIcJKMpdx19TfhGfH0DdMV5r6byEG2YJOWWM6h4zeAz18gz5L0HG9zwYg2ndo-MeGiydCNmfPa-r39KVzDZ_s7i87PnxYQGjVRNiHxOtpKA-ZDXCYYMd6wTO_3hQ9ah56WKFu2Jo4jsz2-VGLUqJ5zwVhJWvZXf31m6kagD6A1wU2z0K14lf4HfXqrz8R3Qicr7kWFXdbgnGS_VQRgKRF3fLxjnRfRYrcHibT6G9vc13BPMeleqJpok_kel1HCj8eK3XIqIdTXlxoQ1sMGPrv3zs0NUXt2QBUovqUiazy3CkhffdhhnDM_3oMYwIDjX-bTkf9TkovlFDvZqr4o6hTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f0b92b95e.mp4?token=aIcJKMpdx19TfhGfH0DdMV5r6byEG2YJOWWM6h4zeAz18gz5L0HG9zwYg2ndo-MeGiydCNmfPa-r39KVzDZ_s7i87PnxYQGjVRNiHxOtpKA-ZDXCYYMd6wTO_3hQ9ah56WKFu2Jo4jsz2-VGLUqJ5zwVhJWvZXf31m6kagD6A1wU2z0K14lf4HfXqrz8R3Qicr7kWFXdbgnGS_VQRgKRF3fLxjnRfRYrcHibT6G9vc13BPMeleqJpok_kel1HCj8eK3XIqIdTXlxoQ1sMGPrv3zs0NUXt2QBUovqUiazy3CkhffdhhnDM_3oMYwIDjX-bTkf9TkovlFDvZqr4o6hTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا حملات جدید در ایران را با موفقیت به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) امروز ساعت ۹:۴۰ شب به وقت شرق آمریکا، تازه‌ترین موج گسترده حملات خود علیه ایران را به پایان رساند.
نیروهای آمریکایی، از جمله جنگنده‌ها، پهپادهای رزمی و ناوهای جنگی، با استفاده از مهمات هدایت‌شونده دقیق، ده‌ها موضع نظامی ایران، از جمله تأسیسات پایش ساحلی و پدافند هوایی، زیرساخت‌های لجستیکی نظامی و توانمندی‌های دریایی را مورد اصابت قرار دادند. این ششمین شب متوالی حملات آمریکا علیه ایران بود.
سنتکام به دستور فرمانده کل قوا، به تضعیف بیشتر توانمندی‌های نظامی ایران ادامه می‌دهد و این کشور را در قبال حملات اخیر به کشتی‌رانی تجاری پاسخ‌گو می‌کند.
بیش از ۵۰ هزار نیروی نظامی آمریکا در سراسر خاورمیانه در حال فعالیت‌اند و همچنان هوشیار، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/77184" target="_blank">📅 05:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FazSvgcSWDFpJMVH6lGJSvGc_bvMqv9AFWEir-wqVMJYmwjLJYPgZYr23YKB0tCeTV_tlr9tB5YtQCnn2AxCh7CjS0wH7PND9VbJRKlssPgtB8YrABiKJumpyuZRK2_BvRlz9g23mIIPrlJf61U66NpuMGJxek_ZGA7M8sk1SiSqiHHOnrcGcWizGnDw0W-FCmh0N3xFjzHuyYr_s41zSy_u7iqtArdajgqVRFM5rwxcoXruJ5lQ6zmXiWZzU7JPso_xyF9SyJeVD-veCGPKJb5owGhLyI5w65dyyEgbMDMhSSjg-cvMUdfQDCjAsE2GB3WuYTgxYNBtppTc1HW3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: 'لحظه انهدام برج مراقبت دریایی چابهار'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/77183" target="_blank">📅 05:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bv3T8CIaDOfaS0M-E1dq0keG0frTEMeNVybjt25odOblf2wO4K-zgJ-f0QozPbJ20cLOCFqyDIqNgBPwRotgIlzfwM31OVIpmTSNaSGJGXIk6Tsdqdv-dGN40pJw3lX8u1k_THRL0L3VGKruAb9s-PWFnwS2ncDIggHWeYnrF5ZlekUrqfyDvoW-EAnTIxZdB5bzl0QjNT5qYmTN5EWUNiKUf4GU397bPBWmzv7OHIfOOAwhKbn0KnGJwUzxMNTvlJo_2OwDBNrVu2ELYcZhq4aQ9Huhlie9yB8kog_CXue9MYXO4DMHP3YGJz_Wf324n8qT8ZH_n0D3hEvfRv4hfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس و پیام‌های دریافتی: در حمله اخیر آمریکا به چابهار باقی‌مانده ساختمان برج مراقبت دریایی فرو ریخت.
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77182" target="_blank">📅 05:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77178">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bYAKxBk6X638JQwJycbibs2RJ6IHCFjvkJjLvG5OWnbO6bDDfljkBXhksGsCUVC79yKP_-mBsOLGbJf6jRgPSn9kBLoUi-jgBYx-xZtSEJdURhHzhChbvjo_4trwwEif651HH9FdCd6k5dw5Q8jiczsBQdaaMyflNzG8QPn43bQ_lXSeEBKBm_4dR1iNc7M5b9fc3UBJhxpQZ13cYnzPN46iKc0QCpgWpbLdDjdcEDuMqNoJ4AcOUQMVZ4jBE5HNjMPdD76ETzlQn0VBQEERq8Fz_vWJak5M_Wqc4qhzmLy10IOyPnnERis8dP2V3gT3_MheEx11V5G-5_Phzs_plQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9b8ff5804.mp4?token=YcgnHmKZVLHewwzOlf589zqRWO_CmtY9k1skx92W2nyCr8DDo-_Vn3DYlPgGIw0J1IUzWghH27UN7TYLMYs_FeiKf8LPY4ybLeMgeNn9vBol_bF8e1NrYq1gGbfKHCqsIyJuWUx5rKXV7qrRtvr46ZRjblVMQk3Tpatib7keHMP5SRanE5g3Fr3WYN25T8AuzpFV8QnWlQEc_jTpbbASRFmbnmVsrSyYd5g1HAvyZnUIUTgfPo4xcGB6dypA8E6l4dgsEJCT-7813fud6vksjGBC_3y58gorAyyw1FvC4M-3qm2wk3lixqGyST8ScWnclLaqLqLdoITIbYtgvKvUoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9b8ff5804.mp4?token=YcgnHmKZVLHewwzOlf589zqRWO_CmtY9k1skx92W2nyCr8DDo-_Vn3DYlPgGIw0J1IUzWghH27UN7TYLMYs_FeiKf8LPY4ybLeMgeNn9vBol_bF8e1NrYq1gGbfKHCqsIyJuWUx5rKXV7qrRtvr46ZRjblVMQk3Tpatib7keHMP5SRanE5g3Fr3WYN25T8AuzpFV8QnWlQEc_jTpbbASRFmbnmVsrSyYd5g1HAvyZnUIUTgfPo4xcGB6dypA8E6l4dgsEJCT-7813fud6vksjGBC_3y58gorAyyw1FvC4M-3qm2wk3lixqGyST8ScWnclLaqLqLdoITIbYtgvKvUoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: دود انفجار حمله به مکانی در چابهار
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77178" target="_blank">📅 04:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77177">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Moa3r4o8__tSPl9VCJF6Noc6AVTOqKaPLR4jrnZisyD6Ui3Tea4jIMELwOpne0SnSDWzKj0hkGnYb3tv7mcEFqh-Q0ThyCLOvS1CAZu7vet8MW1RWC6_JOQhN1pBYbpslNJiiIBP2yC1xm1K6JVlv8hHSSwV6gt2cBV_8D20bWrOjUR4xHz4B3NFlsJ7NSkTy54brQJoprUeIESBaUP2qUNMpSgUb3LwQ5NRXxKd54uU9x12-ywl538ArfIP9cLlFj-69oZ3rMiyOPtA7D-ml0DuXM73FayrQcjzIpinED2vF8Qg_bzQVXK1aHPS-c9VmQJkrCMn5A_U4L58AW4a1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری هرمزگان اعلام کرده حمله به پل‌های گریوه و کهورستان در بندر خمیر ۷ کشته و ۹ زخمی برجا گذاشته است.
خبرگزاری تسنیم گزارش داده که پل‌های گریوه و کهورستان که بخشی از مسیر اصلی ارتباطی بندرعباس به شیراز محسوب می‌شوند، هدف قرار گرفته‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77177" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77176">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9aE8tfIzxStJ0RbtOSZTizIcUsjm3yC7QYey2KA7JG4eXMnFgkLWtpWM4Mfmq57QdxGm3eP7nuLw6DVBkYdRvmyhzE3iJSaDkubz9EXiBDaZ0SodcsvYHo8iNOdT-LjmwS6Px__tbXV-pdkHleVee8MWc3t9Sk4GJ0w7LYyOv7_qRun1BefUb8WQhvwuS3o4DbteFt1T4omBXlgJ8vqjhsrnqiK4FeN_17ciizrfLbDgRHXVUhe_vHPZC62tSUhDVFBgwlORdR9Pz1pB4g2wFpBllFzU6xBqEX1H_h1VtLY6zPh0jF-Sy5_Ln7kHfx7GxIk1c5lRZgLBWyEX4xkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گزارش‌ها درباره دریافت پیامی از جمهوری اسلامی که در آن استیو ویتکاف و جرد کوشنر به سوءاستفاده از مذاکرات و کسب سود از اطلاعات محرمانه متهم شده بودند را تکذیب کرد و گفت هرگز چنین پیامی دریافت نکرده است.
این واکنش پس از انتشار گزارشی مطرح شد که مدعی بود جمهوری اسلامی در پی مذاکرات سوئیس، ویتکاف و کوشنر را متهم کرده بود از نوسانات بازار ۹ میلیارد دلار سود برده‌اند و خواستار اختصاص نیمی از این مبلغ، معادل ۴.۵ میلیارد دلار، به حکومت ایران شده است.
ونس این ادعاها را «کاملا بی‌اساس» خواند و گفت ویتکاف و کوشنر از اعضای مورد اعتماد تیم دونالد ترامپ، رییس‌جمهوری آمریکا، هستند و ادعای سوءاستفاده آن‌ها از اطلاعات محرمانه «مضحک» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/77176" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77175">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پیام‌های دریافتی:
درود وحید جان چابهار سه چهارتا موج و صدای انفجار و صدای جنگنده
۴:۳۷ دقیقه
۴:۳۸ دیقه چابهارو زد
چابهار زد
سلام وحید جان صدای دو انفجار ساعت ۴:۳۷ دقیقه در چابهار شنیده شد
چابهار ۴:۳۸ پایگاه سپاه امام علی و اسکله سپاه توسط جنگنده ای که خیلی پایین پرواز میکرد بمباران شد.
🔄
باز هم زد
دوباره زد الان ۴:۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77175" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77174">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پیام دریافتی 'از قطر':
ده دقیقه پیش صدا انفجار و پدافند، دوحه.
Still no threat cleared message.
آپدیت ۴:۲۳:
Security threat eliminated.
هم‌زمان از تبریز پیام‌هایی درباره شنیده شدن صدای پرتاب موشک دریافت می‌کنم. قبلش هم از شهرهای دیگری پیام مشابه فرستادند
.‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77174" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77173">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/146830ca4d.mp4?token=HdCnSbXzF_PVrhtxBPPnFhvxKdiyHlZacYrJjMvBd-wkysN6w0IfEIcVJGVYpd6b1_10h-L_iMV-qzaBZh-qIDo7mpMSmvEAxF2Wu8Jr_-wXbyyiZwk3I3GQLIYo9WieMRdqlRtcu5WtxkLv8N_m2uzyz4NOEZB-alpGbe3lGfIETIWU6AwbA2fF_pKDt1QwzEHv_xsgCkU-r4ujJlZNGUFdLYZMCBdz_80QmVH3-_MwHs8fK_Wc4wEu8PB2DiZtCbukT5LPpog5Pp2h1UUanuXiDhLDmXwNjMXTj64p-8qUR5O_sXBZimtnuMOQVPToe-9FjR8kCuG8hh0yzBuTDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/146830ca4d.mp4?token=HdCnSbXzF_PVrhtxBPPnFhvxKdiyHlZacYrJjMvBd-wkysN6w0IfEIcVJGVYpd6b1_10h-L_iMV-qzaBZh-qIDo7mpMSmvEAxF2Wu8Jr_-wXbyyiZwk3I3GQLIYo9WieMRdqlRtcu5WtxkLv8N_m2uzyz4NOEZB-alpGbe3lGfIETIWU6AwbA2fF_pKDt1QwzEHv_xsgCkU-r4ujJlZNGUFdLYZMCBdz_80QmVH3-_MwHs8fK_Wc4wEu8PB2DiZtCbukT5LPpog5Pp2h1UUanuXiDhLDmXwNjMXTj64p-8qUR5O_sXBZimtnuMOQVPToe-9FjR8kCuG8hh0yzBuTDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منابع حکومتی از
محل حمله آمریکا به پل جاده دسترسی بندرعباس – بندر خمیر و جنوب استان فارس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77173" target="_blank">📅 03:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77172">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bcxAill6_Gylx12iqASs8um0r4vvofGuG3CHpYU5-6cTyV8sYHhSMUtICAmEFRJ7vbzrjF_zF2aOpZoAofLd2vQoPuBc4adnneuhgrRUQ4IRLawk1ZuLS0YQsYM_PhPz6qrujUVtSCwU2f7R9anB9QGesUsaduyRYhMxVPmkG6Tuy5zkb-BSqN62M3GBq8-aXk30SGVNLEQkkipIuQ1DZGgQmEoQmHrE8MuuhwGXN5qmi2C8nH_F7uKdgi_dvUdECSX_gEUvRBNDDwzBIUW2eOorr2yPNAy8VGIdQ18pBZ8FnpwYE1pUsQvPRzPGr4ttYFiHEUYGf3woYRD6HKlg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به روزنامه وال‌استریت ژورنال گفت ارتش ایالات متحده چندین پل در ایران را هدف قرار داد تا مسیرهای تدارکاتی منتهی به بندرعباس و پایگاه دریایی واقع در تنگه هرمز را قطع کند.
آمریکا می‌گوید جمهوری اسلامی از آن پایگاه دریایی برای حمله به کشتی‌ها و نمایش قدرت استفاده می‌کند.
تلویزیون حکومتی ایران نیز گزارش داد که چندین حمله به پل‌هایی در بندرعباس و مناطق اطراف آن انجام شده و بزرگراه‌های منتهی به بندرعباس از استان‌های همجوار مسدود اعلام شده‌اند.
رئیس‌جمهوری آمریکا، سه‌شنبه ۲۳ تیر در مصاحبه‌ با شبکه فاکس‌نیوز گفته بود دامنه حملات آمریکا به جمهوری اسلامی در روزهای آینده گسترش خواهد یافت. دونالد ترامپ افزود حملات سنگین ادامه خواهد داشت و اگر جمهوری اسلامی وارد مذاکره نشود، هفته آینده نیروگاه‌های برق و پل‌های آن هدف قرار خواهند گرفت. او تصریح کرد: «تمام نیروگاه‌های برق و تمام پل‌های آن‌ها را از کار خواهیم انداخت، مگر اینکه پای میز مذاکره بیایند.»
ترامپ در آن مصاحبه همچنین تاکید کرد عملیات نظامی آمریکا علیه جمهوری اسلامی ادامه دارد و این حملات «تا زمانی که خودم بگویم کافی است» متوقف نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77172" target="_blank">📅 03:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77171">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3729a1df42.mp4?token=MzxsixkpSX8sooUZ1iaFV_Od41gYTrwaRbNW-EW3KzIDWVwGLitwEoyJ4-eimlxvju86kBU0p2nMoTJtr2TzR6aeCr1xChFe1r6HiCqBjLEBN8eukp4t9aJZpkkAMbJ0kBObxOU_IxjFKNcOlcza0rmj9iBb1Ts5kO-dRryx_EUsRECXQ5wy9FMBqhE_R6dJDM0ZfpyWIdwCCdPvPL01Um3224gg5J0vBO1yFP5UkhNRLxwMPfwZ258TRMWWyROYZ5jzOjFJa562OTkdkhhDSAe-BuTfipJhFJFO856GskwudcRSGq-FczGh6f8KHXaI6AI2scUGzmcX8U1mCP6H8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3729a1df42.mp4?token=MzxsixkpSX8sooUZ1iaFV_Od41gYTrwaRbNW-EW3KzIDWVwGLitwEoyJ4-eimlxvju86kBU0p2nMoTJtr2TzR6aeCr1xChFe1r6HiCqBjLEBN8eukp4t9aJZpkkAMbJ0kBObxOU_IxjFKNcOlcza0rmj9iBb1Ts5kO-dRryx_EUsRECXQ5wy9FMBqhE_R6dJDM0ZfpyWIdwCCdPvPL01Um3224gg5J0vBO1yFP5UkhNRLxwMPfwZ258TRMWWyROYZ5jzOjFJa562OTkdkhhDSAe-BuTfipJhFJFO856GskwudcRSGq-FczGh6f8KHXaI6AI2scUGzmcX8U1mCP6H8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
سلام موشک از شهرستان جم استان بوشهر فرستادن
سلام همین الان از جم موشک بلند شد(۲:۵۶)
۵عدد موشک از جم به سمت خلیج ۲/۵۷
سلام وحید جان از جم موشک بلند شد
سلام همین الان پرتاب موشک از جم 2:57
سلام وحیدجان الان ساعت ۲:۵۷ از جم موشک بلند شد نمیدونم به سمت کجا
همین الان ساعت ۲ و ۵۷ دقیقه موشک از جم بلند کردن
ستاد کل ارتش کویت اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی جمهوری اسلامی هستند.
ارتش کویت همچنین اعلام کرد صدای انفجارهای شنیده‌شده ناشی از رهگیری اهداف مهاجم توسط سامانه‌های پدافندی است و از شهروندان خواست دستورالعمل‌های ایمنی صادرشده از سوی مقام‌های ذی‌ربط را رعایت کنند.
@
VahidOOnLine
پیش‌تر:
وزارت کشور بحرین اعلام کرد آژیرهای هشدار در این کشور به صدا درآمده و از شهروندان و ساکنان خواست آرامش خود را حفظ کرده و به نزدیک‌ترین محل امن بروند.
این هشدار در حالی صادر شد که پیش‌تر جمهوری اسلامی اعلام کرده بود پایگاه ناوگان پنجم آمریکا در بحرین را هدف حمله قرار داده است. مقام‌های بحرینی تاکنون درباره علت به صدا درآمدن آژیرها یا وقوع هرگونه حمله جزییات بیشتری منتشر نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77171" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77170">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZWz4J6EE-wjTauzhGkVYMI2BiMgiL5pJfNGslrWHbZpMbTROcYqv55wSuKAIEUioAd_uU916fya4c2wdNeq4Wjhw0_AOaNrmYHGc4kOXGmc9d8_3r_eklPU8C3d4tkjLvGU_j5yfl3U30CiAM3dfBswOI2c-Pqn-gl-FnD90QzYTQVexQ9Ct_WiyCcIjc-ScHwbvw_4fH_heHz-3s6IYMKUjRmZwph_8-7UcPXcB_3FYfhGIDw1Qwd13F_z_xYEJpLCoac82Dn3eY04KTRrjowr78Mn8e6n0bZd8zb54O4uF3q1hwOvY5UGXq7SJApMbMCcCs2ziqJsvnkOT-qfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع حکومتی به نقل از استانداری هرمزگان:
در ساعت ۰۱:۳۰ نقاطی در حوالی بندرلنگه مورد حمله آمریکا قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77170" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77169">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/033b4ebf1c.mp4?token=XY8YQL0VFMkKd5A3AsWJQfIUvnFjw-2NFTOEiNyIIIAV5GOoRUrRaFGHc6NwlzJ6TP4wBbUykS2GjQtpMHSgNy-xDSvkqlx7cziJaaSlbTeD20W5jMk_DuFA_jZhI4NDYXSqkh6yfApSB6VKAoAJgQdOI7Mh99C_8ZxMC29UuICYZ4IFJKbGjIgebEYFIC6xxJCZ0OIH3C5hVP-iGwusv9v8nAlSYMt4PgvMC0k498QZxRqFaxiyVOtgVhcEyboAzLduflSAORQZCNi-X06qzkokAbu8AVQ_xQM1pwrLszYagqMrp6AWqXMh2W5KYK2j24jEs7leXtcI_KHOwPBLfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/033b4ebf1c.mp4?token=XY8YQL0VFMkKd5A3AsWJQfIUvnFjw-2NFTOEiNyIIIAV5GOoRUrRaFGHc6NwlzJ6TP4wBbUykS2GjQtpMHSgNy-xDSvkqlx7cziJaaSlbTeD20W5jMk_DuFA_jZhI4NDYXSqkh6yfApSB6VKAoAJgQdOI7Mh99C_8ZxMC29UuICYZ4IFJKbGjIgebEYFIC6xxJCZ0OIH3C5hVP-iGwusv9v8nAlSYMt4PgvMC0k498QZxRqFaxiyVOtgVhcEyboAzLduflSAORQZCNi-X06qzkokAbu8AVQ_xQM1pwrLszYagqMrp6AWqXMh2W5KYK2j24jEs7leXtcI_KHOwPBLfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
فرماندهی مرکزی ایالات متحده تفنگداران دریایی آمریکا از یگان اعزامی یازدهم تفنگداران دریایی، ۱۶ ژوئیه در خلیج عمان برای راستی‌آزمایی، سوار نفتکش «وِن یائو» شدند.
تا امروز، نیروهای آمریکایی مسیر ۳ کشتی تجاری را که تلاش داشتند محاصره را بشکنند تغییر داده‌اند، ۱ کشتی را که از دستورات تبعیت نکرد از کار انداخته‌اند و برای اطمینان از اجرای کامل محاصره دریایی جاری آمریکا علیه ایران، وارد ۱ کشتی شده‌اند.
تنگه هرمز و آب‌های اطراف آن همچنان آزاد و باز است، به‌جز برای کشتی‌هایی که تلاش می‌کنند «دیوار فولادین» محاصره آمریکا را نقض کنند.
🇺🇸
CENTCOM
ویدیوی دیگری رو هم توییت کردند. میشه از ثانیه 00:20 ویدیوی بالا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/77169" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77168">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8860c5a306.mp4?token=Wb9P5qP0n2MEIF4cKa8VWJ5m7mIblJVBuX0fzi-XUCIs-BWtlvC8AR_yEu-y7iVQWvSUOlmcTtRABfCAcbktP_8NrhycO40mygxwH-qJWdL6GbgxMtwp4KMvw4Ywbrjf_1vJZ1xZbW2Q0ecKakiW1h1R_8s0Z7_gxEMic4wv-psY-QX_Dz1XwUYLl4f0I7eCBCyOB52bvhnqvaFVlgAwmwwUleYLjR7tcYj3gNreqeBrrfTo1-ilYBso8BDbpLCbvEFxwboPDeGxaYP2SGgOG9n_loW48qtqWl46AohwVCesgrKij6SiyuW_d2fuxM6ZDLCIMuftGPumWr2eFZH0mA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8860c5a306.mp4?token=Wb9P5qP0n2MEIF4cKa8VWJ5m7mIblJVBuX0fzi-XUCIs-BWtlvC8AR_yEu-y7iVQWvSUOlmcTtRABfCAcbktP_8NrhycO40mygxwH-qJWdL6GbgxMtwp4KMvw4Ywbrjf_1vJZ1xZbW2Q0ecKakiW1h1R_8s0Z7_gxEMic4wv-psY-QX_Dz1XwUYLl4f0I7eCBCyOB52bvhnqvaFVlgAwmwwUleYLjR7tcYj3gNreqeBrrfTo1-ilYBso8BDbpLCbvEFxwboPDeGxaYP2SGgOG9n_loW48qtqWl46AohwVCesgrKij6SiyuW_d2fuxM6ZDLCIMuftGPumWr2eFZH0mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت چند ساعت بعد: صدای چند تا از انفجارهای در ویدیوی بالا
پیام‌های دریافتی:
وحید جان همین الان بوشهر سه تا انفجار
۴ تا افنجار شدید بوشهر
بوشهر ۴ انفجار پشت سر هم ۰۰:۵۵
بوشهر سنگین دارن میزنن
سلام وحید عزیز بوشهر همین الان پنج تا انفجار رخ داد
بوشهر 00:55 صدای 4 انفجار
بوووشهررر همین حالا زدنن و دارن میزنن
همین الان بوشهر رو زدن ۲-۳تا شدید
مجدد ۴-۵تا
خیلی شد
حاجی رگبار بستن
سلام بیشتر از ده تا صدای انفجار بوشهر هنوزم دارن می‌زنن
بوشهر ۴ انفجار پشت سر هم ۰۰:۵۵
۶ تا دیگه پشت سر هم ۰۰:۵۶
بوشهر ۰۰:۵۵ بالای ۱۰ بار پشت سر هم زدن
سلام آقا وحید همین الان ۱۲.۵۵ دقیقه به بوشهر حمله ی  شدیدی شد منطقه بهمنی و من بسیار در خود ترسیده ام.‌
بوشهر صدای خیلی مهیب
۱۰انجار بوشهر الان
۵۶دقیقه
بوشهر
۱۲ تا انفجار شمردم
ساعت ۱۲.۵۵ تا ۱۲.۵۷
سلام وحید جان بوشهر ۶ بار زد خونه لرزید
بوشهر ۱۲:۵۷ چند انفجار خیلی مهیب
بوووشهررر همین حالا زدنن و دارن میزنن
بیش از هشت انفجار
همینجور پشت سر هم دارن میزنن نزدیک ۱۰ تا بود پایگاه دریایی دودش پیداست
بوشهر داره پشت هم میزنه
😭
😭
😭
😭
بوشهر خیلی صدای بدی اومد انفجار شدید بود همراه با لرزش چندین تا انفجار پشت سر هم بود
سلام وحید
حداقل ۱۲ تا انفجار پشت سر هم بوشهر
سمت پایگاه دریایی
بوشهر خیلی صدای بدی اومد انفجار شدید بود همراه با لرزش چندین تا انفجار پشت سر هم بود
سلام، صدای انفجار شدید بوشهر
ساعت ۵۵ بامداد شهر بوشهر محدوده پایگاه رو داره به شدت میکوبه شاید ده تا دوازده انفجار
سلام آقا وحید ساعت ۱۲ و ۲۶ دقیقه شهر بوشهر ۱۲ بار زدن صدای انفجار شدید بود
۱۲ تا صدای انفجار بوشهر اومد
پایگاه هوایی بود پشت هم رگباری
انفجارهای اولیه نزدیک فرودگاه بود صداش نزدیک بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/77168" target="_blank">📅 00:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77167">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y7NGMbXMxYH0o1_O3lSh3it6y84vIsZSkPBn_r93g4SNGzkvPF6mq5bFsDVSsChQq_CgiIQTLP8DIVOCXnx9tpjrQdcl8LeQQ2_51jMs7ttyoPfDL_V7ZSknFEQJNMS-cbUzSVxO4UWL5mSgKouv_NebbAKo1ovURSxVtAXf7370GsmMvT-7-jAIoJancw3QW3oLWndAdI7odkvQ5dsMidFOpDuEBch2c2bHXuUE6jHzldzKPn_hKgqDWEAcatvkD3q4Ebtt6imAB3rtNptSMlO2N9Kqi6iH1RvywKjsRdZl2-bRGqqB8tewuR5VkeUJADrlqpo_YiZWhwKxCDdn7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: 'پل کهورستان در شهرستان خمیر استان هرمزگان'
که گفته میشه با حمله هوایی آمریکا تخریب شده.
پنج‌شنبه ۲۵ تیر
Vahid
فارس به نقل از استانداری هرمزگان:
علاوه بر پل کهورستان، پل گریوه نیز در محورهای ارتباطی استان، مورد اصابت قرار گرفته است. ۲ نفر کشته و ۴ نفر زخمی شدند.
تسنیم:
در شهرستان خمیر به سه پل حمله شده که مهم ترین پل، متصل کننده بندرعباس به لار در استان فارس در محدوده بخش کهورستان است.
صدا و سیما:
استانداری هرمزگان اعلام کرد محور بندرعباس - خمیر - لار و محور کشار - کهورستان نیز مسدود شده است.
📍
میگن یکیش این بود:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/77167" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77166">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NkMH8U50C84G4KKW3AKed4VB9sQzhLrDBJYltDx3NFe_APVGfgVVPJBU6KWDQPt91hnPkTFThQ64GHRLuQW66JgxLWglX55BGDQWr-DlVETd0VPsNj-Ga5KgBcPjNHicwFN_KzR2RxqBV75ZHdIKy5XGj5tIfAKRtBhtQLzBOvKpVdtgzv6K9xyFEQP3zxcvd1YmSAV51Rvn67X8eFSCCDZK9-Ih-DJeQPnnBeTMXSTBHyi3sc5yneDL9epfQjCYOxvE2ljKkKCgCEK0zIo0exsRuRTO7sU7nG6dqgdPNTvXnF-x_yEqx1sawc1TDKxirBjRMjNBx_fPY1mJ7DS8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77166" target="_blank">📅 00:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77165">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/713dc65855.mp4?token=ajPExPqypg9gj7rvZWwHthrvkC5ByH9RQUEKpaQAPOjlwHBdFryfplR-H09Xpyh7mHhxhVjWKx-mdmGakIWJ4CI5Tu8o7FmPL5ePyPsnltcBooDpdjnUi_OjDWXCMPwe-oAA63HLLWdv9PT0KXGaCEKj3DY3rlXdmMvPh6gYhw1ATGa9V6bcTuHGeFTBU9W0FQMpXhyyXfg-fJmRL5PbS7szwRGaS_l5OWkVhjrBw0oUGTsO2mNy8k29fhOVf8fQidn9JRQ8dTVwFBsjZWzyZg-ePQ4j4uTltBWXfiTBsHr_SBTnQpBNx3onQNn-q5g4zNLNtGzRzmR6OtyfsZOQKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/713dc65855.mp4?token=ajPExPqypg9gj7rvZWwHthrvkC5ByH9RQUEKpaQAPOjlwHBdFryfplR-H09Xpyh7mHhxhVjWKx-mdmGakIWJ4CI5Tu8o7FmPL5ePyPsnltcBooDpdjnUi_OjDWXCMPwe-oAA63HLLWdv9PT0KXGaCEKj3DY3rlXdmMvPh6gYhw1ATGa9V6bcTuHGeFTBU9W0FQMpXhyyXfg-fJmRL5PbS7szwRGaS_l5OWkVhjrBw0oUGTsO2mNy8k29fhOVf8fQidn9JRQ8dTVwFBsjZWzyZg-ePQ4j4uTltBWXfiTBsHr_SBTnQpBNx3onQNn-q5g4zNLNtGzRzmR6OtyfsZOQKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: یکی از پل‌های کهورستان شهرستان خمیر
منابع محلی: محور رفت و برگشت
#بندرعباس
به لار مسدود شد.
پنج‌شنبه ۲۵ تیر
Vahid
یک خودرو دیده میشه که احتمالا از روی پل سقوط کرده.
آپدیت:
محتوای ویدیوها به نقل از شاهدان عینی صدا و سیما!
تجاوز هوایی به دو پل در بندر خمیر
🔹
به گفته شاهدان عینی دو  پل حوالی روستای کهورستان و رودخانه شور شهرستان بندرخمیر مورد اصابت قرار گرفته است.
🔹
راننده یک خودرو شخصی، روی یکی از پل‌ها شهید شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/77165" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77164">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dfd383428b.mp4?token=JYAm0d2yIIjPPfrRVGXjag4gdQrEbrwnhxGgl7lW2InnOq7jp20AR1hPwYk2ecmVGcdj5FUyt31bQRDf3chLTTp6EzSHPzcJEQiENbZQcNEPKRvjAekAdp0-AvMr7i7-KlT_sixwg5tjDZ7oVHyqoHYbYSOOIfDstrgRuDGfBsu53uRpFmjAg3EbtJnBi7UvUeeeddVjGqJLJA58OUAjRFGr6Fl_6uoZEB-YbzVgbH_M55izIYag9mNIvGSSwzJfBzq1-BtyHxmLEv_PzJAqk5TLoMH2C-NczDa7qx3TkJFof0DpuUZHejNqb4zUARY7ncTTb98kqp2ZndWCKGQKPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dfd383428b.mp4?token=JYAm0d2yIIjPPfrRVGXjag4gdQrEbrwnhxGgl7lW2InnOq7jp20AR1hPwYk2ecmVGcdj5FUyt31bQRDf3chLTTp6EzSHPzcJEQiENbZQcNEPKRvjAekAdp0-AvMr7i7-KlT_sixwg5tjDZ7oVHyqoHYbYSOOIfDstrgRuDGfBsu53uRpFmjAg3EbtJnBi7UvUeeeddVjGqJLJA58OUAjRFGr6Fl_6uoZEB-YbzVgbH_M55izIYag9mNIvGSSwzJfBzq1-BtyHxmLEv_PzJAqk5TLoMH2C-NczDa7qx3TkJFof0DpuUZHejNqb4zUARY7ncTTb98kqp2ZndWCKGQKPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: در کهورستان
#بندرعباس
یک پل هدف گرفته شده.
صدای ویدیو: موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
پنج‌شنبه ۲۵ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77164" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77163">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3efbf07c20.mp4?token=DBFqrSrosbvO2Sg1J_UPX2u28b1TFEDIj37pJ0m3U_8uXvYFy1o4aYwD7urgnaiikRYxSgHH7-LXOsi6UViWg7Env8_dqDjynDhTrUK6Ml3VL9_e1ufuNt5v38QSsW2H3gPpYTxV9hwZgINQ9JEUHY7nbiaHSTnTb1cqPFBS5SSc4-7_LJsuZ3D-rirWin12E1diBl-ay4oV966-BRahEnpcayhqhvztnvxDpxCfKB6KCNEv1jP-5Q2NtqMRFOhgXZ_RcHhan0VXFAe92Wy60VMBwq6Hu4Xz84GQ0qgZhXSLOEWwwWfVHL-KT0tUmndHkiBoYHPTTHmUvo-Tw7jvEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3efbf07c20.mp4?token=DBFqrSrosbvO2Sg1J_UPX2u28b1TFEDIj37pJ0m3U_8uXvYFy1o4aYwD7urgnaiikRYxSgHH7-LXOsi6UViWg7Env8_dqDjynDhTrUK6Ml3VL9_e1ufuNt5v38QSsW2H3gPpYTxV9hwZgINQ9JEUHY7nbiaHSTnTb1cqPFBS5SSc4-7_LJsuZ3D-rirWin12E1diBl-ay4oV966-BRahEnpcayhqhvztnvxDpxCfKB6KCNEv1jP-5Q2NtqMRFOhgXZ_RcHhan0VXFAe92Wy60VMBwq6Hu4Xz84GQ0qgZhXSLOEWwwWfVHL-KT0tUmndHkiBoYHPTTHmUvo-Tw7jvEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: کهورستان بندرعباس پل زدند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/77163" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77160">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vc8ddiOIkirqryiOxW2N1wI7lvRpZeQztRVPGo3rpxs9QjMRnk_ch2kF_3s56UIHdg8E9RMXvvEpGZPy5zEY4ej_PKlXM5sQ6vhCoEmeecffmh5Vlo2PJYlOH9VXRVIbO4TClvvPPuKPotQox_oNtOgqz_NXjksDPQAF0dPptRPcFEVrLa_skGVQlL86iK9UTQ_pUD_mxxcDfG3qxyu_pTmlUxCmzKfcCLf7mNJh5LLJQk29E18Vhpdiq5wgFXOutAcQNVE0PQHIMF9B-fUvlVScpjOMjvkDBMFGK86hB8U-j17Ezcom9smCiAPi3rFnLSaeLeJKJCrrUnfhXZFtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I9yASRAdLQ6ux8HQlIQiBsUuWaharh9ZF7Wa2ZMB6bcu4hCAgRrZewxv03tfeHxbOXv1coJsHvgYA7CQJ4jAiAOhy8kkoqykn_CPKJwYxSev5-t0vDBlUoug7_GliAGEwi5gDsmAAGieegw_uO6iczPJYzEyW8IIRyRgkBRl2Ebo4ouqIGXEQTyFBMPCr1aeIKf4-ZKq4Xky0rbYNizOrw3blAI6k6XvMqa8x2_1SdizXi8TOHo03ZFizmQ1pDC7hKe0b2lOcUhTUBZt-0IAq0e22BHNPB4SGqhsegZB0rsu-HeXAYJQecSTWhxe3K9u83XXFGBbBMZhIaAg7JeJOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4d9ea9eedd.mp4?token=BkVXOzujkR-pK4BwWTzv4crW464g4Cl2PXkXzh7F9QLqBFbFGhKZlOw8yudEM3WFJUtaa4Hv5BL15_qoJ3NdmLY_X-b2qeEHorOsOFkrrPGBpUibOUT8vl8ZOKGd5FepSrKXElDZLr9Z9YyBBsSM7KZpCD_e_hHe5rp8UcnZ_ynUajMci13vP9zdIsGncCdySVH1YbWroHm42EYMmM1t9Ii8PLb0uUYlq46YLezxn2d4eH8aDUt-TnnoXZM12F1CG7iSBy9Tjz6PA5z97H9ONCEuFTYlJ-2dF6bk78d7y5qhWp36hP_Cr8mSwzk08KTRN4AO58qDM-uMNbE--31K3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4d9ea9eedd.mp4?token=BkVXOzujkR-pK4BwWTzv4crW464g4Cl2PXkXzh7F9QLqBFbFGhKZlOw8yudEM3WFJUtaa4Hv5BL15_qoJ3NdmLY_X-b2qeEHorOsOFkrrPGBpUibOUT8vl8ZOKGd5FepSrKXElDZLr9Z9YyBBsSM7KZpCD_e_hHe5rp8UcnZ_ynUajMci13vP9zdIsGncCdySVH1YbWroHm42EYMmM1t9Ii8PLb0uUYlq46YLezxn2d4eH8aDUt-TnnoXZM12F1CG7iSBy9Tjz6PA5z97H9ONCEuFTYlJ-2dF6bk78d7y5qhWp36hP_Cr8mSwzk08KTRN4AO58qDM-uMNbE--31K3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: حمله به فرودگاه ایرانشهر در سیستان و بلوچستان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77160" target="_blank">📅 23:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77159">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پیام‌های دریافتی:
سلام داش ایرانشهر فرودگاهشو دوباره زدن ساعت ۲۳:۰۱
پنج دقیقه پیش دوباره فرودگاه ایرانشهرو زدن
سلام  ده دقیقه پیش فرودگاه ایرانشهر رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77159" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77158">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y8fYYtoIp2eZd5Hw337A7m9kP8NPv5dGkxUDwb9QoGVTPjpKfn_kcWehhACaSSD0FNKbUKT1ClTmzRjKtp6Dyl71TZjRFMsiq9mO2inHMxwRpI2esSP4xitbpi3WQT4yovvrHt0UfMT2xMhTjlGlOkNXmjSkgjBkeBLi9KBcoWptim3aG_8NrWNyFFE9a8CtN2m3jwb-lR81_unlMwccTT2xNpP7JR7FEY_snYfc8LvD7m6mIVXF_ZPFvEjt-GtK95LwiNmz3b0KzmgmX4eeN6f1QvhqADx7wNbjRhODFDYPhP_BgeVJG2YrdCONlfW5TF4sbfM9wpJooxXdM2Y3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم:
مصدومیت ۷ نفر در حمله دشمن آمریکایی به بندرعباس
🔹
به گزارش خبرنگار خبرگزاری تسنیم: در پی حمله دقایق پیش نیروهای متجاوز آمریکایی به محله مسکونی تپه الله اکبر در شهر بندرعباس، متأسفانه تاکنون ۷ نفر از هموطنان مجروح شده‌اند .
🔹
بلافاصله پس از وقوع این حادثه، کلیه نیروهای امدادی و درمانی دانشگاه علوم پزشکی هرمزگان در حالت آماده‌باش کامل قرار گرفته و اقدامات درمانی لازم برای مداوای مصدومین در حال انجام است.
🔹
روابط عمومی دانشگاه علوم پزشکی هرمزگان ضمن محکومیت شدید این اقدام تجاوزکارانه، از عموم مردم شریف بندرعباس می‌خواهد ضمن حفظ آرامش، اخبار را تنها از طریق مراجع رسمی و معتبر دنبال کرده و از هرگونه شایعه‌پراکنی خودداری فرمایند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/77158" target="_blank">📅 23:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77157">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پیام‌های دریافتی:
‌
بندرعباس صدای انفجار شدید ۴ بار
ساعت ۱۱ شب
همین الان صدای انفجار شدید مرکز شهر بندرعباس اومد
سلاام وحید جان
بندرعباس دوتا انفجارر
شرق بندرعباس پایگاه هوایی ۲۳:۰۰ دارن میزنن
الان دو تا صدای انفجار بد آمد بندرعباس
بندرعباس دو تا انفجار صدای دومی مهیب بود ساعت ۲۳
سمت شرق بود
بندرعباس همین الان صدای انفجار
چند دقیقه قبل تر هم یه صدای انفجار اومد
بندر الان اینقدر شدید بود پنجره‌های اتاقم لرزید ۱۱:۰۱
سلام الان ۴ بار با فاصله چند ثانیه خیلی با شدت بندرعباس رو زدن (ما نزدیکای فرودگاهیم)
وحید جان سلام الان ساعت ۱۱ شب قشم هم صدای جنگنده اومد هم ۴.۵تا انفجار که خونرو لرزوند جنگنده تو اسمون میچرخه
باز هم بندرعباس صدای جنگنده خیلی واضح داره میاد دوتا صدای انفجار اومد بلافاصله برق قطع شدد صدای جنگنده اصلا قطع نمیشه
بندرعباس ساعت ۱۱ فکر کنم سمت پایگاه هوایی باشه.
وحید جان سلام ، قشم سمت دهخدا ۳ تا صدای نسبتا شدید شنیدیم.
بندر عباس همچنان داره میزنههه
صدای زیاد و لرزش
برق هم داره نوسان میده
ی مناطقی هم قطع شده
ساعت یازده شب صدای سه انفجار بندرعباس
الآن سه تا صدای انفجار بندرعباس اومد
بندر عباس تو فاصله چند دقیقه ۴، ۵ تا صدای خیلی بلند خونه لرزید ، آخریش ۱۱:۰۲ دقیقه اینا بود
سلام وحید بندرعباس اول برق اتصالی کرد بعد صدای انفجار شدید
وحید سلام دقیقا ساعت ۲۳:۰۰ صدای انفجار بندرعباس
بندرعباس ساعت ۲۳:۰۰ صدای ۴ انفجار خیلی شدید و سهمگین اومد
بندر دوباره زد. بزرگ ولی نه به بزرگی یکی دو ساعت پیش
انفجارهای امشب تو بندرعباس از شب های قبل خیلی بیشتره
واقعا ترسناک بود
به مرکز شهر و نزدیک گلشهر صداش اومد
بندر رو چند بار زد و برق هم قطع و وصل شد
وحید برق نه تنها بندر نوسان داشت بلکه چندتا از روستاهای بندر هم همینجوری نوسان و قطعی داره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77157" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
الان اهواز صدای دو تا انفجار اومد  ۱۰:۳۰
اهواز انفجار دوباره همون ۲۲:۳۱
اهواز ساعت ۱۰:۳۱ دقیقه دوتا صدای انفجار مهیب اومد
وحید جون 10:30 دو انفجار پشت هم اهواز
الان ۲۲ و۳۰ دقه صدای انفجار اومد اهواز
اهواز ساعت ۱۰:۳۰ صدای سه انفجار اومد.
اهواز طبق روال روز های قبل ساعت ۲۲:۳۰ صدای انفجار میاد
صدای سه انفجار شدید
دقت كردين همش سر يه تايمه
😭
😭
😭
😭
دیشب هم دقیقا همین ساعت ۲۲:۳۱ زدن
اهواز ساعت 10:30 زدن سه تا بود
همین الان 22:30 صدای دو انفجار مهیب در اهواز
بازم مثل دیروز راس ساعت 10.31 دقیقه اهواز رو زدن
اهواز ۲۲:۳۰، زدشون از قطعی برق هم آن‌تایم تره
اهواز صدای ۲انفجار ساعت۲۲/۳۱
همین الان اهواز صدای انفجار اومد
ساعت ۱۰/۳۰ شروع شد مثل هرشب
سلام آقا وحید دو انفجار پی در پی اهواز ساعت ۲۲:۳۱
اهواز صدای انفجار دو بار ساعت ۲۲:۳۰
سلام داش وحید اهواز ۲تا انفجار شدید الان
اهواز ساعت ۲۲:۳۱ صدای دو انفجار اومد
دیشب هم دقیقا همین ساعت شروع شد
هر شب راس ساعت ۱۰:۳۰ اهواز میزنن
امشب باز ساعت ۱۰ و نیم و دو تا انفجار شدید
سر ساعت، برنامه زمانبندی خاموشی هم اینقدر دقیق نیست وحید.
🔄
دوبااااررره
وای وحید دوباره دوتا
۲۲:۳۴ دو بار
اهواز ۲۲:۳۴ انفجار مجدد شدید
دوباره دو تا صدا پشت سر هم اهواز ۱۰:۳۵
انفجار ساعت ۲۲:۳۵ اهواز
یه انفجار دیگه 22:34 این یکی شدیدتررر بود.‌یکی دیگه هم دورتر
دوباره الان زدن ۲۲:۳۵ اهواز
اینبار شدیدتر
خیلی وحشتناک بود
سومی و چهارمی الان ساعت ۲۲:۳۵ اهواز باز روی لرزه‌ست
وحید دوتا همین الان اهواز، ساعت ۲۲:۳۵ خیلی صدا بلند بود
اهواز بعد از اون دوتای اول یکی دیگه الان زد ۲۲:۳۵
۱۰:۳۵ یه انفجار مهیب و بزرگ توی اهواز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77156" target="_blank">📅 22:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77155">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q6zlvITq41Lxp1hHXzRZBEgJB04TjLm9LSGRc9G-R_YsZD4CVDon2Uj_sFigvmN-b1iSGFv8LZdikajlBkFVaYEkuIAwn1nFMXj7UTcayrUmvD0-ub6_qFxfSzhZxUTRPaFc2C8J4F_8k66sLPAJ0U8mA7bzHP6NiyAKoGxThym9h_UwazG7fg8i_--_RBvIj8OAZyLjsZPCI4BBTbo1gS1j3gX5vAQdOhZ90I8t3c5hfFTFTFg-P__n3PMtnFvqs3GvsN3gNjfml3AhVFH-L4jBMXgT21odclABcAeMX12LCq_Kw-17VPTCbVSJ64PQFzTIlwCxuVgDuFf_fhveuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
ساعت ۲ بعدازظهر امروز به وقت شرق آمریکا [۲۱:۳۰ به وقت تهران]، نیروهای ایالات متحده برای پنجمین شب پیاپی اجرای موج تازه‌ای از حملات علیه ایران را آغاز کردند تا توانمندی‌های نظامی ایران را بیش‌ازپیش تضعیف کنند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77155" target="_blank">📅 22:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c552ed27a.mp4?token=lTe121xsnpEOKVuob2eQqyThVc5O6HNY8pO_4jITzcFzNGk_DCpFJcHfnCgs3ejszaK-8qYbZvuQsgPg66gyS3skOJDmseIjThEUM2piL_2uFkiEClVkRz-eL2Pr3Qs3n1b1Y10Q9YQQ40caOsvywwrVy8M_U41z3g6Qc3svAs1WEme_SuWFFZNIMLmUbcfo02ZPc65hp7UKYzg8YzU0SX99kt-TMgfpGD4Ak64M0sMxXrl3xgY4AKmGxgxkEVEXGd7JzS-KNxw4r8LzJLR8sxX0HN5StqRjDpHDoTfcoVj0cSDcVV9uUvXmzBwoZc_iSmIFS5YazzCJt6GYF4fROQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c552ed27a.mp4?token=lTe121xsnpEOKVuob2eQqyThVc5O6HNY8pO_4jITzcFzNGk_DCpFJcHfnCgs3ejszaK-8qYbZvuQsgPg66gyS3skOJDmseIjThEUM2piL_2uFkiEClVkRz-eL2Pr3Qs3n1b1Y10Q9YQQ40caOsvywwrVy8M_U41z3g6Qc3svAs1WEme_SuWFFZNIMLmUbcfo02ZPc65hp7UKYzg8YzU0SX99kt-TMgfpGD4Ak64M0sMxXrl3xgY4AKmGxgxkEVEXGd7JzS-KNxw4r8LzJLR8sxX0HN5StqRjDpHDoTfcoVj0cSDcVV9uUvXmzBwoZc_iSmIFS5YazzCJt6GYF4fROQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود از حملات امشب به بندرعباس است. @
farahmand_alipour
پیام‌های دریافتی:
سلام وحید بندرعباس ۲۱:۴۴ صدای میاد نمیدونم پدافنده یا انفجار
سلام وحید جان سه تا انفجار خیلی خیلی وحشتناک همین الان ساعت ۲۱:۴۲ بندرعباس
بندرعباسم
دارن میزنننننننن پشت هم
۹:۴۲ چندتا انفجار شدید بندرعباس
ساعت ۹ و۴۵
بندرعباس ۳ تا انفجار وحشناکک
جلوی خونمون بود
سلام وحید جان، همین الان ساعت ۲۱.۴۲ سه تا انفجار پشت سر هم بندر عباس
سلام بندرعباس ساعت 21:43‌چهارتا انفجار
بندرعباس همین الان چندتا انفجار وحشتناک رخ داد
سلام آقا وحید غرب بندرعباس منطقه ۴ ترکید ۵ تا انفجار فوق العاده شدید
3 تاانفجاربندرعباس
نیروی دریایی ارتش غرب بندرعباس
و ایستگاه رادیویی بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77154" target="_blank">📅 21:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvpQ9KsqLlIWiovKp7uRqnEfg0cC2ZLP_Ul9-9O2Ufy9ixWb3v7G_YbrViaexg3ygDKDL9RwvkShSlSJsjqxN_D7Cyk607zEd5hoewI87rQN1gW2MT_SnCbgpHdaQrOkjxGDCmxMrCU9F-gZ7o9E-sRhCClBJMMDfLNtj8QBR2gQ_JXuh1_wZ4o3mLaEq7b8vM0LrPhFsoER29P9yCg8CId057HOGatpatiwhSrWOuDjn67Br6KiR7IOofDHOYrtEpCTWama88PPEf6fDR4_Tc0TUFt0pzF37hiHliNDmlzlVjHLPeSo7opm-jDDSFGLbAA4Ufbwog_GqBCK1y4xOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس:
🔹
استانداری هرمزگان: در ساعت ۱۸:۱۰ نقطاتی در حوالی قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.
بندرعباس:
استانداری هرمزگان: در ساعت ۱۸:۲۰ و ۱۸:۴۰ نقاطی در حوالی بندر عباس مورد اصابت موشک‌های دشمن آمریکایی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77153" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77149">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hv1TTZZz3FYEN9WLk7WhW9KODHh101a2Jg2DZWHAvJPbQZpBHm6XtwUwRtGxg1fxZijP5PWjRZ_9jQ9VavbKmJDexZKltIGOsP6rMw_WCdBv_M3VgHIk9xmp-6H0stdtSeJoZXCJYfRGXoy8R-uBdw0BTGM_cHO_Qk67sZDJU9lp9aYng2jtlLGKuXIz1AfyaGbiLIXRHpYAQp7lGV6WZKUTMnPoKK7YHsbu0tNQQaYv8ednt-VGdT1eslYYj2Qo8uz3hq_V7HSl_bB6PJBFnoJ_7hKCB6L-1Y5e3p9XKfRObTFj2KzkBnUWI9zylUKQ2jGGffmp4c3wMCAkdugvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jfm-VQm1xH2H5uD1VrbtwB0VCkqTv63FCXHJ64y-wnMVzIV-vz-K0pWJVDznUWgl1pNak4WAu5ojMqvjYXp_XGG5Z5xYUEe9Tm4UPBuOyLNJdNcYsS5kK9__rMEMYOx-j9SKI7B1-x7TULSfAejYTLDixW0TOcJZwnl2DrC6DHr8xx3nf9KjPeB_uRH7uJ0skpOX67RLhxe0DeDl42cV8V2vtBeVURAz2lalAXAwAz2RztAnMijorTZFbkXlrwQ8ksM9OrqhmcwIAbJSAELbQIG-5evJu8kdOXm7g-D6cmMXQ1VHmVCdPCPsXvQ6IAY9Nxyo3N_YdtFm8nqn2bL_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zn9Mbwyt6jMczEcMzrtwAji2qj-7LQNHKHdwP0aCyiOnDChhCXyKR9ALAWijespCY1Mwf2e_tBPLM65koXkHcjBezC-b2vQmQv39Ymrq5kgKk1QIG9L2-P6hqe3wDW8nTRYFS_0sq6Nhd0wZcb7B5MB9pbZzP1kWynWpIuW9nZVd5GS0reVA0ejYWMltc34A_0Ph7cMtHL9VUG3PUG75kxUr3Gz2U2IsIS9fvISrL3NyLIslj0tCOgl-OnpflXB6w-bTxgfTJ-cDDrj_K6UU-m1qy4lTbR2NOykmGeeNUNn-w3Tb3pNnPU9CqlrbOeRhufdNml5quzYo8gllhC6D3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96d56893a8.mp4?token=e4Ku5KI3bGEaEFzVUwIPl3IX2GJBwkBONBll-dA_ebP3SvhnKMbJv-LMNdLXsOufIsHwtRbMpyo6Igq75R0RZwyw4R7EOTEaAV6lo29ifBQYV8PdK0PsMv0wuP_ESj8P_aoX6mlXcpBDfFNvVD7JiNVeCL4TVSghqooqcZpLbTelV1gL-ZFf5dDzcfHeC0iPFPeLiBjLVPTanWCDknD5upewkZv8OoaX4S4-MDlPtNTIOZh1nlL7M--ctAWAhHxa1yxXnIs3BT4LupUvg_iX1q6F_BQyKzAkPVZMGxql8-ZGjyxsZttywcooo4O6cOD-zao_z8oW-EMre0mBjbqXMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96d56893a8.mp4?token=e4Ku5KI3bGEaEFzVUwIPl3IX2GJBwkBONBll-dA_ebP3SvhnKMbJv-LMNdLXsOufIsHwtRbMpyo6Igq75R0RZwyw4R7EOTEaAV6lo29ifBQYV8PdK0PsMv0wuP_ESj8P_aoX6mlXcpBDfFNvVD7JiNVeCL4TVSghqooqcZpLbTelV1gL-ZFf5dDzcfHeC0iPFPeLiBjLVPTanWCDknD5upewkZv8OoaX4S4-MDlPtNTIOZh1nlL7M--ctAWAhHxa1yxXnIs3BT4LupUvg_iX1q6F_BQyKzAkPVZMGxql8-ZGjyxsZttywcooo4O6cOD-zao_z8oW-EMre0mBjbqXMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرستنده تصاویر: پلیس گفت اتوبوس خراب شد پیاده شد تعمیر کنه خلاص بود از ایستگاه پله سوم تا پله اول رو رفت.
آتش‌نشانی: یک اتوبوس متوقف‌شده مقابل پارک ساعی با ۵موتورسیکلت و ۲خودروی سواری برخوردکرد.
اتوبوسرانی: بدون مسافر بود و پس از عملیات امدادی و رفع نقص فنی درحال جابه‌جایی بود.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77149" target="_blank">📅 19:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77148">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e1540b68c.mp4?token=vOkuMO6vBwzAmZBfiA-wvC3Sl7cR098qPZDjnRUFYSXIeVu1UNe7pBBeRYIjLYDsjt1jf93k8J_Z5DUEW27Q5e6p4mslKcJLrhulU8Q7npNIIZEKOauunNBPBVhP72GywB1Mqw1r0J2N_HJXn_GCFCwy3lKTAvd891JBZG3HWF-j2QffTQpzY5N7gpX7pf819x3P2DPw35c0nNEoP9W5eCkJU3_fFa7KsH770mC8UuqB4IzpOvcaVB4Qc_FAJKqLGx84Q9ziMORoW7Ldl8lRHBNobiKeDvWGptwBJv1zt1hHglfvAorvANvCK-uNg81zRsz3nkPQzA0p_rWv28GZllnFzloGcwa9S8dPPXIur7_C6yDBBkAPz0SJGjP6DlJNqytNzm49zLojIKCZl6gvGeM7TztffdFyAlxHot7a2VclDcf8QXpYh7b0gf2bammZuFcNDZu1iO_1jRLee0rZvYxGMcGBafRqQ-xS5y8T97Y5R6Qo_tinzBspQ4j-EQVFGjq21yoLBx3RZeVT5boF1D4holejY-UzUePeqImA02zocgJ55xDaOcnfXAyuyfoCzK6XgRWzBZs9dFRRsNRcuxRsPhohg4cFP-t1aAL_b59OwGrtgfaEnFJmxogRvb3hewKRdc2FVXIJEkaYDWgg4aCXhlIEaM4ElMZORK_JLhc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e1540b68c.mp4?token=vOkuMO6vBwzAmZBfiA-wvC3Sl7cR098qPZDjnRUFYSXIeVu1UNe7pBBeRYIjLYDsjt1jf93k8J_Z5DUEW27Q5e6p4mslKcJLrhulU8Q7npNIIZEKOauunNBPBVhP72GywB1Mqw1r0J2N_HJXn_GCFCwy3lKTAvd891JBZG3HWF-j2QffTQpzY5N7gpX7pf819x3P2DPw35c0nNEoP9W5eCkJU3_fFa7KsH770mC8UuqB4IzpOvcaVB4Qc_FAJKqLGx84Q9ziMORoW7Ldl8lRHBNobiKeDvWGptwBJv1zt1hHglfvAorvANvCK-uNg81zRsz3nkPQzA0p_rWv28GZllnFzloGcwa9S8dPPXIur7_C6yDBBkAPz0SJGjP6DlJNqytNzm49zLojIKCZl6gvGeM7TztffdFyAlxHot7a2VclDcf8QXpYh7b0gf2bammZuFcNDZu1iO_1jRLee0rZvYxGMcGBafRqQ-xS5y8T97Y5R6Qo_tinzBspQ4j-EQVFGjq21yoLBx3RZeVT5boF1D4holejY-UzUePeqImA02zocgJ55xDaOcnfXAyuyfoCzK6XgRWzBZs9dFRRsNRcuxRsPhohg4cFP-t1aAL_b59OwGrtgfaEnFJmxogRvb3hewKRdc2FVXIJEkaYDWgg4aCXhlIEaM4ElMZORK_JLhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خون در ۲ ثانیه اول)
صدای ویدیو: "اتوبوس ترمز برید، هرچی موتوری بود رو زیر گرفت رفت. خیابون ولی‌عصر"
به خودروهای پلیس هم برخورد کرد.
Vahid
تهران، پنج‌شنبه ۲۵ تیر
via @
iliaen
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77148" target="_blank">📅 18:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77147">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/71f1bffd36.mp4?token=huCTVr_FtBeHwHTbp8nwUcY6lMG_mOj8CkFWmPm4HBXeseNS-yQBam_9owDrYbG5-jGVfWdUS_YElD365R2pyMY_0XcPRTWmYmPhY2daxd57NkhzBWfDI345Mfd8T9cDVm4E4FRiS_jNZP9sshBA-XIeMA9aVXCP9KpoPM9A0hOSWldfJhoietzbNzkn7cupTlju68kPNHxj2ThBFC40Qv9QsiM4qEuVl_zJQD2RC5q0mndqTCd7WElZ1VrkRIywQSW18UB6B6DED2zVB_ne-lm3vwnp5m-cBWbylfZp9ANBX_bYodzylve2XT4mWCAIHNnr_N_4MIZBw1IlsHEMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/71f1bffd36.mp4?token=huCTVr_FtBeHwHTbp8nwUcY6lMG_mOj8CkFWmPm4HBXeseNS-yQBam_9owDrYbG5-jGVfWdUS_YElD365R2pyMY_0XcPRTWmYmPhY2daxd57NkhzBWfDI345Mfd8T9cDVm4E4FRiS_jNZP9sshBA-XIeMA9aVXCP9KpoPM9A0hOSWldfJhoietzbNzkn7cupTlju68kPNHxj2ThBFC40Qv9QsiM4qEuVl_zJQD2RC5q0mndqTCd7WElZ1VrkRIywQSW18UB6B6DED2zVB_ne-lm3vwnp5m-cBWbylfZp9ANBX_bYodzylve2XT4mWCAIHNnr_N_4MIZBw1IlsHEMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77147" target="_blank">📅 18:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77146">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FFLwi1b0k-ELOkA9JuPy6RkMvDx13xaOQhQri6lLXk5pYwbLpMZ3I4CkdSuNu6dVKnUovOCinfCf-V6Aj-VhQo-sNpMJZdv5m56uXsDq-ku1RHe85d_WEGg3ypuJ1Pi-ldqx_VdUIkMTeDp-DBQBurRDxDslPOjPxU69F5AzcldC3WELvQTfMNjAxtCzPQwLTv5NdcIAknpvznG2VpY8HOyL-pZm_S57rnFdeGBSIwlIUBw0g7tNrbENxm0o-JB1iQfFwGJn2rt-uDf7vaIQOMyKhgFzRxNstkD6Y6eHBbWovwGYC_vv7vO87BBYwrZjD4YHtv2bHOAVgw71LUkcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام استانداری سمنان:‌ در حملات بامداد پنج‌شنبه فرودگاه سمنان نیز هدف حمله هوایی قرار گرفته است.
محمود قدرتی، مدیرکل امنیتی و انتظامی استانداری سمنان، ادعا کرده که در این حمله یک سوله جانبی در محوطه فرودگاه هدف اصابت موشک قرار گرفت و بخشی از شیشه‌های ساختمان اصلی ترمینال نیز آسیب دید.
به گفته او، این حمله در ساعات اولیه بامداد رخ داد و تلفات جانی نداشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77146" target="_blank">📅 18:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77145">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIjyJIEjvgqYSgEwsuzS0iZE4-PdMJlefUkO-2-1tkf5HUPLeycpnAVzRIQhCl84PxItTjvm6yRrIAn8BEUsN06goCDKcLBEjmxNNeK9avTOGetgwpq8aADm0OxR_4sWx-tS8ZcJPOrz_0LEeEG7OXwEOm5oq909VfMaJ2N-vSbPl6oyopod_udws4InYeqFswonRnPuxoKz2UjMyRJXITuNF-XFyWe-XSA5ctttimn87l7x0VcF_EDI51RaojuOzK3cBBh3FBsGMAwEs2JGCrBpo9CJKnGEp0xXCUtSxiv4ZjL-cyzjxooY_BCviMEcUgCZGyI2wccWbFypbx3Jng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امنیتی به خبرگزاری فرانسه گفت که روز پنج‌شنبه ۲۵ تیرماه پهپادی به یک کشتی «حامل خودروهای آمریکایی» در نزدیکی یک ترمینال نفتی برخورد کرد. گزارش شده این کشتی از امارات متحده عربی آمده بود.
همزمان چهار منبع نفتی و امنیتی عراق به خبرگزاری رویترز گفتند که روز پنج‌شنبه بارگیری نفت خام در تمام پایانه‌های عراق پس از برخورد یک پهپاد با یک نفتکش در پایانه بصره متوقف شد.
در واکنش به این گزارش‌، سخنگوی وزارت نفت عراق با اعلام این‌که بارگیری نفت خام در پایانه‌های جنوبی عراق همچنان ادامه دارد گفت که در حال بررسی گزارش‌های مربوط به سقوط یک «شیء» نامشخص بر روی یک نفتکش هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77145" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77144">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbiqaZBkWsH5iIpzlx8-viGRtvwtQkv1_j3at3o4t5ws7irZVj7LL7H9_qDNqjiATuN8KUCO03DSo3w0GTxpvlhMK9Jp6a5tIV1XTShIhIWxn4Yi8j58XdEJFdUX7pvoKGNLTs2slxgeTZB1bGCOekJRrbh3HjOO3FtX7HGaSjJivgjgrsEyvS9G-o9WZPS2-saHyGU6cioawepeMMF9lIu29Dce0ALmMlv5iqyWWvHkykHEoIUPWedP8NMDacJsE9-MoALvEnMO1a3gk2sGiW45caUVnCO8Q3EHMa93ZGecoeYwOJBg0nvRj6SDy5uxI2kFflbaHj-NCf-6hTEblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی، وزیر خارجه لبنان، می‌گوید تصمیم برای پایان‌دادن به نقش نظامی حزب‌الله در این کشور یک تصمیم حاکمیتی و مستقل لبنان بوده و پیش از توافق اصولی اخیر با اسرائیل اتخاذ شده است.
آقای رجی روز پنجنشبه ۲۵ تیر گفت که این تصمیم زمینه را برای توافقی فراهم کرد که ماه گذشته با میانجی‌گری آمریکا میان لبنان و اسرائیل حاصل شد.
او با تأکید بر این‌که لبنان «تصمیم خود را گرفته است»، گفت دیگر بازگشتی به «دوگانگی حاکمیت» وجود نخواهد داشت و جایی برای سلاح خارج از چارچوب مشروعیت دولت یا تصمیم‌گیری خارج از نهادهای رسمی کشور نیست.
رجی همچنین گفت استقرار ارتش لبنان در سراسر خاک این کشور، موضوعی جدایی‌ناپذیر از خروج کامل نیروهای اسرائیلی از همهٔ مناطق اشغالی لبنان است.
حزب‌الله که تحت حمایت جمهوری اسلامی ایران است، از سوی آمریکا یک سازمان تروریستی شناخته شده اما اتحادیه اروپا تنها شاخهٔ نظامی آن را تروریستی می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77144" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77143">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CU-CVYZaA7OoKAifCpBVnioRMWPOzuhlHFuZfj25vub10EKJe9dTqylm4TBbGpSFPJK5577_3rwzcHx6YU2hxBmSR0A0QqUkzHSsxw3x30h3Fg-zdNvi4QfwKP8uDVfCgixFrbWBpRBKZwSr3HD_RrUvl2qwqZA3fX_kVt3XpC02JHhrWfKGvnYOuMZwhT0HOeQMQWHOpCqPs9FP-Y83S268URJXz7FSHJsru39GBSQtwSFXPL2B6dfK_DPDL-JWdPC1rreh_2KDwug0JqX295aG-BdCR0z2UBjz5pksCFOfLzIWP9O8Z9GVkn38PACUHf6t8W7yf-34UwD2m0U4ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت جورنال به‌نقل از چند مقام آمریکایی گزارش داد که دونالد ترامپ پس از چند جلسهٔ توجیهی با دستیاران ارشد خود، به گسترش عملیات نظامی ایالات متحده در ایران متمایل شده است.
به‌گفتۀ این مقام‌ها که نام‌شان اعلام نشده، گزینه‌های مطرح‌شده شامل افزایش حملات هوایی، اعزام نیروهای زمینی برای تصرف جزایر ایرانی در نزدیکی تنگه هرمز و بمباران یک تأسیسات هسته‌ای مستحکم و مخفی است.
به‌نوشتۀ این روزنامه، دونالد ترامپ عصر سه‌شنبه به وقت آمریکا میزبان جلسه‌ای در اتاق وضعیت کاخ سفید بود تا در مورد تصرف احتمالی جزیرهٔ خارگ و سایر مناطق در امتداد تنگهٔ هرمز با استفاده از نیروهای آمریکایی و همچنین بمباران احتمالی یک مجتمع تونل در کوه کلنگ گزلا که به پیکاکس یا کوه کلنگ معروف است، بحث کند.
کوه کلنگ گزلا محل یک تأسیسات هسته‌ای عمیق و مخفی ایران نزدیک نطنز است که تاکنون هدف حملات آمریکا قرار نگرفته است. وال‌استریت جورنال می‌گوید گسترش حملات هوایی علیه اهداف بیشتر در ایران، از جمله نیروگاه‌ها، نیز همچنان محتمل است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77143" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77142">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81194af4f8.mp4?token=SQeW-_RvI8yS_llSHysvMjQ2bqn2klYH93W7UJWWUpO5fokTkghBRUzK90rfSWRK6PDE9JzdmX0ZiGqS15L8ejsUbgv3U9C7ybaOIVCK97b63P7GKhKtyldf3eadVN2FMyEFnxDAMeZgj3QoPRyAuSnpQtB3mltHGTIxY2TP2dW42OQc0jWCphiLvTRCz2Ij4yAX62WOwNLn4OvsNKGonRqU0Zukz5wsZga-yU6eNqPUTEC8L8UuWjrEpDti0OyPeapJ_frQKxtWvp80rk_jCe35Y4ttehNvS5MFWs86OY8CuG7_o4iAEmhuR2sHk9b02Q4GDRqNkBITXYhJCyIJ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81194af4f8.mp4?token=SQeW-_RvI8yS_llSHysvMjQ2bqn2klYH93W7UJWWUpO5fokTkghBRUzK90rfSWRK6PDE9JzdmX0ZiGqS15L8ejsUbgv3U9C7ybaOIVCK97b63P7GKhKtyldf3eadVN2FMyEFnxDAMeZgj3QoPRyAuSnpQtB3mltHGTIxY2TP2dW42OQc0jWCphiLvTRCz2Ij4yAX62WOwNLn4OvsNKGonRqU0Zukz5wsZga-yU6eNqPUTEC8L8UuWjrEpDti0OyPeapJ_frQKxtWvp80rk_jCe35Y4ttehNvS5MFWs86OY8CuG7_o4iAEmhuR2sHk9b02Q4GDRqNkBITXYhJCyIJ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در پاسخ به پرسشی درباره تهدیدهای مطرح‌شده از سوی ایران علیه جانش، گفت که به این موضوع «اصلا فکر نمی‌کند».
او در گفتگو با فاکس بیزینس تاکید کرد: «اگر به این مسائل فکر کنم، دیگر نمی‌توانم مؤثر باشم.»
ترامپ افزود این کار را دیگران انجام می دهند و به نظرم در این زمینه عملکرد خوبی دارند و تاکید کرد خودش به این موضوع اصلا فکر نمی‌کند.
@
VahidOOnLine
او همچنین تاکید کرد که می‌تواند سپاه پاسداران را به همان شیوه‌ای از بین ببرد که در دوره نخست ریاست‌جمهوری خود داعش را در عراق و سوریه شکست داد.
ترامپ گفت: «ما در وضعیت خوبی خواهیم بود. آن‌ها تضعیف شده‌اند. تسلیحاتشان ۹۱ درصد کاهش یافته است. توان پهپادی آن‌ها به‌شدت کاهش یافته است. هنوز مقداری دارند، اما زیاد نیست. ظرفیت تولیدشان کاهش یافته است. پرتابگرهای راکتی و پرتابگرهای موشکی آن‌ها به‌شدت کاهش یافته‌اند. موشک‌هایشان هم به‌شدت کاهش یافته‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 472K · <a href="https://t.me/VahidOnline/77142" target="_blank">📅 09:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77141">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نیم ساعت از
سه ساعت
گفت‌وگوی جی‌دی ونس با جو روگن، بخش مرتبط با ایران
جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگو با جو روگن از آنچه «جنگ‌طلبان» در آمریکا و دیگر کشورها خواند، انتقاد کرد و گفت این افراد با صرف هزینه‌های گسترده تلاش می‌کنند مذاکرات دولت دونالد ترامپ با جمهوری اسلامی را به شکست بکشانند و افکار عمومی آمریکا را تغییر دهند.
ونس با دفاع از رویکرد دولت ترامپ، تاکید کرد دیپلماسی برای حل بحران حمله‌ها به کشتی‌رانی در تنگه هرمز ضروری است و گفت در کنار اقدامات نظامی، گفت‌وگو تنها راه رسیدگی به این بحران است.
@
VahidOOnLine
بخش پرواکنش‌تر:
... من دو چیز را از میان سطرها می‌خوانم. فکر می‌کنم بعضی از آن‌ها می‌خواهند حکومت ایران به‌طور کامل تغییر کند؛ روحانیان سرنگون شوند و فردی بسیار دوستانه‌تر جایگزینشان شود.
ببین، تجربهٔ ما از انجام چنین کاری چیست؟ خوب نبوده. خوب نبوده. خوب نبوده.
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، تصمیم با خودشان است؛ اما ما ۱۵۰ هزار نیروی زمینی نمی‌فرستیم تا تغییر یک حکومت را رقم بزنیم، مگر اینکه مردم داخل کشور خودشان خواهان چنین نتیجه‌ای باشند.
در هر صورت قرار نیست نیرو بفرستیم؛ اما پیشنهاد اعزام نیرو یعنی عملاً می‌گویی ارتش آمریکا باید کار مردم ایران را برایشان انجام دهد. ما دیگر در این کار نیستیم. واقعاً نیستیم.
نتیجهٔ دومی که فکر می‌کنم بعضی‌ها خواهانش هستند ــ چه خودشان آگاه باشند چه نه ــ چیزی است که من «نتیجهٔ لیبی» می‌نامم.
اگر به نتیجهٔ نهایی سیاست ما در لیبی پس از کشته‌شدن قذافی به دست دولت اوباما نگاه کنی ــ باز هم تصمیمی بسیار احمقانه ــ چه اتفاقی افتاد؟ لیبی عملاً به کشوری شکست‌خورده تبدیل شد. بحران پناه‌جویان به وجود آمد. مردم به اروپا سرازیر شدند، به بخش‌های دیگر آسیا و آفریقا رفتند. خشونت و تروریسم زیادی از دل آن بیرون آمد.
فکر می‌کنم افرادی هستند که می‌خواهند همین نتیجه در ایران رخ دهد. اما باز می‌پرسم: چه چیزی به سود ماست؟ چطور به سود ایالات متحده است که ۹۴ میلیون انسان درمانده به اروپا و ایالات متحده سرازیر شوند و زیرساخت‌های تروریستی که وقتی تروریست‌ها را در سراسر جهان پراکنده می‌کنی، می‌تواند شکل بگیرد؟
ما قبلاً این آزمایش را انجام داده‌ایم. سیاست کنونی ما و هدفی که دنبال می‌کنیم این است که تنگه را باز نگه داریم و جریان آزاد نفت و گاز را تضمین کنیم. بدیهی است که می‌خواهیم مانع داشتن برنامهٔ تسلیحات هسته‌ای توسط ایران شویم و از ابزارهای دیپلماسی و قدرت نظامی برای رسیدن به آن استفاده کنیم.
بیشتر متن زیرنویس ویدیوی بالا (تا سقف تعداد کاراکتر مجاز):
telegra.ph/Vance-07-16-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 482K · <a href="https://t.me/VahidOnline/77141" target="_blank">📅 06:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77140">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/858e125a28.mp4?token=PWfeCcYWtOWAw80158lwHV1HG621PdbjA99YpsAqXP1xcspPkrnk_cw6E9ta0hEJ5y3h3ekVU-FTdGnXbvoTWDL-DiJOdXtvY9jMr-j833j_bxMHkIyWXYEcOU4KoLx3MremMLox-pesTbv75qiF0FDjDKeGWvLTx1Eh67leMYWZVK0qITOjv9y0q5hRGhxRCjprHeoA8VVPMjvQl0xtET7214EGtmgiJ8yCqtf_Mepw6nLbroFMrdhObasCdpzvIC8UAb12Kz3xpJNEM1t9xZFkOR7PUf7fLgkKbT9FJtj_bgqmfDhnLt0I9Whk7iHYcFbkZsIIkZsVXaUpL_uZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/858e125a28.mp4?token=PWfeCcYWtOWAw80158lwHV1HG621PdbjA99YpsAqXP1xcspPkrnk_cw6E9ta0hEJ5y3h3ekVU-FTdGnXbvoTWDL-DiJOdXtvY9jMr-j833j_bxMHkIyWXYEcOU4KoLx3MremMLox-pesTbv75qiF0FDjDKeGWvLTx1Eh67leMYWZVK0qITOjv9y0q5hRGhxRCjprHeoA8VVPMjvQl0xtET7214EGtmgiJ8yCqtf_Mepw6nLbroFMrdhObasCdpzvIC8UAb12Kz3xpJNEM1t9xZFkOR7PUf7fLgkKbT9FJtj_bgqmfDhnLt0I9Whk7iHYcFbkZsIIkZsVXaUpL_uZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام،‌ ترجمه ماشین:
تازه‌ترین موج حملات آمریکا علیه ایران پایان یافت
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) موج حملات شامگاهی علیه ایران را ساعت ۹ شب به وقت شرق آمریکا [۴:۳۰ تهران] در ۱۵ ژوئیه پایان داد.
نیروهای آمریکایی مراکز فرماندهی، مواضع پدافند هوایی، توانمندی‌های موشکی و پهپادی و تأسیسات نظارت ساحلی ایران را مورد حمله قرار دادند تا توانایی ایران برای تهدید دریانوردان بی‌گناهِ خدمه کشتی‌های تجاری عبوری از تنگه هرمز را بیش از پیش تضعیف کنند. سنتکام برای حمله به مواضعی در چندین نقطه، از جمله بندرعباس، از مهمات هدایت‌شونده دقیق استفاده کرد.
پیش‌تر در صبح امروز، نیروهای آمریکایی طی یک موج حملات ۹۰دقیقه‌ای، مواضع دفاع ساحلی و موشک‌های کروز در جزیره تنب بزرگ را هدف قرار دادند.
ارتش ایالات متحده به دستور فرمانده کل قوا، ایران را پاسخ‌گو می‌کند.
CENTCOM
منابع حکومتی:
اطلاعیه شماره ۱۵
🔸
رادار پیش‌هشدار سامانهء C-RAM در پایگاه علی السالم کویت و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا آماج حملات ترکیبی قرار گرفت‌
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
مردم غیور و بپاخاسته ایران!
🔹
در پی تجاوزات شب گذشته دشمن به نقاطی از سواحل و شهرهای جنوبی کشور، فرزندان دلاور و قهرمان شما در نیروی دریایی و هوافضای سپاه، در موج هشتم عملیات نصر ۲ بارمز مبارک یا زینب کبری (س)، در یک عملیات ترکیبی با استفاده از توان موشکی و پهپادی خود، رادار پیش‌هشدار سامانهء C-RAM را در پایگاه علی السالم و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا را آماج حملات خود قرار داده و درهم کوبیدند.
🔹
بار دیگر به مردم شریف کویت یادآوری می‌کنیم که این جنایات توسط آمریکا با استفاده از خاک شما علیه ایران مسلمان انجام می‌شود.
🔹
از شما برادران و خواهران مسلمان انتظار داریم کشورتان را از وجود متجاوزان پاک کنید و با عمل به وظیفه اسلامی، شرف و عزت تاریخی خود را حفظ نمایید.
سپاه درباره
صدای پاکدشت
: پدافند بود. هیچ اصابتی نبود
🔸
اطلاعیه سپاه حضرت سیدالشهدا علیه السلام استان تهران درباره صدای شنیده‌شده در پاکدشت؛
روابط عمومی سپاه حضرت سیدالشهدا علیه‌السلام استان تهران:
🔹
دقایقی پیش صدای انفجاری در محدوده شهرستان پاکدشت شنیده شد که بررسی‌های میدانی و نظامی نشان می‌دهد این صدا ناشی از عملکرد سامانه‌های پدافند هوایی در منطقه پارچین بوده است.
🔹
ضمن تکذیب قاطع ادعاهای برخی رسانه‌های معاند و جریان‌های سلطنت‌طلب در خصوص وقوع هرگونه اصابت، هیچ‌گونه حادثه یا اصابتی در منطقه صورت نپذیرفته و فعالیت‌های مذکور در راستای آمادگی و عملکرد پدافند هوایی بوده است.
🔹
از مردم عزیز ضمن حفظ آرامش، اخبار مربوط به این رویداد را تنها از طریق رسانه‌های رسمی دنبال کرده و از توجه به شایعات هدفمندِ رسانه‌های بیگانه که با هدف ایجاد التهاب و ناامنی روانی منتشر می‌شوند، خودداری کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 478K · <a href="https://t.me/VahidOnline/77140" target="_blank">📅 04:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77139">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیام‌های دریافتی از تهران
احتمالا همگی درباره صدای پدافند:
صدای پدافند میاد ساعت ۳:۵۱ یوسف اباد تهران
تهران انفجار 3:50
پدافند تهرن داره کا میکنه ۳و۵۱
تهران یوسف اباد صدای پدافند
نارمک صدای پدافند ۳:۵۱
سلام وحید جان مرکز تهران صدای پدافند میاد الان شروع شد
.
تهران صدای پدافند
همین الان صدای پدافند شرق تهران
سلام خرم اباد صدای یدونه انفجار اومد
تهران مرکز شهر صدای پدافند
۳:۵۰
البته زیاد نبود، چندتا بود
وحید ساعت ۳:۵۱تهران نارمک صدای پدافند
داداش تهران سید خندان صدا پدافند ساعت ۳:۵۰
پدافند تهران میدون شهدا داره کار میکنه
صدای پدافند ساعت 3:51 مرکز تهران
تهران سهروردی صدای انفجار از دور تقریبا
صدایی شبیه پدافند از دور شنیده میشه، اختیاریه، ۳:۵۱
تهران عباس آباد پدافند ساعت ۳:۵۰
پاسداران تهران صدای پدافند
سلام همین الان پدافند سمت میدان امام حسین فعال شد
۳:۵۱ دقیقه
من ميرداماد تهران هستم
الان دارن ميزنن
٢ تا صداي بلند و بعدش ٥-٦ تا  كوچكتر
سلام.تهران پیروزی صدای پدافند ۳:۵۲
وحید سمت سهروردی صدا پدافند شنیدیم 3:52
سلام سمت سیدخندان همین الان صدای انفجار شنیده شد
سلام ! ساعت ۳:۵۱ دقیقه سمنان صدای جنگنده میاد
الان ساعت ۳:۵۱ صدای سه تا انفجار اومد تهران
سمت غرب صدا شنیدم
وحیدجان سلام الان ۳:۵۲ تهران محله نیروهوایی صدای پدافند
مرکز تهران. یه صدای انفجار اومد (دور بود) بعدش صدای پدافند ۳:۵۱
سلام وحید جان شرق تهران سمت فدک ۳:۵۲ صدای پدافند به گوش رسید نمیدونم کجاست
سهروردی سه تا صدای بلند متوالی اومد ولی منشأ رو نمیدونم و دور بود انگار
سلام وحید جان غرب تهران سمت فرودگاه صدا پدافند و جنگنده میاد
فعال شدن پدافند در تهران محله دبستان ساعت ۳:۵۰ بامداد
سلام ۳:۵۲ دقیقه سمت گیشا هم صدای پدافند میاد
من میدان سپاهم
صدای انفجار یا پدافند! من تشخیص نمیدم از دوره
ساعت ۳:۵۰
سلام‌وحید جان سمت امیر آباد شمالی صدا پدافند داره میاد
سلام وحید جان تهران شریعتی سمت میرداماد صدای پدافند اومد نزدیک نبود خیلی
سلام وحید جان ساعت ۳:۵۱ دقیقه میدان شهدا چهار پنج بار صدای پدافند اومد
صدا پدافند بود فکر کنم
تهران محدوده خیابون امام خمینی
ساعت ۳:۵۰
وحید سلام توانیریم، صدای پدافند ونک دو دقیقه پیش
سلام تهران الان ساعت 3:53 هم صدای پدافند میاد هم روی اسمون نورش معلومه
سلام وحیدجان سمت شرق پدافند زدن اما قبلش یه صدای بلندی اومد اما نمیدونم زدن یا نه چیزی دیده نمیشه
3:50صدای پدافند شرق تهران
سلام ، غرب تهران (پونک) صدای انفجارها پشت هم و خفیف از دور میاد
سلام وحید جان
شرق تهران الان انگاار صدای انفجار اومد . مطمئن نیستم چون خواب بودیم ولی شبیه صداهای اسفند ماه بود
ساعت ۳.۵۱ صدای پدافند تهران خ شریعتی
کوتاه بود
سلام وحید جان الان ساعت ۳.۵۴ صبح ۲۵ تیرماه صدای پدافند گیشا
تهران شوش پدافند ٣:٥٣
غرب تهران 3:51 چندتا انفجار پشت سرهم شنیدیم
الان باز شروع شد ساعت 3:56
همین الان ساعت ۳ و ۵۵ دقیقه دوباره صدا اومد سمت هفت تیر
۳:۵۶ دوباره صدای پدافتد یا شلیک سمت نارمک
۳.۵۶ امیراباد شمالی دومین بار پدافند
از اختیاریه، ۳:۵۶؛ چند تا صدا شنیده شد با صدای قبلی فرق داره که پدافند بود [پدافندها انواع متفاوتی هستند با صداهای متفاوت]
وحید ۳:۵۶ شرق تهران صدای پدافند - تو ۱۰ دقیقه گذشته دومین باره
تهران شمس آباد  نزدیک کلانتری مجیدیه همینطور صدای پدافند میاد
سلام مجیدیه شمالی صدای پشت سرهم پدافند میاد  حدود ۴ صبح
سلام وحید جان. مرکز تهران صدای پدافند مکرر اومد.
وحید جان ، ساعت ۳:۵۱ دقیقه بامداد اتوبان حقانی صدای پدافند بسیار کوتاه
داداش همین الان  ۳:۵۵ حدود ۱۰ بار صدا امد  ولی زیاد نزدیک نبود یوسف اباد
+ ده‌ها پیام مشابه دیگر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 469K · <a href="https://t.me/VahidOnline/77139" target="_blank">📅 03:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77138">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیام‌های دریافتی:
خرم آباد صدای انفجار
سلام ساعت 3:48 صدای انفجار در خرم آباد
وحیدخان از بروجرد انگار موشک زدن صدای غرش سریع و شدید تو آسمون اومد
خرم آباد ۳.۴۷ صدای انفجار یهویی و نسبتا شدید
خررم آباد به شدت صدای انفجار اومد
کل ساختمونمون لرزید
سلام وحیدجان ۳:۴۷ خرم اباد صدا اومد
سلام وحید جان خرم اباد لرستان ساعت ۳ و ۴۷ دقیقه انفجار
🔄
دوباره زد خرم اباد رو ۳:۵۷
سلام وحید جان همین الان صدای افنجار اومد دوباره خرم اباد
سلام وحید جان بروجرد الان ی صدای مهیب امد. من هدفون داشتم درست متوجه نشدم بعدشم صدا موشک یا جنگنده امد
آقا وحید بروجرد صدای خیلی قوی صدای واقعا عجیب و قوی،واقعا نمی‌دونم انفجار بود یا دوباره شلیک بالستیک،صداش از رعد و برق بدتر بود
خرم آباد دوباره صداي انفجار
دومین انفجار در خرم آباد ساعت 3:57
بروجردو ۳:۵۵ زدن
انفجار خیلییی قوی
سلام وحید جان از بروجرد صدای شدید و یهویی اومد (ساعت ۳:۵۰ صبح)
طبق تجربه، صدای شلیک موشک بود
داداش الشتر لرستان دوبار صدا اومد معمولا از اینجا موشک پرتاب میکنن یبار 3 و 47 دقیقه یبارم حدودا 3و  56 دقیقه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77138" target="_blank">📅 03:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77137">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان تو ارومیه صدای انفجار اومد از سمت کوه های اطراف شهر
همین الان یه صدای انفجار با لرزش خارج از شهر اومد (ارومیه) بعدش با صدای بلند مثل صدای موشک یا جنگنده تو هوا
ارومیه صدای انفجار اومد دقایقی پیش با صدای جنگنده [احتمالا صدای موشکه]
خارج از شهر ارومیه نزدیک مرز صدای جنگنده میاد همین الان
سلام وحیدجان، دوباره از تبریز موشک زدن
سلام وحید. الان ۳:۴۶ از تبریز موشک زدن
۳:۴۶ دقیقه همین الان یه موشک از طرفای اسکو آذربایجان شرقی بلند شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77137" target="_blank">📅 03:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77136">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">استان تهران، صدای پدافند:
سلام وحید جان الان ساعت ۰۳:۲۷ صدا انفجار اومد سمت پاکدشت
اقا وحید همین الان پدافند پاکدشت کار کرد بدجور
صدای انفجار پاکدشت ۳:۲۵
۳:۳۰ سمت پاکدشت داره صدا میاد
سلام صدای انفجار و پدافند حدود دو سه دقیقه پیش داخل پاکدشت
پارچین و پاکدشت انفجار سنگین
خیلی صدا شدید بود
فکرکنم پارچینو زد
۳/۳۰ چندین انفجار در پارچین
سلام وحید
ساعت۳:۲۰ پاکدشت صدا پدافند اومد شدید
دوباره الان ساعت ۳:۳۰ داخل پاکدشت صدا انفجار میاد
دارن میزنن پارچین رووووو
صدای پدافند میاد
۸ بار صدا اومد
سلام وحید جان پدافند پارچین فعال شد همین الان و صداش پاکدشت شنیده شد
سلام دوتا ویکی الان3.31دقیقه.صداتا قرچک ورامین امد
البته اول چهارپنجتا انفجار شنیدم که احتمالا انفجار گلوله.های ضدهوایی بود
شریف اباد پشت پارچین صدا شدید پدافند میاد ۳:۱۸
ما صبح امتحان نهایی ریاضی داریم یه دوازدهمی همینجوری از استرس دارم میمیرم
و یه صدای انفجار اومد همین الان پاکدشت چند بار 3:30
صدای پدافند میاد آقا وحید شدید
🔄
همین الان پدافند رگباری سمت پاکدشت ۳:۴۳
همچنان ۳:۴۲ ضد هوایی شدیدا فعاله
ساعت ۳ و۴۳ دوباره فعالیت شدید پدافند توی پاکدشت
🔄
دوباره صدای پدافندا شدید تر شد
از سمت پارچینه
۳:۴۵ شدیدتر
دیگه همینجوری هست
هر موقع تموم شد میگم
😂
صدای جنگنده ساعت ۳ و ۴۶ دقیقه
بازم انفجار شدید خرم آباد ۳.۵۷
سلام وحید  دوباره خرم آباد زدن ساعت ۳:۵۷
خرم آباد بازم صدای انفجار اومد ساعت 3:56
انفجار مجدد خرم آباد خیلی شدید بود
تهران صدای انفجار سمت آزادی الان
وحید جان 3.48صدای شدید خرم آباد دو مرتبه به فاصله 10دقیقه کل ساختمون لرزید
لرستان. الشتر(سلسله)
صدا و لرزش شدید اومد نمیدونم اونا زدن یا ما موشک شلیک کردیم
3.50
دوباره 3.56 همون لرزش و صدا..
لرستان الشتر وحشتناک دارن میزنن
خرم اباد
سلام وحید جان ساعت حوالی 3:55 از بر‌وجرد موشک زدن صداش خیلی بلند بود
آپدیت: منابع حکومتی
فرماندار پاکدشت: صدای دقایقی پیش در شهرستان پاکدشت به علت فعالیت سامانۀ پدافند هوایی بوده است.
روابط‌عمومی سپاه سیدالشهدا(ع) دربارۀ صداهای شنیده شده در پاکدشت: این صداها صرفاً ناشی از عملکرد پدافند هوایی بوده و هیچ اتفاق یا اصابتی رخ نداده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77136" target="_blank">📅 03:31 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
