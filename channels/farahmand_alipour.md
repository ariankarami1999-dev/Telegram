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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 00:04:59</div>
<hr>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2_NxrDf3lqgi08vo8y-vLhn240A_uzfeiQYrm-_DqPBGXpK1Gf-smStOIYIsNGZhKuHwC0d7SPvqqIPuVtXbMlfDdNEVYrEKgpmvdJKw1jAs997HPCWzBwlYLblGOzYkSIiHevncRnVvP0sLaiHpuouyAAhC7quzcwB3MrcJuQNbJZCMpUkd0Nyv1I9wBuOnUzPBnfJVCpFIB_tz9LgUu1fos7ImgwiqCLH30MOkbe7zg6iCNlcT4IRqgZdyxzj9K-3itP1fg550uH-Ucq9r1nWZg61nt77YVNw66phZ_fWlWYpkmrCPp-kieaFtXxoSI8kKgGGqXuU2k4tKXGZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVU-nDZkvVMadV7tl3LNLTuxH72pYU5CaNIsDpSVAfsYyWebLiP8fhqd727ZvWTwz2u-zDA4xF0zWoyg2IFWTcY0B4qovADQl-SCOxzhUPXuYiEZuEjk3eJYAsD9PDTpG3M5qKyjXFI9bXNVt4ANlpq7x-xWP6MmFRa6H57xCSejt71lZd-ngv7jIdaGFFXHrElikrNWv_-WkQRgIAECXSmEDWz7IhnnMYdfLXb1KMNczAgpHEXsWY4zZqlta8I1QjB249pzOjAAINpWiH_NpqYQobDKJaIWptEaxlPOURJOARy3H8YMisIQSTSeta5rg2zo38F7EHphnLi0wWWvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=aOWdx-kjqpNlLf_hjd1eb5E2Sk6qQqxN5yqmFeN-NyKk7KCPsSEQvt-PKFPbNUvN_toki5Uc4P1XZPv9YpHMVCqyVZ24I_h8Kp-VIrWOrx-A_feVKJ8tyGog3A-WApFMHrrRqPDGkUFqNOJcV_nGheECSiOkpGz3jHbrC-PTsoyAWkRx2BcQgW-iHqeLTBeTwzKjvDrqW5Rhzcu3eEbbfECTLzW60kDOE-1eTewufalRdFXDLCGNLlYtzBsr2N5FXM0bMnPyiY8vC1KqQCwaN6gO-mOn4OHkAFnfm_yUFfCfVvAoEBTh7II_LViYFNNJKi2QqNe8XM3AD2fcE62NYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=aOWdx-kjqpNlLf_hjd1eb5E2Sk6qQqxN5yqmFeN-NyKk7KCPsSEQvt-PKFPbNUvN_toki5Uc4P1XZPv9YpHMVCqyVZ24I_h8Kp-VIrWOrx-A_feVKJ8tyGog3A-WApFMHrrRqPDGkUFqNOJcV_nGheECSiOkpGz3jHbrC-PTsoyAWkRx2BcQgW-iHqeLTBeTwzKjvDrqW5Rhzcu3eEbbfECTLzW60kDOE-1eTewufalRdFXDLCGNLlYtzBsr2N5FXM0bMnPyiY8vC1KqQCwaN6gO-mOn4OHkAFnfm_yUFfCfVvAoEBTh7II_LViYFNNJKi2QqNe8XM3AD2fcE62NYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjIPXzCbYPwjFi9oe00DJVtesjM8S4PFKJLr3g4b251jI1q8a0Wwxy2JolqH3umtm-vobb_2Bn7_mBadHvUIFAk_hRvVRbBFRHUxg5e7Hv_XQrRL28sh31xCgjk6mbY0lR1NTfvNN8KmTFUUemnVXkjXf5ns3POtZsFpxfuVQF2uLSf10V023zCc90QXuFmmoqTi5pw4vIIIoRTG6iEm61XoPIY6tN-s4kMnodT4HA7w6s21416OCh30JnFd4RtDGHyPauEQD4qLTjRgIoKXdhTNz9DgC-o7Lr20m0a8-dHnChi_24IrBDleutOkXo3Eg_w3iQEfgrKi4Jc4ab7Y2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-cfYJQNLiQhORzcP8Yw_97m9JovkSFq8nUOZxJpTfGXIMupYO6eNxllsMiVEPfWEaKp7AwRPa6O23oe71cTJkd1DmuMjcGvCUup3qc0skYAWlaIgz9RheD7BvR832qfbgBNp4Pp6f_vkBn0yJXBvW0AXykzxmZt-erxBEx04mF88lip38kqomYJXPPTjTLTBOCvWR6xE5MNiKDDaxNscdxf3imM2gO4D_Ujm0oYHCAyQLYladGlSolw22O98SnjFgFUHJl6MFVZactJ1jtVWJt-KH7cxdViRxenvlpVCbe_l4Ibbc3fx_r2enx1VOJP7U26x2oLbXzoKwHhX1dnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1f61vL42ySxQn5kYMCloRcoaUAkfAtXCjC_lNTA0zTKTDWkOQy_ZWZfgmhenzwH7EdwIPX3IUij3OHPCgMi2KDQIiJ33IS5-eZECTj7rLA8Xc4TO8Eke7v2MO2dXSL7Wz-S-Uhvl9BAsodrP8dylVH33cX8ktvdGZmshCvOCD1J7X04Dl98qBTAA3sHfUTTIPB7YT8PRVflBfyS3LHm5ihIH_S14XgvhZcEpTbJUbBUviyq8e_Lk3AaSCkCSSrvGiRylZ8fKHkdB14aHaJGh1TvjV_oyJsZEcmpe_kVlcAOwz6Dv59yJsV0qQUAH-YXt7R1w6XROe7UhLx9z2nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_kWza-Ol5frBCLnmexrS8u2AGjYT1ApPyNVoG9lA7ADKY8GXUqknQoT5TwQOHsXDVVVZR_9EcdpFYnYBtCyg4LFBNWNyyR9utQLCD1so_xACpttTuWNYYtvQiHkoT_juGVOg-wQ4YMu8dZ10-cYJ29au0z9POgXSGSDbP5Z4MUdPzDuy_Q0smSjBqsXrdV1rpjViaKFFJMKYlfsakYct-xMYOfZC_6AEsN9texy1-zCWxLDyzO6yaIzIEm2xEaB59HKDVcAEjomeM0acaBljhotP-2A4_x5l91AX6BbrO7RWr9naJ0X3RfVrmoKke3kKi3AkcKEB2jmVT8Ko7VZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=hfRSnnbkj_HzC68nSfnbs963_4hK2ggiFjJJG75xUFcdfIIMWpK-U2_vyiYPKrVzLr2XAiYoTpeUWPIdK2pqoVyhcSu2wYUvaEB7zxhueKhQ2b1prH1NCD0-3u_Nc6jNnA5o1qpqwuWh_sZ-b-Gr7Lfsie8zFypXe58IAoWvKqTtMxuQzqnlLPB-ycnF6L4gGT01yaptfGoDCIrvnXJdNNA-oJ6X1BzQ59hWpr20w3Jmo_MeDL2Jeji6H7A6TedWZ1p5EpKWnZgN_qqJDsZJ9r05qbCq146AUDLusBHTCcFz40WTNZs45bPa_3ZN6tKDFl1zYqToImBJH9XqsHzMXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=hfRSnnbkj_HzC68nSfnbs963_4hK2ggiFjJJG75xUFcdfIIMWpK-U2_vyiYPKrVzLr2XAiYoTpeUWPIdK2pqoVyhcSu2wYUvaEB7zxhueKhQ2b1prH1NCD0-3u_Nc6jNnA5o1qpqwuWh_sZ-b-Gr7Lfsie8zFypXe58IAoWvKqTtMxuQzqnlLPB-ycnF6L4gGT01yaptfGoDCIrvnXJdNNA-oJ6X1BzQ59hWpr20w3Jmo_MeDL2Jeji6H7A6TedWZ1p5EpKWnZgN_qqJDsZJ9r05qbCq146AUDLusBHTCcFz40WTNZs45bPa_3ZN6tKDFl1zYqToImBJH9XqsHzMXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1yROZXme7Jz6MtSMEqF4mPW8kOyrF5aUfl_HVrjGe-aAeWHwevXJg1d9SVFSNX68uFGRZtUi4jZ4gJLsQlk4pOXZvAto_t9O_1OUmAzvNQdAjQ2eqWCLpr1xch1XfxphnfNW51M6juJNm3k-ZOZg3xEtd6pkR9K-ez70RygzFa9cEH52a8j0IE4a8aDjO62-PACGl2FC2OH6KL8i3RuhGPAElT_AiD084WxsO3eUP4ynlXu0CBcn-Z73S9vO0bE33MKxK_BR33f6rz952x5EuQ3quYAoOJ9ipRCTeSplkDSSmmKYelZWbaOSU2YJngrqFiFN0E16Q-vdQvVkn3dmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=lVNsbB4Ed_1IEMGYjNDU6q8Of8cpjHQRK8sB337M0zoeS5tQCBPlNKIi7tWeDcE2K91ZpXGbr-6jy0AE9oeSbP8AbkN8goWre0JAFFD9z6bjNJAZFi--oY9ouoO92ZsqWf7H4s0dZM6gUW-8OyYggJZLpXgAUrOhOhDmDMFSIEP9_JX7YA9UW2DyZSK-efphJugH6XCO5gTk4M6dixFijZAKPIabxYnm2deO5rdE_EoX5zPPCiAioTaholSosszz_hj_ew8bA18aTDqrELGC8R_d2jzzwiJoYqZBgglbVOabzeWqmDEMzu36Kjald1ZWlkaphWpevsTtjS91QE_qxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=lVNsbB4Ed_1IEMGYjNDU6q8Of8cpjHQRK8sB337M0zoeS5tQCBPlNKIi7tWeDcE2K91ZpXGbr-6jy0AE9oeSbP8AbkN8goWre0JAFFD9z6bjNJAZFi--oY9ouoO92ZsqWf7H4s0dZM6gUW-8OyYggJZLpXgAUrOhOhDmDMFSIEP9_JX7YA9UW2DyZSK-efphJugH6XCO5gTk4M6dixFijZAKPIabxYnm2deO5rdE_EoX5zPPCiAioTaholSosszz_hj_ew8bA18aTDqrELGC8R_d2jzzwiJoYqZBgglbVOabzeWqmDEMzu36Kjald1ZWlkaphWpevsTtjS91QE_qxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdHmmXXc8trK4MhLiSE1bUtB2v6rcX7Salq4kn_F1IusKTO72C4-YaI8YlXNh1vkLMQMOxucCwz6GU5llci4M1SRzmlafcaiOKxGioWAd8thNcibg50z1-ZHMvnVE_aMjfEiln4vRb-OS2MinECSfoXoIUo5n_kYQTbuaogn631BzbpuWoMBE6yVTUC4Fzyux4NVJNg_2fAoUXEDT6c4_w-BP1w0HQMy2Rdg5SNjtkNbxhRLjYJlbFLzolJvYgux_NIMsuGcIP6XL8hQKoWlcK6MeYp59d7mcj8e2DrZAhnkm7e9OOrUJEIR54KCDt6uvPyYT0MLKyf2JDNXjQvGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-fadso-ziuEO0QUUQtof1oEqVhB3Yumjn5Ut1_ZCQghERLw3OE3oOvjqNRoJAxHr976Hj9gfnbra71EwzIIjG-vDspimbdqF-kLhDrGX7is3se9Jx8evGm3E33t5QGqcG90cEdCM6J5y9gXgKGogDxrIEJtpGyD7pucgJ-Iskm2_xhhBVcnAuDHkqcjqRcdSwxLaEpuv3dE2HW3QgfuFgbWUC8F_wCm-OwqSL5SJRUrJCYawKIdCDKBd86XFPfM9qo3OR-ZP11v30FRCPpm5fmiWva98xR36QXrX__jI3qefGFP3faWaNGuHnMnOikRrJH60hcfIz9Vzyu4NPvo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh2IkRxGq-6-ePdNopCx9gJoqznIHYG-NCBtM75dT4d5RfDGkwdOJPtujB5oAcHN1Co5d1kemYAqd57w0oWlRRm90GBI39cHEF6De1gpt-MUc-Cr8LQlRnsularkYU1_ggigPOPsDWGtLqT5hBmmsCDgmhARfd9CAd3BfYLnAUF245d2UhUiT41V16gE7T-tioKPGGDm8NsBY1RBPLRFVVUG9PHCihsiqEV757SuzB1CWZgMBUkv2HOVvWhaEpkC9-Nca1Lcz_ZEiSpmB5i9O4DAmej5Il8OfYy7ikP1d0zb945PE3MtVEnIoyM610kXFK0LtsIt9_cI9yzH_NX9vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtKUGlMzf3zS-zZS4KNzyXi3_v0ZyOD4Ff_srwvTZsGXrA6eaoQ5JjWSIEEvwcQ9jzFGzNfImYBgqy8vyfliay7ms2kUAmW3nj5HcmEAtO2zqr1WbAy4pfqjsyS__-U_d3hBrexhUh-L6_j6_j1mmeo71IYV0ibEkVc_uyen0L5WBy8P6Olh-nWNc60e-1XfjucYtJMeOGE_MAU8DXhJ9bLNRCdwp4rEBuiLJOkMp4D3dOxKf5AvM_BJapcTgDvNKc9fL7S7OOhrLGG4Di3D7v6A9l3GUGgtUtPs0SWd4Rdd4yl4D_rHMUTcOoU70UdUZTdMDwTl_Pl1gvYrRW9gqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3pQBZh_IzXkiwLrEioWwiGLkxwah_KsoSPmgrYAdlljy3_OzsGX5y8h6MOSI9Qe0QRcfHIhSp-B4Nz6JTfr_ZdnpGc7vSVdhk9h6DV_4ejYC8xfKHm8XbwtbeqLaPILsCEDJKNMYSTetUWsXD5WxlIDDv28fhsl2SvI7uEItEH5jD8R_ElgYv_vj0KYjtl_l3dXaLrLy1_90UPWL-JyXT2uXy-VeA7wn0hpNjA_4GIyqESQ5ZpFz7mpnueGrAqBDI5ETDSRr-fPEqd5SHpkC9kP5aA3H9Iji0M-PPOBFF1SpFWEhBy_bkOaJE9Y4N4YoYTbGqBbGFxI5oZtZ7NNexkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3pQBZh_IzXkiwLrEioWwiGLkxwah_KsoSPmgrYAdlljy3_OzsGX5y8h6MOSI9Qe0QRcfHIhSp-B4Nz6JTfr_ZdnpGc7vSVdhk9h6DV_4ejYC8xfKHm8XbwtbeqLaPILsCEDJKNMYSTetUWsXD5WxlIDDv28fhsl2SvI7uEItEH5jD8R_ElgYv_vj0KYjtl_l3dXaLrLy1_90UPWL-JyXT2uXy-VeA7wn0hpNjA_4GIyqESQ5ZpFz7mpnueGrAqBDI5ETDSRr-fPEqd5SHpkC9kP5aA3H9Iji0M-PPOBFF1SpFWEhBy_bkOaJE9Y4N4YoYTbGqBbGFxI5oZtZ7NNexkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=XGW6RW4asufE6yUbGonN33n4lgqzCsRVSNG3-bleo6CwtTMpo7JsFrAEF-IeKbXf2DMnx4tvjepJqHvfgWnZVDzaTXo_GGoCDp9IKxjCxfsJ02xst5eJwj4q4Clbsd1LR8ZTQm_oPESxsrWw1r2YyRs1Olvn0tKzrdtI57gfbFm7jz-8ZODl04aIB9ZxWAxLCQN6HzKXF9gOw5EY6Lu2fAIPWvjUAcFunFGI-Q5CTW3BIqyEcD8zHbZoARx-9hFxwRT1oHdaDAYLr2HckSWdpzRCKhKFfeIiyvvCAQb_pyjSntRZkKH_CrkwpzsXvJhMJMSA3RUcVqSR48kldvyCbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=XGW6RW4asufE6yUbGonN33n4lgqzCsRVSNG3-bleo6CwtTMpo7JsFrAEF-IeKbXf2DMnx4tvjepJqHvfgWnZVDzaTXo_GGoCDp9IKxjCxfsJ02xst5eJwj4q4Clbsd1LR8ZTQm_oPESxsrWw1r2YyRs1Olvn0tKzrdtI57gfbFm7jz-8ZODl04aIB9ZxWAxLCQN6HzKXF9gOw5EY6Lu2fAIPWvjUAcFunFGI-Q5CTW3BIqyEcD8zHbZoARx-9hFxwRT1oHdaDAYLr2HckSWdpzRCKhKFfeIiyvvCAQb_pyjSntRZkKH_CrkwpzsXvJhMJMSA3RUcVqSR48kldvyCbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=gq5sU_RbfRlQiQQkVY3YMkKncKj42RNHF9Zjdt-j_lvG9xnezWrXbM3gyylBszz0joCpUUFrw0ggrTtVpIjHnwpzEL8r01XewmN02VzCeVz5eXtcKOP5FZXgqIeTlru6HnLuoIqu56T8EWJlS9IizFrkHb7Nqtqe_jGSBI17YV-CI78RofsCsV78iSznoqkmRka_LP-UT1XY4xDYG3tKCBTNVDBg45weMBVt-VEN3eUEV_pO7k-6MJlTzR4yx3G7PlpQVuibCUI-FCBYkUogUZc18g5SlIzoCRySQNdo7RBbAKjsqg45aTZqbngf8C4TGxCq38yEyAu_-2S3w9Z4BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=gq5sU_RbfRlQiQQkVY3YMkKncKj42RNHF9Zjdt-j_lvG9xnezWrXbM3gyylBszz0joCpUUFrw0ggrTtVpIjHnwpzEL8r01XewmN02VzCeVz5eXtcKOP5FZXgqIeTlru6HnLuoIqu56T8EWJlS9IizFrkHb7Nqtqe_jGSBI17YV-CI78RofsCsV78iSznoqkmRka_LP-UT1XY4xDYG3tKCBTNVDBg45weMBVt-VEN3eUEV_pO7k-6MJlTzR4yx3G7PlpQVuibCUI-FCBYkUogUZc18g5SlIzoCRySQNdo7RBbAKjsqg45aTZqbngf8C4TGxCq38yEyAu_-2S3w9Z4BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=iUvcxtrGq3bZsGbc3IGLQRW_7dxJMcujl7ke2Bk_8vkH1fpcr_JNbwnp9eqHAHwnOBBfcdZ4KdZdqFmX53GSqvk13JqXDWDO2b3fRZ3E8o6GyoqisWBrH02jn6WHj8VqswdtVsWx0mIZ_xsPGabEEVMYuPN7iQQ-uu5mOmFvkS5MtUghjf27vViiLD1a8sYtRORkpJenEXq4MX0BISfZSpvzFiZTDtbYW0foMr6yku3qKj3Es88ozxisx3n7y3S32qOIwfpkPReexbWivJ5JvamexaZGkHNCepknsnJOWE_G988Lvyd--1IzJMz7WP3NhZpwH_OhSEAkVGexKCTjUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=iUvcxtrGq3bZsGbc3IGLQRW_7dxJMcujl7ke2Bk_8vkH1fpcr_JNbwnp9eqHAHwnOBBfcdZ4KdZdqFmX53GSqvk13JqXDWDO2b3fRZ3E8o6GyoqisWBrH02jn6WHj8VqswdtVsWx0mIZ_xsPGabEEVMYuPN7iQQ-uu5mOmFvkS5MtUghjf27vViiLD1a8sYtRORkpJenEXq4MX0BISfZSpvzFiZTDtbYW0foMr6yku3qKj3Es88ozxisx3n7y3S32qOIwfpkPReexbWivJ5JvamexaZGkHNCepknsnJOWE_G988Lvyd--1IzJMz7WP3NhZpwH_OhSEAkVGexKCTjUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=n8tXL_S8FsEK4QnMALkKn6Ph-xO2nB_TLb-wZMi4Gvcqtm3kvXx5Mm2eHpUYNoV0rAHa-y3EcnCR-Ei-lO2k8NiY2NrV_ESXM4FjoP9hRInF8ITfwAaN3N24pIh3s3hjXiEJAuLNU9gQg2zCqe6WUaUupfctVBD6oAaqFfzb6Za99V9bqB4ilgQ6RQ1_MOd1NEKlbHYLGt2B8xC4xzS_nQZRLwP2eqkvFoD_MplRBNvyHG6rSgisymqDkmrlkVqLd1QEbt388cqP_eah9cHSaJvI_bu1wUFdyZchEgntRQ7shnWN6qIHB683aDbvroFaY2bSdR1WhMGYYU_-7CDh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=n8tXL_S8FsEK4QnMALkKn6Ph-xO2nB_TLb-wZMi4Gvcqtm3kvXx5Mm2eHpUYNoV0rAHa-y3EcnCR-Ei-lO2k8NiY2NrV_ESXM4FjoP9hRInF8ITfwAaN3N24pIh3s3hjXiEJAuLNU9gQg2zCqe6WUaUupfctVBD6oAaqFfzb6Za99V9bqB4ilgQ6RQ1_MOd1NEKlbHYLGt2B8xC4xzS_nQZRLwP2eqkvFoD_MplRBNvyHG6rSgisymqDkmrlkVqLd1QEbt388cqP_eah9cHSaJvI_bu1wUFdyZchEgntRQ7shnWN6qIHB683aDbvroFaY2bSdR1WhMGYYU_-7CDh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9prpaEYgiAoEi4NYfVurtcr1sbXUWf2wI293cLdfGQMeOFmTvNN1Th13Me6Y1vO3dDFknDbL9BXJIh8hzJ4jNomdvlbrVKH30llYw_YEwd2v3h9Dwprh2CVwOoYjhyHdzJC-0P6bFSXgTkAuGB4JC0NA4VscLzLhfLttUsylejJYld1gAO19uEGz6Y9lQqkqBV2YSi_ZiElFgdwtio4b6ZEmYOcuGkVVNNGbiTw2VwlBqOGPB3ilUyyb_b9FPKlzjUsYVOggj6UxipvPLr4Mb9_prPJt7FWMwvSfRDRXuq8ghZa0kqqxM28WrFtRJ8L8DElXwcmiX40XntrZuT8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t64K40HPsMXGFM5n2oW3VlBhSa_np-1813RF1pU8u6HakwxFj-erucoD7fUC6g5OeOEB_uzPDCqZ_WczvvDN5xwIFmtZCfBqtw6I8a7SCR_zZGHXd7A8fy6ZMOJq28l9f2Hx6VGr410vbOw0Z8T613FfwQXVg117I1I0-nF8e1Wi1u034aHU2i0CQvRPByFOTQrtBnUEUHONvrfuaAmXKWTinSpK0W8umx55I6q29OJsQH7k9TjGup79NO7U-xtAUChxhi4MWevL-5Hi7DM38rnVji2siqIijiA24xqBvptmg_7yJT1JK1Jno5NKNZvPPq_g4O6QSRwlXZd8Fhea3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=FnJe7c97r0UOruHOoQVZQXSMDZQwZXJxgKkEvmCxCdJK8GipCcYFxQnXZ9CgzvFnAoVp1ZZNXMzGkE2_PW1tS6m5SVKY0KF_aQLUmGLhQR87n4DsbPrkZPiEHuAKCstos0QBHkyk8BCp-gQptY9dRonxqVWI5ik-Y72Ne8weeW2C5FjzdZM_RY-zY7iUm5aCwfr5O7fL1usGgilRHlX8Yam-LrtR9b3zUDCP-qBRB57PB4V_1SZ08t7cWiE9LYeF7zaq0KTWPi2RZuehxG6KLXmQGJIvW8vUS0Qc3WQOGtOe9o31tLtKl-QNxud2U6sDpuJJP_r0a8gn2LQv8diIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=FnJe7c97r0UOruHOoQVZQXSMDZQwZXJxgKkEvmCxCdJK8GipCcYFxQnXZ9CgzvFnAoVp1ZZNXMzGkE2_PW1tS6m5SVKY0KF_aQLUmGLhQR87n4DsbPrkZPiEHuAKCstos0QBHkyk8BCp-gQptY9dRonxqVWI5ik-Y72Ne8weeW2C5FjzdZM_RY-zY7iUm5aCwfr5O7fL1usGgilRHlX8Yam-LrtR9b3zUDCP-qBRB57PB4V_1SZ08t7cWiE9LYeF7zaq0KTWPi2RZuehxG6KLXmQGJIvW8vUS0Qc3WQOGtOe9o31tLtKl-QNxud2U6sDpuJJP_r0a8gn2LQv8diIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6E921P7SOwJAoyBcFz2q3DoJMdG7ziXgWOnNo-ez3g-kPcpi7EYeyp88NJ-F5wyPciF-sj8AKLc46I-b2MR38jJBCnZgEHoP0a30jFjFFot6KzNAtiuTB9HHWj70iQtM1ON_Z3MlV7sTX-xj9Fky3HP3DXMgdhkUkltUHCm9nep3OP3qd-QPEyxn2XtaydZJeDdbd-eMhyKb85uCSrANu3INlMDrE6hmpNw8LrhQ440DzzIAaSDyHUSXppuheihHvugYNS0JfQiGOKqvPsVd0QIc4Jx1HrfddMFZspr9ShgBm9HdmhvNuYVSKtmSZ-jjcE0OOoZDNkw1G-_lHQWOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=DsAOSYkn_CYe5Ju9fGP0JE6jXOkWuXIS7o7GSmi1XR6es7pvoh9Y_daoaRdOWpaZN7Zl-uSIPMhQYQWf625dZ3U67zmiFPsFDO4ZCdwT8SwieiuFVSTCr3zIw9RKCIHKb6hikiMbItjhpZ-y8z3ziiTjUtgKFgLhXfmJL9rNfDo0Pegd6TEeg1EPEPew1LigiVv-dMGKFCBDkee316vHmsKqbgy-KkqK5z921T3tUm98ZcuHGA6lJq_WdBjSYBovXw4-hzW59uxX-KMhILAy5Pr1q2WGQRFINDHLMrKs9pc7Ov1OvNfYfq86cp-uIc4f23gP6i0Q4rxSH301iHKwsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=DsAOSYkn_CYe5Ju9fGP0JE6jXOkWuXIS7o7GSmi1XR6es7pvoh9Y_daoaRdOWpaZN7Zl-uSIPMhQYQWf625dZ3U67zmiFPsFDO4ZCdwT8SwieiuFVSTCr3zIw9RKCIHKb6hikiMbItjhpZ-y8z3ziiTjUtgKFgLhXfmJL9rNfDo0Pegd6TEeg1EPEPew1LigiVv-dMGKFCBDkee316vHmsKqbgy-KkqK5z921T3tUm98ZcuHGA6lJq_WdBjSYBovXw4-hzW59uxX-KMhILAy5Pr1q2WGQRFINDHLMrKs9pc7Ov1OvNfYfq86cp-uIc4f23gP6i0Q4rxSH301iHKwsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUHta-Xk_Cr8mT4YvA1-lgkCmWH7cI9i-fQvfJOQcmT-7EnnB0oXrFnwdXcfjVf4d6MgZyzpRWyQ0Ev5T_7fnIyE-5khCMiGu2V9awItO3ev1YsRLMoqgOd6aE1AzdqplaFSLwBk2kkoJPHqSYPVbm5xJf_FIElMBAxPKq094qwuP2TIy4TI_Z4SFIpH9rKPQG8TkNDg3vTneYcc9bIlEAA7M4vdVaERQAEG8kpvPZrs9CfYwe4T6G7E8mL-ENsMlHFxSjef4aRL8KStWH0xKaWfC6BPfUN1LuhCw26VzMHFJohH4_vpqTsnUb2DXyouSzT9ix3SYzhxztXyu6sL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsbRXz2BJ-Ho1HmlOuJD8tIoYKZIjCXXa9Ls0KWoTmPagCvxBU-ZSyqe9uA3wvu7b-8zoBFMiHqg3dJMEfzzvOln-U5Q_QY631TsKpxowEEEWxVJ_vY6lneOhqyl26kIlzX4G8JBPXIax5Yr7rxOoP5gKdxZ7CuDJ1GMHB44o2vDmRtTpLfYHvt-N9sE17MYoOCAL-0b1cJQdwCilEWZ1kqrFD5rEkGKnnaxOX6IN_0XNJfLq0EULPtf_NQJqMsEX9U_Ot80WT9cxO94eshnvJPNX5Ijk5UIfIJ3DT5FEHLfx4i20AxVBUaWrmgqKafDuiMWlgkt_aY3roLkcsV9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDAY2BOQrBcWPS-VonQlHf--QJx5opwaBGi0Ke_ja2rIY-hL2-KS-jwyW8XV5gkfwAktHcDWNsZ5ZcchwOqhRMUq62aTmhHywJpzmEzU7vHd7ZDjsTQHni-rOhLc9z3I07rsW6Xn1I88kbKcDPrO30-cNpAC2gvefdH18yFL-wSWMycyiJ2-nSJvIf2V_od24K81uOJpE0iv1PfllcwHhpKPpcCmdvJG_IpGZFeRORZYd620qAYnT7Ht3mrN75UmxU8BFC4-CkablwdCCoIl-BaZEgMmtaK36bmD5Us4h2q0ORsU8rCXRXVOqCfkXQ9p3NDkwSrF2NBO9dSne-7U8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqNd9A-GajUOmDge2__QMcWSr1HptbKmNkKrAImoRNMCP4afFqzBWp-eOEzbw5B1aLOeZvsLqAYBoPpUOSe6JbRzPwxkh3prfjSLk1i5N-IwamK8LVTqFCohRvhoQRa9yrnHX6YmNXvjBWe5eiPxRsDuToQcsOYYkEGw0zwuCFoci1JCWbWOpNbWodG9kKFRXXjQn8260CGUmJvuqh-pMRmd9tEOHk67ENfnQE-MY1kMTotZtjVJdzT1C53lQld4truplNaTa7Peb5AZxmzwbzMnRCZ_YYjAjGFwGd2Qx-ze0b4B97rz_pElVf8UNosKPWJpoN02tFsZJLSs14vhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRMFVygFvrcIGk5DEJZ8eli-1f9-q2rBEeYkdREzVJVCDWeSG8iMYDJ7vlneFHKLP4ztdG2zZ3GabzklQ5HvTF1tmwMNVqOSLxOS5zVib9P-WBFPNbmG47XDXvhaqlhzYscJtFMiW7RYqe4uQ7GTLNPcav0QZueNL6RJ1BnHurFI-NIU0DmSSgQOyDQEAUbcE1LstYcQyiRnskuaDl0wuWmbnO9ORmpt7Bkgg7ckbmghPmeSAFgF6CYRoRN6k5L_we5HhyiaTSYMmPdA5UnFj3_VVadwEeF4OO45-Ys1mGQlkuJPvv6GlYTudYgpruQbNz3VuiWVBYaw0lJ26t6-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/biI_1DKyN69uebeMhR0MKxqs8v6xFQPzmJrTrz-sg6tARRBGGNCr5Q7TaYSIvKJrzqLQVy9XoHSFBRI3wYMNKi6Pg8Gpjlhxu63LmFeb-Wgn-QoY_sJoa50_ogkqRzBfJinobeRzP8tAf811lg585ksvYbyQBU_H7Hs3ooaBgDtgm8MB5nnfJ3DTLZhage1uNH4r4zkea3amzZGTk4wj4ZgXuWGlyXHfSYI1gLfyO5HiIDl2W3vIaJOM7Ej2Q1TuytdWtQEl6hzzr_qU6iKTel44gNwVw0EBVm_jIhz2hSax1t5aqHJnI336TbB3pooLD5d3GM6x5QqoRQiG80WEEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQNIwIOQ1ui1ptNgeWx4IjMvlcu8gyvWeqtGrslV2Wxo5ozDG__AtkJIMvEYkZEK28At6AjiHb787mMnFALBctGW7RxGWpACe7edGutmW1yZ3gHju_o5oeidnCYwzaKGbwWGCb4LpZEJNTWCmij0HAigBZWfDOO4mWRt5Px6YMoRsfwLKmKNYykmnFe9L2uhqz6oE-AuE86UrxmxnailQqUrGOEo1FAO2YwaDG6bXHtV2t2uZ_ObSDJ-FbQFfp8NyI8LEeq8NrMZJNznzaI-x4VwNccMtOmC4Q33_PoyehhOX_bH3r7lsct9iU6N9FZVtEevdBs6fTVKvFSTyF-buA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9_bjBkrC0hOVR2SDYXkfZ1NDNlDtjE9XsUSNV9NjVP4s1PqpkjKskUi87xyzsfDLlo5A69jhsAzN6G9gJRq-9woSKArgF80SZ-S9TqUVySG6KGbmKkQ6nA19ifHbfpgujP1XBykXj4GSGp_EdNfNOJq7gfiI8BNnj_04HgRHyDpzoeSa0l_Qsxy7AcmFOkSVQDTsXlugCn3tFsIxAY1htjXDTqD1-rBuBF-XHQcQBu5haH69_bI_UtCEIjhnKkzG3xCRS2BiR-ECcPd0V4rJIrtIgDvpu7Ttf6Ant9hPbcHvmxF3VMRZvVWXb5m8tqCf0UqLb-8ikxkiDjpyILVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxuCHMfK9p4LuIbjOhYnTYaW2rR82dSEmX_8jW5Hp_eYqz8nlPfOQ-TAKA-xsMYUlz0m8bEacPYZLdEAQWXdMZw6XigKZRvxwfOgWV9nDYjsf1rtkAacDghelc8vb4oy9Drp2Sov0VvX1wttwGdQQzmk5EIPXcF4r8GQPVuBN8s0AL_mZJiBQkZsNxSSfAbYeW_5icsQ8ZxoAgEtt4E91h0Qtr6HJvQLb5ohS2chxUKogg3y7prPpSVXFMgo8fYWmKnzj2p1jwdNPNrEnhbw65ypOtBAhaK109y2eig-nqFbIPJj5IugJj_IRq42TjK7oFAJt8tOEXhcRoJ-Vgb2CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jneWF4KLXfTjL7-0OQ8xE_pR9imJFe-LoQZkICOoDkoCy4nm8RuiAeZqNvaigukBylA0e8DOmMk8EmQ7rp-HAMOpLdq9JYQSxvHO2sLVaKBDdqW1OI54AyWHRnvGHtzYhCJo77ZUPWkNVoLX6xQJN0LxiY5rGcQfHMm4U2Reud0rJfSWfWRG3h6hmSgwwZ8g-FoYCAAjfIevW5sViTTfjTuii1LTs7UozJjVvLVFq3NhZQrY5gvf5itkOa0LPmJX8ikT5sFudVG6qSkGLmXs1hIUQ_X4oNgeUbxljayoWLrqy10ZkNl5DS3wYilruE1ayfnLbK3_jbBYzIXlzY9Sww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyhGoydrJZ5_i3q16cfKvrQDxp-bTqJqdi-X4QWA1NKaSnyFg4wBsPkyj40qPCdv2rs_dYy3jWhtSatK8H3PJYgHAt_3Mmu3teRXlddEFbUEDmuC4Cb7YzE5ZFjplBqqr86JS3njdZJeCdQNAB3mPBctz5B3MORkov8NHnLxNPOCJrOiz-s9_G8vAcv4GCL-HxDMsbdurCU3Nym0A5jwVBaMvyhbXOWru4xKMVjRzf-4sdwaRFTZd-3t5CacE1T_WpRrnWDZfl2b6xxezvp0XQyqJxncIhDioy9kwE_5oo1B7Bljf18CFsn2w-r0zX83aoMYzMQ4dGrfaL2dESFYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=pPJakvwgaYowM4J1DfS-KpTBG_yrVlkWcstE5BtRuSYDvWhPMss_qKsED3MGqxf-nqCQc8_Qy47Twvf2cZ11t4VdijeEAuoabf6FX-8-8c12ou8HNkmzd7o2exjtdABNxMPXLp5xaZG_IklCiFa34--hXUB5VAhp9PrAnFKeGVJWXjORj9dDx7m7surwMNZcQMEvlGEMUFH3R9Tio9HTJcCmBj0df3Ya0jRNeFnmVJc6GHLXcpMCZxWM3QVphVUD-sWigrnwog-9YVMHijDqZp43D1wXxNFo3e0Y0kn68O14HppKO2xaA74CYfEnIYJMskfs74N4EjJ6IFMzxSvwcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=pPJakvwgaYowM4J1DfS-KpTBG_yrVlkWcstE5BtRuSYDvWhPMss_qKsED3MGqxf-nqCQc8_Qy47Twvf2cZ11t4VdijeEAuoabf6FX-8-8c12ou8HNkmzd7o2exjtdABNxMPXLp5xaZG_IklCiFa34--hXUB5VAhp9PrAnFKeGVJWXjORj9dDx7m7surwMNZcQMEvlGEMUFH3R9Tio9HTJcCmBj0df3Ya0jRNeFnmVJc6GHLXcpMCZxWM3QVphVUD-sWigrnwog-9YVMHijDqZp43D1wXxNFo3e0Y0kn68O14HppKO2xaA74CYfEnIYJMskfs74N4EjJ6IFMzxSvwcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na8v-OII1dsq2fdN--kv3_WYKTBj6IqAFILOyuecG1vwF0Z6Wfzx2cpcm0bmyDd530yyC7-swfYWeCA_YgGftTdD6YQWuoLQOXeKdB0WenoOPz1J5jmjUqGpxWR9M-TyvsVZlVLP3ZhXepkE9zPr_X5NBpbbFG0Ksh6cPifOy0Tw0n-5XlXLxM72cxJteaK7JOraKxYqoFV60Zr3OFxAf4YM0xSRmGmUCMXz3xdUM6P4Fozttk0lcMLpjLzBxPH0-LTMI9RyazJaZsYsBIi5iqhFn7CBUpeed3MEW_ZRbPWz6WE_BaXQ1JzRgwkBT-XnQ6XnwRNFsAXNbl7rDcTRMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=mL_IuKGM01dOWsDu2a3gr6xgpBvN6DnH36yWwSZ5xuTKNZPqccgnil8xYy6BvDfHpuRtRuZwF5HZrYmHrMUNeXJ4d7NREr-Nx5pyQfNTJGVbOI_O6KHBX0EHvcsvKfltBf-A4TkdEaM8999751rW6vYDzKcB_82VIBfxkUhWfCK1cHHhr92PdMMf1Ai8_wf8gdI1Yz91ztErZPRCSl48ZWORpsf3rlH6DLruWFIxAWELLNSCRp4VNhgLbvOabzBarCgsXTnB8dv6dxTko5F_QhkygNyLQYXgcK72O6EMt9KFtkt8WR-ipbx6_d8J4T4Mk-Xua7NDtwSHAJFYf-AlQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=mL_IuKGM01dOWsDu2a3gr6xgpBvN6DnH36yWwSZ5xuTKNZPqccgnil8xYy6BvDfHpuRtRuZwF5HZrYmHrMUNeXJ4d7NREr-Nx5pyQfNTJGVbOI_O6KHBX0EHvcsvKfltBf-A4TkdEaM8999751rW6vYDzKcB_82VIBfxkUhWfCK1cHHhr92PdMMf1Ai8_wf8gdI1Yz91ztErZPRCSl48ZWORpsf3rlH6DLruWFIxAWELLNSCRp4VNhgLbvOabzBarCgsXTnB8dv6dxTko5F_QhkygNyLQYXgcK72O6EMt9KFtkt8WR-ipbx6_d8J4T4Mk-Xua7NDtwSHAJFYf-AlQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHE3-BsrgdoS_RDbDKwFQwrLKUOCxgINedlnCSV_8N5C7meFQVQRpEQPtEFoGSmwmOFui9pFh6VoyGKrbkdzQ1nQm47ejCnfhZnNNZGi_7fWAFzJZM9Clpa-bAP4fixUoAeJoRMgsAcx0HqzuzGHsSna6T-17izpdFXONv2V3zNX8W6bjStnCUjpenUT0v0WXVjcM2YN68BrYPijKLFk78qLlzs6gf9iVIaxYdOpQTU68kGurrCrfPS08s2KIeYpAQdGmMmhmcYKpeeFTaMWP8fNk0chrejGs0Tb6bFQyscMYaVDddHSP16npwKQ9iIy2YH8_rHZ0brFpTgvpTQmJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNI5xmsmHKyMEa-9ojUUKHDZfoZwBArZ-ZRGjYJ6JLybCe_rOd9FQfD9Q2Ur4AgGD7tqepqBUsjC0Iq9CtjsOzeVzhQq-ogHArfJ6sKPvDIGsHi2zNBeAUOnq2TJ6gYKlNVKmGElqrtA_fjyk8mB711GJbWAcqyKKUoZHKyV99kzUjcmhFjX4TN6gUoQY7iiKMBzqLdRjzbkX5D7K1Ds9W20xSL3ZBizkClkAMdByPhZk00GZSSHSax14knBCM9oVPWCih2C5kuv5fo442SC11Pt3LULZyCLUrSfj3O60lowBIibtZJrVgW3XWXqy3Elc4f4V9nI9-cCGG3IvgG4yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=FypX3_FOYOeEf8YvhzSNLSc3_kdVXf06m5ohtg4c-glioZcqpGwH0rvRAYWgaMggoQJ8DE_5W8bmhcOYkQqSlMMQSLG9vJUE8rsE40X-vxv05NB1RHrlv0WXEm71FYtWi_10VFgjLaVDZCBJt-M7tyazhuvdPz07nxtBv3WMBfXMWhZ7tqGetdeZaG8Ir-bdW29yJBvnZgfWwy4tO8vSiA-cwqDC5bPWj-3eDVCQMGAzWUJyym3VO9S0cqMlUBykV_Gr4JEaEkTYT-hIvw7EpzrxM5zdjL-EVhrGPlqLNE2JO0HGFOENzTHpMYcpeq9t30fwQXUKjnnC8v34XPpzh10pglKQuwpqps5DOepKCdMUVuEKAcG8yD9tghTrXcaKyAjP92PA1WIFX4qvybcP-lJPsqTeQUmViWXWdIgGnhAW7sL0xPwwDqii3GcEi2cB9_aAUokFvCSsKcTZmekrbH2rCHnsds_O8ASBftoU-19wr6_fExCdyvDiCyWx6C5fyA47RPv8ydHmztQzv_Bg3BI2UUEZEJ5W-1j4W-qMNNOk66xxdchAjrUNaqakk6Ax28LIMNDY-YiFAD0DnCU64rEJJfPGvnT_SJ5zpF5tNbIr31CM2onz2KAzicwlMJzNwAe8T4OcSUIdzobgAuPtejG_MRCx78xe5mUOA0hK4sc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=FypX3_FOYOeEf8YvhzSNLSc3_kdVXf06m5ohtg4c-glioZcqpGwH0rvRAYWgaMggoQJ8DE_5W8bmhcOYkQqSlMMQSLG9vJUE8rsE40X-vxv05NB1RHrlv0WXEm71FYtWi_10VFgjLaVDZCBJt-M7tyazhuvdPz07nxtBv3WMBfXMWhZ7tqGetdeZaG8Ir-bdW29yJBvnZgfWwy4tO8vSiA-cwqDC5bPWj-3eDVCQMGAzWUJyym3VO9S0cqMlUBykV_Gr4JEaEkTYT-hIvw7EpzrxM5zdjL-EVhrGPlqLNE2JO0HGFOENzTHpMYcpeq9t30fwQXUKjnnC8v34XPpzh10pglKQuwpqps5DOepKCdMUVuEKAcG8yD9tghTrXcaKyAjP92PA1WIFX4qvybcP-lJPsqTeQUmViWXWdIgGnhAW7sL0xPwwDqii3GcEi2cB9_aAUokFvCSsKcTZmekrbH2rCHnsds_O8ASBftoU-19wr6_fExCdyvDiCyWx6C5fyA47RPv8ydHmztQzv_Bg3BI2UUEZEJ5W-1j4W-qMNNOk66xxdchAjrUNaqakk6Ax28LIMNDY-YiFAD0DnCU64rEJJfPGvnT_SJ5zpF5tNbIr31CM2onz2KAzicwlMJzNwAe8T4OcSUIdzobgAuPtejG_MRCx78xe5mUOA0hK4sc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzMe9OM0HlqPoB17nQt3N7qLW4QHguovN-kq1GAWOAidg3swHTOTosUWiluI4Yrs2ekF0Mw4yyNYkabNIoxYgd-dHgP6CIs9Z17ob4H2CyqjuedVsR3IRBTs47qlwevZUls28LTVL2rybXTFr4AZwWG5tbL34ew2BWoW1yWnN46mBdrR3D5fLsASWHuDfB2Dj7f2vmpq5VIk1q12jKAk08a9u7ZW6SRGwmr23VX8ix4g-l-CVjQPR_2CwmKGUROUaF_DXYSFdRSYe7JFdFf6dJPV7JxtLPxdxAw9gprCD-jEiQUxLFz-PK6yjzaxTitxYqUA8YIh2Gko5tby1e82Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFAtHl6-G4l8qIhYQC3im6ZvrBJKCxWDcnY1UcQuBVbmuN6R31nm2tGsATV3oZ3WjpqvAq5YkKEz_QitvUIpWJiopB_oFUFn55gsxkX38Bb5lzLzU5WHUAM_6a62KRtqZ7XkWtOUocA--7HCajHdsk6ZvHZOhWy7Ug25sbGGolj5650JEb-1ZlGSzB04Pe8n0i2TVKHe87mXCOcBl2cKXP95B-rZ40FQyX8rhBDY0rvOUuGJ0qIRnUZUH0jC-3jHum_ASZ9CNUxMJZrtZdpf9ZmIlBG33pwt_uMpa5fiE_x8WDuBc1ujrks5fEBcNnIdJhl2EXGGwutZUArHXOjRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJsVAeqdwWSdbYTTuKAlK47iRJAPEsthWzRuC6AQitYTOKxtxbSJ19MT2a5EytuZKYjJiX-m4I5WHcj_IBibGoL43Pcn6qxpWfNfWZT8JYDyLq5PTDLrjatk7u3vSkGn6hGCyOwvmBmoeTXAOvVzGRz08CLgup-_z60PH4mCYreciBgtQRwv5JCF5CVFpLpciBr94txa1ayz76A3MIxB6GM7f16-aXn4I2JubgJCchDpyTT0hJquxX7zU96aIBQ0c0Lvq6KpzKLGTgqfsam1dqEb1Ijt1SwyxCQxXPTR6J0eHboql1ylC_xLKApKkwnBRy3upu6M4MXbDFcFY5SD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=IK0U7ayaw9OFtwcNl-utBPLAtggQ5fjFSKfeVXVmHrDkO_efjpEw7H-PQdgysw-iQrwxY_DII8HGODGshKIkIwY03FSEMFTtl8DO7cHt4YygCy8aqRrZnbxe2r7_3pUnk699-24UlhRr9FYRoUK-e8RJqrlhHMjAtneKkdGVksGuQeJsk8H-eOKWToOiDGgyx_d2eeLr36ZBdbgRQHp7FQtkVRQXs6ODNsfIhWz9xANhu0eNwifJkaL0G2FBMDwxHlVb_2Dr5AvsSrnJN0c1uneIkuhI8grrc1CfYrOGobU_USW1g6ktZvESIHMa9sOQ-02qKmrd_kxHz6lPn9R2mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=IK0U7ayaw9OFtwcNl-utBPLAtggQ5fjFSKfeVXVmHrDkO_efjpEw7H-PQdgysw-iQrwxY_DII8HGODGshKIkIwY03FSEMFTtl8DO7cHt4YygCy8aqRrZnbxe2r7_3pUnk699-24UlhRr9FYRoUK-e8RJqrlhHMjAtneKkdGVksGuQeJsk8H-eOKWToOiDGgyx_d2eeLr36ZBdbgRQHp7FQtkVRQXs6ODNsfIhWz9xANhu0eNwifJkaL0G2FBMDwxHlVb_2Dr5AvsSrnJN0c1uneIkuhI8grrc1CfYrOGobU_USW1g6ktZvESIHMa9sOQ-02qKmrd_kxHz6lPn9R2mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyzX1frbR8l9VuwJDjNf1NhvGK7qJDX0-pXlct4gh-BqPWU29u_lWh2ptMqmL8p4ls1JoF9dvvHUJC3gpBw7BJar6tW2Ag0gIpooWw9oOlMh0BUCNJtaahDsxTejSVpOUCWnJLj9hB6T9L8IyDBgPfhlL3QlEuYIpAxBUL0vAyHmihyyFrMZ2eC8cl_ooOib_8DsA8yJ1FXdzjCPUC59WmtSShMKjmJyuZJX2JtDIqgyv9Kc6-E2_K03PYFai7yn5r16P5zrXJZxAgOOPKBYoJdYxikDX7swkwtSH2Hqr0sCdwHNmTq7SslLSOMYMddlFmU7ajETukaWZJrVqO8VoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pS4Zf_c0QH34x4xCcA-t303FNP586PpY1Z79SDjikhfgxcrRDJlaqmNkWOWet9btFpdRUuImIwbx4NoaixVUAfNf9zJFekYuVJlOdNbbb4rIc1egSOJjKue11dTdQwGxHDrkwMMmFrbduSSULdcKLZ6JRwr3NUeqVCWt1K-InNSBf-T-Dl5IpD-z61ecBB3f8lHOEcPchhmktQ1rWy67i6077gugULDjq85GP9Hc-vnvsWLYTXVA9hmwSK7W36eMbp2usHWWME9vYv49wtTA06f1prFkRJwlmWBotqmgnX8hdF8lrAHsSX66y3lGvXYTcbYIwmbHGnI7zAFS-WW0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu1Nqfl6ctiSZ4Pf8oWbnZA4v7btAfg4NVu24S5AoKcE6BHW7PNCxZaHxHaetnIJmk82EIEp889p2OxAqCHT92g5y7VyXU05_JPZCtkoa4N9hy2iKxZ5LegoGoraZjeJdt1-TOGEaaRc5JaxaJlMakqfxmIQcaC0ZimoPDNmJKQz4ziumIpBSXc-CpfSogYU5bN6OlLmmgxPvGn8pWdQaFDgZCxrPthJBYNmRhzkMaXz-S5oe38-nuCeFQJivg4SURi7fKFBWCbw-28d1LP02blMdUmCdJwckYm6qUpMyPftMYMUfkLYKU0g6R3SmNqFmJpJsUfaqd_uJj5VCreZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhXF8sMJewuH2m3fGh1acwqV2y76-emskV1E2zY0YWB45jq3elLGtKsYofBS-xNuWbAHwVztmh3sl4VztClChgT6aQIlfDHLmQy_tZrc010wWuo9ZG0HMx_FcfoVd6R2um5XIoffUhzoP7vjvKUg2-1qNNRtaROT5vdtTg2FdZBSBiO16bOGKMkP8zGBRYlctCOxBJLgWBLtWA9mzXIwdSrXT4ueDWHwHJTrwI_qIBbRL6eNpluRhqbyMIzojQ1lprOC9VEkd5tvI6x5STMWmVRaRTk8nCMmsqxRa5Xbi5WG6sDBrSRP9kv9ZbSHRI_nSqycC-OOWxaqWchSCuPQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdURbgjL5RqdfX40sJzVtSI2W__9wyNjxRCAFc4oHZxPXT6HDIOZcw9qPZ_krkwoHKqY2fxq7ONMMeQ7R8cAVEOIborITjlMj9ENPUJmk-sWj1e4_RIxiE-Rpq9PADbQigO65JoTMo0IaDtll20toPK5lQTeFgTji3i3VEs8Vj85a3jxMAAUAl28bmbi8nfs2m1ZYsN262nwfW3owEjeaNRVtSJiQTo7r072xxF-lFqHZSom_ZFl8au5l2tV4kJoW5ptgwSo4a0t5HKVXER_lUsX0oHWXZL4hv6mfkku_K38ARg0ktnCs4XDaxzGcsCP_kEvBpTI0Z9zB9BuHqqfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbjoYAdMha9N3FjkA0OwpsYKIF00yd4H-gjkNXpMkl0-BrPsxSqkr_bN9UCtuFqNZk1GmGwoJ-_hq9-wMoonMkMBnWUnjbLHQXJwmkDpblkcGLo0yxBjF2HoKmScBSoJvA-sKxeJ1Q-qBBvoZsUpaEYrqVW-QAN7G0PxdVUMKtDt7DiMFWrb5o2rGzhpX21MiHXfEpRImPSsXXPwYWjiPTXCcUFk7DwSRtiz_H7OF3YuQ0FQsBrEnp4ZSkAi3Utuk13vZY0iBmULthpBLdDBL3QK1wNGoxlQaA-K7_q2VoW937LZfJda5Sv706EglYbbOGGoCbN76YGKqdNyCxO3zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldlLlbqVdqyaNg8QF9Hy1EwnRJ2XXAHEffpHZTfYDNQZew79l6hJKQyS7Hb8bGFT_GqIAYZ9M0LS3GQ7WGL0x_a-z3-Vb7FJya6tqFQp_iwCiIPRoBMhCFCQcvNJshuLwgCwm_m_Pku307klWAf2WcCDYLvqEatoQpfrJB-LtTqzRNkDJ-xzT7TIMjRpHPNTRTn4VvK0AAWDcjOBbDcTdaPl1cbDzGz-MxoEm2DzaKXDDYobvLh-HLw9Zbqdt6fGStIqCpYWTtEh5H_LT3oQOWa4rO38ZLdUocB6xrt8Hq0R7Uqk6pqaT9URfVgrh3C_kfow5FHdGzqtiXXR6mOA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhbXtGQ0MaJxsw_WmOisyQaVe2WjkV2MOYkLUpDw7kQKvs2t7Zd8q0NF20mZZKWwwGNXmVVvQTtQzp-LmAqUy8yNROaHqWZKghw7iVTslSSf5SZbkEsALioLaCD8m_QXdrVWF3MzarbhVh4zLGKiqjsxHJDnFkjPf7_q5j01GVeLR3hOJFICXw5fLa5oEQm6BBpCxFElDK7AG_0eHGERjw9q-U2DrfHIOyxtbKDrPwB2tfYa1Fcq30guRT6BS-ZuX5-Uy3efKBbF1ex5s35b4LqowM1ECJCguxbPDcrCfMT0AzWyxPEX8oOt3Isp_u2VYt8F3mzJhvObAN_xNy1L7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWdEEyiQvJRT4AGT_fvZC8nWHQQR7N9mhSE7zzIw1Hrg-uD-z8zznzuQHF-jmleeAcF1cTTx07tRTF1TVbGwuNvFZgWrQ0I-2HsMeDjDQhDym_I0UpqCKB1PZGMkqHzmZo5MDFpoacW8sEIcu0VSniCqQwQolJDK7eQq9V4Yy7wgZ41fXRtYPkGBSzZCyHv08GKSLnmXOtxQuuQuIJAEGcbMx_EcMkqk3hS5BxAIYpVPsrOKI22arvu7pOb7yB5QVSP5pl4j90hM1PySbuObVYVH8x8t-x6CWMu9q-y8r9mGEUdw2Yu3BfDd8XtMgZbMD4U7gjAEpG1nWD5Tjm6_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9unGodQB_q9TqjGuBkzD7T7necri8ZBGuuMJPocj8gPRfI8VSB_tNwNBc6J8jlrkENKE5dR-OQoUSZb-gmJaaRXL3WcV2MdTwiXggHksRzoNCdtPlbS3yKCsdFTkARssNHCcwzCgmizXxpsKVi-whyLB8x9oEgHwBEHaKD6YjrdgAzCGCD5EHMNzLHXfq_xYpoFgbYEQAs9DuW7oflY1Em6UlvxHCFLvlb8ivjYOoITVG2vxRSi6Qr-DyUmFCuphx-_9vd036weKn-aWLn9dpIBKsvUkUijiyiL2_pzhfc-RD7PEpwe9Rg_1zN8lki5Di0ejrkL8r6UOf4tSIp68g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=iT6Cbx4yF_6r_xcWqrZ0Elc2h3j2E1eUg5oQLHYb-3p3Cb41RS4ZuiZk38dWBsnq-DeFlf9JRiWcwajHj5gVQZm1s9Kb16vBL3hxYddX2E2ddLd7J3-7rGbsuVpFmM2LJEKNe9btm1Ok97UYnbXajzHIFt9b1kuMxvRR9MNNgDlfZDcvCLWHeSN6YoFpavtXzxGXnGkLFMwHFYS_McXMwZINr4YYRtnjj2VlM5toRnp3GJM6FZ0mc2SBOcLMQbrEig8FXUbVWCEyWABe0A63DfqRGUz8BMKqC0nmI7oFjnHD9OuJjQdVKNR0NrLcxIMK6NPzM1Py4wAqQ1YhfLjxfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=iT6Cbx4yF_6r_xcWqrZ0Elc2h3j2E1eUg5oQLHYb-3p3Cb41RS4ZuiZk38dWBsnq-DeFlf9JRiWcwajHj5gVQZm1s9Kb16vBL3hxYddX2E2ddLd7J3-7rGbsuVpFmM2LJEKNe9btm1Ok97UYnbXajzHIFt9b1kuMxvRR9MNNgDlfZDcvCLWHeSN6YoFpavtXzxGXnGkLFMwHFYS_McXMwZINr4YYRtnjj2VlM5toRnp3GJM6FZ0mc2SBOcLMQbrEig8FXUbVWCEyWABe0A63DfqRGUz8BMKqC0nmI7oFjnHD9OuJjQdVKNR0NrLcxIMK6NPzM1Py4wAqQ1YhfLjxfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=NIFLYmIbzI87XMLJq1RAqQsLg8aYjNDGAWglI0WOVlEjwefuMUcT1Bh1nF_0_a5uZF4MJZAAbBKX5UEgUpSkiZT5kHRNGqcLla7GOifO-1uBfuzA2bZ8eh5GEh7vvnlvZbEU0NKnOQ7mA1Y11FsTaKnRh5dW7XJBWdF1NSQR7sLNUHxnO4bjvrWogpLp-2hbqEdlxwhxZ_bzYPeTyPbjlTg4zxI_QbAfsvaCB3LG-C2Jd7LALyNB_afSb6bDesDuIP8rnmaeAB75WgKrTNfq_sqgpkdTVMdrTjJmUDM9gUi5G8ZFdETHD_96rdSa0c_JBCgXngGfwJAov4qMWI6nI4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=NIFLYmIbzI87XMLJq1RAqQsLg8aYjNDGAWglI0WOVlEjwefuMUcT1Bh1nF_0_a5uZF4MJZAAbBKX5UEgUpSkiZT5kHRNGqcLla7GOifO-1uBfuzA2bZ8eh5GEh7vvnlvZbEU0NKnOQ7mA1Y11FsTaKnRh5dW7XJBWdF1NSQR7sLNUHxnO4bjvrWogpLp-2hbqEdlxwhxZ_bzYPeTyPbjlTg4zxI_QbAfsvaCB3LG-C2Jd7LALyNB_afSb6bDesDuIP8rnmaeAB75WgKrTNfq_sqgpkdTVMdrTjJmUDM9gUi5G8ZFdETHD_96rdSa0c_JBCgXngGfwJAov4qMWI6nI4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
