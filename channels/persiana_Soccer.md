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
<img src="https://cdn4.telesco.pe/file/BeLSskF5GDFEfoeftmQ0aCWSxrsQ31UgjHXCXaY0nEdiz6N_AHst36mPCFvflWGfT_sKxfd0M1SdUXMTwMOYxOG32_sCyBDEyM0DsnZe3ejmQaXDJ-XitrhcNCma3EddPN5CbKH3Xg4hM54nRn-bIw4wj6dHgAw32DZRNkeMgsIxJFDPWDzrIOCxINE7dVQkVWIi0oOo_2Ef2-CGobgzd8Pc3MfNDoBw7YHiu301sczTvW_fzSvilswaJ5WBKE4Tc0fYW8glcBG2s_-1h00Srg4Z4ULxm3VKKtdrJrJ_axQxZ5bgH_FzVdUnyu46SfELSRPyKGvDfE673w2k0-IJhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 450K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 20:15:07</div>
<hr>

<div class="tg-post" id="msg-25619">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-78Q2Ul-Kn0HRsEgaIK0ERarZFdei1xcCOEL8PsibSVtKc9iVicIIdzHvu6gslZNWaMH4Z5bqIf5_gAahNh_ahZzKru1vPA-17KNBMXq6Fx2Isy0eUFT0oy7yNeT96agtXvCdf4npdB09qgKO0NOnOTiSTyNDuicPCnGYhMAisxxjf5E6Ss2TKHbFv4BHfSz-tJF087Lo18QeYjsVe7jxiQwk--NRiDrS50sCumx6i-3JqeSEGuNH-6tsxu1A5zJEhLKz3Fq5xLfxpZgNi7H8HxQmXw9tdyfZY6qYC0tlSZsmLFs8NRmtOiiJVyuIGwlwR8Y_eUMnF0gln7jyfJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال: باآسانی برای‌تمدید قرار داد او به مدت سه فصل دیگر مذاکرات مثبتی داشتیم و توافقات خوبی بین طرفین شکل گرفت. امروز آسانی برای دیدار با خانواده اش به ترکیه رفت و به محض بازگشت به ایران قرار دادش تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/persiana_Soccer/25619" target="_blank">📅 20:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25617">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Demse5jCWndEOsVb43HmKULJOO_4lRBRB5OCjN8or8I0RyObftshrTtq8x2x-8cyrkMuiWRfShQY8VHLSTjB6n3FfELIPedabczuDXPNh7C1CqiP3sFIKU8stROTl0k5UoWshX0Zf-BeR9kTJk-MDp8pn4_FhAxYaon4CL8vdWFSBRFbVZaO8x1YE9O8CkX8VumXABuA0b0WUrZyZsLw08RMcmebP4V0CW-Vnb6rWKNJtf-1Ut2oDNOMkMgOjA8yzSAzB6C6WGf4sXhnJDDVcXT5ifnhVbs8ZcevlHZwzXK5SB271pUbmiKLWAPnICjbgjheYgwbfyvPEqbAbhordw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/25617" target="_blank">📅 19:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25616">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnZXvzzeYsBnW0hvNewarJLDiCpJxHTSC4feeUW4QRDtTV052YPCFGh5OIHhNDvdwA8hfLD96Hrc3pFzSUPlnrGVQD9KSRMyq1sCQez5Ue4Z4AEAj8UfdiCPvTlzYRPg5_xleFAOE93HRnxkRGMr0v5BwPGv5u5iFJKKWCOc_nip34wfuPU81vXI1SdeYTvQZSgOOfcxA99EGTLlBtNvEG-gEB8RREEkVg-epDyyZoCWccsFpaE7U1u0XSZrzudxkIVvrWTnDyYd2K9_uWCUd_0uSzji4BX_5wNbYSbufuy3cJSKoNuVi-YStKTdWj6yFgDjM_PzMO-i0H7o0OpjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/25616" target="_blank">📅 19:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25615">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSDHlvjtomttDwL6eQijls0Wl3B_Di1PkkPLuMo75Zy24qEOLNDppOnpZXSyluq0WMci-7tEIbKTXHGxrsHqv7Tk76PZHh-VVwtKrxwDQz8QxYlHXOFjrGipk2m9ZIuNW8fH2pQ7o__Vftk0xyrwrFE4PDNCt_h0Sxo3q2OnxFNfBjBlVORU1-7FikZy9fey1xyGUnryzPuFV94_39gvZCe6uiwXhDLZqgLajiELt8TxVIijSUsZxTprcpRy1Cg7ALjk0kYy85grQ4ChxPcJ4VTbad-GyqoI9MTaJsemBskxTo5s9xU4CZKSE-EZ69cR5H5OPXLT7E-kPOFa8hmdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/25615" target="_blank">📅 19:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25614">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=lJNMpn54lnzgD0NRX-ag_6uTAtr0yWeH3lVa0c3l9kRGODZ8u1BA9_15DuKtmOI2JvSnwRlrmh9gMrA8vujes7VhEVmToLjvEKTic7R5j9hBGcGwiMgbPiwG_lzDVxcVIQ7fqMQZtmSLQQ9ZS2Z5T6XZot3jAW-Xzh5KMjFVEnmHVp-vuMNDGJf-6_6f02MhREtt3QClhzz1tqH_MlQtL4JvSIvHa6yiIRThtSGBkYAUNkg4Y5yohBENFHhxDzgRia5TikhLfu4V-O_3xkbd4SeTOthOB9qRIcLLTqu43Df8tQjue-_YGJ-mPUT7nrpXyyQPE70U8BFCuQ_o1BIrsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=lJNMpn54lnzgD0NRX-ag_6uTAtr0yWeH3lVa0c3l9kRGODZ8u1BA9_15DuKtmOI2JvSnwRlrmh9gMrA8vujes7VhEVmToLjvEKTic7R5j9hBGcGwiMgbPiwG_lzDVxcVIQ7fqMQZtmSLQQ9ZS2Z5T6XZot3jAW-Xzh5KMjFVEnmHVp-vuMNDGJf-6_6f02MhREtt3QClhzz1tqH_MlQtL4JvSIvHa6yiIRThtSGBkYAUNkg4Y5yohBENFHhxDzgRia5TikhLfu4V-O_3xkbd4SeTOthOB9qRIcLLTqu43Df8tQjue-_YGJ-mPUT7nrpXyyQPE70U8BFCuQ_o1BIrsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ یک سال پیش در چنین روزی؛
تیم چلسی با‌آتش‌‌بازی‌ مقابل‌ شاگردان لوئیز انریکه در تیم پاریسن‌ژرمن قهرمان جام باشگاه‌های جهان شد. دوره بعدی این رقابت‌ها احتمالا در قطر برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/25614" target="_blank">📅 18:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25613">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=uJATVYfJiYzubIvcifaHEGiEjNAdWm1LWe_AMtLB-93I8_EHPrIGQsgfK_vLoHJZ1q_PWjEBxuzGJv1mERmv6dzc8EP49gvL1TsRJ9St06tB6ptmJTc1Pa2ycJluTvm5KlbW990faMMx1UJRy4gnjM36uCW951xNTx4LakFKWKYwBG-oB7fmimuPpNoE0GaF26pKZ0Sm6DdUqeWnoARln6HhuGXQOcLxCvOV5RzpAWczNhZmbAXDpri0E9dZrnsY0pXZRM8ahzrhxv6XJ6gJXSfWoB5mJMhFE_oTxyZ50-FoNroZRfP7XpLiwByg407pOTZ0JzRIEu1x-Jl4dHUyaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=uJATVYfJiYzubIvcifaHEGiEjNAdWm1LWe_AMtLB-93I8_EHPrIGQsgfK_vLoHJZ1q_PWjEBxuzGJv1mERmv6dzc8EP49gvL1TsRJ9St06tB6ptmJTc1Pa2ycJluTvm5KlbW990faMMx1UJRy4gnjM36uCW951xNTx4LakFKWKYwBG-oB7fmimuPpNoE0GaF26pKZ0Sm6DdUqeWnoARln6HhuGXQOcLxCvOV5RzpAWczNhZmbAXDpri0E9dZrnsY0pXZRM8ahzrhxv6XJ6gJXSfWoB5mJMhFE_oTxyZ50-FoNroZRfP7XpLiwByg407pOTZ0JzRIEu1x-Jl4dHUyaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/25613" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25612">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLTM7XsFCjS-nfUuWjAOjEx6z8s4M-uMnBR-ek_nOUeRj59X0n6eV-7s7Q6C2K_LopnrW2PXzzHyacOtoRO3gl0r8CZwA2wbtG0OEYK0cJfU8Mn8Q7W8D7tpF40CE9uyakta2BAoJbqC3G5VjSBtejbetbd4FQ28pyiW5sPSoWUAcQlPyHZZdF8NhTLwhRy1u02S4Y5NQZjnjkVq0x5G17bv4KnCLz4nRp5Gu7cjZxegylR42tvdhXdGOgnZ3bMuXeKQTpWbVbZ0WJSFOJw8alWquWOd1ymAh720zmXWC3RYDeWueURQcZF3KCdB-SW_qgLwXDZfTB6e7gIBKvnRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/25612" target="_blank">📅 18:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25611">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vxyd5iSWyBniqe0luiGRYoEfShq3JNXjoYEHv4WlwCol0_yrguuJcUkbDTj9x3pszj2aBF_fW46_2C7FJU7sRoMin0ahIDkuM5_UhgLzcL5Krn0D7RtZxa37VOwxMxEvx4s86u9_QPgtuaTLstVQqNaHZDNYuD0oWVoO7LgRP5EHSm5WhSrJeGR2Vf_WN9S39ozQnp_id-N9uDehWCyYR3vNpVFPWGiHrEs3L5WLLPPfO7swDBK0fC8ZrU9vZ1-Gmo0FgjSZmnBRk24BRwAy94geSRw1a3ESVKsJJAwQXMw7Aq-bacwAxbJwBsDdHtOWBnnZssZDpLuZC0Oyr1PbpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
مهرداد محمدی وینگر سابق استقلال و تراکتور؛ باعقدقراردادی دوساله رسما به تیم فولاد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/25611" target="_blank">📅 18:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25610">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-jHzBcAGMfFe2GJsi1imo_YZycYf6SlMu-ypq1zti59UoQvSPHslq-NiAq5NCf8ZzIDmSq2dUVcciUEdfUw-ho-7kcnuUrFKuTGj_JbmfSqWRyoKK8SZy1b8YNPiR3t2x1lIcmuMpel7QlRjko2WToAlyZrhDZgbqilNopJ-V3VcnAiokdjQtD2DLw6d5jH57ZemmaEZcH51XQWfmPDC7c-eN54OBPct69eBS8coU2zhfKr5skIJWOg8MT1hq_uzK75jFFlXksLdfvRk3jPp_tO_YA0kvCxQDjFXPtenJ1JEcx_hKiz8lUFkEZ5KQPAfCxYpocFN4_z65EpCTgu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محمد کریمی هافبک طراح سپاهان قرارداد خود را به مدت‌یک‌فصل به ارزش 65 میلیارد تومان باطلایی‌پوشان تمدیدکرد و در این تیم موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/25610" target="_blank">📅 17:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25609">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqriLFHajIRHfwoOfqnmDuI2GdvzQKaqejMctENwh1daG0Cf5fPO7ZuhN71ROBoMBTEdj-VsRhbItxgkvVScsfy2c6WR6kx7AZVSXeJr0fJ6WOZtIMJ3mJfljjEpF-Do6s1FtozzCsujQzJd08nLV4bQpMJzzDBWOeGkyMUfKlcpyrx-TSsgktOFCEamO-EvRMqbjkXQvEsYPFCOghpZazilSpKMTkKXpaypxBsI-ZQst_O0Kq0GxQPgd9q6_AlnDgM0omO5PZAp4A3ybG88Igtis030AjYROmW9uLep_iFrRZHBS7Z8AoCU_XpZfvjVTQvQljSrfP90DX9Dv3ioeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/25609" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25608">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCBs5rkN8CTmcWkJjMIu9_HZ3v-0PZT9EmD3sqv4RrWK6GS7eq0PLBfjSUxhLUcSC4txe3wdJyqhocYcfuH_ZsWxAelPG7MRpMNnTOaiN5h6KYARK6SV6DIPMQH5ZMk_fOfog6QzzC2ZIl7XgQER78MYsMxIqVAvDMcBvG8G7coK6XRS5pMvD6Bvf95pD7B-4go9U6TaYzpNlFXlmLRUu9DeLXiaXf1wdqmeGUuvI-vJErWZHBnj3dQzTIpadWuK_08bJCofInO5aR0tmpPbdAVy7xKVx8xZWsQ3mZacrWXrY3lgWj8PyzCVI6bNXrNMa6_iRRMP2Qo9LUdnvlaTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
خریدخوب انریکه‌برای PSG
؛ لوکاس دینیه مدافع‌ چپ آستون‌ویلا با عقد قراردادی رسما به تیم پاری سن ژرمن پیوست. آستون ویلا 10M€ گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/25608" target="_blank">📅 17:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25607">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjuqlK7DetvZpKR1A5e1wIT9awh_M7pRtiFoVYkoTggjcUTJtA8nIV09-Sih5lkMs-PEbwn1xO2b4yBlSpuBj5B1l51L2DWmbiZvDX53USM4dtFFxhA8tZHzMIddEO8j-8l2ogFHAvTVEL6I0qONN0_PCCTgiQy8-P-VeA6eh_lfbczEuk_TcA4F-6r6yaYaG3nWyPYeaJKNCXK_4O6UatLbGCbgOwRHRQ28dn8rb9irg22CKkY2hUtAF0axLGiVs1EybncvGZANDqqj16z-NIGyxBYcd21lIvlh6m7RvSfbDlI4TLYjLymlv997EE23NOZ7NaqAepPKgbsp0KLpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ 5 سال پیش در‌چنین‌روزی؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/25607" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25606">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTffYSjIdZMBgC9KzfB6wehFLLFK7VUues_HSd2qgMuL79TAZq93deMJRrdyi--bKdIBXiUTc0WymZNqci5OZ3OtiepN2BhLroRQoaUH5igCu2CW1PUmGss-yQkm4CsLvSAgfhzrbmr9AN51eyMUD2uJOYUbkYWx_r-U0GIfeEX_u-VlW_pyPIHsRxn74Mo4K0CwB23wbPcdU7NfPkZ1CbB19-0jwM7eSk0Q0RuMZUjbdtFQb6ZRIX0HDlC_f6WJpvngpt04OCl-8fLCER8bZvP_7urRtU0CUy-NqplDd2Ad97MdwhTSVQxQshkYdfnGi0iCzfgmB6PsP_vXG6v2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/25606" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25605">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzygQH4GgW6QiNJlvi4-okX7wvc2aRKrhaGNX-7YNfw1pS8lhczTO180gof9SXPqlYfdcK-KTeDb8TyvLLd0gfRuiVoXYA3p8EhZIUZU8KcoP7NzTMYl6z9xdAZfaqV_0OIr8DXkVp89mGD2goe2mkELjVjpCzsUt-04NMUEq9nmsdZz35uS3ZD5rt-3gu7BNKIAcPtX3eycLUdJqOleYE1oQ9Uj0E7aCjgY4hd_jdZYISSm_o-ZBDjhW0Yhy_lM6NYCc-m9ToVR7HBMc4qx1fuV7xrAp3mYdfX5NojYcf4hxFejcfPNvex7vzWgZnubSegHO9dFF7RxfYgOf2wc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاقه‌ویکتوریا همسر دیویدبکام به فوتبال کاملا درتصویرمشخصه‌چقدر زیاده:)از سِر الکس فرگوسن پرسیده‌بودن‌اگه یه اسحله بادوتا تیر داشته باشی به کی شلیک میکنی؟ گفته بود آرسن ونگر و ویکتوریا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25605" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25604">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daGEe8bTcw0OhECXnIxlNt58bo9oMob15GHL25Q32M6nm7Mzfei9bslCK2xMmqqobRhTmpx0crlD8TxwaJ5BbjdMtD-VWaHHJYUDxtDVZ7irAYFxSq2HoJYqzHtUluBgJ6Pr8T9QTkYFZ263WRlFZ8P1BENPjV_0liSydIr1PCKUCeHkIjphEy4dW9PNj-FsHM6Z4BJPIYRw-O-zCW0RmQ6GozO6BQ06E7-np6TYLvfCKhXSqrRn6X3KtJC1hNRl5Nhzk4Wzrs0ORzBJsbgWARIT4cnoLeoH89lAuQxL1plq6oRWPLeIXWUxVjnZu9NsLqcQws_pik9kWSeUlJC4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25604" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25603">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXNjP0uhQ3RdTsmXsGtSQCODh5GdU5imEZ7cSjNOpbV14TUxVyAeHYcCp5lGNOojSx3kJEHQAmgMhB6p_oJpOuv3JZ2zs89yGtXxCTCseHMKsDSVaXxQzfMGBfGyr2DGLJ4YujFuOmWg7YO-sTj9AGwVlWP8yCbf6NibrtT-zduABIkYWFBp6esay9NuECNzwdlLaQ361piemOE6u4GYo28Yi4wBkx-TOgLmsuNntnF7yYW_4zPq_KgCMYAhUapEdbKTYURfUoIrOjxr8wj_qfKPXBIPos9jx_U-l7ZZg5K-p6P5Bbf2Djb5tdZ00nGZvnDviOT-ycoTy5E-TatI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/25603" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25602">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la5b1-qvOLXmh9NrtIx9Nq_pI52klFrZCAkHfSIDdXLz9EcCqTuad__Bg9Lcbo9YuxgnnFNeI7TtPFoBkp4oEVoh_p2Ij2vG1oFVmSMOKR0AEl12fR4Bb-9sssa6yGuAYtJJaRNkbQ9XFGPNygyjXz2__jGhQ7mTwqCv48X0m5ZlhMl2MbCzojMHgv-5nucSfV1sfA_ynmgZsEAWx0nOSKdNrybJ135RYlxzNk5YlMSovcvLEHsXC4Myb9i5GtSzj5ZIjJYfNQFSQ6XHJaqd9TU4GbeWIHFUUk2LsrmvN_s8DW4JaBQWyJGLru7jOMRw2-bU46_bCc12_F2fCpNdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنین مهرداد محمدی جدا شد.</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/25602" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📱
دیگه وقتشه دانلود از اینستاگرام و یوتیوب رو بسپری به یه ربات خفن!
🤖
👑
هرچی بخوای فقط با ارسال لینک برات آماده‌ست
😎
👇
📥
دانلود پست، ریلز، استوری و ویدیوهای اینستاگرام
🎥
دانلود ویدیوهای یوتیوب با سریع‌ترین حالت ممکن
🚀
بدون دردسر، بدون سایت اضافی، بدون اتلاف وقت
✅
فقط لینک رو بفرست
✅
فایل رو تحویل بگیر
✅
به همین راحتی!
اگه دنبال یه ربات کاربردی و تمیز برای دانلود از اینستا و یوتیوبی، اینو از دست نده
👀
🔥
🤖
لینک ربات:
@instafilerrr_bot
📱</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/25601" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bilUJU9g1OpMEuAhG9IezUwSfCRpSv2848xPxKUwf3IiSwoHtlVwAaNDBYROU4jwdu3Cw8rZTCNX7RMBy-PzfYmorF_iXWlAs4cgBsYSwu3GK0u0piTyFEbk1dkkEYPjRsHXy__BHYWuqBUj0179D5xn77-T9bE1mLeDhmWpi86T6It88YYawGIxt492WNhzA8mAzMPKrJ8lsk0TnpbEZrpplJZgcGlYKL4VdsUNmea5RQQtP1umBAaZUObCc1-cF_qc1-0P0udLXyivkTytrcSeE9jkr48Q1BdhVMId7Ey8Y1BQMKvwwS5jUKoqQFFaaaqSn-Fop250UaA-Rb_WJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اخرین اخبار دریافتی رسانه پرشیانا؛ امیر هوشنگ‌سعادتی‌ایجنت پارسا جعفری دروازه‌بان‌ سابق ذوب‌آهن او روبه‌باشگاه تراکتور پیشنهاد داده و عصر امروز جلسه‌ای بین طرفیت برگزار خواهد شد که به احتمال زیاد به عقد قرارداد منجر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/25600" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=A7CnRSTxiU_6UX1zC2xdLGdhN7uPnk8C98pTaZb13IRzgarP99UobXcxOBMIdGYscd7DS2xvvwb6lUWKKXGpa3K4SixZw1lQ22zAjkPffZg2KMNGObtf1vDgTgESaJX2KtPmCyDDm8GRAA72GmEPUKGplA8Jbc4SwkmO9muLzagfLjjOPJI-Mg7aPqUtiJ1l2otrM7cBc7dhZ1NNGhb_zKnMVg5TRWQZcU2V6X2fPc-0U6-dXW_99pPC-9aSc2gHdIU6EQ11eenWKUnmaUA-OCsI30L46r8-bkTH18Ejxbhx9rTT4TdLiiJm4jx5gsEsZ9Svn2ceZz_r81qM3_aORQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=A7CnRSTxiU_6UX1zC2xdLGdhN7uPnk8C98pTaZb13IRzgarP99UobXcxOBMIdGYscd7DS2xvvwb6lUWKKXGpa3K4SixZw1lQ22zAjkPffZg2KMNGObtf1vDgTgESaJX2KtPmCyDDm8GRAA72GmEPUKGplA8Jbc4SwkmO9muLzagfLjjOPJI-Mg7aPqUtiJ1l2otrM7cBc7dhZ1NNGhb_zKnMVg5TRWQZcU2V6X2fPc-0U6-dXW_99pPC-9aSc2gHdIU6EQ11eenWKUnmaUA-OCsI30L46r8-bkTH18Ejxbhx9rTT4TdLiiJm4jx5gsEsZ9Svn2ceZz_r81qM3_aORQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
علی رضا بیرانوند: یه‌ روز طاها پسرم گفت بابا دوتا اکرم تو رو دیوانه‌کردند. یکی اکرم عفیف که همیشه بهت‌گل‌میزنه یکیم اکرم خانومت. منم گفتم اکرم خونه خیلی خطرناک تر از کرم قطری هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25599" target="_blank">📅 15:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMv9_AdwwddkV5pEeTx_DqqZUeLlSsm_cuYplI2k3gLUJAgtPQfmFX7g289NH0n3xrLH-gsA48zdW4uU8Re4xCWb1egppWCP4ZxafVY1OCz7-NSh1GBE52esaDJRQnTwFHYzj6Rcd23nw0vBKxgbWQ8p_NO4F5cugrbrGZ-eHL07pI2RUvTxrj9LvMekBl7fgWv50MaYiN_B_grrRRHGbf58ImphtWcef4wskYrl0DiZNjd-oJKqlwoVFYhkfEONFyEitiCk-QFoJYsXc0clEANf1Zs9kFQRjghlBs3AAzTNfzdMwBPsiZEOGuqpllc89P4hKVE06XfhP2NhlChaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25598" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTtor1zocHM_RbKP9AWj-UtbaGiUtwvJfxl_TL2cxXxOmGsl38cNOU9hOfYXkskb1gg_sxAiNQXNoTtxlhmaxjOCIpxQFKBwTxnkxrl62Mj_zHL3NsENXTp0r-C4_CmqK4zDZLU5res0XRZ7smOvLWBlyV0jkZKT908kP-xg33YYfyC9e4jO_aAsPq4V2glDC2qE2TqqKjMt7ol14IjJ7uTsLRenaTGq-RFF_ln8ujF9dUvHevTxy7ofgQtQwxYqtD0-7AroJGLS3af86TTj4dMgAYNoonoeJ4lgdn2bY7XDNPYsuYNBcljj4qbo5dFuymVpUaDyKQHsPFGQbI10AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
👤
محمد جواد آقایی پور 26 ساله که دو فصل پیش سپاهان برای جذبش 100 میلیارد تومان هزینه کرد باعقدقراردادی به نساجی پیوست. آقایی پور در استقلال خوزستان فوق العاده بود اما بعد از پوستن به‌سپاهان با اون رقم فوق العاده سنگین افت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25597" target="_blank">📅 15:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQc3lGnupxYEIU_SQhhwarFrzHhcsjX9gfTgmMbzbKCUS0yQZg1upBMzT8gABBGYD8PRT_1pSPYOyrV88pXzwfMTc9eALcFJDOSgBVhjTxNjkCa3D4MEYqnrzg-lQkKOGm-fBR9Wrh-mx2B_OG6VxmJesb4Ee5YZ9x87fnJ8XrlOvEnFLlo-sBfaYTMu-fWgmOJRvY4l4jmnm6Cg5tu-vpZb4VjrIIPnB7jS6EKHTeA1qfDfg_Z9yyghV_uW8idgIKiYRKz4WGwpT8F6fpg-v6UvdLQYN_Zlar4jjUKtlXqxLVN-d-iJdW0h15AJI_Y_VrInhxY4xD7d-UlkM7BCpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
فرانسیسکو ترینکائو مهاجم26 ساله سابق بارسا باعقدقراردادی سه ساله رسما الاهلی پیوست. ارزش این قرارداد سه ساله 45 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/25596" target="_blank">📅 15:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKXB85msAPz1N5jA7-jt220IiaklJaCfd-5c5gLz2Jd4DTs7fHImDvb1X7Z5dtxiR3pwlDEWHKitnfE97UlQ6VWfltMdxgwMTl-jFUu8V48i7XpI9ShOpV1HACGyDFr3z4qYsMFTUcq-zSlY6fSXd1koittId2v8IUOuPB0VZo0EBcq0k5YLSvaFsf0jORFGPcZA-tg8M8jXSDjfN3MjOHdJN-JyuMSIgKyH9qU8W858skHisxHRnc8rzMBRuE7icF5gE2pcn6OwqZTc-bF373hyHxuGyU7QwTEbtju46p9OCR5W_z9IeB8LARU_FzC_9jPx0NE3SMrLLlDocVoC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇮🇷
بااعلام باشگاه سپاهان؛ سید حسین حسینی دروازه‌بان 33 ساله این تیم قراردادش رو به مدت دو فصل دیگر با طلایی پوشان زاینده رود تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25595" target="_blank">📅 15:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSBGGdsgujj_fuFkZRC501hUl4D83SX30tAXb0HCXsdU9Y8mvZtZlcXkhBzGHUPOtaHKUBskSb5G96k12cF3P-0DvUx1UDQ26qDx59_0z9jm58KEbORMjnGV9G8dNlBDO-sUBr519IcT3WMs6u5N-KFwXXd8ep3CQpQ5CR7lQMrPbpB4h48RqtULC7x_tA7ohi1Q7JYoR5IwN2yUmEt3K0RBb3mTePkWgpoVykQMGjapreO6Ughf0U0G_l99Ux1GSE5D3Ou1AXlvTh6RR4Aj4mbVN7xZpXWyKM9O44K8kHoxvfwBfcOWAN_L6_Wrm5oxDxfW4LWJJ8ctRGM44p8aVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25594" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1YclFbd_GenBXLIuA16RaC0g21PN7amCuFOY7qyGCQTUX1eewS2puzDY0pYQbqnIjqzNxXsWfCx2_LsTR--aPZ8sUcUUVj88o6EMOUXxWF548wToO1SR1c_v2teC50ca6lLvxAanUc9i52i_s1gAGXCWkDnzke4xWmUF-Ur9S7YrOm811EBrZ4qsERU0TObNr6G--rOdJDsEPGJ-cARCA6KAsKEccdBFlLqM0OUIobjtAKNBUEUpqd6BSj5XWNHoinpe9AmdqzzNmD-xAmRMrjjKrZNEzuPWrFEr2x8w56bsajcQoWaPpzotvs-9k6xs6XKJQkTLUGA3kpIs6DwRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حسین حسینی با تخفیف 10 میلیاردی که‌به‌مدیریت سپاهانی‌ها داد در این تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25593" target="_blank">📅 14:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-8LbxdAqZg6TQgvY4LXRDkuCQXbHXSE3GPznP0AP6i66Hatqmi2Yq6jnNfbKSkChA2UFMCamfrTH0GKkXbo8us3MGbAyz97EmcpPvCdQy_fqTfyGK-whh-YJj9NH3JWz2gJQN578RqUfzp35Cwm9elYJOO6VldBlJt9TT0E4tHgZZbatHX0TlliXSK-LLLauNOxWni3qKTLXIEvjigGNQOGx81ie3v7vpqhnoYxLes5UUxd8ZHXqLZGsAcR8keuUuVGfP_H8pqHKVWyVUa3Kn7rkZybcm7I_J3swUO4RaAGgtbb-B3XRkDAfm7BG22WYUvEN-QsIHzzbhZUKu2tZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25592" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25591">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKpHiYsB3geSorRWC7D7KKfmQ1pKjVheqr8EHI_d9Kp37YDOZWn2bEbnrCbyVNtWZeKaSl87hrUSWU2cdXyX4H8yhvlQVmAY4WeP4lyTVokHmmu0labR3G7YpzkVsxSMTS754UB-LAwGqNnhigjcGEyf_MyXSXQegroNNIqSCQCsGSQaYadzEA7RGVEPxeqrPqtiwMqhYkGwMMKMj5gqNMya_sERTD6GSOp_v3IDXEgWOG1U0oJ_v9a4sTpMScYsJqdICzSEwAOwfx_YJC8nZOr4S4lj9s4cfq7itO2JgrxurNOSY2-WRGkTzbmJv4vkHzpIqRlfdSlWLWuXvNfsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی سابق دوتیم النصر و الهلال با عقد قراردادی تا پایان جام جهانی 2030 بعنوان سرمربی جدید تیم ملی پرتغال انتخاب شد. دستمزد سالانه او 1.8 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25591" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25590">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIz8LDxCPH_yVnmjNv5ra_XO-fOOpHmZp7nPrMl_OT1grj2XkjQbHSIvLM0ChEbEgjEgpAQs3GTAYeZtebOzv9IHU5iw0ccZg1vaUnfMCTKK__3wu8WDz9O5Zn-U52gmKUnJI3YDnC9mO3arvuaqcutFiJT0w9btKPvTJb1U2OAeOjfwsTs6WNr0sqE1qWb00P46p96G7nfLrSq_OOsYYAlGMjR66-UawIZAoL_30ZHXNvjz68UzpzA0IkmuFH1Owmc-B-O2cTtYEs49cjT6Kpkp55xmTBNriAD_Ri3e8-if2vC8xLFJh1ewIl2gUDOwK8YP7TVlTuCU45r0na7ciA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25590" target="_blank">📅 13:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ES88fB9Vb3UTv3ZitX39SSsNxVSm41Kz4-YI7NlNsIAmTx_xF7oetjV23v2CJht4h00eUYP8fuvHW2099wH_FaxTbLc9jrkgH6i6vQqH8Yir1rV9NOxg2d_6XRYef8kshDS5PipBXNCOYv61f9Xrbblm7FScDPYZy73MqQ-jgOqiGTdz0VaSL0DYiJna62zoho-fqe9fbeTaJNfof4GFyXKcQc1UWgcZ-jypp08qnPZBHpYMM4fcPmXJAVaVLokrLfRA4Wwo4lUiYjVvGL-EHclDkfHLn26r4FDv5z2nQkETaqYH19rPAP7m0Cn12bd8WRyXO8rxMrmi3l0O-phVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛
یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25589" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25587">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6G-GO7qEsij4TlbKz3ZwhuVGaZt0wzrJR3jUjSiLc0GYpZvq_HJEEUgt_4hvLLsTVdyH-VOcGUR2jXyezCPkKZnh8fK3DTFvJxEizdm3F_8rouXZI6_99xg_rhIoHRh1YnplutfQR3t_Si4G3pIWm-Ufy37wRq64KruhuOWqJOYAjZKEAnZ4Cc-bXV-5AL0RqR1V-WyiZzfdE6oLFEHZRd1kIIfdYP-9iI8QjIhN1k-GtqfKUnaGvQnj7WCatGiRcGNPwINGRhPS7LsGJoIOoDdqU7tRyxCAVNYuiMJ7LA8kjuqNk3bZjz_qcvgAF77ba1V399CJzzdSPEaRxmAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmpiJhqqQulfsX7T79QAf2zAnfRv5_g4QnL11H9DtQjo0PfMieKOwr6Vt58yQqCLSY1OyMOrk4LTovmUNDkT0j2zVtHFrZFmCdzf9I_B9UtoR3wf9963L9-SaeundjOhIrRA12cBE62niddXKbM0ImSPIXsrkjcniO6GwME_NRaM42yw1AVcBVFDO27ZBDz37RFYrRLEvad3dCHnJkzRS5xMBoT0Qo6Bbke19t6eXS6f6Fa7WOlKyRc5ZmEFDS6Yl14KpMJ0iIUCQBCq4UmDK5FCFQwQSpxK2OauNiIf9_lXcXppG3U806kC_ngtL_kFpq1cYPK55stUXov2OtwjwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امیر سام دلیری مدافع میانی 23 ساله نساجی روز گذشته ازدواج کرد. جالبه‌بدونید که همسر ایشون مدافع میانی تیم بانوان پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25587" target="_blank">📅 13:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25586">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcXpQwE6MCVxbcQTg-p4cq3GaGZb_eOKoNqxXz3w0jVFJPKegqXsI64BqisNjeaY-bL2T3dUuIoPDc72LUXO4fF-k9U4T3fhDX4DwJbwg7tvd_ai7SnIH5OdeGcwRJ3v02ZjoJfFSngbQ796WUDaALI0OAQgvr2Sv5mXkm6CVWa8joCAZFJrYBW8DNXm3LhCbflK-NdzscABUNzlYU58XhjSaBbbMJg6Zb-FqNTKxrRFBl9od_K8GxXIH5tH_yMUJPu3XvWz5QrwMUp7eagqf6p4ZzESWDdl1MNOLIQJiBqEWi1ANpbSXVtg2ZttjMHbyZjbDPg2fJEyKxTVlj0xiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25586" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25585">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=NwH7wjnh8QbeIcIKV8G7RURLxhcyeM62Xu8YkwMrI1ZVqDWw7awaME76TJPQ8y5ymDJy3uqY1_aDJsaXdE27n8PnTR4EePacjIeNrAQ54_BkSNarb8XqmU6HL1MECgKst4LNKYguJ2spxc_1zNvPLRYXMTY7G3n1D49hmGMboWfEXYAjI3-3sg2tsXDoD5K_YHb6zOZ5ySX-_uMxGIOzQ1b8fYBA6A7XUtsT2XHIIIngfoT4KIKAqIVVlwDFrPGhb8d0nzZc1x4A8u7fjGH58sXpkkcfl-IkslXERNZQWmaBh_3PtpkcRbwQu3FnrmrzLvsfQJZaG5d-xji_XQWA4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=NwH7wjnh8QbeIcIKV8G7RURLxhcyeM62Xu8YkwMrI1ZVqDWw7awaME76TJPQ8y5ymDJy3uqY1_aDJsaXdE27n8PnTR4EePacjIeNrAQ54_BkSNarb8XqmU6HL1MECgKst4LNKYguJ2spxc_1zNvPLRYXMTY7G3n1D49hmGMboWfEXYAjI3-3sg2tsXDoD5K_YHb6zOZ5ySX-_uMxGIOzQ1b8fYBA6A7XUtsT2XHIIIngfoT4KIKAqIVVlwDFrPGhb8d0nzZc1x4A8u7fjGH58sXpkkcfl-IkslXERNZQWmaBh_3PtpkcRbwQu3FnrmrzLvsfQJZaG5d-xji_XQWA4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25585" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25584">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6VIEaoZ67vWjGZulECvQt2voN_ehUgfQIdvFVToZFYM_SWA3iVsfUUFl9IMMamH1OLfhweJtT_U-evjeJCo2vs5-gPG3rrYt9IDHkX0LQeRTYB2BKbjMNkj7FVIjL5dcvl1N0sUGcwDg-c4RRJ_UfYOdOg7H2thX0iaqDzxcZ7xEcJO6OlklbSiwKHx0FXANazYiFAd7_4mL1Xd6ZHcgQfNdtJNIZpHXsTVRY-wHvr6SMaxu-yQIcaL8qSdrB9jRltn7popA_TysTufE8p3ByCOD-vhWEyG1uCqoB9aXSqq1ynzGtEKf1QFIXLTvEYgjq_-Nd7wEGhUbPLDshzdcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25584" target="_blank">📅 12:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25583">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckGRBR-0L9iIY9lRoxQwihpEFT4BWBjJ3KDIcTjAsGmDk4AEUZ-pGwY0tp1yOEq68wEPTLCsMMBrOsGW5TSlARU7byp8aBAhnTjZY1UzAubrPDDHPlVKS2EwgW-EF7qRNBdaWutUH22Bdlcm_Hg-wmDawpmNPmSSwFrf6tMI1mL2fFmj0M6ii8T0sxpNUjDAvZpsve2k19IbYLwoVIHTZCu0IvUsb2k8wTjeVMyJTwsI7vUnUZdNuMs2T4L0-O6LofpbacRjXHjkiRh-KXH4zuRXQPfvzkr_ayfh35uzGzKiVvunUTZuqPL7mQi0eErs7duOWzJ5pXUUhYFNPx_DnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25583" target="_blank">📅 12:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25582">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d328dwc68qtKENtkANGRquPqnLvqtLoNZXn5brP02W1ZkUa0aHF4pDV0LAGcoEGN_rzVB_-MhndWpNCFfHcZfTwMegdwtyHWzUe2y7E3SpTm9KzjoqZvHUD34vFyvAverh9QxfZQYtydQmDJg2sWKg9JagOQ27yIpi0kvf9nrqblDFpE9NDMrHd3PV7NGfibtJ9Rl4T3nvC9k5Xvto2bwJeW6_gx3CqRfNIZS2ibYSG08hajCMYVVymO9FUS-QH0mQ3e7nBvK1sYhm1O8WQypXxohhmcmBQ87LOtRbbEsovvSQmCW034YynBn6lATOrGAaHKBEHh8kNdiF_k73mzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25582" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25581">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEbfLhRp2tYYR4DKlLVbIO0rH2KQJuBCmxfTv8CEHfT2cEWMYkAGB2Qa4w0cogikNLBXFO7PReuVfkkUXvq843imWWXXhETpVcWHupxT8sNg9oXIumJo7yg31rtN3kOL8z3yNMpaCLF7ToXwelOHCQwli9_vMsPvoFw2bvxso6yFKYsfC-9X4jQtSS2ToJ1fzrgrGYWgBrZ8UksqMsL4Xp9qXFaIsimA_5diatotDXyj-FPQdH1kGtJrRzF1-N_yroFZ1MMFt_8qIqSBvHuvOsj-O5dX4klHstJ2HQGKGk65FYG88tGWRHcOdsTb3TT2m4f5KzbyH48QYUNucvcJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25581" target="_blank">📅 12:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25580">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I03wvIJjBUezhazwRoIG545IyWgnq4l5c2Y6hl5qPBsi6ZQ6WeySH_bECrxYAkfVaZIUeRdqBxa2BsMV_mYOfriMHwmP8jZiRTgtguA14eRGu8TVxRzTNxL1paQKcfK5ZOt9ADG8fGgh2eOymOl8N6W3q3SzicdTc_D4fj1UTEwZEMbQ3wZgjIF_FPcQJv3X9IVCl18BlGtv7fyaQIre34QaBRUu0G1yqosuwUMJjL7ZaBfejt9aQNtcKDMBNOKOMyod4XwJEduLmKOovQOPY7icxtgzFJvroL07Dh5N3Ot8BNKBHJq76pIydKTNHXgZ_NkY7YNoxu290bkGEo27bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25580" target="_blank">📅 12:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25579">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3YUxPAMgLGyYecKWObNA_dHFrouoXrBEXXMODJrYOyJnbQW_h2h04qRB8tttf4TGtifL0zZ0IJ42BQo9177kVqO0tBY6hlzSUSx7y3V75Zm4y6bIIsp0OVPkbeNStiYzJhQx1FE6M34ZBV4zAVBnMA2EWiOZPQKw6ibsOwKkIABSLNWu1kj9dyW_Pqrl_SVicjHmLDoYuugKMUt30oT8mCx8eislybzFvGtsjJ2GWK92kJjt_fp-H3FbYFG195kLMsSKBuX-WaW1jFYOG1oX6Ukz4dMzKjAh5Tys2r6W96T9FXahERCi7jXgPZYFHZ2JzaMie59fjWWWirYftVj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25579" target="_blank">📅 12:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25578">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tod5gKFGTLqzaK7MUOZ5wl5lWDmmDCkvkcHNHYDPOiC0K-N_daFyKSTkbG9P3xxqmkYAzIHR6UoMT3oYS9IPlv-tibepmcNC9V5d8gYY0FL-GFKJWvnqjuIFcZqRjasHAwg4xvp-0uvB0VvmY-b19E9RhcrLzkfaHgF9rtT5gvZElHnAT0kJ-YpcugTF_AIQrhiGEZY7sQjDmEEzfA_0uOrEZfNg8FZdBzU835Vsrfm-h7ATF5M1jmcNyVJVCaeJVXGbwmq0R06Vf9jiCKKbwH5MmOe8tIc2W8S-3vmwNGHXUpuUz9EymIKQ7ikqOapKbdCJRYxa595JZkJXSvrVSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25578" target="_blank">📅 11:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25577">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvxQfsulHw8G6IE_17woquaHtYk-69CaDHfnTySj2nFS-cvIL6wq8L13saX1KoqzWOzIWsOvLwwvkP9enBqHhE0vp_nHcOV6Niud0cA2NcJTYAf4AbgutZ9VuUYQ1MIxIq9yjGzOaQlsPAHEiAG6RC2NjM0vgZT7EJrk3rOF2gkI4m046J_aAlQazV8y2e9WqR3Ec2T1PGPIPS21SDL8Q30jvjKLWzrL1AZxp5oTw5-aEOVH0L5zT3FzYMhJDbTVYzjjtO8MyoWBntidB4cTuM5R-Ul8iVDtvRrrJJnwJmf92jofZYEGu9WtHkcWuOICSrRagG6koYuE5WliPy6Wsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اقدامات لازم برای زمانی که مبلغی را اشتباهی واریز کردید؛
این پست رو سیو کنید و بفرستید برای دوستانتون. ممکنه یه روزی یه جایی بکارشون بیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25577" target="_blank">📅 11:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25576">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfjyPrMK9R_pZbQnD1qGvmFxhwB9IvfyVTd2ZTnh02cDEIqqHPuju5vfPpk6eRcQkgGwIieL7wvsAg_vyrHG71WJ010OefqXoh9cXgCE0Bf0M2o_zelhDdA7H8MbmaENhNsgPCgQRMFza7d36V6wgfCkZa15gE9fKvJjWWLCAz0qnLpF5Blh8665yGTVhTWTkF3gNVWWMU9W4ChVctyb2XKnNmkQDh8MvdjTynLJlcFVDO2t_vAxwVKnj6mRw3e7dRA37dnQLyoeEAphas7EJe3GoottItPzXyvIEVH0TSDXCT1IhguVNHRHT2bF5Jbkn_ukxHaGiz0SHDFjPn_NUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25576" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25575">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq1ez2_KTZyRWR8-9GMKowEju4bwoCnhX68jB-iGQZu1xDZHUkGg2nmptfPsAeD1MbobVWuG-PI4JY0clRKEiXzEyLYsxg1JAjNOdiv-x8RDgXEDCd7TBRFFQRc190LBQsPRFxMH0RTdXNrjS64Mscv7hBMGtZpJ74M0l4h_C0N2OC7rRsnBiCpsU6_rN4U9j8NOdnwVPPx4ZFLQuLRWJQdt4UE7c1MqKbrUA5SlP0wrss1L8EVsi6hhQ47i_EMR52gt8VQRJTnVs3L47aCX152waukPSZKngUFAbxTuff_LQAdfNhhfVrwLFre3qOxp9UAEejgDNhuXY6wyQQjKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسپید و این بلاگر آمریکاییه که میبینید در مرحله حذفی جام جهانی طرفداری از هر تیمی کردند بلافاصله از جام جهانی حذف شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25575" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25574">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWtGBaZJcd6VHtnoG9zT8CRyH_tqs8bY4L2ibxlweWHG6VErds6WD6s6h0WNP_GFARFB7APjKAccb3mHqIYtZiO0Cyvo53bWT3r5NByVR03CYXZrctfaOxyTLdCnCBiY7ntwhO5aUk7HlJTILL1mdlWatHfO_647nrZUxr5YeGnbVfNzWis09v_xFsGsETTUJ8RBi757bMR-1ghgzesvdALyydYBJnI4coe6ZrWFaxy2-hLU4hi3KhuJcp1cpm9G0Fnyq9LuxsSxZOoGGNolYWiaqj2PyvB141EnZ5arxvOm_eQakd0N1qJN0fMXsO59aleP-UvUsUDBBnev3o45wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
امار فوق العاده ی کانال ، کافیه هر روز با یک میلیون شروع کنی و اخر شب حداقل 15 میلیون داشته باشی
💵
اگه نمیدونی تواین‌روزها چطور بازی‌های فوتبال جام جهانی و والییال و تنیس رو پیش‌بینی کنی با مستر تیپستر همراه شو
😍
‼️
میتونی راحت حداقل 15 تا 50 میلیون تومان در روز سود کنی
💎
کسب درامد انلاین ینی زندگی راحت پس این کانال از دست نده
✅
لینک ورود به کانال :
👇
https://t.me/+HOIRMsG7xT4wMDM0</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25574" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25573">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=TO8p4ajamYn2GyTd-TOkzFX8ETkXn8Vrl1D-ugTQ9lCAuceprveX4FYgIl63IQ3X9TITttsvLkWch-NIrqjKqQAgWOMTHOVg4LW8srKdZCc_zlQ9IufcHV7NOXt2QhV3ve7sJc_1L0bXc9HLSFXFr1DiqdX1olER5v-smDgRaEYPCigyw0l0JtUndbKAtCHcxZ--4X320v60Bvm4eNwlv_y_3IEpwFUTQa8sQ_ZJrDnF2ejbn-m7yr3GmQZ9QDosjaXXaehp3gLeyBcNxf_pONbf7fUjiGUt7d_75HEWzsTzOXEed2BaPkHL6F0vXvUOWAwFwMZAHyK8oT6rqtsbUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=TO8p4ajamYn2GyTd-TOkzFX8ETkXn8Vrl1D-ugTQ9lCAuceprveX4FYgIl63IQ3X9TITttsvLkWch-NIrqjKqQAgWOMTHOVg4LW8srKdZCc_zlQ9IufcHV7NOXt2QhV3ve7sJc_1L0bXc9HLSFXFr1DiqdX1olER5v-smDgRaEYPCigyw0l0JtUndbKAtCHcxZ--4X320v60Bvm4eNwlv_y_3IEpwFUTQa8sQ_ZJrDnF2ejbn-m7yr3GmQZ9QDosjaXXaehp3gLeyBcNxf_pONbf7fUjiGUt7d_75HEWzsTzOXEed2BaPkHL6F0vXvUOWAwFwMZAHyK8oT6rqtsbUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25573" target="_blank">📅 10:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25572">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTog8reJ-fBd2ywk2HDaakLIib3JJnZ5-MLUkXtbdq7P0UC18RBctYwaB6V1IfdwdcQPrD5rSYCkggSGA10F-M1KzrQkGHYVa6SlfVxqXMkiWEC5q2scQ3rb_FHkvfL1ptv0ws0826U7i1bv9J4R302k4lU84rTebXfnY_dM1qr1Rb936J1N-XoWRPi0kCohc6h3uAqAHXGedQjshUB-4mYYsKfdVT9-z6m5YjfTZhZXqIaPVJWWZxI1TkLwtbO3k_QMBB-Qa18UVrx9WIkXoGI7aEUOiEa-xqmqSMyp_ZMZA2IOP7vhgEdoWlE7-i5530IYL7TVgKxn2czIpmuk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25572" target="_blank">📅 10:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD0RKi0c_Hne1dusaJ9CMRyRQf0n_y9FSxHCCZe70F67NkBWbKa4--MNlZzC8iVoETu0EaeXh2NE5sbUxD32m9edwjx7f-EJiVN28sRu_6NkqnXUW3_Rmkt7X97NYOrM3UL4zxQlJPv38ND3n2oVwKqOJjtu2pqzeWufy_0SecgPnshnOTdnpqLFQwnTqI2JTpysVj6Ez8TGgcAPJeHYLd0iZyZlKbDVQPp3wYKodh47gdBsjyTsHtBtvVQJWiWiNgTP0iNIEVlc70k6bVNaZ1otyqPrnJyomZLE9bYHa6WXMTcHCsPQ5uW2dF1W4hjXYxKuZhEq796O0VZErWhQnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25571" target="_blank">📅 10:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25570">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=RbUOGPLnKD5vV174ueVwoLWMoIWx8JDS6jwtE9FIZ-wuR0mnPP9aOpaoPmvP1BkdntRxS4XxRDQJ1EcHA1N9zkA2IBlTAnsv0laaNtSdpeXcRUcX5vidX_kBba9vW6K9xWOvfheHg4-Rp1CZoDuyTCeqoZ5NYdJMH7c9yvwzVaAhtM3gPr0oQtyBRUzgoiMj2kJIVT4UXfnV0H_1vhvn25g60G0Hg_GpVvWWS9qXxiDsNyVBUFK7yNDSK6s4bJ_daqQ5f0b26UbuFpbQrUC2M-cg6P7vLSQRHbwmcEwHaQaLROKaFArQiSJfPWoaWjzHigpGW25P3KgepQfn1FhKVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=RbUOGPLnKD5vV174ueVwoLWMoIWx8JDS6jwtE9FIZ-wuR0mnPP9aOpaoPmvP1BkdntRxS4XxRDQJ1EcHA1N9zkA2IBlTAnsv0laaNtSdpeXcRUcX5vidX_kBba9vW6K9xWOvfheHg4-Rp1CZoDuyTCeqoZ5NYdJMH7c9yvwzVaAhtM3gPr0oQtyBRUzgoiMj2kJIVT4UXfnV0H_1vhvn25g60G0Hg_GpVvWWS9qXxiDsNyVBUFK7yNDSK6s4bJ_daqQ5f0b26UbuFpbQrUC2M-cg6P7vLSQRHbwmcEwHaQaLROKaFArQiSJfPWoaWjzHigpGW25P3KgepQfn1FhKVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25570" target="_blank">📅 09:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25569">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0U8ZUlwXcFoNFrIyFqbXqoeE2WBXGYL9xP17Dzc-JU4BeUHgxP3EshYxDVA6znx5YxfyPvD1yiqHxAztOAvTcQjHXPzN-ASP5S-GavwTWw1L544lt7IfzZb2zy2HoFRUSLmXCfnHCxXGYnzQNLshLMFhIxMNPetHXqcc_JC1yxXsm0atOuaDj9X45C8c6jRlJ3JtL3WOLR3WWFZ-RPQ-o26jSTcOqPkrsyTvvERD4BzgKsmGZH5RcQ6bPnrLLGzVCUXWSat3WAuEjpJALwXV-_jlDSB1KzCXQPeXIo3b1oyaO3cIDGFGSPS3QBlV_2KYH07gZ67GxyF7X4dTTQn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25569" target="_blank">📅 09:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUnMzJE_OeoSgPgNse49T-_tOlg3ey2PBiXCLxVZ8gTttYFQwKB49I2u7gudSdj4PIYyOnJhwhG6isApaFjwb5T-1poAWnVdL7rA_FhoxDHDLLTMEOcF5fHtrrS-9YzHH1K1-iJpPBDKxBycdPksXYIt5yroCOUQQpqvDkbNtv7xjrbeXoyypao5Hf4NZ5Pqlm1MaXWdjU-DmiMmIUOlrV8dleMDWJh4Me8c8rBLycXJn_l2RT5vkhptOu70t2yhDAEOxfC4AyZwceJDlSTS6IcPWaZGDvhYO5B-_uauVQadkMKL4Ph_P0Cvpn-exUYLsk93_oxQhErGRS0riUSWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNwl_NWGZ6y4fKjwIRzzVR_M9TqGlm8G-GYWfXG4ghC6j2x9lGtjmo5IN32pJGj0ngc-bCcOVq71ufewL4V1IyxyRBnF1fQfKD11fthkG2aVeH9VZbX3fCY8wUzfEGD0f7O5_GxwBHuDxbPlFXxeQhijt9l4m-wgUVenfzdlGQKvjvUjKKRPFU4un1Gxnn0rf81-oTcW4iQKqZsWs7j_EtU5kevFl_eWzLFAgbugjwJkhoIpKtPcwag-9a-1SEbUxOTzLDbH7Ee84Qd1zBZBQsNOr1eaxn9tHqJVgvYtJuTQQeOoUJ7hrwpM_oJ_hIn27jRnluv8C3oXZqwo0VfygA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25567" target="_blank">📅 01:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k97xgpDOCXoZQgPdQtIzo9-cDj11NarHkzrfkBxl2uxKewuxJPsGHR-Jhm39rEHbWwY8M7EXSac1Ib7c_zObafZQix0FjzIymePmFXT9lO1PQL1n3n9C-5jqMzuPAHJ9xgazKiaDXAE_HGRW1yR7nVswm4nK7T_YNz3uPJLDhXcJsmBckbOJNrIgWOTlO4B8UwBV18tp4GQjwdhbjws9MaYBdu6fkz_gC1P2qL-088VabBZNQbRFBiDbSrew3HMuZsfcF6yVJDDrWeAIgP32x1vr9TOhGV5LZoJulhnPQAR5JuNlkzVg_xnfJsMFivXzCIwCZ5CHHOuKC0oQprUwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25566" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=LHKRBOLB4D1aKidXkU75gXlEMrQgKyF1_rySNzbGTGxqvRNfKPLOxRdk1kVDTmjLo2kOhaLzlZayanFhW2AGK0ae0XAJPg_Qhgz7xtRZpq1c41iVI6LwBo-lgWJw52UMKozWxXs_smWWSil35dfKkjFe4qqGpJTpzccoEZaYFD_TxCZuj_EHVzHXyo-XUG-h7Twnx8P_dcNcnnEZ1LepLI4JGvOCJV9i9kEZe1zKaeb-9HxrYo7vTGS4L-lNccHFqd1BmmXkvYd8qed4gvIbDMu2WcPbNYNmkkKxDie0_Ov7gm9oixAzVeeWRuBvDTF2v8G1iI0eO3L8_QC2xxgHpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=LHKRBOLB4D1aKidXkU75gXlEMrQgKyF1_rySNzbGTGxqvRNfKPLOxRdk1kVDTmjLo2kOhaLzlZayanFhW2AGK0ae0XAJPg_Qhgz7xtRZpq1c41iVI6LwBo-lgWJw52UMKozWxXs_smWWSil35dfKkjFe4qqGpJTpzccoEZaYFD_TxCZuj_EHVzHXyo-XUG-h7Twnx8P_dcNcnnEZ1LepLI4JGvOCJV9i9kEZe1zKaeb-9HxrYo7vTGS4L-lNccHFqd1BmmXkvYd8qed4gvIbDMu2WcPbNYNmkkKxDie0_Ov7gm9oixAzVeeWRuBvDTF2v8G1iI0eO3L8_QC2xxgHpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25565" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=lpX9K0dCKbz38QHB8ldw2F94mPNNQnUVeCTsNzLSRaWnyXDtupADv1CMXpBzm3kin-gKKJShRJ8AiMr8Q-2ZJXK4c9hMRx9LTSgAM4n4ACn0iqzwCDu-Qz1beOnht4v9HqMMWjEiucZs1PdW_MncHf7CHYjQN3ssG4sY0ii4uDE5BDAn7k-H69cwWDNB0MFQLm9j-kulXFoEO0HMyMs67Y2ZBD-M0oniC4kPUcDfpL1-De4kqeDlEcJrZ-ncO8uPVin2Nf1I_YjYjw0F-xvJ7dJI5CgvpH2Yvfmn3coBa3cDbCB_fTCBp6sFJhYMZO3UijD4CHaseMkR060yUSBjmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=lpX9K0dCKbz38QHB8ldw2F94mPNNQnUVeCTsNzLSRaWnyXDtupADv1CMXpBzm3kin-gKKJShRJ8AiMr8Q-2ZJXK4c9hMRx9LTSgAM4n4ACn0iqzwCDu-Qz1beOnht4v9HqMMWjEiucZs1PdW_MncHf7CHYjQN3ssG4sY0ii4uDE5BDAn7k-H69cwWDNB0MFQLm9j-kulXFoEO0HMyMs67Y2ZBD-M0oniC4kPUcDfpL1-De4kqeDlEcJrZ-ncO8uPVin2Nf1I_YjYjw0F-xvJ7dJI5CgvpH2Yvfmn3coBa3cDbCB_fTCBp6sFJhYMZO3UijD4CHaseMkR060yUSBjmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تکمیلی؛ علیرضامنصوریان سرمربی‌سابق‌نفت تهران از بیرانوند خواسته‌قبل‌از پیوستن به‌تیم استقلال این پستش‌رو از حالت‌ارشیو برداره و تو پیجش پین کنه!  علیرضا بیرانوند از چندپیشکسوت‌استقلال خواسته حمایتش کنند. منتظر استوری‌های حمایتی هاشمی نسب، منصوریان و مهدی…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25564" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=cj_hUQHyC_ARMnRJVzyDyPqZWt3cTAaMGC5dUuGPCtXklFuIvnQeOGHQ6LtubcW-dn-soeAYc0vzZRX338a1ZAAtniDle0Hp7yPX8vZDNq049YkI4btjw7rtPpVWyN7Jo7NmHkpO7eFbeCYod6zwJwng9wzVMKb1b71iinM36ge_yoNw7QwPEC2QPbS37W6wgcUzTaKqJLAscn_fsJgqfDFyYZTNI7R-5UJCjyBjvT_pro53t6x0B8FUIeUPzL5tDm_41luwp37_7hqyNFux2u1kGRdo5mifGGf6hYNoL6ig6TCK0fTa5SklXF4VEU_0JSzi3dJRINe0BWicUVGaSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=cj_hUQHyC_ARMnRJVzyDyPqZWt3cTAaMGC5dUuGPCtXklFuIvnQeOGHQ6LtubcW-dn-soeAYc0vzZRX338a1ZAAtniDle0Hp7yPX8vZDNq049YkI4btjw7rtPpVWyN7Jo7NmHkpO7eFbeCYod6zwJwng9wzVMKb1b71iinM36ge_yoNw7QwPEC2QPbS37W6wgcUzTaKqJLAscn_fsJgqfDFyYZTNI7R-5UJCjyBjvT_pro53t6x0B8FUIeUPzL5tDm_41luwp37_7hqyNFux2u1kGRdo5mifGGf6hYNoL6ig6TCK0fTa5SklXF4VEU_0JSzi3dJRINe0BWicUVGaSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25563" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25559">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXjfaI4N6DqAq8DRaOV6ErMwb-XO9cHosYdU5JloN27wdPMtcmjPOJIfYCt4yw9dErHuMRX4NP4vNqwYneiMRzRAIL7hklgz2ByBo0RvGQ5A6GET3UvX7pLvCKSmFXFe6EokmeC7dpC7WEQutEB2p7Uexzd8T4ZqJwsfi-I6EELAx0MTP_iW3EmNDwpbq5sEuBRSGYexuSGwN7JgGXh5nGzC4DOHqy31fSao1vwvyBCz2hztl1LGOKlOqOgvB5OUsNoPOU2aG-G7qg1UR0ZWlldvwIdUYUApsZDT_YqGGc6OinjAZwqTKTg_EqP9xHOwPzDJvj8RXzBPLG0m-p4LTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25559" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25557">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtOB96F_7I05jv1l7tsydO3lBg01ORBk1vnl0rGmQh_uD66_3ZbFWfLDeg-nsbUpR-AnEwHDrhUYeV_zZJrp-655o6bl1qVS5QI7MyZUhonrR5FMi9pRTHuODlwnLH-4KcyJKaIvTnepBl9dKf19xyEEdElnssrgrl51r-w_JBhd1x1AyeyM8UiikJp0afrySdTNdEQ47xwzKKcXx6UolUh8PgyxEOf5o_6bGNc4Qj8z_EyE57G4G58cQ8RUA_pBbSklJ4xboLM192nfhEc_88DatQnSJjflGiVAlFH0OpCDCyONokEsNw-4xfSVfrSmM_VJ4TALAxdgTnAIlfa2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کسری طاهری مهاجم جدید پرسپولیس: ظرف 24 ساعت‌اخیرکارهای‌رضایت‌نامه‌ام از باشگاه روبین کازان انجام شد و فردا باشگاه از من رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25557" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25556">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs_m6mqF_YsKyX9T8IP3q9lKrZfvTXgMBlJQuEKRTYPhTbUg1Nm5FdhegkzGmZkT1SmfKNuOePmuCa80WISUb9eyDPU8dp9mrdQH5ENT4mATbu65RgvkMCjW8D4_4wCnsBS8DZZmLjrNO5f1_kMtO_NZKjlhYvvoNwauJGOr26KjgV0I7uU77PSZ9Ms6E3RlF6QYsHcnwkDhaHTOlDCMztbPdOEJ6FQAWskcgIaWw1fhz9oqJaqoitATlpYLqX4Zl_dO2eG8SBADItPd8mBYOK8pukHJ6zW1vRUIa1oKaar7_-LO6w5AOuxoMmVPZWnXaL9_qTFqH_NMoJlKZvw75g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌عجیب‌ زیکو بازیکن تیم‌ملی‌مصر:
لیونل مسی، بزرگترین بازیکن تاریخ فوتبال است، اما بعد از کریستیانو رونالدو و راستش را بخواهید، حتی حس نکردم که لیونل مسی در زمین حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25556" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25555">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=AN4KfLBZcQlcgT9rNqE-73krhORZJO7wCfF9EXDKbJe73Ux1xyiT4QFiZn_ctwlx2cNdh6x6G4k6kB88LpceBWmJP3mOdBFux5nTbJ0FD_HzUVvJg-Vnl0sq3e7OTTygFSC6SZTGBHvBEmNC-_tQxeiSEerG0Ya51SydjDhUqzguhCD43H6l8BkrkFTDJ5BEQbvuJ3cOyRxcZsjElcjpS7EsrlO0-Xkc9seWXylbn2E-uNu6mTPz7KZuAzCjvM-xdhlCeRwC_edMFK3-Ns3aqOSRhKb5THHfs3BAmTmUF87NMf9V4oSTvfvFwQoDVMYAi25dScK1wLNRHV-MY3V0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=AN4KfLBZcQlcgT9rNqE-73krhORZJO7wCfF9EXDKbJe73Ux1xyiT4QFiZn_ctwlx2cNdh6x6G4k6kB88LpceBWmJP3mOdBFux5nTbJ0FD_HzUVvJg-Vnl0sq3e7OTTygFSC6SZTGBHvBEmNC-_tQxeiSEerG0Ya51SydjDhUqzguhCD43H6l8BkrkFTDJ5BEQbvuJ3cOyRxcZsjElcjpS7EsrlO0-Xkc9seWXylbn2E-uNu6mTPz7KZuAzCjvM-xdhlCeRwC_edMFK3-Ns3aqOSRhKb5THHfs3BAmTmUF87NMf9V4oSTvfvFwQoDVMYAi25dScK1wLNRHV-MY3V0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب فیروز کریمی کارشناس شبکه جم اسپورت درباره صحبت‌های طارمی در رحتکن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25555" target="_blank">📅 23:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25554">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Chm63u4G3NeAZwwjLrahuHjpm1nMHfbz6FQmhMmmwrk2VuOqFJTyndZsYv0tDi13JVv_TUOzJGIe1cJ6JMqRXL5EIQcruku9A9sG-xz3kBsOrOAToKhHA7Yc7IihRHAPFO0IeLWWaNBzEymprj59HV2Yq7YkRtxnyeDLhTff5-zFbxEALn4ojcYAepJlptfV6rpEpoSBaQtbv6MoHaAQoSU593pNzXA-YnjmMk1vFRekhykYabVSGnTmKhRKG439nws30BfgUQPkm06K4Ch0bziXmF-1-HqGGKQgSG2XJnsi4JhUb6NS4XrvxMaHWw6iOe83CtavDzNhqA7st12LHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
رنکینگ‌شش‌تیمی‌که تیم‌ملی آرژانتین در این‌ دوره از رقابت‌های جام‌جهانی‌باهاشون بازی کرده؛ به هیچ‌عنوان‌نمیخوام‌ارزش تلاش و کاری که آرژانتینیا کردن رو پایین بیارم، اماازحق نگذریم آرژانتین اصلا مسیر سختی روطی‌نکرد و سخت‌ترین حریفش، تیم ۱۹ام رنکینگ فیفا بود!…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25554" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHryhs8wsSlP2FMuJ8j7_TP1ShSd1pinK6K8Xd--ybxfGkryTQao4VRG-m36tK74LWwT3bq4oic8NbW6m8895DhOdhXLhpsyw9pSIXG26tpfvVIyM_k4BL-vuGF2ZXep57ejo2TQ3iyGAx8T3uc0GdPF8CNWoj426kxTf1SnFxufdpEFG7Ge64JOyLf7HXXs_Mbn-F9WghVhHLi4vrn5RHS4F_lM-zbd3oozB-e4POMPn5anXGAh_S8zAjzZ-hyaVAl3TsJXAhUw2a1dMHKvHnHClB6LtHaOqUJKZc4Lx8uH_rxe91kXybZclfwrPrfmg9ZTTlqu8kxT-TiV8wdBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25553" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4XhYdhzgTV7fS1HQex2p2GLgdrHLxRvVsHd25uGIZp2gnN4E1oCg-9-bSuIqZYcUcU0kDqlxLgPf_gpiD5bugIF_yG6xTqsboLcYPH8kxHrUOTfyIgCtPHiNjZ98zvGPvtw4MQ0_2uwsX1qKE7jDl-KHtJnAYJDKj_Qaz-xo9FCypFdj76GDTPeUtylp3WCHsaICWZSGAY9ODrxDPnZ7iirbNH54no69oPv2LKFn19JT9hUU1e0nKvVlYquVGhJehPecIl0JYKCnuOCJO_dRBQybrrc3NgnLRiLOOLB2Dz3w8PrKTesZyvDTE3aCdUcs_fDMeXN10qWFrnjnLkiPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛ جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25552" target="_blank">📅 23:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📊
🔵
عملکرد مهدی تیکدری ستاره جدید سرخ‌ها در باشگاه گل‌گهر سیرجان:  ۱۳۰ بازی، ۱۵ گل، ۷ پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25551" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25550">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHM74Non24JNa-lQlu1xh5wdaXQCy8B6ym2pBGHDx-_t_oCzoJPrRgIsZRa5JTqxdJP82S8L_1aH_iystJ5IuTWdD8yQmpHEwzqCZzgrY1neWSAhNzD3bo7Xpejz9qr4e4q0TQR2KV5US1R7Xk2KCO9mGxs74lpxykppdiqmUCO2d9qhFKTE0lgvssnXFyqcqZaAQYiagZ7oJnMjH_HJd7YITHjLQkTOALDuTIF9ceayT2gHAS8qYO7b69mwoCRe8t_iS3yWjpcKjyXoLXACSpg2aCB6yvphc2XV1CeD20ZQv7auG7iQ1Nxb0ezt7TiHayw7yAV8wxnWJwn-fUywDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25550" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d726AcfHqwT6uy3FqMkqMGElkJgI2XnVghSVRO_2b3Qu0zkrzI4NfpF2AifHbjK5OdqBmeMH1g1tARMjgdH_Lf7roj9dnsY_Mh1FCgtUypzkY-ZxbhmouS-r9D7RRqJZvh48WyZ15m12UrfbXhSvM_yAeR3E6rbF26kHtdpDvw-qC0YANczciMhx2VFDm5_MXhRFaeQOktWHdELTPddrheD6QLrRtJpIjdlv8pQx8s65gTHGhvhGYCV6tHc5hH_U4776aRJ3YMeisXyfD_u-4TvKcHPJd3e-_f0tzQ7HkAEHZW0ZqofImdhZqxVPI9E_G1Irrh3VrND7oTXv5-116g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25549" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDt6SEk2_bvVQSDIF3-i5uHWVxsI1wAQbMesCeTAk-6mLLc_KzBix8kEKxn7Xb_-RRb9lN__YHIihlK2fkk7tYW0o0bP3fsLB9CmlxA9G-h8sawK4cHl-0o0FIt52I8RdQ3ACXbGLRkcMom9OyBslEeUXDfQMjXljR4pklayDcO8lUWp7znzjgQaM0921nmJhMx0eUW4zjfDkHxdpw2xEASGWE0PNv87NwkVNjcAOGXPH3FcNVv25kdvUEYJDuRRFBF60sEnam54bFzleVt47UWhDRmAcRbt-9lzGih7h6syITRo5oFmb8UO8-B6aHJcDZcoVRNlXzJrf5a7nLygpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇱
فرانکی دی‌یونگ و همسرش که در تعطیلات بسر میبرند از چلسی پیشنهاد رسمی دریافت کرده. ژابی آلونسو درخواست جذب این بازیکن رو داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25548" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2MBkbsGigobinCQ7J6lAYJVoRXVjY6QxsdPcXPB-oNnIc4-7IyyL7CmYpgQCLQBWQtCeFvyJz0fHgg1ugJYuD9M4HeYmt0FHvDkR8f3tXC6WM3QS8y6ccoQi69XKSxLPpLMVYwp2PYcs4bFZNRWy4H2mjKtoPNEo4mV8232WXz0AUZ5ROYWJLrMTOJ5kzx91XGzz-omZ3vc9Kjhsl_xVv3qtp5fk30uUGPdxVZtTrR4xHms0Xn5j0iKfB273gjl6KF20dxehqHvLHsLuaAhafIixwI61LmMepWphZ7ewRX4iTZRW1hQepZkn0ADRGFAL9UktyM95DtfUypd3p1p1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌جزئیات‌ عملکرد لئو مسی فوق‌ستاره تیم ملی آرژانتین در رقابت‌های 2 دوره اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25547" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2TKv0usvV-nN7_SXgQ9OD_pKAfCie3GYBi322Kv58x8zxq71DmlNQonGzBouG1A5LLkCgtQlEGds7jqK4FRU2tcqCr66SNgZQtrKZI5v9t5nIWGCYhLtKjsVRHQwR_zdPYIv0ouiRi3xQb5E5PGkhs4lF0q3OA__SMvWFGGmE4hOXpxzJHsoZSF81eJi7Rs_eAGieClQzpdb8Jgbe9f6Tr3TjbVGeEoD-9BAk0EwV8l6Jhi7Y80CpIF5irSIMNsjxPeWxNgjZqa_2hIDnftbcxOKi-qp16--6-TWAHTPIx6xTHMKl-cblrXTKGrUDOkE7OvQnRYwmfAHz19FGw49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اینفانتینو میخواد فشار بیاره تا جام جهانی ۲۰۳۰ با ۶۴ تیم برگزار شه. و ارژانتین و پاراگوئه و اروگوئه هم یک بازی به شکل افتخاری میزبان باشن. مشخص نیست فقط برای یک جام میخواد این کارو بکنه ولی ظاهرا عزم راسخی داره که این پروژه سنگین رو در سال ۲۰۳۰ انجام بده. جام‌جهانی ۲۰۳۰ با میزبانی سه کشور پرتغال اسپانیا و مراکش قراره برگزار شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25546" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB_W-N6URkdG5DXuiNRGtqPUOumg9ZnaSC4p0JSQwizLUteS46WlSL2U01EnD3G5Sunt67rWchiG2-m8NVirGla9vbyvxpjpMyygAhUtzSHxAjL2c_SWyeEdgUfaqxTNDD5ovhXTTUW9vahrKCAlyupOfGAJNUt86GivvKPgJ_cIKTQHrtkDI5hcnluYm_noaY0t9rFY2RjfczMj5rIwBx151iaB83b-1RXIdFrRw1QGibc2yxuUBj5SSy_bpqIIof_DngWEVxcdOIdHmiGlJz5XmbOwhA7-gNFKlGSVQFlCHeEJ8IWWPXwFGLzJVjbXNlXr-CfcUSWxckvTU6rqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/25545" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=Scme0ltolIaEm2clnRc_WJzcbrn07FRlrj8FJgvgdbLxjOCpVdbOeeMjVLnhZFyQIce_sMJhDbGIAQXziRq40zNil9j4OAvYWYjRBn7eM_1jVYVBOspthpHsKjUZgvCD6VcnicY1wceg7kLFPsjcTUwlWMxscwliuYv2APvhhC0gwltcnz8cK-9o8pBsGudjf-DQhVY0p76t4wHG_rFPynoGngs8G6N-cAJd_UafIT9r8ESxEc2BmQdDOFQf69tlbIBQer1iUfpaasoUdkjpmUw1F4LYIXA5m2Q4rH6WcxDt684R-irtKS_CYoC7W3gHN4t86NA0VwEK_KO_51t4KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=Scme0ltolIaEm2clnRc_WJzcbrn07FRlrj8FJgvgdbLxjOCpVdbOeeMjVLnhZFyQIce_sMJhDbGIAQXziRq40zNil9j4OAvYWYjRBn7eM_1jVYVBOspthpHsKjUZgvCD6VcnicY1wceg7kLFPsjcTUwlWMxscwliuYv2APvhhC0gwltcnz8cK-9o8pBsGudjf-DQhVY0p76t4wHG_rFPynoGngs8G6N-cAJd_UafIT9r8ESxEc2BmQdDOFQf69tlbIBQer1iUfpaasoUdkjpmUw1F4LYIXA5m2Q4rH6WcxDt684R-irtKS_CYoC7W3gHN4t86NA0VwEK_KO_51t4KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw48efXVZvi3IEZCxVTcj-A3eDog3gnknaO7NfAzgVixa_CuC8P28iOcgtgFi70qtSmOd8Dqoxmtu3TCbxy1OrL4N-qEDGuqAlBlWyDcMnxu8i34LiFqyNMktngUnBEJ4luPlu51O2ikvI5HlivhJKEgF_e-kbB2GrygwsliD3ydpxveJT7dJEJ5aLN-PVL4MOtiaI9NklNq3A4Qg8NDNpnfu4v3BAiMX42ScK_n1fIe4ng8G-vZsn7HkPQUc0fe_Iec83tCkyoVI5-Qk7sw1KbcVPFi8ojbmwFf3nYFLwZtpBr-yFp2Vko6U0J4vMKIiSooERcWk2xNfUvwKnUB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_XtjkP9pqIeUJPrV-YcJIAV1mw8nnXjbe4uOMvKN12z1LwUXl5mbxpyZ3TzPEB_I9qC5cPshW6qyJIYqv2e8i54R1igyTKf2sl_DmSM99ki_yDJ4-HicagU6tYtB9w6E5KWYOgdhZg4w-_wm_2XeYpLyzZeyvwtSL6CLLH7eGttwmtr28SGnrh-vuTJp8Ugusql7XfF-axhbZpns-kFQodRLvysYhwCx5WHdSF3HUNm-C3d39GdKJPMskQTfsLwPDx7c3iuaKqC41AkqJOc5gjX_ADus6wu1IV6u0fL_lbfIrnz0qkr2KJSK7uy2nqPN9h1I2pJ7ThFk2yOJmVlUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104d086276.mp4?token=OWSmbT3eka7lVQDRl9bCgYx_P6E_YKAthRQQZhifiddiQn07s5kLgDe3tz7t6hdR8UdCij1-BvjfniHsx-wV3uOrFCBNUZJ055lLVoI-j6KnMcUE4SPc5j5O_4fUWTbbCFIOGVstoejzuSN3xWuSfX27vuomyYLxEZKlHAv9ZsYQkTzDYAz66rjfp64kXaV1srrK4veiqvMnYOEmsv1hA9O5NxqbGnuAeOsSwvBn24A7yPBf9AOcmZPWYNqEbUIdQBM8MMDe_oSgiiy0jzxHc9CzuyQ2SGW6y5rSGjcpKVlDBFVrANeHvVf0x24Z33P_ry0SrkjhMOENMAIZdGGCyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104d086276.mp4?token=OWSmbT3eka7lVQDRl9bCgYx_P6E_YKAthRQQZhifiddiQn07s5kLgDe3tz7t6hdR8UdCij1-BvjfniHsx-wV3uOrFCBNUZJ055lLVoI-j6KnMcUE4SPc5j5O_4fUWTbbCFIOGVstoejzuSN3xWuSfX27vuomyYLxEZKlHAv9ZsYQkTzDYAz66rjfp64kXaV1srrK4veiqvMnYOEmsv1hA9O5NxqbGnuAeOsSwvBn24A7yPBf9AOcmZPWYNqEbUIdQBM8MMDe_oSgiiy0jzxHc9CzuyQ2SGW6y5rSGjcpKVlDBFVrANeHvVf0x24Z33P_ry0SrkjhMOENMAIZdGGCyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه جواد خیابانی به قلعه نویی و کادرفنی تیم ملی به‌دلیل‌عملکرد ضعیف در جام جهانی: فکر کردی منم عین مربیای تیم‌ملی‌ام که 180 میلیارد بگیرم؟
‼️
هومن‌افاضلی‌خیلی‌جدی‌داره میگه فکر میکردیم که میتونیم تا فینال جام جهانی 2026 پیش بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NI8Ly6ezCVTOU0bdRdyVH2Ca9hF_T8WMPIwJDHWj9jIi0iUDXBwvKcMAsQbBe0MXC1f7hGfIveSPUVzfiLMyJGcWWn3E7wDoUlbZ3djvC3Ucmgedl-P4fa4SYdIqn9_vhOMGX66MzPGVmubOcyau9x4ijrZTHgamR_xdrrmj3G7TOeO7Hsk8omwQ1uUyNstJBv8Yd4jfI21epaKig0J3tyBqflVYoBwPpXjYlexk7G2NlbtP0cEn0fK_rUU0lO_fBp3PVDxlr5i_a34JvjbgJzFGt1D1qq8jeTujtwB6B3ZBpPqtlB3CdITu0IsyGlLJq38OEhFgSNGHzJyZTjF5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRZNWsZUl3QOQ1z8-NuBNotymPQOFQy5xOANSZMh7VWrWX0dsxg5foVsqmjl4k_yMhr4zpM2_leb58AOX2xh7huwdoU1M0C-qr5pfUGi93CQM_FbJ9CjmtkxT2qVfxPA2TqiOXxRQLQz3vSqIiDtfWJQiHfEWsJP-mdcgwF_LUqxLZtPusPBos2i8MoVJA41qqTxdd6IO8p16rRZiEQNdoj7TQnjH9RSIQGXeHaf8FMYRYcTCNwYfRQXO81-KZsUHfGNwPSMWy-vsmuVMaFqgXyMh3iXDWglgofKH2CDip58q4KwF0aQ58GupU6m96GOKw8bOM8z5Wqvg6ZrA-VvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsmilHfK0KQWfth5QsIZGjxxpJk2i0O8igFnRICd4XuxqlDNr_LFvdsRoB5V4uvroaXTWwjiasDxXd01JQ1g1cjLh64uzBnBH-IoNXz1gQOe0xyp7mKCy0EpOHNwo7CcFGL9MZGizpyBm7mi0lw5DYhZlpl3cdDSlESC7gqelQfw7kpUYgItekLdCwObMNIrZsz4tHchpFM9I0ZQuvVr3Q5BuhMMx30v1Hjlcn6IKoCIXofaP-_i1EmKPdsBPHOVH2f6KJprpJhAVwUYzjm0k4PjMjEGnrM3lHOvwI8RedS3JrYpuDbPq4qFZCFcfpDFBOlUkSOVd9jCXCnFeBFbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=lixwSy_2ilHYNXst5Jz0QHPCargyOGxiuw1MgBv7g_TxxKFsm1P-JeJmprXCoKM6fbH7OO0iFawH10Y_cJIxmyx3W2DqhbO3ZMGLtoUMaO3aPfX0fZLgmZWJzULSPRHfhklN1KUYs4FPaXI3hVMUUJb4PaEwGJzXa9byXMidYNtCDpOqYduMp2WdxMPgmziBSHal7I1tTSBu4FdpRp9mQp-CeaAO1wRSXkf-1Kl-i8yJ3SkKSbBRkldqgJwJHPpkTAOzM60Cxzt-eMD5E9iQu_y9uY4kFsPleOYLFN6_vs-dHJJLq8ZIc4YsgnKFXbRFm3pUR0jw3qD9vSU-3xUU_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=lixwSy_2ilHYNXst5Jz0QHPCargyOGxiuw1MgBv7g_TxxKFsm1P-JeJmprXCoKM6fbH7OO0iFawH10Y_cJIxmyx3W2DqhbO3ZMGLtoUMaO3aPfX0fZLgmZWJzULSPRHfhklN1KUYs4FPaXI3hVMUUJb4PaEwGJzXa9byXMidYNtCDpOqYduMp2WdxMPgmziBSHal7I1tTSBu4FdpRp9mQp-CeaAO1wRSXkf-1Kl-i8yJ3SkKSbBRkldqgJwJHPpkTAOzM60Cxzt-eMD5E9iQu_y9uY4kFsPleOYLFN6_vs-dHJJLq8ZIc4YsgnKFXbRFm3pUR0jw3qD9vSU-3xUU_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگهام ستاره انگلیس در پایان دیدار با نروژ:
مادرم یه هفته‌کامل بهم میگفت مراقب زبونت باش، نه فحش بده، نه به‌داور گیر بده که کارت زرد نگیری. آخرش هم مثل همیشه حرف مادرم اجرا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_5mK_bBi91-DwSC3dcbUMTmye6XaFrtsDtWhcRTPphA_BM3wcA1qUtpnd8V4gLacxPnO3coCM6m5MG2cNPmmIOcJh5c9CQsJFylB88QZrxYC1irSw8cZvdOX-Qup9Unfu-VtM0_s9bA63bDqjrwFjNi5qWVX1gmImIevUpSJEXJCKsuD6oEz4J4C8znQ1q1hihYIriVths-aTlS3Fez0RuAFOCoaGjlIZBpyRM9KAlcZympZsD7UFcPbjSCkD4X_wRY1aBozwX9PdOMROzZWVMhMcTtWMMHQEVxLPD_Mxx4FP_QkShV_zRBftPOOIWio-DJPFJ5vJ7iDZsdvUTZ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOWZWSULV5-Ezwk0SzksrBvJJzUM5LLY7F7_O81c_hhq3ocgeGIfeKwx8rlAT2eOFTM2LE3rosEBzh4cXGdMI8YJAQL0xzbmz0QoopB9f4nKxn4N50BpHtd8si3nIo0_E40XZwH2sFEoj2Ooi1BwVUGOIFbW1Nzg75N6FmO6Vo_-2K8ktFoApz1nyTSEtvXR-3VP6DYGrl79PSHw4ONTlmHloarou4KlIgiSZ6ykdNbJjFZcwWVs12tVq94CG9zqf9Y6-i_5Dx_Xnn2wZlIiIMxbVFcsfj0Q0ZBt50pNU0nbFOCxoBlvlAfmVD00dkDP-h6aRXFzZKkzlD1W1ErlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpEc0UrLv9CBOB_f0Iq0HvNaIQcpS_MdKm7Vg8X7vZLy7t-tH3uFYuWQTEUZB5r3oq_n8fNqTWqjGv2yOXsfoM1Q2o1zOfRWXRNRw7di0F42eCNa3iKrxWG6ctGM3yP17t77tua0GDQfloyDTI2boterCZoDabNz-ovXjATVk_geVzmCwhqzb5dK6Z4Skz8rJU_3zh7Cj_Iv1kUxbcynya-_KqwzYT866wEm4k5OPd9gmKvZyEWAsmZlzUvXiaMiO04NeJ1kNExQp3tM9TONQ78t_7RKPGbX-n3VsYTUreGelOCmlh2_NHXyTUxwpYZax8mqGXtDgMlmtCmYAVI-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=cUWsMJZZzwZLsi2Lo9Onq2zqDPSNE4Rd53chImn4qX2xfRJZUDS9olov6CRSCUBPlRD8asv5H86XZN0ZyU8EaAX94kySWH07TdoBa-k40H8QSH50JJDV80ZbQNUNfYMtK-TA8N36H_22y34Gtk9n1dNDxJQ2qrR0sXF77vaGbDbI8Z4NfuVJ5f0MD1PPfy38wvWiS928bBB9tzGrJchcPWfLIqCXaKZhjGZAMloPrINS-m2LGa5oiVeAp2JaYrXTVlq_euStreYc6PaawGek-i3c6wB0odHaecYa4H9h-uGhaIxfjxJiD8-DVNgNsAybZbm6Tc84VzcPcOp5jNe9TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=cUWsMJZZzwZLsi2Lo9Onq2zqDPSNE4Rd53chImn4qX2xfRJZUDS9olov6CRSCUBPlRD8asv5H86XZN0ZyU8EaAX94kySWH07TdoBa-k40H8QSH50JJDV80ZbQNUNfYMtK-TA8N36H_22y34Gtk9n1dNDxJQ2qrR0sXF77vaGbDbI8Z4NfuVJ5f0MD1PPfy38wvWiS928bBB9tzGrJchcPWfLIqCXaKZhjGZAMloPrINS-m2LGa5oiVeAp2JaYrXTVlq_euStreYc6PaawGek-i3c6wB0odHaecYa4H9h-uGhaIxfjxJiD8-DVNgNsAybZbm6Tc84VzcPcOp5jNe9TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=EEf9Rf-0dVHgA2lgaqSqRqeDDe_fzdF3W56-4MULU0Fg0_tCQlzzKUyEzElnzl_OnFUd-e9TO_Wyjg4rQsmEiZ5km9nQ3sm7QEIB3dicuDymvGJ1nBvxExnFrLPPBQ6mnkdIYXUip8JRLZChddJgTbhhmUsGKafl9vKEci3e8cNUx5j8b5rsiRPWEd7HhP6S73JWqw1e8UmA_nSXtdkvBUFCw_o5wDoQERZ6F2llPo5rmZhqvd2ZWMjZ6FIy5Bwg27MLguVBqoO3UndO4L9Ag5mDs9R6UYtGzhzLZI7iTtnuYIgTlRjo2zfMhypjmTdtFaWc6W6AXoVplSW-W8N5nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=EEf9Rf-0dVHgA2lgaqSqRqeDDe_fzdF3W56-4MULU0Fg0_tCQlzzKUyEzElnzl_OnFUd-e9TO_Wyjg4rQsmEiZ5km9nQ3sm7QEIB3dicuDymvGJ1nBvxExnFrLPPBQ6mnkdIYXUip8JRLZChddJgTbhhmUsGKafl9vKEci3e8cNUx5j8b5rsiRPWEd7HhP6S73JWqw1e8UmA_nSXtdkvBUFCw_o5wDoQERZ6F2llPo5rmZhqvd2ZWMjZ6FIy5Bwg27MLguVBqoO3UndO4L9Ag5mDs9R6UYtGzhzLZI7iTtnuYIgTlRjo2zfMhypjmTdtFaWc6W6AXoVplSW-W8N5nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=QwSq05gENxF4o3TOLc3jg_c7373kwjUKydwyRa0Wla1n850sRbLz3AjHhH3jN1TyZmy49KkdB0umMEfNR_UiPSrtpqLgQujQLD8RPReiRuUIylXDCvYht7AkuuSJ4Dv7iG_c02QvyZuvBMzw2db0KAk1NGbHd835NYuCyhqeYo2HJ1kCACc56q1hXpodnJQrWRDKgVLv7HbEcMEU_gnasJbybSLlKnOl7UzMbeGmnUPf4A4p9KOyn0aVyf_h6itCfsV_NSzPO7sUcMxNK5w6uYrNhFzIBAfsHnQu6QJCkyIEuJ-Gent9G_7T3PRoe12VZqb6S1scPIVnpStcpTU4oIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=QwSq05gENxF4o3TOLc3jg_c7373kwjUKydwyRa0Wla1n850sRbLz3AjHhH3jN1TyZmy49KkdB0umMEfNR_UiPSrtpqLgQujQLD8RPReiRuUIylXDCvYht7AkuuSJ4Dv7iG_c02QvyZuvBMzw2db0KAk1NGbHd835NYuCyhqeYo2HJ1kCACc56q1hXpodnJQrWRDKgVLv7HbEcMEU_gnasJbybSLlKnOl7UzMbeGmnUPf4A4p9KOyn0aVyf_h6itCfsV_NSzPO7sUcMxNK5w6uYrNhFzIBAfsHnQu6QJCkyIEuJ-Gent9G_7T3PRoe12VZqb6S1scPIVnpStcpTU4oIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLlxsIOsPzZwROJqH-gAugnqDf4dyDDGSSTr_WsuPWPAWbyAb1IWnwsU2dL8sdKAXfzOEURqVuvhnXSy1K68DfLoprOL0adBrLzaYIRcdbYZ0Btf4eK5bayPzrboU3mSvGiH9t9QRda13OaEL7Trbeh8OPPT_LufTXpvNrvUi0qEi3KfdGyH1aCfgaVX1bf9YDdX-5N2tTmT_AELjJvYRIzdLbkgv40LWlVY_NElqJlES1Fsli9SA6k0osUSixA_1SaosGiJHSmQ_3dt8z522m0LxVSMlaUO0cYP-dW-9AbnhGmywbO46p8fp2sWqpGrJ5oBUrp9mYAK8aGAxEbJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TA_btvshCT0a7vkZeInw7YiJswE2hHWCTPxkTmqi_C2cKbuzBEzxXhNrL3iQWBH6vwI6-6e_gE6xL-Pqcnaaf8SiIDXYySYE_RY3nXMAAMbJ-Kv79TG7w6WYcHcroEQuxB_SOjsz4jj0N4B_5Tu7TisPMgtZb-aNDr8rT9cOouQKOOnjXGQpHoMNg-jNpsi8orjk6L6FlGEYHn-mXeKOR9XGFHdYlRaCn_LEap9qBJuDLxJLn_I7uhLLqDRXsJvY0CrVa_7-Jzw8yKNWnqBSlmq0hI6u-pA7_I0iQkGzm0-muSwAF0OatkIXDOB7_N3vZailleQg760mkj4-thK73g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4zlG67xAm3CPG2om0a-rcWDbtuy59sosNwyNetMs7nNBHY0NOm_sbiGfHJhhYvKAsosI-ocbnp85Obe9vLAEPSxAnVzeR8QQqV7cu3Q1eTUN68jOOIp2ew8Bfx8Lj9H4YvLd3h2CBmTwCiYslycE5-D4XpEIj6cBT7OaaEcSrDs4tcqGH29_9F8NgC-tjZK1znN8i_y5pvQJany-O0wJzMEjzO4pLEvsTZy3Bh9QBZQhAGHjEtGapceAXgj8hEz4LDrjjsWQbwugPvT8YAUsa5NB02PfUY2mzgH7ntGvQTV0B5kdLXfcWJpknRrgS3WHnNHIXMa0AmgBiVSTSlT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehmBs2GQKYiUXERB2GQ3JywoKYdwIhqxCoWl2v5Pb_KC16JBnBNx8CNvQV2MuQZWQril5lZ2P8gtUO_1yeV9du54zKAl84Fd64TI3rFVIullTgaIZC-vHq9ieIwXtCnlBcr3VJVv8BW6OW6BZvvmG5XcdZqPREOOg5Ep6k_nkc8kU4DfFNqzCiDZzBXcRlSmFXCG7w4YwHg3H7Qc1duxS9UsHstHXLyEg_T0rlJm1wHWYOoDdFSodDS196Zxcpczw9PCiSBse4MUdBcgNKZUEzK3Vii6s5wVM_qWDYMCtQ83rh6pqcQuL_Z4yfC7dhlLYIRcWPna-vKwaFvEeXe_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=gPOwss4noqBtLrKSmkIw_Rx95uO-JY4LoT8P6ZNSt6uYGpzggtGKRNNd4ODiG5_xpTrAf1ZtcELraTvyTENwH2Yfw2y72gzubpHUsEQ0t8Rlu0IGYG1H3Ga1JE8PnBJRLGOYGlx8snAVoOAhYOAeE2kNg1BlOfSEMjcjvq0qTeAKO1jM5uhwj4UYfZFTAl_-avTu7JgsOKobS_PTiO88k7E2a008s66c1qbVASmRmEFYNVD_L--Bm9PwDvdSHGsnmQ--Zi5xgEkD9Pc_saWvS40cHt8b0-LJC4vZ6ZrwWkcFAHpySClTFn4ssIBT-HTh1yhaprD-FV6uuLsedlHSog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=gPOwss4noqBtLrKSmkIw_Rx95uO-JY4LoT8P6ZNSt6uYGpzggtGKRNNd4ODiG5_xpTrAf1ZtcELraTvyTENwH2Yfw2y72gzubpHUsEQ0t8Rlu0IGYG1H3Ga1JE8PnBJRLGOYGlx8snAVoOAhYOAeE2kNg1BlOfSEMjcjvq0qTeAKO1jM5uhwj4UYfZFTAl_-avTu7JgsOKobS_PTiO88k7E2a008s66c1qbVASmRmEFYNVD_L--Bm9PwDvdSHGsnmQ--Zi5xgEkD9Pc_saWvS40cHt8b0-LJC4vZ6ZrwWkcFAHpySClTFn4ssIBT-HTh1yhaprD-FV6uuLsedlHSog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=v4VMxKGnHrlVmH31oE9RZHAdDbbEaR00Stkb0VkHe5daPei3SOdR6TCEvdA3muqDI8kJ0fFDGk2AOpG02Oav5vhj1d0P4RuO0MPWagwe-nJneA2ruKW_SQcsBF_e_V6CLz2T4N4OKrWVkvgxVyorl2elNGxEad51iM1H7Q7YYZ5GrIVEVXkH37HHwlIWUgD4uV9EjZL9c-jlHfy3Uto-neRlnnmi4RWA3U7E1RWRksdQXs4uTn2zBn-0INAMisz4V-9fF6BZ4Na4Kz--Wu9mFGKzbs0-RIE7to5lKx3lUdMqa0gE9iWKNlIb60_R3V0_P4xafuOcnV_2GbwFIQW40g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=v4VMxKGnHrlVmH31oE9RZHAdDbbEaR00Stkb0VkHe5daPei3SOdR6TCEvdA3muqDI8kJ0fFDGk2AOpG02Oav5vhj1d0P4RuO0MPWagwe-nJneA2ruKW_SQcsBF_e_V6CLz2T4N4OKrWVkvgxVyorl2elNGxEad51iM1H7Q7YYZ5GrIVEVXkH37HHwlIWUgD4uV9EjZL9c-jlHfy3Uto-neRlnnmi4RWA3U7E1RWRksdQXs4uTn2zBn-0INAMisz4V-9fF6BZ4Na4Kz--Wu9mFGKzbs0-RIE7to5lKx3lUdMqa0gE9iWKNlIb60_R3V0_P4xafuOcnV_2GbwFIQW40g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=W_aJ3J2SZMYK6m95Lv2AxX7z6MLpmPEXIounNRNUAEFE66_QAbFCAYdHTMcR4ZHZMLFb2evw2749Y2alNhoZ-fRQV9ZkyiwWCkzGrwruUs0vcblEu03q74T2vNckcoHq4yap7_0Qe-gihSgQZfSS4Ej2nR_GSXq8HVMYkXfPxPsI3zCvg4DN12lewdDIZ2XiRLTAfdgb7GQtBx4uoyqvkcoZGVZUTWMqvbsJ6B2Wi9_hW-jwhoZByO2p6_5fV9MG9mdrGEEQL2EvBtzQcYTOo-ZmxIiTLEZmzFICVTu2qjI_RQOqa7-xENFTCE1xYkQbURHItI2v4UhSKGRlLVjqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=W_aJ3J2SZMYK6m95Lv2AxX7z6MLpmPEXIounNRNUAEFE66_QAbFCAYdHTMcR4ZHZMLFb2evw2749Y2alNhoZ-fRQV9ZkyiwWCkzGrwruUs0vcblEu03q74T2vNckcoHq4yap7_0Qe-gihSgQZfSS4Ej2nR_GSXq8HVMYkXfPxPsI3zCvg4DN12lewdDIZ2XiRLTAfdgb7GQtBx4uoyqvkcoZGVZUTWMqvbsJ6B2Wi9_hW-jwhoZByO2p6_5fV9MG9mdrGEEQL2EvBtzQcYTOo-ZmxIiTLEZmzFICVTu2qjI_RQOqa7-xENFTCE1xYkQbURHItI2v4UhSKGRlLVjqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-oWPtTGRMcGWwRGbcZxRkHqYdAaX9ZVdHF8-mTTBPqn44pHoPDJ9HvD8PcB93_aZM-wtZ4r_gLoDu-_4CX9rGqSULX_tccf9UsA4U8qnFNAz0mkTnXNzwlTBK_NoHmy-K8lZL39VhV5zhvmqUGH79I8ibNyffm-5QiH6jyg6XkgoDA7vIo1i3867AOWbu2U8q5Jh9j26u5FOa91j4m41593fj-LR6m5j6bFPMPflJqUUYL8OZnK7IBXXP0ivVBcGjKNsxNl3xEoj0zzySsp2-VD7mfv_ZthO1QtHTEX9B2TvmVVtp5i8LnvFr1ClV7B6xMHL844NaJIMT9S0nT0Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6xU_0Vl76jEJywIalbvAvsEzUKgVClnHbN2SHOGkGgrqxnJLUXbh0v8G2jKw418pzu_EcYZg-DAmsX473FV1943Ot9bBh4fdAwEcHcre7EsLnnVDQWi43s8PqkegKcG5sifatBeOR8FRMilJHoXqxhdggL8gw0qf76k5VfTvDi-NFXLuURwttQXeEIrMO8FlhR-FWNvzSpSSuUWgtDjDQoTeapILCG6x5W7JODSMPJ_GST6FHi1AipGTbLuthGlqwleOfjtCB9QJfEILp4QS_tG2QM_pRLmw8wpMibHSpBymsjilB_2VuJ21QUVeTjmAlcUWVigC5ZG-X6Ib6SaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snUWiHbUV-ER9znV55EmMZOwXP1KYgGYqaiRfveRGE_p9FtX0HArGrg4eMkxS8x6HxuCkBOqHy1ov94GWLZYB7xW4VT1qYD7BeVHHnMMuQrHGjeF2WtCxcud4uIgmNHHdMy3PBu83u-DTfiVkwkcgkFjXKDsQFZXIRR6hqzJ9-wlyqIPdRkejzk73V3y2H-D-_0Ub71sqtKQ4Bmp_wJ22zEmrrt5xLvnvjoyeAUAOuEvJI74txf3rFmi8bdffeJoiX3QHzRLh0VwqJYsCPGDx07Eky2AlF6tw_b-Xj7JbvmUE74QwA1Eba9uOZcaPpNZBTvHXYjmtAMW7H_IIJGcnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSffHyplOTzGM0QitHkETPBEXQMdO34q6-XTcYRjAajfJ5_P58g1AAN4_HhIVpO6usqGMUNtdDI3AujL3TwWnnOfrPkgxGu4WS3vbBTb7Z72rZQoD8rtj5m2Az72f-uE5r1qHDWJghcr3Ch2Tgf5Gr7sfJ_e1xu1ntsooUTWb1exe6gPlGBGWmEtv7LCQF8eUPTa31DnOCFZiFo55Aqq6HKdo0C62PNbGcuCGqdAvg_HIsxnrHAJL0OVYh2yNljYW3Z6eE3AD7yXO4YVALQob1JChWZ2iVCGU4h9wbLNtwNYcOY9xJgYUgYwGEqQKxFu5cxYCGriE60bPerrErGgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5t9iLVHj1_8z-cjVSZpDPOx84Zl2Bkfh4V5EnE5n_zzG8f0xTcOtI3YytFhZXPzMlvZXR4ACSlP2Ogj7ZCnwOfHtpegOtv_0X6jEon44dcpMOAGTAVHRU_4LleezmgRj4FFQHOy5yzK6eBnfkWDFi4QRpUEIkNPqeFz92jJd2yqhvsJF2N3TElP8bU5bOUulIhggArvIpVdCV0U9lFEW_qDs2wUFbVIvGk5plX6-HWln2nuxWHXRdLDAklTNhtYtzJ7HHEC5xjCV1l-vP8eSb22O2oehlxAesn9quaq5hESPgEN7wk9mMten-ZLBdyGC2rrr8m4VhaltoJK2bzZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=n6ph_bQTvsUmQixhFstSQm1eGyQd9JuWnN3wgl9ZKdY1uth-TO65Ot3uB-RNA9zVQzWvlGbY6BLTo2grfbcT0evxV11LlSFBVsiRWlsWHtTMDGyyThVcRmGdIQhIHGdeOZTOp9qlZXJmbxp67pglZZVkfoHJK_5-5Hn_0uCMeAtkcDp--wpnbMfDRHuchrSVgUr77VttzLy-P-w70bFmKYvZgVD3GZ7BvlT8Juy6sgGxXXgIaCRSdnPyizkxPHXWzVMrU-QreuX8kn0S3TkpC43bSqQvaIZj3LDyzN-uN60OP2-zlIfXvAweMG83S0mpsW3XtHjiAIGe_N2oCmPJAjDBI0mot0qndcRA8UGYbZeInT86uAAoNqcKE3SX8JmQzw9wLP3eei3emOGOGQbBttoG8vqtUHFsh-C9uhNnH2kv9aOXdTttiNs3EWvIRyztUAmY6XvTkj-AupDYuFZgIqUtz5_h-BA_3zcmcGouweC8iWiRAWKoo2ZqAiRBuFW_Hk0hbRaue6j1l0bXJoMNpvB_YswdK9jt8r6eCOaF8EoM5eOMrR2U8GYj1pYq0BWDP-gmKc0NPKTl46IeBEiaMsav6yJ4MQNGDANca94mjS1RpW6qPQdfgcqNmJxV8CBBJm_ymiCwR-SK56Z3Gdo21a3_Gy_LAKi4Oezo5zh4fUc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=n6ph_bQTvsUmQixhFstSQm1eGyQd9JuWnN3wgl9ZKdY1uth-TO65Ot3uB-RNA9zVQzWvlGbY6BLTo2grfbcT0evxV11LlSFBVsiRWlsWHtTMDGyyThVcRmGdIQhIHGdeOZTOp9qlZXJmbxp67pglZZVkfoHJK_5-5Hn_0uCMeAtkcDp--wpnbMfDRHuchrSVgUr77VttzLy-P-w70bFmKYvZgVD3GZ7BvlT8Juy6sgGxXXgIaCRSdnPyizkxPHXWzVMrU-QreuX8kn0S3TkpC43bSqQvaIZj3LDyzN-uN60OP2-zlIfXvAweMG83S0mpsW3XtHjiAIGe_N2oCmPJAjDBI0mot0qndcRA8UGYbZeInT86uAAoNqcKE3SX8JmQzw9wLP3eei3emOGOGQbBttoG8vqtUHFsh-C9uhNnH2kv9aOXdTttiNs3EWvIRyztUAmY6XvTkj-AupDYuFZgIqUtz5_h-BA_3zcmcGouweC8iWiRAWKoo2ZqAiRBuFW_Hk0hbRaue6j1l0bXJoMNpvB_YswdK9jt8r6eCOaF8EoM5eOMrR2U8GYj1pYq0BWDP-gmKc0NPKTl46IeBEiaMsav6yJ4MQNGDANca94mjS1RpW6qPQdfgcqNmJxV8CBBJm_ymiCwR-SK56Z3Gdo21a3_Gy_LAKi4Oezo5zh4fUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsRtFrtI2YX96YOHqyYFgnOfUluxTE8SnvSSPQR_EAu3tZRrH2rNrcmh6UJa69beCKogd9UH7AsR5Wfm6y1XoTmynHJoSDMOg1T57UhiTjwsbZ6Fp2tBNJ2JTyl3OsN7g2s8uu2WgVF4KmHBHkZZqOuliKQKETuHMoTkz2RkFK8a_cXtKWXcPjfHO-zFdrzH7XHEMsukThnSFJgyeL_Qa7wr17sTizb6HOSTOm07kmmS9AhAQdw61F95rPPq5uiTlAxnrHFMKHLifF9ewmvUSYw5Ne0gg5XsD_rVZ6NwJMR_3155TxKj-hll9weoDVAAJy0ut-wHoPsQklU3Wg-OrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrvN7EuExHIBnw6KmcHoVKP0Zd8kHpYC4nVGt2vll_2hw1_vF6DhqtQZQCtInCVRTkzwN16K0cacdwocBGBg9AzRW9RGnUPui1GDskVpd33LDbAzcVfiZqnQxs45o8kAo2hP3lytwZ7i-y3oc6WtnKj-BhxFI2RkF43rfgmn-s_Uz--_azGabXEQCN_O5jkaiDOu_iVD2nzldEX-Wc5QH-Ug2gQmrA0IafoYFPpWEEhaYNIEf6KoOHVsvoLvvUmZ6u_tCxKed38_OeXBZWApEEOftgBgunG1kE07Gw_1qushVkwJG3K0t59QUd1_NEZLeueoy1UGh_qHgo77dIssMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj0MPQe33biaWSNWKmqp7olz7xddIZ8oT__z8IbT_k1HIB12XJdKZ6E_Fyb-ZuCyxHnGk1De7bo46YIVIVntB6tAF4oA-cqSu5JEImDABOBVe9ueUOnPVd_VBYQ6bOy4eWbhAY1XMJhjOUqFHEHAzGIdr6RmdMothSUDxqR4xaJvFf1bNxl3OGKhzYGpuZnfqathrYVa7z5fbxnfqMdbjskfpinFeULh8u7U0M9IZX-ZruTZGici0dvuwtX48qtrzHd_DbXTIto1M-0pFebrOV9N7uvsphkiOHrYcH2Jy3K3zaRSWCB0SL5CfL-Nwev9AteNxUBWiei8_59fmV4JZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEFfPJOKByMS8hv8n2MBZ8Havsn4lwZD4x8Ntmn_0MyMj2BzBnxwt2bi_nDG1yO6MdCBZk-xo7s5XSIiDQpVydnboVg9yRpBjiNS8jxJLemcJQgjhi2HjBD6VYrLIqLq1Y2oazoIjBWE6zdqXQd801B7dnu-NQwI8mW9SZT1VRyigJGOeiK52jMeA8JcoWfLymPXaFJKFFoEy1yIWkGdU8kJAYgw7D_dIxktLTo80JAakLEup3l_EYfjCoc0RDZdO_DhhNXvG11rfzN1xT_7gyp9cyf52DZ2iE4jEi0qOUFzX9ecLrB7vrNtfjF2qcDRm-OC7tLHCwiUAMzcVfxYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
