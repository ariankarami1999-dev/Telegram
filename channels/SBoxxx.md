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
<img src="https://cdn4.telesco.pe/file/DwWsLWBDMCc7k9vH_l53KGkNJvdAFcG-TcIHebV04UefHrfO1gs-I41vbcocqn1X3LD4JYlVRfvIBhZgsgnozo-wfh5cmz3YuO5MkhFsHvUM2GuxgTpC5rSKWT51nFOtUuo8fTKnm6PDJgycMn4buCgAzJSjIivcsgPn8-Dtx3-v0Exn4ykDYeTWI1YMXDGbjD6cwy1IbEYnI2rcr4njVfTv3Ydj94aasGPVRegBHSonIQQBFkQazeBvc7BGL4cNbw_2yE_sAv0-Yk2sT2EadEuCsFIHcJg8IgMZlTBLY541O2IvHRndQ3Va7S3BJia3KrqmzMv6v8fU-R2qcPBGDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 11K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-21701">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ساخت نخستین پایگاه نظامی هوایی برون مرزی چین در لائوس!  بر اساس تحلیل‌هایی که در روزهای اخیر به‌صورت آنلاین منتشر شده، این پایگاه در عمل یک تأسیسات نیروی هوایی چین است که تحلیلگران آن را نخستین پایگاه هوایی خارج از خاک چین به‌شمار می‌آورند.  چین این محلِ مدیریت‌مشترک…</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/21701" target="_blank">📅 19:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21700">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تغییر نام حشره آخوندک به راهبک در کتابهای درسی</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/21700" target="_blank">📅 19:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGHPs179CflPjYrYeJLpmVvppUGnm6ultGnw2GsLkMvEPKZs0LsTIjkHVXpqAYxMyQyPcdWvBlRAn6jU9OWhVc09MMauzm3ToyL1wZyvROfB-7Nkv-chy1i2hX9WuyKVvLLH5VeyMyf7RYnVbQTUBVKc72z03CLSCW0lx0xEa6p4GfpAuOGdmoQNosEByt_w0YJ9hstycFA1JsWIfhI8jr1M9d8oLuptE86mLp4YSAXJGJNNIjnNaSeLNtXU5ctAn5LDhibpiSslO_Nk6ooVPoJNg4oL9csMSCXdyDmDxp0hancm2MZEOGc6njxhWK6-Gdp-ezT_mipJJeIIZMlFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر نام حشره آخوندک به راهبک در کتابهای درسی</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/21699" target="_blank">📅 18:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhmcxqmt-TyiGwnCQekIw3zulzQuq2HSJ5OaPo7Iho1SFHMT3wrzP53vFJKqoHJkO-nxbFyN_JQ6zXiH3gD2OI9jsncBus_tUZYNH-Th1BoOxCOOJFJGe1PYLLOB_TzQKatwKi_t5A2iAo9ILpIxP5ts9E94GKHf_r8OCusndCVAVzw6YB3wbHHocEtlRYHPCBdFpeOj_EKwUe-Utz1VbHE02u-yE1867V7LK_OjpGygIknHV1xA0wbRnf2uR4_Wlp5p9wV7Q6n8_uBnjIehwyzCfHdVES2Uie16OMadNdkWh_9FBFyYXAQI8z3EZdeBd2NEiQJ1-HDzz3dsO_tgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح!</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/21698" target="_blank">📅 18:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21697">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">طی توافقات ترامپ و پوتین، خدمات رسانی استارلینک به اوکراین کاهش محسوسی داشته  است</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SBoxxx/21697" target="_blank">📅 18:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برنامه جدی از سوی سپاه و حشد الشعبی برای حمله زمینی به کویت در دور‌ بعدی جنگ وجود دارد.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/21696" target="_blank">📅 18:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21695">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">فروش دارید ببندید</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/21695" target="_blank">📅 15:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">بومن، عضو فدرال رزرو، می‌گوید «هیچ نیاز فوری» به اقدام بیشتر در خصوص نرخ بهره وجود ندارد.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/21694" target="_blank">📅 15:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21693">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">بومن، عضو فدرال رزرو، می‌گوید «هیچ نیاز فوری» به اقدام بیشتر در خصوص نرخ بهره وجود ندارد.</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/21693" target="_blank">📅 15:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7JYTH8aoZgOEGtrhziux6GwaSociMnsF8Yl-UkPhc-yyxUPZVufTnlsyCQd8GD5_pQJmfcPvNmP_XRYMHK35pYM3IW7PP3OlliQ8Om2Yh7B3k7ZDR3W7wF7-sKiUHx0fSrjLo6KEmnbWgeIYDgC9VbQ7oVYnmUO_gF5xkiFQ_i_3kPiFtHo4o1SPXmvdU6uQf4ki7QI_uwyRLGd5nkeoWpYwvxqRVESmCB3hH7BJE-7tiRQ7nWI-6lr3h6F2z85uN22VA2sGdxHfDWqbLEuifcs-pYpXgI6p_kLiGK0CmJDuuPcWhugMeO9D2tvHDRH1466fWqyswHAyxOrBusSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت نخستین پایگاه نظامی هوایی برون مرزی چین در لائوس!
بر اساس تحلیل‌هایی که در روزهای اخیر به‌صورت آنلاین منتشر شده، این پایگاه در عمل یک تأسیسات نیروی هوایی چین است که تحلیلگران آن را نخستین پایگاه هوایی خارج از خاک چین به‌شمار می‌آورند.
چین این محلِ مدیریت‌مشترک را یک مرکز آموزشی برای خلبانان نیروی هوایی ارتش آزادی‌بخش خلق لائوس (LPLAAF) معرفی می‌کند. این پایگاه در واقع سومین تأسیسات نظامی خارجی چین است، پس از جیبوتی (۲۰۱۷) و رِئام کامبوج (۲۰۲۵)، و نخستین پایگاهی که حول یک مؤلفه هوایی — و نه دریایی — ساخته شده است.
در طول جنگ‌های هندوچین، بان‌کِئون نقش «لایم سایت ۴۴» (LIMA SITE 44) را داشت و توسط «ایر آمریكا»، خط هوایی متعلق به CIA، استفاده می‌شد. بازسازی این باند فرودگاه از اواخر ۲۰۲۵ آغاز شد؛ تصاویر ماهواره‌ای اکنون یک باند ۲۰۰۰ متری، یک مسیر تاکسی، پارک‌های هواپیما (اپرون)، آشیانه‌ها و یک برج مراقبت را نشان می‌دهد. جدیدترین تصاویر همچنین ۸ فروند هواپیمای آموزشی جت K-8 را نشان می‌دهد؛ یعنی دو برابر تعدادی که نیروی هوایی لائوس در حال حاضر در اختیار دارد (۴ فروند).
به گفته تحلیلگران «مرکز مطالعات استراتژیک و بین‌المللی» (CSIS)، الگوی «مرکز آموزش مشترک» می‌تواند در ابتدا به‌صورت یک تأسیسات مشترک با لائوس آغاز شود و سپس به میزبانی هواپیماهای رزمی گسترش یابد، چرا که باند فرودگاه برای تمدید آتی طراحی‌شده به نظر می‌رسد. با این حال، در حال حاضر ارزش اصلی این پایگاه نه در توانِ اعمال قدرت، بلکه در «حضور دائمی» است.
تایلند که پایگاه هوایی اودون تانی آن کمتر از ۱۷۰ کیلومتر دورتر قرار دارد، اعلام کرد «به‌صورت دقیق تحولات را زیر نظر خواهد داشت». ویتنام که اکنون به‌طور عملی توسط چین و شرکای «جدید» یعنی کامبوج و لائوس محاصره شده، سکوت کرده است.
بان‌کِئون به چین مدلی تکرارشدنی برای دسترسی به زیرساخت‌های خارجی، نخستین پایگاه هوایی در جنوب‌شرق آسیای اصلی (سرزمینی)، و یک مرکز آموزشی که خدمه هوایی لائوس را به تجهیزات چینی گره می‌زند، می‌دهد. شاخص‌های قابل‌رصد عبارت‌اند از: احتمال تمدید باند فرودگاه، ظهور هواپیماهایی غیر از هواپیماهای آموزشی، آنتن‌های جمع‌آوری اطلاعات و مناطقِ محدود به استفاده چین: آنچه در ماه‌های آینده در اپرون‌ها ظاهر شود، مهم‌تر از آنچه رسماً اعلام شده خواهد بود.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/21692" target="_blank">📅 14:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RYB_1Fw06wjLYFLWVXY-dVV3Aw0Ypf48TfPo8l56DmOSFUwGfQ4fqvbHhrA21UBlk9eQVRzwucoNfg0lAtlk-3CXXx1xya51N3vtvn-DM7GAixdZUkmhImcl1X8q6lvp5254BwXeXlKN6_G5jH4xcQsTPkxp2lNAPtRHq5oqwbmtxkRmiWI8NBJZCob6HfVeGSHlg-eNFK3ppximd3kWP6ZmvOaybdt6UBLRqHL76kMdpGK-Zkxfc11lGIfjszNlFYGuZXz9pi6dsugG67fJpmFcG-SrQoYuYwaELmyOImvyBF_v6o6AuyPmjXOztHChcWGyAN4l1YW9ImUwFbPgeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف لعنتی
😂
😂
😂
@Piknikanalyst</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/21691" target="_blank">📅 14:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rryPuV-ofepbl5ri_89DKxhrAtwkG6WvSKDhlDxkH4Ns5MdkowEkefEKy2nOMD9FTBC72YTEGft1AY1C1j9j97CBahXUlpxho5BdgZbMrcdxPOLQtXXdTOmp7NUdt-V0WD2_2YO_bH-9CV0CmTi6mC-1MO-lEzC4VH5LfngHxA2BYYjmCBtuZF2K_d7e7d_1m-f21eXIlDgclJXJW-2m7j5tKK2XJnVEAQ1AjxN2_53k2qzvTdXC6PaPcsKgo9FVGp6EVIA0qGVBFyuloFoiA_VExiE99LZyAuFgpSkBvcRzV6wrtVIwdEXysx5WWFvZP5yxyi2EMEzaU86tCOsf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
ریسک های پیش روی بازارهای مالی از دید صندوق بین المللی پول
صندوق بین‌المللی پول نسبت به ریسک‌های بازارهای مالی از جمله اصلاح بازار هوش مصنوعی، افزایش بازدهی اوراق قرضه دولتی و تشدید حملات سایبری هشدار داده است.
ترکیب این ریسک‌ها می‌تواند نوسانات جهانی را تشدید کند؛ به‌ویژه بازارهای کره جنوبی و تایوان که وابستگی بالایی به صنعت فناوری و تراشه دارند.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/21690" target="_blank">📅 13:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21689">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">روابط عمومی نیروی دریایی سپاه اعلام کرد یک کشتی کانتینربر  با 2500 کانتینر امروز به مین دریایی خورد و غرق شد.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/21689" target="_blank">📅 13:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21688">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7GwBnNMwsj6UOeey--x40rqaE9Cf17FBzbeeZCJLIQAEboTa7j_Y15PFV_unBl1yw84s1B8JsDQ1X4TcTnVGlmpqzX4Fo2M0jh6dzP8fqhRFprTfmKXTSwDFg4V0wW65m2ADxvFVpdXQ5aIHifHIQDQjvam6K_5Bqr2lbvB7L5x3W3EfiyeCUKn9Ko466FuGfif7DvtCJBO6Fh2-EFTCKJbfPQ1WJj-qGM3HbxV82YhczMRmrZ2giKOGnOHDSVYeaGv6MS_lnknt_dD6Sxl8FFYjroq9MyMQxSxZrwGAyBX223xvrG_3-OpBhJShtHoDYsinelsvcRUYkMDZyFczg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD
— M15
بر اساس تحلیل 2 ابزار بالا، ادامه ریزش تا سطوح حمایتی پایینی محتمل است.
بهترین استراتژی خرید در محدوده 4125 تا 4115 است.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/21688" target="_blank">📅 13:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21687">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNAUMkCNgLvFPsu2iBUbg_4zx2_11Twd7lUDIQrTrxfonoQEdFiOJlxY3vWsjccasTn_4JlfqSLDXmw3jCJ4IHTvwg1OFQf65oYp3l-By7YVAVNbB1CkiFz4ViLIPP4fHkkqkRhKzad9NagSOv9XqGDiYjLc_U2cEvU5ces5b2pzGFo1iJnEut2U--8uQqPeyc1e-dESTPcqL0Sx-5Q6RO-kuBbyv41JkZaV85sohjaKFlzY5mo0u4RizJ9NTvJ7rjdKFhT4NKOS0_6eKXJ3TXOlJ5EsT0zFXtJpahf7hP98Johp1JeiirESUEVkrSlP7x7TbTX5xfiqfB8c9ePd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به محدوده بیش—فروش است و این یعنی خرید در سطوح حمایتی توصیه می شود.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/21687" target="_blank">📅 13:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21686">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_efBDPyop7L62gPOgoFb4PAaIc_jRT1iCKfws3ybyYlH7SnUMRQOtZo6tpRWGZcoaXgVLjWRkkKS2luJgaE0-2FdmCZZnh4gZnmGfUSlEwhvIqnUSLTcemIOFZP9G6g6UBGIb4l50uBj0QX8zmoIDiuLvBqybupzn48jXg19XyJLb4W4KmZ9wpx7SQnx7hmjK2Qmv_qOYeaI0KAjvdKav9AUts2MnffJ0ax7lpyOIzejMOu4TTIhZt8AvC7_-eachq8LPjudj71aWq763wFv-Jd4J91Js-6hkWRoYksTAus8tqGJuZEccSgz8iIoXha0R-GCPSWoyA7zr0de50kkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بالایی است.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/21686" target="_blank">📅 13:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21685">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در سیستان و بلوچستان، وضعیت  حملات به نیروهای نظامی تقریبا دارد به حالت روزانه می رسد.  تمرکز نیروهای نظامی و امنیتی جمهوری اسلامی اما روی مرکز و شهرهای بزرگ و غرب کشور است</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21685" target="_blank">📅 13:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21684">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkUYmeqskalG2z-nlGZAh2vWwpIRpc_qiZQFZSgIcVtKUNHfznPYlHJ_bDlO5076kbaFN1UIIYpd5KUz2VLxxc2aJEJnE7DW0jyYLy2ZeAEJf3U-0NVGXv76EeGki6gO03vSMKXhZBW50fFA-fQfK3R-L-XOqMOuPqDfO9OuPWzu82gxKcyDg4M5Pr8-GrN9h3jAtmwPSh7H9rgk4aSmuMHOM9rXArVnfClAF-HD6eMJBhFxqU39ogstbQva6YpMYpM28sOJUOS9g7YRszfmb_05Mw6N2KNnKhlGzqgv6dMWa2_uP0oOp7uuzyHu-WkSMvYoy87UAWJoBFRC7W8lbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات ناجوانمردانه تلگرام</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/21684" target="_blank">📅 12:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21683">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsUpuNwtZ1KtgGEZTs2Se8WLv1MFoY8A0_NdLW16XMOEyfpFx3Cz8RlrVuCPg7RaUZbUOcCwTczOE-QNsSFYK_6M3FdFq6zf7YPAiUZLouDuZJSK0uchLWxcwIppJV10fotztZkGMwlSIsk8FcwXQLjJCqj03S1pYiQ4fvkn8-T1qGspGk1vHc9x8VVLKnmT07EChkH4K5MnsNyMn37YW7-HKm5oxzfrf9QvxvuPMezpSb2jbYGQQ6VT-eymu9WFBVUuts2DQ0tKsxYSHJLsOa0jOZlkbrkXgRN25LNZmuM1DUuo3qRcMwxyXuqGBY2vTYfJx2h3B1aaeyGcdVpoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات ناجوانمردانه تلگرام</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/21683" target="_blank">📅 11:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21682">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خاویر میلی، رئیس جمهور آرژانتین:  نسیم‌های تغییر به نفع ادعای ما در سراسر جهان در حال وزیدن است.  اخیراً، رئیس جمهور ترامپ اعلام کرد که ایالات متحده در حال ارزیابی مجدد موضع تاریخی خود در مورد جزایر مالویناس (فالکلند) است.  ایالات متحده در حال بررسی این تغییر…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/21682" target="_blank">📅 11:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21681">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حمله آمریکا به چند قایق در سیریک</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/21681" target="_blank">📅 10:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21680">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ادامه رزمایش های موشکی سپاه</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21680" target="_blank">📅 10:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21679">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آمریکا دو پایگاه نظامی جدید در گرینلند تأسیس می‌کند  واشنگتن قصد دارد طبق توافقی با دانمارک و گرینلند، پایگاه‌های نظامی در نارسارسواک و مسترسویگ تأسیس کند و حضور آمریکا را فراتر از پایگاه فضایی پیتوفیک گسترش دهد.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21679" target="_blank">📅 07:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21678">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ابوالفضل ظهره‌وند، نماینده مجلس:
پیش بینی میکنم ظرف یک هفته تا ده روز آینده جنگ از سر گرفته شود
نتانیاهو بدون جنگ باید به زندان برود، برای همین چه با ترامپ و چه بدون ترامپ، جنگ را شروع میکند!
برای زدن زیرساخت‌های ایران ۳ روز برنامه ریخته اند، با این‌کار نتانیاهو انتخابات را به تأخیر میندازد</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21678" target="_blank">📅 07:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21677">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ:
ما به ایران درس سختی خواهیم داد. ما دیگر از رفتارهای آن‌ها خسته شده‌ایم صبر ما تمام شده است</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21677" target="_blank">📅 06:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21676">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آمریکایی ها میگویند یک شرکت چینی به حوثی ها برای هدف قرار دادن کشتی های آمریکایی کمک می کند!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21676" target="_blank">📅 06:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21675">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">استفاده از نام درست «کاسپین» بجای نام منحوس خزر برای دریای شمال ایران در سداوصیما</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21675" target="_blank">📅 00:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21674">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfRafVS18ol7rMQoLDUS7w0V_wsu_3K3zYPQ8MFYA_ilXi_ANzkXQUN1OeoiZptg9987yMN9reySCjMMepkR9FvrIe38D2_HNLFUlj9dQIHynbM2MTTPRHgvO_hiB2DIMyPBmadKdr1itnGIOQ7bnGCIAzpDGCxhWHCcOrqQCd-JN7jeH0zV6od8vrS5YR47PaKXz7KGft14O1VBcymmvUgATSIzBZ1UGRyXsRAyunGejfJHQ202FmcvcrNKw1kQuYe1U0W7_7ZP1psJdgRYJQinZP9BRI2_QZnKvKrSHK0LLvBeT05WTxxStcFcwjk0YvY9Q8TIVm-oeKmiW5kFpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده از نام درست «کاسپین» بجای نام منحوس خزر برای دریای شمال ایران در سداوصیما</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21674" target="_blank">📅 00:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21673">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حمله حوثی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21673" target="_blank">📅 23:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21672">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گویا نتانیاهو در حال برنامه ریزی برای حمله به ایران حتی پیش از انتخابات اسراییل (۲۷ اکتبر) است</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21672" target="_blank">📅 22:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21671">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پوستر جدید سایت دفتر رهبری !  مشخصا بر جنگ ترکیبی (زمینی + موشکی/هوایی) اشاره دارد</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21671" target="_blank">📅 20:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پست جدید ترامپ که به نظرم به نوعی تاییدی بر حمله زمینی است.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21670" target="_blank">📅 20:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21669">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy9c_aK_i3-oqN2N5vrIihDCcSdFBDOt2hzJ1il3o6rWvL-iY_QjYT9Nal4N49HS2aybuRZIgYXizN3i9mM6KcQnK23g7UAFhGDejitDh8sqAAQXPWOYBNggijwoQR1IXoo9QhhI4L6B42bPVuy5xSlFoVLK9538UFxDHAW2in2aEbzKe-jDdItmrFumVecJXMRc5kvFq-vJoXlm9Oupd2xjKSfkI3pyJrrwMu-_VilbI5Q-dr0DCVF3pq5YcC8jScEu7nlGznv4amHw3CYLXLVP6sS_Ux9QT9E0WcGsb3_QzBSh1gJsamLsDDq-IiwCJozetz8RS3HDWVm3sBcGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نقدی:    آمریکایی‌ها اگر تصمیم به حملۀ زمینی بگیرند آن‌قدر تلفات خواهند داد که خودشان تسلیم شوند.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21669" target="_blank">📅 20:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سردار نقدی:
آمریکایی‌ها اگر تصمیم به حملۀ زمینی بگیرند آن‌قدر تلفات خواهند داد که خودشان تسلیم شوند.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21668" target="_blank">📅 20:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21667">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ:
رفتار حوثی‌ها بسیار بد است. فکر می‌کردم آن‌ها یک سال پیش درسشان را گرفته‌اند؛ یعنی زمانی کما آن‌ها را زیر شدیدترین بمباران‌ها گرفتیم و به درخواست خودشان، عملیات را متوقف کردیم.
آن‌ها مدت‌ها ساکت بودند، اما
اکنون دوباره سر برآورده‌اند—احتمالاً به دستور ایران (کشوری رو به زوال که نه نیروی دریایی دارد، نه نیروی هوایی، و بدترین اقتصاد جهان و تورم ۳۰۱ درصدی را دارد)— و به شیوه‌ای بسیار زشت به عربستان سعودی حمله می‌کنند و عمداً سعی دارند قیمت نفت را بالا ببرند،
احتمالاً پیش از انتخابات آمریکا؛ که اصلاً کار پسندیده‌ای نیست.
کسی باید برایشان روشن کند که من قرار نیست در انتخابات نامزد شوم [چون] همین حالا پیروز شده‌ام، آن هم با یک پیروزی قاطع و عظیم؛ اما پس از انتخابات هم آنجا خواهم بود و هرگز فراموش نخواهم کرد!
رئیس‌جمهور
دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21667" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرنگار:
آیا از ترکیه می‌خواهید که در پاسخ به حملات حوثی های یمن شرکت کند؟
ترامپ:
شاید این کار را بکنم. رئیس‌جمهور اردوغان دوست بزرگی برای من است. من احترام زیادی برای رئیس‌جمهور ترکیه قائل هستم.
رئیس‌جمهور اردوغان، به نظر من، هرچه از او بخواهم انجام خواهد داد. من احترام زیادی برای او قائل هستم.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21666" target="_blank">📅 19:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21665">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdVyOkfptS-qTyVHqTumMDQJnXaPRGv-iK6iOtwrgjrtoAKwma_E1-tu0HoNlZ55eXXU4d2MQclyE5kEFCg1nKKsrTuoa412tLpVPQ1tx0LRxfPmPwsSdeW7hDAna0819pC8WCg2ZmzXLU49VXteTKAACOD2EE6-xUa7usDaNJsll9o39tmmg2b-37ophFO1sahz7D-qofJrXuILC7bQrEDgi1c2Rxx4mTU9Hyjfysi_8DsX842bVNvaovbdxZD-I4c3p0TCiPXtjR-pPsGl4lHx4tFzO2UQBgKbK96yCwBTzgxO8e1D01za12jl9arFZ1bkPXonXRPCzk61UJxwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بالایی قرار دارد و با توجه به رشد صبحگاهی طلا، فروش رو به بالا از 4190 توصیه می شود.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21665" target="_blank">📅 18:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21664">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔻
اختلال شدید در اینترنت کشور آذربایجان در پی وقوع اعتراضات سراسری علیه قانون ممنوعیت حجاب</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21664" target="_blank">📅 18:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21663">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">— حملات نیروی هوایی سلطنتی عربستان سعودی ترمینال نفتی بندر رأس عیسی در الحدیده، در مناطق تحت کنترل انصارالله در یمن را هدف قرار داد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21663" target="_blank">📅 17:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21662">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">— حملات نیروی هوایی سلطنتی عربستان سعودی ترمینال نفتی بندر رأس عیسی در الحدیده، در مناطق تحت کنترل انصارالله در یمن را هدف قرار داد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21662" target="_blank">📅 17:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21661">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
آقامیری؛ دبیرشورای عالی فضای مجازی
:
مودم های استارلینک اگر برای اهداف مخرب استفاده شود ، هدف مشروع جنگی خواهند بود</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21661" target="_blank">📅 17:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21660">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر بهداشت:   در ایران سالانه حدود ۲۰ هزار جوان در جاده‌ها بر اثر تصادفات جان خود را از دست می‌دهند</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21660" target="_blank">📅 15:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21659">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر بهداشت:
در ایران سالانه حدود ۲۰ هزار جوان در جاده‌ها بر اثر تصادفات جان خود را از دست می‌دهند</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21659" target="_blank">📅 15:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21658">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پایان درگیری مسلحانه در کورین زاهدان با کشته شدن ۵ تروریست
یک منبع آگاه گفت: «درگیری مسلحانه نیروهای انتظامی با عناصر گروهک‌های تروریستی که از صبح امروز در منطقۀ کورین زاهدان آغاز شده بود، با هلاکت ۵ نفر از تروریست‌ها پایان یافت.
در این درگیری، یکی از نیروهای حافظ امنیت نیز به شهادت رسید.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21658" target="_blank">📅 15:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21657">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔸
زارعی ؛ عضو کمیسیون امنیت مجلس
:
در اسرائیل گندم کاری خواهیم کرد</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21657" target="_blank">📅 14:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21656">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
عبدالملکی ؛ وزیرسابق کار :  اگر گرانی رفع شود ، قطعا مشکل اقتصادی دیگری نداریم</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21656" target="_blank">📅 12:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21655">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
عبدالملکی ؛ وزیرسابق کار
:
اگر گرانی رفع شود ، قطعا مشکل اقتصادی دیگری نداریم</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21655" target="_blank">📅 12:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21654">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⏺
دبیر شورای عالی فضای مجازی
:
اینترنت در سال گذشته فقط یک بار قطع شد
هیچکس دوست ندارد اینترنت قطع شود، همانطور که هیچکس ترجیح نمی‌دهد در دوره جنگ، پروازها بسته شود اما چاره‌ای نیست
﻿</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21654" target="_blank">📅 12:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21653">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">روزنامه وال‌استریت ژورنال گزارش داد که مقام‌های ارشد ایران هشدار داده‌اند در صورت حمله به ایران، تهران ممکن است دامنه درگیری‌ها را در سراسر منطقه گسترش دهد.
به نوشته این روزنامه، اظهارات مقام‌های ایرانی حاکی از آن است که سپاه پاسداران انقلاب اسلامی ممکن است حتی به عملیات زمینی و نفوذ به خاک کشورهای همسایه روی آورد.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21653" target="_blank">📅 11:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21652">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS6_0pJVpIgAyY5n8YWFLHduD0ibmLn6pqYdu2SDNUzTzia9qLRZ973bRC6lrttU4mFSAREkL2LA5iUKVhBni9VCTm8pdyQ6YrL5z00AaRwfU0F62Z42C05lLQ2i4ZYIer6uYlz5XyJNg32kN3R-mNf5SSz-vdGh4-62UwrZNGsj9BxXXcPfXu6WJ0cGxBBft820Atc7hEgkE8o68qwTkDvdKdTHpRpBpCdpTjuN1NLATiy8Ek5ZEWiIO5-zFtmA85Fhp1HPYxWG_RwQjCDsL2nap3nAaQ0k_yF0F8BxXq0rLl9SFNsGvwa-1Ifc8N_HB7FE_i5DS7L2sei3ABllLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC نیز نزدیک به محدوده قیمت منصفانه است و توصیه به خرید قوی ندارد.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21652" target="_blank">📅 11:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21651">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5uDneFpXDYwzZDrNfhZU_QlRj5_1OiFtkjdx2ljSOgEb-R2-Nv5uQ1hs9QjaIQdDOJDXIScU40S3-57hdUM9SRazGg8VYUA7J9xdFn1nZ6U6jEZNtdsCmnd3apJElNBJyppV4NRqiwk9TOAva8SgdZpRj4a6CVVRP8_lfR40RU48COSVSC-KisX4uutB6D1ooPjWxsDfjksGf4q9VpeMr8z_9Y5_PeJniFl9SP6dEII63tAINk9VjRY-vesGfFPH-375yw_iTYiAohjI9U_1RjAonSrEhSJ_QC7bw2nDpDzpY1tlz1NZqY1zffpyaKQYnR-1gGCrWXs-9aSoz8JRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بالایی قرار دارد و با توجه به رشد صبحگاهی طلا، فروش رو به بالا از 4190 توصیه می شود.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21651" target="_blank">📅 11:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21650">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ولی حس می کنم باز فریب می خوریم و قیافه اونس میخورد یک بالا داشته باشیم.  دلار هم دارد پارابولیک بالا می رود و این مشکوک است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21650" target="_blank">📅 11:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21649">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kinneGbwMerMF76HzkBNfd3w8y9DJ6IOUljW4rQ_edPt_ch1C4lpqfvCnwHKpvrN2T4dYzN-G4OLGV-7v36RS9N83BF7XF6i9OkBvxzFtfwE68GfXsskk2-wXagq1B9zBjZQol01FjGtAduxBWTl_tPX186I5UQo7ZMKRmJRcSa1eFjwsTTrtDZq46yw0F_drMu2-tsjM3M3wB7tjTukh74XSEzxZB9WI2syUAJSxx9BxXy6oOjeXjca83qQ64eBNQ2cK9DGTITEAaiQObncNG4AU-BRS951S9MluTKNDJgNf259xOl0VQgPITjmXI1L5k6XBhRBVpMbGLnHMXuktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD — M15</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21649" target="_blank">📅 11:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21648">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVf87qBsI-7_9arzszon_jXTnoQ-bFWs6XQAXtKkbSYWPnl2DH6rNXzbcVHL9hnQQ2Umg6iEHaSodA-MCVjD6L8eVp7OvoybUDOViPtjQOam-_wh6e75k34hUfiEwC0f6bhk-BPVUaQRo9KTk2vueCTVS_u5l7gs83-us7Ivd0yYyCNoaFXcwsPHlB3eeDyEUZ0JkimwopZRs971bFSCRAiCI-HVFbgkHGKastfdXZXas_xeUFPrSZUypWzlUBVhlUwuFq0sQ7O36dkkcgWBy-TG_b_5MBgvTPI1GP0-Wn9GA_L8MLDDGO5ECNuQL3nx8bTpE3S8KYgX5Gmf3XXdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD — M15</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21648" target="_blank">📅 11:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21647">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنظامی ترین(گذر زمان)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb4e26728.mp4?token=W6VxscwaviunI8dTczFeC93Stz7sFBlai-24qGhJLISkBSnNYY3ZPGYcByZOzWyIAJ5T6SK-AYIxKwjzMdDr9s4iYBm93w6z9NgQMV8XOXOXVqUw_KZ7koF8wzp0DFkB-NKn-UOPtNuAWPXXl1QCcRI6FZxHxOBYWKLfgx-6Oh7O1hiVd3wXC4g8AWif80DSQlHKCF9jjWwFUKAImPHhvLvOOuq-fmGLx0l9_dLWoXhpWuXP3hzQNDzdmg6AiA1JjRC5nZqjsXnH5Dj41YkNsIR-3Y-roVG4UcA6E0FlmbudR97E-fimYTU7Be8oiMTy9U1jIN3T7qsU55tGrHJnZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb4e26728.mp4?token=W6VxscwaviunI8dTczFeC93Stz7sFBlai-24qGhJLISkBSnNYY3ZPGYcByZOzWyIAJ5T6SK-AYIxKwjzMdDr9s4iYBm93w6z9NgQMV8XOXOXVqUw_KZ7koF8wzp0DFkB-NKn-UOPtNuAWPXXl1QCcRI6FZxHxOBYWKLfgx-6Oh7O1hiVd3wXC4g8AWif80DSQlHKCF9jjWwFUKAImPHhvLvOOuq-fmGLx0l9_dLWoXhpWuXP3hzQNDzdmg6AiA1JjRC5nZqjsXnH5Dj41YkNsIR-3Y-roVG4UcA6E0FlmbudR97E-fimYTU7Be8oiMTy9U1jIN3T7qsU55tGrHJnZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افشاگری‌های احسان موحدیان، تحلیلگر مسائل بین‌المللی
یک لابی قوی پشت دیدارهای پزشکیان با الهام علی‌اف است
بیشترین خصومت را با ما آذربایجان داشته است ولی پزشکیان زنگ می‌زند تولدش را تبریک می‌گوید</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21647" target="_blank">📅 11:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21646">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ:
شاید در هدف قرار دادن رهبران ایران زیاده‌روی کردیم و باید در سطح اول یا دوم تنش‌آفرینی متوقف می‌شدیم</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21646" target="_blank">📅 10:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21645">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بزرگ‌ترین صادرکنندگان و واردکنندگان سلاح در جهان</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21645" target="_blank">📅 02:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21644">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyNuzRZPMfDG4esMLTcbQs0PYQXCMilsoCi-ma2GjHgLEU0sqGjsDCP2YfI6Ohv21hqsqvU1lyY8g1449rVJSWwl8P6parOCXgOVZBQ9gOMeTQZPSTB_zQArBl7ybdOZREK-KETnUfEC_l_cjSDXhvzf0CuuaHs3DwUVS2u9U-7IZeERNuvlFWO3zqC1Bqev-ICbKi-Fcyi9ccCNEo3HNQwTR7gva_MlMaY4uMX_Gx6tOLXiAyv2awpOsvjkxQIn20a8VJHUlhQQwYllxKXTjdbNXtsLOzp-5IttNKwxBLkigaX4Wun9zotlwIVdJERH5RG4RXKW2Jx9kHHwR9lQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین صادرکنندگان و واردکنندگان سلاح در جهان</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21644" target="_blank">📅 00:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21643">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soDB-oBDZ56SMTyY4e_eU9uY_ClTnEsAvD7mTWXbvWmFweSaFnlZS7ZiSEIC45rxQFAGwrxDB7zYFWACmMFLPXw4zRGjPgk60e0XdlPKqsyl7nillFm4l6H4jw2qnrstGqNgnYc8Vv-1XmUbPFNUG1OjIP2jf-wUK9fdcnHv-890kZS2i5CW6Us9IGFjczYnywbeP6tJKtR9o4FfS8OlgQSpgecSUqWTBbXoMITl9u4YWYPAKZHWb701sGoahjypl7FM91vtOYwegODrLxV_8RqhyAw1SyZRerD8IrhM8CscDwB7OwatzWrwSe9jAlaZCvmMAXuUT2jHYaU8fucXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ ایران هنوز تمام هزینه اقتصادی خود را به جهان تحمیل نکرده است
جنگ ایران و اختلال در عرضه انرژی می‌تواند با تأخیر، هزینه تولید، حمل‌ونقل و قیمت کالاها و خدمات را افزایش دهد؛ بنابراین، آثار تورمی جنگ ممکن است هنوز به‌طور کامل در داده‌های اقتصادی نمایان نشده باشد.
تداوم این فشارها می‌تواند بانک‌های مرکزی را به حفظ نرخ بهره بالا وادار کند و با کاهش مصرف و سرمایه‌گذاری، خطر رکود جهانی را افزایش دهد؛ تورم غیرانرژی، انتظارات تورمی و بازده اوراق دولتی از مهم‌ترین شاخص‌های قابل‌پیگیری هستند.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21643" target="_blank">📅 20:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21642">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ در حالی که به توافق تأمین سوخت دیزل با مسکو اشاره می‌کرد، گفت که اتحادیه اروپا ۲۵۰ میلیارد دلار به روسیه برای نفت پرداخت کرده است، اما رسانه‌های آمریکایی ترجیح می‌دهند در این باره سکوت کنند،
او همچنین تأکید کرد که تنها در منافع ایالات متحده عمل می‌کند و به اصل «آمریکا اول» پایبند است.</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21642" target="_blank">📅 17:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21641">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔹
شریعتمداری
:
درصورت جنگ مجدد کابل های اینترنت و فیبرنوری تو خلیج فارس را قطع میکنیم تا علاوه بر اینترنت ایران، اینترنت کل منطقه و جهان قطع بشود
﻿</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/21641" target="_blank">📅 16:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21640">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سومین تانکر در تنگه هرمز به دلیل عبور از مسیری غیرمجاز از سوی ایران، به یک مین دریایی برخورد کرد</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21640" target="_blank">📅 12:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21639">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♨️
سامانه دولت من در پی درخواست افزایش ۵۰۰ هزار تومانی کالابرگ مختل شد</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21639" target="_blank">📅 12:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21638">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
حملات پهپادی اوکراین به دیتاسنتر روسیه ترافیک بات‌های یاندکس را تقریباً به صفر رساند
▪️
در پی این حملات، حداقل ۸۴ سرویس ابری یاندکس از کار افتاده‌اند و ترافیک کلی شبکه به شکل چشمگیری سقوط کرده است. این عملیات در پاسخ به حملات موشکی مسکو علیه زیرساخت‌های فناوری اوکراین انجام شده و کاربران روسی را با افت شدید سرعت اینترنت روبه‌رو کرده است.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21638" target="_blank">📅 12:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21637">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♨️
سامانه دولت من در پی درخواست افزایش ۵۰۰ هزار تومانی کالابرگ مختل شد</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21637" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21636">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGOWNrZ6HIfyF-jgxJDKfgy88lbH0q3XkRVOucFYmHO9IYGmoE3i-IGLM7UVbNApJZ9dw0zmkv6lzwJfshgZbUIFVtl-K-tPdn6RorWC-oP6kqqjocunED1B1Qt0BX9u-8DInoBk_GgqJn2rhGowgREQ2iDWO1ze4yKmvKLy_pMcqVZ4vKibUZmQTsojHH-a_U-RVG2cjTWL3X9Y1y2nzJ1vItpXtUoke_EYtE5GRuteefhTc1RGzpj7O3UtXfeN-BJNdeeUG6CwVWceWuEkYismTU7bfByK659f7CYZ_lCZXIGOhCFVVzhjSAlsFN0JAS5vB7ussAahXZfDDI7J6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
— M15</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21636" target="_blank">📅 11:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21635">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P23AyJ1MkN6ISBwGjn-6pXV4nWDqsgntEp_tT_9zC9HH5_E2SjqWD86rmMH7dFh-Z2uUHrK_wBrsXjN3MV6Dgj1ZN-B-0DsS5wiUEfJ0oug4CIwnb7yWPkLX1irA0kvIZDLKvRaMotoNlntepaFGtcyL8JoI0Pw00sYRVa1zpsp_knohJOBDqzRxpr3iC1Qbh_GeQypNR5DcJ537bmVJVU7xXQElympRfzF2oCnYP-3Kbtle3uG74shCDqX2KSyl6rGWrIT5sE2dFDuZFGPUJr6H3R34BcmwaSXyq_f_I0YBR_efuzSGh1Jgu4J5vVh0WqWLMNAWehzUrLDmDNM-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD
— M15</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21635" target="_blank">📅 11:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21634">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjbNLg6-odugW-SFYcPrVkkrvJepJZ0M-6R0vkgNjKORbDIJXMIKO0tYW8P9zeCccWN12Nhc-M8XFppNwjcKvfnKsNbjTeFD8GrEYqB3q5lWJgB8cDYJKZnAfF3u1m4dEDnPYHzAeye_B3P1s1cxi5hQGHoIWqDw86beE9TADJrcB8gEgPJDr68t6isSgtJ-wZGWsHOt4j1bSanB2ZC2WaIbuyb58WvdiQ0vvCZpACj0W1EsrZSmN7PgASx94ERRQTWRHRkkfqajls2JehwUjqIYtEWSELypKxHyFYAA2PnrZ7y7kqlMnz9M1cTG1gGiUvdkevCzrm3PC0tFgMnqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC برای امروز نزدیک به سطح قیمت منصفانه قرار دارد و سیگنال خاصی صادر نمی شود.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21634" target="_blank">📅 11:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21633">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_hHZbCHWRHKQfcj7CnYx8hHFW8bYv7lUocAwfwQ2keJThlqcmBf6sC6q3K9ifu2MGwJyV-ZSkHH2y2PxwJdN_T_t_7sWsUxXzg4GD5mShtWktpuFspZMyLrHAMXOCxbzj9KQmrliApNmABd7-q3nvuDwh1luJFU12xa9HbxjxckR8xRegKSuED1AKcVROdb1iibGa5ar9WZIL8VjJWW_EAycgjz1PqTLzZ4fpX9zN2ZskrnYE47ap7grGBooutXMOLuq8qvAzGqDMluBtXj2XD6butweX1dClpJPtff2uCn5KX7mf_q-hKmmh9noNTOoZdpEq5ItPQ9FzKFd2dh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد.</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21633" target="_blank">📅 11:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21632">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اخبار فوری: چین اعلام کرد که حملات حوثی‌ها به عربستان سعودی را «محکوم» می‌کند.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21632" target="_blank">📅 11:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21631">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">توطئه در کار است؛
توطئه بزرگ در کار‌ است؛
توطئه ها در کار است!</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/21631" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21630">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اوضاع یک جوری است!
زینب ابوطالبی می‌رود اما بیژن مرتضوی برمیگردد!</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SBoxxx/21630" target="_blank">📅 01:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21629">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbsxJGAqheJI_ihK72zdGZWfwtCLkL4fm6t7QtsXen4vBoMy1DcEkkj4EZOUgweLfRQhsXvnfC9a0yz8YOx9LHg_5aNWut5XOJAWOUg7a5xWSLIc1F_2Z3FkDKGJnfOLaufPED_peBchxuDGuul_QlOlf7hhJs8m85yvuTNnCdbZJvVw6YQmGhId9NQX85L3i8o157QMb8J-5JLEhymj70ZJ4ikxsF8EohKPNaOsFPT4CeQaS7VHweS6V9-B6SiOFMx0B9gIx8LyW-ItmPehEn6_xZ0hQyiyW4OpATtESzrGAf5j-7U2mp79QiGm0uQt7YprKB9KnuWNPjP60EA4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SBoxxx/21629" target="_blank">📅 23:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21628">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja-GEcyQXUIx66hbLxPxmAR9TTTxVXi7505q0MtZI8jv3LDXaelpn6cpKBbWAQEg13RCpvqPc72lsNjdBrK2Lo7RccoJPgA3rr_y1-aQ40QUZ_yi0YQLjOFgZc7RaTeR5KOVd2IV-lbDDxAEwLl--GDIQ_xBajfvoMgPSjYn0C95q23aj6MOec2HSO4xmu7z4o8m7HYSEiD4UoTPNFLDmekdTrCXK8vHhRBrCVBp2cpGMNN9-KgRugqJB08vK-x-8YpivQ8crCUo9vnBpMoJNXL_KuW1npYUGdxV_s4zQX8qQCm4L7fRGyfxQgSVnfAhchuJMmVZ6DHHEMk4ubLjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کری خوانی سخنگوی سپاه با استناد به «سلحشوران» اشکانی و ساسانی !</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/21628" target="_blank">📅 22:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21627">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیروی دریایی سپاه:
دومین سوپر نفتکش با مین دریایی در تنگۀ هرمز برخورد کرد</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/21627" target="_blank">📅 21:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21626">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محسن رضایی  رئیس‌جمهور آمریکا، ترامپ، و فرماندهی مرکزی ایالات متحده (سنتکام) متهم کرد که بر یک عملیات قاچاق نفت در سواحل عمان، با کمک نیروهای نظامی امارات، نظارت دارند.  رضایی ادعا کرد که قایق‌های کوچک نفت را به تانکر‌های بزرگتر منتقل می‌کنند و نیروهای ایرانی…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SBoxxx/21626" target="_blank">📅 19:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21625">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">محسن رضایی  رئیس‌جمهور آمریکا، ترامپ، و فرماندهی مرکزی ایالات متحده (سنتکام) متهم کرد که بر یک عملیات قاچاق نفت در سواحل عمان، با کمک نیروهای نظامی امارات، نظارت دارند.
رضایی ادعا کرد که قایق‌های کوچک نفت را به تانکر‌های بزرگتر منتقل می‌کنند و نیروهای ایرانی از چند ماه قبل، هر شب، به پنج یا شش فروند از این کشتی‌ها حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/21625" target="_blank">📅 19:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21624">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1cYAKs1nZdYjOqu9h0rgo7R5v47Q0b78v1g7ngkNlY2GVu5eUT3Xg5is_W-nRlapnXLBaaSBt5E50LmWcR94nTbXCz5Ky-SIZ9URLptB8B5GG2rtJQiUq3Bpci0JpTDF8RqovQ0zvQHMXI_4ej38ohVexbUOnO_3KuoKu0J13gFy4cwWVtQqfbik4VRRNNzJ13zg28laoQR-YeDBqwz6PcdAI3DT8cXpoORjNg1-qhFi-sUxNY7RYN7yvn1EqrjXOCV76gNj6jeeSay_pB5Rxi4l3H8ASvC_GgK9kuzAZHiH5Hb3QxyYiKYyld5K430oQd4WKvW74OrLoGrzgTe-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ دال بر آغاز «آتش بس انرژی» میان روسیه و اوکراین</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SBoxxx/21624" target="_blank">📅 18:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21623">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حمله دوباره حوثی ها به فرودگاه ریاض!</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SBoxxx/21623" target="_blank">📅 18:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21622">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔹
سرلشکر محسن رضایی ؛ دبیر شعام
:
تحریف کنندگان تاریخ برای تکرار شکست های باستانی از ایران آماده باشند</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SBoxxx/21622" target="_blank">📅 18:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21621">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
عزیزی ؛ رئیس کمیسیون امنیت مجلس
:
کشوری که ذاتش با استعمار و خون ریزی است ، هخامنشیان را که خالق بیانیه حقوق بشر است متهم به جنایت میکند</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SBoxxx/21621" target="_blank">📅 18:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هدف قرار گرفتن یک نفت کش دیگر توسط سپاه</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SBoxxx/21620" target="_blank">📅 17:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شلیک موشک از تهران</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SBoxxx/21619" target="_blank">📅 12:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21618">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرگزاری یمنی YNP به نقل از منابع آگاه:   عربستان از چین خواسته رسماً میانجی‌گری با یمن را برای اعلام آتش‌بس، بر عهده بگیرد</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SBoxxx/21618" target="_blank">📅 12:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21617">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرگزاری یمنی YNP به نقل از منابع آگاه:
عربستان از چین خواسته رسماً میانجی‌گری با یمن را برای اعلام آتش‌بس، بر عهده بگیرد</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SBoxxx/21617" target="_blank">📅 12:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21616">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
ایلان ماسک رسما به اپراتورهای موبایل اعلان جنگ کرده است
♦️
شرکت SpaceX با یک قرارداد ۸ میلیارد دلاری، فرکانس‌های رادیویی با باند پایین ۸۰۰ مگاهرتز رو خرید
♦️
ویژگی این موج‌ها این هست که به راحتی از دیوارها، ساختمون‌ها و درخت‌ها رد می‌شوند و گوشی‌های معمولی هم از آن پشتیبانی می‌کنند
♦️
علاوه بر این، مجوز ارسال ۱۵ هزار تا ماهواره نسل جدید را هم گرفته تا اینترنت ماهواره‌ای پرسرعت را مستقیم روی گوشی‌های هوشمند معمولی بیاورد، بدون اینکه نیاز به خرید گوشی خاصی باشد
♦️
ماسک دارد کاری می‌ کند که به‌ زودی کل شبکه موبایل از روی زمین به فضا منتقل شود</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SBoxxx/21616" target="_blank">📅 11:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21615">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سنتکام از هدف قرار دادن یک کشتی در حال حرکت به سمت بنادر ایران خبر داد.</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SBoxxx/21615" target="_blank">📅 10:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عربستان از ۱۲ کشته و ۳۰۹ زخمی در پی اصابت موشک به فرودگاه ریاض خبر داد  سازمان هواپیمایی عربستان سعودی مدعی شد که در حمله موشکی یمن به فرودگاه ملک خالد، ۱۲ نفر کشته و ۳۰۹ تن دیگر زخمی شده‌اند.  ۴ نفر از گشته شدگان عربستانی، ۲ نفر از بنگلادش، ۱ نفر آمریکایی،…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SBoxxx/21614" target="_blank">📅 08:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SBoxxx/21613" target="_blank">📅 08:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عربستان از ۱۲ کشته و ۳۰۹ زخمی در پی اصابت موشک به فرودگاه ریاض خبر داد  سازمان هواپیمایی عربستان سعودی مدعی شد که در حمله موشکی یمن به فرودگاه ملک خالد، ۱۲ نفر کشته و ۳۰۹ تن دیگر زخمی شده‌اند.  ۴ نفر از گشته شدگان عربستانی، ۲ نفر از بنگلادش، ۱ نفر آمریکایی،…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SBoxxx/21612" target="_blank">📅 08:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۶ کشته و بیش از ۱۰۰ زخمی</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SBoxxx/21611" target="_blank">📅 08:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سخنان عبدالله النفیسی از کویت و وعده اش برای حمله به «صنعا» و پاکسازی آن از ایرانیان و مجوس‌ها!</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/21610" target="_blank">📅 00:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21609">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">video.mp4</div>
  <div class="tg-doc-extra">1.6 MB</div>
