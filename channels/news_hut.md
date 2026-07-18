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
<img src="https://cdn4.telesco.pe/file/uajieOeGUUNjUJaVJZb2sxNf628ksEd69WIa4YSpNsCcfs9b9TwFxkYZpQNJUIpS8eVmwJTOCQvDj-t4RkrIOGDnNkm6GMw23uK1TyxprNS6_4FOs52RiQTSGYqcosWqzCElTfufXnhdzJcteiDG08HdFMr78duF1kP0plU9-2TQIY5gndXe4uGfRCoGpxNk-XwIMJBG0CfgEZPq0fBG37qaMsntzGyesvdFBrmH3TEJjAiHE0E-MEjvBCpP5vHJUYhqet4DyEiYLLZPf2WeXhJj_Fy_CzJ8lhbFX2ylRan7tDujSpJBbcjOB6-isltdOpMzD1YC62kVg6wNXIZl1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 166K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 05:13:26</div>
<hr>

<div class="tg-post" id="msg-68421">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/news_hut/68421" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68420">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdujzBKrPQ-ebTwAzXCI55txLFvdyQtktHJcXwTIV_YwLYgVk9070Y2MOo6duk4aC5RYRIy4DSf2JKsdRAfhgZHhWje7tGkfGlo-rK2-X6mCteJZA1CcbDPRcnNh0rL1QhiTBL4TuwokaVzyNmrgDl5Dqdnxvy-7CvHZgxVMciJp5G9MdXt-K2Ice7K3HE6TS7Dwenku-fm68of_EwCzdcxVS2GYRkHgv0QpriIKpCq0d2F8IGZx9Ta0qLChvS20YzWHBTueuNjpFIR5_CktCL_ZeQsTkO2XbvnVP5UPAAP8R1BWpvAeC9-WfOh2EbuHZ4JTp3NTvSlXkkIs8MRHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/news_hut/68420" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68419">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در جزیره لارک
@News_Hut</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/news_hut/68419" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68418">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKBbY5FZTcTIu2NAf1k6IfOSagNZrk_ZmJZ51LIMN-sU2xg2RR2sAanDMPWoAHJj3oovHqlvS1S-EzE-bU1AiRepAvsK3oprN9B3AJkeuYK9_TQ3p87gNatZOl4AuxaZYJx6JqhIoKIENGOvgCMx3RFE1qI_Dju0-LHUvRhFr4QsABn6r0GeaeExxYab18vPRUPXyALdzI04GQUyOmtfhyRa2S-pqIBgfV6IKAvH6rVdm-OFbaxDh-vMy5105CGT7VGsArM1FzPRQ-1TFZur4TDKC50RkjdLbAJvnfGjs8J--gUcJMxX_h3A06b4_WJTIvgvmBC-cL2Z1ClnV_KK-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۳ نفر در اثر حمله به پل بندرعباس_رودان کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/news_hut/68418" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68417">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:    ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.   اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.  @News_Hut</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/news_hut/68417" target="_blank">📅 02:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68416">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTi1Un8zG7pcYrgVVfVy0HWHvAfdN0ZQt0YODXDh3c4GikPRQZ3QgD7u9ZVCgXi5MXPxFMlQfj28VpEC8_cVhcZCePotzq4TJGQw_uHO-4w1C3FbRFYHjjfCt6tTk5YmU5kHdX_ryQW4CD6mtlFq379ZJtun4DyY9hangYfW1BcUGohCcf3vDLuWXDypvWlgnB6KOJb-boHAvCGSYVxK_48TtEBCbBo5PNDzQWUnSx-7ISnZHuM9toUkj6nRCBeLIUIW59Zn52feUgeqBNho-Gwesp2yQnGDuZBo731ZGgGidcelEsPRa4_Ip163vB9R1p_wwdIaCbJrFZlOOy4EUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:
ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.
اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/news_hut/68416" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68415">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.  حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن…</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/news_hut/68415" target="_blank">📅 02:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68414">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
فارس به نقل از منابع عربی:
حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/news_hut/68414" target="_blank">📅 02:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68413">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=SjtGn8mv2FGq_g6D7L-iVvvZDVui64RXLMHeE_OK9a1qmZIoIAOXWkdYJ1PCvxberaWOjeo1Fh3Q3l-HsdL8_-rZ3R_QsP4HzOmQj6Af9rhfVpoXX_PT77o_tJf6F0vDeiiIn1776arZ0SPPOJMPG6TkClpGZKZBymGTDdD5OojRLIRv-YlOf9_vHqc8_aE1t61nHN-q5ONc9N2YJia4WNhS0Ltfr_S32zAoHdXImMURDQLESQXPR9wu8Ozl6e13QNpgZCqL62ApR4OHFBp5JCXkHoK3NwhFj7JJyhVFKgM9eL0jAgPcenEI3crQLrdG-jshtDRY4uvrZn8O8rQNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=SjtGn8mv2FGq_g6D7L-iVvvZDVui64RXLMHeE_OK9a1qmZIoIAOXWkdYJ1PCvxberaWOjeo1Fh3Q3l-HsdL8_-rZ3R_QsP4HzOmQj6Af9rhfVpoXX_PT77o_tJf6F0vDeiiIn1776arZ0SPPOJMPG6TkClpGZKZBymGTDdD5OojRLIRv-YlOf9_vHqc8_aE1t61nHN-q5ONc9N2YJia4WNhS0Ltfr_S32zAoHdXImMURDQLESQXPR9wu8Ozl6e13QNpgZCqL62ApR4OHFBp5JCXkHoK3NwhFj7JJyhVFKgM9eL0jAgPcenEI3crQLrdG-jshtDRY4uvrZn8O8rQNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پل مسیر بندرعباس رودان
بعد از ایست بازرسی چغازردی حوالی روستای سرزه پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/news_hut/68413" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68412">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJajQlr3Sk9vaQeP3K7Tak0AZWIMk8N2Tthjm67wHOgBkvVtc-HR_3PCvrzDSniVDG5WT5niektMuxvZXw_Twxl8a1VxcTTKyk4aJJX6ClCHFcixlaFqfnzStr_L87Wp_vccEWGj97gIhJQCE7zY0ApctX3bfOcpcxDoIQf9qM7ZERnvl3kqaqMGxzkLWzLF9saIdc0Fm4UBIwhV8p8_4eLTi0y4SxV_DtA1QkobguNsWRuG398GQPQC4V0A0wQrP9nx7TCaJb1gs2mPfy-pkvogzIaM6licTJ_aYJG377P_WNBgOou668rbQicYqxoH2G1nOSqXSInEckJVXe4U6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیرهای هشدار در شهر الخرج، واقع در عربستان سعودی، به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/news_hut/68412" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68411">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XctzEDdrJg468ZfVp0qpA5_RHVvGR1xwf0NoCxtXxIoBomdmtmJQOWTeujULquoRTBxTP-3CYxZChHoNHPFfnpsl80cm24BjBckL8gFbGQi1pQBR0-CJe8zy5TVKzA996qmIk6POmdx88E_T-fwOtFt90GItiJNDEJagNM-LnuXiZXOn8sRPJGAX_NQcWTqyzsI106UNBUQG2SBEegTQS0lENBUUPIoy9vpOAUSsxgXiX96iSUdljCaGYE5Lw8Vys3YGAuXJD8YrwSWdnmrCHkNSQaYS94_I0tAERTnWwEDdeKWFEknQqFDyg6INi4Kx3zNiyUs0r7ShVdc8rMJDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پل سه‌راه‌ میناب به‌سمت رودان
@News_Hut</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/news_hut/68411" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68409">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3W7DmsGszEBUF5UKh5lY2YU4dmtU0YyZHPu9TVs7MLq2c_Npa44oCZEJlS-RYruPiZIsw3tdhfTjajmTKDAyT3JVtDqyCUNjLDjUtQlH83fMaOR5u4QIl6mFzsMsVVnDg1zksCTYKyoLDMmgduFaCamIykRhm9vB2FRk--mFeMcZP57sqCHtgR5wX7sljMk9Ll32Ze8gxn8vA1yTFKlfksb3zA6NrXGjDNNDSzbY6JOZ2UYlhSf3pJuos06wTlDx-NoORP2HPyS7vOE_KS46TrwWDit589I9gcYlqStSk6TcOV8imcqBVPUpKs3epFIk8cXjlWVPkxw-4G8aBzieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VphKW7QLjPAk0ooEMwgmunBLsdJHNidxoCWhBpLSW89FmwdfV27uSH3EhGOZsHlsNzUr2aWahC2_kZMrlZUMhu3PGrYyXip8-lAaNNWuOsink_fNMBxzbYdxi7ZorW2sqg9FxZsjFHRw0WQtLzZk2jpcXDHdMZrpqeR6BgmRaznkgVNkbD7Gt8hEfV5HDLxBReefKtKthMLfov7AaixB8gwl-LgM44ayarm8H2JAfvEtGF9WeSLMtsj3dagxdyZGi4fm6M0rnIe27ZVU_tVkrY0RI8fyl0m5lqz2wyCtJuUEU-Jxx7b9xGGINb4RA75IW0B89zmqcgQ8sTFdIn6_Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ارسالی از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/news_hut/68409" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68408">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=G7VDGotub5FW-lzo2C4q-S6mG5yZ9UD4PanedrtnzVsImumDxZOJriqQrNmuVpGsnEfDMwrXW4Zkypn9pBKbgOVloOC7_0zIu2koFPx_TAY-XRlTi2cxyS7EAsQ7-PIQ6bKGPkdOhij51fjb-1nW9WwU0Hj7aII16EIAvRkFScHBZsrvmj9iVCR3FaxBMKwj8sCLBhtXThiz4VOAWntVA5cH3LtBF2WMqqJeLMaY7yTdS5Eh8aPM9MpeOckpNDTK1m_rugo_JERLdHAFPU2kB9NhI1w1D8l0khXCqiXxTvnAaKP95cwPdlDN9uxJKoDcNNm3YjGCke3x0z5iFFSmPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=G7VDGotub5FW-lzo2C4q-S6mG5yZ9UD4PanedrtnzVsImumDxZOJriqQrNmuVpGsnEfDMwrXW4Zkypn9pBKbgOVloOC7_0zIu2koFPx_TAY-XRlTi2cxyS7EAsQ7-PIQ6bKGPkdOhij51fjb-1nW9WwU0Hj7aII16EIAvRkFScHBZsrvmj9iVCR3FaxBMKwj8sCLBhtXThiz4VOAWntVA5cH3LtBF2WMqqJeLMaY7yTdS5Eh8aPM9MpeOckpNDTK1m_rugo_JERLdHAFPU2kB9NhI1w1D8l0khXCqiXxTvnAaKP95cwPdlDN9uxJKoDcNNm3YjGCke3x0z5iFFSmPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/news_hut/68408" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68407">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
دو انفجار در خرم آباد شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/news_hut/68407" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68406">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از تبریز موشک شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/news_hut/68406" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68405">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=hp-EdZSKwKuZ7nwdTA-IqET7QqywB6tZbbIcUJHyUPWDwpUKwIKJ2L-XFrD28cHuh7-l9tOgzGAwjb9DCMRH8uCPZJVI4u9VfRk0no1WSSAGVnUmDVos2I_7BrkNzYGZXkyGdHuyRCxHyv253Nrz5cNNSLBgPQpFKRC18vxVHtzQtO3NNedpnVyC8j79kg8RbP3rDOIsyJcR9uuDCdqqR9iPH00Pn6T_JrAENzjYE3qA6JtnofufutHnlJjsHdpULbhBWqa4noD70UAbUvsoKqBGcgZrAFkEnpTh8qHLyse5cwHJhG3qYIOCpf72Zsp5AsEEoLANWb1Pc7SOWgyzCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=hp-EdZSKwKuZ7nwdTA-IqET7QqywB6tZbbIcUJHyUPWDwpUKwIKJ2L-XFrD28cHuh7-l9tOgzGAwjb9DCMRH8uCPZJVI4u9VfRk0no1WSSAGVnUmDVos2I_7BrkNzYGZXkyGdHuyRCxHyv253Nrz5cNNSLBgPQpFKRC18vxVHtzQtO3NNedpnVyC8j79kg8RbP3rDOIsyJcR9uuDCdqqR9iPH00Pn6T_JrAENzjYE3qA6JtnofufutHnlJjsHdpULbhBWqa4noD70UAbUvsoKqBGcgZrAFkEnpTh8qHLyse5cwHJhG3qYIOCpf72Zsp5AsEEoLANWb1Pc7SOWgyzCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند:
پل گلوگاه بعد گنو بندرعباس و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/news_hut/68405" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68404">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/68404" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68403">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
منابع داخلی:
چند محور مواصلاتی هرمزگان در پی حملات آمریکا مسدود شد
؛
⏺
بر اساس اعلام منابع رسمی، تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت به دلیل حملات دشمن تا اطلاع ثانوی مسدود شده است.
⏺
همچنین پل «شور» هدف حمله قرار گرفته است.
⏺
بر پایه این گزارش، پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرزه، نیز مورد حمله دشمن قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/68403" target="_blank">📅 02:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68402">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amP7Nk7OrCK0LnaWp50UGV2CCJPW0S7Rv7QYmI2r-8yTkRyHERVWqWEyA-T918JRKJiQz0XW1JV43QNCjVEUavzvBRALqa3kXg0S8PzEvkQSb6FnU1MU2oE0SyPpcEBKUNfvki9l8_VQ9T_Qn9_S8xPrM9bkzcPU1nTMwribf9QgPcE2uHimqeVK20uIeP9t2Kt5Mi_KUWTz04glr_bOSR0uxT3X1cGXM5ZEJLyMJEsMswNy3YZXlwfFojeCOtk6-F7zo-1SzB68Rejo_ZWzXAdYN5_sLiBnpAgYgCMC2Sh2-680EUAs5wrFC0dppG_vdR6kW2ZITHCTJpC9y5bNVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پل مسیر بندرعباس رودان هدف قرار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/68402" target="_blank">📅 01:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68401">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871564b347.mp4?token=Wx3gJGMW5Oa9Eu6J9_iDggnIhYIKfRnvhrCsMz12DqyyuiLIzwDZ63iB5Ek45ndJIjzEW7hlzi3H9cWZuseviC-u3Nc8uWQ2lVbZLZk4oAOwhP4U2md07TlKC58ajTK4fGSc9UENGhlIOAv3XNOo2NYP1zOP1iRvpgtM2HAJ3G8tqUkW--8TWZHno9Ng2pILa5kMg2VZR-SHI8uyyIpZDVyVHcUh91GBLPUoNdlP3xBOoDGYUWUCcdWSMjuwcMAMHFt7pG7fEicZk30GiM0YKoqr0T2dy5YfiCWSQOf7HS_vJ9mY-eVELOQZaGzIU5kaZR1zIk3e0rzgiT4bVEaWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871564b347.mp4?token=Wx3gJGMW5Oa9Eu6J9_iDggnIhYIKfRnvhrCsMz12DqyyuiLIzwDZ63iB5Ek45ndJIjzEW7hlzi3H9cWZuseviC-u3Nc8uWQ2lVbZLZk4oAOwhP4U2md07TlKC58ajTK4fGSc9UENGhlIOAv3XNOo2NYP1zOP1iRvpgtM2HAJ3G8tqUkW--8TWZHno9Ng2pILa5kMg2VZR-SHI8uyyIpZDVyVHcUh91GBLPUoNdlP3xBOoDGYUWUCcdWSMjuwcMAMHFt7pG7fEicZk30GiM0YKoqr0T2dy5YfiCWSQOf7HS_vJ9mY-eVELOQZaGzIU5kaZR1zIk3e0rzgiT4bVEaWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره پسرش بارون:
پسر بسیار قدبلندم، بارون. بارون عاشق فوتبال است و یک بازیکن خوب فوتبال است.
نمی‌دانم، سرعتش... من گفتم، وقتی یک بازیکن از اسپانیا، آرژانتین یا فرانسه از کنار شما رد می‌شود، بارون، چه اتفاقی می‌افتد؟""چه اتفاقی می‌افتد، بارون؟"
او گفت: "بابا، من یک توپ‌گیر خیلی خوب هستم!"
من گفتم: "اما بارون، اگر او سریع‌تر باشد، چه کار می‌کنی؟"
او گفت: "بابا، او هرگز از کنار من رد نمی‌شود!"
"من گفتم: "اما اگر این اتفاق بیفتد؟" و او نمی‌خواست به این سوال پاسخ دهد.
به نظر من، سرعت در این ورزش بسیار مهم است، شما موافقید؟"
😐
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/68401" target="_blank">📅 01:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68400">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
تسنیم:
حملات مجدد دشمن آمریکایی به اهواز، لار، یزد و چند شهر ایران
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/68400" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68399">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=kACtIKrvWbhSsw4xhig-YxB4OnYpmjxthFlI6E-wq6UrQbe7pjFva1M0ZuzxdwWjboB_3P88FFsiS2_Xch_k_q_VSluN8fKaEXRFPr2uyE_WLDqmJWptdC5JdXzIZ_-bMhfKI3tGkZlSNJAcQjQy9TPR_Hj8DU2Pq0p7vXbbgSZ8t1AJpWgSpcBMm4JS5_9zr-cJQFzC3CLRzQcS92jzzcCzxo0UA3mXm_pJ1Ck0IwS_n9Lt0pYVoWO49pdO94jTUxyksVhQei3OAKWTc6BeT3PaQOZZGkiQYPaVpSdoghAp9F9le-FKouEcwB-hnrUFFhR-1_7gBuZeq1CJGfDnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=kACtIKrvWbhSsw4xhig-YxB4OnYpmjxthFlI6E-wq6UrQbe7pjFva1M0ZuzxdwWjboB_3P88FFsiS2_Xch_k_q_VSluN8fKaEXRFPr2uyE_WLDqmJWptdC5JdXzIZ_-bMhfKI3tGkZlSNJAcQjQy9TPR_Hj8DU2Pq0p7vXbbgSZ8t1AJpWgSpcBMm4JS5_9zr-cJQFzC3CLRzQcS92jzzcCzxo0UA3mXm_pJ1Ck0IwS_n9Lt0pYVoWO49pdO94jTUxyksVhQei3OAKWTc6BeT3PaQOZZGkiQYPaVpSdoghAp9F9le-FKouEcwB-hnrUFFhR-1_7gBuZeq1CJGfDnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دموکرات ها در انتخابات تقلب کردند، و من چه چیزی نصیبم شد؟ جام جهانی نصیبم شد. المپیک نصیبم شد و آن‌ها را به اینجا آوردم.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/68399" target="_blank">📅 01:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68398">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در لار
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/68398" target="_blank">📅 01:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68397">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
دو فروند کشتی نفت‌کش با عبور از مسیر مین‌گذاری‌شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/68397" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68396">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=hHhKl9OxZTBJISu1bH7w5Ra_a3LPzbBEn-yGrPz2ErHpYSr74d1cG5M31Zm6K9oIgwyhwpqK62ZrOtEtV8OAhK2B9vAYnRbsgMojgabIya6NcW48voZ6MQj5-MT0_CwtrQqv1bum2-LZN3JPlKRlEfOm2GXs2k7xsDggPCCu_VgfhbRhHsTJh4Q_vEyIWPd1DI0pcZO6529C_ZQUiyRmliPRCNqeG7_Zpysvy9MQ0ZUwhEC3qaZnxr8gqsf-3lpbVf8MIBS3-4luDN5758zWhCodZTfd5bRoij6mm0gTGbOS7XBCSEr-cJ3cnDXhVX6EE2UEoXU83BQMXgeKxRoNLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=hHhKl9OxZTBJISu1bH7w5Ra_a3LPzbBEn-yGrPz2ErHpYSr74d1cG5M31Zm6K9oIgwyhwpqK62ZrOtEtV8OAhK2B9vAYnRbsgMojgabIya6NcW48voZ6MQj5-MT0_CwtrQqv1bum2-LZN3JPlKRlEfOm2GXs2k7xsDggPCCu_VgfhbRhHsTJh4Q_vEyIWPd1DI0pcZO6529C_ZQUiyRmliPRCNqeG7_Zpysvy9MQ0ZUwhEC3qaZnxr8gqsf-3lpbVf8MIBS3-4luDN5758zWhCodZTfd5bRoij6mm0gTGbOS7XBCSEr-cJ3cnDXhVX6EE2UEoXU83BQMXgeKxRoNLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به یزد صدای جنگنده
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/68396" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68395">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خفه شو کصکش
#hjAly‌</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/68395" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68394">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
ترامپ: هری‌کین هم خوبه ولی ممکنه تو پست اشتباهی بازی کنه
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68394" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68393">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
ترامپ: مسی خیلی خفنه
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68393" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68392">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
ترامپ: رونالدو مرد بزرگیه
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68392" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68391">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/68391" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/68390" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/68389" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=uQ1ces81WBIcPZgUaj6SlbOpMug9G1gnnaOwfoFwtmc3Hp5NJfRhlzXsezKr7uDslJvXfwbH_ihSSp35GUuSvBz_9wmE8LkNhGe8vwuFnWKwrMfYObLhdKIja7QUC62_6bZJME6lh0B2YhL2uPlFkO-I1LlC4WkYWwnT_dkmaNIBvjblbCw1Rbap_FRba98cu8WkOxaEF55ubVQ5YrV-d5UAfmKKvEEY3YePfoM-dxi8h2yIQhcocQoS8MpY9S7xT0h7Vx6drxh3uRLQ5hcF6CQEmA-lFqq2KDOIH_PTU4Lqdk7X1nKjWKeKpZ5t1smmgRzd_jWeAsoe57KsJPTH1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=uQ1ces81WBIcPZgUaj6SlbOpMug9G1gnnaOwfoFwtmc3Hp5NJfRhlzXsezKr7uDslJvXfwbH_ihSSp35GUuSvBz_9wmE8LkNhGe8vwuFnWKwrMfYObLhdKIja7QUC62_6bZJME6lh0B2YhL2uPlFkO-I1LlC4WkYWwnT_dkmaNIBvjblbCw1Rbap_FRba98cu8WkOxaEF55ubVQ5YrV-d5UAfmKKvEEY3YePfoM-dxi8h2yIQhcocQoS8MpY9S7xT0h7Vx6drxh3uRLQ5hcF6CQEmA-lFqq2KDOIH_PTU4Lqdk7X1nKjWKeKpZ5t1smmgRzd_jWeAsoe57KsJPTH1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما ۵ دقیقه بعد از حمله به شهر های مختلف ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/68388" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
دقایقی قبل آمریکا به نقاطی در داراب حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/68387" target="_blank">📅 01:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
فارس:
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/68386" target="_blank">📅 01:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=AC2sCGgU5xfdKMlzcc0IOyD4eGJl_qhV1abB0Fk5BvvAKjnIQ1P-PBH7GEko_wlBIDYzyxtpqD1eJh9ZtneMi5uU_DWrpYDc0sqva3hTgVomFqAMep-tcYJnJcszPSJXQm7vtKS0opSeVFfQBl-Ka-oTRJxRNcjGxWypf7hDMPWqL0Y_zbUUigpdRz5XzUM2PSpA5FopQkfkjt-wyV1td2dbAfv5Zee_SaZAvhdW5FmzSxNaixUcPPw8Sz-QOhEA_4ncCQfAD60NfiZPiL5F_Co818qnJTOcRfIRyCCU9MMuhmsUGpA6G1xUxdVzHUampt8TKAx4mrWmP1jjrFJSKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=AC2sCGgU5xfdKMlzcc0IOyD4eGJl_qhV1abB0Fk5BvvAKjnIQ1P-PBH7GEko_wlBIDYzyxtpqD1eJh9ZtneMi5uU_DWrpYDc0sqva3hTgVomFqAMep-tcYJnJcszPSJXQm7vtKS0opSeVFfQBl-Ka-oTRJxRNcjGxWypf7hDMPWqL0Y_zbUUigpdRz5XzUM2PSpA5FopQkfkjt-wyV1td2dbAfv5Zee_SaZAvhdW5FmzSxNaixUcPPw8Sz-QOhEA_4ncCQfAD60NfiZPiL5F_Co818qnJTOcRfIRyCCU9MMuhmsUGpA6G1xUxdVzHUampt8TKAx4mrWmP1jjrFJSKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به لار
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/68385" target="_blank">📅 00:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68384">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
معاون استانداری خوزستان:
دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68384" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68383">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=WYTIv1PmINwJJKYuVGs_MMaPJI95NxSu9Gy-4GIxioEvUYqy5-GY7xZH6hPAxtY58D4WuITVvgB4TcesaenN8zVUAvXGMzFQWLEQprxNFwHCuJ6n7NU9uQcD8VTsaXBjf6TuXgtayucQihdw62d7woxjdyHEE28I55j7X_5JW707mn2FuSG6j0lBm3fmAtE6FdubxCliluhkRQIjs_NSQ9yiKFq7qFAZ1FvgJXMUyqV9PJlWJMWe0Q5JDDeWjxk1J4wqMAzxiUegJSmdFS3ktJx8R9rSBGSTtUBKDEPhBc5Lv44uhlIVqRZZbNxWqcojnHGQdW3A2YZinp41D08uIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=WYTIv1PmINwJJKYuVGs_MMaPJI95NxSu9Gy-4GIxioEvUYqy5-GY7xZH6hPAxtY58D4WuITVvgB4TcesaenN8zVUAvXGMzFQWLEQprxNFwHCuJ6n7NU9uQcD8VTsaXBjf6TuXgtayucQihdw62d7woxjdyHEE28I55j7X_5JW707mn2FuSG6j0lBm3fmAtE6FdubxCliluhkRQIjs_NSQ9yiKFq7qFAZ1FvgJXMUyqV9PJlWJMWe0Q5JDDeWjxk1J4wqMAzxiUegJSmdFS3ktJx8R9rSBGSTtUBKDEPhBc5Lv44uhlIVqRZZbNxWqcojnHGQdW3A2YZinp41D08uIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا به سایت موشکی یزد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68383" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ممکنه امشب، سخت‌ترین شب برای جنوب باشه
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68382" target="_blank">📅 00:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68381">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از چندین انفجار در یزد
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68381" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68380">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428210a926.mp4?token=TsfEb0QTm9XXAG7Cf_dmf3YYxx6260bMeYsXvKhe89Eo0PykgUC-248Wc9lAhrG9sfGXubCiZAHq6L1_xd5YBD9HKGs9nEciIA3c-3nkw-tdsTRsBq4BdAGPDE_Us1HrJznHGvKLvfVTfJa3XHLrszz4qqMQNXiqtOYZuqU3TT3j5MQKzzEtsrNPNye3U5Z4k_AxUNNd18vXAy-PQrEqRGUk1WYY0K6kx1LWp_K3pwKSKQuHBQRT0UGQANOin9bA312XjyXTrsZ2AVoFe3e4A_RGgKyDHvX43E8JnxTscIDYRfhzGZ-T4Ah4tkxLdZDqwmGDpSa5LWFQ4-vExSQStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428210a926.mp4?token=TsfEb0QTm9XXAG7Cf_dmf3YYxx6260bMeYsXvKhe89Eo0PykgUC-248Wc9lAhrG9sfGXubCiZAHq6L1_xd5YBD9HKGs9nEciIA3c-3nkw-tdsTRsBq4BdAGPDE_Us1HrJznHGvKLvfVTfJa3XHLrszz4qqMQNXiqtOYZuqU3TT3j5MQKzzEtsrNPNye3U5Z4k_AxUNNd18vXAy-PQrEqRGUk1WYY0K6kx1LWp_K3pwKSKQuHBQRT0UGQANOin9bA312XjyXTrsZ2AVoFe3e4A_RGgKyDHvX43E8JnxTscIDYRfhzGZ-T4Ah4tkxLdZDqwmGDpSa5LWFQ4-vExSQStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حمله آمریکا به لارستان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68380" target="_blank">📅 00:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68379">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
گزارش ها از انفجار در لارستان استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68379" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68378">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
انفجارر
بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68378" target="_blank">📅 23:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68377">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
سیریک و اهواز انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68377" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
قشم رو وحشتناک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68376" target="_blank">📅 23:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68375" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68374" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68373" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68372">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioZL8fXf9MwS-K3NRHY7QwXqjFOxyJuEXPWSTbqVtH_h-mOSq30yxS25WYWq3MFiLe0CID52RlTTd8xVeoBcZHejWwkkD7nUkWSA0tOY8rtnMEe3nUDPFNa61DNoO5vTi9LK_8vWt6ZIkBjfGosw-whTFd21xNjCbaaBZZMNms0ucZx9EACCoJQBh2vAlAt9RmyRRzpJb5sJkfJ8EWshTQedXHJZMt4I332CqPRCnnc5abRYNtFN6XCCdq9v_kmDxXOjqnzK7E0s_ZGs8Kz9EHOGfsCsfokIvN4-_oqzinsRoUlgv9seY4KtzlFGLq9FxA51xhE_JDHDJLBo7z830Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
سنتکام امروز ساعت ۳ بعدازظهر (به وقت شرقی) و برای هفتمین شب پیاپی، دور جدیدی از حملات را علیه ایران آغاز کرد. این حملات با هدف تداوم تضعیف توانمندی‌های نظامی ایران و بنا بر دستور فرمانده کل انجام می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68372" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68371">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
با اعلام سنتکام دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68371" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68370">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68370" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68368">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HftnfSSMsJg0my09wnU_gWoj7YBKJi9n6gqk6UAlK1HsYH6a8WqcYugE7Vdbah6Br_byWkbzWttbFST7NoFV2Xv3GtFWE1kicBoxVCGDP4_Wyw5F6c60oBcTXquTq6n_O84Ej9Ldo4IWzfgMyy9E06MdISQlYST4TadhWEEfPTnn8QRg3iDldk5TCSSjmK_vmiEsCB-EnZtBj-2sDblVQ3dPtEowZrI2LQ3dMbxxsT2wasakQLwGaRkiPxTQd90hPbeMEFEb7mSZxNOivIHTUY_fgYXbCNoM1ZuRqmty35b8LkjJ8Aond3hK7aJMNXGA3nUHlPN2IDfYUqJWDA7W6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV5SpthHiUKkyl_1yXcKj9u2x1xmXQJuKRsQvZ7AC7R6hItuwYGuDqKEftMMn5jCUwfEQcPC8279o0VjWdN1Ls9anijyVLLYDujdAGWrFhE6Ue3fjU4IWhThZHgel3UW4Gd8GwZvUea3L7Iz1yR0ZBWlvsX0vR0nQ7sJ6--vx1gTCOCwu-OZ4dZFJmLlFdTwYchnauU482KI6-VtRiAusZ29qIry4J7BSltezzV-5sl6uDxjGhcWRi58Hg2EY3l6GuYBticEmkeJKtReDk8oswdn3PC8K06LlYtCKTjzj4dAYwJ-SqKAYoqpIonUjJzDpvV21ZjmSqSReyXfqF2u1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:
علی دایی رانتیه و آرزوی بمباران ایران رو داره
!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68368" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68367">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=qpgE5T8sTwDIAyKVesNghPGL2YZ3SrZBBDX8cqf3E6e4SwLwTe4ueBtTCo0kp81VWPPOzjjLS2XZV68Qf6wdbWy9fl7X11ATsFxH7a53vf-41Gb6hxqo1KpO54yXZQfLNqJ1YLmR0brxOwvFQYqv49eFiw4Ky2siLzlC25EtyKhYzUI1UNWOC9ugg1akqPL1cxsYIkWm2Oyc99qVhPUJr-miTSJ3eC7eSSkcK4yemoSS0qfFHbb5itMitlHjtmiJmJjSDW7byKg23x9R-oPXmhKiSibw9ZakCYGRNDFH-ExteNZJnb5-eQvv6s-XZYylduL0SDLjggpSF_4vNc1fww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=qpgE5T8sTwDIAyKVesNghPGL2YZ3SrZBBDX8cqf3E6e4SwLwTe4ueBtTCo0kp81VWPPOzjjLS2XZV68Qf6wdbWy9fl7X11ATsFxH7a53vf-41Gb6hxqo1KpO54yXZQfLNqJ1YLmR0brxOwvFQYqv49eFiw4Ky2siLzlC25EtyKhYzUI1UNWOC9ugg1akqPL1cxsYIkWm2Oyc99qVhPUJr-miTSJ3eC7eSSkcK4yemoSS0qfFHbb5itMitlHjtmiJmJjSDW7byKg23x9R-oPXmhKiSibw9ZakCYGRNDFH-ExteNZJnb5-eQvv6s-XZYylduL0SDLjggpSF_4vNc1fww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آرش اعلایی به جی دی ونس گفت مادرجنده
😂
:
جی دی ونس یک مادری داشته که هروئینی بوده و مدت بسیار زیادی به مواد مخدر اعتیاد داشته
مادرش پشت سرهم مجبور بوده از یک خونه به خونه دیگه بره
جی دی ونس یک کتاب داره که توش نوشته چندتا دوست پسر مامانش داشته و چطوری دوست پسراشو میاورده خونه و چقدر کمبود داشته
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68367" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68366">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=cSt_n_QetnViYX7nuS4jVvFL_3D4Zb6c74MW_qMXrWmFk0TsV1s_g340Ipc-ILRC6NchAOgZj_TNt767heMNxEOpjHYQTG3EREhwIoJ8ZbvHdYuiBwqRFZJhWBHJblpglq1KWzpM1nH4qS3FO5vOhaXv2R_OzN1cU5X4BK6-zYILxrTVrj9JBRS7M68zl_tzXM-eik3IiyJdCa_CBX3UkGm_8yAZ3OUZUgWc89ckPyktOTb9Ozxn0g63YkZHenVCRcLbigZ2b08cavyQ3t7H95jQY2SKbOQshvUs4B-nXVyVc4yc1U1cMobt1bRnxUj2Wr3IXL6yAoXgtPBnylMQiweLR95dAydlzng2UDJPAAnna8Omvh6bN9-LUQRpkXCf97oHkFckyycSo1-Lp59_hGHaG0sqJ1-nOvf8ZBeQdvU5Slff6Ia2yh7Z5E3dc3KAF3nQ7Edzh4sBvRrwReykl9Ek1HrrVka5GPdpS4WBpeIKNSP9gbPEvzXkcR1QwFEuS87fURhkUBBDtHXv8dl3P3U03tOuquzNRocAcy_d_upkdyfw94V_r80Kzn37lw4wc8xTbH-a3eDzDxeryC7048m4mWnwFeJHPSqOUZAZ8KLUkkHp6cZeR1kWOQ0AAI8-QsMo2heGJihA1rxLlN3_UK3ZDWDO2id35RtE5fy54rY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=cSt_n_QetnViYX7nuS4jVvFL_3D4Zb6c74MW_qMXrWmFk0TsV1s_g340Ipc-ILRC6NchAOgZj_TNt767heMNxEOpjHYQTG3EREhwIoJ8ZbvHdYuiBwqRFZJhWBHJblpglq1KWzpM1nH4qS3FO5vOhaXv2R_OzN1cU5X4BK6-zYILxrTVrj9JBRS7M68zl_tzXM-eik3IiyJdCa_CBX3UkGm_8yAZ3OUZUgWc89ckPyktOTb9Ozxn0g63YkZHenVCRcLbigZ2b08cavyQ3t7H95jQY2SKbOQshvUs4B-nXVyVc4yc1U1cMobt1bRnxUj2Wr3IXL6yAoXgtPBnylMQiweLR95dAydlzng2UDJPAAnna8Omvh6bN9-LUQRpkXCf97oHkFckyycSo1-Lp59_hGHaG0sqJ1-nOvf8ZBeQdvU5Slff6Ia2yh7Z5E3dc3KAF3nQ7Edzh4sBvRrwReykl9Ek1HrrVka5GPdpS4WBpeIKNSP9gbPEvzXkcR1QwFEuS87fURhkUBBDtHXv8dl3P3U03tOuquzNRocAcy_d_upkdyfw94V_r80Kzn37lw4wc8xTbH-a3eDzDxeryC7048m4mWnwFeJHPSqOUZAZ8KLUkkHp6cZeR1kWOQ0AAI8-QsMo2heGJihA1rxLlN3_UK3ZDWDO2id35RtE5fy54rY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای که گفته میشه مربوط به کشتی تایلندی هست که مورداصابت قرار گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68366" target="_blank">📅 22:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68365">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68365" target="_blank">📅 21:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68364">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68364" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68361">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=aGIDZE1Dex3SpudYwMafYqR8fgeEHG6cLj2HsMZ04_VbaCbcB8S5kjng-wPRrzsC6bnC5zkju99CuTvIYGuVr7VFpElj7RnDK8V_K97xWkqoA7Wy9Z_WtTfQQ9Ax4CnigT_elayP7YiJp_Fv5OINx_ZWFidEhzTHLFNQmehsWTmYzRSN6H3CMqo0CuaMpueKVHU39eXAMDf-vT-ONup9MVLlrMD0ZXwiXazehdiOgV4vCY-kB1pWJNt5okY6voZOV3tNCVER_xkigtm-JanNmzB4Id-ZTARRRokILUM-8U3jt4IIsQzkw7tW8ZU0C5trFS6DTyhHPIspqZKkSqu6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=aGIDZE1Dex3SpudYwMafYqR8fgeEHG6cLj2HsMZ04_VbaCbcB8S5kjng-wPRrzsC6bnC5zkju99CuTvIYGuVr7VFpElj7RnDK8V_K97xWkqoA7Wy9Z_WtTfQQ9Ax4CnigT_elayP7YiJp_Fv5OINx_ZWFidEhzTHLFNQmehsWTmYzRSN6H3CMqo0CuaMpueKVHU39eXAMDf-vT-ONup9MVLlrMD0ZXwiXazehdiOgV4vCY-kB1pWJNt5okY6voZOV3tNCVER_xkigtm-JanNmzB4Id-ZTARRRokILUM-8U3jt4IIsQzkw7tW8ZU0C5trFS6DTyhHPIspqZKkSqu6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت اقلیم کردستان پس از حملات جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68361" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68360">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68360" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raOYel0Gj_FV8S2WmMTDETKE5krbF0VO8ThVsoJ5rPcGHFjdkjdJEchu74ogZE3iy5BPHn1XLcO51zg9z2fK6vshMXttULa1Oj6iLJFpg3cpOBjoVQbwH2bDfxvtECMp_x-rA7IEtF-XlR7ieQYTbj1p7Xuk5arodyhssKeoK6TXyHqb0jgjf-QvIwUVIzVaNCfbFb3VPuw4mIk3wob7LyCDOnBsSR43DLKv_slTJhMnyWdVQU9mmxWPwR9AplECPBlgv6XSdQLRH88VCNBjfSwXXAMWostj-ngNl_Dw4XJTMy3AXonTaPW8Rq-VKb5W9fcbev4mnfhsQt_O1-zuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68359" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68358">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kowQ9Ujb1aFv7NE-VJ4O1UtrUiwvYn-Tp_gOYcCC9intS2vg_vcyPoS53kZnVHrgNNKK4cJIkg7148f1OWr4pfFVo4m6GPkI1FfYlj45ZfpG0unn8oBJg_y-bE8mBuRlujbTra7JSETafA5HxTWNRPsrnf6U7LwUcJf4JkNk7icVKrJEa5D1u4N5rGp73lSDZgJSV_gYf2AqNvx4R_xG65mdF_1XDLQK_nOsgAHyJMy4Q_dCYZgEn-xbKTQm6O90ORTEKij8RWDtsYMZ3FI_t9NY1TS601mHlmiTuf66eudIffJuu85qpOz78PyOu7ONcdbF9TaZfILpCATsKzoynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تعداد بیشتری از جنگنده‌های آمریکایی مدل F-16 که از اروپا به این منطقه اعزام شده‌اند، با پشتیبانی هواپیماهای تانکردار KC-135، در حال استقرار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68358" target="_blank">📅 21:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68357">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=GTL043_UKVTaB-u-pBOivCjJbs4PhUYnW4tbGegs3xppDQsH-B3FlyTZvdOUtKdkvA9nUc77Nhsq2-fesKPSQAprp8TCrJzb1BksOUCiwnCJBun6pKkOGnSKM7ZaWR71USShYNsLv9tLKiqi-rmzJTBGxbvPq3-JOK3BIbfzu9TBOPG4W_u2VUGtZbkYUe8ZwW7R6GX63Fz4Nl5m4zZ8fniSMZ5oywmt2H6zOvhN9L7fPOxVIBnjIDd6plqBJ1hWTUy3KqiwkTh-GHfKF_5OnBQ3BVHKLNRTNPCK7Y8o4r9AjgfFooBc85vKkjdn3hbySSMu901YYr9hBPexDnB3BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=GTL043_UKVTaB-u-pBOivCjJbs4PhUYnW4tbGegs3xppDQsH-B3FlyTZvdOUtKdkvA9nUc77Nhsq2-fesKPSQAprp8TCrJzb1BksOUCiwnCJBun6pKkOGnSKM7ZaWR71USShYNsLv9tLKiqi-rmzJTBGxbvPq3-JOK3BIbfzu9TBOPG4W_u2VUGtZbkYUe8ZwW7R6GX63Fz4Nl5m4zZ8fniSMZ5oywmt2H6zOvhN9L7fPOxVIBnjIDd6plqBJ1hWTUy3KqiwkTh-GHfKF_5OnBQ3BVHKLNRTNPCK7Y8o4r9AjgfFooBc85vKkjdn3hbySSMu901YYr9hBPexDnB3BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترافیک تنگه هرمز در ۱۶ جولای به کمترین میزان در طول سه هفته گذشته رسید و تنها هشت کشتی از این مسیر عبور کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68357" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68356">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
تعداد قابل توجهی سوخترسان در حال اعزام به خاورمیانه است</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68356" target="_blank">📅 20:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68355">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=jFjQISafE_pX9Kso-Sd04CUMuuTYwu-P_rGxQOv_KqN4Z90wzzYHom5NBkykIdXySqxfnPVK_AbZx8On9IMRjOzeeb4ADn1zMXAh9J3zGpYbmfXtCThgUqn6B4F8e2NiNCMwmTYWQWvsL5Zg2x1Bg6__5Ow70FgJjN6EEK2aVH3BkAy_150prGhEvjSqsHXoL5h1ssGJ3bUUDi0d-HPCWmSJVTGva7TA0lVZVIEg1m_1h2sA9UN1adBCYeaqXDegzc0v2nsJOzXO0waIxfvQeZU5nKkh_luCgTPCwZUTzthoR0f_LO1YVlMR04QQtYw_OO0uAppTms1piOwdtGjeEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=jFjQISafE_pX9Kso-Sd04CUMuuTYwu-P_rGxQOv_KqN4Z90wzzYHom5NBkykIdXySqxfnPVK_AbZx8On9IMRjOzeeb4ADn1zMXAh9J3zGpYbmfXtCThgUqn6B4F8e2NiNCMwmTYWQWvsL5Zg2x1Bg6__5Ow70FgJjN6EEK2aVH3BkAy_150prGhEvjSqsHXoL5h1ssGJ3bUUDi0d-HPCWmSJVTGva7TA0lVZVIEg1m_1h2sA9UN1adBCYeaqXDegzc0v2nsJOzXO0waIxfvQeZU5nKkh_luCgTPCwZUTzthoR0f_LO1YVlMR04QQtYw_OO0uAppTms1piOwdtGjeEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماهیگیران ایرانی یک پهپاد انتحاری آمریکایی مدل "لوکاس" را که سقوط کرده بود، از تنگه هرمز خارج کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68355" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68354">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXXQjf6WRE1ISMxo9dagc4Krqqt_EAQ0eVtvezu1o13439Euwy7ZQcvmsUIvRcvyraR2l3bKsDluOVBul8x7rB2nV9dU5EkcqAmXQuqavlJ57qy8n6JZilycA9uNefLIpNQyLOyod1QzTgcNLA0p5hphupyG5dXDWYu9uisRQIo45s2Ad_a0T5Sshu-0ZIAQBAQO-DBD4xgOyUL6LFKcj0XUAgseDpNjSpcBnh7ILyxJSv2KVlGn8QkHzQL9CUol9n3MQFc7eYJAlTPCEe3U-Yc5LwyYzUtmnxtQ9lLq6FpCvbDiRHxdHiAV_Vx2PCTmNdYixg1nXP6geKPK5v_nrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.
حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن به این مناقشه قرار داده است؛
امری که می‌تواند نقش احتمالی آینده اسلام‌آباد به عنوان میانجی میان ایالات متحده و ایران را پیچیده سازد.
پاکستان که دارای تسلیحات هسته‌ای است و ماه گذشته در دستیابی به توافقی موقت در مناقشه میان واشنگتن و تهران نقش میانجی را ایفا کرد، سال گذشته یک توافق‌نامه دفاعی متقابل با عربستان سعودی امضا نمود و هزاران سرباز پاکستانی به همراه یک اسکادران از هواپیماهای جنگنده به این پادشاهی اعزام شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68354" target="_blank">📅 19:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68353">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_Tjs3yAObjwngS8Hv9lNgInYkyQ02hJegwsUiOdEc_5z20vF2frkrE2LQFcG5N52C_zBkT8rvq9hXo_4_XaTK9MkY0QHWz2cridtWL8dTKnmdeiO--4Id3IrnxjjuBGltKFwzbn5W8Ug_YtwPYZ7xfKoLVFz4sfssinmqEi3J3H3YAjV7B91f3dyDe-nhZWAZlUwJhKabqbNJ-k82BwS9aFggHOuFJlYrhol6CUABjU3FLhbrrY4JlrBb5xv3dicAnFAG8XUppUCUuqej23igycAJzswwGRhdYVru5XevEV727wBvnELQDVk_0yKW6olVfvcWqSAmFl38o9NZ7UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای ایرانی مدعی‌اند که به پایگاه «التنف» در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را اسیر یا کشته‌اند. این ادعا نادرست است.
✔️
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در این منطقه کشته یا اسیر نشده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68353" target="_blank">📅 18:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68352">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=HSMeJOLsNgbUEBVHsApLBZJZaZokoviHTNJs7ThQApwHoT-nCnnJiO60FgrTr59QYlaBuKELyzifNgNgM3plPa23PWrrM3aTZuQ1B3MhHNXka_YRUqMPUBX5eQxAjGVj1NJVgKTLI2DNVBYh0fjITrVNOUtcfvXEO2MjMTsYf_B2pfPdElTi-_gUicfyqTOMJvEsKlN16BaeOqs-iYbZZIzChmOdmeAcBzVr-VT_3WUMowt5-S9M8iqP_HvGejNNX-5d2pG2PG2o1XtpQ45Awri9t5m1-CCxbsDAQrD2Rf4X9BzT1v0F2J1q7lVQbw5zT0Oiww8UaldEsDcYTbsRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=HSMeJOLsNgbUEBVHsApLBZJZaZokoviHTNJs7ThQApwHoT-nCnnJiO60FgrTr59QYlaBuKELyzifNgNgM3plPa23PWrrM3aTZuQ1B3MhHNXka_YRUqMPUBX5eQxAjGVj1NJVgKTLI2DNVBYh0fjITrVNOUtcfvXEO2MjMTsYf_B2pfPdElTi-_gUicfyqTOMJvEsKlN16BaeOqs-iYbZZIzChmOdmeAcBzVr-VT_3WUMowt5-S9M8iqP_HvGejNNX-5d2pG2PG2o1XtpQ45Awri9t5m1-CCxbsDAQrD2Rf4X9BzT1v0F2J1q7lVQbw5zT0Oiww8UaldEsDcYTbsRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در ۱۶ ژوئیه، نیروهای ایالات متحده با موفقیت برج نظارتی بندر شهید کلانتری چابهار را منهدم کردند؛
سازه‌ای که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود و دهه‌ها توسط سپاه پاسداران انقلاب اسلامی برای ردیابی و هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز مورد استفاده قرار می‌گرفت.
انهدام این برج، مستقیماً توانایی سپاه پاسداران را برای هماهنگی حملات علیه خدمه غیرنظامی و بی‌گناه کاهش می‌دهد.
علاوه بر این، این اقدام از آزادی کشتیرانی در آب‌های منطقه برای تمامی شناورها محافظت می‌کند، مگر کشتی‌هایی که قصد نقض محاصره دریایی جاری ایالات متحده علیه ایران را داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68352" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68351">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=NqgATHzKZD3JhSVgdBvg7U91j5bpSOH03mqIs12uhf-EHBgfTCqGNpI7u-MOQotSxkocTh4LKUPA_FcaxHx6CJeXznuFntTKeKKNvWPiH7ElyuuDwmbox43x8v6L8DbIsEljO60z0ghx0O-Qy-SzEbWnCa-E6Uiv1UDeHuOQjBwsbdBW_8bv76tL7L5yhArfilfybgAzHqSL9e13d9K7r04B3cnK3lmGdNPcluMJesSOCD-7j5GjSLAUUAxLdR4nLq7sAy7fHC7jLZBg7UVanROLvR7BpBws8B_X51ZRdUNVk0kzRNJ_nCxwcREmiUAcZ_mbg5sld0cyRdNzx9u21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=NqgATHzKZD3JhSVgdBvg7U91j5bpSOH03mqIs12uhf-EHBgfTCqGNpI7u-MOQotSxkocTh4LKUPA_FcaxHx6CJeXznuFntTKeKKNvWPiH7ElyuuDwmbox43x8v6L8DbIsEljO60z0ghx0O-Qy-SzEbWnCa-E6Uiv1UDeHuOQjBwsbdBW_8bv76tL7L5yhArfilfybgAzHqSL9e13d9K7r04B3cnK3lmGdNPcluMJesSOCD-7j5GjSLAUUAxLdR4nLq7sAy7fHC7jLZBg7UVanROLvR7BpBws8B_X51ZRdUNVk0kzRNJ_nCxwcREmiUAcZ_mbg5sld0cyRdNzx9u21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی باقری کنی، معاون امنیت ملی دبیر شورای عالی امنیت ملی:
برای آنکه رهبران آمریکا و رژیم صهیونیستی از وجود اراده جدی برای مجازات خود آگاه شوند، سریال «مختارنامه» را تماشا کنند
😶
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68351" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68350">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم‌اکنون وضعیت پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68350" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68348">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHu-kqxgikpXkUo71iT_LhLcGkN0J7cDY6quTV1VBHam8KJk0SHLdHZ8F6h0ugKDqa_s73-QM3DEpwe8a1XbGeILNYA3SA0uagbT13Ce8UVZNozCuvaRG-2DQHMicflGTHGqb59g3xVVFRQidTLj2SalfC1hQLWTJ5NASEu3NURX2cWnhV6b39F_DG_YHGk4XZeuLVE31UTqJV4nyNOyxCq2qLKsmRjQBx2RjzmXfW7pGt70PA-mhNrdGxeq0szGIZ6wFWKXzrcejesdLiykBvpgCwIVQw8oXPN8hWY9If56LWvG3w2n8xQDHIzOG5aII_u_2PMl99cr32TR38LZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6De5kUpyXRL1NqiYJJ1cdw1R3GsR52uj2aLSEHocYqOMVxqM2NGSwxN8LVuH-yvnTuexfrz5BC8BJQR0qIqG5D8Z0OKzWKqpsdbTEOiPyTpt0egsAzQZkBxpJdIOx8VnzpQqoBCQcQ7p9z8odHyTFg8jWmyPQjhcTcyeBP1z7Dv59Jxo2ocmazhWwS_AOREShrHhDX55NmSoyK4RVlQz50NM4P8ogI4r9Mfuiw9bVPkPlxzsaolbLgf1J5nHusd9qrz3LUkJqTsroji_4FlehxmRvPlfxVoV0tLxrKIXX11BC8kPic6RhOQzZHb03Lz0rxBahT12NP3huiAGuM7Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدون شرح.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68348" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68347">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeOhbH0igCJnnENwNcnp-RWLBwwNVLlGQL2l_8V5S7OC-G8X-wwYlks7T0GvscnQaTpueJZvGXX3iFJJnyGRSPO1dbh54LRoS1ttLDRi1V96Esxn-6DoplkT3AZ0U-hayGoGFCQOazGvC04UtOSXhIyzWq5iYT1S7GhwBL4RGT2SupYD5D8MxsUfemBmYke9qbpFXE-vvbrbjL22ndbEcTOv0DFqwlLXnbgd4qRRBgTUsX6OabdYdVhUffHm1Kj5AyUwu4PS3Wc1txn1gNtPmvtoLWqrDZHi-9BtXv7QHWZlo_25Vbz8aZ3xmeFSDSLKLqbKdIe2quavR8bFZajnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سید مجید موسوی:
حملات موثر و هدفمند تا زمانی که صلح به سواحل جنوبی و تنگه هرمز برگرده ، ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68347" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68346">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2_AhHecTZ1NbIKLVSYm3DsEifTMZ_9TSU6kXO4fWXeMs3hD2_ArJEdaXy3ciQmNj7V_xzRcyn2FUO5V0g39cSHDBADV-Xai4_BRouYVE8U6yygCV9cTtAg987Hv9yf9ALYS5sJJE5L8Acaw3hsiF2geBJ0WGf0nonnKsuFDcT73kgHj6l8EMzzXd4IKPaTJPyvKF8O09x7HzzOp-FqykqyKjufanHl_T_SUCG7gnPluPs-vWjy-BvcaaxDYvh_SdSUEdadbxPDrq7VCS7LwyXEJAfSBvpyrsxZc3QHvoSewiDPYwWrZ1zITH82WAiw01Ejdk0Zc4o_FO6BKelrGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از قوی شدن احتمال حمله زمینی امریکا؛
بسیجی ها توی گوگل لغو عضویت در پویش جان فدا رو سرچ کردن و این جمله جزو بیشترین سرچی های یکی دو روز اخیر گوگل بوده
🤣
🤣
عرزشی فقط زورش به مردم بی دفاع خودش میرسه تا اسم امریکا اومد وسط همه از ترس ریدن به خودشون
😂
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68346" target="_blank">📅 15:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68345">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioxqVO2YppG9C8xOF16wAPWGeeIeVUjpgy4JKIhhW_0oG5I9As4S-VMBUIHlOpoN64_-75CAQVT4mEWKG0s7cha5LuQIJqrwCY5LxgAg9bOIjzSVyAlqbFQ0kH5VIxqotwyKX1eq-bZAGRvquGe4xihHZiKHTLgeEKUAWxv0WSEkYqR_qHW5_EYvm8NJpFlLv7G1A8IcvmHab66Ru2P4CHk_GS5Qa7NHAx-Ck-ti06QDEkiL_ANFU0oSnj9m3lgnpOQ4JuJKMajxiIS7Pvh1rs9Dy8lFUvbF_SK-Hq--SkMjccC3E9a8cli6etgP9owjMWvnZx1-vkHSM1R61lCmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همچنان آمریکا در حال انتقال تجهیزات و مهمات جنگی به خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68345" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68344">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی، تحلیلگر ارشد اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن؛
الان هم اگه سپاه تو تنگه هرمز به کشتی‌ها حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور رو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68344" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68343">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
در یک حمله غافلگیرانه به پایگاه آمریکا در العدید قطر یک سامانه راداری بردبلند و چندین فروند سوخت‌رسان آمریکا به طور کامل منهدم و به چندین فروند دیگر آسیب جدی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68343" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68342">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68342" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68341">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHLLfoI3Z-JTjxWWm95I9LkWX-h0qaYZD9tzQbbZBcVUVaskEV20U7GAYAkr-mWh7bTu9gAgyfuxwwoO9Y457u08gXm5GL_w4T66QPwRdlhMAOZKWIss4cTCNk9fPTTukDujKarq3ssMwhlmo0f9_AILMwS8Bfk0R9Rpfc_BuWtgJNuyPexjfxXFHSSDTy3WdFIBGtzHMhpGb4C0WkZ1AJUEzdzG8ENIm3LwslmImhfTR-xjRVfHGeDcGINjPChJay6-oJEEkf_ZuGTvySLgyc2BnD5yUbjO77Z4mInGbr-zdlTyd8HSz91IQq3EuB4VTr87xTRVlbhUgGmDcKlaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68341" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68340">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی مطهرنیا در برنامه «با ضیا» به بررسی برخی سناریوهای احتمالی در تنش میان ایران و آمریکا پرداخت و از احتمال حمله زمینی و نیز مطرح بودن سناریوهای دیگر سخن گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68340" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68339">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسلیت به بلاگر های چابهاری!
برج کنترل دریایی کاملاً فروریخت دیگه نمی‌تونید باهاش ویو جمع کنید
🙁
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68339" target="_blank">📅 13:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68338">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn5TQD-dCgfuSV2W5TNDbOMbV_ZL2oVcg5TLAL9GxBVNqKusEMM8tlv5ljEs270YSRmN8wFu8weocjHqQcd4vjAdlYbfUlrMUCtURXbpEYV-W_5_2noEdWlCKg_Ic8avQgtkpX1AcdjajTtDMz0VwNSEsOyKflIUlHg0h1akTd0c0FkG7_Z6k_EEBFWGZd5N12amNZ2URAj9Q7ds3WEQzeliHhqcZlb-ChHGk6T37gHYGTnnkxu_6Crbfdb7sHkDGnh62wbPa97O5PcB9QMPXkrc7FUUELicyPz9y4tY73MTfe0BFOD4BrJ_IghbYTsA0WYP_ecy2rT5drznNsxurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دقایقی پیش یک فروند نفتکش که قصد عبور از آبهای عمان را داشته است مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68338" target="_blank">📅 12:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mi7BttRD_VR5EK9QC8cUXdoDUzZbQ0xZBg4QqOiwpK3IABA-J3_7HhZloHFKXbAESOsKMS4CqnKhGsi_xUBigEaaf6fdE-MTGO-3q4xOzTDVm-NjoWJsVrGPrsDmoePIBg_9oInEiUG2QKu0-FUYGLoFpGLhgYrahJ3MNUqB6LBDxcmcrivse2lNotPKcAD8ATTCTDJyvxqhOqIRC0JrXI9StuySMbaakcCTFq9wi9G2k0blT1kuLQECiURV6PoQRbPRgUNRlox7aO3ggmyJ5PFfLIgCLKKMT7JTLwOxqTEpJJxQEAl7mfxQVRrLDD-ARQQyogmmBotlUkPWWDRgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcKRR0ukohSmu2TwdLkfo7lZRvoRYl46BVhrtxUkFtEwZAZaLO7j3cnn8HmfgLtNPq1lmLpWyOBz4k9yMfdw5OBwrNQibH-EKcEpVtpSvMb9yUSLuY-N5nBpCs1J_BaKxEBKGTe2l_QHuqk9JirdAsMmqBSsKqXjqo0aesRJDh1WuCRo5OolSsEiMlR7UcclQdwlIC-2Zj8nzMGSGUuFzWeIZj1Y2t2tDwCObfQKAlwmi_enpxfIQ2qHwMJSb0VtUcTLxrsYadD2DpOg0PR0YMz_XDXG2ZfatWHA8CsK4PqOlYuW7tgzGyrjT6fBTAMT_XabExl5riKocOWSbFKg3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
هگست وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد!
الان فقط یه خاطره از این برج مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68336" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
⏺
پل گریوه؛ مسیر بندرعباس، خمیر، لار
⏺
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
⏺
دو پل مسیر کهورستان، لار
⏺
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
⏺
پل روستای مارو شهرستان خمیر
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2nxrlVHIFxVOibw0bcckepEoDzXIrdUVRkRcukWeAHF6I5N8AfeJdfoffFEzfOnwNevucUVv5bo6ZNH8jQ5Pzlq0KavZnpAeyP7qEhUIygfZZPyOao3_8UXFnzYXKr90Rks1emUunjWToC8pTHroe_C-_O3klGTun4J97LOiLfIx-KGy5h_cbE76tKI8x4Z3_Sf4jOoaG2i4hSwsU7U0XB2lH-t-AfwspayzfwnJsvhCpscuBYoPudNsKcWogs2QdHGLXuUjsh6CH1XRJSyRKu-bNdX-Gx1laEjKovJO_M4DDp9KihdDzMdpCLG3qK5pTdotBRYnbL0OAy2UDHRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSEvhXWR_reVlvuXq34y4-0ZGZQPuSiLwOh5G5PsbaArkWlSjxCIhXgrVXyGIp7fgE9fLqmfCYRMIZsq9rbFO2B-PTFfa73PmQgastYVSrEIjyfTPRSe_1htFUkh2WdO4x9-QuefVDXFJjkXLH1jyNa0mgUVu-kKbcn6H036gbwBEcVEHeoYyAb4hNqLxbXF4V-SMTEimYpv9o1sooNJ5SIoIkhSNn_18obKJRpdWZi5vo051vtuZCRPDQXMxB3_vgxNrqWSQKCHxU37uHPquya7XmNGayQMDb_7p9vSjHgRbj04_g8hVnzvwgk25jqARgyhdnhtltYFlEx4UzOhWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=NOfUKKQP-nd_KxYuUU-3ZIVxQ1nqrLYld0j8w4OsN3A2mnMQuum-rWD9s3wfDPwz4T_EOfQTmn6yTDvSk8cQGkNWrSfM3bvMfapb4yMV-Xt-vtbUp1YvTM5SyRrKl6siCp3USwjyXHhw3zy3dic46KBpiT2C88MXzFZo3uZJjQqbDELJLedeXgfLdur-jRSr5c7Ogvy8_xQyEEcsn1oEUPvLSmrAm-KHnEei9QJCxJZUP7rTBM2eZpBAfM42qQaqfzwZE4axa8qxNJUKOjdCbQEfKlY6oCYpm9fe2HbKrdIa1RPFsQAGhCuhXjctqTvSuunD6Aj3tz_NZrCJ6Hj49g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=NOfUKKQP-nd_KxYuUU-3ZIVxQ1nqrLYld0j8w4OsN3A2mnMQuum-rWD9s3wfDPwz4T_EOfQTmn6yTDvSk8cQGkNWrSfM3bvMfapb4yMV-Xt-vtbUp1YvTM5SyRrKl6siCp3USwjyXHhw3zy3dic46KBpiT2C88MXzFZo3uZJjQqbDELJLedeXgfLdur-jRSr5c7Ogvy8_xQyEEcsn1oEUPvLSmrAm-KHnEei9QJCxJZUP7rTBM2eZpBAfM42qQaqfzwZE4axa8qxNJUKOjdCbQEfKlY6oCYpm9fe2HbKrdIa1RPFsQAGhCuhXjctqTvSuunD6Aj3tz_NZrCJ6Hj49g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khUIkCtQDwJtTPXDTO430S4btMi--AT8V0egBuU3LYRm5tv8U1jreuvWjNEqxl3fknLzSskmA9VQCnzhF7NWlQL_GSZZC9gASBSDFezsP6YaCXycC_6lwVo0fx87TsGmLk8y0-UZTx-H5To-CENzi_nHgqYirQD6-e2YImqMEOFQlEcIKSwV-O0vPwtxmR98ODTEBHu54EdHU64ReqTX4L3zYrtIwdEHPYbVvg5k4ZILMfw11pe4SPiLHg5uOUdhV1pYL7FAAiJR06nzWbP32pJpXE-FzFqoPuxTj2LMWvw7mYGqViDEKwQkxZ1KF5MKc590ojcJjcKDRMRbeYrOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=ZYiyA8zDit73TgPqjNZlrB0FmvxZcTRgqHRAEMwRnq7_YroOcnDJx_ShmuCVPO7xHOqWWSsPmxb86pQlIpaQxJaF_8NCaCazbegUnAtSI6iMcSi1F93PlY-E5Ke6Z7AR7yTe88qzKutd4zMEVEoxfHKuehSlF8axBNepJy8-RVMZ6Z0xQLVa036lGrJFzPiHBMuo5qj3OYFUQzVzjWGAPODkrJUggC3oO3dQE0CpFyMzZRrIFI5ZzrPTCskJhJDnXAtAyCP38XhiwDAqXhr4E9mwbryxTAyocbd57NKd1lrJ3Ma20ma8eMedMVrO7jinImL6vjjgk7soRVPPF6eqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=ZYiyA8zDit73TgPqjNZlrB0FmvxZcTRgqHRAEMwRnq7_YroOcnDJx_ShmuCVPO7xHOqWWSsPmxb86pQlIpaQxJaF_8NCaCazbegUnAtSI6iMcSi1F93PlY-E5Ke6Z7AR7yTe88qzKutd4zMEVEoxfHKuehSlF8axBNepJy8-RVMZ6Z0xQLVa036lGrJFzPiHBMuo5qj3OYFUQzVzjWGAPODkrJUggC3oO3dQE0CpFyMzZRrIFI5ZzrPTCskJhJDnXAtAyCP38XhiwDAqXhr4E9mwbryxTAyocbd57NKd1lrJ3Ma20ma8eMedMVrO7jinImL6vjjgk7soRVPPF6eqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=EhRN5ss_CeIpkE42hz2mr9MA6Be0fD4rHkOfKFkIgVptDMyY3UBst17q1JMbqdkS_0Zhgzpww3Dj9CeD7gj2jZZKk0Oqd08KjY1GpIZ5u-n9LwoG6F_bp_4FPWgxd1bi_jotIfMw25OvQzV4gZm4hxon46MQ3QBUQEw1TlP12t4jotXljm5huvhHTcR2ykFd6rK43oqkllmX5-mzhMhMftHHZhPjwehTeSF6kgYf-siR4Pl2p1BkqlP8X44NFwUWtqaIxqLtdFK8Y9JAlv2_Y1BQJlWUus1AecRAYZWC9DW1A4Yp7Oap8K3A6tIa5ZIVTIJ3YbggCBC-63UmCZCz6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=EhRN5ss_CeIpkE42hz2mr9MA6Be0fD4rHkOfKFkIgVptDMyY3UBst17q1JMbqdkS_0Zhgzpww3Dj9CeD7gj2jZZKk0Oqd08KjY1GpIZ5u-n9LwoG6F_bp_4FPWgxd1bi_jotIfMw25OvQzV4gZm4hxon46MQ3QBUQEw1TlP12t4jotXljm5huvhHTcR2ykFd6rK43oqkllmX5-mzhMhMftHHZhPjwehTeSF6kgYf-siR4Pl2p1BkqlP8X44NFwUWtqaIxqLtdFK8Y9JAlv2_Y1BQJlWUus1AecRAYZWC9DW1A4Yp7Oap8K3A6tIa5ZIVTIJ3YbggCBC-63UmCZCz6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPDkojMbdYkRpMrRAG_cbIiO5Nf5aM8J-a5ZdSqFosXYLocPrvP3wknkpBI7mT3FL99qeb84-zOlM4QM8K2NchcR6Bovb4-OZcK-lH7tDfHlqNm_tn2QfSxknVbzWcoPksRw7YjX52opnBVImGAePt4wkJT_tgdimueUISAyBWIJElLMX-YKRif_Pz5lEciP1yhs3QD5OeKeEgT1UU4iHM64eHNcAk84jK8umg4JKmcYcBTPU1Bvm6ZM9ESCC2OvfuYM-1yOjakj6zkRqOrpye4M1SeKLr3uBenW-FY_z91qgNOEklDLxLs1n_E_U3K1Gz_eQshrwsIV2qrk2SlZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=BPuYI6ElXeHUPjO0-r7WwtG6Y8PbvcnVLxxxHNNbIVPAHV2iJetCOuNgk3HMinvDrE1f9sdWbXSJKITeCMBy-21uWkXojzH0Sm_sZ-VM3hafviisLLWZRQZnvFUlW5Sm66ReyIDOVxyP9xUGYdcrrHjh5gRH4IPN1J0ooXXlWROTfuApbSXPn-0iNNjVOvk4T9dIZ-ZyIIxatA5Nf8hosWKtStw4oWsEP8yb_RAVOkRo90lplSnoZ4OnV0dWsNeUHH-NH3Q2cFQqEnH1khg-DWf3pQFveSgvtm2DD__YPrN6kSMHq6ndB5WYzYTFwG0LoBivIzK8kR78OoIrmqjlHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=BPuYI6ElXeHUPjO0-r7WwtG6Y8PbvcnVLxxxHNNbIVPAHV2iJetCOuNgk3HMinvDrE1f9sdWbXSJKITeCMBy-21uWkXojzH0Sm_sZ-VM3hafviisLLWZRQZnvFUlW5Sm66ReyIDOVxyP9xUGYdcrrHjh5gRH4IPN1J0ooXXlWROTfuApbSXPn-0iNNjVOvk4T9dIZ-ZyIIxatA5Nf8hosWKtStw4oWsEP8yb_RAVOkRo90lplSnoZ4OnV0dWsNeUHH-NH3Q2cFQqEnH1khg-DWf3pQFveSgvtm2DD__YPrN6kSMHq6ndB5WYzYTFwG0LoBivIzK8kR78OoIrmqjlHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6Nrjg9JoXKYJmLEHeqZKKJUcfapkT1J1BC8RN-6oh3b04OZ1M2FGSSNe9m4XVJdc8EqyDRuDOa5yQ4QbA_uYIsPFqRwJokZjzsSwk7lHewRxIIDGCeG5HaEGrTxf1hn4F715J4J-NcIDBPUC0ipNqb6diHAOOBYIpbxfz8r1NmTuYDNL4zV0uSXExB64SUacKZluydZxgFNhw9ddQSFMM-apnCxXBApVB013SESqYMsd6yQSLMZGriBcgicsvTjZZos5V4pKHYVAW7LofD6q5UsPOFqsTNkVwM_ozLCi6Yxah_Z8B1t4aBwhdKRgc1GRanINILIwwU6s0zofPrmqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=RF8CriPC1Z0o3sLN9dbWVWtDPf4Hn7mops2VhfGAFOLmsh1OnhCeREAmUE0B3pswQszeqibtI91WznupEEQy3wQeZZjKBICWz7Je99PE0jwXhAu63cNupudP0l3BmKm9koNtJJiv6PBfKWszckaNmViAFdZIX0r6GuTX6goFMsOcyXno7YUF1koVLgKdFFm0JNIpioA8BkSrYD76mvSeatjKpHM0WOWBqsO49ZC2YHZC1J6PBDznVGjLyNkoWRRCe6k3--ShPuQbvvliK4frPP8_zvH9dEx-mwoDXlf3hcVtI99jpKTEY_vPVfy5XE2ehEswzOG2cCHyfLe8RizJcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=RF8CriPC1Z0o3sLN9dbWVWtDPf4Hn7mops2VhfGAFOLmsh1OnhCeREAmUE0B3pswQszeqibtI91WznupEEQy3wQeZZjKBICWz7Je99PE0jwXhAu63cNupudP0l3BmKm9koNtJJiv6PBfKWszckaNmViAFdZIX0r6GuTX6goFMsOcyXno7YUF1koVLgKdFFm0JNIpioA8BkSrYD76mvSeatjKpHM0WOWBqsO49ZC2YHZC1J6PBDznVGjLyNkoWRRCe6k3--ShPuQbvvliK4frPP8_zvH9dEx-mwoDXlf3hcVtI99jpKTEY_vPVfy5XE2ehEswzOG2cCHyfLe8RizJcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=a0BUYmg0AzG3gcoyHGjAjeUYYzV_K7BCppU1WZYp4_FF_VAIQB61GgKCHnTNBvjO4OqHfuQKlj8kPqFNonni2XIrKQjxBhFzRg3M_58PjlXbd46pECwbQn0j_fn1mqJFc2a4kO4ykxDy90VLyTm2lFMZpdVDax2aC6tGYNY-KRK7PDkUuDnirQiLXyJVsgrabbNJlrJRwqodtZ-_e1LECWR2qkRTa76hBbdW4ui0MRsjI49_QQYRYF0P4T-AaWK_6C5V-uZ94BcJOV6AHux8YPaSoSIX9Dd5INw40z0aNeFVUgWUzqfLj-Aq5mrEsZ5OS58d4QkE60WG896BSoV6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=a0BUYmg0AzG3gcoyHGjAjeUYYzV_K7BCppU1WZYp4_FF_VAIQB61GgKCHnTNBvjO4OqHfuQKlj8kPqFNonni2XIrKQjxBhFzRg3M_58PjlXbd46pECwbQn0j_fn1mqJFc2a4kO4ykxDy90VLyTm2lFMZpdVDax2aC6tGYNY-KRK7PDkUuDnirQiLXyJVsgrabbNJlrJRwqodtZ-_e1LECWR2qkRTa76hBbdW4ui0MRsjI49_QQYRYF0P4T-AaWK_6C5V-uZ94BcJOV6AHux8YPaSoSIX9Dd5INw40z0aNeFVUgWUzqfLj-Aq5mrEsZ5OS58d4QkE60WG896BSoV6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات موشکی و پهبادی سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=lk7_cPbmnn46HTofmPmWggYVi_10QDou4bEZDqD7LBc8Ffx9N77l0gHdfimIcbmEg1YLTEHnR9PzXgjQg_TmElW7x2shmlYIAdwlDNVjmB3UvGnhrchFJL1aDfpqYKbVgl4SnnQkaWKeJPXsCCvgJwq9T9Kjd11-8UOLUToe4F37vYnWqsEm1lJu8NYhBhEul0NIMqI5QbqoAtJXG7-Mx5364_gfwMJPTlhuj8ADQ2_HC6ZRm5WeCZj9izIui31C-kcRIPRjFiGfw3_aCu7UGbPjhrL3rt3kt_8uHO-rAy9W5c9rMwSCSYVOq1-wdkvHae1EydijUtdEQl3wnOlg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=lk7_cPbmnn46HTofmPmWggYVi_10QDou4bEZDqD7LBc8Ffx9N77l0gHdfimIcbmEg1YLTEHnR9PzXgjQg_TmElW7x2shmlYIAdwlDNVjmB3UvGnhrchFJL1aDfpqYKbVgl4SnnQkaWKeJPXsCCvgJwq9T9Kjd11-8UOLUToe4F37vYnWqsEm1lJu8NYhBhEul0NIMqI5QbqoAtJXG7-Mx5364_gfwMJPTlhuj8ADQ2_HC6ZRm5WeCZj9izIui31C-kcRIPRjFiGfw3_aCu7UGbPjhrL3rt3kt_8uHO-rAy9W5c9rMwSCSYVOq1-wdkvHae1EydijUtdEQl3wnOlg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/68316" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68315" target="_blank">📅 01:24 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
