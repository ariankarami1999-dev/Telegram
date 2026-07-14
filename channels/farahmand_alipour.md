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
<img src="https://cdn4.telesco.pe/file/fK0MYDSoSWZ-TymrWo9Q_SS-a8_1hBXJtXZ-9rBexyPzmuLj4BlAUOeSuJH-neyBqxGgskQMU3Ff7utuCDaMchqOFXmRkuvU8gPczLmRfU7TVSGXBY4lixzRtegFewBiBn-XBIE6eKHHWTPXYccfS9lgM5z70GazGURpBXuqjGxvIdz4gEbyHg1DuNB3eGQmem7rvi0eUUeFBXd6_aeEEFHvtYGtfaYGJFSKRgcphagevrLii5A50u9_lT-oVWKUQ6ZAPruzMiwgfbYkSbwC-bLHbZCPtCvW8WW0mprsMhMwHlMN5tsrIHw3xDsQxdeQrahi8bvt65OiRRe77hdPzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 16:14:42</div>
<hr>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://telegram.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-cfYJQNLiQhORzcP8Yw_97m9JovkSFq8nUOZxJpTfGXIMupYO6eNxllsMiVEPfWEaKp7AwRPa6O23oe71cTJkd1DmuMjcGvCUup3qc0skYAWlaIgz9RheD7BvR832qfbgBNp4Pp6f_vkBn0yJXBvW0AXykzxmZt-erxBEx04mF88lip38kqomYJXPPTjTLTBOCvWR6xE5MNiKDDaxNscdxf3imM2gO4D_Ujm0oYHCAyQLYladGlSolw22O98SnjFgFUHJl6MFVZactJ1jtVWJt-KH7cxdViRxenvlpVCbe_l4Ibbc3fx_r2enx1VOJP7U26x2oLbXzoKwHhX1dnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://telegram.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
حمله به آبادان و ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔺
امروز سه‌شنبه ۲۳ تیرماه،
در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان
و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔺
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه
اعلام خواهد شد.
🔺
جمهوری اسلامی در این ۴ شب و صدها مورد حملات، هرگز اعلام نکرده که چه تاسیسات
و مراکزی مورد هدف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://telegram.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=GPLQnmigjpdwyJSJiV6t-uCx4iG8dazsXwaNZrTBrR1i2Onv59IFIl0XVLC4J-FmMAI6mODeNxTVvryiWAE2Ac5QcbxunzyCtadWZl__OfyTNWt4YH8316m3fYSe9czc_kmAqmmNKH3--HD8_l2CPu7MaFElHBfRxXkdtn3r1ouai-HfqROe2cQjFgZJEA-L9RwD2y5kZjQLe9AxPRHJMJSfdHA3pzpDOGk3mZo81HugC0dpgIc8v99-0RvIVj7lydSAn47n8VZAUjn4NqjbrRd8oAwN1NbTW_NIQMV2qw1u8X-OB1fKYoggAnM9PpJybLkeOyq5dOt9iKR093BjOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=GPLQnmigjpdwyJSJiV6t-uCx4iG8dazsXwaNZrTBrR1i2Onv59IFIl0XVLC4J-FmMAI6mODeNxTVvryiWAE2Ac5QcbxunzyCtadWZl__OfyTNWt4YH8316m3fYSe9czc_kmAqmmNKH3--HD8_l2CPu7MaFElHBfRxXkdtn3r1ouai-HfqROe2cQjFgZJEA-L9RwD2y5kZjQLe9AxPRHJMJSfdHA3pzpDOGk3mZo81HugC0dpgIc8v99-0RvIVj7lydSAn47n8VZAUjn4NqjbrRd8oAwN1NbTW_NIQMV2qw1u8X-OB1fKYoggAnM9PpJybLkeOyq5dOt9iKR093BjOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://telegram.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1f61vL42ySxQn5kYMCloRcoaUAkfAtXCjC_lNTA0zTKTDWkOQy_ZWZfgmhenzwH7EdwIPX3IUij3OHPCgMi2KDQIiJ33IS5-eZECTj7rLA8Xc4TO8Eke7v2MO2dXSL7Wz-S-Uhvl9BAsodrP8dylVH33cX8ktvdGZmshCvOCD1J7X04Dl98qBTAA3sHfUTTIPB7YT8PRVflBfyS3LHm5ihIH_S14XgvhZcEpTbJUbBUviyq8e_Lk3AaSCkCSSrvGiRylZ8fKHkdB14aHaJGh1TvjV_oyJsZEcmpe_kVlcAOwz6Dv59yJsV0qQUAH-YXt7R1w6XROe7UhLx9z2nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://telegram.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://telegram.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge21nCCb68rC7OiRrhNXHZSaBmAekuVYVy-oHMedOGNqVdINDTM8aFLq9Q5Sfg9-BHiDMC7fdCHNH6Pk-pOmRJBvFbjAR_821w9FgnxgRR7-wNblk7yMN9ITc5kBIXUp4JQkv0Df_QRg7BI_mNI8IaM_foIeG5uLsAe-30y-hc71Q9m9N9VhLHULsHF2QRuULbeKlJKyfxrJhRS8JtAc7qWVZo1Usgqo4A85HY1nL8JYedcRvIN3lKJmtNoGJ8CZ2RqScQ8rpBVr0043Q5AdQtycLWZuzlI6pyXj2bh4BN3qdWy6fNTvEjRqtlirnEL9AN9xy8uHpJb1XqJ3Bsk_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.
در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!
مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی) نیز در این حملات مشارکت دارند.
🔺
دفعه قبل هم که امارات در پاسخ به هفته‌ها حملات جمهوری اسلامی به جنوب ایران حمله کرد، مقامات ج‌ا تا چندین روز نگفتند که کار امارات بود.
الان هم برخی از این حملات مثلا دیشب، با حملات دقایقی پیش مشخص نیست کار کیه.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://telegram.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=vdb0DPy_eqH4dlYnjprrj8TQjNqel7SOv6ThkDDuD1DoPgySYxyaVE0_hMSjiL5SuQf9cU5lqVDefxx1cdH6Zxkiynwnx79TbrpabzaUgkLf3Gv5HiFZO8R0GW0eTV_7RcfE5QzR1CKzqfY1qMx1Td2bj9qV2aqJm4NJV58G65hoKViUxBwZv7gh8398k-VVY1JvSsUPi5yd5fumr5DYfF8sNAGnNvDDF_Zzcr69ro47TrElm6iY7su2omaymPXJMrV5CHsEOT93J-ULNtJyVJVtCiGqKzK__mB-787VgTGbmToY6anV42QVxbmNmEvWk8FloVds4Pa7xsnMYlvO6XzjiztmNJgIWJvkvlG0mAkYYQATX7_QkUKJ0EYzlyym7y2mRCugaTLFoM0aQBx1dWJeM-5z5quclj2hGH83GjSYhYgnFVfrUCqxBzhniLtFMONW1XzlXKju64nGn8ZP6NFP-05CL-tLL6uBVNbyCMCHMZWRQTp4_pbqv37l6Bl0YvGS9LYT3tlR9VLHYDOM7QtuwAsIB3cAT4DzJKsJLSF1OL6qjmlq0HbpCaCIEsR7ldjC00B92kS5ecqTh_hNaJOwsH9LSr6HNUkcXop4RjfbiEN-Wire812BYoDWm2Q9cIfcqiGrNCK3Y2LSuxZf4uv7nmORCYS1CNL50lAtaqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=vdb0DPy_eqH4dlYnjprrj8TQjNqel7SOv6ThkDDuD1DoPgySYxyaVE0_hMSjiL5SuQf9cU5lqVDefxx1cdH6Zxkiynwnx79TbrpabzaUgkLf3Gv5HiFZO8R0GW0eTV_7RcfE5QzR1CKzqfY1qMx1Td2bj9qV2aqJm4NJV58G65hoKViUxBwZv7gh8398k-VVY1JvSsUPi5yd5fumr5DYfF8sNAGnNvDDF_Zzcr69ro47TrElm6iY7su2omaymPXJMrV5CHsEOT93J-ULNtJyVJVtCiGqKzK__mB-787VgTGbmToY6anV42QVxbmNmEvWk8FloVds4Pa7xsnMYlvO6XzjiztmNJgIWJvkvlG0mAkYYQATX7_QkUKJ0EYzlyym7y2mRCugaTLFoM0aQBx1dWJeM-5z5quclj2hGH83GjSYhYgnFVfrUCqxBzhniLtFMONW1XzlXKju64nGn8ZP6NFP-05CL-tLL6uBVNbyCMCHMZWRQTp4_pbqv37l6Bl0YvGS9LYT3tlR9VLHYDOM7QtuwAsIB3cAT4DzJKsJLSF1OL6qjmlq0HbpCaCIEsR7ldjC00B92kS5ecqTh_hNaJOwsH9LSr6HNUkcXop4RjfbiEN-Wire812BYoDWm2Q9cIfcqiGrNCK3Y2LSuxZf4uv7nmORCYS1CNL50lAtaqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://telegram.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://telegram.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_kWza-Ol5frBCLnmexrS8u2AGjYT1ApPyNVoG9lA7ADKY8GXUqknQoT5TwQOHsXDVVVZR_9EcdpFYnYBtCyg4LFBNWNyyR9utQLCD1so_xACpttTuWNYYtvQiHkoT_juGVOg-wQ4YMu8dZ10-cYJ29au0z9POgXSGSDbP5Z4MUdPzDuy_Q0smSjBqsXrdV1rpjViaKFFJMKYlfsakYct-xMYOfZC_6AEsN9texy1-zCWxLDyzO6yaIzIEm2xEaB59HKDVcAEjomeM0acaBljhotP-2A4_x5l91AX6BbrO7RWr9naJ0X3RfVrmoKke3kKi3AkcKEB2jmVT8Ko7VZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://telegram.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV7GH96eqBzXzYIjklO9g32erecuA-J-wxmTE2Ed7sXrupmkfd8nfy5wJ9UlZABFNUVsiZvpOKBAmKlQFiOUBT5DFLG3q5sKSjYBc8T2uRdIPngWAFH4WbzV1tfG4k9oDKCw3IHn9unnW9HTKCK5GjIkCzFbyxVZE6IGr0sRmf6oyIlgaCA1Moyt_ZiYDTN7756uoh7-DST4D6q9Iz3QNdtTBS0atJ-LRonzhe9tJOKOOD56JZil9v7RT59iQntX3CAkyA07BybEyD3al4CEgxNvbJMdIfkekr0UXANVdYYt6W2pokXWWPFWfeRmQT_JIWpy7xYbKJgM8skkaERLqUt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV7GH96eqBzXzYIjklO9g32erecuA-J-wxmTE2Ed7sXrupmkfd8nfy5wJ9UlZABFNUVsiZvpOKBAmKlQFiOUBT5DFLG3q5sKSjYBc8T2uRdIPngWAFH4WbzV1tfG4k9oDKCw3IHn9unnW9HTKCK5GjIkCzFbyxVZE6IGr0sRmf6oyIlgaCA1Moyt_ZiYDTN7756uoh7-DST4D6q9Iz3QNdtTBS0atJ-LRonzhe9tJOKOOD56JZil9v7RT59iQntX3CAkyA07BybEyD3al4CEgxNvbJMdIfkekr0UXANVdYYt6W2pokXWWPFWfeRmQT_JIWpy7xYbKJgM8skkaERLqUt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 22K · <a href="https://telegram.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=hfRSnnbkj_HzC68nSfnbs963_4hK2ggiFjJJG75xUFcdfIIMWpK-U2_vyiYPKrVzLr2XAiYoTpeUWPIdK2pqoVyhcSu2wYUvaEB7zxhueKhQ2b1prH1NCD0-3u_Nc6jNnA5o1qpqwuWh_sZ-b-Gr7Lfsie8zFypXe58IAoWvKqTtMxuQzqnlLPB-ycnF6L4gGT01yaptfGoDCIrvnXJdNNA-oJ6X1BzQ59hWpr20w3Jmo_MeDL2Jeji6H7A6TedWZ1p5EpKWnZgN_qqJDsZJ9r05qbCq146AUDLusBHTCcFz40WTNZs45bPa_3ZN6tKDFl1zYqToImBJH9XqsHzMXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=hfRSnnbkj_HzC68nSfnbs963_4hK2ggiFjJJG75xUFcdfIIMWpK-U2_vyiYPKrVzLr2XAiYoTpeUWPIdK2pqoVyhcSu2wYUvaEB7zxhueKhQ2b1prH1NCD0-3u_Nc6jNnA5o1qpqwuWh_sZ-b-Gr7Lfsie8zFypXe58IAoWvKqTtMxuQzqnlLPB-ycnF6L4gGT01yaptfGoDCIrvnXJdNNA-oJ6X1BzQ59hWpr20w3Jmo_MeDL2Jeji6H7A6TedWZ1p5EpKWnZgN_qqJDsZJ9r05qbCq146AUDLusBHTCcFz40WTNZs45bPa_3ZN6tKDFl1zYqToImBJH9XqsHzMXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://telegram.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://telegram.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://telegram.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://telegram.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://telegram.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLs8ji3SRbTfV3557QN4F6aIKnmRJizshBzGZZCrlXmIqjxIYWo6YPMU1hD-7WwAJ1qbcC_6H7868CPlQs8AgoOpAbh38w4Itb-5qlooMxNny27vR0WkF2kTj8VSgP-x1Oqo7UHfpyBIGenNj7NDWHtaIaTuTALV7JORH5U3jToabNGZc9KKQ_8ZwGviSs1ENgKEXTXa5Mcd68CDsGK0ltsqx3S9JCVMvSgYcYsSIa4JOXHwKt8TMU0XTXZGANQ6oxcdFTUf-W890Vgn61_RXyi5SYPaLF3FWiEHcWZIDSi-CU1ERfewGmyh5m2-3Erfj0_IGFcW1EohBt6DwK9miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://telegram.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=UInfzEqdhosexGzjsDt-5A0DaXq79q96LwtLsdMXGq27tFA4j1CmS4HomaYpSPzu3KoXxCjYFGyp-wsqF9nPZ-7-PH4Oyy8OWNr64TgYdFq9sDGmsTDDFfcwpCZBMOwU8idbT14sFdw78Tkle7B_PoookUISOP2uZXgPqWa3dADcihmRPu3JLU8G3UaFjplPbOWHb_0DYroxslw1tCdU9H3v_8AKWf3irBAl5mAOPGfTpjXOg7Ikwn72r26XkZYDPctzJY5Y9f6mLq_43biOC5_EOdffhtcj-qQkhwkuEda3dPl_60myPSaAwxeyquHmSEauFdsKeM84jWoZbf2KUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=UInfzEqdhosexGzjsDt-5A0DaXq79q96LwtLsdMXGq27tFA4j1CmS4HomaYpSPzu3KoXxCjYFGyp-wsqF9nPZ-7-PH4Oyy8OWNr64TgYdFq9sDGmsTDDFfcwpCZBMOwU8idbT14sFdw78Tkle7B_PoookUISOP2uZXgPqWa3dADcihmRPu3JLU8G3UaFjplPbOWHb_0DYroxslw1tCdU9H3v_8AKWf3irBAl5mAOPGfTpjXOg7Ikwn72r26XkZYDPctzJY5Y9f6mLq_43biOC5_EOdffhtcj-qQkhwkuEda3dPl_60myPSaAwxeyquHmSEauFdsKeM84jWoZbf2KUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://telegram.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://telegram.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=JeejeAdMdS_Rk3rLM9C5RPUsWcc9tyQw0tsQmnUr8owU1DjOmJ93yihGy_IhwFqtKFz1JqZ6vcfhE27FZZrPOtdhXtYXF91jmpMJdO4XupTC4KCqGhMFK5O08y8UchbFl1nWRiXKMK8a86BZYCIjBs4wHp-6LOe7J-B6nW_gQ0MvdF7JQJ3WzNLSxSv9QfuuOUC87GGafr4exMenpZ_tZO10xQRtkzwflypnj5ychppOYcjnRu93ttrunUOhsWeZIUk1rbzsB7tVoELUb8QYXDSFcp8BT3pZ3l7xyrfKDEBP9Qph_wn28-NRpg3wRyBcCz70MIoMMEytUS17L59seZRRkX-nLao518hIVkHZOqrdnU3rKf4uHJlYoLnl6GWyOSrLLcRBwo8_OEJY0IadGHgbCHcjxzOVYQLvE2gS42tFFnsR5esq0b4pjpTbZ8-AIH9JKDSu_zgOjFSDAZg7vO_cdQK11aBAzkSf1AsIP3nN5dxkrSdlWbkZUfLbIOMVSH3qK1ANjSq0YbmdAfsmbX4llkzks1EI1dsNxbgxL399q2mcTUbEKyTY1DkJ51Pcd9hGxqvvI7LqRA-cXD_XGPgtcmYDKQD8eCilszgJP-pGw-VfsHFDd_nEHOlpdFND38_HHYAicJ8qwuf5MrKDOqTqIEqRXLJWXLSyvi3TgXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=JeejeAdMdS_Rk3rLM9C5RPUsWcc9tyQw0tsQmnUr8owU1DjOmJ93yihGy_IhwFqtKFz1JqZ6vcfhE27FZZrPOtdhXtYXF91jmpMJdO4XupTC4KCqGhMFK5O08y8UchbFl1nWRiXKMK8a86BZYCIjBs4wHp-6LOe7J-B6nW_gQ0MvdF7JQJ3WzNLSxSv9QfuuOUC87GGafr4exMenpZ_tZO10xQRtkzwflypnj5ychppOYcjnRu93ttrunUOhsWeZIUk1rbzsB7tVoELUb8QYXDSFcp8BT3pZ3l7xyrfKDEBP9Qph_wn28-NRpg3wRyBcCz70MIoMMEytUS17L59seZRRkX-nLao518hIVkHZOqrdnU3rKf4uHJlYoLnl6GWyOSrLLcRBwo8_OEJY0IadGHgbCHcjxzOVYQLvE2gS42tFFnsR5esq0b4pjpTbZ8-AIH9JKDSu_zgOjFSDAZg7vO_cdQK11aBAzkSf1AsIP3nN5dxkrSdlWbkZUfLbIOMVSH3qK1ANjSq0YbmdAfsmbX4llkzks1EI1dsNxbgxL399q2mcTUbEKyTY1DkJ51Pcd9hGxqvvI7LqRA-cXD_XGPgtcmYDKQD8eCilszgJP-pGw-VfsHFDd_nEHOlpdFND38_HHYAicJ8qwuf5MrKDOqTqIEqRXLJWXLSyvi3TgXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://telegram.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_FEgegbTtDmpOG-h1cl0tLFdIH2zI0RfyqmLTR-MCNVB9KuDHpnxGOazS-XwQTUgubIqH3mT_AgFeRni3g6H_7yiuMF1yL-nlJbotxfdeQ4aSZs1LR1diCLTSLoGOE9PahxL0VwXh6cdeq0PShg2ekRIwQjtto5dlRpqY0tm5SWFJeyuPV-L817yU5fdpYajUFf8vD_eBB_OszeqqAk38JSWy-FWWWRY9ov90rC1dHcvRBDl8jgqRWa7ELCan50r3KUvGXJlsZRXwIRa1Jedd44vBooWx7dq6zV66hnDdm7KB-Q7ohe0Yzrxs21V56fynDmC6TA3I_el1WfhmcV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://telegram.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gidsmNEnzGcmQ0wpDx0bugY_bOnuxSUlelKEpWvIH9k3urdUSo8KQb_ruYe41N82F7ZVRBCK4wWyNeFSyJIomt4ByZE2Dsv0ucsOVzEKydSS610NigwIB8u9ZH_DzUz30LIxiDYKF1v7uVCJNnIPYtXtXLqaTWbckLjeyL5b9ZJDUV8_K1kU2NA9mi_SQ_G7u2rDF_fQo4xd4yyCUQ7HBKWTsZe5jPWa6hoqGIXeKZ-pzVZZZQdc6fWdZTgqFDw9Fj-oNdBhtLzU3W8vBkYTCt1rc5eiq_BfHrcPoBWVuDoH6iJGM170h5z0utxXr8ITMOlvZfbqaNcHCn59a2FH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.5K · <a href="https://telegram.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WodYqipS_f4drNmmCLsdRxnfGxzGkE9AkTJYlt6iYnbfZzpcem_vZa9XsBaKEOvSAaJS_9P4agq_4HDGsFuhpDnKDi4f_yl20g4i4VnX5VRvRwZjsqeI3k0hYFcBkl_50ci6CaCiwoK5eQSFlUdWVlEC9_fmWzJJII_fcD1Xm4Hli08-szxeI5M5cofnOrv7sczl_plveVieSIP0-SPlVyGO5B6KDtQXtIgIIdS0307oZLj9XGchYE1ovAEvBCtvr7ED8F3pTX_OQ7Mfe51nSWXxp5-fo8oRAYQ8eatbkykGSa_ID3sxuAT6UwfcnPmEOCzsTTm56gLFDpK8GOlyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.5K · <a href="https://telegram.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://telegram.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://telegram.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://telegram.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO3xrhSVk0xlagsBTyJTPeMG8nuYv-PhQ_DAxQVX0JZ1fO2mSKf3EQOZgkr7u79ZrhMnacM6WsULDpKmq-1jNCsSGzN2UV5RkgaOk1tTErXkTMvJXLtkr0lL9eRRjlEMCjpNhhO0aft6BmKGt4HMqusRAKRv4pbbzxLt89xCF6kYfq61ytJODqwv9y5fvKBZMlmQeLY9Eil9J3ixS8Mo4lLq7AG38ZuNnHu6v6vDGtr7meO4PIgKnOtNSVgkl23lm9OLDcUr78XbtXe8Mah0z5Kn5ECjQje6zxAoo1Fx-zAACuHc0r2WcgJ46afxtVkl_bPb5vuws3-_kqnCQ16RmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://telegram.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlaqHRaLe5_ROu87fS2EYgKxR4y8RjAhcH5XIQSQqD-zuxkLffmU2ErLmHXKKbeLPRLmYmeW9hzKSa-191zLhe3TiONNsuMt_RhalycNT1KuT9TI2BmsgnMxNWkQHTxBUvReur7VRVOHLbLgAoXQcjom6csfGx5Cd5XjAanb4ptebEC1eRDsz490b0RJt19w2ik4kMpyOyZ_HI0dzARtIFmtoEAQcLu6UNBRGo095rvg_aXeOwgK2ImrL3yYZfv_QdFd_H-XE49zr0ql6DxZO3JaBWMHMyy-bU_z-PZ8p-dSDC7Us9gNkntZHmjzKzIzsv2hkv7ieMF9sEUgPrTmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»
شخص امیر قطر به تهران رفت،
همراه با نخست وزیر قطر و وزیر خارجه  قطر،
اما برای خامنه‌ای،
سطح هئیت قطری به رئیس مجلس
تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم
شخص خامنه‌ای شد!
از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی که قطر برای
خامنه‌ای و رئیسی قائل شد،
خودش به تنهایی یک توهین به خامنه‌ای بود!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://telegram.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnnoU16QgmLk7WSY43tVHMidl0w84CsGQ14suw20a-DgrFWcg1gPAZQMxd6FkwVYgdF2lH6a_6ReLrS6tkhEhm_NxvXQjrh8DjdyHNs3TSMUc88LlNUM3zDm5Hyvc_E_mTG5uOZXYR0_u4mCOQVJooiMv-cDeVw8JCI_oCFBjC4G_0IOeXl78HfYHEgJgX24W-zrYew8W1Qio2OuCCCs_qNaPXkGTohW8Vvp9FQDuJpQJdqF-1Q_WatZeolbVaADETsraoONKY4wLTKpgu5LU-sXBeTnrGkDlXXjXEsQ22f5z1mRE5BKs-i9eC7Eegc3cSGAx9e4XhWVqtXyoGh6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که در دو روز گذشته
توسط جمهوری اسلامی مورد هدف قرار گرفته.
عمان، قطر، بحرین، کویت و اردن.
عمانی‌ها از حملات جمهوری اسلامی
بسیار خشمگین هستند.
عمان همواره یکی از دوستان ج‌ا در منطقه بوده  اما حملات مداوم ج‌ا
به این کشور باعث شده تا سران این کشور از ج‌ا خشمگین شوند.
🔺
بعد از اینکه در آخرین روزهای جنگ ۴۰ روزه نیروی هوایی امارات دست به عملیاتی در جنوب ایران زد، ج‌ا کمتر به امارات حمله میکند.
🔺
عربستان هم در میانه جنگ ۱۲ روزه به طور رسمی و جدی به ج‌ا هشدار داد که دست به حمله متقابل می‌کند و ج‌ا نیز رویکرد خود را تغییر داد
.
🔺
ج‌ا در هفته‌های اخیر بر بحرین و کویت  و بعضا قطر و عمان تمرکز کرده.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://telegram.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qnq-GMhruKiLxP2II9pWUtqNcAwyzbxp5Cy2_rimt_3y7UkrpRRjUdqNZdRU1fGJ4SXncsaejflH6ykBRgUp-9Id2-Ru0BwzRQStVfKmJRjWmDO3DKXBOy2dM8VqtBETesWbX626r7R837HZMcJn5XAO_C36V2EH280Xt4o0PJ2FgayQiU4Ped5lP5-Mc3JrgtzI14Ui-I4wH9XatkuAHFH4phYetz_vrUWlg9zZFQEFNjBf0zBmz-CgUdtxRSBPGbhBd2H6eNLu2lj1-UAxDnJoUD_PSHqr50dxTgqoiAcVuulQHZ4d9O0cFWBSiwacPuxNFJVcoocYeiUvD5O1gjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qnq-GMhruKiLxP2II9pWUtqNcAwyzbxp5Cy2_rimt_3y7UkrpRRjUdqNZdRU1fGJ4SXncsaejflH6ykBRgUp-9Id2-Ru0BwzRQStVfKmJRjWmDO3DKXBOy2dM8VqtBETesWbX626r7R837HZMcJn5XAO_C36V2EH280Xt4o0PJ2FgayQiU4Ped5lP5-Mc3JrgtzI14Ui-I4wH9XatkuAHFH4phYetz_vrUWlg9zZFQEFNjBf0zBmz-CgUdtxRSBPGbhBd2H6eNLu2lj1-UAxDnJoUD_PSHqr50dxTgqoiAcVuulQHZ4d9O0cFWBSiwacPuxNFJVcoocYeiUvD5O1gjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://telegram.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56plPVVRRppRb99U7Klrk-PJL-6jxlO8UnKWkKiqfd-poiVk8voYcMjormJ6DOnJWo1PYzgOhO1ci5ENxBoOxItjB14UsudWh5H_gnWoK6GCEBCkBmoRJAn-q2LJfXPkOv8TISMNvQ-_lLHfPqJTZ-7HaGG17Ku2h8W8r-SqUAx1HuBELcY9KYkSBT1_QDNchIYH6qZxLEYINNGW2mKVtGQt38eUBlYxAJw6BbpnT2i-bqfatvOnUxfFejpnztMP8ZNsykbgYNZvP000-ysX6kq_BA0C4dB8pzBNxwKjnOSaRzOB791GV7RdFxhsbGSrqcsSpQLcauZciw6ahgmwd8bLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56plPVVRRppRb99U7Klrk-PJL-6jxlO8UnKWkKiqfd-poiVk8voYcMjormJ6DOnJWo1PYzgOhO1ci5ENxBoOxItjB14UsudWh5H_gnWoK6GCEBCkBmoRJAn-q2LJfXPkOv8TISMNvQ-_lLHfPqJTZ-7HaGG17Ku2h8W8r-SqUAx1HuBELcY9KYkSBT1_QDNchIYH6qZxLEYINNGW2mKVtGQt38eUBlYxAJw6BbpnT2i-bqfatvOnUxfFejpnztMP8ZNsykbgYNZvP000-ysX6kq_BA0C4dB8pzBNxwKjnOSaRzOB791GV7RdFxhsbGSrqcsSpQLcauZciw6ahgmwd8bLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ارتش آمریکا شب گذشته به ۹ شهر
در استان خوزستان حمله کرد : اهواز، آبادان، ماهشهر، بهبهان، شادگان، دزفول (پایگاه چهارم شکاری)، امیدیه (پایگاه پنجم شکاری) اندیمشک و خرمشهر
🚨
بندرعباس، قشم، جاسک و سیرک
در خط ساحلی و «خنداب» در استان مرکزی نیز شب گذشته مورد حمله قرار گرفتند.
🚨
جمهوری اسلامی نیز به اردن،
کویت و بحرین حمله کرد.
🔺
ویدئو : ارتش آمریکا این ویدئو
را از حملات دیشب خود منتشر کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://telegram.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://telegram.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=ZON7mC1Zxdy84ZYhQ4cpdzwA6r3Eb0bz_Agx9qisML5iu2tWX-oONO98fsA7RFp4j81kCe7_5vQHB5nUdfvqW7VO5TDdkKpB8ew9_jQsUtjMMz1xurpmrqgeRcsJhkemyxt6wpyuwsUeg0Q5mUhvaKqQUXsABb9HgxBszmcaVoQ-hlkpxPDkY943EB2nTVSusbkpatp3UzFJIqIR36MkbChZJX8NOsVAHxdYGij8uoKaxtT11gb9bAwnc5SNiUOZGCNDpUQl9c8dDBn5zsPz7SxsUFlwuqs9JiCevyJoWtTZNJtjUg434ZYejlNHpflbjRFNZ9VTj2dcT-6UWmYLfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=ZON7mC1Zxdy84ZYhQ4cpdzwA6r3Eb0bz_Agx9qisML5iu2tWX-oONO98fsA7RFp4j81kCe7_5vQHB5nUdfvqW7VO5TDdkKpB8ew9_jQsUtjMMz1xurpmrqgeRcsJhkemyxt6wpyuwsUeg0Q5mUhvaKqQUXsABb9HgxBszmcaVoQ-hlkpxPDkY943EB2nTVSusbkpatp3UzFJIqIR36MkbChZJX8NOsVAHxdYGij8uoKaxtT11gb9bAwnc5SNiUOZGCNDpUQl9c8dDBn5zsPz7SxsUFlwuqs9JiCevyJoWtTZNJtjUg434ZYejlNHpflbjRFNZ9VTj2dcT-6UWmYLfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://telegram.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://telegram.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=LvdgKh28oK4iuJb-Yhc8pIIOxvLOtnuutDD9MBpl8OiYf72slI5x_yLYRmhXGXiKJCx1fMeW6RQMi1EpYjiH0Rkk-T9VqjypQYs8Vzs4NtKKWQ96GBJQKOTGBCS6lQCjZyykfqWVZDJLGKsvz-J33VN1g3TXb4viTgqT4_rlVRl_jpnNs14c5ammbxYsDoaQjCNiAInp08Ll1AZnB4ozSdp5-JOOH6Ry4AKooWyGxe4pwmCxwK1abBQAHewbCsVwEZ3LNwIiOnfFzkyzXjE9lwykmLg-9urcZXeH_wT62sKyJ3G1dEEgx7PCPyZoxgJ4iLcfJ9SrQkL_G2t08t4VVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=LvdgKh28oK4iuJb-Yhc8pIIOxvLOtnuutDD9MBpl8OiYf72slI5x_yLYRmhXGXiKJCx1fMeW6RQMi1EpYjiH0Rkk-T9VqjypQYs8Vzs4NtKKWQ96GBJQKOTGBCS6lQCjZyykfqWVZDJLGKsvz-J33VN1g3TXb4viTgqT4_rlVRl_jpnNs14c5ammbxYsDoaQjCNiAInp08Ll1AZnB4ozSdp5-JOOH6Ry4AKooWyGxe4pwmCxwK1abBQAHewbCsVwEZ3LNwIiOnfFzkyzXjE9lwykmLg-9urcZXeH_wT62sKyJ3G1dEEgx7PCPyZoxgJ4iLcfJ9SrQkL_G2t08t4VVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://telegram.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://telegram.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27K · <a href="https://telegram.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=OuAgmcl7LzeDADJV8ZXTa5NflaJap5mh7vxSp5mzZ2qLjej19LjJgbnT-H4bVzxn8hpKxaMXxxOEw1fV3GWBkfzJKm6y0Yj4SLq7DnXVrLbpY4lrHkZdMhtn30t-LW9VMkjwjVcuDPuxx_rCJgk3OeGgd1GZgfbiZru7JEq2jfqwRwnO_Y5IeiKihf3xbYMq6Y8uBfWy8mrqjuZjibKHIybsuGL8sm4_cgkstfhosRll7ob887unNsV9_TfHrj9Hw69ZD4TCQQ21tPMstaqC-eVb4KMAvBcXeZRGm6rRYzWy0PHPk_8L2An_WVgYuAX7tJ1pSdgLbelObEWdyT7yTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=OuAgmcl7LzeDADJV8ZXTa5NflaJap5mh7vxSp5mzZ2qLjej19LjJgbnT-H4bVzxn8hpKxaMXxxOEw1fV3GWBkfzJKm6y0Yj4SLq7DnXVrLbpY4lrHkZdMhtn30t-LW9VMkjwjVcuDPuxx_rCJgk3OeGgd1GZgfbiZru7JEq2jfqwRwnO_Y5IeiKihf3xbYMq6Y8uBfWy8mrqjuZjibKHIybsuGL8sm4_cgkstfhosRll7ob887unNsV9_TfHrj9Hw69ZD4TCQQ21tPMstaqC-eVb4KMAvBcXeZRGm6rRYzWy0PHPk_8L2An_WVgYuAX7tJ1pSdgLbelObEWdyT7yTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://telegram.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=EJST799viuUPv0zhzlC8FA1-PFZ-F2QceKNGehINzSnk4p8Wug75uAkJ-b3S4-OURjFxSmdY0fkUhvjNGspOiT3gNY1k9oo_7TvbH3gwfyzjtheYNj3aHPPNglgL5YkzHoGV--j7QK4NEJIuuSBcilMYFnAAKlCVjNY11-z02HSAqmwGmDkcBI2MrNvtXXuiPonwUV13VzDbdkIBPvuwmXCFRHQJR8JJRLDTTXNHRL1GqAkoNs178-Rqh9OGr_otkDi-vh_1I0D5EyfjdxPplzs-1KNjJEdlyocXvj6HL_2V9aq3eCj85ivgX5PcZPNUwJNroDVZuNNdBeyL0TBh_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=EJST799viuUPv0zhzlC8FA1-PFZ-F2QceKNGehINzSnk4p8Wug75uAkJ-b3S4-OURjFxSmdY0fkUhvjNGspOiT3gNY1k9oo_7TvbH3gwfyzjtheYNj3aHPPNglgL5YkzHoGV--j7QK4NEJIuuSBcilMYFnAAKlCVjNY11-z02HSAqmwGmDkcBI2MrNvtXXuiPonwUV13VzDbdkIBPvuwmXCFRHQJR8JJRLDTTXNHRL1GqAkoNs178-Rqh9OGr_otkDi-vh_1I0D5EyfjdxPplzs-1KNjJEdlyocXvj6HL_2V9aq3eCj85ivgX5PcZPNUwJNroDVZuNNdBeyL0TBh_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://telegram.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNR8iu_V1eV1Pz8kReoGE_MrTvYTrQXe3PK1fusd74aKyJVg2u6AIfzRxQ5t0oW3VpKhpkhPxO7wcZcBrKGxFArcGY5sheEX2bi8Y3xbvcVRXmltq7PBUql0oPKkJXF4VfbPLG9_bk5TGkI8iNDHlcZ8ddJY-irKfMqi2Ekh66SIX5XgO263REsDcJDvSQMK4j-dxWWdBsj70qlgWaQuQdcLPEc0VAhJxaqV7Ka7grfKI1CTb_DI4m5JKmPyQ6RbSCBoW_nPIKkmTYgtkATRQyVoWRf_oyJQsbDGLN8UJEJLGMIypsxM1FGe4vuNKunCMHyQqvEa0_wW2c9E62SawA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://telegram.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtfQdj5FDeNDi4vDV_Ke2BNmYqzB2VpqiGewy8cEF2eJ-rRqinrWHlRxGfKRnrpmnsDGy57RayKOBrctT2gcU00iITDpeMSyjkf2K1ZdlkoVV1oDmntw1mosyF6_PY0Eh4MpyKiZr3P8-cEAM8CW8Y4C5Ze3cNvCcUoozQCaYOZyoO2v1qyBGB1uFmdAMJ0-uhEkc4BKBZr_Qxes8vnQj7FiX4x70mB66rEpEx677JYxCN6jrfwcSfPul3j1oi4SjJWV9rRlZ-PaPKk9ukpi-MUdoxYN8U-DbwCzB7LMCa41SN5I5CLazJNMHGF_70CqOOJ-eg8Yj97dV0j4c2KDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://telegram.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=IpICL-UGIDLN76WHYUC5ooGv3QPBz2AyHLyxh8QLJIxFZRLILJzFh7thTSbSFbPZa1AvoB3K5vcdSmS2nM49viPE6fIDIvNG2AGfenofJ2KBONjP08IlDDtbugrZe_B9SASYuiBUTN6StYNdCatc8UYfnxImshoGznm6EoryJ0zFr0KemP4TcUR0tSRSDwlOdr7QPUmBZcb70Mih95YLQa2qbFpfWxaY5kSoQhTeb7XzeRKQtvujz0on4DZ34UQLg19woN4ZtQQ82Xulc6WY8EKqnz5mmGBhsqu9ul_PKgDDhXFYyrP0ZidWfGHLB-oNes0LgPMYhpl2pwuF_rqsqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=IpICL-UGIDLN76WHYUC5ooGv3QPBz2AyHLyxh8QLJIxFZRLILJzFh7thTSbSFbPZa1AvoB3K5vcdSmS2nM49viPE6fIDIvNG2AGfenofJ2KBONjP08IlDDtbugrZe_B9SASYuiBUTN6StYNdCatc8UYfnxImshoGznm6EoryJ0zFr0KemP4TcUR0tSRSDwlOdr7QPUmBZcb70Mih95YLQa2qbFpfWxaY5kSoQhTeb7XzeRKQtvujz0on4DZ34UQLg19woN4ZtQQ82Xulc6WY8EKqnz5mmGBhsqu9ul_PKgDDhXFYyrP0ZidWfGHLB-oNes0LgPMYhpl2pwuF_rqsqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://telegram.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTFAC0PWA2Ec7I3_jzku_TBBepLW_PyH2zI2L-nK-bfyoTQWbEae9cp7LrG-DY6swAvKJXOQzHK_LkSGbCOzmBPyfmPNO3zviq41qpf21WzHT_kq4sZUhTkJJbVhwVN0MnEuBoP4opSxQMAJdtyUA3k7XL10KtfuorpqdaET9NqztjRBBClZ7S90lo1r3JX5oX1y0dtNIY_llqDF365hR1H9RufcJ-JTMGvNM2PoltfwnLMdeUN6WmreRUZ48oR5lr-82IL1f1H0YE18VJO4S4L7NDnFL8hk9Uk_Af703meuIBJkWoPpyUBJu7t-xpRwmBExTmySaYJQxCgdyy3VkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این لیست عاقبت و نحوه کشته شدن چهره‌های اصلی که در کربلا نقش داشتن رو نوشته،
خیلی جالبه، چون نحوه کشته شدن اونها تفاوت زیادی با نحوه کشته شدن افراد در کربلا، یا ائمه و… نداشته!
یا با تیر کشته شدن،
یا سرشون از تن جدا شده،
یا تشنه بودن و کشته شدن!
مثلا این رو نوشتن که ببینید عاقبت اونها چی شد!
هیچی! همون عاقبتی شد که مثلا نصیب بزرگان اسلام و شیعه شد!
مثلا یاسر و سمیه چه مدلی کشته شدن؟ به مدل کشته شدن سمیه هم میگید عاقبت بد برای کسانی که مسلمان شدن؟؟
در مورد یزید نوشتن در حال رقص افتاد  مغزش متلاشی شد :)) از روی پشت بام‌ افتاد؟ روی پشت‌بام می‌رقصید؟
بسیاری از تاریخ نویسان مهم و اصلی از جمله «طبری» و «ابن خلدون» نوشتن مرد! نه در حال رقص و نه متلاشی شدن مغز!
عرزشی عقل نداره! با عقل دشمنی داره!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://telegram.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://telegram.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=Scny3tIXPOY7VcrRoE_kdKGna3nq3uHW_MPvs8L0TQdzFqp8LMxl846cxBq86Rh5q0TKTOBECNyC0_WgZmXZQRHgs4ux9m65w4rLE-DQKzFe6mh2s35FvmXT34AnXWYTgCR7X9AX_Frahyr0mOt2F011Ysm77J3zpJ825-scTAmkmQPEoo2mZoz_rvKlgKZfAjJT7afHjhTr8_6QJhJcjT4iFx1IwCMLTgz5NhmyTbowa_Jb-yrXj9Rekjk1BwhX5549mtmyboOOIggsV6852T4-pzhUNWB6VxHIShUTmw_anxCSV69EiwFYMrVsO0c0NLiYTVSvgqQq435PauHHvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=Scny3tIXPOY7VcrRoE_kdKGna3nq3uHW_MPvs8L0TQdzFqp8LMxl846cxBq86Rh5q0TKTOBECNyC0_WgZmXZQRHgs4ux9m65w4rLE-DQKzFe6mh2s35FvmXT34AnXWYTgCR7X9AX_Frahyr0mOt2F011Ysm77J3zpJ825-scTAmkmQPEoo2mZoz_rvKlgKZfAjJT7afHjhTr8_6QJhJcjT4iFx1IwCMLTgz5NhmyTbowa_Jb-yrXj9Rekjk1BwhX5549mtmyboOOIggsV6852T4-pzhUNWB6VxHIShUTmw_anxCSV69EiwFYMrVsO0c0NLiYTVSvgqQq435PauHHvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27K · <a href="https://telegram.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnkWQA_6xfll6TJoRw6yPZSBptWOvHfb-zvud_v22zpG5StT3rIaaE6mBdFQwJnHTJsoOrPpRxcjZfxj_6ByJJ6srSDfEbSmulOfEniIa0XpHv-WUS0XP2Db-k3YxrEl8CGYHneqBSqe-g3l0INJs8NlAFsd7FOPmMJMeOnEIKehIu7Vcw9zPPl0B1ZDZVOyFruvMuY55DSeANi800m8_EsphIVpE1er3YrfGeq2ODvM9hempS9xJ5ggI7A5UZnKVOakJG0H8jGy6xxN2n753hKvzkNVMeFM2zw4rYoEzv3ZgoUfuxMHhZ2_nGejZ0NIZY1vagUvR36plnFMyZGobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://telegram.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://telegram.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyMdPBv8n3vEDXEJ1_wlTox3BJKaBbL4XDqJ2_r4Q88V4GvqDCSkNk-zC2PaxfFNIm0VdN8tJkDcG8aB63xbYbRmW8-ZQOkq8MLozQqZVH24rkUzDbEASJk7GcqnaulWXaI7JHWqHVwooKDwlmnq0EBvjPwk4ViM2f5h4D9DRz2FhCnee7bQjJ-YCTALEnNzmSUH6GLZa2IShdJnF3z1c_k2YZ2PYhyRPfRdDdgAGvrhZWTPVuiNfWcs-YNRFRr_vTbFNrKJKyWdgdsWeMzeafg4IZHfpd7gs5fljzJ_2sUUUkgP5aDboXlRvVWSXwBs-gmvbzgsJ_xRTG_X1Y0nHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://telegram.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkTJ64C7TFED9-SOxBG_pzFeWeU3dJtozMlal70RT2Kxp8vJRfUcDSHTUkm6qAIRu-CB2mNYFKp4RnTdGrJjQh4tGoZ7NXDokKXZ4iegBmnaNMYr6p18QdNjqc3jXYlFLQMNixrshfE80F6fdL8pH472YKeyJAnUYPlNdsfH25x-a9imAG8x-4yXCvZ766P0SMjcd1ap7y61HXLEfGR5L3SuINw3kaJgcLr0lmw_sP42YccMt4rz83X9lb7SjrKiw1NoX1sMxLtNIU9W9mDx_EvYuYzgchieCtJL1SE3DtIalw1kMW3fydR5B622gkcSKbbJa8zb95PrsmmXnsT8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://telegram.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3mGPpSdwPxMAwtquY79bu21GV9FRttbFGb22eI9F7ovN-TDiORimsdLkG_9ur73BoGRW8vmTKEOnzqGqi6_RvF0WccukCOG6hCOCe-DBcS885F--2kM_4VYiL6UkHxr5jsyV-lAAcQvbDpG9J4qo824-pO6GMe-tgUdgF4E75o6DdaV_UAlSl00AatsmMswZztFqMchZ6Gu1pAwJbj0OUr_M5BHgInmG94XU7zFeiUYgR-VrDmC885AjEqRqTs-jhMnhFzYtaBi2Xs7c2aJossk1KwKCziqyY1LPTZdcxAg33FRT84l6MUpC-45OkwUAeWya-W0O0BbiFHzu9iZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23K · <a href="https://telegram.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtZEEGqZz4c0VfTH_fpeW5_63y8E5y88ti2XOdlj0EwQy63mRdNEROmz6LVhtPopa8gc8Pd2L9Mv_5JWPDel5l911597OV_cXRD-nI3s4hBd05IWvU6EqWVJJYLVpZo4ykyq5GwAD5vkEonvo_wsQvnT36aaaZe9iNKq525FB8LC6WMBPyYuTmN7OaqIjWrc4uJ4cPFKsyBHhrfgor7mqa4DBs6rU7iyO7-4WV1IMA8Jui7pKToz1TOcrpedfxV3QIcJcHjZrp9jVgrf9CVeBXuOvZRUugDnNYpzYFBcYMB1ARcBTteuh8wEEE24gNRZKO-ZrC_ubKlL84hPoQOpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HtMms-Z4q9u106Cz4aBVg3APuEkCG4FV5BatRtNViS5FoPVyDSfVjve-1K9D3DpPBWHMXLVa5h090nFtFj7b1PNbfbPqLI98Wje89kqRYvLk1zCnyH1i2mvtG3jBktX3zs6s7OjMRg7hkXOtg31GaL51PXYH7vGMLN7gjwSlySMmsGMYsdqd-HC7DMqy0xYD9i7IU6aq5oiyiD8wMYbh7UWD1EVT7qYVa3F1NkUlLjMAehRoy1NM5NCf4mpznSCYkyL_6qGBB6__DDORz_lAadvwx6-6hN9jT1zhsRtMln7GSpgDpjvCYjpyh2Q0lHSYgmmsrTWBpt-IRAaCPtkw9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://telegram.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://telegram.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3NgXx8SD5EkQR6eCXNtj423_UXlYmt_WhFjei9B0S9PcHgqADaW7PhQqwKP1MDBAyjTY2M1sRjcRjLSzgKJUoLGpXsAw1Ilzi6ksNv3fVmj7mvTiO-RQJmKiv4fubWbB4Z78AOXW_MY95gzcMEhfYRuwANMsOAwwmvBpebGGcpo8kWv7BFrqO1fQpRlPzUgl6Qc-ZNH5pMTlYaZL3JmieWPZ3QUBwcwR697rh4nqeak8cl82PoRFSFNVrm3JYcgDacuPe4vvLZw2DhZMBkYx-bWnBU3POCmzgNovDSx0cuQ8noV7RhKTdbh9lBZPSWkiZg3iexyx_YSl5aJERe7BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://telegram.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://telegram.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jok5HY18li7KWpjk0M5wOrGnswQTIEyi6avVePAXsvg_vnuUrYRNhE124EDTVMcIYxbSUbhCfD0x3eK82RVs8mLJSXorPgCajViStuJdLreNSOQB0IWWhe2YvWvbxbi-jthegw5U6oiJ6NwC8bw-bnCtYouULFRag3zdYil0iviwrTajk3mwyjSOuBc5mnXEzZNzGYYZ7bfjkaMArtnahWfMI6xCrPU9oDNMoxbGLNSsnhP7GyfL7KbFtoWjS6t95yoMkVm3lLabs0KF1AgLe6i9Q4wQsjV704wGNTncnigQrB1qaGusTSSN953MjKZ4sgDXRCuqgy3lYyiewTLIzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://telegram.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCzO7Q281wOs7Ye8h6PqGSXEPu_NT26ObhnTBP6fzdgQIPj-e-W4NzF8pwHgRyCzOBrIc77jZMFLLdwBjOfB3udoU4mZQV4lx6xBCoy-tOlBx3E2ndQG6jk70KrUyaPc1XDMk1WgZcfgTFD5gxC8d34Hanp8FrMsJjVgebp8sd1yXTLAb-ezkyz5oQATHs9sPMiJbSZeiBTRoxLJZefiGWYUa7WtvfijBcR5GTox9XfXve2UTNb7HDtyyOvxbcG_VOJzYysvy32nW9Mbcvy9tlAIj2rYS-AJPPlq1KghFo_mh2rENd7ZkEC7DBHDn6pvajxNPuBsZ2rwQUxBFaNdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://telegram.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://telegram.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://telegram.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0Wm8fZ2CgSiH65hcfk-Bc1w8XsyEgWSl64Z0O8FUIKyUspIH3U-B9aAvsES6E4RNSLDtfzh54k9tRkOzFAd3AUluv_OYTDHQ-J5Sr6D4ESXaotPe72HKAnn9WuL_GbNoQPzQrjsAj8sf2sfjOOdyJ4HN1YjGQq7FPWMzYMiL47n27q1iDtsL_dpHdEz-gNhE8rCFf6oo42UZeEF_RjMhfK1Vks6qrYRmuH7014A9YkfItnCqBdCgFGfKwt5qx_6VT-J43XhD-1CAOwkoAlYxKzIr25RZUh_TBlBxAWzLbaQeMhqzJaot0deaNcQh-QnoRh7S5lM96-sJOi3SmJXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://telegram.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cb-MNLVF1MzRoXu5ErDkUd6Bxbn-1ChLhHHG8U6qXs91yT0uH0nukMjXbZfja0GPB1ZfREXy3QcT15yuhlAt-_VVyrha7kUrWFskSQxaZ3DbGVaTsPv6kH33LNTsYUt6PLvyvjviK0qSAJFpwUqWrHa1KTtM-zktiTYtDbcLrvjcPm3nH-iQg_zdddcAAMymVVUtwCbfreyltAtQ_qkxyicDuAxZlNFMMqhz-zZnxDIwba5HK8ykJJY3EjrFkJORMYfS0fGF_yNfR6DJ_46I0nci6F_vqtbAbPfA_VNwC45928TJtCJShL19modBBr4WRK8tJVoWjmip3MLenX7iqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://telegram.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 23K · <a href="https://telegram.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://telegram.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://telegram.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=YqnW_1TSgZ0ufgO8cNK0PIpltKO5HME69EGt6vaC2mh3VX-xtuIn-cC8MEAhhaJH5dR3IemZTAdVcTX2Qs20oEkHFz2WINRoQFLSUPVxujgkWX66jiZ58mhtLHbkzkji08a5RnRO8ONvMzu1kbbroR5NnNzMPm9EOAxH8Plzw219FCbB_cW78HAeFyTdA1unaQInXqdM73NSVbnX0xswP9l0efvfLL2I8aP6N3KhCjPDFJ2sPd52qNEotsOIoZbOiwAiVdto0tn9-u79XfX_XN2RD-gdqom40Xw0dKzy0C0berO6YaJYNgLgHfVssuhWISvHIcaOusXKqAl6Lgsfqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=YqnW_1TSgZ0ufgO8cNK0PIpltKO5HME69EGt6vaC2mh3VX-xtuIn-cC8MEAhhaJH5dR3IemZTAdVcTX2Qs20oEkHFz2WINRoQFLSUPVxujgkWX66jiZ58mhtLHbkzkji08a5RnRO8ONvMzu1kbbroR5NnNzMPm9EOAxH8Plzw219FCbB_cW78HAeFyTdA1unaQInXqdM73NSVbnX0xswP9l0efvfLL2I8aP6N3KhCjPDFJ2sPd52qNEotsOIoZbOiwAiVdto0tn9-u79XfX_XN2RD-gdqom40Xw0dKzy0C0berO6YaJYNgLgHfVssuhWISvHIcaOusXKqAl6Lgsfqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://telegram.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 24K · <a href="https://telegram.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://telegram.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://telegram.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
سپاه: تنگه هرمز بسته شد / به سمت یک کشتی موشک شلیک کردیم.
در بیانه دقایق پیش سپاه آمده است که : «در اطلاعیه قبلی گفته بودیم تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت.
ساعاتی قبل، این تذکرات نادیده گرفته شد و
چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند
و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
به ناچار یک فروند از کشتی‌ها مورد اصابت شلیک‌ِاخطار واقع و متوقف شد
.»
🔺
جمهوری اسلامی به زور میخواهد که کشتی‌ها از مسیر آبی ایران از تنگه هرمز عبور کنند و نه از مسیر آبی
عمان.
🔺
آمریکا از جمهوری اسلامی خواسته بود که شنبه - که دقایقی پیش تمام شد - ‌به روشنی و علنی اعلام کند که تنگه هرمز برای عبور و مرور باز است، ج‌ا اما دقایقی پیش آنر‌ا بست
.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://telegram.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjAttHdN4VmuOc9UgsSK_7PhXxQUvLXeLrFqBz25Z-sUazQSkUb4ygOf_4PKFLyf8IObL1lj-jhTfjU8l578PmVV3igfuag2Ju1uyDNpuWMm_OMZGuw6mgRnhlI87unydg1WLbPOiANpplrjpXRjioZjy492nTF2ygm9oX-57Fn6yEmOlWUdhPGzytDElQmJALRJGICNM_W3XVbKAZrurn4HoQZ0FX-_62FKqCaxTOQbfaw_hnsYIUNIdyxk4D6-pLbKodvkmVK3CckarYcYFHjUxeWUiJySVVEvrzqIEWGwH5ojNAFtmRnU818RfWSnh5a_CiM4cNqIB8qQYVY6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://telegram.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=rWl-UECVklXPHd8TmLQHHrNIksT3UQKOM0w_e5dTFD6eZdUphLgm4rei7ujiMjPApc8EM1xyoTFV-1COCBxMZoafXpRNuSknYoX9MGRQO9U7-AJdZdziLuiJ4LqNy0FA5Sd-s62HFUOnIN2GaRaZhtRqeRjR6ENh_PS3tMAliaI4nknqoJ2B_Zr7G7FirkFDcG1HE9mT69stRcaRfw5-AQWcQLcUrh2EPvx03gy-b7blkqz_zHcZtxUx4wenFL4DZG9i7UbsxDNlVegPwV9NYB4cxJcLKG_xnsIHNN8LXCrMv1yrH6UKz8-mMqG3RVdU93pajxKK4Vl5Vn1iXQkoBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=rWl-UECVklXPHd8TmLQHHrNIksT3UQKOM0w_e5dTFD6eZdUphLgm4rei7ujiMjPApc8EM1xyoTFV-1COCBxMZoafXpRNuSknYoX9MGRQO9U7-AJdZdziLuiJ4LqNy0FA5Sd-s62HFUOnIN2GaRaZhtRqeRjR6ENh_PS3tMAliaI4nknqoJ2B_Zr7G7FirkFDcG1HE9mT69stRcaRfw5-AQWcQLcUrh2EPvx03gy-b7blkqz_zHcZtxUx4wenFL4DZG9i7UbsxDNlVegPwV9NYB4cxJcLKG_xnsIHNN8LXCrMv1yrH6UKz8-mMqG3RVdU93pajxKK4Vl5Vn1iXQkoBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://telegram.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CValIJVdaL8tmjjVSyAgox6tlWKjhjxRqsT_1DafnFbPMUSNDUVQ5wEqJp06bn0Mt6atpsrPDHygli6EDRkkXnWGlTNeLe4m538DiIptLdSbsbljPHPqQVh9SfhWf0AbR-GEkg8gDRPLzDbRDU3rAjEe_h3yC20t4P4ryEiLfReW7t7q53I-Pu2K2eVz19fTZjznkaM2G_x592S5VNSc5kMazJUHl9VjVfi2ACdhPMC0MIj3KJY0XCeaWUEXY_29jrATwqlpmPO1rj0507Bvmui0vLp5qgR9yeUHrrvcubpOoeJj_2Rlr59TuO8Iq2CTqB4S5WqF68_D2NAyXVrJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://telegram.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://telegram.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnkeO5T7YDztqV5c2-Rq8Xm7XRP4BYZzxjfhI8e3AtbwI8cjzEfpjgDS3wi6ewvaxPYprBcZ2EWa5mdT_GhODK9nZPsG2TPbzcw102IF_XPZF_nY7iZFUfIpyRsd9Z4VvkxzsHOLGoYFuyYZCHLZlo7eKJVjtXRXyHyEpcHs2nwEShVPiZYcPRM31qkNHEnEeXpaH58eTZR8GyAh756EYsDDUKIUJ1FbcFOv1zDANjelv92hOIFyr27LyasRI7wUGzfiKmhz2HWxir2Eved84m2d3YbyNWLN3Ds8C8V67vo7ISP9LAfiH9mmtJNxzyb-mYb8PAK0sdt2tEu7OHo3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر یک مجله ژاپنی
در آستانه جنگ عراق
که پیش‌یینی می‌کرد جنگ جهانی سوم راه بیفته و…..! رسانه‌های غربی هم پیش از جنگ، ارتش عراق رو باد کرده بودن و بهش میگفتن : چهارمین ارتش قدرتمند جهان!
رسانه‌ها عامدا اینگونه می‌نوشتند
تا خطر رژیم صدام‌ رو پررنگ‌تر هم کنند،
اما این باد کردن‌ها، در عراق هم باعث میشد
که فکر کنن بسیار بسیار قدرتمند هستند
و جهان به قدرت اونها اذعان کرده.
رسانه‌های غربی با «قاسم سلیمانی» هم همین کار رو کردن!
و بعد ترور شد.
تروری که ترامپ هر روز یادآور میشه
که اون دستور کار رو داده!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://telegram.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=lXMAv0cvOrOaYJEdXoR7jj8IcF5lC5BYcIqndhqwfYL2zkPpFQ9Jxv-03u6zrPBGSHvaSY60wHXfghOZB7nk_V8SmF-_kwlzzg0LFPrHEUKU2R1_XaCEbi-DeKkjnzE7wZNF0N5JLQdtvqfjTfMKcxHm2emNcrP8ka8I4mCXLPHVL5s4yWRw2JAt13hEu4KxMGhlAECrrYOcOmTNI78XUMmRWpZa967UI_gT2Tgiwsy9Z9PFggho2YuZLGKf1zB7avYq6snE66u_MytJzoxNBW3RQfsFxKrpH5B6Ywk4QBVkVFvBB5_MGqdIscxVZBndJ0YefO_c5NKUgVYAZPahoxzBtk9Q30SN0pb292vv2an10Wl5AysGt9LjhJEkV-OP6-M23EZVrPCChlfeympjyAT5DdtgG-ySpQsfrjWkLZmX_6ISfshJqds7haQ6YdgGDaDEfVqXQ2bI7evOs6KdzowYo8FjMdeTxvhlFqwrq9lId478p33NqmPZQgBdZGsATOYSL8rgvjJ9ti3zjpgiPP5-j5fEdtRkLM1GYkPWDVxIvCK-MqbMxqOlUM46VhCqlSV2lwivR6o89vxlN--venyw1UZoNnTbpLtiinlxkHzGz_XywFbO5d5QP9Bbs-1RKDvC9gbv3nruZnWAFPAcvI5unoDXXLFcpEllj5b8YoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=lXMAv0cvOrOaYJEdXoR7jj8IcF5lC5BYcIqndhqwfYL2zkPpFQ9Jxv-03u6zrPBGSHvaSY60wHXfghOZB7nk_V8SmF-_kwlzzg0LFPrHEUKU2R1_XaCEbi-DeKkjnzE7wZNF0N5JLQdtvqfjTfMKcxHm2emNcrP8ka8I4mCXLPHVL5s4yWRw2JAt13hEu4KxMGhlAECrrYOcOmTNI78XUMmRWpZa967UI_gT2Tgiwsy9Z9PFggho2YuZLGKf1zB7avYq6snE66u_MytJzoxNBW3RQfsFxKrpH5B6Ywk4QBVkVFvBB5_MGqdIscxVZBndJ0YefO_c5NKUgVYAZPahoxzBtk9Q30SN0pb292vv2an10Wl5AysGt9LjhJEkV-OP6-M23EZVrPCChlfeympjyAT5DdtgG-ySpQsfrjWkLZmX_6ISfshJqds7haQ6YdgGDaDEfVqXQ2bI7evOs6KdzowYo8FjMdeTxvhlFqwrq9lId478p33NqmPZQgBdZGsATOYSL8rgvjJ9ti3zjpgiPP5-j5fEdtRkLM1GYkPWDVxIvCK-MqbMxqOlUM46VhCqlSV2lwivR6o89vxlN--venyw1UZoNnTbpLtiinlxkHzGz_XywFbO5d5QP9Bbs-1RKDvC9gbv3nruZnWAFPAcvI5unoDXXLFcpEllj5b8YoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://telegram.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K01xGz_fjMa4XVeM9vUL1gEmbuAgKzSEnRGPr8kjYxkrxH70FVAC2Ot4grJ7FO-AG49w9V4c0tFpsgzmSeEFrL5WpslvdbOd0jni1j2HdPTDXb5unsSYwi7bQ_Q0URwVDhX-d3Q5Xcjz_x39nwiVNBWIPtoB0J8ba-_iASHHmEZwVQoXutOhH-bIhsqRGhzMaopK30AnGxpSKzTK8YiW0XGGwFp0kSHyLzpC1d4CxjJ44kQw_tge2xqPkB2j9p8LS9azdy3Zx7YjfujrfIVrFffsXy7sFhn7m0VYKNySwTgEHoUGN6kGERfZY8xwSEqiHZMl-eVyuA9MgvnHunWKeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://telegram.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGbx0qz5EuLSa_NL1Mxn90IkUzD36snUVHMflNkIkXD95V20VNFm5ZPN9mFhz4kGMLh6tTwOHbRtkS_XluPl-HU_2bp-uIGTqYM020Sp8IFq7F4VdQh-sSiVay1TMqB1tODPqLwWRW7yzgJDWB_4Zi84pWhuoNNkAI_IhMjwVdozWuaenZlgBaHrJzexTS3kpatrcmQQApSrmZ9lBgzD_6DS1iPoN0IA1pFoUqfL0o9YvGMNIRwA0aRFUkbCeo2kwKlYEzDhHXWYmw3XPfgwmItkBpD3p-DB5uuI5ikIF0Ub1zrn5sLRicEIj6oUcHGerULuflB-agA1bG2NeJblPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://telegram.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpW6Drd_6EzlvJOLa7U_l5buTGAmFyx7VgHfCl5IEqPL6AeiHZfz2EF9OMfqLQNX-aH4yJxwA8Tk-zJzMnBt-MmV-9juWrVw66Z-vOmppaeuYfiT5aGg1X5WI1nBeGtRivwM7LmxeTThQkdT0DyvAiDY5QX87A0Sxk0DLULBZstsZH8nKQ2sUPmf1E-V_UNfeWZq7-rfTO_D9IaNltwOcf4_T41Myz03XW7B-6eXaL1GH56Q-ll3BOq_mcUEqxwvRYwzDmGVc29GIBo6wE4fFV_JrQWaiX8nX-zDdAhL1yrcFEGo65YeYEPBz5wTkcJ0FFOOnjar_Q8LjGd7jhSePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 28K · <a href="https://telegram.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://telegram.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=syRxALB1DVW-Is9s1iAEED4B5Wm7WRkuv-rhb0fywZyuugzM4WRYLInWpSdPNh8WgCMGam1fVXorzXwgNhiMgmj_oS4ERf3ze7d0dMPu8J_f2MbjgpDlCdJ9ih4qqzfPHX8Zpd1ULx9jkhy0Mt5MdtUKxZV02qj-llmn03G32U1O0_diKu7mKqQSjzK74lmOJxtG3ggll2S23H3zHPfYqBFo7IhoeIBomF7AcVY1iD9kQzoa3GMDuA98LmGhmem3GM-RAOV8aXGtel7N_LQwyQTLDWUSMz9O09u1Sws8zACf5F17VYFT7BU8Qbzmfo2Avxpmn5WiMqv_dRhd5qpx2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=syRxALB1DVW-Is9s1iAEED4B5Wm7WRkuv-rhb0fywZyuugzM4WRYLInWpSdPNh8WgCMGam1fVXorzXwgNhiMgmj_oS4ERf3ze7d0dMPu8J_f2MbjgpDlCdJ9ih4qqzfPHX8Zpd1ULx9jkhy0Mt5MdtUKxZV02qj-llmn03G32U1O0_diKu7mKqQSjzK74lmOJxtG3ggll2S23H3zHPfYqBFo7IhoeIBomF7AcVY1iD9kQzoa3GMDuA98LmGhmem3GM-RAOV8aXGtel7N_LQwyQTLDWUSMz9O09u1Sws8zACf5F17VYFT7BU8Qbzmfo2Avxpmn5WiMqv_dRhd5qpx2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://telegram.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://telegram.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeYgDswhlJHvXrlBAWbpRzlExDvoS0PSps7uvzoO5kcUVXe9KEVfGlLTUum4EgGg3-wcpGHfDnjAS3HXguFzdkEx0okMVNms3dA1ALJ5HBjDlIgqRVf53DGPEVAVT6z1R2flQtn3PHbBJ3xjprEoBrN448jIqbGWgsQxajnFEGT6ZWnfbZYY51ELpPTM4XuqIsL2XHUFpzlq5h3ECudUQnuLmw_O5iy6r5Nm3Wi1WuY-oB_WX8492DtcEt5xllbPOyvdhEF5WIUAcBJfzsjP7e5BmLecPq3oqfm2xgLh5A42FT3WAiEc_4uJ4EIePr_0bf-_KG0VKi_IqNg895q5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://telegram.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE8MgWhGTIn6jxyQDB4y4wr2MvTVh9khoyTMRLEAotJ9EiiCajLZNZTM-RaWQb97APeuRKaoK9FJ0R-qtXwIVI_1hoT11Yi-syzO3ilGYcUvhwIgKYdLNzs9xxFxLch-TI8WCu5B9vw9zZKmiE7NWlPxgdJsRgHKR4FUxofuzHDBSpiSymmiLWFm502EAKnkAznfjkQ39zNXFBidPyi4Km0Z77VlmScMIflKFcO7Qy45GFd-0I5Yhym6x0SS09d74EgbErUVfQGl0xISgGk7kDSCsmEMTXQwZZZud45KuRO9uyVZvYsCSgVpX6CTGkglRUs_BS4RlFddBIVVXzAsNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://telegram.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://telegram.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2R6wxDTx0ex1bkPc64fSRofAC76zoLAigENBrUxs6matCsWcGEv8MBVyZe07ciYncjtzr9lB4rCp4amWu4O3lXmRHuyhktpUvaRQY5IdW8f3VlRZwzyl31fPYDC0ifN1PyUDLU9Sza4mLZer25qqJbv-O3tqgfrz7OTuTcxt0fNLtRMqb4JqALFOmZw0g2rSNxBI9ARr9PYfTqcs1YsfMhNL8asdZPy3ti0BdK7Q9thCDARQCvJZYiSiX-scrYy7Vja4fYGAbF8d8Lrz-dmpy69ZSsoZRd9YXzTN20V9D2GKpNjXqjdcckvZPijZhqtE81qtBDjIkbc0dCwu9JEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://telegram.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONjsUdZszepycSii1HNAGsPJgub6cTA25tsRdM3iDET9kxllcKyW9V9ivVjioJ8zIdWHKXOFmxWQKI-HgNdgfoR0oCd0Pxl7BrmVB2PeMBbXy88gPVkRDk86YsHBMTUusDiG9_LAz-5luVgjvVRdael5sOov-W4SgXw-oxS_aXN3RvkBaXzh41p6nnJptFMbdfGKrZNmspcjmbsbSFAU_aq1qlbqky2UuF4hqQYHN_xNQbtIP0EWA0kl69buBNS1j95pkBcfxjnIsSINzrZ72XDDHIzkYqjd9wZQwN8aDHcbmZHiTaVDXRqmg84HHbHjSm5jtCpvZkIi7SkczERmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://telegram.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da1LZCkexxD2PdBzb_4S7eEg1frqwtSPGYUe6EaGRp_RIcaciD2wJT2CrVJXJG1_bMJmx68K89am0afzi8bZbzkOo0s-X-3Dj3hCwSZjLvpJaIFE3QQipiItoADg67GwgaNmhBR5vFZTLObaaqici8G9albSQyutW-1GK-xkX3A4noFwT56jjSdLXmR2dCKaTl7xqFVrLuqhjrT6gh4l7hJwYIG0hc2ibJs-MSC4BuXYey9m7yOamp6N2UsogyB85_X_jpAZtTJrAi0oUQ1-Ka0J9sM0Gacyf11hsvZaLfZuLDNDLZpqo56nwdpRZe4Ej7uXsLYRO23JOe0laoZe7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://telegram.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVydzZbhwv62ulOBHm01V2I6lFjG59Y6ipSfP-eaprSDxWcK_Yn05wFLS8wkoFJeH6XcNbsWRRoZU8EgweETqg2AOrz5loFbxP75PXofw4NXN5JchuWtsHMPBl42KNKP_lP8a0V8Gg00oFqPIPmmn7JU5Uhk8-XPfx77Xm7BNog_Ui0iITh1k0-uOH0kBdAbbriObqS_nYeAxrjx_-LvgvdZP2YENUwCMI_XPHoJzInqefrVUTshExIazOrsqVnt0qhHFscHWtf1ZRICiZvyziS4vQptZmZsHtLiUFr77gLqB-A8R0YPjw3YwkZZnpoeMX2AxKKNfGqypiJPT_4_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://telegram.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://telegram.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmGhDI_vAfdfMt6dMJgqCm7yvgnJfcMk5ciMqt7wplT8oHkSJ8mMBLtdZW5DEBQnFeHmvY1ZlpOjUcfd1tyWdUmgnai2zH6Ae96n14B1QWMCe0sjwA55hasPEfge3gPKyQym-F6ZcqQQ0Anlk4eThOpADlBEYffKXLr1QskwdSRPGzEEwHlY-Ck_NIIQz5M8q61T3-6lwQaRs5QCpW76-mIyBQKcA8CnF2H0QWjk5GQksdiskQhOPqQsgp9PPYZ2f0lyl0IOL_ShEeX9I8g0j9JIB0V9Q8qPQvUeBCe1m3yp8Yak5yuuXK2ApSD5iKZqBMDRLvWNgaMCnGc3uc4Kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://telegram.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIUqiGC31lUyD7FZriRr0W6YWwyBEmV-y0zxDjgLvu_SAyRZd-oCFNiuC9RwE9yQpzAIPk6NxZIZ4M1J1LFTiF2_zmTm2GlJCwcAq9YJpt_6AFNSqDYdKkHdR5sogNdcUBg7cvybPQX1b1MfEDhya9d1Z1Su-NPZr0R8V75SdedvS5da7yEtW_85UALNSi3bg6Xjp9JOrxvEvQgO9mkYQnix-OE9zCJujdIfP_3gdBLNuTC8bwt0SteDpYGWLhAwFWL-dETwa_NPXddTe-D6M1LKfBKZ1ZJuWbjFMDqJVMIMT78lOnCvWoRYWOd2s_W98Tf95WzBzDt0vTj84qsIrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://telegram.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edQO6pKM3l8cgMazd1u5Wd9Fwx2MjrorH5YBedtqvJmWNpWn53tucgLaGsyamvIIIgX1WMQm_quGQpPze-l00vdGVzARF6ewJ2sA4vVQMQL_049EXKuRugDyyf_AbqWDpzvCgB9BzzUkNYaXbogWbrU6hhbAD2G9s60hCjPUTRDMEhbyh8-xjgT-4aThq_WZOyTT-KQaLpMYFfIleY43uWo5pDLU2KqSOB96nB4mrRmYVDYAgl3hkXMI9F5meVyr8TV6qZnX-D_VW_Mj1U4_WQxqNioL8URuYyOwWRwz6yimtq0Vz9MTYWXE7B0fmVrQ2m9SRcY_VYU81QVP010NZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAhVtAjhvYtmtW2GE6cwEo42Cn37llzgLboMYDhsE492kLbysE-jrgxvmUEMETQboBEg-3cULy4soQZeS2LpQDkol0FQEeNLiHJCYpaviA3cMJT2uVdR8dLUo5rGdOYqZev0Oazxdp_ivT-4YUeVv2MVClgAM2EG3NFPbo6mIjSc675-s4cK2aDvT7NgkwbqmNfGbYAh5Oe5FmtcNiJ_wO2_6EIjDeXuqoLWKvxfH3HrOL4crpxzoOkfDwXUBhf2U5xVKePSGVx-ZIY_5xvJ7FAaZ45gY2dZm38d8qpTBVXXMtxVuD5ee5OcndPKYOO71mzfHx388JnMoMJ1lIlyrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=IPQ-PIDISPrdpGBZNIYTALWK-xLpemuTEvyGwKmdKUrTf03zA747XwtG3DD4Wzzc0ban6Zqg6H9ZTSqRfJm__xZ3PX7Uw5eMOwI5R67JTrK8yPEXzHySWy0hwyzIel3LfJ6l65uLPAaN-DdZhqMJm7UgAZ2tpPHGA770JV_dmCoPqVTgPKbRLObzUXJH356haPNvmtD4OlMYhc9YXznLGk_Uimi_7sOLPp7pQC8gvqZrketGYYGAKNJ_x-78q9RK7C1IFCjR9iSTkBOn8f8Nuy7GMnPDvBmyjPLgydhvaoXscTWm473QPSresBUNx6SSjG67HO2w7WvHJ71iZRvkfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=IPQ-PIDISPrdpGBZNIYTALWK-xLpemuTEvyGwKmdKUrTf03zA747XwtG3DD4Wzzc0ban6Zqg6H9ZTSqRfJm__xZ3PX7Uw5eMOwI5R67JTrK8yPEXzHySWy0hwyzIel3LfJ6l65uLPAaN-DdZhqMJm7UgAZ2tpPHGA770JV_dmCoPqVTgPKbRLObzUXJH356haPNvmtD4OlMYhc9YXznLGk_Uimi_7sOLPp7pQC8gvqZrketGYYGAKNJ_x-78q9RK7C1IFCjR9iSTkBOn8f8Nuy7GMnPDvBmyjPLgydhvaoXscTWm473QPSresBUNx6SSjG67HO2w7WvHJ71iZRvkfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://telegram.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=rOUv45w1WfUV7rLuQIYhUylRgqNhHQ4jDba1sasgEvFsfoCjyCZtc8D8mfHHciQ9CFw62Wf9oE_16BqIF3Jv-sNVqTSTF_1A8qStL4nWC1eo0-sQNqFCZK-Fp7KpBdScGwOlc68LxEyDe3C3z5WNUes2GJS7shFLeskNP_UpRtfkQpWz0sB-ffZvz_SvZW_JL8f3LjgxExVoKS1Ew9p95TZUI7Q0UKid_xfqcLGKL2J75v-zeSAptkSzfsLU6SlJvAeJJCJhnazMhn6NBYZ1MqpMZfjFNCoCjln_tv7gNY4rEW7eIvwkSN5n1or2CSaraXg2rl1oq-M9Ddtpoq8I84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=rOUv45w1WfUV7rLuQIYhUylRgqNhHQ4jDba1sasgEvFsfoCjyCZtc8D8mfHHciQ9CFw62Wf9oE_16BqIF3Jv-sNVqTSTF_1A8qStL4nWC1eo0-sQNqFCZK-Fp7KpBdScGwOlc68LxEyDe3C3z5WNUes2GJS7shFLeskNP_UpRtfkQpWz0sB-ffZvz_SvZW_JL8f3LjgxExVoKS1Ew9p95TZUI7Q0UKid_xfqcLGKL2J75v-zeSAptkSzfsLU6SlJvAeJJCJhnazMhn6NBYZ1MqpMZfjFNCoCjln_tv7gNY4rEW7eIvwkSN5n1or2CSaraXg2rl1oq-M9Ddtpoq8I84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://telegram.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://telegram.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ein-sEzlsYcdZb16wetAtVI7uDQS9zdpTwxEZy0oykjIgEM8LS68a-iBXtNgPSI2Hj0zAg4z5lPZSlSrOjAtXbwn1fTEZGp6_MnG33kQiPU1bDO0QfkkPJ6sbOgKDjuVRTzLesVYxa_6Ohne15LZIJhl9DWGMx7mFynv-Rchr1TmOcgUwgtC9qV-uRaxepFjxzZWBsksstxBNky6wjojwRMqKrv9c9zc0Dszhlx1cs_AmhUTP7sVW2azqO2wNlmJKS6rltCniIKkmQOkTNQJB5G8wTJYh_DjYyI6fuDnfq5bBx7cvlZiIzoh9Unam0jjZQFTdIqBbvgJUshBvnRgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_BPdOveQkcR_vrjhsDmYznRwu3-IeInqY9tIr77kqhLguDasa0dGcj9qF43TUDbnguhSiH4a8qIKZsWjP1wUcABQ2QO-_s7zdV4MxkzUTx9478g0OEWT6RahNZ3V8KzKt2Js2LjG4xQCWhGkajrvccH57sUtAWtXRUsDYWpv02hkV6U4VrD--TDxXG_5usCmZYYLciVerOzFiQuv7v96shVoe2_eunmR0rle2SQ4HHoY_Y2JAIoRSUyczf-5foMgPErMI2vBEQfRtSIOurz9cZnyARc9wCJS06OtDgmDjjcHvT4R7Z45g5paduMUtlBN1iXdSbsuVyfkf6nVB7Kkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://telegram.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIu8lA99s8BzG4iIe-GFZwtmFKD3updrSi7bkdhSH2EfpunlVkfRg_ymD75oMKgqArQYQs45Hr2Up2G0u9rrhMD5JVdH52kxOB1KUgygE3dv9Cz9D3A9hpuyy5OnfjPWPEGxWlTCo2tvG4YbVwrORL_qKrXnJUM3RzXwMcjsK-6smkIJmq6dFeWcmMZ_Z4tTp59TR1vmpJj9946cM9D2mTqbx_QcVrmsWWPUgzR67cIaXVm9AufQRLTbh0gMH72oVqVOMXU3-h1I7W8hqVPIWn6n2eREPB9IjIrqhRoC-mJbHvDBmnIXgRjTSDEXa9Z0QU2tjehHD8fBXkrDkAY97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lWcHTTmg7mpeHtn9DP8HsvqQClS7zRqy_5typOTZfjXIBNatKmmSzsKwjZWU7VKa4r0XBe5k_1r4cgCj2jYyDL2zmejigZOmg3g0-43flM6SodUezxnSZc0g4aupirr9Jq1yAwnRbcu271WUTtTVAT-nDLCWgLuLGeepNNty4NZZLjZ900DZQQytbre39ZH3RyLfgE2blzDoURuAo7UY8j0fzk53cOsXTYnfmgCzf74Pvj63NWTs6Cr4vqwhnV-PiMb_td0ohe4NFtc-p_xJNTRe2dQhJoYqUcrs1RNEdQqA8e1ZD_LAlCPKlBNukZA-i7FCQOrq6TgWJ1nGlx_xuGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lWcHTTmg7mpeHtn9DP8HsvqQClS7zRqy_5typOTZfjXIBNatKmmSzsKwjZWU7VKa4r0XBe5k_1r4cgCj2jYyDL2zmejigZOmg3g0-43flM6SodUezxnSZc0g4aupirr9Jq1yAwnRbcu271WUTtTVAT-nDLCWgLuLGeepNNty4NZZLjZ900DZQQytbre39ZH3RyLfgE2blzDoURuAo7UY8j0fzk53cOsXTYnfmgCzf74Pvj63NWTs6Cr4vqwhnV-PiMb_td0ohe4NFtc-p_xJNTRe2dQhJoYqUcrs1RNEdQqA8e1ZD_LAlCPKlBNukZA-i7FCQOrq6TgWJ1nGlx_xuGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما
که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!
همونجایی هستن
که بهش گفته بودن
نفت آمریکا در ۲۰۲۱ تموم میشه امروزه
در ۲۰۲۶ آمریکا بزرگ‌ترین تولید کننده
نفت جهانه!!
سال ۱۳۸۷ گفت بر اساس محاسبات کارشناس‌ها تا چند سال دیگه  دلار و یورو نابود میشن، در عوض و در عمل این ریال بود که نابود شد!
کلا محاسبات و آمارهای شما همیشه خیلی دقیقه!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://telegram.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=W0kligs8S4BHXU0FJRr1OGWi4knuuDputLcpa8w3fpifSwI8gF6P6B0qSRHj5b2j7Dg5Q8TExRT1eMAcgOz_qGpg5tM1A-U-oFZpUMShCTB5RktIEM9isTakhrxpxl0NjIvxo0vgHeiLLO54nize_4VDmgCSJzSm0TtcPJVZusZMZpD_s1DzJWvbw7CRoudHaQRJPsz8a0oS_beZCcbATW8vTAjpMYCucZFOICKf32iwyOaVqdKldQDgS_5nyQ9Yhd2EgNu1E_OnaMuZSVS6G45iRaZjlkmUHJIvP9B2O1IV2POhrB0Wp1EKmzmiE-udpsqeHaL3uM3i8uyfYDrlIp_ocuKhzmMl56-S1ORX28H9OdRf2gdAIulPaAnuTrg3z1rKeuOFTqO1jjMfblxoa1jd8gbVP01SEvsMJAQ9o0qfK_3Xu27JJiTQm4pyEdKgKSEFmYlMYK8c4xqasB6EZdA89diE6qx6I2CzRvF9sdRb_DvBq2kVB9ve98YjI57gAWyNkBGxpIiSQgRIkNoFR1ka3bNd_o3P_OvVMgmImpht8LxTczE8C72fZgsCivzmQA7l56Z0pThtOy0mv22JGMoQ5rWew4A4ypeZMEW1j_4b4wO25_F4PSPDswlmhCevwPeoIusYOXjMPaMW4JQGedmO8P-kZzplVksqTS3Gh1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=W0kligs8S4BHXU0FJRr1OGWi4knuuDputLcpa8w3fpifSwI8gF6P6B0qSRHj5b2j7Dg5Q8TExRT1eMAcgOz_qGpg5tM1A-U-oFZpUMShCTB5RktIEM9isTakhrxpxl0NjIvxo0vgHeiLLO54nize_4VDmgCSJzSm0TtcPJVZusZMZpD_s1DzJWvbw7CRoudHaQRJPsz8a0oS_beZCcbATW8vTAjpMYCucZFOICKf32iwyOaVqdKldQDgS_5nyQ9Yhd2EgNu1E_OnaMuZSVS6G45iRaZjlkmUHJIvP9B2O1IV2POhrB0Wp1EKmzmiE-udpsqeHaL3uM3i8uyfYDrlIp_ocuKhzmMl56-S1ORX28H9OdRf2gdAIulPaAnuTrg3z1rKeuOFTqO1jjMfblxoa1jd8gbVP01SEvsMJAQ9o0qfK_3Xu27JJiTQm4pyEdKgKSEFmYlMYK8c4xqasB6EZdA89diE6qx6I2CzRvF9sdRb_DvBq2kVB9ve98YjI57gAWyNkBGxpIiSQgRIkNoFR1ka3bNd_o3P_OvVMgmImpht8LxTczE8C72fZgsCivzmQA7l56Z0pThtOy0mv22JGMoQ5rWew4A4ypeZMEW1j_4b4wO25_F4PSPDswlmhCevwPeoIusYOXjMPaMW4JQGedmO8P-kZzplVksqTS3Gh1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://telegram.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://telegram.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js94-Wb9mzxCcAkPDwG2xwsigTEoAMDjsBErb6DuaMKqOwLNWrcRkrfoqdWSHNsnRgPCevoN5_Zt2MHC9YtYWSXelMH_2l6a_c8Xz8qWlELSY2JxmB6Vjf4-DijfoaAFHLc-mcsvF6i-EET0jzuSGKl0IumJbaQNqYxlwH0a_v5PxGcxGyAylPIQkgK_CDNhZDi8TeAi1vvg_vp-0Bb3uXd6w6-n1dMEI55nycbeVGLhHVnq6ZJJMB1a3hLZg77eAeX4kQvp_IYMNrZW-QcnjmwwcD80Y-VohzsJmOKahl-hHazB9SZb-9Jgh92kI16hRUHOrzHqEFZapUW9MuW1tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://telegram.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://telegram.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://telegram.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
