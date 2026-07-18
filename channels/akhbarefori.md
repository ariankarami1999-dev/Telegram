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
<img src="https://cdn4.telesco.pe/file/XsC6sW3Ug4EOkokJQpk_lMnxVg9_YQ0I4pzD-VZsv1pRr7dvE1TahgD4Brr_EZbxf47ZbsGbKd6K3AgHnImN6wUt4VZ8nGqlOmHEzKTUptt3oEB0AKU-HeL5Y3YLeB2LZFRCGsSul7ZKgIuELS1FMsDvFADoh8vOcBlxewx5omDIpF3zoCBX5L24X2lIlHRzrauF6-Oy_y-TaId4HRaV0aZ_BhaWIQFaZfbWE-ppm8oatz-G-iUXwNWAN2EOByoXic-e4iwxL3e4J-yaM24SeLM9YrsMiMBJ1oDPCdQG5FNx56XGii6V83gZKJ4CIEfKrnDOWIzqkTakku2YyHnuVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.28M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 02:09:42</div>
<hr>

<div class="tg-post" id="msg-672795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا مدعی انتقام از ایران به خاطر سربازانش در اردن شد
🔹
ارتش تروریستی آمریکا در پیامی که دقایقی قبل منتشر شد، ادعا کرد: «حملات جدید به ایران با هدف مجازات فوری سپاه پاسداران به خاطر حملاتش علیه نیروهای نظامی ایالات متحده در اردن انجام می‌شود.»/ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/672795" target="_blank">📅 02:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0813f70fda.mp4?token=WmjN64--QkJ9vwdaRMcIeWRdHMvG3yBOkdo3o16qShTV9L6t9UR071gRgqcHtk0dTmZqlSkstifAWsb6jLkzviRnJePlRnW80Dn2MS1-o2ejMHJZtxUIV4VUSIHlHRZInFQJdFttx2G1k8nZt0qMYg5Veq4HtcEw2uMyBmBEKK3FkxgaQR7RzOGBhEUeG5qWtNfUCZevfaSdIE-m8PmT2oPPQwpjmJG6h3CZqZkD8SH3iWXMo9b8_NrT65U5oUnoTe1LS-7b7FwtCh41pFYDcMD0GJJs-TWWXX5ruVO78t3ib6mYrNj47R4cIuqvtUWz_rjNz_Xe12LR0xy0LAiVeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0813f70fda.mp4?token=WmjN64--QkJ9vwdaRMcIeWRdHMvG3yBOkdo3o16qShTV9L6t9UR071gRgqcHtk0dTmZqlSkstifAWsb6jLkzviRnJePlRnW80Dn2MS1-o2ejMHJZtxUIV4VUSIHlHRZInFQJdFttx2G1k8nZt0qMYg5Veq4HtcEw2uMyBmBEKK3FkxgaQR7RzOGBhEUeG5qWtNfUCZevfaSdIE-m8PmT2oPPQwpjmJG6h3CZqZkD8SH3iWXMo9b8_NrT65U5oUnoTe1LS-7b7FwtCh41pFYDcMD0GJJs-TWWXX5ruVO78t3ib6mYrNj47R4cIuqvtUWz_rjNz_Xe12LR0xy0LAiVeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرانسه در آستانه کامبک زدن، گل سوم فرانسه به انگلیس توسط امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
3️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/672794" target="_blank">📅 02:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
منابع عراقی از حملات سایبری علیه شرکت‌های گازی اماراتی و آمریکایی در اربیل خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/672793" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حملات نظامی دشمن آمریکایی به حوالی سیریک
🔹
در ساعت ۱:۳۰ نقطه ای در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت.
🔹
در حملات جدید آمریکا به سیریک هیچ مصدوم یا خسارت به زیر ساخت های مسکونی و تجاری  گزارش نشده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/672792" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672791">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سنتکام: به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه اهدافی در ایران آغاز کردیم
🔹
امروز ساعت ۶ عصر به وقت شرقی آمریکا، نیروهای آمریکایی به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/672791" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672790">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
منابع عراقی: حملۀ پهپادی به کنسولگری آمریکا در اربیل ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/672790" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سنتکام: به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه اهدافی در ایران آغاز کردیم
🔹
امروز ساعت ۶ عصر به وقت شرقی آمریکا، نیروهای آمریکایی به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/672789" target="_blank">📅 01:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672788">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
منابع عراقی: حملۀ پهپادی به کنسولگری آمریکا در اربیل ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/672788" target="_blank">📅 01:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=tfzwm9Fxa01blINuPwP8JmcciD-oe0v7M2lK9yvdtB_BFQTnI7UfBgVC_3wWW1rW5G9_YBLsvO2v9H51kkX7OF09Bu0JQkuTzytnZ0UrXWbn7RvGrXYZr6eOdRhcQrm0dl6yt0jJe5tIfB2ua2BONrMgrRgNJDzSzATyNALxb1TCu-4XRKvz6JqSr3g_hYwBzNb_vuFNfVeMp_KPc_7CA__vROWXVO6ZWTAraGct7IKywAy33qxAtvQuoNaSeUy4A9goOnJnWAkm2LEC-9_JtoevkKTFJJvyWoigmczOtTGvKkTaH3cCMb-YAQhSDAkn7-IOHDPGEzkLYW-YBAINXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=tfzwm9Fxa01blINuPwP8JmcciD-oe0v7M2lK9yvdtB_BFQTnI7UfBgVC_3wWW1rW5G9_YBLsvO2v9H51kkX7OF09Bu0JQkuTzytnZ0UrXWbn7RvGrXYZr6eOdRhcQrm0dl6yt0jJe5tIfB2ua2BONrMgrRgNJDzSzATyNALxb1TCu-4XRKvz6JqSr3g_hYwBzNb_vuFNfVeMp_KPc_7CA__vROWXVO6ZWTAraGct7IKywAy33qxAtvQuoNaSeUy4A9goOnJnWAkm2LEC-9_JtoevkKTFJJvyWoigmczOtTGvKkTaH3cCMb-YAQhSDAkn7-IOHDPGEzkLYW-YBAINXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع ۵ انفجار در اربیل؛ سامانه پدافند هوایی کنسولگری آمریکا فعال شد
🔹
بر اساس این گزارش، هم‌زمان با وقوع این انفجارها، پهپادهایی نیز بر فراز آسمان اربیل در حال پرواز مشاهده شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/672786" target="_blank">📅 01:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672785">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d35cb592f.mp4?token=LgqikZTzA_L_AKQSNAw7j6zilX4SGosAvHMhhduOm6eqKz_sdNJuMB8Oh3jmUmNQShhalPzzI5uT6qsCxe_GAKR8ou9uK6jKSDLczSZ4PUpcp_qqcl5-vZJL4bhJFPVH2QLBCWL_EAimouMNvMMKFE_eJ8QEjjmNIErgT08PFr5x28Z6X9V3aF24CA70FyXn-rdbyHC4uhfASXWKsflXrCMsscb-1X_GpeyIP6pKeOigLnh4JvLOIYCu3_x9TwsncfqNhcYdYg_SfazUV-q5s7PYKM02uoHxIfMW4nKbhI2ZZmHbbcuZxeQcz1wlwKfeSapWS2Gn-TMtetMYtG6FJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d35cb592f.mp4?token=LgqikZTzA_L_AKQSNAw7j6zilX4SGosAvHMhhduOm6eqKz_sdNJuMB8Oh3jmUmNQShhalPzzI5uT6qsCxe_GAKR8ou9uK6jKSDLczSZ4PUpcp_qqcl5-vZJL4bhJFPVH2QLBCWL_EAimouMNvMMKFE_eJ8QEjjmNIErgT08PFr5x28Z6X9V3aF24CA70FyXn-rdbyHC4uhfASXWKsflXrCMsscb-1X_GpeyIP6pKeOigLnh4JvLOIYCu3_x9TwsncfqNhcYdYg_SfazUV-q5s7PYKM02uoHxIfMW4nKbhI2ZZmHbbcuZxeQcz1wlwKfeSapWS2Gn-TMtetMYtG6FJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرانسه به خودش آمد، گل دوم فرانسه به انگلیس توسط بارکولا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
2️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/672785" target="_blank">📅 01:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27409c54f4.mp4?token=NJMLnE0deph-dCcBqD8qBhNliBTR9GwZcBzRlOdObshLFJJG2aAYsa_Om0A_6sX50K2hYcf8SWRCfgjVIyEVg_Z0lfG-wMbUqwb4Plrs3WFde8z41RsBYdrUshznlulI7piO7qJ6Tm9YuG-u1bZeGeAZIMlk5CKgdF8LGdH-0GN1Q7Dg0p1ZNFgyY7kpl3UNL0owsNPGcp4yIKPPT6ebrf8LO3ux1kmppHioSFCuP-IpOy_78PCzSLsH7HsrXVl16ZskZbX_11_7lfzHu8REEmxHrVyeL9H5tBGXgxcxrLDMmzaBMPoH8adet43MFnnW5rRgnBFeuDJccsztvNCfow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27409c54f4.mp4?token=NJMLnE0deph-dCcBqD8qBhNliBTR9GwZcBzRlOdObshLFJJG2aAYsa_Om0A_6sX50K2hYcf8SWRCfgjVIyEVg_Z0lfG-wMbUqwb4Plrs3WFde8z41RsBYdrUshznlulI7piO7qJ6Tm9YuG-u1bZeGeAZIMlk5CKgdF8LGdH-0GN1Q7Dg0p1ZNFgyY7kpl3UNL0owsNPGcp4yIKPPT6ebrf8LO3ux1kmppHioSFCuP-IpOy_78PCzSLsH7HsrXVl16ZskZbX_11_7lfzHu8REEmxHrVyeL9H5tBGXgxcxrLDMmzaBMPoH8adet43MFnnW5rRgnBFeuDJccsztvNCfow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به انگلیس توسط امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
1️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/672784" target="_blank">📅 01:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رسانه‌های عراقی از وقوع چندین انفجار در کنسولگری آمریکا در اربیل خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/672783" target="_blank">📅 01:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b1c746642.mp4?token=SdqhU1sUVo0Cl9rDf80-F770vi3-8WFDWgqFqsReTtriDEwX3om6gga3x5KxaVidgXtOzSNnG68Ggk2XsDP060iK78CRX1Ep8gWjphZFHdVVTpmlaqrbZASoOXmrMC-dbAdrMr8PNUvvISVqTjr59P-bTmldMM8mM8q_P-dLZ1mbHnaKFvnchxurqJCXXiNzUG9IVBDnMGa-_A0DWhuPBBNmAzc_e4nDfxAcC4Fxta5EUs2oxh0zzxNO13jD6zV4nBjgxva9r0PPSBZwlshi4_o2xnFzZaj1taq9dWdNtjImyiKxBO43z_cU28ozgJXboYFEiqyjMv1DbmmurWgeRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b1c746642.mp4?token=SdqhU1sUVo0Cl9rDf80-F770vi3-8WFDWgqFqsReTtriDEwX3om6gga3x5KxaVidgXtOzSNnG68Ggk2XsDP060iK78CRX1Ep8gWjphZFHdVVTpmlaqrbZASoOXmrMC-dbAdrMr8PNUvvISVqTjr59P-bTmldMM8mM8q_P-dLZ1mbHnaKFvnchxurqJCXXiNzUG9IVBDnMGa-_A0DWhuPBBNmAzc_e4nDfxAcC4Fxta5EUs2oxh0zzxNO13jD6zV4nBjgxva9r0PPSBZwlshi4_o2xnFzZaj1taq9dWdNtjImyiKxBO43z_cU28ozgJXboYFEiqyjMv1DbmmurWgeRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش نیروهای اشغالگر صهیونی  به محله الرامیس، در شمال قدس اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/672782" target="_blank">📅 01:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
انفجار در اربیل
🔹
منابع عراقی از شنیده شدن صدای انفجار در اربیل و فعال شدن سامانه‌های پاتریوت مستقر در پایگاه آمریکایی حریر خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/672781" target="_blank">📅 01:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
فعال سازی پدافند هوایی در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/672780" target="_blank">📅 01:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b100100dad.mp4?token=msFrQfjwVfMAcsUMi8FFRrjMCHfUMHxLZgTid0-i5u7nRJjGnY8mEbNLdp2KO0qU0QnR-S7ZrsfzTTyA670UFWS7bHzDfuUbXZJl92aCJxhK19Ck8SuoJ16eOU_Nw_N0VLnnOXn24rYqeeoss202RleLt8kARrVtWInWlgqnGGWr44knipY8Pdfgh0u0GW8ojED-cPmLHZh8o-ZfvW8-S3_frzNxaZW7p6xC0UIzhQUU4rOtMq4tsxDO5kZOJM2eiFjTgx_P1PlxEfiQxDCe_NlFtIVgsMlYTbj90Ne_rPczCnnPIZfH20bqE9tdJk1zp5Q-Qnb0L7KHlYhDEdTpww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b100100dad.mp4?token=msFrQfjwVfMAcsUMi8FFRrjMCHfUMHxLZgTid0-i5u7nRJjGnY8mEbNLdp2KO0qU0QnR-S7ZrsfzTTyA670UFWS7bHzDfuUbXZJl92aCJxhK19Ck8SuoJ16eOU_Nw_N0VLnnOXn24rYqeeoss202RleLt8kARrVtWInWlgqnGGWr44knipY8Pdfgh0u0GW8ojED-cPmLHZh8o-ZfvW8-S3_frzNxaZW7p6xC0UIzhQUU4rOtMq4tsxDO5kZOJM2eiFjTgx_P1PlxEfiQxDCe_NlFtIVgsMlYTbj90Ne_rPczCnnPIZfH20bqE9tdJk1zp5Q-Qnb0L7KHlYhDEdTpww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعال سازی پدافند هوایی در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/672779" target="_blank">📅 01:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2530637954.mp4?token=DLjqnGk3ZVHgdXjDmRWyBdmaYVMpv5Mp7Y_bQbpneQGAOkHs08Y5Qa8MArlaUyuEgxLyJcU84a3xBwXdQKlu-YGxsTYbPHKS4n9JX-3826pFGKSQRknTRGcIZLmOolBhErDtOa0cMJKii4HWrDlA6tKaZZglY9ZcyhVXFR03ATFQm6fileChcZqftnv0RYuPmGfuz-hGsa-L0QnIyYN_2uhWHEx9oW1rZ3jLPA8GfwTwreRB-A8gfhRhk5STYRP4SgQPU2WtLDHIHZFAjHwM8HyQIcRVg4f8WwmRTUmd8zEUkvM0QDIFIeFJ7VLS1ZbFW5G2sZjyRPA4M-_BTU1U9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2530637954.mp4?token=DLjqnGk3ZVHgdXjDmRWyBdmaYVMpv5Mp7Y_bQbpneQGAOkHs08Y5Qa8MArlaUyuEgxLyJcU84a3xBwXdQKlu-YGxsTYbPHKS4n9JX-3826pFGKSQRknTRGcIZLmOolBhErDtOa0cMJKii4HWrDlA6tKaZZglY9ZcyhVXFR03ATFQm6fileChcZqftnv0RYuPmGfuz-hGsa-L0QnIyYN_2uhWHEx9oW1rZ3jLPA8GfwTwreRB-A8gfhRhk5STYRP4SgQPU2WtLDHIHZFAjHwM8HyQIcRVg4f8WwmRTUmd8zEUkvM0QDIFIeFJ7VLS1ZbFW5G2sZjyRPA4M-_BTU1U9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تازه از لحظه شلیک موشک از کویت به سمت ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672778" target="_blank">📅 01:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc83a1fc86.mp4?token=M7Eu83G7nSstAcsdeqRh41kzFE0OVxKbmqDDDTihetk2j_S84jegYd4JecjnhyyneuWFThjaU9vLRjdsHMxCJdtPJ1AZ8l6IBEv8-oPCTvnMZt8qwn4s4PPQGeEhQPC0pDSyeYJ4yfiotAAzg5_BWqX9iX-XFWJ85VhXNsElHUb4NeY982tbeOKuet5HCT1rcg4VcmmW2k13NUeGviANX8IkxAlecqYZu3oidmWoDUDf__O21GMeUHnIVOmXrvt7KVcv7S_LUxA_Ck7Ox2sD-cRne_r4ZQvQSyWFa_VpXygRR17azYIdggsduVzcXXu2Ax4oTbdBQ8sP6Jxc7JTOfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc83a1fc86.mp4?token=M7Eu83G7nSstAcsdeqRh41kzFE0OVxKbmqDDDTihetk2j_S84jegYd4JecjnhyyneuWFThjaU9vLRjdsHMxCJdtPJ1AZ8l6IBEv8-oPCTvnMZt8qwn4s4PPQGeEhQPC0pDSyeYJ4yfiotAAzg5_BWqX9iX-XFWJ85VhXNsElHUb4NeY982tbeOKuet5HCT1rcg4VcmmW2k13NUeGviANX8IkxAlecqYZu3oidmWoDUDf__O21GMeUHnIVOmXrvt7KVcv7S_LUxA_Ck7Ox2sD-cRne_r4ZQvQSyWFa_VpXygRR17azYIdggsduVzcXXu2Ax4oTbdBQ8sP6Jxc7JTOfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم انگلیس به فرانسه توسط ساکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672777" target="_blank">📅 01:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5f17f766.mp4?token=BxhWVSMndOGVCQgGiHTvlF5B0PWa_Q8AKlFTkXts7iEmoUgYXuH4S95MjpStN31igvF3iQfFGoOR1HnHAnxbPEcbw9-7Sd3jKO5DImBfuCNCuH7IE3QEAVEzqGlxDdZFy6rQtX_8qqD4V7ipmqI0OXir3r2N6TdGgEjiLOvNC6q5zqgBOF7-VrElZX-oPxl3549QiIAL_wV0HTkB7BUWQjhuKH2Ge7ExDhYnCdPinJ4wxJNTX2duR_wFZyyg2xBk8n8w8Efb2hjwh11nKeUjavUwYnOYhWUbnwp_vIkOEzTASx1UZVU7iJng0LEg-6dYt4xllA4NkW3B61QXRI2-tpixxjLZCDvVGZmgyIYoutSdvvUN0qKpOYzy-fPR96NBucgWht7_6Ba27Yo8IOawHff5HNXb-UnaHs0lOBZCh_TCARpnnDEUl3Ohl_8oKyyYantevisCJpya_KgDk1I1DY29cDALR1eOpcAoTNP7bl-I7m3fyu20E2eT9A4wWXIOIYhbgb3aht_cbwXcpDqwQxG6XVNYeSxrW65ShkSHeAh7emcVMpDkWGq_k9iiIAqfuYNEXWBYlxMhysZ_oOUwZgr0p5TNqye9r1A7_cqiLtXe1qfts_uYm1lTYF-0qr3-96Dki-0rOdMEF7-ubawwuIcHDEFQNfn3afi-XmTJHyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5f17f766.mp4?token=BxhWVSMndOGVCQgGiHTvlF5B0PWa_Q8AKlFTkXts7iEmoUgYXuH4S95MjpStN31igvF3iQfFGoOR1HnHAnxbPEcbw9-7Sd3jKO5DImBfuCNCuH7IE3QEAVEzqGlxDdZFy6rQtX_8qqD4V7ipmqI0OXir3r2N6TdGgEjiLOvNC6q5zqgBOF7-VrElZX-oPxl3549QiIAL_wV0HTkB7BUWQjhuKH2Ge7ExDhYnCdPinJ4wxJNTX2duR_wFZyyg2xBk8n8w8Efb2hjwh11nKeUjavUwYnOYhWUbnwp_vIkOEzTASx1UZVU7iJng0LEg-6dYt4xllA4NkW3B61QXRI2-tpixxjLZCDvVGZmgyIYoutSdvvUN0qKpOYzy-fPR96NBucgWht7_6Ba27Yo8IOawHff5HNXb-UnaHs0lOBZCh_TCARpnnDEUl3Ohl_8oKyyYantevisCJpya_KgDk1I1DY29cDALR1eOpcAoTNP7bl-I7m3fyu20E2eT9A4wWXIOIYhbgb3aht_cbwXcpDqwQxG6XVNYeSxrW65ShkSHeAh7emcVMpDkWGq_k9iiIAqfuYNEXWBYlxMhysZ_oOUwZgr0p5TNqye9r1A7_cqiLtXe1qfts_uYm1lTYF-0qr3-96Dki-0rOdMEF7-ubawwuIcHDEFQNfn3afi-XmTJHyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم انگلیس به فرانسه توسط ساکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
3️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/672776" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
مدیرعامل شرکت آب و فاضلاب هرمزگان: تاسیسات آب‌شیرین‌کن بونجی در غرب شهرستان جاسک که در پی حمله بامداد شنبه ( ۲۷ تیر ) ارتش تروریستی آمریکا دچار آسیب شده بود، مرحله نخست بازسازی آن با موفقیت به پایان رسیده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/672775" target="_blank">📅 01:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672772">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpq0LEsDKJilUPMd3UlSZPHvLpdr8WmNByL8VROZiTX-LBFKi1q2m6-6k0cXXPHcQs5n14Q6Vojc1-zsYZQQIvDtQEikJPvgGKsdDKpRZ7mXBZjDV6A_Nm94oIlQJJ0XghNkPFlgIdj-aO09GGGgPgqUMZc57tVk6N3gMuOAMrY4lIqF52Y8Ti9PpEfkjr6nyzLLyODIfszt7vN1Xt9UnNVP5h7IkQMVtCVPLqp2POHzkqVwKqArkNqmXtWfOBoJbt87HlMhq6zDPzzSUA0WSlg8XWFAiYxlloDFtqkUmJvY366MDvF46nvl6vyaGUwc88LpMjTbDpEQycc8spTf1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LGg4TKcoQS8wKG_dKv-W-n7-hAHZ2pW_ieEsCCvgmED5bdldv8lwoKWmu99VC5bQfogin0Rk9wwl2Hl2053y0S5V5Gd5hLETBCfiCpKHUzS3YtIEO3W9JVHSQQQGvYyHCiXp9OCZweq5wRh2VkrQ-83LvOrdAhQL03io_kWzu_naDmlw8I5mCPkXEvKTZYPvkSGpda_cWk8oHUbZ0tBRKocIWNNNsybUjAoAhzVgz42biWSNd_JQBdvZmbhybTEG7lcQHpOQniE21tNB6EmEJ2Zje3conNNRbtxAzmJ0GipzwaNSEPhioS-fyDK9grq3k53WLA6RiJih9FzTlD5a3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4894ed02a.mp4?token=YgtyDC53-89DTF4-_XreBbhZ1cNuOqIw9uGIt_-pL01McNCFBAJtX7Z06-4TRnrpxwcD3lJnBRhKL8v1RDVFWH3HaiMQueQj_vCoNEaIrCQvxeZKla0FUaX6-Q_eO1IyLcutFK74oH3yD0ydhg6rCayxQVR_tc582ERP0OgRcDTIMimC7B4gFT0ME_wnwYbswSVFSDEOEK7ZvJ8voWXlVKBpqdy_o6PeCDjt9GLF05vaOJxSftH2n84oevAV-e7vsDhmSzQ0kHuj0KOAEmv3Gms-KCKu-42iqf8iIP7v8ypciwJSAN8FEL8ard6AdlyA4-M2FZ8JUzgZvQvVgujjpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4894ed02a.mp4?token=YgtyDC53-89DTF4-_XreBbhZ1cNuOqIw9uGIt_-pL01McNCFBAJtX7Z06-4TRnrpxwcD3lJnBRhKL8v1RDVFWH3HaiMQueQj_vCoNEaIrCQvxeZKla0FUaX6-Q_eO1IyLcutFK74oH3yD0ydhg6rCayxQVR_tc582ERP0OgRcDTIMimC7B4gFT0ME_wnwYbswSVFSDEOEK7ZvJ8voWXlVKBpqdy_o6PeCDjt9GLF05vaOJxSftH2n84oevAV-e7vsDhmSzQ0kHuj0KOAEmv3Gms-KCKu-42iqf8iIP7v8ypciwJSAN8FEL8ard6AdlyA4-M2FZ8JUzgZvQvVgujjpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوکراین به مرکز لجستیکی ویلبریز روسیه در شهر الکتروستا حمله کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/672772" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672771">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/672771" target="_blank">📅 01:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672770">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
خوک زرد در گفت‌وگو با NewsNation درباره پایان یافتن یادداشت تفاهم با ایران ادعا کرد: اصلاً برایم مهم نیست #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/672770" target="_blank">📅 00:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672769">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
خوک زرد در گفت‌وگو با NewsNation درباره پایان یافتن یادداشت تفاهم با ایران ادعا کرد: اصلاً برایم مهم نیست
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/672769" target="_blank">📅 00:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11dfde57a3.mp4?token=hdYbQGURWIye7NrIJGOoKv9L2qJqG6mEqzvosqMOj3eoSKBANZ8m-XDrGO5y-SoJ5mzbXr1ZLj1nIqSeZHEDJoY1tp5FXoG9Jelx-0-Bol8R9z18PdJlErL60pzCUAtHSe0_xdUy-ncc7Fd2zf0n-JFPwQ-yUpxUFWC7pRraY9_IOVhJK2sSlJPXT0SZFszbHr487-ZAxl8Zx1Mu-5te4Gf4lYBJFbK_7jl8O04WKTJLM2wChF3SitghnQVDMA1rQmT7gk7J5beAPQmj_Bw3OHQOF_jauWAVyj8bQXk492p6SAmixQGm-vVH6Zt7wZNknX8jbaeNbmG44EBkgcPqwF4b7LqbBKV3s8War_2trS96SSyPGCCemL0It8GdGkvar9TJEQ5oENpnu-sW4IUIKMiCuuInNY6zCQz1eD3aAshp2pHCDBw0VL6JPSil8SreQ3MnrPSJZjrW1mqFASHBAoPQ0Ohu4arPTZO3JVU4EkiPy-PXEeB-y59iajt50VscmD-bGoWo76JyDFvpjOEveQXIg8rjl8jAiLDNKSFXz5q8pugNSQxLiM_N16asJ_SYXyTbD8_8GqocT2drhhBu3dXjwsaeCkVqa3JqPf4XZz8mlicQf5xiAeX3XVYf4XxQNOh-lz5UUWuQOF_IhDWLythazbjVt-sZvbUcO9RY3P4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11dfde57a3.mp4?token=hdYbQGURWIye7NrIJGOoKv9L2qJqG6mEqzvosqMOj3eoSKBANZ8m-XDrGO5y-SoJ5mzbXr1ZLj1nIqSeZHEDJoY1tp5FXoG9Jelx-0-Bol8R9z18PdJlErL60pzCUAtHSe0_xdUy-ncc7Fd2zf0n-JFPwQ-yUpxUFWC7pRraY9_IOVhJK2sSlJPXT0SZFszbHr487-ZAxl8Zx1Mu-5te4Gf4lYBJFbK_7jl8O04WKTJLM2wChF3SitghnQVDMA1rQmT7gk7J5beAPQmj_Bw3OHQOF_jauWAVyj8bQXk492p6SAmixQGm-vVH6Zt7wZNknX8jbaeNbmG44EBkgcPqwF4b7LqbBKV3s8War_2trS96SSyPGCCemL0It8GdGkvar9TJEQ5oENpnu-sW4IUIKMiCuuInNY6zCQz1eD3aAshp2pHCDBw0VL6JPSil8SreQ3MnrPSJZjrW1mqFASHBAoPQ0Ohu4arPTZO3JVU4EkiPy-PXEeB-y59iajt50VscmD-bGoWo76JyDFvpjOEveQXIg8rjl8jAiLDNKSFXz5q8pugNSQxLiM_N16asJ_SYXyTbD8_8GqocT2drhhBu3dXjwsaeCkVqa3JqPf4XZz8mlicQf5xiAeX3XVYf4XxQNOh-lz5UUWuQOF_IhDWLythazbjVt-sZvbUcO9RY3P4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیارت
از نزدیک‌ترین فاصله
🔹
فیلم یکی از زائران سیدالشهداء از لحظات با شکوه تشییع و ورود پیکر رهبر شهید انقلاب اسلامی از بین‌الحرمین به حرم حضرت عباس علیه‌السلام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/672768" target="_blank">📅 00:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672767">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۳.۷ ریشتر بندرعباس را لرزاند
🔹
بامداد یکشنبه، زمین‌لرزه‌ای به بزرگی ۳.۷ ریشتر حوالی سرگز در استان هرمزگان را لرزاند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/672767" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672766">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9defb1eb81.mp4?token=hmJUW9ZDIMfkGXfEL5kWD6m7JByrBnBBI7AE0gWUqa07cKnK-bqba6fgRDAZQPifUijL5DTN_RcJjWWn7TBjUODNB9M_CGBPZPATmnyqbeEN4fNdx-SKVbBhEykYgLOngNFh0Oae3GoWK-tcxq5tDMlRBzzs-BfJtsvIzieAhGRau4wbwOUNQTdwXUOM2ys58dpAzMx6SmlatmG1ZQmyANMGNPW3CzRU4l0d75QLqOEX7eZ7OYpsmGpruQyh_TpZnJFcO6lt32z50z6MA4mj3Ljr3lQUeVXySmmoG9YEGDNYrosTPUi5LUc-gDNYRuUdeFz6wCSoPKM7eLDlUbe9bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9defb1eb81.mp4?token=hmJUW9ZDIMfkGXfEL5kWD6m7JByrBnBBI7AE0gWUqa07cKnK-bqba6fgRDAZQPifUijL5DTN_RcJjWWn7TBjUODNB9M_CGBPZPATmnyqbeEN4fNdx-SKVbBhEykYgLOngNFh0Oae3GoWK-tcxq5tDMlRBzzs-BfJtsvIzieAhGRau4wbwOUNQTdwXUOM2ys58dpAzMx6SmlatmG1ZQmyANMGNPW3CzRU4l0d75QLqOEX7eZ7OYpsmGpruQyh_TpZnJFcO6lt32z50z6MA4mj3Ljr3lQUeVXySmmoG9YEGDNYrosTPUi5LUc-gDNYRuUdeFz6wCSoPKM7eLDlUbe9bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم انگلیس به فرانسه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
2️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/672766" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
کانال ۱۲ عبری: اسرائیل در حال بررسی امکان اعمال ممنوعیت کامل پرواز پهپادها در آسمان در پی نگرانی‌ها از تغییر روش‌های عملیاتی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/672765" target="_blank">📅 00:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672764">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
یک منبع دیپلماتیک به اسکای‌نیوز عربی ادعا کرد: ایتالیا پیشنهاد داده است در کنار آمریکا در سازوکار بازرسی از مناطق مورد توافق در جنوب لبنان مشارکت کند تا اطمینان حاصل شود که این مناطق عاری از سلاح‌های حزب‌الله هستند
🔹
این منبع افزود لبنان با مشارکت هر کشور اروپایی در این سازوکار موافق است و اشاره کرد که ارتش لبنان ابتدا در شهر فرون و سپس در مناطق زوطر غربی، الغندوریه، قلاویه، برج قلاویه و صریفا مستقر خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/672764" target="_blank">📅 00:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672763">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e924394c6.mp4?token=hAd5EVdXAL1UIxFDIBmo5-t8EHO1qcoKdb8Rfw-4xminrWFAEy17J3ErQesl337wkEapinTovBbX0YH38SXjpPrDGzq343dKL4_uI6VzTRbdXR60sNQsJBaUxDbIarNPDLKkRSQB3yK003xXo2XEaZA7bb1chzyK8VRp6rKN5mtwdtSZ8j2e1v-LDxElT_a-KOzveQCCBO-WeMa6_Jcm7xOm07gF2aHJWbRHwgZ3MM7eBXvi1s34srZkTJA2SCMc5sI63JXCB5Kq4EwK8xYXclvCjgYi36mqQ5Zi32C72HDT8nSaawcIIPYPms-KbOSLVyAPsNp6XUppgsSYsk-wIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e924394c6.mp4?token=hAd5EVdXAL1UIxFDIBmo5-t8EHO1qcoKdb8Rfw-4xminrWFAEy17J3ErQesl337wkEapinTovBbX0YH38SXjpPrDGzq343dKL4_uI6VzTRbdXR60sNQsJBaUxDbIarNPDLKkRSQB3yK003xXo2XEaZA7bb1chzyK8VRp6rKN5mtwdtSZ8j2e1v-LDxElT_a-KOzveQCCBO-WeMa6_Jcm7xOm07gF2aHJWbRHwgZ3MM7eBXvi1s34srZkTJA2SCMc5sI63JXCB5Kq4EwK8xYXclvCjgYi36mqQ5Zi32C72HDT8nSaawcIIPYPms-KbOSLVyAPsNp6XUppgsSYsk-wIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول انگلیس به فرانسه توسط رایس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
1️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/672763" target="_blank">📅 00:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672762">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ضربه به شریان نفتی جایگزینِ هرمز در عربستان
🔹
در حالی که عربستان برای فرار از بحران تنگۀ هرمز، صادرات نفت خود را به بندر ینبع در دریای سرخ هدایت کرده بود، گزارش‌های غیررسمی از خسارت به تأسیسات نفتی این منطقه حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/672762" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672761">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX7owXoZ2yNQfCghggDUDLhbgE2mazEXU4uwOSlvEybV0BYwPyDHRBI-jf0J6PplgiNGUgGMU8-bEDqVIiTpqZzhru7FNjPF52IOzSbiCHlun1mnYDjn5VS_OTW0u7iC9VUEarSY0Cpe1XsYlg99pMavwIQZTxr6OvNAtiOqFVdcdKVDkGtsDdLJbchfEdauL3UJydSJlRgK_L5CewBszTvsWeHT7AiVboAI8NVCR-Qu7f5-TPYjS4QZCliSwHJL4RmZGd0iwq4PwwdX1XWHQ0XNF83M6d9qbgk0yshUQ0yduwspkAOzCW0PHIDZ1lm9bnafLn0QlR1b5_tOX72Rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا هشدار امنیتی جهانی صادر کرد
🔹
وزارت امور خارجه آمریکا با انتشار یک هشدار امنیتی جهانی، نسبت به افزایش تنش‌ها در خاورمیانه و احتمال تشدید غیرمنتظره بحران‌ها هشدار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/672761" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672760">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نیویورک تایمز، به نقل از مقامات آمریکایی: حمله ایران در اردن به تعدادی از بالگردها خسارت وارد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/672760" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672759">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
نیویورک تایمز، به نقل از مقامات آمریکایی: حمله ایران در اردن به تعدادی از بالگردها خسارت وارد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/672759" target="_blank">📅 00:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672758">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
شبکه اسرائیلی i24NEWS به نقل از منابع خود ادعا کرد که یک هسته وابسته به حزب‌الله لبنان قصد داشت یائیر نتانیاهو، پسر نخست‌وزیر اسرائیل، را در محل اقامتش در شهر میامی ترور کند
🔹
بر اساس این گزارش، سازمان امنیت داخلی اسرائیل (شین‌بت) این طرح را در آخرین لحظات خنثی کرد؛ زمانی که اعضای این هسته پیش‌تر به طبقه زیرین آپارتمان محل اقامت یائیر نتانیاهو رسیده بودند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/672758" target="_blank">📅 00:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672757">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شبکه CNN گزارش داد که دولت ترامپ به‌طور اولیه با اعطای مجوز به عربستان سعودی برای غنی‌سازی اورانیوم در چارچوب برنامه هسته‌ای غیرنظامی این کشور موافقت کرده است
🔹
اقدامی که در پیش‌نویس توافق هسته‌ای میان واشنگتن و ریاض آمده و اکنون در انتظار امضای دونالد ترامپ است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672757" target="_blank">📅 00:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672756">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06c16cad.mp4?token=niRMLl8reYd20A5vZ9d6jJ8DdMDGId9RiavFV928pdVM2YeFxwo_jUeCiWhvbBew9v6oebCK-LDh52fe0qcbBxdXTt5JVkRxMXkSzI5u41VzBi1caDAFbrsDI8zJOVaieC4mKXMJ8__atTpeH5r53wYg4K7_oUY0jVtTwKjXjEiMtT-nHrh6f80FOfire1rdFH7X1jOsaHim5B_7SHlQO3kKHF35gDMOQlQ4ma5M92UXjAiRKslCwktmbts28KoFmZGJh_YT7X2-2w4vZZakDR132s2o9rRcg-uI2g88uBSDfg2hfBZSIszojCPJmBGnjImEywbDMre7GdBo0SLCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06c16cad.mp4?token=niRMLl8reYd20A5vZ9d6jJ8DdMDGId9RiavFV928pdVM2YeFxwo_jUeCiWhvbBew9v6oebCK-LDh52fe0qcbBxdXTt5JVkRxMXkSzI5u41VzBi1caDAFbrsDI8zJOVaieC4mKXMJ8__atTpeH5r53wYg4K7_oUY0jVtTwKjXjEiMtT-nHrh6f80FOfire1rdFH7X1jOsaHim5B_7SHlQO3kKHF35gDMOQlQ4ma5M92UXjAiRKslCwktmbts28KoFmZGJh_YT7X2-2w4vZZakDR132s2o9rRcg-uI2g88uBSDfg2hfBZSIszojCPJmBGnjImEywbDMre7GdBo0SLCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز روز امتحانه و در روز امتحان جز دفاع از خاک راهی نیست!
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/672756" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672755">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHUHjBtddNmnw4DPgJ0qrBzsqyvoXTHyqRjxWhiHKixPPGEk0OXxcdyj91KUedDVg5w0UYtfB15Sx0w8cXvJn14T1Thd_KZAuvpDE929g6zlXAKVTywJZGCXllHowFfrEvGMtDMiwW8ug1du2P3imo5-NWqc4XgpsQSLll3bxSW9hbvRgLGn1j6QPB-Ox-mOevcgNuDfG8NsfHJgm83INEQE0irv9_HfdrIX6eJ0uvzztyBCm7row9HdgqzSAa596Fa-cFsMNCtcSk0oLvrDgwIrjEJavXQKxO_0ol726bpemJedflmvQg83-WuijaXP9mvIY39uUMQNhO4jWmSnJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پارس‌خودرو قیمت جدید ۹ محصول خود را اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/672755" target="_blank">📅 00:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672754">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FieSlzgb39gmidLXaobo-teQXDSRDyuBBYb67YfUAAZSaVApRzMiNa1esz-roZdXvWd4ZIK-jO82ToWarx6Bd8Tm2CKa_CYjBHIRXxxAsgQ918xxb3a4JPRLImFkqbAzg59sPzFZ5khp2NLmok0iPyBtqMk4xl9RwcAbVvQiOtzAl_XYJeVJXUuhKgbgVXZfMkwJM_Y67lwyf45yRW00Xsj1OkLi6MMuAoiSp76l_dkcrOop1-MxU5D_N1OpHZtQfWwrRS2VjxLNbfN9Ehxxs3q48el7ub9UQ0RMEpPhBr6VCmFPOc2gIcLDKjAInKLW1pzIU4H9-zsaq4LYBY0m_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اتحاد
اعتماد
انسجام
رهبر معظم انقلاب امروز در پیامی فرمودند:
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی سطوح مردم و مسئولان و در تمام عرصه‌ها برای تحقّق آرمان‌های بلند انقلاب اسلامی و تأمین عزّت و استقلال ایران عزیز خصوصاً در برابر دشمن جنایتکار و حیله‌گر امریکایی است. همانگونه که پیش از این مکرّراً و مؤکّداً تذکر داده شد، صیانت از وحدت و پرهیز از تفرقه و تنازع، اختلافات سیاسی و برجسته کردن تفاوتهای اجتماعی وظیفه‌ی همگانی است و البته نقش مسئولان و عناصر دلسوز و دلباخته‌ی انقلاب و امام و رهبر شهید در انسجام و یکپارچگی کشور، مهم‌تر و حسّاس‌تر است.
🔹
هشتصدودوازدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/672754" target="_blank">📅 00:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672753">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBCQ6NalIGn0aVD7wGk4k5-DEmQ5izM-AKU05ruySL6kRxCrzZ5w42NaQF39n9idHNZVo_EpgyQ8XoludqtzQDvbMU-QdmYiY9-Qly0ez33-VUdkoXvI5tOunWF-Q_tFspHN7zRdpxw35ikzr5rkM7az4MWzqOd8-0mIxgxzt0QdhUwLXchRfPctqYq7YLHiZAUCy0tBP-c9rN-yX8pMfqEk7FzrLxh4IBBQyMTKVmP_k-I6CbFn0X7cQX7ewu4Ar3ChxwrW9SDqTDe5odLMZxpYffzjzPbR8FHq7--kAeixucKnCEvpFEqUyQHZ14oGdUsLUf96wif-5w6jap9GPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت آب‌گرفته خیابان‌های نیویورک در فاصله ۲۴ ساعت تا فینال جام جهانی ۲۰۲۶ #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/672753" target="_blank">📅 00:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONXDa5Gp_QvHcOuMA05xI6ncPDsm4WqRshKZ1WVbhTthClOeALyFrcPyIElMYp3V68iUE4MfFa9Jyf935fN0FsF4X9va-Ub0zLOgkj6moADMEUFialozb3KXUZI5lFrNi8c-mZ-Z85Uqdg9m_fiBIQeQCqfhnA73SUSpCGldHmc75J6Qz7RsrUSiV5_MMEvAh3OVFlsPmngzA-IBTWu8FjyEJ3_r8Ni4KHIPbY83UG6GA8OCMhYvtX0W3rQC6gKRQjUkfi7nMrxxU_5ScQYQvWLzH5h8abioUvf_aXasqtsXZgA7XfXjddw4cKs6KpuaoYC0rR0e5bNhKgxEarrJRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اطلاعیه فوری برای سهامداران بازار بورس
به درخواست کاربران کارگزاری آگاه و مفید
کارگزاری آگاه و مفید جهت رفاه حال همه کاربران خود در نظر دارد ، سیگنال های تک سهم خرید گروهی را در اختیار کلیه کاربران خود قرار دهد
https://t.me/+werraAXV39phMDZk
از تیرماه۴۰۵ همه کاربران میتوانند از طریق این کانال پربازده ترین سیگنال های خرید گروهی را دریافت کنند</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/672752" target="_blank">📅 00:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672751">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhPngkEIiKyeNiFdoryuLLyEDmfERf8m2ZkQbJHcbnl71wrAPgY59yqKF1DV-NxnXlZ-nph5uZ_6epPxnukDZBNELOZ8Vv6SP4N3nO_joXnXdz3E8s82diWYP5BNsh660B_r4TuGePPz7r0h2INEdcZJWvJoWpG48Ky2ZcrT0A2q5PKEjOfnBelxUMWhVCkG2pGmzebzxhEJBcVYI9KpH4UbyQ3vOYImFsP7BYoP-chnp3TyJCaUHP35SbW7aXGF2BAyXNV9_9SNPjGZaFAxHydF4LcSDZ5t7fXjs0fe1-1kZJDTmF_4KTrqYfyBuVK-NL0fghYjZZ2C8cVcxN7coQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/672751" target="_blank">📅 00:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672750">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3be390f66.mp4?token=BoB69xWb1iABo4aOKFXku8iEAeTPcnGtZIUYZgwecH105S3v1H63IrdFkj2S3-pgbvWsAq5zD8xz6d60VHvPf7743Y2I-rGrAlZQutiaJUj_k78-xsvAe2_1a-BoXDkM_UInZCZmr0zWEREzx1Cgv7ot3pCX6KXRaDARQupMHmJXiR9UWJmHtBIct7GC_Y_IczgfOOdNi2t3x_MklLb0w_dLwE0JgRM0XgV4r22Wrf7e0Tf0oqMCgB2qdouXCalkhI6tS5CMM_gGMrlUEbO7fdGciT8iRdXOaV8KnXjXBUi-5hmIIS2aBrlRfIags7TFTyrqW_AE1MJC9rL2jhRxcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3be390f66.mp4?token=BoB69xWb1iABo4aOKFXku8iEAeTPcnGtZIUYZgwecH105S3v1H63IrdFkj2S3-pgbvWsAq5zD8xz6d60VHvPf7743Y2I-rGrAlZQutiaJUj_k78-xsvAe2_1a-BoXDkM_UInZCZmr0zWEREzx1Cgv7ot3pCX6KXRaDARQupMHmJXiR9UWJmHtBIct7GC_Y_IczgfOOdNi2t3x_MklLb0w_dLwE0JgRM0XgV4r22Wrf7e0Tf0oqMCgB2qdouXCalkhI6tS5CMM_gGMrlUEbO7fdGciT8iRdXOaV8KnXjXBUi-5hmIIS2aBrlRfIags7TFTyrqW_AE1MJC9rL2jhRxcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسارت سنگین به آکادمی امنیتی کویت در حملات موشکی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/672750" target="_blank">📅 23:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672749">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d689600b6.mp4?token=DLBx8Gd--ITfFY_WsIly8pEqDgV_vIdEplWkweqPo97hrPHo1bou0v4u52RfqBo1qAHwoGXwgPmvcKpnwYYhG-0yaLXCWnybUlgpzqeWUhoy9elNo0GZjLEyhksoV8VLLdXSkcTD9io5FOmAKYHeWBCzy8iMzFpvFoGv09Y-FAeCDpXB9tJklWbxDsGPpGl8Qd6V2Q9q89EH816qPRI6XXkpyjPZ_gIcAwXd6rKYE8V6ymKRk-WJaV6kigZrcT0two4iDzHcdVqwTOLef5hcZ6g1QFB085rw_4MDez2ypTCRFa2Fr0OpE-mqhHuccB17-GWZXojVYcTd6f8GjWhPkj9rasIyEImz8-26Os6McjUTZnOBkwGmQonh5MVI2xe9gLj6vdgdkCmMqTMlqVn02tOfnfJL-MbQ59jkB3Sw4ps3jSn9COjZHiosqUrpfbU4YVBVv3dG74o2xQwLmSytPXK756GgCtPpiBrSYy2t1LobhPPhedomV5hozUYYvoa_BtaXyWuEzLyf0JJRwlRxQMZ7PJtqmN7P4ylomsHbblfiI8EGbXNKlM0aRaGcsANGr7nUFWS4P51crwPg61R_eHNo3oZR9JiQx5tjxuW128e4Y_WIrJV1zIfIPibAXOWnBWaJCKRt0fDKCLPSfhFxXUeiJWXg7WBGzTIybjxXLiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d689600b6.mp4?token=DLBx8Gd--ITfFY_WsIly8pEqDgV_vIdEplWkweqPo97hrPHo1bou0v4u52RfqBo1qAHwoGXwgPmvcKpnwYYhG-0yaLXCWnybUlgpzqeWUhoy9elNo0GZjLEyhksoV8VLLdXSkcTD9io5FOmAKYHeWBCzy8iMzFpvFoGv09Y-FAeCDpXB9tJklWbxDsGPpGl8Qd6V2Q9q89EH816qPRI6XXkpyjPZ_gIcAwXd6rKYE8V6ymKRk-WJaV6kigZrcT0two4iDzHcdVqwTOLef5hcZ6g1QFB085rw_4MDez2ypTCRFa2Fr0OpE-mqhHuccB17-GWZXojVYcTd6f8GjWhPkj9rasIyEImz8-26Os6McjUTZnOBkwGmQonh5MVI2xe9gLj6vdgdkCmMqTMlqVn02tOfnfJL-MbQ59jkB3Sw4ps3jSn9COjZHiosqUrpfbU4YVBVv3dG74o2xQwLmSytPXK756GgCtPpiBrSYy2t1LobhPPhedomV5hozUYYvoa_BtaXyWuEzLyf0JJRwlRxQMZ7PJtqmN7P4ylomsHbblfiI8EGbXNKlM0aRaGcsANGr7nUFWS4P51crwPg61R_eHNo3oZR9JiQx5tjxuW128e4Y_WIrJV1zIfIPibAXOWnBWaJCKRt0fDKCLPSfhFxXUeiJWXg7WBGzTIybjxXLiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون حقوقی رئیس‌جمهور: علیه ترامپ در دادگاه‌های داخلی و بین‌المللی شکایت کرده‌ایم
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/672749" target="_blank">📅 23:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672748">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
آغاز دور جدید عملیات روانی دشمن با ۳ محور هم‌زمان
🔹
ارزیابی دستگاه‌های اطلاعاتی حکایت از هم‌زمانی ۳ جریان در روزهای اخیر دارد؛ تشدید القای فشار اقتصادی، تحرک رسانه‌ای هماهنگ برخی سلبریتی‌ها و افزایش مواضع انتقادی چهره‌های سیاسی.
🔹
آنچه ناظران را نگران کرده، شباهت توالی این رویدادها با روزهای منتهی به وقایع ۱۸ و ۱۹ دی‌ماه ۱۴۰۴ است؛ الگویی که در آن زمان نیز به اغتشاشات انجامید./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/672748" target="_blank">📅 23:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672747">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0TkhWO6rNdZUc9-A2lyYSjpNNzXRUH0N7FOevHL6dziw8uSnMV2HhmpliTrJ2LzkWpdngGzxJyCnTYOr2FvFVr92KIC9keASaunH3Ks69TVCyFLidbtAuMBGHgr2Bh1iLj63FH-reQ1TQ1oofLEbqSxWQRt8sc2ObZzoDswkIg6qzjZNS16mTrRqm1v07LYDTFXCOog2satlOtMggNBjGMHfsC1J73gMYNrI5IpTjf73b1T-asNsOUzSq_VsfNRL5U6B83TZXyKVMOPgR-iLjiN6m0Gv53OD4rhrlaYR1ZY7uWK4aK9yrHTvxX-1HNoC5ed8HY0R2C8tTyriPwE-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی دیگر از حملهٔ موشکی دیشب ایران به پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/672747" target="_blank">📅 23:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672746">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
وال استریت ژورنال: مقامات آمریکایی می‌گویند ایران با استفاده از موشک‌های فوق‌سریع و مانورپذیر که رهگیری آن‌ها دشوارتر است، خود را با پدافند هوایی آمریکا سازگار کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672746" target="_blank">📅 23:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672745">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c524bb9a28.mp4?token=KHvC_x3RQAne_ntWnLQFREhhETMNxUf-IFyZ5ZhHFt1uEg6gfBLrQ7cWm2XIOKy5L2NaHABr5i0Xzmc16Q9jFzbcOhMV4glBIU57SvXLebl1NsaTkQ4KE8_4f3kobICliB1jnm0eF3HuOo_r5tqN1WMdtWxUSsA6uEQP5Zx1PZRxQAsEWCDBVLBBjzwtDzcy3N1lf_-M1SCNXZN55Q-O2iNcPnOfnk2ol1kKgP-Q4r-oGVH514IqtdoIJOPPDbDYag8l-1frnxnglsXGVFuD4ADQB3_T85ZaB0B5QN_jVrnREvQSNbRR0p10yu6CaCh9Dwr5oA-UrPTfzf_fSmk-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c524bb9a28.mp4?token=KHvC_x3RQAne_ntWnLQFREhhETMNxUf-IFyZ5ZhHFt1uEg6gfBLrQ7cWm2XIOKy5L2NaHABr5i0Xzmc16Q9jFzbcOhMV4glBIU57SvXLebl1NsaTkQ4KE8_4f3kobICliB1jnm0eF3HuOo_r5tqN1WMdtWxUSsA6uEQP5Zx1PZRxQAsEWCDBVLBBjzwtDzcy3N1lf_-M1SCNXZN55Q-O2iNcPnOfnk2ol1kKgP-Q4r-oGVH514IqtdoIJOPPDbDYag8l-1frnxnglsXGVFuD4ADQB3_T85ZaB0B5QN_jVrnREvQSNbRR0p10yu6CaCh9Dwr5oA-UrPTfzf_fSmk-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ملانی استنسبری، نماینده کنگره: باید عقب‌نشینی کنیم و از جنگ با ایران خارج شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/672745" target="_blank">📅 23:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672744">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbMeUqRDDoRuZzGwTF06pJWa_QdqGTF-O_5S_OXC9dvOhT7WyRtv2X9R58lzfBL4Sk8CZCHIXrQNDOcmJMQUEZmduajMM0-BlISOv5BozzYeseWcgOZU5ZOid7_c0teWK9mQJmAzSxXec7m3K_29rjWOVI5cH0ccmQfSmNvsFoLmZDvevYirKSmYtr2dQC6dDsX-RatL5UNzCSLQIfSsimQtUbQEapfT8RJdqzgVufJeNC1Xemk8iUVOuokDzzt5lYqz96uzaJntnvEJKSQVjTnjhJiciJ1OGICLm0Cc_wWVamAO6MkxL7sFZ77NZRnuqNaGJFt1NGrvPhP77QoFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«همه باهم برای ایران»/کمپین ملی صرفه‌جویی در وضعیت این روزهای کشور آغاز به کار کرد
🔹
در روزهایی که دشمن شیطان صفت با حمله مستقیم به برخی زیرساخت‌های حیاتی کشور در تلاش است که اراده ملی ما را تهدید کند، نقش مردم در حفظ پایداری کشور بیش از همیشه اهمیت دارد.…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672744" target="_blank">📅 23:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672743">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEeC5IowYgZZjphRK14hYWEAn_tBgdZRKS_hzhT9Wmkm6OJYi42IoVp17sGBuOsC6r7a-2CiTBIqDPnt2M-YyWkle5UWpCEey0OF5BbdXy9xfyBq-iAWe_0cqBXRH0Qi4nfQjgkSl3gwTmVa6e1VuugxKGsScHs2mq4OGmzCr_0JZPwwJd4TxUJPCfMpLiEzYcn98kOvm9DAiEEgnrmev59lncCT1BIBjCvEsEIVG3_8zWgzqUzAvXjehzb78kEhzDeQMySONLe1r5MlZq0G0ubW-mx-GCefR2DEuBr7jK2dW8K12vBMsM-2iCGyYonILHW5oCtIP62xhuG0_ooRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوکراین حمله پهپادی گسترده‌ای به کریمه و غرب روسیه آغاز کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/672743" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672742">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71053f856c.mp4?token=Y3800GHNLVb0_QXEmXxOpFakztZkeK7djuf8hjj9kXEjSP_169SoTlFXbIwAoBV1gM3a3QGyA42uXwPCaf_KCrs_r0enBf7LGBGWSdX9pJswswb0gtPQJ7rarT0OtpE56oOLO0RCzm-tE3wYTJF33tJuEBgUrfJyOvv3HIeeZKum3gKZ4SDzzaCjkrz7tTyFfSUob5RX79jRq2HVOkXCTJCBJAPQUuvXuB8dnw3GdDQIgeil6PNI9JuMSc2eHZniln2VVnL4RmT5GfDHi7fg2UXEIiEAMB7XBZuC0IIyHPEstmo2kjBgds0AshFyR83zPlQV0QLii1Y_9mAhFXMDZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71053f856c.mp4?token=Y3800GHNLVb0_QXEmXxOpFakztZkeK7djuf8hjj9kXEjSP_169SoTlFXbIwAoBV1gM3a3QGyA42uXwPCaf_KCrs_r0enBf7LGBGWSdX9pJswswb0gtPQJ7rarT0OtpE56oOLO0RCzm-tE3wYTJF33tJuEBgUrfJyOvv3HIeeZKum3gKZ4SDzzaCjkrz7tTyFfSUob5RX79jRq2HVOkXCTJCBJAPQUuvXuB8dnw3GdDQIgeil6PNI9JuMSc2eHZniln2VVnL4RmT5GfDHi7fg2UXEIiEAMB7XBZuC0IIyHPEstmo2kjBgds0AshFyR83zPlQV0QLii1Y_9mAhFXMDZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش فاکس نیوز از خسارات قابل توجه به تاسیسات نفت کویت
🔹
پس از آنکه مقامات اعلام کردند تأسیسات نفتی کویت در حملات مکرر ایران مورد اصابت قرار گرفته است، دود غلیظی از تاسیسات به هوا برخاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/672742" target="_blank">📅 23:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672741">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TanHNbYmGjybgXQlCJyqJabxA2b3cqK_1sQxwGLun4i2-DUgCWo9_tzdSthJfdW7ab1HcD-xp0dfJwwJK2Sa2viGgbGQubOa8B2lqZlTb5qww7Dtz4pq58f1X83k1UqvTAbE2ajaQIrMEuq_1n0P_KdGaFiRS245PyOW13zBTJHtrCdXPcZP5afKv3Sf5jehJlV9a6pdtcAYrioqTmIZ9pACHQGML00atWt3vKCcwpStsqmPfJ1ArVQPep0AsEeqUgW3GkDqavhC-jbC2bfZVLEnBUmsicodKk1n3AwDnhmvtcTIQge_btoU45DUP0ycEipCM-EFMyAixeFIzsYMFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حملات هوایی مجدد رژیم صهیونیستی به جنوب لبنان
🔹
رژیم صهیونیستی روستای «کفر تبنیت» در منطقه النبطیه، واقع در جنوب لبنان را هدف حمله هوایی خود قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/672741" target="_blank">📅 23:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672740">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزرای خارجه ایران و عراق
عراقچی:
🔹
روابط ایران و عراق نباید تحت تأثیر برخی اظهارات شخصی و غیر رسمی قرار گیرد.
🔹
ایران بر احترام متقابل، حسن همجواری و توسعه هرچه بیشتر مناسبات با دولت و ملت عراق تأکید دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/672740" target="_blank">📅 23:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672739">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
آماده‌سازی همه‌جانبه آمریکا و اسرائیل برای حملات گسترده به ایران
👇
khabarfoori.com/fa/tiny/news-3231341
🔹
بنزین ۱۰ هزار تومانی در راه است
👇
khabarfoori.com/fa/tiny/news-3231318
🔹
پیشنهاد جنجالی مشاور سابق احمدی‌نژاد درباره پروژه انتقام
👇
khabarfoori.com/fa/tiny/news-3231310
🔹
علت نرفتن تندروها به جنوب برای جنگ و همراهی با نیروهای مسلح چیست؟
👇
khabarfoori.com/fa/tiny/news-3231169
🔹
این سلاح کوچک تعیین کننده نتیجه جنگ ایران و آمریکا خواهد بود
👇
khabarfoori.com/fa/tiny/news-3231295
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/672739" target="_blank">📅 23:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672738">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxhzn5MlViXA-KIcySuOhuINLAKSGW34EQqZhLVSx29LydvNxxhTmvyza2ns9usqe2XyfeVHDuLSsB569vfUOazlZRx0KX3jL1eD7AgCUrzV_WIAwFCI24IrNWlMOfgulSAQnDPw0T8hK6ap8uxVviKThL-2XyJy8XfaIbSXUr6wyfWN125F1mdX2KH9WeFuJlZ-T9qqAFG7wkemkv1Utq39Vg8eRjczKGlvSVhQLFptC4fmLkUh5up3Effk_ZTRWMQH-CRXyirmqscQJh8sX6sdbZv5qZGs_ehY8kRm4CuWIfXXcUpbzCFoTXQRfkRUMgxwm2N30HaFNghJ1DEmUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردم مؤمن عراق در استقبال از قائد عظیم‌الشّأن شهید حماسه‌ای عظیم و پرمعنا آفریدند
🔹
به محضر شریف مراجع عظام، علمای معزّز و اساتید و فضلای حوزات علمیّه و دانشگاه‌ها، اندیشمندان و نخبگان گرانقدر، اُمرا و سران قبائل و شیوخ عشایر و سران طوائف و مردم بزرگوار…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672738" target="_blank">📅 23:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672737">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLCw0AB0ZGhus79-fZOP96KlLVH6EafautKe53qaeFlqKfnABKzjCejd9O7t2TV-83GJgn4_VqyFvriGqpdlhWir63mwEBEaBswvfhoTRXopuOB1QjtRpSC3RQo7wKT1ymU2L6Ms15Q_2BTjRsrL80IqIfpWbssjBJ29E3L-kSUYmQBDcV7foJfdZxl2Fl_avBk9iDYuSQ9FGwUapALqe0CtB6yZuBUw856bLlBHgwZFHn1Bce31KAgEPgg66nGOQaLAotsPUqQPOn22WthTeDUA4W1nVLWs4X2aOfach9MF2cPuNfGRfdanvj7ZJ8hkj95eQUr1pev59jerEck__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع میلیونی و بی‌نظیر علمدار مقاومت، فصل جدید تغییر معادلات مستکبران
🔹
این تشییع میلیونی و بی‌نظیر از علمدار مقاومت، جلوه‌ای تمام عیار از همدلی و اخوّت و هم‌مرامی بین دو ملّت عراق و ایران را نشان داد.
🔹
بی‌تردید سران استکبار با دلهایی هراسان، تصاویر صحنه‌های…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/672737" target="_blank">📅 23:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672736">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZOlbIcrTqsb-vkk5Mc2dTu3dol8nAMVM0fOEjLY0elqAEOnRsO3vgo4gmL67lq3L6A621erzNy4pMBvnz8cBF813aILlbwUkMaEi-rL0rm5QZBoDGAuLjacs5AgjIR_sGX6arcUz7ZKgkvK5GbDil3Y6bZQ2uOZwOSbkK7PHkaGji_ao0ifLw08Hg2BgYhTzx57fNvQ5BwTHSOZQ1l-BGNr48BzrUIBGR0BkYFce0k7GPYwbku2TvyjoQqtttHKsucrYz0Tkf0tuGlqLrU3BF-MERUxpCfQ8nveC3rrI-SC0nZwDrYi9H9ht65ipGbnpgi0sNmPbvhv-6jNZYo3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع میلیونی و بی‌نظیر علمدار مقاومت، فصل جدید تغییر معادلات مستکبران
🔹
این تشییع میلیونی و بی‌نظیر از علمدار مقاومت، جلوه‌ای تمام عیار از همدلی و اخوّت و هم‌مرامی بین دو ملّت عراق و ایران را نشان داد.
🔹
بی‌تردید سران استکبار با دلهایی هراسان، تصاویر صحنه‌های باشکوه این اجتماع عظیم در عراق را مشاهده کردند و دیدند که چگونه سرمایه‌گذاریهای کلانی که برای تخریب رابطه‌ی دو ملّت به عمل آورده بودند پوچ و بی‌اثر از آب در آمد.
🔹
این حضور چند ده میلیونی هم در ایران و هم در عراق آن هم به مناسبت تشییع و بدرقه‌ی امام مجاهد شهید اعلی‌الله‌مقامه‌الشّریف، فصل جدیدی از بیداری و نقش‌آفرینی برای تغییر معادلات از پیش‌ساخته‌‌ی مستکبران را رقم زد. اینک شیطان بزرگ، امریکای جنایتکار فهمیده است که استمرار حضور بی‌دردسر و سلطه‌گرانه‌اش بر منطقه، خیالی خام بیش نیست.
🔹
بخشی از پیام قدردانی رهبر معظّم انقلاب از ملت عراق به‌پاس حماسه تشییع امام مجاهد شهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672736" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672735">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
متکی: با توجه به اینکه دشمن، هموطنان ما را به شهادت رسانده است، رزمندگان ما محدودیتی در زدن ۷ هزار تروریست آمریکایی موجود در پایگاه‌های بحرین نباید داشته باشند، ملاحظات را بگذارند کنار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/672735" target="_blank">📅 23:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672733">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rdojbL4GwW-08dNvd2cZhWZGHVRk1h0T5M6eDzecBdDeenWOn-u3UehoAmhJrI_yPIsxoH_Q1LzSybBD3lz4hWkK35B0T_akgg_DrnSaDJEWyHhlfZJxPLhHxipeq7MnXE58NkAvb3Rs1IPiztvmXtXAel_SejFCIrCvzBX2lFVkocUmly0vZ2G3Q0ofwxuEsk1gL_Q3MDjtIdsgRHgsy5AOX2ETuq0aZnGE5BJ-AITRqSFMZKraLTiH72JCaNa4sLQ0LNGukgw6dZ4KdLe7Hlbtomi1Pz_V6iiaZZOSBQwI0RJX0SnnuhKNjhSAdY8Rlky04t4S-FX_IzVh4iuagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBuGZskcW4k3_3JqJoI2ES1k-F-De0w9J6jiQxu72kYEOA8qbzsIOt0ZWlyKZTa5T2GcWrq6MIifG_tVktqebqh32xF_-HJNnj-fhUz57o68ZlY5zAbAlwScc0sYp_Rolye5M8MrpC9i7S9lJqpJ4c-OjpW23q01J27k879KhtYQOhtBMOUw791vc8Ni-2nUSThArjNGXReTsRd-6dhR0S1feGc0K4hWLLvMybIbhby0nVnxAmxjNdWw47IVlKUvZmgU_zTE4gRP6KuXFQDRO5YBAu6oCnSPy_ClS2r6Jc-QMGTijUT2noG4acskDhMIW-ZjsKjxSP5vRxLrGOe6cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر بخواهی فقط یک کتاب عاشقانه بخوانی، جین ایر بهترین انتخاب است!
🔹
اگر فکر می‌کنید عشق باید بهای از دست دادن عزت‌نفس باشد، «جین ایر» نظرتان را عوض می‌کند. شاهکار شارلوت برونته، داستان دختری یتیم و سرسخت است که میان عشق، فقر، رازهای تاریک و انتخاب‌های دشوار، هرگز کرامت و استقلالش را قربانی نمی‌کند. رمانی کلاسیک، عمیق و فراموش‌نشدنی که هنوز هم نفس‌گیر و الهام‌بخش است.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/672733" target="_blank">📅 23:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672732">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مسیر رفت بندرخمیر به بندرعباس بازگشایی شد
🔹
بلژیک واردات کالاهای ساخت رژیم صهیونیستی را متوقف کرد
🔹
فرماندار بوشهر: مردم بومی جزیره خارگ در کنار کارکنان صنعت نفت به زندگی روزمره خود مشغول هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/672732" target="_blank">📅 22:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672731">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
متکی: قطر برای تفاهم حتی ۱ سنت به ایران پرداخت نکرد
🔹
اولین محموله پهپادی اوکراین در امارات را نیروهای مسلح طی جنگ منهدم کردند؛ اوکراین در عملیات پهپادی علیه ما شرکت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/672731" target="_blank">📅 22:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672730">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
متکی: آمریکایی‌ها شعار اقدامات زمینی را داده‌اند اما ما امکان اقدامات زمینی را داریم، ما امکان این را داریم که یکی از پایگاه‌های آمریکا در عراق، بحرین و در کویت را تصرف کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/672730" target="_blank">📅 22:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672729">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae6fbe629.mp4?token=lw8i3mR5tDfFHOK7pf8hzsWxzgndE3xIvve4ZDLsYCRyK7cq8RT2UYKDMVDTO8ZCQ_Ds10F4vrxpPqQ2UlODa5wgnai8BEq3paisoppNu1dRhF5ww1Gm9EhqGIWzgkmqXlxLFFGuwKataRvgyi2XDuxgDFWZcAa86BFcds2o4m9ngAVlt6N6V-O_YBagTdwkZtSTaeb9BOaaYrSOekFRMAwcsmnyqJavg10eCf-zyb3-mG1Q59ZAkxrs1Y8vodtChBvhsEY4nKoDb3oLaa3AcXRLKZb6sCIxIeqX9CVY6t8fr665joZsa2bgB0EOHMTI6ERQbtjKy1MuM_4_S11SRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae6fbe629.mp4?token=lw8i3mR5tDfFHOK7pf8hzsWxzgndE3xIvve4ZDLsYCRyK7cq8RT2UYKDMVDTO8ZCQ_Ds10F4vrxpPqQ2UlODa5wgnai8BEq3paisoppNu1dRhF5ww1Gm9EhqGIWzgkmqXlxLFFGuwKataRvgyi2XDuxgDFWZcAa86BFcds2o4m9ngAVlt6N6V-O_YBagTdwkZtSTaeb9BOaaYrSOekFRMAwcsmnyqJavg10eCf-zyb3-mG1Q59ZAkxrs1Y8vodtChBvhsEY4nKoDb3oLaa3AcXRLKZb6sCIxIeqX9CVY6t8fr665joZsa2bgB0EOHMTI6ERQbtjKy1MuM_4_S11SRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی:  همانطور که مذاکره اول و دوم فریب بود، مذاکره اسلام آباد هم از سوی آمریکایی‌ها یک رکب بود
🔹
برای ما روشن بود که عمانی‌ها تسلیم می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/672729" target="_blank">📅 22:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672728">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E16X5VhaWLIcdwu8Ly6HcKoTQR0BeGwQwzY0pnMEfjMGQw5uaiAfTCU3z3bwfEEuf_9vstlzzEl4kTdktRYcDS7i7dArBBCG8EVI59xlc3Wp__IWXsX7MFSKQ-q-U5HLuqYyH9LJ0DARc2_S_aFpYtmf9SfA1BS3D6q8chbD5GM-arRduG9rJidgm76hZWlU8_t2oAR490GFZWVNWB2EawBU1qAb3cL--k2vtPcMDfs0sKvIQUQOknPDNNh11n3r1pP5eU7SPecCzumaEbUy6FlW3zpCBQkiq9ckoP8Egx-hks1XPvn5xorgb_gTxgwcGfmeNb7Ldt-ZcXjm_9vtXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر ارتباطات: خبر قطع اینترنت پس از جام جهانی با دستور قضایی هیچ سندیتی ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/672728" target="_blank">📅 22:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672727">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQWXC0MPYIzdndRVXUufYdz59mm39sGnfde5ArdZ6xmpsCrRQ2XeJa-NvWiLfgg4BAHRaEWJIGQtyxIQgmHjKRhOxgMVdyHDnjnQpd9IKC8SDotoqUrAQ-VtQknDKZRExad4RRXsof9ovUtPx_eay3LOdyz6guBr6Z8XSOnOz01vgmy19yicgL6hJAr06Is7fx63-7l2ZZqsesJ9LILs7c5cNJuKs3OBzwJNJxVSXrgQl3duqkBBl7FaAqMlpKlmrc0Yj3b5isoOtaYRDNsv28f-pBMlugfifnivwfiUCFR0a6Rw5ZRMa_1J-ZsRatvO0e6sSTgaUJMo-XficEqwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جین شاهین، سناتور مطرح آمریکایی در واکنش به کشته‌شدن سربازان آمریکایی در اردن: ترامپ باید برای پایان جنگ مذاکره کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/672727" target="_blank">📅 22:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672726">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfc7da749b.mp4?token=e2-fM7CWelPtCraA3EQbxdfCEon150Tmr-xcK1szG4QgT68vrPOmsB8Gv3GBoIUKZsFf6Icj6kao5y4WW2NzjYX9YfgjlfYYcyFraEeyGXIj_NS5qZ37paZoKxC5TAqzlXhYT-SSW9zr2rsyrZCE7aeAnRIFndWqQsZY301SklivNDoiba8G-0sY1gc4gFteYMFFdQO1nz6oPqXExHm_wc4ChCvLfmfJuub97Z_Afy0-xHeWkZz7cc9OsWGykZw2hQYxoL0DB_PYjdJno4B2vW8ehg3UfK-_Ml26WYeNBUxgcRpQ2hqvbzIgOtPRKQB9tMkKb516FgLCWMHBJiJYj0eAiLo1x87I5_Eg4rVGlP2TNxhEtitnFpAzsJvKaXPpi7r9_0hzUkn4x0TbyK57fNw4muywOZqq3CQMmK7EGzXBHe66ybpJa88-6wzM_i4V9MVKt7AtfQf-WuaYQsTXwBz_7Q9GJK4s5u8jg9nE6Ng_gHazXoBLriEp2HJz5jJeRQoK4iFi9H13jp7f1by80RnMTOVviIRtwoRi1X6Uk_n4ePJuO2iuhc9t4f-qI8FLzSHGyy-rvULNL24fOIAsWyN4HzPFHYaIKgwJ6bW7E6WGsr46PQBza_fuKDDA9HedQpcOf0qZLS7-PRLUK2dEiauXjtvmMfZ8GWXBuOOF_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfc7da749b.mp4?token=e2-fM7CWelPtCraA3EQbxdfCEon150Tmr-xcK1szG4QgT68vrPOmsB8Gv3GBoIUKZsFf6Icj6kao5y4WW2NzjYX9YfgjlfYYcyFraEeyGXIj_NS5qZ37paZoKxC5TAqzlXhYT-SSW9zr2rsyrZCE7aeAnRIFndWqQsZY301SklivNDoiba8G-0sY1gc4gFteYMFFdQO1nz6oPqXExHm_wc4ChCvLfmfJuub97Z_Afy0-xHeWkZz7cc9OsWGykZw2hQYxoL0DB_PYjdJno4B2vW8ehg3UfK-_Ml26WYeNBUxgcRpQ2hqvbzIgOtPRKQB9tMkKb516FgLCWMHBJiJYj0eAiLo1x87I5_Eg4rVGlP2TNxhEtitnFpAzsJvKaXPpi7r9_0hzUkn4x0TbyK57fNw4muywOZqq3CQMmK7EGzXBHe66ybpJa88-6wzM_i4V9MVKt7AtfQf-WuaYQsTXwBz_7Q9GJK4s5u8jg9nE6Ng_gHazXoBLriEp2HJz5jJeRQoK4iFi9H13jp7f1by80RnMTOVviIRtwoRi1X6Uk_n4ePJuO2iuhc9t4f-qI8FLzSHGyy-rvULNL24fOIAsWyN4HzPFHYaIKgwJ6bW7E6WGsr46PQBza_fuKDDA9HedQpcOf0qZLS7-PRLUK2dEiauXjtvmMfZ8GWXBuOOF_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی:  همانطور که مذاکره اول و دوم فریب بود، مذاکره اسلام آباد هم از سوی آمریکایی‌ها یک رکب بود
🔹
برای ما روشن بود که عمانی‌ها تسلیم می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/672726" target="_blank">📅 22:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672725">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای پوچ هگزث از خدا خواست محافظ نظامیان آمریکایی شود
پیت هگزث، وزیر جنگ آمریکا در واکنش به کشته شدن نظامیان تروریست آمریکایی:
🔹
خدا نگهدار قهرمانان؛ فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/672725" target="_blank">📅 22:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672724">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
روزنامه آمریکایی خبر داد: تمایل ترامپ به گسترش جنگ در ایران؛ از تصرف جزایر تا حمله به سایت هسته‌ای زیرزمینی
وال‌استریت ژورنال:
🔹
ترامپ پس از چند روز دریافت گزارش‌های توجیهی از سوی مشاوران ارشد، به سمت گسترش عملیات نظامی در ایران متمایل شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/672724" target="_blank">📅 22:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672723">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
رویترز: به دلیل کشته شدن تعدادی نیرو آمریکایی،ترامپ دستور داده که در ساعات آینده، یک حمله قوی انجام شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/672723" target="_blank">📅 22:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672722">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
به گفته برخی منابع خبری صدای چند انفجار در بندرعباس شنیده شده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/672722" target="_blank">📅 22:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672721">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlstTpfnXRxJ7sb6EVraa_tHhyYYCTwCbLYMfpRZfcLCvHPY3s1JLEnXxo85Dc4GnomPP0Gv99BCIp51Y85emjOR0XItG2bLwieM_rpcrYlk5_lyu2ktaJVdQ9Uo_93EfEN6DV08Rrf42w58Zvv8lb0b_q4SGVYyeQoj_VaSgccmfbT6aZAdC-x0CPzDo4vchGLs8lbUrkOdBk4Ugw8Y6ykRWAhf96ieElhr58A9Gb_9lEWsv_FnOE8rI9wQ0WPx4v_K6CWvba4COcPh_EbJbI97ioJGhyLMsqtGApZuN-x9jWvDdPkyOYvVNuRsMkgQR7XvCYBHP4xNc9HqEVpf2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ما بازی به نفع شماست
🟢
همه در حال حدس قهرمان جام جهانی هستند، اما شما با چیدن ترکیب مد نظر خودتان از صندوق‌های ترنج، شاید برنده‌ی ۲۰۰ میلیون تومان صندوق طلای رز ترنج شوید.
🟢
کافی است وارد لینک زیر شوید و ترکیب مد نظر خود را بچینید.
🔗
cup2026.toranj.ir
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/672721" target="_blank">📅 22:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672720">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
هشدار سراسری آمریکا به اتباع خود برای انجام سفر خارجی
🔹
دولت تروریستی ایالات متحده آمریکا در پی تحولات اخیر در منطقه خاورمیانه و افزایش ناامنی‌ها، هشداری سراسری برای شهروندان خود جهت انجام سفرهای خارجی صادر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/672720" target="_blank">📅 22:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672719">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام قدردانی رهبر انقلاب اسلامی از ملت عراق به‌پاس حماسه تشییع امام مجاهد شهید منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/672719" target="_blank">📅 22:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
هشدار جدی بغداد به دمشق/ دخالت در پرونده لبنان برایتان گران تمام می‌شود
🔹
روزنامه «الاخبار» لبنان در گزارشی از هشدار صریح دولت عراق به احمد الشرع (جولانی)، رئیس‌ خودخوانده حکومت سوریه، درباره تبعات هرگونه ورود به تحولات لبنان خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/672718" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672716">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4495c0bcbe.mp4?token=OqsEEx15jwJrxcTmz35g5MlYjj8gSazqTMlXPi4FQRRkWrw2Y5Yk-9GIz_qUFZaEMewdToRj3AroZuMdD05jz-DJpfCbfkVuYQsE0YjXl1sJyAYhz-ZFiu5xfqJ8hfhWPBGIYzju0TSwa4mHLFVRaNm9M-NpsX2leJOhCDRNd3eHdD20rerz6lpN2cVGBltGqgpMRUdES3b340uwP5kuPbZf1WJxLLCZX0wVQhuOXBZv0yDduBRigvfO4KkA6fWYSPR5qFSa9mw5XcR_9UJ9r_sS49MOyJwH54WVJ_k7von-Eled-BTZ1nsO4cZcHfSqq0tNmTkbYoN7dx6-7-pTfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4495c0bcbe.mp4?token=OqsEEx15jwJrxcTmz35g5MlYjj8gSazqTMlXPi4FQRRkWrw2Y5Yk-9GIz_qUFZaEMewdToRj3AroZuMdD05jz-DJpfCbfkVuYQsE0YjXl1sJyAYhz-ZFiu5xfqJ8hfhWPBGIYzju0TSwa4mHLFVRaNm9M-NpsX2leJOhCDRNd3eHdD20rerz6lpN2cVGBltGqgpMRUdES3b340uwP5kuPbZf1WJxLLCZX0wVQhuOXBZv0yDduBRigvfO4KkA6fWYSPR5qFSa9mw5XcR_9UJ9r_sS49MOyJwH54WVJ_k7von-Eled-BTZ1nsO4cZcHfSqq0tNmTkbYoN7dx6-7-pTfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت آب‌گرفته خیابان‌های نیویورک در فاصله ۲۴ ساعت تا فینال جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/672716" target="_blank">📅 22:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672715">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
علی الزیدی، نخست‌وزیر عراق در ۲۳ ژوئیه به ایران سفر خواهد کرد
🔹
بغداد حامل پیام آمریکا به ایران نیست؛ اما می‌تواند علاوه بر ارائه موضع عراق، آنچه را که از نظرات واشنگتن شنیده است، منتقل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/672715" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672713">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4zOmNatgpPXcyleTb2zTekW_UgjEwPu-DZYLZAZWnz-D9fPqg7IkFLpDEM9_Uo-GgaDrKPmA2qc5H7hlU8vptOgMsicXNMA0v1cYU6MNX_QlpBPAflpBlqIZB6OAFuYLQHR2O0jLbD2rl9YD31QpY9qRb4Meu11dCpG1DPSMoNNl6avhYGCpF2j4-QoFzvS_-VuJpTLGVAaIapxqLWaPjIijbp79nFvG50QlBCgU9QFvTVCCzwtyDUPiFO1HipQSQLmAEpwx9JdK4S9bioaqJUQoPpHOZM1ewYVUySjufx8qXOEujaD7PXm1AhbdSWCHsP27LChdnV_BCydAJ22kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«همه باهم برای ایران»/کمپین ملی صرفه‌جویی در وضعیت این روزهای کشور آغاز به کار کرد
🔹
در روزهایی که دشمن شیطان صفت با حمله مستقیم به برخی زیرساخت‌های حیاتی کشور در تلاش است که اراده ملی ما را تهدید کند، نقش مردم در حفظ پایداری کشور بیش از همیشه اهمیت دارد.
🔹
امروز باید «همه باهم برای ایران» پای کار وطن بیاییم، یعنی همه ما با یک تصمیم ساده اما اثرگذار، از سرمایه‌های مشترک کشور محافظت کنیم.
🔹
آب، برق، گاز، سوخت، نان، مواد غذایی و همه منابعی که با تلاش فراوان تأمین می‌شوند، سرمایه ملی هستند و مصرف مسئولانه آن‌ها نشانه همدلی و مسئولیت‌پذیری ماست.
🔹
این روزها، هر قطره آبی که هدر نمی‌رود، هر چراغی که بی‌دلیل روشن نمی‌ماند، هر لیتر سوختی که بیهوده مصرف نمی‌شود و هر قرص نانی که دور ریخته نمی‌شود، سهمی در حفظ توان و پایداری کشور دارد.
🔹
«همه باهم برای ایران» یک دعوت عمومی است؛ دعوت به اینکه هر کدام از ما با پرهیز از اسراف و رعایت الگوی مصرف در کنار یکدیگر کمک کنیم که از شرایط فعلی عبور کنیم...
#همه_باهم_برای_ایران
#صرفه_جویی
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/akhbarefori/672713" target="_blank">📅 22:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672712">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fddfe1fcd.mp4?token=Vqnd8JjkfCq7Vf3ga4gXTrhFMSliLvM5kF_1OxJxCaD-c-SWW2s4fEz9wq2MswBp3XbSV4cGdcxAgsPIqFO2NRmT4fVwEk8G4LPVEAOismrUsNO-e75KKKaeobQNXdlLxyrTXuCAZxhCkFuv8zhQYgWQdHcxXG12-4NDOiSDHZ3yyWrHwFFNlxm83Evq7VNdmTQTngQjKDvKtlO3Ak8lSS6lQV7WngXw6GbVahJj7fjeOm0m8GmzczZcfXMm0yYTQKU4QFxetsfr3scfzl5Aw3b7GMM95qsy_ExwkF5N0QvphAY6GPJaBQKQt6Mfn_RoJ3j6APF2VymRgfF8AUx4Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fddfe1fcd.mp4?token=Vqnd8JjkfCq7Vf3ga4gXTrhFMSliLvM5kF_1OxJxCaD-c-SWW2s4fEz9wq2MswBp3XbSV4cGdcxAgsPIqFO2NRmT4fVwEk8G4LPVEAOismrUsNO-e75KKKaeobQNXdlLxyrTXuCAZxhCkFuv8zhQYgWQdHcxXG12-4NDOiSDHZ3yyWrHwFFNlxm83Evq7VNdmTQTngQjKDvKtlO3Ak8lSS6lQV7WngXw6GbVahJj7fjeOm0m8GmzczZcfXMm0yYTQKU4QFxetsfr3scfzl5Aw3b7GMM95qsy_ExwkF5N0QvphAY6GPJaBQKQt6Mfn_RoJ3j6APF2VymRgfF8AUx4Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شلیک موشک های آمریکایی به سمت ایران، از خاک کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/672712" target="_blank">📅 22:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672711">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7XS20UbdUePoASlxXnulJ0vzqtaimseXA3jzDFRJ9Rf4aTcP8lSyIf23fzXUgcbgdkrqb4T1TlykZxPI5Q1ucnTMB23AMoF2n8CwX-2rQyd40jfKVaJsi0oDFstFyFcE0TkUByi2GuwLuS5tt6YJnBFq8BBgSeIvMwyd3dRbaZGH9ySuiNxCec1ml3AfoIyLrbONzi5uYZrjJNChfgENz82i65PmjyqLggBO7xZxiDnWT8YNzT1df-VJuthAudOR-RmNAWs9bJiGPeeTmYfjS02ONoXx1y3JPOLClHvJFWuNW4tinu0N8leWsoY4X86tYKZ4L7MSoZnVT1ENjgKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
ویژه‌برنامه عزاداری شب شهادت حضرت رقیه (سلام‌الله‌علیها)
🎙
سخنران
خطیب توانا، حجت‌الاسلام‌والمسلمین استاد حاج شیخ مرتضی ادیب یزدی
🎤
مداحان
کربلایی جواد مقدم
حاج سیدرضا تحویلدار
📅
زمان
یکشنبه ۲۸ تیرماه، ساعت ۲۱:۳۰
📍
مکان
امیرکلا، میدان انقلاب، حسینیه اعظم امام حسن مجتبی (علیه‌السلام)
🌐
کانال رسمی
@gharib_madineh</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/672711" target="_blank">📅 22:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672710">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
انفجار مجدد در سیریک و جاسک تکذیب شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/672710" target="_blank">📅 22:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672709">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f4d4b9b2a.mp4?token=nwezV_3g-R0KRiGWRWuMuDu37UQVRivtvwfaVoU_PM7izRk7jx_YH5mmNW_qxKdPAhL8JV7SnU7Cbfw_od_8NySDTeBnHMCaUOygX2TrVNIAzKXbyECoNxhFORGZT_TV25pu6FjAQ3DEaNgJrp2mJOAtzxBOZeiYd8VGyHMkvEKoLBbzga3GFKQ-OheVv65Dw0zZKQ4bm40oZilQKJNShs3c4GGHVBt_coPXi_7zV-FAQ7zDIrOea2PCyvfZx8N5dmFzpcuucpf3vn2VzJvS8PJEltuhMz4Hic0EWllyPc0b47krFPfULaWswWVKideduVXL3UUes5wQJAxb2AlT3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f4d4b9b2a.mp4?token=nwezV_3g-R0KRiGWRWuMuDu37UQVRivtvwfaVoU_PM7izRk7jx_YH5mmNW_qxKdPAhL8JV7SnU7Cbfw_od_8NySDTeBnHMCaUOygX2TrVNIAzKXbyECoNxhFORGZT_TV25pu6FjAQ3DEaNgJrp2mJOAtzxBOZeiYd8VGyHMkvEKoLBbzga3GFKQ-OheVv65Dw0zZKQ4bm40oZilQKJNShs3c4GGHVBt_coPXi_7zV-FAQ7zDIrOea2PCyvfZx8N5dmFzpcuucpf3vn2VzJvS8PJEltuhMz4Hic0EWllyPc0b47krFPfULaWswWVKideduVXL3UUes5wQJAxb2AlT3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر خارجه: پیگیری حقوقی خسارات ناشی از جنگ‌ها در سه سطح درحال انجام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/672709" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672708">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
فرماندار بوشهر دستور تخلیه به ساکنان بومی خارک را تکذیب کرد
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/672708" target="_blank">📅 21:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672707">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
اعتراف وزیر جنگ پیشین رژیم صهیونیستی به عدم تحقق اهداف اعلامی علیه ایران
وزیر جنگ پیشین رژیم صهیونیستی:
🔹
تلآویو به هیچ یک از اهداف اعلامی خود علیه ایران دست پیدا نکرد و عملیات ها علیه ایران شکست خورد و هیچ‌ یک از این اهداف محقق نشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/672707" target="_blank">📅 21:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672706">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAqc3nc1VvkLoyC4G3wGao0NJToKhZOoKdmQeb4fq7rA9tExUBvLnLPRp-tVOlq83OZwR2jE8MWA4zY9AkG7jTDWXd7ttdqpZwnYU0EB_lrIrvE-Osfxx-AJjLo_sGf96y0foA2Pbn2DXPySXIGLC9KOiuHZxPoO2oLf0jpBO4M9dAUR2ARmXyX78rdx0wcth9URM_3tZ4sogDuYdZylLBdUVDSAnLhxddhKC3eGne83tBbzPB9XpiRIYAbzG5IhBQpKo8iOuaSKqLALMtcJfly0p-mBFwQ3GD6npEFT0jLkJOrQYhJD1zCX1fPJDvKqjyLBDIvIjwwlfuuABzcSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز فقط قیمت‌ها عوض نشدن...
ارزش تصمیم گرفتن هم عوض شد
💎
اجرت از ۳٪
🏦
بانک طلا؛ شروع از ۵ میلیون تومان
🔄
طرح تعویض با عیار ۷۵۰
👰
مرجع سرویس عروس
📲
داخل کانال
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/672706" target="_blank">📅 21:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672705">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5-IIOWSDqQmB0uptCm0Y2JmWyEP7OaUQzJI8wswOXYD0mge91UUXO9HdCTyTeBwwSF7jLqfgqaxSwjN5mHSmj_oYosTH02aoEU-VDpUbG_vit-oQHI4Ydm1vbqYyKcaKg071JlCZnp2GpoOM5uiEbJIARqvhfkcJETLZCVGi6VhCSHPMbHsKP-sQuq032YSAd7H8OxlUhrmoFfhTz-hDi-ycIMn2w0Op7W6Yupo1Ofy88IA1F5O4Du2s0WTzUcuoY5C8WkDR1uUiAkfIHNzNQR5vTm5BTABZ_ZX858XWNvjcWsRKmsXJ36bTCl3ic1eHkHaS2RCxXa3bfkwYnwMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تظاهرات علیه نتانیاهوی کودک کش در تل آویو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/672705" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672704">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0W1Djs2RVKdraWOMsaHuA70ok_8CUfQNDff1Dt8Rt8etzrBtC2Psiazgok0r5JanNysmjgsc-c_vFOW0bybfSw_KHoRdba1AuA3xwsLYxyetju38xFh9m17a0icBqcRPK5gdM29ZpdRjwnZOsDgUHJm1azyawQgmcVsd4PIFzzLuJNjHz0rK4Ab-Yb2hJFBytlxr5hcMAHq-6EMbCyIGwqrqOpuKIPcRr45NOIEsNyvGZaEqm53EutglIW_i21PWPrkbstd6aDC8RZirLZRTIirJHzX7e0WMgbOatvN90NrgcATQCnoF8mE0OGuYytkTDL7n8gMUmoxrtEebfJ1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: پیام حکیمانه و وحدت آفرین رهبر عالی‌قدر انقلاب اسلامی و حمایت ایشان از سران سه قوه و مسئولان کشور مهم‌ترین پشتوانه و سرمایه در جهت صیانت از منافع ملی و سربلندی ایران اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/672704" target="_blank">📅 21:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672703">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnWQqFyj7DLxmaFcx9Bz_uZCtCPEsDoWZxkM6IlBm2f4bcgRjzdXYjwJ5y_BLnzGK3hBT1OEkqDQhpM_xcgvsPhsoXsGv5F_TZt2h7YCEUQKnLEyGvQAqJY_ErWLBrBj_Q79UsrnLofk2dW9W35ksyH3PXrebIEehf48JmgosyfjcjzixsdrSK9HSWa4h4XpkYUu_8KazYbkIdSwOu90Zs92UvRqHhGvYP2Xsa6gyhL1XoGEHm_PUcZiDr8kNz4sCJo5vWV6Sz05--bvEk6N7AYgahRQFsUZksCLDj_5POilTMF4F6_Yv3vYIVDIckg1BDjfaj3ThnDCXWZH9moQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان تداخل با سیستم موقعیت یاب جهانی (GPS) در کشورهای حوزه خلیج فارس به سطوح بی سابقه ای رسیده است و این میزان تداخل حتی در مرحله اول جنگ ایران نیز ثبت نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672703" target="_blank">📅 21:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672702">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009c2f2675.mp4?token=FvU7KpawUW-2QzwxwFRbkfZo18cPwBuShLF2jAIbbMcCh41t9QDzUNixBMoPj2y1VjQGV_zay_cJhWqtBK4k5-KC4BCcHNuRxkrKEWj4KqR8Ai2NFElpq7uWarb5CJFooWCYtNCafTdERI2fyGjKJ4ZzqbWuNqUBmWJ3pIkrX0F-YtjfPBekfOprMLOTtsOt3lCtRTXrGhwyk_5Az9HW4-J7N1PElcxWWHl6g6wp525cGlVWAui4fcPBeHOPG8KEuuqSdZC2RdUwH5D1Eeum700wPj7dNFfQRHxGICupQQNkTaUIwcngt5mhI9nfEyRS1G5i_3AFiY4OUtjMYwJbgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009c2f2675.mp4?token=FvU7KpawUW-2QzwxwFRbkfZo18cPwBuShLF2jAIbbMcCh41t9QDzUNixBMoPj2y1VjQGV_zay_cJhWqtBK4k5-KC4BCcHNuRxkrKEWj4KqR8Ai2NFElpq7uWarb5CJFooWCYtNCafTdERI2fyGjKJ4ZzqbWuNqUBmWJ3pIkrX0F-YtjfPBekfOprMLOTtsOt3lCtRTXrGhwyk_5Az9HW4-J7N1PElcxWWHl6g6wp525cGlVWAui4fcPBeHOPG8KEuuqSdZC2RdUwH5D1Eeum700wPj7dNFfQRHxGICupQQNkTaUIwcngt5mhI9nfEyRS1G5i_3AFiY4OUtjMYwJbgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای نزدیک از لحظه اصابت موشک ایران به پایگاه موفق السطلی اردن که منجر به هلاکت دو نظامی و مفقود شدن یک نظامی دیگر آمریکایی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672702" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672701">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b8938fde.mp4?token=P_YMhxY-TZC-trIihuWttfeid93gOwFIM-4a0Pj9WjvDVL1q-320ayFmA-nx2PGVJBaVuNiX5cUgqb9oBGI4_TzYszXMYiooadFGrI01M7g1dQj4sr9yBjYIVI0klJyMckPZTRyc_ZrezRwgHvHZZY8e_faXIpdjhvmxUZwa7AWpyd95mWYnMZEnu3lWbNYSnKKrfRP-8c39qg08H9lOjylT2imLEMkjEfzAw10Qh4znx6bcZbEhuA2ohIIUHmLuDx_c0UcEjvWVgIMZkVvVR4NJK54LI_Tzt7GKMAxQ33Ov22hduYbN-d0_qTiuTIeZe9hMhDoolGrGlSCHqqwKGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b8938fde.mp4?token=P_YMhxY-TZC-trIihuWttfeid93gOwFIM-4a0Pj9WjvDVL1q-320ayFmA-nx2PGVJBaVuNiX5cUgqb9oBGI4_TzYszXMYiooadFGrI01M7g1dQj4sr9yBjYIVI0klJyMckPZTRyc_ZrezRwgHvHZZY8e_faXIpdjhvmxUZwa7AWpyd95mWYnMZEnu3lWbNYSnKKrfRP-8c39qg08H9lOjylT2imLEMkjEfzAw10Qh4znx6bcZbEhuA2ohIIUHmLuDx_c0UcEjvWVgIMZkVvVR4NJK54LI_Tzt7GKMAxQ33Ov22hduYbN-d0_qTiuTIeZe9hMhDoolGrGlSCHqqwKGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کانال ۱۵ عبری: تشکیلات دفاعی اسرائیل در حال آماده شدن برای احتمال تشدید تنش بزرگ در منطقه است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/672701" target="_blank">📅 21:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672700">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCFx_VyaZdyqZGmiOKv-SFBkGJ5ZzirWhKtcaJ_AEpruYzt5kI_p270kG3jVMtBD5S8ZdaHaHxL6uh5BeSxH3ZrSeMQ1G6KKaMdYFSLOS3WkB8qXLz8gHIWb7ydZ0d1LmZ2swjEz8GsugpcMC2WoeSoH32dylZZCquPtVY38s5ldSwou13-Y_GpIGJIytiEz4g53H4Lia4NrRxcFDHAjIRQGDboaetQZ6LECkUwBob-TXoRmGzYiMCql6-zZaYf6aMvjuVp-uW8vr5BrrCl78itug4d-ck0XXIa6a4rRwIc9HqGV8VWGKjdbk0LT1cI_Z-IufBRWRA5vwI-PpPK3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۹هواپیمای سوخت‌رسان آمریکایی اکنون بر فراز خاورمیانه در حال پرواز هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/672700" target="_blank">📅 21:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672699">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn2hgdhYL-OXx_JF8KzXS6wUF2qi9S1XHHWefYo0TgEnpAKJ3__qQwhRu1ZwvnDGDHBG4hIaIkLmOY2BUfyOkF2P6d0qLxj_N3-MGcu1WkdKQPLjgdFBgemYLw_dWywMuyS0z3phAD7dX4q7DhhjLsdEEuZPBjbu8Ugejd1nLvYIrvzcZGdWdkFAk_85pT-rX7T-Nt-YL9iz9Ohg1wodI3Fl-Uz7g1n0aUkrHLm64XzAmya3iWEAFHp5xv7EvvNypmfhi_V0_u-8zG0KsA5bOYXywQOyDP1tJ4-GgYOgsSM8DKH9n8GdC7yTkWHz7J52P_GjFTABa82d8ZkbBz41Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سید مجید موسوی: حاکمان کشورهای عربی اخرین هشدار ایران را جدی بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/672699" target="_blank">📅 21:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672698">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
هرمزگان از برنامه خاموشی‌های برنامه‌ریزی‌شده برق خارج شد
نماینده مردم هرمزگان در مجلس:
🔹
وزیر نیرو با تایید شرایط خاص هرمزگان و برخی استان‌های جنوبی، دستور لازم برای خروج این استان از برنامه خاموشی‌های برنامه‌ریزی‌شده را صادر کرده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/672698" target="_blank">📅 21:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672697">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
کاخ سفید: سفر رئیس‌جمهور چین به آمریکا همچنان پابرجاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/672697" target="_blank">📅 21:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672696">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/narQK6jwGLzB5Xz7RSmQoYJUE0J7Pwbnw9RuvD8C4ecXRlAS9AjwAxGkTRqe2eicZCgnr4Lwyw1g0eO0pQTTYELnqZFSNURUYCXqk3mdA5S93HPAKH9O5JnZCgejcXpAgjkCnCZKFDPf-iWzW4_hEKb7iRI-FWtW0aMlBI8lA6ZkXoLU813pvvYaphcZtLRNgQGLJtJZ_tZUw73mKq59tkMJRfTn20XzneKHDVE4-BsAjoIA32szrqf0CJ3Aw2AEZigyqWVtD00DCqTJvf9wR27lu79L0jVX1PvldY_8JOVMPO5U-CsD_hx9XEHaqKkjigD-UnW1LocG7tyRTfEOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در جریان حملات آمریکا به پل شهرستان خمیر در استان هرمزگان، ۷ شهروند از جمله ۲ دانش‌آموز جان خود را از دست دادند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/672696" target="_blank">📅 21:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672695">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3LWQvLp7NLbLcQLRvoSENvLXpOGfG6MPgTbAeJj19DcuC1DUFvgcCIa-BGZE-_fF3QJ_86ywIET3YzeI0d6JyoDZbtD4M6M2MDF3qrCNObghZD55MXf0U7iAnHhNDzcEUBzrmsVxli5ucFPPMmCebYizW1qnDA6TqZU6d5m3lhGLmpMcJBv2koRQ4gVfN1A_cWoNPEsR5fU9VSRoR74oXasogrjlqQkmasAfZQrvgCsFLS2WUbR4gJ18Qvdg_lPqgjLK3SwuD6CihisIZGOI3M6lxBl2uEApEFmsOkIUxxVoeuUEmDbUDDnXLZPnK68NH5XpUxH7O4JD3nfAKklyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام امت اسلامی
آقا سید مجتبی حسینی خامنه ای
رهبر آزادیخواهان جهان</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/672695" target="_blank">📅 21:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672694">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc93bd0cb.mp4?token=OJwUL7nT3952_vtXThZEOaAwYzaEggFAr23y6_c-W7kuE33360c7u0pxH-kTstj39a0VBdcn813gHnGXurGMk2Fwfoy8NFcukeyXlkgvbc20LjspUiGkdHfVhJhL6_M6zRfnRD4oMdVnO-6L4M5vsHjO413_9tMRCOrSoxjgOjlFgzyqknPyOrPMgvssKI8eDbVWy8MrPAqoB0RG1aptbyGQ2OuxBxdpMO7rJ8PO8mmWLA7pzQDJSGYg_IwigJfNrkl_ULiVDFbauH_gSONKcaH7xPNaWh7Wlkvriw-MnAIhHVEaE83rMuIrd-HMHH6iZcYGzBCupF_xEG7RQgCPRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc93bd0cb.mp4?token=OJwUL7nT3952_vtXThZEOaAwYzaEggFAr23y6_c-W7kuE33360c7u0pxH-kTstj39a0VBdcn813gHnGXurGMk2Fwfoy8NFcukeyXlkgvbc20LjspUiGkdHfVhJhL6_M6zRfnRD4oMdVnO-6L4M5vsHjO413_9tMRCOrSoxjgOjlFgzyqknPyOrPMgvssKI8eDbVWy8MrPAqoB0RG1aptbyGQ2OuxBxdpMO7rJ8PO8mmWLA7pzQDJSGYg_IwigJfNrkl_ULiVDFbauH_gSONKcaH7xPNaWh7Wlkvriw-MnAIhHVEaE83rMuIrd-HMHH6iZcYGzBCupF_xEG7RQgCPRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: خوک (۱۳۹۶)
🔹
ژانر: کمدی سیاه، درام، معمایی
🔹
خلاصه: ترکیب عجیب و شگفت‌انگیز حسن معجونی و لیلا حاتمی را از دست ندهید. خوک، ساخته مانی حقیقی، داستان کارگردانی ممنوع‌الکار را روایت می‌کند که در اوج یک رشته قتل‌های زنجیره‌ایِ کارگردانان مشهور، تنها…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/672694" target="_blank">📅 21:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672693">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHGS2k8rbLfA8tYsExmYMcceoEOKcKTRUCMzUHcaYlCoI0pfBlUKOJakPJTbcv3erDGgyBNfRcEVbWDIzs2u08U8e3MuYIPN7bEtAEQgDbKXpq5zAMeB6zGS-OwlrXn3WTD7KbrvALTXQSY9xzQ4DiJn-PdC8Z8n2_2-S1ZmIQv7rJjsKu_Ze8_n2a-G8IE5nnklJOw3DgWqK1YdjSX1aqlEYHnJVaIu0VYEuW7utJ9WkA5OQVfbU5s4-VCJ6e9PAbN9neqoY9vTNdXXrkfuzuf8qWYcCAYLZxHQHPpIoDMxlJaz5nR4JePRMpyzVh19_UeaalpEtpmb2Mht1MlgHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک در یک روز ۴۰.۵ میلیارد دلار از ثروتش را از دست داد
🔹
بر اساس تازه‌ترین رتبه‌بندی فوربس، ایلان ماسک، ثروتمندترین فرد جهان، بیشترین کاهش روزانه ثروت را در میان میلیاردرهای رصدشده ثبت کرد. ارزش دارایی او در یک روز ۴۰.۵ میلیارد دلار کاهش یافت و به ۷۹۷.۶ میلیارد دلار رسید؛ با این حال، ماسک همچنان جایگاه نخست فهرست ثروتمندان جهان را حفظ کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/672693" target="_blank">📅 21:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672692">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bbb86703b.mp4?token=XlEy2IVFLbDe9W4sxnzz6TS9EXJlrIt9-x-oOhTrZEOGx2cHNWfxMWzhq6KxIuthMecDlQyJH16TkR5D2_mglqOKznnsodnyz8l5q8FuAYKhEh6nTOA-YbRQvWPAfZgfrh5UYtRUvx9MEh8KPDBHdhHhqo70BuY8ltrmlY2pTfuKv7Qpakg5ogvY_-gMQ7jiijAoUgoUrvM6sR2zXeoZ9bVs4lshmKIitYiL4U0g7HnwzeOLxs21bPfHNrFCJpd7zfNUhdsKZSL59EkeN9G-9LojtOzcl-QvYo6q_dAhHSQZjNXBXVihDB9gKlrWgMGiFy29-0vhARbsrQKTt45YAoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bbb86703b.mp4?token=XlEy2IVFLbDe9W4sxnzz6TS9EXJlrIt9-x-oOhTrZEOGx2cHNWfxMWzhq6KxIuthMecDlQyJH16TkR5D2_mglqOKznnsodnyz8l5q8FuAYKhEh6nTOA-YbRQvWPAfZgfrh5UYtRUvx9MEh8KPDBHdhHhqo70BuY8ltrmlY2pTfuKv7Qpakg5ogvY_-gMQ7jiijAoUgoUrvM6sR2zXeoZ9bVs4lshmKIitYiL4U0g7HnwzeOLxs21bPfHNrFCJpd7zfNUhdsKZSL59EkeN9G-9LojtOzcl-QvYo6q_dAhHSQZjNXBXVihDB9gKlrWgMGiFy29-0vhARbsrQKTt45YAoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران وطنم
🔹
پیام‌های صوتی مخاطبان خبرفوری در پویش «ایران وطنم»، روایتگر همدلی، غیرت ملی و همراهی مردمی است که با لهجه شهر خود، پیام امید و حمایتشان را به مردم شریف و مقاوم جنوب ایران رسانده‌اند.
🔹
این صداها، نشان می‌دهد که ایران، با همه تنوع اقوام و گویش‌ها، در روزهای سخت یک‌صدا و همدل در کنار یکدیگر می‌ایستد.
🔸
شما هم با ارسال یک پیام صوتی، صدای همدلی شهر خود را به گوش مردم جنوب ایران برسانید.
👇
#ایران_وطنم
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/672692" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672691">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
استاندار هرمزگان: تردد در تمامی محورهای مواصلاتی استان برقرار است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/672691" target="_blank">📅 21:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672690">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
حمله مجدد و نقض هزارباره آتش بس جنگنده‌های رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری لبنانی از حمله هوایی جنگنده‌های رژیم صهیونیستی به اطراف شهرک «کفرتبنیت» در جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/672690" target="_blank">📅 21:13 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
