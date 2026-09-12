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
<img src="https://cdn4.telesco.pe/file/ceNHDQbfAK16gq_FGVVgh5iLUnT-tFU0ZzLRVHeyPA1DCRJi8n-G6ZzDz0WoO4Vtm-ohqK14AYDL3HEtW4MyPkZQUrx0wXOKoWS3AZ2bjMyJcTPehJ-lGdmizZeSdFear0oQDvtX7-VMG7NZKSEGuZ9YVP7iAxUNjHm-Sb-KrxpedW463hi_-ckPyDu-XDLU1HpMfkAODuRiMolHmR9kqQwhtfCN8JrNXoGIe03P4NUdSGcEIfr3YIQPz1LAiEHYDZwR9TRAuNnmHmlxpdxRpYdQD2DM2bW1_nt3G2M9ubH5jSPek7UsHH5Ct5avkE0c19mGsnnOQZwc7ScD0FSuwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 04:50:25</div>
<hr>

<div class="tg-post" id="msg-689135">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFO2nSPj0EpJ9PYs6R5HAaFneZLTHEryCBokoDOWhxY7YKQs96Q7S8iu7OtgyBknKuPlyGcCtLk4qdwtwryEGLC7ho-Cy8kZsAYl7dfOVqk8ENZ1kmdE_TcVTvQ3d9Fk3Z6HKADMGv4QtxgsrxLkGQifRWRb6IkCJ3gUvdo52U2txrp4aoJe4FHd1SZPaQgSYC68UJelgo9BxE7qzeWSwqMyy0HOAvFV-ox9oDoJGVm19WxH6OOiIYIhnVw7z8bNNjZVfMb0BYN8DoRRlb1GkQF_tPGJ_a3dmn8bctWppUQEGHWgGlH9XacXYCTOGT4Wic20MdWDfL-nbpqYPCxgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
کلینیک دندانپزشکی کاخ مشهد
🦷
با مدیریت خانم دکتر آذرفر
✅
دندانپزشکان عمومی و متخصص درجه یک
✅
طیف کاملی از خدمات دندانپزشکی برای کودکان و بزرگسالان
✅
اتاق عمل مجهز برای انجام اعمال دندانپزشکی تحت بیهوشی و آرامبخشی
✅
انجام ارتودنسی و ایمپلنت بصورت اقساط
🔺
ارتودنسی
🔸
ایمپلنت
🔺
بلیچینگ
🔸
لامینیت
🔺
کامپوزیت
🔸
ترمیم و معالجه ریشه
🔺
روکش و بریج
🔸
جراحی انواع دندان عقل و نهفته
🔺
جراحی های دهان، فک و صورت و ...
☎️
05136028800-4
📞
09155671518
📌
مشهد، روبروی پارک ملت، امامت 22، پلاک 8، طبقه 2
🆔
@kakhclinic</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/689135" target="_blank">📅 00:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689134">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHRhTomn0Xlu4I_W_45Gra7tDcQ4DiI9bPiD03o0arww6p5iCj60WU__DRVd5SMc-R-6CuQkcMBNl61vEeUUXphHDcNws8-d4ZmtyER0osjZ1g4TJDRBuaFXo0bGP3ViCtJN7gN22QZC9Gt2CiZuLYsYrn19cbWCJ0IUGBV-ogwAMHngV4QU_ObXKKLsPRLNJObpkHF4b160kt9vBQRLsWi9_AKRqCKeekkbeZ8md3tZ3eMNs6H0bNvNf2UcVcjqqHP6JB3XHo-J1yG_VV1k-suIWoDRgLR4BhtUMIcXra0a4i3SUmARTVAm1w7sgbZ4s0sn_wZp4-p0EFdnsIA87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
اگه بین ۱۸ تا ۲۷ سالته
؛
این تخفیف ویژه توعه
دانشجویی و برای ترم جدید کلی وسیله نیاز داری؟
دیجی‌کالا
مشکلت رو حل میکنه:)
7️⃣
نگران هزینه‌ و زمان ارسال‌اش هم نباش
، اگر بین ۱۸ تا ۲۷ سالته میتونی با وارد کردن کدملی‌ات
اشتراک پلاس رو با ۷۰٪
تخفیف بخری!
پلاس رو با تخفیف بگیر و به صرفه‌تر خرید کن!
🛍
🪄</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/689134" target="_blank">📅 00:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689133">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqkHGHd-9nsCsdRyYiJNSQSxJH9oojm_LcKo2ROsfUdc_vU3Uvr9cPjADF0qO-czxnGzBdtJdzc-3zfaYyQARFwM8sIDml5fvyM-nhF50mgfhugACiI7TBG2sIiSopkug7HN4DtO_9AAhm5yMaGQV3T7JzHPWJgplpBOl3bz_mrFAXYO5CB5VyF7si_J12s1HOuqT8VU9Pi2IKoHauAWWIn8ii7wgD7YgdJxBiW3TUN3WjqzlquPm8uv8d4xy3Okvy-TQzno4axhKdq5P7XparLZQhUmXv5-5U_mdBWNqg6tt7sCG1O9yKDvgnrioJi6JaxgiU1rLnpCmsOMoVw2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج دستگاه تست قند خون دیاباتان SMM 1000 +دستگاه فشارسنج بازویی دیجیتال
یک ترکیب کاربردی برای کنترل راحت‌تر قند خون و فشار خون در خانه. مناسب برای استفاده روزمره‌ی سالمندان، افراد دیابتی و همه‌ی کسانی که می‌خوان وضعیت سلامت  رو با خیال راحت‌تر پیگیری کنن
🔴
قیمت: 2580 هزار تومان
پرداخت درب منزل
خرید
👇
https://memarket24.ir/product/brief/63615/180124</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/689133" target="_blank">📅 00:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689132">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPyrHbxem96KATvkfLge78Y5ER6k0dCJ4_qgNdmWiEYoCCfaMevA37SR7-ddxQ6_Q2AVxI2I-SnvPz2zEqVUzAdYQxvchPBByimZDG7GAkk_SPB_apMVeoTjROOe2leKqaxQokradyz2szjjmYvLUORRraILNYLHTU7hVdZcaHwFvbERBmrlmaNMK0_NfPMH4nEDMZ59GLp1fUVmPjH3FMy5PjB2k2EvwnTxl1y7SiegWlCPwWKHhCu3IeXscYy-TAiY5H3-uNW8L6f_JlOEpcqNwwNMMYlx6qwspl7RROKQSzj7sRNdr1jb81MSQSHJh3k_96JCzIqXWNc_xTkkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیروز، ۱۱ سپتامبر، با غروب آفتاب روش هَشانا (Rosh Hashanah)، سال ۵۷۸۷ نو یهودی آغاز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/689132" target="_blank">📅 00:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689131">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb8vVVYQbXpCJmVLSlF2phcPAT9SmQGOAUQew0FnS2FmPa1GmiUfD6CWdYjd45mR0XARQbcAK1nw2aqyUy_OVXWbgOk7Ola6ylkeQC53ohZdgf9PM-02_U52QlsOdXMP-TOqld7cHNhsmu8QAlVTsJqObUU9IHmjx_h0k4WUuYC_uLqhJVvaGYjWN-ZxL0ZzYuJK7Ux7-aifxjn2KuKAHMoQ_7DrVBq7Big4kedxO-8pvL1eI8KaGdPTZEdHX6PKPpcjo7b9jH70t365CjV7O-gSh-__JSDxxrxBPe7mFBjoHxQcv6FNpDc3tsVbSFz9T41v_h8NV5gZcMi0zMOWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع محلی: انصارالله حمله‌ای نسبتاً گسترده در جبهه مأرب و کوهستان بلق غربی آغاز کرده و شهر مأرب زیر آتش سنگین توپخانه قرار دارد
🔹
همزمان، نیروی هوایی عربستان در حال بمباران المخا است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/689131" target="_blank">📅 00:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689130">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای وزارت خارجه عربستان: خط لوله «شرق ـ غرب» در چندین حمله پهپادی که از عراق انجام شده، هدف قرار گرفت و این حملات به مصدومیت و جراحات انسانی منجر شد
🔹
عربستان تأکید می‌کند که حق خود برای اتخاذ تمامی اقدامات لازم و تضمین‌کننده حفاظت از حاکمیت، امنیت و…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/689130" target="_blank">📅 00:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689129">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UG5fJHOjcZ0tQZoTFrCy54gigd1Z-f2xyB8rZTpkWPEYMxya8a0-zNP27CgibN4srQcg_xSA-I0ehDKrmrsGf1COvSi6akLeX9XJCi80zlg9cXKsVot6_V0r8BUqRP2ngjbNBb5LmYvCkz7Rwj1flBAAKZCoV0zUyDgd8O69qXtVdGrG-hpdPzEWRUCPmb7SSmoqLtJBGDeZC1zj0ykVRv9sU5xX0drccCEc1zHQRvYIyQ1xnynnIa7IwFEDU49sP9Al5oiPAPSXuCkY2TKO3cN45PuohM4lmQHaqAkbRi6SNgLh_39SdVb_f-T-OtfL1YeHRBh6jGrpwZLx2zWXLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیبی و پروژه آبیاری عظیم «رود بزرگ مصنوعی»
🔹
لیبی حدود ۲۵ میلیارد دلار برای ساخت بزرگ‌ترین سامانه آبیاری جهان و انتقال آب به مناطق بیابانی هزینه کرد.
🔹
در سال ۲۰۱۱، تأسیسات مرتبط با این پروژه در جریان حملات ناتو هدف قرار گرفت و کارخانه تولید لوله نیز ویران شد.
🔹
لیبی پیش از این، در چارچوب مذاکرات بین‌المللی، برنامه تسلیحاتی خود را کنار گذاشته بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/689129" target="_blank">📅 00:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689128">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByltJgVlapghv5WIW1Qew0vVg1QwOOddpmhsnBNC5QDTHoBnpC1HtAcv1xWJgd57jIXprWI50NeyKwCb_EGCiWcpEJLafhPwxHDlnxY2glaViD4beazW7jB7hsxoD_OJwhCm-kHGzg0vau_WGwDFLHEFkCzM9YeJDAnj6omuteI02zBdsCd-dSc63oBbmPZacjI29UB4kXbGAtm8z7XIdc1p-4qfI6hXdYFILTHp4vz3ilbbuWzr6oMItoswwSS0Ksqw5EhjC19WsRGEvHORtLFQ_CGQGlKFUAJXknqmY3XR32KdyDl_Mq_0biJauA61cwSHM42ZC6ZSb7tMtmLCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای فایننشال‌تایمز به نقل از منابع مطلع: وزرای خارجه کشورهای خلیج فارس برای پیشبرد توافق هرمز با عراقچی دیدار می‌کنند
🔹
این نشست قرار است روز دوشنبه در شهر ساحلی صلاله در عمان برگزار شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/689128" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689127">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449e1510e9.mp4?token=OzWi0aVOFCug8IKty0RAiOEKItSA8bxmyWsMpV0Wr7NAcIX7LZqs50S_We8xAIi_absUfhSegpyxLhnhxbEcbAoHb-yV6MQ85Nop7TGTXS2WnXBEH_JkH_WMYoq7Y8ZgajPAIB1jBCm0t6A87MI8viT3S4pfPNhc4RP2dWGfWK0WAIChcEH1Xz6e8Cs9g7hFeeXkvGe3XUogfJHi_b7HxSLIKR2LlK2XFaJMC2TKZfVbtAHuA3JChcOKK5RsHCuwxMMoL3QpkKg-K5GdoDdXF1XL-YaHTedpjtPBXX950NkwnjckBUNUE7lH5KSXo8DX6g88rOiWpxGVfif4-nyzUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449e1510e9.mp4?token=OzWi0aVOFCug8IKty0RAiOEKItSA8bxmyWsMpV0Wr7NAcIX7LZqs50S_We8xAIi_absUfhSegpyxLhnhxbEcbAoHb-yV6MQ85Nop7TGTXS2WnXBEH_JkH_WMYoq7Y8ZgajPAIB1jBCm0t6A87MI8viT3S4pfPNhc4RP2dWGfWK0WAIChcEH1Xz6e8Cs9g7hFeeXkvGe3XUogfJHi_b7HxSLIKR2LlK2XFaJMC2TKZfVbtAHuA3JChcOKK5RsHCuwxMMoL3QpkKg-K5GdoDdXF1XL-YaHTedpjtPBXX950NkwnjckBUNUE7lH5KSXo8DX6g88rOiWpxGVfif4-nyzUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از نبرد تن به تن رزمندگان انصارالله یمن ضد مزدوران سعودی و استفاده خیره‌کننده از RPG
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/689127" target="_blank">📅 00:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689126">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ3j7LcKkdEvNjMQ-ccpmAUD9bV5DRr9c4fNaRc1V3df2Sx8zJzE0l1JbgKgudlaxKdyYqeOrXOO74Wlk7d2n1DTUQ5O0-vV_D2U2vzfV_4ZeZJG3FupuOznXey2LIwRiDUOPlgQFDUAhTv8OlnfMhHiAzedyFdr-IjDbOHCBrU1ZBEqASoZtwmQ3ZbQYRbOyjyf7M4PFnL4ymXmBYtyBWLgtssyisfOnCmr-09XJG16s-EgepiBoy2zi01uvOUMJivUuRvIZBQqeMQbNIdYVEyijPj7p4NkskeJVjZyvvcOj1iw7dBG35lQXMrEgrgKHFEVKUFSHgUXcmJrlUPfQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/689126" target="_blank">📅 00:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689125">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c03af870.mp4?token=Us4lgfFmQxnHyK8LIvNHYGdkMOA2r-wFKo1YVrM7XnUT5evEnPiyzV83xrFX1Lp_yFGynQodmBazYS8hC0FJRyKVn91YQwgobE7PTVJ0tcMZLnvUG-2g4gOKYu-x9OCQICOql8Hx419WurAEbvvCGBlU8-xu3xb9u8jEQybMsLh0SeTPnT_riSDrpb1sc5gJ6IOeWI8rTQTTuI9CthQ-R8nn8ONQyQkDQrIm14eRU2tRFXA1U1loaUYkEh5NrYgo0eEGMDRJknxRoZOpHgE0BTkPebwhk50ByAgHHitl3ePoUYqoP3yJALYUvhckM3oUwf20_GHfsEXo9ZqAG7QD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c03af870.mp4?token=Us4lgfFmQxnHyK8LIvNHYGdkMOA2r-wFKo1YVrM7XnUT5evEnPiyzV83xrFX1Lp_yFGynQodmBazYS8hC0FJRyKVn91YQwgobE7PTVJ0tcMZLnvUG-2g4gOKYu-x9OCQICOql8Hx419WurAEbvvCGBlU8-xu3xb9u8jEQybMsLh0SeTPnT_riSDrpb1sc5gJ6IOeWI8rTQTTuI9CthQ-R8nn8ONQyQkDQrIm14eRU2tRFXA1U1loaUYkEh5NrYgo0eEGMDRJknxRoZOpHgE0BTkPebwhk50ByAgHHitl3ePoUYqoP3yJALYUvhckM3oUwf20_GHfsEXo9ZqAG7QD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزارت خارجه عربستان: خط لوله «شرق ـ غرب» در چندین حمله پهپادی که از عراق انجام شده، هدف قرار گرفت و این حملات به مصدومیت و جراحات انسانی منجر شد
🔹
عربستان تأکید می‌کند که حق خود برای اتخاذ تمامی اقدامات لازم و تضمین‌کننده حفاظت از حاکمیت، امنیت و تأسیسات خود را محفوظ می‌دارد.
🔹
ویدئو مربوط به یکی از ایستگاه‌های پمپاژ این خط انتقال نفت که مورد اصابت قرار گرفته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/689125" target="_blank">📅 23:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689124">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLf4xnjpgAIIgzuFFCFiwJPB4hW0NPj_SLXa9KOn0pErXgw2e09EaRFXi0Tg0M2bFy3XIJZUOlZj32RGI37_n0MIr8LSYz91X4dM7M7TILv2is6-7yHGR21NBps7ub3MHlqrvNq8mvbZVqI5YJWn0nDLoWsZHA-bVfvgz9gv7TxczSF9UEq-n36BnSZ8-idYH_u8QxoodNW5flEFFqD03lbjraThPddcMnAaoBsqXkJ1FqR_AElM2gyTI_9JPPuSsFvW8DhH7hLS01BtP4w3ciYNZpO3Sqf_rYzfF52YkqaXrxGHXn1v408fXer3W_f_LMxKGpKlaWL90QUn4pmnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الکساندر دوگین، فیلسوف روسی: حوثی‌ها و ایرانی‌ها همه ماجرا نیستند. غافلگیری‌های جدیدی در راه خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/689124" target="_blank">📅 23:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689123">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
المیادین به نقل از یک منبع ارشد ایرانی: مذاکره تا زمان پذیرش شروط ایران امکان‌پذیر نیست
یک منبع ارشد ایرانی:
🔹
ترامپ شکست خورده تلاش می‌کند خط مذاکره را بالا ببرد تا کمی قیمت نفت را کنترل کند. ما بار‌ها اعلام کرده‌ایم مذاکره تا زمان پذیرش شروط ایران امکان‌پذیر نخواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/689123" target="_blank">📅 23:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689122">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا به نشریه اپک تایمز: ایران پایگاه ما در بحرین را کاملاً ویران و نابود کرد
🔹
منظور او پایگاه پشتیبانی نیروی دریایی در بحرین بود که مقر فرماندهی مرکزی نیروهای دریایی آمریکا و ناوگان پنجم ایالات متحده به شمار می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/689122" target="_blank">📅 23:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689121">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ماجرای شهر | سرِ درِ تومانیان
🔹
یک بنای تاریخی تخریب شد؛ اما سؤال اینجاست: چه چیزی قرار بود تخریب شود و چه چیزی واقعاً تخریب شد؟
🔹
پشت تصاویر منتشرشده از تخریب «سرای تومانیان»، ماجرایی وجود دارد که برای فهمیدن آن باید به آبان‌ماه ۱۴۰۳، یک استعلام رسمی و اخطار شهرداری برگردیم.
🔹
در این روایت، سراغ همان اسناد و اتفاقاتی رفتیم که شاید در هیاهوی تخریب دیده نشدند؛ و چند سؤال را بی‌پاسخ باقی گذاشتیم:
🔹
چه کسی مسئول حفاظت از یک بنای تاریخی است؟
🔹
وقتی ارزش یک بنا رسماً اعلام شده، حفاظت از آن دقیقاً بر عهده چه کسی است؟
🔹
و مهم‌تر از همه؛ چرا باید میراث تاریخی یک شهر، بعد از نابودی‌اش شناخته شود؟
🔹
این فقط ماجرای سرِ درِ تومانیان نیست؛
ماجرای نگاه ما به میراثی‌ست که اگر امروز نشناسیم، فردا فقط باید عکسش را ببینیم.
🗞
اینجا ماجرای شهر شهر را ورق می‌زنیم:
https://eitaa.com/Majaraye_shahr
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/689121" target="_blank">📅 23:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689119">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VM4KuKY-CFcZwHb1jps7ca-AdyQpr4u1YUKkSYgfseh-0DzPrZ-cpDwKZRkj8czjgS2lhbpmqAYYiddhFXN_3mNoSCSjs8O5Rrix2uwJ5TsWr0aVsqbwynjnneA6gbLJd1JudZVcAJBAg-iD6OIlZ2ZL2xWf3XwMuELQQcwt0OGDx4kfmqghYc8T_O-QUDIgx3bijKLPy5B-J9DhtSAgN-VPYKzypZqkVidKI2HMqKG5naSV3nSPHqY-H0Sth7rYKT8F2uVB7m52TLRs6BELdootlBK_2UNRUIcIlvllG6snvjctgZchDI4mmpe7hyG-ZLqIVRMOzWLxH9k4yJE8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ck5H19o4FDt-6Vxr9jDoz-DOdDtxAMs6vCLyn-3hORkpoPRAjAxymXSjAPgkB015yV9GJ0nlfGNGJ2GVmsYNWfbokKgY-Mtk0Z014X2bY8D_lgdzDYSQGkyF_8LMyVLtRy8qVndEEgs9tqPAw6uI1WjCuNMzrAYUPGR5ywxejRBQj1SttGkltn69nNOTEJbx2lrZSfLEfxPJu8zZAisuAmMbjD8DUpR88ci1tbFewAxrEttvVpFh9Wyf-cSbTpsei6wEc_m33hMTILzydgNGRQQM1AjEy-zWI_fG-QJj8tpeHXc-pqe9m_FcmqENJp99c0E045v_sIiPRIuFVknopA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از تسلط نیروهای مسلح یمن بر برج کنترل تردد کشتی‌ها در تنگه باب‌المندب در شهر مخا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/689119" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689118">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54f1063ecf.mp4?token=fW_YBGITCnSgnoighV0ZDZUZ3J_Zs2elREBcrnw3G6lOWvN8USmFiYrS5fxe-VL6Bd-jCc6ky_CJjfAxtBFw-0KfDtAbrVmPibRseyTKyvDODLsNZ5fLGJohKqcJd0L1xmhOCymzxzx9b20N2L2nbsrXCH44dU0Trv_4toCXkL7BJ-yWYDUR2cNTBl1GCgXzfTRmRJQhqWaIPNdqybjt0OW_U3FWGgC1DAlKCW8OwejqlspU2gY8Vz10ohMjy7EZZcZB2XFtDXKDWyCJpolbxmR--dXRMY-1xRzJy9lRoWCT1bp36XvJUBsXHZiAxe3nn0bW62XdE1VK541wcM79qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54f1063ecf.mp4?token=fW_YBGITCnSgnoighV0ZDZUZ3J_Zs2elREBcrnw3G6lOWvN8USmFiYrS5fxe-VL6Bd-jCc6ky_CJjfAxtBFw-0KfDtAbrVmPibRseyTKyvDODLsNZ5fLGJohKqcJd0L1xmhOCymzxzx9b20N2L2nbsrXCH44dU0Trv_4toCXkL7BJ-yWYDUR2cNTBl1GCgXzfTRmRJQhqWaIPNdqybjt0OW_U3FWGgC1DAlKCW8OwejqlspU2gY8Vz10ohMjy7EZZcZB2XFtDXKDWyCJpolbxmR--dXRMY-1xRzJy9lRoWCT1bp36XvJUBsXHZiAxe3nn0bW62XdE1VK541wcM79qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: تحولات یمن ربطی به ایران ندارد؛ آمریکا عامل اصلی اختلال در صلح است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/689118" target="_blank">📅 23:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689117">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
خبرهای متنوع هر روز را در خبرفوری کلیک کنید
🔹
🔹
چرایی ترور علی لاریجانی از زبان رئیس سابق MI6
👇
khabarfoori.com/fa/tiny/news-3244385
🔹
نتانیاهو به‌زودی می‌میرد؟
👇
khabarfoori.com/fa/tiny/news-3244472
🔹
لقب تازه برای روحانی در تجمعات شبانه
👇
khabarfoori.com/fa/tiny/news-3244435
🔹
پشت‌پرده پروژه جدید جاسوسی سیا | ترامپ به‌دنبال چیست؟
👇
khabarfoori.com/fa/tiny/news-3244449
🔹
مرد پشت پرده حملات به تاسیسات هسته‌ای ایران | شلومی بایندر کیست و چه نقشه‌‌ای دارد؟
👇
khabarfoori.com/fa/tiny/news-3244415
🔹
خبرهای جذاب را هر لحظه اینجا دنبال کنید
🔹
http://khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/689117" target="_blank">📅 23:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689116">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
خبرفوری / تنگه باب المندب به تسخیر رزمندگان یمن درآمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/689116" target="_blank">📅 23:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689115">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2J0Ilk3fxjJIK25qvw3-1N--kDoFdmlGgvIsoRl-Xjwi_aQmbgUwcRa9lx7KxvSF4AqcV82D8m7j1xE-Km6f7uiVdd4ZhnE4X-ajrnSb3VWcLVsXdQ2-5DVgyHimT-mWHfZK5ZV7u-LEGE6su4hO77iaQh8tK69lJ52QEvhD0MEo5LPLvmGjU_GZB7VXxwJWq6Ig39w8xwunAv_nmkUh2Yx3FU2zCymHOdLNRyLDNCd02hqrxM5lreekJpfrIdJNPUJcH3dKMbEuflaWdUbU4kHutx6gr4Mpjy3DajzurR2yiQxQczXDwiX8CVx8dePHVgJWzoFe36fzeMSVZmaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو به زودی می‌میرد؟
🔹
نتانیاهو در جریان یک جلسه دادگاه در می ۲۰۲۶ ادعا کرد که در اواخر ۲۰۲۵، در جریان آزمایش‌ های دوره‌ ای PSA، «لکه کوچکی» در پروستات او شناسایی شد که معلوم شد آدنوکارسینوم پروستات در مرحله بسیار ابتدایی است. اما ماجرای بیماری او چقدر جدی است؟
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3244472</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/689115" target="_blank">📅 23:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689114">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms2o0SkuiArtThBOYldC3ZW3Ah7jRJPxUX_E576MD8rDD6QHiFRMUbH4VEYpqZnlSmC5mbYXhv1s97DN45dSdJZdF13bnce5ypl60ZbJ_CYZ8NaQQ6O7O9DjSw3gs5hkdTbN-dDYSJDE52A-lb7GQlZWaXjmyLOJPqqW9gNItlCKU_SUGHDvWxd4NFcLepRzPTldvhE84SUpoT9pqYl18XccJfGA1u4C96HUw1LmIZMGJqiZ5UOKh_P3n8ln4frhMnp1Dxgv456JSD6KX52eDLoIKIT9lfsUbUNliFG8rmE7ylJm_zLqdefTw-Q7epMYPfKJsIigt9CZHYZQeAwK8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
قاب فرش اشک حرم حضرت عباس (ع)
یادگاری نفیس از حریمِ وفا و ادب.
این قاب، جلوه‌ای معنوی و چشم‌نواز از حال‌وهوای حرم حضرت عباس (ع) را به فضای شما می‌آورد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۴.۵ × ۲۰ سانتی‌متر
▫️
جنس قاب: PVC
▫️
طراحی شکیل و مناسب دکور
▫️
انتخابی ارزشمند برای هدیه و یادمان معنوی
💰
قیمت:
۱.۳۹۰.۰۰۰ هزار تومان
✅
قیمت با تخفیف ویژه
۱,۲۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/689114" target="_blank">📅 23:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689113">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
اجرای ویدئو مپینگ بر دیوار ساختمان بانک ملی ایران، شعبه بازار تهران
🔹
به مناسبت
نود و هشتمین
سال تأسیس بانک ملی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/689113" target="_blank">📅 23:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689112">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febe288c78.mp4?token=ao_kPw3HtQmpxWsw9zRcEO1ISCihjUM5B2X7vhC_Y08ydrL5mpvOzuaS04Kh2VC3YwyZE17kxUVeK8AXYWolZInHbq1dxi37ji1e57v7Al8Y8yFwuuXN3lLpjP9rPpl3ql2DfU8yxEGhe90-I1KYi9ROxR1tsBAifbqZ1MLR7-SIO8Do2QuTcv2o_oNHZG9Zx610_nGWUxHjwk0adSm_2GnqAX3xD0xEqn4_stsBqxe92tRBcjH1RVt02zYTAhGZlnt_rKmkyW5fCZMeJDpQdFEUOE2ojgYwiFPotTX5-XsD9c8fqCGi6p3iHhp1HIwwZDqAJCLG1FFiLWiyWWck4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febe288c78.mp4?token=ao_kPw3HtQmpxWsw9zRcEO1ISCihjUM5B2X7vhC_Y08ydrL5mpvOzuaS04Kh2VC3YwyZE17kxUVeK8AXYWolZInHbq1dxi37ji1e57v7Al8Y8yFwuuXN3lLpjP9rPpl3ql2DfU8yxEGhe90-I1KYi9ROxR1tsBAifbqZ1MLR7-SIO8Do2QuTcv2o_oNHZG9Zx610_nGWUxHjwk0adSm_2GnqAX3xD0xEqn4_stsBqxe92tRBcjH1RVt02zYTAhGZlnt_rKmkyW5fCZMeJDpQdFEUOE2ojgYwiFPotTX5-XsD9c8fqCGi6p3iHhp1HIwwZDqAJCLG1FFiLWiyWWck4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: تحولات یمن ربطی به ایران ندارد؛ آمریکا عامل اصلی اختلال در صلح است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/689112" target="_blank">📅 23:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689111">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCIYPjtLUz0jGU9uqfq99eud7TbELb1jNBW2IwWAXVu_P1DIHn8syNt3wkqasTm1c6eMu8vHa7PNlyMnft_oVhNToUzAy4NbuUpS_0aPLIYTPY9ZYZjrSx9zTCWypo-Xh_baeUbFbbBU_uCTPI7itrCQeUCe4GRQ2ITX86gMIf6LJYdtQsWY_KBtkdLfyDLZbpU8SKsBOpzaLGWPFstg0vMt8k3F5oUHhh1eLb1cXDzRMftmKBVIdbxNcFktuBp25Cg5wWAvVIs1ntxSntY4HkCg6qzRmCt9ltIjN1guCgMOEO20aY7mcc_E4onVs8xo7Q80TSR3W4CRaILnUEofwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کره بادوم‌زمینی رو با چی بخورم
⁉️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/689111" target="_blank">📅 22:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689110">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تایید برنامه جلسه امروز شورای امنیت برای بررسی برنامه هسته ای ایران با وجود مخالفت چین و روسیه
🔹
۱۱ تایید
🔹
۲ مخالف (روسیه و چین)
🔹
۲ ممتنع
🔹
این رای گیری صرفا برای تعیین برنامه امروز شورای امنیت و تایید بررسی برنامه هسته ای ایران صورت گرفت و رای به پیش نویس…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/689110" target="_blank">📅 22:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689109">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
تد کروز: احتمال اینکه ترامپ ایران را به آرمان‌شهر دموکراتیک تبدیل کند صفر است
نماینده مجلس سنای آمریکا:
🔹
احتمال اینکه ترامپ مانند کاری که در عراق کردیم صدها هزار نیروی نظامی پیاده وارد کند و دست به اشغال بزند تا سعی کند ایران را به یک آرمان‌شهر دموکراتیک تبدیل کند — احتمال این کار صفر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/689109" target="_blank">📅 22:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689108">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
حاج رضا برکتی: مادر هر روز با عشق، انگار برای یک سلبریتی غذا می‌پزد/ تا هست، دستش را ببوس؛ یک «دستت درد نکنه» کمترین جواب این همه محبت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/689108" target="_blank">📅 22:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689107">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما در وضعیت نه‌ جنگ، نه‌ صلح نیستیم؛ ما در وضعیت جنگ هستیم
🔹
تحریم و محاصرهٔ دریایی به منزلهٔ جنگ است و هر آن‌چه که ما در این وضعیت انجام می‌دهیم نامش دفاع است.
🔹
منشا حمله جنایتکارانه آمریکا به لامرد، خاک یکی از کشورهای جنوبی حاشیه خلیج فارس بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/689107" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689106">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار آذربایجان غربی(Admin)</strong></div>
<div class="tg-text">♦️
نهمین جشنواره انگور در چی چست ارومیه
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/689106" target="_blank">📅 22:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689105">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: نتایج اولیه کنکور اوایل مهر اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/689105" target="_blank">📅 22:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689104">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
عربستان حمله به خط لوله نفتی خود را تأیید کرد
وزارت انرژی عربستان:
🔹
خط لوله نفتی شرق به غرب این کشور در ریاض و مدینه منوره، روز پنجشنبه، هدف حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/689104" target="_blank">📅 22:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689103">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون آموزش: شهریه دانشگاه آزاد بین ۸ تا ۳۶ درصد افزایش یافته است
ابوالحسن مصطفوی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
شهریه ۳۰۰ میلیون تومانی مربوط به پردیس‌های بین‌المللی دانشگاه آزاد مانند کیش و واحدهای خودگردان است که برای جذب دانشجویان خارجی طراحی شده‌اند و ربطی به دانشجویان داخلی ندارد، در واقع این شهریه برای دانشجویان خارجی بسیار پایین است و باید حداقل ۵ هزار دلار یعنی حدود یک میلیارد و دویست میلیون تومان باشد تا با نرخ دانشگاه‌های ترکیه که ۱۱ هزار دلار است رقابت کند.
🔹
شهریه دانشگاه آزاد در سال تحصیلی جدید بین ۸ تا ۳۶ درصد افزایش یافته و این رقم بسته به رشته و شهرستان متفاوت است، اما خبر افزایش ۷۰ تا ۱۰۰ درصدی که در فضای مجازی منتشر شده صحت ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/689103" target="_blank">📅 22:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689102">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d409fe30f3.mp4?token=GS7fNFv1Vl2OA4InuAVoOp0uzY33bUIgti15-ARECIpuOgSYBCZr7XZXk2W943boo-Wu4Z4NEfgBnJYYXY48QMgmwo-x8IdJXRiDrySLReCwAHAh-Y7RkT0gSuB87aIbiVqtf2Vvvfk6x3EpWx6VDb0izT3tF9GjmweN1rodfmwoZEeAnWY1Ru0oEZdYFvvtkkbxluFLAILEE0lDOBELo5tXzu4E__atfh_FHMwmw_m9VwYA0RYr7HHgv3UBMfv-7fxJ4EmSXTJs_5IWsDao27dmAE04QNCXZG-pJnGC4q1FuSo7ZXLVngPPnhy3HLChxlbkpiX2NSbvgYI3k51gXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d409fe30f3.mp4?token=GS7fNFv1Vl2OA4InuAVoOp0uzY33bUIgti15-ARECIpuOgSYBCZr7XZXk2W943boo-Wu4Z4NEfgBnJYYXY48QMgmwo-x8IdJXRiDrySLReCwAHAh-Y7RkT0gSuB87aIbiVqtf2Vvvfk6x3EpWx6VDb0izT3tF9GjmweN1rodfmwoZEeAnWY1Ru0oEZdYFvvtkkbxluFLAILEE0lDOBELo5tXzu4E__atfh_FHMwmw_m9VwYA0RYr7HHgv3UBMfv-7fxJ4EmSXTJs_5IWsDao27dmAE04QNCXZG-pJnGC4q1FuSo7ZXLVngPPnhy3HLChxlbkpiX2NSbvgYI3k51gXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازخوانی هشدار ۹۰ روزه در خصوص علی‌الطاهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/689102" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689101">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIbz9iOly0Vb0RlhtHkyujEZKt3wlhEnZmoRTsMdkZBPgbx8O2TLkbAFys1MQ446iOawnIJEKp1AXMptF-R0aTfxJgtGTrCaGmdroB47lg0gZWUQ8sCNlBZKeMSg_i0ZJZGDOSolEOT8aTpgaif8I1ScVvDgpBU4XwGunmHxAorCHc4rbpVdiu9B4ufGkT13ynNo3XDtkXsJiXYdIgETeQ9ZcmbIeB9RI9TgNJhH7-Hd_fj8crw7NdiT1jIVW_K6mhIl76X3rLdk8GGir6B_u5pnad4NDST-Tn5j3rWSLYNq5_c_xubZ6VHLYKOZ29KWbwSKCyWJkz0pq7UpeWge2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصرف گوشت فرآوری‌شده؛ زنگ خطری برای سلامت معده و مری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/689101" target="_blank">📅 22:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689100">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
طائب، رئیس سازمان بسیج: نباید از روی سستی و ترس با دشمن مذاکره کنیم، ولی اگر دشمن درخواست تسلیم شدن یا مذاکره کرد، باید با قدرت و به قصد گرفتن حق خود با او وارد گفت‌وگو شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/689100" target="_blank">📅 21:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689099">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
نماینده ایران در آژانس: همکاری با آژانس ادامه دارد و برنامه‌ای برای بازدید بازرسان از نیروگاه بوشهر در نظر گرفته شده است/ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/689099" target="_blank">📅 21:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689098">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609389c52f.mp4?token=VJkrhrllYjU2ENundfOVt0CUMOfbRFqkHTA4iCyMNXbKWzgh4QWUhQVvdT6-NZudVB1aNIf6ktpnzLCHsAMRr-VtJouNTwVUQ6enEpr-rjBDj1sBw71UJSblnvfSTyK-w7s7_83dlhMB-U_hyI0urpWojA1dO_5YKaJWng-77obvdfEr15fADmKYWGb_WPvWew-7DTpM3igDES0UXQiKJSQhjwtjl1BN41jhKCJvS3I-QO5F2zQUESEmQIr2DWCbyy8MmVSzyOzgRzc0-7u2gAwAKiIE6M2GVJNo4KUAIzsG2LNzAnQSzXIruxhvGthCBrADw772-7yOLZkmcgg_9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609389c52f.mp4?token=VJkrhrllYjU2ENundfOVt0CUMOfbRFqkHTA4iCyMNXbKWzgh4QWUhQVvdT6-NZudVB1aNIf6ktpnzLCHsAMRr-VtJouNTwVUQ6enEpr-rjBDj1sBw71UJSblnvfSTyK-w7s7_83dlhMB-U_hyI0urpWojA1dO_5YKaJWng-77obvdfEr15fADmKYWGb_WPvWew-7DTpM3igDES0UXQiKJSQhjwtjl1BN41jhKCJvS3I-QO5F2zQUESEmQIr2DWCbyy8MmVSzyOzgRzc0-7u2gAwAKiIE6M2GVJNo4KUAIzsG2LNzAnQSzXIruxhvGthCBrADw772-7yOLZkmcgg_9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: حوثی‌ها (انصارالله یمن) کنترل تمام نوار ساحلی یمن در دریای سرخ را به دست گرفته‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/689098" target="_blank">📅 21:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689093">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xi2S-jXWyOvDVug0mgpNqiJwai7pmyqo1jNFvrJeVhBaWkhqDEcFAzWMIjcSgAFG21PPhSNw_yKirlnYl-nAAUfQhuWrTSzXyRNZR27WOeBB5lygZ7x6oUuI4vD3tXG-RDQUtXvTWBpl84nysnK1AGY_iFhEHgmpd-UklMypgDHZ6iAHhHJTg_RPLoiMMLbiCjHcwMGKwqQItJD5GtrKqH9k0peco9071wYmq77B79BGOyx3TJTl9gcmLeLcOrsY6GCG2HlSBuRbhM41HUlZU5kbuW5r_CarfIQiDCKEKMCjKb1jYMZTD9-aN3NzQoqPNnuv_s6mWtQOPy9lBRzTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stTdifYI7eSQg7K0_8MeMn41e9Ke5qbOm4QakMIVviaAzRI2cWoosuxVMXJQCmfGOa4Sz-CW5aGuMTHFOfHo4_hSAx_SY8WbPeFU9k-Hl0kZ2dcHUqhhDsvMzgHhYkC1s4s-qUrMnqDqIKNdyJSpwSwtnFrB0JC2tlFXiGRx7a9CWVTYX7U2JdBRuv33VtvYVHGlv41TV-muxxsA5Sh33bZW4kwDxlH16MK7NunJZIUvaNVocKgY2KHTTraNL8QE-nBEpZlzxy2utffhgGD9dgzxV9PtjupCJpMN3bO_qSn9HMHZR4lMQoa5l-ky0hxTUzIqlDVd3954flfRFTLVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nllgHF_VSsSdSZ6im3Ee9AaHqaX4pD7YPZ2dVoFnNsjyiO0jK6mtPIBzTWEM3f5YcgB0WJMBpxlVldZRJm8hS9IMlQOojuwV5E4v_29ffrmu1Yy-2E1xnH2_ExrYAOvLyrxuPbW93RiaTSbH3AOla2vphx2KVgVXPF4sEYNch56WBmhqe4g_vF3OuqCxu4JngIFGXuhVb1iGx7-IRUE91yGq3cSjySM4Kpc-mr4b6saG1Q76A_lOuLH9TLWx9I4Bsr5uHVsZGQrstllDfvyeIelbzarVHrS4y2sxbfWB2pp-xwerfTo5hyfSeIBudrDwx-wNDE7ul_AbmDBdyMRbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DH4FzJKKmjNKroWjdbFApeLfFHKfB8CjRNHtwYXoGMa62S0l36UPuOPrFaiVBqVFXLuFe4Qwhh1qURx-PESIVBAKRk2oY4ddFnM6o1u8ev7RyHjcccTuJlYge-m4LCK7rroWIT4Sw5Yz2R1mWzY6XJ4ukf0Zgk7E2nedYQAIyqHk1pQxpWDFKtCOH4bwpn49YUzJXT0Ei6oJRcr94ljp5_Ep59rKlVwkqB0DHir33uq8b7fq9ts7kEhPQAAekaNlMlgCH55zphwBaLob-M1omuZbaotah_tRbWfMP5KDFcRgXktmak4yvCvA1eeoYOeFnnnQ9w1JYh2mdzL0RjD5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqjx_czRv5kS4h0MUTgDma8F3PPdO0ekfL6Qn40AZlSWdx-2CGI4sQ6xh5O3rlzxNtinTqZBxr_inTj511IsOO6qgQ7Ccez2rpFxw7gou82YslljK647pyBIpxYrNLiJsMwRZSPVNalUN-w91FXj92Gq3vmD--ioy1zKAH7XTecHSL1enPNcv5VlKGH9kQJxsCwbNv9dw0f5afZoUX38Srj4oxR1LTtgqfzHWElEB6dVb2QVfGRmxR3Qm00fIF9Gm2OJFV5PqSod5a8pi38sCiKoCD0aIQ4_MDizc-HGHx8mF2AEm_7cLsUnuvkMrdXABz4vTzmux2NS4AEneTD65g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مصرف و هزینه بنزین در دهک‌های مختلف درآمدی چگونه است؟
🔹
بررسی داده‌های مرکز آمار ایران نشان می‌دهد ۷۳.۸ درصد از خانوارهای دهک اول اصلا بنزین مصرف نمی‌کنند و این آمار برای دهک دهم به ۲۹.۲ درصد می‌رسد.
🔹
در سال ۱۴۰۳، میانگین هزینه ماهانه بنزین برای دهک اول تنها ۵۲ هزار تومان بوده، اما دهک دهم ماهانه ۲۳۵ هزار تومان برای بنزین هزینه کرده است.
🔹
همچنین بررسی ۱۰ درصد پرمصرف هر دهک نشان می‌دهد ۱۰ درصد پرمصرف دهک دهم، ماهانه ۲۷۱ لیتر بنزین می‌سوزانند؛ در حالی که این رقم برای ۱۰ درصد پرمصرف دهک اول، ۱۵۴ لیتر در ماه است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/689093" target="_blank">📅 21:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689092">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">15-1 Ane Manaee (1404-01-31)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/689092" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه پانزدهم؛ بخش اول
حجت‌الاسلام امینی‌خواه:
🔹
تحلیل تضاد بنیادین میان کفار و مؤمنین با تمرکز بر آیه "سدّ عن سبیل‌الله"؛ اعراض شخصی از دین و مانع‌تراشی در دینداری دیگران [01:00]
🔹
سنت الهی در گمراه‌ کردن یا هدایت انسان‌ها بر مبنای نیت و مقصد آنها [05:42]
🔹
هدف جریان «برانداز»، حذف شعائر الهی‌ست، اراده پروردگار اما، اضلال و هدایت به ذلت آنها! [16:38]
🔹
دولت از آنِ “حق” است... از سقیفه تا داعش؛ پازل پنهان خداست برای تقویت جبهه حق [24:07]
🔹
تبیین مصادیقی از سنت ابتلاء، به‌ عنوان آزمونی الهی برای تشخیص حق از باطل و نقش آن در ارتقاء فضایل اخلاقی [32:05]
🔹
"چلاندن الهی!" ابتلائیست برای برون ریزی واقعیت‌های درونی و ارزیابی آمادگی فرد در مواجهه با سختی‌ها [41:42]
🔹
روایت مبارزات شهیدصیاد شیرازی و چالش‌های سیاسی و شخصی او در مواجهه با فشارها و فتنه‌های دوران جنگ [44:45]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/689092" target="_blank">📅 21:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689091">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f433103ae3.mp4?token=PlBb1SwnoB5cLMbBYrJfVb-AO9Cp31nIn_rDMvJLOjjsQDjpL9CSNobHAj6UMN4BB9HK740LTtkeZfWyTpLa94ilznixS89BinksQJNVuONitzp305z_X38wXgcSeKjXpbvRrBmEWKYz3oEdMPToZV_fGiF94CyX9b6kmolXIovpzHWxPC8dqHiTNsa70Ppg2H_XHHSMViw-2RIGCI-xZw_Owc5hmj0nSIiTrY4kxLODl9nvk0DTbv3_RwAOZKPNCg1G3PUqAJfWcskVrJhRCNqIVWrWIiSwSL8FZ7y5k0JTl8oIiwsjs-ORcPpZ7qn0w1V6OyvZiLwcP4_7EHtErDIq4d6kfqCN8TLJuxsyJhU7BawKuY2NtPVI3zYvZTK5AainmbuymNhWVSHtGFjzoLAzaoDDJOVosPCrdOFtzePYTcr8cGLuXH4Dck6v9oBkrsO83cmykHZLQYnl4GKpnqEM2eDOUpl-78oFvG139NbiLKgyxtc1InDnKGl5LefLAamuD7T0C-3QCkoyOGDTCZyNFaunYMrziPOAHoiEzuQTuGHuqK7DEkVQu-F6O10iqq6xHKbUV8soOVzw_Xlt7t1vhdtjGJckKeJdebPJWoBWFDBN7UwHcqkYrPdQvC4WjHs-pSIPfSVT7sdrO_qwvJK5GZxDVwT5lH5sk4SFqUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f433103ae3.mp4?token=PlBb1SwnoB5cLMbBYrJfVb-AO9Cp31nIn_rDMvJLOjjsQDjpL9CSNobHAj6UMN4BB9HK740LTtkeZfWyTpLa94ilznixS89BinksQJNVuONitzp305z_X38wXgcSeKjXpbvRrBmEWKYz3oEdMPToZV_fGiF94CyX9b6kmolXIovpzHWxPC8dqHiTNsa70Ppg2H_XHHSMViw-2RIGCI-xZw_Owc5hmj0nSIiTrY4kxLODl9nvk0DTbv3_RwAOZKPNCg1G3PUqAJfWcskVrJhRCNqIVWrWIiSwSL8FZ7y5k0JTl8oIiwsjs-ORcPpZ7qn0w1V6OyvZiLwcP4_7EHtErDIq4d6kfqCN8TLJuxsyJhU7BawKuY2NtPVI3zYvZTK5AainmbuymNhWVSHtGFjzoLAzaoDDJOVosPCrdOFtzePYTcr8cGLuXH4Dck6v9oBkrsO83cmykHZLQYnl4GKpnqEM2eDOUpl-78oFvG139NbiLKgyxtc1InDnKGl5LefLAamuD7T0C-3QCkoyOGDTCZyNFaunYMrziPOAHoiEzuQTuGHuqK7DEkVQu-F6O10iqq6xHKbUV8soOVzw_Xlt7t1vhdtjGJckKeJdebPJWoBWFDBN7UwHcqkYrPdQvC4WjHs-pSIPfSVT7sdrO_qwvJK5GZxDVwT5lH5sk4SFqUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توکلی‌زاده، معاون امور اجتماعی و فرهنگی شهرداری تهران:
«بشکند آن قلمی که ننویسد ۱۷۰ شب مردم ایران توی خیابان ایستادند»/ کجای دنیا مردم ۱۷۰ شب برای خون‌خواهی، دفاع از نیروهای مسلح و دعوت مسئولان به وحدت به خیابان می‌آیند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/689091" target="_blank">📅 21:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689090">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
نیروهای یمنی به "ذوباب" در نزدیکی تنگه باب المندب رسیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/689090" target="_blank">📅 21:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689089">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
عرضه نفت عربستان در ماه اوت به پایین‌ترین سطح در بیش از ۳ دهه رسید؛ ۶ میلیون بشکه در روز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/689089" target="_blank">📅 21:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689088">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3986c3b36.mp4?token=Ar9cHd17XhjATu0wyA2Ubw_n4DvU-YKHSwgOKAPz2irQNHw_7z89H73_EJN9w4XIJsAFy3BhicosaKZmVegH0SufRdnp80XSagAsQkZ1edKHKeKjXnRmSrlmbYXFjws5F3CoYFlOGRpHoFUywv8nwIHwO76y4DwVppK98gHr3qv3AVzuYip6UivIKBxVYu_SsG2qFtaSxIN2PiPZaE29Kj-Xyt5coEDsax_er3JIybJLfQSOcPzPnAu1pZ_uMF-NrGD3CddX0MtHRPOQ3XqcQqjXnYSjTPM34ysNNFpeP6hdrIq3TRjCiy4Gds4YacgCkBGLEaUyiQpywn_NCrldgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3986c3b36.mp4?token=Ar9cHd17XhjATu0wyA2Ubw_n4DvU-YKHSwgOKAPz2irQNHw_7z89H73_EJN9w4XIJsAFy3BhicosaKZmVegH0SufRdnp80XSagAsQkZ1edKHKeKjXnRmSrlmbYXFjws5F3CoYFlOGRpHoFUywv8nwIHwO76y4DwVppK98gHr3qv3AVzuYip6UivIKBxVYu_SsG2qFtaSxIN2PiPZaE29Kj-Xyt5coEDsax_er3JIybJLfQSOcPzPnAu1pZ_uMF-NrGD3CddX0MtHRPOQ3XqcQqjXnYSjTPM34ysNNFpeP6hdrIq3TRjCiy4Gds4YacgCkBGLEaUyiQpywn_NCrldgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برچسب سانروف وارد بازار شد؛
برای اونایی که ماشین سانروف‌دار ندارن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/689088" target="_blank">📅 21:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689087">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIVQULWmJrBn0FEaBLM69ha8Qv4DhiMJglyf_K_2OWMTi2jo8FdObq41Y216r-0o6Ii83hyP6L4qtkFcDU7Av_Z_d9aH7vmWYhupry2NNadEs0xzVDNhPv2Ll4yBAe0l2y0t46NbaaJbsZLyPmULK1q5vJ9lwveqN-9DSC416JMmvSbBi7Aw4gK17rNNRyEuCaYciD29z7tGa453G7ggrncrw5NLDGHqO-6fp9mx9UrZ0PRgDruKGrduZZVXSuqzgygAoO-Ow9ILh3RgqzgpC9ED92npxl7OZ_0tHbXFcqhidkllwBVdPxfnUWTkTnoGcBsrq11UCufB9zcPGVAquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانه‌های ریز معجزه‌گر خاکشیر
؛
فوائد خاکشیر که تا حالا نمی‌دونستی
🥤
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/689087" target="_blank">📅 20:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689086">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
برگزاری آزمون‌ها PTE و AMC هم برای ایرانی‌ها متوقف شد
🔹
پس از دولینگو، تافل و GRE، حالا مجموعه‌ پیرسون (Pearson) هم اعلام کرده که برگزاری آزمون‌هایش را برای ساکنان ایران متوقف می‌کند.
🔹
پیرسون یک شرکت بین‌المللی فعال در حوزه‌ی آموزش است و شناخته‌شده‌ترین…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/689086" target="_blank">📅 20:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689084">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U82-gGrJQ5tkk7b_5InvEuiheICa7ew1wOOGEG2FWoccE8oEgLeHCFSTFZHiWz_Wt0rfpC3tLQcMavgwMgEbKCW_-QqcIuQzKe4GgcWMn5qALXDm0Yq_KfgrS6HBTuL3C-x3FuExt2aSrQ_uOpHxEPAAz52boZFfgZC1tdhVLQvqmE3zV2uKJhnuGh76RLm9tUCXjGh7CoAzNb0uFicVE0vlPcdYUQ7o_5KUHhN-kjyffp4b_qnG3cApdKox4vbn9zvh-JQCtR68xMUOEghV8oR0VGvwOS0q65yg40nJiEDGBHk6UxUi9UTR6XLi7m5QwbOgD3KQ26NBQ_Cf2ZsXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/685db0e885.mp4?token=JaJDunSL0ufVedfy-f8ejRokiS3vrSTvNt-qrqPGkAOaUdR4W77rgvw4ANc57cDMNxZ_2xEGrYrtfFKUoTQmsdxQpYvbW5ig26VsLcu6CfeeFy6bPKUYDJX7S0rtHJiV_gn-qvkGKMk8ShWwQyrCgiYTUv3SbyCPT_Nr3Mug2trSkkGAlzqcNiGKt4CiQ83EL1hLuF6XFc4xfJPPPn-dO1asVazYF_DCEz7-7nrj2lSZ8ta-nW17yLnbLL5RcDH6w9ZYNGH9a4K8gvYYSxeql2n5zKsh9J3sIirJv-pxHrsJM7c6KbVUTo2H35G7IEWV2QajN3zixWi3QFyFf-QrxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/685db0e885.mp4?token=JaJDunSL0ufVedfy-f8ejRokiS3vrSTvNt-qrqPGkAOaUdR4W77rgvw4ANc57cDMNxZ_2xEGrYrtfFKUoTQmsdxQpYvbW5ig26VsLcu6CfeeFy6bPKUYDJX7S0rtHJiV_gn-qvkGKMk8ShWwQyrCgiYTUv3SbyCPT_Nr3Mug2trSkkGAlzqcNiGKt4CiQ83EL1hLuF6XFc4xfJPPPn-dO1asVazYF_DCEz7-7nrj2lSZ8ta-nW17yLnbLL5RcDH6w9ZYNGH9a4K8gvYYSxeql2n5zKsh9J3sIirJv-pxHrsJM7c6KbVUTo2H35G7IEWV2QajN3zixWi3QFyFf-QrxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از انفجار در خط لوله نفتی شرق–غرب عربستان در جنوب مدینه منوره پس از حمله اخیر یمن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/689084" target="_blank">📅 20:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689083">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای گستاخانه ترامپ: ایران حامی شماره یک تروریسم در جهان است و هرگز به سلاح هسته‌ای دست نخواهد یافت./ الجزیره
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/689083" target="_blank">📅 20:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689082">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lW4IyisbYJEKOXXQn6k8kj9ygxE2Uj1zdLJ6M81nrpIstuLka3RXnOB5HChxLuBPYG45QQDE9qIN2VGGM34woVifE1TPCzDcUiSiPIqu5sC72B1dRCJYbtXt3ZzXcG-lndrio4NhAMxSJYGi5PCpZ9gWgdJ_wfDglt3nmSvH60yuIPRyzL797lIdxdTWwE2z2iebO1-vDwIlaAXLnZ35AyCzr-c0l_2RXNib8Iip1WS1jwPt7bN9sY4D49ilHUf5xP2xybAv3r5Sv3Mdoazc2PkYWxK21Z9S3CDbwzK8Uy6DV-u6RCoZFaDFTxFJOgEVwAyn_z6MoMERIRPueb3Kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس یادگاری سران بریکس باحضور پزشکیان و پوتین در کنار یکدیگر
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/689082" target="_blank">📅 20:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689081">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e369573f89.mp4?token=tjwP1j9YmIN_PLzhltVdDbXt5vrN5j6ZEC2o3h7gwS69WK2rZT6S69-YYHLr6_uGpwics6JhpOvlnG4w57pJGSRwXCwQbN2reSSAi0-C-SeGekMmruLTPdiji-U-EO_af0O2FuQeobl9Uja-jamgrBQiWyI5vsE7vBbL1Pt7-PKRFCoOJ0K5Lg2Wk5Ov1lPuo_tg_e_-GK75aNp-Amo6zCBB36JF6dCMyt72WToLMSWXIzrnlPg0lPB60NUwqdjTvpTO8FjVDbewPHfU1IuAnniy1P0M2fTGIDwKHei2vCIupFuHgXq-LwBZGPodqTZoTWmvafdWQxBo51YfdnbTJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e369573f89.mp4?token=tjwP1j9YmIN_PLzhltVdDbXt5vrN5j6ZEC2o3h7gwS69WK2rZT6S69-YYHLr6_uGpwics6JhpOvlnG4w57pJGSRwXCwQbN2reSSAi0-C-SeGekMmruLTPdiji-U-EO_af0O2FuQeobl9Uja-jamgrBQiWyI5vsE7vBbL1Pt7-PKRFCoOJ0K5Lg2Wk5Ov1lPuo_tg_e_-GK75aNp-Amo6zCBB36JF6dCMyt72WToLMSWXIzrnlPg0lPB60NUwqdjTvpTO8FjVDbewPHfU1IuAnniy1P0M2fTGIDwKHei2vCIupFuHgXq-LwBZGPodqTZoTWmvafdWQxBo51YfdnbTJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ایستادگی ایران در برابر آمریکا و اسرائیل به دلیل مقابله با قلدری است
🔹
نمی‌توان در برابر قلدری سر خم کرد و از حقوق و منافع ملت دفاع نکرد.
🔹
کسانی که خود را مدعی حقوق بشر معرفی می‌کنند، در حالی دیگران را متهم می‌کنند که دست به کشتار انسان‌های بی‌گناه…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/689081" target="_blank">📅 20:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689080">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
پزشکیان: ایستادگی ایران در برابر آمریکا و اسرائیل به دلیل مقابله با قلدری است
🔹
نمی‌توان در برابر قلدری سر خم کرد و از حقوق و منافع ملت دفاع نکرد.
🔹
کسانی که خود را مدعی حقوق بشر معرفی می‌کنند، در حالی دیگران را متهم می‌کنند که دست به کشتار انسان‌های بی‌گناه و حمله به غیرنظامیان می‌زنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/689080" target="_blank">📅 20:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689079">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1bf8d4aeb.mp4?token=LvY12ac8ISFFfUCr3u32UyY1UEAnWyO3utj1TED3blzeKJGpIu1o6x80e51GqT-berTCvrRncRk3dC2SgF1M0X6SEKBF-R8Ba_mxLWFVPwStAuKMW33749ELizhS91MwsMhdNVQjDv1d2ccK0NL43pcDjSHtpyvEuI1ZOk8-HIzyonUu-pRGzRyrD8UI2NxHygJPNA1XccZiQfo2Ro_B-Qr1w-iwKe0QyBhLFFcRPfjI61PwR0UnLIXT8iGaE4mr1Ktr6_UB3025nj8AH0lIibXPYTGNpAoezjj6YM1-xbw3UN3HZ_R4uf6CQStg44_zlm4RPvDdRbc94s7umkp47WthgurHYHsw7pYNJ7_J87izQ_dF5MU-sjY6AW2YkNvcxpdjuDv8Lb3hNIYUzPyY74bjo8vfBWrhKYKoGE6eaqSqvclIrCZN5d6BcYrRSyP_7DE-DeCcQf0TtZQ-M36v0DC-WTd476whk86KaZ-O7sTWRPDe-gfmCLQ-YzhFIWCyWDlv0-NlQoO-NEQY_z08TGphCNlBrnOg3OzH0iH3W2E30k4JuGTwTlASIJmmpFGS3i3VLHkdiqQEyFMCfT1UR48DSshbzgUvNUc32MY-sX2zK6YVvjTeXrWNsVvGHoLitXeALAfn8KdRvUCnCUDkK1lU3U7iakcGb8xg-B7HWkk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1bf8d4aeb.mp4?token=LvY12ac8ISFFfUCr3u32UyY1UEAnWyO3utj1TED3blzeKJGpIu1o6x80e51GqT-berTCvrRncRk3dC2SgF1M0X6SEKBF-R8Ba_mxLWFVPwStAuKMW33749ELizhS91MwsMhdNVQjDv1d2ccK0NL43pcDjSHtpyvEuI1ZOk8-HIzyonUu-pRGzRyrD8UI2NxHygJPNA1XccZiQfo2Ro_B-Qr1w-iwKe0QyBhLFFcRPfjI61PwR0UnLIXT8iGaE4mr1Ktr6_UB3025nj8AH0lIibXPYTGNpAoezjj6YM1-xbw3UN3HZ_R4uf6CQStg44_zlm4RPvDdRbc94s7umkp47WthgurHYHsw7pYNJ7_J87izQ_dF5MU-sjY6AW2YkNvcxpdjuDv8Lb3hNIYUzPyY74bjo8vfBWrhKYKoGE6eaqSqvclIrCZN5d6BcYrRSyP_7DE-DeCcQf0TtZQ-M36v0DC-WTd476whk86KaZ-O7sTWRPDe-gfmCLQ-YzhFIWCyWDlv0-NlQoO-NEQY_z08TGphCNlBrnOg3OzH0iH3W2E30k4JuGTwTlASIJmmpFGS3i3VLHkdiqQEyFMCfT1UR48DSshbzgUvNUc32MY-sX2zK6YVvjTeXrWNsVvGHoLitXeALAfn8KdRvUCnCUDkK1lU3U7iakcGb8xg-B7HWkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
ظهور یکدفعه اتفاق می‌افتد ولی ما یکدفعه نمی توانیم آماده شویم
🎙
استاد
#محمودی
#امام_زمان
(عج)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/689079" target="_blank">📅 20:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689078">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VihhVoH0jf9ZXbYXj2sPfjZgPpRnxSkE9wv3OlBy3sn0fDjhHQnVfbVx8LwvY3D-YgtSPA0lOQdfal39z5nto6wDd0h-x5OQMeaYsZDJJUIURxBiTKlVQpgbMRJQNRhGcfNNPfr5Cj4UIyvMKzEbv8iWsDNqyq8IuUND7WK6VaobLtRfGj8SCl0CeABNYm5c6dATvAWeT6E7vEoyGcly65t9mN52k6mNulj8D51zCWW7E47G1_w_Wv3C2gLJ3_ep_T9SC4MXy_DZh-NzirLw4e_70I_moiW5I0NSwPozvk3ihql56owsvgIYH_BVsFM9jw7DrhO8pvp4DAFRXqJ5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش توکلی‌زاده، معاون امور اجتماعی و فرهنگی شهرداری تهران به حملات برخی جریان‌های سیاسی به اجتماعات مردمی: دشمن در کمین کمرنگ شدن اجتماعات شبانه مردم ایران است مبادا با دشمن همراهی کنید و یا در زمین طراحی شده آن‌ها بازی کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/689078" target="_blank">📅 20:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689077">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ایران اینترنشنال: به ایران بمب اتم بزنید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/689077" target="_blank">📅 19:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689076">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07a7d03189.mp4?token=LnxDcnsEY_pAnE7Vnp1U3n6whoy3A5hey6Ud7K9ZrghXQV0aB_SSQt_MeT73es0oGo7mXwj-dFPk21UTkf2IzDtpdPUB5pqSo_tvVhnt0P6v2cGxHNriKgQxtZfdwVe0TyydksuxCeTANVeyAl6lO1t8tzRQpgWiPB0td078TUNrucKsjnCvplF49SSY5kPpwMq-HvpS3_EUgAPKI3f8Hf_j7EHx1_iMzdT5a8_zOIMK6ExPduAxMFI5m76DVH_gk-DmmfAhOqPWlWLB97NGCgxdjKxnYq_4cRTSWd9M8TnY1MXe8RmHlyLGdtBNa1V9zs89AhzG6icrW5FqACwMDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07a7d03189.mp4?token=LnxDcnsEY_pAnE7Vnp1U3n6whoy3A5hey6Ud7K9ZrghXQV0aB_SSQt_MeT73es0oGo7mXwj-dFPk21UTkf2IzDtpdPUB5pqSo_tvVhnt0P6v2cGxHNriKgQxtZfdwVe0TyydksuxCeTANVeyAl6lO1t8tzRQpgWiPB0td078TUNrucKsjnCvplF49SSY5kPpwMq-HvpS3_EUgAPKI3f8Hf_j7EHx1_iMzdT5a8_zOIMK6ExPduAxMFI5m76DVH_gk-DmmfAhOqPWlWLB97NGCgxdjKxnYq_4cRTSWd9M8TnY1MXe8RmHlyLGdtBNa1V9zs89AhzG6icrW5FqACwMDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپ پربازدید از مقایسه استقامت گوشی‌ها در طول زمان
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/689076" target="_blank">📅 19:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689075">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
صدای شنیده شده در قشم تست پدافند هوایی بود
🔹
در پی شنیده شدن صدایی در محدوده قشم عصر جمعه، منابع رسمی استانداری هرمزگان اعلام کردند که این صدا صرفاً ناشی از اجرای تست پدافند هوایی بوده است./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/689075" target="_blank">📅 19:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689073">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWGzsisJ131ixChw-9S1j1LXtfhWrP14z5M7BkKKI7xMOiiNHu0So4MM0kGWinFHW6VoOsDEUJ2yYVlMtPPDcvPly_HrhQp9ojPK1swEiGiMm6pqlJSapTI-HroJbw-hcUlNYUA0n25EWklN_Qkv7lU5j2WmAQezDNJaht-TP4HSAryGP1bJIv0puzG132aS7_yfrPK17yDofpjbWtTQiDm0AJ-cNm3Lrgjtuk0doFnfB81De1qRBf1Nu0O_MdSF2tLab7o8zd1Ck7RhaZImWSLKozzB1lMUhSHtciYXQtdxwqH5btljHXCXCmaK21QrOiZSbAUHQlP9xkJ3OhBfxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZt5RhI5aRW7_4DsQF4AXYB26OwzF3JRLl8XgWa9ECm7FxIsuYAH_w0KLI0zroSH3zPDe8WtrclTnRXPubXoJu9dOBVP5oKtcIyPvRYahZoZOyXvVtBm7KAI0BdljpbOwDyH8jc_Hpl5hfvSADl1gxsw08MDe0XWLUZhujl3kiKsM5OoHll9dzhaEK7wrIPlF3iLhahjqGSVnaccSLuK3ArSqvAxpulSHv14orbbMBpVNdiCV3UNhIZxfjUyuCDmQmFwHFS_hhu1CZ3mYpr-ZNj0Q47Fd8Wy-RY5p8C-hUqXTfn2wKzK37xGnocvxF4dmH7qnGH5JXcT5CGC9x_C7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت زیرساخت و تجهیزات تونل‌های جاده‌ای ایران چگونه است؟
🔹
استان تهران با بیش از ۴۰ کیلومتر، بیشترین طول تونل‌های جاده‌ای کشور را تا سال ۱۴۰۴ به خود اختصاص داده است و پس از آن لرستان با ۳۳.۸ کیلومتر و مازندران با ۲۵.۶ کیلومتر در رتبه‌های بعدی قرار دارند.
🔹
در شاخص تجهیز به سیستم تهویه هوا نیز استان لرستان با تجهیز ۵۱ درصد از تونل‌های خود پیشتاز است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/689073" target="_blank">📅 19:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689072">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPJ9TSW84g4RibnNdUc0vU9m6PcXN7GYPr6fLXSaOzUeSH5LueyA7oNbaaiL8ZOuD8g1MIu4sM2trI0wZzCWwVQxU5muKpNO47yO5XwLsxWZArqbMF6VuTPycXvIO3KxQdqHnXchXM_yAENkyfMIy92wxjtBzpUZwi6FuBArZ9WEno-2lLwJv6lTqxFjUvWaXZh2EfB4_QuwtGr5TFoaEP82z6TxdczG5n8-YTtL9PMavCtsEc2a7evPx673AFWU0wce4eMGPkBi_ztnxrp9KzbN7QzWDRxaep5awqEFK15AHUSIuyDmJ1b4Ptqrn3s-Ahyp3GGk4CW3g31PF7WAMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: گرفتار ناترازی روحانیت هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/689072" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689071">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رویترز: هزینه حمل نفتکش‌ها در خاورمیانه به رکورد تاریخی رسید؛ هزینه انتقال نفتکش‌های غول‌پیکر از خلیج عمان به چین به حدود ۱۱.۵۰ دلار در هر بشکه رسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/689071" target="_blank">📅 19:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689070">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irTrfGO5DOWRayvud2iaYTAaSveDKx4BX_HGvyIXLHfy6u11qJUqRDM5zb06qay7hen_MvBWpoO8MtcJNhm2pa2n8CadAgIB04nulBtgro98zQy6_FN8NJA7APZErXz0Y3RlYLKsOMMlo6bxm5zNlWF0gogW6HhrmQktRwLSLi7LLJMbgO73E9wELDibqRJLXE6ZANkgod0qmeoCTEoV8u_K-Qmdcg-5k6x0KCFAglP9SsD90GamrRbYa0IBi4nK5uszxBA_JDm4vU5QZX9S0HgBAGhknhfxKV2F3Va27TDKjvHKxDd251kYiM03WB_VtYBP4ciDiI7Ut64t85SIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها در راه است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/689070" target="_blank">📅 19:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689069">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjucvRtSR3ks8tXiNTk9G3jjhVQfIcp6B5KZ7BW2jzo18mAXc4USWSk82BvpYE9aqQqBUK1-_5dkC158kdAqCqMDbth3z97q7du4u_Frn-eA9qoiDuQnE9d2hRNQvnnsXoVuS-LU9M1z3l_a1gXMngNzbgbJGpuh9ZTCxWwwelg8ktyjPjqZuPBvRe7AQ4njUzDE8FfIuUdYi0k223X9hgTBpO91Yf-8Jgzss1cnPmaZT58aMe61dXaR8qJ_VVxBna9ane0SADV4pGcHIgehM_KkVcKj9jFw8KASDF3Mg6JSnEBqHL3bK9kTDtBvycQC1ItOTL78depPOji8op5Jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار انصارالله به دشمن سعودی درباره حمله به زیرساخت‌های یمن
حزام الاسد، عضو دفتر سیاسی جنبش انصارالله یمن:
🔹
در چارچوب معادله «تشدید در برابر تشدید»، هرگونه هدف قرار دادن زیرساخت‌ها، فرودگاه‌ها یا بنادر در مناطق المخا، ذوباب، میون و دیگر مناطق یمن از سوی رژیم دشمن سعودی، با پاسخی مشابه مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/689069" target="_blank">📅 19:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689068">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231591cfd3.mp4?token=qXF6lGwUVgq9RzzGK7PqcSChQJpu3NLFLSR8xkpeftFA4BpZi77TxhbvFe0pzMojy7nWFC784dvKnEQWYj9XJRiKYCoILUbYwWQ1YYMTkNuv6NlRZkBJct3T31ryL-YgcrHmSCLp8_e1jcaU8BpFP88Qv_VRSCFQL7_AhjzneeQ9QaonYiaNJUhsk8cHw0BhVIhd-CeFgI-XB8rglBS4wBX_3FTNqa_ataT4DNKHu6ad2ae8LHv6Jjuy0dLabFmBCHYvnIogQlYxBu-GxdDLbeFUASSQzeEMOJHG79Pa9EpnyySDMFrIU691XEURD-zSQSCe0AvMDiaFBcDSHIlVDZ0PIfc29b3DumJ1hCinCPlMrjH0ttcX-12qqzUj_-MRFB7wVZxTmnqG_d38QiiBzPVbM8VcVoQUznBV0spOimUsIFLu6SxDv2XRCkLr7M6Mge-FZJXQe7aOOTmh8KV03ydW_AWLnqIHRnGNiiuErfcjXkFl0yZ9gmFwhp1SL132HDr9nsq3PcbmuZCsC3Q931Kis69CDRXAflNB2mnucQULO_Fw-NcY9tkx-r1a0bSUckn0hRf3F_kvya1n29UTd3z83MqcgY3O-nI9AgmiDyzATiFKiHkJEZd5HuB8tBG-P653t4F0laOdggFcTzY1klxRYVYFhJxyxwbIDQHmSWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231591cfd3.mp4?token=qXF6lGwUVgq9RzzGK7PqcSChQJpu3NLFLSR8xkpeftFA4BpZi77TxhbvFe0pzMojy7nWFC784dvKnEQWYj9XJRiKYCoILUbYwWQ1YYMTkNuv6NlRZkBJct3T31ryL-YgcrHmSCLp8_e1jcaU8BpFP88Qv_VRSCFQL7_AhjzneeQ9QaonYiaNJUhsk8cHw0BhVIhd-CeFgI-XB8rglBS4wBX_3FTNqa_ataT4DNKHu6ad2ae8LHv6Jjuy0dLabFmBCHYvnIogQlYxBu-GxdDLbeFUASSQzeEMOJHG79Pa9EpnyySDMFrIU691XEURD-zSQSCe0AvMDiaFBcDSHIlVDZ0PIfc29b3DumJ1hCinCPlMrjH0ttcX-12qqzUj_-MRFB7wVZxTmnqG_d38QiiBzPVbM8VcVoQUznBV0spOimUsIFLu6SxDv2XRCkLr7M6Mge-FZJXQe7aOOTmh8KV03ydW_AWLnqIHRnGNiiuErfcjXkFl0yZ9gmFwhp1SL132HDr9nsq3PcbmuZCsC3Q931Kis69CDRXAflNB2mnucQULO_Fw-NcY9tkx-r1a0bSUckn0hRf3F_kvya1n29UTd3z83MqcgY3O-nI9AgmiDyzATiFKiHkJEZd5HuB8tBG-P653t4F0laOdggFcTzY1klxRYVYFhJxyxwbIDQHmSWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاسر جبرائیلی: ایران ظرفیت سکونت یک میلیارد نفر را دارد/ به هر ایرانی ۴۰۰ متر زمین می‌رسد؛ زمین را احتکار می‌کنند و به مردم نمی‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/689068" target="_blank">📅 19:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689067">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
یک دوربین امنیتی، لرزش خانه‌ها را در نتیجه انفجار  در تپه علی الطاهر ثبت کرده
🔹
زمین لرزه ناشی از انفجار علی الطاهر تا ۴/۱ ریشتر گزارش شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/689067" target="_blank">📅 19:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689066">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvgN0_OyxX6RrRt4jzYCkAOjcDGQ8oR5pcNl8JnqHm7UM77sBU6-SUsbWD1g1vsNGgESzeUQ-s-suulefAqpH3WECxTo8RSxFbiadcIiikvmJzxtPdFKuxH184Ld16f2pk0DrraIyZi5v5O_gyVeniFdAgyO2rhQwR7DbS54ULlHxUGQ9ZiSg6DX8k_8Zvw3vVQ9qkd6_dDg5SM3M5H2RtdWLfdyZr5NNIsMAMzQmG3wKXZuTMX3Kyb_htlnXXimcb9R3KuUXe99T2f7A_yzo5e7yI6OScwW4bs6mAYPPKl2uvUsvEJ4aUiY0ffxen2TcuX6kJu0AsguL4zY-sAMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هتل رو از جایی بگیر که بقیه می‌گیرن...
🥇
علی‌بابا، رتبه یک همسفری
🏨
کامل‌ترین پوشش هتل‌های ایران
🌍
بیشترین تنوع هتل‌های سراسر جهان
⭐️
بررسی نظرات مسافران و مقایسه هتل‌ها
💳
رزرو با نرخ‌های ویژه
جستجو در علی‌بابا، مرجع رزرو هتل در ایران
👇
https://albb.ir/8g6Rx3</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/689066" target="_blank">📅 19:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689065">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: استفاده ایران از هوش مصنوعی آمریکایی علیه ناوهای آمریکا
وال‌استریت ژورنال:
🔹
ایران از مدل هوش مصنوعی آمریکایی برای ردیابی ناوهای جنگی آمریکا استفاده کرد.
🔹
آنتروپیک مدعی شده این مدل برای تحلیل تصاویر و اطلاعات و شناسایی نقاط ضعف ناوها به‌کار رفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/689065" target="_blank">📅 18:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689064">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyvNiq39iodp6LJa2Bg_rTvmR72WYL_a9UZLFcIqTmSXBVJnklax4eEHo6-97E4wh337rES64GsCLjvdAokigsvRV0tmz1RyLl7OEGNits7ic9o3biR0IjRumAGIqfFtIrXm_iXG6vKOLMIN7rVbz1LqGq02-BKknXL1kBnzaYmZSMOlrEJVOe2ORdex1GAe1RFrrE3O5xn-YkGZpxL5bBvUt5Av-Lyrc7AhTqoMqMVsgwidIT3Ji2hJMZARQpPrNSV9y6ayQZ7OMvbmy_G9ZlH6aCz8Vmc8d5K51ZqqWqzVf2cKjff-Q9M0yrpuZSMcfLFujff_HHhZmj2VOYEZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرز تهیه ۶ مدل قند خوش‌طعم و رنگی؛ مخصوص پذیرایی
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/689064" target="_blank">📅 18:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689063">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
تبلیغ دارو ممنوع شد
رئیس سازمان غذا و دارو:
🔹
معرفی دارو فقط در چارچوب علمی و برای جامعه پزشکی مجاز است و تبلیغ مستقیم آن برای مصرف کننده ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/689063" target="_blank">📅 18:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689062">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
هشدار مدیریت بحران کشور نسبت به تردد و اتراق در مسیر رودخانه‌ها به دلیل احتمال سیل
🔹
این هشدار برای مناطق نیمه جنوبی آذربایجان شرقی، نیمه شمالی زنجان، شمال قزوین، ارتفاعات تهران و البرز و دامنه و ارتفاعات استان‌های گیلان و مازندران معتبر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/689062" target="_blank">📅 18:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689061">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVYTfRKdp3xFNfkvTep6WGq24QpIkod7Fk-JkGE96UUYfAKn1NJg_u4x_6o7PawOCrCmKyPdJZJtCB0eiMnLZMdKQMpD-IyhMWntDcWFx_g3TH46hieG3BcSdGD99xt-v6oStxaxTNrjfH3YfVDUeG57axqktN-q_OEubQ8xjD7BuUrGNYUxFyYQy4SGizghvIN4mEYugDp-szT7uV5i8F6MNfolmlW_LSMjj5EpAoyL_9wLjsJhq0lEMmgnfiI5hvHkdWQDHH9nCoggeg-RjDPQcpEyExdMijOZO8jYT9JJdB6rVlPkB5W9gjfmhf1iqzFCQOhkDSgt9DCDP9d87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانبرهای عمومی کامپیوتر به همین راحتی یاد بگیر!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/689061" target="_blank">📅 18:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689060">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P93OmX3s1LCM8jaNvs8SVS1PMOeWRLfLsceRDqyVkM8T0JqynXG5axw8rqjhBkkU6GNfGQ1Fq-YNVyOYfF5j9CZqX2_IdKYZ7Zteegz1GcL1_AGQuqIr-O3gS14NvfeyrviXCj3tInSwRVwGH1VCHM7yVMO-KPyA6zBIcl5cMQU6lX5z9ttVzblqiNrd_PZoxxYaBN3lm3anhLakFSRFc_iY1SfqE36xOKmokFaVnCRwT5Pv9DB3fuikbsYOAAso-puUaAYUK7f69SJ5KsE3cOdWrS4OyfIYvOD2wfWsJguosMFBPImGU_zlPj-G3R2IIgsDcatdX8cETDjSw8mLTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرفوری / تنگه باب المندب به تسخیر رزمندگان یمن درآمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/689060" target="_blank">📅 18:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689059">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaaafda3c8.mp4?token=cHJeNXsfv0zMDlvQal-4Sg3wI0ra8crJz8G476vYXHTy2EOVjr5KhGsFM76diFiidbSzvw31tpwAN8dxS_vhFR_13LOQ3JSMtXjrmgqnDs3cxwcq-vDpsLAqqn2Tt0tc9jCEeSUNLXCupQBsQntKwF6N0vvc9qZWblKXd2dXRpOlbFGWSeSwmyxX7v8n7OLIn8fFZoVJws0GA5NnlS5apT_OFZdDcQ0wAJYCBkWn3feYDuImiGGAoEXWl0ohiEWkgx9M9y19Qxss3A-_h_N8Yi9GWBLkV5ll7-resDn7f0VoP4Oo4bNI3Vb9FUcNN3ot3fpWf9u5FPhq05SjyPsy3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaaafda3c8.mp4?token=cHJeNXsfv0zMDlvQal-4Sg3wI0ra8crJz8G476vYXHTy2EOVjr5KhGsFM76diFiidbSzvw31tpwAN8dxS_vhFR_13LOQ3JSMtXjrmgqnDs3cxwcq-vDpsLAqqn2Tt0tc9jCEeSUNLXCupQBsQntKwF6N0vvc9qZWblKXd2dXRpOlbFGWSeSwmyxX7v8n7OLIn8fFZoVJws0GA5NnlS5apT_OFZdDcQ0wAJYCBkWn3feYDuImiGGAoEXWl0ohiEWkgx9M9y19Qxss3A-_h_N8Yi9GWBLkV5ll7-resDn7f0VoP4Oo4bNI3Vb9FUcNN3ot3fpWf9u5FPhq05SjyPsy3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای خرابی ماشینت رو خودت تشخیص بده!
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/689059" target="_blank">📅 18:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689058">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYfzMgp7wkfYD8IDOsYa07E3ZsnEKoYNE1iyLOBLa7GuU6mQAPfyeYs59547M9S9blay0Esu4sUMIRywFsgZma18fyCemmooHXjar8F75Ms_5IjV9p9RwMMUlpOc_2E-FpX9wY6oHcKQ9mJhgdd8ib-dd5luf0jBc34NJNJWJ8yx90U3K0umuE3squq0Qyj9Z3VwHzKTBuYeHxTcGdgGf5aE8rmBMsydx18Tm42QcwKSePf84FLL359ocxE4L5qug_w7Cb2h8ZN6Q56PexNwPXSVsWv2j5hd34XSHbXqM0D3KCI-VSUVzpEdiUyVDRbsiy2IBnSTs7xwG5w0p-3vVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهروندان کدام شهرهای جهان بیشترین زمان را در ترافیک تلف می‌کنند؟
🔹
در میان شهرهای مختلف جهان، لیما (پایتخت پرو) با هدر دادن سالانه ۱۹۵ ساعت از وقت شهروندان، بدترین وضعیت ترافیکی را دارد.
🔹
دوبلین ایرلند با ۱۹۱ ساعت و مکزیکوسیتی با ۱۸۴ ساعت در رتبه‌های بعدی قرار دارند.
🔹
تهران نیز با اتلاف سالانه ۱۸۰ ساعت از زمان شهروندان در ترافیک، چهارمین شهر جهان از نظر هدررفت زمان است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/689058" target="_blank">📅 18:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689057">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای گستاخانه ترامپ: ایران حامی شماره یک تروریسم در جهان است و هرگز به سلاح هسته‌ای دست نخواهد یافت./ الجزیره
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/689057" target="_blank">📅 17:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689056">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
مینو محرز: واکسن آنفلوآنزا به دلیل جنگ و تحریم در دسترس نیست
متخصص بیماری‌های عفونی:
🔹
سال‌های گذشته، واکسن آنفلوآنزا طی چنین روزهایی در دسترس بود. شرایط به نحوی بود که نه تنها واکسن در کشور تولید می‌کردیم، بلکه واکسن به کشور وارد می‌شد. در حال حاضر، واکسن آنفلوآنزا به دلیل مشکلات ناشی از جنگ و تحریم‌ها در دسترس نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/689056" target="_blank">📅 17:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689055">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
گزافه‌گویی وزیرجنگ آمریکا: ما تنگه هرمز را کنترل می‌کنیم و به این نبرد پایان خواهیم داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/689055" target="_blank">📅 17:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689054">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/689054" target="_blank">📅 17:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689053">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a5c03b6f.mp4?token=aL7QGtZEo1-vO4yumLsM0QJZN1s3mAX-J--wrcZ53QEC38uulvfEyGftlWkKsfmzcJZU3tX70IxV7BDtjWOieqCKYQb072GDD4FjSfsvm4pVwJdNCeh8Xu61H4DkRiUvw8V-TTtiI9RCzfTz6rhJfTQVsb2BIiH3OXtxy81uhhgDkETvYbVRq2wkhxzCbfoH8xrejJMKIdk-CziEOI8npHsVwQtaWlZESVlqrDQVhLfLYZUqkCaj2L2FlkzH8j-QBmvA2gb1O8usVJRA2__jrVQyfqYLvzby4KeejSzjvAZbuDWX_2T_cahIYmqmzU5XAE4BROW6Lr1W3SMNqLRVEhgZl6Kpq3fkVn4LnUwCX2WXwAnyGSXPxZz9cyx9qrHj27PEXXisZ5UW_0Bg7c4sATc3JBF4UdrWSyOrGD9BSpjQPtTXA3sSh_zwfutA-TIFFAVAmvQn1ELH88NvFNVhBPZLdHgkWjmyW2S1G6h-H4T0tljfW_wfmYsOd8oV0dD5W_YyAVB0Z3SC-k149VrlWiBqbO4JrqpNoGr3NAUxg7Cb-KpBEt4B9ngh6oiy6442D7wueO9uL1m-XdmKDR_3j41O7GoHPx5rI0BxOPozJf1Puge36SK1j_1Z7potgGI9eb3ujJmHgV7_y32wtWOk95sBCZupRTaxg-0M14rTTRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a5c03b6f.mp4?token=aL7QGtZEo1-vO4yumLsM0QJZN1s3mAX-J--wrcZ53QEC38uulvfEyGftlWkKsfmzcJZU3tX70IxV7BDtjWOieqCKYQb072GDD4FjSfsvm4pVwJdNCeh8Xu61H4DkRiUvw8V-TTtiI9RCzfTz6rhJfTQVsb2BIiH3OXtxy81uhhgDkETvYbVRq2wkhxzCbfoH8xrejJMKIdk-CziEOI8npHsVwQtaWlZESVlqrDQVhLfLYZUqkCaj2L2FlkzH8j-QBmvA2gb1O8usVJRA2__jrVQyfqYLvzby4KeejSzjvAZbuDWX_2T_cahIYmqmzU5XAE4BROW6Lr1W3SMNqLRVEhgZl6Kpq3fkVn4LnUwCX2WXwAnyGSXPxZz9cyx9qrHj27PEXXisZ5UW_0Bg7c4sATc3JBF4UdrWSyOrGD9BSpjQPtTXA3sSh_zwfutA-TIFFAVAmvQn1ELH88NvFNVhBPZLdHgkWjmyW2S1G6h-H4T0tljfW_wfmYsOd8oV0dD5W_YyAVB0Z3SC-k149VrlWiBqbO4JrqpNoGr3NAUxg7Cb-KpBEt4B9ngh6oiy6442D7wueO9uL1m-XdmKDR_3j41O7GoHPx5rI0BxOPozJf1Puge36SK1j_1Z7potgGI9eb3ujJmHgV7_y32wtWOk95sBCZupRTaxg-0M14rTTRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی قدیمی از نتانیاهو در کنگره آمریکا؛ طرحی که از تغییر فرهنگ و سبک زندگی ایرانیان سخن می‌گفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/689053" target="_blank">📅 17:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689050">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09abc8db34.mp4?token=pbvEzNagOPerwB46ZyVaN3rtpDyIQ50ANoBOQVl-516kmy88uVAf1bmc-quvoMrevOHPPkwkOOrTCjde6QNTNURlUUpzQLp-Qkm-XLijcUV5VEM2eBYVid5hTFbCcYLJ0TzcDI4w-dCxN0PcAC_O_02WELC_T_ZrtijmKlwMxjpacQ1z5j178Y_MK_3mH0PTAJfYUSAmUWlbl6Ct_LmtkH_cKokaGHA2tPJ-Hiuf6Y0MMtM6FgXviHtONTIbPE2jgeV_dM3Bc4VThjJQ-NcpLctpoElUheNbQW5iOPj3DqTZNkLYxtjrbyNGipuoNsQ4fsHp73_Oz7To-rElFt73ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09abc8db34.mp4?token=pbvEzNagOPerwB46ZyVaN3rtpDyIQ50ANoBOQVl-516kmy88uVAf1bmc-quvoMrevOHPPkwkOOrTCjde6QNTNURlUUpzQLp-Qkm-XLijcUV5VEM2eBYVid5hTFbCcYLJ0TzcDI4w-dCxN0PcAC_O_02WELC_T_ZrtijmKlwMxjpacQ1z5j178Y_MK_3mH0PTAJfYUSAmUWlbl6Ct_LmtkH_cKokaGHA2tPJ-Hiuf6Y0MMtM6FgXviHtONTIbPE2jgeV_dM3Bc4VThjJQ-NcpLctpoElUheNbQW5iOPj3DqTZNkLYxtjrbyNGipuoNsQ4fsHp73_Oz7To-rElFt73ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غیررسمی| وضعیت مرز بازرگان/تعدادی از هموطنان‌مان پشت مرز ترکیه ماندند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/689050" target="_blank">📅 17:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689049">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
وزارت خارجه ایران: روز دوشنبه با مشارکت عراق و کشورهای خلیج فارس، نشستی در مورد تنگه هرمز برگزار خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/689049" target="_blank">📅 17:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689047">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQeOr99T268VBCoNwGTSY4ttfqhvXwefgGwP_Vipe-Zx3L1FNuXwfyOKZ_L_BheytMVh_WxyUsFWb_PJYBohat7AJosj9n0FECcphYzTglSuvbkKCdtp6MY3AQxRGQBGCeH4aWNaGp9wHYCt-6LfZkZ7h80U4pyX-Jkx3jWCga5P_xo7epwzQOxLyki8mgbtsp88i0Gw3DA8IPQYIXIRCpon2YoB-JFhUsykEJ4P6dpo81PHQEyllHpLAGG0LEuQrd7fM5opb-xst_wrX31PUTBitF3saGlNCewS1d0Ce9Ov6bVC1ijF43G_mupZ-as6YQo4JsNNE2MfUuF77z9YBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از انفجار در خط لوله نفتی شرق–غرب عربستان در جنوب مدینه منوره پس از حمله اخیر یمن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/689047" target="_blank">📅 16:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689046">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd837a201.mp4?token=NyeIEqPLAw5s0Z0cgaUFVKUWMRCxZ3OpyzbZDdLCQ80V9VxInNIfp8xrv3J-c2LWnadr0CwOjqJWzZwnafFhbe7J7nhxYPchjsfKtWpgX2_RM_la8aK4mgKZVWNf33NKG33NSMaUH7KDOXIo8H4glfAwQO4CtnAcf53MWqb-4Q6RUh006GdvAqnvHA0hMa7db6t3whtTHlwhaHf0hCfK0gXgCgywa20AYH-CjUGeRcu5wfgYAANi2Jyqox00gM9MxMVdRZXQUPpbQI0r0oOJlHdVh8ArxD1VizLegrmaJRKOELdWjE0xOsIBPA5pusz-KUq71Uw1wOZpzcBxltvR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd837a201.mp4?token=NyeIEqPLAw5s0Z0cgaUFVKUWMRCxZ3OpyzbZDdLCQ80V9VxInNIfp8xrv3J-c2LWnadr0CwOjqJWzZwnafFhbe7J7nhxYPchjsfKtWpgX2_RM_la8aK4mgKZVWNf33NKG33NSMaUH7KDOXIo8H4glfAwQO4CtnAcf53MWqb-4Q6RUh006GdvAqnvHA0hMa7db6t3whtTHlwhaHf0hCfK0gXgCgywa20AYH-CjUGeRcu5wfgYAANi2Jyqox00gM9MxMVdRZXQUPpbQI0r0oOJlHdVh8ArxD1VizLegrmaJRKOELdWjE0xOsIBPA5pusz-KUq71Uw1wOZpzcBxltvR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیفون تاشو اپل؛ دوربین نامرئی زیر صفحه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/689046" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689045">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
یمن: ۵۴۰۰ کیلومتر را آزاد و ۹ جنگندۀ سعودی را سرنگون کردیم  ارتش یمن:
🔹
نیروهای متجاوز سعودی از ۶ شهرستان در تعز و الحدیده بیرون رانده شدند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/689045" target="_blank">📅 16:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689044">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxWTU1j-qU4R1j3-eh3y1arMds8bcAixspHNmwI2SR0HLUBJ_plYTfr5VFJCod8HKR6wVhTAHQJEQBy1XBAHOeKGEnLqqKSb0Lrap9FVOIs5JuKZsC4JtJjyrUe-SOntvnkCbdyX2zktmiKxCVlAV_L8x4OY7OGdHT8Q_q80enrGt6tR61vwkzz6zQP6GFJA0Tjupc2gDwuENY2o6DKkze-kpe9kdrSwcqagmHZCoBGTcxnYxALIzZ7HGs5x8wSYIvAYC9TJb6vdGfsySQBguYjf_jiVH0acCo_vDKpu_UAwc3A0xo_PrXKL2ldV97WkW6SpFVp12dDeLQqg5ZmleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: جهان روزبه‌روز اعتماد خود را به نظام مالی آمریکا بیشتر از دست می‌دهد
وزیر امور خارجه:
🔹
وزیر خزانه‌داری آمریکا با خوشحالی به خود می‌بالد که می‌خواهد ایرانیان را فقیر کند و اقتصاد ما را به فروپاشی بکشاند. اما در عوض، او درمانده و ناتوان در برابر افکار عمومی قرار گرفته است؛ در حالی که جهان روزبه‌روز اعتماد خود را به نظام مالی آمریکا بیشتر از دست می‌دهد.
🔹
بحران ناشی از هزینه تأمین مالی بدهی‌های آمریکا تنها آغاز ماجراست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/689044" target="_blank">📅 16:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689043">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30e945671e.mp4?token=a10QDNdzpJis2HySyeRucV1vle0R8BLEK5bAvejQExSH0fv5ch5r1eZBW5zvlix4O_O5TAOwhtx54AHVoMw8jNqq_b5ArO8D9QWUtoBOUwtQ4IHvKpMroE2dmx2rAwcgZClIjXzjK-KQXwdFPlKh3SgusA2AC9IwkCi27yqmqJIgx4CUR9eoZpYV2XiJVj_jUYE82bGZ2vMtXOs9QIIzkk6gXxRkCsu9_3HIUFMDP6GbGxZ4LklQCUPNZUW2MHkJnyJJpc2Txv0sjFSz2k3YSNJ6XlHONcnn8UG1UdN8P2HPxsj2Yh3Rf7k00s0ZIO1iBfTGFd0R4mQGlvgnDwXaZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30e945671e.mp4?token=a10QDNdzpJis2HySyeRucV1vle0R8BLEK5bAvejQExSH0fv5ch5r1eZBW5zvlix4O_O5TAOwhtx54AHVoMw8jNqq_b5ArO8D9QWUtoBOUwtQ4IHvKpMroE2dmx2rAwcgZClIjXzjK-KQXwdFPlKh3SgusA2AC9IwkCi27yqmqJIgx4CUR9eoZpYV2XiJVj_jUYE82bGZ2vMtXOs9QIIzkk6gXxRkCsu9_3HIUFMDP6GbGxZ4LklQCUPNZUW2MHkJnyJJpc2Txv0sjFSz2k3YSNJ6XlHONcnn8UG1UdN8P2HPxsj2Yh3Rf7k00s0ZIO1iBfTGFd0R4mQGlvgnDwXaZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسنت: ایرانی‌ها تلاش می‌کنند مشکلات اقتصادی در ایالات‌متحده ایجاد کنند، با دستکاری در نرخ بازده اوراق قرضه، یا با دستکاری در قیمت نفت با استفاده از اکانت‌های توئیتری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/689043" target="_blank">📅 16:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689042">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
انتشار بیانیه‌ی نیروهای مسلح یمن درباره یک عملیات نظامی گسترده و ویژه؛ به زودی...
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/689042" target="_blank">📅 16:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689040">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/461e74698c.mp4?token=PwC1fG6rpWLSN4wHFtuXkNxrig9ByTI9bTjEz3l_Q2T-RCW21OffynWmSEa2-z2HKX1lmYQFAKMyGDfLcfBKPwlzbOt95UmWckjUitq2YupViBvfthmMictlfWJtStNgBLzGAesdB_qVAbbn9Sdc2KoG-YRa5VVI2zl6l4kV4LYwc6fJ8L6FcTSAV49MEGqjDRt4XHMKEKM4JFURQheMcp02iC_o60L5cthuwflwxhGpU0ILlc1aB2wayV4B5B5g4sc1385XYwG8XrD9S0PsjlU3NxDVpHeRBi-xL6yzosjODIFYu4TNyBQZYjQVIvC1SwiD0yDZYVV6kZASiaZLCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/461e74698c.mp4?token=PwC1fG6rpWLSN4wHFtuXkNxrig9ByTI9bTjEz3l_Q2T-RCW21OffynWmSEa2-z2HKX1lmYQFAKMyGDfLcfBKPwlzbOt95UmWckjUitq2YupViBvfthmMictlfWJtStNgBLzGAesdB_qVAbbn9Sdc2KoG-YRa5VVI2zl6l4kV4LYwc6fJ8L6FcTSAV49MEGqjDRt4XHMKEKM4JFURQheMcp02iC_o60L5cthuwflwxhGpU0ILlc1aB2wayV4B5B5g4sc1385XYwG8XrD9S0PsjlU3NxDVpHeRBi-xL6yzosjODIFYu4TNyBQZYjQVIvC1SwiD0yDZYVV6kZASiaZLCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: کشورهایی که فشار تحریم را علیه روسیه و ایران آغاز کردند خودشان با افت صنعتی و کسری بودجه روبرو شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/689040" target="_blank">📅 16:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689038">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
پزشکیان: یکی از پیشنهادات ایران برای بریکس راه‌اندازی صندوق بیمۀ ۱۰ میلیارد دلاری برای پروژه‌های بزرگ زیرساختی و انرژی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/689038" target="_blank">📅 16:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689037">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
عکس یادگاری سران بریکس باحضور پزشکیان و پوتین در کنار یکدیگر
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/689037" target="_blank">📅 16:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689036">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf797f04f.mp4?token=rs93nVbfm6Wjg4FVpWm_Z8UaZzONPhvjBzMEt8bnl_H2MpRN70-LZDFUenYBR28c5Hp6eCymw8LXIWGWDFtRBd7-MujUgA3qF1PtQNDX5TxkipeSrG7tkQsoydH-HuWUt120gxjpFVy3G25z4ba4cq7Obs9BuNpuKgs9Srde9FaFlfYtvFVxHboQKX4yqhpIKJQem1ORuEjC5LiPjaK5FXgDP0Ef1XlTRUI7lvv5AJwq8yt37iEWNk0As3Fw6VnSJ4QN4beYLbVWbBp-gXsRL299cYHAbbzR72f6j9mDQ9J9WebkWhwHbpngLhiHcrotTqqZdw4d44ypBPhvMYILYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf797f04f.mp4?token=rs93nVbfm6Wjg4FVpWm_Z8UaZzONPhvjBzMEt8bnl_H2MpRN70-LZDFUenYBR28c5Hp6eCymw8LXIWGWDFtRBd7-MujUgA3qF1PtQNDX5TxkipeSrG7tkQsoydH-HuWUt120gxjpFVy3G25z4ba4cq7Obs9BuNpuKgs9Srde9FaFlfYtvFVxHboQKX4yqhpIKJQem1ORuEjC5LiPjaK5FXgDP0Ef1XlTRUI7lvv5AJwq8yt37iEWNk0As3Fw6VnSJ4QN4beYLbVWbBp-gXsRL299cYHAbbzR72f6j9mDQ9J9WebkWhwHbpngLhiHcrotTqqZdw4d44ypBPhvMYILYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس یادگاری سران بریکس باحضور پزشکیان و پوتین در کنار یکدیگر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/689036" target="_blank">📅 15:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689035">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6466595315.mp4?token=XfsTm2GtQCXpUA1-xVNuRZlL1UFqzqLAWHBNlvj6ViYTTc3ZZDgx60UELzNaxJIg4F5bjfblEI6bWt8I6EyGN7e8cL5DvlRJqGfNbSPnk65Xd56LIbw-HGnhpsfijxOAZ63kPIqA6uZThSyBMgV2CRHlmPOILYtv-vA-VsPXaTiEGCuVCCDEOBcoBWlEZ04dQsUIOPRKNg15Dxsxi7Df5mzaLuTMvLxD9sFfSlQwRPZASLgRc74as61Tn5CflRziKwuQpuKbxwJgkDXorDY56FATJUYT1yPrg5fkBlz_2K1NAlQD_oMHyIexSPivtm5WGo6I9GhRVu1g8WBB6kc8sINx5ic3WxCVtB2LzqYCb1amPzkKdE6gcebquZKiG67KcoId1Mq4s1SYtUXqYaXiVEd8gn64lVm57jw_1fQB9AQ2gHpAsZZe1kDXJzxf7ggb9ciAfJosEa1q3QwILwoW-KNfVquvwmoFv-3jwD9cm_jyhVdijg0DA5OgFliZHHbemu8Ll39W6whp9q8HiZL8_L0bU2GjjX9LorhmjiMziWND3p1TNCrvbz8QxANcYY1lmUsc6l6-ppJFBSOYUXZm_VaXtPLD7vDkQVvxjV7lLnBY1kpQ6jVmIpdup4Lf2rAh9ksH0IFILFK6Mg7Sf37DcMP7WA7Ai8yRfkZ9_VYTbP0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6466595315.mp4?token=XfsTm2GtQCXpUA1-xVNuRZlL1UFqzqLAWHBNlvj6ViYTTc3ZZDgx60UELzNaxJIg4F5bjfblEI6bWt8I6EyGN7e8cL5DvlRJqGfNbSPnk65Xd56LIbw-HGnhpsfijxOAZ63kPIqA6uZThSyBMgV2CRHlmPOILYtv-vA-VsPXaTiEGCuVCCDEOBcoBWlEZ04dQsUIOPRKNg15Dxsxi7Df5mzaLuTMvLxD9sFfSlQwRPZASLgRc74as61Tn5CflRziKwuQpuKbxwJgkDXorDY56FATJUYT1yPrg5fkBlz_2K1NAlQD_oMHyIexSPivtm5WGo6I9GhRVu1g8WBB6kc8sINx5ic3WxCVtB2LzqYCb1amPzkKdE6gcebquZKiG67KcoId1Mq4s1SYtUXqYaXiVEd8gn64lVm57jw_1fQB9AQ2gHpAsZZe1kDXJzxf7ggb9ciAfJosEa1q3QwILwoW-KNfVquvwmoFv-3jwD9cm_jyhVdijg0DA5OgFliZHHbemu8Ll39W6whp9q8HiZL8_L0bU2GjjX9LorhmjiMziWND3p1TNCrvbz8QxANcYY1lmUsc6l6-ppJFBSOYUXZm_VaXtPLD7vDkQVvxjV7lLnBY1kpQ6jVmIpdup4Lf2rAh9ksH0IFILFK6Mg7Sf37DcMP7WA7Ai8yRfkZ9_VYTbP0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس سابق انجمن واردکنندگان خودرو: یک سال تمام هر کارشکنی که دوست داشتند علیه مدیریت خصوصی ایران‌خودرو انجام دادند
مهدی دادفر:
🔹
روزی که ایران‌خودرو را به بخش خصوصی واگذار کردند تا یک سال هر کارشکنی که دوست داشتند را انجام دادند. از شکایت بگیرید تا کمیسیون اصل ۹۰.
🔹
منافعی داشتند که ایران‌خودرو را دست بخش خصوصی ندهند. سال گذشته با توجه به برنامه‌ای که بخش خصوصی داشته، تیراژ تولید محقق شده و حتی از نظر تعداد تولید در سال ۱۴۰۴ جلوتر از برنامه هم بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/689035" target="_blank">📅 15:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689033">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0d825838.mp4?token=GvT_1AVQCD_w4UYGk00ALuymvRajamZnhKIl2dZjRHHMJHWUR-bVLJxj9k4YtGVwhOO-MHtPwCW87frEAdBZGX8gecvG5fwar0o-i9Ts_ocCCiTmlgMqJTpQBMTBjyu9RGHvajUramI07qeoFW-FPSivSpL63506jFP4ONwq9_4B7yOb55FIuH-0LNBdEl-AtFWAZHld8cgGmmdzoGk-nSy_kVV2JiDk973G2WOVHx-KZseL2MezdJwNMPXF1vRkX_AeCg-ORcKZFsqYzT5ON6vivP9hwNoioSCpaLKDaHoTQ1DZO12bPbLA0gIUED_KkuAJfBhUFf0aWdepmII3DgWGpaIPyxaTPYh-WdV6IGPpr0k8WJMqLSvSyZuamXUNoGtxvjQr7WHtkSlAGnfarJHx2zL1kgWhKWIsvDr6csQIDPphVoJ_tI67bLWTTnXEp8O18nnytU8ij4J480yIAtSXco-Cp3-YwGR4ujj_1yalSHndNjh4TXBKbOdf-vz7xOoZkXuRT212v_o7X2P_ssbZ6m9cHo_UBasOmkbXhqIJJJilrHUXV4Hr8-4hN-XwA0TI7kXXtWKM6H6vJI2gNKp1PDYsmIudeO_DjDaixLae2kqskbAaGFt153zCrqic8tiuS0rzJ_xCzKXLBNuAhJzwmO3tI-gTPII8KzwVnEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0d825838.mp4?token=GvT_1AVQCD_w4UYGk00ALuymvRajamZnhKIl2dZjRHHMJHWUR-bVLJxj9k4YtGVwhOO-MHtPwCW87frEAdBZGX8gecvG5fwar0o-i9Ts_ocCCiTmlgMqJTpQBMTBjyu9RGHvajUramI07qeoFW-FPSivSpL63506jFP4ONwq9_4B7yOb55FIuH-0LNBdEl-AtFWAZHld8cgGmmdzoGk-nSy_kVV2JiDk973G2WOVHx-KZseL2MezdJwNMPXF1vRkX_AeCg-ORcKZFsqYzT5ON6vivP9hwNoioSCpaLKDaHoTQ1DZO12bPbLA0gIUED_KkuAJfBhUFf0aWdepmII3DgWGpaIPyxaTPYh-WdV6IGPpr0k8WJMqLSvSyZuamXUNoGtxvjQr7WHtkSlAGnfarJHx2zL1kgWhKWIsvDr6csQIDPphVoJ_tI67bLWTTnXEp8O18nnytU8ij4J480yIAtSXco-Cp3-YwGR4ujj_1yalSHndNjh4TXBKbOdf-vz7xOoZkXuRT212v_o7X2P_ssbZ6m9cHo_UBasOmkbXhqIJJJilrHUXV4Hr8-4hN-XwA0TI7kXXtWKM6H6vJI2gNKp1PDYsmIudeO_DjDaixLae2kqskbAaGFt153zCrqic8tiuS0rzJ_xCzKXLBNuAhJzwmO3tI-gTPII8KzwVnEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه جالب از بندر المخاء؛ تصاویری از یک مکان در دو مقطع زمانی، از حضور نیروهای پیشین تا کنترل آن توسط انصارالله
🔹
ویدئوی شبکه الجزیره نشان می‌دهد بندر مخا که محل دپوی سابق سلاح و تجهیزات مزدوران وابسته به آل‌سعود بوده، اکنون به‌دست مجاهدین جبهه حق افتاده…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/689033" target="_blank">📅 15:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689031">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f384f506b4.mp4?token=Bf-2rBKe6SmqxG6jYcimFwOvWoUMRnTLX6G1ZxV1-3x_OfNj1Psb91sC1KUeWXxnQxC9E_PEeSA2cZoq3wqt_mAGj7CWtgUqPquqIeRJxARfcfXfynxNZXOIYGeWwuXC1vgSOsA4SVpOVASu238sNJKfdlk_S2ITf7PXXTZUTWCfodkZOBizRduWLLe8FpQBuRu1zFqDMvr_XtWKTjIveVi-_d-dnjh0Rq-PWIjJnE8ea-A0s4qQ4ul1-7LqJypYA3xZjPX9QvueAtXeIpk-YtV-pWqG9nvJS9fOFj5TKGTkebCIjZ93PAdmLjiW27belzAw1980kxHMSwv1xV8c3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f384f506b4.mp4?token=Bf-2rBKe6SmqxG6jYcimFwOvWoUMRnTLX6G1ZxV1-3x_OfNj1Psb91sC1KUeWXxnQxC9E_PEeSA2cZoq3wqt_mAGj7CWtgUqPquqIeRJxARfcfXfynxNZXOIYGeWwuXC1vgSOsA4SVpOVASu238sNJKfdlk_S2ITf7PXXTZUTWCfodkZOBizRduWLLe8FpQBuRu1zFqDMvr_XtWKTjIveVi-_d-dnjh0Rq-PWIjJnE8ea-A0s4qQ4ul1-7LqJypYA3xZjPX9QvueAtXeIpk-YtV-pWqG9nvJS9fOFj5TKGTkebCIjZ93PAdmLjiW27belzAw1980kxHMSwv1xV8c3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طلا چگونه از میان شن و ریگ جدا می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/689031" target="_blank">📅 15:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689029">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7d8296a4.mp4?token=DF6WVEF6FRInAx2hwykP4jRujBHn9dnY9LmmPqxzn2zzAygSiyU54VeCsR3oyq4uvFn9JzUx4UdMnfHMCAb8HoVCGC7kUSWrxKvJyI1p55IoLtbZqIwpNxYkMjEuKpBjxVzUV4_P_3xTy_ZeyStjnNFC3c6YVzqbfRdlE4V-rRYBvkIbWSvW2wWNyBmHYNqaj6RXB_8TCwCQgt-sXqSBGb9r6V8Gjb0mFWAcPvAfpMv4cglEcTfxTcRYBvBkkmz0MFXPvCffZsM3DbtFLwlnzuF_ePzA_gfDDnUHyzxZhovnuNuK9yMkWDeW-E6TzFag4npPCUSeyyTl82zZcZX2jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7d8296a4.mp4?token=DF6WVEF6FRInAx2hwykP4jRujBHn9dnY9LmmPqxzn2zzAygSiyU54VeCsR3oyq4uvFn9JzUx4UdMnfHMCAb8HoVCGC7kUSWrxKvJyI1p55IoLtbZqIwpNxYkMjEuKpBjxVzUV4_P_3xTy_ZeyStjnNFC3c6YVzqbfRdlE4V-rRYBvkIbWSvW2wWNyBmHYNqaj6RXB_8TCwCQgt-sXqSBGb9r6V8Gjb0mFWAcPvAfpMv4cglEcTfxTcRYBvBkkmz0MFXPvCffZsM3DbtFLwlnzuF_ePzA_gfDDnUHyzxZhovnuNuK9yMkWDeW-E6TzFag4npPCUSeyyTl82zZcZX2jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپ جذاب از مجاهدین یمنی و ابراز ارادت به رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/689029" target="_blank">📅 15:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689028">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy9PXT2LcYwt2yjktYtsjYo_YARHzVkBpkyYxFINM5p5vho_MZek-yWzC2w2H5XstUnKRndF5GuoiJNCmcYxDLwnQzr61GSChlvaq5lCI3o4k58o5gO_bO_qH2k1GmKx0juDBZFV9QaYFQJJQ92yKSkxlJvrk5da9ZxpIyYD3TjWQ1V60zM44GNVPfiOGLDoIyJi-_qIDSxD04jf7JtMgT9S_Er5M-GwbO7cavZnGoTo842Mmd_dvtLG-LMZTCVFfVjEkr6k3HRhXWB-x61Ft5dL4FEIgESoMtQwpDGgVfGtSjINhl0xWxZTC6AuIJ915XyOjyy6KOY-K5yjJFeyjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبح پنج‌شنبه ۱۹ شهریورماه ۱۴۰۵ محمدعلی سالاری از مدافعان امنیت کشور در جزیره بوموسی در پی حملات آمریکا به فیض شهادت نائل آمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/689028" target="_blank">📅 15:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689027">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdb8a90c6.mp4?token=HCxq-Uyz1jBEKmSCfGRH5AmzSE4gO_RIqYSJ7tiLnWDS7hsalyAnQh2Ghca9zenGR6WwL_f6oKxKFm1A_tLgo1uXthuOtGWVxmutmUuZzv6jBffnMKtCvBi_Pp4Wd9qViCBGM_tL9YR3U8sZ53brOzRqrcR9vfHcjiOvf03OQ68Rd5jcTXCxMoRSDZmELJU9zJTCx9uEpU73J5brTbYsnz9Zv6U-LM2gJ2fsQB5jxU9oqEYqsU5-KtTn74vbymm4xVS1H-GiGKQS33NeIxx37pPX3EUZ8jnm-fpHefTWo3xwAn5jz7-d0HuCDjdYpRQWuEScxtxAyp7A94E9Xo6K8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdb8a90c6.mp4?token=HCxq-Uyz1jBEKmSCfGRH5AmzSE4gO_RIqYSJ7tiLnWDS7hsalyAnQh2Ghca9zenGR6WwL_f6oKxKFm1A_tLgo1uXthuOtGWVxmutmUuZzv6jBffnMKtCvBi_Pp4Wd9qViCBGM_tL9YR3U8sZ53brOzRqrcR9vfHcjiOvf03OQ68Rd5jcTXCxMoRSDZmELJU9zJTCx9uEpU73J5brTbYsnz9Zv6U-LM2gJ2fsQB5jxU9oqEYqsU5-KtTn74vbymm4xVS1H-GiGKQS33NeIxx37pPX3EUZ8jnm-fpHefTWo3xwAn5jz7-d0HuCDjdYpRQWuEScxtxAyp7A94E9Xo6K8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرفوری / تنگه باب المندب به تسخیر رزمندگان یمن درآمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/689027" target="_blank">📅 15:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689026">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
با تایید رسمی نیروهای تحت حمایت ائتلاف عربی، ایستگاه دریافت هزینه عوارضی انصارالله در بندر مراد و جزیره پریم (میون) دایر شده و زین پس عبور و مرور کشتی های خارجی ملزم به دریافت مجوز از انصارالله خواهد بود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/689026" target="_blank">📅 15:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689025">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad652c96e6.mp4?token=OnOpI7hxGJCQo-yUlS0dBvEYATKFJOjlwyV2Vo5h9BMMSiPAnyohQxgObl1kkjulGLbRVZjXdgGppSy_1eLCaD5ZZF-o1_mJzsCOVfp3pcQitgcZQvKe9Tz_DIKYmnGkZb_1YCQTOqNpCLx4h0Bz-r9NAaUJJaGaeiJQCCFmlCxWNzPBQvV71UBJDR6EkWoJ4kQlDMI8EzDhPnYqYg64WOvfG_YgL05gMGfmgam_B95VZL1_Lm7d2JDO--MQ6GrVuNb6uCKF4qJmrgTmKDlHumhMNjVxG2bqZtL9Y53CZ8wayl7xSYJmR0Tz2poarpObX7DVP1arvoRG1u3WYMo_mKkHoOdiHVciQkwq-P9ThTmG7Ok0rAPe7MoyLALFKWmxiJWMv8t-pkMFYnLf0dESGgJ13QbBO6GPg2ydPxj3d4qq_vUjm1Ij_SrZNo80FmKkRVXSkSzLkeNTVpFMMmgpTqh4UWAX2DKGDwTf-bIulTCqMJ95bzql97Xj9h5lNkxp1vXEuyrclV2Tzke6yR0TQDICtHEbLNTGBPZHx9ZbFyx8EuygSu8JfMH2nRu_qjaY6j-wKsOYcK_xe3rVsPCXcxuhmrFGd9lhZth4ptZus-6O2N6iPKaNNYMohgFNdXs9iUZ8kVu2aXpRV3A2HFnxBb4V20ouGCc_OuCSlhtUTq0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad652c96e6.mp4?token=OnOpI7hxGJCQo-yUlS0dBvEYATKFJOjlwyV2Vo5h9BMMSiPAnyohQxgObl1kkjulGLbRVZjXdgGppSy_1eLCaD5ZZF-o1_mJzsCOVfp3pcQitgcZQvKe9Tz_DIKYmnGkZb_1YCQTOqNpCLx4h0Bz-r9NAaUJJaGaeiJQCCFmlCxWNzPBQvV71UBJDR6EkWoJ4kQlDMI8EzDhPnYqYg64WOvfG_YgL05gMGfmgam_B95VZL1_Lm7d2JDO--MQ6GrVuNb6uCKF4qJmrgTmKDlHumhMNjVxG2bqZtL9Y53CZ8wayl7xSYJmR0Tz2poarpObX7DVP1arvoRG1u3WYMo_mKkHoOdiHVciQkwq-P9ThTmG7Ok0rAPe7MoyLALFKWmxiJWMv8t-pkMFYnLf0dESGgJ13QbBO6GPg2ydPxj3d4qq_vUjm1Ij_SrZNo80FmKkRVXSkSzLkeNTVpFMMmgpTqh4UWAX2DKGDwTf-bIulTCqMJ95bzql97Xj9h5lNkxp1vXEuyrclV2Tzke6yR0TQDICtHEbLNTGBPZHx9ZbFyx8EuygSu8JfMH2nRu_qjaY6j-wKsOYcK_xe3rVsPCXcxuhmrFGd9lhZth4ptZus-6O2N6iPKaNNYMohgFNdXs9iUZ8kVu2aXpRV3A2HFnxBb4V20ouGCc_OuCSlhtUTq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه CNN با مهندس هوش‌مصنوعی شرکت آنتروپیک که روز گذشته از سمت خود استعفا داده و هشدار داده است که هوش‌مصنوعی ممکن است در آینده‌ای نزدیک بشریت را نابود کند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/689025" target="_blank">📅 15:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689024">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
از حفظ خدمات در روزهای جنگ تا بازسازی خانه‌های آسیب‌دیده؛ روایت همراهی اسنپ با جامعه
شرق نوشت:
🔹
مسئولیت اجتماعی شرکت‌ها در سال‌های اخیر از کمک‌های مقطعی فراتر رفته و به بخشی از فعالیت آن‌ها برای حمایت از جامعه تبدیل شده است؛ اسنپ نیز با اجرای بیش از ۱۶ طرح در این حوزه، در مسیر همراهی با جامعه گام برداشته است.
🔹
در جریان جنگ ۳۹ روزه، اسنپ برای حمایت از کاربران و حفظ دسترسی به خدمات، به ۳۷ کاربر آسیب‌دیده ۳ میلیارد و ۵۱۵ میلیون تومان کمک بلاعوض پرداخت کرد و ۱٬۵۰۹ کاربر راننده از تسهیلات بدون سود بهره‌مند شدند. همچنین راهکارهایی برای مقابله با اختلال اینترنت و GPS توسعه پیدا کرد.
🔹
این همراهی پس از جنگ نیز ادامه یافت و اسنپ در تأمین و بازسازی ۲۰ خانه آسیب‌دیده برای زنان سرپرست خانوار در هرمزگان مشارکت کرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/689024" target="_blank">📅 15:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689013">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-EpyAwddiKEJW0ywcjxbk_Fmk1hcDyj-cNODsqgiUsdra5FJpekzT8ibhfTvDWgbvPjNKu3XHkr9_g_ccke4mIrUlIMEcECAe8fdQtXqrLg2mmXhMxjwbM3rroqoboVLq7qOy6ZgJrtAArZkEo68tf0oWHhCWp6vIKlpC4uG2PN8yYDEn18Dk9kNlf9sGfNYrIHJVUhNrBzwNWQlyroYOzZEe3ZFsrdX9oEgGlR5Z8ZvcrEqdqtZr4MQXxrJUnWp12HrjbAI8WYITzwG6raM-3DG7JFCHtseWMSB3rmsKp3zB0PK1hgt0n9YYbqcSBP123MmsRwgWhHma3UThYrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGnERH8A1vXINKY5hlP4xp3pSKtiXwS_W2fJ0lG3zyOoStMiDsaJN2OOSh59I0GYz8LR0Juj5FaahCuJY4cYo9shE3pVh_V8vBIpZGpv9KxmachGhN-yga4T-m2n-vEOkPMx7LpkeA5xbhrzKLS_No-DKX6oe9nVlsIDmVuOWW2j6cdqwu4XbJEidllrzebFbA3AIe9iVQ_iaNTU-wSVHqgtWDL-9xkYelVIDlj1oQg-XwoRIiV58b8tTyD2KR8zI-5PeEoTn2aCojdhZ_gd7S13y13mzAccwmCZJ_MGav0DgqS8SIvu66JbdcsWh8tuoijfPX-lu2KN2wapqYKJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oknFwXbTsZhRdy353AKGxLFWmMXdEnr5M7vG_jg4TEKpi8cwPZEn7afck0tdFdEXTK1-wPgJ-2XHOo_hbTgBJFa2iRs0wBeQmLa-kYZ15qwWyshYPwXrA7BfAqHUxxgmZifRImJpShx_ThUPU_p02Rhhv8LF5K9hqTolext2BBBRF1qO4DpXtkX_bI1O90P9oVTcaCPzOzadjhmRIcLFLraCXgcg5BjFautUQPZG1GVMm3qrB_MpVRurlqZYPMHbdiK-sQEDt5IgOaC-1uYQEnFQ6iu4Rg_Yf5lyT7LRdgOOk17yJ1Z0qMB_TONqDzCSvQWpmkTWStgHzia0dky3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Knm92FLT9-DCk6CT7B2qP4sMhJjESlXzX3_BodiV0B6Vyxb_ZrX2IgEGHRgAHEizvAd6_MTeuWpWt8-ZJaohwyHau2RqRohZ_TbxmCSTKeoce-q7XUSt0oTyF-zspzA4s-GfrHy3Ri6Zih847JSSL0UBPTYgTu9iO2KG2KgvyYGOsQTjQAQrL6uW99wrq-lWd_RpyMel409QyaeRvmXuf0iGL16N4_YHfKrdPzzikirG-bt25Cs08BfaKknM6S_VUJGWIhUvmMgvIWNA32lS13F7mWfucmL9AopyZmgMT8aKz3aiKpnSvseTGwqfTBD-n7f0Wal4Wb0jEyWUfFbujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7r2hdMAA5U0X493e5uDSAd2uZWYClEPq2jDEz_z4-ciLk5UwknsRJB-H9JJ4vrpZcVMwCnM2YMSX9Ww-xSA-51jcaOGlMqy92EmYRyPMy1Hkq6pwFGuhDZ_i_eTJht1zPfBPinULqt8bK0vlwlExfUSWFwcJ4yMO2xUu_H9GuY_iXz2wiozfPLtu5zxWl0fiRnWXipF-TNSEO5vc_ZE7IVQVOq_Q88JYHn5ltKn4kBKHSbbdR4hwm_PBfGlhE6bTbBOwMdTlE-yd_E2ti5GnYMUs3o17TVesPAmD5DR1tFj9p_PDamuf_gbSYmT_MtB8EUV9Fll1j6dWoPRkgoEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qciD9i4ZNCGqVAAqJa7EH2PdZbeHhVniHjV8aARBa9AIvYgj5o1M1JC5WhR50aT_JuHrmM88X-pUiDw7y2kwdtCN_i5qQ7Dq3qoAYajiT7YcY3cUltNHUY7kh2McMyzUqHhJr68VEnVGmRVSCzjtBiZDjKcoan7bfTLiW013d6oCFly1-JQ1rO67kRwahIG0ny533Apbu6Z4EPFo0tPEqXlz1htUT8bQY-x-G7TR1tnk6AX-d0NB4lgaSZAj9xCXaNkvmoFRm3TbAcvq_EfMxhY0w64-fLgPIoEOlRxS48BfIIk-nQBre4Y_TNYf9GOwOd7L0MW76SNrVgJRjnKYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0hUf5BJewZHGVu96QHohzLJTRIbVq1HmpMoLZFfV3LXhWRPkkv0iYHEt9b9Pr7HUl9Y-HDY7-CCeQ6zMKayBwUwnNWgapP3F39WIev29AF9Nh7Z938ehNU0554Fcby6zTF26MfDAxJhB0OuR2Ez3dl0SAu_ekCiRSzFyR642YW8shvxzAyJIemburtou3XyKl4s8jsB5FCiqW2l1f7fBhF_BBRW2m3LZvAZQ6EeywGuSJs3KG-h6P0yyn4GbYPx4VLK8Yf1pjkLViGw9nh9BhjfZZ717xgg3DnmJeEsYUPgwzEWQG81IG2yWeVjSb9TVvBx_ZF3AxK3O_JiaoHS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viR8cqUEBUVxLhF_yDa8d-ggFo6Tzicn5BmeMKfhY8viXi-ios3dlQzuZ1TGlGR01hGJk-9C7LhXE25iNVcB0OP3Oet-Tk18PDYlS1gWn98yowayBAR_e4thFsu3oRlETGTNHa9s2WVMNur8oiLjqUktD86pz3HuZbFidQ5OtnCfJvff-SF8RkZz_HK8kJS3LnFENxFcSLEUGntL7eo2FAGjl5pV3W3AgnrzjL4WSqbhSFjfr31VCy1bEbyCHhSDieKCwxxFa_XAxszE2yNm0G6nRqyoeiFtZXcc947n8l1r5sOnQPfMIzEtHAyf5OrYtMM4Udt8SAwyR-9HDX9dBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPISHbvLsoRRpDJXoGcsYE3H6eA-NB2c3Xj9uWAXKFmxCUM0980YY70HmuhKsG3BSifXnSyGZGnO6mulHu7xFUqp4yB76U4aPnMadvHqpQxJ9APoht8jmK3Cpw3dOHAdS7YVxiF1njEzFCZUdTo5nwvZOR-wj_SvRISJEs27M9hA3basEld8izphBpKQjkeYg5A0bRajGRA0Pm1WtI5VHWQZP45n_vquoZ3jM4N67D1l61z3Aj4Oxu7d3UIFxEbyuoaflAkl5iuVCLhircdOJZ9-BHjXE5UE2nDKjfAVdJzuF1JBeyblcrjymcKyc72L1sI61FOMU15tiHvlPxi_pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
بازتاب دغدغه‌ها و مشکلات شما مخاطبین عزیز برای شروع سال تحصیلی جدید
🔸
روایت خود را در قالب  متن کوتاه  ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/689013" target="_blank">📅 14:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689012">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrLu2zs8VpY83Alf1dIYghISgzBgAwzHFaJXivf0sIvOp66h0z17ZEDxK-SCZFlt5tnkoEYnQZA8l36HKjjKJq6yqFxkaYQHdtcsbNlSKLeZZfhRVyKWwbNZJmuCILlDxjfDWoZ6fv0fUVYGVIA13dhA03Td4sCnBbxTBvhRf9VOfBcVz0YyayzPl2MVk7QYpBDoysTAyrMhuYXcF6n6U2zuvZ7U5wmrkj_PoGeTYvojyxl-sQsn0ZhQWcnSD96lUQ2-n0XWg8MSa5eXnNCDIitTM8MTkCSw9rm5oOHI-XbwGvRaQfzANW7gx4_NFKjd0kNGnIxClh-bxKcwI3HDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: فتح‌مبین انصارالله ثابت کرد امنیت خریدنی نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/689012" target="_blank">📅 14:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689011">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5aee1199.mp4?token=gyysFzaAD3D3qVg2vc31-h7N_LdW60LzFGYLb-OOXGmsHbJ7BRCNx1t5Y-mzG7e95kpePNUJAe_bEM_PWedz1rpgZjxuqgR2bBIv1y0l8c_0if5cH_gqZ6XaTxjr1d3DTYsbWNVBBGn5zF3ubrr_gKRgYbMWwDXeC4ARS1xzhKKs7YCH4teHW6_d3slrzmQzWMaz7lUICAjK86tRDaxZMVboKVzBrGRCJkSq3cbr4tGxMKQFuyLqXf6kJgJinovbG1UrML8gJYOPR5N45-jZX2abnS06Y3YgB4ssz1aVBLkcr-SCVp3GKAYBW44P2Hs18XF-sD6mGRH7er1SQyJH5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5aee1199.mp4?token=gyysFzaAD3D3qVg2vc31-h7N_LdW60LzFGYLb-OOXGmsHbJ7BRCNx1t5Y-mzG7e95kpePNUJAe_bEM_PWedz1rpgZjxuqgR2bBIv1y0l8c_0if5cH_gqZ6XaTxjr1d3DTYsbWNVBBGn5zF3ubrr_gKRgYbMWwDXeC4ARS1xzhKKs7YCH4teHW6_d3slrzmQzWMaz7lUICAjK86tRDaxZMVboKVzBrGRCJkSq3cbr4tGxMKQFuyLqXf6kJgJinovbG1UrML8gJYOPR5N45-jZX2abnS06Y3YgB4ssz1aVBLkcr-SCVp3GKAYBW44P2Hs18XF-sD6mGRH7er1SQyJH5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/689011" target="_blank">📅 14:46 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
