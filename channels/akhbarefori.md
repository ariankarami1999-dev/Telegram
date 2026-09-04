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
<img src="https://cdn4.telesco.pe/file/pGGFUxPvsnjDETcgdY9M_QgTzzwcPpgCZFDnYH1GM06Szm8wUgCdqwLHbN_dZRbRa_I_Dk2sfFkYYFLWsmeX76E4I0O_61SsahARHuVRNQwzmZFf9B_hxDStVFdSwRnmgdfUh48iSh1wJG2S0a7nFx01a-xEjfqXbavy23GXdoxFkUtBY2IEK-s3MuFlXBMeD1648AonkQY54krU0C9T-1Vy2bMZiH6dEMw0eTUdQjFnK1KRVa2F4vQqB2Th728hhO1jImNssffdaFtgJ9gOduNdjdFeciOpaFXHg4G8Hzi4HVOimKn5yOyCGj9yU31uTtuuc_JnZEWnVuCuMhyNvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.45M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 12:42:35</div>
<hr>

<div class="tg-post" id="msg-687120">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
آزادی ۵ لبنانی از اسارت رژیم صهیونسیتی با میانجیگری صلیب سرخ
کمیته بین‌المللی صلیب سرخ:
🔹
انتقال ۵ نفر از اسرائیل به لبنان را با درخواست طرف‌های مربوطه و در نقش میانجی بی‌طرف و بشردوستانه تسهیل کرده است؛ ۴ نفر امروز و نفر پنجم روز گذشته منتقل شدند.
🔹
این اقدام در ازای تحویل جنازه‌های سربازان رژیم صهیونسیتی انجام گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/687120" target="_blank">📅 12:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687119">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15209ee1b.mp4?token=GHV8pLiFm35kVGadv6tq_WbyZ3JiBRAGfmXKgSyTt99v0zdx_jManpviO6Zhe0EqOuAC8M9sfuV0aokjK4uHjEKYxFb95twRP_OVgXjUAaH0iShk4Hu9cxn7ixkoFX0WskZQ5E206tmzRM0_XGLrkP6ycgWxNTfJs7hJo5Bt2g0D_r6XHax63e8Ps7TiUJ_iPAMPv22FPp7UKSZZ2eHC923CCUH5lfakgJZRSxhwrjVaDyJKDyo6i3E7orRBSlmU9sjXyjUg55tV-15RgMtRWP8ZDqa4np8oNgXeRgffimEiCUiuUmOBYyaHEdHg4t9yG4p6-P8rKdhC77lT0JcXww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15209ee1b.mp4?token=GHV8pLiFm35kVGadv6tq_WbyZ3JiBRAGfmXKgSyTt99v0zdx_jManpviO6Zhe0EqOuAC8M9sfuV0aokjK4uHjEKYxFb95twRP_OVgXjUAaH0iShk4Hu9cxn7ixkoFX0WskZQ5E206tmzRM0_XGLrkP6ycgWxNTfJs7hJo5Bt2g0D_r6XHax63e8Ps7TiUJ_iPAMPv22FPp7UKSZZ2eHC923CCUH5lfakgJZRSxhwrjVaDyJKDyo6i3E7orRBSlmU9sjXyjUg55tV-15RgMtRWP8ZDqa4np8oNgXeRgffimEiCUiuUmOBYyaHEdHg4t9yG4p6-P8rKdhC77lT0JcXww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تسلا تاکسی‌های خودران Cybercab را در بخش‌هایی از آستین تگزاس راه‌اندازی کرد؛ این خودروهای دونفره فاقد فرمان و پدال هستند
🚕
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/akhbarefori/687119" target="_blank">📅 12:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687118">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده پدافند ارتش: فناوری پیشرفته دشمن، تضمین‌کننده بازگشت هواپیماهایش نیست.
🔹
کره جنوبی: تصمیمی برای اعزام نیرو به هرمز گرفته نشده است.
🔹
گرمای بی‌سابقه در فرانسه جان ۷ هزار نفر را گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/687118" target="_blank">📅 12:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb3a7636f1.mp4?token=livCp3YvaZzojdRH67ZnWp59W464kDs-0UpGAcedFubLmEphPdBZgatP3orjNu85LSuLuU3Z0hZDOyvYWwVS67JRHGEXWHEtuJuv3KO7RCi2LmPbwyVDZ_sHm8CoCu5yTcwBSBOBRPcV9VK1uEVmJMr3G8MIFniy_2-JlpHoP-Oj5zCFcQ9HUOteHBPQZvrvplXw126dnj5eOEHIV1h5QSw39xyaZDj-2oPcAYQhna4Ylm3kQiDeN9UqnFUoinfO5cAG0N1mCEEtLCetNvCpap9OR8-B7Xgaa7eadcnadkSpIjRmclbQke8W-Y-CjPzadGIrQC9nU1SYZirXttbDDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb3a7636f1.mp4?token=livCp3YvaZzojdRH67ZnWp59W464kDs-0UpGAcedFubLmEphPdBZgatP3orjNu85LSuLuU3Z0hZDOyvYWwVS67JRHGEXWHEtuJuv3KO7RCi2LmPbwyVDZ_sHm8CoCu5yTcwBSBOBRPcV9VK1uEVmJMr3G8MIFniy_2-JlpHoP-Oj5zCFcQ9HUOteHBPQZvrvplXw126dnj5eOEHIV1h5QSw39xyaZDj-2oPcAYQhna4Ylm3kQiDeN9UqnFUoinfO5cAG0N1mCEEtLCetNvCpap9OR8-B7Xgaa7eadcnadkSpIjRmclbQke8W-Y-CjPzadGIrQC9nU1SYZirXttbDDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروسازی که از دوطرف می‌خواهد از مردم سود بگیرد/ آیین نامه دولت را که حق مردم در آن دیده نشد بود از دستور کار خارج کردیم
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
بودجه‌ای در کشور بابت یک قانونی (در خصوص خودرو) وجود دارد دولت باید مشخصاً آن بودجه را به مردم بدهد؛ نه به خودروسازی که از دوطرف میخواهد از مردم سود بگیرد.
🔹
نظر ما در مجلس با قاطعیت این است که این پول و بودجه که از منابع بیت المال است باید به آحاد مردم برسد.
🔹
همین که توانستیم یکی از آیین نامه‌های دولت را از دستور کار خارج کنیم که در آن اصلا حق مردم دیده نشده بود، و الان آیین نامه جدید را که ببینید یعنی زور ما رسیده است؛ البته این کار تقریبا به انتها رسیده و هنوز ده تا پانزده درصد دیگر وجود دارد که باید کار آن انجام شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/687116" target="_blank">📅 12:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f56b44f1.mp4?token=sXdPCVVbBVMqAOSxyiVt0IA8YyBRZjT3EHRSHT-Dn6NhE83Xu-W9wwVw8kfruHOmLHeOPS5pBS82XZWhLVzxYFp0JRrCdN-P0zsButxtc36Wt9cQm7-BrWlf_HuC0mSvuQCGvLbh1Y7TVUkXrwS_xKlrRWVYB9GndK_vyNtT-i_ov_nQ9kXEldxiq_InFh6dT0kmgMeJR6vJu-DfXN62hEgQxP-zmvBd-_KG7t35ItidpYbqM6yszdee1C0MAZn1zCfCF1LtsHLgFLJn7ZLYH_avVHzTpRwlnACLZOyr7_eoxd1g-omITQQMIvFExmSRVUfJ6mT46T7goKq0d4SjhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f56b44f1.mp4?token=sXdPCVVbBVMqAOSxyiVt0IA8YyBRZjT3EHRSHT-Dn6NhE83Xu-W9wwVw8kfruHOmLHeOPS5pBS82XZWhLVzxYFp0JRrCdN-P0zsButxtc36Wt9cQm7-BrWlf_HuC0mSvuQCGvLbh1Y7TVUkXrwS_xKlrRWVYB9GndK_vyNtT-i_ov_nQ9kXEldxiq_InFh6dT0kmgMeJR6vJu-DfXN62hEgQxP-zmvBd-_KG7t35ItidpYbqM6yszdee1C0MAZn1zCfCF1LtsHLgFLJn7ZLYH_avVHzTpRwlnACLZOyr7_eoxd1g-omITQQMIvFExmSRVUfJ6mT46T7goKq0d4SjhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سونی ربات میکروجراح خود را با دوختن سطح یک دانه ذرت آزمایش کرد
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/687115" target="_blank">📅 12:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687113">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تلاش عمان و قطر برای آغاز چارچوب جدید مذاکرات ایران و امریکا
🔹
فایننشال‌تایمز از تلاش میانجیگران عمانی و قطری برای تدوین چارچوبی جدید برای مذاکرات میان ایران و امریکا با هدف مدیریت بحران میان دو کشور خبر داد./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/687113" target="_blank">📅 11:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d791cc65d.mp4?token=oINMObo3u_j06S8bN1xQ4bQeCllDd2LlmgALxnmL008USvqpxClS8l_DkXffBfwM8d9npAIskduqDwEcbjKkl3IzluShtV6VTUsh-jOlJoc43jl_7SNbc3EIe5-gg7r68lboNH7-jH87vGIc5SW8nCToZcRpP8-TEVN-NGtqhsIGLMqdWvT3Dm0Pc5hDIlzakYYcL66LCanovToQ549Tk64OAHUEDYy25WQ1P7gK6DI2ui_36_E8lnkuj1SP8_GpLLI1xM15WMldUPxdOmwGOmZZFuw1FA9TJngSXTldtkpyBi5y0JJwYTuCo65FnPZnB8hw4L28WBTMoQUUymdqAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d791cc65d.mp4?token=oINMObo3u_j06S8bN1xQ4bQeCllDd2LlmgALxnmL008USvqpxClS8l_DkXffBfwM8d9npAIskduqDwEcbjKkl3IzluShtV6VTUsh-jOlJoc43jl_7SNbc3EIe5-gg7r68lboNH7-jH87vGIc5SW8nCToZcRpP8-TEVN-NGtqhsIGLMqdWvT3Dm0Pc5hDIlzakYYcL66LCanovToQ549Tk64OAHUEDYy25WQ1P7gK6DI2ui_36_E8lnkuj1SP8_GpLLI1xM15WMldUPxdOmwGOmZZFuw1FA9TJngSXTldtkpyBi5y0JJwYTuCo65FnPZnB8hw4L28WBTMoQUUymdqAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جدید لحظه وقوع سیل در نپال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/687112" target="_blank">📅 11:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیر عامل پالایشگاه تهران از راه‌اندازی واحد CCR که تولید بنزین کشور را روزانه ۱.۵ میلیون لیتر افزایش می‌دهد خبر داد.
🔹
صندوق بین‌المللی پول: اقتصاد امارات وارد مرحله خطر و کسری تجاری شده است.
🔹
فقط ۴ نفتکش از تنگه هرمز در روز پنج‌شنبه عبور کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/687111" target="_blank">📅 11:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
افزایش شمار نظامیان آمریکایی زخمی در جنگ ایران به ۷۶۷ نفر
ای‌بی‌سی نیوز:
🔹
بر اساس به‌روزرسانی ‌های انجام شده از سوی وزارت جنگ آمریکا (پنتاگون) که طی ۲۴ ساعت گذشته انجام شده، شمار نیروهای آمریکایی زخمی‌شده در جنگ با ایران به ۷۶۷ نفر افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/687110" target="_blank">📅 11:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687107">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuOczDEQGQmIKNNHvWnHVNH9UQngSwG-SZAoMOtlccAA4TyotT-0aezyc_y7uNi99SQHVXUPaoUIzKRIPbpBqNCDYsbWBRZjrI8t8Qd3kLSA5T2iYqGXA2WZzXiqW01YVVGvjeScQPD8LHV55acT44O9tpyszo_rWUjRv-ZIDxhEBrWL7rOQika5cI7QAkhCjXAfvS3HWxZtIrHrLf54D6PzW5DJrElQP6cqyQNYGoqx58dejmp4_sDRImCrPEjFi43BCQtsCPAhrnN-iQk4fzYJru-6IM_Ec9bJeEav5ZYfb-_PIjhW5_UWNQHK_6YZaIvTs74ZypLSf4MC7Dp2_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hmue9yMlsVdHQD9NeaW0oBvPnwmPnAFeqkYOgCj9JsxXm_UdEA80X3A4wphbPNnraSdnYc8ACGfsx-mGRyWo1FF7YnyRQsCqjfp5i_0BY55zN5jotkK55G-kiL2iP4siKNqWSfM0-Vk4Iqdb8GIyoZkt_W1OymPaAR_LwtPysidQDhhT4cwAIYhN_uG6gsycvVntTCRBQLY37TXo1F3-yqp4bawoXgn5tBu-VnTPNnh9VA-ehRXgUIArvQcWxq5JXYp1qs9G0loEStIdwrIMztbEQvDc751m0IqJ0au-omqafu1WeDu-jhG1OyzeITlZAMk-r1Ojh2ddrRId4fm9wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced1356087.mp4?token=kNkZmax53dvHriw1DEydK6JeRUnA5yxH_8KRjn97EA4LCucwF05opdh2Gme8TJOCKA8KBxl047ULKJkwFsN5ZV18tPEud9yS5r7CpvmInFoVuEH0vNDDD5MfjO4MVMlDJiMtsuGayzKlEdkCryaDcaUC6vd02VGGT84a15zoPwO7PyAWu7P_zySLImYdZNubq-Shuqc1-UGpkBdifKdm6pz0CoTnLK66GhW5uKwk1ns6qUlxSAFSvt0uqTb8KrROhYGlfQx6AVkHx8L-kxuv3OR737xymIoEDEo25U_4Bq08z3Qy58ln_nOtkMAEzk40VA02WQUONjbV-N5sMDBJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced1356087.mp4?token=kNkZmax53dvHriw1DEydK6JeRUnA5yxH_8KRjn97EA4LCucwF05opdh2Gme8TJOCKA8KBxl047ULKJkwFsN5ZV18tPEud9yS5r7CpvmInFoVuEH0vNDDD5MfjO4MVMlDJiMtsuGayzKlEdkCryaDcaUC6vd02VGGT84a15zoPwO7PyAWu7P_zySLImYdZNubq-Shuqc1-UGpkBdifKdm6pz0CoTnLK66GhW5uKwk1ns6qUlxSAFSvt0uqTb8KrROhYGlfQx6AVkHx8L-kxuv3OR737xymIoEDEo25U_4Bq08z3Qy58ln_nOtkMAEzk40VA02WQUONjbV-N5sMDBJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه عجیب برای هواپیمای مسافربری ایندیگو در فرودگاه سرینگر
🔹
هواپیمایی هنگام پارک با تیرک سامانه هدایت برخورد کرد و آسیب دید، اما همه مسافران و خدمه سالم ماندند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/687107" target="_blank">📅 11:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687106">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLca6cxZyA8EcHyMPhpjU31xnV9a6-9FWuboSMnarLXde3JxB8-zuuqbhijmY_Gm7TEKnoztFuSMoSnjxQVTlRUgRfutRdlC-ImCs5REOKfkqbU5wj94hLSdDUKytzRoXCqdMZOfkyNezlFWd47S_D9ulR-MyEfD_Im1xhJtEBQF-p_pt_IB0WxpDfhiY_EvZKUY4yScvUie2zBcqg9hfFAiT_oWfnYKtKJ71YWeU9h-4YtNTADG-31-YnXNOidPQ7YYz_whzx3YW11ji3oCRrwC80bCDSboPZCNjmtL9OlaxUzYfZwCffF6CEEscdnwPwJmV3y0t07_r2LAy27DwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزیر امور خارجه کشورمان به اظهارات اخیر همتای اردنی؛ ایران برای پاسخ به متجاوز چقدر باید منتظر باشد؟!
🔹
به نظر وزیر امور خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟
🔹
آیا او واقعاً از این موضوع بی‌اطلاع است که در نخستین حملات آمریکا، از حریم هوایی، خاک و آبی کشورهای عربی استفاده شد؛ حملاتی که به کشته شدن ایرانیان بی‌گناه انجامید؟
🔹
ادعای وزیر خارجه اردن: حمله ایرانی‌ها واکنشی نبود، چون دو ساعت بعد از آغاز جنگ حمله کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/687106" target="_blank">📅 11:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687105">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ca2b9ae4.mp4?token=j_g9-w1_MXyXJdgpRIgP7lZaWfmQg4hdWiPPAqOf6gfjL_mKjFNXMcIgbHb9lEs62JLTjvLA2_ogranIrBsJ1cXAOIvIEGoX0sNFzYrKD1eLppQsKXmTFipQtFE5Z590Gv9wK4K4yns1BgNjNY7YmBdWiSQGdzDsKtNL8YoOH-jC04xKpDyHtV-QECeMV9ac2Fx0jwSPOkPZgnoa2KUKRzb0iMOv07rSEvlOS__mroSQ0BLc6GQaDjIOzmST-bqLHTUeP2qkqOGEUCilxizr1NMlH1Afn1LjlcCMxB46IVRgMXh-FUN-Ic5SIKYydu7kEHQn_FcIZUKnH7w_h8oYQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ca2b9ae4.mp4?token=j_g9-w1_MXyXJdgpRIgP7lZaWfmQg4hdWiPPAqOf6gfjL_mKjFNXMcIgbHb9lEs62JLTjvLA2_ogranIrBsJ1cXAOIvIEGoX0sNFzYrKD1eLppQsKXmTFipQtFE5Z590Gv9wK4K4yns1BgNjNY7YmBdWiSQGdzDsKtNL8YoOH-jC04xKpDyHtV-QECeMV9ac2Fx0jwSPOkPZgnoa2KUKRzb0iMOv07rSEvlOS__mroSQ0BLc6GQaDjIOzmST-bqLHTUeP2qkqOGEUCilxizr1NMlH1Afn1LjlcCMxB46IVRgMXh-FUN-Ic5SIKYydu7kEHQn_FcIZUKnH7w_h8oYQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقابله با عریان سازی نگرانی زنان با پوشش‌های متفاوت است؛ نه صرفا زنان محجبه
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
یکی از مطالبات مهم زنان این روزها بحث به سامان شدن اقتصاد خانواده‌ها است.‌
🔹
همچنین مقابله با عریان سازی‌ است که دارد اتفاق می‌افتد؛ جالب اینجاست که خانم‌ها با پوشش‌های متفاوت این اظهار نگرانی را داشتند. نگرانی در این راستا صرفا مختص زنان محجبه نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/687105" target="_blank">📅 11:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687104">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a98fd41f19.mp4?token=ID5eJyYU7ykeyFZJYeFN0TV9bupp_igNWyXL6jBPqhCCuUjraXdzOgaSTC7b3NJyKt_Qu4lumGpROJphpucVdFIh88-vo3uQw6PahjV93hzDuU91CDomVukeA0hJT8w-F9KB1AYZHBnvHzZZuThiFYeLIVXBcDQKrh9nLj3pfKLcctbrMS9JFFHvrCLchAzRz_67w-OdmSmJpOpFK-ntbiyfdCX-_1ntfBCOqvrWwQLWzN3g8ZWQ7XITIRYQMc_N5VVN7CXC2SJfuSh6Mf70lb74xC2n4R5XxPDc5tRgH2I6qqUChlx8dpLCo5GFn3o2iyhmVtJ2O8FZ1-hdO78AQClSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a98fd41f19.mp4?token=ID5eJyYU7ykeyFZJYeFN0TV9bupp_igNWyXL6jBPqhCCuUjraXdzOgaSTC7b3NJyKt_Qu4lumGpROJphpucVdFIh88-vo3uQw6PahjV93hzDuU91CDomVukeA0hJT8w-F9KB1AYZHBnvHzZZuThiFYeLIVXBcDQKrh9nLj3pfKLcctbrMS9JFFHvrCLchAzRz_67w-OdmSmJpOpFK-ntbiyfdCX-_1ntfBCOqvrWwQLWzN3g8ZWQ7XITIRYQMc_N5VVN7CXC2SJfuSh6Mf70lb74xC2n4R5XxPDc5tRgH2I6qqUChlx8dpLCo5GFn3o2iyhmVtJ2O8FZ1-hdO78AQClSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد وحشتناک قطار با کامیون در لهستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/687104" target="_blank">📅 10:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687103">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72545c257.mp4?token=LYtBv2ydOb1aatu91SXmupseUMx6iJZDzYR6kK_oJwp3rgJIlPaTpVJk71PlQVgJUcy9W5tEOMVGYlKquKit9RgLbWW3exoURg3zuNdYCbQs8tD0uxX-CrdmKUUEvVbvjQBXYQsU577OuPVV8K6uu3Bcu2xdfuvjjweLsz1jiXZ47_vMkscC9JCLkKVfPubGilLnBjK1BvgXzCf_wIHxq7juoSK0Hzg_LEiBB1BNnk0h82ZRAmHUdD6wR3LyxYawevRehtkeDiCD1D86ufz5yGBHI0S43cpwYjkU3hf949OIalyPewVD9HgdI-fYACwwzvBkrkgfGnrqEOekats6bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72545c257.mp4?token=LYtBv2ydOb1aatu91SXmupseUMx6iJZDzYR6kK_oJwp3rgJIlPaTpVJk71PlQVgJUcy9W5tEOMVGYlKquKit9RgLbWW3exoURg3zuNdYCbQs8tD0uxX-CrdmKUUEvVbvjQBXYQsU577OuPVV8K6uu3Bcu2xdfuvjjweLsz1jiXZ47_vMkscC9JCLkKVfPubGilLnBjK1BvgXzCf_wIHxq7juoSK0Hzg_LEiBB1BNnk0h82ZRAmHUdD6wR3LyxYawevRehtkeDiCD1D86ufz5yGBHI0S43cpwYjkU3hf949OIalyPewVD9HgdI-fYACwwzvBkrkgfGnrqEOekats6bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت صحنه لوکس‌ترین مرسدس‌ها؛ جایی که طراحی خودرو هنوز با دست انجام می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/687103" target="_blank">📅 10:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687102">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اولین جمله رهبر انقلاب پس از بیرون آمدن از زیر آوار بمباران
فریدالدین حداد عادل:
🔹
موقعی که زخمی از زیر آوار بیرون آمدند، گفته بودند: من نمی‌روم تا تکلیف خانمم معلوم شود. نهایتاً به بهانه‌ خطرات امنیتی و احتمال بمباران دوباره، ایشان را از آنجا بردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/687102" target="_blank">📅 10:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687100">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc132b42.mp4?token=Q7XlTPsSQFZA2ZopKpfN12SAmukX5S_2_7WCCbeEp-FAVghqbyCPHAvrfnYLLbjisGJcFHrOr9JCJclS-kKOjG61BE7PuoHBNLg5ced-TDbQ9TGujHN7V8lEF_mBjiY8rGU2US6ABvBWhPA9kH7cehozOs-bqo4stIZqJNGk9CbKnQB2EOtzzOKYbR-WhgaxMg8ft9JeZE87HqJKOs1ybC3A5daePyrirKcTmCJngAQlR2L2nKedTKlGmMLynyH-TEl_ID_idIQsQWjoYhGw9boRObgk1qwCJWEgV-Np0MuE1udXEWRDW_U9fnJrztjnbeHbpgFDUNBSSM1uEtOkgVixw0lfNVue3nETqf-OB3db_HGq7BS0G6tRMMfxqyQvBFWfP4mW3bzP3SXO7gSM66kE5YN0lZnvsXlQY7zEsU2GT4EJaXNFpp2kIRLALbreQJdHboukoSPlfxU3TaPtwKNYhgFQ_GUU89LlkhPluWblw9434JmpNPQYju76xb3t3ies43m9XHXucnh-wYezhM029S_qdQdNGhhfOU4ufpqyhXlhbsDIUkJ8Q8OJx7iOfTxxqgtv0TETqgXb4vtZdlLLJWqx1-XzzLXvE2_nEgUrbDPq6_bxoLK4wkVc9OWMutsLI-Xa-UQWJL-dFWRZEN8tnF491mnm006qk1F84Rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc132b42.mp4?token=Q7XlTPsSQFZA2ZopKpfN12SAmukX5S_2_7WCCbeEp-FAVghqbyCPHAvrfnYLLbjisGJcFHrOr9JCJclS-kKOjG61BE7PuoHBNLg5ced-TDbQ9TGujHN7V8lEF_mBjiY8rGU2US6ABvBWhPA9kH7cehozOs-bqo4stIZqJNGk9CbKnQB2EOtzzOKYbR-WhgaxMg8ft9JeZE87HqJKOs1ybC3A5daePyrirKcTmCJngAQlR2L2nKedTKlGmMLynyH-TEl_ID_idIQsQWjoYhGw9boRObgk1qwCJWEgV-Np0MuE1udXEWRDW_U9fnJrztjnbeHbpgFDUNBSSM1uEtOkgVixw0lfNVue3nETqf-OB3db_HGq7BS0G6tRMMfxqyQvBFWfP4mW3bzP3SXO7gSM66kE5YN0lZnvsXlQY7zEsU2GT4EJaXNFpp2kIRLALbreQJdHboukoSPlfxU3TaPtwKNYhgFQ_GUU89LlkhPluWblw9434JmpNPQYju76xb3t3ies43m9XHXucnh-wYezhM029S_qdQdNGhhfOU4ufpqyhXlhbsDIUkJ8Q8OJx7iOfTxxqgtv0TETqgXb4vtZdlLLJWqx1-XzzLXvE2_nEgUrbDPq6_bxoLK4wkVc9OWMutsLI-Xa-UQWJL-dFWRZEN8tnF491mnm006qk1F84Rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رول سیب‌زمینی پنیری؛ ترد، کش‌دار و بی‌نظیر
😍
😋
مواد لازم:
🥔
سیب‌زمینی پخته
🧀
پنیر موزارلا
🌶️
فلفل قرمز (پودر)
🫑
فلفل سبز
🧂
نمک
🍋
آب لیمو
🍞
نان تست
🛢️
روغن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/687100" target="_blank">📅 10:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687098">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46cd469101.mp4?token=lxfFYiNp0j0w08Hwt8fbojJNZc88FLFLL2WXigCULQMjKIkUSJaX1xGej6EEDwd9S6snXcgeLKpL5ot95euevf7Y8AfW-Z8eqYLsmUz0ruKJw5opF7WC1TAIsw5pR5AELNMEBgAr3Yvl5XgVxq5w2rRlUk2zHV9M7xMZ7TNGEnyXyxWFGZp9K0MO9ugm2nFCb31vQEJNj-YxpgXcQ45kVWbJOkvAWSNCY3oE6LRDsuE0o_YASaQn9VqarHoLJPbPirvY7hpDp_PQRzpwQC11s6Stuqg9ZC5023DOllo2ZHQYz9Ev4HubTIXUkyDQKQDLoj8DvGlTSNz62tJJaLuXLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46cd469101.mp4?token=lxfFYiNp0j0w08Hwt8fbojJNZc88FLFLL2WXigCULQMjKIkUSJaX1xGej6EEDwd9S6snXcgeLKpL5ot95euevf7Y8AfW-Z8eqYLsmUz0ruKJw5opF7WC1TAIsw5pR5AELNMEBgAr3Yvl5XgVxq5w2rRlUk2zHV9M7xMZ7TNGEnyXyxWFGZp9K0MO9ugm2nFCb31vQEJNj-YxpgXcQ45kVWbJOkvAWSNCY3oE6LRDsuE0o_YASaQn9VqarHoLJPbPirvY7hpDp_PQRzpwQC11s6Stuqg9ZC5023DOllo2ZHQYz9Ev4HubTIXUkyDQKQDLoj8DvGlTSNz62tJJaLuXLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمل شتر ۴۰۰ کیلویی توسط فرامرز رحمانی در آیتم پایانی قوی‌ترین مردان بازی‌های جهانی عشایری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/687098" target="_blank">📅 10:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
اهمیت احراز هویت و اصالت سنجی قبل از خرید در فضای مجازی
رئیس پلیس فتای فراجا:
🔹
ناشناس بودن هویت افراد در فضای مجازی علی‌الخصوص پلتفرم‌های خارجی، اولین، آخرین و مهم‌ترین مشکلی است که ما در حال حاضر داریم.
🔹
توصیه می‌کنیم قبل از خرید، از احراز هویت صحیح فروشنده مطمئن شوید و اطلاعات فرد را در همان سایت یا اپلیکشین بررسی کنید.
🔹
هوش مصنوعی در حال حاضر در جرائم‌هایی مانند مزاحمت‌های اینترنتی، اخبار، تصاویر و رسیدهای جعلی استفاده می‌شود، اما تعداد این پرونده‌ها در حال حاضر زیاد نیست./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/687096" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس دیوان عالی چین: ایران و چین با وجود مسائل منطقه‌ای، همواره از روابط سالم و پایدار برخوردار بوده‌اند
🔹
هشدار سازمان ملل: گرمایش زمین در چند سال آینده از آستانه ۱.۵ درجه عبور می‌کند
🔹
مرکز لرزه‌نگاری کشوری: ۸۱ زمین‌لرزه در هفته نخست شهریور ۱۴۰۵ ثبت گردیده است
🔹
فارن پالسی: چین از فشار اقتصادی ترامپ علیه ایران هراسی ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/687095" target="_blank">📅 09:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10708a381.mp4?token=AGwrGOv3DiS-6HHoRjemTWLWA1WWDvsvs75LaOXwQz0tOR-cVSKTUOKHi0FqVhw47YE4PH3wtbtM7oxtp0T9ZIVjNmnAMageT1KZ2IP_ZrLbxQPlxPsdfNmhlRmx2uTn2w0MpeI0g86hz44luOl85A3KkQ7BfxaZK0zJ44tdACGUOeM6jnnYJsI5BkHyLfcGMfMykeAIxlEG1dAzdRS-xt3ArydqYpuWSfu4JEXee2nMG3CipFTVXCN8PaaSyG1hlGErYMsDoFrNfgjbcmZMIxxloBMzZcyXv9J5lxe3XXQKgaPp2L7MG4eKua1z_xPvgQW9KI2fbHSOcPsoWGwMsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10708a381.mp4?token=AGwrGOv3DiS-6HHoRjemTWLWA1WWDvsvs75LaOXwQz0tOR-cVSKTUOKHi0FqVhw47YE4PH3wtbtM7oxtp0T9ZIVjNmnAMageT1KZ2IP_ZrLbxQPlxPsdfNmhlRmx2uTn2w0MpeI0g86hz44luOl85A3KkQ7BfxaZK0zJ44tdACGUOeM6jnnYJsI5BkHyLfcGMfMykeAIxlEG1dAzdRS-xt3ArydqYpuWSfu4JEXee2nMG3CipFTVXCN8PaaSyG1hlGErYMsDoFrNfgjbcmZMIxxloBMzZcyXv9J5lxe3XXQKgaPp2L7MG4eKua1z_xPvgQW9KI2fbHSOcPsoWGwMsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات‌ها ورزشکار شدند؛ حرکات آکروباتیک خیره‌کننده ربات انسان‌نما
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/687094" target="_blank">📅 09:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0800fdef7.mp4?token=f_AOpBJmqZlHEWXfuSpdgzqcGqm5uX7zUyVUunqmOBVw68CYMJNM6RLUa2_HDTOezTOMnbF-CtJlVBCbyq7lGwLvys2e1nCfaPFcwhv5wSSk6-VGBOjhZ_nsLdsQXPFnWMGaeAyWWlT8GWd6WWWgU7zP4fJhuikntgvELdlSz1jMa_hlniRsfbmupSR7u_kKk0sKI5YlwP-vPHyTwayH9eBwsL03JZxigMclKN0Y_F7EBSgGSgX-aVkeUned4CwNCADDVecX8BymvRJSnFj4pp7P34wiCidn6ijzxZY11zbqsY3s1ybPTE8vP5hD6DnFng1xC7x53NQQEwf2MydbWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0800fdef7.mp4?token=f_AOpBJmqZlHEWXfuSpdgzqcGqm5uX7zUyVUunqmOBVw68CYMJNM6RLUa2_HDTOezTOMnbF-CtJlVBCbyq7lGwLvys2e1nCfaPFcwhv5wSSk6-VGBOjhZ_nsLdsQXPFnWMGaeAyWWlT8GWd6WWWgU7zP4fJhuikntgvELdlSz1jMa_hlniRsfbmupSR7u_kKk0sKI5YlwP-vPHyTwayH9eBwsL03JZxigMclKN0Y_F7EBSgGSgX-aVkeUned4CwNCADDVecX8BymvRJSnFj4pp7P34wiCidn6ijzxZY11zbqsY3s1ybPTE8vP5hD6DnFng1xC7x53NQQEwf2MydbWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواشناسی: سامانه بارشی یکشنبه وارد کشور می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/687093" target="_blank">📅 09:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773498a3c5.mp4?token=K_3kVc5RXWC9ko5MlWL31dNk3vMsGBzqmfCGETE39uKfjtVrCUpPb1iFnl9OO8K1LC9QPHsN6yUCw2w5yiHNKuIPeGPGiZlvVvkj-rWVmqsHGo1J-IXz_fRTA0erERxoN1SGgecvQanufNKQ3BfY97f6y9g65A4jq4RXlF1oev6jaMZ98HW7AEzaQi30AzmoxT_qsA6moqYAewM5w08OV1XQZtdozj66yqu7g8kSKAY-_kGy0VittDGgEeEtdj4SWWoUO5J5pxYruTFt8PiUpJAH3azS6uxw5LTnMy5WqyQddLCMx8iEa8COu-uEzKBBwwsIi0D3eCGMuHcNboNIng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773498a3c5.mp4?token=K_3kVc5RXWC9ko5MlWL31dNk3vMsGBzqmfCGETE39uKfjtVrCUpPb1iFnl9OO8K1LC9QPHsN6yUCw2w5yiHNKuIPeGPGiZlvVvkj-rWVmqsHGo1J-IXz_fRTA0erERxoN1SGgecvQanufNKQ3BfY97f6y9g65A4jq4RXlF1oev6jaMZ98HW7AEzaQi30AzmoxT_qsA6moqYAewM5w08OV1XQZtdozj66yqu7g8kSKAY-_kGy0VittDGgEeEtdj4SWWoUO5J5pxYruTFt8PiUpJAH3azS6uxw5LTnMy5WqyQddLCMx8iEa8COu-uEzKBBwwsIi0D3eCGMuHcNboNIng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوچ وحشی بر فراز کوه‌های بافق خودنمایی کرد
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/687092" target="_blank">📅 09:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92a7c1a188.mp4?token=DRYBg8P_vjDBvMFMZHslua-ws3cV6grmz3TQAAGVkiqdbX1ehM2MoOzG5fNgzvNaOCS7jDAO5EqBAwRE4afmCqVnm6SjhCwkY9ACLnJZViduX_q9J-pcVTzkjff7dSyG7zSd2fIWjIPISBMxP-fMIYc2Zy251FajGxYxT4SXbo3I6BW-nSDhIO1yLPoK4dtc-y0S06BdK6MeOtKseARFudN0VtTSi_aaOWfCqdH4msU3hp9q4d3jr2nD93DPIuca49EUdLJsFQNicrk8IZYUQ6RJDbDzwAR9uAG2pXLj4AwPTsywj8LK0UxABKzbfB0zJDbRUtSk0HapbJTKc57IFZXE_93p9Q1xeVVRgbq1aDdCye-8DJVMc8OEFjhybdtmyugkHeDAMYOwgzKXFLhPomaCDPzEPSfIoKtkgybx-SgaZtdX0rkU0BvxuLqSthSPmdl4o9qC2MAtJVx3wjUy7rOqnfNVF1qPr6y8-Jwwl9kJg64C-gxdrFIO_IeF1tJYsTQfW2_43tb4CZiebcNyP7tz75rKkAzGrH4JEqvRJvkDq1JjFOq7DT0IHenWkFUqMp-bvy_txHzEiWQ2BcDkgb2FQUlZSwGE3Lud0HPLVZ0mGt9qc-TWkboZDlfgVhZwtIRw7UUGF0nfvGD4sdkTRG9nV7cOMHD39GOUmckMldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92a7c1a188.mp4?token=DRYBg8P_vjDBvMFMZHslua-ws3cV6grmz3TQAAGVkiqdbX1ehM2MoOzG5fNgzvNaOCS7jDAO5EqBAwRE4afmCqVnm6SjhCwkY9ACLnJZViduX_q9J-pcVTzkjff7dSyG7zSd2fIWjIPISBMxP-fMIYc2Zy251FajGxYxT4SXbo3I6BW-nSDhIO1yLPoK4dtc-y0S06BdK6MeOtKseARFudN0VtTSi_aaOWfCqdH4msU3hp9q4d3jr2nD93DPIuca49EUdLJsFQNicrk8IZYUQ6RJDbDzwAR9uAG2pXLj4AwPTsywj8LK0UxABKzbfB0zJDbRUtSk0HapbJTKc57IFZXE_93p9Q1xeVVRgbq1aDdCye-8DJVMc8OEFjhybdtmyugkHeDAMYOwgzKXFLhPomaCDPzEPSfIoKtkgybx-SgaZtdX0rkU0BvxuLqSthSPmdl4o9qC2MAtJVx3wjUy7rOqnfNVF1qPr6y8-Jwwl9kJg64C-gxdrFIO_IeF1tJYsTQfW2_43tb4CZiebcNyP7tz75rKkAzGrH4JEqvRJvkDq1JjFOq7DT0IHenWkFUqMp-bvy_txHzEiWQ2BcDkgb2FQUlZSwGE3Lud0HPLVZ0mGt9qc-TWkboZDlfgVhZwtIRw7UUGF0nfvGD4sdkTRG9nV7cOMHD39GOUmckMldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدرسه و دبستان موشک‌های قدرتمند و سنگین می‌خواهند؟!
کودکان ایرانی با بمب‌های سنگین تکه پاره شدند
حجت‌الاسلام‌والمسلمین محسنی‌اژه‌ای:
🔹
دشمن به جنایت‌های خود افتخار می‌کند، امروز تمام اقدامات ضدبشری علیه ایران انجام شده و دشمنان به آن افتخار می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/687091" target="_blank">📅 08:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
جاده چالوس و هراز امروز با محدودیت‌های یک‌طرفه و تردد مواجه می‌شوند.
🔹
تیم ملی والیبال ایران در نخستین بازی قهرمانی آسیا مقابل نیوزیلند، ۳ بر صفر پیروز شد.
🔹
چارلز سوم و مقام پاکستانی درباره میانجی‌گری اسلام‌آباد میان ایران و آمریکا گفت‌وگو کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/687090" target="_blank">📅 08:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687088">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lhor6esi2TEZiqvkI7db84p5qQGxa5l5sTP42PNBxvNjNp1edPIar3Gaok5xW-G3ZO-Ro3Es8BkOco9-dcjVLx2hOcwgv8fjix5aRMzBwZbo4jC3AXmh9Dn56NDYf6vRYFNzLrHSVT0lp4PF26YCbQYCf5lY3LMGsqmJ66ayO9Ybs1FFR45Pr4DBjmp_crUK5WURb5LsNSfGjxIC4u1WdksZc-ec1HLnVtq1a2PmUIXqYd0h-XzEQZI7gp9sBpOMxjRohwxq9LRis1pKzUHQWwKRDGg8CfaCz41L6d0fxDPpaYAaMKWofzBFkHqRid33VYzO4Jjpkq-u-djd-UIdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مفسر بریتانیایی-پاکستانی: بمباران ایران، منجی از آمریکا نمی‌سازد
مفسر سیاسی و فعال رسانه‌ای بریتانیایی-پاکستانی:
🔹
این دلقک نارنجی تصور می‌کند پس از بمباران ایران و کشته‌شدن هزاران ایرانی، مردم علیه دولت خودشان قیام می‌کنند و برای آمریکا می‌جنگند؛ درحالی‌که این همان توهم امپریالیستی است. او افزود: مردم آمریکا باید علیه این رئیس‌جمهور قیام کنند و او را از قدرت کنار بزنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/687088" target="_blank">📅 08:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687087">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: مدارس حتی در شدیدترین شرایط حضوری است
🔹
تمام امکانات و ظرفیت‌های آموزش‌وپرورش برای آغاز یک سال تحصیلی آرام، کم‌دغدغه و مناسب فراهم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/687087" target="_blank">📅 08:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687086">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
فایننشال‌تایمز: ترامپ توافقی شامل برنامۀ هسته‌ای و تنگۀ هرمز می‌خواهد
🔹
میانجی‌گران در تلاشند چارچوب مذاکرات تهران و واشنگتن برای توافقی جدید را ایجاد کنند.
🔹
به‌گزارش این نشریه، ترامپ خواهان گنجاندن تنگۀ هرمز در هر توافق احتمالی با ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/687086" target="_blank">📅 08:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687085">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzUmrO7gJzMEdBtP5NDqetshvaNyxU9uB3dcuo9NtkxzoCOMt-CYAAFQUeckgXCWyHufCESR_7RwOJHTcBp_bvJ1ZglrVJlnJhIwoL5AN0zJXXJglNgRx172sGImmYgGxQ2vi0MAMLTWyrhZ5LFy19IE8OdtbPD4FCE7YZMagOsFA9H_NRIkzSJAsue0IKPcib0N6OycMt-DIPry8UvYujhC-7_KX8_FsNUfJMNRh1_mXPAQxgHELlU08xL5j2ALXxnhxnzfxrguzh7__Xfl3ZJ1ltHPtgnLzpCcKMY9nmWgzfgNLd8YajegD2hBngH12UCaHDGpj8Ozs9mMjtdYew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انیمه ژاپنی از حمله آمریکا خبیث به مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/687085" target="_blank">📅 08:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687084">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLuxgJxNWye7uNfqAU7GgM15MmEq33ytfRNhvv_Q1Whf2xz4zmetbN19XjffHcEpdaISFKesR0Ginn4Du2t1te5SWyvML637Fvh9vY81VBUPZJRvCIvapiAqftGPVvT5XobmaILiiQKuyyYS_WzKMeT0AL8D0tzVX_5Uj6y-7tks34hMeDfBRwo0biwBrf9pW2V6TONJXyeFlT5xBRakGVXUFUOrEIqhz1K2ki8cX18td21Yg2VgqfUP4KNc8e6qZers6KOqYdTLObXkKong5VGwxibnV98Xz5VyKOAWc5kyvFf5qr-UW6xE6wIO0LgTIu8mRd-CbU3J2vglnHtmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۳ شهریور ماه
۲۲ ربیع‌الأول ۱۴۴۸
۴ سپتامبر ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/687084" target="_blank">📅 08:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687082">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
هیاهوی تبلیغاتی جدید وزیر خزانه‌داری آمریکا دربارۀ تحریم‌ها علیه ایران
🔹
وزیر خزانه‌داری آمریکا مدعی شد که اتحادیۀ اروپا رسما به روند «انزوای اقتصادی» علیه ایران پیوسته است.
🔹
اسکات بسنت بدون ارائه جزئیات بیشتری از این «موضع قوی و زودهنگام» قدردانی کرده است.
🔹
پیش از این رسانه‌های آمریکا گزارش داده بودند که جنگ اقتصادی دولت ترامپ علیه ایران، تاکنون ادامۀ همان سیاست فشار حداکثری با دوز بیشتری از هیاهو و جنجال‌های رسانه‌ای بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/687082" target="_blank">📅 03:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687081">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4bac92f47.mp4?token=UIW07X1XC6gVkfpTyyZNUHLlzPLbbVpK2aYMyoEXBP2Lekr4TsoWQqJCvkqINB_Mc6ZsIx3XVgfDVLGRAmZv8BQ68IyTF8BO8_ENTX9cRoY_JXoSRPkMeJQGRF8n27RTudrYvXTgJiwjtpNmJK7VDFbXROz8McJYNnv46NcC4L9FPmb2p5-4VbsGgvIZKDwWeKZjRCSdipUnA0V797nCe3A9bowuRdpdRTm2ySNtyYJTm4rYkCyr7CQiGkfWmWIL-NcEuULz2oVeCXfALebo-wKOF_73UViKVtyk_cWLV72ipxFqAInlKHwRVu903EXksUJEj13IbXcmnwh-BT-CmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4bac92f47.mp4?token=UIW07X1XC6gVkfpTyyZNUHLlzPLbbVpK2aYMyoEXBP2Lekr4TsoWQqJCvkqINB_Mc6ZsIx3XVgfDVLGRAmZv8BQ68IyTF8BO8_ENTX9cRoY_JXoSRPkMeJQGRF8n27RTudrYvXTgJiwjtpNmJK7VDFbXROz8McJYNnv46NcC4L9FPmb2p5-4VbsGgvIZKDwWeKZjRCSdipUnA0V797nCe3A9bowuRdpdRTm2ySNtyYJTm4rYkCyr7CQiGkfWmWIL-NcEuULz2oVeCXfALebo-wKOF_73UViKVtyk_cWLV72ipxFqAInlKHwRVu903EXksUJEj13IbXcmnwh-BT-CmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار درباره‌ اسپانیا: به بسیاری از جهات، این وضعیت بدتر از یک حمله نظامی معمولی است. آن کشور نابود خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/687081" target="_blank">📅 03:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687080">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea9acc591.mp4?token=oPDRjehuNJrK9u-bw2CLuwVy6rWt_Ha_cPZG7JhXEAKrcPaLtYthi7oSbcNKM4rsQsEy-1JQ7KijT4-_OOdT3n2vCDIL7DwKEndkpmjhJHC3-zQmaXsYpHLFcZNl-8nxD-U3KIdihDapLvASR6dJkSLVp2t7JSa9kCq9Cf2CAKZK6AXLNaspyLV8R4jvRiPFNgIhiq3wiXta2JZ1YgX7-Suapapqgx-15r2yAvcwxoGmx_MoOCnbFsn6lAoTj4saQ4InpHoszvjuYvjYqpLH4JJev93OS0sfvUKsb_TIeLLjntc7rVzIUhMVOwDVe9zAnWVyb9DSUEE4g5khKjyBfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea9acc591.mp4?token=oPDRjehuNJrK9u-bw2CLuwVy6rWt_Ha_cPZG7JhXEAKrcPaLtYthi7oSbcNKM4rsQsEy-1JQ7KijT4-_OOdT3n2vCDIL7DwKEndkpmjhJHC3-zQmaXsYpHLFcZNl-8nxD-U3KIdihDapLvASR6dJkSLVp2t7JSa9kCq9Cf2CAKZK6AXLNaspyLV8R4jvRiPFNgIhiq3wiXta2JZ1YgX7-Suapapqgx-15r2yAvcwxoGmx_MoOCnbFsn6lAoTj4saQ4InpHoszvjuYvjYqpLH4JJev93OS0sfvUKsb_TIeLLjntc7rVzIUhMVOwDVe9zAnWVyb9DSUEE4g5khKjyBfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو: من به توانایی خود برای سرنگونی نظام ایران، یک بار برای همیشه، اطمینان دارم
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/687080" target="_blank">📅 03:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687079">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای نیویورک‌پست: عمان پیشنهاد ایران برای دریافت مشترک هزینه خدمات از کشتی‌های تجاری عبوری از تنگه هرمز را رد کرده است/ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/687079" target="_blank">📅 02:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687078">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ترامپ سرپرست جدید وزارت ارتش آمریکا را منصوب کرد
🔹
دونالد ترامپ، رئیس‌جمهور تروریست آمریکا، آدام تیل، دستیار وزیر ارتش این کشور را به‌عنوان سرپرست وزارت ارتش آمریکا منصوب کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/687078" target="_blank">📅 02:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687077">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
چند انفجار شمال عراق را لرزاند
🔹
به گزارش خبرگزاری المعلومه، همزمان با انتشار اخباری درباره شنیده شدن صدای چند انفجار، صدای پرواز پهپادها در استان اربیل شنیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/687077" target="_blank">📅 01:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687076">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سناتور آمریکایی خواستار برکناری هگست شد
🔹
«تام تیلیس» سناتور جمهوری‌خواه از ایالت کارولینای شمالی آمریکا در پیامی با انتقاد شدید از عملکرد پیت هگست وزیر جنگ ایالات متحده خواستار برکناری او شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/687076" target="_blank">📅 01:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687075">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
دستور پنتاگون برای تغییر نام جنگ علیه ایران
🔹
ایمیلی از نیروی هوایی آمریکا که در ماه اوت ارسال شده و شبکه خبری سی‌بی‌اس به آن دست یافته است، نشان می‌دهد پنتاگون به نیروهای خود دستور داده بود دیگر برای اشاره به عملیات نظامی جاری آمریکا علیه ایران از عنوان «عملیات خشم حماسی» استفاده نکنند.
🔹
دلیل این دستور آن است که دونالد ترامپ سه ماه پیش در میانه درگیری‌ها با کنگره بر سر ضرب‌الاجل ۶۰ روزه برای اتمام جنگ علیه ایران مدعی شده بود که «عملیات خشم حماسی» علیه ایران روز ۵ ماه مه با آتش‌بس به پایان رسیده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/687075" target="_blank">📅 01:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687074">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: ما قبلاً در جنگ با ایران پیروز شده‌ایم!  رئیس‌جمهور جنایتکار آمریکا:
🔹
با ایران، به محض اینکه پیروز شویم، که طولانی نخواهد بود، ما قبلاً پیروز شده‌ایم، زیرا آنها نمی‌توانند سلاح هسته‌ای داشته باشند.
🔹
اگر امروز ایران را ترک کنیم، ۲۵ سال طول…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/687074" target="_blank">📅 01:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687073">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad8e63141.mp4?token=lO5uJgq4nxhB8VDPdNn-Gg-jyjXFwnMW4pWwW6wPXJm-xmy3hlL5zLbBm1Qg8ff2V6vs-mdl-Tf7Do-e4wIcBAYQhB0LabNZlUryS_6Mfp3RSw0shMjPiygk8YFlLUonoAitrQfB3-XWaICWUynjlrrlKMOz-WIDVhzncwIJ5vvoTN_jQGbDxF3pjNdN9SSISvH_Nqbu-xfJtHGVDTt1IwXSqMtnQrnUHKL5LaByOs3IZGYfHz5L-ydzGSRf5KnwDtPbrasb7qF3YwHnCSW_ZVpMW6SYo4kFl1nCwJSUX4I10UpkV2Bkl-zP-czPXH8Br0TriQbRgAXGFT2k_hJ0YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad8e63141.mp4?token=lO5uJgq4nxhB8VDPdNn-Gg-jyjXFwnMW4pWwW6wPXJm-xmy3hlL5zLbBm1Qg8ff2V6vs-mdl-Tf7Do-e4wIcBAYQhB0LabNZlUryS_6Mfp3RSw0shMjPiygk8YFlLUonoAitrQfB3-XWaICWUynjlrrlKMOz-WIDVhzncwIJ5vvoTN_jQGbDxF3pjNdN9SSISvH_Nqbu-xfJtHGVDTt1IwXSqMtnQrnUHKL5LaByOs3IZGYfHz5L-ydzGSRf5KnwDtPbrasb7qF3YwHnCSW_ZVpMW6SYo4kFl1nCwJSUX4I10UpkV2Bkl-zP-czPXH8Br0TriQbRgAXGFT2k_hJ0YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم همچنان به دنبال دستاوردسازی در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ مدعی شد که اگر ایالات متحده همین امروز از جنگ علیه ایران خارج شود بازسازی این کشور ۴۵ سال طول خواهد کشید.  #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/687073" target="_blank">📅 01:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687072">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
طبق اعلام برخی خبرگزاری ها ادعای نتانیاهو مبنی بر تصرف تپه‌های علی‌الطاهر هنوز به تایید مقامات لبنانی نرسیده است
🔹
همزمان با این ادعا، همچنان علی‌الطاهر هدف حملات هوایی و توپخانه‌ای رژیم صهیونیستی قرار دارد.
🔹
به دلیل اهمیت منطقه علی‌الطاهر، نتانیاهو هدف استفاده سیاسی و انتخاباتی از این موضوع دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/687072" target="_blank">📅 01:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687071">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8db55a23.mp4?token=H9cdOMDYYTprFb_lAt0KyTO5dYswo4Eyinxg7aq1owooQzBeVd4rz7quXP3_0cLHnmyDVUzspejrOoWEL2HmuyCwFSx8QuD67bMxloJldI8qsdA63sEqrKsEGZ256arhiwWnVfpkAxMRbbrXwmWb_wOeWDcrgBUJ-rl8Czfu_NOZlIbus5Gnt1J_CWFvCQl0tfdI9gJQv5iIxTMtGVe549RJqfK1FBzkhmBhjN_ghooMU6nT7WIsAxStDNhIotLYaGnBwvW8_WoBMpk39aGejKgUCWBYiiFIbNb2xJUqE2kfhHU7869pB1c_yio2OJq_dY_mGxJgLMKT2McpqtJXAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8db55a23.mp4?token=H9cdOMDYYTprFb_lAt0KyTO5dYswo4Eyinxg7aq1owooQzBeVd4rz7quXP3_0cLHnmyDVUzspejrOoWEL2HmuyCwFSx8QuD67bMxloJldI8qsdA63sEqrKsEGZ256arhiwWnVfpkAxMRbbrXwmWb_wOeWDcrgBUJ-rl8Czfu_NOZlIbus5Gnt1J_CWFvCQl0tfdI9gJQv5iIxTMtGVe549RJqfK1FBzkhmBhjN_ghooMU6nT7WIsAxStDNhIotLYaGnBwvW8_WoBMpk39aGejKgUCWBYiiFIbNb2xJUqE2kfhHU7869pB1c_yio2OJq_dY_mGxJgLMKT2McpqtJXAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اختراع جالب چینی‌ها برای تمیز کردن شیشه‌هایی که دسترسی بهشون خیلی سخت و غیرممکن
است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/687071" target="_blank">📅 01:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687070">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
مخالفت دولت عراق با تمدید حضور نظامیان خارجی  حیدر العبودی سخنگوی دولت عراق:
🔹
پیشنهاداتی درباره تمدید حضور نیروهای خارجی وجود داشت اما دولت با این پیشنهادها مخالفت کرد. حضور نیروهای خارجی و حتی مستشاران در خاک عراق تمدید نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/687070" target="_blank">📅 01:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687069">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
اعتراف ناخواستۀ ترامپ به عدم پیروزی در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا در ماه‌های گذشته بارها مدعی شد که در جنگ علیه ایران به پیروزی رسیده است.
🔹
با وجود این او در یک لغزش زبانی جمله‌ای بر سر زبان آورد که نشان می‌دهد که حتی خودش هم به ادعاهایش در این زمینه باور ندارد.
🔹
او در سخنانی دربارۀ جنگ علیه ایران ابتدا گفت «به محض اینکه به پیروزی برسیم» اما بلافاصله سخنش را عوض کرد و گفت: «همین الان پیروز شده‌ایم.»
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/687069" target="_blank">📅 01:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687068">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405e6a7140.mp4?token=PY6VQLuXWYnAG1pMGD6goqXjxITtlzYj06Ln6E9HPLXOvrhFZkrj11Cab6I6ifL2Fa5D4JYJV9j0usu68G_uJNy23FnRXZ-KCRFsmElMB6YlUiIUkbF_Rr8QyR1hoI3gLPInJvn-_RC5WYyhPszGWJuT-FCGAwaGcMapu5awbx8Cfdrqa3Rlyj6WOphiYn7o6SbfMREJ_gbGrPmsTBkpLBOnieetVBtzvHA6SoCkDagrrbj-r01OgLS2bRqgqMZzBi5qt5KVyD48JMS-Jr3Il5f3_0psdZWlMY5HtmdvXoghy7xoI-NX_QIsMxYS0ot0Qbdq3uNaWS3vnKKCgXJkhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405e6a7140.mp4?token=PY6VQLuXWYnAG1pMGD6goqXjxITtlzYj06Ln6E9HPLXOvrhFZkrj11Cab6I6ifL2Fa5D4JYJV9j0usu68G_uJNy23FnRXZ-KCRFsmElMB6YlUiIUkbF_Rr8QyR1hoI3gLPInJvn-_RC5WYyhPszGWJuT-FCGAwaGcMapu5awbx8Cfdrqa3Rlyj6WOphiYn7o6SbfMREJ_gbGrPmsTBkpLBOnieetVBtzvHA6SoCkDagrrbj-r01OgLS2bRqgqMZzBi5qt5KVyD48JMS-Jr3Il5f3_0psdZWlMY5HtmdvXoghy7xoI-NX_QIsMxYS0ot0Qbdq3uNaWS3vnKKCgXJkhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه درست کردن سس مایونز سیر خانگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/687068" target="_blank">📅 01:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687067">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای ونس: ترامپ شخصاً با رئیس‌جمهور چین صحبت کرده که به ایران امتیاز خاصی اختصاص ندهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/687067" target="_blank">📅 00:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687066">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb1538895.mp4?token=FstZE8uC5MdBHJUkdKzhJLVMG2yMMC9fGo3vd4K6PKMvwtZ1m630EiEANYjA7D18nUuCDytD2TpQRYNqTMIPq5SyfMQ3DQQNDKZjJqeb-m5gM07Ge3LqKQDssSZeuFTAqBwyaNZa8-_o1Ci7agEUZF2C2vT0pkG3PeJEa6SOG9II4bdZS_1IaXbfNoHNXxyvBTsPnbhstIaINR__O5_7qvyAI12XDPYXNz0kQbVaIUm6s5I-AKQOZD5HsYu1_SA7mBLHdbaEIaT3BuNb0py5mrVZDbHUMb67E5f-_NakdZREX7id-BLnjJs24C3jYUkshfhrD5NdbQ0jbN_0qIiNhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb1538895.mp4?token=FstZE8uC5MdBHJUkdKzhJLVMG2yMMC9fGo3vd4K6PKMvwtZ1m630EiEANYjA7D18nUuCDytD2TpQRYNqTMIPq5SyfMQ3DQQNDKZjJqeb-m5gM07Ge3LqKQDssSZeuFTAqBwyaNZa8-_o1Ci7agEUZF2C2vT0pkG3PeJEa6SOG9II4bdZS_1IaXbfNoHNXxyvBTsPnbhstIaINR__O5_7qvyAI12XDPYXNz0kQbVaIUm6s5I-AKQOZD5HsYu1_SA7mBLHdbaEIaT3BuNb0py5mrVZDbHUMb67E5f-_NakdZREX7id-BLnjJs24C3jYUkshfhrD5NdbQ0jbN_0qIiNhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم همچنان به دنبال دستاوردسازی در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ مدعی شد که اگر ایالات متحده همین امروز از جنگ علیه ایران خارج شود بازسازی این کشور ۴۵ سال طول خواهد کشید.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/687066" target="_blank">📅 00:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687065">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8VeSwlDRRnypUNsBNtuQefghKGeVrOmnQMrcS6ZR46hvntnRdAONzOGv1YW9QjB75wVLjg73FMi5icF8ESU4WM5w9KbKmAm-QGw5R2MH-IwSyE6ljWaA2fltHXQ3C1hyYiJJUR1RqENYAYtN0UjVRWe26ohGZf4f7ys_F9SA7fpYUX7MNBV_bh9OmHE3MhZ7DUbIro_TKYKDH17Tm4mDXE5D2tghD0QrXfaoMUPW3fzC7kaS67mXdNH4KEKYLq4UdiNnDUaWUOBJfLcadTEzO7ksB2GbjOT3cmtxkFuatGojb1UA0LWfT241kbPuhZyP-eNhdnVngjzwCkLxjGZHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشکل جدی لجستیکی نیروی دریایی آمریکا در غرب آسیا
روزنامه نیویورک‌تایمز:
🔹
حدود ۲۰ کشتی که تقریباً ۲۰ هزار نیروی دریایی و تفنگدار دریایی را حمل می‌کنند، هر هفته به بیش از ۴۲۰ هزار وعده غذایی و حدود هشت میلیون گالن سوخت نیاز دارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/687065" target="_blank">📅 00:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687064">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
وزیر نفت: در زمان محاصره اول چند بار توانستیم نفت را از خط محاصره رد کنیم. نفت را هزاران کیلومتر دورتر می‌فروختیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/687064" target="_blank">📅 00:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687063">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264181d47f.mp4?token=sVdg__1xa-9YcsqLlT_N481MgYLYVKdAeZtXkDDmu8iA5SrJiK2kLq7-NFB4MnnG7pdH04qNYViCU7GkobdjV1rX_cIO0bovcjYRylwD-AypF0o3KFT7JfVHWiZA2oTFUrNsGTmhJInh72Shkgj2jE07jbhML-0mLKHu7BPLCL27g7ncG4CIXsqe-B__2C6AR6ejKrtS9FNX9-XgVVdmrcr_8GFFt7ROBDrztb97BuSpRXvtBFsrKJtLk57gz-H6_w_Xe3_9PX5-0MZdCeMV6AXjGTdsGpxtdncVJ6gBIE0GDKUQNTccPL_nj_n8CW9xFwpiKcVbiJ0xbQf-b10IxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264181d47f.mp4?token=sVdg__1xa-9YcsqLlT_N481MgYLYVKdAeZtXkDDmu8iA5SrJiK2kLq7-NFB4MnnG7pdH04qNYViCU7GkobdjV1rX_cIO0bovcjYRylwD-AypF0o3KFT7JfVHWiZA2oTFUrNsGTmhJInh72Shkgj2jE07jbhML-0mLKHu7BPLCL27g7ncG4CIXsqe-B__2C6AR6ejKrtS9FNX9-XgVVdmrcr_8GFFt7ROBDrztb97BuSpRXvtBFsrKJtLk57gz-H6_w_Xe3_9PX5-0MZdCeMV6AXjGTdsGpxtdncVJ6gBIE0GDKUQNTccPL_nj_n8CW9xFwpiKcVbiJ0xbQf-b10IxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الکامپ ۲۹؛ جایی که تکنولوژی، آدم‌ها و قصه‌ها کنار هم قرار گرفتند
🔹
ایده‌ها، گفت‌وگوها و لحظه‌هایی که ارزش روایت شدن داشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/687063" target="_blank">📅 00:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687062">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77c5f4cdb8.mp4?token=XKdFHb9Ynkn-Y7xCCPr5Ta0Jh_TbP8okyOUEe2k1qNBLw7YOWlVbtK2ZOeO96k6BHDcovC0RbfZnEiS8BWcmzDZLiEQa4xElGO3JYKu3wabBewWmggsVaiSLYqUhqjAlcADAB65vLz6b4cZCCR1DuT8DXLGCAyMWNAnMrQlc9NRm7PIGVO4Eb5Of1wR3S7kEU-YjKDksRQ1XHwAXUGSFvaHGBFMmRJZDpCw5vZ-2iXwE-lZNkKdBsanhVgPlxpR4VaoLiEkAig3uYlAFk11ST8CNoOblabTEwUXt8hwXSmPqiQqEeRKA4CnTp-i6ZFQJgXfhLuj8ZitdXXusDEainw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77c5f4cdb8.mp4?token=XKdFHb9Ynkn-Y7xCCPr5Ta0Jh_TbP8okyOUEe2k1qNBLw7YOWlVbtK2ZOeO96k6BHDcovC0RbfZnEiS8BWcmzDZLiEQa4xElGO3JYKu3wabBewWmggsVaiSLYqUhqjAlcADAB65vLz6b4cZCCR1DuT8DXLGCAyMWNAnMrQlc9NRm7PIGVO4Eb5Of1wR3S7kEU-YjKDksRQ1XHwAXUGSFvaHGBFMmRJZDpCw5vZ-2iXwE-lZNkKdBsanhVgPlxpR4VaoLiEkAig3uYlAFk11ST8CNoOblabTEwUXt8hwXSmPqiQqEeRKA4CnTp-i6ZFQJgXfhLuj8ZitdXXusDEainw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگ‌های مختلف بنزین چه فرقی با هم دارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/687062" target="_blank">📅 00:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687061">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افشاگری تکان دهنده نماینده مجلس از همدستی برخی دستگاه‌های مهم کشور با تراستی‌ها در فساد مالی
رحیم زارع، نماینده مجلس در
#گفتگوی
اختصاصی با خبرفوری:
🔹
گزارش حسابرسی که سال ۱۴۰۲ شرکت نفت داده است و تفریغ بودجه همان سال توسط دیوان محاسبات یک اختلاف ۴۴۰ همتی آورده است که مایه تأسف است. پولی که از سال ۱۳۹۶ اختیارات شرکت پخش پالایش گرفته شده و به شرکت ملی نفت داده شده است؛ فرایندی غلط است که رو به جلو می‌رود. این پول که با دلار نزدیک ۵ هزارتومان دست تراستی‌ها بود؛ یک نمونه‌اش در بانک ملت است.
🔹
در گزارش دیوان محاسبات بانک ملت از محل وجوه ارزی حاصل از فروش فرآورده‌ها (که تراستی به عنوان امانت در اختیارش بوده است) به شرکت اهداف تسهیلاتی اهدا کرده است تا سهام بلوکه هلدینگ خلیج فارس را از دولت بخرند؛ یعنی از پول شرکت پخش و پالایش به خود شرکت صندوق بازنشستگی و شرکت اهداف وام داده که سهام هلدینگ خلیج فارس را بخرند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/687061" target="_blank">📅 00:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687060">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a4dcb8c2.mp4?token=K7vT09Ch1qnLkJ3oi8sg05zj9QrBsXGKOD69jOgp-7M4jLHWMoPGp4gzrTmO6QJlJwkRqNcw2SMsrQQIfgEIoJtaFhBp2r-v8wEvNjvQgJGX4doIwYpPi990k2iu_l-I-DQElFc2YhAsav2fcJZB6q8pNqlwhnt07NbixpRwS3nigRkpIe86aqzHsQ6R9FTR9bt2LUpR0Rqge_oi0YtI4ggkXtu65mwIInbIxFwmPfOZjrgM4ZZ7FWH-VX21AhJ9EDbE6Bo-5FQ0L9KWNGsJ2M2K_CnglJPPwzg6B9jY-VbMVcDUArrT3gftMAnLE2fs1r27GBBQaXoNCGxSJru7GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a4dcb8c2.mp4?token=K7vT09Ch1qnLkJ3oi8sg05zj9QrBsXGKOD69jOgp-7M4jLHWMoPGp4gzrTmO6QJlJwkRqNcw2SMsrQQIfgEIoJtaFhBp2r-v8wEvNjvQgJGX4doIwYpPi990k2iu_l-I-DQElFc2YhAsav2fcJZB6q8pNqlwhnt07NbixpRwS3nigRkpIe86aqzHsQ6R9FTR9bt2LUpR0Rqge_oi0YtI4ggkXtu65mwIInbIxFwmPfOZjrgM4ZZ7FWH-VX21AhJ9EDbE6Bo-5FQ0L9KWNGsJ2M2K_CnglJPPwzg6B9jY-VbMVcDUArrT3gftMAnLE2fs1r27GBBQaXoNCGxSJru7GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمه ژاپنی از حمله آمریکا خبیث به مراسم عروسی
در سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/687060" target="_blank">📅 00:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687059">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D51WVqstVz0l4b7OkmVyYbsLTTkzDPwapl-fdZijm1IF1UkmFDLjlerAMt2Rz8vCsYA95Jnxl2zC565dn_9epy4WRTb6SWXIZVSgllNsiBBlo9EEwfryQi-ZjocVS65sCkxbA7bhkl0W_lH1zmV-D3RLENFMojO2gjabPWN2FA9Uc_EAEiJaw7H_ztREgX8VyDxcaF_7fw_IOaYNTGEm4NoqWbLy48YC94WFhdxNnVyIoDlFE__4crGwaqFu3YETv5Eerbvs47cTY_P4ffkwuxIGaEn55BDZKh2xqqT0A6_08FWSjyi-q8swUyYP6CYiyaIGJb0WS4sNiI6LDFfiQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/687059" target="_blank">📅 00:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687058">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
مخالفت دولت عراق با تمدید حضور نظامیان خارجی
حیدر العبودی سخنگوی دولت عراق:
🔹
پیشنهاداتی درباره تمدید حضور نیروهای خارجی وجود داشت اما دولت با این پیشنهادها مخالفت کرد. حضور نیروهای خارجی و حتی مستشاران در خاک عراق تمدید نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/687058" target="_blank">📅 23:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687057">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سنتکام: در راستای تضمین پایبندی به تحریم‌ها علیه ایران، مسیر ۸۷ کشتی را تغییر داده، فعالیت ۳ فروند را متوقف کرده و برای بازرسی وارد ۲ کشتی دیگر شده‌ایم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/687057" target="_blank">📅 23:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687056">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d834f1eda0.mp4?token=nsyE7KUX3R_voviIbth-H10zaE4mFOS13E-9TUeIbs_oSzqwiEJYIiRjvEK_Uu2eZs-CgnfE5Yx3IlJeGs1WnvVci4A1vEwMJw2cvhGXYArUJQAsknEGfwG2ZOMhWQd-bs-FYW4kQwpMk22vUDGLZr9lhWw_Kpjd3WDVxpHmX6JwzMifE2Tz-1PkcoOBJmzGtzS7aoO3aNhrzJAbc03z31qk69DhQJxh7VTTKP_KU_gUmqAfTG7CWCXtsyKaEEMcAdl7jmb7aFm3MRGDa7rjsgdv9CnUxFfETGEb7tbHHQZ4zpRVDJF9BgJbfcLE9X-OsbHKa8N-W8LJXZjNS85V4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d834f1eda0.mp4?token=nsyE7KUX3R_voviIbth-H10zaE4mFOS13E-9TUeIbs_oSzqwiEJYIiRjvEK_Uu2eZs-CgnfE5Yx3IlJeGs1WnvVci4A1vEwMJw2cvhGXYArUJQAsknEGfwG2ZOMhWQd-bs-FYW4kQwpMk22vUDGLZr9lhWw_Kpjd3WDVxpHmX6JwzMifE2Tz-1PkcoOBJmzGtzS7aoO3aNhrzJAbc03z31qk69DhQJxh7VTTKP_KU_gUmqAfTG7CWCXtsyKaEEMcAdl7jmb7aFm3MRGDa7rjsgdv9CnUxFfETGEb7tbHHQZ4zpRVDJF9BgJbfcLE9X-OsbHKa8N-W8LJXZjNS85V4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات گسترده در پایتخت اسپانیا در اعتراض به بحران مهاجرت
🔹
هزاران نفر از ساکنان مادرید پایتخت اسپانیا با برگزاری تظاهراتی گسترده از نحوه مدیریت بحران مهاجرت از سوی پدرو سانچز نخست‌وزیر این کشور انتقاد و خواستار اقدام فوری دولت اسپانیا در قبال این مساله شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/687056" target="_blank">📅 23:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687055">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fab0b1b62.mp4?token=BVeLXUfuUJiOksNTBF6L1hyVxircbMXBj6TqFGLv7MVq3nGiR8kBQhm4hTQRQAJ_cc-rt-7wJgIrE-bFMREnRqOW4gCWjjosqqWBcnDSZBLAkcIOuzxHIBiy8OS2qUy7HKXO3tWEoKyXiIS_v8r8nKqIO8qPZEVI83xa72AvozKN-B41OExcX91D6ZiL27F-eLZmIVO-wRtuz8il2VKk7jF0SeH23apDRDvtXsI92_tX30JEc2195rkxiLu4yEMuOEpiOa2s3vBQ6wCCu5jLRxq-y9IasIRpfCeDCMG62ArBYDx4GergmZ6zGK8SbCSZG0aGX3KLMcGMMEcKR7Mmxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fab0b1b62.mp4?token=BVeLXUfuUJiOksNTBF6L1hyVxircbMXBj6TqFGLv7MVq3nGiR8kBQhm4hTQRQAJ_cc-rt-7wJgIrE-bFMREnRqOW4gCWjjosqqWBcnDSZBLAkcIOuzxHIBiy8OS2qUy7HKXO3tWEoKyXiIS_v8r8nKqIO8qPZEVI83xa72AvozKN-B41OExcX91D6ZiL27F-eLZmIVO-wRtuz8il2VKk7jF0SeH23apDRDvtXsI92_tX30JEc2195rkxiLu4yEMuOEpiOa2s3vBQ6wCCu5jLRxq-y9IasIRpfCeDCMG62ArBYDx4GergmZ6zGK8SbCSZG0aGX3KLMcGMMEcKR7Mmxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری ویژه و خاص از شهیدان حاجی‌زاده و باقری در رزمایش موشکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/687055" target="_blank">📅 23:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687054">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1WQLwkNLE2HxrvSvpzy_okTcdTo8FptLrD7yD5dSEkYTyc3rx-YQDaOg2RxMmZddVhhzMP8XaUOw2-bWuRrDBjsaWZNxNLlr4j-7TKiTkg6KEn_86UkkIX3qkEIVIj9YQbMrkjzrEegovFdY1s_FuUTn5dFKsCfvDkjl7N3gmIA_AnVBynCky6hxCZhO2eEdcCIxIOuub-jjgcLIZ_ZSmH94R94LXPIdGTR5cbqnBo6Jd70vwSygpGY9MrcNMggkjMn4UhWNXzi9MKydXhMhH3JAfcLF7yhPeFQYzeTZMuTXO0jJXkLj6eSLi3WoaEOl23Co19GC7H4doJ78OB4rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: بر خلاف آمریکا که حمله به اهداف غیرنظامی را تبدیل به الگوی ثابت جنگ‌های غیرقانونی خود کرده است، ضربات دفاعی ایران منحصرا علیه اهداف نظامی بوده است. گزارش رسمی قطر نیز اثبات‌کننده این واقعیت است
🔹
سخنگوی وزارت امور خارجه در پیامی در شبکه ایکس، با اشاره به سند ثبت‌شده توسط قطر در اتحادیه بین‌المللی ارتباطات راه دور (ITU) که در آن تاکید شده ضربات دفاعی ایران، فقط متوجه پایگاه‌های نظامی آمریکا بوده است، نوشت: دولت قطر در سندی رسمی که به اتحادیه بین‌المللی ارتباطات (ITU) ارائه کرده، تأیید کرده است که حملات دفاعی ایران علیه نیروهای آمریکایی مستقر در خاک قطر منحصرا «متوجه تأسیسات نظامی آمریکا بوده است. هیچ منطقه غیرنظامی هدف قرار نگرفته است
🔹
تنها استثنایی مورد ادعای قطر، حمله به یک تأسیسات گازی در ۱۸ مارس بوده است. اما در این مورد هم باید در نظر داسته باشیم که آن تأسیسات در آن زمان در خدمت عملیات‌های تجاوزکارانه آمریکا علیه ایران بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/687054" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687053">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giGlfyfLb0WNQf3pYVc9eKovmCVylZQ5D1dGctEUph5kTGUnJUIbbn8mOD202jynnJPco556Uo6QRvZS3V4Ss-70JVAa91oXXV_TASoOYcBG8vlSO_WL7hagfsmJ1o7Vaoh57HKECExvV4BDHc2--lt2mac1Fto68W7KSUuYIK6WH8fK1k7EJyTc49OFpegHNpvcGEd4ON96dDIF-nyeLriFGWp0X_8Wn0tcJ__tYeQvOIDkRrd_71FR0SBcCQzqqZ5am9YsnXDvgJ1IgiRLmjvbf3kLBoRXLvxTXx4ysS9nNkmGidCLCqa5Y5w87LDBOrtkZR3Ty4g2sJxaeea9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ متوهم: منتظر فروپاشی اقتصاد کانادا باشید
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/687053" target="_blank">📅 23:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687052">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GACZOJIFOqapW2SYh98vXjJ6JCVoBSMnp4gDyRrXRAlv1ztYWKgsGp_h7VZHqgqTCA4wvCmlH7agMbnaUUhSPtQ4piKXJD6bn56mmp-K_fx2JWYhS3o0Bp3KXex3TC_zjQoTKGpl1_gu1iCErzf4AQHRZEyzI5ix9Zivh2g4iP-URSAXCFc2QOY7YZou9nfw6rW07EZGL4C2aKfmg9WjqaR0YNkH5V8KvLjNioyifmqP62Uq_hBita7uX__-PPpDKa7L1Vgeaw5v7sZGy5IqQdCaw7qWjD11lFMaUC4vZdV34wpXy-_FCTY7y1ymMRPokNVnN3-Ze4rMjHIWTKYCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روی خون کودکانمان حساسیت بیشتری داریم
🔹
از انتقام خون شهدایمان صرف نظر نخواهیم کرد و بخصوص نسبت به خون اطفال و کودکانمان حساسیت‌ بیشتری خواهیم داشت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/687052" target="_blank">📅 23:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687050">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromزی‌ ویژن | zeevision</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4193564cfc.mp4?token=ItV96GLooMJfZnAtdoRwuvKB7dTJpS7cRN2fFAvMDv7fiplFo23ZAH-SX-8YtnYRVXk68QkFiK-ms2AjcvfjG39jjRus5KHulzBcSXWrROjDREzea2J3S1eYoSZ6AheUctIHhaylKJCFsr8s3LVougpa-Nm_sJotILL23T01TOcaViuf0O6Oxw9GoQmF4ERtTr_qLeK7aOaydPymysVGBwdv1EgHpd5GHYv3izZs6InrQN8eHGbRrGQvQ74KuOR4JTlS8yFvJ7AlFAqvYHwY9M2Wot2kCi75K5v_OCoydKF5UQYswzTe9cQZ6OpqmWqnUxin-z8kBaS9wg8VNmoBiB8YFJtTjLcLB0t9vWb8oUGz9j59iJ7jhgEksi1ehGwY7oyrur0yvUk_iJKBFyHLfXwTLZXCBf6NzXslV8U6LVyDD2ZLOl7c2dVKwqXVKmc4kKRpDBaA4JRmAMx77szsWUQVH-Tk67giH5QRQRPgPqUrQ9PtrloiIZukoPGg6AsQZSSBzrKDk8WwEAX-zEdyNU-arpTnFZnbEbJp6OBeN6NYH1sw3ZI6r85rwCwnP9IN9GEh39sQNnh4bDW6EKhMduoCFtMTJWL_8DloRSHaun9DPDmy6mR-eAbiaE9oUVld09kucc19Uvv30Al8KmG8Tjg4WtpYoRuGHW3yfeFWyIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4193564cfc.mp4?token=ItV96GLooMJfZnAtdoRwuvKB7dTJpS7cRN2fFAvMDv7fiplFo23ZAH-SX-8YtnYRVXk68QkFiK-ms2AjcvfjG39jjRus5KHulzBcSXWrROjDREzea2J3S1eYoSZ6AheUctIHhaylKJCFsr8s3LVougpa-Nm_sJotILL23T01TOcaViuf0O6Oxw9GoQmF4ERtTr_qLeK7aOaydPymysVGBwdv1EgHpd5GHYv3izZs6InrQN8eHGbRrGQvQ74KuOR4JTlS8yFvJ7AlFAqvYHwY9M2Wot2kCi75K5v_OCoydKF5UQYswzTe9cQZ6OpqmWqnUxin-z8kBaS9wg8VNmoBiB8YFJtTjLcLB0t9vWb8oUGz9j59iJ7jhgEksi1ehGwY7oyrur0yvUk_iJKBFyHLfXwTLZXCBf6NzXslV8U6LVyDD2ZLOl7c2dVKwqXVKmc4kKRpDBaA4JRmAMx77szsWUQVH-Tk67giH5QRQRPgPqUrQ9PtrloiIZukoPGg6AsQZSSBzrKDk8WwEAX-zEdyNU-arpTnFZnbEbJp6OBeN6NYH1sw3ZI6r85rwCwnP9IN9GEh39sQNnh4bDW6EKhMduoCFtMTJWL_8DloRSHaun9DPDmy6mR-eAbiaE9oUVld09kucc19Uvv30Al8KmG8Tjg4WtpYoRuGHW3yfeFWyIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁨ ⁨ ⁨ ⁨ ⁨ ⁨ ⁨ ⁨ «حالم از خودشو هر زنی که تو اون مطب رفت و آمد داره بهم میخوره…»
انتشار قسمت اول سریال «نیم رخ» فردا جمعه ۱۳ شهریور ساعت ۱۲ ظهر در
#زی_ویژن
📣
@zeevision
🌐
www.zeevision.ir</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/687050" target="_blank">📅 23:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687049">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اقدام جدید آمریکا علیه دانشگاه‌هایی که اسرائیل را تحریم کرده‌اند
🔹
مجلس نمایندگان آمریکا روز پنجشنبه لایحه‌ای را تصویب کرد که دانشگاه‌های شرکت‌کننده در جنبش بایکوت اسرائیل را جریمه می‌کند.
🔹
به گزارش گاردین، بر اساس این لایحه دانشگاه‌های شرکت‌کننده در بایکوت اسرائیل یا دانشگاه‌هایی که برای جلوگیری از مشارکت دانشجویان در برنامه‌های تبادل دانشجو با رژیم صهیونیستی شرکت کرده‌اند، جریمه می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/687049" target="_blank">📅 23:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687048">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoboDa8Ebgr8TLICbRf4VaAhy99rSZlmRoE_c5Yvp5G3N3hky3-v8xB2O8XPuF8-AnNWG-cwnvN28dzQao6RRj1PGpR5LZ5iQiYEZ3Nt68rzNefEuCbsQtgjDwlumtaWOzHvnDvGAo7rK0T1lPtUIeXDKZp_aK_ZWDdRGT7xwhWqa-wfq3mMVrKZWnUvzWCEuOf9Dxfwro_zsML7G-e2AXbla_ohq5_esqAglE8uGu7QGLU1i98GhtMQm7rvC4vBEJmH2tVBGCYPgqN-oGzQrQfYKfW571f7lLatvoiZ8MSHBUR7g9DBZ8DgSXi6FLvamCPgTDJ3GhovHqqSNTluew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت زیبا قره‌داغ ارسباران در تبریز
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/687048" target="_blank">📅 23:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687047">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مهمترین رفتارهای مجرمان در حوزه سایبری چیست؟
تبریزی، قاضی حوزه سایبر و فضای مجازی در
#گفتگو
اختصاصی با خبرفوری:
🔹
عمده رفتارهای مجرمانه در حوزه سایبری ناشی از کلاهبرداری رایانه‌ای، جعل رایانه‌ای و دسترسی غیرمجاز است.
🔹
بسیاری از هم‌وطنان فعال در این حوزه، با مبحث متا‌دیتاها آشنایی کافی ندارند.
🔹
برخلاف فضای سنتی، در حوزه سایبری مفهوم اعتماد به معنای رایج وجود ندارد و اعتماد باید در بستر داده‌ها و سامانه‌ها تعریف شود.
🔹
ریشه اصلی رفتارهای مجرمانه در این فضا، ناشی از خلاء‌های موجود در زمینه فرهنگ‌سازی است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/687047" target="_blank">📅 23:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687045">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/278fe1e4ed.mp4?token=hmt2vHgJVsSgJSGFhBNIGWT6aG3GlWQI7yPAgAGoLzrwAAZgim9fbzYwdsFfVHn7c7cJbPTfZnQg6oYUBkKOI4Z52xArtEKU0SwTWgryl12ePhEkPmU-c9FmLkTcfEO33ngRXDKl7Wm6hYlDDFyeLcokVxsAog_tCZARkdDHKxEclC55D8L2XQ7r29xLggSSKsfqFzpSrK9_kqKZ9dsmIQEaOANQN82wAot3Oi__zesS5i3Gg3OnCC0v_BWp3nJmsmbt5MRPjR5Wh9dbCHzCpSgNyGkZM2U2dqVMwjPlfEleiLfkVLgLQdtYnFyRG4VDXqTgPTRg-HlX5U659ND4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/278fe1e4ed.mp4?token=hmt2vHgJVsSgJSGFhBNIGWT6aG3GlWQI7yPAgAGoLzrwAAZgim9fbzYwdsFfVHn7c7cJbPTfZnQg6oYUBkKOI4Z52xArtEKU0SwTWgryl12ePhEkPmU-c9FmLkTcfEO33ngRXDKl7Wm6hYlDDFyeLcokVxsAog_tCZARkdDHKxEclC55D8L2XQ7r29xLggSSKsfqFzpSrK9_kqKZ9dsmIQEaOANQN82wAot3Oi__zesS5i3Gg3OnCC0v_BWp3nJmsmbt5MRPjR5Wh9dbCHzCpSgNyGkZM2U2dqVMwjPlfEleiLfkVLgLQdtYnFyRG4VDXqTgPTRg-HlX5U659ND4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلفی همسر عراقچی، دختر پزشکیان و فاطمه مهاجرانی| امروز
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/687045" target="_blank">📅 23:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687044">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c991d2b8f9.mp4?token=PWztu7J7k3eBgW96jydZs8pCDIRJIx2fjxlYWzIb9B-bbYC_8GNn4THz58Ip7cF0KPbhvkOfW84CSDXW788Rh6AMjNfH5P1hI7URzptYHWEnsexQrK2bSzxiDJcMkVja8ZKPQQrh54kYSboB0S9k7M18CfKwA3AmKIP7k8hfr-xryR9wf6uEyF7fLtX4GIOteZMhHnYJC7RCBYdDAjlrjIrSSWSAYwSIYM-MDb1GTWXJqPKcMCQxzibZTX8SRUysYQUReaLLYCrFgdj_xdHI5PqxSjCNYnv07kFDEXNgOxRJtIaeLvdC7za2_tuH9_yREKfoPtWy2FXNMZZcFJQLrbDpjWnaJCTuXIcELFbjrjDuM2y_1jHrND0F-5VGCNrn_3rholkJtf8tr7Z6Prx_dk8Vl9serruC2mifDaiv6r8OtkI7pV-kUfewrD8TRf3OHfVQj1oE0w6eQZ4PwYKB3C8wHyEPMQIUImdbvya4j4nhiGQvPcvbasb4nyG1sQEhFosfD0kRRx0PDGLy5PkM0n9I4lXEdbIoLVuyY0aRhdKHSorOb0qwZt2_tYnHRn1XfNazVhfnMwKQ_bAbqf00vB7ZP4Rr6I9C-JuODlKXZZ-rWnWnoP9p7t0ssgZRLhBD7lu_dGGv51F-bcTbdd6_cksfR7RtxX1NneGfidAAL-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c991d2b8f9.mp4?token=PWztu7J7k3eBgW96jydZs8pCDIRJIx2fjxlYWzIb9B-bbYC_8GNn4THz58Ip7cF0KPbhvkOfW84CSDXW788Rh6AMjNfH5P1hI7URzptYHWEnsexQrK2bSzxiDJcMkVja8ZKPQQrh54kYSboB0S9k7M18CfKwA3AmKIP7k8hfr-xryR9wf6uEyF7fLtX4GIOteZMhHnYJC7RCBYdDAjlrjIrSSWSAYwSIYM-MDb1GTWXJqPKcMCQxzibZTX8SRUysYQUReaLLYCrFgdj_xdHI5PqxSjCNYnv07kFDEXNgOxRJtIaeLvdC7za2_tuH9_yREKfoPtWy2FXNMZZcFJQLrbDpjWnaJCTuXIcELFbjrjDuM2y_1jHrND0F-5VGCNrn_3rholkJtf8tr7Z6Prx_dk8Vl9serruC2mifDaiv6r8OtkI7pV-kUfewrD8TRf3OHfVQj1oE0w6eQZ4PwYKB3C8wHyEPMQIUImdbvya4j4nhiGQvPcvbasb4nyG1sQEhFosfD0kRRx0PDGLy5PkM0n9I4lXEdbIoLVuyY0aRhdKHSorOb0qwZt2_tYnHRn1XfNazVhfnMwKQ_bAbqf00vB7ZP4Rr6I9C-JuODlKXZZ-rWnWnoP9p7t0ssgZRLhBD7lu_dGGv51F-bcTbdd6_cksfR7RtxX1NneGfidAAL-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه: دولت فراتر از حد قانونی هم به بودجه نظامی کشور کمک کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/687044" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687043">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای نتانیاهو: ارتفاعات علی‌الطاهر لبنان دیگر تهدیدی برای ما نیست
🔹
نخست‌وزیر رژیم صهیونیستی، مدعی شد ارتفاعات علی الطاهر در جنوب لبنان دیگر تهدیدی برای اسرائیل محسوب نمی‌شود.
🔹
وی همچنین مدعی شد که نظامیان صهیونیست، شمار زیادی از «شبه‌نظامیان» را در این منطقه از بین برده‌اند.
🔹
ارتش رژیم صهیونیستی ساعتی قبل مدعی شد که به‌صورت عملیاتی بر زیرساخت‌های وابسته به حزب‌الله در ارتفاعات «علی الطاهر» در جنوب لبنان مسلط شده است.
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/687043" target="_blank">📅 23:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687042">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
۱۱ همت پول حقیقی در یک هفته از بورس خارج شد
🔹
معاملات دومین هفته شهریورماه در بورس تهران با وجود تداوم ریسک‌های سیاسی، با رشد ۱.۸ درصدی شاخص کل به پایان رسید و این نماگر در ارتفاع ۶ میلیون و ۵۰۴ هزار واحد ایستاد. در سوی دیگر اما جریان نقدینگی حقیقی معکوس شد به‌طوری‌که بیش از ۱۱ همت پول حقیقی از بازار خارج شد.
🔹
در این میان، صنایع محصولات شیمیایی و حمل‌ونقل بیشترین جذب نقدینگی را داشتند و صنعت دارو و صندوق‌های سرمایه‌گذاری با بیشترین خروج پول حقیقی مواجه شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/687042" target="_blank">📅 23:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687041">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ساعت کاری جدید، شنبه ۱۴ شهریور اعلام می‌شود
حسین رحمانیان، سخنگوی سازمان اداری استخدامی کشور در
#گفتگو
با خبرفوری:
🔹
بخشنامه مربوط به تغییر ساعت کاری روز شنبه ۱۴ شهریور، یک روز پیش از پایان مهلت بخشنامه قبلی توسط سازمان اداری استخدامی اعلام خواهد شد.
🔹
آیین‌نامه دورکاری نیز در راستای مصرف بهینه انرژی و مدیریت منابع کشور، آماده شده و پس از بررسی نهایی، پیش‌بینی می‌شود طی یک تا دو هفته آینده به تصویب هیئت وزیران رسیده و اعلام شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/687041" target="_blank">📅 22:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687040">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbLaqNh5mwOuBz0N-TBGcyA1EmYxSZUMritaUh4qLqdpkovBsgiWWEK4cYmdg0JUF_Hrovb3hvBVz4jmV6hlVZhb3ZRBEOlrxjjzIdurHfI7C8-P5ciqBXN1WGZTgq6EtoDXvgHc5LWDQWvhnqeoh1gPiMpO70uQzn-W-QxYyfo9l-ruX6it82LESD-tlm2mSw4rE9gQxeUFKstVuQWP3tA9AZrnQDAcfenEQboIfSllaCVdlRFTsnR9Z3EVSWOmo3nRnwNEXjY80ZhzJxMJG0BhJSvqy8Q9L1f5FWUf10wh_mXy3NccLGg43cwcddjhSkr5tSTTGBQMq_4w1Dns_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این زن مرموزترین جاسوس تاریخ است/ چگونه ملکه مخبر شد؟
در این گزارش با یکی از مرموزترین جاسوسان زن تاریخ آشنا خواهید شد
👇
khabarfoori.com/fa/tiny/news-3242281</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/687040" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687039">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aaae49984.mp4?token=rSpjsXWdPRCOrwfuH3krxRnEec8poZgVJFp1XrnAiDVWJKWF6LeUyHxprKItZkDsMTfmpPg1ix8Y8rOKbMfYOcqMvjgcaMX7c8X1F-7cVsaSH-oVXQx_GDvGUsnJCB2-L9xJ5xglnoI6v8XsRakrViT44PwPb0Q-OAgP8WAY_oCBxeTjt0q1SBZdvdoyZxzV9ZrcGRgIFvu6EYJPjGZhjBvGLuqS5hg7o9CvtPnNS_zUiNp0pc5d_p6xarXkubHPpqO2PdE8ws1JbXn3b6fkHj-YJIAhlrWdv63Plofc3VLcUCBKfJUc3mAdn8RV51z22ScRskhr3nbib4uFlS2U6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aaae49984.mp4?token=rSpjsXWdPRCOrwfuH3krxRnEec8poZgVJFp1XrnAiDVWJKWF6LeUyHxprKItZkDsMTfmpPg1ix8Y8rOKbMfYOcqMvjgcaMX7c8X1F-7cVsaSH-oVXQx_GDvGUsnJCB2-L9xJ5xglnoI6v8XsRakrViT44PwPb0Q-OAgP8WAY_oCBxeTjt0q1SBZdvdoyZxzV9ZrcGRgIFvu6EYJPjGZhjBvGLuqS5hg7o9CvtPnNS_zUiNp0pc5d_p6xarXkubHPpqO2PdE8ws1JbXn3b6fkHj-YJIAhlrWdv63Plofc3VLcUCBKfJUc3mAdn8RV51z22ScRskhr3nbib4uFlS2U6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ: اروپایی‌ها به‌صورت علنی از ما انتقاد می‌کنند اما در خلوت به ما می‌گویند اگر آمریکا در مقابل ایران کاری نکند، هیچ‌کس دیگری در جهان قادر به مقابله با ایران نیست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/687039" target="_blank">📅 22:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687038">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0963adeb1a.mp4?token=A7flAZcu7U8eLICWPhzLjaUcYQehFAAEB0Y92i2avnin4xVfvgpS2y7zdu9WAQ9Dn_LQhRbThCtUpSlJaRxFVYVRAbrLfI5fY6JhDzQY8iw5U4s1hnkMZjgsGCwAw3JbPgYPkVCCDtehmTw-uMmF5vKcLLO9xg99GxFHHP9gVz7wcuUlxwufQpxlwCBeKdQw90hGyUZRjoCgVt46-5fIOsHk2JAwmwPdbyDWV5ICg9E5potehKZv2yc26g3a8IQ-_4Lah2j5KDH6ooxdl7EkMxcifgK-t_-fG-HkAoW2O1xyVPxeOR1mHiUsrjXqDvgAvb20s5jNHLwLFwz-LQ8mPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0963adeb1a.mp4?token=A7flAZcu7U8eLICWPhzLjaUcYQehFAAEB0Y92i2avnin4xVfvgpS2y7zdu9WAQ9Dn_LQhRbThCtUpSlJaRxFVYVRAbrLfI5fY6JhDzQY8iw5U4s1hnkMZjgsGCwAw3JbPgYPkVCCDtehmTw-uMmF5vKcLLO9xg99GxFHHP9gVz7wcuUlxwufQpxlwCBeKdQw90hGyUZRjoCgVt46-5fIOsHk2JAwmwPdbyDWV5ICg9E5potehKZv2yc26g3a8IQ-_4Lah2j5KDH6ooxdl7EkMxcifgK-t_-fG-HkAoW2O1xyVPxeOR1mHiUsrjXqDvgAvb20s5jNHLwLFwz-LQ8mPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ونس: ترامپ شخصاً با رئیس‌جمهور چین صحبت کرده که به ایران امتیاز خاصی اختصاص ندهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/687038" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687037">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
خبرگزاری ایتارتاس روسیه: ایران برای نبرد بلندمدت و فرسایش نیروهای امریکا آماده است؛ ایران زمان و مکان مقابله با آمریکا را مشخص می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/687037" target="_blank">📅 22:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687036">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5368d3b591.mp4?token=dxvmmGsMAq_ED2sWoNMl9yDWATkLNFVqOfn6dDeMdi4Q8-uIeEfYJ5jRGrIdY2jdx-YdbCCw_glnTpuBDj5fCfR3iL3vBX6LrX0cKnLlpJOOXJ7GT-KrHvg9bkk1jqX1svxU_9nswG4HAZbo11b7iWKupi9TpcArUExkR7DPJzaogJaksYT7RDTPZXz3dswSFPrOwvAdfDfZv02_sNJ0G9vlW28-EkdAVFt7EUUDOTTpuIuzVfFntbX1tOy4xRzXn3_hUp5R5SCj5FBMU97vpP3KqZ1lb1cdYMpaCZ50cI0zOGbuIcuFy9I33f7kwRTJvx83WhUmCw4cPytoe-bs2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5368d3b591.mp4?token=dxvmmGsMAq_ED2sWoNMl9yDWATkLNFVqOfn6dDeMdi4Q8-uIeEfYJ5jRGrIdY2jdx-YdbCCw_glnTpuBDj5fCfR3iL3vBX6LrX0cKnLlpJOOXJ7GT-KrHvg9bkk1jqX1svxU_9nswG4HAZbo11b7iWKupi9TpcArUExkR7DPJzaogJaksYT7RDTPZXz3dswSFPrOwvAdfDfZv02_sNJ0G9vlW28-EkdAVFt7EUUDOTTpuIuzVfFntbX1tOy4xRzXn3_hUp5R5SCj5FBMU97vpP3KqZ1lb1cdYMpaCZ50cI0zOGbuIcuFy9I33f7kwRTJvx83WhUmCw4cPytoe-bs2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخاستن ستون‌های دود از منطقه «الشعله» در بغداد
🔹
منابع محلی در پایتخت عراق از مشاهده ستون‌های غلیظ دود بر فراز منطقه «الشعله» در بغداد خبر دادند.
🔹
هنوز علت دقیق این حادثه و میزان خسارات احتمالی آن مشخص نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/687036" target="_blank">📅 22:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687034">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشرکت پتروشیمی پردیس</strong></div>
<div class="tg-text">نسل‌ها می‌گذرند، اما جهاد در این خاک، قصه‌ای از جنس ایستادگی‌ست..
روزگاری تنگستان سنگر مقاومت بود؛ امروز، هر جایی که ایرانی برای سربلندی این خاک می‌ایستد، سنگر دیگری‌ست؛ از دفاع و امنیت تا تولید و آبادانی.
۱۲ شهریور، روز مقاومت و ایستادگی، گرامی باد.
🇮🇷
🎬
نسخه با کیفیت ویدیو:
aparat.com/v/wwqj4n4
اخبار و رویدادهای ما را در کانال رسمی پتروشیمی پردیس دنبال کنید:
👇
👇
👇
🆔
@ppc_ir</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/687034" target="_blank">📅 22:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687033">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42091f30d8.mp4?token=vg1Nccij3DzD_tAG9ITyBKgGlX3ES1mDMjTo2WjGCfmZeJ_V_1pdDeZSq6n5UvS8eN_dkfkU-yoYHioZnV2sgPC93KnRl1iNDr6hmnKNMi8Yuh7wj58Sdi2tuHadjKfm-oixbE181diVn-tIIyjznkgVVqhhnVGodf7-vSpm5P_CNi-t3Cwoy63i1wpEGaoit2CBCJZ9DAC8E6yz3bSZWhCo2uupGzg_f8_vUtetbIClE7u4uHkjGOHybdeST60rs05u5fi4SzgG73c7Gv6MXSf4Ngl0cYVTW6GXtt1bln04LgW5yYn9QxJMUFzBQ6UIL-Ya0ORh-f6CwIALZkzYeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42091f30d8.mp4?token=vg1Nccij3DzD_tAG9ITyBKgGlX3ES1mDMjTo2WjGCfmZeJ_V_1pdDeZSq6n5UvS8eN_dkfkU-yoYHioZnV2sgPC93KnRl1iNDr6hmnKNMi8Yuh7wj58Sdi2tuHadjKfm-oixbE181diVn-tIIyjznkgVVqhhnVGodf7-vSpm5P_CNi-t3Cwoy63i1wpEGaoit2CBCJZ9DAC8E6yz3bSZWhCo2uupGzg_f8_vUtetbIClE7u4uHkjGOHybdeST60rs05u5fi4SzgG73c7Gv6MXSf4Ngl0cYVTW6GXtt1bln04LgW5yYn9QxJMUFzBQ6UIL-Ya0ORh-f6CwIALZkzYeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف ونس: ما باید نسبت به حملات سایبری ایران واقف باشیم
🔹
چینی ها نیز خواستار عدم حمله ایرانی ها به کشتی ها هستند! کشورهای منطقه همه خواستار تنبیه ایران هستند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/687033" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687032">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
انکار مضحک معاون ترامپ در خصوص حمله به مراسم عروسی در سیریک
🔹
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در اظهاراتی ضمن انکار اطلاع از حمله هوایی به مراسم عروسی در «سیریک»، مدعی شد که ارتش تروریستی آمریکا هرگز غیرنظامیان را در نبردها هدف قرار نمی‌دهد؛ ادعایی که…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/687032" target="_blank">📅 22:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687030">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHG5WTqGzLqFMZz9udr_nK5fe47Odpx0U56T2-6pPRmdAYUAqPWgbAL_t0k3jyIWRa3Dh0b0Rk8Dw-HDYVLyhKJcjTNE3SuZGUj7nZRZ_Q9_w3UNdtm77PGeE83-E8ecnUAIZ1kw_xwEdsKgtmMB7TAMugM0ofoMopSIBZYuMW7_mvFyrGRmvGq17j1OnnCqK4KWWGKBvwUbqSHufOIjeciMfaPyi-EQNkcIZcWrUS4D-LtrwoPOAJBIGtyRsk2w5CSDXcSI79zLDChhnxZcYxMdHzaLzWDAyRdBGKDzaQSUZk8k1ei01AEbqlFnFW_TP3iazdhfmRgxqFKbcvFMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nztHBP5kw62tam6D9citLNTrHYg0KD_EeU0sSwZkwYEmn32qEvUKk1CPMpyEio2BLXTZ89rEMpVm499qnEh6iVwu9po7wwRGyIQ4iUrVThFjITXUzywYV8jX0tqHEUSwYwRLc4zFfgt3dNf0sJ3_Faj1S1OIjlgTp4y0S19TF7i4KAXLOZRsPpjdHSzsnEd--1QMrfvBNjHecOdkSdoKxvmS66vn68vQSrXYrrrC717BqPm9nJHq3bU_KDQelM-5C1cG6Bz91wBgXQqThRCTtRUWRpQ_G-MXBmedSDBuvpYQvX3f9luRslrb1-XHFtgC6yR8VgIpRZvV8aA3wODYbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مردان و زنان در چه سنی بازنشسته می‌شوند؟
🔹
آمارهای سازمان همکاری و توسعه اقتصادی (OECD) نشان می‌دهد میانگین جهانی سن بازنشستگی برای مردان ۶۴.۷ سال و برای زنان ۶۳.۶ سال است.
🔹
کشورهای شیلی، کره جنوبی، ژاپن و آمریکا با میانگین سنی ۶۶ تا ۶۹ سال، بالاترین سن بازنشستگی را ثبت کرده‌اند.
🔹
در مقابل، ایران با ۵۱.۵ سال برای مردان و ۵۱ سال برای زنان، در کنار عربستان ۴۷ سال در پایین جدول قرار دارد و سن بازنشستگی در آن فاصله زیادی با میانگین جهانی دارد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/687030" target="_blank">📅 22:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687029">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور آمریکا جی‌دی ونس: از وقتی که من زنده‌ام، ۴۲ سال اخیر، آمریکا جنگ‌های زیادی را پشت سر گذاشته است
🔹
ما تقریباً در هیچ‌کدام از آن‌ها پیروز نشده‌ایم تا اینکه دونالد ترامپ رئیس‌جمهور شد، قیمت سوخت در آمریکا بالاتر رفته، اما در سایر مناطق جهان بدتر است.
🔹
ناتوانیِ مضحکی از متحدان اروپایی‌مان در انجام هر کاری برای کمک به حفظ عرضه انرژی جهان دیده‌ایم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/687029" target="_blank">📅 22:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687028">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DulTvq8g16RtMLe5jFu2Prf4sHYRuWHPeP0RUN_EMGTO1HgohXxQrFnHi-WRxmLLTMDO5V-1Cd3bWuG6Sp44Pa0M8ykkGQkDzg0RM2HzEwncp0xByj-VwdPoDk0bBDwHbFcTahaXLw0SRH18Een3MkS_30C4eL8MRiIAXD5a1P4AmqXLyz3-UalkIn_xILfkczVA6S0xz66jMy4g-qlVXeYi_6UL1wVMSoNImmFwUHdWw_E9mvApMrD_4xL2ZCIS481rkWG_rQIK-TRv5nZ1rxlxrlZeVTW8LjH7seqV30LKBMtTIevdXJSdimDLxLZ71ZGOIyxPr_BFancN_cEwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر رسمی «کنسرت‌نمایش سیاوش» منتشر شد
🔹
بهرام رادان در نقش «سیاوش»
شهرام حقیقت‌دوست در نقش «گرسیوز»
آزاده صمدی در نقش «سودابه»
الهام نامی در نقش «فرنگیس»
رایان سرلک در نقش «کودکی سیاوش»
سروش کریمی‌نژاد در نقش «ناخدا»
مونا صوفی در نقش «اشکناز»
سارا پارسایی در نقش «آفرین»
شاهرخ پیمانی در نقش «آذرخش»
با هنرمندی مهدی سلطانی در نقش «رستم»
و با حضور علی زندوکیلی در نقش «سروش»
🔹
استادیوم تنیس باشگاه انقلاب از نیمه دوم شهریورماه میزبان این رویداد نمایشی خواهد بود و فروش بلیت آن به‌زودی از طریق سامانه ایران‌تیک آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/687028" target="_blank">📅 22:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687026">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA6Npfyd4TlEaGwM7Q8SCtKw9JABZXjZEHv524uvvtCDM1HurYaJu69XfAEdhAszJFrm94x0hKHFe7WPxJPbJOnvzvGUbxO1ErnQ9YK9u-gd11FqkzQwhyzxhrOnS97nXuBZvmmx_86Jaj2kY6XAyRwMAdiKW_Un0non4xqCY3ZW3iMEp5aKTNjlbdjvYti3f1sI2suPkEQRSU3lbih83wtICp7UbIT6fttGmzKQWXgIucH4oo5FnJMAg1pOOT--VBciCAWe_45pTDEWlikOqYs6fi9WKzaMpE2QRvBXrP_OSS73ZwfSiBhwkK3zWaSoCQdH4nirmnDkN7FbIKMwAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بده بزنیم
🔹
میزان واکسن آنفلوآنزا در داروخانه‌های کشور در شرایط خوبی قرار ندارد و طبق اعلام سخنگوی انجمن داروسازان ایران، این میزان حتی تا به مهرماه نمی‌رسد. سفارش این واکسن از ماه‌های قبل باید صورت می‌گرفت، اما به دلیل بسته شدن مسیرهای انتقال ارز و دارو، سازمان غذا و دارو به موقع سفارش واکسن نداده است. با توجه به نزدیک شدن فصل سرما و شرایط خاص فعلی مانند، عدم وجود مواد اولیه کافی و واردات نامناسب، این شرایط نیازمند ورود جدی و سریع دولت است.
🔹
هشتصدوپنجاه‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/687026" target="_blank">📅 22:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
یارانه برق متخلفان یک سال قطع می‌شود
اطلاعیه شرکت توانیر:
🔹
استفاده‌کنندگان غیرمجاز از شبکه برق از جمله استخراج‌کنندگان غیرمجاز رمزارز، دستکاری‌کنندگان کنتور و مصرف‌کنندگان برق خارج از مجوز، به مدت یک سال از یارانه انرژی محروم می‌شوند و بهای برق مصرفی آن‌ها بر مبنای تعرفه آزاد محاسبه و دریافت خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/687025" target="_blank">📅 22:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km-6ur_JpLHlyRhz2_uqwKmD3Lq9R4l6OQ6xA99wu5vL-cDl1hh-t8P8g3HXyJyKRxRcCvrl6G2qBHqBi_6UDFXXIPFL1U6IUK_8ulkjDJrueM8yXlB3XWTxykUWCq4mG6wf6CNZgW7ODmh9SWcrPGbJFOHNnyLO62EcQ0133B2kovpWsu9ZQZH7v4tRFk0u45wzDD-aa6j9SNcVxPGb5aPY1E_sIYbi50aFGXEn0kmGNlw6AqBr0nSRtaJY_hazbizRa-Q-ZiRPx9k4bmRH1NNgpyD_Rf6QlqOnY1lNkGqRVnCNnLAZTfykRvNpDLgO4MErs8BT2gb94-N-yzt0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت ۴ نفر از رزمندگان هوافضا در کرمانشاه
🔹
روابط عمومی سپاه استان کرمانشاه در اطلاعیه‌ای از شهادت ۴ نفر از رزمندگان جان‌برکف هوافضای سپاه استان کرمانشاه در حمله رژیم سفاک و تروریستی آمریکا خبر داد.
🔹
اسامی شهدا: شهید رضا محمدی، شهید شهرام جعفری، شهید علیرضا…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/687024" target="_blank">📅 22:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687023">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLlhNtQfkdPDX7K5SEpRe3EyY3xayQRhkRaX9G5-6yguYLKj1uZW5dt3JrpTY05B3MksN0c2zTh7VF8zGAKAwm4uUSiaRgIDMSAdLdksCkJkAOzY0lAaFBe9njAo_5B76PUWxuNVALij4wrxGJMvTKufX5uBWY6f1lP5D2y7PmE-8B9wA08JK0X-TeBH9-ZE92gMImaZSsFz65sF_6q1e7fguWE-a8ZwpH6dylko1lwa2rVBqeQ6Vifln2iM4v83mxMoz12VOLJiU3p6QGa7Jx4aYo7V96fDthr3Go34HStrZzFimQU9EORv84781b4MooMu-bWXcowhNYNtCYGZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر پایانی، پایانِ راه نیست؛ گاهی تلخیِ امروز، مقدمه‌ی شیرینیِ فرداست
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که هر کاری سرانجامی دارد؛ گاهی نتیجه‌ی یک اتفاق تلخ است و گاهی شیرین. مهم این است که در فراز و نشیب زندگی، امید و صبر خود را از دست ندهیم. #…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/687023" target="_blank">📅 22:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687022">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtmyH7zSsx2h2DM2SS-_zKgnr3OS5aXe1UeFGIMGCDONbPYPI5A8lIwBoNRzjmzFe9rUUGl-4ujBpw6qjlVTv5b9eB0l2qEPmJeeqyEor4EK61LqC3tcfgs5MseT85njnBzgHlWF8ADO5EtsmpCH8owLF3TlvKYAy1izE4lh3g2asLDzvOgGjfNapBAQmQBvo-yeP4gdDDbSc2Kao9HVfxUgJwRVYC3J44u3oIcTDMhs2IvSRxIEIYUBOxt5EhHFqL7P25oFtvWxGQsJAFayv8RTH-neDOeDjRBaKPH2_wqSTeO1xw67RwA4IoYd2ijmuznihLgIziCbGhraZ8FoCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون علمی رئیس‌جمهور: دیگر فقط اکوسیستم نمی‌سازیم؛ می‌خواهیم سقف فناوری ایران را بلندتر کنیم
🔹
حسین افشین، معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، در
نشست با نخبگان و مستعدان چهارمحال و بختیاری
از رویکرد جدید معاونت علمی برای توسعه زیست‌بوم فناوری گفت.
🔹
«ما علاوه بر ساختن اکوسیستم، به دنبال بالابردن سقف اکوسیستم هستیم.»
بر همین اساس، تعداد شرکت‌های با درآمد بالای یک همت از
۷۹ شرکت در سال ۱۴۰۳ به ۱۱۷ شرکت در سال ۱۴۰۴
و شرکت‌های بالای ۵ همت از
۸ به ۱۷ شرکت
رسیده است.
🔹
افشین:
«ما به دنبال قهرمان‌های فناوری کشور هستیم.»
او همچنین فناوری را به موج تشبیه کرد و گفت:
🔹
«فناوری مثل موج است؛ برنده کسی نیست که از موج سریع‌تر باشد، بلکه کسی است که آن را زودتر ببیند، آماده‌تر باشد و در زمان مناسب و موقعیت درست روی آن سوار شود.»
یعنی در فناوری،
زودتر دیدن، آماده‌تر شدن و به‌موقع وارد میدان شدن، رمز برنده شدن است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/687022" target="_blank">📅 22:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687021">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeHwKYtg5inKUMSwTNopS-bX1sbBP6xlAXxGfgyPBmLyQ_ZRXeTAULq981_F-qqFQPGB21VcQEcTuGUo-19Jc32tLM23VJ88CcAwPwsr5BVDCn9QUJ_jjIA7dKq8lrvr4QAcjEc1F3GRZv0DO9IRWOw-OjLfRji6kbPpfTK2HLd9WBmUz5xrwNqVF6GqxW7ClyPldPvtqzeWT8oVB4-7Y24Uq0oZ1WKmpd3byqcv3BkSqXLZCeOnwfLJej-8LixBhSZcHOt0AH9_bXem-ufNgZOAVQUagtlEJ6rcso6mxoIsMB2WIK4ROAr1GWYTTWdOovbx09H0e8A-cQST0p-ZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
فقط تا جمعه ۱۳ شهریور فرصت دارید
!
✅
طبق اعلام بیمه‌مرکزی تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه، به‌طور کامل بخشیده می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو با
بیمه‌بازار
تمدید کنید.
✔️
تا 2میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/687021" target="_blank">📅 22:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687019">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be6859d2b.mp4?token=e06C6C0g-a5lA0W-SLKc1h78w7pUnQ82ZNrweT_zzN_rlk5-jVgHOakxz_VAkcK3I_PVxTGRPsJp4632qOvB8LdJAskWCJWKDF7zA2p4OU2Py5Ogch_58zREPe0o8WgZjlj_HOst36G-ztOI4UJjjE54IsyFRGpTmAvhLPpr78-wk7C-I7tDcHBNgnAV13IFZzrB4abWXAqu8ueWqUyGMBTN1oq8GC-RoZP6SGAqiXF5sAdmLv-R0FK99gI6mfEWWn3z2B2pAvXnY7e62Sf1E7vt5DUk8JL554HxFLv0OCMa78s-NtiD3bdfJ7p5y0tbmWD5Z7ebfw18wiHGQVkuhSr0UEHYIwgPAQrsziC6KlzNpEWwAjtpHpLAGbXUIPpnXmIyRQ9fnFxLzZvghx6cVS7k6a8P-kErZjDOHCFT0f56g2WOM2XpXCpqeD-RsgJLgPGdVk3PsANiBkfGUXfzTX5mJNHwHzAN_eARsMXDerqBgc_a5WaJDHNK1UR8Buah1I1beA9UsY9nEo0VaiJUV2FTO5QgCTNX87xyy3gZu9g1E1sMYEWUPVxb8qZcseivoILhCGqai7YTqFov3ZkBIPQsO7Hav3hFGaHKGJbBMBTdj_oB4Dp9F46UYPixL7jeLwLXzuuTRZsoC31g3lvzNC3MMhoIwklta_boySAfW3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be6859d2b.mp4?token=e06C6C0g-a5lA0W-SLKc1h78w7pUnQ82ZNrweT_zzN_rlk5-jVgHOakxz_VAkcK3I_PVxTGRPsJp4632qOvB8LdJAskWCJWKDF7zA2p4OU2Py5Ogch_58zREPe0o8WgZjlj_HOst36G-ztOI4UJjjE54IsyFRGpTmAvhLPpr78-wk7C-I7tDcHBNgnAV13IFZzrB4abWXAqu8ueWqUyGMBTN1oq8GC-RoZP6SGAqiXF5sAdmLv-R0FK99gI6mfEWWn3z2B2pAvXnY7e62Sf1E7vt5DUk8JL554HxFLv0OCMa78s-NtiD3bdfJ7p5y0tbmWD5Z7ebfw18wiHGQVkuhSr0UEHYIwgPAQrsziC6KlzNpEWwAjtpHpLAGbXUIPpnXmIyRQ9fnFxLzZvghx6cVS7k6a8P-kErZjDOHCFT0f56g2WOM2XpXCpqeD-RsgJLgPGdVk3PsANiBkfGUXfzTX5mJNHwHzAN_eARsMXDerqBgc_a5WaJDHNK1UR8Buah1I1beA9UsY9nEo0VaiJUV2FTO5QgCTNX87xyy3gZu9g1E1sMYEWUPVxb8qZcseivoILhCGqai7YTqFov3ZkBIPQsO7Hav3hFGaHKGJbBMBTdj_oB4Dp9F46UYPixL7jeLwLXzuuTRZsoC31g3lvzNC3MMhoIwklta_boySAfW3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی پر بازدید از تلاش مامورین پلیس و حراست بیمارستان برای دستگیری یک قاتل فراری در شاهرود سمنان
#اخبار_سمنان
در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/687019" target="_blank">📅 21:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687018">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
معاون ترامپ برنامه آمریکا تسلیح مخالفان جمهوری اسلامی ایران را رد نکرد
🔹
جی‌دی ونس، معاون رئیس‌جمهور آمریکا،  در پاسخ به سوالی درباره حمایت از گروه‌های مخالف جمهوری اسلامی ایران، از وجود برنامه‌های متعدد خبر داد و تأکید کرد که دونالد ترامپ گزینه‌های متنوعی…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/687018" target="_blank">📅 21:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687017">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ونس: ما می‌توانیم منطقه را ترک کنیم اما کشورهای عربی حاشیه خلیج فارس به ما می‌گویند: این بدترین اتفاق ممکن خواهد بود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/687017" target="_blank">📅 21:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687016">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس: همه گزینه‌ها برای مقابله با ایران روی میز است
🔹
معاون رئیس‌جمهور آمریکا اعلام کرد برای توقف اقدامات ایران، تمامی ابزارهای اقتصادی، نظامی، دیپلماتیک و پنهان در اختیار رئیس‌جمهور است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/687016" target="_blank">📅 21:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687015">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d45284fd8.mp4?token=IWQML9DYW3IGxQf0wlmuTf91FOmia3vX8Zy2pr353Bp-pLjbbDm2KMAM3Pl8DSvXC2VdHw_0r075uJgnX2vEcour9hG-iLAuf7q9KxqmAMPOymFx_6gafojOggmtyFx-7BDz79CkHlt49dRiZxy0UJvTHTJim-1XUW0ceD55-ICaNdTtsgudy-sCXRuNkvaHh-iQBIkyrU8MPx4hoyNX6Z2IXcivGr9aKkpPH1EIfwTzcCb70qKi5aAD92l2ceh6c6IeQRAlroZxghtPcjjw87mzudFHfNHMObapEpCFXyWw4jR4PeQN6gXt3sajG6ktGSxCmzQ3N36f7biRmgLjQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d45284fd8.mp4?token=IWQML9DYW3IGxQf0wlmuTf91FOmia3vX8Zy2pr353Bp-pLjbbDm2KMAM3Pl8DSvXC2VdHw_0r075uJgnX2vEcour9hG-iLAuf7q9KxqmAMPOymFx_6gafojOggmtyFx-7BDz79CkHlt49dRiZxy0UJvTHTJim-1XUW0ceD55-ICaNdTtsgudy-sCXRuNkvaHh-iQBIkyrU8MPx4hoyNX6Z2IXcivGr9aKkpPH1EIfwTzcCb70qKi5aAD92l2ceh6c6IeQRAlroZxghtPcjjw87mzudFHfNHMObapEpCFXyWw4jR4PeQN6gXt3sajG6ktGSxCmzQ3N36f7biRmgLjQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
جی‌دی ونس: همه گزینه‌ها برای مقابله با ایران روی میز است
🔹
معاون رئیس‌جمهور آمریکا اعلام کرد برای توقف اقدامات ایران، تمامی ابزارهای اقتصادی، نظامی، دیپلماتیک و پنهان در اختیار رئیس‌جمهور است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/687015" target="_blank">📅 21:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687014">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ونس بار دیگر مشکلات کنونی آمریکا را گردن دولت قبلی انداخت: تورم آمریکا نتیجه سیاست‌های دولت بایدن است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/687014" target="_blank">📅 21:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687013">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ونس بار دیگر مشکلات کنونی آمریکا را گردن دولت قبلی انداخت: تورم آمریکا نتیجه سیاست‌های دولت بایدن است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/687013" target="_blank">📅 21:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687011">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
به هوش مصنوعی باید شخصیت حقوقی اعطا کنیم ؛ ورود قوه قضاییه به هوش مصنوعی
دکتر تبریزی، قاضی حوزه سایبر و فضای مجازی در
#گفتگو
با خبرفوری:
🔹
هوش مصنوعی بیش از آنکه تهدید باشد، فرصتی است که اکنون به عنوان دستیار هوشمند قضایی در محاکم مورد استفاده قرار می‌گیرد.
🔹
ما در حال حرکت به سمتی هستیم که به هوش مصنوعی شخصیت حقوقی اعطا کنیم؛ موجوداتی که آن‌ها را «اشخاص الکترونیکی» می‌نامیم.
🔹
قوه قضاییه به عنوان یک دستگاه نظارتی و حاکمیتی، مسئولیت‌های متنوعی دارد که نخستین گام آن پیشگیری از وقوع جرم است؛ حوزه‌ای که هوش مصنوعی با ورود به میدان عمل و کاربرد، نقشی تعیین‌کننده در آن ایفا می‌کند.»
@Tv_Fori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/687011" target="_blank">📅 21:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687010">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
پاکستان از کشته شدن ۱۵ شبه‌نظامی در مرز افغانستان خبر داد
🔹
ارتش پاکستان در بیانیه‌ای اعلام کرد که نیروهای امنیتی این افراد را که از آن‌ها با عنوان «تروریست‌های وابسته به فتنه الخوارج تحت حمایت هند» یاد شده و قصد داشتند از مرز پاکستان و افغانستان نفوذ کنند، شناسایی کردند.
🔹
در این بیانیه آمده است: «در نتیجه یک درگیری دقیق و ماهرانه، ۱۵ شبه‌نظامی کشته شدند، اسلام‌آباد از اصطلاح «فتنه الخوارج» برای اشاره به گروه طالبان پاکستان استفاده می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/687010" target="_blank">📅 21:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687006">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEX8qG45tTh5AT5u1WqomTmpkPc6DcP-13yz8SjRr_JGM8KawcB6RmqxxNydK7xNzwTtHtDP7kgA6p3KlaqFeTwSpRdur2y5lORjVncjewCfE0VWvWgCqNZvSqcOegahRNA_r-83ABSULTdI8cdNVCrwIySXodEAveOQjjwfc1-__3xfsrhIrWQfgSDMKUUnGa54lK1ysQs3EgcVXatgNWIGXGfq4XKk3jbFWbdFPeyO_06-GGHETCsyMg_KTGg98wnNWkBqitYS9MVP8Y0wggu7BYy7BKZKBnihNTuYvh5nrm4PbACwqa7BUfUmnPgrtX9vVSfL9eRBJ2UtU6M9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kwori_XtQ5Fc7ciI1zxYRjXdutJPBel0BkvwIfG-v_pyvz_Hx8M3XzNocOURbolZuWzve5pkIKaIaMc6IVhS940cF5U1AL6fPzMpS0ZtdNq_8lbgcjcB_-c4qUWW_KP_z-r7MP4uZAF7fywKcpkVjcABpBiyjBqLn6oaL6LKPjtGSZO-vR3dRGq0-6KBYw3qQ2fcxBMTgboqVYgT9tDJ9czbDkSvz4jA5k71O0GdepLEefh0_QLHrQgPSqEmrNyIEorAXrm0jGzV4DTWzbB4rBDwFwg71TiMRsFI-_TlPp-WDYdf8KwYkj0af_PF3yI-zTIqyGmp2jvlCNXoF1AjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCrbRvXD5VcNANJBQ9zEFgNvwvuv2DEu2xANDRR7DrLv_CiM1Wo4F_BqOu3YBrJt-Cyh9ci5mN1Gv3w3bN4fGr_1AbRaclvYZ6lh8Govr4QQNMXXvUBNeDGEvZ_6a0aVrdKe0ivPhdnHrpi4TFg9DEvGl8z-sjjP6FbApjHRL49SQYeDdVZ9CPpG1oQ52EOgdFLzIEUxEjfYXA_WOpRLV4c2HaZvdOmXWHJkYPUz_0XaafJQxmkVZbceKuHTh2UEbvlp3Cx9qhWP40F-FxUXvWXelGZNtyLO1PTVkTn_BM4eK0NfgulKsH4SEggFTZGOQ1l2BNyaLKkZC6yQkcRDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HL1-wu2IPfDZ1QPa8XOAOTwJpO_txJvp1KN2nyaEKzqnpIy8Qq_V4YmF0uP511Ywx0ggJ-NlZTSIuMC1QWdF2T4Aqq3vpNIfCvZiK8duv0ePjbziZxMxeUPXbxrLN5qghgirVYednr497mXUYa_1U_Tj3OcLTZKaccM37cBEoGJ4cif9vBNEcYuBuSNjeuczkAi1QeVP1a7_lRMUVcHLo06YK3EzX6b8OnNOi7cGpp9J5kBaUZk1WNpmWPAA9zB8eLCfVKUcIXwKDGiGht6jgsKuc5in1_IwxaH09GUqvvs5S-smbI0ASI9S0I6592bq09YfM6QzgGUd_fxGIGc5yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نیویورک تایمز: موشک آمریکایی عروسی ایرانی را به خاک و خون کشید
🔹
روزنامه نیویورک تایمز در گزارش تحقیقاتی خود با بررسی ویدئوها و مصاحبه با افراد محلی، نوشت که آمریکا در حمله به جشن عروسی کوهستک از موشک‌های JSOW استفاده کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/687006" target="_blank">📅 21:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687005">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تمدید وضعیت اضطراری در اراضی اشغالی
🔹
کانال ۱۲ رژیم صهیونیستی با انتشار گزارشی از تشدید تدابیر امنیتی، پرتاب موشک به سمت عقبه در اردن را پیامی هشدارآمیز از سوی ایران خطاب به تل‌آویو دانست.
🔹
تحلیلگران صهیونیست بر این باورند که حمله موشکی اخیر به عقبه، در واقع اقدامی جهت ارسال «چراغ هشدار» و پیامی مستقیم به رژیم صهیونیستی بوده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/687005" target="_blank">📅 21:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687004">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0b85fc6c.mp4?token=cwnOeFVpmz91aljQVP8uVUcnzeD147bx6GZ2X4CMLg5u2y1pvHfxa4fb1ybnf0LdbsFuZxBw6JmSrL42Szj9nfbJKA20kC7FsNCu4p-VGziV5bEDcQGCyyTVe1BaJnhArGeuh4ywhcjS21YXRoRXIRQ1rxTBztqGPUICdotvfgS6OqM3oFaAwSJEbHvYfAam-HHjiANg1sA_EAhbqRgT8dEoAvwTc2KBLT8C5moDmAH2SkDT_35nb09OTINCRK5DWaxvU9gYfIPf7XId6xJqUopL44aAsUrl3GjqG3vC8WCAJVtjPJtHFk65-d0JLC_idKBZqvfs-Rs64ZVRBpr0Jyh-iD8KaFHKzo-dqxsUfePljPR3tr1HYN4ORp54BmglJi-dmwxMwNghbPBFCwvo0y3XxZjNdbz-E6gXH6PPDTPPHS88ApZ2QrcXExVS3jR0hXrI99LSAtqa6Hc6qKGxfsdRMwqay3TPkZ63g50NzwMe6qZF8h4BCtOHeQRFtwKjR7Vfj_haeS-VFyK3VS_hsteW2nEntfA4MxJSRfiF_bALzeEk2Ax27qHEY3MQmTUU2shYo9-cnv7RQKtL7LcLmvAkGw1r7dXp7ffMQj4gvIfhVKYbJOf3RijbbeDKLKlEYBDOjJe5Q70kpbM8bc-fJt8LwUVgal9ERXOeusRZhVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0b85fc6c.mp4?token=cwnOeFVpmz91aljQVP8uVUcnzeD147bx6GZ2X4CMLg5u2y1pvHfxa4fb1ybnf0LdbsFuZxBw6JmSrL42Szj9nfbJKA20kC7FsNCu4p-VGziV5bEDcQGCyyTVe1BaJnhArGeuh4ywhcjS21YXRoRXIRQ1rxTBztqGPUICdotvfgS6OqM3oFaAwSJEbHvYfAam-HHjiANg1sA_EAhbqRgT8dEoAvwTc2KBLT8C5moDmAH2SkDT_35nb09OTINCRK5DWaxvU9gYfIPf7XId6xJqUopL44aAsUrl3GjqG3vC8WCAJVtjPJtHFk65-d0JLC_idKBZqvfs-Rs64ZVRBpr0Jyh-iD8KaFHKzo-dqxsUfePljPR3tr1HYN4ORp54BmglJi-dmwxMwNghbPBFCwvo0y3XxZjNdbz-E6gXH6PPDTPPHS88ApZ2QrcXExVS3jR0hXrI99LSAtqa6Hc6qKGxfsdRMwqay3TPkZ63g50NzwMe6qZF8h4BCtOHeQRFtwKjR7Vfj_haeS-VFyK3VS_hsteW2nEntfA4MxJSRfiF_bALzeEk2Ax27qHEY3MQmTUU2shYo9-cnv7RQKtL7LcLmvAkGw1r7dXp7ffMQj4gvIfhVKYbJOf3RijbbeDKLKlEYBDOjJe5Q70kpbM8bc-fJt8LwUVgal9ERXOeusRZhVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی منتشرنشده از دیدارهای صمیمانه خانواده‌های معظم شهدا با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/687004" target="_blank">📅 21:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687000">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwgoFIkKoVo3d98zL06VcP5_4Niy5M1KaR_nP6BWbVlZokWbGHqTN7BMx-M9cDMOI06cQWlQrOX672WuUn8TQADnz4EeY1WgVFCOg1r3mO8-48Ddzs-U8RQ2w0UINL6x8vwvy-tfFjILmzhPtUrJrPnN79E5CEDmlZNJNJO8Hhwb23stfzJOty6Iof-exbIy43Fi293xz9uLZxMrBUWgPqtvTstaPVGl7r3Rp5RxFYMzwmP7IW7YA2ta_serfIF56W5iqkSaBs1o5WtvrPZDgFP607Hw39S0mZOjUFqg8Ut2ejGLXNp7Ty6Jo_ec_Z_1uOFAAHjlp0dAec7BRPcTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sabjMt6N9CnZF72Cdo6X3zh5ptmLB0uOjuJEyq25_P6sxY1UOeW3VomaN8rjqkbBbYMQxrnlgUs9-KmMkIcCg9y9-xaCaX-XJ_dG9EJIthJXwPSfObbivqa8BE5-CvC6VvMncEa0L-qRSS6WONPgfiECdBhGSoI0m9ESFyQIRP-LjInbegKNjJO15pf_3Eu-jhXkr7WjqliRCiP-_w6ZDx_DBKHYsq3Rr_EvwzncjAHxUa1nrXQui0dgbKiHipIyoxorBvDBzLIWS43HJgxyDU5Bkp6Qr30S1U_3B93eDozGFDhmyqQusylhFs-AatmSRFv4gM22QwXSxXcwaVL_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXnfTFSDRQ-IPY-uSQFq5J1UItPCg8jKVWP_nXby1FxTzFcTVpjLcmTr3vYxCuxq6aqt5wXE8bvM-KULZ57Nmjwa0pCssPd71EZPtAUDe51k3pnDPBDirEM8r4TLocqtSnPGQJXtpio29KCbTK33NMuYVDZXIlVJN7CL9Pmm0lQVJ0F8h_Ix-xQrSkjcKCZ9eyTO15FRC2vvaAWipOc0WDTBQNE3pGUNqB8HXJYkc1JJ-hJUXQCmfcvHiigW-9y0nV5N7RQ8V86Gds3snz_zsXl74Xxs0qZkXO9VSjcORc3OTSK5KCXHgRu7Lfh0tq5TkMJO-klsa4etAMs4ZXlnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/crHssI4K-prKZPMlEL87efqz8big2fWXC9dtwZLP4VYz7dRxAFmtTkl2dpJRUBCHOphhqwQl2WaZAnprYIsXhAa1I3DJA8aXmNDRub-379St95etg7s0-GPfPGnaR-Nr2BovCQ6NUMgsWyFiTQSXKL6h4fIx4HYlwRhPr0-TAkNNNJHE6SyKkFcW70iZB6jIUtjWAyDeM9fMCRDTOxMBKR1ZCCjA6GJ225yuigjU9tZxEJ1tbz4LknzjkyDOsXmp2eSTHQWkGBzShQyt9S5ob7ZG-gVhsnPaxuUFGH_gwiUhMEwhLLss3gpBa41H42TGYCZt1gHkbANKOHwpFufS2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هوش مصنوعی فقط برای چت و تولید محتوا نیست؛ برای هر شغلی یک ابزار کاربردی وجود داره  #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/687000" target="_blank">📅 21:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686999">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
مخالفت قاطع چین با تحریم‌های آمریکایی مرتبط با ایران
🔹
سخنگوی وزارت بازرگانی چین به شدت از تحریم‌های اعمال شده علیه شرکت‌ها و افراد چینی به دلیل مسائل ادعایی مرتبط با ایران انتقاد کرد و از واشنگتن خواست هر چه سریعتر این تحریم‌ها را لغو کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/686999" target="_blank">📅 21:02 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
