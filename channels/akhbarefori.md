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
<img src="https://cdn4.telesco.pe/file/hORRUvpcKqnOS2mTyKrc7e9GrHLuFdESizufa5HIo79EUA5T_FV4RouRP2Pzfm7p11ISB60BJZNUjgGX66HLneswdv5u9KOyVau5V5iHF9CLt1xgW_I9Pwye1VNwAPK8bh18BIUkBu2OhdvgeT5h8xK5c1igCFs1Gr5bon35o7KujNWR-fmEh1crU4yQS3Qi8MZjiOKj8Qw9wsj1oTZnKQF8yd38uZ7Wt7XoEO0QFS7631-sqPqHNVZypAopWgySZe9WdlUGWh2l9u3jsZKm1PE_3uwn8fTxU5N70oNxx_VIVuTqHlpB5UXt8wy8SuxwCmuemRh-BwiLHTuhpiUPSA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 05:41:06</div>
<hr>

<div class="tg-post" id="msg-695665">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p48SWXaZd03X1AD9oW7BKcOKUX6JIvrqlNu0UoOV-7SK7B8AHznFTgluuMkhAhmH5lpQTjp2bril20AF6bFcP2VVHVaIx7AQUTcc32Ibf69CcekCvLiHk5M2sGMk_cJLgc_PShc7Rm8WvDSRjoJxvQtmNEOH6yQhhf1Cn_94Uzo2RE9pp4Sq5bXVc2UZmg8gMKYwbXTPyQE40rIYdi_SiWRfC2H5VEDyCJLVAbhoaB3cXCTauZfkWRiSY862CTY1zX56J62ABEuhvqjVN39U97Xs38SyVSKNtUwxobuKPyBbBnhOqPzuEANMT28C-oOv9RkaHwmSPV52V9WcbsGUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبری‌که همه‌منتظرشنیدنش‌بودن
❌
پژوهشگران موفق شده اند ترکیبی را معرفى كنند كه مى تواند
سلول هاى بنيادى فوليكول
هاى مو
را از خواب چندساله بيدار كند
😳
😳
✅
این تحقیق روی
۱۰۰۰ نفر
تست‌بالینی گرفته شده و
نتایج فوق العاده در قطع ریزش و رویش
مجدد
داشته است
✅
🔴
حتی روی کسانی که ریزش‌ارثی هم داشتند اثرگذار بوده
رویش مجدد مو
به همراه دارد
🧬
در حال حاضر در ایران این روش
بالای ۳۰۰۰+ نفر
رضایت‌درمانجو
داشته
به زبان ساده، موهاى خاموش را دوباره زنده مى كند!
دریافت اطلاعات کامل و نحوه و هزینه درمان روی لینک واتساپ بزنید
👇
https://wa.me/message/TUKIUT5M7IO5O1</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/695665" target="_blank">📅 00:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695664">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUYktEgb38e_210u_rnrUU3syouosvAYHiD7uk7bmJGMzg6ZCGK-c0TZquRIoksNa-w6WugOM92Z3Is3QWLfcCWx6A-AT-HSFF6jPzMGW4EWuCckHdXHiljOu8Tc_gEqh17EE0L0KTZnjBRNdFQD5XjTgBuQisK6RkXAY_pRJBXBkuMuaBgYgE3yGKY5B_thRnxn_Js6vmrYCzMiS05TVU5e11wfII4a_ExbbxTtnx06JOtZ3a7tRIAZtbOLr02l1Ft7dWNQJAQWkN84dhaXFrxhYn-J06PCSzxKg2rxPmvkLdXEzKEGN7yx4xmP3M03h4ZdyeVltN5-YM0j1kZ1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
سوییشرت مردانه خزدار؛ گرم و خوش‌استایل برای روزهای سرد!
❄️
جنس
مموری ضدآب
با آستر داخلی
خز تدی
؛ هم گرم و راحت، هم مناسب استفاده روزمره
👌
🧥
کلاه‌دار و جیب‌دار
🔒
زیپ‌دار
📏
فری‌سایز، مناسب تا وزن
۹۰ کیلو
💰
قیمت نقدی: ۱,۷۸۰,۰۰۰ تومان
💳
خرید قسطی: ۴ قسط 495 هزار تومانی
🏠
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه کالا
خرید تلفنی
👇
https://memarket24.ir/product/fast/50703/180124/</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/695664" target="_blank">📅 00:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695663">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aac7ff8f3.mp4?token=Ti67pd2YISHEgdQBAETpiEzOpo7YEGH97vkqVk2ZQQ-qIjO_58GGoi-CM1dQouhR_1ayADXj3C-V3Eikr4jY5PMKWjkURACZhGP0jqTidi7GxaObYC2L3QJoiIYHogS-4rJNnMXwF6rL04AmM368-1rgEitzFXyya-6k8nbSMND-eLpeHD56g8B9n-XrfDk4TMYr7jhyjVYrRZacIGsj2VNFh-4RXg2dWpbsr8iEw2s79X1ssMxcKZHzUy48GjWqWnwBowpfUTAH6eKgcRYjwKFKU3LD62yBUZ6BtR38todz1_3zIR4L3IcyAnUlxtY6v4RK-_vEn02YhE2Zz6QE2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aac7ff8f3.mp4?token=Ti67pd2YISHEgdQBAETpiEzOpo7YEGH97vkqVk2ZQQ-qIjO_58GGoi-CM1dQouhR_1ayADXj3C-V3Eikr4jY5PMKWjkURACZhGP0jqTidi7GxaObYC2L3QJoiIYHogS-4rJNnMXwF6rL04AmM368-1rgEitzFXyya-6k8nbSMND-eLpeHD56g8B9n-XrfDk4TMYr7jhyjVYrRZacIGsj2VNFh-4RXg2dWpbsr8iEw2s79X1ssMxcKZHzUy48GjWqWnwBowpfUTAH6eKgcRYjwKFKU3LD62yBUZ6BtR38todz1_3zIR4L3IcyAnUlxtY6v4RK-_vEn02YhE2Zz6QE2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوردن کره با شکم خالی چه بلایی سر بدن می‌آورد؟
🧈
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/695663" target="_blank">📅 00:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695662">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gsh6w9uTa4gWicoGLbhSKC5HbhzgezSc0f0s-UfaMPKKexxR2dYSvIKpBmLqNNS_-NF9fG_4GxuSV8tth-gI1wgIGlD9qpz_KODQIZddot1cugBrIIe8WObHqvJxHVqk9TvwfzqdMC0yvrE5VtlfISxk44Lpnm0v4wKNGyogGctVRJ76p6qS4LI_qJlkeSaQPejA3axJgjciHWnMSH0mD3-LLukDzfzRcDrA8ttwtaIU_tCXWvGDpcCOwF1avEWTttzrDVFCSjOwZbNtDzhnClDJoyzFQ6yWSZeGust717t5bgv33WnHh2FA5A9Dt3TC7fJSwn1klwVxCY8l-zoKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید صفحه یوتیوب تتلو: امروز دادستان و رئیس کل دادگستری صحبت‌های خوبی با تتلو داشتن و اگه گزارش خوبی هم رد کنن، امیرتتلو فردا آزاد میشه و به استقبالش میریم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695662" target="_blank">📅 00:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695661">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqcipQh1XoZ1p6Nw9X210CKHlu1njvFdwSrtTmvTZvmCXgziA1VD5qVCY9FVtcmSPM7qrBmBHEyE2aZf0O1Qn86_yCSc5T3rwjfXRAZyb3qQPP2w9nqFkoMMX7ttK5cUk26qT0W0_W9tVqah0Rsmulg7d8_-EeAR_WdSu-vUHbOXg9Mx7gvhzJOt43LKnHm6dmgVRiGTB6TH1y-rSIPBXgeYEECJk68lF_9bGjgUsQNmDda9Z6lxD-w5pUzNel9sCUGwuAk900I8NUHQhvHiEY98ZeqAE2dsCLJka5ezGJmDIfIGFYusFzROjmboEhjKEx_Dd8cTR8TvBmUoV6sLdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/695661" target="_blank">📅 00:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695660">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
فرار بمب افکن های آمریکایی از ترس حمله ایران
وال‌استریت ژورنال:
🔹
بمب‌افکن‌های آمریکایی از پایگاه فیرفورد به داخل آمریکا منتقل شدند؛ یک مقام آمریکایی نیز مدعی شد واشنگتن از طرحی مرتبط با ایران برای حمله به این بمب‌افکن‌ها و کشتن نیروهای مستقر در فیرفورد اطلاع داشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/695660" target="_blank">📅 00:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695659">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71b3a2afdf.mp4?token=CIZXfC8hPNcoQLD22koxMnunKwf3J8AOVjuSCzPVqpoRqd9_N_ZAxliPUYMR25r9grp0IYCI-37yrzhbo-zSn6u-jf0VMg-ps6_m-8isiqBjUaSpEDkTYy0kw4Zz_kx69uQvAs9npJTgGkaVS89Wm7BoNZOgxwzg9q5ke3q6UXSmsIJrk_r2SirKACU1p_5eUZ1iI5AyuR5i8oCKX_brA4dSyUMBjIt871WJ4Se7PwmxxYlXjMjN665fPemBmJrGPenLZKa7ZCQodrnO0ZoUQ2LhGp5ou7-SgpAHuERZ4ezkrPZzm_deISwmil4LMNz2HcCu1Koahm_DJ6r4ZgYSJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71b3a2afdf.mp4?token=CIZXfC8hPNcoQLD22koxMnunKwf3J8AOVjuSCzPVqpoRqd9_N_ZAxliPUYMR25r9grp0IYCI-37yrzhbo-zSn6u-jf0VMg-ps6_m-8isiqBjUaSpEDkTYy0kw4Zz_kx69uQvAs9npJTgGkaVS89Wm7BoNZOgxwzg9q5ke3q6UXSmsIJrk_r2SirKACU1p_5eUZ1iI5AyuR5i8oCKX_brA4dSyUMBjIt871WJ4Se7PwmxxYlXjMjN665fPemBmJrGPenLZKa7ZCQodrnO0ZoUQ2LhGp5ou7-SgpAHuERZ4ezkrPZzm_deISwmil4LMNz2HcCu1Koahm_DJ6r4ZgYSJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عددهای فشارسنج دیجیتالی رو چطور درست بخونیم؟
🩺
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/695659" target="_blank">📅 23:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695658">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سردار فد‌وی: مردم دنیا و مردم آمریکا می توانند خودشان یک مقایسه‌ای بین توانمندی‌های ما داشته باشند وقتی خود دشمنان می‌گویند که در مقابل حزب الله و یمن مستأصل شدند و مجبور شدند خیلی از کارها نظیر فرار از یمن را انجام بدهند قطعا حساب شأن در مقابل ایران مشخص…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/695658" target="_blank">📅 23:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695656">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn3xMon2P--BGvIdc35sifktr0JJYyHR-MBwxXE692sb8Mz3eQCoI4WSeigOmrkinUqvwG4rs_hBt78xpkNjbwVR0xBtgjuz0FgTIYbW9MJFtOJF2tDIQkPbMVqzDl0VpzUqOsrtGQjDYTmCw2yMxGyLr8RhMU2mmVZyOOlRTEGW3TjRklULjBhBAA6ADfB9w_EeZ-QRp5KOy3WMeG1q--E9wbvXgNaTWe_cDAE6yBXjqlqTZ3jHNAA86aFmFyQ7zIelihDpJkhBao3QBpvnHN3boz5VGAeH9ur33Z8taBCT38nAgFkSK6ikrlsjWB4MwKql399sukSsUki_z1AFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ مکانی که آب خوردن ممنوعه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/695656" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695655">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌹
فایل‌های صوتی تفسیر سوره محمد
با سخنرانی حجت‌الاسلام امینی‌خواه
🔹
جلسه اول
🔹
جلسه دوم
🔹
جلسه سوم
🔹
جلسه چهارم
🔹
جلسه پنجم
🔹
جلسه ششم
🔹
جلسه هفتم(بخش اول)
،
(بخش دوم)
🔹
جلسه هشتم
🔹
جلسه نهم
🔹
جلسه دهم
🔹
جلسه یازدهم
🔹
جلسه دوازدهم
🔹
جلسه سیزدهم
🔹
جلسه چهاردهم(بخش اول)
،
(بخش دوم)
🔹
جلسه پانزدهم(بخش اول)
،
(بخش دوم)
🔹
جلسه شانزدهم(بخش اول)
،
(بخش دوم)
🔹
جلسه هفدهم(بخش اول)
،
(بخش دوم)
🔹
جلسه هجدهم(بخش اول)
،
(بخش دوم)
🔹
جلسه نوزدهم(بخش اول)
،
(بخش دوم)
🔹
جلسه بیستم(بخش اول)
،
(بخش دوم)
🔹
جلسه بیست‌ویکم(بخش اول)
،
(بخش دوم)
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/695655" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695654">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2463caf8.mp4?token=g6Q4_rZTGdX6NEVWjkB28mE4IzUqjPBIBN_yAwnsjCvWtMp0d-rKSnXPYijAYFtnCmDqsgYeHuOO7cXDXQ4w23V17RPIR0fPlVl_5ZTo-emVXTKpIKt2zpS6R12Re6bKJDegiLRvqTGdqGKUY2Hc4DMfGuHmKMy3HSe3lIMBDn_k9XRN8HW3oSokZ0CDOOik10jQgvH1G3zXXow6Qe75zcUwZD4A2U1d2uZabWl5Rj0QpyKXHxGEtJD-B4W9xYUGiSxhdVrmdmkS1UXEb3Jv-yIro2mJyH-VxD3Ey0d8RRh6QQPEBPlmfVfA9583rSIXnUFnoFJ5RE1p5j3ZdLP0gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2463caf8.mp4?token=g6Q4_rZTGdX6NEVWjkB28mE4IzUqjPBIBN_yAwnsjCvWtMp0d-rKSnXPYijAYFtnCmDqsgYeHuOO7cXDXQ4w23V17RPIR0fPlVl_5ZTo-emVXTKpIKt2zpS6R12Re6bKJDegiLRvqTGdqGKUY2Hc4DMfGuHmKMy3HSe3lIMBDn_k9XRN8HW3oSokZ0CDOOik10jQgvH1G3zXXow6Qe75zcUwZD4A2U1d2uZabWl5Rj0QpyKXHxGEtJD-B4W9xYUGiSxhdVrmdmkS1UXEb3Jv-yIro2mJyH-VxD3Ey0d8RRh6QQPEBPlmfVfA9583rSIXnUFnoFJ5RE1p5j3ZdLP0gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت عجیب بازار روز تایلند؛ جایی که کباب موش و حیوانات موذی خورده می‌شوند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/695654" target="_blank">📅 23:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695653">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Da8reW74rfBmopmUxJahaHmsEVWL5fKuMA4aLhpXC72FR6SB17sYmXCeSHtK2O_J-pg-mqMxD_Ay87_GWopxBU24ztURf3sg6givPzuGLXUJ1s5xIlD6GaoJPetDdoSB738EC4t_65lZx4558EPMHxWOTyg3Z1uiRHxMAnZGL1kJbN5MkmISjp1eV38FHHHl2DkQa0cwIByvmSDqivGS4hN18v-CMeCc-KYx870vI_u2nOSa4-7sfiGuuBPtnHQ09Q_ycawgcgtsloPTKD9_Ov6Sb6naFiNUyAXWHvKw6MxNUTXDR3KsS9GT-KCNTztTXvOTZr0pXhxdhlrIvZQUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ با انتشار عکسی از خود در کنار رئیس‌جمهور چین: ترامپ جوان‌تر به نظر می‌رسد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/695653" target="_blank">📅 23:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695652">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b7bf20cd.mp4?token=TD-uPZkcBZzMrnPPCYk2kkSqahfJHhHY8YTGXSjhR4RMXUQl8yyDbQZ_STvQzEcJ32haEMWfuNoscixn5ExYo90li0qX4diZjH4qSWSDQx3xxOb-d_g8J7Bu4khpKjS7itLZxfFcvxeChLY3eT5JZ-DqCmHY4tflJzcIneK4qndGjezUpQqA2rk8DHbYv4nQw2rRxfTU_rLzifTPD4PS5glaf4tR8iGKOLH2cNkONwEgbvEggKqM67Y5Apz62t7oxFLwMriENsd-RZb3eBQ1PKgoc7y6Zq5KUrzd7RZXZ2ER3ez-aKs0pQpb2xbApCo6_wwhjtBAEFj_KkpEal9jog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b7bf20cd.mp4?token=TD-uPZkcBZzMrnPPCYk2kkSqahfJHhHY8YTGXSjhR4RMXUQl8yyDbQZ_STvQzEcJ32haEMWfuNoscixn5ExYo90li0qX4diZjH4qSWSDQx3xxOb-d_g8J7Bu4khpKjS7itLZxfFcvxeChLY3eT5JZ-DqCmHY4tflJzcIneK4qndGjezUpQqA2rk8DHbYv4nQw2rRxfTU_rLzifTPD4PS5glaf4tR8iGKOLH2cNkONwEgbvEggKqM67Y5Apz62t7oxFLwMriENsd-RZb3eBQ1PKgoc7y6Zq5KUrzd7RZXZ2ER3ez-aKs0pQpb2xbApCo6_wwhjtBAEFj_KkpEal9jog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۸ ریسک مهم سرمایه‌گذاری در طلا
🔹
قبل از اینکه پولت رو تبدیل به طلا کنی، این چند تا ریسک رو بشناس، چون ممکنه طلا گرون بشه و سرمایه‌ات اونقدری که فکر می‌کردی سود نکنه!
🔹
جزئیات را در این ویدیو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/695652" target="_blank">📅 23:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695651">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6911c9232.mp4?token=Fr7xoSlPHL1GmKAsuLzjdOoL-0xyjX-KwnqTL9byumyvUqCYorSbYw6AuM5jaxS_nBNcf8nMc0EjRx0yA7jv9vD92cUxiTmOI0ystX5ZTnTTXzLxBu00dM4qN27JoKkPgEUILSEYUbMxNghm8lBGqa1MN78m8XzklqY3CHVSPB_i7jk48Kb5kmznEd81N9TVqpA0d-tRHJKV7DpmNsl9AwcETXYP5Co3Rba4KrYFpO-mNPW-pf4OkaYGoXDGIercfWqXfIkma0lRHuVl4aE9E8LSNMkzsflepeUSdzKlH2SiaF_mQ18D66rKPWQnB_SJtOcHqT43mDGx67lvn8OYMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6911c9232.mp4?token=Fr7xoSlPHL1GmKAsuLzjdOoL-0xyjX-KwnqTL9byumyvUqCYorSbYw6AuM5jaxS_nBNcf8nMc0EjRx0yA7jv9vD92cUxiTmOI0ystX5ZTnTTXzLxBu00dM4qN27JoKkPgEUILSEYUbMxNghm8lBGqa1MN78m8XzklqY3CHVSPB_i7jk48Kb5kmznEd81N9TVqpA0d-tRHJKV7DpmNsl9AwcETXYP5Co3Rba4KrYFpO-mNPW-pf4OkaYGoXDGIercfWqXfIkma0lRHuVl4aE9E8LSNMkzsflepeUSdzKlH2SiaF_mQ18D66rKPWQnB_SJtOcHqT43mDGx67lvn8OYMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با یک لیوان آب سرد به‌راحتی فرق زعفران اصل و تقلبی رو متوجه شوید
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/695651" target="_blank">📅 23:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695650">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سردار فدوی: ایران و عمان بر تنگه هرمز حاکم هستند و قوانین تنگه هرمز را ما می نویسیم و در حال اجرا است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/695650" target="_blank">📅 23:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695649">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944336ecbf.mp4?token=nTOuB5yERH9wv6D6gVs8tygnf6BmMZXp31eonoQgXKMgCPv1BUhTheWjr3owMEtdNBX9ufEA6TY83-QMODcENvfbRWkl5OL35LYZ7qIQk7pVbVPtX-ZM8ZHlONbfVr9mkXvxXN6F2filRdLFjFlD2DciPFZ1ehgASvW1hzqt54oEa-Oy_pG-MaV47vd4oHehXdLLnjgF09zvaNe2g6T6_uRyXOZYhc36TShQGGdJZt2n0U04f0zSAHhRHqQC_DXm93OhU8pt43mFIgkc4cB6E91H178y-q1YmrzEnEYcrYr4I72vJMgDNKNwtmW5DH7W6hzBqMFY8k_9_9-2hPRCDXmiuvSJafyMxwTCXcBx_PnQR3rdJpWI8C7ZS8BnSsiydGlSFTXFJ2LsA8c6o0b86scFItBlbvQDyrMhK7aLRWiJxxsakiht23lSeQdS1JTLDj4CQpMOkBTXaiMViwJpbUVyStEIYXhQLEd9LYPzOnjsCs6v2yFR5dnVIJy4TYCa8yUQIMN2vkrqU2EIvdGFQ3_9TZerd6aAEOgNYf-QFarGFV_xUigN1mWnM0SUbusRD5IrpRTnVUbuKXts67ofgYiEJAdT2t79ybzTP24CJ7qqXY5nXZHE1EONCJJ-yw5djjq5ZHw2l-fFZOIu6jprSfDs3vQ82I-7in40HBe1F-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944336ecbf.mp4?token=nTOuB5yERH9wv6D6gVs8tygnf6BmMZXp31eonoQgXKMgCPv1BUhTheWjr3owMEtdNBX9ufEA6TY83-QMODcENvfbRWkl5OL35LYZ7qIQk7pVbVPtX-ZM8ZHlONbfVr9mkXvxXN6F2filRdLFjFlD2DciPFZ1ehgASvW1hzqt54oEa-Oy_pG-MaV47vd4oHehXdLLnjgF09zvaNe2g6T6_uRyXOZYhc36TShQGGdJZt2n0U04f0zSAHhRHqQC_DXm93OhU8pt43mFIgkc4cB6E91H178y-q1YmrzEnEYcrYr4I72vJMgDNKNwtmW5DH7W6hzBqMFY8k_9_9-2hPRCDXmiuvSJafyMxwTCXcBx_PnQR3rdJpWI8C7ZS8BnSsiydGlSFTXFJ2LsA8c6o0b86scFItBlbvQDyrMhK7aLRWiJxxsakiht23lSeQdS1JTLDj4CQpMOkBTXaiMViwJpbUVyStEIYXhQLEd9LYPzOnjsCs6v2yFR5dnVIJy4TYCa8yUQIMN2vkrqU2EIvdGFQ3_9TZerd6aAEOgNYf-QFarGFV_xUigN1mWnM0SUbusRD5IrpRTnVUbuKXts67ofgYiEJAdT2t79ybzTP24CJ7qqXY5nXZHE1EONCJJ-yw5djjq5ZHw2l-fFZOIu6jprSfDs3vQ82I-7in40HBe1F-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‌مدارس ایذه غیرحضوری شد/ مدارس شیفت صبح در ایذه خوزستان، امروز یکشنبه به دلیل بارش باران و سیلاب غیرحضوری شد  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/695649" target="_blank">📅 23:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695648">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 6- میدان ششم، قصد</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/695648" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان ششم، قصد
🔹
در عملی سالکانه نیت، قصد و اراده، معنا و مفهومی مجزا و جداگانه دارند.
🔹
با یاری رساندن به پروردگار، در حالی که وی نیازی به کمک از سوی ما ندارد، نشان‌دهنده‌ ارادت و قصد ما در طول مسیر می‌باشد.
🔹
استحکام قدم‌های ما و استواری گام‌هایمان مانع از رخنه کردن ترس در وجودمان خواهد شد.
🔹
قصد ما ترک هرچه غیر از او و روی‌آوری به خود اوست.
قصد سه قسم دارد:
🔹
قصد تن به خدمت: از جهد نیاسودن_از تنعم بکاستن_فراغت جستن
🔹
قصد دل به معرفت: رنج کشیدن_به ضرورت زیستن_خلوت گزیدن
🔹
قصد جان به محنت: نازک‌دل بودن_از سماع ناشکیب شدن_به مرگ گراییدن
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/695648" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695647">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سردار فدوی: قیمت گازوئیل در اروپا ۲ یورو شده که یعنی ۷۰۰ هزار تومان
🔹
ما اینجا ۱۰ هزار تومان پول بنزین می‌دهیم که حتی یک دلار هم نمی‌شود و اصلا متوجه نمی‌شویم گازوئیل لیتری ۲ یورویی یعنی چه.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/695647" target="_blank">📅 23:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695646">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
مدارس پنج شهرستان سیستان‌وبلوچستان فردا به‌دلیل وزش باد شدید، طوفان گردوخاک و افزایش غلظت ریزگردها تعطیل شد
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/695646" target="_blank">📅 22:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695645">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f64fad2c13.mp4?token=JRFbyeM8xNWMKATw4S_gsKFH1NFiKtUE-dF20Rc8B-RnbNRdV2MuzuB0oPaByMUSw3hn8OUkFCzjuSwWAUH5PJh-9_YR1sb05_ccXB1PSAP9OSbpfARDyuXIL0mvYNdQAKayEKyv0wNC-h0Zw14IYQoYhrsP-vQ3yiAj-jnoJEUcVXlDShaGHDqwGFcwmZ7jk94rbBpdpFo4Pj6Fwp_V1xqQ8plOU9DszztWLsNdwlUB6K88VBHqNPFNNpApsavPopRkVbaHooejyQ634sovzRPNiL3Br0JTCmqcX6PUnFCJ74c54-xGDjLPVVb4g5jbku1sXG7-NaS8FMvmh4pv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f64fad2c13.mp4?token=JRFbyeM8xNWMKATw4S_gsKFH1NFiKtUE-dF20Rc8B-RnbNRdV2MuzuB0oPaByMUSw3hn8OUkFCzjuSwWAUH5PJh-9_YR1sb05_ccXB1PSAP9OSbpfARDyuXIL0mvYNdQAKayEKyv0wNC-h0Zw14IYQoYhrsP-vQ3yiAj-jnoJEUcVXlDShaGHDqwGFcwmZ7jk94rbBpdpFo4Pj6Fwp_V1xqQ8plOU9DszztWLsNdwlUB6K88VBHqNPFNNpApsavPopRkVbaHooejyQ634sovzRPNiL3Br0JTCmqcX6PUnFCJ74c54-xGDjLPVVb4g5jbku1sXG7-NaS8FMvmh4pv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار فدوی: قیمت گازوئیل در اروپا ۲ یورو شده که یعنی ۷۰۰ هزار تومان
🔹
ما اینجا ۱۰ هزار تومان پول بنزین می‌دهیم که حتی یک دلار هم نمی‌شود و اصلا متوجه نمی‌شویم گازوئیل لیتری ۲ یورویی یعنی چه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/695645" target="_blank">📅 22:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695644">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سردار فدوی: ملوانان کشتی‌ها علنا اعلام کردند که توسط آمریکا مجبور شدند از مسیر جنوبی تنگه هرمز عبور کنند
🔹
برای نخستین بار هیچ شناور آمریکایی در خلیج فارس، تنگه هرمز و دریای عمان حضور ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/695644" target="_blank">📅 22:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695643">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4225e108.mp4?token=edm6mYkSvMxI82Lex2D71qT-Oo60P9czXxk4BrOVjridbCYy9cNz7wqmzTJ96kFJOHdRPJBShyDgiCShbj0FbrIX2VEY38YIX5MhDHiU4B6cFwGwzghmGsku4haswXRBZttuirdcY5rQFptj2Gz75M7i_0Or8OHHlrumV54Tgn3F_F6-4yW1XgOr3a3ATqmKzJfjjHm1mRIsCYIqf8bkijOJhvVjdIrvXFdYj2ZdHX4wyWBVxP1LdGMd-GmeJtgXMhYRhnhrY9c69JPUHkY0HMxUcrmByq4_kJyv6EFNPdubfBuwcqZCFAzgqPro7tWEyhOJ5WbaYXPgZzfikN-PbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4225e108.mp4?token=edm6mYkSvMxI82Lex2D71qT-Oo60P9czXxk4BrOVjridbCYy9cNz7wqmzTJ96kFJOHdRPJBShyDgiCShbj0FbrIX2VEY38YIX5MhDHiU4B6cFwGwzghmGsku4haswXRBZttuirdcY5rQFptj2Gz75M7i_0Or8OHHlrumV54Tgn3F_F6-4yW1XgOr3a3ATqmKzJfjjHm1mRIsCYIqf8bkijOJhvVjdIrvXFdYj2ZdHX4wyWBVxP1LdGMd-GmeJtgXMhYRhnhrY9c69JPUHkY0HMxUcrmByq4_kJyv6EFNPdubfBuwcqZCFAzgqPro7tWEyhOJ5WbaYXPgZzfikN-PbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروهای یمنی: شهر تربه به فضل خدا آزاد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/695643" target="_blank">📅 22:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695642">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq-t80hYLWO0RRVJLkajIhAnOcKLe-xnYm229CN9FCbdQ6ux4mSyb6GYKzxdFwy1Siu4UWTF5_bLp3s-RjEtRVezcms_Fn8iQ8lRvFAUQyGJMd3ftMHhuCLJP40PI8SLdJM2KPHGOrpCXAIkfipCyArfc8oLAe3k2rraSPHwpVdfrLtjrMsoK-KmD6FhoKwVq5bpyAD_g5gZTSRZzFZeJpWS2aDhwVCGtpUHYxr727vZCQfBCmN1EMUUtMwvf73GR80sDpZX3Fo-sBCpQnE3KMBnqPHQ0ddsFocvXc70selOHi9gzU2X7JH90orbZdpZZE-wEu53XoWt3Px_1AdSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ مصاحبه رتبه‌های برتر کنکور، پیش از اعلام نتایج در فضای مجازی وایرال شده؛ حالا سؤال کاربران این است که مؤسسات چطور قبل از اعلام نتایج به رتبه‌های برتر دسترسی پیدا کرده‌اند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/695642" target="_blank">📅 22:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695641">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سود اقتصاد نباید در جیب رانت‌خواران برود
پیمان فلسفی نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
نرخ بهره بانکی را باید حداقل یا صفر برسانیم، چون بهره بانکی مشکلات زیادی را به همراه دارد همین امر باعث شده بانک ها به سمت بنگاه داری و فعالیت های اقتصادی بروند.
🔹
الان با مشاوران و کارشناسان و مرکز پژوهش مجلس و معاونت قوانین مجلس دارم برنامه ریزی میکنم تا اقتصاد مقاومتی را به یک وضع ثباتی برسانیم.
🔹
تا زمانی که نرخ ارز در کشور تثبیت نشود مشکلات ما ادامه پیدا می کند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/695641" target="_blank">📅 22:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695640">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQqok0st5dqaNtxGHDKBN7stTnlREwKuuz-QoEI27UcLCjnI4-c5XvZEKiDYDwqN0r4j4kDPC59ZwN3tW8t79-PZH6kTblsseyFFEdVbaquthtsCKL1L8Rqt60R8DMABwxKKMO9y78v-9oxPjFskMkR-XTmg0Aug5z8_5pNi98jY9KUEcPPRvnjNIRAEArY2T93i8YYUOAiIT9OWincMDwWeyFH_76WjxdHh7TEtHaaP2wv-aUp8UCjCMiMyIRpQpiXwPw_vfrQjaG9_t6Edqy7h5rB0ABBVVJeC1dzzSlAoXxw1UroxoDLRe_Ei8Ubp2ySK4viMoVF8tbwG2wI9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو در پی خداحافظی از تیم ملی: یه زمانی، همه مردم پرتغال رو در جریان حقیقت و دلیل واقعی رفتنم از تیم ملی می‌ذارم؛ تیمی که همیشه برایش همه توانم رو گذاشتم و از هیچ چیزی کم نذاشتم. فعلاً فقط می‌خوام برای پرتغال و همه هم‌تیمی‌هام آرزوی موفقیت…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/695640" target="_blank">📅 22:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695639">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEhZ-WaCKz_62V_OpiZKpy_RSda52c-N_jJUMokiGETvL0CMD553ETd0nlFED6Pc2-YXhVQXFpZ7fNCUA19DO2EMjIW5zmVaxwL6iQPDrnIDM8Mu4Y2HkJZYrgBUny-kPVctD-heURbMufrX-aDIEwqYvJnmDyBuqFlll_wcTqeNwwHL_LjfzVxOWRZIzFe9a3jycDhXto0DKUDt77AzaEh8kLaqtI7V5GQ5WgQmJv7fT4w1s4h9w9xF6uHumeeGk1IH9sXOgxAovJqb3k7PYrEVHpoVgnzF_veKBlvroKXTMOFJl1laMBZEJruvHN6qclCU979MV8K3x-X_JH8Lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای مقایسه قبل از خرید، بیمه بازار داره!
وقتی می‌خواستم بیمه‌ام رو تمدید کنم، ترجیح دادم اول برم سراغ
بازارش
!
✅
چون می‌خواستم
قیمت‌ها
و
پوشش‌های
همه شرکت‌ها رو کنار هم بذارم، با دقت
مقایسه‌شون
کنم و
مناسب‌ترین
تصمیم رو نسبت به شرایط خودم بگیرم.
تازه، هزینه‌ش رو هم در
۱۱ قسط
پرداخت کردم؛ بدون اینکه دغدغه ای داشته باشم!
👈
برای مقایسه و خرید بیمه وارد بازارش شو
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/695639" target="_blank">📅 22:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695637">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiVr7V-mi8k5elzV0QdqqAb27WtsHh7RBHleGJlieIgpSkO3n0qCCXTKX91WTlhdZ1RnQQeCjzGbg3cMj79b8arzgCf7d-5v_JtFVuyY0lWUfSW6vPlHEIRCUUs7gM4Q34YOfBi5f8EdAz31zE4s-00C-_AGGm-o-mGidbZikBVY0_3El75wlAY4akNYCKvOooYowPFq1f8IprACnUS7NwL2Y48bvcnHitwApjnKlvpqcmQCGpFdPEtIhh-yY32kd595CMObS9EQ5MEfbSpOUl2uxsEpELiUPG8T7jp4Jyb0mgYZMkvGL7Gh1Egoizjx38VrHXo_uIV0Y_uYoKK-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: گزارش های مبنی بر
حمله به یک کشتی در تنگه باب‌المندب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/695637" target="_blank">📅 22:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695635">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تغییراتی در کابینه رخ خواهد داد/ دولت شروع نکند مجلس دست بکار می‌شود
علیرضا سلیمی، عضو هیات رییسه مجلس:
🔹
از هفته آینده و با مجوز شورای عالی امنیت ملی جلسات مجلس به محل قبل بازخواهد گشت.
🔹
بخشی از مجلس در صحن است و بخشی به صورت مکمل و وبیناری برگزار خواهد شد.
استیضاح حق نمایندگان محترم هست و باید روند خود را طی کند.
🔹
اولویت ما این است که خود دولت دست به ترمیم بزند و شنیده‌ها حاکی از تغییرات است.
🔹
اگر دولت تصمیم نگیرد آنوقت مجلس از ظرفیت‌های خودش استفاده خواهد کرد./خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/695635" target="_blank">📅 22:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695634">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
خبرنگار الجزیره در تهران: به نظر می‌رسد که همه طرف‌ها در حالت آماده‌باش کامل هستند و منتظر هرگونه تحول نظامی هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/695634" target="_blank">📅 22:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695632">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekvjWU8jAzwIBS4ezZNtS1DXLwEZ_v-3JJsw7PMCnhXgIT1Tw-YiKFXt7kK6UIGO1d1I8IJqkUd1qYwkql2MuPo_npIATjpvxOUq47gbLDrdFJZ0qqRDJfgqw9SpPxSAHbHVLkZ34p7ddrYox3hTv5BSlS7tWTdJD26B2xNNOF7H2Dkf_mzHKV_WJk4q0FTRhzICuxOuAi8u3HoXjq6vG9MYbYz_uHCKmkJQrMxV13ScqMnuOhcxoYfYQwkViMzrYQNL1NxjQrpzz4pRZYFH58U-hWfMn7mGi3TlP-sccZv-71XbAud5zP4exeNx5NlQvgZlpe2-mS2de9p8XcYocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای و سیاسی یمنی: یک توطئه شوم در جریان است
!
🔹
پهپادهای «لوکاس» ساخت آمریکا به مناطق تحت کنترل عربستان در الجوف منتقل شده‌اند تا در طرحی تحت نظارت تیم سلطنتی عربستان، به سمت مکه و مناطق اطراف مسجدالحرام حمله کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/695632" target="_blank">📅 22:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695631">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حقوق کارکنان متناسب با تورم ۸۰ درصدی نیست/ در متمم بودجه امسال حتما باید افزایش حقوق دوباره لحاظ شود
پیمان فلسفی نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
کف حقوق کارکنان دولت پایین است و باید مناسب با تورم سالیانه باشد؛ در حال حاضر تورم به ۸۰ و ۹۰ درصد رسیده است.
🔹
ما پیشنهاد دادیم و رییس مجلس نیز مورد تاکید قرار داد که امسال دو بار افزایش حقوق خواهیم داد و در متمم بودجه امسال حتما باید این کار انجام شود.
🔹
قانونی را پیشنهاد دادیم و برای اقتصاد مقاومتی آماده کردیم که عدد نرخ و ارز، رشد قیمت ارز را ثابت در نظر بگیرد.
🔹
تنها کشوری هستیم (شاید بشود گفت یک یا دو کشور دیگر مشابه ما هستند) که شناور مدیریت شده قیمت ارز پیش می‌رود. در کشورهای دیگر نرخ ارز ثابت است یا افزایش بسیار جزیی دارد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/695631" target="_blank">📅 22:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695630">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkfMfVPruZ9QlpmASmZExmzKumgiZgYRRTLbbEQERif0UuKGEMb7hZdu_iSv2z0Ejp8Y7nJR-hqrhpsWsEYT_NUktfG2i3pCapza26_IhEldSYEfD458yDJ8kyeXTrcDAxXhp4gcHsulCIEkiKjZYwALcFzUd1I2zeWyKQU9y9J1f1vxWERVUaQ9jy7ojFUmQPFWPUUGKCkjH1mdZNpJQWtkAiLUTV71SYBpGaoRLUzyn16U5M8Ygh40ykvUVu2lOA5jdgMK0bhxd1kH76qPldzIGF3AlWAoo7KYNVsTAqfZPWFOSVR7Lu1C7cBKu6kV9YW5OJekL6GmyUsGFiYyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: عربستان پروژه ورزشگاه ۲.۵ میلیارد دلاری نئوم برای جام جهانی ۲۰۳۴ را متوقف کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/695630" target="_blank">📅 21:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695629">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-yiIfmy20qWCzJXRJt8cgWGErekFzl1dAJKEmOqaDyFJ2GGSP2Pj2hosXFVNS_ZfsTXg5iim6LZ7-VwkNmx8bMoolrEqbbHAzN-zGPQwZRiGOZG576IVuy0SGL7JGBbbCgkMiCKMfgKlUHZ4l6AVzRfTJJ8nRQXJ4hY1uHiXn18KSRQQKnYT3eMqZvLPjwMUo25k5hYEyADrDRuDMUaz2e8Yakm0qQcyy0SZhc1VSmaSzv5kWURR_vqV7M45hcEvTKhHX6jFU-NO4_cWl1fQbSUlqyYeO-HQNC4qQD9bnR4ATzGkhQizKb908_6VQGvzNdGfb_QGV8iSLP_PbESCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر نفت استعفا داد   معاون دفتر پزشکیان:
🔹
با پذیرش استعفای محسن پاک نژاد طی حکمی از سوی دکتر پزشکیان رئیس جمهور، حمید بورد به عنوان سرپرست وزارت نفت منصوب شد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/695629" target="_blank">📅 21:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695628">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMMkYlZrRYVBgGL9ZBAyymfqUBoVDgSiIqaj6cU4Pdjy9w6D57d67iYFN_gD-psEBVz55t0dlEa050Y3HKcJrFP_CBjb7-OVEAa5RJ_3Zqyic94Mhky2qQZHgBsbQhZSOV2LVS878ePxH0diA_cNR7ZES45mAhl5x2vmE4CKCf9zJtUBJ5K4_HANCpSWModNNLQJqZg1hz2fpjsCZFv44HM9-WjfqOK1Cf-wo6F6-tepHJ2PPcMVunGN4L0C_oUmteXI_jFTyiy50HHnFu_7shdn_dR7E2o6IEiczhYdf3YBj7yodQ4h3m7g5kAdFRF8jPx7IjI_7BEwo-bUGP3pZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصغر فرهادی، کارگردان سینما: اصلا چه کسی از آمریکایی‌ها خواسته بیان مارو نجات بدن؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/695628" target="_blank">📅 21:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695627">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c040077d42.mp4?token=Op-u5AHhx9GYoHZQjD2vu73YLUUo_2AKosd51mDZ-XafdmRygDpYrlNuKvO7V0ZPOiqeTdyHK6x6OVF3onmpzuEec7Zv2ZMaS5bRj_sjmkfRU9Jehiyuh23VXicbFBNVZpHPx1fAEioKE7luCujxUuzX2n-cqTy33QU8J8D9egaXRR1r5fuwV7LZG_QAf4CnEBhWbRtPFSG5m5-pROI5Kxd7C1l7D7Olu2GY5E16a4bFKLgQdYzx_w5IuttUd-x13Y0hCN1lUMbDUOE8iYS2Djeqi3uT3vWcOtIplYJk-fGGBuZOw0ZDYHoGYWkEAVmSkjWRw6LQjA1EUZdEKru3wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c040077d42.mp4?token=Op-u5AHhx9GYoHZQjD2vu73YLUUo_2AKosd51mDZ-XafdmRygDpYrlNuKvO7V0ZPOiqeTdyHK6x6OVF3onmpzuEec7Zv2ZMaS5bRj_sjmkfRU9Jehiyuh23VXicbFBNVZpHPx1fAEioKE7luCujxUuzX2n-cqTy33QU8J8D9egaXRR1r5fuwV7LZG_QAf4CnEBhWbRtPFSG5m5-pROI5Kxd7C1l7D7Olu2GY5E16a4bFKLgQdYzx_w5IuttUd-x13Y0hCN1lUMbDUOE8iYS2Djeqi3uT3vWcOtIplYJk-fGGBuZOw0ZDYHoGYWkEAVmSkjWRw6LQjA1EUZdEKru3wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
والله واگذاری زمین به مردم هیچ هزینه‌ای برای دولت ندارد!
عبدالجلال ایری، سخنگوی کمیسیون عمران مجلس:
🔹
اگر زمین به جوانان واگذار می‌شد، دست‌کم ۵۰ درصد هزینه مسکن جبران می‌شد؛ این زمین‌ها متعلق به خود مردم و بیت‌المال است و دولت نباید روی آن‌ها چنبره بزند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/695627" target="_blank">📅 21:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695626">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
دقایقی پیش صدای انفجار در جزیره قشم از سمت دریا شنیده شد؛ اصابتی در سطح جزیره گزارش نشده است/ ایرنا  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/695626" target="_blank">📅 21:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695624">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشبکه اقتصاد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NS5c3z7BefcO5xkepwjuO7VrNsVYrMH8wRi2NIOCkIr1K711Buplx1aQY-36Dku6_ciPWsYo_cWeP6a_bgo4UpwfkJVffptQuoLD6NjM1FZ4WYpdA_EeP9r4XC4Lu2I2XUpNTrRBmlg6IZG4wtY8zmnwq29IuncYsYejeS7Fspz5ZSY2dWTgKQ75NHoNZS81hleWviKoayDIHWSorvOcoYVKXy2fGeEdA2rWkbzVargMFptKFsOVNh_6tPFgDDhV2GYifGuSbb0RWI1VDM061oYuv4eCKZC-C3jJlDbjm5qR8-Tz89rs4A4sT7IkvUdxaYoi6WqGYAD_6P27lP6iEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش فعال رسانه‌ای به تقسیم کار علیه دولت
🔹
داوود حشمتی، فعال رسانه‌ای و روزنامه‌نگار در شبکه‌ای ایکس نوشت:
دلار بالا میره و تقسیم کار شده
‏عده ای میگن: چرا دولت کشور را رها کرده؟
‏دولت شروع به فروش ارز میکند
‏دسته دیگر واردشده بامغزهای ⁧
#کوچک_زنگزده
⁩ میگن: چرا دولت ارز میفروشند. مردم ندارند ۱۰ هزار دلار بخرند
‏نه عزیز. درد شما درد مردم نیست. درد سرمایه داران است که میترسند قیمت دلار کم بشه.
#شبکه_اقتصاد
@economynetwork</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/695624" target="_blank">📅 21:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695623">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/albRsflM8ffhKog-CIYx2NICGjWiIQ7PMmimKh4aV_fmXGZ9Eu1S9oktQRTkaQnpNwObt9d3Fv4et205Kdl4MMCjbVrA_xYHrtFTRj8KlPi5dhvlBaz-ioBt1EDZByEORhwN5zvQlf-r_taZUsTxfc7njwI8VKAmkR-0cyicWbCH4hXls9ATVqFR8D83bpZrsU4XpCyUzalg54oxgZuwf_FZv9dc_i6Q3qK3MNS7HsYToP-RIClskOPzJrus4LPxRN8HSP2GMzGXfTuRmTvNLtXcNMWtdxJzd70u85ZZCAD0wvsFs3pGH6QvK6rpfqMAi96v4xwigu1OLW9Df7Vx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ مدعی شد: ما با دانمارک و گرینلند به توافقی رسیده‌ایم که به ما کنترل دائمی بر امنیت و سایر نیازهای گرینلند می‌دهد #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/695623" target="_blank">📅 21:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695622">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9500e3685b.mp4?token=dUO2V38y2P5PaZqvMIRVM8e_xBN3RORNoUCgsZ-KQ7ayn2-zwRS9UNicLDerqEZZjrUW2ANzIjWqohSyUgpCTrlLjbLwMMmme0uYBjX7qxtYDtd2h1MRvZSKvyrcWHCCMAyV2Ou0qZNb3TJD3P6cfoYekitJeqET6tB1o7EFF2h98ZnBKmfZPdYPLn_PyxQFoY2oQU4AEcIB1CFl4gc9Yg8iFXKB32T7znNAAdUYOr9uUqh3rK2iA8lQosQZd1Pkzp2Tuqn_kNmP8XcHoc0PCFF2VeiCJXuufN3RIIXWCIV5t2ZYShbjhVGedjWx0p2isYyx5idEeXsIutqHcUZvOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9500e3685b.mp4?token=dUO2V38y2P5PaZqvMIRVM8e_xBN3RORNoUCgsZ-KQ7ayn2-zwRS9UNicLDerqEZZjrUW2ANzIjWqohSyUgpCTrlLjbLwMMmme0uYBjX7qxtYDtd2h1MRvZSKvyrcWHCCMAyV2Ou0qZNb3TJD3P6cfoYekitJeqET6tB1o7EFF2h98ZnBKmfZPdYPLn_PyxQFoY2oQU4AEcIB1CFl4gc9Yg8iFXKB32T7znNAAdUYOr9uUqh3rK2iA8lQosQZd1Pkzp2Tuqn_kNmP8XcHoc0PCFF2VeiCJXuufN3RIIXWCIV5t2ZYShbjhVGedjWx0p2isYyx5idEeXsIutqHcUZvOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن روحانی: اصلاً من نه کلمه رفراندوم را گفتم و نه کلمه همه‌پرسی را
🔹
بحث من، لزوم برخورداری «اهداف ملی» از پشتوانه مردم بوده است، نه برگزاری همه‌پرسی درباره دفاع در برابر تجاوز
🔹
اینکه جزو بدیهیات است که وقتی به ما تجاوز بشود، باید دفاع کنیم
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/695622" target="_blank">📅 21:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695620">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5a0e649e7.mp4?token=ptIK56czXZPzRE2D4UyP-RltbWzFjxDMoQ_mnkgsdd9aQqURUjpfIBHb_jAMGOrGn48DO_ggU0QwDsSCEdFv7SOJDCxXm6qE0FrZ6W7R8l28gVGzwuBb2yZeIqKNcUu0JyWr2My9z2xtwn7LF1lJPJF2x41ApVwJmp4oKHYX4nuxmescH-ooPy8WeE_Einl4BM6_qP_VD0MaWP9m9dq_PsnCA2IyWjsFkJ7vB70WPxHpbE2ArdrF-MdYQBFYixtXMyvBH_GMmn2H-g7TLmIjmDmuoLqypG6ilu-2CspEejAcWB3XGeo4nBZQlFaF-aHetstl-KwOvmgL7SrhF0T9h2KYZH0UApi2KvX_rhNT6U_BmCmjjEa5ZuFLfgMoo_2CEaYY55plQpBafoHewMRMKfTrpInCSKM_7I60I05LbPDRPYxMcnoDa0pu0L0dicoNlXcyECDtkfsNrmjbaROGflZLeACrxWtnwlObxSz3YP-F76GVzwpMAdUH9GRfAJ6akvSthbm1kkR3zkirMs2t9RXu2xXgQj2NZLCJ5kFs_-A4zVysWJpSEIQfP7EvM01eS_2ERt6P4F781bnWFPfTiSdq9FvTk-Au5TZjg2K51DMHToSlCCSRynyjAzVuN-QO8l-hx_8GNTNom_3w_StKLOreyvc7SE6ZSQLxgWQpKtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5a0e649e7.mp4?token=ptIK56czXZPzRE2D4UyP-RltbWzFjxDMoQ_mnkgsdd9aQqURUjpfIBHb_jAMGOrGn48DO_ggU0QwDsSCEdFv7SOJDCxXm6qE0FrZ6W7R8l28gVGzwuBb2yZeIqKNcUu0JyWr2My9z2xtwn7LF1lJPJF2x41ApVwJmp4oKHYX4nuxmescH-ooPy8WeE_Einl4BM6_qP_VD0MaWP9m9dq_PsnCA2IyWjsFkJ7vB70WPxHpbE2ArdrF-MdYQBFYixtXMyvBH_GMmn2H-g7TLmIjmDmuoLqypG6ilu-2CspEejAcWB3XGeo4nBZQlFaF-aHetstl-KwOvmgL7SrhF0T9h2KYZH0UApi2KvX_rhNT6U_BmCmjjEa5ZuFLfgMoo_2CEaYY55plQpBafoHewMRMKfTrpInCSKM_7I60I05LbPDRPYxMcnoDa0pu0L0dicoNlXcyECDtkfsNrmjbaROGflZLeACrxWtnwlObxSz3YP-F76GVzwpMAdUH9GRfAJ6akvSthbm1kkR3zkirMs2t9RXu2xXgQj2NZLCJ5kFs_-A4zVysWJpSEIQfP7EvM01eS_2ERt6P4F781bnWFPfTiSdq9FvTk-Au5TZjg2K51DMHToSlCCSRynyjAzVuN-QO8l-hx_8GNTNom_3w_StKLOreyvc7SE6ZSQLxgWQpKtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلف خرها، برنج روی مزرعه را هنوز برداشت نشده به ثمن بخس خریدند و با قیمتی چندبرابر می‌فروشند
پیمان فلسفی، نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
برای برنج سال گذشته پیشنهاد دادم که شما ۱۰۰ یا ۲۰۰ هزار تن از برنج تولیدی کشاورزها را وارد چرخه تعاونی‌ها کنید، دست واسطه‌ها قطع می شوند.
🔹
آنقدر تعلل کردند که سلف خرها و فرصت طلبان برنج را به صورت شلتوک خریداری کردند.
🔹
برنج روی مزرعه هنوز برداشت نشده به ثمن بخس از طریق دلالها و واسطه های بزرگ از کشاورز خریداری می‌شود که به واسطه همین عملکردشان قیمت محصولات کشاورزی را روزبه روز بالا می‌برند.
🔹
عملا سود نصیب کشاورز نشد، این‌ها در انبار و سیلوهای آقایان ذخیره می‌شود و در زمان مشخصی که خودشان تشخیص می‌دهند با قیمتی چندبرابر به فروش می‌رسانند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/695620" target="_blank">📅 21:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
قتل همکلاسی بعد از زنگ آخر مدرسه!
🔹
اختلاف دو نوجوان در سال ۱۴۰۲ پس از تعطیلی مدرسه به درگیری با چاقو در پارکی نزدیک مدرسه منجر شد؛ یکی از آنها مدعی است همکلاسی‌اش او را به پارک کشانده و از پشت به او حمله کرده است.
🔹
متهم اصل ضربات چاقو را پذیرفت اما قصد قتل را رد کرد و گفت هدفش «زهرچشم گرفتن» بوده است؛ قضات دادگاه کیفری یک استان تهران پس از بررسی اظهارات طرفین برای صدور رأی وارد شور شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/695619" target="_blank">📅 21:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMav04ojeisu4a-tzff1agy_oT5qdtYRjIKSQnrfJtouqf4CbvkAiiMOg-6Ytng_LcBAaXGLxN2ET-YjYVaJOHAk33LU5rZJtCaXLFuj6qbC91RSWTDsG7cZdbY4kMC6L5k1FQovd5sS-6EIWXw7UhvlcEqNE7p9LGSyydvLjx4nLD7HRRy4Hj-oIO-HSdTaq5h5vgiP43rI7rS4kPQK7gzF_Z6V8a-zBh__2u0kWmbwYYKpeR9us-6uUYMMR5g3kzAw4ndwrL8OTJdeU69Xl_9t6R6Q1Goa0hEx7XfVElsm5nOZb-e65SBRpPFEiKRipXNV5dbEYnepTlNoBvNMxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استیو هانکه، اقتصاددان برجسته دانشگاه جان‌هاپکینز: حالا در این جنگی که خودمان انتخاب کردیم و علیه ایران به راه انداختیم، کجا هستیم؟
🔹
ما داریم بدجوری شکست می‌خوریم؛ تنگه هرمز پیش از جنگ باز بود و مشکلی وجود نداشت. حالا با یک مشکل جدی مواجه هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/695618" target="_blank">📅 21:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Pk3Zwj-WJp0btG2dxlgUDn5-OxChZp6-HTvbOXEGlbiX5spddpb5wf0D49Jpk36e1BrBRNbMzN4ngC7SDf9B9m46E8zVuecIL8H7hWxcFYocnAYfWvNOfZaEJFV1cDMLZ5uhF47cPr9u_YRbzhSnuB67gz3_uB7OWnM1wnPF0TcD6GqAJwmobmu9gmbbTpeq19FkHRJi8rKf5pIoG_flaPcQq2A11kwGzQNRcZSkCJt1GwQof9iEiUa_CLQe30ZyHnxJi9YGe_TQLf-Yi4CAmEHGzpNZqXkbTLslK6TKVWya2t3lzoq_Hzjx-g1kIkb-w8ZPRSYk-9FVvUIYv9HVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن پاک‌نژاد از وزارت نفت به تراستی‌ها ربط دارد نه شریعتمداری و هلدینگ خلیج فارس
از ظهر یک شنبه ۱۲ مهر خبرنگاران، از رفتن پاک‌نژاد از وزارت نفت خبر می‌دهند، داوود حشمتی، روزنامه‌نگار در این باره نوشت:
در مورد پاکنژاد و خداحافظی او از وزارت نفت گول نخورید.
واقعیت این است که موضوع ارتباطی با شریعتمداری و هلدینگ خلیج فارس ندارد.
او باید در مورد تراستی ها و فروش نفت پاسخگو باشد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/695617" target="_blank">📅 21:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پاسخ متین رئیس مجلس به عضو کمیسیون اجتماعی
🔹
احمد بیگدلی، نماینده مردم زنجان در مجلس شورای اسلامی، در تذکری شفاهی با استناد به آئین نامه داخلی مجلس اظهار کرد: بر اساس ماده ۲۱۲ آیین نامه داخلی مجلس می‌گوید بعد از اینکه استیضاح وزیری در کمیسیون بررسی می‌شود، در اولین جلسه صحن علنی باید مطرح شود.
🔹
این عضو کمیسیون اجتماعی مجلس شورای اسلامی خطاب به رئیس مجلس گفت: همه منتظر هستند ببینند هیئت‌رئیسه مجلس در مورد ارجاع استیضاح وزیر تعاون که از الزامات این مملکت است، چه تصمیمی می‌گیرد. الان کارگر کمرش شکسته، بازنشسته حیران است که چه کار کند، جامعه بهزیستی پناهی جز خدا ندارد و نمی‌داند چه کار کند. آقایان در وزارت تعاون منفعل هستند.
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در پاسخ به این تذکر گفت: در جلسه امروز هیئت رئیسه مجلس، حداقل ۳۰ تا ۳۵ دقیقه به طور خاص درباره این موضوع بحث شد. ان‌شاءالله تصمیم‌گیری انجام می‌شود تا کار پیش برود.
🔹
این پاسخ کوتاه و متین رئیس مجلس به این نماینده که طی دو ماه اخیر بر استیضاح وزیر کار پافشاری کرده و فضای مجازی متاثر از التهاب‌آفرینی‌های در خصوص سرنوشت وزارت کار باعث تشویش جامعه کارگران و بازنشستگان شده، به خوبی تفاوت یک سیاستمدار با نگاه منافع ملی در مقایسه با سیاستمداری که در قید و بند امتیازات محدود شخصی هست نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/695616" target="_blank">📅 21:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695615">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msJirlqKKFj6gvfX3_sYoS-uEnwAy8sF2jJ7CTAd-Ljer4PRDvlcI_Go1DMIvVM0Dh_OcfVstsURIX5YpsQTjYmOZzS2uvyXoz1QqZKD6sE10z7wsysSkknY3XmFrQpJPK69DOT4OMXD2GA8k_YFTrOBsDM9peuswDgJpFZFBZprQB_QrntBxueqVkuY6k_yK2ffVMKtqR9EDRuFsZ9YCXUPwAxgfxh6veD8O0v07AAGpp1q6XwS5fZebariRRTjQ6Sz5WFHvff65aopBnwXGnhljeI_cQt2VQIN4d-05YHLMWErMxeMQSsz8OxGTpi489sNhWjjMxhzvuxcVKYlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر می خواهید نوشابه گرم را به سرعت خنک کنید بهتر است دستمال کاغذی خیس دور آن بپیچید و داخل فریزر بگذارید تا در عرض ۱۰ دقیقه نوشابه کاملا یخ تحویل بگیرید
🥤
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/695615" target="_blank">📅 21:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpCGBORapElmmCKbtHOm-URnoZb7db123TxpX2z4U8Gcmz7lDdcX4ZXNjnvHzMaCwNaqh1OkTmTJr1mOWmvVQtqU3kQ5Qy7SpaXupwDvtHa1VB8ZwxSHVhUHyAI5wvzKUkzMsIQ824aDAUvbQHqdOcLZbxdzOFdL5vCLwrlBqjS2H1S1pPaMZrUf1XI1roW07GsqHJT4FCwUXJ8pziF8Ir_Og-Noqg52ZhDU6-pky0UBQ-ahbJFeVk8P7PQXWOsIVJjGDKeXaL4dpY0u5BLNpzOBwSwBAUn6g58_KAYK_gtK4Tb7ufWnN01TLZaneqtfMWLpMHFRjDS1kQoohINNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات حمله به چهار نفت‌کش‌ در ۴۸ ساعت گذشته
🔹
سازمان تجارت دریایی بریتانیا از حمله به چند نفت‌کش در تنگه هرمز طی روزهای اخیر خبر داده؛ در یکی از حملات، نفت‌کش دچار آتش‌سوزی و خاموشی شد و خدمه سالم ماندند.
🔹
نفت‌کش دیگری که ۳ اکتبر مورد حمله قرار گرفت، برای مدتی کوتاه دچار رانش شد و سپس با کمک یدک‌کش به سمت فجیره در امارات حرکت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/695614" target="_blank">📅 21:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695613">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtaygHvmkWV28fBlwzOQtgO0r6lFXiX-Cf_x7YYHxjurmQrU2MGdkGZqUsRphlnY86DZ9DnMhRKmrcbap3M34K8rXGj1H2--Y-WmqbMT7i5fHalZM1rQZyOw9G5CXZIB9XFMTnNSXx7BNM8NQ9DG_8tIhz2B2_LOByrcjJ78_KTvKIeLU2CejSdYvsQMezGFT-hhbMoRYRIrdxnrzNRAe1nFpUbUcvxbedW0UgQVQL6pK6DxvUjdwVJemXHh4oq4vZOQQIL5dml0TUCtb2a3fgPSpnvZcnJMr35ztwlTebwlwhITzE_qmm7LU3IDm4NLPP-dZkC3FDItBzs64w24YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای نجومی
🔹
تیم ملی المپیاد نجوم و اختر فیزیک جمهوری اسلامی ایران در نوزدهمین دوره المپیاد جهانی نجوم و اختر فیزیک (IOAA ۲۰۲۶) که از ۳ تا ۱۳ مهر ۱۴۰۵ در شهر هانوی ویتنام برگزار شد، موفق به کسب ۵ مدال طلا شد و برای سومین سال پیاپی قهرمانی جهان را از آن خود کرد. تیم ملی المپیاد نجوم در هنگام قهرمانی، یاد و خاطره دانش آموزان میناب را با نماد کوله پشتی زنده نگه داشتند
🔹
هشتصدوهفتادوهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/695613" target="_blank">📅 21:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695612">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
آکسیوس: محمد بن سلمان روز چهارشنبه دوباره با پیت هگست تماس گرفت و از ایالات متحده درخواست کمک در جنگ علیه حوثی‌ها کرد، اما درخواستش رد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/695612" target="_blank">📅 21:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
دقایقی پیش صدای انفجار در جزیره قشم از سمت دریا شنیده شد؛ اصابتی در سطح جزیره گزارش نشده است/ ایرنا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/695611" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695610">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1829c3d8a9.mp4?token=hcMBsZw67j_EAWq7N7ThPRgAKJB2mWLUcXoGlQxDAqOvbTg4cZU3yCM6TVsoMl5nY1H2eUKBxlM4A3CGujp8Q601bbhfLqfx3CBMxkoiJozzTvupa8ahltDjfik_NRz_lZeYur5_IHBrjKI05k-vocJzBfb6klK27rABB0tSL-uDukkEU7ODHEYjVLjYFilV-F8nwdJV56Y4JzRTsYd6J60ZDdE2xa_kgUhmrUV7ZjVpV-2O2v5AZd9TxPrDn_pfgvOY3NUjhilQGtdq53SPGxGEhxdgpfX_TBgNYYgYD2LSXK2CZFGk7idaIJkzrRQjS9otfQbh2acNKZgYASISGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1829c3d8a9.mp4?token=hcMBsZw67j_EAWq7N7ThPRgAKJB2mWLUcXoGlQxDAqOvbTg4cZU3yCM6TVsoMl5nY1H2eUKBxlM4A3CGujp8Q601bbhfLqfx3CBMxkoiJozzTvupa8ahltDjfik_NRz_lZeYur5_IHBrjKI05k-vocJzBfb6klK27rABB0tSL-uDukkEU7ODHEYjVLjYFilV-F8nwdJV56Y4JzRTsYd6J60ZDdE2xa_kgUhmrUV7ZjVpV-2O2v5AZd9TxPrDn_pfgvOY3NUjhilQGtdq53SPGxGEhxdgpfX_TBgNYYgYD2LSXK2CZFGk7idaIJkzrRQjS9otfQbh2acNKZgYASISGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروهای یمنی: شهر تربه به فضل خدا آزاد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/695610" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695609">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29fa97a69a.mp4?token=YzZ0ReTSnYq7K3eftWSuFYk74TrBWIn08ZWb-bIOWoCN3q31YpCEb6b-bnQvZPJJI9ozQY-wtKN4F9uTAbYV5eavX3s9JGtsvEKKY7QlSXrifErsnsVkdB2NmLQqfiO3SmG01OOkexzRPmc_itHWeiX9-i3ZMDWHNzsnkedKA28h0RiV9MwtHuQsxPzzoCBxM0LeQfY_-ST6ch-mazbecRI_OPcfuitgOOCwfIxhYGP36wPw61TumtEVzA6DRDwZ60ky3wRMynRe9QClmKoLgSw9W3DnqhEMM5TAPmz1r_2929tjY-99MQMr9QNK22RRNNIrhJTgW8MQKpnr0FLuIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29fa97a69a.mp4?token=YzZ0ReTSnYq7K3eftWSuFYk74TrBWIn08ZWb-bIOWoCN3q31YpCEb6b-bnQvZPJJI9ozQY-wtKN4F9uTAbYV5eavX3s9JGtsvEKKY7QlSXrifErsnsVkdB2NmLQqfiO3SmG01OOkexzRPmc_itHWeiX9-i3ZMDWHNzsnkedKA28h0RiV9MwtHuQsxPzzoCBxM0LeQfY_-ST6ch-mazbecRI_OPcfuitgOOCwfIxhYGP36wPw61TumtEVzA6DRDwZ60ky3wRMynRe9QClmKoLgSw9W3DnqhEMM5TAPmz1r_2929tjY-99MQMr9QNK22RRNNIrhJTgW8MQKpnr0FLuIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: به کسانی که برای پرداخت هزینه بنزین، غذا و سوخت دیزل به سختی می‌افتند، چه می‌گویید؟
🔹
ترامپ: شما بازنده‌ها هستید. این بهترین اتفاقی است که می‌توانست بیفتد. اگر در این اقتصاد به مشکل برخورده‌اید، یعنی بازنده هستید.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/695609" target="_blank">📅 21:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THNBmgN9EjC3sagQVBKnvBDAgKE1ZcamZuGv66U095oh-ml1jJlDqTBnKfGLsXSRVTlF4BguJu8vI6qrZocGobL4dBsjryu9iITE8rLYwY6v4as4g8-gMksLcOuLan4r9gaf1BmUBSU8MT7sryLkss4zdi3PXA-vHv5w6NRQzOo32NB5-liiIR3WwxwXuZn1npe3fYk5ROc755-lMSAYyHG3YPN83ApRZh7RzvRFQSsdctgQQZJDbFIxTmsVx9PTivOmiP3DbpEva1NNFapmxH1w4dx3Xy1kzBsS0OzUWiqllswwhVaI-iEOiPQDBfWzqyq77-w9AKhc-JTONeskaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJ89SkcWYAH9NCgQXeZkuZEwSVcTwx45ihuhjX-KV8bkJ-iSRksVcA9Vb6obkDn6-5VvznILGkDELvPswkoiTimeJgV5VrATxmof_yqfGWGjkgVEc3eIh07uRVsZs6ndEigIh4yPdOx_JNPPtpgEcctB_In-uWaHpZLhmhE-b5sSC1R2TWCSbevWNuHGlbVkL0cJHup_mxks8QEluy3kub0W2BIjXET-m17mDrET3GRTCPAGB_2neYAHB-PLb9TMArchq8-ieyHgy2PnfjZZfG5ES1xFMeNjp2q-3EfVtdnpxZFKRbhTu7RSe6Z_68XSoCqSqFi4FxBtGKLA1E5j5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aUQFJPxLEfEV9ijywbpH9raMH-09oH8QQ-hdJ_XI7J4095h7BgP_7TN6WLpFC8OJJWKQPb9yoVPeZC6MlqtIAHHrJj3co3_lI_yn2h6VpRSBVsHre7P2RYQmcr9H_YiAL9Qeba4AVesYsv3VbQAaZxNkjfgIGttWSsQasgl_34lAUIsd6snlK03S2c5wWvI2oLD4IGNlye7UKioNbhUQu1Q7tygLG0psSHBzzt7CcPWNdM1OkTewNtcH_wl-0bM6xwt9SSXkMFWdA7i0hBZhbl3-wIYN3y5Qc3qvJRO_Gnn8c6QXA17dj9Hq1PDfu4gwa4MhUG6NGpCdzQMoo_Z7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tx9pIAYEZQgZhYJc6K_Yd-2ZwKjnxWcpyoUu2fHXq34CeU-NxfZqDJCAijRH7A8DcDyDZeBDk0La2iaza8UOcFseGKXSI43oCU_rV3kSqkNuJessqQHLYztIKqlMFVmVjUJ64YkcmCRgpx3a0tNKIfSrfgNknq90c-9W34wdhSNFLG9bkqLetiB1REFJilUdlYTkXE9jHuSvIEi7fzj2cj_QbCNuhFpDadjjtvTqy-FWLBthW_vA31pTu7J49e3kHGj2vsYATWxsazIZn2cK_YpHyOjEKCHXzVYgbRmB218XxEJX8Njm-cQ7-wbTm02Qm59o3Ci7s6Wd14l4Rv3Pmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/foLQWX1Qoo41W6MzTLBZBOapDPW7AxCbcyjGIs7GKo3KvS2ruXAvxMqtT_AVJVicvO9zWi33uminWO50c-3KXxTQCP4EcgtoFisijNY3GhfYbuesGq0ZLppotSMpmt6ZL1ZEtIBxqsPVzAj5l_nCeR1miC1obV7_v0MZnmkQUUqZ4IDvkT90G2Kmzof8w8cfqoTrhAttHTwqrYC5PLYsosHb86G_YbebYKVd3Bb0Lq1U2tjIhzieRpfZltFrYvZ18T5xVHNR449EcjJRpOMIKVY70uCEiYtBLBOm8MgSYBtsw6MMBN9tLe69s8H9Wv6IypTDtsyqiXm2zfcH-cnZVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کمیاب‌ترین گل‌های جهان که قیمت میلیاردی دارند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/695603" target="_blank">📅 20:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695602">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeNSfFoSO2YkaLKIWRP5ypQjC0nEy2PgIEEm2msv5YoFrZYxRVxe0-F4q96Wzk0SxVkjOTjysYdoI-RTbOCpX0CJMd9bQK6chPXYk1NT0fcXN3T1e6r3GRVQWNYWTjh-MwGlKAVXaytl-OUzOS6_xGNB5dYsxDSa_jZQtIONVL6D6QWVypGVlVjPDzlyrmSaSWOc4raiTNzMFDsbKs_zFPVm7TyiXdt8i_I2Y-xY1nnW_ZqdaNbpgzPa9HndjEfgmlxuLmk8UpXTL0vtNpo4PVGIxhgemhveaFNMMMPOim3dj5fmySqrp4yvVstpw9jpeec7K_tERbr8jB8ISldI5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد هاشمی، رئیس اسبق سازمان صداوسیما: یک روز گوگوش با چادر مشکی به دفتر ما آمد که پولش را بگیرد. خیلی خوشحال شد وقتی چک را گرفت. همانجا گفت: «من برای آقا [خمینی] یک ترانه خواندم، می‌خواهید برایتان بخوانم؟» که ما از ایشان تشکر کردیم و اجازه خواندن ندادیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/695602" target="_blank">📅 20:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRO9CXSKvABlFZ_iCTaLWlUgiZb1ZxlhgotKjIrEKrJCD990drE6wlI6C9jz9IG_8IGD0Wf_Z-Wf-ptMBUOPjCWj1ItbVp8kG1ciwGzGxQk92__r63NQlHFNb1gAwgiZeCCkFyQS8M-_CsEk-5nsl5zkrXC19j_WpJlNKaXn8qJbRK5ljS7rpAQehLqo-qN9H0gIdzVoGIJuOoSNUR2a2v9gYy6MbtKmOaDFO4oMrn9mBCxagXZQnaEEs7ZTNFsRE6lIK-mdpHtreACPrxCQ1msv06u4SSoBDu3Aka--XEQ_FzSxgdpWvHv0blNx01_3xO5S7_RcBSIz9_YBkSZAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای عجیب ترامپ: رهبر کرهٔ شمالی به من علاقه دارد و ایرادی ندارد که سلاح هسته‌ای داشته باشند!/ رئیس‌جمهور کرهٔ شمالی به من احترام می‌گذارد، پس می‌تواند سلاح هسته‌ای داشته باشد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/695601" target="_blank">📅 20:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu9PDfj20hAojRLOqgt97kqXUzdo7LnFjToSEbRIM-ZqS4Jnkd-UtwjVsfIHd3yCo-slqbMVymtCFSM7txBd8FbzqdEeBl5PHCOusnTSbANWqGycUlAVmBzY6EhR42GVxMU9coL8by_bjApsLpQtZlmCda4cS217OwgJjGuEjO3KCQtNTcC3u1H9xS8KdiK0dMHdZjOuvBmz8O9vH25u_6aJAUufSeWewmG5zjI3EylrW-oQBPB68SzCt418FxXEKKQ-8UggtCidJ0Wgl8JMS28rfl9nhV68BZqBgZ6xV3Kr2LPrahU9tM4AqCTFgniEVdNG8bQvWt2i4CKiUwd71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پترولاین عربستان دوباره تیر غیب خورد
🔹
تصاویر ماهواره‌ای از دود سیاه و ۴ ناهنجاری حرارتی در این تأسیسات خبر می‌دهند؛ جزئیات رسمی حادثه هنوز اعلام نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/695600" target="_blank">📅 20:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وزیر نفت استعفا داد
معاون دفتر پزشکیان:
🔹
با پذیرش استعفای محسن پاک نژاد طی حکمی از سوی دکتر پزشکیان رئیس جمهور، حمید بورد به عنوان سرپرست وزارت نفت منصوب شد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/695599" target="_blank">📅 20:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695598">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b07137eca.mp4?token=BgpA4hDoxUok7L2uNRV25Z1_rBTt46btI6iz2PLTaOUESgYian0cIn6qRSgrMAiwdt5rm1HBZADiy5NX_KCTUqOh2Sdq4QbYUqakNUyBfzdKlFaEewFJU1Nrwc40wv7yxiTxvVk6kMznjZ2g6CQ7IqPmklWaqo9ilvj_o2UHAhLiikZVDwH2jDrbqtPPpw-YPzz9NLbcM9ILlKNY83STkf-Zoa08Opjv9FLCRRrVNp5jg_0EyXCoqAGx1j2URcovPmdn8hFdlDnMpDAXSI2vbVcoquQ8mYaEU2tH8jU-6QVTJOVass_Db0t8Q_xkvG23MToCQacULbj7yNbDNnYWkIlJQIP9wxLnK5KAXjvL3SqgeSn-HiMU_67_EXSFFETa46RHGoC6oWIMkb11Lwj5V84HlZvO4gHPs-y651anFJce8Ki8529lmEUVP4FNBGLIXoxJz-hHdwNKEE2X-8vJIhEQNw65NYPgEBJzMN3qYfWd0Dwhx9mTDc_HfAlFNtqI5KKWSw-8KRbR_ySsL7Gt8aYctUuQj5Yp8S9NvHl8h57nx_Gx3bth83iO19jYtmoRLbkhV7YbbmDCTUxg3srHKtW0p808Rd1p2ozZNePFT2vudLqtbsO5QfKSrcFhWZyayzV4P5tE10UMcWeqhxftk_93LppLhZcKMSNAxsXgSmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b07137eca.mp4?token=BgpA4hDoxUok7L2uNRV25Z1_rBTt46btI6iz2PLTaOUESgYian0cIn6qRSgrMAiwdt5rm1HBZADiy5NX_KCTUqOh2Sdq4QbYUqakNUyBfzdKlFaEewFJU1Nrwc40wv7yxiTxvVk6kMznjZ2g6CQ7IqPmklWaqo9ilvj_o2UHAhLiikZVDwH2jDrbqtPPpw-YPzz9NLbcM9ILlKNY83STkf-Zoa08Opjv9FLCRRrVNp5jg_0EyXCoqAGx1j2URcovPmdn8hFdlDnMpDAXSI2vbVcoquQ8mYaEU2tH8jU-6QVTJOVass_Db0t8Q_xkvG23MToCQacULbj7yNbDNnYWkIlJQIP9wxLnK5KAXjvL3SqgeSn-HiMU_67_EXSFFETa46RHGoC6oWIMkb11Lwj5V84HlZvO4gHPs-y651anFJce8Ki8529lmEUVP4FNBGLIXoxJz-hHdwNKEE2X-8vJIhEQNw65NYPgEBJzMN3qYfWd0Dwhx9mTDc_HfAlFNtqI5KKWSw-8KRbR_ySsL7Gt8aYctUuQj5Yp8S9NvHl8h57nx_Gx3bth83iO19jYtmoRLbkhV7YbbmDCTUxg3srHKtW0p808Rd1p2ozZNePFT2vudLqtbsO5QfKSrcFhWZyayzV4P5tE10UMcWeqhxftk_93LppLhZcKMSNAxsXgSmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس صداوسیما: در صورت حمله اتمی به تهران، سه‌میلیون نفر کشته خواهند شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/695598" target="_blank">📅 20:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695595">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEva7vPAaB2DUPxoi4-5TnxMUikjdy958z64w51AbQG8RX-zQ1tNaAEUsUrQ9osHqkrJ1KDwvILmHdYdlPwizSRJ7iwRKz0VawV03fjZC1aJUb3egdPN6UALcJYjtnUogwDVOu4VZ6MM8E1CMfejDy76siZxSbOFBEln0vlFCdoIXfeAsi5VcEQd_xmDkcKqe4WYJ8u1RsDBe_pVw66JA_neJxdz6q-NEbjAf8S2mCT-zmzGArKZyq0Cq45vgpOLAJ0qBxb3hhzBRtT64TtYDmwPr8GmdV3ookKoJsFgCzbCqT-WSNe6-FJjYurum5JqNYAvx99uytLFbRaixa0LzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d738f2c41.mp4?token=L8SSQOyXWPT1ZtQRX5ZY85UBD_JwFE_FrRLajw91YG3MUU1-DJmGIVQ59WEizlVDO5198c5dqAoaWpA0LVUsDC4J1dBduWPdKvf_po4oUANTzf-7epbRJBhIZ5i9UEYKMI9Ns1D_YvMFBoDaeWXnVtO5vtir7O29ge9ACkSr5LKfLFMxgwutbYfArj8mC9umT5hH9HMEkG4LndmvJoNCoVtsEM0xq3xFVJgxpm9OGlX9jseJULvQ4vxk8KSOPo2Zv6EaWwNwee1tRFalkMzva4U7YJ4TIUgdUNeOQOcseZ9Hx489LxMsadz9L8x0fQefpCSeo48iBxNMxuNJQF3tOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d738f2c41.mp4?token=L8SSQOyXWPT1ZtQRX5ZY85UBD_JwFE_FrRLajw91YG3MUU1-DJmGIVQ59WEizlVDO5198c5dqAoaWpA0LVUsDC4J1dBduWPdKvf_po4oUANTzf-7epbRJBhIZ5i9UEYKMI9Ns1D_YvMFBoDaeWXnVtO5vtir7O29ge9ACkSr5LKfLFMxgwutbYfArj8mC9umT5hH9HMEkG4LndmvJoNCoVtsEM0xq3xFVJgxpm9OGlX9jseJULvQ4vxk8KSOPo2Zv6EaWwNwee1tRFalkMzva4U7YJ4TIUgdUNeOQOcseZ9Hx489LxMsadz9L8x0fQefpCSeo48iBxNMxuNJQF3tOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاق عجیب در کنسرت میثم ابراهیمی؛ سالن پلمب شد!
🔹
سالن برگزاری کنسرت میثم ابراهیمی در شهر پردیس در ۱۰ مهر، پس از برگزاری برنامه در ۹ مهر به دلیل نداشتن حجاب مخاطبان و ورود بطری‌های آب‌معدنی پلمب شد!
🔹
این خواننده با حضور در جمع مخاطبانش از آنها عذرخواهی کرد؛ ساعاتی بعد پس‌از پیگیری‌ها، کنسرت با تاخیر بالاخره برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/695595" target="_blank">📅 20:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695594">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-LNekFeaCvYGtHwKG1aqipBVfmwjBna3B5t1ZyKlWzCYZ-BFymteatXMa0Pm6akuVdgyBrUoYBYHvOgY1zRKgnK1brcAv9ke_t9bpvEXBssXs7qbHoK1sqeDCtuT0U0qnrn_xiEiaraklhL6iU-zEL6SFeL4RZ82H_W1IERKP04b_Gciq2f0X1-SZe69UVlbrvVnf03Oq7vjIEoHtih08NrcqPM9_2ZJScdE5hlC8TIqcPltcMNPKllnL0gVoiLoLTQfPxKRtj83AZFlMoToddSdjbyjj6PL9gGR16_P27Pp_TU-t7x_eHrNUBp7vLCt8N3NEgGf95sv6j07jx_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳۸ابزار هوش‌مصنوعی با کاربرد‌های متفاوت
!
#هوش_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/695594" target="_blank">📅 20:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695593">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592495b982.mp4?token=TZIOO9QHL7-y7_q7VlhDvh-yU1tAPeCJeMGDg2DfuyotWrHrMhwj9RWssEObLgHzIXdaQ42ShODVEqSXf25kJMgcwX_eGi1Gq4D84EbIc6Y-5DJaG6wh2oS6srHHDCsoHWhfT3rz4ABZuM3yaJXw4R8bKexvDZimygVwPE3jZC-fk2VMwVjGM75Im0iG2X0E9bG2HL-a_leWJ-HHuv6RUx8QMgqY9LavIvPM3vUYxNxpwbWV-72YhzHgOTxbJ5kmqSmuopkj3iLpQgjeGyQfqDnQQRllOERVGfN2YH2fCQKgAkE5yjtjj5DSKSWnn4Z1as6zD1L0omwkelqyKklNhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592495b982.mp4?token=TZIOO9QHL7-y7_q7VlhDvh-yU1tAPeCJeMGDg2DfuyotWrHrMhwj9RWssEObLgHzIXdaQ42ShODVEqSXf25kJMgcwX_eGi1Gq4D84EbIc6Y-5DJaG6wh2oS6srHHDCsoHWhfT3rz4ABZuM3yaJXw4R8bKexvDZimygVwPE3jZC-fk2VMwVjGM75Im0iG2X0E9bG2HL-a_leWJ-HHuv6RUx8QMgqY9LavIvPM3vUYxNxpwbWV-72YhzHgOTxbJ5kmqSmuopkj3iLpQgjeGyQfqDnQQRllOERVGfN2YH2fCQKgAkE5yjtjj5DSKSWnn4Z1as6zD1L0omwkelqyKklNhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بالاخره کی پاسخگوئه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/695593" target="_blank">📅 20:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695591">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16e95bbad.mp4?token=awl84j6n90QAi89g6pRx_wg9le6O_EvcY2fb_BtFU3ER2j5Vca4VvG_d1asPGySf8fX3OPd6G9fDyMHCElLyaUAuhYB0OFIUli9aiTcIIL1WGUglqtcnHOBhIj8MPmwThgFMrqMvAm9XM14bL5JSR5pbUeEVHIekSPH-NKK0rA5Fg1NhHv-a0O9ROdH6WpreRGDOfN3dp9L7X_lBBDVl76gn4XLgDTEOtFfaw9XAgSThDGyWvhSVc_7S4JsINEuHJj1_KlDL_8JvBQEka8Aogqp-PivH4Pmo9qA85KDMg4m9EE7b3rM1ohMNuHsx9bx_pML7q0WHbUcvpeeALj8YgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16e95bbad.mp4?token=awl84j6n90QAi89g6pRx_wg9le6O_EvcY2fb_BtFU3ER2j5Vca4VvG_d1asPGySf8fX3OPd6G9fDyMHCElLyaUAuhYB0OFIUli9aiTcIIL1WGUglqtcnHOBhIj8MPmwThgFMrqMvAm9XM14bL5JSR5pbUeEVHIekSPH-NKK0rA5Fg1NhHv-a0O9ROdH6WpreRGDOfN3dp9L7X_lBBDVl76gn4XLgDTEOtFfaw9XAgSThDGyWvhSVc_7S4JsINEuHJj1_KlDL_8JvBQEka8Aogqp-PivH4Pmo9qA85KDMg4m9EE7b3rM1ohMNuHsx9bx_pML7q0WHbUcvpeeALj8YgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه عبری: ایران، گورستان پهپادهای آمریکایی شده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/695591" target="_blank">📅 20:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695590">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">22-1 Ane Manaee (1404-02-09)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/695590" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌ودوم؛ بخش اول
🔹
"فی قلوبهم مرض"، یعنی ایمان واقعی در گرو “توحید” و “ولایت” است [01:09]
🔹
تفکیک امر خدا از امر پیامبر و عدم تبعیت از پیامبر به اسم عقلانیت و مصلحت‌گرایی یعنی نفاق! [09:56]
🔹
اشتباهاتی چون فراموشی، نشان‌دهنده سیره عقلایی و انسانی انبیاست، نه نقص در مقام نبوت [14:53]
🔹
پیراستگی جایگاه پیامبران از هرگونه خطا حتی در امور عرفی! [28:32]
🔹
مصلحت‌سنجی" یا "انحراف از حق"؟.. نقد به رفتارهای رسانه‌ای در ذبح اصول اعتقادی به بهانه دلجویی از برخی! [31:58]
🔹
"سکوت در شرایط فتنه"، رفتارهای تاکتیکی رهبران الهی برای مصالح بلندمدت بدون خدشه به اصول [38:27]
🔹
اهمیت حفظ محکمات فکری - عقیدتی در شرایط ابهام‌آلود سیاسی - اجتماعی [43:04]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/695590" target="_blank">📅 20:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695589">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما کدام عامل بیشترین نقش را در حفظ فرهنگ ایرانی در میان مردم دارد؟</h4>
<ul>
<li>✓ خانواده</li>
<li>✓ نظام آموزشی</li>
<li>✓ شبکه‌های اجتماعی</li>
<li>✓ نهادهای فرهنگی و هنری</li>
</ul>
</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/695589" target="_blank">📅 20:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695588">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/026bb1441e.mp4?token=RPxATQJbz_WIbjT82jQjgP1u0gVn1cBJyaBRoRYHkjDPRxfc4WWnyd2wfilVGq2Uoc1-7yner7Pdd8K1iBeBhNJqOW1RQ8yyUWkF6TzBJfcGYSS8UiH-Ss-yU-7kfaSUNRAqMACaqax6IG7uoRj9QLcRD8WYbwGOQHEjHG0Y-TP5H1s6uj6lLqd1DD-LQBKu9x5X-GKuMBrsiDwEBcPWMPSUd5WRkZ3R6Gc5dIabs7XFSrD-ZD_uHX6FvvjLaOGWT6mtp1tfQ7jbLR4Or2r0FoV--hZMwxQGS9pdMI6mgZoXNk_xvoA_kgEvUXoZH1WkDUdcNv95-TwHB-egb7AYkyM3EKjDfk4VLsCtLyV_EkkKODORPGoaXt5bp6N506vkG82XaDsiGanmvvvbi-f_gCOlps0vqV29cygOP8R3UhtD-9L47d30Qi4M41kJhLzr2hJtIjKa6tvidzO9ys9GWECESsfeWSh9g7XFFDaA9EkA_WMInFxeWgGCdOUFZpjD-JP-dZoGbAdSSmHqav_pQLBeJHTsSUxI4rHAd_tiU_bt76fTIPMzR58_93IKfbRX3R2XPsXRj3bOEOmhNNey_XQqlEWqgJnm87KHKNVO8wix01BmGTWODqcbw3pbKXbJiXc5P7NSHbQYerzsMcXdi8Rq6oZykmpkHNhDRb6XgQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/026bb1441e.mp4?token=RPxATQJbz_WIbjT82jQjgP1u0gVn1cBJyaBRoRYHkjDPRxfc4WWnyd2wfilVGq2Uoc1-7yner7Pdd8K1iBeBhNJqOW1RQ8yyUWkF6TzBJfcGYSS8UiH-Ss-yU-7kfaSUNRAqMACaqax6IG7uoRj9QLcRD8WYbwGOQHEjHG0Y-TP5H1s6uj6lLqd1DD-LQBKu9x5X-GKuMBrsiDwEBcPWMPSUd5WRkZ3R6Gc5dIabs7XFSrD-ZD_uHX6FvvjLaOGWT6mtp1tfQ7jbLR4Or2r0FoV--hZMwxQGS9pdMI6mgZoXNk_xvoA_kgEvUXoZH1WkDUdcNv95-TwHB-egb7AYkyM3EKjDfk4VLsCtLyV_EkkKODORPGoaXt5bp6N506vkG82XaDsiGanmvvvbi-f_gCOlps0vqV29cygOP8R3UhtD-9L47d30Qi4M41kJhLzr2hJtIjKa6tvidzO9ys9GWECESsfeWSh9g7XFFDaA9EkA_WMInFxeWgGCdOUFZpjD-JP-dZoGbAdSSmHqav_pQLBeJHTsSUxI4rHAd_tiU_bt76fTIPMzR58_93IKfbRX3R2XPsXRj3bOEOmhNNey_XQqlEWqgJnm87KHKNVO8wix01BmGTWODqcbw3pbKXbJiXc5P7NSHbQYerzsMcXdi8Rq6oZykmpkHNhDRb6XgQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمارهای عجیب و غریب از میزان تقاضای استارلینک در ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/695588" target="_blank">📅 19:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695587">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db760fe162.mp4?token=AJWPuBFctHu7mG9B3A0YHVuVTKu423XQkYcs0x9LiDYKXaqhFMVwgtMgCrwqt-gJ03ogGru4AOmya_-2ENvYCMxbAAcL1ma2cL6xsCB2ziugEKjyCxqg29Ngg8iOrS6qAmgJKPTK3ClvrhnUh9cpDaWTrH_sSsmLRcgJInu84n_u_c7TSJ7mTu32BBREo-rf21FzMdzGFhoUbub2201r7fwJ8ox-oa-onN2c1ae7gUewy3EDi42SDVI3o1fJeDMWtcot6WT4y4f_5Ppws7lSlDlEZvDQK1b61lMvlXvNZ619alTTgpvm4Ac8ZdASITBX5zzBFIGUS-3Qm5gdI4Afrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db760fe162.mp4?token=AJWPuBFctHu7mG9B3A0YHVuVTKu423XQkYcs0x9LiDYKXaqhFMVwgtMgCrwqt-gJ03ogGru4AOmya_-2ENvYCMxbAAcL1ma2cL6xsCB2ziugEKjyCxqg29Ngg8iOrS6qAmgJKPTK3ClvrhnUh9cpDaWTrH_sSsmLRcgJInu84n_u_c7TSJ7mTu32BBREo-rf21FzMdzGFhoUbub2201r7fwJ8ox-oa-onN2c1ae7gUewy3EDi42SDVI3o1fJeDMWtcot6WT4y4f_5Ppws7lSlDlEZvDQK1b61lMvlXvNZ619alTTgpvm4Ac8ZdASITBX5zzBFIGUS-3Qm5gdI4Afrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سه‌ترفند کاربردی در آشپزی
🍳
🔹
سیو کن یادت نره.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/695587" target="_blank">📅 19:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695586">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال اطلاع‌رسانی سازمان توسعه تجارت ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31788f03a.mp4?token=jTIL_S6qV0iEee532eqhlfvD6vm81qNjPdBi9w-qcmvt6_I00r2cf_aGUrp3aLD16gTqzYKTLLX7wIzI8_I9oeAPg_zlQv504x8Giw3J_URru0FjoemUhnU6QqQt-4hDSp7r4KvVaJsr8HnXvGZD19A4PMeCjm7o5oTuUCsPTvxspN7QA4siCTQadBu-mE_s90ivh-xVB5GjdKfWIHGcSdF0eg2VvTLE3sih8VaUjAqWl3qrLvSIQwpPKSHkcww05coJSODLygDvPNZGUClPTjE9R3GeW8QQ7mwt62EoYHhzx_-IL0neabiOlE4vi87Yebwj3OGpTvys7Sm9hZ22DAbrzcnNRSIESghz_aEkiUgx3HtKrBAe_xY67NwQwtdKZkt4YvXn4Uk05Tbi-i88tNSb7bGDKeYv4BN9ful1Cuuys8hXCQuKCfydAkHzIPPvz0A90v82_PneC5ji8rrE2swPOeK3BeOPbnhTbfpNyPZFrjfwRNe99w7AqS_dXZr_RtCizTx5VzC0_yvFh1ePXaCxwtT1gLNadvqZAVTmoDChCYQn5uxR1t1id69hDKesPv_692FzDmHKUAV9hK2IBY-dZkIeI8z4-alC_lIwL69G2FxjaBjA_vpGNpHZrwA-mObGY-a9cwFMGbuJmnJnU3XwxgLTzUYMF1NcE2vsCPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31788f03a.mp4?token=jTIL_S6qV0iEee532eqhlfvD6vm81qNjPdBi9w-qcmvt6_I00r2cf_aGUrp3aLD16gTqzYKTLLX7wIzI8_I9oeAPg_zlQv504x8Giw3J_URru0FjoemUhnU6QqQt-4hDSp7r4KvVaJsr8HnXvGZD19A4PMeCjm7o5oTuUCsPTvxspN7QA4siCTQadBu-mE_s90ivh-xVB5GjdKfWIHGcSdF0eg2VvTLE3sih8VaUjAqWl3qrLvSIQwpPKSHkcww05coJSODLygDvPNZGUClPTjE9R3GeW8QQ7mwt62EoYHhzx_-IL0neabiOlE4vi87Yebwj3OGpTvys7Sm9hZ22DAbrzcnNRSIESghz_aEkiUgx3HtKrBAe_xY67NwQwtdKZkt4YvXn4Uk05Tbi-i88tNSb7bGDKeYv4BN9ful1Cuuys8hXCQuKCfydAkHzIPPvz0A90v82_PneC5ji8rrE2swPOeK3BeOPbnhTbfpNyPZFrjfwRNe99w7AqS_dXZr_RtCizTx5VzC0_yvFh1ePXaCxwtT1gLNadvqZAVTmoDChCYQn5uxR1t1id69hDKesPv_692FzDmHKUAV9hK2IBY-dZkIeI8z4-alC_lIwL69G2FxjaBjA_vpGNpHZrwA-mObGY-a9cwFMGbuJmnJnU3XwxgLTzUYMF1NcE2vsCPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🔻
سه دهه تجلیل از قهرمانان صادرات
🔻
🔻
29 مهر؛ نماد تجارت ایران
🔹
روابط عمومی سازمان توسعه تجارت ایران
پایگاه خبری
|
تلگرام
|
بله
|
واتساپ
| ‌
آپارات</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/695586" target="_blank">📅 19:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695585">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: در کنکور امسال یک سؤال برای چند دقیقه درز کرد که به‌سرعت شناسایی شد و به‌گونه‌ای نبود که بر نتایج کلی کنکور تأثیر بگذارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/695585" target="_blank">📅 19:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695584">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افشاگری نماینده مجلس از گروکشی کارتل‌های بزرگ برای دریافت ارز تا همکاری دوباره دولت با آن‌ها
پیمان فلسفی، نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
برخی کارتل‌های بزرگ وقتی دیدند کشور با کمبود ارز مواجه است، تهدید کردند که تا زمانی که ارز ما تامین نشود کالا را تحویل نمی‌دهیم؛ به نوعی گروکشی کردند.
🔹
این‌ها در مقطعی بحران درست کردند و به بازار نهاده‌های دامی و کالاهای اساسی واقعا شوک وارد کردند.
🔹
برخی از این شرکت‌ها که تعداد آنها به سه تا چهار مورد بیشتر نمی‌رسید با عملکرد نامناسبی فضا را تحت تاثیر قرار دادند که باید با اینها برخورد شود.
🔹
فکر میکنم دوباره همکاری با این شرکت‌ها شروع شده است ؛ وزارت جهاد کشاورزی و بانک مرکزی با این شرکت‌ها کار می‌کنند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/695584" target="_blank">📅 19:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695579">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">honar_v1.pdf</div>
  <div class="tg-doc-extra">18.2 MB</div>
