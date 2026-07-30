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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 13:28:27</div>
<hr>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7XthsLGAbueYTke__O6EqA1OfNJX7qRRxRkneRRLeQd_t-Hmg_-8Fbvq5VUU-2cOHTmdWd0weaAvTBhOGM-p56BL8po1f93TN1Z0NbSmAC2EYoAUB7eOrFfGYwTyZ_q9FzNJhLkH_zZxqnq6TstEvrohjg3V_WUqHJDApDjuAmTNKucJCykPIQzCbC35ukmowrgCXTIkVehNoOcnrVpBdRzRiyYyFwQhYq_8K7jNsOMeHtZECvJsfPc6AyiZ_nCPszZCpVyeXBCasmjEpT6wTSwTK8quH4zzeHo23n7Ish3D4zPoP0Spvw9or1j1rHCKjrYSHJNYB07sS_9QubGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW0wuwx5wpxEj0qfFSrWPY--QIoL21plRkJs2TygsHFF2-btPN2dPlFPmIsbCO4QcdDhcOKqpcJGZcXhufTIrnF3VF9V75uNWeKQQKztADEPn5eaviv3anx86FIpzWmwcquvsQq4qJy1rI4YwUJA-1XU1n8-L2u8-TO208GFKs2k3GaT08sj1flILFN1kHDx_DSf-VObq5z8IeKasrvEtA7kzQrlALN3F-rjwH0WQy8hsbKu2xGl1nVBm_oAMLgUCiqxeC_DXafzYLFOSRaNCuRKZT0A-CuF0WIErBvkt9RixZ88I-ZGMT-RirIjDalpY1RqZ8wkTVvcssLdKglPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE363c-PA2y9UKG3dUH5jjMEJ6orFvpvBexFK0NCgGCywDzTw_rRJZA_VZ3y9v744rh6oBLgfgUBCJtJqecK_mZiSHayzH5VzpGfBmQFpLUR943g8vAOV-onwtWz7c6xlFL1fZmjmDXCCZgiINxyrezsKbVgd1xKQZc1GgIT0JbtOxwr6ccFTnWdUdEGoKR8F-8oOuB4-CgxzikxnRAoFc8v04SBwcYnOmy_JkuuBhpl7Rd_cn-F0e1X5rCoTrAYCoaqcvTjmTA74lGyvYacfrANYQgL5FFT40wA-Q7NkwSUjNAr-Gdal2LjXoKszZtzZaykDUa8Y2xxlC7NPJEizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81500">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81500" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4TxqELbn1yZTudPcl_0bQauzXYIuq-z9TY7iVlWlqTfFsVl3uz2lKxq0rjBIU_icKUYfhqmZAzEoWQMw608IGHP5yTNfLj73oYIt0qnS6111EG_Wp4dpMB91RVxuDG-7zzMKy8dGvfssyi6uexQFcJrwXPo8RaI72PQDIoWIO_gSYP-ddPHqQh2lYs9LOshDq1Y1ocNAImuA-a6Ke3Go7owlSH1Yen79Zj6vBMo1T5-ksTz6luuGdPJAWBZXL4ucS78d0pFDiIYqXP-ylHysrsTSsINob1ap3z-XlIukCV_PNm-1kTvL36XRB5pDZFQSMxcRipHPiCZiacLvMEcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_S1tdkov-vgrdF0PwsSiPD6b10MS1SAWTxqM95lNSZI_uo07LsCKmqHahGvk4dRVEEkgF1bEXK92PQIVpRHqYU0uJZGlcdQj_eIzgWVBvIYOSb923w_uqEAKr14OlClBrQX0sEAVonKoQ1XVGxJYkj8ekLjavnWAHY-B_Z_GCQatRhEajuIfQlACymTWrBIg00YeLKcdb0Klf9Q6Lg1voCAvuwChXWpd87XVJtKdwpznRn-CMZoUS6zuLoHAOQKbkN8hdqLccf0LAFnkZYxIPSBzqm36FeD6Nyb9ALxs8v2IKEsHjTYe7M-OL6r55q0HOnMHuFy8El2kVuS_AD-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEh_KJBC4szG40IKIan4LX_NC2lUfsgiTnxwl-bzr9xVjfbYQDF5uMTSaHkhRSST4iAzNPV-s-ckZ9jmyBgZITv7tANcdCYi0F-qi3OPfpK9xuroufnt26z5uC6swOH4f8pHF3-PpcqLLNum8cvjuBRqaBzS6OvfKVgIbnnv-wBGJnuCwvC0pieOfw22fNg0ekggWYzO-vDGpOGLyNWU6b-2CML6hG-ixedW1RbfVvGA3T70i7AN8KI9uAKjjzY5nNRYYnpPs3lD3m06Wh63ClrQgzIz_oz3aMNnZFPxw_se6Hh95tStTHkOQ7gh4jUIR_LRZz-LWb1QxhLHuQcIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OS4NoLKXN0FElnups2bdIwC9h3ipPj7Z35pUl6K_Mz7sqocTERXr33_dXM3GjnSEFCQDrxFimSY_HYNYy7dhJVBEQ81RgeuLNYYutFZtiJhalP3wlcI2DRXhCZ8j3y8P4KQFjtMotspZrme0UEZcnhJVBzs3UtyzNtCAiT5ZAVNEd9qydFcF9tBHdRIdEsgAOOyv3u0IY1sbRSAoaEOXZz_dKGAmVBuXhVhet-V6hzM20dRQCZ4A7vANOKFmhvz_VmGDz3JLnrDGGECvqhVPuB2q6fJRKrsRxdiU9vn_ofLRnXSfKInntTdq1K_sC3iUH7yGR7ocdjNYnSJOFva8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5iIF3bYOUlAuowQkNYrRfOR_2cbH_rGCrUDqOo89e5ZVrD48RCd6kXB9rGGTr0_-Ryvbfe4Yyg93mQrgRdkpDaBOI6a4VySkRVLN9n8pStx4rlStUSHvR47uQEopZK3Z7zOw2nrWooVVnaQIRS8fgGWuef7syDrL1f0eJOFwQ1H9knZAoIyDQwUZ4Pi4XmpoAyT6JXXwsrq4qO3y4i5yTd0D2TdjjY0eZFLU6IO3HtFF-5Gb6z9iijvHVhgy6bH6-SVaMIJ_rzprhREbR2n0dJOGUONI8ppAHPjFEzaj5LDVCSmnYGQiNEWKq56zojmXufCMStTsEEo2BHMerw-Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9U0rYXxupzSatkWGJTZgl1U_w74Z_zKsnkTDmlRiKE5X9O2MFiuy6Om5VN7bUco3Ox0h2V8AR1vlB1_FPfZqy0EDPvZcPhUwtV1kUan9GfeO_8a4KoqZ9RjsZsFKx_qXsZD0nO6-mZngh41G7zYQNhMuqUgv0-db1EJyupkEQZtxcoW_kEUxmX2E4Rv22gFvZmAGojDcWrSuIEGAximLtGE5g40DtdBTP-JfrvvIBO7UAStTrz-GIirSR58ZHzi3QPRr6ELPbrDwD-ANLuXcbGk32srv7_1yPnA8iuBpX5VjmhWjRTGfpy2vQ2cNMeByEvQLJsQcmamSZAD5wDeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ex4xeDy9KFymLtYsQQvMF23iouLOgazJvxUIM9rSlf-WzPRFU3SxspAHp2Le1Imak2zPDzSHN0en54-htazqDQyNAn14x5Kh0cCeQQaJxN3xgzTijkrdp1jIff9bTdE80WEHNpyHPSzOdv7X9ryHpRvEqQLwjcV3lyh_yEUhnD6wXpdAoWMZQ9_1xj2hyFcXbFbvyKnipbfNccu2ULXlcnKKX-kQqr4C7XiXaoAWP0G0pshaL7F4tX4vqW2KQSq1Tt5iLw9l_KqV5IJlSgnD2klgvDcnnBI-lGcJ078oJxetc49QR9TBIdOsUQYxfxGEIAYvu3FwXCbCj2IFpJYGQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clvjphwDvSnbodjDQwyW4XWP7fv9HFeDHjZ5IYD-DbmRTRAXI2vTYbVDRy_bsgoe9OjDvv5yd1upC6DSmpMuMGN2irJNFQsMfLWv7HuTzeTjDibB3YrdxuEegBUEDxvKmdLpqaFtHlJGrNMha7lyBkEGK-R2xyuiNk83_A1tOhgvqeWAHuJpviU4e2_jW1OeSR5OUJ4AgI_1xQTWMjEOveU096rT0wd0Z1KJNxARVygDzOsZlI2Joj_rnK4Mz5cjwbNuse93dsjTbAqKmQnyWAFXFhUe6-nz69PBT8L_yHmkXHz2lU2E6HFBJs8o-SQf-tHhz1Bnwv662l7f0e0YhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81484">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIJFOYTVZLBPZsivFZfZrKFaiY1pPocrhC7ZRUEbaFaiBKJXDm_Hi5oDq8r7GssTzHlqb9d03R-iHyHl-949W-Ed3bCp0ReP_c99sO7Ys7stnVhRPo9lFcsJI1CNaVlqfsvfghI6sBySAYjrdWxLSTd36BtnS9zTaKh0rJFGh6R2AcCeF82Ccf-qQGWUD5EZtWV1VbI9W7NWVxCf0ZtZlORua9Nl06DVIJ_BolDR8Z81HyALmZ9cpCqdf32xzwsuilaS2DlnNHImwFhUpV7DqkYu-dT4JaYK7KNlZcgJdG2OUS1feHD987Ch8intJcGCgwEou8dRv_I1nLGbRqMPQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81484" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0jna6aJYohNkuE56sbKfjI1lVQaiV9KaOSQMcQ1IM3sPLc495IweBY_ITD0vz5i1lKtpBANX35wvSE3JHeZhZhuWLIO-5zSyYHoCTld9nmDcRtZm3Nz57nkTjF20nSLXtaede5L-vQyDCp5K6SjO2dxuoyNw0KajpifX70cOrJrz4UUwTJIReLv9ZA8h6tzhzn3kSU3U00dl61Owo-_MHpso9FB_fWGXxOx98v3VL6KskUE9DRsC2Ru2dNCtbt4KFdBkW9Qv07XxpSY0AhW1at_a06-IHECKENXwW4_hfQWnjiUSE0Xlu-92dY3yCKcgOBZA01db5OYQ72GidAldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnD8wc5W229lDwc6THrBnbyCpwjpzsJBge2LG-0ZylloAX3UcJUlz_SBuwO3aSV1HMuB1I2NP7s1ge3YCi61AbKZIJwxwE1ceqxuLbOrfZ02zSikuhIlnwmdASCmvNCfmPR4HZakfYwgaZZMSzau0T_FghSSwcrmhL5Zw878IIwNKmOK8Xaz4JW9YKrgdH7DtIhIPIeNPtQRgoBM56EvD5RcIWROoo30E7tPKg6qZV53kgB7g5wS-wPT5jhR0BNCQl5TR8fayhqSNcZScAz3NvYtaKD5QZaqkD--X8G6Qi9djR-8lj0b4EFSdVAXeaXnXfDo_cmalk1AEwmXIa4r8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdDhoNrTpgPlTWBcT08xGZLq8-Yp_n0ebMufgZmclY-cuzLNLGmCYO8mlvdmzyxhlCY2FKTHTo5LYaRVia_s5Yf-TjxVFod4eniEgzruA8esPUl3PBR-7bz_MoJHSEcERVPhhII85xMmgmhehi3QnzzL4bOPvelG4FvAlSbQVpIyIKArdlJpJgLNmBGaj_fd2veQsELyLgtgtCtjuOM8rEtH4NTL9T_AJ-mfa11SdU1hHIGQZoRVMQDOX8ixQEuBxigqsf5RMtVpcx-1ulhLJMjYNgdBn6grnj0Z3MBWN_b7onNm9GEH-PSRC-86E6hw-6tMnOyMyosx6TO3-N0CMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGQZDAn0f19qF9f-HHd6atCej1e2xWP1EgkcBhmeT91i1P9PQJd-5JoiFR-5etSNto3wWwotlWQ3638ehZ4_vjQa-OqMSy4rpVxU-rfbPUDSOljXZvPHbmG_8dWnyLbblmNzNhf7qLWZZti4wWO2WWRNMnMYtOW9dwZ6slEDr6PBsKuy_oro0nN_6gj_sV7mgWw2ok8vV-HcfnShLu16tDtShU1Vjs-9NzDx-LkxryxphQttuF1hEz6zRLaWjsB4cXAEBl5EIb64k-pd_R5r9XucKjvnmbKECDa3C8GYAI9kPQ0qC5SQuklpiPLpkwWR6sAfFRtByyWbeX234_pLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OE9wl-h6Xl71dkPSfY-omGy-pbNVTea_2ywEgSXH8Imo95stTde15oZFZvd4SrGgIRDcOaPgZ3wlRSv_YyHIshHZu4H9zPUlDwnDWryUBZnEol4rl5kDwOGQY15tlLASNDdzbrsEhNkL5OXuR-H-5b0xqxW8ziGS3a_4YUh4I8Gbt_RNfse_VbGAH2H0_wh4vFnBFC0cKcp1oihssKv1Pm1GfsH1rP3VaGtovB9riD62zxGeuIQPW7uiLBDftMMsv0mgh6d32cFpUnc-soH3qYIa7zkgtVsiQZYUSOjsHneIjchdrPMtnvyQ-r1xKF667Z8SXbylJ2Jn_shpjnrmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVzH0FaT-DNgW2ff1DpTpcpNxEw9WQwBSdxblyNEgKs0kT7VinjNwUhw0rE76LHAR1dPPq-V-0BSaJX04RFf1CfdeT32AVdY7OwVqIp_rYo_MKHbvy8bEwQYXlFs8568ZFsmFK_JgGaR-9ZJB9zhQMzOVTLkv8JBh6SkU6AiiJqcTjSz4-aGufzfARajMwx2aQoy_CQvTUi8NSw61mrJXNzR7KyPNFJRhIOMPgi5Oif2JENgijKXSsIEmT-6-mBu0tWjeyfNE8vOFLFPCNNYMdBFUm6OiHgLqpykyObWnsYcnsYx98Mx05cR3pImz_Q9qJYqkKqQcSV-zi_G09Vo6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3RHsoDANH-4mpblCd8IwpVf0rP5uj32MzcLE6_QKJ2KwcRWP68mF7DBb83FhqLYL_n5BJkcZ1FXz4SOlGnPNQv0S-0mSgeVfMPGk9X3_10U-k63k5v3Rzl-kLfqIde4z1dtMuT_izk7YnjZ5jHKmy_N_5VRZ3wgh13dc9IR2XNydrd9CARgCoq99urnjD2LHWV1eYvgJBgG9CNQFG0PDMtkzuIUZpDLu6M94CS3A6iu4O6zRb0p3fmAKnPNREXUsvt4_q5BKnkBGGJfTb1smgmWuGvtn-V_I5OUyOcWBjsfbwsj0eF23RPLxdj7afI1q5K_Qt5KI6_KDd8shrhPBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPTp5UFxoknWEGRdvngGx4YqP0Js9d-Uy2HJCswN8jC5hknq7H5uyFDG_Pn2dbQyHYG5BbX90S_6FbC2qx9vE5th475Y5I1G--kGg31fKbry8PsV5iNSTjKJ57-Wa2EoRUR73amBYhONzpTEcyEaXMAG8okasokzJiT5_-I67uytWJSVi4AdmVJk7dWKFWBvggaaaldrELt8ItlnzbuYyCxJseqR20ZOKHf3YIOts9OXoliALz97Ld3453vNWS3IM2vsam9gzbmYbwtGRAG1Ypj2ffdNMp3d6n1a9h12Xx06HJqQOb4tQk37KIulNmGsk0RbLwYlrp8hUHhI0huyqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cE_u3dM8X_TIS82DnefIcnRz8UYfo4Q9GTUNgo2BmLhUAW4_ipPHChXY7cBftAbZuPxQijRvwvGxYKK34f1BuTXU6kXKPSz4bhc19zQ32QD2Wkd4jHAsdCPZx2JsId67nAGVndF-Vc3UvYx83FBN1eJgyLcQuNBvgOg2Z4F6q_qfMy1GUaHStbhsVgrIzcH5rmPJZb-wUojTkPAEm0VT4zsHc6eUCDRM3XQ1iizyU3DSe8HaaSHATCV0FZzftmb5oVNG52aWvcWNqW8cy05humOv7ZgEmS2WPOZyGUfFSwL3lbrgjuu-1MOw6pKcMG4fRCNyzNbMDVfI4j75wMO8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W745jgJs7Uz7I1DsSz3jp2KChZlkrcA7j-c5IUQ4FZoZtai1vye3KB-m1PUZMkzYSSxsD6Cs2AJkXBBYYkgKmISo6UVVUcs3lAkyeKKOEkTfeYWrGs9jfOSAAXJQOVb8Y2S8Eh5uaR6NcuMAy3DmK9mI8-K-TNSLGCI-IClhVb7g-or_1dmeeRw4LA0hlIiKKRbkeJ79BnO5V8Pu4Sb_sUSVD_7izGA9D9a3rwmlohpFC0PhP5D-aCbP2hwunP2fA1WYFjLogGT35Cmnv2Wf9IKsHzHILqHzhoBuESeurQWDJV4MCg4eRJ19d85C2vgDZVDXwWI9xpEMvpb29vaOuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8BZ7aC0IH-lwV7aaBZNGqcPOP3RubCiMNN2h28DuiUTF8xJ46QLjS9k3HxwjMZztIZ6Y85XD8O1M6YQO6RGcJZ6OQDzVISntLsPBoY09YUVjgqkmsOmtonRaJ21emvL2pOTrOZRflrQpr-zhtI4iqhQ9GjdmX9MljVUp5PPFfS4xHLP783nmQI4rHjW5iip0otlJKIM4aFW856GJTOSJulIeFTTJNTIDy79ZVbDgf8HgCF_DInQ4aF8UtfNAO4Rdqb915anTr0c0hySUfOhxZ2Vq5Xmkw4SVwkvybvJ1pNRD2N5VVJsc9P0UF46lT0iLOwbF-XFO8cqh3DS08oMWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl5qEvCqgF_qn8rTi5DAtoA0bNR9ra2qevA_wgv-RZHVHfjZ4cohrGiJjiTfPzLLeXzgWPX0ncHZWQzY9jv0ZP67KB4apJrdFom3S4Eu3YlXPWQGeoxzZ19HRhC_-uL15TridTC1Yde9YhU8mCXPgf9poaMTG-_Ne_9T9t98WNYOMSgdsgbqZM_9cQ1aDU0zkmBw_m931lkQPaJLbpt95qgAV0Kn9XmzdmTmDiSQ6-mZBJE9d8tVz36QjOgq-y4CUe0zje3ddMntvcdAg_N6Bqb4aaA5l3KrBWyGkLYUsyPWDvsTifkPB3OD8rlrMC9j2FFZ7w9RDAWahlSt-9sBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4gfYoeqVn_9Bg9d3UrghzXBtzzXcKTsplcpEjqTvOCOpkGsVjEDkldzCLCESy1jSSV4p__9HVXqKZyswcU71zkCv5W_5gmk9zY3O7ylJeTtqVcyZA-wQFC2abCNlRtKvk9trEl1MtYxXl1hJevY3z_zz83bL8TX24kLl6wyMS3YcSFkDcLdcPquv37e3_FEB_fFvV82wF_oPuaCsGPe6asFMqZ1EYwXW3XXO6Smif0EQ5V8NykQK3tQXgEHC3G7U1je7cngTJeoqe8h4ydxRjNSgJ3GyHzvIGQacDK0poajr_EHzj_Jg979zcpmdTO_sP2cQVng2bzIrmYIoIlf-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9VAaLIpvYGZ2BsdbG9JDyawa_C3AOfugAbj_ocUrHdgXRBeLaXKdvKvr1-Jeq6-J_Z6FOoRy95emHI5KAWGD1BovtlXA023HnHRNB0pH0hbHQvfXhKn4yG6A84yTTE6mF9W5qURX58z9_vYiscThkaF3RBj9U7lVEk2GNnR_BRW5unW8lTljCFyT3-dz7CaeEL_zdi6dSawBe11y7rGQZR0a3ROFq6j2T94hk4fKc8m4EKxe_F0F4bNw2Yae81XVojFa3_nBzgU4q2TyCxGt1Dxht_hMDXhRM_u4mP_0ly_5WUZp6JuSYhmkz65TDXXWXBznaHus14rPhiuo3X9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDtJ-O95GN6Ivi5CX_XzcQqtipVZrHZzqMNxIlP2Ewr-kNj6XY-BVkR7jENRTXKXFTJC9r_JzvCFYM-w3HO2UImWlerW6JPct4qv28WXTccauw_cocpF2V_5AXqmXD37lWgeto--0GjEjHXjBQCf05IgzHMnLNnlYXIOb1cQtdhYpsYfN5NZv1PcdUeYPW1xWb86qRQD3ibooD-kQpYoxvC54DU-i-a56UvyANEPZGpjkHuRuiNjLbe0Ne-xJULPEp8N8vv_sS-2PfDDegOFohON6XMnNVcPk4N6d0yuReXS_dckfJIMBUBspMf_2IHroKWpniPwRYm_K7pIKG1DFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMe1fRJKArZbqvJWmuFfbM5k0c5Q8QKxGGAVl7ldpQCFuCqmP5whbv03gyVvI7HKk77uZJ9g61H9DFnMj83yCrn5MfHkk4oKTlXIOGsX0JKb3EHsoFt2Wd4e0sC-T5lH_QBi4TvYfJiiXaG5-xAQ9UZGqdhdF_3kEb21ZEjTT7V_y0RfnbAA7_fP9PS8SFM-gtj4LvBJHI7hTmT3kgMYbY1G9yFYdjLZyFsQM0dFNqsDUEObrWJeFcMrjJ1hLmXrSUaEc57JZ3ehRC0sc6xQEPA9eqxceiShE2hL08892HaCH2mUdUXHcR5KJ5YKB591JBTAjrle-NEjB7k1WGe68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NifIUs40Lxp9KaRze82yGnsN_krCfrAGYhZSB2gCl0i6IcruruPFXwWWnYkOjZyFNQ6rD-YLP59FD32g0nmGoidwg5ZiEmcjHpYntFpD6f6YIj0UWQiPD0gLSFdQG2LFMMVp1cCxhCcnTBC4Cnzi9uehzN6JONjOk6Z79Oc12e-D-SR6el_W23NmpebHzoGYxs8aciwX5B6yN4tF1A6QjwdOG7WfhMCaw6VUvAadGIL0zP0L0DTpe10PJIemu6Mnr8SmxztRhjqbC_vjHNp1vsxQea8oDgXsV3ok7ukuBcfWHbp9djJMoznAW2_8rwn-ISCN3g4d0PgeSCme7PKyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvvzysFYe633bv89PqGzHv11Q6099PurWd3bYXuhtcb_W7MwlM3Sek19-t2mYptK_lnDfvP0j76d4TbJM4frC3ArM5bWBJ6B8zp8N83wddAzf_9-VdFfLOYkmMzDi2_Ti6V9UlqdGhSxuS6AF3HZQlkIQti3LCKO1Cx2pzz-gASVKNzqmSJABTdVp-ISaJXi9dauE1r-HLPGrqCgw3xpSlC-PAn25JV9x3MuGHKWlrztM5pcckiwBtSC-z7UXHtQDm373YnXLvXBFfSkLXpdJGWqo_0btDcVXblJui2K7lpAJ9nR9FCUscE2zmuBG8L23X8InX1cPnCUlf4uP0B2gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=T9cJB5nw2xMMoHnfo-BsNwtvX1oQlHcBEjrc0exzmYNB8frJekyvY2C9TCnRSmkIpmHo4BNVzNen8MquO4fYQJkpBx8be8AGFNetnHcJLT_32WXQFXwUNrtDuWP69g2f2D2YTAd2IXqgzWKrUHVUk0UPpsWcQzTONkVRBFcqFo3ENUuHNq-G3HhuSLnnyOn3m7J_pxrYaLbdnjJ5Fgi-Xt_421Zdc6PQZNRsNR-kjZdl9Lmwjo62upfaUTRh6kTlu6-TipxBI6OCqMYfKPshv7DiYIjlRJDlQ8q_z-mhDqychPRew0AFCJu4YcJxA20Ne9_koy7fBGVeYT08-d0-jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=T9cJB5nw2xMMoHnfo-BsNwtvX1oQlHcBEjrc0exzmYNB8frJekyvY2C9TCnRSmkIpmHo4BNVzNen8MquO4fYQJkpBx8be8AGFNetnHcJLT_32WXQFXwUNrtDuWP69g2f2D2YTAd2IXqgzWKrUHVUk0UPpsWcQzTONkVRBFcqFo3ENUuHNq-G3HhuSLnnyOn3m7J_pxrYaLbdnjJ5Fgi-Xt_421Zdc6PQZNRsNR-kjZdl9Lmwjo62upfaUTRh6kTlu6-TipxBI6OCqMYfKPshv7DiYIjlRJDlQ8q_z-mhDqychPRew0AFCJu4YcJxA20Ne9_koy7fBGVeYT08-d0-jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q3kfk-kNatwdci24a1lqOT-l-018dd5F3hcq-NXXPJdfDRGZkbD-1sjM9JgXL_4NCbM84KEjqLM3V54tBwaio19qPWG_fOfzJTlgx1mTFfFEtGcNqi825MB6sW4O0UKuo5GCvHEbF0z6w0CdyyIxPA7QhPjdAyMgehj-SF4FJNOmkFoXDzMFpp_4RddRYaQJWQUb-9fYVn6jTSUSfbwBNuuNMR4ZJxVtD2aGPAPwk3U36LfQ6kF5LMqtOnvHS4cpvZjBhLVDfpqydgqv3gPX4i7hgWgxci5OieUMwzIjlm9cGAIThy7aB7K-9iV9nTVICxtsbqebiWJ-XhmxxjVEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TmPI8Po4T2WJ4c8OejBSPUoFxiZToPmYHa1xfALa97ftGxccrebGswFAVREzbv5-eyqsAOhjhZdCueksEyZ_0sm9qDSWgPkLZdX1Y3OMmyaUf7C-piT59qCTDs1sKTFi-pbAjrK-YC4EnJFuo6VMfAaYsZ1PIoDwQv0idhNWCs2e7j6lWw-NFwEDfKnYYRtDP_2bErNzqcO9yBPPDfBARij1va7lLlPXi9C32BRkmMi7pfH1TH1bs0MDD-axq4daTFTeICZJD9mbC94x4DgWb8-4dFKkr56111Li_N82-_L3PxUBgstI2x4fEeIz2qdWnwGMuwivqI347knBtmkJlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiQ904LSpf3Q8d6T7xXGKlKbrwIZAVgfKH1t5E-0ZGIE9Eu1gXUC14KImTrBYRqalXgYtUfgAXZnQMmmMJBGqQ5NpfTjCCvYhQLMpMrP3p_ayeh8MUsbwA7IZBPrh4jJ7MFEeb0hS5OKHJueMgOxQkHJ31Db5xpDpEPT_Gu_N_kxi0FBelF9HwcWV9Zo1qaQgkslkyQI8aBO3GtTsf5JUYe1vQuBrb01jiMNia6pY3-XA4urD-svQ1mbyxxa6mYP4X58EKYi6mbAkX7A-tR2b4li5eaVXFXwNBB3bY0jCqJ5HsPzzZddFkedfB0FC8vG51Cxd44r0Jly8ZXTijLq_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esXZ4g4uGxf9mq7Ke-ykDFbG3heods45GDfkNwb6AtkuoafJs0cmH4g3cMwem_07VceFd3wOe4YvckWusxaS4AaT8EGWfelgR0Vlfhj1LH61QdlouSpAioNm8-DsP1kNPsFBk5bnm9uchaL-k36eC2pSBGLMLMJ7GG7awTXg_fxCzuy1Q_eOrPdNBgql0HyTV5KlQh6CYGueHSw0xzvBpD-kXoRS-wd0Eu3UwaCOgvsbP0ZRfBE5rKX1WiiSdV3cTBaSEIpnO-DhpgqzG27qBbkJ-jZ0NxaQc0QMEuDJdoOE2QADvvHSepfmcrPZ4XzM8qNwC2CynFU5EGYEDFowuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_oDfT_BoUINGxrCNyGMIu53vQq2C9s1pk_mHncdK-l0J59Dih8mNr--cvHOiE6nNSVhi-u7S_N0oXs9snNaX02k2Re_o2bbsF9eXI3mlaUwOpOC7KbubG65Q7GHtHE_TO9Se2cd0b_FBVrMca0gWaNFQaOZEFyFSaE2QnjA9Rm5hdAkQ_DjkYGgKsjWalse8wls37abnWvOlDHuJs6-Snt6xxodWUlY9H_OUihnfKxlpA5IzuZ3vKe1sLtPopcWeSs3_vwFGUSveyIdww3H10H9BiBySu-JheJVxFfGtBwHNwV-EgV3A-OCY-3DsOpU5h53VmLvEMgNnD-1JkBOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiA3-pACG98yyxpvl0RrfDf_G6WhUqiHUmbVHAFBbq0DQvHWDbXt2MmzBT8L-AVc10QjhX73P1el-hPfN-Z3IqtMLLg8vOfHcXk4MW4ntWF1-Dn_esRZpz0wbjXIsC0boqztpL_I5G5FcfSvPelyU_AaEQVn1VzROYjMdl6zhkNHapScTTCMJ-U5Slm6B_vqSEPLIHrl8lEKSgCDh3PBCS26MzQ6eclNlsWqyVldQNYaHBMXotlB2lwZAovmOf6HSPwNmd0PFzENHOXm25gXoJCpoYafTwyEGVx20eaJ30JS11pNvEUgSE70mZ_SLUr-cTiAPHK6cqXCcW4r10U-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjPB5O0_zsThvyamTkXCtaT7HE4AQlkVnO7eEd5N1VBngtVP-qq54QcDgTvqz5p4B5kSw523UtVIGhiyGYp7o7Rub_segu-nlAezpQ01nGBABhiYCSTtm1lMWMTUL1Paq0fMqfa2q1uP11mtoivuyvguZdCOtpv5vGkyQlUeePUPCgNrevXQZS2YKEj5cidPuoczREweRteRIr-ihu1gsfODKHpND8WiC0FTEQ-Mk28a7bAzpAKCED3O0QSuzClb1BAX-k6rwVg8xGt6riFUf3DG3Sye63OslPh4fMlts4HVgvLF_dd4CFmud8Q1kZuD2NV5-67fLEjaUybe98teRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCWoEJH7RIeWuVF0ujq0KvwTZhOVsTefDONbLm9GHjwXx052UFyLyEoDeGZAunBmEScPqqZGwn2kt7bezy14vhUnOnJ6GsxGIyiKjOYkd4_ImZIMx-bQzgb0JchWs2wV0tO7lA7DMi3ihbFnV1WM6CxI-91KgmZqsLXTGpaOuLGyEfU-Jkx5Pb6Qgt98cYzIa2_Gkt8Rk8gBbmYTMDxAIKeRt52G51CPLtBJVIJ0HP55N0hG-EOYe4rp1DxtEfIzo9RQBo_QcBAWWVIvqXwnMVK0p6OJ8cfKuB7IIRj3VRZGhGoUUZSc23t0ZF8559TynO5hemkk9EvRFsPdcxTBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE8lRw06zDUDaJgdMQmJGmnDy1zeJB79WKVnGtRt9a8k-kJ_wQ_WB-mM49X5zn0Kk9YqyUJgp0jiNNa91FcPuxC-wWmTbdA4YHPpIAJoMDU3lNxywXLkl9m3URSwTkr7hEKRP3iY8vdnHhko-Cw7k79Pdj_G0yC8onkavjTwvPAql9uQvQYrQFKzUqYbdB_1DckdhmbMZgYIZ0n41pMby6sDyuNt3JQlwITyxH0d50amlTz7Gk3hcIpy3J_KI5hqUU-Wt-1v7HIz_c72m0JM0o7aXPagoBMTxNjdTLIPm2C7wfK1FkdP77CT5D-A3uxL9XSo6nQlN5l72TJiBt3zDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81428">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZfrJwk5N_XAfJAbEh9XYoNt41DTHQOGeGrOMnBUsJuE0KiWrqDbYqSuRe6YvLHw_oFE-wnoXdn1w--ypOxJQ_2GXAMnrqDeHUii7UQGrdubnp674YtgsaHgv1TYjdisrIljq9BmhpDBe7uEpT008B1C1bS0oCW6EU2jJpKlp4dmnxIf7QCXP0trSyaYjId5nx4SrGF6h_PRwXs8Lu6Fj_XBBEBgBRHyrW1FCBRu2TjU9QaMS6peWBBlLSi-Mf3V4wfBKVjYhsqzkn3a473jU8CNiUUpP7Yhl6kgY7-RKrOaW6FT77U-SukUoIWCsXF3I7NIJXRxQkq-NpYujyyd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81428" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyVJU0PNxiTdAXecZR9V_tEg0Lb9_2eF6TbqPc7jIaJxFqnMPz1x6im1yk5R3TMXOUWIkYud_I0EkGta90iWrA3ruygjZAcCFDA8LegDQsGxh-WEkHS4pWiWRKftp_PxziI_CmYKcHuxYN-IxBB7UCCKd2Qsd4OWAnkayLqlhZRNLwvUKFWzhY0UwRvTYbrGiek3kABYv6gNs62QAFx_EevWPfKzGZII7mDECZ2ZAciOvdV6NFCxZ0tbKg3t-sAyaruWs5DlytmNqraUuKp0x-2SLyAn_EyCM7gx-a5NyWSh2MTcW2QWDtKqNAcr08I9poBqojefeCtx52C36_k0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxypArchM29fmQPc0pvuI7pWzN-Z3-58AmuZtdF4P0PwO_dxSlgDOj5-Z4lE5vPPsrh6G_0fLep9g4lV6Iesc6cS707g_2KbobGexIbp3ei-iEeR3haaGYOYcTQmxE8g8Y5OGhfwg2n5tmLezPY5-PDF3UAtT0pxBNk_6ZDn2q5inmbs7R43yf-T0cNeEeGjmEMj-CkUbhyfXzfACdhbeSpvDOplQTa28SSwrZtBZ3-7nNlEgzW8q60X77tex_V01Fo22tDzPbNC3Us4NOIsbbg-tLmQ42H9H3NOX36HwOqufHGgVnqY119qp7zxw0vgBsqzvPcYa05knFYvC-wBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzTWGddY5Mjrp3J3wUCddnu3b2tzJKaw-y7jUGBO7Q8xGwaGZwbNeUPp97yJEBwdp2pPJ0_XHxmvZlWSeSxOHvZAP195Um3DCjFW5efaeJ6WxLR3vbmKtTl1U7wqGw4Q7WWmk6JdPGS7uYwmVPzcPF_--6bvUuplMPllAZ4lUQigb0gCgG5dW_q37fsL-5_RqRRH8XlWlw09HGBpQC8Hd_dcVHqvW8WHohswhcA2rgLh8AYmwvPenRCsXSjucD5YVBq5fL7k82_Nyy89SrTJAc_ElHKeUClwtHsWyVFUslPVbsIxfqMOlQheM8ArEmM2P7KFaFEJuTDh1CqISPKtCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaN4H3tynWF5p690V5ExYDKokHJhzb94yeRE4qt2cN49R_cnGpUx0H65qUNbySXAes3XdLiwcxXg2NlZiJGfgXF3fLHn8k0WDo9105LBBkr9KjR49YNk1CE66h2TD8urP4jzon4SdW_dUNwilL7roS1IbHVi1QVnEK6gTF2fXAC-vtvjOukhAYhD19vnqrje0KT2uFFpLVlr0wu9IydQYqD20lNULINqwJkEBZinoHBrRUU82PcUkdcWNa1nXnxmKxc-GygkCCCVBuVb1BsrKtH9URsVy9RcX37Wy8RP9Dy9_oRxUPBqn6rzkxkypWmMWBxwFg3TS4_uL0P1UhPTeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f171036de.mp4?token=eWY7CPl3IlpV0dbBTh631eeLSWVrH6_6Dc7WEqjS6yney7yolAzYHiV3TuB9UaMxJubT5rPjnCf7f8kFOt--W_2bPCPOzEHEZUBO1MVA6t58XxWlVBzNYDjyhxzjJEFbLFR5qu9GMkageHA1kMLGIvKneW6JAa91ZW0TqJ2_Z0h4Je_MkSpc0109f6aQuNnMOyqHKpaJkM8EN78jfWba3HQ_OPAZVHnpHMWywb8x3bNnQ0tji0XeSTHTHCImq3awNtohwGCNpebWK0z7xzoRf7Kh1oL0qzk9VYtJTAIKPIOYymdTJj4BXcZJyzS_LiNCkcXI-psrQKBhjX9belK6tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f171036de.mp4?token=eWY7CPl3IlpV0dbBTh631eeLSWVrH6_6Dc7WEqjS6yney7yolAzYHiV3TuB9UaMxJubT5rPjnCf7f8kFOt--W_2bPCPOzEHEZUBO1MVA6t58XxWlVBzNYDjyhxzjJEFbLFR5qu9GMkageHA1kMLGIvKneW6JAa91ZW0TqJ2_Z0h4Je_MkSpc0109f6aQuNnMOyqHKpaJkM8EN78jfWba3HQ_OPAZVHnpHMWywb8x3bNnQ0tji0XeSTHTHCImq3awNtohwGCNpebWK0z7xzoRf7Kh1oL0qzk9VYtJTAIKPIOYymdTJj4BXcZJyzS_LiNCkcXI-psrQKBhjX9belK6tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طقه پوبون رو زدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc18WkoM0guelQkwdFiL4hCPbp9UwcymqQWad6d90jUC7pkLfTk_6xNnILWIlHBKllEcNkjyyqcDtEjCeWWsxOuQBMuL6wWOXXXjcWhOkJvDdTo5xIoJPZM39SND9OgZOiq-3RhGNuFdZpf6ElrnIIXu3NtruKzsZQutBsWESWoY2SpHPs_ZHQmcusF1Re9LsZx-_S8NpN2iP5M0Sn8w6YJ7rw4W8uKwWz5wM_hKdep0zRwK-0rkWdnnzrsesTRxg4XyTyL5kx9mYUlJO7xZtw3nzwnd6bckY22bMUVVRh194UsCUnP9qQetnYqHMgosE1YBdq7gLFy-Kmy4C5mC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=e10KwHzdc6RfF2qw6qrVIWKxnQI05A-FV3bdJO2CNCMkWLRLd56tMie-iA3JW7VKZQLfbOto10H00oHSnTt-RUXaAq7b2SG9hd-oscoREMaGTXylTYRKWQj44GFtSewOdFBgXpYugco3GiQbSvWpLnB-Ek1aUO3kMHUVFVaASvYaEg6zNG_hoLch9Mexy8VZXdqvPBSdqHIDAunCb-faC4nkAGszN8I4YgwT1IZYYmOTO5MYH8k8dPSGivjpyjDlnyl3DqIVpVjvyFz4sQjTsY7M6SxOmY4px_EDn06WN6Uk_vZhXAZXeszif7K9aZNIsoLhmXI6_A0bSvxog1FrIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=e10KwHzdc6RfF2qw6qrVIWKxnQI05A-FV3bdJO2CNCMkWLRLd56tMie-iA3JW7VKZQLfbOto10H00oHSnTt-RUXaAq7b2SG9hd-oscoREMaGTXylTYRKWQj44GFtSewOdFBgXpYugco3GiQbSvWpLnB-Ek1aUO3kMHUVFVaASvYaEg6zNG_hoLch9Mexy8VZXdqvPBSdqHIDAunCb-faC4nkAGszN8I4YgwT1IZYYmOTO5MYH8k8dPSGivjpyjDlnyl3DqIVpVjvyFz4sQjTsY7M6SxOmY4px_EDn06WN6Uk_vZhXAZXeszif7K9aZNIsoLhmXI6_A0bSvxog1FrIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
