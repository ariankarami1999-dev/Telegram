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
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 16:59:30</div>
<hr>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFqv-2NJwU-MsfhWuq1wnbH3im9qq4mrv6JmlWSm_jKIB1OFaUdtKysCoLSUWdWurqO2GXFTnJxxYNaP5CMMZqzKNHh2OzOs6Mikt7tu2jdGAxqztjEicu5MAerqz2Lf08GTemXzg0v0mrGDrlbXm0TSrUW3IVKd368Er_OmVJOnU1WxmSmhTs2-teiOwtZlXO0w6tzPzk6i-DMux7w3Ehn4OTzpG_UljmbuXRkK6M2NO4o90c2sSn3JtrU3VaNVSbljottwufImorfTCyJk5gjKKIPuCM3bp0b1Jj4923NAARS08Q2crtvMnbE8UMcr-I6ZUPwML3AjTkVX2rYE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sykDJ4ItBp9wrUGLlocxt-fBq3oDvpeOAO2n6qHjtBEGi8EfeFnhIe1vMffpzHAJwIqEaDwCWqj00A07h9u8yqAp9nQkDc1M9RBrr5nU9Df5ExA7K3U4l8hNbLYHZl2Fu1WfSARWkQKyGfCWhUCqSFT47NJgHzL2_-4d_dEfOLp9vYRoysheKfZyYZUAMNDB5lO4dwJyU0Os82kUhBRmPaHWt2YHpLFazmkoPqUkppJpg1pekN2GO_x3jMajKuLQ1RUY5MBLtN8sXOMjfnjTHEbI1aGlmnmIAA1RlwSlFG5ci9No4ZHtExNVvZXhN6n20iZX1-x6lvnDhmGphRpIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGuidskOVLpNpUWDu5JMxRfhjt9loDq22EC44GwUkBfPi3v5GMBRU9na38y_vGSVaj8t2eCcfPzQY1jeZDrscToKgcYNLwnNfAbYbyl4x86D4ILW4OsfF8DJVmaQ3a-c-92NvnNozqX8OeGd8XV37ee3P5xe_49_mZ6nNHmS7151a-pqFsYG3KjqqBE3qfzYjReVbz1aeeeXhWx630j9qd1_4EB3qj0XEoAy22bA8T-rfVAYngWlpigqb42yMuzwvoVmUpLRsk1QH_TvvmkdCRaPfHqxnC1fy-jKu_QmAUFBiH4C5coK96555WMN4VXCy3SR-LPe4uwnbnT6UCMSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWpJlySxe-p6wUyzWkeqQt-H-qAZ-wfJlNaKBZrNxzELT5GXTC0htjUyMO6erjuOInRu9Hf5KMSpo-lEUItZA2a5JCWQX7QA3hs-MffOrEdPC362AyK4CEuemBDKAN7YY7pUdY8_la0ABEqPZ5rxSKj421lq9pHlMZ3to35CBnIqCtyezbqeZpvZhA2gpkQmPJD9rcFwnFxGSfrTsmLRicz4jIbFVjdx0jCYblRbDPMDHdj7QAStXAYXtofNPFqWtLvMpEgy7VQT0GLy1eLbMIwFJr--jrJjVbbz-hF8q-CJrWGvJrfLUzFukUG9EapNLf_JMOXdQjJGd2m_TuuB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS1t23kUxwAsMK8wwApqJymzPYLmUKK_XCky0FJyr_6FWe2wdwCBsm8GKQnBdBatXYuH6OfkhcsEgionMa7aw0kIpSIPejZwhFuoeDNYfcSkLVWPVOpvXiedNpFC9Lrpl3LitlvBYD2EvaobpYcQH7dFUD-DPgzMpRHVqwg95A4ll54add8bNLn_OzcqqkmTo7NvObnJcLk1VEJyIb8srqCEdcTBKxA7WiMiHlogls-8akrC6FJjjBAsY5XhXwaERW9ZtjQbSaEEVjjs6vNhTgxYHYMulKuTiD1Cs6xb6pj0ny11lhPkymF5RQUwHj9-GaWEs1-7P6F6ePu3Bwffzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7XthsLGAbueYTke__O6EqA1OfNJX7qRRxRkneRRLeQd_t-Hmg_-8Fbvq5VUU-2cOHTmdWd0weaAvTBhOGM-p56BL8po1f93TN1Z0NbSmAC2EYoAUB7eOrFfGYwTyZ_q9FzNJhLkH_zZxqnq6TstEvrohjg3V_WUqHJDApDjuAmTNKucJCykPIQzCbC35ukmowrgCXTIkVehNoOcnrVpBdRzRiyYyFwQhYq_8K7jNsOMeHtZECvJsfPc6AyiZ_nCPszZCpVyeXBCasmjEpT6wTSwTK8quH4zzeHo23n7Ish3D4zPoP0Spvw9or1j1rHCKjrYSHJNYB07sS_9QubGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW0wuwx5wpxEj0qfFSrWPY--QIoL21plRkJs2TygsHFF2-btPN2dPlFPmIsbCO4QcdDhcOKqpcJGZcXhufTIrnF3VF9V75uNWeKQQKztADEPn5eaviv3anx86FIpzWmwcquvsQq4qJy1rI4YwUJA-1XU1n8-L2u8-TO208GFKs2k3GaT08sj1flILFN1kHDx_DSf-VObq5z8IeKasrvEtA7kzQrlALN3F-rjwH0WQy8hsbKu2xGl1nVBm_oAMLgUCiqxeC_DXafzYLFOSRaNCuRKZT0A-CuF0WIErBvkt9RixZ88I-ZGMT-RirIjDalpY1RqZ8wkTVvcssLdKglPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=DpwqODK1NbVAx-IgvX7hQyESAS2GjMoT1uhqdyCCGcbL0BbzeCo6FF9b3SJDhMFhmIV7pVtycJM40dGyvOfBWo0Ap6n7zqFWxRBtxka-Qc9P2-5LWCrxQmITDEhkBmC9iHb3Hn3tiT3jglKu71YAmQdnSSRp6Aw-jk09LaVtQxP23rNa3CV9Ch3RwC9ko4OFI0H4fabi1zitSnoJRY0QPWhR1fqIXGICtBSzgxPehwzNls_ERMqsJrmtkS1qpMW1fCZW7vAHNx4Gih8nVy3vPhIc5BEwDG9va01cw9Gdc5QIfHYPhPKOPl4nJqRiVzst-U5tfFEXltpF0bFa_J4m-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=DpwqODK1NbVAx-IgvX7hQyESAS2GjMoT1uhqdyCCGcbL0BbzeCo6FF9b3SJDhMFhmIV7pVtycJM40dGyvOfBWo0Ap6n7zqFWxRBtxka-Qc9P2-5LWCrxQmITDEhkBmC9iHb3Hn3tiT3jglKu71YAmQdnSSRp6Aw-jk09LaVtQxP23rNa3CV9Ch3RwC9ko4OFI0H4fabi1zitSnoJRY0QPWhR1fqIXGICtBSzgxPehwzNls_ERMqsJrmtkS1qpMW1fCZW7vAHNx4Gih8nVy3vPhIc5BEwDG9va01cw9Gdc5QIfHYPhPKOPl4nJqRiVzst-U5tfFEXltpF0bFa_J4m-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpiXc5T4A7pbhZ7BPHNJ6ZWKAxVcafNg73EnEKUk6Z9mvPmfQ3c2h-B1HgblkTYGeB7avbRaWj38SMhR7hWqTzp8gjLvxtNSOQl60a-4nv37lbrn4LilU1PxZmL_BeUOHdPIg925s1rcCAYVjL4NFWoeZV5XF7rBGFPrnshK8QslRU3NWHEH1h4_NWwtQ8o-ITdhlk_5anaKUOd9G0aqij4dwZ5JQ-GtlMcXCeKZgtWsKs6F8ltcrT2bWNsd_eHjlvAkSTxSORgAbIAr1u84vVJOQNdsLKhE_vWdhYbYsfGML4Buu9BT990wRXoPXR1jTWTmHFUEXuEq2o6G_k5h5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81500">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uObDu7Jm6L4yWBz8A6t6LNCtTsHvcuHW2l6l2PklJ19O44kk1ydzljCM-pUCTFErD0r0AbsIkslbViumRtvcO0-fzRPL5KACXAxdWBomxWk1XEz1zLOI0aoSF32032tBMUUDi-6ahKg0gbI8Vkjx9nXpIT2RResU9m5qx0_ISAnnL8hfYtfm5Y6R2lXAdwEWfY9_phH23jJIFf812vluylLMfFkX1hihyBwnWMdxmYZZgy4rCBlThXiWS6fSjyZk9jJgKYZKBYUf21ypYPFRLh5OYyzEbxegvY4yuZNPvUJZzKhMduE9gPaiYpEbLw5vVzNFnfKN6kp4gnaeCBJ0ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81500" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPLtWZLZZpG6F-WTwTS10djegBPLxxckxKCet7IU3JNHUITyhEqxbVa-vOfswj_-7z9nu5m9Suqome3cer0_lXN7M4lhWzl5fs35vQLTFEhVGz8Ymqa3tadzLU9-Q3EaZV6uPsvK6_bBNS54vK6vler2BBn0t92Re6FJYFev_S5lPtXf61-nUeUtunyEYk85f1SL3Qglu5gfAd0CYxzYkGjbWeKyMHg5ONlkSqAH2uyFtVywfDGqCyv4t-4GHd4QwfFRZ1arokSnzHJLegjXlSe8u4i8ukHViFdB5WvO-bHLUXIKHW6tGwJbCiBUH3wVTuX_NU-HlRm66iKBAkCV6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBZk5_Bbu3V3UMFFrsXHoZXBt9MsJC1YsCory9rk6R8QiPSjj6tAi1GcVXoyat6PhYD_WabhPKQOuXAZEQRReFcpPJ3dPpP8uk33hb6tzR1yW5L4VziCKx0EHevbd91UMMBl-gEj60ssdfELqOx8o7IPPc_8tAqnhI6k9T6Df4YQ9cysQpWwlZc0poCaOp3OKZ76KIBckQ4jLCbjbCJbRY4RYpk__1aBO6NhlytW7bDar31Nuct4ufz1_4ix9ygSi-R0F5bZjar01EGpI3zilxLFenmuZ4PXm_jJ-db7MbML5SC9_qGrzNAeexkAW7QcnfSlJQUA2P2xh71keYsB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc9aFuU8f5idemiiDfxwp2Km8aWPKtkp8VWntjQpTAye5ag3DMbs_hkwnMsplWLTsV88ssP0GECYuGwEVLahDEcD0g0YB_wwLCBH6vdTkVIN3UjDpe2m9xOse4kQNQTCfFiYCw5qx6uTR2rc4QFGSsd2btW48eTE6gwSA6FJSryfdZ2tARkk36YDxf47ddO28couDSA2uSMQxYDa07hHR_bYG12Q5-q6N0-ygbZ2zOrdPA4vHiovyjvDJih4vYQhgk5x9QVBMuraOgbo-G-zdKBQzuFULUMEds_xcxl7AfqHZZXRXNZvCsHobchoQwus0rS_P49bcv8SNrGtKd934g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRyuv8qkVuESHsCuRc1Lwl7M25wH0PT5XqhptRtcqEHnT7JfJmiJMiTvol4PfPdeM0faOMzfHoGR7butr4dcZUx9MXFtJwBwNpWkbIXYoTN8TfeqhWrJFZZPPv7sXCJ9_ktgVmc-MGFFlUmM2PpAr8uo-AHNWiH4YhobxggNXLAG0X6Xvc-5QZQeXmBhAzc9HU31QRXDle6dMffmhjE-2FLLMNIsKyf2nXWqEq4DtCYJcTtszXhz1lhgX6oawFX11kiXB_kK6kH_tC3fM1xMcdH-x7bI4iVSuZHNF7wB89HsH3jUKvglYTHi06twFTgu3EU1GdlDaFp4-PHOnUgEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6bJdgolWdbSo6YeEDTetMJ9v3GvO9o9u-FYRHvXoJKy9o6kapam-lgK9x2ybIo-rumnYkkMw-HMnzLUo86sqKulkUpdyyY3KwS7P96c4ftasT3oaaCpypng0HuUK5tp8-BBbFnYobNlhUDmHsill7ML2jVzmFfLCTK66HokG6E1kbCDJD-8FMYSwU8esjEdCD2gV5sowKh_XDLzT-3m9pRG6KLiBKfDdMhTfqpezfND_9Mf-5RPbBVUYHc7m3-QwvjHudhKMq2-IOKUrSYyxR9iz0T6JAiYIJeymmcZ-FFThWObVIe3tmmQlI2B5iqj173pnmjnJsl9uXwFOaDvhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vb1oIj2SfG_EZIDiojGmDyVjXaRe_by4yE5sB_cFiWjrEErw9fBPKt1YmqpiVZrl-COTyTX_s790dfeD3qRNhemykeAHm-dLFPvOIh8lYJtISaN6S_EIKpeJ6IciPnQTCDakVDvUU2w6q7zC8gDFOwNM2AVIezrCAAW81TATmT3uWHFqeF5Jk0EXA68u7wJ9g7zjpRQ3F9cRIAy9bbnZrr1rpbMMvgPIqsr5VQPqH48o3ldcs0OAs04tkt3OFFL7iihRF9EeGu26rweSws4tsb1ex5Gr2YiCJmZJT47yeMaLTBfS6JSpkO_7GdDZDWDzoUH8U8eb2BTqC2Qmpa6l2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jz4nsAGp08Rg-Phmdc25JndO5u3VC04t_0V2Pw9RUPd7fh0M_1o8DeJcmED-oJPYtokLb7xCAP9SyYVZ0_xBVPSIwoAdGKsUjb_mVzGCxTiKydrfTMFdHrzID4u1cIQ-3sxhzQkJabg3SpZg15fA7EPFcbqiwK0WZ5TDRt2495GHNgShMyMawkiuWm9-1el6qRjWW0HizSwAA7I6vKlWHZVX7U2HVu9lXMNsAA3PdN20y41dlKwRapMNwq4WupgvM2WKwgVjU0hiPZftHl39lc38Vi5BSJFTyGMCbYtmZugHurIGrwAy7aPy5i7ESSKVoNuHSMyHWQElsIGNnokZxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyb8e_A_1_oQt5EPqQ2G-l1POG5ULuaXUM51xSje6L44IUWLle_5UkzAwymWQaUVlYijRApJnzgVYGvBSn8hwQIH_PvXqn9m1_SuuJLv-3GvBuiJMt6LxC5rPIdCG2te1HQYPFDdsSPMYYvu7Ju81fhCBWtogqTwr_e6EvXR_wWValmg0OSn2VhoPSfrKQL5evdMgaPO_dpvjhmGR9quvik0ZGAexPr0w0iSN2gGb6hDmERczfEd_OxwIlk-ZWadiorAmn0WQzZi3pWZNmMrkpKfUZcIAnc14QCfiQsHK0oUDusCvbgvWXIBcBhnsAkUmu7qdmj3OAWmLXfLKyfiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaLE8FPOUgmfFmkax6fe5Orpy_8PAs0AJWCohtZ1vL-Rh4ksupdXfd-pIJX1Ow00-3bg24sPPzuL0sdUMwZUahZZBm1fB_aqBeWodt5dLuqSVPyK5Bbjaz9mSK0mBAqPOswPMVJgi0VvKZ-1iDRjXuBUsWK-dx66Y4pidK7fTDOBgCKjW7tHWug-N7Hrz3uc3szHZhLjtzp9h5W8rpPPYViRVmT0inH_xkhHr5_YgUiePuAO7guBjdcxKpz37PcjPSy36A1ERvD6mqy-OihidiFVqI4FHk_4AaOb6Yifq8dJEBxfo4TdSag8XXw3d8ThWg34GkQL3WvEWLFAg25ugQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81484" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_yURIE-THhYIQ5HU8nwnvh9uvX12eW5Doe1lghHb2LMvh0jdaYA3cXsErwqlqh9sIkPglmYwSALyD4aAuCPWV90fuBl1GGKak-ca2pyxk3HacXschCN3T3RpyVgSaOQS-5fjx7bHEM9I6HVlZBmEiPl_eeaN_n2Zv6CDZu9XFMkad-UEh8PZbogPNpLizw6Wt15m9AXJap4AG-vdCy5h-fOGvbzTG8HnKkpHTrdtJ_TCGQC_mFOUoevlEe0ElHC-lG8Ue3uAVevknMYBz3WnNGN7wtAoE0MBEts6B6qk9K0ZAzIe6OlzCG70TnpriubQ83mx3LpUpET4Uo6ILvy3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqkSCKoBgwU6tARfHMh1JBzx0h21b0mGG8pNzAB47iWLgMhh6sRx_4kQwkS9-yAkowtAZGjh9q9qSkyNO-0W0viRj3kL9J4wB-bjBoD34OicKtvKqDZtl69qiTHVDAy2ZaD7MsD1GZo4K4M6tGBA709IgYngRroetSXLrvFikpqTJ6Bp5jczzCx5D6nJY79e-_EJL6eurlWrttaN0wxpq-HoAKdeOhZivQsPGir3UVxYFarhTZNMG951ZaviqF4489CmtMOgSXzQZe_lxCChJ5MZl4ce5rfBy-6TywNxV-5NXjcAS_aK9b_MV5WAf4d2LJRNwcmKC1eZa3Gnpjc2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWNtfM3CpZH4nm4Zf98lnOj6INppjZRIe4ytbH8KGUjTvr8g_Xx6R8BCxo20MZmjUDsjl8rCMYWPnVcEkMGHvbn1pIjB7Tka47oBs_XIuxJfOm8WH6TTNC89XENGEJsKZkj15X3Pcd8qvObYOmP6hCe1f_sTrxkGcutxQtXOxvol_Z_faArp-jLPALM_6ByqGV8f9-HhJOedG7pBB5-p53r_WC4GwR1GN1bcfxAf0rlpsZxWWusLg4xVSWOpYJIdzkfKvr1IS7b61BESAH565O6cBBs5gbzP499rxcB4u0S2c6PnsdTGOyZ_PITkMwCnlpoVZZobdPlNw1hWFiwwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCsGz2U9yXw7ISecB0j-Cvmp7sxu1-2c_xqvkZWwAaBw7P-7FvgEwrpl_t8DZNcQJHDAy1rJFSQ3jq5X5jIjWzhfK-5nlcOiYi-22yONCxar5i06I8kFD8Ywbj9_to1PT7JpgG0jvBEX0VHiFdG4h5aH8JQO4Pjn-BSDnTHQazuK_igsXPD4C8FUof2dDONUfu-4nkTF-qZJjQrCIhx5jUMkynIZDJptMzslBXN-Wp_D5TC5bF_r8MMJsLV8evooa3kMavSpsefZpCzuKeuF6XPSruxTr1pwZozr32LU-nPBMJOhurskePzWIgyiyEjflaTu6hd8Lt_euCoJISPd-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTF2qGsEWLjrZW82Ba1A1xElds9tRpAsKtXMuCL_nbK8RZN5HaNa-7BlrgGZMLL368rpf4E68TmkdVhqkuUg1FIHLyY6Zma712noyN2p7A9bMJ04gmv_4URyhdPHGGR-iqxh52JaACe2D_hGmFNEQQhwhkouPHanpk2EhAd8eLfo981B4MrVrzMqAajLyGiy73X5xmUwSsHQs54VV3UHpDDsd26RbthwVbkvkNGlHs0Q6zQw4kYs6tRgsImY3U2XZGOQuOCE2gTMboXWtYPEZjWTV68YepQe6d2P9VpXGrtQUEs_rT3FKMoOfj2LNLFiH1x3gwsEa6_ftmgvZbgQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knutnHcXMmi0NejAtrA-TXI0BvqUh65neiZYGorvAVeWiSHBwJJds2aoUV0gf6kALecDuNT3uMMm-8p3VMkYnERjTiRB7aZCbLny7D_Vrj40kWOrKa61jxzlCqfDw3Umue8m2qWkOtduxj-TsbYvwSQO4VXWmwINat2t3rzEitfu6nWmvBBm_QiMNhIYHQ3IjG9krlO7mOLJc9fmD1YgQPH4-vpdISqikm1Vpz3bm7VAPuxR2_MhGR5JllgfAaX6MvlTPo6HEtWKZDr8ic2QcYJQ-JD_sz0P1GuPMcoJdMX02V5hjfXmj8Yo4XIZ7aEd1Ctu0FCcSmzu1MKAzHXL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRMuhXfqZBgruHaLSWVHX4iCflBeRCHgRPeHZRCV7Rp0sqZ8VkX1komTnHfmtLqErFPxd5D1OBQFTeS-xh860l5pbb5fQpPl7ArOMlIg7JY1b7xyMyJ_bYjCheLgI1VsacVVU19B6ltJrySOO5dvelybpRcPuvxmQ71A1gwI1hFlWhzRfBqRIlg3hz_SIvZFreoh9pgZVwxKgc-ZfXXDumIF4eOmFAFF0uAgY3BQnwnwcW11qk7O0WEJBPuzKiRZT0319tuWJzfh1TkbBX9qK8wV7dlpd1tnwv_J5dwR3r8K2lrTFBPCFAKWWIIziB3a-ZCmpcOL2YqcZbOzFZMwbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZ6gB4gapBDU30DGy4BaEqnAcYBR5fLAtbSeakgjdFl1EnQVcGLLisa9Rp4KIO47C0ZORqELHAevmtJRqZuBtuesesZ7Dg998Hfy2zbtC7obaqTYLxiaoKwXMOHR_1gYkvLouA_Q74s-nrBpavKgp1THcCsXDOoVwC7H8h0-amJxEN18ERCBBjRTOTjzZ92aKGDNAheIBIrJ-vYTtseYYR7RNz2-kto8SLQLISML33GzgWcc-IpjqK162jl0aBvX4NWEE8RXFPccLUj-U4avNG-NLKdmuudzaStrs2jKHo9YwsMYnka3Mg6GOUlth5Kl0RB0DAbSUbASm6Z07TqzFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrTQEp7J2EWFpoDS9pH1aKzNgaRfZ-NB5vZsLd1CUxiw2n5-FBu5x_kCwDWw_K5n2SwZ0nsje10toFSzcJaNc--Q3gjwaBZGgda3e6_2FLjWbAEAv9_1qr2p6rn9n1Taq3sBVNMhc-EkEBYkctY_D4GKoHxyfpPtKYDEeoUcjLBzc5WnRGJmP_QVb5hgLAEdHYyHq-krWgLpSTeW9KO9fsQiuYIGzbhIGUYzKETzouVyRvT11gQ2oTEfSELcOOG6o58ajG7PCOyG3sg1BlQgJZi-oF-0Ch36hYTZxZE3RcMjw6_opG8N-K8dyhEibqHulH4mq4YpyNbUDg9cfoZ7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8EvcoklH8Ag6A4cImuD0p7A2z06e0ftnTluF7MOfc0_jNOOvyLmH2I0mhYkE1ZDbXFCpCTjSVNLLDECHw-I6BUdgqqrJA5oBg8lAG8hS35JVXJXZQT7MRAnI2zvKLJJ6dl4uYNN_fCgP4h1HdcEeGndg3JJLzJYWChHKrFZxUZqXWS9YnlXhf6AyG3cVu_nlQiunvoLR8TzVf5fMisJbCi8qdm_ISwzJohjiiAIyEGzEKv0egywvDITan1WJtQW3t708J43u1NX5NuwHILhiWTD7Dvrm1o5v2lfAT0LbLTjhCaCXeB24O5BZWL4pDdmmobvV6hTZmmxP_hzwKqo4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CROerLAx0L3O4QxKBkLGiCs7v-VsfcUj8oVYxchM7WTxxLLghQ_1YPZdgnAVL6QikjuzFPnykImQ6Thw-eRRkl8-bgLk0F_zRBv13kqg6u-1cy7eWT6PEcKslIK3OswE7ZcLJusEbasRUbPRhPI4tCwifBiNm_Yz3cI8OQ69nQqhSufgxuzyINzQ-FuJTPBOwUQ_I5mBN6A84u6bt2cU0NVnntat5Y6zmJ4l6DXN_EE_tY8Gt2mwZtRk2qrffBXXub_i-2mxPl_3kifHObTBN8p0eDfJi29GXBQkPIVoW40yHRHV0sguJ1SkkZOBDbzlRclASvcuk9Kzw0OUGkbvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX2Ht2csvKpk27byGsCqOl-SSWvR8UxaitytfrhbTD4fMOSiRXL-XyXYvUuMs4drIi7PYvxm23pu7FO5IEJ68Gl9f-Z1TxJ3_SaY1EEhY4Qo_Obx5LDhrq0GYf7TMZiFLeuFqiBQqF0w74fQOnPtS-RiD5RK8_Y8CYqNA-btU31peiWo8DeMQy7tDzI02Iz2E313lscjMmOB5IGakjoJ009bqaZ1Tp_Znt0vC-_y8e7_mgCAIFwAZE-t4HCcaumvZHxURrpssJg7WMPfDJZ8fhGoq01MAUrl5jlH5dZSphXgYlK7Uth0euE2ZztHRDZClXz3RUuQ7HtjnVGs9CYN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4O0VDhOwmZIktwM-ENg6i-OOZwlNWCCVpFVj1nYGZV4ovFFkuFtAsaiVgimvSdfiWhsl6Jb0Og1RbbCED6kwNsLXf7UMxaJJyrQdNQL5fccOFn7Azy0KaXzHprpJnPAY6sRUgL0icDKel-Tl1L9coqqJUVIqnD9xrjZCahQTr-ynhQy1fKdGDllrLGcQ0E3rFevaDfA4nMixK8dOHnISVdHNkiUAKe1v-2QiE0t55S-4yj_rPEATtEaqOQsF5tueHvCL6Z_s2hYSXVyDpd0ILZIZW6TNvRMyk5-qchDZcgCe2QWE9O67woT_xRXImVXvCJ245czGCvMBJfn7g_l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4G2-BIgbq-5jgGRNvAwIhaVtUG50LC7L0gc4WnLX1yHG2wX8TJ52jpAp0Z3bZS_Cjt517Jr92dcMd5wSntmnCQ3k8OW255Q0w5eY9WZes7sTdAGSLyiLA9kz8ngbcDZyddfhva-U43l_vcABybqsCv0sU0GCsF_5V8S5OmbAzlGL8ZVE1a58HL_vdgU_EhN00ZbQcsClVnOGGgiBFcjvdB795s9wlh0dJfdaREWPWOF3fMcJzvEUuDJ59c92gly6fo_saXq2MCpfDubaV1Y4dzZCWReNbH4xvZACDeapFDvF5DKgf2Vi9H3T6CylDyqFhuwhXpcT9c46XxqqwtStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7OdalAx7uS2pdVBKCHi4scsblxLefKXarSZgPZT_GHOYnA66FERzE1wXxn3FS-wNJ8V6MZyLPrkkWNK2nNwi4d8UsS8d6UrfJKOy1OSfsjPMYsoMmFQ3ah3qHSvW5krMquU91NcxYJIK_T4wf69iCFshl31GcZsJl80fbqugS6ZCO9Um1wx4mbXkhMPeNPOeo0zeJUhnKAg0uv0mBwIw6shDnIZMBdtdflIMwDeGacv8ulLzF7ir47KlrDTR_s_QywIi6D4v4ag0JfXFLdusgmTNqFIYbqQw1RvP_QYBQJcJ_57rALcMV3J2BVUr1xfX-0hrF2rSCEVBpNacWu6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFKu3dxsuIj08FqFdRE97UWyhRs7En8DUsZb2fVEGBpAs6RU6MZu3dndIr-RD6KswuzIuYqcxqgJWi95x9kZMF6rqCKocjccrfu7DONTw-HcLqKw_8oHS_qqF332K9HLUsRcpFdhQSmdHySevJxBhMobj1qDoNqwW-WHuztfTuOySu_zrDh1gl3QodI99POy2YmXMm8h67I5UFAiKdkMkmUeoXJdQ3bF47ntX-JWN6kNuI2U6dY9p3PQ-EW7qNcnmOdYZjBdnk8VeUntL5VR8UUcKm0MRGydRTT3CUDqki0YCzegzidBC5hrnum0bdNb8SL3ZejbrZsKCrBAJiQIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmIgkOUF8FqliC2GPIfzyn3M1JY6biwJx-tF07sZPA3jtCq-cWfttnQePHJsirlRVJXWBAdqIRjk0SwRHo5rsz1kzfs1wP_HChTSyDji2CUEz_-WNlMWo5Mkjr4q78tZjS_Yv668g5X8YTNNk91aQLvQ9d3aiGOaNc2SvrogTUtYqjWMGobJwdSzA-NJyGrD4UkZ7S5c7GUHGyXHcIESqbIAwuQ4Ixd1xno-ufgvBFxlp4aQiOJR8b6jz3O66btHoss3rE8bmIcx03GXO8VEz5b4HbvDMqL6-xfT4WzmzRQJbbrHyEhSV4x7DP0g6BeLoEWafVFhoVvLTe6CBa8Cew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYW89xxP51_Yxmcx9tqC93U4zJwk0qaAoHwEj4Qjrv1zwosAHXjMmYgGR0jHobHKL5C04EUoaF5y_2RQJgsLP9ybtfV_hi5XRCvYmuZougxN0eDdcKgIBEBgij8WlRKhoMYgLgCLvynBwjHxJj43ebPs3SzZ8jxrl9ub5Tw-Sjrer59gnOfZ1dVw5cs4MNmBhidpZIx1DEsmNZF5nmLy0Ksuca_5n2VQY-n_nGFBcLtvXki5_x7I413T5ipEM8cPy0nCijJfG3ZGpdm-XXwvhEQ1zTI7BXPTsBRp4lDjIbrNq09UguHBWMRpNIvfQ2jPy5xlCygDdZAvhbyw5NccNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=O11EeJ1umy9DSO19D64EcX5gmbHVhYWLms2sfDgHRAZ-B8t3z3nFpQ7depuVGXP6l1LtT_UAmR5ByWWulCJpGwjHYo1BUvEl0HWj0snGNWgrJUZDyd5NsMjZcpOjlvJ4ojS519HjoI2c9as87DwMogSOtkdzVgxh1kr-M5CKVq1npLF27RaZHKw0VWkiHhtFwoirvrdXXWvp5SnNf5pVDRL-HNuZO3AFCq0ZnzUhfcQ6-roEaJxkuJm1edh6z5ujB3ESeR5YGQfo9PUWx1FEWG9VKcqx2Xel9miTImNEKu0wZ72lV9PyFE2t7jOO4wWJ6hjsb4yuoonQnJ9gBeWtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=O11EeJ1umy9DSO19D64EcX5gmbHVhYWLms2sfDgHRAZ-B8t3z3nFpQ7depuVGXP6l1LtT_UAmR5ByWWulCJpGwjHYo1BUvEl0HWj0snGNWgrJUZDyd5NsMjZcpOjlvJ4ojS519HjoI2c9as87DwMogSOtkdzVgxh1kr-M5CKVq1npLF27RaZHKw0VWkiHhtFwoirvrdXXWvp5SnNf5pVDRL-HNuZO3AFCq0ZnzUhfcQ6-roEaJxkuJm1edh6z5ujB3ESeR5YGQfo9PUWx1FEWG9VKcqx2Xel9miTImNEKu0wZ72lV9PyFE2t7jOO4wWJ6hjsb4yuoonQnJ9gBeWtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdxcdrpwqfGiFgxcLF_g_jmZY8HaBxaoiTfoNwvQP-46JkHYePAOUBmam8ak-1dt6YxUTVZ5fzwUuKJX4ziEBY5yCxyFOxjmnSgP8nG8QARv6-IRdQ1BUE2aansZj0iGsmxrskBTfaeGXcOvEJWKAvF24QDvl96IC3J0kZ7unw5UOvxf3M6aWzgsJPJdfNBhsLjLMpRk4-mBI_IX1z4sedp2cGeaiqE-LUjowH5Lhs8MYfkfsDCDTt8bb4R7UYXfE2xrPzR8GyVXMSkD6rhlEsTEzGsw107NF-_CpG1Eyc1N-rDGfkYCQ8AtGKzjg8-oYes7An5t1iz8H08jlunT2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ncLcd_-sa-9H0X1VUpPVF88KIlNZLHXBWRkp65xRMPQYIE8RuOCe6nHOlWMC230c9rhgYFAFj3hSTVmBFcJvuuMAgSv-iezV24I1p-m7mLGOt8B_L9rQtaifNhMY8IAxaJHnq5abYpzs0VKq_KOiUgNtWbrNefYXNh8l_O4Nv05LYFfGTIxggycv_mCtndoR8TrX7F4gUl-pggOJfkQEdU-yp0BlLLz6FrrlRJeQMfpq84kjUHWiI7PsZqgELIwgQVPDNP60QQb1QxWfc-jvio5oywNbE1S8gA4DPn8piKYMqkbie6vZQmkT9TgefAppm2N-0zJVuKOdAnA5PJVDBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XD8uqINXiZN-rsmypTb7ubl2R4nEUPEHsq5gPwftyiU86J04xE4DnywOCZrmG9oWK1JXK2IWY7HIG8vZISgzeIO7KJB3nnsJpwzOy-buhDCbQ9Ztso5Ym02UVz3692aT3n19LUkofaPjaP9R7nKoBo2RM2et-oKH65qXpltq-OmQ9SjzyJLXFd5E_YTh0vFJZ-DtDueyqu2NyVB3pru99hAnfbwnr7LMH0MTnZofdnJw7VfwK46KhzLGHK23lPh_vKtYDZTXeBNdoJYRVuAFbhLTUNrmgLEWVl_P-8Y4loXHLNhtt-tk7N2am73gtnhGHt8Z7iuNUXXgdA_TbH7T0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxfVFtkqMNA58TQETkqqxfNX40VOp95LCA4RvOm2hrJVJcWN8T7F23Dzstb7JSppGOZa3ULRMonhbcI6ejoWq6y8oS8ZslU2h87XeaQLHwCZ9_6yZl6hggJKeuSB_ja-6eHsT2O9qCPNmC1WUtOgw40hqS87b7V7Yb2k6--EHsvU6a0xnUkr5VIOPPbRLMu8J9dEBCVVcVhVo-FsE91wCohNqjQ0rRC28cmKDw2FM2Zeqeu1m4uyCgv6Vlb6RSWS2K4sj7Ls4UORVpTM7ScsqO8huJdRWLQiqMgs3WLRILnZQYMlRA92HS00pU9SaKAVVFIO6Ih8mM-uW6pMg1WQTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dD0Pnq5d9t2R-PV8wNfPRhzN3Np8bFRO_CF2aQeeW1cXqndp5jtCEelryQggjl7HddejhXgmuk1SmCZiqtZikkmzRzVPXwYA3GTxIsGLh33dQbkpIEtiHhxOAnquIfsoB298lyhSeoR9C4xAU8cSlV1MXemVfiYuZwMx5w5Taqi7vxA1at-9QJyJAse1ehyoA2e5cpVxSeJuCm0U9czLMPHf4iI4JA4rJesOn1eoafF5laKHQ7Fm1ELEo5NwItiOGOvBTT2koDSQOi5eybhVo3Q5qRxQ4UCV2pg2hZuyeVyudWS6ZtaJk_EA34-EQ6yEHclCfPWwVopnQugDQ1tmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBPU7dF0JF8NXzuPX-mL92jNI2BLma6gRgo5WDtnzIrbFyfTKZN6pQQmlZwztFX9dys-ZtcZ4sk0uuCxDFFicd00hFSYUxorVZqodoD1ldRaWXu5qkZkzLI852K1luq45XQ5eJy6chqj7oY3JH4-sCcooMhdlUnj4juBDt8RyMQX7UF1JNTHd1XmiT7BkqmW6Qlq8oIIIDMy1DGQe0Q9FdlbA87FhucEnYgnjnjccbzh2W8K-MV2EGZF5gGrpptV_DfwQhyshRK2mrPP7Y_Weyo339426xSC-yaxGptagDcnCXlbiJZKei9929ksiBrwudHcy8o5Q2JFxHmUJ9cqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRyHnrFhvFAeaALQajKhZsyFSTn_O1nGhURFyE9C2R4aFgFL-5-kqgG5yZEYpzKJDXgbX9tXTljAMy1k9KKmQGL4hquGL11pAhIra2fzUPUZxcsOLHXoR8ZCOudyRWuCfH0YvgsasBMrP26Av3n6RvraV_60i4C8mxEFAUBJQumRt5UOY9IKd68dDiIHLMvBv9P7ViWDJ1brZFvfpJU-5tGFEM8kNJVaBGho9I0nGNW-bd148YJ6Y7IqNHtUR31gHqZWgDKKyGSvPCO1H-c31Swo782LGgalUrvm-LHRTNGMyHp24quk5gmC01Z5WLL9dqrwZFsgH2Th1_ufbj_vdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAAvaynARt9SiFkEAiRTafLIvBZ4AKPqsGdlObBDDgrJNum8Pd-3UCJspXYxUjvsprbMGhdVgr87p942B1cPdjRvVHGxaWRVJpqIYpQy1O0G-kilutwRkFJ8jvDV6uAHoOb7M1d2-LoiV-FjCTbKN_m3RP9MmRE4cRPXsn9hCFzqHcAPgezWSUQ4pI1Z1FVyEoJXTq8hjSmTuxhq_Mf8P0CqcTEL1SRoAIPVhBY8W055FYDF4pU6XmztrgdbF_9aIFBUpd5acvwSFo6RVqd5W3jc9BMpaRpp-QW7162FfINcEf_aSFK7slHvCzRJtwHt-zOsUnIZPdG7gBVq-yypgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5viCdv0LD_Q7-NdQ1UiKFonjSqqUzYE0Ix-6FBR2AXMp8hYB445MtE02cIU8mAeCOb3z2Wlq9tve9NhImx1nBA57cFvMrUOe_AljSpPmpHmWrhr8bZV4bGt55i-H74riGnYck69Cebd4QQdlxbmWvF7pgCI7O24nMKn_RkjVJtOBU0TmxlgnqZVmib6ZkUBjqm3xbNFrhIOJ3oKggBMFlTmL6N8TNSJthRDa-_W-3Wo-DFkHFcMhDoWokw8Hf7NFLSybzkH0NqRms2DhkFvF9cWXCUY788PJp1nZID_QLBGpn0UxoX1NFKOkvhwZU-ut0ZLX45VtExF3htgvsKZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKMjoMmACVizA7qjUkNDs3wKBglqyjFPMR23H1s-OTYm3J9i07MeMUf5oc5VQ7Do_D0EKEuEVCpM8Hn58Azyo2VEqfj9J6dlVYm3ogBzxRzLBei3eLB0yBG2VDxWnooYDQLNCBcbB4hpnyWDSlSc1LFyIDZWxu13lJNqnbez3c2_ZOkQbw7rpMCTzwrWkf61td46UFFhYnpPpcAGpITCK02tZ2RTjjKo0cKlSLrfe-ejHd9vuCv7f2i-tcuonAN0VPNlXQKrVeJ8u5DVTduCrkbX8CZcbomR0NNpVY4A9iE2utC3kmT1Fla2y_Z2qRYbwXJLnPFolJy9HY_hbNsZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
