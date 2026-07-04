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
<img src="https://cdn4.telesco.pe/file/CbzMCmJjDOCNaSePphkJ6U9S-cUs3MFBNxJzuLzYKmnlL5X-c5DgfvzJy9KBYQnH8gqsyu6mKSd0QdOSQ-zfm27lf9ZosICPQ9SEManGfst1ft_D7yOKzTCbVt3fqCBynC8LQiYJEQ5DbAWGbfPw9Yxcq8GwgZ_zhYABpWhDpjAAzipbPy8-cmxYJIHT5mwYjqAb2gCdhx0LXMquFwh5ZUSCCCZIQLmiyE9w08ppRGQrqYfWfaRweyI5CPS8Hj4Z0lgLYtLUUMq5eQcDTafGFgZenuRb2YrEieWl3OFDr6kYvY1braPpUoQIdNJ_8RxXxfRCAPQ2pvviRsbqXzro4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 08:31:44</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 277 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z65uu2iS4_-jnf66_3KtPvYBefeVs1JVCWlkrVPjdMkaZkcSaO4pp_fxDgJnzqbss1WYLjLYrwi5rh1-OmwABghbDAnCAXpOkZMW-V9JnMsFsZFvk8fphZcK5mkYY539lN2lDGN5jlfDnxA02n3ChcNtvOPovnJZsK4MzFswrDFwb01eRHKZJL9UR6JWccqxdFUucqqCtiSA_vRMLiGio03OkwjwqWvogAJRo2iyuKz_Izdwg8HLffT5yj17qqTYR3wZzXrhAUYyrHpOc-ETt_QyeEmcJE6jx-92K3qy7OVa8PCPnPi1qTuCFF309-zxi6ccvq7LYJLVUL1DFkZc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 507 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 753 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=j2PLq1MBE2zEbh1omKXknQuKj61KVaNc1SmxSQrVQZJ4IfJJ0_P9dftfRZjuFfq-8puVL-vcyjeMYjAWUa7u_3KQH88UOMxLxdDCns91vDlF_6QzGh0z9FgjJWVt6cm2CwMEMF_8lL7RDAhCNcnRtXt1C_vMOJTPVV9l-moRhbineTUAkLxGfLTN5dLmD6mTLaOtuPWoy3Gz7mPxpMBOkCxZ3eijQrcus3mtrfSbZsedE7QytKUBsSbqvB3FKxq6ulWzbN1MmXpMYQIMVoKzzLgoGJRBiIA0UWK1-1Bvn572OBLt4UWeC48MoMR_fMDeCYCrspf3jYdAFZXUy4kJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=j2PLq1MBE2zEbh1omKXknQuKj61KVaNc1SmxSQrVQZJ4IfJJ0_P9dftfRZjuFfq-8puVL-vcyjeMYjAWUa7u_3KQH88UOMxLxdDCns91vDlF_6QzGh0z9FgjJWVt6cm2CwMEMF_8lL7RDAhCNcnRtXt1C_vMOJTPVV9l-moRhbineTUAkLxGfLTN5dLmD6mTLaOtuPWoy3Gz7mPxpMBOkCxZ3eijQrcus3mtrfSbZsedE7QytKUBsSbqvB3FKxq6ulWzbN1MmXpMYQIMVoKzzLgoGJRBiIA0UWK1-1Bvn572OBLt4UWeC48MoMR_fMDeCYCrspf3jYdAFZXUy4kJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 768 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0qLMtsPs9KnnFjNUNVr2gKyT2eufvBPD8VzbgvC4vVg6HvNpxfRhniASggqqVJdBdHAMm7KpZF_w7vy3yPK7ghnisPsp-zFglo_etzLpLKSyjMlEBSxlII0FsCWBAE1QG23eCWr3Gvgx7Dt5CiqhoZNowSF6tti_SGaZw3Z7EvwNJBQV15hXkWYUdsKm8MtGRLkp2Z6BdgAgWm25klrpOHENz3HYPjuzlv5nmUM1bHta2rZ6RufhSleMULoPwuzlZQRKqGEMrZYQXXL-G2v1YjbC2teLhpdp88BC-f2-febeAZNWjyOPiMIbPTpzFOdICvgXm8AL7ELU1fKfSqXlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 630 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSi_KvGt-1c8YsgZkv9NfhC4LZEAT6Zo7ed2gPREm_cmngjM8EgOu7ERWb8thlLwykmxas44jvv5t2kbAl_fw5kBnGqm77y-5rJO1mzfZHE8ZYb9fZIKwd-oNxze5jCfxENBbCSZ-eV9TSZ-oVeFohSY0iHMtS40r5oDXJXFaHy6-hVcZl2-ZQWP0b_YgRuYFI3k4m7K8T91UWe9z00eCFoyBe8hAvzS2YWV5hqngN75jH1LZFy_nqajR0N4IEQHFYAZK6iN2e_qtEj0Z6yqcG6MI-BjXvJp_GHbfcThTU7AcoQFbHyGDpC3BpbKX9DzCTVxqGAPzgOSGWBdV3AKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 998 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1VT9tSKyWnYvX6dYZ07m0uiAqKpy8Bsn4ei60O-4UuKXK5xrhNzO6MfV-x0fWOlix8blc0aNLuY3S9eez6yz0woydS3eRtQFmtMhvv1VcBgdMNWOgy2twpzFj1okKd26OqEWVRSuTU2p0XVgx4RoiNxmNctJoL_Ool2AhLtNRrfsYT_c1zpVCruvEKkr0yswsLwCFaLzMs1dH4zo2WDhguq2T7Zv4fTy7phEXequ9eXBC8RJXams-uzJZO1Ak_qkzAb2A5VXjJzTwHuXM5L_NpGi4t1KdC25Hl30ORIXPOJlXmnnp06pi5A9JbjCCFq89lebepLhTS55h0sJSVDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb4x1_KvMeeTp0hh_LuocQ0ddbgtMr-igQsWBA2g9EP3y01fjtRAW6YlqUsslXk2fyQEG1_zowltTw5cZlGZBmpSYRRYuaKaYpzOX8HE-iEDVRrth24ipzztXFauxvbyOV_rs0hyn9sDCJVBL4hvp-R3G7jwEWjKwzLp5hJq2iOhW6FjLcmBrPfHV9l0zzGTqP2yv7Z_wqQTaz4_nDRY2-GyqZiJe4MrNNQVsTlVwglTZTVHsk2MvEG2C8VGxx7kBVdlhQLPYbuH23muBjKPZEDxgH3nbP_SuYD2tzYYCHMvjlfkjN_obH7RzCGR2DPNW6RaeeN38szDFnE_C5IgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XktSRph-r1U8lAychPlyX1KvbO-ja6186uulZwg8VyLXrcfXsWupfA5xt6yDscpvLaL-N7Tdudjwh_noYyu-h-Sm5H7r2CxyAp7cA2J1GvKQvM0i-D4ttuaLIULyawfj5z8WrFNiYJ3LTv_IrPVQP9pwKWGytXvDVdlGIpx_E2h8350U84bprgcp5rx0aqTyfNlq9qBLMP-4i6PX1hpnAntdH54bfdFot2U9cvAgiJoYYRYVxO6cjeVeVeWPOZW6VWuX0Q-lR0OSlb-sxVuVXIugWHSNgssqYMdf1I8YVoB-kCEAORP4c25lHx-_-Ax9bOHq5qdxTHWxgus32BGbQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVkKZ4G5O4_7hsF-aPDOXzaf7iJv2Ti_O_4dM6jzFzf5EKRbtIhg5L_xGowfuM2W63R35ukY3bhTV9wAKUONfzAgvLtkUERGJ-6xNCD9iin0WciLd8BhaQspgLebjgbGPvh2oUpTTPVWN41Pt0vgONSrqNXFF8i8k6xGaqhExxtRFkbGW54j9YtxPc3Z6Akar9e3t-ghOpYVf8el53EDDAPdbOfywmZHEFNU_D1FuE7-beL8l26NiO1qsC0LzvAoJTYBCACVrBnzY1s9rLU0tVHfpg2GSymPELNSwua45RLvmbl0EVpC0bSN0R1hoEoTd9qtcMP-4kJioIs3OKZ0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 949 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 970 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWZR-C-rMDxDPWGfmCfLVLYUxvw7RJBBZggsh0q6zKWHRMFiNLZ0tAoNrahPv1PIFGheafsQh_2RBLxtLAEPxFtcxqxQR9Rw0hlTIw4DwqEAVZ-tK0O_-vnACb6cWAMP_rD7IoAEDL0pLp5RzwT2thfNbl5Z-pEi8r0bjMQJaLqXJYgUSROckly_lfOdOE1SwOKGOQWgkPZYvsijIT2ekukh1EdwDgp0KZpCieeZi5AxPANlXXkpYO57w--eAHgu3MW_c38ZWRrM5Q6DyuAgNIjGoyKwhx8Y9rKnrSDEcXfC5Yu29ZpwzSBtvjSCweOWr4BwM0ljWv2G2uY_8YAkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZR4bB3ysa9nv4sdgtFHxoK1icwU9OsFog7sYr6amLMxymTgnymCp4oWXl29yrJQ4qVXXKfguJFIY9QGdrgys5f0t81zTG0GGJxetiJJuix_rXfwFNHrM4j_vqKIZZRbeLFfO0hOslvfAgQQaxiNCS5O0meliJVNtdNllxG9Appm_mWxkM_15IkOqakuc57dn5ru3rIp5M39SyVbK309ZC-BgveRr8b3-yqd93HCSKuhE43LD1YSl73-6YYtNq8mEMvWGQyS8vLyuO3__gYYBTHXE7K79xtBgb5nfGQbmOSVLrJhRFgTum9W4PW_msrxAwSyi8grL-Yj7qYhKHRW2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caVpLkO4cDsgKadu7MQerHielIwORPA4yxbx4x4pWEKThjJIq6HHjofo1SUtX14-baTRTEFqV2AzY7RBc_WX8hIhGbtnF_PlZoryklDoSjF_XjPpJuSr3kqA_FFBWbzvS8o9pKXMIlQR7d-AFvA4QyLYrfOC_UQxy-OIiu8r3LvaDa2aFXsuhjJKTbbcrrc4HDV-54Zctt2WarKrmy9-5hVNo_h7wsxnhvIbai_0PdC5voq5ne9P5KaFfgaZ6DN-KNhTT-YQ8iZcBr2wHbho6nvFlaGxKt2JJqeqvHgjpLRxWp4hIF6PNCaYhswvrfu8miSvRvERejathkZN1lEfMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHvQX5BcQqkm8K7sKtrPceiju7Sg14TDCaCh9wXJoHKM5lvBu5_SryHkYfyqfOQtUK59gFG387zajnYyIbKAm2VfOynA3cVFuGaf1Ax0-0p8FrxptEoSHTgK9In9ksLkk962VxuF5Wd-0cepzH7zLFCMQNw__5OK7IMeln54HcbY4bPDGtBhodDFnOIluue5cw1udX2YKXPaKkWr5SBfDxcSKhvAqqsWFy5bqC_ja8rYPYdaOvAczxD0bpH4T4QHmx2-sfatw_GILzNAKCPIndDtmapY_1h3QQOeku-e_mRvNzJN77PN74gtLnEUCB1PLljYSuWDIAbCpGJdmivHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 840 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5-uTvLdqqarQ2YA2lQ3G1qzfXsJBySwWz-Cf3G2_Qpif2h_c9p_LTPwcLW-89HqXgnQZccqrRinK8kzIZCW3P-6aZvLO0lEQvXGVobw3zRIdEqpeBxxhD3Mce4cWL8lfTGIjF5c9QS7vmnTT6IEWinDKpjAgF93fxqhHezpptrDc6w_ZQS8QIKx9K_UxFZsDp5XYHZ7HTClY6X7iTI-v63FODWPUCHAh04cErmhLzV0t8fjANoYzfDtiWMI7aJwwmGIm9eNcFDKTp4vFe375gd_B1CKRD1JVdZ_Dp0kc5ATLdFfF_0PgsXhfHVAt-SQ_fQlyxUThGF3Pa8j_Ug3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 834 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEvtJtZCAN__GBAt64BlV5jBUDDD4llkEXy3A3nZXfX4GUsTlmOd1dkPDAyahfHGpxFzv_zS--mHOcYoYiUmPlFMtcQJ7AhZncSxSxGK2nH1CrpI8fNd5z4FUgW4L1jGNhK0XwjDtHme_WMFlw26QlHhBLKai9usKc4IE1zqZrwrw48oZfSNMbEKuGpMHmGf0KPKCqqHDzTdSrkpVjdcwNzNfO5zklTNE-6u-BrjMxTjOjV_-Lubqf5Jfo9mIyDKECMx3fv0FVJNmnY0-XPpf6CJYfGPrU2uSdaJ9B545_Z0gIcNBBK35LuYLP0OlLURnOqbH9GBXnUs2-XlPlqqWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 855 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 689 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3DFrHa1acYJTThjAJiWT3eIBacktmGFl0RlMAfEx9Km4MRhB2dpNxvwsbA6ftoHXB7z7r-HD2ffshV-JIqkTb63n2-jq0j1XDtR6_EylZ7oxepjLi3-x09tGsDdZhZH8mD-pbyyqzqEvZoNZK9HgFHOvuHexmxZzcgqNd7sXee5o4Tzopg6JfJhM5ztUq6AM1bpp7PAuh3CFYojWHwIlAY8ORwGCFtwtO7_C-p268PHuG98sHzlZkuoV58s3KQWmjBSsTTIwH20Oo3EJcAKsCzSK6Kma500IbZr5D04K7xxZPDH-i58wmCH8ujTcnsanFVNHq5M4Nsvad0rvlPxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwOuhjdhrn7L0HczsFQaSEEsxR3upWtWR9Foobqm4iXHj5PrUkMShTfUud6oD6pe6cAmy7JNASl-wetVKRI9FXyK-x6oyDCEick9cPyl6uR4H_cQ6BnAF0ZsGnxHiEVI1ohL8KlxJi_6x6FuoFAfCPKR3zr3umCGJqhnEolgGlkt-hEMjxr4DBkAVVDIbfgTslPeSQ_vf0yR_L-WBmnP8Qlxh68FVFKe4QyVVLsfQvzdoajLSOl6m1BTFoDBQZWINly1w5nW2egvgeol8lM2K35BCHxycDRHkfnG9o-W0mh0qHC4Bbx0PTGKv5NiVM6XkFun4zwg8DIu8NQNFIALjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lngdCXonLAImHZTax52kx_8vHAZ-L0qRNKbic6EPOA8MOg6jgOEi2zQ4cQeLqQ-3uQnC1eT1TkXec8Tbnk9AzNPJQFd-ZPqYym8ciTZz5W2wNHPt6D1i6JTElMbS10dISipc5eh9wGwnYZy3sSyHYwNZwaTetnEnf6zLRK4S448stdHDOlN1HkaSbeZpP8g4PZ_Q2_s0hPlEEuHL23KPcDM162oAVyU4ti1lYNAQnreRCveCLofiSj2rCESVNEVUEIf16U-Ga0z_xwqYVhD_Ek6yBf8Y5uJXLTEz-5HJ81AQy45kCVHV00DgUtHWjHXffVWX8DiaiLPVI4ddLeKIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaAIbVswDKgWOvDsrWOVWz18PcZcQL9cNF4A_u_Vh2yCkPZhFFAmvbsN8MJiruuDbGNflnrytMXVUO4JFj7CEUuLQsQDXF9kY7dQ8QzFhPcLZ7l_p7PKYYecr0IoCBlN7VxnupjlpqaCKaVw6lBuSEcWMwdWhIaN3nwVcKoR0qTIhhDuwxkl9Mmnj_JDF136IbuxwwCf_zvq-G9I4H0wUNaI1rKCMexHx-lCwZPlZ-5Q7OyncWqrLag0krc5vh6UpO_puOKBtKJyVVzJHFI51qDqMpb1p6tKRfctR65zIL_tz_7gHN_N46DppvjtpwNYiU_NEazgBb4bbDmb-Ag8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/og1I9qOEIA1kjAt5zvVJkWdMFVQaU697j7ZXk9amgfTRW9ddcnghGYWzvPQbFRNNAWUOEMlmaeuZHj_ZnUOzu8HEH0A4m7opYyfXObzAwEpqiBcG7-2jh2cUEKhu6tL9TZu0DndK4xBObXYsnFutNqdB4_y3YruSDO8YT2mkTmrceEs2MGO5j7wKfQsqGLUcBeOrQe7vseBeJVPeC5D6Yi1zvr-Qh6HgrmKiuAR8qTQo23ydYcbjZLTdyadZR8zTe9R9qZoFDONqNz622fvd1qbAkSEd_yqsdNeOuzzDAk9JQK4HvCjG0YqNZb4mEfwyu8Sigwiw_F-3ujc7Tom9eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE8gh9g9S7WD30n4U3RCczhQJCZcZRW8WcHDUGMJmE05DOiNXVpGAblQQJ298UU9dXdHglpYepLA9al8tRsKGd2tgtbhCmyxzQwlwGksAIWr5WcqyIg8XYS27EjASheNXmU2t4To4qkzV3u3sAytckgSFSAnaZ-5d44g68e9Ffn7J_WpJu3xX2-a5eI9moXogNtwjUXpL7Xj90HgmVOqdoWz70neWSr_oX5GZMskreCk8KOdCPHlCn-U8FDN4CbRAgbk3h-u-_wT1LPEX-RGDjfTbtHzVAwyOn6YV6Zoo-YmO-1Eq3OvzibkZ6MUbmfGee7__J_osg6Hyy9geVig1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=MvpLatPxkAZy-nSpvFqlSzKIUxz_JON75o3f_yg9JYkMOQpDcn9mBccmYI2z_5GryFE8m8IwW6zFO5X6sJhUazK5ins9IjEK6dYj_TmXThcdoLuzhZVHZdPc4kBae_d1r7L97uXN9447yuyetLMe-Hx0yxHohgIWxGQE7JJJNBN5CZ3IeEqHjhtyZihJ5hAoHc3NtzvpcOJyW0epntrwJRwblO00yGbRBz2QQhZzXIJhPooPtWWTs1kp5FI2pFzlnGuPCSdsYNFtrKJLYrvGjQHYHlvbKghxUCaPI5MyQFrWa7BaONXC0QduSE42TgYWGytr61ga4G75besQSRjKXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=MvpLatPxkAZy-nSpvFqlSzKIUxz_JON75o3f_yg9JYkMOQpDcn9mBccmYI2z_5GryFE8m8IwW6zFO5X6sJhUazK5ins9IjEK6dYj_TmXThcdoLuzhZVHZdPc4kBae_d1r7L97uXN9447yuyetLMe-Hx0yxHohgIWxGQE7JJJNBN5CZ3IeEqHjhtyZihJ5hAoHc3NtzvpcOJyW0epntrwJRwblO00yGbRBz2QQhZzXIJhPooPtWWTs1kp5FI2pFzlnGuPCSdsYNFtrKJLYrvGjQHYHlvbKghxUCaPI5MyQFrWa7BaONXC0QduSE42TgYWGytr61ga4G75besQSRjKXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaETfuuaiLkY7QRmlvZHiI7AcA6Megj04Z_ZvWU3WfuNIP8YV76kR_ED26hS-VyjZV_yx30fr4aZX0bdbeZGFegteE8qrh10-0f6e3acaIDANMZFtrBZZCEpHDI2kUtzBjsw14nj1cusELwnV3OSwC0r4wBZrBSZvGGFAGfpOt2yuwrdTS5rijSCc9_Kt88mvlTfN3xKsU0tMOzEGSI_FUxeGx-ojdDFZIWLozwMb9W1Tuvdd2jUk3KaliC3c9XZNCJHBrqNTkDKtEnqsAk2tM49wJSDArN2Gm0MpGKyd35f7waxSuZWpswVF1alp6UAP6i6McIb5AaGEpTkro_WWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 934 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjzUQa-W6Wo051ZTpw7vP4kL70WZjE0ZbQzNV7vf8lrZdyYARLtPPHICNvAqSK268DWEOszsVdk8yYK0S345sqrSLWm9M9TYGJKxtySZvFVwgI5AGdZSQml4_eWql9JIWmb1e0yipzUkBuk3bN6EbD6BNXrXRp13YF22cwpLsPkqypBI_djkodagLMv7WAnDW79Awe5XLLo0qPB_WhOi6XQcJ_nU_eMRoxM2cZDCQxhJjpGzTe6QXIvC1T3fIUSASeNnGQ6vaIKP6GBwZoLWtlkQS0TlGMNEKYOLkWPcc-BnIr-QBToDCRb4nb_QCO7ilr79HkwHfbsw-Dsc0K87SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dM3qGfJBaiwKdqkHrLrO6VJPRynHC6xIepg638UJ_Vx3_ihY0qszPTumZ_14fD3QFxw-pa_-Mf68DTGcuDg-drr5RKS2yOBPadWdmTK5N6hsUZxcIGzKB7Gu6JO_FCZt8drJ6fn_FesYSR2qRwtHkZnUxZtFDXsjCEB0ElhR73aqqCTfK6UkwAc3yN5Z00zu75YhDYNrON41xKf-EVc18Sefy4DkVanbTlKjf_14Qo7RgG3HIQxTHFcwbfyKbtxKg9rreB_-szDT1r4tsGMcxj8nw2sBVdEtCiqAig8jtaqXgjeXW1gCeM9ApayDwoiAq-Y9b2OtCT1CFtXNS94gsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lW6WgEmzJgA4WjoIDjrkX9r93hDXnGiSxYqyc_XxX5HQe2pRbeQS-PRfdyGmScYgE3SbvM7RekLT--kcAafD7oox6wUpC2FJKnF1rMq4Dy3rQB7N6kL-enKyXrYgku-GX8L4Ri0wUPjRJLpmGmtAY62iWObbfS2BM3qmt5jLS8eo6_26Nmn1xwjWtysMRvfSgAsBQnLZ7b9-7MR16AhxT1ypwYQ9bmUSNiYFHct9xy0uhPqMnY8tEnJtSvub7tjTOlXuWNpcF55eu-xst8uBSw5NxfDjbTfk1haVHmHRiNMClGvqEMgVuhCkoP1mIJRbn0wi-HjnhfiUwPgVAXhTvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 803 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUA5c4VNbwZ5niHIojE_KyuiSRFRWG16q7xHA5me-TGqb-2ImHh3RjxkcNIjksW1FNp2Zr5hbRIVt9aM59mvDYY8hgOQ3nTTYOYcx4nYU7EMaVcpXU851tzrWYzS3oqJDA6_mGX9-B6Jn8sl4dfQ8sZwP6aRNUHIGs1z8pk5ZQ8NHHmO8KV6gYVA2GPO_KEysENUti6LkvCyxYMVyH3ongSsf1YNxB_muGV5Tr1bqzY7euDFB9WC20lNYtVovnuILVu7ln7oBMKyRaWYsNLJI1XIpr0X_3luMtXCpCDYCReRmxomm-aGiB3jHKJDKYOddcywqf9UPUxZVj3YXz4EHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ceu6u8owSU2Oi-6YWeVIUY0uu4FD6udYxmmu2YekJKEfDXjeurudhwzojTMXaiHyYW42FZORoPu2Xrkw-Chow1PFZ3LzOOYTTKTLdpavholSFpXFJOq2ug2dBN-eT8tXzquH20VkxRdgfcpJNbX9Iu3FEHn1meQkhskFq4HAyvBBIuH5sIjsjtZAll4eQgR9Lq9hzFiPqM5UTqQlwWHIDr1NQzKhGG8XdjND9sMRKV3c4ChXJOoLjpEdmpjcP6yGInwtboLiu4nUVYI5Yeg4XgLkKADyNDEFSG2ZOJGvGnDn_7KPkv_JUc4nwWYM7WmA2KCrH7X8eyN4493dxQ6g6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4xj6u6Yr6CaxEiFyApFq89rUiSbaBebq2CdPViaL53qPjscPeWjqQcGiXf8GQRDlJP0jkr3_QPrfOHNOnugm0Hj5HgyBYOCKjDhIwhMwVHHmqZQHiQkW-14bjQX1inkjSQvThSzWrn4ZrTuwfGo0705lUgJNwYdZH078gz-N6g-umOK89-cgv3FSfG5L3QnWCi6lKkpEmoRwu97icZSeQwnElLKyIOnilM2g7QDMilP28IpTcTKg4Ji6X7a3FA_4sJnEdngYhf2NXghh6Mp4hgSSJQ7GDBJGuidLhnIFZelW9wrpSU61VM8-mhYPhHG4RiN_pccjZIVhMq_rwYdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ay1wDy4hCrAE5M2d6Q_-v32pH_kslY1MujEZLWmuH5KuVlx2deMUTk6Kb9mQRPLn0s89s0ZgmHPDEDGPf9V3jhvE6tN9ebZHqcN05_l3ofeo4bea2JEdt58b6pHSl8ExG0ejhTGymnDlH7iXVgKBw-4RttePVe1VvwOTmNdPOQzh6JTenXBYINfJGbm7UouXGWn47pac-imBU8cOzBWeTaudSckZvs-k_0Y6yPsNCdPaGr9xM90zlEHVr-QzN6CTuYHV28uYA39bLGl1KYNqqY5FenUkfYRtv94EaJTUQwad7D4WCkNLEFn1SIn5qJrippSJJOnWkFYkAAnVKcxi6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 756 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjwjKVl2mtOVKwxL_FyLKA-gIte-UQ9QaH55wQZP8hElwikuyuDv3vjnYIxycexwrby3SWK_ncMyYdvaGQxpS_RBhTLCp2asI3-BWJl7OlU6_JscN1Paf_rSskq_WYIqNsbhttu-QbpNcm9pK3dyAskgY5AM2GxHUPSWVScIgKrmHPY9HKcAEmVNRLx3wU-pDdmJFWUMYqF8otzT_xM3SocI1LR_xka3kL8e9NKJhxElnJKtV8HTAlicJ-d4ObPqa2ddmY3PkJYt7erNgZmDCSp0xjRLyq_i41Kcer0ASUoXbIGJN0GypWXvtNKS-Bqkl7BHQHmXw11rfNfL0oRumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 721 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdS4bxmcNfdkXPvAjzAyH5sh9NGxenG05tyYFVPaGQwl3yCVGzz_mo6jkFSQC33xarRsI--6qUex46TFO6Yq1s2swJKS8TCZTKLTBGybPwiKyGy3mfs1rBIE8nQJ_O2qeaHj5c8d9KDcZM-iHMVcmT6oq2f3aAMupXviD87C4A3qfjq7sxAljuDPsPbk2p1hejPRu0euYh8DcnE_rdMnwkivgx85znmbIxqm7Mwc3W1zpkiaRBUCSjMe5tngwLQP9wLyXBkZz9mv0sKLclgAWC49G6YyROK1Mr-48wKp4s5zu8GD03x-x1kpKoDMOcGQiJqgeQqXcYfruZ27Vhp2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiidYbWBR9fY_Nw2cUpnAzu4sBVQWhsZ7vR9RaOrDIMuGuzg7nB3NCMHrqvyoq0H92lpO-5rDWFFmkBIyjiANiZ1WGqcy6koZ_lgYBYHouotdwrAuU_uTFFypegIb-ur3Tlf5Kg3ICl2LpGLrHGiusRubq6I0P5U6j1rG-Hj4mKOy1iI1t9IQ6sEtmXVX64k6PWWkH14K_7lVNclAo83nSzLMWlaqZRwVjWbzXFIvpThmFRaJ9vT3seu0JpTOlxlbJRho9XnlILdzG2YxDLDS6mXxLEC9EqqgD1rMjSMZ0SfRHh5YQ5WVcxhECoUoTC8rpLmgk7XMDWPH0GZ_FBjRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 604 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asWTfxr3lJlTusktzKe35FeZnq-0kAn7CD4wITRtb-cYpR2eNr__gG-ljlnSME6H2DJ_zeTs_RtFcQQzY5senxwbN5YTFsF0tz192TBVH3kFNA9t4RseXDi8IxUlQJLsMqtsFsujjSMfD-51-UPK8ca5azkGWF3C01SgcNtbSw70eeHBzWwEr0EaajXZxihRfmBDHgoPh21EzsCNdbGL-Qp6Jdy71i65CH56WrfZslRT4F0nnC7-8oXsxwAUoBMxQTWnTiX6PLEXBc3rogCVh1j8wvcZdA99wI1Z3B67N6MzAOoZBBA8jmqunUn1WWKYJxzBBbfUnY_Ml47ca4p9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfOM1F3LfVo7-npOJ1Bl5Wf25jp_VMXXNSCdwcMZ1s0PN_Pn0fEmWWipZJeAjO43iR9hCPQhp4w_xE2FVrMQsyDnPKY8GvJ2HOnxmvEJlXTi_vaUi2P134SvK8E1Gi8w2NJwEAbmaVvtB2D7CkRS0xVkEMGCzyXEFE5XYKB5USS_D-PPFEmCkBt9d-rAeZ9cZ0CTv2Iksze3g2fCUVYB38dIW9yJDm553F6b96tnz6AAEGQFtqyIRHjHSmi7zWyfsNepfA68KzscHI8fEGdS5yNcOiPBsEPZVQnm1ovH0lTdGkD91x3NQxXIqNPSZ7vNTaTfDpTL9GnCFqXwnIzh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUsMoAk8kc2y8-LHrhSUgHlZMxYvtMgO3HoY20XqjrROGQvqDWpSmuzitrJ6842PqBj-axbDG30gne2hyeMQyPatbptWWGH5AqxOox5rYOuIlvTP7DzMpkCSY0efZlNzg7LRGxXdbUJgYF1GbWIGxIpR5eiEcw_iz5Tf079blXBvqwbyJ_mPfc0FRfNiabndoPCgc1IezWhZr_8gMM7K3qvNIKb4_p1QdhlYv5qbwqEaDRDOZ1V0rlG8HTEqugYgYnuvxeSRAzu0n68AScAxJ3ZPsaEuTSjPHLrzfqKyMjm9h8OsoU_katwimzXc2AcTiRdBVsZ5fqKRqcGLRQM07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pNs1OV22mdocfvvEQE-E_wXRR5CTpTw7zaKjsdnhS1QgWS79nIhDpoCT9wzPPZNBD_0rIXhr2FvHIg6wr8SbC-dX2azRD290h812IAMxrksLZhOmAlJMd1aq3LKEzIWphMJK699RuQGS2GGQfdGeNv45Byo5x5TzHx6gC7rcQbJEL7wYKb8HhG_qCwFYZ91lnaT8ZjnR7pYtMWA-1CTAHvL9BuORy5CHD47lfdjoCqAlkLpaGAmriEjF7mV_Kc8oOpQ4VbgkoIXximNHSJfguWrULUff2q--o0MZS2fLewWQ9QBP7Ge_5NxsL5zqcShSfEE6RTkJTol-28CdWIc09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdB0B0pLkIGA-9rau2BaMRfcMcDUXRFILsEroiLC7vfAjr_-0MWlEITf5y74qvYzL743kZ7ynY16U0C1hBzh_Y9RcVZt7KJn_Vi1QInPTRvRVhXoJo4eeudPbAwwomQiTGt-PnaOhn_fLOdX61j1IUs-4XGn5Dc4ksr6NbNnqr-JSJtAthi_G5k0UTmiHLyIfPPTQ14rbZgNaAzv4gO4dsIqP4P7WNKAe8SWUoaqrKeUwxsorL1wAAa3z1wzBQIoF2JhOScwtr17uQ_MzWfy2JAsn5WhwJCQHY9X0t8lW-0kx-ifz2_xJQCAz42N58jWKfz_Ot3h-TVQHvOMeBqjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKYowChrEKHfdmeobOXtzPCAmefIcKH6l1UErXm8TkSGruBpWkuJPe44a6Fm7pB3EXxCuHA8PAr76l1E2bl1RSImsZlLl0DkDL64433Dnr8fuCifbEbCZ4hyyzNDL-SLMZ5OWukIDumnKhs7KRhDEqO5MSYgV_XATdPYqxZZU_rgVLqtT-sakCZMXI7-sXcSDEDc4BrT9mUdjR35xb6jDTFWy5ALY7w4AjULBiy2Pl7TqNjnV8htLgKIKDAzkr0v1wEW7ErvSdZmFcLO5Dpjl9qMzVXphZCLQRG0-6Uz4F_GQFoWHC9utOm-qadmpktvv6Zy6s7hygJOlHDMIqRKOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oV1Q4_ujnanFhZEG_PISmiSUdQQDhVQqtrqyAdLEbRa3wuEUK-XzozTYKgCnr-9shxq6Lsw3tzB9p6eV3ZXdeMmwPPT09FbWvrxKEcmiy8saQJ5Hs_NVdfLvT-cli7sybhllVQfR8gQN0L14vxJiqF1uF9kpSP38DrV7-zuVb8uARMUNjiQY5cRNHY6jWzDHBcG5SVBcyO5hL4B9qu0kh1xLu5yN1M6xb6fv4ukhJqYGvck2XeeOMHm-5Iloq1mTxbLKB0Iu7cGlL8i_I9k4lj_WjrKb9YjAxcfOKgBKd9jSxzCdJl63JrGpRy2OmIasdO88DfezE-hj0sSAjfHnkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 581 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwj-nZ6asFEIJVV_tnI-tGBImtzGoQWGTCJBTdiEG0pMDFU8BVj6nfq5AP__SR2c_YnEKYvHQtO2qP2pJh7OJTPu-K11_g0cy8aVsrAHigjBAaKXo9YqZhQjUDB2UwiwFxBp3O_0dPTxx9s6heWxH6OC8GxF_q_dfRJlJ-QMnVEBHeZhHq6hGPIxE3-czacfoq1HGUXCSwHuggugH2iMQ9lC83U4jclL6W1ANbdcLO4BkyWySRnnGmf_tUSM3qq5m60N1QxqFKwcGI4hrJ7OAVACMIq1olojIMemlsfP-yeijTxHVHUOWJ5mEUAgzx6AyPitS-QZ9NZql17imJXtng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 593 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlkC7Z1O7i_XD9tsff3uKJwwQ812aKo9mnUyG_ATU9mqRGBj863HWCjoBahfalaLqgAMDnE-32yN5ZilvTi9iIQvGXCytmMuan2k7HG-iSVQ24o1ENHlPSwA5Ll5ILSlWK2ApYa4iAVhhDbJospeG0NYJckAe3Vx6YKEIoghh3EqNCINn7Pf1UObqouW7Xj-4QKUD2Y2xY44K0ugPbTVqZ2Fk8naQ2uW7yfuLwOU_33_bPJ0iTbERqtIDVueHY8_-qutwO00sDmeGqtjPBM8T0lznMB1QLoJXckWc8Gz_Y1-u8JEzHB2xpf-_aQ0mGmAiy6KNPynfP35ed4QMklBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeGG4ct7HBmW3YECAB44CnGmpjGhKe3bU2QLIuIugcwMpg4Xs9DkX6gOyV1LoQgBiNp0EBGd_O-W4caNsYujG4yn_OmVJmmi0_8suGGxtZTLcl7DLjB2emoqH0pQD76OiKkYsk91-2oTNpN4jTgGUgmW5DvtaAYY7Hjm1cRvG1Gu9XmVcjGyVaaLhQbDurhqUkpmgOSTG_MQYo4Iff7sq3gIYtQH3BIWr0hh2J5RwRQGa-I_4St-epU9QziUTQA9Ooc1QdJoOdmjkVOGihqQLNjeGLMJeDcTY-ZPqY5FlHsMk9isD1z1f1kqmZv9Q36Xqwx7RNujSBSeFxT63E-m_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 646 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOdARh0ASBkCpPtwb5B_ZiIR8Vc8H4ZmbeYdA55HeDQMdkmTh6v8SBdB1egbYjRrCssISh_xVCX06M9up09pj-4gl1z3IJxLg8r8qzqPFjpaDsfGCn7d-_l2MM9LkqCvqtNxI0pQ6h_FeB1icQNIehuZP-NPVQckQ561GVQANPsUEz7hf7ibA05nbxmaoBgQ4IOFKUWa9NVgAH_x3GH5Nh7r9XPGEWiSlXohutRkn13XcO_8IyBpU5y6wDzeELPjn7KfqD9NyRVBw4KLoXTVgE_CrY45FUnYj-Ra-cZNUuuKj_AEp28-Tef3sglluXUHAJCcX61eaL01w9cV5l7n9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 714 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iICa6k_JK-eKbFoooos1USQVm7N3rhq-kOmgjYfXsAe8U7SNmsFtjHGvYd8gvPJoWbt3JxGa-O22UmqxpCux7untErzb3D1pNs6RKB2Pv8jiE2gx-3sUVyd4o-L5Dyu54GRLH_vWEVF0NtX-96PBtL-2MeyO6kCTJ8low3o1SkPBaWvV5XZX3dFVS6Dcr1jKmWlIn6WONAd5ofTkmfIDtO2H4IOoYD8X4B6yDZfcqGgbj68Xj15sYsWmbbCOkLiLjl9B8OE0bJR5nPrgWy5zwc7z0t_FHCmk7yBE-B9E3QevFMVVtT39ApRFU3cot-LxoU0XTeCEPYO1-XUxur554g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 612 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSTUtgwYMf834GKI3_CSFo0VYCQf35vkdcrLTad1EW6dRU9hpiDoBhoNtKRhA7t3uPwMAV2ELKrxnNCr1-9zjj8wfKbvKqYS4ygszaxZaN8jy-UmCBfjO-VGqE4qPjiHI8cEgI9HEQQLFjrXsrE9baNndvdPckPutvXKBV2x0O8610hkifMz_-LmFFutCa5bwP0W6U4su6ye1Mjy8WQSj-MlYAsLKINNZkjpewUqQ4COSBfIKapVPYx_jrclE0feyrdSYeeuBDYAdcQ47in2sPz5iOrJyeAhzXQOR96s0vUkAnlydp6i4I6mBonb9bNDTjIJoSCPXJJIAkd5Yoy4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6CFLzuqQW-Ock8N1SR0NLn1DX4Y3nnpUlejdzJuIjYbTrfE9pSD6I09-ul8OKwLBSkG-3B9C0YwrxhUoKxDNtKoJgPIKPtnVDnPi1oEGhezPmzQ61QQMTj9UpUrOT6gG0GkoRDjq_AX_dqNROjdg24GPsrQXtqeyQtL9p-gRVRlBU3L_i0zIGUXZep-56BUFj5quFH-Z9YtLDri_8vtsjJp-xfDvuyDueELzfVre_qDGET5b8rq1gY7gUiwJXo2c6UC-KRDdBWqFr9x_RZvB3GjQq6oKtgoeuiw5KMQBrSGFJnQpAo8vB-dTDBlsqTpLntSARhE5IrtTL2LmiUc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juud-PIaRzFCdRPuilz905ODSUhFZl5lrLQOvVwJkegqvvzyIMx0LM7DZTLz3mOCb1vIHtUWJa7yd9h9cAQrKGyM_YeOOBA3gv_DBYJfAmF8mIx9fny-wvFgpQbSOvRhlcUtDzAtGhQa4KpwC4Vlb4AnRq_GmyqfuTFiI0uM-EN_WGKbVJvCZTn2ALNODbMBNe8FbvcfDnABMKXm0bPjYsbtww0Lr4mxeoPT_2WilMOu7pKTqSFB_bhzQEcm5OxHEreNHXVs_zGYI9lxVNCDp4yjTqf4IOWd8tp6yNedV0VCmTRSfErVX3pRvCJSixIHU3Eb5-XzBS7Egn-8eZsr1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GluQFirvAE6eEvj4t_s4L18epo2wL-NfRrbLLvEsGxWnUy_526inN-LNF8DSLn5atvaXBCZ9AUlP7o8mT0gHL2WL8GvYh48mwKK-eEmYTwu7fVU1OaFrLWnaQItuPihtSX_NZ2JkfP0G1w8DZuc2_KKIDS0z8G-nPPte9JAOR7ZwtWFsNuW8a3vKC0nGQJjMsV6hQDwkRz6B-A7DETXdvRaxcxqBeXME25Dgychj5oU2ByJ7i5OPbW9DqK8jsyq4319ZS2seV-Bg0laJPQjx0uZGGUes-HPCyIEoOB7mupUHsRWzR869mCjdTpRjFom-NvyIetzKVfV8FCA79ROocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 545 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yy8uj4CfBYVMb8wNEuaXhs17v6HLs9pA3xzM8CR50lkUarAR69yLZ2_NbSppzH1nLR-3q-CQx1w80Ga02qCTvVNdUV8lhjTdrlaVFcPqXxsE7iFtVJG8iv3CWO9PINcrlLWYiF4wWdxFcXYa5SdWDdiRgNtvBS6eebiy7htgJ1f-9FHt3ugJaqVNjfeUQ58L6DOEcBXkBQ9rFfMsiewrHiND6ZnM1aN2RysWCNG71VFwONy5r8Edl8P7uoiR_5G37oDXjeQw-OFlCiWo-Wh_ca9r4zqL_c6UWN3ZTrrzLmg3XgxXfUzC-x3dWu0LDnqnekKgWzs59f57qSqme2b_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 544 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObNdqOTTV-_96qBOMaaHKXTSamZQ7BvhPlLC66vh6gsMDrHp_EUYsjgQuzuzHxGRq4EH7ZNlVQfTEvxmTh1X6c_GZUoNuk6H4WG1WS2-LLxiE4B0byZXNmI02NwNiKn6Rfw0hDA_eJJRQRJPxHOpAqLcqpfWgogapjxet7NMi8eT13wHjqu6zwVOnzo4T-dWQymN1LopQt5zPym2Xk4fJVjUmvIWThu0PuaTz3dqEM2jaUKvxz_H1k7kfT0DsllB63utaIBSYcQjnrcNpL7sZ54d07mvLrkkIgfOAuoLfvxXkhbiqdANphZZycZ0Wa5RQD-wbGRfBg91sGcdMqNRSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo1eXUNQ649NYXYmsXfoHPwRr3cvgJfqRncEo0HrctKt1lNY8b-Mcyhk7QTMXpEosdAR4NEirosNu48yqaDfSQsa4CHJrFut9T7aUFbOHUQcefcNS2EZo_v_UlP5plrRzs4VQ4vrz2Sx-NmAbxvGcfOzg0eRQhQjICnOvy9jdg3-xmjmGIDwyINs3-AsIT5w1Yr0LzsOBRfJ_DD6xac_wSx8TueBdCUtpZqZIWRAzLbsEa42Cha-P_sZgaUEIeXXhp3lY2UIA2RjwZUc3IP7DeCrgtWbpjuNfkp8_56ZTU7sRGoj0JMslv3JxjH_3EJWdNqZFxHf7YFgMMZABd5X8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Au8A5WGiKH1xl8Y5Asse4zHEW4XSNGh1CnM2sZ0nvej2EgPxzAPljUwJZbYiENUnPDo1iqqq4t2o089Chl2KyWPwb8EpQ4rOJn7DYGOxID2LDRdTgTn1YbZFzL7pvTInPbJQc4sRkseXqQxF9GwM_Bkw7X7Ifc5_gHk4_LzzmyEi3tG7czrv7JVHTQkEGFaHcp_yTrou40BsCtiQxCgNc6GRfYHCjt6JLW-k1rJ-4tcRzoM-Yo9GWmADH9glkaMMj2ygEUXSpvGJyRUGREa5q3fmVyqWVX1RUCnqa8VC5Ef8UrakfWZ0h841xUEL7G7W-CbO0howk_xOBs5HHcNpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhodJIoFJ0OYEw_IbJupwaGw0jnpItkdqZtsN0KrNxnQpO86FbhH2f74dICwuhjgskn1ak521-vJ7hizib2vKVEPZJtEopUFJDuvrGtE03O7D30F1LQ5zOjBfPZqvGUhn9RRBsJdLX8YxHyzp0jZU5ybzxl6R9MMh41gujwuk4pzFfFipIcJYYS7Fg2i2IkZ8963kjWiuWdsGyJ7XCSCGoDa44utTU8_XMKqGQqSMLZn50AoGt1xflvm1OVMhE1mnN2NPgo9Xq0Znb4ar5Ye06DSDh8OUdzjVr8dopGcaMCe61hKJokvd-JxoQZMAtHSRkLgbRhhaRWGwjJfbbdCZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LmjgsRrfMVRmyapnLGwPbZvnHlrrqtgNyQgPGjTfLgbYuaqKcef9-VI-XwJNrQ_kCVLaCJCTjlEYcJiPmvPNdjMMgpm7QnlN9m69pbpUK7OFwXhnrv_SgYBv9F3kW09wbM521pDhnzH6vzaeUoOe3idN8b2Y__EXqkWKjAG7XF_7tG7rJLq4uJTlggvWEN5EtligtDVf1u1zXT21RQ7-7nS_yj8L1EDhe1vmSjjs4MGBtoAcGc4KiTuQzh6NGpOaL7RoCl9NjT-gwwuIudVo89nI5PAQ0etpmmfG2EuBGAS6R8LGkckDFVrB7WtfB0ZyO4X95JGW1Jc01Mul20QLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zlg7vPbiY4_M_JYHgmvAsc9VjLgrovt8gbiGhIuflJ1KEdrAp2KOauMSpDenG71EiVf1KXOKhs16ZHSGsB6L-h6khoncKhgG31DTi0ADk3WY5SCDJRtq3c0Kpd5r6kCSCZKX1NMFoR2ilmFf5iCITZDcpEXDZQ3RGoc8O2y8m3Fyme-PPdiifff6aYjJ3GEppMMNELX7hMigRJzSi3uGi1jXHofZfZBxWYEIIBGGJqUdmlAzKuTIXTaYZwzqIYxHr3RqeYhIpRmwfswYm1WQSS4gvqjcUPrEf7WexjC9Bnj75c_4AzJ5Qu1zb7PZ3xMeatTDf6ESUaEGgtxvJV5Dfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgqKkx1_kG5NHWtZSBcFyoAz7uYCLl7Shk5AgG9T97gGgYkEINqbK7Ah3SwreyxSPMbbFtsCOpnKswKCpA5p-dJrHl-Jqfi4CW_d8bXUuW_-UfusUgoE6RQ1d7Gxnwp5j6j9OjwlW6722QYhgnHC-u0nqu-CbGt24GI5Ftuvl8htRbiudTYBa048G7lvPHl7lz_Ur47T4UGHmTh_KCDQNFDFXtw1nM_8kk_5hUC5KmQT-aLKKi9364X7nZl-3YmbV1kXwHz4HZMgstZj3hn4j9ULsILJFF9me_byHSFYdEDMbOFjlMDnEnwLO_EmEJr9HeQY0fTdkCoc-9bsMfSrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-kV8MPXxpQKDJ9aqrgGwGQ5IvYaLmdC3ifvGmfzey3KMFluroaYaLBU199iG-NL1HZVefxjIk9d8SFYJHsfDvY0MnMi9wASVdXa2cazLdOsQaa8In5uf0SpTfiX2t0kUW-_GgGSgaqzE8r_uyig1vUKLK6zlBK8QNKh9X6H28JGdrCu4yL1i2chBCsPZYt8dE_PSTEGIJravsuHtNucrbajiay9JjN_Ijic27xB5TFzwLsNFGMxy8WSb49lFiE1TOCEmjavQLFUqQPV0sRXvXpN7pamNOP8EuI4E3AbRj24ovy9CGW9hcKjdWy3bvYStilK28Fk9_rmoqGpjH9btw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQU6GjBEBJmbOyij9oG4JZGUBzOyOFlmKpT5XkiKKuG-hnydvIJXBJyNKRVMdpUvVv7P_tdWycQK9RVZ5-BBJCmgE8RI2up748vWgqbDml9t-paQ1S0lobwCe1SVjRVEFbj5JRSD-QKcpduH-x6GHMTRpxi4-lG9WVjm6kgf6GOuPtqUNc34Sxlq8DLkJgrlfwmcrtrUB_TAl2plBHoFYNH1vcV7NgVE4bGSNBFo7doL4UhdwUHReSq0YeuZ30pJw9HDk4TEPVhX4TEpNQolyo4y7AWjm-BCDzSj1CDXRS8h5YVCr0gh--uepHLDZudS-LQgHQIX4BUhH1QdSo0ZNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSUyDfG7nnfLeObaAy289Nmqzx9rLkJLPSHL58MXbUJxdR25K9ijDwpcxEJ-BlAJbdIxizldlPuU4TalAaUDXTvCH1i8L7ZuBDDgWK4nctOvt6nh6kiQwktszxiR5Qm3WXHQRZ2KgJ17f6g62xUtmIykS7ZJTGPhRCa6yK9lYnNsx3neDE7KnJCRQk9dWx9zMRNU2_oE3fYTr2GTKz7TFKyuUT-4zL1lnBdydqhrGKsUCiGccAYylYTartVqySwoUU6YtyzjVoyhJ7_O_-dl1n_6EzO6W7A0Ym-sAy-Ij-MDvmxK9-RhwWxm_a3S0vn6qTh5aBzPY_A5cYbBxBGHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvmKEU3HVOXnMgmIYESsnthwRBL50aOdKRCKQilPP8aBe2j9VwsM4BwbJ7__iXwQig23sT6eA358pi1mq8IjukV5GNEZMbBchdcj1WqW4pbjcpxjIMFNMv8iPJV1EKVSzftCWcNLZopYXccejvCCWmIjKm2EgJc60Oo8cSMd01v2ERc3ao5Uy9aFE0pxe3GAZOQ6_95JCt2nzi7cB_PVobAACx2vaTf1LnZsQ7UufWOFdRIVCzsNeJSYY_t9BEaQzEN3ckJNUeMHP02UWNYXUVCMTLFqqV7SiBgNzFx7n4IIjEst-T1cnHwvFsZnjwvp_eCcSeJfK2BMVnuBnTNH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxkbYm4gp1rymo2k4KvCDTnGvlRgvydbXpEOHXJfxEKVhePDY2JfQBT_3T0EVdD0rNG0SarOiZmhpRpCJ4V8_ejAfkJHOAB8WCAvJeeOJd6bcrVFWexnKHTS-iV5R0sGsDDtANXEisbgM0deB5wrg11DGuKCnHs2QuRsJs_wl64NuQVqdsB8-aQ-gSYJxTgZwlBXYIbz6gYv5SbdNYZihhYfIs6tHJr1GOo986fvZtu-v83DqT2vyAU1KbuLPESxNLwWZAOUXUXShYT3SfaYgEzf_5H_XJxDbmm8hsagqKux5sgLA-a3l91lf6PdxWjdM2UYy27VdDCCAy7GLasyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MkZfNkhRDUi6PXJQtXz45tPqNGEhr2eRMBYBhic20804DzKKCS7YBNqt8p0NhIlm9tq_Oz0W9odzdSBsHF9tiwdYTz-iL10iUnCna0DjqCTpoenlm2Fc8t_DtHwdWZAUP8EjYVXTOiIjrtzSIzWw4JWvKWwXgllFe17dNeQC8EBYHnOJaChq2kCaAge9poq9EB9t0mXj9NwNqzQ_dQPGV2ACPuV-vka-EQD1V2mFh88rdjAQ_dxu4Dj5HdUUAJPTUNHWv_UISzzy9QFowAWUsvFlrW2K7Fnnl_sAuNgya9YqB5b-TkGhHez-C8qvEfHd2c_KXNYb2CTrbbEuUQRXTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcDwKL8C8kTzQBrKbBR0xuY9GrUmEViBoEy8TjOkZ8sROE0Y3sjY-O_OgAl4Ic7m8qjCDfPwpuKOYEsVzMHlO-JN5E-h2G6D_rmPxMGaxM9tqTN7LmnBKfE_L_mdJPlro6MRvs80oWjRecNivKQfuBC9z5wFbXGhiheP5McjbrA9jrcRYJVaZr4mxN2by540bTOzySSC4b7PtvPjWC1HzvK57QqCLLFxNRnGxld4F4x8zJPVkVwL5MfC1EQppF3mrKr03TVQs5UwcVLit1DTnmt03g-r-9HxJVjyDySTovQoVElvl_BOO1IshyMQH5joPACfqylL0cE3PGail3j3HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goIjOQrE5qnu6BvLc1u8VFeACaN6vZV7UsyPGCU_u8dt3Zf3lxbDUOI_nPr8clKrVWkvUP5Fr-iZsnBSPp3VEBgiW4EZX2qi-L7bvfRNNFezE8mMpsTfJCJ8S9sqw68kLS3uujirJ-JETGqIrGWj9NL1qv29flCKQ5uBM0vllLOw_Jm0UX8SD1G0JaBpBK2khjrBqmQORRpXz9uBNXBxxc8JbwSERic_k3DCf652hzoqWzUriCyDjU_aKC3TbhAqeHLFzOXPhXKoJMvMiE25PW3QIbmicQ53sR_cvefdnWcm0e5PtEBZnqSmMBC8eXAEnVgdlk037P9aPDByJwVjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-lFL2B1YevdwstWlOiugyI_v2u9Gmj8BUUy_UkbKjAQFJRVdzHiaDv304EHA2AKuQxcJoUn1g39wNzmCKrVRkUKEGlSCCNq0JHlxJjbLok5cYci99ryqTFYexP1XyKV8_wbirAp1PGUdZPd6jSST8pgeQmVovjtHNRcuMUIJ9Ksa3A9CgXgrs7SMugR3Jf9Jm_pWNGzN6TeNEcnl8ueLZ3cKnGuTJVOuUTlBj6jCw61d6620cj4XfnM-_PRQAv5iL6hMPq5lypLsaYR_nRa18VGqgcqll4L9877AO4HuQPoCQHxLBgUeOseVyiyqRzEYM8thdwk8oU9m93uRAJ4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-MJTk7Myr8PSFYcLEyTP24rDN-uuJQZlY3_rM20E_YHsXsLEGYSgdxJ_Txxt9GdKyJfc6kYSDWrfqWC6IX7AeZKqQlEN-zxvzUwJy2UNavbkvEFmWmXOiylc7ut3i2GPfJ7J3TEfUtVC_JVYShs9_bUnmNt_tLDb5kR-oGeNsIVKfYFJcq_MGur9FVN6TKM7Nfffu55jxW7xdf3twCPggt6F0YunbdtBGnK90cfDUre7thfuXmSzVH0vdthL257D1w-5nNlK71moyRtooUchjw-1eXiKFvnFsLQx_VCXwKpoHbUOzhLQF9eJSQajixcUdGQYwe7ULCNmL-BwCmxDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUTam3W61d7eBSUcyvRWrU7hJ3gKYZKucL0UgGX2e_Qs4xqXyElF7y_AEbYVGj49fi1fJdT1cfHlcGiqzeU9fISzr1L_ByQlRHK2sjJq0WRmu1UjKF8ip3ccPvReRFEIhCVCG2cG3HelBF2xMOyAVZ_Qi7W2jMqXYFhycfNgJzvo9L95PmknA_jnEINeTsJgUwtc0nWgnwtQMDtcJyoOtzIxIa6r4DJBb1ySEj4YrdHlLqLJbWFtnAPuNSkRhjqN8oe1I9HetRp3scEM1ykhiWrXn9KV4y8_pKQq8rfVXhi1RLSgikoWmgwshOA_WkXpypuw1kUkWT92SBbzG4IBxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=smifddMvUkT530ET9-Py9YAJShtyl1zHQm2Hje6F7r3z1eaLU-li5x92vEuew1A_mBqw8Vz-J5mDWMeF_GSpLu39N01f3sbhHkpNecYM7dx9KQ4kHDejbxyc8danOrPeQMvqQMxaQNNk96QCnjt3_foyF1SkJBWYTv9rgbGrs5kmEF5s9JSYYZgYDi-K3YYed_2afU1x__8eRccn38EIIGLdD-IOcfeZNzVrEUR7hu1GXjSHFu3_AlIVRll8hxR3_qBaIZiPtJ2_S-XXa8y0wyuwSI5osjqbrq0pnluPLPYXxxccJSi_jeSJYawyMl_A6YbzveUJYuYHUR_-9FyuAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=smifddMvUkT530ET9-Py9YAJShtyl1zHQm2Hje6F7r3z1eaLU-li5x92vEuew1A_mBqw8Vz-J5mDWMeF_GSpLu39N01f3sbhHkpNecYM7dx9KQ4kHDejbxyc8danOrPeQMvqQMxaQNNk96QCnjt3_foyF1SkJBWYTv9rgbGrs5kmEF5s9JSYYZgYDi-K3YYed_2afU1x__8eRccn38EIIGLdD-IOcfeZNzVrEUR7hu1GXjSHFu3_AlIVRll8hxR3_qBaIZiPtJ2_S-XXa8y0wyuwSI5osjqbrq0pnluPLPYXxxccJSi_jeSJYawyMl_A6YbzveUJYuYHUR_-9FyuAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4FhMVBhUrWBeFJr8VRBoI91-8dH_-mnL__Kw9Clh6ssGYWvPzGqTlcNZ8CJVY-Xj2483wPV6k_GESkm_f3craMsus4mj5A21COvBXp4pT2fSL0Kl4icETZ5fvp4xQAuJOlRH55yyzQ6XZiUVMeoFaXU_LqMcJe2eJA1sPz6fAMXWEg_v30ZB7N7FZOBKWLDcK1MsWFNtlb8wXwUmrfnL8AoOf3vjULjYdgHh16Q0fgERM6iRmj0D94WOwL3fQ499Cq8soS8Y5Opdt6row_bzOBmtWzoj1YxqWIiTVkyrmALl-Nb8Kiczn3rt1_6WlaJcVR9VDt0s5YARadkMeOECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syCAv3CDCur23RpHR1nhgBFSvZVTTLc5NfMrszBsfqtHy4Iaq-KjDUG4zho3KJ9nsSnkYdqKQMiKokoS06hTn07VyUNm9uO31HpkAczqoM1YsHNOdjz2f_CDp5jbPMJ1kkiMrJcNENB3hTJpGh2F_PWRu27oKdCvY6qFfQVQEsUPRPcALHiT34OuWWeCEPUQAZ3ka4sAwOhOlxcUAeLQWbbkut0xiw_JNF6mo8GdM1s-QA8e1u-jI4eUGSSqUa0r78GeZwqyxVX7ocRZFmST3VwOZIu9fby4v5hZsuVYK4SGjfMzFNA_puz0ahjsMsoIE8EBvDMDW-8kAcAJx11Upw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/la3tq2erZ2Wg1y_sGwG4IPbMUpP_ixvnkuZvbXX2yOcMa3FQ-Ix28wEk7RaaW7gSe2ki__17htk_4dyVX2BbO3RlOWO6h1Gb1Hm1PInmpeZvhokxJQWeA3I1forStVlZC7UK3Jz2zQIieqTQAv7GCztj3Narzxd86e1svkiCH7idaOAZa32wMMFpBAd235AmpRRQHU_xyL9LLd-UVIuMn_BYEtHjMt1gWPcl2gMPR7y-y4TgB2aLMM8D0cIjAvjyfaKAqz2HV6RbNqgSsUjkWfFa758ml3iq1gnE9Z4hFRgwpmt8CoEnS0d4hzK0FKiSi59Is43nZPumVu8ysLtVSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLQXsMYT18Mk7Oip8b6PH7fpTGu1p_6S5GBnrKEUJum5qCwnRHoXXlfbRoujabpihupSlJfcDmICa-O5YOIN4BEEZXz6oll3kD3lDWlE1uCmsd_D58Q1BGnyLsyEneWmuFvngJ12tOpZ4KqtCpr86V7BrcJp4XOQS_w5JnNiqRA5czrzMdlH472OL5iwoqS2wXLt7SpVPn7JUbwcd49nROWY6h_H6LlT6ANIXview0o6yYEkXjsexBVj3yIfjpL87UPB6ZXIt2SmYa15tGt3zdEVgtXHOdrUeLggo-li0Qf5yyn5Jfb-ckoHA1Gjnt506l2aV6m99OWgSvbKOEvzlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K2JRTbcGaJD07Li2ipwgiY5h5F2T2f-twPllSuZuWYkPNNLtm0ODeovqdxaTDESwPpG3jLVQSJnMirO7CYV6TAF497p6ua6tcEccmk-rtpwSxlOCQ5bRqK-O5KzXRvFvaR7PNMYYZi6tjKFS240aSxOru4q1S3HxQIbIaIkMNSDZLVf-Cn4ZgeVG7oMdXLyfwbWV39xHz520hKng34LTqM88Ald6VqXrygCwj0we9yrwSVMpdC6KZ3Zd3nJ6Ph5kovTAOYgvAj0IPGSabcl3BTwT1iJbcgtmwF8M7mkhlzerK29iqi7pi28HBFEVhJx5ejqwpQBLaY6O5MtbR98JMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAcDjib-SlGkR_KRd69JdJEbjdWgfkfXzKEvnQs6VYGjs3xv5LtyOsJpj1RqiNfjOVU0LZiukCVp8OckPXeqWRrMi3xkSmRKcgEKwqPteO31SM5Ct-AFRFpRqelMSlFQGjR7Yf8ARZmd1aGeM9xmRNU943Rx4khs7hKNf37P1iuPRUtcVk01Z_H6s4HA_E6LRjVyh9ZJbSPCiIzSHyXV0P1aq7CtvAqdawoZtI-TiLSYsYzUHlsZxzHFsuN-ObTeP0XWy_OAPsO34cOydvA31ZGQghfRUSA0gvE4T7WYh2r6XnUOGPHzWT3tDpk4wAIDTtkIWDh9M3T6ZGrq41f5SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMYW_yHgSmQSpTwc4zYFr5gPwg9151nIW_gC8Ynwfvi_Q-M8MUA2XKWTw5a_6FwBWXvNQ0jDIdrA3_B_USzeAepyIBMYF0HmlECB4LPQ3CEBHqzeUeq5dbjP89DGTBWAFOf1diFm91d6fVmPkq585DobUqEJCkdN3eaIz86tw4lCgmdg6lshOCT3ICZ4m5FT_rYX26TjooukDxMO-oi-itLH9c8unXq8gpAJl_aaIP8znnC_CbAVNEGpGM7DdyD3XKSn4Bq4HXjx-hDU0Vz-PJ9Vg7YjD0uwsagryGipG8ieJjfJ8rskTEsJnk0S5hzw1ukofiSjVSZ0ucGoUQHDOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Hn_s1I8xCk5--NhDGBy_xc3gOGutdj09PHGns-iw8HlM7oE85YPQDSD0w2PlBR50vH7VqGOxppm-3WHzqjacAh7SkbSucOXeky9PgkUYZXEmI5ofhG6ErfL2jAmhH1VN1brsTnv0gsQCNqhQ2fbdHAG618mJRGSavm33PWtsOXtkXp-dkCIg4J52iTVTkInLYJWF0Q3QYp0qyxbtxkSmp6jSUw1JtEZemOzOfxStZM36Qbw6xeR-lh6EFg5cHaPt38oAvP7YnoryV7qwGIatWWP9GOe9oZgBUAHu6gmKL5y5pDwn9m7FUavcT_FfWcdSIYm7YZ5txdOPkBj_UkpKqAmvJQ00lhwv60afNq65gv_fjbGlee1qZfsfUqqGIf_7Aciq5B3wWws_8Qx0HZdfTymrIliLRd5p1kjKYNDnmW_jqmtpHomvRP59QeExjb-0nmXEdQCLgMd_1tYgfYi7GNlSc9-w_nY84ykh2NISpkOvgetpeU3B3pfaG1acbszjo3JEQxW0JGw67RX1AAQ5X-ytMkqN2l3Qwjr4wwSM828PQ-J629ehDXogWcx0X-dTi2VUw7CMxRLN6w6uVN2qcdvrcozwXIjrjJb1vMxpZsTZZOv4JAjMhZIcbY5YLRXF-MBsSnibD2yN28wsFS69_qsf4UcNVpfHDJtoK1OQGgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Hn_s1I8xCk5--NhDGBy_xc3gOGutdj09PHGns-iw8HlM7oE85YPQDSD0w2PlBR50vH7VqGOxppm-3WHzqjacAh7SkbSucOXeky9PgkUYZXEmI5ofhG6ErfL2jAmhH1VN1brsTnv0gsQCNqhQ2fbdHAG618mJRGSavm33PWtsOXtkXp-dkCIg4J52iTVTkInLYJWF0Q3QYp0qyxbtxkSmp6jSUw1JtEZemOzOfxStZM36Qbw6xeR-lh6EFg5cHaPt38oAvP7YnoryV7qwGIatWWP9GOe9oZgBUAHu6gmKL5y5pDwn9m7FUavcT_FfWcdSIYm7YZ5txdOPkBj_UkpKqAmvJQ00lhwv60afNq65gv_fjbGlee1qZfsfUqqGIf_7Aciq5B3wWws_8Qx0HZdfTymrIliLRd5p1kjKYNDnmW_jqmtpHomvRP59QeExjb-0nmXEdQCLgMd_1tYgfYi7GNlSc9-w_nY84ykh2NISpkOvgetpeU3B3pfaG1acbszjo3JEQxW0JGw67RX1AAQ5X-ytMkqN2l3Qwjr4wwSM828PQ-J629ehDXogWcx0X-dTi2VUw7CMxRLN6w6uVN2qcdvrcozwXIjrjJb1vMxpZsTZZOv4JAjMhZIcbY5YLRXF-MBsSnibD2yN28wsFS69_qsf4UcNVpfHDJtoK1OQGgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8RxDxpDHUcnjnudqTIjLR1Vso3ARGbl19itTQfwc3ud0hWLnzBuHSlCy_aIIvv5qM2G5pV1fUorPdZbP2JzKneGdHpghgZlYU1TCE_pMhtzIH9Hcl-FkTHKuDu24r2lKR82EnKgyOi3BlaCdjp92eQWWa2ReVnqYKk5eRf_4zsfjzz7kQARlzn2VkKc6yeXAy_wsvFDExTLz8Zzuq9qT2-VqGoe3RAHZdWK-s7TD1mhjuzIQX4ZMx6ncc_K0nmZfNj4b1x2mnu28Fs0O84OqpleSSikft1WkrBAknmTTj-d-Rw6mfd1zcSJv-gE55uHup6rAv-9R3sQuWoqr_Ax3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9VMKHVlOEiD3My3pgxstK-kWxjKUVrn9GObz33wjncBeP_ybsHNM7W_IKZI7WRYGsd44a3-a1NP5myQ0qS5cIdJo1Fnw04uPzzf9iLY8cKtjtfrfQQODrI7VTrTueJsFyQ1vt5hqfLLsYsARfO5rfoedRhmPYKMfc9bFkGVI3S9tnYWXRqMD4Sp8iXIj7j6RcsnAC-km1D4PUUviXtoVlQAW2sC6UWyjljbqHRNBa_uluDIi3piDvZ1h6XAXil35ZoabvsCYCqmgDDl-hGaPOi5e3yYTm1KxlhORMJIFQ-_45vRyT3bRd_qdmv7tAuT6KLVZ9GTfdpRhmZBVXVBtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMoOCbpMqw0_zAtwvwklT5jVK8oxeCNA0BeS9JNQmkuJSzG4YQMgJbGXFNGhBnqk8pwIKODd2EjgsudBubzQZzm599hWIpJo_5p9hpSDN3n8TkJ_ZnPR5dYmln7dXR0nY4JN--rQYF0ANUeJNGlSh1UkrR4hmzc3jcuwr8XLsZ5fuIAxhIxKkKrx3vOXyyy1GZt0rb9Mk3lNGTTT2fkQR2F_qWTeLn6myfiyWXaGngk1pdnhBLvwJL2gNfizRUde0gVa1gOe56Or7iziSn-ZhaNN2NwzHVa71BrBHREghjAt91gLNxxjB6N7k6vzF_FRO4bttCvBbDF6mK9HNdFEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7DC3QYOjnpZYkNzjq6rudahlSDiYIVFkvBYhd1Ib4XFRX6-EvG-7twwv4vmw06BbYsJPg6WlE9chYpM_ZFNbgZValLjiGy7Wh0x2D681azuS8qjC6pgi4fFrxQZqJKAftSfloVnNjZ03xme1Ku_OPS4c0tmSq66AphK95SvCtdaJ6ABcxJ-a_tdHVJCkTs_IN9530sumf2R45wSVd2Kp61XhW_bBaUPoSvpkV8AtBk7FBkNfi9SqEa5jkG3ElJfDCY7nnxyg7f0bLL_AcK2X-AKQZfTYG3vjQ5i9UQXkhE5ECGBAcsuts8tyM2o4-vMiTObkvX46iFmGlbjs6vIHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UeshiQelg84zEM0ASBBHaiI736wNj5WoZdCiYN3k3tFK5adG2xldGjx3s6Ouvv1gHyvcm1RtkrbB7KkMDWF2-8S3ACNU2VE-laG8c9fMgV6K3VSkJT8U6dvCcvTUuvMFNcpYOSRTgrRKyEUjXafnvtOczqcKi5LxnLR6c6hXEhcR5pszDHzkmmdWD6bwhSJwMXA_TR7IAvXPLLle8UblyU44uQy5tj_740T1T18sxG6e1Hy8rbL_tzTaiEQqAEKpr1oUmtwMl40LEgQ9fFjbCctiunv2KuUepbNLpWKfEruG_DB0KV3ZOaeiAl2cjlqH01_O63MMkiZie22jnGULhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0brFcmm4bE3oXj2OYp7P3taM9Faluc8zaeJA0FQxU0TX_SnL4mwmQUHLtWpBEkP_ymKmjAfWpxdPW-STxoAeX8XyBgoz1s1_-8vjPybJkgSftQRkpmmPzASRRpBzVwHfsE24PQCXl12gNqhHErO-LRp7oZJCeqMCHnK3o_Z-AmiMFvXKBn1ea_uSPHnfgvEqqfPUVqSe1ZDug4plYEobha8Ys8pfdj_kHlfSc2bYUsZx9KbF89IeAQQeYxAsLYWkCb0wU49qyXE6uugnWOr6dkBMFb8nJUaZLBkwlqoa6aLEvc2ZUguI37o7bsbdvTD1hmvL3wF1Z_iGcErKEV6gL30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0brFcmm4bE3oXj2OYp7P3taM9Faluc8zaeJA0FQxU0TX_SnL4mwmQUHLtWpBEkP_ymKmjAfWpxdPW-STxoAeX8XyBgoz1s1_-8vjPybJkgSftQRkpmmPzASRRpBzVwHfsE24PQCXl12gNqhHErO-LRp7oZJCeqMCHnK3o_Z-AmiMFvXKBn1ea_uSPHnfgvEqqfPUVqSe1ZDug4plYEobha8Ys8pfdj_kHlfSc2bYUsZx9KbF89IeAQQeYxAsLYWkCb0wU49qyXE6uugnWOr6dkBMFb8nJUaZLBkwlqoa6aLEvc2ZUguI37o7bsbdvTD1hmvL3wF1Z_iGcErKEV6gL30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgIAWaqXuoPD4hwuCxZT8JHOX_a9_gqa7bcjtgDeT6trid9ht1lYIOijt0A-jzRONfv8pt45eoFNCRL0sDsblRn9tpgdrkcGi_1JpSMgOw1wO0-e1cRH4NbJk9zEEL3-c5ZVpMO_2ETO9bY_uPssJhpQ1D2PBSmGWAdgvyvD8dGkZRNctBmHERpJVP58sPBLNQeDggrFREPgNb-_fb75H9h89aNKDECbIpOJhgetpFOzQBQbbXiw3CJ5PJDQOpPUL2VIy9UC4wJqjKFutsuo0SXEuKzUXES2Dxc9f1ymRvb7_Ru7r7SIcK2soRxqf03akJgTL13rFAjy94Zqqmog6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
