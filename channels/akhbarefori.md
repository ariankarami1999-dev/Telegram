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
<img src="https://cdn4.telesco.pe/file/ODSb7qYGPBSP8CPij_bTJauttfoMmkYDajAkfCyexnIg6cXBE-3-SKgtMVwmtq6QYOj8DuOGWRyPrHREQQwXk5d8zT0StXV2y2NLf6nXKmHVZ8JIq7_KIS2U5AalaerSoht-r9jL8SuhGdP6Kp_FMDZKzpebEHWE3bs5TWLd-WY_pH4suARqj3cfLuWjzTTcc0HV3OR_TkqZ_KnC88byIsmhxUUKqYtoZYLj7rYlaCE_AFqPqmclqj0_srzQCK0lg8_jkLgq_eWl_e3waIbz_4kW9wg4oMz0lWSnbZb-e7KblN82BmO5oOVF0YlIbI2dormFLM52d3U70TsjZfq5Lw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.09M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 16:27:18</div>
<hr>

<div class="tg-post" id="msg-655026">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuVM1fE9Ze7M2rAiw7fdYyoq99ZMugmk-zKARCRqA4WyehRDd2v-N4ewxe-5vHi17cgZUGjQwqasMFmmqtVMnevhgS-1ZOK_n877mQ5OFJl6QUDeRRTAQFlo4IZqxv6z8PuW51DDQvIYjGw9j0XU3Kvh6xd2kcX-j5BCTvo__y8utjDMIVc6B35w8LxBU6LmG9UET-Nxb2SdOQMXzgUOqOc_5il4eAIr44K3rYkdFAuYbbOdM5OLVV1D-c3PluX7_tcT0zCLYxO45pPHyq397sXAuenlV5WQH9GlWWrVo6MKejmJe7usntJo6U6CMlCGQOXmxTDnz3S716K9uSoe6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با این پرامپت گزارش ارزیابی زیبایی‌شناسی چهره‌ات را دریافت کن
Create a clean, minimal, high-end facial aesthetic report based on the uploaded photo, using a black-on-white editorial design with thin linework, rounded cards, generous spacing, modern typography, and a refined luxury feel. Include an isolated front-facing image of the face, presented as an analytical attractiveness-assessment diagram. Provide an honest, objective evaluation of facial attractiveness potential, avoiding excessive flattery and focusing on symmetry, facial thirds, overall proportions, eye spacing and shape, nose harmony, lip proportions, jawline, chin, cheekbone structure, skin texture and tone, hairline, hairstyle, grooming, overall facial harmony, and photogenic potential. Assign clear, realistic scores to each major category, along with one overall attractiveness-potential score, keeping the ratings grounded, useful, and not artificially inflated. Include practical, achievable recommendations to improve attractiveness-potential, covering grooming, haircut, facial hair, skincare, eyebrow shaping, posture, weight loss, minor aesthetic procedures, styling, and photo presentation. Maintain a refined, direct, constructive tone that feels elegant, credible, and easy to understand, with an emphasis on actionable improvement that build on the subject's existing strengths.
All visible text in the final report must be written in fluent Persian, with correct right-to-left layout, accurate Persian typography, clean spacing, and no English text anywhere.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/655026" target="_blank">📅 16:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655025">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcee3d1a93.mp4?token=F8u5Q9hTGAVc1EZ7-r5DVk8mUVgohJgqsqVnATKpdTv25hncAhX2oCyBpNxmQaYxICVyDjiTGWtJ2bvOoZai5MIeb7eBnMXtFp9v_viUtAw3GxVZwXgfmo4CPqUbkT3zb_Kp4SXOxSWB4ECb_YZxgHM3eIW1qVrYHgN55FFHCffCn4Bv39gxdzzXVwq4x7jLuaYOvFgdTk--lTnEah-v7P8p87ivL2gUjYe2ooI0BS2RgCd8Rm388f5aORlcEyCdeO-WBc53BEz2eeP9g4XVsAAESdGsXtDUKotJvQPj8w8ANg3r_X__zBw5Z4W5VEDWkCyARw_Poa9mMJ_91Ed-6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcee3d1a93.mp4?token=F8u5Q9hTGAVc1EZ7-r5DVk8mUVgohJgqsqVnATKpdTv25hncAhX2oCyBpNxmQaYxICVyDjiTGWtJ2bvOoZai5MIeb7eBnMXtFp9v_viUtAw3GxVZwXgfmo4CPqUbkT3zb_Kp4SXOxSWB4ECb_YZxgHM3eIW1qVrYHgN55FFHCffCn4Bv39gxdzzXVwq4x7jLuaYOvFgdTk--lTnEah-v7P8p87ivL2gUjYe2ooI0BS2RgCd8Rm388f5aORlcEyCdeO-WBc53BEz2eeP9g4XVsAAESdGsXtDUKotJvQPj8w8ANg3r_X__zBw5Z4W5VEDWkCyARw_Poa9mMJ_91Ed-6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوق یک پسر بچه بعد از وصل شدن اینترنت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/akhbarefori/655025" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655024">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ترامپ شرایط سخت‌تری را برای چارچوب صلح به ایران ارسال کرده است
نیویورک‌تایمز مدعی شد:
🔹
ترامپ عناصری از پیش‌نویس توافق را اصلاح کرده و آن را برای بررسی به تهران بازگردانده است.
🔹
او نگران بخش‌هایی از توافق احتمالی است که شامل آزادسازی دارایی‌های مسدود شده برای ایرانیان می‌شود.
🔹
ترامپ از مدت زمانی که طول کشیده تا ایران به پیشنهادات واشنگتن پاسخ دهد، ناامید شده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/akhbarefori/655024" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655023">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاونت راهبردی رئیس جمهور: ۷۰٪ شرکت‌کنندگان در تجمعات شبانه زنان هستند
🔹
سی‌ان‌ان: ایران ۵۰ ورودی از ۶۹ ورودی تونل‌های تاسیسات هدف قرارگرفته موشکی را باز کرده است
🔹
ادعای نتانیاهو: من به ارتش اسرائیل دستور دادم تا دامنه عملیات در لبنان را گسترش دهد
🔹
وزیر‌خارجه فرانسه: بازگشایی تنگه هرمز اولویت است تا بیش از این هزینه جنگی غیرمرتبط را نپردازیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/655023" target="_blank">📅 15:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655022">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ناتو: ممکن است در موضوع بازگشایی تنگه هرمز مداخله کنیم
رئیس کمیته نظامی ناتو:
🔹
کشورهای عضو ناتو در حال نزدیک کردن نیروهای خود در خلیج فارس هستند و در صورت فراهم شدن شرایط در مساله تنگه هرمز مداخله خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/655022" target="_blank">📅 15:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655021">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHggPFi59qF-Fa4lAAqzdUzGeMJ3EZ7_ZsCyD6ShPZmmrDW6d5Jf1EyCruINh4ftNOp6Rqj9mljVpqHTEsJqyNgbfbJc4vEQBmCmhudChCs2qoJNgwjiUj7X0U9Yyk4nVihZexrnvkoA4K-tNJdjFW3zZliJV70ii_tSo9MOoUbWqFuHzOn4WIfXlvZLN5Gy2hZAkdHj0L0VQKe0y6CGR2O6logVG3fRQFb7lV5M4Nu6cM4Whaq_4nnqFLzMkaym6o3THmGFLiOkAOkpmiSP7c2OkzEyYUKBUYXCkULDrkYVm6OBN7wfoLgVbUgKCfdSBhhbXQ4yML6R_FB-RxSatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس وایرال شده از استایل جدید صابر ابر در یک نمایشگاه هنری سوژه رسانه‌ها شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/655021" target="_blank">📅 15:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655020">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
گردش مالی نیم میلیارد دلاری کنسرت کانیه وست در استانبول
🔹
کنسرت کانیه وست در استانبول با حضور ۱۱۸ هزار نفر رکوردشکنی کرد. در صورت فرض حضور ۱۰۰ هزار گردشگر خارجی در این مراسم و میانگین هزینه ۵ هزار دلار برای هر نفر، این کنسرت می‌تواند حدود نیم میلیارد دلار گردش مالی ایجاد کرده باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/655020" target="_blank">📅 15:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655019">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
قتل پدر توسط پسر نوجوان به خاطر بیکاری
🔹
مشاجره یک خانواده ارمنی در محله مجیدیه تهران به جنایت انجامید. پسر نوجوان پس از درگیری لفظی بر سر بیکاری و عدم توانایی در پیدا کردن شغل، با چند ضربه چاقو پدر سالخورده خود را به قتل رساند. متهم دستگیر شده و به جرم خود اعتراف کرده است. پرونده برای بررسی جزئیات بیشتر در دست تحقیق است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/655019" target="_blank">📅 15:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655018">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای فاکس‌نیوز درباره آخرین وضعیت مذاکرات ایران و آمریکا
فاکس‌نیوز مدعی شد:
🔹
بنابر گزارشات جدید، ترامپ شرایط توافق با ایران را سخت‌تر کرده و شروط جدیدی در موضوعات هسته‌ای و تنگه هرمز اضافه کرده است.
🔹
پاسخ تهران ممکن است چند روز طول بکشد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/655018" target="_blank">📅 15:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655017">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7106a3dc12.mp4?token=AZqffglLuC4q1EpLsUBcpXhuKA54C4wQZ7sMWuVl5PUqHTqqmGLFsLFJ6N9m52GAXKboBkozW5vzURF81IdtncfToY_3zHdm7AL_xjSbyAKPrgqs_mP_lCJQVpkl8K2Aneu3QpUGUdC9kgg1vjQymgU0L-ABUj0EoCU8mTQeDfUOITlTkcH6Tql37u7IDo32fKdyNT_7ObsW1ScaVqa_V6_wE9ujWLOfbQt8oIkzsvY89oudWO-H0VR3WtbXszpRUr-fPEIx344UxvgEihTT3eR_KwULJ6CEWs8R2PZQ6jbPzVsxv1WqdZi88VRbIw-78hk6A7fCQmpk20OWhDKLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7106a3dc12.mp4?token=AZqffglLuC4q1EpLsUBcpXhuKA54C4wQZ7sMWuVl5PUqHTqqmGLFsLFJ6N9m52GAXKboBkozW5vzURF81IdtncfToY_3zHdm7AL_xjSbyAKPrgqs_mP_lCJQVpkl8K2Aneu3QpUGUdC9kgg1vjQymgU0L-ABUj0EoCU8mTQeDfUOITlTkcH6Tql37u7IDo32fKdyNT_7ObsW1ScaVqa_V6_wE9ujWLOfbQt8oIkzsvY89oudWO-H0VR3WtbXszpRUr-fPEIx344UxvgEihTT3eR_KwULJ6CEWs8R2PZQ6jbPzVsxv1WqdZi88VRbIw-78hk6A7fCQmpk20OWhDKLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم امیرالمومنین(ع) مهیای عید غدیر می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/655017" target="_blank">📅 15:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655016">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
تمدید تردد خودروهای پلاک مناطق آزاد در سراسر کشور
رئیس پلیس راهور:
🔹
خودروهای دارای پلاک مناطق آزاد (ماکو، کیش، قشم، چابهار و اروند) که پیش‌تر در شرایط خاص عملیاتی بودند، تا زمان عادی‌سازی کامل شرایط کشور می‌توانند بدون نیاز به تعویض پلاک و در قالب «گذر موقت» در سراسر کشور تردد کنند.
🔹
این خودروها همچنان ملزم به رعایت قوانین راهنمایی و رانندگی هستند و در صورت تخلف یا تصادف، مشمول جریمه و مسئولیت‌های قانونی خواهند بود./ فارس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/655016" target="_blank">📅 14:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655015">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 آیا شما از دخانیات (سیگار، قلیان، ویپ و...) استفاده می‌کنید؛ چگونه و به چه مقدار؟</h4>
<ul>
<li>✓ بله، به صورت مستمر و روزانه</li>
<li>✓ بله، به صورت تفننی و صرفاً در شرایط یا جمع‌های خاص</li>
<li>✓ در گذشته بله، اما در حال حاضر استفاده نمی‌کنم</li>
<li>✓ خیر؛ تا بحال هیچگونه مصرف دخانیات نداشته‌ام</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/655015" target="_blank">📅 14:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655014">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
توافق نهایی هنوز حاصل نشده و امکان منتفی شدن آن همچنان وجود دارد
تسنیم:
🔹
تبادل پیام‌ها میان ایران و آمریکا درباره متن تفاهم‌نامه احتمالی همچنان ادامه دارد و دو طرف به صورت متناوب اصلاحیه‌هایی را مطرح می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/655014" target="_blank">📅 14:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655012">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNGg8obo3mWw3sM-wJuJoWLbdMncSFvjhiCQVklhBmsQ8meC1WHOKE9kSg7BFONbzw3uv0AIhTcWuvVgkE2q0QYvOXbQkP7UxN8E3LXtGqfLY5HEE1Ob0thVxTvNyzg2pDY8aw-1GhFRVpWJ6N3uJubo4coHv3B0PnbTHbK0BY1mz04YKLR1dkBG8FZL2XwyCx64DBz5TDsbnet4lVlkJK-K2gBlsYVsNA_CLqthIR8TrumMoqWJYnfZrcsLhS7t5WZOLP-SqE3xFb3GKInwyooYZrXX8FjcKzLlm1O2aDZ2mHnGiIh5fMRGCL2SSkA6BymSC-5IZhp88CL5ykEFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6YJQNLvqoesdyccqqXUq2CddbVKQPj6eI2yKe--RHa07X2lOprt8JPx-dZ9cjcdEXVajVo7VcNvW97HfV7BN5QGKnqtD708cuJ3HOCqnwy8gdq2Z1GgB1rQLN-JkRS0zsUe6XA2_ha3GF8l7199mXo2-be5UcDHew-MPcAGaSmlSlAytKU_7uiNw5AYfV3Mz5i8o_rEw7lYvzXpImHXH1S2XC5uuoYfLfx9dzqyJrmSWNbgoxAefXnJoFkLEGG4BE0szqI9t-N4NkFi-fFObt4PCjoaO0DwCSwJ_qVE3zE0S8TCn2SA4wa0qCUDalj_VjPb8rXaB4_4wZ5VkRrNRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قالیکوه، الیگودرز زیبا
🇮🇷
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/655012" target="_blank">📅 14:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655011">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsdwggwXwfKVS4_K4okOPGZSIEnZueZP4VSdll8OKruupv602Ass9Al7GBVs_eO-NfPDOGqXwaJrYEENndEcXqyQ9Vsyt1l3EnWp6UMpJe0yh3uUTY_pwQ8lbYKQy4DQ6Ffd3UDjbOtAJm48tZQUdxY7Yf28QHf5rNXKVnoHKSnbOruGlTrXMKY9CAkfs-AMcdWyJluv3pDUpUXnD-xALI4cHnCt4Q8ajtpJn_W40Mx6lsnPrqJEs1Kov09_-puyQbMqfA5K_h3ai3TLev1Er2-fKCWXsA9Q3exo14mM67IjiCaPpCtnrEZrfrBIdW1ITqiPejQFB9gjYezRBOD2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیما، پیشران بانكداری دیجیتال/ بیش از یك میلیون فقره تسهیلات از طریق سكوی دیجیتال بانك ملت پرداخت شد
🔹
در کمتر از ۸ ماه پس از آغاز به کار دیما به عنوان سکوی بانکداری دیجیتال بانک ملت، تعداد تسهیلات خرد اعطایی از طریق این سکو به صورت کاملا غیرحضوری، با ثبت یک رکورد جدید از مرز یک میلیون فقره عبور کرد.
🔹
دیما که از مهرماه سال گذشته در دسترس مشتریان بانک ملت قرار گرفته است، امروز با بیش از دو میلیون و ۵۰۰ هزار کاربر، به یکی از موفق‌ترین نمونه‌های تحول دیجیتال در نظام بانکی کشور تبدیل شده و نقش مهمی در توسعه خدمات غیرحضوری بانک ملت ایفا می‌کند.
🔹
بر اساس آمارهای ثبت‌شده تاکنون، تعداد تسهیلات اعطایی از طریق دیما به بیش از یک میلیون فقره رسیده که این تسهیلات شامل طیف متنوعی از محصولات اعتباری و تأمین مالی خرد از جمله تسهیلات پلکانی (میکرولون)، تسهیلات مبتنی بر سپرده‌گذاری (نیک‌وام)، تسهیلات سازمانی(فرهنگ وام)، تسهیلات ویژه کادر درمان، تسهیلات حمایتی حفظ اشتغال بنگاه‌های تک‌نفره و اعتبار خرید «دیماپی» است که تمامی مراحل به‌صورت کاملاً غیرحضوری انجام می‌شود.
لینک عضویت در دیما</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/655011" target="_blank">📅 14:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655010">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32db4f3eed.mp4?token=vnSdepNxX707PdZnzJ17LkZbSVffg2GkWt3IWT250Ry6LaF1P6l9FKhqczbFWNHiHczMy3wj7IQYT0obkW38sbFkcCNV9vM0OtmgzNzpkEaisSk0Uz41A15f0VNsgKlliQMBzo1JXu6fE4oOJlInkxyo4oObdwpMlzfDDdKk97etTlSW3xLoree2R-m5_f_ROWqdVXSES-79qujpRxmyYyLV69W7jdWsP00cbRIvo7WbQz3NPrtOBQs_b_anjDik0V6BUyoqKiZwgamRCtsabh9gw3_bj-ftQ2mEbkfj24k6zZVudn_2WciNtgThb_psZTVUZ0Ifl9lc3DtsZ2hWNZV5CFDr_eW0kcvsdY7QGFiQ85-qYcb5O_hutldxritwsdPKGM24MWMiydWmWRQGmdmzB7M9Cvn8sWt1g0HkjQ1CXUEnQXooMSVJzD7GnDc93lVkf5HG8yOgiD_NyGtQxZEW5bj66HIItp0fxOgK2KtTie9tPGxSDO4LOQk3tZ2o-vxhz_Sj_pSoIu3OYWhOZIOQLeWWYsNaiS3BrnkQP5OVzfFK39xHPIqd8dv0PzhIqSuO1SY2i3_9L8IcQJyE3zCC2CzoDwexGVkEgAWrx-olBZUanfifp2tyzmvmQBJoje5S9fJ0nd5oxUrorCix7snrzxWPtYotM3rAi1OF4ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32db4f3eed.mp4?token=vnSdepNxX707PdZnzJ17LkZbSVffg2GkWt3IWT250Ry6LaF1P6l9FKhqczbFWNHiHczMy3wj7IQYT0obkW38sbFkcCNV9vM0OtmgzNzpkEaisSk0Uz41A15f0VNsgKlliQMBzo1JXu6fE4oOJlInkxyo4oObdwpMlzfDDdKk97etTlSW3xLoree2R-m5_f_ROWqdVXSES-79qujpRxmyYyLV69W7jdWsP00cbRIvo7WbQz3NPrtOBQs_b_anjDik0V6BUyoqKiZwgamRCtsabh9gw3_bj-ftQ2mEbkfj24k6zZVudn_2WciNtgThb_psZTVUZ0Ifl9lc3DtsZ2hWNZV5CFDr_eW0kcvsdY7QGFiQ85-qYcb5O_hutldxritwsdPKGM24MWMiydWmWRQGmdmzB7M9Cvn8sWt1g0HkjQ1CXUEnQXooMSVJzD7GnDc93lVkf5HG8yOgiD_NyGtQxZEW5bj66HIItp0fxOgK2KtTie9tPGxSDO4LOQk3tZ2o-vxhz_Sj_pSoIu3OYWhOZIOQLeWWYsNaiS3BrnkQP5OVzfFK39xHPIqd8dv0PzhIqSuO1SY2i3_9L8IcQJyE3zCC2CzoDwexGVkEgAWrx-olBZUanfifp2tyzmvmQBJoje5S9fJ0nd5oxUrorCix7snrzxWPtYotM3rAi1OF4ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو ناوگان صمود: در زمان بازداشت مورد تجاوز جنسی قرار گرفتم
جولیت لامونت، مستندساز استرالیایی و عضو ناوگان صمود:
🔹
در جریان توقیف و بازداشت توسط ارتش اسرائیل در ماه مه، وقتی دستبند و پابند داشته، داخل یک کانتینر تاریک توسط یک سرباز اسرائیلی مورد تجاوز جنسی قرار گرفته‌ام.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/655010" target="_blank">📅 14:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655009">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای آکسیوس: احتمال روشن شدن سرنوشت توافق ایران و آمریکا تا پایان هفته آینده
🔹
طبق گزارش آکسیوس، یک مقام ارشد در دولت دونالد ترامپ اعلام کرد که احتمال دارد تا پایان هفته آینده وضعیت توافق احتمالی میان آمریکا و ایران روشن شود و واشنگتن برای دریافت پاسخ تهران آماده صبر کردن است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/655009" target="_blank">📅 14:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655008">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در محدوده جزیره قشم
🔹
صدای یک انفجار در محدوده شهرستان قشم از سوی چندین منبع محلی گزارش شده است.
🔹
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/655008" target="_blank">📅 14:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655007">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
اسرائیل هیوم: آمریکا در حال بررسی سفر ترامپ به اسرائیل در ماه سپتامبر است
🔹
مقامات آگاه می‌گویند تا زمانی که جنگ با ایران ادامه دارد، این سفر مطرح نیست. مگر اینکه توافقی حاصل شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/655007" target="_blank">📅 14:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655006">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در محدوده جزیره قشم
🔹
صدای یک انفجار در محدوده شهرستان قشم از سوی چندین منبع محلی گزارش شده است.
🔹
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/655006" target="_blank">📅 14:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655005">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
وضعیت پاریس پس از جشن‌های قهرمانی PSG در لیگ قهرمانان اروپا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/655005" target="_blank">📅 14:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655004">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea2beb520.mp4?token=uXkyo4j0h5Df0CGwwAmpTcOli0KJaivjOR9OZHWLN2BaYEUmMp6tb8jIrjrcntlrNfiT3EWy80_oTtUjZ9YeH2ura44Fzhdb8eTKAOwcRHsLeWIZmfRhqVb_fME-bX3gSqvTD5AKGtgt6GaX4CEXWf3LpNNyt9PHvmmOGFtWS-5PycjuCtX-l0M8WLo_2Vo98jEcQ9BrUzfHibyuSQ8agUXBMijgq3IGA5N1VtP0BqPzmWphdg0VlM2S1ZSe-k_PlX2y0FCjYIjjr_tngoxIrHhGRUuuWJUfpDjj2Bjr4m78wfcMoMEjpT8au24niuGmyUGDHZL1I5Cn1-4ZFWT19ziZs52L5L0D5rbGsjXp-j5bKb_UzUAsc-YxVUj2wgpqIub2-80yNeAv6twR_0Q1Zt2un4ToFEg9H3zOTYG2iuRcnnB2kZu1oEqsZVGMnn7zL62uouOKegv-ZUqCqa70fc64MiCpBZ6yqG-n7h6K1Mtu-hj-27aQ-7PBU_cHXTjaPGVNK8rtB6P_zOd6xT5pSmeT3bGL1rmaFyDF1tVv2uHtKqhtq0yQx7aUsJKyNJQ77G3sqC1pbLbNxN65kwTS07jtnMiu6lanOeVtH1iDGaV8giLHjfVqvBIOyOyBVf5FkfPPZI7Imzm2EUg3-f0bmGvhZpfDevjIwlYXt7nuW4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea2beb520.mp4?token=uXkyo4j0h5Df0CGwwAmpTcOli0KJaivjOR9OZHWLN2BaYEUmMp6tb8jIrjrcntlrNfiT3EWy80_oTtUjZ9YeH2ura44Fzhdb8eTKAOwcRHsLeWIZmfRhqVb_fME-bX3gSqvTD5AKGtgt6GaX4CEXWf3LpNNyt9PHvmmOGFtWS-5PycjuCtX-l0M8WLo_2Vo98jEcQ9BrUzfHibyuSQ8agUXBMijgq3IGA5N1VtP0BqPzmWphdg0VlM2S1ZSe-k_PlX2y0FCjYIjjr_tngoxIrHhGRUuuWJUfpDjj2Bjr4m78wfcMoMEjpT8au24niuGmyUGDHZL1I5Cn1-4ZFWT19ziZs52L5L0D5rbGsjXp-j5bKb_UzUAsc-YxVUj2wgpqIub2-80yNeAv6twR_0Q1Zt2un4ToFEg9H3zOTYG2iuRcnnB2kZu1oEqsZVGMnn7zL62uouOKegv-ZUqCqa70fc64MiCpBZ6yqG-n7h6K1Mtu-hj-27aQ-7PBU_cHXTjaPGVNK8rtB6P_zOd6xT5pSmeT3bGL1rmaFyDF1tVv2uHtKqhtq0yQx7aUsJKyNJQ77G3sqC1pbLbNxN65kwTS07jtnMiu6lanOeVtH1iDGaV8giLHjfVqvBIOyOyBVf5FkfPPZI7Imzm2EUg3-f0bmGvhZpfDevjIwlYXt7nuW4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت سوم، فصل چهارم
🔹
میثم نثاری تجربه‌ای نزدیک به مرگ را روایت می‌کند که در آن با حال‌وهوایی معنوی و عاطفی روبه‌رو می‌شود. محور اصلی این تجربه، توجه ویژه به مفهوم پدر و جایگاه پررنگ او در لحظات بحرانی و معنوی زندگی است.
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: میثم نثاری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655004" target="_blank">📅 14:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655003">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3974d5e6b9.mp4?token=FvZR5hwZA_fEP9Ouni3h9WrMGScbWApEGpOolhRr9QNP5hm2u2nS0lrSWLYPupcR0zE4rjVPTWZhFoG_F4r3SNZtL4u2yceOoVsahYYoDwGxEOrtbvGkc772uoclXQD4Ndb4mxe0lHjh4DxocoCK-a7VnjFZap5nFse0NFlTcGxHBt7RU4tDE5E1q8dAEli-PUlbdCQm1cu0FLVVCX4z8ldsE6zackJDCd_2UmVmgEsbYq8K3KqQZZJYCs6EP2BCiFBA5HCzh1-TnWaVOoSNsrNQoDbwtpNqAfAijbLN14kzr-TdOKblQhhbZNxdxJ7ZmAEpPQ7aB97DZu7QSr8MiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3974d5e6b9.mp4?token=FvZR5hwZA_fEP9Ouni3h9WrMGScbWApEGpOolhRr9QNP5hm2u2nS0lrSWLYPupcR0zE4rjVPTWZhFoG_F4r3SNZtL4u2yceOoVsahYYoDwGxEOrtbvGkc772uoclXQD4Ndb4mxe0lHjh4DxocoCK-a7VnjFZap5nFse0NFlTcGxHBt7RU4tDE5E1q8dAEli-PUlbdCQm1cu0FLVVCX4z8ldsE6zackJDCd_2UmVmgEsbYq8K3KqQZZJYCs6EP2BCiFBA5HCzh1-TnWaVOoSNsrNQoDbwtpNqAfAijbLN14kzr-TdOKblQhhbZNxdxJ7ZmAEpPQ7aB97DZu7QSr8MiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ما ارتش ایران رو تقریباً دست‌نخورده گذاشتیم؛ خیلی‌ها از شنیدن این موضوع تعجب می‌کنن!
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/655003" target="_blank">📅 14:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655002">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58003f3547.mp4?token=E4TEzg7ky5HBYZ-LcAcGhAIYak-u8hH4yqCJWJBEok6-niZlNNXpqAXRuLHQhM-WzSse8tEg-r64CvTf2XB0hlW1ps36_qGDURgY7eto06KSVAXX_GL42Y49u2PS4TO_wXQg8rTHsyID2xVdwl_wEzfDhejKSGXoPe7e1RHyjmz6e-2TRZKKgZnnfVyT8H1HPlvd5LsMA2ikoDKqSa_EI662T0Jsh4W2Sl52uFKN9NsW8oLi0IzEQb0uR6ghH70BzcRvoh6UEtdq59_zQJns8ii7KgM3VHEPTwI6MYjG9D78CQD5zEuMO5kSDtD-88lxv700_vYMQyIrVbtCCxAaOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58003f3547.mp4?token=E4TEzg7ky5HBYZ-LcAcGhAIYak-u8hH4yqCJWJBEok6-niZlNNXpqAXRuLHQhM-WzSse8tEg-r64CvTf2XB0hlW1ps36_qGDURgY7eto06KSVAXX_GL42Y49u2PS4TO_wXQg8rTHsyID2xVdwl_wEzfDhejKSGXoPe7e1RHyjmz6e-2TRZKKgZnnfVyT8H1HPlvd5LsMA2ikoDKqSa_EI662T0Jsh4W2Sl52uFKN9NsW8oLi0IzEQb0uR6ghH70BzcRvoh6UEtdq59_zQJns8ii7KgM3VHEPTwI6MYjG9D78CQD5zEuMO5kSDtD-88lxv700_vYMQyIrVbtCCxAaOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگه‌ میلفورد ساوْند نیوزیلند در یک روز بارونی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/655002" target="_blank">📅 13:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655001">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vf1sVnkJ3XHUQB2wp6owt5EyRvJo7mCl41H6rm7yhs-wRjzlBzTDSG2LivfGa0oO8lDuCXCyV5CSrP8diQ0kN8enVd5556zZoK7fw3VSZffnkcigXC3gXHQ5hOmXhHuDtlsxT36if36Ms42cj9vfgBj8_sUkmPd5rN18OTi_i66Qwp6-Cvz7TujorWWGP7JzpBbM0rZNw7fckxLiH8Vx6f9EhpQvBiljqtZrF3PTj__whgF_93T2irArTp3V9Xcex5ReTNxBIhLTKW5fyegn2nj0d8D83_tPOxKg8YeNnViM3rrvDc44q2Mu3LDyzTPvrus5EY-L-V0VJDod9tR0pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۰ خرداد ۱۴۰۵؛ ساعت ۱۲:۳۰
🔹
دلار تحت‌تأثیر پالس‌های مذاکراتی در مدار نزولی قرار گرفته، اما بازار همچنان برای تعیین «کف قیمتی» دچار تردید است و معامله‌گران در موضع انتظارند.
🔹
در بازار طلا نیز هر گرم طلای ۱۸ عیار با قیمت ۱۷ میلیون و ۹۶۰ هزار تومان، در آستانه ورود به کانال ۱۸ میلیونی است؛ امروز سکه بهار آزادی با نرخ ۱۷۶ میلیون تومان معامله شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/655001" target="_blank">📅 13:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655000">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fdb5ba3d.mp4?token=BYBv3-MYJ5vllwwOPGUi1vhLwiua4etJQeL8SPYe8eX7IhNKQbMZ0tSlCGiebbdZq46MWDweaj2YaqLZhYE5PbYl17eg7MgPFPf6zIBfdMkPQ8sd66vfuRRofH0e_wehrnRsXP0A_deUgJj6adobLsdWtlFde6LLE3SYcJeourYJ8oqxU7TEr7U_ItDea-q85Hfa_eaorwg1rFz3vvlmVnOc-j8rL9EB9ESmi6Tccyl23JeRr3gaipvstldoPU-GQzCS3vZwhB117GxQZ5gJ6lQ5Lwl2OhC4-xCBVA3WsDuDXfRcWPTHKxmHGbiYM5fzXmNIsxYpbqztqeB4EPEsLkSK_6E2qGXwAb-UpFQs7Ttn1hHtmwP2f3DL7XhXURnQgwWknNG-PXJpA5WHrnV_1SV5npm4y3M2bEGmkHaNV7m23eKmZ0wLpeZTrZSaQfMkc7Os2Hu36Rd3A62jDFsPDADsqF0_XRe1bR8T8I1S7g7CUkNmP2Sd2uFifhO2iC-OB53xdkpWX6KVhYnnmr4R5POjaZ-BY-3Y1KWlPSikUnV5EX3h-7SsYhBMPFmtEHZgy2O2_xMGpvh0BfNCLRn0aOUbrBky_dN2vsUpYTgSSd41JRZQZqf8hIA1CK0pLear4qO07IL2RpzJRpfgUcT1PcNqXHqytHIl9-BeCTVfMx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fdb5ba3d.mp4?token=BYBv3-MYJ5vllwwOPGUi1vhLwiua4etJQeL8SPYe8eX7IhNKQbMZ0tSlCGiebbdZq46MWDweaj2YaqLZhYE5PbYl17eg7MgPFPf6zIBfdMkPQ8sd66vfuRRofH0e_wehrnRsXP0A_deUgJj6adobLsdWtlFde6LLE3SYcJeourYJ8oqxU7TEr7U_ItDea-q85Hfa_eaorwg1rFz3vvlmVnOc-j8rL9EB9ESmi6Tccyl23JeRr3gaipvstldoPU-GQzCS3vZwhB117GxQZ5gJ6lQ5Lwl2OhC4-xCBVA3WsDuDXfRcWPTHKxmHGbiYM5fzXmNIsxYpbqztqeB4EPEsLkSK_6E2qGXwAb-UpFQs7Ttn1hHtmwP2f3DL7XhXURnQgwWknNG-PXJpA5WHrnV_1SV5npm4y3M2bEGmkHaNV7m23eKmZ0wLpeZTrZSaQfMkc7Os2Hu36Rd3A62jDFsPDADsqF0_XRe1bR8T8I1S7g7CUkNmP2Sd2uFifhO2iC-OB53xdkpWX6KVhYnnmr4R5POjaZ-BY-3Y1KWlPSikUnV5EX3h-7SsYhBMPFmtEHZgy2O2_xMGpvh0BfNCLRn0aOUbrBky_dN2vsUpYTgSSd41JRZQZqf8hIA1CK0pLear4qO07IL2RpzJRpfgUcT1PcNqXHqytHIl9-BeCTVfMx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: اطمینان دارم که از این جنگ بزرگ با پیروزی خارج خواهیم شد
🔹
تا اطمینان پیدا نکنیم که حقوق ملت ایران را گرفته ایم، هیچ توافقی را تأیید نخواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/655000" target="_blank">📅 13:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654999">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWEHDTtcL7jCvQpccCH1M3Um1djkdCkfGFH6kQFXHdAlJuqSlGaAyXCEf-W1y-f0ZfMdaNVuQiq-diUxgk7TkNS0jKK2Wt5VdFS80oSL5liSQrqcd0b3unnZ9jYKAowbmHxHfJZr4bQf66ZzdZaSWGWVi9v4pf0LcvoTMg1vVFxUcVBefYcIzWZE7OXqtilNEDbekSi02i337IAoHh7YwPvNWb3sPnJ9QUlOn0UmtrJFkjReKLDMAAzKS-HuXouzi2aWJ5lOoxpCb_WlgSZmYQ45b9_NIebO8erHu-UaJW9EJ5FUEhCRWaVMtsPgYwjR4-Tc3TKCJ3Iv-eLrT7wGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی دولت: فعلا خبری از افزایش مبلغ کالابرگ نیست
مهاجرانی:
🔹
افزایش مبلغ کالابرگ از مطلوبات دولت است اما باید مطلوبات را با مقدورات هماهنگ کرد.
🔹
وقتی جریان عرضه و تقاضا دچار مشکل میشود بازار واکنش نشان میدهد.
🔹
نمیگوییم ورود محدود میشود اما دزدی دریایی آمریکا تاثیر میگذارد که ورود کمتر شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/654999" target="_blank">📅 13:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654998">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b0209531.mp4?token=XuuyUoRw3BXwm84yvJqvLN006WHMExy0F5JcaSMPZf6rvmItRohyTonCxvSBzAf45oDImcvd2QbjFWhlyuteV1g-Joh-U3zJrqfCHO2cvW2MSa6z4Jdd8btCLeeafSRMqU5yUOplGzR6cr-WQ2e1wneuVgT8UTiShA5-fH25I5-G88Ly9ZkToYtHhphGIBkqt3pxUwIVdV6Q0kjH2XrbaL_kin1UVZfubhS0uBs-4KFHwTWycDq0g1aCy4Qu1HaA4b6CctNKSKZGvSq8P1hMRjINrYM3_4cLc73WyiA_x2_pggIUd0lqND9zRVfQFaa55tVeCXfQvSftcKd0GaBlIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b0209531.mp4?token=XuuyUoRw3BXwm84yvJqvLN006WHMExy0F5JcaSMPZf6rvmItRohyTonCxvSBzAf45oDImcvd2QbjFWhlyuteV1g-Joh-U3zJrqfCHO2cvW2MSa6z4Jdd8btCLeeafSRMqU5yUOplGzR6cr-WQ2e1wneuVgT8UTiShA5-fH25I5-G88Ly9ZkToYtHhphGIBkqt3pxUwIVdV6Q0kjH2XrbaL_kin1UVZfubhS0uBs-4KFHwTWycDq0g1aCy4Qu1HaA4b6CctNKSKZGvSq8P1hMRjINrYM3_4cLc73WyiA_x2_pggIUd0lqND9zRVfQFaa55tVeCXfQvSftcKd0GaBlIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک بار اینطوری درستش کنید عاشق مزه‌اش میشین #آشپزی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/654998" target="_blank">📅 13:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654997">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5BadmHZnVt2CejXFasYym_CRO1B351Rt1r_UdLmSef4ll0Q8KObttSrLJaPzdzyf3qhkJ351xt-IHYCV8xQ3aTPitafQ9UsglZaUKcJHR88A2nVY_ZngutiF2ehW_bs7osXhlS8PNn8vwcLjUQXByg5RaHVYO2CO8A0iXIiFYNKK0maosk2tV91J5AWVRXiPMQnDnYVUc-27q9JxsHjlJtgJz72-d1V_pQ-Zymw1UWQP_p98mkcTaoFCJeCwlZEE-dFPdl1X5yx0lg15j-tQDV5jBMUjscIcyIf4KpZh0yHJh0A6f2tku6nwyJnNfW0Z-dJv_vaXJ_5zru_wA24og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۸۳ هزار واحدی شاخص بورس
🔹
شاخص کل بورس با رشد ۸۳ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۲۳۶ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/654997" target="_blank">📅 13:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654996">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
قالیباف: در حال عقب نشاندن دشمن در یک جنگ بزرگ و تاریخ‌ساز هستیم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/654996" target="_blank">📅 13:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654995">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899a9d430b.mp4?token=LU0ul4w3vBF0HK28gkPS_ze1uehvl36-Qzo4YoAomY1HShKmNOyAH__-fyrQ0OyC-zPQG1MmXQ1KrpSgZ_sh5sYcegxs-TotbaXokiniisnOgGeDTsop7-EXxJUE4qt-I96QWF0sTjVZHLm7gWrX2Wz-q-0gltqRRPB6umnDfRUk1iHkgNYSzdAQWHxYwEpr6jGFkA9nDu4NTZZeGG5ALnPKaUj21x7dfwzf87Dbajk1luH1vrgwxLoMJqcs_rfoCkhGKPA2dAc9mPUBAM8K4i420e_-N99qKMBgMMDJrGRnZwn3Sr657zAxzCz8rwHRe9rSvxi2iSNxcoIPsDmDcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899a9d430b.mp4?token=LU0ul4w3vBF0HK28gkPS_ze1uehvl36-Qzo4YoAomY1HShKmNOyAH__-fyrQ0OyC-zPQG1MmXQ1KrpSgZ_sh5sYcegxs-TotbaXokiniisnOgGeDTsop7-EXxJUE4qt-I96QWF0sTjVZHLm7gWrX2Wz-q-0gltqRRPB6umnDfRUk1iHkgNYSzdAQWHxYwEpr6jGFkA9nDu4NTZZeGG5ALnPKaUj21x7dfwzf87Dbajk1luH1vrgwxLoMJqcs_rfoCkhGKPA2dAc9mPUBAM8K4i420e_-N99qKMBgMMDJrGRnZwn3Sr657zAxzCz8rwHRe9rSvxi2iSNxcoIPsDmDcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: رهبر شهید جانفدای ایران شد
🔹
رهبر شهید، پایه‌گذار ایران قوی و مستقل شد. رهبر شهید به ما آموخت مقابل زورگویی با مشت‌های گره کرده تا آخرین قطرۀ‌ خون مبارزه کنیم.
🔹
رهبری که ما خود را جان‌فدایش می‌دانستیم، جانفدای ایران شد.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/654995" target="_blank">📅 13:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654994">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJc7EHgE4Q9PP15EC1Bf3PBlrzT3eBOwvs1cre-vnKF9qvXzutP55f1TyW5IEbOEB1zLvYw6qTe7zxIvR1Y7b1oyLHGHOIlP3ZkKaS1C_Nhq1F1Dno8XJtdn2uX2aEI2xs1yvFv0TgXZs0LcqSYpvMWYzDGBC20MD2hXY4P4oYXUnWOGo3_0dYfLiiZGSUWoQ7WELUOWjILt6smxR-m8Dz656lddlIashkzw4hZIiNfdT6CFlre4pnFokpWUsdrRK05z1zJkfmySloL-hHj7JRvpSEtmZueELz1fLuPjaA985Emrw5MJgKVrSl2w-eKYVvgCHTHmRau_VC3g0vWQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شوخی کاربران فضای مجازی با قهرمانی پیاپی پاری‌سن‌ژرمن و ناکامی امباپه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/654994" target="_blank">📅 13:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654993">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f30bf6366.mp4?token=YO0Wa2wxVpnuUzN2hyMfFaaptTQ9h2eAjpYjoyF_JIAy4cAZhndNNEDLnrBGDpGY0dK5_KfWYqlJ0dTnOna2ueg3Gp2LyO3sDTTo1avRKBQWBFu536G5CCp8pdciYQy1oZ9SMhHRlD3xsd4QxZChI0OFOujTU7niXyvwsqf6-CqhslFdFEgqvYxSpAuHGJzrowrWLZb9e2AligQ2mmlSugug8VZ4ycYpM0hIgQ74Fdi-CS5XH5Sd4KQrhDMZlVETt-CA00wSzHvQ7-mVxS5GACf7-ZOMMsRujEldl_uC-AyOJVmyQCjZ4dUzeMtyGfsfjdvf4DP0aZ-_zORkzdQVNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f30bf6366.mp4?token=YO0Wa2wxVpnuUzN2hyMfFaaptTQ9h2eAjpYjoyF_JIAy4cAZhndNNEDLnrBGDpGY0dK5_KfWYqlJ0dTnOna2ueg3Gp2LyO3sDTTo1avRKBQWBFu536G5CCp8pdciYQy1oZ9SMhHRlD3xsd4QxZChI0OFOujTU7niXyvwsqf6-CqhslFdFEgqvYxSpAuHGJzrowrWLZb9e2AligQ2mmlSugug8VZ4ycYpM0hIgQ74Fdi-CS5XH5Sd4KQrhDMZlVETt-CA00wSzHvQ7-mVxS5GACf7-ZOMMsRujEldl_uC-AyOJVmyQCjZ4dUzeMtyGfsfjdvf4DP0aZ-_zORkzdQVNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ما ارتش ایران رو تقریباً دست‌نخورده گذاشتیم؛ خیلی‌ها از شنیدن این موضوع تعجب می‌کنن!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/654993" target="_blank">📅 12:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654992">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c32975f3b2.mp4?token=JqU5OlSzBdxQhsOru6ump3VjiGbto6sKccvl_IWAZZTUwpqr72pc9JNcWMNCgG1CloDe9CVNtc-aZBJbTr0kNkiC0DcPvb4aSpqO8Ioe76AgOZFybWe6xFuwVMuYe0AwP4MVoIZNcbq2XRXFqDdJZBQlTlKJBeqUwCdE2bptn2PI8hDDtHhDa4MBvXEUoDpeMwh6xSTX5yqroLylKlmGMnb7Q6RmqLwx7tTFLkivl9CcKh3L7_dC50kzVIPjQmome63one59Dk-VjGneS_koQGFEGQtJ93urB7itI8QWbbP5toGxebXz_vbLG1RuKMotMKTAb1T8dc7lp2NHCsv2RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c32975f3b2.mp4?token=JqU5OlSzBdxQhsOru6ump3VjiGbto6sKccvl_IWAZZTUwpqr72pc9JNcWMNCgG1CloDe9CVNtc-aZBJbTr0kNkiC0DcPvb4aSpqO8Ioe76AgOZFybWe6xFuwVMuYe0AwP4MVoIZNcbq2XRXFqDdJZBQlTlKJBeqUwCdE2bptn2PI8hDDtHhDa4MBvXEUoDpeMwh6xSTX5yqroLylKlmGMnb7Q6RmqLwx7tTFLkivl9CcKh3L7_dC50kzVIPjQmome63one59Dk-VjGneS_koQGFEGQtJ93urB7itI8QWbbP5toGxebXz_vbLG1RuKMotMKTAb1T8dc7lp2NHCsv2RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: رهبر شهید جانفدای ایران شد
🔹
رهبر شهید، پایه‌گذار ایران قوی و مستقل شد. رهبر شهید به ما آموخت مقابل زورگویی با مشت‌های گره کرده تا آخرین قطرۀ‌ خون مبارزه کنیم.
🔹
رهبری که ما خود را جان‌فدایش می‌دانستیم، جانفدای ایران شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/654992" target="_blank">📅 12:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654991">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
قالیباف: پیام رهبر انقلاب را نقشۀ راه مجلس دوازدهم می‌دانیم
رئیس مجلس:
🔹
تلاش می‌کنیم اقدامات مجلس بر امیدآفرینی و آینده‌سازی از طریق ترسیم مسیر باثبات در اقتصاد و معیشت مردم تمرکز داشته باشد
🔹
ما به ایشان و مردم عزیز اعلام میکنیم که تلاش خواهیم ‌کرد اقدامات مجلس «نسبت مستقیم و مشهود» با مسائل اصلی کشور و نیازهای مردم داشته و بر «امیدآفرینی و آینده‌سازی» از طریق ترسیم مسیر باثبات برای اقتصاد و معیشت تمرکز داشته باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/654991" target="_blank">📅 12:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654990">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
هاآرتص: غنی‌سازی ایران دیگر موضوع اصلی طرح‌های توافق نیست
🔹
یک رسانه اسراییلی نوشت غنی سازی ایران دیگر موضوع اصلی طرح‌های توافق نیست و بازگشایی تنگه هرمز و ارائه غرامت به تهران موضوع اصلی آنها هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/654990" target="_blank">📅 12:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654989">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU8YUd9iu2smgpHJ_nqmetc3IJvwW3m2Aks1olDeD0kKNGnGKf-zJ3QYLV2fpvIKaubqWEhKMqD-J512gvotdPVlwvV4D6Beiw0UV_B6uzubtMGisWBCqgYKs63blP8pq6TXxN8WDvRx5GHTKZz_xz_cWecboLQCVu3sGjiljRpy8Y46M6W1Y9StCy7_Ws3zd1wORgyTgubwzf2VbSLUngZi9uGJTQvJ-n4r2D9GfgxBhHSbtCGx4oBlcBJ_ogUPXqv7vzfLhfQH-cL3BuGPcugn_Bv0wCVDMejd9LYstVlpTLNagcii-emZpz0brQ_U1Scn2H57vM0U0Frm4nayhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گران‌ترین سرمربی جام جهانی ۲۰۲۶ کیست؟
🔹
کارلو آنچلوتی با اختلاف، در صدر فهرست گران‌ترین سرمربیان حاضر در جام جهانی قرار گرفته است.
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/654989" target="_blank">📅 12:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654988">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn0k_JrsxeNjxWTbRG1tKDWNOzeNHR190YDLOs7skqx3q-7aGq2gtvJZCO2A0MJ2TQvQXUR0u_jEI6dH5SUECZmuwXltrXGY3RfsNa5pLHhpvKjHb5VlVzFvhX0mopZCON6aXS8Z2uWJaY7f4k3R3RyhE2Ko3ZscMOZCvKXPJTuRsDmOJlFIaWVpBvR5iT-S39MJ0Vdl41vCr31O6fdhjGKhudrK-YVlft4OCU4eidVjXRl-fBk-k93jkgpoLMAc0u04Zzjn5Me-Lh8swn-5x7jzuK96jGdM9BuHdBBQZ3No7Wfqa18PaoLHfWqTroo42ZobLqKoYXz8-Nj1pWZcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«ماه آبی» امشب به آسمان می‌آید
وبگاه سی‌اِن‌اِن:
🔹
هر دو تا سه سال یک‌بار، دومین ماه کامل در یک ماه طلوع می‌کند؛ این پدیده نادر که «ماه آبی» نامیده می‌شود، امشب، ۱۰ خرداد، به آسمان می‌آید.
🔹
چرخه ماه شامل هشت مرحله است و ۲۹ روز و نیم طول می‌کشد یعنی کمی کوتاه‌تر از طول یک ماه معمولی. به دلیل همین اختلاف، گاهی در طی یک ماه، ماه کامل دوبار دیده می‌شود. به دومین ماه کامل در یک ماه، ماه آبی می‌گویند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/654988" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654987">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
خبرهای داغ امروز و دیشب را از دست ندهید
🔹
انتشار جزئیات غیررسمی از یادداشت تفاهم ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3219059
🔹
تاریخ برگزاری کنکور سراسری و ارشد مشخص شد/ سهم سوابق تحصیلی و سهمیه جنگ زدگان
👇
khabarfoori.com/fa/tiny/news-3218868
🔹
ماجرای حضور رئیس‌جمهور با تی‌شرت آستین کوتاه در یک جلسه رسمی چیست؟
👇
khabarfoori.com/fa/tiny/news-3219063
🔹
عکس عجیب نابغه ایرانی که نفر اول جهان را شکست داد
👇
khabarfoori.com/fa/tiny/news-3218974
🔹
گنج پنهان در کشوی خانه‌ها؛ موبایل‌های قدیمی از معدن طلا ارزشمندترند | یک موبایل چقدر طلا دارد؟
👇
khabarfoori.com/fa/tiny/news-3218959
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/654987" target="_blank">📅 12:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654986">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXs8jGezckfij_Vw7Zt4jIyVcoegm77yhuhKuwnHQ_Jvmdid6wSwN96jSOWrBi1m4FOfJfXAN72OrtaCpR7SSzUebCPXDracu7bzdCAduhWryWnp5RyWHc9wR-wdZw4P3YoP5ZLDB20LqBryD3B6Qv6YxgyaZq-ZPuFpMqGKytSY1RhmVud9leqFGJpRXahdNsIQCUoH8ZTqVRl1t3UZT8O9ev-NBRc23Y3y5jdiqSLImpsXIdd9BbG7mCCrAkCgOdznjgvKax24G-siHg6gOOLdhGCwP96fIyPQa5KIgBt3FkzV1MQj1vBP8Oq48NkR7O-bMfztGTlEwClSWl0EyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پسر ترامپ به جنگ با ایران فرستاده می‌شود؟
🔹
برخی از کاربران با انتشار تصاویری از بارون ترامپ،‌ پسر کوچک ترامپ یک سوال مهم مطرح کردند و آن این که ترامپ و اعضای کابینه‌اش که مدام بر طبل جنگ می‌کوبند چرا فرزندان خود را به صحنه‌های جنگی اعزام نمی‌کنند؟
گزارشی درباره جنجال رسانه‌ای در آمریکا و مساله استخدام سرباز را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219028</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/654986" target="_blank">📅 12:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654985">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwK8RVtZKpjPSnMqNn3S4qx6Ir9Qlj4b-DWdISl2tcfwsW4qaxkAVQAdOHU8WLoCCLsygkUHKXILbwxWaOmPjVvjFMAdU4eCOAfIvQrTHlQlpZrn51y1LA0w2afbsMCPgzPOZPNlfXF9byMQ8B3kuUIBUjnKdaZViWS-YYXlPgsE-ULBbflp0VZCrNU1RDlsy9PtmSEtApMdqQbiRG4Jm5nhGpB7rgcKBfo9gf934NhxzX5ASOBm6TVXPBjCHbdIQU5zmbZi5_obQU-dqVV7ide2JoHrKZrvCRbvgC7O0-R51-y12Fcpuwj05HlgGvnxoI1pzy2iBS9hYTCz1qwnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دخانیات؛ تهدیدی برای سلامت فردا
🔹
۳۱ می، روز جهانی بدون دخانیات، یادآور این حقیقت است که بسیاری از بیماری‌ها و مرگ‌های زودرس با یک انتخاب قابل پیشگیری هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/654985" target="_blank">📅 12:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654984">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e9502b75.mp4?token=j8qShYYGwpstYPRCMc9QjEayZn2GVxTXvwejsFeCmLRNz1IVGABp0sQnvw6I0K1viJZ1rl1fdzBbU-ag-7qaBW1w0DwAgLWdPjh6grJ51cuQnWkcYeY-zC7oawrkkSMzRcP4eTynJWhbZtydwEth_MFoPemSIlOo8r1z0VWKe-f3zazNcSiNtrT3KN4XzL7f6MnN9rPVRH2VFHxqBR-3wPimooQiVwjKElITX21wxTJvw74dqkHgmHJzsz8DUzabK6jdVpQ8Wm8uhCkH_aQOm0PAFe7xWS1G5yEWUHMDaD5BD4Dzy0ryOPDPzq468-L8EL6EOZTKD6gheCpl5As0TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e9502b75.mp4?token=j8qShYYGwpstYPRCMc9QjEayZn2GVxTXvwejsFeCmLRNz1IVGABp0sQnvw6I0K1viJZ1rl1fdzBbU-ag-7qaBW1w0DwAgLWdPjh6grJ51cuQnWkcYeY-zC7oawrkkSMzRcP4eTynJWhbZtydwEth_MFoPemSIlOo8r1z0VWKe-f3zazNcSiNtrT3KN4XzL7f6MnN9rPVRH2VFHxqBR-3wPimooQiVwjKElITX21wxTJvw74dqkHgmHJzsz8DUzabK6jdVpQ8Wm8uhCkH_aQOm0PAFe7xWS1G5yEWUHMDaD5BD4Dzy0ryOPDPzq468-L8EL6EOZTKD6gheCpl5As0TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش صهیونیست‌ها به مسجدالاقصی
🔹
شهرک‌نشینان صهیونیست با حمایت پلیس اشغالگر صبح امروز به مسجد الاقصی یورش برده و اقدام به خواندن سرودهای یهودی، اجرای مراسم تلمودی و هتک حرمت به این مکان مقدس کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/654984" target="_blank">📅 12:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654983">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سخنگوی صنعت آب: اگر شهروندان ۱۰ تا ۱۵ درصد دیگر از مصرف خود بکاهند، امکان «عبور از فصل گرم سال بدون بروز مشکلات جدی در تامین آب» فراهم می‌شود
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/654983" target="_blank">📅 12:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654982">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBLV8KZUfaIwvl9StPj-_FNHyW-1iVaaUdCFMzEqWXVQ7SJRGDD-FoWhfKkJwjj1uLANeY66t-2g5qJYO3pRLQjy-r9rmsKDDhL8NOjiw7aexCpRuU84rO8tlYZABro3Fwis9dEIvE8dRyC1qvHywMZE_DbGU8xZjPAY13uiLHPUTstRA1DUx8fYiQihT1JLEF29LiGh5KEizNuJys6rpwWSe4YqBMXbt0OBzaVYWfBKYQSlC_HhEnjHxuKm8mxLZ2iIQ0zZmTIUacPeAsWkMstpCbV_q5aLgLszTtgiSTE7Mtl2XJBz1TjbNkPrmiUqp74HSqUpYLY0VNxj_KW69Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سواد رسانه‌ای؛ مهارتی که جلوی فریب، شایعه و اخبار جعلی را می‌گیرد
🔹
قبل از انتشار: مکث کن، منبع را چک کن، بعد تصمیم بگیر. #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/654982" target="_blank">📅 12:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654981">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
عبور ۲۸ کشتی از تنگه هرمز با هماهنگی سپاه طی شبانه روز
گذشته
نیروی دریایی سپاه:
🔹
طی شبانه روز گذشته ۲۸ فروند کشتی اعم از نفتکش، کانتینر بر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/654981" target="_blank">📅 11:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654980">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWJTrbhRALljhgh8Ns4A5RHZXwVhD-YXSz5A7wIHfGIa5gpwSLyWRxjcyMpaLug6fM5utTuiedNseHUgIiaIGzsNhRdy31H1c3uVBzLwPGGUfejidEKp1BK88KGUerc_k3x1nK4oEiinxpH1YV7YViXfy1ptmrZb2wxsSvYQSTX5BYD8btHSNqWGy8Ef88FE322RlDK4MqIJcdVaeL4GgoS13tC8x5-zpKVDi-2Dd4b7TE1lTZZqDMXEnpJYU_QN3WTnz8rvVkref-_6l-1ndj-yOdsogtDXHKRnDq9eJa6p-t_22fKtyM7-Qh3c2XMuj9HhnHMcQPtrC39_X76MHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تولد نوزاد دو سر در بغداد؛ پزشکان از «مورد نادر» خبر دادند
🔹
یک نوزاد با دو سر در بیمارستان «الیرموک» بغداد متولد شد. این نوع تولد که در پزشکی معمولاً در دسته «دوقلوهای به‌هم‌چسبیده» (Conjoined twins) قرار می‌گیرد، از رخدادهای بسیار نادر به شمار می‌آید و برخی برآوردها احتمال آن را حدود یک مورد در هر ۱۰۰ هزار بارداری عنوان می‌کنند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/654980" target="_blank">📅 11:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654979">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73fbb9da9.mp4?token=ELxLlpVWlNaPhohpLnR4uoc8ihqzRT1EFYUiW2FpdI6NEd_dRV1DrFCKawaCCnCQkVTgKRibCU4zPDW_Mz61oQxxbJe3qzout7-YIJL37qzDL4lUhYs2rGS26zuSfBjUN3-eLBYS8V-kM46QYruy8QiwVonWkUq3zji3UId6luPd9WPFyVwwuRyNzt4aFjlF4lmu5jNjVgJv1Q889SzQveCfEOecF2z0V-73MX9jEbnJehKS8KqKvvDO1HncunxYrU6KmOza9VdgYBN_h59MxL3w3Abr5Yzu_MO0Q6zY_bHRW_Cn2V2hsJRlcI1Yz9xh6uDWHEPByoDteMwXYH1Xxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73fbb9da9.mp4?token=ELxLlpVWlNaPhohpLnR4uoc8ihqzRT1EFYUiW2FpdI6NEd_dRV1DrFCKawaCCnCQkVTgKRibCU4zPDW_Mz61oQxxbJe3qzout7-YIJL37qzDL4lUhYs2rGS26zuSfBjUN3-eLBYS8V-kM46QYruy8QiwVonWkUq3zji3UId6luPd9WPFyVwwuRyNzt4aFjlF4lmu5jNjVgJv1Q889SzQveCfEOecF2z0V-73MX9jEbnJehKS8KqKvvDO1HncunxYrU6KmOza9VdgYBN_h59MxL3w3Abr5Yzu_MO0Q6zY_bHRW_Cn2V2hsJRlcI1Yz9xh6uDWHEPByoDteMwXYH1Xxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مری ترامپ: دموکرات‌ها باید ترامپ و نزدیکانش را پاسخگو کنند
برادرزاده ترامپ:
🔹
دونالد ترامپ و نزدیکانش سال‌ها از پاسخگویی درباره تخلفات احتمالی مالی مصون مانده‌اند و این روند باید پایان یابد. در صورت تسلط دموکرات‌ها بر کنگره، باید زمینه رسیدگی قانونی و پاسخگویی ترامپ و اطرافیانش فراهم شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/654979" target="_blank">📅 11:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654978">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFkfLZhQsZwKOdDtFT0Kgmfbs0leemDlaNWkBkzzmKltwzwU2yGSNBfECyiCKEUK7pCF_fjhBetbV_H2JsFYN9vwLNuQM7tF8vccKSb1WYrw9k_micV9k7kFfe12SFW7-ibIlgXZ04qJPHsVEeWFNvOuY_tnIJKwaYhLuraBKNinuyWZ-2FaxcAOTJTgNfmyOJSR7U60pkholTHuvoJGtSpVvKUsErM20BgDyA6u0nx-bxFodIvEfYTCsGmoTvjM0yH4IHd2ImGFQgmiqmvRwOpQZ3tkmRTQh312Xfi8_eKGMyH-rAPk2OgkY1Nbtc34sNCaRam1xXxxM-UyoqSuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممنوعیت استفاده از شبکه‌های اجتماعی توسط کدام کشورها اجرایی می‌شود؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/654978" target="_blank">📅 11:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654977">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sixbrMny4kr7Vr6uj6IhtW2fiiJkpxMgUCShV_Zusoh3aMeWD4ywj7iAPCaTNT6q9Sic6DOxFSb-RE6IDgODZRHdhZSujChKxrFa9lUX-ZrE3rSGW7h4k4GWOjdDCyxT_-DVFuralUXm8zntdn-CX9aJFz0j5q5RdvfCii2q3ig6JWVz8vDm-o64xmMm5UwmnH5cYGxSpyttymv75jK0t7H3muvJ-R4gjtszcBRaBpPRFI3TVmS_uzu-SaEtvwgLzEHtVCXUMwV8Mz3lGMqKEWumeM1oNDPEU-EB71Qq2Hm7p5OExJBnbEA1IiFVSS_G7OHWFqkJ0CT15cJldvbCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد سناتور وارن برای پیروزی انتخاباتی دموکرات‌ها: به جنگ ایران پایان دهید
الیزابت وارن، سناتور دموکرات با اشاره به انتخابات میان دوره ای ۲۰۲۶ کنگره و ۲۰۲۸ ریاست جمهوری:
🔹
اگر می‌خواهیم در سال‌های ۲۰۲۶ و ۲۰۲۸ پیروز شویم، دموکرات‌ها باید تلاش های بزرگی کنند.
🔹
هزینه‌ها را کاهش دهید.
🔹
به فساد پایان دهید.
🔹
به جنگ در ایران پایان دهید.
🔹
زندگی را برای آمریکایی‌های کارگر آسان‌تر کنید.
🔹
دیگر دست دست کردن بس است.
🔹
وقت آن است که جدی باشیم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/654977" target="_blank">📅 11:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654976">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
یسرائیل هیوم:
ده‌ها کشتی حامل نفت و گاز با مجوز ایران از تنگه هرمز عبور کردند
🔹
منابع دیپلماتیک و اطلاعاتی به وبسایت اسرائیلی «یسرائیل هیوم» اعلام کردند ده‌ها نفتکش و کشتی ویژه حمل گاز مایع، طی هفته گذشته با دریافت مجوز از سپاه ایران از تنگه هرمز عبور کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/654976" target="_blank">📅 11:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654968">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlvGo7h7WgOumx2GF543KCmTBMXmkMWYiqxWg5DWHcDx5erRK6SrGHBVxLJv7ydrD9dtE3ip77dIDyJdpuUtWUeNtdvrcaU5DtK9OZ0dbTHZ5q_KZ2a1OXzmN2eBqjFto9ozCZaRx4VOFKtu2fcICA55RzWYPqpNbYLG_Qh-yS872u8Fsb_4eo4gM46HzNVd8RNJmo-LAumC3Nao3vIC_-W6u4_2tQxe1avhmRLf1N88NcXcaSbrYiP4TssrK7GO3wkwboSEaedzyQn6uZKPZ-8YQ3LJ8O4HTVCh9z4d8ThMca1hIEBxVqqE1m1uU4Zj7K4Mq1A8mWiGm6TaAbPnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sM_t3FxNwdBPbqtvW9fJaQJ0xZ0LHJ_3I6pKglV8f9Za7nqIJtYflX4N6y32ks2Rdol9m4mTeEf8wRkMjWhhnx8Ar0itpZVeIsNQu_jICI1vDAnUKj6MABhmcyzwIYQB57n-lqz4RmqwgoGi1Gkr4v9qGd6CnuAn0rKYgWTXluaiwdJLBuVLwDBro4LcyBY7okptzVYtmL8Idnqx12Ai063roEnwGck5lCcBT2ISu84qrpZWgLFM03NEyxFlf0rnBPcNFLOEPwnMGiyY62YldvXtYhxT5As0C53YgJya5NnjOc17w6ks0Mde-p9deUkJI3k2KJHApXXb2r7LqXgJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xbv3gAY5Ay1OB-5EUwUnWMpBN1I47H6a1e6Ds1J3M0FScNYi2ULWvGV_yBgqeAfWaXbl4FY9rSw9qiNS17yC7ojar7NPJzvJgz44Ze2hGfUxVwheVxnVudiIN3NCWZ9gty6bzX3Hu_C7s0bRBYqTbEQlMP-zSLaoBZ9TfcqyJu5N70OEhoy61hjzmdXjTz35K7Cg7nWP9ZuDI6jErlC2eQi2nirmJ1OlmXxMrzN9yEaVzUCnyX96jUtdeV0zWWqbXEFfbwy5LnzJSRF24EV3rFxZ0_je5iXvDJq1JrOn_PXUbzeNLdZZ5heZJ3fjN66RirP8fm6yg3-Qk6B_pJnbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRCBrhT_9t3xHqW7wipT2S95wJf8mT7mgK6OOPmKVUL_dSFMDqXLPh_bffk7gjGlCro6l-n_pnFftgQxS6yFtYqFshjESmMqzVvL6m5y6h5gQeua-EYsslTboNfZuOkBYePvxrABrniG5O0M2aofMHOyZSfzbDCCWWOeRszGZ4LjYMV32Mu1Qa9vlznCwFf_ZO30P5CONJ7vj_WwbRZWL8ABTkZkpW8QMgW0S08Zq0s0pZedy4KYzy6CEK9blmC5u-Y0uY_zOjvVh9ocTqFE6fX4-6dCXMFlA920PEUBF2K2E4FXYzoKDlyg3fQU3b0GAifkGUDUiiiFC69r2Kkslw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بابونه‌های فندقلو، اردبیل
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/654968" target="_blank">📅 11:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654967">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سخنگوی وزارت آموزش‌وپرورش: شیر مدرسه  به شرط حضوری بودن مدارس در سال تحصیلی ۱۴۰۶ـ۱۴۰۵ توزیع می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/654967" target="_blank">📅 11:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654966">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromصبانت | Sabanet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2te1pgIFWG0dfBTCu9o98u_MVCzHieuXhCXdSFSn_yJplhqTR9zMROeVx-WS6KUMifC2VRIaBm7422w1fFcNUpCqmrhyRBumyHk1xo0gnrpdwnCY3nHxP_AG9lGjN6D_9nL9YtcNVQ0TNtAVWzuiH-xtk85qC8G2lE1eKMwk-1TS39QqpVwW4HXgvgzHz83nvQW1MGcupU3_uUmvi_uQ0uBt34bABrbRpVDNGVJtfeLFJFj2sU0ZFGhbHZB2JYey0vDzErKMhnbRhnwK_fakz3bRx8FCsKEhVpIGRlGP3Elm9vwikTOC7gCH4kKrBLFdVNwfbCjnGZfZ1s2SOzRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اتصال به اینترنت بین‌الملل فعال شد
💥
با
اینترنت پرسرعت صبانت
، دوباره به سرویس‌ها و سایت‌های بین‌المللی دسترسی داشته باش؛
از دورکاری و جلسات آنلاین تا وب‌گردی، آموزش و سرگرمی
⚡
✅
فعال‌سازی و خرید کاملاً آنلاین
✅
نصب و راه اندازی تخصصی
✅
شروع سرویس در کمترین زمان
✅
پوشش گسترده
✅
پشتیبانی ۲۴ ساعته
خرید و فعالسازی:
👇
☎️
۱۵۲۴ داخلی ۱
🌐
وب‌سایت:
sabanet.ir
📲
اپلیکیشن:
sabanet.ir/app
💻
پنل کاربری:
ecare.sabanet.ir
لینک بله:
https://zaya.io/Sabanet_ble</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/654966" target="_blank">📅 11:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654964">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiWy6RNlcjcbqMmwXbC1mSzp8goEuxtTV1B5190geBQU1Rp5Rcj6LGklEgWPD674Ym6haRwHYBV_MVMgmYk7axCYGE3CILZTL2PhxMYJLmiCizPk6AQh08U89hvPGb_HcygMUKpM5kKm8kY4Mj1kToraEk7fbEF4MnlGKvRJ-oSgNg48NPDkZpuM2ob9BdfUBi0GAg6ozfDHKrUhp5JJRFIXOlMSM2Tz7AOC7SMKXWuyj5l8-4xV_U0hSeoHd-renPUJ1CpInqh6RfOFQRkUeYq_rKviD04ySB1yXDYOvqLZOuLujYN5V1lN4ULfTjnsniKUNftb5olmWaEKxFNa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شناسایی دو ماده مخدر جدید؛ غبار میمون و کروکودیل
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/654964" target="_blank">📅 11:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654963">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
شرایط دریافت کمک‌هزینه بارداری و مرخصی زایمان اعلام شد
🔹
بیمه‌شدگان زن در صورت ارائه مدارک لازم و عدم اشتغال در دوران مرخصی، می‌توانند از غرامت دستمزد ایام بارداری و زایمان بهره‌مند شوند.
🔹
پرداخت این کمک‌هزینه منوط به داشتن حداقل ۶۰ روز سابقه پرداخت حق‌بیمه در یک سال منتهی به زایمان است.
🔹
مبلغ کمک‌هزینه معادل دو سوم آخرین حقوق بیمه‌شده بوده و بر اساس میانگین دستمزد ۹۰ روز پایانی پیش از شروع مرخصی محاسبه می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/654963" target="_blank">📅 11:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654962">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وداع میلیونی با مردگان/ قیمت خاکسپاری در تهران ۴۰ تا ۵۰ درصدی افزایش یافت/ مرده‌ها هم از گرانی و تورم در امان نماندند
🔹
طبق مصوبه جدید نرخ بهای خدمات در بهشت‌زهرا هزینه انتقال هر متوفی از سطح شهر تهران تا شعاع ۱۰ کیلومتری به ۹ میلیون و ۷۵۰ هزار ریال رسیده و افزایشی ۵۰ درصدی داشته است. نرخ حمل به پزشکی قانونی کهریزک هم از قاعده افزایش مستثنی نشده و به ازای هر کیلومتر اضافه افزایش یافته و خدمات آمبولانس خصوصی بیشترین رشد تعرفه را تجربه کرده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/654962" target="_blank">📅 11:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654961">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615efcd34c.mp4?token=iWOVOBS9fL453axWwIzveEiYvc61xpuWO19NjGJ8zdR7Jj7xsatEDAfKzEpkoqzsT9tC7ZxymcjpZ-Sz3J4o-V0QiQED1gQbeRBU498_1KUo7Mw8bZfps3ikdX2GL2rDqBnP_hqR0H3T8uXB9_gekBkDKPO9s_fzKoleXDu9YMKJxuhLdthO1kyhcrG8fibDCarirQGS6NYN5vQX7VLR4uvb9IRcxxKL8aQvC10VlhbgD1wUMTdc4tqwKlQAC94gK8WlMOZTrJiB7m_sYXdqm0ecuC9M8MdRHr6Q9Kf0UtYSUiZs_2ZPMT0RdVmGsoyAGjsMpJ5XZWUjR_VJeb-KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615efcd34c.mp4?token=iWOVOBS9fL453axWwIzveEiYvc61xpuWO19NjGJ8zdR7Jj7xsatEDAfKzEpkoqzsT9tC7ZxymcjpZ-Sz3J4o-V0QiQED1gQbeRBU498_1KUo7Mw8bZfps3ikdX2GL2rDqBnP_hqR0H3T8uXB9_gekBkDKPO9s_fzKoleXDu9YMKJxuhLdthO1kyhcrG8fibDCarirQGS6NYN5vQX7VLR4uvb9IRcxxKL8aQvC10VlhbgD1wUMTdc4tqwKlQAC94gK8WlMOZTrJiB7m_sYXdqm0ecuC9M8MdRHr6Q9Kf0UtYSUiZs_2ZPMT0RdVmGsoyAGjsMpJ5XZWUjR_VJeb-KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویرانی گسترده شهرک دیرالزهرانی در جنوب لبنان
🔹
ارتش رژیم منحوس اسرائیلی با حملات هوایی پی در پی شهرک دیرالزهرانی را بمباران کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/654961" target="_blank">📅 10:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654960">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
سخنگوی صنعت آب: اگر شهروندان ۱۰ تا ۱۵ درصد دیگر از مصرف خود بکاهند، امکان «عبور از فصل گرم سال بدون بروز مشکلات جدی در تامین آب» فراهم می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/654960" target="_blank">📅 10:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654959">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22981454fe.mp4?token=XGnylrTMCn1sxQoY03Ufu1fBEtc4w76fIbwcCW1NKLjU_boy2C0ik59QfJwEHmnhZVvUS0f4zS7e7veAMklxk9TeUue1pFVXFEWH0FLkUChCwOf9Qrs3a554qmYf5Cs9jn9TwRqrioRncqgaNlwYyw3X2zHSEmpjynLt4Ym-keLHDHk1XDg6iW2TNsvh6dVvz9uX3_clLfJChuFcPTE0fQWiplsBsNLjgPVB1DFgTYSGyr8xtSKYxvJ2oLTl5Xc_xQz0Fk94V05p-gCXRw77aEQqU7RdFBL6x3XUv69Z5TxpKkwOzDZ6lKLkW0omnXO0mdAvUlz88Fl089GXlT4ZMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22981454fe.mp4?token=XGnylrTMCn1sxQoY03Ufu1fBEtc4w76fIbwcCW1NKLjU_boy2C0ik59QfJwEHmnhZVvUS0f4zS7e7veAMklxk9TeUue1pFVXFEWH0FLkUChCwOf9Qrs3a554qmYf5Cs9jn9TwRqrioRncqgaNlwYyw3X2zHSEmpjynLt4Ym-keLHDHk1XDg6iW2TNsvh6dVvz9uX3_clLfJChuFcPTE0fQWiplsBsNLjgPVB1DFgTYSGyr8xtSKYxvJ2oLTl5Xc_xQz0Fk94V05p-gCXRw77aEQqU7RdFBL6x3XUv69Z5TxpKkwOzDZ6lKLkW0omnXO0mdAvUlz88Fl089GXlT4ZMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه بالا بردن جام قهرمانی لیگ قهرمانان اروپا توسط مارکینیوش، کاپیتان پاری‌سن‌ژرمن
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/654959" target="_blank">📅 10:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654958">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM_dOxkFi8kSqvxM62nPsN9ba-pLzVRg7e5hXRqQanT2KMNmniJN_6J1_VBGrerOZxch35UaNrn8B4gmG4W-mQghXnnlawtuT3Mq9k0p-L9FIdNvjcYjIzsQBgqcVgmcy3ouRTDTnLYlxjIHLj8uq7zIggtATsrZ7xRfzKqdlAt3sBPTpJv7fzedRbnu7pc_qYLA4T1J_7pL38ZN2ipcal5j706IHpikUbUONjo84tgi1hZ6t9La_LZvfeUf_QhyMncD1IbVmHavWY4MIVODY98vvXWQNTCKZ-yr55A9KEbqTNZnyn6f2sntQ7DPnC6HI9U2KcIo0zwWhrE9xh4EYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: ترامپ در اثبات روایت خود به مشکل خورده است!
نیویورک تایمز:
🔹
ترامپ تلاش می‌کند جنگ ایران را در آستانه پایان و با موفقیت کامل جلوه دهد، اما روایت او با واقعیت همخوانی ندارد و پس از سال‌ها تحمیل روایت خود از وقایع، اکنون با بحرانی روبروست که با داستان او در تضاد است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/654958" target="_blank">📅 10:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654957">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc796c50e.mp4?token=OYmkL98pKikhpbtqwVUcrkDwWdelDZsKDgKszSssA0b6Ig96BY8ysvjWuvxXwOprLmkYHDUQJc5uCPAlFY895KW6f8HLA1c46-lmWLLmqynu0oS8mCWDPH2dXQssAwAPMu8mwylh-dTvpi_0cSKNZY-01hifB2ssCR7ZTAwwnk82oXPSnbGNaccYTWuBI2mb_Wa11TrhOaoWCFWQnLPg3EfQXhqpE6pbc4Kp4ZIAr637TNPxu3a2s8A_dI_AjfJD7JUDE08YxW8NfzVGtj__1H3CVk24CI7ZGGgyZ1BClf8nW_Y_4ozlhdec-4Oyxv4I-0NlfLzf9rOPdauvpFwm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc796c50e.mp4?token=OYmkL98pKikhpbtqwVUcrkDwWdelDZsKDgKszSssA0b6Ig96BY8ysvjWuvxXwOprLmkYHDUQJc5uCPAlFY895KW6f8HLA1c46-lmWLLmqynu0oS8mCWDPH2dXQssAwAPMu8mwylh-dTvpi_0cSKNZY-01hifB2ssCR7ZTAwwnk82oXPSnbGNaccYTWuBI2mb_Wa11TrhOaoWCFWQnLPg3EfQXhqpE6pbc4Kp4ZIAr637TNPxu3a2s8A_dI_AjfJD7JUDE08YxW8NfzVGtj__1H3CVk24CI7ZGGgyZ1BClf8nW_Y_4ozlhdec-4Oyxv4I-0NlfLzf9rOPdauvpFwm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلمب کافه مروج شیطان‌پرستی در خیابان ولیعصر تهران
🔹
این کافه با برنامه‌هایی با ظاهر موسیقی غربی، بستری برای حرکات نابهنجار و «تحرکات شیطانی» فراهم کرده بود.
🔹
مشتریان (دختران و پسران جوان) در وضعیت غیرطبیعی و با حرکاتی عجیب و «شیطانی» دیده شدند.  #اخبار_تهران…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/654957" target="_blank">📅 10:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654956">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
شرایط ثبت‌نام کودکان در مقطع پیش‌دبستانی اعلام شد
🔹
ثبت نام کودکان شش سال تمام مشمول پایه اول ابتدایی در دوره پیش دبستانی مجاز نیست.
🔹
ثبت نام نوآموزان و ارائه گواهی پایان دوره پیش دبستانی ۲ از طریق سامانه سیدا انجام می‌شود.
🔹
شرکت نوآموزان در طرح سنجش بدو ورود به دبستان در دوره پیش دبستانی مورد تأکید است.
🔹
رعایت محدوده جغرافیایی محل سکونت در ثبت نام نوآموزان، ملاک عمل نیست.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/654956" target="_blank">📅 10:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654955">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
بازسازی تأسیسات نفتی و گازی آسیب دیده در جنگ به کجا رسید؟
‌
ناصرآبادی، عضو کمیسیون انرژی مجلس:
🔹
تأسیسات آسیب دیده با تکیه بر ظرفیت متخصصان داخلی بازسازی می‌شود. همکاری با سرمایه‌گذاران برای بازسازی تأسیسات نفتی و گازی آغاز شده است. هیچ تصمیمی برای افزایش قیمت سوخت گرفته نشده است./ایسنا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/654955" target="_blank">📅 10:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654954">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSYqBJr_iOn4eifZqZ1J2XbPa2TTAJhL9b39vhGzG_qNVS5LXhg5s2syyCeexzRO60OUgJPoG1y4wfxd1LdBgo0j8uuFNrZlGDyoEB5H6bBGg-NeYpHg9oUUou-2SupJfBHSRMkvJphV5S3PGFEZmSXUXjtZXZ4aOO1ib9UrA4Wg0UvKS1xKGzyiiP5wJRXPuAZ67Ka3jCSj8HrS0G27U54wfmhT7or6Ui39sruYW1zEFEJzg2PI1EmYhXzp5Q7A3jl8cEFf6Oa-ZFS8ff3tF0GpyGITfpsuNwGpEMEs15tXfF0ywOxbSsUVFinuSeP_suk4_8aEMrnKjx4AadgtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز عجیب حافظه بویایی انسان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/654954" target="_blank">📅 10:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654953">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTvFYkaDFwi680dyGbtKC6Ye6D__n3kzglDRQ2hPS8RgYwJXeLr_f0QUjnaKq4xNtblw9S3mMmK2iMYaV-gPsimGO4QyKF4n1g89De0V4RaMEKtfy_2dtYysln5F2ZOvP94aSUswmnquk4WUmkHYAsJ1jt4umiP8cMke7MziFIipcN2EI1fMrDrYm1_ir6X7obt6VW9EZvaRYyi1JqPTaHCCUaSGQiM-kIow_vGt5KaiXrZ_ekmTIwl5fskgkzAgFrB-Rn1BrSWHY5K7EGxESw6bqF-LQXjqz5Tq0cPmotZQKvsyltgifO2M9s_t58CnAlqb2cNHJm1WUsBPnc-z8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماد بازی‌های جام جهانی از ۱۹۶۶ تاکنون
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/654953" target="_blank">📅 10:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654952">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSz-wrQsIkmSKuVryDpv2kxplyCa-VLPs1bp2MEdDPRQkBsokI636I07FwBvOTJvT9KK4AYAGaeazCvcMjXo3cPARApvJyOrwkSi_CJodOFXw69ohabfP1OCtAhrfjFKTudOXjNjmaKzOR2u43HLwn4bL04vrkek-DaGxg4HJW1d1FQOFy5hGT1aTONd4GzXZuNme8tghx7dnpVATmSDU0sVtJwpaLmgFnmqyNrqRuzZmVJ2a179JJoRaTokK058vn7wlu2a7LB1pjIy6XT6nHNVAS5lch3cVt6CGq4YXylYQjt-At3jqJ8LM_WPPKZgLbMq7BzA6fKydYMbLcPhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه ۶۰ میلیارد دلاری جنگ برای مصرف کنندگان آمریکایی
نشریه میدل ایست:
🔹
جنگ آمریکا و اسرائیل علیه ایران تاکنون ۶۰ میلیارد دلار هزینه مستقیم برای مصرف‌کنندگان آمریکایی داشته است. از ۹ اسفند تا کنون، هر خانوار آمریکایی به‌طور متوسط ۴۴۷ دلار اضافی فقط برای سوخت پرداخت کرده.
🔹
مودیز هشدار داده در صورت تداوم قیمت‌های فعلی انرژی، این رقم تا اولین سالگرد جنگ به نزدیک ۲۰۰۰ دلار برای هر خانوار می‌رسد. اقتصاددانان آمریکایی تأکید دارند ادامه درگیری‌ها هزینه‌های بیشتری به زنجیره تأمین و سفره مردم تحمیل خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/654952" target="_blank">📅 10:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654942">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/loL-rsGD-A_N4UJYH5JqRD1gEnOD4H-msW4H1G7VnxEicXMLpfNUo4wwOfTqWulq0wqAlGz1spz2zWX-5wfevjjZunyXdQFuFQvcQLVTuS313w9oVIHozhedQ-sbe4MNCJyTv6xkg3HhlOuLcHh7e8M-Lr4lcgs-a0qPpBthdbisXHnN7YSRAP7geD787kvlSlTDIJYf4FGgePwYLebi0XGAb3U2M8qcclVg4fpJtJe_xwwbd5BZW-wwWUKqxPV34ubaDZd3p8F0Ul4r3z74-sd7zCMuJJJx3UvrJHIttSyy3jSDOoVY5JRpPNRbkc_mMYa5TRdXVwSYTncfFiw8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e9igSd6b_ls4OPBftRrIBsZW8BkLRT62RtZTSS3xTNaPVjl2hV_fTh3dx4Hv12Ao_HOUgkVibHH20gUGbTI95-kKL_c4Zx6aqiXs72ElsQ8m4nhLI-QS4ltvYtnZP-PxgtAFXzMQbULZL_3EvEGAzuHRms31aflPTbux1hVhfC3ScW8NenOB5IZaJiRfV4nObmkL1B3sDRH7Td2QYIv4WuPcYLqqmz6L-sHVK_9K7nWQS3NDEGwm87C8xEnVLcC2GLeyjdSOQ-kkXWPMR50jjuFf9sJTAi9tU0G1MFhdzEzsKDPwiUWe2VCmonxDMFD1lZ1rEioIfsu1VHSTv2eiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jlTAGcQ2ijIH-PWVpHLiKur0ikgwrpAJR23dZvLQ_XSlVKfwynWSfK6opPcPafm8Cjd92nxDQbaZdKWn0SWOj61hCH_Mg1SlkQgSnjt_I5vPJiO73kz1WNVE-NWnAT_aJHp9Fc_yIDP9BwvgERmjm87-m6uJ22SYJ2x-r180CQRLqracgBB8xHQKIQmx3n1DAzyYBNRpk8xOEQA2bmbIN9XnmTBsrWS7bmI0aIaUT8CAX6j_M-y3m_yIRq6GxBioeLZ6v7RudC1Fb9wmQirhu-1zd0Eq6anyaoVz9Aw9DtsxYtYCFnlq65Dwfs4A3NHNA2FKn2qkYv4eSmXkaRUBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sfdc866yFuOHopORtvyIOKANw6V4oR3KtuuexByRY1A6xEGhcHBTczgbKKnczbPpOvcn0ijPkMdbc5iHnz5ppqxTMOFQptdqzjWbvfu9n0TbY2JLR1i2h8SkkExM-U-MlXQ2lfdixGT9TQvLadCYYyuPLdTsQPZYHu098oHWeNbqnHdLrgVzfBrkgrSoAebx55KsNZ2ib4jjtHDJiz5Yic_jdHp0jG2DwACom7bt8rsrMsJWQZYm-Tp2LJw6rXqrcjU14s7jEFRjqjZsHiMdpRH2OlCRU_jEbFu4cxi-V41QyfEmWxmWX5eTXLuHEf9sg1wAR4aX9dg5lXYAsn5KFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B9J_C-CdVK6dRC2NpFr2zMpbNa0kMjjHVJGlnwP5g1AfSr_DMG-F6nbOhQxOytyiGrIajVZgTLtd3yajyJvFPTJH2O9sZNT55dvaOQ3JagiZm7Rv0rBs8_NZJksymD3R4yOu9Udd2hcngBqqHWWjt65BRyPrpOlzCVOC4TF3tOcWdCJNhkJgrTDbJadMG48wbQ66tHzGv-v5xbdS3NkXmMr_EgZxVPMIi6QaVgsIeyF030QpwRLmDZHF2VQp-LzTwFXmv76CZRaRr0fsmIb7fLyvk7mlSL-YN7ee7wqdiz0IucisgKDlhp4sjH0Z2i99DjYJ7hFb-UUhoJxicexKSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hIf7yOGzywnrE29o66j-PbEJbcLRIBqlj1E_IuDhDSdrxz_BFE_g6RjWvS20CsX1b7PG9vuoEBiqaIMcQfFg5DsYpgm4QXAQe0A6O6kkqzzoqn191GhXR-9_d5qBwep0gFR2UxTsMSBY56C1hokEZkPP-j1hVl7Y4nbahaepmYS7_KxsqvaOzB9Pqd5kniouE0tP2f-kYzozgG2Y7paQJ-QkcuuvFgE1-ksMdQk2rhHe4B9FBkD9XJlZVIA3nPxsGu88GMuptUeXyU7kDZ9G0DOTWV40El-CK9bNEChXxRpRSDymc7W74ANlGeFypA_CoSnwA_3htJFjbf5e0mEZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tIzXfkCkH1T_azG-cx0OUSkb5Bs-VO-PwnFDR3tXxGEGoPazkPVXy1Usdu1hiKG8fd4G37W9pIv9zZK53Q1tTqyeIdPGhJqGqCfMVsTqQ_WAvn3POSs96rBSB0xhyuCU1-mOsyTHKqtUZZvPV3nNEjBdyRnznQpLRXgPZ_cvyKAIRvx9466Zq62g_4KfbgsadJ3UepUZYk9yyYCSKmQK-o43CQ7M9opqjbQFRfQ-Ebwrm1oEujOSATCEQisbR5mr-KI3AiPoXEV0nkD75NB34qEpzGhrP3LQxb6G_37tj8-uUUxFUUkZCopyJB5_LeVt198eKdPJY2E-dvET-LIU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mRDhn5FuBMYyOcSJtw1ZiroVpQN1JQFKbXC-64mqF4tCItLWlUKWd2SDTEoAAsq0DOSIUbUfkg0tV7nXry9AdsCQvDWUPOLUcrw--BkiKZSeCM8keqAc6LiR55dUN9P_bLDo9IYu0rq0pavIg7iXyva4cRcSiDPhrQoLy8SDHfa1l69xRNC5JGUuhLjFwH1x9WiPlJjMR8neiY_L8-zdK5wxmU10adhbefFqWG3wPbKHGELoNdUUqyNpA0TL9lc46v2yBQ054G1Hahg3o5iEV0IQhe4q8tN6pqPkkPfUmY5c7Rn5VU_Fp4l9ola-KPddr0lLHSR6CKi1QTkJ2viSzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gkap1jbcCfhxGDbd6ldJLIKxyGK8wrkuO5czU_pyM12jx7n2LG-cr4Kej0lKfxo9yJVpdc1cgdfD3cWBHqv_1WpgruBgIBoubp3LV9_PJ7JXK1EStRQpmwzqE3ESWac1VoJy8tvJwyyoAYhZo9HEqv_iWm-WN9lOH2gZxCUBbbOoq1-zVNC2wvhXp27tRCeaoyhBfVv4CdUgD3IxB8KAkaQRudo9E757o7ocQ9zR4qtubz4wfRj1ykOCtHuETEhmFuEFjyYICJFnjEIzmqUZK5cDxdov_q71-j0I5mt8a0yQOG3-0rlgeyHPMWqgF3PnwCckPougxPvquev_NbysJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/grBu0J643A8kIP5TlqBeHiQWeTZnbNEc4f75NmCm-LrFodU9FMDSDDDj8SC7UFbopCnfl6-Zjqv1MIV0FKI64aCgk_iCoVEXz13dVUXNqafHgcSV-vHQ7zD2xrbLY2211EfHPAIOdM_BUYo5W0appktVpp62r3mQKsHXDECY0zWagiO588MH2kbj4MfvQLWL-jXa2zsR0GtxEDCNM1eY2LY6cfmQmpT0yjLjntTp25KPgj_DGcwJvurHIHm4x2S6_fMXRWJE-c20ucbx7aKhFN8uVUDIez1pgj5zqcvwvQ_jzzlE07ee2gFv6GBjxJK3hsEc_Bydsn3acD4fkwEPvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نفوذ حنظله به مرکز پشتیبانی از قربانیان هولوکاست و انتشار ۲ میلیون سند محرمانه
🔹
در یک عملیات سایبری بی‌سابقه و چندلایه، به‌اصطلاح «مرکز ملی حمایت از قربانیان هولوکاست» (
k-shoa.org
)، که مدت‌ها نماد قربانی‌نمایی صهیونیستی، جعل و تحریف تاریخ بوده است، به‌طور کامل توسط تیم هکری حنظله مورد نفوذ قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/654942" target="_blank">📅 09:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654940">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQCyv1q6XO6VVJYQUFmjMk83eqEpG5LRtLz5Q8CE7kLwqTVClZ7vwoKE_bVa4mh8C9mzLStYZ40YgnLucxq0hPsUieVB1Bbaok2j9E_rj4iScHdJygywCf3JSfGMBoBrhFbwRZ4eXCBPDu7iDqymOur7rCHGxroXC6h9npRgKZYeLVkjNYpDx3aSiGSztDqM2nIUMWev9TQlgzHsql6XmVYYMfxOuOF34ugNfhVR2Bctkw2NuCcgsyeFJc7Cm80l0gWUZqIIAZEHHgQ1H5uai-fG0_fHe0BokYH9K_e0ksJPFgr7_QnE2Q41JILtj0pi9QkioJvFennkB6LKgt2Pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت سرکنسولگری جمهوری اسلامی ایران در استانبول: “پیت هگست: آمریکا توانایی از سرگیری جنگ با ایران را دارد.”
🔹
اگر شما توانایی جنگ داشتید، برای آتش بس التماس نمی کردید.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/654940" target="_blank">📅 09:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654938">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
العربی الجدید: همکاری نظامی بین مسکو و کابل؛ روسیه از طالبان در زمینه سیستم‌های دفاع هوایی و سلاح‌ها پشتیبانی می‌کند
‌
🔹
پاکستان انتظار نداشت مسکو اقدامی انجام دهد که مغایر با منافع اسلام‌آباد تلقی شود، اما این اتفاق افتاد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/654938" target="_blank">📅 09:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654937">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4d7ccf7f.mp4?token=SgmD-VzvKBvqpArb0MNdZMtlVAA8gAcZ-EG53hp1oKe3gW2vE43F92agzoefqi3HLTtpNqoadNez9U9hKVa13NQnFEa9JH6fHyg4rXQdsMvN6KgviMyisw0-Mq06sar07ZMln0bQsxUTkZHJ4cP9x-RmgG-mlY2ZRESnwSSrSEhEAUho2ySeRhXGB2u_Z2pEB2BOFqhuLP8zcBxRV0fvUgviZYPJ41YYBaLzImmfuyW_-pfZAVB9G6aTmXI9UBvnHS7Cg32vhgvn_GcxRGIsxoTSkR72HXUu_88kOn_WN73Fjhxj2JeMOIrFOucE1U6zs0mN0nzTUvChQXgcOTVobIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4d7ccf7f.mp4?token=SgmD-VzvKBvqpArb0MNdZMtlVAA8gAcZ-EG53hp1oKe3gW2vE43F92agzoefqi3HLTtpNqoadNez9U9hKVa13NQnFEa9JH6fHyg4rXQdsMvN6KgviMyisw0-Mq06sar07ZMln0bQsxUTkZHJ4cP9x-RmgG-mlY2ZRESnwSSrSEhEAUho2ySeRhXGB2u_Z2pEB2BOFqhuLP8zcBxRV0fvUgviZYPJ41YYBaLzImmfuyW_-pfZAVB9G6aTmXI9UBvnHS7Cg32vhgvn_GcxRGIsxoTSkR72HXUu_88kOn_WN73Fjhxj2JeMOIrFOucE1U6zs0mN0nzTUvChQXgcOTVobIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسرائیل‌اینترنشنال و تناقض و رسوایی و وقاحت
🔹
دیروز: تکذیب و انکار حضور موساد در ایران
🔹
امروز: تحلیل عملیات موساد!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/654937" target="_blank">📅 09:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654936">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbueMNkypG1NjNe-pa4w9PEh6eBoY9O4ThqIWHF3lY1oSdJot3MaNQQV-P41oTVHkeNSVlBE--WcL1sZP6XR8OYB1R_0jGyBa8LcbQ_JJB0oQiAdRbTGmztWuJOnFC78FfS_R43TSvvyyW1o_9MzUIVBCZmDjfWlzr5X_zqxMKTQ6P1Ad9xX0QWkis-_q_2zWO0qKP0klT0yjBOGrvAaE2z5sk2TORNN3S2j6ekJop0aiFMXQvx3GP8t9HmmdaQDNVatDUgB03jcUjgwMpt-5tncV3NxTTYIh-KpPs5cbvcFZWzyiTi0gjzsHI2k_HHJVO8ZuEYy41U9u0tHO7lXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدارهای حملهٔ پهپادی در نزدیکی نهاریا در شمال فلسطین اشغالی فعال شد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/654936" target="_blank">📅 09:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654935">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/333fb34799.mp4?token=sI3BfbOjKfW0v78vZa62mufOO9B3LOrTZKQQWpao3rc4qB6GdxHj26oE_gZIVpHeMXNiK_Ds_GfFlkT2eytbrAUu0YdWYhZK-B5EiQBFbhXYQ7yIUwhlUXuqEFqH4kicpW_-LB8B6B49IXoAEFeyn_y7wB7fwrqpqu5qRNHaOaZTl8iqxHlEydBlJpgQmumKwIZf3iiVuesdW6gooZc8ts1hYBUNunfit-5zqVCNrcu75Xxp8N-tmtz_KOXLMOV4_UTESbgveMRXsPhuCJtpcC2MCaii6WNKcSNV3gUjdlCXSdcpGDsHrUtM1a_aFtG8qN6FP_catngC6JwrO9sTpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/333fb34799.mp4?token=sI3BfbOjKfW0v78vZa62mufOO9B3LOrTZKQQWpao3rc4qB6GdxHj26oE_gZIVpHeMXNiK_Ds_GfFlkT2eytbrAUu0YdWYhZK-B5EiQBFbhXYQ7yIUwhlUXuqEFqH4kicpW_-LB8B6B49IXoAEFeyn_y7wB7fwrqpqu5qRNHaOaZTl8iqxHlEydBlJpgQmumKwIZf3iiVuesdW6gooZc8ts1hYBUNunfit-5zqVCNrcu75Xxp8N-tmtz_KOXLMOV4_UTESbgveMRXsPhuCJtpcC2MCaii6WNKcSNV3gUjdlCXSdcpGDsHrUtM1a_aFtG8qN6FP_catngC6JwrO9sTpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد معاون وزیر بهداشت به نمایش بی حد و مرز سیگار و سیگار کشیدن در سینمای خانگی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/654935" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654934">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQj_Yt2a-BXN2fifXHzQ1fdOEg0rl7Ppz-YNN4Y4JjBa6LlBl4ofKinRljdVoKwvewkV3fQEk7mT9L7AxkI7nb94loSNHbwGrR3ctVoYeJp8lokqEGjGvx7cvenKW4R0z9n8b6b2ArvipxQJKjzsNgFFCGF_jh8lDpPArjOygnsHKBTA9QE0driIjezvOF7QFusIJEYZSb7MBmm4UyA590XcYLibs5tlnZ-gxjz-ol-l0vCnTgczdVZCI8ZAVyO1yBNd8T3kGJfa5wxD9MzaI2n6s9Ikz0n57lwRJB-St2Xo1k6QA8HoLuTX4-8Ty8XocIxpanyCEElB_Q8CgoY4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز:  تمام شد و جمع شد؟ روایت ترامپ از جنگ ایران با واقعیت همخوانی ندارد
🔹
دونالد ترامپ تلاش می‌کند جنگ ایران را تقریباً پایان‌یافته و یک موفقیت کامل جلوه دهد. اما پس از سال‌ها تلاش برای تحمیل روایت خود بر واقعیت، اکنون با بحرانی روبه‌رو شده که با داستان او همخوانی ندارد.
🔹
در خوش‌بینانه‌ترین حالت می‌توان گفت که یک تغییر در رهبری رخ داده است؛ اما اینکه حامیان جنگ آن را به عنوان تغییری مثبت معرفی کنند، نادرست است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/654934" target="_blank">📅 09:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654933">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC837SbCzyq4RzUBr9ep3sdQmb48GiEdroj8moagey66j6OHdce1opZGtUf0zbrRpaNqQXgjF0L66UXR7BAx6h63W93Y7vRgTP-pMniGYQUKcwahhGKIyis0yES7_d7C488EvgkqVMBN_AqJBbNgdVS8eDgbR2Qqz-i5WSLwpAlDHru8lcQdPlHOC2rL0vArhxoYSVVnOKmJsqh6sFRvb-iciMXoWvRsPMR6XmAMhfOT_7i67dhsEuRWH8m-N1V9YV9aXe2CwU76tP6nOKgqyJchcakQY1bm-yHzIwZrB6n8yVsejVHbajmNit3X2f0U5zkB27fCPjrXIMURp12yZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس تهران در دومین روز هفته فعالیت خود را با رشد ۸۱ هزار واحدی آغاز کرد و به تراز ۴ میلیون و ۲۳۴ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/654933" target="_blank">📅 09:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654932">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14cc54b6c5.mp4?token=VvdptB5-JcEuFrkGVPHD5kF0lX9tGPjUaK7ClhJxO8eo7dlSjthZCHFPeDkzqcrzmUdb_Ps3YEyQ05ZdiJ0FYCUuSPdaqaBeSOV_g3ahWoOdRGgrlNnvz4_hhB4C3ytYv0QmW2Xo11dbqfQNL7LIPGfRPQq4GRpr6uV7VhgGUmnnBL1fhCpPFniwlJZVfdqh_vIA9mkyU5VqZn_tNr7Tf7UNUbZAbZi_PMAexGo1TJpfhU1cAJLAjVmUCWZNGAoF02jwBgZ6eBmrRy5SeFJU--6Aw1beNvnMGqUdIuKuaRG4sxVH3FBfSh4_-D6ZL-pNrAGkOVuhTlKS7bM5-ebLRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14cc54b6c5.mp4?token=VvdptB5-JcEuFrkGVPHD5kF0lX9tGPjUaK7ClhJxO8eo7dlSjthZCHFPeDkzqcrzmUdb_Ps3YEyQ05ZdiJ0FYCUuSPdaqaBeSOV_g3ahWoOdRGgrlNnvz4_hhB4C3ytYv0QmW2Xo11dbqfQNL7LIPGfRPQq4GRpr6uV7VhgGUmnnBL1fhCpPFniwlJZVfdqh_vIA9mkyU5VqZn_tNr7Tf7UNUbZAbZi_PMAexGo1TJpfhU1cAJLAjVmUCWZNGAoF02jwBgZ6eBmrRy5SeFJU--6Aw1beNvnMGqUdIuKuaRG4sxVH3FBfSh4_-D6ZL-pNrAGkOVuhTlKS7bM5-ebLRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط پرچم اسپانیا جلوی چشمان پادشاه؛ واکنش سرد و سلطنتی فلیپه ششم سوژه شد
🔹
در جریان مراسم روز نیروهای مسلح اسپانیا، یک اتفاق غیرمنتظره توجه‌ها را به خود جلب کرد؛ پرچم اسپانیا در حین اجرای مراسم دچار اختلال شد و به‌طور ناگهانی سقوط کرد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/654932" target="_blank">📅 09:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654931">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
دختران میناب زنده بودند اگر بوش مجازات می‌شد
‌
نشریه آمریکایی Current Affairs:
🔹
مصونیت رؤسای‌جمهور آمریکا از پیگرد بابت جنایات جنگی، باعث تکرار این جنایت‌ها شده است.
🔹
اگر «حقوق بین‌الملل» قرار است معنای واقعی داشته باشد، باید دونالد ترامپ و برخی مقام‌های دولت او به اتهام جنایات جنگی تحت پیگرد قرار گیرند که اثبات این اتهام‌ها نیز دشوار نیست./ ایرنا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/654931" target="_blank">📅 09:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654930">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HitltUUp145hidHGCy_BlmDpaRx_GVQpe7iW7JJ1tm3uf0dxZoW1Tsw4XMEeC_iyPhNSplBwjTMEHjimkk7-BSBT5o6gZ3RZRxksQ1HliEG8K2OI3MamTP98GimZNBxu3qFdFYzejA7y0zi8e79inCX1o493IBk7tcbRKkShYcw9QnAeTCgzK1wGku63TBeLI5CfKOSJukquLA86FRqW5c5-CxIusw_aosrH0FbfyIuHdffsB_WqLnxXoBjzqsNTOHirkEvpX6AkEYf1SImXyX15OpkJgC1x-2YkbHcCAanR0dyXWJ3ipR6uxiahlD5K9sANnlV6v1ZzgbHY4tNTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوشی را از دست ترامپ بگیرید!  آرون روپار، خبرنگار مطرح آمریکایی:
🔹
پست‌های دونالد ترامپ در شبکه تروث سوشال طی حدود یک ساعت گذشته کاملاً دیوانه‌وار بوده است؛ این حجم از چرندیات و رفتارهای عجیبِ پشت‌سرهم را ببینید.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/654930" target="_blank">📅 08:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654929">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEAvuI4vlCTyW7istB-J6A31I8HLRy0JsQCv1jp2WH4yfUn5L839aHOC_w_vnguht-pZR7hrwVQTJ-XRQ9N7hRK29TwZSb2fM052jwvhJD3snyuI03fVhvbGxlY9Yr4G47vq0LuK3H9k-F1RzaSyZ-sqFpklVjs5Cj_zUVPkDZrklNYkrD2AUFNaGnjjaKygtVwYsMbU-eVGf-5Waq28FAL3foxNbW8baDe5h0kon8MxJgJ9BXPSf-Kf5EX9icQ67tVDQC4paMSmCDnoBh72cFZEpYOe0t_ScpHuJNvz59F2ynx0t6LumvP0JQnKCOVJ67qYrxi5RjFr65IsT-oXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حذف صبحانه با افسردگی در ارتباط است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/654929" target="_blank">📅 08:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654928">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c74b0d35.mp4?token=rIAlA_q3Eo5v46FvT8uAd0VEnU49u27zYU4P8q3RDiaVvHHGCSKJmU_G2rtVn-IZEBE-0iT9ImuUfqhfT8E364Cng5aSTWfzDLMX0A4MCZ_PO47nGMJlTgiCvOJmKjrAoFvu3FaGX9nLBDR2e2OOsxr6zvpKPaHG6_TCe_x7lX97kscUGAbk2TVS_u8OVhzEZBu1GersnUkZD82LMUJfkSDYvhoaX2sIIXic1kC-aOTa9z5eGY1Da60kIgXPFtbQGESDU90qG3Ec-H_NYUaFapv-ZI0JFZmfOUlyqR4sjjs435dZu-x346Uw6n_LfTJZYyx__iCKe1CAmxEl7XbX9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c74b0d35.mp4?token=rIAlA_q3Eo5v46FvT8uAd0VEnU49u27zYU4P8q3RDiaVvHHGCSKJmU_G2rtVn-IZEBE-0iT9ImuUfqhfT8E364Cng5aSTWfzDLMX0A4MCZ_PO47nGMJlTgiCvOJmKjrAoFvu3FaGX9nLBDR2e2OOsxr6zvpKPaHG6_TCe_x7lX97kscUGAbk2TVS_u8OVhzEZBu1GersnUkZD82LMUJfkSDYvhoaX2sIIXic1kC-aOTa9z5eGY1Da60kIgXPFtbQGESDU90qG3Ec-H_NYUaFapv-ZI0JFZmfOUlyqR4sjjs435dZu-x346Uw6n_LfTJZYyx__iCKe1CAmxEl7XbX9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تناقض‌گویی مضحک ترامپ
‌
دو جمله‌ رئیس‌جمهور آمریکا در مصاحبه با فاکس‌نیوز با فاصله چند دقیقه دربارهٔ ایران:
🔹
ترامپ: ما در واقع ارتش آنها را دست‌نخورده رها کردیم.
🔹
ترامپ لحظاتی بعد: ایران در موقعیت بسیار بدی قرار دارد آنها هیچ نیروی نظامی‌ ندارند!
#Devil
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/654928" target="_blank">📅 08:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654927">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
پلمب کافه مروج شیطان‌پرستی در خیابان ولیعصر تهران
🔹
این کافه با برنامه‌هایی با ظاهر موسیقی غربی، بستری برای حرکات نابهنجار و «تحرکات شیطانی» فراهم کرده بود.
🔹
مشتریان (دختران و پسران جوان) در وضعیت غیرطبیعی و با حرکاتی عجیب و «شیطانی» دیده شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/654927" target="_blank">📅 08:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654926">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
کاهش سن مصرف دخانیات در میان دختران نوجوان
دبیرکل جمعیت مبارزه با استعمال دخانیات:
🔹
حدود ۲۰ تا ۲۴ درصد جمعیت کشور مصرف‌کننده دخانیات هستند.
🔹
مصرف دخانیات در دختران ۱۳ تا ۱۵ ساله نسبت به ۱۳۹۵ حدود ۱۳۵ درصد افزایش یافته؛ صنعت دخانیات به دنبال جذب نسل جدید است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/654926" target="_blank">📅 08:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654925">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک مقام آمریکایی: توافقی با ایران حاصل خواهد شد، اما زمان نهایی شدن آن هنوز مشخص نیست
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/654925" target="_blank">📅 08:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654924">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS2BP-8C-Ma5YhPFDK5SwP3xMs0_ramrXvXprRrAWyuyVueK5AH2naHxIAoXPLQIuxiUo9X8Rk53aSwNpB0EsvAJxpBsW0o4CbUbwgHbzc2wxzWYgCEP3j69-TbamjcjGVG4E8cvseenrIzyC9px85a6zPcCNlVa9Sht6LDQgMKpdJJw4oJx5BvBUlS51XAd763wvrSZFqWvNqjB_yMTUykMOnOnxalMn0b6eG4wzxJXQ2uafhmmqfqzRtVBagTtoVus5vz5juurB2wrJxNkdC4ZSRw-bMCrgikafgR_KppNmdQQnU1n1HfefEYCDrkeo2oX5r6ifTM2of-IeftFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاجعه در دنیای علم؛ ۱۴۷ هزار ارجاع جعلی و تقلبی فقط در یک سال
🔹
دنیای علم در سکوت خبری، بدترین بحران اعتبار خود را تجربه می‌کند. بررسی ۲.۵ میلیون مقاله نشان می‌دهد فقط در سال ۲۰۲۵، نزدیک به ۱۴۷ هزار ارجاع به منابعی کاملاً خیالی و ساخته‌شده توسط هوش مصنوعی در مجلات معتبر منتشر شده است.
🔹
نکته هشدارآمیز این است که در حوزه پزشکی، این تقلب می‌تواند معنای ساده‌ای داشته باشد؛ مرگ بیماران!/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/654924" target="_blank">📅 08:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654923">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8db579356c.mp4?token=owC04zbJHTipoAVpf-KOXMQkF4hJ-UnBQPP5DGPEWES_AsfeWxcY6yxjdHrxJGoSWRp7P9OlmdQ2IwrIUQazM7MsTUjTrxZ8ygeUVqZ5VT880v3SDQHONvn66Bif8mdIeFA1Z_08i877FoUJG84yfr_3cnbGAg17JmmcdiSVMKhXMMffKPV0dvpBwHiLu8ofjK5QpxCj9QGUuAy8REtI-73FbI5wrRoTtIjyJjMk7TSbAnQ2KXE6HlWuQMrIoIU5MrKVgupGDfr-4Qbtk6cZf0CP02gIKkXI_bhuVQ8Ha-Y-mteOB-f1Lv5X068pbs3e9PTOAuoolcUkgN_UOwn-u7m8Lk8U2hOi-_LeJjeX0o9l0KBT6hL14yQE1MqgSgy3_J7FoGLFGId9jUNWCSnTXLLqEY8hDmMSkNpXXEQQcWE8s5mYNL2niXuFhD280jGxbLUDYcbRc5OpGEyRF6ZwWXu-tVmhPfdMWiABNp-C1Yzp1vCukjVvQKNASUmWDqiHMhf4rtnNP8SvEsy7zV_OcF3LH5QQS5T03EIpnF_t-r5qj6xHVVKyU0cuIgb_9A1A577ozFB2fZKxIDF7iakSrVA4avMfjnWiB9BncnpsJ2KR_DgjE93Q5d737mWA3Ml2q_g47DWQR5g2MWV0L3XiqweYFi0LpMIjK6AGiakeODk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8db579356c.mp4?token=owC04zbJHTipoAVpf-KOXMQkF4hJ-UnBQPP5DGPEWES_AsfeWxcY6yxjdHrxJGoSWRp7P9OlmdQ2IwrIUQazM7MsTUjTrxZ8ygeUVqZ5VT880v3SDQHONvn66Bif8mdIeFA1Z_08i877FoUJG84yfr_3cnbGAg17JmmcdiSVMKhXMMffKPV0dvpBwHiLu8ofjK5QpxCj9QGUuAy8REtI-73FbI5wrRoTtIjyJjMk7TSbAnQ2KXE6HlWuQMrIoIU5MrKVgupGDfr-4Qbtk6cZf0CP02gIKkXI_bhuVQ8Ha-Y-mteOB-f1Lv5X068pbs3e9PTOAuoolcUkgN_UOwn-u7m8Lk8U2hOi-_LeJjeX0o9l0KBT6hL14yQE1MqgSgy3_J7FoGLFGId9jUNWCSnTXLLqEY8hDmMSkNpXXEQQcWE8s5mYNL2niXuFhD280jGxbLUDYcbRc5OpGEyRF6ZwWXu-tVmhPfdMWiABNp-C1Yzp1vCukjVvQKNASUmWDqiHMhf4rtnNP8SvEsy7zV_OcF3LH5QQS5T03EIpnF_t-r5qj6xHVVKyU0cuIgb_9A1A577ozFB2fZKxIDF7iakSrVA4avMfjnWiB9BncnpsJ2KR_DgjE93Q5d737mWA3Ml2q_g47DWQR5g2MWV0L3XiqweYFi0LpMIjK6AGiakeODk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی را از دست ترامپ بگیرید!
آرون روپار، خبرنگار مطرح آمریکایی:
🔹
پست‌های دونالد ترامپ در شبکه تروث سوشال طی حدود یک ساعت گذشته کاملاً دیوانه‌وار بوده است؛ این حجم از چرندیات و رفتارهای عجیبِ پشت‌سرهم را ببینید.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/654923" target="_blank">📅 08:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654922">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4971def66.mp4?token=FlK2H7gQHFpWjyd_sWgKyuSTDkdYWG5-b9oCdqjMhMFZU7grbmHeaucpbMaVrrDrmEBf8O6MgdJSSsT9veaVZk7UPoJ2JF_JH2_XNj-izrf1HhJTRUoIIiXoKbCMTWLSCgUGJQMRxSy21z4_uaNiUsYuuRBmxmUUxkeYv-mGGGDp1HUZ5jtKVGd7Kpi9DqrpgCjkZo8mNeKsynJIv7v92IebZWLbDFxIKtdiaJGfm8p57UOCw-W8Zu9tLpgTH0RyikSgnZxqfxOJ01mMt4e51QZwKi5lnfs32BhorOCgqzIPwKqCp3WrVhlqZUN23whuV5StTSkmVIYAwZgAnuT9DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4971def66.mp4?token=FlK2H7gQHFpWjyd_sWgKyuSTDkdYWG5-b9oCdqjMhMFZU7grbmHeaucpbMaVrrDrmEBf8O6MgdJSSsT9veaVZk7UPoJ2JF_JH2_XNj-izrf1HhJTRUoIIiXoKbCMTWLSCgUGJQMRxSy21z4_uaNiUsYuuRBmxmUUxkeYv-mGGGDp1HUZ5jtKVGd7Kpi9DqrpgCjkZo8mNeKsynJIv7v92IebZWLbDFxIKtdiaJGfm8p57UOCw-W8Zu9tLpgTH0RyikSgnZxqfxOJ01mMt4e51QZwKi5lnfs32BhorOCgqzIPwKqCp3WrVhlqZUN23whuV5StTSkmVIYAwZgAnuT9DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست‌وزیر لبنان بالاخره از خواب بیدار شد؛ نواف سلام: اسرائیل دیگر فقط مواضع نظامی را هدف قرار نمی‌دهد / کوچ اجباری جمعی بخشی از راهبرد جدید اسرائیل است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/654922" target="_blank">📅 08:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654921">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUUdzXT_4przSkFbyZmH-ZG6K4BejmH64cFu0kn8gPrtEZLJi41wzP298_rT31_betr4zgvdLjCqgqAOuBjS5vU4V0kquySgmdfOAasN0NTZLBr87sNRKeMmuQlz5duscosWSsDXj62K-K-u-dGDGTJotk7rowZ5U3IzwUhSYdqr1rz19GSuX-hzC4et7naicQKYGLHsB9urJ3eDXsl-KVaAchTfvoCoDmLb67X-G17vFz6BO7pPAFks1dfT3ULaAneyzI-MwK5zBKvxEkHhzmIUtsXqR-B_kevp522v6Vceg7aODx_qcyIBzBJKTzioeTpo-pY6Oet29uC4z15Igg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخه جدید براندازی نظام ایران در موساد
اسرائیل هیوم:
🔹
موساد در سال ۲۰۲۱ شاخه‌ای مخفی با هدف تغییر نظام ایران تأسیس کرد که رویکرد ترور فیزیکی را به نفوذ روانی و سایبری تغییر داده است.
🔹
این شاخه با ماشین مسمومیت (هزاران حساب جعلی) بی‌اعتمادی مردم به حکومت را افزایش می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/654921" target="_blank">📅 08:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654920">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2ImM4T0DUOz1AakhaS11rXiFFa0VHOmkgDCAkH1Wibl7wpMeHeyeejYBt52PUvzVq9PBprSss4siwTquJDfNa4aPQFLpK2aIFNCZdefpiXgSwirW8NxAvZmcuN9waWobOZ4OhG_kwS8QetmUeTKeZUVgLIeyIMy68cfjl84xPFSr6BnVcdV0WW5-vga79y_XTmOEdt7zSY1kpnuV4RRf6KIadGGCthnWo8bGAhW50MVJaOON2jcGgkFWL2PJM6cuS32lkbt4DH0QjiboJeSxaFqJTPJzTM3-6RzpIfLiOvxQy0zlotc9lglrkU-uNi3THa8eJqCblFsaJq8-MWF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حرکات اصلاحی برای افتادگی شانه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/654920" target="_blank">📅 08:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654919">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک مقام آمریکایی: توافقی با ایران حاصل خواهد شد، اما زمان نهایی شدن آن هنوز مشخص نیست
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/654919" target="_blank">📅 07:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654918">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30655bc731.mp4?token=cemvZKozWXK_6x4yfw5swf4gY_cbf-T8J0erJ_2TZu2jGhKP-pTWjNxhTHDLGxdp29Pzl2aJ88DrWd4P_sDSQbTDsCxsj9SJ8oP0Ml86TXRjp2mkV63w3tAzXhOTxslItYJxBHMC2UVQyeHekzauOSY7eOcmB_wxWguF7Cfd9ozy7SytJ65WLD9s6mU2B1k9XT9hZFtLyawPZhxj_kWJGxOYe5Qgo6AOeq7NkTR7yVIAVYgpLbcFr_HedufZ3S6SgQGU8lPnU-9fs5MFa93qD6SBn2OiMXL5hLU0_MAmfFHDRkH2sLITlOyVl8d-95mU67TS3hNdu1YqOVeK11fLPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30655bc731.mp4?token=cemvZKozWXK_6x4yfw5swf4gY_cbf-T8J0erJ_2TZu2jGhKP-pTWjNxhTHDLGxdp29Pzl2aJ88DrWd4P_sDSQbTDsCxsj9SJ8oP0Ml86TXRjp2mkV63w3tAzXhOTxslItYJxBHMC2UVQyeHekzauOSY7eOcmB_wxWguF7Cfd9ozy7SytJ65WLD9s6mU2B1k9XT9hZFtLyawPZhxj_kWJGxOYe5Qgo6AOeq7NkTR7yVIAVYgpLbcFr_HedufZ3S6SgQGU8lPnU-9fs5MFa93qD6SBn2OiMXL5hLU0_MAmfFHDRkH2sLITlOyVl8d-95mU67TS3hNdu1YqOVeK11fLPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف رسمی راب مالی «دیپلمات پیشین آمریکا» در گفتگو با بی‌بی‌سی؛ جنگ علیه ایران، غیرقانونی بود و موجب کشتار صدها ایرانی بی‌گناه
گردید!
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/654918" target="_blank">📅 07:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654917">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
رهگیری و انهدام یک فروند پهپاد دشمن در آب‌های سرزمینی ایران
سپاه پاسداران:
🔹
بامداد امروز یک فروند پهپاد MQ1 ارتش متجاوز آمریکا که با ورود به آب‌های سرزمینی ایران قصد انجام عملیات خصمانه داشت، بلافاصله در رصد و هدف موشک‌های پدافند سپاه قرار گرفت و سرنگون شد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/654917" target="_blank">📅 07:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654916">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اجازه آمریکا به کشتی‌های قطر برای ترک تنگه هرمز پس از پرداخت پول به ایران
اسرائیل هیوم:
🔹
ایالات متحده به نفتکش‌ها و کشتی‌های حمل گاز مایع قطر اجازه داده است پس از پرداخت پول به ایران، تنگه هرمز را ترک کنند
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/654916" target="_blank">📅 07:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654915">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bc563da99.mp4?token=ecjZIAYumnSiBs1Gz0GUUaEv42DRLevIAwSBXhKGl_Y7QOvNfNH6f68-eQxeW8SA-hfobDRQ_gYP2XCeCRykdFn17VwI1okWlsaz39z2pVoN5uEC6GDynXbeSfDnYhdhMY4EFkNNJzvuPCVI5wDqYXkVyqs9cLQmpNaUNcRIAmOUEyAT37iJq8dkyIObzQhRZIVtWZNfFbYkDFYiGzcNQfmOjY63_JhGeJ8gMPwMkPBWCcBpQXOHA-_mRlp-D4i4wjHYSzNgSA8tYG4ZF9otUxh-GNqpMKZ_Ma0DHLrMEGoOTBCM75h6A8gSQKn9oyxFxm2cCgicE7CgX-pDkojeJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bc563da99.mp4?token=ecjZIAYumnSiBs1Gz0GUUaEv42DRLevIAwSBXhKGl_Y7QOvNfNH6f68-eQxeW8SA-hfobDRQ_gYP2XCeCRykdFn17VwI1okWlsaz39z2pVoN5uEC6GDynXbeSfDnYhdhMY4EFkNNJzvuPCVI5wDqYXkVyqs9cLQmpNaUNcRIAmOUEyAT37iJq8dkyIObzQhRZIVtWZNfFbYkDFYiGzcNQfmOjY63_JhGeJ8gMPwMkPBWCcBpQXOHA-_mRlp-D4i4wjHYSzNgSA8tYG4ZF9otUxh-GNqpMKZ_Ma0DHLrMEGoOTBCM75h6A8gSQKn9oyxFxm2cCgicE7CgX-pDkojeJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه بالا بردن جام قهرمانی لیگ قهرمانان اروپا توسط مارکینیوش، کاپیتان پاری‌سن‌ژرمن
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/654915" target="_blank">📅 07:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654914">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
جزئیات ثبت‌نام دانش‌آموزان در مدارس سراسر کشور
🔹
پایۀ اول ابتدایی: اول خرداد تا ۱۰ تیر
🔹
پایۀ هفتم: اول تیر تا ۷ تیر
پیش‌ثبت‌نام مدارس شاهد:
🔹
پایۀ هفتم: اول تیر تا ۲۰ تیر
🔹
پایۀ دهم: ۲۵ تیر تا ۱۵ مرداد
🔹
ثبت‌نام پایۀ دهم (عادی): اولویت الف ۲۷ تیر تا ۱۰ مرداد، اولویت ب ۱۱ مرداد تا ۳۱ شهریور
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/654914" target="_blank">📅 07:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654913">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ کودک‌کش: به توافق با ایران نزدیکیم؛ آن‌ها نباید سلاح هسته‌ای داشته باشند
ترامپ:
🔹
واشنگتن به «توافق بسیار خوب» با ایران نزدیک شده است.
🔹
«اگر منصفانه نباشد، آمریکا به وزارت جنگ متوسل می‌شود»
🔹
«طرف ایرانی با عدم توسعه یا خرید سلاح هسته‌ای موافقت کرده است»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/654913" target="_blank">📅 07:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654912">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpfrfSYV5NHDhgMtRXGkeiSJNTh1QogHc23MIzbTAKrOu89Cej3f4qlj1Hu2BRl9Ko5EkbEEvXi9dGG8aPgruUz1-6Qswh-fa1iN5Xrs1yFw-laotrhU67RvqHm7JP7bdFNUNzEBZxf0z5SFALce-Pg58vSyCGnxyxQDrxRuKWK6wEpH9eOjIxccAfhFDTBoD8aKbAIAjzcwszxxtp5nHbhIJwZjx9eyFdTLMMWpjBAwFasCMBFlM9ThEhfurkt8KT66uymf2YxooOl2INpKIyOPeO7IwIgvX1HcjWK3gz5EP274Srt9nADRyP69F42eJAI5KYmcf8Xy5LP2K_Y9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۰ خرداد ماه
۱۷ ذی‌الحجه ۱۴۴۷
۳۱ می ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/654912" target="_blank">📅 07:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654911">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0Eyw3H4W5qJ_d8GRWu84bK45ZvI4s5XHx5f8hO1Wn8FHqbkO4BbvK5g5ae4ky0OW-N9mItbWX0WPWeSt6NifQ8WDG7clM_JK1ckgWhpQ9O0qJIzKLcQV5pQ_Wk01G05gpCSxRwvF0ad53AzsDRce3LLAxU90jAuEd_09CjxPhHD7VGwpk5VBdN46cUr0deyD1zFl6WA41afiqML_NEImH9czQaTzlLY9b5Wq-OTPpSGvKEd0bwhIKDvUjuw5-AW-VvuNAO-Lqhq7MGdqArk2XSu2R-rzUHcDQNrYU-vvJlPxW6Wjt2d4_op4VgHTgokCwpgDpCdit3kofEAe49UnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/654911" target="_blank">📅 00:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654910">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9A755W2WF6NrkQZL_QsqK5RV_QSCGEZ7ZYNZPqruabpVYzE4BmvwRKwbpzWft8ktHK6hjoZI30tg4iEYV131wArsHojjMc0gRIAcxH7xJGTrFGYeKHdYGmFf9SctW7WKI2KkIG6QcgT_Z4tEEId_fTjf-ILqssLSxbLV9WSxUT-zCGfre5T4WjMYQYUe6qIzGnYVVhlxRG63GEqvqa6iwtohcMpSA2R68Jt49jubEBSpoALPnr_0zOwsZAuSOn_I0parGUrx66Xzv4GXXyn1ulZpl92bVm1U-VSfiEMl1Kd8l9iVuMMxuNUzGRAoGWwNDRR3HaEcHiEssWulAISUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اجاره کشی
🔹
شرایط کشور باعث نابسامان شدن بازار مسکن شد به طوری که بعضی صاحبخانه ها غیر منطقی نرخ اجاره خانه را افزایش دادند و از شرایط موجود سو استفاده کردند. در خصوص وضعیت به وجود آمده وزیر راه و شهرسازی: تعیین سقف افزایش اجاره بها به میزان ۲۵ درصد و تمدید خودکار قراردادهای اجاره به سران ۳ قوه پیشنهاد شده و پس از تصویب ابلاغ می شود. در حال حاضر بیش از هر زمان دیگری نیازمند همدلی مردم در تمام امور مخصوصاً در بازار مسکن هستیم
🔹
هفتصدوشصت‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/654910" target="_blank">📅 00:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654908">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfqtxKm7316yTeZOzwWxxgIDK0OcGhxzBDUPaTX4cklZ7lMEfoWBugM_B9I6ZlVNiinj7ZhWiEpsX0o8Bl2C39DbAkZIFsqLTYh-BLeKoODpyWEjKaSXlm_aMT4Ge59mRD4zb_aHWD64QcZGWrGDDeFdcEUOBbc-_I_AhZhXNC7aXk_VdnVno1pT935PUdkXc_SdBw52aIJp0dP43fJ05uRuyLovPCH9Thx68fDV34840g9DAo_N934YTbeJwgHJD70lrd0fXHiuPM3JPc2KaOKkH7ZToMmfqInInY_WAwS6iZqmJw_S_8CW85qg4WsIfaCLcUgTL-3CUQt9CxMiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر دیده نشده از شهیدان: سپهبد محمد باقری، سید حسن نصرالله، سپهبد محمد پاکپور و سپهبد حسین سلامی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/654908" target="_blank">📅 23:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654907">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8n2TlvxH_vU78-wYzjMnAqCoZjdaDh6XyWKMUbm5qruMD1nbgETck8URoa7bb_6Olm77_EsJ6CiyUENk4BhUeAWrc8RhOlwMy1T5YFvNbTLn5B8hqZ4h9GyXjL4I-2VolwrnsgBgVF5uNjC0rnftfYdUYLmxEBrq2MAq2OHtNEQjlRY4J3RGrkP_poLF6JxzqpYM0E2p3FySnXYKdt6gBAJp6HSNE2VzWKX33zRbzyeRKyk4Yoj2-I1qhDIbTcoL72ZPotH_4fcH3pZOQYmoi1w7gYInnd6smA3IIB3oTqwsy8BtRNR5O9URlS93J43IQUctCQwwBVX35TgdFTj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ چیزی که هیچ‌وقت نباید دور بیندازید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/654907" target="_blank">📅 23:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654906">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac963e4575.mp4?token=XKp_bLQhQ_5yZ_iYpDLEYWKEBzLkAapBPKTjAwauI-zW4XvO_KHI5Byy44-SOdEP-hnfB9qcwvKbJ-RckjFHcojRq0LKhs9_-gwb0spIoy9i7kFkxMXJKW1V2XhihXZK8BLvpHJqnooEiATSXHowsJmGChmI76u-n496Qq_HdiNCcGJpDvmTQCcYRwMWaNhaaMgevJccFI2z_dQgZvcosRUiu9V4E6jAT4qVxs74lAskDqZ2XbI0GWFZRBgjzXCfdbffBqZxbIFyYHIlPzQrGaX-X4GTWDe5ILcqRtjfZvbJWhlRNOyT7_31OjZCK0PdtPwgZ67KSBfFEtq94DA0ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac963e4575.mp4?token=XKp_bLQhQ_5yZ_iYpDLEYWKEBzLkAapBPKTjAwauI-zW4XvO_KHI5Byy44-SOdEP-hnfB9qcwvKbJ-RckjFHcojRq0LKhs9_-gwb0spIoy9i7kFkxMXJKW1V2XhihXZK8BLvpHJqnooEiATSXHowsJmGChmI76u-n496Qq_HdiNCcGJpDvmTQCcYRwMWaNhaaMgevJccFI2z_dQgZvcosRUiu9V4E6jAT4qVxs74lAskDqZ2XbI0GWFZRBgjzXCfdbffBqZxbIFyYHIlPzQrGaX-X4GTWDe5ILcqRtjfZvbJWhlRNOyT7_31OjZCK0PdtPwgZ67KSBfFEtq94DA0ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار مستقر در بیروت: اسرائیل خیز بلندی برای اشغال شهر نبطیه برداشته است/ دشمن در ۵ محور در حال تلاش برای نفوذ به شهر نبطیه است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/654906" target="_blank">📅 23:54 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
