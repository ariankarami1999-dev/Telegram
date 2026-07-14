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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 18:12:24</div>
<hr>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=aOWdx-kjqpNlLf_hjd1eb5E2Sk6qQqxN5yqmFeN-NyKk7KCPsSEQvt-PKFPbNUvN_toki5Uc4P1XZPv9YpHMVCqyVZ24I_h8Kp-VIrWOrx-A_feVKJ8tyGog3A-WApFMHrrRqPDGkUFqNOJcV_nGheECSiOkpGz3jHbrC-PTsoyAWkRx2BcQgW-iHqeLTBeTwzKjvDrqW5Rhzcu3eEbbfECTLzW60kDOE-1eTewufalRdFXDLCGNLlYtzBsr2N5FXM0bMnPyiY8vC1KqQCwaN6gO-mOn4OHkAFnfm_yUFfCfVvAoEBTh7II_LViYFNNJKi2QqNe8XM3AD2fcE62NYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=aOWdx-kjqpNlLf_hjd1eb5E2Sk6qQqxN5yqmFeN-NyKk7KCPsSEQvt-PKFPbNUvN_toki5Uc4P1XZPv9YpHMVCqyVZ24I_h8Kp-VIrWOrx-A_feVKJ8tyGog3A-WApFMHrrRqPDGkUFqNOJcV_nGheECSiOkpGz3jHbrC-PTsoyAWkRx2BcQgW-iHqeLTBeTwzKjvDrqW5Rhzcu3eEbbfECTLzW60kDOE-1eTewufalRdFXDLCGNLlYtzBsr2N5FXM0bMnPyiY8vC1KqQCwaN6gO-mOn4OHkAFnfm_yUFfCfVvAoEBTh7II_LViYFNNJKi2QqNe8XM3AD2fcE62NYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjIPXzCbYPwjFi9oe00DJVtesjM8S4PFKJLr3g4b251jI1q8a0Wwxy2JolqH3umtm-vobb_2Bn7_mBadHvUIFAk_hRvVRbBFRHUxg5e7Hv_XQrRL28sh31xCgjk6mbY0lR1NTfvNN8KmTFUUemnVXkjXf5ns3POtZsFpxfuVQF2uLSf10V023zCc90QXuFmmoqTi5pw4vIIIoRTG6iEm61XoPIY6tN-s4kMnodT4HA7w6s21416OCh30JnFd4RtDGHyPauEQD4qLTjRgIoKXdhTNz9DgC-o7Lr20m0a8-dHnChi_24IrBDleutOkXo3Eg_w3iQEfgrKi4Jc4ab7Y2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-cfYJQNLiQhORzcP8Yw_97m9JovkSFq8nUOZxJpTfGXIMupYO6eNxllsMiVEPfWEaKp7AwRPa6O23oe71cTJkd1DmuMjcGvCUup3qc0skYAWlaIgz9RheD7BvR832qfbgBNp4Pp6f_vkBn0yJXBvW0AXykzxmZt-erxBEx04mF88lip38kqomYJXPPTjTLTBOCvWR6xE5MNiKDDaxNscdxf3imM2gO4D_Ujm0oYHCAyQLYladGlSolw22O98SnjFgFUHJl6MFVZactJ1jtVWJt-KH7cxdViRxenvlpVCbe_l4Ibbc3fx_r2enx1VOJP7U26x2oLbXzoKwHhX1dnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1f61vL42ySxQn5kYMCloRcoaUAkfAtXCjC_lNTA0zTKTDWkOQy_ZWZfgmhenzwH7EdwIPX3IUij3OHPCgMi2KDQIiJ33IS5-eZECTj7rLA8Xc4TO8Eke7v2MO2dXSL7Wz-S-Uhvl9BAsodrP8dylVH33cX8ktvdGZmshCvOCD1J7X04Dl98qBTAA3sHfUTTIPB7YT8PRVflBfyS3LHm5ihIH_S14XgvhZcEpTbJUbBUviyq8e_Lk3AaSCkCSSrvGiRylZ8fKHkdB14aHaJGh1TvjV_oyJsZEcmpe_kVlcAOwz6Dv59yJsV0qQUAH-YXt7R1w6XROe7UhLx9z2nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_kWza-Ol5frBCLnmexrS8u2AGjYT1ApPyNVoG9lA7ADKY8GXUqknQoT5TwQOHsXDVVVZR_9EcdpFYnYBtCyg4LFBNWNyyR9utQLCD1so_xACpttTuWNYYtvQiHkoT_juGVOg-wQ4YMu8dZ10-cYJ29au0z9POgXSGSDbP5Z4MUdPzDuy_Q0smSjBqsXrdV1rpjViaKFFJMKYlfsakYct-xMYOfZC_6AEsN9texy1-zCWxLDyzO6yaIzIEm2xEaB59HKDVcAEjomeM0acaBljhotP-2A4_x5l91AX6BbrO7RWr9naJ0X3RfVrmoKke3kKi3AkcKEB2jmVT8Ko7VZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=hfRSnnbkj_HzC68nSfnbs963_4hK2ggiFjJJG75xUFcdfIIMWpK-U2_vyiYPKrVzLr2XAiYoTpeUWPIdK2pqoVyhcSu2wYUvaEB7zxhueKhQ2b1prH1NCD0-3u_Nc6jNnA5o1qpqwuWh_sZ-b-Gr7Lfsie8zFypXe58IAoWvKqTtMxuQzqnlLPB-ycnF6L4gGT01yaptfGoDCIrvnXJdNNA-oJ6X1BzQ59hWpr20w3Jmo_MeDL2Jeji6H7A6TedWZ1p5EpKWnZgN_qqJDsZJ9r05qbCq146AUDLusBHTCcFz40WTNZs45bPa_3ZN6tKDFl1zYqToImBJH9XqsHzMXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=hfRSnnbkj_HzC68nSfnbs963_4hK2ggiFjJJG75xUFcdfIIMWpK-U2_vyiYPKrVzLr2XAiYoTpeUWPIdK2pqoVyhcSu2wYUvaEB7zxhueKhQ2b1prH1NCD0-3u_Nc6jNnA5o1qpqwuWh_sZ-b-Gr7Lfsie8zFypXe58IAoWvKqTtMxuQzqnlLPB-ycnF6L4gGT01yaptfGoDCIrvnXJdNNA-oJ6X1BzQ59hWpr20w3Jmo_MeDL2Jeji6H7A6TedWZ1p5EpKWnZgN_qqJDsZJ9r05qbCq146AUDLusBHTCcFz40WTNZs45bPa_3ZN6tKDFl1zYqToImBJH9XqsHzMXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLs8ji3SRbTfV3557QN4F6aIKnmRJizshBzGZZCrlXmIqjxIYWo6YPMU1hD-7WwAJ1qbcC_6H7868CPlQs8AgoOpAbh38w4Itb-5qlooMxNny27vR0WkF2kTj8VSgP-x1Oqo7UHfpyBIGenNj7NDWHtaIaTuTALV7JORH5U3jToabNGZc9KKQ_8ZwGviSs1ENgKEXTXa5Mcd68CDsGK0ltsqx3S9JCVMvSgYcYsSIa4JOXHwKt8TMU0XTXZGANQ6oxcdFTUf-W890Vgn61_RXyi5SYPaLF3FWiEHcWZIDSi-CU1ERfewGmyh5m2-3Erfj0_IGFcW1EohBt6DwK9miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=UInfzEqdhosexGzjsDt-5A0DaXq79q96LwtLsdMXGq27tFA4j1CmS4HomaYpSPzu3KoXxCjYFGyp-wsqF9nPZ-7-PH4Oyy8OWNr64TgYdFq9sDGmsTDDFfcwpCZBMOwU8idbT14sFdw78Tkle7B_PoookUISOP2uZXgPqWa3dADcihmRPu3JLU8G3UaFjplPbOWHb_0DYroxslw1tCdU9H3v_8AKWf3irBAl5mAOPGfTpjXOg7Ikwn72r26XkZYDPctzJY5Y9f6mLq_43biOC5_EOdffhtcj-qQkhwkuEda3dPl_60myPSaAwxeyquHmSEauFdsKeM84jWoZbf2KUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=UInfzEqdhosexGzjsDt-5A0DaXq79q96LwtLsdMXGq27tFA4j1CmS4HomaYpSPzu3KoXxCjYFGyp-wsqF9nPZ-7-PH4Oyy8OWNr64TgYdFq9sDGmsTDDFfcwpCZBMOwU8idbT14sFdw78Tkle7B_PoookUISOP2uZXgPqWa3dADcihmRPu3JLU8G3UaFjplPbOWHb_0DYroxslw1tCdU9H3v_8AKWf3irBAl5mAOPGfTpjXOg7Ikwn72r26XkZYDPctzJY5Y9f6mLq_43biOC5_EOdffhtcj-qQkhwkuEda3dPl_60myPSaAwxeyquHmSEauFdsKeM84jWoZbf2KUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdHmmXXc8trK4MhLiSE1bUtB2v6rcX7Salq4kn_F1IusKTO72C4-YaI8YlXNh1vkLMQMOxucCwz6GU5llci4M1SRzmlafcaiOKxGioWAd8thNcibg50z1-ZHMvnVE_aMjfEiln4vRb-OS2MinECSfoXoIUo5n_kYQTbuaogn631BzbpuWoMBE6yVTUC4Fzyux4NVJNg_2fAoUXEDT6c4_w-BP1w0HQMy2Rdg5SNjtkNbxhRLjYJlbFLzolJvYgux_NIMsuGcIP6XL8hQKoWlcK6MeYp59d7mcj8e2DrZAhnkm7e9OOrUJEIR54KCDt6uvPyYT0MLKyf2JDNXjQvGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-fadso-ziuEO0QUUQtof1oEqVhB3Yumjn5Ut1_ZCQghERLw3OE3oOvjqNRoJAxHr976Hj9gfnbra71EwzIIjG-vDspimbdqF-kLhDrGX7is3se9Jx8evGm3E33t5QGqcG90cEdCM6J5y9gXgKGogDxrIEJtpGyD7pucgJ-Iskm2_xhhBVcnAuDHkqcjqRcdSwxLaEpuv3dE2HW3QgfuFgbWUC8F_wCm-OwqSL5SJRUrJCYawKIdCDKBd86XFPfM9qo3OR-ZP11v30FRCPpm5fmiWva98xR36QXrX__jI3qefGFP3faWaNGuHnMnOikRrJH60hcfIz9Vzyu4NPvo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh2IkRxGq-6-ePdNopCx9gJoqznIHYG-NCBtM75dT4d5RfDGkwdOJPtujB5oAcHN1Co5d1kemYAqd57w0oWlRRm90GBI39cHEF6De1gpt-MUc-Cr8LQlRnsularkYU1_ggigPOPsDWGtLqT5hBmmsCDgmhARfd9CAd3BfYLnAUF245d2UhUiT41V16gE7T-tioKPGGDm8NsBY1RBPLRFVVUG9PHCihsiqEV757SuzB1CWZgMBUkv2HOVvWhaEpkC9-Nca1Lcz_ZEiSpmB5i9O4DAmej5Il8OfYy7ikP1d0zb945PE3MtVEnIoyM610kXFK0LtsIt9_cI9yzH_NX9vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtKUGlMzf3zS-zZS4KNzyXi3_v0ZyOD4Ff_srwvTZsGXrA6eaoQ5JjWSIEEvwcQ9jzFGzNfImYBgqy8vyfliay7ms2kUAmW3nj5HcmEAtO2zqr1WbAy4pfqjsyS__-U_d3hBrexhUh-L6_j6_j1mmeo71IYV0ibEkVc_uyen0L5WBy8P6Olh-nWNc60e-1XfjucYtJMeOGE_MAU8DXhJ9bLNRCdwp4rEBuiLJOkMp4D3dOxKf5AvM_BJapcTgDvNKc9fL7S7OOhrLGG4Di3D7v6A9l3GUGgtUtPs0SWd4Rdd4yl4D_rHMUTcOoU70UdUZTdMDwTl_Pl1gvYrRW9gqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3pQBZh_IzXkiwLrEioWwiGLkxwah_KsoSPmgrYAdlljy3_OzsGX5y8h6MOSI9Qe0QRcfHIhSp-B4Nz6JTfr_ZdnpGc7vSVdhk9h6DV_4ejYC8xfKHm8XbwtbeqLaPILsCEDJKNMYSTetUWsXD5WxlIDDv28fhsl2SvI7uEItEH5jD8R_ElgYv_vj0KYjtl_l3dXaLrLy1_90UPWL-JyXT2uXy-VeA7wn0hpNjA_4GIyqESQ5ZpFz7mpnueGrAqBDI5ETDSRr-fPEqd5SHpkC9kP5aA3H9Iji0M-PPOBFF1SpFWEhBy_bkOaJE9Y4N4YoYTbGqBbGFxI5oZtZ7NNexkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3pQBZh_IzXkiwLrEioWwiGLkxwah_KsoSPmgrYAdlljy3_OzsGX5y8h6MOSI9Qe0QRcfHIhSp-B4Nz6JTfr_ZdnpGc7vSVdhk9h6DV_4ejYC8xfKHm8XbwtbeqLaPILsCEDJKNMYSTetUWsXD5WxlIDDv28fhsl2SvI7uEItEH5jD8R_ElgYv_vj0KYjtl_l3dXaLrLy1_90UPWL-JyXT2uXy-VeA7wn0hpNjA_4GIyqESQ5ZpFz7mpnueGrAqBDI5ETDSRr-fPEqd5SHpkC9kP5aA3H9Iji0M-PPOBFF1SpFWEhBy_bkOaJE9Y4N4YoYTbGqBbGFxI5oZtZ7NNexkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=mXfLmvoLsAKK7OWUOhGWnk3YOjYFpuSkkYAlMZbKmwq0Bk1RVWzztTpQ2kJ8Ie1KTeV1WphO9KSVXHb3nBoohRytPwxfVVjlbzfMONiBIw_6R4SFKrbQmQMNGpw9zgVqvtjSnaypZ64usHqyenJpAl93Xe9yCrBESY7NUYPk1VgYxBiowggBrwx7_AALx_Za7PSWqdVbKm8oLjMxeE3fTdE_PCQbBnxdQQa-4BwnaFE4G4TJ_wKAq_YL6HIqfZYlaW3MRl2s7S0JpO5K1qPMauUmVCBoYtuzhX6GYF6lELh-3S8-ikuSm_qJC0H2SZcCfUk2NOm6i3OQTNU2a3d-hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=mXfLmvoLsAKK7OWUOhGWnk3YOjYFpuSkkYAlMZbKmwq0Bk1RVWzztTpQ2kJ8Ie1KTeV1WphO9KSVXHb3nBoohRytPwxfVVjlbzfMONiBIw_6R4SFKrbQmQMNGpw9zgVqvtjSnaypZ64usHqyenJpAl93Xe9yCrBESY7NUYPk1VgYxBiowggBrwx7_AALx_Za7PSWqdVbKm8oLjMxeE3fTdE_PCQbBnxdQQa-4BwnaFE4G4TJ_wKAq_YL6HIqfZYlaW3MRl2s7S0JpO5K1qPMauUmVCBoYtuzhX6GYF6lELh-3S8-ikuSm_qJC0H2SZcCfUk2NOm6i3OQTNU2a3d-hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHFxW1GEWj-QEalZld2MPWCuSM32L-N9TLFdTOlHr22jQB_0_FeinGimZ3cOTV6JSih9SZ71P-J35powNB6pDUjKQgPSuPgKZWb-sD6I1Q4so8Xa_RPdrmT1NFJdGPsG_-dNFG8v59JZ_ZJ6f6aqz8osRjWvBDyA9nu38A47qAiKXx59RgdJCFR-3IEtO8ZwvdquLbgTG5nQMf2_hQSHjiqOo0vNxkWKUc8MaCykfVIFAglY4SbzI4UOUd--2-_EE0TfaAv1iVwsOKZtlovJ1ka4Fh9dz149bZ9TsbdtzpRgBoMufItPvslTNhYk7zCjOixHS1gpzE-GJYal6EA8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1fL83Zlu4N9sDfh1fSVhvKQT0YxxKRdth8r1h0Gzw4blMEQfQnncZ-9H1XnIGYZetr7sL2YHNClmaUv0c9MJRXnU4rkfjFaXOHr38dGANGhrXwK7yb2GUutUSoMeQS9iJvoWk7agkKJgNC0JkKxb4GzuP-wrafoCGoS-yvX4ERiB3DGyZrscr6pT4sEIKmG2SIeI6pHe1unk4t5oHCnUG6EeySVtVrKp8peAd_9ZM9CV3L2Br1Ay8TPnjGc0-H-seyllZiBiNxfq5YA6P_736znCbd0yTm3bwYagbVN_vJdScII0rSK_JHtZiHmnRRotRWFkPIxtm6COT2EKP_lbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-arePFSeSKRz7hciP9rU_DOGfLrMNTepFRBVKYko99VoUqF9tZg3zBnnNZeQRESZPL4oz5T9X52gOcxEYNDlOnsk0Z7WC5hz__0e0cL7BwY0jBaZkP2Bd8QuJ_0PbC0JnPdT-7blxZ15HsjYOAqJHuWEI44584H9xZKk_IF-lO5nh6JzCIQWfxLix7P6ngGFAn-k9FQQ-LJY18_F6DdeoYf-wdr8uUSYu03xNBN9svQR5qVowdBOcZ4xVYSZVvKxSoZJmd4rs-EDFLJd1kcesidg7D3HcJfWk224DxI2b9rNfMI0oZPr8rYUjbvIE6fUYWtw6rDR7x8TuLOU3_J-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN-bP5X0Lu0t7J3XEheiNFMnKSyASRPYNAVFv2SZ0VMxyD1DbNDeLulaKBpxH0WGPLVyUdATpzNWXtyWNGinvTYDDKlHd6rA69J--naoScDHtqq15x7qsl9EdCQIcuipekv87HQbZBoiCnXING_5zK6qafLQXMNZSSDTaHrJucQFOdXCKOxbei9cOx9uXtLB_o6aWCr8zuJkXsg-8tumqar5tFKP4CHqguAXATHADF9E4OFUl3PwqVsQkzoXFHvPn71LemYEVECHXKnPmzgr4VQiMDIJUOQzbVlG4HBr38V8S4jcyXaTwTeMvZLoiz66yuApeyt-zJit6vPEuOJPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atTQz8glEgwmRxUNmTXrONydn-Yn_hvuXoQrfOQUa63yp_Mk2dn2gqkGtDh0nY4vWsVsAGZc5zUgU0wcl-TS5n95h1ujl_MXwgVr3sI_l1CUsDLSQAVBM3sMpYA1fYemM_MauR2YQMgPiSM3PjD5i9kZTC7DWg1SMmmYYJJ3EU5Hv4voWX42oXZYzIjImneoPxio20HopD-voqpanq7vv7cBBbfhD36HKJb-84-Hn_FJgOvfLk4wjBNVPxzlysjARkt0Oosy2Xo8z8l9hnJXWWXmPxuFfHwdzIp1P3aJqQ_wYc5npLBgsxYdAGheGO8wSpuSi8Cj47NrF67pMatpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhaLjz4rTCB7D8-iarnceKllEMWd63DdYMOSni3i9hB7jZ5hI8yMpgtwA4aqHJ7MO3-gk3s-zEwMbqCb_-nheLnj_cDBHwnQ-ZcH-PwN3OLreeFEh_hQfETRBoAwTzTPAVSPqmoMDSDGX3mVaDSd9FulJc7NiiAywqQM15jSlCm1_xXWgEYPYKNvq46BtHUISJA1Ti1SE8z9bG1MXekzkHlHitfj6Xvv5znEDS1RWiM2n6gDlBYYO0O0O7pbbHxoipTC-ErGLiMy0qXQ5k5_MUaMu4X-iBDxmk2a_3jf4Fv1ePHXPHl3u4lqC53WGca01pgCQ8iYlCewjND52MWOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVXqUxMlE5QtkqwrvZ0EcdNMJoQJdJNk7_r9cJROW93k8d50DDu9iANAPEbceL3yC6ygYoOnJBpqzIgZr2gKY130WWXAh5jiPyZVJprqm92mqfBhAG1VlT4NRaWb2TPfaDX05nYJWvbysCV2LWji76BgueOFs_C4Ts5h9eBHw45ZJJ5ChWtSSoYbKjY20-k3ItOx5U38NTQ_JzgkAXlBa4mcFjXtsac1EUl4isrmSLLoOuLx6Gjx7X8ahkb5ES5pRuysvkPTe65gYf4vsWk3VU9OUyDhWCW6IaH2zMbFcg8UQI14HYcsy3XPdcTQCAIzv5DE3nX5QmjiH8dv_r4-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNAVHqf2HfjQf_qYXr7i0OtnH8dYltUG0SCjpNJSMrzWZAaz0qJxHMIvtEnnoi-RRUN2pz_-w8O8XdhtQHkaJjV7TeVwlMJQ0SiMYbIxNqds6zJYlKmhBGLoWsQG6rs5oLEB6y0cfYoSI1fsYtwg3fdD0V8zxCwgaMsKXV3M_ccB9aCDwbMHAxb5FhduBWtquTGD_g5bygeY66Kk-X_Z4qjxQUEMhKPxKoD0KrXwawoI9EGeILWlzZpux2jJuEPteSysqCOWn_mjqZ1LWljYaHkM6Rsj-zzYg4_yTfHqcVKzJeJEUGCX44kyp4UJYWzpBPc8o_QIkCl9kOhaqhLejA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRrgiLRjZXZMQLDgoDf-JcGLQEoSVN241Ph_2NQedlhzlZ6MmQa2VRgb6EFrFMZZM-r7KDTjxlvqiiL8nkPdfPdvVvE69giODnbiLz1OTH0H4WJXfZgZIdmrcCRaMp8-YopReJ1kR_trovcZIpTIZeSSQ7Y0I0ZljtW_KncSXcJZ2lx_l423_KvgCydtkR3Ye_U6iTXdM4AXcp6yj38BMsoKPcTscAHmh7dMxMzpmOUOEqDZdSoQjSrcBdAjUvWKL5IA-rpUUYDPcyraeh7d2Bhk40cTeE7Ko0bBM8zqTJn_ozhuJ0Z15_vtM7-O165xJWxZDeyy0Fjbw8Be1KL1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1ZRylJMg7_UU9Qm7EBrCTn5gfI1muIGDC22DdpcCQe6_tQTaALguGDyLeg99yzE1CqxWct1lOmluqjjpg_F4xcYpH46B267SquP3AKWwXjC7I79O4x2NTJyzbR05Y3JctOn-UC4kB38oT5U90R_IcSSxiAxNddqoq-dIa9GLsOKB0l7hKdJXtntXXYYuW1ApyEO-qt7MuRGkgmGDeruq4ZPVrGc3OfLOAdVDjV8h_RkJgXMGgxL_9ayon7pUo60OVHx55AOMaR5Vh-FZuejiZrxr5JRkfsEB9vVo-Z6Q28XLb_x7dzTDHe3EhrbzkVQ5paaU1wjW1EpgOFZpWERLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DysKo1dN1xKy9pFWaFxXjsNEYqjUPVuaNKm3YsCMST-mbLkNUomAvArOJV4sXg5UX7lckk1dBGJ1d0DwinVOhFZh1CkGacTRX5j8gA_u4MEP8R2rbR62_MaCvGYWZ9PfxA--Uoq5_p-dXo6r44Qt2hNCGjr_UsXZAsjzuq9DqcaCmX0EIZFnW97-ktv5DlAY4nAp24gIjZ84n7SSTtZDLLvZ5LoYkNu-BldTjXQM3lnwWYAlRzP7B_neDpFpsLdJTc7i9vtaRcKe2mi14y6bZToDNSt1lMvgNT6l4Ju2kmAHEcKPzkU1BMa55hzp5XP1gJmEeli40JV0Rar1GlpqsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7Ss5mxylNvwOWhMtN5PZHOeJ0dTLxM4A2viJ1HJvNGNUD7uPXofpQ6prwg3co7-6vHrZJe82fRMONcMktUEmzcSaXD3D96lvHEypN52x0KPZ9CGYU-vF0DwLzJKdb8NRP59VjatBNGKyoI9N94LdxCYcNfzh1lkQQp0prcGACX_-ynCBfrb63ZXF0zUcz33OpeP3DZEXoPEAAm87jWg90-4Uc3rdxhwvYOqogaZJphEEXXPJzL7hlI-6-XnZ4kkM935C5bCZy5ImZcqc_tzBNNxuWhP3hiOAGj-nyi3p31HPpRJRlX7vlSa6aOWP6BR9ksSZb2CCmEzxF6QJcGICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0tuMZ684WcNUdHdlRpJBP82Im9bOb7XSkWVyj4lSUiweRrdYykYUhyJ_lL_F2VmT0IkpDpVtsflzrVeRGuuFZQ1GEsuiYF5H8SooYS9LE1qBrL4quI3oigXLXxyBqoNihsnaxfyOuE2jrXKipmH-Dh6qqUV8vyZsLgUWWOwCw5WTsplmSEejzxybpmLOnhXKD-6NISQi1CzM-nid5PEukXBqvaleaDrSPzfoJIvTyuWEJW_OsYq0jLKSIObwrdDC2HD49NMiGhmBxItNuiL3OLJQaxpTfJ8X4y2TEFQVMrnpswz6L6J5lJwq8vTvuA8dVgeKBKljDB9S3Ymk_105w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=AFZXR0ntwZ9zmh15fzrFz3X_bc0pC-0X0w0vax4BWeiK2hdRYkvDr76mnPg_oy2rWyxzZ8lZ3PR8r9Rp5MBfa8c2oV8O_G0HHpredSm30ndgaivodWkYJDwQ-LorllzwHGy3TDE61iRq8P9Pp2pv99Zu_7CrIjdGA_AiQizZMbeKbx6Gnvpnw5hW__UB_FXzjaqHb8F8V5syjll_P4MCah3bnLpryUe6hvdmzcsCyt1WO2_HyZGLizKDAEVlnmXsq-mv1IEy39mrbUX1pC7OqadzPjRi3IsUubzQFaNx6D6apd1-_RZLF2RF9o8om3JtsVpNYfbkZMatEMjVL_LPVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=AFZXR0ntwZ9zmh15fzrFz3X_bc0pC-0X0w0vax4BWeiK2hdRYkvDr76mnPg_oy2rWyxzZ8lZ3PR8r9Rp5MBfa8c2oV8O_G0HHpredSm30ndgaivodWkYJDwQ-LorllzwHGy3TDE61iRq8P9Pp2pv99Zu_7CrIjdGA_AiQizZMbeKbx6Gnvpnw5hW__UB_FXzjaqHb8F8V5syjll_P4MCah3bnLpryUe6hvdmzcsCyt1WO2_HyZGLizKDAEVlnmXsq-mv1IEy39mrbUX1pC7OqadzPjRi3IsUubzQFaNx6D6apd1-_RZLF2RF9o8om3JtsVpNYfbkZMatEMjVL_LPVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSdFlJj_bYrXsX42gGHQiFB3dm1Wd8OitTjn82mTHvOJuz5W2qANpEi0FVetV9gmXB772bkPNm4TR1QpW-OdMRKvb1ko9RxB5jnOX8muMjWkHZbLyqYrA0cvRGiOb0NWRpUO5w8g-Er67siFzr7apedIjiaBClLaLFQzDMNq7mHcTNZjb-OKBFERN2rys53koM7DxPH8F9TBl-zIe693VgNPQKoMOzYJkvxpFQVKIKDiGd1CAZPx9N82Qv-LA0IG3nhhbg0fDAzqzc3OU2B4BxqsvI3kA-aR2o1TG7RuD37aBu_YLfhXiU5hIAADc3-dlj-zo-cUh-YdIeKGUln3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=XqwfOGJhISZxfhG9L_mTnA8RF-oZBZka7rQd1ZFKdzcHOB4iuGYb3v3Q6lYsPsnMaNI7rtDk3JWjM8ZoYfdb3y0pxs7pyY0LT3FP1Z6WBbgNPzaAjAq_ti2Dnf16oKXyFs9zxxaQQ1aaRQI32rbMWYrSjDtAV5gSTCZF0Sb7jZVER4AR9AbpO4D7nzFoac3h_S-vhvJEDvbCxTNg6LdUkdSm1c09T1JFAUgfeTts8bG_KNIOETJxP9aqphrE8eOZuygI7lqw3LleEINJR2fluikiOo4FGbAsx1CsB9A8sYZ8bG_mmRKjQvaxmQJeBeEIQ7TEJpjVx7G3RLqBa464bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=XqwfOGJhISZxfhG9L_mTnA8RF-oZBZka7rQd1ZFKdzcHOB4iuGYb3v3Q6lYsPsnMaNI7rtDk3JWjM8ZoYfdb3y0pxs7pyY0LT3FP1Z6WBbgNPzaAjAq_ti2Dnf16oKXyFs9zxxaQQ1aaRQI32rbMWYrSjDtAV5gSTCZF0Sb7jZVER4AR9AbpO4D7nzFoac3h_S-vhvJEDvbCxTNg6LdUkdSm1c09T1JFAUgfeTts8bG_KNIOETJxP9aqphrE8eOZuygI7lqw3LleEINJR2fluikiOo4FGbAsx1CsB9A8sYZ8bG_mmRKjQvaxmQJeBeEIQ7TEJpjVx7G3RLqBa464bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwvp1q-9EA1SV7DPO2mhDOuw9zKPv009N5VnZx6HjDFHnSs__rJ7CEDE-a9xXHicKVEhYyW75Uj-iL3PXH_gOc14hv-sUASx93FKHhd-RNPrUOzopWtrtc8wL6dEahNWED8CCKJWysxxcCD6YYUVvg99ia1q-DjUtIZ7FmHtAoWYjAuaLHzt0-uBIaqB2McKYlnNHioT3QkSdqCWqBaMUggP9YAZBqJdCDYL0D9Pm8bfWzYr5lVgvUIgeIuiAvpKbHMHZG4TYFbwVfu0fib8DDAleRoJpj77j0oNzsnP7XxaN5e6-sHHWgM_Oz_AamqQJartyrtzKkcvppFCaeWmKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDVfcBl5FmEi6DFMvLMZzZaXkVGhoyIjXCksjAtOj7Nl3LjJFzvDeQlUJ-qzKxbk7QK1jFgtsJfVyBshaRmvW0sScMue1L5mFgv5MVF6BOBW6wU4_B8J-yTamzOtcyIrrMNKv4QC1GG1jMxUfPsee2y1OuNfPyxBBrV1L1kx058hRWRyLFe2e0z27Ud1QiHgI5M_wZUqTcGfYavlhZyT6SFZEcnwIzcDe4UGj_Jy9QyNDeJLvhJf7q3Y7Kan7z2CXYZqrV7BSGYF4TKrDJGmtFljpBQ7RQKFCZl8ZDl3QLpgkRx-kPqRgzKQe3M3YYia3gzvuNa6EQLftKfjPgQiFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=B0nwbfCOJTcc-C4I8NLd8ydBUJB3bqs-n-bSnqJzryu_hVFqw7n3NJNeDQXE9x1rabDsPgaWqII4zzAALt9Y4EWDsPOn7fIwWBG33oc5g8RyQbfPcGQTEYbA0bUPhJ9xZ7vOXIVMdLpyisZ4eTikgTlzdhuUIQYaTwjePWzqyysLQCraLUYE_OGdCtS9kbu__9mLVr3PxYxheCy13FD0E3pu5J1q9gq7GXR2LcJ7v1pF_CxxMp1ar8GbV24_bHGKgbZrem5wI-PS8ShAnqU2VlDl9gZZP-5Lw9UTtOca9ODcp3ocGcplweEHsM91VuKZzwy0zH8uZ4Hh7lWNgbrLvqqqvPRNZcGM-U7SAuW78FqHvNiWphKFavz0Z2CK70hFq3UL0jhuvWzTnbwElF5iyq1UzyIXH6dsGXkEgcjwCufe7NUDcmV56x9JFRaQyQL9cUVmi7vAlvXmniR0anLF_emx30TeVF-XK7YIV6IwufCez5IM32q7l_fPEFsCPCRodySNX8KAE79EqmuPgb7bmsyUTTqXiCvapKEcXB3jH0anAWESTXsbV596Fs0cIjUCxw_mxsHujYSr4F5nom7ieL-eWMWlDh-OOdEnh3xz404hv2XpTcbVDef70CEW-R8I4qi4EFasbjAhppzjaU0lZW_DwbAx0ObMMwtZ7eQlyQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=B0nwbfCOJTcc-C4I8NLd8ydBUJB3bqs-n-bSnqJzryu_hVFqw7n3NJNeDQXE9x1rabDsPgaWqII4zzAALt9Y4EWDsPOn7fIwWBG33oc5g8RyQbfPcGQTEYbA0bUPhJ9xZ7vOXIVMdLpyisZ4eTikgTlzdhuUIQYaTwjePWzqyysLQCraLUYE_OGdCtS9kbu__9mLVr3PxYxheCy13FD0E3pu5J1q9gq7GXR2LcJ7v1pF_CxxMp1ar8GbV24_bHGKgbZrem5wI-PS8ShAnqU2VlDl9gZZP-5Lw9UTtOca9ODcp3ocGcplweEHsM91VuKZzwy0zH8uZ4Hh7lWNgbrLvqqqvPRNZcGM-U7SAuW78FqHvNiWphKFavz0Z2CK70hFq3UL0jhuvWzTnbwElF5iyq1UzyIXH6dsGXkEgcjwCufe7NUDcmV56x9JFRaQyQL9cUVmi7vAlvXmniR0anLF_emx30TeVF-XK7YIV6IwufCez5IM32q7l_fPEFsCPCRodySNX8KAE79EqmuPgb7bmsyUTTqXiCvapKEcXB3jH0anAWESTXsbV596Fs0cIjUCxw_mxsHujYSr4F5nom7ieL-eWMWlDh-OOdEnh3xz404hv2XpTcbVDef70CEW-R8I4qi4EFasbjAhppzjaU0lZW_DwbAx0ObMMwtZ7eQlyQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDHkKbabEW4gPSOPPjYG4MdQZ6V7K5q_2Xda472TQJEvIea69-B1JG-IwQ0YGeL32dm7qgsi250aAj90QDBsUwNB-t20ixZ8LZuHWcX6lZzJ5nhYQYv9QcuFOSZbsiV9MWNvAz23D-DKFY5VZFRkJGGq-4e2GSO0N0vJYplaVn6Wb9dx7FUSNnlAZgqYeAru_kS2kc9T__5e_DoN47GYe3rIF_tCrodzco-cmiuiS8U4DaXWlLked8Xl-aq2LdWJ91Ovp3IUn2KAKSyiV9MIZ9ZuyVuxrMiwy0hozpv_QXz7DS9d1UZ-DmZqGV1gD4Ee-_5Z3zeeRGmTiKCI5PVA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giE8LP_RPQwL33ODHtOgHV3xhMk10IjOdG7MjyPvDEvbPX3Ho_YscEajrAbm03_lRl65VeNG3cLvOStgWjGeqMQRqgP7g4TXKSBVRfwG7zEy-ciKfouFYIcBB5lPhMajqV31Qcy_gQAiZs3OYcuz4xP8an5auuSGYAVr55vuouCZSaMy53O9K4WUv4_V9ctfSCNwdattYLxFbN_o44kL2uQwtvvCfhweXcNsXmnGnPPgzYCX-zUGnova14YiacamR-ChJgFCXc1Se2k7uXHWYvZMe1FcpBsQ58lEjlJ8zu11IKZGdN43pzwv7zSgIoByBNBTz7Dagopu6hanhqYm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsmxhELIVMKdhba8rpXT3CeL7uXe7Fk6Q9o1dSBhGNZ0Wlr5Haw_UefuO8jr7aCmNvW1yNQ0ZAtTfpnsarbiLB0_5yp3jNlvkAVfhl8cuge0Knsi9gFik2ZU2SJJzGgzM41uSu4pSGGnRB0WDgdr2bLvdbv9CDF0gBm-PUTOQC2V-vbwN3RESANZvobKWniWtK4xNXLt9kmpBCe0v-AX9nr8HhxISJiSENNmHFcZmLb0MiiU0scmCUNeDi5tO9-ma4t9iiY0etKUB5HY2cYVwdIOrLZWgCGYVH3icIYIBqbjtrADNH0mFZvtFWX2NIinCaBPHFoUFEQoEozfG6y0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=SNe9ig4FFlnVF9UwdRPb1PgSIZaOkQ8hXBPAcKHnClKrrwisV8GkPXL4ADI3A4vbdZFTxzm56ka1wx7w3XsUGVw4DDJbRsq2Gu_jplIZ2HKJn-GcloflFRc2YzyjZeDJihTDdHVdHMKX_LTZG7SEjLYf6uE5HrhkoPKXQktEe_NzcHZC3JQujKEBOjYSF1NZTeMjqFiJTjoAnRvRU0lJn-HNf6LSX6ltgGmGk94JVzt6XFp8udQKn1RJswliGHsMeGdQf2vvY15KcnqUJ03SFNYBMtcb8-8UST9wrY12fNHaSh0ChAB8UbBiUcGhQpHSIYslQnmgG0trqrWh8QbD-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=SNe9ig4FFlnVF9UwdRPb1PgSIZaOkQ8hXBPAcKHnClKrrwisV8GkPXL4ADI3A4vbdZFTxzm56ka1wx7w3XsUGVw4DDJbRsq2Gu_jplIZ2HKJn-GcloflFRc2YzyjZeDJihTDdHVdHMKX_LTZG7SEjLYf6uE5HrhkoPKXQktEe_NzcHZC3JQujKEBOjYSF1NZTeMjqFiJTjoAnRvRU0lJn-HNf6LSX6ltgGmGk94JVzt6XFp8udQKn1RJswliGHsMeGdQf2vvY15KcnqUJ03SFNYBMtcb8-8UST9wrY12fNHaSh0ChAB8UbBiUcGhQpHSIYslQnmgG0trqrWh8QbD-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiXvzZz8foIy2_mXbzb4n0S8A_QUuCOhWfGNNux78vbaAe8Gk2665sxDOI-9liVIbfdQsW7IepPG1eQEOverT5Ec_DQ56u3kyuN8yr9yOLIiZ_rX3e4QHdOKH6EuQ20G9lU2ZFxW7P02kZvLdn3Pms8r85KP0GDsMU8DrnmwurX2bAjlFlVMR2KnrhmxKoyZwE7NZen4VGohTyCrwyzypQDFfhe9QdH_ywnSV7YbFclsXHMQB3w66t1GWJmjeFEDjQeYZoeSfGGJrQxQyGHRT34rAYtM_pNtVWpQiKV76bC3MqFzjamQ7U9deA7UTi63_kGxEEky72jsI_RxZQF6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjbEYFmJU04PrmhYFf8f4moZUAERBtFwPZOnIFmjhjQmkHqXdWTctMQgfpBztlahjrLb6COcB7y1_zVaZkFk3XdNL5h_bQ6mFEqPKXL0l9yPHd3Q2J97-TYt9jGsV9KGnToNpgFdTsghnJ34D2Ou0WvAPk0iB3MDbigMB2xNpOD8rgFeD43mkBrwWaACC4bAp4zuWEknPM2JYIlpfOe8Tza9M95x4b9lMGchAuPHcHT4KW0GTPD6qik3l0gglg9trXMih8_Qo2kiZS2WfnJGvldmz6Abe-tmBHQ9o2J2Awv1UHDiRY6HSc7m76xQeDRiEviZzD47BVqvhkoAUFjPEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaXA3IdgzDvdVj5roI3VsYHBRgyXkiOX5lTAw_atIOniNs-0QNve3PEd4TubqZtoeFcDGbcKKdKnPoRXDfA4Y1Er39EqHTfywTJ4JvdsJ6TgfFG1UBgiwT7jGZuvpVKQ3Pa-nQHYF1k3pX6YrBuqlPX89qEvAKm0jHBePLOBFZfdYkEaykZ-B3TRBou7sYOcOyXlWpPAzVCKMTrQAB1HAdR1AWs5ORXiyHHGIdtz3bnIzv_OxzPhJJcUB7EmhTegX6PzTzL5J12IEpS1o1JRfJhp5399PUXkusIpvxDXPxKMh2jOFgO3NcpQ-WaA1xCVUB9p4Qbutjo11q_sVYGDRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzqdeLreV12atnPwJt-NlPavAAnl060rAARINScW-QAfMusuv6UaEeiOY60Rs6V208oyXI3eY8kl3b44Cab8v-7ev9AQi7JwxpsvCw8EGtO0L79U1SdLpdyk-IEDkywbWSzI1Ma2nlyWdsGQP2xxfktATdFjz9EAVJxTCjrB7-gma2UZZU3lRRMmCKyW6bXirJAgtvMs9_UZlGQ4F9nbKY7OhKpfF6j7bbrY94qK9qRvswZIC1p6HkqOcXJJUIkL2nmWXEoIKR4C8p53U8Gpv2elhU5xSy7Nh8LbBA5Orh27Se9hqrqmyNtwkWVpRXR5vqVxXce4aZ6lV4G2vnBsIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS6Wtuz6O_jf__lHORodL66zGXarCpwruDf9h9xVH4AOiQ7e7f9o_uYHzaHLEOZ1BnIhE-6q_3-9fHCjjHJeeE7Fs9y0rSEWunYf7Fs3dtrNDzrJ76rPMPmVAia24j5i0c6RpKrrxk4_mMlPClKzzEN4nhWOqTb0_yYCDQBg7M3q2JtZZ9yQGfyNJnhAHNUEEpGPrKg2XWU9hAwcatE-7_xQZQCYWWKQqlRK0ZQzQ-i4j08uOyunVp52-76Zxq77jmCdUTw7kk4TIhYA4LHSRyxXWOdHGAXwNSVHTmkthz-69PNXcjorBqo4_Ur9Xpqe-u2OTgAeNFcYa0lPX48cFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cea96KySHWTerVDYdIGAxK_MErvG4I2ZkECtdITz0mETftVZW9flneA_5H-gQ9FlLqhcmVa_KNL-dC8mflKGEcAhvF-v94XgmiaAhLp312W0tq_PZegBrlPCVVwX2Hz05_uYdPwny_0HeJ21LRY0A7bftE12k4vqxTOPaxG03EZ1cXu7TmN_S8h8nB0o5U_1EHdguFaz1vSoR1Vck_lperhcMmKNkrQrXT5ioDacNlTxF9oR5nZXMKkSDo6LfvNS7CwI6xjuIap0V_BReoSN6q53h3mqM20icGN0RcAtNXDF9PVIEyoEk374RG0UDpVzayX_qH1Rgse8xUNz_ro8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2KSS0_mKcyp871LhU9v2o5pbMdX2rkeQ1f68bpRRB49XfELJAqQ4ptbKhx5_Wcb0mmS6bDNXL_6xBt5kjtZZzOHZm_2OWv3CR2u94S-w8UnOfIXbrqmTuNMb8CpYjOthbhIqLuh9H6rHZrWHERWfPet-YmnbeRNpvUiFTL8lXd3RRpO4KXIqwW-a7dFuy4sapcQ6Z-WXV2mGzXCTqJpOn_bVWMbwkmQujsV8kXI7uiPguwtli2QJ2YFpChdfrgejdxXHGSdySx7-Eu47Rhd48XqP2Cs1D_m2n_pdAr3hsxNnadKBWeVvg9e0P4wdueOAAVyl3-3a9I8URu41vC1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLYgm3Wjf3tQWfB_Jz1CJVF8hXNwMpGYpC3QVIFTwA3VVgYEvcwNDaEjouuIJZV3V8Bnlj-B8aejC3E80iNCulQqAStYkxSs3dOCls670bD8HiqxyEeDmyB-jDjdDoD-X_4K431WgSxADX7PWBpyLtoMQXHp5nRTz1n6zZNfEd-f3u8yPNUMmuVb-C6gF-Gqj_sY-NRXFglYTmthDUo3K0xu3vP5KtGPJg6HyH5HSZff_vCaVkq07Ps7PCLKaNkK2VJiJyD5FfC3DvF1vArY-Zgnb6OsYyCnja63FvxEbR-a53idKRhQ-El4IoDiR1lyl1cxtS3xjqtH0c_uUDYbQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrXYcLvZ7UbKF8nhave_we9oJD4VTAOY4gbu-fiNr8z1SPlID-w6NhMV_TZixTr-7jQEN4-f4Pk24vvjn2_07neLOxA3g9_28pMIccBvfajUIn_SydSGjSElZiwY2NxSxUX3W72piAxD_6tG7QDNKfYF0QoiWCL2HMZESnmAnARLcKfjRbEO5Gd45ZdTsHQPx5Ivy2lJbNPPtS9WbN4GCdqcnws-cR0UbUeNI8ufm8ccp99Svcy2qU1z0PeF3YGlo9RYJAdUIeBOPErPf4w1vr_9AUsWwrd2Q3GqUr3jEJk8uSTbpc0MZEFj-qnxcjvf59OUqw4pqMFmGP8R_-iSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTMqWztHoS-UKrWV3SbZEkWuDXl9E9Zl1mJMXh-la82sj6LUIbpjFRwgWdRXV4IpFC4byHjjw7bCiXpEvH5m18FrX4OgPnmXqsA0jT7qtYaNM7sKzUIWiCIIG4xOS7Yzcon1aNXk6Tme1VJ0ID82Psfa_GJF4FWau3fQQtx5lDVBoth1yt2JaFKwsxrTtZ3_gGzGW8QJo_RdLnexKzZ7TkS1SoeHSS-GSfeQAs4PJRs4-wbVreVTjTCK3UbJgvsNMAFU7Siu65gkFxK9ZIaiBb_iifjzERjRoha_OMeWVlERXzTyqtXW-HtchSSmYFta6Owe6TAT3SSsVXtUS-cOZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=a9SFut0tMkd8hy4daCch-vlINEcCH4IUEW6FweDVWtFf2jli-hZ6aqL8E-ZphlP4CwBflcrT2UH8n4wkP2pK9L9Q6YgJMe-ePmCHp_bJ5OoQdtZAMybMgJlK9JskehV5EfJ71jV_-AUVZu_lMH888fZAs1AhK92s5khWT3yYHB95Ldd_WloPuHEAf_6a-PtIv_Zj__iXMw7Ksh7ZeuFTC5Vo221Wf7R-ahPb0MgXw2bNsYExkZbg02LGIas5XHTyyWyxI3UqVre6tT6k1NxsEU2syXbsGe4HpIzzV2ZXCNRCY385L1y8E93DPewrMtdbsW66ZJp4wrxy9LyRppLO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=a9SFut0tMkd8hy4daCch-vlINEcCH4IUEW6FweDVWtFf2jli-hZ6aqL8E-ZphlP4CwBflcrT2UH8n4wkP2pK9L9Q6YgJMe-ePmCHp_bJ5OoQdtZAMybMgJlK9JskehV5EfJ71jV_-AUVZu_lMH888fZAs1AhK92s5khWT3yYHB95Ldd_WloPuHEAf_6a-PtIv_Zj__iXMw7Ksh7ZeuFTC5Vo221Wf7R-ahPb0MgXw2bNsYExkZbg02LGIas5XHTyyWyxI3UqVre6tT6k1NxsEU2syXbsGe4HpIzzV2ZXCNRCY385L1y8E93DPewrMtdbsW66ZJp4wrxy9LyRppLO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=T7jpk4ABaRsgHsgEir0aM4bUxWGLNlEwkdYsD9SeNPK-APKdUi9C4XrG5MCUscEbzuReHLCAW2dIx-yaiTwsdCFhfq1rk8do-CKWZbyeYsasxHm7fRCos35YsyS9yCcUEzZE5Xj2oNRK-G2CMxOpSgXKBgML2ORd1bNQKIpA65hmZW58jwu9r0ozjYsL8jp0Xh_NsP5Kwr0VvQn7GAk-ami0pwq1-yEAPJpuzsxtCK8DzrICe3mJBk53XNQr1cRl1lZjH996aWtaUq-q75dfMCOImFQVCU27muzGFkdzP8uvBm8QyA4I_5tb7KxsQxQR73jc3TOdWCpfsaj3TkuJvYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=T7jpk4ABaRsgHsgEir0aM4bUxWGLNlEwkdYsD9SeNPK-APKdUi9C4XrG5MCUscEbzuReHLCAW2dIx-yaiTwsdCFhfq1rk8do-CKWZbyeYsasxHm7fRCos35YsyS9yCcUEzZE5Xj2oNRK-G2CMxOpSgXKBgML2ORd1bNQKIpA65hmZW58jwu9r0ozjYsL8jp0Xh_NsP5Kwr0VvQn7GAk-ami0pwq1-yEAPJpuzsxtCK8DzrICe3mJBk53XNQr1cRl1lZjH996aWtaUq-q75dfMCOImFQVCU27muzGFkdzP8uvBm8QyA4I_5tb7KxsQxQR73jc3TOdWCpfsaj3TkuJvYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRW_uMu_7RZ5Rn5v9PBMNJc-API3vXBmfEIiLFxJ5l4JWul-riNRMp5c2pGfLqZ3lZySmgy26ybs68pg2qynUVGFbD_EPFS5W3_CU6SW1BWtXDY6YwXdEHT8u_Pl4K8E09gnCNRESk2lyQlBaNufNJobFETGfiyZGLMMehAnkF2_SEyjSDHpj8RQDBSt4MqvkmCrlQ7lmhFus_SVV4w4hAIGVO-vDyYvk3E9jLcR7T9IY8U78vEsyvwkdF8G0ybb_pw7zNiv4LWVXOzZo1SSk7w-C3QFeQRIs0MYQuPaNYqC7UyBz9YPt7nOQ2Uz9pKGM8_n3Q4_GMvDVO3TbHPlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HtabwdFRfIDs8eUONzz1q38wO5HpLVok2FAjADtYWi4oVjR3RFfzmBYaBRRmmNThFvErbHLEdkJNyLyy0i4zCA3x-hgUiia4Ry0seP78hwgXx9rK2YAzdcIA8T1bBHKAhZCzb4VPwDW9CcU66_ScSjQhG8sjY-xeNiL_EIKKX_XbYRCbL4SLuFr9HNcqardV6JS3gC4AiBPXvQVINJiDkwQIYVrJPlUWG-gYCV92G2Mp4iQGnIqoOQEbRehnF6QnAd4i9PsBgGIxL-rXVfBv2R3eNNrZEypRPzXniZGUr0d84JytCeB6eqMK4xgxJakhemWLhVpQ7pT90RcD1AjEKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfXGttjjM8KcY2gxJImr2TxrDKXXTbxC0r311EIOm_rKFyO6PN-uVkySnLLIs1R8bSaal6LeZ3eZg1tho0hhkIqVvJz9b3vdytFu2EQFhx6Ls6zy4w9xk5QuKYVU0VeTeV-prwn2WEzbV3oQYhGqSUfHdPZL989yFiDjqVD4v4_BGbnWurm_9yKdI4n0vcZkgQKQZGoFHiNQ6w4wS7i-L7Xl1JtPAl65CodqzocmUTObYbChM23YI95B4rklWQsQHsv30HLKPyNjiizgucxyOhtaMDCiIWa4AtHDSTrBKHC9INCqFDyucQmQ52SC6ZbCGIZhr4Io98rzQgMMe0whXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lZMhTELjqyp7P3OYMcYUs2tq1Q5AShMRwGe9Xw8FnPx_YEUlZtx5nG1Rdjb5bDYU_YbMYvlaphjOP08kN618tHo5UOMHZKJnv4Whe637Y0UiXLJieB2MKOR_rHqb2Oq-OgIdhhqISa_0f3MtdBacM1ovE6lH7dR5KyVvBKy9s1g8leikeIl6srUZJVJpsRQpNR0pxFtSK1TCM5Sc3-FJGEIZdZVZNDbbxlKILAMoxOsYWoNkaNEgKOQxdWlLS8zf3mixODxUXTmxuSCJOWVASOFSvSiROAx0nEFZ2vNOCqPh_sZPihqIDxh7eh6nbr91tao2zZyFLCcoiIFDoM__Rfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lZMhTELjqyp7P3OYMcYUs2tq1Q5AShMRwGe9Xw8FnPx_YEUlZtx5nG1Rdjb5bDYU_YbMYvlaphjOP08kN618tHo5UOMHZKJnv4Whe637Y0UiXLJieB2MKOR_rHqb2Oq-OgIdhhqISa_0f3MtdBacM1ovE6lH7dR5KyVvBKy9s1g8leikeIl6srUZJVJpsRQpNR0pxFtSK1TCM5Sc3-FJGEIZdZVZNDbbxlKILAMoxOsYWoNkaNEgKOQxdWlLS8zf3mixODxUXTmxuSCJOWVASOFSvSiROAx0nEFZ2vNOCqPh_sZPihqIDxh7eh6nbr91tao2zZyFLCcoiIFDoM__Rfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=fPmLZnI5yBtwa08QqHrFe3pqRZ1PUhcLkzdVuNl05TOuAP-E3PLdKXBnyfkvEg-kRSZwTcwytofvfAvfEEW8gQizbqV_f-EhMxTwLx3JqEtma47khEQUQvKIfHbRhzFUfFd79xXwWJgf2VkMH1fBevTD5i_7XXglM7J1x49c1FnSh6fT7KrZJ8LALVA2kxjXGdzV0uSgb0oSy1dbwU3as7jXiAmNVgjJjU8yTNxmpgpTEvtatOrJabgnkJaXidRuXeer9z-4ZXVY2MqIdlfiVRgYmkmiflh7WWJJ27gUoNYSjcvF4aovMvm9tP3Ewafck9396HghfzhP4WC3CeTrckwtrlIC6tpHeWu-oKU5_Qy6ITbnlgWQ5GsQ64ZZNasr12xbkfGxxQWbs5PYhhK0j61tJdKDqbnt63evdENBn7snYelZ08r1MYPJihCF7rN6S9CnhqHuunlmj1LbjYNSvUkTUmuDvHwqBgnpbtp4WPY2pWjSmcOikBuuIgNmG8T_r7cxicC7PZrSp5IC4hd85-xqEqYMBJufVbylAZDnsO48otxmIvQgJ3m7tp1NSFBIDtKbx0F-COvsAkN5f10YHlIRWiWXFNkMKX26tWxxUIIzeNt5OLCjWBt3rNE0bqgGhijlHaw-NfYSE9OtvvX74catxzlyNsnrGgise2l-C3o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=fPmLZnI5yBtwa08QqHrFe3pqRZ1PUhcLkzdVuNl05TOuAP-E3PLdKXBnyfkvEg-kRSZwTcwytofvfAvfEEW8gQizbqV_f-EhMxTwLx3JqEtma47khEQUQvKIfHbRhzFUfFd79xXwWJgf2VkMH1fBevTD5i_7XXglM7J1x49c1FnSh6fT7KrZJ8LALVA2kxjXGdzV0uSgb0oSy1dbwU3as7jXiAmNVgjJjU8yTNxmpgpTEvtatOrJabgnkJaXidRuXeer9z-4ZXVY2MqIdlfiVRgYmkmiflh7WWJJ27gUoNYSjcvF4aovMvm9tP3Ewafck9396HghfzhP4WC3CeTrckwtrlIC6tpHeWu-oKU5_Qy6ITbnlgWQ5GsQ64ZZNasr12xbkfGxxQWbs5PYhhK0j61tJdKDqbnt63evdENBn7snYelZ08r1MYPJihCF7rN6S9CnhqHuunlmj1LbjYNSvUkTUmuDvHwqBgnpbtp4WPY2pWjSmcOikBuuIgNmG8T_r7cxicC7PZrSp5IC4hd85-xqEqYMBJufVbylAZDnsO48otxmIvQgJ3m7tp1NSFBIDtKbx0F-COvsAkN5f10YHlIRWiWXFNkMKX26tWxxUIIzeNt5OLCjWBt3rNE0bqgGhijlHaw-NfYSE9OtvvX74catxzlyNsnrGgise2l-C3o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H28pDlfQFl21xKJhaIf7aNKbHZO3t89WmYfThU5erUg8XQtKnUiQGqmvKf9HSXXIaeq2e-yyDdvRwhUzR9tpCNoLebzxOuCpJnobXDYUHcf2qFQCDsaALIXmDZG6ZJaHx7crbMx9a69EPam63VWAkNxcVX1C7EjnaY8qQtgsf4n3MY4BdUuDSEmdcAUJgwLn2tslijJhZPoLI4zpUjUjC6FDiFnXfGONv210pRdYBDdqgqrrdGIfqBSurvq7BbEuOuOfzDvs7GnkaGHooL94i6h1NgSfZZM5aJvavrspcE8i7rov0tOme-Nm9fNE__eocD6Ljhe9RG5322rG-_YBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
