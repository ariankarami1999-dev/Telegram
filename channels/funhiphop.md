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
<img src="https://cdn4.telesco.pe/file/n9iJPeezaSCVqPqH72PRo_RSHDKX6w9IhrFcY2Pr2yLf3GmMYpBjtIcUTtUYnfUJOGVPs7Lw8F4Zk8Utn-vXKLmgZr84bTP1CgsTeYK9IztmZI0a_ffAJyIUOpP-5tIhbzSj6gMsYWAtT8JX9F-5mqyvDU02mbtIx1ehzrQ94mPho09S24qWjZKS-3vg-CYeAcI3qzm3F2c7UnWR_JaWYuq-P3UCalT9X7V2u9WYe2C7GaR86f_yCFHP9RDyCJ4v4monxygSP5CC5XZ7SahfQYadFXxTZU1JWT1ut74_N5JhbIPqvGW2X_FuRN81m47YD3SV4Y34vrEWmbKYkxd2VA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 19:02:01</div>
<hr>

<div class="tg-post" id="msg-81542">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxOykL7OLvvKfb1fzms3DnDCwKA3Az2yiMfANyv6mAeJi-OwcQUUNoIrIQHOUc-wMb-mpuH--BU7HrFwMObc7k3-639VwmZuVaxy1aJ_5e3VzLPpx7Oanh3FlERLz7dUBX022z0nDp5m1kRaIItfMo0cAKSz6_NYgPOGjbmaXZbEeFHI55FqUnR7xC2WkNSGYN7bT_Ct3KrSucoDJ6e_FoM3H6fXTXV33NDp5Eg09uFkZsRz0MUH22oH55tTDG3NXk3BMQqPqx3h0PfxpLP2aULzv_bQ1fskM8nV48uOpgKB6nPcckr13xeoVqD49ZdLUm8qqOxfOHpqdADpxQnC2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلشیفته چقد ترسناک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/funhiphop/81542" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFqv-2NJwU-MsfhWuq1wnbH3im9qq4mrv6JmlWSm_jKIB1OFaUdtKysCoLSUWdWurqO2GXFTnJxxYNaP5CMMZqzKNHh2OzOs6Mikt7tu2jdGAxqztjEicu5MAerqz2Lf08GTemXzg0v0mrGDrlbXm0TSrUW3IVKd368Er_OmVJOnU1WxmSmhTs2-teiOwtZlXO0w6tzPzk6i-DMux7w3Ehn4OTzpG_UljmbuXRkK6M2NO4o90c2sSn3JtrU3VaNVSbljottwufImorfTCyJk5gjKKIPuCM3bp0b1Jj4923NAARS08Q2crtvMnbE8UMcr-I6ZUPwML3AjTkVX2rYE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sykDJ4ItBp9wrUGLlocxt-fBq3oDvpeOAO2n6qHjtBEGi8EfeFnhIe1vMffpzHAJwIqEaDwCWqj00A07h9u8yqAp9nQkDc1M9RBrr5nU9Df5ExA7K3U4l8hNbLYHZl2Fu1WfSARWkQKyGfCWhUCqSFT47NJgHzL2_-4d_dEfOLp9vYRoysheKfZyYZUAMNDB5lO4dwJyU0Os82kUhBRmPaHWt2YHpLFazmkoPqUkppJpg1pekN2GO_x3jMajKuLQ1RUY5MBLtN8sXOMjfnjTHEbI1aGlmnmIAA1RlwSlFG5ci9No4ZHtExNVvZXhN6n20iZX1-x6lvnDhmGphRpIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGuidskOVLpNpUWDu5JMxRfhjt9loDq22EC44GwUkBfPi3v5GMBRU9na38y_vGSVaj8t2eCcfPzQY1jeZDrscToKgcYNLwnNfAbYbyl4x86D4ILW4OsfF8DJVmaQ3a-c-92NvnNozqX8OeGd8XV37ee3P5xe_49_mZ6nNHmS7151a-pqFsYG3KjqqBE3qfzYjReVbz1aeeeXhWx630j9qd1_4EB3qj0XEoAy22bA8T-rfVAYngWlpigqb42yMuzwvoVmUpLRsk1QH_TvvmkdCRaPfHqxnC1fy-jKu_QmAUFBiH4C5coK96555WMN4VXCy3SR-LPe4uwnbnT6UCMSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWpJlySxe-p6wUyzWkeqQt-H-qAZ-wfJlNaKBZrNxzELT5GXTC0htjUyMO6erjuOInRu9Hf5KMSpo-lEUItZA2a5JCWQX7QA3hs-MffOrEdPC362AyK4CEuemBDKAN7YY7pUdY8_la0ABEqPZ5rxSKj421lq9pHlMZ3to35CBnIqCtyezbqeZpvZhA2gpkQmPJD9rcFwnFxGSfrTsmLRicz4jIbFVjdx0jCYblRbDPMDHdj7QAStXAYXtofNPFqWtLvMpEgy7VQT0GLy1eLbMIwFJr--jrJjVbbz-hF8q-CJrWGvJrfLUzFukUG9EapNLf_JMOXdQjJGd2m_TuuB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS1t23kUxwAsMK8wwApqJymzPYLmUKK_XCky0FJyr_6FWe2wdwCBsm8GKQnBdBatXYuH6OfkhcsEgionMa7aw0kIpSIPejZwhFuoeDNYfcSkLVWPVOpvXiedNpFC9Lrpl3LitlvBYD2EvaobpYcQH7dFUD-DPgzMpRHVqwg95A4ll54add8bNLn_OzcqqkmTo7NvObnJcLk1VEJyIb8srqCEdcTBKxA7WiMiHlogls-8akrC6FJjjBAsY5XhXwaERW9ZtjQbSaEEVjjs6vNhTgxYHYMulKuTiD1Cs6xb6pj0ny11lhPkymF5RQUwHj9-GaWEs1-7P6F6ePu3Bwffzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7XthsLGAbueYTke__O6EqA1OfNJX7qRRxRkneRRLeQd_t-Hmg_-8Fbvq5VUU-2cOHTmdWd0weaAvTBhOGM-p56BL8po1f93TN1Z0NbSmAC2EYoAUB7eOrFfGYwTyZ_q9FzNJhLkH_zZxqnq6TstEvrohjg3V_WUqHJDApDjuAmTNKucJCykPIQzCbC35ukmowrgCXTIkVehNoOcnrVpBdRzRiyYyFwQhYq_8K7jNsOMeHtZECvJsfPc6AyiZ_nCPszZCpVyeXBCasmjEpT6wTSwTK8quH4zzeHo23n7Ish3D4zPoP0Spvw9or1j1rHCKjrYSHJNYB07sS_9QubGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7zHFqk_Ub_EO65X0K-bk-pwuIHw2w2l0R-QfyPEfwcSUbGS_GuFg7PHBTcEBOCzZtSY017x058p8Qw0ZcD1n9GTgV7D073eZciBDORSSjyuf3nUpPOBsiYitYqjIg99GcSXSNGXzcBubHvYmTX6Q2evfH9ZdU0bpkI4J7-WiC0W8HePLJdhclobeM6E7fzagQM3uLHgKcMI1aRx4ARnTe3IH3aaVaDNV6-Fs9O-hDyPZrNhqoxqKISfJdSC06NOvSn3brTJamYHJE62RyPkMDwbaVnbNmqBnA8pnMXIctFmk_3pz7q_jTKsH44TxFoDm-RFXzq70U5MIEpNyP3mVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW0wuwx5wpxEj0qfFSrWPY--QIoL21plRkJs2TygsHFF2-btPN2dPlFPmIsbCO4QcdDhcOKqpcJGZcXhufTIrnF3VF9V75uNWeKQQKztADEPn5eaviv3anx86FIpzWmwcquvsQq4qJy1rI4YwUJA-1XU1n8-L2u8-TO208GFKs2k3GaT08sj1flILFN1kHDx_DSf-VObq5z8IeKasrvEtA7kzQrlALN3F-rjwH0WQy8hsbKu2xGl1nVBm_oAMLgUCiqxeC_DXafzYLFOSRaNCuRKZT0A-CuF0WIErBvkt9RixZ88I-ZGMT-RirIjDalpY1RqZ8wkTVvcssLdKglPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=G360l9NnA7kOt7mjmSCdMQS4fh9Py5TukuhVCHfkyhs3kF4VfuZzH1ssnJn20gE-xCT3ZUVvYm6bCXHOLlDdfMWpoQk0SQ7GW6V_Otg6_GVih__V_hNW3Ks1Aiy9iJ4gRFcOL-71pt1viVjYO3qtg53HCttzGvG1kitpxX2WJYLoGsH7rLojHLm5KBoPG5O37JdOWXcJxxkoQDeuMkf--865QrGq_n9mJB2kwol_e7vq5dOPT2CKd1wsEg836m86cnlBH3Iq66n7DFah-4DheM7BGIN5xKiQD2kqaX5rSPGfOPkVo2OESbw5M8jMjmaBTGRbUP7TYrXmKeSxIZNiNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=G360l9NnA7kOt7mjmSCdMQS4fh9Py5TukuhVCHfkyhs3kF4VfuZzH1ssnJn20gE-xCT3ZUVvYm6bCXHOLlDdfMWpoQk0SQ7GW6V_Otg6_GVih__V_hNW3Ks1Aiy9iJ4gRFcOL-71pt1viVjYO3qtg53HCttzGvG1kitpxX2WJYLoGsH7rLojHLm5KBoPG5O37JdOWXcJxxkoQDeuMkf--865QrGq_n9mJB2kwol_e7vq5dOPT2CKd1wsEg836m86cnlBH3Iq66n7DFah-4DheM7BGIN5xKiQD2kqaX5rSPGfOPkVo2OESbw5M8jMjmaBTGRbUP7TYrXmKeSxIZNiNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه شب گذشته هم:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=LowVGvI6_ZHloAx4xRm3rPxa9WjQY2fEcuJrEc7r9MFFmiWcvRJb6fxSiZ6HxX3gpWTJmqZb1PurLKqpT0b6kGNXZrpzO10cvxXy6A_d_zZ7DsNS3Jf3yEuU8l9uym3sznbiwuOTlJ0oM3N1DL3KQNBWy2vroJl2hrtVYmtzV2WC2DcHRT-VRvwb0KNTYiv56RTcdLek25sqSV0mv0NXgNq9SMU_iXFe-ndbZaBcAH2CW787sICnEd9SBciEbqiWSUwHWlPRB7_CJBlEq2PGuKiFTd6Gz6vKBbzopd8HpLhZiMw0NNt-v-e4fSjr0cx6yS4r8oTUdVvH_ycVqJAmrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=LowVGvI6_ZHloAx4xRm3rPxa9WjQY2fEcuJrEc7r9MFFmiWcvRJb6fxSiZ6HxX3gpWTJmqZb1PurLKqpT0b6kGNXZrpzO10cvxXy6A_d_zZ7DsNS3Jf3yEuU8l9uym3sznbiwuOTlJ0oM3N1DL3KQNBWy2vroJl2hrtVYmtzV2WC2DcHRT-VRvwb0KNTYiv56RTcdLek25sqSV0mv0NXgNq9SMU_iXFe-ndbZaBcAH2CW787sICnEd9SBciEbqiWSUwHWlPRB7_CJBlEq2PGuKiFTd6Gz6vKBbzopd8HpLhZiMw0NNt-v-e4fSjr0cx6yS4r8oTUdVvH_ycVqJAmrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVfgtSC7_Tr_ERzFRpNMz4Tw_RkJ2Wl9tip4JdNXdoE7FrF8pGo0_4P_I3NAxOUWCn-4KTuK3TfWCYnQxaSYT9U8GVYFTZlaL7-apr0CROkBl_Lq6AjAl4Px5h1Zqv-iCm-YrOqbl4-Y7DC_7gB8I-cFtkLxh8Zz_3VltrQHJeU1Rljrf0uC52_Zay2VRQUQwly91Lt6Sh7YDqdpK5ocmApqDYrqxGzpIiLrZbLQlleTGGNGQU6IGFA3u7gOK30R7yATCA8WuMJztfHCtc4wa61HrrDsHCu8kyOsFcc-geOSb2MgDB4dh51-D2cZtCezGpX-bpnbzOTaeYBDj2DbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81500">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvyRIN6waFTkN8UMYmpkXiDg10ThXZit-SvR2ZwLSZwIi5lKGQ38ZWDXb6p1mPp6Kr6dUg4QmWaNZATgLdgyonuU4a51206kLSmyL725OAEQ50v36g3SLZ1qk1FqmN5nZigKyetsakW0cooN3m0Y7-o_6_8bOOAALibqRcY_wlssK4diNUygwCNKDyg-mT4HHfDMW69izmo9v3fG9Yeo0OOEmKPwKCzX5TdE2kbfpPgAiyH9ijJHyJ4sUY57Uc_dkfciYM5k28mPR4GsSP2WayaoNhTbwiljAnHXJc5tw8X-f5r-VMzAMO98ZLRvMnsVgZHS5Ec4rfKvlZkfV1gmCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
با نایت موویز، دیگه سینما همیشه تو جیبته!
😍
دیگه نیازی نیست اشتراک بخری برای تماشا و دانلود فیلم و سریال!
🤖
تازه نایت موویز یه دستیار هوشمند هم داره که بهت فیلم و سریال معرفی میکنه :)
💵
با خرید اشتراک خداحافظی کن و به نایت موویز سلام کن
👇
❤️
🍿
@NightMoviezBot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81500" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAfz3Bmt2yeEBWIEDUZHJ7OloO6VVQfR-2Vpa2yjCykWpl0S4HSQRoHCFUCx0tiDlZhSCg_NtSZCUzKiPLg24UGBMQhqE4m8GgBmC3Odz9zaNrhNgA-DM1iQhWEgnee6QAsmsc425yOoKGAru0cSc33FsdCiuHq43azUNB_cjfb9M2Gpi-2pJCNyDVD_CQ2EQPPd8kwA98od1Ed0cRm-qpNn6LDtR_Vyijm5L4pFxt0d4D6zOsidbRwdbtclJ1j7yMpE4KPQCrB6IcD9M4qxu_ATPHCkjmqcJ0DGSYcCdb1yzq_4a5N0TVNc2-aePng0AEYNXS62iaaoRAOIQrAzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqRFLbxXcjAPj3pKzXhEsYpAaD4nrFKnpEqq7j9kWUqe7YEmkk2QW051r46nstfLDFmdQH4t7OZBDZ_8-OFS2XTP6HYnnbBg62r6lzNdC_pv0GEcbzj_Pt4V536ygnbJHxPKe2IDaLSabYPpOMHzh5DTEhHUwaHGXCu8igNkWQO-BQoWW-UssT2DZ4MpK9dDknElzFbHrzeeZj77h_bXA2bzO3n4Yf-DXq3Vog1fEKmqcorqZdbZReT5GfwMIKJvqBLpif_XuUd9FqcDK4S2-nJQNaDp73JYspix1YFbL9Fx1MR9Gtb395x6Dkjj2U-GXC9-XE0GuUdK5Y92QvYhXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkEUUqCnVVUqsnaOCGMz6qXt1PvbMpiNCssd1lrcgiUl-nLCIJlnj66GHrmB9_V3jFTqZz-ru9MvwjbkCHXxSb8xWALDBEggV-c388f6kf1Sk2PCOY_hHtXeQ2YL10Pyl-PW4x1PTm8ytXRIWbiEP7adTYhdlwkEknOv2ewqYROu-eVDWHypp5zK6SRVn0F_G5rxKow2S7WVRKMzytOymVEa_evg-k1KxXjnUTVerEKcZAfNe_aV1MeFF580x1jeCd5Xz8Ym72kc4ufTlskpbXxp55CErMY0FRIpIjWcz4id77RqJdj3XF6kUCBWZZEjn_z_wIvGrFuOUDwrhlzyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1tLMuqYq5C1uvsHGl6KhvZV18fSXjFJDKpecIwvJS1nFZNVeNk-xmT3a_-JwAxlb1pxmCKjuhupcCzi65HWTho67HkzUHnyMJpqEE-nFsXsQM2p0XkpRZjzfpJxUpTe4BukhA2py4vVmDDyLkMqZBKR3YvTZmwR48K7cVRKgsDvKq-Yw2uPkhL-CHS4BGD69IZ2th149N77PcXQmRgwBdx9EFagxnrKFAEhGLqzypkEaf4MpXCdOoBxQMHuQbCt69pFYnWTDJ7VuK-NM-WkuhvIgu3e8zha2KJZp4GMs6b_zJp2wlsbpX1TYWzMRCQ6o9P9twQaKADPFm62OyZLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQ7glW0qhr31YJ-inIjpyLJ7wtHSv2gk1UfZITExocKJfNvA0IaDyWcg5B-vK1Wxw0zvQrq93C-XxrCMW9ZqXJI_R3OMQTCybt_xCbByT_7McBklNQ3krfsZx_Yeom9xT9wktmcUa60jcEcckFG7PWmi3eMwwW4DbNiw2IAiWBsB87HLdyf9HKwTX7rlf4bin-57kqgEnJmoio5NaBGtbhOwvC4GaBy7PTmdeA5wKxfomCJE58e8yen6f3ZGNmJA74iOft7JHTi6S3br7BvlffEqII7jNLp1UU68UuFACq6iwnF3AmUvJJmoSgse5qsG4fKi4TGOL89hayHIzEXaFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwcPHT9i3pgJymDqKs0ZcP0bxQuR8eY2TTHfaUq2v8uUHS-KaMEuN8VSlNNLuv211eo9pp7h1AduLEzK0STOYUVf34Y-ITtz4g6WGMKngHUOs0p2srKmsaUZsj7Nct8PMiSVBIjseVcXB68skyPdeniM8NiJzphpPuUHCKR22AX_OBGiYdKRx0v097IpbYYKU7lXDbSi1akVCjCC2DDn3krQ9f_JxHl5D_kzqe_HOjQXb5IDdi14FjSDqBSetCaSJnsvrdQyYw0UnAAGwCCpab47jGvnAWN-QG7s90EMe-6LqT_mkd_Ia3sVaths-djBK7EcYCoN4nw3YYpA0mIuqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmmWhuGcFNy7FF8vINlUI1gv_hbwk39zEQbd6uSNEr0GwMml95sTK_rsaqUgWooLvlsf9Ii11LYgs9dcZ7IT_5eTWBhLvhZIRM3QO2lNpTM8fUlCqw6A9LLznjyzBLfOr01ZwvVXBulHBtI3_PSBubw2fyoKlDnM9wJ7dEi2ipsGUiCO6pUPH2of6hO_0_Dw5z6lk80V8qhkkkNQz1LAcJmf32BGVb-y795rTXa8JhwvPVoitTBFCv8wK1tbyxNGfpD_k464IpdDVUvZSrXKUjco4MuKoaDUq6EuNAPjJGlDOoDNfEIFeQTKv25NOdQcVOt9upI36NS5tGtZdSC8iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID0IpCNpiJdDS21f6mY5PXVfF4GOii8NLV4Y__4pl6KvfxrpjHscWvhRVuWwqMczD9xYWW62cPNdNgOPR4-WWGikJJfQ_KLeD4ALNiSw7PmsTJkEYDX1hcBkwC1fLmYht2NtCCGOR8oyaQktSi0Wiz58stY6G3IyiP-ngXKs0a2nDEtQtyg0qJ12izNwFr2iG-MQmm9NV6Fb-z92UTlxyCTgsQ-6jw6bTFXzPdbWVsjg0-eMfj5445k63PrPA_Zs77bQQkP1p4rw_rufDX7Nzc4dCgiUCoMo5ca8TuDrUte1lSSWzkWYlmIZo0ewM57I2xcqROQO96nhL_3G2izkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81484">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLPydbJ29FcTSKdiw7jdjUzk9wiVIeyrt8qLUKkT6ey_pOMiTrTrM7WHbktHi--PrenAbQmfGK7tvY094m5c2O5jg0Oe_pUhLUL--GNzHaygsjZIWR9UaNMQf86vxuV70NGaQznJpujhdoA7io9ArWabpe2gYIrDOF7F2FJih3RvXgHFMpcsTtSiwUByQF5ldCnF1mYj5yZITjJccGTQYxapCy3G09GsM4NprK-CmkjOvbqbenMQUnt3I2LbZ9MFga1RmADxkKAAbvBGWrx-vYPSd6b0v9h1gNXn-xyYp3daL7MGLn6QWLt1ddjHfi9R4wREwzwGM8IrSD9iEJx-Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81484" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_BSGhoYnQvrdmYfVEbip-tb1O741q_EmSzfV2vro36JjrnZlPUquQQcgC2qwmxW7H1ovoBbTvOWWW1EcepONaJmItSllVg7Kb9xSfIynIvZbL5Dl_XCQuJwASmovrd0J1ZK84Yt3xt_MTkHM28HQFrtDtpv6Z7m_7Y1YEcjbM5FdAMwI0bD0ogHfPLb30HwuvdgN7RwV53nkooECOMKNMbmm5VZ6o6G1-HIr_VYOPTHGbjjcFaCntVszG4orYAllrw0Intf3RthlEgHnpJ8LANNSZ33mQV5sC46LwcSfsrwEI4LOl8IAq1XG8rFoWphHLMfc_ZJcd-_UAg51RFeUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ_DTtmsoDG8sw7u4w3_1LwLkcBD_rTUF-UkwI-_JwtO3UNY-9uVRAVYCz5lYtJY-6V63iFulvRZ5EvF5I9R4oqyS0rnWq8awWI38_l02XXxez-5nKpFxzofhXrGqQ7MkkZMwD3yoNzCW8kY7N7qGOI30gMcPQNgXIjj2Hc7oxXAFDOJXYFRmIiA787ZptHSPmjRfz-SmOYTexbX44c1ZbP-nj-H4g6oG63SeBmUQbpBfPBrI2CjdYRy4CHuWpDmPbGUDiDMj6LtuFswFqj-WIfP8JK9AgajLrGht1Yf9X9FYM_1pyxWifmUiojqIeiGNN8rZQqylNJd_f-PpksTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E37K5BYIUIrCxVzIstJxYisUALNXtvPIsVX8btpUWUiHe-kcOlxgnvW1uYl7uslOe5ooRfZiwJ7fGTzgBBJ7fZeLvZPChhpqGQi21HBxpcas3yzI1lGLeD_Sbuq0LDW3FGC8y6B3WHQKt-DM9A6wckrd7zvOv_ZTU1RVV57tcpi5uQbfEoMDxrUz_l6c4ZqtqsyMwV5MAfd-WLOZrz7l0rJnYtRqVLwZBaXzVZbmoAs9qcQyhaSC3mLUFsQzlkznZ5V3kdBeVvA-di91FSvQvjBHMAmt7zaMLCwEZYTBvjsQAr8lyBtIyScEYl0lvd6N5RIahCejht0chy0C1OVEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9tSbgUcQgrUid01PnRNYxCatrDi8gSFENjh4lHkfKBGq50hFuhIVmrL41xdyzY1NR9Uu-3NOh3yTkEh21bYyXXpx828ETFFZXHOmtcw_hJAU49-EoxKetmjR_7q48gGMrFl8uC3bJA9YMNSWORSelmjcd52n1OKcooB2w5mHDQCl18eey2hXY5AQv9-QzOTJ8mOtid-lQpjkqW96vOTqUtmJdjzadYRgj7p4faG9YP2piNLN8Z4z3WzlPulSNx8Ml-BoKngAMQfwPN6rLOMxP2hHKOA6TpFlw_CKY_XPawAQgVoJfDFzxHp8ONu6jDKg6ZWK8QStg-5XGjMrvPFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx1nhJINdamgwj7rpbGIAD7p3FqN8IzXPlOCSbV4RXz3eKbsPiHXEPaoJbqZQGY28X4ju_hgb2OeDRJr73cuLX5VLLZZ_YPEjqTgN3A04Eznse1rnOcmgULxsl88phpOIDm3bV48k8rvosdKelRtyuMPE0qmHUWRtWfuqH5eYNIyoH0jT-cv7YFUQkrmAnPysAns7UD56B6SO7utR75cnYeTObDoMxVMyH0K3uD8nRrXAqIeKqFA4mNORP9Gw7hjDH0Q8BXOgyxmqPcfjLSEP6ipkVzq9Dy6yx0FM8s51NkUvRoD56qyjA0ldabG0N3hutr6gFMT2cbiDYJJil0O-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BS-KdACO1g6cb6UNJswlae-6BUw0mdzF7fpEX7VOAytIX4m11gqjWNfLYImlU2XTczj6HV4RAuRSKDvRl28n1cISooKGYtEeTAUxd8kkzlmNEI4tzZ9vqIYfBwxmRRdEX-VY8Nx9YP_jBMuj7ZVRkYd2oEgGCBvOhLUtFYm4KLmyL8atrtPxxpBMwXNpOHD8QPRD5CgZL8fqtCf4yW5FO0vOUcngK1e_TcigcLaIBuHCtPkAJnUMe28AN1LQkKBDp1VjdctFAPfhbq-Y7_5JA8366KAc90CiUBoq9Uo07F_NRY6BqeVLDM7YGZkwzkxBBm3pPf3Qv-npOJ12sidd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pei5U5fbsTYynFt4hPFe-Ii6fAaT1Msu7rquhJSMTOXabzjkAYztMlj-dQ1GlPy4yLPxNOHHerGXLjNN7LmuZ2kqYUtPeTH3cfuphi-D0G347ZNIzIXXuXEz_WwKnJtS1Svn3ecLlgH_VNm9zpAbmX4vbKNvNFNt7cxmkiTZNvW3_j_1zqT4u4ROTSq-ap8L-9xbC-Y_Ndqc-d-d_9RIusncspCKBmOesHlXGJ3eLp0Hxw_bOGnxPEMgT5ZWNHRA5WUHk2bbDH1wxV4YaTNsiAFR3dC_rBFG-sZBWjv8JjTiwJbonxgtvNteCSafWFSqM_maBp9b9PRWQ-T8AnMQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKfoS17JbWScZ7djPYZiP4jm-9Ql7LU9LPDEptZL-FiGuXf_BE2nIdFLEegoJPVREgC7QhFu_ZkuBwBrO2d0ZrNpUFKrNE5xqB4ttBcQ6sjIyWTaJRADdkuz89NRBjuzQZ80EeEq50vGciO_z2zQz7xAW5Z6dbeqgqXzTFrSBWFlRtzwnX0p1JPhhJulTJulZSqCZX6ga6yAq6Ma5yDx8c_KL2KUhrssTEfBdHvs6L6rIe2UEUdpDDhJkbflskQFuzrlXCtU7EVoamLujPVsalsP15EsSpAcLyDTgQ0H7qnHN1YSUWyJThwRDIv6YDlPrbz6s_qR-WxGYln17jc6dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPvFG5xF8qbHsqUeEEF1Y8oULeyyN0lr50FvaR2pfIj2cuo6iZtPYtC1wDLZ1MtzMQmbobs-trXjiFo65mcKjAkDlk_auqTagVBpyfC2NSqLh1qpANMf150AU6LR3-FujbZUtjyviAMDByykm59ADsZu61W4mBubpUYT1vB70iG1hZ4oNHJ0Y78wT1kKa73FC_m7lCSkLmCdMscZrHv9lcV-HZuNhuAh2j-L_2L4C6rEEu8vZxpC7Ws0m3TN38TMHGSTs53oqNhat8SpIWDDq8GT5cOl1eILHYnwmSeWMGOZ_cobadaGgR9kc-OZKX6pi3iiU88SNiqRdZDyzUsACA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbSRXE3bG1onjBHfKc7sTzGXO-0AQSNpC5rzwggf5MYoVinK_gA0IEmqyNB71UViLsMYBwCPg0ALqaItqRCaoPwa0P8DtusReeCd-CeQ7KsBasKZa_OKYPIjVGrGkP_Yan1XFzsAx27cF08YnO7LJfR22awSzeC-TBTIPP0J4bZL2C9Kn4OLfVZnO_r13E5OzJDDjoamOZ4spw9wyLuM4eKXbBYDPxqhKZDc9ZoeNB498BdAOZNaf-jYf-fZ7FFSYmaayBUYNh6kzjIBbIYCwoWF09EecX0vNyI6PsL3oNamndHaqMx2vGTe0Fuxt4V21aLzjaWvHKulSRjyzCvZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHbmnrWGsfkfKS4ukIZlFZ9gzKG9U71_ue6hcciXxKPWZqg3HmlGtNGLM6miW2zR4KSag8B7anGp9DW_xDIiFpxxa_xAnxL9PPr2anR7H2CM_qKiOgFLQdYZIgTrHGRod5TtZHE5j3LcNGrCiFsqr_zrnmgZx_pyyoaWvwl4YU5u8XsZvDCnO7TLAUDNmwOvbUO9nn80tuBGvQWsi4_oxXbHue1z4Tq8ze8MkcArqFF1390U2KkqO9JNGnuOuanPbLGivukChe11dJ1ftv8BzzifPwjXbug8AMkeT8Gvh4rnEsz50KG4ZCK3APn_hWDYlDfWBiwDMfaBBLpmnWug4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giBXh5LBm-QAVqG__VmU1UtS99V0uDQf26mDmt-LyA26riCj08OZbv9u-5Wnu--3XS3PQUSmsG25t4bcqu1kd5957X8qSiZlFzCY3Z5Sq80Jz71_niL-8E6G9Oq8_2x2sHVTyKv71A8VpZWGWJnTrUrXqMakXpLJRgwZZBT3AzPgKhGGOX-fSBhY7qj7YOF_njYwl10aCWbBWRTbq5pEqDAlgSk-mQTkRJ5Fy2IE7-n1olQ9wq871KpwQZNVrfjvukqOdSdR2GPn6YKMYHERGJF7epCA517DMfDEbxfQgHiJPb4baTerAzYwzXAHW362R9go1Qyq8B9mVymg59hDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4GFP3KHoLlIVRREe1bmmCyv42jO9TqB6GI7dyIEcAw3pVSPDEoujco8CdCNXAAH5IytZ5mj4eZuJmI1diRWsWsGwbO9j9xk3JYmfMVD43GTj_ukeDb2AmS_OUtyCNw6fO8ZpcSbw2l1flqBEnavbvdTPsoPpNTxFSyqL5if7HY_wuujX34qKOYPV2WhmjZhmkqIGnqaQBt4Mi99ES2G8RZyaGID6FyIlZ142HobINtpGwGIvEdOQgm_9xDREfi0mhKY5eR-3Ld9eX60-koTNuEc_DOZKD9XoafLaPPk7Ok3RKTQ2MKc-plllgj3cXApaf37rcfGHal6uFRPkzOWNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiicXBNdt1FXL2dmpKGfSJp3PGf_fndJjeVuCWoXYjtjX9tc0id-3KX6cqGt0Bz7x0rIPeVq8ZYFifNgE2S2epxFzPQygFHPV1bWV5iWqcQ2YaBKcEm6VkH0T1KVRKivhc8h5ln0XkuUqo3Pkty4X8nkg9dKTUzApxc254VZoKatAiazEVFm05HAiSs-JvMnZueJ34uNt35nd6G3F-rE0VugY_5MrKHGmTyo_PAN4C_o9twd3kZrMMtHEdb75eBKHNRsJjFZF5fDUt6utaNOoAUuWsg0rVbnWWGhdhJQILP_MFhlif7tq94Hu-H3-nA3oSTgrgkPb8budSSBZI_FiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5yD2fPWzd4Z6rK1XhhMcb0udtPGhKQdqOlmOuwp8L7VeUqpS3h0R2qx8ROgGT5bg2kBO27d6HT3HlauEBVrD4q2vkuyq2AuYWmi5nFp06F91b2fpM7rHu9vp63iOK0WnP7XgFZNEdBmHTqUN7Pbb1r28O20n-fBT8zmX-w5GKbZpE9qdGD0SUBGqi_DiCsrQx8cPdUIRm6LbA7xGTatCyKapHYHGCnWdR0hSZ8seAdLtXcEl-PwWt2SUKXWI8AZ28yQAESGdhn9bl0V5Ixx6z45MLUSZ3T_-icvVWwuzc3XoLOrzALrMPo-YcLA2dWoPToeE1AIr2CMsEU6YBR0Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVhhWSYFfu4CXTUeOEYCTbayT_I-ZsWnhq8ftCclx8YnjL_lUrblPUZBhmcURtoxk1szPKlXkaejhZwgkGYG1_3cOIi2l9xi4XI2HZmMr0qSmiV8yLSuqk1J78_goZ1hajjdG6h2C97GxxlyrN7Z1EScO7D6Em_40rVgD8UAkyUIgtvsCFd0PvZzziYcn2NzVb2VUBopyoLZ9moLVyWk0LkYzg0JbYX6GP8GQiykfCcddCXxQirnj2dDEY2R9k-6T5A8l6d5Oo1Et00cPJmHzP8UuFl2q39EmNOiOiYp4HCb2qTC0d-aLJiV0J8NWwSLLbnNt534kMwos-uoRp79Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن ویتوری موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر نامحدود 90 روزه - 45000 تومان
🟡
سرور 20g - کاربر نامحدود 90 روزه - 95000 تومان
🟡
سرور 30g - کاربر نامحدود 90 روزه - 135000 تومان
🟡
سرور 50g - کاربر نامحدود 90 روزه - 225000 تومان
🟡
سرور 80g - کاربر نامحدود 90 روزه - 360000 تومان
🟡
سرور 100g - کاربر نامحدود 90 روزه - 430000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHqpUCiQ5QThrdZ4cdkwSs9wjuLWcVgyrWh7os6wu9VmYG4Qk_TleIB-1huO2XZg7fCogqYqf8n2Y_NcHRGw8QkYxb3wCLqUR21Lp8saRV5EHwI3xLLiRh8LxTfFHsp6n4539y1KJGlZ7Yo887-xFi_-SWXaFkBEdLzu4B5y_jAwcfNJS83I_zdjp8r7VHpysPxpUdRAhPcglmc7qKcZtK4Mv9bICbyHVJzUWbaXBirZwaGohWJ5Y_3wB07FDoVhDQgw5DlWRYMmji__djLSX1es-deNFjjEJsGn-Q2K9mpTkWPyFD_Pc8ev0lNj-J4T0cNE7psQSQNYnWaRU6cPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOIaaqGqeyTZlh0Vrvv-UJDEqW-phXAYwqImn2bZIuLhmbzQ8JzSHERP6t7OOkPPOUuruF7Afbv__0qG4-83e8AeOe5PnOkOnYYT86AaeQ3UXCtWfNdeqDND8NhAXafXgVPRWoQAjYui3v3iZb79zEwIYKl6ndpK0cGGC0NdwX8BQLDCar4GXh6HI6fsvRJaJET7cZI7qLtg4pqGzbdBHVffb-5qAROx4vEKffgcV1Mc33GITXdU1D6a2QhZk-BuQvtB6YbqpRTbAw386PmFjZ2B5iDfRcjo61XywycaLLme9QagY1eOfoTld63EfJqBgEv64Z_2RSZ5C79-qhFIjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=Y4oWF392DRoQIXATA5xm2Jjc3YujW6trVIiSWtbyxRgquKJd5BtgUvr7zJeMP6yKEa1ZojlDrxdaSM-eBENlEEfgAPMZL8iYAkgC4lEylXqltsgwMxIz-6Z826dqWl7y_Y3_nDmi7mQV132Xn3jMmhBV9r8_dSNAtJBA7U1b6s9OyYub8DDuwOQr_KUGDSVZhH4PDqjvEOq_Sbi-s9tr7qSxoeevLWTzKD_iDe_UGgq1yXEUlLAVNdebOs7idPLJ0VFwakssU4tPF2BHrT_L4lkr8jYPV-U2G9MGC-zpS3Tss_BJ4d8sHBTrPXZaElqSZxwkFlXOGvEqk7tii1dfGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=Y4oWF392DRoQIXATA5xm2Jjc3YujW6trVIiSWtbyxRgquKJd5BtgUvr7zJeMP6yKEa1ZojlDrxdaSM-eBENlEEfgAPMZL8iYAkgC4lEylXqltsgwMxIz-6Z826dqWl7y_Y3_nDmi7mQV132Xn3jMmhBV9r8_dSNAtJBA7U1b6s9OyYub8DDuwOQr_KUGDSVZhH4PDqjvEOq_Sbi-s9tr7qSxoeevLWTzKD_iDe_UGgq1yXEUlLAVNdebOs7idPLJ0VFwakssU4tPF2BHrT_L4lkr8jYPV-U2G9MGC-zpS3Tss_BJ4d8sHBTrPXZaElqSZxwkFlXOGvEqk7tii1dfGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7NBn73bGyaxZanSYQl5R3vw7_Q17nPV7bh5c2rzT967EIntOdO7Neyg5kXVyis2XTRDS8kc8SaFxQ_dtSW3tED8HoyA1vZjLwe_Wm-CNpp90xhAkrc58Jnjtk_pFVWBBQF-wW9zNIHEyBqt15v5m0yOY0-csBMtfDBNk9eKDIg1mtRnmucz2PCVztLSaW44YvtFU-UjGQGcOujKgrLRLZQRhBkKdvtWN040Kx2y8rEe3KOOxwiTVpz2zg2wOuFktFRis2e5m0kB9tJ6uqTMgOk6zypaYOzMQ6SEdXFW1LUdNbF_Y5RRWirTYAM56rfFDx-6IIrTzwAqf2vQgjP70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EobvbhbXORE9xx0ulG4v0YR5WiJ_TVr_I6_KygAXyc6F7TohyoNSzC6M_wTOuwca_56Fuinxi8maZ8puNsBf39fsoxud82P5tZz12-suhaFKUfBn00XWKEMdsS86-wRwQygQs1HrHTGvNsnOfe_OnzDegVzxY9rcjkjplTwYIibgqlwhrMWc6Zv1JKsH4Wn2sgSh33duyUPPWsCVLa_wQoumWKCtmfHrjlx704qd6XfsdnI5lBZc_nO-gQm5X66oNXpmR-t3vw7HmifwYxx1Pr_qH5F8OvAE5yU-Z9HyIzVaB6Gl5GwrBNv0n0KR9cry1fp9GVAmPqKdK6LLxWUeNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S885_TNfui3Xtt4kIwCdaJCGvIdEV703aCLkfgpl0oKzJCmSNgabqgsYlOcRzZ0bzSPQoehjuadu8YCEj299H33XhpStgBQOl3Z3PVBTTSB7QEWfKOnl-oTIgUgIqs1w5dopEDmOFpWCP3-eb-At5RGnmbUMlb4LRBxKPB3fTztF6rwBBtuLKorC_e1cd5-LoJ3Mjc29vDKwwwXa2zFs5_S82bS91hKHLDyOgEgEM_newodpq7ijNzjwh0ajUZOVG9JH9y7nSoMy-avSQRVAjnCUorNEbht4DtvzDHzsjqrFMCz2U96WsAvVZ7jpUFzZSmligdkL4zVsp934H7GwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممممممم
😂
🤣
🤣
با هوش مصنوعی فیلم سوپر زن رونالدو رو  درست  کردن  اصلا ببینید پشماتون‌میریزه
🔞
یجوری داره میده انگار  ۲۰ ساله توی پورن هاب داره کار میکنه دهن سرویس
😂
😂
ویدئوش رو اپلود کردیم بات برید ببینید بدردتون میخوره اخر شبی
تماشای  ویدئو کامل
https://t.me/CONFINGMeliShkn_bot?start=3126b54d70f9</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPQshTadPimq6l3T3TXkO0kVOqJyDzZ_HfzWJnwrZs-uKGsQOeJ6hq7GwZxDnFdb-s_ppekatNWjG4Me280WTGgZhXwxhXTWG-nQzMZpxgmEjP_kCAXKQVNEHwXDUjCfsbZHn4GQBYrxyZNIPbywZl88J9vwnndW6lS5Jt_LaUspUtuUZw65ymkklTWgZ4dEECLwu1SH2xRrk0wZZyAkftGBIEz-rPnG6Fr_0NS5oCD0iMXrKVbqXI1c4zRc5rbx1QyaEmTv5jVInToJTAPW2KKsHDwAOEwosg5kQAu2gLvl_MO4dPdnJQK2NMJRcTbvTchJrT48hW3OmCyjs0risg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTx7vD23mnsvyx8hw90IWpLQCmlRwo5_4OihD-8bjlx_33HxhOamexOlwg5T-HQLCVOU7kur7kgw8yDIyleYuMIaiKLqgJVykI0sl-9EVEN9EpHw8P8fP24NBbHoc_fPLm9qDCmqf9WtZ0_Qt6uUBx4hnSmvfrVIZUcelOuugySEgN0bh8vZevS56NTYbmH7-8IoJH2O8zvRGWbseA2AFeXuVmZX-NNRZ9X_bCKJ_alCYYEuxZPM1VRqcUbgZhXg_Df9vv2CZKDNyUi-qztrotHtocaYoT_frJSGSu_jhR_6OqmQJWquBLSF74QlOdacEn_yhNyphaJi4UxsttoE_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq40ADG_E1z8qyiwmXvWo-_b_t1a9l8V4S5BLM9rV5LxBAKripboExzcPStT_9pxBFuecZf_M3iIUesWjCYKwBGmW_U0keFKH5N2aunVrA_tFM276xnPAHWXlFZLE3MMJmf-0gzvJWw34h97KMPTb6CyMS6Zxl3S9JdkI5KxdkMcKvyj346KkaUD2JksEBWcGaOYeJPSvdrj_JIfpgoTCWmeBPC9zPDTOg3TlwDp3uBXZpaGjWBAb7KCIlw96Z6-W_RT2UC365jIdHaW1_flKY9LqZJJhIpdcJqD_HaesVjiIGPcnukywKYUsxWPCXDpl2BXjssIYNqC3sJeHyMWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G40O-e4-cZGeiHvVMgEzacMw6_2K2kokBmJfM0n4ZaA5mdU8h2WuqTKCcf54PGYMom24HSxPuu5mVgKPBNpulzcg2dDWut4qw-CWtXV6jL-JbGhgDZY97XIiCzM47bS4asxol_Le45vLsJ_BqDD0YjeHHs55es5L-yD5DkMi84ZAM2yYXMnHh43rLfFNNeHZ-YGzOSpzwXZDkaNjBOtAxUpaWjX-qEpwz9VpVkoHm4Q-cDDVXhGB1E4mquJ9WNNM9qM7GX36hCLfG23asBGNUgx-HJs-aTbXTy6ySxb2USL1_i5uvVGYwAQEcDBXCcuRWwXU5t9EQsI0FMMfZCRU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFZeSnUrhFLOtDr6JWoj2eXptuT9jTCyOzsCVx6d5smDfVclNSVOAinyicJvNkL_f8XfV74cOFbRTZjP9xIKlu0Zkm_HMi4GDhAoC9PW1onHUfqaJETHcE5kiLPgFXat4dTcov10403TkMGibdq9SwVFbyuy8o7_guX2hWQOwpfPNha2HcN0DOPgDJMibkZoA9i4YLYt8S1BgIzrq34ozO_qM8DQEVMlOXA4bO_kAUgnKlCH4W-YKf193pYIBFYTnnwPXrj4s5kJL1iTg8610hRHMezwo7L8G8WwLeEnNtCNJmCKFCVJq9YYmLIp9726_B-c6HKLI-r9WP7dOY74mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXeCEeDJh7wF8ec2T5ZYF_wsrq1Ngrv3o9MMstOr21TaLLRNMixtt18afNX36Du_eyayfbY5Ku3lITLBPxtLgmfbZjOh4Kbrk350TBHLZke1cMUqQiQ0CoJFdNNBfJwkK_Sgmfl_OUtO7sf3fMIwdTX1b_xqsvF3We3cUt020WP18ZD2mKelAKkAU-NV4EtpmZv4Hhr-awK6vSHcZxuzO23cZpcGP1v5Ha7XV95ZS5IpeIYI-MQaP-JrOZfN1TR36OUuGIqAPegOU6qsxO60ssw3q7K2fiYnAEFdI4gZsh9_wNsBDBdNKLm9Edteqzka6-_6CqNfXakb3A53hZQNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1jTk6yazPr4D0rrF0ip_8ech9UCz9Dwpua3Qs42hQnA9lvochFCaPGn2lelZobQR8zfDXB2dIYAxB0BMsEhS9irClbrDdp2g9jPYORh9k_mfuKfE2-wfL9dc44r53hIX6B-Tfu32FPDK0vCKc8hYD3xhlOvvh4ZvsmonoOw_j9STQGcgiIz9rXcgksFwjSPqBRBPjDMNWdJVCPht8MSiDv86BK8gfFjRNs2VCNXvghwkxJTk4XppocDckGtgZ28vmnhmbaQar4AHvISAkGGTlVD77gQgN1EwIjLLuooLQ1_jt4X2WytbwB396He813Evf0bdwtJ1Y9u9pts4Ybnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
