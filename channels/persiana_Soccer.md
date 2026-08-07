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
<img src="https://cdn4.telesco.pe/file/qNKmOWaOTHMpRDljFzFWi-hyllUcRe13pJSn0i9BJ5_DvHowBMQwcSOnzq9jRKO0oLfpi5HsDPDf3xbVo54lijep5btRql0_7OPBnfgbH04_v3tch8B1Q2AokweTxmDIBpKu38wiYK4-sbquIVun9rnzqU9LvR5mWrQbnRY5X-7obhfDCFUcBc2lxxzYwFnsc7YrV-mP-WOFwYKmClypZY58glGY62jSEw0IGHm-P3R7HaxrBogKotbicYNwnBBvuhYnCH3JPniZnFRwjXtEevNNzWpI7miwq-BE97ZfBORFAfG_B2OKlP8HiXcPDJELwB2d89saCdeZmZ_Bxs6ctw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 633K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 10:11:15</div>
<hr>

<div class="tg-post" id="msg-27246">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CswQjuCNJGW6jGllHrLadVgoJZpxbJ-676qdpb2PaDBCcpLLliRmWBBAgCe4ODHwTXKRwU4t47x1N9E3Pg0XgaoIZSFlFcpE7gEPmYlwOL9LEsyVjcqUQT2Pu7QWaNbRBP4TiF46iM8UnBKqVkJzyubRTYyRCIcVmGLhsGGUVCFQxQjncpiQ_oam0KZxN6hMZcPJLVu6K0eYTQCYHUqzVfz3fqIJsQrQn7YOagq7zNPinuvxFFD9dweuoQRRFdKYT1VrK3DJPD6JhbZTXyC8B0EGn1qRCvRMhTSSHLiVYF8pRi3eSyoFmAH_maFHQOzTrHDZikWnWcx7nQjP1HjTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه کوپه: انتقال رودی به بارسلونا نهایی شده. او دستمزد بسیار بالایی در بارسا دریافت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/27246" target="_blank">📅 01:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27245">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3UvQO9sJ6X23UQ_Y53XgT07caO_7sjrBOURe7ypu5_RYOu-rClZ0vx_FsUOOhk_GEbRZreHIuiQbh5Iq3oHiYNnHhuOJ17XeypKKg5KX1eBXHXy41b4vL4ml4szz4b8g4gWyUxgqKBiE6G0d-Jz98L316YZ57Z7yDKyUSAzoXHXVy4dcX2Nm0aucoLKl_GKuUjvSzdDj48zMUOgoyM9Qrj1ac4wmpEzGzhyu8u717HFTsWQH2o5vcVnrpFgSW2STG29sk_AzN3nP_-YwGFesoZO-BCGFlQ-DDs9d6cRlNPDh8rhqDSFn2d3eNCB-2QaKzyWYCES22iWXu2wNBJxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
🇨🇮
نشریه‌مارکا:باجذب‌یان‌دیومانده و تمدید قرار داد وینیسیوس جونیور رئال مادرید به احتمال فراوان دیگر خریدی در این پنجره نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/27245" target="_blank">📅 01:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27244">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a50e09f5.mp4?token=M_4oi3XmNGOZ--FX_aaFaUdEUBH-KUXJ4Mw2hcs8mdBGNUUoAwaGlxu0nE7g8iE6__bZF6TjXz8JEC09FDTJVbVQ88Tqm5lWm4-58mEFsnUXerlOztYNEwLMO2xNmZGaitrCFoGIQ-cHJKAC_RbTXrBbpv9VIVSY-dd-wqyYrFXGcPCWVeHNIpomZd1O4VJjUe5uwbt8vWitCk8Dyd9yW_2NCbGOkGE93dPov9EajmNEh2HncFpxIveFZ9F-xKi3z8wnzk9M5oVw3-e6nBI9FPWmtQofZbIMFZdQ6T_CWRc-6zBw9kojGLpeFF0_VUap9X5lbDUA_iGCMkCb3j2egQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a50e09f5.mp4?token=M_4oi3XmNGOZ--FX_aaFaUdEUBH-KUXJ4Mw2hcs8mdBGNUUoAwaGlxu0nE7g8iE6__bZF6TjXz8JEC09FDTJVbVQ88Tqm5lWm4-58mEFsnUXerlOztYNEwLMO2xNmZGaitrCFoGIQ-cHJKAC_RbTXrBbpv9VIVSY-dd-wqyYrFXGcPCWVeHNIpomZd1O4VJjUe5uwbt8vWitCk8Dyd9yW_2NCbGOkGE93dPov9EajmNEh2HncFpxIveFZ9F-xKi3z8wnzk9M5oVw3-e6nBI9FPWmtQofZbIMFZdQ6T_CWRc-6zBw9kojGLpeFF0_VUap9X5lbDUA_iGCMkCb3j2egQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌فراری‌قرمزی‌که‌پشتCR7 می‌بینید، یه فراری معمولی نیست. حتی اگه پولش رو هم داشته باشید، لزوماً نمیتونیدبخریدش. این‌مدل بصورت اختصاصی توسط فراری برای مشتری‌های‌خاص و خوش‌حسابش تولید شده و تعداد خیلی محدودی ازش وجود داره. حالا اینا به کنار، نکته جالب ماجرا…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/27244" target="_blank">📅 01:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz2Sl3kHYmmjiwvjMGtvfgY7K6Pq3hOvt9wAHEuXvcAVL_VoxJRgjqVOu-hoB0M2NQrwshV97FVdpVOBpc1nC4ctMZ-IW9KBKs2u3bYy7zhX8RJXHuGGvd7zcb8IGm_k6YEU57dgXxgI306jvZteQ3VnGJ5eh9UNlr-7j2Z2D-ni0prgkm98AyDz1h1k-pOu0pzc2gGSjUc8ifkx_QOg_fkHhdrlsZafmInQBHFJcvaBqKyVe-HU-7gH1Drukt3P-oRT_D1BRyD-HAFxSYlRKsEP_G9p0eUABXYzzMVpt-nUkW7-bZ9apjpd6YiewyxBxCfkRv6WNdBqnx8fH7WxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/27243" target="_blank">📅 01:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27242">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRnB36yFb1ggsa0G32jwsfCNKWkWV1a98Fh9nQaynFiYOtsy_LvO9WOi3JlxVnV4r9Ex1GsP7UkP2hINPYYM38BRRqyBcHFUjaNgyeOW7gcYzwp4EgSMFqRgCk787PWiL0TQyCtf0pyPBmVLTOQwtTljRQAGiXGY1A12YLm5dedl6U-ZXLFMWDKkT696F1xBFr-0DpDn8q267pqVNL6vb-F3h3Frqr74RqsSnIT1Hq8DedCs6_dCcnagBj-02ghKXyn9VoSz18Qnnf1XMDZ3AzVYfoVndisJCxxY8jnF8LV0gWittGWc2-i-aLXQHJqoQNhBG44WbWqigEUaM0vnvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/27242" target="_blank">📅 01:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27240">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZmzlUstei67Iyg3qDp0FC1UNzp8EIP4YMscxseu8hBIIsLWk6dE1399DvTCP5bO5_GR8MExoRKNIa4ypv_S3yyJqYl9ffzOiqnLtFi__aEogLKqSn1LnWLnQsSqr5FQq_Z14PXqk0lI50y7tkLEoe8OE2TMErus_C_30o5Wh0qyEZiSn9XJQP5bK8bv66aayduCX6fLP5_n6EnSBgz3G1nRlTwXAkRqNnGOCUA1isncx5fMx4OF9ooTJelkj17cuEGjJpb8UJJwaAU6BJO7Zd02Eywj_6hRUC-4JYc2KqGhEyk_PVKGE24d2Ac9S1N2QRhyOprvCehEPkjjqfVVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها مسابقه مهم ‌‌‌امروز؛
دوئل دوستانه و جذاب شاگردان اونای‌ امری و کمپانی در هنگ‌ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/27240" target="_blank">📅 00:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27239">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT7pSF3w4rGbkIJajQ51EDliRFmB0ZgESnjsz3LJ_tHWjg_XBbqAGY8msIM_L7NMQQRSX7uOAcPL7aL8SNGcDrhKRfCvFLtKibDn0-jd76QjXW2IoLMyPieGYsKF7NDRYpTORQ33blBz-EtsfIp9MIJafuAxzrIQfXg6Yn78qioai9TipaCRAWzp4UHnAYP-MpM8JUGOBI6q8cWUXKTGx7Zo71PRosvlNShxnCSBVM3sO9AwTX1Cg6NcsTo3NvPZOvGBq7UOsu8ztL1eQCjSyR3X1iyf8WLbTTHaSwY5YthOhJJJyC7fMZ09KdOAxaT_dDek1PkiRz5geRgZi4qzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
برد اینترمیامی با نمایش درخشان لیونل مسی و ثبت دو گل و یک پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/27239" target="_blank">📅 00:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27238">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc_gAgRNBvcvsmQLh9aEZJWV2vi9dNLG9df9OGqXDYBd5wS70jUTs98tzH__b4yYZlGOOLaJPnIf7OZGUInoYJAWL8R9-ByjGt7C4NkmCMJpL5NSBNxysEXq3GRrrEz2IAgrvu5MRCDjVzEy-292IHB1uIkwKpSHUnQfwrkPe0qFevNERAALJP-oNstn1uigcw32DFznp9xIMpLjeU428EpzWC1Fu-dcZ9kfowpOOmIaKCjHiNMnfDJaj46WIBrNatdDWO22MwWwN29FYN6Jh-NQejN3pe6_2XZuQFwDEUYeofCV11QoQdvnsvxuEgpIVQjAjRFEDgbEIQERawe85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/27238" target="_blank">📅 00:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27237">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-IY3vgS9Z9jq3zIk_SJAHJOtD6i5a4aMOUiLkfuBCTi6hccA-x0sN6spTU-3VqbpscGU3JOWG6tW6AHJAd-el8b4IW4-QQv5J9q8FzyVyNz4KDx0cCVihPiF6ub7fui9-RT8AwGqDFVwANY_jy6pGYswlxUy60_ifb7SoVKEJpxrJ04OFVRXf2p1m_sD_tIv8PJ7Yi8Z3iOQWxeFSpHPtcHu5C1slofGLC8Ou6DKadf_TGimVwnY12fHFtLHg3iigjowoOU4MSjg9X_pSUA7JP_PrvaLnIp85v4a4bNsml3Ke09eiNdrSr3jErg1P4kWy0IoBsoJBXYtJYUXR7hgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور بعداز تمدید قراردادش: هشت‌سال‌حضور درسانتیاگوبرنابئو برای من کم بود و دوست داشتم شش سال دیگر در برنابئو بمونم. شاید اگر شرایط همینجوری فراهم‌باشد تاابد اینجا بمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/27237" target="_blank">📅 00:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27236">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUU1P2ZvzToCtqyGBoe1CY_-Yezo7XVK0_i_zay2AlZkMNTJ_6RBBxwLFRzmgK1BKttouRU68JVPuIst3abrdwWNJYVwUtnq7AsRAS0y6xoMVCsh7RQDmGVGesDVaHUP1wV7sPSDGeT9bKP0pWK3BczsNWg3Cq2WTFrj1CBAFL9AA9szSM2HA8P6-GZFEPRVVZj2i9p5lFXf3hsHknB3SyrgEnTGgpHyinzoo7xFApIuG_k3O903DcOMDqgL__E2MGwDpszwv6YcX95L0YtifE9ttzVSXwCYGAdaAS3ogemcTEDF5oFJhDzjpFMoNecwAO7gJTY5kXevhLsC2Y819A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متئو مورتو: رودری ستاره لاروخا از صبر کردن برای اینکه‌رئال‌مادریدبامنچسترسیتی به توافق برسد خسته شده بود. بارسا به او تضمین داده که مذاکرات مستقیم با سیتی را آغاز خواهد کرد. هانسی فلیک با رودری تماس گرفته و این بازیکن به او قول داده که قید حضور در رئال رو…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/27236" target="_blank">📅 00:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27235">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbaK1vfh-SXzQirTme4euouJYoDhY2sjk46N2JYkBUmZZB3xeZBwgFD017gF-Ho3r8d3Z6J-jX1dP625TVxLro_idoZMDjLKppvVQETVQ8pepcmNb8Taa2uCUsv74hlPQrdCf_1Wn2vmfWngSwMnewcPfYZN7JQUwnnzm6RHZuC_zISuGebf4V7h0J895qdFe1QfHxhcR938-jqj7T2gwJH2gzY7kWtffk0wnQe5Uh7mzgjsctR_T6oA81YWJr9oqg2KC45bBv5NiUI-OUUKg_Q5GTPphSBJzntpXUvTEVOizi9n5xS8CaQzfZDF9NQ5_3ZCYhzL6yS4kIyKhm03_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور بعداز تمدید قراردادش: هشت‌سال‌حضور درسانتیاگوبرنابئو برای من کم بود و دوست داشتم شش سال دیگر در برنابئو بمونم. شاید اگر شرایط همینجوری فراهم‌باشد تاابد اینجا بمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/27235" target="_blank">📅 23:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27234">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqFAt6S20rG_LnA6u5toUVXZ416gRU6mnNw9QEEdTeKoGwJoh-xDZ6Po3N1hoKtp0qPVnojVto49MsKsdU6XvZLc5qbF4VXV0_8l-CXd_YHzey13ytQj8tcoGL_-B-ARz9yhRy4uhrC9zkwA9Dam3vFL0vuh8yw0v9mPkf4DXHlydwlWZGxGKfArWtAV52FG8GS-ZQqq25wa2qPIsd63PI3wT_-L6kSWPWI_pSKwdngT05TzZajPiIFDqaxXKj1uUFhSA-me1s4fgyWWkoYVVlt1JFP-bZ75V1eVOEf237P3NS65flZZlaXdn1ElyfVVTaIBoM8Q04tJDN5QPV3Lvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛کادناسر:پرونده‌پیوستن رودری به رئال مادرید بسته شد و این انتقال انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/27234" target="_blank">📅 23:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27233">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e40f288f69.mp4?token=mOxQHbcLoMTzGc_8lnyTGc7LeG0V7fnnG4YkUzARZ5IC0-mx3d8DV3o7dymr1CzqzOEJq4h03TYCR2g7okESXIP1ia_JSsnoXLZUCgS4RSo4UXs0pIlotwvAO36gQxqBcxrao0tO2pkGSVSJuu68hPMBwkr2Rhk0YfWIqsKfdtnf11fHDtM_2bVRcLTM1Im7pRJI-c0WGWZH_mdaM5Sm9kGpOB059HEEo78Z8i9gmEq3Z5IZxtBgQ1_qN8P1qu0dzXLT9fyA8quiAOpHPYagwbPY50orWZUEFZwEZ6kIdoa1fFv5TXsE3YafZJQe8agp7I0v8ACOyt2ywjoG8z8Mqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e40f288f69.mp4?token=mOxQHbcLoMTzGc_8lnyTGc7LeG0V7fnnG4YkUzARZ5IC0-mx3d8DV3o7dymr1CzqzOEJq4h03TYCR2g7okESXIP1ia_JSsnoXLZUCgS4RSo4UXs0pIlotwvAO36gQxqBcxrao0tO2pkGSVSJuu68hPMBwkr2Rhk0YfWIqsKfdtnf11fHDtM_2bVRcLTM1Im7pRJI-c0WGWZH_mdaM5Sm9kGpOB059HEEo78Z8i9gmEq3Z5IZxtBgQ1_qN8P1qu0dzXLT9fyA8quiAOpHPYagwbPY50orWZUEFZwEZ6kIdoa1fFv5TXsE3YafZJQe8agp7I0v8ACOyt2ywjoG8z8Mqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میلادمحمدی‌که‌ازابتدا در ترکیب ویتبسک حضور داشت با دریافت دو کارت زرد در دقایق 21 و 33 از زمین مسابقه اخراج شد تاویتسبک که 1-0 نیز عقب بود، ده نفره کار سختی برای ادامه بازی داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/27233" target="_blank">📅 23:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27232">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f42e1af.mp4?token=E0TROxMe53BdLacLnasei9RdAQQQoXMVjCFFswsIDBsRlM2UUamX8Uas_OodVcroK9i24O9UOjCnkXDI6Up1IV8pCOXh_fQHGaXJnIPADyjpKfZsgTw0p9YPRYieNZXfArYShBIGlhPrhE7EZeuIWGruJUgP-xSlsxnLNFJ3Zz-Js_hxtkReRNWBoM2inAHh9BrUH9Dq8OzUb6NCqM4_YOUF64qUqo-4srIKiwmPa7guN0lOJzIbQf_JXnjV6xJGgZkryDjWedia7RAUDgqj6ILlaIcmJGCZaceWqC3wuTL3LW-ipScZa7Bl_qKO3ByBkpJypRgsox4XML5rT2-4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f42e1af.mp4?token=E0TROxMe53BdLacLnasei9RdAQQQoXMVjCFFswsIDBsRlM2UUamX8Uas_OodVcroK9i24O9UOjCnkXDI6Up1IV8pCOXh_fQHGaXJnIPADyjpKfZsgTw0p9YPRYieNZXfArYShBIGlhPrhE7EZeuIWGruJUgP-xSlsxnLNFJ3Zz-Js_hxtkReRNWBoM2inAHh9BrUH9Dq8OzUb6NCqM4_YOUF64qUqo-4srIKiwmPa7guN0lOJzIbQf_JXnjV6xJGgZkryDjWedia7RAUDgqj6ILlaIcmJGCZaceWqC3wuTL3LW-ipScZa7Bl_qKO3ByBkpJypRgsox4XML5rT2-4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره‌میلان در مصاحبه‌ای جدید از دوران مدرسه گفت؛ زمانی که یکی از معلم‌ هایش آینده‌ ای برای او متصور نبود و تصور می‌کرد این شاگرد پرجنب‌وجوش به‌جایی نمیرسد. اما زلاتان مسیر خودش را ساخت، در بزرگ‌ترین تیم‌های ایتالیا درخشید و ثابت کرد بهترین جواب به ناامیدکننده‌ها، تبدیل‌کردن همان رؤیای دور به واقعیت است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/27232" target="_blank">📅 23:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27231">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1Sgocr8K3lV4p8xf-WLPPEZhGZzzADGagy2j3jUQNjZzLw-pDdMqeKZYbwQSuULcCN-lgeZ6mkoUzXCAVjCJh9hCGWqr5bBbPXn0LUh6_gtKOFTABiHeF0txUXBbBp6PNC__WPv9tiCF9ySogDO9LGcZ6VMYF7kRPqhG_Ko-qumeG0PsHMCBYQnnqdg7NwEvbT1Ai_pbeUdVHse6rregRvrjO6hJTDq13wI0YeZCpRiJGxLh3gBLZU2CY95YPsvYr-cvSRFzKbb90Zg1ujy3kJOuAMcktnFsNo8PKU2GcHaM1des8O6sWEYXkS4U0IKcxNfSFgppTBJgrw3P_BJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلطان‌میلادمحمدی‌متخصص‌اوت‌های نامنظم تو یکی‌ازمهم‌ترین بازیهای تیمش تو پلی آف اروپایی تو ۱۲ دقیقه دو کارت زرد گرفت و تیمشو بگا داد:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/27231" target="_blank">📅 22:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27230">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902ccfdccd.mp4?token=Bwid9Yg3lZ_bC1n3yjhQftqkaHLDTM0ihJP3bhw9lc65PZf2lbirUSxvMvFth02-OQIzL24JYCTyqhP1C4xde4FPvy4sYurypy8qeWS5wgFWdIGngjXfYcZ0fMr08ys_yisAraA7rFapOCj1RNJymwkHmTryyPPRfQ0XgAi5vKUiphvet192yFeyNuZp54VGtNUJcJP7jNmJ1Jjq0wFavZuBWN9ZrsMzCkGsmHnKQHNcrSPFH5rMAtYAy_oL-7fPx6P_HNZQI_zFg-vtLXtAgXazP10Suby8QwEin0xAtxJp5qY76fcvlxlssPUOil0Jp-Fi17c2lV_Ls9oTI66obg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902ccfdccd.mp4?token=Bwid9Yg3lZ_bC1n3yjhQftqkaHLDTM0ihJP3bhw9lc65PZf2lbirUSxvMvFth02-OQIzL24JYCTyqhP1C4xde4FPvy4sYurypy8qeWS5wgFWdIGngjXfYcZ0fMr08ys_yisAraA7rFapOCj1RNJymwkHmTryyPPRfQ0XgAi5vKUiphvet192yFeyNuZp54VGtNUJcJP7jNmJ1Jjq0wFavZuBWN9ZrsMzCkGsmHnKQHNcrSPFH5rMAtYAy_oL-7fPx6P_HNZQI_zFg-vtLXtAgXazP10Suby8QwEin0xAtxJp5qY76fcvlxlssPUOil0Jp-Fi17c2lV_Ls9oTI66obg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇪🇬
دوویدیو برگ‌ریزون‌از استقبال هواداران تزابزون اسپور از محمد صلاح به محض رسیدن به ترکیه و رونمایی باپیراهن شماره 10 ترابزون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/27230" target="_blank">📅 22:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27229">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHLSALPyer_M-NKpKCQhzKQ2-6boj7li95lwVOGDr0qx7KrzE6WMlqYkFyp3Zlsb23yo2Fgdo4PCL_HJBscZERqGMJBR_VWKYwGI-d0sL6DYREvTejOrjbX_0WvH4Cf3hlStKEEm0E_alK2JHquAot2Bnbhe0LotBHHVEhgpDPWFjXWGo5SqthRZbUr758DkQZIqlJKCU0VxZYoUQIF1oXdGO-Upxx6u5850S4ZF1hFN6tFDR2glX3C7-noNYr1EHzpZAJmf0EQ__IyNz7fcAHyXcOdQiK7w00Rc6zhua6qcuVR0e94iT11t91wRTgqoRFuYCbkvR_BXcxumY1ANfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رونمایی رسمی رسانه باشگاه رئال مادرید از وینیسیوس جونیور؛ وینی به سبک یه گلر ایرانی دو هفته رئالی‌هارو بااخبار رفتنش به آرسنال اذیت کرد اما بالاخره قراردادش رو شش ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/27229" target="_blank">📅 22:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27228">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86333d6363.mp4?token=kVKGiCa9bF_jPlhJ0zZPn4AefWnC1mxQ1wsSYvxizGvLcftrlw2fd-V6hPGKoA9fh4j2YhuyCKtrBoKsoOkX_dm9maOmLCLTJMeaA_Q5GXJOe5WU0BGnvBJsvoIbOqabuSn9jTMb-Bsw-UAsPfvkRdkFOpASNwAlMlus5z4UyQjkSkCuTgTpVADBhM6u6InocX27M7gxonsKK4IH6nrx4SyjYXyf2EGMSNhtspIreMAiO21F2-B8meawcSjPgdCMPEApzW_XB8mkzTN7Uy6H9J6m6R0tW0FAywtW3f2P76ZV7MB36r0eSaLGC2mBOnVNiMyT9nDEWYbgojchJm63wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86333d6363.mp4?token=kVKGiCa9bF_jPlhJ0zZPn4AefWnC1mxQ1wsSYvxizGvLcftrlw2fd-V6hPGKoA9fh4j2YhuyCKtrBoKsoOkX_dm9maOmLCLTJMeaA_Q5GXJOe5WU0BGnvBJsvoIbOqabuSn9jTMb-Bsw-UAsPfvkRdkFOpASNwAlMlus5z4UyQjkSkCuTgTpVADBhM6u6InocX27M7gxonsKK4IH6nrx4SyjYXyf2EGMSNhtspIreMAiO21F2-B8meawcSjPgdCMPEApzW_XB8mkzTN7Uy6H9J6m6R0tW0FAywtW3f2P76ZV7MB36r0eSaLGC2mBOnVNiMyT9nDEWYbgojchJm63wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇳🇴
دو گل استثنایی و مشابه هم از ارلینگ هالند غول نروژی تیم‌منچسترسیتی درلیگ قهرمانان اروپا؛ باباش گفته‌شاید درآینده‌نچندان دور این فوق ستاره نروژی رو با پیراهن باشگاه رئال مادرید ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/27228" target="_blank">📅 21:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27227">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🟡
👤
وقتیCR7 از اسباب‌بازی‌هاش رونمایی کرد؛ كريستيانو رونالدو با انتشار پستی در اینستاگرام از ماشین های لوکسش نوشت؛ اسباب بازی های من.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/27227" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27226">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPCfVXTWvnXe9oU4oFZi5P6XX-lPvwVCTPE2IWrai8-jdy78W7qwgOG6sh2ejscwWR-Cb21YPzkrBnhUyE_EXToQZLF3asOaHlPjqEttPG2btlNJPl3xgYbap2rkStEVqWb2IsnVeKjtBeMwxLN90PxPKY2iHtGmtEniUdCvba_eNn-V82DonPhNoyo9bWYZsbcAWZDNGpg6WtGF40y0eDI0oRZUBCTKmvktv6-uk4pQnHC3fL2TC1brajXHf5p84qqwhOOyHsGQ_R48nRXXhOCYpjtuFj-7gKQZxpPj4kYGUGntUhONaJxt2fULj_7EDFbbHnEsj6Uuu6_6K9pfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رومانو تایید کرد؛ بالاخره بعد از کش‌و‌قوس‌ های زیاد؛ قرارداد وینیسیوس جونیور با باشگاه رئال مادرید به مدت 6 فصل و تا سال 2032 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/27226" target="_blank">📅 21:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27225">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQZTZZk1djOGxPjz3hBnmRROtVH5Bi0sRxs_S8N0UqMDxPRBcCBzN8A2W1cSr8pWVXsgsX109lkKR8o0mHz4akvVyXH98HOPKR9svxzBt9riVqPcNjqmQzoOW-rAPH_bZH0tNVuYH67sZwXIaKjDhHQ6jza8_scLZVvFN3I0ol0O7T6UFbaleux_ch9ln3in1Gvv-hEYti-DO9bB3oGBQjxZRIkzF7tQpDE7WjqdvGf-knEK8tPHE-Bv_-bBPmZa9PTf9-7aatG6-Qo55jDT7AkL_G-aQ4XLaH6P_F0EaxUI8EbOFYAg5i4vsYhKa06-hlk_jujDeVeGu1xwsIR3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27225" target="_blank">📅 21:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27224">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgKq1ghCu8KjCDorGhdqB-f2oVD2HexDj8vwMq0CErkxGHk0TG_lTxwJ9CTLQhLg2wkJT0LZUIO10oRIzW9DLuSkHHCu4n_LGDCD1BX9lW6776i0V9jb2EZVo4wHg3TClCNMW5CcsLEyP-2EiXQ7Wg2090m2Yrx92fH_Uhf_Rn5Ij5L94j6Nu3Johei5X8-Xg9OiMZRtRqcFuTf75qdMg9CAv5qAyPQ3b9-DBgbnnFj-L1fTx8bDh69w7aZfOse3Mtgryfpvjz6xJTVAFbXXLlgg6f8ZwQim66_3zCEq8gsxSoI8RBuvzp9sDYq4WRapp6z2vzjtei4a-OY7eZwxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تیم استقلال امروز دردیداری دوستانه با دبل سعید سحر خیزان و گلزنی یاسر آسانی تیم استقلال خوزستان رو شکست داد. حردانی دو پاس گل داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/27224" target="_blank">📅 20:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27223">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHN57XCN0qvo2LhJuburVvHApjoRTrE7xEzy1MZyVxv68g0umWBYW9K6Fht-scmu6ZpFbOtjPS_o6P1gOZGsD1TWGOnAZV00prcwu0kXGNR8QZ0JVRFCMZ6FnI7lqm0UNvOy6NDuY4cTvv89flxcZq88C-BhdyYoJ2xM4CoARmjnkrdLr6PpUgnAFr4Xy6RGKqoM27YqA42VRg8TlOqwaW25lKYi24AiZ-ggOPZeBq8EniSdP3f7ANvcBVhrDe0AEt8oStHnvepcQEp3O6dHuQXY6tT3O33ebvTYjlbNR5GaPFU3t779VQeBnsxyAxQ38BAtj1bem12x0E8OtDTVjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇧🇷
#فوری؛وینیسیوس جونیور ستاره برزیلی رئال مادرید دقایقی قبل قرارداد خود را به مدت شش فصل‌دیگر باکهکشانی‌ها تمدید کرد. باشگاه بزودی خبر تمدید قرارداد وینیسیوس رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/27223" target="_blank">📅 20:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27222">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883695a5fe.mp4?token=XHG5ew91UgJuBZe19Y10DGQgxeAJua7yeRRZU8HSFVA0Sp-h1f2dKkau5teoD6qr9MkIOCQTzlVSCv8_m3_THMSZUbkJdYucGO8Q2dMeKooySE_KncXwqJZX5QSx1rdcHpyAQlrbOIzYarrfnALyXQjecYxTEbj8MbH_xcrJXBmwSBWGI-dQkXPKjN0LFOgSHnYYEB4Ehg86o0HKEQo805b0HrA2EszYEZush2QYApwuD9TvbBWMQJq19uRkQA3t6M_m5YBsx0Txv2Ji8NxUa82ipQUGjKTxEthPuJy9gXOETEkmhmDyoKvYzbLy6aQSH8c544311HXyrF8h6o5eiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883695a5fe.mp4?token=XHG5ew91UgJuBZe19Y10DGQgxeAJua7yeRRZU8HSFVA0Sp-h1f2dKkau5teoD6qr9MkIOCQTzlVSCv8_m3_THMSZUbkJdYucGO8Q2dMeKooySE_KncXwqJZX5QSx1rdcHpyAQlrbOIzYarrfnALyXQjecYxTEbj8MbH_xcrJXBmwSBWGI-dQkXPKjN0LFOgSHnYYEB4Ehg86o0HKEQo805b0HrA2EszYEZush2QYApwuD9TvbBWMQJq19uRkQA3t6M_m5YBsx0Txv2Ji8NxUa82ipQUGjKTxEthPuJy9gXOETEkmhmDyoKvYzbLy6aQSH8c544311HXyrF8h6o5eiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌ای‌جالب در بازی دوستانه اخیر دو تیم رن فرانسه
🆚
گالاتاسرای که‌موقعیت استثتایی داگلاس سارا ستاره گالاتاسرای به طرز عجیبی به گل تبدیل نشد. این‌صحنه سوژه تموم رسانه‌های خارجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27222" target="_blank">📅 20:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27221">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOTfK6C4PK87lKcOmd6XiibaIaYJld47OVVWBITZZ-VEQfi7mXeXiKf7lJu_a7x5LSjM69auWVAToo0N4ClLRuMoJE8szhaqNfl2TL_-ZOUbi1aHDl-_5nSda9dIysH2atF66Om_6JF1a9UCxzriteQjL81uCs6wykoaY1_ntIlpHJAYi-0xtON_bnDCFEF-EJhRFLU8KJkflSiZs5po531iRWE0v58B7KBzeUMvCG6quka9A8nJwFmuOS5EbgZp_IdYtB2qyu0a0npCLcKNFZckMo0nmXiRx8F-T1A0e1UeoDmaKdmHb1z7gFEzkCj1ZodwPhDF7U2Wb-dH6TO5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌فراری‌قرمزی‌که‌پشتCR7 می‌بینید، یه فراری معمولی نیست. حتی اگه پولش رو هم داشته باشید، لزوماً نمیتونیدبخریدش. این‌مدل بصورت اختصاصی توسط فراری برای مشتری‌های‌خاص و خوش‌حسابش تولید شده و تعداد خیلی محدودی ازش وجود داره. حالا اینا به کنار، نکته جالب ماجرا…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/27221" target="_blank">📅 20:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27220">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoBMZPDn03TzWZ-2mc062Wg46jxBQbFT4kPoXDNEwGB8FZ8wWlVlUONvM4bTk0xfIDJTylBUVDMALbmwgzS4t_RV90A0FELIiayuFsveJ7eN9FWd0OPm1qxfxS9PCLT-K_RwgCt88B1_7tN10SfSOfuEIKzpCAQsvu6GfTIbine5S_r2ZW5blycS00Q0p83BK29-tKC1qB3cowhOFVS296O04QhxPW2dq4vUr0gs4bR_hg-CCc7_goHQjRpPk045FFSjbWW_PlpCc-RH50zj38f5oAZBET5kY2oy1VK4P7zYwvAgABdeZlHfCtsIGmwBywiepnFCYgd4XqYt5IlzsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رامون آلوارز: وینیسیوس جونیور و باشگاه رئال مادرید بر سر تمدید قرارداد به توافق رسیدند و انتظار میره تمدید قرارداد به زودی امضا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/27220" target="_blank">📅 19:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27219">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHkBAMvx8sJJscm6xjE8q1ZuNmsOaFbLhuOqzJMn6qxwJh724YaJBI3DL4vmpzVR-H1TEOF0I2dZ8jkJOp1s1PUjoY0dnt3ZyyfNg1E3RcfNTSL37blMkuQJ0Eyku1KiAM-Wgfu_ChVTaho3okrf3A2lo2eO0LslWLX6aP9FGIp5Lmlkh6Drl-7xj5RBiuJtHIxHG022y3XQTbI9t7d2nUfH51bh3zmYUqOMpmiKPM-6Lc2pSXFwaUVFqQJ6NPAOQ5j-871hFtTdYrJ8lFuTkvB3r58s_hgpis59WF4JRrc5updHXNsyARJkturmbsXREMmZOZ1BMk2cgxs8SD1NAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال به آنتونیو آدان گفته با منیر الحدادی صحبت‌کنه تا او و همسرش رو راضی کنه و بهشون بفهمونه که ایران امنه تا برگردن به استقلال.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/27219" target="_blank">📅 19:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27217">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ9IxxeHyBml_iMoNz0rJ6K9enw0uIy8vsxRNHhKt_lEZVMvdCO2NS6rVmi9iXm2yPy7CLybzunBxPDYpHbg77gZkh8ctyCrK7FjqoYDeOgSb1Wcr87LUjtZwfteI6hKJ36krN7N5RTPrw8yXsTlBPpc89lYZmYOTI0GBrrFAGO2xE05isUfR64BzsIJHbS32Rf5Sq97-w6BsGMh0uFSJmT0Cyicgusvi-cT116Ygx6_oHSH-OZdhz4jUCHx-WrVeYMjE0X9-AXJ5b2ateS93I5x4eCMxDF8TSkf8jwLX_VgNh0hW0Cqow8II5fyH1ksMF4IgHZ56NzHc9c8pVei6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛کادناسر:پرونده‌پیوستن رودری به رئال مادرید بسته شد و این انتقال انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/27217" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27216">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4H4Z8R3GTllHTP-oXn71lEgw1PxmTrVJWru2H_VIrf2CzSbmvwaMrMRnGldl3NT5yAdmKoHvkOlP0JnyYQ1bgPYCsIb26nqNopvc2Ml6XodatgaPj26W82KN2zJ4XqRB-fBE5OHL18IQH64uNDde8StmgINf_90nx-23M6Jt92N0YwLQN9V42NzaHboRU_IANhAFRH1i0yygeZFEvC0vOgSIft8COQ4UxDbQEr6bMM8xa3Nq_F-ugH7Eg8jQmB8odrEomRy3kMjOqZkHmzmSVWBUalqjNHwSSNh8zs2kd-10D2hKPFPD1YH58ow8KgRrRfVjsJrNHCgRexA83rnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/27216" target="_blank">📅 18:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27215">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbrJe72ATlNXRExbMmD10EqnSduddVLOV7nQGqHT53xL0PJclnFhcwV5nOmaG18RKFXx4BekVv9YWa4L0t4ilONsi-7e1ihkXUMpAKGl_eXSVrEwrWEtspSDxHOfcV_2nmFN-jSGvSyS-Odj-dUcEVIdA0ne-WGd3ZJpVW81MvQRp_zoYCCdnujk3IaZ-CE6YWquqXcyTbwGLLe9Me-8vkihjNMEW-xG2SAe_573J06cEBbOBwYOmY1nBxkA0yt0BtdkQRG2C819H693PjX8LGWcR012-0nsePW81LhNhqFcbEaJbsshxqW8WMo9lO-sUUefLrVYVafPfD5fYqdDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛کادناسر:پرونده‌پیوستن رودری به رئال مادرید بسته شد و این انتقال انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27215" target="_blank">📅 18:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBsuBDTMlGRqfSuHMHt73iXLcXax1SIoIbWWG7-LwwxEWuDk2h3vyKhEVEHBVqaXSgTZI6NaWLcMKszzLyRJS6LJQpf-tUukkQ4ntW8SoPiFEmlJqA4kbkZguXkwFpnFtVCGevkbWhiLNtwGZGw0oVoF08MTcDadwNNSy36TRYxi6lfijBBd3k8AKyVprM-DvK7Nx4rhBlmV41OVDeV5b5kPbQMmJJRwgDDpkBEba_kAMdqQWq8kH09xl5Bnv917M25203-fbYEU079B_yNAfv9zIlmXBq0uj2IQsuSNC-3VN0Hk-FxeIkcxR1IaBhY9qtkMsAcVdFelzAiS-6HBeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
برخلاف‌خوزه‌فلیکس‌دیاز خبرنگار حوزه رئال مادرید؛ بقیه‌خبرنگاران‌معتبرازجمله رومانو از نزدیک بودن رودری به پیوستن به بارسلونا خبر میدهند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/27214" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27213">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkDeE6hlzHEDQIbmchQM3YqiS1f6xauxi52C3GJwUqX3eG6hzEQBsxiAgZIkRYKkK16EFn7CbwL7kqyozwHnLt45pgB4RxzLlpKSExGU6K3XOTweS2XFY6lF4kC-QZe3vUUjNDsrojYTMjtvlPC9r7lkJNTldbkjhy6_kNKwKILAHEA7V7cH1AyyVIark2P7p03D8jgpummwVCfBckF_KcMR_J6t0mVEUlU400fzzEDn_TXTO-NaiO038oAfLRNsXLrCyatb-AGpXjZ7-7z-UhS5xCQGOdyrttLklfBlGWHij77yvWrqxCd1bT1cGn1PXbijp1UBaWagNtZvt3UFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/27213" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcsuVYTLnCwhlgxDOPHn6mv-Of-6BwvcOYmVTDkba_AW7BhynacyckWIfH-1QHSwC6SyOOsh2VWoYQOWdf2MyqGAOmyhS6UNF1jn415VsAMIM5igGyX4KbmdW7EVvcrYXlFS4EaYIT6aF15YRmvQErmyOwsGS3aY9Xb6YmHhOqwqqHyu2zbP8WWjAycIY3IrFrANWYmvhYE-eXaKsPVzxaQhduW8DeezEATeiEAw4gqBmNxT22gyET0XSkOrHROMW9lk_MfsS15BVi0zljs1RjjYB_eEL6fjt7pQezovngDcTBgADidtQM8hpUBwkIyIUm3rHzdt41kixjV7pTIEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥃
خسرو خان هستم و بالای ۳۰ ساله از شرط‌بندی و پیشبینی درآمد دارم
⭕️
با من همراه باش تا بتونی روزانه بالای ۵۰ دلار درآمد ثابت داشته باشی
🔥
💵
با عمو خسرو، آروم آروم به آرزوهات برس
🔗
آدرس عضویت کانال vip:
https://t.me/+J_q7c-COftQzOGM0
https://t.me/+J_q7c-COftQzOGM0</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/27212" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubTWwhIfhj7243BJhAJP2bZJBvW3Q8jcHodQIKaPGR75g31-KUxX22yNOtR7psKwihuDRDVSMkYnhr5xV6f1bIH-Shv-vJq4O8Y7Xx6QPe3SLUV_FTqiAZs6skoCDyf88cnp0ZLDw-9yf3nFj1hFi5txdu-tSopH6wjYo7hF_ZRAvVsChqkB94mfQp_UuXSGWm1ufzrWs2F1s6Z3b4zXVo4XGxKQ-NWS0PKJH57H55gsSle5_UbXRVPwrLA9RKswpDhnHPbogPJazKDD_ia04sUA61z7WqFmBS89BQ76cpznVdIDY-y0av5wr8fnIsVPXkWVErHu4Z70T4bFf5UTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/27211" target="_blank">📅 18:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmfT0U5j4LdyY7MwLaknAABPkU0H6HN5fImTIZnM7j2t8ROCvplmwvPIcdr3U9EnfDGkWxCuhG8GkiJbTXClf-p-L5_AEAqEWCacCEHNEhfHl7j58RheQPfNQKpSBzMRKd5s97Ld6iKpQeIkRswDYjM9ToYQ2z46_h0pxV_82GtQy-MdAkjcUl98HN1C2_H1YZmOYJUbsQn2-V2XUgKfw5U1Lf-h6UgNQigvorhdJACIzrXZFHc5OFbyriLv8k7czuTDzqCjloFRJj9oRGuLSNcX35jF1naj7XFhACdVkGFX3-k0FOAftfOpriL2f9pphS9uSd3ByXpqBMyAfLW6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری قطعا بازیکن رئال مادرید خواهد شد اما سران منچسترسیتی قصد بازار گرمی دارند و میخوان این‌بازیکن رو با رقم بالاتری به رئال مادرید بدهد. رودری بارها اعلام کرده جز باشگاه رئال مادرید برای هیچ باشگاهی بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/27210" target="_blank">📅 17:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27209">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmOT2p6IeYrjXNtUfYTg11WGfRLGBsYOcnKUsCytKyOSiq8u0zcYFTUvMWXSKZRCD9e-ZwKTioZpLs7mJEH0QFi6SM5xAmPoe_0SDhi7q4egqej6MOhL8YVOXShGcx_5VNf3t-cvZSAR9CpL1lk8-Vrf1U7WR6xLCqY9qB3f8MwB0wsVkScEEOYUX7lgyyL8I7mwSpJnNF5jWXmvxvDgCCYQhxqWuTRlUj8VDhzegkqZVYCeQdR-ZtbuF8-W9FRLvSFmtwV5DqOEP8_DTIQejgsLLNA8VgWdFetdE3QXCEtOGhqK4RymVFuoNiCABOveR4xepyeIgJo8huVEsxSDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27209" target="_blank">📅 17:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27207">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIs_l1K_XQHikWRJLnr7fPbbPw4zOxeVYZFJBMRiw_yuCT8DBKbA4JIhKRyjkyzu_0IpFonrr0xEYKBrmU5UcDMmYhQa-cWFOiRgVdNCazi1QXvP-NuQuCcbSQjDHGYlIWjW48n1OSpGyrSkr2ohv6obBlczYatlOAmNKlDJaY3nsXGLdQgLttIrL2sr_uwevxF3JlqjmEVZI4D9n9_ZkvgRCZb5sLBnVYHkOxe2jmIIbvLsSnuZOI5jtnn61EUPJyEJOAvd_uQZzVNKQUph-17N70Jc-xxDnvjs1HosWXl5VkAl00FsfFkfJvbo6LU09izjAolHtAes28XoBo6cAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
عملکردخیره‌کننده لیونل مسی دربازی بامداد امروز اینترمیامی با به‌ثمررساندن دو گل و یک پاس؛ گل‌هاش رو در کانال دوم گذاشتیم برید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27207" target="_blank">📅 17:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27206">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f47e64799.mp4?token=JbHRbuyj6s_MPziRhzN-25xHc4mOsuESd2WP7ft2HRRfW1nQ4FH5BFokCMh0BOcxh5F8bk8ttWGKxr6V13kwuMDuQ3Lb7Wn9x46tZ2EFiJsaDuguxDnxnVqRjeV1R4JdULmAgLFMVJMe808EdbIUA0p1Ciqu83IigOB4JSwwWjcQeY2-cnHFyxfUZUVS9Ndm1UF3_6DYhDOMKHflxm3erOHRm1xfmoiEowShArTXNmXwZCvF7OTJEcvp186haA5l_GBu4Yg8NRjz3nwF-dhlCdC_W7yadl2b3UKjVY_Vv07EuW4IjAcKiQCeIf7pBXtlW9IzSUYKBL6ZUpDyMPK_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f47e64799.mp4?token=JbHRbuyj6s_MPziRhzN-25xHc4mOsuESd2WP7ft2HRRfW1nQ4FH5BFokCMh0BOcxh5F8bk8ttWGKxr6V13kwuMDuQ3Lb7Wn9x46tZ2EFiJsaDuguxDnxnVqRjeV1R4JdULmAgLFMVJMe808EdbIUA0p1Ciqu83IigOB4JSwwWjcQeY2-cnHFyxfUZUVS9Ndm1UF3_6DYhDOMKHflxm3erOHRm1xfmoiEowShArTXNmXwZCvF7OTJEcvp186haA5l_GBu4Yg8NRjz3nwF-dhlCdC_W7yadl2b3UKjVY_Vv07EuW4IjAcKiQCeIf7pBXtlW9IzSUYKBL6ZUpDyMPK_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری قطعا بازیکن رئال مادرید خواهد شد اما سران منچسترسیتی قصد بازار گرمی دارند و میخوان این‌بازیکن رو با رقم بالاتری به رئال مادرید بدهد. رودری بارها اعلام کرده جز باشگاه رئال مادرید برای هیچ باشگاهی بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/27206" target="_blank">📅 16:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27205">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF16uMZd9hSbBQLGgJIjR9mkL_-01yUygVhH-cP1JIXjJCpLsJkhhXZRQKkDtDexsh4Icm3EsBAyZocDip5i5wgCZ3qpwIpkuHZC-4fNWF4nBiNw6eT8N9iy_eM7zOdC5UXk7QJKC20Oa0HwYryTnwR9QmDAPCQx4zA909md-ltQRziyPVkE_dvgIRJSej6HImp8wdMZ7QwkiEcGl7mlEf0RlpD-VeQhsrdiiOEasaHx4tn_yu-WPVrq9Q8Yg7dEzWCspOfTaR6rMXMytYVBtn4wzBqjKlyL8EiHfxSxis8V2dydLnRGnl41gZQYaHXbogMtavhIyjx1fqIJtCDsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیریت تیم‌استقلال باایجنت‌های دیدیه اندونگ، موسی‌چنپو،داکنزنازون و آنتونیوآدان تماس‌‌های خود را آغازکرده و اعلام‌کرده‌هرچهار بازیکن‌رو برای فصل جدید میخواهد. اندونگ، آدان و نازون آمادگی خود را برای بازگشت به تهران اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27205" target="_blank">📅 16:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27204">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEiPxiQ0NNORQzZHdEcEEhAf1uCM6XCHz7R-eArO9r1YAAMfYh_pvpdXoX55IgWABM8fT2AKhJbGAghcWciWAh7A0Sn6ZrVmI-76Ew2cnO-xVd-KDHhWdZWO4gVO0ngELPeaTfjHRR2a5vP8OqDgW1BrazfCzDdlilxEz7RsE_6921GH96J7bySYxcyjcSKKCd3mpZbWVGlVU4E9w8US8N6KRjOvfpM3aHlYLhNBGsHItf8kGvYvhWCJmKZhIpP3vFHGU_9tTjx7gwUCgckgkrTkm8aKVAtYmG-4s73yyGiMSV-6pxdJ6Ybiyj-oTCNs8FyNS_E_FrY6B5k6-6L4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پابلو گاوی؛بازیکن‌اسپانیاکه‌قبل‌ازجام جهانی گفته بود اگر لاروخا قهرمان‌جهان شود موهای سرش راصورتی میکنه در روز تولدش به قولش عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27204" target="_blank">📅 16:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27203">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcW98M2s8GHK1-VMTAu0AzZuDnQt0BfD7s97UrrFxpGwOxXNXvCUjck-EYdtVzZaGIivhqwFcxdtCG4JRC_BNXqFC6WUS30LIAC3wBPpDAipwp64dLudYuV26w3l1jgLcV_lUFG0EzIvgBHFfEuA0Is6yy46HvQtyEnZecTURckmXAVwBr_w0vvYRUbCjH60IpYm_bu46_p2yybileDc_qqsPml9puWFsjkAW5PNPRuMuskegfSBXJxvNG3o6tw20ImHVMnvoH-rm22sqZzkxYRJMKfLr7t8zQQnySfr0R7wabOwyX9bQdBYwEpcXMHTszAkI5QY1EdOeVKcDp2OdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی پرشیانا؛ باشگاه استقلال برای‌دیدیه اندونگ هافبک گابنی این‌تیم بلیط تهیه کرده و این‌بازیکن‌ظرف 72 ساعت آینده به تهران خواهد آمد تا بعد از تمدید قراردادش با آبی پوشان در تمدید شاگردان بختیاری زاده حضور پیدا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27203" target="_blank">📅 15:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27202">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsD5gE_RNIl-hLUik63z368lsJoDOEurCtIreCukbnCSXUXLHdhmtt_7A4T0Pjlh1lcscmPJrQBa2pGapwCGkMbjW4ioESynwYy9Fcqo27z-2jLyJAMKwIqJzHuKagVEprT3ukiLa2qfiNqrxFvrJ2ijj0pH-boEIToaGRXv5mTJPmvpxm89YpAAJvC51tEwXrIfHfNZ4pKj7Tqbl-wMCfLy02WBRzTAwO4pLvtjJUiEwwyPSV0XOCWtwyePiQs7hyx0FsAQckJeVULji3rmu6nfJl0XjdbY-XQxg0gZZ7yuJmmaffkKmmRWbdJcHHbLLhw20DB2da-4ITdBYMtHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا؛ بعد از بسته ماندن پنجره نقل و انتقالاتی باشگاه استقلال؛ علی تاجرنیا شب گذشته بامدیربرنامه‌های ایرانی آنتونیو آدان گلر فصل‌قبل آبی‌ها تماس گرفته و ازاو خواسته آدان رو برای‌بازگشت‌به استقلال راضی کنه. به احتمال بسیار زیاد آدان بزودی…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27202" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27201">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=XWeIK-sOwb9H3FFDVN1n9ghLAOj_SJsQDQEo8Mgq526i0Sh_idqzjbPEf5qZtNNrsr6Gh7mnxaXUKunS_XWcKD7Hnkwb86A-m3mzXSNTs6Xny0AF0_s9lxmGB_rNacKaXdt0R8NJ0ygFY8irQThaC7Okc_t2KpFc2BO2vaQ_IyQ3pt0BrBvSInf6G0qc9iFr8cho34G2Q_lHes_UUkxlFcQutnaT-yanDXzCUwtxD-qP8dLqaFmsWAJputn8wDDK_QqVtUJ4UONE_eFhMLGiPhpdYvsNzyy2bh-a4qtrOoKEeBAt3QdvDY0-fbsjGn8Nw5opKEaEG2cwFTOcfzDICw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=XWeIK-sOwb9H3FFDVN1n9ghLAOj_SJsQDQEo8Mgq526i0Sh_idqzjbPEf5qZtNNrsr6Gh7mnxaXUKunS_XWcKD7Hnkwb86A-m3mzXSNTs6Xny0AF0_s9lxmGB_rNacKaXdt0R8NJ0ygFY8irQThaC7Okc_t2KpFc2BO2vaQ_IyQ3pt0BrBvSInf6G0qc9iFr8cho34G2Q_lHes_UUkxlFcQutnaT-yanDXzCUwtxD-qP8dLqaFmsWAJputn8wDDK_QqVtUJ4UONE_eFhMLGiPhpdYvsNzyy2bh-a4qtrOoKEeBAt3QdvDY0-fbsjGn8Nw5opKEaEG2cwFTOcfzDICw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27201" target="_blank">📅 13:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27200">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27200" target="_blank">📅 13:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27199">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=Aj-FjLzxVWyAvkTdWVTSkVnk_cbhO_2fYsZKdZ6htZs2tWUPWf-OLktpKIn9N5JRgTkclOY7THik7j3rNv_Nj24Q-rbrgkJbMfvRwcaLWMVZXNznybsjKopx8iqPUZHLo6Bs2FSAsmmW38aInhHq3g_esnbQpQk-YDlOs4Yzz-WdwQ8i6BTUozRzXRDiNQ5_PUgbAOZT71S2UUhHRY2sTeJif1DnLnJ8AkS7tQaNuzXix-ttrKsT6-dUW0g4_jgReE3SHi03B_cg2__w7VLC5b0oX747E2eEenQDOo_CHI6wlD7rUZ9AJAApyah-QBxQWSckLFEkur9QJX17yhtoZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=Aj-FjLzxVWyAvkTdWVTSkVnk_cbhO_2fYsZKdZ6htZs2tWUPWf-OLktpKIn9N5JRgTkclOY7THik7j3rNv_Nj24Q-rbrgkJbMfvRwcaLWMVZXNznybsjKopx8iqPUZHLo6Bs2FSAsmmW38aInhHq3g_esnbQpQk-YDlOs4Yzz-WdwQ8i6BTUozRzXRDiNQ5_PUgbAOZT71S2UUhHRY2sTeJif1DnLnJ8AkS7tQaNuzXix-ttrKsT6-dUW0g4_jgReE3SHi03B_cg2__w7VLC5b0oX747E2eEenQDOo_CHI6wlD7rUZ9AJAApyah-QBxQWSckLFEkur9QJX17yhtoZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌ تامل‌ برانگیز زنده‌یاد علی انصاریان ستاره فقید استقلال و پرسپولیس درباره حسادت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27199" target="_blank">📅 13:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27198">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvNjLfRyeImK5bzcYjtwxIxfqUsEV7rQZmN_t7Zhrz1pQ9ggw0ZDi6Oa9lDyhLy5SCXxR-LrEBA754g0C-ttfPh9cfRKoal0PeJtksidMtgpVnFZKIKqGPK-F-e8sN9QVJQwKZTwqe9mGpX2gGN_-s4AHgdIMBxJRynKaI3n8ASQqFzdy8vEASbaesw_DsbtJ6dkic6kyJs7Fja-f1aVNCuCqu7RLcayL3xqTNu8NdGUaNXXK1lAMfWU_YNSBKOHUc22mQH2O1NOOQVKWwhYpgivlcE6MR5yas9Ugz1R0X9Rz-Akm7um2pRMVv4PVWTIWbYCbFXDqy9oRpWTj-HLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27198" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27197">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bor17LPbqOR7edqSB4pHlFSty9vzknusLq-lRBVYZuQ2sWaZxDkGqmhutg3W2JZd8wJzHsWhMFBbdyLJWv3cK66JCjE9ehTdHMQnH2ab8F4iAFcGKYO82PPI7EhfVcOco_Ac7uxFHPJbuLyi44dj9Q4SNAP3foAuwzaOJjAxS0hx0bPvHu9Ngr7H5PUuY-iXXNft5qrmdFJ5JX-enP_UgxH-wmHf-WrDXvYZ2pyHnGUwMljdpCTjph-W0YNom2ix_dCkXEL8itscFXfdan_5j1y9tVscsR07d5pCTq-74djWp9RIqNHlcdM2D7sPdxXI-MvYbcZi9K8H2KKbrj5Uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فابریزیو رومانو: بعد از رئال مادرید، بارسلونا هم برای جذب رودری دست بکار شده و با مدیران باشگاه منچسترسیتی تماس‌گرفته و آمادگی خود را برای فعال‌کردن بند فسخ قرارداد این ستاره اعلام کرده‌اند. حالا همه چی به خودِ رودری بستگی داره که رئال مادرید رو…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27197" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27196">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHgJo16EW8CibtxmNos93kkeU2TTG4rjnqepXUBhJX15TLYy-X9rbZli1IVBSSFSZQTcGkgWjwlmX9R2BgMuj1WugYkz78kgiKJpVm0nr-AvGAj_ZzWm9pjgiF6fPMgj8V4-kYT7lkkgvsKEYBy2A_cMh-YLb7HYlBPRbjoU3QYmRZt-ScQhDbmuOfIs5YXhxMJuBHBhIPy8jssEs3OjWRGfZ3tQx-eqMbhDd6FbyDdQ51SVIjswtJj8VIf-kk-_jhhbZkXfVz69UTqaUGeSu75LqoYW0J-LeGbkTO7PXKQQl02Nv-gkxyAM44tlBOOc7NSgCPpjTNnK69NX_Ro-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27196" target="_blank">📅 11:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27195">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWHHFWydoS9S7_kZ-lNA9ZHh-XvWAxFP_Yew2Lr91sPcJkc2Ly7sm2yCpzE8i35IUTvMrunvcd9iOZX-xA7KcBpvILrITcSM6O_07hzCOstxl_53YSxNt0Q292kC88jQI0GB75U4opR6Ye-KBR85dVTdIUo7tqgE5HZsJ8FzVK0FYnGMXiDbLHKL7zFOMnPVj7eXhv328vDfYhk6WbY3H1hI2VRzy1E2CkLu8aMKWcjkbCFUJk2RnHSDyA2_H5WGu8yp3_mqahhWlwuh-x0hN3_iVbxhW2kqqavlyRXX-JGJt76aaqStjXTaWTEwTMuGbWweslcQUKK4F1iZCmUKScoc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWHHFWydoS9S7_kZ-lNA9ZHh-XvWAxFP_Yew2Lr91sPcJkc2Ly7sm2yCpzE8i35IUTvMrunvcd9iOZX-xA7KcBpvILrITcSM6O_07hzCOstxl_53YSxNt0Q292kC88jQI0GB75U4opR6Ye-KBR85dVTdIUo7tqgE5HZsJ8FzVK0FYnGMXiDbLHKL7zFOMnPVj7eXhv328vDfYhk6WbY3H1hI2VRzy1E2CkLu8aMKWcjkbCFUJk2RnHSDyA2_H5WGu8yp3_mqahhWlwuh-x0hN3_iVbxhW2kqqavlyRXX-JGJt76aaqStjXTaWTEwTMuGbWweslcQUKK4F1iZCmUKScoc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا دانشجویان رشته علوم ورزشی دانشگاه سنندج به مناسب فارغ التحصیلی این ویدیو زیبا رو ساختن و درپیج‌دانشگاه‌منتشر شد امابلافاصله چنان فشاری به مسئولین دانشگاه از سوی نهادهای امنیتی وارد شد که مجبور به حذف این ویدیو زیبا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27195" target="_blank">📅 11:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27193">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fi0TfOsQGekcSfHk94eDYkg_jGNCloHsEtLOnSwcG4hqZL0EDzJxWUu3owAD7yMA_yiRP-FIWrzGkvtXvOadQvYnHbqzTWfjEDbJc6MIPwElby43KiuYO8DTeM_fTg6lJajNsUtAqIGy_8uFCfEQFDWZ0-OXfBhSvLqiWRXPCDmrmJCCVzEtXIYdXLjjZ-IjsABqqUifYxtU1v7mG1pkZ-l-zo_7q-aMJUFcDhUqnOEc4JiDELEQMaBgmDfwCUFud26nDDi7pr1jsK872g8WWpFgALZhYM4kps5SVl-s5HcagJsvi_qPtGimqq-nWs_WLNNcFaNJYroUtADMtI_1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxq8u3bCHbZEvvNdo2XZ4Nty1h_f1KJtItVp56i84vuqk_IpZ7VMl-Z9Hg_h01-dbDq22iZeRMLwgqZxN21lS6WM9d7qwqwQOQsPWJWaLmi-NKKq0XBNKWur9HP4sqCLxSD3xAml82Qz2MLyMtph5C3eq3kquxTWMq-VArq6pUgn19uGsc5H5VnwIxaxTi4c_LL1Lj2qd3rDlv41f6iCMSJ4PBzNRy2xW-fsf_Ffj1yrM3OSScGIK2LEYUavpvRo790DwJMp9RxBcRTaAm0BJ5d2aAExd1IE_n0L4Mxt-o12K2kOje0jeE9UnxfjFHWwREbXbLl3uTLY4LGQbhdNbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به جورجینا هم اومدن احساس بد بدن راجع به بدنش، در جوابشون گفته: واسه من موفقیت واقعی هیچوقت این نبوده که خودم رو توی یه قالبی جا بدم که معلوم نیست اصلاً کی و چرا ساخته‌تش. موفقیت واقعی یعنی با خیال راحت زندگی کنم. کنار آدم‌هایی باشم که دوستشون دارم. حواسم به خودم و سلامتیم باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27193" target="_blank">📅 11:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27191">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV0073ht0namwyTEvIUWzJiz_c5HO5oT2YkYd_ya_S8OZAFTL-vnrgrfTYDZaP8cQYKHejjKZXCExhUm9OsK7pIF06TMQQRtgtPEQXSV6ngj-eOBJqdcKTROnTus6Eqy2WAqNDpAhuZNYemAasuhKh-SVqlwXdr20GIdke99AEv58e9FeLhxD21VmD1c-hvmSiHRmiLv0d20MyOKimTgqDyP1-G-6vWzL2RkmJyeSGVTrI764s3qg1NjcdmM_PUKdLx3gB2FX-KNnRJrcnM_IluroKuXHPEslKHo1goxkEUk2dE0gbt4_aHiBR8lNAA-5A5t5FiFVFBW7vkWOY7oBfdKobQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV0073ht0namwyTEvIUWzJiz_c5HO5oT2YkYd_ya_S8OZAFTL-vnrgrfTYDZaP8cQYKHejjKZXCExhUm9OsK7pIF06TMQQRtgtPEQXSV6ngj-eOBJqdcKTROnTus6Eqy2WAqNDpAhuZNYemAasuhKh-SVqlwXdr20GIdke99AEv58e9FeLhxD21VmD1c-hvmSiHRmiLv0d20MyOKimTgqDyP1-G-6vWzL2RkmJyeSGVTrI764s3qg1NjcdmM_PUKdLx3gB2FX-KNnRJrcnM_IluroKuXHPEslKHo1goxkEUk2dE0gbt4_aHiBR8lNAA-5A5t5FiFVFBW7vkWOY7oBfdKobQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ محمد صلاح فوق ستاره مصری تبدیل به سومین بازیکن‌بزرگی‌شدکه‌به‌ترابزون اسپور پیوسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27191" target="_blank">📅 10:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27190">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeYhb2jmQ6INLVbaXKEJrYf9NZ_YHpfWEJyHkNALJ1mu8V2Tex5XCMUW9EXIJMhcRFgA-YNcYFdaeyKtn7_-yKjp1BW1ezkhJYs7iS-7URtjkQBLuIA-lM3zz9o7-I4P6czWjeeaeTPn4sq5Smugo-QM4VMNDRJWhRFVvxcfT8NoTlBF3lG13QyB-W6MmsPVu9gTjS3oJdfukNq8ePCWNgS1AYppuIuWucDmKNygPx6Gp0FbBYE23ELLiS2__uCLDcEeS6RC4hozPYZC9c9KGYKi2sbgTuYhOAx4vr6ws1FdEQ2uuhM7vvGDwYd0Uof2_OhwioxdxhAqYoQqtNJHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
عملکردخیره‌کننده لیونل مسی دربازی بامداد امروز اینترمیامی با به‌ثمررساندن دو گل و یک پاس؛ گل‌هاش رو در کانال دوم گذاشتیم برید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27190" target="_blank">📅 10:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27189">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=d7pFU2pJpde4SGT9jFENEme4BOL5ohB9FIcgU6fOsMVfi2va7kY0qky6uReGMaWTpoun25fL5VwlUXu5elU-7bTn2wQFidY1NKjcEeoCg6PofCoWqy5iAabaUKuHYtBbH7sL300uZXFbX8jEZ2bLeKDff5UWCFXojzYtphuu9W3zqYyhqkJ5O4riuDwMW8PZvn7W9Q99v8IDu9O7P1SJLuFubaZTel9c75XtDxXWEelviyU1FDAyvRag9UXnZReXjoQ7p28Ss0ajJnmlEUF2kz0yCsY33jlZF3eTM7Ig3bptKCrDQUoFtMzuOGLiYI9IwwElWD_tZtY6t6HJ3LAPgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=d7pFU2pJpde4SGT9jFENEme4BOL5ohB9FIcgU6fOsMVfi2va7kY0qky6uReGMaWTpoun25fL5VwlUXu5elU-7bTn2wQFidY1NKjcEeoCg6PofCoWqy5iAabaUKuHYtBbH7sL300uZXFbX8jEZ2bLeKDff5UWCFXojzYtphuu9W3zqYyhqkJ5O4riuDwMW8PZvn7W9Q99v8IDu9O7P1SJLuFubaZTel9c75XtDxXWEelviyU1FDAyvRag9UXnZReXjoQ7p28Ss0ajJnmlEUF2kz0yCsY33jlZF3eTM7Ig3bptKCrDQUoFtMzuOGLiYI9IwwElWD_tZtY6t6HJ3LAPgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بغل کردن جواد عزتی توسط یک دختر در اگران عمومی و تذکر حراست سالن به این هوادار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27189" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27188">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a3912563.mp4?token=u4LOU-_GZlfP0SX21CcbnyvTJDPYaux1xG1Gpyx61cxlhmRmj_9Y2OVAWOXuThuHxLovnXUKzcqkyOxnMHJJgFpsPAqRcUlfLBWugDOEkZiEvZ_Urw1FX0t57KwG60sJso_GYkfVJUEhOHnfCuUTxUWEQ7Z8ttO7UvIFPClzSX8cqA752bmHFu020Sof0OCw-3Zmjee00aujXeazkTl0RyJNxZp0anINMgmMggKzd3GX7_8hFUa_3prsbxmE0rM7YiBC1tGTGqar0O4PncOGgVlQLZgzzMXZgyJGCd7BOVm7zcHOLFwBM6uNGsRWXtXJwrUi-cg0SekE6IGJZAcFNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a3912563.mp4?token=u4LOU-_GZlfP0SX21CcbnyvTJDPYaux1xG1Gpyx61cxlhmRmj_9Y2OVAWOXuThuHxLovnXUKzcqkyOxnMHJJgFpsPAqRcUlfLBWugDOEkZiEvZ_Urw1FX0t57KwG60sJso_GYkfVJUEhOHnfCuUTxUWEQ7Z8ttO7UvIFPClzSX8cqA752bmHFu020Sof0OCw-3Zmjee00aujXeazkTl0RyJNxZp0anINMgmMggKzd3GX7_8hFUa_3prsbxmE0rM7YiBC1tGTGqar0O4PncOGgVlQLZgzzMXZgyJGCd7BOVm7zcHOLFwBM6uNGsRWXtXJwrUi-cg0SekE6IGJZAcFNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
پابلو گاوی؛
بازیکن‌اسپانیاکه‌قبل‌ازجام جهانی گفته بود اگر لاروخا قهرمان‌جهان شود موهای سرش راصورتی میکنه در روز تولدش به قولش عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27188" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27186">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ise4MtItvG8qaLX1ExFHnH3v3GzUvlddQJ0qc1hRQ_5lW2bdge0J2LwfiYXKcMy2OJ74WfYcd4__ttH0PR51fAh_d5Eu0guGo3kaCFJNRiWIctL3W0mqQqqUgU0hPx1gHlvDeoqcKFwefW0fiuU-iLFPPA3vxbIlm8FmZDRhpHc4VbFIPYswf6R9c2Hl4PekXI6ghNAYigtY1mYyil6Uot8WafhdOln-bUW9Q-1LeEgYAMQ7ctTMa1dZ8DTgk_VVf1U6vc9qnpG3Saf8SviQgJ11NXCSZiNjqkpbRQ0xvAhHOEL9SPw8IMPn-_mad1OpelnXpm9YzrEs7WqIdoAo9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
نزدیکان دانیال ایری از توافق‌شخصی دانیال ایری باباشگاه‌پرسپولیس خبرمیدهند و بانک شهر این باربه‌مدیریت‌نساجی قول‌داده که بزودی رقم رضایت نامه این بازیکن رو به مازندرانی‌ها پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27186" target="_blank">📅 09:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27185">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j68z6MXOPbhFxyb250VJoUla4PJUICZOC1OtMgE_B4aFEmMdP2WnODvOBcaGJy5QlcHeCQ2W5qOSfJavFGTeERNjWrKIbQjvckqBaElL1dR9yIXD4w4fH3rEn6uOuJ8RJKujP0KXVi23wXfzNHHvVxbmT0npnpwG5_9Hx8A2pGFUseKpPrKej126hZVgLSBDwX_oa15DY1rEEU5OhWgTkIWtjX5RpZbYklNct7XF1S_zgksJnJ9jhpa_mAV9QNvaJwd10KeezoBFfdrL4R3pL_IJzIrNwCSc0QfGEOEnFI8X7vxoORCp-AaUxyv5NUAeI72_IpB83FJ7JvNaOM0iJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو آدان گلر سابق استقلال: هیییچ صحبتی با باشگاه برای بازگشت به استقلال نداشته ام. باشگاه استقلال به‌من‌بی‌احترامی کرد. دوبارنوتیس فرستادم اما مدیران‌باشگاه به من‌پاسخی ندادند. بر خلاف میل باطنی‌ام مجبورم از باشگاه استقلال شکایت کنم. اگر جنگ نمیشد استقلال…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27185" target="_blank">📅 09:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27184">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ__UeliJ4ofhu6ltFBq6fHLMRhESJ7NvHnFwZAMeJEhnNCXLsgkEU8IQ6Vt6gyCOA5ZmRCYn24H7WJYfaUb6SNZvWLQLFaixbzpNSTf2bRz1YIv7oZTuqbn3_b6wHCOhAsoe-KYjj81KMAu4SHVveZ90DB-Px8RdL8LlltDLdUFnr88jotuo_p3Z0z2kPzxBh5BguQVml4ybeQYg0kR5kPezTrYtI-IRU-LbGaiIa_VjjGVIeGO4eWC6Y_dM8TWqX-RkQTTSS7U4TgI78LMejcex8fv3TQdBaCa2bLCSc3k8GZCz8Q3-PHdth2Fqy7MvW54emouO_fR3g2q7TTuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبل لیونل مسی در اولین بازی‌ بعد از جام‌جهانی که از ابتدا در ترکیب اصلی قرار گرفته؛ همچنین لئو یه پاس گل هم از روی نقطه کرنر به ثبت رسوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27184" target="_blank">📅 09:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27183">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syM8TY0OLNNtZxOoE3ygjjSJ6gxmrPVMPcNYmx2X6WFOml_wjihaaOiGxAeXoPqd4jHS0nYYc35Q0eofPhWs8BJCDPhzMOucWZ5TCT2dBvhhbFPJVoe1U2gpUsknU6gY4tJN5TWidnxytnahOExZmCUEB4VZ9eYvGBcbc41D3tc8d4-PvYB4RMdNVuKJP2XmtERi4Rh43OsuGfzQpN8Hizp1IdFXn5FAtDRcMrdBSRK9BawIykc8un_gPTH779PvqVcwWjms5TshkQnzleuiiSi9GDuf4Xk6KyDi5qTDcY465x73dPT-j-s09_B610cVy8KpxRuQd7LZ9zIcoP8cmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آفر مالی رئال‌مادرید پایین‌تر از ارسنال بود اما وینیسیوس بعد از مشورت با نزدیکان خود از جمله نیمار تصمیم به موندن در رئال مادرید گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27183" target="_blank">📅 09:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27181">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA66dZgB4RJwRaL2rDOnMh0W4rS9Ysl9VaYb3Tz368_LEu-sq69myLX4IA8Plac-aXsSZkia8R2XmNGKLkMEjnOfg_JwazX1oZDJgPh1yOUW0GBgWbATqD7W9jFCIqGnlL6XU7VwN4qob7XgpVaXYCJ38y3kxVSyAdPQDVLh7WgqOIB8M9CSlexm4Na41r5iD0roB7o_hCLyt1YAz_5lCbtVmNug0j2O5JedwozXYjYaH84Y_RMczwrYb9TV9R1gwa28csP-eyyuSgLWIWpIDbj_gb4JoPgnK_aoHxbveK4pFk6mgcBbezrxrcJLwZjgLY9-EluOBDcnwhMWbT4YPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=fcjtGspoTeL4tt0lSUOcCsM_MqOMh7sH-Mz4jEf8UoVk8ADWsFznitoLcEOthKbhVfZcdl-ZEUtVNYfVSOouKsqLHSjF6bcV8XtWF1do1CCdfGvquy6mLUEe_iG1OtgU41fUi1-g7tsqgW71vzSXxt8tc_HGVa9h6MjQpwfUOejFxClOfNQod0reIJ6r9F5x6G_ZgkDzKj9d14rNTdCl_uzAzlqGPfIV1i6eZnRL0Z8B3XcnIHkE1kO9ZTJ9SHRPr9MynEWMouijuHokSfM8EHNvDnKcXvrGHtyM-v7Fmn2Iyk0dy-nWXWfFmEypIOpaCxlvxIcX7Q6lixk_AW1yIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=fcjtGspoTeL4tt0lSUOcCsM_MqOMh7sH-Mz4jEf8UoVk8ADWsFznitoLcEOthKbhVfZcdl-ZEUtVNYfVSOouKsqLHSjF6bcV8XtWF1do1CCdfGvquy6mLUEe_iG1OtgU41fUi1-g7tsqgW71vzSXxt8tc_HGVa9h6MjQpwfUOejFxClOfNQod0reIJ6r9F5x6G_ZgkDzKj9d14rNTdCl_uzAzlqGPfIV1i6eZnRL0Z8B3XcnIHkE1kO9ZTJ9SHRPr9MynEWMouijuHokSfM8EHNvDnKcXvrGHtyM-v7Fmn2Iyk0dy-nWXWfFmEypIOpaCxlvxIcX7Q6lixk_AW1yIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/27181" target="_blank">📅 02:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27179">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHoUdNzD-Sbdk5nsWjcY_6Z89yICgigRri172Di-EYqYQwinKQek91NZE0G7XBMXZMZbnDj3TCQEiOFIqlHXDrVkly2PXb_nVAsZt5po4ixliKwOcLRVCc0eBWB8CNb-5252xpxzaXHtTUUcl_k7Dy58WoQdhfES8FrIS_Vsyu1x2fVZP3AwIkdlhP7WROkv-rLqxjCgzeJifI4y0wJtzC4QTBFabcbteA6LOJocWqleRy0zgkoOlzxRZi3XlVZa5tq5ctB8ryhDCEjsSTG2sbx9WsqWRTA9ck5AFgJE6qqjqXYOx6JBSvMMqoyGYXMiyPIDPfRCRjisjE2nqackmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/persiana_Soccer/27179" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27178">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=N_YcWq2-SNOn7_UNwDBmy15IIlQHoV6g7FKJOxck7sOe08xjnkmxyU1SA8xMO-jxmdNRJTKhmarmF2bDHObl9qQ6PVPb9xas4clkDIv_RgpYv2aKbCT8dDx_h8pFFm9Z7cdYuzJx8F7wOQefDFKUUhEHYddpD7wlLK-pYyEiDWcAf73zKRJb5S4kaGiCq_-zJ5PahdE4QRyRSL-rO-Z4pnjGLvPZLmwbO0ndIMHxVVow75f2TOmy7h2aeCNrI1CCA5IljI4-XzU6J9gd8pMFsQaNqZCqodwhfXZc4XcFS-injmAYZYmz_6pstC0-_ZqVKZxtlojlB4dmgxTbLPSk1xNJYsu1o4dYcemyyvWXausxQ6rrUIFm5PM320u6B6ovq_vsemBr1JhBOpXSj7VeB8pDop8pscqGXuP3ZVD8hDCjVMlUhgh3iEUoWoS1l5N88iw4oWcC-wYPD84keu9koiVMnj7g8M8i26PsTYAIr3boIz2AEFcLVbWZNu06QiPN-izI9LyLqCmYzuAmgyU-_-2Ay9Sfm1StJ6qX_-H37skdj8YVWWixMASpn-zz6HOHtRAzrVLcrJpwhrwSjfV-bXmTaiB1kX6cNa_rAxRWzIbd0cxlwLcjARy6vWtWAG26tgYwLigxyBswSM6j0rvERJ4ts8UhQRSE71Eoo9cmmmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=N_YcWq2-SNOn7_UNwDBmy15IIlQHoV6g7FKJOxck7sOe08xjnkmxyU1SA8xMO-jxmdNRJTKhmarmF2bDHObl9qQ6PVPb9xas4clkDIv_RgpYv2aKbCT8dDx_h8pFFm9Z7cdYuzJx8F7wOQefDFKUUhEHYddpD7wlLK-pYyEiDWcAf73zKRJb5S4kaGiCq_-zJ5PahdE4QRyRSL-rO-Z4pnjGLvPZLmwbO0ndIMHxVVow75f2TOmy7h2aeCNrI1CCA5IljI4-XzU6J9gd8pMFsQaNqZCqodwhfXZc4XcFS-injmAYZYmz_6pstC0-_ZqVKZxtlojlB4dmgxTbLPSk1xNJYsu1o4dYcemyyvWXausxQ6rrUIFm5PM320u6B6ovq_vsemBr1JhBOpXSj7VeB8pDop8pscqGXuP3ZVD8hDCjVMlUhgh3iEUoWoS1l5N88iw4oWcC-wYPD84keu9koiVMnj7g8M8i26PsTYAIr3boIz2AEFcLVbWZNu06QiPN-izI9LyLqCmYzuAmgyU-_-2Ay9Sfm1StJ6qX_-H37skdj8YVWWixMASpn-zz6HOHtRAzrVLcrJpwhrwSjfV-bXmTaiB1kX6cNa_rAxRWzIbd0cxlwLcjARy6vWtWAG26tgYwLigxyBswSM6j0rvERJ4ts8UhQRSE71Eoo9cmmmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از گل‌ های دیدنی در مستطیل سبز روی شوت‌های فوق‌سنگین‌بازیکنان؛ عالی‌بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/persiana_Soccer/27178" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27176">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=h9iyP6KHKSzsn17Qhl3iA9cOSWkY7ieJk-mWDdEykfH3moG-xM8C3c9iuqs_WL5ucdHytTWRBkk4MXDJKtnnv8FChQViSyyDwXVcm1Bj-mk7B_10PotSjPVelZPsWVIkzIc3UE6IogeTl00fjUMjl_vD45CvOtUzGmtAeqlQ3ZQ3wF7sDL8q3Ljz3_bJE1D9fNXVr-z23FmVE62NqWYpGR4YGSx5Cc8ZctqkebjTco4B57W1itNs-hpZ57NWWBt3LeqG0e7BLQJ8F1nLh2DkfKnuqenoyZ4hLWBALbAt_m7Jk_ZfmhU34jPvgxn9UXY5pH8NT6f0u21HsDpNjkfr9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=h9iyP6KHKSzsn17Qhl3iA9cOSWkY7ieJk-mWDdEykfH3moG-xM8C3c9iuqs_WL5ucdHytTWRBkk4MXDJKtnnv8FChQViSyyDwXVcm1Bj-mk7B_10PotSjPVelZPsWVIkzIc3UE6IogeTl00fjUMjl_vD45CvOtUzGmtAeqlQ3ZQ3wF7sDL8q3Ljz3_bJE1D9fNXVr-z23FmVE62NqWYpGR4YGSx5Cc8ZctqkebjTco4B57W1itNs-hpZ57NWWBt3LeqG0e7BLQJ8F1nLh2DkfKnuqenoyZ4hLWBALbAt_m7Jk_ZfmhU34jPvgxn9UXY5pH8NT6f0u21HsDpNjkfr9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/27176" target="_blank">📅 00:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27175">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vg7gr1-bpxASnZYv9kurd0UoyWOOVJbF3E80kKkL7ttcf1mFeKnyvfALxUTiIS8Hk9hDVIii0fjoJcO1FVhCbs53G61MjqU5bHR23eaDqFA7BIW2M1Ef1KEjvaYKOu6ngdRlM1am_NBh7pry2iIgZePRPfO2owfPXkV-nYfQyxpyMzp4LyLXfukKPxpbDkn65TbDQ2TNJY-MNGmzmNvmlcQCDSaOxIfjUm95-XsaU3uuoen8eyf3JdikEXbxQIGj4eVbyA3KjtnDt2k2Q2zOSzUjFCA2YG9IEz7j1v82klbFGe5lKKXQAOjK0Kj1SC-7L26sMhkZ1Lk_DUAtRQJF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌‌دیدار ها‌ی ‌‌‌امروز؛
بازی یاران اللهیار صیاد منش در دور سوم پلی‌اف فصل آینده لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/27175" target="_blank">📅 00:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27174">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOtY5RhpITtLagGGezCEk8XLdu0dchz8PfMLlVqloLHgFvm1XcXGOYPVmvvqWKGl4h6oPrtOUmwISUCT3-cihxs55OY3Fx14ai8K6nn0X5rTN0B8LJwilCQ0dePC2mCCgEbtilSdi6Efo5lBqlrdCLNI2ZeCLXLzf1OL7YBXAXxgqwaIIRc-6HCZwae_l_7ZmtxTEtEWxs1Nqg0bqpsg31ZYkbXNXbKRWMIndfnd2yFu_raKVjOBica7kDZ7sEFq3LAJaE3WLhfcFmGdSCEYPTuHPHjod_gGW5VD8vdMDl0RwznsJJ8qG_lu0aJGWZtX_LpeBgNlpfUsA9eSc5wqGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
تساوی در دربی میلان و برتری شاگردان اسپالتی در جدال دوستانه با چلسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/27174" target="_blank">📅 00:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27173">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAWTBz8ezC675zigRH84BQZD9Jzvzfgs1sUd177sMaVV02Yf4uKzzJxGMfrFqGk-9830bnZkeH65nrT4dFTTr0X5UXd1M9fzpvEqGpDx-1jk99zGusKRAznwyRgSUHaCmVuH75lmpSjm_Hnsi4o08JPTxhMBE_r6AWE3gTzEtVmEChlS8CAjnX0PJ1x3Ls9EZ6Fp_JbCogffNBGvGeH2vyntUaA__ULgsmASjhJfydorqdryaFMf4iTIKUj9W-xCOhGRzaBNYXTmTvC4NqaxxqcYYkXkm6IHmlZFtdjmzHH4r39dr34xP7ZZRpggK-Bj2Qf0c2tz8BY3fSZko2tMEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛بیانیه‌جدید باشگاه استقلال: تموم کارهای‌اداری‌مربوط‌به‌بازگشت داکنز نازون انجام داده ایم و منتظر بازگشت این بازیکن به ایران هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/persiana_Soccer/27173" target="_blank">📅 00:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27172">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Joh4B1bymKZePsuMPgAWd3H0SsmKNJ39kzjaLy7BNZpNhYNThTRKU5m0CaPBH2m_m-kEtcqgqqYTJQgyuVWmDLVyfXencvnTUAdTuG93YG85cazXj7nMXLMj3QKgyJ3Q90kfQiLQHzMfT-ggG4uFSCoM7n7fajCSaKKgZvOoJ9IJvbPpgNKIkwjmh2Fd66Hjq80e9muuktYDHPYl_HloY8_RfzBUbXudOeHZX_p5R8lLRTM9RcF4mmdwHS6Y7cmwxYpnFujdNO326E8eSkNgd59_NndgK3qziIZHHPXHTkZuKe_kuvcRykqIWhveiuIsd44_L6_sfs2msoGPd7yulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/persiana_Soccer/27172" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27171">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTH4Gz_mIim-1hl-TpAk4J6ICavekXGWhwP5-a9alKyKw_BtFcE0Z3o0Df9ZEf9Xy5otLIMBliGoIX8am00aKF__fxC9vyYxWm4xL4F1tpQhgXasWse_2Ka2ETUlcR-YfpolxxFrGvQZek6_rC5LE0jGxp6rfrchec2qDK4W_tjnzm1lNgxJJIEHm-FJ5GpgpCuQIuFmBDSKq5wiAw8donerBUfLoDVCU2o_d7mov6LjN0RjmB4LD4_cvRWtS6ASncHDIuHFPYsePVADGKgjt1zWr8ZdOr444SI8Ko5LGbWQwQiMMZySM5tKojFVisHLKQ8H_S5wVEW6vxLNU3OApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرو خبرچند روزپیشی‌که دادیم؛ باشگاه نساجی به احتمال زیاد به‌وعده‌اش عمل خواهد کرد و دانیال ایری رو پیش از شروع فصل خواهد فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/persiana_Soccer/27171" target="_blank">📅 00:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27170">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQwRQ_4eYDXeA01bciFbMjkfXpjD_BdPZV_DdQ_HjlLlgk8ILC-MRUCFa8Su-hBm92-6E67q-E-VlrSZxnYx026z7gv7T5BDItmGZ0rBXVP3pxND15FKw6EDZNV0XxROj7QAGE0DcpZa8X_7Jvv4hNedrbSInwUWGQ1NYHlfmMpjGIR_5lTn29gU8Ugo86LYMZuwjV_LfCviZlYmBsyilLIb-qa9In6biIiwCFH5Pf_PMqfzpbS6K7spzURHtsN3Ot_LjIlw6YQSbsJSIqqVzctqr5SE2v3jLuv87hIaCfYVJ9DfNNs2NHds5kiAFDqDS5W1cPUYeQieUy2HeNUgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
وقتیCR7 از اسباب‌بازی‌هاش رونمایی کرد؛ كريستيانو رونالدو با انتشار پستی در اینستاگرام از ماشین های لوکسش نوشت؛ اسباب بازی های من.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/persiana_Soccer/27170" target="_blank">📅 23:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27169">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAMArbroEmytxAjQARer5HK68J4r1WnTIHST7OCMPVceIgFdMbECNu1NnAZ3PNE7p2cqFbwrOBcSNF7-iJvuyF47aer1DwyX1vlpvvIS813c28WwHMjcJJCzo5aO4FPS62iwpKFgRUj7ofHNwX9AlIGbivebd_KVf5HVRXSuGadm21OpF7ZoonZMo-4dfNLuGpMdXgJl3P9bxCBDQn1pfHbbd3UAhWGzYZbh9u50_pUsF4z9eWfOJEaIjIWwtdPSI0pnJXTGgyfBWxHV7JcDtRvIvSQ5TSDwAvqWd8nEbZV2ZoEZWAORp_mJP1efd9C8_Y7dD1Zyv0JQwoefbv9kGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
توییت‌جدید علی تاجرنیا رئیس هیات مدیره استقلال که غیرمستقیم‌اعلام‌کرد که رای دادگاه عالی ورزش اعلام شد و پنجره تا نیم فصل باز نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/persiana_Soccer/27169" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27168">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUSt3bAY_qXLH7UUXS_JHU_qO6zSQ6wMCLIYVFCTV2DKdKYhlJv4ZDH7gA9UDBZu2OkScgqaM0kIoLuxdnElo1Z0ylNbpjWv3huf3JEq2Uxq_lK_hsF6UFVABW8ZFLQp00g9BzhJ-xwiZmOLVVe6x_VGuQJA5pxfAoGM0Cu1vliriN1ctszozTMWaevW3Br-P9rXX1XqfzJ4_Q4hBxM1iCXdphpLU6K4QrqNwadfOyCGZgCmom8uHgDEApCxbHLFlmZsjp4KO6pT4XcgABAeYiqOruCOQ1Cgxfoh2wEfeEjXHbkoPSPzbVUA8k27mT7CnDJtDfcbWkaVXAwqHjZ0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
ساعتی‌قبل کارت‌بازی محمد مهدی زارع و محمدمهدی محبی دوخریدجدید پرسپولیس از اخمت گروژنی روسیه و اتحادکلبا امارات صادر شد و این دو بازیکن جوان مشکلی برای همراهی سرخ‌ها ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/27168" target="_blank">📅 23:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27167">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Zu5Ngub-Sn_KAqCqodKBj0Agbwo093hl1WeWjKY6HiFZ4W390El-qrdL3Tlvd0t3pEq-1BYQtdDukqhNzoXa9HQJ4ivR1uvqd2Pw0dG5h_Nopfk5QUjKOuqOPgHvJH5z5e9Wl4whMuKyugs8VutOwxwp9e1IOgPLB-EmtgBWR6g31xeJrLbnO11LxIylLeB77-R2Qcs0D5vxI-QjvKNUdNhWaE5iPMIjKjdT8KTZ97z-kY3WH3ocwfJNk8s_X6l1VLWXG1rKSRRpU5GXN17i76iLFeSxc31lpA-YZ0507-v8HyjtEV5GV8yC4AatXfxiCpTrnJJez3RygDhvLygZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Zu5Ngub-Sn_KAqCqodKBj0Agbwo093hl1WeWjKY6HiFZ4W390El-qrdL3Tlvd0t3pEq-1BYQtdDukqhNzoXa9HQJ4ivR1uvqd2Pw0dG5h_Nopfk5QUjKOuqOPgHvJH5z5e9Wl4whMuKyugs8VutOwxwp9e1IOgPLB-EmtgBWR6g31xeJrLbnO11LxIylLeB77-R2Qcs0D5vxI-QjvKNUdNhWaE5iPMIjKjdT8KTZ97z-kY3WH3ocwfJNk8s_X6l1VLWXG1rKSRRpU5GXN17i76iLFeSxc31lpA-YZ0507-v8HyjtEV5GV8yC4AatXfxiCpTrnJJez3RygDhvLygZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/27167" target="_blank">📅 22:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27166">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=axrVEZ3HqyMnm3xfMhW9rDQxQtxd05T38aAMeFmufln7Um19FwE9Kn8LKEd--o1M2lUfuIUZuWJYqY1qkPJr4maThVs62zvaNF4My0o540EXzUVkmYckYmYFPXyI1jIBB0ehvAkdC5UvXlkbtSoDGNTn9nmYS0jbzbDCTCs5yayJJMw3ZJfxXi_vm30t_2unTnzljHeU8Pu2kTUOEEqQJ9RTrBMYrGM5tTqa59CWbx7385VWDi-paY6sNuzAWtgyNobvtQeLyBb035ctIgw5RezoMJ64ah2Je7aTKbg10wpjpazXaoBScnDagJIZFJ-0wBr9jvMC5QHeMReX2Jn4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=axrVEZ3HqyMnm3xfMhW9rDQxQtxd05T38aAMeFmufln7Um19FwE9Kn8LKEd--o1M2lUfuIUZuWJYqY1qkPJr4maThVs62zvaNF4My0o540EXzUVkmYckYmYFPXyI1jIBB0ehvAkdC5UvXlkbtSoDGNTn9nmYS0jbzbDCTCs5yayJJMw3ZJfxXi_vm30t_2unTnzljHeU8Pu2kTUOEEqQJ9RTrBMYrGM5tTqa59CWbx7385VWDi-paY6sNuzAWtgyNobvtQeLyBb035ctIgw5RezoMJ64ah2Je7aTKbg10wpjpazXaoBScnDagJIZFJ-0wBr9jvMC5QHeMReX2Jn4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27166" target="_blank">📅 22:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27165">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUxO2L_28CxIdycrLDWFIlySfxtGQ_wjKlwKKcWg1XDRae4FhuKCx6UAS8H6NR_GMFyDT8ngH2xkpUDDQZFYA3eQsAbp9sJMigrBX1qY7vdgBYTGKRI_2FcOIPpvMyRzSUQ6ZPDVXPOL0di9R-zFD3h4Lt675pzlYCS0vl30LGiUm8EKH8jOvEjdOfZ3CSIZhzjYQ4EbUSYCrurOYK6ZjMW6FoAY9mxO7asuIgjn6pju-q3U842SZo5N7L3WWiDysBYQwktp34AazsoH9aTw-RLY8azuer3gO-Gp0jaZ7pAIrJ6IsH3dm1NJL4KRi8jvxhjI9TYWmulKFOtOQMz2CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
🔴
مدیریت باشگاه نساجی به دانیال ایری قول داده هر کدوم از دو تیم استقلال یا پرسپولیس رقم مدنظرمدیریت‌نساجی رو پرداخت کنند رضایت نامه این‌بازیکن رو برای آن‌ها صادر خواهد کرد. ایری در شرایطی به نساجی اومده بود که از مدیریت این تیم‌قول گرفته بود که او رو در…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27165" target="_blank">📅 22:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27164">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s21LKRvGV90vp2A5PscO0pN_h1vrxqeP9-40mSQfCR1Si528VQVVY0GgK6VDYFdf4xs9G-CHobsrmQmHSmSF4Hq5VUhm3mXGJ_j6NNsSeZ_f4sbOzU_NdXqh3LApvAtnIfv-WmoGibnMK9g6EKK2SXIwriayaSkhCwgJeuOBw6P0raSyC3W13XzkwpifxT94uDZdX3k6DHuwloHS-MJxbP1GV_mAw99Imk1f89bK42e46s3bT_BhyduvZmjPki4AOWF7-hsXq4McjqOslIceS9CHzZKo2b3chVZWyJcmyU82A-kjZyH0EGHvSJLnpyb-5NlelBfP_gGnsOrqcvgrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده:
وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/27164" target="_blank">📅 21:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27163">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8x1U79MCk23KzHozrfpFJgZJwq6-uMPStekrgSkYq-sZQ4Adv9IYT41OfD0CBXra6d3EKIDz8NtoZOikb41Xynm10IsxDsz_jOc07hY2xOlNkdikntVsMrBcVtK2qwFSouAQvh2Nx-lj2bWt0NiWdewS58ibMHrsWDCI46yJNFJmtczAACng2ztiJzr_CXcCPeOAP-3phkqv4yEs91d62uV-KjuD2htdxXLWNGip9KAfz4wtjTZXSGnD-Sgv3CaztWiG00fJUU1FjIFZPT8fATr8I5pQzmjebqXWxa-EMUycXwySoMPROz8n5uzZs5kx0z85nEVjnSWTkShoOe6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اگه‌اتفاق عجیبی رخ نده؛ تموم خبرنگاران و رسانه‌های‌معتبردنیاخبراز موندن وینیسیوس جونیور در باشگاه رئال مادرید میدهند‌. گویا فلورنتینو پرز با رقم درخواستی این فوق‌ستاره موافقت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/persiana_Soccer/27163" target="_blank">📅 21:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27162">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp2D-7r1XJbG8moMuTO5N13bD48rzH2OFdeEAm9ZscGj_XKcWZeNkRPYvuo8W_UJi3qdiUHjYD3aJipFyaoAoYn-FM4Q7w3pX1YL6WwLUyYl_G8jcKLqDctM34C8d1Gjucji-kmU-PciW5-Ri_ibJadEIUjH_fWaiRcWRp6fTsrMggJ0cqdVGj4BOqb4io4sAIjr1wE4r-HntdXxMNSpdOfG2qYRSjWf_0BCp909NX_vX5F5ZrPQzxxohRCLT67kXpn3kkclWGFx1z2floa4SsYLxQmX7MZntLJ22A3V9rSv0whBZR8QK8iKTw24fWzXakhjEW3k80vRcci-2sgTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق ادعای جدید مدیریت باشگاه استقلال؛ فردا تاظهردادگاه‌عالی‌ورزش"CAS" رای‌نهایی خود را درباره‌پنجره‌آبی‌ها صادر خواهدکرد و به صورت ایمیل به باشگاه استقلال‌ارسال‌خواهدکرد و باشگاه در بیانیه ای اعلام خواهد کرد که پنجره آبی‌ها باز شده یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27162" target="_blank">📅 20:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27161">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu9oq92uh7q6zznhoklAjWZInHgw7814jusFWALGvT-TuRjxjmLdvccTBclBnlwIaQPFZHj1y57zCmlIb7oZogqxzntglj9jin5al9O1VsBS7Mi0G21yKccdt9qQfAxq5VXwsLaVCUp_sY4t_oIlv2AWOo5jr9FG26iCkHWrCpYnjyKQwc24A13g_H82zaH-e0JQHlBNgxIhGBh_LJuUz-JH5ohLewobMZXUzT11-R_l9quuCZwg8diCY49RjMiCQhysBvnhxWtyEA8Z5KZ0JOTB9suWwwKeL1IA3iistyPX7xSmB5SOqBupuSkKPFdiSNaMpKauUELfMNX9_VmULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
ادعای اسکای اسپورت: وینیسیوس پس از مذاکرات با سران رئال مادرید دراین‌تیم ماندنی شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27161" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27160">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmsuH_Gb_WRAE8Ajl2T2Eg_myyKgw7seTdtR3lJPxm7LzVGnrTLeRP4PYTnmhM3mXIqOhWaPoBusrZmkvkIDb8e4SQ7ZhvnHYVMaB0XZ5BxxsljuqaEOj3eGWJbg09aJddovIPTrzYeXpS7hCP4jF0Xbe2xBGxkrfeWuI4fvSOjg-chlKtI-qUYUmUrl8fitiEQDizgeqxiOkQxq7fHSxy-0yytnSlbABa0D4VbtoKjv0aitWgT4vkvMuQeAgAXY3sZssHXlX3_8sWR-lDNF5bR9A6HuMROxaiI9WYpdOtXC3WoLsS-s0X0DtGP2y82Nr7MoEsYAHEAE6dSKNufJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
باشگاه تزابزون اسپور ترکیه با انتشار این ویدیو از محمد صلاح خریدجدید خود رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27160" target="_blank">📅 19:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27159">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cC9YqYNvk2-Ct1y0EC4YruZh9BquT74NqUQ3PWN5A2h6uWhrP7rv6yRdTM--dN7Lz9Q0kSKjGfEMzxavqsCHFQI73ZLIlnmUo1wBfgzSUudJljR3jg3Hgy2eBeH3P7CQbyTLWQpPTcA3Coj2i06gPG1CPWiFj1sPATR-PNsiMYQCiHLZb0OZWNB-fEpuIRYIx-2JmH3AtoHv3gDR23QggaagfnetfSV-urV_TVFlOm5JyeBhT1S_pdKzy9DTKU_MlFNSKR87spXZrE5RDF9tFPDCFqGTzPB2Sq5yTrcDA8wDxobZpckzXZrcdhSDIIJz473u9BhMt8ReEyguGErIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بااعلام باشگاه استقلال؛ رامین رضاییان ستاره 36 ساله آبی‌ ها بعد از 1.5 فصل حضور در این تیم جداشد. مقصدبعدی او بزودی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27159" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27158">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k99Z8Vok2JoA9cKZsr3ADRGghdqR6fuOfkA_II4PlsJYpphnWP4tjEBp_Iug6u076U3dJ87wcU8YsXtEZmHBx777MvTwXw_E8cNMtOAbDKNWmdi8bl8Jawv8pwtt0X-uJHyXU65Pz1vngO_LHhot7fnppJEL0bopveRUnhhaaege6DH6QEpN46CxuVkEGv3ojAlR0Yi6cfdfZfsN-Kd95gIc4RGlbqA50eBf6xoOtNU-E3zBfQ6mi_DRVvV2VKiYiLevDUc8GBRbU-ba8k0YO2nwu0SmIlOfdQqKCdRXeDjMJXHuaZQuoaXDHx8B2lAK5GoJocL8d86IhCbOwqbwVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ امید عالیشاه کاپیتان سابق پرسپولیس باعقدقراردادی 1+1 ساله رسما به تیم گلگهر سیرجان پیوست و شاگرد سید مهدی رحمتی در این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/persiana_Soccer/27158" target="_blank">📅 18:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27157">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb9aoGurehpwJEnk998zKko161JaYnMaWhUC5o6M7aozti6lv0XaX5ILPWLXQ6qKMyLX64Pb7bQSE3XsIH4RyjtAVHrgkuPXXtTfG8RftFARevivDEFAjYQhMW_yRx6r5Y80dUSWvML9OgqknuXwht3YO4qXXcINZk93jNT9RHaLsh7GoD1rH93PIR37nYYQnLBmihkJn_-QiFYXQgW93_jkAAvMJ7G1RebAOJXr2_8hNRJ0DfMxkHyd6acfv6wHVbxUkCN9iIlMOFBr8tQVNsCabQl4bBWyfCvdZcodTLUt0TRc4xJ6W0Ihr8mOhtfEjlE8THQQrcn2K5suNbuiUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
خوزه فلیکس دیاز: مدیر ورزشی آرسنال به اعضای این تیم قول داده کارهای انتقال وینیسیوس جونیور به این تیم در حال نهایی شدن است و این بازیکن فصل بعد قطعا در آرسنال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27157" target="_blank">📅 18:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27156">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7xY2V4WMsrbPM7p3cbgU6AQs_RXf-M3PSC1W4egb1dQhM-pvyrQQ-YnuBrL_X_VRqMSDD_GIx4b992UC70H_ND0DD7FZpp2n2zbcGeCLlKYukBhRFIeWWkX5jwj7k_GGAEnx8MxmaEqLC7uh07HCQKX2p4Fv847jH1ZrMsLL4HM8_GXMeQu1X2Ny-S1tkpfPI1pe3iNGY8oRzGa9Blbnj03DZ8QxlC3VL1nHk3lBvf_63av6J6_GDblgUKrh1s9WvWSAGJfWkRxKezw3wg4v-T1AOE47MK8D8krcaPoafo9JQxondkHd7PiUSJbTu2M_KxC0r_sZUY-VgyAVtmpSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعد از کش‌وقوس‌های فراوان؛ امید عالیشاه برای عقد قراردادی دو ساله با تیم گل گهر سیرجان با مدیریت این باشگاه به توافق نهایی رسید و بزودی از او رونمایی خواهندکرد. بعد از اخباری و گودرزی این سومین خرید گل‌گهری‌ها بود که سید مهدی رحمتی شخصا با بازیکن مدنظرش…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27156" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27155">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNe8MqPKRY3B9yCQ6xkEkYV0BkJGkUCNCEoV0D1qsfUUstNx-NhvovegPHwB2C3oid4MzvPKn_136IchNLB9fg633TP7sfvE8apEwJzoJjuiISaUlWL2_wlCAH8SpW4ASvYYyPG9-pK2-tLIUPVhoIusTfzvrsdRmndmRq_-YeVbNYYQM1_Jpn0kk7fbK40eS1EisT8wguGvXGuwR-aiZUU4bMUcmWdj4GF8t1U6IdLU-39Q-rvTb8XAdk88We_5uyUhdARmj_ZgSdGdN8BQ0_V8iK9OOdbi5xyFeMRTXGapfDRiVRgDQBN4WYVpmIYv9u3O8pJHOnoTMgY-hrZEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛ امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27155" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27154">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfaij5YwW8IUf1a_omY5qPe_KCAGtiToQxxhtbypsLlgee-S22ySYwl8gIOVCAxF5nDg5_SeMp7gXwALezkcI-TwHSJ0WZmqU_6Ea8Dj2gvDPEHQoHugYyJXBAxQ1vpyPc6NDrhQ8iT4KWGxgYeDALCj2Ok9s65ELWpvwE1N34yAl6UFzABlGsmAkI0s1mR0QUBRcsif01ls9vZIwXD05EETCFrVmYmybbtjZ4LrL4NGTcXTUE191blyykKVhvyYDzktQxqpBsQClZOkF_t1zimh91hQOCAnbibCf1DVQ25EnX_ErEiX0kJSQNLXoSaopO0SZel4Mes5baYMoeE08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیررسانه‌ای‌باشگاه‌ماخاچ‌قلعه: ایرانی‌ها با کامنت‌های پرشماری‌که در اینستاگرام برامون داشتند حقیقتا دهنمون رو سرویس کردند‌. هر باشگاهی که با ما به توافق‌مالی برسد و حسین نژاد نیز راضی به این انتقال شود این بازیکن رو به اون باشگاه میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27154" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27153">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=nxYgKzkAYJV-qEx9LvwGv6onnvyuslQxrmfifUrS-chdzBZ4WX4fddZ8Qhl1KtOXg6hwaeSqMvnF7r-dNcCSGpn_yntS8RS2-DkJYhDGU0Rngtg5yUgSyw-i90o8AkZReB7uaQevkzWv2CYXkxOj5JvU15BqTijrfg_-ecpoegwkzBbCgVguz1YGz4TABO4eOML-6rvLyM_5SVRIaVO4UMz9GRqm-imR2hfmsMtXiIrNADWmY-KzU0zuhsx2SBO7NSCtQ8798-xzMuZHlwyg7ycd0MxQ1zNsTxHl77IKRJDvBMfOxpBqCaDG1_gnJem45vm56mCj1s2183oRYM5B-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=nxYgKzkAYJV-qEx9LvwGv6onnvyuslQxrmfifUrS-chdzBZ4WX4fddZ8Qhl1KtOXg6hwaeSqMvnF7r-dNcCSGpn_yntS8RS2-DkJYhDGU0Rngtg5yUgSyw-i90o8AkZReB7uaQevkzWv2CYXkxOj5JvU15BqTijrfg_-ecpoegwkzBbCgVguz1YGz4TABO4eOML-6rvLyM_5SVRIaVO4UMz9GRqm-imR2hfmsMtXiIrNADWmY-KzU0zuhsx2SBO7NSCtQ8798-xzMuZHlwyg7ycd0MxQ1zNsTxHl77IKRJDvBMfOxpBqCaDG1_gnJem45vm56mCj1s2183oRYM5B-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه‌دو دیداردوستانه‌امروز درتور پیش فصل؛ توقف شاگردان‌آموریم مقابل‌افعی‌ها و پیروزی راحت سیتیزن‌هامقابل‌کره‌ای‌ها در دوران پسا پپ گواردیولا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27153" target="_blank">📅 17:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27152">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6wH2nJegENO7n1jGobOY8wm_93QYWRBuS6lPhZXSiSsBsipVcIiUggGjr-G1EVnqkqDyUrCwOy1AfmPiGOBbHVZI9ZgTvc48DLKnRKCQ-pQgfGS_C9GTeGsla_Hxs1wApgc9YU3R3FyHwbdmXy6RES-kNBJqABypUcGTxX1hBGNuJia8xV1-OItgNV7RqOwO6GDn47bYoMRhtVKfpP1dY8_uh1M8hzo1Y26PMhm3RHHZH1MYgTuiTOmbhAT8xZjEMmjWFC7ngA2gNPf0YmCCzMf5RuQIribHXJYqUavYbFI7rSm3o6M-us2phtJLfMF3R2F_htQ9VMWezj1KN_Yuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27152" target="_blank">📅 16:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27151">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anNa7mpyBdnuV4zqlU3w69MNf8rcvekAPD2Kb8ke7JCFM9KSXcxrrjFYQubDaGVSKkEPryXgsmTDdftYHYROfEXvEA2S5eL-yeQE4Z33cuJsayvJKksgpfqk1WIC5e3tHXfo3plaXZTc0jRgvTQ97HyxRjBsOeMXRit1Y8LcKRUbpJtfUa1wEuajRtPbjh02T_9UxJ_kYkkseuH8SJmEOIm15_w5m9YtZXn1kdyVvvgO3JsqIeDh_nGWMHCD35PVzjuhF2YsLVJEuWbpBkx41JluEa4XrkLIeFIJnHE7FEPHQJFfX4v0S9l12_82GhbEdGdcETsNN_k85zajvBJYbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
#تکمیلی؛ امروز سرنوشت وینیسیوس جونیور در رئال‌مادرید و پرونده انتقال خولیان آلوارز به‌بارسلونا تاحدود خیلی زیادی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27151" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27150">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=CALgPsfQCTsu0CFxRb3o91JgwhV_-n7JA38MwhJyM9va1KwYxLUs9QTyrBvBF2d3V-ZJhJXzGMW97anej7WQTNkjyUSHqM4MJfpwSTlVIkbQ68bIB2W0Vkp0_AgtOWzQwvxv5hTr4GuRtstNLU65k79HE0nurxA1ZIr6D7mSLWUs5nkvPG8bLdTxeytH-hAupUpocBGbJABfRTedSnYLlhvTg17N8fYuJ32DT-pzd5yNBAML0qXPWHzoyOU73KgSI7Yx5VOfI8cslAtG86o3DdbPEhiqmy-G2M53LxnEUg5-1w0rKx2eFN0gPmjzCxc2UCkYpA8_WkI4P90ACcwkeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=CALgPsfQCTsu0CFxRb3o91JgwhV_-n7JA38MwhJyM9va1KwYxLUs9QTyrBvBF2d3V-ZJhJXzGMW97anej7WQTNkjyUSHqM4MJfpwSTlVIkbQ68bIB2W0Vkp0_AgtOWzQwvxv5hTr4GuRtstNLU65k79HE0nurxA1ZIr6D7mSLWUs5nkvPG8bLdTxeytH-hAupUpocBGbJABfRTedSnYLlhvTg17N8fYuJ32DT-pzd5yNBAML0qXPWHzoyOU73KgSI7Yx5VOfI8cslAtG86o3DdbPEhiqmy-G2M53LxnEUg5-1w0rKx2eFN0gPmjzCxc2UCkYpA8_WkI4P90ACcwkeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27150" target="_blank">📅 16:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27149">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvSdRB-nBMfQnyyR3a2WXy28CnDRxc_nBpqRJ21mMDVMTiX8LzDKroKbXSTf0q8yHYPoX4tNhcPo0EjsvY9qVPtGQo7lsSR3uy19rPmvd-lWuqJSBkGPL3F7LMJEey4BvDgmoIUkYqcwlMpuiTo8cGmU1ssNCdoaRNg7rU8vzK8c0TEHt-7-AursB_jqw0ibcz_wsMnuVCU9rs6yeiMi0lTggrMlLjbhTzOZ0VJbdnVZCN9VmF_aQlUBr7VO76WETY53HsOvCEarY_xG2q0Rj76Y_cmFEnd2L9_JSM416o24WoK9RaQAMeWOTHLeGoPkpvAjmALvlqX4MFTd7uubrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
چه خبرهه زیر این پست محمد جواد حسین نژاد؛ استقلالی‌ها میگن بیا استقلال، پرسپولیسی‌ ها میگن بیا باشگاه‌ پرسپولیس... اون‌ ویدیو هم فن پیج‌هاش ساختند. انصافا شاه ماهی نقل و انتقالاته. هر تیمی بگیردش برد بزرگی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27149" target="_blank">📅 16:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27148">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315f795088.mp4?token=jv1fNbD-DQdHenSsl6lc-sevsUnfQk9ORrpkiH33e9LrbHv-M9Op1I55dWLx4W2UXdjXS0VOR01slCWoohDGNh-6ercy-_KtZh13TMzlerypYvxghDDIz4sywkx59mJApgB0sk9O8m-9B3Ylhf6Q7xpEeh7DSSn-YYBHY1ymD8B0L_XIfuKtOs9sknYXtvF_i0rxZ9kDYaP_ehpvNHCeeBS9EGAKWM4vPt4QVIfHoHIDcszrH42GzVFVTZodi6ZRKkVTMzBd7_Wy_VF8iFue24CHl1BPG7x9iyvLsoMINZDWVLnryfhsmGLfWQPWyiWZFaB1i3jCyu7pU7AB7h1W3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315f795088.mp4?token=jv1fNbD-DQdHenSsl6lc-sevsUnfQk9ORrpkiH33e9LrbHv-M9Op1I55dWLx4W2UXdjXS0VOR01slCWoohDGNh-6ercy-_KtZh13TMzlerypYvxghDDIz4sywkx59mJApgB0sk9O8m-9B3Ylhf6Q7xpEeh7DSSn-YYBHY1ymD8B0L_XIfuKtOs9sknYXtvF_i0rxZ9kDYaP_ehpvNHCeeBS9EGAKWM4vPt4QVIfHoHIDcszrH42GzVFVTZodi6ZRKkVTMzBd7_Wy_VF8iFue24CHl1BPG7x9iyvLsoMINZDWVLnryfhsmGLfWQPWyiWZFaB1i3jCyu7pU7AB7h1W3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
امید عالیشاه کاپیتان سابق پرسپولیس بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27148" target="_blank">📅 16:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=Z-wRypbNvUohzxyaBA-_Zwju-52oT4kT1PFK-4CrFRaKFWdsjVucCzSOhrurhif6_G00qzL25QV1qgDvrceEWfEfvKKM2fvNmr5hsPY1l7NB2JhIPlKnxHKXoyf59sPhnfZi8lfVCY_yqNL86vFc-rS420HH_pxSymM2wsDgT4gE4sGvK_TkIVlpE-YwsPCmxNxnG_6z5NLo2uhxGxRgCuq7un_Dvej3Sf7yelrDR27TeWULqgTLd-iAsfV4fR1rwxHBMrmlE0Md8FPrqRzE3M4TZ370PAZgSqmxg-hSQ0m_C21_kRhH-ctyUyCwm41dLZLVqp8FSfMuX3PX9CBHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=Z-wRypbNvUohzxyaBA-_Zwju-52oT4kT1PFK-4CrFRaKFWdsjVucCzSOhrurhif6_G00qzL25QV1qgDvrceEWfEfvKKM2fvNmr5hsPY1l7NB2JhIPlKnxHKXoyf59sPhnfZi8lfVCY_yqNL86vFc-rS420HH_pxSymM2wsDgT4gE4sGvK_TkIVlpE-YwsPCmxNxnG_6z5NLo2uhxGxRgCuq7un_Dvej3Sf7yelrDR27TeWULqgTLd-iAsfV4fR1rwxHBMrmlE0Md8FPrqRzE3M4TZ370PAZgSqmxg-hSQ0m_C21_kRhH-ctyUyCwm41dLZLVqp8FSfMuX3PX9CBHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
توضیحاتی‌جالب‌درباره‌پست‌جدید کریستیانو رونالدو در کنار ماشین های لوکس و گرانقیمت خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27147" target="_blank">📅 15:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27146">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1Ct_AVszYeThyuqyGBz1oVicC48mlWm1edJTfPbdIuOuFjoQQCfR5tSLHqgJcnEE6OXeXgqHbMtSC14-gtgDaMnWIq71Qc-TH0DV83qhup0DFibgHvzCS-XEMVNSCy3P41t82iESR31GwGmrnJAIxfHAFNXTZpxAJTyZ1w2zFusQmyt0aDZvGxCOiiXWwqopD5komdr6RhnKHlDQFMlt1tVmxVhZNSTgSEicxYaCpTRab7fw7LvMTHMBzDZOiskOlfBEi41KqMflg8YhR5z-l5rkG9uOeIKlGR8lMbtznv8vtpEQiURCmYRy6ypZLcfUv7W9TpAUXCwrjmCUce3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیدباقری بادریافت14میلیاردتومان از پیکان قرار دادش رو با خودروسازان یه ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27146" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27145">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTvCSYSlmEoHYPZnH4Kh7QTg67cp25lXQ7RvQ0jJq_Rqbe39VJvabGtEzlEJaRUYe1qzGuxB7JUnSPcDGl3qLqtq8YcO7-d2Qer-4DyL6R8i2JvVbkrcfYDawcZSSZCCiTjBnSel0sm_BFy7FAAdjG3qRV_us0WpJsuJNp7UBbqcj9JDE_DmIprSBWrXYhlkIWSYf7ZoMGEjtOA9qWh1Hznmf8VPTuwqMYhMhOgV3gntrGqJcxZfxnoEDtl4EDURbFWxsx5tLyL-YwRhmfd722X-Vx0_hTY8HrRkXwX5AVIVhaiiJR9FTu88VjkXQUFrwvZc0c2VidEdOnhoZW1mVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛
امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27145" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27144">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkpxGIlSMgny6AGPV198fC9japIAp2nT8g8v7bvsZRHn1Y--aGfB3REZM4q8m9sP5ktuglWygVTU_WBYVU11aZBPXnSPoBYyDjoVsRvZkZTTeHaqTUaB7tD3EeYGoJDk1vOB1in3vn47d1I3f5d3AWfeNlwu8ADyyDyRLUooLQ6zveTfwP16PzYnWIezo7mAGMEoPe7paGWQxl-p3DSR5yCKXxTK8gBHey35U_0CJMCviXWrd4CIjhrmAsLNOPYialCSAUOtRHmsQgEXzjs8eSd5XAjDbhc5dvtHUzA678k6eP65pEI3KPj_nFsicYKsAySvkGkIqYM18rx957X1cN7bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkpxGIlSMgny6AGPV198fC9japIAp2nT8g8v7bvsZRHn1Y--aGfB3REZM4q8m9sP5ktuglWygVTU_WBYVU11aZBPXnSPoBYyDjoVsRvZkZTTeHaqTUaB7tD3EeYGoJDk1vOB1in3vn47d1I3f5d3AWfeNlwu8ADyyDyRLUooLQ6zveTfwP16PzYnWIezo7mAGMEoPe7paGWQxl-p3DSR5yCKXxTK8gBHey35U_0CJMCviXWrd4CIjhrmAsLNOPYialCSAUOtRHmsQgEXzjs8eSd5XAjDbhc5dvtHUzA678k6eP65pEI3KPj_nFsicYKsAySvkGkIqYM18rx957X1cN7bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به‌بهانه جدایی رامین رضاییان از استقلال نگاهی بیندازیم به لحظاتی‌که این بازیکن در این تیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27144" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27143">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRtqbLwtswEpVQ-dMi4596GliD8WacBvrNXk2jN6ilFQ_5Hu0gqzeT3Rz9t9Hfz1hLYlQSBet7GI3DTk6wPkKKhmd3nYqiG--n7io5Lh55XD8pgUll5J4b1Z3a4bdgSiO0CNuVO-_ORPz0x-5v7GSiIDHILk0nI-oRAsnitVSg9A6FFBpywZwVhW1I6n-oZ_LpIRrkYjl4btEr-qNaAp1k0vtrL2aPHG98V9sWokumGJivmh7Wc0KpaNLIotqj1ffaGHFxHM3Skc2R4W0Tdp6p32RZppTCoHBWEqRabaRfP_7-xPBdKf9BBW_25MC16NL5fTULz0ONpkQHZaRjhgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27143" target="_blank">📅 14:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27142">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
اولش یه لحظه فکر کردم وحید امیری رو برده اون بالا؛ لامصب ته چهرش کپی وحید امیریه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27142" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27141">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=n2gaZEz4PZ_cmPZYPdkNciISEtzS3AFXF3YjngHJ4uRh5uuuXS1LYaGL3-Z7FgcNjYPOkuarJqVthCjfVCZTcxc2R9C15LIIJCNf3JBe4Lzu6PXmXYeD9jnbGAy0agR8kRz3VgCGfkXny_oVC9BRkumRw-cNtttDs51Z_1lnWDITLEOsMg6qwUmIpj0cHJItEaZwsPrAikog0MkXnldpYYz6U8WfKBOzYt9KNPVsi0hejTHJBc9Y8XezYxwFHJCn0KIpb3ormnuH9F7l1I1Wy-DMMy3F2XWzJXO84CC8sWTm0Q5LWlPJoiiCG2Bm5g8BttyovrNaQZFF74b_oAF9XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=n2gaZEz4PZ_cmPZYPdkNciISEtzS3AFXF3YjngHJ4uRh5uuuXS1LYaGL3-Z7FgcNjYPOkuarJqVthCjfVCZTcxc2R9C15LIIJCNf3JBe4Lzu6PXmXYeD9jnbGAy0agR8kRz3VgCGfkXny_oVC9BRkumRw-cNtttDs51Z_1lnWDITLEOsMg6qwUmIpj0cHJItEaZwsPrAikog0MkXnldpYYz6U8WfKBOzYt9KNPVsi0hejTHJBc9Y8XezYxwFHJCn0KIpb3ormnuH9F7l1I1Wy-DMMy3F2XWzJXO84CC8sWTm0Q5LWlPJoiiCG2Bm5g8BttyovrNaQZFF74b_oAF9XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
ویدیویی‌زیبا بمناسبت درگذشت فرانکو بارسی اسطوره تاریخی باشگاه آث میلان و فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27141" target="_blank">📅 13:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27140">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇪🇸
🇨🇮
ویدیویی‌جالب‌ازگذشته سخت و درد ناک یان دیومانده ستاره 19 ساله و جدید باشگاه رئال‌مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27140" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27139">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DedvaNnMyo1St48u0DGur0uyx9ESnGJxX09s8DsTS0mrsprlkoEJCKtTaSXXKsJZ3d_ABdYs6Zdtwvjzx_Y8vkEmgQ83fiDylhMsIHD47C3c5dzqtxuQ056TDkcB-HFQx1cvhC7F_YkKIux2FCQuUfZVENX76GlcTqQhdtQfXNA7MKBa70WMHgGXi5h7twmMgJ7-SPXiaVwFO7AcBbot0hcNFZhMxA3hTqFTeZBt037b4XipcVojbjtuVBGJIRIxqEbHoPQEv9ysDyFs1ann1gtuNxBQyHlP1FjTpw0Xmr6wj7PVohGdTolojDLrtR1rDQ12xaD67EzaEnPeKe8BVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات|فابریزیو رومانو: با صلاح دید کادرفنی رئال مادرید؛ فرانکو ماسانتوئونو ستاره آرژانتینی رئالی‌ها در ژانویه قرضی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27139" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27138">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NePgHFuCRzKBOlPh98LP-lXFQcLlSDxJv0hSmIgx9YTPMMhst-8vti8irpWtP2DvD7aiFGlVUtNtsHz8sHxrczWm77aQIpHVDpNa7LJmD67HL3qZlWRsMOEEPOOp1tBUXjysF6n7-vthaR96m3hr5I7CJFfQ6KtQIlvUIJL4lgf3aIAudaCKP_Ay47M7mx2O_4rHjKL45jm9R9Zg9-p-Uxt52cvUOm6XmsluFDquewzBCBtvWKGfXFSP5oLajMsicaWeY84e65TCKjE1JpAoRBrHIMK-YwA2Y2_FkTl5RbZ7qwNAuN0JOdyvBjdDPIXZpNvnzTzC7EwzPWqGoQeHKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27138" target="_blank">📅 12:06 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