</div>
<a href="https://t.me/SBoxxx/21609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SBoxxx/21609" target="_blank">📅 00:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21608">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گویا تلفات غیرنظامی بسیار بالایی گزارش شده.</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/21608" target="_blank">📅 23:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21607">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">روابط عمومی نیروی دریایی سپاه پاسداران انقلاب اسلامی:
یک فروند سوپرنفتکش متخلف حامل نفت خام، که قصد خروج از مسیر غیر مجاز تنگه هرمز را داشت، به دلیل برخورد با مین دریایی از مسیر پر خطر اعلام شده، دچار انفجار پر شدت گردید.
این سوپر نفتکش که سامانه های ناوبری و موقعیت یاب خود را خاموش کرده بود، بعد از برخورد با مین دریایی در یک آتش عظیم در حال سوختن است؛ به گونه ای که برای مردم ساحل نشین نیز آتش آن به وضوح قابل مشاهده است.
نیروی دریایی سپاه اعلام می کند: آتش سوزی مهیب عاقبت هر نفتکش متخلفی است که بخواهد امنیت و قوانین تنگه هرمز را نادیده بگیرد.</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SBoxxx/21607" target="_blank">📅 21:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21606">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آیا موج آبی دموکرات‌ها در انتخابات میان‌دوره‌ای آمریکا واقعی است یا خطای نظرسنجی‌ها؟!
با نزدیک شدن به انتخابات میان‌دوره‌ای آمریکا، نظرسنجی‌ها از تضعیف موقعیت جمهوری‌خواهان و افزایش احتمال بازگشت دموکرات‌ها به قدرت در کنگره حکایت دارند. با این حال، یک پرسش اساسی همچنان مطرح است: آیا واقعاً شاهد شکل‌گیری موجی از حمایت انتخاباتی به سود دموکرات‌ها هستیم یا بخشی از این تصویر نتیجه خطاهای ساختاری در نظرسنجی‌هاست؟
بر اساس میانگین نظرسنجی های  RealClearPolling، دموکرات‌ها در رقابت سراسری برای مجلس نمایندگان با اختلاف قابل‌توجهی از جمهوری‌خواهان پیش هستند؛ به‌طوری‌که سهم آن‌ها از رأی عمومی کنگره ۴۹.۸ درصد، در برابر ۴۱.۹ درصد برای جمهوری‌خواهان برآورد شده است. مؤسسه Cook Political Report نیز پیش‌بینی می‌کند دموکرات‌ها بتوانند بین ۹ تا ۱۹ کرسی به دست آورند؛ نتیجه‌ای که احتمال بازپس‌گیری اکثریت مجلس نمایندگان را تقویت می‌کند.
در سنا نیز شرایط برای جمهوری‌خواهان چندان مطلوب نیست. برآوردهای کوک از احتمال کسب خالص 2 تا 6 کرسی توسط دموکرات‌ها حکایت دارد. دموکرات‌ها برای کنترل سنا به 4 کرسی بیشتر نیاز دارند و رقابت در برخی ایالت‌ها، از جمله کانزاس، اکنون بسیار نزدیک ارزیابی می‌شود. هم‌زمان، محبوبیت دونالد ترامپ نیز تحت فشار قرار دارد. بر اساس شاخص نظرسنجی‌های کوک، میزان تأیید عملکرد رئیس‌جمهور حدود ۳۷.۶ درصد است. در نظرسنجی اخیر اکونومیست و YouGov نیز تنها ۳۵ درصد از پاسخ‌دهندگان عملکرد او را تأیید کرده‌اند، در حالی که ۶۰ درصد نظر مخالف داشته‌اند.
با وجود این داده‌ها، نمی‌توان نتیجه انتخابات را از هم‌اکنون قطعی دانست. سابقه نظرسنجی‌ها نشان می‌دهد که برآورد حمایت از ترامپ در انتخابات ریاست‌جمهوری سال‌های ۲۰۱۶، ۲۰۲۰ و ۲۰۲۴ با خطا همراه بوده و میزان آرای او کمتر از واقعیت تخمین زده شده است. هرچند نظرسنجی‌های انتخابات میان‌دوره‌ای معمولاً عملکرد دقیق‌تری داشته‌اند، در انتخابات ۲۰۲۲ نیز برخی مؤسسات حمایت جمهوری‌خواهان را کمتر از میزان واقعی برآورد کردند.
یکی از مهم‌ترین مشکلات فعلی، کاهش نرخ مشارکت در نظرسنجی‌هاست. شواهد پژوهشی نشان می‌دهد جمهوری‌خواهان تا حدودی کمتر از دموکرات‌ها در نظرسنجی‌های تلفنی شرکت می‌کنند. بنابراین، نمونه‌های آماری ممکن است بیش از اندازه تحت تأثیر دیدگاه‌های رأی‌دهندگان دموکرات قرار بگیرند.
نظرسنجی‌گران برای حل این مشکل، از روش‌هایی مانند افزایش وزن آماری پاسخ‌های جمهوری‌خواهان و تنظیم نمونه‌ها بر اساس ویژگی‌های جمعیتی رأی‌دهندگان استفاده می‌کنند. با این حال، این روش‌ها نیز بدون ریسک نیستند؛ زیرا فرض می‌کنند افرادی که به نظرسنجی پاسخ می‌دهند، از نظر رفتار انتخاباتی نماینده مناسبی برای کسانی هستند که پاسخ نمی‌دهند.
بنابراین چنین می توان گفت که در شرایط فعلی، احتمال از دست رفتن اکثریت مجلس نمایندگان برای جمهوری‌خواهان جدی است و وضعیت سنا نیز می‌تواند به سود دموکرات‌ها تغییر کند. با این حال، سابقه خطاهای نظرسنجی و دشواری نمونه‌گیری از رأی‌دهندگان ترامپ، عدم قطعیت قابل‌توجهی ایجاد می‌کند. برای بازارهای مالی، نتیجه این انتخابات می‌تواند بر مسیر سیاست‌گذاری اقتصادی، مالیات، بودجه، تجارت و روابط خارجی آمریکا اثر بگذارد؛ اما تا زمانی که داده‌های معتبرتر و نتایج انتخاباتی در دسترس قرار نگیرند، نباید سناریوی پیروزی دموکرات‌ها را قطعی تلقی کرد.</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/21606" target="_blank">📅 21:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21605">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">در ابرقدرت چهارم جهان؛  — برق به دلیل ناترازی در گرمای تابستان قطع می شود  — گاز به دلیل ناترازی در سرمای زمستان قطع می شود  — اینترنت هم هر بار یک شلوغی یا جنگی بشود توسط خود سران ابرقدرت قطع می شود!</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21605" target="_blank">📅 21:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21604">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر ارتباطات:  در صورت وقوع دوباره جنگ به دلایل حساس و حفظ امنیت کشور مجبور به قطع اینترنت هستیم اینکه در چه سطح و چه مدت اینترنت قطع شود مشخص نیست اما به احتمال 90 درصد اینترنت سراسری قطع خواهد شد</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/21604" target="_blank">📅 21:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزیر ارتباطات:
در صورت وقوع دوباره جنگ به دلایل حساس و حفظ امنیت کشور مجبور به قطع اینترنت هستیم اینکه در چه سطح و چه مدت اینترنت قطع شود مشخص نیست اما به احتمال
90
درصد اینترنت سراسری قطع خواهد شد</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SBoxxx/21603" target="_blank">📅 21:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چه بازی شد….   طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/21602" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