</div>
<a href="https://t.me/akhbarefori/695579" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دفترچه انتخاب رشته کنکور ۱۴۰۵ منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/695579" target="_blank">📅 19:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695578">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
تمدید ۲ ماهه مهلت خودروهای گذر موقت
🔹
گمرک به مدیران مرزی و استانی اجازه داد بدون مکاتبه با تهران، مهلت پلاک گذر موقت خودروها را ۲ ماه تمدید کنند؛ این تصمیم شامل مسافران و سرمایه‌گذاران خارجی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/695578" target="_blank">📅 19:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695576">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KD-b3nV9NUuiHgEbqw-A-0TAb6rzoPDDKxuwjeAUB6QhBHvsYercy7Mo79alwewfnQp54XAQtAa27zXKVY4j1armAUczJef0yBVceDg2NGG1cvzHgyROb_vPzI0-X6VvoAO4viWISyzhJNTADUTddjofSRvaA7ZHf65XGcZ2bCOnDfxH4qgWcsmZoc90paOZkBdlEXBZGark2e2WY1NSyaW7MxCJKLE_xDVSJp6MxwCkyF98cJ6nNL7IPKluBp9aMD7ULI_LxEuKW8FUXD7LxH-X38YYIKL-MzLI7Uu2aYrTXARy4zQjwNHnuotBI06fTdZaE84y95LXS8AGgyLA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqNXn3wHePMjvfvggvtB7RJiNh9GOWQPhd2jVbFYZnHsqk1afOd2ffQx9_jCfGe4XZ0LdYjJOg7P0Ytwhry4-LmGyLD1Fj9e7lhuxmeM6CwUSQVlXL5alMUgbHUDSGDZ9mZmbCqymNiyyos2hKpbZIM2-65NJCMzbrV-0UrQUUNl-WeJ-sZEeVkoEQfOZTUTxlIxFKVbTgxZ7UAo8g-q45CYBKFz8OD63A9JylHeL1IwDHcTHmonX8VWD-qAGzvk9eQ-cxTdyzXfOJ9PNGRuKsyE5s0yhzZquT10F9Yfx2_6pp6e_f8qp03-TGlwky7GggIqt-qr4E8W3_WVKA6f6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عکس اتاقتون رو به ai بدید و منتظر باشید تا با شناختی که ازتون داره اتاقتون رو دیزاین کنه
:)))
Use the uploaded photo of my room as the base image and redesign/fill the room based on what you already know about me from our previous conversations.
Your goal is to make the room feel like a realistic physical reflection of my personality, interests, habits, hobbies, taste, lifestyle, and the things I care about.
Before making any changes, silently consider what you already know about me, such as my interests, favorite activities, aesthetic preferences, technology or gaming interests, creative work, entertainment tastes, routines, and other relevant preferences. Use only information you genuinely know from our conversations; do not invent personal facts just to fill the space.
Preserve the original room itself as much as possible:
Keep the same architecture, walls, windows, doors, floor, ceiling, room dimensions, camera angle, perspective, and overall layout.
Do not turn it into a completely different room or location.
Keep existing furniture when it makes sense, but you may reorganize it slightly if needed.
Add, replace, or decorate objects only where they could realistically exist in the photographed space.
Fill and personalize the room with items that make sense specifically for me. These may include furniture, decorations, technology, desk accessories, lighting, posters, books, collectibles, gaming equipment, creative tools, personal objects, or other details that naturally match what you know about me.
Do not add random generic decorations. Every noticeable object should either serve a practical purpose, reflect something you know about me, or improve the overall coherence of the room.
Make the result feel lived-in and believable rather than like a furniture showroom. Include subtle everyday details such as naturally placed cables, objects on the desk, small personal items, realistic storage, and signs that someone actually uses the room, while keeping it visually organized.
Match the lighting, shadows, reflections, scale, material textures, and perspective of all new objects to the original photograph so everything looks physically present in the real room.
Do not add people.
The final image should look like the same real room after it has been thoughtfully personalized for me—not a generic “dream room.”
Prioritize:
1. Personal relevance
2. Realism
3. Preservation of the original room
4. Functional and believable object placement
5. Visual coherence
Output only the final transformed room image.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/695576" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695575">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6J65YQ5pVDc-IGpxN5Fpy-Pc6McwNo2bN1mqaxdWdizGfnrxy0UuV6J7-sZUefkN185STfmh36Ou4LRM-Gyoz4fQFJ4uMGFWzm4UhDn9aVPqhQgHD5eqggeX4tCB_BglVav9NhtbLoEIizr4onVBF77pcfUOhwknduFiMuNbKerfigDWMJMUYl8Zl-7irybJF3qHV5uHAG8htsVC01rem7ug8-0nWbyvWzeDC3NxbXgFFVGau5dOZKrnsEEeThoIihGG6QyXGk7ykTUsCT-v7-A-XKWbL3b-r-NHfkJVSSPh-tjzr1UPfDHgtYmNw5JXjyhWtryHDZ-47PXzfYpdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو دفتر سیاسی جنبش انصارالله یمن: با یاری و لطف خداوند، تعز آزاد شد و آرامکو ریاض و خریص در آتش می‌سوزند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/695575" target="_blank">📅 19:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695574">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
حال و هوای هالووینی خیابان‌های آمریکا
🇺🇸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/695574" target="_blank">📅 19:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695573">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8sjn4Mabu-F-L5lRWnMYQmSEShj1KrEiMGK0pvHI0dM0i_lnVrj_8qw8EFZYmeT2hHgR_UaKLAqtiQNpMm2v82Zfs92cfM7QVgmWgrmuFVOWartMbjTPmsYF513TZfBtYEXxq4xzyu_HdSAlIQqWReIMJMjP6ZlACtVOXBVCWyZ1_WKeqAW5k9r1IxmAAbpVp4ECqSBM-aWigsqMDJlj577jUq8_Y71rPuOfE3Cy11n64054sCB6vYueEWpwIqbmsuNZZvLJI2n6FrCmBE6seaEmxKHgyXD-0NP9qcEdwbfs0Oi1z8gJzxSw7iqf6JTX1d0PEc9i3z21TzdgzMZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی در کدام صنایع بیشتر نفوذ کرده است؟
🔸
بر اساس پیمایش جهانی McKinsey، فناوری بیشترین میزان استفاده از هوش مصنوعی را در بخش فناوری با ۴۱ درصد دارد. پس از آن، ارائه‌دهندگان خدمات سلامت (۳۹٪)، خدمات حرفه‌ای و انرژی و مواد (۳۸٪) در رتبه‌های بعدی قرار گرفته‌اند.
🔸
گسترش هوش مصنوعی در صنایع مختلف نشان می‌دهد شرکت‌ها بیش از گذشته از این فناوری برای تحلیل داده، اتوماسیون فرآیندها، بهبود خدمات و افزایش بهره‌وری استفاده می‌کنند.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/695573" target="_blank">📅 19:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695572">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
وزارت ورزش و جوانان: ۱۴ میلیون جوان در سن ازدواج در کشور، مجرد هستند و هرگز ازدواج نکرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/695572" target="_blank">📅 19:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695571">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سرقت ساعت ۵ میلیاردی سفیر فیلیپین در تهران
🔹
ساعت طلای سفیر فیلیپین در تهران از خانه او در شهرک غرب سرقت شد؛ پلیس یکی از پرستارانی را که برای نگهداری از فرزند سفیر استخدام شده بود، بازداشت کرد.
🔹
متهم به سرقت ساعت طلا و برلیان اعتراف کرده و تحقیقات درباره پرونده ادامه دارد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/695571" target="_blank">📅 19:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695570">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842665b733.mp4?token=ZeBeguSu1ZT6nrqmHVFccEHvOy4jgmSPWtge0xO9KexTqDMXlH5B5SRBR9RcNm9eRZTanyog2bzD1MWsvwGjZc1MsXsdjiWVjwshv-tUnF3DqO_y8Kapu8zBeq8YabISNJ6WHmE7a9qQjm743ax0yZRNDrYF9JglazRBsyTsSxg6rCPEscaMuFXI7DyDHbNFJE9wZi0mB0siaw8zX1f6vt9AAolzYud9lnbhKVZzWqMCPbLRyVompNPkIiHkBjkVez3ey7uoDBhfyDI78unBcn2HLMawfYNoFxvKzRVfoaQzjfkENHfzaWHZFNtFjnJ6rRDdzsm-aJ5m7ubZvJCLMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842665b733.mp4?token=ZeBeguSu1ZT6nrqmHVFccEHvOy4jgmSPWtge0xO9KexTqDMXlH5B5SRBR9RcNm9eRZTanyog2bzD1MWsvwGjZc1MsXsdjiWVjwshv-tUnF3DqO_y8Kapu8zBeq8YabISNJ6WHmE7a9qQjm743ax0yZRNDrYF9JglazRBsyTsSxg6rCPEscaMuFXI7DyDHbNFJE9wZi0mB0siaw8zX1f6vt9AAolzYud9lnbhKVZzWqMCPbLRyVompNPkIiHkBjkVez3ey7uoDBhfyDI78unBcn2HLMawfYNoFxvKzRVfoaQzjfkENHfzaWHZFNtFjnJ6rRDdzsm-aJ5m7ubZvJCLMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی وایرال شده از کیفیت تجهیزات خودروهای داخلی: شیشه شور کوئیک داخل اتاق!!
🔹
آب‌پاش شیشه پشت کوییک به‌جای اینکه بیرون ماشین نصب شده باشه داخل اتاقه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/695570" target="_blank">📅 19:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695569">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d58981eab.mp4?token=g5jX3wnTD7uzagbPLTES1wwjR4MBP4xGk_E7gsn-KSOFZF6GKfQR_cD8I4X4jKyE0GZ2gpHTv98ScSFtXWQKxI6f7elO2BcK9zZecKYbGqbYdUTsIV8ijvgiGtVoI5_3O5c46AOGfAuQM9-N7aMYjIZ5fhp4SXAfpHLrLLhGnMs_c773qOkt0EbN5UPe7Ievd2GrqEv5AdX4bXRcbTItYx1kK9mA2q44jYbCOsujn33tVsI7yg-3bEi-aLLpfLnytFt6L3JOKPZEmgP_nGw5ZDLe0ySnp18cxc8klB8zm8pjfMS86r8R9ki9QDnLfpr1E6lrLCOjJE4yr-cimw9oXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d58981eab.mp4?token=g5jX3wnTD7uzagbPLTES1wwjR4MBP4xGk_E7gsn-KSOFZF6GKfQR_cD8I4X4jKyE0GZ2gpHTv98ScSFtXWQKxI6f7elO2BcK9zZecKYbGqbYdUTsIV8ijvgiGtVoI5_3O5c46AOGfAuQM9-N7aMYjIZ5fhp4SXAfpHLrLLhGnMs_c773qOkt0EbN5UPe7Ievd2GrqEv5AdX4bXRcbTItYx1kK9mA2q44jYbCOsujn33tVsI7yg-3bEi-aLLpfLnytFt6L3JOKPZEmgP_nGw5ZDLe0ySnp18cxc8klB8zm8pjfMS86r8R9ki9QDnLfpr1E6lrLCOjJE4yr-cimw9oXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیاوش جمشیدی، از اوباش مسلح شهرکرد اعدام شد
🔹
کلاهبرداری، تهدید، سرقت، حمل و نگهداری سلاح جنگی، مشارکت در آدم‌ربایی، قدرت‌نمایی، واردکردن صدمه بدنی عمدی، تهدید با سلاح گرم و شلیک با سلاح کمری مقابل حوزه علمیه شهرکرد، از جمله سوابق متعدد سیاوش جمشیدی بود.…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/695569" target="_blank">📅 19:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695567">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromصبانت | Sabanet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOR7RyvZmk9xxDuV0dwBLKi_bSjPq1az1y_jyEwQv7JM5FUUkRP_Eytz5gY9vIOuLiXqa22CfD9HHQ6gG9_JJVrsCOIEHeMBVi6EAJzadWlTVNRTEztsdE5mqtwtUTqovD7HsSg9WfLo1QUd2fjO4wt43NybFXoDO4h2-N-QDgD0R6eBoKyK0Aco83q69907wiBanLKyqRSOXDfhSId_6D1DQedbbitjMIMkdKMZwS_Ao56gCsGAPG9i0aE4pHYJERCKYTLX8KRVKDSbfEUG8ETk7jLh_6aL6P8TFQDAFwdNKRfjD4K8w1jBGZf8GhB0GO5tVOU6f0G5pbzSbQU1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت قطع شده؟
😶
🔴
نه برای همه!
وقتی بقیه دنبال وصل شدنن،
تو
با صبانت
، بدون توقف به کارهات برس.
🌐
اینترنت پایدار، پرسرعت و بدون مکث
⚡
سرویس‌های ویژه برای اتصالی مطمئن‌تر
🎮
پینگ پایین برای بازی آنلاین
📥
دانلود سریع فایل‌های حجیم
📡
اتصال همزمان چند دستگاه بدون افت سرعت
🔴
صبانت یعنی؛ وقتی بقیه متوقف میشن، تو ادامه میدی.
☎️
1524
🔗
sabanet.ir/UR
#اینترنت
#فیبرنوری
#صبانت
#اینترنت_پرسرعت</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/695567" target="_blank">📅 19:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695561">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
معاون وزارت رفاه: حساب بیش از ۴۰۰ هزار نفر از مادران، تا چند ساعت آینده شارژ می شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/695561" target="_blank">📅 18:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695560">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leX2J2wgqya0opg_Tu9YS9b5stuaWWY-x_pXCFuNiWTcXcI31JAoS_-6WNELwcUrjMytNHbiwPPQLxRMqd_FFX45vJ8Y56xduBW_Gmt6mJdJO4TKZo5IxPKH4Y3P-Lj5y-J6iefZ28Iwu3eA5dbl1mpngWkNm0wSVTME-Z1H7PYo3perMpAOtuoVl49Nri4K3EQNXwAgm77D9dQ0VefOHjLJEZb-aD0ZWiLv6R8IgG6lFapguVdn74b7L4YcG8YlRmjYpOmb4BYH0bwMvSr-sKW--zeuZjJMIBeVw3HsjQYSPYocLbvdXdd6BziiT9w7D39t3UqrifWOnh7d3f_eYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از آسیب شدید به یک فروند هواپیمای شناسایی RE-3A عربستان در جریان حملات ایران به پایگاه هوایی شاهزاده سلطان در مارس ۲۰۲۶ حکایت دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/695560" target="_blank">📅 18:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695559">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873583313c.mp4?token=QEbKn08UG66kYECnzEmR9HmRyCX9Ino5OSn97lJh7Eou-nKeVA7XV8pr21xMO7SNhCW9S4oEs_gWOQgOwYHAroM-R4G2gAQSZ7OhUsKH3zZ4HHFs_6m647TZJiE7R2IlaWFfZhkaiV51W1ASLC5HI8HnAAseViqyv3KtdXflO2ebwvUY1cxcyTiBxhA35yHZtf8Ih9O-KZ49Uj4-YrUw6TikAf1o34V8Xhuw2gx1RsEyJxenY8dJdNz6AruTkBR4NowR7Rlc8TlxNEII4r31AC6dg1i2ASLAx02MonSPjSzZAg0dNjyRfEOI36px81qdBUhq5sEP0IfQ89484bjb3FnfeR6tu3wNMhLY2y99ws1h79ZPP2EiY_fRexIDqBBR-KguxeDVpJFT8c4K2cF3yNBGIJINs9_VYpnbdIQ9xM_FW-VGoHYuRcMR5lJ5cwiAa-E7fsqlpaiwh4jIpJTSkxoGcI_lUbIv_F8l4qjGm7O7M0GNX2tD6GqWABe1gOyp-SqvbHnxc57cmws27PxBJzUqZSxJ2KFZ7HfeXZyxsMyY1UyM0I0rAgZGKDspghLq6do6fKFvpUmEvNRP-qSunOZCE0q2YvGbtihG7_yoIWtdT6YdD-OHftTaNbYr0sFyjSLXyNoFTerzTvkSsW8LQM_UykpNeX0qTq8oGhxLHJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873583313c.mp4?token=QEbKn08UG66kYECnzEmR9HmRyCX9Ino5OSn97lJh7Eou-nKeVA7XV8pr21xMO7SNhCW9S4oEs_gWOQgOwYHAroM-R4G2gAQSZ7OhUsKH3zZ4HHFs_6m647TZJiE7R2IlaWFfZhkaiV51W1ASLC5HI8HnAAseViqyv3KtdXflO2ebwvUY1cxcyTiBxhA35yHZtf8Ih9O-KZ49Uj4-YrUw6TikAf1o34V8Xhuw2gx1RsEyJxenY8dJdNz6AruTkBR4NowR7Rlc8TlxNEII4r31AC6dg1i2ASLAx02MonSPjSzZAg0dNjyRfEOI36px81qdBUhq5sEP0IfQ89484bjb3FnfeR6tu3wNMhLY2y99ws1h79ZPP2EiY_fRexIDqBBR-KguxeDVpJFT8c4K2cF3yNBGIJINs9_VYpnbdIQ9xM_FW-VGoHYuRcMR5lJ5cwiAa-E7fsqlpaiwh4jIpJTSkxoGcI_lUbIv_F8l4qjGm7O7M0GNX2tD6GqWABe1gOyp-SqvbHnxc57cmws27PxBJzUqZSxJ2KFZ7HfeXZyxsMyY1UyM0I0rAgZGKDspghLq6do6fKFvpUmEvNRP-qSunOZCE0q2YvGbtihG7_yoIWtdT6YdD-OHftTaNbYr0sFyjSLXyNoFTerzTvkSsW8LQM_UykpNeX0qTq8oGhxLHJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک‌
لحظه غفلت یک عمر بی آبرویی
🔹
در چین در صورت عبور از چراغ قرمز عکس فرد خاطی در تقاطع‌ها گذاشته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/695559" target="_blank">📅 18:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695555">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxwVV6vNW0OoVNZXt7YY02cvHRF5XV8qkVw9bbxMPoWiiyVyjX7YH7xcJs6ct_YQTlsuHGanoSD9r0tgr_BMO6N39OtZedEQGpexU8rUhZTaEXSYkWUBhjCzhkl4XP53z8GY9jbKQyGcxLAvyaZJtPyWSMSdQwDciPRsp5giAWd5xytuqLBAk3gIuU37rAzQE8uGbGOxvbfhv3MD73P1WVguYdHIdkE7u2zV2dlDXo3cUMlJJIeHFw4HzCSt3rtj4ks8HmbtdJ1znvWx_rzSKB4L1Anqh2aoAba1P8R42_HlKllKXCWBw1WcxSykoJWkVe8XarsEkOLrDyga5a--eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از رعد و
برق دیشب ساری
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/695555" target="_blank">📅 18:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695554">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca56ffa255.mp4?token=J0WUwk3XBC27NCl4a99WCSZuCyubJiSAyjX_YuXFUSVk3HvaP6iPniOOOktRTYuy3h3HfYtfbWo4rV7lyA-Mv1Xzyv11fg2HBtC98ldpYm_UqBlEBJ_GZVakO66MIyItp53h5m7J-hPNxMGop73o3eMJ4CwErXbjDmm1OEN_zMDLGHh5dNIJfjDCPsGlPnmbyboF5u8rgjdLLYH_aNQa40Qycq8H52qGWjy6RBLHgmE5NvtRnFPNGO9YIHHAuLtn7OJ5JYlE6JAE8oHWVadU6kHrfxAvVXbzDBZTApd7AqzGy2G0zkXhZjiDk6BnGYM9uv7W2ijYrMsjch5cFf_5w4GBAFuANNKaY5-o4ZvMGC6LWWb8UhcrJ7IWQ4GKshWQTi8yYsD-Vt-dnBgaVicmGOKKNOKmQqEfP9as6-u9q9KBbKvUKN8GH9PouSO1p89CfPkcSjwwi8tCyUzr-m2btATvZvXVBVhHAh7eeGlxXcFJnDZk0nj5goxrLEg1AvY3gFUSKhvnyoM9I3n2bNv3RT-jjNcACoOmdJX76kfJiUfloPRl7VxGbdIMwAk5eUKUk-5yYxsrakiebaUqbA2jjrns2POzSa0UsiulelbttW-fmSpvBaz1f8xaZ9nCfNvRKafGBnxpb8nKj9fE7ni9l5TVMscNlPz3-avzli6ukg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca56ffa255.mp4?token=J0WUwk3XBC27NCl4a99WCSZuCyubJiSAyjX_YuXFUSVk3HvaP6iPniOOOktRTYuy3h3HfYtfbWo4rV7lyA-Mv1Xzyv11fg2HBtC98ldpYm_UqBlEBJ_GZVakO66MIyItp53h5m7J-hPNxMGop73o3eMJ4CwErXbjDmm1OEN_zMDLGHh5dNIJfjDCPsGlPnmbyboF5u8rgjdLLYH_aNQa40Qycq8H52qGWjy6RBLHgmE5NvtRnFPNGO9YIHHAuLtn7OJ5JYlE6JAE8oHWVadU6kHrfxAvVXbzDBZTApd7AqzGy2G0zkXhZjiDk6BnGYM9uv7W2ijYrMsjch5cFf_5w4GBAFuANNKaY5-o4ZvMGC6LWWb8UhcrJ7IWQ4GKshWQTi8yYsD-Vt-dnBgaVicmGOKKNOKmQqEfP9as6-u9q9KBbKvUKN8GH9PouSO1p89CfPkcSjwwi8tCyUzr-m2btATvZvXVBVhHAh7eeGlxXcFJnDZk0nj5goxrLEg1AvY3gFUSKhvnyoM9I3n2bNv3RT-jjNcACoOmdJX76kfJiUfloPRl7VxGbdIMwAk5eUKUk-5yYxsrakiebaUqbA2jjrns2POzSa0UsiulelbttW-fmSpvBaz1f8xaZ9nCfNvRKafGBnxpb8nKj9fE7ni9l5TVMscNlPz3-avzli6ukg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
بازسازی جنگ بدر و نبرد تن به تن حضرت علی (ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/695554" target="_blank">📅 18:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695551">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سازمان مدیریت بحران: بارش‌های اخیر ۱۸ خودرو را دچار خسارت کرد
امید محترمی، معاون سازمان مدیریت بحران در
#گفتگو
با خبرفوری:
🔹
در پی بارش‌های اخیر
۱۸ خودرو
در استان‌های کرج، البرز و خوزستان دچار خسارت شدند که همه خسارت‌ها سطحی بوده و حادثه سنگین یا خسارت جدی به خودروها گزارش نشده است.
🔹
۱۰ واحد تجاری و مسکونی نیز دچار آب‌گرفتگی جزئی شدند و حدود ۵۴ مورد سقوط اشیا، تابلو و درخت در نقاط مختلف ثبت شده است.
🔹
یک جریان آب با ارتفاع حدود ۲۰ سانتی‌متر می‌تواند به‌ راحتی خودروی سواری را واژگون کند، بنابراین هنگام جریان داشتن آب روی جاده یا خیابان نباید با خودرو وارد مسیر شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/695551" target="_blank">📅 18:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695550">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac482bfcef.mp4?token=u_BTd4mj5EQwcxpY6vGo6AIIGGfs_90nIpek36KVqXHZ5F4XHJECgulfGzKUFQI_i_0tJzO2qG1cVc5XstuO8KDxfsa6iq1JjtF1zlTO2VorIKMCyiQn9FMxGtoanjCMvtNmrhFshhQKmecz_YiNp9ItMaWMgMZ5tl3s6mD4_88wa_jfz5aveC8EDjk6-CBCzwQPdL26mCy2RNnKyClXOGAxLPOWxZkhr20QgfzdEr4SpPZto8Syy5ngHpEP_sGUNgQYBCEPOrfP7uLu7M8Jm2RhyDHtV80ewX3sOAFcDi58Y4VN3v7zy-vt0ZTvZi0xpAPF9URRpBC8FL3jNSy00w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac482bfcef.mp4?token=u_BTd4mj5EQwcxpY6vGo6AIIGGfs_90nIpek36KVqXHZ5F4XHJECgulfGzKUFQI_i_0tJzO2qG1cVc5XstuO8KDxfsa6iq1JjtF1zlTO2VorIKMCyiQn9FMxGtoanjCMvtNmrhFshhQKmecz_YiNp9ItMaWMgMZ5tl3s6mD4_88wa_jfz5aveC8EDjk6-CBCzwQPdL26mCy2RNnKyClXOGAxLPOWxZkhr20QgfzdEr4SpPZto8Syy5ngHpEP_sGUNgQYBCEPOrfP7uLu7M8Jm2RhyDHtV80ewX3sOAFcDi58Y4VN3v7zy-vt0ZTvZi0xpAPF9URRpBC8FL3jNSy00w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/695550" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695549">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFaraDars_Course</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JORSQP5GNv82_lp29Gi1FjZ1DG-IHILq3smgHoYckZrhMuYkt4KdwGilcwyfrdtcAF35HoP5Fau-_jGgAgE_dgQHr-ZdM-0Wv2oeVmvfHW7TJJCEJH-wXlWS29EY5McFfM_RpSGgq_1wbFZdUrvYv1nmWFADJU-j8Md1ySJxMf_rpQTZ-4wXz6DHldIQx3Qa1FMtFwr6LAUdX775Y_qZ0V7_Vi1CRbKk2byn_80yF-OqnUb6KWB-zodNT3bVw93OjMWSrFADRmki2bs8AgNILMiBXhEgvS56VXBCuoR3fwCscgfC9Cj3OAwBXJvyLSyePbI-tEaQVNBEdcGd6NErNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
خبر فوری — انتخاب رشته کاملاً رایگان و هوشمند با «مسیر»
🔥
نرم‌افزار «مسیر» توسط فرادرس و برای داوطلبان ورود به دانشگاه ارائه شده که ابزاری رایگان برای انتخاب رشته است.
✅
بررسی بیش از ۳۴ هزار رشته‌محل
✅
معرفی بیش از ۷۰۰ رشته تحصیلی
✅
جمع آوری اطلاعات بیش از ۸۰۰ دانشگاه
✅
مقایسه گزینه‌ها و ساخت فهرست انتخاب‌ها
🔗
شروع رایگان انتخاب رشته با مسیر [+]
🔥
رشته‌های دانشگاهی را بر اساس گروه‌های اصلی کنکور بررسی کنید و با مسیر و محتوای آموزشی هر رشته آشنا شوید.
@MasirGuide
— کانال تلگرام مسیر
FaraDars — کانال تلگرام فرادرس</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/695549" target="_blank">📅 18:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695548">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2f834fa.mp4?token=ekKW8G7h7EPfZrRHCacWx30cF5WOrYDb9knABGLZMSTnP3_bzwqcBR3tG6cjr91g8mI8GVJqE-qXv2mwH1s2-rGwYopuVJcv1NAcY6J8IxlZxqI6vF_oHsDYsPfyBFVpOKLF71AUnZKjxqGJ1yq4pro42wzU4rhaBy83xsjrU2Njz4b7Vra9F5xIY0EWUl4yFMKxf62bWE_yD8LcR7Ef_F2-NP5ICR08-2mqGfwtaH4n-_CkDeniInIvKIJoeeIcXIHJFybu1P5UKVFllz1-IP9BrtF2DOh5V2qAE5lSlIe4h6tsT1Rm6eBLSSeXCnlv4kgmrFygPwtHrM5vx4rbYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2f834fa.mp4?token=ekKW8G7h7EPfZrRHCacWx30cF5WOrYDb9knABGLZMSTnP3_bzwqcBR3tG6cjr91g8mI8GVJqE-qXv2mwH1s2-rGwYopuVJcv1NAcY6J8IxlZxqI6vF_oHsDYsPfyBFVpOKLF71AUnZKjxqGJ1yq4pro42wzU4rhaBy83xsjrU2Njz4b7Vra9F5xIY0EWUl4yFMKxf62bWE_yD8LcR7Ef_F2-NP5ICR08-2mqGfwtaH4n-_CkDeniInIvKIJoeeIcXIHJFybu1P5UKVFllz1-IP9BrtF2DOh5V2qAE5lSlIe4h6tsT1Rm6eBLSSeXCnlv4kgmrFygPwtHrM5vx4rbYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فشارسنج خون درجه 1 برند Arm Style
قیمت ویژه و فوق اقتصادی
📌
استفاده راحت فقط با یک دکمه
📌
کیفیت عالی
📌
دقیق و بدون خطا
قیمت نقدی:1,698,000 تومن
🌟
امکان پرداخت قسطی هم داری
✅
4 قسط 480 تومنی
🔥
تخفیف تا 15 شهریور
🔥
🏠
پرداخت درب منزل + ضمانت بازگشت وجه در صورت خرابی
خرید سریعو کسب اطلاعات بیشتر :
👇
https://memarket24.ir/product/fast/37863/180124</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/695548" target="_blank">📅 18:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695547">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
صدای انفجار از داخل پایگاه ارتش اسرائیل در نقب به گوش رسید و دود غلیظی از آن به هوا برخواست که از مسافت‌های دور قابل مشاهده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/695547" target="_blank">📅 17:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695546">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7e577ef3.mp4?token=jebEJL1occFjgmfabSQ3PK6hhvMyT3SfSW9doVYSwlzZZCXqOyP1IEEUAVJtSUdmArL73Cjzy3ktpoE7Pl_O7v_08MOpCYkTpU-IcSp-U9MPbxVfGWQ63f6QHC5xrBcTiLBa3hnE_F1o7UCV_zQzOrSrPK6PNNaiZzJtFBRWZbr3JMoUpc3uqIahGfpr388AHQIn1czug0i20vFwBdN_lwWmhR0SZTzmXMo7UijPUR65wI2P-C0IsvzrinR9p3lAVnVJ3xHd2fhWCCYNrZ26abUsEy09nb3KKAjGq5o_tuCdHLmF-5CUJtz_Dq_kvSx_BpKCHgHRCNdqUohe5plNzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7e577ef3.mp4?token=jebEJL1occFjgmfabSQ3PK6hhvMyT3SfSW9doVYSwlzZZCXqOyP1IEEUAVJtSUdmArL73Cjzy3ktpoE7Pl_O7v_08MOpCYkTpU-IcSp-U9MPbxVfGWQ63f6QHC5xrBcTiLBa3hnE_F1o7UCV_zQzOrSrPK6PNNaiZzJtFBRWZbr3JMoUpc3uqIahGfpr388AHQIn1czug0i20vFwBdN_lwWmhR0SZTzmXMo7UijPUR65wI2P-C0IsvzrinR9p3lAVnVJ3xHd2fhWCCYNrZ26abUsEy09nb3KKAjGq5o_tuCdHLmF-5CUJtz_Dq_kvSx_BpKCHgHRCNdqUohe5plNzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: سوال درباره قیمت دلار را از آقای همتی بپرسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/695546" target="_blank">📅 17:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695545">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
بانک‌های مرکزی هنوز طلا می‌خرند
🔹
بانک‌های مرکزی در جدیدترین خریدهای خود ۲۳ تن طلای خالص خریدند. چین با ۲۰ تن و لهستان با ۸ تن در صدر این خریدها بودند. از ابتدای سال نیز لهستان با ۹۰ تن و چین با ۶۰ تن بزرگ‌ترین خریداران طلا بوده‌اند.
🔹
این خریدها صرفاً برای سود کوتاه‌مدت نیست؛ بانک‌های مرکزی با افزایش ذخایر طلا به دنبال کاهش وابستگی به دلار، تنوع‌بخشی به ذخایر و مقابله با ریسک‌های ژئوپلیتیک هستند. کارشناسان می‌گویند این خریدها می‌تواند سوخت جهش قیمت باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/695545" target="_blank">📅 17:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695541">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDKqMdaJ1QngIhQkyewTZ-kVqdFa1SnRc8J4SgsNH3JASqYjbgGIL2AwVq3Nhb6gOEWMTs70Mc7-yeTK1EaHmKvZUPOtC_RyKv0RqTLD3TFKOxngA4gkSPo3wv3YLLmeufmBNtpZBllR9ZEPG4oaptVTIuw4-p8hfu_F4PwLsxOGAaLq2qsVZTgEMYM2kJANQL1VmFqaDyuMHf2_5nRhGvW44RXrGYtUq6WcqdHjcnLpYKbANQOLBpm-QZ819sHr3EZxox2UwX2UkgKSJ81Km95F4T8AyRmipLGIgEYgdfRxYtzXxe0fnkW9xyShhP4mVMCPUJ3t1aMC-LTmgmm0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دمپایی جدیدی که در مدت کوتاهی مورد توجه بازار قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/695541" target="_blank">📅 17:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695540">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
وزیر نیرو: افزایش قیمت برق در دستور کار نیست/ برای پرمصرف‌ها جریمه خواهیم داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/695540" target="_blank">📅 17:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695539">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه درباره افزایش احتمالی حقوق کارمندان: افزایش حقوق‌ها فقط در بودجه اعمال می‌شود؛ بودجه آذر ماه به مجلس تقدیم می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/695539" target="_blank">📅 17:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695538">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c847298983.mp4?token=O5JL49CuipboPLn5YiC4j9qgFTDn7IA3OOwBR-uB1gfU-jpq3JBZu0sj9_ZA_0Lnv0fTFonPDXj0GpmORFx-5iVauiL9f-0k0IKSnArxU-NOBVWWLw-PYWG1-LwvZR6gb_0CreT8e-dOKl62MyRTl65td0Txyx6r4htxSa7TXbi9sVt5aNSnIeGwd-yPS-YXloXiXbpt0iCVMdXgSBtCAgN5s0SwMsdmvi2oCizkiqM4DPH-To6A8Lu7hVE5LJAQbetIJsurShxPs1WrjhYTbpeBX8ySD5EI1XKgqd0zygzF5azHp3v2kET3yL0Dq1_wyFtQepD2pyj6bvVmr2RXtWFYwnHwYWrRsA4OvoDX2KgaTWzmgxLym9H_qbJzoiK783aJypnDY0S4eTy_nQcDCi59-mnzzgnhfadd5S5bEYAUXBfpY347Nnz0jthjBkoy02JFHEfFVus3uVa6yToDWqtRHYYyvX6E3G1BVNjhi1uqGoL3ViKDNnAW8ioGfdcL9oWhLS243OnkIu1MZJer-SGDsKWMBtxKtK7ttdzRJIsmfMslHnJegR8EMzSitbDIaAWQWyGdgyNMQ9gExC7MRdnc8-E8NDcmR-VhekdPASP_NikP1fAXnRO3pDAvbTQFNLdwnx4z1wTvJyP3IFm8vCyybidG6LPLej5ekr4Q9tM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c847298983.mp4?token=O5JL49CuipboPLn5YiC4j9qgFTDn7IA3OOwBR-uB1gfU-jpq3JBZu0sj9_ZA_0Lnv0fTFonPDXj0GpmORFx-5iVauiL9f-0k0IKSnArxU-NOBVWWLw-PYWG1-LwvZR6gb_0CreT8e-dOKl62MyRTl65td0Txyx6r4htxSa7TXbi9sVt5aNSnIeGwd-yPS-YXloXiXbpt0iCVMdXgSBtCAgN5s0SwMsdmvi2oCizkiqM4DPH-To6A8Lu7hVE5LJAQbetIJsurShxPs1WrjhYTbpeBX8ySD5EI1XKgqd0zygzF5azHp3v2kET3yL0Dq1_wyFtQepD2pyj6bvVmr2RXtWFYwnHwYWrRsA4OvoDX2KgaTWzmgxLym9H_qbJzoiK783aJypnDY0S4eTy_nQcDCi59-mnzzgnhfadd5S5bEYAUXBfpY347Nnz0jthjBkoy02JFHEfFVus3uVa6yToDWqtRHYYyvX6E3G1BVNjhi1uqGoL3ViKDNnAW8ioGfdcL9oWhLS243OnkIu1MZJer-SGDsKWMBtxKtK7ttdzRJIsmfMslHnJegR8EMzSitbDIaAWQWyGdgyNMQ9gExC7MRdnc8-E8NDcmR-VhekdPASP_NikP1fAXnRO3pDAvbTQFNLdwnx4z1wTvJyP3IFm8vCyybidG6LPLej5ekr4Q9tM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بانک مرکزی مدیریتی بر ذخایر ارزی ندارد؛ فقط به دنبال ورود منابع نفتی هستیم
پیمان فلسفی نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
نظام و بانک مرکزی باید بتواند مدیریت خود را بر ارز و ذخایر ارزی اعمال کند، اما الان اعمال نمی‌کند و فقط نشستیم و شاهد افزایش قیمت ارز هستیم.
🔹
می‌دانم رانت‌خوارها، فرصت‌طلبان و کسانی که تا گذشته منافعی داشتند، قطعا صدایشان در خواهدآمد؛ باید دست اینها را کوتاه کرد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/695538" target="_blank">📅 17:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695537">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83703e962b.mp4?token=icV3fjeGy2Fj__Q-A8QFGkaHlhwaRvAMURK9Uz73OGk-0o9nrdwoX34jcWUJ96Ah8-9swXFkE7_UHNfEQhS753r-zACGGHhZl2Oe_JFXp7ZKUwHsKTj-eZ42Xyu7-SmFBxNVMoUkzgYtGoxnTl6mOZTHap04rz21rt9wLyYHg5hzSKsO6TLbdJrn1hcaC3vhuulwsDsxaocjD2j3W8LYf40Rw5r33FGgFbw4jWEk-ucn5vySkl0H6K9faxIbvQ1b8RPrMdVeRB-O_McGpJA21bDHNKovJVAe1YTBZyzm0UDQo847V1KLvgfimBlAFWN47Sjed1TEndsoSmbHCxqo7pa6S-pJyOFXfX5tcJUAB6vGx-p09un8lKQYfI1dKEcnAITuK40UKA6Pf-6GVdy8z0nzeyqjDb2X-i9sMdLa71AabFobbd5aSr5klSiRJA5UbGQh46XoX4bC50FyGnOipCB2OGdIPZK4Ivr_4M40eOMEq596HBYWwAmbwSsd4Flnw7w2bv7iervwSr_t6AQ9vbx-4qkhTGsxX3iqEUx0-4GZpmAIuin5OQ3tN4kWIiHDNTRq_gAm_mF1kaUHT39f7MH-fy9EaCY-Ys7z5OTbrypVz7meHs-z1pED9n2KoqrQOfGNv6kLhYLyubvA9BvRewhP8y5i75xE3Q9JJQOgynU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83703e962b.mp4?token=icV3fjeGy2Fj__Q-A8QFGkaHlhwaRvAMURK9Uz73OGk-0o9nrdwoX34jcWUJ96Ah8-9swXFkE7_UHNfEQhS753r-zACGGHhZl2Oe_JFXp7ZKUwHsKTj-eZ42Xyu7-SmFBxNVMoUkzgYtGoxnTl6mOZTHap04rz21rt9wLyYHg5hzSKsO6TLbdJrn1hcaC3vhuulwsDsxaocjD2j3W8LYf40Rw5r33FGgFbw4jWEk-ucn5vySkl0H6K9faxIbvQ1b8RPrMdVeRB-O_McGpJA21bDHNKovJVAe1YTBZyzm0UDQo847V1KLvgfimBlAFWN47Sjed1TEndsoSmbHCxqo7pa6S-pJyOFXfX5tcJUAB6vGx-p09un8lKQYfI1dKEcnAITuK40UKA6Pf-6GVdy8z0nzeyqjDb2X-i9sMdLa71AabFobbd5aSr5klSiRJA5UbGQh46XoX4bC50FyGnOipCB2OGdIPZK4Ivr_4M40eOMEq596HBYWwAmbwSsd4Flnw7w2bv7iervwSr_t6AQ9vbx-4qkhTGsxX3iqEUx0-4GZpmAIuin5OQ3tN4kWIiHDNTRq_gAm_mF1kaUHT39f7MH-fy9EaCY-Ys7z5OTbrypVz7meHs-z1pED9n2KoqrQOfGNv6kLhYLyubvA9BvRewhP8y5i75xE3Q9JJQOgynU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید سرکه سیب رو از زبون خودش بشنوین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/695537" target="_blank">📅 17:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695536">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
وزیر تعاون، کار و رفاه اجتماعی: تلاش می‌کنیم افزایش کالابرگ اقشار هدف از ۱۵ مهر آغاز شود
🔹
میزان افزایش اعتبار کالابرگ احتمالا ۵۰ درصد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/695536" target="_blank">📅 17:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695535">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/661232901a.mp4?token=PcstZgX30eIb72hRnY7XyMKpsSMHNDe-OHuO-0xZ9C0jzF9x8VMA9UFG2JJuzoekx4ROqAomUpcv3IHIHyTo74rbXrugqrvDvh-ecH4oU5AttPg5RngK2q2v9jF4gDZicdQppP6rKKI9n5AyFG5HHFOh2Elx3x1XVIT6D3_0jsZNYW37Q78Z1auC2Tu86t-ctcPn8y_9KILFq9P5H4UEnLX1zmClX4i8RZxXycYKwwQH36uOZtRaZptptWgUWM4gUR8OmlwpR0Kzf2ZqhcTg_ExJsF0u97d4dZ8x5Dvan1mkYlqEo2vyzt0c3Che3vbYZMd_sLClTWr9WvZB9FWfyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/661232901a.mp4?token=PcstZgX30eIb72hRnY7XyMKpsSMHNDe-OHuO-0xZ9C0jzF9x8VMA9UFG2JJuzoekx4ROqAomUpcv3IHIHyTo74rbXrugqrvDvh-ecH4oU5AttPg5RngK2q2v9jF4gDZicdQppP6rKKI9n5AyFG5HHFOh2Elx3x1XVIT6D3_0jsZNYW37Q78Z1auC2Tu86t-ctcPn8y_9KILFq9P5H4UEnLX1zmClX4i8RZxXycYKwwQH36uOZtRaZptptWgUWM4gUR8OmlwpR0Kzf2ZqhcTg_ExJsF0u97d4dZ8x5Dvan1mkYlqEo2vyzt0c3Che3vbYZMd_sLClTWr9WvZB9FWfyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات‌ها در کره‌جنوبی جای نیروی انسانی را گرفتند؛ این‌بار یک ربات به‌عنوان کارمند در دانشگاه مشغول به کار شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/695535" target="_blank">📅 17:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695534">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
زاکانی: برای ساخت پارکینگ پناهگاه‌ها در حال اقدام هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/695534" target="_blank">📅 17:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695533">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ورود تراستی‌ها به واردات کالاهای اساسی؛ ارز به کشور بازنگشت
پیمان فلسفی، نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
برخی از تراستی‌ها وارد فضای واردات کالاهای اساسی شده‌اند.
🔹
قاعدتاً باید در تامین ارز ورود کنند چون ارز در اختیار آنها است.
🔹
تراستی‌ها جواب اعتماد ما را درست ندادند وگرنه این همه ارزی که قرار بود به کشور باز می‌گشت.
🔹
دولت، حاکمیت خود را اعمال نکرد و این شرکت‌ها را ایجاد و اعتماد کرد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/695533" target="_blank">📅 17:15 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
