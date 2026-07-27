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
<img src="https://cdn4.telesco.pe/file/QrvxPEjXiB2H_zBMRtR_LJlirnrMhl3U5xR96ve-ivnlP77LXSdtOBsS3DqJTdwQjTSJ6dSehNhGDdtBTLq0v_4hlvw775mlqgSackhzhMQww7rjKhLhRFNF8Kg9-01IxlLWWhcE7r23s3MeQLa3VXZGGTgkoqxpgOEmlX-THh1GSqFA35SPOO6oYSMOEgJfgYcOMRoB_a_SsRTPl7YbUxWCkmRIEaNlJVA1xDZBNrsj01VolEWxDcNsW22fOwI3F4ToC7ioNuJk67YJIQhJ8sGXhthXqMFyOKhsNM8fnipTWz5dLAr7xJ4BHUrf0-Tylk5Wd1sM2Z5VMzNe-2g36w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 147K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 12:21:40</div>
<hr>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Ae5PT8gUezxTIk5pw6H-_Npx8BT5WKK-EnKuYF0o_rqwwBaxx2UtmYvwtS5PZ8h0AMAh5GXaIOMZIipyx65TpaDA7gH_FMUpE7z7v-B684_394M5JuTDZUny9o7EkAjL6i_bH2A-nGMjjxCZ-AIdLy9P2Pfl0_8LAcxhfz8E8IR_I9_w7jyuWp6cziwbHuiq9dfedqVp1IrFhKY3pEqw3ruqayrgrGcb4L2OGSsCmgZ7T6lmtMmH2UtFcQ93W9YIOtcT_xSAgQGxeXzT3NUnOF805g05q6-10GYNDJAKopc5ZmSYZ4swNkZw23vDuVsr5DOnqyrstw7ivdJRgVs1F1jcM-umYkB1cQjeZa_YjekvmwEUUijaLEkZwEpEQfAjVO3Mz3ZW_e6G75eN0VnjoY_Z-nJs3WnkBye-f9lqyKoZb2mwSvfAbXdr4TY_iUaeiFkjUUd4yT1atTnfqsHinFjWZ_r7G8cu3MEDoqJcSBy9_FBrvGpA5_6UQWJzx9sXAf5vhHGa06-XQAa5T6XL72ZR-SoZYgL1_4ajmBwsr3iVL5KHvzMxIB1ATLSmiBy-L2tRa7RmCtvolUZYn3qZ_4IZaIX_PJWsz_m0CVnt4ldS7UtER6phJ-m58vg0Cy-3kWv5chCwUCJVLJmGIkYVsCM2qJOGjr9L5nfnNCKn5s4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Ae5PT8gUezxTIk5pw6H-_Npx8BT5WKK-EnKuYF0o_rqwwBaxx2UtmYvwtS5PZ8h0AMAh5GXaIOMZIipyx65TpaDA7gH_FMUpE7z7v-B684_394M5JuTDZUny9o7EkAjL6i_bH2A-nGMjjxCZ-AIdLy9P2Pfl0_8LAcxhfz8E8IR_I9_w7jyuWp6cziwbHuiq9dfedqVp1IrFhKY3pEqw3ruqayrgrGcb4L2OGSsCmgZ7T6lmtMmH2UtFcQ93W9YIOtcT_xSAgQGxeXzT3NUnOF805g05q6-10GYNDJAKopc5ZmSYZ4swNkZw23vDuVsr5DOnqyrstw7ivdJRgVs1F1jcM-umYkB1cQjeZa_YjekvmwEUUijaLEkZwEpEQfAjVO3Mz3ZW_e6G75eN0VnjoY_Z-nJs3WnkBye-f9lqyKoZb2mwSvfAbXdr4TY_iUaeiFkjUUd4yT1atTnfqsHinFjWZ_r7G8cu3MEDoqJcSBy9_FBrvGpA5_6UQWJzx9sXAf5vhHGa06-XQAa5T6XL72ZR-SoZYgL1_4ajmBwsr3iVL5KHvzMxIB1ATLSmiBy-L2tRa7RmCtvolUZYn3qZ_4IZaIX_PJWsz_m0CVnt4ldS7UtER6phJ-m58vg0Cy-3kWv5chCwUCJVLJmGIkYVsCM2qJOGjr9L5nfnNCKn5s4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW2Q3N56kec2IOBIner8y4HmSmILluGaNwHntKycY871xHOSeKYBAj1a4UB9le8XQ8_yyGghMSGI5msmM-mo1zYYOjg4IGac7jfc3UMqQDTrd2tqXtsT9YLmfWhUQDPuf5DH_6hUKJKgjQx_hRIsVAW-uZ1B15mlPyXGBBeRcSBCqMX9XXd0KZM6h5FzYxKaxXGcYwgCEJalraEkq0LZrnxMpVEk5LK5lGSwJTwJITdWXzP-odFvY1zri6gd7EyuI2TjxBptNNoQGADP07yWOR7LtwhpRipmdNqLfWUxGXVff0be67C3Qv1JKV0YhgzEksMLClPV2ywEuF87K_UX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Qo8wqHHlw8u9Qdl5VMeTpTbsKwQwMdhyEZGbywzXzvt7gyvrVJsshrH4lnmZbXhkfA5-7ca5IJUcoD-E65xpnkhmUxtdhs2J_2EIHHcIpbwWqIqSjDtaUiO6g-mHSoErhgsF3VtoQwo1n5W4DtmgXWDgxoG1rRnEBw1kBlkJ1zw3tl3XDFXXsWI0NuCg9IAggR-q6YT-ufCnMEoQ3HEw1fn8cqPWZ35BZ_lgCnfP9PLONhAEzEzymt_gTsGEdcxZSMER3jf-aayQTLJS2qaON09bKsc1gwGoHQmbosHZJI6jh6wjQk8KfrGPetvGOyd1EqOeVnqgfaNUQvoD_xDCwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Qo8wqHHlw8u9Qdl5VMeTpTbsKwQwMdhyEZGbywzXzvt7gyvrVJsshrH4lnmZbXhkfA5-7ca5IJUcoD-E65xpnkhmUxtdhs2J_2EIHHcIpbwWqIqSjDtaUiO6g-mHSoErhgsF3VtoQwo1n5W4DtmgXWDgxoG1rRnEBw1kBlkJ1zw3tl3XDFXXsWI0NuCg9IAggR-q6YT-ufCnMEoQ3HEw1fn8cqPWZ35BZ_lgCnfP9PLONhAEzEzymt_gTsGEdcxZSMER3jf-aayQTLJS2qaON09bKsc1gwGoHQmbosHZJI6jh6wjQk8KfrGPetvGOyd1EqOeVnqgfaNUQvoD_xDCwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToFNKrBPP-FwnkbjxgYubi1zoHJ5rozCxD0KjuL923o3lCeLhkjJIBksUKbwJtlIRBAxAopvfOHFr__kdt208UT2m42-MqERjO_gaKT3nRAsGWujuMPuD-dDQ0r9VfsjoM0ByBzTNaNW6NTAHIel7zgILVm8TMVvv0zbNCUl1OLgv_p9Hrd5BH02OJvPBY6NL7mH4JS8Ucl4CiwaWpDCq2N78fgTBup34O4rgp-k5mYJkm4voijkxmK8oK1QYw0pTHXv-SBgN4mNZeoDhpnzOMkb7EH968AKp8k4bNSvO6tS7ak-RU7l-BJArhs05eMalzqWoKeoeX-vl243_zEDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوش پرتاب میثاق ۲ / ۳ دست نیروهای رژیم جمهوری اسلامی:
⏺
نقاط ضعف میثاق-۲ و میثاق-۳:
برد و ارتفاع درگیری محدود
وابستگی به خط دید و اپراتور
آسیب‌پذیری بالای نیروی شلیک‌کننده
محدودیت در برابر اهداف سریع و مانوردهنده
عملکرد ضعیف‌تر در شرایط بد جوی
محدودیت در مقابله با پهپادهای کوچک و کم‌حرارت
ناتوانی در درگیری هم‌زمان با چند هدف
تعداد مهمات همراه محدود
فاقد سامانه دید حرارتی/شبانه پیشرفته برای کشف مستقل اهداف در تاریکی
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h-mny9qaFlhJ7Jn8ao8wFQ9ifyQzjt7-lnHjOn7WOAG32fb_NzPxwe7t3DGZcep-QV7T2xZve0MKiuSfLo2Vt6s2N9sCbZy6EIIjHmyV5TzWTideKlMU5GaEV1P7N8LIi2Eq2bE1Uu3etq6R0ZaAb7wRyEF5AnX1XLyzKlUw581S3bxNqQzefnmCZr9tn15tZFKncjgdYABOTUx7Co87G19pfQTKwvkwb1vaOSOz_1OC0DwZSIpy4WtlgRKlPBhrWriTpFmBBmCjUiOccizTIFD8XslDKENJvohxUd3Af_QSsuNUu7FEZqTC4oE2AXcV27SUXbA97J0P8uCFKd1NIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p1sCX9o0tHaU37cU8Is6ijgJUtN6Q3PcYmGYIpFUXr0d1E_aqN0P1NE97-xSQ3pnh5txY0Sv5ifuMvm_8pZbX0xs_w1SGpWRCJHt9JxwjRmyD_TZNuboouU0VBQGj8lfbTF7GQ1U7dWdh31n9aBjNmJy1mHXbfNSqr4_buQRiQOllG8i1_HbD8tIBiGJEryIR1Jhrj3Zr8uhmRaEH4etfu01NAcuSmfwM7RtyGqOwdNQ6mV6lPm_Wgg0oqBRwuQn90DmihB4MRijc-R5SevYv1e3UV9IdVTC8Yw_4YHqAtruFrSVPp1Ew35NeeLsP93LXjFXTBMSOWbuQu6WeAtfXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sdm5MygwAxl-V8q-q9x850WIvECrnRVaCJIFTF4eVCoFSx46jg047Lm_KFQ6d-1Bus6oSZp9ae9f4ygwbqhGYo-INmbe9CQuiPMx7YWgnHyx3jZqMS627jLej4FC-QRvD2NenRwMFbm4wD5jj0GYZ306-1cjgSCcS2P7hl8n_XWVscRM12HT1gNEk8I2-WfATblP15mbQ4_hnvYM8_8dwHjSa-TA6j5HeziF1fyxcMD6Q5N9hHetYOmtdcFnY9acF_OeMXmHYKKUuvqkRM7q9Hlixzeu4yz5T5Y0xdihadve3A4vOURcBfPplTXMt7V5wqoSb1hSoyi3OhGoskCeuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sdm5MygwAxl-V8q-q9x850WIvECrnRVaCJIFTF4eVCoFSx46jg047Lm_KFQ6d-1Bus6oSZp9ae9f4ygwbqhGYo-INmbe9CQuiPMx7YWgnHyx3jZqMS627jLej4FC-QRvD2NenRwMFbm4wD5jj0GYZ306-1cjgSCcS2P7hl8n_XWVscRM12HT1gNEk8I2-WfATblP15mbQ4_hnvYM8_8dwHjSa-TA6j5HeziF1fyxcMD6Q5N9hHetYOmtdcFnY9acF_OeMXmHYKKUuvqkRM7q9Hlixzeu4yz5T5Y0xdihadve3A4vOURcBfPplTXMt7V5wqoSb1hSoyi3OhGoskCeuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5y1a2KLuM15rJ58ws0N-_7TNYsk8hCVtYvu_WTpN4bvuVqVm1exC9lGsq0FVYID1hqr3pT_5kGWC6ZaHulBhKarW2ge-g1sIw8e0Gm3XtL0Hs-jBkCOT_PL2aYoEcHQMb1xdb6p5fJGKI728c4v_pc-dvWYU3fQc7fgMws_4nxP6SzcThO4xL_nymww-yjZoZXpnyGuVwT9sVICG_VmgzEr_Nq4vpRh5BtENJV8cRLnIkhWIc82zj6y2f274w27ovyTNJ8sO67jNjfIQtEr0kGEuH995rTwqI30S5qG92F9CRPF8QGVkLSl3SD-7iHCmXI4RJPxLRBQKyA-8eGyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUOvCvOioHaohVvdQUwqFVFlrf9mDr8052V9KwPk7siJ1p6Yu42xkKfaBWY2u2yr1mXYqnxTTZN8bDEaWtxpA2UmX__c_AnWVHhS68vJRvl-7oIa8YXIm9A98w6o63JsE4dYknj1zAf-KQAjqO7CG7iM7GNxkSCXFerdG6oiNR0Vk04qWUu8J9uz5_St0aE6PRvfmzHiyWxjJlBUMIkxcAVvT2VlxKI3U-2u-BU5nSoBV2rpJc8VgbCQO7K4r78UG0lxlbJDha9JqQz1QjcE3CgXffTXvO7kPX7iJhZGU0HVz7wX2G0i9AWboE2SJINersqSNqEJmHgDBQiyz5g-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6gYhEugDIX-Tww12P0DzcSg94evEWu6syKjA5r6h_DGl7pC3esHrPn01nDfQOypTn7Wtg5OdZWVt_pF6PIrzA3yGiBA6ED7jEFrxdDYzNaAcOcn_E-kCVvDIZkbwKSCZlObWuwKAhED2R7o4RWFv1kmGd-2ctWHbf8FX04S0o0NdNWQP0Ou0KFWxPvQWLPhTO8OTC5WXQH8U6Cnk_Cu9npGzCCug5qGWsagpr9RVmoq1JyYhh8ktHMJecmCkEI2kNatrNuSyaRPdorr6cRlbCQYOrPPGSkRqwIhhECA2Ddow99s-Wkx1eW8kVIuE0EZlaJALm-XXMcVTwQn5q0mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDvMdlkfzDheHcMPeLoYmRVALTMV78kx_rSxpNdhCUapv95RMTJG1dwtRk0nyvQmhMsRJfQuZHLTw_XyuFYGv_U9A9bmZKabtCAH-h3DcyQtYP65gAJK_JHE_SYfoMTMP3RsTHWWHPS570yIGE4MK6BcvueLia5vznIY4qbA8ms1vw8G19DxGEOZL6HZ5uQstHrx3i3OgKp1XrPZHTAz81IC_5qcu-FDgYZ55FFQR_Bp50cVmfLx1UC7q40qYrVkaoqTBjBNGl8M4apyqWgSiOXyHTkVgFPurM3PJD6tWnAjzoHcEkgd5tOwXz72j06k6C-3yoylnFkEPcahxTyu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qk_mK4qzor8fxJLEaisia8lHgXZlkfDvVRcerwiWCwfwj82mpMbzI1mJu5QNHhHuO34kLm0rxguEgHikSTOy1kbcveATi3RYHjnUR7uTs1sF81iQ0Mp6hSotvwyZwLytPSHfRIH4Y9CdPLIw7RcejIxsBu-Ct5bJRCoWAHr8ExMVVCwQ3H8uPKnDJzpMwQCyA-xVdOM8WGNhtoA34wESsVkO8856SW0FbWRaUq1OVWxBTPJiYfHEvrwgWOeS0rwSZSfdzQMQ4SwXPq8Y6UXPFlDuBDYKXDq8GWmETHgV7aCdswTGJAyOWLDPDP7t0_R8011Vfz7mhA6MEIAPkaXbWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWMWlgvAbtND3FeNR56bbRbzSw5qysmjogV-enKZriOe1uyxoWoUcHrdFyZFLyngwDR3yovq5D8er9ch_VU9AIY9-q1ji88-XZYg7M2ClwxbA6i5FhzMf_5x2UyaMFzD2ZEzSGqB67o8TAeRFBG74NkbaLTA5kYScLvK4g7MTkTlEMsjG7qnNZQLXK5xImCDaio1wvB70yovr_cpQc6Cun0onQuJVMgipDkEk38pzZXdHSndg-JePoUSHsKkGay6y6H1J0nDVZbpFB5qZPNAkavtcQz-rTHVPxrVTnlArILoKPawyW9FWgHCUQRLDpAnQWMvsfeYhhFOMjGtZwsQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhVbztuVaHrDiarLc4Vd-K7ti_7k1F73q_83EUNC6AGcRVf1Al3D_Sf8ctRFQrxPwttI4w_r0yJ9q1DyVtxzc1pFf6fcevzkMDpUP_uKReA6jzsDTwXUwsvMUbL2OPwGjPrA7s_Db9MO0cGTKaymyp3meEtHYXQytfFvOX8NvbYHSiB_2fF_LRHt2rCJqMI812knkMGgYt-SGMc0t4lH51rIEVImfxkuG5M1yuY7dXOkhimNmvevE9LbbAGi6YGbdDmv9gb9VdmIBXElqx6lBUT04j9juaf3yBpJISt0O8W4AJc5KUPbHcJcRMoaLBvvjT0ltlS2OzSKkaUZDmGazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnnNTLe-3_Zft_tZDYhNITNsIDju1KGfRCEO_EyxQb0M6jbwMeuICcSiy1eoPBjNquBTajaD7A7lhgHuRfElje7Uy8SXctriJMpiTIOHrRUu9eCfydG7xbPtXmkocrgCTyf003kHddRM3iumBQImdEgVe68Oo1_hKWwz-BcOavlg5481qBHqq3Uk3iFGcGvHeAx_Eg6cvSKJYss6jK9-p0XaaCZk7SPLD79ppKZE0UZ5A9X_giO5ufI5zB3TRjf59rh2WBxwoHl8JfsBCyQkb0DwhU4ulaPk_gj-TssmwbI9LnS389f7PaGoWYPd-RXgkjzNwORvnOg69V-QCw4yOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tx0eGbOvUPPuAVj80ZZDq0TEGp6scsBVBZvjqDK5uK5P4UtpzKHU0zp5cgoFyYnccDBr2sMXCnboV6NnurNjPuZP4J3O9YELemuc70jhVyFEdZiulnt22XfsKm-FvL51Nq6CEklaXEOvbjM51cNmjXtlgunQKU9JzQSAFQWFr0ZWkPUdofYUzfFqsE79yx74UAiU0AUutZ2iPLQOlq12zhhsPAwZTAvWKBKt56I_lRby5_1moQaQfkc4CjROUmvcqYP1pPiz_NQRX0L8q2VloK0dDqjddY6RlNmCuAM78IdsH6_q7kfwWj5EyYQJ9Y2KvzF8tAUlwec5sm-31UncXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7oNV3rCVQ4u0STnILGPCM7c6NmzDhFfdMXoIFQBY3ep9x1psQdDEOwnHDHmmMD0pukBPzGI0SYiCEYu3BCHq_CUDqw2_qwDnPLuzD8aX8IfyVMs7SBU6168xp6bwtf4PQz6jghzzXayTMyCnwgEKrRPzbwBKxQXpt3MmfEp3YPCuGc1PoDaZd8ZvnX7hHqXwLheMUzbuaswtdiidWU8FPD8khD8AUpqwkbcA92ikogf4RjtWn2FQoROZ-zpF-Z5Z6buQqO8PDJXOn9Wu_1wmyHcFpYl3Heu1duGEnc9bBmv7tkcZPf0WQiAfDEsxEIqI52EewjTfvc7wsBYFR0Yew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrNRm1kIEwuZqmenYVIr8_HjJDOkg5RvyCW8kkLwVU960TT2hHLdyelx4Gw8a3MrUSaQtFyVhpUAMvhDQMYcKnIedO-uAQM4RBI7HNgkqxeUuJSNH9joIvO8YaiQ0PMOQBa6xVF3Ov6gZ5AobU-dRLokAm3nA4wdN0J2ho0a20JmOZD-Kq1gaVOI6E7W6E3SW-h-zoO2bGgavNJLdPLhW-vxS5TR3ebuoRALb4wWauZDYWc-TgU-KY1kgMaCMoyuCeYV_cgKmNOPpbFO66Bsh0Yb8hveiVDMAVDnaucFXTQOweR93IHABxa3ijKejClLKOnCy_BGU5HlLQnjf2Q5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFAHgaCBLOtnj_4Mf4EEzIWRYJ_RIDfyYj8LA96j7JfbtvWkT1JsdBO9NywRpixZS5ZbAHjHmD4njphW2mvX0C6u5b2Dnh4lIR7xyEfAa6rkh1xOPObDlflG6po_EF0FSIb_gcV5RLZO0etLbS6ol9AuFqrFgxw5B6sz1rTEW8DRBh3tUdwX2-QsogvL_W_3eQ06s14bAzJEivA5YllCXIaFtkJxjY_FY6siJKzx6JHK6--JnNs2B65pA0-wn1_4lItOiurriEfbV3PA6vPJMKlsLr3lV0bL1c0fd8OIThsWHAMHRdzCM38_R1m1ZClxReSD5Fk3J60-GLFls8shHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onpOWQkQ0XwlHH0k93a4FtttvtJriK_E0bzxTS0g7SxP_ZeKszT9kCtDOSXnnRdD5UUmVClUAlwSjoXf35VA0JQH97PTtEiIbk-gTL3-URpX8kdqddYw3iPjzqYm9GOfFFyUE3bW1LCAPq5SSNstw-bW9_2BHyfQ6HpTIpj57yng2LSI5-fgvE1W24epEfB5-IVOZ_xpDclZEQMqnr8vU2b4OsPL8S5jidGNf2B22MJ-hBRfQVU_EbLx6HDoUo-cZQ2t9N0JlLEszZFUA4tWc6tEMRPvDzTkm6iWIZS6oGMEnuzFfbsI5n7_77lbnIvU_y5zpzDcC1MC3Yyuyd16rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4XjPm5UVn8jDAyWG3LqxpbXgSSOFE6KC-H9V-IGaPSv6bsdHTTCjRTljWveOBKxB0QfVU2IMEHT1HvKm7MXQ8PhAjTw5JC5JMAjY9QKJJlh-07rENk2h9td8--j-PTXa5juZML2qvpFrXMesuvOB0WANMchOhAq_fAGB6TSrkKnxYQL2U5l3EDxnrdqcct7uW5DLJZfOaI3MYkx28O3wnI9E0-4IlDdi1LlmgQwSvQnDVLZzoIt0sCAwQSzmaO-ZcN40qMVBEB-3m8zUAWXAE9RhW7l-4uEYZugP9IP-v4V_im9T9e2_eQVmhcpSU24KaZ4xdRqFlrh_vBK8Pn1cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=WvI1iuhKV7ThIxt4McMRn45tNyKPHnATYZ2qXfE_zFOXvIEBNI7Tou4B-rKcN3tDaCSc5sAL3xUqs7EOFy3Y9xUUv2D7FMh-QnPecWsd6EMipRSzn8qH6esMn-CFsItK0_uLOFpMawhXmheHrbpl88kQW0HfKrwbJWqKGAlDcGlgLjYtrmH8RY5TpgzJXQK9hoqxDQ-wikf-tdhbaichRwV8bdK4lPAab9kWzBQkTkW99epNXjzq5LqoEh4-JvawY5ZVJ0Ldy4GQUapkqgiIHn_lihPNwY9_tpRgVi1vSbfvsmiuAzXJJWkm48vwsOZL0Y761AhYe2ZgSZjCwsaL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=WvI1iuhKV7ThIxt4McMRn45tNyKPHnATYZ2qXfE_zFOXvIEBNI7Tou4B-rKcN3tDaCSc5sAL3xUqs7EOFy3Y9xUUv2D7FMh-QnPecWsd6EMipRSzn8qH6esMn-CFsItK0_uLOFpMawhXmheHrbpl88kQW0HfKrwbJWqKGAlDcGlgLjYtrmH8RY5TpgzJXQK9hoqxDQ-wikf-tdhbaichRwV8bdK4lPAab9kWzBQkTkW99epNXjzq5LqoEh4-JvawY5ZVJ0Ldy4GQUapkqgiIHn_lihPNwY9_tpRgVi1vSbfvsmiuAzXJJWkm48vwsOZL0Y761AhYe2ZgSZjCwsaL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0p-DCiNeTOuDhdwm3zjxLgfM78VFWf_sfY15ihYObkv2nwiuKdoB8hScg1pVQjjUT3hUV-cIzWJ8V14jf0EOEh1yEntGIKubJxOCZoCaC1jGB-xv1cTk3jjP6Nr08IFXAGRH1iHw_BgGG_CNSX_15h157_MYGfksnBs2ZRblvUB1_jSgVupZlllw-JlIo4uu1EFi1rUUSkN0O1zE3lLDYXpneT9x_QxMi8NzZ1WEX6t6r4Wjt5m7l_AlgF_JQC5_rSZld-bSRT2H9srngbvEQnarMnRtCoqwcI1aiHXYkhmYbChYTk9RhK0mJjDhQqno9DMjqgj5hwdmtIdW1mYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlBXjLGChHNXHVWE2n6vSVTLkRWlQfWEwSf3v9eOM4ecuA-aojg0M7RZGBuwB1SiEeXJUbQ8pRO_99VOd8GOWrg38-NkBsmSP56gI7O4aQZfCuUMIdTKBO3HQVfcQcfNR25wfAUXeNsRdVpP4FbXaWxTV3_xZvvg7EEqEGRqMW8f9lxuNYZHGg1C94tvKVYKRxxK2LQCqxjuaLQ6n2WiIS4yDZ4DRTndMYJWsuI3KuiYm08dMMErhmBZVkauEwqWbA9uSb4T7OGO9FXMq6xrk6tanxst_YYD8yab9Y8VDdQ3LTSN92f3Y6QcX5ZDqX_nKIt1hyqFGbpdozDmDjeqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VE8NJzRvTEQ61Dbynsq4mamg443f3x3drklWSC0XhJ491lClU3_ECDKpWsA13_zy2N73wOzeTsys_SCGGt42m_HBkAbFS-tkAlOUmJnv14YffqKFxNIXMW59EXB3a0I8FT3BOlClfkyUrbCmct2FLRTCdtXPj39VqV0jM_ItRjXMVaCZF86kkA1-ccLrnWjc9UH011Aj1GYasbacSr-C0fiwnytz0NEHzmiG9uVTqU_zS-4T6Tc6KJtDTIfc_XFdbUqeEC1nB5b3FCy2GPH2LbwveT7db8a_RaI8kLas2unbVLS76AUlXWoLwz2uwJLKBf3Qf07w4pP2lu54uHy_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrG-dU3eagKRytsptvG47xqC83iqYQP4gCZROGtCf6PO6Zd9yhHP1_H2iMiX6sPO0HybhYo6H8hX4pdo7eva3XdMTUd8sxUl-HXRqFFp6tnN4lg3Mj66h3FGTKkScpL7AhdNY2VUcFt0P_T_pTz1Y37jQaZUC0pEEB80-84ZsW246ewTGBZefXrhIMeeMewESmi19JWxUoxccCwo3-odP00UHW1wJ2J5LPq9h0pMEz7IF6tHzE-n10iIUFqpsBgJRHCHry0sFZfc5lTu935Sg_WHeVhgwX3LddM5IYkhTJ89e-u2xHSoFl3-4gbVj7yBNGH15c91D7c6wQbYqKGaLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=GWHHy9fMXAQ9CyJGC0hymf_PVQGC3CPYoKbB6wt9OzuSrFqOY2EfnPXPOu0EM0RQ4GdCO2W40v3ujB38wRHvv0loswE0dLZmuS6GS4z0NU4VcuA2_nCTYFxKDyLI_qhFPyVoq_lTfyNUGDlYe-hYQV6lacmWbUNE3EuykI9Y3LdURTKvV34ZT2ZTsDTLk8rqyHK3izP3YWQn7j6oexkLd8GZXUhLfSsQ0wHaSh6cpaf2yFAIs368H4jBJXNaSJBhsxbx8pxdqRukopn7GgtrB8q6MAWOFc-r5SIcutCY5yTO-3CDPd7Tqe8Tocm8ioGDxsYYyXUdHd89KasCeUv4BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=GWHHy9fMXAQ9CyJGC0hymf_PVQGC3CPYoKbB6wt9OzuSrFqOY2EfnPXPOu0EM0RQ4GdCO2W40v3ujB38wRHvv0loswE0dLZmuS6GS4z0NU4VcuA2_nCTYFxKDyLI_qhFPyVoq_lTfyNUGDlYe-hYQV6lacmWbUNE3EuykI9Y3LdURTKvV34ZT2ZTsDTLk8rqyHK3izP3YWQn7j6oexkLd8GZXUhLfSsQ0wHaSh6cpaf2yFAIs368H4jBJXNaSJBhsxbx8pxdqRukopn7GgtrB8q6MAWOFc-r5SIcutCY5yTO-3CDPd7Tqe8Tocm8ioGDxsYYyXUdHd89KasCeUv4BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=WDIWLANxofnM_2hqFr-1XE2chB8LxEp9WWpLtsHXZ_nap49RNvpRZl2nkEeFLqinKWmuMEVanedJbkyU1PGVAgOUW-hp_HMOERZbQBsDOKWCqdAyjhhMrSEz-bOdYwqbNx5QKkNrb9oVQrLDi_dChR93ehxwzs-ANjy2163wBT9Wnt-yah9MuQexiX2Kp-hhcuKGXY7FEKaaPP5anjviEqQidTMPArti9nRcuqrHe7yYWEUTvIa8wGSHywIsiWUWEyg7iyI5hTqIMQiD8Br8litcxT9x-5I-xD_czL-sbIdLLhfFF1YO9oRsQXiv_6V0iPIxg4HepoJ2vmpwoIDlrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=WDIWLANxofnM_2hqFr-1XE2chB8LxEp9WWpLtsHXZ_nap49RNvpRZl2nkEeFLqinKWmuMEVanedJbkyU1PGVAgOUW-hp_HMOERZbQBsDOKWCqdAyjhhMrSEz-bOdYwqbNx5QKkNrb9oVQrLDi_dChR93ehxwzs-ANjy2163wBT9Wnt-yah9MuQexiX2Kp-hhcuKGXY7FEKaaPP5anjviEqQidTMPArti9nRcuqrHe7yYWEUTvIa8wGSHywIsiWUWEyg7iyI5hTqIMQiD8Br8litcxT9x-5I-xD_czL-sbIdLLhfFF1YO9oRsQXiv_6V0iPIxg4HepoJ2vmpwoIDlrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe5dZ4uSIsNRu6BbjfH9FYxlMELxTy05UmWyMz0nk9ya-m3IQPv9z0U1N-wwRBi_dsNfAeIqAmL1_RsJwz-f7IylqzLeh5Pl5Z0gvRXsO4REhjGEuR1rk61WGSuyndDQnnrzYV3CDs-Z6XgnpMUuYz8eHaOX55IrYyl5r776-9QF8xYo5FGTQ6E2TM8zzGV2OHrDOoSAWODPpgB4PAuccDptyMZ1kd8b9m2h5n2PwQYNDLNG0B8NMdm8BvXScWxxzeFTTr2ue5W8mssgLMz3a7y-6qzYnqmT-RcRM1SS847MeCARvV0qTBshSiAHd3RRWf3N2wIhljOFODE7xML6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=gsa3zVHZDDjeyZbotQNkvFok-WvRDcWtKNHgrxnJb61y_jsmwGLJwVi6CdKenZlZUCuN8ZWEK16KdjeYObiD0ws6mHfB_7JQ1z8s_-a3MEpaY_GgjG3EtbLNFd2CKWr4bXfPoqTLoYxiR7k2iFfii4je10VaDpAXAig9rwPKYEkQmSMLwyP6PoCFDFpfTqRHRpA5He2ap1JXDYAf7f2l0rROjMu0cqROTSk_ku7WToNfBo9mhIV7MDg07R-w42uEH_QjEtxIngW3BF1u38wwK107Qk41Qs3epPsLKSneHLlRq4GIICoWzm3AxBnLjM8pnbCvmxRVarDm6IF9AIIC7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=gsa3zVHZDDjeyZbotQNkvFok-WvRDcWtKNHgrxnJb61y_jsmwGLJwVi6CdKenZlZUCuN8ZWEK16KdjeYObiD0ws6mHfB_7JQ1z8s_-a3MEpaY_GgjG3EtbLNFd2CKWr4bXfPoqTLoYxiR7k2iFfii4je10VaDpAXAig9rwPKYEkQmSMLwyP6PoCFDFpfTqRHRpA5He2ap1JXDYAf7f2l0rROjMu0cqROTSk_ku7WToNfBo9mhIV7MDg07R-w42uEH_QjEtxIngW3BF1u38wwK107Qk41Qs3epPsLKSneHLlRq4GIICoWzm3AxBnLjM8pnbCvmxRVarDm6IF9AIIC7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArN0263wjjaUJXc1p91YW6iKwjfbj5g2WswiAs8JpLHIvQcZYKmp6w6AdA9_k51UsPCA_WONzHG0267ee2ZC8DBISk2iTOaBLE5YzTiDdhN7dH-SXHyOlVo8bmUXo7o_YwpzIsdgGURk2nCscxUOXlqHn6yBdHn2ZsDwfxqqGZ521_S_bE--8vA96bEilxdKdmnLtLKOFVe_ZPWJ6loj2Q-toDxzdT5MF669DDPXpXX8eh5E2IKde5YxVPBdS7a9e9PXhr_NTgTvOyj-MG7Q2xj2g638wD_tfQYDF-cTXgQYQ82BeDI6x1NwRrYA4xdDaM6MuCsnPFx9mu3hWr9b6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH-NTtkv-Up4LkjTEf8KPckOUWDbxnriyLA65RRPt518bla9DVh14li0S9MDzsQER3PcDHiPudoI6M4KoZM2dVGSesa3Z8ETS24l_waza2LiJR2m9jBeENORsPlnQAbCSk2jvygpAbbH8cG0R5m9NYdJ8m4G2jOr6I3Jna1M-s2eGNhXr4Ewz2sl8k3-CWn3gR792ZZk6IjakKo4j_uNu3t4Si0IPQyIDxw1_IsnCoCGrNgbO3Z1BqftXM48FenACPR7_p5QcwBnNno2FCtHncE98frk6EkT2mdOKgV4u-V0Xf_YC7V20_Cr4s7f0GzrpSYQWkn_obU2JpqxbS8PZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=EMl_020kHc3tvw9gkAEIEjGXVrONTDgfGV5LtDsVkpXki1iTUGBfASq-9pUFw_vf-NSI-20gooNbVtT2FeycOjqodAt7ts83odhei5H5JQDE5lQtwkh4rDSn10DgedDtLPtcE1Q06xAftP41NUhuagbydKgiQnMrJ6cT7Rona9VO2_mjFsrxNrbCflyaGjzvQZ0bk9ft7CuhzaWuwBtYDrECIMfud8PNTbCQqBE3-oHLwoEFM6pSXf0d_gnsqyWZUsZd-Ow-EgJzz6m4ul36zYsCG8CajGlS504otbQnIxt4ZaKNp9GgH_XaWIXG4ssbtzJhxvFSWH-aEk4aqPcUDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=EMl_020kHc3tvw9gkAEIEjGXVrONTDgfGV5LtDsVkpXki1iTUGBfASq-9pUFw_vf-NSI-20gooNbVtT2FeycOjqodAt7ts83odhei5H5JQDE5lQtwkh4rDSn10DgedDtLPtcE1Q06xAftP41NUhuagbydKgiQnMrJ6cT7Rona9VO2_mjFsrxNrbCflyaGjzvQZ0bk9ft7CuhzaWuwBtYDrECIMfud8PNTbCQqBE3-oHLwoEFM6pSXf0d_gnsqyWZUsZd-Ow-EgJzz6m4ul36zYsCG8CajGlS504otbQnIxt4ZaKNp9GgH_XaWIXG4ssbtzJhxvFSWH-aEk4aqPcUDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nqlzLqY8vIu_SDeiG5CWzw6KwedAW2NzqtCVRVzBT9lHQHWyCI_R_B8HU16Vn45-c5AniBhGam7YsRSi_E9oTMATBDDCpdCjAA6TOxi7-Og-wFSOy7ejc9EMbCLYWMeMJwnOLNfgcJ3M5DOTG4kPGO_lHH4hbr32JnjkwDat8rWY7CI_a3om4SrKcsNq8ONXQme587WBbl0-0i02uYS9LLTilp2xcJ-l8tvCaq48HaR5R8admzl8QLYe-Y9DeYnagvFcCOJ4JxnT-5HvIGTjyRKIPRFOpvppw2mWxGcU7BbXAO9hKhUPXt8tyynbkFHxOFk3h8zisMYdj9ngwU25Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Us5a8rY8fs_OssRdVpSJitCOVxak2QTASwj0zpWvVFCLLRj23YMXObgoduXRcOb5uRNk_cAaYsedXI1qhdCwggfzLWqq0aIINi9RzDQJhruVvhP0qyeBYap2CyutyjF8FAmuQhXTSyWMkloLmSEFOJE4SLvPfWSQv1yE1Rp766hLH7GzP-hB2elQRhavM9rUjz1NGW8bnCTJC_9Z-2accHTrSJ5oBr_nsW2kbPPKY-QFZFlvbcCzYtQjJ7XnIor8QMcnn5i1xzEfNiSt22xMM2cvqUNAB8dztBT6QFIrdV34LCYHr8iS2NB0ZkTJlq4I13SU9Td7aIK__OVYFBBeyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=D_lHzVdl_-CptVMDdBTe_aY0hjjo_9TdvhwMr5242DGM8D5Ws_emdLK_TwubfXoNrYbLqvKJSmnbDUjq2bSj4AghovXFobj7Qvjw6H0K-VrHhWf8pOh3iGW38pu26S8otk7ZYuf3myQTPaFE3RdEjZv39EaXklOfRFqdbS-RRIt9goG8aEbWG3a3np5ukDiFREg7JcGaw8LZVyWZXuP9M8uKRdMIHxPEm_el0G7ry2_o4oRL_LuD0Fu3aDu8NAC3hrmThJhehVlPxjYyrUTpHdtzMPb7BTJi_PbgzUxFuZQt81qJsAzwZq8wxXdCzlQZiVQSuWZaNO_ZhPuXjX1BnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=D_lHzVdl_-CptVMDdBTe_aY0hjjo_9TdvhwMr5242DGM8D5Ws_emdLK_TwubfXoNrYbLqvKJSmnbDUjq2bSj4AghovXFobj7Qvjw6H0K-VrHhWf8pOh3iGW38pu26S8otk7ZYuf3myQTPaFE3RdEjZv39EaXklOfRFqdbS-RRIt9goG8aEbWG3a3np5ukDiFREg7JcGaw8LZVyWZXuP9M8uKRdMIHxPEm_el0G7ry2_o4oRL_LuD0Fu3aDu8NAC3hrmThJhehVlPxjYyrUTpHdtzMPb7BTJi_PbgzUxFuZQt81qJsAzwZq8wxXdCzlQZiVQSuWZaNO_ZhPuXjX1BnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=bWdbGp3nw3bRTnIDsby2oHM8Wyy0y0GjKA9mo5YZ8vYd0VUZnQu9jl8hDuBtABi3EHZSQEsSO8ofKwFKXzmmPdzEC7Wxf64zXiaJS9Yjolksb6E-qah9jd4nVds2AlLxH7smOm-OCbk7Lg39lrQYTGJoInvR3x4WHqjtVAHXYRs2mN_K7InsMXELJt4gKMJ3gPYXR73f-X6UDHPzeG3M41F75PtWcL9CpS6ZowWIxzE1q7trGp51FYrRoGvR4qsamh3MiWq6iTwTsqIwekWMi0PbMQKPNksIxAJTTNN9Kz_yOFbjUK-CoNIg43SB80uEdoEg-JHCGUeIsXQP38Tgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=bWdbGp3nw3bRTnIDsby2oHM8Wyy0y0GjKA9mo5YZ8vYd0VUZnQu9jl8hDuBtABi3EHZSQEsSO8ofKwFKXzmmPdzEC7Wxf64zXiaJS9Yjolksb6E-qah9jd4nVds2AlLxH7smOm-OCbk7Lg39lrQYTGJoInvR3x4WHqjtVAHXYRs2mN_K7InsMXELJt4gKMJ3gPYXR73f-X6UDHPzeG3M41F75PtWcL9CpS6ZowWIxzE1q7trGp51FYrRoGvR4qsamh3MiWq6iTwTsqIwekWMi0PbMQKPNksIxAJTTNN9Kz_yOFbjUK-CoNIg43SB80uEdoEg-JHCGUeIsXQP38Tgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XY88PGB6VWj-f2mb2Frol7J74c44BCv42WeYv71aTH2d2IXYCLGrEu2oG7uWmB9yTT8PYbhQVmHIojjKKEMft4mBxa6GU2xlp180EATeYtp0NQA0ALNtMcfuDXGdzUcVgajfQ0DuQI4bfU31LKGD6ewMx2kNZAIPFkbJEe1b_5kD2bPmneSBQtyP23tg8QyTX2MupTTaJ-2KT6Z5Q__sfW1a_WIMj_sga8xXgDSVNeqp9Rz_ipMw0Lp0ogW1RczTmjl7rcr1K-ornRD4tM0PbkcuMcVy7_AcrHY8GLezyQWgie3_H93tbjMVm7-Mq0WMhpT_LYTq0i15pHKGiD9jFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmiammVfQvWBTAvtoI2kqJQTQ1sE_5bZ-EiH9wK6LQBy8OHZHPeDXCdOhvjJVOsG8yIZe1DE8dQJcSheq8k0d9liZlnHU9D5K2_ptuEYH-falcQB_iiBxonI3g5gsi2ECM8o9Gdt57zzzYAJKZfVhjPGkKXGHEhAuuYlMUIfhRhT7_Bs3dpIY4GwY5LrH96cftbSiWOHqRZNQEWHN4riGBUnPSmqwV8hRfZV-dUYgueZLX4mp-URvbG-X8-DIl2zhh92sAkHgYlIOhnXCrih856r7XDgkFMnMh8y-uWYiTxVYNzR6M0TKXoLHvO__VPVGJWQV8OnmWuxuui-DCNAVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=LoVNN0S_Y4Tq-nYTxarQskbzTygaXGJ9awxEpVKAJRMXR6NcTryIbQrMKFKjxCn5iTc63fjn4v4y01QSOc0RkzYTMqOsaPiU87MXjaZZmut5NRX-qFwxM2hAsD1gUQDmz4-ABtYEsQMptUBbiQTIpwzFTn3gpiV7Ws0jyUnkoN5Kb9JIpk0sTwl111xr47eVEwjUIzoqUenAXSKs8qexLXI0TYm6CnPw5D17SrgC71h7Rrn0JydJSIn3IE9rWGecU7CIzu6NfZADJyqQIRvry1J7FsNFCgHm7CfalO3XDLb7xIB7H1c438q-QQVTgv4MnDbVCKwMQy0w8sl4pTm70Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=LoVNN0S_Y4Tq-nYTxarQskbzTygaXGJ9awxEpVKAJRMXR6NcTryIbQrMKFKjxCn5iTc63fjn4v4y01QSOc0RkzYTMqOsaPiU87MXjaZZmut5NRX-qFwxM2hAsD1gUQDmz4-ABtYEsQMptUBbiQTIpwzFTn3gpiV7Ws0jyUnkoN5Kb9JIpk0sTwl111xr47eVEwjUIzoqUenAXSKs8qexLXI0TYm6CnPw5D17SrgC71h7Rrn0JydJSIn3IE9rWGecU7CIzu6NfZADJyqQIRvry1J7FsNFCgHm7CfalO3XDLb7xIB7H1c438q-QQVTgv4MnDbVCKwMQy0w8sl4pTm70Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=gngqexoZs_vpDGwNWD6oZpDmJUMHVireDhsNceV9dsBbJ8JCzXklKg7tB0IE52ffOX5eroj9MlzkPwlU37WKseqAsXo_lyGA8ZpghdgzIFCNmbgihSdYqIHVtWJgydqul0LED86RNh9EePRsDRhyjWtku_Rlay-2x_cwEXaZrAhjo6Xb1Km2e0Czi7T8KMqvNJBWOUm8nrSQVeN0vVnr8HTv72uuELwUdu9hoUJuAoRSgIpTtAAIt6oMFySzFMms8VA7bF0-vYwfiR0z3OtnwYvF3qxsPchG5GdDj3mNUga3Vd2G9DZMT7SKhKJFq8jNnyIiMGfMYC2Bh7glWxq-sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=gngqexoZs_vpDGwNWD6oZpDmJUMHVireDhsNceV9dsBbJ8JCzXklKg7tB0IE52ffOX5eroj9MlzkPwlU37WKseqAsXo_lyGA8ZpghdgzIFCNmbgihSdYqIHVtWJgydqul0LED86RNh9EePRsDRhyjWtku_Rlay-2x_cwEXaZrAhjo6Xb1Km2e0Czi7T8KMqvNJBWOUm8nrSQVeN0vVnr8HTv72uuELwUdu9hoUJuAoRSgIpTtAAIt6oMFySzFMms8VA7bF0-vYwfiR0z3OtnwYvF3qxsPchG5GdDj3mNUga3Vd2G9DZMT7SKhKJFq8jNnyIiMGfMYC2Bh7glWxq-sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbzdoZfBMoE4BeKtCE-Z4Hs2wQFqxyV1XYG-etp_uu1Rfzk_SDDYE92BOqhC1kg1ptBJw6JnwcJ54Lei3DvFaYQx66z2eHowhZzyUQ3E2ImV_O8oxo5p1mib9oANyBuqT-Mo_luOoBlObyACkRmFv0B-5G0bDch64SDBLnZoJyLNpeadDm2553f86yNSY7JnelIrUBvYkneXsu97scHRaaXGovzBl_8vQKEOLrC0ARzF3p0aCrfBKX-f9vot7DUvYj8ewT9JBFB09Ov87qoBvzd01_92_CX9BBow4J4xG8JnuuEiO5TcCM9FTwp3ZEHvEC0H9j6kwEXJWLaZIDwduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=PaFTnDKWPHtP28wrroC6c-hSfVTtfCv1H9HROI7lNDzMu5z6g4zIzuhia49lzbZzumYKrarELFFIimGvrZpVj19Ss_x1VCO8nMXyfmva9ZmXOe8mmBved6uFAXBLQhpGD1R3zasY7zq_A1lIJ126sl-WwajEafGYF_Zyzj5wlkJJG7sPVZ-3tWfCSVFX2USfK0VaLwGk4psCjUa5fqpFZIDLbaBAApC8iPABkAyYZQD0QICznppM_f6EE8_lxtBg44MFvvq9bU58DSEXSus5lIK7xyT7FTtayvDb84Novl_7WRjOdoEScHEehm8YlSH1NyRVAkmDPP4OVp-aneKlpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=PaFTnDKWPHtP28wrroC6c-hSfVTtfCv1H9HROI7lNDzMu5z6g4zIzuhia49lzbZzumYKrarELFFIimGvrZpVj19Ss_x1VCO8nMXyfmva9ZmXOe8mmBved6uFAXBLQhpGD1R3zasY7zq_A1lIJ126sl-WwajEafGYF_Zyzj5wlkJJG7sPVZ-3tWfCSVFX2USfK0VaLwGk4psCjUa5fqpFZIDLbaBAApC8iPABkAyYZQD0QICznppM_f6EE8_lxtBg44MFvvq9bU58DSEXSus5lIK7xyT7FTtayvDb84Novl_7WRjOdoEScHEehm8YlSH1NyRVAkmDPP4OVp-aneKlpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPuSlFEvPKAf6UnEcTXiXBk40-lzEv7iUcNQ9n_wIS3PVbYnP34p3LhHjckNuIMmH-Bkzf8CLAGBWNzGVrrlGzIwB5lM74yIpEHTevr8H5cAHjEXLd9YmhrafRXOOGLsm6mnKNIC_BAQFX54CPRFdf4kb9e1Ywod11DtAVB1Za1Jw9Za3fuWWHX-0vyGndLNLkTB8KULUs_OQ7tmvyeYut0uf0D5tqbbeCYYsh4-cNDnntdqkshsxvDiPzE6DlkjFSE1wbqr_kaaraUwpAiaTgVMr7Vac6ELMQIV080o4-NAfq7-oIpStC4iDZXLr32YvPVmrNvoIot2jIffwg0-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJA-5wUYFhQ0ErrHe1NevRq7vQZdJweh7cLtIpI4AyKoEXPohUvWR5Qhs2jCfo4lwQB4BUr64E1c1sCrnFiOWDcN0h6v1YA0oCLrdYKmqwkdf0Qt2_IA_UrHBgxmQ0nt5bWsj0BVAm8PTEe8NwKM3m10i7jdf0qDmG7ss5DoJuZAyxHDXEQuRKVnQ5lYwfhoopiUQpG1NeXmctggJqfkgtL3_GyzpGfjj1WQuJ_42LKnRT8Tb6D5F-sv3g8TfIkxPyEMuO8xTBnmeKqZeapZYmGnxLl_F1gI6voNaeJMW92CSb-yKWS7nhVKTqEy9l3fVJqmZ75U2GlHZ2xkxR1ERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OU2QzgBCCRXkHDVf6llEiipt0CEKJY65bN2fDNe9M6lzSx-1Xtablcn6Qj7HqoCwNiUtGnOqfOu781LuAom3aMZUezvwaCHFrjsURojM6jZ7DM6zZwyN6Sp5swW4u14ePApLbN9DoAb5DM4H-O-Q0x3PQVKHPFMy5Ru_FKKGu4pOp_YlD4QncMkDdICp9f_L_DVk1pFb7cMHJXBWC3U4BhURwIrQG919Rw3trrHl9wM6hfforY1Yf_hclxI7-acogKDfyGqtDvn8u5gIChwxPavre6CQmSQn7Jaq9y2vC5ezXyXRgpYrXJ2AgNasxxcANnS10q2jXx8BQ-JpDCsoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-_tv_4Gi6UJWQfw7VyWsqFOWQL2p52EI8CNyTa2aU1wTshR_xqKafzVYb13LfKmnDSYuoBHkzuXqLNUo_u6glwdMU_9aIcPVWuRF2okmIQj_X_QqVh3YCifeVs7zy-KvcBGRY21W1YzYEHc3ng9X5CETcz2ZOjduYvHnJPrHhR1V00ijuxFDUhbilvAt8Ebm8kvEeS1s-VHo4uB_z8Db7Op-Bd0Q4TmTo65D2v7OTiKvQEKy8SZ1cev0J7maezgi4MF-ewnII_5aZw4_Pm1wFZr-6zk-p22KKQCH4IwUnQO0OYJ6cgKDErrUaoQ2OXfwjv9Qpo3MwN44TH5_jsS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=oY0Fjtj09p2oDc-CoDQXNTK-LQntqPgOAJ3N8qeTOMYDa9myZeXHPJE34OhWBfs_X-rfPRTGIEerHZeU1uPYCp9SexMdNKMcDaT_xiF5GE4JGC5PWaR_GvpLotMVuPRN9_X1Ag23tcQJgn4jYVCB7CLo7cJhrfxR5Fpz6EkNN1AXIFzYTM8ryNvsrZbI0Ty6RSYoJJCv1tD9DEeVjoKdk7x7TrLlaq_bvXUBFWQcDcj4hMYhzLNHD63A-2A4Mo12a_Lm0ERxgluQBLIhlZKG_XN9FH5xdPmJZdjsJ7hkagxthWlVMRnmE7AVwYzk_l26A_0-1hGoHeJuiKlCtFNDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=oY0Fjtj09p2oDc-CoDQXNTK-LQntqPgOAJ3N8qeTOMYDa9myZeXHPJE34OhWBfs_X-rfPRTGIEerHZeU1uPYCp9SexMdNKMcDaT_xiF5GE4JGC5PWaR_GvpLotMVuPRN9_X1Ag23tcQJgn4jYVCB7CLo7cJhrfxR5Fpz6EkNN1AXIFzYTM8ryNvsrZbI0Ty6RSYoJJCv1tD9DEeVjoKdk7x7TrLlaq_bvXUBFWQcDcj4hMYhzLNHD63A-2A4Mo12a_Lm0ERxgluQBLIhlZKG_XN9FH5xdPmJZdjsJ7hkagxthWlVMRnmE7AVwYzk_l26A_0-1hGoHeJuiKlCtFNDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=DSZAR32UCXJDXQUxWP5srvMrPQyuMdOMuzxkgdc9AaKqV6qUiFwQE8ufek7KtmHMOaJWIqtasUpLOPkL4wIKrPM08IKItrakNDOV9yhdj-K4nWdnGRw22EBBeBFCkBzQmrexswmZx0mrSm_ozb4C4YX8qFFuMQ7WL1k5JGFnhvJl41HUxFmk3f1zIWgYAlMu42vKyAmOuAQTr_m5icoaC0_70_tWsKs19KMcgbE4SrRBXUAL8lCuKTGE7LgFQzAw75Bs-SnlxhOUNNQs3vFxdBrCKIHuc7ap_qtivWQpVOhMN5Ugg0TgktVK7gPjH0J-Lx8FEhCVyVpAri7LsmTK0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=DSZAR32UCXJDXQUxWP5srvMrPQyuMdOMuzxkgdc9AaKqV6qUiFwQE8ufek7KtmHMOaJWIqtasUpLOPkL4wIKrPM08IKItrakNDOV9yhdj-K4nWdnGRw22EBBeBFCkBzQmrexswmZx0mrSm_ozb4C4YX8qFFuMQ7WL1k5JGFnhvJl41HUxFmk3f1zIWgYAlMu42vKyAmOuAQTr_m5icoaC0_70_tWsKs19KMcgbE4SrRBXUAL8lCuKTGE7LgFQzAw75Bs-SnlxhOUNNQs3vFxdBrCKIHuc7ap_qtivWQpVOhMN5Ugg0TgktVK7gPjH0J-Lx8FEhCVyVpAri7LsmTK0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3KaMNuts5TfziTglPW6bQ10XkYe_WpggZwfkCfqGXzZE5Qux39fqk_TjbuOWFXHlLQ1B2DQl1Dd1YoXiTwQP9a6K7xKoWhU7G3AwQ57GT6QK1lCB_oSMrhmaeNktAykwwTlcvJw8jZlJX1tKIeiWvduFXVxve1Elm_NsTRLgljAV1wAEEKzlkoTFQAzJ7EWyL11Uc37QIAxp8Q1d94HaoCvXywUQEMgJ2MuL232vrFdxe800pRvSdGvrcALSweChA5H3KPm3F0HDSagY-zjGpe21A5nLWsEUO34Hq1JTnD3y-3SVs3YJApBTzWH_tTvxBndlggmLd5Ryz4AlBTI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=dvCwm1o4z4CebW8x74KMDAj6eosKGQwn8HHcEenXcyv-p8Gepj6Y2klIzOs_v66DGd-XVBZA6f66HplvIjqNoUzXC7NG6w4p3aFMvmJdmFNi2Zxrz-exr_HS1zME8sYnz1-ZfeM28pDYOU4EKLJbtPhqxh3_1YSn6BJmL7hUL4Jy-MYIJKM3karA7K73X7XBQlzlXZP0biZZ-MDmcK1OABU1wRGLzq9AFILyx1y4Q9yEYOagkAZpD2XIpfB_x-jCqueCbXi6R2qT-9x04AF8NFT6X58w580w89zy_Qg7DqZx7Y5QEKYuD2D74ZiQYhBK69E5W2yyaeAY7YWYj8Lz4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=dvCwm1o4z4CebW8x74KMDAj6eosKGQwn8HHcEenXcyv-p8Gepj6Y2klIzOs_v66DGd-XVBZA6f66HplvIjqNoUzXC7NG6w4p3aFMvmJdmFNi2Zxrz-exr_HS1zME8sYnz1-ZfeM28pDYOU4EKLJbtPhqxh3_1YSn6BJmL7hUL4Jy-MYIJKM3karA7K73X7XBQlzlXZP0biZZ-MDmcK1OABU1wRGLzq9AFILyx1y4Q9yEYOagkAZpD2XIpfB_x-jCqueCbXi6R2qT-9x04AF8NFT6X58w580w89zy_Qg7DqZx7Y5QEKYuD2D74ZiQYhBK69E5W2yyaeAY7YWYj8Lz4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=qKZDxZzU-Bm58cyxIXg_TmxoZEahJs7IA_bWQEo1jfUtb_FRQ8TBqRAp566qmKUgYZsGHZep7_vhI5FOZTwmE8bn_tqFctjJRQRR7awkYu6CgDcCtHcpvJAnpZbYd4tZbu4AfSF9mloPlnbfZUki_5sfKBIzw8I2jfvp8uJHSjO5kJnItWH8yogDY94llAbYay5qGPsaDqFauOJRVQ6fKKpQZhaPtOfTFQGzH1FsLthtGsX-3OW1MdVq7y-BtI2ipvgyI0vt4A3GJF1a_oENPUodsE5A91E7ZrG3GPVX9OX-1CMfZlDn-u43HZPfZh_BuVzd2a3V2rrDUuUn5ShnUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=qKZDxZzU-Bm58cyxIXg_TmxoZEahJs7IA_bWQEo1jfUtb_FRQ8TBqRAp566qmKUgYZsGHZep7_vhI5FOZTwmE8bn_tqFctjJRQRR7awkYu6CgDcCtHcpvJAnpZbYd4tZbu4AfSF9mloPlnbfZUki_5sfKBIzw8I2jfvp8uJHSjO5kJnItWH8yogDY94llAbYay5qGPsaDqFauOJRVQ6fKKpQZhaPtOfTFQGzH1FsLthtGsX-3OW1MdVq7y-BtI2ipvgyI0vt4A3GJF1a_oENPUodsE5A91E7ZrG3GPVX9OX-1CMfZlDn-u43HZPfZh_BuVzd2a3V2rrDUuUn5ShnUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=B_ngk_m-5kvXP4iSPTXw4kGL-dcYC4VwiJMnCo0wjw5cv81TlAsTRUZfFrXeEfO4rt3gQGHSKlj_miEX2zmtvu4PEruzonMqf0yf2ljjJNstSOXBESSA-m-QWCz_y8jUaQs3tJS8REIm5y5ntwl0E-wUkU1pD6tWEvh6fwfMZqV35OF7A3zlo7QXEqtqC0CLkfAQHWI3io-mnEGEDEmqHH8OEj9YmU7XcDtfOcOhsw-XYE0Qf5kkOydUAF2cgiBYRs4Q7tKJTHYqO2igNgKXRQrFyYL_gyfUw21f_ap_YGs2tefoaU3KwvHEelg6r0VRKeDhrS2VkSHoL8Smq0Ttmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=B_ngk_m-5kvXP4iSPTXw4kGL-dcYC4VwiJMnCo0wjw5cv81TlAsTRUZfFrXeEfO4rt3gQGHSKlj_miEX2zmtvu4PEruzonMqf0yf2ljjJNstSOXBESSA-m-QWCz_y8jUaQs3tJS8REIm5y5ntwl0E-wUkU1pD6tWEvh6fwfMZqV35OF7A3zlo7QXEqtqC0CLkfAQHWI3io-mnEGEDEmqHH8OEj9YmU7XcDtfOcOhsw-XYE0Qf5kkOydUAF2cgiBYRs4Q7tKJTHYqO2igNgKXRQrFyYL_gyfUw21f_ap_YGs2tefoaU3KwvHEelg6r0VRKeDhrS2VkSHoL8Smq0Ttmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=YYV7l8IensN6QLGuthfl3noDTB_Xc4R7cyNlKxEX8iNjHp9jtg_duKpIJ1x3vNS0Wl_TTQW5akbpQxvOT6kYM3sR91-A7deP7G0MTAFT_DOxe7Tizi1nZBRbBttWoaErxM7vkuAblB3vCykSIYJ885EVoViDF1vAHfS9b_1bzFhVP6PHnurQ9ij8fkl_56fHElauEDALkehX9MN_JkZBN-yLrYS0sGrYrceMxCGGtvu4NTeEWgvG2l34rtaPumOWj1vbMxV_LbCQ8TAAS1GoKhH6vsCWcOvdGygPNWc7ROlRCLzH2GKkrb6BG2NepPRra9hPYF-_svgpnoBX3HlPPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=YYV7l8IensN6QLGuthfl3noDTB_Xc4R7cyNlKxEX8iNjHp9jtg_duKpIJ1x3vNS0Wl_TTQW5akbpQxvOT6kYM3sR91-A7deP7G0MTAFT_DOxe7Tizi1nZBRbBttWoaErxM7vkuAblB3vCykSIYJ885EVoViDF1vAHfS9b_1bzFhVP6PHnurQ9ij8fkl_56fHElauEDALkehX9MN_JkZBN-yLrYS0sGrYrceMxCGGtvu4NTeEWgvG2l34rtaPumOWj1vbMxV_LbCQ8TAAS1GoKhH6vsCWcOvdGygPNWc7ROlRCLzH2GKkrb6BG2NepPRra9hPYF-_svgpnoBX3HlPPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=TGZvJbQ_S4HLZr2MhKBm0MJ4u4rp1RkjLkxfrL8gZ4b9cplucA8OfN8U5fp3zn0i7t9uPnbT9kKopmSfUmIlQgPipHX1fTWIbXP1cfgD8omoOt-XiD2UblazhJgVmMU4HLhgmAKi-c5EQFAZwtVGEv0RFg6WnAQ0zjOAh6Wvi8bYnSLHuILo8tlG-s2JWwTjZD42oj1ZCv0XWbsGPbfx8LiYkIOgPggZp9BjeMbXGDbTkMrGl1mr-nI77-tMbinHNTh4mC2wQCMNvc9v2HMmEFzPdWmr0IUis5UDpbYX554hKqlZMNwqJsN5vJqDeJyZJ2RVUcnHhBUxA_sqIngI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=TGZvJbQ_S4HLZr2MhKBm0MJ4u4rp1RkjLkxfrL8gZ4b9cplucA8OfN8U5fp3zn0i7t9uPnbT9kKopmSfUmIlQgPipHX1fTWIbXP1cfgD8omoOt-XiD2UblazhJgVmMU4HLhgmAKi-c5EQFAZwtVGEv0RFg6WnAQ0zjOAh6Wvi8bYnSLHuILo8tlG-s2JWwTjZD42oj1ZCv0XWbsGPbfx8LiYkIOgPggZp9BjeMbXGDbTkMrGl1mr-nI77-tMbinHNTh4mC2wQCMNvc9v2HMmEFzPdWmr0IUis5UDpbYX554hKqlZMNwqJsN5vJqDeJyZJ2RVUcnHhBUxA_sqIngI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bATYLXrUku3R-n2mC3TW-Cu8j3k8M5m9UponF2dwmEIF-pd4trmhRrG3jeB-Gyknr2jyczThR5QlBMru0uokdGA34g3QPtKiTdPXbiw5XEhMoZU9o2xOD0fldzwkhMknXhgrzNuUDK_n3opXvrgmlZIl-L2K9OQ7Z45ukFyJWZpzXD3LFsZTnzOfrfodIAhyd-dzz90eT28qXJdGgh2fxsThFzEbpBGov_PZIDGOtZiaVbMsVj7qWxeHtXv5MImTvZ1sYqQ2tQL8RYJFKphbYayr7ZM52tXbVdgFxduAYi5ODippDaN0A8Mhr4YE410f7TaCNB6tHGU5F4aCvPwAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=lv2Q134W7V5vfjUy5QrovUqSAZvSVPHzduZeV2UFuCRWNqBt8Y86jNwbAN0khG2Thbm4wkVXqTre-z77yK2q3XERsC5cBTMk9WYpIy-jq3qUxcDXft0y5rlSfr8E2qCvQPaviKqVQAjxVEYD0vgRJk1I5aKCwdi1gRYVD6bWRWjwgqf7h3ILwPavfHTDgV1Owabtx5NC4X_C7QcL7MVcJwq-y-At13_9UNL68ed3D54YPsNgQrNrKoQNdKFpO0N3HzH2E18DNVBnuzw229Ulz3wY-YPqUr_46iwoiBbFYr5XJ7pO0pMaKfZLTcLzoMqga2AtFS9-eSyuzskGWENAVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=lv2Q134W7V5vfjUy5QrovUqSAZvSVPHzduZeV2UFuCRWNqBt8Y86jNwbAN0khG2Thbm4wkVXqTre-z77yK2q3XERsC5cBTMk9WYpIy-jq3qUxcDXft0y5rlSfr8E2qCvQPaviKqVQAjxVEYD0vgRJk1I5aKCwdi1gRYVD6bWRWjwgqf7h3ILwPavfHTDgV1Owabtx5NC4X_C7QcL7MVcJwq-y-At13_9UNL68ed3D54YPsNgQrNrKoQNdKFpO0N3HzH2E18DNVBnuzw229Ulz3wY-YPqUr_46iwoiBbFYr5XJ7pO0pMaKfZLTcLzoMqga2AtFS9-eSyuzskGWENAVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WavD3tTZdxjRL-FAS6ERovKSdIbqPGmxmtz7TW1LIBKtL7FFBdLPsRLovvO-D0klgpQ84lhefpPFDZ6YBrS4JrjPz-nEbrM_M8UTS1GUwCmgPlnqBwzJ4OH_Gc0fByVsD7Fc68fEcWunuMSPmzZcEIm6KCDls-_IzYm22KFPs8RZOxj05j6eEQFtu1iWkFTpsXyabwlkSDTsQm3cZzDKT5OODme-sGNKJfDF50M0mfrSztLJ4X2VnU9bV88Njb9vgS9bWTB7FRHOuQka06U8QwAa6Iqyd9rhM0VxqbG56aHTPEA7LsoUKonbU4SGtOPBRRKUHi0l204DFjxA3q8tCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=DlS-ssGTeCrAkbtw1lDa2A0Iw-ubYUsBjLuzBZ_WLkHv4PwYousGpAsUWmanJlXufhR64U7WupgmMlfkZbZJ-8OH_qOqEsdJoXTjdM2MFF5cytCS5BReMvKaF94KL1-CY6vmLVWCxEvt1egPk0r2Tlz0_DZ5ImK5emvsZVwG49V-m4zUvE5SXE-KAtgPysLqkcixzKXeuVCBD8KkT2yRsSZBrefBJhJTiacAFWWXzD96H5-hE9zMP7hlSERDA8a16CRtkHzTHeKn62x7y_OqkOf0ZMIjKVh9QbPAwinocUEmltWy3pmdRRl62OdKZ5rA9NGY-8_Up_evgWI4lVyAIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=DlS-ssGTeCrAkbtw1lDa2A0Iw-ubYUsBjLuzBZ_WLkHv4PwYousGpAsUWmanJlXufhR64U7WupgmMlfkZbZJ-8OH_qOqEsdJoXTjdM2MFF5cytCS5BReMvKaF94KL1-CY6vmLVWCxEvt1egPk0r2Tlz0_DZ5ImK5emvsZVwG49V-m4zUvE5SXE-KAtgPysLqkcixzKXeuVCBD8KkT2yRsSZBrefBJhJTiacAFWWXzD96H5-hE9zMP7hlSERDA8a16CRtkHzTHeKn62x7y_OqkOf0ZMIjKVh9QbPAwinocUEmltWy3pmdRRl62OdKZ5rA9NGY-8_Up_evgWI4lVyAIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=qV6lqR9dqTdpyqp_F60tX0f5gOZDTKq3D5pCtuEHrgRO6_w4Nshp2-tjGHf81YaOBf5E1FCgFt_L2LOMq52l4P4s9sVHKUSR4TZ4WcdPJnAczktXqBsQIRRBqnvgu8ZqQiIFaSEunSo1u8ZECa7rCe0_tMUOhCRCJd7BvPL8vVIM7hgiCpDWT-vECuGZBt19gkfZGX4KErf4CHAc_gS8vD3PMV8Iepyv2G_4gkXUJpqnTKoSGyRBuTaxMFNKPCxEnxzQW2-W7WQ5kWGklxFuhoZCh35gtru2WuQ4ASaSW7zl5yg17XU6JDGcaOF-Urf7kPUZrc4tzD27I2bx6GXuKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=qV6lqR9dqTdpyqp_F60tX0f5gOZDTKq3D5pCtuEHrgRO6_w4Nshp2-tjGHf81YaOBf5E1FCgFt_L2LOMq52l4P4s9sVHKUSR4TZ4WcdPJnAczktXqBsQIRRBqnvgu8ZqQiIFaSEunSo1u8ZECa7rCe0_tMUOhCRCJd7BvPL8vVIM7hgiCpDWT-vECuGZBt19gkfZGX4KErf4CHAc_gS8vD3PMV8Iepyv2G_4gkXUJpqnTKoSGyRBuTaxMFNKPCxEnxzQW2-W7WQ5kWGklxFuhoZCh35gtru2WuQ4ASaSW7zl5yg17XU6JDGcaOF-Urf7kPUZrc4tzD27I2bx6GXuKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=Lt-M5b-j7H-vrIheJQ5xgctkfu7SlL2TX8G_p_BprXR0Qe-qGgogQzbi0-2EEaW6k77gzAErGlbHOJZ2BIsjyYO9fCH80pEQFAoFdlxKZGV1MJtlOnFoSN-5ytDFRCfF5iK-wf3mljE_qabjVlSPCjptMWQFP7m39EAMez51BRJ74_ZbwaHbE9hvaFskbgEuXmHNYbDpz4dbLSzLmW48EqpqURzkb8q2lyrpU87XSqBYI62QSpsH1Tpy57Ygyhd87iftC94dxLMJAc9LVkTFGEzx5nktW7WHwmNG4hnu2PUiUeVQTaO0CADnzT6x_y7KMONnXUzfZM604ivKOR2f8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=Lt-M5b-j7H-vrIheJQ5xgctkfu7SlL2TX8G_p_BprXR0Qe-qGgogQzbi0-2EEaW6k77gzAErGlbHOJZ2BIsjyYO9fCH80pEQFAoFdlxKZGV1MJtlOnFoSN-5ytDFRCfF5iK-wf3mljE_qabjVlSPCjptMWQFP7m39EAMez51BRJ74_ZbwaHbE9hvaFskbgEuXmHNYbDpz4dbLSzLmW48EqpqURzkb8q2lyrpU87XSqBYI62QSpsH1Tpy57Ygyhd87iftC94dxLMJAc9LVkTFGEzx5nktW7WHwmNG4hnu2PUiUeVQTaO0CADnzT6x_y7KMONnXUzfZM604ivKOR2f8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=BVWjrrl4AWcdS1tl1xn01sbYWmIGB-4oTziP0cfBrk4Xtu4cH5AqV_A76YGGgqzOUULl26wWd6MaVOvzbQjVo_LeEQL0R6YBzwiKM-bj3tYMQBaWuN1brtwMIxu0XrB2Ma8QvEjZ6FrYDmpOA35TuEncAOEwlewcF5UmN5Lys6tIbH6ZK1Zhi_Y2Jh3VapQzaDoxlCZCgRld19kHUbnVuY7kQSSgfazfobbQCx3_BzLbWuQfjOLAak21FD99LF4YrxY7DmhHY-onpDUuKssyfIM-1teMOIhl_0_2KKVK0xRIKoVcvQSfVKqNjmxNsJjrF1tY44FLyLGdqaezIDgxJb37ts0ytJOhnXr_Bt9Sk5DlZCoPuWel9Q6AXwhTRdFDHCmpEkvGKrRjK8-QgXtNzQsYCYPYUWnzG01IerBS2VfxojaUWJOQfApa_0ec0Gh0U0nyfejmiCgJDN4m14CXUETPm2obGpHmQCRkE7GdMF0BnFOVUikZguinID0NZVe9wP4amZQMnKlNkSkKQPG5_Q-kc6SugoVKCTGloDmsSIgxyt8FLMkSdqAU2rtxfQdWxvyERewqCwDtuZKc0-dka-L9oXyCJ4KkZ9HcQBz50g_EoLDtlhrcbpf3reKN-goZGxRiHzZ3VaA8MrUDP9-JxYGhdj8XjOV0PaJ1zWfc5AI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=BVWjrrl4AWcdS1tl1xn01sbYWmIGB-4oTziP0cfBrk4Xtu4cH5AqV_A76YGGgqzOUULl26wWd6MaVOvzbQjVo_LeEQL0R6YBzwiKM-bj3tYMQBaWuN1brtwMIxu0XrB2Ma8QvEjZ6FrYDmpOA35TuEncAOEwlewcF5UmN5Lys6tIbH6ZK1Zhi_Y2Jh3VapQzaDoxlCZCgRld19kHUbnVuY7kQSSgfazfobbQCx3_BzLbWuQfjOLAak21FD99LF4YrxY7DmhHY-onpDUuKssyfIM-1teMOIhl_0_2KKVK0xRIKoVcvQSfVKqNjmxNsJjrF1tY44FLyLGdqaezIDgxJb37ts0ytJOhnXr_Bt9Sk5DlZCoPuWel9Q6AXwhTRdFDHCmpEkvGKrRjK8-QgXtNzQsYCYPYUWnzG01IerBS2VfxojaUWJOQfApa_0ec0Gh0U0nyfejmiCgJDN4m14CXUETPm2obGpHmQCRkE7GdMF0BnFOVUikZguinID0NZVe9wP4amZQMnKlNkSkKQPG5_Q-kc6SugoVKCTGloDmsSIgxyt8FLMkSdqAU2rtxfQdWxvyERewqCwDtuZKc0-dka-L9oXyCJ4KkZ9HcQBz50g_EoLDtlhrcbpf3reKN-goZGxRiHzZ3VaA8MrUDP9-JxYGhdj8XjOV0PaJ1zWfc5AI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtnXTXdGN1nCEVHEfaSP_KUDJKx-gOa52nyjDlaCF3-sS-Vcx8RLnNJDxGVFUT5tO0ycyPcUAmlK14kYpHkWK-87wiWcvOpuvJtDhY30VMDQBl2b_ep-IAkt0O758dPcJKnWTEyihMLO1xRMZHO925OXRL9V2pvvnV6U7zS-vuHMiIbOMARwFAJXltHx1ElTTN_009DY2KN_Te8_YLelZUneY6WWhr2242AzTYlnAVrawuSGqzEhfhdCp0XKBXOADnUUZBCg6zQ2Dz1VT_VIIP3SO1h0imv9_uExsXTcodBtEpe8woM5fd8WFrv4uGSkM6Wxa4pcEE_u-7SUEVzUHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=TYl1g1hYyz-yD30IQZMp78vNn6A4690aM4Nutudf3ECt4dRPQf6KlzKvJ564RqyDc5Yz5mj9u4BtL2ACLacesbXqAiCnFfcqq-nXfMyNkcreEFd3XrMw6O0tzwHHYfKbN0mUduKB8pqDJz5fH8iAXnwkgI3OURckVe9Q3r0VXc6sJupnCNND5SGv8EwMVeuyytFmPZyhnweT5xUA8pWRoQMFBuKhfDbMFfg_bqMpAH65cZ366ryT5DInyBtfecrLZHCNOuibLpXfl7dgrTwfY6CjgYU2ZuxWFIBf85zFQjWWKqmfaD6cOCssDxU7FoCzakeaELouLc0zSj-7R_uG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=TYl1g1hYyz-yD30IQZMp78vNn6A4690aM4Nutudf3ECt4dRPQf6KlzKvJ564RqyDc5Yz5mj9u4BtL2ACLacesbXqAiCnFfcqq-nXfMyNkcreEFd3XrMw6O0tzwHHYfKbN0mUduKB8pqDJz5fH8iAXnwkgI3OURckVe9Q3r0VXc6sJupnCNND5SGv8EwMVeuyytFmPZyhnweT5xUA8pWRoQMFBuKhfDbMFfg_bqMpAH65cZ366ryT5DInyBtfecrLZHCNOuibLpXfl7dgrTwfY6CjgYU2ZuxWFIBf85zFQjWWKqmfaD6cOCssDxU7FoCzakeaELouLc0zSj-7R_uG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBb3hWRFyvr6jgUSnOf1RcXeNI5J0LPqiuiWS3xbPtSIn9CuscTRNarQJHpT5r70f9MP41YRdRi41looiDVThDNts1WLo7y_0PbRSg0IyBUzu_f8iLIkDcVtTvnKKchxapXRFPNWLdx8jq4Tevc0NZheJIA22DNU7Ry4tcPNsTqZXVtaaJvCSnKmr3QMY2DTyR5s-jUwY65SXkN2pflvw7Ch5-hjF2az1vUV8JG5kG7fs3FsgYG8zpMrai2fHlzAYMYkQjBYSC9oDC3vl8grzJ4pJ57DxrEzo_cb28JwKD-kpzn6aa3KDNW8HeZCHl4YkppGMecsScUbraLaZrsNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFKSOwBP9CZt1Ijg9Ql_D0fOHOTarwmEtaIa_-22xWKt-p8_u1mDNVhRYlOWqJMgkPEFJQQOkYK6yKVtqbEfY6GudcJZSNCbdWBakM2OA8uZoLgbIR2pEXl9Z8fvyoSbEFrAvOk-AoldBR7U088_OX0NEL5px0BREPlr4gBQRQxRYEN_v0dIUf4yaSvGWbmveG5whJj6WYE7D-jKa4-A-QFGeUOIijWgImRI2fu84gm1wpoR97q9rydmg5N7dCa6UZfYDDvK3fP5_qixaSAXHTQYPIYVtNU8EHA5LqRvvxv2ejX5goLlR2Rq2eTVfAFo8WhSkIa8mXdLfRsAKxugEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnZAzpioyTogLoQE10thloOY7n7PiFS_tqNZeAZ7tChq-DQH_YFCOGSt1h31bnNirk_QvHA5atF9vqXQErqRBzctsIxaLBWDqmEVqZrq9_Ycjyae4ggAJakdWzV0a4by3Czk48p-AbEqmMxt3RNfihsXZSbzQSm_cfOWY3dloe622Otv_IADqUwgN61Y7V1DhQlJNefQblfA6-ivY7jfZPHLVcKHTZwnr4raPOdU9ZyP1HhhQdCe27j7t8gtr7uoIJGdmumH_55gJY88ZaQhZElohjXgdl3azBFbqldQiANEed7JdBSQBsRdm9rB7jd1_SSYvVtdHxIEeHS0cAEIDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opHx3cLjWkJHk21FZDQxnbnJ2e4GMe2h7DTQ6syHNU4zyeCUyoEeFkpl-ES1iGWPLn_TZ4AQv2NjNzNNV8C951ebjVRgBI_vzHKSS_GfrS1fQiCe2NohX9RnGy98dMCoTcg9dRU5MdbXQyTgryANEkGq_EwW_wCbz1Xsgq72juShfLzcXzRm_UrFDXaAFL9tMnCkBIVfWNyD37SDS0Ps4uQfuYCdDd560wWOLDZdz1msbVnNJo7YPwE8KHx9kdBXQt8NcFef_pY2ZNhBS0v3xFFGYmo5qDpWQx92ewqRhcILEB6lbenfLHjZUT8owFvsRm85fNdlWXQza5kHs8tnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMUfYBloVJ-oAE_0eNw-wmPNDjAP-qNHpsSLESkzmG7VmbqR-oRhM3ubQeP8II9XyyGzwvzNAJ8BJjMj5gay96Wza53ZuQEu8muUqi4Z9kKXA_3AKtNWQdeRkFSOHoKQ83WRa5v6SMcwtgrmFkxHT45BcHzyYqiAgNRESGF2Pmo_XW__rMkvhHMDhecnCHmOnu3yooGvm1BEvjw-e6uTV76rW8wO-bpa5oi0M2A_HT_dfDBT-S_HmX7MttoylclIC9nqyZg6zA-3WJf_58aswWjXhIbWqgZtH3A7QPrCPLvibzj4HBXDJe9nnffedKl66_-qj_PQf5W0UhgZAjSxsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkMEuAyFivXWZ8TfEYV6DEz3rsWC_XAkdNU5ySZn56VDZpYt0s2HX_KtCvgaUIzcDFBY8lcJ8hSxp5g2ED1x2siVDMNcyoMKzdHbxd5D9o0CKODm15WTxws9OfypiEApWxjqtEY2r34O-v3VWxCtsLYopuwyq83lK6P_OWvXu_h26ZONYkrSbuSwtnOvHf5VIanpOSBo8-r1OIvWeqq8j44VX4-61KCFoi84uCFAEU2O3Oi8IOSwlZVEtudU7DM7_Oq6Nk4_uvvfxgnP4uhOMqMoAZVFXZi3h5mZxo73tbMgVnSXrpAWkI4isphU9aH-lmQzxMqN2v-LzGS1w1PTYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=EYPeXU7f77nWfUKJ1Raxkva7zCt9hIaB8QGcGHsNUC-hEM7qIp_Q4GTKZGNDTLdQdJR8voiG2yyG5WvE14d5ovAItJvyEh_FttY8wHZ6ydwGlU4fnJ16VWYrj-fOoVUoG5kn_Hp2gdSZBH44iScCevQGyRINDuWSlb-N7Ky31crsshwbq1QZ2IgVf2XFSJ_HxRUZT7FcKdnZHpQwidHt5HuWjM1Qe0RDYWT3cSvfT0dBk0iklMoxdy62JGE1JzCpiLCbaK8Od9ut0GcC9wJT6MnyGK0eRnoUJEZXS99dYRPQL3B2T0aS2A_DLtL_YfhuZBX6mAf73P3OG4fXkff0ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=EYPeXU7f77nWfUKJ1Raxkva7zCt9hIaB8QGcGHsNUC-hEM7qIp_Q4GTKZGNDTLdQdJR8voiG2yyG5WvE14d5ovAItJvyEh_FttY8wHZ6ydwGlU4fnJ16VWYrj-fOoVUoG5kn_Hp2gdSZBH44iScCevQGyRINDuWSlb-N7Ky31crsshwbq1QZ2IgVf2XFSJ_HxRUZT7FcKdnZHpQwidHt5HuWjM1Qe0RDYWT3cSvfT0dBk0iklMoxdy62JGE1JzCpiLCbaK8Od9ut0GcC9wJT6MnyGK0eRnoUJEZXS99dYRPQL3B2T0aS2A_DLtL_YfhuZBX6mAf73P3OG4fXkff0ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=d7YAfGU0i0hAHvu7IOvcuAUXSCM3Y3ZhvbtjIHMWF-C1LSoR-wZh77yoFtcSH6ykwA0F_y5cCyM8T1m1h5tmxVnEQlMsMWs4Iz8-E5rdBOf_LGmYtS4839DbAZtwTauoemojsIRxB5kkp_TuTT7hAdj3d91NOJfbuce0ptgXpi46RCI1V_FVP96pnFoVNBlWyXpanXhAFUWWJx56RFDnXdvBKUsOu4_oe3f8UgVnbHcd2PAvGonbhXhlLvz4QXlnJ9oniJDTrBbRmK0IK4TVyq_6HgqO6dFLjhYiVTltw25_OJ0G_oCkD1MoZyxX4Enb-Fd1QJjTjaAu0gGLPy3NgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=d7YAfGU0i0hAHvu7IOvcuAUXSCM3Y3ZhvbtjIHMWF-C1LSoR-wZh77yoFtcSH6ykwA0F_y5cCyM8T1m1h5tmxVnEQlMsMWs4Iz8-E5rdBOf_LGmYtS4839DbAZtwTauoemojsIRxB5kkp_TuTT7hAdj3d91NOJfbuce0ptgXpi46RCI1V_FVP96pnFoVNBlWyXpanXhAFUWWJx56RFDnXdvBKUsOu4_oe3f8UgVnbHcd2PAvGonbhXhlLvz4QXlnJ9oniJDTrBbRmK0IK4TVyq_6HgqO6dFLjhYiVTltw25_OJ0G_oCkD1MoZyxX4Enb-Fd1QJjTjaAu0gGLPy3NgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=RoUcUZg6aOKAGr0ZSc_BX64vOdmk1jdBqBA5VpTSj-Me-EL08fajFGahhDUxD7isJEvhB2Z2CjahaP0n7Kz-DOQSb2NfSiIvbY9HTYFJZ5Z7lyQGlwPkSmMXsID51LLuvFCJy-ev2GhBz8WOQfUKcMZfPlpWl6g91y1Qqmzhmvz80IuL--t6ur_BZXHW1YK0ZwD0nsbEvtzW0dhNZ2NuTBJgHp1gogRqSlNP5PniPbMZHoneDhMg64Q_QcoBxAq1OpbihkrKYQK906D-0bQrjHaUb72ty0g3wTBgLQQgSbqlqqRoAaiFe_dQNx7c2wuWLJYKgytBEVCIZWruRGwwAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=RoUcUZg6aOKAGr0ZSc_BX64vOdmk1jdBqBA5VpTSj-Me-EL08fajFGahhDUxD7isJEvhB2Z2CjahaP0n7Kz-DOQSb2NfSiIvbY9HTYFJZ5Z7lyQGlwPkSmMXsID51LLuvFCJy-ev2GhBz8WOQfUKcMZfPlpWl6g91y1Qqmzhmvz80IuL--t6ur_BZXHW1YK0ZwD0nsbEvtzW0dhNZ2NuTBJgHp1gogRqSlNP5PniPbMZHoneDhMg64Q_QcoBxAq1OpbihkrKYQK906D-0bQrjHaUb72ty0g3wTBgLQQgSbqlqqRoAaiFe_dQNx7c2wuWLJYKgytBEVCIZWruRGwwAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=ChDUshMqdy-hmFRDIKl59F8vkh5AuLx7WNLS4LF4BFidtYMLdHX_OMTwRgaLJdoJdczOOBzTquNs0BmYmnIKxqzisWTudZxJGOKjCwp0HnJQ_U2xCyVFyuGCi8HWI7B0_Qh63YCdIFLYDD4peWRZ24OqAEuoJUxud3aa1uY2HTK3i_HAgqXjnh0xE1GdOKtMoCnopVEHACRUcdMi8EOEIFcDaX1aQNae8-U-fsCZRes7W0zyS5asj9tngAtRehgc3IH0YYW9o7zxSzrCbsVzpFK6LppZyQ9jLBX0ALBYuIACjhAKTYWRHfNv6Y4RzkKRkVvZS9c8Ea-COj9VeEkfjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=ChDUshMqdy-hmFRDIKl59F8vkh5AuLx7WNLS4LF4BFidtYMLdHX_OMTwRgaLJdoJdczOOBzTquNs0BmYmnIKxqzisWTudZxJGOKjCwp0HnJQ_U2xCyVFyuGCi8HWI7B0_Qh63YCdIFLYDD4peWRZ24OqAEuoJUxud3aa1uY2HTK3i_HAgqXjnh0xE1GdOKtMoCnopVEHACRUcdMi8EOEIFcDaX1aQNae8-U-fsCZRes7W0zyS5asj9tngAtRehgc3IH0YYW9o7zxSzrCbsVzpFK6LppZyQ9jLBX0ALBYuIACjhAKTYWRHfNv6Y4RzkKRkVvZS9c8Ea-COj9VeEkfjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=oIEWjZVcyq6ncfKmTW_hGHyAxf99VDJhyAGgybfFk_9gz14dxjjAQTWLU8PZO052d7rUo9xQa4O19F33GjTrdSfx14zd7CfciwtvHeJvWGjba9EMbsTpxDf9oR6BDM_8HzMs9QvvUinb_V0l9DqKj2mgOJ1R35O-DX_XFZZCziqEewCNnNq3lAcuR-1-les2_fl9zxvflUpywxZpR7eF04FvwIJnkx__0wDgD5Cr_SnGfGo9cgQqFRbaKxQEXLS9iug-ioslbDeuq30CiQebZdix7IqwYgJKbRCjNYWhinLgRwIs0wHsuqu6s5avOKxzRQrr8b-WH6fXRuS86f9z9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=oIEWjZVcyq6ncfKmTW_hGHyAxf99VDJhyAGgybfFk_9gz14dxjjAQTWLU8PZO052d7rUo9xQa4O19F33GjTrdSfx14zd7CfciwtvHeJvWGjba9EMbsTpxDf9oR6BDM_8HzMs9QvvUinb_V0l9DqKj2mgOJ1R35O-DX_XFZZCziqEewCNnNq3lAcuR-1-les2_fl9zxvflUpywxZpR7eF04FvwIJnkx__0wDgD5Cr_SnGfGo9cgQqFRbaKxQEXLS9iug-ioslbDeuq30CiQebZdix7IqwYgJKbRCjNYWhinLgRwIs0wHsuqu6s5avOKxzRQrr8b-WH6fXRuS86f9z9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=ZXbhjszlb8_5-QreYZwNMSFgKt6QxHgmP5hqQsIs3M-lLZotuCy_TPT5CGFN2qWKRBLLwPbaxLda4g9dGLZlLXDT3pKMjdV4Abz4S1GkXQ00oBW8TaWkHgKeEFv1sealb0EbZac6_HKXuud3ZvDQ3HoEOoBtlvHPf9azAQb3e2s4IVaegyNVc97IkUlpr-Q1FertpZZ34lMEhyrfe8XM4AQiuDLWyRX2dned6U8VPMq6ILjREQmpS5okFa2sX2EcRkv4x5hOY0yaQURl-3fNxkxLoWvPqlPxaybMPCK5Nsm98BPqeE0eJmy-Qo1jB6S5cMaxLcrRNBJe5R5Cz1wlGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=ZXbhjszlb8_5-QreYZwNMSFgKt6QxHgmP5hqQsIs3M-lLZotuCy_TPT5CGFN2qWKRBLLwPbaxLda4g9dGLZlLXDT3pKMjdV4Abz4S1GkXQ00oBW8TaWkHgKeEFv1sealb0EbZac6_HKXuud3ZvDQ3HoEOoBtlvHPf9azAQb3e2s4IVaegyNVc97IkUlpr-Q1FertpZZ34lMEhyrfe8XM4AQiuDLWyRX2dned6U8VPMq6ILjREQmpS5okFa2sX2EcRkv4x5hOY0yaQURl-3fNxkxLoWvPqlPxaybMPCK5Nsm98BPqeE0eJmy-Qo1jB6S5cMaxLcrRNBJe5R5Cz1wlGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmb9wmvf8-NoqB3km5ocUV7yq00Jn91ksaMNfdV5Zoh1ONjrOB8hlTFWkvXnaBItWCDH402UhgvQXD3rn_I4e4xqJHUWgUperW6bowuIN4rpJ3qoki2mb7qbnbILxcgK90AYgfTNY4HNX0OdOhtrWzXH_6mQr01zYVbcCAtRWkyMKxEUrQXc57JJTd4IbPnR85EZTLe2v-EI24x_miebEtaJx1KpNho56B-Nj05473jY0A2Pw_OiJjhpbOqcfBVlxoaTO4b4rgmVMzN3nZN1J0TxNzrHOvlHtPyE306RgYJIobHcFq_ohuJc8FNUljoFL0fkT23PGgx1kcD6ipYDqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljJecY1VIYBpShceC4U82vvwjafyVvt6tEQagavVNcnVWViSUyjogOvdbzFfc0JzxHEX-vLuV68glQEVpuvLjxHB8UK7Ij6CHDEy9WKk4HqARzAtXDhwpVbVDbfy5Pzj66IK_Zis72fh13UxWh3c5XF2HAVyzTX_Bce1qMh-L56gO0-yYqeF2pOuc_Q2ggtykeOYsIvdiRhg6_ion5BjK_7pEl4EqlsLmsCfAqyq8cat58bz4q544Ow1ziOVRRZ6Dt-Uz6C5cVK329nPm0mC9KR814M3W5rmQjg_G5L4iyofeYSFEs4wc5eWsDPvUPjeV_8Fo0zpCCCs4ogw8xxNKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YA9N4zXvCSejtYQq-g0TE7e1UKIjXePiY3TH25L-Piv_xYgqm-k1NAQW6qIqBUs7FITtp1K0fqAmvjtChFXuBlrJEW_PkK6eAPObysudz_DGUbWAEklG1OAJ6RypBXowe8j4I1wrbVW1_eAM3UsUMzQaK6WprC1_UM3DkTlURdcxJglZ4KslOLe0cSG1mRJUmUqM3y4JkzrvuY9u3-YWuKtBFB8o_5psUslmE4u2_8OKeZLnegDZOcf7nrsmjB8B4aa6nvGtl9nxBm7K4zKnE9qvj0pMRL_hHE7cemowrMuMau1M0ogK-TZeNJbZPCgdW25oKksmHKnj84g55cPjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=aFeXGI5F5t_2ypm5sLdDO_mH4cJuOgNjSugLRiiteyM59og4dxkrXxo_n_ywZ6IeZeeFSfAlMhrLocZRyLcvV29P8GPX8XjUNVm3PmFpKlVJ0v9ThqSAyEtbvHjc4Nya8z-84BazF2ZlZU8E4K2bpGpoweH147Ha-ad4KtezcVagw-IPEmX3Te3XdQp4nVzufMBtgaqj338dCXqD8GVp-VUc8aInaaOHBRna1chAphdplDIcT6ZnPsRxs6Dpd8bcTzd7Bi56m93_g6zUwqKoSRGgCR4sxTMJwJz-TJey3T7fcjoTGXwYhyiel7aClPReSqySk7TredPF57iaX7qN5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=aFeXGI5F5t_2ypm5sLdDO_mH4cJuOgNjSugLRiiteyM59og4dxkrXxo_n_ywZ6IeZeeFSfAlMhrLocZRyLcvV29P8GPX8XjUNVm3PmFpKlVJ0v9ThqSAyEtbvHjc4Nya8z-84BazF2ZlZU8E4K2bpGpoweH147Ha-ad4KtezcVagw-IPEmX3Te3XdQp4nVzufMBtgaqj338dCXqD8GVp-VUc8aInaaOHBRna1chAphdplDIcT6ZnPsRxs6Dpd8bcTzd7Bi56m93_g6zUwqKoSRGgCR4sxTMJwJz-TJey3T7fcjoTGXwYhyiel7aClPReSqySk7TredPF57iaX7qN5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuhXYl9g_Z3S7THBVPkIvOCe8fZapD3sieP-9TFJrS6NwwfyNskUZuVrNn5-nPMQls5AP86APP-3MXXm9rvchtgQUfbXbh-702QgKxNGBb0bKMfL3B80FTnvykBz5gdVsBsfl9ePAR6jS2eUv5kFP1Y_Gj6jW1vkKIBbDVNKEbRgwdOkrUjcG9i_PXBCRKpvQkv1d6TnUY7HCacViw_XRkb-L1HAHQ-v1DYxzmaNp1veOA9xYaUy_rGR-h5Scji4Oq4LNaKgLeoD7zJfN9-QuxFWzCIkYXaKtUQIIrpyQwK0rjYm-vtRtwiS-f2POziCaN0lNgFywJfZo16lx5BI7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbGtbSVmL5LtmFDEAFViYdsBOqFoFM4GK0FUvK8mcFjZ3RqIZ_7IVCbkAxIC6L00JdPDeNfyos0soYkvhHep7VPLEOdlUmFu2BsH7Wr9YDnSaokVptVd1CuUSWA3ALX-EJZa6Vm9JGije7H4eAF0D-v5T3eKNV6alG-v_rFmkOkresVqZxpqiY7XsHMWNqQ1kh3SClIQj5hDU9GilEt7pyw-mIzzHJm9eTSLb-WjyPXs_a2alwIEDMM79BsKtAu6gpfvbPXVabKmsd7G36vA_Y9KFqQpnVu2tYd0tX7vk-xokYN9e4jsdkmAJx-9zlQ1oBUufhDgo--pETh101ODqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=AEzZildFH5a1XP1rd-Jg66hMgeOsyZGYOXotTsoBE3Hb0sGPoJcuAyzIWJ3esnMNJkKN6qug-4nnJzozS6AxQgFJWF_G4ZJOgJxUv_T6gzl89Sx54VbS17hWYDL3AYxQQNTCBMcfaENlXpmhjT6HaYjxBVrDiz06qV2PRwLgjFYhJs9B5LqNTbJe2smz8dtUbqJmUBhI5urziRO30xuVeK38RkIROaXN1m3E3q5WHPY53IP0uQog2Bb9z8BMlxfe3B02QhLywya5vEq-nK4ftnPwcKHS4mggb0s8JGTxUdLQPRu0yi6BmjNpArQo2wMQWKCnvFRZ96lSH0slRo8Fdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=AEzZildFH5a1XP1rd-Jg66hMgeOsyZGYOXotTsoBE3Hb0sGPoJcuAyzIWJ3esnMNJkKN6qug-4nnJzozS6AxQgFJWF_G4ZJOgJxUv_T6gzl89Sx54VbS17hWYDL3AYxQQNTCBMcfaENlXpmhjT6HaYjxBVrDiz06qV2PRwLgjFYhJs9B5LqNTbJe2smz8dtUbqJmUBhI5urziRO30xuVeK38RkIROaXN1m3E3q5WHPY53IP0uQog2Bb9z8BMlxfe3B02QhLywya5vEq-nK4ftnPwcKHS4mggb0s8JGTxUdLQPRu0yi6BmjNpArQo2wMQWKCnvFRZ96lSH0slRo8Fdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoLoDjRk1xjNOiq6_lXfUJ_QZ4ZMOaFrxi5PhUHrSZGjyAewQxaKOi48oDotm6QTr-yUPFMFbED6ApIFvgcyto7LbHz_2PqaeXkPjCSFaypSatBy2I9mRRaV_T22iHtYdF20FEoK5oZtRPh2C3CYRWCf-p1GttmPP-Ju153ItuTjPWYr1ch6M4kZdxvXN4WxTzCAfVTWbqKPRtDWvZpSTutpyBzNwO8rXUzY4S8madkd35aHK0P_J8sP4KyRx4VIV5a6KhVj76Dbc_BKUNDJoBBz9o3-H5pl-yIcHFkpd-oKOwqrsX49aihqzxoPIW3EQtgSnzrvWUxAEqOw5YY-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avUR0qWBp957j78CZp5h_CwWr95F9T_2M4OIwleeGCAlUFNZPdmrBXYV5oE02isKtAKIsCERO7uLYGMVL-vbjtF0rV-9E9xTZ7xhXXzJyXelqM02KnFxOSioCd4izrrx23yMakV9669GTatxs2lGTBVH5ICKmCwOf0soRzCUtgAQKaq5qjhjdZ5qeY6l6zb3SGNUAaZgaB0KzUoCYDhISc357Mwt87f5gXRRPcEuphsWrjGmauUZa6cerEIpVuasMspWuCjiD_FDJ8INwhzdZgGOSxmQtNOSdj1KqWzTxRaSDSXC3eOGUn_srr4cMyHnC4xFqIzaV_s9ttQQ-V4FEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ttva1DLZ2aEnba41XZyfVBKhYp4i3d73BypW1_5sbKnQ-nPXT5iFc6lZ5bAVCqKkBqhTi-3MPSfsvoddqKYjfpMyWW7hoiQI0sBj9S2DgStj7OexdzXy3jr9HqQ1lWXXZrCo9_k2RTxTmLKXqTb0mJlk1XAcuWMmRtkjzujtdXv7XKGeII8hFemV1OpgXieX0fnRr9bxFZmvcAcwTZOi7-D63Fpm85J0rMd6SqG0AyjS4wykwudHC_EW0K7iu9J2NvMcF33gpZQNLi0O641LD7tQ1bLOJ2oTOjI3k7D8CEyU2gtGHr94CUHUSFzilW-22tG_CHc2se6Mf8fb87wcAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEDbfI2sxqzkZ-kI1Mk9ecd9Bo-IQSkGwh7ironkTtPxHyx-K98d5wimwZ0Dsr2OlbJ-k2qNgNJmLSB-9Wf6MtizGFzUEuezUjGzSs0_cTW9s-HQpbwGQ_53UqWrAIdIONrn5ttrV7m83q7OIMGDxKkamAGrWDNTQLBI59cnOOxsV4F7NCNxb85NUBtFGqfmDc8lTW_P-8IZPlR5SItZvZ3xQ6rPYE7QEUvP-5IY7D3KTAqC8tYdmeG1DHzRsrH_4N6lq5k7anfIjR3iZMCqC_7GNB63GxjMvUe97QuLRjwU8QC9jXqeaaDSZdA_Htqxx8NLLOi888bWI68NLiBk1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=JNqjyR3lmPvWtplz9GDBELp7hOLp1wCZkl9a5NTvLZw6IxWf3IOMlEiJfKWLPcyMKETHN80wnyq1LuTyNx98hxrHWayw-C4U_4WF83MNGPTgzSvSgOFa-D2H8VMdJmPmegmlpyh9FyMErP9SSRqtw1aYhKXJAGSil29vuynrZTP82bAfDEhikw7X4zJWt8n09aYkepwYRnDM4J0_DpmJY9mG0O9tufHBZlv0PCqNegvA8rmIFfrAJ7eWFmUZqNZGa0ofe28XbHxi-JV-6r_RL2OR9aommLSiRju4VdreGyIouEVPh42mur4XfWlM1X-fywis5nRUG8P9c52R9ZLGqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=JNqjyR3lmPvWtplz9GDBELp7hOLp1wCZkl9a5NTvLZw6IxWf3IOMlEiJfKWLPcyMKETHN80wnyq1LuTyNx98hxrHWayw-C4U_4WF83MNGPTgzSvSgOFa-D2H8VMdJmPmegmlpyh9FyMErP9SSRqtw1aYhKXJAGSil29vuynrZTP82bAfDEhikw7X4zJWt8n09aYkepwYRnDM4J0_DpmJY9mG0O9tufHBZlv0PCqNegvA8rmIFfrAJ7eWFmUZqNZGa0ofe28XbHxi-JV-6r_RL2OR9aommLSiRju4VdreGyIouEVPh42mur4XfWlM1X-fywis5nRUG8P9c52R9ZLGqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=ncSD0pSmpH03y5V_UMOepxFvkJmwQlFdlQieKQ0IChd_iMVs9wz83BoXxhr6j3EG-IvWWVJqOly3JQ4LSKCrGHM4nCq0XqLTIGjcLCH2pgP7pJ0JLF7Viqszu0B0BOgtwtkkKf_0JbcQM28PxUdpGPZTHzbF08PnxrrYkLXdoZs_7x4tSAUI7puohBW_OrLm1eL7YUDz7OkcbMZu6RHXIie3oKVN6uF3z-xkOQUrbILsAwBztd1A5QXmZ2aiEmd2lfRsWL9JAqXwviWYH6cmrGwd2cDDTZjBf08BeTyM2kwATnic0GrDzu65iBNJaT3NbFkuCVQzg03E8dlnWvfCzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=ncSD0pSmpH03y5V_UMOepxFvkJmwQlFdlQieKQ0IChd_iMVs9wz83BoXxhr6j3EG-IvWWVJqOly3JQ4LSKCrGHM4nCq0XqLTIGjcLCH2pgP7pJ0JLF7Viqszu0B0BOgtwtkkKf_0JbcQM28PxUdpGPZTHzbF08PnxrrYkLXdoZs_7x4tSAUI7puohBW_OrLm1eL7YUDz7OkcbMZu6RHXIie3oKVN6uF3z-xkOQUrbILsAwBztd1A5QXmZ2aiEmd2lfRsWL9JAqXwviWYH6cmrGwd2cDDTZjBf08BeTyM2kwATnic0GrDzu65iBNJaT3NbFkuCVQzg03E8dlnWvfCzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWGxr3YdhaLXZXfXEU-ov-Ibh3sSmPksm2KjzmUAvyxpBAgLykdpuo1vqBSaSZBvX1CTSRdI3EUckWdU7x_Jp3vQf_2yU0dXe8Pismsz_nUoh5jIZTJMvzDOENT3VhOX0fDLK6YhfFB1R3Dbm2-LzBfqBeyrIY6YkdtpMEZzj2e0Y2MVCeHiVgACaWRufV2bdDPiOTq1Xw9q_1JH2Em8TOMSZdB3O_lwEs8WNo1JQVogeZiNc8tc35tt8ST4gDUSrTnq5CUx7R3AYyNwQDBSFxrZNCn4rQm3U6YRDGX2c4gX_irZWfzQLJ1LCvgEF_kqANttTF9qPjMCF6P4CmDymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=TLohzgLMtjx-wBp1gvYlPfw9ZaOQLc96Yk2ymmOoqTbxr_s8LIMQvr9T2iHl3DC_IH3qmCO4fLeRge9c3YUKXqATjkneNfiXcAyeKFz2Ni03J2MkJfrNKjRUEnwI3qX0psCy9L44N55eUxjoczoUKA5co4LO-sxofjEz5vT_BOSowgm0ov_oXK2EUU7JYBrSVXMzomlyaQOa3g__iYrbaPJG280mlAnJ7tttU9F-wjbpECxl-Stl29kDTPRs43aYbj1A4Tu0c4mR0sFWJWC2StoNTu500RGfkayEFmpMJBAK8qTLk_SS3xHY49mvHigYxv_GfTx6xkgLVqWJxWkuLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=TLohzgLMtjx-wBp1gvYlPfw9ZaOQLc96Yk2ymmOoqTbxr_s8LIMQvr9T2iHl3DC_IH3qmCO4fLeRge9c3YUKXqATjkneNfiXcAyeKFz2Ni03J2MkJfrNKjRUEnwI3qX0psCy9L44N55eUxjoczoUKA5co4LO-sxofjEz5vT_BOSowgm0ov_oXK2EUU7JYBrSVXMzomlyaQOa3g__iYrbaPJG280mlAnJ7tttU9F-wjbpECxl-Stl29kDTPRs43aYbj1A4Tu0c4mR0sFWJWC2StoNTu500RGfkayEFmpMJBAK8qTLk_SS3xHY49mvHigYxv_GfTx6xkgLVqWJxWkuLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=TOMN7_3snBUpJUtnLYGZKq32D7JKT8HKnMeWB2FLGKO8qhR6V0a4ozBkQ72s4AqOaFvJS4KUnSoySp6DIrLP889qrJb8Wcx5HxiivuQzHvL7ywdcW4pxRmFfYHO3qx0-yj3_RUYtsZdYBKKna7viDwJ2-uhyG2p5zpMmyR2OA34p4-QA5yCRkVohpHiit_tK6GJ78mmvfs8_McTvwAlvQK6wT4IcLiDCHnUkvue4EXXXNYfw1qZ9bPujUSyNGWtoB4mwW-Z80vNr62ztyKu6kY_564Rt45JwqBc1miSJbLmazBTbS16glQJn8txksXvcywG85v7nI64LhhGRzaTX6mAuvq7WpxOmrEleamvbu-5CXRgzJs9Bg_VPbiSWujNaKdPnqDZ2qUck6WlUhsd7-OTRI3cihKNt-0xH3Sjc5fShM7UHy6culsUGAVRCTkvvw8o6AvdDY7083-JR4n9WcpiLrwQwfx-qDtlFUxgoGkGW08P3lLxiTlWYJVKPdX0lAxlQB0dLoIdxEeWrEhQFHuPDzthULww-NXw7jQ6Sqqmr2rsEkWOPDqceND1IgJtzRafq8o4mK7pVD-Twq4ivICxxT6AlPfoesArDPYD9TTAdEO4nMs00pppihY24sTCNjVV6nym2BRJNeTcX1AN_eXLRoaIh_bvXo5Duh4NPq78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=TOMN7_3snBUpJUtnLYGZKq32D7JKT8HKnMeWB2FLGKO8qhR6V0a4ozBkQ72s4AqOaFvJS4KUnSoySp6DIrLP889qrJb8Wcx5HxiivuQzHvL7ywdcW4pxRmFfYHO3qx0-yj3_RUYtsZdYBKKna7viDwJ2-uhyG2p5zpMmyR2OA34p4-QA5yCRkVohpHiit_tK6GJ78mmvfs8_McTvwAlvQK6wT4IcLiDCHnUkvue4EXXXNYfw1qZ9bPujUSyNGWtoB4mwW-Z80vNr62ztyKu6kY_564Rt45JwqBc1miSJbLmazBTbS16glQJn8txksXvcywG85v7nI64LhhGRzaTX6mAuvq7WpxOmrEleamvbu-5CXRgzJs9Bg_VPbiSWujNaKdPnqDZ2qUck6WlUhsd7-OTRI3cihKNt-0xH3Sjc5fShM7UHy6culsUGAVRCTkvvw8o6AvdDY7083-JR4n9WcpiLrwQwfx-qDtlFUxgoGkGW08P3lLxiTlWYJVKPdX0lAxlQB0dLoIdxEeWrEhQFHuPDzthULww-NXw7jQ6Sqqmr2rsEkWOPDqceND1IgJtzRafq8o4mK7pVD-Twq4ivICxxT6AlPfoesArDPYD9TTAdEO4nMs00pppihY24sTCNjVV6nym2BRJNeTcX1AN_eXLRoaIh_bvXo5Duh4NPq78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL-z8hY5KTYbjLWILynvIkePq2hU3T5xFznW7Kw03_nclkNTUSc5Fx1V05O0iKZEMHuwR0HnSCxcYN1LBfpCMZDVoSASphahFJYjKVCOQzQFjvlNAKlAiGTj4_kV8qzG_ESxEmFwd1xilHRketSj2ua7yIeL3oA90nnJlprDVkmJ-yFpGx7np7zpXx0RJwnx1xohZJOPL2WZFW3D2JJbwSOksPfBZPIYVlxDA9_HuHDsCYRXCTTac2D6ZjPJ8K8fvXkZwBnIXfrMyfrY2A-PBG7lSZPfQkUybOCG_DlQW8tUMkdYYHSMKodGuGsk01S7R1F1fP2tp1VLvcsqSDSXOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtORTFcQYVvg7yd6y7ze0f513hqLhYeItVvZ7so-hzla-KXQg2SKlLr9iOCUyFv6E5z-ZZ7iuOR9wUoWhkzT5AHA9vPr_xc9QAaDKejEE5a5HBApKeP7vgKqHY9ZsnqOwgLVldFir244ApptWeQZREl6W9pf9rUUlzNwBqPNm0jM38_JehYkEgKcU5tuSXk0Q19rJmQpfQWbeM-R-cDIbSkunfd16Ec43BD0Pdttn3hI2wkE5DGMX2wzbrKQwpRxq16-L2AC3Xn_uKxBDUVOYd2Ccp8NyYv-KU7x7HmVWeL_2X84sCKyhvnZfLu6PgQNfAeH5UPOvPzm5p5sSpNfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLRTDQVmgVX8L1gi44Df1qPnZNEGeRKl_fCfj6_GbySJ5vCr3QsVUG7CqHo3lpGxWbOo4vLNdnd2VVl_HG6Ux8Q1AW494QKWU5fv9LB47rFYEhs3Xo9CXwhDcEzomVjHJQ_IZ8QphOLognaPLtucPWfzP9SW9o1t3Nt6d6TkfF6y851_HooJnADauetNKYZoXKLUDq1er67_o7V79NOCaPL0-HiYlmP4UEIGuDjZEEg5dEGn67OFnmgsKrSbYa3U5xbyLnfcJ9Xxcq1PxHgXmAUTdKL5CvcVc1EJsvmtZBqqRv7ARdrel8GIpRMgnWWXs_VnMKrNiTg1i4Xn5fwsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6pDHg35qW2MNt8gF_7L9Ct41t9EU0nRy814YuKk2cCaMqih_DQnU4jPypCmgVV1XDa_tyIjGpsl04NYoBZCkDUbGv-UTm2BsE4z-bC0ziu4W8sV9j4CXV9zpl90QkpZ4lSxkQHYp7kGBeSydYNoZpG7gbfmC8dpLM-0elhM1asQkE0b1UbSI0Ji98M5LLGdcf9JgRlI0Hb3dTHMQVydMyQyNSpDxNoQp8ZKe78t2H_jxFzVqloQMBXbEmc30BIH5NyZNJIiaTV6Q9bCNL7D44xbgzd_6lewMaVInGbeiEPVoi90yNWXRJrpq_9JF7jQlY86SlXeXLSUdfXoP1CHVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PrclWQdm4SzxNPQxYc_X4fRt94eoz57jZiz2ipTPjC2lzj2zQtREs6Pj9K_WayM3fwVybs0omJmkwKAFLWu07sR1I60VDe-RF-ZkWlxwiWpEM2zZcnRKZXxExtk8gT4szULg661GjeaWT0BHTDwofP5M9GTHnD4GRuQ_XjKQWo33mw5s4uOUePLXgCytrt-7MnMPJrccE5QCHBXdNs_T-CxvmCagmnExuyw2OpJbwZXU5xIN8MX7uBuBBWz_x2dQ5Zl5cpMy5bidWf_9rXL3FIHRYeBjyZeXFYd_P1gWEYZrVECaeZAT_Hi8cQZjSSO11AxQyCl73ko9HOTLyxG7Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PrclWQdm4SzxNPQxYc_X4fRt94eoz57jZiz2ipTPjC2lzj2zQtREs6Pj9K_WayM3fwVybs0omJmkwKAFLWu07sR1I60VDe-RF-ZkWlxwiWpEM2zZcnRKZXxExtk8gT4szULg661GjeaWT0BHTDwofP5M9GTHnD4GRuQ_XjKQWo33mw5s4uOUePLXgCytrt-7MnMPJrccE5QCHBXdNs_T-CxvmCagmnExuyw2OpJbwZXU5xIN8MX7uBuBBWz_x2dQ5Zl5cpMy5bidWf_9rXL3FIHRYeBjyZeXFYd_P1gWEYZrVECaeZAT_Hi8cQZjSSO11AxQyCl73ko9HOTLyxG7Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpVJBtuw5j-_rtTzRFZHjOg51oWAn4esZnRbFNcUz6HtOsgcjSASOBGOkSEmgFrhf0EfeeVVNMcn0poVvkI0c0gMOF9sSx-hmoqJ7tThwSuZlY9ymDJXzCGN_SWcVC3XfOho6y2UOscgo4bI5Lk_7ZeFTCvT0pF6SnAvUJNMtgCGAjpnale-7E9_Uh3QOZPF6f3f3WaprQNhBB00Uh18W4hL1cuJ0HuZGDNAyQd2LXBrUlcmriHZTHQUpLPLmKrd-8P64nwWDsrgAaLqrPQKlYjLuDMESWownl_qvo9v6JXHS55R0DBEEUPRTkCsYRA7GSxXfe98iagAnRFO86q6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
