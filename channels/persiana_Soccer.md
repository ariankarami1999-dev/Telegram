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
<img src="https://cdn4.telesco.pe/file/dxjWttm1eoD7zvH2Mb2Uw7FZ-8PkdNfpiViSv_GRNxSYrbP3suAn01wluDKPcu7rJ0hGvSwteZGH1xjXW1Kfm-2QI4q00AN9vUC-MItuVyXFhda0DE59wXlQwG1IHHMy3NDWdfwRFfBacrr6mxrQCGcy8jcjxURnFqZBdRlQ9EZcrl57kYXveMEkGne0mSAmR-Z0EnryxOGI8ti4GBLUK1CeUv-kuwnPQIznEU3WqLjsnh3BU_LR5EG9x1oKN0yIm6fma-vSDmfDR__fSOfFIg3BqCKTsju9tuk39dnvcKqdKNNWLCBdIJy6wWfqSY4LYtHRhzR7KUl8OR-tbUOUdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 623K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 02:55:44</div>
<hr>

<div class="tg-post" id="msg-26979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m920qkEA6wA7S9p5_sdJUIaTmqp-myCGep4aLlxfb5qlYed1crPlR3Pg60t-RJNS9DBU-SOonbE_YldJScAOhPY7-PTJGNBhbN9cwTedj6th8bHBLLXt4MXxEJBk4tEv6dbCdxtCwS9Y5ZUMqvveYkGYdHzTg3D_aikish_xcyxePSIPJfJvJ76NIlbdO7x3xaThFMNCGmyoFP8hEjhWZvuCr9EUHcFfDMy4VoyBGv05m9IN8WQBRYhAgWNNHKNE0qYgy-4gOitXLGI_N_V-AuxhzuE9VDbwRwTeCsdZzM2kbspoEY3FyYEbiPZIKJpjQWKEh7EZxZhew8Z1gvWQRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تمام‌برنامه‌های‌هوش‌مصنوعی مناسب برای تولید محتوا در اینستاگرام؛ یه جایی ذخیرش کن به کارت میاد. برای دوستانتون هم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/persiana_Soccer/26979" target="_blank">📅 02:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E10L5c_OqYjhgnAi8s3j3LrbbWWEmkCb-2M6oOMxUCVy8o-O13PYXtj4aAr43-2C7CnUTbNFKSarfXz2Rn1Cg7EE0nii8EzSX64Y7QqH3EjZiZv_iPiEvh-NiSFerWK7euWhQpAlWS4iPbGC1WoIkB9rXWEta9jAREoXCnxG624A4A8qtGIlM38DwwPJnmQyCGjANq0RgFz5keoX355i2BGVuhY60Zenyc050bVJEgBdHxvu5jm3ICRDN8HYONoTT7fdBROo3ED9DleWtr3CWLwUR-jm13x5Ff7RuwzthzUeHNy7pY75vHcAFFaaTF5qrucnz89BfbE6QK0kIkWZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دپورتیوو مونیسیپال پرو که به خاطر بدهی های سنگین در آستانه ورشکستگی بوده و به لیگ آماتورکشور پرو فرستاده‌شده‌بود در یک حرکت خلاقانه کیت خودش رو به ۱۰۰۰ قسمت تقسیم کرد و هر قطعه بین ۲۵ تا ۱۵۰ دلار برای گرفتن اسپانسرینگ به حراج گذاشت. جالبه بدونید تمام شرکت‌ها محلی و حتی هوادارصاحب‌کسب و کار به طور خودجوش اسپانسرشده و باشگاه‌رو ازورشکستگی نجات دادند وقراره این باشگاه به لیگ برتر پرو برگردانده شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/26978" target="_blank">📅 02:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26976">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFlTkjgBGKXEdefTvvxj8o8dF6sXwJaS-7re12pPoKvsQhd4eVHMVcZssphQLUMYQgenq4c7TDb4cIt0YHiwW7SqDxxVMIFxBK-HAq6a_m-I1tfR5VfEGRKqQpCbTP6tuiLxmzgLLgCHuL3IKoJgHjhKvTCVLI-wyj1N6yg0MrYf63B6qxoTG__07V_fMlS9D8GVmmpDVu7fWZzQuiDik4cMaNHK0-XxH2CVxK2ivfdPJXe8otDepRb7bhLX0A74Qg6v57bh59vt2zQ6gJo9mL0fdXhVEt3AUuUkhc6vf4510GBXRkTAbb2NfujTEb3TzfZYWz1EIMQAlba1WdY8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
بازی‌ میامی‌ برای بازگشت به صدر و دوئل‌لیورپول‌ولیدز در اردوی پیش‌ فصل!
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/26976" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26975">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/namfBsEFqdZxMC9ANAziQL6ZzDOb2TqQXMf-vlBHT0nj-ZtyjnVKDzOzup5gTZhn8Bkhu9h7BYj8gGn3V_W48W49SiYSbFDxTV-UB03M8abn_XvuCxv6HIIEXtofQ7G4dNbqFbarjKSsYerR3J2_HMJRgT8HVJ_yzBto3seoqJJkRkfFhtK4T3ngmsGfMupnb4zIIiZNDIc1nEFY7I1whfhD3O8lRpimFj2mNC2oBHRciFVausj9mTH3wOOu3-PMj4bZcPRxhCPE9hl63Swoy9d9fXT0gBaynQC0USKiGuLwQi18gLrGWCMTTtvQa7WlibOK2XUywshMUaCjtIpNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برتری لخ‌پوزنان با سوپر گل صیادمنش تا توقف رئالی‌ها برابر یاران دخیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/26975" target="_blank">📅 01:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26974">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX1Ji_nYSX5FYFf5QvrKid0WdMFQxeUpmWnAiytD5hmJkZdNiP7GcC8BXX5P0xtjWxFQFKbExrF5b7NQCLf65REvDYtxFZCa_TdazQkYvB8b-iib-oSXCpIfYU3Zqxz25KQW7BoZi7BwlUaYMvW7JKPeb7A0KSM81uzdQnSftzqqilZPZxweTsbLG-WmMJvGiYg0d-9iBCa2TRIpAskkPhsu8T5A5tOgFtBP0Qw41nsQK24aU-VKUd5s6UnyeVtyEWw1gi6033qyhhbQ1m3Yw9LNUEz0K2bIbSaw68WLGZyd9DK3CTlT65eavrhmwkJSYTjhBBJQ9vKgWWTmFT93Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/26974" target="_blank">📅 01:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26973">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOTA8Bu5H8UMT4uRv5sc6w8OGxBVV8NmNc3q0fhJNzk1YSPXPGxxu4fZH5fkfHKNBY1zX8D1WLPtKvPw9wLf2IMEcdyq_jupw8FtowyVXCk5vlfJAQcNhnZicthVatFf1uzY6i2-BaBBCBAm2ql_ZlcyTVGjL7wWc9j2vuqK7jhM4TJaJcm_74FoP193970Plf8FANTyWIFbS77a8GleLvXiSX9BBEQqLJgzPibK6Ikj1MGBAplxLbUOWrc3BQkqqv2MtzrzlWwHLnWF4dSpupNZf3ytF7jJi8wg2T8zav0BxPaz80X_6GqjgDyZfi7Ui6pkXAXHDRPocbHtzCrkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون مهاجم سابق استقلال: دوست داشتم درتیم‌استقلال بمانم امامدیریت هیچ علاقه‌‌‌ای نشون نداده. بارها گفتم برام بلیط بگیرید تا بیام اما باشگاه هیچ پاسخی به درخواست‌های من نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/26973" target="_blank">📅 00:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26972">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXsQf-QfEwUw355lSPgnSTnVp3RZm7Kr1bv_2YSmu9E9slAOM2vBRUsamTmtN1NmYv6ykk6wKrFC6wjuJT8hDRrYHIB8wt1moa7MCnMtjVegxzjtd93qIZfoZG3W95Ho0pBufOlhWYmHPawePQvbSkoVc8j0nh0eJTxvJMW63elMYEAjGvVi9UiOb88lmeX6yggLQEld6OmrbhUE_zqM_8ojm0qAlBw9I1hEnhWP7kDdUHHDD48I4G5gWfqMC2tItSc8ThuyZfboSbHcp7F8bUo00qbseNCmv2axQNt_hKd3626LdI2ekM5Dn8NrOuNIqkYG2b6UviYZ3Rjy7vhhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/26972" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26970">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhIbpPE6PLIdehsWdq7IhO_QCSp7sb1-YglLczv0wPxhzmRCBgzZE5n-l0i0kpMUknqiCn723I3_8fQ4stmYXYqDPx6TDA48nQ5evYZHAMUc1odnk4i4i0pBC5NFxZwAl9TGLbcvt14MQGta0QGGOUGXmife0qUnQwovGTd63mhC_WV546gJzjrOxLiAHQ16cZ_5xzQxGJsGRyjwvntH_UuCjHfoHEqhbDOXE29gBXY6PRk0qo2UWAtV7HpvA67wGeUN-uaagOOWMbtKlAF7vPNKb0LKpLsDQnkya7mqQlj4R1ChS_fLp5jMaUaZhxV_A5GzMlMWJZxIUb3RVQ7o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HW8JcJop0fdjUhP7O2ZCEYeBFpNiGK4TM10YmO0tJgbrIkiPEikJZHXjYMeVzmm1xJj6oa_nomR-UgmJrMkzeAlNGQNoZYU0SyqSAIrdXwmxUp13qFNgqzh5tkI5KrhKUzVK-uD1FDdrlKubJa7Qxmndsfa-2fxXl_nt0sORhS-ZujlRFGk3SJUYhG8_FnqibCrdjDL0PukKxnToElHwNtAGKVg0jS99tqjLlSGc_rex6qHixgooXdynTruPxcgBvvWHiOjiaW2C1gUtiy3b-N3vFFTuYxkiIl0E9psEH8Qh2Z6n34H3vOBSl1iDR2ON7V6ynW94vkKZY8DhR2-21w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دریابنگر دخترخانم 20 ساله محسن بنگر: از بین بازیکنان ایرانی سبک بازی محمد جواد حسین نژاد رو بیشتر از بقیه بازیکنان حال حاضر میپسندم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/26970" target="_blank">📅 23:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26969">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGkj0yp-MGBx2IaJGP7PmCZo_G-RgMhArGXjuj6mgNNNbG1KHIUBj4nYHROQ7iBW95kGXiMQDN6e4T1ca6mzofyWZ7B7F3n_iVr5vBoZyaBF1VZ0CMvLn9o9Sl4B6xKULw4kC8f6FC4sKA-OibgwmFPEIAtkyEBXpZKnR1IHfGXB5aleUJh9mPO2dm1RBeBrkpdv0msuB9t6UI8WZyZjFO1QrMHrM7188Oby_lHaZaXYp3ATEHMUYiK1GJsPXmd7SczIstBuIebr-Kl02iNK6qhNwvF15PB7c3scBhNt-85xFGKCDhepVfuCNwDxEmRL2dpEcq9qtwNiHvuEedGN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/26969" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26968">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJcGmFTgXeKGsArk0bLpQypS4TrFGYuiEt-dcAUkE_V5fHyfAXtQAXmIU3eyH5NhR4nfMGccWbEGi6iJTszlAma8G8YqmDoUKwNCXTL1CrKRw2Xtt7Os06wzGl0qp8TQA8ixEnBYcYkh6_1_iLUL9kcUu0K8fDbl-jptA1zYzEhthy619GQDSfLfCPF3OkpQIWefQClfyIFQiA7jMa9SfrEftM7x8jSjQyBmRHh8EqLaCpenbQ4SeQfVFYxft0orNx8Fm5h0wLEka4Q4ytOvKs0hSe9rcFhdcSXXPZGBmBiDZqayPu_xPbk5pPeC_ZHTNl04Pb6LRoJqhU08BhhBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های ما از باشگاه پرسپولیس؛ علیرضا اشرف مدیررسانه‌ای سابق‌پرسپولیس‌بار دیگر به کادرمدیریتی‌سرخپوشان پایتخت بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26968" target="_blank">📅 23:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26967">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL4M4pDR0qeyngTH3G2rl5nXsujun4Qd2RrygoLb0CJJdSQ2q2i9MLpNx9M6WuchLfAM9fKE9TBMO3FC8Ot2AvWNX5HdTSMMCUknRnT2-izRVbllxRNULbLU1fgoWlQ9RkibDIY_yeoXjPeN7xyrkCSWwbNBnEmOTvaqkBYgI0If9FmftMVVuLZzzAo4W-qmq6MgEaI5aWAAVmxCWvkR8orRprbjS2mCToWlfPnRGNj6ouhgRSaEHc_80Yr1saH6vHLjDNMihwgwm2C7mBKbMCiOoc-xxYNAMbedfxCVxJg5Xep_oWDqe_f23ZCVit1-O7nFCi1l6mwbZe_9ID3s9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26967" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26966">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBoivn64JUdRZr2isyCIh7za7kdAZ6TnMFM9amcc7-dPW-OCLxcN-mWL6wIBlZVieoiC_W-KDuAq3wOXDw8-ZJa68yj4f7p3w4CgNdS61olk4cjja4Ol2n_OlyGdJKCXua2Tig3pvineSrnfHnz0MTIrKyoFo_b-2o1OvalXM-8OD-_Ae-WoZe0aMIfvEhJ-E5ONYmVJIVKj6kF3JrmqC10dv7XcJOC1A3Bc9G4_jwm0VOqwqY7GQ-dtbT7Xn_nRAQ1h9UyStGanJc_66QhttY5LMUsutMp56f0BOm33Ad7JA4KSzzUSVhlbR_DIPb3ttyNMybi_s53EvkLPCh4Trw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف‌شایعات‌مطرح‌شده؛ باشگاه استقلال تابه امروز هیچ مذاکره‌ ای با آنتونیو آدان دروازه‌ بان سابق خود نداشته و برنامه ای برای جذب او تا نیم فصل در صورت بسته ماندن پنجره آبی‌‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26966" target="_blank">📅 22:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW70BsjGJ7O1MFImFenjokgD-7Vf9ZTo9JitdhXIprOj6Y1TRr_mJAFCcNKoziSDK-PKr2LD13SgVplbMajXAMtbaxLVKWV_DXotIS6RB-LlPfcjlOKwnTEINf3OtDiOmOJHL1-Xy3s_zOfsDHhChFlUGhVKGXgtnA08Nwt_C0RSt7rA6CjQ10d3GeaMt4o8o60d8JYfG4kXq0Z184U2scOYytgQTw1qLgn7v757ToED7-KgEQJkN044vB9KYT8If0yh4itrsKoMVqyIHicd0eJ3dwahOinpIgWhDzOCvcbPifxMLhw87SiXcGOg2pLquc5cWNlqx2m-lACC4CQs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید شد...زهرا خواجوی دروازه‌بان تیم ملی بانوان ایران و سابق باشگاه گل گهر با عقد قرارداد تا پایان فصل به‌تیم‌بانوان پرسپولیس پیوست. همچنین زهرا قنبری مهاجم تیم ملی نیز سرخپوش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26965" target="_blank">📅 21:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26964">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIPqeXDYxBrS0iA2D4u_ZCig_AUO3ewbJI4TP-g-bfd7oB4sWoZxSfjJmxugwaYTuUaiQ5jcT0dB3061yjm0rd-8ReyvZl_eyOH4L3NQvazyQvdVxit60BmLZySaiNToa2JFR_cxM2qFhifuTQ54dSd51IoFWmnDADLGpTsN7-FqAL-Q0A_NAQLIOdTgnA_2ZC_ZqRtmOazeZz4ZujNHgh1AnxlCLHCO9E_sXMH78PoEmz906nRh-Z8Eo_0o8RJDMEpyj281GYJpOMr5SXGerOeeG5e7eonhkltY4to7VI5SAD5pl9EGS8aCHcq3d8ftoNfcutqCx_IkPsftIR1uVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدید
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26964" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26963">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLjGodyE8R1ZiMlBFrsE2Cgq0WtucCb9tGmxlOQsdZR4k3IKSxDsJsGONaHqRZjh3oPxiUecDaPiRiIOyewc0S54240tU1YKCEjfEkD-3F1yDABy76sFu0bo12KfE_GhK1PVyEI8_CeumSHwofUV4CP5gJ94jwfqZAf5s8xahp1WcCC3YY_9fUkz5opJP7C1qTBzf8dYHgwmunuKM6NdjVWuLX-dlpHq6qsbb7Hm5Rm2ntxkYaNa8CLpD02TeL_yFzkvOezJ54Ean-H1-UFouNKTh4-CMd4GvsN1zBE-ZZ8JzcS6dVkDy7lRnM6HuAa8884cpRWf3-x5cwJmcbKlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26963" target="_blank">📅 21:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26962">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbgVO-znr2-E0VqSA4KErGpsdA1hoTm5fmhZLVrJyDGRFiryDkuAvRgSrmVZOkF1AOLlURhacxWzvRTtzZfWIVLFc0vvqPtHpxxllK0doYIgA96BaxY3pUX3oJDmiaB5yyefbFxy0ZpJe3ERMkhM-rofLDDbGHbq7bdFib6YXNbrMI3lGPN4alIbawA2aKRlbbIDtLfU9jY5vt3MFeABq5e4dEukcviDJ-e2KSf5V-i6CptmyTZi1b65yeOWmvvV2bLpID3tDta-J29Y2UbQ8ep5iZ1f66hk9D6-fV0F6E_VF7Tvr8voY3P6FyrcW0Jaiv7cTxdAFy2Sh3iewYUk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26962" target="_blank">📅 21:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26961">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipQ5ITNIWNnV_Uj4I87G2SFjoNbIB41kffpZM8qXPaHxNF6OJF9o0Tgvc2NTvDkjxPxmqCkLup9z5v4zZj35gzy1AuGhAWnh1QQfmvKLHcIOwVLyutmzmwC0rCr9blDK78k0qtgTG00rPACxh8xiD3dxKKre6A3jctprVeOgz6TPztwME-B28K421HeUbLW8Ysl4yFch-2pFLAPGpdvyapebhpzoTd3a_BoeNS63iLvY43OQ4Rgh_iKnrLnw3UQVj3WSRV_C2MJZWE1X91EQbLE8mTjiP7_MKTTUVKoXD4oEOSC0PPIppmvNzlBI6O2xS42CEYl8d483CiI_NR8DiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌ های رسانه پرشیانا؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ سنگالی علاقمند به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26961" target="_blank">📅 20:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26960">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOq_1iGhKLHvT5lFEWP3kNvZvlnkMyU99h2e_xui_rJTUYYGWWR_xA_Bre1MJMYdF9Uwzyxj0W4j7Q51yMQGqdLq8UCJqNFARkhKBjtH3DgmAQMapkPhBWL8v2lpwtn1L9Gq9P_PQ_cQXj7PpuVBzkOxTXgGAbqr_GSUXwdtv8KHOrPvckD-7MfvMpPX7jfiweHQXmx_Dh5tB0hECeIRAdoaFQ4sBmKyBnBi9Uhir0_00-t-ZRx7xGitHfOsPDCvqzYxVn_6wXhDGuBOaAUiKf4x8n_r-HYZXl16u4ESf4v1q1P45n3ytqt-D65MWIxvIwGNzu4HEITAKLm2QkAJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26960" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26959">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
موبایل سامسونگ A26  پنجشنبه 52 میلیون بود و امروز شده 87 میلیون! فقط در عرض 2 روز، 35 میلیون گرون شده!
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26959" target="_blank">📅 20:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26958">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=GLiFGNdzi-ogH9TrFru1o-zv6lBUQaEF1x8QZg5of9iZ611YAp7aDJqBL8ndwg4PYzgzDrQbSkM6FdtkIbPLWabQXEmz921bmzaCgJWGWc6bxRYq05udMv5IrF9d6eiJs7gXTcNlYk5XOgGQcBqpiMoA8TBwYgLJ1nEkyfMnBMdgwSxI3ufTj3fa_W2t0nSC4iR-0xnUH3_b8rKV69wlzU0nGFpvr59dFFkbx1njp334Jw_sGRvLOXM4-nC9D-lJqiCOVf_UmPBS-anPWPJTUkpzUjI9HyczPkxvNKZb0WaK_EDYRjQY0hZy1vOXe7MOdYRqqMcwux_FW2rtNGEKwn9aXXv2mD5UDmd-DxWh1AyEnsAirbLvvwUi18vhL0ilAQw0eELpeyTDF_92wxO-ZuqiLEiwTg7CMLeqQraOIe62_kTClxVwzboAaSCyiq4qznGvHtf_zcaSbI8JKpw8OEa1AbhUg-3BhlH2YH95HWiIPFvCwXfs0-9o9Mp45G8lVr8QAhwctSHEED_dAMoiZgXJT_-f7hJvIT4gRAo-JmvqBiCZsUafOpUB76E-YNoEb-i4ODNgs_wIZmCoP5hG6cmaV53acL943LutbYtIaJ85yXYkhIW6gdK-c-Mx5zytodbToMSad3kNQetbu3iHEKDQVlWjhjIJYxatwQnQtbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=GLiFGNdzi-ogH9TrFru1o-zv6lBUQaEF1x8QZg5of9iZ611YAp7aDJqBL8ndwg4PYzgzDrQbSkM6FdtkIbPLWabQXEmz921bmzaCgJWGWc6bxRYq05udMv5IrF9d6eiJs7gXTcNlYk5XOgGQcBqpiMoA8TBwYgLJ1nEkyfMnBMdgwSxI3ufTj3fa_W2t0nSC4iR-0xnUH3_b8rKV69wlzU0nGFpvr59dFFkbx1njp334Jw_sGRvLOXM4-nC9D-lJqiCOVf_UmPBS-anPWPJTUkpzUjI9HyczPkxvNKZb0WaK_EDYRjQY0hZy1vOXe7MOdYRqqMcwux_FW2rtNGEKwn9aXXv2mD5UDmd-DxWh1AyEnsAirbLvvwUi18vhL0ilAQw0eELpeyTDF_92wxO-ZuqiLEiwTg7CMLeqQraOIe62_kTClxVwzboAaSCyiq4qznGvHtf_zcaSbI8JKpw8OEa1AbhUg-3BhlH2YH95HWiIPFvCwXfs0-9o9Mp45G8lVr8QAhwctSHEED_dAMoiZgXJT_-f7hJvIT4gRAo-JmvqBiCZsUafOpUB76E-YNoEb-i4ODNgs_wIZmCoP5hG6cmaV53acL943LutbYtIaJ85yXYkhIW6gdK-c-Mx5zytodbToMSad3kNQetbu3iHEKDQVlWjhjIJYxatwQnQtbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
پوستر رسمی باشگاه لخ پوزنان لهستان برای اللهیار صیادمنش مهاجم جدید و 24 ساله این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26958" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26957">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsnaj5aszU3Qv6imQztKtUejr7ZOLkHmVq7Z5zQ1E8n_Nr-z8W9mP3gVnPq2u6wspR1lP0_4ZjE2UGt3wt0aqF6jl0EsnRZjo08UVxrC8U59fBISdE_1SSOHjwNvuzFZOChBFYoQLeC_EiJWFo6CpZAJWq9o3BhvSXkpJ5zFVur_HMtXurq3LDA0GXaFrZS1R32qUkHdEN6lKD7KxEGV-gQG4-AkE0XF5Q8AFn9QRzj_4KALz9pMn_WxplHxWMZkJ61GLJsmXFLhIcPS06a4hXUQAkSQcFpSiZL_h9HaYgdX8r6RICNCum37HQ1ZLPHN_WYzosWOnw-xTYxHbGhEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26957" target="_blank">📅 20:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26955">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfDErY7x4m8eplMUlbzvYbhkuHilawZnr1pGjNkeXpGu0BG_tfPIObaewToDkbNSKIu4m2meL1WUBIlqEKdSxZbAA9kVPqVU1iAclnIsHv9rUF-rrzN8H6WJYfcbH22vJy-U3akdSkmwN3Xr1jp_P_3ik1LSNUa6Kggbwvqt5yhGh1Y9BVwDL72TMUGupN-2JFkMgwoZaLgC2b1VD8bi0CwaQxNYxVfkku2TtrkeOH4rZZEhLkcZfsoyaX4Z162tv8dPXtH_pJ2SOicsdeQBhjlT-DN-lZ9drmSOzR39Jh0k9ZWFq3cSVJR5x3BftuHO6j5LS-wxisYmUIyqy06eNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCnLKJ6dzrNWYcaYIG5q2nYcUiOS46An4ktx-25VYySRf4SlsEZr4yn95uHgnF-GH9k0bXHzFS4l6YCzj9Vx51ogxBVGQws-C-5AAyMB7dS-jTEAH8xKA3W8-HqtJWOo5aguIpreMaCPteAHWWusN0JlVCG_9hayqcBkhygX5HzgY9XZqwINLOBTE_sCoS-T9Hk0HFxTqRBt5sxkgts6_8jPjPQVz8TkqPWlTuLpnZK3hweRHTH_WxJ3xK05Dqs8VCFUsOiHnvdrrYypV3IdVHniCQWfsczFKL0QHfQJhUCA-Tzg2ef-XN3rsQ1zDA_nPDTLVA0uLPu3l5H_RrTC2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📍
برسی تموم اپراتور های اینترنت در ایران. این‌‌ پست‌رو ذخیره‌کن و برای دوستات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26955" target="_blank">📅 19:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26954">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-dEmR23PYm_wC-hGhFGDTVa3ovmMQKrLTznYxRCjETZL4lauEMyT8W6aePt9yT-TzyzNw6cZYBVaVp4Xs6c6NqHYChjR3es_EdMiuK3wAVstL2rDRJTiUGzPqUUGKh0fJWt_57vmoepiBGqTAjpDrEAA1V0hHYlhmSsBEt1Khn2rh8GqtHD97v8WgGpGMsQDa-UALKnOa30HnWHe7D-KfRoarYFAT_MzR3E6R6qP5Z1ZnnQ9O7bcscuf_adCu_NmXNRw5ARYyxkqK4OmfHqW4lxlePW4XFGloTymMYPSiKEYsPJL7s5M8LWQ-HVquAB43VyfC4NXOKM06PjfI4PFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26954" target="_blank">📅 19:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26953">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMD5MdQ7XIuCJrBrlLFagx76psu_i9F7Rap1Z7uRGfyQYyFlfe5MA-ByjX1XjXN5aB12XmAig_sErkNspN9Q59c0UOcHjmzt3ack-96pMYGbuGLhX_IHx7oxSe4kGuUkCMAaJXPm2WMEHaSlp5ZmtxUtTTqtNDH2ogQgSO14VaqoL_2b-XoCgvIT-gg_sA7AsMBv61pvktarRgPTY3R_P-OarJqdrXP99pfz7VCakAnJY0nAP8OJY2FMARPSteaLemcdXPExunSczTUP85GEVTamAifbX8aWIEPE2dpcV7TJh6fYWwe7EKzbJtcgh3safbNLzU08zYuKNEpjBlo4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26953" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26952">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26952" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26951">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbUwnAscmcO_b8ea0OXyH0-xnoQK-llRi4FmK8yoPeeA0oZdplN2UcBSgqFGEBmgBj1HMuG7irczTukl95DKUoYSIqJORBZe82sQWUYoKjFqgP3rBpzqO_fUREpY04Cm4h_nfpRFUr6tV9KywLqdQvklcNFJLi8lLi-fa6V-srCnBlHpjj-A5gQNckzS4ceyeh_5Qz5VHiLCKkskQEozceeA4071INcHL4KCWAoAB6zpf3OeX5xAw4csOdALbzuYkIde-qbN_tbNgvLSigJ_dAXxPzYvaTPu70Fl3Z4o91QswZNANTC-0o691rqt3P8yOKzWLcLy-ApGKFKXbp7HeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26951" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26950">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی بدنی خیره کننده احمدرضا عابدزاده گلر سابق تیم ملی و سرخابی‌ها در سن 60 سالگی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26950" target="_blank">📅 17:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26949">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVNPF5ylIfHw6rRcCHblYkuAx1f4tdqALGOwWz-Pv8SmhtVYmHrggrtcwbx6ag1zMuxZFoYVIL3mvHjH5X9IUDKRNqrqwxrq_GZX_jMeyZUYvfQzmATi2X0F4FtToT09G4D5oDzyKehXww3uV5ogHFU2q77wD_gHMACMXveVaNkAZMKNVFbkdDC_lf6GTghalY2qdVSD_ZWjfJnnHgE1VaNEnelZPD1ggXC324BxqiilGr7dGz_aS_pv4shgdxEZQLAHlmfDyB5hiUpfy6Jc-LBz-3ezjuV3XjostusFuISOYqS-whsTfL9mSysDzopvqaUigoZLCBrpvxVQkFajBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26949" target="_blank">📅 17:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26948">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQNhnn6_P5sCQli5uZytMLWxgVap_1t5pt9xfVrUR2OqV3LhONyrXtZT0WvnaJDEqVLb3EVcAvJ3f2WUd2flwP156YvYyGEDj2x8Wmp41dL_CDscDPx6uP3Cfl2a9lg9xD5487lbNfTyl2fxkja0YEbKKo2neOAhpuQ2f_jyfqRpouQJfIJplZwFApVTnQNeICwM3pVit02yFYtKVqB9N4WysFYI_2-Ew5WnzUF05FA_1EL79toJfGJTkFqFQqnKNVvS1wl9Pq9vbtbgwWGqhG4ZWwe_dll3JOOux86l0dIkk6n37aIlpZtPkPrakRjxvogks4dNzWRJnefRPGgvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26948" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26947">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3XPZChWv2TYjxTnrvlhhZuuRH4m1HTX_CuZw12ZFwobKCO41195qaQDpYSiMFPYt0g2fHwQP-QRvTrZlXfy9kVU7wSajBvMRTqTr-HYGdYY_B8AzITX0JsuQ-EvOYYjy5bYSedcPSe0pr5csG8WOjT8NnxskyIoMkBwN4IRZfbFFW16jzHji-fOQXRTEIh6FU8AtTc9rTH7b1d9lZEwGLyL_AGz0tghN0zxSwAyTXgDL-XqW8cLaZtAqOW2kdu1Xh7r5R3UEkezwCoPdmoejbD1Uc9h_U2n-_3dL7L705pM_NZI6g8nK58CcSzaE4vr4kIcJaaI7Cc_ZiMbBrEN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛ اسپورت: PSG این هفته از فران تورس خریدجدیدخود رونمایی خواهد کرد. تورس به لاپورتا اعلام کرده هیچ علاقه‌ای برای موندن در بارسا نداره و میخواد شاگرد پدر زنش در تیم PSG بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26947" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26946">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HytOmBI9-yN24uC31VcJrrFrGH0GQp9D206okleJ2jW8lffkB45ODCMMezOf7bDpRxTbKracbp1yv5oA_NqdyDFQ-GptZDkBGI_AFYbBYSxa2KoS0rC3PWYQUSxlFiB5eGzRq0skqGqm_ThPK0w8GEBB6lXhpGoGO8oTV5ai-yYgk-inhQTD_aVdozwmd-6X8nVP221mEiderNRjDYYrtdTmnjCaldgSUEJS4ifE7dhPqHW3d0PCWiXv4q_Y-iISowIX8-kReKUzCeDBfveXUQiofPiwvIE_r953ri_xz2C0B4A8kBGbDPFiamjh3VUuwI-OdKKUauXkYuKOEyi8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26946" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26945">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vev9AcsSR_XTbQoOUH02RttiuAVPsvEikWkpVai-QUIV-4diZEHXMlI82RwofTZfO-5XqcFPZlKuSEstPuNePXfkKhB_6nMPRYM4hVCIKcMLe2vuVqGAeo_n2V3eV3wM__EiieOFm6A8D0LTheZMQ9sm9VMHDuJVqqTj54wgJ0Tm82CHWecbkHBWvmJPXFbFbvuEK5e5rYKwJqgnZXjxDbMp7jur6irm-4PApAZSfKw0h3ns0I9xfvxkrAo6xMOijtIBvVs1-8cAN8lh2uIlPl5v9UooyYolrZ0b1uBPKNGU0IyvYbjYfDmikFZ2inx6PyT9sdP-TmOqXrMKQ5JM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26945" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26944">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSCyDKaxOarI0GZaK4-PJx9Rz-xiuQ4BSqsi9lks1TefYoPqXKimRKuRyYvOcQu__5LAsoJ5jpI1ZKPi3OPr2OUKbCncY0ZvsXvo-GFqlU67-Z1sttEoHANHhwjx_M5swY8IFoiDVGikyfjIHyMdctw2DTjhSPsL6yHNcuuNt1wowTWe42FplNGWEuMxs0FRmV7i8LiHxthOwO8GYWvnjJCaw8NmC-GfQUEAg3ZWVm7qMYwn59mBbfMbI6rJIAN19im7UNFWz24Rj8R47xcnu4lwQhmLFaj_cXtpVMhwJmPm7rPdfBi5WO0Jq-hQP48uUclMtgNcBP3fH5bCvMcydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های‌رسانه پرشیانا؛ فردا جلسه‌ای مهم بین‌مدیران‌دوباشگاه خیبر خرم آباد و استقلال بر سرانتقال‌مهدی‌گودرزی و مسعود محبی برگزار خواهد شد. مدیریت استقلال به این بازیکن اعلام کرده که با ماقرارداد ببندید و تا نیم فصل در تیم خیبر بمونید. قراره فردا تکلیف…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26944" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26942">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSbXVg47Al8IkjRVuX64CUtBIT_UmUi1Y6v4lRA3KsdyCvg5LbdPOichGJhVK4G1kwovVb-3TdFV3GKwea0sHMyGJO2hDEVZjSaY_bKj5RUZGYWtki5wzsGhHi9ic85U58arGBuIFguwvQgC27M49W8ckzDg5YrvNlKhApY5N4r1GIGz-h0-MNOECYn1cA3cpjb2nzIwKdDbFSHijcrxc9uYl6hDbY0jM6cPyBa-HePahHbx8dwfmjQAnyxIanbuPO2zxkHyiX3moahfhFN6SXNR9-AL5UtJ20ipHagGtjas6cozYoodkiO4SeZgYYxEcL_57aRHoxejW_YX3j4NYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26942" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26941">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن…</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26941" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26939">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5Kye87fZZaI48VlwD6ZHR2zbbQjH0rOZCI4xs549sG7AkwhnHMj7eJcaMOaKruKheYo2VZj_kRIi0SWRTCBFoVbxWEuihDoi7EFHF1TfLfOEuz0iV1781NgptsqYu9eu2jyZL1RNEbTtG9-SBEj007ZzTa-EG3eTGCEHB4nMpR4uKbsYeq4VNYOR_NzHS7GX2On6kg_Sz7_5LvOa4E3WWsWbsOfhFMKKovXFVnqimJRAJudMEq8AO48jRGH-AyB7-9GD1x5nGUenZCYXoRXdNzshYouvX2B4PEN-vdRXeXaY3PGtQWdLK_odKygrtcpQ87b59SFsyezBo7AHfDsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kojPwKPGswjunlkauR1LyJpQSHY859fod9vDP5utZPb4jsSGEGdPSEf0ylJuFIqkXzet87s17JbV0_vNGzl6beWAkrMYFsaqJf6fXx6hfHhurnBTxxK7Fh1WYJiJWHaEU_eWg6-uV_t2wyh6pwi8K-E2DEUUNqVcrge3CKUBzpOY5b03plUYUg6fO7QXz9pOY1Vx03pBdvtXovTWQxQPGux1fh4ema3x5uvosmUugoE7vkX5vY2p938CkKuDKmFikpvELhFdPJ4Nxb-uaMBYd78aaLHbAStHIUjgBdKiffPnst6tCts1oDETLxzY8W0NQkuwaQRmY_n-iiaKmjSpww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26939" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26938">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5mbmXMmvWGHxKi0E1RKzwlktpyCZUVOnHytEF4ToBD3jHUsi-IjCnKvYz3Pi5ysD4xruDieD29fTXKIwKGyJ-NKWBkn9nFtWXGvBs7XchA8alvlV_GihrON545R229R4H8otF7zxBCIt11HakJeXRo-r-D1VgD3m9_GfGufuir81VyZfsAQ7mlY98T8kLkSTtEiQdu0dE5UzjAX15cAy3t1ZyEx_3TRGp-oC4R0xwS5JTzUbulArT8AD2KD94kWuR-MLHg0kS8lFMOnVBqu3xrji4g-XXAxoDMZzWh-Hrr7nn1AYwA_783fW79YALlmLcmmMfFOA4CnizlmU6ReGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پست معنادار و تامل‌برانگیز رسانه رسمی باشگاه خیبر خرم آباد با استفاده از اعداد تاریخی 18 و 19
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/persiana_Soccer/26938" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26937">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلیامیپرسن‌دارایی محمدرضا زنوزی چقدره که هرچی خرج میکنه تموم نمیشه. این ویدیو رو ببینید متوجه میشید. امکان کز خوردن پشماتونم هست.
‼️
طبق‌گفته‌خطیبی؛ زنوزی قبل از تراکتور خواسته بود استقلال رو بخره که سلطانی‌فر بهش نداده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/persiana_Soccer/26937" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26936">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eezm3_wEa5GiZ-Uosk4dh8Ymk-tN4y2sAOhlVpe6Kyo6hs-byj9DyeFjPA8CeW9lqbC1emk2W0uTktiox5AQlvQgPj0kpB4O9_9g5O24tVB51pDFRrZP9NukewHzQk-DmCC4eEcRAtfKIMOpFq2CYATvwkPVslz9s_6p2bUtZrLJf3kQZFFJpdsyA3iWK9C9g1-ngfzFUhSstI8VuBCWAy03qJTDWHmcbewgUOsYxvPy5jvVyBN0aXxK-LvAvyOt9z3yr4Gd0rkEkTq8-damWQghTI82eBEAUxBWijb9udrc1FLcIeKeZB_QxYM35maLnnHIT9FGFbVu381DiL2Gyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/26936" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26935">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYgq0drOC_FPZJudLX6tn36gsb5_-G0t5uCaog-BbzngD2_XI2Nwm7m-LaHhe8B4B7vKZCZjVWWkaW_4IRH-4VQy6rzSuusccKx_3DH_3ExHCUChiLHQ3nYb_Pm3ARAEsNTB6TWNbKJnh98jqv1wc4GX0IB42-bhc_xbRh6P-poe0TNb_qh2u0lEvGEa4VV_0A5XOHcbbiJBo92oMrIY4ZvOvqYzEJlTFAFTVOIfi1_9MASysw4oM2M7Yx-lGLq1CHxLRJ5kRJcjFjST05GxTmvQLyTkAebQRiWpe7jhsKmATvc9B5202tLnh3uV44_1aEhlGL0CRD8rX2eeprxWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/persiana_Soccer/26935" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26934">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0a57Uya4TlkNos1NqnnG8B4RzA68Wy-hYRMk68jgtwVhd-2ggs9CN7EKBC41UbDrKVsHK_hkeW6SF82lc6MFzM0V91Gd3QXdV8ljhMaMfz1tuXrMfl19UQe_GObNzxR6ZmG_CAhp6DkcwO34e102bBkjvSHmdyXne2SBeJ-mxJQtmXSChDNuPhUnVKpaVyLk2ZszdXPFyZqX8ROVRWEf6BKHslaEo0vtopoi8oHXE1HfZDZvxnZMuCIf4A7uTUwiENnhl_1XmaeRdr8R8kQwPNE7gnOeQOoe-70KRDcJkFa-UlMWUNMe61__EgOQR4OgyR1b4VHdMg24_tZLllmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/persiana_Soccer/26934" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26933">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5gxYw8DFPf-pLB3RwsV6zCQB6qLhgEKgAbmcGjg_go-7jW6SFs7qZf7T0_spHQci6UvEY5VlfOxwB_yzOCAoTcBVAMQf7wl8MbDoInOcuM4tN2VzgnyED2_OaHZ1wDBpqzNHca5feUi2ACw_qal2lC8LTVvvuDfNkw5EWf_Ira7jTWllFrjn9mv30eXvUBXCHaW-fwPEsSJVLp1DAOrkPPwNtN9N4eJje8TpZlXTSIN4jtZ4ge7GvgYsKPliT0J7wd5dZvqgVrdCQ5Srb4kS6mSZ6kXu1FnD6V_dFTEJhbjXFKhU2JAMv3FCTk3Sm2yuKRJgTd2-taARYN69mbRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/persiana_Soccer/26933" target="_blank">📅 13:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26932">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq_nTPtigzcTF_Bi5BBoJmb5YAxWL2oxitJmcvbO8uKOnqkj_ArYicPox6wdmeOVOkq2c3SUXZw4uEPqgG5wD8kMF8KWCz9P7pUa3Hin9wxSkig12D0oHSoWPq_a_M1NRENgS4INfMWRrLmKQM2U-XX7i3bheztSHv1j6v2XK8sQ58xQync4GDYBicYcWIGTqg5TDgV6YB_NezUXgcWX0ladpoFoi4U5jofXriB2ApMtHSqSuSrnSMBFh7-5XNG2oIFEI2qFNDBjUE-2pYWgnMgdb7eAacULc7AjcD9AXlzXaxcw3fnQaVgimHZlPqT0DiZnJ34EFY2y57TNJjmJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله تیم ماخاچ قلعه روسیه پیشنهاد تراکتور رو در رورهای اخیر رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/persiana_Soccer/26932" target="_blank">📅 12:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26931">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcHQeIfzsaOA4DvJ5B1u4jFbcBzezLahXc8BsAImFHIvbFufNN1A7fMEqMXb5lz14P8nEm7p9yxvLza96DKegLhncBIEzxmPETNj16A_n6eO9b_NcximpyDl7du659B2-WmjJZdoqWCQ7WeWox9Er_ymy4MzAZeeh4b2QiQQHRBYQLhKJ2V7Ro6bICBVwHJWJkljY67znirQd3rd-KXA407uunrYogSU4i7mixxHvuLx4N5iu2Iwy40qA3hTUXM-UKlBZbWG7O6s23S97pyUE2BSnOJwOdVw0LAC2mcMp5ND5hc2NamA2YdYvPHxUgS7mdMzsZO-M5JcZ6TN9cbghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
نشریهESPN:فلورنتینو پرز قصدداره درآمد باشگاه رئال مادرید در این پنجره رو به 400 میلیون یورو برسونه. تا حالا 200 میلیون یورو بابت فروش بازیکنان‌آکادمی درآمد داشته و به‌سران آرسنال گفته اگه‌وینیسیوس‌جونیور رو میخوایدباید 200 میلیون یورو هزینه کنید. اگه توپچی…</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/persiana_Soccer/26931" target="_blank">📅 12:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26929">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cupPuKfqFkJNNGTPDruIv9JkNCa3Plg199XF9_ukvZVsHsR94p8Uwra-p_j8j81RCDhdQi3G46BnUvzeLJ8wUojBmwTiVdS618XuvnATy0MY6FBkPqbv4M9CbLO5kUlQwmMPkhZOfnKpqDnvz4GNuO2y-2tzKnRBS9nIkSR91YgbB-MGImq6L3XyHSg-77B3URjyR_4kx1fBtMp_vUqcBKweDuUmTXYTmn41vg9MpBbLS_emG-tAyftiT9geEICwCjafmV7ycChuqYpsKNyaj1wONLzUbjOvQXej-1WgU-AdcuFx-Y2TT8D3iULPyV7AyK8bvgBG84alKzqZdMwMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFcKyEByPvrUGAXrqyA-f2Hhg9dFyC8lVTVv2Sv9UbJ3JgnFaTooHZdRkjLI6d5zRabv0AP0HAUQJydoaUdfb7ztBXBAabPgsC8bOVy-Uqi4osxsEHXmGNQmiW8DGML3Mf87Ms2UjTzheDbIyTaFpdxI1MraYw-K1iwCaWLHXAcnEigId1aqFLq2eJbZNDvJaoW3ReBLKu67UNNO8rg2RU_Q_AE-fhCQw5s2pl8M81HIHXKwZ_ySrG_L8BslKD3G0GrQk0GfAGrR2Xm3WVejjn4aVVP7FosxAfQa0vLDsCnZ4so_Ts0xhSBucb9f06nqmoGxKlfW6wGcmdt1o_edGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لیست کامل ورودی‌وخروجی‌های دو تیم رئال مادرید و بارسلونا دراین پنجره تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26929" target="_blank">📅 12:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26928">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0eEmL5r0qCN8Ne4WHQGj8utcTq19IyqEJqUX4E5pxcC4dqh7bOGGdHkd_4nGTlf9JVq9W2QjBDT-AknBtn7Wrs7TKSgKbxGSulXvh26X9oHbw_X60q_8yC04oK_PA-PM8NOjQypyluTYCQ9m2GOWEbMyLYgAkYCA0egTmx1Jh-Dh12S4wrgNrFcGBUAevT1A9DhNGgGk-6bGA2Eti7JlBHZWwEagEiwbqaavKqNNtuFAH4Uslu5JVyDvqtlwdRY25JdleSMi7eLnmJmD_GpD80MVFY_ZRxUlRFoTmbSMMeCso-uOkWsm3CiUQjAS_VnR9kLfiHanpfH_LVEbfPLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26928" target="_blank">📅 11:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26927">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26927" target="_blank">📅 11:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26926">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U620xkxK98PnOB0J6PXDHbjdBwE7skXRJeeWcEzl82KxAOiXbi8T3g18Y66wPetkMNsa0WgHTmHdzvzPSIjZX4tR8ZXjHGL4TP2g2fF-2VWJlFJ0eDQHdKqCNHDlkprSa9Au3RdRVMuZYewL6TgYsJsSUg7t9qb9yHgeMzJ5JogL9gIdZFSBttl7GR_N4OXgDBVvKkEZD84UY3Qzz5AFmdx5rVFwEe1XS6IxFF3XTsjUPlIWw_UvaXOfY0_4B43jRxrNIGxHqnJFz5ZZvqWDjniLI4RVhYfRAWNbJhtzBWhsFOQk-4VBjLtpViEbQjJFCWSWB7pdczBVf3Jb5WrTVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
زندگی رو لامین یامال 19 ساله میکنه که تو این‌سن جام جهانی برده، تو تیم بارسلونا بازی میکنه، حقوق بالا داره و صبح تا شب با دوست دخترشه نه جوون بدبخت ایرانی که از بعد هجده سالگی باید به فکر سربازی و کار و قسط و کوفت و زهرمار باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26926" target="_blank">📅 11:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26925">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIeqjoGiiFEnmJWtXrp0KbBmMTGNcClGTzlvKskxvERDEaaF37u-q-4kBYTy9IZkWl-06YMM5CcCi-pKll2F4w-aFcrjt1DIj3B13oJEdOcaL4yZp3i9gQFfbevjbHK-VgU0w4D2Ls7i16tUyxrevz1dRUAmrw6IklfTO1L5g7k4arr4zQjpUcz2Clj7BdfjNIoumHQIzZIupkPIlYuY-2bxPm8LeSYzUvdKf77ghmitd2t0KYEwc4aWbQuGFTnGGn07dGzLnlejdH3H2xCB0LogqZRjwHGubLGqN16KtGM6E7xJIoMcGya-XqsTnZ-Fzc5If64bz0pwntVZZ2tQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛
با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26925" target="_blank">📅 11:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26924">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEvWIc3lWZkVj49QDVIn1MxBHbtamWfaRWsFQdOrm4Pt86HKhkaOOkCgb_Llf5LLqDWpsN9ohJcI1hvialhFoaU7xELB2RLB3NOspS1MccV6OW1pjqAamjcPaI7EG8wBEmia2eBS9F_Ec4R7tsv9oQhb8ISl8dRmZCNN7rcrO1RCSfMwAshR1sC0yG3XDKZtGl8klud8_cr1XcTJVGrDeuy26fdvI26mihQiTaZyEMpAHCkwS4USHmOS0eXKskv05HgGsxOcSgoyuWisR3zNVksNEmpfSZ2I-Yom9UUvr5ZVrqy_q5KEQE_OyoET2ILJ2NDLLc41N7y-bIVKNRiKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26924" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26923">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRByRPiYCPE68GiKq2CrPHMV74O8QK-QmW-4oPcm1n845h0Dqma7xIuW7m8xhrMSsHiyn6bC39qrZmmTr-tVZWYdnQTXHZ_8nLHuTdsBLfT1CH36XTftIQjcUdFmrUvjXngLhWLwsNfoX7jaAsBBQjSWken64bX8LtM4oNdXp5VyfV0_CYN0DTZQ-jCnw5dfpmfNx5C6IGuobLna_mVArOoT-1j7dpfyHTXSV-uqatGQXMl0dZwtfFltPEZbWWJ71Fm48aYeiOGkCbaEVzY3AdS6jWwbgygbwZh5WGLWmGosszvHHMFoCSvdfv9PUfbp4pvcFn83_F81rKv5dDg3M_NMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRByRPiYCPE68GiKq2CrPHMV74O8QK-QmW-4oPcm1n845h0Dqma7xIuW7m8xhrMSsHiyn6bC39qrZmmTr-tVZWYdnQTXHZ_8nLHuTdsBLfT1CH36XTftIQjcUdFmrUvjXngLhWLwsNfoX7jaAsBBQjSWken64bX8LtM4oNdXp5VyfV0_CYN0DTZQ-jCnw5dfpmfNx5C6IGuobLna_mVArOoT-1j7dpfyHTXSV-uqatGQXMl0dZwtfFltPEZbWWJ71Fm48aYeiOGkCbaEVzY3AdS6jWwbgygbwZh5WGLWmGosszvHHMFoCSvdfv9PUfbp4pvcFn83_F81rKv5dDg3M_NMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
چند تا از شوت های روبرتو کارلوس رو ببینید، زمانی که فوتبال از کسب و کار و پول دور بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26923" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26922">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja3SMauFUpFAw7hPyiHz2Cpmu9H4dCvmsxnea7-GRCFnw3oGxKmfk8XJVP5ckWuY4wk3_d4iSsTq5miEZDbew3IrGOp6FH0nZe34ezQOf7JmwWcU_oGLd8elgSWrEivjbY4shLSU20nY1ZrFs4iqKWOOSyTzKIzCRMSxx4KdkuiMBOMTtouYE2f62I-aWgmQ3GuHrWcr-DUhzxM9jjujDt6B9YlBKXjnEVDgQYvLmzVNF69EJq9zQeMh2VfuaBFXrC1BvyNb1phJ1JS2OGGqLZghkZM77Ugiw0WVMKaBIf1y7FjbWq_esvnSdkjcrZY048Nlbg2obprneAlCwm-smQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26922" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26921">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM1dyE_y1egN25fxHERYoeDPy0Us2WUEFvcGY3gnd1Ly0DW7UjDUgZ2p10YxlrbuX7VJ3Og_MeB3XQzABApnvKGX5U7C5P7Ouku-FNgWf9SAc-ACrSq4Ssxsxg574SPlFweWGzpdiL5gm9c8VjHyGXagJbAb6OGkKjMnsleQplwVXqk5js755QEk6QyEcIoz4e0sls60AkYZFU805EeOcmnU5P9j_OtWxeRwnnMozRVxaNeLP65FIUkXwY2Sohp2C2zS7jtDk5YR66jwaTK7At_3M1Cvsl7fPIzrdjdkgQzOmKOpBtuaowNYXGsFZT9blcFHkei-YQu7SK--63inlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیس یایسله سرمربی 38 ساله الاهلی‌که فصل گذشته این‌تیم به‌دومین قهرمانی آسیایی خود رساند باعقد قراردادی چهار ساله به تیم نیوکاسل پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26921" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26920">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Zpg8pOV5TqamFwASssBaZddOD6FZi6KzghcTclNIPPCm4NTA8Xbpr_x_Qi25Q5j1nypx9MNrI1GXKTfhqJ7bP_aUdZIrA5w34kh6wH0YWOh-82NuT35RL3AUU-41WO6c9AYPGIL0HJvDaizCu7QBweOT-PlpkkBh3XWV92xr0ItDiA846nkOMjbh1dwDV_0l7CRWICI59f2wzlkeTSU7Sm8p9yHyYU1EOkfsmsi-eGmVCRDjdSne5Nugde9ccScmtg84JJ7TznB0K2lXg3olyJ7lXLlGunEw_eiQyqAJF-6iqIlyfgNuHAbN5vJ9S8r4nhyIFwg6khFAhjTYZ4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26920" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26918">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zgu25g1-ecNCwjsuYrEp3htU_F9w_MZ1RC86BvYfJ4fsVXDxDbyJ57rtlX_jQZVrbWFig4CXUGNAIIXIQYal79tYdKSYLIlJ31v8lznlczuEIfzO4s94yAgkLkJhZ7tEEmpEpliLXnVFp_e0V_oYSPspgzVctBDr68u5UqOlFh1zGcBmr2pOXQ1vSuAPH6Elw5QKpXw8DK9ASvvzQYIZyGIgNpTK3sXopQZwjAjFg4gugHpty1wOOZNXhv23DmQsGphnl-8fvdaNBEvcK46HRpWbMhODTtDsB0tJIkZdmWgMtpyI7HX7uhTQiFekBLqmt72oFWUqGBN0VR6bYnyQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
رسانه‌های‌یونانی: تصمیم‌باشگاه المپیاکوس برای فروش مهدی طارمی قطعیه. سران المپیاکوس برای فروش مهاجم 34 ساله خود رقمی بین 1 الی 1.5 میلیون یورو تقاضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/26918" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26917">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR8TSjb9yMOcDIsGyWOi5LYlD-7g-wZYbzzsvOOc3wgUJKhPtVX6dfce_0RyCOU4IXGp6pY2pJyrt0odzUXbI52izzjX7Cq4Xoc00rei6RJBflQAsD5WLRP-SMiWmTSRa5V9uu7LSiBmQFFZFH4PbQdtgp1Xk7MbhX7Qo9nBJfRbF9TTmEhQcR9b6Je4ShH968AHS69S0_3alnEVJs1qaBI5-uWR7NXvGUAY5WnpH9yxnGbrtdN5mD2pmjklekB8nak5a9-ubQrivSNBXHXqtQF46W5DjpuSBJvDzs41Hn6H4aWshLoJ6sXOJZRJ84sKfIefPui4BIin5N_qIPBs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شامیل گازیزوف مدیرعامل‌باشگاه دینامو ماخاچ‌ قلعه در گفت‌وگو با RB Sport: سه پیشنهاد خارجی برای حسین نژاد به‌دست ما رسیده اما ارقام پیشنهاد شده کمتر از رقم مدنظر باشگاه ماست. سیاست تیم ماخاچ قلعه فروش این‌ستاره‌جوان با بالاترین رقمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26917" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26915">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWzfaC1z51Cf5qM4mGQZGjeUgzkeNkOWBsgumtiSNyfTprMD9kOFithwvrx9e1kKmYEFsb1B3ebDG8GXEbi1EMTS1Vsu3zcqhLwAAWDtP9cYeSay4IUKQoi2JjTFeSQ-Aehb3LWs-PNhZfNSrnI6r_IHcM9KWEE-6Lsej0aXZVoyhXmuXoSJ3vlj4PF4ZtVvByJieEywq_uOu0OPguuwJ-_ODuhpMQ9wA_XrKJWQG5zdbpO_64VGXF6KZqT4rb7I9F1c2Xvp4Cbf90C7khe2OOXqPiX08Ff_EKhq9Eciv_9isDqphWzY6K367bIMUORat7s-Q55xQexVKxp687Bd2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26915" target="_blank">📅 01:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqRfaHRe11c8832Gy1HdgvsIkR9cgsB5q4N_7MZM0qLtZ21KlwnNkhYFgh2o_CzTQNo0D4hVbJ1w8YGtiXhiBhAkCEnob-Sv5FjMDLHCIWRnvSSfu0sog6XMHebBUFjWDmvne0aUJMops8v7lOH-gF06yRNmHVl8HOQf0SwvlQvgoP42CzeCz5ih3Av_-fOr4jqWRbFmjLz0lRE58bfqBohO4TItocW0CbKh1uZZQshVYlUqSPd-2zy2eefZHZYYyMcnMHlFErKUb85_Fsm3nk6ooafvsgU99UUPQNT8yJv5s75KyAn6Au3Ey-Y-C-hbOXd-hJhfZmDdksPa9Y0A9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
بردشاگردان اسپالتی مقابل تیم فرانسوی و شکست کاتالان‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26914" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxY6jLyyOL_pfKvhlF2KYy1AA40VBmc5N-0GlZv2RvFDfiD4M9AtvRw-pZpcbVj-XSzdGmR8fzYHHvg3Vw2lAbySNA9jkN3bUKL0XHNirE9XmLMcF9SovOge3oy494vQ-cjosB8F7u2xSNognuoTw4uwc6aAMlkGfgxbivgjQrKTReKZlcEPyinzXzWyrTBpPbqElP-B578WKexZYramOEFN4AJJWOLnhT6vHbBgBaDhB1sV_pWGJhxhmIu_M-W1XREnHINIxdllpqEltmufkCx9mvK9WYk6rPchuIUgSfW7NaSp6uxD2fGrMpHTsVa6LC8IOcSCwk36AIhHStiKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nnw6bstDLjfO5VyvpB0hnW9dPtSZnmdqIzPRBv5TxIAbmT__5CQmC0i9qEopH3qkovtnpFEumzTkoAHnOGl50s8iCGZs-1Zbl3GNlykjAe5l5Oz_8rGWnhdjBfWvg0RHFrJdr8YW292JMp_QQG19Wsgv3MpRRYujC7zQo7Z3j8Ju4BG6VehnMBFX99Km9G1sMyoqqv_MxGHf7Dap3ux46vPuBK9hjHBiMfivgtezW23EeWvqnfSFFkjCim2sssesb58h4_SuPf3LOBHNrrlXQdZKeJMsXaNjduPKfc9r5AFGYEqOsVt7C6jYckEkjzijgXC8WzqU_xQvdLBFfoIc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJH0ufs-zIGBxgGnhz-roMyW99V8NTDgCQYTClK_nDl9tRT2LChR3dtqJgrwn8soQMNvohFdStvDK6MC7oIh9XBCHeysTywLqEEsLIlnDb9YR3uMsjSiFx1YVEg0fBkFkOdkrjathLeXyJGQbKZdDkMfjNBJ6qXjI7z9loeX6xgl2LPVBf-yRC29Dw3x1H5cjgLgMBfmN0mXk2JO9U_RxlszYFXZpU3YOxzvNaNzjnmL8MxGngIaQVc9HggRbpshvFQFVyMIVAFChbooRg6xh54ys6Kn53FwwT4l8DaGUYxlCVrPNZyYilTMyGf23VmNPzs6pBdfW8tSGTqSC-YBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wltk1L_yg3qYVPWoZeagbhO7g65fH0ln1JgQCEW8-LGVvSvUw20sJlgmlovLRx-fCCRgAmgdEtun6mI8XKUGLtqOdshkt9RHHTJwmsxXQ48Ei2sDExcsS8lZQvADvXnIWpce09f7TdLLxCydgL4sdv1aIIsnFpiw3O_xiOHqdZP7cQUSm1VrTfIJ56kncQOCoFyLyvQVwXrH2ZpK2Pdv6RTL7z80dV--izoCZXV8S8KgOCcJKmuJlr1641bcevADel8CtXpyNnMBMtSRptB5mdomPw2Xag646sI2vUI64QDda2DQ_gl0k_lCpILbQQsCSJR6B-3TQngWSzZX6sbzLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEUuvoJ1Fdup5--MeaLoqZaYzxQJc0Bpyz5wc3Duu4tc0RUJDIF8KLRxmiRpJnIKpXXf3G-futK7cRyaHYh0V1LTmdMtxOeZzMZiIIVkUXjTmKJHLr85UR6H8cNoKGe_vGzQxS4sDQC-A5769yODlKpnTPVL1DC3gb6mM6B2GkO42mrOpb88MqHVlJdcVIKWsxdS63aYYbR9obcEdNpaGzsejdnzVcXN1XtQRKxolSkv9w3gOw_ffpllJY15R3snmyRZO3BiKCxPkxZb01YT-_P6xwQ5YlWg4knnvKcqqiPzLxCPAJi_V6JAb66SVVRXp2PxHBzCuLZj6StF5K16MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0s1tkeCDAbK-m2UnwkwVzlKGraclPm2xmy4XQ_AWF4eLP_U_YIXCvk0MFt5L1tyEymkDXiNXrqwb0khXrW2697V9QBCIXzK_dex0t4xEhmTgvPXmBjNeNkwqXVHgmJEIpLoxURi9Y52w9KMcEot0q2jHzk79CxFW0aFi6OnjLwBsdUu44rtCBLw65lax0g8E0suzPqRuFsHhQniS5ovHPUqwzDdJigRf9TOKyDv1NGyemjbSE3Y0AJm2vznErOO666otUjUukfINTLcanHMjcRz-QQn5-5d8toZ0BtWWoPMiCeTmjphDtrKPPpg_ZjGYoHmlc_4l5PszH5Izocdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrInXMOQK3QwJxzvhWt0CXIctjZcgAB6AAdD1YRn72_dacYwMaQ7Kh1-MIKmhXkuLCo4CJlHY2Plpk6mCqn6VQ7kYRBtltmIqkXkkpbIl_nuqjZSBPg8wlgzLs8hv5eYjs65wS4vuM0TeVQ4mk-nYtL7dOXCUiNoeIwv05279skYOc9JLHG_fkFqKNQTUx3vjJuc5idieAQRAe480CqKuPdvTLDI9zqTfeqCAG93Pxz4YoZ3y5dbQdu5hq5Kn-tkkrOhU-OLcvoHBg1v3Qx1JI3gLGuLdiizGg7F9UHb8PRUrYlkJpHZgocScJS8g87wy8QhZOw8kGHNYIL_RNOwZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXYVvos0PbmF6zlWmSsbswA77OFopoWl7nZEX6lQgdMSaYtnqZByQDPwtXyudevciHiKWFwa4wl6ldspmRm6p1hFbJI3-5RLnm5tInPCSCo7iAFfPWIcymHXllhP3ycWhz8rP35lCWzm962QZONlidLG1umnR3r7Ekrf11VzRShnVBwdGlp4cSZvdJA4jKzOT5C08JhmaVvIr2aEB8PpJ3EtotskD73BRRiW1eEoBfoJfM_ABKlz568BCXv5x-zEguT21-0yVEoOvCNIEH50GU6IjojYxdmXMV8qX_cQ_vcPQR03jL39LXHm4MXvfL0mgYIPiIqt9v2ryirDr8R5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_VJArSAfikIougLxBr93-9hajHvnWn9gDBqX4e9t_t3jS9WaAjRyqkx323dAQM_eLxSLnTzziZUmy4IVq4nyYIQuL16HUm2nm70GaleMDV4CVc_I33L3QjwXWp25RXopJRiCM2YQMlcvdXVSZDokR1nF9uA2IXvQK8ZRC76IyriHhEo0LOHDN9wezEqfsBG1wfY9_OMlz0qrXCnzyl_W1tdbbqpX8K44eYpF4O-gTp7z_Y4yLbZqj7f3yVP8z6dDarXhoB0Ddz-c5c8GWn8LU-nEEKYPul8aBk3-wT4BcV_x3g0tJ-jj2pTE1SXSbqHA74FbWVfNm0kzPGRZZ1X1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNu0qGab4hfDCaycveh_REXuiNH7HHoymhqQyK5l13MU8gb7QAsnT82gM1HJlAapYZjt3_0hZCnFXxn3JCohip7l3uI6hZvNvp3tSpNLB4mK95WfjoL8QhNl9A8WlMUYu6ZynDu-0Octogllf7Z4vin_ca5KTk0jy-kpB7HMwUVbuKcBBT7mAXb9kGQ2g6k9_tAo_03wumsMeQJYDPsrvb29-8zh6UyX2fWQA7TwvrPn_7yur0HqXh-1gcD6jnCmP59IOWCKG6ibhM4hnPZxrHAptj0z6XdirM2Okh6NqXNAZ1zW6ZBdg_eZVaYkHKdsSrkK-RRG--CqtSkIlJeXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX-DK20vwBa9whG9YN-vFuhBjwxF_6kSfgu0Ul4OQsNty7u6dNxCkLOnxGmOUIYXD6YQeejdZJ5q84SArI2KZc8e8uzqtR9AbpGiQrDvhZLDm2RCr4HMMMJM3WIxwDrGuJv_bNjA3lnFi9lbUL0WnDp250fxwl9_bYI04PTQlbvFDTvc4QcqkjRnvxJirn7kDVC41juh-_YQTvSrV-UEIlRsXJiw0Hjf2gsx-7wTOJqQzR2zmA746tinoclRIa6vDmZtgywFxq0ywIVOqBk-w_0t696gguZ2x7Tod42tbtwchOXfJdZX4nMSvx3DOPJZtuZAxQ8XcdZW5dBqVe4maA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFDRKgLsnWDD2c8NsuTNttjjfei4dZyx7OnMUcb2H_7B_bDEzEAFiZNJ3Y-qr6yb5M-xJn62KM79l89BQWb6_ZXFxOEcZwQ-a_AoE_m11Dfg5Si-B-6OZhGjkIJ3i3LkiRhYJIrQ7ds0KNjZezoSdGMMySz9uRDUushYaDrVHjn0zLXo_Yu0Gl9LP90EkspifEQt7hAQA3quyVDntjCI-NqKBO5QsiLKG7_VB6yGWQHTcsrBvWwOOi-6YjysO9zOYAlJ0nKeSo_kpXAkpxk9ie9Ei6TugLtKyTt5hI-E29VJ_qfb9LspTcqs-aF71fByRPkBxlVpTjAPAcsz3j6E1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-z-qmqFxDv6xqmQMDfcO5i1vOb7z1YKOA0Vd_ElNd0K-tC2QDQioM__dokN32LCg2z7gSiLYRguasD-B99lihfIQMdahpryQk2P_vsTvTwcnY2VDzhLRQwpCmzeY8wZVK3X9RZWPIkf1R1chEV8WpLizwi569PoldIuAiHIjcrfQ_mW2fCFsavBe_NVjiNqM95R1BcMQfrON0gCVCsUCSpLejkitoBJSKgMIblRhcxiuUyLwIJRwX4laCcnHIvP6LjgUsDjbzaUttugwLFoyx8CSKbRY03DkFpTLPGVXRNs1mnqrzt77jRN-BoeK00oYQFaKwIvdC8j0H5kglZhPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ovjz_qiznazx-xucGWUEYzMMqbO8dA_6jo41iRBSGCdsKqlRKfOxHWA_AZRePpezItY0o_0wgVY2vMTR_mGhufRDZaGeYrUR6dvodce5PgKyRn46BKWun6Uq7M0lGrFpToGB4f5jm76Qq9SS529RUH_8BFMPwoP-YLkqWMpm8GXZKxw6GS4LgSSgtnOjJvlpHDemapS_YF8gXLeJltSe_nPm_HUnbOodacmUOc8ZDTq_ZtE_TRsQtKyGlPG-6WJEAKJo7pQ4C3NSSTM_1r6WWAmp2lLes6iDjo6TKAKvriqPuLlolpFaxSOE8Fg3C2_ocSdvizqDawFf8vwXfEelnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=A4g8jYy-tegPtDlTud3xCUfrPDOEGU5mfopstEhZM-zSDfA-vMfEo9ofSMt4eOHaFj_H9RsQl14HDCjhdABgZ9P8xrWxLjv7oj3BaKh6o7mmYsVvTneogpHAVKxuX03sq-reJI_6_f4mRtB4ZFwKzETi8-KAAtahfRexrHmctlulL15iBP7UK_hTH-Wof6KyD_rFxwpRC5HY0vReFdC-k9elRLnIweWcnn3j6PxtSC7c9TD6cxRYLbPO-D9Z0THDpQ25skhkEdW9DhU-BQxITVmCLl1GvcMA_H4VUEgEmLP-JzxI5E2jusfIt1luTVa7ppi0Ep86D6rCMIT_RONaGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=A4g8jYy-tegPtDlTud3xCUfrPDOEGU5mfopstEhZM-zSDfA-vMfEo9ofSMt4eOHaFj_H9RsQl14HDCjhdABgZ9P8xrWxLjv7oj3BaKh6o7mmYsVvTneogpHAVKxuX03sq-reJI_6_f4mRtB4ZFwKzETi8-KAAtahfRexrHmctlulL15iBP7UK_hTH-Wof6KyD_rFxwpRC5HY0vReFdC-k9elRLnIweWcnn3j6PxtSC7c9TD6cxRYLbPO-D9Z0THDpQ25skhkEdW9DhU-BQxITVmCLl1GvcMA_H4VUEgEmLP-JzxI5E2jusfIt1luTVa7ppi0Ep86D6rCMIT_RONaGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1QXRQWwulELw6onmNwPfoEsPhToYHHEt1FxGA8K_JspQFAFvz7KqxT9Z2GrrmgTUulzHVlaDFUoPf2Paw__h3-peF5UCGfiSjATnmzQn32RmdfkkK8JyRvyAPPWllPAqJeHadWEVidtj52Wp6zHt6jnpIdmgGKpSXSX3vw3nhaslBGBaKtTFKxAsUKq9aviHFtAd4SSPep5zaD2P8W-kU2rrYw21osnfeUML7rAAUZi4xxYuUGTXo02wzeZDkWk-bMjNjLbOho5wDmu_QKT1gFiO0J9kNsEoeIP7fwRknEtwAxXDkT45APeJwxVjkRwhM7jcJEcFc4A_FR3tGUrlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-1u3KAXlm_4Z-HNSXI71zCth71edR8LjP3Jl7sgWwkUBIOWoCMZpfcWfw0E2CIflKVKkWDEY6OTuEgcyf9kcdIpHMUdpaiyVrkXnZGHa_XzPRmy2p4CWHPGWDbC9w6ETCHlgJ9_ZM853vGD_l7XL-jALID3DgJ4TT6Mw-sSXKYZ4eI7wHzYd-QjA6tMN27mMbP-4X83XABxsY-Wlslxqo6Ar2Rd3wjRFBrKMyA656k58LmG8yxj2DcnfchcUP3eCyMNdL-NMxJCUu6uNLpPqlv7mJyrpQRwQ31NIQV3pVCsRAW_yDtI8ojrMht--ro0qzLn0FkD3cCZ_iHd5uSMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txRMl3pvtL8RLz9Emv5c-Lp8xtxmh7PG6SwlTry49HAVS3lRCU7hPTZNJfh9wxo67sTwMf-WyTEnnvnI7QgOPXe2KY6TXCppMoUVZe9iLw1ryXLGilSLUYlFjHTVa_ZEuFM6dhGCtCyCjPjNyqfHkvn7tpiiIlDB0fBnDqxv5Hw6qXuxtqy54M4NxEy0PHrOz8sv5Bn6sE0N67tVQ7JTeb9n2Nsdks8nH9OUn4on2MS-aOGfizDcYecn2JXtxHw5VzvvtHRq68327wH-tMD4t9ZgnGqFcYyPXMtSSQVEergB79VvYfsk4Oye0y636AFRKChvPGbnfMN9qwSkdKxi0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ttpZAGKLIGNe9qgpa2wX1vdX_AN9s24D_ijf7SNeDQ0AayGNUdMZfDQiHv-T4ma9TVj8yVjWKnvN8uF2EfBMxL6bvUiRNOh2AK1Ow9UIyk8nXNys27TKUC8upQ0EO3BYteGbi3twdIglxwQA8r2cdFYKbKMBI9o0r52d2fxsMaDzEZSN2sl0Fhw420MbN4Ku9xuON_1pMoTY6ju-WBu1nJGjgwil0tayxGOFhYAmIrxh3yNcpZaHoT2M6-pgrklJUjOs_j7wRg0kxNhhj4HqF3K-ePxmUgLY1XLcxgkGMIlsZXiA_6lvbtGtYJN4bwijq_kwFs2QWcl44j-faVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgTNY3TN4UnLEekNI7ioV473V5ACcqePVq2leiMHot4fOTY3sPXaUiQyna3el4xjd5w4lqX7lFJfIeJ58r8MeDH1ttjS0y7b9C73O-ZkWNOqGkPZwnNqvbZ0Qg4H5J4HIE-tWQg_ZIx89p7h0PXn4ds26uukB20lRMlwZVLvT4CDl0DUBtYYp6uhCljRm7j3jITP7udNeBbUsxGIy35DztbiI1PIrKCNpDI4fkOF5m14yfJhkLqqiLVCLYt2pJXzxcoDSe3FIiXJi2XBgtD9PoKrvxVRjpv6aXBaC4alMW-9xty76pZiiesXTNK8zkiKVH_Z70XoIWd8f0sZ8qSjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_4c-nYoIMFXHcupYo-_tPcBG_6cM_aXXamZ0bizHoTkKaJcOs1w1gdhc8qwzKagbXhRXegZjisYxL1D7q0t5tfva_k5ieIL5fnKLkNAR9q3wDGLp_f_zhoVV_F5n8hEmhh-HibrPK59dWAk35gHO_8ThJmwCMwuTb4_tbIIdoqNHUrOL6EZBQPxyie-r-OWU7DMqwWPuOmQuyO7jg7uQhPCK_PR1I07YvjOAV8qM-RMrTxeYAlomkLWU2b3GiYWlUXLYzjqoMyp1IPNdX5ci1BMO47pTVmUnquwjJfnBz2qtt3FzPoAGO5SfnxNQJPfJ7EDruqz5nlBNxEeE_UPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoUnjk0TQDOoYSzrkfqimVgg4U1DG2N52xkNRVgL0H3j3700cfMCfyy_6Fpip7b-PXJU8c58A1Axjt4c0W1bk_TfAXjZattnwGIav9HB02MgZWqR5OptCFFvw-hHDbtmd37o3G90fnT3eTa4wXNMj0wVGtscb9QkMLnH8YXWAALdrxfr2BVQtDSJYEILSGNR97dJdMohZ_DQlUlNYEwSI6k0dHzAP3V_wXeJrwvn9n2_VgMIWCqn7jPGNPB9vDRktYGF6CU_3PWMX12g9sJSfImrX8IL878_ySk7R9OC2wSPqpCD9ZDtnohxkrc_vrF_kX3mRjZM35740o_LScKjoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3ASleiDrfTlRwLHXFCbnRYmUNatI_IrMprll6nyRNg0R2y2wKfMSJWrDx5DkRII0wdYeJ0mlMcU2Ooyji9Do_qXR5p0I5-UMffaeY8Wq0MxaFkP8oaZt0zKKEMIr0tBHjeyeER_bNs_sm0KCqsW3YmlC4Dz5JuaXDtSku5MWxYNsoxSX_5SFW9zLc6jUvKRiskkMgW6JPNDZqn8lJE2uulDQIKM9l79ORKL39IEwnwFHfigaykLfWliWPO7QxudAWKEglFUyKuvzpVVgvZVkdPgHkFXqxw15a3kSW3N4uu1EhidIeIGuKTkF86SaVVf-q7QAW65DiDmstcT89HEKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVvgecPM9Pbe2l1tWTmEaakKRpwmUCrNaMTNrmMLpdpnd-YqdxS6x4CZn4CvyRdB-goJS00LtVKelZBIhhEPkM-lij55M5xmDH0koycWQUO-8Efozcm9jHUXERM00jlNZSdWlBmFqppCGz_V9EV_pdI8JsQ4TWpL5SoxJ_WluBRrhWcU9EOs0sIM55OA-BgQydM2YVe7iM_JKmhLJsJgKf9Q6v5--gIl7M8A4ag7t0Me8TRmcf9slNntl2L-lfyTTblRpqWmqu_RAMjmhbt7eOpWwgl8H6p-REcHmcWcMQme4IiH3FDvm1SL8gXPR73b7ajiN77R8_j9cSqf6ImWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfR5RMVkWz3O5h3RKPleSDev4RcdlH4R-woeywp3_KLejwWfiQUnNHVEYHXsiqFR6w-m4NImf7QZI-eBKfWER7wT1Jh4bzy82VUka2orepKaSG2Vg0DOVoTxKbCLuiGhPztcu3IzTNJ9tw2Uk6Ybo2UbKnekEr1HUQwbXv8nzL15FWYrmV36UFQHtvaHiJJZfalK7GGLKrZqeouwj3KnmIXELTVB1YCS_CvdS6NRUk0WlG5qmDNKpNUnIFv-h9Orws-27jZPqPvWRO31UZ_8PkvPyyFPUBUZcV45emWSZLQwtR_LMl7_ZDl4_8OHX3rcaOckxSy-Tm2Mg8-TLxtSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYPuo52SqYz4CkUIRMhtUXPMg9ActeznBPGzAUUNVWJdRHWLRmSPz2-kNHvwtmWvxA791JcAgDboBsY-d1a_85HqNS16-WzEfazhxelmzlqGBw4mInV1-7gcz2JKD5Y_eUA1K8F9no88tDUmK61rxXrRTff_zdOmCpgJomMx_WYgHcbQoWCAg8LbDuSqhhyIeTrAZY_qEDhLFdeCgA2ehGG_DP8rrrJ9CHpmqyqytXcHSLjUb5rjj-LydNyhL3QDXHUm-KSXqAWrsANzvtImv7hQ4gbQpY5CsYw2TzQ503_zuVeSG1N6EDQQrpbIqTfJJSTL6gLkVy3ZyEOqk06a6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpBQVAwhBaU3vY9H-xENBraAJ6RQ99UvCKeqgVq3NKENgxkj0OahJHCwZD_NQyfxOzGIXySs_N5rUW21nnGP4HpcLQZHrclOdoDw3cPi_hiVfFTNpzibuMzIOwyLaMdVJULYvFBtfb26n_zeIFYzPE2smfLTjRBFLYd1jQoETIegKLY9l9e1LYvN3yrStlc26ZhU6ZThrx2ZYtW9jSSpsyo6I4JDIF-GOTq5mS3smIZbtXCt7KBu8atYSmbuq8a_xFe2ph2sa2PY_3p0-lF78uhflM3qv0oE2jt8U9Fdi44QVJC4iLMwHzj4uuIax_ckzwPfZRzaws4gg815eLWtSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alxeQO4koALfRshbVxw-HTlu0DD8GfjK1bty9IGEZ8aALD-1Kcoj5SBF6pp7vNUlfyfm2ErAvl8ly-kRfoktAS-KWgqS5ssEnN3fNpBvOpxZDWHNYkJys4VQLmLWc3KzdoTaCb57tQ-Ae7W7pFhIgAN22NnFtWnSFESqyNqDhtgl9M9fGFOgGk4USHT-T-wP1kdUWyBmZgwQm-isBynkYM1OsSRV6hE3GjUM3f2MwRxznKZizhbKVcXci0L2_8jeQArQ2FWPwnLsUWLTAGyhsBBMeQo-UV8EufuXUePqLQUHbWITW-JbiYQPV9R1czzt5Y-kaKZ0v8pJpH3gPqDSbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=DwXW0or_k7vVggr4474aE_CAC5Hk4k9Ji259bk4e-EWWgFwF-y_9B79G2ZTnfizkVEpgKfg1qOu99bl_Nvhn7VsKqNsPqWfnm_u1MJckK6N20az-qOxMUpfp-ZV7DVoYl90SqenQmYZkz0VzMnbmOuIe3vNeEjfoEkMGVcJHwKs5u4U9CCuBSrfzUcKHJc34BCoNqeoykJ3iyd4UQznNhwKi18nX-8lgfGwfsnnfLX77i25QTkOydo9AxtFa6JxHzLiOFjU00SGX_l3Ot8WpeAVMvnwKORWpgyfQ_pM6Nc6A3IfkE9N6bmPPrk-Q78xFmZZ6KcMMZ8WpRT5S3y2QBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=DwXW0or_k7vVggr4474aE_CAC5Hk4k9Ji259bk4e-EWWgFwF-y_9B79G2ZTnfizkVEpgKfg1qOu99bl_Nvhn7VsKqNsPqWfnm_u1MJckK6N20az-qOxMUpfp-ZV7DVoYl90SqenQmYZkz0VzMnbmOuIe3vNeEjfoEkMGVcJHwKs5u4U9CCuBSrfzUcKHJc34BCoNqeoykJ3iyd4UQznNhwKi18nX-8lgfGwfsnnfLX77i25QTkOydo9AxtFa6JxHzLiOFjU00SGX_l3Ot8WpeAVMvnwKORWpgyfQ_pM6Nc6A3IfkE9N6bmPPrk-Q78xFmZZ6KcMMZ8WpRT5S3y2QBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=IM9LhctFqtmUyzdwGxZMPo9m6eVpxrV6ZywWAkK2PsYr6V_CVsuT5shP4s5k9fWOn6U6t2P232NIK3Igfq7cfgV3iCJNtAM_FjH4_Ks8sI9H9fclZbPBCxDbzcC9JdYLknXNS1BxlQzLOMnQy_XBc9Qfha13EvoWuhzx_l-DTwGb1mMxzXziUsdHUBDG9PM4zrZAcGYNCChroyWIqWx-ML3lXGirdqWCJ4ti61sBYp7dW12Uye6JljHLzQShxeE-4u1rED1ut1noChn6yUpJSzVgvD0Y-2OhDLstG0-Xoy0_8IfEUibhx1CecH_W0iqq_13PJVhWJXJGN1MlFxOrqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=IM9LhctFqtmUyzdwGxZMPo9m6eVpxrV6ZywWAkK2PsYr6V_CVsuT5shP4s5k9fWOn6U6t2P232NIK3Igfq7cfgV3iCJNtAM_FjH4_Ks8sI9H9fclZbPBCxDbzcC9JdYLknXNS1BxlQzLOMnQy_XBc9Qfha13EvoWuhzx_l-DTwGb1mMxzXziUsdHUBDG9PM4zrZAcGYNCChroyWIqWx-ML3lXGirdqWCJ4ti61sBYp7dW12Uye6JljHLzQShxeE-4u1rED1ut1noChn6yUpJSzVgvD0Y-2OhDLstG0-Xoy0_8IfEUibhx1CecH_W0iqq_13PJVhWJXJGN1MlFxOrqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI6tk40C3RLVsX06J4i4HBNVsU7_dV7rTaZrCubrnEhHYnpa8D1CDXUQnWUHFK_z7Ruc_XhQbAVOfTWcKxEMlnpOt6fi0jihEsgENO-5MohS_pvjcX-asqZ1EQIIvDN9K0-ByILNPap6-aqq2_Snk5S2jokDn28aBZVqYYhbKAB9ax7MNmsS9ixmlius_XCTRvpzVkU14FIn-gVHcb6stlw-DC6yUzifWdWGHHvFFk91da3UVFaz10kaugNPbE5yioSnozq-6jAH546bkxeKXjBvapry_c0-9v0GD8oa2W7Ag-i_uk1B-EeZ6rlvm3r80qPEZCNzBcWzKvkx358Suw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFnaNHzcoX9dIxE8xGpY6UA_NfFbir-_C3jjwqkn8ncpc0dmPSx7sgnORfFwLkdBO5DiGrUKRFsIc-AQYX_QmbnfI4P5O6dhbBfbVF5jw7sjPDV8SC2eDLwo9jv7_3zmMskDpZVHE3aFgecXcjpkuHl9u1E5bBGy7Yw7p4dPu4h9rQMTcPCMRpcfcu9ky9UFpMSSwNNStZTLyNxGVbuAUsMc5_iHzdLQggPH-KjryAzq5HlGZr6bsyqUtJ1Y7kxzxshGnQONSWlk6LqNTJ1xX4uknSAKfaUtoZI6gNeL942x5bvv5mT4Ddn_oCmgQvr1CVlR3xMs1QviGAnI2UmPfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=q7MIt50OXO3O3jHWKXaiHZ6s9oLwSm892le9bLyYEI6kSkWRVZ1EQpqrSLUyZfcK02t6K2c55XPXhmqHlYeziwb8PzI8gD2kR4ZboaGO1SgGcrzjLLZBzpA5eOzbTRXzwyKYBD03uBdZzj9UoT1yFXVlynFAnr-vcpVHcw7kIm76d9LYMTw9b1upJeElUc8YIBfifNtS8W3ltPBfMYnlmhSn6Lsu69HXsW_hdCVjfgwJFmxeBo8te6gfZw2IYxgk73toiyCopxnYN6kI3mvS0tTApjwFD5_QFtct9vdH_YO_Fb-XCQ39L14vhf9hcPBjnPsZYtoigXlJXtVE_YXcvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=q7MIt50OXO3O3jHWKXaiHZ6s9oLwSm892le9bLyYEI6kSkWRVZ1EQpqrSLUyZfcK02t6K2c55XPXhmqHlYeziwb8PzI8gD2kR4ZboaGO1SgGcrzjLLZBzpA5eOzbTRXzwyKYBD03uBdZzj9UoT1yFXVlynFAnr-vcpVHcw7kIm76d9LYMTw9b1upJeElUc8YIBfifNtS8W3ltPBfMYnlmhSn6Lsu69HXsW_hdCVjfgwJFmxeBo8te6gfZw2IYxgk73toiyCopxnYN6kI3mvS0tTApjwFD5_QFtct9vdH_YO_Fb-XCQ39L14vhf9hcPBjnPsZYtoigXlJXtVE_YXcvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbtwyaeSJF-b5kdPl8bIsgn8vC8mErcgeynVSz5vnUZiILUUsr_qU49sHGMlNkhGr1wILYfetpk0pIuwyCm9qjQG0U8R2ymPlmcQj6uMGCGtCijtG2Qy-hs-KOvPyDXYSwhUjoHVQc18NN9wUbxu0DaqkJkgRDdgG-U2Yu3_Vwf-RVqsCMdGiwwuVQtkHGMkVwCe3zEb-a2VUjNK8TNWt1-4BZU1ofCAdCe6px66u5sIRvR-iZHllZ9vTsRcd9GCnd1Z79NMHq-33iwns8frGb0afVicMLXw8QspK31OLGLpJ8ZSd3CrkliVLqbKmuv8hUXAdppfXdxpQvROVnyUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjXWHYs8tjcpH1dPkA-P0LeTFFdY1U27VIXzOpNIROqZ-XEiKxKMJrCXQZkPiFqUCArq3k7Jp9BDG6wxYPIGXTDkJC8sCN_KZt24ugEIZcnaaeZ79HJWqRE_sVovwJyrRDkYsEBxEVcBSeqJTugU4yPvSUYNy2A1zujMqgL01PzW-5V5ArK6Lm_HxfQ147q_Rx6fWoZKoi1X_EvQY-87jvnu4ansGgiescOWA12ahkQcJPqUq-Xfp20cJ7EgWhR22uN20Ks1zgmqR2RUMB_K7ru_rCw9v2JfxCaQOE7rXx_dBs5aKqtjpbcPFxsbYNMIeeGna9_kUPxhKcIFaSKOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=ssrYmWwwhFU6f2LF_p6_4JpdzhsZLNLQgkHJSv9HaR5h3vmo-B7ul2OFPo5FZx_DsMSjlFMCMDODFyIXNTshIYsnWSXMVUN8VWKxXYM5y-he5lY3udIKGv710YB2smcrZvFWi9-mskaR1OD4QD5vB8bDRKWaz9hgbk9E5Gk5wGMK_SLJF7N1d3XQcgg04AeUpkXJX4F_x4XMpLoCz4LHzsVGRuxU5cFCDJO8_GTQYuox3uh51cAAwHio5qn_bIItSRh7DejZ_qzxKm7KYBq2hEmXtxgHFTI2oyq0Ae8Ybu7gh9o0ZANnz6fiV2HUkut5teioirLnMztU7cj22ktJXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=ssrYmWwwhFU6f2LF_p6_4JpdzhsZLNLQgkHJSv9HaR5h3vmo-B7ul2OFPo5FZx_DsMSjlFMCMDODFyIXNTshIYsnWSXMVUN8VWKxXYM5y-he5lY3udIKGv710YB2smcrZvFWi9-mskaR1OD4QD5vB8bDRKWaz9hgbk9E5Gk5wGMK_SLJF7N1d3XQcgg04AeUpkXJX4F_x4XMpLoCz4LHzsVGRuxU5cFCDJO8_GTQYuox3uh51cAAwHio5qn_bIItSRh7DejZ_qzxKm7KYBq2hEmXtxgHFTI2oyq0Ae8Ybu7gh9o0ZANnz6fiV2HUkut5teioirLnMztU7cj22ktJXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rghBOkxUlzF0Coued0-LeBowP8dv8zjG7_k4nsbV6hhDFAX20vcNJPrtT-8xZuFls4w-b4p9Gw3Rxyg5wAD4vCArr13uUrOig1uP1Z9fDUnIbxBN-4BVZBldaj1mCF66GXvgCwKGUvivBWOO7_fPC3W7TRqcJEn30PV01cijXgLsZJ1uuMf5QKRdZ2JYRJpRdz1JfuUcBOpqzfwSan0Pk7lMW5Exb7SSYKnGCPqi_8yr6l3OkiGp60S8tPXbCl7epcoKV3ECGaKN13P2ixpl3mSl_DZGIENJQxQPiVZ81opToKETkCdVzeKX61qVycLUiAPVw5RhNhHXD1Ay2w_AWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=OAekTB_HIc7YT_o8g03M3c5Alx3hFtnYSLUlZTDFk695W8nPSljnZPYqWcTVAjO0PM7OZKaz6hbIBw5IQZA6Y6MgUPXiPSR8EU8OnKaZ-4Z9f6NMhBDLOPqZd-HcuDLX3L5BbmW28n6lr7qO5WE2U0LAWu3VlzFZZpF2sMjWK5OzuiwxT0wxEqPcSt2eHvN6MZaLPgelPN-Wc6EhT64yZ3T9u3t8P449ZQv4_sBRV7p90J8UJnGKDf68aF7VTySdkXUk_KeXf5seojMOPnNN-s20mzMltaVS4QtdDU5kOa-xmF9FlDdOb7gCU4tnOdjKbYfiOw2xJYXpaVrepn7buQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=OAekTB_HIc7YT_o8g03M3c5Alx3hFtnYSLUlZTDFk695W8nPSljnZPYqWcTVAjO0PM7OZKaz6hbIBw5IQZA6Y6MgUPXiPSR8EU8OnKaZ-4Z9f6NMhBDLOPqZd-HcuDLX3L5BbmW28n6lr7qO5WE2U0LAWu3VlzFZZpF2sMjWK5OzuiwxT0wxEqPcSt2eHvN6MZaLPgelPN-Wc6EhT64yZ3T9u3t8P449ZQv4_sBRV7p90J8UJnGKDf68aF7VTySdkXUk_KeXf5seojMOPnNN-s20mzMltaVS4QtdDU5kOa-xmF9FlDdOb7gCU4tnOdjKbYfiOw2xJYXpaVrepn7buQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VomH1XNzDYQMoN6tNTs_p1NN9Il7_yalhM02GoskCrE653_cwEF-zA60LU-F9pELLXe0Q2pvpxB1zQ9y_g3xrH2fzvvBBHvr4cEmy6Nq-lOtLx5215K1rZRxncdzT5sZ3Fk2cNGCuam4QZRTBqIgbkPWVK-nOBF8bo_jkO1s-HNhAh2IEbCxBv48du1lLwiIXaIr_kEbwTM9h9paAaB9D5aVxaEWvceaMjDbVNuang15bw5ywmVYpNUOje0FmAIc1yB4AG7WNGxom-7h8RzbASWBAr9ib7lgEtEliOXZf5lQhor6eS3IRetJA0Rs4z5Wn4EKzqZf5EwePae7YVOvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lsml0B_zFBAeicFpS2bAOfVFsUxj-ebLw3vaKf4oEV6pOi94zDcEGOuw30gXODn5-RZWhPJsWx-yv5HTFp3kSnkUPURsHxVfD1LHwodRPWzpc0dQMU1JRTXjhU6exnajCAbYE_rMn9x847B6R6BpITJNiRi0PQ2-64ZxDmPoH14bewKgftgbsqHrtYlscWjYWVfuGDLCQNMveJ9M-k6c6g4QV5jDQrqIy8iVeEbtSlh9OvSfPzhT5QuoEpnMj3UVkUe_2_KRMG8KJ-83HowruPlvrssrw609o6z4-ngiCh_3LPSSpA8cqc7A-P4tg9hxi2exQW2bvjjPX_OP6rPSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
