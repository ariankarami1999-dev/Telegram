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
<img src="https://cdn4.telesco.pe/file/AfcILezzwYHZNbc0Dx8ZI4rh_G7jP7EZhqh2YyOliUjfgbcxjyJMKypq7wSKu4pSd-wrF4rtE_deyZJ6ctpkShhv0gmna9R2gJ0VAC7_qJgHwC08KcIhl8-8J3cMb8q2XhR3I8SXzVA90HaDHfRrGL-tEaD3PmjttuiPF7AWGsr8P3FadUyhsfo2VcCje4MmdnsPuw2mBcMPx7Ppm7Hy7OOBZZ4nJgj1i0u3D72tABB2DLJgnHbnnBbqcjjXNZYiagMlhg1Jpf1tv_0BEdG1FaUcvr1gdsURiJ-HbUojLzcCBBFmcPSKERcshazC4hgVaxMrpMDDnGHtxd74vBHF8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 19:05:01</div>
<hr>

<div class="tg-post" id="msg-677781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-pSS-aCdegKtdYa_BuyAr8UchWxMGfo0jiULz_WE_bttzbi9dMCpi_vykYg7b7-5Tw2rcxu3m3Ub7ccC6RDxxgBNr4Y9CiuSMjJGByHyX1RTwP2j1fJcKfN5nmxEcp9xMn7fyvQDTlnf1SnQmeSeI2xndSILwNQe1mVRFZu_0BQMZyJfWRnXb0ZxwQj-ZFH19X1qzM1e325oUk0UkEy4ihZVO3H1EBhXHX80Jy_ah3czoAftiU4pbxJeXrIXMDMs2_EoaTPtgSF91Gf19l8DjXBxew_fAZPAYV9Xx8OSuoqDlSqeOrkTYhcblr78vjknwHQjYFk_WnqqQ1ZqyK_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران با کمترین تولد ۷۰ سال اخیر؛ ۸۹۲ هزار تولد در سال ۱۴۰۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/akhbarefori/677781" target="_blank">📅 19:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
سخنگوی دولت: قیمت بنزین سهمیه‌ای تغییر نمی‌کند
🔹
سهمیه ۶۰ لیتری بنزین ۱۵۰۰ تومانی برقرار است و سهمیه بنزین ۳۰۰۰ تومانی نیز ۵۰ لیتر تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/akhbarefori/677780" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677776">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5020d09a.mp4?token=bct_iioPp41etqO4tmX76BWbmZ-5pSqfqDpvczre8Myhh2Ioyxmeamo5l0NQk6ZjTu-pw5BfC9PnwlArRZFNNK8t01-u6ywaLtMPMmZTQyNqydS8c_PBgKegDYsu3f2pgdf2PUBXvQphRCecad7ciKksy-0QsQkJGeWqU5tQ4djCulFFONC52gpqvgszry1dMOCm6ZCQJwpQrXugY8cOdGLq8rLpHHN3hcNb5M8bvSZyabIYvgPP1vbSOdZb4ggg-tVmpi4Mb0H8Irdbatd0Wba1aMJytevi9qDGRaGiX7ktfissFLg2WKYhFkBlOpReemTNM81AhaEY1Y61pQn5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5020d09a.mp4?token=bct_iioPp41etqO4tmX76BWbmZ-5pSqfqDpvczre8Myhh2Ioyxmeamo5l0NQk6ZjTu-pw5BfC9PnwlArRZFNNK8t01-u6ywaLtMPMmZTQyNqydS8c_PBgKegDYsu3f2pgdf2PUBXvQphRCecad7ciKksy-0QsQkJGeWqU5tQ4djCulFFONC52gpqvgszry1dMOCm6ZCQJwpQrXugY8cOdGLq8rLpHHN3hcNb5M8bvSZyabIYvgPP1vbSOdZb4ggg-tVmpi4Mb0H8Irdbatd0Wba1aMJytevi9qDGRaGiX7ktfissFLg2WKYhFkBlOpReemTNM81AhaEY1Y61pQn5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت سرکرده کارتل مکزیکی و مهار شورش اعضای آن
🔹
در پی دستگیری «پانچو» با جایزه ۵ میلیون دلاری، اعضای کارتل او دست به شورش خیابانی زدند که نهایتاً توسط نیروهای امنیتی مهار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/677776" target="_blank">📅 18:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZi7-0r28v8mPO_JErL01R80STkwTRC4_Srg0-RUkVicBRUuWWrpxG3awr2CB69EbispI-QB-KKPZS1D7LRgqu-fu-iujT9YlKI1CZuCfTUAU21oFEDM3FIO5pY5X5elF2AF9DPznGwoyhAAU0qiL0wNsP079MqL9tey_Ka2U-rkgDNV_3OhF1fEpaVHAZ7dvIlHsrxygPX6Q6EDhRvpe80q4Q5N2j7EDL8UBWkbz_annPPv_DuQawVhcrusQK8Cb2Tvjjx2S8GPblYqQEQ0wQNPWy0Zeg7pzbILDNmWfBulVGCZnMI4WXFuzcw2VVyjh0f1Wi2ARqaXzXcFjdYg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تکذیب خبر نادرست درباره حساب‌های مشتریان بانک صادرات ایران/ تمامی خدمات حضوری و غیرحضوری پایدار است
🔹
بانک صادرات ایران خبر نادرست منتشرشده در برخی رسانه‌ها درباره حساب‌های مشتریان را تکذیب کرد و نسبت به تداوم خدمت‌رسانی در همه بسترهای حضوری و غیرحضوری اطمینان خاطر داد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/677775" target="_blank">📅 18:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46424e6872.mp4?token=P1chmJip9RovsV4dPkBY6G69N5EBPshHrXss9UjxFLG2AZ3Gwp3Dq6J_wskKskNsVr2-uR5f53v7ArQnluV04ZitKm9hC_i9jtzw1KZ5frVbB0wKLrFULHNgfI4bI2-Yre9L_efJ6Ts5KeZQf2lqU-d61qexJshPKa4R6riNWuf9yqAFe6Uk-7j_wcngI_72EPGfdbd--Ecy8Ie7aWPBKO5MF1leYxacYOad0lxmStZymnn5XwvBk6zHtyRw7K35XcWDd-UqVvSRluJpofA8PbOrwYq-RL9ym_Mm6I74XXGamoZWaCuuj3z7ozaBVyRBy-4tknuOen_3r8PxWcQrOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46424e6872.mp4?token=P1chmJip9RovsV4dPkBY6G69N5EBPshHrXss9UjxFLG2AZ3Gwp3Dq6J_wskKskNsVr2-uR5f53v7ArQnluV04ZitKm9hC_i9jtzw1KZ5frVbB0wKLrFULHNgfI4bI2-Yre9L_efJ6Ts5KeZQf2lqU-d61qexJshPKa4R6riNWuf9yqAFe6Uk-7j_wcngI_72EPGfdbd--Ecy8Ie7aWPBKO5MF1leYxacYOad0lxmStZymnn5XwvBk6zHtyRw7K35XcWDd-UqVvSRluJpofA8PbOrwYq-RL9ym_Mm6I74XXGamoZWaCuuj3z7ozaBVyRBy-4tknuOen_3r8PxWcQrOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسپانیا خواستار نشست فوری اتحادیه اروپا شد
🔹
پدرو سانچز پس از ورود ده‌ها هزار مهاجر از مراکش به منطقه خودمختار سئوتا، از برخی کشورهای عضو اتحادیه اروپا به دلیل درخواست برای تعلیق اسپانیا از حوزه شنگن به‌شدت انتقاد کرد و خواستار برگزاری فوری نشست وزیران کشور…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/677774" target="_blank">📅 18:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677773">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a90068b7.mp4?token=VN1PJHMnBi_ArGzdnxofgK3o_Y6m32MROw9zyyO5hbM4adgxCX0BwJjdX86ZHPD-Vk4eeDf77xprZjxx98OX9z6xlwYEp-w0eIp7AOL-TUMfMeb_Ywg2LBDZIeo0qkbydU9rDyRDLaElTJ0y-2_IE8oy2KMCNiClE-JSKPhusrkD7gZBW7PoNaGTBs9peV1LvNyX9JXUk-YCEX_jIS7sSmdaFowB6SpjIO9x3iSE9QvMgVu2rlqMWntSeX62pprXClGGqUw6FrM0611wuKhug7d-M9TWCZsVcaZjtGQvV6Q2hkm1fWzkBj3wbDO_p9Fo2BxnoE-bMwMDAsvB0wBQfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a90068b7.mp4?token=VN1PJHMnBi_ArGzdnxofgK3o_Y6m32MROw9zyyO5hbM4adgxCX0BwJjdX86ZHPD-Vk4eeDf77xprZjxx98OX9z6xlwYEp-w0eIp7AOL-TUMfMeb_Ywg2LBDZIeo0qkbydU9rDyRDLaElTJ0y-2_IE8oy2KMCNiClE-JSKPhusrkD7gZBW7PoNaGTBs9peV1LvNyX9JXUk-YCEX_jIS7sSmdaFowB6SpjIO9x3iSE9QvMgVu2rlqMWntSeX62pprXClGGqUw6FrM0611wuKhug7d-M9TWCZsVcaZjtGQvV6Q2hkm1fWzkBj3wbDO_p9Fo2BxnoE-bMwMDAsvB0wBQfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هولناک از پاکستان
🔹
حمله انتحاری در شمال این کشور دست‌کم ۷ کشته برجا گذاشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/677773" target="_blank">📅 18:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677772">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
پاکستان به ائتلاف دریایی عربستان پیوست
🔹
پاکستان به همراه ۱۳ کشور دیگر به ائتلاف دفاع دریایی به رهبری عربستان پیوست؛ ائتلافی با هدف تأمین امنیت دریای سرخ، باب‌المندب، خلیج عدن و حفاظت از کشتیرانی و زنجیره انرژی جهانی.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/677772" target="_blank">📅 18:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677771">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_YipcA89-9ZCFlVn2JfdxL2RbJH-p5tpsgGggYu4kHEUk0l7pXRCYCMbZaIwHRxtE0PjCLTCbacrjMMOxPar-7TrO4EbAcqjBMKhzLpiStoKnDSoqj98RuHkRMQKQURSby5sycMYcIPJNeeB25Ua_KfLxWT2Lcot5j7gYsU_JMOs5GJVWaSkVPDieWEs2pzS7Y6Wv0bS4OO45MMQ1z80MM2D126hfuu-V_9jxWWXAd4A7XseQCPwQUhlHWVdeNVXzgQ0y5AtGAyijZdSF_qm4eUsk4NLar04myqws0S2qAEUaQIDM2-FJrBvM03aLPmvy5D0Ne_9Fxl8dmfyvMjqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مناسب ترین نوشیدنی برای لاغری کدوم نوشیدنیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/677771" target="_blank">📅 18:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677770">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gijEyoFLDGHeX-_u6lyliNK0KxtKOL9ktbGuF9_vQCyzj6HogD38GyvmcRdRA2lZGzFVfxgS7JenMI_OXnsaxm3p6rMDVENdKttO5WSR93gBJZcxfgCo0hYGp1DlsZlFA2JXv-gh5g2yYLtiahUdjeFeL5I3PYqYA3oMUWCvuH1n8Rz3Qyc5HTgWV4vQlG0w_q1ueDZx67yjk8QHJbdCIClJeU3HL_1AtySAC51iOFO9T1hOzeOxn0l4huGzMReRYQeqUJtDKxYw8OS3C62fx3ANoXR3ZKoNQ0QHSGsPs_d-B4iFdtOmXB18Gejre7--nDn35YPnqylZkK1F8neDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚪
🦟
پرده توری آهن‌ربایی با قیمت اقتصادی
❗️
پرداخت درب منزل
❗️
✅
جلوگیری از ورود حشرات مزاحم
✅
عبور جریان هوا و خنک‌تر شدن منزل
✅
نصب آسان، بدون نیاز به جدا کردن در
✅
مناسب درب منزل، باغ، تالار و…
🔄
گارانتی تعویض و برگشت
🚀
عجله کن! لینک خرید اینجاست
👇
http://khabarfouritel.affdn.com/lead/45272
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
http://khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/677770" target="_blank">📅 18:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677769">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتایج قرعه‌کشی ایران‌خودرو اعلام شد؛ شانس برنده‌شدن در طرح عادی، یک نفر از هر ۴۵ متقاضی بود.
🔹
نخست‌وزیر مصر: جنگ علیه ایران، اقتصاد جهانی را تحت فشار قرار داده است.
🔹
امریکن ایرلاینز پروازهای خود به فلسطین اشغالی را لغو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/677769" target="_blank">📅 18:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677768">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amg-1Arr6RxvM-a6OAFwqho1CcA235JXvxK_8v7MVDTvlJHKkIlOXpW1MDCz9gasXP9nleWaZL1h99d7XV-nPNb_EJB2Hzky9Onl4hmI_md65NtwpSbj1b9LHjO63ptfJLVdhdvYaRWIpxszxgF6OkSiq8pZqTCWXsPT9R1wDOD02k1z7ojvQLCUaHGe2henaLB2rA40fOYJ9-HjnGfErMJ4qSSgVe148BxLo_qe1_7dO8Wf7FnSosueVhHJ8lNV0TJzMDtA9keUpjFRH7xYrJGd_ZB7D-EoI3qagUsAAHOiu6iZvReSBaXE76Kw4clI7OPFoD5pTGnzmEKkJxODpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
موکب داران با دل خدمت میکنند. احترام به آنان احترام به راه امام حسین (ع) است.
#میزبان_باشیم
@Heyate_ghararr</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/677768" target="_blank">📅 18:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677767">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvtfB-tLbYdisusOGAV-eZGallVov507c7R8RaMuQXk3Tl6lvqSq34MwLhjOmb5d5_oaL8o_5bgyUi2sEImmniGnE4mlKDFiHVH3d-WyIe7XdHRJo-ZsPnifNA1oLgTMkxIzvol4-m8Vtq5uJEhBHqIn95YUEUFAhHIS7InMcxS2VdhQn4Xehe6K4xzOicJnJd91WOxOCu1azhUpyzYMQhY2DkFDSc4Cb6HSxZGBf-pm_dGG5ODQy-Nhu7w13XSil8V11wJ3BYPTYjJjOqou7Rw7Ij12OG4JROaR_nu7_oD-RCkHC560RGBnBwGw-UyyUOnAhwYrPzndux1SNGjBuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردی که قرن‌ها جلوتر از زمان خودش فکر می‌کرد؛ ابوریحان بیرونی
🔹
ابوریحان بیرونی فقط یک دانشمند نبود؛ او کاوشگری بود که با مشاهده، اندازه‌گیری و استدلال، مرزهای علم را جابه‌جا کرد. از نجوم و ریاضیات تا جغرافیا، تاریخ و داروشناسی، ردپای اندیشه‌اش هنوز در دنیای…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/677767" target="_blank">📅 18:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677766">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a2f85ffab.mp4?token=Ks-iTw1dfuhTyIXmTUgUdx4POsSCzXDFNwyuDPXmKrSHfGS8x73BAYH21-Rfg-rcr43d4qLPANuU04CvMOVScfFsvodezcpHifFJSWaFqobj9YtuWt1Ng3-SSyMV5ZierwYBRohTJ7_-JAg0CnroSVf11t3rj5Plf6OZ3GkyknycBw-czo4eOv5UYEcU6sg-K_uQ4QMtg9XLVI_gETilC0XUA_1RBS1khlnrmtYmGNVuGU1yRNrAeypvywkXYdATiy1gz7BcA2NRJ9G9IAqMa72iU3xmY5SRd6roSCbdtrazJUR5CfMrz7QttK_CHnQExSLgr9GcgSv_iPLlZLI1M0hnGEXT6WRT5edyW2Y2XC9UdI8rVB55IHVy3ATXl_2AYk9nMMElofd66Pfmrz_E24DRtG6HZe8JtzpUSno5thU00nFjFF4prKzgjsIUaWMaAdfUEwkoPsI6NiEhQvdixnTxBHLYMN_GhmEJwBjT3HAGpIX3kMdiUg-aRzl-_mRchqTNaxKvRiPiVQuE9ERirksXMe6T4JuucjlnrBw7HtexSe-L0_X3WqtyyrEqm23GqtEbraBpax3mmoNcC_TfTmkFaAH_m4vtFr0EL_SEZmgqxMVc19y6eEQmIfDgqoRXT5Dsoj0V1UpSgI0ox6yJURaXpHx13855t7I-_pL5TH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a2f85ffab.mp4?token=Ks-iTw1dfuhTyIXmTUgUdx4POsSCzXDFNwyuDPXmKrSHfGS8x73BAYH21-Rfg-rcr43d4qLPANuU04CvMOVScfFsvodezcpHifFJSWaFqobj9YtuWt1Ng3-SSyMV5ZierwYBRohTJ7_-JAg0CnroSVf11t3rj5Plf6OZ3GkyknycBw-czo4eOv5UYEcU6sg-K_uQ4QMtg9XLVI_gETilC0XUA_1RBS1khlnrmtYmGNVuGU1yRNrAeypvywkXYdATiy1gz7BcA2NRJ9G9IAqMa72iU3xmY5SRd6roSCbdtrazJUR5CfMrz7QttK_CHnQExSLgr9GcgSv_iPLlZLI1M0hnGEXT6WRT5edyW2Y2XC9UdI8rVB55IHVy3ATXl_2AYk9nMMElofd66Pfmrz_E24DRtG6HZe8JtzpUSno5thU00nFjFF4prKzgjsIUaWMaAdfUEwkoPsI6NiEhQvdixnTxBHLYMN_GhmEJwBjT3HAGpIX3kMdiUg-aRzl-_mRchqTNaxKvRiPiVQuE9ERirksXMe6T4JuucjlnrBw7HtexSe-L0_X3WqtyyrEqm23GqtEbraBpax3mmoNcC_TfTmkFaAH_m4vtFr0EL_SEZmgqxMVc19y6eEQmIfDgqoRXT5Dsoj0V1UpSgI0ox6yJURaXpHx13855t7I-_pL5TH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باهنر: رأی دوره دوم انتخابات ریاست جمهوری به آقای پزشکیان و جلیلی رأی خالص خودشان نبود/ روند حضور مردم در انتخابات کاهشی است و مردم از ترس یک نامزد به دیگری رای می‌دهند
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
متوسط حضور مردم در انتخابات مجلس ۴۰ تا ۵۰ درصد است، اما در انتخابات اخیر پایین‌تر آمده است. افت حضور مردم در انتخابات قطعا به معنای کاهش سرمایه اجتماعی نیست.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/677766" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677765">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e195c9c66e.mp4?token=kve-9Gio1tcopr9KvgMKmxnRD72ZcOCm9kZCKbR8Nzp4HTGGqdBjpPSbNCwl6lLX-cbZEU5iXherSheCZ3W3eYjNKpbfXynNUiMDP57lVhfcYJjopdMZY9K_sVvgDoEzYjzrHVX6W-z0EWz8jN7gs0YmTq82GOODuyvvzVI74j3yH1kFPrwB_YWViK0NH_u8eM84QlslHc9NwAeYrD_LQEd53WuP-bRqMgPE1y2tzzvC830amRBIKdJIl_O7XqVTt_uyY2piqL8WV8A_KvPg3AaHoK93ah_mMdIBEGVScvHTWzEpE37TIZpr7-URImQAgqUCcfzAphwmoZTYBfRmxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e195c9c66e.mp4?token=kve-9Gio1tcopr9KvgMKmxnRD72ZcOCm9kZCKbR8Nzp4HTGGqdBjpPSbNCwl6lLX-cbZEU5iXherSheCZ3W3eYjNKpbfXynNUiMDP57lVhfcYJjopdMZY9K_sVvgDoEzYjzrHVX6W-z0EWz8jN7gs0YmTq82GOODuyvvzVI74j3yH1kFPrwB_YWViK0NH_u8eM84QlslHc9NwAeYrD_LQEd53WuP-bRqMgPE1y2tzzvC830amRBIKdJIl_O7XqVTt_uyY2piqL8WV8A_KvPg3AaHoK93ah_mMdIBEGVScvHTWzEpE37TIZpr7-URImQAgqUCcfzAphwmoZTYBfRmxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در پایگاه نظامی «التاجی» در عراق
🔹
منابع خبری از وقوع انفجار در انبار مهمات پایگاه نظامی «التاجی» واقع در شمال بغداد خبردادند؛ مرکز رسانه‌ای امنیتی عراق دلیل این انفجار را دمای بالا داخل اردوگاه تاجی اعلام کرد.
🔹
این پایگاه مربوط به تیپ ۳۵ زرهی عراق است و برخلاف گفته‌های بعضی از رسانه‌های فارسی زبان ربطی به ائتلاف آمریکایی ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/677765" target="_blank">📅 17:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677764">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2164949e3e.mp4?token=QclkYO-uhJNvLyFnlQO3WhZiRe3HQD8rLNol37ZYaNCwchkq3WHO6Bf_pYcW7XOvmvKb9HGR8U2rASR-mq5UsxObz7XkN9vjrYwdBnZSHHmVd6Yj2zNgvR_T98AP2w_gs0jr-gCIs7r45Bw_r61iW0zdaCue7HU--RSo9S53TJbmr-wyZR6MMc94S43KiFuMHsyY2L64tokinWOkJ3uyOez-yiPH7GJ3DZf97thiehsEY2QOi-LI74V39RCDViKI7whXY4nUN4rMCTu2_EAWjQ_PsgrgIHP0xGpJZncEk8YdyT8XvjaR9V-KClT2GtouBdV6k2VD0M4G-bl8bE_F_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2164949e3e.mp4?token=QclkYO-uhJNvLyFnlQO3WhZiRe3HQD8rLNol37ZYaNCwchkq3WHO6Bf_pYcW7XOvmvKb9HGR8U2rASR-mq5UsxObz7XkN9vjrYwdBnZSHHmVd6Yj2zNgvR_T98AP2w_gs0jr-gCIs7r45Bw_r61iW0zdaCue7HU--RSo9S53TJbmr-wyZR6MMc94S43KiFuMHsyY2L64tokinWOkJ3uyOez-yiPH7GJ3DZf97thiehsEY2QOi-LI74V39RCDViKI7whXY4nUN4rMCTu2_EAWjQ_PsgrgIHP0xGpJZncEk8YdyT8XvjaR9V-KClT2GtouBdV6k2VD0M4G-bl8bE_F_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنج قهرمان گمنام خرمشهر؛ رفتند تا ایران بماند
🇮🇷
🔹
اینجا خرمشهر است و این ۵ نفر آخرین کسانی هستند که در حال عبور از پل هستند تا مقداری بیشتر تانکهای رژیم بعثی عراق را معطل کنند تا مردم فرصت بیشتری برای دور شدن از دشمن داشته باشند.
🔹
نه پلاک و نشان داشتند…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/677764" target="_blank">📅 17:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677763">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d706f40be0.mp4?token=vSboW5qbQp20U6IpjekFCbE9k5HhSDCbrqhLgUNCXB2HiPB3UMtZwMlPK4Mq9i-ECl4fIAtSOgXciqiQKhKV6P3a5BDwzDn9NtQ-gq2VQDZlRtnXoRHs35bhBTaeJ7HhRfdsV96OiILsLcPgwiiaLAlz3RtOBFFc5B8nhkWaCoZpZ5NJjGOiPuZjRigoxzeJchV8UEh8EDXrBPSnhnFIUIprmgUMMnX8Ftv9i9hdb8e8RNJcTCrBskYzfoS5pVn9-aHkKVO50yUwW5Pmvy5ot2ld4H9Jl2h3qyyQZ1rLYCCAhsb9ihSxm7JD8KWVQP1Z4jOUPP1hCnHUC0pdU-CbBlvWeNr3x2zStUX20E6PYUnX8PwRy8IomuDVXmg-URpTLlBGUUm58VcYWPsptA6KMGIKH_hTmHtAGHb8Tic4C48gwu7lAzks4REUWhmlHQH9MQRgC-Hjn6RkboD-tHDGLfdBqOiqjIFKP6KHew2N3kZ4J6glxoXJfh7lX8drzzqTntdPQMWQUvopdy-es8YE8nMi-OKVZMVIM5yBgyL17HOmF0QTWHJQtlctXqW4LJQI0aw4cXJSQh_1Yh-DPMndBiA-yI7xy-WFDaF4ECNPCPHmbH-qWDJFDQkaxY7tym4YeT6JoKZL3G9SljgBmnNYcnaekVA-INZK6nsJIinRHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d706f40be0.mp4?token=vSboW5qbQp20U6IpjekFCbE9k5HhSDCbrqhLgUNCXB2HiPB3UMtZwMlPK4Mq9i-ECl4fIAtSOgXciqiQKhKV6P3a5BDwzDn9NtQ-gq2VQDZlRtnXoRHs35bhBTaeJ7HhRfdsV96OiILsLcPgwiiaLAlz3RtOBFFc5B8nhkWaCoZpZ5NJjGOiPuZjRigoxzeJchV8UEh8EDXrBPSnhnFIUIprmgUMMnX8Ftv9i9hdb8e8RNJcTCrBskYzfoS5pVn9-aHkKVO50yUwW5Pmvy5ot2ld4H9Jl2h3qyyQZ1rLYCCAhsb9ihSxm7JD8KWVQP1Z4jOUPP1hCnHUC0pdU-CbBlvWeNr3x2zStUX20E6PYUnX8PwRy8IomuDVXmg-URpTLlBGUUm58VcYWPsptA6KMGIKH_hTmHtAGHb8Tic4C48gwu7lAzks4REUWhmlHQH9MQRgC-Hjn6RkboD-tHDGLfdBqOiqjIFKP6KHew2N3kZ4J6glxoXJfh7lX8drzzqTntdPQMWQUvopdy-es8YE8nMi-OKVZMVIM5yBgyL17HOmF0QTWHJQtlctXqW4LJQI0aw4cXJSQh_1Yh-DPMndBiA-yI7xy-WFDaF4ECNPCPHmbH-qWDJFDQkaxY7tym4YeT6JoKZL3G9SljgBmnNYcnaekVA-INZK6nsJIinRHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خواص آب پیاز و بقیه مواد مقوی رو از زبان خودشون بشنوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/677763" target="_blank">📅 17:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677762">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
مهران رجبی: از اکبر عبدی بجز خنده آدم چیزی یادش نمیاد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/677762" target="_blank">📅 17:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677761">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a13c543b1.mp4?token=u1MYKRG7JREcPMcOfyxObUj_7N16TQQF7m0JUmHaDclnH0V9IKN-UgvQ-zW63rVh7WWYXkSkLB0D16yF3u31TyUDMqg0lByRskYC3A9xTqEXpY7SoKzXR17jOmKHnGpgllyZTUv5z1Ynh1QfJBo2A5i0bRXgWbQJ1gSF6SyBdBNQfvYhzLregpqZImxuH_4mrNCzejJeJ9rVX1SXR9-qEbvvOCVFAFA5O0mMq0XUrNrpFn5vnEpXI19exO38vscM9JSTyHdwhDhH44UY2Le9GcAgV6FjxqeV1OvOd97XfSE5Nq40rt8U4kCdwZQ9BU_1Brm8d5STR11en5tSxbAL-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a13c543b1.mp4?token=u1MYKRG7JREcPMcOfyxObUj_7N16TQQF7m0JUmHaDclnH0V9IKN-UgvQ-zW63rVh7WWYXkSkLB0D16yF3u31TyUDMqg0lByRskYC3A9xTqEXpY7SoKzXR17jOmKHnGpgllyZTUv5z1Ynh1QfJBo2A5i0bRXgWbQJ1gSF6SyBdBNQfvYhzLregpqZImxuH_4mrNCzejJeJ9rVX1SXR9-qEbvvOCVFAFA5O0mMq0XUrNrpFn5vnEpXI19exO38vscM9JSTyHdwhDhH44UY2Le9GcAgV6FjxqeV1OvOd97XfSE5Nq40rt8U4kCdwZQ9BU_1Brm8d5STR11en5tSxbAL-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لو رفتن نام شرکت چینی در مراسم افتتاح بندر آمریکا
🔹
مسئولان لوگوی شرکت چینی سازنده جرثقیل‌ها را با پرچم آمریکا پوشانده بودند، اما وزش باد نام شرکت را آشکار کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677761" target="_blank">📅 17:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677760">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما کدام الگوی مصرفی در ایران نیاز به اصلاح  و فرهنگ‌سازی دارد؟</h4>
<ul>
<li>✓ مصرف انرژی</li>
<li>✓ مواد غذایی و آب</li>
<li>✓ مد و کالاهای مصرفی</li>
<li>✓ رسانه و شبکه‌های اجتماعی</li>
<li>✓ دارو و خوددرمانی</li>
<li>✓ پلاستیک و ظروف یک‌بارمصرف</li>
<li>✓ سایر</li>
</ul>
</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677760" target="_blank">📅 17:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677759">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec84885762.mp4?token=VhCbzVESF87DLs0POOeamJ0dWq_y2P_tDZFOksBuxP82g5wTpvxHr4z5ObYJQbxQM5T111kZYX9TTWGqDYEHUBpKjKL8xk4WWBSPK6o4Bvfm217u374zCTqKiX4kp3m2f88N9aTU-27n848kRlLrTmtEcJLDRzmV5-RlVdvJWheO2rRFuSxtldYNhZsUgbEaP5nnMsImd_IgiceRRkmGtfu-iGlZMD1fhaYmBvILy4JBPRA2_BfZ2yf1wh6lkeOkBn7u2NlLPD_rXYxbdifgZMQlmK6AA-81sJUbaiQ5-C81zwTl3BG6WGGPBdLkicE8lWJhHwFJVd7aVGD6qk_NBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec84885762.mp4?token=VhCbzVESF87DLs0POOeamJ0dWq_y2P_tDZFOksBuxP82g5wTpvxHr4z5ObYJQbxQM5T111kZYX9TTWGqDYEHUBpKjKL8xk4WWBSPK6o4Bvfm217u374zCTqKiX4kp3m2f88N9aTU-27n848kRlLrTmtEcJLDRzmV5-RlVdvJWheO2rRFuSxtldYNhZsUgbEaP5nnMsImd_IgiceRRkmGtfu-iGlZMD1fhaYmBvILy4JBPRA2_BfZ2yf1wh6lkeOkBn7u2NlLPD_rXYxbdifgZMQlmK6AA-81sJUbaiQ5-C81zwTl3BG6WGGPBdLkicE8lWJhHwFJVd7aVGD6qk_NBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دو بالگرد اطفای حریق در غرب آتن
🔹
رسانه‌های یونانی اعلام کردند دو بالگرد اطفای حریق در منطقه‌ای در غرب آتن با یکدیگر برخورد کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677759" target="_blank">📅 17:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677758">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
خسروپناه: اکبر عبدی دنیا را شاد می‌دید؛ او سعی می‌کرد گره‌ کار مردم را باز کند، هنرمندان کار مشکلی داشتند او سعی می‌کرد به آنها کمک کند
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677758" target="_blank">📅 17:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677757">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ستاد اربعین: ۳.۲ میلیون زائر از مرزهای کشور خارج شدند.
🔹
ادارات استان بوشهر چهارشنبه تعطیل شد.
🔹
سفارت ایران: روابط تهران و اسلام‌آباد در اوج است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677757" target="_blank">📅 17:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677754">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGWZIg4y3EFIp6t-31T6Sqq2ZjCleB8op4NsaXCp57gosWenmdN2YGaLPm-pd1T0ZqvaeAiYAvD1K7yASyoaRyx43QYzN-TTM1OXjSSzk1J1FgLfgUPH4f84RZ5rmtqJiuVxXd1UCrWjs626MZnepvedAwrRxzdkybXHLlYMNdaGWLyk2dNhRtIKbreLMhSk8_br6HEEtsAu5NnHIO0B99IGcF4rp9ZnDJsshmVjZQy2tDgvTO25-jRngVYfmG1jbzR0ZFIkfEQxwIn2tgwxNcaSW7aEKIBNCuVy-3V32Pj6bdWHaKvXLZc1IDYFjzJSi66xE4JULp1wpCyVIkMnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ce6GgCd_OiC5u0z5NpYfXMWxM9bZmmz6P9JiHrn9aDn09SaF4Uj7rKr2_yUgBJ7IOTrUJXnGP-msAOr3bYZ-yqwKb58jANYt5rce4vTbprlNvhrznJy_MYlB7iBrbBp8JVuL9DUJ8Hj16TtCFN4VrPIR_BL3v1rc-n1ed02zfqZdYDPr169bRLsUkxGbMQ0xacjGpAcp91IaTRqmSSoVNH3cMdlHMPz2AId1xDSvlP-XJeKSkJD5CutXdUQDYVGSvChVTV9znIUWH_nM-5yJbchcmWQWKynz8DFeRCcBDxnpsZye7Vzdfzq4mLNjtFqdQ99qVfHX31hSnOjcfDIo5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پستچی خوش‌شانس، بسته کوکوریا را تحویل داد و در عوض هم با خودِ او و هم با مدال قهرمانی‌اش عکس یادگاری گرفت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/677754" target="_blank">📅 17:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677752">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WeeO-Huz2Ks2AsY5z2zvz1IVcrZ8d79qADidlzYYA4BD2VspGI0t1V_qMJv7SPckYDC7pfzdKsZwyOaBIANHHfqn71ncMtKKX3lMtZmGqxdZD7XAAKaBdJAsBJFJ0yvrA6amgMDl-m8tECCnqFmWkLaZxmBRTbSWOd83t3wexMUh5_txKyy6OUH0Xg4VAWfS_r0zIJr5FAHC2UOPc7Phmgpk_6tdw0kNTRp_9ji_GNR45T0sDPjnLhUpwaa2BexG2to7E30po6aG8r3pGN0znlY6MgtfRGbKgpZbpDuWkLiw24zKA_MIgLF2fgHSlx4S9iIywR1YRSBZspcQiW7aXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSS0CfjeB9wN24lI3gwbQqWEIwYlcIl0uBziM4sNDSG2RQwf1FqiV-Lzri1aHPuNPmcQtADh9TMpnIfrtxecCCBZuL_OC2L2IiewPXrD0vrcJkKKRbVxbo0LKBd1OlxxkjEDeLSb9XKLz2JkWhyCiMGDyWwwPm5TLl78yViFleiEI3iF7rBmxcN7Ux5_X0X8GKHzQjOB7UH3q0tM9LihCfCL_6mYzMaHp3awb-RUa4XyB35uaIVHpyI-Ak3aUnm0wWpnkbfXyaOmFXzh9dTsQ1fz_7q7y0UwZS7xX4CTykyOL5hE46uYLXUf9jLhLseaj1f21WZNMgAdZM5OVbInxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازگشت هواپیمای سوخت‌رسان آسیب‌دیده آمریکا
کان نیوز:
🔹
یک فروند هواپیمای سوخت‌رسان KC-135 ارتش آمریکا که در حین عملیات بر فراز عراق دچار سانحه شده و بخشی از دم آن آسیب دیده بود، پس از ۴ ماه و نیم توقف در فرودگاه بن‌گوریون، به آمریکا بازگشت.
🔹
این هواپیما پیش‌تر به‌صورت اضطراری در فرودگاه مذکور فرود آمده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/677752" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677751">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea621d41b4.mp4?token=vO7rtTbcvc4KTT9uEpnXDtDfZRL1cAqbPPJVwvuTdBCND6vy3yDZnenEeexdXhdO0CwClIrZamQzlwq6g_iIfaane9k3fwZDLlLGZrEXphrOzXtEu5NGCcXDj7uHmsue2JxTJwvpD2aBqg4oYzSwmamLsqWhj0nycPFqNO1YuWYk8GVBi-zNocYYkrwIm5VJORTteNkjfGOJYRPNbLn6sEZO9TM4AzQMzBoabmR7DMoSePXsngkKvy7o-Sw4wW__woe7armUqGQcw5evHcojAPrw1ZFHUHDg--v8W364qt6Q3wtU4T9ZaDzm7OjyHeU6hXnuuUf92r8IKEtYqtWHv0HZqwj6rRG8TlMhdNZNrEP-mwgglk1hieF-U2Gp-3Dw0VBsqYXa9pWHQM-q7UZPEGilVXWPww_4RMj_ldHgMT0qhew00EVLeelzqWUvLuQc6Vpanx-XqQT3cm6158NlqyQxGKhs5Cv_SfpxeOJsZHaghe9A4xZdonVxypJJAlEevrf98F6q_0McCVKssGWUPy0RwRAINmmtCR-iqYWGIvbRsZofxxUt8Dw78cFL341vaL3Wd7QM--qci_YugzdUkwZAvfUrX3rVWqSmZgsizP4RXXDd1flbuh6MgRbr_6yvlmpJWduWsTYP6d3yP8fUHO1FveL_XQI8h6R0-m-znqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea621d41b4.mp4?token=vO7rtTbcvc4KTT9uEpnXDtDfZRL1cAqbPPJVwvuTdBCND6vy3yDZnenEeexdXhdO0CwClIrZamQzlwq6g_iIfaane9k3fwZDLlLGZrEXphrOzXtEu5NGCcXDj7uHmsue2JxTJwvpD2aBqg4oYzSwmamLsqWhj0nycPFqNO1YuWYk8GVBi-zNocYYkrwIm5VJORTteNkjfGOJYRPNbLn6sEZO9TM4AzQMzBoabmR7DMoSePXsngkKvy7o-Sw4wW__woe7armUqGQcw5evHcojAPrw1ZFHUHDg--v8W364qt6Q3wtU4T9ZaDzm7OjyHeU6hXnuuUf92r8IKEtYqtWHv0HZqwj6rRG8TlMhdNZNrEP-mwgglk1hieF-U2Gp-3Dw0VBsqYXa9pWHQM-q7UZPEGilVXWPww_4RMj_ldHgMT0qhew00EVLeelzqWUvLuQc6Vpanx-XqQT3cm6158NlqyQxGKhs5Cv_SfpxeOJsZHaghe9A4xZdonVxypJJAlEevrf98F6q_0McCVKssGWUPy0RwRAINmmtCR-iqYWGIvbRsZofxxUt8Dw78cFL341vaL3Wd7QM--qci_YugzdUkwZAvfUrX3rVWqSmZgsizP4RXXDd1flbuh6MgRbr_6yvlmpJWduWsTYP6d3yP8fUHO1FveL_XQI8h6R0-m-znqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس صداوسیما: آقای عبدی در نقش‌ها زندگی می‌کرد و نقش بازی نمیکرد؛ او با مردم زندگی می‌کرد و به همین دلیل محبوب مردم بود/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/677751" target="_blank">📅 16:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677750">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjONT8z716gQqRTMTWU7HfHsa5gIuXCGcU95-XpTR6mLSDCinNtnEeyHXsQCM-NS_EzGEuARZQHstGjxhrfOvcBKAuoTRWlDTsy2_dSXwg3cBBDUJMt9ojP3Jc5xE1opBFm6iOisax1xn0HmdfeqMe-KCIXYR1__x_FvnZ6qoGhlS2zUQl8EF6zJP1xrZNOSaVvxteIdJS1zxuHLfCN3nXpA1Yu4exiGtX7c6np5AhL82hoMkD6j2modWXO5Q52y-kkHwo6kez-s0yzE_qKQHtJZJyEU9PwHcedKGSyMxY_rle8znjjg4mwTzUnO7m5jyKnH9vefS58rRNN28uugrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یزید؛ عموی جدید علی کریمی
🔹
علی کریمی این‌بار در پستی از «یزید» به‌عنوان عموی خود یاد کرد؛ اقدامی که با واکنش رسانه‌ها روبه‌رو شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/677750" target="_blank">📅 16:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677749">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
گزارش تایمز درباره منافع مالی رئیس فیفا از طرح فروش حقوق تجاری جام جهانی
🔹
بر اساس گزارش نشریه «تایمز»، جیانی اینفانتینو در صورت اجرای طرح فروش حقوق تجاری جام جهانی به شرکتی مرتبط با برادر داماد ترامپ، سالانه بیش از ۳۰ میلیون یورو حقوق و پاداش دریافت می‌کرد؛ طرحی که با مخالفت یوفا، AFC و کونکاکاف روبه‌رو شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/677749" target="_blank">📅 16:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677748">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
حماس: فقط سلاح‌های سنگین را تحویل می‌دهیم؛ آن هم با این شروط
🔹
حماس اعلام کرد با مرحله دوم چارچوب آتش‌بس موافق است، اما تأکید کرد تحویل سلاح‌های سنگین تنها در صورت خروج کامل اسرائیل از غزه، تشکیل کشور مستقل فلسطین، بازسازی غزه و پایان تجاوزها انجام خواهد…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/677748" target="_blank">📅 16:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
گاردین: جنگ آمریکا علیه ایران از کنترل خارج شده است
🔹
درگیری‌ها به چند کشور منطقه گسترش یافته و با تهدید امنیت انرژی، خطر رکود جهانی را افزایش داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/677747" target="_blank">📅 16:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677743">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2KirR8g9MHP8WRwxckDq786LiBBLAu6HfMS7g7Qjl_ZeVeeojWf1pjNq1MuHyIYUiSiu3tQF-EQwVJmeEgL_9-5cMbyzf2pAK528S-zgFh6Zl28EC2WlzfBTSbiRPJbMaCxoZ9YfLSggqJfnO7ihgcNTqtmyFUxYEuuHPm3JaaL5_MWEWVz3OHvCNjYO0Os21x2tZTW9iM4hszfLLLKSFLIZwXtOR3Bd6uhAJyXX_uUFtGxWpN6OJXkNAKBArSVMn-M0r1fP-g45RWCLiHs6DHm97vPMT6GY3thsw-yVzTSsrvwvo3fbUZ-a-ObJWj0h-GvMeEMbRrNj5r-E-khhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEvO0KVkVcZIKHOz_CV45yt6GJJPZ2uLg1Ao-RNbH8XFFmRCQ44oWEHFCrNG79JpMTUJ66A9mv2q3RxIMQLNEtPXGomFh794YTcfdcr_C4Nl8XZlwBqBs60f91-5Wlf6M53B_tI8q0i5MeMFI3e1EsqxWGsYiEEKJ8-mlsoM7soScn5OsWiasbOziSyvU_4Y_Gk_E1IgivX3SuF81L-JffZBonYccaVrZDkaC5p95BlWcXB0nvViMUA7fO-AshXZnDO4_HT8x6Hy4xZJI8lFxT3vmJrSXOxAiXuAgEoR2HOrLYZRlM0xhhfu5WP_1EXq9NZZBhFXyoBQ0HJXEhun1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slzyVqO4YCOgN_lf6-y_2OP94iPc1E8U57BbHQRJxLZU-y70tWE4dn_Cr-x9CxeVbg2rXCufhP_ukCm3oPSEXzZj0OtFMJUmRHykRtetlNeY5b4BnDm-OT14ZemIoOOim-aF-ms3cfHC3iIr7FEXdI8Wyw5anoaY11ALSRVL3hZGj_VTi9UaUJ-7w43HTpOzEwv8VID0U2VloIWU3xXYv4x0kkAAm_-yzyEQWsWzhYN76IwtZ4KaUMKo4NmIg8PKxMWzj4HvLVxVw8vsEOnhzw8JqQi63JhyURsGW9z-UDNsCYTNmfH2x_YvVa1Y3V7q8iy0v0JBRPfxDnuCfyM-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sf1jyjt5ot4g6dzQp4rjIIGW5LArZ1OVD5x4uozLTZlbOWhvNBAmaGILBjuL-0YJALolUKSNPK0-Ry8CnLbLhm8Q2F77cusFtMfbitMtyNLWhDpFnohN4TKMTy5VdYF-LANxdo7X9xtvAHG1r1xtCiOkLNuJLSpADf47CH8uh9Gu1LGeJARJ8AxoteSMK-edyhY4AeM-tLbTCMBU1zGvWKCXjSpcw6PXmyZivjhpiWbVZC6WpRugeYABo9IKwhZeLOLuqVpRCK1PoOz7dYyYZjBimyV3l4YP7jHutZslauG3I_n0zYssgfUoh-dJc2rMsaXOcHpFZm4Q9ehDxPAtpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فوران تماشایی کوه اتنا؛ سیسیل، ایتالیا
🇮🇹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/677743" target="_blank">📅 16:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677742">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f9e79799.mp4?token=gtSxlacSWd874Yaa_jn1qYXMWqIsv4Me-2S0q0gYi_vgEzNxoaBzNW4niafwKV9MY78xLPMLawreFlzSkBasV6FOl18ga4YqvlI8DVCJEGGi8fJOeJA0jsG7_DqHT6LytTyhOrM0x6NbIlN0ncdAa3vO4yDKP6o3cGp87TW0oaeKVxUgg8HREXUaZYDj_QU8fGkGTxLdqAE05n5BDOTxQ2mZG3_-o8-YbW1L9BbHvbSXFH6vtfx7ua3LoYY-8siZjhaLEaJb86IxD1QafOO0N8w0tj7UnVzS4pt3CM14nj4-W9zGPt6KdRxr2utpzgvrDBYoWrVcPFHKBV04sd1Wqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f9e79799.mp4?token=gtSxlacSWd874Yaa_jn1qYXMWqIsv4Me-2S0q0gYi_vgEzNxoaBzNW4niafwKV9MY78xLPMLawreFlzSkBasV6FOl18ga4YqvlI8DVCJEGGi8fJOeJA0jsG7_DqHT6LytTyhOrM0x6NbIlN0ncdAa3vO4yDKP6o3cGp87TW0oaeKVxUgg8HREXUaZYDj_QU8fGkGTxLdqAE05n5BDOTxQ2mZG3_-o8-YbW1L9BbHvbSXFH6vtfx7ua3LoYY-8siZjhaLEaJb86IxD1QafOO0N8w0tj7UnVzS4pt3CM14nj4-W9zGPt6KdRxr2utpzgvrDBYoWrVcPFHKBV04sd1Wqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهران غفوریان: مثل برادر کوچیک اکبرآقا بودم و اینجور افراد تکرار نشدنی‌اند؛ امیدوارم من رو ببخشه که کمتر رفتم به دیدنش/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/677742" target="_blank">📅 16:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677741">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHxtvfhzajsgrO-eJH6tZJGJp1NMHq_iVZuHww4l7HCoipB63YaZU-txgQ8etHIM91eGQk_lVUUy60e25tgJVmlCXO7wMTbBqLrh_ct1UvmtnliaTEQHHFwKujzyi0FkJU-ildNHNHLh_ezHSx2-w4CggoxX3uxaCBL-wdDNFsl8T3TbcER2doz_c2FX_suAOxyUkxrwBdAdDbwqwxMA_aKkbJaJRHsDcx74eeaHP0BdPbg1FqHJD4mXrXCXxFGhcStJ82dSV6nzT763WjOv4jfFxkaZcLQBAZM6GD8YHUe3Afh7hKFX8xqSkfEbOB6pNIekFUIbdVYNjmx-zzk8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای جنجالی مایک آدامز درباره سرنگونی اف‑۳۵ آمریکا
مایک آدامز، نویسنده و فعال رسانه‌ای آمریکایی:
🔹
جنگنده F-۳۵ سقوط‌ کرده در کالیفرنیا در واقع توسط ایران سرنگون شده است.
🔹
او ادعا کرد پنتاگون برای پنهان‌کردن این موضوع، لاشه یک هواپیمای آسیب‌دیده را آتش زده و حادثه‌ای ساختگی ترتیب داده است؛  نمونه مشابهی پیش‌تر درباره بمب افکن b۲ رخ داده و ممکن است «سانحه‌های ساختگی» دیگری نیز برای مخفی‌کردن تلفات آمریکا در آسمان ایران و کویت اعلام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/677741" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677731">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKPRrbICgLXkiHKiaoqqE29sd0QiijTLenkEou0QvblGPVnTbDTPxB7XPtR_ZfCgC6cLhsflYUoY9IrOx0C0vgV-mPrqdZa8XlrgXOnyvKR7kgzvOQOZW8BuyhUFJhtZqUfFZhHPwZzXC_zMPWIelAbMX2gLXjMxv9M0WD56g7Tgof43V2AlJ0wDrLfRTC1lZqqrt4ycDqMoGJKddn8O5_JAg6pFij8sruguMTAve10IFq7CHAHzm7utvsk56AWKzbe-_UPAaUq1TdPiJ5nBwwVcFRB_Bja8--lsb4WmwYMWSSG0QabQNIBP31ayM6jtzAEkJEmHo4abyREaEjtM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPupgmM7uj7zDgyOMpcka_Alvts3Hk-yRG-BRpK-VN_1P7ooweK3PzKaR4xHJc1cPx95Wc47lOLRmpaa7kMGGM-uNLhYMlbWui1sarC-1jFJtZ2v1vlGGRRQO7QPTCYRI-1BkAzjjDsrLp2ZGkyAGDT6rZ5JR3L8lM2LbaE0gcys6nYdUsOx9_sDQUCIdopp3vZ4gmjKcfcqsjMWDg1Vvs3QXGI3FosHHTGp-sB55QpyGXmYwhNsZPIqyBvwmZDM9N4JBhG4QsJ2WNEw9WK3_CdmnrmofG3uK9XbqbOxurYWsgZeXG63uVPHUKfTGjeKD4Dza-6GDB19WLwBG21LWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJGc0gzP8Ns6XNY_jFmMtk_0pn2NHhyk2xFROIVjx6t_uxWI9jTbFmfdx92PdQ0dSaO4daoi09lB40VhWIr0LHNuge5Pzj3HNhLojocdiks9ze5oZutnRFhc6C3jUpQKbpiCuzCst3XcvpEmTPMHJOdg_Isw5h7BEzC4n9lf8k1PespgQE04R8ERy5Ms4VNg3GJhK1dtgVeQKpeJtyLyOoTn2yg_XWj-jerQGWCgd3fP96r45NKzdA-QF_ZnGrFwp-mo6YgAWipuXFTyAPt_ToshLHko1KrmIF9dLHkQqxFZTFXukOaK5CDpHsz-j170TgCoFlFv7vuIcnPnaEV2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q72aJ8hZy6LsZwuAcaFTNGPMfrZmetLpiLxdpxsfnHmLUCiQcPZu43wNzKAxxXXy3oCTCko17KA1iGEUIvr-6O1ZRpNyeqKY0xvIOli25aXpYSivJfGwt79X8j88VR1YoMq9VpbOiFEuJR6TkGox3WHInJ0nOqq7Q99UzEQ0SRO5k4QjBDDGupkiM02zlqPjExrNEbY6S6-5W3WWIqUAUgBP2O7VNARyJehKHnJhvA08lkkQ4OxP6eb6HYpzrwuqytgb3ygFPi00zjx9I22YPL5dL6FWQe1NzJJ6bxDcI03dzg6s08O9RdEkaCelHMlsRwcNv_q_wEU9VmH-Er4-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5l65uXuHYKfST6_3XChvvyTlkPrXF3dGOdpBFL3AS2sYLTbTXza4LrHtW4kEgbLi_jsM73MxoRfCWn86JAjOV3lJ5YJMDd2aq9KDHZxxAdhhud-7UAL09r2QlXPMFuhDpe3np7rExNr4tWuH-_Ga8GOtdqw9qdMv3SUtVf5XdgOPPWVEV57VIedecq2ZSaImOWiJ807-O0OCXHh9GbkiPOWQqgdFMMl9ISEsCkeJAjP6m4YiDFeAVHMVok99PoMNH0sx7ULjPUAe01_b0fU5xj9XKaKYSHiSBcmeh_43Hp91tF66p4NOqAy1mw_7hPziLGeF2Tek_pIFgP9Kew1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OfHyY1fmN5e5UdCwqaMexHCboOKkdm56rMe3ADvb2GGKxzwRuirsetBy8LNfo-w2rX1vTQdqDAqwCDoaNLBxwFz1YA3PZT9X1Qkpc3Gq9pEruAmB80ZXi37ZiX666srLxDgTZiwSiNrUdeGkkb33nFsfaaqR_vcxgvuEDEELrfmOF4NuMbfqBPk4TglQrMLUsTKTSWp8LiMjpx7zBwl9VkiPDcJS5zuSpIoSxm0v6nW2UtjDH8mkWNym4VLiGxq-0se1J0-bUVVXHZV3xb8YAetWAzoRsyfzRbhM-FZqXiAnDKwAU5LST4ByrwWuOfasl5BsRswKnWrNTYI3sNqGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eT7myo-kaAlgfrTJ5wVtdtmK6jJlgnSIS2a-rEDI_0sTbuvjvQj60xQCWe-qIl7sxsUNJ3TYbwQcb2ETDhxFLuQCqyWBYFx2pA_d4Me1BBg7iGVJWKw46G6SfNDyESiG5yKCkrDW_1fXzVBuYs8t0axk2O8Mc0zVz2DrG9fDGYR83axD0xO0H2b_P0YtxbMVjAbdKLXHqLk00rP4a8_Jc2aKlyjVKYK0Eg_mg_yjg0h11BCsm6f0Omz0MJ1XuZ5KO3LTTAujirvDvge4Rg4UxBjlmHaQect_Epm_FWt6apbSv5Ipl24dYcsw3a91P-5v8Rg8He-RGGMR5tSgd4A0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrZ7Qbl57R0V_CbqWLEX8arRJS1GiiftlYd8j1-JVeL1-0eTRitgF4fhSqWtXay95KcBe4nmkm-zI1FKmgVXV6yrROdUh105i-xbC_G4RNVqPDf7IdoqW-0R0_X0Rp0IsOvsfoz0E33ZoohprNH7wlruCHwpT6G4Iwm1FXl__P3OgQJSULryw2ILW_7ABr1-ruv8DD3aveBVMbHC-LZTbfT2N3_Tk2oEmXQUsT0VUUDABWlF1R83Yu4QnM0X_g0XgxwrQzHruMFV1iOEyU7tOLg3OO5nr1MnVojCaolKJSSg4fKqtHwz476rP6kddSvpSt5tPRPbkR8gnV_Gysxlxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjzULQ94YmkNNnOA5_eMJGe1jzfbefU6X3-nebA0gygRyEpH7AMwdCuQQ4Lj52nSt225Z3e_LgWAPlOkXU7nhpFYXlEvuYaKuBl-u00y0ZGGVrJbpIgNCYYmLOHnfsVShQPk4Ux8-69-SzAlJke4x15elqnJzRy8wO-TVEt5pHmdgnBkqyyJqhq3WCsG5gi7-gnhaxHJJ7TeHGEs0R-0xV_sRrLtKugRbYN-zlONzvFFNzwL8WVIkzJ6iJ7OZ7ZnOPmqeM7onyumVzorXQFGTh2L85Gpc-rbj2if3Wa5u7VUWT-CqBcnfwzwJNgNtCXWPDnEBW2vq01VmZgpHBzY2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨️
قبل از قدم گذاشتن در مسیر اربعین، خوب است چند نکته ساده را رعایت کنیم:
▫️
ما فقط زائر این مسیر نیستیم؛ در کنار برادران عراقی‌مان، بخشی از این میزبانی بزرگ هستیم.‌..
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/677731" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677730">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzSGnsFbPkLYfbA4Kv_JbRgVd-9UuFSsZKfakdEigiU1m24pcADsfc9qIFGBb5zcHtI5Y8uSUPchqtouIAgEDCPPSZQcg6lZMOszC1fMsg7ENR7AwNRkie9Vdt6u8B605saAyH9kdqZ2Wdo2POzYMeyDW8jhn60HOWScA2v0EA9VApQITu_D8g9Vmew-353loyWHXE--37dDKfTjnA3cU6Km44BaxuirP6iQ855V5bWAiE-wp9Py_pb6X8iRfN3LvcAOLP9HPN0QOI34DTM9yFdmd0iEBfYmetzz4wQU-p80KyTBORiDjwNiU_2S1TuO9PCTnlqfLMp5tTdXi_9zEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس جالبی از خیابان فردوسی تهران در اواخر دهه بیست
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/677730" target="_blank">📅 16:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677729">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
کشتی اسکورت‌شده آمریکا زمین‌گیر شد
🔹
منچ‌اوسینت، اکانت رهیابی‌های ماهواره‌ای، می‌گوید یک کشتی حامل گاز قطر در مسیر جنوبی تنگه هرمز لنگر انداخته و متوقف شده است.
🔹
بامداد روز گذشته؛ شنبه دو نفتکش در مسیر جنوبی تنگه هرمز در آب‌های عمان، یکی در ۱۱ مایلی دریایی شمال‌شرق لیما و دیگری در ۲۱ مایلی شمال‌شرق خساب هدف قرار گرفتند.
🔹
منچ‌اوسینت می‌گوید که این کشتی در جمعه شب ۳۱ جولای تحت اسکورت آمریکا بوده و هدف قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/677729" target="_blank">📅 16:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEfR3UWD1loyeqOqjVzJP3XlWKQwi_cApRBHqATW6focAJVGghWmkpUaw9sjWvjwV5JnSnOkbohp5YGedFO-ljS8G-MRuc3k1cC5C1aHRVBIwvsJWEEnntPtjxF2MHDZ0jLxdPsn0TIbfJe05-SztV8fqMZ51Bia7jTvjciNdCQah1xLQsfxRVSf1kx8leGF5aGe4z0ETcqXi9fTnDmNPz6wAaZD-l7v23CwiU4k3Ld7sBQrDgHVTQ4RSR2L45bTpQjh1AeqOTDSVQz5BOhnkTEa4V21AJOjSIl1vZ63zWALOqWBzAJKqtG-XDNHYjbRepQ6NykJckVwn1yH93IDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umTNt5XWz2iUTsaBq7JbtNFJPhQ1C-BRenp3PMcfcCC8IKXzTcC2yzghDyhAY_Uvhg1EyPvN_QI1bzDDQtzAIvyddLUjd_xErsJR87BzlCRJrJp4qKgMSEmU9fRpplRdF-AndERfaKDPs1NOcDIC9rgr2W7sQ1lEi9qppH_hQQqfgBwRveZ0K4uFOc5PC3Agh6Fa309uXPRO1fp7RnGWmN5CcUFyVkvjrU2wedY6IEpyzMXQKKVSQN7jcRFW8pk8iO7PHtjmNTp4qqxDO-YYPu___M4Q7JJzO-vk_wBluBkBBn8XvaserbGPc9N2SEwEn4c_xbbulACIAeFq85EX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6owtfn1Ppsv4jE5PObdfiFH2mcvCQq4CAbIPw_lk25cIYTs6lbn0wxqfQGFBnnBDsjiZUa3taXlLNUTQv8HJ1XQtQ3lv45Qo8-27Z1vkt0UT3RrpGjdQPkMsaddio-mbxya5UENKo5E-OYFjlSP86db8NtLhyQ5qynITkgNqFr5bFG1EC-Qslr-K3uo24gpBP1WrWjU0FuQRY0DiswrzKKk46u793Fuu1nqd9tR70JxXx7cAHZM7-nkpsamO2o9DC62xFMr6dyPBdgTlpAMfC_eA84OqJJdSSyU5veZi5BVuRTmPpdNp6BgquG3OgEGImDgO_fV5UkkMDBih6AZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWL110ri8O82yZfmIl7fwaJ_6GZUgbZJbMUB0dHL12krOqlWMK6iqxiyQBeDu6q_GwU9vdu5Tk_3ePblHgGO51zyx1Ym9do2_dXqc191ehpClloeoNsFPpG5DfywnSptAmuFIWHmOLzcQ8gqi5K1IZ1w_i3RcR2YHA28tRKz7hV1qqeExzIQvHNhUFX_lcK6Rw76sgMhFy-so6320lDeWWN-IFm1xfi5ELDHE1qd09mNyW23zQ8w1iKEBMnLc85t691boUzTiExMe05GFIYi_5poqUaT1Usgy5Z1zhgYPF_1xKGlOjvbw4u6S3poEXt2TRudM3FNsbIrOuk-N6D86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvY8KlnUlUtsdnGCIh1ZmUnURiN5kZg3vqgdNTZeKLXJ-wzn3yE2XYw5nCx0x_iO8RDJpvCewVesuGpFyNKWFckcIQEQLQDy5SKVZBogtddXxt8UMyuuoJQljawI9ejSMLwGqfBNjY-MB62ldWMuj2M_Xqxe2ZGfXBYaHOIGCpGa9CuHhrjFvegYQUogOK0FpVdAisyHligBUfRg_VKV2a9b8ukgx0CxNDLVOP0Q2DH-9EObs094BabAOiHIV_O_wLkOupa0XQVwgE-zlMVD9DULSyTIe7b1PQfM-QVDT3mH3lPYR7AaAbCJUr1kjAxNT0bViMKW35PNiL8w7K1-YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا باید ملک سرمایه‌گذاری کنیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/677724" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c4ba95b5.mp4?token=krs3rlfDKHBU8T1nG4B6PagROwFlA-sV-TNac12BGJd2SJGWigdzn3t1SxL0bnte402VTGCOp2QFaTPQDNIKqy5t5qWqEpNrwUwH4FMiD7IaAgUGWXvZBN79D6zKd3slbsjsNtiJelYY2BDwpmqDxGG1DI4Hd0ZKm91vyh4t_QUpu1ndzk1CfIVkuRn9BmjhkoGCd_qxtGS2so630-yKPHAfoEi0oK_1TRYGEw8SDeArZK35sm9F5XA1gAfFpF7bV7AD3qdKDkY44JaUblED1s1D_oEatiujezTfHobIKDgzYzp8srhfQfFX16dTpMZzzJToW64eB-M0ArEiVDUfPw5TrTuAlU22YxIm-PuUZ8_jDCCFhvuD1niGMmklLj7jO-LY9WELZVMZpC2_xPI1LGTAXTpID-h9-5TsV1vG-IJAbJj5U-a62jGvhTC0CvSe-SEzk2vv2B1A3gQncrpUyKXrzajE1oFtjrFm7CzzDqfJPbnR-DHxp_ZvkUs_C7Iq9hZD8o0DHoasiowtYpwS_MGLloR7XUkWZtUoRIJ_0p5HbDxKaB0t-NKtlsTGzbJpcAFoKtM_LBC0thz006rgdUZd_nUOyKr7AlXSp0ATlC0Klkq0HjiPN6JS5IFZvya0uuvOV1aWTEeyWf9KSQ4CcIzb-e4PaBSSHpGQ_PCYdnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c4ba95b5.mp4?token=krs3rlfDKHBU8T1nG4B6PagROwFlA-sV-TNac12BGJd2SJGWigdzn3t1SxL0bnte402VTGCOp2QFaTPQDNIKqy5t5qWqEpNrwUwH4FMiD7IaAgUGWXvZBN79D6zKd3slbsjsNtiJelYY2BDwpmqDxGG1DI4Hd0ZKm91vyh4t_QUpu1ndzk1CfIVkuRn9BmjhkoGCd_qxtGS2so630-yKPHAfoEi0oK_1TRYGEw8SDeArZK35sm9F5XA1gAfFpF7bV7AD3qdKDkY44JaUblED1s1D_oEatiujezTfHobIKDgzYzp8srhfQfFX16dTpMZzzJToW64eB-M0ArEiVDUfPw5TrTuAlU22YxIm-PuUZ8_jDCCFhvuD1niGMmklLj7jO-LY9WELZVMZpC2_xPI1LGTAXTpID-h9-5TsV1vG-IJAbJj5U-a62jGvhTC0CvSe-SEzk2vv2B1A3gQncrpUyKXrzajE1oFtjrFm7CzzDqfJPbnR-DHxp_ZvkUs_C7Iq9hZD8o0DHoasiowtYpwS_MGLloR7XUkWZtUoRIJ_0p5HbDxKaB0t-NKtlsTGzbJpcAFoKtM_LBC0thz006rgdUZd_nUOyKr7AlXSp0ATlC0Klkq0HjiPN6JS5IFZvya0uuvOV1aWTEeyWf9KSQ4CcIzb-e4PaBSSHpGQ_PCYdnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: نباید دور کشور سیم خاردار بکشیم و بگوییم در همه حوزه‌های اقتصادی می‌خواهیم مستقل شویم/ در بسیاری از حوزه‌های اقتصادی نباید خودکفا شد و باید تکلیف خود را روشن کنیم
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
بالغ بر ۹۰ درصد مردم بر روی تمامیت ارضی و استقلال سیاسی کشور تعصب دارند. دشمن‌ترین دشمنانمان هم ما را متهم نکرد که تحت تاثیر فلان حکومت خارجی است.
🔹
می‌خواهیم کشور نفتی باشیم یا خودروساز، فولادی و یا معدنی. اصلا نباید خودکفا شد؛ خودکفایی با خوداتکایی تفاوت دارد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/677721" target="_blank">📅 15:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677719">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/677719" target="_blank">📅 15:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677717">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqKYMJULmBwAAz1Za5G8HBQXrhjXWQHR7fy9JRMyNeTapc22yZ_est8pDK3_H4HZu1qRvrIAFuySjTpxJzKuEgr6TRT5dmwn0mUQju76z3UdIexWbWg6ZNNaZlQ7JWW2LqfrEvpzjbUzhlpw8DGRFefIS0XpvYIp7VGGAKkFLb5ESHG9FySWn2tjB1QrWU8zSApPl-qQUOextwrWUMIerSoS-aEMQ1iMoHVOPAYBL2jNTwynR8AXPU1mL-erfq7-mugQj62v3zOJFYJOphdcW2KM2njxQjf_O7efHKIgk9OE15lH8ZAUy8WlsUBOQcxIqt0--kxQFfclitzh-PTCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکرار ادعای جنجالی اسموتریچ درباره تحقق «اسرائیل بزرگ»
🔹
بزالل اسموتریچ، وزیر دارایی اسرائیل، با استناد به متون دینی ادعایی، بار دیگر آرزوی خود برای تشکیل قلمرو این رژیم از «نیل تا فرات» را علنی کرد و گفت امیدوار است این رؤیا روزی محقق شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/677717" target="_blank">📅 15:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677716">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
نماینده مجلس: ۲ تا ۳ هفته آینده قطعی‌های برق تمام می‌شود
سنگدوینی، عضو کمیسیون انرژی مجلس:
🔹
تاکنون ۵۸۰۰ مگاوات برق خورشیدی به شبکه اضافه شده و تا پایان سال این ظرفیت به ۱۲ هزار مگاوات خواهد رسید. قطعی برق شهرک‌های صنعتی به یک روز در هفته محدود شده و تغییر ساعت کاری ادارات نیز حدود ۲ هزار مگاوات صرفه‌جویی در مصرف برق ایجاد کرده است./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/677716" target="_blank">📅 15:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677715">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6b73bf56.mp4?token=bnQZ9sDBns0u7fUK3_9Gziheg6kt9nGxG-YzH5HzlgoXPOtv3EqPvN-rnSMznGOJjNcsLGzaZWg9GHjbC9UnzNdlBA7Ies2uaJFQ5krf944s7Nhspkfr-vAwae-o9lIT9-hz6I8x36ah4sql-F_ReeXgpoae2avRhq_i6dbSg_uLb7ATb3zagQCHLnD55rDUMlbTv9bsfiTMR7eGerksVqDtB8uV2Wt1Wq4kQV_wGhUBVpXSjQaomPWV1ZgEqEmipFV1P3eAHev8Qeu88qGtzG0Z1OQsvtriQYo0_NF928ZahZiitoGTRXQ4MTuvmlzeRWHvwIovU07Lznw8kxAU2JsaahVJ814WHJGOzZEB_feLPtgPxNav1DJhA8J0LvytgzpebdOQ4VVbcCgr9KvB4M-skEXnr6tYSSuRV-KApm-XCiAzQM6KikzBSFqSYLKRo5vgIse4vto7cSwOcxDsICS9hQ9-hN4MQNH1sPBrQstJALoLLwyq5avGFuqRtRZUGuphdiuepSF8CcXQEpW9YwN_Kv2GxCnQZpX3sX3ApwxzS0lwTUy6oDHabenUMzwwtauK8qhm0UeBpRcMj2HqH0PvVSXEuMIsEso3BIsjmgYAYjvFGQIPQeNJSdBd7x-5SvTzg_5lfgsQGkgJMgyv_5zhJlrWQ9Kh6GsOX6tKlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6b73bf56.mp4?token=bnQZ9sDBns0u7fUK3_9Gziheg6kt9nGxG-YzH5HzlgoXPOtv3EqPvN-rnSMznGOJjNcsLGzaZWg9GHjbC9UnzNdlBA7Ies2uaJFQ5krf944s7Nhspkfr-vAwae-o9lIT9-hz6I8x36ah4sql-F_ReeXgpoae2avRhq_i6dbSg_uLb7ATb3zagQCHLnD55rDUMlbTv9bsfiTMR7eGerksVqDtB8uV2Wt1Wq4kQV_wGhUBVpXSjQaomPWV1ZgEqEmipFV1P3eAHev8Qeu88qGtzG0Z1OQsvtriQYo0_NF928ZahZiitoGTRXQ4MTuvmlzeRWHvwIovU07Lznw8kxAU2JsaahVJ814WHJGOzZEB_feLPtgPxNav1DJhA8J0LvytgzpebdOQ4VVbcCgr9KvB4M-skEXnr6tYSSuRV-KApm-XCiAzQM6KikzBSFqSYLKRo5vgIse4vto7cSwOcxDsICS9hQ9-hN4MQNH1sPBrQstJALoLLwyq5avGFuqRtRZUGuphdiuepSF8CcXQEpW9YwN_Kv2GxCnQZpX3sX3ApwxzS0lwTUy6oDHabenUMzwwtauK8qhm0UeBpRcMj2HqH0PvVSXEuMIsEso3BIsjmgYAYjvFGQIPQeNJSdBd7x-5SvTzg_5lfgsQGkgJMgyv_5zhJlrWQ9Kh6GsOX6tKlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحول دیجیتال در قلب شهر مشهد
🔹
شهرداری مشهد با اجرای پروژه هوشمندسازی کیوسک‌های شهری، گامی بلند برای تبدیل شدن به یک «شهر هوشمند»  برداشت تا دسترسی شهروندان به خدمات شهری سریع‌تر، راحت‌تر و جذاب‌تر شود.
🔹
تلفیقی از تکنولوژی و زیبایی شهری
https://samesh.mashhad.ir
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/677715" target="_blank">📅 15:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677714">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781b3315bb.mp4?token=XI5xkemZaQ9TirTz1eJdKOutRMyuMKvSzqTyTpkRvg5p71duKO4icPk3qQo6mR4eCdftfXjvrnXsrdYLNpz7-gW56_TOjxNs09NjZnKNrZm14cfd0yoQ5rarwxu4eg1xIBuT7b7-ZNuVs6z93R4IZJwt2M8JJRaKwFRFWJclwmy9G61wX3sZJwcd0eJGXqjhTsKv11YqzR43AY6nNgv9Mt9PBZYtHbjviHH7bvKJQeF-PFa7AZq1F7fnUlym6dN_Jn0IuNL_dx2pgTJqoM93Of4s-fDRd41gHMauyuufd2_UKY7HuAOWYh1fqsNnlMHm0VHbj6HLnWd_NAUIkWJtMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781b3315bb.mp4?token=XI5xkemZaQ9TirTz1eJdKOutRMyuMKvSzqTyTpkRvg5p71duKO4icPk3qQo6mR4eCdftfXjvrnXsrdYLNpz7-gW56_TOjxNs09NjZnKNrZm14cfd0yoQ5rarwxu4eg1xIBuT7b7-ZNuVs6z93R4IZJwt2M8JJRaKwFRFWJclwmy9G61wX3sZJwcd0eJGXqjhTsKv11YqzR43AY6nNgv9Mt9PBZYtHbjviHH7bvKJQeF-PFa7AZq1F7fnUlym6dN_Jn0IuNL_dx2pgTJqoM93Of4s-fDRd41gHMauyuufd2_UKY7HuAOWYh1fqsNnlMHm0VHbj6HLnWd_NAUIkWJtMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مترجم کوچولوی موکب اربعین!
🔹
این پسر، مترجم فارسی یک پزشک عراقی در مسیر پیاده‌روی اربعین است و با ترجمه‌های بامزه‌اش توجه‌ها را جلب کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/677714" target="_blank">📅 15:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677713">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCRI5jrNYkBQrPWY-myyBT90gKo01EzAdwBIouQSRLHZEyFg6yP4x--CoGP5RQ32RA_5JmamTWoXuy1LnOjDlvpTUGwtj70o2O4j3lFV7CzuPYkgiJQTXWe6A1J3p3_tGkM5Qz8KLGVKcTxwgm1S7ackdHczt8TToK7z9SWdmhe3kUd8tSQ_tykeUiUtC6ZHtHv_hW9lfEU0PYl7RJ2VLFVakPEhKJAj3Ek6My5o3ykPrHOWB0eGTZhHXnWIerCo9Pqdd6cL2XG6bABpho19BTKfD3Wqtw1-LdRa5nqQR0zToktEMAvCOt3055rrK9MF2446eV60bloikR2xed1ajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
من حاضرم همینجا بمیرم  ولی با جنازم یک متر از این جزیره رو حفظ کنم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/677713" target="_blank">📅 15:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677711">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
جهش قیمت مواد غذایی؛ روغن جامد با ۴۰۰ درصد رکورد زد
گزارش مرکز آمار از افزایش قیمت اقلام غذایی نسبت به تیر ماه سال گذشته:
🔹
مرغ ۱۹۰ درصد، شیر ۱۵۰ درصد، ماست ۱۳۰ درصد، روغن مایع ۳۴۴ درصد، روغن جامد ۴۰۰ درصد و سیب و موز ۱۰۰ درصد افزایش قیمت داشته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/677711" target="_blank">📅 14:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677710">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcAwtxDyoLI9cRXl5QtRrdHJnivjK2JgxShj4FOqqBJebHFRbh7jDZ13nrZdsLCMaYdqiQh2sJ8IyIKLpvHWe_d6hiNiJv5Ic4WLJb95hJgjlNjFS_ikkAF8HwqFr6ytOGfbg1sgftOeb5p5bkQozHAbHozN0ZmMjvgDYksIjvNDQV_4OEXMthBAVM_FZ11e9zZdNky4rTUPJ-H3VrY5ELxnoiSVasE95kXY5QG4YxLEsLNIGnzWqD_iIBu5R2u-ysKvP149wJpgg7EaMcDZ1NDyJ_IoxmJS1P0yahROVcq60pLWsOaP2pj7uFaVL3XLYTO1CAcq7FrUZb8SDXBM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صورتی رو با کدوم رنگ استایل کنیم؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/677710" target="_blank">📅 14:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677709">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8ef43fde.mp4?token=jq0hD0x6nSRatk6yVQly6BKUFCCIsbV6hF2AaaFLRmwfgE0IK6Aq2b6jxguRYyoUwlCa29yFlMlrmVK9KpPvXODMBFEtNOd5xs9cr4nYF8ZRSoN7dvGzzu56hVXli0fxs6s7TuiTJbOQs-4hBshZqqd-xN71cOohrAKzRHfOM_IThWmm2T2Ipef0w2sO-co9-4P5s40s2dfia_0MsZwCgkX1jvkVPTwzI2wSKdHD9p307akvEHI47lVQo1zzRD01d_JT1rtsevKPtIgRzAKylmuac-ui8BJtfk_4cNpgH1NQBiVEe5x8QRFwFIrH2GApvZQ5UmlQI6e7uVoRuG5vKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8ef43fde.mp4?token=jq0hD0x6nSRatk6yVQly6BKUFCCIsbV6hF2AaaFLRmwfgE0IK6Aq2b6jxguRYyoUwlCa29yFlMlrmVK9KpPvXODMBFEtNOd5xs9cr4nYF8ZRSoN7dvGzzu56hVXli0fxs6s7TuiTJbOQs-4hBshZqqd-xN71cOohrAKzRHfOM_IThWmm2T2Ipef0w2sO-co9-4P5s40s2dfia_0MsZwCgkX1jvkVPTwzI2wSKdHD9p307akvEHI47lVQo1zzRD01d_JT1rtsevKPtIgRzAKylmuac-ui8BJtfk_4cNpgH1NQBiVEe5x8QRFwFIrH2GApvZQ5UmlQI6e7uVoRuG5vKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیافت هوشمند پسماند غذا در مدارس چین
🔹
مدارس چین با سیستم‌های هوشمند، باقی‌مانده غذا را به کود تبدیل می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/677709" target="_blank">📅 14:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677708">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📱
اینستاگرام تمام پست‌های عمومی را با هوش مصنوعی تحلیل می‌کند
مارک زاکربرگ:
🔹
متا با استفاده از هوش مصنوعی، تمام پست‌ها و ریلزهای عمومی اینستاگرام را از نظر محتوا و لحن بررسی می‌کند.
🔹
هدف از این اقدام، شناخت دقیق‌تر علایق کاربران و ارائه پیشنهادهای شخصی‌سازی‌شده‌تر در بخش فید و ریلز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/677708" target="_blank">📅 14:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677706">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac27ed8c7.mp4?token=Vq1uImr8EwJFWc4DL02e8ZyswjRHSQR4pd-81IrUUdFFWHTP2bHCUjkovVCDUSsg7ZU4ZwTMgJREgKC_Fbt62p8l99ixx8pwhZl13di5tQUw8JseSPfc7NU5DVDSR_Mc2Yi6XPYGTC_Ho4VcmniiN_dbhaSVucNcPr48mfO0RxUMtmRNc21OfZs5jq6ywYGqUyCv0Ic_6s9IzTZRRKMMi9mWJrVdXHDtk8PdCdtxBWugy6odQMR080Rt2Ullsxuy9i7IQYF_OS_zLEyj_ayTdPjT_K6FiOaFdLDdpojbnAsxr9hJ5p1gz4dR7I2eWMrtq20BDSm5siZfOF14MuOsDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac27ed8c7.mp4?token=Vq1uImr8EwJFWc4DL02e8ZyswjRHSQR4pd-81IrUUdFFWHTP2bHCUjkovVCDUSsg7ZU4ZwTMgJREgKC_Fbt62p8l99ixx8pwhZl13di5tQUw8JseSPfc7NU5DVDSR_Mc2Yi6XPYGTC_Ho4VcmniiN_dbhaSVucNcPr48mfO0RxUMtmRNc21OfZs5jq6ywYGqUyCv0Ic_6s9IzTZRRKMMi9mWJrVdXHDtk8PdCdtxBWugy6odQMR080Rt2Ullsxuy9i7IQYF_OS_zLEyj_ayTdPjT_K6FiOaFdLDdpojbnAsxr9hJ5p1gz4dR7I2eWMrtq20BDSm5siZfOF14MuOsDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تراژدی در دریا؛ آتش‌سوزی کشتی مسافربری در اندونزی/ ۵ کشته و ۴۱ مفقود
🔹
از میان ۲۷۱ سرنشین این کشتی، ۲۲۵ نفر نجات یافتند و عملیات جست‌وجو برای مفقودان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/677706" target="_blank">📅 14:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677705">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6ee52879.mp4?token=GUgFYdZmPXPX7CS-46DlSBeHl2EOFAiGQEFAbgl5XMS0b8fb54VVyIOFydnyXQTtkyKuJdtz5p21n00-gGRFgaGUwvG6sRdOGGCe9a2dKyN3h2U-dyGfbKggjKxkHTNCq6AJpjfuYv-S841Exvg3S0h2NplRI983uemFJBR8bOlqPwxbOMSsx5wQRH0ZP_nMAhgQFyCdI5BzyrKHM3x62YbnSmg54KfayPezWGgmpDbokLBra8A1Z-GMY6eQpc9CeVDBO6D2sR3kzM0Djwp7dMRDfjUAPua0Ku1fhcs4ckqv9oT6dpznAHDXSzi1iNL2-Qp7JLzw6EjM9Am182Kc_ztxKHm_ee6JYvPWoPGytD8ZcnkcbVNMpt7jAK4uLhM61IEbVqDPoJxeNkVoAsnngIirBIcHyWN49Ji2V6TDTPqf4lUdkuV6Xaqfci-6E-8bNSH37F3KHUlyIqnS0owZ1uHB2NewMMopIJh1HDk7v0B45arPbUEOmtTq1ttLTUcbbCrtOj-yZu4B-S_uRKhb8CyA-EfO4RDu4ideO6-SMe77LOYKTuVhzgaa037KtdHSlQV7wbRtX1snAm0e9omUkYtLB4UyPHyzxgDgfg_emGaV2QZg6gfDLoPS2f10R1TYRHF2Ss9NrcL9Xheaue0hAKLKp3F3Qv82Hgqt1RpTaBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6ee52879.mp4?token=GUgFYdZmPXPX7CS-46DlSBeHl2EOFAiGQEFAbgl5XMS0b8fb54VVyIOFydnyXQTtkyKuJdtz5p21n00-gGRFgaGUwvG6sRdOGGCe9a2dKyN3h2U-dyGfbKggjKxkHTNCq6AJpjfuYv-S841Exvg3S0h2NplRI983uemFJBR8bOlqPwxbOMSsx5wQRH0ZP_nMAhgQFyCdI5BzyrKHM3x62YbnSmg54KfayPezWGgmpDbokLBra8A1Z-GMY6eQpc9CeVDBO6D2sR3kzM0Djwp7dMRDfjUAPua0Ku1fhcs4ckqv9oT6dpznAHDXSzi1iNL2-Qp7JLzw6EjM9Am182Kc_ztxKHm_ee6JYvPWoPGytD8ZcnkcbVNMpt7jAK4uLhM61IEbVqDPoJxeNkVoAsnngIirBIcHyWN49Ji2V6TDTPqf4lUdkuV6Xaqfci-6E-8bNSH37F3KHUlyIqnS0owZ1uHB2NewMMopIJh1HDk7v0B45arPbUEOmtTq1ttLTUcbbCrtOj-yZu4B-S_uRKhb8CyA-EfO4RDu4ideO6-SMe77LOYKTuVhzgaa037KtdHSlQV7wbRtX1snAm0e9omUkYtLB4UyPHyzxgDgfg_emGaV2QZg6gfDLoPS2f10R1TYRHF2Ss9NrcL9Xheaue0hAKLKp3F3Qv82Hgqt1RpTaBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از حمله آمریکا به یکی از زیباترین سواحل خلیج فارس در روستای بنود عسلویه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/677705" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677704">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5TztulqKy8fytx3dU7ZdMUIExeZh1EHp0aqQWHuvp6vyHK5uRll5edBr-7qGrDvMqODXE4LDTJVejHFlJUGG_BhNYDZcID8jS27sBC0dOCHnb46h2Glh4gcN6Lwm_SetzGyQUzfaOvsrelLrBJVGJuDpFjbD8sOQ0hb3KmlNPu7mKo9xmTqOpaQQ1-OcjjaYLTFkzCr_x-eH-pT7adlQCO2-94rtUKukuFwNt1YZSN0fXOGbFzbIUXdIIt1y78ypR63FPKXth95tRWmkX8tLtpf86KidR12wvN5Lt5Rkirjzh5PpkHMO_w6WNUU9V0sZkEOhyO3h9CVB44M1vkA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲۸ هزار تولد تا ثبت جمعیت ۸۷.۱ میلیونی ایران
🔹
بر اساس برآوردهای مرکز آمار ایران، جمعیت کشور تا پایان سال به ۸۷ میلیون و ۱۳۴ هزار نفر خواهد رسید؛ برای تحقق این برآورد، ثبت حدود ۱۲۸ هزار تولد دیگر تا پایان سال ضروری است.
🔹
بیش از ۶۷ میلیون نفر آن جمعیت شهری و حدود ۲۰ میلیون نفر هم جمعیت روستایی خواهند بود.
@amarfact</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/677704" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677702">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تیزر قسمت نوزدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای بهنام راعی که با داشتن غرور جوانی روزی به سینه پدر لگد زده و چند روز بعد بر اثر تصادف روح از جسم جدا و در برزخ شاهد عذاب و شرمندگی به خاطر گناهان دنیوی می‌شود ولی در نهایت با دعای مادر و عشق به اهل بیت در کودکی و شرکت در مراسم عزاداری، مورد شفاعت قرار گرفته و فرصت جبران و زندگی دوباره به ایشان داده می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: بهنام راعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/677702" target="_blank">📅 14:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677701">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVvz2QPkRmjm3Fs8pbtvC94ttrFgzQVIWc9sEkbL3L1oGa7DIoh42zqRALWxrmVnoN3_42FGL2bAlDWwJ3cgXNpU-4K-0cGgGfcGMS3bPwA75KSYuH-eqkEBuxn1JH0hoUo7PjYVLgM7daAOIHWnDfmLziPrQrDHOWG-WLyNWyP8f0mGcMMXxn-dBS2dQ_9tBqjgMaK16s8Ou7lfHxJs97qy7q83hqRiEUe-NC7HUEpDu7_0pSBbgk21R2kH1yqD1WQLnbWiYI0W8iOo2rYWZ_53oSm9l0oyhLIeLXOqXiC7-hc5PI7zc5IPtfOB3Blqtn2khzP9H5lzhjnxYEW7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی با انتشار تصویری طنزآمیز، نوسان در مواضع و اظهارات ترامپ را دستمایه تمسخر قرار دادند :)
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/677701" target="_blank">📅 14:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677700">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8408da7d.mp4?token=bjfTp0rZAs0JMn4U7gwA25oxYR5WEWOfO2nuYJJH61L0rx4aAN6dBvZUchh8UfQB4hXf7eXlSqSd3JzeaYSPwpQTyJ4lY7JlR6pVcU8gtpqmDoJoYwrKmDPsNluIRaZBV5kUKA_53fcmo5Sl8_0YnE0c02hVjhoPpcKMGXBSxdShN5dGBn9zc65rhzP_QLJzbDDNljZWI4RTqWgEBJcYhB-mLV3BHvLzsJgNeKfG1BNicW157AZwlVTcaMTuk9pdRzklG2RPDaREBT-Bh3Up8Vpj9yjpdf9JfYaElBlkBvs60GkBxwg1S6VMJtjSJcqZe2FxxLRDFPq5I5lwmPaYwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8408da7d.mp4?token=bjfTp0rZAs0JMn4U7gwA25oxYR5WEWOfO2nuYJJH61L0rx4aAN6dBvZUchh8UfQB4hXf7eXlSqSd3JzeaYSPwpQTyJ4lY7JlR6pVcU8gtpqmDoJoYwrKmDPsNluIRaZBV5kUKA_53fcmo5Sl8_0YnE0c02hVjhoPpcKMGXBSxdShN5dGBn9zc65rhzP_QLJzbDDNljZWI4RTqWgEBJcYhB-mLV3BHvLzsJgNeKfG1BNicW157AZwlVTcaMTuk9pdRzklG2RPDaREBT-Bh3Up8Vpj9yjpdf9JfYaElBlkBvs60GkBxwg1S6VMJtjSJcqZe2FxxLRDFPq5I5lwmPaYwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: عده‌ای در کشور می‌خواهند مذاکره را ممنوع کنند/ دشمن‌ترین کشورهای دنیا هم در طول تاریخ با هم مذاکره کرده‌اند
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
پاسخ‌های ما به آمریکا باید پشیمان‌کننده باشد، اما هیچوقت در مذاکره را نبستیم. تجربه گذشته نشان داده به حرف‌های رقیب نمی‌شود اعتماد کرد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/677700" target="_blank">📅 14:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677698">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/677698" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677697">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ff33ef79.mp4?token=N2bO_9THo5uDwRLzMGmnVypkFsP56Eu-ZD1gaVA7Lq576jZP-StjD8m0iOsoo_Gc1gmLR-gKVN_YSlYZWfL0aZLQqb-9bGcFIMsadA8Qx2Qs9W_5RYiIkxbpbIwGTS2cKjMvFU8CempUa_ukWd709sENmc_woykf-vWZ3xyGWsyGkv9W37pgG2h3BFopl37NplMYut-YWS9DfMlZpOda5c9_0pIpgEQW-NIFupQwX_S6UuEL3VZdy0nacWMTXuBcWT8yiduMDNg4cSnpcMXkaHx7aU6rXvLK1IL7SE_ByT9F3GiSks3BEk_ucv8tgyxpLlT5WYcp-sXmY2hz-PYziA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ff33ef79.mp4?token=N2bO_9THo5uDwRLzMGmnVypkFsP56Eu-ZD1gaVA7Lq576jZP-StjD8m0iOsoo_Gc1gmLR-gKVN_YSlYZWfL0aZLQqb-9bGcFIMsadA8Qx2Qs9W_5RYiIkxbpbIwGTS2cKjMvFU8CempUa_ukWd709sENmc_woykf-vWZ3xyGWsyGkv9W37pgG2h3BFopl37NplMYut-YWS9DfMlZpOda5c9_0pIpgEQW-NIFupQwX_S6UuEL3VZdy0nacWMTXuBcWT8yiduMDNg4cSnpcMXkaHx7aU6rXvLK1IL7SE_ByT9F3GiSks3BEk_ucv8tgyxpLlT5WYcp-sXmY2hz-PYziA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی «دقت» به اجبار تبدیل می‌شود؛ OCD چیست؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/677697" target="_blank">📅 13:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677696">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5GrWY_fnHdrYV1ga5VXVto3_fyBAfyY_eUzVLncOYqLyHtxPoeVWCMO80w0k8d37hjsIvEcmwdg-gNUfmTJQKpxFpWVbIiq6Z0ZaGqEJotxa4w-Pqqyl1aZF6pSSsRaS72rEQelANGPoApmxOs7di1MgRkjjp5GTQXrLS-IHdD3ao4BASslPWwJWM110FPtrVfAORPSNEOIBnftVBNyKMWYqGssVLCzgJWdk1bhI5QzKtUYGSLG9s3NqjRToCzbSwdWjMi9zZRJCu6vuvvy2i2z_xfKkQ1zV-f6n1RJYgySsAf7baQeBTYadc_aPRZyqBVpaaH8Nfux8Xw2fDstrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
شاید چیزی که اضافه برمیدارید سهم کسی در انتهای مسیر باشد
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/677696" target="_blank">📅 13:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677695">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s42DuIKmwa82Fjnbbf2mPji5r7i_ZMiWFK1JKg-foq04IxAD7rz0suLAFloy2AumMawBhDXtZE0ke4FtWJ3o9m-L1H_nR1w_qhQn83FxnuH8a6jsnIIliDxSNvW3FWmLH074oe81cG4_IrOm8btzofK7sRbTrevqiHMn0yo-1k3S4x7elbsTc43_U3jn7VfxRXtO3nYs7eZ0fsvB2DFFokTiIJOWA9bcRG_bjPkzvYFSLdvc6UPLGZnrOH5Thtd3R6b_pg5J6tyC03dZXVrGcLCdOzCfk9TYXvvKTi3iy4MRwUMEYphKsrWfvZqb_5ofnFzRfJ3h242fdd65AX3RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر اقتصادی: هدف ترامپ از اینکه این همه تهدید می کند و حمله نمیکنه اینه که حمله به ایران عادی بشه و دیگه قیمت نفت و بورس رو تغییر نده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/677695" target="_blank">📅 13:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677694">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/677694" target="_blank">📅 13:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677692">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBS63rHMtYv1iC2oT2es9cN6FRlFMOgX0eqBD01WMvm1cxoBntxLS2jPGlY4khxDYYj0WfIi3vCP2zcW3fA2rkH1JGbfGd0arv4yic2s1Zvw25axyH1J4k8w-UEPtT8Sh3svzHZ5PrjEVYvJ5Sa29Z5CR1GH3AOMew7VTqG4IZK0ftmqvdVcISNhZOuLOgEH8sG3uJmENlNAYkkA4VZtbvmKJuXrKzDToXHXgkZJvBtiHj4ByOG-i6PxChK5BUMJO1I2PxyHYz7wZU_lCcfEdo1AagRzmMoq8JIWrjALTpp0CJkZU5RcVL8lFctrPvjLaP2wycXMy3CS2dMEOR6ZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سواد رسانه‌ای در شرایط جنگی (۲)
🔹
اطلاعات نادرست در زمان جنگ می‌تواند به ایجاد ترس و اضطراب در جامعه منجر شود. تکنیک‌های سواد رسانه‌ای به افراد کمک می‌کند تا منابع معتبر را از منابع جعلی تشخیص دهند و اهداف پنهان و سوگیری‌های پشت پیام‌های رسانه‌ای را شناسایی کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/677692" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677690">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmRh1j-YdGleYNJTgXESE9AhJETR3zF5kBiZyKjY-aPGjTL929xbaurHWNjJxd2IPU48bGW11sfOb0KOTZOz3EZpguS-XUVRSE7U9yiAxKbexILGQuAMb0eKXkksbHrVl53Yohyuankh4HK_hcv5tdjqtxwNMKXEp2P8HEmTjQSLZ-0YwEIWCw7TK0QMTKSqskW2c3T2tscO8QnJhZHWPVOWvY6dsaixPOktf2Cp6ale9OmRNvBBNzIYDhCX1G0VmoygomE8Q1bEWrPHNDFzYcZnM2I39DGrc5YqpcuwR1-m8et-DWSUBLRSOQAW4YKEvH3vsWipY6acst5lV7T44A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTcGCunXKQyUh4Aab6HjpGuJnh5kReRccof0M5YJ5kKi907qrBk5NmEDqbN-3cIh1hAkVffnYV5jFekZc8N0cF_H08q_-7S9FJF7BGOrCzydzVK9GxUIZbePQzjUviGa5d0eWaMoTCN2QOu7HCuxN_hOLxVFDWtlNxaxCilkF11t-8bWS3I6MWkXlVgtwpP5y7qUSKBYAOQgVLo2kK6YhA1Sni3cBB0cBSSYlCKO5kcBkCgeJiRw9I2xCQdQLce-e6weP2ZZuQguy_uguLAgzngpwro3wVtPWQbWqa5nXgoqDUV93PuMEj1WgokaarPWnPEKC80r0Z1D_HYXyRXRwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیشب دکتر محمدطاهر ابوغریف را در موکب نداء الاقصی دیدم. همان پزشک محبوب کودکان که با نام "پزشک معجزه‌گر غزه"در جهان نام‌آور شد. محمدطاهر عراقی‌الاصل و ساکن لندن است اما خانواده خود را رها کرد و داوطلبانه ماه‌ها زیر بمباران وحشیانه‌ی رژیم صهیونیستی در غزه ماند و آخرین جراحی بود که آنجا را ترک کرد. او بیش از 300 عمل جراحی پیچیده انجام داد و بیش از 1200 مجروح را درمان کرد.
با او درباره خاطرات و مشاهداتش در غزه حرف زدم. هنوز عمیقاً متاثر بود. احساس کردم آنچه بر او گذشته دورانی از سلوک معنوی شخصی را برایش ایجاد کرده. او به آیات قرآن پناه می‌برد و از "صبر" سخن می‌گفت.
گفت حالا دیگر سخن از دوگانه‌ی شیعه-سنی یا دوگانه‌های دیگر حرف زدن جایی ندارد؛ دوگانه‌ی اصلی "مقاومت-تسلیم" است.
[ان شاءالله گپ و گفت من با دکتر محمدطاهر در تلویزیون پخش خواهد شد.]
✒️
#روایت_اربعین
۹
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/677690" target="_blank">📅 13:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677689">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1d20dfca.mp4?token=QH6RHmrBt7lN-aypqTh6KgV561gmFFV8Gm_4HNx228GIO4cQWnyD_RbNXNCFexX0bIHck6ZZ-vYvome5-w0Q2PFLElSIN5OZWwwxfKa0OV9Ydtpgwm2U6l5g2kqrFkxew49jSJgH5LmH6_KJEsWwMVfb7AXDo46YyHUyl5_cTN50rs49ZiZLZfJQ09-4EzIgyXnA-a-p5d19kFDxixyVZQU3bIWFRENnJ8R_zbHsvvDpYlK32qyxCzholbofjIMNtNaOD7jniocQulYeCcoK_uBT3p6eyRTeF9HKSq6ZuidfuRhLZpc6RfYnlMjkdIldbABdzau75NY-XZHluNMgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1d20dfca.mp4?token=QH6RHmrBt7lN-aypqTh6KgV561gmFFV8Gm_4HNx228GIO4cQWnyD_RbNXNCFexX0bIHck6ZZ-vYvome5-w0Q2PFLElSIN5OZWwwxfKa0OV9Ydtpgwm2U6l5g2kqrFkxew49jSJgH5LmH6_KJEsWwMVfb7AXDo46YyHUyl5_cTN50rs49ZiZLZfJQ09-4EzIgyXnA-a-p5d19kFDxixyVZQU3bIWFRENnJ8R_zbHsvvDpYlK32qyxCzholbofjIMNtNaOD7jniocQulYeCcoK_uBT3p6eyRTeF9HKSq6ZuidfuRhLZpc6RfYnlMjkdIldbABdzau75NY-XZHluNMgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لجستیکِ غول‌آسا: هنرنمایی تریلی‌ها در مسیرهای باریک
🔹
پره‌های غول‌آسای توربین بادی با طولی تا ۸۰ متر، به‌دلیل ابعادشان نیازمند تریلی‌های هوشمند، برنامه‌ریزی مسیر و گاهی بستن جاده‌ها برای عبور ایمن هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/677689" target="_blank">📅 13:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677688">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwDMaeUIQYY6As0-6sckc3S_bS2H8mzdKclSj5Yau-4g2GR_eYDTbreWx7QLqgVsh7QLdIFKFe_MK9ovDEjBN_3dBUYM_h68mY8XsX6w1MEaLJm5NPNuZJ1mNpPr6aoDFqLHs-FcwT27JenT2yq1QpPEGMWS_QyYV-sHt5cEao3Px994ybZW917Hjm31EEfBiUxj7SJuNs9vQKSgwjYcF_Z9Ifu0L0evzSuQaX5KP1KtnvWXzubxgj21B1OkoJlqxRWy3L85s28fA-3ay0zDN-W0rgqx2WBtI8Ew07M-sGA1f54SeaR3hBFOj5Tm7w2PpawnISTN5A0z165F1GJWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه‌اندازی رشته «تولید محتوا» در دانشگاه‌های آمریکا
🔹
دانشگاه ایالتی آریزونا رشته کارشناسی «تولید محتوا» را راه‌اندازی کرد.
🔹
دانشجویان در این رشته تولید محتوای دیجیتال، برندسازی شخصی و مدیریت شبکه‌های اجتماعی را می‌آموزند و برای فعالیت در حوزه‌های بازاریابی، برند و روابط عمومی نیز آماده می‌شوند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/677688" target="_blank">📅 13:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامـیـن‌الـلّـه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5VVE6NXKsI9ZHcmwya34hue9HkE_JCxQ7QN-BhjRodVbqw2pkNjhc6HXlRyb4c6j-kcG9afq1NLXk4x3G-nFG5ew6RM16CkCtblNF18Qdi-Lc_3wpVBfoOnd_foyVVD9c64MHjr0GjrKqeS6puBzRPW-DkQnAGrkDMAkB2Kpsc9jCx4EejiQdynrS0X_LEgBlp8ZT2BUixwKBPl7xEbsAATcJyZXgnlH7prju5pgVZ5pj5qE2QztglBCGDxyzD1BK96T1u9WyxzHrYLQ-uo8oApnuDPd2--0SwvGp27u4qsatQnJPxIwiJ9ZB8Mnw0Eb4PKGQ46IcdFOSZlx1faNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vSPAHmdBMPxd8lgtCopwLQB83ND3PJoFpyTlZ1043UAHjg7t8ahgExG8d3_TyJew5WPTckYoDlw31ydxahScZSqRhOmIgwZISXBvj5HZ0VsXBEqXy7-RSvEWXCnhFcBa6QNvQOt9dqdUiZQddoVFGCJ8bDvYdxZ4s0hMY-zexkYMV5yuQjpeowuxJYFjRJeLaJNr1ePBCBkfP8kQeRa2zjjZ1i4ydxc4tcImgGpMPB7uAhQUgG661jsmcb7F_xMrZEHLWeM5BztJ3Tf84l4tIkPpdblbfiq9sjYjKqpRj0Zz7OZ2Td-c7m2Jzw8qC5UTt84Uy37MogQCF8nElCy4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qertR3RR6YZ9cJCKs6iwshF7Hlq75EFTjwonwt-NaXwLGXhBNeXIXPPcBkPYkibJZryzXahHMewFyD1q5Y8S6wCf5oAFt3McinPcoD6dDKdXnD4u_5WtLYlLzJQHAmRQT0Zj0-AFKjgnn5hPiC18j_2LeaGRqf3kM4KELtAU24s-yYgk8FkYYb8XbQLx-KJ_tWOzR8Toeyx_S6khQDSVich5aObcMAT6_CbNscPq6_AWaWoYpQ5j2tf7XLVbceDr71_cvSO9hJDq-ZDWn9ToJLu5GMX_sfF9H7X7JHH9Ekg_G-_cRB2yJoj_rQF_k8d7UjM0sPXV-HjRIv00c5zNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIkar2NwcdSL3sGmw7lkA9ToJ11-WHkHIdJUB9jrwS_ujxW76V8LICnSkQiHSdLf2iOeHAxgqz2xfoW14vFaZhekOvqa1sSloucS48bYPAmETM5Nc2u0eFuYvhfc2YE20D06ZUdn5vipHjZJB-Mwu1QaIxj5N3ZpaMM0K7HqjVx9_Q9nplvLZihqdEyFPoZ3pe_UUI-ZyGXiC7lLyOlfybwFCcLcR0oZzRXbf9B_ufDjO3wnepzoV9mrJPVp-GrqY5MYL80BTyTOfInBsbTrY7_tjTTcofBL7sTlZl_csVrnL-IBq4aOAbDV8i3PDiSMGkGT-63g2vs8f3eAGGh2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwcGerT56m9NGLnePFYzMQjIVCZ0XXV7fzrufuehk-z6o6O8a8NSr3Iv5ly1ep3ScUbMOvzrfc3HqS_B9zEiQbjDBQoNiX0w7aAXyfm6mt7jyxi0bP198TlAYn3V-3LNNc5k72t2cQU9aFsZNvF5r9M3UmCHjknUxFf7TDrIQe8-5WXbcKnSYNLVE2oSxQLY_Y-kib6jmJn7Hf2ycWswnU8Xz0ZBxNON9TMUzm6QSijC6J5Y1fhacN9Up7nalWZ32gyLFiym6NnZJE5yZpntQZn9Lh54ITe02Hr8PV7Vy8Jw38_vyhASZf-tVSKPhSXl764rO4Tf3-VXSkJxgK_2Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">؛
ارتش حرام‌زاده‌ی آمریکا به دستور ترامپ برای به شهادت رسوندن این خانواده از یک بمب ۲۰۰۰ پوندی «مارک-۸۴» استفاده کردند؛
بمبی که طبق ادعای رسانه‌های غربی توسط رژیم صهیونیستی در حمله به مقر شهید سیدحسن نصرالله و ترور ایشون ازش استفاده شده..
این جنایت همون «اقدام بشردوستانه‌ایه» که پهلوی از اون حمایت می‌کرد و خواستار تداومش بود؛ حمله‌ای که نتیجه‌اش چیزی جز به خاک و خون کشیده شدن غیرنظامیان و خانواده‌های ایرانی نبوده و نیست..
و نکته قابل توجه اینجاست که خود آمریکایی‌ها بارها ادعا کردن، بمب مارک-۸۴ بدلیل داشتن سامانه‌های هدایت دقیق، از دقت بسیار بالایی برخورداره که احتمال اصابت به هدفی غیر از نقطه تعیین‌شده رو غیرممکن میکنه.. به همین دلیل یک بار دیگه اثبات شد، جنایت مدرسه‌ی میناب توسط ترامپ و ارتش آمریکا اتفاق افتاده..</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/677682" target="_blank">📅 13:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677680">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
مژده لواسانی: کوچکترین مزارهای دنیا رو در گلزار شهدای میناب میبینید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/677680" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677679">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=fqJrlXOo6sywgULF9i25AEvJ4u7z97tremdOdZG_Vo6KqYttiFcPV4Tx5fA0M-3eGKkOGhhVzpbrJ3CQeuYdN2_SXS9ZLKN4Mo9M2wZLrJ2x-UDnsFc4qIWdAcKZCx3qlmsUCa2qwM_vWqoxgFmjvr0NCjolBnRA_2NBTbfOCpEu9BN86xfQ-vxBJwP2oevvBJxa3Y9T02Ea21LMhJc71lgE-YSJQp8goz2e5sMryMV_m53IdIwYGHxHt_pj7Hd6pUk_8LX2XzWo18nADBhoVoYzdOzePacdGwXt73tvGPxKEtpMrtdIShNYmZFyZNsOSpPoumiPmdeVS5G6tjb28w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=fqJrlXOo6sywgULF9i25AEvJ4u7z97tremdOdZG_Vo6KqYttiFcPV4Tx5fA0M-3eGKkOGhhVzpbrJ3CQeuYdN2_SXS9ZLKN4Mo9M2wZLrJ2x-UDnsFc4qIWdAcKZCx3qlmsUCa2qwM_vWqoxgFmjvr0NCjolBnRA_2NBTbfOCpEu9BN86xfQ-vxBJwP2oevvBJxa3Y9T02Ea21LMhJc71lgE-YSJQp8goz2e5sMryMV_m53IdIwYGHxHt_pj7Hd6pUk_8LX2XzWo18nADBhoVoYzdOzePacdGwXt73tvGPxKEtpMrtdIShNYmZFyZNsOSpPoumiPmdeVS5G6tjb28w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهیدی که بجای سردار رادان در جلسه شورای دفاع شرکت کرد
🔹
سرلشگر شهید «غلامرضا رضاییان» رئیس سازمان اطلاعات فراجا ملقب به «ابوسجاد» که به جای سردار رادان فرمانده کل انتظامی در جلسه شورای دفاع نهم اسفندماه شرکت کرد و به شهادت رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/677679" target="_blank">📅 13:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677678">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a26eaf0d.mp4?token=iLh2oHWgmTUraT1Sq6p5G1dnvexGybNeunRGF1PGVgjOiYTDKyKXwueZfB36U0hmHDb_UTZM7Kv5F25CNd5BrRTQNsGU20F0X8fsqQSSFBa4XMKqcMHeYG7_meeY4-jhfbu6kJ_2LEZP_ujfgn_WuW6B39PxK3-b1znzG_1N1ci1H8tKp8RUbgMTI_31vLl_XEuHRXwwIQKtfwKXZHFfHC1zAOXTVZyNNCLh5-qiMPYjrdHFMQtHREGwq_VDbxOICwuAAd1LNccZo7g_M1m1-sZtBOJ8r9ETpxc9Q_R-V54uisVFbFGTsEYEL-e5ca5Xnxx19aWKCOcUWHLD4gaVTWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a26eaf0d.mp4?token=iLh2oHWgmTUraT1Sq6p5G1dnvexGybNeunRGF1PGVgjOiYTDKyKXwueZfB36U0hmHDb_UTZM7Kv5F25CNd5BrRTQNsGU20F0X8fsqQSSFBa4XMKqcMHeYG7_meeY4-jhfbu6kJ_2LEZP_ujfgn_WuW6B39PxK3-b1znzG_1N1ci1H8tKp8RUbgMTI_31vLl_XEuHRXwwIQKtfwKXZHFfHC1zAOXTVZyNNCLh5-qiMPYjrdHFMQtHREGwq_VDbxOICwuAAd1LNccZo7g_M1m1-sZtBOJ8r9ETpxc9Q_R-V54uisVFbFGTsEYEL-e5ca5Xnxx19aWKCOcUWHLD4gaVTWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اربعین، سفر همدلی و همراهی است
🔹
با رعایت نوبت، صبوری و همکاری با نیروهای خدمت‌رسان، می‌توانیم بازگشت زائران را سریع‌تر، منظم‌تر و ایمن‌تر کنیم.
🔹
چند دقیقه صبر، سهم شما در خدمت‌رسانی به میلیون‌ها زائر است.
↗️
ما را در
cheshmberahim.ir
دنبال کنید
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/677678" target="_blank">📅 13:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677676">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ba8b111b.mp4?token=sqWttwMtUIMmNK37_jtFmnjYu5XEqp5xsigB-8R4hTwCHwWYi2NvJR1VKdTHRVeJTFnPshlj0hd91U9_MeLcH0X0qr3Ga1zXUsnJ10lsf7eUcspf-ovFp3q4Um6g82AYHKx9Y8E9aIgxasqdCSOGODzfCsp3SXYc7M6B6ZcAcW8buL4GKOYmeU3bgysQz27VDOPhqV-kItL1lt7rt37x88VL51X18i6hlZ5qabOnO5OEFF0yucqjCEikZWI4ypE_7wKJrDW3zn1tGnVsh01bwEykKyuiW7ozSNwI2vTcoZPx3Ij5dcaa_RumLPwh8B6brDhdQ1Xe3_JeHMKR7hEfsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ba8b111b.mp4?token=sqWttwMtUIMmNK37_jtFmnjYu5XEqp5xsigB-8R4hTwCHwWYi2NvJR1VKdTHRVeJTFnPshlj0hd91U9_MeLcH0X0qr3Ga1zXUsnJ10lsf7eUcspf-ovFp3q4Um6g82AYHKx9Y8E9aIgxasqdCSOGODzfCsp3SXYc7M6B6ZcAcW8buL4GKOYmeU3bgysQz27VDOPhqV-kItL1lt7rt37x88VL51X18i6hlZ5qabOnO5OEFF0yucqjCEikZWI4ypE_7wKJrDW3zn1tGnVsh01bwEykKyuiW7ozSNwI2vTcoZPx3Ij5dcaa_RumLPwh8B6brDhdQ1Xe3_JeHMKR7hEfsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از شاهکار به یاد ماندنی اکبر عبدی در فیلم مادر
🔹
همه در پشت صحنه گریه کردند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/677676" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677675">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
فارس: طرح بازگشایی تنگه هرمز کذب است
🔹
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای، ادعاهای مطرح‌شده درباره موافقت ایران با بازگشایی تنگه هرمز را تکذیب کرد و گفت: «جمهوری اسلامی ایران هیچ توافقی درباره بازگشایی تنگه هرمز نداشته و اخبار منتشرشده در این باره کذب است.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/677675" target="_blank">📅 12:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677672">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=JgzbStbt7G-JxfHvzL_gDEw9gE-DFld2dy3RBlx86kZ7vlgr55XrxLtQgvY3AdGc1GxQk_t9IytTfh8pcesdxm_Nf36zfSO-Mv6d2q6EiD0lKgm-KuHavQ3WiXUj_BD5WLiZ_iEArTTJ18e0p2vZx89ccdcs2exkWU8oMfFzosZsBjuhRkZm0G_agePrv7uFueIf8D76wfnOCwHMs2HCo0wimXUQyV4pdF5rlHLFUcqErdFitHv2_B5Z5la7oYZwGH6_ZajlgobrtP564s3ayzjXMH8I58gN9bMz0dxVvEQF9kHaVWINOZuKAjjHGodxC8bPwh3i6a_6gEaGE5vpkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=JgzbStbt7G-JxfHvzL_gDEw9gE-DFld2dy3RBlx86kZ7vlgr55XrxLtQgvY3AdGc1GxQk_t9IytTfh8pcesdxm_Nf36zfSO-Mv6d2q6EiD0lKgm-KuHavQ3WiXUj_BD5WLiZ_iEArTTJ18e0p2vZx89ccdcs2exkWU8oMfFzosZsBjuhRkZm0G_agePrv7uFueIf8D76wfnOCwHMs2HCo0wimXUQyV4pdF5rlHLFUcqErdFitHv2_B5Z5la7oYZwGH6_ZajlgobrtP564s3ayzjXMH8I58gN9bMz0dxVvEQF9kHaVWINOZuKAjjHGodxC8bPwh3i6a_6gEaGE5vpkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«راویان پرچم سرخ» روایت اربعین را به شبکه سه می‌آورد
🔹
مستند «راویان پرچم سرخ» با محوریت سفر کاروان اهالی هنر و رسانه به پیاده‌روی اربعین، امروز روی آنتن شبکه سه سیما می‌رود.
🔹
این مستند امروز ساعت ۱۶:۳۰ پخش خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/677672" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677671">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تخلف در تصحیح اوراق امتحانات نهایی تکذیب شد
ابوالحسن مصطفوی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
هیچ تخلفی در روند تصحیح اوراق امتحانات نهایی صورت نگرفته و گزارش نشده است. بعضی تخلفات که در فضای مجازی اعلام شده شایعه است و صحت ندارد و اگر کسی مدعی چنین موضوعی است سند ارائه کند تا پیگیری کنیم.
🔹
سطح سوالات امتحان نهایی دانش‌آموزان استان‌های جنوبی هم‌سطح سایر دانش آموزان بود و تفاوتی وجود نداشت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/677671" target="_blank">📅 12:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677668">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eh_OVCDlTuxRpUSslM9Gl9SwTIXPLEtiYf77EnQIwszT0Z_SALI77K5g6VlGFbSy7fMXar2q4fzuA0oQhDxQS5WyAn6qwkWp2KaEyc_1iSGKbQC4YDJ7pYl9w_dbGa1oTJt_aWCLVamaTgxCduoGUlZC3m9EYbnm9MOeDtzcatBo0GxETyuH3zuSqZDr6R43v1KefkfyDtM2_87sc1ubnzEKBJDMuPzLT3HVRx_G5AmbU9iRgjf4I_m7WovfUyJixppZNY91GEjLh6oheIhF8Gk5jXUewGJOemoP8_iA10IYLrbChvb4w2BrkgehuYbGxcp2j_n82eNAGPB1T6bibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQe9eBW0UNpK9Yip9HlezMwrnmGSOJIZCFVidh-kLA_V4ZmIb7RxqJFnN9oSYX5JfVwashOef84sa4kqRzJs9INYZhX-GmFjxQ3ulRclnUm-zuc5Ew1tKp1O2In-LJEvqEMZfSpmqLPkLRdLxxVuJy-Ys9agKO-G3d9rcOxEjIhvV37e4DR3Vzzx4n0hn97d5mNxYijQbih6CqJrdmu7eXVZauPEbJr6PT1_xjgFR-XhpphfpIJQNRmM56sWZ6278hE0ewNqnPXqQXyXJZXsIzovZJ1keTtDZngwWLGftC7aRUAw2PHdVHoBPiSROgWKBdZf6jkArmWJ9bPLQvU1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VuFidJq4bYRveP0vJN8Tkomy-i97A-uLmp7CXvJ9vCSWLSrlkpp2VuWlARuML_sjF7xFK4E0EzsH10c0x2y_WTjMcIMZEjuMmzdxmy2Q-Mc0dI1_iunM8v4rAqqYhvgBQ4h9qaSMyIQxxyVpLDKbDGBw8Ab9U507JDQreWjQIXmn8BLgCfwSqQ_IPubm3ntdJZlG64t7BpUnyp7dOmZYCZIaLLUsEg11zOFjcTXtu-7-nOf-qO_6NY_8Nxy-XaXVPkH1d4qKzHJgDenOpY-IdRO0g_-Mognj5K_MzKckaH6vM5DTkx4RbT-l9H4PAuUbdy_l6hOjdtOwGAOy3vN0Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استایل خیابانی نوید محمدزاده خارج از ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/677668" target="_blank">📅 12:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677667">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
نیکزاد: افزایش قیمت بنزین منتفی است  نایب رئیس مجلس:
🔹
رئیس سازمان برنامه و بودجه درباره بنزین گفت که ۲ راه بیشتر وجود ندارد؛ یا سهمیه بنزین جابجا شود یا اینکه قیمت افزایش پیدا کند.
🔹
طبق توضیحات آقای پورمحمدی افزایش قیمت بنزین منتفی است و جابجایی سهمیه انجام…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/677667" target="_blank">📅 12:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677663">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgeNEhmMlDli--H1rr2mYyIBA3HDIQAdU-qViGYWKSSIQgNqpHR9l9tAQgbolL2OQf34g8hhDgbzMpsNfDJE2e_AM7V_Z9t5IDb4tgQqzj_Ue_LaLqIjZKkW3ErW8iRYp4k2dV1ser39YO_5YbTXvuM93xXVWMjjaKZOpG1WLybytI-lVAHEfi35tS6lPfd0c3Z_TnGhhIyGBJ9AF2Wg9ZIBMTTVvKgXjCY_S59nwm3IdyfXLFwjbHrtthbFV43oktodks6T0OtIAbQvzFr3QhTjDifi4Z1IlM5Aj5jV6Ma-NckaEhe4XFzcAw99Y6EIH7lbNotzad0X2ElpXFgeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه چرا مرکز آمازون در بحرین را هدف قرار داد؟
تسنیم:
این مرکز بخشی از زیرساخت رایانش ابری و پردازش داده‌های ارتش آمریکا بود که در تحلیل اطلاعات و پشتیبانی از فرماندهی و کنترل عملیات نقشداشت که هدف قرار دادن آن با هدف کاهش توان اطلاعاتی و عملیاتی آمریکا انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/677663" target="_blank">📅 12:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677662">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f578919b3a.mp4?token=Ow5QmyGijImp_hP0oq9UjXMkdHYwxBhEaknMQKmjmK7wuObSZKJdr3_WqAsBnw8Ug1QcgZu9fNHcHyLtT1x9wRs1SGak71nMan-Zjg5NXyW2kuyeieIpoaaOM5V9bvsFewQpZYwE-u73A2PR5dwrhvUcf_GPgKLzZUHFiRFNl_G_WVxaG75CZYm9r5zyYEvO3YixAdH9i3wOhF9tmu_egjTstzOQbxoxZKC_Zc7U1hYdu8NbObP2QWYSSeuOv_2JJ2Rv1bTfwRzQs-temEEdgX0wb8Di1k06DxnJousCSyBFmRxpMcDfbOvLce1Kpsat9cJk4blqVR9BIFYWEbms-IhlO15l53u-GB0YrTqv7lRhc_3pxPVoF61hOzuRQ14L9jds76L9DsHBj24GEhdqTWB9ckkBKj-NxScwXod5ArKF8L0j87eJN8nUrEDt8OCMLgmKEKSgU1yVslj68dgEI5ktsBF_P_14cSpjUGh25mw2CLTFUpm5yeDf_TFdiZQ7SpyWGywtxLEEJ2Dd0CqD3nkml8eGUN2aFZPoclkmUHBOklFS6qhg_kpr1hSPXhSKCgMVtWl1K3PwsONONjDIyRFCutf_wvCTJqaAVmJeDb2nUbGCJP4t9FmsBRh7iyDgMqseez3X_t5JiU2pw-qQ3aW5yTT-AeSdM_uPNVfOAIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f578919b3a.mp4?token=Ow5QmyGijImp_hP0oq9UjXMkdHYwxBhEaknMQKmjmK7wuObSZKJdr3_WqAsBnw8Ug1QcgZu9fNHcHyLtT1x9wRs1SGak71nMan-Zjg5NXyW2kuyeieIpoaaOM5V9bvsFewQpZYwE-u73A2PR5dwrhvUcf_GPgKLzZUHFiRFNl_G_WVxaG75CZYm9r5zyYEvO3YixAdH9i3wOhF9tmu_egjTstzOQbxoxZKC_Zc7U1hYdu8NbObP2QWYSSeuOv_2JJ2Rv1bTfwRzQs-temEEdgX0wb8Di1k06DxnJousCSyBFmRxpMcDfbOvLce1Kpsat9cJk4blqVR9BIFYWEbms-IhlO15l53u-GB0YrTqv7lRhc_3pxPVoF61hOzuRQ14L9jds76L9DsHBj24GEhdqTWB9ckkBKj-NxScwXod5ArKF8L0j87eJN8nUrEDt8OCMLgmKEKSgU1yVslj68dgEI5ktsBF_P_14cSpjUGh25mw2CLTFUpm5yeDf_TFdiZQ7SpyWGywtxLEEJ2Dd0CqD3nkml8eGUN2aFZPoclkmUHBOklFS6qhg_kpr1hSPXhSKCgMVtWl1K3PwsONONjDIyRFCutf_wvCTJqaAVmJeDb2nUbGCJP4t9FmsBRh7iyDgMqseez3X_t5JiU2pw-qQ3aW5yTT-AeSdM_uPNVfOAIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم در مورد قاچاق برق چه می‌گویند و برق‌آشام‌ها چه کسانی هستند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/677662" target="_blank">📅 12:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677658">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf0ccaf39.mp4?token=UH_GXNTc440gForAZCxf9KZUQDG07zy54whReIu1A4haNNFDPacCfcdv0T0hLeHSPi7S_pO9KoD2vlatHXdWR2XdJNCzK4Xf_CtU7HVDp7S9q1HFEhSMe5a3kKd7gMO0Qw2gJJRcKxyzLWtnDwN9te6FuUsQP8fm_PnyOZgum1DJP-jdGNFPzUpY7J4eWaqfrJ6VKGL1L3mxSRZN06kcJ_cPJ_bBxG_ouSa_0wU_TJTL8iymNAQEHfT4xaoiXUgOnCifXzrmE07WOf4mHdLtFhqJziC1klAWQwDY9NrXzwZK2jglxLCK7UTe_74NNRJWaihI94XdeVPzoA7g6-htj2hoAgFtrpzUZk7r72D0LNR2Vo9B-tLSUbCdsZ19jfH5DhHaJLMXG_d_tshBfxEvcVGkrcEsdNITYTfld6jSb-S5BOtXN7zQUzVuIBmcLhDyY-fGlqyApn4p687Xgv9628e46Ck7VUYUzNrwYDxuhOqsBpqVsW-2XOzvHhC8uX7CnMa987b6HgOZ8SyLBSRgeIFWEj_fN9owLvxjQCPKPVfd7IFvMykMhg86aMdyJ2eWcxxnvNHtG6NWBEhFx--4GyC-dEpInANDH8q482H2MU9Cly-gPklev1nd1uS7LCXjEr7lWDpDt5n6H_rnDXZqmJpGf3_9g93j2fUH-aNBStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf0ccaf39.mp4?token=UH_GXNTc440gForAZCxf9KZUQDG07zy54whReIu1A4haNNFDPacCfcdv0T0hLeHSPi7S_pO9KoD2vlatHXdWR2XdJNCzK4Xf_CtU7HVDp7S9q1HFEhSMe5a3kKd7gMO0Qw2gJJRcKxyzLWtnDwN9te6FuUsQP8fm_PnyOZgum1DJP-jdGNFPzUpY7J4eWaqfrJ6VKGL1L3mxSRZN06kcJ_cPJ_bBxG_ouSa_0wU_TJTL8iymNAQEHfT4xaoiXUgOnCifXzrmE07WOf4mHdLtFhqJziC1klAWQwDY9NrXzwZK2jglxLCK7UTe_74NNRJWaihI94XdeVPzoA7g6-htj2hoAgFtrpzUZk7r72D0LNR2Vo9B-tLSUbCdsZ19jfH5DhHaJLMXG_d_tshBfxEvcVGkrcEsdNITYTfld6jSb-S5BOtXN7zQUzVuIBmcLhDyY-fGlqyApn4p687Xgv9628e46Ck7VUYUzNrwYDxuhOqsBpqVsW-2XOzvHhC8uX7CnMa987b6HgOZ8SyLBSRgeIFWEj_fN9owLvxjQCPKPVfd7IFvMykMhg86aMdyJ2eWcxxnvNHtG6NWBEhFx--4GyC-dEpInANDH8q482H2MU9Cly-gPklev1nd1uS7LCXjEr7lWDpDt5n6H_rnDXZqmJpGf3_9g93j2fUH-aNBStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عقاب آسیا هنوز آماده است؛ نمایش آمادگی بدنی عابدزاده در ۶۰ سالگی
🔹
احمدرضا عابدزاده، دروازه‌بان سابق و محبوب تیم ملی ایران، همچنان و در ۶۰ سالگی نیز از آمادگی بدنی برخوردار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/677658" target="_blank">📅 12:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677657">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX6G1eqQ_nGut_hWrwqGH_OoMQymOQBMVLAPgjtCYb0RswBVsF0TM_P0Fulud-bVrF1PiGchn-gF_VdS4vI7MpoTqVw8WotwpK-fKxsXr7kle3a9vphtQJsGEmwO8FqPW3GpmYCkEd2uaIFfmI24chfAVwyt4p6iqjNd9_BCpuPN-xRrB0yqB0PdKgib7WnCmge1f-pQAhRYoaYTjERi-GBDRMvvjYB5jaLM6IZ1cNfpPpbLrUUdZofSScp3CGxDBIK18PgfyGyTW_rFbBijKv22Lm-Bnm6mMJAnA-3k--8Cu_B7q1SF8Up9A8FQ4ZnIQOLiko4SpVWF3LF-JwRHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور روانشناس زرد رو از روانشناس حرفه‌ای تشخیص بدیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/677657" target="_blank">📅 12:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677655">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144ba700bd.mp4?token=mARAa3Nm8NYYboqp1-mypnZ3D_ThmrqMPh5OO7xEHQyBaN3qV6dH1IhZN_LZKQrIM0PE_xA7aWUbCgQ73f-rl1q7a7N3mtpI28Vy9H0UtqtJVVBJ4qt24jR3k0k9MIMdSP8tI4KkqWVk0orVXwizjOJpk4M_m2UwqMfC2oex2Lgdfa3b9ge57KVoUHhDkwBkutdDcaeASDTMjK78RTLhHU1REbW8rTKRIp9bxL2uWp8VS9_AfbT2UknWlTZ2TgD1aoGrQYEwsVB2mG7tZLv3KNY0FmpmJzt2K2etBTlHyZP1dQCTwxmHC4-lH3bRA8azewyY5nGY-kiYdWLAe4uO8Wc7tlkQwakiRZyouA2GWAtiiyDv4h1Ol7sDTCPtjkgrCUS0VeT-h9zuj4rncd76ttvMeAjGHV-BUF1jgKE-UcS6c-18xGjQHBi7PQBcH4h1364LUtxvNHs_mkfaDtMkx-HRt60y_vEAF6QzHJ4L9nXYrA0wEl8ySO7J0nRq9dKOspK2XUO5cNryh9tYgvBKrW7IpxwGBrXiLtQE8F9EgA_HvcvsSammV9MHzJGGY_qEbYtuTAVpU8WQneFdctR1p_y519fvFzycTUfzIcSMfLrUX4o9ktmfb-upL8S9iQZcEFCOFUyAVEqvvNTDOnrWSnMNRN_Pn4laW1DCKTfjHlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144ba700bd.mp4?token=mARAa3Nm8NYYboqp1-mypnZ3D_ThmrqMPh5OO7xEHQyBaN3qV6dH1IhZN_LZKQrIM0PE_xA7aWUbCgQ73f-rl1q7a7N3mtpI28Vy9H0UtqtJVVBJ4qt24jR3k0k9MIMdSP8tI4KkqWVk0orVXwizjOJpk4M_m2UwqMfC2oex2Lgdfa3b9ge57KVoUHhDkwBkutdDcaeASDTMjK78RTLhHU1REbW8rTKRIp9bxL2uWp8VS9_AfbT2UknWlTZ2TgD1aoGrQYEwsVB2mG7tZLv3KNY0FmpmJzt2K2etBTlHyZP1dQCTwxmHC4-lH3bRA8azewyY5nGY-kiYdWLAe4uO8Wc7tlkQwakiRZyouA2GWAtiiyDv4h1Ol7sDTCPtjkgrCUS0VeT-h9zuj4rncd76ttvMeAjGHV-BUF1jgKE-UcS6c-18xGjQHBi7PQBcH4h1364LUtxvNHs_mkfaDtMkx-HRt60y_vEAF6QzHJ4L9nXYrA0wEl8ySO7J0nRq9dKOspK2XUO5cNryh9tYgvBKrW7IpxwGBrXiLtQE8F9EgA_HvcvsSammV9MHzJGGY_qEbYtuTAVpU8WQneFdctR1p_y519fvFzycTUfzIcSMfLrUX4o9ktmfb-upL8S9iQZcEFCOFUyAVEqvvNTDOnrWSnMNRN_Pn4laW1DCKTfjHlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: همه ۸۰ میلیون ایرانی حزب‌اللهی نیستند/ خانمی در صداوسیما گفت مملکت متعلق به حزب‌اللهی‌هاست و هر کس ناراحت است برود، در پاسخ به او گفتم شاه هم همین حرف‌ها را زد
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
در مصاحبه‌ای گفتم گروهی در کشور حزب‌اللهی هستند و ایثارگر هم هستند طوری‌که به حال برخی از اینها غبطه می‌خورم.
🔹
در حال حاضر دشمن وظیفه خودش می‌داند که جمعیت منسجم ایران را به تکه‌های متعدد تبدیل کند؛ حزب‌اللهی، نیمه حزب‌اللهی، بی تفاوت و....
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/677655" target="_blank">📅 11:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677652">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDZ6-PQnU-iACsSh9CauTbFCyrweIA46JWqY9Cc7NcdyP0BjtxFvkZobZPDO2fZQhH0B5sV8aZWu7uJ6Obm0zw6KOmxsSxpmgEKdefT7GPAHhjdDMZ3i_VbKxp29_4K9rz8SMySlhwFBs1dF9dkNEcpYeq8F_pdE7ZMjm7JuaYbqH6hzpmC5onVxcQh7t7HU_-7d7hJdMLE1rWRGDCoPYvGXGiL1LVNfCZwYf5JA-wIf6JKECpfDRzVFKLaiUnwQbybNJ0NhbUdq7f1voXumyrB3nHRXCe71ryiHzUcOhM0V4KTeLwdufjJnt3A_V6_-MCsZYcuHSpBGRCjDmybTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArXwAYkMwtEV2x6sbTdMjmySEXkIyoHBA4WcZ_h9hWpwrfObYiGELJIaLfsOGegruE3o9Ipxh-G0nMh5lpoRiIOLK-Hgzln7RMlDLsyHCQXCMTQMEXAf3Z2X28AUMqs9Is3ROFBUuCaoMOEyfY5m3Hh_zKAEEglCFfHxDC6MhiuuBLokmCSo293vq2VA_UZ2Ip3Y3bw_nlB5zob6hhEItd5xg3NGsMw7x59yfMx8_N1CylFK5uHJr4w-EZlfJ-Tg3CizVBI9dlmg24udEmSqiCsU3PnzwbaEgluPynL2dWR73F1gMXFmhDAXvecQRJHnNR8USIeO8RnJve__UKtQDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
امیر جدیدی، بازیگر سینما عضو تیم ملی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/677652" target="_blank">📅 11:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677651">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4c2PYLge7xxLrAIsPz6i004ykNF_mgGJOSz4dp-3W-pZfCCTBJtGm8AvKAkwAe86fpz4MEfWKhML4mKRO5jJsP6X8i6905eVGEOzjYJBtp7IHspUxF1Bg4Kji2E14Xh9-Fw37T47Qy3td28RGz_UNngOTJnFHfVqcxTVUfHXOVJkTclmG_G4MBEdrAwukXQ6NW1YzLYrqmt5NuIhU-acj4mqPrfDmL--HC_2a_J-EpR5hYqqxSJlesNS7POc_7oLoOf2nRP4iCjP_HNHTBVXY3490OOpeyrCAxeMYQOajjN_VLxNIIVCvTo82DXr84hZMIFmLp9veoHaBGFPZRDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۱۱ مرداد ماه
🔹
در بازار طلای امروز با کاهش قیمتی نامحسوس روبه‌رو بودیم.
🔹
قیمت‌های اعلام‌ شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/677651" target="_blank">📅 11:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677648">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61093b3671.mp4?token=SSjZCh-lxgd0i9W6kTa9ZFJ0EZD9EVPd-_0uhy8faY23fWoXSI0ZUsK9sb4VdBJnyETKEP0aG2wwqrBCr-dtH9jbuPd5Wg9R-V0VTBz-2c5pqeeSlprYEVwXfa9e63ZVHNaLsPUhwxT8mQW-4ovdOCTJik7MvP1ZKYZWmhEheSDamKgJwfNb-cuzJpGeBoj6cndocz84_kaMHIRuMOUkBB7V-2UjAJBLyvQ6au-bHsnllp-fQnH-0-UG8o1xA4OT_yEMc_foBnlXm777HmUkSFr-OsH7cvAHcOkrutfBWVSPFFtJv015B21TQ_V8KMAqxkfpqfrH7wGUwpPvLT1IuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61093b3671.mp4?token=SSjZCh-lxgd0i9W6kTa9ZFJ0EZD9EVPd-_0uhy8faY23fWoXSI0ZUsK9sb4VdBJnyETKEP0aG2wwqrBCr-dtH9jbuPd5Wg9R-V0VTBz-2c5pqeeSlprYEVwXfa9e63ZVHNaLsPUhwxT8mQW-4ovdOCTJik7MvP1ZKYZWmhEheSDamKgJwfNb-cuzJpGeBoj6cndocz84_kaMHIRuMOUkBB7V-2UjAJBLyvQ6au-bHsnllp-fQnH-0-UG8o1xA4OT_yEMc_foBnlXm777HmUkSFr-OsH7cvAHcOkrutfBWVSPFFtJv015B21TQ_V8KMAqxkfpqfrH7wGUwpPvLT1IuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
🧹
خودروی همیشه تمیز، بدون ذره ای گرد و غبار!
جارو شارژی خودرو  با مکش قدرتمند ۴۵۰۰Pa و ۲۰–۲۵ دقیقه کارکرد مداوم
کم‌حجم، سبک و قابل شارژ با USB — همیشه همراهت، همیشه آماده!
⚡️
🧼
از صندلی تا کنسول، از زیر پا تا گوشه‌های دست‌نیافتنی…
همه‌جا رو در چند دقیقه برق بنداز!
🤩
🌟
قیمت اصلی: 1,598,000 تومان
🔥
قیمت ویژه فقط برای امروز: فقط 1,089,000 تومان
🔥
🏠
پرداخت درب منزل
خرید
👇
memarket24.ir/dirmob/180124/g-en26903</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/677648" target="_blank">📅 11:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677647">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2vG27lZoel2nfZLdoTcZtcGfkyYxIUnN7p-e4AI7KT0vo1ItJeid5wxtpamg2q1lUZ3W7O25d7CddgXI4leFiAtSJgDHl6N0oW8u6i1bx4UEBPBp0MjayoOFSGnEBvy_xco8qf2VnNl8RLn2B2X6wL1icI6cepFqOmMS91vbBxGEryBqV_TxtaC0gjI2OzpV-IbJAywF5R3WhVk9AlSSHaFy0Po9MYHPaM5ZXgcqgrUjk29gz2YEa7_ET8BmUHNek166nALFoSibBlCaOkeSkJ6KKXgi8L8Dwgva-nBP1WSuc9dV9BRjIpZveDfSzLKNipaK7XVhnS1XhMsOOgAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باراک راوید: اعلام لغو حمله توسط ترامپ بار دیگر نشان داد توانایی نتانیاهو برای نفوذ بر رئیس جمهور آمریکا خیلی کاهش یافته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/677647" target="_blank">📅 11:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae21676b1d.mp4?token=USIFFHtPsPyZdKt-hkkWBBg29bfiLoqtdfK6vyFXGp3asd39QEIq_RaUNzqusaQ6nPzqBkyFlLujlylJlCKWQZ6KtDNzUGh3FMU5C8-eJFuUL-wPUwiASwZlhoR8Er7jWizlSFCABzxqr-dQ05Rufa7ZjRUuDPYCwWgzxIDreu8cW2z_9CgeQheluZo5ZQMUOx1sLelKkqIHz6HafKEBCGyOVFeMH7msJfjcahsjOx_ty8bMaOvOK_vn0XC04F53Je5gm5iehDF936Mj4LcypOf6OpmxYoLByAC3nlYsbWaytBjJzcAFg94hq6C-YVBbAvOs2-NpEufr8UOlkIJgSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae21676b1d.mp4?token=USIFFHtPsPyZdKt-hkkWBBg29bfiLoqtdfK6vyFXGp3asd39QEIq_RaUNzqusaQ6nPzqBkyFlLujlylJlCKWQZ6KtDNzUGh3FMU5C8-eJFuUL-wPUwiASwZlhoR8Er7jWizlSFCABzxqr-dQ05Rufa7ZjRUuDPYCwWgzxIDreu8cW2z_9CgeQheluZo5ZQMUOx1sLelKkqIHz6HafKEBCGyOVFeMH7msJfjcahsjOx_ty8bMaOvOK_vn0XC04F53Je5gm5iehDF936Mj4LcypOf6OpmxYoLByAC3nlYsbWaytBjJzcAFg94hq6C-YVBbAvOs2-NpEufr8UOlkIJgSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فلامینگوها در خلیج گرگان
🦩
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/677643" target="_blank">📅 11:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677642">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBAQPHwSnFftNbVl-Q0CA2oEpse_Pn6__ae4gfYCiGTvcgFXIfQZ05jvLcJ1KHl3fWxbW98H3_Z1Z8RRDHMEzvBRGjEeBgcvXrRXw7uGzlImAXp-vlqUhv17nc_n8sVgYD--LJPXM9T6GIV1rQmvvN1aY3U-T2jPtsOMmAci8WcLVpCy5Y-xhUX66FSXGGy4Tk4sv1GhJ9HpH5zOvdDAFluA3lu8cBUPhx-uJWAFhJ2qXDxMFpCrxtLFE-V7S0cRfKLJTbwM4I-3ZuE15FjApGg-APacH6CLDUk3q1nsp9BBYnjOgJMXurb1HfY7TP_YW1ZLitj5J1hG_Bj8Ld1VhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بشرا شیخ: برای واشنگتن در ایران کار تمام شده است
🔹
آمریکا به موشک‌های پاتریوت و تاد نیاز دارد.
🔹
اوکراین به پاتریوت‌ و تادهای آمریکا نیاز دارد.
🔹
اسرائیل به پاتریوت‌ و تاد آمریکا نیاز دارد.
🔹
عربستان به پاتریوت‌ و تاد آمریکا نیاز دارد.
🔹
قطر، کویت، بحرین و امارات…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/677642" target="_blank">📅 11:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677640">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
هشدار پلیس فتا درباره رسیدهای جعلی در معاملات آنلاین
پلیس فتا فراجا:
🔹
فروشندگان در معاملات آنلاین، صرفاً به تصویر رسید بانکی اعتماد نکنند؛ ملاک، واریز قطعی وجه به حساب است.
🔹
به ادعای انتقال وجه از طریق شبا و واریز در ساعات آینده نیز اعتماد نکنید و تا دریافت وجه، کالا را تحویل ندهید.
🔹
موارد مشکوک  را به شماره ۰۹۶۳۸۰ گزارش دهید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/677640" target="_blank">📅 11:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677637">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_3B8jorWHIyqxuTK3ycg9dkLIXK91vALS0GK2v7umxaw4DKUQYtJ1l9H4iNvXgrGzw1MIsW-ggPz_WLVadlWUlXVTrCxQ_80FL3SDFCzmLFBsbJyifk43-BFJt8fzUJKYYqZ9MvUuzx41g6own_TXne2hHdNnR5a7GoPDMMG7qb3sC0OwgREhWgH0C_H_sMNj3o0ZwtfSGgk9eIAHw07GgTlWARKq47PIVLHxgUCWwdrm5usJH4augTdT4ygs0_bCo-OWsILJ97qtyaEGDA_vZMOXmmKcwqWWYOuCT3804o4wb53ZoZKyA6R0plWwjQvYyDYStsJx_hQdTV_HORiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر مسائل دفاعی و امنیت ملی آمریکایی: واضح است که در ظاهر، این ادعا که ایران با رئیس‌جمهور ترامپ تماس گرفته، از او خواسته حمله نکند خنده‌دار است
🔹
سرانجام بخش کافی از هشدارهای نظامیان به رئیس‌جمهور منتقل شد که اگر این حمله را انجام می‌داد، برای آمریکا…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/677637" target="_blank">📅 11:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677636">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ابهت و زیبایی حیرت‌انگیز در خودروهای BMW موج می‌زند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/677636" target="_blank">📅 11:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677635">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdFPPJH9edNsXXsnHIA2avF-pF4B8hLgU54ACrgOqykrIV5K7UWW4grPdRXXMOsM7nbwLei7Gx202P33vJZ7frMSa2whzMhnsbaKzE6jD-q0D37sq0TMyl_pzou77C5m0NcLrdhN78iT-30vY4RgGhabo4JAYusIq_mrDk4j4H0iXx1WhLL4IgHJV-aOWm7oiwVQId6-4udt1FP9Fcijt0jlF-Mj5ggDryVoRcFEoIoKYq1CBg4oa09MJbeivFhkpP2V2vQez2dKy3HSEqcjDGs4bXIE5SwXX0zW4QWlKqqc176mUp1tBEh80ytYTPfKAX1fHjKZduQI1W3gG851wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر مسائل دفاعی و امنیت ملی آمریکایی: واضح است که در ظاهر، این ادعا که ایران با رئیس‌جمهور ترامپ تماس گرفته، از او خواسته حمله نکند خنده‌دار است
🔹
سرانجام بخش کافی از هشدارهای نظامیان به رئیس‌جمهور منتقل شد که اگر این حمله را انجام می‌داد، برای آمریکا یک فاجعه تمام‌عیار به بار می‌آورد
🔹
او کار عاقلانه و درست را انجام داد و دستور حمله را لغو کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/677635" target="_blank">📅 11:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677630">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf768c0fb.mp4?token=RFeJDkJsg797jdG6IbAlPDV_RapjrQSb6czCxgnD5ZN4RgMEtc_a4LZuJ69nCnSM1wO3CUsCbgzR0h4JZh0yAKQWL_tg0gpIKJHNsD82LTF2giLhUK5Sp4q_ivNgGQZM0F5gSkT4DtyUHZoddsR5vV7ppEptpJu6Gp8yYgy-Ek1BTz4HgpmuBx0isFc3735S364C4-t-2GaKj9uaxb7ZWgZ4NcQj2AwcNqUxUW7FjgvVQsKEFzGmDpUANtSmMMMvKbC31TvdZB44mX6WSlrllz7RxXECqda31GvyouzYA7s_GgswSfKyCotJ1Qm42GTDH45YHvBFSETlzqxAjnmksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf768c0fb.mp4?token=RFeJDkJsg797jdG6IbAlPDV_RapjrQSb6czCxgnD5ZN4RgMEtc_a4LZuJ69nCnSM1wO3CUsCbgzR0h4JZh0yAKQWL_tg0gpIKJHNsD82LTF2giLhUK5Sp4q_ivNgGQZM0F5gSkT4DtyUHZoddsR5vV7ppEptpJu6Gp8yYgy-Ek1BTz4HgpmuBx0isFc3735S364C4-t-2GaKj9uaxb7ZWgZ4NcQj2AwcNqUxUW7FjgvVQsKEFzGmDpUANtSmMMMvKbC31TvdZB44mX6WSlrllz7RxXECqda31GvyouzYA7s_GgswSfKyCotJ1Qm42GTDH45YHvBFSETlzqxAjnmksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوقلوهای تازه متولد شده همدیگر را در آغوش گرفتن و می‌بوسن
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/677630" target="_blank">📅 10:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677622">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqR4NxGG7VW3ig8QoFfuGWenwUV_hcrqWBvKVwI7LC6azEipuseqNEpt25jravMhLbvkayFFvIO7LA5arUewdICleL3EPf7yDIEe2dOeGmVMQ-EyBrKglmP3vzhq4MJ_gfuBhsb_KU_T3cp5ViGn07veoCwp4lYJIIlhUgWD3F_7G_XrGGJ3dPTeO2bSBOtfzccs3Bk-i_5YoFtnAWZN3LmxXzXFAfbVC1hzDr1gC0JwM6N1MD1jtkuNpYGFXsLpCZsK8QpsbIDEvW3oQnfKRfcn6IfstriTZDX57ZzyRi7eCn9Vq69ot8RQQRPJq-8FGcVlX_9tXWdduCrcEnVGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشانه‌های افرادی که از لحاظ عاطفی برای شما مناسب هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/677622" target="_blank">📅 10:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677621">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
چرا از رهبر سوم هیچ صدایی در رسانه منتشر نمی‌شود؟
همشهری:
🔹
هر فایل صوتی لایه‌های پنهانی دارد که سرویس‌های اطلاعاتی می‌توانند از آن ابعاد فیزیکی، جغرافیایی، زمانی، سخت افزاری و زیستی گوینده را استخراج کنند.
🔹
آکوستیک محیطی و هندسه اتاق:
هر فضای بسته امضای صوتی منحصربه‌فردی دارد. با محاسبه زمانی که انرژی صدا پس از قطع منبع ۶۰ دسی‌بل افت می‌کند، حجم تقریبی اتاق تخمین زده می‌شود.
🔹
تحلیل فرکانس شبکه برق
: سرویس‌های اطلاعاتی با تطبیق نوسان‌ها با پایگاه داده لحظه‌ای کشورها، تاریخ، دقیق ساعت و حتی بخش خاصی از شبکه برق محل ضبط را ردیابی می‌کنند.
🔹
طیف‌نگاری و امضای سخت‌افزاری دستگاه
: میکروفون گوشی‌های همراه فرکانس‌های بم را تضعیف می‌کنند و قطعات ارزان‌قیمت اعوجاج هارمونیک خاصی ایجاد می‌کنند که مثل اثر انگشت دستگاه عمل می‌کند.
🔹
نویزهای پس‌زمینه:
صدای سیستم‌های تهویه، ژنراتورها یا تجهیزات خنک‌کننده مشخصات فنی محل را فاش می‌کنند.
🔹
زیست‌سنجی صوتی:
رزونانس‌های مجرای صوتی یا فرکانس‌های فورمانت ابعاد فیزیکی نای، دهان و بینی را نشان می‌دهند. الگوی تنفس و وقفه‌های میان کلام هم وضعیت جسمانی، ضربان قلب و میزان استرس گوینده را مشخص می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/677621" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677618">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjOYVfuGT5Uu6P4Lu7az-ZzOwKt2mIqFhFONA1Ilnm_XJwXMyzV7dCWderhN1ysTAAJ10rD0wonkZl0j9TKMuBs1eQPM39vQXHB-n-U6mwQcr5QmnjlQOGU25K_N1RQ3i_ChZz0nv1i5ofgKrJKdvsCevZ5uNMoK_7hNQbMRjCANAe264qk9loacx4I1mlLNvYxwic6Y2nGE4ynvphjb4m8yxJVOKvvnFlVWpSkxLIV865gHrZMciGvBbQc5olEsyFcrQne38Y1rXE-gPLm0_qs5EAjkAxJDcjXJADePle2W1616oPFcSc47XTFaUpaSJqvg-SW1ZdmPu036euMUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: آمریکا با بمب ۲ هزار پوندی خانه‌ای در قشم را هدف قرار داد
🔹
نیویورک‌تایمز با استناد به تصاویر، ویدئوها و بررسی کارشناسان مدعی شد آمریکا در حمله به جزیره قشم از بمب ۲ هزار پوندی «مارک-۸۴» استفاده کرده است؛ حمله‌ای که به گفته مقام‌های ایرانی،…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/677618" target="_blank">📅 10:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677617">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecSn1HbBS5Tz1YPer59PvFykwBcdj2-HvvHNE_LVXw1w9tPBHLdakcbh_p-UvrehhBXDfVdgAkhrAdC5HWjSFFTI__aT_emPbQuPk48C2FarbxiRJcx6PUtQr9-hYValExhh3J-Ii7CC5So3Xo3ywsVXZ1Ysk_0jZa2luygR9Og1J1_IT0La8bDa6qkusQ1PHzatzreXOVreCbkVR1h3Tnz3tYfpg-xHSpHYt-OrN1yL8b0lz4YgSxWxvbrYhj7fabefnBZOMaqbaCx82Wc0RCmyN37YInEWNBruSoQKAdSd-hD8C3QWRYaYNYKHswrdm3kGcoc9AGqLKurTYPeKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امور داخلی کشور: مدیریت شهری برای مردمی سازی خدمت رسانی به زائران اربعین گام خوبی برداشت
رئیس کمیسیون امور داخلی کشور و شوراها در مجلس:
🔹
در طول سال های اخیر اقدامات خوبی برای بهره گیری از ظرفیت های مردمی در برگزاری این مراسم انجام شده است. مدیریت شهری نیز گام های خوبی در فعال سازی و به کار گیری از این ظرفیت ها داشته است.
🔹
همچنین درباره اقدامات فرهنگی انجام‌ شده از سوی شهرداری تهران با طراحی شعار « یا لثارات الحسین» و نهادهای مختلف برای خنثی‌سازی فضاسازی دشمن علیه مراسم اربعین گفت: تبلیغات امروز اهمیت زیادی دارد. دشمن به دنبال عملیات روانی، شکستن روحیه مردم، ایجاد دوقطبی در جامعه، بر هم زدن وحدت و یکپارچگی جامعه است. رهبر معظم انقلاب اسلامی نیز همواره بر حفظ وحدت و هوشیاری در برابر جنگ روانی، جنگ شناختی و جنگ ادراکی دشمن تاکید کرده‌اند. از طرف دیگر اقدام مدیریت شهری برای مردمی سازی خدمت رسانی به زائران اربعین گام بسیار مهم و تاثیر گذاری است/ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/677617" target="_blank">📅 10:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677613">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/442feeb9ec.mp4?token=UOhs_aYK-qxBcRx2Fh-tJjTLKasWGYKue4u5OcKB1L8vvk22JoHJCjvmamkQO4_DPhZmL8bL111x_RIaZ0Uv2idmRxA62krXyyvG4usCjHefPrSL5gxk1zErym50CQ8Gz1VS48p3KGkyLE86e5nHf4t4qR_TiIdAB-am_kmOfxoy9xvlAYisI4a7ztOdw0kBNEWIZRETAmO5w0_Hs5BNXSS03By5PqVxTZSamj9pBjjIOk2EEuMiDEyB87P8JSYGZVCnS_k1sbbxhOMJHLqp-tjjw5AociGn_nGyMr4B64RWbAAULq2gXoDGETEbbhqwY_Y86CJaYbVhQkN6YwM8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/442feeb9ec.mp4?token=UOhs_aYK-qxBcRx2Fh-tJjTLKasWGYKue4u5OcKB1L8vvk22JoHJCjvmamkQO4_DPhZmL8bL111x_RIaZ0Uv2idmRxA62krXyyvG4usCjHefPrSL5gxk1zErym50CQ8Gz1VS48p3KGkyLE86e5nHf4t4qR_TiIdAB-am_kmOfxoy9xvlAYisI4a7ztOdw0kBNEWIZRETAmO5w0_Hs5BNXSS03By5PqVxTZSamj9pBjjIOk2EEuMiDEyB87P8JSYGZVCnS_k1sbbxhOMJHLqp-tjjw5AociGn_nGyMr4B64RWbAAULq2gXoDGETEbbhqwY_Y86CJaYbVhQkN6YwM8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی قابل تأمل از دختری ۱۹ ساله که در این سن دهمین عمل زیبایی خود را انجام می‌دهد...
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/677613" target="_blank">📅 10:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc59a098af.mp4?token=h8uMvmtKORwowrtqn8ueq994zcuq261nEpniqtW9b4666BksiL9P4M0o81aDngp2JycyC6r9BImIeDQluCCV6VSix8a7iuaRjBB0YH7yGuP1U-KpR7joE_A7BOUY3w9wo90hJywxyEy7mpxpZxFmMHPjn8eO4-4CR3ndk5-joPu6TXHWiXVjRR36XPxFzZZ5iWpcpFz-TzEbxAFLwqAhUgDjza5dbynMTPZjzEz02OmqvDZDfb_uuWMOeDb1u6JV6DomP6aES9LwGbhy1CIM_0ifLm3phKIuN9Iv5h9VHgJuXCc-leiiUyBjQzavZ_aKtuAwWxShavqZCwMzCxsk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc59a098af.mp4?token=h8uMvmtKORwowrtqn8ueq994zcuq261nEpniqtW9b4666BksiL9P4M0o81aDngp2JycyC6r9BImIeDQluCCV6VSix8a7iuaRjBB0YH7yGuP1U-KpR7joE_A7BOUY3w9wo90hJywxyEy7mpxpZxFmMHPjn8eO4-4CR3ndk5-joPu6TXHWiXVjRR36XPxFzZZ5iWpcpFz-TzEbxAFLwqAhUgDjza5dbynMTPZjzEz02OmqvDZDfb_uuWMOeDb1u6JV6DomP6aES9LwGbhy1CIM_0ifLm3phKIuN9Iv5h9VHgJuXCc-leiiUyBjQzavZ_aKtuAwWxShavqZCwMzCxsk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به سبک انیمشین درون و بیرون، برای بچه‌ها غلات صبحانه شیر و میوه آماده کنید  مواد لازم:
🔹
یک پیمانه غلات صبحانه دلخواه
🔹
یک پیمانه شیر
🔹
نصف پیمانه میوه تازه
🔹
یک قاشق عسل
🔹
یک قاشق غذاخوری مغز #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/677612" target="_blank">📅 10:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e17b7771b.mp4?token=oAZdoPBsww5CtDUz0rJMkPVZ5MHY4fc0N5hLZFp0ngtKZ9PZg9QIsOBS2ZcR4ib38opB-KTbEVMgTFkx0w4NwH_QM0BGoq2XUvXdwf-_ov2sPEyk6Yar-DHd4YP00PSpXsQc1MyI7RaccV5YaTRmqPY3RTI1SZocfWvPHdYxcdbYb8xDJrVJK1glWjJbkzk8bNpomteCgr-IrJ5nUbX8FRM17y1igdDXrm1KZC8i1QTXHb2rXAL7s3UF4dABmcGsJJsDhDX4AVLx6ui939UXRhK2L-GTJZ60uVK8B5RgNSHZ3zagPqps_gHGjMY3luoOH6VZ9IV2GCmkW2TaIcnXALg5Nd-IS8Bd5x3786-VF2d6o3L4eXq6qwZVrtOgscJDOxuIra0TStRFPviWSzkldhMWF1gpoVPcjD5y5leMuxxhhO2L-YgWvmZ1FCN872mdSCAom7_yTA9LVRz9ZQC3a5zWdYGDA1nui40LQMs-zXnIwUmrG4RjxmG_-vWVgM4hF0Y8I8xKcA7i6_AYABakTc0RsgO4LvvpKSN9Vvuw_Uhndf7VNcRLGvveT-axwBtwCr5eLirj2ngiAGzRZveH_jthVVI9aI-fdcwwiBJF7UnGabngNSWrOFJ92u6yhh1cd1orC1nk8bPvPDodEibLpZePzaLqbbQ0BLAckuWCtkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e17b7771b.mp4?token=oAZdoPBsww5CtDUz0rJMkPVZ5MHY4fc0N5hLZFp0ngtKZ9PZg9QIsOBS2ZcR4ib38opB-KTbEVMgTFkx0w4NwH_QM0BGoq2XUvXdwf-_ov2sPEyk6Yar-DHd4YP00PSpXsQc1MyI7RaccV5YaTRmqPY3RTI1SZocfWvPHdYxcdbYb8xDJrVJK1glWjJbkzk8bNpomteCgr-IrJ5nUbX8FRM17y1igdDXrm1KZC8i1QTXHb2rXAL7s3UF4dABmcGsJJsDhDX4AVLx6ui939UXRhK2L-GTJZ60uVK8B5RgNSHZ3zagPqps_gHGjMY3luoOH6VZ9IV2GCmkW2TaIcnXALg5Nd-IS8Bd5x3786-VF2d6o3L4eXq6qwZVrtOgscJDOxuIra0TStRFPviWSzkldhMWF1gpoVPcjD5y5leMuxxhhO2L-YgWvmZ1FCN872mdSCAom7_yTA9LVRz9ZQC3a5zWdYGDA1nui40LQMs-zXnIwUmrG4RjxmG_-vWVgM4hF0Y8I8xKcA7i6_AYABakTc0RsgO4LvvpKSN9Vvuw_Uhndf7VNcRLGvveT-axwBtwCr5eLirj2ngiAGzRZveH_jthVVI9aI-fdcwwiBJF7UnGabngNSWrOFJ92u6yhh1cd1orC1nk8bPvPDodEibLpZePzaLqbbQ0BLAckuWCtkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحید شمسایی: امام‌حسین(ع) خودش دست ما را می‌گیرد
وحید شمسایی سرمربی تیم ملی فوتسال درباره حضورش در کاروان اربعین حسینی:
🔹
این حضور به این دلیل است که خود آقا دست ما را گرفته و امضا کرده است. اولین بار است که با کاروان و به شکل گروهی در این مسیر حضور پیدا می‌کنم.
🔹
زیبایی اربعین همین است که هرکس با هر توان و شرایطی، به عشق امام حسین (ع) قدمی برمی‌دارد. فرقی نمی‌کند عراقی باشد، ایرانی، بحرینی، یمنی یا از هر جای دیگری؛ همه کنار هم هستند و از این سفر معنوی بهره می‌برند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/677611" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677609">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رانت، مافیا و دست‌های پشت پرده در مصوبه تعیین‌تکلیف نیروهای شرکتی  بیگدلی، عضو کمیسیون اجتماعی مجلس:
🔹
مصوبه هیئت وزیران درباره نیروهای شرکتی تحت تأثیر رانت و مافیاست و به جای تعیین‌تکلیف، به هدررفت بیت‌المال منجر می‌شود.
🔹
رئیس سازمان اداری و استخدامی باید…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/677609" target="_blank">📅 10:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAlldt23hzkbfY9ABBK1mdEwhiLfDX9kJ_YyM_eZ7U2c9ElJAD5bY7toE3RTA9vYsaBKD54KKvfbbV5nyGjSkOvP-ML57OIoifqKA1KZveGqKxkj3B9OsxrYnrKoUehOENWblc9hcj0Pq916nF9J-a-nsDQxeiSJlv_IksQ41l-i-mgBik2W8LYbdtusyT52J0EAkFibzglgaENj599qxcWYqoEh5FJGzMiEg8qLqNAgdgu-dktKniaoboclz-t5c4HopL0I_GxZh6IA2tHp0Mp60O1IeD2FntOkDCRug81ciSIXJTfN4w1Y508BpO7rdmZSU18BX65UwtQcWqmqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر روز ناسا؛ رنگین‌کمان آتشی در آسمان ویرجینیای غربی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/677603" target="_blank">📅 09:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
فرصت دوباره انتخاب رشته برای نهمی‌ها و امکان تغییر رشته در پایه‌های دهم و یازدهم
مدیر کمیسیون مقررات تحصیلی شورای عالی آموزش و پرورش:
🔹
نهمی‌ها می‌توانند در آزمون تعیین رشته مجدد شرکت کنند.
🔹
تغییر رشته در پایان پایه دهم و در پایه یازدهم (فقط درون شاخه نظری) امکان‌پذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/677601" target="_blank">📅 09:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677599">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
رانت، مافیا و دست‌های پشت پرده در مصوبه تعیین‌تکلیف نیروهای شرکتی
بیگدلی، عضو کمیسیون اجتماعی مجلس:
🔹
مصوبه هیئت وزیران درباره نیروهای شرکتی تحت تأثیر رانت و مافیاست و به جای تعیین‌تکلیف، به هدررفت بیت‌المال منجر می‌شود.
🔹
رئیس سازمان اداری و استخدامی باید در این باره پاسخگو باشد./ باشگاه خبرنگاران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/677599" target="_blank">📅 09:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677598">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad4M5qDHRfo1QyIcpS1LILAkdHyR21BRT_OhMqWqQOiIZUM8v_DwmFWmykX1awfnQJnSXzbGBjVHMBx-lWlJ4ps_faK88iXuxomopYc0a7uWmBqAtOPWrp7GqlqvbF3v7b0SXDb6C6WtCVMwZzkzYK39NHc7NfDvFDirQU9K-BQeM0rziR9p9HR8C5YI20eVW6LTEQzdCwIG7LWvdvq-rp_YCDPgbVTvwH2cEwKXn8vO6CbvlnApaWqhbHK8rjk8jl-WiiFpgk_QYq9l4aCfW3mb2qxRRWrkA6dpt5VzNgo4XHioWF1a8Bnf0KPCnYhcMDBY1s63oV3_-GbdUWttkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح فروش فوری کیا اسپورتیج 2025 کوشا خودرو
✅
قیمت قطعی
⚡
تحویل حداکثر 20 روزه
📅
شروع ثبت‌نام:
یکشنبه 11 مرداد 1405
🕚
ساعت 11:00 صبح
ثبت‌نام و پرداخت وجه به‌صورت آنلاین از طریق سامانه فروش کوشا خودرو انجام می‌شود
👇
🔗
سامانه فروش:
https://sale.kooshakhodro.com/
📄
دانلود بخشنامه فروش
⏳
ظرفیت محدود است و ثبت‌نام تا تکمیل ظرفیت ادامه خواهد داشت.</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/677598" target="_blank">📅 09:03 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
