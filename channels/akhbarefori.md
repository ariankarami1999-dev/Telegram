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
<img src="https://cdn4.telesco.pe/file/QVXn3d0oSKEdI4e-U-s8biouUjj9p-uqeX4bnbJeDT3t_d-sOkfNgihB2j2qSg6cTe0z7jnqlHGvtB1u1lW2wKJrJxPRplcHoxTVMIjypRJG062sOsFHKOTk4S-nwHMJ9yv22l4anleSmjKf0rg5UwUu_0G8fAtmWyzn533B6kLukAyEENSdx7UAZrdLO4fREmCvPB8AHGk2JXDxEhpzWlINwTiWGyiPsAAczVxupWCBgltZAVUEjeSPrjG3P4JBkJURzOBIA1KvAwb6YqD7A7qCipizHf1Ozg5VFOLBqJlYkSr2amwqijFnrMAZsUayqCLjifnJg4Z1H6a-5CwupQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 10:56:22</div>
<hr>

<div class="tg-post" id="msg-691110">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/471e910179.mp4?token=oPAiiB8TmY7cezzzutqUAdCIllo_rXUfjpOspx3uiVJ8b8CpQgSzS5FqYiSLUMAW5FEFns73gcbQYhPghpX-9fjEBexAG0-aFbMKod-mXkuzNpdZjtD99UXyOvgFsy5eRYYwpsZ7YQjeGG4B9BbsmLZ6LUcQEcFNseiZUJJOJRaY26HlhKJWbN3GMzUXKmq7RnZnXVyhO9WvEzt2kquTTjAs4l4MidVNX8K9hg0oMgbJ9xKr4fE797jd0ceG4K_mrV5UTI0eYz3fo4YTAbNsWRgHc73-8Qy-467mFYs8BicWiRocmSD36Sne5AAue7dWfIloD9KvDV1ptrxFhLgunw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/471e910179.mp4?token=oPAiiB8TmY7cezzzutqUAdCIllo_rXUfjpOspx3uiVJ8b8CpQgSzS5FqYiSLUMAW5FEFns73gcbQYhPghpX-9fjEBexAG0-aFbMKod-mXkuzNpdZjtD99UXyOvgFsy5eRYYwpsZ7YQjeGG4B9BbsmLZ6LUcQEcFNseiZUJJOJRaY26HlhKJWbN3GMzUXKmq7RnZnXVyhO9WvEzt2kquTTjAs4l4MidVNX8K9hg0oMgbJ9xKr4fE797jd0ceG4K_mrV5UTI0eYz3fo4YTAbNsWRgHc73-8Qy-467mFYs8BicWiRocmSD36Sne5AAue7dWfIloD9KvDV1ptrxFhLgunw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لوکاشنکو، رئیس‌جمهور بلاروس: هدف واقعی آمریکا، ثروت‌ ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/691110" target="_blank">📅 10:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691107">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ویدیو کالبدشکافی و تست مقاومت آیفون ۱۸ پرو منتشر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/691107" target="_blank">📅 10:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691106">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
اتحادیه سراسری مرغداران گوشتی کشور: کف قیمت مرغ زنده ۲۰۰ هزار تومان تعیین شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/691106" target="_blank">📅 10:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691105">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvgMG_-u22zzENDVgRTbNCTXQNAqiiyKqwzt4O-yfoupem7tOlGnogwSRUwSOg5Rzdnk9zCS5-kO5vSL1waAZKwcL03KmOLWRm3FaXns25Kn7WHpjQt88HF-EqlAlEtupbHvdwDcPO1Q5dtHLjKi1-772lA1adXddqEWRDb1kl1753INd6QDXMCU4q4eOPKpyIcEVZkLMaRbTVdgQ2wUBabpu8cG2QPM8iS98VpwaX7i6FbuwOYktB1OqIjZ4uacyvhbGyjf8v5DbBxCCFdmWAusAmhH8JMpbzsFUH0e_yY7_Oz_MO8_xgEVm8S490UsaYRII75ejZ1DWBLBJYYrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕰
ساعت نگارگری پنج تن
ترکیبی از هنر ایرانی، هویت مذهبی و یک دکور متفاوت برای خانه یا محل کار.
✨
مشخصات:
▫️
قطر: ۳۶ سانتی‌متر
▫️
جنس: پلی‌وود
▫️
طراحی: نگارگری با مضمون پنج تن
💰
قیمت اصلی: ۲٬۱۹۸٬۰۰۰ تومان
🔥
قیمت ویژه: ۱٬۹۴۴٬۰۰۰ تومان
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/691105" target="_blank">📅 10:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691104">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c218a009ee.mp4?token=gkNt-hdR-K4vDeYzjPHGaqQaJseRFnyyJ7Qq6NQgcGxZx3I0U1TLynPHfyuxMxrpLNDVscHqc9y_Oz-OB3xzZZtmFFvzDnql5hh2qnedyMFdC4G0OzzfrSpkv4EQEu8pk5NZb5eClKi_BK3YOf3LVgnEHPmWshVRTUlMY5BVN_HDTSzG0b3YU8O46kEIOrYuade15ikEdUDSkNo4WcLHjYcdvqxI3r7BS3FFDzZ3DaQiO5-b1199LOx5EeFwU5JqwHQKB9QR1NWlkTLsgcneFDWbFXJHCPLdW9IxCyuvcUlljm22X8pGt5_CGTF_9dyX1qrAWdJbkSv2omt1NTfSPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c218a009ee.mp4?token=gkNt-hdR-K4vDeYzjPHGaqQaJseRFnyyJ7Qq6NQgcGxZx3I0U1TLynPHfyuxMxrpLNDVscHqc9y_Oz-OB3xzZZtmFFvzDnql5hh2qnedyMFdC4G0OzzfrSpkv4EQEu8pk5NZb5eClKi_BK3YOf3LVgnEHPmWshVRTUlMY5BVN_HDTSzG0b3YU8O46kEIOrYuade15ikEdUDSkNo4WcLHjYcdvqxI3r7BS3FFDzZ3DaQiO5-b1199LOx5EeFwU5JqwHQKB9QR1NWlkTLsgcneFDWbFXJHCPLdW9IxCyuvcUlljm22X8pGt5_CGTF_9dyX1qrAWdJbkSv2omt1NTfSPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیاین با این سمبوسه اصل بریم به شب‌های آبادان
😍
😋
مواد لازم:
🔹
نمک ۲ قاشق چای‌خوری
🔹
جعفری ۱ پیمانه
🔹
فلفل کناری ۸ - ۴ عدد
🔹
پیاز متوسط نگینی ۲ عدد
🔹
سیب‌زمینی آبپز ۴ عدد
🔹
فلفل سیاه ۱ چای‌خوری
🔹
نان لواش ۵ عدد
🔹
زردچوبه ۱ چای‌خوری #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/691104" target="_blank">📅 10:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691103">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJACUtjsqXLyrRyw4dX2SvHrY1577XrKe5OCyGFmiTyOcSWBW_PeRwct7VcPxWcBXC8MNCs2Rk8UdaTOjFH20qiUZP6XWcMmXWG79_k96luWGKwzs2nX1PuoucjRxEXs5LHPNeCTjgkjJNkHy4Q4QWV8cy9KaiqefWlnMHoR0f0q29MYVyj6iSbrh6g-YDeF5f2VonK74qwCkfHqg6mshyyB3b_lWkYVAm-D5-JkzCA4mzBm8PKJutAOnveRLaPTQs1lPPrvWcaYQnk00yEx003qQhEFefjZNfMnBZM3vIDHV0cUsOe98zyRuoRgzVlkYELwxCdhsJn3tLaZ-8Ka-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت ۴۰۰ مگاوات ظرفیت برق فجر انرژی خلیج فارس
🔹
فجر انرژی که با حمایت شرکت صنایع پتروشیمی خلیج فارس، بازسازی تأسیسات تولید برق و بخار خود را به‌صورت هم‌زمان در فجر ۱ و ۲ دنبال می‌کند؛ تا پایان سال حدود ۴۰۰ مگاوات از ظرفیت تولید برق را به مدار باز می‌گرداند و با اضافه شدن ۳۶۰ تن ظرفیت جدید تولید بخار، زیرساخت انرژی منطقه پتروشیمی را برای استمرار تولید شرکت‌ها تقویت خواهد کرد.
عبدالله علی‌پناه بهنمیری، مدیر پروژه‌های بازسازی و نوسازی نیروگاه‌های فجرانرژی خلیج فارس:
🔹
احیای واحدهای توربین گازی، بویلرهای بازیاب حرارت و تجهیزات جانبی و مشترک نیروگاه آغاز شده است.
🔹
در فجر ۲ نیز احیای چهار توربین گازی و دو بویلر بازیاب حرارت در حال اجراست.
🔹
نخستین واحدهای احیاشده با ظرفیت تقریبی ۴۰۰ مگاوات، پیش از پایان سال ۱۴۰۵ سنکرون و وارد مدار می شود.
🔹
برای تقویت شبکه بخار، اتصال مسیرهای دریافت بخار از مجتمع‌های منطقه در دستور کار قرار گرفته و با خرید  دو دستگاه بویلر جدید، تا پیش از پایان سال ۳۶۰ تن بخار دیگر به ظرفیت فعلی اضافه می‌شوند.</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/691103" target="_blank">📅 10:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691102">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
افزایش کرونا و آنفلوآنزا در سه هفته اخیر/ موارد بیشتر خفیف است  رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت:
🔹
بیشتر موارد خفیف است و با استراحت و مراقبت بهبود می‌یابد، مصرف خودسرانه آنتی‌بیوتیک برای بیماری‌های ویروسی توصیه نمی‌شود.
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/691102" target="_blank">📅 10:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691101">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5a05b9e8.mp4?token=VWtjtpRvLqO0ttKS42yzn1UY9OSQw47lwMHgiPZVGP0BKaR-350v6sZ-NhhFR67prYglEs7sNIqZOhGlmxCrjr_HdL9KYkbf-oc6fClM8BEsIYn6XHDJLkPmRjabIhqk9tn4zGNCfECFonXtxQhF2RCcRGkRQQRad43eoAqZZ1P1So6vwyMICCEV4ODeb1SRO6vD3M8CbJBvvpAv3HPZ2H-rzrmEF3TJhyVj3nEedlyLTHYMDDRpGiGfy2YBuwiP2rwIaXOmHnJD2WxhtWYu7coZm60EGfQzm2Gdv7ewAsiSWmXVTERnGqS8BGX2JZxew56HgJRn2QV5rkgHAXE2dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5a05b9e8.mp4?token=VWtjtpRvLqO0ttKS42yzn1UY9OSQw47lwMHgiPZVGP0BKaR-350v6sZ-NhhFR67prYglEs7sNIqZOhGlmxCrjr_HdL9KYkbf-oc6fClM8BEsIYn6XHDJLkPmRjabIhqk9tn4zGNCfECFonXtxQhF2RCcRGkRQQRad43eoAqZZ1P1So6vwyMICCEV4ODeb1SRO6vD3M8CbJBvvpAv3HPZ2H-rzrmEF3TJhyVj3nEedlyLTHYMDDRpGiGfy2YBuwiP2rwIaXOmHnJD2WxhtWYu7coZm60EGfQzm2Gdv7ewAsiSWmXVTERnGqS8BGX2JZxew56HgJRn2QV5rkgHAXE2dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطوری ژورنال نویسی کنیم؟ راهنمای کامل ژورنال‌نویسی برای مبتدی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/691101" target="_blank">📅 10:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691100">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvJKYmi2DR1CYf3K1r_2acOEKLsgnGJQbDYnUnitmkar3GrCNRPGhFcOSpCFqmE-z6n6t2zIVc5LXvtp9JtJs9qm1zrReBp0FLHhGQu5eBBCWq-ZDESuCRxTYjlXuJReGBPqTo6OmmR7ILXNTEOf3zQXqGOl6qs29Ogrio5LEfuzwtqjgLRdZenJddVwbMA7pcxUB5i2ahMXZWFswLCaYPsL2QPDm4qlOArWwd6IrniFmaprz4KnFk3Qs-cHFRzig-L12sdIrmY_6efqbRvWzadSHLlwWTQmZV4czpP6fy0tJ4WImv5Obr_u2C5e4Z2F7yHhL31KxcSGVkh1XSngWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت «تلما» و دو توله‌اش به "توران"
مدیرکل حفاظت محیط زیست استان سمنان:
🔹
محیط‌بانان تلاشگر مجموعه حفاظتی توران موفق شدند «تلما»، یوزپلنگ آسیایی ماده، را به همراه دو توله امسالی مشاهده و تصاویر این خانواده یوز را روز جمعه ۲۷ شهریورماه ثبت کنند.
#اخبار_سمنان
در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/691100" target="_blank">📅 10:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691099">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
فاز دوم فشار اقتصادی آمریکا علیه ایران؛ آیا مرزهای زمینی می‌توانند جایگزین مرزهای دریایی شوند؟
🔹
آمریکا در فاز دوم فشار اقتصادی، فشارها را از نفت و کشتیرانی به بانکداری، هوانوردی و رمزارزها گسترش داده و دسترسی به بنادر را محدود کرده است؛ در نتیجه استفاده از مرزهای زمینی آغاز شده، اما حمل زمینی گران‌تر و کندتر است و در کوتاه‌مدت جایگزین کامل مسیرهای دریایی نمی‌شود./ دنیای اقتصاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/691099" target="_blank">📅 10:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691098">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
تعویض لاستیک خودرو چقدر هزینه دارد؟
🔹
بررسی قیمت‌ها نشان می‌دهد که شش سایز مختلف از لاستیک‌های ایرانی پرمصرف، حالا بین ۴.۵ میلیون تا ۸ میلیون و ۷۵۰هزار تومان قیمت دارند.
🔹
خرید یک دست لاستیک برای بسیاری از خودروهای داخلی، هزینه‌ای بین ۱۸ تا بیش از ۳۵ میلیون تومان دارد؛ رقمی که برای بخش بزرگی از راننده‌ها از یک هزینه معمولی فراتر رفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/691098" target="_blank">📅 10:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691097">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3342a42d47.mp4?token=VxRoGhOX6C_WTFbyNkbUJb03VoRaKklllv2FA-dhu7ReDELIduxBZYodR7Xd_2c3LEDphFK2ryCpXnjlxOL14-blHrJSMEYikjKHVHPmHJDsJG5PR38uuQ__2OLez69pH7uGxxyOpo268bn5m6vUt8rKU3yNdwMprO4YWEXLXQgWXWGeoajdYKrc3hkfvOuFaL5bSSK6MGPUBN6BFFShZU9SsRMaODH5ERm_DGbA2VDFrfbexv_8J1EFM5ZqUSL0k0fBG81sBMNFooD0TRRY0QBUenaHhlrR-adT7aNhHyhpN-38gjqWLPiRvYexeXoEVFmc9ORo3Xx_12JFNkSQ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3342a42d47.mp4?token=VxRoGhOX6C_WTFbyNkbUJb03VoRaKklllv2FA-dhu7ReDELIduxBZYodR7Xd_2c3LEDphFK2ryCpXnjlxOL14-blHrJSMEYikjKHVHPmHJDsJG5PR38uuQ__2OLez69pH7uGxxyOpo268bn5m6vUt8rKU3yNdwMprO4YWEXLXQgWXWGeoajdYKrc3hkfvOuFaL5bSSK6MGPUBN6BFFShZU9SsRMaODH5ERm_DGbA2VDFrfbexv_8J1EFM5ZqUSL0k0fBG81sBMNFooD0TRRY0QBUenaHhlrR-adT7aNhHyhpN-38gjqWLPiRvYexeXoEVFmc9ORo3Xx_12JFNkSQ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امام جمعه دزفول: دختری که تا پاسی از شب در کافه‌ها وقت می‌گذراند نه می‌تواند مادر خوبی باشد و نه همسر خوبی باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/691097" target="_blank">📅 10:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691096">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnYhl5JxkwCmHp8OOyVlhw9PbPuDVS7_swEdrY6nPLSA9fSIW-4CwYDmqJS1IcaueNAbUuLlBpa_dnxpxx5kWZaB0NuNcVMtf3yrEDE7nYWpPjgIFWUQfKqUj7sjBE2xiJ_QT5wf42PgqJsFeEa8UHcpNeEdlf4SSf_oM9H7Ssk_rivQ_Hsky_V3FZd3gz1R-6Ep4n4pGo12QItR7vNmVOxdPgcsEHU2SmY-OJmd5nNii_J-AExhFgb4nqE2H0vlR9sMQR8dGxIZeLd_iIz0F8-KZ5wthAkSQCyX16U5obwXU-wiUE5_XRWn8AtrW29AcMsTm-Q2JpdK1eqafDN7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ر
ئیس جمهور چین به واشنگتن می‌رود؛ جنگ ایران روی میز مذاکره با ترامپ
به گزارش آسوشیتدپرس؛
🔹
شی جین‌پینگ، رئیس‌جمهور چین، هفته آینده برای یک سفر رسمی به واشنگتن می‌رود و روز ۲۴ سپتامبر با دونالد ترامپ در کاخ سفید دیدار خواهد کرد؛ دیداری که جنگ ایران نیز یکی از محورهای مورد انتظار آن خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/691096" target="_blank">📅 10:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691095">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEkizfgiuKAhxcfmnGVHEZEQrPwPBEhcd9oZP6VHOYanKZXlDrIOOCT5z7zpPl_O2WHnX254sdxwxisSEW0ebdqg-zmGJJCSvvcjWk9ocQhP90-xgr2h8frgnLFvHaYT_A2F4tM9K_brHmG5yRUFGWTjhqaQCbMlQKl-nG8aDCTkdiqboDS5h191gDe1jS4FCf_GKqJfcCA2pxnxvb30gAfep8DkwkvCc-3gt5jQIgAD0ZNi5fTEw3frcaMOrkqmlLYd1D7GD9lyvOCak-gaSQXkqWCDcGDvQ6YOfMn90pBeoBT4txuXKvBUMCoiD5iAFIOHh4HW164ZS0-tRSH_xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/691095" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691094">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e03437a32.mp4?token=Nf2XCaOS3AZU44IPOoOUnd6gd5wK-pGb2kQ7JEB2IhFbOOmeviLKpVleSpTX1oYBSIkuJ59SM_3Gr3CrZOlWsqbKwuNpSP3VlK09C1rP5B6k9moPidryVKkExNLmeUUeDKFIkhAKmHvcfhjWl-IhVZpTftHM1qwYxyL0AyacbPOCjjfJ_ov5Bk_KDxAUSNEpT4ItQDA5r7ZRjIgTcMZCGo9Dw-f35mDC8O6ZQ5vRI-9RhWvcgHlqpIxykn1yg53kAYbQJ7cshyubL04oTe38ShM6Wx2WXHYCzByMCYWpM-YxkihkBRJgvu_3neGKSjCEeMxPbFIUFKbkmCKZy02A7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e03437a32.mp4?token=Nf2XCaOS3AZU44IPOoOUnd6gd5wK-pGb2kQ7JEB2IhFbOOmeviLKpVleSpTX1oYBSIkuJ59SM_3Gr3CrZOlWsqbKwuNpSP3VlK09C1rP5B6k9moPidryVKkExNLmeUUeDKFIkhAKmHvcfhjWl-IhVZpTftHM1qwYxyL0AyacbPOCjjfJ_ov5Bk_KDxAUSNEpT4ItQDA5r7ZRjIgTcMZCGo9Dw-f35mDC8O6ZQ5vRI-9RhWvcgHlqpIxykn1yg53kAYbQJ7cshyubL04oTe38ShM6Wx2WXHYCzByMCYWpM-YxkihkBRJgvu_3neGKSjCEeMxPbFIUFKbkmCKZy02A7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهکار مهندسی چین؛ آسانسور کشتی سد سه‌دره، شناورهای چند هزار تنی را در کمتر از یک ساعت ۱۱۳ متر جابه‌جا می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/691094" target="_blank">📅 09:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691093">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHL1ZuWFLhkA8bRN192Z9WZzAiMLEwh4nl_09uUbHeVkBnDzEm6Ctl5t1CScj2rk-Os480jmBs3Ee0Kgu0uLH-jCeV1oa-b57SQk0uCwzC9h3LDc3yrQLNviBU-YaFgnw-3PP4zYtJz472TWCsTaH0p7djkAX5XlvoOfMNPELAGeS1su0_xmZsRojjSY8mpoccLJSFVz6CA4eBIFZH_Mn21sDE_hgpSA8KlK_HqYWKOXqCUmw7r2NcgY9KJhRnucPBbEKAONnZjWTDthuwI23Gah3Yn_aOaeIHZ9ehwkEepgmJHhOsjS0QchC5KfJITAuFUDc3mkOrDMR3cNM5vZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ صدای شهر
🔹
اگر در محیط زندگی و محله خود با معضلات محیطی، کاستی‌های خدمات عمومی و نقص در زیرساخت‌های شهری مواجه هستید، مشاهدات و مطالبات خود را با ما در میان بگذارید.
🔸
گزارش خود را در قالب عکس یا ویدئو و متن توضیحات ، همراه با نام و نام شهر به آیدی زیر ارسال کنید
👇
#صدای_شهر
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/691093" target="_blank">📅 09:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691092">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74dcd9335.mp4?token=OH3b2I7cw9am5ZroMr_05K5x7Da0rIDhZ5HdgbEXk1RI0abUOJ_KBEp-XtDrHOy0RcufTC3NI-1wtWzDEhOOvpFwteyrmCkSPxJOMC6AGwTKaGULmzDdXQUfiLhMK3RHC7KEyfV_WX_y5w5iR7g5whRUt-iJSDC2H29TrviEf7q6qD2rrO3xaxLTrcJhZ-1CWzYFEx4xjsTLBB7pgUaXZSJGIlK_qJXY8CyqFxI1aRBnGTNA2vizijZK_3RBPDgLP6Vqi2be5ae17jUsLRPHVFcVpSdCfo0Wbj5gjqzUtkOo4DHWHRzUgWmJuppI6JnpT3haQpDsNLjj_7Ij9U_Wdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74dcd9335.mp4?token=OH3b2I7cw9am5ZroMr_05K5x7Da0rIDhZ5HdgbEXk1RI0abUOJ_KBEp-XtDrHOy0RcufTC3NI-1wtWzDEhOOvpFwteyrmCkSPxJOMC6AGwTKaGULmzDdXQUfiLhMK3RHC7KEyfV_WX_y5w5iR7g5whRUt-iJSDC2H29TrviEf7q6qD2rrO3xaxLTrcJhZ-1CWzYFEx4xjsTLBB7pgUaXZSJGIlK_qJXY8CyqFxI1aRBnGTNA2vizijZK_3RBPDgLP6Vqi2be5ae17jUsLRPHVFcVpSdCfo0Wbj5gjqzUtkOo4DHWHRzUgWmJuppI6JnpT3haQpDsNLjj_7Ij9U_Wdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفتگو با دکتر "غلامرضا نوری قزلجه " وزیر جهاد کشاورزی دولت چهاردهم به زودی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/691092" target="_blank">📅 09:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691091">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac3403a0e.mp4?token=ANoepvfiPEvR3cKzDXV9r05_p5p7Jy9t50tUIFKeHSeIDs3Bn1whibyawMMJb3dV1dsaNs-Zu440hsci-yojjD6ZYxdFiRVGGmNUKe04_q3rbw7X9CvxWR3uyIHdj2yjSdn129ninlzvxdAhuw8nOPbD6LgAFUKGTL29HtwFV_a8ynqa47MvwrWuYvQhESHV9s-l2BCZS4B7HA6MOj5gA8eYefTZsnsO4QFrP63-V_pLaUpy0w_vSlUFRkE_O6A2n0uFOz1SJMq5WRmq6uM4Rxdix5WgO9S-AkjvvqDYAVLJOg0rowWFlH6UU6A64vyEX2FItDHbG6sgqtsqiTei0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac3403a0e.mp4?token=ANoepvfiPEvR3cKzDXV9r05_p5p7Jy9t50tUIFKeHSeIDs3Bn1whibyawMMJb3dV1dsaNs-Zu440hsci-yojjD6ZYxdFiRVGGmNUKe04_q3rbw7X9CvxWR3uyIHdj2yjSdn129ninlzvxdAhuw8nOPbD6LgAFUKGTL29HtwFV_a8ynqa47MvwrWuYvQhESHV9s-l2BCZS4B7HA6MOj5gA8eYefTZsnsO4QFrP63-V_pLaUpy0w_vSlUFRkE_O6A2n0uFOz1SJMq5WRmq6uM4Rxdix5WgO9S-AkjvvqDYAVLJOg0rowWFlH6UU6A64vyEX2FItDHbG6sgqtsqiTei0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده مرال و شوکا در جنگل‌های لنگرود
🔹
مرال و شوکا از گونه‌های ارزشمند حیات‌وحش جنگل‌های گیلان به شمار می‌روند.
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/691091" target="_blank">📅 09:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691090">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2c6047ab.mp4?token=TaRdh5Z5VXkrTz1jvMVfy81mxI4wxaY7kCuOJsVDYeAFQ9wryEyu2YHcqF0vGooRaV3UiZCHZKjdCjj1RJpLHPLV99LaO1lXZZUcyryatoggi1iQodW8I6oGsv48o4nzLlTOTJbeBGIHQrcI0yOXCXK8PIdYpY2UB9j80XcU7DxA1m5rL_ed1P1pYCi5rFpFVlH4CZC4_7Xh2ft5Ww8UhAzSbKfkOisQ1miSSrGOzpNiABMPi6NDhUPkyqzURlz2WxEpJibv_LSzOJUmRz3XBrl2p7MIp8tU0ZunhnknLnTe_I42t8z8IEaOuLJECGKlJCF3YJuYj-pN2CHW8WbhPTAYz4e76FEl6yCpv1NJVv1bRf5U1FWi-SWwVH_AmrSqIeml1mCfh_n8jBZiNXVUK4QTU3uf9xqYPu9fK5idzlhaMn3zEyKZ5SB_RfmU9mjszqPFmd1iXMxovT4gS2BEWcQrymVK7ZywqiN7lIha2qBApcf2SpO3DZpUS5fe3YXKr-EOG7PZztM5oPNP-Gnn3dmRu__CJzpf9ZtZttiKkthhvqvJh6k0RYa9mqnkhW7yN53Rb7LANDLvEFAjTdel7sKpDVGaTl3_C_sBcrcU5U5pmDp0Izw1WXsSMgKQ4cZ_OC4BWDQyNKneAzeiWgy8k7ZqA7rEKRFaFCfwP9-tN0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2c6047ab.mp4?token=TaRdh5Z5VXkrTz1jvMVfy81mxI4wxaY7kCuOJsVDYeAFQ9wryEyu2YHcqF0vGooRaV3UiZCHZKjdCjj1RJpLHPLV99LaO1lXZZUcyryatoggi1iQodW8I6oGsv48o4nzLlTOTJbeBGIHQrcI0yOXCXK8PIdYpY2UB9j80XcU7DxA1m5rL_ed1P1pYCi5rFpFVlH4CZC4_7Xh2ft5Ww8UhAzSbKfkOisQ1miSSrGOzpNiABMPi6NDhUPkyqzURlz2WxEpJibv_LSzOJUmRz3XBrl2p7MIp8tU0ZunhnknLnTe_I42t8z8IEaOuLJECGKlJCF3YJuYj-pN2CHW8WbhPTAYz4e76FEl6yCpv1NJVv1bRf5U1FWi-SWwVH_AmrSqIeml1mCfh_n8jBZiNXVUK4QTU3uf9xqYPu9fK5idzlhaMn3zEyKZ5SB_RfmU9mjszqPFmd1iXMxovT4gS2BEWcQrymVK7ZywqiN7lIha2qBApcf2SpO3DZpUS5fe3YXKr-EOG7PZztM5oPNP-Gnn3dmRu__CJzpf9ZtZttiKkthhvqvJh6k0RYa9mqnkhW7yN53Rb7LANDLvEFAjTdel7sKpDVGaTl3_C_sBcrcU5U5pmDp0Izw1WXsSMgKQ4cZ_OC4BWDQyNKneAzeiWgy8k7ZqA7rEKRFaFCfwP9-tN0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی عجیب تکنو با بدنه ۴.۹ میلی‌متری؛ باتری و دوربین را با آهنربا به بدنه بچسبان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/691090" target="_blank">📅 09:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691089">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2Pd73xNJ6VPOvA_tkvx6Ms0RNDK3q1dkgr5TiCpvROhGg95ekpnS_P_ZjzU7ZyD8ZWY7PvCWYi4x8lY2xM3ocQoqqrgE9FzdkYMP5UU7zvJSyAtFTkqKvRavgC22TY6k-vxrmXvn3y2ZjeHPPgbJ52SwvCmZdhi16aewiE1-b_h0ArEV_syeISqAM0pR0Byb-LShm1AuyvQIAKDdU6UFdgvHqc0oSXbpoIdL1IUSlx1Smf7svYP6sIGUPqgv8ssFkWmreXxzUtfX_IQ2vX1euEIW4zJQWv48jO_tP1Kpc29Mnt7SA43d6i4AZe-zuUBqYbnmb3oTkbhHLEn_Vug8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ عراقچی به وزیر خارجه فرانسه؛ اشک تمساح بس است آقای بارو!!
وزیر خارجه:
🔹
یک و نیم میلیون الجزایری توسط فرانسه قتل‌عام شدند، اما پاریس همچنان از عذرخواهی بابت جنایت‌های استعماری خود سر باز می‌زند. سکوت شما در برابر قتل‌عام کودکان دانش‌آموز ما توسط آمریکا، گویای همه چیز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/691089" target="_blank">📅 09:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691088">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
اسامی ضدآفتاب‌های غیرمجاز اعلام شد
اسامی این محصولات به شرح زیر است:
🔹
ضدآفتاب BIODERMA، ضدآفتاب NEW WELL، اسپری ضدآفتاب SADOER، اسپری ضدآفتاب FRUIT OF THE WOKALI، ضدآفتاب ESTELIN، اسکراب سفیدکننده صورت و بدن SADOER – WHITENING SCRUB FOR BODY & FACE.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/691088" target="_blank">📅 09:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691087">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pws4xN9CQsxwCB7jk6-ca7WlCMKHBqIzxnM19b_3A6aQoVrbk7vkh2w44upY5t4CADCReNy5_v-cLCLVipJ3hwfpPv4EqV7LNfNOIKySvENn-KoHNeVisxcena2DQPF8OzkMCUzk70DSl0JEr61RliXHkHGg5peAHMwsk6SDAPAJwQe1VwmLyRaNE3hj4Y9u1jTUvqtK-YAoHIUst0EbUmZirYXc6Qb1g1r87BgDAJLGOp4fO9wy9YZU4VJWlnPtmaSr0Ud8t0DnObuXy2W-gMy0xDmaX7_lfM0xNU5_VWmR9lLlSw3fkwxmIHdGyhBVHwQNzx4Jdb_0t7u6thU93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حکم اعدام خائن به کشور(حسین پدران) که اطلاعات سایت‌های موشکی اصفهان را در اختیار موساد قرار داده بود، اجرا شد
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/691087" target="_blank">📅 09:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691086">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
فقط ۵ دقیقه بوی قهوه کافی است تا خستگی، تنش و اضطراب کمتر شود
🔹
۵ دقیقه قرار گرفتن در معرض عطر قهوه تازه‌دم، احساسات منفی را کاهش داد و فعالیت مغزی را تغییر داد. پژوهشگران این اثر را به ارتباط نزدیک حس بویایی با احساسات و خاطرات در مغز نسبت می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/691086" target="_blank">📅 09:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691085">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a276f0b2b.mp4?token=iKdj59Nhrz6tSzjbiXJn2mfzZXZuUOh0e9lYbGo9OPbdq_MU1_heVjt1iig2PsYn3EMjK3ppdQaqNXWpjs87Q7x_8p3dB_s4yZkMoSXnJnxnO3yUSPIIgRw9vVDdM6TadonmghXsO5_b7T6hUYESwV-G7QDEehfWm08wfZn48Xz8LRPLh32yxFVtv99JslArHCtR5WT4E3baKX6Bv7nMxeV9zB-_Izs7OUX9PgCx1Qv0OJjXcMXlbK5TdfYnCfSUH7GR_8sI6Bjyjr5m4yRWWzfP8gcfsDiZj_Bf8PO2aG-VyjywRSJSQ5riz3fEIC16WboxFMtwZ8vdcLTvWvVYfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a276f0b2b.mp4?token=iKdj59Nhrz6tSzjbiXJn2mfzZXZuUOh0e9lYbGo9OPbdq_MU1_heVjt1iig2PsYn3EMjK3ppdQaqNXWpjs87Q7x_8p3dB_s4yZkMoSXnJnxnO3yUSPIIgRw9vVDdM6TadonmghXsO5_b7T6hUYESwV-G7QDEehfWm08wfZn48Xz8LRPLh32yxFVtv99JslArHCtR5WT4E3baKX6Bv7nMxeV9zB-_Izs7OUX9PgCx1Qv0OJjXcMXlbK5TdfYnCfSUH7GR_8sI6Bjyjr5m4yRWWzfP8gcfsDiZj_Bf8PO2aG-VyjywRSJSQ5riz3fEIC16WboxFMtwZ8vdcLTvWvVYfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد انجام این روتین صبحگاهی بدنتون از شما تشکر میکنه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/691085" target="_blank">📅 09:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691084">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
افزایش کرونا و آنفلوآنزا در سه هفته اخیر/ موارد بیشتر خفیف است
رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت:
🔹
بیشتر موارد خفیف است و با استراحت و مراقبت بهبود می‌یابد، مصرف خودسرانه آنتی‌بیوتیک برای بیماری‌های ویروسی توصیه نمی‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/691084" target="_blank">📅 08:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691083">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96bc38c38.mp4?token=ghr74B3Ueh9KLQx5_QyJJnOwBWzra4F_v5x-96ElmGTMHghVngBLoRrejVtNlJELCY3x2igdyRfMTJ6LKwRrUXyloQkg5MgbOlsCuihXxXm9YQ3scw5meC8mAGmx-Imv6mkuwhXbOQ6ViSwYAm09SPQUoKzh6o7HJ0EqLbeTmkYr7Yu0n7s8qbs98cVjxrGB0YwUtKRJyr0at5fLSHR_PNUTiNIosLRiLO4-w5NGESe3rsWi19jP-VKA9YzdlBqyjtqvfhm7_AeG1TIoXFu75kAzPWhAb_jNfbkJf-HR-rslmAT7dTsgocFT4set47kN6O9FEog2ERiPOz17I1BgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96bc38c38.mp4?token=ghr74B3Ueh9KLQx5_QyJJnOwBWzra4F_v5x-96ElmGTMHghVngBLoRrejVtNlJELCY3x2igdyRfMTJ6LKwRrUXyloQkg5MgbOlsCuihXxXm9YQ3scw5meC8mAGmx-Imv6mkuwhXbOQ6ViSwYAm09SPQUoKzh6o7HJ0EqLbeTmkYr7Yu0n7s8qbs98cVjxrGB0YwUtKRJyr0at5fLSHR_PNUTiNIosLRiLO4-w5NGESe3rsWi19jP-VKA9YzdlBqyjtqvfhm7_AeG1TIoXFu75kAzPWhAb_jNfbkJf-HR-rslmAT7dTsgocFT4set47kN6O9FEog2ERiPOz17I1BgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهداد اقبالی میلیاردر ایرانی، باشگاه ورزشی چلسی را خریداری کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/691083" target="_blank">📅 08:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691082">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2344800b2.mp4?token=tHZQo89hr9sLC3PvoSjqjLqB3aepj-xejuZ4_ISJJV9CjB9vOhGNtY_Y6bHPUH6PxX0d3CbLsbNqPu2X5BooONESVyFIKAxHAio3aKgQRtZtrNz8xn_2cNnF0zSPjGvSqznCT3AMEMRVOw7vnWu1Nl2s2KyuBUZ0n1wYc0OTFcg3zGpKM6pbDYQhD2Q10KcHjG6s0tVPxvYU-_9mZ739kPvJadWtERdNxPbZBPm4JtFBbyPwru8tQDsSyAgBeKX7PXxTEDy8-w8GPu7gE7zG_BILpCQooa0vNee2ZAtETvv1w1bxhMxaa9qpu2GDxbFFwj_fgA7-UAnKz4A4ibdIJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2344800b2.mp4?token=tHZQo89hr9sLC3PvoSjqjLqB3aepj-xejuZ4_ISJJV9CjB9vOhGNtY_Y6bHPUH6PxX0d3CbLsbNqPu2X5BooONESVyFIKAxHAio3aKgQRtZtrNz8xn_2cNnF0zSPjGvSqznCT3AMEMRVOw7vnWu1Nl2s2KyuBUZ0n1wYc0OTFcg3zGpKM6pbDYQhD2Q10KcHjG6s0tVPxvYU-_9mZ739kPvJadWtERdNxPbZBPm4JtFBbyPwru8tQDsSyAgBeKX7PXxTEDy8-w8GPu7gE7zG_BILpCQooa0vNee2ZAtETvv1w1bxhMxaa9qpu2GDxbFFwj_fgA7-UAnKz4A4ibdIJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا ستاره دریاییِ باردار دیده بودید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/691082" target="_blank">📅 08:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691081">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f6d0aef8.mp4?token=r5O0K0zPRyMVxWnEHkQLzjxSL92G9A1GqYoBkH1FCMs_5GXrD3vTrCwUQTnVjo2yLTVodSXEaWmF9xybwef0o3pP80ZhiYCWJfMkHjSQLmisAbFMySYdTcm9d0eJVGa69-A6PMOjx91vRYt_K2bZnVYP-7mL03sitYvJlLAHgj3D3JsJzitxa4ifG4kmKLjwgOskJldTXsout1Ayjl-FA8i_vVM_IvHSHVCdRTgnUp7SglvoSOdOvjQBtlodKglB6B8mH1_scHgeqAcH_vOkIVc2Ri5niiu_k8_Vvu2NzuVEf0WSrqD_y5rF2fmqc4eA5iUkODZR6nUw9CIqmUf2QjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f6d0aef8.mp4?token=r5O0K0zPRyMVxWnEHkQLzjxSL92G9A1GqYoBkH1FCMs_5GXrD3vTrCwUQTnVjo2yLTVodSXEaWmF9xybwef0o3pP80ZhiYCWJfMkHjSQLmisAbFMySYdTcm9d0eJVGa69-A6PMOjx91vRYt_K2bZnVYP-7mL03sitYvJlLAHgj3D3JsJzitxa4ifG4kmKLjwgOskJldTXsout1Ayjl-FA8i_vVM_IvHSHVCdRTgnUp7SglvoSOdOvjQBtlodKglB6B8mH1_scHgeqAcH_vOkIVc2Ri5niiu_k8_Vvu2NzuVEf0WSrqD_y5rF2fmqc4eA5iUkODZR6nUw9CIqmUf2QjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهمن عظیم در قفقاز روسیه ۱۷ کوهنورد را به کام مرگ کشاند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/691081" target="_blank">📅 08:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691080">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgYq1XDBxoiKxwfXNjAvGVLWDqZYvZl3ZBlcDWEKReE2q5xAM06ktiHxc64O3M-YLzbXNFB2Xur32Q1Yy4sIgaMuo8CLn10F0DlBUsNHpK4DIc4szp2bjMA6V2lR-UEuWHlEUL4C7TStKTihlzCHho4yXx0cz3BcAvCq4Ovg6IcOEkdwTPhzU9TG_RCgW5Ydqj_FHCnfzJFvPZykUL_6TX_2RkM5kaSiyj7lnk0lDnZTtglwzUaJKvuEYnMykLt3cP4i89RYFeLN22YyPm3KtOj9S8sEi9061LU4vWO4w_SCsxvdnTgexDI2pCu2UEMSPBBwh7eFa2RllKR-uTxorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شارژ حساب ایران در آسیا با برد استقلال
🔹
برد استقلال مقابل السد در لیگ نخبگان آسیا باعث شد ایران جایگاه پنجم آسیا و سهمیه ۳ تیم مستقیم به لیگ نخبگان را حفظ کند. حالا نتایج استقلال و تراکتور مقابل تیم‌های قطری (به‌ویژه الغرافه و الشمال) برای حفظ این برتری و سهمیه‌های آینده ایران حیاتی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/691080" target="_blank">📅 08:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691079">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNv1dReyjgdXtvxNtCqEFCDfhA1tSQfwMUDn8KgI83hPaBZiwp3KgTqubvCsxtI-5wtGU1YEHkHhV2HpkIRHTJmjaLZbrdrd79J-x3YDQkQOH0FsmUgbDjQmHmFnHiMKLvYDpnT7Npi71myk1rEco02GjT8grDvV_bTDwPjpDZEK2DliF-Wqs2-e6A1Qe3Qqfoa7O11q1iiT229vEXkLw9hcrsue9fSh1n40RU5ww18Nhv0wQ-TirPNwUHoV4n16gAEq70jFZR-LVSN3bYG4fn-sypti0GRULBHZmeZTlyp-6-nyS7DkIWai5vwDyVSdS3C_ULlPxPsXsyfOR8HWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری تماشایی از دریاچه قله سبلان که در پی سرمای زودرس، کاملاً یخ زده است
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/691079" target="_blank">📅 08:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691078">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0928532f0c.mp4?token=B2JztS4Bcz_y59S6UMg4Xj9MNnK2OlFyQdcTGhCjMpiekGSy8cRwy_x2XG5lSmAGZIYE2AWhXPFq1odrA3_tvJIQQtlZ5oQiBHZKutDjIHNcy6DC0Tp_Div__yfxmfOl4JtQ15WQb-o9cgkh5rjRaSISGNcyCx6-IE-fB_2BNdlJK-PG0kiEDEQv2h3CLOI-hV16i6qu8rO8N6rVRpoE_dT9zCxq7uH14aac9q2CaCv2QCWTPniUBbF1bI_rq5kM6ZXYXA0AWBcL-j4F2KZSNc1YlY0u0z5tbg-MfsuWC8XXCfhxPsHZxz_684xLdbIZjsGMiZoL3VDyiGT5qqaOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0928532f0c.mp4?token=B2JztS4Bcz_y59S6UMg4Xj9MNnK2OlFyQdcTGhCjMpiekGSy8cRwy_x2XG5lSmAGZIYE2AWhXPFq1odrA3_tvJIQQtlZ5oQiBHZKutDjIHNcy6DC0Tp_Div__yfxmfOl4JtQ15WQb-o9cgkh5rjRaSISGNcyCx6-IE-fB_2BNdlJK-PG0kiEDEQv2h3CLOI-hV16i6qu8rO8N6rVRpoE_dT9zCxq7uH14aac9q2CaCv2QCWTPniUBbF1bI_rq5kM6ZXYXA0AWBcL-j4F2KZSNc1YlY0u0z5tbg-MfsuWC8XXCfhxPsHZxz_684xLdbIZjsGMiZoL3VDyiGT5qqaOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک وزیر جنگ آمریکا: ویرانی وارد شده از طرف ما به ایران تاریخی بوده است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/691078" target="_blank">📅 08:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691077">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
الجزیره: ترکیه مجوز فعالیت بانک ملت ایران را لغو کرد
🔹
نهاد تنظیم‌گر بانک‌های ترکیه اعلام کرد این تصمیم بر اساس قانون بانکداری این کشور و به دلیل احتمال خطر برای سپرده‌گذاران یا ثبات نظام مالی گرفته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/691077" target="_blank">📅 08:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691076">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران: ما در جنگ با ایران به‌ طور قابل‌توجهی پیروز هستیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/691076" target="_blank">📅 08:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691075">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-C-mGbj9Yv3qCWyr5r6zBM9XiHrucLNDyn6ABzbFS4RMqTAk3aw5__Tbey4AQ25DZ3lqsk-Ld8Uir_QUaF4Jcaqh6_HesuYf1TvUVvGDGW8hOF9DwVDy9RO7HcGx163mK8fpYdGUbNaSi4mQjtKEU1rD8mgEgXI1JbLJgoBWNkgHHvIyLGUvXwhYNRrfHQ7L-6fSqKRdpQCQqhcNdiysEDVgSB8_kXmQ7kDPB4wBMJhQL0jlLvl1_3Jc19PUIzvJNTP45yIvI-Y4HQNJJ1Dl2st2sM88Ygdr_Dgm49yXKDu1Cgpvcc6nszxLTP1SjZNJXRU-2hRGv9-ZP-QNmOhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری منتسب به موشک یمن در آسمان شهر ریاض
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/691075" target="_blank">📅 08:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691074">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
اعتراف پنتاگون: جنگ با ایران تاکنون ۴۳.۶ میلیارد دلار برای آمریکا هزینه داشته که ۳۲.۴ میلیارد دلار آن مربوط به جایگزینی مهمات، هواپیماهای آسیب‌دیده و تجهیزات نظامی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/691074" target="_blank">📅 08:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691072">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6435dce4c6.mp4?token=L4wV9kfqle3rMB8vLM56BC3-TJcJa7OJjrMtYUwTuZXSaufAs-joHFayGl2rZHt-OcH_lGZU4W4_M-WwQLY_2YlFQ8vSvcARWe729QfhwUP2AOWXaM5ez5pjs5BmfpPijm0hHhtwAw67AtxXXt5RyarFpB2B21Elhi71kdYvA9ugyh6yaMD4giiLO_KchyZhEBehUZHEL-ygUyMfN5MvOO-Uhj8sPdI3isBhPJeTau6BspC6pFw1G1EXPH4wGX8MhrstZjH8petgyrkxhZ8OF13eqDVX7TVi6daUKTLQzK6neqJf6X1Orr1AeYIREcnKTzu8UkfRHkQ3LjNwATFnlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6435dce4c6.mp4?token=L4wV9kfqle3rMB8vLM56BC3-TJcJa7OJjrMtYUwTuZXSaufAs-joHFayGl2rZHt-OcH_lGZU4W4_M-WwQLY_2YlFQ8vSvcARWe729QfhwUP2AOWXaM5ez5pjs5BmfpPijm0hHhtwAw67AtxXXt5RyarFpB2B21Elhi71kdYvA9ugyh6yaMD4giiLO_KchyZhEBehUZHEL-ygUyMfN5MvOO-Uhj8sPdI3isBhPJeTau6BspC6pFw1G1EXPH4wGX8MhrstZjH8petgyrkxhZ8OF13eqDVX7TVi6daUKTLQzK6neqJf6X1Orr1AeYIREcnKTzu8UkfRHkQ3LjNwATFnlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شب ناآرام سعودی‌ها، سیستم هشدار قطع نمی‌شود
🔹
منابع عربی از حملات موشکی و پهپادی یمن به پایگاه هوایی ملک خالد خبر دادند. همزمان چندین انفجار شدید، شهر جیزان در جنوب عربستان را لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/691072" target="_blank">📅 08:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
دونالد ترامپ قانون تحریم‌های روسیه و ایران را امضا کرد
🔹
ترامپ قانون تحریم‌های روسیه و ایران ۲۰۲۶ (طرح لیندسی گراهام) را پس از تصویب در کنگره امضا و نهایی کرد. بخش مهم این قانون، تحریم‌های ثانویه علیه کشورهایی است که با روسیه مبادلات تجاری دارند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/691071" target="_blank">📅 08:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe2c81d8d.mp4?token=sQZxTcWr3h1JYYRbdDv2im-1pI-AJfw9_9r_XVQkTKoSyfA8-sM3Q0Uv9GDVu9j8n0uo4fa81zTKRSLaurAS0xQZ-xWbIt4jpfEeV37YhLSSpu8xdWooSnpdnIn0hr51xZ0f0R-SyFdvGSFZjiNQsnGN7I1xnXPnB6fmcqIrYceEI0pZXOcLxtNFrWGwivxrjEOi-JUpcVNSZaZrTBsUcU48UWPAFWNcc0dEsgK_ttp3MQ_D4eNNFW1xvRMrFmAZoxLOJ2vBarw5PnlIoR_4UE_RCGSXEnEZpQSJZb0_GILixUExBlS38er8Ywpv5rmnfzaoddu3HpAGPjFHEx24Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe2c81d8d.mp4?token=sQZxTcWr3h1JYYRbdDv2im-1pI-AJfw9_9r_XVQkTKoSyfA8-sM3Q0Uv9GDVu9j8n0uo4fa81zTKRSLaurAS0xQZ-xWbIt4jpfEeV37YhLSSpu8xdWooSnpdnIn0hr51xZ0f0R-SyFdvGSFZjiNQsnGN7I1xnXPnB6fmcqIrYceEI0pZXOcLxtNFrWGwivxrjEOi-JUpcVNSZaZrTBsUcU48UWPAFWNcc0dEsgK_ttp3MQ_D4eNNFW1xvRMrFmAZoxLOJ2vBarw5PnlIoR_4UE_RCGSXEnEZpQSJZb0_GILixUExBlS38er8Ywpv5rmnfzaoddu3HpAGPjFHEx24Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمیشنی از جلسهٔ شورای امنیت سازمان ملل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/691070" target="_blank">📅 08:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691066">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOGFfhPjA1Pdq1ASkU403N25UnchppCtey1_G-I1lz7ekTcYpHIM1ip6z3h6rW5ylhd3pxn1X5qQ_TqgQ8if2CK0h2libOoE5QMUcUwj04a6yZGVDPOp0u0xOAH4sXNQeEB01jUWctVd8-9-tCWWEmgAWDo27B3kdkjKY5qBkuSlx5JCgUe6msZRoYvZuf1KQlxlLrXuNXGQ-Rt72sXFDVgfQkhkA0o3I0KZeq_lz3tufSMcim1rqz_bMeTOplH-LKgCMJnH19zaZ3n7-8MNyaX7CsAF26Oe0zRN-l_6EpT0nTzlDERMKzkQAbZhFxTH7HBSq_cOV7iZC9swajMtBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbQWHqTj6GiTRQ1kdpRt2lLW5dI9wnuAPcUR58IhbrKmW16b91hS6GxrJ90MNzXx8r53cBfYffe9VdtvmPYQmqaOoX9DW4vNkGZ-i7DivMc1HkjuY2ArVlSRITtGfXlZcjyMa7E5-tNCUpoI2kIHD1wu2_Gbqi7RIUJGubfqsHHKzD6m0kmcKd-bhrsWoUXERK1koKaa3N6huW9W92x6Rs1aMcNR5VU3um4Pbcfyl1GeqfHvPixD3uwzeR9N8tOMBwVNrXkMzgSFUiC4EBlwUzD9CS3athupEtjwdnaJvFvEz8noUKiHZz-4QpNWkV8d4OahzQPxEwRQxZqIkN1wNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQKSdxbJwwn5CpaWU_M8LAttlCGbu5mrr-yOHcjsfX8btMk-WUDgq6M3pOEBa8mx276OXNHhnJKSmVcgHDifAhIWrv0T6vvvrshh_owuuBZkh6wiMRgBdsbD7BVhq8KSH1g5XfYrx8-laH5sbM4BPyQHEYyUL5AOTORpdBg9VBcC07wbmglg1Vhrok5v4v_4Du2BfC1gCrKzRRg_CD4Ns8wBFaeXUbPFALMQ4E6XOLVhY7qaeudRUh2uMiUfdssF44AdAbAwDcA_osoRusNTvflTcAuN084EEm95CA4o_U9-5TR929XPnu8J50EhN3UCjoM5A5eojy4rf83Ej3GMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bepiM1s0PZz_fwLs4x4s215sk2Bjl5UE1Tn9eKC3hrFFJ24eWMFtsb1zPB5PcVWrsQEFjCI1GtJ0hoPS1fIyvPfI2OooomB2j2jvs4-vw1iaD4WeQpa002RskWrmrj0oNgeY0pPopWbvyPT5DiTqIa6X5Iz0QWflHJJlICUjq_dj1OqsSxodewEry1XFW5wtN_z9pwkGhtnmzTzv108hYjgajyl3WLQMhVDkn222mNFHC0DTTvtD1tGNbFk4QrfW8XR39CR7ghatvh5gNmYsdq_I4qC4sOACUNUeOWPVjlCBN36QLJ7U9zpH06aKQQYt0jte5PxwjqPnBWg2_ypBMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر تازه از ویرانی‌های یک پایگاه آمریکایی در کویت بر اثر حملات ایران
🔹
بر اساس گزارش میداس‌نیوز، تصاویر تازه از یک پایگاه ارتش آمریکا در کویت منتشر شده که ویرانی گسترده در پی حملات موشکی و پهپادی ایران را نشان می‌دهد. چندین ساختمان کاملاً تخریب شده و یک پناهگاه نظامیان نیز مستقیماً هدف پهپاد قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/691066" target="_blank">📅 08:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691065">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRpvajjdmub76IBIuSMk1rxKOYEkEA0i36S5j9Pioi3Zvn7JcOAQnDmzkFIxy3MZl14b1Vka4EN6K1hv88GgkYbOT-D-yQpndxe9OWlWx984QgrgE6BbjBxWeHIwKS_ZTRaqZ3lpdD9hj-wozZGre7VPfRSZw7jh3OpyMy2xUfl95zbG9NhXTV5wHvy7hbuZPVCyCI8PtKe356jqZdBpRVJafydBlqEz8uDYlBCbZhYPE-SPjcZClgXb9D42vNqLMQ-Y0SjyQLXy--E22bZMA8CkLWjlCjjLl90IR9sZSwqbG9LrT4k98JFw7b3WNrI2w3BYLEnsdezHjnByB5CYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲۸ شهریور ماه
۷ ربیع‌الثانی ‌۱۴۴۸
۱۹ سپتامبر ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/691065" target="_blank">📅 08:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691064">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2f834fa.mp4?token=HCiq8oWlBN1D5NDWepVxE8095w1bU8Uu3tFdmFxF5HNawr_r39t40MFJadfcYdCucq0V410fTwxJ5uzcEwMxCDJlbrzm383JT65yX9yLIUj5q3WCBOI4EVoj1Qnf2Z9O1RS8iq_J-HRhpgdJjwRRQv4EDZi5_BdvCVatnvQDsLzK_n-sHoSsTTAcRwWjldcQZQcLKpitbjLg3scfV4L9Kpy7-zlrl6F7Drc5U1h8upWjx9jZxmr2XffFQArDPVC-Cl01HTbyE89yp1UrZrJdM0iWICkrRttyNle7kO0nlzh559pwiePiSWiKliWshL4hNycIK6W2Hz_iP5cGuSBw9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2f834fa.mp4?token=HCiq8oWlBN1D5NDWepVxE8095w1bU8Uu3tFdmFxF5HNawr_r39t40MFJadfcYdCucq0V410fTwxJ5uzcEwMxCDJlbrzm383JT65yX9yLIUj5q3WCBOI4EVoj1Qnf2Z9O1RS8iq_J-HRhpgdJjwRRQv4EDZi5_BdvCVatnvQDsLzK_n-sHoSsTTAcRwWjldcQZQcLKpitbjLg3scfV4L9Kpy7-zlrl6F7Drc5U1h8upWjx9jZxmr2XffFQArDPVC-Cl01HTbyE89yp1UrZrJdM0iWICkrRttyNle7kO0nlzh559pwiePiSWiKliWshL4hNycIK6W2Hz_iP5cGuSBw9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فشارسنج خون درجه 1 برند Arm Style
قیمت ویژه و فوق اقتصادی
📌
استفاده راحت فقط با یک دکمه
📌
کیفیت عالی
📌
دقیق و بدون خطا
تخفیف تا 28 شهریور
🏠
پرداخت درب منزل + ضمانت بازگشت وجه
خرید سریع از اینجا :
👇
https://memarket24.ir/product/fast/37863/180124</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/691064" target="_blank">📅 00:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691063">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
المانیتور به نقل از یکی از منابع ارشد اطلاعاتی اسرائیل: نهاد‌های امنیتی اسرائیل با هرگونه حمله پیش‌دستانه علیه حوثی‌ها مخالف هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/691063" target="_blank">📅 00:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691062">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
منابع خبری گزارش دادند که ارتش عربستان مناطقی از استان صعده در شمال یمن را با توپخانه هدف قرار داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/691062" target="_blank">📅 00:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691061">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وحشت ترامپ از افشاگری رسانه‌های مستقل
🔹
ترامپ جنایتکار، در اقدامی خلاف قوانین بین‌المللی ورود خبرنگاران شبکه‌های خبری سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و وبگاه پولیتیکو به کاخ سفید را ممنوع کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/691061" target="_blank">📅 00:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691060">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌ شدن صدای انفجار در جازان، ابها، خمیس، مشیط و العلا عربستان خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/691060" target="_blank">📅 00:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691059">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dcc95981b.mp4?token=Or1DKSRi-s3_6FqE6vNNYs_pRhfsdEEZLwGW9HPmT9UlQWFcStr3pMpihyVAKD7CVnxazn4xz9x4D9tCFP1KlxjdoMhpumYNsmZgKXu10L5Lm0tH_xV2a2bAE5e7ye7HEFM4kT2uu9OqSdSV-oFyUomTI-hF9Q1WOkVPqNc_IpIHWarm1O2Je5FiQCzNtQWPLS0_Xbq-ecHK6e8myHxASWLpDCV6zVomCQU8ps_VR4yki_QfoDW5cQBcPR6DRjFOpJ9gyxClm3WTKXnMCXe-GEMxpEmgt-FaW_XNKGh88X6_cPHPoRQZVAU5Yjs4RLdey8YTTQ-Viwcwk7jVo9-GRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dcc95981b.mp4?token=Or1DKSRi-s3_6FqE6vNNYs_pRhfsdEEZLwGW9HPmT9UlQWFcStr3pMpihyVAKD7CVnxazn4xz9x4D9tCFP1KlxjdoMhpumYNsmZgKXu10L5Lm0tH_xV2a2bAE5e7ye7HEFM4kT2uu9OqSdSV-oFyUomTI-hF9Q1WOkVPqNc_IpIHWarm1O2Je5FiQCzNtQWPLS0_Xbq-ecHK6e8myHxASWLpDCV6zVomCQU8ps_VR4yki_QfoDW5cQBcPR6DRjFOpJ9gyxClm3WTKXnMCXe-GEMxpEmgt-FaW_XNKGh88X6_cPHPoRQZVAU5Yjs4RLdey8YTTQ-Viwcwk7jVo9-GRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاد استتار اقیانوس؛ ماهی مرکب صخره‌ای باله‌بلند که در کسری از ثانیه تغییر رنگ می‌دهد!
🐠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/691059" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691058">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4921ce8ad.mp4?token=C6l8RWpuout59tsxiFwuQWTgYkRHaDTEo_qaHy7IravfHibJ5xwlTxXMCOeHGoBVraeiNuxdrg-FYrPcogDCM_oAUKGFQ5R9XwZ-2ewmw3a-WctWHdES17SOPO8wsCuKltSUmCGsKeLSpXkNab0RN5lJmZzY1RkShdMWFrXRVv5NOyrcploAbpe5u6jKRnmwHuP7OkO6Bg4-i50lfChLDlXCOeeSlWyOmgzbVEvo9CMCzEeHcHmBBoUEJY_N3gND3iupLeveDITwDDLHt2Oc5jFfJoFZWZHCt9JjdLzGeZZSutPcyk9yLyo0u85Fkpe9-dVYjNTl1hX28c3hl9Wf3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4921ce8ad.mp4?token=C6l8RWpuout59tsxiFwuQWTgYkRHaDTEo_qaHy7IravfHibJ5xwlTxXMCOeHGoBVraeiNuxdrg-FYrPcogDCM_oAUKGFQ5R9XwZ-2ewmw3a-WctWHdES17SOPO8wsCuKltSUmCGsKeLSpXkNab0RN5lJmZzY1RkShdMWFrXRVv5NOyrcploAbpe5u6jKRnmwHuP7OkO6Bg4-i50lfChLDlXCOeeSlWyOmgzbVEvo9CMCzEeHcHmBBoUEJY_N3gND3iupLeveDITwDDLHt2Oc5jFfJoFZWZHCt9JjdLzGeZZSutPcyk9yLyo0u85Fkpe9-dVYjNTl1hX28c3hl9Wf3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔧
دیگه برای هر کار کوچیکی دنبال تعمیرکار نگرد!
دریل و پیچ‌گوشتی شارژی ۴۷ تکه
؛ همه ابزارهای ضروری رو یکجا داشته باش!
💪
✅
موتور قدرتمند و شارژی/ مناسب باز و بسته کردن انواع پیچ
✅
ایده‌آل برای سوراخ‌کاری چوب، پلاستیک و فلزات سبک
✅
همراه با
۴۷ قطعه کاربردی
✅
سبک، خوش‌دست و قابل حمل
🔥
قیمت قبل:
۲,۲۹۸,۰۰۰ تومان
💥
قیمت ویژه: ۱,۸۹۸,۰۰۰ تومان
💳
پرداخت درب منزل
👇
برای سفارش و مشاهده جزئیات، روی لینک زیر کلیک کنید.
https://memarket24.ir/product/brief/35160/180124/</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/691058" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
به‌ صدا درآمدن آژیرهای خطر در عربستان
🔹
سازمان دفاع مدنی عربستان سعودی از فعال‌سازی سامانه هشدار زودهنگام در برخی مناطق این کشور خبر داد. این هشدارها در استان‌های جده و طائف فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/691057" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691056">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFqV2z63DmMCj8LNgip9FEUSJ28ai-KBfBVZ9MORuNWXYYxBwNUnjTY-KL_hewdiOUCRrXflxJqHaFKVmprpLZrc51cWcFQfatE1nygG5pxc9ydciSo6gt8WgdET8WTfhi0ZpjscV7N6Ykh1A0GMF00hWJvJxptApRam_3lLmUiSKNg3lubLr0t7Td9syx_tMxO2bb9MkXUgSXdMzFlMD1jP0Q86W0JrpzH-vxcDIh5oozuM3Q3b57DrU9BcXQkYVLnUZil55jEO9D-0T8wEWA0cdmBsUr5ug6w4TI1idSmsGzgPv3G14KyBnQ5sgaPOR6ZuiCW19ItFrj_YTs98OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/691056" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691055">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔹
در لابلای خبرها، پربازدیدترین‌ها را از دست ندهید
🔹
🔹
تصمیم جدید درباره بنزین
👇
khabarfoori.com/fa/tiny/news-3246091
🔹
ترامپ دوباره ایران را تهدبد به نابودی کرد | نظر شما چیست؟
👇
khabarfoori.com/fa/tiny/news-3246176
🔹
آیا شی جینگ‌پینک سکته کرد؟ | شایعه سلامتی او را در اجلاس بریکس چه کسی راه انداخت؟
👇
khabarfoori.com/fa/tiny/news-3246067
🔹
افشاگری درباره پرونده اختلاس فدراسیون فوتبال
👇
khabarfoori.com/fa/tiny/news-3245981
🔹
هدیه سنگین ترامپ به اسرائیل | آمریکا ۴۰ هزار بمب یک‌تنی به اسرائیل می‌فروشد | این ماجرا چه ارتباطی به ایران
👇
khabarfoori.com/fa/tiny/news-3246085
🔹
خبرها را هر لحظه اینجا دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/691055" target="_blank">📅 23:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
به‌ صدا درآمدن آژیرهای خطر در عربستان
🔹
سازمان دفاع مدنی عربستان سعودی از فعال‌سازی سامانه هشدار زودهنگام در برخی مناطق این کشور خبر داد. این هشدارها در استان‌های جده و طائف فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/691054" target="_blank">📅 23:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxnSMqu6TQVvCJzSDjR8qR00rwEODOKwcZR6i-uQoTKgyLPSeIKLc5xXrrbcRc2LEP8m78tnDFDheJfbjv3IlLWAsozo1WuHdwD-sen-uScBeKY6ZhTmTRYvfwAeLSkZu-1Z4KqXWfNbAsgM4bPJeO9R5MEtvAubsreJjTfkvM6-VEA_QQqmHhUH7OY4DQjjtJVryV_ZqRTC8181fQo3q0CwvzooTLmr2Dg_G3QSShr8HVrGnxgxhGkVkPS1qvkeZtVwNYjCcpEyegyHuIPylhfj37gjad6XPalN7PJ6s8ye6VDlO8g_vXD_1w4zqDs-4ObzY_jPZYUAJF_mv918tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مکرون: قیمت سوخت غیرقابل تحمل شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/691053" target="_blank">📅 23:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691052">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c21eca87a.mp4?token=M5-dt_waIbnxl3c7UtmKEUlJC6hfokW3emv_1AOjux4G6od4qFc0I4JYrA24Mt1NOKyES8UFS3GF6OWRDtEqMre3mrayjUPAMVw0k4-K1tV0JKjXXDro1Y0Q-elVembUI6AAgXs6tF_c92U_hIKDKMzX6JZgPuUe8NmkvLgq1ufyGwhe-7FBOhU8YG_EUXaKRVuvvzW73lZzeEV7M5JWWiYk8PG5EAKE-sykFNLrQA0BUMqVmoeadfWmfkDBexhmbpusXQ9esYIGbs2WqVSgqAo9u4CpUzSjllJIi-Fuv5mYZNfT8cmt_LS8rip2SDamf1M7kRKmFpWkAKJ0QIG4Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c21eca87a.mp4?token=M5-dt_waIbnxl3c7UtmKEUlJC6hfokW3emv_1AOjux4G6od4qFc0I4JYrA24Mt1NOKyES8UFS3GF6OWRDtEqMre3mrayjUPAMVw0k4-K1tV0JKjXXDro1Y0Q-elVembUI6AAgXs6tF_c92U_hIKDKMzX6JZgPuUe8NmkvLgq1ufyGwhe-7FBOhU8YG_EUXaKRVuvvzW73lZzeEV7M5JWWiYk8PG5EAKE-sykFNLrQA0BUMqVmoeadfWmfkDBexhmbpusXQ9esYIGbs2WqVSgqAo9u4CpUzSjllJIi-Fuv5mYZNfT8cmt_LS8rip2SDamf1M7kRKmFpWkAKJ0QIG4Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ایران سلاح هسته‌ای نخواهد داشت؛ البته برای تحقق این امر، مردم باید هزینه بیشتری برای بنزین بپردازند
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/691052" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908b5c30e6.mp4?token=oxz_4SyFWs98aPcVzWyMJ_Dj66gq1jqY4USckI46nt79FXgTN30uBFJpSGjvQDtlMj6g9uImGAVkDIAXoOK42XSGU7uwf5NOowUoEFAYz0VSsnNcQYQXhWWWqHhCRxt6GDxfrRtX14jyle9jMcwB9GbeCdRvzfzC6hLj5iIgeydfdgs7z8PcBqxhzFU3-FIoCwpR3e__Bf06QJrUsvDE_SN-5GsD1Ap54CzpnJrUu3PFRwELm0LXz08JK7mN0GBJsYe5JY3rfRrWBRl4Vu01Qjax0Dgr6Xt7jR7fQoG3KpMrXCy_2dzrFsUpkRvHSHOvCknRcIgKEGhYIOKxH1UGyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908b5c30e6.mp4?token=oxz_4SyFWs98aPcVzWyMJ_Dj66gq1jqY4USckI46nt79FXgTN30uBFJpSGjvQDtlMj6g9uImGAVkDIAXoOK42XSGU7uwf5NOowUoEFAYz0VSsnNcQYQXhWWWqHhCRxt6GDxfrRtX14jyle9jMcwB9GbeCdRvzfzC6hLj5iIgeydfdgs7z8PcBqxhzFU3-FIoCwpR3e__Bf06QJrUsvDE_SN-5GsD1Ap54CzpnJrUu3PFRwELm0LXz08JK7mN0GBJsYe5JY3rfRrWBRl4Vu01Qjax0Dgr6Xt7jR7fQoG3KpMrXCy_2dzrFsUpkRvHSHOvCknRcIgKEGhYIOKxH1UGyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران: ما در جنگ با ایران به‌ طور قابل‌توجهی پیروز هستیم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/691051" target="_blank">📅 23:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691050">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6ab4aabd.mp4?token=lYB-GYT32I7W4aGJY3w5AT6bC-gdTKHKjy_YP0a7FKLk90z-xizV_ihua39U3-hOn3xB6qteWg9EkQyom9km8rbu8v6pYrND6kCGjtobJmUEGhogbwc5JDcAQ2nXLBJ_G9R7Q7J_3DtYeP7u_DRmABzoUUvMW3t0IBa-4tg-Tnix23NXm_rU6E14_Net0TDOosmDCFWVkL-ZjLzcx8ciZlB2YnDG8xAFyjF0gNlbBdhW9j8FPCVGFkwDxXbJqTHcy8jD3sLpk1MMlePBbOohTi8UvyforHUMKOXgIxcc1NNs8vTTdCB6XaLaaUOicm1TAUH5EA9zoFhx9I56LML6uSBDsTDbybsZPZV2_yBQQFHmG48tGdH57WhQIhbeKlSMVuLvXq6w5TO3QxQ0RnYDgawWd0Xzj4YKxYAzlwHCa_iooOTEsqVlSphrtVmuPZHNtafRHBe7EPM6rGEzi6JtTfnAsSfGYf7UPhZmM9MmVI71nJyk22q37WeqYRect3etE50Pr0RKib6APNnUqHybutUfX2QGpeVh8J901KzjvFks356dAVaoPMxg1b1qOA9R2KDcrb1IIbSSZmD9veiSJY29cEHKdhSMAdDEuCydaAlaEKQMJXvbcL-YqkKzo0AX8PbdMzUSNtkrIZjguHEkxyJbLNHhSjv9Ls62K07SoCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6ab4aabd.mp4?token=lYB-GYT32I7W4aGJY3w5AT6bC-gdTKHKjy_YP0a7FKLk90z-xizV_ihua39U3-hOn3xB6qteWg9EkQyom9km8rbu8v6pYrND6kCGjtobJmUEGhogbwc5JDcAQ2nXLBJ_G9R7Q7J_3DtYeP7u_DRmABzoUUvMW3t0IBa-4tg-Tnix23NXm_rU6E14_Net0TDOosmDCFWVkL-ZjLzcx8ciZlB2YnDG8xAFyjF0gNlbBdhW9j8FPCVGFkwDxXbJqTHcy8jD3sLpk1MMlePBbOohTi8UvyforHUMKOXgIxcc1NNs8vTTdCB6XaLaaUOicm1TAUH5EA9zoFhx9I56LML6uSBDsTDbybsZPZV2_yBQQFHmG48tGdH57WhQIhbeKlSMVuLvXq6w5TO3QxQ0RnYDgawWd0Xzj4YKxYAzlwHCa_iooOTEsqVlSphrtVmuPZHNtafRHBe7EPM6rGEzi6JtTfnAsSfGYf7UPhZmM9MmVI71nJyk22q37WeqYRect3etE50Pr0RKib6APNnUqHybutUfX2QGpeVh8J901KzjvFks356dAVaoPMxg1b1qOA9R2KDcrb1IIbSSZmD9veiSJY29cEHKdhSMAdDEuCydaAlaEKQMJXvbcL-YqkKzo0AX8PbdMzUSNtkrIZjguHEkxyJbLNHhSjv9Ls62K07SoCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات دردناک از پیدا شدن پیکر مادر مفقود شده تهرانی از میان آوار منزل مسکونی در نزدیکی اتوبان شهید باقری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/691050" target="_blank">📅 23:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691049">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSejnC_DP1JZh5HsNFnEWOv3eNrdZ0daOJlTsU9Mf2QMPdT6swrQwVjUccyQzVkFtEC5Hwn8BW9slPWe6OfgrbY3yfSYU02m7ItHCEXkiDecWrn3QMGWODIiOUBsKvh1_IpGIV0-eOX10BKAFIvMOecaKijS7Wip-KB0H9fi06LXfongPQ5Ez2G_DjeYX0IHdCCkfAf8T3mj32KNOuxf01U8959BytO3JIxCKw-DUh6t_jNQbrgMpzL5HC57l1eqdbv0LOSzklLLRbzMxBhq8TJVEgP3ipMRrc8vpWebRk0GJUdJnKfHxvoRQmw1JxrMf09gukThwmixQhKHKnF0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه بلومبرگ: هشدار پنتاگون به متحدان: کمبود موشک رهگیر تا ۵ سال ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/691049" target="_blank">📅 23:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691041">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
اولین و آخرین آثار هنرمندان مشهو
🎨
🔹
دالی: از منظره‌های آرام کودکی تا «دم پرستو» (۱۹۸۳)
🔹
ون گوگ: از «طبیعت بی‌جان با کلم» (۱۸۸۱) تا «ریشه‌های درخت» (۱۸۹۰)، احتمالاً آخرین اثرش، نه گندمزار با کلاغ‌ها!
🔹
کاندینسکی: از بندر مه‌گرفته اودسا تا «شور معتدل» (۱۹۴۴)
🔹
پیکاسو: «پیکادور» را در ۸ سالگی کشید، و در ۱۹۷۲ خودنگاره‌ای کشید که مستقیم به مرگ خیره شده است
🔹
موندریان: منظره‌ای از جنگل لاهه در ۱۵ سالگی، تا «پیروزی بوگی ووگی» که ناتمام ماند
🔹
ماتیس: اولین تابلویش یک طبیعت بی‌جان بود (۱۸۹۰)، و در آخرین سال‌ها با قیچی و کاغذ رنگی «نقاشی» می‌کرد
🔹
مونه: «منظره‌ای از روئل» در ۱۷ سالگی، تا نیلوفرهای آبی که تا لحظه مرگ رهایشان نکرد
🔹
فریدا: «خودنگاره با لباس مخملی» (۱۹۲۶) پس از تصادف، تا «زنده باد زندگی»، هشت روز پیش از مرگش
🔹
کلیمت: طراحی زغال یک دختر در ۱۷ سالگی، تا «عروس» که ناتمام روی سه‌ پایه‌اش ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/691041" target="_blank">📅 23:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691039">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رویترز: داده‌ها نشان می‌دهند که حجم حمل‌ونقل از طریق تنگه هرمز همچنان کمتر از میانگین ۱۰ روز است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/691039" target="_blank">📅 23:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691038">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
سخنگوی دولت عراق: ۸ مهر آغاز مرحله جدید روابط بغداد با ائتلاف بین‌المللی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/691038" target="_blank">📅 23:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691037">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d124f0d6.mp4?token=G1i74il6LPiLgjIAEVD8_usNdCkNRWoF3Def8ZNPkAkRDFx_IB4CKIkeKPlaaFBbdJCMKb9craNYYVfjlNGfk4gbNp2RYlL7z06XcrhPSQXd8oj-SftrD71ce5M7gkpRyW5g7YNHVQH8SB0_EMLKSrVm-zkhlJOX3bKeqtPgMFyem7YjgBIB7Slfvc4HdpMVcQNEZGDfJySM3Rn5755S-B3MRfeWelxW8yd3Zmk_TdQ9_CY70cKlnuQTi_1ndiHepFarip-DrQe9p9HneartDcOspSdiKk7TXYuQSQKmbG3D_VXfjRZFjPY7t5jZoEpu7A8ciPUskQzpK_2OEi4xCKpHinCjDcg0ZNhLTGuLxY-b62mMnxxhwpkfDT7p8G1DsyOCc80tH2aN2dm3tG77KhIgno-rOIRVu3t4TpOCya3efY4RPUz7xN4U1Gt-I7wpUv_ZpvT378kpydtq-uQJXP8H7TmGDpiTdjk2jXHeWfakp_1WYOkyeHkxGGysGGE_FgECjCcoesj5ugBYLOM54U59l16EVkNGvxfVeo-djzlSEC_x7-XHGGLysGsTmY6MYHgxHQ_L0wjbPAe3sPzuPIRfV4et_PMAc3-emvAc85S5xdGIPx8sxUZhMfWPUF_pcVIgeAJTkIYP0vclY4Wlgu7HRq73tRzH0NAEZh_nKPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d124f0d6.mp4?token=G1i74il6LPiLgjIAEVD8_usNdCkNRWoF3Def8ZNPkAkRDFx_IB4CKIkeKPlaaFBbdJCMKb9craNYYVfjlNGfk4gbNp2RYlL7z06XcrhPSQXd8oj-SftrD71ce5M7gkpRyW5g7YNHVQH8SB0_EMLKSrVm-zkhlJOX3bKeqtPgMFyem7YjgBIB7Slfvc4HdpMVcQNEZGDfJySM3Rn5755S-B3MRfeWelxW8yd3Zmk_TdQ9_CY70cKlnuQTi_1ndiHepFarip-DrQe9p9HneartDcOspSdiKk7TXYuQSQKmbG3D_VXfjRZFjPY7t5jZoEpu7A8ciPUskQzpK_2OEi4xCKpHinCjDcg0ZNhLTGuLxY-b62mMnxxhwpkfDT7p8G1DsyOCc80tH2aN2dm3tG77KhIgno-rOIRVu3t4TpOCya3efY4RPUz7xN4U1Gt-I7wpUv_ZpvT378kpydtq-uQJXP8H7TmGDpiTdjk2jXHeWfakp_1WYOkyeHkxGGysGGE_FgECjCcoesj5ugBYLOM54U59l16EVkNGvxfVeo-djzlSEC_x7-XHGGLysGsTmY6MYHgxHQ_L0wjbPAe3sPzuPIRfV4et_PMAc3-emvAc85S5xdGIPx8sxUZhMfWPUF_pcVIgeAJTkIYP0vclY4Wlgu7HRq73tRzH0NAEZh_nKPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت شگفت‌انگیز رقص موج؛ چند ثانیه که به ۴۰ ثانیه تماشایی تبدیل شد
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/691037" target="_blank">📅 22:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691036">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985f734a23.mp4?token=lC06lAckgBZQJl2gecHUa500M27XnznLEudtADchqHEhY8PB46jQm_b_Q9M_KN9rjBm-rH43-vsr7HUdUTvllhfx0dFZ0yawHaXckzarrs4--WC8Q1OE0Ag0A5jo4XBKsInLSsIvEtfw8kutbaT2gBKM6zP_-vJs2_23DmZRnxihD7dMzafULx5MUaUc6RaUbE5Ell4i5OM1fzMA3PIUgO31wzwgLlYp8ZJrekCMH28noWopu9sBKgCbMPI9As-sbk8vBvfoZIb0PqdagArAOuz9ye96N-MmXVy3qMAKCUR5LPiB_ubu8Y0AbyTbCy9u4j9bvTxS38HmHX1BHPDEcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985f734a23.mp4?token=lC06lAckgBZQJl2gecHUa500M27XnznLEudtADchqHEhY8PB46jQm_b_Q9M_KN9rjBm-rH43-vsr7HUdUTvllhfx0dFZ0yawHaXckzarrs4--WC8Q1OE0Ag0A5jo4XBKsInLSsIvEtfw8kutbaT2gBKM6zP_-vJs2_23DmZRnxihD7dMzafULx5MUaUc6RaUbE5Ell4i5OM1fzMA3PIUgO31wzwgLlYp8ZJrekCMH28noWopu9sBKgCbMPI9As-sbk8vBvfoZIb0PqdagArAOuz9ye96N-MmXVy3qMAKCUR5LPiB_ubu8Y0AbyTbCy9u4j9bvTxS38HmHX1BHPDEcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشکر آقای شهید ایران از جانفدایان ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/691036" target="_blank">📅 22:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691035">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
عضو ارشد انصارالله: عربستان خواستار میانجی‌گری ایران شده است
🔹
پیش از این سخنگوی وزارت خارجهٔ ایران تأکید کرده بود: «انصارالله بازیگری مستقل است که خود تصمیم می‌گیرد؛ نه از کسی دستور می‌پذیرد و نه نیابتی دیگران است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/691035" target="_blank">📅 22:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691034">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
وحشت ترامپ از افشاگری رسانه‌های مستقل
🔹
ترامپ جنایتکار، در اقدامی خلاف قوانین بین‌المللی ورود خبرنگاران شبکه‌های خبری
سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و وبگاه پولیتیکو
به کاخ سفید را ممنوع کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/691034" target="_blank">📅 22:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691033">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0510776e2.mp4?token=TYML69b1P0eubrf6Yy1HRWMS8PrUYI0W3ZCE4nAhAP0W6sSCioOvoW4tKKsaA_ZRmcNEygm7rvOcGjr8SMkgMCI9IN8K_Lw0LIvZP1gh541f6odFGsJJpgAx0DOevs4XiA3a36iv1I6aBsoQ5Voj2rmWeCXHUC5pkSPcD0iYV0iHPSeX_7Vqa2UrQ-7WBKR_x1RCjnbSxTmqJzXjLXCO4RxVVa258Mf9CRO09lAKebEuTJuGKhFav3JUPbGqq0pRUft60gCyXIcR1i9sdaOeCSGwmKTE6lxxLNL2eoka0i_o4Y_1u1qnmLGEmV8C7_8flHAr2c2QwiZtWeFTwzsU3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0510776e2.mp4?token=TYML69b1P0eubrf6Yy1HRWMS8PrUYI0W3ZCE4nAhAP0W6sSCioOvoW4tKKsaA_ZRmcNEygm7rvOcGjr8SMkgMCI9IN8K_Lw0LIvZP1gh541f6odFGsJJpgAx0DOevs4XiA3a36iv1I6aBsoQ5Voj2rmWeCXHUC5pkSPcD0iYV0iHPSeX_7Vqa2UrQ-7WBKR_x1RCjnbSxTmqJzXjLXCO4RxVVa258Mf9CRO09lAKebEuTJuGKhFav3JUPbGqq0pRUft60gCyXIcR1i9sdaOeCSGwmKTE6lxxLNL2eoka0i_o4Y_1u1qnmLGEmV8C7_8flHAr2c2QwiZtWeFTwzsU3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معطلی رانندگان بدون امکانات پشت مرزها/ اینجا منطقه آزاد نیست، منطقه آزار است!
🔹
نبود امکانات اولیه رفاهی و معطلی‌های چند ساعته در صف‌های کیلومتری ترانزیت، روند عبور از مرز را برای رانندگان خودروهای سنگین به کلافی سردرگم تبدیل کرده است./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/qJni4yP2kbU
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/691033" target="_blank">📅 22:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691032">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4168e38cac.mp4?token=m99kE59F_Avhdf3SoczCY4lTJaXZWvG4gE4BamF3F_a59MDnW9GBU13SKXBl7S4RFm0PiHPtavit9Zv14Tsuji3WBY655823siDbYaED261UdtBRNgTJHJNiyZ0DR1VdToUTZ2JZagDlwyTaSMABN6nPOtf-BVJ5jpz7cCjQIR9AqdnF_caRPaGdTbyJATmKc0XtVV1BdY2ujlPm7FQzfXIHuy4M1evVIaS5jlYsKZgeYa7xgcyca8H3t96xCnnoskzS14Fi8gvt16_ZC1xz52es9a_MIgI6daxorGXWBWXv3Fjjh-p3OzOYK5WzR9J9gGyZUu7VUai6F4Q_IsAR4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4168e38cac.mp4?token=m99kE59F_Avhdf3SoczCY4lTJaXZWvG4gE4BamF3F_a59MDnW9GBU13SKXBl7S4RFm0PiHPtavit9Zv14Tsuji3WBY655823siDbYaED261UdtBRNgTJHJNiyZ0DR1VdToUTZ2JZagDlwyTaSMABN6nPOtf-BVJ5jpz7cCjQIR9AqdnF_caRPaGdTbyJATmKc0XtVV1BdY2ujlPm7FQzfXIHuy4M1evVIaS5jlYsKZgeYa7xgcyca8H3t96xCnnoskzS14Fi8gvt16_ZC1xz52es9a_MIgI6daxorGXWBWXv3Fjjh-p3OzOYK5WzR9J9gGyZUu7VUai6F4Q_IsAR4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درد دارو
🔹
صدای شما از چالش‌های درمان؛ بازتاب مشکلات و سرگردانی بیماران در تامین داروهای حیاتی.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/691032" target="_blank">📅 22:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691031">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای واشنگتن‌پست: تعداد بیشتری از نیروهای نظامی آمریکا در جریان جنگ با ایران کشته شده‌اند، اما پنتاگون این تلفات را به‌طور عمومی اعلام نکرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/691031" target="_blank">📅 22:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691030">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmFI_i8AVuOz-lco_HUObAGuPdCB2ATa_OFBr_0XhjCSbLckchbjGHiI_y9ccanIwcJGdVPugyfOogJLhVt-bbs2jX5pWYobmJUrriPCyvNwhsIu5J1_XV77KbRnVa2PcZRIM7TxpCtWr_oEFoVvUSwKunG0gxiRh9VBjRIytxqR70AeEQZzIGIoy-M1C0Ggdlaka9TMWUWgw7Wvk4zdUw1FscPtuOXFqc1P077GzshR-3ZuwryuRwYis9mo6VtpSkHp_Mc5vl33XV3IMN68u0vgnE3ShHf8-zsDB4OO8Udc7Cql81CRVieLjgrbMZxem8dxYVcYlBDxhHLhKRFPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار اجاره جنوب تهران هم دیگر ارزان نیست؛ بررسی ۱۰ فایل منتخب نشان می‌دهد حتی برای واحدهای میان ‌متراژ هم مستأجر باید با ودیعه‌های چند صد میلیونی و اجاره‌های سنگین دست و پنجه نرم کند
/ تیتر تجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/691030" target="_blank">📅 22:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691029">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dd4c53c0.mp4?token=ls9ch3fIkyNmR6_TWSOLG-pBETU20n5l7xQrwj1Qk0h2x9booFKrtd9ybhHGV-g04lznUnNknixTQXkDo6QsWRtU5QocrPOOFreiAnWWoZXsa0pk8Plwkvhca0xBRmpZPbBLjjTxL_gCl9ujm4efpn60p89fsmW_Yl5TyjHFk0bTL74J5_y6UucrXih8Fz-kX5i8GzpqNWu3HlVMWX9tBNB4XYQHfFW5C86vPuCXPdcEFx9WvWCMjule4MBsqf2JZ3CvhuJ1Wfa-eyZAaAcOHrKraZJqqpYQGxumt1yVX1jsCw6NU3Orh0wN-bo1ACpIZIm32_2ZjPsTehsqFl1rBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dd4c53c0.mp4?token=ls9ch3fIkyNmR6_TWSOLG-pBETU20n5l7xQrwj1Qk0h2x9booFKrtd9ybhHGV-g04lznUnNknixTQXkDo6QsWRtU5QocrPOOFreiAnWWoZXsa0pk8Plwkvhca0xBRmpZPbBLjjTxL_gCl9ujm4efpn60p89fsmW_Yl5TyjHFk0bTL74J5_y6UucrXih8Fz-kX5i8GzpqNWu3HlVMWX9tBNB4XYQHfFW5C86vPuCXPdcEFx9WvWCMjule4MBsqf2JZ3CvhuJ1Wfa-eyZAaAcOHrKraZJqqpYQGxumt1yVX1jsCw6NU3Orh0wN-bo1ACpIZIm32_2ZjPsTehsqFl1rBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش شجاعت جان‌برکفان در رزمایش هزاران نفری جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/691029" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691027">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oi62KwyDVzPpbilyshTSrDcnH9HKLuCWzz9RMHUw6EWInV8Lx91bMTrw1muVV4VJ4xxhlPiBYlma0uoA-apjbytvsldv1W4R8Zr9dwmh3zlNidOdpUsK-4QfhYHP4NY4Xbb8XJISpV8RCZkzqc9CcCEgESEHfUl5vWJ5rAvysXwTSBymTrE3UcaRS0LGV8yo1w1CUhRq9llCpUI-JAj8xsFSJ9T3T3wM_d858m1GO2iWMSXmrSf8Nw-By-LBbofy_hh-r85h4GxtCAIqhr4uF-ePqAM8rF2CfZ9J4O-eAwOxtf7KCBpvACEtCThaWxY_ivaFuHe9GnMhZ3f5a9sL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQX3aXswWaNE2i7euBDWOtX_s8m-KXVEcfxBjj6JYuG0s_79X2o-VAjwRGqQ8bH4D0ZqaIun6ZcbEeHjqkhP8GD1EejeDd0N9P9Hx-51dJd3g8HlL6SMtTVwcgJNcLnqTVsujdL2K69D9GcXHkzDYmY_l0hxpUUnHxvqMhatJLmJI-VL-2mOKoZRq1E_-V13cU7GLrhk2wjTPhL_APJF-xFoBJeaCw7GKoMXcE-EJcTp9oCpw-n29LAIodi-hR0TcmU10YtkESBS9C1gDKhqLceSY81zlAVQlMUcERf0x5zGEzN4JPcyRsaMqDMkD1-DeBKDIIjwIlrD8scMjbL0uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میزان خرده‌فروشی آنلاین و کالاهای تندمصرف در سال ۱۴۰۳
🔹
آمار انجمن تجارت الکترونیک تهران نشان می‌دهد «زیورآلات، طلا و مسکوکات» با ۴۵۰.۷ هزار میلیارد تومان، بیشترین سهم را از میزان مصرف خرده‌فروشی آنلاین در سال ۱۴۰۳ داشته است.
🔹
پس از آن «لوازم خانگی برقی» با ۲۸۹.۶ و «مد و پوشاک» با ۲۳۸.۴ هزار میلیارد تومان قرار دارند.
🔹
در بخش کالاهای تندمصرف (FMCG)، «خوراکی‌ها» با ۹۰.۸ درصد سهم مطلق بازار آنلاین را در دست دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/691027" target="_blank">📅 22:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691026">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
پوتین: روسیه هیچ برنامه تهاجمی علیه اروپا ندارد و آماده همکاری و احیای روابط با همسایگان اروپایی خود است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/691026" target="_blank">📅 22:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691025">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7R9oqY-FcLTZ4Fe5S9vOmC0kFtMuD7KqFal1ttSTn9aAYVXqioc8PjgJi4fpP587Z20lvtF8GLBBat22ZTlwjsRWiB7SwkmCDOnNZ3FLsTr8V_hcN9ZpCnaLCCNnp_p6nFNbEX_evGFZkpRDue9bXDA3LREijz8r9Fbl5rSOc4rJnKBCerW3ygZkDAJFuraKfLzVO6IsMV5tp__DKa3_0mGnO6WVkvMVIKMImD1LAftYOLT7NerIbAvhPgpcAHyE1CwIuOatnXPDG8_0yqk2lW0MQRKRmzkQiLwNndUKNNqxSoKv_ylWa85_mrbbs6evL5T26dnebzNUdDw89NcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بوریس جانسون: عمران خان در زندان کوچکی در پاکستان در حال مرگ تدریجی است
🔹
بوریس جانسون، نخست‌وزیر پیشین بریتانیا، با اشاره به وضعیت عمران خان، نخست‌وزیر سابق پاکستان، خواستار استفاده بریتانیا از نفوذ خود برای کمک به آزادی او شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/691025" target="_blank">📅 22:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691024">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac7470020.mp4?token=kN68K7qcT02f1VZRbWbP-h8FSOEeAFhqRYiZxVEyWH-JBnvu7YLGnwb_7ULHLwM1T33XHV7OwS6B4lAzvDQPMdGeOaFeepykKkT4uqKnhj-0KhBYcJqwO9aV9dpKRlHEovAoBCpcXm_mZSUIs1SuRLnudcmQB513AvZDKprSOX2OXwugJwhIjKcikBaz5ZzD4S21zKrGG4VPE-5ebTMCdbAlsCbZPQhxpTiU80XrxtL1_VPuyxouHBMz9s0Ny5szaIuloYXD75IX6akdBeE2cyGHih-WLeS4vu3BKWLqh_pkiZY2sYqHDpq2KhYucyWX6GpIvwnC_WA5Idg7cQ066g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac7470020.mp4?token=kN68K7qcT02f1VZRbWbP-h8FSOEeAFhqRYiZxVEyWH-JBnvu7YLGnwb_7ULHLwM1T33XHV7OwS6B4lAzvDQPMdGeOaFeepykKkT4uqKnhj-0KhBYcJqwO9aV9dpKRlHEovAoBCpcXm_mZSUIs1SuRLnudcmQB513AvZDKprSOX2OXwugJwhIjKcikBaz5ZzD4S21zKrGG4VPE-5ebTMCdbAlsCbZPQhxpTiU80XrxtL1_VPuyxouHBMz9s0Ny5szaIuloYXD75IX6akdBeE2cyGHih-WLeS4vu3BKWLqh_pkiZY2sYqHDpq2KhYucyWX6GpIvwnC_WA5Idg7cQ066g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیرترین موجود زنده جهان؛ کوسه گرینلندی که ۳۹۰ سال از عمرش می‌گذرد/ متولد شده قبل از نیوتون، موتسارت و داروین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/691024" target="_blank">📅 22:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691023">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4994b7f7.mp4?token=TNgK5O_DscgLJKgwMqb3qtpPb-qKeZb4Mh2Q6Ibm9tgUaVFWmHiqSl_eelsjODINWFbfDrL3BEY69xVxDy2OJGUSCJGg8TcMLaobRocYlbqi6UxHNNcGeMmxZcc2vpSAromUYVc2IIRpZMVLsmhWcH6aZLQJ0U4Pq-5sqK-NeU_EContiWXLtapVz3kERXEN28pFcvnTJ9TuC7T3rMTpAjjq1-yPW0OLHtWvtXpMFZCztyw4p-_aYTnPXxhY9ZCee0ZiDn2pjhiFb2K5gOFaNYNmim_TYQh3bhoq6QxSpOH26XHI2r7ZX4otFjjsrf5Vp0Jk3Twp-SmTdXVbty0fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4994b7f7.mp4?token=TNgK5O_DscgLJKgwMqb3qtpPb-qKeZb4Mh2Q6Ibm9tgUaVFWmHiqSl_eelsjODINWFbfDrL3BEY69xVxDy2OJGUSCJGg8TcMLaobRocYlbqi6UxHNNcGeMmxZcc2vpSAromUYVc2IIRpZMVLsmhWcH6aZLQJ0U4Pq-5sqK-NeU_EContiWXLtapVz3kERXEN28pFcvnTJ9TuC7T3rMTpAjjq1-yPW0OLHtWvtXpMFZCztyw4p-_aYTnPXxhY9ZCee0ZiDn2pjhiFb2K5gOFaNYNmim_TYQh3bhoq6QxSpOH26XHI2r7ZX4otFjjsrf5Vp0Jk3Twp-SmTdXVbty0fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لبیک یا خامنه‌ای
🔹
اوج همبستگی و وحدت مردم در رزمایش بزرگ جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/691023" target="_blank">📅 22:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691022">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1-v3wbGYG-trDD2BF2Q_stJy2AQLGhYDtFIJpe2mfmqmiczkZQv-6-UFbrgUuVfLsjD2t1ebg_26y9wi6jo-Bm43CMr-qvfJqHHz9LcKA0DR4fFN1A0kM6k9pO2gq0WZwv_ocedjdm288zaa18ARwHfx3uRmviuq9rJlk2IpDQ1FuRX2Y0nNVFNoR8Ubk22xVOLDjiyf-0S1JOdXLPlQb3JI25bBeYBTCwibDHcZcPcTWlI-tok5Rs5QXY2wjHSWeWPELCsKIbb5IpqGTVP1Ef0sPRZQWZNa3vf91aN5idRBNz2c1oOjrSlwxqchiu-M_Wc1mTKv0cHXqxgulDDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: محبوبیتم در جمهوری‌خواهان ۹۵ درصد است!
رئیس‌جمهور تروریست آمریکا:
🔹
میزان محبوبیت ترامپ در حزب جمهوری‌خواه اکنون ۹۵ درصد است که یک رکورد محسوب می‌شود. رونالد ریگان با ۸۶ درصد در جایگاه دوم قرار دارد. متشکرم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/691022" target="_blank">📅 22:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691020">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تهدید به «فرستادن به استخر»؛ زیدآبادی درباره مرگ هاشمی رفسنجانی: فرزندان هاشمی مدعی مرگ عمدی پدرشان هستند
🔹
زیدآبادی: اگر مدرک دارند شکایت کنند، وگرنه تکرار نکنند، حالا تندروها هم همین را می‌گویند. یک طلبه روحانی را به «فرستادن به استخر» تهدید کرده. قبلاً هم در زمان ریاست‌جمهوری روحانی، طلابی پلاکارد داشتند: «ای آنکه مذاکره شعارت، استخر فرح در انتظارت!»
🔹
یعنی مرگ عمدی را قبول دارند و دیگران را هم تهدید می‌کنند؛ اگر قوه قضائیه قصد بررسی این موضوع را دارد، این افراد را احضار کند: اگر مدرک دارند، پرونده تشکیل شود؛ اگر ندارند، باید بگویند چرا چنین ادعاهایی می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/691020" target="_blank">📅 21:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691019">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای الجزیره به نقل از یک منبع آگاه آمریکایی‌: ۶۰ میلیون بشکه نفت ایران یا نفتی که احتمالاً ایرانی است، در نفتکش‌های تحت تحریم بلاتکلیف مانده است
🔹
واردات نفت ایران یا نفتی که احتمالا متعلق به ایران است توسط چین، به ۴۴۰ هزار بشکه در روز کاهش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/691019" target="_blank">📅 21:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691018">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمرکز اطلاع رسانی بانک صنعت و معدن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6ec2409e.mp4?token=kNa41A0aZhWPPz8bXRfg1cKSN74XdnOf9IZMQQh1v0ApY0tNc9ISOe1otPfAk_oJqiLVgumIgms6886FLkTupfU_uUmki1hLKoSvcFU6q6sigXMjdK272D60oNZIyrLSD20bkV-nZyvESKkMPEMqXqDPd5uC8e3-x4rk-5eNnq7odDOsfjePPwO57Hp95-1ukVvaCn6bdCyTjfve50g3EnaaK6OfPJvPEEKl7pvJBi-Tby4NK2R78vuF8tEuMF_igyd8LDEvqL2nhfEYYnwAAFGynYLWeNOl7AvEBMd2dMDg4HUQCuIxj6TfcuqZFwDp_faTY68kLtT8dhHYtV9m0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6ec2409e.mp4?token=kNa41A0aZhWPPz8bXRfg1cKSN74XdnOf9IZMQQh1v0ApY0tNc9ISOe1otPfAk_oJqiLVgumIgms6886FLkTupfU_uUmki1hLKoSvcFU6q6sigXMjdK272D60oNZIyrLSD20bkV-nZyvESKkMPEMqXqDPd5uC8e3-x4rk-5eNnq7odDOsfjePPwO57Hp95-1ukVvaCn6bdCyTjfve50g3EnaaK6OfPJvPEEKl7pvJBi-Tby4NK2R78vuF8tEuMF_igyd8LDEvqL2nhfEYYnwAAFGynYLWeNOl7AvEBMd2dMDg4HUQCuIxj6TfcuqZFwDp_faTY68kLtT8dhHYtV9m0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دکتر
شایان
:
بانک
صنعت
و
معدن
طرح
توسعه
واحد
داروسازی
فریمان
را
به‌تنهایی
تأمین
مالی
می‌کند
🔹
مدیرعامل بانک صنعت و معدن در جریان سفر به استان خراسان رضوی از تأمین مالی کامل و یکپارچه طرح توسعه واحد داروسازی دانش‌بنیان فریمان توسط این بانک خبر داد و اعلام کرد: طرح توسعه این پروژه تا پایان سال به بهره‌برداری می‌رسد.
▫️
در راستای حمایت از تولید، بانک صنعت و معدن متناسب با سرمایه‌گذاری مجری طرح، مسئولیت کامل تأمین مالی طرح توسعه این واحد داروسازی را بر عهده گرفته تا بر اساس برنامه تا پایان سال افتتاح شود.
سایت
|
بله
|
تلگرام
|
اینستاگرام</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/691018" target="_blank">📅 21:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691017">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7586235fd.mp4?token=Gf9fjwTkbNCf8yNzcWwNDUdQrks-Syi73HoyN0ZKZixJiG3tgQofqZbFhbaHOFjYyCNEbpG3v-Gu6GWxEKeo8gy-hmG0czkypxdgRhG8mfRFsGHogAVrWHhQZX1Ru7fMhNK6eeKUF1BUyZHYKCKTZhWin1SLFV4VsDod0DymcYkFf-e2NSVS_DM9EY8NZzARtwe0gZNwqyamtT6_g4dvLBn2SXUNCUBaOyhH2UUnvGOr2-mnIDUs2qDo2LH5dr2wY8-NgIBaRII14A551-49ny7UXhVrtJLXj8iKlqi8OCPzCrjGDEnA9fjtU6mLQgowcDn86Qkp0ZBTlfyVi79J6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7586235fd.mp4?token=Gf9fjwTkbNCf8yNzcWwNDUdQrks-Syi73HoyN0ZKZixJiG3tgQofqZbFhbaHOFjYyCNEbpG3v-Gu6GWxEKeo8gy-hmG0czkypxdgRhG8mfRFsGHogAVrWHhQZX1Ru7fMhNK6eeKUF1BUyZHYKCKTZhWin1SLFV4VsDod0DymcYkFf-e2NSVS_DM9EY8NZzARtwe0gZNwqyamtT6_g4dvLBn2SXUNCUBaOyhH2UUnvGOr2-mnIDUs2qDo2LH5dr2wY8-NgIBaRII14A551-49ny7UXhVrtJLXj8iKlqi8OCPzCrjGDEnA9fjtU6mLQgowcDn86Qkp0ZBTlfyVi79J6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تنظیمات رو یاد بگیر چون باعث میشه با گوشی سامسونگ عکس‌های خلاقانه بگیری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/691017" target="_blank">📅 21:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691016">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار آذربایجان شرقی(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d741aca11e.mp4?token=lPlEHrMs2OU0jt1k8S_jBlsVqzXDjrNNSI0yLyVLjc2LcMFYar2eebxsOJdW3mwAYfQ-ZKHbyI3m-c3ShJZGdX8S-2PAmFolmcyUMEZaGF1GIATfGQKxCep1URJp-iOF1xrGnP-2ALMkTFJuLPAeM8T5pRFGNmoL8CbBzjJ7OooYSPYX9znIcPz2cvvaooceZSzj6d3g7Z7Z_8foIBYNe6PR_Ol1BeL-HafLziWSqXeeE4Q9BSEdpnj0CPzz58DwduB8KThKBMRK9XWT-29HkJ-GmYZXoCW68hQaBEEGpKnFtOFY-7w8xDUfLVJfpMGvQ7cuADP-fTDrMM9T8Bxo9oeI-BzFvs0inmd9ZWD8_rhDSK2tukK9QDXTLhvny3Iz_DMb9i3fslBe6zWwu7ZvxQGn3XautWDIlJJZUpAQDtrnpLth8U7PQLj_b0swsAaLi-pRd_KcLl4nZDPoU0Z3m3GPi9K2FjCv20AE3XtLmQweS3jO4JIbqPjzK0VE5Luvhyj3zI-B4SqCALclTiCgKgt0h-N5aA7HyQH3q80dPpeDWvUClt6k7pnKkrxXmkrIXu-UfOrfD-K8oLkpiJ1LlbQ5LG5kduvg2ACIjQjz62u71W7Z5yGYeBu4x6gycxbjffpOnB63rrh2aMkkuQOI3pdS-nyDa7yfuQd247EbRJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d741aca11e.mp4?token=lPlEHrMs2OU0jt1k8S_jBlsVqzXDjrNNSI0yLyVLjc2LcMFYar2eebxsOJdW3mwAYfQ-ZKHbyI3m-c3ShJZGdX8S-2PAmFolmcyUMEZaGF1GIATfGQKxCep1URJp-iOF1xrGnP-2ALMkTFJuLPAeM8T5pRFGNmoL8CbBzjJ7OooYSPYX9znIcPz2cvvaooceZSzj6d3g7Z7Z_8foIBYNe6PR_Ol1BeL-HafLziWSqXeeE4Q9BSEdpnj0CPzz58DwduB8KThKBMRK9XWT-29HkJ-GmYZXoCW68hQaBEEGpKnFtOFY-7w8xDUfLVJfpMGvQ7cuADP-fTDrMM9T8Bxo9oeI-BzFvs0inmd9ZWD8_rhDSK2tukK9QDXTLhvny3Iz_DMb9i3fslBe6zWwu7ZvxQGn3XautWDIlJJZUpAQDtrnpLth8U7PQLj_b0swsAaLi-pRd_KcLl4nZDPoU0Z3m3GPi9K2FjCv20AE3XtLmQweS3jO4JIbqPjzK0VE5Luvhyj3zI-B4SqCALclTiCgKgt0h-N5aA7HyQH3q80dPpeDWvUClt6k7pnKkrxXmkrIXu-UfOrfD-K8oLkpiJ1LlbQ5LG5kduvg2ACIjQjz62u71W7Z5yGYeBu4x6gycxbjffpOnB63rrh2aMkkuQOI3pdS-nyDa7yfuQd247EbRJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهریار را همه با شعرهایش می‌شناسند؛اما پشت این نام، زندگی‌ای بود پر از انتخاب‌ها، دلتنگی‌ها و اتفاق‌هایی که مسیرش را برای همیشه عوض کردند
🔹
از تبریز تا جایی که نام «شهریار» ماندگار شد، قصه‌ای هست که خیلی‌ها فقط بخش کوچکی از آن را شنیده‌اند.
🔹
این ویدیو، روایت کوتاهی از زندگی مردی‌ست که شعر، فقط بخشی از داستانش بود.
۲۷ شهریور،روز بزرگداشت استاد شهریار
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/691016" target="_blank">📅 21:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691014">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDbfJmGoY3LmlCzF5RwKjcDpMY_L2iGL8BKgOoyItdPJi9lahZ-P6EEJMQTObWmWp3i100UQN3J3yswAlpNO3YxOb87Ddt6kgdTx6-ci_FR5wIspos1W4kU6uZnAFU1xnGBJ2XGCCYyLpJdQVytKZ5ij4-8go7_B9KsV4DzHwqM_Hxp6125UtWWCz5e4IoLKps83erToEITad4O6VxZuVeBQukohLe5iS83Xpi9bYp7YLAMDN8D6QTqEd_WRAh7_DSM8bRXGH6oHP_6zQcc1JWxCAsVz1QSPqntZNdAAwvRjj2JlL6aXIXn9S0udbeG4cFHHCHZBtSZy8SOH5REyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TAO7c7AIlWKzq4xJvoc4Wuk1FK3ujtQMq5cC0cMys465Koo5elpNbYVZsxUX7zSPQ3IZ_v73gn8hmLHxzrLXjkf0lQRW0f23MN135JWJ7ahoB92engN4Q42h6jcgmOmGF09Z9eQtEvstq_Pm-2a9oVnDQNYb4ac2Xjvhc4iTr029cgndVkKEJ8vIh8tPnZN4r6AiFHMGBtU4dfjBQkDR-YRVIKfjiLw_DFSqXzT2j9xdfJ5gGxN1Xpe2orYvC4bxPmlfbsC8P5bFOwmkxBcqT9JN5c2MnSjp4hpFxRI6zU1sn_aMWCT133Kd9YBjJe8tEddil6arWeVyS0s5obSSiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مشارکت بانوان هلال احمر در رزمایش بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/691014" target="_blank">📅 21:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691013">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
فاکس بیزنس: فرستاده آمریکا برای افزایش فشار بر ایران عازم امارات، ترکیه، عمان و بریتانیا شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/691013" target="_blank">📅 21:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691012">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0e624bbe2.mp4?token=H4pOFIrzkZnSGnMhkPgOoXLpZytKWLQBHbNdTT27Wsq2WEEr225mwHQUMGiUELv4OWFufI2LRFJg_tVtfiThF6WW6JaAD4WYZ1HhnrC4z4tPp1Td98MuDCLvUUpr8PsXk-teRgSPG71X_258l84W_TtdooZXPlTxbHHwMYMYh0Nv2RO9-MObKs7qvZ2Tq9nldGuSoeMn1KGaOMMTah7tcYdV5jt9o_RGmX0Cmg-YOzdLbVaw2YCtzCkWjz7CoBjq4Ohb6agVUAbFjhFNnaknIpZ4sI30mhms0O4mwfol0zoTwKY0c3ZhU2acfAiV-UUS5UVOIXVO2MgVUX5P-FekGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0e624bbe2.mp4?token=H4pOFIrzkZnSGnMhkPgOoXLpZytKWLQBHbNdTT27Wsq2WEEr225mwHQUMGiUELv4OWFufI2LRFJg_tVtfiThF6WW6JaAD4WYZ1HhnrC4z4tPp1Td98MuDCLvUUpr8PsXk-teRgSPG71X_258l84W_TtdooZXPlTxbHHwMYMYh0Nv2RO9-MObKs7qvZ2Tq9nldGuSoeMn1KGaOMMTah7tcYdV5jt9o_RGmX0Cmg-YOzdLbVaw2YCtzCkWjz7CoBjq4Ohb6agVUAbFjhFNnaknIpZ4sI30mhms0O4mwfol0zoTwKY0c3ZhU2acfAiV-UUS5UVOIXVO2MgVUX5P-FekGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده از نوزاد تازه متولد شده که حالت خاص اون مورد توجه کاربران قرار گرفته است
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/691012" target="_blank">📅 21:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691011">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
العربیه به نقل از منبع آگاه: وزیر کشور پاکستان طی ساعات آینده به ایران سفر خواهد کرد
🔹
او در تهران درباره تشدید اقدامات انصارالله در یمن گفتگو خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/691011" target="_blank">📅 21:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691010">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
جنگ در کمین انگلیس؟
بی‌بی‌سی:
🔹
دولت انگلیس از شهروندان خود خواسته است که مواد غذایی کنسرو شده و آب آشامیدنی ذخیره را برای جنگ احتمالی با روسیه آماده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/691010" target="_blank">📅 21:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691009">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mA2Yb45UJ_C3PN_Rg97KMSNxf0Qs5gbHKRbcQheX8STc3-MQRjbHUkJShS2nCCoxxTEzJgwaZIUgIgKJT7IMYDgqgqk2VEyhNlaG5qT4kwVdCedMKyYsbu2_dnF1GUzf7rY7q6CUyAlgcmsneemGqhrbkte585ETj3q1-yxFCy9NQpGu9fTIxdXXeF92yufU1meYcEiXqKn1akZmxf5XQ4w5TJtVpwpZerVorHfGpm-uzP4_W6hH7LVSQ9-a-M9lHp_5OQ4ExKC544xZAynJDG9j87ZuiHePLB2kSA_k2FKBm6bTMY3w9Xf8ZK1NvJ1SwcPNwZd_0_1RStQ21u6-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام های درد بدن رو بدونیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/691009" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691000">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ar24WWoHkI2SFkF7xjyXTJpzQ5-IKjozJTuVzT4kVMHkPjmWhn9UJqsdVy156PBEdDrnge3D0txoM3ZPz2j8-twfvPt6m0giQ8wIQckkCbccvKtKrC-ALQ6MazyzJ6wK3jvMLRJUi1rwa5FurqS9xwVWp7FvnSpilWnfgZvl3CsxneDi8ol6RVdKbwJsni743NCcjstf3BJwKaB2mKSwBSmefj2EiX5onQh2ioH4bebVXf3junoFhQigDzyca5GrI8zS38r0JW4x-z9kmpPK9UYSmdc7l-SLluaMYy6_drmAje7PybdH3Zi5zwqkN3GGe6hnquDLX8MYQM4DKGNhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZCnnQlmrhJed9z9CTu9Wg_MCKxKp9GWR_FzmmHb8bFBxk5DkK14dKB01VfS_h_nAvDGVyq8ORyQh8LNVvnT1Bk_RQHjPNxes22cQo2Dhq_b2nmFikYvjInK7P3DGEnumUtBM7I0E4vOOXkNMDTIUAKTRdZqb-kLWnX5_NQqocfUrtfWb9FDUG4PUQ8-EVEDHaTe6nVDDPw--t7qNGwM8HSrEJH5TFB0BGSdchM2qmsIS-dPGfqVIMjkSjJabqDZ5OW3RBZ-nf_Xwrs9dAkmO-RaEPo73O1Lw8ivIlJ8PbXjDu_3cGuXoAnftV70sU7gnwr6M4EMmRZNAjmbOGfR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5wTr8ut2bIjVTtE4h5yEmdJC_0qqEXWn_RQORSF0lsu5UwsX0uEQ-54uGVwZkL2ZQDw55nwVKFV5XSqo2ijkdwMO6jTFI7KQhVLKucMec5_u1WgEHivXSnIJ_NJSJsv5lZJdnNGh4bYrFbSp4d7RhZ9VHF6DZjHOHz4QUc79ky8_mloze6G08G0Y7Nfm-JAr63lTKTcWwWpCpsvXr4n8TeH9W8yLWzTI8hueBFfqT8DAwgEkqm0rZtHuV25tM3DGdX93DadvalXNPcovmJE2xzVg0ItJ5qwwSu0FlnsHvcizTi-2jjuu9eStXTMt08eTDn0L6eAl6u32tEsAzSuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPqHf5dWXZZw9MirsRb5l5tdG5ZptHXatO1qmP8DzLbqV0MDC1lFWcL1JMpZLTpjEIQynLQHXBjRJ2P2rGTORWaCDwH2DgXolGrqHLLDJKmHFEbUZeIpy8F-t_JI2yAgnib7dzBm_RMcU4ZYV6FpW5VA4Tb9vRrYj-vBX_XouEsIhU62wLWA3MOZEcC5z4mDsStI0Do0d2oLUNzCkYAJaXusy4ZHtLy4KWqzdv4Lz7oIl1I8K8iBx19zZoF7qGthAG4Eb_BfN95627uJDDo3o3i1Kjk2icsBRzHwME3KwlbGn1xaP7qq-mS4QUD4PrMOz31yL-S140MtnHPZZKxH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHiq2hg3mbuU2OQaUSMk_e8S6cYh_Udq2ytiwImRpKXAtfuT4n7aziK2XbUuOn2IPnC_MVIEQJPyjvduQ9BIabXe9VH5MwV8ACGzEC1o_gs_IUBbrmxGIWPlfPIt6aN7xmAqPJIDdVQn7eJrwz5JaowPvIROQeUQ740GIIv0rONx4i_PsX8NRFFWDQEpmuM3A7gSYgU9zKRm4bc1zDfAaf72XOCSo0bxQfNU7QrC17tQ61quSHLK7GQzy1ycuMXBKytYS_kF6Vqsv4nS1SN9J2bK3Vva0h-dwGZCRZ1j4zYLQRM4KrcYGE6XAwFo1Xja-J-PZLfIxoLds0pgilZLew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ok4YJzCpIujoAEpAOJwEndTu2Lb3L6S38-ZyFnjG0B-49hY1vyZIcsuUEudXPpDsRfbAMDGBgC3a4wTyQ6xDW-55evHVSyhweLi7ezHYa9fSJycbzgRehaM4vGtWwVRy6HcqZDUCqj7D8zei3gOcFuz2V8XqZJM18qKT9kRoyZubQRYYoSKFp3bQTa6_HqsgfXC-CmY-CUE-9GvK4B6BMKXLsWPXt_4anTrWvcatw3PoashjO0Xw004Fg4UtLajhLCwjL_ks4j1zaXGAZh6VEF-pUwsSC3VAn8RZYdduhv9wvaM1uvXOETIHIYdZkpjxO2k5ZFUxeZq2Rzcqz8I9jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1lg_I6V_YIMX57wje62pjNzBgrWQ2PCD527j7wlkiAD393992KHlvmW0Dop4F4a8g-7SG0RYmEVN6Qye_9UB8c5xJ8P2li8W1LoB6PtI1uU94ykWrtLxgc4LtgaJ8VHNBbZ0fcdhgi4KJcQlf3VRWF2tEP0ADxtBBsZBUQnDnSpkmlUklcua5GPSFniH8ygcYTesfcwVtmat0H5EtS0OBbctpNeMlPgRGC2a5cZLb4imInAlk9YBMyRkBu-p-5BbWpFp0_KH2W0t6VMXyC_h1Q8KCLTtT7VI3gdM70EG3FtPjhJqn4GY3J2_XKpC9Z_ljzPqGEatCwyfUiaBtBpAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IH-npPI6B9raBRc_Gmsbt2FE0KP1tfyFraorbUbbU6K_jaEzVDmCyww0WSVJyf_XdodjqpKu2ERXDL6vwAail44Shb5g7LVfPNch9f72okAH7WFYdnU0WBIneB_Bweh5bB0nVYz2_sRCAMA8owaKPxhOouLvjXTcOfoRUECMIFMw3nOZ9ivz12mgpJ07ejgKEiVTfaKZ2ZV63aIAYELRtKB6zLEz4sPos__8fMTq3G3z8Hdl_JJwiqioNvnJs2GtI0j8nYWJdlVqvPSoW4jG9SIJKJyyzFqvNRISILG9kofmkXE_NnZjuU1tBpOg2jg9Iirb3bwDp0zVpD17hlAiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTM7eruR1WzPlD3ojnyftmJcuWmPozfGd_PRCE3yMG2sf6jOdqBP0xXCb5j2pIBaKePBSMqyLuFda11yris5B7xK2EKkKWk02sWwoKe4PcjNw1kAlYUBlTcsN87DEuQK8T89C9sncE55mUP2BwMmtyyChhxFv1HI_0MxYDf9MQSqI55rMS4MQVDjw3DBgt4Y2soqj3OwcX_eqYid-IdXF_H4bZXo6pTAzu-jMEiGZUnMug9trFX48gwzAa9d7dcNdqOOyinaVtBFHuVCM_mL2YxAzjGak0nFWDvWhMqzrmaWA7S7s4ob5kUTAf_fzJdXXJSf9Wfc07SD0XX9l4qNZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پرچم ایران امانت دستان کوچک؛ جانفدا میزبان کودکانِ و نوزادان ایران زمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/691000" target="_blank">📅 21:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690999">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKI7aVXwWW3BIHBfk-sV1U9h7idHM4G3ShdOmd7zmUSt9CZ0E4WIJSm9JX3dcCpz9n94UOpkF7fN-n_N_bX3OnX2tx7rLUplC2ryFCPjsW8w7vGIA-SsE1h-VvhOl461OpngpUzFkogCGc5ztokZruJaaqhmhG6yGRiHnwbTBozhbDnVqW6VmzwGh9flYYYMbBIG6Vltg4H4I3UmKxK4U2_6ADs-QQFf1xz1VvlQFRlj_quRAwTdJ0xJBopgbMKD5zQLtKNB7kgACWrIaRg20iwz27tr6vOrjuFcRMHgJ-iSFwzmGGE5j1fCDCjzDxMpUJm2tjajpW5t6z1adRfvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: دوره‌ای آغاز شده است که در آن هواپیماهای شما، از نوع F-35 و F-15، مورد هدف قرار می‌گیرند و شما مجبور می‌شوید گزارش دهید که به آنها آسیب رسیده است
🔹
آنچه که روزی یک کابوس وحشتناک بود، اکنون به یک واقعیت روزمره تبدیل شده است؛ شما باید با این موضوع کنار بیایید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/690999" target="_blank">📅 21:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690998">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e616241d65.mp4?token=EZjkt34QwpsSo5N_9njdf8BcKJGaw4RrQmBBmDd6ZjgwoSPtbGwb98pcaBLwviLgvb-AYPLgPlvKoKmswHZUoonkrMWC2c8RuL06xHsxK6srTmfg0nTJLVVU9AlRn0vwF57Ld7bpK6c_6iMZVf2Lrt_G7-rMLvOKPzzYjDLomCJaiyhflY6pD6t1TPKXg6W7oaU4I4pzqscLtJ9BTdA1byabOs51jF8WUbi37119qheNhO2eZgrZZn66piH_PutN0FYcpuHYytW_FvHtOdfeZHKPMreeZ7UgobMJHr9fyTMSL8zzKhbH51E-xwTdcC0UhNBQPbxEUP5vyBmoxZ_mNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e616241d65.mp4?token=EZjkt34QwpsSo5N_9njdf8BcKJGaw4RrQmBBmDd6ZjgwoSPtbGwb98pcaBLwviLgvb-AYPLgPlvKoKmswHZUoonkrMWC2c8RuL06xHsxK6srTmfg0nTJLVVU9AlRn0vwF57Ld7bpK6c_6iMZVf2Lrt_G7-rMLvOKPzzYjDLomCJaiyhflY6pD6t1TPKXg6W7oaU4I4pzqscLtJ9BTdA1byabOs51jF8WUbi37119qheNhO2eZgrZZn66piH_PutN0FYcpuHYytW_FvHtOdfeZHKPMreeZ7UgobMJHr9fyTMSL8zzKhbH51E-xwTdcC0UhNBQPbxEUP5vyBmoxZ_mNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای سینمای دهه ۶۰
🎬
🔹
صداها، دیالوگ‌ها و ملودی‌های فیلم‌های آن دوران برای خیلی‌ها حال‌وهوای خاص و نوستالژیکی داشت؛ «خط پایان» محصول سال ۱۳۶۴ نیز از فیلم‌های پرفروش آن دوره بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/690998" target="_blank">📅 21:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690997">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
یک گزارش جعلی هوش مصنوعی؛ آمریکا نزدیک بود به کشتی چینی حمله کند!
سی‌ان‌ان مدعی شد:
🔹
یک گزارش اطلاعاتی تولیدشده با کمک هوش مصنوعی، نیروهای آمریکایی را به اشتباه انداخت؛ آنها تصور کردند یک کشتی چینی حامل قطعات مورد استفاده در تسلیحات هسته‌ای است و نزدیک بود علیه آن عملیات انجام دهند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/690997" target="_blank">📅 20:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690994">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tJdGeQBYQ1Jex--_-M-t_EcUh7KAMlVvGhqeDmyE_wNSHpMCNJMNEJY0RKQu-YULMDsTm3Gmtttw3rP9Jh35Z2HJHefcKRoxnd3-XL0EfsHygABZ9QhThIhjmfJKLkzNu7SNHO0zANyLcBCWgTbhGbtP9dOgij6otfdy2DBTE2gUe8ctN4vI7XMBuYCtXB05naAwMK6edSU4qc6ZcEwhRq4xQWMBBJ_kuR_blKuX1wPjxGUWiMghtXbKIM5BhxNDrg05RW2g-hT4GtN9qQaKDN2Yt07NL8lNAhbY9Z4DcVWHrX1AMIMP2YtnVfWMFSMzu_loMKuAovU87wvbLIIyhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZpZ4UR7D7DwgKpSTxNz0IFHSFkhoD-snqkxKMqHkOnjOrRE0ZHu6woNh_QHfux5bTgTMzn3YREiihPud2VnCIZyZC_ftXU22pskiVho-dwuP3H7WcWP2T3VyzSaVBij3u9ucjBRm1dbu3tfREMXkbSrRbZCzpUMSspfKILIT5T09m1h0j-pPzOrTB_aBwOIxXrjUgMvhrGWG0oUr1DCVN4fjW4cusaDdDxk-e7qPScZY8ZHN3KhNsZ8WSXLYuMmqMFQEjJs046YJXbTaE-V_cfGpkKITkL4PVRLblVEXHsd3JR6bttMuX8h6QVM_7HNZiuvAtBaO0LlJ7HqrC0xP4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4179a1b0f0.mp4?token=CiLbjJ25cBxzu4pGQKhUB2MgYadtThZHwIwvis7SXy0sDqJP_HUXm6-Mp5NDHC7sydSoqcv5q25VxDRjOFkQQqWzj8bgP7F9R4CR_MWPaqipeSBSwvdsO1_o4mixZB8F7dRBfejv2MNK-YyxEuzMrVwiV0wnoPoBZjxIORCjLhCimAbiv-3BUEAMm2632dierwS0aVKSkIQYwXMCHE8i-KeF5hYHD5zKBHSSmljxV10aPmYzJ8NdzCRNt1v85bU99ctm9HWuLvgaxHRtaZk-qEfIWR-J_s4Dt5OqcKy9nsXcXtdECYLEmf96hA1V3LOBN-v7BlIGXvML3vue-9dTMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4179a1b0f0.mp4?token=CiLbjJ25cBxzu4pGQKhUB2MgYadtThZHwIwvis7SXy0sDqJP_HUXm6-Mp5NDHC7sydSoqcv5q25VxDRjOFkQQqWzj8bgP7F9R4CR_MWPaqipeSBSwvdsO1_o4mixZB8F7dRBfejv2MNK-YyxEuzMrVwiV0wnoPoBZjxIORCjLhCimAbiv-3BUEAMm2632dierwS0aVKSkIQYwXMCHE8i-KeF5hYHD5zKBHSSmljxV10aPmYzJ8NdzCRNt1v85bU99ctm9HWuLvgaxHRtaZk-qEfIWR-J_s4Dt5OqcKy9nsXcXtdECYLEmf96hA1V3LOBN-v7BlIGXvML3vue-9dTMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به یاد کودکان شهید میناب در رزمایش جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/690994" target="_blank">📅 20:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690993">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار سیستان و بلوچستان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d58954e4.mp4?token=mewuTf0-qaY94WNXKpG5dBhFUUvJFxiY4u8_Q2PulBxprmw0c0gTdd_-OknaBKpNqyPUkb2uD491o8GpwmTpTrsxIhTzBH5nKL2uTiTN6ofSW7WWAmaOyW28_1nhacoYv374skdDsAMf_LmqRD2BRsLmyLVbbWdxTJQV7XN2lUdmx5ThQXTIfamKSjds4JWGb5ngr0x3Whtvqd7z0Y8GIMNkn0IKBlxaWG-FjmNNZjlJC1y_2y9n5udANliXsNhtbsuF_oFLbAQwqphjnoUOZ8KSKb-GL-oyQWgcM4K78fHvCyx3eyOlyjT-WghbrR_jpoaoG9I53ArCh10egdc31o3dyilBvETps-7af4y3Z9Kbl62uca6FVqWSUUAl4qSOBoos0Rf3eblKfY_HYHErjebRcxGc07WS1cnjdf4DLvGgyLkzb3Yxxe1RF7nSbA6ZsY9ZL1ckfwDLkdgItybDjcQGEL0ERYZUIkK0eqwVY9Rncd0KwgQOg8tcBogpc5Gtp8ME0u80VPkxS9WNTDFWEsItwiG7hR4uz9C_Fxv7p-yp--JuRHnH7MGiC_pjjwXL3fs0aN9M9NwrL7QQQe0OnhMKwWJbmkqlWPc51EdCEgkReJB4PAC8RqKDM9sqpd7VUbotb5Z4kwhZUbtVpaagpF2GbGCrmaejg1u7Ggbmzoo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d58954e4.mp4?token=mewuTf0-qaY94WNXKpG5dBhFUUvJFxiY4u8_Q2PulBxprmw0c0gTdd_-OknaBKpNqyPUkb2uD491o8GpwmTpTrsxIhTzBH5nKL2uTiTN6ofSW7WWAmaOyW28_1nhacoYv374skdDsAMf_LmqRD2BRsLmyLVbbWdxTJQV7XN2lUdmx5ThQXTIfamKSjds4JWGb5ngr0x3Whtvqd7z0Y8GIMNkn0IKBlxaWG-FjmNNZjlJC1y_2y9n5udANliXsNhtbsuF_oFLbAQwqphjnoUOZ8KSKb-GL-oyQWgcM4K78fHvCyx3eyOlyjT-WghbrR_jpoaoG9I53ArCh10egdc31o3dyilBvETps-7af4y3Z9Kbl62uca6FVqWSUUAl4qSOBoos0Rf3eblKfY_HYHErjebRcxGc07WS1cnjdf4DLvGgyLkzb3Yxxe1RF7nSbA6ZsY9ZL1ckfwDLkdgItybDjcQGEL0ERYZUIkK0eqwVY9Rncd0KwgQOg8tcBogpc5Gtp8ME0u80VPkxS9WNTDFWEsItwiG7hR4uz9C_Fxv7p-yp--JuRHnH7MGiC_pjjwXL3fs0aN9M9NwrL7QQQe0OnhMKwWJbmkqlWPc51EdCEgkReJB4PAC8RqKDM9sqpd7VUbotb5Z4kwhZUbtVpaagpF2GbGCrmaejg1u7Ggbmzoo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنگاه که افراسیاب با سپاه توران به مرزهای ایران تاخت، سیاوش، شاهزاده جوان ایران، داوطلب شد تا در برابر او بایستد
🔹
نبرد آغاز شد؛ اما آنچه پس از میدان جنگ رخ داد، بیش از یک پیروزی یا شکست ساده بود. تصمیمی گرفته شد که سیاوش را در برابر خواست پدرش قرار داد و راه زندگی او را برای همیشه تغییر داد.
🔹
این نخستین گام از سرگذشتی است که به یکی از تلخ‌ترین و ماندگارترین روایت‌های شاهنامه می‌رسد.
📖
روایتی از شاهنامه فردوسی
این داستان ادامه دارد...
@akhbar_sob</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/690993" target="_blank">📅 20:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690992">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfFQ1ga9Uq7IHlHlw-vjI29AUq3L2cast31NBZqtoTRVDlhwL_nitfeph4LMxJn8iVbVuek_oOywa6fqvIjznQCc0KZDxUbu3W-6a6gcCdYdU9ggeB4faq58YJ0fwGwbwK7oXw_L8O5BYVGIJYcvQ2bTXuJ9qoThgnJfQfc5kQ0oqlJDTxWGEDpicXTulkxOTopjofQKlDLVYUlSQ_grtUOXVzn0CwS9GncFi94bVNhPisBtFENqLTAAyT3FSm7P2k-5MBn8pK54IRMHAKN2IvqbXUaT4JaKqXccEcat4V5r3yqiDSRE0GkIF97yLfCuGVCrdm9gK66kiGascKuAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادداشت کمتردیده‌شده‌ی رهبر شهید انقلاب خطاب به جانبازان جنایت وحشیانه پیجری
بسم الله الرّحمن الرّحیم
عزیزان من!
از امتحان الهی سربلند بیرون آمدید.
صبر و استقامت شما یکی از برترین جهادهاست.
شفا و عافیت و عاقبت‌بخیری شما را از خداوند متعال مسألت میکنم.
سیّدعلی خامنه‌ای
۹ مهر ۱۴۰۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/690992" target="_blank">📅 20:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690991">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: کارزارهای نفوذ با هوش مصنوعی در ایران، چین و اسرائیل
🔹
شرکت‌هایی در ایران، چین و اسرائیل از مدل‌های هوش مصنوعی منبع‌باز چینی مانند DeepSeek برای ایجاد شبکه‌های حساب جعلی و انتشار هماهنگ محتوای سیاسی در شبکه‌های اجتماعی استفاده کرده‌اند؛ طبق این گزارش، کارزار منتسب به ایران با حدود ۸۰ هزار دنبال‌کننده در نیمه نخست ۲۰۲۶، نگران‌کننده‌ترین مورد توصیف شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/690991" target="_blank">📅 20:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690990">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63097770d9.mp4?token=AMJ-0OtwHrBC-sTyUf53_kaBZVunezfs6JNpbyhKPnlwuSuQzTW5FkhNyaEjNU49IUkg6BCshTJzGZQiS31054zI5X0FsVi8DyqsOfLhOBPn8rjubBI0_X9om2wgoRzZckxk27SUJONdIdMjQZh1chZPMglJzQx2RxzhMi2q8kMza3o7q-o3Ct765ss352tJgx9q6E0MKL0YcH8DBGiGGvpnG1tIFMgSRKagI3S8xa_u-y3CULuXPQ9GUnRo0BAOr7VUbcE9ov1aACpcV_nAyHI3sppVBafQPeWj1TFBq4_e1p8wG21Nd7IWU4T8dOJxxwTXykh1vXqrWaETDtCJww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63097770d9.mp4?token=AMJ-0OtwHrBC-sTyUf53_kaBZVunezfs6JNpbyhKPnlwuSuQzTW5FkhNyaEjNU49IUkg6BCshTJzGZQiS31054zI5X0FsVi8DyqsOfLhOBPn8rjubBI0_X9om2wgoRzZckxk27SUJONdIdMjQZh1chZPMglJzQx2RxzhMi2q8kMza3o7q-o3Ct765ss352tJgx9q6E0MKL0YcH8DBGiGGvpnG1tIFMgSRKagI3S8xa_u-y3CULuXPQ9GUnRo0BAOr7VUbcE9ov1aACpcV_nAyHI3sppVBafQPeWj1TFBq4_e1p8wG21Nd7IWU4T8dOJxxwTXykh1vXqrWaETDtCJww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از شکوه حضور مردم در رزمایش بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/690990" target="_blank">📅 20:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690989">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی سنتکام: از زمان از سرگیری محاصره دریایی ایران، مسیر ۱۰۵ کشتی تجاری را تغییر داده‌ایم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/690989" target="_blank">📅 20:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690988">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e096ac356d.mp4?token=tckhzq45rkHRhd3hxCsqvof_xyXLdX45YgqXq52hko-_L6IAA_qWG4RJ2wZ5FVINEJXz1BISe96c3SIhJI-LC8VXn1spBJVYPM5nk5hD_ZWm7ct510csbJEXjBzvs-XUJ3ipCFh-p9-CxxGfftQvfSfffd-Uz9pOBYbj1CoztpL2RqXc26lirnFZqxVUjWPjIb8HIQvw_trwJ2T2mzxMDRj0aR9X8ZkoZEWEzF8ec7C1EPBT997tvWXnEigm2BlxFu-esIY6AlhoaP3jwSx2xz2IXA6LcFmtBnb_bFJ7WGaf1V4nUuUv4wa8r-SpzMZuCPZ5QnSuxUBY_TuvDAB4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e096ac356d.mp4?token=tckhzq45rkHRhd3hxCsqvof_xyXLdX45YgqXq52hko-_L6IAA_qWG4RJ2wZ5FVINEJXz1BISe96c3SIhJI-LC8VXn1spBJVYPM5nk5hD_ZWm7ct510csbJEXjBzvs-XUJ3ipCFh-p9-CxxGfftQvfSfffd-Uz9pOBYbj1CoztpL2RqXc26lirnFZqxVUjWPjIb8HIQvw_trwJ2T2mzxMDRj0aR9X8ZkoZEWEzF8ec7C1EPBT997tvWXnEigm2BlxFu-esIY6AlhoaP3jwSx2xz2IXA6LcFmtBnb_bFJ7WGaf1V4nUuUv4wa8r-SpzMZuCPZ5QnSuxUBY_TuvDAB4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: ایران شرورترین کشور جهان است، خیلی سال است، ۴۷ سال نه، ۵۲ سال!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/690988" target="_blank">📅 20:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690987">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
اسامی شرکت‌های هواپیمایی ایرانی که امروز در فهرست تحریم وزارت خزانه‌داری آمریکا قرار گرفتند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/690987" target="_blank">📅 20:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690981">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ty347jXroadQGFQB2b1MpCpfI2jvfhuwaYLTEM6tEsH0zV6AV_xfqiZVUQrV2uc-lxPr7TNk81JMtxhX0Q04spYZ11usHviX5umFZCvNTgPM3l-hssgf8KnkUMuG72Xrc2ze9QlWEOij_V4cxxziorMpK_d3agKbTuzHEz7aJC15GUAPGZ0ZmpHu7W9T5MBhwzL8VeyWZa-7z9fRoa2BNLQziC3nvH6fMb0tUnPu5SYfJe9HEaWyX1IXZYKkfJs_499O5Zu9yz7g0advPWgaNRnwWDnXP6pGhESs7VY3Gv5qw1wOoXTEjVBrj_V3j47QwZZ9g4pupNt2oXFyKIrQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GkWNvmcfl8hzaH1ukYV0_6Lkei3lAJ5j76a0pA_F60cJM_O8WDRPzv2HE2kEsvQ40pSrqzIeHvHTmaopeG2otHD0xp4hVeRURLpYBdc-PdXPouyDS7pl6S__KFF4ao7bE3VAR0MxaHkwAnafd_diBjcXIPvBOchpTU5pT4imig5ITrLzVAJhE6ctAaLmR-NBVoOAPkNXlCUGCH8CjeVkFm8VNCqltdpYHUyZWFMzZCPUwAtn3W--5hUbnXwLlRiv0V9vbCXozsMLZIqcKfFgoGwaCrvacFTtSE0ZiE9ZpfKVR2fmpHiwkdVU_Q8SpKtB6rpVKAE3w8alrZvtmI_Zqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNzZ0ESgDrqqYw_mnV38AE4xhvVdtmbwYGhubAw04Qw3zt5dIw60IGi8m1qg2m--ck4mfMAiI5Cu6V_42DKxG0-SbM2O-433Kz5dSlRr0jKsNMj1A5f46zUtDkGJjZgVKU3T94beOjkKKZPuBnXNsNoa1FFmZwUCGCXm5JMTqCgF3ZcBQZ4Yf8_LfzePzOBOwqDy5DLVcOFnWfjhlZnyxEsdtmLc-JFlOrp1NvlrIwSe8SmGNGvmKziPm-ND_7UkXMjMYYkpWQW8D2srlpJypzywxOz3N3J6Ud2lowMgQhfT_2y8M6JUABeqzPA1FKYBHm8Y6cf0su_gar99cwyUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6mT6vSnCuyBJANNdSgV8zb6JPDUwrl_4fOGiZOzAOK_HdrayM8BY0abrL_d1J1Cez_nv53PvvfhAEls9eCN5600BJMCokOdH69f2GefOp8GdtUyPpH611Q3AXTOGK5m0Q1t2hmsgu9ogU88FF8UuJKjhptczPsnX29z8UPL8rxBL2wcgo_AD4nYhcX4lEDHU-4lQVqqShb9Qo7_F3mMl0mf43aV3OraHzA5mqZWsXuBhTq2mgCGnazjvbwStAfpFa4kLR2bq-1Em-9Fe3A0y3EhhPXfsUUNcne9jWF9ZNc9DGadrixtkDCE1w2DwudbbdfvdTAj6755xTT5dK8v_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ja9jP1Mt9YWHn--9-8mmnrRJRjuEGf4qaIvxchu3Lc4rndAQ21Vq-2jGLohT9mPz-nxMmSiuppgKQG5Y7gfNWfhHsnJRtZaM57C7V4oQRFwi4Ci6TN4kKj0wAMA4stFUiAMRhMS2FRgN0wRWsji84Iy-Vp5PhnK73lZkwxVdjwZ5uptoK0hQlu5p_wdYNHWsK9gqj5D957lDJWkAg0GdWxb0l93fCuQFaOX5699FlfCw4bT39C_8NqxoENtSp0_-4gWEpOOGt-5NnAQvhtjejyD7K-0Ct1Y12CdH7xHRDnyW6D6Mqx7CYYeEpvELFUy8jhBujOYW_JBasSp3axwpVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیگه خرما رو ساده جلوی مهمون نزار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/690981" target="_blank">📅 20:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690980">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdw7DCuWa-EIu2ijSypHDgEMpQwyWfTcT9bn_5VIUVlf1vfdHJf6QbotaplvPIuYitdOiYjOHkNB1JnVLZD1hMWNYeEaeWZTMZ2sFLWEBxxAl7dJMg5a0ySqe8uZH14Iivrc2mB7CDLk_KbBzuoAGjI7VnDtXwoESXg7q2su1BCBIJVziq6G5awn-3h6vqG1rkS4fuLqH06BrKvsVUkRnl3JvmSS9QqCzUsRUIZGpz1c7haXbym-PNZrPOJ9cEnMBPsk0LtnPqm7ewVcnJ6-5lDii0rtDdZJxodNgZUwXGzDsdfabLG_DPs5otpfQSUfKvc6udnchltZv23YZmmLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احمد الشرع،رئيس جمهور سوریه درخواست عربستان سعودی برای اعزام جنگجویان سوری به یمن برای جنگ علیه انصارالله را رد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/690980" target="_blank">📅 20:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690978">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUMiOx93j5VQ42-6zgZEJnmtuXJAUmoHqfsGlotkMZoqTzWdybaiEJkjppQ6DcNX0WwzHAI_bDXpJXv_yWihpXW_bwhdZaav4f1Wxbj0swLfxhtx6AjslFXzMzJpYD5xMv3Xe1dAPSWbO912zBI5LCAQN2SYdFg5QAKT2TSZ0trRH41rHw0YuT6eIA2vulX2MKSezDKAOkG8j8H6qpEcnGxcCw2kDZq48wvSGFTVDAclgxV64SVlRfZbMuVr8y2LXrbz5VIQAjHpe5IjeF9Ld9XZNMxMPMcTecJzCz6MVTMdeFr9Ugm5ESqiSzJEZaHgMYrV85CQp3quDzPYQoNSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iquFqaLPjy2yCa7f8WIG7cea9Q2VnpWfsIDKr0JJhqEECxgUNwznL0IpIIKjMdq32acBmkcFOkx_DW3znWyuuSjw0k0j77SsBjMgCn_N91k_1_O5idLH4hVfIrll5c6Fie_5kY4dSoq4wJpjDNIVJMG7M0hBpRs7KZGrWHZIjmNx84FNViK9yPrFnKISnYNOntPZ9X5b5cdHSuJnyxaI76kHUlCNqWTIplzdagkI6C0Ye-Hvf5xUfGcakFmBqW8A01rpHYhpJJAQFDqJhYs6xWVBQccjfHxfol0Ch_J5AnrwYXzS6gG7jA92huB_THdHQuaEIdY03BajHM4zazWXrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم دو ماراتون در بوستان ولایت با تایید مجوز استانداری تهران برگزار شد
🔹
درحالی‌که از ظهر امروز تصاویری از همایش دوومیدانی در بوستان ولایت در فضای مجازی منتشر شد، پیگیری‌ها حاکی از آن است که این مجوز یک ماه قبل به درخواست اداره کل ورزش و جوانان استان تهران و با تایید استانداری تهران صادر شده است.
🔹
در سایت رسمی این رویداد نیز، «تهران کلاب» و «هیات دوومیدانی استان تهران» به عنوان برگزارکنندگان معرفی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/690978" target="_blank">📅 20:14 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
