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
<img src="https://cdn4.telesco.pe/file/q9EIGojXLT9w_yuw8Z0tEd2Be5zZ-5HPVIRK3qw0QwN5E-3Gc2k_9SjktQQQa1ZaJGoHe5iHzMeyMuv_f9IcNCLdwaiRTH-7Mnk5gpQXIjsDvw9965zEqlv_VRKUyhp_YBwP-FfeFOi6xSo-TSMSl7W0vCpFPPGHHTq4A38jwL7q7w0zEGuNvKm9uN-jlbiK3dUtYhi-u9MN82zNJZ5T3xIYp6N-goh8Rd9YgCysC8z4PkpmfCF9rnmUUP9mEx1H1JKYdmoc7ySIUKhn9Z4rG1sgPSnDXN2yNytohB7jFFNivM0NGgZIKJhhEjh58T30pT3N6UWLTSkSOxk1q0rnKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 477K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 13:49:48</div>
<hr>

<div class="tg-post" id="msg-30120">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXvtCab2ZVyz2hzkkujE7ClS98CTdotEo4kcd-59jH9WRmGIgvJczPpGZltRlnDn5ROiNxZcqYGYqWSYbRLVhoxekTiLwGPIaG1An4S3fAR7k2_Q0_F0Z2pNzmcZMQGZOS5UtV1GofDoJAlFUYIA1CxHhexFP1rDV9hSVOYtlZ9IJ3VEXjyG5ZegCCGezEyrUS-bu3ksFV0GWiu4JL7tQlztxjtcZb6NVMahO5TZEvesr_2IJoP8ncMF-hdZLL8xq9qTFDEs5EeV38OBUd16V9kNRjggLqwT8VV0LkOmRnsu9n_cGef7gKOCyZTU8wICYD4aUbG0CEz1hfNFXPMzeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها:
رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس رو گذاشته بود. تعداد فالور های اون فن پیجش هم خیلی زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/persiana_Soccer/30120" target="_blank">📅 13:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30119">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=GccpSAhP0b9KA8YkufcZ0W4RzCpiwGsZCKGb3LhWK_JeJ3odoh8OvzRNjAkTKEwht3pdknzwYGwMstVJJSd8BvdGwSj_vqpJoIl97bcbpnJ-p2vNG8Xt0US6Hrbgs2RJO9IwYOiaXegZoM7BgluH_4-u2VNonoKDu_NFThJOEEwz3WKAUVGBKNEgbwsRS1aJNGEQzk093qQEmNr71j8P09MJtsuU_ZYMcFBEjSJmaT46DfN6AaRbhlgL9aVVNKBqWVDoIODoPNWIXTXA29uS7OOZfsJ_DYg4l452jdlXKrplGcDPjCIM3PTFAOhgrKnN6TozgoENLi_h1hZ_ezsjrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=GccpSAhP0b9KA8YkufcZ0W4RzCpiwGsZCKGb3LhWK_JeJ3odoh8OvzRNjAkTKEwht3pdknzwYGwMstVJJSd8BvdGwSj_vqpJoIl97bcbpnJ-p2vNG8Xt0US6Hrbgs2RJO9IwYOiaXegZoM7BgluH_4-u2VNonoKDu_NFThJOEEwz3WKAUVGBKNEgbwsRS1aJNGEQzk093qQEmNr71j8P09MJtsuU_ZYMcFBEjSJmaT46DfN6AaRbhlgL9aVVNKBqWVDoIODoPNWIXTXA29uS7OOZfsJ_DYg4l452jdlXKrplGcDPjCIM3PTFAOhgrKnN6TozgoENLi_h1hZ_ezsjrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#تقویم
؛ 20 سال‌پیش درچنین روزی؛
ژابی آلونسو ستاره اسپانیایی لیورپول این سوپر گل فوق العاده تماشایی رو درلیگ‌برتر انگلیس به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/30119" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30118">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv4Pn1JBP_DtFOzkYICBj4miL8mLszgj0l7ZhXD_n_dknpES3B_z7PoKdUtVzLCEkvph0iexBIJwekGVMLuCTrO9BMh0CrkehsRspprEZGZlTAPytLEQpxwguVSHZJWGzeKOeiZBISBTVczoQS2epW_G_0auH1ex4dmqyUl41R3yU5E4m5xpQCWqMf0rN1dVVwil97NxMUj5JXRwpYjnElHJ2SkboWs2f-UZZuSDJ6HERsuj6HA4kOsf3fH289ZLRzZerKSbA41rdxqZPmWk-LqVsgk6hDr0i4Zmwj-91ZH9D6rIYxjG09CO_b6fltuHODqEKvhbrr4FJElpOlgzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/30118" target="_blank">📅 13:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30117">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVU6ElnhcHCwOogQWFCa-xMwUgVDmtqDoUr6_NcFDW30AJ6ToxE2C3P96vOC6kF1-KpcBqGn37b59Q_wWNZeYT9LMvu5psiZNqHBCUFFr9lJY-kTzZmpQeJ32cmm2AcbZA0lgaV7wsvmdcC1QxlJ8oFTpwoN6CF86sLX4oJkn7cSoS871dGrmhovycMr_TUyoFFfR206K2fHqmEyu0OI7oBbLYxmy689QDXvIBV7BXzWy4JXDjQ8IpTd4_KEitfNmxjfyENLRdOsEn-J5TSDnYm1qHqpOAKPGCkG3OTqqD9i6CQDvaTLfiM8GEG0FRk0LAGw7Xjgnsz_86PKacq9Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم رئال مادرید و اتلتیکو در تمام رقابت‌ها به مناسبت بازی حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/30117" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30116">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VePK8Bwk6nci8rGCuAVW8xLemTqr_Q3mg0xtM_56lm5McLV6wniBX_dy1EuJUuppfeKMqZ1-qXR2wPNY3VedOTD-T4UJKxkF5tnHFJ2rjq6uE9vgxlYegBo-Goy1d1DXnnhsNjXlEoPlhVTDN6hawCfbcT7XoXfOoqi4uag1rDLenhdex-JuCUjtfxFAlOU8zaXMcO-6kMTmuSHsgI3ufEd71hJCTT0KVew86DEtxvWRA_Z3UXDYt_yZbAdvKc2eBGEHQw0tn0W17OZMmsG4_lLNwFSnI5SIhz5-PxLYQb6WVFSTPDOatomuNGoK6Kb_2zbgCdMKjnszdFrtHLBBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عباس کهریزی وینگر20ساله آلومینیوم یکی دیگر از ستاره‌های‌جوان لیگ برتره که مدیربرنامه هاش درتلاش که در نیم فصل او رو به یکی از دو تیم استقلال یا پرسپولیس ببره. شانس سرخ‌ها برای‌جذب این‌ستاره 20 ساله کرمانشاهی در حال حاضر بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/30116" target="_blank">📅 12:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30115">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWwZCh-ORmAflKjgt8Swt_P0Np_NYYa2WP_Wm4rPA91fDMWn4UcUehJHcSpXHlNfF2NhhNqApEAcOvHIFpova9wf4rv413RQ2WA9N7Z4qVif5009rAtaTs6T_SM6RZVenwz4vr_QnUTOCgRW37fskMwjwodhjJ4rhjwEcdOLhaXCJIIb9ev1h0BpLWcKYMc3h50eCYpp969t34tM6kencDDKQ-zqQ3utctNg_HObaFLSixKWjXu0yVrgnMrmhtGUR6LDC0xeIEP876AvkWJAhpSYG1kdCdvqYB_MYOPnFtRtuMqhCEXRPdEx9-IYPjAVZi6eqBIb4xT4XGtOQ4Ew6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇿
لیست‌تیم‌ملی‌ازبکستان برای بازی دوستانه با ایران بدون حضور ستارگان استقلال و پرسپولیس! این‌مسابقه‌دوستانه روز دوم مهر ماه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/30115" target="_blank">📅 12:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30114">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/30114" target="_blank">📅 12:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30113">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCVsVrcjTpZIEgIV7Dw4SbeyeXIgynf8UFyWvcOyyD8groxXqgIpXPdwpY91Tk2LNjfhekFekbzFEeeJaO9NA4dVyK3Wh91yK1NOtsTJPQmbkj_mB3WmKbZAXu3rtgy8iM26oD3sY4VADjED2-LLTC_Ov7erbsInjcfkoRtGGNnG8tzvGZI6lPR7Z2zno-_85ctLBh9kPhX6sQjTUPmTZobIJgTyJsUGp1h7Jjfq_bn8gpgDaecEnUDx0Lumyvv9tq_DF8Zc3N-3LitatizeiHAR4Noj7SLgSpwgBQyXIwvHakXsGD8LETBMfwxPirChre_Utw8MDikdAVXih88MLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال اواسط هفته آینده بامدیریت‌تیم فجرسپاسی جلسه‌ای مهم برگزار خواهدکرد و با پرداخت 50 میلیارد تومان رضایت‌نامه یادگار رستمی وینگر 22 ساله این تیم رو خواهد گرفت و رستمی آذر به جمع آبی ها میپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/30113" target="_blank">📅 11:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30112">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmWHL6oJH7poRkYgW6SS68JCy42ru2qzJVkwkhHPJMBS4LoclSKP5LNkmZdYvA7Z9lqbOXN8cp-Tfd1zYh8pKGCAHKoXalFjOVA9P4lIBHvFwez-nYGOaiU5ePVzYlkrlWXayyLxkxGiIknG1bvyUSUBsAHck5cYi_PtM6Fg_ubzwS4OjuOw3ENnqrPq3DJGOZ9HBN2pzUngY6UWpnAfltYY198047k3vO9_S6pYs2xAVbJA_TYzc455VN0Ec7EO_O8Sb-10TCBKJ71bLc28f4ojOjy6uD8KGLKwNzV1ZKkc78oZutQUHZbbhNr9i7-RT6AulGqbtBmqJsABTjQqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز تنها در یکقدمی رسیدن به رکورد رونالدینیو درجمع‌آبی‌اناری‌ها؛ از رونالدینیو تا رافینیا؛ ۲۰ سال بعد یک برزیلی دیگر در بارسلونا می‌درخشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/30112" target="_blank">📅 11:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30111">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnMbVfUm5IaC_sb5je2UHA8VeYB-1TFVze3l0p8gzIDEs-gxlx9mHIfG0ibC1-wFiMqsIjKu75A2Mf8x85Jq2IKT9WTVkRWseSMp-p6JURc2C_sIxVpzsUkjRrlmWTVcwfT8cZgjpikJXgtT0YRIKcalzrXCnHoawobhzDR0gil41SOpW1srB_vUWwZP96w-s2N9_FJB3gWa_DMLUUNEJ-jXfomeSxEXrO3rJY7WBmRRHe-gV_38scXTRVbNg4WOKIVbqjEqVeJacpJgpdSkPMcRexBpXwDLlFMYWzfQmztrSyLzJY_I7YZKcZIRHMA_EhveAyXE-pdmi_CjitunHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌آپدیت‌شده‌سرمربیان‌لیگ؛ مجتبی حسینی اولین سرمربی جداشده درفصل جدید لیگ؛ سرمربی بعدی نساجی‌به‌احتمال‌زیاد سعید دقیقی خواهد بود. فرهاد مجیدی آفر مالک نساجی رو رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/30111" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30110">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPgBOpaxFPSDi73cfgR3PiNR962bxugv7aEGToKmJW1LtvBavFSgWGiM3BIynZuf9KcPHamPNLngdGnaq3Uh_k6sawQSzvau1PL3wSH4MiL_vsFhO24zkbC9DrsKWuz7eOpaIyLrtTAdW697UJI0nbzWdMGKpK7c9SPy1FEK-9O5tymiDxmTvNzRMd1XHGKWCnBKgwU2nWEbEQpvpcbOuOG49ITGw_oSvSaTA9mAUR9pT4f5kwIA4oB-nfhK8Q6mKMzrsH3H57iraHz1p0DfnWCZWL6Vqbopyy3kBkPsCY9EOv55LYsftnvedHBvD98EyZxKKrwbxXxdj38olsqkEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تیم منتخب هفته اول لیگ نخبگان آسیا در غیاب ایرانی‌ها با وجود درخشش ستاره‌های استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/30110" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30109">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLK5QnupFyZSNVUqLdg9sEwsHHxiS-JwqoRw0DKpV6ib6uxu52s5NwUvELnSt8_cfuvy6TDekU9vKgcavMt5ZfX-jfNdKvxv11burmROUst_4-D2AEUnm8ukaMD_DumBoAowLemDvaHSsrzS22PMZbanum9I9uWwJj_rUVhapLqsEv5AdlT_G9wGUCIzRzAJipTAAe9ickfb1xUMM7-07-QihJRqaLlxumseivKjhy9Y6kWImyHGROxju6iXJ3kh76aXKb60auuHg9itD4VotWFMmljuczE-yjcKY2gAgxNBzluKw0dD-XOiECyBV5fssx9QlOojX1AeqCl7U8Jfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
⚽️
لیگ فرانسه
⏰
شروع بازی ساعت22:15
⚽️
مارسی
⚽️
🆚
🗼
پارسن ژرمن
⚽️
💯
اولین واریز، اولین برد بزرگ
شروعی هیجان‌انگیز با
🤩
🤩
🤩
🤩
هدیه خوش‌ آمدگویی ورزشی تا سقف 250 میلیون ریال
🖥
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با روش های ارزی و دلاری
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
با هر واریزی
🤩
🤩
🤩
هدیه ورزشی شرط‌بندی میکس دریافت کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/30109" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30108">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/30108" target="_blank">📅 10:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30107">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBzFmoH6A8m2X0bljK_aK-gXLJq_ZXDydk795eU2fEIAOY6eqoZWjgm4Aruy6AW3MFZgPQ9CKKAIa1iFgwSb7QFkYJTDtQUgR8OFiBdKpC6xUzOBt2Hrfmf7-E3YTZiN09qYN5zQtsS9xAMRqdJdbDDFx6O_R-b1VPWKOm104gy8d8ZH2uy5YF2yYfOh_qi7r7RgnYNPzmrBg7Tp8dsbvY_0SsfKAeXWi8ODN1KftBYtDMg6H3LbWMiCsujrBgGocCkhnlFUiiSrJX5wyCVYgyAJngWXUnd1Vbrk4WPilUFnW61TG7v-oidYlu3tBFmX1NvAeytPwtc_AltTUZPEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شرکت EA پیش‌بینی جدید خود را برای جام جهانی منتشر کرده و بر این باوره که اسپانیا جام را به خانه میبرد‌. این شرکتم تاکنون دقت 100% داشته‌. ببینیم کدومشون درست درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/30107" target="_blank">📅 10:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30106">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi-nzu3wbW9O5ndF1v7hr-ziYRmcrY1-sqELVXW5q47lo5ZkYNOlLF7tMi7i54z-jawpDIqod3s4Sh1RVvRf-gxpQGGu4YcRPApBEiif_Klw7yw3EZD0CTrrAGW3zj4EawprlYaKV8gVZxjaLuHig9rgkI7lN0smEaDoi3Z2-JqRGA5SUD6jQMXbLG08YAeKrvYMPD3mtew-erkgnLQW-7Lh9O_oImlr7RWDNzC-ridTNMoat96-Ty2u4D78yxr3I0ffv-cQCOZJPQRc16qumfk44Dtd4hAB3ycWmiBIoRgxyr_3yXMx8KMwhyQFMlOt_vUCPUJiY9m8SofJON1e8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت فولبک‌راست‌بارساکه‌دیروز به لوانته گل زد شروعی خیره کننده در این فصل را ثبت کرده. هزینه صفر و خودکفایی از سوی لاماسیا عاملی‌ست که شرایط اقتصادی بارسا را در سه سال اخیر بهبود داده است.  قرارداد بازیکن تا ۲۰۲۸؛ دستمزد بازیکن، هفتگی ۶ هزار یورو؛…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/30106" target="_blank">📅 10:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30105">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9e6-1VPGoGPUe4tH0VheyQ743sleEjqYcAKvOXVlGlO1k747WwlaXta9HzM4KlkrzclD5h7Oez6IyY0Ca9n_kMRflg6UXDwxpMy1J9rAuEgdOQFgXxAzXiJCYWZ1hrVkoCXv2kCFUukYn76NTisuCfswltdTFKqn2nWK69GpEuj-vLdQpNtknbAqkI0USWwIx3EXl9ljBhja2dimf38xL-TxKLntl-w0vk9RW6LgbZUWMTMTmmbOGBRbFe-ei63OpYeclU20Kz5AvldC48m0E7AgzYAZv-dwpjEIGiCGjbVDw2P84y89nEl00kR4DqTMkUnx_lbZoCUpzo5LQipgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد مهدی زارع مدافع میانی تیم پرسپولیس که‌هشت روزپیش پاش هشت بخیه خورد از اواخرهفته‌آینده به تمرینات سرخپوشان باز خواهد گشت و مشکلی برای همراهی تیم تارتار در بازی روز جمعه 17 مهر ماه با صنعت نفت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/30105" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30104">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTOGziEmvSlLH8xZqQMZMPYayq7C4rBbZz9oYIzhlhiQ6RlsyXp-NwZnrsmY-R-S7TVktnqZCucY0vQMMpUQyLI-ck6vITq1xofvoNSz1P9zmMZFOU0_z2toqb44SH5KUsF1l7acovB9R9KmyI-YUW_eDorHNnArf-tpD9HlvvlTeZ3oy8W4JmxbvG6PXB19ajdSZjcrKn8oEwxz_VFLOMGJFjExhOCT8d_5jzTzkYJDtBJqOJFJAwB9HnjCUIqpgUH_uSf-cQucnBFLDIq4zRbO7ShGj2pYdqIIdX9_HwoHV190pr3M4kY1cUBZGGqjjAFjP7SteKwCYb8L5uWL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30104" target="_blank">📅 01:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30102">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3cOl_PxZpvQqewNuue5PEE5E4uASzpR_0h2hWoJzZDlGnjAmijxO72kKmaDWptdLxb2fvwXEYnSpjHe7Ig9SYfksfcsxFcp60B6pzg6ZswmO8b--sRehg5Maae-H_qNy6PI4zkC1wtyUT6I-7l9Z0T6L4T8gZKg0AfQ07cKTQyy9dhIzvR7qML4rEr2iJRRv3fDi4UwDb0qWl29-gb2QGhg8ilxf3_Fj8FJheGsSOHg126epCrtcabK2JJGJOJYxDEi6pBf2PqF4IG4Vp90DiMFlr-835dWl00a8Owp6cXu98xofFHpvphT3TjMNCHu7eywZV29PrZWeI8SnXSBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30102" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30101">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBgEpdJM7bSNreHJCFphhtRuqZr_0ZhLsfRtdiz15L9De2ukIrlI_MRjXtWCRFKY7oCq3NWT7EU-A3Ece7XkE0V_y_FoyqCy1nWh6T0II1uaBWif1t32lrr4IQk2OdvpD91cn85NQtSHhZXxw7DWGWPvczRB1exEy5H_BSevQmkMkpBAJKNx8c47lQI1Hp4G-lJyi9OrJuVrk7ccuCLVNBhSK-HJ0o0IUsMJI3vrFEkzAiAP3ejcpDNW_UWrx13pPMrlWfTTRX1xOKoJHrUT6qjr8luIRblebTE6Bo_MfwnG5jwzlkUh-YbIivA1BE-fzHkSTK8TKLH8s8AkwFxpJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد بارسایی‌ها با هتریک رافینیا تا تساوی در دوئل آماده‌ترین تیم‌های سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30101" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HksGXoT52PhqkZ1k-W-BD2SlFrn_dRlVYoGgNGqsz_rUemD8s7LJm23YvdfhGUIU9tsGHA9Sb5NoQ4yOhXi8flcDVftscqgTXmlvqrySkL9SGtq5O8bqnQtrBN9lc7F2XDixh5CM1LliTFeMmh_QbAZkhYpsQZkcPVJn3anSlPBkXgAY9rEliY0XzAu-yQLfEh3fzq1yp9APW55UcnxlLssts6u9satx0K7MKUa-5oic3ox0q3ytM66vv-8ehyPQJPmsznotvxiATVGcW5AD3K80VhicPhCYAZ60ddMQXI6Hw3oBMwif-8y4GKthMXUZ0sVwyGWpjPlXQ4YM6FS0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/au7Bq1uNATrlVXA-2ga1gTA0rY6hxaTTdWlJvtFtmhAQZhXV_kOMH--zZEh0iVxzhQ_KZUNoheXY61aXWW-GSf0bde284Q4g9T-NNRchx3p2PsH0HS6hpLjxTZhCoZOyp3Rmzloa3Ys-8TcwyT_O7q4ZaWmXfAK1-Lyn0vw8y3uTRQtteC3O6akiHdKrUWUlL3kxokQvGAteqfdbmLgOS2dsA7K5H1WM6SVOXqKuBOA6WDTqVtlfU-meGJophZvBuJv1sdNkGHGvh_pUVrJOmaeX0XLYDmGhuWfd49DIdPyHMRh4UMFY1sy04Hly35n8KQWBUg22BtvNGOnx5sDSxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30099" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRkSx1CVLmXw70ZlpuKzmNe5WG0XnrPIhi-lEJ27PUIDE2UF7wo4WB6NKzRiYSxroY92zGLuFM7D5fDH1kTO0Z6TyKDuV6xEmLdmmEVjxRhSrFByNU9R5UVh5gmn8jOpGalBB2LYzN7Sal4ig4FHXG841ljeORI-WyCpLIFK8S_aN0XXHq1UBd7baGUw4hgRf1Uo1Y-OzVlRaZfiV1utrB2tqu7xaJ1WlN08q86NAfPHdI_9b_u7aYO_Ke9J_ezY-kr0pdUvOf1W3idPE-GIau-diSZAy92GG3iGQ2aU5-jNow3MEHsj7fQkVqIO7XhQahIEzHQ6-O96yGFqXQHdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30098" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30096">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfi3LKkchfvraePiRhYKjfbdGExPU2VBSNg5pa7TgIIoZZb5alLDK3vIuqJEaYtJ6_N1-ibuRqBDceVH62vV-IMNfiVLKN_bFJV1AQkJR5k1GMFc4cQD6nv6udVBBI0T4Ytfh-yFImqbizr5RFNHmUHh3TDVnC6zEFupkHi7Tk_Z7W2OLcjEQ7dF2dq4uqGKFOQucH4WfLcOwo3rtCvSAvdcBrpPjmEWtXNNnXXvD6U0yo6L9M-aRglg-dDD0I0A2uAQcxpkVl5Qv3x65LiVBdCeUIYMp4pkD8nf-yjpTuzceETZXkMXQYdntPTGdaIvnRaleLvmrYY8saD8I8mopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/30096" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O25t1wiznl-5R7CW-u9C9dnoHit-Zx0hP8MJRyG8E3-GVy2Xdr1Y3aVociS7bAdSHbWFuJ3eCbH1QX2D9Mv4HaU8kRGBwNZ2yZHoYtz2QoQtXjEAKxdqkJoAgpUc4-SM9Aeo7opZPwyn5039yOfkC0Yq0BAqJ6M3sow4LAPV76vcm4M3dClVK8D8Rz7ceKwqhgc5E2oJnlOrQJf8cH2uT4-BJ5xM31QIKp89cgbvC5uDq_LJUxudQ36E3aO7aYZTf4xLYCRCGHFaVPEAMBDDeSIiKyUB0HMdFCW7Ml6dfVWoVaq8Q_uAdrapav0giaojDewRXeWyiJyHCFZXRpLLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده خدایی تو سایت پلی مارکت ۶۴ هزار دلار بی زبون روی پیروزنشدن بارسلونا مقابل سویا شرط بسته. اگه‌این‌اتفاق بیوفته ۳۰۲ هزار دلار برنده میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30095" target="_blank">📅 00:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30093">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg9NeU_g6wgAeXEqczzrEb4h3wziwqyrbAgB3KjPmatvMjnsH3LbHRR9q_lLX-UEANjj5FHdQoCzCCMB--paGMFr8p9fiF6APCIPNyrzdWtLNORqlnS5Ts7FmVCw7rp5ir4-XZMtxEla8uSE98KcKiwtB_Z8ktGfTriQISXMi8y0ql6y3H01xNbv8IXHnH_I7TreEruAITpbQh6kkSAM3lAscVypExYkoaxryqwQNzOtmjNHbgR2hTQSmzPZM8_l7LrEFEzFJuT5CYCrKz3wQbyrSmO9CbHDgwndFyRUOKXxCd0hg9tXly667fuZjZWEHWqbmZB5zKj6fcJQWbJ1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30093" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30092">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIGbvZgNUlpYWbaDoBMh-o6-nOvcvLT71H-SowmskkjBAfHY6Bg1Hefok8WCxWhKpXlqD10V-qVOqkv-y2uLZhwlHEZoIIh_CWdV9T0vpqBoNyuN4So7XqSZzbEp-hWjsgpDqKc0734O3nr97t1a67toExoPkeefi2DvpU78TLd4zj6m3bAOY-JpUABmSScRFnJUbGFlwVBTeN0clUiiXrkO4-BfK2gLsQ95REtLD1qP4CnOtgU4TX3bGPtfcEwHiw9E2ly99cQHgsY7kw2BcBhhAbUrhys8XO8E79jEYdsS15w7nEMr9GDcCAeW3mdhQJPTqN17KDIBYfPRe7bAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یگانه اکبری و آیتک سلامت دو خرید جدید باشگاه استقلال برای تیم والیبال آبی‌ها هستند.  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30092" target="_blank">📅 23:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30091">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onylzP1WjChArR373TBFiqEYy6hspV04RiNes6oZ6nxCKn_xP-HSeNoNNcebYO0RfeREfNzh0ua5PyeznfD6IrzvRnHG1hhIgg_mds-20_TutUVPJTAzxj0R-KP5G2ESU1h-26mnAWKhSFQVvRl1pMUIUfckkFhYrkMK27EVzYxI6P_xNo-kpBEKEwQ2tcLV6F4Vcr0en6efNuDjv_QrWbxbv7P_fQK_Ry5qFwoKJRK6kNvJYFrzRRsVlMnz_nHF3-fcvEdYP9xVJqA8B5Rsg4u_Us1mCIrfMMIdK-3Vs54C4YWF14RON0VaP_c9GKV7oOkGQVftbF0PYuaky3mc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه مسابقه فوق العاده حساس در انتظار فوتبال دوستان همراه بامراسم داغ و جذاب فرانس فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30091" target="_blank">📅 23:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30090">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇹🇷
🇪🇬
درشب پیروزی پر گل تیم تزابزون اسپور در سوپرلیگ‌ترکیه؛ محمد صلاح ستاره 34 ساله مصری این باشگاه باثبت یک‌گل و یک پاس گل و نمره فوق العاده 8.7 ازسایت فوتموب‌بهترین‌بازیکن‌زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30090" target="_blank">📅 23:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30089">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5sD5U3htL94PyfLpPLHIIohvih1yzawmlJNq80nlvV9huSE-n5i07FivoRhe-dTAKp8wVi9HqPYKyb4z9FH8NKYTIRmKamS-K769tpJsbeLrmLMnA9Tb6_EnMJvNwBzKeKtUTV1SdKYmHdxvj1DvdI9YyhsChFMooA3sJAHUMmacMSdSE03QC4emoKXMrPvxp191oVedfdQXY9PyrSSQ7eASECOD5wgF-YisGCm-MoaoATzOmPX79GSHD18XMpkwqTsN80badAARLbdl3bHM6P1P7FyHCOYZsLPEETKS638y4rBtrOVaGa2ITh3UEKN0Is2UX-aKrFmGiIHbi_GOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مجتبی حسینی باعملکرد دوبرد، دو مساوی و سه‌باخت‌از هدایت تیم نساجی استعفا داد و بین محمد ربیعی و سعید دقیقی یکی‌بعنوان سرمربی جدید این باشگاه قائمشهری انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30089" target="_blank">📅 23:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30088">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSAoxkyu1wn4NuJxuxb4R7LsUlwu2CYkUe9NByVFwM8Lmsar4uiHC7NSwTlbyL5demtBEmS3A22xryvjPDjTIoaYUbgYvtWcX6GgK94Y-psvaJcLsAYlo_wvY9LM8YnpTcelUQcAPQqynRKQ551_WB8dmJTE4Fp5R9oF828L5Xrv546qo_SfYpirwad_sSUPkUYa6EJ9NIA_ajdpJUN8WUPAYysbIZAnRt5nvyURpW2R4bF3M_1v8qs3voVsMUk2mlwvj290723yR8BkPhPD1NhgkdF2pOVkhCWIgegrqVG-6is7x3-nEWthu4NQVa_h3FXj6TjZM2D-KzGlwUsJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم‌بوندسلیگا؛بایرن‌مونیخ‌با درخشش اولیسه آتش‌بازی به راه‌انداخت و با هفت گل یونیون برلین درهم‌کوبید. هری‌کین‌به رکوردتاریخی 100 گل زده تنها در 98 مسابقه با پیراهن این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30088" target="_blank">📅 22:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30087">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZsPzhWgw0n6PX1vt5XcxMgFP7k6CZgc0_pLn3iqlT31s9UOmTVDXDExdCqDdmTx5L-D1LdaKtOy2rY7KpmZ1V_S7_juUSMwKJ1T1K_kOhDEPY_1oS0fRuUq5Bdz7sjl47F3J6GNQ9zb90HSjQHZgXBKy_Zq39IRsuUrp6G3fQCYQybjIMg5AYzYtSJYt3PiX08ufbpqiu9p9fhrP14z12-N6aPngCCJZpushqZbF8kt5ys--VDraR6mOp9XQhGREfn8cJi8WC97g_pHHRIifriqKhWpifY5nmys7X9yrU0mNgTCrGsT7tq1Jk5EFY765o-BSbSRGI_wtwRju9qbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30087" target="_blank">📅 22:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30086">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf-DgOHpgXDHJNM8L0qjggzR9ELOsER1IVBQsCl7_t5yNDaBynl05sznj5ZlV_k4NUCeljPELcmFrHYR77E4UWdCESeRfhAMWLAf7UllWrC90_jv5My_9t6hp9-jg71HbVMtn936nFljdKxIgZr7W0xcjt_ua4TRd0WNbbLkEg4LKlTeXwdggmHWDMW3ethq7BBHa0XllbweugjqYA3Hj7vkEWDpDx2R0JnAoa44YOQvENcgS9ipJQK-NZXBbg7eCKxgipCYTbF6esrqOH6IN0LEs-5kLNrR8f4wVxCE9T1aN4zc7iyUNROEiXlNSsjDHOxWaNzpnEjYyGj7vXsydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30086" target="_blank">📅 22:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mthtyuuvogo9OwwN2JuT7Qtd_6IT5hNd23xtRaOSWIlZsEvFiboZc5861soGyV2X64_a3Y6eUaYLM8df9ysysao1TAsCbi_Cx9DsmbNziGVPfVYnde64YslTJ6iOSGFF__0piArA2Rsc1pmsMps05ABI0zHK51HdG3R1dRJE02U-4935KdmpxSQ38tF5tkffsMCHCUCsOg0-kDrcmVRWRW_1mMbTjZ_98sjWBTDFbSIAoP8QIRMbPvMBInbrGbMUKo6ISuOkAJyGXeUpwxvhR-rlIuqkT9RG65C9yHdZcJC6YqZUyIcld6VxFQm7IhAZLnji2JbSpL9f1MuRt53KSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
دومین گل مهدی طارمی با پیراهن الوصل؛ درحالی الوصل امشب دردیداری خانگی دو بر صفر از العین پر قدرت عقب بود مهدی طارمی به این شکل از روی نقطه پنالتی گل اول تیمش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30085" target="_blank">📅 21:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30084">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYXxwO-wa0k846V53zN4mHs5zFO0vZwnuWmxcvdMBgldEwJERcjhhqynKBW2J0IxI_BIKgdqaTQFbbhpvRLn5-YWtMtd9MnnQMVj03qtcW3o1MOqw_T_LP6IU5lh0gwbEoEAQwY9VLIMtE-D4gGEAOAZUntK6t1cvpLEovkmQO7L29GvAxu29viKa2h0sEpeV43rv7ts-APeKbFwcSubUxrFMO5q553vz-x0J9CEIbbrKM9lgqEjJ2qz-ByKE9_tDQcid-LhNYCOpVfXMdj_Smh671FlrjKbJMlh2P2CkrEo0-Qew3vZfFMQjzBmTm_ogLQqHao0ag5ObEDtHd5nCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30084" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30083">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvGY0yuOgZ0rQKNiMk5a4eiamxIuMdePRqUBnS3YQHjoGF6t4vo_iYdLvKgPEcRKEDVFPikme7sP8fLYfZdSlJ1GWWwuUJWc4O15hkqax8pyZJJ_yFPyiip85ptKNdWOkXr_f6axFcFTtpOlHn4cX8Q_aHrIwPrunQ0O8BU1qoXTqNdfUvkz67mVp6p_avto7KsEcPB89D6iWj4p1vOjv17VzVIoXPfVdHSzEOc5K1gbgO-SRsLYCJr0vshnCGOOiMxNNo_GJuS-_iSMKo6oBKzi0HFU6X2SysONogQ02qplCWZNZDI6jacQONZwAnp4NvVmBwVTra7T6BM56cK2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا
|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30083" target="_blank">📅 21:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcEBTt9yp_92dgrFqtUTCcBCf-F_oDVN1MHySPiBfSQTHwYkFKn9lKiscOhtXKKKaxrEKRb4UENM_nhzfL1ZskZq1bmdUzvuVdVjZ5uvJsiBivHWQzy_oTqVA5Gq0nIWtDLgCLj5mJ3oIYnkJjcxHo297s8bAYT8OVmyJ1ej7oemIFnPA6FlB_e4EsS9TL9vM9hhxVEMFpX3yBnQ-avnZ_Cvxw0E1clQEh1Z26YkkJcivgCWFJa1t-a8xs81B-F4XeIRw2Q5rPssOmUc-Z3YKKRcnl_lkwYHKKEUMVXCJFPJfJZy7IlcNHDdMjsdJWxh1Bwrm1lCD15BJ51sySIEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30082" target="_blank">📅 21:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30081">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZmNg83CmHb3Ky4cbasjRik0_cOSK7UPloLP7OQ68JGLSAycmYwI8T5_l72AQzXV-qrkgrp05gs8P3Ie4UP4dzZS0m9Wrl6gr2QSApMQtGq2nPurFPY3CVZ0swzaJys0LtfXlv7H-JTC9SCbfEiYv6cLlXNXnMczK3XKc-Nc8pPUggVI-GZHM5xctV8dGzb3ecdtuUFs7oto2GJRhgfWiXkORVvRbgt0KkeQZ6AHYvKEwJ12QU0Mh8CEIWD3lFk-fRp0OvLpZKC3E0hYbbJQajeO-e9GbzDV53EfgWyt_amBBHXPOTgihhBZ-gGFRiuv-lJuzemgObUATnheigC7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30081" target="_blank">📅 20:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=ONB_fjvLrDcWVsy6_2-10AvqwBt4PYyvdy7HQdlyWIureF4LXWdz8plhK1lUnqod-n8B-pXVNYjvCgRgh7qtOGR__ta4dx-Qi2wWCLLMcxKWDgUkbs9hrCrmULd7oSA3dbEXSKHkM0qyocNWrKO0Xga4GfU0AeV2LcajPUi6w56iuZ_AqDw9t8sUzWvTTAxFQ7-APtHDEqcr2hyLqY0slQufFIMYckJNe0_Soe5Lbb_25tRLREtIseHbv7zumcAILrGImTOTFzlA4-ucoksqomvLA8Sq5EQU7yjflS2vXYPOcGS9ADbeMwQeHOyQTAi5pAk6XB__Z09FGuHCG6FSMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=ONB_fjvLrDcWVsy6_2-10AvqwBt4PYyvdy7HQdlyWIureF4LXWdz8plhK1lUnqod-n8B-pXVNYjvCgRgh7qtOGR__ta4dx-Qi2wWCLLMcxKWDgUkbs9hrCrmULd7oSA3dbEXSKHkM0qyocNWrKO0Xga4GfU0AeV2LcajPUi6w56iuZ_AqDw9t8sUzWvTTAxFQ7-APtHDEqcr2hyLqY0slQufFIMYckJNe0_Soe5Lbb_25tRLREtIseHbv7zumcAILrGImTOTFzlA4-ucoksqomvLA8Sq5EQU7yjflS2vXYPOcGS9ADbeMwQeHOyQTAi5pAk6XB__Z09FGuHCG6FSMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
اولین‌گل مهدی طارمی با پیراهن الوصل با یک ضربه سر دیدنی؛ گلزنی ستاره ایرانی الوصل در بازی امشب این تیم مقابل العین در لیگ برتر امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30080" target="_blank">📅 20:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqIaEgYmglcYwyHzt4M56AYTdwlihUGnZeoP4i2kAVe6PCZZnwpc3uUL2DLTIxclckZ1KYdlF1ETa-PPf0hmlRpN7swaaA35iC_yNR5ZMZxYAkMwbA7mHqk56dnaxDagTjIN5tMbqWZM65crB5DYkc1bEsrleXMiZu79BjypFl3mlgzOqHB_t9Ysd4M6iHGzd0mlncMxTrzb6LuZg-CuYzJQ8TBmBHSPP0bw2lF2KvH9e4SpAIS7cqGKTXM1qrleICyggDWvxQlEWf6gOwPXiFvde4eCyUFGR9ferylkRptnDQKKWRm0LVMusYW4N_dYVrRvR91luJhYiiWGwX0ymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شنیده‌میشود میلاد محمدی از وضعیت خود در لیگ بلاروس‌ راضی‌نیست و ازطریق نزدیکان خود در باشگاه پرسپولیس پالس‌های مثبتی نشون داده تا درصورت موافقت مهدی تارتار به این تیم برگردد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30079" target="_blank">📅 20:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGugPRA5IQ9Z16qzKBce9N7np_gUEH2R19KJpUnK7apmwzIX6ejTbha95oQ40ZX6j_6F1mW1hAHEAhLidZL1eAOeGC6AJbBOW8vIyLdgo0uH32GQp0ozjz001xgtgQUKxZyHHPA5vdxUkOuemgAVDywYtQ3L6bu6he4mHSTkkVifk2JJdjjJKJFNIy26vgAyD3KKUIfQJ2CUYNQ9mJWle7eY5menbLO46vW0XD9ThByeIgueqJcy0VaDhguap-c4lud_-ochTs85-inNih1z6Mh9Bo9VAB-CXzzJYIudZ6exnxB5vf8jIvrR1-wBEh-1Rwey2ql2YCTDEx0Dz52VRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
ستاره‌جوان رئالی‌هانیومده صدرنشین شد؛ چهار بازیکن‌رکورددار بیشترین‌تعداد دریبل موفق در 90 دقیقه در رقابت‌های این فصل لالیگا. نکته جالب درباره دیومانده 19 ساله اینه که مورینیو فعلا زیاد بهش بازی نمیده اما این رکورد رو ثبت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30078" target="_blank">📅 20:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKSrAjgxEc3YuDvQukqrK9MIpH3oUEFj5wPwPkJaNwz-u-LUaS4ac_F9sJGDi5yyhFpBWo_gDiD5G8OADyUHbbtUhAI8gYstp-XkJVA8uCNpRpg5TTJQnnUdqtYhJobponHesiek8CYRHVRZ1wGWNOBqWRe3B2f48n7Bmnb9m0lANYg_hrnw4FpvNh62xmAsPGMlUDPreXVrgKb0FJob1ws3dZTKKKU_sp_kpE3odbiQHeGnCs86CT4pm-_LG0MdHl5MU6ESLCkHJ4ml-B5vceFQ9X4VLRaBDwLY27VTWFtAyFzBWC2mITJk5n8dMhKkBckunMEo2xF6zyGM-n1fFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآمد لیگ‌های معتبر اروپا از فروش حق پخش تلویزیونی در فصل جدید؛ نوار سبز میزان درآمد از فروش داخلی و نوار آبی درآمد از فروش خارجی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30077" target="_blank">📅 19:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🟣
در هفته پنجم لیگ برتر؛ شاگردان ژابی الونسو در در دیداری یک‌طرفه‌متحمل‌شکست سنگین سه بر صفر مقابل برنتفورد شدند. برنتفورد برای‌اولین‌بار بعداز 88 سال، تونست توی زمین‌خودش چلسی روشکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30076" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5BSgqvybJGjsAQuXUIORRAgv3TVFUd8tAlQBbMM-mjR1QWRzvD3yW5cSEvVKo72JsS0K8Nk2T-L6ozc5v_ttIhfrhfAe-y7xuwvv8m-zAma7GEOUH4BybuZ8Ybf1KrIBy-pc_OhsjUAxWbAOMPvRX5UOvmTXAYKxoDRxW-JWr_uy_80naf-taBfpcflKYgZAr1dVU_wxgoOu7enT_uOaenllq_17jtl3f61iyE18BhnnO_T74EJB8PBlHczVQ_Hnwyf0_RrvmzUwek_CoEysdLbM2mdH86K3xUK7RbeldaYKOl2h1UvtcqeK-cbOzzBzqfGT79iS0mBLbnp17u0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام دیوید اورنشتاین و رومانو؛ بعد از منتفی شدن حضور ژاکا در چلسی حالا این باشگاه به درخواست ژابی آلونسو درپی جذب جردن هندرسون کاپیتان 36 ساله سابق تیم ملی انگلیس است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30075" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=UYRZcn_6-BbIr6c7KQkLWYYVK6PwiSc43MZAsaRqGAIZNk-yyoSMK2TECdIBu9qgjQJss_-cmQ3Cv7U1inrSIuRVAempI3fwRObljKFFlBS0d0fXjKnT5rDg-ieKoqSXRT8VaKtXzGkwz3UIk92aX_tV0p7VAPDdoUtkZthnLYFoyk1bxiAwYjiEmYe8T3ghsPry57JFItgNfMWOTGFgB6Opz3ZHU0ZOQRmDoxxWg14uK0LLr5lBJZGlC6YiPXmVUU2VAro0qaHXTHnBbtR_Wjah6FU0fu7eZp-VszGo7nSgOz6vA7PauggW88_VTrFgNoSmtjpqTbCVrM0E_nluOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=UYRZcn_6-BbIr6c7KQkLWYYVK6PwiSc43MZAsaRqGAIZNk-yyoSMK2TECdIBu9qgjQJss_-cmQ3Cv7U1inrSIuRVAempI3fwRObljKFFlBS0d0fXjKnT5rDg-ieKoqSXRT8VaKtXzGkwz3UIk92aX_tV0p7VAPDdoUtkZthnLYFoyk1bxiAwYjiEmYe8T3ghsPry57JFItgNfMWOTGFgB6Opz3ZHU0ZOQRmDoxxWg14uK0LLr5lBJZGlC6YiPXmVUU2VAro0qaHXTHnBbtR_Wjah6FU0fu7eZp-VszGo7nSgOz6vA7PauggW88_VTrFgNoSmtjpqTbCVrM0E_nluOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30074" target="_blank">📅 18:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30073">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJzsZhslMx0ZmWVNOwfyodbUiEezhohBed_XH5FTtvp9GbXapV9hAW7g660i5ZsEvnigJ7uOk8hyt3k5nfbzXu4u7hEUTjepVdmQNwPrhTOXlesq1H5aHTx2op0KgAYjZeQHpeo2MyHaB6bfoFnMi47ap7ndbI2833DdsTE8qoF6h1B_z0CwKR3m5-MvywtYZDStF3JJ2lqzBShtyI717wAac1fOPCx2zTmwoKkt0ghY2MkYRNb7ZbQ_nZUuAE1atG3xVtC2RucQrhKhhMWi9xXvax6N3oFwFUnHun9OnXvEIcqhDIDxGd_6Fn2dS2nInMIadozRPdMZpikt9bY5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ دستمزد بشار رسن در پاختاکور سالانه 600 هزاردلار بود. این‌بازیکن در نیم فصل قراردادش به‌پایان‌میرسه و علی‌رغم اینکه پاختاکور دنبال تمدید قراردادشه اما گفته علاقمندم که به تیم پرسپولیس برگردم و اگه باشگاه بخواهد حاضرم مذاکره کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30073" target="_blank">📅 18:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=WSpzLq0yQH6K570TqGcHmVr6zCJW1HbgkFjVh3yyxWfhYAdUwopSHjIvBP5U6BeVutCiy7dFtJF8lNkBt5-gyby9UUPKvEyZpAT4jJm-WWRbNg5Zr67wh0yPBp3MIJTq-puTN5gUWENUAJncZTAKlr-14SxlriZ6swaUPfDHpMCMMg_bKYq8pRiiZF3xujTWepp2KjX-GDtOT3SY1pZzOs5PxDScFKSD1ucXhNPlEOOq3Is1LDmjXN6Nda9McXHK_MkpLIUPwoFHB5rfAEKgNa1ujf1u-SGoLm91IqBeL_9dZqEnEx9skvMHGDRZ7z_ilFmjXe2L0u49hiXT4fOhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=WSpzLq0yQH6K570TqGcHmVr6zCJW1HbgkFjVh3yyxWfhYAdUwopSHjIvBP5U6BeVutCiy7dFtJF8lNkBt5-gyby9UUPKvEyZpAT4jJm-WWRbNg5Zr67wh0yPBp3MIJTq-puTN5gUWENUAJncZTAKlr-14SxlriZ6swaUPfDHpMCMMg_bKYq8pRiiZF3xujTWepp2KjX-GDtOT3SY1pZzOs5PxDScFKSD1ucXhNPlEOOq3Is1LDmjXN6Nda9McXHK_MkpLIUPwoFHB5rfAEKgNa1ujf1u-SGoLm91IqBeL_9dZqEnEx9skvMHGDRZ7z_ilFmjXe2L0u49hiXT4fOhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج الطلبه و دهوک که تحت هدایت علی رضا منصوریان و گلمحمدی اند در فصل جدید لیگ عراق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30072" target="_blank">📅 18:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30071">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDJWK9emWXq66yAxjVv2c2GevtCBvRn-X4jHo0fFXVAAVMlt8A9Rl9PW6GSawH2ICy2fSbClYk5xZSpdVDM9Nr5-mwP9vuJaUe6soc1UocZzBmjZL1t3h7FtUzPkU69lI2ujDM3P9wgKU9VvltsGOXr4TMG-LhWm5TB7kB5VNrT_Aufhmg-fMbKiKzOFXcqJrl86LB3K4lg2OokZAstXe45Zf2N8VmzODTUrcdsczuzXe5a1g9f8AOqHSORvzViYC4F1685Gt_DxQ45jWLDmx7z9ii40UyVzzkTYmuzjrZnv6yw3wBxcyJSH0YAn88l4lAfsEPunZvAEFnkhMwCYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30071" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30070">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUJKf5DItL38qdgIBMc5doNb-DyZdKUIHfqQ35BZ5IompZOuzYV7D9ECA17A1Xocc0_nDujmqrIpDZ2ApKTpghQVVqgzCa1bEbCi9IG258uW4omaeEJI4P46bEhfZrHeoSFhNio6LBU-2KlZozB8lqbU_OaodyJ9iBcB8mSedCNTHDZiEGDdXkgIDQukO6Tue1pi7ESbneki2NaG49swvN2qPKZSEVpAxXj4SkJ06d6-3alY7jZAQzAm0JHa9Lq1uOaV8oLoFmyb4AZwyKqg9hS_sIJKo4LCZ4vb8IU9CbE1ivDWV2yX3PR-5t9K2S6z1aAf6xcfNfme08CPeZC0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30070" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30069">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnUlpJ0VUAls4vOa4Mzb8fMve2hI6Jd4M96IcmyyH4tGTq0avJW5XLg7FUhRYyYDB25ztN6EfGRNdHEsBIAJd7yeCrPAYiLRAvLqGMBBqUZPB8DX7BLKL5AvB7mJwBxRvF7JECgXeSP_ADXYPYwwwSP-brOVvY4xZQBELwV_TisDRoFVyFgLHnY3UpMOhFH0vHSsuLVwE8Xe1TsHzumo2gPUydtKjgDy2Od7LMtCSaamHsK_nQHinulenLsqRzaJbUE2vNCkXTGZXhpT01pB-z5AbckIqZhlN8sLiESnHzdPUsbTMqgOp2yL-S7p2S5wdFRjw8PUwRy5Dvt7SU6fMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g28
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30069" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30068">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=lEgOV0KeUh1hY9-b5u7GrU50dpQGjcTD6XPJo1KhNhXfcQds8aGreJB_stHe0x1CuJrQTy2xp7h7maWGhA3azh-FgnyapXIMx5mX7spgrt5g_fu7BvrAINwj-v28R2C3ynwaj81foWJd8Ssvrf7uY-c7VHHSrqcR-eQWry4tSplFdVElA_sH1EeCrhK5vwD9fQdvGBMRwd88sl1mSqxtKZuEq_XMiICay8rIsrvAS51q4CM11QPEWjerBK5oFnhgexnDAlS31M8tShHkRCXkn-TMrKW6S3a4aZFAKvfaHQ8GoSydXMS6zUwMKa8Q88VYvnoDjIpfO_qgKZR53IALvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=lEgOV0KeUh1hY9-b5u7GrU50dpQGjcTD6XPJo1KhNhXfcQds8aGreJB_stHe0x1CuJrQTy2xp7h7maWGhA3azh-FgnyapXIMx5mX7spgrt5g_fu7BvrAINwj-v28R2C3ynwaj81foWJd8Ssvrf7uY-c7VHHSrqcR-eQWry4tSplFdVElA_sH1EeCrhK5vwD9fQdvGBMRwd88sl1mSqxtKZuEq_XMiICay8rIsrvAS51q4CM11QPEWjerBK5oFnhgexnDAlS31M8tShHkRCXkn-TMrKW6S3a4aZFAKvfaHQ8GoSydXMS6zUwMKa8Q88VYvnoDjIpfO_qgKZR53IALvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد لژیونرها در رقابت‌های باشگاهی امشب:
🔴
الشمال
2️⃣
-
1️⃣
السیلیه؛ پیروزی‌مهم یاران امید ابراهیمی مقابل حریف خود با گلزنی بغداد بونجاح!
🟡
اتحاد کلبا
1️⃣
-
1️⃣
العین؛توقف‌اتحاد کلبایی‌ها با وجود درخشش ستاره‌های‌ایرانی خود؛ سامان‌قدوس ستاره تیم ملی ایران زمینه‌ساز…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30068" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30067">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpRT8Dp6GEGF5RuR0wVVsbzCJ9yyK59HrgRm7RNJ5G3BhTbrpTRtXSFbI9_cAjAvkht-EPC37JfxDqjUYuLq-9DXXXgMmdTsKXc3qOX-Ps8FjlU1USEsV_8aJJAGEWhzL9uqG_jpXjfLBshlBA1HWvjPCjkDxzV0QSyDpOFsQwVNdnSPfTO3QNNTKBkjhpImvnEbcU-AwZOTOpEB-4pflp4qxQpE85P4iezLTe8H8lq90VSvSYnl0dCrKin6vPxqwgLOr1kxgfx6P7RfbUum8CwBpdSFYHskVOQ6n6Z7dCYUyDPzuNbM1Om_0A0_WeBBXABz_3ASXSABTxTQXDg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30067" target="_blank">📅 17:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30066">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVVHEhDtegn8dZT6O43Brb-oKqBBWAQYAnkOmdw_fo-nsroGN5DWChrmlx6GSkiQveEjDmBhVhyrKwRSXbBXHtF320xQEeh4GKUrmdnKBhtbubJBQuv-fCfiEjcHYcd1o5jein1eSEMSnQ4hadG44aGdLTZCFNeVOY5oHNsJlF_9ULavw3VuN29G3a8oGCiJyqz_K-VWlXTFmIQcmPFAsxUBobaQKN6Ya4BEVJzcWXtptH516a2a9Su8U2UcK2KPtQgGWlodKC5l1K6dqxoXmGKs6E-JyaiS3CscCm01Bs34ZsFCOGNnAhNmNHAEgdmzVgCGXjESUVO3mnECbBED6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
به مناسبت دعوت دوباره CR7 به پرتغال؛ نگاهی‌بیندازیم به‌عملکرد فوق العاده کریس رونالدو در تیم ملی پرتغال؛ نکته‌جالب اینه که پرتغال تموم افتخاراتش رو با حضور CR7 به دست آورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30066" target="_blank">📅 17:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30065">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMOAnUzdVduC697Pjo868Zntg0st8J1-r1_qEdPcfu_ZMeOHkIwkf-aFg0sUz_oV5s6rYmi0H_KaOCKQ1KdUZTrYw6GXEuzPjWcmvQPOva3nvZk76o_ZMG6J1GzXQTdX5-1yzX112uUSL_76ND-RUM8Lqu1RZEY22rsL_RRhc8WJ1aYXzlIT1HTcOFmwz4_XnNcKBaaEWYlBNf0E6f2DPTLAg6xQaZr-7CG1ZUOdUoPP2RSwsUfPAFDkYbjoRs2Q0d1PW3HIrM97PW4t-C9fg9Kea1d4UgBhft7NJpurbuGqImb5NMZJTkPQmuXL2a0iCSzeZtDxnM9cYL_p-i98rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکردفاجعه تاتنهام دی‌زربی در این فصل لیگ جزیره: 5 مسابقه، 3 شکست، 2 مساوی، 0 پیروزی، 8 گل خورده و تنها 2 گل زده در این فصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30065" target="_blank">📅 17:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30064">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig4DHNG-ttUbcyHrsZQ8-rTYCJ2IL7J8AS0bCOfyYeujEp6Y-sqXv2H5jmZbKdQBOUM6RAnaoGcXg9wfKiQJ4foesVOj5kx9rJjdGCBFWdEPB45v-l9H3-zHburTaIlw-Tlu6qNlFgvLJ0DHtI5SvkvoOm-7iC9B_s0CmOFV06igDPtm1ELnusQBNuITe7i84lXZfJAruL9HErskXI9dvsq576_1f9EkuP6m97r6z9XJO5njRBF9WKlpexb-fRlg6M-kYNhbQsdcZ-zepGrdnspjoarg9aMI-viAfaMHerVrMgWnF2LS-ORuQGE-90aKR0oGdQr8LhQ_1fdLLXiUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شب گذشته پرشیانا
◽️
مجتبی حسینی سرمربی آلومینیوم با عقد قرار دادی دوساله سرمربی تیم‌نساجی شد. درحالی گفته بودن بافجر امضا کرده گفتیم فقط مذاکرات مثبتی انجام شده که دیشب مالک نساجی پیشنهاد خیلی سنگینی به حسینی داد و مستقیم رفت نساجی.
⚪️
…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30064" target="_blank">📅 17:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30063">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=ejAaGcrNfgDJPFEZ7lm-1rYsDUmEax5IgUjipWTD8gLJieDrj2OPhtepFbtCmhhrK5nCZY0UtMDvcRAwO45mDE5vESnd9Xm_-8e4lgKnVHludEwrzhAdDDgriqTCW6cjLeIpZ4n2fyNBzGIExEpIbQ4qFPqo7gwU8qRw_8qSzZ7_CnVoMAx9R4Dc5sb9GYGK6tuWdZyNX0Y7n0czGZluov1Ellpcr_VFS0zeYOR6tloe1HM5c7uAQJV1jzu7EV3YV2BY-964gFvBiY_pDDQYnsnfymdMDYXQr7heEFo6alQTiJ3byGskdJc2X2mgsspXtnKExMSawoE3uetYTRYIf2aOdZ3ULaVnA4dumcfw1JNMavyL1JkiIYmSvtHslMAbzlWhOv7E4ZzclVVJRdP-k_bcTwfESml8-4QQnyTU8Z-SAvqi1xQwd4WONHsYevvvf9IkcpOuojg7NsF6Vf8Iqn21cWmEgGuQPL8JAOl0ZJxWWmIjYxzOx5hwjWdJ6ALfpSbq5A1JdXAUIN1wdrOfZvihyPbkiZuvApDXCY-ZDfhXfPFlHNVXJBXb09GDRiMGdGkBSKcw8IG0QdBHU_VaBlosSYZNl2Xxuc7JMV4DoImLpgj0YAOx6Kl0ZBbzMIRyVZ0Prv7xvz4lZkueeGCHDDh2judfEGXl5xk2LJxUtpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=ejAaGcrNfgDJPFEZ7lm-1rYsDUmEax5IgUjipWTD8gLJieDrj2OPhtepFbtCmhhrK5nCZY0UtMDvcRAwO45mDE5vESnd9Xm_-8e4lgKnVHludEwrzhAdDDgriqTCW6cjLeIpZ4n2fyNBzGIExEpIbQ4qFPqo7gwU8qRw_8qSzZ7_CnVoMAx9R4Dc5sb9GYGK6tuWdZyNX0Y7n0czGZluov1Ellpcr_VFS0zeYOR6tloe1HM5c7uAQJV1jzu7EV3YV2BY-964gFvBiY_pDDQYnsnfymdMDYXQr7heEFo6alQTiJ3byGskdJc2X2mgsspXtnKExMSawoE3uetYTRYIf2aOdZ3ULaVnA4dumcfw1JNMavyL1JkiIYmSvtHslMAbzlWhOv7E4ZzclVVJRdP-k_bcTwfESml8-4QQnyTU8Z-SAvqi1xQwd4WONHsYevvvf9IkcpOuojg7NsF6Vf8Iqn21cWmEgGuQPL8JAOl0ZJxWWmIjYxzOx5hwjWdJ6ALfpSbq5A1JdXAUIN1wdrOfZvihyPbkiZuvApDXCY-ZDfhXfPFlHNVXJBXb09GDRiMGdGkBSKcw8IG0QdBHU_VaBlosSYZNl2Xxuc7JMV4DoImLpgj0YAOx6Kl0ZBbzMIRyVZ0Prv7xvz4lZkueeGCHDDh2judfEGXl5xk2LJxUtpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال زیراین ویدیو که یکی از فن پیج هاش گذاشته گفته همین‌کلیپ‌مشخص میکنه که من در حال حاضر بهترین بازیکن جهان هستم و مستحق بردن توپ طلا فوتبال جهان در سال 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30063" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwJIgCW_1JGNvlYOU4mffP-Y1nZKVjg_4gJbA3yjV91pEMMfucIRk50pH92as5dvxXLTP5_SZG2PvEmAwv7HBK45cdbS18FQTpqbfGySPmXbB6YncbIYmYV444s5QHG4ZmS7GKw6ARvcjBEw5pA32D_8cMKOQkNBvoVvitkFr89ddWxuP2x1upl7v4kOQEDqj_CY-0LjT-DLo2N3aZ5FL0smRICVZvJbi8EW4LQuhaVHZG7P73lzRZLgRgeC0T9fFNBWs1a6RqJglDx2CYU7IJLaSqvh0SD7fCVJZxpG_ry-KB5FBFlpsGDeu-X6nnWW4qKZbscfZ10o7L5UVSdObA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه فولاد برای فروش یوسف مزرعه وینگر جوان این تیم در نقل و انتقالات نیم فصل 150 میلیارد درخواست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30061" target="_blank">📅 15:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOIfCNl9gRHm8Uog2DXJpG4olmDAjikFuVbNOEf6hpCfQPldUZkSrZQCRhD5xyK_VZ8e7KUgMHVMqUO3u8Nq-O_r4yvllCCsNstri2LPoI1DCudRbD9AFZGF32J2EPyAQWWh4lNZs60yln1vV2nGmwiX8corLUZBIgeD8ftQo_XDNlatAcgdR9iGtn1rNUF-pEDzQsyYuMbGyy-0eqZ9UwazjaP0fBjDfQDvyG-Q_JiNM6Dp2bqqr1L_M0HUNKBGT_ozu-mlTOMKqZc_NUY7gWIWK7QHPTYF2zpJA9djZrsyv0FzK7YVFg94JCa4EFSHU26SwdkehpTdhB4dZ6iSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛رقم رضایت نامه عباس کهریزی 20ساله150 میلیاردتومان تعیین شده. حال‌باشگاه پرسپولیس میخواد که با رقم 110 میلیارد رضایت‌نامه کهریزی روقبل از پایان نیم فصل بگیره. کهریزی از استقلال نیز آفر دریافت کرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30060" target="_blank">📅 15:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozA5H38JZDCp-JX7RJPDPIsvfMde-vR2DoXHAmyYDpUjB441TTVdx_ryqp3upNmDl6bxaYW45sQ2PJZRMZafXs0Soeq7BUxrl5DrYUYSpi9PAwvH0MCXk4vYyki7V-YLD98iumv6aJS_2AKXIYgFSlQUzoNAvdPXUL4tqrx-aDria1zrzy6Mu93tLEJYS9Uc_YdsO5_fp5zW-ZaVsz53ZLK84FM6MtsdB8db9EwnSOjDZGFbb-mSLwy3EjnvZKVai_eP_v1_wxJIktJFjNOEeDrilVTa8bvGGQ_LkaJhGtat4z2iS_WPVw3-va9peyNTARya-olN2vHk3EVcg0L2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
خبرنگارت: بین کریس‌رونالدو
🆚
لیونل مسی انتخاب‌توکدومه؟ مارسلو: کریس‌رونالدو تا ابد. بنظرم بهترین بازیکن تاریخ بدون تعصب کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30059" target="_blank">📅 15:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C907D7I9pc6lrtQVwRWz9fla8xVDNG99Ww9uZt4qZiJnwYJm16a3T_EmiTjXDvQVXcLmmAYYK9zYbg815j4MfB7GioRUbb9kSaCBPpaCkR4gASI0Y_wQOVyku_UdkYcR1v4P7paVITiA9RawzmM2DYQr7YK7wOPibA_7lUVKbJ8Gzhnb7AWJJ0C-ipm0TEdQjkelm7M4IXAhyjGqFdoDiaBejOmCaBqSNNhgzWU1dlHeYDOxGbZ9YKmHAE9Gk3YhAmGuq-AzBrzIO1cLUSZNbYPep2DOO91a4nx4vEZVIswszdhTmGpiIokzMTwurdPHNsZ34n8O8tJ_iQkGpLXTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30058" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30057">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb1fPky-701asYS4mk-PO3G9cQ4IquLx0EbNdMF9Hg-hpNiRetDwUQg_XSA1bPNs3ojg6NYFv8AdfxkpYZy9Nphnxsw4VFVtsvLRfQpqvPaVNiqdXAAe7bJEm0ThhkKTCRWgYB8WbTZ_TmByVnXzFwL7QGq0xRILOFku4NkaTQ0pIIhjsaQiBFiFBvA8tAU4-WFEt2hN1vgBhxVI7pX3bQFsF82FkJzarRMJsSMCEZi5fViWQop5Qknf3f3VO7RXNfIskicDnM3sVEueWF6LQ0no0tYiXNEXIU1lh2zn1c2nnyxFqdjlZy6JdTTkKRXMI-SnHE2JuIP5jyAdZGgyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیانیه‌رسمی‌کمیته‌انضباطی‌درباره شکایت باشگاه پرسپولیس از یاسر آسانی و رد شدن این شکایت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30057" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30056">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGxUWbHA-B6Id5-eN2mQYk-KmpTdYfdsj7QYosevC3redE5dPcxz8xCNcojzHAo5AwErNp7IHcFaKdP7BXxIMwhKKB2eL8cOYa3wf8rnsxYvpJko5I3MyXsL_quFWat6WyEveRYDUBMa7vxSp92wCneFdZS3WXzAAsO5pdE4NRO68ps-8awDjDYMdsyHfehUCBIstQEBlJBP75hsBJnZdJXHBp5plZtIf4IeC3DL3Iy6BG5ibyKJIQFhUgMcNXZyr0ZOqQ4tAX8q1QJ0Js_wRPs_mKeWtKxHTg3vU2yLDD6V4jgRLFol2XpgV8tIjACyg_1rod2_DYLx8BNBlBE2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی پرسپولیس در دوهفته‌اخیر بارها به مدیریت این باشگاه اعلام کرده بود بین امیر جعفری مدافع چپ گل گهر و ابوذر صفر زاده یکی رو جذب کنند که انتقال جعفری حدود 100 میلیارد تومان برای سرخ‌ها هزینه در برخواهد داشت اما انتقال صفرزاده به شکل…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30056" target="_blank">📅 14:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30055" target="_blank">📅 13:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFb4mzKqgVnfksvU-awX72RlicUkKTS_zU6upyplE-RmCFXjZwI2KkuM7rs1NJi64pEK6H3Z16ifrbRiKewXCxCCng1tLWxrL2i2VNncDZPKUQL-sPsE7aTjK1eLq49fv31JPtLpF0Aos2ZDIG-zS2KYb5nkiX9xvwoPhGPZYhxw85j_ZZmfj4nWgWVHYvkXh_SUTskP2T52E9SrO13HoTwEi6IT-UUWXMULPswasYZ4qIriJ2cE2FOz89_5z3VHLdhKhdhSBfUZsNJtbIfxRCOosY5jkSKweHXVzNc316zNoEaiGtTP4NrD6EY-I_F2SZ4incWM3BXDyCBj6uo2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇱
وسلی اسنایدر سه گنجینه گرانبها از تاریخ حضورش در تیم هلند را برای مزایده گذاشت! توپ نقره‌ای جام جهانی ۲۰۱۰؛ مدال رتبه سوم سال ۲۰۱۴؛ توپ بازی هلند-برزیل درمرحله‌یک‌چهارم نهایی ۲۰۱۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30054" target="_blank">📅 13:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhTppKPnUG2aWpZmLVtyCoCOUI8FFb3V9SEsmABOd2rnVGSoFUq0sEvMcShC57k6hyrvXX8LUZtPeuqQY1UGiSHf0ZTxS9fuUoqxg_ZL_XXQX20cgrGPgY-4lNekqcfhui2DQ7FOPoHIksCKfXhFdtvbzZhBe2mxRQWh0Vkvi6U6wYTbOuXrvi9Po0zkPD_JfOb1e10V1O_vNeK3ye_uiqKj-7ug4zQ_83Ji-XG4Q1hWakU9JDQloD3Va5Kr53fnRcBSCTy_glGG9DXnNX2m38m3hmqplY6z3jXBzrOOHiAqyd5AcXsKEJmkAc2R3XsoGRTzbPMVPlid5fxH0wRefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=TUNEZKVHy9qQ9WpkSejiwb8HSVKzHjUI1HfyJ2oA7ndLDgDb_RbiIwuH8U1enTFYBAMHblllBf8iazqk3kEP-PPD-yvW9zZUWN3XCMX2O8vaBtnY39l7atRWrCpmGS8zP6-Lk3agXzQFtlYXDluIYqaXjzv1u1_d23UC2lKQ9r5m9j3Y0dHjBf6n6RTj9HxCovogRT7z3QXlIBU8KipzUTLIqBjLIt5bYy__xuGnNd6pQ3TyRgMAlnIAw3oJgIo3zfcJ8vGbRutMwnUd7AXs4DTgjNwyQ84uN6Uwj97MwngBUWuzgjuaSldVMtd3FTCgBL19Z9KhDUYVYlqWUzP8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=TUNEZKVHy9qQ9WpkSejiwb8HSVKzHjUI1HfyJ2oA7ndLDgDb_RbiIwuH8U1enTFYBAMHblllBf8iazqk3kEP-PPD-yvW9zZUWN3XCMX2O8vaBtnY39l7atRWrCpmGS8zP6-Lk3agXzQFtlYXDluIYqaXjzv1u1_d23UC2lKQ9r5m9j3Y0dHjBf6n6RTj9HxCovogRT7z3QXlIBU8KipzUTLIqBjLIt5bYy__xuGnNd6pQ3TyRgMAlnIAw3oJgIo3zfcJ8vGbRutMwnUd7AXs4DTgjNwyQ84uN6Uwj97MwngBUWuzgjuaSldVMtd3FTCgBL19Z9KhDUYVYlqWUzP8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30052" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtaQM9AlhY5T3T0hqcGgtBYqWZB0-dXBR8Q0r-yr17YBASnCnd-zpZtkN856_-3ixnwzQ-RjpekGRo5FSM3JBiTBKXFPYkVsgqVUgqQ8tWUCuc8ae0YZcB50eIOsXjNqqgWGtXMWxXvBTP_pReRWE3p4BGl9jNGUG3X8XlDSL20tPQ2W8uCB8ZoSReB-46OrB9ICO8hSqEGa2Z0QmcaDucjreDW14rLaTDwkyYmfR8rGKF5evBYdVk6vIygEGO6pOvmGlbiHEUhHO6rpyi2sjZW08KsvnCLv_SRKQk6AjxSSECNxy7CRas422KnaZOdLa1E4MwdarKL7mk27fePAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
هایلایتی‌ازعملکرددرخشان کریم آدیمی وینگر فوق‌العاده سرعتی‌ بارسا باپیراهن این‌تیم؛ آبی‌اناری‌ها برای جذب آدیمی تنها 20 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30051" target="_blank">📅 12:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30050">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=FpfPzG_YlauKvFj8zw6W0EzpV3aaKHmLGtAaKN8Yclr4uqANj301o6MythGIs3kvLhsxqn8zpc1PJ3T3npfgA4WtxOZUhCKMJqoZZYWwSr2saIo8vitV2R6Z_ecapNynQ-PoqFYbNUW5LzMHOyxXOEKAa4qnhmc0i4JnIl3GYaY8altOdFmG3jXjprOtvdrBdLqp9gwGbua68qFfuRX7MMXtCOl8Une3DZt8_ZiBqCq9rjda8UG8QGVqX6T3EHoDvRYc_8tonVN37j0UoZPN4vN899wqAb9isgyfmSD5JzCQfOVOD-BLqkGaSXT46TLk-isSTR1beG6hpR3yOQ5NNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=FpfPzG_YlauKvFj8zw6W0EzpV3aaKHmLGtAaKN8Yclr4uqANj301o6MythGIs3kvLhsxqn8zpc1PJ3T3npfgA4WtxOZUhCKMJqoZZYWwSr2saIo8vitV2R6Z_ecapNynQ-PoqFYbNUW5LzMHOyxXOEKAa4qnhmc0i4JnIl3GYaY8altOdFmG3jXjprOtvdrBdLqp9gwGbua68qFfuRX7MMXtCOl8Une3DZt8_ZiBqCq9rjda8UG8QGVqX6T3EHoDvRYc_8tonVN37j0UoZPN4vN899wqAb9isgyfmSD5JzCQfOVOD-BLqkGaSXT46TLk-isSTR1beG6hpR3yOQ5NNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
سوپرگل‌دیدنی‌فرانسیسکو ترینکائو ستاره الاهلی بعنوان بهترین گل هفته لیگ عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30050" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30049">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSGKohOHCbzya4oWQoN-zq4fQ9_asoAkL4yFiyMFzXHuPP0LAu7KPIbNBAxkHvNR31zi9sw5r0z4EpbRhaQMZPiMsFj9PObgosqCfwopzeltgO-d2iHWFVaZ1GjJASEXLq4-sSUbeahDKXmE7r2bzXA0WtuTvtTaubQwcS0Lf8m8vuvSooMfOZrqT1qxwraAKhJA9fVlVkhxQ-jG01fKiD7Xh0-p4ujvBMiFtd-nkiex8Tddoh_Qlj1nnLHi8MMCh9B6Cn6vv_r7ChuuUpbUW7gcjvPmre5n2QygGYb7QM0fbHeHvg1twpBLysouJ7_HuMwrpxKFQK0i4x20_O7jsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آندرانیک تیموریان دستیار قلعه نویی در تیم ملی بعد از سه سال کار با او از کادرفنی تیم ملی جدا شد.
طبق شنیده‌ های پرشیانا؛ در صورت موافقت سهراب بختیاری زاده آندو به کادر استقلال اضافه میشود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30049" target="_blank">📅 11:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30048">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAltU-AAD4a2UgTIMrstErOVNz7IwTY2XUTI8FBD1cZpDVzoARlw7PCJJPioxkNZJ5F7-jekkXUnBVWCQfPly7Z0S3u6IVkiKt6qQtKGdMETaXTxOd7YjfPLCd5AbKpEnvANEX7ONRzS_fqI99pWOuhUbU07RTq4U9gW-PAynZ9LwjM_gHenCzCYm1Enznqk98fOmX9qBRwYNsYgPO_hSrSgZu900ZHcV5rhAmmLbncILRneCuyZNRAq57oHXdomY57-0rA2ykYX8xtEZVnnLUTY49TjLUNE2SFrZ_BIrfK6jcLV4jmIiBMdWp_BWIO-Yh5PHccXM3OseQ8baB6IBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جالب یونیون برلین بعدِ گل هفتم بایرن؛ کاش این پسر 19 ساله بارسلونا دهنشو ببنده! کین و اولیسه امروز واقعاً روی فرم هستن و ثابت کردن که شایستگی قرار گرفتن تو جمع مدعیان توپ طلا رو دارن. واکنش اکانت بایرن مونیخ هم ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30048" target="_blank">📅 11:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30047">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp9C2f_e0agwCYjyDADZ-I0YXIb1rD2rVzEnUt4f_7PwBFdJrU4wy0MC_Yy1TLSIlAidkJ7xu_PH1pZyk12boNp2HCduISVW1qAas6Ycy_30ATB8yC1zhVeTpg4okDjp8pxkbJF65yOJHTnWiyI69PRC1xVYdeBibBFvL8vd7UV3zhfZl3uyJ-AYxyQQ-gkgy3TV6d4y_MmAzILpxYwI6LYXci-atsaQpfDCfEqxLKNSC3pWSDqwBWW7XAaR6RsICzG5EJdr4v6M1TAiTZi9UOCJYhICz36GL8M6-WrmyhJN-YPGCX69pkHgU12Q2iY6DvwNpkCZ29k-Kzye0qysYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
یه فلش‌بک بزنیم به زمانی که ژوزه مورینیو سرمربی‌پرتغالی‌رئال‌مادرید برای اینکه خشونت بازی پپه را کم بکنه. فرستادش با تیم زنان تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30047" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30046">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4j_u5DvDzpDZhBaxHphSMaN-dOgA3cDg2cP3tAzjAOs5jxzFq38hs4tx15b03mMczzJvSzVgwi7P_HZGU3KcOexiCbKNLbBvgmfd5L2yrNlI0FBnMLDd44lJV-XFjWKfPqCcpM2Utv5_dv6e2B7DqqNwVF3_ekwqk1qZFczIX_th1x5d3DuaYAVww8kO_enf9lYKOJU66xQnw6e5JlkI3RwEgmsU779Mnlt6HxCtJ1n-a4Ztv21sBpygn91ixgNmzIoa6U8BJiyMICgp35wsI8yDpBKUSYDIXZxmWzo2fVVg9tHZkNt37xikkSxhHafOjX-ZlbpXIeoZZXlHhVyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کری سنگین مارسلو ستاره سابق رئال مادرید: خودم به تنهایی اندازه بارسلونا، چمپیونزلیگ دارم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30046" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30045">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clMmA-_G7tmtCq9fBiJOGrpVuZ2hfsK12tsz6jkMXiaifBslB48W3aiOqsL2HbCMK_A7_nE1eysmMlpaKPDGhyWlHcdliK_Kmn-SeYYTJBl3RI265aNAxYA75ALTxjMQOUJrV6IgpTFjmDLdrBAXNnzFXuop3vr6m7rPV0gH9cG2tPldGYJNc03xG2jAmmBeRJAo6g2h8jvcZ5dQXDYcBhjhSS_atpINnSrszRxFDFgI_e1v-hE5JC8ZC4r52QiInAXShqeSKMs4RHRG60g2lWqFzIHc5IrMmio18QTgCIkhfPqNOSBaUNX3oWLcHzly1F8d7-HY-Z82UUapERqBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌تعدادفصل‌های‌الکس‌فرگوسن و لئو مسی برای رسیدن به 49 جام در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30045" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30043">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=RsM73wwSF2zhyeNr8fRr6dn8iFFpTohiCUpElfGA0jL2S6Qp60EKwOjQUbUWExzUxN3q6KM_iDNYcnucTi7PgE5VF7tMA1Y72KWI8V1a4SNRxU2tEbRK1GbNIdlyfZVxb-Tdcpy9kYmamImMwi2iWrWN8vf9lkYtOOssCtaOa_82y32wutVExCNctAO3x8ZaOHMXNKj5pFqiJ0D3KfPjNRv5LDZO4aIZqzIJ_xdbNfX1kdXfkf1SZxIbkaWSyztpmmHHEPEkmskmSI9b6PR89ybrJaY18ETxVLvai2xFH8o3nmEsfCJ2RL4jPZkr2_a-PNoTgH2Jubepc5G2NDPDbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=RsM73wwSF2zhyeNr8fRr6dn8iFFpTohiCUpElfGA0jL2S6Qp60EKwOjQUbUWExzUxN3q6KM_iDNYcnucTi7PgE5VF7tMA1Y72KWI8V1a4SNRxU2tEbRK1GbNIdlyfZVxb-Tdcpy9kYmamImMwi2iWrWN8vf9lkYtOOssCtaOa_82y32wutVExCNctAO3x8ZaOHMXNKj5pFqiJ0D3KfPjNRv5LDZO4aIZqzIJ_xdbNfX1kdXfkf1SZxIbkaWSyztpmmHHEPEkmskmSI9b6PR89ybrJaY18ETxVLvai2xFH8o3nmEsfCJ2RL4jPZkr2_a-PNoTgH2Jubepc5G2NDPDbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد: وقتی گوش دادم. دچار شرم نیابتی شدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30043" target="_blank">📅 10:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30042">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBGQgylk0SNbjsb4GviP1MZSCSjdy1mB_Qy6dIc163138FZMO8PcoySzs7T-T8mXLT_LVBY0JteeTRgqQXpWP6WL0wI_eiopcW7Lb24ZtEtMxCnuAa-SGfaxQycDmT9O71hc2HHgnPg8tfs3aVdRMZdjyUsShON9pCjQkafMbIDycdFHCe7CzMpGmoJlhLxQwbYfS6Mv4TYxN2RJ2sRFChsxKTw1K1ZuAL1VAhNrTHXdPw9n7gJJabdwzzMNSBzjW2eLSXz1WatQHdniSe2k6zJlw4BXbKKWA2YTYW6Wvnhom1_uPX89Qr2WocTsmccCp1se4_kFoZhQySVnIzSh7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇪🇸
🇧🇷
ادعای نشریه NC اسپانیا:
باشگاه رئال مادرید بار دیگر مذاکرات رسمی خود را برای جذب عبدالله اوزان ستاره 17 ساله مراکشی برای رقابت با وینیسیوس جونیور ستاره کهکشانی آغاز کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30042" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30041">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4a3aRC8ULajOJT8sdq1wA-CZdlHtifhdzx6zEo0tJiuvTrQ1Kg4R-n8bIoejzarR0BSnxl6I7ASsgrnLEM4X44YDM9F4rzPR1TqpZ_yDd4rv3eJTyFXqb4Sz_hdlHRoubOVgVjGcqskk8YJ5X8PdMWDy3nYVtN5aG_YtOTMHf-4niss0MnnuZhnUTzAvgQrkOiW--LZ1W3zbfDSo7uWPY8_7T3A7cpMAmcFSN6q2BHuveEAATatvYEXXtk6WzLANsuiByGf7glmnRJEGPIwcGi9p07u3pCdqIdbnSbsDBF7oAgSYBcaFa3YePobEkzD2qDSL2wcG1yGWZlm5INwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
یکی از مدیران باشگاه استقلال: محمد خلیفه و حبیب‌ فرعباسی دو‌گلر تیم‌استقلال هستند و فعلا هیج برنامه ای برای جذب گلر جدید نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30041" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30040">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIvOPHVbqFd51TZR-Liu-mxBfoUgP-Ale_TQbftGEy6VoaRk339fvRzlUCwHKGg5BQ-I14X21jH0DlyzKngYSun5ulhtexQqsvm0QfdTqFJu-fRnuFH3ZDnKxaprh9WjJBjXX6_JE6ETPK0cZZapwgzmE6J6HBrZQNzpuD3TVl2Y03HwNnOjT6o3QkFWs4sVI-7WlVPFXV1nEVJSx4m5SNDcPvFuFiFYqCy7nFOdW2bRmpviOb81AF_d2CtFciDsR9cMJkg1BbXT8FMv-wcZ5WB4eN9JYCvB1rqDiCrhsGzQ5BAOZ3Y33ePadCiAYQoRdNSB4-m1hNrKngpKb-s4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ محمد قربانی ستاره‌الوحده امارات امشب دربین دوستان نزدیک‌خود گفته از وضعیتم در الوحده راضی‌نیستم و نیم فصل یا با پرسپولیس قرار داد میبندم یا استقلال؛ هرکدومشون‌پول رضایت نامه ام رو پرداخت کنید مشکلی برای عقد قرارداد ندارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30040" target="_blank">📅 09:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30039">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135cc26708.mp4?token=DLqKKbjlK5fz6TDwFCwu20--vgztsp_ap7TkaPEZmvmJkLfzrL5gyChSSi9iEGP0q-EgvU3PLS0FLXJozHjcnMjrJ5J2Gif8iRrjodvw0N-8_MKTFmlIUqeigKqN1zJdUOXKQDvJde-HGCMCIv-R1BTAlOUwOjWuDqF89zceD99R3hDoNv4x3MHyrUK1EKz60N8-M7hHrW-qSHGAM6Gr20UYlFflpBd9XEMiUoKHThM7A1y-aoQUOd8etWLlW4EZWioNofGZyl8YYbptPWcREAkT9fsg27ocMRIQFJBewqIekWYB2EEpdYau5ZHxg5BcWpWeXyRgdLe6LfQp0xNnIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135cc26708.mp4?token=DLqKKbjlK5fz6TDwFCwu20--vgztsp_ap7TkaPEZmvmJkLfzrL5gyChSSi9iEGP0q-EgvU3PLS0FLXJozHjcnMjrJ5J2Gif8iRrjodvw0N-8_MKTFmlIUqeigKqN1zJdUOXKQDvJde-HGCMCIv-R1BTAlOUwOjWuDqF89zceD99R3hDoNv4x3MHyrUK1EKz60N8-M7hHrW-qSHGAM6Gr20UYlFflpBd9XEMiUoKHThM7A1y-aoQUOd8etWLlW4EZWioNofGZyl8YYbptPWcREAkT9fsg27ocMRIQFJBewqIekWYB2EEpdYau5ZHxg5BcWpWeXyRgdLe6LfQp0xNnIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌سنگین مهران مدیری درقسمت سوم مرد سه هزار چهره درباره فرهنگ سازی تو جاده چالوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30039" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=pNh6wbSzQO9E7DxjsHxbCgNNhESlVJrT1cAajX9XfsG1q9-yuw7dSimcVQF5SPRLA4bi_DBb2ZHtNm8tLyIvqMW6BvTgyqPQXtS1FN_VsyR1aoq-OftqH2GoDjwx5KRRhSrTrTSaAuDdkeAID2E7bxV9FU1t0wMfTKwGEAq2Z8XAvNdyj_-ORojwGZRPaB0jYbkECf4jP97pP_FsMGCyd6WWX43ecuS7kEylBlTC7GRpHH2pT0jZ7C2FLhrHpbmc7fFzczvHBuB5_nJI390r65_aupCnLICtyyES2tRVtD5dgQO5nV_lL7wYwfFAkM5jpQF87FtpwruEbktz7useKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=pNh6wbSzQO9E7DxjsHxbCgNNhESlVJrT1cAajX9XfsG1q9-yuw7dSimcVQF5SPRLA4bi_DBb2ZHtNm8tLyIvqMW6BvTgyqPQXtS1FN_VsyR1aoq-OftqH2GoDjwx5KRRhSrTrTSaAuDdkeAID2E7bxV9FU1t0wMfTKwGEAq2Z8XAvNdyj_-ORojwGZRPaB0jYbkECf4jP97pP_FsMGCyd6WWX43ecuS7kEylBlTC7GRpHH2pT0jZ7C2FLhrHpbmc7fFzczvHBuB5_nJI390r65_aupCnLICtyyES2tRVtD5dgQO5nV_lL7wYwfFAkM5jpQF87FtpwruEbktz7useKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌مهدی‌مهدوی‌کیااسطوره فوتبال ایران و باشگاه‌پرسپولیس‌درباره‌پیشنهاد 2.5 میلیون دلاری باشگاه چینی داریان که به آن پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30037" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKh66Gu8fthRFlxvt9f7K1TofpzvOt13KK3r56HeRcSSWEgqLFkT8UKjIEEAbhJgS3kHYY70oLSxCWjJX0PJdigKbrSERZr3R01Cgp7z89tdZRhOaHlfjtdsXZhG0wJlW7SXeiBfrYH9rdvk0f5N3gEe5EBReW-4bEGzULyVbxEb75e8tAdooREa-yYvfEYfGlvuHgC4OLqi16DRnir0M2QYREgJjvnFPAGUT9DYMuJ60IROLAwVezJ5KAhtyseqZGwIPRQJTIy8-T5Y1O9MSwj7K3HWFKORW5jFmhPQdJZIBxDuili1mFFqx_rAMUMQ101JZ7NE7zwbfKyL8Vnv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل‌تمام‌عیار یاران دیبالا vs لائوتارو مارتینز برای صدرنشینی در رقابت های سری‌آ و مصاف تماشایی شاگردان فلیک با سویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30036" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30035">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhEnPf4CsmeJGUa6v7rG7o-A7Yki5x36tGZFfjBF_Z5rOpatPDiKCGpPwJzxZqzuoZlvKk8ko-WCxMCnEIDpKLYhM_i803UobKErpZCn8J80jbst6_Gxic4XULi91KOrejKFbni0CsloIno-RVglc5WwhVTYc8yakxtjdWKzoT4vVbWvKfBnHQE3KTY6IjDePiWUYuGjUSgx12ksb2Qd8Sp0Ae92c0BkRA20nIlq4C5gqNG8BhG8Jr0QofYJ_wNrC_oAaALVb5FehqsZno5zSUgGKnxIOqpqd1l50k_9xQLgVTyyHd4dI9GOVG9YMzIVcV0U_3c40jsBVsDhiu1m0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از نمایش ناامیدکننده یاران ژابی تاجشنواره گل‌مونیخی‌ها درشب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30035" target="_blank">📅 00:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30033">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
#تکمیلی؛بهداد اقبالی مالک‌جدیدتیم چلسی: از کادرفنی‌حمایت‌کامل‌میکنم و هرچقدر نیاز باشد برای این‌تیم هزینه‌خواهم کرد تا به قهرمانی لیگ جزیره و لیگ‌ قهرمانان‌ برسیم. به هواداران قول میدم چلسی رو درآینده‌نزدیک به جایگاه‌اصلی‌اش برمیگردونیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30033" target="_blank">📅 00:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30032">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDQ-_TFKvDgaXCRiUcghZb3NeiMpRRnpvDVJgZQlgucvRMsYt_cinVnQhssZbabOJcOqvAbhnBxSkDZs5zHyYdHQbMle5UUQb72hDW0nqT1D2vqhus2xX6ntpps5qElb3thhYUtIw7Nn34PG33Z7L2Eixl5Lhew0BNdMKorpap7pI3XLqQ6Sa606Nu4rru5hxZzgf7TKi-bit5LLl4KkEJTWRzenNFeguwoGXKlov6WgEnNNS-rZ8PY2dyNB1UTnS5HgQV93pN15XSwBDG9IbdOhJ1656lckMuXgBJbz_Y3QC6QxBU1BN6RHJwQWKkIlBHSb8b8GA3oWThvxA3BQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: دوس دارم در چمپیونز لیگ به رئال مادرید بخوریم. برای‌الکلاسیکو 3 آبان بی نهایت انگیزه داریم و میخوایم یه نتیجه تاریخی رقم بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30032" target="_blank">📅 00:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30031">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30031" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30030">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiyP2GOkaWrP-t8HB55PXgmTpbzQFnV_5SUKjgsp9KxcsT_mGVSZuW-1MP85oehft6f37bNR6uDobAXrtzIwKhBS3HCMs0Gvc4cjEK7_bzoEz_gH_7pXa0cet1gGXJ16r3Kqx1Mj0987zA_gnH0Ehrt45_zXquJcUA04eK3JTE5KrDPtgjF4E1exLUT7wffGgqKbCddTXViFZ7b4XPub6WMJMrepvTy2CmD3IS4vNyXAuCw31qGxWnQtSmXQIQ6zXccFKg3w2LguW8CRmtQ0KCWGtNiC_48lX8Di24Ie6Wp-xh0EsJdO5DVzKijVcjbkkv5vWcigop295hZx0pjF0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهم‌یک‌امتیازی‌یحیی و علیمنصور از هفته هشتم لیگ‌برتر عراق: دهوک‌مقابل المینا به تساوی یک بر یک رسید. الطلبه هم با الجولان 2ـ2 مساوی کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30030" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30029">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOvpyNnsfSwYt_u5cDUbeksER4jF7Ml7WpZR-0TfplrHp_YcuoQrakHtpUetZnjoidptY2_RDqgM4n3R6Cnmbi0T2BlLdbbJSeq1ixXy2xCLfjbut2w1-UI0km7h4rx2YWcaBxJ9m1GWqkKur7DOG09dnFSFBK9KSrFB3eyFBvMo8ysWN_OlMSv2cxpl5PyJiSZht9XZMmQ5z_lm1B6wXpyJilqMZG_TeX_PD7zvhRwVMWIsjbn4FPDoDS4EjvJZpgokZEGHWzEs2oVyql68LPBtbA8S8Z0OCRSSqZKVDIwkCmdsEDG9iwYLVapvezJnpag5BdXlBfo4Txc7aRMIgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدارهای هفته اول لیگ برتر بانوان؛ استارت پر قدرت استقلال، پرسپولیس و سپاهان با برتری قاطع مقابل حریفان در ایستگاه اول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30029" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30028">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=YZb4Hwb4YBXTfaX5nH-kLPuYmgqZxK_5F8i3p9IVOcX6VVaiifRu-soW5HIFrFEEnH_glmSidIRrjIbyt6Z7hWROGgQnzQRfhbdn-omVFArzOlTs2J-NAc2kWTknZ6G3IcMohRbRmjgdcqAtA8fuxiZkyzQ2G_69qdXk4LNIDobViAuJLTyupFChAxhZNEaFsmx9OW9ms8mPIqFUFXhbFJBHqaxfvrhbb_co6w1JqVSGSx4cEi8zYLHGhhIRgTVFn86AM8vaOgU_36w6oaSj7UBRdVyy1E0iWkfseOriuAN3rO8K266gYyIg6p6Gz1cUtapgitglbqjcj8oGM4eQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=YZb4Hwb4YBXTfaX5nH-kLPuYmgqZxK_5F8i3p9IVOcX6VVaiifRu-soW5HIFrFEEnH_glmSidIRrjIbyt6Z7hWROGgQnzQRfhbdn-omVFArzOlTs2J-NAc2kWTknZ6G3IcMohRbRmjgdcqAtA8fuxiZkyzQ2G_69qdXk4LNIDobViAuJLTyupFChAxhZNEaFsmx9OW9ms8mPIqFUFXhbFJBHqaxfvrhbb_co6w1JqVSGSx4cEi8zYLHGhhIRgTVFn86AM8vaOgU_36w6oaSj7UBRdVyy1E0iWkfseOriuAN3rO8K266gYyIg6p6Gz1cUtapgitglbqjcj8oGM4eQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نحوه وام‌ گرفتن درایران به‌اینصورته که میبینید؛ تیکه‌سنگین مهران مدیری به وام های کلان بعضی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30028" target="_blank">📅 23:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30027">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=QLmF1hvI-q1FYeeLvm_YvgRUY0sZKww4JJK8YxYgG5IIra_0YoZ5Ex5iK2WR3uL70eF6ePVQaj839p5X7oxMJjGsuvzwA29d5lPdHZ6-gBFDes0Qaaxn-kxezpiAT7Q2V-73bZDX7hd0O_IbVOpufbT03urpvB9_6XAPqWnlL2ARVLJHzVbHpcncsIeBazgmzsQPyZh9fES3jLN-T9LETsx_lCy6GMMlnVUUqUBsqGqULA0rvj_j8-3b2dsOWdrdaYfNRT8Le7r_segeqS_t6U0mS0v4BI1KAZC_hbIexy7JxlZoy3uynCGOl_0JfC7cYUs_IEiw-WlizVO6Rp3rEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=QLmF1hvI-q1FYeeLvm_YvgRUY0sZKww4JJK8YxYgG5IIra_0YoZ5Ex5iK2WR3uL70eF6ePVQaj839p5X7oxMJjGsuvzwA29d5lPdHZ6-gBFDes0Qaaxn-kxezpiAT7Q2V-73bZDX7hd0O_IbVOpufbT03urpvB9_6XAPqWnlL2ARVLJHzVbHpcncsIeBazgmzsQPyZh9fES3jLN-T9LETsx_lCy6GMMlnVUUqUBsqGqULA0rvj_j8-3b2dsOWdrdaYfNRT8Le7r_segeqS_t6U0mS0v4BI1KAZC_hbIexy7JxlZoy3uynCGOl_0JfC7cYUs_IEiw-WlizVO6Rp3rEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو باشگاه ماخاچ قلعه روسیه از شاهکار تماشایی محمدجواد حسین‌نژاد دربازی شب گذشته؛ تکنیک‌ و آگاهی محیطی حسین‌ نژاد خیلی بالاست سریعا هم تیمی‌اش رو در موقعیت گل قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30027" target="_blank">📅 23:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30026">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl2ywQ6pCgZPhKgVGkwp24hcNs-oqMLT3bsAf5BiXwb_pPcpk6N3hHZBwmaS4sVDsTRsGurix-uYfLuxeX7tF4AerIDtS1-eN4Y3Fr9X0WR9n2tR67oNAE7tHA03XCzmnfAWt6TYiCRFN4T3m7kg8yJUp-RBkSF_1zkMWcUEojwXBWqGFe2m_g79lzVQV5AhVNGYtXgJPL9Kh9Cqovc_65rfKGbxe4smh-AEIl0F5weYnryAg770Q6hZ-YioC6tFc0rMIV_SG_0SeXvTc2h7IaA6sSoyHLB9tvhn354LHrr11U-p3vNTWnV9BymZJVlqh9lji72d5CxvrrNdI6thGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بااعلام مدیربرنامه‌های داکنز نازون؛ بازگشت‌این‌بازیکن 31 ساله به جمع آبی پوشان منتفی شده و این بازیکن به مدیریت باشگاه استقلال اعلام کرده علاقه‌ای به بازگشت به لیگ برتر ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30026" target="_blank">📅 22:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30025">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaLRw9b8KQ7NbI2CQDS_ns12IzuxW9hlAfMB-kTKED0sjMnVSvXe0cgGNgMUhdXW9X08z39kZ4dLfWNIrjc8uD_bFSCIjJBreeiHauauunYZAOUXgQfMOmwSwXRCfHzRe9o19L9ScQd8AzvklNMuYjZoDSS0stMonZIBYTxFkfj8sP5qI3_3p3snG9H-jmSXCGZRrk4hrwoxaeNJuFI0qvhc0I5cszzbJQ-sGe4VQpGzY_D5DpQ1WCoRqVSWuxIcdWTmoFwso0q6JaRD98rgEhAnjnkY2WcOvS2f7qR2ltbh_zaFsZM42JYcPNN8EEnIE4m6WKXUb0RH2sFcKkrNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30025" target="_blank">📅 22:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30024">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkiPIJ3s3-opLNJW43lqBWZALlNXLeCg9zrHTuN2gRw87nS82c3MOQdj9h1zqNl2k5Hpz0zx-YohQkQ-wcT3DNBDnPPlYd8QBEmdXi9rDFdkzasPfLyxcnuwlcWniGOz7TLQn3DslkZd2nFGtA5HdUejNbL3HHEyvCtGun6_dfHozCpR-X09Y6xbIWvPeFsP83pj-SkN-z5tX8a_5RvyLc-P3JIQC8q50NARTOK9looNz7RzidvsJKJw3Lpf3UruAj-21Zol8-Gz0lBhbimkY83x_OrALoY6OrbRUXKHWu_d6pqrDBYzgWEq09jbetp17PTuVMC5tf7ad_XF-f1U0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30024" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30023">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PG-D3ModeGuGotwRidPT_H54UPrhIsYiShlDNpqNZ1nJlWbvq1NjKz8hdmZ66ndBmEFL0121dFTPm25Y8VdtxF5R8mIIHOPAKpZL8OTogCygFHvF88rLh6w3MZMSDwFQOIxL7-5aPp2SQDorGE1R9m7L-9Lw6RSBhYr8fNQAuzBHgz5O1_UQfy2Ipxl7kEkiNUpx0pslap58Ah7h7nbwJIfGsKClrz11tDqwk81BdMdxaT35umZI83mWsiSm7CguYacRkCDOLoFgmwn_QLYoT9_YkefvSmu0PJZ3iW-nWfSBIB21farpGybKqr3zF9V-VBFPNHrzYiImCtVtcmeg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی تیم ملی پرتغال؛ کریس رونالدو اسطوره پرتغالی 41 ساله تاریخ رو برای فیفادی پیش رو به تیم ملی دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30023" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30021">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArUhk0vzp6ziOb2r3IZ4W_OG0iSrMtcqgavZPu3rXmOdrI6oqErOfpnvzu5XeXHsnd8RFyXuv6vc-zOA7oxK_-LBn0aLs3DG9tNYvR_DzeDSt0w9L31vdaolNBDABAFoMbXFbQX9OnbTjQDQTjCKILGFbckU3Zu32Yh6QIG4vT5wRKT-fBtFN6hr-dBdGlbgOdYfvRJ9kp5YbR3k2lPjp9oxImlf89dxASlE3yz6pK_PmIO0SMZt0idvNXx-M6lx_266tHT9Jf2YHYJSgd1LhpLjVGwhYSAVgiOdX4k8MTwRiDi9GNv8xt_5dtAuZJj9bCREkZWPp6RTdwb9aXh60g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30021" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30020">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🟡
👤
سه‌سال‌پیش‌درچنین‌روزی؛
حین ورود رونالدو همراه با بازیکنان النصر به‌تهران این حماسه تاریخی و فراموش نشدنی توسط مردم خونگرد ما رقم خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30020" target="_blank">📅 20:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30019">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ps5UEbC4za3HC7E-YkgiPBm9G7K91Ala6MKNsIbe60kEhTQef-8Xr7lsuYMIhN0tymF9rCmeBtxjf544x7JFP4y2PX0DQt0qfehx5rNm0xNh1KGxyxWULOb4pi_eFXfGV6UHIbbMZ4eTwfnDu4yCgbfEIgP-agWOm9R0LxF-P6T8H922GoVWk1RvxFiVwnxuDPh8Llll8TgKbZ-KntVJR85TgQr4Gqvd9epBVC-YMcNU-34VxRCrNvJ6i4Zfyv9Iema2u0F6zE6iSlE0w3hgzJFvC2vJ-CpV6YRilM1P33zrcCQc1wamd5F3Wk1W3WVuAiqwfjkGLV9NkuPx0CA8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30019" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30018">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJl-HDcCKypDpECBLtdy2f4kGS1z8eKF-QWAhUVW8IoeQ5FSa8Lcle7du4jwos963qBUVPQcxkpq87RDLZDMWGofSXyq_XTWNSyPoEBECQNKoo4vpnSQPdumQx0Cj8gMmaRnVDTbvamr3VR8WRkbnppeUg_pY6nME5em4mMeCsAgOWhl_vwEQs4c_Fb0dTPYOyvb0p6PXD6aiOsl2Lu7wiYJG2B-XRbXhtbU3a0pWUE4KvCgAriMR-NDct9tIkij3hOnyJQFyWWz00DeOl-tdiTLNBS9_pHCU--PhMLQv4kxYmUvml4sbjOEag0Ei4oaJDJtJ5J4ZhoKgR5BFxyrJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30018" target="_blank">📅 19:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30016">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARoL8-1YTi3dgTR4q8Q4cA3WNEX81bomdc26jpuT0aIHUZUt5L1jeC7kcp78ytHoU9c9Mq3BUp4ZN9aZGGlvstYBwdpG7r4AxAn8ROU1JPEqrBOJtbBYX48TKvcxORgxhhWMiGU4PQeBtM38GNwEFLXLdvyvv1TwfK75KIE6k0GhAGuFdhqkxp1_dTEeqBbjJas6PJgYIqi6XQyB4VWqMvBCxxC1rNmttgPTfFBnCb7UAfG3iqoWD65cEwrnH_9FipQDoR89U3GhBWC7hDOv8nMFXu7LDgsCLsKCIIJMW21r7N1cdF0wtOUQFzNpG_IIk00mXUSX32tp_jE7S3AFAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dl5go2CyQNG77zTzGuLJqmMQCmaxGdeK1Q7rxj2Z_1dcSSJ4PCy2kQLKWgjXAgv6y7imUfmyRdISqHU2irGG_aInk6CZqOZr5ToXDBW3-CeQQObmhMXo2j8zVqMs_tZN8PrVZWcJd5i3Us7WHcxxFe_ugta9F_gVdp0P3Yv3upScfolYs1MThPmk-8uP5mnjc59OAVegoPaaH5IA6Q1Gyfs3MpXka4MNyFtloWTStCCmOyhsF7YF7f-f9w2Bze0h5aC_xXvH9NtSiXWbZ8W6NDgxhqOh9F1DgWQ3SxBgt8eL_0XDU8HrThY6A3BtFPxSew5z8cMFvDzgZN0vG_zKFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30016" target="_blank">📅 19:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30015">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42Ra9kj6LCzfRMKMorZ9EF73-Ewe_bX8EaNXYNpLm4uJaebo2pauttoB37YRVHy6ySwYCUxLNVRndapqO0sAReKjEKjO-zqKlz_96RPtqnztUDn8q1FYsYeayCIWQV8Si2DJ1fHoecttQ8Otq8_OSBBG01klXXlzxLHV4xd8kI5PeP9ajnoofRTk1whPkdMstCXbSw0JgOHwKpRePsJPKh2SGrG60EG5RBFFZBusFh15tgMqPuwUJn2btCm9GFUOrJXOvCidR8ao_JAExviZqzwNCPJjkzVGQNoVuWUQXVZDsIfObeuRoXiR3uHYZ47wuxw2W1FLf2BYINCeZoVQ-CP20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42Ra9kj6LCzfRMKMorZ9EF73-Ewe_bX8EaNXYNpLm4uJaebo2pauttoB37YRVHy6ySwYCUxLNVRndapqO0sAReKjEKjO-zqKlz_96RPtqnztUDn8q1FYsYeayCIWQV8Si2DJ1fHoecttQ8Otq8_OSBBG01klXXlzxLHV4xd8kI5PeP9ajnoofRTk1whPkdMstCXbSw0JgOHwKpRePsJPKh2SGrG60EG5RBFFZBusFh15tgMqPuwUJn2btCm9GFUOrJXOvCidR8ao_JAExviZqzwNCPJjkzVGQNoVuWUQXVZDsIfObeuRoXiR3uHYZ47wuxw2W1FLf2BYINCeZoVQ-CP20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابک مرادی هافبک سابق استقلال: واقعا دوست دارم زودتر بمیرم. خسته شدم از این وضعیت!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30015" target="_blank">📅 19:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30014">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=qCujdzFbYFU6ERBOZMMSLjn8qY-ZL4QNHRi8fNt5mwlzjV_k-eqMaPfUwPtfC_dDVcx8NOoiO2qqiyVtrMBU_im9jNer54oUfunLNhgWoVL7dGuqWOHZWfA3KtzkSCDQVh-nP-P8SIXbfKPbDqP6MZu-NwvX7qaAM1mi6irqPD4f7VNHi3IvM69ukV4XdexEfxHtsxGUkpIvFT6A4tzNJy_deRzd-sD3GJgZu9ZIq3i4F9schU_G-n8aX7ZvPYYAUpmhBK30_RrqTGUr8uj_7ore3PbhNg8lTVzVg_NYOKCNQzTI9vgLEqVYAmBJkmP96tFK0v5rbA7vRIZfBgzXnaZul75ZP9W4WdRvUqYHnrreE_DSOWhM_kD02qDpqVABroUNgnar9qep-LSg7TikwE-rdUH7XU9SMvQk8BRsvjXirQjVZ-H2y9pjLaH0ZrfYLYSmCHeziEHLnRlQNRPP3KMsJR9RF_iW5Na2EhGAJfW5qAsXwSX9WMCeSF_Ld2zfP6xtE0I6z6QzaRe7FnK1h8BCoD9uSfX2f2VjgFzPKl42Hsgk1unV0baCgSdiu3mQMcpth6xMnFYDEBE7sBOxcZ68SN5hOBCLoK8NrEeZGdcCNj49lgNxXr-2glDs4c8izJHp8R6aH_SnUmS3CEfhP_b4B1dJfyqjjAxevYAn8q8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=qCujdzFbYFU6ERBOZMMSLjn8qY-ZL4QNHRi8fNt5mwlzjV_k-eqMaPfUwPtfC_dDVcx8NOoiO2qqiyVtrMBU_im9jNer54oUfunLNhgWoVL7dGuqWOHZWfA3KtzkSCDQVh-nP-P8SIXbfKPbDqP6MZu-NwvX7qaAM1mi6irqPD4f7VNHi3IvM69ukV4XdexEfxHtsxGUkpIvFT6A4tzNJy_deRzd-sD3GJgZu9ZIq3i4F9schU_G-n8aX7ZvPYYAUpmhBK30_RrqTGUr8uj_7ore3PbhNg8lTVzVg_NYOKCNQzTI9vgLEqVYAmBJkmP96tFK0v5rbA7vRIZfBgzXnaZul75ZP9W4WdRvUqYHnrreE_DSOWhM_kD02qDpqVABroUNgnar9qep-LSg7TikwE-rdUH7XU9SMvQk8BRsvjXirQjVZ-H2y9pjLaH0ZrfYLYSmCHeziEHLnRlQNRPP3KMsJR9RF_iW5Na2EhGAJfW5qAsXwSX9WMCeSF_Ld2zfP6xtE0I6z6QzaRe7FnK1h8BCoD9uSfX2f2VjgFzPKl42Hsgk1unV0baCgSdiu3mQMcpth6xMnFYDEBE7sBOxcZ68SN5hOBCLoK8NrEeZGdcCNj49lgNxXr-2glDs4c8izJHp8R6aH_SnUmS3CEfhP_b4B1dJfyqjjAxevYAn8q8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
#تقویم
؛ چهارده سال پیش در چنین روزی؛
کریس رونالدو فوق‌ستاره‌پرتغالی‌رئال مادرید این گل استثنایی رو در دقیقه 90 به تیم منچسترسیتی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30014" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30013">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5P-EBWO6-7MKODuEtVvkaTxUU9GnqvxFTgob8lXgr5COjz_ZjqQ1yOWliDd2Rreajw1WWwa96Ik743IyOO52Vl3Bnd489nmaacU73sqjbrQaNlL6BW4oi9Fn14PgEzQzFTRc-0kurg0r7sS6O_mjIfCy_BJyhXMwcMrw3zGANlDB0IWlzBbgk64G4L98IUksoGX-HFQw3OOT-hSHt3-ptnLSsvDL8H8-SJm7SbHfPM70e8TvvXmmJ7d2XrqB1r3_9_m8W9RLyuMqo-uwGAy8hzSXzYrB11iajYvlNY8eQ6U62a8KZ8WVzTXhSzaJ6-rjzBcqP8zxH4ofR6WUU93UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تقویم؛ سال1999میلادی درچنین روزی؛ تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30013" target="_blank">📅 18:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30012">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWzfr2JH0gXEcjkkQN2e664HOqmqFTeQ9kjEpLZZ0y7VVxz7VHS8wTpc-cimsfvCPc7_Lf9SI1f6tg995azI7ONGt663SzHUPo3RRa40ViN_q0P_Ca3DcBhKIanxMFVEb8elkyhvA5PSlnF39jSXOG1cifqktNh4KK5wkWmkhRFud2O6qBvAgJyu9YXWyNA7lNutcgHU4UO4eJwTEX2W_heWkJzBp84cMC5bX1DHNJEXGoN70cBBfQkmSNkwqtAysn7VwjAIdaBQ_3_bFxA87R1NB0XV2cqqValO9wYzFUSml7w7chaNgv342aN_PBuPBcefYMcL8-Wx8B7KoBf4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30012" target="_blank">📅 17:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30011">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seaA7D8Au8NA-oNkRcKvRoCqw-VyEHmxaijhdWJya7Ib7MfGCTx3xjqHku9KtdjelqpDVViRstTKnisbSW-l3i4alG1lC1cAJFUD18MpSZHMoiq6oL3qJb68gCcUCmb1MZaVAQBn4ZWVSS3MhMMhHxPxMKtMOMY-hK9pLiA1YhTdREgvxu_H9shb9vLf5XbORCjKftYqNqLTQ0SagOOBe-iu_Vp-QCl6cU1ZZW2fwKWHO8zugkz_GAyxF_WlAfGhvGgBhXebh61y2kA1IVJg0fH-WxZw0sZcUjfvJgtpkK7tbMRgzsi0h47SENNYH3wcDOPS0A5bIQD906LERSaWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلزنی آلیسا لمن برای تیم‌فوتبال بانوان یوونتوس در هفته گذشته رقابت‌های فصل سری‌آ ایتالیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30011" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30010">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=jDdG5uMwkxqNLG87X40nFp7dmRCQ_CLaMRzacPV320Xkh0ynPhjf-bJt64ZYidqP8rXyfbtyBiENzjnGdhOyLORdulbzBF1TC2NSLM5NwuunodXb5wvtV0JWg8dc9uLpD1t55tACvO_B4EDYJmYb8CUf4B0Ggq_8LOLO-5wlrpGy_4oKB4G4XZ7UaHlKoYX4ltBCjDKolyQUo6vD7euQ84EtKeR6Mk9sWfmHC2M7EtkgKJBZRDZmsTY83cvXca3ILowc0gQl7Ni6A-Q_SYfKxWD6tBeSTr_fXbZQf3HBe8BTUCPdO_Nr6OGEAln9kV_6pGvYBjH5HAW_r4Ke-r5eog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=jDdG5uMwkxqNLG87X40nFp7dmRCQ_CLaMRzacPV320Xkh0ynPhjf-bJt64ZYidqP8rXyfbtyBiENzjnGdhOyLORdulbzBF1TC2NSLM5NwuunodXb5wvtV0JWg8dc9uLpD1t55tACvO_B4EDYJmYb8CUf4B0Ggq_8LOLO-5wlrpGy_4oKB4G4XZ7UaHlKoYX4ltBCjDKolyQUo6vD7euQ84EtKeR6Mk9sWfmHC2M7EtkgKJBZRDZmsTY83cvXca3ILowc0gQl7Ni6A-Q_SYfKxWD6tBeSTr_fXbZQf3HBe8BTUCPdO_Nr6OGEAln9kV_6pGvYBjH5HAW_r4Ke-r5eog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ سال1999میلادی درچنین روزی؛
تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30010" target="_blank">📅 17:28 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
