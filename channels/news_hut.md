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
<img src="https://cdn4.telesco.pe/file/LP84syQkixBjY2HgrjZmL23Lf9f_T2CL_5XYZ2pi2UwzHAnG1YmR3exAiZ2g-4YA8BmhPaTbrr7IuOh2M_MLR1xWvg9BicYjp9dZ76VQ0jatZIGpfxdj-0-b7VXjTaUAu-GT3yZ3C55NgtgbkOBq7V5XGLjzfjm7RR8aB9igjTpMPzRI8jLJazoleiMlX7oeqtobxE_hDP2pKfz75F1T6Bnwh4MYm0yz0cDcvnDibXw0lEmFh-dFhq7i5aqtbX5TXAyM7R9HXvNqT48mlBKYB1N3yfRSII8ruHZ8tSDyco0GBPEphfU6CRwwF4TkW3w6jJyGrWG0UnrDzV1t3bt0Hg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 23:46:47</div>
<hr>

<div class="tg-post" id="msg-72746">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=ebiJENrdneP_LFXYME4aUrILVngnO3i9sQ3A4WlT7_5yIuhMybEW3X5tloF4alBoVbeauRAMgL8pI8wV1d0-UBTQQDc2jI-WOIt1Ka4pulwOmQvpYncMMcQ2IHLt_7koo6EVZlZarfmTTHb2sg_4k_VNUAymuUROzy9IhO6Q3iHnIZYi8OXbzVNC1GwrC2_C7fhTF4P0GH8iLb8_Rbwdy6p9fXmm37jCDS8CqOaU8xgtuCqejGq1FOvoIeNJzJ6l6Vjhe_bX_cwHZV7Tacj3imMoPTgAiEqRWvwFUASg9HeHOGteGWKC8PTl8WwmcYwy1JqYgjrYLHM7uOFJ9evb4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=ebiJENrdneP_LFXYME4aUrILVngnO3i9sQ3A4WlT7_5yIuhMybEW3X5tloF4alBoVbeauRAMgL8pI8wV1d0-UBTQQDc2jI-WOIt1Ka4pulwOmQvpYncMMcQ2IHLt_7koo6EVZlZarfmTTHb2sg_4k_VNUAymuUROzy9IhO6Q3iHnIZYi8OXbzVNC1GwrC2_C7fhTF4P0GH8iLb8_Rbwdy6p9fXmm37jCDS8CqOaU8xgtuCqejGq1FOvoIeNJzJ6l6Vjhe_bX_cwHZV7Tacj3imMoPTgAiEqRWvwFUASg9HeHOGteGWKC8PTl8WwmcYwy1JqYgjrYLHM7uOFJ9evb4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای عجیب در تجمعات شبانه: حسن روحانی در یک سفر استانی دستور داد برای دستشویی‌اش کولر نصب کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/news_hut/72746" target="_blank">📅 23:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72745">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673e09822.mp4?token=DcEm1MKiQ2qQbN2t3OGz3y-1Z_U2GH-knZZaKexBkj1RJyvqrMn39Ih-DarGsIuQYLgVMcyQVWzdOB-m_qA8OJJErlViR3XAcLaxpRjJgTpdUrOdlVYO_6pOFKkSegshRj1q01uBqGsTwot7tVftXY5bK1M0DRi6UdgJ1hyD6GmCEuDPl_aTjrDN5vJiPcLYqEyYP9730XCANvn1hh6rqnHHK1UIyyOS_dqjEPmDcaD5xsXi1NEjByqddJK5jvVF0MwJpyuTNs_UCKV1_ocRKMxdagUnStS8z53_lkalEoil_Kihu9Co2eN2_WcEEz0cHE8JiYOYBDCps3EIttNtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673e09822.mp4?token=DcEm1MKiQ2qQbN2t3OGz3y-1Z_U2GH-knZZaKexBkj1RJyvqrMn39Ih-DarGsIuQYLgVMcyQVWzdOB-m_qA8OJJErlViR3XAcLaxpRjJgTpdUrOdlVYO_6pOFKkSegshRj1q01uBqGsTwot7tVftXY5bK1M0DRi6UdgJ1hyD6GmCEuDPl_aTjrDN5vJiPcLYqEyYP9730XCANvn1hh6rqnHHK1UIyyOS_dqjEPmDcaD5xsXi1NEjByqddJK5jvVF0MwJpyuTNs_UCKV1_ocRKMxdagUnStS8z53_lkalEoil_Kihu9Co2eN2_WcEEz0cHE8JiYOYBDCps3EIttNtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سیل اخیرِ گرگان، یه
موش
برای اینکه جونشو نجات بده، این شکلی داشت تلاش می‌کرد...!
@News_Hut</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/news_hut/72745" target="_blank">📅 23:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72744">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=OxXGjIolj5pSY-1ohqfLHeX7Q-Rx6TPWzsH7OeHTfCRuMNxWBpX8XljqA6QWo6CmB8b8tfbZqIL0TQdym_kqKJYjbxOqyivP-Htv8obNeywBbO0xWdO9_AKWWPfLHOV6I2qU7SKtm6tXDWLZ74ykrykC9rnXk6wZOXodoeeP768vLTI9mcJPPmogT1qZPlyWUThdpIFIfRuuMgmi9vcbFrDSD2NJHAbnmItrbeO3WcRCPnWLb_mPcxIK4yMI1Mk-8TIz9rrUASUDDVrPJi1g-J80aI0CmC9M-QaPX6QyubpQQNL-_6BJSh7lYFYpw6YEIlQlvp8FjNhWl9GhY4yjYYQjT2PZ4BZq66cY-p0h4CBSMZDyTE1XL1_j_aEK417cU5rpfTXyvIgFV4Gg_5aapGV_8TzOa0gfyigIGhiztC9U5PqdwcLx_YmiCbTg9y__tywCTP1FA7eDwOTQz4Gp72uRlV9b8tTDJZgBoQSsCeRM05SoJCaJiOhY9AvFKQzgUVY69t4fJ961n4-Kc26Xlo_oLTpGAporfestcN0fgd2i3pFf5ZrT-d7R_Bu2qGcwZsJ8tzPYDzh1YmcT7Qp4AQoBQilsVx6FYdj6KDfvQSPocD_TGgRwvrIum5joSeRQHOfRyFOdD9hHYFaoc_pO9rw6yvfBWh1HoglFrpeSjNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=OxXGjIolj5pSY-1ohqfLHeX7Q-Rx6TPWzsH7OeHTfCRuMNxWBpX8XljqA6QWo6CmB8b8tfbZqIL0TQdym_kqKJYjbxOqyivP-Htv8obNeywBbO0xWdO9_AKWWPfLHOV6I2qU7SKtm6tXDWLZ74ykrykC9rnXk6wZOXodoeeP768vLTI9mcJPPmogT1qZPlyWUThdpIFIfRuuMgmi9vcbFrDSD2NJHAbnmItrbeO3WcRCPnWLb_mPcxIK4yMI1Mk-8TIz9rrUASUDDVrPJi1g-J80aI0CmC9M-QaPX6QyubpQQNL-_6BJSh7lYFYpw6YEIlQlvp8FjNhWl9GhY4yjYYQjT2PZ4BZq66cY-p0h4CBSMZDyTE1XL1_j_aEK417cU5rpfTXyvIgFV4Gg_5aapGV_8TzOa0gfyigIGhiztC9U5PqdwcLx_YmiCbTg9y__tywCTP1FA7eDwOTQz4Gp72uRlV9b8tTDJZgBoQSsCeRM05SoJCaJiOhY9AvFKQzgUVY69t4fJ961n4-Kc26Xlo_oLTpGAporfestcN0fgd2i3pFf5ZrT-d7R_Bu2qGcwZsJ8tzPYDzh1YmcT7Qp4AQoBQilsVx6FYdj6KDfvQSPocD_TGgRwvrIum5joSeRQHOfRyFOdD9hHYFaoc_pO9rw6yvfBWh1HoglFrpeSjNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک جانفدایان در اصفهان، سازماندهی اراذل و اوباش با قمه و شمشیر و چاقو!!
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/72744" target="_blank">📅 22:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72743">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzocfCyvuEquKTPBUucV8FJXLEuiN9R_F_vtd39tl3vVT32vbakSwsbtnr9KYpaBfcdRshetWYg9qmeFKLY_H3gTgChF_crMAhdb1QDXGiMURu4vybEaEmjKbt1P3OCmh4IxtukXe9F12w84zXYZAjQX_Ev6aPLj-5wXtevCZOrMHAYgxHgXr3fFddvhVNnqvsy8MZjajd7cqiAg3-LsCLIfowe0FUXk0bs12Fa_q7W20gGRl9AyoYSaD0EjfZQhYgkqzM5G6ESmGjcsfFUUL36FtkYd-JRjsEw-GBy_Go2xHZI0vaqoM9rQQF-PGP-0kt3P7Yjp28iY-cl2vnBmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از خود به همراه پنگوئن‌ها در گرینلند منتشر کرد.
پنگوئن‌ها در گرینلند زندگی نمی‌کنند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/72743" target="_blank">📅 21:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72742">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم   @News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72742" target="_blank">📅 21:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72741">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72741" target="_blank">📅 21:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72740">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=XWCvx-Xoi3-zS9ih_J3fai8sUI20OCY39ChHsZOeaHEgO6eka2eko8V7_EBXisto2QD0oKPO__B4YM6CkUi44TuONnyrnQlXJSQHufK_LrS9F4n3nKhpKcsnU47b495j2sxCCAZutFL0ZYPn8bZew8nJ0aMRFm1ls3j1kp3lh2iyvHhtMwr1IHnqhY8PnE-VJAEgENp2toNGmqIBDAPYxNziaqOaWWL2Q9AIUKEkjF26-URe6w20lJclyozDbR-BcFuRrve7BhaDjREBTTsnhct3hd2blyhYP1Wa3IWixXYo-TIiojL47872L2ALr_VbQrrZEqr7aVAy3_jjq24wBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=XWCvx-Xoi3-zS9ih_J3fai8sUI20OCY39ChHsZOeaHEgO6eka2eko8V7_EBXisto2QD0oKPO__B4YM6CkUi44TuONnyrnQlXJSQHufK_LrS9F4n3nKhpKcsnU47b495j2sxCCAZutFL0ZYPn8bZew8nJ0aMRFm1ls3j1kp3lh2iyvHhtMwr1IHnqhY8PnE-VJAEgENp2toNGmqIBDAPYxNziaqOaWWL2Q9AIUKEkjF26-URe6w20lJclyozDbR-BcFuRrve7BhaDjREBTTsnhct3hd2blyhYP1Wa3IWixXYo-TIiojL47872L2ALr_VbQrrZEqr7aVAy3_jjq24wBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۰فروند از ۱۲ بمب‌افکن راهبردی B-1B Lancer نیروی هوایی ایالات متحده که در پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) انگلستان مستقر بودند، در حال ترک این پایگاه و بازگشت به خاک اصلی آمریکا هستند. انتظار می‌رود دو فروند باقی‌مانده نیز امروز این پایگاه را ترک کنند؛ بدین ترتیب، دیگر هیچ بمب‌افکن راهبردی‌ای در «آر.ای.اف فیرفورد» حضور نخواهد داشت.
پنیک نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72740" target="_blank">📅 20:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72739">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtya6Sv8nW8oOKNRPoCxKGE8ezPZ8N26C6CMfmjKKKX-uRp243ep_2W40QUcRpDQqblExFlu7Ww0jK2z_N5n9tg7YoGbG5NmywpmID5wSkXnrx7xbm57nuzE3p_30A-hI8c2zkoHwofK68U4UWWh14s_QnY_OZ6OAEYkC5YWLYN9nr7-LjJ1dYFaUg34BXfWiLLEooGQrkwT6MWqRqDlogC2ojePMwg5mkoJ2tCCPl4H0_dPKuI-YltRG-QARHn5TYPPX_5mFDuoNpRnDEexYLdtuoD8LfcFPXakIrh_RtDPoVH_zixAERmjio3N_p3F0tPnrXYm7UPq1Qkkch9iAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72739" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72736">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=gQcY2gMmK3zxiae8akzNTB2MzcIGsHW4v5lbppgtwkD7FixVu1HaVBcmlo76z21U26gWr79wfdtzIBm-TNnF48UbVtdb0hOc1hsqeNZ-DvfVnh1d3421nah00zgEUTjca69LeNxE8iCOa6GM_E48PovZF7Eq6DkJPKmhPhTvwnFD3pJtyZ4Ni8EWaSKX9dzyCmBstuoMRXeOyy_lUgR4VjA0xcljJ8cKgoDvJNAMcs0CtiZJUznKXgcoRfoWcecZ7nyrHHeancnxvearWpaPlEgPfe6l7M_lVn_UQlhTovppsCTnIlnm65jv0OhaMY6mdJggocjPB8Wk0b9sBPthmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=gQcY2gMmK3zxiae8akzNTB2MzcIGsHW4v5lbppgtwkD7FixVu1HaVBcmlo76z21U26gWr79wfdtzIBm-TNnF48UbVtdb0hOc1hsqeNZ-DvfVnh1d3421nah00zgEUTjca69LeNxE8iCOa6GM_E48PovZF7Eq6DkJPKmhPhTvwnFD3pJtyZ4Ni8EWaSKX9dzyCmBstuoMRXeOyy_lUgR4VjA0xcljJ8cKgoDvJNAMcs0CtiZJUznKXgcoRfoWcecZ7nyrHHeancnxvearWpaPlEgPfe6l7M_lVn_UQlhTovppsCTnIlnm65jv0OhaMY6mdJggocjPB8Wk0b9sBPthmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رتبه یک کنکور تجربی همین‌جوری داره بین موسسه‌های کنکوری دست به دست میشه و تو همشون میگه که من از بچگی اینجا بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72736" target="_blank">📅 20:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72735">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112f06092b.mp4?token=aLSq3-monHuHXEztNh02HYJiOBQF4kXe_zEhwH_DGCB9Rx7b1rLKEapE1omAhuCTDC0zQe9N2ILg5klWwtnC-3bQfw3SlmIMTMrV0cBK1V9XTmz4_mjWnIh9mM9Ratc2c2GR5dGHLLAnfJ-eIKXVvnWfYmnzpp6tbzz8zkkg191vg_Th0LRLQjzMpXjLW1HgYNIlkoui9ygSHgWKq_7ev7YtwUIZ53lu8Z31QTkjpPMPNmI7kZCv5bkXb3_s70N8EQGwnbo18mWxttLG2Kkf6gBjrU9GlHt52R1S1qzEfulZFsTh-TznTQJMxLqSkeHQqOQlsmLFkzpWtYf-4eOK82Zm4Aw7PJxZf-Zy2dhdpb6ZRkV3eZG4zS19v7gMRwRK8F_7K6Xpw8ZbCpWUugCNQUAzhwXyGU34Ky278-QJ7nvCEDodvw09Er-JJTqxIxbxoeMnwdeWyak6IQtOLSmfqlHh32GjYeuKseT6RQAeOo95c0C_gMy1cD0SvOb3shqdLtmmt8qNbvRHWqTz03qRxbqFIT7AIqM-dYOFWixFFTTFX25wBwfHqkXzqp9iepC8tJQrqjsCmpDJMhL63s0AmF-F8mehskvNhe1DsIkwHgBVQPOn9kF9Yta3iVYXJly4SJwFyV8m6MKKbVjudp9Qeo5au3cExOQtjwpE8LENCM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112f06092b.mp4?token=aLSq3-monHuHXEztNh02HYJiOBQF4kXe_zEhwH_DGCB9Rx7b1rLKEapE1omAhuCTDC0zQe9N2ILg5klWwtnC-3bQfw3SlmIMTMrV0cBK1V9XTmz4_mjWnIh9mM9Ratc2c2GR5dGHLLAnfJ-eIKXVvnWfYmnzpp6tbzz8zkkg191vg_Th0LRLQjzMpXjLW1HgYNIlkoui9ygSHgWKq_7ev7YtwUIZ53lu8Z31QTkjpPMPNmI7kZCv5bkXb3_s70N8EQGwnbo18mWxttLG2Kkf6gBjrU9GlHt52R1S1qzEfulZFsTh-TznTQJMxLqSkeHQqOQlsmLFkzpWtYf-4eOK82Zm4Aw7PJxZf-Zy2dhdpb6ZRkV3eZG4zS19v7gMRwRK8F_7K6Xpw8ZbCpWUugCNQUAzhwXyGU34Ky278-QJ7nvCEDodvw09Er-JJTqxIxbxoeMnwdeWyak6IQtOLSmfqlHh32GjYeuKseT6RQAeOo95c0C_gMy1cD0SvOb3shqdLtmmt8qNbvRHWqTz03qRxbqFIT7AIqM-dYOFWixFFTTFX25wBwfHqkXzqp9iepC8tJQrqjsCmpDJMhL63s0AmF-F8mehskvNhe1DsIkwHgBVQPOn9kF9Yta3iVYXJly4SJwFyV8m6MKKbVjudp9Qeo5au3cExOQtjwpE8LENCM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه محمدرضا پهلوی:
"همیشه تلاش میشود ایرانِ دوران من با بهترین دموکراسی‌های جهان مقایسه شود، ایرادی هم به آن ندارم.
اما درباره اینها (ج.ا) که چنین قتل‌عام میکنند همه می‌گویند بگذارید درک‌شان کنیم، بالاخره اسلام وضع ویژه‌ای دارد، در حالیکه آنچه اینها (ج.ا) می‌کنند، در تناقض با اسلام است.
حتی در لیبرال‌ترین محافل، دوران من با بی‌نقص‌ترین دموکراسی‌ها قیاس می‌شود اما به اینها که می‌رسد می‌گویند بگذارید درک‌شان کنیم، اجازه دهید با آنها دیالوگ برقرار کنیم.
این چیزی است که برای من قابل درک نیست."
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72735" target="_blank">📅 19:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72734">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=T_EZOQrK8EPoHdi4a5vMfS-Td-XP6vvSswlExloHfigm3D8tWxV7kfZkLmlkI424OlalJHkpSpMXVwPL9dAZJdE2mR8RxjV2H4RNoctm5dxMXbRV7Xpbm99ht2fNIp-XuoRVmGA5UnR5jQglVHfYfBek4QHu9_F9AaGDH6slvQK_TtIbH1OaOv4woUcZi_QWTvLRtE3NFigkBl5nwu5dJ0ifI4sNBvjJXx5XNgL0nJ8_NegxjLYnaiszrnOulXGxTn1PkJawG8IP8IYefN8181QMkRVz6owpsUA6Wfv_9Ldp8wFLQYAZo-gewQyuksZhqcrSpGEJ46Fpvod4qJrqvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=T_EZOQrK8EPoHdi4a5vMfS-Td-XP6vvSswlExloHfigm3D8tWxV7kfZkLmlkI424OlalJHkpSpMXVwPL9dAZJdE2mR8RxjV2H4RNoctm5dxMXbRV7Xpbm99ht2fNIp-XuoRVmGA5UnR5jQglVHfYfBek4QHu9_F9AaGDH6slvQK_TtIbH1OaOv4woUcZi_QWTvLRtE3NFigkBl5nwu5dJ0ifI4sNBvjJXx5XNgL0nJ8_NegxjLYnaiszrnOulXGxTn1PkJawG8IP8IYefN8181QMkRVz6owpsUA6Wfv_9Ldp8wFLQYAZo-gewQyuksZhqcrSpGEJ46Fpvod4qJrqvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های عربستان سعودی مقر نیروهای خودی را بعد از اینکه به تصرف حوثی ها درآمد، در تعز یمن بمباران کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72734" target="_blank">📅 18:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72733">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMaIiBKSTuxI_lkeE_IMPfwdYsrXkMj24jsOTJGUQnFLhLZJHtvxLCldLSV1lGFAVOzJLizRJj1zv2TaSbDDSpfHO6TRosyFudDpCI-XQuqUkE2ZYXSC2BeiXSOAxLmq5C2xQ4qT-ammhEETs-UgieSDE4_XVtZthYULp7MUHWcCFVVcORiQR5oaM5qftE9QnOLDgzfNp8Sy7BqbKt2hE174Uo3kLfHZdKVq6Jug7NZ6jKzuyWTJNNicJa6q9V0nK4Bu8NskLdAZ55oQGO8q5x0H8OK_A5i7JU2w96fEUkUB2bSqzOaxLkGmkIKPRwEDDWyT29ERcHkcgK-QyGA0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده با ارائه کمک‌های اطلاعاتی و پشتیبانی در تعیین اهداف، از عملیات تهاجمی تحت حمایت عربستان علیه حوثی‌ها پشتیبانی می‌کند، اما به‌طور مستقیم در نبرد مشارکت ندارد.
شاهزاده خالد بن سلمان، وزیر دفاع عربستان، از پیت هگسث، وزیر دفاع آمریکا، درخواست انجام حملات هوایی کرد؛ اما مقامات آمریکایی اعلام کردند که واشنگتن فعلاً قصد انجام «اقدام نظامی مستقیم» (عملیات کینتیک) را ندارد.
گزارش‌ها حاکی از آن است که فرماندهی مرکزی ایالات متحده (سنتکام) با انجام این حملات مخالف بوده و یمن را عاملی می‌داند که تمرکز آمریکا بر ایران را منحرف می‌کند.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72733" target="_blank">📅 18:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72732">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=ky5W8chamQ-L3pISWdRfsq0e6SFx5sRijDftivE5szc5UWB8RU6VmqgMj9PDhQopP9O7rxmrGXsE_6WOllqG6MBRta9qRtsVgeHVU1Jl8q9i-7cX19s6hF6oHqs_B5wO_2FtoIVV9Dvou5wIP-TzCkzzTBiE_O6VucgsbKiIINPbIs0XiNl1SNK5YO0V1uv9iQdgPu7cMNsbVlQ6e35D5t5J___ClMBjsOsVXl1s5GuSRQdbqeYFFKeKCBKlx0ggZ_X7rH8Sl-DpP7xLrsOsr7MorQRgcrnyhaOsiH8Mr2vldwdJ0i-VGRTIm1G6oLp_fSMxM9Vodfdcwk2bQh35Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=ky5W8chamQ-L3pISWdRfsq0e6SFx5sRijDftivE5szc5UWB8RU6VmqgMj9PDhQopP9O7rxmrGXsE_6WOllqG6MBRta9qRtsVgeHVU1Jl8q9i-7cX19s6hF6oHqs_B5wO_2FtoIVV9Dvou5wIP-TzCkzzTBiE_O6VucgsbKiIINPbIs0XiNl1SNK5YO0V1uv9iQdgPu7cMNsbVlQ6e35D5t5J___ClMBjsOsVXl1s5GuSRQdbqeYFFKeKCBKlx0ggZ_X7rH8Sl-DpP7xLrsOsr7MorQRgcrnyhaOsiH8Mr2vldwdJ0i-VGRTIm1G6oLp_fSMxM9Vodfdcwk2bQh35Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
در جریان این جنگ به این نتیجه رسیدیم که قطعاً باید برد موشک‌های خود را به ۱۰۰۰ کیلومتر افزایش دهیم، زیرا دشمن در حال حاضر در فاصله‌ای دورتر از سواحل ما مستقر است.
اکنون در این مسیر گام برداشته‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72732" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72731">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72731" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72731" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72730">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmfhAOvNZ3y4hgDmuhzVNQGHuVtE0F1BzgNLEyT9B88KX9C4Lne-a1Pau_UR8ZgTwhMrtsl4GNDbPDMQJSjq4R7n6QN_Pn4On6fmRSefeuXJIOEC-5KU5cKRrqMHmwTVGhnwqSATyLXY5F65ChDTxzSbgoecqWj2DAgTAKE5JydIYuaybLpzKJiG066JO9jGoUV9XIOTgcv53kqQP8g5nYR4RW60tm4VCCXX8tkbdpMvKz4DRr5cO9pl5V76TVjViNzYmpCX7sDAaitsskQ8hCt9X7h10KTmtxWKPRIOPWPDNJdKmHP5FzZBzjWFFVnZs2kVukEZKQyoibHVkoy4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز نروژ
🆚
پرتغال را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
نروژ: ۲ برد، ۳ شکست و ۸ گل زده
پرتغال: ۴ برد، ۱ شکست و ۹ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72730" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72727">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKiY6TT2IDJd8flplMrcJ4tke_55_VYhDJyhAJiv9EGM6uHRC6tAcEil6vvWvti2gHjmKpT9f4U-gDVH98QIeew76AIuqWTImPwe4cupCrbIZCEa9DpqgFk9t1gTkGxYvFSqVf7FKvwo39PuTn58h7DqQ4nzp0ZzEEFE5tbL_iqxLp2EJv76sadlFQ2kIXEEaPR2WjQ7kQnylgXHiNDiN2XKZBYTWDvzS0X9RAWg-tTUuV7a4nLPbySVyrtYRADbXP6g8eJibKvIl4dUjIts9x4aSFt7lchP1gjpqHIqFp3Vt0cMWHuN_5WVASwKHcqK7WhlUs93ittqvYgW_n87qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0214da517f.mp4?token=g4OiLDJslw_z6Jh563mniWL6Y2jVGZrkNeKJGocK96RPjJFW6wQBdoh5sQhkuwgvi_hpZbBhq1vWHIFccqece32BoV3CUjldGOlGYtYDQp2Z2R5JcXbbIDF5bI4C2XZWUbf7UycrQsPSFA49b-9oc1FGQdgztW5elTnX6Yd8eXOHKeBRhgAjWMb6MfBvYmRlNQGC3R-Ny2mGAtw_SDmusiklwEoVG32aufw442qBQMZw5tBOycba49GuFyR8hl6AiGqQA9UGyy2_OFqr6u-GDL8WuICFpDagFdc-UTp8ClHYENTa2mBNYVluzxXol5zPklTk-x4vx_yfSBsS_8OY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0214da517f.mp4?token=g4OiLDJslw_z6Jh563mniWL6Y2jVGZrkNeKJGocK96RPjJFW6wQBdoh5sQhkuwgvi_hpZbBhq1vWHIFccqece32BoV3CUjldGOlGYtYDQp2Z2R5JcXbbIDF5bI4C2XZWUbf7UycrQsPSFA49b-9oc1FGQdgztW5elTnX6Yd8eXOHKeBRhgAjWMb6MfBvYmRlNQGC3R-Ny2mGAtw_SDmusiklwEoVG32aufw442qBQMZw5tBOycba49GuFyR8hl6AiGqQA9UGyy2_OFqr6u-GDL8WuICFpDagFdc-UTp8ClHYENTa2mBNYVluzxXol5zPklTk-x4vx_yfSBsS_8OY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظر می‌رسد نیروهای انصارالله موفق شده‌اند کنترل منطقه «البرقانی» در شمال «الصفیه» و در محور جنوبی تعز را به دست بگیرند.
در ویدئویی که منتشر شده، نیروهای حوثی هنگام ورود به خانه «سلطان البرکانی»، رئیس پارلمان شورای رهبری ریاست‌جمهوری یمن (PLC)، و تصرف آن دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72727" target="_blank">📅 17:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72726">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=RA0GFBiKm1R5n6Jv096LESY0XC71hFcWh2OXvptBlB9AU-K2D_d2_qH5Y3b9EW-uk7NFCSBPr5sWe-peKCnIQMUWucJNE32Yv44jmx2GjpSAy457pBaZxEGOecQ5_c4hvGMEYpQPJ-XTk_-4SF9XoOliRXBquEkJh8FSTXATM7AtZhh-sv6DUn-LoPKBA5ilvm6JX-upLgA72KUtJaFv87G15aUxj1AljDsilXtP5eosWhODQxNJcRMuMoSDsXgPy5GoUW_aiNk-66EeSFDdTJao75kjRiMCP7kNYfD9dwFCjyFEOEHsXNJws-_SNFuwiqWYRcpxvyhVpqJIbM4d1iu-1Q1SEWn3qsYBXrm6dJso5yQudljS6qk-UJJWzGg2auTta9-2wixwLTU_zmPh0lAq0WUIideMFQzZjxjMnQ3sjNMulWCyznfOVmQsh49ubIq01uQgHb9xrCXa1c-WDZ0vYwxvmpxxyn0n14EHIoLWfb5t5s9tGa9sbXunEA84uLgXY35Av931G7_r0nqOZHxR89bZ4tRf1DKX9C--pL_dAU82ZsvZsLizFdLZBHDIVNE3z0tIHXq2Vw0FflMrdmdnz7gY8rUnPbPPp6r9wMOqD98CLACqycrEADoYU7LHFjsgfLEuXPcakBxZqhZiQlHXQaUaNEegsM9Ry4_nqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=RA0GFBiKm1R5n6Jv096LESY0XC71hFcWh2OXvptBlB9AU-K2D_d2_qH5Y3b9EW-uk7NFCSBPr5sWe-peKCnIQMUWucJNE32Yv44jmx2GjpSAy457pBaZxEGOecQ5_c4hvGMEYpQPJ-XTk_-4SF9XoOliRXBquEkJh8FSTXATM7AtZhh-sv6DUn-LoPKBA5ilvm6JX-upLgA72KUtJaFv87G15aUxj1AljDsilXtP5eosWhODQxNJcRMuMoSDsXgPy5GoUW_aiNk-66EeSFDdTJao75kjRiMCP7kNYfD9dwFCjyFEOEHsXNJws-_SNFuwiqWYRcpxvyhVpqJIbM4d1iu-1Q1SEWn3qsYBXrm6dJso5yQudljS6qk-UJJWzGg2auTta9-2wixwLTU_zmPh0lAq0WUIideMFQzZjxjMnQ3sjNMulWCyznfOVmQsh49ubIq01uQgHb9xrCXa1c-WDZ0vYwxvmpxxyn0n14EHIoLWfb5t5s9tGa9sbXunEA84uLgXY35Av931G7_r0nqOZHxR89bZ4tRf1DKX9C--pL_dAU82ZsvZsLizFdLZBHDIVNE3z0tIHXq2Vw0FflMrdmdnz7gY8rUnPbPPp6r9wMOqD98CLACqycrEADoYU7LHFjsgfLEuXPcakBxZqhZiQlHXQaUaNEegsM9Ry4_nqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛رشاد العلیمی، رئیس «شورای رهبری ریاست‌جمهوری» (PLC) یمن که مورد حمایت عربستان سعودی است، از آغاز عملیات نظامی تمام‌عیار در تمامی جبهه‌ها برای بازپس‌گیری مناطق تحت کنترل حوثی‌ها (انصارالله) و احیای حاکمیت این شورا در سراسر کشور خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72726" target="_blank">📅 17:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72725">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=dSKijXYBdh_L-nvdaCfNu8jkQGPKLi_GJJR3dxeVVQQK7C3VlPYEaos6Hl4fpomGEFlbjZjuAvhu2OgwpqXTV_vQFUspDOeBTeMNUgySUgSf80JBFLLUmX1oB9Hrg2EDSCHCG6e9KB2JkRucM_Wk1mvIp2H5ZmdmGhjCCXZHffJw_OV_T7IFsWcbGA3CNIUuRWG4Ik6b0dMI4MrbBceYVrLFzc6CCng1oz0q5AR8vE4Ve2XBuMcN6he0A1xcdQF_iUaqT6W5hkoUNzytHQybdkiR8NTxDdonSL0LpEZX8WHeWco-qE9xTvwrAsnPVqWR6mMwk8ZN52Y28P5q3-Z6_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=dSKijXYBdh_L-nvdaCfNu8jkQGPKLi_GJJR3dxeVVQQK7C3VlPYEaos6Hl4fpomGEFlbjZjuAvhu2OgwpqXTV_vQFUspDOeBTeMNUgySUgSf80JBFLLUmX1oB9Hrg2EDSCHCG6e9KB2JkRucM_Wk1mvIp2H5ZmdmGhjCCXZHffJw_OV_T7IFsWcbGA3CNIUuRWG4Ik6b0dMI4MrbBceYVrLFzc6CCng1oz0q5AR8vE4Ve2XBuMcN6he0A1xcdQF_iUaqT6W5hkoUNzytHQybdkiR8NTxDdonSL0LpEZX8WHeWco-qE9xTvwrAsnPVqWR6mMwk8ZN52Y28P5q3-Z6_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پای رپر ها هم به تجمعات شبانه باز شده:
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72725" target="_blank">📅 17:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72724">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=uY-3tprnI7JUBmcqCnEmoIRvnrhWR_GBSrhFd6vH8vUNxqlWLO7GgJLTxdJvQPQGrXkl_Cge9CLGz9B6K3kW6cDa73zVorKqdFRYTTCwithhdz-794qF8848Bzdcr72xpCKbuldL7zGrHatZ1hb-ztBn20R6taJ2-LXitgZJQJ5UwXUx8CZrF7Ie2faZqPxptURfyetHmqqXqkTMm9a-hYTics9S9tXLMa-ys8cLHFzKVE9xTMm0agJCASm_b3U_iBNXxVrBG0wVBc91O0KA-TJ_4P27KfuCKTbK1qkojunUMMZQ59psgHQULX0A5K8uIEeJ-bUEVybtXwxcLlZwmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=uY-3tprnI7JUBmcqCnEmoIRvnrhWR_GBSrhFd6vH8vUNxqlWLO7GgJLTxdJvQPQGrXkl_Cge9CLGz9B6K3kW6cDa73zVorKqdFRYTTCwithhdz-794qF8848Bzdcr72xpCKbuldL7zGrHatZ1hb-ztBn20R6taJ2-LXitgZJQJ5UwXUx8CZrF7Ie2faZqPxptURfyetHmqqXqkTMm9a-hYTics9S9tXLMa-ys8cLHFzKVE9xTMm0agJCASm_b3U_iBNXxVrBG0wVBc91O0KA-TJ_4P27KfuCKTbK1qkojunUMMZQ59psgHQULX0A5K8uIEeJ-bUEVybtXwxcLlZwmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زنه داشت از حس و حالِ ناراحت پسرش تو روز اول مهر فیلم می‌گرفت که یهو یه مرده اومد و این شاهکار رو گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72724" target="_blank">📅 16:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72723">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=fnY9zOGGkZf9830vlpLP5iUr78mWOhQ-6b8vAZUBrdDVeLkM_b-DiTF8fZdYZNDE6TiFvuOKYvx-z9srnpyAO7Q9DCopS7nQizWO6AKBXUvhRz_e-E8W38r4RqqC5Gfn5a8E0Z7Ql9B3GX1OMqaXXPcHa3P13ziipZWxZH84TQASSWQy7rlirt5KBFTF-oYvqchstBrs3fRsVbvJSIe25prpcJerERGFn5IK7bHByGDYMZ5JSjA5_y4d2Knevj16i4Emdr0ZobZ7onOSVd82gW-TWu2tVxDjAMBJy3ALdys95mMyKNjgD8ibksQ9Y9LMLJ59DpcDgBfxPxt8bzP1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=fnY9zOGGkZf9830vlpLP5iUr78mWOhQ-6b8vAZUBrdDVeLkM_b-DiTF8fZdYZNDE6TiFvuOKYvx-z9srnpyAO7Q9DCopS7nQizWO6AKBXUvhRz_e-E8W38r4RqqC5Gfn5a8E0Z7Ql9B3GX1OMqaXXPcHa3P13ziipZWxZH84TQASSWQy7rlirt5KBFTF-oYvqchstBrs3fRsVbvJSIe25prpcJerERGFn5IK7bHByGDYMZ5JSjA5_y4d2Knevj16i4Emdr0ZobZ7onOSVd82gW-TWu2tVxDjAMBJy3ALdys95mMyKNjgD8ibksQ9Y9LMLJ59DpcDgBfxPxt8bzP1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مکزیک  یه گزارشگر داشت از وضعیت خرابیِ کنار جاده گزارش تهیه میکرد که همون لحظه یه ماشین لیز میخوره و تصمیم میگیره گزارشگر و فیلمبردار رو با دیوار یکی کنه :
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72723" target="_blank">📅 15:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72722">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=FULAkLCUhMDIGOJXqoNXTEmABlDHsieOyyX0H4XTlCRnHs6YSNX01ZN0Ugrne2lWZnzlNFAWj9m8j442hXfV2WrpiawBWYCxl3786tMhdRqgLvYLvZOs0GVsInRpZmnIQLpSASMEEuPV1qAMVrehdSOZm7vhCPJBZD00476q39aabETZ5k-WtxIQuyY9_JsV-b1o8VAUh5emk8Sfr8KOBz2PMdS_to6oM7rTBh0QQ7Po1S2YoRiTV5ZuWs8mbB9-eU3I8LdPMpypZUSHimSD7jjla8QtxTLwoQ8WrHfYz3RxPOr1LanNyTWTil5guK4Gt-Y4Nw6OguEmfBV5LfRMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=FULAkLCUhMDIGOJXqoNXTEmABlDHsieOyyX0H4XTlCRnHs6YSNX01ZN0Ugrne2lWZnzlNFAWj9m8j442hXfV2WrpiawBWYCxl3786tMhdRqgLvYLvZOs0GVsInRpZmnIQLpSASMEEuPV1qAMVrehdSOZm7vhCPJBZD00476q39aabETZ5k-WtxIQuyY9_JsV-b1o8VAUh5emk8Sfr8KOBz2PMdS_to6oM7rTBh0QQ7Po1S2YoRiTV5ZuWs8mbB9-eU3I8LdPMpypZUSHimSD7jjla8QtxTLwoQ8WrHfYz3RxPOr1LanNyTWTil5guK4Gt-Y4Nw6OguEmfBV5LfRMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فریادهای مهدی کوچک‌زاده نماینده مجلس بر سر همتی رئیس بانک مرکزی؛
کوچک‌زاده:
مملکت را دارند به آمریکا میفروشند.
«به خدا اگر از جهنم به خاطر کوتاهی‌هایی که در حق شما مردم کردم نمی‌ترسیدم، امروز خودم را جلوی بانک مرکزی آتش می‌زدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72722" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72721">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26538e463.mp4?token=MolsRkj3v7pg0Mi8kVxtJHfkBvPi3aYvSnj1DYigUur3iKTlze-b9-CZY8JTlPfrVgmY5gxZZYTqRsEfPKQ0un_NORYFlR-WPbALjYV58obXcTrffkfhvYO2yZm-ayaqjU9CLlq1ApBGKen9Zk6quEDuMasbqRqWn4bjtxE-jlN5CkdbJ0D7pZh_E9VYyzXO0Fk38-2-NzFiBTN2ioWHC-Ax-MNe1yKGsuKa1fptuif-7SSSNvX_46A5wozDmXxOLaLi44H1_7B53RFJRn70c3MSFPhulFIubhPke1H4-3Xmhv6dsyQaZOdp_gnuOPV5jwVdITbAzHbqT8LE9fsoYAHHrIUWVMmKnswQSqp8LiuIgUDDnH-B8vEklUNvbvDRJJlUjLwx-f4mmMmD0UfLKkzbOAFBFq5SAURrDbQPC0sI8uEUtUR6kyH79afkSJmDMszi8ynE0CwKs1xDvtsD92WA9OyfqnfDBtkN4uN9NiCI7Iey7xRSPHXn-cEpJkIahFFdBGDBEPO8ETAn9jzg0kwqkApbY3rf8IvLG4ViDNktkdb13J6TRLw-RIJ6yxh17e_lD48aEMMF3dVcSduNyBh3dPAHYudPgwncjTol26t8oYYy2a-FZ4SZ6YUXdZwEl7ykRgPotKMvWkDFqDmrb4aE3PBy-RYP2tnMRBSHifU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26538e463.mp4?token=MolsRkj3v7pg0Mi8kVxtJHfkBvPi3aYvSnj1DYigUur3iKTlze-b9-CZY8JTlPfrVgmY5gxZZYTqRsEfPKQ0un_NORYFlR-WPbALjYV58obXcTrffkfhvYO2yZm-ayaqjU9CLlq1ApBGKen9Zk6quEDuMasbqRqWn4bjtxE-jlN5CkdbJ0D7pZh_E9VYyzXO0Fk38-2-NzFiBTN2ioWHC-Ax-MNe1yKGsuKa1fptuif-7SSSNvX_46A5wozDmXxOLaLi44H1_7B53RFJRn70c3MSFPhulFIubhPke1H4-3Xmhv6dsyQaZOdp_gnuOPV5jwVdITbAzHbqT8LE9fsoYAHHrIUWVMmKnswQSqp8LiuIgUDDnH-B8vEklUNvbvDRJJlUjLwx-f4mmMmD0UfLKkzbOAFBFq5SAURrDbQPC0sI8uEUtUR6kyH79afkSJmDMszi8ynE0CwKs1xDvtsD92WA9OyfqnfDBtkN4uN9NiCI7Iey7xRSPHXn-cEpJkIahFFdBGDBEPO8ETAn9jzg0kwqkApbY3rf8IvLG4ViDNktkdb13J6TRLw-RIJ6yxh17e_lD48aEMMF3dVcSduNyBh3dPAHYudPgwncjTol26t8oYYy2a-FZ4SZ6YUXdZwEl7ykRgPotKMvWkDFqDmrb4aE3PBy-RYP2tnMRBSHifU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
من با کیم جونگ‌اون، رهبر کره شمالی، رابطه بسیار خوبی دارم.
وقتی طرف مقابل ۱۱۲ موشک هسته‌ای در اختیار دارد، خوب است که با هم کنار بیاییم.
اما تفاوت اینجاست: ایران هرگز موشک هسته‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72721" target="_blank">📅 14:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72720">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=CW-RmmqPxbb6b3Hc-N1NyKPdh59uzJgvWtfhvb57W-sUMBcBZ3If9rePAk5ZDKnjqRWKSq4VspBjBHFmki_Wj9LcyHmm4sLl5br316NSM4Ck_4Ae719X4x7tr8EzzkFL0uJYZNxLVA6C0ZmngZoe2wLr6D1MYM7g-LfgmEkTFyiwqMLNcDNUMvPejDcdIt5Q_7r3Kw9nd68GWsQCbFSShB-u9iNh5mkIIz_lhz69AX7JETtaxKDLZdxbhWYH7vibhSHyOLR7KGfPh_ltOpnD6v84T8ec4pRAovHKEhCpkdS7-guWnd62gPj4Ws60JUpKCbW1NPeJiKrTt6ePWBOdpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=CW-RmmqPxbb6b3Hc-N1NyKPdh59uzJgvWtfhvb57W-sUMBcBZ3If9rePAk5ZDKnjqRWKSq4VspBjBHFmki_Wj9LcyHmm4sLl5br316NSM4Ck_4Ae719X4x7tr8EzzkFL0uJYZNxLVA6C0ZmngZoe2wLr6D1MYM7g-LfgmEkTFyiwqMLNcDNUMvPejDcdIt5Q_7r3Kw9nd68GWsQCbFSShB-u9iNh5mkIIz_lhz69AX7JETtaxKDLZdxbhWYH7vibhSHyOLR7KGfPh_ltOpnD6v84T8ec4pRAovHKEhCpkdS7-guWnd62gPj4Ws60JUpKCbW1NPeJiKrTt6ePWBOdpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی :
بحث‌ها پیرامون خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) در محافل سیاسی ایران بسیار جدی است و وزارت امور خارجه به تصمیم مراجع ذی‌صلاح پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72720" target="_blank">📅 14:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72719">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=pSGY8VwZxR9-GroUZ4kTxk-KkFHiQh-iFZL-aNnl21J5HWQWmvyM1Z61gPm777GDwkNQe-gnGQ3jzJyldsMHlaxMAZn4JgNwtOPdmhkYfGIgkjUtQNzl1WeJVf1S-s7YLv6Yr1920zAvceTzELi7WiIhtFLy1fwJr3IrR8lwSjc1n2dswJjMzgt5zF8dItapTI3QekSxS0HxGwcWNxgPAIa3BGsnzKeSD9JAtSWV1ZnvWxS88ykJBCG2ZzC_XGP9BDhFArEU_13fPZjpasEXuFNpv58JpDOqObuEdbqR3SArRQOLA0UR8BINoN7C7ElvhenOx8iL2JYfWQk2wmFgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=pSGY8VwZxR9-GroUZ4kTxk-KkFHiQh-iFZL-aNnl21J5HWQWmvyM1Z61gPm777GDwkNQe-gnGQ3jzJyldsMHlaxMAZn4JgNwtOPdmhkYfGIgkjUtQNzl1WeJVf1S-s7YLv6Yr1920zAvceTzELi7WiIhtFLy1fwJr3IrR8lwSjc1n2dswJjMzgt5zF8dItapTI3QekSxS0HxGwcWNxgPAIa3BGsnzKeSD9JAtSWV1ZnvWxS88ykJBCG2ZzC_XGP9BDhFArEU_13fPZjpasEXuFNpv58JpDOqObuEdbqR3SArRQOLA0UR8BINoN7C7ElvhenOx8iL2JYfWQk2wmFgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکشنبه ۱۲مهرماه۱۴۰۵؛آتش‌سوزی در پاساژ خلیج‌فارس عسلویه به دلایلی نامعلوم:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72719" target="_blank">📅 14:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72718">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDesa5_kt6wJV_MUzPI7MhdjpBktGmdgvvPBRu3Qr2o1MdablP5tn0vdlB1AXTYEakF_hKt2RskZSny1i9DXOoD4TP4E4MfZ--CN4aieSelRHiRZaQ2WvDKo78l6eHEqbcJj0HxAFeFS7ygr1EBmF8SmU8G6xyHruVggjE6Y6IVn85p458DM17PoElGlA-OjKRHmPzcr4RD_XCdwQ-yUQ1mMEEkRUtFj6B-1jUAOR3hS34YFhQQZw8vCexfDCTZetR-GCHixuujK1RtAoJhXAzgtqTbGPpLXHlj-3g6fsBTVuCg0VgUnaIdGwN2zL-rP8-jHlQ9uxJtVzv6tQirSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران _ نجف که قبل از محاصره هوایی حوالی ۱۲ تا ۱۹میلیون تومان بود ، دوباره برقرار شده اما بیش از دوبرابر رفته رو قیمت و شده ۳۰ تا ۳۸ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72718" target="_blank">📅 13:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72717">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=BDdjLjuFIP__runP94ZVL78lEFRxkqsb3t3KE4-DZOz-Pq9lWNJEeyLvS-btlH9iSHrDFtzz54C6-cX6ciHAMUPA5V0rVn6fEJXI92aT0VYI4Eq1tqIHdYeV8bZ4nhR7VYuJ-B6KcGg-vAY5iEOg4D8ICyRUR9ArSDqpuEvrVexyVPmAL-hBl-tFSNitgIu-n5TaueI8q6pqZ5uRuOZ35yak3DIF-vdaH_nOJIoS-IqS5JDLX6YSnoPaOYOA9xyA_aUO-fmOkkZL7hX4GaRyQIOfdlCez20ULzVHULGVrZDg2UQY2nYkIi22TErHvkCa1VS47O02H7qsffjdHeW7HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=BDdjLjuFIP__runP94ZVL78lEFRxkqsb3t3KE4-DZOz-Pq9lWNJEeyLvS-btlH9iSHrDFtzz54C6-cX6ciHAMUPA5V0rVn6fEJXI92aT0VYI4Eq1tqIHdYeV8bZ4nhR7VYuJ-B6KcGg-vAY5iEOg4D8ICyRUR9ArSDqpuEvrVexyVPmAL-hBl-tFSNitgIu-n5TaueI8q6pqZ5uRuOZ35yak3DIF-vdaH_nOJIoS-IqS5JDLX6YSnoPaOYOA9xyA_aUO-fmOkkZL7hX4GaRyQIOfdlCez20ULzVHULGVrZDg2UQY2nYkIi22TErHvkCa1VS47O02H7qsffjdHeW7HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش روسیه به پل شمالی در کی‌یف حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72717" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72716">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=oPQRo0Zu4K6kQm_n7l5nlyNUuHMrB6KcVlZcdjRJ7hNInPNXS71WqQuOgAnNjqbuAVNo_zsDvDrclDLa2mUjrsmnu5LsiNdf78B2S-fOMx3Xt2D9YxNLWD5l2NTfTafG0hMtOCwqDq1kXb8beitfIsULgczLKM5skfxFecfD2YDz43P0B4UhqIjy8vQo0kU4fetLHHL9U3ebDtSKuaR5kY8dJCFfGt70gUewriHcddyPWRNewjEm6pYfQydK_mJ5jeIbuqT4vJ8bqSSdM39yQyg_SyQxoviz9mg5dRWaTh-OPFMWL7cTx5P7sm7OQ8dRof8Wpozb4yO_y0P1qewsEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=oPQRo0Zu4K6kQm_n7l5nlyNUuHMrB6KcVlZcdjRJ7hNInPNXS71WqQuOgAnNjqbuAVNo_zsDvDrclDLa2mUjrsmnu5LsiNdf78B2S-fOMx3Xt2D9YxNLWD5l2NTfTafG0hMtOCwqDq1kXb8beitfIsULgczLKM5skfxFecfD2YDz43P0B4UhqIjy8vQo0kU4fetLHHL9U3ebDtSKuaR5kY8dJCFfGt70gUewriHcddyPWRNewjEm6pYfQydK_mJ5jeIbuqT4vJ8bqSSdM39yQyg_SyQxoviz9mg5dRWaTh-OPFMWL7cTx5P7sm7OQ8dRof8Wpozb4yO_y0P1qewsEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حرکتی شاهکار نگهبانای ی شرکت رفتن با سلاح برنو بالن هواشناسی رو زدن و بعد زنگ زدن به سپاه گفتن پهپاد آمریکایی رو زدیم بیاید همین الان جایزمونو بدید
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72716" target="_blank">📅 12:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72715">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دلار ۲۷۱.۰۰۰تومان
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72715" target="_blank">📅 12:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72714">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da8647691.mp4?token=V5w6y75awvR-7OU7jHA63wfRwJxhkeEqClt9QmHCxyq8QlyxzEKPDu067oOPkjxWblcIII3ofgDa-l8XEIX84Kpe0zhh0jcmXpl7Svk83DXixhYItQ7YMobBp7qoXmTl6NT_ou0nbqZN2kjfibp5qIa6eYa6hCR5CQeVOfUJtw291fke7LljW1T7Hq1RLkXCoN3PQ5QgSd65EDPpMZ5H36XX15fNzEFZBYU2MJfrz6q_BcHXY7CxUyZibe9RxyUhMRKPDIO4vzhxPF9aRg_0ePoTM1w5nte-PYIShPpBeFc7WVZQpylbnVEGRi4Q9TBh8PcIZ_kguZr73My_vaHmSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da8647691.mp4?token=V5w6y75awvR-7OU7jHA63wfRwJxhkeEqClt9QmHCxyq8QlyxzEKPDu067oOPkjxWblcIII3ofgDa-l8XEIX84Kpe0zhh0jcmXpl7Svk83DXixhYItQ7YMobBp7qoXmTl6NT_ou0nbqZN2kjfibp5qIa6eYa6hCR5CQeVOfUJtw291fke7LljW1T7Hq1RLkXCoN3PQ5QgSd65EDPpMZ5H36XX15fNzEFZBYU2MJfrz6q_BcHXY7CxUyZibe9RxyUhMRKPDIO4vzhxPF9aRg_0ePoTM1w5nte-PYIShPpBeFc7WVZQpylbnVEGRi4Q9TBh8PcIZ_kguZr73My_vaHmSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت بر سر قبر علی خامنه‌ای، علیه مسئولان نظام شعاردادند؛
«گرانی رو آوردن، سازش کنن با دشمن»
«مفسد اقتصادی، سرباز آمریکایی»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72714" target="_blank">📅 11:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72713">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsV8D88Ks5pziMGNX4DpqOlrkokq8uKYxnT_qeGaeQmVj9zyprkX6hnsD-kJFvvnU2fO4rHC80u4vWr2Xl4vaXNn_9lkrWbQO2ujzhSE-599JmZgl4_ChQ95mebYXyNyc7pjLT1QdfWKjy4vwhhtcXrnCYC1X-4RvJyomwCzOG7f8_q_I1Y1EkVpX0wnwYOn4aX9MaPifaIqe4TQTWOoDBDoj7LcWUg-Xuw1GeSNt9yOUO1Pj4yLEFMEkM-rXFnUzsdQRx7ccrNek3hGjDnwbl7l9T4qRLlRMGQynwhIOFsCC9CuNcFfIsTuqrQWg6_J36veFgVyTMm57LwQaopI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72713" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72712">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72712" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72711">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkhYQn94lOvssFptX8FxG8P1-G1Aex0zMC-e0R1MlIInhKn97Fioe3Fwfip33xn9BDhn_OfBZvAWPQf88-DuhLo3YqJpgEyfza9z-8sOhkgII_lSDKZYLFI3-zjJxwsUlOB5YKXXQcRKDLATsr8Lspw0cIABG39-HYexGDyoTSa8xfWbPyNHLxuSYMEiLcFAMyRo_qiY4vxLl-ELzeV4MGh8WCvc69dctWnqWz1HKfWpaynWbIeuyOEpZugKXhrUS7sGEtJPUaIAmx6xuZcqCaYPfHLufJeGHu0DdqC3C-Xfb76VkdfYGpbHUfXzslTnM0cMsSYmo33mTlMzLjQynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
یونان
صربستان
🆚
هلند
نروژ
🆚
پرتغال
دانمارک
🆚
ولز
آفریقای جنوبی
🆚
مصر
مالی
🆚
مراکش
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72711" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72710">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=E6GXW3nmyeqA4WWQ0umSal1jdAX2ufnjeZxnKKK88Yy27EFxZhlefWZ_WatrhkKh9cqQl5tLlQCNg2xY4a3rqYroeVKfThsujmknuPWp03okrVGLJ6pGZ02ujVIslVzecQeyZtqdmX6GMHGPhuvzXt7mkn_APsWcCjPKSx6dleBrYuTwcoYX7kCwdB01Fz7EhXjVSXz4OeSYrF9GRmBbyInoeJRaoaSq5B-qdX_MegdLMv-kkqtSK2YFo-_1ry5s_7dRKf0C2edK1GwxjFen6wVc3hnbVRyQrk2DVRe0Xm74nc0BHukaanVvD0VkuEeKJzTtSkcgR8YN1ZZBdlNwHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=E6GXW3nmyeqA4WWQ0umSal1jdAX2ufnjeZxnKKK88Yy27EFxZhlefWZ_WatrhkKh9cqQl5tLlQCNg2xY4a3rqYroeVKfThsujmknuPWp03okrVGLJ6pGZ02ujVIslVzecQeyZtqdmX6GMHGPhuvzXt7mkn_APsWcCjPKSx6dleBrYuTwcoYX7kCwdB01Fz7EhXjVSXz4OeSYrF9GRmBbyInoeJRaoaSq5B-qdX_MegdLMv-kkqtSK2YFo-_1ry5s_7dRKf0C2edK1GwxjFen6wVc3hnbVRyQrk2DVRe0Xm74nc0BHukaanVvD0VkuEeKJzTtSkcgR8YN1ZZBdlNwHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابایی، رئیس کمیسیون اجتماعی مجلس:
می‌خوایم حقوقِ کارمندان دولت رو 5 الی 10 میلیون تومن افزایش بدیم!
قراره «فوق‌العاده خاص کارکنان» تو کوتاه‌ترین زمان ممکن و با امتیاز 2 هزار تا 20 هزار واسه کارمندان اجرا بشه.
این افزایش از اول شهریور محاسبه میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72710" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72709">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=EOK-_bWB9gypjB5QPj2f4fyR82yYcwRAoEbuCEDwmlpKPYltV9pCO_OITNObyW-9_aqeh8xZNTrfXUnp0_dxgtyyH8TpDbEzYpIwj0ERbIzWz-cbVf-Q95fWPC9mOvIrkKnM5U8P3eSAW_rfUlFXPYyAcWwAFy2XRGB1XXaifa4LCOaAz-6kV_8aGRGkSjmt4eB0h6xWHZC9Q2aLKw2sOZAUUR1PMDqaZWLao1fXjKVSZHE8zF9dn221HlQW68XJDDP-aPnusbzHOHmjrRpB6BfilEsX377sGYgGpam1Oc_XkggABGBKBJD57EuRpc4EQyoH943kd8WiAYrCLHG1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=EOK-_bWB9gypjB5QPj2f4fyR82yYcwRAoEbuCEDwmlpKPYltV9pCO_OITNObyW-9_aqeh8xZNTrfXUnp0_dxgtyyH8TpDbEzYpIwj0ERbIzWz-cbVf-Q95fWPC9mOvIrkKnM5U8P3eSAW_rfUlFXPYyAcWwAFy2XRGB1XXaifa4LCOaAz-6kV_8aGRGkSjmt4eB0h6xWHZC9Q2aLKw2sOZAUUR1PMDqaZWLao1fXjKVSZHE8zF9dn221HlQW68XJDDP-aPnusbzHOHmjrRpB6BfilEsX377sGYgGpam1Oc_XkggABGBKBJD57EuRpc4EQyoH943kd8WiAYrCLHG1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانوم 15 ساله به‌خاطر اینکه هر هفته پریود میشده به دکتر مراجعه میکنه تا بفهمه مشکلش چیه؛
بعد از اینکه معاینه میشه، دکترا متوجه میشن ایشون دو تا دهانه رحم و دو تا سوراخ واژن داره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72709" target="_blank">📅 11:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72708">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=BxDZLUxGTLcHgdUYrG-NnpcJN1mos_dE4WMRLIQFtvMHjZnVOLnr1-Y2cHM70FdNuWT7o0HkwHEg2OI8BAe0L0EYq8BfbxGndbN0SHPZP2ENYIegarANKhkn2PsfvT3fZ1K6s_c0i39nWUB9lOOu4rQgydPLhOp3RUYVVZUIzudkC3vJM8iri3ODMMyoFQDz4ZmChgJxoDbVDBcMTDVVy-w8KJbOm0d5svkJivjqi2VfeisnStYFOoWjGdoMrqZ9NCeCpLeid-rqMONTLQPdTzsejkQ0gzeSCoJMip7z9lmGpDKNR2y0KGhuQlw2xpd9k-gLwUGd-RG0WCOWj7Z1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=BxDZLUxGTLcHgdUYrG-NnpcJN1mos_dE4WMRLIQFtvMHjZnVOLnr1-Y2cHM70FdNuWT7o0HkwHEg2OI8BAe0L0EYq8BfbxGndbN0SHPZP2ENYIegarANKhkn2PsfvT3fZ1K6s_c0i39nWUB9lOOu4rQgydPLhOp3RUYVVZUIzudkC3vJM8iri3ODMMyoFQDz4ZmChgJxoDbVDBcMTDVVy-w8KJbOm0d5svkJivjqi2VfeisnStYFOoWjGdoMrqZ9NCeCpLeid-rqMONTLQPdTzsejkQ0gzeSCoJMip7z9lmGpDKNR2y0KGhuQlw2xpd9k-gLwUGd-RG0WCOWj7Z1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:‌ حتی اگر بمب اتم بخوریم باز هم نابود نمی‌شویم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72708" target="_blank">📅 10:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72707">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=NWOJYNkvWQUIX7dYY-A03ke6rQF0gwczktsqpvTOXIYcV-prejc5Wmx_R-4ZENDEFt1iu7SuJUBBjkeofGx07nWkVQwt5mawTEw05xrrcGEBvdNMcUPs9k08UFhY-YUNSjoiwmlbjY_kurSmA3QhIc5ZuSBYQ1lKlKxREhFtMlI-9pMm-zPaU9mohsSmY5n_PlBfxL2q-cwVsxgnGGIRmqLEi20s5qtSs2ntge7ef-y9LGS0XivSDKr8wOOqcpMMx6Oahhh-Xisf8FKp0Nv9zGLFPY7vekiCCxRXJUy7Hxe0xVYoT384xZKY4BM-i3dBJ_MLBJRekpTP7LjjwOTuuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=NWOJYNkvWQUIX7dYY-A03ke6rQF0gwczktsqpvTOXIYcV-prejc5Wmx_R-4ZENDEFt1iu7SuJUBBjkeofGx07nWkVQwt5mawTEw05xrrcGEBvdNMcUPs9k08UFhY-YUNSjoiwmlbjY_kurSmA3QhIc5ZuSBYQ1lKlKxREhFtMlI-9pMm-zPaU9mohsSmY5n_PlBfxL2q-cwVsxgnGGIRmqLEi20s5qtSs2ntge7ef-y9LGS0XivSDKr8wOOqcpMMx6Oahhh-Xisf8FKp0Nv9zGLFPY7vekiCCxRXJUy7Hxe0xVYoT384xZKY4BM-i3dBJ_MLBJRekpTP7LjjwOTuuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه این مدرسه اس
پس ما کجا میرفتیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72707" target="_blank">📅 10:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72706">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8589525917.mp4?token=LZYk9cJzDRIpF2mxYOY0A-bQJ2V6Z8t2GRwcc0sZoml-K-Q1gFKVqNvoTfaMIHbwqu_OmMtXvaVujo1hk1f3DFApalz2Zb_CtUTxFtoGhd_XmgldLvhUmKFsJadCU4tnOizMgxLgsVBK7Nd1x5WstYZpDZThHz0t2jiIiygxQ9Imn2P2Xsb-oC4fZgdOePo7C6T5nIdf_DpyQ5pSLwmpaBjyZit6DB_ZXAvIJJY87bhbiNXaVwuDe4fyzKLfk-HDITkU3pV-8VcysH-kIppPYHLZOruXTrWUjfNGXb8DzleOYWImWixMj8pDwtDk35pLoD05efrpXgjNw3zm7KVYwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8589525917.mp4?token=LZYk9cJzDRIpF2mxYOY0A-bQJ2V6Z8t2GRwcc0sZoml-K-Q1gFKVqNvoTfaMIHbwqu_OmMtXvaVujo1hk1f3DFApalz2Zb_CtUTxFtoGhd_XmgldLvhUmKFsJadCU4tnOizMgxLgsVBK7Nd1x5WstYZpDZThHz0t2jiIiygxQ9Imn2P2Xsb-oC4fZgdOePo7C6T5nIdf_DpyQ5pSLwmpaBjyZit6DB_ZXAvIJJY87bhbiNXaVwuDe4fyzKLfk-HDITkU3pV-8VcysH-kIppPYHLZOruXTrWUjfNGXb8DzleOYWImWixMj8pDwtDk35pLoD05efrpXgjNw3zm7KVYwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش‌هایی از کرج، از جمله باغستان و جهانشهر، روز شنبه ۱۱ مهرماه ۱۴۰۵، پس از بارش شدید باران سیل جاری شد و خسارات نسبتا زیادی به شهروندان وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72706" target="_blank">📅 09:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72705">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=dUcBsLuAhkzsxazICZWN0M-NYXJs285V18pq2jG4o8KeIAJM-KyCly7TGK0TDLlq33O7JFnrxW5o3bRleRgkMbjYzAx7mtDh4dQfH59otktlr3UM8bJZw9hzHVOGbQbg5le3NM7RVoZhz6TMYpVdJv3hWkbAjf6CQ9inxUx-BnbbyGDstA386I-4zqDbpvG_V1yaOycy3vr-vhOjFpTi0geDU43DciFnFxQ56q-hRTWYa1l00-jDmCkxVuMoQHEEBCdg0XHBF84DQLr1nhQauMWnoz1q_B8n97IwdBO8tDpAyQvdQ9hQ-K0EBzwatW4CJtBWSEmF1Da6ip-yTB_uKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=dUcBsLuAhkzsxazICZWN0M-NYXJs285V18pq2jG4o8KeIAJM-KyCly7TGK0TDLlq33O7JFnrxW5o3bRleRgkMbjYzAx7mtDh4dQfH59otktlr3UM8bJZw9hzHVOGbQbg5le3NM7RVoZhz6TMYpVdJv3hWkbAjf6CQ9inxUx-BnbbyGDstA386I-4zqDbpvG_V1yaOycy3vr-vhOjFpTi0geDU43DciFnFxQ56q-hRTWYa1l00-jDmCkxVuMoQHEEBCdg0XHBF84DQLr1nhQauMWnoz1q_B8n97IwdBO8tDpAyQvdQ9hQ-K0EBzwatW4CJtBWSEmF1Da6ip-yTB_uKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خراتیان، کارشناس صداوسیما: چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است!
مجری صداوسیما: چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید و بعد به سراغ ما بیایید
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72705" target="_blank">📅 09:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72704">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72704" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72703">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBzE0mfxLSq-nTNRTSaH_uF4YJFpJvzH3sZCCjIDhNWTQEwvCqOToag7zSZ3aLZsGapY_JdWvSU6c2GopvFfzBgvF3JlHD6YJraFFb8Ov4TVYdBwR_VQv3CezjscMeTubEZCH65_QiDA7-N2fxAl3GBKRELeuhobw83UdRan_r6GR80WqrO-LTsRCZ8hpnnzgR3ngfN3bca_UB-9kYK7lzmUI_9pAXy1gAAZIUcAupf6zmK8pMbB9Fineiqtg0y11yYJTk13eF3dtPyscTYm74DEgZZnrMt4TEX6ZQI78pgIncUMWPRk298hECf9YaxTM5py-UzZ6e_u3A5hrqGpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72703" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72702">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2d851559.mp4?token=Qkf2igdCOAn-1QuMLtGFjYO_r8x0LuAW5QgMKgthnE35Dwe11gXL_0WkOkr71IcAyhkGaN4gGN-1tvnV0wShYzGmskbflkzoHACtd2IkTp0wmWfWYuNd7ZtdbWIJVKAE7d5vJnlDRc332V9JQ0Gd9m6SJiXNb_uSlr9zhkqBf1RYiPlvRRJlCYm_QZCFub74yxuX0rN7Zmrs37IcPov6Pwt9y9ogO9BN8tXGH0ZStU45sd60eXoXM2c3D74kKg5a8UZOUk7ChTP9KLt9_C4a1dh5MOSg-G2l6QUyCgtY44vIYafX9iCE9-cpTHf2sV3XPi4MaT7Yr47v17XRNEtwn2VlRshfs8-YQ4USHKUPSlxQakvBHHWj5eWcAPtqRj3tXjsmt1x9A7yZcJq5OC-bg8Ki3M-5zT4wI3EcfHLK3FzGyg-xCS6HBJ-hhDuyq2xHRYFqTmZ9KLOtfWOJKV6iun01ZRuN-mGl1ITHEWUqELf4L3kuTsQwCS65TDDC3OsItyaEV1T9v1UzSYsRl6q4WZnFIqFsfSU5fnoTS_bxg8ru6Nfhkussc20_poFE7Ddvw5nn78gRMGEDAt5-ftfEoJzfJxILjc7Fy2o4xFHJfUkT8WfHZgWXqMwpeD4gqSzN6P2L68WbpR5keqN0dSIIaTih77Cr7BlAHyFXBRT13lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2d851559.mp4?token=Qkf2igdCOAn-1QuMLtGFjYO_r8x0LuAW5QgMKgthnE35Dwe11gXL_0WkOkr71IcAyhkGaN4gGN-1tvnV0wShYzGmskbflkzoHACtd2IkTp0wmWfWYuNd7ZtdbWIJVKAE7d5vJnlDRc332V9JQ0Gd9m6SJiXNb_uSlr9zhkqBf1RYiPlvRRJlCYm_QZCFub74yxuX0rN7Zmrs37IcPov6Pwt9y9ogO9BN8tXGH0ZStU45sd60eXoXM2c3D74kKg5a8UZOUk7ChTP9KLt9_C4a1dh5MOSg-G2l6QUyCgtY44vIYafX9iCE9-cpTHf2sV3XPi4MaT7Yr47v17XRNEtwn2VlRshfs8-YQ4USHKUPSlxQakvBHHWj5eWcAPtqRj3tXjsmt1x9A7yZcJq5OC-bg8Ki3M-5zT4wI3EcfHLK3FzGyg-xCS6HBJ-hhDuyq2xHRYFqTmZ9KLOtfWOJKV6iun01ZRuN-mGl1ITHEWUqELf4L3kuTsQwCS65TDDC3OsItyaEV1T9v1UzSYsRl6q4WZnFIqFsfSU5fnoTS_bxg8ru6Nfhkussc20_poFE7Ddvw5nn78gRMGEDAt5-ftfEoJzfJxILjc7Fy2o4xFHJfUkT8WfHZgWXqMwpeD4gqSzN6P2L68WbpR5keqN0dSIIaTih77Cr7BlAHyFXBRT13lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفنگداران دریایی ایالات متحده در حال سوخت‌رسانی به یک فروند هواگرد «ام‌وی-۲۲ آسپری» (MV-22 Osprey) در خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72702" target="_blank">📅 01:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72701">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=D56aGAwo1lYZJCTjtMySVgn3pSKD_SxzRHX6I2tCYvo7hoquAyr84VjZR78HbONiNlfLAOoteGIB6jNKgGTTokfo7i_Fq1RFA5JvG2hWRrzvaGTUcxvcyRtMeugwRK3GLPwBWB5X0OkWpCC86PKly-gMdcKxufN2QsDQXYzYrics5Qb1_fkS7JFbkvKEzD8hQ2gAw4FBwCr86xa0-3rjxnMJjndv_rOhKFygOQ-nJarPSZeE6QhFDnb1BGUc7HYmq5qygiskEqLQJnMrDBIBKd-m3OFUX5OvtezbRTxbY4Gr86Pk6dansswyLcG_qXP0jNOaoNtGtF26ACinw09iBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=D56aGAwo1lYZJCTjtMySVgn3pSKD_SxzRHX6I2tCYvo7hoquAyr84VjZR78HbONiNlfLAOoteGIB6jNKgGTTokfo7i_Fq1RFA5JvG2hWRrzvaGTUcxvcyRtMeugwRK3GLPwBWB5X0OkWpCC86PKly-gMdcKxufN2QsDQXYzYrics5Qb1_fkS7JFbkvKEzD8hQ2gAw4FBwCr86xa0-3rjxnMJjndv_rOhKFygOQ-nJarPSZeE6QhFDnb1BGUc7HYmq5qygiskEqLQJnMrDBIBKd-m3OFUX5OvtezbRTxbY4Gr86Pk6dansswyLcG_qXP0jNOaoNtGtF26ACinw09iBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. البته، همان‌طور که می‌دانید، ایران عملاً از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72701" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72700">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=Te4B_NJrTe98ZQzx_7cF6e-_F3AfVhEY8badluxU-I--BPteeSe75Ymh0LdcysL_vsqGXm_16m6SlhzCd1RcFGWAkxgC2ijhLc4URQS14fN6QnB7AFiQRne18G9NtQGIG-Ws31Q53XBnn_FhJAHoBNawg2HvyokL9Ajf92yEKukUS8gH9M-eRcFx2wsK7qflaqNLtRs9h6E3YlqBkS7fCM01DgFgMnBUKin7xyjHN4U6Ky5SgkIVSQ3Bw4Vz7Q6eRpL43Dpl_--NtXpB8vxDmy_HmBWhSyBhDgItQHY_GuWFYobl38rfxywFdRpiQMhdx87Ar0d4dcAlvByREUisDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=Te4B_NJrTe98ZQzx_7cF6e-_F3AfVhEY8badluxU-I--BPteeSe75Ymh0LdcysL_vsqGXm_16m6SlhzCd1RcFGWAkxgC2ijhLc4URQS14fN6QnB7AFiQRne18G9NtQGIG-Ws31Q53XBnn_FhJAHoBNawg2HvyokL9Ajf92yEKukUS8gH9M-eRcFx2wsK7qflaqNLtRs9h6E3YlqBkS7fCM01DgFgMnBUKin7xyjHN4U6Ky5SgkIVSQ3Bw4Vz7Q6eRpL43Dpl_--NtXpB8vxDmy_HmBWhSyBhDgItQHY_GuWFYobl38rfxywFdRpiQMhdx87Ar0d4dcAlvByREUisDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ: تصمیمی درباره ایران دارم که باید بگیرم. کار را یا به روشی آسان پیش می‌بریم یا به روشی دشوار.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72700" target="_blank">📅 00:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72699">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=VSo5sCu-aACYIopjegTnzP8aZtcLgIKdNwJa097bnKATDRdMYXgzhB6O1TBdBa6tf0YweDBrWcLt3ZLKAeTZ1cQVawFal3wgozw1R-6LqX4x1KgZJrGd0i4B0MDpoWm8v7EU5OyY988m3TaWgapUc70uKjMJZvnhxftGwvDTF2GVexTv6tDbtXoYD-PvrDpkqWNtkuSmyafn9rrMFG07M2ueUsy4tScfQ_0b69RYjUVP7bzpv4kqiaRrwqwb6PaoA4DpQa0jBzHtOGzm6pxQhLM87kMfAzgVj6z2wFq6Th1kk4aW_is3GiYt48ySyI7B_tjz7A__m0Z9GnRyqVH0-EjsXdadG9q4nuk-1k74khOYls3Q3r2nPPtK5_CkF2ftUgOOtURKK0BxHAwc40hekVmt7WDai7hVzqhGA8iD6axPqR0D1w2QXZ0BJJtr_jhXKk-Pw0LbycHE_5qFe_4yz8UJ6U5Hclm_zT372bKApL8aeE_Wny4A58VfoXc_vEuHtqKDHIcRjZs8xY5zxEZBaG23fw3Ekq7G4SWzIMS6YLwDjRyNURfH8xLkxoDtr8LFKmiMpzYqZYZxFgT0JCS5Wm3poEi18xI0ptbecupV5dMCXnhryLOlQ0eIkGNZy3VTFx_U9jx_Y6p4_j7SUd-owsZYb1JGP_OrT4Vm_5FaiDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=VSo5sCu-aACYIopjegTnzP8aZtcLgIKdNwJa097bnKATDRdMYXgzhB6O1TBdBa6tf0YweDBrWcLt3ZLKAeTZ1cQVawFal3wgozw1R-6LqX4x1KgZJrGd0i4B0MDpoWm8v7EU5OyY988m3TaWgapUc70uKjMJZvnhxftGwvDTF2GVexTv6tDbtXoYD-PvrDpkqWNtkuSmyafn9rrMFG07M2ueUsy4tScfQ_0b69RYjUVP7bzpv4kqiaRrwqwb6PaoA4DpQa0jBzHtOGzm6pxQhLM87kMfAzgVj6z2wFq6Th1kk4aW_is3GiYt48ySyI7B_tjz7A__m0Z9GnRyqVH0-EjsXdadG9q4nuk-1k74khOYls3Q3r2nPPtK5_CkF2ftUgOOtURKK0BxHAwc40hekVmt7WDai7hVzqhGA8iD6axPqR0D1w2QXZ0BJJtr_jhXKk-Pw0LbycHE_5qFe_4yz8UJ6U5Hclm_zT372bKApL8aeE_Wny4A58VfoXc_vEuHtqKDHIcRjZs8xY5zxEZBaG23fw3Ekq7G4SWzIMS6YLwDjRyNURfH8xLkxoDtr8LFKmiMpzYqZYZxFgT0JCS5Wm3poEi18xI0ptbecupV5dMCXnhryLOlQ0eIkGNZy3VTFx_U9jx_Y6p4_j7SUd-owsZYb1JGP_OrT4Vm_5FaiDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، درباره ایران:
ما از همان ابتدا اعلام کرده‌ایم: ایران هرگز به بمب هسته‌ای دست نخواهد یافت؛ تمام. این موضوع، یک منافع حیاتی ملی برای ایالات متحده آمریکا محسوب می‌شود.
ما این مسئله را در جریان «عملیات پتک نیمه‌شب» (Midnight Hammer) به وضوح نشان دادیم و در «عملیات خشم عظیم» (Epic Fury) نیز آن را آشکار ساختیم.
ایران می‌خواهد با مسائلی همچون تنگه هرمز بازی درآورد؛ اما کنترل آن در دست آن‌ها نیست، بلکه در اختیار ماست.
آن‌ها عملاً هیچ چیزی به دست نیاورده‌اند؛ چرا که محاصره ما آهنین و نفوذناپذیر بوده است و ما هر شب تقریباً با همان ظرفیت‌های پیش از جنگ عمل می‌کنیم.
ما احساس می‌کنیم که در موضع بسیار قدرتمندی قرار داریم. ایران باید تصمیم درست را اتخاذ کند؛ در غیر این صورت، رئیس‌جمهور ترامپ تمامی گزینه‌های لازم را روی میز خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72699" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72698">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=UP-mVtuYMSsDQefhreBSf0SxxqVAAVxk_1WgBPqW-IShFY5cLQTC7Cr7ZrogeeuiVdPkVL60N5w-sm6p96cgDDSsG3-OHtNd-BJL8Zkw-b0fCXARsMlHvnoCB0hu81N9o5Mbaqi3aQLAMFJ0r2pg3Ph6pOzEl3mx1IHwA09hXtvt3JKncNacok57nQ1dMDVe7jojyME1sD3MwksmcJTxMDjTgYrjn6K_ZaOklM7cevgDbId49GvXwwNa3GY3CJXprfq7zyjjYRrr2p0stmKYU5RkIYmT2VhNiaSeV3PHbc91sV9OpXopd_0ENOjacua8YV5eg46_X1jMpMSMwsqEjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=UP-mVtuYMSsDQefhreBSf0SxxqVAAVxk_1WgBPqW-IShFY5cLQTC7Cr7ZrogeeuiVdPkVL60N5w-sm6p96cgDDSsG3-OHtNd-BJL8Zkw-b0fCXARsMlHvnoCB0hu81N9o5Mbaqi3aQLAMFJ0r2pg3Ph6pOzEl3mx1IHwA09hXtvt3JKncNacok57nQ1dMDVe7jojyME1sD3MwksmcJTxMDjTgYrjn6K_ZaOklM7cevgDbId49GvXwwNa3GY3CJXprfq7zyjjYRrr2p0stmKYU5RkIYmT2VhNiaSeV3PHbc91sV9OpXopd_0ENOjacua8YV5eg46_X1jMpMSMwsqEjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدت زمان حضور رهبری تو جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72698" target="_blank">📅 23:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72697">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e8309253.mp4?token=S0IpA09RcmtQDdi7FX7agDFnr1BB39qnHrfi-d7DPSMIVl2l31xE1bqH4e-wZEfg77uPc1C5s4wUjuskS-3FmzBpAjaw-L-td3kJ0_FTvaXp9Z6uSbhrEqjt8w4lPPW0sBQhDDOsfcMS1mYlkaQhohnt6Ao-WX5Vi3cqgT6Ky0bVIq0OOntBtHNK5Xe4aBs06I-Ipr5a5FyXdtpdZtgw7zYtU2Q7eQsz-TSjre0nvTR2QIaFdpoaRZYnpAzhFM4_Jnjs_ubpXTqm1hro5pncnxaG-ywNmhUIDif2z_UND8inOCLCgkhvNxqIXZw2LtBjxl0wwTmheYwM-WHJtGCmpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e8309253.mp4?token=S0IpA09RcmtQDdi7FX7agDFnr1BB39qnHrfi-d7DPSMIVl2l31xE1bqH4e-wZEfg77uPc1C5s4wUjuskS-3FmzBpAjaw-L-td3kJ0_FTvaXp9Z6uSbhrEqjt8w4lPPW0sBQhDDOsfcMS1mYlkaQhohnt6Ao-WX5Vi3cqgT6Ky0bVIq0OOntBtHNK5Xe4aBs06I-Ipr5a5FyXdtpdZtgw7zYtU2Q7eQsz-TSjre0nvTR2QIaFdpoaRZYnpAzhFM4_Jnjs_ubpXTqm1hro5pncnxaG-ywNmhUIDif2z_UND8inOCLCgkhvNxqIXZw2LtBjxl0wwTmheYwM-WHJtGCmpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
سؤال: آیا ناو «یو‌اس‌اس روزولت» قرار است جایگزین یکی از دو ناوی شود که هم‌اکنون در آنجا حضور دارند، یا اینکه قرار است سه ناو در منطقه مستقر باشند؟
هگ‌ست: سؤال بجایی است، اما من هرگز به آن پاسخ نخواهم داد.
ترامپ گزینه‌هایی در اختیار خواهد داشت؛ بگذارید این‌طور بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72697" target="_blank">📅 23:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72696">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=ky0m--H2O6x4xWc6O4_sI70sdeY9G5UiYL6dP7ve6KwBjIarZT8PCGbghDyWc-vcS69GvwLUUZWMH5pG3OP_AiPMAqgt7A4KSIQxb0oMroKUBUtmfWHhuXGc4B0zqkwvibd82nRVVv-lFSmAVWnYReWUjA8egWaEHMNELlZzPjWV1GGwG9NMjXwpqFkQQ-X2bVRmF-3J744Yha9lvoCTZb7mIxO6VrTLK1FdkeE1mWtjeg_1wKEOrJjhkW9O-OqfcyMv8hCUmxTOGSA68XDZn9wS5MkMSmzVy52Li1vWtEeFu_M_wjM7u4yit56vMosLS0mdWNcZN88PMrisjnAbcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=ky0m--H2O6x4xWc6O4_sI70sdeY9G5UiYL6dP7ve6KwBjIarZT8PCGbghDyWc-vcS69GvwLUUZWMH5pG3OP_AiPMAqgt7A4KSIQxb0oMroKUBUtmfWHhuXGc4B0zqkwvibd82nRVVv-lFSmAVWnYReWUjA8egWaEHMNELlZzPjWV1GGwG9NMjXwpqFkQQ-X2bVRmF-3J744Yha9lvoCTZb7mIxO6VrTLK1FdkeE1mWtjeg_1wKEOrJjhkW9O-OqfcyMv8hCUmxTOGSA68XDZn9wS5MkMSmzVy52Li1vWtEeFu_M_wjM7u4yit56vMosLS0mdWNcZN88PMrisjnAbcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز قبل تیک تاکرها باهم دعواشون میشه؛
چندتا دختر ریختن روی سر یه تیک تاکر به اسم ستایش و اینجوری همو کتک زدن:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72696" target="_blank">📅 22:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72695">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=LqXYNNy6p_5Rec_qsbCb58YbLHXigMTZxvw-bRFtMC5z4VbcGs3QCI18pFMF1z_0Q5ZuEFWDWRk70nWxwxsrtp3cV7LkR5FnOBe1_BRrY35eiyGOwYVuxfp_4lksAFXfpiAecREVZgpDZLFoEBS9uSAVlXSPLCiAVdEW42j0RXMEAu0o3uGB7-KNIFRNjA4GlZRKB2FK4TYqbwu7fihAzEB9l0a3meIhCoojwS2K1vdBR-0pcXs5Zk-WHILJ-fNzmF-PJzk9q80aShTQ5KAq2H0XX_WL0sNr_RmiaQRcgLYnH_8nMeXdwGaxAbhIWHuOYcIrBVKfFjWsF4zcy6Jc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=LqXYNNy6p_5Rec_qsbCb58YbLHXigMTZxvw-bRFtMC5z4VbcGs3QCI18pFMF1z_0Q5ZuEFWDWRk70nWxwxsrtp3cV7LkR5FnOBe1_BRrY35eiyGOwYVuxfp_4lksAFXfpiAecREVZgpDZLFoEBS9uSAVlXSPLCiAVdEW42j0RXMEAu0o3uGB7-KNIFRNjA4GlZRKB2FK4TYqbwu7fihAzEB9l0a3meIhCoojwS2K1vdBR-0pcXs5Zk-WHILJ-fNzmF-PJzk9q80aShTQ5KAq2H0XX_WL0sNr_RmiaQRcgLYnH_8nMeXdwGaxAbhIWHuOYcIrBVKfFjWsF4zcy6Jc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اخوند تو تجمعات شبانه: در پیروزی ما توی جنگ و ابرقدرتی ایران تو کل عالم شکی نیست؛ الان دعوا فقط سر میزان ابرقدرتی ماست!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72695" target="_blank">📅 21:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72694">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=nvpHdfJ049FrsE7nUeeQXr0f7t-QZDOCIH0JBKR8O3OS4h20K4e3vYmRLfvfNroBqnWLQdVd5xPqAXZBtMRVobdH54365qis6fdYUjqi3VG4i4ExNsrUYDLXWiOREQjn4eHq9Hcxx3MczusUcYASIMbzV7Buq0xUsV6OrbAxlB6wlgCrlaJ4hE1j9EQFQtGN52Wu1lkYKILhlvuT9zYTA2kV54dQwAn1qZwClabFNWpsRt2win-sk5Jkkbzo9Unilepk9PQMuV_bQFr6MgvXn4FfRWD_jR2S5Gw89mgdGmFit5X-iGtmdePjIapNdIcSJpye0F4T8Jx3JStNuL840w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=nvpHdfJ049FrsE7nUeeQXr0f7t-QZDOCIH0JBKR8O3OS4h20K4e3vYmRLfvfNroBqnWLQdVd5xPqAXZBtMRVobdH54365qis6fdYUjqi3VG4i4ExNsrUYDLXWiOREQjn4eHq9Hcxx3MczusUcYASIMbzV7Buq0xUsV6OrbAxlB6wlgCrlaJ4hE1j9EQFQtGN52Wu1lkYKILhlvuT9zYTA2kV54dQwAn1qZwClabFNWpsRt2win-sk5Jkkbzo9Unilepk9PQMuV_bQFr6MgvXn4FfRWD_jR2S5Gw89mgdGmFit5X-iGtmdePjIapNdIcSJpye0F4T8Jx3JStNuL840w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بمب‌افکن راهبردی رادارگریز B-2 Spirit نیروی هوایی ایالات متحده بر فراز محل برگزاری مسابقه تیم‌های نیروی دریایی و نیروی هوایی در «کلرادو اسپرینگز» پرواز کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72694" target="_blank">📅 21:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72693">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=IBe2mOVA_ljx-Lel8OCsP-qOa8b8JtP_3cDjTQYLvUM1zQ4utLFSLbBDeHec5uZBJpcviw8ZshmD4KFbtEZ_W8R2Gv-5YeS291o_jZRd_fr_p_GiQ9ghISrqfMbwqUYqabDkcc6vHKJpztR49J996FttHbX8vEc9YAWdX5MVGLV5MGyC_RE24sK9LSnCfuLKEuZfxfL_UMKOtddxyTNsTa_c4tm-QqBuoLkXmDHzcA-Jp6baqri6lD7J8zmStIEJVQL_Cm98_i2e-VxWhxxd6gS1a2wTlZJzAZ3lVcsSqAkXhStWtpm1912piUzuI0cQRJdIm9BBrWmObpSLUFPW0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=IBe2mOVA_ljx-Lel8OCsP-qOa8b8JtP_3cDjTQYLvUM1zQ4utLFSLbBDeHec5uZBJpcviw8ZshmD4KFbtEZ_W8R2Gv-5YeS291o_jZRd_fr_p_GiQ9ghISrqfMbwqUYqabDkcc6vHKJpztR49J996FttHbX8vEc9YAWdX5MVGLV5MGyC_RE24sK9LSnCfuLKEuZfxfL_UMKOtddxyTNsTa_c4tm-QqBuoLkXmDHzcA-Jp6baqri6lD7J8zmStIEJVQL_Cm98_i2e-VxWhxxd6gS1a2wTlZJzAZ3lVcsSqAkXhStWtpm1912piUzuI0cQRJdIm9BBrWmObpSLUFPW0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از سیلاب شدید امروز عظیمیه کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/72693" target="_blank">📅 21:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72692">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72692" target="_blank">📅 20:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72691">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df1mRlhiCll5SK480Oliec56r8uIdaMnn93GTLD-S5mYSWpW4wcOYQeqHU1b_rOOcFmXTQhmGgrlfRwdesZRK4hjVR7A2ykwtxaZMeEn1z9QCRw0X9KEjr25ZA6L0y9OXrFhsf-ZDq35AxjGBUUb426xnI3RUEURYC3aHrcDSOz7aTJi4oskOGqONK-BXtj6qlJcS1owmQGZP5-Phny91Y0qV61gBPX_FzQKVIEZCO5DYie-U3DSINg9OQ4KnOCyyJ2dwH6Pida5AUQoCN6Wj8pf_q5540oUjhgITTMV7mr0VlA7bcOHx5-bgn3Ol65Xud2LJyAJPV0uPsvRzpmuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده — در ارتباط بوده‌اند.
بازرسان در تلاش‌اند تا هویت فردی را که این افراد را به خدمت گرفته، شناسایی کنند؛ کسانی که یکی از مقامات آن‌ها را «افراد ساده‌لوح و بی‌خبر» توصیف کرده است.
با این حال، مقامات اذعان کرده‌اند که جزئیات مهمی از این توطئه ادعایی همچنان نامشخص است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72691" target="_blank">📅 20:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72690">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دونالد ترامپ به تمام شهروندان بزرگسال ایالات متحده وعده داد در صورتی که جمهوری‌خواهان در انتخابات مجلس‌نمایندگان و سنا پیروز شوند به آنها ۵۰۰۰دلار خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72690" target="_blank">📅 19:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72689">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=H13V44NoUsl2gehIE6YjTum7zNZX6erH4BE9XkmKMfyaHyNmphbuNOMyqA09jMNV3hLd9jap0Ar35DJDNnsmu605JQA8JVcZc0pwmtQyi15bEo7Trhf7Hm8fmcnNVGnWAzE4hrX73TWmY1zoCvmIAIY5dXWIYM1N3l_WsPtua1leipeb4GoHnAH8q2bv0BhMa1PdFf6W-l_Qc-qSsqWrtm4hbQwIWvEra5hmZelSRoEE07JB-RkYVRb5rdHMlDRG0IWPAWx3xvsSg-lvRBVvz2zdkSDMtxVrWJIoj4B_D9bVvBDXpRtuh-LU81c0zSXVJ5vMxwR01YCY4LowCoLcx3Y_LxZ5Y_drLAwjLkg7OSoixJOxstoP7L5KNHRoT8hvMkXrMG8iPpoC3z9VI-2zwcu6FAAxBCsU8UCEEBUGyWoKySqjLR5pdAGtxG_zZ_geFdwsY-1DS_vkjtyfepAxdEgMMt3ysD_3ATg3uMGLbA5bHTd582x_Dk1k3LWDTSvjZXFI_aqGzes98oitYUgLBNNKRZiSY1wPBAyOR-roVvnhz_E9Y4pOsFduLsBZKngAKM-ALVi6QhlQ_8dHcTSTVhlrtZakohFjMSFIJgbOdWH0UFavIHom_60CUl9QccD8jcu4vIQBybqDLOt4DxTR1esdSAyjCUfT4buQWlo7x2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=H13V44NoUsl2gehIE6YjTum7zNZX6erH4BE9XkmKMfyaHyNmphbuNOMyqA09jMNV3hLd9jap0Ar35DJDNnsmu605JQA8JVcZc0pwmtQyi15bEo7Trhf7Hm8fmcnNVGnWAzE4hrX73TWmY1zoCvmIAIY5dXWIYM1N3l_WsPtua1leipeb4GoHnAH8q2bv0BhMa1PdFf6W-l_Qc-qSsqWrtm4hbQwIWvEra5hmZelSRoEE07JB-RkYVRb5rdHMlDRG0IWPAWx3xvsSg-lvRBVvz2zdkSDMtxVrWJIoj4B_D9bVvBDXpRtuh-LU81c0zSXVJ5vMxwR01YCY4LowCoLcx3Y_LxZ5Y_drLAwjLkg7OSoixJOxstoP7L5KNHRoT8hvMkXrMG8iPpoC3z9VI-2zwcu6FAAxBCsU8UCEEBUGyWoKySqjLR5pdAGtxG_zZ_geFdwsY-1DS_vkjtyfepAxdEgMMt3ysD_3ATg3uMGLbA5bHTd582x_Dk1k3LWDTSvjZXFI_aqGzes98oitYUgLBNNKRZiSY1wPBAyOR-roVvnhz_E9Y4pOsFduLsBZKngAKM-ALVi6QhlQ_8dHcTSTVhlrtZakohFjMSFIJgbOdWH0UFavIHom_60CUl9QccD8jcu4vIQBybqDLOt4DxTR1esdSAyjCUfT4buQWlo7x2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
مرا بفرستید تا با «کت‌قرمزها» (نیروهای بریتانیا) بجنگم.
مرا بفرستید تا با کمونیست‌ها بجنگم.
مرا بفرستید تا با نازی‌ها بجنگم.
مرا بفرستید تا با اسلام‌گرایان بجنگم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72689" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72688">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=DRPY5pv7C9D9QPMVRpiYNjXrQn93oV08bN8BLfnLdO3mkKpmpPrj96MqWu3owfx10BgLPNUQXoKNvJJ9-cISKrqzSkIPp6tKjkF3itOvas85jOpD0-I7JPUsNkGozglUfrWy3U_VLWlwA83mIwqJLH2dagfSYCP0oX0EQ1u7WDHcfm1J4eOHPtoUCVjFXtg8QuMMjpF2w0faSviJQrFtoi5FFRFHL1AQWD2rw6j3AcXw5hDXPB-SyVSBrCHf96yX12xlW_qfmUmG96wOT3Xn9XMswFYBWuuOUDnsTnIdnhoBLKWoYTX3OEI0jIH3zDS40_6CA7tLpl9fIN5S4z6-Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=DRPY5pv7C9D9QPMVRpiYNjXrQn93oV08bN8BLfnLdO3mkKpmpPrj96MqWu3owfx10BgLPNUQXoKNvJJ9-cISKrqzSkIPp6tKjkF3itOvas85jOpD0-I7JPUsNkGozglUfrWy3U_VLWlwA83mIwqJLH2dagfSYCP0oX0EQ1u7WDHcfm1J4eOHPtoUCVjFXtg8QuMMjpF2w0faSviJQrFtoi5FFRFHL1AQWD2rw6j3AcXw5hDXPB-SyVSBrCHf96yX12xlW_qfmUmG96wOT3Xn9XMswFYBWuuOUDnsTnIdnhoBLKWoYTX3OEI0jIH3zDS40_6CA7tLpl9fIN5S4z6-Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
اطلاعات نادرست، اطلاعات گمراه‌کننده و تبلیغات عامدانه‌ی بسیاری پیرامون ناو «یو‌اس‌اس آبراهام لینکلن» وجود داشت، اما ۸۰ درصد از کارکنان آن گروه ضربتِ ناو هواپیمابر، برای تمدید خدمت خود اعلام آمادگی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72688" target="_blank">📅 19:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72687">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=sCP0EsjVQDJ_XfXIX60lG9AelE2nBEj03pprdYPloouMFsRmNdiBBnuFGA1jdwk6GUPjMhxJuFdPIeGUjdnvWp-gp1MshiBjOVerK_2grE_Ir2oybuYzIUVAsXmeBpX3c-9StzwzKEECgcGscelQXCrwKTO5sm0saMYk6IYpDuixPaXtIhlczbLQ7IMIWQyVCztXTFbs8P96T47IpZDaOe2-cOE7Bvw0t2M1mzrSF-Mh0vvn3nLgS1IXi-tDAIHSeVxvMlx5_XHMoTYsPbTBnYKtdudwWEz4iVej8S3_2rFJiikVKb6RbfMDxiosBxPMKfwwV5KqSYv7jZE_CEbMCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=sCP0EsjVQDJ_XfXIX60lG9AelE2nBEj03pprdYPloouMFsRmNdiBBnuFGA1jdwk6GUPjMhxJuFdPIeGUjdnvWp-gp1MshiBjOVerK_2grE_Ir2oybuYzIUVAsXmeBpX3c-9StzwzKEECgcGscelQXCrwKTO5sm0saMYk6IYpDuixPaXtIhlczbLQ7IMIWQyVCztXTFbs8P96T47IpZDaOe2-cOE7Bvw0t2M1mzrSF-Mh0vvn3nLgS1IXi-tDAIHSeVxvMlx5_XHMoTYsPbTBnYKtdudwWEz4iVej8S3_2rFJiikVKb6RbfMDxiosBxPMKfwwV5KqSYv7jZE_CEbMCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست لحن و رفتار ترامپ رو تقلید کرد و چیزی رو که ترامپ هنگام پیشنهاد این سمت به او گفته بود بازگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72687" target="_blank">📅 18:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=hWiG4aewnMpVV_Ttx9CWtUGwyodGbLNpaiGhMUhpykVZIgj7lnaLMh2iU0Y_PbeKgxSvAzDtN_7q6Nm8Cw2ZiYqr332xNWjYbfBx0NgHDCQBGjrNmC-md11WnXLnGh2PeSvG7HQApmOsqrLGKT_-r2B1qvD1evTDDOi6P4NfReOBWDMrX2Ot0m3a_Muok6ISh4iKpNl5dkOwkW5hGNpesBpAJr4Qw6bpOurEjgtmSF3CuxHTcFKzAR08ayRdMsDZ9aUG8fnsGgYexEL-Kt5P0ZC6fGAKuTaMYRWL4EUAZKZUC0x8OrnOZ6S78oY6fjD0LB8CB_23DzfhZjqEsiXSvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=hWiG4aewnMpVV_Ttx9CWtUGwyodGbLNpaiGhMUhpykVZIgj7lnaLMh2iU0Y_PbeKgxSvAzDtN_7q6Nm8Cw2ZiYqr332xNWjYbfBx0NgHDCQBGjrNmC-md11WnXLnGh2PeSvG7HQApmOsqrLGKT_-r2B1qvD1evTDDOi6P4NfReOBWDMrX2Ot0m3a_Muok6ISh4iKpNl5dkOwkW5hGNpesBpAJr4Qw6bpOurEjgtmSF3CuxHTcFKzAR08ayRdMsDZ9aUG8fnsGgYexEL-Kt5P0ZC6fGAKuTaMYRWL4EUAZKZUC0x8OrnOZ6S78oY6fjD0LB8CB_23DzfhZjqEsiXSvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آب‌و‌هوای قم رو ببینید
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72685" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72682">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p42fR8L_mejdcFHO9jkLC4HcnNf4yZ4ywzhPZkvAXzd0EY1A5Jfd_8WPT7E1mEu80yLoyvBVPGDEndzMFWiMfehg4kCB-yb4ZdokjrmIxk_kpha7CxsrT_GXofTaMmUWCtO3KdnElm7_nPW0hnkaX6PPrhfh3Hcs3sMkvodAOU1wswn6oXg60F8zNYgUhdLGDj3KDNROKxWFqeGOSR2YBvPI7YyP2mKMuizFxbIfKaW89aiX0v4g-WzLarP_4yX2I4S1YWaXdJfsC7FKJaTFapC4wnc1UQtjWqCKTDpTAVeIlKDqKNShoXgh-HHb--PZKPC4RQ5ONXLHcMePHHcCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YFu77yeNi0s7kZ3VZpa-OjkQNQ95rmZ90l7xRJjB3RApqWcgsRwSDY8ZNzXuQs_qkyYaROvZo83mF8g0FsWA9VN-pB6NLR-CQzp--vY4xF-0UlhQlwb9UKdLSvOV3wXFzzRH8ZiNggOahqBb5_DxZ_tLpIVPHcYGt3e2jjs3my15d1d4d30Xt1pdHH8g-G5OFOOrVOnRsf7Vhpkkj8Cpy8ahieFfuuthOip-AlmOGdBxkzHgIhhejWjCWME_ItmVK8unIWxEhVhZLUsnKh0L_CABrJDrnGyz4DcI8iMO9YjwaSoGrTFF5PTBI97PsBaS-fxz3kk5SIIMqijhJjaQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e6nRkXXPc8LzRNPdph0jJsOiihscfp6Yo7z7qj6NrpqH0D2hN_wFrs7htaZ8Q782XNcvvXsMwbDdP6WK4wumlpO-Kq8q6aThBmpoZIHD1NM3XpDKVBM3-WThgAiPEi_cdWsltP6_AnAd1cOsgV5dEcOlJL127hQAtDFaPdi_QJ-TlHfFXkTrCtyCaHUbriOX65dp1H1Po1pJMFVkRd4mLv6kr8BA5Y07P2D6YiRbh2AQGQ21npHxQCjA8yAgdulRTkfHTxl6R8i_t-p1j1XX2S5EoHj4x2Pop3fxGX7G6IOSfugBFlxJE4-tepC3pvdhzc72lLqUoIHcSpWJhCCKLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایلیا هاشمی:
ساعت ۱۶:۳۵ شنبه؛ ابتدا صدای جنگنده در قشم شنیده شد و سپس یک جسم مشابه با بدنه موشک، داخل شهرک بوستان قشم
سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72682" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72681">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72681" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72680">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOAuTcPEDWX73zR656dw3ExlEv09pbktK2UOh9p_2IPh5TPHAyeFJ-T28sQjrj1OnJzcyqsg50dSSBTzAOEquehwwB7Hl2By3wCWtbM9hRAWCzNazSTDoSM2_hFwj_A3Hj4SHPMCNbIQc6jWZaNY1ek3Brdl-zIbWbAmdscKQqSs65QZrPWZGND_pRSBHsQRW0VlT1xYe_s89ainHT3Jn4-NA9gsCHEr9Hwu6gujTM553HvJ4Ep50VEH-B0blw2uxcl_uO3puSo3-qkjpXeXRV239kWS-MeUccKTdPO56bx9_1XufbmWq1htrKZ_B0JGVs8gg_xqLqX1s3k_b35-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز انگلیس
🆚
کرواسی را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
انگلیس: ۳ برد، ۲ شکست و ۱۳ گل زده
کرواسی: ۳ برد، ۲ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72680" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72679">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323337b42.mp4?token=ce5glxwVK9HyZ25hXLgVcY-7OlC3qXZi6iEvTOLaOBBX-lxHBh1QY3xM1Js7zAOrj5cuUkOnHu04VcMBTmoLPpDvIetxUw2wdBh6HFxgY4CZu77l17Zo140rbQKqYqvPXeAmwONA28wqMerbdDbloe95yg8I0dTbGemkJdhYTLITS_0z0dNpv52phv9uyWuMPWpdnq3MIkjC13gD1Vrf8TsLCEGMb5-O9GATpQH0MQnnx375rvYIX7lLIJOoiGGTmTtHiDx769rUrqdeafgAqkuVCjHKME4wr0Tre0mwKa1-rbmViExXjF0Lcq8fzf7VsA_HX-LysVKpArL3q1vSEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323337b42.mp4?token=ce5glxwVK9HyZ25hXLgVcY-7OlC3qXZi6iEvTOLaOBBX-lxHBh1QY3xM1Js7zAOrj5cuUkOnHu04VcMBTmoLPpDvIetxUw2wdBh6HFxgY4CZu77l17Zo140rbQKqYqvPXeAmwONA28wqMerbdDbloe95yg8I0dTbGemkJdhYTLITS_0z0dNpv52phv9uyWuMPWpdnq3MIkjC13gD1Vrf8TsLCEGMb5-O9GATpQH0MQnnx375rvYIX7lLIJOoiGGTmTtHiDx769rUrqdeafgAqkuVCjHKME4wr0Tre0mwKa1-rbmViExXjF0Lcq8fzf7VsA_HX-LysVKpArL3q1vSEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن مرجانی، رئیس انجمن صنفی تولیدکنندگان شیرآلات ایران:
اگر این وضعیت اقتصادی دو ماه دیگ ادامه پیدا کنه
کل کارخانه‌های شیرآلات کاملا تعطیل میشن
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72679" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72678">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ناو هواپیمابر USS George Washington  در حال انجام عملیات پرواز در آب‌های منطقه در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72678" target="_blank">📅 17:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72677">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=VEQzP5V63j5h78gLUciypvLOl9tgDAGvujfG2N0wcbNTTFURxHBX_5VqhLdukLx9XJcCEG4EuWaYWOmEVDU5k8USqOvFq-tR4UrqznHAGdIfQZSsJRaS6v8tovl4kEGYLcO4-0We7SZJvd-lWYAEUn6EllAHsxsrz9uzKF9cYJAfZX930ns5U4FlU-eu2Zlh7ctjqgxLm7htbfoZDxm5jpTD0OVSw1cGJp731BVDl_ZZr_21d2PGjO7GWw-yFkWI2TCnZgczUh1pzYn1NfP7koed-w2tkTo3Y04vY1n3SCw3cc5fb2_WFoDZl85Iuh5tsk1Is4MW4VYHlq4-KLxaPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=VEQzP5V63j5h78gLUciypvLOl9tgDAGvujfG2N0wcbNTTFURxHBX_5VqhLdukLx9XJcCEG4EuWaYWOmEVDU5k8USqOvFq-tR4UrqznHAGdIfQZSsJRaS6v8tovl4kEGYLcO4-0We7SZJvd-lWYAEUn6EllAHsxsrz9uzKF9cYJAfZX930ns5U4FlU-eu2Zlh7ctjqgxLm7htbfoZDxm5jpTD0OVSw1cGJp731BVDl_ZZr_21d2PGjO7GWw-yFkWI2TCnZgczUh1pzYn1NfP7koed-w2tkTo3Y04vY1n3SCw3cc5fb2_WFoDZl85Iuh5tsk1Is4MW4VYHlq4-KLxaPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
برای نخستین بار در تاریخ — از زمان آغاز استخراج و صدور نفت(ایران) — آن‌ها در هفته جاری هیچ نفتی روی آب (در حال حمل‌ونقل دریایی) نخواهند داشت.
آن‌ها هیچ درآمدی نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72677" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72676">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72676" target="_blank">📅 16:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72674">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2XCZhwGzR7jIu5T3r2c8cclSUYF7cBlswXorVe1rVu4tk87lxinyirlkxh-4EHmbd9WydI-8uYqSvv0qt3zSw9QRXBNRA0ynss-u52OU0h08FjoccEpJIHC2KsYLy5_paC14ubfBe_W-f4acxtkk9Vyj8CkaCGfH2YsbSrddkwo6gE_lXWPFmItgz061i7vdZCQfuSjiTkjI_pTd9ai_-rjRZsfQ-iq6_Kt8iaQUJqcYXiE4a3FONKuHC4vHFlLkdm67afmhY2Sk1tgsInXOVqCS0Z6DODFa9O_vClPW0h9Xm-4u_OfbrP0OC7j49D_x3XNfE5mPhij1P_gdbxQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vSvGuCKOqmtfQstY8TrCbwlYZAfrlQdb5ZMchPtNUiZZ5J172JeNwqE0E3yAGNUiSREYciGfwtBRhfnQKD304nLMb-JkiWBCzEmNuPQdUGDfuLPIy_l-7BZ1vCsrZLalZM4p0nV1X7g0aDAqJ-Yl2N_9AA43KCbSPFz31GB0ETImo4ga1cnNUBm_9FVz-8Ws13TV2SgsAcYvVQoXQK8BFP1KOBqC2biAcsezFspVTNvXShjTv1grcNeV6VTGZFHYdZlFuWeIS0VTjRq_nuJr5U6Uq4yt8lxJPO9ODcuOTJIiEwoI6xliajv-gOMnEWRUgzd7DrwIcOQ3zWDmO_nVmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمونه کار:)
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72674" target="_blank">📅 16:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72673">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heO5zUOkbolpZc42gOJrlAhFJ5iACti5z8KXuzBaNfOxyNAbrGeJgiGfn65Idka3RcuDKoCcHkPpb3PGIpL_Vp8bwfXeGvpXUyQXASKOuwaZx9F7QtzcJTHNiOYJ26Wfi_PqEArZp6kHBDOGY9biyRdMn29msF49KEi7xURnILUM1_xTXP2ZoEMNDZJdnScMUXu_23IWhca4ImWiKs2mmAVc-AvyEo1BSvolUX2rZMwM-SYFIa43iuHdmxgP3U0Q0txwn9FIqP7qH2wtR6Bx2-SH-3hSoNVcO4J6Iiwkrz7GPDsnMwY6aey5oQ2IghjmSlceq9uaPhVoy_kk6jiiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به دانشکده 05 کرمان
✌️
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72673" target="_blank">📅 16:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72672">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#فوری
؛نتایج اولیه کنکور ۱۴۰۵ اعلام شد!
با ورود به پنل شخصی خود در سایت سنجش میتونید کارنامتون رو مشاهده کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72672" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72671">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=TqaTr-j_gGJurJ642GGYjS6DroJhoP-5d-rd9UP3BDcd04YdF-mdGrLINzUdXDK_Z0y8R7xuu0VP8VbT9M3pHCYZO7zN5Nw1SkOZGvDQU_l7O6j6-uV4bsVc3Bik81cfUfkOsUkIQSvfE8oUMZ7iiB4ir7HMUsrOQ3jCm_tq4CMlNK5yLv-umrKST0GMeTcz0BrdFZX8zbWtfp_YMvf6GVMcPhIzgoVvLQx6fYf9Q19Nl5J4FymaCthEgjhJKGaEszKB-40m8RLKRcTTtoT7ZVqfUISQKHiZlr29TXEiX5EvzAmvyg6u_oz0Vs0FxGIfdknhBADHW4T_iKWV-piXqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=TqaTr-j_gGJurJ642GGYjS6DroJhoP-5d-rd9UP3BDcd04YdF-mdGrLINzUdXDK_Z0y8R7xuu0VP8VbT9M3pHCYZO7zN5Nw1SkOZGvDQU_l7O6j6-uV4bsVc3Bik81cfUfkOsUkIQSvfE8oUMZ7iiB4ir7HMUsrOQ3jCm_tq4CMlNK5yLv-umrKST0GMeTcz0BrdFZX8zbWtfp_YMvf6GVMcPhIzgoVvLQx6fYf9Q19Nl5J4FymaCthEgjhJKGaEszKB-40m8RLKRcTTtoT7ZVqfUISQKHiZlr29TXEiX5EvzAmvyg6u_oz0Vs0FxGIfdknhBADHW4T_iKWV-piXqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ما از این مناقشه با ایران عبور خواهیم کرد. به گمانم عرضه نفت بهبود خواهد یافت و قیمت‌ها به‌مراتب پایین‌تر خواهند آمد.
روند افزایش دستمزدها ادامه خواهد داشت، چرا که شاهد رنسانس (احیای) بخش تولید هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72671" target="_blank">📅 15:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72670">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72670" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72669">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=OzYaD3pQMCrPE23RvK3-rn_8CCQVSBf9qJHod9e5r1vVcVbW4cNseICARqEeMEegRgyVvrTZI2rAbcRBJcV-XBNQDIMxFUwBciU3iQmHAO7whoRzfuFWuhJOLCgMckeEoPRLZM7kFnLBeeok1yF4dGu3uWC6MvDzAmjiKHhbZPfygq3IoDj_gY_kMDOTvPyeiDVCnKIKFZfwsibO4qYFSxUNFk_uHupNTTyXzFdwvYCGP8CaEjfxG4gh1Cj5Q6sCRjP33hVJ6JdJ7-qRlsXv5BqFkIaLrbCla_yx5x3NVEqXgCA51-ryzC_NyYXTFFWahqrV-3jp6HfmIAAzP7HLng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=OzYaD3pQMCrPE23RvK3-rn_8CCQVSBf9qJHod9e5r1vVcVbW4cNseICARqEeMEegRgyVvrTZI2rAbcRBJcV-XBNQDIMxFUwBciU3iQmHAO7whoRzfuFWuhJOLCgMckeEoPRLZM7kFnLBeeok1yF4dGu3uWC6MvDzAmjiKHhbZPfygq3IoDj_gY_kMDOTvPyeiDVCnKIKFZfwsibO4qYFSxUNFk_uHupNTTyXzFdwvYCGP8CaEjfxG4gh1Cj5Q6sCRjP33hVJ6JdJ7-qRlsXv5BqFkIaLrbCla_yx5x3NVEqXgCA51-ryzC_NyYXTFFWahqrV-3jp6HfmIAAzP7HLng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واژگونی ترسناک کمپرسی بر اثر ترمز بریدن در کازرون
💔
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72669" target="_blank">📅 14:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72668">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پشماتون بریزه!
ایران‌اینترنشنال در گزارشی درباره مهدی نادری جهرمی، رئیس هیئت‌مدیره شرکت تهران‌اینترنت و مؤسس و مالک اپلیکیشن هف‌هشتاد، ادعاهایی جنجالی درباره ارتباط او با شبکه‌ای مرتبط با موساد مطرح کرده است.
نادری جهرمی با نمایش چهره‌ای کاملاً همسو با جمهوری اسلامی و حضور در ساختارهای اقتصادی و تجاری، به تدریج به موقعیت‌های حساس دسترسی پیدا کرده است.
ارتباطات و فعالیت‌های او در حوزه‌های بانکی و مخابراتی، در اختیار شبکه‌ای قرار گرفته که با عملیات موساد در ایران مرتبط بوده است؛ از جمله انتقال اطلاعات، شنود و نقش در برخی عملیات اسرائیل در ایران.
این گزارش بر پایه اسناد تجاری و قضایی، مکاتبات بانکی، قراردادهای شرکتی و روایت فردی با نام «کیا» تهیه شده که ایران‌اینترنشنال او را مأمور سابق موساد معرفی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72668" target="_blank">📅 14:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72665">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXnj_-m-2fipwPw0UbSXWk5fYJ-9hxnOhD5n_J8PuX6hv0bfWoHHwcosZhi_P4-_vc5Gg_hFQN4w6nCBLU7LwZqRAPkiZf2tqz8PVdlmMAQY2jqv8hjuJWtFt68oIAzLt65zpZSw7t_UL0-Js7fa3BfQHTvt3FIgthqgRtnj3Hljijw8EMK0yaFlS-_JEe55rIjcZ374xb6qtUlob-VgHmgVJoylFIuEjmPFe2pXLVg-Swb85ZCiT4sqv2Xe-sk4kQw2xZH4Ri1uhj5abmQMw50TMtEE9oIvfgzvTKTZtou7caJOWSnpT4ILSyvZVj4Y7sVAIt2j0gqsGowT3X9wGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=Ru-A7GBctCvCUW7GxjuQUDhybYxyyX63Ek4VnHswQOuc8O3CWqX9l2-N5FUR4xnjAZ8rap3jhD55p40soVXvkxXBSjh-eChYNbXMtDR5DfL0mU_gsJkgAhyLyqJRyAhXV8v7dkBcKes7GkXkO9TjEEtv9F6Lj9Afc5gH_BpuOEI5YXxP7AIq9PUXjOljk5s5loDcdmpd1VP2rrtK2b_vnAZRlAlWTSDSV3kQ3AvR-bJ7YJQoAFkDG-SFkCjl8NEH9dQ9siE_Qd-yjnMviVehdV1ROfLi30B3JRlz-TZmJglrVlheJXNBe0ZCU2jBHjaYMaggIN2UKqpubF6fDkzlZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=Ru-A7GBctCvCUW7GxjuQUDhybYxyyX63Ek4VnHswQOuc8O3CWqX9l2-N5FUR4xnjAZ8rap3jhD55p40soVXvkxXBSjh-eChYNbXMtDR5DfL0mU_gsJkgAhyLyqJRyAhXV8v7dkBcKes7GkXkO9TjEEtv9F6Lj9Afc5gH_BpuOEI5YXxP7AIq9PUXjOljk5s5loDcdmpd1VP2rrtK2b_vnAZRlAlWTSDSV3kQ3AvR-bJ7YJQoAFkDG-SFkCjl8NEH9dQ9siE_Qd-yjnMviVehdV1ROfLi30B3JRlz-TZmJglrVlheJXNBe0ZCU2jBHjaYMaggIN2UKqpubF6fDkzlZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هزاران دانش‌آموز دبیرستانی فرانسوی به دلیل کمبود معلم، ازدحام بیش از حد و ساختمان‌های در حال فروریختن، مدارس سراسر کشور را محاصره کردند.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72665" target="_blank">📅 13:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72661">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=PT1Eeyamb5QwxE4f_RJoFzFu2Uuqf67Alz0205OcKbw2tKARTfbOsZRUfucYysn2QLlRsIUB8mt9zIGb4-KlBentLwbtbPVpgS_Sov-6lPeSW0GrPzNwkYndwKW360J_eKVGKITXBTUesZY43ukt1RVp2gn0Leu83lda5p2ZmxbzmR0iH8tTXO8zkhiuTTalbfKgP5_ciwYHcVuTW21A6ENUawdYOxB8H38hu0TlHA9YV7_V4v9aJPpOrz0pQN3WmD99e-ekzEEXL6YDVkijKdbIdcSJuNnTVG0iE5aZPIBzX_KV0GJV7C6sEo4JnHkeo3xK4GzKuiKptTIvT44rrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=PT1Eeyamb5QwxE4f_RJoFzFu2Uuqf67Alz0205OcKbw2tKARTfbOsZRUfucYysn2QLlRsIUB8mt9zIGb4-KlBentLwbtbPVpgS_Sov-6lPeSW0GrPzNwkYndwKW360J_eKVGKITXBTUesZY43ukt1RVp2gn0Leu83lda5p2ZmxbzmR0iH8tTXO8zkhiuTTalbfKgP5_ciwYHcVuTW21A6ENUawdYOxB8H38hu0TlHA9YV7_V4v9aJPpOrz0pQN3WmD99e-ekzEEXL6YDVkijKdbIdcSJuNnTVG0iE5aZPIBzX_KV0GJV7C6sEo4JnHkeo3xK4GzKuiKptTIvT44rrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از انبارهای نفتی آرامکو در ریاض که هدف حملات موشکی حوثی های یمن قرار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72661" target="_blank">📅 12:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72659">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EMYf1msN9pCNIeBOG7o948lLM2crsYcWqZ7MUZcW4NzQ5kv0EQD4s6zuY_SwwifB51RaSf85I9TY1nvyWhfwabqsU10NAdwiftjE9BflOL5yk6daK2lVP-2qUALatAMYdul-0BBDtsStIzWyiuoIWkZYdYAvv4SquAllu9J1IqO3OAs1N643680LfrxiLITXU-4aboQxpaJLs0ND5G1Y6dL5_vGXeJ54Rz6zfifTM2mapnCH7XSZa4Hrf7yzKfoFHgnXVBcFnZz5yjOk52ycVWKqb3bwvJWA3mfgPFkCDqH68LVq4WKLjdQeou0fHAOFyLZ2uMs6plrZbx06x3wsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=UH5aU7zwyZ6fAKjNK-hI0UWsmK7h57As4cO1qWaakgN5xKcLcZn-rn_aPI_Ry83aLahndSujLcOuKw-tFNqBaxERT9xOeKdNa8uevzU8LeOLG7Gk_gZyEMx3BOiJsehgojiL7mMerF7BVJe_Cqf5ClbVLgjG6noTVWPsAtgXqqYsvA7OgFLkq812l1KceGt7X55skjgWowwwb01Hakdj8r4xxk9ax4Z2Kqpygq7jGTs9rFwY_za7Cv16fyHlHB_lRXhxbrWpryMC7FOWpJV0c7H1M40BSb6YYMQlEQCEUOy4YxW7NJH13YsAmHTKG0ytV7YLckTwC2wqdRldb-OCcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=UH5aU7zwyZ6fAKjNK-hI0UWsmK7h57As4cO1qWaakgN5xKcLcZn-rn_aPI_Ry83aLahndSujLcOuKw-tFNqBaxERT9xOeKdNa8uevzU8LeOLG7Gk_gZyEMx3BOiJsehgojiL7mMerF7BVJe_Cqf5ClbVLgjG6noTVWPsAtgXqqYsvA7OgFLkq812l1KceGt7X55skjgWowwwb01Hakdj8r4xxk9ax4Z2Kqpygq7jGTs9rFwY_za7Cv16fyHlHB_lRXhxbrWpryMC7FOWpJV0c7H1M40BSb6YYMQlEQCEUOy4YxW7NJH13YsAmHTKG0ytV7YLckTwC2wqdRldb-OCcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی جنوبی ایالات متحده فیلمی از عملیات شناورهای جنگی آمریکایی Saronic Corsair نیروی دریایی ایالات متحده در پایگاه دریایی گوانتانامو بی، کوبا منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72659" target="_blank">📅 12:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72658">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ:
باید با چه کسی طرف شوم.
کسی نیست که بتونم باهاش درباره ایران تعامل کنم. هیچ‌کس نمیخواد رئیس‌جمهور بشه.
من می‌پرسم: «در ایران با چه کسی صحبت کنم؟» تق‌تق(در میزنم)...اما کسی خونه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72658" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72657">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72657" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72656">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXFnvyRFOY4zz9sF-vj74vJVch3ZRUYe6o9OEKDTimzKz9zdrFkv69D9q24eqFSENBNRQES_V_BMSxza1z6alQtzlVBdlvYOckCm5CIZt-Qa-vjJoqT_c6ateI1BYHwjkzbUwFA4EBpVfJ0eVgxd_rPijfwj0D_oChJTbxPb4bBuLJgpuhQxbEWqc4zTEYCeOqaqjLKCa6Mt5UXNPW7FhpoD00hxTF_yNpuZCqPSzcBhTK4UOFrwlhZmmtijanrE28ZoU35ISKWc7OMJQPkhUbcDmyM8HYERZRMiaGfj02UVUoYlw0HcjNQs-8qET-w0br2tjtyLhFuA-t3NtKjwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
کرواسی
چک
🆚
اسپانیا
اسلوونی
🆚
سوئیس
لومتزانه
🆚
اینتر
یووه استابیا
🆚
لاتزیو
برزیل
🆚
هند
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72656" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72655">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=mC22jI1KkmICOsDfxPNd3wjeRV2AmI_H-2TDTAKQ1sWk1R_ksgdjng4Q4atQsadarUhFJ3WZxat9Vy3FMv0L_FRBnziwhJwJIQ2jizceZpjLahJIHN5_NND10Z8pww1aoblxc-dzgzRfMfCZOWLprArWKRfXiNxxvJahUoPHnjXJ6RX_5RugIT0miicyZJcjp2xQKWZWn-r5A6QJ4-SwLFIbw619EZ8zYQy2XdKNwsLd1LUCAxDifwFpyHMlGAIRhNj2YQd1_f8wlNCQpbuc3Ko4tb1Y18SpniVPvXf_H_UnqXjTXdbqUU5V196pX_ut7YdfZ1aJBfkwsqCT2bYvQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=mC22jI1KkmICOsDfxPNd3wjeRV2AmI_H-2TDTAKQ1sWk1R_ksgdjng4Q4atQsadarUhFJ3WZxat9Vy3FMv0L_FRBnziwhJwJIQ2jizceZpjLahJIHN5_NND10Z8pww1aoblxc-dzgzRfMfCZOWLprArWKRfXiNxxvJahUoPHnjXJ6RX_5RugIT0miicyZJcjp2xQKWZWn-r5A6QJ4-SwLFIbw619EZ8zYQy2XdKNwsLd1LUCAxDifwFpyHMlGAIRhNj2YQd1_f8wlNCQpbuc3Ko4tb1Y18SpniVPvXf_H_UnqXjTXdbqUU5V196pX_ut7YdfZ1aJBfkwsqCT2bYvQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
گروهی از افراد را دیدم با عنوان «هم‌جنس‌گرایان حامی فلسطین». بیایید یک روز آن‌ها را برای مذاکره به آنجا بفرستیم.
دیگر هرگز آن‌ها را نخواهید دید. آنجا کارهایی با آنها می‌کنند که باورتان نمی‌شود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72655" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72654">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵  @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72654" target="_blank">📅 10:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72653">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTpRnvZeoIs0ZwzYXArICyXWfaACnri_Z1VCSm9VE_C2eRS9FTf8Pm8jw0kKsEfozIh9L4T1IHttYD8Ev6hu9EOg3Ys2p2OwLtC8WMk_maiVAgGYTBTWXqDSkzq5EN8fWrl5IDXyPlNPWJ00esyBfQFKwelCfPQHpjMPeqrRs_77dzG7nBmypFR4cFqkf1CMF6i1c39isQfQCwbR0SayVCQ2DM8wUaUOrlzeUPin5XDGJuvLL23x7yWB_8i5yo59OJsVzctkHev5gRtzP53CfRYRnZIMniIVQy-H71UCycQ14cmEGmNBb8hFEZUeFtnIO3a2Mk3Rm76BjHoljB0mag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72653" target="_blank">📅 10:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72652">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نتایج کنکور سراسری برای عموم کنکوری ها فردا میاد!!
انتخاب رشته از دوشنبه ۱۳ مهر ماه تا ۱۶ مهر ماه ادامه خواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72652" target="_blank">📅 10:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72651">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9O9u8IAVqAs5TtWdEDxP8ymlYFsBpPNii_TFYJqkw3R6F3pQ0aiC9eIYfhqRTz7mzsrdjcQ2s_gxFYoNQN5qQ1zBBPBYLwjqkh-qwJfou5ss1sDle7ju8CsRGIEHqgenm3MUZh3ODVIrvjwTwY9TiBZOl_GwarrnuvAdaZPvPsXujfjc7dEPBpdrC68Am22BA1R9uDYcwe8vlqGi8wKmMcw-tDDv-R5a-HWpOE_zQJTyr7pE17zECLE1q0SG1fH1fNkeD2xHuhxKTdhNXnbJGjHjaRBrE98uV-Vog73Gc5Cu6sNgNAPtjzq7Y2ni8jyPfHwkPyx0rr_HhMSTrSJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خبری سنجش تا دقایقی دیگر!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72651" target="_blank">📅 10:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72650">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XZ1fQEhWW_ZZkjCmkHtMQ17tZvqCLZ6dfzimmI7T0l-d1wXxu9Ogyl4hLv2F2atYswsmg1Cukcjo6raIaTcK4b0qAMSTPXnV7My3h9SZyG5_43ccMkKxg8KYn4XyXriArUiZGTzj8kD-u1GJxI9bihBpN7QD3zBiUeqQpyunKjB52sLRj9JAWNkChhg1q38i_cqJdEsU_3uZ75CpjSBP16OJqP3oDOENB1235RSO8_FjEUNgeQnvC-hfhXlVoM0FKdifbtyAPQaB-ZLBpX2qHI8EEH9kIURQ0FPyrmCcDKZG7GyD-l6TXtJF90vqQa0nAd22stCGjkSeATEvgvuuFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ اکسیوس به نقل از سه مقام آمریکایی:
مقامات ارشد کابینه ایالات متحده در «کمپ دیوید» مریلند گرد هم آمدند تا درباره گام‌های بعدی در قبال ایران و انصارالله گفتگو کنند.
یک مقام آمریکایی اظهار داشت که در این جلسه تصمیماتی اتخاذ شد یا دست‌کم بحث‌های عمیقی پیرامون این موضوعات صورت گرفت.
ریاست این نشست بر عهده «جی. دی. ونس»، معاون رئیس‌جمهور بود.
«مارکو روبیو» (وزیر امور خارجه)، «پیت هگسث» (وزیر جنگ)، ژنرال «دن کین» (رئیس ستاد مشترک ارتش)، «جان رتکلیف» (رئیس سیا) و «استیو ویتکاف» (نماینده ویژه در امور خاورمیانه) نیز در این جلسه حضور داشتند.
آخرین باری که نشستی مشابه برگزار شد، به ژوئن ۲۰۲۵ و پیش از آغاز «جنگ دوازده‌روزه» توسط اسرائیل بازمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72650" target="_blank">📅 10:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72649">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=tw_aKRmDR6zceDKGw32AWFEbNHZwG6_74ryMh3BisYiiXNM2uYA9kc40Z5hZZlQRHJ94LG7wAcPGYDqy_S6ayyJ5qbyQLzZHJwhBMfg0WGt_RhLFw8FDmMxDOSvWiqp4EfC7YqNsj8bBKjQtJZvbU6Xc9iTGQCay_NnaY8UCgBWdWfca3JqkWHf6X-lkznqkhu0WXvGsv7PQtT6MqN6cXX1r0ZvyeBmSKr-Gg-wC4amIiUbfN-sD2uCXy6AJPLCnNC69iLnS5UY2amxNNzMGHi1_WNmdxWOcCndTPPBWSaEKQ4ERH81cjWR5IT3yfdEwVei657B5wXIKKoiMZwYMBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=tw_aKRmDR6zceDKGw32AWFEbNHZwG6_74ryMh3BisYiiXNM2uYA9kc40Z5hZZlQRHJ94LG7wAcPGYDqy_S6ayyJ5qbyQLzZHJwhBMfg0WGt_RhLFw8FDmMxDOSvWiqp4EfC7YqNsj8bBKjQtJZvbU6Xc9iTGQCay_NnaY8UCgBWdWfca3JqkWHf6X-lkznqkhu0WXvGsv7PQtT6MqN6cXX1r0ZvyeBmSKr-Gg-wC4amIiUbfN-sD2uCXy6AJPLCnNC69iLnS5UY2amxNNzMGHi1_WNmdxWOcCndTPPBWSaEKQ4ERH81cjWR5IT3yfdEwVei657B5wXIKKoiMZwYMBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ربات‌های چینی با لباس‌های سنتی عربستان، برای شهردار ریاض و سفیر چین رقص محلی اجرا می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72649" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72648">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An8q-RDTH9Wt0nKsu29N7sNUNeqfJKCRzV7phqKJ9v6CU7t_7rli4LtuhgaFvIFDCm_TazOPnXCwpoWcwdHt_Nzhaks9JIzH3ro57ij3t0OdERlPuyrEfwUmtfOUkTtcPor5SV26XNwwbHC5eC2aOTypmIzdP525dmnB3XylNTaAlAqZcELsDkqU8BVQx6uPiAjSxelZ--UcnhJVoGvOs8P-1AkykjINPrVp8ZQETLeXUP1BbcKpW0Xltv_0k0jAwREOO808GPGpfJATDnylYVch8s43-MLoHUXQd0QA9zN-onMS-r4TEYZSgiQ3TFzeKfqvYJNLanveor-0Mq8LMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «ای‌بی‌سی نیوز»، کمک‌خلبان شرکت «فلای‌دبی» که به خلبان حمله کرد و قصد داشت پرواز شماره ۱۰۷۳ این شرکت به مقصد اسرائیل را ساقط کند، «همام الحمامی»، تبعه ۲۹ ساله اهل عمان شناسایی شده است؛ او اذعان کرده که قصد داشته هواپیما را در اسرائیل سرنگون کند.
الحمامی در سال ۲۰۲۴، در دوران آموزش در شرکت «عمان‌ایر»، پس از کشف مطالب افراط‌گرایانه نزد وی، از پرواز تعلیق شده بود اما همچنان در سمتی اداری به همکاری با این شرکت هواپیمایی ادامه داد.
بازرسان در حال بررسی چگونگی صدور مجوز پرواز برای او در شرکت «فلای‌دبی» و تعیین وی برای مسیر پروازی اسرائیل هستند.
الحمامی با بازرسان در امارات متحده عربی همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72648" target="_blank">📅 07:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72647">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYTHsksHKWxlXprI7RnAqTE4us_JkrGA1yx8wpoUMujs209bRV6NRNC3BMYA-SlEhj6V1L_Fn1youigho8DB8TiyPh153vh2ehaeTeT98QowT2aKwvWyfccBJ9Yxqe4-gcT9UOc79DQB-rlBEqrf45dQ7a8vNuZ-D4Gx3EUtRnMc5hCMxiYMVW6RyHTEvRa4fMuv_iszOSjylynNrdpTbK5gun8xtC7c5rK-b_5ux3Yl8yF8R5zvyaNSsGZDg6E0wldl9gR8aUFlci5kawXuQdirX9waZnndLhHLavZxd40kv8o1ta4cBNyeoUcQOcDYxhPmL8aMLOiTbZCNaAB5sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟  ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛ اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.  @News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72647" target="_blank">📅 06:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72646">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72646" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72646" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72645">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5Tr-i_1YaTtGGqqlv-Jkdm9idkxYAVj717ErZ0cD3OhWpH0YQ-ixHdYLLs3WyYO3B8RuNU26wrnqoHNs9M78Qzj0gMDf7sNZE8E2ijOhgLNGaCUCvysovRDOONT3kPOatUrF3JxL7oRPZCtkVP1JupGEK0YDHP0_5VICY_DWBcdqlZLxmiG9tWaykdgvaxwsmT50QGMORt07THT-F6bVvAzljgsMZbKr6N17CPU_ewMkHwYMPlJnXZ70Uq1uEEGu0b57_Rq721ct91oYjK39Gr30dQGQnHgGPOflE9zHVlPC_KaI6MfmLz4Ene9Op7qIqZJ8Ijznhn2Toed0Qc68Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شماره معکوس تا رویارویی بزرگ
​
🦖
دیوسون فیگاردو در مقابل پیتون تالبوت
🦖
تجربه اسطوره یا طوفان پدیده جوان؟
​هیجان واقعی و پیش‌بینی بالاترین ضریب‌ها در
TrexBet
!
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/72645" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72644">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=YNQtsypeuP-rhw8zotIVeqYwjpk2ol7fvUw4RYISxWMwMBdVTRUdwBjC5r6TItSokWW8YKaKg30xmNxEQfExgENdU0uoL6nI_k_LBHQWoz1v00NvJ_BvHweekZkn4Jf_ohMBbC1YYng3VA6jaRga6NR2hNnNt0vjiJvTYtxOHl63i1tK-kcwOTpLGMEPNN2RyShZCLdrCT58hAjg-GvKTHWDzbqnddPdMI8t4aXjWjqvBSX1sKQaO9XRlsXJBAYMn7FcYPDiKilDYMNmwc-qqDNDcY80AmKXWMBLGytAp1EIJ5n6emmAqt_4tGfigOkW22vYxJoTz5ysHW1urHQByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=YNQtsypeuP-rhw8zotIVeqYwjpk2ol7fvUw4RYISxWMwMBdVTRUdwBjC5r6TItSokWW8YKaKg30xmNxEQfExgENdU0uoL6nI_k_LBHQWoz1v00NvJ_BvHweekZkn4Jf_ohMBbC1YYng3VA6jaRga6NR2hNnNt0vjiJvTYtxOHl63i1tK-kcwOTpLGMEPNN2RyShZCLdrCT58hAjg-GvKTHWDzbqnddPdMI8t4aXjWjqvBSX1sKQaO9XRlsXJBAYMn7FcYPDiKilDYMNmwc-qqDNDcY80AmKXWMBLGytAp1EIJ5n6emmAqt_4tGfigOkW22vYxJoTz5ysHW1urHQByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟
ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛
اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/72644" target="_blank">📅 00:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72643">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ساعاتی پس از معرفی رتبه‌های برتر، کارنامه داوطلبین برروی پنل شخصی هر داوطلب در سایت سنجش قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/72643" target="_blank">📅 23:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72642">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طبق گفته حسن‌پور خبرنگار خبرگزاری فارس، فردا در نشست خبری رئیس سازمان سنجش رتبه‌های برتر کنکور ۱۴۰۵ معرفی خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/72642" target="_blank">📅 23:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72641">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=lt5RHW00ovzVCahTdwobqebVCa6tnAdzasqODOgep8DrpY8-74S45rsKIop52PiUQ-VWjLoj1a3S52ksrc4NmeF3F_EkbgptpKXryxTSem12qEr5XhRiwd_AjenpCS3Ui-DHHARU1IO_HWOJseXBiM4ldpKR13Oqno544iThQIz7R3pYfCgF1ZcpgDiH-z9aAv-QT_njumnKLW8yc-6VxK9xUPfDosWVVROS9zT3kCPLucFA3vGsHqByUda5f0zHLn8asdnxectU1oPp-OdWJWftiwzJJ8IAJ2ogq7DZdCgE0J75zEQzSbpN1uxhDmStE8vSdKEu-eG95UOM3zRERA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=lt5RHW00ovzVCahTdwobqebVCa6tnAdzasqODOgep8DrpY8-74S45rsKIop52PiUQ-VWjLoj1a3S52ksrc4NmeF3F_EkbgptpKXryxTSem12qEr5XhRiwd_AjenpCS3Ui-DHHARU1IO_HWOJseXBiM4ldpKR13Oqno544iThQIz7R3pYfCgF1ZcpgDiH-z9aAv-QT_njumnKLW8yc-6VxK9xUPfDosWVVROS9zT3kCPLucFA3vGsHqByUda5f0zHLn8asdnxectU1oPp-OdWJWftiwzJJ8IAJ2ogq7DZdCgE0J75zEQzSbpN1uxhDmStE8vSdKEu-eG95UOM3zRERA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر گوگل‌ارث با مقایسه وضعیت در ماه‌های مه ۲۰۲۲ و ۲۰۲۶، ابعاد ویرانی در اطراف مدرسه «القادسیه» در رفح (واقع در نوار غزه) را نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/72641" target="_blank">📅 23:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72640">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=I84MGlLJnK5ntFSQngY10c_bTa7ZS9wgekMBShduBUzHEqOfwqezj8PdYWXFRkHxj7n3Vtzpr0HiX6OJ-ORrbGutSHR3wxc00hOrBg2zxF_a83rjaazwq1v0rJ8djf6td1ilHbR2FFH7IseawwIq4PPSzQqaYaATlUgTjqrdHXfaWg7JfycK9OpFz0wGTLno1hHrbVZ5tlWaDGbbi_sJKbXm0AKvz1aR6yjJ3IWl4h33tmykHDghMrB8DF4cqREvotwuxRQ3Xdbl5JUWNyDk-U4OS7HHZJEaUZ_NWxPjl1Tq8CUCMFOWtDW0Yp9hSblJtc6uWTYj24h39KYKhRyMIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=I84MGlLJnK5ntFSQngY10c_bTa7ZS9wgekMBShduBUzHEqOfwqezj8PdYWXFRkHxj7n3Vtzpr0HiX6OJ-ORrbGutSHR3wxc00hOrBg2zxF_a83rjaazwq1v0rJ8djf6td1ilHbR2FFH7IseawwIq4PPSzQqaYaATlUgTjqrdHXfaWg7JfycK9OpFz0wGTLno1hHrbVZ5tlWaDGbbi_sJKbXm0AKvz1aR6yjJ3IWl4h33tmykHDghMrB8DF4cqREvotwuxRQ3Xdbl5JUWNyDk-U4OS7HHZJEaUZ_NWxPjl1Tq8CUCMFOWtDW0Yp9hSblJtc6uWTYj24h39KYKhRyMIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم میخواسته بره مهمونی و لباس درست درمون نداشت؛
اومد تصمیم گرفت یکی گرون ترین لباس‌های آنلاین شاپ که بالای
۱۰ میلیون
بود رو سفارش داد.
حالا چیزی که به دستش رسیده :
میگه این چیه لامصب؛ من با این برم مهمونی میگن خرم سلطان اومده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/72640" target="_blank">📅 22:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72639">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=MicbOP4XeCZpv9IG0zrKtJkKYdw2EWapzeyw9-9aOzkQTY_fX2QLPGZqaUgK9y-V_5f9mQfHDg8SZuWE7x1mQsViV8zATO9YwKduwu1NBFn5H35xoWg4MYm8o3nUs1Lkx7bfsUgVs6o9VGhj1JeTsFaEi60hj2FUMOMtykHSkUov_qROyQ-UevNmWK2Zg7SdOYml3i6f04CAcMmv2gf0WmtkhshBV8_XEKeqDUw8ZUow1GypfZqwzSEM2EAC6HeTmKAj6zPmJ-binFFWFI1-8nJn7kTPrz_Vz6XpqNnzXQSi9dU3MjO3gYjvlgj6fKzcD5yPv8KaDr5wWhvPT1DGUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=MicbOP4XeCZpv9IG0zrKtJkKYdw2EWapzeyw9-9aOzkQTY_fX2QLPGZqaUgK9y-V_5f9mQfHDg8SZuWE7x1mQsViV8zATO9YwKduwu1NBFn5H35xoWg4MYm8o3nUs1Lkx7bfsUgVs6o9VGhj1JeTsFaEi60hj2FUMOMtykHSkUov_qROyQ-UevNmWK2Zg7SdOYml3i6f04CAcMmv2gf0WmtkhshBV8_XEKeqDUw8ZUow1GypfZqwzSEM2EAC6HeTmKAj6zPmJ-binFFWFI1-8nJn7kTPrz_Vz6XpqNnzXQSi9dU3MjO3gYjvlgj6fKzcD5yPv8KaDr5wWhvPT1DGUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره سر صبح رفته گوشی داداش ۱۱ سالشو چک کنه که میره تو پیامکا و با همچین شاهکاری روبرو میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/72639" target="_blank">📅 21:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72638">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDWcxzpzcr8SVc2Ir6imKVSH7TNnW0ZfWLs7Zj5NrAEX4ZCcpvIUEUUWab4R9Z5UEVEJss9UrszSWeMycmWMefJK8DfQ7TOzjusN-1BTsVNdbJJzA5SpQ8OwAwnZvG9bzOqtWBGZrHICI6qR7xUnVtz0cZ6tTjKE5-MYMRAGN8y7_aoNLxzwbJ5rZxB8nqVRQgXZBz2JrHhOiBhac9FJHm0cjkluPjx-tmr6FwJuPMrHlKvLkrzibV-4YVP1tpFDoSdqUeHQGSqeke5VsnASn19BYtZW0t_b8qqngVbhiS72HR6tJyojNdYSz8jY2aL28CDLCtWF208PYcA3LvFsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که ناخدای یک نفت‌کش گزارش داده است این شناور هنگام عبور از تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
در پی این حادثه، آتش‌سوزی مختصری رخ داد و برق کشتی برای مدت کوتاهی قطع شد؛ با این حال، آتش خاموش شده و شناور به مسیر خود ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/72638" target="_blank">📅 20:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72637">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72637" target="_blank">📅 20:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72636">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/72636" target="_blank">📅 20:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72635">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=ukkUWz6rqwV1ETjL8wB22PWkKoCqwsDYRDFxsfGnqT1gOCOgzabWDK0KKCiPw1Ty5X_2U9s2D8pCpxmVRm4aHxKOJNVhYHe-kDyMZDmFM5gkl8N8k27wgEs4MvVHKQl14l44ZjNpagFo2aaYVIoTyRgpjn8w1H6RWnFJKIaQZrQLAsBzYVQ_7BN20c5GCir7ehHn7neXMwtFwqonwRS2BV7zF6c5ITes0bcO6wZIOXG40NnERc-DbMxJI9Hmkmndkhb5l4w1Wpb5YR9rR1RR6EyoAALvPPf18Y1j9UGBoLFOphM1811RSyeOPKXW1a_xFiSN8n9uAqqkPpwolZ-IXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=ukkUWz6rqwV1ETjL8wB22PWkKoCqwsDYRDFxsfGnqT1gOCOgzabWDK0KKCiPw1Ty5X_2U9s2D8pCpxmVRm4aHxKOJNVhYHe-kDyMZDmFM5gkl8N8k27wgEs4MvVHKQl14l44ZjNpagFo2aaYVIoTyRgpjn8w1H6RWnFJKIaQZrQLAsBzYVQ_7BN20c5GCir7ehHn7neXMwtFwqonwRS2BV7zF6c5ITes0bcO6wZIOXG40NnERc-DbMxJI9Hmkmndkhb5l4w1Wpb5YR9rR1RR6EyoAALvPPf18Y1j9UGBoLFOphM1811RSyeOPKXW1a_xFiSN8n9uAqqkPpwolZ-IXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش تاییده خیالت جمع برو بگیرش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/72635" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72634">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
😂
😂
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72634" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72633">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عراق اعلام کرد که مجوز معافیتی برای انجام روزانه ۴۰ پرواز توسط شرکت‌های هواپیمایی ایرانی (به‌جز هواپیمایی ماهان) به مقصد فرودگاه نجف و بالعکس دریافت کرده است.
هدف از این معافیت، تسهیل سفر مسافران و تأمین نیازهای بشردوستانه و پزشکی است.
نخست‌وزیر عراق از دولت آمریکا بابت موافقت با این معافیتِ درخواستی تشکر کرد.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/72633" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
