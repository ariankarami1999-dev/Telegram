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
<img src="https://cdn4.telesco.pe/file/YEs0ppM50J4b-QbKBobXa3t7WPx4BRZGTQIi4R9-t45ruDo4vijUBg3jUa-dq1KqzhIRfO6j1-PXbYacFdYC2XDOwCeIWJOmONXbo49Wh9UZ2wKZxJOvqAAGReY2ZGOpb6LImaZPD8sZ3tA5X8INrjyc8_010HjcOFh4wFmZFg6CmbU2-J2OgBbT1SSKqVQVhthtT3bmK3Q6t9r9l4lP3KWui6j3gPmco_rmTIYXLoy9aIktsQBDdo4uJH8JCGWOX31N2mgxr-iJJxdQJ4QqjrGfFwcrVwL8l0RwkPsbYihi1d6jMTL6bSAC5RZkOPnDxEnwSJsUhOxqBWkcAhkbGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 251K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 11:30:51</div>
<hr>

<div class="tg-post" id="msg-76419">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇩🇪
إغلاق مطار ميونيخ في ألمانيا بعد رصد مسيّرة</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/76419" target="_blank">📅 11:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76418">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Homayoun Shajarian - Iran e Man (همایون شجریان و سهراب پورناظری…</div>
  <div class="tg-doc-extra">Melodifa</div>
</div>
<a href="https://t.me/naya_foriraq/76418" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#شاركها</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/naya_foriraq/76418" target="_blank">📅 11:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76417">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">أفادت وكالة بلومبيرغ بإصابة عدد من أفراد الجيش الأمريكي وتضرر طائرتين مسيرتين من طراز MQ-9 Reaper بشكل بالغ في قاعدة علي السالم الجوية الكويتية خلال هجوم إيراني وقع مطلع هذا الأسبوع. وذكرت القيادة المركزية الأمريكية (سنتكوم) أن الدفاعات الجوية الكويتية اعترضت…</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/naya_foriraq/76417" target="_blank">📅 11:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">أفادت وكالة بلومبيرغ بإصابة عدد من أفراد الجيش الأمريكي وتضرر طائرتين مسيرتين من طراز MQ-9 Reaper بشكل بالغ في قاعدة علي السالم الجوية الكويتية خلال هجوم إيراني وقع مطلع هذا الأسبوع. وذكرت القيادة المركزية الأمريكية (سنتكوم) أن الدفاعات الجوية الكويتية اعترضت صاروخاً كان يستهدف القاعدة في 27 مايو/أيار، إلا أن بلومبيرغ أفادت بأن شظايا من الصاروخ المعترض أصابت القاعدة.</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/naya_foriraq/76416" target="_blank">📅 11:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76415">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/naya_foriraq/76415" target="_blank">📅 11:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌟
حزب الله: فجرنا مسيّرة إسرائيليّة من نوع "هرمز  450 - زيك" في أجواء بلدة زوطر الشرقيّة بصاروخ أرض جو.</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/naya_foriraq/76414" target="_blank">📅 11:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76413">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92fdb1ed99.mp4?token=WRIHGejPGx0i5iLtUpPL7iIlxkAemWoCINtZk3YyuF0ZNOfeb5pv1rcQz8Hr-caIZldoAk1T8vYGrdzQK94munqYg--7pJ5mrrFhtVuvUWR_YL6V9nm6wFiYRkXY3af36wc-lTeib6uej_zCcUF0oQSxnh7dsnumLrr2MdmTS_-qPaTf89XvUmNgh0e_wGoziT8JqJ_VcVADtC9NPPG_3x1WT48ervwGuonCiKP6_6-N9Ib0-d8OwM1thljcCbUsOtMG3mnBfsaBd_Tv8tPaJq0Ooi8NVxPnLbqFZgBMXGsIf2sgS9C14hkugqPtJpPs3LlW80q1D5r13dJ4dMZ4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92fdb1ed99.mp4?token=WRIHGejPGx0i5iLtUpPL7iIlxkAemWoCINtZk3YyuF0ZNOfeb5pv1rcQz8Hr-caIZldoAk1T8vYGrdzQK94munqYg--7pJ5mrrFhtVuvUWR_YL6V9nm6wFiYRkXY3af36wc-lTeib6uej_zCcUF0oQSxnh7dsnumLrr2MdmTS_-qPaTf89XvUmNgh0e_wGoziT8JqJ_VcVADtC9NPPG_3x1WT48ervwGuonCiKP6_6-N9Ib0-d8OwM1thljcCbUsOtMG3mnBfsaBd_Tv8tPaJq0Ooi8NVxPnLbqFZgBMXGsIf2sgS9C14hkugqPtJpPs3LlW80q1D5r13dJ4dMZ4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">" سيوف بيد الزيدي "
ارتياح شعبي كبير في الشارع العراقي بعد أغنية الفنان حاتم العراقي بأغنية تتغنى بدولة رئيس الوزراء والإنجازات العظيمة المتحققة و التي عبر عنها مراقبون على انها سمفونية او معلقة او تشبه بخارطة طريق للخروج من بوتقة الأزمة السياسية التي تمر بالبلاد على أمل ان يخرج المارد من القمقم ويرجع العراق يصدر الكهرباء لدول الجوار  …</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/naya_foriraq/76413" target="_blank">📅 10:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1kcCRnL7kERow243II_d69GDZjt7BVLL9R14j5T_oR_utJNxbyW889zCC9jLBmJ8Wbdmkgeb7J8QFZnDukFLH0XhR303wFXcuiEsj4evJKB_IaJjevPNvUNBYCAdE3XB9N0q0Zqk3-F7xCu1EXz0bDRgZib_e9elVOMU6F4dIZhWOGdOl_jteJx6vTXsGuIVwLECpXM6X3gmJJ1IBcJQi8y941kFcyvKsMVH4kCR3GlPaWsaZ4sANnz2ZjgIAYzz9TCbQs9mFE373-49su284IwzFfdklK-ddFATpGZY96FRuKjXV7V-WKVfLueajQx3JszT5HuBzJP9wLmJy-2Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏥
في حالة نادرة جداً.. ولادة طفل برأسين داخل مستشفى اليرموك بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/naya_foriraq/76412" target="_blank">📅 10:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76409">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AST0mlXQUGx_l4KCITAecRMrN_E6b3zZmfkAMgN0LSQpAWm_9azkhRflHoQetLOeLzTIW5BLQeVu55pJwE2xYpPRwWi0INL4iOwBwy9EoaXBFJmMjDIHgg5E7htvvxFY2Zbr6nq8wNEDsYTHxNCZ8r-LVzUedzUguCIC5D3P76oVheXbjmsAWYKMzhMfB09cJnHnSk_uiiGDvvOq1SoXVXxbTlGOPY2J5se-Lx3iGurUpf0G-IlctKZSCYKSNGN_BRW6sW395MB5ekHmbmnQPvm8aZXqPnyk5FNSuD2h9dD09aQlKWw-SJX--QtCfjRoBcpJNflZsvxGVesTNzKL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQ_ZYyeYCvjfeG_X1Ty32EkaMB7-vWp-lvVZe1qiRF5wSVtfQQTQcV9Sj0WgkJTQBerz4mFy_7W6i1dYWxreGBmQeH5QmzwR6yKPAiXGRmyxU6q1zhMfh4QvUkGfVlDgeKmapvCFTnBsoDevXAQttFxHIVldyeSlD6JIRC9NXBnnkDVEQii-kUeOxs1wGz07nKrUthqvoUyk3AIp25Cziu_qlKBgjBJMbPKQROIq4Tpz8RkS_4ihvfqox_qJBaeox6zGowYgWwAOg-W2PNmk_-LgUqcxpTBkT_bAga9UADtqngGgxNPPmSTpwgVW_hwSgO7lKMS8qklFoVqm_urLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjDEASYKE58FZXjvHqbezIb9IWbFertCWFjM69s_CBiQzUy13Rrhafd7na-xUMimwhiaJNonnufaMmSbXTJpjr5xI63OLXW5pTZw5XoAeRxqKi7AU-AFHOKyyLjaTV94qeyV7L1RbsXjDVkWfdH8hHTYFmYRLYlY6EN_nHbI5IUO6wARw9lWAU0XPHrYNwFgY8qGJZ179OZ9U5aB4Ck_3WG641Kg7lXbYAFUFfo6WgPNm7syCnfyH28yY_DRUnjewwocne1rBvvWYWb7XRWtcVV6CdqSr1QFV3tLAWH88_oUyAkR-Vsgktm7go008Lq0pr72zRMfgk52mJ7xkPd4jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
أصدر البيت الأبيض أحدث تقرير للفحص البدني الذي خضع له ترامب.</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/naya_foriraq/76409" target="_blank">📅 09:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76408">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23184ff86c.mp4?token=USnqjr9dXWjqD2i2nxEbr_9SGYY-vMM60T4cS7eOZ0fD6fgWiWw4DhuH8uTA8XH4OHgdXSjnenCPv_NXWLrp36YFcyk1EHryKm0AtUIj6nYlsx83OiS8-epuSMRMaV6plUXpp1U_3SL5MF__O7aKQRLk1e1m60_hoCzHqRLpC_jS5UDF91ulmqq_IxCwBucIkLGAUZIm6y0QjKyigE3LVCWOk8VuECPN5Y38gNfMYmwChk9xxh5RnG3OfLRdcEBGx77BKpV0yZx4ryw6v6JildjMe_bf225O2B8ZGshAfltxwCNvTvahfWspTeNiYcLI62Cpc1hRVY5qaZENyTqR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23184ff86c.mp4?token=USnqjr9dXWjqD2i2nxEbr_9SGYY-vMM60T4cS7eOZ0fD6fgWiWw4DhuH8uTA8XH4OHgdXSjnenCPv_NXWLrp36YFcyk1EHryKm0AtUIj6nYlsx83OiS8-epuSMRMaV6plUXpp1U_3SL5MF__O7aKQRLk1e1m60_hoCzHqRLpC_jS5UDF91ulmqq_IxCwBucIkLGAUZIm6y0QjKyigE3LVCWOk8VuECPN5Y38gNfMYmwChk9xxh5RnG3OfLRdcEBGx77BKpV0yZx4ryw6v6JildjMe_bf225O2B8ZGshAfltxwCNvTvahfWspTeNiYcLI62Cpc1hRVY5qaZENyTqR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو الإسرائيلي:  خلال الليل والصباح، تم تفعيل الإنذارات في 4 جولات في عدة مستوطنات بالشمال: كريات شمونة، المطلة، وهذا الصباح أطلق حزب الله أيضًا صواريخ أعمق إلى منطقة ميرون.  صاروخ أصاب مباشرة المركز التجاري في كريات شمونة.</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/naya_foriraq/76408" target="_blank">📅 09:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76407">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇷🇺
الخارجية الروسية: تم استدعاء السفير الروسي لدى أرمينيا إلى موسكو لإجراء مشاورات بشأن خطوات القيادة الأرمينية نحو التقارب مع الاتحاد الأوروبي.</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/naya_foriraq/76407" target="_blank">📅 09:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76406">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22015f29c4.mp4?token=L5-vOE5PsQR6fcyJAe7TtIKE6D3dYhtbaU_jn7XqnjpgjnO0hpxgpqv-hx4VGaExCQ3kFSa3Jart4I_fzk8IHVZQGzUMgt7DDOs4QZbgTvf0b9gTPffWKZ4GwGnTs0q_u681phn3hHP5lnDuov8v9W2Q_PHIfJgyUr6h2y-wv1QXnH6QO7U7Sn6ERKQnhbim1J9g-zbwJxVssfNuJBvRB7LTk8AZjVRU4K33h2PFEOQ0WxNDJIeNBBmwTZ3bNY723qf_YzCfRlXx2DEgySxNcHxGjW_Ye78bU2TIeNQORB2PCj4wPDsPT3eUAMNThl8DaOAQCp1eSChfaHVjWqSNzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22015f29c4.mp4?token=L5-vOE5PsQR6fcyJAe7TtIKE6D3dYhtbaU_jn7XqnjpgjnO0hpxgpqv-hx4VGaExCQ3kFSa3Jart4I_fzk8IHVZQGzUMgt7DDOs4QZbgTvf0b9gTPffWKZ4GwGnTs0q_u681phn3hHP5lnDuov8v9W2Q_PHIfJgyUr6h2y-wv1QXnH6QO7U7Sn6ERKQnhbim1J9g-zbwJxVssfNuJBvRB7LTk8AZjVRU4K33h2PFEOQ0WxNDJIeNBBmwTZ3bNY723qf_YzCfRlXx2DEgySxNcHxGjW_Ye78bU2TIeNQORB2PCj4wPDsPT3eUAMNThl8DaOAQCp1eSChfaHVjWqSNzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو الإسرائيلي:
خلال الليل والصباح، تم تفعيل الإنذارات في 4 جولات في عدة مستوطنات بالشمال: كريات شمونة، المطلة، وهذا الصباح أطلق حزب الله أيضًا صواريخ أعمق إلى منطقة ميرون.
صاروخ أصاب مباشرة المركز التجاري في كريات شمونة.</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/naya_foriraq/76406" target="_blank">📅 09:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76405">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
أبلغت القيادة المركزية الأمريكية (CENTCOM) البحارة والطيارين في المنطقة الواقعة شمال شبه جزيرة مسندم (عُمان) في مضيق هرمز بأنشطة عسكرية خطيرة وشيكة لمعالجة الألغام الإيرانية، وذلك وفقًا لإشعار صادر عن مركز عمليات التجارة البحرية في المملكة المتحدة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76405" target="_blank">📅 02:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76404">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f96f0fa6.mp4?token=bQwLt_8tV7S74NXkRglDA3V7Q17f5kDAyk9j0Ihn8bUGcBFwPp_ESNVykkerv1BBjiRQr7zjFZBFLNjWTj32DU5RzkuUh7ns-FCGt_v7MZztEDnpKDftYKFK-1nA9yXRN9ZSGcHCgqX_fTuMgsU_2WLV-BbIjFR0GGyKWSYPuPQmz4_Esv3_rqxa6sLYw_rVIJ1Qi_l-qW4xPBa661v5O6FA8w2wNl3IIxx9btQKgD1U1HPOMPNI2g0riAeVWm-bKnfxTUonU_kJzKtKSkKqtflrOjsaT240NhhEPGUG1HEAFPsRbjaVP2IhSFPpjAEKAqzbSou9kPcVPVS2EgItWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f96f0fa6.mp4?token=bQwLt_8tV7S74NXkRglDA3V7Q17f5kDAyk9j0Ihn8bUGcBFwPp_ESNVykkerv1BBjiRQr7zjFZBFLNjWTj32DU5RzkuUh7ns-FCGt_v7MZztEDnpKDftYKFK-1nA9yXRN9ZSGcHCgqX_fTuMgsU_2WLV-BbIjFR0GGyKWSYPuPQmz4_Esv3_rqxa6sLYw_rVIJ1Qi_l-qW4xPBa661v5O6FA8w2wNl3IIxx9btQKgD1U1HPOMPNI2g0riAeVWm-bKnfxTUonU_kJzKtKSkKqtflrOjsaT240NhhEPGUG1HEAFPsRbjaVP2IhSFPpjAEKAqzbSou9kPcVPVS2EgItWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇹🇷
العراق وتركيا يتفاوضان على اتفاقية نفط جديدة قبل انتهاء عقد خط جيهان
- تجري مفاوضات للتوصل إلى اتفاقية جديدة لخط أنابيب النفط بين البلدين قبل انتهاء الاتفاقية الحالية في يوليو المقبل
- مساعٍ عراقية لتعزيز السيطرة الاتحادية على صادرات النفط وتقليص أي ترتيبات موازية مع إقليم كردستان.
- تتمسك الحكومة العراقية بأن تكون جميع صادرات النفط عبر شركة تسويق النفط العراقية (سومو) والخزانة الاتحادية، مستندة إلى حكم التحكيم الدولي الذي صدر لصالحها ضد تركيا عام 2023 بشأن صادرات نفط الإقليم.
- في المقابل، تسعى تركيا إلى توسيع الاستفادة من خط الأنابيب الذي تبلغ طاقته نحو 1.5 مليون برميل يومياً، عبر ربطه مستقبلاً بحقول الجنوب ضمن مشروع “طريق التنمية”، الذي يهدف إلى تحويله إلى ممر متكامل للطاقة والتجارة.
- تراهن بغداد على مشروع خط البصرة–الحديثة باعتباره العمود الفقري لمنظومة التصدير الشمالية، مع إبقاء خيارات التصدير عبر سوريا والأردن مفتوحة لتعزيز مرونة الصادرات العراقية وتقليل الاعتماد على مسار واحد.
- يرجح مراقبون أن ينتهي الاتفاق الجديد بإعادة تشغيل ميناء جيهان التركي كممر اتحادي خاضع لإدارة بغداد، مع استمرار استخدام بنية إقليم كردستان التحتية دون منحها استقلالاً تجارياً أو سياسياً في ملف تصدير النفط</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76404" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76403">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مسؤول أمريكي يزعم: الجنرال الأمريكي دونوفان، رئيس القيادة الجنوبية، التقى يوم الجمعة بقادة عسكريين كبار من كوبا بالقرب من قاعدة البحرية الأمريكية في خليج غوانتانامو</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76403" target="_blank">📅 00:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76402">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tN8ZoYivQFGX5aJeTUc-0KmVgiQkCBNTUhg4wruuFKGJ01UXsfiO1BWBXuvYUk-IaK7dAVJ4KFr4PZl06lbH2rXDa7XTrN-wpzebYVoS8MQSO_l3EvjAYz7HV6v-GOLzLcnxyXbVXwQo1wJ6bt7fkwiC6rQl1FA3iUVMVZ4Epgask3Q3AapxC2KPkG4X1gjwf2a_2NqH-_eoU4G30QhQ-TntwpO4_qsD5g5UsOD6hdhuxBRrw75_88u0RcC7fX8tMPMpSozTDcP9z2BapGrZE8OJ58GjD6B_www87MBq-bYjUdEji43z7_glSAcrqhoWsqmdsvd-oXaf6PG5To-0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: أصدرت تعليماتي إلى وزارة التجارة لإجراء تنسيق مع الكونغرس من أجل نقل والسيطرة على كامل مركز كينيدي.
بشكل صادم، حكم قاض عينه باراك حسين أوباما، كريستوفر كوبر، بأن مركز كينيدي، الذي كان سيغلق في أوائل يوليو للتجديدات والبناء على نطاق واسع بسبب سنوات من الإهمال والاضمحلال وسوء الصيانة، والذي كان من المقرر أن تحوله إدارة ترامب إلى أفضل منشأة من نوعها، في أي مكان في العالم، لا يسمح له بالإغلاق لهذه التجديدات، والتي لن يكون من الممكن القيام بها بشكل صحيح دون مثل هذا الإغلاق.
بالإضافة إلى ذلك، حكم القاضي كوبر بأن مجلس الأمناء البالغ عدده 36 عضوا، الذين صوتوا بالإجماع لإضافة اسم "ترامب" إلى مركز كينيدي السابق، مما يجعله مركز ترامب كينيدي، ليس له الحق في القيام بمثل هذه الإضافة، والاسم،
خسر مركز كينيدي، على مر السنين، قبل مشاركتنا منذ فترة وجيزة، مئات الملايين من الدولارات - في بعض الحالات، بما في ذلك وظائف البناء السخيفة التي تم إنجازها، أكثر من 100 مليون دولار سنويا. لقد كنت فخورا جدا بالاستيلاء على مؤسسة خاسرة، وتطلعت إلى جعلها فائزا عظيما ومرموقا لواشنطن العاصمة، وبالفعل الولايات المتحدة الأمريكية. لسوء الحظ، يفضل القاضي كوبر واليسار الراديكالي رؤيته يموت بدلا من أن يحوله الرئيس ترامب إلى شيء يمكن للجميع أن يفخروا به، كما فعلت، في كثير من الحالات، طوال حياتي، ومؤخرا، مع جميع الإنشاءات والتجديدات و"الإصلاحات" التي أكملناها مع وزارة الداخلية على الشلالات والنوافير والآثار وغيرها من الأشياء الجميلة التي أعادناها إلى الحياة في مكان آمن ومأمون الآن، بعد جريمة تسجيل الأرقام القياسية، واشنطن العاصمة، والتي تزدهر مثل، ربما، لم يسبق لها مثيل
لذلك، استنادا إلى حقيقة أن الديمقراطيين اليساريين الراديكاليين يهتمون بمعارضة رئيسك المفضل، ME، أكثر من إنقاذ مركز الفنون الأدائية المحتضر، والذي يفقد جميعه تقريبا مبالغ كبيرة من المال في جميع أنحاء البلاد، سنعمل مع الكونغرس لنقل هذه المؤسسة الفاشلة إليهم حتى يتمكنوا من اتخاذ قرار بشأن ما يجب فعله بها.
قدم القاضي كوبر عرضا تقديميا من قبل كبار خبراء البناء والتشييد حول مدى خطورة المبنى من الناحية الهيكلية، مع العوارض المتعفنة، ومناطق وقوف السيارات المعرضة للانهيار، ومختلف مشاكل الحياة والسلامة الأخرى، بالإضافة إلى حقيقة أنه يحتاج أيضا إلى تجديد كبير، من وجهة نظر جمالية، لكنه لم يكن "متأرجحا"، وقال إنه يريد أن يظل المبنى مفتوحا بشكل لا يصدق، وبالتالي خطير. يجب أن يخجل القاضي كوبر من نفسه! لا يمكنني التورط في وضع يسمح فيه للخطر على الجمهور بالازدهار على مرأى من الجميع ومفتوح. ما لم أكن حرا في فعل ما أفعله بشكل أفضل من أي شخص آخر، وأعيد هذه المؤسسة، جسديا وماليا وفنيا، ليس لدي أي اهتمام بمواصلة ما يمكن أن يكون رحلة ميؤوس منها إلى "لا تهبط أبدا". لم يكن هناك أبدا رئيس للولايات المتحدة عومل بشكل غير عادل من قبل المحاكم مثلي، ولكن لا بأس، سأستمر في القيام بما يعتبر، عملا رائعا لشعب بلدنا الرائع. لقد أوعزت إلى وزارة التجارة باتخاذ جميع الترتيبات اللازمة مع الكونغرس للسماح بالنقل الكامل والكامل لهذه المؤسسة، ومنحهم مسؤولية تشغيلها وصيانتها وإدارتها. شكرا لك على اهتمامك بهذه المسألة! الرئيس دونالد جي. ترامب</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76402" target="_blank">📅 00:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76401">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مسؤول أمريكي يزعم:
الجنرال الأمريكي دونوفان، رئيس القيادة الجنوبية، التقى يوم الجمعة بقادة عسكريين كبار من كوبا بالقرب من قاعدة البحرية الأمريكية في خليج غوانتانامو</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76401" target="_blank">📅 00:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76400">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">إن بي سي عن مسؤولين أمريكيين:
الجيش الأمريكي لم يؤكد أن إيران زرعت ألغاما في مضيق هرمز رغم عمليات البحث</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76400" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76399">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزارة الخزانة الأمريكية: فرض عقوبات جديدة لمكافحة الإرهاب تشمل أفرادا وكيانات في إيران</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76399" target="_blank">📅 23:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76398">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3fb52f44c.mp4?token=C06RUvlXUizEN4IpWcolOXqRGaVgO9ZDFq5xcxlPsdse5JSrw1TPHiM7iJ5ZRvYgwz8r4r109ne7KiLgcGGq3oTnoTWzq2r1xIP57SVKMiiR51ZU1VAwua1lwmIk3s3DPxYGYeM3jeQWt2ruj9wUfpa9iW3ZuUe0aO1hSCDewlGJd879TW4gB9RymhYim5qO_YwmchhBDe8jncScMmLhMVeLw-bHOizc4mLu8-Dn9U4cjdiNa-RjR5ifA4c9Us9qDln4LwXqu2cf62f9WnhUmFABCNzVaS3k6kZQ38CmEPU6LzFqdgfCSqs7uQmHaKeLPi1v0CvhSXBhS80CxX3OIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3fb52f44c.mp4?token=C06RUvlXUizEN4IpWcolOXqRGaVgO9ZDFq5xcxlPsdse5JSrw1TPHiM7iJ5ZRvYgwz8r4r109ne7KiLgcGGq3oTnoTWzq2r1xIP57SVKMiiR51ZU1VAwua1lwmIk3s3DPxYGYeM3jeQWt2ruj9wUfpa9iW3ZuUe0aO1hSCDewlGJd879TW4gB9RymhYim5qO_YwmchhBDe8jncScMmLhMVeLw-bHOizc4mLu8-Dn9U4cjdiNa-RjR5ifA4c9Us9qDln4LwXqu2cf62f9WnhUmFABCNzVaS3k6kZQ38CmEPU6LzFqdgfCSqs7uQmHaKeLPi1v0CvhSXBhS80CxX3OIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من مدينة العامرية في العاصمة بغداد.. ازمة في توفر البانزين تضرب مختلف مدن العراق</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/76398" target="_blank">📅 23:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76397">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزير الخزانة الأمريكي: سيتم رفع الحصار المفروض على إيران تدريجيًا.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76397" target="_blank">📅 23:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76396">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزير الخزانة الأمريكي:
سيتم رفع الحصار المفروض على إيران تدريجيًا.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76396" target="_blank">📅 23:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76395">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📰
مسؤول إداري رفيع لنيويورك تايمز:
اجتماع ترامب في غرفة العمليات استمر نحو ساعتين، لم يتخذ ترامب قرارًا بشأن اتفاقية جديدة مع إيران.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76395" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76394">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏وزير الداخلية الأميركي يقول ان اجتماع ترامب قد يخرج بأخبار مهمة للغاية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/76394" target="_blank">📅 22:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76393">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfd30ea590.mp4?token=odGY3_tARXLROQ1G_gGVMpf4oiAOKW45COQ6KbIX43I6mwRWKcK8jUEaH8jXMrhaOEJuTOiI4LOvV0jzPqxRL2iQ1m7v_rEYDBOAvbj6wzeQ6aNv8mzZdXukx5Tq9RiRUoFLN_pxKG_ht0fUhmxj-INd6QOfiGx0E7mtolTRdMb3qjQqb9Qe13fVgF702O2PM85IWp0pltxOH5teSKIkDj8WZTjr9XbY6_5EF4Go5VnNEaWhjWWA_c70F-Ya9fCJ1430iJi7XNOZwe_qlqHO3vWtx44yoyVvYNH4az2__j1XNL6MM1Zcc2BMFrgK12OyQ-NCevYObG7ZEmbnPTDFYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfd30ea590.mp4?token=odGY3_tARXLROQ1G_gGVMpf4oiAOKW45COQ6KbIX43I6mwRWKcK8jUEaH8jXMrhaOEJuTOiI4LOvV0jzPqxRL2iQ1m7v_rEYDBOAvbj6wzeQ6aNv8mzZdXukx5Tq9RiRUoFLN_pxKG_ht0fUhmxj-INd6QOfiGx0E7mtolTRdMb3qjQqb9Qe13fVgF702O2PM85IWp0pltxOH5teSKIkDj8WZTjr9XbY6_5EF4Go5VnNEaWhjWWA_c70F-Ya9fCJ1430iJi7XNOZwe_qlqHO3vWtx44yoyVvYNH4az2__j1XNL6MM1Zcc2BMFrgK12OyQ-NCevYObG7ZEmbnPTDFYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الدفاعات الجوية الإيرانية اشتبكت مع اجسام معادية في سماء جزيرة قشم وتمكنت من استهدافها واسقاطها.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76393" target="_blank">📅 21:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76392">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed32016f8e.mp4?token=T3VfAhJJro2wcEwasIJhY678mF4WtPMeGfuO6OlwrzELWkUQ3JaXwZDaxtWSaeXwoK9v0nalMmGdPj9uui7HGBqRyFM9RzxqAGEfY9uTbFZpIGysMNQpOAot5oB_aXDcAwWLlvwltFgIFRGPwkM9uzS8Oh5cZXUzzZsj0UL2QH4ETv9jwcwCI4Qwd7ILZz-RgQAE1z6_dmoKeRN1zB8yr0s3s-e3Y5QWbqtTgUzATBayvglU--h_zS0dV6TgIVpwI-vDY1-yd4ymj0R6gcMd1m8rBJQeCqPLaLxgIdrmGVbCTmTH-dslaz6ZopLtsC2CP1JRdFCqqi5QvJ9qmtfc9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed32016f8e.mp4?token=T3VfAhJJro2wcEwasIJhY678mF4WtPMeGfuO6OlwrzELWkUQ3JaXwZDaxtWSaeXwoK9v0nalMmGdPj9uui7HGBqRyFM9RzxqAGEfY9uTbFZpIGysMNQpOAot5oB_aXDcAwWLlvwltFgIFRGPwkM9uzS8Oh5cZXUzzZsj0UL2QH4ETv9jwcwCI4Qwd7ILZz-RgQAE1z6_dmoKeRN1zB8yr0s3s-e3Y5QWbqtTgUzATBayvglU--h_zS0dV6TgIVpwI-vDY1-yd4ymj0R6gcMd1m8rBJQeCqPLaLxgIdrmGVbCTmTH-dslaz6ZopLtsC2CP1JRdFCqqi5QvJ9qmtfc9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
تفعيل الدفاعات الجوية الإيرانية في جزيرة قشم جنوبي البلاد.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76392" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76391">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭐️
تفعيل الدفاعات الجوية الإيرانية في جزيرة قشم جنوبي البلاد.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76391" target="_blank">📅 21:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76390">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbT4_QRJWuWAu7JBouUzep_FQW4U6JqkHYL_Xq5UGm9QjcQa8lbU-Ag3jlZ52apK4dbU45SOvmHbTw9HbN5P275UKwk3k2gyqXc_qmC-rUg3TwDpXhC_2s5-eL07zZS--BrQgFT0KbMO0aSutEpAG9T1s61pKp73DCEH9lnX9n7LlsG5dVCC6yu0W8id_koyIGH3wX8Qgqg3x_3Hra8RN2ljc5cjPGBIzmil4vYhBDHrOFKfn0LlBlqnuuUDnetHemfS58ZdloUy1CiYdlGLeahnZQzjA6VM9evzFDTLbauBFDDsLzTgTUxbG-fBUdBQjh10tHWXO71uNyZMdL41iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: يجب على إيران أن توافق على عدم امتلاكها سلاحًا نوويًا أو قنبلة نووية. يجب فتح مضيق هرمز فورًا، دون رسوم، أمام حركة الملاحة البحرية غير المقيدة في كلا الاتجاهين. سيتم إزالة جميع الألغام المائية (القنابل)، إن وجدت (لقد أزلنا، عن طريق التفجير، العديد…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76390" target="_blank">📅 21:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76388">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbte7vCqzn4TyIgpSMxyOoeHkBQ6M1V55ArPQUqr70ee05FcKn3NYBTpP3pL7kWB9tfFZZGN7E0EQVgrEGA175VrTrgYu-JmfBb_TCtYQkgmWEoahLu8v7YKs5_MMORBKoCaXWrNdVxuAyQ-1LspxB3HkADaYgqKkKIos1UFX7RTKi6twNSNzxoboy4FAerAagLaFT-WZ1mFyKkotzCDYJywIf79mMNzySXzZTbqZlZ02xt_Ppc4Y3r2kgd5humwGEDh3PfLi5eeZ1d7xMpGJGA_LhgangbzFz8zyqP9RE5WBVRCW5BC89kMIosWbp8WVREZPz_pYF1WBVALJe6CKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bb6AIPhQgcjFfMbQauHFVDK2wwAHtN7YN_wUVqzF2Zc1iOu1GTmGmz0Sk8KIJ6-oVOb_ht5Rt0QNsWR_1EYLRdn7NcTDQSxkbnTZntBy_Cp7dOEqdhlXhv7soOlW4dC6ntF2f4faJCMF8WdAz03Tr_PVokRhpkOo_5FP85wBuypwA_OxVJYRZ_l3gCAN4vBiRM7z-jvXxcuHUjHR5K5S7ljWguut5uDeWYeODL1Awq8i81QsvacE4GXvXN4nENn7MIdmOH_zkShVLmB9WrtDFDtgRQw66WvWaFunweCShOaDSwia9_yIM-bMraZOcd6ZjOu31AHzFohvbgZDSNabXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
رصد نايا..
طائرة تابعة لسلاح الجو الأمريكي من طراز E-11A BACN  تحلِّق فوق العراق، وتحديداً فوق صحراء الأنبار، وخاصة الطريق الذي يربط الرمادي والرطبة بالقرب من الحدود العراقية السورية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76388" target="_blank">📅 21:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76387">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYpez4071q98mNNMrP_0oMIbN69XeLbouBkNUV28AwY6vfEhxlMXkEaync6OTWUggIAZu2SzDawco1CloqC4hsnvsVUIWBzp_RAukzxtAlKfrjEU6K68bFY2NH_t1a4PPesRfes_07fSc6YtCwelZdWipkeaTS_M-cQ9J5X4mGLhiV-f1s1a6vLrt-S7V2oedIijdhUiinxRdfAY_-slnIifzfG7CnIqRy3OjbHO_UP77IsEy7yv7bhWakoYXYOqolmgIDSHtL4lSCZbQVxUHOJP0O9-aZ7hormp268tE6gZICHOecaq3IXBWXJwebCJzmr8gw5eAP3i4HqV1b12fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
دبابات ميركافا أخرى تابعة لجيش الإحتلال الصهيوني تصيبها وتحرقها صواريخ ومسيرات حزب الله في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76387" target="_blank">📅 21:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76386">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546ca50588.mp4?token=VJF-QAVG97JLSqGDaSK9BOTN5NhckxR-GTYgJaOn8TzVnMS-0HUh9V7yNs2_29jENvLt3AQDpj2u7rIvQcdhMce5NU62eio2c6q85DmbpjFZSJFRN1mOvihWM2qgaMzzy3qWe_iCoFwfBzcnH9XJFwHr6X4O8PAFipMm9EdB647SGh7L21_Zh5HbO8OSSai9Vqok-TLIPp9iAhKyhgbfrZWojqLf07kMYfNAT-0uMPsabdW-nmzHpYz5x34WVpcNlZMTnrsvJematEpWrilnrjq23gMhw2q8pz4mScEyLsPlaOAo8RJso0F-iYxXOJNziHMKVgiZ3sk_7XIciMbSHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546ca50588.mp4?token=VJF-QAVG97JLSqGDaSK9BOTN5NhckxR-GTYgJaOn8TzVnMS-0HUh9V7yNs2_29jENvLt3AQDpj2u7rIvQcdhMce5NU62eio2c6q85DmbpjFZSJFRN1mOvihWM2qgaMzzy3qWe_iCoFwfBzcnH9XJFwHr6X4O8PAFipMm9EdB647SGh7L21_Zh5HbO8OSSai9Vqok-TLIPp9iAhKyhgbfrZWojqLf07kMYfNAT-0uMPsabdW-nmzHpYz5x34WVpcNlZMTnrsvJematEpWrilnrjq23gMhw2q8pz4mScEyLsPlaOAo8RJso0F-iYxXOJNziHMKVgiZ3sk_7XIciMbSHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر
🌟
🏴‍☠️
دبابات وآليات الجيش الإسرائيلي تحترق في بلدة يحمر بجنوب لبنان بعد دكها بالصواريخ الموجهة والمسيرات الإنقضاضية من قبل أبناء نصرالله.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76386" target="_blank">📅 20:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76385">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: لقد ودعنا لغة "ينبغي" منذ 47 عاماً؛ لا يمكن لأي من الأطراف الغربية أن تتحدث بلغة "ينبغي" عند الحديث عن الجمهورية الإسلامية الإيرانية.  يجب أن نرى مصداقية رفع الحصار البحري أهو حقيقي أم مجرد تصريحات إعلامية.  نركز في هذه المرحلة على إنهاء…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76385" target="_blank">📅 20:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76384">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين: الاتفاق مع إيران سيتضمن وقفا لإطلاق النار في لبنان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76384" target="_blank">📅 20:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76383">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418eb7c1ed.mp4?token=qaqpS3dZ6HdpXfJLFWUSNQhK6f__tvaMdJD5GyOWbosfQKp2R6odB9LOPmZH7HuNypXpCnQju2-Kbb-OPgnjIVie2okhB_5qbxRwzoS03su2S8_RrJqGYhRKFNp8fOcaEmiAYV60Umst-tCPf66OCzIpP8ouqXvV2ia6ViUvEuhBS_d4aATqrABNsZBSd8mitCnuMiu8SqO5UzUynMijvTF4O3ZvzW99TMeYA-1AvjU0Yty9-QHW7vWAyhoamJCZ8Z1NE2SXo6COCyP6CUaEaIN3YwdT7Yh4kU_HREHSOsJ6WHfeLTHt2OyfSPY6IcTwQ5Jvh3CcrQCWwNydAOhd9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418eb7c1ed.mp4?token=qaqpS3dZ6HdpXfJLFWUSNQhK6f__tvaMdJD5GyOWbosfQKp2R6odB9LOPmZH7HuNypXpCnQju2-Kbb-OPgnjIVie2okhB_5qbxRwzoS03su2S8_RrJqGYhRKFNp8fOcaEmiAYV60Umst-tCPf66OCzIpP8ouqXvV2ia6ViUvEuhBS_d4aATqrABNsZBSd8mitCnuMiu8SqO5UzUynMijvTF4O3ZvzW99TMeYA-1AvjU0Yty9-QHW7vWAyhoamJCZ8Z1NE2SXo6COCyP6CUaEaIN3YwdT7Yh4kU_HREHSOsJ6WHfeLTHt2OyfSPY6IcTwQ5Jvh3CcrQCWwNydAOhd9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا في بلدتي يحمر الشقيف وتبّين بجنوب لبنان بواسطة صواريخ موجه من قبل حزب الله.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76383" target="_blank">📅 20:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76382">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyhOHTuetpymWodLWwe-S1833nL-DMesgzuGtL0TPnAqDE1bpTIBgEZiFnShWmgt8QhGqJLyrCdvC6XjJzo_OpxBAkGbka67kRLxQNEhiEt1rAZQ-7I4L_z1zBNEhhgNRbLrqfx6d9J_bPZ_74aTx-iEPhHoteCiDjltOJw-XrvpO_YPCd1GeMh37n7am2aMK6ICVGpr0ufaKq4TIhrUDvfKLIZWCFd2MsU6_cgyiBBqT2pXXijpv24mF1avFZuW323LU_49-IlJ-lNrR6kwTpuPK-1KrMjr-Nc5cNTqwrb55_8bjTX9sNganAlkgXO7F4OGtbI_aJpGBAyiHV8UeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
بين مايتحدث ترامب عن الحصار الفولاذي..
تانكر تركرز:
شهدت الأيام الأخيرة قيام ناقلات النفط بتحميل النفط الخام ومختلف المنتجات المكررة على طول الساحل الإيراني وفي المنشآت البحرية. واليوم (29) مايو /أيار (2026) ، نشهد تحميل ناقلة نفط عملاقة (VLCC) مليوني برميل من النفط الخام.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76382" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76381">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: حتى هذه اللحظة، لم يتم التوصل إلى تفاهم نهائي بين إيران والولايات المتحدة.  ينبغي النظر إلى تصريحات دونالد ترامب، رئيس الحكومة الأمريكية الإرهابية، بشأن رفع الحصار البحري عن إيران بعين الشك، وبالطبع، إذا تم تنفيذ ذلك فعلياً، فلن يعني ذلك…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76381" target="_blank">📅 19:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76380">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الإسرائيلي في بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76380" target="_blank">📅 19:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76379">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إن تصريحات ترامب غير صحيحة.  يُعدّ أهمّ بنود الاتفاق هو الدفع الفوريّ لـ 12 مليار دولار من الأصول الإيرانية المُجمّدة، ووقف إطلاق النار الكامل في لبنان، وهو ما لم يذكره ترامب. وبحسب نصّ الاتفاق، يجب دفع هذا المبلغ فورًا، ولن تدخل إيران…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76379" target="_blank">📅 19:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76378">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇷🇺
بوتين:
الوضع في ساحة المعركة مع أوكرانيا يُشير إلى أن الحرب تقترب من نهايتها.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76378" target="_blank">📅 19:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76377">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4d5158ec0.mp4?token=rrWoKxIsE0o-qJbCm-H9fZG6nMrfcG9yLeGR35YEUyo06HHU5qF-uQuZzythugWruZ3ZTTCnI4zy72XwbZ1FM2ikwqGFHWbVWu3w3VWJl6NABn5sARo_zk2nB4xjOxWqAHTtmFB5PsJkri27ohyKeIfTYv7ZHsxinDRJmVPRjrhSNwcluzjhA3G7qkdKNN7yoHlqHJdLZmqZhk7DK6rXZkLTuSfNbvLujfyIWrgbZCS50p4n5eChNG9ResR_LzXiMIZVCl5wrS3qeumzT_CELXHk1jW8HFGgSELF6YmfBm_7-JoDSDsDtAMJneatYSSu9Swd2pU5nNKQnt7ndHqYUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4d5158ec0.mp4?token=rrWoKxIsE0o-qJbCm-H9fZG6nMrfcG9yLeGR35YEUyo06HHU5qF-uQuZzythugWruZ3ZTTCnI4zy72XwbZ1FM2ikwqGFHWbVWu3w3VWJl6NABn5sARo_zk2nB4xjOxWqAHTtmFB5PsJkri27ohyKeIfTYv7ZHsxinDRJmVPRjrhSNwcluzjhA3G7qkdKNN7yoHlqHJdLZmqZhk7DK6rXZkLTuSfNbvLujfyIWrgbZCS50p4n5eChNG9ResR_LzXiMIZVCl5wrS3qeumzT_CELXHk1jW8HFGgSELF6YmfBm_7-JoDSDsDtAMJneatYSSu9Swd2pU5nNKQnt7ndHqYUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
وسط غضب شعبي في محافظة ديرالزور.. مواطن سوري يهاجم موكب الجولاني.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76377" target="_blank">📅 19:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76376">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
ترامب: يجب على إيران أن توافق على عدم امتلاكها سلاحًا نوويًا أو قنبلة نووية. يجب فتح مضيق هرمز فورًا، دون رسوم، أمام حركة الملاحة البحرية غير المقيدة في كلا الاتجاهين. سيتم إزالة جميع الألغام المائية (القنابل)، إن وجدت (لقد أزلنا، عن طريق التفجير، العديد…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76376" target="_blank">📅 19:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76375">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400a10f551.mp4?token=ThI3DxJtGnwJf6Il9TyqsLBfyD3Xa8Un1Xz8W84GSRIRi13O-hoFBkY5Q9ft1JLbAgVPKx26Gwp9jzctr_MX_TqY6M30Dvp8aEwkHHUdrKGsSMsH16x-UvzAHd7zfvMFkeQcgoGhSsujvwQ8OXLlVUrOUmMWSKVDlMKF13F1jBRN3sJZUnhZgiOy-58y_J3zJ9UbJ-4pzKOhmuaZGlZ65kwCIPY5FBR9vEukSFMyz69oNE2c1ARNEtFxQ6FR08AuLhrswQSDBqG0udBY-XHdOmt4MCiauIOvhq-AjA2Pw7k_Yt1TLC5D39aH6RKsHa-ZVIC_Qd-rnbbVi7b7CLeWzFxWqb8kaj7uJ-Iq7lW1bAcOOom3zravBefcnsibZ1HZDTkwv9sV3b9I1HHQhJOuuvfKrAcDPmd6TUKgS0aMjf-3RGkjne93G1sq2kdileK03VZ6QSzxg6Q62SCCY6DQq1lazLWcHNaTDj0zPou6hLrbVL2e0-3lTID03K3AtR-zZRXHAw1sSLqoazVP8ASsI_dn_vT7WZfGRMyWzWJGFQeKvCSw6SW3JDXQquGFTxTy6SM9ht7Ajp4ImwBgHbICMUUYg5icbbtgtPuouGGmuk0Y6ZeIZXwykxyZGgRpat64v4TRgZT42mdl8mcKKrZCHFboJkugsO8efPNeu6yVUaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400a10f551.mp4?token=ThI3DxJtGnwJf6Il9TyqsLBfyD3Xa8Un1Xz8W84GSRIRi13O-hoFBkY5Q9ft1JLbAgVPKx26Gwp9jzctr_MX_TqY6M30Dvp8aEwkHHUdrKGsSMsH16x-UvzAHd7zfvMFkeQcgoGhSsujvwQ8OXLlVUrOUmMWSKVDlMKF13F1jBRN3sJZUnhZgiOy-58y_J3zJ9UbJ-4pzKOhmuaZGlZ65kwCIPY5FBR9vEukSFMyz69oNE2c1ARNEtFxQ6FR08AuLhrswQSDBqG0udBY-XHdOmt4MCiauIOvhq-AjA2Pw7k_Yt1TLC5D39aH6RKsHa-ZVIC_Qd-rnbbVi7b7CLeWzFxWqb8kaj7uJ-Iq7lW1bAcOOom3zravBefcnsibZ1HZDTkwv9sV3b9I1HHQhJOuuvfKrAcDPmd6TUKgS0aMjf-3RGkjne93G1sq2kdileK03VZ6QSzxg6Q62SCCY6DQq1lazLWcHNaTDj0zPou6hLrbVL2e0-3lTID03K3AtR-zZRXHAw1sSLqoazVP8ASsI_dn_vT7WZfGRMyWzWJGFQeKvCSw6SW3JDXQquGFTxTy6SM9ht7Ajp4ImwBgHbICMUUYg5icbbtgtPuouGGmuk0Y6ZeIZXwykxyZGgRpat64v4TRgZT42mdl8mcKKrZCHFboJkugsO8efPNeu6yVUaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
24-05-2026
آلية هامر قيادية تابعة لجيش العدو الإسرائيلي في في موقع المنارة على الحدود اللبنانية الجنوبية بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76375" target="_blank">📅 19:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76374">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
ترامب: يجب على إيران أن توافق على عدم امتلاكها سلاحًا نوويًا أو قنبلة نووية. يجب فتح مضيق هرمز فورًا، دون رسوم، أمام حركة الملاحة البحرية غير المقيدة في كلا الاتجاهين. سيتم إزالة جميع الألغام المائية (القنابل)، إن وجدت (لقد أزلنا، عن طريق التفجير، العديد…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76374" target="_blank">📅 19:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76373">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇸🇾
مظاهرات ضد الجولاني أمام المبنى المتواجد به في محافظة دير الزور وسط تهديد المتظاهرين بالقتل.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76373" target="_blank">📅 18:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76372">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الإسرائيلي في بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76372" target="_blank">📅 18:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76371">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ4JoywnVu1gcZZRecR6m_yXB72C-UCIlkRve7XvZbhtCGd3wxquqF7bQ3kVnVoXzSv9D3hJ3Vvgtjiw-lkiCndYAlOkHJHUkkwDYKUUV2JrNop8CBArkIajLIxsaZjjXI72b-EGXW-bwFOvQhz1DPRybFBswE1vbEfC54d497tRaA7AV6hvcmgqoujgEht4P0d40lNbfGzZlaG2LdtF1Rf2T2LTaUpktmF9-Dy5pwRgfRYIWVCv3ziDAFouO6Euj2s-5mZeriIU7XCRl5EWPU8A8EwVoWe9MZ9ruO1NDBLtdevW_N-I-vt4V5OF0glYK6FdTRZS4LLgHa6ooc0oHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
يجب على إيران أن توافق على عدم امتلاكها سلاحًا نوويًا أو قنبلة نووية. يجب فتح مضيق هرمز فورًا، دون رسوم، أمام حركة الملاحة البحرية غير المقيدة في كلا الاتجاهين. سيتم إزالة جميع الألغام المائية (القنابل)، إن وجدت (لقد أزلنا، عن طريق التفجير، العديد من هذه الألغام باستخدام كاسحات الألغام تحت الماء المتطورة لدينا. ستُكمل إيران الإزالة الفورية و/أو تفجير أي ألغام متبقية، والتي لن تكون كثيرة!). يمكن للسفن العالقة في المضيق بسبب حصارنا البحري المذهل وغير المسبوق، والذي سيتم رفعه الآن، أن تبدأ عملية "العودة إلى الوطن!". سلّموا على زوجاتكم وأزواجكم وآبائكم وعائلاتكم منّي، رئيسكم المفضل! سيتم استخراج المواد المخصبة، والتي يُشار إليها أحيانًا باسم "الغبار النووي"، والمدفونة في أعماق الأرض مع الجبال المنهارة تقريبًا، نتيجة لهجوم قاذفات بي-2 القوي قبل 11 شهرًا، من قِبل الولايات المتحدة بالتعاون مع الجمهورية الإسلامية الإيرانية، بالإضافة إلى الوكالة الدولية للطاقة الذرية، وتدميرها. لن يتم تبادل أي أموال حتى إشعار آخر. وقد تم الاتفاق على بنود أخرى أقل أهمية بكثير. سأجتمع الآن في غرفة العمليات لاتخاذ القرار النهائي. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76371" target="_blank">📅 18:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76370">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1a1115ab.mp4?token=TVrbIstfI_OluDehRKnOFtnCvw4Ca_fZcrtVvUTwIR472tBimA-LWI9G_9F8ad3TOWj7mA2NlUx25e8BQ8-IgnC4XDgbgF0xs2VlRjJ_bu9MxzQiFAjx2dGZgozJ5yaoqAI_mzjjHp-8G-OG76PhBbYn5q0NAahsYuSs1STQs6fcrYYBSbKcLTXy9I3-PNgVrCDGUkqojxd1WUM7K2oGe_qVE4OcwOT7nbgt_W__IfZDarQi2BKjAHm2j99Y_8Lwn6c4dXFL8FoMAZ6tZ4YqJV9GMblkyHIlQHsALPxtVV1sKNSN91DrMC7cmw5PTZajNOWJOSWl-5KnDfEtK15WzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1a1115ab.mp4?token=TVrbIstfI_OluDehRKnOFtnCvw4Ca_fZcrtVvUTwIR472tBimA-LWI9G_9F8ad3TOWj7mA2NlUx25e8BQ8-IgnC4XDgbgF0xs2VlRjJ_bu9MxzQiFAjx2dGZgozJ5yaoqAI_mzjjHp-8G-OG76PhBbYn5q0NAahsYuSs1STQs6fcrYYBSbKcLTXy9I3-PNgVrCDGUkqojxd1WUM7K2oGe_qVE4OcwOT7nbgt_W__IfZDarQi2BKjAHm2j99Y_8Lwn6c4dXFL8FoMAZ6tZ4YqJV9GMblkyHIlQHsALPxtVV1sKNSN91DrMC7cmw5PTZajNOWJOSWl-5KnDfEtK15WzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مظاهرات ضد الجولاني أمام المبنى المتواجد به في محافظة دير الزور وسط تهديد المتظاهرين بالقتل.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76370" target="_blank">📅 18:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76369">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpShLycoxWtv1NiHzgX2xXVK0PhDoEF8dAIUcbzRoclT4RDC9YaHho-9qZALOe5gI2bOs6d45BrYUy6t-o96WYwJU01164YRiBWUfdsO7ZL-CHQ-6IjQiA0g-3mX5wKPVDOeQGUCGiWYRLPdLUwdJS3uKYaQY4_GFQmyJu0OoLLOUzIUvzxCzdTeBEBqc5SnIUgReT0Wn3ajasaoBWp2RYeVAej1Oru04iuwKuE47ufLigLfntjkhVKS8nYte2FFWkCPjXP7EaC66LAwqGFUGE5GPCUSduyZpHag2lV7pHIEYxEWAZB0Zkk04ai_gmpAMOtCqVMh-ilFuj7272lwUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحفي تركي يدافع عن تركيا المظلومة من تصريحات الجولانيين حول فيضان سد الفرات في سوريا ويرجح السبب للشيوخ الجاهلين لعلوم الحياة في سوريا الجديدة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76369" target="_blank">📅 18:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76368">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd29d4c9c5.mp4?token=E1gNnKuOGzQIBJRpa0F21JkW-9Pn5wUbZ1A-9qFgZ6EDPK_F93bd-jk_AtZJlaIeLdCgWx4hHzS2rpXgVcXrjS659wW-ZXR5CuphamhNEaB839ZsVklnfEt9mBVauURRTvgJC7W23-XluDz0z4unYUKZ_QnvGJ2KUT90YLwVC7N1l_iOkF2Hc-a4ZRnYwitHTtpBRizS41iHApBdFgahIKwwpCE2REgcM-Paceio1I15mDk4YVSeVTHLzgoD4jiR6hX90eC5bFFsnMHx_t6KzqIgIlufFK8w8iv0YManRZiVqG3K1rlFXhL1X8cy2oFkmrg_dj3-p5BgZybvzITrdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd29d4c9c5.mp4?token=E1gNnKuOGzQIBJRpa0F21JkW-9Pn5wUbZ1A-9qFgZ6EDPK_F93bd-jk_AtZJlaIeLdCgWx4hHzS2rpXgVcXrjS659wW-ZXR5CuphamhNEaB839ZsVklnfEt9mBVauURRTvgJC7W23-XluDz0z4unYUKZ_QnvGJ2KUT90YLwVC7N1l_iOkF2Hc-a4ZRnYwitHTtpBRizS41iHApBdFgahIKwwpCE2REgcM-Paceio1I15mDk4YVSeVTHLzgoD4jiR6hX90eC5bFFsnMHx_t6KzqIgIlufFK8w8iv0YManRZiVqG3K1rlFXhL1X8cy2oFkmrg_dj3-p5BgZybvzITrdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
لا ترسلوهم الى لبنان...
אל תשלחו אותם ללבנון...</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76368" target="_blank">📅 17:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76367">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPhvsOPfBmNX3AsaGLY13tMCqPINPEA4InUntBAotrsFOL_dT3pRRTSjBC9Kxb1qA38SIe0rxnBOXDJPUAY4JxRsv0dpvHy2vpFG_vW034kymJAtFvBoiRovxM89WZObdOlZLLLm-f_D8IWZFXUix8tKRAZpONb2wwLEIK3WzrC7KsmhO7GtMgnDIb0Mbds8klchqkMOTsVUygAXUSMVwiQNopsRaJaDzV26VV8T6F2nwaLUMNQQVH7zMJTUul9onLdpvSmseGPaUziOdRBWqNnEoETqZvL3gKuCZEYz_4tu00IPU4Bj0HwIrrjYrHQ06UPPi5Db1nNgjGRLv92gpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
‏
وزير الخارجية الإيراني عراقجي:
ناقشنا هرمز وإدارتها المستقبلية مع عمان بما يتماشى مع مسؤولياتنا السيادية والقانون الدولي.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76367" target="_blank">📅 17:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76366">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfLvPNZDJvTyEhim-z_sEdhBFolLGLO8Awlmxkj_8bS3HV4o4aD5XiQ6QG7tBKhtuHQu13BgwNFmuRfINxxOGCH7DeGv61XZwS25SqRw3lXfMn_VIzdKPuLVf8194uA2vP3U4O2VlqoWt-LHK6kqBxLP0gmpiaNnyKrj-GluJStYpJrnIIOVt8i1e-ciWS0luiU_ccmzV60ZusW94N8Ogr9YfEJzaypV8AiUnFE5KNnPg0hxs6ErET2Uya5zeswaKMcr5sZKRx1XM0cPRvr6b_Jgt_uqHDAnFVmtjQu6HY3fETwrEqUPfaLLKtINT9Lgydo89kLbRDjuLYzFYM8LvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
حزب الله:
بعد قليل...</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76366" target="_blank">📅 17:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76365">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6933bc2db8.mp4?token=bNiy5f-9UdhAiQ6m8v_v0AgDMHptWfmRS3geLOPoi-YtShVvWZzK4wO_s1ZN_FYsXpwsQBWl__06oKhllS4u4S-jKVLDSWLUISUHskbb8yX7JJ5qvS04JF4COn1XrcmoXI_keuik-RDa_jTsmlT2lEfVyoGqr5w4Dg65UT2VWxp8GGZ3fRwjqakIpITuz7VL4pSlnBnsglOjrCd65Y2SwzlVC2LF7tbV83w_T54096w5bydeJrSPeN--eztXGc69Ck9zKxcsGKqiYBTEHKKSvYRyYt4F3PBMF0L67buMdGeeLliGAjZicAwUzI7u88lN8eKtDOo-5hYEHOUGic0LSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6933bc2db8.mp4?token=bNiy5f-9UdhAiQ6m8v_v0AgDMHptWfmRS3geLOPoi-YtShVvWZzK4wO_s1ZN_FYsXpwsQBWl__06oKhllS4u4S-jKVLDSWLUISUHskbb8yX7JJ5qvS04JF4COn1XrcmoXI_keuik-RDa_jTsmlT2lEfVyoGqr5w4Dg65UT2VWxp8GGZ3fRwjqakIpITuz7VL4pSlnBnsglOjrCd65Y2SwzlVC2LF7tbV83w_T54096w5bydeJrSPeN--eztXGc69Ck9zKxcsGKqiYBTEHKKSvYRyYt4F3PBMF0L67buMdGeeLliGAjZicAwUzI7u88lN8eKtDOo-5hYEHOUGic0LSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
طيران العدو الصهيوني يغير على بلدة البيسارية جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76365" target="_blank">📅 16:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76364">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
‏
شركة شيفرون الاميركية:
لدينا 6 سفن في مضيق هرمز ولن ندفع رسوم عبور.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76364" target="_blank">📅 16:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76363">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7bX3r-zeU6L1gvZAcNSaaGQ5Q3-jRAEps3g9R4te08XVtEBgFYHaPb55DAP7xdVZjuOyfQzcyweRfGrerWVXmJ3KLydqdW6AzaOKpNGNEd4quA1Iphls9ql9-IM1nYpDnGh8fSKeB87WHjdZHVQvD0NXDtsa9Sh4fZRE4XflVKsBUc4TTLywkad0C5hXE-JvQYVNRrar_Z8AMTiFRYcoDmnQ5pjfIfzJsV_m6A0CV5bBUMh_UQlzxWYUtAci04LLgpzvx4cxK1GAb1prrobHquFw_T_JTvedkZHDhHqYNxVOllavuVMo4VnOSOuIu4q4I68-etCvIuAI5HRg1m4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
دمیتري میدفيديف: التزموا الصمت. هذه مجرد البداية تستخدم الطائرات المسيرة الأوروبية، وقطع غيارها، وأسلحتها الأخرى، فضلاً عن المعلومات الاستخباراتية، في هجمات على روسيا يومياً. وتؤدي عملياتها إلى إلحاق أضرار بالمباني السكنية، ومقتل مدنيين.  جميع أنواع الحثالة،…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76363" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76362">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PL1ReQSaPBQJ3EJ2FCW7V6d7nEmif4qncf-tqGYfeoljV4m8IGIK0uz3FZhn86WF4oAxyGAOa0_RDIBzv7fRDtaoY9mssjmRbi4gscke1UTP5aBTQA9sG_WPuddSisZk74frgoRzSfA_13c-NoyrfVp9npRSAawuFUmuZ2wGUD1UMAPbsq-4E88uInnn0jnFzlrGQxqhMjABxSh4SIy0bMHXIs11YFDJ80aD6P71S2GEVo3x7UDCDOM9-tJ6wntfVwj6Hgzjqx8U853BySBbO79zgY5eK7rUxuHeDZUU6aOY6V03jSssiBu2kxZZfsRObhdTQDemOTDylQVknAlgMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
جيل بايدن تعترف الآن أخيرًا بأنها لم تكن تعلم ما الخطأ الذي حدث مع "سليبي جو" خلال مناظرتنا الرئاسية المذهلة ذات التقييم المرتفع لعام 2024، حيث لم يكن جو يقدم أداءً على أعلى مستوى من معايير المناظرة.
قالت إنها كانت تعتقد أنه كان يعاني من "سكتة دماغية"، وأشياء أخرى سيئة حقًا، ومع ذلك لم تهرع أبدًا إلى المسرح لمساعدة زوجها المضطرب، كما ستفعل أي زوجة جيدة. والشيء الوحيد الذي فشلت في ذكره هو مدى أدائي القوي قبل انهياره شبه التام.
بمعنى آخر، كما سأل الكثيرون، هل تسبب أدائي القوي في تلك المناظرة في أنه "اختنق" ببساطة، مما أدى إلى هزيمته المخزية، أم أن هناك أسبابًا أخرى؟ لا أحد غيري يعرف الإجابة على ذلك، لكنني أعرف ذلك!!!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76362" target="_blank">📅 16:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76361">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkKgxPJhfWUnjAJQqrKKIskLIHSP3GorDwkhfFOUiNUIbitBEHm3h8pT7ayfESKOOJ0KITpzjFoL7G4GPYFyWi60b4njQvT14HUMfINyXQKdyVUL_2VPn421haGCw-4UtUHEcEvU4NaMDq0qCv0mdDmGjb6aMdzbX2PVm-635zMVWpKtz5S0XvKNrH9jsBa-YixQa4LRZGyA_WRmNVixzZiBX4dV_IZsVtwNzOmnBaSKHNLm90friLws222hMLrho3i3Xz97XX8dW4qgjifA_4lJITnGFVaR0-e5jBEf0wiTrDdfuyH5e1AlFERl8WXinCjM8U628dxwF3tKHR4s-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
:
- لا نحصل على تنازلات من خلال الحوار، بل من خلال الصواريخ. في المفاوضات، نكتفي بشرحها.
2- لا نثق بالضمانات والأقوال، فالمعيار الوحيد هو السلوك. ولن نتخذ أي إجراء قبل أن يتخذ الطرف الآخر إجراءً.
- الفائز في أي اتفاق هو من يكون أكثر استعداداً للحرب في اليوم التالي.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76361" target="_blank">📅 16:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76360">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bf1f46f4.mp4?token=AeTf4msicDi3oIHaW1Hq_S3q2mYnFYvGGbSZItdS4WNQKDQY9CKRhax19YxPoPxUyIA6y2SzQdWsJUjX7kuts5KtCiGFN4pwJvKwG5TftlzzDZVpeLRdu7tddnl-MjlarOccnH4Uur468j1WwqH4F0PePcOVaS1lsFMiwbUf4U3yZR258AvXmPG6uBVSVFVFCJjk3GX8a3Dk0V09Vu8hYxH69Pj8l0uu0F-lHNISwCUJuASgY7dXsfIX8oKu8SNSULiWtFVXSiXebn_28U8FUsBb1zzwlKCafb77DGNtR0CDv92WumQHyLaz9yWDvZ6a6jghQRD0oUGKMzVfcJ6mMlw5JMriVNt_y2DTQXWbFERKx0G7Ow5Pqy5Rqh-t-fq2WSy3fe6N8yZ0K6FJGow9RpVfeh77v4c1d7oQ0cNAl2uk1rBFQxQagPCywOezqaEndMDupwZsJS8LIEZvfyq9_hXtgWdiiQRGwNEgNO9xVB7U0SGmz0hoig-grm-L2lamOA6DAq3KQitxKY090AeRFMNix9-t13n3F3i7G1tlvb5w1lGUv1knqPg7xhht_fXrTmSbz65-TxfOQ-XmvDZXKMz4J4oHVqQD6ZDvLfvp-3udSBnFsFA6eycoMJi4SMdF0plH-f4mGMvQjxtuikAvtseQ6ow2IHR1_dcubm8bTTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bf1f46f4.mp4?token=AeTf4msicDi3oIHaW1Hq_S3q2mYnFYvGGbSZItdS4WNQKDQY9CKRhax19YxPoPxUyIA6y2SzQdWsJUjX7kuts5KtCiGFN4pwJvKwG5TftlzzDZVpeLRdu7tddnl-MjlarOccnH4Uur468j1WwqH4F0PePcOVaS1lsFMiwbUf4U3yZR258AvXmPG6uBVSVFVFCJjk3GX8a3Dk0V09Vu8hYxH69Pj8l0uu0F-lHNISwCUJuASgY7dXsfIX8oKu8SNSULiWtFVXSiXebn_28U8FUsBb1zzwlKCafb77DGNtR0CDv92WumQHyLaz9yWDvZ6a6jghQRD0oUGKMzVfcJ6mMlw5JMriVNt_y2DTQXWbFERKx0G7Ow5Pqy5Rqh-t-fq2WSy3fe6N8yZ0K6FJGow9RpVfeh77v4c1d7oQ0cNAl2uk1rBFQxQagPCywOezqaEndMDupwZsJS8LIEZvfyq9_hXtgWdiiQRGwNEgNO9xVB7U0SGmz0hoig-grm-L2lamOA6DAq3KQitxKY090AeRFMNix9-t13n3F3i7G1tlvb5w1lGUv1knqPg7xhht_fXrTmSbz65-TxfOQ-XmvDZXKMz4J4oHVqQD6ZDvLfvp-3udSBnFsFA6eycoMJi4SMdF0plH-f4mGMvQjxtuikAvtseQ6ow2IHR1_dcubm8bTTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 27-05-2026 تجمّعات لآليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76360" target="_blank">📅 16:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76359">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇷🇺
‏الخارجية الروسية: سنرد قريبا على قرار رومانيا إغلاق قنصليتنا.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76359" target="_blank">📅 15:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76358">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇷🇺
‏
الخارجية الروسية:
سنرد قريبا على قرار رومانيا إغلاق قنصليتنا.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76358" target="_blank">📅 15:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326e188e45.mp4?token=EJ5hwnCpJQGEFi298Bw7G5CF4eIodFuaxkH0rmwlMJaKes060Sel4MSou9qhqIaYBqAltS9nEdsStZESFp85bcSemuzJFYeR9oku8aXBHSwxzMrMuwACQ623KSj-8ubAHpZs0OfSFeIny6udnlYAn3JlBWd-ZhkfFuNN3WK9bDTELUVTC9LyJhUb3alnR2xdFXg-wGXdet2OwiSODt4y4twWH9iWJwuO-NVnSr4ZgSkldb6Gc3GRFdD2HiK2q1taAY6_oEn4ene-ptYgfyCUxbyZewKqLmTe-R1nxA8KOyKqFLLgpNnV6V8ma3Ld6nOFlBh3dvzKZJWGl0EzqLE0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326e188e45.mp4?token=EJ5hwnCpJQGEFi298Bw7G5CF4eIodFuaxkH0rmwlMJaKes060Sel4MSou9qhqIaYBqAltS9nEdsStZESFp85bcSemuzJFYeR9oku8aXBHSwxzMrMuwACQ623KSj-8ubAHpZs0OfSFeIny6udnlYAn3JlBWd-ZhkfFuNN3WK9bDTELUVTC9LyJhUb3alnR2xdFXg-wGXdet2OwiSODt4y4twWH9iWJwuO-NVnSr4ZgSkldb6Gc3GRFdD2HiK2q1taAY6_oEn4ene-ptYgfyCUxbyZewKqLmTe-R1nxA8KOyKqFLLgpNnV6V8ma3Ld6nOFlBh3dvzKZJWGl0EzqLE0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعتراض طائرة مسيرة اميركية من قبل انصار الله في اليمن.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76356" target="_blank">📅 14:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مضحك
‏
زيلينسكي
: مستعدون لدعم رومانيا في مواجهة مسيّرات روسيا.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76355" target="_blank">📅 14:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7483fa8b.mp4?token=ofzHbOK6fOR38gSsH-2WfXQqHf6tpUYGSNDGqwTbie6NSBvrtCtSE_Q7aQyTJMWTUYYGx2nGBM1bQHFvtOSrxw17ylgj1zXRsWRGru-R5Wmg75W8eJNXLocxC5chPi200a5u7HhVC6D7RBvHwnUR1Vl73H8Nv2cLPdeRi_KjDbcxFIzY0roB4ZfmcSFPZ_T2unZXWeNnuWH5devHR2A_r8hrtl4ieAHqmtMs9I22GWFOsQnrbEqhGCyp7HIne_ppP2339lWimVapm9mbCS2sX3-hRUThAhY-U16rEXiz5TgmeVqHR7iuij8ZP9wXQtr7s7vPsjrulKphJ11-c7ufLrWSVTb6l2xjVKrUIjzmquV25BBCCVlRlHEisavXxmAEcf3uWusUCL8wUj79WBbqDv0gRRB0cIFWA3s21Yd0CmIWRFd-YomoASn90Jo05J2ijmK59l39pBiEmGozciKUydBe78V5daQ8Rq2mbcRtpwlplLGmAPuLIomNoP34nncCuyvKkExfF0Au1StFn4F4TolV94vRnRYie1ohx6NoTygmP4tRg4QXieSQfEgLCgyPYECKedSn_InWjZk6EsPA0vf84omCE1EeynVVrS0d7cwQ3HSLhqIM1y1Veo1OF2_P2SLaT_nfwOu3-ywQfZARek_hMsXhUOEYOrYWo2qsSq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7483fa8b.mp4?token=ofzHbOK6fOR38gSsH-2WfXQqHf6tpUYGSNDGqwTbie6NSBvrtCtSE_Q7aQyTJMWTUYYGx2nGBM1bQHFvtOSrxw17ylgj1zXRsWRGru-R5Wmg75W8eJNXLocxC5chPi200a5u7HhVC6D7RBvHwnUR1Vl73H8Nv2cLPdeRi_KjDbcxFIzY0roB4ZfmcSFPZ_T2unZXWeNnuWH5devHR2A_r8hrtl4ieAHqmtMs9I22GWFOsQnrbEqhGCyp7HIne_ppP2339lWimVapm9mbCS2sX3-hRUThAhY-U16rEXiz5TgmeVqHR7iuij8ZP9wXQtr7s7vPsjrulKphJ11-c7ufLrWSVTb6l2xjVKrUIjzmquV25BBCCVlRlHEisavXxmAEcf3uWusUCL8wUj79WBbqDv0gRRB0cIFWA3s21Yd0CmIWRFd-YomoASn90Jo05J2ijmK59l39pBiEmGozciKUydBe78V5daQ8Rq2mbcRtpwlplLGmAPuLIomNoP34nncCuyvKkExfF0Au1StFn4F4TolV94vRnRYie1ohx6NoTygmP4tRg4QXieSQfEgLCgyPYECKedSn_InWjZk6EsPA0vf84omCE1EeynVVrS0d7cwQ3HSLhqIM1y1Veo1OF2_P2SLaT_nfwOu3-ywQfZARek_hMsXhUOEYOrYWo2qsSq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 24-05-2026
آلية نميرا تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/76354" target="_blank">📅 13:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🐦
نيويورك تايمز:
أحد أحدث العناصر الأكثر إثارة للدهشة في اتفاق مشروع السلام الإيراني هو صندوق استثمار مقترح لإيران - يبلغ حجمه حسب التقارير 300 مليار دولار أمريكي.
قامت إيران في الأصل بتصنيف ذلك على أنه تعويضات عن أضرار الحرب (التي تقدرها بـ 300 مليار إلى 1 تريليون دولار أمريكي). الجانب الأمريكي يعيد تسميته على أنه "صندوق استثمار" دولي سيساعد في تسهيله - وهو إطار أكثر ليونة يتجنب كلمة التعويضات.
يبدو أن الفكرة نشأت مع ستيف ويتكوف وجاريد كوشنر، اللذين اقترحا تعزيز مشاريع العقارات في طهران وآلية استثمار أوسع كحوافز للصفقة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76353" target="_blank">📅 13:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏الصحة العالمية: نتحقق من 223 حالة وفاة مرتبطة بإيبولا في الكونغو الديمقراطية
ارتفاع عدد الإصابات بـ"إيبولا" في الكونغو الديمقراطية لـ 906</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76352" target="_blank">📅 12:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0fc8b717.mp4?token=Xd8WK9O7ioiLeB2OnwOwVK3EV73HEXOjoYgoO3DP-L9u2QmslhVirUQCvKuJiCjcIqEHLP3QBXDnRC_OfW0oKZIzLVMiC-jg04Bqn8M2RYQO_HVJT3k9HHTSXwrDJEodL9kFRcE5S0rAl9mLx1JtQN8UUgV1I1en13kBqosfkwVlnYj2E6UqSpP4tg0Qby1qNTBSVpBinN0a2UyS_b__UuAO86GiuxfJ6mlKTpkzV5etvgXArvLkDvVEOjpuVOxetshHY9MwYfxT7h5g7z8g9r7jmqBeEtkkjb47ATowV1uG8lnfq3paguuqcBCo_X3rk7hAoLfGyekLAtT1R3nZmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0fc8b717.mp4?token=Xd8WK9O7ioiLeB2OnwOwVK3EV73HEXOjoYgoO3DP-L9u2QmslhVirUQCvKuJiCjcIqEHLP3QBXDnRC_OfW0oKZIzLVMiC-jg04Bqn8M2RYQO_HVJT3k9HHTSXwrDJEodL9kFRcE5S0rAl9mLx1JtQN8UUgV1I1en13kBqosfkwVlnYj2E6UqSpP4tg0Qby1qNTBSVpBinN0a2UyS_b__UuAO86GiuxfJ6mlKTpkzV5etvgXArvLkDvVEOjpuVOxetshHY9MwYfxT7h5g7z8g9r7jmqBeEtkkjb47ATowV1uG8lnfq3paguuqcBCo_X3rk7hAoLfGyekLAtT1R3nZmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
دوي انفجارات تهز محافظة حمص السورية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76351" target="_blank">📅 12:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">🇮🇶
وزارة الموارد المائية العراقية: جاهزون لاستيعاب الموجة المائية القادمة من سوريا ولا توجد أي مخاوف على السكان القاطنين على ضفاف نهر الفرات</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76350" target="_blank">📅 12:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDzuAQ93SkMUmn8i0Ze8qPoVRE4KC2ZEWs8YxYM10ULWEdqz3R2BCZNDbwvcU5l8LnKEZkbSa74QrV-J7-8FYdFJcNjhkxyqg5SAz5RfPmh1wYy3YjgVqagBqb-YvB_b_Lo8CvD5DJdvIsm7FvBXyELVhUoGwpLPw3u3s2NrWwtrlT-oBLESZrRAEFqAtefbKneNJNBjP_n0HJtFLizfbOw-ys3NIyLSSIn9cM35WtDlKCbzPuPzwU29hWj4P4jZenFrVJj0xK-OG-8Qkr1WwE187SWCKobbAvFlAlIjuJFgmPS1nw3WGCCY-O-BJURE_29r8b1k0591q6PD_PT4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية الآن فوق الجليل الأعلى دون تفعيل صفارات الإنذار</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76349" target="_blank">📅 11:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 26-05-2026 دبابتي ميركافا تابعتين لجيش العدو الإسرائيلي في بلدة رشاف جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76348" target="_blank">📅 11:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏الأمين العام للناتو: خرق مسيّرة روسية أجواء رومانيا يؤكد أننا جميعا في خطر</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76347" target="_blank">📅 11:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">إعلام إيراني: حركة الملاحة البحرية في مضيق هرمز الآن</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76346" target="_blank">📅 11:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حدث أمني يتعرض له جنود الاحتلال جنوب لبنان</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/76345" target="_blank">📅 10:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📰
سي إن إن: تراجع مخزونات الولايات المتحدة من النفط الخام والبنزين والديزل بسرعة مع استمرار الحرب مع إيران</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76344" target="_blank">📅 10:16 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ول ستريت جورنال:
مقتل
7 من أصل 11 جندياً إسرائيلياً سقطوا منذ بدء وقف إطلاق النار في أبريل بسبب مسيرات الـ FPV
مع كل رحلة بالمسيرات يكتسب مقاتلو حزب الله خبرات اكثر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/76343" target="_blank">📅 08:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">في خبر غير مهم
🌟
وزارة الخارجية العراقية تدين قصف قواعد الاحتلال الاميركي في الكويت التي انطلقت منها الصواريخ لضرب ايران.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/76342" target="_blank">📅 02:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌟
فانس
: نقترب من نقطة تسمح لنا بالجلوس وحسم القضايا العالقة مع إيران لكن الأمر يتطلب إحراز تقدم إضافي.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/76341" target="_blank">📅 01:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f662ae4b77.mp4?token=YhUi74VJZLS7mSeuOJ8SN1d4BPX481eEEPduXDVUmVQZuS-ixjUxvSi0f1Fw33JqFxxIjzA17WVdeiA3lCNLlMyOV4O8P6ngwXVTUmJ2zwlWXFABf2Gja6czQkszncN_s7PD-TS_i9zFfaWV_T1ECNIBRsIL4VeaSq3KnuyVNdLzPNHc-7gLjCGdEvGAuU-i3NK8_lwjsWkLozkGf3CZ4WEP-kNgHwM8cJ89ngeuEaUSG6yf1fxQ9xcuqQPQyuwQGnef_TqmHP0rjhtlxmYktxhi3HxSEejp0pZU_Z0ezu6PC4rKAmtlRD5dvh8Anuhh1g3LUs7xHV1pbo0MCLKZ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f662ae4b77.mp4?token=YhUi74VJZLS7mSeuOJ8SN1d4BPX481eEEPduXDVUmVQZuS-ixjUxvSi0f1Fw33JqFxxIjzA17WVdeiA3lCNLlMyOV4O8P6ngwXVTUmJ2zwlWXFABf2Gja6czQkszncN_s7PD-TS_i9zFfaWV_T1ECNIBRsIL4VeaSq3KnuyVNdLzPNHc-7gLjCGdEvGAuU-i3NK8_lwjsWkLozkGf3CZ4WEP-kNgHwM8cJ89ngeuEaUSG6yf1fxQ9xcuqQPQyuwQGnef_TqmHP0rjhtlxmYktxhi3HxSEejp0pZU_Z0ezu6PC4rKAmtlRD5dvh8Anuhh1g3LUs7xHV1pbo0MCLKZ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
البيت الأبيض ينشر فيديو مع عبارة "هل أنت تستمع؟".</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/76340" target="_blank">📅 01:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🌟
وزارة العدل الأمريكية:
توجيه 8 تهم للعراقي محمد باقر السعدي بسبب أنشطته مع كتائب حزب_الله والحرس الثوري، السعدي ضالع في 20 هجوما ومخططا ضد مصالح أمريكية وإسرائيلية بعضها على الأراضي الأمريكية.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/76339" target="_blank">📅 00:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/76338" target="_blank">📅 00:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFLZ0SV_iKlBNg7spFibVhnjybGdwAfZb9m2MVPv_rbIwEnjLlUhMTuzIiutKxr5Gr0lBAso9JQtxmIuIh7ySpmWo9hOJCjXsTdxgfx8mRqItomglwBPPP2nZZVfjU9mbNB1mKnXUi8vAiIfu2Zx_TJU6jn6THc-7RzUsKniWBCVW6cZ51FuldMm-BTl_7LKRc8C4yNXMhw63qJPNK_gWbC5iV5FZ_ZEpG3aXhP7YqVEWlhnoWaNfL_ogPw_qB4Bh6ddl9Znk5YnjwI_XU44dKKJYXqwro_HjLDnxTnEwjLRvNWAJQet67Jfs6EV3C08XNsFeme5B8CoczJv4IreUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/76337" target="_blank">📅 00:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/76336" target="_blank">📅 00:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXWk-AUZpaZrGowVmuByxBbj6LC30WmqjzY8P9NzgoDHLmGTjGvWcwjEYXAmg-2_3Oeq0rlJl2xxG5rl_DOhv0is51UZCXPxK7bIW7fhgel7rm76yHBfx8tZvq-cFmZ5Ez84ujCee63i5WrY2YXYy8xvsf6aFYA19lo_bZldBMlBI_iW6vLsmmIHUBlzSQ6Anxj2GKxwUVol9m7RZbkhHaeSlkgreNZU1OXnDlDEqv0qw8Doh_gGzstpg80-i7XE1gv-H7ugRCaJh-UwzhsH93wtoZ_YbJ0kKjcVlZR3xm0dvlLcX9Cw8oL4RN0V_94uUgQ_rQRuAniJ5fyvoeFybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇬🇧
رصد نايا
تمارس القوات الجوية البريطانية نشاط لوجستي في سماء العراق حيث تم رصد طائرة شحن عملاقة " A400 “ بالتزامن مع وجود طائرة إرضاع جوي اخرى تؤمن الوقود للطيران الحربي ؛ يذكر ان السفير البريطاني في بغداد قد صرح لقناة عراقية ان العراق يتمتع بالسيادة ولا يوجد هناك احتلال</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76335" target="_blank">📅 00:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76334">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
‏وكالة مهر: الدفاعات الجوية حاولت التصدي لطائرات معادية في بوشهر.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/76334" target="_blank">📅 00:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76333">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
وكالة مهر: القوات المسلحة الإيرانية أطلقت نيراناً تحذيرية باتجاه 4 سفن مخالفة قرب مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76333" target="_blank">📅 00:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76332">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صواريخ كروز من طراز ابو مهدي المهندس باتجاه سفن أمريكية في هرمز</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/76332" target="_blank">📅 23:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76331">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌟
🇷🇺
‏الخزانة الأميركية تصدر ترخيصا يسمح ببعض الصفقات مع شركة "لوك أويل" النفطية الروسية.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/76331" target="_blank">📅 23:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76330">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
🇷🇺
‏الخزانة الأميركية تصدر ترخيصا يسمح ببعض الصفقات مع شركة "لوك أويل" النفطية الروسية.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/76330" target="_blank">📅 23:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76329">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">أنباء عن انفجارات في هرمز</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76329" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76328">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639d01573a.mp4?token=bJSPeh9FG9kJ_lu9QmFtXrfpxaiWer3DLudF6A226Yv4AkVyb9SAKAjQ8HRIy6CCdbZyaZ9bnb4Uc7-vQ_ErmUZlVm3TmNHPGGRBw3iEyyQAyGwPXtIYULPf3kn0P5KsXIdeK8_R3-Jm0N3aCT1LKIK7trX6Hq0QDpVq5h3f_kgvXdMvDCyHjqK1PY6bewS-rj_NA7eZSFVSDQab7ljAHx8hMhl3NLKjbY-Md8tvgVzduTeOZ1Ls-d8dCk0ctU_qszYb55cL37iW8wygiSX0he9p-wVgR_R6kL5UystSs2MhKul-dsR41k8yZa8VfJMfX2H3yN_PY3FflIiBE_4BC1EIZecMjWzOwvfcf_G7qa9C329LNVWCQC1rUG1zfzC7XmfW7cvmTFZRVd7MT6zqexAmioFkrexMAOb38ADo9TaWUXKuvK6pPg1hs9TeQTXHdHD-IorK0wdYK0TtBVDv3_cmUC9dQe_IHVvXOCAF-PWt0t1f4CJwdOsId2wuyFKRWhXH0YjryOL5Q5Jc2jOn5ztZk29AYi2b2kc84MOXLTSlQjpyrPucovL0GtAtC5NjJeK6dFejBmFryzEYygvVL4TPWsS6O30fyjuPCIuzA7Vd1HClgX6OuRIsE6jCBydspTfI2oGZdaLLB5IXZjYgG_uvp7PGCxUmPMpT2zubgcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639d01573a.mp4?token=bJSPeh9FG9kJ_lu9QmFtXrfpxaiWer3DLudF6A226Yv4AkVyb9SAKAjQ8HRIy6CCdbZyaZ9bnb4Uc7-vQ_ErmUZlVm3TmNHPGGRBw3iEyyQAyGwPXtIYULPf3kn0P5KsXIdeK8_R3-Jm0N3aCT1LKIK7trX6Hq0QDpVq5h3f_kgvXdMvDCyHjqK1PY6bewS-rj_NA7eZSFVSDQab7ljAHx8hMhl3NLKjbY-Md8tvgVzduTeOZ1Ls-d8dCk0ctU_qszYb55cL37iW8wygiSX0he9p-wVgR_R6kL5UystSs2MhKul-dsR41k8yZa8VfJMfX2H3yN_PY3FflIiBE_4BC1EIZecMjWzOwvfcf_G7qa9C329LNVWCQC1rUG1zfzC7XmfW7cvmTFZRVd7MT6zqexAmioFkrexMAOb38ADo9TaWUXKuvK6pPg1hs9TeQTXHdHD-IorK0wdYK0TtBVDv3_cmUC9dQe_IHVvXOCAF-PWt0t1f4CJwdOsId2wuyFKRWhXH0YjryOL5Q5Jc2jOn5ztZk29AYi2b2kc84MOXLTSlQjpyrPucovL0GtAtC5NjJeK6dFejBmFryzEYygvVL4TPWsS6O30fyjuPCIuzA7Vd1HClgX6OuRIsE6jCBydspTfI2oGZdaLLB5IXZjYgG_uvp7PGCxUmPMpT2zubgcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية تصدي المقاومة الإسلامية بتاريخ 26-05-2026 أجهزة اتصالات تابعة لجيش العدو الإسرائيلي في موقع العاصي على الحدود اللبنانيّة الجنوبيّة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76328" target="_blank">📅 23:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76327">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">أنباء عن انفجارات في هرمز</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/76327" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76326">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محرم 1 00_٠٦٤٢٥١</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/76326" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">شبه لهم يا حسين
#شاركها</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/76326" target="_blank">📅 22:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76325">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وَاللهِ لاَ أُعْطِيكُمْ بِيَدِي إِعْطَاءَ الذَّلِيلِ، وَلاَ أُقِرُّ إِقْرَارَ الْعَبِيدِ
وإنّ الدّعيّ بن الدّعيّ قد ركز بين اثنتَين؛ بين السّلة (والذّلّة، وهيهات منّا الذّلّة؛ يأبى الله لنا ذلك ورسوله والمؤمنون، وحجورٌ طابت وطهرت، وأُنوفٌ حميّة، ونفوسٌ أبيّة، من أن نؤثر طاعة اللئام على مصارع الكرام ..</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/76325" target="_blank">📅 22:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76324">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTljBKLvL-M2pgtcPy2WAt9PdO68JFD1oaPEGJVXACsg-kir-houC8zisuv_6J5HzwMj1jQN7sXgqULeM60smdPXeRK_GtTFYslniNP3Q__jXQXvlZruJqZt6sqwu505WuZcnKchwoiZ185KGYkrgElNKRy5uYSoFAtuaU2f37hGsnhljAK_dNS1-t9sIiux01qWb6yv5o3EKR6JuQ-4IdYNr8Oi4PsCmXV548s0pBrOi2aAdT9tDIW7yn-g9iyqbSnRsPbGUuXHzGzjLI0bnkS_XyIeveb3jJgs8yYqUDbN34LWpeiTsAZ1qs7p-SPmK2B9IWrI8vwaPGuWsgB6YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المتحدث باسم "سرايا أولياء الدم" أبو مهدي الجعفري: لا تسليم للسلاح ولا حديث عن الطمأنينة قبل أن يرفع الظلم وينتهي الاحتلال عن العراق</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76324" target="_blank">📅 22:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76323">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKkXiiWyk2VtlxrpPwGWDt6V5mSAEduL5-5oaTrtRUUj_fjOgexr-dGXrWiX1YnNecrJtmBqYKm-A9IdalmUKNSDD_cMNR0AkHn7vZG3R_6DxHFfLHDxVu2OOPKbA8E_zh7Db7m_T0NCjZakjgTxlmaYUSHBXMQpeVtIMtyW1EOpomoY-B17kElGrNsPmNdO4lBqgUmqHycnJQJRfcr9tjvGS1NSCFwstNE_aRfkeB2kFBWFA-SPXlwc27gaaWYKaOiu8y-sUDSUC0hxmEk5wC9YOYQ_GIWi3DcvAw_YTOGpCyW30NoWCIEGoqaKTLf27_fB3zwLvPADm9U3sfl39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كلُّ عامٍ والوطنُ بخير، ما دام فيه حُرّاسٌ ودماءُ شهداء ورجالٌ مستعدّون للتضحية.
لا تسليمَ للسلاح، ولا حديثَ عن الطمأنينة، قبل أن يُرفع الظلم وينتهي الاحتلال عن العراق.
في الحرب ينادوننا أبناءَ الأطايب، وفي السِّلم يتناسون أسماءَ الذين حموا الأرض.
فالأوطان لا يحرسها العابرون، وللمقاومة رجالٌ أوفياء يحمون العراق في كل ِّ المحن.
#موقفنا_ثايت
#قرارنا_مقاومة</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76323" target="_blank">📅 22:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76322">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 23-05-2026
منصتيّ قبّة حديديّة تابعتين لجيش العدو الإسرائيلي في ثكنة راميم (هونين) بمحلّقتي
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76322" target="_blank">📅 22:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76321">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله ردًا على مزاعم العدو الإسرائيلي الكاذبة حول سدّ القرعون:
يواصل العدو الإسرائيلي سياسة الأكاذيب والتضليل لتبرير اعتداءاته المستمرة على لبنان وجرائمه بحق المدنيين والأطفال والمسعفين والإعلاميين، في انتهاك صارخ لكل القوانين والأعراف الدولية. واليوم يخرج علينا بمزاعم كاذبة واتهامات سخيفة لتبرير اعتدائه الخطير في محيط سدّ القرعون، الذي يُعد من أهم المنشآت والبنى التحتية المائية الحيوية والاستراتيجية في لبنان، ويشكّل مصدرًا أساسيًا للمياه والريّ والطاقة الكهربائية لعشرات المناطق اللبنانية، بما يمس مباشرة بأمن اللبنانيين.
إن ادعاء العدو حرصه على البنى التحتية اللبنانية وخيرات لبنان المائية والزراعية والكهربائية، وخوفه على الاقتصاد اللبناني، لن ينطلي على أحد. وإن سعيه لتحميل المقاومة مسؤولية الأزمات التي تسبب بها الاحتلال نفسه وعدوانه المستمر بدعم أميركي مفتوح ومباشر، ومحاولة تصوير المقاومة كأنها تعمل ضد المصلحة الوطنية اللبنانية، يندرجان في سياق التحريض الداخلي وإثارة الفتنة وبث الانقسامات بين اللبنانيين.
إن العدو الإسرائيلي، الذي دمّر خلال حروبه واعتداءاته المتكررة على لبنان الجسور والطرقات ومحطات الكهرباء والمياه والمرافئ والمنازل والمنشآت المدنية، ولا يزال يمارس يوميًا اعتداءاته بحق اللبنانيين وسيادة لبنان ومقدراته الوطنية، لا يمكن أن يدّعي حرصه عليها أو أن يكون حاميًا لها، بل يبقى التهديد الحقيقي والدائم لأمن لبنان واستقراره وبناه التحتية واقتصاده.
وإننا إذ نحذر من أن تكون هذه الادعاءات والذرائع المفبركة تمهيدًا لاعتداء إسرائيلي جديد يستهدف سد القرعون أو محيطه، أو يستهدف المنشآت المدنية والحيوية في لبنان، فإننا نضع هذه التهديدات برسم المجتمع الدولي والمؤسسات الحقوقية والإنسانية، التي باتت مطالبة بكسر صمتها إزاء الاعتداءات الإسرائيلية المتكررة على لبنان وبناه التحتية.
كما ندعو الدولة اللبنانية، بكل مؤسساتها، إلى دق جرس الإنذار وعدم الاكتفاء بالمشاهدة، والتحرك الفوري على المستويات الدبلوماسية والقانونية والإعلامية كافة، وتقديم شكوى عاجلة إلى الجهات الدولية المختصة، بما يضع المجتمع الدولي أمام مسؤوليته في لجم هذا العدو عن عدوانه وإجرامه بحق لبنان وشعبه.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76321" target="_blank">📅 21:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76320">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
مصدر إيراني مُقرّب من فريق التفاوض: خلافًا لما تزعمه بعض المصادر الغربية من أن نص ما يُسمى "مذكرة التفاهم" بين إيران والولايات المتحدة قد تم الانتهاء منه، وأنه ينتظر فقط إعلان الطرفين، فهذا غير صحيح، ولم يتم الانتهاء من صياغة النص بعد. لم تُعلن إيران بعدُ…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76320" target="_blank">📅 21:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76319">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c58Odtx6ufx4XvkpZS5p8gywpRUVqS8tWS5wneETMzuWuf9UxsKo0juW8UZAzYtLnbBYX5FevRnmPYoqbkxDBWOja7ZrRXIoJZ229uHyDtOpPoEvp7kLxWoh8o4B9KUFB_vK1gyqwsXe3svXnWiJt6d5NJPBd8_eBkKo27bZ2QSlHsclKDYKIYN9CArHaHMNhn2OvitSNV3u8Q86QsGg3x9LFzpyyYRCj6lcayekTvpiCQxaXmy8Epec6ymmHNMAyot-C3GOVTMEoiZqIdfuupmlgAF8e8JxhP9Efun2q4lCXJ3kshAnjwyydgAW78JinAk0wefsOGfjbioBDyykyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
🇮🇶
🇮🇶
اهتمام روسي إعلامي كبير بزيارة الحاج فالح الفياض رئيس هيئة الحشد الشعبي و السيد قاسم الاعرجي للعاصمة موسكو ..</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76319" target="_blank">📅 21:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76318">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
سي إن إن: ترامب يسعى للحصول على المشورة قبل الموافقة على الاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76318" target="_blank">📅 21:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76317">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/76317" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرايا أولياء الدم بالميدان
#شاركها</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76317" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76316">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بيان هام بعد قليل لا ابو مهدي الجعفري الناطق العسكري لسرايا اولياء الدم … لذلك نسترعي الانتباه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76316" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
