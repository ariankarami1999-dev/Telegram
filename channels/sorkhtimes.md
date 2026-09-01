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
<img src="https://cdn4.telesco.pe/file/K8k_wOvr-ZHact7WsHMpuXkF-okP18UfCYn7D6FfxwnLhNBaqJ5EdKWN5aPiBuCvSki1kO_A1qoAzc82vOPLicdp0I_YApdEzUOPPxZe-qODm15wZIgXFhmXJu2E95TU1RjVa-P9Y7yCfCnmxniJ6nkPXhhewLET1HMl625GIKF4_eRLiiYkr_MP-aNM6ep4hIOtN7YJPtQ9xZvqC2tlNpIzhK8guGsya_dsQ2n-WAltld7q4F9sHnTgGcE1t2IJ5BtbPrJ5nwzbbXXYLD3dDIWwOzqred3j7RrDwUjIkA1Yc15LXnJG-0GVZ8U8N5zKvEFSBUq1qXgNGw4heyOCzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-139378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=hWYQFxBov_lRn5OoPtGetnk25nxSfIv9kvu67wjc-S9TAAvqU592w3Ubi9-SX7fhQeKVP_WZcoOec3tiBKfvAcEoxcM1CZyDyF_b2xWJfdpvwymnl_qArJThCQKOy3VeoUHGAv7MDhxeosOWH8hSleLLG0H8j9Up04J79suPYHYFyhyKCYqVdfPHtOgAeLnlIHnaXmTmFYAEGOBn2g6DXcjTN1MfMBSkjVul8ils_znAwtvDCiNeMRQdc-dvokN1C94Kck333zRBv0u3fpwn_weR5KVWbxhTq5QSIvGCtybFI-NSZtaFfAgg3ZWf8UbRqMSc389w86rURgk-ONU2-xRPjV3g0viGyD9LIwB5ms46owHPjvmCe7mM7BGlBPn_9MqUw6zx7pHkqPBUHpVs8CqplOrpnah_gNt3otg9_1hA1fyA0y4SN-0Sqii3216kaaENmCBTbzcA34cfK-AfboTu9MIvObrjj7imUFScxRcUolwwOSrweNhFJF5PH8tHzSXterc-0fzJ9UuvZJ6Qth15aRbCqgQXKLTva1Z5V0RXVfIiVZPCg3lC7hRCsnO4IQ5NNci4Dg2KpXAGnF058tuodA5sS_5qmJdqqPMRMlXKFO1rmNtRsfbVjBA38bRaDKKcrRFNLikNb94GI1Oz5tWcCGpcC24ljJSbpGdR18U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=hWYQFxBov_lRn5OoPtGetnk25nxSfIv9kvu67wjc-S9TAAvqU592w3Ubi9-SX7fhQeKVP_WZcoOec3tiBKfvAcEoxcM1CZyDyF_b2xWJfdpvwymnl_qArJThCQKOy3VeoUHGAv7MDhxeosOWH8hSleLLG0H8j9Up04J79suPYHYFyhyKCYqVdfPHtOgAeLnlIHnaXmTmFYAEGOBn2g6DXcjTN1MfMBSkjVul8ils_znAwtvDCiNeMRQdc-dvokN1C94Kck333zRBv0u3fpwn_weR5KVWbxhTq5QSIvGCtybFI-NSZtaFfAgg3ZWf8UbRqMSc389w86rURgk-ONU2-xRPjV3g0viGyD9LIwB5ms46owHPjvmCe7mM7BGlBPn_9MqUw6zx7pHkqPBUHpVs8CqplOrpnah_gNt3otg9_1hA1fyA0y4SN-0Sqii3216kaaENmCBTbzcA34cfK-AfboTu9MIvObrjj7imUFScxRcUolwwOSrweNhFJF5PH8tHzSXterc-0fzJ9UuvZJ6Qth15aRbCqgQXKLTva1Z5V0RXVfIiVZPCg3lC7hRCsnO4IQ5NNci4Dg2KpXAGnF058tuodA5sS_5qmJdqqPMRMlXKFO1rmNtRsfbVjBA38bRaDKKcrRFNLikNb94GI1Oz5tWcCGpcC24ljJSbpGdR18U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💣
⚽️
❤️
حمله شجاع خلیل زاده به عادل فردوسی پور: من دو سال است که فحش می‌خورم اما خم به ابرو نیوردم، فشارهای زیادی روی منه و خدا رو شاهد میگیرم که یزمانی می‌خواستم از فوتبال خداحافظی کنم اما این کار رو نجام ندادم، دو سال فحاشی به من شد و تمامی این فحش‌ها تقدیم به عادل فردوسی‌پور
🔻
همه مردم تبریز می‌دونن عادل فردوسی‌پور با تراکتور مشکل داره از زمان برنامه 90 همین بود، الان هم همین است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 428 · <a href="https://t.me/SorkhTimes/139378" target="_blank">📅 22:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
شنیده میشود که چندین بازیکن تراکتور به دلیل بدنسازی بد مصدوم شده اند و باشگاه تراکتور با تعطیلی لیگ به دلیل اردوی تیم ملی امید موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 731 · <a href="https://t.me/SorkhTimes/139377" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
✔️
شایعه شده که تارتار دوباره میخواد همون قمار از پیش باخته بازی تراکتور رو تکرار کنه و با یه مهاجم وارد بازی شه و عمری رو به جای سرگیف بازی بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/139376" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
سهراب بختیاری‌زاده: می‌خواهیم ریتم خوب شروع لیگ را ادامه دهیم و پرسپولیس حریف خوبی است که به امید خدا بتوانیم آن‌ها را شکست دهیم و با روحیه بالاتر راهی لیگ نخبگان شویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/139375" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
✔️
تراکتورسازی تا دقیقه ۷۷ نتونسته به شمس آذر گلی بزنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/139374" target="_blank">📅 21:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
شنیده میشود که چندین بازیکن تراکتور به دلیل بدنسازی بد مصدوم شده اند و باشگاه تراکتور با تعطیلی لیگ به دلیل اردوی تیم ملی امید موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/139373" target="_blank">📅 20:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
#فوری | شنیده شدن صدای چندین انفجار در شرق بندرعباس و اطراف قشم منشا صدا مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/139372" target="_blank">📅 20:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
صحبت‌های سهراب بختیاری‌زاده سرمربی استقلال در نشست خبری پیش از دربی:
🔻
دربی همیشه خاطره‌انگیز است و بازی‌ای است که در تاریخ برای بازیکنان ثبت می‌شود.
🔻
ما شاید موقعیت‌های بیشتر و بهتری نسبت به فولاد داشتیم ولی استفاده نکردیم ولی از بازیکنانم با توجه به شرایط…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/139371" target="_blank">📅 20:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
مهدی تارتار به کنفرانس مطبوعاتی نرسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/139370" target="_blank">📅 20:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
✔️
شایعه شده که تارتار دوباره میخواد همون قمار از پیش باخته بازی تراکتور رو تکرار کنه و با یه مهاجم وارد بازی شه و عمری رو به جای سرگیف بازی بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/139369" target="_blank">📅 20:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
فوری/حملات آمریکا شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/139368" target="_blank">📅 20:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔽
🔽
کانال ۱۲ اسرائیل: شماره معکوس حملات به ایران آغاز شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/139367" target="_blank">📅 20:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9DBUiCuHbnqVjro8AFhKww3EqmYKnkkP5uBc0svEacjlMl--rDSQi-Y8W0DTqBwMjp1zDr_zE5Xr4ZGhGOCjaTvrNHN2r1UC-tdGN_x_vzTzOkl8rh_wsDHCOSH1Be7s0-IGl7ZzbTqnMNWJjpcoBT4YZFxB30QNo1vCcIgaozYFW-aIBndJzCKLVKOZn2luGlLRH8oUWC884H5-p5d2xrBsWzdsmJxTlII6PMe-vWvpDPqOK1lEz-w2p_ehUk0R9HcpoB_Z0WPq8YCcAe2Twuycqvyuom42u6H4IEDe7sN0v5x6DHa0c2REcAijlNEPf2DpQZp9aVF_r7ytHOHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
نبردی برای صدرنشینی!
⚽️
الهلال و الاهلی؛ جدال غول‌های عربستان
سه امتیاز، هدف مشترک دو مدعی.
[
الهلال
⚽️
🆚
⚽️
الاهلی
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/139366" target="_blank">📅 19:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
تصاویری از آخرین تمرین پرسپولیس پیش از دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes   ﻿</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/139365" target="_blank">📅 18:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
با اعلام کمیته انضباطی قرارداد یاسر آسانی با استقلال قانونی است و مشکلی برای همراهی این تیم ندارد
✔️
البته خب انتظار دیگه ای هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/139364" target="_blank">📅 18:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE2ewwMtKiPt7DPc_Vb-bcThfIB433MDE2uDw8CXJsx9efqYn1wWbBZYY-KvFtH2QU36nCpyKw9HMV02o2PC6ZcjJtDCUKEPmgfpTqId2gYbBUmzUb1pIJZIfegWYRaOkb9RC6fp2SR2eo-jA-PBXAKY7izGPDDZbkJtMjJ0EtPCso4qbPTj0eraCMKTrr6wUdj_AiAaDlkqnhUAdzmcXIPXmZ2s6N7tzqWy0dNz29iCv5MeyNH-pM8Exv8Cgxxjftlg6nZa_TN66PaeKiUjU1e-rwrgH5J6w_qk8BCi-tsyv9N3nwcFiL0rINXko3wU7DvKQvvzNBW5mSHnaLl_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از آخرین تمرین پرسپولیس پیش از دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/139363" target="_blank">📅 17:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rj8hXTpHFDO7JXhlFUg4tDufKF9NykrUemVewCLU-RuA0iXYQpPG1GYXoJrDmo-DXON3Qv1n77mG7zUw8uSOb5EMCvjHYbz0_CN091u4SwHRlp6jwMNdFMhYBHDQyaDdvtj2EiPkfIYP-aE2SnPE8ZJ5p_24BAalkyenIPJ_pt7GAxbCGp0R_wuvr0MVLLOXiHaHUgC9PH2opPZMGY1rfz9AU1s_G6T5m7qf2JM8mBpJhvUYcgKrUzSYhWgfZYvxCPB0MN5rsm9UOgsGcA5LkXXNhja2JnoSWtCrQW8xPJycCsU6vCt10fXmYdcBtVAjSTxv7EtpdasyHR8kjc4ybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
کاروان پرسپولیس راهی اصفهان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/139362" target="_blank">📅 17:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139361">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
کاروان استقلال با تاخیر به اصفهان می‌رود
⏺
پیش‌تر قرار بود کاروان استقلال همزمان با پرسپولیس و ساعت ۱۶ با پروازی اختصاصی پایتخت را به مقصد اصفهان برای برگزاری دربی صد و هفتم تهران ترک کند.
⏺
با این وجود به دلیل همزمانی حضور تیم‌ها در فرودگاه و رو‌به‌رو…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/139361" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139360">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
تیم داوری دربی ۱۰۷:
⚪️
داور: موعود بنیادی‌فرد
⚪️
کمک‌داوران: علیرضا ایلدروم، بهمن عبداللهی
⚪️
داور چهارم: سیدرضا مهدوی
⚪️
ناظر: اسماعیل صفیری
⚪️
داور VAR: میثم حیدری
⚪️
کمک VAR: علی احمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/139360" target="_blank">📅 16:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139359">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139359" target="_blank">📅 16:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139358">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
❌
💢
💢
💢
گفته میشه تارتار قصد داره ترکیب پرسپولیس مقابل استقلال رو بازهم تغییر بده و عمری برای مهار آسانی بجای سرگیف وارد ترکیب بشه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139358" target="_blank">📅 14:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139357">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن جانشان را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139357" target="_blank">📅 14:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139356">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
هفته هفتم لیگ برتر فوتبال ایران به دلیل اصرار بر اعزام تیم ملی امید به بازی‌های آسیایی ناگویا و تداخل برنامه‌های اردویی این تیم با مسابقات باشگاهی، در آستانه لغو قرار گرفته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139356" target="_blank">📅 14:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139355">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzP5SJcDWvP5-vuNjb9NXJpz-eoIW2TZWFNGpR54cIc9nIJA_Ij9t7HmS7CMA1W9A__5SGaYKG1EPg1Fu8Kq4S8SRx-o2FUN3Q7yYHgz332sFu21vR69XmMA9CvlM50Ie5Xd3e3xYFGmG5pL7O267_Pub-VXMI55LU8oycWUy3fIyVx9E6cRCLX4nAX_iPEAQsl0YzVQl3yIZkNH6XeeuovBYkoT3ag7KyP15u50WqDYxnP81kmJAAYRXvGhAlRnc0EMXJGCeCBecC5OoHaMXao9Djxdi9LI4C1rmKw_vw013-3aoPJJuZ9N39OL-xNIAf3Aum7xK3qXmqtcr9NenQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبردی برای سه امتیاز در قزوین!
⚽️
تراکتور با انگیزه‌ی برد به مصاف شمس‌آذر می‌رود؛
یک بازی سخت، حساس و تماشایی در انتظار دو تیم!
[
شمس‌آذر
🟢
🆚
🔴
تراکتور
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139355" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139354">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
گویا هفته هفتم لیگ برتر بخاطر مسابقات تیم ملی امید لغو شد
❌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/139354" target="_blank">📅 12:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139353">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووری
❌
احتمال تعطیلی لیگ ایران بعد از بازی دربی وجود داره. علتش هم برگزاری اردوی تیم ملی فوتبال امید هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139353" target="_blank">📅 12:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139352">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
تا کنون حدود 40 هزار بلیط برای بازی دربی فروخته شده و ظرفیت فروش پر شده اما احتمالش وجود داره‌ بازهم چند هزار بلیط دیگه شارژ بشه؛ ظرفیت کلی ورزشگاه نقش‌جهان 75 هزار نفر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139352" target="_blank">📅 12:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139351">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
رسول باختر کارشناس حقوقی: یاسر آسانی بازیکن غیر مجاز است و دیدار استقلال و مس شهر بابک سه بر صفر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139351" target="_blank">📅 12:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139350">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139350" target="_blank">📅 12:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139349">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووری
❌
احتمال تعطیلی لیگ ایران بعد از بازی دربی وجود داره. علتش هم برگزاری اردوی تیم ملی فوتبال امید هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139349" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139348">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
☄️
تماس تلفنی پیام صادقیان با پدیده ۲۰ ساله پرسپولیس
✔️
✔️
ستاره تکنیکی و سابق پرسپولیس قبل و بعد از پیروزی شاگردان مهدی تارتار با امیرحسین محمودی جوان گفت و گو کرد.
✔️
✔️
گویا پیام صادقیان، پدیده 20 ساله پرسپولیس را دعوت به آرامش کرده و از او خواسته است…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139348" target="_blank">📅 11:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139347">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139347" target="_blank">📅 09:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139346">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
🎙
سامان آقازمانی، بازیکن پیشین پرسپولیس:
‼️
اصلا دوست نداشتم جای بازیکنان تیم ملی باشم. راست بری، با دولت درگیری. چپ بری با مردم درگیری. بی‌طرف هم بخوای باشی بهت تخم‌مرغ میزنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139346" target="_blank">📅 09:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139345">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
فووووووووووووری
✅
شنیده می‌شود سازمان لیگ تنها مجوز فروش 70 هزار بلیط برای دربی داده است! ظرفیت ورزشگاه نقش جهان اصفهان 75 هزار نفری است...!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139345" target="_blank">📅 08:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139344">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139344" target="_blank">📅 08:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139343">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds-sTY--G6XzFzaMzfummh9TJ9cf1YqTytTSlHk9666c5vEQVGfHAI-tC5p_vNv3q75k4hvGqjUfQLabVNdnxKab7LzTuZ8pizLVeDLpWsgv9f-Te0xVMPSwmUTJON06_SmCE-Rr9zfBJso4gbXbmG2m-DqTtoUUBn_YqNdnzPMJYndZ6t96gjfkBma-shRUKSrRp4eB5LF4ZyxuyeF0sAn7KMmu-4kihu9mf4pUWgEcrl21mx09UZ4vqU-4sdzcmaBJZa5SQG7ISZDuHPq-miixnSJUfPglvmo3Rb5azIHkvx8HW8gdTyl5W-qKHM9vEzR5Dfjr_hWO-RetNGnzaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139343" target="_blank">📅 08:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139342">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtUK5XvALNT5MGpBWxKLSFd7ZeVh3arzhlNlB_0LfFFKXC_mfNYhbN_-xxpWkJ4XV-ACnJ9V9fGyun-cQqeD-nFh8SRO7AbDL1H0N2m15ETBqVdhYuDVRRGvaVrMDXh33tgZUpz5k8HJF4aZ6FPhIKmQxKRcfC9aiNGvt59b0dKbGuowgVZ6r_WzGdW2AjVT8DkEL1n8I9HxLzGyU8C5clOfeleYNDeK3BlYWo6WAqH_OAMj0WydQQiv8rAUkuPydOQNJFLIOSb6RelKdseLZs2pctV9M6-I7YWeAHmMgb7n2GdzNnHnLEr0jP1eAvNGg8OUggOO5tETUVgsDp0awQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
بن شلتون
🆚
خریکسپور
🎾
تیافو
🆚
مارتین دام
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139342" target="_blank">📅 02:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139341">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: فوتبالیست‌های ایرانی قلیان می‌کشند
✔️
✔️
چرا باید دروغ بگویم؟ بازیکنان ایرانی قلیان می‌کشند. قطعا فوتبالیست حرفه‌ای نباید این کار را انجام بدهد اما متاسفانه این موضوعات وجود دارد. در ترکیه چیزهای بدتر از قلیان می‌کشیدند
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139341" target="_blank">📅 01:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139340">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: حضور من در ورزشگاه شهر قدس خیلی حس خوبی بود/ دوست داشتم لباس عوض کنم و به زمین بروم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139340" target="_blank">📅 01:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139339">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
پیام صادقیان: حرفه‌ای ترین دوران فوتبالم ترکیه بود اما زیر تمرینات پرفشار آنها بدنم دیگر جواب نداد و فوتبال را در ۲۷ سالگی کنار گذاشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139339" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139338">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: بهم گفتن سایت شرطبندی که میزنی قانونیه مثل نیمار و فوتبالیست های بزرگ و اسپانسرش هستند و نمیدونستم قانونی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139338" target="_blank">📅 00:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139337">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
پیام صادقیان:
❌
شرط‌بندی هر نوعش تهش باخته و فقط شما می‌بازید؛ من اشتباه کردم و همینجا میگم پشیمونم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139337" target="_blank">📅 00:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139336">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
صادقیان : شرط بندی تهش باخته و سرابه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139336" target="_blank">📅 00:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139335">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: با محسن مسلمان تو تیم ملی زیر 10 سال با هم بودیم بعد هم در پرسپولیس و تیم ملی با هم بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139335" target="_blank">📅 00:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139334">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
ورزش‌سه: در تمرین امروز تارتار به سبک بازی با تراکتور بازی با ۳ هافبک و ۳ مهاجم رو تست کرده که مثلث خط حمله رو علیپور ، بیفوما و محبی تشکیل میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139334" target="_blank">📅 00:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139333">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
پیام اومده فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139333" target="_blank">📅 00:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139332">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139332" target="_blank">📅 00:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139331">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcdef74da.mp4?token=ddKgR4TrhTU3NvMGRSBjCpMPIqrrdTpmO05Yt_CqiLQsq28rZ_Q3MuWAEA5ZbO8qYfeRCB1ID553WTQws6EfGxPGz1h5DMRtuOsahUIqozc2DpBtAeHRvSfsCof-I1-xd1cHSeh8Btt1N6mQ34XEn2i1hIuZUmLDmC0rJOpg-ORK7GKDAI86lHp3HfPCC_Wei5xnSHdso3otosg-0iNg3ljSR5Wpofyst3qRhRlCLX28NJwVGCAVfg7xmhVMJxjTlTql6YllJRL0MARKuH0Mz2hW0840hFZuA4lc00G_ht2se8e7niBSpvLF-yUdP023HU8HiRojYhaIHnygt6ZB-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcdef74da.mp4?token=ddKgR4TrhTU3NvMGRSBjCpMPIqrrdTpmO05Yt_CqiLQsq28rZ_Q3MuWAEA5ZbO8qYfeRCB1ID553WTQws6EfGxPGz1h5DMRtuOsahUIqozc2DpBtAeHRvSfsCof-I1-xd1cHSeh8Btt1N6mQ34XEn2i1hIuZUmLDmC0rJOpg-ORK7GKDAI86lHp3HfPCC_Wei5xnSHdso3otosg-0iNg3ljSR5Wpofyst3qRhRlCLX28NJwVGCAVfg7xmhVMJxjTlTql6YllJRL0MARKuH0Mz2hW0840hFZuA4lc00G_ht2se8e7niBSpvLF-yUdP023HU8HiRojYhaIHnygt6ZB-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
عادل فردوسی پور: با دیدن فوتبال ایران میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139331" target="_blank">📅 23:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139330">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139330" target="_blank">📅 23:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139329">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❤️
❤️
اورونوف در تمرین آماده بوده اما وضعیت جسمانیش همچنان بهش اجازه نمیده که ۹۰ دقیقه بازی کنه و قراره نیمه‌ی دوم به بازی بیاد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139329" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139328">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
‏ ترامپ به شبکه فاکس نیوز: ما امشب به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139328" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139327">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❤️
❤️
10 دربی بدون شکست برای کاپیتان
✅
حسین کنعانی در آستانه یازدهمین حضور خود در شهرآورد پایتخت قرار دارد؛ کاپیتان سرخ‌ها در 10 دربی گذشته که به میدان رفته، هرگز شکست نخورده است. او حالا به دنبال حفظ این رکورد ارزشمند در یازدهمین شهرآورد خود است.
✅
پیش از کنعانی نیز کاپیتان دیگر سرخ‌ها یعنی امید عالیشاه که امسال از جمع تیم جدا شد. با ثبت 18 دربی بدون شکست، یکی از ماندگارترین رکوردهای سرخپوشان در تاریخ این رقابت را به نام خود ثبت کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139327" target="_blank">📅 22:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139326">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139326" target="_blank">📅 22:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139325">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a89afdca4.mp4?token=nBr7fW8MocnRtFEUMzpVMQ6bbAGAvZHvyUdS3NlGXm7QB9uSJBFqVAIc6PrC6jPYhUcjK4JSt49IGnFR9HKEUZtgabnhgHrunDedRRlZ1-oB-2UmognHd__hiptamWq6Dmo49M6Nd5hwAb0r6k05_q6q7yljxaqtJODkUzrboSk5rjqbzQg9buOE_JD3lHHmLhNZ6ha52t3K9yHkO5frrUDyvn4LOuc8mCf5ac2kJlCDw_EUJYEbxkxyMX62b9b9VkXKVIJFeUoN7Ixx7-25rxafLX4aTeImi7xU_kCc4FpccRT5F4upxlwJSk-MUxl9pXfF3u7tbM9EQvgccysOsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a89afdca4.mp4?token=nBr7fW8MocnRtFEUMzpVMQ6bbAGAvZHvyUdS3NlGXm7QB9uSJBFqVAIc6PrC6jPYhUcjK4JSt49IGnFR9HKEUZtgabnhgHrunDedRRlZ1-oB-2UmognHd__hiptamWq6Dmo49M6Nd5hwAb0r6k05_q6q7yljxaqtJODkUzrboSk5rjqbzQg9buOE_JD3lHHmLhNZ6ha52t3K9yHkO5frrUDyvn4LOuc8mCf5ac2kJlCDw_EUJYEbxkxyMX62b9b9VkXKVIJFeUoN7Ixx7-25rxafLX4aTeImi7xU_kCc4FpccRT5F4upxlwJSk-MUxl9pXfF3u7tbM9EQvgccysOsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی تو لیگ دو روسیه‌ با پرتاب اوت پاس گل داد و پشمای گزارشگر به این شکل ریخت
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139325" target="_blank">📅 22:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139324">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
تأیید پارگی رباط صلیبی «مهدی ترابی» بعد از MRI اول، در انتظار نتیجه معاینه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139324" target="_blank">📅 22:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139323">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeoQhDjGkp5SCaGQsCRGTwoEGWL13CpzKluQlghE8zoHaaV09wpRZBiGFjOxxBWhwIbUubJajDvS12ADz66nJh0n5SEszoN2EuoGgBHUWPuU0-06THQkE0wL5-MO5401vxkGWeu5LBeMiwLx4K3h0HHFtJZvqEibIGN91TzhdPm4tm7BixZYxH1TSWTu_7-nEXGuRPYMliwoetvsRarXqgsqskDzpPrRRV0b9n6A3qGIg9hqp3nV_a9DLrMVC8lc9aczhO-3RvK6ynW-F6jSBOPWiZkuNCOrAActS__Vp4sJoiFelEoa4DizgPSPf9TiMMnv8vVD-5zZfLAlMqQD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139323" target="_blank">📅 22:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139322">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139322" target="_blank">📅 21:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139321">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
اسپورت عراق؛ یحیی گل محمدی داره با سپاهان مذاکره می‌کنه، اون اصلا حواسش به تیمش دهوک نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139321" target="_blank">📅 21:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139320">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
✔️
جلالی مصدومیتش تموم شده و از دیروز به تمرینات گروهی اضافه شده
❌
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139320" target="_blank">📅 21:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139319">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🔴
بلیت‌فروشی دربی پایتخت آغاز شد  هواداران عزیز از طریق لینک زیر برای خرید بلیت اقدام کنید تا روز چهارشنبه ورزشگاه در دست ارتش سرخ باشه
❤️
https://ticket.sepahansc.com
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139319" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139318">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oA3i--oWTVMdIlVA8WVhjHaiZ0ZBjLRsaWevNWf4lraOKsJTIzD_Umz8zi34lJU7MpBuN9ZcUWueJZsyans_EYDP96KNKc-5K-7DK7uQz92rJOaolXbavnE3agZVmkePYsVHmyWOBikaPs7iUNhgaBBK8zKKWUw9xXZWhtu8p5kPJpBenUJJHjZuXgbAFF3UFVTmixyCaTGpLWHWEt8WPTFwg-hz7PgIlTAjXEEmyeXJ2f2zLYQXBV7_2RavNsX2jcrJpQPYZpiv19m-nJS8y0OkDAscQkczFZZfVoHrtSY9IRXqM2nvfM8HzIoXc7dMj1T9hU955TUEiMlC3ji6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139318" target="_blank">📅 21:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139317">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4_FJ6ppZWnOeCUj0i-C69TF162yI48fyQ4t475yozxYJn6u3vReKbJH-Ddr5-0rmfFoEKGRYpOnRjnPCf5nNJdeUKUKa-B7IIYjknUSp3CSkx7j7jmoFqrJqRXZ1MZv0iEjoemUYS61v1It9dU8rgW-Xtytv-VSYFitqD6sJI7wsFzi7yAyQI4K-L4iz2yGeXNMZ5XO-KI4VBvDIAcXX7K_qIHbvdHe_IY6cHWwnMz7f2qDL1Q4tmx9Ofvo7RWeTkLqEOH4dC778z1ev9vXQI6CSxYnKSACTTbrTjPkvpvPgt6FphEg_0TMLW-x_depy2QDLj45ZHpZF4W3AOtk4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بلیت‌فروشی دربی پایتخت آغاز شد
هواداران عزیز از طریق لینک زیر برای خرید بلیت اقدام کنید تا روز چهارشنبه ورزشگاه در دست ارتش سرخ باشه
❤️
https://ticket.sepahansc.com
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139317" target="_blank">📅 21:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139316">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZWRPLn-QBr142O50lQPZ7O7hZMAFx7VLcAUJe0lSFOwCBZ4C7Yb8uB98OkkWaMdMH1H4bdcgFH5FlYo3pMBXLnIP8WCKEW4XN1ih6Wqn_fL4eZ8tzkCOHiwRJq1RTRZGh3AofZw_gcv304bovvct8sdIIU_CIz8TAX9m0MpJ_uXov7sj_1RQfEhC2g4WndRB4o9CzHUfqu2IKEfnMW0Q99plCS3hv6hIOZc6BiIZUAvKWlog17-q2tyttySHdHO6lajGI6uc_Vwf9ZQVoiOs9U0ruZy8iTKu06Zhk2KWVWZpLDrIqmfML00zCiNIQ6GFhw4SjkbvSEoH-wEh-GZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بارسا به دنبال ادامه مسیر بردها!
⚽️
رایووایکانو آمده تا کار را برای کاتالان‌ها سخت کند؛ نبردی برای صدرنشینی جایی برای لغزش نیست!
[
بارسلونا
🔵
🆚
🔴
رایووایکانو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139316" target="_blank">📅 20:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139315">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
اردوی تیم ملی امید تعطیل شد و کسی بازیکن نداد و سه ستاره‌ی پرسپولیس به دربی میرسن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139315" target="_blank">📅 20:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139314">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
احتمال زیاد پرسپولیس با ۲ مهاجم بازی میکنه و بیفوما هم وینگر چپ هس تا پرسپولیس تو حملات با توجه به ۳ دفاعه بودن استقلال کمبود نفرات نداشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139314" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139313">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
کامنت کریستیانو رونالدو برای مسی:«لئو، توی این روزهای سخت، یه بغل خیلی بزرگ برای تو و عزیزانت میفرستم. خیلی قوی باشین.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139313" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139312">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139312" target="_blank">📅 18:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139311">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
✔️
جلالی مصدومیتش تموم شده و از دیروز به تمرینات گروهی اضافه شده
❌
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/139311" target="_blank">📅 15:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139310">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
تارتار نمی‌خواد ریسک کنه!
✅
به احتمال خیلی زیاد جلالی در دربی به میدان نمی‌ره و تیکدری مثل بازی‌های قبل در پست دفاع چپ پرسپولیس قرار خواهد گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/139310" target="_blank">📅 15:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139309">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
فوری؛ هدایت ممبینی برکنار شد و با حکم مهدی تاج، حامد مومنی به عنوان سرپرست دبیرکلی منصوب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139309" target="_blank">📅 15:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139308">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139308" target="_blank">📅 15:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139307">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🤩
پیمان حدادی: وظیفه تلویزیون اینترنتی باشگاه، بازتاب صدای هواداران و پیگیری مطالبات آنهاست؛ رسانه‌ای که باید تریبون هواداران باشد و خواسته‌های آنان را به گوش مسئولان برساند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139307" target="_blank">📅 15:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139306">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieqp_nbGvrFNJBmHL95SwMsIEIdBxwYTBuZJOGEInZxQrc-MHlXNlH6wkIz1eByMflhuP6I30tFrh5JnSu9jpWlAraMKUZC8WD2i9es_aot2jI5jPqwvAgJA-sk-5SPllgwntZtZu7Qajljf2rkNwHnV7_Vl2QVxhkSlc8yh5xR4phe2PV7cPGV_YCEqM8f2VUEIDyzbCBNBuW7yibyUUdTTFroWBqzAt4HEUK0VtWKTX8l-6_1e7AonWptr9wXj43wegWBGApYpEl4ZhLRqvhI2fE8yxF564w3D7k_XlM0eBwYE1AVaIXD2qD3JpA8SPFAnbZANN5lrjjtMbnVhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
ویلا پارک آماده یک شبِ آتشین
🔥
استون‌ویلا و آرسنال؛ جدال قدرت و جاه‌طلبی
اینجا هر اشتباه می‌تونه بهای سنگینی داشته باشه!
[
استون‌ویلا
🔴
🆚
🔴
آرسنال
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/139306" target="_blank">📅 14:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139305">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
حدادی قول داده فردا صبح پاداش پیروزی مقابل ملوان رو بریزه به حساب بازیکنا تا قبل دربی انرژی بگیرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/139305" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139304">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
‼️
بلیت فروشی عصر امروز شروع میشه که ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به صورت ۵۰ ۵۰ بین هوادارای دو تیم تقسیم میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/139304" target="_blank">📅 10:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139303">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووووووری
🔄
🔄
با اعلام باشگاه استقلال بلیط فروشی دربی از ظهر امروز آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/139303" target="_blank">📅 10:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139302">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
بلیط فروشی دیدار پرسپولیس و استقلال خوزستان شروع شد . از طریق لینک زیر میتونید برای خرید بلیط اقدام کنید   https://footballeticket.ir/buy-ticket.zul;jsessionid=23B55854CCBC6E89F276AA81C2DC01A1#  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/139302" target="_blank">📅 10:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139301">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
ممبینی : به عنوان دبیر کل فدراسیون فوتبال تا الان نمی دانم چه کسی گفته است که تورنمنت سه جانبه برگزار شود/  هیچ کسی هم نمی گوید که من گفتم و اصلا نامه ای هم در این زمینه وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/139301" target="_blank">📅 10:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139300">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAXKZOroOq0YzXZ_kH3zXcnI71s6qMEJNSEkss6mEZ3UKF7J06iMTAqHUIk8d3i7YgTCxd9aTMy-2zEXHkznFGod33Kn11GdjwKBo9x8KioMkUoEXIhZMu7p3N1gOjyVL-WA-n1bm0HGKo-U-UMHBMdLQE9eqsiLHTWPQCNUwLVWnRlueNxU-SnhuCPaKx7-G43J72uaY9izlPRrcE0yYt15NsextzBYju_-I2VnLjDO8uA1ubItgHtmC-fjzwLYLiiYeCXfqrOfB6t2VPCRiDHfqQoT3qvUuW-M9etQnATsn8RrQYkF9KxfkUeNa0r872rP7fhusUYF09TOhkv9jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسپورت عراق؛ یحیی گل محمدی داره با سپاهان مذاکره می‌کنه، اون اصلا حواسش به تیمش دهوک نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/139300" target="_blank">📅 10:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139299">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🏅
هوادار همین سبکو میخواد آقا تارتار تیمی بدون ترس و سراسر هجومی تیمی که می‌تونست امشب خیلی راحت بالا 5 تا هم گل بزنه
⏺
خداشکر با روحیه بالا سراغ دربی رفتیم و امیدوارم تو دربی هم همینطور و همین سبک رو ارائه بدیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139299" target="_blank">📅 10:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139298">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
از هتل المپیک خبر رسیده است مهدی ترابی ستاره تراکتور به علت مصدومیت ادامه فصل را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139298" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139297">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
چند دقیقه پیش تهران لرزید کیا حس کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/139297" target="_blank">📅 08:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139296">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/139296" target="_blank">📅 08:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139295">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ..
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/139295" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139294">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDivFHFo2j_r9gI8WDMFQBUj29LMiur_Zvf0a8Lut8UlgVYsoSrCDOl7xqRJoSQlr06sfu85rvja7Gj1P-JMykyqdo8DZGE7tMWbGMx3FAwnICxupVHk2R5O_ejIFDv5gGhBEc2YRq38yZfpYvQMEBXs9SW1igREcHYa6SWgOCPEDPpJZb9-qKCBLuZClFeKC5z9i9BvmvpbnW8oYP8u2oSpauGRYK6jvgJaQAPceJvruDS5MMeXBVlCkzlA05FzgqPYP-A28OAMWtPczxYgRM0pr0dJxBBx-Qag-Trk_zEKCb8pYr6i-uPx3k6P07nDWwI-VDc8WBx_diCSxv-p_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک شروع شد!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/139294" target="_blank">📅 02:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139293">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
سپاه پاسداران انقلاب اسلامی :
🔴
🔴
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/139293" target="_blank">📅 01:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139292">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
قیمت دلار برای اولین بار در تاریخ به ۲۰۶ هزار تومان رسید  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/139292" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139291">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/139291" target="_blank">📅 01:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139289">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
درگیری ها بین ایران و آمریکا دوباره بالا گرفته و درصورت تشدید تنش، احتمال لغو دربی زیاده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139289" target="_blank">📅 01:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139288">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">💢
💢
💢
احتمالا دربی پایتخت لغو خواهد شد .
🟥
چون پرواز ها فعلا لغو شده
‼️
گفته میشه در صورت تداوم شلیک موشک ها از سمت آمریکا و ایران هفته پنجم لیگ برتر ایران به تعویق خواهد افتاد.این تعویق شامل دربی هم خواهد بود
⏺
همه چیز تا فردا شب مشخص میشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139288" target="_blank">📅 00:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139287">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">💢
💢
💢
احتمالا دربی پایتخت لغو خواهد شد .
🟥
چون پرواز ها فعلا لغو شده
‼️
گفته میشه در صورت تداوم شلیک موشک ها از سمت آمریکا و ایران هفته پنجم لیگ برتر ایران به تعویق خواهد افتاد.این تعویق شامل دربی هم خواهد بود
⏺
همه چیز تا فردا شب مشخص میشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139287" target="_blank">📅 00:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139286">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🎙
🎙
تمامی پرواز های کشور از جمله فرودگاه مهرآباد تا ساعت 6 صبح فردا لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/139286" target="_blank">📅 00:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139285">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
فرودگاه مهراباد بعد درگیری ها تا اطلاع ثانوی و معنوی تعطیل شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139285" target="_blank">📅 00:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139284">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERDdFipMxrebZMktxgtZFLt9N6-uA6P5-kBkAFPoDI-p0lRpsBoscw28koYcXhlx_PiCD0pomATbcu2FxaZt9c5vAfstRp9_rXXlz2Bs_r7IC_z4xkQArTfuLjyxP1gieT_aYtxitBraE3zy80kpV09I0EKnw2AM9MqIbL9UwyC-ceNPsxgiPd95iC7ITnin6ec1CS4pnzLDoxZfUMdiMWhPqUB5KF0J0OA0K738jtAS21wjkYbm1qiTLe2nPUl5MGuAzLUVoKa6yGtDVm6AXigYwu8dBS88KDeMAu4bnAGNEFhJlXX5Uh3uv2jlgcCePgFjqJbeBZmDVxKSXXoHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
فوری، با تصمیم تارتار و موافقت علیپور؛ محمدحسین کنعانی زادگان بعنوان پنالتی زن اول پرسپولیس در دربی انتخاب ش
د
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139284" target="_blank">📅 00:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139283">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_Weex3K7yhNC-GjfyokhC8ZAQ7x2GPw5hbig7tQ56aO02o4NTYuQ42vqgLZr7RtpjBLwv4hJEbv_H4HNxnU85gOImEB_Oa89LsXhutH5ohEg0E_SEdqMXNJLkE0qwqMdVH0_RRgPbJvh1H5Li00S-keKcRXB9zjQtNleS8q0QH-WWv65-wWFXuOmOLAkbi004emy3g8cdM9C-5ZgAr5T3g4zmwqXvKgYdUgLqX0gRRfp-5-2ilQQ5bJCfybNsgoHWhpj8wQ3AxTfzuVV3RgTYV_Ne4vPS4i0Xj-NAjpWS-ngLFwTYDRXTkzhKHqEev2lxG97g4DMVEEC3ZEpAw9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139283" target="_blank">📅 00:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139282">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139282" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139281">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🟥
حاتمی: پرسپولیس در این فصل تیم خوبی است
❌
دربی‌ای که در ورزشگاه آزادی با نتیجه یک بر صفر پیروز شدیم در ذهن من مانده است چون اولین دربی من بود. ورزشگاه آزادی باید به این فصل می‌رسید اما این اتفاق رخ نداد. بازی‌های بزرگ باید در ورزشگاه آزادی برگزار شود. امیدوارم دربی خوبی داشته باشیم. پرسپولیس با مهدی تارتار عملکرد خوبی داشته است. همیشه هوادار پرسپولیس خواهم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139281" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139280">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚽
نورمحمدی: هت‌تریک ایمون زاید در ذهن من مانده است
‼️
دربی سه بر دو و هت‌تریک ایمون زاید در ذهن من مانده است/ هواداران دیگر مشکلی با حضور بازیکنان استقلال در باشگاه پرسپولیس ندارند/ زمان ما تغییر تیم سخت بود/ من پرسپولیسی بودم و استقلال را زیاد دوست نداشتم/ امیدوارم شاهد دربی خوبی باشیم/ پرسپولیس در این فصل یک‌تیم بسیار خوب و کامل دارد/ پرسپولیس در این فصل موفق می‌شود/ جذابیت دربی به ورزشگاه آزادی است/ اینکه دربی در اصفهان برگزار می‌شود عجیب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139280" target="_blank">📅 00:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139279">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ
: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139279" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139278">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❤️
🤩
کنایه مدیرعامل باشگاه به برخی رسانه‌ها:
‼️
این سفری که به ترکیه داشتم و چند ساعت دیگر برمی‌گردم، از چند روز قبل برنامه‌ریزی شده بود. خداراشکر همان‌طور که ترکیب تیم‌مان لو نمی‌رود، دیگر سفرهایمان هم لو نمی‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139278" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
