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
<img src="https://cdn4.telesco.pe/file/TXjFBB28p284z6vBwR0Ilz-KNyFcpfDSaPszQK124QlyEALApjLF0iWpR_KiTr7Tpnar2JZUAytd4Kih4fd_r-Ynj-0J3lJRhsv0m3HaulvP0td7qZEGtJblarRR7NzP--QhtckYI6aC3fwAPShB-k4xGrAk6WjG0qCCMXWJtcX17EBkLJSYnwntqx_1sVcn4lv1QkBEtMaGAv3d0q3gJ4J4sXqm36bNlQQzi1JH78zOXcTAZ5yuM2CDHAlEM3HZ9kSry2z2-FGC20q8QPwN2aDe9-GIKAW5q6Bbj7ZcZ-ze_2W4SAurtQq2bqcFTCYyP8Us5TskzNiUCfsH2OKSHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 13:38:24</div>
<hr>

<div class="tg-post" id="msg-463615">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">احتمال مجازی‌شدن مدارس در برخی مناطق جنوبی کشور
🔹
وزیر آموزش‌وپرورش: در کل کشور مدارس به‌صورت حضوری فعالیت می‌کنند؛ ممکن است در بعضی نقاط، به‌ویژه در حاشیهٔ خلیج فارس، مشکلاتی وجود داشته باشد که در این موارد استانداران تصمیم خواهند گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/farsna/463615" target="_blank">📅 13:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463614">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6agn9-B-IZPx3cV5n-J38w8v9NrYKEerhZST9Nbb5KDBkUiFe2lSCS0YoSfEiVAuRpSIrEtGAYN3Bn1kiVYD21Y4NVTbtNq2IAPU-YwjDfTcoex2EmrWz1QrVowe1eK-JbeXOvBlmhs0nlLoXZetLXMBAimg-E7rFjceFolNNUnX0sCLDzJ58kP4AAYMmBqMFks6D1Zs1fxEGoU9TKnCmfwVtXPOw9CfMjZImOT_HqXOdTJ2XO7iwJTEBD8ZEUt7H7dKfrJ6vl4vBq33Gxm9stjTs0t8D1kf_C6ByBp3mmJ2EKPJvNQUM8h2i2Bub3KBgc4PKvQ8OE9qKIDvxbaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان در پلی‌استیشن هم حریف ایران نشد
🔹
در رقابت‌های بازی‌های آسیایی ورزش‌های الکترونیک، ابوالفضل آقایی‌نسب از ایران در رشتۀ eFootball Mobile امجد عثمان از عربستان سعودی را ۳ بر صفر شکست داد.
🔹
حسن پاجانی هم در رشتۀ eFootball PC عبدالعزیز فلاح از عربستان را یک بر صفر برد.
🔹
بازیکنان ایران در بازی دوم مقابل کره‌جنوبی هم یک برد و یک تساوی به‌دست آوردند. در بازی سوم هم ۲ بار قطر را شکست دادند و به مرحلۀ حذفی رفتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/463614" target="_blank">📅 13:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463613">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-r-OsWwSDqryN_0cPik2jfLtYGR8v_lCW2_mnElcymLh_qSH_yU3aRy9nB6fRBSiFV9L5J0Ofyr8A50_mjEOBPyx4c6y-NnSLh1wyAmOZVjr2w6eMnmxMc47HHS2R8wn7vca5Y8UbfDRNJc_Y7FsXSClXqYfAfJPx9Pyno6jgwmTmHbMrtUzlEUk6-Ohm8v38KgYjW6Nwkduq7lZ5rXAt_wG9rCXyxx8LwvuwyfyO4jzcOHCYvFDrLOTWGbtS82gXfTJJm5cPN34kZ4d83qpdQixV8zSW95EMW6pCM2F5J19QB3gGMnMNFuhLOuPkwUY5uxV2TnnEsew9aiwMu3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون تیم رسانه‌ای عازم آمریکا می‌شود.</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/463613" target="_blank">📅 12:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463612">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0TB_D0zoig6zkqYQEt9Ed0hb0A8tLLk_edyjUlIhIURl2a44j8X8Ig6YcR9QOk9i6REPF2CyN_XXXfvea8vi-irMSXWtdafrNWjbL7ckcu3DI7N0T_KNPf2otY6hSC5iCeIJK2Wx_Za9HPhLLEdzJdOEHSk88MpmNrXV31NYKXZdWYKWeA6FbvcYQpixn9PZFTHWogInFajkbsHgUYdPm_JG37KsWCwtCIg-orlbn3zilUNvER6YPVqia0NUx3aC29VaOez6x2BcYXKZnPlyDEBF2cjJPypzahR1gKeehflFJ8SC6QGh9I2Mqx0hpB0T0zSfBl-pUShEUC3HDDINA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس صد هزار واحد دیگر هم ریخت
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۱۳ هزار واحدی به ۷ میلیون و ۱۶۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/463612" target="_blank">📅 12:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463611">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قالیباف: با موشک‌هایمان بدون محدودیت، به هر هدفی که بخواهیم شلیک‌ می‌کنیم
🔹
امسال اولین سالی است که فرمانده‌مان کنارمان نیست؛ اگر درایت و آینده‌نگری آقای شهید نبود، شاید الان فرهنگ دفاع مقدس اینطور به کمک کشور نمی‌آمد.
🔹
در سال‌هایی دفاع مقدس حتی به ما سیم…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/463611" target="_blank">📅 12:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463610">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0LqZCZZDOJiHieZ-CD68YPqd4EsWtkvq4NU9gErzL9WZZK-c1DCkgDnwbXPFdR8YXGwanw0ecIqOSco3D49PRhUHYX2il2VGdzLKcxupm9W9Jn_sX0kGtiaPt9BhXu0QD1uk9-6KUfwN2CyVPPRbhjgMs-XdyJQv5urBjFdTts5-1FpTRwQtyElbSxZIIbTr3FVQ2-YMVr3u6nkporMpJP_LTqxT3c9QCHIjLpVhgmF7Y3T_pDkwt0wm0Mric6A40wtuULk5aLYFW7Pes5EiID0ubXalpPAmKHoL3h5WW03P_Z3y0QXKMSOLs3qjxCk84zWf1Ha58Z6y1xvqYfLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: با موشک‌هایمان بدون محدودیت، به هر هدفی که بخواهیم شلیک‌ می‌کنیم
🔹
امسال اولین سالی است که فرمانده‌مان کنارمان نیست؛ اگر درایت و آینده‌نگری آقای شهید نبود، شاید الان فرهنگ دفاع مقدس اینطور به کمک کشور نمی‌آمد.
🔹
در سال‌هایی دفاع مقدس حتی به ما سیم خاردار نمی‌فروختند، و آتش توپ‌خانه‌های ما تا ۱۴-۱۵ کیلومتر آن طرف تر نمی‌رفت. درحالی‌که گلوله‌های توپ هم جیره‌بندی بود، اما این فرهنگ باعث شد امروز به جایی برسیم که هر نقطه‌ای را بخواهیم با موشک‌هایمان بدون محدودیت، مورد هدف قرار دهیم.
🔹
امروز در این جنگ ترکیبی، اقتصادی، نظامی و دیپلماسی هرگز تسلیم نمی‌شویم و ‌کشور را تعطیل نمی‌کنیم و با قدرت پاسخ خواهیم داد. همانطور که تاکنون پاسخ دادیم و دشمن را در همۀ عرصه‌ها عاجز کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/463610" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463609">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQJ9pg4HCoNhHB325vi0B0UqftTbI58c7F37lVksKndcZZprXpoE5cnssDrpmbCEGqn7FNMz-oUFL-YVaH6br5i1rQn_Cds0kd4b1ZRJsPVndBppDZDvDiVStw0L3UWMLqKTA3BNk8S2-TXF2oIJwhr1OrHH52YqIPHm1ara6pFqU8DM0TYI7cwhG_FbfVIt9JYBGfxRb6HFiGsN64bmwzatj2NnAklR9TpFXl10H6bgm0LVLjFf6s24x_DedhKG8ZRkCT7uKYDSk_Lhtht7an7ZRDH9W-4LIULmx8UZZOXojXjcgE9n8X6Bu6HSv7W2-K6WSVW8jPGvw7R70RZUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اول تا هشتم مهر نمی‌توان از ۲۰ روز اختیاری ورود رایگان به طرح ترافیک استفاده کرد</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/463609" target="_blank">📅 12:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463608">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5gWUPN-eoA64mFn554W-2U0JBYL9YLkm2YgpZFDnctIKZBX56sDTRTOmWpFsERuWBTamPAvnKIkfmCD_hW3lI5SEd1I1PdMFrllvFtkSn3vxxd6E2PSjeJnmzTONLJckL6SWNqhrF_glEoXymxk85Y7XH1eUhKqIW0UuQQDR_dBkCenOrk9Gz7Avp21d0_LxJ8Or95rni8efLmoTeM5ZeBOrRaEV0JCHRN6eGdS3xBXy3GniNu7Q5hTi8TQTaikp_QMwOjadGYhOFpjUXgbiXifroJXX0b-sThraimv6xkfh5cLHZ64K52d-60cGM4JspYrRIqooiWrDEAj5EE1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۷ درصد مطالبات چای‌کاران پرداخت شد
🔹
رئیس سازمان چای کشور: ۳۰۰ میلیارد تومان دیگر از مطالبات چای‌کاران پرداخت شد؛ با این پرداخت، مجموع مطالبات پرداخت‌شده به ۳ هزار و ۲۸۲ میلیارد تومان رسیده که معادل ۸۷ درصد کل مطالبات چای‌کاران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/463608" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463607">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516e39796d.mp4?token=n8veajQta9Mm-FhOYRNI1WofGaFXhqX-wPAM9Xe5cUcHrw_P5mfJvD9p4A2E7oPgJaSlKbRnZpDQri0UR3AW9Qq6TGs0fcUoB-ZDWJ2xG5RF6Q--6NMCkVjZaz9IO4__6FDanRzxAcbgq4pI6KQUhzSHOUeWYhuXg6d0YD98uxf0TwQ_KiMR_mS2knqAUHV9ud7SdgwpIJp-LQeIaEBXilBM4CX3pQ_DlEzTLfKc1YGJ4oaPcC_8CHmKxi5JSm-kfM3gQr780VkBRCcNbZrpJx9RCHyBZaYhDgy5GDRF83ttD6xvD7YiOpHHYBe7JB1ubWHvd5818a1M-2KJ0WoPhbe4NoYLc-7c5gByQUxSx_FSvzlMb_uNw0-itO0PkcyIniecCoJ_S4h5FcJyEQ-5BafWNanZTzwwYsltLBPTJgqLVa8bHnWkTUpPWW1Uf72otB6JwdfkHzYC20vFJSaUih2Xa9ozObdhu3u4GwMJKKeVyReHuI4A4NY-l8IeEj85nFq5BnzAV-03n2Ax6vFKsErEGhZTeIuLrwQo4_6HLus8gvWhkInIrh_t0M3G5h-Hh-1sD0UllDpRLnZXtsz23NQjpbnpMWOJkjN4EpzW2xfdGx2lUwUGzgYs8TlAXQ30iUhLLrszQezMqBOccTIssLPlcq9I8wr9cr_c4wv-PII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516e39796d.mp4?token=n8veajQta9Mm-FhOYRNI1WofGaFXhqX-wPAM9Xe5cUcHrw_P5mfJvD9p4A2E7oPgJaSlKbRnZpDQri0UR3AW9Qq6TGs0fcUoB-ZDWJ2xG5RF6Q--6NMCkVjZaz9IO4__6FDanRzxAcbgq4pI6KQUhzSHOUeWYhuXg6d0YD98uxf0TwQ_KiMR_mS2knqAUHV9ud7SdgwpIJp-LQeIaEBXilBM4CX3pQ_DlEzTLfKc1YGJ4oaPcC_8CHmKxi5JSm-kfM3gQr780VkBRCcNbZrpJx9RCHyBZaYhDgy5GDRF83ttD6xvD7YiOpHHYBe7JB1ubWHvd5818a1M-2KJ0WoPhbe4NoYLc-7c5gByQUxSx_FSvzlMb_uNw0-itO0PkcyIniecCoJ_S4h5FcJyEQ-5BafWNanZTzwwYsltLBPTJgqLVa8bHnWkTUpPWW1Uf72otB6JwdfkHzYC20vFJSaUih2Xa9ozObdhu3u4GwMJKKeVyReHuI4A4NY-l8IeEj85nFq5BnzAV-03n2Ax6vFKsErEGhZTeIuLrwQo4_6HLus8gvWhkInIrh_t0M3G5h-Hh-1sD0UllDpRLnZXtsz23NQjpbnpMWOJkjN4EpzW2xfdGx2lUwUGzgYs8TlAXQ30iUhLLrszQezMqBOccTIssLPlcq9I8wr9cr_c4wv-PII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانش‌آموزان جانباز مینابی ترس و دلهرهٔ هنگام وقوع این جنایت آمریکایی را روایت می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/463607" target="_blank">📅 12:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463606">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ed9869ef.mp4?token=djC__axzCUWv3vHa0OmypLkWtffpfFSsXzhCgo5ZLKhYjW_m7MyBV_M55OQoTi-fkwjVbfRNG8o-Q4qsB_zOTMJYSFH-4YVzjIqq6-VOUf5CIHW9fxCx7KkDqqmujiDHvf2Q4B1ZddMAuoysqWbOu01iBjv8gQNIQDCjUGtIRHfR70PRYxn6fwi2E5frOX5KgLy4RR8vvWvX1cBEoIGF7dui9HfwM287Wbk8YxSCDsz7B4GsLomqBYeZbiWPR8-DB9LswWJ976urzDYTohMN5zITgIHMWVHN4sWrfA2MIT6OoolYurj4lfJUBL2QS-jd2jPeMLBgRuYYEwOYZPmKPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ed9869ef.mp4?token=djC__axzCUWv3vHa0OmypLkWtffpfFSsXzhCgo5ZLKhYjW_m7MyBV_M55OQoTi-fkwjVbfRNG8o-Q4qsB_zOTMJYSFH-4YVzjIqq6-VOUf5CIHW9fxCx7KkDqqmujiDHvf2Q4B1ZddMAuoysqWbOu01iBjv8gQNIQDCjUGtIRHfR70PRYxn6fwi2E5frOX5KgLy4RR8vvWvX1cBEoIGF7dui9HfwM287Wbk8YxSCDsz7B4GsLomqBYeZbiWPR8-DB9LswWJ976urzDYTohMN5zITgIHMWVHN4sWrfA2MIT6OoolYurj4lfJUBL2QS-jd2jPeMLBgRuYYEwOYZPmKPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: دادستانی سبزوار به پروندهٔ تخریب ساختمان تاریخی وارد شد و ماشین‌آلات تخریب را توقیف کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/463606" target="_blank">📅 12:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463605">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc61292397.mp4?token=m0AZ4SxLZ2lHn5LC5fd1ziO083dhJfZ4PPRsO_d1SaPSEm7QiSxs6dyuDB3LSWG2yM6KmmCXlV8zOJSTTGge4TCLf0N-CLlBqMEtD5GxTFo0iS1ifNH7ny_iMI5Qc5CDk3jwF91UzSHPHmlUmQeOyUgYS-2zlz71QFL3C0cFokF4xexT1XdnnXsBJycwY1dzQdtWP6_U08HqK140SX_MslB-pP7YjP-mBnVGxshIP7Uxr1FwTwOcrqGFFD2UTJCDP7Bw2U4OxvowWdnHjUa6w95U1WJVKJNsxXvQbAR6GiIocWyXCg_HxrjGSb3PbYpH3qlbrO4Rp83OLt0WXH7G-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc61292397.mp4?token=m0AZ4SxLZ2lHn5LC5fd1ziO083dhJfZ4PPRsO_d1SaPSEm7QiSxs6dyuDB3LSWG2yM6KmmCXlV8zOJSTTGge4TCLf0N-CLlBqMEtD5GxTFo0iS1ifNH7ny_iMI5Qc5CDk3jwF91UzSHPHmlUmQeOyUgYS-2zlz71QFL3C0cFokF4xexT1XdnnXsBJycwY1dzQdtWP6_U08HqK140SX_MslB-pP7YjP-mBnVGxshIP7Uxr1FwTwOcrqGFFD2UTJCDP7Bw2U4OxvowWdnHjUa6w95U1WJVKJNsxXvQbAR6GiIocWyXCg_HxrjGSb3PbYpH3qlbrO4Rp83OLt0WXH7G-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: دربارهٔ اختلالات نظام بانکی، سازمان بازرسی بررسی‌ها را انجام داده و بانک‌های ضعیف را شناسایی کرده
🔹
هشدارهای لازم به برخی بانک‌ها اعلام شده و برخی پرونده‌ها هم به بانک مرکزی اعلام شده تا به تخلفات رسیدگی کند. @Farsna</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/463605" target="_blank">📅 12:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463604">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ql_GrOcbaR-r0E0v7wPZ6dVDofxjr_SoQlXTdG_KhZ3rzUD76tqC9WVjEJ-JyYNUHSG4YBYlH98X5liVQCoTkSduUo_RYXND0SN0W_5UhxQc0UWdV3h3HeSwn13skNpUxnF0BguSpJSRF-YC7kxBAQorQJ2W6umJnDJMkujXYVXRVrB_h1RFYXZAm9D2ryc3Mrn6d_i2zGUFl3QhaNnRzWjbiEDro7fMUM3bIwtZhvg6uF9ZhygT4iyOeN2ce01i6O_IkNgQ4fXGGOvt06yw2QBzel1bkVJ_tYQa5EhfNJG__hZQpL06PrK404cb7jJu14a6PnSKoTTAbAMhMId-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پینوکیو» فرماندۀ جنگ اقتصادی علیه ایران
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا فرماندۀ جنگ اقتصادی علیه ایران است. او در هفته‌های اخیر عملیات روانی را کلید زده و گفته‌هایی نظیر «افزایش صف بنزین در ایران» «رسیدن دلار در ایران به ۳۰۰ هزار تومان» و «تمام شدن نفت…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/463604" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463603">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fc0c690aa.mp4?token=k_CBebfRIlIXE2X0SoRMQG30WbPbXRericMaa5Nl7yVcoaUwel7L_q7pyiCg_AtWzQjU5pNDg7Eqc_r6mBq96haDJHXXYiO6uPEW24zuimm9a3rG9ho_azvsJpY0Y84e4FY-o8uCkAQpU25SGoXHkHeIlGBGv2zfM0isvw-EZHOZ_CxTuhRIhsrXKvq-VZ-pHUDA3klyqRX89b0qfMLRvqzj69y-PPzUwvsq7XZLGKN6hsOVdI98Gf0IrSk3SAB4SLm6T_xgK6g6ET9t6DtMSVL5Mjy5ShlK5he6dbo5JGtAXnNODggfKO2UHHvWI23eiWik-QFqwKLAzMQ-wIkPCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fc0c690aa.mp4?token=k_CBebfRIlIXE2X0SoRMQG30WbPbXRericMaa5Nl7yVcoaUwel7L_q7pyiCg_AtWzQjU5pNDg7Eqc_r6mBq96haDJHXXYiO6uPEW24zuimm9a3rG9ho_azvsJpY0Y84e4FY-o8uCkAQpU25SGoXHkHeIlGBGv2zfM0isvw-EZHOZ_CxTuhRIhsrXKvq-VZ-pHUDA3klyqRX89b0qfMLRvqzj69y-PPzUwvsq7XZLGKN6hsOVdI98Gf0IrSk3SAB4SLm6T_xgK6g6ET9t6DtMSVL5Mjy5ShlK5he6dbo5JGtAXnNODggfKO2UHHvWI23eiWik-QFqwKLAzMQ-wIkPCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا | نعمتی اولین طلای ایران را شکار کرد  کاراته‌کای وزن منفی ۷۵ ایران با شکست حریف ترکمنستانی به مدال طلایی آسیا رسید. @Sportfars</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/463603" target="_blank">📅 12:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463602">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbgafQWxFSOy9r7iFf8pHW9YHnhp47dchiVK1xqyKJjNlujznOq2rM9NXhsRWCHeJVigxEWMtw0Bc1u6azIWwbA4FrPvud3CCRUUHc2aE8AxOK998bdaIb8ZDNmRJwlHBwob18jO4l9Kn7SfcdLFaxCT0QfrQQknkdUoicBEnC4bj9G6R_x1U753c-0exVyl1xgBlZtK_uuliNQcY0icD1N4bVxSKQLMyRQ3s3R9FrnHl5bsNFjM_1PhabSdjIGV36jRGkEH_xEKegQdlvNDmcV0W42fhnNc6I7q-MGALTOolHnVthF81VzR84FvqgrJ3LMXHvuVUIfClpUzf_5bCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان‌باختن ۳ نفر به‌دلیل گازگرفتگی در غار چرام
🔹
اورژانس کهگیلویه‌وبویراحمد: درپی مسمومیت گازی روز گذشته در غاری در ارتفاعات چرام، ۲ نفر مصدوم شده و ۳ نفر جان باختند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/463602" target="_blank">📅 11:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463601">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b9d2454d.mp4?token=dTmTS8OR82wu3-pTHAjg0IgUKSRJ0QdsdP7DDWZiZWUr07XlikW1TQOdnjyy3j77eitkLyJ4aKQ4sjhrYzW5H1YFfvBaur1Y97RSzeaAfx6cojNz7lto5HhwfbXakyR9jQ5IZmBsfZJEZIlgtSQa1cg728TV5mQZbiahkZTLNbGLcNSo8gDTimju8EQVCJ_picEBmJx105zD3bonSQiKDISMS-b27inx5c5o6w1Cx9hFkNaXFQ69IChvu_vidWoUoIG3B3eqAuVynPAz7xVqnK76fRZ4blpGimn0UtTRyqzRkPjJYzSlsi8cGahP3ijErF6N1kPxhGFgoyRyVieMvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b9d2454d.mp4?token=dTmTS8OR82wu3-pTHAjg0IgUKSRJ0QdsdP7DDWZiZWUr07XlikW1TQOdnjyy3j77eitkLyJ4aKQ4sjhrYzW5H1YFfvBaur1Y97RSzeaAfx6cojNz7lto5HhwfbXakyR9jQ5IZmBsfZJEZIlgtSQa1cg728TV5mQZbiahkZTLNbGLcNSo8gDTimju8EQVCJ_picEBmJx105zD3bonSQiKDISMS-b27inx5c5o6w1Cx9hFkNaXFQ69IChvu_vidWoUoIG3B3eqAuVynPAz7xVqnK76fRZ4blpGimn0UtTRyqzRkPjJYzSlsi8cGahP3ijErF6N1kPxhGFgoyRyVieMvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین نقرۀ ناگویای ایران سهم بانوان کاتارو شد
🔹
تیم کاتای بانوان ایران در فینال بازی‌های آسیایی ناگویا با نتیجه ۱-۶ مقابل ویتنام شکست خوردند و به مدال نقره بسنده کردند.  @Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/463601" target="_blank">📅 11:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463600">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e95560c5.mp4?token=MZCWe2UTo6E-zwCedmvrlWXrGPHyXoU8gpvVHK0TrcmQHiMjl5wwWSrSMkcsCiXYQbL-Utc5exoq68V0d-INd2WUoSWJLMIIx9urjojWXBxTVBhpklKdJaqSTuD1t7xmac9UTrQFaJDKG8qTUjomxgoB5lk0y50dd-Dx6ix7IF2EE7jxyHWDkg78gVxgVObrovLb4ErhqE4u8Miwd1RnZ8fyGzUzAabh44p_yS_PAPVSJPdo-G-6nDODlJwatLB5hCj-vOVqvazXkXhaTRJgWmJbzxo8OMAmX3BRTp92uVerzm0PZaEnHsuVVdCV04UG4_fW3udpmf96y0p3wIhAiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e95560c5.mp4?token=MZCWe2UTo6E-zwCedmvrlWXrGPHyXoU8gpvVHK0TrcmQHiMjl5wwWSrSMkcsCiXYQbL-Utc5exoq68V0d-INd2WUoSWJLMIIx9urjojWXBxTVBhpklKdJaqSTuD1t7xmac9UTrQFaJDKG8qTUjomxgoB5lk0y50dd-Dx6ix7IF2EE7jxyHWDkg78gVxgVObrovLb4ErhqE4u8Miwd1RnZ8fyGzUzAabh44p_yS_PAPVSJPdo-G-6nDODlJwatLB5hCj-vOVqvazXkXhaTRJgWmJbzxo8OMAmX3BRTp92uVerzm0PZaEnHsuVVdCV04UG4_fW3udpmf96y0p3wIhAiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: خروج آمریکا از شورای حقوق بشر، یک پردهٔ دیگر از چهرهٔ دروغین حقوق بشری آمریکا برداشت
🔹
خروج آمریکا از این شورا صرفاً یک نمایش سیاسی بوده و ما گریبان آن‌ها را برای پیگیری حقوقی خون شهدای میناب و امام شهیدمان رها نخواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/463600" target="_blank">📅 11:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463599">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d16be13b9.mp4?token=UjSQyIKkn_s6sgGktgXQHU6IWU3Mt4JMjtP_qSSA-4qDYT0NbdGiHWc2fAcV-nGfh1-Up67lIhosdgr-7eWGWChV-k1eyEViZUVwP9kgrdOcpvd37r6TU1xYRYLlTAgelFyQuZNmleesf857Ne2o0nUFESdEBTITN692zG0YgdmaWHYfcZ5nYDOR46kSrd9cRX0yBQaGO3NKyYxWbm5D8CgL5M9ClkCXl8zyWVoYQo8y1L_EiNxTQFNdO-2SqJAkLIUTPChY_qNOOaWj_3JqSgdo3Apb-TKT8XGR2XOsVNpEv2HVzCg4b30x5zpvS3uixTdz6O9YbaeJktvzwcktLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d16be13b9.mp4?token=UjSQyIKkn_s6sgGktgXQHU6IWU3Mt4JMjtP_qSSA-4qDYT0NbdGiHWc2fAcV-nGfh1-Up67lIhosdgr-7eWGWChV-k1eyEViZUVwP9kgrdOcpvd37r6TU1xYRYLlTAgelFyQuZNmleesf857Ne2o0nUFESdEBTITN692zG0YgdmaWHYfcZ5nYDOR46kSrd9cRX0yBQaGO3NKyYxWbm5D8CgL5M9ClkCXl8zyWVoYQo8y1L_EiNxTQFNdO-2SqJAkLIUTPChY_qNOOaWj_3JqSgdo3Apb-TKT8XGR2XOsVNpEv2HVzCg4b30x5zpvS3uixTdz6O9YbaeJktvzwcktLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: ۷ سرشبکهٔ قاچاق سوخت در هرمزگان طی یک عملیات ۲ ساله بازداشت شدند و حساب‌ها، اموال و املاک ۷۵۳ قاچاقچی توقیف شده است.  @Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/463599" target="_blank">📅 11:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463598">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06554c8831.mp4?token=EFJYxBz4Hx4SRQuvOQaxTOPOMRAVkeYuvE7E8ENAc99KqKyJUbVp-IQVdQav6spBoy7WyhW-2yp3Cy4rJ_V9cLhjPMcz1SrnyKMWjTIuh1gEFrI_YEUHkfwcykAuLznEOBsSjqhg2ODnUzdQeCpCIklQUBVouF-Q5xbf4dMA4tdzVaMwvDHNlBUCHOLc2KBpGs--45MrNFHS0h-NBu6d25oeHT6wCt2DfbqMO9Lo_nggU2OYovJrVGbmNr10sWpuxXmuTAHxAixvsP87SxzpkkFlWtUSLhY_A4MZvCZKiFas2VYtM-SGx21eyrju34q8ZJesRB-yPaxUrDp1rllTdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06554c8831.mp4?token=EFJYxBz4Hx4SRQuvOQaxTOPOMRAVkeYuvE7E8ENAc99KqKyJUbVp-IQVdQav6spBoy7WyhW-2yp3Cy4rJ_V9cLhjPMcz1SrnyKMWjTIuh1gEFrI_YEUHkfwcykAuLznEOBsSjqhg2ODnUzdQeCpCIklQUBVouF-Q5xbf4dMA4tdzVaMwvDHNlBUCHOLc2KBpGs--45MrNFHS0h-NBu6d25oeHT6wCt2DfbqMO9Lo_nggU2OYovJrVGbmNr10sWpuxXmuTAHxAixvsP87SxzpkkFlWtUSLhY_A4MZvCZKiFas2VYtM-SGx21eyrju34q8ZJesRB-yPaxUrDp1rllTdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه بقایای موشک آمریکاییِ اصابت‌کرده به مراسم عروسی در هرمزگان را به دوربین‌ها نشان داد  @Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/463598" target="_blank">📅 11:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463597">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad24702360.mp4?token=gaFXZuzRpbaojAFA0T-BDQp1L09ER5OchrPQXwVLKA9QO9X5c_mDhAvmDn8AgSAxcZevVLMk7FJhFc-WtQ-9OmgjuYdyV669aPhDgVKW3mjyoSnTwIAG5_U5eGVZQu-zNasKlQDtjcXKMWlTGtFwCLYhaXidbHMpG-R-CVFZhKweG1mX5Z5mVpyj4IQNAf6GhFeRE0f2LW214pTV6bomwi0z8Wxn4TwZR3PjGxcohnoUWGSTS9hPnPNWGfaxeSXIVJEqmZiusLf17xo-JuncWxhddA_X7RDHKWBAL6a5_9hvuhT5vGR175tiOyrzndqb0ZG5mQkxzhcwX8S8tIbmeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad24702360.mp4?token=gaFXZuzRpbaojAFA0T-BDQp1L09ER5OchrPQXwVLKA9QO9X5c_mDhAvmDn8AgSAxcZevVLMk7FJhFc-WtQ-9OmgjuYdyV669aPhDgVKW3mjyoSnTwIAG5_U5eGVZQu-zNasKlQDtjcXKMWlTGtFwCLYhaXidbHMpG-R-CVFZhKweG1mX5Z5mVpyj4IQNAf6GhFeRE0f2LW214pTV6bomwi0z8Wxn4TwZR3PjGxcohnoUWGSTS9hPnPNWGfaxeSXIVJEqmZiusLf17xo-JuncWxhddA_X7RDHKWBAL6a5_9hvuhT5vGR175tiOyrzndqb0ZG5mQkxzhcwX8S8tIbmeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای پیگیری قضایی حملات دشمن به مردم و زیرساخت‌های هرمزگان ۶۱ پرونده تشکیل شده  @Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/463597" target="_blank">📅 11:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463596">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a3b282b80.mp4?token=crUNr6mk37z_dxZUb4L1XIhpEnzCboTrb2IIsUFXqeDN6MeO8Fae_tlUb9c3kUocMFyANtKog_sNBsHy0z-c8LwuYMbAMbpgBCtw_D1hQgs4uQxcjqzYzvBnuvDINtUiML05iQhwjTLlWQGqZPglVl_SIE_Z3bR3APeoKI8oPeRVeVRCFDM2_vYdEe2WP6MoQ6p_OGdoizMknEyzSuUqRpMFcI0F5lWiWUNuOeLyZlCsdzIQdYOM3SFfyV0vFOyGifgrwq8QPjH1g0FJiZ3o1KqehQH7WZC2a3jQR5UbPX-q2lGjHo_3vxJjLtQjr2Zh9AYYjyEZYwwr3IrWziGn3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a3b282b80.mp4?token=crUNr6mk37z_dxZUb4L1XIhpEnzCboTrb2IIsUFXqeDN6MeO8Fae_tlUb9c3kUocMFyANtKog_sNBsHy0z-c8LwuYMbAMbpgBCtw_D1hQgs4uQxcjqzYzvBnuvDINtUiML05iQhwjTLlWQGqZPglVl_SIE_Z3bR3APeoKI8oPeRVeVRCFDM2_vYdEe2WP6MoQ6p_OGdoizMknEyzSuUqRpMFcI0F5lWiWUNuOeLyZlCsdzIQdYOM3SFfyV0vFOyGifgrwq8QPjH1g0FJiZ3o1KqehQH7WZC2a3jQR5UbPX-q2lGjHo_3vxJjLtQjr2Zh9AYYjyEZYwwr3IrWziGn3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: پرونده‌های حقوقی و کیفری جنایت حمله به مدرسهٔ میناب تشکیل شده
🔹
پیگیری‌های بیشتر قضایی برای این جنایت ادامه خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/463596" target="_blank">📅 11:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463595">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ae445547.mp4?token=js-0Un-MxhqSmJR770Hecfi6BEeOf4X5_EofuciP0mI7kh1FjCLHbTrdrCMk9E89muSlZth-c1dU8tvV5jSaysEa_qpC-2nGqDUg9i-VxYXVdaoZTjXb3-kbgn3keMjGFUbdD8arKsMYHni2_9ThQtIMISEvQ8otHIRdil70dZis9QSm-A-xLtmJ4YzLIpF3sPrHpOfGW4nYz4kEYmPR9VJvb3YRU3JbY_XTm8FAUZaZywZAwi_xg4Orjk_NHE64x1vR0FAn7qrFb__3k2qRTRUnVK1_76tEnXSYk6gTX_zYXopHUQw0I9iikEnXWpO9n8PmS8SUjlB5Ei0DsHynYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ae445547.mp4?token=js-0Un-MxhqSmJR770Hecfi6BEeOf4X5_EofuciP0mI7kh1FjCLHbTrdrCMk9E89muSlZth-c1dU8tvV5jSaysEa_qpC-2nGqDUg9i-VxYXVdaoZTjXb3-kbgn3keMjGFUbdD8arKsMYHni2_9ThQtIMISEvQ8otHIRdil70dZis9QSm-A-xLtmJ4YzLIpF3sPrHpOfGW4nYz4kEYmPR9VJvb3YRU3JbY_XTm8FAUZaZywZAwi_xg4Orjk_NHE64x1vR0FAn7qrFb__3k2qRTRUnVK1_76tEnXSYk6gTX_zYXopHUQw0I9iikEnXWpO9n8PmS8SUjlB5Ei0DsHynYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: بمباران مدرسهٔ میناب، بمباران بنیان‌های اخلاق و انسانیت در جامعه جهانی بود.  @Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/463595" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463594">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70d7c99d8.mp4?token=MkATZh5m6JWqGFxh-hvz8gv7KJZ3ZNxTO6P2KZTUCr7oDYhoBk9o4H5uZfTgzK7MFdM4xC9u0JszDvIsS29azrDh-pjysLnUm0nmQJC6IjRd8MN5sdZZeovIRrz4M1m5VmLH7iwud5ay0Ry2zOcS33D1isM7qK5Iph3mE4i1CPjVYNVzdrB00BfVrBxR4y8yWO-t8mCQYOx8zog9ysFv7jtFR6HcW_kBvErAVX7fvb7U0NeXIskpAP3f1bT0gjOWIt3fapcLNUw4kCKmuoz1IMN3ri_6Ndnk5QvhCT27t6IXK9AVQXwRcpZygnEPpnPaZvoilYTPFiX8lYA1-wY2Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70d7c99d8.mp4?token=MkATZh5m6JWqGFxh-hvz8gv7KJZ3ZNxTO6P2KZTUCr7oDYhoBk9o4H5uZfTgzK7MFdM4xC9u0JszDvIsS29azrDh-pjysLnUm0nmQJC6IjRd8MN5sdZZeovIRrz4M1m5VmLH7iwud5ay0Ry2zOcS33D1isM7qK5Iph3mE4i1CPjVYNVzdrB00BfVrBxR4y8yWO-t8mCQYOx8zog9ysFv7jtFR6HcW_kBvErAVX7fvb7U0NeXIskpAP3f1bT0gjOWIt3fapcLNUw4kCKmuoz1IMN3ri_6Ndnk5QvhCT27t6IXK9AVQXwRcpZygnEPpnPaZvoilYTPFiX8lYA1-wY2Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: با قدرت، مواضع ایران را در مجامع بین‌المللی مطرح خواهیم کرد
🔹
مواردی که در سازمان ملل مطرح خواهیم کرد، بیان مظلومیت ملت ایران، جنایت‌هایی که رخ داده و بی‌اعتمادی‌هایی است که ایجاد شده است.
🔹
ما چندین بار پای میز مذاکره رفتیم و توافق‌هایی را امضا…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/463594" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463593">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10628ca9be.mp4?token=QslAzHdxK8VBnMRrL10D7U1XOl_YXgOvxepGXXyP_1AilX-4cKqgcD6-Uqw2eYbVlt8GKibbeiws1PBpruWdEptX-jUZpGGGxXyxtEm1IX2GpaWi5QI5o1b-JPd2wzSB05w5ckCqqs_VkYtgkbqD_rIbbVYRXRniqewChvdRhPAG5E0GQeMWw-NeeVDulQ2RktyX0WTkLgSAZ1GXbacEjKkJkUGUEaoje_HlAGXN6oYJLvLMnk6nvoevddD1TXnRtXqGlaal3nqzxA3C86U9955ShondkdsLq82q1CYslMJjzFKMAKnzvXnfDTBO51Mj97oGZEGZL1UyCWwoeKXpMI3If8gSJYtXWPbHrOjZYpdxOYmW36MNvh8sB0eN92nMjHM5XwyF59K5xSNgQs1M5mET6D5c3C29lyo05-_f_oWkGgGq-O3mXhztIvHV1Vnn5gDqzbMNSt7cJ8b2xd8-xJegAWm9uklxa6SZNNiR8JQZJGNgsvVmsysDJDU01EmALzUef9YhJp7pZL48PmIkyPR0d7z3l3kx51Q5HgvRPNPgycNdoqyVjZnKmlrwiokENYIAXMLFpZhs2MIjtct8uiAuEjC4CXlIuGKaGS0uSEOJvHZDwwAoQal5qJvAc3lOBT1R_I-BqKOW6r5SWjt5ybvjorivXm1nA8JQTaAScu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10628ca9be.mp4?token=QslAzHdxK8VBnMRrL10D7U1XOl_YXgOvxepGXXyP_1AilX-4cKqgcD6-Uqw2eYbVlt8GKibbeiws1PBpruWdEptX-jUZpGGGxXyxtEm1IX2GpaWi5QI5o1b-JPd2wzSB05w5ckCqqs_VkYtgkbqD_rIbbVYRXRniqewChvdRhPAG5E0GQeMWw-NeeVDulQ2RktyX0WTkLgSAZ1GXbacEjKkJkUGUEaoje_HlAGXN6oYJLvLMnk6nvoevddD1TXnRtXqGlaal3nqzxA3C86U9955ShondkdsLq82q1CYslMJjzFKMAKnzvXnfDTBO51Mj97oGZEGZL1UyCWwoeKXpMI3If8gSJYtXWPbHrOjZYpdxOYmW36MNvh8sB0eN92nMjHM5XwyF59K5xSNgQs1M5mET6D5c3C29lyo05-_f_oWkGgGq-O3mXhztIvHV1Vnn5gDqzbMNSt7cJ8b2xd8-xJegAWm9uklxa6SZNNiR8JQZJGNgsvVmsysDJDU01EmALzUef9YhJp7pZL48PmIkyPR0d7z3l3kx51Q5HgvRPNPgycNdoqyVjZnKmlrwiokENYIAXMLFpZhs2MIjtct8uiAuEjC4CXlIuGKaGS0uSEOJvHZDwwAoQal5qJvAc3lOBT1R_I-BqKOW6r5SWjt5ybvjorivXm1nA8JQTaAScu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسیابری هم نقره‌ای شد
🔹
علی‌اصغر آسیابری کاراته‌کای منفی ۸۴ کیلوی ایران بازی فینال را ۹ بر یک به حریف اردنی واگذار کرد و نایب‌قهرمان آسیا شد.  @Farsna</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/463593" target="_blank">📅 11:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463592">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7435d7776a.mp4?token=vb-LTy6l4C5evM8ICvZfofOOYiZrp9AiJZG3tzAjaRDseY_XJP2AeOFV_BlWV7rbj4-NOQi9qOsXYXUhE0jprj15bi_M2pEH1ego_pxF9YPUFjdUsczl8-aNPrQuGEBh8qItlzTouQZKEsmHFb5N8SDjCDhfv251rkNZnYe-dYb-fnfXB5TuwGeclY6mHIFLl6r8dYw-sMP0vxdlMeBpqNlePRzhm-oR87dJGgQ6lI0BrhNzEVoxXuS2FMC7KgRTRRU2y7mheyoW2njJUplBnc31ru3fK2dvSazwyGD2Ppu0fnLb7PGHWl7Hb5egLqaFUl_0jWexKC8QYxKorTlnUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7435d7776a.mp4?token=vb-LTy6l4C5evM8ICvZfofOOYiZrp9AiJZG3tzAjaRDseY_XJP2AeOFV_BlWV7rbj4-NOQi9qOsXYXUhE0jprj15bi_M2pEH1ego_pxF9YPUFjdUsczl8-aNPrQuGEBh8qItlzTouQZKEsmHFb5N8SDjCDhfv251rkNZnYe-dYb-fnfXB5TuwGeclY6mHIFLl6r8dYw-sMP0vxdlMeBpqNlePRzhm-oR87dJGgQ6lI0BrhNzEVoxXuS2FMC7KgRTRRU2y7mheyoW2njJUplBnc31ru3fK2dvSazwyGD2Ppu0fnLb7PGHWl7Hb5egLqaFUl_0jWexKC8QYxKorTlnUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا | نعمتی اولین طلای ایران را شکار کرد  کاراته‌کای وزن منفی ۷۵ ایران با شکست حریف ترکمنستانی به مدال طلایی آسیا رسید. @Sportfars</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/463592" target="_blank">📅 11:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463591">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287d502760.mp4?token=oURtQj064kjws9igw7eCfJuadoIXVTW2RVeya8Q8cTJls4_FPkN_7-z-sD5RmMBFCP7F_FZPZggl7G83vjAOiEjBpd0ruBMYTskfKdPuhRh-Td5g6KFwQlK3EIHpurEw6jJWAGDxID4YG3hc39kshRz44xDPZ1gI52zKPzykZWZIRnYMoDQPSG40VfbUUPyArJz2gDOVt-ztrW64d5lihol05CclS2QJLqnKIniA_SG7d9gXOPoGZz-IVNzbd2DosyJJ1CCx3Y0yOri2PBMUXRsm6CcBCPU186-A-9qZYhvvU80Dn44GDyb0vjAZuY8c7YHra_CVLwc8rNQ7lGFygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287d502760.mp4?token=oURtQj064kjws9igw7eCfJuadoIXVTW2RVeya8Q8cTJls4_FPkN_7-z-sD5RmMBFCP7F_FZPZggl7G83vjAOiEjBpd0ruBMYTskfKdPuhRh-Td5g6KFwQlK3EIHpurEw6jJWAGDxID4YG3hc39kshRz44xDPZ1gI52zKPzykZWZIRnYMoDQPSG40VfbUUPyArJz2gDOVt-ztrW64d5lihol05CclS2QJLqnKIniA_SG7d9gXOPoGZz-IVNzbd2DosyJJ1CCx3Y0yOri2PBMUXRsm6CcBCPU186-A-9qZYhvvU80Dn44GDyb0vjAZuY8c7YHra_CVLwc8rNQ7lGFygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه زنگ مقاومت را در مدرسهٔ شجرهٔ طیبهٔ میناب نواخت  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/463591" target="_blank">📅 11:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463590">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba51ceb74.mp4?token=DmydHQPoRgR3QSFXty3Vqs9xaK9_oXGFKG7km9hTX7ntUNk6rlev_SHRUdKAwc-AOSxp9cvrf6qoNZMhCnZxWX7ZiGiCXogZ53XGpiyD6xSsWW5yxrbhNAWJHwXHCE8FKYYZHIejIJDUs1SYc7DpEi0pD5k2u6PshZMfaIg19yvDCQQDMrVSrUnOcWL4ccDpxah2_UrGb8m70S2KIwJ5yctMlxWFmBEg0j9x1EUEIvySlWY3XzP7jnhUpTUdBRnStmSJKxs59K-0D2mzsTNnqg4mbTvyZwTnh6gh4TEUOLCfGP7LlVmyOl5gBBLIBSN0bqqOB-PPhdFZ8gKWbnMYsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba51ceb74.mp4?token=DmydHQPoRgR3QSFXty3Vqs9xaK9_oXGFKG7km9hTX7ntUNk6rlev_SHRUdKAwc-AOSxp9cvrf6qoNZMhCnZxWX7ZiGiCXogZ53XGpiyD6xSsWW5yxrbhNAWJHwXHCE8FKYYZHIejIJDUs1SYc7DpEi0pD5k2u6PshZMfaIg19yvDCQQDMrVSrUnOcWL4ccDpxah2_UrGb8m70S2KIwJ5yctMlxWFmBEg0j9x1EUEIvySlWY3XzP7jnhUpTUdBRnStmSJKxs59K-0D2mzsTNnqg4mbTvyZwTnh6gh4TEUOLCfGP7LlVmyOl5gBBLIBSN0bqqOB-PPhdFZ8gKWbnMYsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا | نعمتی اولین طلای ایران را شکار کرد
کاراته‌کای وزن منفی ۷۵ ایران با شکست حریف ترکمنستانی به مدال طلایی آسیا رسید.
@Sportfars</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/463590" target="_blank">📅 10:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463589">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575f3e76cf.mp4?token=YQdhTbK6M5Qd7GsFUE7C7nRQuGsd-LqtMPo2hODqeOONINyq4b6GB_Rc8pQKuYYi0z8IkHVgzDnl54IQ4AOM0JnTIwyedaC3vAO4QO7r0pWMEl39xjQMvApzsUIRvPXE9jZkJz8q4f5ELr6YJrJGAV4vDDXU8PVaeHezD1lF1y-KWDsTXaniDQIhrQw65I5r18CqvGeTWQNh3cjc0SLZKGgoyr4KCUUzoHjvgoI_9ynDDJh62gPpTmywNJPVEI4bbeZ3WNWn8JKZRhzEEzT6UbsYa2nESGGKoayH3kzsrnZrdXJ9GUZXIUC5VYpkP3MYUVvdiUOjho_v65hmhrgp1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575f3e76cf.mp4?token=YQdhTbK6M5Qd7GsFUE7C7nRQuGsd-LqtMPo2hODqeOONINyq4b6GB_Rc8pQKuYYi0z8IkHVgzDnl54IQ4AOM0JnTIwyedaC3vAO4QO7r0pWMEl39xjQMvApzsUIRvPXE9jZkJz8q4f5ELr6YJrJGAV4vDDXU8PVaeHezD1lF1y-KWDsTXaniDQIhrQw65I5r18CqvGeTWQNh3cjc0SLZKGgoyr4KCUUzoHjvgoI_9ynDDJh62gPpTmywNJPVEI4bbeZ3WNWn8JKZRhzEEzT6UbsYa2nESGGKoayH3kzsrnZrdXJ9GUZXIUC5VYpkP3MYUVvdiUOjho_v65hmhrgp1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین نقرۀ ناگویای ایران سهم بانوان کاتارو شد
🔹
تیم کاتای بانوان ایران در فینال بازی‌های آسیایی ناگویا با نتیجه ۱-۶ مقابل ویتنام شکست خوردند و به مدال نقره بسنده کردند.
@Farsna</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/463589" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463588">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
عربستان از فعال‌شدن هشدار حملات هوایی در منطقهٔ نجران خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/463588" target="_blank">📅 10:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463587">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رهبر انقلاب: آیت‌الله‌ شبیری‌زنجانی عالمی محقق و ژرف‌نگر بود
🔹
پیام رهبر معظم انقلاب در پی ارتحال حضرت آیت‌الله‌العظمی شبیری‌زنجانی: این عالم بزرگوار همهٔ عمر شریف خود به‌جز چند سال اوّل طفولیّت را در مسیر تعلّم و تعلیم و تحقیق گذراندند و همواره از سوی هم‌ترازانِ…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/463587" target="_blank">📅 10:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463586">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
عربستان از فعال‌شدن هشدار حملات هوایی در منطقهٔ نجران خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/463586" target="_blank">📅 10:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463585">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: هیئت کارشناسی به پروندهٔ مدرسه میناب ورود کرد
🔹
کاظمی: در آغاز سال تحصیلی به‌نیابت از مسئولان قوه‌قضائیه به هرمزگان آمده‌ایم تا یاد و خاطرهٔ دانش‌آموزان، معلمان و والدین شهید مدرسهٔ‌ میناب را گرامی نگه داریم.
🔹
شعبهٔ ۵۵ دادگاه حقوقی تهران…</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/463585" target="_blank">📅 10:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463584">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxl_AELFjwqQkQJQrWyKm-5eQ5Z-QGOQ_Tvu1-G-EJM9C3ztvGSo4hajBsknxlG-YDg5q6wn0Cs38j7THsXILwZXymRxCYSMKxzY8triLebmlJR8dNMYplKzl3ChVKHrlGf2acM2-7tvSA8znInA5nu3zycPlDTo_ea0MWi7mU-P5sj1lpZu2DPTtF0VtBCErGXO8hI7b3FNSSBhagTdRbDQZfKR9CRN5mGrZB8SrpNGXFwI0TJa3EYNSpbxeyoj71U080NFNFxtJT80Ub1WQCMBOPfuQB53D-R_oAN6FLFpEjLgPix-MNi-U4mBm84BVHW1hvVevfLsH-erHZey4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاییز معادلۀ بازار گوشت را تغییر می‌دهد
🔹
«۴ میلیون راس دام سبک فصل پاییز کشتار می‌شود» که عرضه را افزایش خواهد داد. رئیس شورای تامین دام امروز خبر داد.
🔹
این رقم ۱۶۰ هزار تن گوشت معادل مصرف سالانه ۲۷ میلیون نفر می‌شود.
🔹
به گفتۀ پوریان امسال ۱۳۰ هزار تن گوشت گاومیش هم در کشور تولید شده که مصرف ۲۵ میلیون نفر در سال می‌شود.
🔹
در یک‌سال گذشته قیمت گوشت تا ۲ میلیون تومان بالا آمد که تولیدکنندگان علت اصلی را کمبود و گرانی نهاده می‌گفتند که با فشار روی تولید و عرضه قیمت را افزایش می‌داد.
🔹
اکنون قیمت هر کیلو دام زنده گوسفندی به ۶۸۰ هزار تومان کاهش یافته که طبق عرف گوشت خالص باید ۲ برابر یعنی معادل ۱ میلیون و ۳۶۰ هزار تومان دست مردم برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/463584" target="_blank">📅 10:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463583">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPXvBVkjXbZU5vwl1LkklKuldbtXqoUN3hRWB1U95S3mV3L1gWPun4kb35kFZ8KQxU-ImTSAOtb2dXthtvv5i4xX1wdIt91-XuMMmRsPPDTvwWFbfi2x5rFBcV00ZvwyRXNtoV9-XGfYpOVCDjrFAWQUQNgW7JJXvenaAoUF7AEuRDWb3IM2M8YkrvtctiACmlJHYmfXow86h_fMzrFmGLRhPH0epgQxAYd-AtujJe74YwaN-Ty3UrGs7iPqGRQAMHWEZJmZ8NkoA2Hq8xgN1Li7hT7Cq8ncPWdWBmry9eqZz11jsg40x73WeD0c4x2XWdwYnsktBd9TYF-yQalGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نگاهی به زندگی پربار مرحوم آیت‌الله شبیری‌زنجانی  @Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/463583" target="_blank">📅 10:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463582">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سپاه استان هرمزگان: انهدام مهمات عمل‌نکردۀ تجاوز آمریکایی-صهیونی در شهرستان رودان امروز ساعت ۱۱ تا ۱۵ انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/463582" target="_blank">📅 09:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463581">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b516cd8c96.mp4?token=h-w_mqf_W40GwNQpH7QMr23DU31APDwnYQZ6RHAeIp8QvXCLDZmKK_hNOJEF0aGPgdjjv2QIv791iviUWRr_bAcNWnJDIvHJJOKyqh2-6H4runTTIAX4cMNkJoX8XcfFIAeGe5JGxEonnZEwV_UQV1QJVwzgyhPxD_3x0ie_cMEjqrrvgwv_2eVDwBCMg0tS_mj471QFN3zWyVmPqtnNPLOGYrP4Y_HdD0Rzuic-tBdCXWyqQgXPwbPaBqtAvH5JCkF68n4pcEc3fd2GJqIewUETj7DlDR679RJcsQKeWQ4aMMLUyEiO0SUPcf65kFL8V13t0o7MjG4gXP9ShP2h9paBiRXbJSGtHrWSFS9rLvwmNtjkCQEuSHxRPIgQqg9r45GLEX-O6wUaFB-4svuvLWMSwH29lXFGAyGgt62tx_geZw1yQBGXIv1K5wy4TX5L1lLTK2pRlNMSBQ9za8zegZZ20jM-D2n0JVuWeepAtYJggehrAVJjtiLB6QWFjpLcDrkRMve0rzRUrKkql7XCZpBdmFC2Thx4nyKHZeeLIA6Y8dXmuAfAlBaIuv0sxnK72Z0p26_m59nO4XLaBwbIVpskV3CRYw7zKlKpa77eoHfmxX1MhKqYYqQ0KsxxO5w_E5_SchSLEAE-h80AQGXC-6U_GnFmpapEX2KQ-nxSyAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b516cd8c96.mp4?token=h-w_mqf_W40GwNQpH7QMr23DU31APDwnYQZ6RHAeIp8QvXCLDZmKK_hNOJEF0aGPgdjjv2QIv791iviUWRr_bAcNWnJDIvHJJOKyqh2-6H4runTTIAX4cMNkJoX8XcfFIAeGe5JGxEonnZEwV_UQV1QJVwzgyhPxD_3x0ie_cMEjqrrvgwv_2eVDwBCMg0tS_mj471QFN3zWyVmPqtnNPLOGYrP4Y_HdD0Rzuic-tBdCXWyqQgXPwbPaBqtAvH5JCkF68n4pcEc3fd2GJqIewUETj7DlDR679RJcsQKeWQ4aMMLUyEiO0SUPcf65kFL8V13t0o7MjG4gXP9ShP2h9paBiRXbJSGtHrWSFS9rLvwmNtjkCQEuSHxRPIgQqg9r45GLEX-O6wUaFB-4svuvLWMSwH29lXFGAyGgt62tx_geZw1yQBGXIv1K5wy4TX5L1lLTK2pRlNMSBQ9za8zegZZ20jM-D2n0JVuWeepAtYJggehrAVJjtiLB6QWFjpLcDrkRMve0rzRUrKkql7XCZpBdmFC2Thx4nyKHZeeLIA6Y8dXmuAfAlBaIuv0sxnK72Z0p26_m59nO4XLaBwbIVpskV3CRYw7zKlKpa77eoHfmxX1MhKqYYqQ0KsxxO5w_E5_SchSLEAE-h80AQGXC-6U_GnFmpapEX2KQ-nxSyAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی مرگبار در دبیرستانی در ترکیه
🔹
یک فرد ناشناس امروز در مقابل یک دبیرستان در منطقه تورگوتلو از توابع استان مانیسا در ترکیه اقدام به تیراندازی کرد که در پی آن یک دانش‌آموز کشته و چند دانش‌آموز زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/463581" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463580">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akZ1806gwauW3WiiJ420cwZqk02hi10an0W328_hG5ERfVnKcq7RpAob5e5HqwLRwmYELbUo4Q5ZTtmBVPUrPdxOoYdCiQuFgsQH9hAoerhOrvqz4HKYgySq4ebjSBGAoX3le54WiXnTYLJf0M7zgGIiC37Gpk2pn1CZ_pj3YZW4nl3awzUybmJ_ALsnMWR4q5zRhSDGBsofZaD_3MwOFKlhmDrqUXDQi4l2MVlgisCvXv3TaDFlNVyP65PHiGU75qv8kYjae3Xcavytcrh53WJEs0xt7NdnQsQadcJq9AJiPt6C5cRzWqb3E4HCRJavjhwfIZJMbe13rBakB_OokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/463580" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463579">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcwJBv93sXF6O8PWEVFf-TOibC1icKkGa0pnHE2ZbaE0OiuUi6BIo0oxF_0LkKwYWR1H6NcUOPvwwaFg21s0PCUQT8cB6OFfm53qWz9cKD6jhQ2ECneDMho1Tx8a6UWUJqCJTQXqTqsvrvWVDP3NMIfMYOMBAkCFZhr0GWrfuUE1qVosbzUXFQ8O5M8_sSWMZOpdiu0la6iIkpnOYqQeg9u-RrubR2U4LyQZHzL_--oSAEle72zQov7Zl5LsI42pASd9DGGtCuEvVXd5luP0pANV5ORgH-GazjlZ6u-GDB5oFTVLZTKLOcMZWzvPN7gLV5CPydLp17oUOjrmA1YW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  هیئت نظارت مجمع تشخیص بخشی از مصوبۀ «مهریه» را مغایر سیاست‌های کلی دانست
🔹
اعضای هیئت عالی نظارت مجمع تشخیص مصلحت نظام، ماده ۱ و تبصره‌های ۳ ، ۴، ۵، ۶، ۷ و ۸ آن و نیز ماده ۶ را مغایر سیاست‌های کلی نظام قانونگذاری و سیاست‌های کلی خانواده دانستند. @Farsna…</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/463579" target="_blank">📅 09:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463577">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d094073aa5.mp4?token=rp7Kk-_u5haZagNjVn-7eHYzR3vPb-aHYGZACLU25aoSJt0ppk3EXhuA_nxQoOHGO9967y3p_CpgZda_R8W6etdg8EiDNK-csTHlp5GTx-VA5t5oWJK7En6ftQ7E08agqeFvsmXEt_jRv1g1pQYCGFY3oBVHHtp6jHhuvetRR1ZtDNkMaFcAoxJYHvjuy2SNfmBq2jozCtlArX9y66-FYw-Za3e0ks7kjHvQs8Ry2FVveu-QRVZMaD2JAVXRM7udjXCEGK4zKa-Hrpx4A9fG4y2ARqxBDARMbQaGDfAh5lnUxlTGOZW6c7DPSbFSMDsWhrjEPenVa1iahQ41wvgcszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d094073aa5.mp4?token=rp7Kk-_u5haZagNjVn-7eHYzR3vPb-aHYGZACLU25aoSJt0ppk3EXhuA_nxQoOHGO9967y3p_CpgZda_R8W6etdg8EiDNK-csTHlp5GTx-VA5t5oWJK7En6ftQ7E08agqeFvsmXEt_jRv1g1pQYCGFY3oBVHHtp6jHhuvetRR1ZtDNkMaFcAoxJYHvjuy2SNfmBq2jozCtlArX9y66-FYw-Za3e0ks7kjHvQs8Ry2FVveu-QRVZMaD2JAVXRM7udjXCEGK4zKa-Hrpx4A9fG4y2ARqxBDARMbQaGDfAh5lnUxlTGOZW6c7DPSbFSMDsWhrjEPenVa1iahQ41wvgcszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ جنگنده‌های سعودی به جنوب غربی یمن
🔹
شبکۀ المسیره گزارش داد که نیروی هوایی رژیم سعودی، حداقل ۳ مرتبه شهر «المخاء» را بمباران کرد که بر اثر آن ۱۴ غیرنظامی شامل زنان و کودکان، شهید و زخمی شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/463577" target="_blank">📅 09:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463576">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">متهم یک پروندۀ کثیرالشاکی در شیراز دستگیر شد
🔹
دادستان استان فارس: پس از وصول شکایت‌های متعدد از سوی شهروندان علیه فردی که مدیریت یک فروشگاه لوازم خانگی را برعهده داشت، متهم اصلی پرونده بازداشت.
🔹
متهم با تبلیغ و عرضۀ لوازم خانگی و ارائۀ آن به‌صورت اقساطی، از خریداران به‌منظور تضمین پرداخت اقساط، مقادیری طلا امانت دریافت می‌کرد و متعهد بوده پس از پایان پرداخت اقساط، طلا‌های دریافتی را به صاحبان بازگرداند.
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/463576" target="_blank">📅 09:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463575">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44af34dc25.mp4?token=sspiUNJFzgzjTMwKGucvdwU9hajSJpi7nda7MO1VUgZzEtLttZdpP3FXjZrSSsHKgb1R4vlXlItmqec9dTGdPA_O-e4hOTNPLh3RgB04KAYUQTgwPVdhJdlT9hhf9nNNaa9sbXQWqZnx76BsaXnGzGwQxxohgGXXZJOLkNIcHkmq3CvVsVhXTjdub3JdAvCu1BxsJG2C72qJMroldUWMLCfeewcpi39hYsv4Cd87ZM6BvM11gbGgeZBwRsJMUcaB51YyXWnKud8J5gIS6pqFKReY4i8uiQyxpHM1qYMZweRIJkWEPwO5_YSsDKEx4mUj-2l56UV_YWeKL-P2DaJTcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44af34dc25.mp4?token=sspiUNJFzgzjTMwKGucvdwU9hajSJpi7nda7MO1VUgZzEtLttZdpP3FXjZrSSsHKgb1R4vlXlItmqec9dTGdPA_O-e4hOTNPLh3RgB04KAYUQTgwPVdhJdlT9hhf9nNNaa9sbXQWqZnx76BsaXnGzGwQxxohgGXXZJOLkNIcHkmq3CvVsVhXTjdub3JdAvCu1BxsJG2C72qJMroldUWMLCfeewcpi39hYsv4Cd87ZM6BvM11gbGgeZBwRsJMUcaB51YyXWnKud8J5gIS6pqFKReY4i8uiQyxpHM1qYMZweRIJkWEPwO5_YSsDKEx4mUj-2l56UV_YWeKL-P2DaJTcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضی نعمتی با یک ۳ امتیازی شیرین راهیِ نیمه‌نهایی کاراتۀ ناگویا شد
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/463575" target="_blank">📅 09:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463574">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8876d0d65.mp4?token=cTLt6aPXw8SxDfHRYFOU6xspWVuJlM_hHe55o39MOZ82CkuWVwJh0yXSxzoIhro2D6S2fZ3qlv6eQyJxez8ETc-dWvRPbENPWW-I0bvkUyvzrs0q9oJLWs-RJjTGAfk2UD9qpx9m8awUc73DdoDDobn3sGqlKW6qOpLMsywKY8bySfjBaQWVMICcJmF0AmRaQIR5W5wZUpRv74kZ5kC2tp_lyNhYlOnkj39E45er1TVfO66pNq72oepioZapwGrE2D8XbRZse_d7tp_O03QpexO2yIjU8Jg2-SxAqR98GmIiUz4IamczBlmIA3MItsg8rm1OyN_TV6Rlj-KI5dxhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8876d0d65.mp4?token=cTLt6aPXw8SxDfHRYFOU6xspWVuJlM_hHe55o39MOZ82CkuWVwJh0yXSxzoIhro2D6S2fZ3qlv6eQyJxez8ETc-dWvRPbENPWW-I0bvkUyvzrs0q9oJLWs-RJjTGAfk2UD9qpx9m8awUc73DdoDDobn3sGqlKW6qOpLMsywKY8bySfjBaQWVMICcJmF0AmRaQIR5W5wZUpRv74kZ5kC2tp_lyNhYlOnkj39E45er1TVfO66pNq72oepioZapwGrE2D8XbRZse_d7tp_O03QpexO2yIjU8Jg2-SxAqR98GmIiUz4IamczBlmIA3MItsg8rm1OyN_TV6Rlj-KI5dxhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سپاه: ناو هواپیمابر آمریکا را در فاصله ۵۰۰ کیلومتری هدف قرار دادیم
🔹
سردار محبی: ما امروز مصادیق قدرت را یکی پس از دیگری به نمایش می‌گذاریم. نمونه بارز آن، جلوگیری از عبور و مرور هرگونه شناور بدون هماهنگی و نیز ممانعت از ورود جنگ‌افزارهای دشمن است.…</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/463574" target="_blank">📅 08:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463573">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee78c3dc3f.mp4?token=nmnJb6OsJ-qbm6m6eEk07xuag088gJfSlsM0EkV5Lstvxn07rMZPxg98Hn0Ppn4t0KyJ8h-sbKjg_JUwSUp5Ukt6fZW_5WTEhcSUcYa8vVzXmLNou9ZGowtKhasJspsbbli-NdtJa0qKqKpTBDpV1Q2ehKxBk6xyEnujEtlZdF938E2pAITVAN-Vx-v4AifJ2YoRocvjRjPIM51fxmautuwR23eVdS7ALa3Jlk4dP6O7vOJ9dGj8rY0iZ8xqJsw4oNlVWAadrykdJXgMjZiFsCWnclrRBnoqklKBxXcAJ_qSFA-QaFK2-GoCBYsyD2E-jO88UQqT04CZUfp_6kV_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee78c3dc3f.mp4?token=nmnJb6OsJ-qbm6m6eEk07xuag088gJfSlsM0EkV5Lstvxn07rMZPxg98Hn0Ppn4t0KyJ8h-sbKjg_JUwSUp5Ukt6fZW_5WTEhcSUcYa8vVzXmLNou9ZGowtKhasJspsbbli-NdtJa0qKqKpTBDpV1Q2ehKxBk6xyEnujEtlZdF938E2pAITVAN-Vx-v4AifJ2YoRocvjRjPIM51fxmautuwR23eVdS7ALa3Jlk4dP6O7vOJ9dGj8rY0iZ8xqJsw4oNlVWAadrykdJXgMjZiFsCWnclrRBnoqklKBxXcAJ_qSFA-QaFK2-GoCBYsyD2E-jO88UQqT04CZUfp_6kV_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی پلیس برای نجات کودک به دل چاه می‌زند
🔹
این روایت یکی از ماموران پلیس است که ۴۰ دقیقه در چاه کنار دختربچه ماند تا نیروهای آتش‌نشانی کودک را بیرون کشیدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/463573" target="_blank">📅 08:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463572">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4a14d887.mp4?token=Ba1Pg6kDKn0WfehRxmg0omTsMRnRLrOcXSeZ9KMIH0Kj0_8ji9koIQZdoAXEtGNQv977pVHWr5A0mpr8H2MRoafbn0orWXpZcicFfKtyS_gRXbC818QU2H9Uz576RNnpmFkHqtNuB2iu9oF1xnAexyY47ryKnT-HzzkH-woVAdH0-Tj-c9wwDfEhV3GIBVnAmRmFJ5phwTyOOgGMg8IZZlE2gwTTGCOj8VwBqojvkV1NjajgJ7PgJJfi4N15NfQxC3dekjF1IsputIvpqQHZ-cvr9yKn1lkeZ4CuZZ5zKk_eR7ddURT_GiAHmqRn2D4gxuc6brEUu5uyh1aYaA7cK3fIQFbnWOwD1DrKPoENdjIccj6CN_HB86y-WqNupGFs6FbaEwwoTHTAoSCqTsR_B3v6aB4DMCdKdqKCyVFe7JmuO8rlk53FL9_RhifTF3K9FWF93Odic_Mh2SNrICwOH_qCEGO32zfBOQXxAxBbsxW2no7Pa_9CKmZz30zTAgqk4iSdAAI1rP4Ycmb2cpWPiu9b8dwXY3lXoeg22SroJPMbJU0Y0I4YT6wCCB7oeL9njPbNuOwZGMed0GUBWE7X9PtGg8Q1BwVew81U446q9PoP92trnO0VgY6DsE00K2uq4dI3Bdpn_VEO9GcFczwwMrOyBZJTmZJ9Ip9JQEJrt_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4a14d887.mp4?token=Ba1Pg6kDKn0WfehRxmg0omTsMRnRLrOcXSeZ9KMIH0Kj0_8ji9koIQZdoAXEtGNQv977pVHWr5A0mpr8H2MRoafbn0orWXpZcicFfKtyS_gRXbC818QU2H9Uz576RNnpmFkHqtNuB2iu9oF1xnAexyY47ryKnT-HzzkH-woVAdH0-Tj-c9wwDfEhV3GIBVnAmRmFJ5phwTyOOgGMg8IZZlE2gwTTGCOj8VwBqojvkV1NjajgJ7PgJJfi4N15NfQxC3dekjF1IsputIvpqQHZ-cvr9yKn1lkeZ4CuZZ5zKk_eR7ddURT_GiAHmqRn2D4gxuc6brEUu5uyh1aYaA7cK3fIQFbnWOwD1DrKPoENdjIccj6CN_HB86y-WqNupGFs6FbaEwwoTHTAoSCqTsR_B3v6aB4DMCdKdqKCyVFe7JmuO8rlk53FL9_RhifTF3K9FWF93Odic_Mh2SNrICwOH_qCEGO32zfBOQXxAxBbsxW2no7Pa_9CKmZz30zTAgqk4iSdAAI1rP4Ycmb2cpWPiu9b8dwXY3lXoeg22SroJPMbJU0Y0I4YT6wCCB7oeL9njPbNuOwZGMed0GUBWE7X9PtGg8Q1BwVew81U446q9PoP92trnO0VgY6DsE00K2uq4dI3Bdpn_VEO9GcFczwwMrOyBZJTmZJ9Ip9JQEJrt_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقدام اطلاعاتی سپاه ایلام علیه شبکه تروریست‌های مسلح
🔹
سازمان اطلاعات سپاه استان ایلام در اقدامات اخیر خود، با شناسایی و برخورد با عناصر مسلح مرتبط با اقدامات تروریستی، بخشی از فعالیت‌های این افراد را تحت رصد و پیگیری قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/463572" target="_blank">📅 08:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463571">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28fd05db0.mp4?token=tf8pp-KwmouyWFLXXrRdvIasW2xXzuMmEgvo34uZnUzO_Qz53D5b1hEl7xI3QOkF2IvsP9K3U8vVzxm6VIZ8JIwwk7BCiH_rgJusXS_SwhkjqN9kV1eARvOhnz2WIA08qeIVZr6gqlcWIR0P5f5C6DeYV2yCrmtJwRjX4ZlV6CQPDiPCeKH1YWw413vr9w2CUuw7zOM8XHYBeb-MfF5ieh0mz96K450rywF5Rv56DApc5zVBY45rjFj2PAwJdBPRyZPOFifzX-aCoQW04UcDT10YdTiVF9r-fUzdjPR6Y7jGfHao21K04AmjJoB7BCutLsikmfAkO1ceDdCzDiBgvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28fd05db0.mp4?token=tf8pp-KwmouyWFLXXrRdvIasW2xXzuMmEgvo34uZnUzO_Qz53D5b1hEl7xI3QOkF2IvsP9K3U8vVzxm6VIZ8JIwwk7BCiH_rgJusXS_SwhkjqN9kV1eARvOhnz2WIA08qeIVZr6gqlcWIR0P5f5C6DeYV2yCrmtJwRjX4ZlV6CQPDiPCeKH1YWw413vr9w2CUuw7zOM8XHYBeb-MfF5ieh0mz96K450rywF5Rv56DApc5zVBY45rjFj2PAwJdBPRyZPOFifzX-aCoQW04UcDT10YdTiVF9r-fUzdjPR6Y7jGfHao21K04AmjJoB7BCutLsikmfAkO1ceDdCzDiBgvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشف ۶ تن انواع مواد مخدر در تهران
🔹
رئیس پلیس تهران: در ۶ ماه گذشته ۱۰۹ باند مواد مخدر انهدام و ۱۵۷ قاچاقچی عمده دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/463571" target="_blank">📅 08:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463570">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اموال متعلق به جمعی از عناصر ضدانقلاب توقیف شد
🔹
دادستان تهران: با شناسایی حساب‌های بانکی و خودرو‌های متعلق به ۳۹۴ تن از عوامل ضدانقلاب که در جنگ تحمیلی دوم و سوم و اغتشاشات سال گذشته با دشمن متخاصم همکاری کرده و در مقابل ملت ایران قرار گرفتند، بخشی از اموال عناصر معاند توقیف شد.
🔹
تعداد حساب‌هایی متعلق به این افراد ۲۱۹۱ فقره حساب بوده و همچنین تعداد خودرو‌های توقیف شده نیز ۳۷ دستگاه می‌باشد.
🔸
پیش از این با دستور دادستانی تهران ۱۴۳ مورد از اموال و املاک خائنان به وطن که اقدامات تبلیغی یا عملی علیه کشور و به نفع دولت‌های متخاصم داشته‌اند در تهران توقیف شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/463570" target="_blank">📅 08:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463569">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34c18721c.mp4?token=b-OS4-cJmnoNZXaE15m18aaHSJS37avhifUrKWWhJ-RpBf2TUk-sdQh0QnBN_4LbS9kWMpgIHfcRBgmY8WLoUW8TvwhAqb7vMjyW8cGI81QmBhgv7qcdEURACZRg-Fzs_LWcNhw7zJhbtDkdH_zKAZ_6bw3URqoFkZ3kmlzhJ5Tq0-0iz-JJquB7L3GMOxygYqDtSbSOO2e1ubs5ncR_lLkjP-vg3LQnTJbDGMCvU-OYhDBc6Eb9N8ajN4o7AB5G6ePJ-gc-8Y-ZOTi_nhNjt3Rad6twvoj_Rauu1Q_2ynKAmz7h7U2Tmed4Nq3yWXwYzS_4M8vjOrwu0hSkMBEHDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34c18721c.mp4?token=b-OS4-cJmnoNZXaE15m18aaHSJS37avhifUrKWWhJ-RpBf2TUk-sdQh0QnBN_4LbS9kWMpgIHfcRBgmY8WLoUW8TvwhAqb7vMjyW8cGI81QmBhgv7qcdEURACZRg-Fzs_LWcNhw7zJhbtDkdH_zKAZ_6bw3URqoFkZ3kmlzhJ5Tq0-0iz-JJquB7L3GMOxygYqDtSbSOO2e1ubs5ncR_lLkjP-vg3LQnTJbDGMCvU-OYhDBc6Eb9N8ajN4o7AB5G6ePJ-gc-8Y-ZOTi_nhNjt3Rad6twvoj_Rauu1Q_2ynKAmz7h7U2Tmed4Nq3yWXwYzS_4M8vjOrwu0hSkMBEHDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور به نیویورک سفر کرد
🔹
پزشکیان صبح امروز برای حضور در هشتادویکمین مجمع عمومی سازمان ملل متحد، تهران را به مقصد نیویورک ترک کرد.
🔹
براساس برنامۀ اعلام‌شده، سفر پزشکیان به نیویورک تا شنبه ادامه خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/463569" target="_blank">📅 08:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463568">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8da70a10b.mp4?token=EpuhccbyThjiwByupsjUXcZor4484kRWR3O6t_JOIEMv-edfqMzKwggxfsTMJeq6iWmV2qOt1w1s8HgLY9P2pVM1L5OBjre5lj9bhWEWuUZi8bBwtTbMry1PJJznFDZb9L4YfOybbluRLT02yvLjDCwtg4dAB_j9TW8pdJLaI_EjS3EvWeyC8UYew74ds8YbA5qfDde0dZ_BKVLGwvREfOX8jQNSEgvxPGdWeIcjTAyDnfBGwaWNeIMGhm0xf8-xZezR8pgZ3iltnva3hSjwXSwntWK4o5vGz69ZMZi8Xq5CR7Fv9NaVOeQM09ZjC7_Sf0Ds338OZZLGQo8nD3gT-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8da70a10b.mp4?token=EpuhccbyThjiwByupsjUXcZor4484kRWR3O6t_JOIEMv-edfqMzKwggxfsTMJeq6iWmV2qOt1w1s8HgLY9P2pVM1L5OBjre5lj9bhWEWuUZi8bBwtTbMry1PJJznFDZb9L4YfOybbluRLT02yvLjDCwtg4dAB_j9TW8pdJLaI_EjS3EvWeyC8UYew74ds8YbA5qfDde0dZ_BKVLGwvREfOX8jQNSEgvxPGdWeIcjTAyDnfBGwaWNeIMGhm0xf8-xZezR8pgZ3iltnva3hSjwXSwntWK4o5vGz69ZMZi8Xq5CR7Fv9NaVOeQM09ZjC7_Sf0Ds338OZZLGQo8nD3gT-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فست‌فود سرطان‌زاست؟
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/463568" target="_blank">📅 08:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463567">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzWnUZLBUCGSsSSNOal3gkYBBiVv_8F_TRfkkcDlAFsl2TxcbS3pW669KVyadbMwX0HpDrcak6iGean94SpXjl1I1o8XJpo-YGeAznrtcOWEnuSTCiAwVDtMB6PP66qTlfA4Q4cYlOZbtaVjpa-yvT_9k8eW40INhhuOVkvAYjg2nD73HP_SFrfdKm4Y-hTu_d-bTcOkcVtsxVnaeUTWmE2JXKj4OgaXF_vqCF-ZqpJlJ6RI2b7Qin6cyXkh2had9DvUnJgRuI7OIqProT56FFsq3G2Dq5AuP5dKFGCuLFLqPoKqz3UngLPxzi0fk53OhqjL8DeUPGLLp2vLX37sKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: در تریبون سازمان ملل مواضع بر حق ایران را بیان می‌کنیم
🔹
وزیر امور خارجه در بدو ورود به نیویورک در تشریح اهداف سفرش گفت: امسال پس از جنگی که صورت گرفت، طبیعی است که تریبون سازمان ملل، محلی خواهد بود برای اینکه مظلومیت مردم ایران، شهدای ایران، شهدای مدرسه میناب و در راس آنها قائد و رهبر شهیدمان بیان شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/463567" target="_blank">📅 08:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463566">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ7hREskYS92n6hH3D3AOYR1arcRwhIaN-iK5-nlzU9Bs1KVXvCVypaeFimVShPU30jS8oZnwmKKGgeqYlhGXZAXxWNXYqSMRDh1aYV9OeUrBdU-RetqjRF5Lpoagl95xmJMUzNXOWDaVPt5kXOdulkRm3A9gl9sm1p8L-5KV-a8vqPj2XQzYrNnjV_0dtXY9fWfYWpHAha4epad1CnQ91lS7hlOm8pjfPNgMyLylfrmR4X__ZTtNFce7TA8VTsg1gA6dfR9RqQCdQ4YBtZLeMwp4v7fy_lLsNjJ1tm4K0UPCI5YHXDfZ5utJ39meyKrxIjeMrH4XtEWNoXdhwbAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کیف دانش‌آموز شهید مدرسۀ میناب را به نیویورک ببرد
🔹
همزمان با سفر پزشکیان به نیویورک و اخبار منتشرشده دربارۀ این سفر، کارشناسان معتقدند ترامپ برای «فرار از باتلاق» و پایین آوردن قیمت نفت به‌دنبال دیدار با رئیس‌جمهور ایران است و پزشکیان باید در سازمان…</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/463566" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463558">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENz8mzcJcAppgFQZX2b0mUxoWEbdBoILhx11N7e2wwIG4Hj0lHWgn8KX_WzSA_SXH7yEIhyQXsukEiN8VquW-2RfNnGIilFWFk4ru_QApPSP5mPW2jNAH73jCfVw9zddfc0yVSpl8WVsXRsj-cFUOzlzbVyyhu6iKUtki-xo0e3LHTVeELdf7P9L7mffsaKebTdF53OgtpmoMSn31W8RzlyEOHDLRTtPmJQrxe8Y_8Cx9yInd53F9ift60sEiEv88te6GrJxEBMo00qUeUCWH39h9WawWFkofvNGeGVtbIytLmXXU-b2_ZSvsoQvW76_0cxRnwvmexWFabbaPiUz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/me9TRhrrQRGmzRdWj6NOsn8KV4xUtOrG3IKI1jpBefsDi0spAskUhT9d5c84XZRfoSPpD7TM36hptWyMcxlELa1vsRyZ-Lq-rY_di05zncx9-Jj3yly-z9NMvb92xbKB67_RW6oRrqNbtfaJ_knqdA1tb3gu_HEAobYkXZQm4eFf1y8wF_YwFpELN9wNRrYRBjQrrOoJbw6EhTGP4bfheUTF1XvLt5fDzGB1v9kRl5cOBgCq-BTnryE0tlSXnYg7fcJaG_DKJuE3-0v_Se7lp7FOTouA68lnUuE0ZxR12HIlSP60_5lm8Qe9SIiag3dYD6FAlN-PbyCzC5bTl4gnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDJLV31AinUolo0WWbeWVpu2QFG8bBXgH9rcKf1bI2A8mhYm7GjVlAfCdmnq4t5DVP6zPcjJu6k401O-C3To5sW76bjllbQphoAdpWIKj0_0KpIi61F3KbSL-YeoQZvJO2BFhJSBKGXXm51-5qjevKxeO-EqbFUiJ-YnEUMr2jFpM6_cyA21l10At6rWCErTm5IwcCotUS_YsIJ1AFFccb5hvsVBY_LOApA2m1gozjWTD436nRb-UcR6kZaFIozu8ivKQhBoKPKEo9NUVzLRCoaqRA268Wp-5npI8CPIFH9iqkIFfihqoWGcsvcYMhWAgrA8bPaKTbkrqidJ46-FFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRut-NNPuHj26SVPtUPigmqLbEO0C84RiqTRXgbGyfZCpC56KQmr9FQJ_fNhw5J74_bPUyzd78Y44p5LevXWOcO2m_v_LlbzNxd_jGgwbKCbwtqfQFtzHzIySr_M3hbV6EwxmY5Y36SIMM43Q2rzJ5aw9m_aPlNeVXRC3nnmLxoJBAr6gHZMF2BtewL1-m1vnU8wINePCOpN9ylh3Y1Dy8BSF-bvL_HtQtlF8Gl5LkkFvma8lb0GHgLQ-DgZMTrrPxLSR17iJL5q2QGISTZFjufTWCqUxuI5zEK5-LqkwlTQVRErJWHxZ91zlp4URrowD3g41fgh5847du-RVbMysA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1qVAJ2EDvEsoDPr9ZpV_FSLDY9_BwR5lvPwBK0edRp74kG2Z4PIxXSavWEydVnqs5SsNoVwI2LCo7ghM-EK_4NSmIZL0-WYa83jV6xWYqdwSmiigksfiVRm4toSgb-gmcnUmT3rKXrej0I4a8ag_RxexkaxAL_Z9rrjGiGatruPwvNpVHG9y29m14dOA3r2UWmn5wcF969Rzxf9YtU8oAhNgI99W_Yn-4oy54Jntdr1tQZhWaUikMgRrhIGJA4ndoxc2Hz7gmosUE_041j4jvoOqcmpjTccOQL9kaQhhvuVPe7FGqp66yM44mwdtdyz66vJsJUkuJWxpkv6JvBbSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwA5rCVBTQgiVYzIiICzkdT8-Nyo-E4WJzztH9PPFQDnpygekd-PxE9e7Mqt6YjXs4WToe27I910dm-ytdsGwZ0f49MoUV0kS7K0ZHWx3ApNMEmtlR1DdZX4_3tg6AgNA8UV8p2Mlwxo4MWx97k_MLlUDKKaeJJ3HlEf2pKfWcARoGVLBIL1SDJhmnmVBdYr_uZaT1dBoqfdk7gc-gbNyxl2e12wrOMUyKNzQEj85Xu1p1ejSrKvVwb1twYEGqkXTh2LQasdws-ylamc6XAJoUaaoK4FPy93TaULE_qgOTQnqlcV9n9_ngJ1qtyT4F3SFYqPNY4k4LbcWgehKUYIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cCssYtyUWelGn1ABBa7nQZM8p_KbHXFtRJJpCH-M8jQH1bQoO6VmHTTOmwkmOPJhDDv1oQNW4QVgWHJWt-DbSTDx4MIFwtuklf2XMq_LzBfBpKCaJYP5Cvbe72o09nhmpiXroYLTdwIpAI605PCv0OP80e36CDINOkH-J0XGLPvNH_-x55jFA9RBMMAx0LTvQ0k-JsJyEX1RcOJmh6v4s2SkVJ3B1NxTA4bGVeDMcr2N5raHDaJTyV_hJ1JOaeCHfnfhRSk5HSKZ2aMG6V4Spz65zACiPYJMErvGtAVVVWwnVhRsm5tEe5pbpg54ChwW3DYCa1x0RWYJlX7ZOlkvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qbn1TtCBZ5UwTBqx3V0nx-9DDAcnrYGdRggz9-M2LNv-yF1amQZMV_muhFDoe-rom8u6jAgvK8JA1voSzJuseJhnYW6RNgIdNFf3VMQy33ZQQpgLgmdvlCchAi4LWdRA0Voj2HZfK-H-Tb34x3DVIgCGxXBGczi4uzeMEJlF1sI4NrC7po-YPYDsDuq7kc9dg4OkjRACq9sTgL6ocvl5vPGQhVbjV4h0xbFtTPIHV9FrxUaGB1U6ME3678gdUfrOLOthpqz-las4PkGyIzUA5OFtbQrtclM-JR4tTO3Y2IWmM-N_ligZoMV8FMeuUotv2Ao7OWQn4x8v6RK8bVaSeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای اربعینی موکب‌های قم در شب رحلت حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/463558" target="_blank">📅 07:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463557">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4cb3243de.mp4?token=oYkH-qOo6ACX7wN-J2LH4fC_eekF66TnyiqO90CSXWyM8QYn9nAMzgfmKvi72Sexk7vdE5T9J8kQw6_CtCxh37uf6KAazPm1WuaUOhdjRtaQC-eX0FfJ8WqdbqnAiLC0a_y7or-MnNKuOW4wbGwmHnFxV8OlPoVfYmPKfrvU9eEZ7XGmXKExqncTNLBLaflqF2vCV2VVgguLs1oT9UYpFkelASteGDHdllaXVukQsVKqOHL9zCYl6Ih7DPMQ9fHAHXmIFXx122Z2OBXOEwGqBRrEg6n0Y9In5G-6faUe86idQ00k8l9CUpjOlw_Ia8KAmoKS_-2McB6FI7NtuYPGmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4cb3243de.mp4?token=oYkH-qOo6ACX7wN-J2LH4fC_eekF66TnyiqO90CSXWyM8QYn9nAMzgfmKvi72Sexk7vdE5T9J8kQw6_CtCxh37uf6KAazPm1WuaUOhdjRtaQC-eX0FfJ8WqdbqnAiLC0a_y7or-MnNKuOW4wbGwmHnFxV8OlPoVfYmPKfrvU9eEZ7XGmXKExqncTNLBLaflqF2vCV2VVgguLs1oT9UYpFkelASteGDHdllaXVukQsVKqOHL9zCYl6Ih7DPMQ9fHAHXmIFXx122Z2OBXOEwGqBRrEg6n0Y9In5G-6faUe86idQ00k8l9CUpjOlw_Ia8KAmoKS_-2McB6FI7NtuYPGmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلیل تایید نشدن لباس ملی‌پوش تیراندازی ایران چه بود؟
🔸
تیم میکس تفنگ کشورمان با ترکیب امیرمحمد نکونام و شرمینه چهل‌امیرانی هفتم شد اما بعد از پایان مسابقه به‌دلیل تایید نشدن لباس چهل‌امیرانی، این جایگاه از ایران گرفته شد.
🔹
محمدزائر رضایی سرمربی تیم تفنگ در این‌باره گفت: متأسفانه پس از مسابقه و در تست کنترل تجهیزات، لباس چهل امیرانی از دو قسمت مورد تأیید قرار نگرفت.
🔹
با توجه به اینکه امروز هوا کمی خنک‌تر بود، لباس ورزشکار ما نسبت به روزهای قبل مقداری سفت‌تر شده بود و به همین دلیل این اتفاق افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/463557" target="_blank">📅 07:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463556">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7am7CqfDKLlXKaVqpyZaCAD8uHUhMExF87fA1a6sNWaZK5cS6YPcOTTNG8NMRTwV3g-1OXTZ_gu_I1lBeRHsa8AgTxeFXn6ihApy7w-lWPAXaD2VnPIzCtv5HSvpsY01foeZJ-n7SD8pHojPnaUZbb2LU-P-4HeujQtdF-BAVnjZ_qW-dGrKHbEVU0sHE7a0089vt2hHDkd704_8cUyj6RwvQgTFWvhgBV75DOp9aur952Skp7ilgDDqaXDWW6VYWV0IzpsrCG_CtPAegPxbpa0DXiT7j_y53ty73VkFkeh7gNyce-Bo5nTslxIbjY1Hu0RbSKKwlFCwn8JPSl24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگرانی آمریکا از مهندسی معکوس زهپاد خود توسط ایران
🔹
بعد از اقدام جمهوری اسلامی ایران در تصاحب یک فروند زیردریایی کنترل از راه دور آمریکایی، واشنگتن نگران مهندسی معکوس این فناوری پیشرفته خود شد.
🔹
خبرگزاری رویترز در این‌باره گزارش داد که ایران احتمالاً زیردریایی…</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/463556" target="_blank">📅 07:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463555">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/019ee36bfd.mp4?token=h6qDCP2M88apbHKUWy46gC-jRu2LCGWAFdAER4ebNiD8Kjvo087dQ98PT97kq0g6SlDL_MziaqO6xMWHDwvBh0TXainGTBFg7Hm8ZiMNN_ex54X6onNiEzdgLT4vf0Cx-QxhZOBY1IuJJNqE1Jn33HXOLpsJIWGvqaZhv-zCSpVQEWMevsKV0Fu1afYrMNAXXwF9x7Ih_mjWh59mCcpAwbvEaY-r5RIX2KvNzQzo2VJLXW2ben7nRtrO1qybgkQF8wBrGY45fLwgu-nWBd342C2w8RO3zgY0ijVNDPhwMyC1Qlg3CXpcPuL5OTEQ67ftAbANbSX3vi_vqlkLQz6D7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/019ee36bfd.mp4?token=h6qDCP2M88apbHKUWy46gC-jRu2LCGWAFdAER4ebNiD8Kjvo087dQ98PT97kq0g6SlDL_MziaqO6xMWHDwvBh0TXainGTBFg7Hm8ZiMNN_ex54X6onNiEzdgLT4vf0Cx-QxhZOBY1IuJJNqE1Jn33HXOLpsJIWGvqaZhv-zCSpVQEWMevsKV0Fu1afYrMNAXXwF9x7Ih_mjWh59mCcpAwbvEaY-r5RIX2KvNzQzo2VJLXW2ben7nRtrO1qybgkQF8wBrGY45fLwgu-nWBd342C2w8RO3zgY0ijVNDPhwMyC1Qlg3CXpcPuL5OTEQ67ftAbANbSX3vi_vqlkLQz6D7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خواندن سورۀ فاتحه بعد از له کردن قهرمان آمریکا
🔹
فایتر فلسطینی‌تبار بعد از ناک‌اوت رقیب آمریکایی‌اش سورۀ فاتحه خواند.
🔹
او حریف آمریکایی خود را در ۱۲ ثانیه ناک‌اوت کرد تا سومین ناک‌اوت سریع تاریخ MMA را به نامش ثبت کند.
🔸
دو روز پیش بود که شون شرف به مصاف حریف آمریکایی رفت و این مسابقه خیلی‌زود به پایان رسید تا به بمب خبری در دنیا تبدیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/463555" target="_blank">📅 06:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463554">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA_DbQt9ZS9BR59qMHAkt1fmVp4Rfa4D6arVlisWqaMPOFTNgxfEVK02G7puBm09-y0rlXlBmGGm_S-QfoPk61SVmlR-HkfdY34Ymf9DdDI4p2mlKQbTYFP-QIgl2BqiPELuzY1uWXKJMxfBO5OiEOpQHS3SsCo5j8YAb-mbaA_CAD1blD-faMwMzs56WHGu5DAD8QQXeHmBwsl9VXEJRBISrSK4x6aad51b0vQZeuSNNE-KHhtEtHQcLaf7jgFk7WkUDmXtNrvHT55_VtYM649F_3v5hCnVwYeEzVsjisHpObXg1GGB_EDcDMVh6k-hueiPeSf3YkGReHiR5EHRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماکرون، رئیس‌جمهور فرانسه: برای کاهش تنش در بازار انرژی، با آمریکا در بازگشایی تنگۀ هرمز همکاری می‌کنیم
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463554" target="_blank">📅 06:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463553">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109244e8f6.mp4?token=p9vpS_nz9XPxzNCZjOTzs25Ro7K_dn8lGSNavaTTZRotz8rzViuXYFpjDULhkjKJyrQ5vTSDyQ_hw_O-udJHVFXk1RH9ebCQtjevsO3fyOQcci-Yadxt1THGa1DE12ka9tOpk8Y6oQhqT7vudrUDRG5cmV827nYgVKObvmKDBqy7qttImGHg12y5lHAIaAbDVPN-ws4VZuYgNH9r0X1iF-BaEKSJwyJpjrND5nCh3neIbDraD2dxNhofBYjTXuEtypSL3zUzWpPLQPdFfbea0xgKqTlIq3Il9SvT4u_kwenBIXeiXSFjLvggiQdQGmqbKYM2zWRzijStQt4G0-JYpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109244e8f6.mp4?token=p9vpS_nz9XPxzNCZjOTzs25Ro7K_dn8lGSNavaTTZRotz8rzViuXYFpjDULhkjKJyrQ5vTSDyQ_hw_O-udJHVFXk1RH9ebCQtjevsO3fyOQcci-Yadxt1THGa1DE12ka9tOpk8Y6oQhqT7vudrUDRG5cmV827nYgVKObvmKDBqy7qttImGHg12y5lHAIaAbDVPN-ws4VZuYgNH9r0X1iF-BaEKSJwyJpjrND5nCh3neIbDraD2dxNhofBYjTXuEtypSL3zUzWpPLQPdFfbea0xgKqTlIq3Il9SvT4u_kwenBIXeiXSFjLvggiQdQGmqbKYM2zWRzijStQt4G0-JYpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا | آسیابری با خوش‌شانسی فینالیست شد
🔹
علی‌اصغر آسیابری، کاپیتان تیم ملی کاراتۀ ایران، در نیمه‌نهایی وزن ۸۴- کیلوگرم، در حالی با نتیجۀ ۳ بر صفر از حریف خود عقب بود که در لحظات پایانی، کاراته‌کار فلسطینی پنج اخطاره و هانسوکو(اخراج) شد تا نمایندۀ کشورمان جواز حضور در دیدار نهایی را کسب کند.
@Sportfars</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463553" target="_blank">📅 06:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463552">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-gVaxgkG8x1vhGGCZXlz_JN4t1iakcB2VW2p0F-ruCLflSiQKAhVtNy8wHsRqZ3ecNmoyWBJabWMvK8M4bmBBgCW0LoHZGfgUO6Jc1mTeI5coYi1HA1eC7jwunQJlIe3Goz3JKgpyGmMGQIUoX8AxSYSnYnjbShIW2_VaLEaC_YlCM7WNcebOvx5OTb-wfhDv9kF5cd_8Kpgd3By4smrwmTeUN33ZiXm7k-SfBs7E5-E-rmpgxLXJTBIYp_occvQbthXzc4l_I6vrldXmNF6kXc7U7p-3M1-tG06usv20pCO7hv1Q2QvUD9q9Xjo9QVwDZ-qs7bxRaeK2LMwOf5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در جمع معدود کشورهای صاحب سلول‌درمانی
🔹
ایران با وجود محدودیت‌ها توانسته در حوزه سلول‌درمانی به دستاورد برسد؛ حوزه‌ای که دانش و امکان توسعه آن در اختیار تعداد محدودی از کشورهاست. این روش، یکی از مسیرهای پیشرفته پزشکی برای درمان برخی بیماری‌ها و ترمیم بافت‌های آسیب‌دیده به شمار می‌رود.
🔹
سلول‌های بنیادی می‌توانند به انواع سلول‌های بدن تبدیل شوند و در درمان بیماری‌هایی مانند سرطان خون، بیماری‌های ژنتیکی و آسیب‌های بافتی کاربرد داشته باشند. مسیری که از نخستین پیوند موفق مغز استخوان در سال ۱۹۶۹ آغاز شد و طی چند دهه به شکل‌گیری دانش سلول‌درمانی رسید.
🔹
ایران نیز با تولید ۱۸ محصول در حوزه پزشکی بازساختی، توانسته جایگاه پنجم جهانی را به دست آورد؛ پیشرفتی که نشان می‌دهد سلول‌درمانی در کشور از مرحله پژوهش فراتر رفته و به حوزه تولید و کاربرد پزشکی رسیده است.
@FarsnaTech
- Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/463552" target="_blank">📅 06:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463551">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک‌قدم تا طلای کاتای تیمی بانوان
🔹
تیم کاتای تیمی بانوان ایران با برتری مقتدرانه مقابل فیلیپین در مرحلۀ نیمه‌نهایی رقابت‌های بازی‌های آسیایی ۲۰۲۶ آیچی-ناگویا، راهی دیدار نهایی شد تا یک گام دیگر به کسب مدال طلا نزدیک شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463551" target="_blank">📅 05:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463550">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463550" target="_blank">📅 04:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463549">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انگلیس به جنگ سعودی علیه یمن پیوست
🔹
با دستور نخست‌وزیر انگلیس برای کمک هوایی به رژیم سعودی، این کشور به‌صورت رسمی وارد جنگ یمن شد.
🔹
وبگاه «پالتیکو» نوشت این ماموریت شامل یک هواپیمای سوخت‌رسان نیروی هوایی انگلیس مستقر در قبرس خواهد بود که در روزهای آینده آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/463549" target="_blank">📅 04:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463548">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c34ee8583.mp4?token=mBR0VgoeRoFRxINqLvRlnJBjgesjIeViPwbKfe-rwkOj7fg_WsmpSFU3WiUJsYtrhhc9zjLBX7pXBsoqnbxYzmE29Nw-5m2zLviQ5b2dBQbyX4kNm7pvNxqbybO6BAQInGkV4mFIi1K7SB1M4eLRXwO00s9Uq7iJ7PdOUPylY1gMpuVGk7inucHF6rGhnvdQRm6FCDoh2c6UCCKaHMltvBTuSNjsIa-_8ZKYnECquhv2ARmWqUFa9r2elcmkS73iooCEvIpWlaSmt-FI7MhVgQ_W0nCgtISFAFjDhjGFpY-Asu7RHzsC6FhcigSMfMNPVNTND9MKQ4vt8n8czoDxrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c34ee8583.mp4?token=mBR0VgoeRoFRxINqLvRlnJBjgesjIeViPwbKfe-rwkOj7fg_WsmpSFU3WiUJsYtrhhc9zjLBX7pXBsoqnbxYzmE29Nw-5m2zLviQ5b2dBQbyX4kNm7pvNxqbybO6BAQInGkV4mFIi1K7SB1M4eLRXwO00s9Uq7iJ7PdOUPylY1gMpuVGk7inucHF6rGhnvdQRm6FCDoh2c6UCCKaHMltvBTuSNjsIa-_8ZKYnECquhv2ARmWqUFa9r2elcmkS73iooCEvIpWlaSmt-FI7MhVgQ_W0nCgtISFAFjDhjGFpY-Asu7RHzsC6FhcigSMfMNPVNTND9MKQ4vt8n8czoDxrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌طور دعا کن تا دعایت بالا برود
🎙
آیت‌الله فاطمی‌نیا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463548" target="_blank">📅 03:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463547">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEiu3B_Wm9UBakiDNG5qwSH_zbA7ibCTQipa1F4w_gkEZWVTmy7KX9pUqo9-tJ97OAg1k3cuS9ZeMqAqErTfbGl4njmG3INKiXcrMEImJVSanAFI8L3id1av9UxESz-WRrnxfugfIkuNrjuhy4apufdsVa3hKZFIeK0DXkDVy2Yw4cgIwYs3ibsN-jMDPMzE4xFQdSy6UiGIrnkg9Vb5MNZecUBeAiO9kfGfViaKYXKik7WMmz81sCuTqeKiwNaNRHop_HcDC49J7LiNPwc9hit2gJJXvCvJ_wCqNj0rz71ZxYt-78PAN-6f8WRspaAPwvrx1y3obe7NUONUQToVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ جنگنده‌های سعودی به جنوب غربی یمن
🔹
شبکۀ المسیره گزارش داد که نیروی هوایی رژیم سعودی، حداقل ۳ مرتبه شهر «المخاء» را بمباران کرد که بر اثر آن ۱۴ غیرنظامی شامل زنان و کودکان، شهید و زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/463547" target="_blank">📅 03:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463546">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8rJ_VHrfm-pbP5TaDIPstwuocLJ52f35GpIEFlW1NYhgaWcE0tdIRURSL8BcFUmTNluo2w4szx8EM200kxdYCmSQT52059Mo6BcEID0JIWemNUFHrBqtXpJ0fMoQ87m7r8NOwTU8OR46OrFs0kI9sskiZHDrql9QhYwgn0Y_biLDMet7SaFeP5_LXs5pbZjNtyU7ynZv-RtCJKOk-vlC6srCcV9t42Q3bkbLvufCe37W7JeY9qv3xQSdvLb7DDT4s47ng5diqWAFEjS1I_dihS3YJWwwwqD3LhacC_MJStsyBLJInYSP_AxPRg7oN_0k_Ky_dyB0qGDdePs8pKB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدۀ ۵ میلیارد دلاری ترامپ به اعراب برای بازسازی تأسیسات انرژی
🔹
وال استریت ژورنال نوشت: آمریکا به تعدادی از کشورهای غرب آسیا که تأسیسات انرژی آن‌ها در حملات ایران آسیب دیده، وعدۀ کمک ۵ میلیارد دلاری داده است.
🔹
در این گزارش آمده، طرح ۱۰ میلیارد دلاری موسوم به «مشارکت برای اعتماد و ساخت‌وساز متحدین» به بازسازی خطوط لوله، پالایشگاه‌ها و سایر زیرساخت‌های انرژی آسیب‌دیده در طول جنگ علیه ایران کمک خواهد کرد و در عین‌حال جایگزین‌هایی را برای کاهش وابستگی به تنگۀ هرمز توسعه خواهد داد.
🔹
منابع مطلع به وال‌استریت ژورنال گفتند این صندوق توسط شرکت توسعۀ مالی آمریکا مدیریت خواهد شد و ۵ میلیارد دلار دیگر نیز از عربستان سعودی، امارات عربی، قطر، بحرین، کویت، عمان، عراق و اردن درخواست شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/463546" target="_blank">📅 02:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463545">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ایتالیا هواپیماهایش را از عربستان سعودی خارج کرد
🔹
مقام‌های ایتالیایی می‌گویند که به دلیل نگرانی‌های امنیتی، هواپیماهای نظامی این کشور که در پایگاه هوایی «ملک خالد» مستقر بودند را به مکان دیگری منتقل کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/463545" target="_blank">📅 01:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463538">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgX-txXvjsWnsIHpWwAjnejQa9D62XuB-o0H3UYqPzmJdQ9yE0RxEaYEvy70LSrLFwX7qRK7w_wjQIdOvgfkiUsMuYRk4sR6KRzIOUrlOn6hugT8pohkDGdFkECJjib-eKkzSkFR2LqGmc6vswju1xOSdIOL716LNvvmpDxtALIM4JArhz0LQz3r1Yg6UrjyE645sWS08CHrL1n6zz4LxseQXS51-jO4WfcNs1tX9wdMJAwlmmBH_FJRw8YVFXNFOLym9mU0yp0eAYS1aNrYSQthXv1-PVzuzOsU5AeYDyVRICdQRJTOBIgA4nR6vEEUII4_PtwwMjQWfPczzs_jmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFWvADGTE_61-hP2jW0ZIed4oOkhiGBOcyhDUf5RWRPDDV0CotPsQoO6bCiqeAyddUvRB32j6MVhZMePiPSgQyIni7OgVF945LB9K3lg4ZpHdGd0YBNw9rPTh1tb3jiFdtWs__IRQyMpcQaSVc-iRw4fT-RUy6oPv-EqK0jPdFe9uASBBZAyuAGPbIOeu6wbebRjl1eV7a1Z9EOFPkmmkvlWob1agnxxfaiUBFlykGC_I1AjmlMIRRrdZpxx4w5fhquLH2RikghxuPrWoit-CZxsdorac9wGP-Hzvmlx9uaRmgNiCleQ_bWuP-rv1H8EHV9eo-6jlcEgJuDEJqaQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUupEGlwAVUcozeNBYybHHvdX8rPZfG-5VDXYfc_TM6ag-J-PgF2D8bGDrMrhVJeMP9dCYhfTFxM0nOFUF4b9T-MULw3ovex-IsuExY5kHO5w1Vkhk5iKGV_wXlVfViQd9CL-w-JWUjywxG9fDhVqR6EnJgZEtOUfGFW_GTpnsJFb3oaZv7_Wg0ERtmLn3gnenWn2_zBuVs8AQ9d6epQAxx1P1jiaMvloc1RkEdMlC9PxbyCNtUE6Y7nsQuIteD69VGUsWBM9__1vyYQEtuXzUH0vDwE1LRHCb6RRN4nOniVnnh_4cxWX7wMfJpkOcsmBsYOBlZBaJVyEt4rLPYC0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4ThzCWE4DdeEbaadVnUT74FhDtXqVMVNMKqdOepbJfRZ6FFHyjJnWhDY72PUkSb95FN_kJNfhzaSlM56UoGxnZKDpsb97vFa_H46geskYQg225PhRwA6CDoAC001Y7tY6q8RgUgB-j6DgFPeyYGAmQkVxv1aKT70QCl6mof2X-rSBl5zTtEbxnl7XuWc76MXWwxBVm1AwYbfhHC-zRwTxutsNeYunyLYaaao0hpR8K6rv0dk2nszyWISd7mJ1RNikHJMAPH40FGaCe3TBsW4K9SdQ83bOeZ1rzEvjYiQuMrXfcTqfxx-3en6hNZ9w7i4y26bSjW3TNehQEsNeB9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IM0L4RSuAnZ1d8GO5PmFGPsyCqyXm-7DZ4oh046Bzkstn4FA7YkbxluSTPT-LSSYiSX2E5fU0rt52yJVn_WV-D5hknf-sOwHmGWeCIFRl0pB6qFZX3pjMm3TW-tDAJYLFmasp9c3HT7PsFtaaP5fIVnUBHBDitiQmhWSXa_bnXAzMkLzi9Gl4l8i2wxeDf5wdqXqMEmA3QclIqjdyZtc1Nonk6EvDMTPe8jfkfXlpfzxTFBMmm6vv0pnVn3De59eaL20yS-cM3I1n7KzBSKz0Iagm4rVmSFiEl6ftKky41-ZVGD_qOA2yVzn7TbM5lTTVQCBmBDvWrXI3gZpESMozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMhnNprrSOl2NJof_r3Z-z4kl8okjiNha6DV9roTKy33IDl3Yn0WEgxGtaNKMTJAqEbnRvZRvdnvZkqfLfTKdvH6lsgGjP3UI-UzgrHHiYZq2DhcVM-damMnG0dm8fA2jQQowi0gDyAWyXxb4bEVK-7E01-g8ZuMuh_B4Hm109O5gVFm9URcygDuwNSdkPOWZF8qcP44nljw7DJKzTaGmt0wlv2UzUVycHUWyY2nKgS0ohahpA0xxm2azo_-LkzipwHafOWR3vKBgxkFTHH3L8Tj6p7JfvzHhMJsjEUcFZNL8xENXqIzP_wmfF_oHl6Vfqv-zy6cEKwa5hsvKqhQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHK1G2we4ykuOnWg5iIH1xPg-jjIfyWcMbATP_hxL33Vw1kQFTTFYxxOm22nHgdT0EJSU9nqOFUtZb5xGYOrglvBNy69ks4KoVzjqLKpoRvgre6luAa6IsDfETHxUgj0Nthak6ZKRjwF3NCvUNr5pJxrdDfQc82AfURTy3RCPwpiRV7gaEedqc8QuuhNvlT3jvKOuQqtir1ag5gdvDRXtoB9PiYkVmB6L9HP058iqkoMCRHCyjT9llrWkkAlZfpb8LoxYPB4HSk8uKlIb6Ug1bg0YnIlEnjaYpGDgeJ4eFEuJ6q8IrP4GWlEKweLt-uLMff67Y-mtyUYv38nDnLJFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای حرم بانوی کرامت در شب رحلت آن حضرت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/463538" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463537">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48bda758f.mp4?token=bBt4LwTkiPg-qbVitMz1vBxngDTPLXaVBcQFgBocVXWnWxbvIyIbFlvgT2yy1vHD3pQn99cQyksoQ_ipIKyXzhf6ZwQNEAxCaI9PHHjN8ictPGCw-wAs5bUTXLmUeb4FS2ErK6aj4TCyb2qttYhmNloTP24drDaVGmDfDl9QNfDiyOR8_D9uBrGaJRp_mvYGkVDBjjPGAmxvIM5CxuecdCKXQepEspVHmbz425Arhdehrz3n2Zt6jnT0NVycHX42SrvjQmmwOBnNEHJoxByDtmlnS0bnPa6oJ0YrQuVTIp5xc4YLWKT6myy84xHXgxeuxtEVaMcFKOEP5FESvmpUPTieGZtzlkayf5hQNeCrvIvW18tQEAAOVCDiwkgL6UyPbPwIuLb10boFSkCOBodW9HG9Ssod5yUzIuBbyRf23OFn9qlbpENzqc0kWaHuOULMKv1zfVLpE37LcXcTKg7kirUPITLDHncz5Jauv-JeWEZJBPflYIyc-wYEAopBaMq4I54YIrj6HJTmyGBamzCb7VbjXIk167TPZjOrVRuLEgjGAxU86xfU9O85BX5VKwYNvlJyTmesc5qDBXOEXU1pJWUbWhqhmm3d9ByApduBd3KotWHCrWtawjb_Bkeo-cj_3UpTPjBL0IRoE4-0Tlz5I6UuFW26nfcc2P35GKrLHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48bda758f.mp4?token=bBt4LwTkiPg-qbVitMz1vBxngDTPLXaVBcQFgBocVXWnWxbvIyIbFlvgT2yy1vHD3pQn99cQyksoQ_ipIKyXzhf6ZwQNEAxCaI9PHHjN8ictPGCw-wAs5bUTXLmUeb4FS2ErK6aj4TCyb2qttYhmNloTP24drDaVGmDfDl9QNfDiyOR8_D9uBrGaJRp_mvYGkVDBjjPGAmxvIM5CxuecdCKXQepEspVHmbz425Arhdehrz3n2Zt6jnT0NVycHX42SrvjQmmwOBnNEHJoxByDtmlnS0bnPa6oJ0YrQuVTIp5xc4YLWKT6myy84xHXgxeuxtEVaMcFKOEP5FESvmpUPTieGZtzlkayf5hQNeCrvIvW18tQEAAOVCDiwkgL6UyPbPwIuLb10boFSkCOBodW9HG9Ssod5yUzIuBbyRf23OFn9qlbpENzqc0kWaHuOULMKv1zfVLpE37LcXcTKg7kirUPITLDHncz5Jauv-JeWEZJBPflYIyc-wYEAopBaMq4I54YIrj6HJTmyGBamzCb7VbjXIk167TPZjOrVRuLEgjGAxU86xfU9O85BX5VKwYNvlJyTmesc5qDBXOEXU1pJWUbWhqhmm3d9ByApduBd3KotWHCrWtawjb_Bkeo-cj_3UpTPjBL0IRoE4-0Tlz5I6UuFW26nfcc2P35GKrLHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجهزترین خوابگاه دانشجویی کشور در مشهد افتتاح شد
🔹
احداث سرای دانشجویی نجمه خاتون(س) با سرمایه گذاری ۱۷۰ میلیارد تومانی آستان قدس رضوی، از نتایج دیدار رمضانی سال گذشته تولیت آستان قدس با دانشجویان علوم پزشکی مشهد بود.
🔹
جایی که دانشجویان از دغدغۀ کمبود خوابگاه متأهلی صحبت کردند و در نهایت احداث این خوابگاه برای ۴۲۴ دانشجو و تجهیز یک خوابگاه دیگر برای دانشجویان متأهل به ثمر نشست.
🔹
در تمام روزهای پرتلاطم یک سال گذشته این پروژه تداوم داشت و حالا در آستانۀ ماه مهر، مهر رضوی شامل حال دانشجویان شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/463537" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463536">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8cSQcxUDeHaAKCqpPn1sVGl9WYi6V5eRAfu6fdGcD8p62eLtTxe0zBJhJmOJFAophkftKw9w_mlD0sgd1pSD-FAXgStkhxwQbBTXCjSPrQsFLJSwbRqW7mTKqr-y7e-RvGUulvw5RRNjuFSCa_ieD0i8m9Jb6-9TlJeYA8lobkMbv3KIIAGibshiCqRsj21t2S6L7EuQ8S2vAXmCIGjanfFImdHWb8bU8DIgzS924YTDMHRkswidqjWU2D-1Y6lOBjagKYL_XqdLjpYqLDTLAa7cnLU8-b9tWhZs1ZcUQBW0FYUU0NGC5LmgZa39i-HmO7Oi15ntF0MqmRc0FmTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع آلمان: ایرانی‌ها بسیار قدرتمند هستند؛ پیامدهای جنگ علیه ایران را بر اقتصاد خود می‌بینیم
🔹
وزیر دفاع آلمان در پاسخ به پرسشی دربارۀ پیامدهای اقتصادی جهانی جنگ علیه ایران، گفت پیش‌بینی راه‌حل این بحران دشوار است. ایرانی‌ها بسیار قدرتمند هستند و در دفاع نیز بسیار خوب عمل می‌کنند.
🔹
ما این موضوع را در جایگاه‌های سوخت می‌بینیم؛ قیمت‌ها به شکل باورنکردنی در حال افزایش هستند؛ ما همه پیامدهای این وضعیت را بر اقتصادهای خود می‌بینیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/463536" target="_blank">📅 00:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463535">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61f9e2678.mp4?token=RHRTuINeEKXPj-wVjLdSPJX03OurIGRLI8bfZ3w-JPHD0uS6Nn9tHEeQKHED0vP7ikWcml8ntq0l-7A6Ph_xg7mWgiArzjg0auuuf3AXhlZzXc_r-gMYfEwhW2IFDMCXuIxAubR6DLp9j21FjeabtCdwHCe80JHGFCr8Jgko4qkq8wPB6BnzZJNmQNnGQf270XgkjHgdRbd6ouUNitylsSR7PA_Bqj6podwJb31pBFdQsp2ZjtBKk1nJTTucEzVQqacQf3CQU3O_VJ4tb3tJ80TEqa7HjvXYvUqmpztUTXQ6X8ShCqc3--PMptbhLN_vPV5AMHOfNfL8Q4O8GvvBxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61f9e2678.mp4?token=RHRTuINeEKXPj-wVjLdSPJX03OurIGRLI8bfZ3w-JPHD0uS6Nn9tHEeQKHED0vP7ikWcml8ntq0l-7A6Ph_xg7mWgiArzjg0auuuf3AXhlZzXc_r-gMYfEwhW2IFDMCXuIxAubR6DLp9j21FjeabtCdwHCe80JHGFCr8Jgko4qkq8wPB6BnzZJNmQNnGQf270XgkjHgdRbd6ouUNitylsSR7PA_Bqj6podwJb31pBFdQsp2ZjtBKk1nJTTucEzVQqacQf3CQU3O_VJ4tb3tJ80TEqa7HjvXYvUqmpztUTXQ6X8ShCqc3--PMptbhLN_vPV5AMHOfNfL8Q4O8GvvBxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حضور رهبر شهید انقلاب در حرم مطهر کریمۀ اهل بیت(س)
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/463535" target="_blank">📅 00:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463534">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKgvNjWBd6A9e3c8eL-UfGO_6SeZbj8iNUB4KyqtBYLRqEQizmDz3JpNoXfE3sys9dq2x8r8Z7nXBnsV4IhAUdA5ZtqqWObbLCbtxI8n9a_uSJoBCXAlGUbnPMVtuuJghgWtI0LAs3XGty6A9vMlIAWv1Z3HmNo41OYx7HHchsuGFCNEZiYEwtNOiQGJheIx07BfKfUTyzXZmYIORjwnqrFdE_1ZqFBSzZ27Eq47PZ3BtcW21nLBg7wH76UlKniyScRZh5dEzykNDoJkf8akEYjuYsek-ZAzpAoa2rraklmzV251bPhWwqBpeDfw-EHp2Qj7oMwyELrl-T0rUo11VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ مخزن ذخیرۀ نفت در قلب ریاض که منفجر شد
🔹
بر اساس تصاویر ماهواره‌ای تازه منتشر شده، پیامدهای حملات اخیر یمنی‌ها به ریاض، پایتخت عربستان سعودی دیده می‌شود.
🔹
گزارش‌ها نشان می‌دهد دست‌کم ۷ مخزن ذخیرۀ نفت در تأسیسات ذخیره‌سازی و توزیع نفت در نزدیکی فرودگاه ملک خالد آسیب دیده‌اند.
🔹
فعلا مقامات سعودی در این‌باره سکوت کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/463534" target="_blank">📅 00:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463533">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">عراقچی برای شرکت در اجلاس سازمان ملل عازم نیویورک شد
🔹
وزیر خارجه در مسیر سفر به نیویورک توقف کوتاهی در دوحه دارد و دربارۀ آخرین تحولات منطقه رایزنی می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/463533" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463532">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdcKANPMJljTuFksxtpVpZgTurUjl34SVn4k04hAnSZWUpW8FtO5aeAjV7vr_S3IpLFGUr72v-wflb8-SNXUZ4YMG8YAZewUu3AUe2jjZyOgb_t18MOcKrK4z2DMDezNpAzOCiJb3R8MARFt9-zOEBLhU7ERLg1TjNNRwUku8cw308Aow1AjsbvgK2XcfbtmCt30UN504YqxKYabKL1RNSB-38IWrclitEdWLl7KWKlKkXuRbX-EY42Aw5HCVb1VWrSCO4XXADJi5l-rayalK9HF-I0DmqVIalR0WYhZFEr1_hbig4waABMYsyZJ0lR8_Z7mgndkhKgPcyJWtfUMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورنومنت چهارجانبۀ تیم ملی در عراق
⚽️
تیم ملی فوتبال از ۱۶ تا ۲۶ آبان در تورنومنتی چهارجانبه به میزبانی عراق شرکت خواهد کرد.
⚽️
ایران، عراق، لبنان و فیلیپین در این تورنومنت حضور دارند و تیم ملی ابتدا به مصاف لبنان و سپس به مصاف برندۀ دیدار عراق-فیلیپین خواهد رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/463532" target="_blank">📅 00:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463531">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOQfuF7W28SAKwk-mdsTYgbmU4_strNK_jllSDZsW-Y4WJH2jSF3LkTYHxNOtMGVXDNPBe5aXY0QMyy9ocLEngx_CmkwtCVNLKZoA1VjFTqElkSCKbc513r9aMnK7jWWaMer37g7HZYuLRCFWSLrvw58BUnmwv-yMUv3fB4R8lwaJS5UZKceKGdZ7CxwNIw9HwM9oDS29xIeRAOat-G1ZsKYJZje058xNL1yS8r1K2Gy2SvT5dJBgAvE_lphsfZ6jvpQF2i4CJ5l5RRs1hpp6AthrwBN9y56pgyGeL-ylqAI04P5LGvZfqE_sE5jqu_OLMCHygiCDrDjtk6wwRSHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سقوط مرگبار بالگرد خبری آمریکا هنگام پوشش تصادف
🔹
در پی سقوط یک بالگرد خبری شبکه «ان‌بی‌سی لس‌آنجلس» هنگام پوشش صحنه یک تصادف مرگبار میان یک خودروی شاسی‌بلند و اتوبوس، ۳ نفر جان خود را از دست دادند و یک نفر دیگر زخمی شد.
🔹
علت سقوط این بالگرد هنوز مشخص نشده…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/463531" target="_blank">📅 23:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463525">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4m9BqPuHVx53WWS1mgvjjhxC0UZ0uv6_Qc7RP0Zqo1T_Sr9LjiH8thb6DBtOOlwYPNjqImkTk6La4q2jWoYi6fGPQvOITwa7fDWkCBVbh3HkGODbQeOune5jUZScT9CwhB-xuXeSri-I9Fr08ljOe0ZwBH7l0hnxr4Nc3Jf8UhhcZSL1VBxt2OVu36f8SU8v7uEw8_mFb6Jq09ZhYVvQS0CR8WqRsCePk-XGUjfUVngzaP286VHmpzG77V4_RKQgLi8lTeuO95cK6UdjFWyj5D7O9y_szAdmwY7LAL-1dfCOa7jKxtlsXugy2SHHYrhlXW76CApdGQog7sBG4iibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHHxH_0tosIxKUcez3LjiGs9gOF-tCheWzdeLRKf-HWGVtbkmg952xPcJPhUGCmgIvasQoykOU1l42AwXW_KgcTxQCDwrHlrrci4XSOhsV6BTi1jHl2OWbqNcqsB7BGbSdmw2a1CUPZJne6jXFj3dcMw6AGPoWeFMRMIsOC4qC-OYQQe5zTL62VIs5OYf5d3etE_sSOaxKg60RBQsS5m3jA1JBJ6kgIVOV0svc834ffFUf2KbjCHTXe-A5ipADBI9N6ls33Zoz6-kqcx78BbT-leykith6XM3653YVuHaywI6bOmbfLAoJuZcWqGyIxPG_4zejy3gD5hQ5fWE_i0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-Pv7xcVt74qmoT-5a05-CLfzVwbulbnVoV5Ym5C2I-pqgR_xVkO11K_gl1o3YqAkMYg3sMjAuIzKIXgz8h1_eIvlTgDGm06zJPp4Zs9LDIkBoh3p7QHmRGcMAoNH-0WpMc-e_9r7U13feJZ_PGqDlCN-yLYEScWee2BNIKydvqCFJZBsWJ5pQiT8NZwDZ-6wwHmEDkKE9Okl5O_Mtb5ZXHbWG6UItl-HXsMbYSkS79_FUKfGUrEGOXPRxsQn_fe43-fDt_mf3WvIdeYEbdCHbhoc86Q6HTs9PX7lMasWKf8-MwC-cIUt0vZf8pepHuzCpAN2zP-_YuelNA4KETZuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOAGZhUU0fVag0O00fvJFI1z_e2gPTLfPQJoHgrAJJmYX11d-F9-0JdmjQ_Wf9i7JWo7e2svDq1MTRA9lE3I2dgpMBNFdjbeEeucxY6xIG9mLXyw2kL1VTtrN_WEhEg3MDNYXlkr465XtmfG5EA-0GJaO0oHoPXVwArsyhte55-YrgcJ5o8RFb4XQWqfit7jk3TYXj0tIAl5Kbnvy0Xua_wOePEjxzmRfnS-kBXA_gxIerSd1ICB4OgrYA0mYjPSHQqQEtstKkdTnqBDfamKAhL3sUf9VEMNK3J-gudJoNUsNadz_FV8Kto42ofFQniXpiqG7Nd5Hr8KFsIH7jqNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0eETXtEL0hFEeI1sDWWt7uw2FJPMlx237rKxpt3Q3-53Z-dBrLJqDq8OH6yWw9kvY6rN-RJDg32ALFOn1_ti1aIoMyrZJDVe7J0k8KkOsdKc7f_XiyzhRv63PDDUL9DGh_AB4EboLl9BjlNCcduNKav0L8lIXLBZspHwC1DIrzUilOvfaNxbISBeKs9UKOvD9m01XXR1D9isgblcWVyiFag2vASyv47s43JOld9bIJZyGS0bkLiFLn6qOo_VnPi_c6Om9YIeWsWpu1H-ngxf6X7TYHwP7BPG0AemiaCOYzb2DHdA5FDmah6GycULqbYrYGdvXYUKw2zf0pv5oLtLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WfUV4u4tcxyjvSOfxmoU3k4HptgDuf6H29FEnGkqRvTIgB_A8gM8yDNwN3nX6rnfv3vtGQP7HLsvxOfkobZZw85FxRDu_joO5i3QNLWNdCv6gjh3Ok3anHAeikH2c9I_u9PxcbV9f0RblV6z0YsleBEEyfVxNAwAQXAcLrsq1DDisVWY6b6GAsKIXJT298H_x4hc5JtUn9JkSzGd1NbHZ6R5-dpn-X_dMu0SP53x2ML6gz__2mwDPRnj1TsQN9Wemww-nqtqX_8GZ4q_qnRYaXh1K7B9gNKAUGLzm4zdcKGwLDLR5TRmwWM0XMlzDbR8DokcJysEYmJj9bEM7Fyezg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تمرین شبانۀ تیم ملی در تهران
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/463525" target="_blank">📅 23:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463524">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEvhMIfG7jhYXKf3vOtk4-pZe_hjdqXz7PPUH6PmKEadtP7uy1FqdycF9DPiOm7iZ_lTiW-Khf6OmcCaa254I2Y16RNYUZ5IhdmfvEYRxYwTSOi2w-a3V0Za_UW5ViGxCVgxBgqXNDoxYZbTj0gY7Dg1j4ez_sjli73PQtku28eUo7kJzf3ir4TKPWJzBOiU6TQSaOwp1hfm8VMN5tgfskwU6W7y44jRP2d176si19Ih6PdLnoK12d8D9SEAoDSkAqZbGk1g8b6SrxZnmiTWXBq_NkVj2RjBf5JxUBRD2xndsaxzpciej1EdKc_c5Hg4KyJp-SfUEWn8xK1HIJzcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب‌رئیس کمیسیون اصل نود: هر اقدامی خارج از رهنمودهای رهبری، از مسیر وحدت خارج است
🔹
حاجی‌دلیگانی: معیار تشخیص حرکت در مسیر وحدت یا تفرقه، توجه به پیام‌های رهبر انقلاب و میراث امام خمینی(ره)  است.
🔹
اگر فردی مطالبی را مطرح کند که در نقطه مقابل این معیارها باشد، طبیعتاً مقابل خط اتحاد حرکت کرده است.
🔹
نظارت مجلس، سؤال از رئیس‌جمهور و سؤال از وزرا، همگی در چارچوبی است که قانون اساس تعیین تکلیف کرده؛ پس هرکس بر این اساس عمل کند، به وحدت کمک کرده و از اختلاف جلوگیری کرده است.
🔹
در قانون، برای اظهاراتی ازسوی مسئولین که برخلاف شئونات باشد جرم‌انگاری صورت گرفته و برای آن مجازات نیز در نظر گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/463524" target="_blank">📅 23:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463523">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWuSbQlw3nyj4-6lG2vLeOtFYLNw57iUFmS261-MCxu_xjxdMPFXYt99NZgrsbu3-07ugFtcD7m6tyKtl_jNUcgrysP0pWXjCAoqk4T9Kt7uARUH5zIGoy9aHj7CUylguXAGj6nRrIJHgoxkQwiLf8SJJgi3gU-srLaNudKiFSVnZL0Dec43ZaDTk18SYWHvigakjXYF56D0EN43u1ejLGuMoh_AB171xqFkvbntH65oTPSGv3zTjTVsaCjE9LFLf1rtS385l4-WTJg7Gcqw_kUB6D3gip5MsKw1tuVN3mGQcun3cZ9afItBvV6_RqtWBjXO5H7JOQnasmW522qnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب پوتین در انتخابات روسیه رکوردشکنی کرد
🔹
حزب «روسیه متحد» که از پوتین، رئیس‌جمهور روسیه پشتیبانی می‌کند با کسب ۳۵۵ کرسی از مجموع ۴۵۰ کرسی دومای روسیه، اکثریت قاطع این پارلمان را به‌دست آورد و رکورد جدیدی ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/463523" target="_blank">📅 23:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463522">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5521d6342b.mp4?token=Kdu2PO95u9yge6pdYYJAbwTJ_XIlxm_6rKKgsjb_iyg2rBIDZsbTeTmw5Vk67Gq7i6MLlg2FnSa7dhWFEPcpUxpw7dB9LVA7UywOgiuW1Vepnoiig9oijvH100CypjuJoIzPPRgq_7yxhpBtMKVQ33Us0fzh9OX0goprdoGXsUsPotADCzP-h-fV2OWD8Ez99E1pI4wL9CVx5-mjSUDLRvhNCoCeBwvEoiiQCKXKl0Iz_fDvDFllj-qudE0aeqQEIQbjuMIIqhGywpisDpEsJoJcs_ipACoGFbs8qOF6gIyCa7Qi37kh0IeUnQ3Tml9ADPKBwWhPhZqdKjDHO3CfEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5521d6342b.mp4?token=Kdu2PO95u9yge6pdYYJAbwTJ_XIlxm_6rKKgsjb_iyg2rBIDZsbTeTmw5Vk67Gq7i6MLlg2FnSa7dhWFEPcpUxpw7dB9LVA7UywOgiuW1Vepnoiig9oijvH100CypjuJoIzPPRgq_7yxhpBtMKVQ33Us0fzh9OX0goprdoGXsUsPotADCzP-h-fV2OWD8Ez99E1pI4wL9CVx5-mjSUDLRvhNCoCeBwvEoiiQCKXKl0Iz_fDvDFllj-qudE0aeqQEIQbjuMIIqhGywpisDpEsJoJcs_ipACoGFbs8qOF6gIyCa7Qi37kh0IeUnQ3Tml9ADPKBwWhPhZqdKjDHO3CfEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محاسبۀ غلطی دربارۀ ایران که در ۳ جنگ تحمیلی تکرار شد
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/463522" target="_blank">📅 23:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463515">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYnZnauRQWKv-3n2U9cMks3Z1XUxYjsIa6OqcPoKtdeU4pGAng4MC9LSPrZQpV1dO0ejV7FBKQdyZj_LDvAIK9l7jaeHQBfEI2P4kCfYDoxiCAPqqdNecTY0j0Xy_GpaTqEr3-1SU-uzGipaNnRQ8qKiYqZHiXB5e-wZ4D-e_UrnB0vKl_c9UuNv8v_wzQ05fdGUWceKM3U4ROpXyaj5mbOdGuxFk8Ay87lWHSmC4BFdeOozwu1UR1X9XbzVs2WMKccTBXQ5_pPaui0ieggBEqd7zG4Sdg1u5EnTUjIxltTkSnfmogrtCiBw06GCFu-BM4-paHMvuhd6hSbHz7Kmuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7PECGj_i93KpFNElENpI9dP7TpgM3KrGDSDNb7pelQlzLrj-bTqgpuKs3xeiN6JPxYBOSfSb66wMsYGtMpjo2pNRUyuo4au4cDbtOEyd0mWZxbtJqeOLvh5fWwRUTL1orJBfHkYsJGzhjlnqflNw8IU7RwxNRUj9ziQ_1TpIQX0gPhpB3q8mMOn95iFb6Z8eDZkcwbrBJZ-4fkhMILKVmRjHArK2uy_egvIOzUKVXoTqca6-W6qr4d6whNm72Kz2ZTL6CWk9o16M3SEJomCyUZ9QowN4Uamx1SBZEIZeqX57medali22S8y6YHZQn1GcFgZGRl5WKnB9ow4W8KIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eI3b2yC3cRsNPiWa3iHbvYnBzbCQKYOG5j2ESxSdBfLjk7HVByraChAm2SmpzvgaYvdeSTaVzBUGUhtZoU5t2B2r04M8Jqz5xEYEEUCVxgnAKKdVS_VDR2rqWk4QJ3mrQrrm41KuuiMcC-rkadOoAcMnJvxFHUpusCCUxUdmJcHC93cpsGhN9NyxdqdA6BPXzaIW4H85E9ptrbAQAyXUhofMeS5aVuGcAztc_w905Uqd9nKem-IYU6MsZs_frOtO5pr_0mKOLjm_uISNvFu5tvVM2pHoqf4AZDNlpwM_fLkmyo8PdRPsaTDHQtXtnDcndTe-Eu8rHB_OGnNvH1wSXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEbIvF-E1QQso550ckGpvezYAzf65wypsww5ddhIkGXmzEEWDbQtPhzrjXpP-34fB6dIeaR3uSeoqb7Hv2XWS5xzDvJ4XMO04s9M72BVTVtpygXwaFq6wrO4K7X3iCbvec2C-gH-OxgibXf7NC4MdK05aWPCopeBH7gsiHigHBlAuUfZkemEMcUTGKl4E7QHZkopYyJR972H_s0HD8u2nTnYPgkOQN9Uvd-CUIUBw2nOBWd6lGkFV9LYP3Ekbn6iuCbalg2lkYvP8jq0Ao_MDOcCsy7Bc7CnDO2yR7A6h6miV21cz0AlNICu7HJCSEQcX7NQ4IWWieoKUniZd0sfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJet7uQ2z2_dGeSD5ou8SZ2b4KKi8YVX7-CzCFAkMpF-HmrKKLfcOWDYPDs48p0YDoXdOD9u5Aaw42FB-hCRzxqu1OW7AR3wsesXGwpqe5brQZqbK_F6IqZ4zkvMqxYaW6sNUqYYH2-UWAJFxMCrPdndqzOdSEi_DISyYof9anE-ZpConpQg5XrpYnXH2RUHIpNNwQ0g3L6pAs1ohePzX2vZi--TKwwPDCz9Am3J2Lbno_dIE3QF8UAvmSpUzAMDaRUqMTwhRBIOidAvSbYEre0X8SQ2R3WW4VxiuPrRJPm5tbYgOVZbUEyqQsWdNuT2VpIku5XbcL8Ek81q8ybPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJR9UnJfJIJgfptZwTiI64am-fq0x2XGm_ef_KL4luY5oFuPEv759YqBG9ZAwaCI0kWMXPCQzkfCs-YEovX7Omy4khUGqpTGQbxeLTB1Ao7FqqG_kXnP3gZB43ciZ1Bq0aUsCOIPn8DmLbsmSmZ0pMpdHlj2p1WWX5NvMKNMo7RO4sELpmZAHyeOKyI-qPX3T8MW_GKcl9SVIElbymEWTWy6ZQPk0jZTJ96Sl7YfA0m_7YcD1PMjimTvGNxSpSuU1018zwt14cU26VOQvJROUCGvlPlpgGOoZAyZuIpkFSXvud-YvdDOjFGSYnzNBGgTR0NnuwTYSMzmqG6Dsh4-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bp7QdLZks_b1Kityq3YDxghemHvyQfut9al3iof1c52g7rzUNgdPxA_7VMZ_-knfHLr1O2jbsOpOT91dNHv2segiIaYkvsTHJRK_OUfAP27r7_9Y6-n6_kfyOKawyxqsmlL_VvIfutUBVXT675dQfKGXotoYxGBKpME1BGQ65-D7ZhjDYFK913c_bOZzYlwthzLFXZcA0iKf7LWCSnDBiej9qk981Mpu1_eVXY_DOlbKePR0AQSH_FehBcoTzyKfBPIwe-CemKJTslTnlJ5Dm08z71JdEt_OuZSUyRiVKpWYQ6-Vb_ltuACiCaS_f5NS9XAU8scxsmYX_RUc2EJmQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین وداع با پیکر مرحوم آیت‌الله شبیری زنجانی
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/463515" target="_blank">📅 23:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463514">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJyJq-h7VeEJt75W0GG_wItW4cb4uoI8np3UFqN50D556MIHclwPdmrs5Ub0od31HutIBX1w042ZsCJgHfIrJuEFYjyhyFKe1jeweXdGFGg8Ot943cKGj-n8cdUfPu-me6m-YxxN59bsoD2OS1skORS07JoD4Xp-DgDmniyxEMwoeARRPBuk9Wo2tqU9KrjwaBH-AYQGQqDrK_-dQliG9J7qjeSUQC0YkO9Et3YozZDkIZmKqhrem9fUPkGcZbhNItzOnkbAA1QHuhXrwIx1LhDUPAZMfpRulEFKU2ExcH-8WtubHWWOvasmTjBcif3aPENqehSzrTTF586bTkTYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جانشین فرماندۀ سپاه: درحال تقویت توانمندی‌های نظامی هستیم
🔹
سرلشکر ایزدی: اگر هوشیاری مردم در صحنه استمرار داشته باشد، بسیاری از توطئه‌های دشمن نقش بر آب خواهد شد و این خود اثر بازدارندگی ارزشمندی برای کشور ایجاد می‌کند.
🔹
ایران امروز در حوزۀ موشکی، پهپادی، موشک‌های کروز، سامانه‌های سایبری، جنگ الکترونیک و پدافند هوایی درحال تقویت توانمندی‌های خود است.
🔹
جبهه مقاومت اسلامی نیز در میدان حضور دارد و رزمندگان یمنی در مسیر مقابله با دشمن حرکت می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/463514" target="_blank">📅 23:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463513">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMjJdO-O2bMecPFs7OnALRc2N3Iau065GP9fpLlrAQcAgJ_og06yXePdQNvw34bl3g8sPE5aCo9PXC2nYcgTZZmCp1J-UILZQOmW_xgrJnHR3ZfHplxUFPFh_NIDpUpUtuO6YU4GZkAn9lz5GcVUA7asXAtkqdg_OZq4RT-AaFtYYt4ljtcNSdkN2uxJ5oTJrGq44a-jdNUzwytCIf64lDr85AwrXaiUDG5W3cwNOdgu29od25LYF-4PI1vpyNSka7iC7RuypkbXVrafrqS1-dgrLXG9I3YGzb3ww4yWfHs9Dn0VwownJKESv_Cw5eQH3G2WNqrdaaGlNPBR14fddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک به چین؛ ذخایر نفتی ریخت
🔹
موجودی نفت خام در استان شاندونگ چین، یکی از مهم‌ترین مراکز پالایش نفت این کشور، در ماه ژوئیه حدود ۳۵ میلیون بشکه کاهش یافت.
🔹
افتی که بر اساس برآورد Energy Aspects، بزرگ‌ترین کاهش ماهانه در داده‌های این مؤسسه از سال ۲۰۱۶ تاکنون بوده است.
🔹
شاندونگ محل فعالیت بخش عمده پالایشگاه‌های مستقل چین موسوم به «تپات» است؛ پالایشگاه‌هایی که سهم قابل‌توجهی از نفت تحریمی ایران را خریداری می‌کنند.
🔹
کاهش ذخایر این پالایشگاه‌ها می‌تواند آن‌ها را برای بازسازی موجودی، به افزایش خرید نفت در هفته‌های پیش‌رو سوق دهد.
🔹
داده‌های جدید همچنین نشان می‌دهد برداشت از ذخایر نفت چین پس از ماه‌ها کاهش واردات، همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463513" target="_blank">📅 22:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463512">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01ac8747a9.mp4?token=I9ON3103agexrz2kPL8XVqNAp7odn5KLuJg0i69Gwfbwk4Fw7RcC0w8OSzwuvPCrBAHRyqDfC07prY5XFZSj42QNRjWbWVA1Bt4wawD0Itgvz3VxHvic15cKFT9N0bP8qVnNtt5sk9LfjOF8L0K_xLm6jySjLXsjCDYOvu22mWz_F513Kvmhwl-iFK1FQ_TtJsRVgpyzSzuowdSNR7EgeKAeHTj7ubPk3XodWjv0ejv-ybG9q4YgpqM3WTBPORvFDmUr40kAKy7yw4zHg-A3nV1gKHSzT2grCOp7tTkZ7Qhsutlxa9jqPFPzynWCHlD6BTeZRW7cCH8YZPtzL3AMVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01ac8747a9.mp4?token=I9ON3103agexrz2kPL8XVqNAp7odn5KLuJg0i69Gwfbwk4Fw7RcC0w8OSzwuvPCrBAHRyqDfC07prY5XFZSj42QNRjWbWVA1Bt4wawD0Itgvz3VxHvic15cKFT9N0bP8qVnNtt5sk9LfjOF8L0K_xLm6jySjLXsjCDYOvu22mWz_F513Kvmhwl-iFK1FQ_TtJsRVgpyzSzuowdSNR7EgeKAeHTj7ubPk3XodWjv0ejv-ybG9q4YgpqM3WTBPORvFDmUr40kAKy7yw4zHg-A3nV1gKHSzT2grCOp7tTkZ7Qhsutlxa9jqPFPzynWCHlD6BTeZRW7cCH8YZPtzL3AMVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الهویی، دستیار قلعه‌نویی: ۷ بازیکن تیم امید در لیست تیم ملی بودند
🔹
اگر مسابقات آسیایی ناگویا نبود این افراد به تیم ملی بزرگسالان دعوت می‌شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/463512" target="_blank">📅 22:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463511">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b814db725.mp4?token=uTnN_uiumNVheVpF4phWN9x_fZWi_1c1FlGCIbjTevpGhtQnaVKyWozkkcNfKZp8bozj5VVFXZHbjSgQtCkTgfz1ELgZaDbVP3DZ7rFV5Gzpk6jNixrZKxY6QyVoDGioPJYs6dxhmXj29Mo1qrjKb6VceGNMuuxyEWVAcDlCw0kSbU0usV2q-hDdU_rB0Z_XJx1bE-r37aLM4OQhyIkMij04xlhOnywTNLQ2JuT2YUrEsT3VJ9lmQC1R92Jc3EGpRtUs1MnxfXOzIPBbcxj9cx6oty9YZiOisWNiP8nE2J_HealJdt_oINKRp9HtUyV-ggxWzDrQzqtt2YzQ8LrZEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b814db725.mp4?token=uTnN_uiumNVheVpF4phWN9x_fZWi_1c1FlGCIbjTevpGhtQnaVKyWozkkcNfKZp8bozj5VVFXZHbjSgQtCkTgfz1ELgZaDbVP3DZ7rFV5Gzpk6jNixrZKxY6QyVoDGioPJYs6dxhmXj29Mo1qrjKb6VceGNMuuxyEWVAcDlCw0kSbU0usV2q-hDdU_rB0Z_XJx1bE-r37aLM4OQhyIkMij04xlhOnywTNLQ2JuT2YUrEsT3VJ9lmQC1R92Jc3EGpRtUs1MnxfXOzIPBbcxj9cx6oty9YZiOisWNiP8nE2J_HealJdt_oINKRp9HtUyV-ggxWzDrQzqtt2YzQ8LrZEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد ضد استکباری کرمانی‌ها در اجتماع ۲۰۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/463511" target="_blank">📅 22:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463510">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رکورد حزب پوتین در انتخابات روسیه
🔹
حزب روسیۀ متحد به‌عنوان حزب ولادیمیر پوتین با کسب ۳۵۵ کرسی از مجموع ۴۵۰ کرسی دومای دولتی روسیه، رکورد جدیدی برای خود ثبت کرد.
🔹
این نتایج اولیه مربوط به انتخابات ۱۸ تا ۲۰ سپتامبر است که رئیس کمیسیون مرکزی انتخابات روسیه اعلام کرد.
🔸
این نتیجه اکثریت حزب پوتین را افزایش داده و رکورد قبلی این حزب یعنی ۳۴۳ کرسی را نیز شکسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463510" target="_blank">📅 22:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463509">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMCpvET44NsAuBxRQaQfEKGV7qNWVf6yLA5melU8PfJRYThjJbSKzzwc05Q_V074NTtWJRw3Ei6KZ7brka-eoJS9FrN16CIVfaZuRFYhs9B96nXBi0wY_CaNrKMWAMBMfNo1Zp13TwSqF1taR2IA-pgcG92SbLgSx3tflhIWf0CP1hPyMUzxq2VwiUZZwmiPexbbZ17aivHG9GSY6WYPA4VXLwG0GSDqiHO0Wv39KDEh7RVo48ICLZEGFP1vXEp7s1WVpvBLRgJsVCGj5oy28SroMcA_L7ngX90JFwiATQc9RbAIJb0u014P202m27FB-Emlk-epCxmDB7p6evI5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر سابق ارشاد: دوگانۀ میان «جنگ» و «صلح» غیرواقعی است
🔹
اسماعیلی: رهبر انقلاب با صراحت اعلام کردند ارتکاب هر آن‌چه به ضرر انسجام اجتماعی باشد، ممنوع است اما بخشی از نیروهای سیاسی همچنان با ادبیاتی آکنده از ناامیدی، شکاف‌ها و سرخوردگی‌ها را تشدید می‌کنند.
🔹
نمونۀ روشن آن، دوگانه‌ای است که بین «صلح» و «جنگ» ساخته می‌شود؛ درحالی‌که اساساً دوگانه بر سر «مقاومت» و «تسلیم» است و تنها راه ادامه مقاومت برای تأمین منافع ملی است.
🔹
ما باید یاد بگیریم مطالبه بر اساس موازین، خلاف انسجام نیست؛ آنچه خلاف انسجام است، تخریب و توهین و ایجاد بدبینی به مسئولان نظام است نه مطالبه‌گری.
🔹
انسجام واقعی، انسجامی است که در آن هم نقد مسئولان و سیاست‌ها ممکن باشد و هم مسیر دیپلماسی برای تأمین منافع ملی باز بماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/463509" target="_blank">📅 22:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463508">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429a53ffd0.mp4?token=Ar5xcj3KriPbXLtLOcBJVmrNGInbKgHJ3oso2MJLQm1y7etQQDQi6ZCQ4Jl5mBOIARvFnSyMS2us-lYODFwVtl5HeaByI7DJzruia3fgRi1vXggZeYT0JgxfvrBC7NJlZ7nJV3Ve_LU1_1x44Trrq69blvWIE0c0IUvmwcbwAtjmv33N-N-vILIo2swQcvz8dyzQo-c12sRSg3XJmaawNjMO3DKTohG6dwulXU7i_oqFGorFmohJRKmQEhZJDOsraekDyF6YeRynWwdfOsmIvHe7Ylda_2siDqMMlciGBL4vAoqmNgPCOLauDhZIalBmN3kxoY21Xhp6LZX9LUr9Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429a53ffd0.mp4?token=Ar5xcj3KriPbXLtLOcBJVmrNGInbKgHJ3oso2MJLQm1y7etQQDQi6ZCQ4Jl5mBOIARvFnSyMS2us-lYODFwVtl5HeaByI7DJzruia3fgRi1vXggZeYT0JgxfvrBC7NJlZ7nJV3Ve_LU1_1x44Trrq69blvWIE0c0IUvmwcbwAtjmv33N-N-vILIo2swQcvz8dyzQo-c12sRSg3XJmaawNjMO3DKTohG6dwulXU7i_oqFGorFmohJRKmQEhZJDOsraekDyF6YeRynWwdfOsmIvHe7Ylda_2siDqMMlciGBL4vAoqmNgPCOLauDhZIalBmN3kxoY21Xhp6LZX9LUr9Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوزادی که قصه‌اش از میدان خیابان آغاز شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/463508" target="_blank">📅 22:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463507">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFafty5YR6Trh2znZnl1YX-LgcSe4npATsfYmwS9G3JpO3ypl84rvipkLLQZGwRSaWb4ApJIU_t4zKiSSozVGBvVXt7HMSdfsDe2_Oyl-Pbl28z2jB-nRJyLDa4JduhBdm_QPg8PLRsXiZtC78JiCeMqiLtdVpM-392YYdfEo3UVG0KCVNvEkqLS7gvef3rsCJvpx7-gdna4pj00Ow0_OHWIHzwRi8ElfXVlD3iSn0VnCLX9oU_t-37MT0i2cjz8x3VPa6flT1-oaJ1Qffytu-gDbfOlSeqwlemmPsi6_c_0vgOJZiUEs9W9hq_bL372Da-eov2-x1EJs_8ieJvJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت ۹ انگلیسی مقابل کارخانۀ سازندۀ پهپادهای اسرائیلی
🔹
۹ معترض انگلیسی مقابل کارخانه‌ای متعلق به شرکت اسرائیلی البیت در استافوردشر انگلیس هنگام اعتراض به همکاری‌های نظامی با رژیم صهیونیستی بازداشت شدند.
🔸
این اعتراض‌ها در ادامۀ موج اعتراضات در کشورهای اروپایی علیه همکاری‌های نظامی با اسرائیل و در واکنش به جنگ غزه برگزار شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463507" target="_blank">📅 22:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463506">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
من
جوانی
بیکار از
خرم‌آباد لرستان
هستم. با وجود استعداد و مدارک مختلف به‌دلیل کمبود فرصت‌های شغلی و مشکلاتی مانند شرط سابقه و پارتی‌بازی، هنوز
نتوانسته‌ام کار پیدا کنم
. بارها برای پیگیری به مسئولان مراجعه و نامه‌نگاری کرده‌ام اما کسی پاسخگو نبوده است. خواهشمندیم صدای جوانان بیکار را به گوش مسئولان برسانید.
🔹
معلمان حق‌التدریس دانشگاه‌ها از جمله
حق‌التدریس‌های دانشگاه المصطفی
از
ابتدایی‌ترین حقوق یک شغل برخوردار نیستند
؛ نه بیمه دارند، نه سابقه مفید، نه امنیت شغلی و نه حتی درآمدی که بتوان آن را متناسب با زحماتشان دانست. در حالی که بسیاری از دانشگاه‌ها نیاز آموزشی خود را با استفاده از همین نیروهای تحصیل‌کرده و توانمند تأمین می‌کنند، متأسفانه هیچ توجه و حمایتی از این قشر نمی‌شود.
🔹
چرا دولت وعده‌ای می‌دهد که در عمل اجرا نمی‌شود؟ برای ثبت‌نام
کلاس چهارم در یک مدرسه هیأت امنایی در منطقه ۶ تهران
اقدام کردیم اما با ما تماس گرفتند و گفتند
باید ۲۰ میلیون تومان شهریه پرداخت کنیم
. اگر هر کلاس ۲۰ میلیون تومان پرداخت کند و مدرسه ۱۰ تا ۱۲ کلاس داشته باشد، درآمد مدرسه از این محل به حدود ۷ تا ۸ میلیارد تومان می‌رسد. با احتساب حقوق معلمان، مدیر و معاونان و سایر هزینه‌ها، این سؤال برای خانواده‌ها مطرح است که
این مبالغ دقیقاً صرف چه مواردی می‌شود؟
وقتی مدارس دولتی و هیأت امنایی هستند، تکلیف آموزش رایگان چه می‌شود؟
🔹
لطفاً صدای ما را به گوش مسئولان برسانید. من یک کارمند سادۀ دولتی و
نیروی شرکتی هستم. چرا برای
تبدیل وضعیت نیروهای شرکتی
اقدامی نمی‌شود؟ با این حقوق پایین، از طرفی قیمت کالاها نیز روزبه‌روز افزایش پیدا می‌کند. با چنین حقوقی چگونه می‌توان از عهده هزینه‌های زندگی برآمد؟ آیا
مسئولان کشور حاضرند فقط یک ماه با حقوق یک نیروی شرکتی زندگی کنند؟
🔹
لطفاً شکایات مربوط به
وضعیت خدمات‌رسانی در بیمارستان سینا
را پیگیری کنید. رسیدگی به بیماران بسیار ضعیف شده و شرایط برای همراهان نیز عذاب‌آور است. هر زمان همراهان نسبت به وضعیت رسیدگی اعتراض می‌کنند، پاسخ داده می‌شود که «اینجا اروپا و آمریکا نیست که هر بیمار یک پرستار داشته باشد». از طرفی گفته می‌شود شب‌ها خدمات کافی به بیماران ارائه نمی‌شود و همراهان باید برای مراقبت از بیمار، از بیرون پرستار خصوصی بگیرند.
🔹
من یک کارگرم و یک
پراید دوگانه‌سوز
دارم که
تاریخ کپسول‌های گاز آن تمام شده
است. برای تعویض کپسول مراجعه کردم و گفتند حدود ۳۰ میلیون تومان هزینه دارد. با حقوق ۲۵ میلیون تومانی و داشتن دو فرزند، واقعاً از کجا باید این مبلغ را تأمین کنم؟ در شرایطی که
هزینه بنزین هم افزایش پیدا کرده
، خودروهای دوگانه‌سوز برای ما یک ضرورت هستند.
🔹
حدود ۵ سال از تحویل
واحدهای مجتمع فردوس مراغه
توسط انجمن خیرین مسکن ساز آذربایجان شرقی می‌گذرد تا به حال
اسناد مالکیت
واحدهای مسکونی به بهانه‌های واهی که اکثرا از اعضای تحت پوشش بهزیستی هستند،
تحویل داده نشده
و موجب مشکلات بر این قشر آسیب‌دیده شده است.
🔹
من
راننده تاکسی درون‌شهری
در یکی از شهرستان‌های استان خراسان رضوی هستم و حدود یک سال است که مشغول به کار شده‌ام. از همان ابتدا درخواست بیمه داده‌ام اما هر بار که برای پیگیری مراجعه می‌کنم، مسئول مربوطه می‌گوید
باید جواب از تهران بیاید
. واقعاً نمی‌دانیم چرا بیمه رانندگان تاکسی شهرستان‌ها باید این‌قدر بلاتکلیف بماند. ما هم مانند سایر رانندگان
نیاز به بیمه و حمایت داریم
. با توجه به هزینه‌های بالای زندگی، دارو و درمان، نداشتن بیمه فشار بسیار زیادی به خانواده‌ها وارد می‌کند. فرزندم نیز معلول است و هزینه‌های درمان و دارو برای ما سنگین است.
🔹
خواهش می‌کنیم در مورد
افزایش شدید قیمت انسولین قلمی لانتوس و نوورپید برای بیماران دیابتی
پیگیری کنید. قیمت هر قلم با وجود داشتن بیمه تأمین اجتماعی، پنج برابر شده است. من همین شنبه برای تهیه انسولین یک میلیون و ۵۰۰ هزار تومان پرداخت کردم؛ این در حالی است که هزینه نوار تست قند خون نیز جداگانه است. ما بیماران دیابتی هر ماه به انسولین نیاز داریم.
چرا ارز ترجیحی انسولین قلمی حذف شده است؟
این دارو برای ما حیاتی است و بدون آن امکان ادامه زندگی عادی نداریم.
🔹
کارکنان کارخانه
واگن‌سازی زرند کرمان (پلور سبز)
دو ماه است که
حقوق خود را دریافت نکرده‌اند
و هر ماه به بهانه‌های مختلف پرداخت حقوق به تأخیر می‌افتد. در حال حاضر کار کافی در کارخانه وجود ندارد و
اعلام ورشکستگی نیز شده است
. از طرفی طلبکاران برای وصول مطالبات خود و مصادره اموال کارخانه مراجعه می‌کنند؛ در حالی که حدود ۲۰۰ نفر از کارکنان همچنان در این مجموعه مشغول به کار هستند و زندگی و معیشت خانواده‌هایشان به حقوق همین شغل وابسته است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463506" target="_blank">📅 22:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463505">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0ZHvU7IeGLAfT66XLs66igehxljxZZVznsi8mtWfrK8KGpL2aZRDrtV7t2bASw5r9qDiqhRFm87V84aEcw6W1LUaXUF6grzaN1X8WUWY7EKAItAn6RCXc32sG6JURQgt6BGeBNfyynxYdgbY09-6wy-YI2LNNPt_USLvUk2yZSOUi77JCKUIddVypljpl8Ne0LlYIszPhrp3ZB7Q7LKqWdS6cgGPJHeKosuSOZokV05TwxIzYbYAGIUf8687C4ED5MHdS8E4u5g4tulKlQQGm91tUPPOwQONpYD4St99Wr6kM0Qw5paeEzEkFAn6NRPwq9RkWOQDQgbJ_CyIY62GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسیج: حضور مردم باعث همبستگی و تقویت روحیۀ رزمندگان است
🔹
هفتۀ دفاع مقدس، یادآور حماسه بزرگ ملت ایران در دفاع از تمامیت ارضی ایران و آرمان‌های انقلاب است.
🔹
ملت ایران با حرکت در مسیر رهبری آیت‌الله سیدمجتبی خامنه‌ای، مسیر عزت، پیشرفت و سربلندی را با هوشیاری دنبال خواهد کرد.
🔹
ملت مبعوث و بزرگ ایران، بیش از ۲۰۰ شب است که با حضور آگاهانۀ خود در میادین کشور، حمایت و پشتیبانی خود را از نظام اسلامی، رهبری و نیروهای مسلح به نمایش گذاشته است.
🔹
این حضور موجب تقویت روحیه رزمندگان و تجلی همبستگی و عزم ملی شده و  جلوه‌ای از همان روحیۀ دوران دفاع مقدس است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/463505" target="_blank">📅 22:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463504">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انفجار یک خودروی ارتش اسرائیل در نوار غزه
🔹
شبکه ۱۴ رژیم صهیونیستی: یک بستۀ انفجاری در خودروی متعلق به ارتش اسرائیل در شمال نوار غزه منفجر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463504" target="_blank">📅 22:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463503">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b1ff18b5.mp4?token=Wt5ePF38QT3djv6GSBbWui2cD2_0EdNR-jvdTYdyfHl7T5-e1f6sMEKGb0A2b_RWWEyAJ3kyT1tHvw_Mhjb4eZ4M_bZaofPximj6m6S4ZuHlCpipfm4aoIXpxvpR1UGV6cmwNuEzpSh9HZXCcYb_vkqFY3NOKq7vGztoMK_dsEbTnok9a89qYl5CZ1DJungGcVDt4j_YOB8Oosx_umCaN5T-rnhAPw_QXvEDuV3CGQw40OXNkQY3h8kiHSN0fTulYhPM2d9ONBIugzPSstimEL49BOn6zZ1wKMnF-S6Cj1I7zKTjHPZPThMOs_VsdwBLpRcLb8R7JYu2WD_a7vDcfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b1ff18b5.mp4?token=Wt5ePF38QT3djv6GSBbWui2cD2_0EdNR-jvdTYdyfHl7T5-e1f6sMEKGb0A2b_RWWEyAJ3kyT1tHvw_Mhjb4eZ4M_bZaofPximj6m6S4ZuHlCpipfm4aoIXpxvpR1UGV6cmwNuEzpSh9HZXCcYb_vkqFY3NOKq7vGztoMK_dsEbTnok9a89qYl5CZ1DJungGcVDt4j_YOB8Oosx_umCaN5T-rnhAPw_QXvEDuV3CGQw40OXNkQY3h8kiHSN0fTulYhPM2d9ONBIugzPSstimEL49BOn6zZ1wKMnF-S6Cj1I7zKTjHPZPThMOs_VsdwBLpRcLb8R7JYu2WD_a7vDcfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چراغ خیابان با حضور مردم در شب ۲۰۵ همچنان روشن است
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/463503" target="_blank">📅 22:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463502">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
خبرگزاری رسمی لبنان: رژیم صهیونیستی مناطقی در اطراف شهر صور را با چند بمب فسفری هدف حمله قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463502" target="_blank">📅 22:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463501">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e45ab4a5.mp4?token=MzhpmyWSjtOKwKaWnWmgaVqlAlkutZ2cmVczCil3nkT_alyF9HzMb6fwrF8LTW38BKhL7NGpJwy3Ai7xmkamBJvxtIutfyV3KwW8_yzE5E_V2GCSBMMq0orh8RrQao9cKTNkw3ZErSAEdAkh6HTDm7RGaekXe1XOp9gaBjemXmMe-FME3bfAJhswRoSaR6c_T08Cf5PQLVWhQCte0IN9xUG5jpNCw6kyFZRbelTGw7Jr1CNz48c2rAWrrr90U_rzr1h0X3PbD4tYR3dFgrgxoyQWjR-xgLOLaKIUGNvafklO7874OxDNbp5i2DXolu0kz7te30T5UUmtm6SJFk56ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e45ab4a5.mp4?token=MzhpmyWSjtOKwKaWnWmgaVqlAlkutZ2cmVczCil3nkT_alyF9HzMb6fwrF8LTW38BKhL7NGpJwy3Ai7xmkamBJvxtIutfyV3KwW8_yzE5E_V2GCSBMMq0orh8RrQao9cKTNkw3ZErSAEdAkh6HTDm7RGaekXe1XOp9gaBjemXmMe-FME3bfAJhswRoSaR6c_T08Cf5PQLVWhQCte0IN9xUG5jpNCw6kyFZRbelTGw7Jr1CNz48c2rAWrrr90U_rzr1h0X3PbD4tYR3dFgrgxoyQWjR-xgLOLaKIUGNvafklO7874OxDNbp5i2DXolu0kz7te30T5UUmtm6SJFk56ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۵ شب ایستادگی گنابادی‌ها برای وطن در شب رحلت حضرت معصومه (س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463501" target="_blank">📅 21:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463500">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1lUDB5-gp5VH6Nrkhjj2rb9_s_Ge4zwPSt2zMWJDTqlV7grk54OgMl9Fi_2h6aOTfzOpfJvkyZ8z-I4zeXROauban5Ds3B0tscZBpTXuKWCPskMNMEnVrsw_hP7DbgQOmfKu8Vzj1cZbpZK1oAkNTmgGWLa88kQx3IoJuKmQZCfiQKh4UCqulYM9z8vgEfUWlo9crmnueuhliTrkKeAXEbyORk7ETt8diSfkCi0p4CXHCE-Ir1CBOij-Y0IQlop3sm3QNG5Rp3WDwrG5-C7t44eQlc9JocrZwBIDf992m_kKvYPCC_Udf5Yc680G-42j_NNYGG0ZMjBO6rLL2AM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیابی کاربران برای گوگل گران تمام شد
🔹
رویترز: رگولاتور حفاظت از داده‌های ایرلند، گوگل را به دلیل نحوه پردازش و نگهداری داده‌های موقعیت مکانی کاربران به پرداخت ۴۰۳ میلیون یورو جریمه کرد؛ پرونده‌ای که به نقض مقررات حفاظت از داده‌های اتحادیه اروپا مربوط می‌شود.
🔹
کمیسیون حفاظت از داده‌های ایرلند اعلام کرد گوگل در فاصلهٔ سال‌های ۲۰۱۸ تا ۲۰۲۰، در ۳ قابلیت «فعالیت وب و برنامه‌ها»، «سابقه موقعیت مکانی» و «دقت موقعیت مکانی» الزامات مقررات عمومی حفاظت از داده‌ها (GDPR) را نقض کرده است.
🔹
این نهاد همچنین گوگل را موظف کرده ظرف ۶ ماه شیوه پردازش داده‌های موقعیت مکانی خود را با قوانین اتحادیه اروپا منطبق کند.
🔹
نحوهٔ عملکرد گوگل می‌توانست باعث شود کاربران از استفاده از موقعیت مکانی خود برای اهدافی مانند هدف‌گیری تبلیغات یا استنباط علایقشان آگاه نباشند و کنترل کمتری بر داده‌های شخصی خود داشته باشند.
🔹
این جریمه چهارمین جریمهٔ بزرگ کمیسیون حفاظت از داده‌های ایرلند از زمان اجرای GDPR در سال ۲۰۱۸ محسوب می‌شود و مجموع جریمه‌های این نهاد علیه شرکت‌های بزرگ فناوری از مرز ۴ میلیارد یورو عبور کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463500" target="_blank">📅 21:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463499">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سپاه پاسداران: آمریکا و اسرائیل دیر یا زود باید به خروج از منطقه تن بدهند
🔹
بیانیۀ سپاه به مناسبت هفتۀ دفاع مقدس: نیروهای مسلح با آمادگی کامل و هوشمندی راهبردی، دست بر ماشه آماده پاسخ‌های قاطع و ویرانگر به دشمن فرسوده و متجاوز هستند.
🔹
آمریکا و رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/463499" target="_blank">📅 21:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463498">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سپاه پاسداران: آمریکا و اسرائیل دیر یا زود باید به خروج از منطقه تن بدهند
🔹
بیانیۀ سپاه به مناسبت هفتۀ دفاع مقدس: نیروهای مسلح با آمادگی کامل و هوشمندی راهبردی، دست بر ماشه آماده پاسخ‌های قاطع و ویرانگر به دشمن فرسوده و متجاوز هستند.
🔹
آمریکا و رژیم صهیونیستی باید به منطقه عاری از وجود پلید و جنایتکارانه خود تن دهند.
🔹
نیروهای مسلح جمهوری اسلامی ایران با تکیه بر دانش بومی، نوآوری راهبردی و خوداتکایی دفاعی، به سطحی از اقتدار رسیده‌اند که هر تهدید را در مبدأ خنثی می‌کنند.
🔹
دشمن پس از ناکامی در عرصه نظامی، به جنگ‌های ترکیبی، شناختی، اقتصادی و رسانه‌ای روی آورده است؛ اما ملت ایران با اتکا به ظرفیت‌های درونی، اقتصاد مقاومتی و اتحاد مقدس ملی، هر توطئه‌ای را خنثی خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463498" target="_blank">📅 21:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463497">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/286a62c5b4.mp4?token=QLAS9Pjz3bDovBtoKySinjN91xeWJebt-xbX6TKjEp8uQxW4E4Mk_BxppYXOJrSUWGnn-YY7XMo_4OOffo-mpoVwYa6JPXZV5ijG54kT8gNfFSdGSyjD1EiX1M5vMCDFyv_Q0eNqitdjKcRgp623wCPaFmR46UefD-NIx4sUURqpDTEG1Hg98nMNuHYtweLezQESPSO_30bmCFNz6DC8x5FF0gzr-F474DG6y4tEYvu5rBAgmjmOTW02jW1HT8IguTtyZiI5YhDDYCEHg7ZsvtSVv5odIPIYBuzRqgymf0JwgKjhVzSmuwlB1qelAWj_rgMwweVmSdeo8Q8mVEG34A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/286a62c5b4.mp4?token=QLAS9Pjz3bDovBtoKySinjN91xeWJebt-xbX6TKjEp8uQxW4E4Mk_BxppYXOJrSUWGnn-YY7XMo_4OOffo-mpoVwYa6JPXZV5ijG54kT8gNfFSdGSyjD1EiX1M5vMCDFyv_Q0eNqitdjKcRgp623wCPaFmR46UefD-NIx4sUURqpDTEG1Hg98nMNuHYtweLezQESPSO_30bmCFNz6DC8x5FF0gzr-F474DG6y4tEYvu5rBAgmjmOTW02jW1HT8IguTtyZiI5YhDDYCEHg7ZsvtSVv5odIPIYBuzRqgymf0JwgKjhVzSmuwlB1qelAWj_rgMwweVmSdeo8Q8mVEG34A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبه‌های عزاداری وفات حضرت معصومه(س)  در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463497" target="_blank">📅 21:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463496">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ebe0de86.mp4?token=b7nSHMjOzlzk9GNJcftAEsunJaVCBqH6QPyK8Sf52aGBr7Qa9HCYhqasmTv6TIEKbZvrDNTJSlgnDV50oDi4sGE_YJjbWZ_hTq-T6-doNcpe9X0F3Gqdu5Ty83u9KPbqNMbQ7DZNE_1hH82QJKr0XyiVencluicj3cMVC-ZAH1bc-JYI4nj3IN6NsSYjs52TryyeNiWgScBIMM1o6tzBXsBNPFSiAaDe1EBCtn7LNQi-JRGUeE_67sPx5PFmyXP89K1UKgtYGBuzkx2C4LVBaDMOt3isbHcrbKsROEmqecTtTaOexfeUeGKdq4hKproWR45t1EbvQtvXFx2ho1rzPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ebe0de86.mp4?token=b7nSHMjOzlzk9GNJcftAEsunJaVCBqH6QPyK8Sf52aGBr7Qa9HCYhqasmTv6TIEKbZvrDNTJSlgnDV50oDi4sGE_YJjbWZ_hTq-T6-doNcpe9X0F3Gqdu5Ty83u9KPbqNMbQ7DZNE_1hH82QJKr0XyiVencluicj3cMVC-ZAH1bc-JYI4nj3IN6NsSYjs52TryyeNiWgScBIMM1o6tzBXsBNPFSiAaDe1EBCtn7LNQi-JRGUeE_67sPx5PFmyXP89K1UKgtYGBuzkx2C4LVBaDMOt3isbHcrbKsROEmqecTtTaOexfeUeGKdq4hKproWR45t1EbvQtvXFx2ho1rzPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی محل آموزش نظامی «جان‌فدا» در تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463496" target="_blank">📅 21:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463495">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787e477c67.mp4?token=jAUKzRwQDOXVmstbvY-cFtqlXwFLUkCbwDF-jeX8RVztrLiCpeO_TEgpYkQirhHHq-iO42xyls3C7BuS7NOCqST5fpqiGF6QvFnRnexiuqjrsO9m_0pO0BQlrWvlKOsIx7mlVLp7q2CUnnv8sH1-fZYIcl0OhQw820fCGs-1_LHAWTR3ZirrSB3qI8poOJO5RY5LPhwi2qkUjzaNxtxUaSgR1cfQNHMMiyntTY92ErkegvEBGrx4uK5t4pfaeo4XMDJoS8nRGmFa-14KAGKb6zm_i12FVMc9MkJsNFUZoiixn5WvJmfooXNfu2oKcoKanTP_DvnHve2JzXZw6DbK3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787e477c67.mp4?token=jAUKzRwQDOXVmstbvY-cFtqlXwFLUkCbwDF-jeX8RVztrLiCpeO_TEgpYkQirhHHq-iO42xyls3C7BuS7NOCqST5fpqiGF6QvFnRnexiuqjrsO9m_0pO0BQlrWvlKOsIx7mlVLp7q2CUnnv8sH1-fZYIcl0OhQw820fCGs-1_LHAWTR3ZirrSB3qI8poOJO5RY5LPhwi2qkUjzaNxtxUaSgR1cfQNHMMiyntTY92ErkegvEBGrx4uK5t4pfaeo4XMDJoS8nRGmFa-14KAGKb6zm_i12FVMc9MkJsNFUZoiixn5WvJmfooXNfu2oKcoKanTP_DvnHve2JzXZw6DbK3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قانون خوبه یا بد؟ بستگی داره کجای دنیا باشی!
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463495" target="_blank">📅 21:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463494">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/717a4fbd05.mp4?token=KudYMUa24kGJbttKhaR2f1K1U_YeqY_1uK7LKiq-Cq7Fdyq_zHwSdm47DbfY6BU7os788DUk7wEf2WqRTa1LeXH9JugemKC9_eaEQkAaqr_Or2GpHhHG2DaoZiFHkBxOb6VrU6sqsfsrTqQMMTHrA8lSmVdfx-y0F2Jk42f_lpZZ0V3OflRt0lc8bzEXjrIVWWk0w3WO0T4G49dFOgFmzXkgyRSDlr1oxunVxncVrtT8TSpOPJFjWoN2gVcMyGnmgapKj3214ze8Fs907WZWxjLd19Rzy2DXuOaQi1flf4dlIygOieoAsPfg2a9Kit7Vr97st1DLrMYtDzO-3_a9ymsJkogJPHP57qQbV9kuj9qVdqXQzhcLlNxYcSts4bEJl3sl3ew3K8IX8YsXWpMkPTJEHnINUD4gPlOjnSgDHo5J2SPt1nKxucziCyO26RqDJGJDlzVC8IylG1CprbVFxT2YMYcQdn3p9_bzpMrJFhdpsWItuQVXzg-z4itVQ0oAs6mdVbObC38nxI4yJy1HXxEzoQ6Ymz1iDxV2gByBm5fO4_OoSQX1d6INnr6rEDoVqi3oN_GR3_7ZJDMz40ogdFtad4DpsfW3nJR273F0Swf-No2sSOgnDkvhPHbHu4IWSkpq7kVZoNRKtNDKLu9gHJU8M0fNPweA8FeKpKRHcMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/717a4fbd05.mp4?token=KudYMUa24kGJbttKhaR2f1K1U_YeqY_1uK7LKiq-Cq7Fdyq_zHwSdm47DbfY6BU7os788DUk7wEf2WqRTa1LeXH9JugemKC9_eaEQkAaqr_Or2GpHhHG2DaoZiFHkBxOb6VrU6sqsfsrTqQMMTHrA8lSmVdfx-y0F2Jk42f_lpZZ0V3OflRt0lc8bzEXjrIVWWk0w3WO0T4G49dFOgFmzXkgyRSDlr1oxunVxncVrtT8TSpOPJFjWoN2gVcMyGnmgapKj3214ze8Fs907WZWxjLd19Rzy2DXuOaQi1flf4dlIygOieoAsPfg2a9Kit7Vr97st1DLrMYtDzO-3_a9ymsJkogJPHP57qQbV9kuj9qVdqXQzhcLlNxYcSts4bEJl3sl3ew3K8IX8YsXWpMkPTJEHnINUD4gPlOjnSgDHo5J2SPt1nKxucziCyO26RqDJGJDlzVC8IylG1CprbVFxT2YMYcQdn3p9_bzpMrJFhdpsWItuQVXzg-z4itVQ0oAs6mdVbObC38nxI4yJy1HXxEzoQ6Ymz1iDxV2gByBm5fO4_OoSQX1d6INnr6rEDoVqi3oN_GR3_7ZJDMz40ogdFtad4DpsfW3nJR273F0Swf-No2sSOgnDkvhPHbHu4IWSkpq7kVZoNRKtNDKLu9gHJU8M0fNPweA8FeKpKRHcMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماعات شبانه، حال‌وهوای اول مهر گرفت
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463494" target="_blank">📅 21:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463493">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOTxle3pE7fvOua1jmchHXLJnyYkuOkmN792FhVCEXiJJsztv7nq_2slW5S8vPLR-i0Tf7_5nG7KAtmHjmaWc-yu6Ex-hKCZLgPF1IK1DueknmrxTt9SQYruMOembAL8XQaGptNqZ3LzLETKrORXmqykI60-VazKDkZxuOda8QREx7w6PSP2_idBINHVroeSoDEzirmgbOM4jnw6y73UuBIHGcZwqmYB5S4cpRAt2pQ_RmcUVRi0uBAmc1zHdmwcZNLj6Ouxwb52FAwgtFwip2DtasC90g4WUUQt9sTzOlPpa38JsmJyT4OZEIEFccBHVXlHeX55PUY1_BvLa0pBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار با وزیر کشور پاکستان: ایران و پاکستان از قدرت‌های منطقه هستند
🔹
امیدواریم با توسعۀ سرمایه‌گذاری‌های مشترک و تسهیل همکاری‌های اقتصادی، شاهد تعمیق هرچه بیشتر روابط ایران و پاکستان باشیم.
🔹
اقدامات و فشارهای آمریکا، زمینه‌ساز افزایش هم‌گرایی و تعامل مستمر میان کشورهای اسلامی شده است.
🔹
ایران و پاکستان از کشورهای قدرتمند منطقه هستند و از ظرفیت‌های عظیم برخوردارند؛ اگر این ظرفیت‌ها را کنار هم قرار دهیم می‌توانیم بسیاری از نیازهای خود تامین کنیم.
🔹
تقوی، وزیر کشور پاکستان هم گفت: معتقدیم که روابط ایران و پاکستان هیچ‌گاه در چنین سطح بالایی که امروز شاهد آن هستیم، قرار نداشته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463493" target="_blank">📅 21:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463492">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34d716b53.mp4?token=jYv7HqlYCwoJX9NY8V5UcDciXn-hUDG3BAzwL0oh6TK4t5NXJ0Ntbo4YkKmExUGVPpREBAAIXBJx5blnzQ7mcl21RQbz0VB-YxLz7LNb7ftHF-20NAcb9SmSHgaMChhWwA5bwtgHgsmhRfvbviDZO14wF1MXMSjpp4e3PYoqCLbet59zVSTfsroUYnQpsS_JQI9JgFpsHhhEWUEDIg9o3L4MafKGXaxd4-pV2ibTEyHeMXqlpAfGkmFKiqRk1eyX5E0nb-sGFxvhWAo9OQqwn_fKxwKERz2O1Q13KGkcYsxZFZyTlWzNuIPe1gCOxPJELudMJAfVitpVnaux5tvUGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34d716b53.mp4?token=jYv7HqlYCwoJX9NY8V5UcDciXn-hUDG3BAzwL0oh6TK4t5NXJ0Ntbo4YkKmExUGVPpREBAAIXBJx5blnzQ7mcl21RQbz0VB-YxLz7LNb7ftHF-20NAcb9SmSHgaMChhWwA5bwtgHgsmhRfvbviDZO14wF1MXMSjpp4e3PYoqCLbet59zVSTfsroUYnQpsS_JQI9JgFpsHhhEWUEDIg9o3L4MafKGXaxd4-pV2ibTEyHeMXqlpAfGkmFKiqRk1eyX5E0nb-sGFxvhWAo9OQqwn_fKxwKERz2O1Q13KGkcYsxZFZyTlWzNuIPe1gCOxPJELudMJAfVitpVnaux5tvUGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیء ناشناخته نورانی دوباره بالای تهران دیده شد
🔹
یک شیء نورانی ناشناس شامگاه شب گذشته در آسمان تهران دیده شد و انتشار تصاویر آن در شبکه‌های اجتماعی، گمانه‌زنی‌هایی درباره ماهیت این شیء به راه انداخت.
🔹
پیگیری فارس از سازمان هواپیمایی کشوری درباره این مشاهده نشان می‌دهد که تاکنون پرواز مشخصی که بتوان آن را به این شیء نسبت داد، در رادارها مشاهده نشده و این سازمان دربارۀ ماهیت شیء نیز اظهارنظر مشخصی ندارد.
🖼
اما شاید برایتان جالب باشد که بدانید ۵۰ سال قبل هم اتفاق مشابهی در تهران رخ داده است
.
🔗
ماجرا را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/463492" target="_blank">📅 20:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463491">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCQXRihJ6SJZ9g7T-Qfhv-uvo-VH4ngZqy_e1yOTbTH-zTgUwUn_WsyDbNLaw7bj8XKMWl2INbp_sSOc0hqwIY5XggGyw2vv8XhMLdIeBSGReZBHJY5Os5_NALt4Znwpy7JUAJslf9Yj5Jwtpb1m4F4_OPPCm5P5GqvqXOGo1M1-2V23JfDlBotPu5J6pwjyPeT7UrPPtT_JulaTi4RDYFtDSFYC9ff2mlh_isRqHdKI5_Ur40IB5EM0kiK2GKvFkxbPEdb4tcQOPHdZCUGp8L_GIY3UT9N5slbieLZyDX7d4fENEB6yk2WGwT7QmMhTQ0JgBSeP_a1LC3EEC6pPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: از هیچ کشوری باج‌خواهی نمی‌کنیم
🔹
سخنگوی کاخ کرملین: روسیه هیچ تهدیدی برای فرانسه یا دیگر کشورهای اروپایی محسوب نمی‌شود و مسکو قصد تهدید یا باج‌خواهی از هیچ کشوری را ندارد.
🔹
پسکوف گفت: پوتین بارها تأکید کرده که روسیه، فرانسه یا هیچ کشور دیگری در اروپا را تهدید نمی‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/463491" target="_blank">📅 20:58 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
