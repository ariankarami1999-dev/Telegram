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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 15:21:00</div>
<hr>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWpJlySxe-p6wUyzWkeqQt-H-qAZ-wfJlNaKBZrNxzELT5GXTC0htjUyMO6erjuOInRu9Hf5KMSpo-lEUItZA2a5JCWQX7QA3hs-MffOrEdPC362AyK4CEuemBDKAN7YY7pUdY8_la0ABEqPZ5rxSKj421lq9pHlMZ3to35CBnIqCtyezbqeZpvZhA2gpkQmPJD9rcFwnFxGSfrTsmLRicz4jIbFVjdx0jCYblRbDPMDHdj7QAStXAYXtofNPFqWtLvMpEgy7VQT0GLy1eLbMIwFJr--jrJjVbbz-hF8q-CJrWGvJrfLUzFukUG9EapNLf_JMOXdQjJGd2m_TuuB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS1t23kUxwAsMK8wwApqJymzPYLmUKK_XCky0FJyr_6FWe2wdwCBsm8GKQnBdBatXYuH6OfkhcsEgionMa7aw0kIpSIPejZwhFuoeDNYfcSkLVWPVOpvXiedNpFC9Lrpl3LitlvBYD2EvaobpYcQH7dFUD-DPgzMpRHVqwg95A4ll54add8bNLn_OzcqqkmTo7NvObnJcLk1VEJyIb8srqCEdcTBKxA7WiMiHlogls-8akrC6FJjjBAsY5XhXwaERW9ZtjQbSaEEVjjs6vNhTgxYHYMulKuTiD1Cs6xb6pj0ny11lhPkymF5RQUwHj9-GaWEs1-7P6F6ePu3Bwffzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7XthsLGAbueYTke__O6EqA1OfNJX7qRRxRkneRRLeQd_t-Hmg_-8Fbvq5VUU-2cOHTmdWd0weaAvTBhOGM-p56BL8po1f93TN1Z0NbSmAC2EYoAUB7eOrFfGYwTyZ_q9FzNJhLkH_zZxqnq6TstEvrohjg3V_WUqHJDApDjuAmTNKucJCykPIQzCbC35ukmowrgCXTIkVehNoOcnrVpBdRzRiyYyFwQhYq_8K7jNsOMeHtZECvJsfPc6AyiZ_nCPszZCpVyeXBCasmjEpT6wTSwTK8quH4zzeHo23n7Ish3D4zPoP0Spvw9or1j1rHCKjrYSHJNYB07sS_9QubGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 9K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW0wuwx5wpxEj0qfFSrWPY--QIoL21plRkJs2TygsHFF2-btPN2dPlFPmIsbCO4QcdDhcOKqpcJGZcXhufTIrnF3VF9V75uNWeKQQKztADEPn5eaviv3anx86FIpzWmwcquvsQq4qJy1rI4YwUJA-1XU1n8-L2u8-TO208GFKs2k3GaT08sj1flILFN1kHDx_DSf-VObq5z8IeKasrvEtA7kzQrlALN3F-rjwH0WQy8hsbKu2xGl1nVBm_oAMLgUCiqxeC_DXafzYLFOSRaNCuRKZT0A-CuF0WIErBvkt9RixZ88I-ZGMT-RirIjDalpY1RqZ8wkTVvcssLdKglPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE363c-PA2y9UKG3dUH5jjMEJ6orFvpvBexFK0NCgGCywDzTw_rRJZA_VZ3y9v744rh6oBLgfgUBCJtJqecK_mZiSHayzH5VzpGfBmQFpLUR943g8vAOV-onwtWz7c6xlFL1fZmjmDXCCZgiINxyrezsKbVgd1xKQZc1GgIT0JbtOxwr6ccFTnWdUdEGoKR8F-8oOuB4-CgxzikxnRAoFc8v04SBwcYnOmy_JkuuBhpl7Rd_cn-F0e1X5rCoTrAYCoaqcvTjmTA74lGyvYacfrANYQgL5FFT40wA-Q7NkwSUjNAr-Gdal2LjXoKszZtzZaykDUa8Y2xxlC7NPJEizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81500">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MN0ynvJ0ZrGpfHovQOikn6BzjuJTAMWiCfh6Yn5L0CaU4FMBaQ6vmp1A4qPYD5rFqn_hX-ZVYki9PNk9fY82brJcPEb5HEt65TklyS0bPaDTqAe6JLDKxWTp3nZBGASY20E4ycNXr16UKLpfoMfyqM-fAK5IgAMCYyqpYopyvFv7uResIkfeZtoiZaiknu7m0eSjqBrWzOBjCQi3mAXV1cfvyqDp2rEYjYnU1u8OA_Av_hutDq66X1_Su4xuesFXONTujRwErXu__XjHVmkqpKB0Ty23fMep96ia2sj_CVPviJc9jNevzkNoSshEx8-M_L3ol6Ay65BxwqztEQfzmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81500" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4TxqELbn1yZTudPcl_0bQauzXYIuq-z9TY7iVlWlqTfFsVl3uz2lKxq0rjBIU_icKUYfhqmZAzEoWQMw608IGHP5yTNfLj73oYIt0qnS6111EG_Wp4dpMB91RVxuDG-7zzMKy8dGvfssyi6uexQFcJrwXPo8RaI72PQDIoWIO_gSYP-ddPHqQh2lYs9LOshDq1Y1ocNAImuA-a6Ke3Go7owlSH1Yen79Zj6vBMo1T5-ksTz6luuGdPJAWBZXL4ucS78d0pFDiIYqXP-ylHysrsTSsINob1ap3z-XlIukCV_PNm-1kTvL36XRB5pDZFQSMxcRipHPiCZiacLvMEcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_S1tdkov-vgrdF0PwsSiPD6b10MS1SAWTxqM95lNSZI_uo07LsCKmqHahGvk4dRVEEkgF1bEXK92PQIVpRHqYU0uJZGlcdQj_eIzgWVBvIYOSb923w_uqEAKr14OlClBrQX0sEAVonKoQ1XVGxJYkj8ekLjavnWAHY-B_Z_GCQatRhEajuIfQlACymTWrBIg00YeLKcdb0Klf9Q6Lg1voCAvuwChXWpd87XVJtKdwpznRn-CMZoUS6zuLoHAOQKbkN8hdqLccf0LAFnkZYxIPSBzqm36FeD6Nyb9ALxs8v2IKEsHjTYe7M-OL6r55q0HOnMHuFy8El2kVuS_AD-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEh_KJBC4szG40IKIan4LX_NC2lUfsgiTnxwl-bzr9xVjfbYQDF5uMTSaHkhRSST4iAzNPV-s-ckZ9jmyBgZITv7tANcdCYi0F-qi3OPfpK9xuroufnt26z5uC6swOH4f8pHF3-PpcqLLNum8cvjuBRqaBzS6OvfKVgIbnnv-wBGJnuCwvC0pieOfw22fNg0ekggWYzO-vDGpOGLyNWU6b-2CML6hG-ixedW1RbfVvGA3T70i7AN8KI9uAKjjzY5nNRYYnpPs3lD3m06Wh63ClrQgzIz_oz3aMNnZFPxw_se6Hh95tStTHkOQ7gh4jUIR_LRZz-LWb1QxhLHuQcIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OS4NoLKXN0FElnups2bdIwC9h3ipPj7Z35pUl6K_Mz7sqocTERXr33_dXM3GjnSEFCQDrxFimSY_HYNYy7dhJVBEQ81RgeuLNYYutFZtiJhalP3wlcI2DRXhCZ8j3y8P4KQFjtMotspZrme0UEZcnhJVBzs3UtyzNtCAiT5ZAVNEd9qydFcF9tBHdRIdEsgAOOyv3u0IY1sbRSAoaEOXZz_dKGAmVBuXhVhet-V6hzM20dRQCZ4A7vANOKFmhvz_VmGDz3JLnrDGGECvqhVPuB2q6fJRKrsRxdiU9vn_ofLRnXSfKInntTdq1K_sC3iUH7yGR7ocdjNYnSJOFva8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5iIF3bYOUlAuowQkNYrRfOR_2cbH_rGCrUDqOo89e5ZVrD48RCd6kXB9rGGTr0_-Ryvbfe4Yyg93mQrgRdkpDaBOI6a4VySkRVLN9n8pStx4rlStUSHvR47uQEopZK3Z7zOw2nrWooVVnaQIRS8fgGWuef7syDrL1f0eJOFwQ1H9knZAoIyDQwUZ4Pi4XmpoAyT6JXXwsrq4qO3y4i5yTd0D2TdjjY0eZFLU6IO3HtFF-5Gb6z9iijvHVhgy6bH6-SVaMIJ_rzprhREbR2n0dJOGUONI8ppAHPjFEzaj5LDVCSmnYGQiNEWKq56zojmXufCMStTsEEo2BHMerw-Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9U0rYXxupzSatkWGJTZgl1U_w74Z_zKsnkTDmlRiKE5X9O2MFiuy6Om5VN7bUco3Ox0h2V8AR1vlB1_FPfZqy0EDPvZcPhUwtV1kUan9GfeO_8a4KoqZ9RjsZsFKx_qXsZD0nO6-mZngh41G7zYQNhMuqUgv0-db1EJyupkEQZtxcoW_kEUxmX2E4Rv22gFvZmAGojDcWrSuIEGAximLtGE5g40DtdBTP-JfrvvIBO7UAStTrz-GIirSR58ZHzi3QPRr6ELPbrDwD-ANLuXcbGk32srv7_1yPnA8iuBpX5VjmhWjRTGfpy2vQ2cNMeByEvQLJsQcmamSZAD5wDeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ex4xeDy9KFymLtYsQQvMF23iouLOgazJvxUIM9rSlf-WzPRFU3SxspAHp2Le1Imak2zPDzSHN0en54-htazqDQyNAn14x5Kh0cCeQQaJxN3xgzTijkrdp1jIff9bTdE80WEHNpyHPSzOdv7X9ryHpRvEqQLwjcV3lyh_yEUhnD6wXpdAoWMZQ9_1xj2hyFcXbFbvyKnipbfNccu2ULXlcnKKX-kQqr4C7XiXaoAWP0G0pshaL7F4tX4vqW2KQSq1Tt5iLw9l_KqV5IJlSgnD2klgvDcnnBI-lGcJ078oJxetc49QR9TBIdOsUQYxfxGEIAYvu3FwXCbCj2IFpJYGQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTFgbSYKKiJlS-1CJkrwRDXa-2GdBrvRPA9-CttxOvaM9-OddMfa6rTGcRbEHWQGbu2m50RZcIScxY0IzMQ3FFHP6_Bo3KBITTZFANxQDCXqg2LJWnhLFZ4lLydP94qPMyTmkM40Sbs7Xa-01CPX5u380cFXLES9BkFnCJHyDi3vEwaIB8UwRiPDE3qUiwbZ-PLYadubWyVWaY0LzNWxTGeUY0Ynxafr82FlmpXWwNb92TNWhoao0OiWVEsBbch8hrQTKIRWg6tb7q8eMrELFeBaMJlk_6hgM_wX-EYoghxuVb8fcCyr1YJKa-glj-z26WIn_-kVyMOHkZs84OwlbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81484">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9YN_hmGSX9Cc7yG2CgvX0oDwd2I1H-SzxYyoqSvkfA53dOErDIhZfG2FnFYftwNZ0td2LwZVAzOO40agIZOb-rVzDlCrSnOhFucWFFlsL9u92ypSLTwQJK2dT7LIUT6Qwf5WG9F2B98cmyflL-oj90aKwN1eVCgOsb1X9SfeF-sQyr6qqan_RmD6VYkTKSZ6o7f1Wp3sDacmjLNPg-T5-UzgIhTJJvzWISejTklUkou-oJ6pLOjQa9mf-B3X2drmRyHeLy_o0SaDq4z8ydJaxrG1ShcZN0gRVQ-4eaqbYsxr4o-9PQBuchp6hMSoYrexzGSAmeLKWXTgV5m3E7Beg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81484" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ettxNK8QT2CjCMP_bI8ngqi77kmomXUboBqdAEkQqpWjuR4gl3dSxpEpuDLLnBQ_JMulx3Pen12Tijj2m8APIHmJtE8LpGreQwSrvs2rpFh0g2oyZmW4X8z13lgMHNWJtlaFAYysccjZ0xE_C9SqcXgcFlCqVHGOBCchrulgeXn16Gso4607xrB0oSGw0j5_q6F_i5HUye2pxfeQwdA01LKUVFB583TleQEpt63rRvKattcfuk6wyAGF-k-_qvwTNes4Z8o_lQrGO8w1--7_MH3dPj3HF12N2QfIQLYPK0hS0mpbg_EMNxtMNzkhRa27HdJRV9Xk4R6DyBI6-Lh7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEFbnnIhsI7HJEwylMtXqYyw_ulrWPSTZ8VMUk1DNsPNRzTKK-hQJWynNjD_dZ-l5wWbSJj3u6a9utAYM4Ot7j-wpf3pkDDSAVueYDt4SFb7CeYTuzEgwSjURV8GiUIx5R4P0mPJLfV0atGTHP6aYZTpYzkjLEea44t5sXMuovfikPYwQbhIw5kPddGLItoq1Zs-ijqSX0U0kNI9_HW0nbbBDEPXEQWorYPBR7eZJ7dB123jCgjCKCj45GBhKBWut8t9OiuSHB2XPvEB-eYuDskXHpMukC2J8zTI4R4xjt_CtMMtgWAJG-Exf_X5gstycn0yG-DleoqXkwEkV9xskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dubWpOIkBSl74X-Eve0rWRWiEAhaqK-BvY-Pzist3KM9LHTRmcJ266Ap0lgXX4FrbgLi6ZZZhxmIsFdoJbhVWCZDSMeaQ1d8gcFVeD27SCz0SqvN8v443eF7w0p_sPa-ztkssKcelXeDFMXxdQ2Xn4czWVQVfAFKifZ2uiffy6O7wpyhsba9MTs5aDqvap8t0ycwKoEo3w9TFL9eAuYpae9_JkK2b4qfIiPWsIvtlZE1U_GFwnRJ6gzmcbiNvgrnH1aIMzklZY0cva-p_wFdQNyqajbSOYtqXa1EQMkoCH6oFYvt1y1qFmr2zFVR3-6h4elGZbn2tbGKfd8GgLvnBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QchHlzNPFFkpnyc5TCvLD-YytlCe877g3AQmmbPnO0mAJ-1qiL64_5iuO2YT8TLwRRdN4a6kcFPHF40eh6bNOxYvzsyyH8Blq-c3ROd90Ldu5VGcJXyo6LFIlMO7dLUJCyabH7h5uBLPsgKNoEdw-G84HK0Wtyxx2DHxaSZT0wVeGdX7bSwDRRoP8SQ02Fl4trgdi1aJBrw4HgU1RwVg57qTVhcvsFlXFoO49S-tKpSfcp_TeIaWECwhBxL94Kbi0njfcNKXysHTpE7YexWtz4YSsDD5hkcEoum8kMZEWpnUD6kU_J07qf_1kW3vRm01U_KM5z3rLhvhnRRXuAoGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q21svDeXwUVomm1uJA8vTuwOoS6cpLIiKO2vGhjwa5Mi3wWaB7j2usJqfjDs8miKg73Wl5kE4okLbdULICbT2vs75iAwK-fA6wdXHAQEFj-Cf0y45GDsvyrSy_NC9_cjEVws57N9emcIT_UMKJj4nGOITtQW5dF7ePJzQb4X5bCdfCTryf2FwaTqYH35Dxp_YxX3aXWKF30Tz0_HXLZ6luG-wGVbF8x3WIiQCXqa8sh-YxwEwrk_i6zv-OeAfL-DSaX_ijl_YHv9LBf70bEfbBAk4ClqLIo8qv7n39y_bgFMT8rSs5EAqTgbgAvav_kvz6ztk91oG0QimGTIgtSxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUk7121KPfG_XHGeZVxAa2FDGqncB8TIclXG_4keBZmTpmQvdjW9UhDXe8L1vI4HS3hZHzQRKTFEMBym27RfMPOJaLIGLd74jX2Wt38rhyp16num5_MdYzKOH-8PfviKCYoKCwRNYtY0r0PWIsyyU_cKhPsDKVC8fAI9z4r-H5vRv_4cciWlCLpqCcrKsvFgC68HFPe0gcKBQy5zxYr5UgE3KWyap9A809EKUiQQEpjrNuIv224asEcgRz4WQOSsCSHr65ApBPYgDCRuaBNNii__5lW0wj1Lb_9lzsgMAaANFzksKiYyor_Euak7jJWdglAb2aHrU_CTeQBAczEQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llmKIYF5GcyNFHtBFh9K4SOOHvjzErgFFuB061d-1GpN6N_Zbh7jpN-EOXiAGe3DGSRd4l_PxeveRWsvXYHv0JLMXyh_Z_W0J6SKzwU31tp5t6EUx_enLMZWtwlK0V-FDpzjDV0TSCA0X6NChRidJJuZfYyndC7pLZl_glAFd8aTqs3gX6RsupQrX5lXzwSsqZRkFDxI3w3HCytGG4sq0DZFqTYRxf7KF7LhGNXlFDIQ13fnBODrXZuJUEJFjD0fyyEJ25OgBChBIeNsyEYAoZOWgAgtCEB9-_9fyLMekeZx5J4Xx-uMFlIXdQDayyOJK2rTDD0fhl3WuBGQHK33cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuzZcCv2F7poRMht36imynp6VojZCLTn6aTYAhSGY8l814yL45_c70NjWh5msSudUHdI6GEx9QkfoLEe82nHyM238QO3w-SCDwX9QlHQKabwwmQOoZRyk7WK1xLCgO79psSKR4Wmo4BeWVMsB3-FLEXLnLP8FBYyUWAcCw4AYF1GCRikZ8Id8cx7zA9xsUSfxK2HvO2sy04SfFW_GoTNYiLWWTSrcHseTY0H8F81NRFEeF682vcecz5EApCP_y2DXTd6MzM7IPTWip4gFV2NWSA-KdIbdjftCsYc1doSmBHgCXepKC4dpjbe0LBV8P-d_Aw2NsypqIXCFMKbUX5gKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gj-3dchFTR248c10yY1nDAmJyhFww4xVM9qqgQkrUZOZGllyqJiyC6fQb-eH5RYlR_YZTNsQACuU6jj2hn6Z3dvVWs9y1bjnbCyVrfss4HrKKosowZRK7HDq1f88Ll7GzRdxlXTCIAsqJwj9vSw8FY6hCBJ4lyI5-dOJt_6N3h9f4AOcY6A9HaZcMh4KekBIdXszVhb0UWfqAXpbJZzGm23GB4F4ZnA0QU7Rnf00uj1uVKHB6Pjmw3S3y-Pjpuaw51X-qb9SPpAgEI3X46egZAX_3jZtD7rswHoZBJnV1koaEtD_RHdHxQq432J2c8zl33ZDS5dKlIwnDnLzBFvD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDDZB1MlMu2tmpVwgmo21UpVflIcrcQaC1TZzfpilZsJac7qMZ9IfSFaw1JFyr0CjQI7bO_-ZzY6m9B6D7VqVzkBDB3NXR8yLjHNg7HPkGaHiTz2aYB0-qxweK90Whjb6HkPYB_KPD8EOeJZwHhI-vWqIh1gyCnH9OYRBgc4HrqBPLotYJ3_CQXRz3bxXkFOGqgisMBV_Pw1SHHeHRureL2AeFBebZOpDbwxHL7w_BZELR4TwUb7zuax6r30iiD2pblmqqEslYOP_s1y43eTZXDT12Bu4qC5Tk_9RsSpkKmYudJbWCtVNiGmSuEIiskdM3ryYaqH2_443rBPfrvSvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5-hNtx7_Lwf_cxQrIXknDgByspaX4eIha4gkg0Jmd1yit5IxpDf_W6QRBjo7wdu3wEf3M-XDlr7tEp5Swi3SIEpTWp86VzgSrTMbEPXPAgFxx2N5lN8W5-82t3ashWeo0-GCHlheNJXElxqXopaXWeKSdjDVUyFZLHQR1-JkLJeIz_5qFHZhk4dzCFHH8i8eW5N7daJfLBu1EzGg0avw1m3z-rb5jUJAhCv2Zn8yK7yDNkcdqz19Fk_0HxqfWKd0mhSEVxepvxyzVVcz6RZnSrIGrJBTGzHblMAEZJaA44bVgsbdKuP5ydu8BuxIORhrtFLj3E5LToHgUsllwvFHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lctvdY_6RktBj_ocC3h9C6bcRBlj2r36ea910SLKk47L6LttQzrhGThoF1XFZYFloIu2eKXKvLmKgGsPSHnDZVhKyNcAI6pU4Ozk8iX62WTdcfSrT-Tb9zr9Chgo-lLUF_LXJrzgvqqQtoqvPLcyVB5nHD9u47xNMb_EPiWWFRhF91DblwYXD4JbxwLrdrCgAwHifBlI_OA8ztZo31WXNXi1EfSJnX16rCdb3TyH7Fnup8KMoNBOcHuThpZp9sEyB1cgjE31tizT9_n36SHxYHa3OkVeJjTM7uP7Mi8RgSPsJym60Rub9R1EWDwbRaOTFbcpj6wFUDRIcU0ajGrCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtIgO4Ryv-qnXonuq9AL2p4UtGAVNJpP-0lJ4rm6EQ9It8Vl8m4dpSXEfRwS9hhs_W121I2QBiVDk-MHk4r4Qzik5jB7ZpTMVJN5fFODjFIqsi5_OglAtFubqJLE-WjRbdS_H6g7DyhiB3G0XTxUM2eVDsLlp_wi4Vg6ZOJuFFAsg6cJY2Hat2rTxGyidXO04gQtsoIHyuHvq1drk799F13SCYByUVzVmuli3hQ3EZqYX8NiWRqWMzXd-5-d3F_2mCbq3OWnL1Ortx7zSyY2sKpe3Y26cWLV_sJ0vd712S5qC7jBqbRgmyeqX3Oi6HvM8bZMAKSYEGpB-qQ4tVBodQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBMwcR9Y0J_dtfXTmP8pbeWPDxhAz8trK-88iqlJAaLe-PxS8r2bYNsnVQNVZq2_2FmIijV1kOvBk0vIO-ZNlZnoqMsPZQFVUleOx66mtIxgu1HVijU4AkguIdWD3m_iodjqhgmgm8qQdNzwqgrRRSReUr2H9ahKj8I3GlH1ED40YirwUHtpugg48OFaHI_3FwXx0_BazIhKao77_HgRZzU0T1KIgWVfFXY89Y3kWAGSXcu80ofPJyhsVa5woKMZrJnUv-Lb3EwJjg3R4xt9YVRgPBH5c0zfjYHxC9Jfx_Yg1xP2aJgLULuGTHtNBeEk26DM1r2ieppJRgV97cfujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1viU-73-M7BP7euNkzD2eqcZKfkkBBcST2T7ZZTs7NSgvRM8qWqtsJSbmJ_Y-PAoTjHk3phhJuprkKGy391xAwPPKkvhAerfJAzjOgMAWW452WLkM-z5J3n-nVsndf3XmglnrebK4eVbY1h-JfVsJHRw6d1gvdXT_bp-qc1QwxMON2nBXSrR5SaezMjSR_dvrP7vEYZgOJq_eApNb4PUil5kEZbNj07C0LZLo36QNEVuI-knD_kNe6uRp6NwLiFCtphSSO-4q4M0ik7Y3AYhgnGCF53B2dzBXJ7rNy9xJa37joQtj4E-WWTmBx1YY-iIOpJdKUFPxvIsUlkdTJjxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5AJINM6cmleZ2QXHDw90mrzVLhu2UQ6NWglobB7wFHkGGlER122rS6RCubXNkdidbuZJMNsW8JKpw1sb9om7gFbL70ikH_iCLVjmMIwsUBWpveXDpwEsW0U8oClPt0jNiHyU4U3fro9SHKVkViEmuQZFtsrhary9wIIGGGEikerWgRBdlqRC8Iyudlrc7K1KbE0Q7TSrct7aGnFxg6pOtLvGXx3Lx4JHjXITyUgHgrwtHMvCG8gJOixDPN61I8EiHT2DwCsTcC7Mo8IrqU8d69exSyy3keOUKLETWog8iPmTJHkBaKm4Ci9CG54Tu4UtiGTuUg2IBdzU6YgG8zn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKxewBPfrZyGwny4KbRiZJfFc646WkKEy66eyU4IYSw9-ae4IEIdObtFx9RuUYW9sTnBT6bn-ePgERJrOTq_7XhdfOOGPr8M6chZxmov5vvT3cvtJMRGBpsNJnTIN0XaKtIw8QREamsaRuXIiRJKbIPqsurEQ0uFid0vh_PXSrfzVbFwRg3GPEvYFulkx-KXex1VDpBhaalhH6TyC3u1HybdC2UQmY8CQj6V1aJ6lx7tPS7fmGItX8V6JFK9OTvY7WinNGaTug2oaiSYopx2b5mqwSSlDyClmXPI-CAJRmNXDOIC5VlupVo9hCJI0rkVg9fakegajMr5HaF3ImGz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KHR08NS_6dCYa_rVvh8ljpka9Bw8GxmI-dHwTPYWCV6tPgNlmGxt8N3fzfe4sGYusPgpY4z4xTeZUu_Jx4OBha3nJHVYy8PMcnZJ-iKiV8Bv_a5x0B2sedK1FfDmZ3nrRF-aImhDL4VjkulEM9_RVAng8N2VlwEtnsM3496ooZsuXyx5L6vJzWwn_PZydIwQ2_qxqF9CK5c9SCmYT95RQi0w057PDFX-N_fWkIOLKZgwvpLUwon6zriztUJ2d4EjCLFYBeKTHU5fPdu65j9c5GyNJNsVoOl4kJcaeTNjoK9etT49QKj3zKWocBTj3lBmXKF2TQ6qzEXQh6Yqg6OAvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=U6_s3r0yVhvt97T5isedidubT6feNb33legfSqEH2VaqbwzWbwsYKZXe38p5v3zhKMYRDRvxud0e0kQVDJqZg2g2iCiemI9tWULUml58e68LJE7opakX6Pc9xySWeWS3rLrEWYBpoA-dDWO73ZNJZN3EJP0zIuP07QPVv4Gc7s4rDNNYPW1E_EllWFpTdV6GueUZYSasmt7cV8BMUuEqo3k9olti_Rnibj3JkOcCeNyNM6JZ2uRkm2v9tNKvzqh3AfdBmA7j00kpSH_spnjMNl5PJ8O7NlmBCfm5OhT4pNtCTVvmt1i6r5rsUNJqS3oCRo08VZMqu9nVlACpmm08wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=U6_s3r0yVhvt97T5isedidubT6feNb33legfSqEH2VaqbwzWbwsYKZXe38p5v3zhKMYRDRvxud0e0kQVDJqZg2g2iCiemI9tWULUml58e68LJE7opakX6Pc9xySWeWS3rLrEWYBpoA-dDWO73ZNJZN3EJP0zIuP07QPVv4Gc7s4rDNNYPW1E_EllWFpTdV6GueUZYSasmt7cV8BMUuEqo3k9olti_Rnibj3JkOcCeNyNM6JZ2uRkm2v9tNKvzqh3AfdBmA7j00kpSH_spnjMNl5PJ8O7NlmBCfm5OhT4pNtCTVvmt1i6r5rsUNJqS3oCRo08VZMqu9nVlACpmm08wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmkTZu5CQTi3UjTWCjoFVpzDB2kQTXgsLubidsf3J-2yfBmbff7LeSmixv077XbMuzg-fFp0a2_OyVkhc6QCRLDnw6jOttL0T5sxFqFdrrqKT3ZNcelFg6qQbkffo_IIQUcLECzTX8FlWyPOvKrC94Z93zvRdeNE6GSadeOHzMVYN9mUpM9oM6KMYdhRZLk2bKik9BzHHP4kmsjzj1FgDets9yq0-tvMh-Ja_M6Ud3ZaQ-7lkhIF03C8UXoKCnG7NqLAHQkJfZf2uwn9BGPOHQeyjNQvRDczU0v-qTwSoBObv8-tScB4uAIAhAdL-xKYL9LWIa4s0zzS94ekY11tKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6z3wE6B94Ii5SYtN7w4FDyLdHTG1GsGdszVmWu5Jfe92lmP-XmjdF4xrjibVi8DvdyIQbGeELR2Vc0hBRlgd31JJfy7z48KV6aEEFJbfnTwWiQoKNCIU9Jc0XhNfQo8r4sT8-C85mXmTlWh6czqr0YqscU_oK8OifVd_nyikfrTb93IdP7SkPR_EeD4sNGJtXuN5_PHH1FIN0HqoPxacy30SMQC-Pb9YDrSnQJYwQzlAyLNsOmEXoHmk5Q52GjmzlNMvlGLlEkovuyRhdcyRD97wnSnSU0yVnErUjsQy40yt77kmGxDLWvuTW1xkKRgkO5IofYrlXxoTHFMb5cDhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROvdfvuROa_Sk3ZWijkQSe_5mUkH5bX1ZLspkCYTUGIwJaJQpfZo6s8pJdzBm9D51WWbneil_7PDo6EELbfUVPBxXOmU0XdMlAr5Qxnoq1AssOkBebi-lTNCNn_Ld-TdoZrSJMSZ_8WgdH0aFWcVs-pCi7TnjBk52PFIthnYsbgzSU2zSRKGq5TTYLSEXB9EPnUBPJqb8FpE2i39aAd3yDEiu060Pb4Iw15MIWCrWuEK_tQCsQm96sIJxPUDja6s_ALtye59TY-zgHmi2w0GCW6LHdpLVpofA3WI-iN4F5GN_I3ba5SXeIWmDFmo-1QdmHr6ZKWUOgMJ6rjuIZkttg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csLlUe0iE00Dmn94yC0THgTq_aAt-wQsCtsjhT9nJcuoNPyLMAcGd5nQCwzAvERJQvSmNZx9kaAp5QDmXiRCfGsY5H0PlXqjGu-GdOqTVWkmZEzc3kV21tFK3A3TcjnhljPHqDRbEEtSKZ0uFVF7kxCptd2hwGwsRvxreNEYdL1p4Dgy0eqrpk1JlOVuOX62mpcofRD95JddCWj3EDWFl49dF_FVaVHugl7IELpB5ok4OUEz6wmG0EtLxQYqBfXwsU3OdXyXCOMQFCbOftqT9BBNbmVzC8ZPEn6epGCWA09CxZ-qmuyKSY10MZF9ahU08ua1rnvhrPizGig9a-jrjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSSgqDOZ4JKWQ-MdXh7dYtDf8iZ48f7TDfeD_zPuuMRonWIMEU02m9GJ6N4CfJkcZ53O1QumgNmGiPqz-EMSqsUXxYtXBkmKGKwzDJEDz2IwRUHQeJOXj654QPUXglfaV25nDC1PqKMpkp6j_FfrEUBPgb1OzXc476KZLvfvHH6tc4itUT28i3AwmGJ3gzgi8vwtE2XmWKmVJaoH4fZNo-WF4MHD3fw7z64gy1FkbGoWWTb0jTgLWXVeHipDAgAVhICk1olhm1Fb8R9snJw3oc3pAH9NRYmq5sHdA6yqNKhXlLBwhVDjQjiEpcyT9CsVoTS6mwW_b6cVz-7inWU3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcuBTzRhzvgLFAgMISAkh_inHpRmiBpHVM0Ma7HzsYg0UFXfQgTOHwueDOaXonbnmqKiQgf8KS-ER8PqIkh402hoaYriyuG2S5DZXHxR2ityNzxjqcoGl3NWR4SMEUxdMxVozIU7Uc7iY3rocsyfWEzKJo3WxaUvR8aC7XJn9LcR_RIHzjZPNtSNFDxGD2XB3PJDC86n_PcaGvFsOkM9Aq1gcNCAqTJ_HtQiLZNwyxPuoXwPeJg0DHNfr2FUNFWgj9ibTN-7r83gatZT0VbAoyVXT4x4JrIHVzLKZjjwiFQO_lRUUbdS6HLwaPa7EGbwAb_fWnm1UPsmWDPbhBO87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGBQ5dWCyyd5iqry3pRXMw9NZzEN6kJa__N3xjPLSOXCIwuP_lDhW2tk_H71_Ea0Vi8irDjJG_VEYKaheMu_mDGUKSMWvpNVxKTlByYB9OimGNlPgngckhmb1HapjoujRDhV6lIcB4NTk33A-siZLWEaW_74TfMSjVcIicMQT8t0klzOYKhwfUl2rEIfIxCUgqUBiZYCJFn8oGjgYlOg0T8tjHYaFyR-J_7TnW49oO2Wfci1ue8rmk1dVvI6naAjmiJjN4KnYwkgpnuD5xW9ibp3e6xcHRIFCeNqpU77nrXoiY17q_AA1lOknffvVrfjjGLiuwcDA9hqgD7FyWPuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA4TOnQ-VbMtN9KKdcF4NCvEoI3VaiT7NCuSHJpcWIA8fkkcKFN4h2Ej7MAV8GQmW7qreLdG-LhpBRlV_AeybzW3f0e8CgSw4MjrMyBri4Rhr6buQGiHyEhEA9Inch9c9ZQRjVHWwIlVKVMfV2XVSOrXGhAOF38RQtmajpIgsibxzKDWj1rla23LOpxNIgYS6zMjjC_CXJU90H6uTSYr65ePYDFD39ZdbDXfLuQbfOWaOqAkmlOZxAkmT4sFMShzu_7r-u0EDrBmBwOaMsjKxaTtJ0jRrfrsqojhYVXKGek0PcUiedGNUHt2hoYtaYjEAUcFhBtn4t9e5WpW8qbtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWVqOZDNfv7hyqbkv-VvU-pe9TX1f35PhXklz-vj9rDkpgFKd1_57YUCeRocxXQ_-XjtOVqOCmYHi2wpO5U52r4-t82OSSybIRIm0oqWX7Rnw9bhgrhb2u_B05Y6jTHSRHJqXD_OZSBGWchSzWrLBTKwUSEZPWx-QmwoqlBFXZFFMdM01ymrln7jLEkJXDAB6aOIOkn1LpxAgd72Bv8FnKaaqCPTTvsE0ZcmGTtxwmcwh2i6p0DOsn83Vw8cuuj03UzYHT07gE05KJ37aFCW7HkR6EaUA4cL2kAe-YhMU34OpUQWHMPYoFLICmU9EqZcPytdMuvwSWNx_46UeSSVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drWWqNabb4y8prCmPP0dfbZctyFrUq8E1TpU3Ffp4uUAmZX_kFXDZ8Fk0gsCobeN4uXiOiK7wbLzpJu27_R0jRM-n1o7XIhAbbwnGAn7MP4lEdW6J5aazOh00PLTLOQ23KDgZlyVynjNAXlOvK0SHfkw95M2VI1F2kjp8ix0RfXQCQnniUVtLXg813mzmzlXElsVGJiXXQKE5cIl7cthellye1nvAHU9U0AQPibmAXqbqHX6jpyq2DoCeZ2On14A0x2J_fffEBRoJzvZoMnqG-_6TsaC-L7c85v-hQbl9MsJRZoPqcNR80r5fE89qy_P32zOPdsmCvV4ypdqFOer2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzE2Y6KM2oUmQix06Lip-oRg0DipusT_gXlw5O--fQFCiFYMC7hqKFT_e2qfttLolLP-G0IqMEZj_jsnyiGR_Q_Ijuyy_okNVQBURoScgqgmvNsonOgV2I_KlL8n-j6gv08DyKTIxs7uoAelz3apFQ6POa7Be66EQqGxx6ZRkhiImDNJ7SFKZ-az-PVaY0qQDev6E7y3KESWtPLFQg6hiBHEsFT_FxUOuH-INubdEK4YMFp1a-uMk0zh1n2xkXcG6xZTeof791O5bViPQvRHKots7skXp9lijm-_m31l2WAQWyNJ2qbcBpfLoHmt1cyx6RB7Q8fOlGvE-tRY5oOIug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrUizKrl2BtXBANPbsH5F_LjBxirKtZOux38zINgttTH5CZiRsQObDhxCqjxWOUVYP-ARxLTsk0a5-PFrRCN_V6XUQKXrI3S_KW9fE-5gJTYpYcXTNXq0-Gmm2sRu5gv11uBR27kwaBCoYf1hrzt4UYiF4nF1flqjV_dVegyWKr_PNvqE9f7Tm28b5xFWRLoGcQQ--aXVlXvVJO8MJrEF141EyVIoCDgED-BNrPejHz28sOGGBPV_wvUa4gLIqFijxrjmkKootfuyYq7Ce6yy_DxhxuFpBIRminPAvVcZB5XFiuthDcCEGt0FPclbbD2RgSSM2obRc0OqIj4rkBr9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuhc9eG_FXrgRyQrB9W7YjGoHEVFV-T4xQjnOEHSvwT_yRB-OCdN3aYc3-aFYYy14rBqTTjOtRt6-d51QX9hcj6Oeg1OHlSdh7J3bm8IJDwnuc-9q94IHASbB-rT0X6SmMTbiSCDoU1f6NcEjZuAynI09dLM0WmVAJWtnxGhsJDZbHgQ-mqu7TqPiGwt7OukwRi6EjtekQafXHAgrkwct__Tw_I3f-_dzdCwWmbKUBiRcjn1O1YOrykj0Slrznm-nZJSZwalmCzdRXQGojCPAplqKuGULR9YPC4i8-di2pm-WBJTv48DviJeatjCRudmuI4qbjil5073pZNDhMVOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f171036de.mp4?token=JNKZtqvHuC1VtlTzfms1RinKqcTQZx-08uzN6URkTezPyYdAEs9zAvn0F94KPFbv_sWQy7xXb9DaHakIaUaL5FU6kWEkKKNzzCof51nVRcyUvwYDfA2Oj1p_F9QcXY6LWrUdXvs6vc-iQjaaKyfSiBiKQL1fL7Hu-LRz_rria19iB8l9ULAN1P5s2w0YO2ilm7BiE3aFDiczvAQDVE6f6LFO1YSUwCXR91G54_KPwqM9GH0-vjounEBmCyo2ruMFNBSp8S4VuUiE6HIQ8sRw2emkAPpVQLy2hZVX_Lw2eCdjSfyehkgyLM2l9W654u-b6JkIShBuQ35YOS6j7Tn8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f171036de.mp4?token=JNKZtqvHuC1VtlTzfms1RinKqcTQZx-08uzN6URkTezPyYdAEs9zAvn0F94KPFbv_sWQy7xXb9DaHakIaUaL5FU6kWEkKKNzzCof51nVRcyUvwYDfA2Oj1p_F9QcXY6LWrUdXvs6vc-iQjaaKyfSiBiKQL1fL7Hu-LRz_rria19iB8l9ULAN1P5s2w0YO2ilm7BiE3aFDiczvAQDVE6f6LFO1YSUwCXR91G54_KPwqM9GH0-vjounEBmCyo2ruMFNBSp8S4VuUiE6HIQ8sRw2emkAPpVQLy2hZVX_Lw2eCdjSfyehkgyLM2l9W654u-b6JkIShBuQ35YOS6j7Tn8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طقه پوبون رو زدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=ck3MIqCPh1qZ2mDrXy5mn0woJkhvYSHhN-XQOxcTVzzYuFKeGpfEnw9YeHYi1xoHezW9afhRH5fsgfSyOGpdQ7HAQ5YH3GL86ABFwtc9KhSG5a76OsnQJGc7Z9Ex4DLQw6aUo11DNnB7ZBA3gpOpkyWHaBiP7uvAoU1W9J4qKmqJRs2FAoYETiSk2Q1wckanEvMkRWMb7DubJQerJCaM0MSDEWRcg2BCTqct3Offzd-3A_msNu3wVMl7buJd2BkNv8rRloZxKdSrlY_qwjnF0UhH241C3N4SxDQ0_tGJvWVBzNw5AZFNQyhP4GhXpNHnJ6bJ5rEcPQGU6o2CWALs9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=ck3MIqCPh1qZ2mDrXy5mn0woJkhvYSHhN-XQOxcTVzzYuFKeGpfEnw9YeHYi1xoHezW9afhRH5fsgfSyOGpdQ7HAQ5YH3GL86ABFwtc9KhSG5a76OsnQJGc7Z9Ex4DLQw6aUo11DNnB7ZBA3gpOpkyWHaBiP7uvAoU1W9J4qKmqJRs2FAoYETiSk2Q1wckanEvMkRWMb7DubJQerJCaM0MSDEWRcg2BCTqct3Offzd-3A_msNu3wVMl7buJd2BkNv8rRloZxKdSrlY_qwjnF0UhH241C3N4SxDQ0_tGJvWVBzNw5AZFNQyhP4GhXpNHnJ6bJ5rEcPQGU6o2CWALs9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی کار قبلیت چی بوده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
