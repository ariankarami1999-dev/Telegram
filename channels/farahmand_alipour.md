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
<p>@farahmand_alipour • 👥 64.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 19:38:12</div>
<hr>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
ترامپ به فاصله ۲۴ ساعت، از ایده گرفتن ۲۰ درصد سود از کشتی‌های عبوری از تنگه هرمز کوتاه آمد.
«به لطف نیروهای نظامی آمریکا و همه اعضای قدرتمندترین نیروی نظامی جهان ــ با فاصله‌ای بسیار زیاد نسبت به دیگران ــ تنگه هرمز برای تردد همه کشتی‌ها باز است، به‌جز کشتی‌های ایران. و این هم به خاطر رهبری دروغگو، خشونت‌طلب و شرور ایران است که این کشور را به سوی نابودی کامل سوق می‌دهد.
بنابراین، ما
یک محاصره کامل
اعمال خواهیم کرد، اما
تنها علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هرگونه محموله مرتبط با ایران حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده‌ای که با رهبران خاورمیانه داشته‌ام، تصمیم گرفته‌ام
کارمزد ۲۰ درصدی بازپرداخت به ایالات متحده
را با
توافق‌های تجاری و سرمایه‌گذاری
که کشورهای مختلف حوزه خلیج فارس در آمریکا انجام خواهند داد، جایگزین کنم.
این سرمایه‌گذاری‌ها عظیم خواهند بود و در عین حال برای خود آنها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.»</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVU-nDZkvVMadV7tl3LNLTuxH72pYU5CaNIsDpSVAfsYyWebLiP8fhqd727ZvWTwz2u-zDA4xF0zWoyg2IFWTcY0B4qovADQl-SCOxzhUPXuYiEZuEjk3eJYAsD9PDTpG3M5qKyjXFI9bXNVt4ANlpq7x-xWP6MmFRa6H57xCSejt71lZd-ngv7jIdaGFFXHrElikrNWv_-WkQRgIAECXSmEDWz7IhnnMYdfLXb1KMNczAgpHEXsWY4zZqlta8I1QjB249pzOjAAINpWiH_NpqYQobDKJaIWptEaxlPOURJOARy3H8YMisIQSTSeta5rg2zo38F7EHphnLi0wWWvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=aOWdx-kjqpNlLf_hjd1eb5E2Sk6qQqxN5yqmFeN-NyKk7KCPsSEQvt-PKFPbNUvN_toki5Uc4P1XZPv9YpHMVCqyVZ24I_h8Kp-VIrWOrx-A_feVKJ8tyGog3A-WApFMHrrRqPDGkUFqNOJcV_nGheECSiOkpGz3jHbrC-PTsoyAWkRx2BcQgW-iHqeLTBeTwzKjvDrqW5Rhzcu3eEbbfECTLzW60kDOE-1eTewufalRdFXDLCGNLlYtzBsr2N5FXM0bMnPyiY8vC1KqQCwaN6gO-mOn4OHkAFnfm_yUFfCfVvAoEBTh7II_LViYFNNJKi2QqNe8XM3AD2fcE62NYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=aOWdx-kjqpNlLf_hjd1eb5E2Sk6qQqxN5yqmFeN-NyKk7KCPsSEQvt-PKFPbNUvN_toki5Uc4P1XZPv9YpHMVCqyVZ24I_h8Kp-VIrWOrx-A_feVKJ8tyGog3A-WApFMHrrRqPDGkUFqNOJcV_nGheECSiOkpGz3jHbrC-PTsoyAWkRx2BcQgW-iHqeLTBeTwzKjvDrqW5Rhzcu3eEbbfECTLzW60kDOE-1eTewufalRdFXDLCGNLlYtzBsr2N5FXM0bMnPyiY8vC1KqQCwaN6gO-mOn4OHkAFnfm_yUFfCfVvAoEBTh7II_LViYFNNJKi2QqNe8XM3AD2fcE62NYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjIPXzCbYPwjFi9oe00DJVtesjM8S4PFKJLr3g4b251jI1q8a0Wwxy2JolqH3umtm-vobb_2Bn7_mBadHvUIFAk_hRvVRbBFRHUxg5e7Hv_XQrRL28sh31xCgjk6mbY0lR1NTfvNN8KmTFUUemnVXkjXf5ns3POtZsFpxfuVQF2uLSf10V023zCc90QXuFmmoqTi5pw4vIIIoRTG6iEm61XoPIY6tN-s4kMnodT4HA7w6s21416OCh30JnFd4RtDGHyPauEQD4qLTjRgIoKXdhTNz9DgC-o7Lr20m0a8-dHnChi_24IrBDleutOkXo3Eg_w3iQEfgrKi4Jc4ab7Y2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-cfYJQNLiQhORzcP8Yw_97m9JovkSFq8nUOZxJpTfGXIMupYO6eNxllsMiVEPfWEaKp7AwRPa6O23oe71cTJkd1DmuMjcGvCUup3qc0skYAWlaIgz9RheD7BvR832qfbgBNp4Pp6f_vkBn0yJXBvW0AXykzxmZt-erxBEx04mF88lip38kqomYJXPPTjTLTBOCvWR6xE5MNiKDDaxNscdxf3imM2gO4D_Ujm0oYHCAyQLYladGlSolw22O98SnjFgFUHJl6MFVZactJ1jtVWJt-KH7cxdViRxenvlpVCbe_l4Ibbc3fx_r2enx1VOJP7U26x2oLbXzoKwHhX1dnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1f61vL42ySxQn5kYMCloRcoaUAkfAtXCjC_lNTA0zTKTDWkOQy_ZWZfgmhenzwH7EdwIPX3IUij3OHPCgMi2KDQIiJ33IS5-eZECTj7rLA8Xc4TO8Eke7v2MO2dXSL7Wz-S-Uhvl9BAsodrP8dylVH33cX8ktvdGZmshCvOCD1J7X04Dl98qBTAA3sHfUTTIPB7YT8PRVflBfyS3LHm5ihIH_S14XgvhZcEpTbJUbBUviyq8e_Lk3AaSCkCSSrvGiRylZ8fKHkdB14aHaJGh1TvjV_oyJsZEcmpe_kVlcAOwz6Dv59yJsV0qQUAH-YXt7R1w6XROe7UhLx9z2nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_kWza-Ol5frBCLnmexrS8u2AGjYT1ApPyNVoG9lA7ADKY8GXUqknQoT5TwQOHsXDVVVZR_9EcdpFYnYBtCyg4LFBNWNyyR9utQLCD1so_xACpttTuWNYYtvQiHkoT_juGVOg-wQ4YMu8dZ10-cYJ29au0z9POgXSGSDbP5Z4MUdPzDuy_Q0smSjBqsXrdV1rpjViaKFFJMKYlfsakYct-xMYOfZC_6AEsN9texy1-zCWxLDyzO6yaIzIEm2xEaB59HKDVcAEjomeM0acaBljhotP-2A4_x5l91AX6BbrO7RWr9naJ0X3RfVrmoKke3kKi3AkcKEB2jmVT8Ko7VZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=hfRSnnbkj_HzC68nSfnbs963_4hK2ggiFjJJG75xUFcdfIIMWpK-U2_vyiYPKrVzLr2XAiYoTpeUWPIdK2pqoVyhcSu2wYUvaEB7zxhueKhQ2b1prH1NCD0-3u_Nc6jNnA5o1qpqwuWh_sZ-b-Gr7Lfsie8zFypXe58IAoWvKqTtMxuQzqnlLPB-ycnF6L4gGT01yaptfGoDCIrvnXJdNNA-oJ6X1BzQ59hWpr20w3Jmo_MeDL2Jeji6H7A6TedWZ1p5EpKWnZgN_qqJDsZJ9r05qbCq146AUDLusBHTCcFz40WTNZs45bPa_3ZN6tKDFl1zYqToImBJH9XqsHzMXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=hfRSnnbkj_HzC68nSfnbs963_4hK2ggiFjJJG75xUFcdfIIMWpK-U2_vyiYPKrVzLr2XAiYoTpeUWPIdK2pqoVyhcSu2wYUvaEB7zxhueKhQ2b1prH1NCD0-3u_Nc6jNnA5o1qpqwuWh_sZ-b-Gr7Lfsie8zFypXe58IAoWvKqTtMxuQzqnlLPB-ycnF6L4gGT01yaptfGoDCIrvnXJdNNA-oJ6X1BzQ59hWpr20w3Jmo_MeDL2Jeji6H7A6TedWZ1p5EpKWnZgN_qqJDsZJ9r05qbCq146AUDLusBHTCcFz40WTNZs45bPa_3ZN6tKDFl1zYqToImBJH9XqsHzMXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLs8ji3SRbTfV3557QN4F6aIKnmRJizshBzGZZCrlXmIqjxIYWo6YPMU1hD-7WwAJ1qbcC_6H7868CPlQs8AgoOpAbh38w4Itb-5qlooMxNny27vR0WkF2kTj8VSgP-x1Oqo7UHfpyBIGenNj7NDWHtaIaTuTALV7JORH5U3jToabNGZc9KKQ_8ZwGviSs1ENgKEXTXa5Mcd68CDsGK0ltsqx3S9JCVMvSgYcYsSIa4JOXHwKt8TMU0XTXZGANQ6oxcdFTUf-W890Vgn61_RXyi5SYPaLF3FWiEHcWZIDSi-CU1ERfewGmyh5m2-3Erfj0_IGFcW1EohBt6DwK9miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=UInfzEqdhosexGzjsDt-5A0DaXq79q96LwtLsdMXGq27tFA4j1CmS4HomaYpSPzu3KoXxCjYFGyp-wsqF9nPZ-7-PH4Oyy8OWNr64TgYdFq9sDGmsTDDFfcwpCZBMOwU8idbT14sFdw78Tkle7B_PoookUISOP2uZXgPqWa3dADcihmRPu3JLU8G3UaFjplPbOWHb_0DYroxslw1tCdU9H3v_8AKWf3irBAl5mAOPGfTpjXOg7Ikwn72r26XkZYDPctzJY5Y9f6mLq_43biOC5_EOdffhtcj-qQkhwkuEda3dPl_60myPSaAwxeyquHmSEauFdsKeM84jWoZbf2KUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=UInfzEqdhosexGzjsDt-5A0DaXq79q96LwtLsdMXGq27tFA4j1CmS4HomaYpSPzu3KoXxCjYFGyp-wsqF9nPZ-7-PH4Oyy8OWNr64TgYdFq9sDGmsTDDFfcwpCZBMOwU8idbT14sFdw78Tkle7B_PoookUISOP2uZXgPqWa3dADcihmRPu3JLU8G3UaFjplPbOWHb_0DYroxslw1tCdU9H3v_8AKWf3irBAl5mAOPGfTpjXOg7Ikwn72r26XkZYDPctzJY5Y9f6mLq_43biOC5_EOdffhtcj-qQkhwkuEda3dPl_60myPSaAwxeyquHmSEauFdsKeM84jWoZbf2KUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=GKDdVqzjght2CmzxXKA4mQx1etEcYUzpqozcPXhal7NN7W13tBo7DDWPA73IklKKEsHD4w51DawBnR6Wn7MSxEjMvdt9vRWbjLlb7LOjUBoIFzwYI1o54gCkLPXXh7EgM8r5iW3nondk0XLTEMSz48avmYl_bUpMmIRV4oSmOtXzpcqibDfiJTZOw_0Nj5PBpDvG1yjMJ2OIuMtlynkU9pIOZBURNYKX3O2_PWplbr1odSIh7tzQ63unK-JwgzU092PPbAKUYfLHQAjuHQvtuWNkMJidB40q-hCY6j92crlwhOZSzBjD7gNnxG0Dte5ABbho6SpCLnwd2Hbr5loraW9WQ3luTpDzIrDbsBBAWeLMZ_GC80UZTVVIoE6ahykM2keUHXHITdlwkycxw5FlJ_Ch3Xy4YFLv-hsrCNwkQTXeehFD-HBJUSjDOnVL9Lp0a8BzR9Fq-iyR5n33vg8cxbdrBay6gANQ2hExReTNWKSX7M6KXIR0Piz7w4OOQXgof-UbxbB2UcHGvgnoHoAGB7t_1l3qAJR01Bspy2CNmoJcdEqgROlpiY9ARHAo8Mkv0-RS6UqyuLpFMhweeMVa4OqBRlnBFpZJoilnc5zLx2Ef5tIdj53oepF3DSdis8JVlvxKtHnajCoNI9FsOf_rS4lfGWUlhEQUk6XnoGh3uWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=GKDdVqzjght2CmzxXKA4mQx1etEcYUzpqozcPXhal7NN7W13tBo7DDWPA73IklKKEsHD4w51DawBnR6Wn7MSxEjMvdt9vRWbjLlb7LOjUBoIFzwYI1o54gCkLPXXh7EgM8r5iW3nondk0XLTEMSz48avmYl_bUpMmIRV4oSmOtXzpcqibDfiJTZOw_0Nj5PBpDvG1yjMJ2OIuMtlynkU9pIOZBURNYKX3O2_PWplbr1odSIh7tzQ63unK-JwgzU092PPbAKUYfLHQAjuHQvtuWNkMJidB40q-hCY6j92crlwhOZSzBjD7gNnxG0Dte5ABbho6SpCLnwd2Hbr5loraW9WQ3luTpDzIrDbsBBAWeLMZ_GC80UZTVVIoE6ahykM2keUHXHITdlwkycxw5FlJ_Ch3Xy4YFLv-hsrCNwkQTXeehFD-HBJUSjDOnVL9Lp0a8BzR9Fq-iyR5n33vg8cxbdrBay6gANQ2hExReTNWKSX7M6KXIR0Piz7w4OOQXgof-UbxbB2UcHGvgnoHoAGB7t_1l3qAJR01Bspy2CNmoJcdEqgROlpiY9ARHAo8Mkv0-RS6UqyuLpFMhweeMVa4OqBRlnBFpZJoilnc5zLx2Ef5tIdj53oepF3DSdis8JVlvxKtHnajCoNI9FsOf_rS4lfGWUlhEQUk6XnoGh3uWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdHmmXXc8trK4MhLiSE1bUtB2v6rcX7Salq4kn_F1IusKTO72C4-YaI8YlXNh1vkLMQMOxucCwz6GU5llci4M1SRzmlafcaiOKxGioWAd8thNcibg50z1-ZHMvnVE_aMjfEiln4vRb-OS2MinECSfoXoIUo5n_kYQTbuaogn631BzbpuWoMBE6yVTUC4Fzyux4NVJNg_2fAoUXEDT6c4_w-BP1w0HQMy2Rdg5SNjtkNbxhRLjYJlbFLzolJvYgux_NIMsuGcIP6XL8hQKoWlcK6MeYp59d7mcj8e2DrZAhnkm7e9OOrUJEIR54KCDt6uvPyYT0MLKyf2JDNXjQvGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-fadso-ziuEO0QUUQtof1oEqVhB3Yumjn5Ut1_ZCQghERLw3OE3oOvjqNRoJAxHr976Hj9gfnbra71EwzIIjG-vDspimbdqF-kLhDrGX7is3se9Jx8evGm3E33t5QGqcG90cEdCM6J5y9gXgKGogDxrIEJtpGyD7pucgJ-Iskm2_xhhBVcnAuDHkqcjqRcdSwxLaEpuv3dE2HW3QgfuFgbWUC8F_wCm-OwqSL5SJRUrJCYawKIdCDKBd86XFPfM9qo3OR-ZP11v30FRCPpm5fmiWva98xR36QXrX__jI3qefGFP3faWaNGuHnMnOikRrJH60hcfIz9Vzyu4NPvo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh2IkRxGq-6-ePdNopCx9gJoqznIHYG-NCBtM75dT4d5RfDGkwdOJPtujB5oAcHN1Co5d1kemYAqd57w0oWlRRm90GBI39cHEF6De1gpt-MUc-Cr8LQlRnsularkYU1_ggigPOPsDWGtLqT5hBmmsCDgmhARfd9CAd3BfYLnAUF245d2UhUiT41V16gE7T-tioKPGGDm8NsBY1RBPLRFVVUG9PHCihsiqEV757SuzB1CWZgMBUkv2HOVvWhaEpkC9-Nca1Lcz_ZEiSpmB5i9O4DAmej5Il8OfYy7ikP1d0zb945PE3MtVEnIoyM610kXFK0LtsIt9_cI9yzH_NX9vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtKUGlMzf3zS-zZS4KNzyXi3_v0ZyOD4Ff_srwvTZsGXrA6eaoQ5JjWSIEEvwcQ9jzFGzNfImYBgqy8vyfliay7ms2kUAmW3nj5HcmEAtO2zqr1WbAy4pfqjsyS__-U_d3hBrexhUh-L6_j6_j1mmeo71IYV0ibEkVc_uyen0L5WBy8P6Olh-nWNc60e-1XfjucYtJMeOGE_MAU8DXhJ9bLNRCdwp4rEBuiLJOkMp4D3dOxKf5AvM_BJapcTgDvNKc9fL7S7OOhrLGG4Di3D7v6A9l3GUGgtUtPs0SWd4Rdd4yl4D_rHMUTcOoU70UdUZTdMDwTl_Pl1gvYrRW9gqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPERQqJURuUFa7lblYV09ezS0jugDgY-vyaLAblxb5ZDEvBIMB8GgWFKsPT1W8RE7gExd_9ep7ZuZhU_BqsUTqx27cDdougOgTT5rPBcVMO2wMYznOVY2JXM53cNkMw0_ahwEmXdDGVUCs-xuBNvmNHcT71XrtGbv8OIuisGwiCUFV14AHJS4RGRU1jfdivfksXzYbSl14jUsBXukoKnaU7HfMQ7sH7T-GtQJh1QAZWbsFCZcm6IE0T7lxc2bNsRMk04l8m20qdO0EumiTNKKyiVybG5O2og2DeeqqL9QfZxmQck1Fkx61CptlB9Ick7o4jSqRCU_bLBY8IU2L_Reg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3HgqRhKTTGIVodgzsxFkJCmFBswfl8b6NLFsDMB7DoicgKkCHzNUd2-tJHpW5OmGDOnNCAvXLWnlhtMOjUQ_hzhBYXXiBSkyLnDY38u6dQNh7f8zfkkyyC2BWfOGsOymJ0XViancXGNUiOrii5FBPf9rVD4LLyX4zo5XKQa_5RXeNZNPp3TULcAJK5RY3MtFv2TdEQWHVBVnrL-o9AFa9GxlQKpOc9K6u221u8p-1wg_TTmcI8Kic8E5d8OztDUkrv2BF5mlNqT5bCyl2GAayNdX8ijaTt7rPAKnKrzTLx5M1NwA-G4JtNSsrQ0-XH2ZreFoQ0Z1X0HCVPhWNM27Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3pQBZh_IzXkiwLrEioWwiGLkxwah_KsoSPmgrYAdlljy3_OzsGX5y8h6MOSI9Qe0QRcfHIhSp-B4Nz6JTfr_ZdnpGc7vSVdhk9h6DV_4ejYC8xfKHm8XbwtbeqLaPILsCEDJKNMYSTetUWsXD5WxlIDDv28fhsl2SvI7uEItEH5jD8R_ElgYv_vj0KYjtl_l3dXaLrLy1_90UPWL-JyXT2uXy-VeA7wn0hpNjA_4GIyqESQ5ZpFz7mpnueGrAqBDI5ETDSRr-fPEqd5SHpkC9kP5aA3H9Iji0M-PPOBFF1SpFWEhBy_bkOaJE9Y4N4YoYTbGqBbGFxI5oZtZ7NNexkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3pQBZh_IzXkiwLrEioWwiGLkxwah_KsoSPmgrYAdlljy3_OzsGX5y8h6MOSI9Qe0QRcfHIhSp-B4Nz6JTfr_ZdnpGc7vSVdhk9h6DV_4ejYC8xfKHm8XbwtbeqLaPILsCEDJKNMYSTetUWsXD5WxlIDDv28fhsl2SvI7uEItEH5jD8R_ElgYv_vj0KYjtl_l3dXaLrLy1_90UPWL-JyXT2uXy-VeA7wn0hpNjA_4GIyqESQ5ZpFz7mpnueGrAqBDI5ETDSRr-fPEqd5SHpkC9kP5aA3H9Iji0M-PPOBFF1SpFWEhBy_bkOaJE9Y4N4YoYTbGqBbGFxI5oZtZ7NNexkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56poj1bWVmeD17xVwdOka8QvdPGsDiKlJg4ZrXFgybAdcfj8J9nzXBM3ImXIZKi1zcpkELvHfPoBJ_jCXB81dAGFdu-nUtG7PWSsBKk4MSO4JzHL_cbOurTw_qmf2tErvGqglsBMi22LqB_LSIW_S97BZbRv9dk5z-0TrlrojEHkaX0avEF6vfX7--8tDHVlzCb34NulVhb61L7QuuarGIGKyRFHV7F0Z0n-XeYhHqhwo1vF5ToIUwbhX5nzVz045PI-FD4Fas5FxSOV4gOTNMIMrbKWOQaLnKLafdDb9rbMPFlCG1fk_QnoI4w7ouheVgbdombqGVRk6CJ582CQYEBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56poj1bWVmeD17xVwdOka8QvdPGsDiKlJg4ZrXFgybAdcfj8J9nzXBM3ImXIZKi1zcpkELvHfPoBJ_jCXB81dAGFdu-nUtG7PWSsBKk4MSO4JzHL_cbOurTw_qmf2tErvGqglsBMi22LqB_LSIW_S97BZbRv9dk5z-0TrlrojEHkaX0avEF6vfX7--8tDHVlzCb34NulVhb61L7QuuarGIGKyRFHV7F0Z0n-XeYhHqhwo1vF5ToIUwbhX5nzVz045PI-FD4Fas5FxSOV4gOTNMIMrbKWOQaLnKLafdDb9rbMPFlCG1fk_QnoI4w7ouheVgbdombqGVRk6CJ582CQYEBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=XGW6RW4asufE6yUbGonN33n4lgqzCsRVSNG3-bleo6CwtTMpo7JsFrAEF-IeKbXf2DMnx4tvjepJqHvfgWnZVDzaTXo_GGoCDp9IKxjCxfsJ02xst5eJwj4q4Clbsd1LR8ZTQm_oPESxsrWw1r2YyRs1Olvn0tKzrdtI57gfbFm7jz-8ZODl04aIB9ZxWAxLCQN6HzKXF9gOw5EY6Lu2fAIPWvjUAcFunFGI-Q5CTW3BIqyEcD8zHbZoARx-9hFxwRT1oHdaDAYLr2HckSWdpzRCKhKFfeIiyvvCAQb_pyjSntRZkKH_CrkwpzsXvJhMJMSA3RUcVqSR48kldvyCbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=XGW6RW4asufE6yUbGonN33n4lgqzCsRVSNG3-bleo6CwtTMpo7JsFrAEF-IeKbXf2DMnx4tvjepJqHvfgWnZVDzaTXo_GGoCDp9IKxjCxfsJ02xst5eJwj4q4Clbsd1LR8ZTQm_oPESxsrWw1r2YyRs1Olvn0tKzrdtI57gfbFm7jz-8ZODl04aIB9ZxWAxLCQN6HzKXF9gOw5EY6Lu2fAIPWvjUAcFunFGI-Q5CTW3BIqyEcD8zHbZoARx-9hFxwRT1oHdaDAYLr2HckSWdpzRCKhKFfeIiyvvCAQb_pyjSntRZkKH_CrkwpzsXvJhMJMSA3RUcVqSR48kldvyCbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=mXfLmvoLsAKK7OWUOhGWnk3YOjYFpuSkkYAlMZbKmwq0Bk1RVWzztTpQ2kJ8Ie1KTeV1WphO9KSVXHb3nBoohRytPwxfVVjlbzfMONiBIw_6R4SFKrbQmQMNGpw9zgVqvtjSnaypZ64usHqyenJpAl93Xe9yCrBESY7NUYPk1VgYxBiowggBrwx7_AALx_Za7PSWqdVbKm8oLjMxeE3fTdE_PCQbBnxdQQa-4BwnaFE4G4TJ_wKAq_YL6HIqfZYlaW3MRl2s7S0JpO5K1qPMauUmVCBoYtuzhX6GYF6lELh-3S8-ikuSm_qJC0H2SZcCfUk2NOm6i3OQTNU2a3d-hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=mXfLmvoLsAKK7OWUOhGWnk3YOjYFpuSkkYAlMZbKmwq0Bk1RVWzztTpQ2kJ8Ie1KTeV1WphO9KSVXHb3nBoohRytPwxfVVjlbzfMONiBIw_6R4SFKrbQmQMNGpw9zgVqvtjSnaypZ64usHqyenJpAl93Xe9yCrBESY7NUYPk1VgYxBiowggBrwx7_AALx_Za7PSWqdVbKm8oLjMxeE3fTdE_PCQbBnxdQQa-4BwnaFE4G4TJ_wKAq_YL6HIqfZYlaW3MRl2s7S0JpO5K1qPMauUmVCBoYtuzhX6GYF6lELh-3S8-ikuSm_qJC0H2SZcCfUk2NOm6i3OQTNU2a3d-hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=De4-DJxSpQ9C9E5KmNMAFjlSKi3MT_u6w993uOymiESDEFfli6Zn6ZrEjtsx-A9jZ30R5_wUR1Gj9oKZxo3etAv2dYYyleoWZ2NlpY8CFPoIdXOgpCNtQPz-E5E6TVwydrJC-dMZN3gUwSs_EwfUcjz_da56qIigutfDsxi0Hd27x_TUQmEE3PCQV0kYEBSu6yMpgQK7yDfhVvDDiX6GXuqk0sTmbNkGWnEdOnZbc_88uC4O-ldfRnovFo7SV-Y_lmSWF1HVJRWETMzk2H6Egnk9Z-XBT8tmaxTHtUoh4lWwzJiJzuhqIOe-g-W8bga9xax20QZzMXSuWbcStSUqaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=De4-DJxSpQ9C9E5KmNMAFjlSKi3MT_u6w993uOymiESDEFfli6Zn6ZrEjtsx-A9jZ30R5_wUR1Gj9oKZxo3etAv2dYYyleoWZ2NlpY8CFPoIdXOgpCNtQPz-E5E6TVwydrJC-dMZN3gUwSs_EwfUcjz_da56qIigutfDsxi0Hd27x_TUQmEE3PCQV0kYEBSu6yMpgQK7yDfhVvDDiX6GXuqk0sTmbNkGWnEdOnZbc_88uC4O-ldfRnovFo7SV-Y_lmSWF1HVJRWETMzk2H6Egnk9Z-XBT8tmaxTHtUoh4lWwzJiJzuhqIOe-g-W8bga9xax20QZzMXSuWbcStSUqaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=Z0YQjAGC5YVMco-QxHM7O2EOq5p4e8Pc8H1bUq7-DNm53X9aqv5tyPBQL1vNZby0APT3NaTho7v1wCs6szZW4Cijx8uiLZEmHdfTSZ_KbCz3e_dVfys2KqeUJuFHoV4cI5ig2_my1am49lhyg5SX8uHvS5OvCYuvzrpA-b9SiR_fGN0ufzpmqdVF4BOYJZrzAn9gQi4r1FcmzecIpnanKs1LPV37I0MmVtCAQVvu2WQHitsDwirUFOQMjNQFq0TRc25r1kRh9lg1eX01yCSz1kR9pGm5OU60_qd5wCMlZTyxecu9p3McCwpRcPVMWvLi2hRMMNBzjLmRhMR2KjEd3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=Z0YQjAGC5YVMco-QxHM7O2EOq5p4e8Pc8H1bUq7-DNm53X9aqv5tyPBQL1vNZby0APT3NaTho7v1wCs6szZW4Cijx8uiLZEmHdfTSZ_KbCz3e_dVfys2KqeUJuFHoV4cI5ig2_my1am49lhyg5SX8uHvS5OvCYuvzrpA-b9SiR_fGN0ufzpmqdVF4BOYJZrzAn9gQi4r1FcmzecIpnanKs1LPV37I0MmVtCAQVvu2WQHitsDwirUFOQMjNQFq0TRc25r1kRh9lg1eX01yCSz1kR9pGm5OU60_qd5wCMlZTyxecu9p3McCwpRcPVMWvLi2hRMMNBzjLmRhMR2KjEd3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHFxW1GEWj-QEalZld2MPWCuSM32L-N9TLFdTOlHr22jQB_0_FeinGimZ3cOTV6JSih9SZ71P-J35powNB6pDUjKQgPSuPgKZWb-sD6I1Q4so8Xa_RPdrmT1NFJdGPsG_-dNFG8v59JZ_ZJ6f6aqz8osRjWvBDyA9nu38A47qAiKXx59RgdJCFR-3IEtO8ZwvdquLbgTG5nQMf2_hQSHjiqOo0vNxkWKUc8MaCykfVIFAglY4SbzI4UOUd--2-_EE0TfaAv1iVwsOKZtlovJ1ka4Fh9dz149bZ9TsbdtzpRgBoMufItPvslTNhYk7zCjOixHS1gpzE-GJYal6EA8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1fL83Zlu4N9sDfh1fSVhvKQT0YxxKRdth8r1h0Gzw4blMEQfQnncZ-9H1XnIGYZetr7sL2YHNClmaUv0c9MJRXnU4rkfjFaXOHr38dGANGhrXwK7yb2GUutUSoMeQS9iJvoWk7agkKJgNC0JkKxb4GzuP-wrafoCGoS-yvX4ERiB3DGyZrscr6pT4sEIKmG2SIeI6pHe1unk4t5oHCnUG6EeySVtVrKp8peAd_9ZM9CV3L2Br1Ay8TPnjGc0-H-seyllZiBiNxfq5YA6P_736znCbd0yTm3bwYagbVN_vJdScII0rSK_JHtZiHmnRRotRWFkPIxtm6COT2EKP_lbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=TgYMYChExcTzmE1IGKXBddyQ3NenRUVMFFrYjpuQZM8RXQ9uf6RDARhridZzYfdU-7hPOJpEQcl891XXQoCUhgIE5Z6k8RQsaZHtGdYWk_pd1d-2aMR31NgVD-ewsmFBhpvYptuVVbUQwiINvtsE_ZImvbq3Ra1ZhHr0KnccLWGqjLNa04ATSWcTYf5iQhPRsTcri8t6HBmrKIH4_c2cFGTh2zWtoVO04GC-CbThY4kVtkpuEmD-1g4_2eZ8kAo0SrJQdQrRB3SC36XLd7d9F8EvMQaaT8P7U7k6B_zIY5o29-ZbQV7RYUB7dANzk8Wyo7xhvNe1cLUhRCizhW0vaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=TgYMYChExcTzmE1IGKXBddyQ3NenRUVMFFrYjpuQZM8RXQ9uf6RDARhridZzYfdU-7hPOJpEQcl891XXQoCUhgIE5Z6k8RQsaZHtGdYWk_pd1d-2aMR31NgVD-ewsmFBhpvYptuVVbUQwiINvtsE_ZImvbq3Ra1ZhHr0KnccLWGqjLNa04ATSWcTYf5iQhPRsTcri8t6HBmrKIH4_c2cFGTh2zWtoVO04GC-CbThY4kVtkpuEmD-1g4_2eZ8kAo0SrJQdQrRB3SC36XLd7d9F8EvMQaaT8P7U7k6B_zIY5o29-ZbQV7RYUB7dANzk8Wyo7xhvNe1cLUhRCizhW0vaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DE0P494ggGmj5LBqv_x-s4qmyIjQ-I6SYTh0pYAwsgpEtoK1Mfr-GRFyr1riAJtdAIMIHbQrIAfWEA5T8I7xqNZkPdlKiKmNXGRmKQk1myL4U6luItTaVAZDMwpfMAPl-x1StgvNMliQP18s9p88zm1E-n7rd_A0ckQE4Cc8CTfdu619TWwKzgeWOuUsErycpkrZZXjbSCjcRZYJrKdJ7yDZp8FbqLqYXrVPWpEWdpZWl-6pfH-cVJE1iKOKHOwMU5asezXEYev_EoGNSj7DXBFfFu0GxKYlPpiy_yeXwKs2YaMsx5YA-BxhKpeJ-kWos7ZDiDxo0r9zTum4X1bl_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=RcjSHdJn5P-_WQABLm2CoUrARjPC2e4HwufAM20icbzlbMIJJdX8OB3Xwq_KqaeQTd4yiGjAhIES4Dzzj9-dr8QgjB9qp5onUvSm1Al_S9celooKUuillnOUmKc9gBjroR4Jgfxbu23n_JfWQz4jUxaUUbGUVuhfuG879X2i2T2S_8D_pZ5KEvlTw0V85z-x_z3SSjwYm0uWSQHrq3SLhTSHE1_sfnf7gDxxN3eXrMCu1ReM-Q5JqZt7OwVQAzoSi9jE-gpiqrk3dCmm-mTx7cNse_aBBxvlmxfs-4kYo4tIKBGlWcD_XFHpsiyzJuRGQcwKzFo1jDrzsTvy6kCj0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=RcjSHdJn5P-_WQABLm2CoUrARjPC2e4HwufAM20icbzlbMIJJdX8OB3Xwq_KqaeQTd4yiGjAhIES4Dzzj9-dr8QgjB9qp5onUvSm1Al_S9celooKUuillnOUmKc9gBjroR4Jgfxbu23n_JfWQz4jUxaUUbGUVuhfuG879X2i2T2S_8D_pZ5KEvlTw0V85z-x_z3SSjwYm0uWSQHrq3SLhTSHE1_sfnf7gDxxN3eXrMCu1ReM-Q5JqZt7OwVQAzoSi9jE-gpiqrk3dCmm-mTx7cNse_aBBxvlmxfs-4kYo4tIKBGlWcD_XFHpsiyzJuRGQcwKzFo1jDrzsTvy6kCj0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-arePFSeSKRz7hciP9rU_DOGfLrMNTepFRBVKYko99VoUqF9tZg3zBnnNZeQRESZPL4oz5T9X52gOcxEYNDlOnsk0Z7WC5hz__0e0cL7BwY0jBaZkP2Bd8QuJ_0PbC0JnPdT-7blxZ15HsjYOAqJHuWEI44584H9xZKk_IF-lO5nh6JzCIQWfxLix7P6ngGFAn-k9FQQ-LJY18_F6DdeoYf-wdr8uUSYu03xNBN9svQR5qVowdBOcZ4xVYSZVvKxSoZJmd4rs-EDFLJd1kcesidg7D3HcJfWk224DxI2b9rNfMI0oZPr8rYUjbvIE6fUYWtw6rDR7x8TuLOU3_J-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN-bP5X0Lu0t7J3XEheiNFMnKSyASRPYNAVFv2SZ0VMxyD1DbNDeLulaKBpxH0WGPLVyUdATpzNWXtyWNGinvTYDDKlHd6rA69J--naoScDHtqq15x7qsl9EdCQIcuipekv87HQbZBoiCnXING_5zK6qafLQXMNZSSDTaHrJucQFOdXCKOxbei9cOx9uXtLB_o6aWCr8zuJkXsg-8tumqar5tFKP4CHqguAXATHADF9E4OFUl3PwqVsQkzoXFHvPn71LemYEVECHXKnPmzgr4VQiMDIJUOQzbVlG4HBr38V8S4jcyXaTwTeMvZLoiz66yuApeyt-zJit6vPEuOJPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atTQz8glEgwmRxUNmTXrONydn-Yn_hvuXoQrfOQUa63yp_Mk2dn2gqkGtDh0nY4vWsVsAGZc5zUgU0wcl-TS5n95h1ujl_MXwgVr3sI_l1CUsDLSQAVBM3sMpYA1fYemM_MauR2YQMgPiSM3PjD5i9kZTC7DWg1SMmmYYJJ3EU5Hv4voWX42oXZYzIjImneoPxio20HopD-voqpanq7vv7cBBbfhD36HKJb-84-Hn_FJgOvfLk4wjBNVPxzlysjARkt0Oosy2Xo8z8l9hnJXWWXmPxuFfHwdzIp1P3aJqQ_wYc5npLBgsxYdAGheGO8wSpuSi8Cj47NrF67pMatpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhaLjz4rTCB7D8-iarnceKllEMWd63DdYMOSni3i9hB7jZ5hI8yMpgtwA4aqHJ7MO3-gk3s-zEwMbqCb_-nheLnj_cDBHwnQ-ZcH-PwN3OLreeFEh_hQfETRBoAwTzTPAVSPqmoMDSDGX3mVaDSd9FulJc7NiiAywqQM15jSlCm1_xXWgEYPYKNvq46BtHUISJA1Ti1SE8z9bG1MXekzkHlHitfj6Xvv5znEDS1RWiM2n6gDlBYYO0O0O7pbbHxoipTC-ErGLiMy0qXQ5k5_MUaMu4X-iBDxmk2a_3jf4Fv1ePHXPHl3u4lqC53WGca01pgCQ8iYlCewjND52MWOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVXqUxMlE5QtkqwrvZ0EcdNMJoQJdJNk7_r9cJROW93k8d50DDu9iANAPEbceL3yC6ygYoOnJBpqzIgZr2gKY130WWXAh5jiPyZVJprqm92mqfBhAG1VlT4NRaWb2TPfaDX05nYJWvbysCV2LWji76BgueOFs_C4Ts5h9eBHw45ZJJ5ChWtSSoYbKjY20-k3ItOx5U38NTQ_JzgkAXlBa4mcFjXtsac1EUl4isrmSLLoOuLx6Gjx7X8ahkb5ES5pRuysvkPTe65gYf4vsWk3VU9OUyDhWCW6IaH2zMbFcg8UQI14HYcsy3XPdcTQCAIzv5DE3nX5QmjiH8dv_r4-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNAVHqf2HfjQf_qYXr7i0OtnH8dYltUG0SCjpNJSMrzWZAaz0qJxHMIvtEnnoi-RRUN2pz_-w8O8XdhtQHkaJjV7TeVwlMJQ0SiMYbIxNqds6zJYlKmhBGLoWsQG6rs5oLEB6y0cfYoSI1fsYtwg3fdD0V8zxCwgaMsKXV3M_ccB9aCDwbMHAxb5FhduBWtquTGD_g5bygeY66Kk-X_Z4qjxQUEMhKPxKoD0KrXwawoI9EGeILWlzZpux2jJuEPteSysqCOWn_mjqZ1LWljYaHkM6Rsj-zzYg4_yTfHqcVKzJeJEUGCX44kyp4UJYWzpBPc8o_QIkCl9kOhaqhLejA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRrgiLRjZXZMQLDgoDf-JcGLQEoSVN241Ph_2NQedlhzlZ6MmQa2VRgb6EFrFMZZM-r7KDTjxlvqiiL8nkPdfPdvVvE69giODnbiLz1OTH0H4WJXfZgZIdmrcCRaMp8-YopReJ1kR_trovcZIpTIZeSSQ7Y0I0ZljtW_KncSXcJZ2lx_l423_KvgCydtkR3Ye_U6iTXdM4AXcp6yj38BMsoKPcTscAHmh7dMxMzpmOUOEqDZdSoQjSrcBdAjUvWKL5IA-rpUUYDPcyraeh7d2Bhk40cTeE7Ko0bBM8zqTJn_ozhuJ0Z15_vtM7-O165xJWxZDeyy0Fjbw8Be1KL1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1ZRylJMg7_UU9Qm7EBrCTn5gfI1muIGDC22DdpcCQe6_tQTaALguGDyLeg99yzE1CqxWct1lOmluqjjpg_F4xcYpH46B267SquP3AKWwXjC7I79O4x2NTJyzbR05Y3JctOn-UC4kB38oT5U90R_IcSSxiAxNddqoq-dIa9GLsOKB0l7hKdJXtntXXYYuW1ApyEO-qt7MuRGkgmGDeruq4ZPVrGc3OfLOAdVDjV8h_RkJgXMGgxL_9ayon7pUo60OVHx55AOMaR5Vh-FZuejiZrxr5JRkfsEB9vVo-Z6Q28XLb_x7dzTDHe3EhrbzkVQ5paaU1wjW1EpgOFZpWERLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsZ76wPSpwRUDy07ZelJtITRglcDsZyknTW4MbriJEjy0AMwsCLEkOCbs8oO0dGSYppIGaYwc5lLPbZqcgvAfJmgaRDBv6nAmHW6P_PARZkm07hBcVnNzX11Ih2UqKj2tjQyvc6OImi0W7ZwrhnrLjpT5nkKe8-53x2i98er9aUJW-P_lLHhi3Bb5rYgwJLDPjbekmtwU7rWq3I7eBcKX9Z4foJiwbH0cyRokMpZR27o2XWqKbrX_sYqzoLyQo1nV2-bEnYKmg3wBm7iYLGR7FaSffsVQqBIGjdhO2iimF10NPHjDzU3ak03aQA40h1Dyo4ufKrrCqnpyMjLiGzkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9I1g0VBAQNhtklq6dC1MWoRCeUEhbunfjQ-v9IcypMU190Kchq12usDQ9D9mqvmcHibTB-sNzfwvFhlLzSPZa7buAq6xgW4Yg1Xh4cxIW_EH4qLIGSjGXmbGg01373SM8t-n1zb4Gi2puY8nZ9INb7XCvtgLT9Cyx2nM4td1b9quXFnezYJEbdLhGMDYOKJ9x3IoURJSXzPSOqygM2nN_WrdBQPtmUQCinvNFiHYD5IB6LF7xNhLix_wjKWwmPxo9pu5UL1RJpAFunJ_ZORTzUnPfDtiK5DTxfCH4j2Cr8DAa9uJZfscmVt78_beNAWnFu80V_LewHh9oH_MWD2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbGOhVcyDiOH5BFQJdRiFIjgu48hKIoZ_J8U68W0EbnrFMoCOLQFcyCMJI9pdU8HuX0jGa8Iwqk831atlOpOUYfCI8YTtwdXt8Z9Ur6Fbb_krspe_IC0zNoNjcr-Jxb-WX8CYiILI9NXlbeHidfvnlVD1P30P8jOVDrRHl2c7hlD_XDbHhoB7s-K_HKK9DNAvQxrL0uuwHWfXR7_VFpFsfwG4-UYCyodzk1QHYjsSu8CTdk5aqPR_ggYtjX9wN262oC0_3OPMQcDVMVqcaA1pe0LF4I-fzjHHVWvgPSAeXg7WEQF0M05OzX911m0f4EmHClPPpLXPRIvxSsvNf53RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=I0QvLOgeITxu2fuvI2M2PA1BPgjCVAxYw2cfmSaYXyBL4oDL-8nTAqrUNv3Pv96xD77WIEFdoRLSvTV_FixLCYLEulJMsIF9aSHu9V9nSvX1s8mDOgWp9sBIO-OnWTLhqNhcyrWDXklZnOl1rAL7JEVcvJDT9fJKfTDTluGfjTysv-JWndob6QkmPNHixqFWBaVZeRQfgFZsUOuu1iXJNs6DixCaG3OlzEoDUxuFtXwR7W2Fdx-OdjeBXCW8J_Q0vSFI3rVEcQQD7u2SMj77viz4Vnvd8VxYg0_I5DjynaJvYI0DoQxAQp4gTaSR5VH5W9D_WBARs5HC5ktjNdf6DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=I0QvLOgeITxu2fuvI2M2PA1BPgjCVAxYw2cfmSaYXyBL4oDL-8nTAqrUNv3Pv96xD77WIEFdoRLSvTV_FixLCYLEulJMsIF9aSHu9V9nSvX1s8mDOgWp9sBIO-OnWTLhqNhcyrWDXklZnOl1rAL7JEVcvJDT9fJKfTDTluGfjTysv-JWndob6QkmPNHixqFWBaVZeRQfgFZsUOuu1iXJNs6DixCaG3OlzEoDUxuFtXwR7W2Fdx-OdjeBXCW8J_Q0vSFI3rVEcQQD7u2SMj77viz4Vnvd8VxYg0_I5DjynaJvYI0DoQxAQp4gTaSR5VH5W9D_WBARs5HC5ktjNdf6DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viJ1Tsc9KE9t1lmQUaBU0Y6OvjwijUjhXO9vfHT1s21FAey4H17gQGctIWDG6J1pDHsKIxKDv268Oo8v4nUB7MHs7n7Ogwqtml9rp1_qykl4QzUJOQAOOHO-jcBTrP-9Zzdow4XGAu6vARdprIAHsnAt36Hk5vIR6icNTqewjVsNTQ3xpMu-LZ4KI2LGmaa3lQOcgeWlwCunrV6TV0WAwUY9LNFErTlyDH47so5PNxFFVcbsR5GzrZQ_8JBjFENBPHRcJdQmc3Z2WfBN1SBaDm_N1O1f1F2T_7GlUUPe8df0LXqGsIoRDnz-4f64GJyINyhKCUb4mi_67y2Ltw9RzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=sPCwBvs_DSbv5TAxNbZR567UpNVdmxo1J2JNWDmoLv9lrXR9_iSyKqlcTQDaxFSzwrLjOTZMpp90XUU0ix2NtIjruRljNrnNLGAopMjBkzu_icTqH1ttT9NLNIdv0EAyXo_BWLWucoxrCAKuuiOCjTwtSPUrbHcrHbK0yyyASJNkN65zlXcBqgmTnrhwH5XdatgZQdz3qbInEaltkZSI49Yffrfaj6-0N0qasilXaDATIF-Fo1W_Q4juZa3uvWUVG0wybcjjZmCX9Cov-9efqbNUqc6zvN-EPYDuOWZlU6tQPNBkjKjROJW1bWZbE0UmzHgZw1bJt5oNLLmwjlSbeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=sPCwBvs_DSbv5TAxNbZR567UpNVdmxo1J2JNWDmoLv9lrXR9_iSyKqlcTQDaxFSzwrLjOTZMpp90XUU0ix2NtIjruRljNrnNLGAopMjBkzu_icTqH1ttT9NLNIdv0EAyXo_BWLWucoxrCAKuuiOCjTwtSPUrbHcrHbK0yyyASJNkN65zlXcBqgmTnrhwH5XdatgZQdz3qbInEaltkZSI49Yffrfaj6-0N0qasilXaDATIF-Fo1W_Q4juZa3uvWUVG0wybcjjZmCX9Cov-9efqbNUqc6zvN-EPYDuOWZlU6tQPNBkjKjROJW1bWZbE0UmzHgZw1bJt5oNLLmwjlSbeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1uTBQIjjXr7T90RqVSJF447jkwGAVUqyvG5HwKJy23P5bq4cIaWv6T6J4bm1LEa3qwD79VcjwGZQ_rbVHK96e8sACx5dvgHyYt6fiiB-gV1x14g3j7cGqSeI7pvQnt6-dh189Ybse0AGnQNBkh6yIwSkIffmkzfKYtNGJL4neA52fcBjb8qNQz1vH7NDRRkbLOrDK8JlwntgnIwggmEdRA_YqWfzRVjD9xwaVtT9JX2g2YRIu4LzAD3DHMaH5zRLf_PnfiZkHc5sOR0cwurgHcW1Rc4apOpSDp6KLvCI_rtBZZUDHjaqHEd9dTH33C61wTx1TiMNn0fzXYsNnJ5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhig7Kv-jiTHpE5QXtUJ_-LfkL03ENrMXOgZJgPVtJkmQCwKCvbSasb8jtMuGebPgBzqsUJGM2n9sr7sRlylyGJolxCKFmoabeexFSfgKGeCsvC2Lpk1tqz_7vlLH5ck_BmIC8sxtEyZK9VzW4SV_yu8rNGF1Gaf1LFoAdemrP3mVWSF2HFdpjb5xA0ywBqSFP2911iPhFX0W6ZjsQqM4oGxRt4rHarqZ_4ATFELhkl8eLAPDxq5Br-XywgiwoUgttbQFNWVQODmkRNl2RHffYZUutF7CO2IYcL-kzi6tc3KOwrmhnyoUvzM2LtN7TSpV79BpcA7P-0ZJT4_k7LOBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=c2AgJQoMqXmuTq1tq2D3Vn-7fwnydwYkcla1F9eJ7gCpeuL1bPvCLOX-YZHSI7VysgBjoaCiUjYUt7MLmEU67C--yHRt2r7DiNJWgnkoLlhzApGi8LZvBYFU92NVDTnXEHCVdpQmzSf88Pglwc8a1Xy2rTVMw8Ru3pSJmQ6SPEm1yEvsWFO-ZhL3SjGTEjtd4j-g_sTjqZ0LRfQXOVzwPW8OkrrvrHuO-EVM1Yct9oG_bhH7N1N6e6Z1uh2QVbC1bEKXolaEEhFJGHOPWK58JBo1d52HHaMGTmA3tyQu-r4qvsZVAYMVm8VlaQXWHocTnHEMwdJyQ7lFpsvJ2bomGLb6xkBb6-hroXrN8FjucLzNBcXuRXekRNS8czN1hn-_cBVmq2b_kJ6gOmctN9d1odbkcPIoEyxxOs_AfzkQU3noAiogE3J0oFvuDUO5aj4Euu9jWQKlGWcNo4FRuB-UjmV7cUp58SZgd1pCSJYvSzmOx3eUqE49RqHv3L7uJ7phids8OO37HrlYzoy40Lp-KzCunwviSejKpkVouRNdLfvzOZraxCjtzat9NgMU9D2Q0xorP2OPri4ZL42v2N-oObLF6Nw6oANHA9V3nTwp4d_IKPrWFncw2KPP31Xu4sWDZqc9uFgvQ4cbgn2SXQqF3chNGeQ5k6QO6BDqnck-3a0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=c2AgJQoMqXmuTq1tq2D3Vn-7fwnydwYkcla1F9eJ7gCpeuL1bPvCLOX-YZHSI7VysgBjoaCiUjYUt7MLmEU67C--yHRt2r7DiNJWgnkoLlhzApGi8LZvBYFU92NVDTnXEHCVdpQmzSf88Pglwc8a1Xy2rTVMw8Ru3pSJmQ6SPEm1yEvsWFO-ZhL3SjGTEjtd4j-g_sTjqZ0LRfQXOVzwPW8OkrrvrHuO-EVM1Yct9oG_bhH7N1N6e6Z1uh2QVbC1bEKXolaEEhFJGHOPWK58JBo1d52HHaMGTmA3tyQu-r4qvsZVAYMVm8VlaQXWHocTnHEMwdJyQ7lFpsvJ2bomGLb6xkBb6-hroXrN8FjucLzNBcXuRXekRNS8czN1hn-_cBVmq2b_kJ6gOmctN9d1odbkcPIoEyxxOs_AfzkQU3noAiogE3J0oFvuDUO5aj4Euu9jWQKlGWcNo4FRuB-UjmV7cUp58SZgd1pCSJYvSzmOx3eUqE49RqHv3L7uJ7phids8OO37HrlYzoy40Lp-KzCunwviSejKpkVouRNdLfvzOZraxCjtzat9NgMU9D2Q0xorP2OPri4ZL42v2N-oObLF6Nw6oANHA9V3nTwp4d_IKPrWFncw2KPP31Xu4sWDZqc9uFgvQ4cbgn2SXQqF3chNGeQ5k6QO6BDqnck-3a0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJUa3BrglcEqsABzMBM0lq--7C3rqbVmmInKO4RaUXMAjfSnKOV1szXpIaicXs_0o4lKS_TTq5zkEwQeQJv-1WKE9RViVz2eR4Kc78cYqSQTR2zrNdQSf4RBBFpDuJ-NMaXKD2xnGi22Ybm9FHyd_c6c6_ai2um-7WfBBcbvEWWyiSZxW-_wCEnCVV1nEoitK78-vHpIMspuhk0JA_4c9vyGAzbdfI_SqUffubJyhfhhOOgNETiWZf3NTjDx44XqViSCM8cQnUe4DURYGz8lscozy4BqmzNgDKhiPhBceJuQ0aaQuJ4EjOl_bzkrJMY-oulnUR8biYVUkBvEOZSK1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7BKxnWkpbI27De_ZubAynJW90Q2m9PbQ9diIG1oilA00hUdtRyd6yqa5VeDvqteRT5_5ncNVqJXe1h_9QTwPOpuYIak81-QK-Ko_Cn5um3afzAMwyNOobhM0au8FBZpTYqzRDjJSblxb0H5YLsV03Oxi3sosfcvO9cwP81owmZX1sRTVrvFE1dxh6JPe8yKCxQskycZH19m0RoGtI0Cn7glMWhWu0qStQod3RxfeqzxS9EETkEL_mLpALM0X-PcVXOXZpIIxk9mv0maMy9T9lGfS58FxHKir6i7oMTU2ohChxi1ZB25Pb1R2KyT7AOTCagjhLq0oevCLFaZbSDqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG-kOz-OybqH9-QN8Vx6MZptl8aF9AEOGGfklYXKRVRQ-noMvexageVDIFAUhsA4wzTPxrJN-gIrYqSOkbym3CpDR18stt-VOgOBhUtSVnRiM8FO00SGFex8o2jZomgwxTVgu-6oiTEGaXTr7HzxGpApo09qj5ihs_u4AnCDhd_ZAoGjz84N2ojBZJPg351G_yGGqBzNFcl_q2KvzJXmT0qIvn7rPxw9WvzUHw_evXZ6NfMavIfW4xSjqaANTFwfgcOyE0x6uHMrD7zJiB5OiTj6FWr0_JL8zaD2NxVVMz9VrLFUDcjeUgF7FD5Yn50sfgk43_a2dogb6FVSHa9FYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=h3OoamNmYbd6wKOiCSKdr08yVW9mZnEDJrt8eBTXQq3YPATCPkpqDah5p2qgwIjlDu1mUM-BEFUAac2nsnnJ7gzVYVLeYttD-V3dEY0vv4JtuQ5UaVOf_IjRM1eWpwXThQABlUEwQd2yzUl5JBkcNmtu7ZT0KFYl2j4RFOn2jTKmxCtqAQYzcbuuUhcbYdtcucDSVBX0BE9ZmYr_ee_AdZFv5UWHi_Gcm_IcB2qnoRHv9AP-aZ6IVtidlHgwt-9yXbdyJq9bKdnkVzIBoxzqkS0YI7HyOxm1DLCIn7Cr-kjInhTEHWdVnb8E201h3AdPf2Jmms5nPgJ82VqAPrfBEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=h3OoamNmYbd6wKOiCSKdr08yVW9mZnEDJrt8eBTXQq3YPATCPkpqDah5p2qgwIjlDu1mUM-BEFUAac2nsnnJ7gzVYVLeYttD-V3dEY0vv4JtuQ5UaVOf_IjRM1eWpwXThQABlUEwQd2yzUl5JBkcNmtu7ZT0KFYl2j4RFOn2jTKmxCtqAQYzcbuuUhcbYdtcucDSVBX0BE9ZmYr_ee_AdZFv5UWHi_Gcm_IcB2qnoRHv9AP-aZ6IVtidlHgwt-9yXbdyJq9bKdnkVzIBoxzqkS0YI7HyOxm1DLCIn7Cr-kjInhTEHWdVnb8E201h3AdPf2Jmms5nPgJ82VqAPrfBEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MADi3sYudoxNvUMTpXDRACvxxWEug2tFVU2GBXpMEaOgsejA52ajRwbEMKx_zOHd5GSQiMJaIrq9hoqcv9Edp9z1OUuuJ0AOkgoGjBM0lDniQe2fL07XMCSAIqegYCie-rxICNNxZeT662DRzXUIES3iAJ9IDfC5Ex7enfUewPE9VDYzHBlzl-XB9OBvZLKzwJIttb1aAr2HJvRkG0yBtF754JW-WmOeZAgF2_Mk3sXavMP-dnBoNZ6yCMIlPte07Cl1T4xC8WiKC06fB7JKvCKKGcZyWy5M0gRWfnqy2b-CuXA9--739RTk46CD31L1D_Lj6gg8TO2vl4ZricOuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWJaFGhCkJgFgVRyb_7JZBXMfJXmo7Mev3xbq5BWcfnXYleuPhvENPTHzLH2pgtrkRx-UDjZgm2UAJQVcwKjxwtwncJL2g-iWKEc--bVbXj_MRCDCyTJXOkZEohxIRz4VM5BCytbItdOR_E1TJcbm_C-ZlgREZ6M7kqzV_Vhed8wuQdXJVSXmEkNUxTcBMvZ6Azx4k1jcLPkgBuqn1lvXJLcUc8J5-Mt-YC9Yjx3tceG1Yqf-C8IHyLUXmu8mfv5ZAacNegRjA6GkgQ4gZXp9xbzCeysoQetbNzBqylWuXUOMuJx643U0TU0zMXdDYxXEfuU0oEaKSVwGXKAwAxDYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buCb5dEIpasj7RGGgaPKoEjgeO3aYProFJd-nlmdNUd7LdP7_rs13fiBv6sOAqHZCJJlfrOcVfWUOsJ_ZUL8b4eSvX7bTjcPxCCCXFPKR84Sow-pPTCHiij-ysgzQPBnfZ0tKt1E8s-QNoXpQgN-5MFNugqDhrbnMi9kbGv925IUMpwL58YZpjzNXlz092wQc1L6D-RFElS_VSN6cVmw0u5-nLyKhMVkkXqRZfx9oX2Ej9ESvA0Tuq81nA8gdrpvySJbkQEbL4vAfyG6M0YqHTBYkCtQUtb9Mm28pHZHrUvKU1FsjUK8NUZR_qXZqW9-O31iuMYW2C7_169HKwlgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk6VERkO1v1vxCZNKYiH3_LNY5gY6tXCasYk_7dGMS2vIsI1OSpn6FQ6ssz63-QweM6v0EI0RyneEVMPenTVIEHLhtUmyzeBhPrOTyTtcGwjltwsOZU-Oms1KvI_n8vH5yhFHfAXKA3kj-WFGekiFuBVEmjSGQht-xF-YoGb6O_q96t1K9xFBcd9pq2gQN74aEN2xXHimb-y1VCk1eSFmxPIr2FLGzVK1vvFBHMEkIeJWPkc-QqASHKrl4oNgO84OJ-eAGY8fkeCWU3S8wpdgyiH8ZwzLpYxvc1j1fk3sBtDpEkGKCvQoipiagbFWaXS43d4ivVVJ1Cxa64ZX381ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1u8rT63_g76km50hD5ykdw6lztZ6tkNyIkyD88z9UGP-VrQ5SO54L8ecvWBr-BCY7Cm10WNLvyUIVupeUrC0M_oFHNOKnVBJS2urqbLKZZWX4UbIqn90OyQMmNVLatKVGdFDg_y9DmUHidogQCjJvL9druaaZA0YMeoHHscx9P5ZCnq7z-rJHtLjMZRysPPWuNzY6WyP2Layu7JJG5VKFByHwYS5m-3y-AHZQj8mCyZlQyf1nwgLcNnRnjcfmH4svd44B-8uJTeTqDO0dlHAGaVlQkLmNoJf27thructcBo8xi6xLd27tBLJ9-qVoOFUe9Y4GSzFo0tjg79sjLE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3zVj6fLPrwbEQnrLeI2jlFoODRUvnQ7P3R_hQEDUxeKTE2NVNXORs78X6kcna9LZhfOryTdtBs3ase-S7Jbff8BfCgir-GHFgfoMlnArYK14yLfE0RKr5BQv3fAYXmx8zxv18CkVOkPSZxvqNCoprWv5lFfjH1iXHBuqVcC2ZBDig_YhE1P0q-usu8UzrlBdL2AkXQJFHIbbDc8TrpETkQysxEcUXKk_X0FeE4Lyic1a4UmoL4TTL76B86lzlp2g3pOGUrvDR713j7sxo0rMQ40l0nOsbICtFeX22jD3FqIM0VuKR0VJQKLK1Iqpy5adUsofL-MGi0uR8ACiZEugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB7-Qa8H8mV-NMbXo22Zxnw32le_lEG2JboUCYYe7r5fQe-jjtihU_lmenTyct80OdY4K1BcGgVsH7Wdj3uF7Wl29bqcjOT4GkqXrwBptEO-phPYRucVjFgX6XKNe228JVpE0P2AbhStEhwV_FkOXlsDNnn8ODqkbEUdi2PdNhic0QHaPkvhxud00nMxbVTFnRneUhC6IbwcHrqzHbBvQy7VIcc_rRqgQwupViEKZ7W1fmkt0h3F0RnShhAvRF6Dqow3ZxHK8_be7-elMEju8MF1dYWz7DhWq14xJsj9_9kcnH3_Uix4KynK7HmwsMMUwqS1VHgJA46htSJneSBVlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecKbFYJ2ltHEMSRFJBiUGEJ31Aqw9pogoq42-5pQ-SuTLklEFs7Idj5cs70DVXv--QFHZCotxMdw6RlnQ-PrGWBBck3uaXiwFJioi4MBdPmZASows9x1xlwvRmdipWOrSvy8C7GbLdiPlLSGdC46GnNGlLjwKXSZ9_u3WRVz2Ve1xoLhM4EhUT5kE7EgLwc25ccj3qhLbKklDwJp8iuRk9HXqORs6K8ZO7QZfP897UUc1Kxx2TMQyXz_fzlk9Jg13nn2Ho3z3xYNT5hG2HHR-IQ8xdze_1chZQKphQtsE7acrruAwWfM6bJ6VZrwud5dmNa8Qwev3SRZHN_kHj4bLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rm4BPPK8YFjucbObSgVoOWgfAF53LqKLeAEkipTD-peomrlXBI-MDxYC6-kbgu6qm4qJ-mv-t-ulB9UehsZ7LBS4uKXHtQ884-8clfhCt3YcJ2xfGHOiTtL7kLWtbXqwvr-nXjxK1Qdr__bILU3jEbb5EGbjErDpsnBSbkCPhcNvxmg78o4e7KoIDXrCOmkZZ9Frwc4AXNgpe3HheT8VCZ4aDhPLEen-o6Vvd221mX9gUywka8fsrGFjzmYnezKFx16kFbWxmj_JiQdiHgo3M_logHqolthBrHZ3ghyGlxiVqr-1MSfGlvs1mofPsRfkYFBaAWtf_zq7ggQK1cusEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9pxv5dYU9C1gT57AhDB-LQtcIvp2-LmhoiWoeDAbMedY4lqS2cWc7VudFHUytgE8Ei0FtJVDXHS_gNdMV4ic42PjjaWWS4JdnOjeFn2UNL9s9sEMZWLH7Mrl8RUjiMbSoRQOfhNS8FGwolL7_oyEntwsE4aDEF1Ld5OrZdgKzwXNHp4ET3a7ajKqddmVXXtxOXF6T81Zjm6ALhTvg96wzkdmtREvOq244ua7DVXxY66vh5Q6uifggSZsPrdxmB-D8NM4p81izvx3913NctwgEhk8H4ip2Dyl3OHP0vAb3vs4Hm0Ds8H8gC6O6QaN0gRM0kMAQZVXQR4LpqQTkOscw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=D_u6M3e0YpfDliJiMBMIMOEQKlrnmMRsHvuHtOvE38RV6IynZjAyj1cb3sZbDvpafoLR61H6VyKFWyV-vRbfvizaEwpOTpEalvmnhqavfxa_dLOGxRpnbmAfQ7C7YyGD2QyGiaFEyqQfEZmYjQ9YUEIk5LaZYI2Kf9F3TgMPMxUblO4KueZv0rNm95cwe6c9CTCEup_m9ShP3gzAROCWo69kh-rO444YQe9G7y0VtdMnJKh0S6pWVflUm-1MFIjBF0wHBvK2XjyO48EE6RW3gq5PCgYlxvMUgkIKYNunV8xIveiURbQbffkUmQk7_csOXRclqS_O9MmqzGIKpDzbhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=D_u6M3e0YpfDliJiMBMIMOEQKlrnmMRsHvuHtOvE38RV6IynZjAyj1cb3sZbDvpafoLR61H6VyKFWyV-vRbfvizaEwpOTpEalvmnhqavfxa_dLOGxRpnbmAfQ7C7YyGD2QyGiaFEyqQfEZmYjQ9YUEIk5LaZYI2Kf9F3TgMPMxUblO4KueZv0rNm95cwe6c9CTCEup_m9ShP3gzAROCWo69kh-rO444YQe9G7y0VtdMnJKh0S6pWVflUm-1MFIjBF0wHBvK2XjyO48EE6RW3gq5PCgYlxvMUgkIKYNunV8xIveiURbQbffkUmQk7_csOXRclqS_O9MmqzGIKpDzbhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=eFKAiQV9v3xTxLz_DiYD67Te9P8HCs6gm3JAa29Vwiw4V2I9HDWe1TLlSMJkI6dwWYqNR8lufbq5ZZ-OLzjUfAmddk5vmHzTRRpJkjD0U8yYXWtr1Ie77mdl3f5_za4NxLKVPC7L69MxmNIbvw54BpEdFStoH5Jgq1U5LXpl-F2IUhVnZyU5Ow1xpUmPR4QSuONwetx0hz8iiEpXifWyb5CYOMzBKxKFpLa0evvsBSY_R9L4CwZBm_p3cmRrY25d3GZzX6lSd9mDz4yq3a_0boYxJg8awli4bpU5riowv4ZEDLdKDKTFhkCRt2t81TSPxuFNyUSdM-Tzn651_11v1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=eFKAiQV9v3xTxLz_DiYD67Te9P8HCs6gm3JAa29Vwiw4V2I9HDWe1TLlSMJkI6dwWYqNR8lufbq5ZZ-OLzjUfAmddk5vmHzTRRpJkjD0U8yYXWtr1Ie77mdl3f5_za4NxLKVPC7L69MxmNIbvw54BpEdFStoH5Jgq1U5LXpl-F2IUhVnZyU5Ow1xpUmPR4QSuONwetx0hz8iiEpXifWyb5CYOMzBKxKFpLa0evvsBSY_R9L4CwZBm_p3cmRrY25d3GZzX6lSd9mDz4yq3a_0boYxJg8awli4bpU5riowv4ZEDLdKDKTFhkCRt2t81TSPxuFNyUSdM-Tzn651_11v1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U78mxemw09xHno1rEy7-1HdTpII3syd5nVOra03zjFP_Nc6fonWRFtzdJSUS2YpPWWG-igDxWjZLXjB9-ai5Vdq4gWrMxat71rsqirj_IDW4Mgavcx6i-qgoDcEBoicf9F8R-ZF0zm6kswe935VQHldAsivIpaxX1EZ67dWxGY2VRduVAvytFVfeGdWvtId1TuhSf23EgNZ9vA-P52luwcG6sXeudqy-jTHhFfFlJNevzq0HVFAy0JONVD_OFse_L8iH4YFXZuygTKJINKE09mVHmZityhFnzZ9c7xJ3RXsqWJISYosh4tFoQvfbps9VlZqR-CalVa_GyvvHP-7rsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tItCM9HqyshKh5zrG1CU0-O8iVMj4jNILMu1LgwlRSZMSNHnnD9sYNpHYMWX-kAdudW6cTjqPpVECkNviB8ivYy2g1N-r7X_Qs_lz0MdKUjPGCnj54BUlDTK4tXQfccDXTludkyuGYuo_yXoActmcaZPqeqSS17LO5ujgosY9PQh3T3KjCisgCMJvU-2SYDg-eVNIRQ3KfJh8f41Nap3Pfy7xQLMuVbSdhA6h2n3QBb9zbb8aqt1Gpx2H0SijhNSut1-ZCOM9QshA_TwFQGN0SZjfdzMh7R3yW7LisfYR4iQKKvDs1JcgulxnB53GJGPOnsmPwuTw-Z0hFgmWEyRSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jqwe5d4J7bWvrxHcu4XZsG9Hm1bjlBI4JtSgTcrqDuz9-6UMoSFzVbIwDQ_vCytAb0adCqT51GDrBKaKlDAyg3cy46KEHA4JJh6yUIRfPo-OM0D5nMEucaSw8F2CKX1llNB7-WSixIsJ1Mk2yYnqtqCDS3R0rsBkXkTg0_Ouu5S73Co47QVan_1oh4ZAtU1ua6oX53HpC-jvoIkUe3WdIIcl2BHIgd49f3GC5jn5ZCf8e2B3XTzW-4nxj2bXoZLDyOeVT9MmAo9s__3J_PD7DNoVoGgbMoclR6CRi3x0kSxDzCPOWIQF68Ho_8xby-cr92FndMtse0CdjwvOBC10xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlkN0zI8pLlsDMOY2pby2b7EdWJoKbe5TuRwKd-uykanj4RV1rm9q_oRzVzfiP6hWajYo1k5V7pv1s0u86k0ZlXRs5grtlin4uqCL0rxK2ahOV7sEYQwAn30d9yajPS3GJUwxBS8DIdfye513x4M_3ovjEg1PiEnrRS30CDMjr4BaWuqVjoCOU7oA0NiojDQ-_CjKeAD64JDct1LAwoQA4LvPNOXccEWwwvwVp7NX6bMijOUTDmHNor0wzR06vNypgRFAfiFJEeaA6SaBJ0Ae0Wg8AyLSFRjb1E7aDtmtYtrDut9AB3Pbx3wFKmbym8p3Qx3C-maov4wua3LJ-mXaaa8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlkN0zI8pLlsDMOY2pby2b7EdWJoKbe5TuRwKd-uykanj4RV1rm9q_oRzVzfiP6hWajYo1k5V7pv1s0u86k0ZlXRs5grtlin4uqCL0rxK2ahOV7sEYQwAn30d9yajPS3GJUwxBS8DIdfye513x4M_3ovjEg1PiEnrRS30CDMjr4BaWuqVjoCOU7oA0NiojDQ-_CjKeAD64JDct1LAwoQA4LvPNOXccEWwwvwVp7NX6bMijOUTDmHNor0wzR06vNypgRFAfiFJEeaA6SaBJ0Ae0Wg8AyLSFRjb1E7aDtmtYtrDut9AB3Pbx3wFKmbym8p3Qx3C-maov4wua3LJ-mXaaa8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=VMfn3tGJbT5PxI13qYxPoQXumXTbHarafdi1b9LMholIs2I46WYbJ3shcLpPy75uIQdPOqg5x6cA-Gwpo1_9Mvlz6lp3TNLxvTPk6SDhxthlZaqEYhPyTlrdX_dUnhEWpjhHm1tUk0xil7qpNy7BwhXFrYqrjmQtuj9Puup93s0pTqPRD57wSMExHDt_US5lvpUGtBlaCq0fkgn9nI3TjtBGAjcOWUKsHMwhLZ1gWwh3raQlyFUXz2KvP4N9Mq8D4lVWzhKucErEHUAU38hwaVxAYIfRHfseuWQnob-Uzb1oRPKn8ALZyoA7YMh3_7mbOZUzivFkXhQfmkzpLt7yCDX6lycfIt6OLvRb5v1_qC1erFRCN1t1CVE9AGSvNpwM_4TaOYQdTAuqYqOnvZdg_TuZPdp5HInUwjfyWsnFnJA-H6KEOy-a2C5HEBOvoT3QTbWZZs0_mN5hSGWABPhQbfElrTRDNzzXocXu5FRHs1UJF7k0Emq5LyDnvdPae2MTD1uJQDrqN2mP7MT7Q42DpZPPZLMwiOwy3nI1TxKz9PEKdtjMqwAapkYkAMoCDQJGZlaoaR6-vTfA0WTI_HfSadP5d0sIUwhamwOM27tqQBP63fn-3ATFw48ioSSYS4CBwDRWerDiTuGz8xQIsgPjkSNoXCPFo5ZpcnT0Fk3u2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=VMfn3tGJbT5PxI13qYxPoQXumXTbHarafdi1b9LMholIs2I46WYbJ3shcLpPy75uIQdPOqg5x6cA-Gwpo1_9Mvlz6lp3TNLxvTPk6SDhxthlZaqEYhPyTlrdX_dUnhEWpjhHm1tUk0xil7qpNy7BwhXFrYqrjmQtuj9Puup93s0pTqPRD57wSMExHDt_US5lvpUGtBlaCq0fkgn9nI3TjtBGAjcOWUKsHMwhLZ1gWwh3raQlyFUXz2KvP4N9Mq8D4lVWzhKucErEHUAU38hwaVxAYIfRHfseuWQnob-Uzb1oRPKn8ALZyoA7YMh3_7mbOZUzivFkXhQfmkzpLt7yCDX6lycfIt6OLvRb5v1_qC1erFRCN1t1CVE9AGSvNpwM_4TaOYQdTAuqYqOnvZdg_TuZPdp5HInUwjfyWsnFnJA-H6KEOy-a2C5HEBOvoT3QTbWZZs0_mN5hSGWABPhQbfElrTRDNzzXocXu5FRHs1UJF7k0Emq5LyDnvdPae2MTD1uJQDrqN2mP7MT7Q42DpZPPZLMwiOwy3nI1TxKz9PEKdtjMqwAapkYkAMoCDQJGZlaoaR6-vTfA0WTI_HfSadP5d0sIUwhamwOM27tqQBP63fn-3ATFw48ioSSYS4CBwDRWerDiTuGz8xQIsgPjkSNoXCPFo5ZpcnT0Fk3u2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
