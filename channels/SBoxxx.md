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
<img src="https://cdn4.telesco.pe/file/tH7D_vfb_xFyvns1-X4wHx-36w1UWVO1rWaZTMloPuodItnEVMQDS3WNFfHAJEhA220J2lQ2TlTZ_cQNLAkdE58RY24wQ7D1GHkNl-WfkQ9_CP_4bVCznuDjMK3mUopaeDmhJetyoCCKmNHiuu1y6-_qPeDNelCsrY6qgwYO37xJZzAxIWiDue55UfOdr65iiCDMpuX0qvw_ACU-BejIhLXJ6pcTQETCGZR4btl5U8oF57dZ9M-RUL-1JP7TVxU0cOAno9D-u8238rKMkhww7wR6cXXdVewq5AEwXYz91vnGN8hFo2rbG5f14QbUXNjCa00IdMbrJ-iimtuatOtPpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 20:13:26</div>
<hr>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تسنیم:
کشته شدن ۱۸ نفر در حملات دیشب آمریکا
وزیر بهداشت: در حملات شب گذشته به استان‌های مختلف کشور ۱۸ تن شهید و ۱۰۸ تن از هموطنانمان مجروح شدند.</div>
<div class="tg-footer">👁️ 587 · <a href="https://t.me/SBoxxx/20474" target="_blank">📅 20:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20473">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ:
حالا که تنگه هرمز تحت کنترل آمریکاست، آیا باید اسمش را به تنگه ترامپ تغییر بدیم؟؟؟ مثل خود آمریکا، این منطقه «داغ‌تر» (پررونق تر) از همیشه خواهد شد.</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SBoxxx/20473" target="_blank">📅 19:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ درباره ایران:
ما اکنون تنگه هرمز را کنترل می‌کنیم. ما آن را کنترل می‌کنیم.
دیروز شب ۲۸ قایق، ۲۸ کشتی آنها را از بین بردیم. ما آن را کنترل می‌کنیم، آن‌ها چیزی به دست نمی‌آورند و ما کشتی‌ها را از بین بردیم.</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/SBoxxx/20472" target="_blank">📅 18:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئیس مجلس نمایندگان آمریکا می‌گوید که حمله نظامی به کشور ایران ضروری است.</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/20471" target="_blank">📅 18:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20470">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بر اساس گزارش شبکه NBC، هکرهای ایرانی در هفته‌های اخیر، سیستم‌های تامین آب، مخابرات، انرژی و سایر زیرساخت‌های ایالات متحده را مورد هدف قرار داده‌اند.</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/20470" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20469">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBXgxe8XlnNbQT-liZuQHmjWE1tNaFoOS1XJP3t0mLmdL_oaT-5l6T3K-h8PYpj6NAQAFYRC_5EyEkcN8H6BB6uCSHoGfEfYxjXg-mkOgyscWk8iV39L96wyiLY-IccQNX5LeV2xB5ZqfxyDxYacdSZ_V-661hCRt-0coqldNrwDnorbUTVZ7IDt67958VRWnyMWxNJ0v87SgPCRacqgYX1ksjOsFYOZb-FS6sUF0T3bB4rZZSEyjFaxhrMtFA57owLcG018iVWc73yrR0dAZ4bgoW_iv23NbTlcxRcSP4fhS16kCo1GF5hx6HOrIOBcxNwwsObK-1eZZ2J3ueWa8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه ای قرار دارد و با توجه به بیش-فروش بودن تکنیکالی، امروز احتمالاً یک اصلاح رو به بالا در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/20469" target="_blank">📅 18:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه ای قرار دارد و با توجه به بیش-فروش بودن تکنیکالی، امروز احتمالاً یک اصلاح رو به بالا در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/20468" target="_blank">📅 17:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بِسِنت درباره ایران:  ایران مقداری از ملزومات خود را از روسیه تهیه می‌کند، اما اگر خطوط هوایی ایران را تعطیل کنیم، که این کار را انجام خواهیم داد، میزان واردات به طور قابل توجهی کاهش خواهد یافت.  آنها واقعاً از روسیه حمایت مالی مستقیم دریافت نمی‌کنند.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/20467" target="_blank">📅 16:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr5Kk_cPt7Yj69u9H_Bjl2QBQeVyyia582mOSQjykPVTkGOZweOccJBZPzwFnSeIiF0_PbTbhNCqaJRLFbkEtuKKyYkYm8j2C5O1Gc4W2lnpfwG8iag3VeyWL5t6NLAfBf4TVFjC9V03vP9-lZiKfRy2NmwzTqrSP1VET3AB5OVjHiwVj9VpTfviN-UTH0qPSNNlY-qXhpMszSIWuMk0A_DZi1hhRuYPbrWkZxn5X8d6YIV4dVUHPGcc3p0QjQ2_DwLI3iSFX2tJaDVjY1T5wBTICZQNfHTsJ8F0J7o_2C5j3PwvIm0T3N3jIaM4ynWP8JX-pTlELNFGIyer83R12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/20466" target="_blank">📅 16:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djzHY3cTo3rT9GhTHCsys1u7W0kbo9MVaTVSNPsEKczPDT8IKto3EI3ILDGHxb-Q9ObsDGyNdPGEC1Nk3IfHseQAH3TDnhu1NK3PxdP8Qhq9Nc1rSRZIYu7EyDcWuQsoPHrHEwwR2e7xesQEZtNIB1FjZ-JNhygxr3s9Nq2SYqlxTxs7HSPYhTQT92v4aDNt2TvGJAsAKzoDCBkNxQzJOWlIjhTOC9gXSvlqYq31Vu2rsZS4OuSuA3NOWY1Vv5ZbHUiwIgaPsAhvtMjfHAK0Es3qjderPV5WkCCdztofkuaQBriBkzGdf_FYugAv5_a_PKe-r1OtEjqJYnm5vReWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/20465" target="_blank">📅 16:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/20464" target="_blank">📅 16:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAKTq0Rzmd2rm7etG1Lx-qraQTVD1-xfbrDttfVyOge3vFlJmEc-XslaqwXnlV7dYZXQlnMoza1UjD6rakdJSldTFMaTZ2w_6yD18kJo2cOrIUhaCLZDBt29t-10HEsqgvq60g6enhsD44dcnqadkBf4VZz07Z0MOnKWPYFy_KNwUtZiA5ay8ottXg59UZs8jl2-VCKPRw5qL8FSlMzA2MZQT1kMtaR9pvJwsDqNcVUzSqrUTqHE75GQdOIheKMCh7J6HmhxgjedeN7UTpXu9coIruo9FGLkdz1KQlqgfQaIjTTDDCo6_DWAE2eHdRYsFMunKnW0J5rcCDTPGW0Ozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی خداوکیلی این آمریکایی ها ترسناک هستند؛ شما فکر کنید هوموی مفعولشان اینطور خشن است وای به حال هتروی فاعلشان!</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/20463" target="_blank">📅 16:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/20462" target="_blank">📅 16:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!
از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/20461" target="_blank">📅 16:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:   از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/20460" target="_blank">📅 14:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ارزیابی موسسه ISW  از وضعیت توانایی های ایران برای ادامه اخلال در هرمز:
ایران در اول سپتامبر، در واکنش به حملات آمریکا به اهداف نظامی ایران، از جمله رادارها، در همان روز، به پایگاه‌ها و دارایی‌های آمریکا و متحدانش در منطقه حمله کرد. این رادارها می‌توانستند برای شناسایی و سپس هدف قرار دادن نفتکش‌ها در خلیج فارس مورد استفاده قرار گیرند. فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد که حملات اول سپتامبر علیه این رادارها پس از حملات ایران به سه نفتکش و همچنین نیروها و پایگاه‌های آمریکا در منطقه انجام شده است. مؤسسه CTP-ISW جزئیات بیشتری درباره حملات تلافی‌جویانه ایران در اول سپتامبر در گزارش دوم سپتامبر ارائه خواهد کرد. فرماندهان ارشد نظامی ایران پیش از انجام این حملات و در همان روز، آمریکا را به پاسخ نظامی تهدید کرده بودند و سخنگوی سپاه پاسداران به‌طور مشخص بحرین و کویت را نیز تهدید کرد.
به نظر می‌رسد حملات CENTCOM عمدتاً دارایی‌هایی را هدف قرار داده باشد که ایران از آنها برای شناسایی کشتی‌ها به‌منظور هدف قرار دادنشان استفاده می‌کند. دونالد ترامپ، رئیس‌جمهور آمریکا، در اول سپتامبر به شبکه فاکس‌نیوز گفت که نیروهای آمریکایی تعدادی نامشخص از رادارهای ایرانی را که ایران در تلاش برای بازسازی آنها بود، منهدم کرده‌اند. ایران از این رادارها برای شناسایی شناورهایی که از تنگه هرمز عبور می‌کنند استفاده می‌کند. CENTCOM اعلام کرد که این حملات پس از «تلاش‌های سپاه پاسداران برای حمله» به کشتی‌های تجاری در تنگه انجام شده است؛ بنابراین، فرماندهی مرکزی آمریکا به‌صراحت میان حملات به کشتی‌رانی و حملات علیه رادارهای ایران ارتباط برقرار کرده است.
حملات ایران در روزهای ۳۰ و ۳۱ اوت نشان می‌دهد که تهران همچنان از ظرفیت‌هایی برای ایجاد اختلال در کشتیرانی از مسیر جنوبی خروجی تنگه هرمز برخوردار است. چندین سازمان اطلاعات دریایی و نهاد ناظر بر کشتیرانی گزارش دادند که در ۳۰ اوت یک پرتابه ناشناس به یک نفتکش اصابت کرده و در ۳۱ اوت نیز سه پرتابه به یک نفتکش بسیار بزرگ حمل نفت خام (VLCC) به نام
Senegal Prosperity
اصابت کرده است. یک شرکت دیگر فعال در حوزه اطلاعات کشتیرانی نیز به رویترز گفت که ایران هم‌زمان با حمله به Senegal Prosperity، یک VLCC دیگر را نیز هدف قرار داده است. رسانه‌های وابسته به حکومت ایران گزارش دادند که این کشتی دوم از مسیر جنوبی تنگه هرمز عبور می‌کرد.
این حملات نشان می‌دهد که ایران همچنان قادر است از سامانه‌های پیشرفته‌تر خود برای هدف قرار دادن کشتی‌هایی که از تنگه هرمز عبور می‌کنند استفاده کند. ایران کشتی‌هایی را که از این مسیر عبور می‌کنند هدف قرار داده است، زیرا مسیر جنوبی جایگزینی برای مسیر تحت کنترل ایران در بخش شمالی تنگه محسوب می‌شود و در نتیجه، برداشت موجود از میزان کنترل ایران بر تنگه هرمز را تضعیف می‌کند. مقام‌های آمریکایی در گفت‌وگو با Axios در ۲۸ اوت اعلام کرده بودند که نیروهای آمریکایی در حال اسکورت کشتی‌ها از خلیج فارس از طریق این مسیر هستند؛ اقدامی که موجب شده حجم کشتیرانی به حدود نیمی از سطح پیش از جنگ بازگردد.
حملات آمریکا به رادارهای ایران احتمالاً محدودیت‌های عملیاتی بیشتری بر نیروهای ایرانی که تلاش می‌کنند کشتیرانی در تنگه هرمز را مختل کنند، تحمیل خواهد کرد. CTP-ISW پیش‌تر در ۳۱ اوت ارزیابی کرده بود که ایران با محدودیت‌های عملیاتی در توانایی خود برای ایجاد اختلال در کشتیرانی در تنگه مواجه است. ایران اکنون مجبور است شیوه عملیات خود را با هدف بازسازی و تقویت برداشت بین‌المللی از کنترل ایران بر تنگه هرمز تطبیق دهد.
مدیر یک شرکت مشاوره و ارزیابی ریسک در ۳۱ اوت اشاره کرد که سپاه پاسداران برای شناسایی کشتی‌هایی که از تنگه عبور می‌کنند، برای مثال، از شناورهای تندرو تهاجمی (FAC) و شناسایی بصری استفاده می‌کند. این روش در مقایسه با استفاده از رادارها و سایر حسگرهای تخصصی، روشی
بسیار ناکارآمدتر
برای شناسایی، تثبیت موقعیت و در نهایت انهدام یک هدف در دریا محسوب می‌شود. اینکه ایران ناچار شده به چنین روش‌های غیربهینه‌ای متوسل شود، نشان می‌دهد که با محدودیت‌های عملیاتی مواجه است.
همچنین، حملات CENTCOM در ۳۰ اوت علیه سامانه‌های پرتاب مین نشان می‌دهد که نیروی دریایی سپاه به‌طور فزاینده‌ای به استفاده از پرتابگرهای راکتی برای کارگذاری مین در تنگه هرمز متکی شده است؛ روشی که در مقایسه با کارگذاری مین از طریق یک شناور، روشی غیربهینه‌تر محسوب می‌شود.
با این حال، سه حمله ایران در روزهای ۳۰ و ۳۱ اوت لزوماً به این معنا نیست که ایران هیچ محدودیت عملیاتی ندارد؛ بلکه صرفاً نشان می‌دهد که تهران در این سه مورد توانسته بر این محدودیت‌ها غلبه کند. CTP-ISW همچنان نرخ حملات و انتخاب‌های تاکتیکی ایران در هر حمله را زیر نظر خواهد گرفت تا مشخص کند آیا ایران هنگام تلاش برای ایجاد اختلال در کشتیرانی در تنگه هرمز با محدودیت‌های تاکتیکی مواجه است یا خیر.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/20459" target="_blank">📅 14:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وال استریت ژورنال:
دو مقام آمریکایی می‌گویند تاکنون هیچ تلفاتی در میان آمریکایی‌ها بر اثر حمله ایران به تأسیسات در اردن گزارش نشده است.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/20458" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20457">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آکسیوس:
آمریکا برای نخستین‌بار نفتکش‌های دولتی ایران را هدف قرار داد؛ سیاست «تانکر در برابر تانکر» اجرا شد</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20457" target="_blank">📅 12:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حملات آمریکا ۴ عضو نیروی قدس سپاه پاسداران را در کرمانشاه کشت - تسنیم|</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20456" target="_blank">📅 12:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4TO-yzCSzRdIajAyg9GTf2mRtap4Or-HQMliA3ZYhJ8BT5JtZQHYnL-w-1fLm9dkDLoR-gRol2zHsMN1oilD2XgbSJk7iGP8jIZ6HVbMktC6wZ843D68ESm9teRpBKyiwG-7jgaRq0S8KOOS9kHlvb-aVbQQYnEToAVtBlfLa6wib1tpQbR6-thNPCV3vcJcYZWWmtUWCxFROBsTg5M0cAe5jkU0rFd2OhThxMcBnypR7nkMig85CUc75-xutvmhiHOezSCf8OjPSkFC8ydCimmNzhzr-zFDn8XVC-M6LlGqE5Uf_YGUYaGjc68sdHkKFyDFV1ViMvSXne8wxcrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20455" target="_blank">📅 11:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20454">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حملات آمریکا ۴ عضو نیروی قدس سپاه پاسداران را در کرمانشاه کشت - تسنیم|</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20454" target="_blank">📅 11:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20453">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3dt2Ic4Dhsa47leBSgT1c3CLJD_SLThkSswJlrcXVYCy0NnFr1Q1vCsS_fWKbhW9KQGyyERfL087ZokKedkTjhvQHXCMKFhgwBeUZKBh5oTj88EXDvRqCmOdOhma-4HKVO1K4bX35wiKz7IIrshwKXt1RfX0i-_VlawlR64VgAU2rEACrnBNySZIccMW20Sg0efxaAyC_nOhJfBo7soYZ7CjIMwyEt0yvQyAQDKRCZ-G98AOdFuhrlTppB59XLQC_EJJ3N9ZvPhhlfys7xJr3-dd8AT-dBUpl_xEqmHar7qoA50CUzPhvB5nEn1jEIW7xsw6PVmRv9GWK8AFjmgeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه ای قرار دارد و با توجه به بیش-فروش بودن تکنیکالی، امروز احتمالاً یک اصلاح رو به بالا در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20453" target="_blank">📅 11:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20452">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حملات ایران به بحرین و کویت1!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20452" target="_blank">📅 01:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyNbG5rfEuhwX7t0bQF3pMfBdD0IMRrGMvwExCD_inaMJGLqoTGA3_DscsEmIv_5_wqIYSEY-auCZ93MHOVFIoGCXItIjtpBCqbBs1diO_WRbRiZ94laOKWc7xJAWWUapDg6tmp00WxIGYsPP2Q-pEbZV-yrJBPP3dXuJHVMhSuVgUZK2X0vJlC8uHaur4VyMjpsZIgwG1_fXwn-TeAVEU4wpI0op3cxg8ajVQtO1p-5vyqysAx3BoCrfbZTvvKuIYe--PAtzFP1EsXKl8G5VfLzPPyaK-l_SHBOsDndun3mOrArJQJ23pQUnNXNRQfeWDaqLAh96FfuWfjNvO9WKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سپر آشیل»؛ ورود یونان به عصر دفاع هوایی چندلایه   یونان و اسرائیل در ۳۱ اوت ۲۰۲۶ قرارداد تاریخی «سپر آشیل» (Achilles’ Shield) را به ارزش حدود ۳ میلیارد یورو امضا کردند؛ توافقی که آن را می‌توان یکی از مهم‌ترین پروژه‌های دفاعی مشترک دو کشور و نشانه‌ای از تعمیق…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20451" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">- یونان و اسرائیل در آستانه اجرای توافق‌نامه‌ای به ارزش ۳.۱ میلیارد یورو برای برنامه «سپر آخیل» قرار دارند که در آن سامانه‌های اسپایدر، باراک MX و اسلنگ داوید با زیرساخت‌های دفاعی موجود یونان یکپارچه خواهند شد.  این شبکه مبتنی بر هوش مصنوعی برای مقابله با…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20450" target="_blank">📅 00:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20449" target="_blank">📅 00:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بالگردهای ارتش آمریکا برای انتقال زخمی و کشته های خود در اردن به پرواز درآمده اند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20448" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">#WHEAT — D</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20447" target="_blank">📅 00:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnK8y5hXlQ9H78IFc2AL4dAK9BjlKBxUzd0VVZsD9UQsE-8vWyoYI45l9tEdMALVr2caceiZw2ip2P_6hlZg-sQKrDku6HFr8BFklnZ7nEhgaKU6w3pj9wdKe1q_7m_wcCDmtGayJOl9lM-gR5k2Y8jR_S1GIRelZalOXRSEwS1je44SI2CzupDItRFjnZtzbeHOYnyhdpLmpy0jruDTC9FfevdC2trUI_gpNJT3euDIfwY_RYZ4KHIp4wn7iIZ-kM4hAgwqYISF1jRgGaqWLXhaJmPHny2LAAc8llKa36PsEyGKbotjoGYSTxcmM7KQEbFVvYM_RczHWTavJXTnJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20446" target="_blank">📅 00:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr0VI5iGuCIUXNbsI57altuhE_q4z5bN7q4JMFK5I4SXvpM0wZHd6dIYv-dDvL7Kg13A17Ml_dfVch01eJg0ymZ0pF6TFrpmR2xvpUbBfQOlP64J-XgmAOL_YbSYCGHeVXpeA4WjBWBAeAWw_Dz7pbsFmrqWvj--33WJmH4GRx1EMSo-LQqp8igANl_fM8Anz0Dp56iZlH08A9QyHF74tUMzTXpo-v9ZbQgNyjzT6uFQyA-7j_WInwqjM3rwrVbFZP_eBnRbp8k-vD2H9zucBzJxTM3ZmdtFciwXOSsi86cS-ykpql_qykEbrSpc9b3mAzdOdS5MdwYPPauDvgnMOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42fd12b2d1.mp4?token=vtJXnC-V9xK0yoV4QvMWn_QsHGD7-AevZ-A0o7c3QZB7nu8fjYw0Ynz7yMqyvQoaojka7wasLTAr8q_FF8JzXrGoK4q4sJQbUTp7LGw6DNYoc2tsU1SOUEk5eoRfuj0XWftiF3kfJZUIIlYXsehw1gQRfSlV9NYnB_94-7D184Iau6Wl41C34P7fj1hX5_tuSEhLagnA_l8liT_Y4IlMQEZ9pTXCFgGJknLnxwqDyqn5zVr-IbcAZwzmyxsl8lIVRGWsedKKFpHxkC5-9dUej0xoWDyRc4Yd93dqQKotUDIgn00gIC3KCmOGb4FLtXxtdWf0tlGBCY7Dl1ZqLM6FBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42fd12b2d1.mp4?token=vtJXnC-V9xK0yoV4QvMWn_QsHGD7-AevZ-A0o7c3QZB7nu8fjYw0Ynz7yMqyvQoaojka7wasLTAr8q_FF8JzXrGoK4q4sJQbUTp7LGw6DNYoc2tsU1SOUEk5eoRfuj0XWftiF3kfJZUIIlYXsehw1gQRfSlV9NYnB_94-7D184Iau6Wl41C34P7fj1hX5_tuSEhLagnA_l8liT_Y4IlMQEZ9pTXCFgGJknLnxwqDyqn5zVr-IbcAZwzmyxsl8lIVRGWsedKKFpHxkC5-9dUej0xoWDyRc4Yd93dqQKotUDIgn00gIC3KCmOGb4FLtXxtdWf0tlGBCY7Dl1ZqLM6FBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20444" target="_blank">📅 00:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20443">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcL0YYIsGRlemPVUwrpHzYXotZJp5w_jfqldwE6Eya0fKd3Z623UxFG0sLeP0K5BJWgNI0ydZT4AfZs5n_Hdm8Vlf-Onhls3kxN5fJkZcOiaMpb1iOZhk_7udiKJPoypo6Z2H1ZzKoOTAD9NnpXWujSUfssjieLVO_wm46NVN5pM_R6IF06PGwe80rpoWv39tuXVU3b7_CZnxO8G8sCw7O8sAw6uiVjI9OFU7OIoLgA3pe00ceuwJvil-8xKL8r9U5cA0d5cIDUQ-Qw7jVhrKpXqav_zN3__P5kxodUwMdRNfw33I1IdSyeAEIqF6eR2yLVc3hF0u1IKx_OXet1nPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفاً یک نفر لفت بدهد میخواهم معنی 10666 را از آرش بپرسم. ممنون</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20443" target="_blank">📅 00:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O10FE2n1jbMM8_DFsrxptOLlmgR6IXbSn7JBFvz2rpje06XAaXXKGM9YQcKT-dKU5DqLZBeTamDqvpF-mj4m_A8RRNadySknaJpLfb7h7bgbBu7INbAipo7BxRzMyX0opFN5_Aljh6d6afMF4j1EfgGcrLRf_DaSEFLbMKprOXv9cZoOIoHYx6HCg4v0D-cBUl07NETfVLDC1Dqyj-Ao5epiQsU8GLRZsRdG3j18W5_z58p-GCEGnhktcYkfPZCCaievhdOOoveNXP5EqJi57_KbR61mohSmIv91v7MuL-6DbVfEdisZX9Q6xVEFbcdzlj2zp3ZVpP_8qKLHBUfDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفاً یک نفر لفت بدهد میخواهم معنی 10666 را از آرش بپرسم. ممنون</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20442" target="_blank">📅 00:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
🔹
ملت قهرمان و بپاخاسته ایران اسلامی،
ارتش تروریستی و شکست خورده آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام با حمله وحشیانه به یک منزل مسکونی در سیریک، محل مجلس عقد دو جوان پاک را به خاک و خون کشیده و با به شهادت رساندن و مجروح کردن نزدیک به پنجاه نفر از مردم عزیزمان خاطره وحشیگری مدرسه میناب و ورزشگاه لامرد را زنده کرد.
🔹
رژیم کودک‌کش آمریکا در این حمله جنایتکارانه یک بار دیگر با به شهادت رساندن چندین نفر از جمله یک کودک، عمق کینه‌توزی و دشمنی خود با مردم ایران را آشکار کرد.
🔹
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)"
با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه
، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
🔹
عملیات انتقامی نیروهای اسلام
ادامه دارد
.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20441" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">باز ما یک سفر آمدیم همه چیز به هم ریخت....حتی سفر درمانی ما هم بی عوارض نیست چه برسد به تفریحی</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20440" target="_blank">📅 00:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ساعتی قبل یک خودرو وارد تجمعات شبانه در خیابان اقبال لاهوری (مشهد) شد و جمعیت را زیر گرفت، چند تن نیز کشته و زخمی شدند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20439" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20438">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔹
موشک بالستیک سپاه به سمت اردن، که از اسرائیل مشاهده شده است
⭐️
@AkhbareFouri</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20438" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20437">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار فوری | اخبار جنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10aa2a3f52.mp4?token=CLXXMUpdaljEbm-Pg8eMG2T5-T6HEYdXzHABG_L5h-2eYFQMDCL8Kd6g_xXtdDA7gKuDN5zajXoUU8y_DG0fc-720mCPuf2rqZPJvlZN5neF5RXr0VZePjS5R0q4XUby77e1-8vQ7L2VOkoWugMqahIJMyC89-MIanIrWA75cEKgrcNDDsCfEaRQG_cg4hFGwKdFNql3M3oNGRfR4dqh2VZBc55sg0_DoG0cTiFVgcSkTf5J9gRo1WpEtklN269OEuGvg487M94eQbos5xfWb3QxZeuen-6vfhjrd9OiddUJc88_riJxDD1Bnw3c1dAb-y8sGci8nqb9GcTVka-zXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10aa2a3f52.mp4?token=CLXXMUpdaljEbm-Pg8eMG2T5-T6HEYdXzHABG_L5h-2eYFQMDCL8Kd6g_xXtdDA7gKuDN5zajXoUU8y_DG0fc-720mCPuf2rqZPJvlZN5neF5RXr0VZePjS5R0q4XUby77e1-8vQ7L2VOkoWugMqahIJMyC89-MIanIrWA75cEKgrcNDDsCfEaRQG_cg4hFGwKdFNql3M3oNGRfR4dqh2VZBc55sg0_DoG0cTiFVgcSkTf5J9gRo1WpEtklN269OEuGvg487M94eQbos5xfWb3QxZeuen-6vfhjrd9OiddUJc88_riJxDD1Bnw3c1dAb-y8sGci8nqb9GcTVka-zXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
موشک بالستیک سپاه به سمت اردن، که از اسرائیل مشاهده شده است
⭐️
@AkhbareFouri</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20437" target="_blank">📅 23:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20436">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه کویت مون نشه؟!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20436" target="_blank">📅 23:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20435">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مرندی ذوالاکتاف:
با توجه به اظهارات ترامپ و بسنت، به نظر می‌رسد که روزهای رژیم‌های خانوادگی عرب در خلیج فارس به شماره افتاده است. آن‌ها نمی‌توانند از جنگ پیشِ رو جان سالم به در ببرند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20435" target="_blank">📅 23:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20434">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جهت نوسانات رو شاخص درست تشخیص داد (رو به پایین) اما شدت ریزش قیمت با تحلیل ما سازگار نبود.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20434" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20433">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWjdajDm6k1-ZCNN3Xis9Xc1AQr3Sy3OM1pyEphRuwCBOqrkFjKRh70ws8fZbExUNIWtOdnLqqjcqENUMJxvUeKFuJlZasuADYNiax4hvJ8elwXOvuubUGoinkIUm2HXu-180DW0vIhHL4C6ojZUagwHeK9tuhz4JtSb62GK262ywFWc-2zvoenF9C1lahA-ZtLz0E34fU12EdG1ZIRzb3GRge8DvN0AoY3upHFXIQCHHC1_kTqLl11dgu9iNXWUnoyiW3wModzRNpJQ9783pKRseE3a0OMjD7WyTbJqs7WSi15RZEQrHQgROxfWsJS9HKJwVu3J5aUNn94FBWRQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه بالا قرار دارد و بازار رنج و کم نوسان پیش بینی می شود.  با توجه به روند عمومی نزولی در 1-ساعته، فروش در سطوح مقاومتی (4477) بهترین راهبرد است.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20433" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20432">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شلیک موشک از تهران!</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20432" target="_blank">📅 23:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20431">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پزشکیان:   همهٔ اعضای شانگهای بدون استثنا تجاوز به ایران را محکوم کردند</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20431" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20430">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پزشکیان:
همهٔ اعضای شانگهای بدون استثنا تجاوز به ایران را محکوم کردند</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20430" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20429">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک درس دیگر هم این بود که در جنگ با آمریکا و اسراییل، باید بیشترین موشکها و پهپادها را توی سر‌ همین جهان اسلام زد تا بهتر بشود جلوی شیطان بزرگ ترسمان ریخته بشود.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/20429" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20428">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حمله ایران به اردن</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20428" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20427">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">معاون سیاسی و امنیتی استان هرمزگان: در حمله به یک مراسم عروسی در سیریک دو نفر شهید و تعدادی از افراد نیز مجروح شدند.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20427" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20426">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سقوط یک پهپاد MQ-9 آمریکا</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20426" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20425">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اگر آمریکا باز هم به تجاوزاتش ادامه دهد، خمین را با خاک یکسان خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20425" target="_blank">📅 23:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20424">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمله آمریکا به همون همیشگی!
سیریک
!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20424" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20423">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجار در همون همیشگی !
اربیل
!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20423" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20422">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجار در همون همیشگی !
اربیل
!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20422" target="_blank">📅 22:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20421">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حمله به عسلویه!</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20421" target="_blank">📅 22:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20420">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گفته می شود بقایای موشک در خود خمین فرود آمده</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20420" target="_blank">📅 22:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20419">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آژیر خطر در قطر!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20419" target="_blank">📅 22:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20418">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpfEwmTJlQ4h8S3WL74FjEP_Ul5feNtUQnW70prMiY-NkNuUPcMrKRSdO7ZkbNGbVJm07oFGw0XwflMTXVNzS1VQf9woc2EHbgz705Ni8giWq-S66Gsoz3zEQP1LE2MMehUx0GUbiy3YGVTKDiaQishJDDUiX7KTsGW0ycTzV5wce_Xd3QWyHaPe3plKDyTgqZa72J3TnvIt5iKU9tn8RWBHMwwkCJbyC1kLMU1JBv41J5-_10sFgfm3ttm2ybwW3DeI8SDC8kYyvLo7mt2M8nx8HcPItDxiDGTbZVBjtidUuHF8NQDPP28-qCs1mI2sS5o94hpqWyQx2HCf3VN4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن دو هواپیما نیستند پس احتمال حمله به تهران هم هست.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20418" target="_blank">📅 22:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20417">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">‏ترامپ:
حملات جدید آمریکا سیستم راداری ایران  و کارخانه های تن ماهی را هدف قرار داد
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20417" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20416">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حالا که همه چیز را دادید رفت، دستکم به رستم تهمتن بگویید دیگر نزند!  کور شد بدبخت!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20416" target="_blank">📅 21:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20415">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20415" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20414">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دقایقی پیش فرودگاه جیرفت مورد حمله هوایی قرار گرفت.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20414" target="_blank">📅 21:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20413">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">منظورم موشکی است که از خمین بلند شده بود.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20413" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20411">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">موشک های بالستیک از ایران شلیک شدند</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20411" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20410">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  «مجازات شدیدی در انتظار متجاوزان است.  آمریکایی‌ها به خاطر حملات جدیدشان پشیمان خواهند شد.»</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20410" target="_blank">📅 21:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20409">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
«مجازات شدیدی در انتظار متجاوزان است.
آمریکایی‌ها به خاطر حملات جدیدشان پشیمان خواهند شد.»</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20409" target="_blank">📅 21:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20408">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ:
«ایالات متحده همین حالا در حال حمله به اهداف ایرانی در نزدیکی تنگه هرمز است. این حملات گسترده و قدرتمند هستند و در واکنش به تلاش ناموفق ایرانی‌ها برای کارگذاری مین‌های دریایی در تنگه هرمز انجام می‌شوند؛ تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد (تمام مین‌ها کاملاً پاکسازی یا منفجر شده‌اند).
همچنین در واکنش به شلیک هشت موشک از سوی ایران به پایگاه نظامی ما در اردن که همه آن‌ها با موفقیت سرنگون شدند.
اگر کشور شکست‌خورده ایران در واکنش به این حمله کاملاً موجه، اقدام تلافی‌جویانه‌ای انجام دهد، بار دیگر و در سطحی بسیار شدیدتر و گسترده‌تر هدف قرار خواهد گرفت؛ اما این بزرگ‌ترین حمله از همه نخواهد بود. بزرگ‌ترین حمله همچنان در حال آماده کردن است و هنگامی که به پایان برسد، چیز بسیار کمی از جمهوری اسلامی ایران باقی خواهد ماند!»
— رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20408" target="_blank">📅 21:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20407">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دور جدید حملات آمریکا</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20407" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20406">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تسنیم:
برخی منابع از شلیک موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه خبر می‌دهند</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20406" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20405">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">– گزارش‌های تأیید نشده حاکی از آن است که موشک‌های زمین به زمین دیگری، احتمالاً HIMARS یا ATACMS، از بحرین شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20405" target="_blank">📅 20:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20404">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امروز ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده شروع به حمله به اهداف نیروی دریایی سپاه پاسداران انقلاب اسلامی (IRGC) در ایران کردند.
این حملات پس از تلاش‌های اخیر IRGC برای حمله به کشتی‌های تجاری در تنگه هرمز و علیه نظامیان آمریکایی مستقر در منطقه صورت گرفته است.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20404" target="_blank">📅 20:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20403">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به نظرم نیازی نیست چون خود آمریکایی ها هر هفته چند بار پیش دستی می‌کنند</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20403" target="_blank">📅 20:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20402">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">— سفارت‌های ایالات متحده در اسرائیل، قطر و عراق هشدار امنیتی صادر کرده‌اند و از آمریکایی‌های ساکن در سراسر خاورمیانه خواسته‌اند در میان نگرانی‌ها درباره تشدید بیشتر منطقه‌ای، «هوشیاری بالاتری» به خرج دهند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20402" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20401">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">— انفجارهایی در بندرعباس، سیریک، قشم، چابهار،لارک، جاسک و میناب گزارش شده است.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20401" target="_blank">📅 19:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20400">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20400" target="_blank">📅 19:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20399">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دلار فردایی تهران
⏳
213,600 فروش
🔴</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20399" target="_blank">📅 19:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20398">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رئیس مجلس ایران از شهروندان خواست مصرف بنزین را کاهش دهند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20398" target="_blank">📅 19:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20397">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزیر راه:   رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20397" target="_blank">📅 15:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20396">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر راه:   رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20396" target="_blank">📅 15:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20395">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزیر راه:
رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20395" target="_blank">📅 15:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20394">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دلار فردایی تهران
⏳
213,600 فروش
🔴</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20394" target="_blank">📅 13:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20392">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏نبویان:   اکنون بهترین زمان برای حمله پیش‌دستانه به منافع امریکا است</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20392" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20391">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏نبویان:
اکنون بهترین زمان برای حمله پیش‌دستانه به منافع امریکا است</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20391" target="_blank">📅 13:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20390">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">میراث مقاومت: پیوند اسماعیلیان، دروزی‌ها و مبارزه ملی ایرانیان — بخش 1   مقدمه در عصر جدیدی که در نخستین دهه هایش هستیم، یافتن متحدین استراتژیک امری است بشدت حیاتی و تعیین کننده پیروزی یا شکست ملت ها در آوردگاه جهانی. برای ملت ایران که به قولی دچار یک «تنهایی…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20390" target="_blank">📅 13:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20389">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20389" target="_blank">📅 12:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20388">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
آمریکا در جهت ضربه به تمام فرماندهان سپاه آماده می شود ! عملیات روانی همزمان با برنامه جدی برای ترور !
⏺
در لیست تهیه شده توسط دپارتمان جنگ ایالات متحده، فرماندهان بسیاری از نیروی زمینی سپاه، قرارگاه های این نیروی و حتی فرماندهان سپاه های استانی و فرماندهان…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20388" target="_blank">📅 11:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20387">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⚔Iranian Militarism⚔</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFxHuMuKIPTtvFWBv8ICiBHNBuITxNk78zFLJY8JC2RqOR0oTCh7lslwOE7L-afjd-SkflhTiQ5d94WgYkuqZBhmgXPtIbquXEOh1V8mnjzXL5rvCb2UpkGEZ7h2ZKE3B_VEh_w381kVE0dmDl9TV0YO0UXUtYdTthmZh_Zxr9fiF8Cs8gD8heM-U6TFLsog4WZY13oOOoCzc4aCS3R6B2W1G8tJM2vgbk8nD2f2juI0woC9nNojHOlcQcrNZn6oE1N9IPRJojSXNsPnfRJ17OQ2gkX7r1v08UDVtEzHfslb_yjkVjFmaWq_C1tWJON_6wOch_tlsoKdElLK8-FFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آمریکا در جهت ضربه به تمام فرماندهان سپاه آماده می شود ! عملیات روانی همزمان با برنامه جدی برای ترور !
⏺
در لیست تهیه شده توسط دپارتمان جنگ ایالات متحده، فرماندهان بسیاری از نیروی زمینی سپاه، قرارگاه های این نیروی و حتی فرماندهان سپاه های استانی و فرماندهان نیروی دریایی دیده می شود! حتی سرپرست فعلی سازمان اطلاعات سپاه نیز در این لیست می باشد.
⏺
هدف آمریکا از تهیه این لیست اجرای یک عملیات روانی و همچنین دریافت اطلاعات دقیق از وضعیت این فرماندهان می باشد. همچنین به نظر می رسد آمریکایی ها با انتشار زودهنگام و غیر دقیق این لیست عجله در دریافت اطلاعات دارند .
⏺
گزارشی مبنی بر نشر این لیست در مجموعه های خاصی وجود دارد که مرتبط با اعضای نیروهای مسلح هست، نکات بسیاری وجود دارد که فکر میکنم اگر بگویم برای خودم دردسر ایجاد می شود پس فعلا از گفتن آن پرهیز می کنم. اما جدی بگیرید اوضاع را !
Join us |
@Iranian_Militarism</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20387" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20386">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⚔Iranian Militarism⚔</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwjCF97E6ts1rLnBSs80zmeWk_weQovWhBMwDu0vb7wnnoT-ad0C4ztirDRkpWqi52q0P7dk-3e1VwnMMTMsBbGCUTw6h1j4dFu_XSuCEZi86zRSmDaYpdNsysTgauP2ZRjLJ44JPErNQh48EVbh5Rv-rdX7uFErCQX2ZF-hDuDpx748JjNVkLsCOfuJlRVJQiUlUMTtn6RVyjkrGbJrbj1nxf2hJCNBwhmbyniA6gD93i09wjA11HLmpped7Og8yfxjPl-tBeN0s37PZxtIukrc3npr_kX9Y8nJiv06Odu-vxzwF_qz5zXVJ1AuHbDRCEZ6kzoHk3VjwOJUfwZ9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر سردار حسن زاده در صفحه وزارت جنگ آمریکا به عنوان فرد ترور شده !
🚫
دپارتمان جنگ ایالات متحده سایتی برای دریافت اطلاعات از برخی فرماندهان ارشد سپاه تهیه کرده است! در این سایت لیست قابل مشاهده است که صرفا به چند فرمانده به صورت پراکنده می پردازد، نکته جالب اینجاست روی تصویر شهید خادمی علامت ضربدر قرمز خورده است به این معنی که به شهادت رسیده است! حالا جالب تر اینجاست روی سردار سرتیپ حسن زاده فرمانده سپاه محمد رسول الله تهران نیز همین ضربدر دیده می شود!
Join us |
@Iranian_Militarism</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20386" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20385">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krjRA0t9RxuE1ZPIgyE6VoD57AGUOgwbicn5uhAI1Tk6RXQfrnpyPwYMRe5bV7s_LJheRMf_LfdSrohw8wCgrDmPlmStJrnUyJUTQUhPna61radCoVYvXifb7rHUeNDSJJTuCfdZk14p_Toh7MWHzsk-uUUY6ITY5ZTgpCVm5dneff8ogDUJ7apPxr9NO3Pa-ZAHgRq9vrOoHgQcYoLOKtDNj9mDs668XM_kjjB-A_wm0r8OeZ04ACME3xqi-EhDzA08BqnE3Hm68OZBoBHcbi4XKejkfJLSCJMBQ6mN-qhxCIeMbeTFQCO6_e6FTwxtf4Gvu4WXM-p5jqGFIFQphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه بالا قرار دارد و بازار رنج و کم نوسان پیش بینی می شود.
با توجه به روند عمومی نزولی در 1-ساعته، فروش در سطوح مقاومتی (4477) بهترین راهبرد است.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20385" target="_blank">📅 10:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20384">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این چیزی که ما اکنون تجربه می کنیم عملاً نوعی «تجربه نزدیک به زندگی» است.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20384" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20383">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجار در سیریک</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20383" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20382">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ایران یک تانکر نفتی سعودی را در تنگه هرمز متوقف کرد.
بر اساس گزارش خبرگزاری فارس، یک تانکر نفتی بزرگ سعودی در حالی که از مسیر جنوبی تنگه هرمز عبور می‌کرد، متوقف شد.
ظرفیت این تانکر 2 میلیون بشکه نفت است.
طبق این گزارش، در حالی که این کشتی از تنگه عبور می‌کرد، ناگهان سیستم شناسایی خودکار آن فعال شد. فعال شدن ناگهانی سیستم AIS نشان می‌دهد که یا به این کشتی دستور داده شده بود تا موقعیت خود را اعلام کند، یا اینکه در شرایط اضطراری در تلاش برای اعلام حضور خود بوده است.
امروز، سازمان UKMTO گزارش داد که گزارش‌هایی مبنی بر وقوع یک حادثه امنیتی مربوط به یک تانکر نفتی دریافت کرده است.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20382" target="_blank">📅 00:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">- یونان و اسرائیل در آستانه اجرای توافق‌نامه‌ای به ارزش ۳.۱ میلیارد یورو برای برنامه «سپر آخیل» قرار دارند که در آن سامانه‌های اسپایدر، باراک MX و اسلنگ داوید با زیرساخت‌های دفاعی موجود یونان یکپارچه خواهند شد.  این شبکه مبتنی بر هوش مصنوعی برای مقابله با…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20381" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20380">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBMrEFO90AsUadKnbG82gY6VWrhB5izjso_9opL8hyJQH6fE98z24kePBEkT_QzOT5y7k7TzzD-18W2rFvdDTx7tQnIhMfc-znhUfNu65N7OoVIlZIS97GB7BNDkYBxmXHJ3xxrzDRcMRLxyWeuZNw8s1vMVsGipZmsJlz8K-T2vI6Z6cTZG87GsJLEkq0J3NP-YOna9ZIMo0iBgxp7A9c03gB_DSsGC7sl3oC5cesYuyBomb54heeYMm3KTSzHb_IlpXMZSuEtMP7wfdksoVK-nqcQpLw4ZN_FUYfhZP5tMDtMyqVFj8fbew0Roe9d7cj320hV8YDwSEaqM4WvMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو بار رشدهای عالی را در طلا شاهد بودیم.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20380" target="_blank">📅 00:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20379">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش های اولیه از حمله موشکی آمریکا به یک نفتکش ایران در اقیانوس هند.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20379" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20378">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حملهٔ مسلحانهٔ عناصر پژاک به اهالی یک روستا در مریوان کردستان
در جریان این حمله، تعدادی از شهروندان محلی زخمی شدند.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20378" target="_blank">📅 00:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20377">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20377" target="_blank">📅 23:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20376">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SE3e6Hyqmxh9kBtIRiCsqtzlCvgpdg2ttH-ZVPhQj1_d7wNjA3wKXy1uMjm6LJuEB8Br7tCsCTQ_TSWqBGSXXVB8FDHrytJYAwEXfxFjb1CihgqQLveQ8RjvdDCs26xFPoUlwCGioUFyqm7YYcoJcTjZB6E0pXzmGVMl0dTT8FLIO3UzZhJoX_Nv24l9LC75nSwrjCQRGfKH1sUXStRve3qYUI7MkTA2J9gSwKTWpTex9AAnpSwBoMETAV7LcC5NnPo9DmRGeFkxjotSW3E4eMzhGDV2jo8I5L9J-uNkWFEBs2eqtBm532qnIHEJvEfEqk3xsnvQbQeYUDd9i_xxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/20376" target="_blank">📅 19:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20375">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دادگاه مرکزی کیفری عراق، امیر رحیم جبار لازم، عضو کتیبه‌های حزب‌الله وابسته به ایران، را به دلیل گروگان‌گیری روزنامه‌نگار آمریکایی شلی کیتلسون، بر اساس قانون ضدتروریسم به ۱۵ سال حبس محکوم کرد.
کیتلسون در ۳۱ مارس در بغداد ربوده شد و پس از حدود یک هفته، در ۷ آوریل آزاد شد.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20375" target="_blank">📅 19:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20374">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسکات بنت:
به دلیل محاصره، تنها 30 میلیون بشکه نفت ایران روی آب باقی مانده است - بنابراین حتی اگر آنها بتوانند از چین پول دریافت کنند، این مقدار تمام خواهد شد.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20374" target="_blank">📅 19:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20373">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شمار کشته های حمله شب گذشته آمریکا در لارک به ۳ نفر رسید
خبرگزاری تسنیم:
در پی حمله شب گذشته آمریکا به نقطه‌ای در جزیره لارک، ۲ نفر به شهادت رسیدند و چند نفر نیز مجروح شدند. مجروحان این حمله برای مداوا به بیمارستان منتقل شدند که ساعاتی بعد، یکی از آنان نیز بر اثر شدت جراحات به شهادت رسید.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20373" target="_blank">📅 18:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20372">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«ایران تحریم‌ها را بسیار جدی گرفته است. رهبران ایران از وضعیت اقتصادی کشورشان شوک‌زده شده‌اند.
ما شاهد صف‌های ۳ تا ۴ ساعته در جایگاه‌های سوخت ایران هستیم.
ایران به دلیل از دست دادن توان اقتصادی خود، به اقدامات نظامی روی آورده است.
می‌خواهم از اتحادیه اروپا بابت حمایت آن از عملیات موسوم به «Economic Outcast» تشکر کنم.
خبرنگار: آیا بازه زمانی مشخصی برای فروپاشی اقتصاد ایران وجود دارد؟
بسنت: لازم نیست اقتصاد ایران فروبپاشد؛ فقط کافی است حکومت ایران به خود بیاید.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20372" target="_blank">📅 16:51 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
