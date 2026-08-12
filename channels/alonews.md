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
<img src="https://cdn4.telesco.pe/file/TF5VU5EXClRNOWjcIzWzl57iqYxUzwjq_8beCc6MU455pTd7H9xnNvSAP1AJWQIz_H-jrEzaUp525VoHVKoFf5jpa9VxSV7Yq99avX8acNk5q4CFG7k9NsTZzSZSeS3LpVubPU00PJwBNWcfEW-7ULPudr4fWCTzkFPZtw8Ttapi5jS2_5rcvVvBhy_9ov6035OM9gW-z3gOuG14cO4NMEWaRvQdEnC6wfE_vi8xyRjUQWl6ljjcCTCoFoAU0oqMxiOSiPXZ5irapoGKLtJhlEZ9B_XGOU9iInnSgWK5pxoie1O7aK3krUu72y7PIePwTRZ6wfV92TVKwTKAozgC2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 967K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 13:06:38</div>
<hr>

<div class="tg-post" id="msg-141291">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65a8eb14e.mp4?token=qmcO84cuDasUAK0rvYX93fefwxbUbdz286YPCA8ZZxwXAHyTd-LF2oULeLhCo0HuRtklrsX13IrnMIEEhYVidJBRR45aX4Z7LQyN2Lyg8e17ee4GsnVKKAo9T0qSt208u22vyyVEZNk_XDqTTen82auTkaQJOsKrDC_qh0qL86ATZUBc4_ytd8SPcVJ-zr_M07jDwqgmcrno-fg1Uu-LJY-FfRziL5ims-JENjwskM0fLzp3nTLnZThxDPftReTllTuTsYhLs_JzB7Snn9GvTCWVuFgQPDqoIZ7_jWnSWPRX9pla1ISqq5y9E-W_tP8UUyOwfTgKHIuC0JdLtnheKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65a8eb14e.mp4?token=qmcO84cuDasUAK0rvYX93fefwxbUbdz286YPCA8ZZxwXAHyTd-LF2oULeLhCo0HuRtklrsX13IrnMIEEhYVidJBRR45aX4Z7LQyN2Lyg8e17ee4GsnVKKAo9T0qSt208u22vyyVEZNk_XDqTTen82auTkaQJOsKrDC_qh0qL86ATZUBc4_ytd8SPcVJ-zr_M07jDwqgmcrno-fg1Uu-LJY-FfRziL5ims-JENjwskM0fLzp3nTLnZThxDPftReTllTuTsYhLs_JzB7Snn9GvTCWVuFgQPDqoIZ7_jWnSWPRX9pla1ISqq5y9E-W_tP8UUyOwfTgKHIuC0JdLtnheKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک کشتی مسافربری در سواحل بالی آتش گرفت
🔴
۱۳۱ نفر در این کشتی بودند که بیشتر آنها توسط کشتی‌های عبوری و امدادگران نجات یافته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/alonews/141291" target="_blank">📅 13:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141290">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فارس: هزینه اجاره نفتکش‌های غول‌پیکر در مسیر خاورمیانه به چین به‌دلیل افزایش ریسک عبور از تنگه هرمز، از ۲۵ تا ۳۰ هزار دلار به حدود ۵۰۰ هزار دلار در روز رسیده؛ یعنی ۲۰ برابر
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/141290" target="_blank">📅 13:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141289">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9e409144.mp4?token=ZWpR7XIHaN3Xoyp2jvS3OVrz1yLCMucLo9a9MdigeS6hipsqF4qhFREPW0JNBV9-43qBzM2ukShshDNuSzNE3PQWWr0mDENUzTw0RfuEJtnCvShjk5YUQAY_2ApK4TDsI6_1P9W2_qAkeIGwTvhdL4G7-_7uBIXs6GRACJlk7RttqooJdqM6oxkosv-quFIiTXjTi5MEgZDf52AmDOB3M00I1AWTn7EUfuaFSzDgm5GecvDyXfmk7Hd8bQkEIU-hUbz0rL2UsAoKHhDw6UB9fh6TPEUohJG4R0nUugjTOOkmbreI2g4ZUJFv4WFoTVBkGA94g3kPnFI3gachF3s-u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9e409144.mp4?token=ZWpR7XIHaN3Xoyp2jvS3OVrz1yLCMucLo9a9MdigeS6hipsqF4qhFREPW0JNBV9-43qBzM2ukShshDNuSzNE3PQWWr0mDENUzTw0RfuEJtnCvShjk5YUQAY_2ApK4TDsI6_1P9W2_qAkeIGwTvhdL4G7-_7uBIXs6GRACJlk7RttqooJdqM6oxkosv-quFIiTXjTi5MEgZDf52AmDOB3M00I1AWTn7EUfuaFSzDgm5GecvDyXfmk7Hd8bQkEIU-hUbz0rL2UsAoKHhDw6UB9fh6TPEUohJG4R0nUugjTOOkmbreI2g4ZUJFv4WFoTVBkGA94g3kPnFI3gachF3s-u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسعود نیلی: وقتی تفاهم‌نامه منتشر شد گفتم احسنت بر کسانی که توانستند این را از آمریکا بگیرند.
🔴
یک ساعت جنگ بیشتر به ضرر کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/alonews/141289" target="_blank">📅 12:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141288">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی:
نشت نفت از نفتکشی که در شمال شرق جزیره قبلیه عمان به گل نشسته است.
🔴
انتظار می‌رود نشت نفت از نفتکش کارولین بیزینجی به عمان برسد.
🔴
بادها دسترسی به نفتکش به گل نشسته در نزدیکی عمان را محدود کرده و عملیات نجات را به تأخیر می‌اندازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/141288" target="_blank">📅 12:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141287">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
زاکانی: زمان حمله آمریکا، آقا مجتبی تو منزل کنار همسرشون بودن و همسرشون شهید شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/141287" target="_blank">📅 12:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141286">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424fedac1b.mp4?token=tFfY7NZOU00zlwUJmZ5qBWZ_feLhPVkERINBftC7yPhJ5ZqRcoOG_V633vhrp_IjALgW70bD_9nmYohJKUkRWX9Tp_chzroVu_DwolXOEHf1t10yWD_1hVWOtPpxkq2CTzyitYgfwVTqFPerc8YX39Q_ePjLvor_HWnZwQJjBkNDdktscjasVrb5HTRm42f5Yc5jr2V_-S7gqT753wTWv70uC7ZttQE8iW3i5TVcsggsi0QB9KHiT19YsvCocxl1PQ9Px5zacqdz53iqL3zSchJ8_VksirzoaF4L-ujFyZWXTW8rRCp4fvo8qDQmrcV6bfuvPWj2RIs5fs-y5U5KAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424fedac1b.mp4?token=tFfY7NZOU00zlwUJmZ5qBWZ_feLhPVkERINBftC7yPhJ5ZqRcoOG_V633vhrp_IjALgW70bD_9nmYohJKUkRWX9Tp_chzroVu_DwolXOEHf1t10yWD_1hVWOtPpxkq2CTzyitYgfwVTqFPerc8YX39Q_ePjLvor_HWnZwQJjBkNDdktscjasVrb5HTRm42f5Yc5jr2V_-S7gqT753wTWv70uC7ZttQE8iW3i5TVcsggsi0QB9KHiT19YsvCocxl1PQ9Px5zacqdz53iqL3zSchJ8_VksirzoaF4L-ujFyZWXTW8rRCp4fvo8qDQmrcV6bfuvPWj2RIs5fs-y5U5KAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تفاوت خرید گوشت طی سال‌های اخیر را ببینیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/141286" target="_blank">📅 12:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141284">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK3VkU-j3Gf2WhRvesf_Fep0pptywOAS0P0is8rB9p8yRjTO4rqeuB3a2c-QlyeY1uB8OMuSH9qXejbXmtWtNuEUBzxfyhQvwTm5JwSQV_BJ2vbnRbtcbdp4DzX0wbIa5CGm9BtoPQwJLZCwslNTChGlkywo-cW_DNh5i7_Ct7GtWvy_kupTtgv69_t0ytGzVkjpWrTwDqcBs8jBl_69SoEu1JmFoRfZynFHIVdjjrMoo3nEQrpGa0lckq12-Gu03Dvc236ePcA5ni9JIiDRPBBsB3pf-QeJzYgXreOTcx530VST8ka2ibE3JR-MEnuiUEfaJtuQ6s1yY6FZKtwaDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf690f4728.mp4?token=MUsCUDQfKdWOgFiOdd3rHwuo2wQUmD38qKHitLTBwXUXeBPgLNUpWjYG3j9EBjSD59j2LTbK1xT_SH2nQVsDgZRVCXdZPrpwWeAEqiyVn1ig9Eb2YCLUpEBw9m1jVAZwLPxjn9lifW0aiI3ri-PyYiZDIWSRwxVFaGO5F5bGDJ-csY9JyevswTU9oJJdZdvxnWGrainTNS0xjMHMCOxXFgmihQuaTV4g30eU6fD7nlYFQe-yrzDs9VmbDtSHvX9yEqnONyYRf9m782_FJyDr3uMrxoW_zKgMuTo-mID5KE8ChRO7mJAOYrPIpICINWhx-ZSwywbENeIshceEg4PEng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf690f4728.mp4?token=MUsCUDQfKdWOgFiOdd3rHwuo2wQUmD38qKHitLTBwXUXeBPgLNUpWjYG3j9EBjSD59j2LTbK1xT_SH2nQVsDgZRVCXdZPrpwWeAEqiyVn1ig9Eb2YCLUpEBw9m1jVAZwLPxjn9lifW0aiI3ri-PyYiZDIWSRwxVFaGO5F5bGDJ-csY9JyevswTU9oJJdZdvxnWGrainTNS0xjMHMCOxXFgmihQuaTV4g30eU6fD7nlYFQe-yrzDs9VmbDtSHvX9yEqnONyYRf9m782_FJyDr3uMrxoW_zKgMuTo-mID5KE8ChRO7mJAOYrPIpICINWhx-ZSwywbENeIshceEg4PEng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شاید باور نکنید ولی۲۰ سال قبل «پارسا پیروزفر» به دلیل خوشگل بودن زیادی برای همیشه از تلویزیون ممنوع التصویر شد و رفت سینما.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/141284" target="_blank">📅 12:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141283">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: وزیر کشورمان پیام مهمی را از سوی نخست‌وزیر و فرمانده ارتش به رهبری ایران منتقل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/141283" target="_blank">📅 12:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141282">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
روند صعودی بازار طلا شروع شد   امروز ساعت ۳ یک تحلیل بسیار مهم از طلا و تورم داریم و ساعت ۲۱ قسمت ششم دوره رایگان  «سواد مالی»   حواسا جمعه؟؟
❤️‍🔥</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/141282" target="_blank">📅 12:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141281">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9cNoG2R89ROAILefAyMAu_4BVUJ73CiqxIyhrzMWlL9mLCccOv8ipAiKqi7dW6kCdR7T4HTTBcBysgLgZvusoHahSKpFJnsOKisGeqX-Xn8XTHzo2fyYtsQwk_JaoOtmyky9aZqKYJPthNQO5FWPfv_YZ5zHf8bPKHa42zawnbuDv96XfYvYIWlX5azoEztpC8ojrSMuMii2POw9MBfj_XI0wVgFtziVI1kzfnftbLEhRP0DCFq_PjKtJwcnuWzUBK7PCML4qvEpcAku0ljy7QXWHtR640ELbGAV2YzFWeOHK8sdn3j2f5k89H3RIGJBMC_abyLmPDeA2wsnXJ2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حجم نفت رها شده در نزدیکی جزیره قشم که بسیار خطرناک است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/141281" target="_blank">📅 11:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141280">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: پرونده میانجیگری بین واشنگتن و تهران را نبسته‌ایم و مدت ۶۰ روز مندرج در یادداشت تفاهم قابل تمدید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/141280" target="_blank">📅 11:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141279">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cedbc59d6.mp4?token=SGAG_8t_ueKntPONwZeO_L538WS7mxRjVN7WBSoYgvvFYWrePWY66D_JGI6B-p5kxmx3mEjpP8y7kHKYkpPeiPhCCyFqbVo4Kd94GWZJF5UME_cx0RhU44NEI1BKy-N7v2on4yykFxqFN6TsDIPlwvPhMYl45eZg-WcKg4B4CGhcQcr2m0Uo-9o7dFFErgKkp-gWSMq2RH2v1waT8HDY-TPueaKfF8ujw16D4YSw38rNZKUQFYzwG7PVnbYEYGhXedVuhMbgez31hzJVsqB2j9jXNv9ip7BhetChzNXHgxwm9qCUY2z3C9BHrl5dVp6fFH4z4Vzc-QIV1DC5JllLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cedbc59d6.mp4?token=SGAG_8t_ueKntPONwZeO_L538WS7mxRjVN7WBSoYgvvFYWrePWY66D_JGI6B-p5kxmx3mEjpP8y7kHKYkpPeiPhCCyFqbVo4Kd94GWZJF5UME_cx0RhU44NEI1BKy-N7v2on4yykFxqFN6TsDIPlwvPhMYl45eZg-WcKg4B4CGhcQcr2m0Uo-9o7dFFErgKkp-gWSMq2RH2v1waT8HDY-TPueaKfF8ujw16D4YSw38rNZKUQFYzwG7PVnbYEYGhXedVuhMbgez31hzJVsqB2j9jXNv9ip7BhetChzNXHgxwm9qCUY2z3C9BHrl5dVp6fFH4z4Vzc-QIV1DC5JllLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های چندسال قبل احمدی نژاد درباره طائب: تعادل روانی نداره و پرونده سازی میکنه برای همه و دو به هم زنی میکنه فقط
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/141279" target="_blank">📅 11:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141278">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG2SsPddmJ2O15UPPxPIk0SVLxqnMi252m37Ef0mJhwz6TJEnhBt-x-OgPsl9punUJAOktiYDnzCM8owRSajdLUHacm-3R2JZDpq8R9fKd5RvBndJWrxRjZl2Wl25hriTHagvv53ZKQRAchL3Dwd-0dcjt05Lzx_4jX3q5o68u0ovwEjOsONXgYnM55lISqLGT5hMW93FZoq7o503BEys-KnzAVkOdSh3yd4-n7Fck0mdQ04xXIkTkd6qUzJ_bdxik-fG4S6S9BU4X-eHDQvSYOEaTQU421HMCkYvJITD63j43FRbhFMMWUIIV1HmoN0u1NQjVidLitEfSnU4zc6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنوب ایران نابود شد
‼️
🔴
لکه‌های نفتی به جنگل‌های حرا در قشم رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/141278" target="_blank">📅 11:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141277">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6895ee6189.mp4?token=K1iNO-hWbEiL14W_YeV5_iKzFwrJIdtJqpdiAJFIEVb9gXdOQnee4lp7fdUjgviFhhlrCAv5_CZU7URezGy2y-A94gOUNLeSivDoA2gCR-Gn6ktUcq_vtOB-De4s2wKGENskRfOBVcUBcWXt1OqQ4SiS9a2_N-R5KGzbGnTIdGKBP4iJlDvDJFqYz3rTSIiAa2SBEockuKk9oVKvMeLH2jAwAIzFJAaDol9AtGJm_5YnFz1nkCd_PzZwJRUBwVjGIsKeD9SLuRt2ORRs952_81UR_xMYRJrF5yCfoyoWbcTDZ5abigT-dDsrV8e4x149_w7BS0HCwdwPWubmVRB_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6895ee6189.mp4?token=K1iNO-hWbEiL14W_YeV5_iKzFwrJIdtJqpdiAJFIEVb9gXdOQnee4lp7fdUjgviFhhlrCAv5_CZU7URezGy2y-A94gOUNLeSivDoA2gCR-Gn6ktUcq_vtOB-De4s2wKGENskRfOBVcUBcWXt1OqQ4SiS9a2_N-R5KGzbGnTIdGKBP4iJlDvDJFqYz3rTSIiAa2SBEockuKk9oVKvMeLH2jAwAIzFJAaDol9AtGJm_5YnFz1nkCd_PzZwJRUBwVjGIsKeD9SLuRt2ORRs952_81UR_xMYRJrF5yCfoyoWbcTDZ5abigT-dDsrV8e4x149_w7BS0HCwdwPWubmVRB_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیه‌ی هردو سینه‌ یه خانم برابر با دیه کامل یه خانم هست ، و دیه کامل یه خانم کمتر از دیه‌ی بیضه سمت چپ یه آقا هست !
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/141277" target="_blank">📅 11:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141276">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ارتش آمریکا در دو جنگ اخیر با ایران بیش از ۱٬۴۰۰ موشک و پهپاد را رهگیری کرده است
🔴
به گفته ژنرال جان رافرتی، فرمانده پدافند هوایی و موشکی ارتش آمریکا، نیروهای ارتش آمریکا در جریان جنگ ۱۲روزه ایران و اسرائیل ۱۲۵ موشک بالستیک و در عملیات «خشم حماسی» بیش از ۱٬۲۰۰ تهدید شامل موشک‌های بالستیک، کروز و پهپاد را منهدم یا رهگیری کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/141276" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141274">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
یک پهپاد ناشناس با پرواز حدود دو ساعته در حریم ممنوعه فرودگاه هانوفر آلمان، دست‌کم ۶ پرواز مسافری را با تأخیر مواجه کرد و یک هواپیمای باری را نیز مجبور به تغییر مسیر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141274" target="_blank">📅 10:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
خبرگزاری رویترز گزارش داد کره شمالی در آستانه برگزاری رزمایش مشترک «سپر آزادی اولچی» میان آمریکا و کره جنوبی، یک موشک بالستیک شلیک کرده است
🔴
بر اساس این گزارش، موشک شلیک‌شده حدود ۷۰۰ کیلومتر پرواز کرده و سپس در دریا فرود آمده است. رزمایش مشترک آمریکا و کره جنوبی قرار است از ۱۷ تا ۲۷ اوت برگزار شود.
🔴
این پرتاب، یازدهمین آزمایش مشکوک موشک بالستیک کره شمالی در سال ۲۰۲۶ محسوب می‌شود. تحلیلگران کره جنوبی احتمال داده‌اند موشک شلیک‌شده از نوع مافوق‌صوت بوده باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141273" target="_blank">📅 10:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سی‌ان‌ان‌: یک روز پس از اینکه ترامپ ادعا کرد تنگه هرمز باز است، مقامات دولت او درباره افزایش قیمت نفت و بنزین هشدار دادند، زیرا «محدودیت‌هایی» جریان انرژی از طریق این آبراه را مسدود کرده
🔴
اداره اطلاعات انرژی ایالات متحده پیش‌بینی خود را در مورد میزان توقف تولید نفت در خاورمیانه در ماه‌های آینده را بالا برده؛ این کاملاً در تضاد با اظهارات خود ترامپ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/141272" target="_blank">📅 10:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141271">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رئیس‌کل بانک مرکزی: ایران به‌زودی عضو بانک توسعه نوین بریکس می‌شود؛ معتقدیم کشورهای عضو بریکس می‌توانند با پول‌های ملی با یکدیگر تبادلات تجاری داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/141271" target="_blank">📅 10:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141270">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7-D5s7jqHIRY-uMVxcwV2m-RmWaVDaQkXpi9heblAajwq9doWcj-TqDIz1wq9wCBOycj9h0ItJTu64KzALtQ7XpfCP2mP5lLYzMS8dLQ8MgEzbuVBKBunzkx3mYbrWDQX3OiHPWvaYeDNQq5Pr0sAwjT99skvwkkQLKPbV4Dcrw2-kwDV_XI7LShvXPH5z5dYK-O_Tx7U77dOhQIn33MEv7lLiTg85trefyTGz0xhOWb0k_bn-noH37pip69sleC4IFCJop-8kcoxLxv_dM9ulSrIH1jiiqLPNBgJnwGCilFAdmy3UTewwoDn1SR-a5qOUXYHgyqcHkzQHOZ29MlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اپک‌تایمز: آمریکا ۲۰۰۰ گیمر را به‌دلیل تصمیم‌گیری سریع و عملکرد خوب در شرایط پراسترس، به‌عنوان کنترلر هوایی برج مراقبت فرودگاه‌ها استخدام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141270" target="_blank">📅 10:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141269">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
الجزیره: روبیو و بسنت از جمله کسانی بودند که در ایرفورس‌وان که به عنوان طعمه استفاده می‌شد، باقی ماندند
🔴
به گفته یک مقام آمریکایی در عملیات انتقال مخفیانه ترامپ، مارکو روبیو (وزیر خارجه) و اسکات بسنت (وزیر خزانه‌داری) به همراه کارکنان کاخ سفید و خبرنگاران، در هواپیمای اصلی (بوئینگ ۷۴۷) ماندند تا به‌عنوان نوعی «طعمه» عمل کنند، در حالی که او با یک جت کوچک‌تر به‌صورت پنهانی به یک پایگاه نظامی در بریتانیا منتقل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/141269" target="_blank">📅 10:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141268">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، امریکا درباره کوبا: من مطمئنم که تا پایان این دوره ریاست جمهوری آمریکا، کوبا در مسیری غیرقابل بازگشت به سوی آینده‌ای بسیار متفاوت قرار خواهد گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/141268" target="_blank">📅 10:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141267">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbB3gzNbmukDGk2JfjzIyFmT5muiy4K3AP_it11BnWDKklESLsvBIlnUHAYlN9XMZr4FiGfncIA-K4vs_QWdfxx9L1pDBUJxnWT9LXHQ8ogU-L29wvk_g2lGqQEpIiZxZslNtGOJ5hIvBasj_4jwrXqAuhL_aX6laj1bIhJ-iROgMGqg3-R_iFaIu6Gc6FTZivlpPRE9APbEX6JjrF1sSu_G3GaZgmv-iwYLKUjH8m7at5z8cSYlND55RpDXaGCM9pjW260hErYge9YPli07dq7y3_dk3R5rPJciqKMqdWJTr4AQCXuhqli25sHHnLIO4WH3w2cv14CQ72geBDF6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: ایران فعلا تنگه را باز نمی‌کند؛ جلوی امضای توافق با عمان _با جزییاتِ مدنظر آمریکا_ نیز گرفته شد
🔴
مُدل پیشنهادی ایران برای عبور از تنگه (شمالِ تنگه، مسیر ایران و جنوبِ تنگه، مسیر عمان) قرار بود برای ۳۰ روز تست شود و در صورت انعطافِ آمریکا در حوزه «تحریم ها» و «آزادسازی منابعِ ایران»، دائمی گردد که با لجاجت آمریکا فعلا همه چیز متوقف شده است
🔴
دو هفته‌ی آینده، بسیار حساس است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/141267" target="_blank">📅 10:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141266">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: کشته شدن ۳ نفر از شهروندان ما در حمله روز گذشته به یک کشتی در دریای سرخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/141266" target="_blank">📅 10:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141265">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
شبکه الجزیره در خبری فوری از اصابت ۴ فروند پهپاد به استان اربیل عراق خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/141265" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141264">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
الجزیره: قطعاً بین ترامپ و نتانیاهو شکاف ایجاد شده و ممکن است برای یکدیگر به «بار انتخاباتی» تبدیل شده باشند
🔴
هیچ واکنش مستقیمی از سوی دونالد ترامپ، رئیس‌جمهور، یا کاخ سفید [به رد طرح پیشنهادی صلح ترامپ در غزه از سوی اسرائیل] وجود نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141264" target="_blank">📅 09:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141263">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae5a508392.mp4?token=GV8dvDkMZGTjtUjGsO7Ktj0gJPFKvXjnow2Sz72simYTPBDKTPbooXGQNjFa0lDSrCZKGvOYtrr8pdAY12BC26i8oegMgr7j1Iz9HEkndUvy49N2pRauh4_Oq1_HVG6xAkQ4eWLHvNdg9KmPxjwnuwAt4T5zgax1brumsYXJVWti8hslQpZiIN_mAZHnqUoHy587uy1nHBqGlGygry5Mys9trbiUUT8rqenvRdBjRO3o-Kk2Y1cPTOQcQgyVQ4r23MuIMNBoQpj5LIihLfyirfHXs4M_YR0cVbBFxDXYICt0l8hPUlVre3BACZQQMt9r4J6IkbW8zJw21WaXhe33cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae5a508392.mp4?token=GV8dvDkMZGTjtUjGsO7Ktj0gJPFKvXjnow2Sz72simYTPBDKTPbooXGQNjFa0lDSrCZKGvOYtrr8pdAY12BC26i8oegMgr7j1Iz9HEkndUvy49N2pRauh4_Oq1_HVG6xAkQ4eWLHvNdg9KmPxjwnuwAt4T5zgax1brumsYXJVWti8hslQpZiIN_mAZHnqUoHy587uy1nHBqGlGygry5Mys9trbiUUT8rqenvRdBjRO3o-Kk2Y1cPTOQcQgyVQ4r23MuIMNBoQpj5LIihLfyirfHXs4M_YR0cVbBFxDXYICt0l8hPUlVre3BACZQQMt9r4J6IkbW8zJw21WaXhe33cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله توپخانه‌ای اسرائیل به ارتفاعات «علی الطاهر» با گلوله‌های فسفری
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141263" target="_blank">📅 09:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141262">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
هشدار سازمان غذا و دارو: با توصیه هوش مصنوعی دارو نخورید
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/141262" target="_blank">📅 09:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141261">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
مخالفت عربستان با پیوستن مصر به «توافق دفاعی مکه»
🔴
گزارش میدل‌ایست‌آی از یک تحول راهبردی خبر می‌دهد که ابعاد تنش‌های پنهان میان قاهره و ریاض را آشکار می‌کند؛ عربستان سعودی علی‌رغم فشار آنکارا، با ورود مصر به توافق دفاعی مشترک با ترکیه و پاکستان که هفته گذشته در مکه امضا شد، مخالفت کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/141261" target="_blank">📅 09:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141260">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نورالدین الدغیر، خبرنگار الجزیره در تهران، می‌گوید: مذاکرات ایران و آمریکا درباره تنگه هرمز ظاهراً بار دیگر به نقطه آغاز بازگشته و در شرایط فعلی، توپ در زمین واشنگتن است
🔴
به گفته او، ممکن است تهران به این نتیجه رسیده باشد که نحوه عبور از تنگه هرمز نمی‌تواند صرفاً بر اساس خواسته‌های آمریکا تعیین شود.
🔴
با این حال، تلاش‌های دیپلماتیک و میانجی‌گری‌ها متوقف نشده و احتمالاً در روزهای آینده اهمیت بیشتری پیدا خواهند کرد.
🔴
الدغیر معتقد است: میانجی‌گری‌ها می‌توانند نقش مهمی در تعیین مسیر بعدی مذاکرات داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/141260" target="_blank">📅 09:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141258">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWcPKSt-LFWrMGOsjEhdt7y1itm837EAofwOAWntsi0I5CUFREtThur5FuPQBWLC2fMFvtzMKHnmKWDqz0mG98SZ3uMQBXiDC7p-s58sKjN7ywJ9-6YOeQzlfBCq6KtpsPfy0lBx1xs_BSyfsOWhnAJYb00zuHgv5l_ZczMZHI33nEfzOWRdMC5O9O3UACEznpvT0O7qel5sAlVkLZPI2VS48q86Fyd5TbXDpkrPjeavOuv26D6hBTyCH-JkXsANDkDIW5ecIKpsYZs0Bkd5RT012nIzh7jUnywUOBdQbd9MgC-ZA1TN3eU7tUh2jaiDuEKzqrMnVoSpogH4Px_LMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0a4d934f1.mp4?token=ggv7sacgVAmV5oMuNWHnmTgMcXdj0M06rQWSNDPx0ZaXPD_cW0uJpU3vj5qZKyOiDh1xdqrGyLdaHYxtxpi4AwLatF2ci7_WvH8E86NSeofF4Znk5bBHNPwre369yxZpjlJ1ecwBiO80O-3nlwTrcNDz5gwW2JWz7b1act_hg7kWs8TNmZzHxdorRfsqbFnzIRMI6IiOKF0x6Jn6D3vBcapD0E-k-3xkcBorZWdeW2QTxSOJEDj8xi41iRFLoZx9IPSCHqxKE1NREOwJPIgO7CrPZw1cDtmDizvvUZ5Q_icszhSJFXczdtqO3slhzbGmYjZTFMIu-HgGPIRO2w7Apw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0a4d934f1.mp4?token=ggv7sacgVAmV5oMuNWHnmTgMcXdj0M06rQWSNDPx0ZaXPD_cW0uJpU3vj5qZKyOiDh1xdqrGyLdaHYxtxpi4AwLatF2ci7_WvH8E86NSeofF4Znk5bBHNPwre369yxZpjlJ1ecwBiO80O-3nlwTrcNDz5gwW2JWz7b1act_hg7kWs8TNmZzHxdorRfsqbFnzIRMI6IiOKF0x6Jn6D3vBcapD0E-k-3xkcBorZWdeW2QTxSOJEDj8xi41iRFLoZx9IPSCHqxKE1NREOwJPIgO7CrPZw1cDtmDizvvUZ5Q_icszhSJFXczdtqO3slhzbGmYjZTFMIu-HgGPIRO2w7Apw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات گسترده اوکراین به روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/141258" target="_blank">📅 09:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141257">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
به گزارش نیویورک تایمز، آمریکا در یک روز حدود ۵۰ فروند موشک رهگیر پاتریوت را در خاورمیانه شلیک کرد که هزینه هر موشک حدود ۴ میلیون دلار است.
🔴
یک کارشناس گفت ترامپ تصور می‌کرد جنگ کوتاه خواهد بود و ذخایر موشک‌های رهگیر پاتریوت را به خطر نخواهد انداخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/141257" target="_blank">📅 08:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141256">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0dffaedf3.mp4?token=VAkvltPBCB4bK4QytC_595JlewpN3IRJmKBNTn1CCxLGaeDzysSr02lm0Xdrhl_jySDus8Eusw4zyf_2gGIrHXScVFN9tTMBnjU8mVheRtsWLXQY2VThLV4XI9X3Sa0m56n2Iv-zsIGrUWxAqL_JkFfzEA0GzrixK_smJYEiVFb6Gddt3PzqvxpBEoqh8T_-Zzc-hw8cgytCwsH0ClWwHpm3ynO1gSw1jQ83G0KRr1PI6spKwQ2WLhfLsUvAvBHwyUguI_m-iGGbbGpgDGgOPtdEC_jbLFqP8Oyw4Yop96U8Yva3CKxM2da8NHdYQZvzgWw3DoqX7zMOqEwLJjRdag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0dffaedf3.mp4?token=VAkvltPBCB4bK4QytC_595JlewpN3IRJmKBNTn1CCxLGaeDzysSr02lm0Xdrhl_jySDus8Eusw4zyf_2gGIrHXScVFN9tTMBnjU8mVheRtsWLXQY2VThLV4XI9X3Sa0m56n2Iv-zsIGrUWxAqL_JkFfzEA0GzrixK_smJYEiVFb6Gddt3PzqvxpBEoqh8T_-Zzc-hw8cgytCwsH0ClWwHpm3ynO1gSw1jQ83G0KRr1PI6spKwQ2WLhfLsUvAvBHwyUguI_m-iGGbbGpgDGgOPtdEC_jbLFqP8Oyw4Yop96U8Yva3CKxM2da8NHdYQZvzgWw3DoqX7zMOqEwLJjRdag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من به ایران اعتماد ندارم، چرا؟ مگه فکر می‌کنید به ایران اعتماد دارم؟
🔴
من آخرین کسی‌ام که به ایران اعتماد می‌کنه مدام به من دروغ گفتن، الان ما کاملاً کنترل تنگه رو در دست داریم
🔴
اونا کنترلش رو ندارند، ما کامل کنترلش می‌کنیم، مال ماست، شاید یه زمانی کاری بکنن و اون‌وقت کارشون تمومه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/141256" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141255">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e1e30aad.mp4?token=aSBLSiXa_CHOeKmP4Q-yV8S8XZKaT0d-Ms4KFTw3KA2kFACou9YFDW_6b89eganKSaDOAZiA2DuynPxUyLIu-28Y6JrfOs_qfirVuRckAEXfqjxPTda8KRhqvrjynJY5_2f6Vb9Cql1Joe-j4gyPeyIcDPIe3nYHfFgYA0flBZ4xYeflXdQdcy2STNOxpKnD-LGYy8vADnc5jRrb8p0WTcQthnv8sMkkCTjDut4kOidZSHmxccYgM0iJh_9411Vm_OPtdpyQ4T58HskyfzyhaiXfF5HcPDZIOfk6pSvC_jlyZzsbkDXjrqYiAFNXxIACPpwiCjDxbdhtS5jBn_O-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e1e30aad.mp4?token=aSBLSiXa_CHOeKmP4Q-yV8S8XZKaT0d-Ms4KFTw3KA2kFACou9YFDW_6b89eganKSaDOAZiA2DuynPxUyLIu-28Y6JrfOs_qfirVuRckAEXfqjxPTda8KRhqvrjynJY5_2f6Vb9Cql1Joe-j4gyPeyIcDPIe3nYHfFgYA0flBZ4xYeflXdQdcy2STNOxpKnD-LGYy8vADnc5jRrb8p0WTcQthnv8sMkkCTjDut4kOidZSHmxccYgM0iJh_9411Vm_OPtdpyQ4T58HskyfzyhaiXfF5HcPDZIOfk6pSvC_jlyZzsbkDXjrqYiAFNXxIACPpwiCjDxbdhtS5jBn_O-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
تهدیدهای زیادی علیه من هست که شما ازشون خبر ندارید
🔴
هر رئیس‌جمهور تأثیرگذاری تهدیدهای زیادی دریافت می‌کنه، رئیس‌جمهورهای بی‌اهمیت تهدید نمی‌شند
🔴
فکر می‌کنم شاید من تأثیرگذارترین رئیس‌جمهور باشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141255" target="_blank">📅 08:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141254">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ درباره اینکه چرا خودش با ایر فورس وان پرواز نکرد ولی خبرنگارا پرواز کردن : نمی‌دونم، اتفاقاً فکر می‌کنم هواپیمایی که من سوار شدم بیشتر در معرض خطر بود
🔴
خبرنگار : چرا؟ ترامپ : چون فکر می‌کنم همون هواپیمایی بود که احتمال بیشتری داشت هدف قرار بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/141254" target="_blank">📅 08:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141253">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65563b805.mp4?token=uPbpRFcMui5nHZKMK6kZ5iwbg0omozFqhckEn75AHd-mRdSKuXk4NDxEU6rl9SWXtYI-3dRXSRZckHL2tF6LBncdlnQx3b8fIJ_Av73h1Qog2kpygft4eLxJmCQ3Qp4rdejFnN4pa06BdxuwwQyXQMRotn1emEMyya-WIIN_eW0iwv9gIvPfXZXyWRaBwEvSDWdMEm_7aTiGmaPqFzbej0yrLCajwh5nrb7sX_o-5HCdUNp5nhdysvpfl2ymEhRoWEw2pt-iVYcV_gDNnVEW5SjhZuEYC0ClIYpzUjF-4QCRkg__i__uM643ZUv2B2UmPtRwIhn-wYFGZh7ugCxxNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65563b805.mp4?token=uPbpRFcMui5nHZKMK6kZ5iwbg0omozFqhckEn75AHd-mRdSKuXk4NDxEU6rl9SWXtYI-3dRXSRZckHL2tF6LBncdlnQx3b8fIJ_Av73h1Qog2kpygft4eLxJmCQ3Qp4rdejFnN4pa06BdxuwwQyXQMRotn1emEMyya-WIIN_eW0iwv9gIvPfXZXyWRaBwEvSDWdMEm_7aTiGmaPqFzbej0yrLCajwh5nrb7sX_o-5HCdUNp5nhdysvpfl2ymEhRoWEw2pt-iVYcV_gDNnVEW5SjhZuEYC0ClIYpzUjF-4QCRkg__i__uM643ZUv2B2UmPtRwIhn-wYFGZh7ugCxxNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
،
درباره نامزدیش :  دوست دارم دوباره تو سال ۲۰۲۸ نامزد بشم، ولی قانون اجازه نمی‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/141253" target="_blank">📅 08:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141252">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ee228998.mp4?token=Rim9OcFO3USdbw4n1Mw9hDBhxf5bmxolTzRucCr5leygc0uwW-ixeGzVnb3s7Mv-UWRs27qs3E-j2Jpjy45g2a7HGRv7G2jRH2yt-5NBoKNVVjViSZvFAHcoLR77tr6jLzGSF87yeNTOeT4KSqmcblvP9hQ-EhXwxSzEDkZzTy293LWATHJhkghpmzmfXD9ViJJACQSzaLoe9XzsuyOS1-iVyPGD2LorXAmHhmr22AtLB3ZaDuDeDqzUGY4vMquvx0jxJHw1uQIrQ397acMuyY8KelYF71xDSBRxV81prWsk-oLQSTxm4NhtP-QmUgS2XenwJ5PKqAwL1hArzGtvdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ee228998.mp4?token=Rim9OcFO3USdbw4n1Mw9hDBhxf5bmxolTzRucCr5leygc0uwW-ixeGzVnb3s7Mv-UWRs27qs3E-j2Jpjy45g2a7HGRv7G2jRH2yt-5NBoKNVVjViSZvFAHcoLR77tr6jLzGSF87yeNTOeT4KSqmcblvP9hQ-EhXwxSzEDkZzTy293LWATHJhkghpmzmfXD9ViJJACQSzaLoe9XzsuyOS1-iVyPGD2LorXAmHhmr22AtLB3ZaDuDeDqzUGY4vMquvx0jxJHw1uQIrQ397acMuyY8KelYF71xDSBRxV81prWsk-oLQSTxm4NhtP-QmUgS2XenwJ5PKqAwL1hArzGtvdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
اوضاع ایران داره عالی پیش میره ما کاملاً کنترل تنگه هرمز رو در دست داریم و نیروی دریایی‌مون فوق‌العاده‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/141252" target="_blank">📅 08:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141251">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e66e57720.mp4?token=rPktAjh2L5p4AiywyCJ9-TYd9gAvFDMBEPO_vuov0N-LHRXrQwfx4NvoXaT9QdMrOELlLP2_WanYdbDPVbkpXVWb--MbWKoML5im37-rhUy-8OR3newr34BTcbwaQhAj1Hb9omlD7jsO1GlT6oTbMa6TtlL0NYfDlGoMtkyaMrIGPna8vmnCzwpWjD2F3RiqetKvagYrnoF92j1Ocr61T7wVSusFDT2fYr6n-yTg6nsfJk2wAV85TvpgSl7Wohc3A5R7iVFdOC9szg80n-JYJsM2-Sln0Fxf5szDMHEPQd9T9e3BB4Nq8LXpSjz5qi7z9UI5OQ4jodgDQY5VK9I3hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e66e57720.mp4?token=rPktAjh2L5p4AiywyCJ9-TYd9gAvFDMBEPO_vuov0N-LHRXrQwfx4NvoXaT9QdMrOELlLP2_WanYdbDPVbkpXVWb--MbWKoML5im37-rhUy-8OR3newr34BTcbwaQhAj1Hb9omlD7jsO1GlT6oTbMa6TtlL0NYfDlGoMtkyaMrIGPna8vmnCzwpWjD2F3RiqetKvagYrnoF92j1Ocr61T7wVSusFDT2fYr6n-yTg6nsfJk2wAV85TvpgSl7Wohc3A5R7iVFdOC9szg80n-JYJsM2-Sln0Fxf5szDMHEPQd9T9e3BB4Nq8LXpSjz5qi7z9UI5OQ4jodgDQY5VK9I3hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شیوه جدید کلاهبرداری: گوشت بوفالو به جای گوساله و گوسفند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/141251" target="_blank">📅 08:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141250">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0bRDGgJ1_6-1a4caEaDfnJgOsWld-cjchpsaz_Qh64K1vXw7YKotFe0o9m9iYYWhbDe5l9oyHqeDHy5FMUnx-Jx5WyOYjDPW60sqk0tJKxyJtq_hgv8FACMbrcb8jzLacFtkzYWk7CB9OEjpCCYtkQOV-t9LXXCPFJt4X-JOSacwwqp1T2eH4PZCTlOH2tXWqyMOxLtzHMZ6WWWU3Q8kr8DlTgSqmABloDs3jRVqZ_asrvCGxIXowZK-tU65-2_bxv2Yr9CYR92q_F6J9usIQIH_1FhUnyah52MFq6dx2smIt767UZHOSGlsAftjZ9aUasij9mAL3K8QxgZJ98OaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار نقدی:
پیروز شدیم و به پیروزی ادامه میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/141250" target="_blank">📅 02:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141249">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPVaj4QcNdWFXPM0SgyyacVKRTnbRTIsYjcLPlEXklqbryQ8-eBP9MiLmokuVFucg7ICQLb35TAHFyEKtkBO8CwDc3eoC-V5MQLSr8-YU1EhevYvUp9rpNc78H1xuola8y001Lm18NAc0SixuehoUAhA_NdErqoV8OP6lfLgstDX-A_4ucJOsK2FzSR2l9FSkAAH-YnW64zGgyvdUoyOkeUDAExGzYQc8X_QUK-mhVirYbOhSJP9JU6YyXEmy9PIhLE3bGAb0QejjcbVUwgQtk48CB2x1aVUMBwlr7LJHNL_YmFgycDLAxm_XBuYjSpwqqCSxmAkTCAq2R4oQ6KiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسارت شرکت ترامپ مدیا در سه ماهه دوم سال به 238 میلیون دلار رسید - در حالی که سال گذشته این رقم 20 میلیون دلار بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/141249" target="_blank">📅 02:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141248">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سی ان ان: ترامپ دیگر جنگ نمیخواهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/141248" target="_blank">📅 02:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141246">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دوستان تهرانی صدا رعدوبرق بود نگران نباشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/141246" target="_blank">📅 02:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141245">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ان‌بی‌سی: ایران نفوذ چهره‌های تندرو را در مراکز تصمیم‌گیری، به‌ویژه در حوزه امنیت و دفاع، تقویت می‌کند.
🔴
این اقدام نشان می‌دهد تهران به جای امتیازدهی سریع، خود را برای احتمال تداوم تشدید تنش و رویارویی آماده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/141245" target="_blank">📅 01:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141244">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
صدای جنگنده تو تهران شنیده میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/141244" target="_blank">📅 01:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141243">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOhAaEEcxp23D99e40K6xfOVKlB8h1sXWufz3Z4H5mQUoUOKiLjCGx02iYtwWV8_VcOEU6ez7EIbU8s8xQQsYHaFlLzZ87eSxhVtE3K0FePgvMMTA-gHxKCmHlkyhj8UaDkqf4O_fXtpkUFDQVdmA9_uN_VapNEBU1cB9iPGHeF97B06QPhVGYLaUo_zitCtb_gKKvJbgB95IZK702RTAcwwkbJAH8XYxK6VQya3yEhs3_5BNQPkDcMA3K6corBMatpzz5b4eQhgNe_LtSWz0iqRNI6kqFJCxyNOBi30GXKRZCWNKkExvTCj1HmH7QujJWmkD7gsCEv9drVObgfdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: آرزوی شهادت دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/141243" target="_blank">📅 01:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141242">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zum36wI-E7VVNO8nzJJTFeYrzRpEUetW1xQtkotBJx60nnNR588n4KDQ5PewxWvCvqdCEiumDo5b9LOW13J5wiVT9x761XMrx3TN_tt41UBS8wmEJc-QF0qR9UXYctUV_Eg0tkaSsviIW4YXSmvutF8_Wn1QdfxNLdgtoHBk10S-Ns-VDvTJBOVtCUBkF4jo_BHBS0h8awMVxb5DQ5m9MCYw0FjITg5iDjON9gv9eo4SD5b61HhfjnYCXqvDZ9t-ZEPtPsCJII_5eUSL1-7OS04LjteW40_3cmqDdICQE4vnT5eD1g5DYSVxsamrkFJuHjdqJZ36eecD3th8N02g6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: نیروهای آمریکایی در طول حملات ایران به پایگاه‌های مستقر در اردن حدود 50 موشک پاتریوت را شلیک کردند. این میزان معادل حدود 200 میلیون دلار در یک روز بود، با توجه به اینکه هر موشک پاتریوت حدود 4 میلیون دلار قیمت دارد.
🔴
ایران از موشک‌هایی با قابلیت تغییر مسیر استفاده کرد تا هزینه‌های سنگینی را تحمیل کند و ذخایر محدود موشک‌های پاتریوت را کاهش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/141242" target="_blank">📅 00:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141241">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbUpgixL5Y3XSk7jIOKvRgj1yicaZQWh2UmyH8SXMiPFAqVAk7kOkO4BEBKkKhIPfPesC3oh5QQ8OLhgtP7-9k8JfORiETrZK39tLKXzC4crntH035p1fD8cFdamQqhKSJQtqns5G8RqI54yL4wOgsNiHeA907POXajdshnBmJd97wWv1M489zRoPUXOVNGnuHbSVVxPoK8K9vIHUwux-LB21OS_62DG7o7AvvdpV6UlCJTuBo0JcEdhiMqTFTE3Jp1TXwVvDTnXgDYfHiqmd8G6DIB617v5_8_FCix6nBcD5DCaOeUWKpMzXEKPE2oHCJUVuXNKpFeGShaHOH46ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی:
گرونیا بخاطر جنگه دیگه! طبیعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/141241" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141240">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLElwHeWTJpD0VEk95kiCS9Pqva_IrncgtEoZ0WWpLl3Z16eD7YW9ZCT04NJ4OIoLPQvPouiwYFl1lKW5QvGvzTXXPx5wfmxuXC8IbtB2VNkBRVjhD37q7Gvm3n9_p867tVRpOr9feasO0ulpc9MG1Z3291wcGqlY5VzDz_MHOHcYeAen5ONuh_xsHxZYwP3JlEs8D-v908hWUiMIXEMUSoTfhhWd-mDQza___snVMQdayv8f3RsdKxEnSt3tBXO65ZwWeVJwCyjLukZGfgOAQuOdGnHYfX7JPsYu76BIV4t606g1yqxI0cXtE4M3tzPkq1CfCKNYT7irz0yfLFFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت به ۸۹ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/141240" target="_blank">📅 00:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141239">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf2v9bR6LlwdjCvLnpDD4fs_O2ja4wRMOqyE1xPUtFrVyHeKGt_KiUCaVTsXAstJjrMCa6bYl1eveOgIlqWUhZL3Qb3id87EE7PYsLQqyp13ZtMqP1XHBI6lqyc2ozAgwXykb_tUa2xbA26i1IXqvnHLmlaekpf73TrLgYE8pm1lZ0lzMvtQSWbxSC7RLRmq1RRSs8Dt64WwUPam7IcI-5tfUVIk-odrCNHUo_RCNYTmgFQ6TZi98Uv29Ojupq4ERgxWLFbXTUomgkNtyKPDmYTrjj3Owl-mtaT-of6uY2FrFqqBSRjj8zOB3YOYNMC5FrWZ2ZwiDnWkHbNKSLs4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک :
پایگاه ماه آلفا شگفت انگیز خواهد بود. ما این پایگاه را طوری خواهیم ساخت تا هرکی بخواد بتونه به ماه بره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/141239" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141237">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/141237" target="_blank">📅 00:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141234">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
تسنیم در یک خبر اختصاصی مدعی شد عربستان سعودی درخواستی محرمانه به حوثی ها داده تا جنگ را متوقف کنند که با رد درخواست از طرف انصارالله رو‌به‌رو شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/141234" target="_blank">📅 00:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141233">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نیروهای مسلح یمن: حملۀ امروز ما به مواضع نیروهای وابسته به سعودی با دقت بالایی انجام شد و ده‌ها کشته و زخمی به‌جا گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/141233" target="_blank">📅 23:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141232">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
جروزالم‌پست گزارش داده سه هفته پس از آغاز طرح آزمایشی خلع سلاح حزب‌الله، ارتش لبنان وارد برخی مناطق شده و چند انبار سلاح و مهمات را کشف کرده است.
🔴
با این حال، یک مقام مسئول گفته اقدامات انجام‌شده «هنوز کافی نیست»؛ ارزیابی‌ای که نشان می‌دهد اجرای این طرح با موانع جدی و سرعتی کمتر از انتظار روبه‌روست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/141232" target="_blank">📅 23:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
الجزیره: ایران و آمریکا در حال تعیین «هزینه ورود احتمالی به مذاکرات» هستند/ این رسانه می‌گوید: هیچ‌یک از طرفین خواهان جنگ تمام‌عیار نیستند، اما دستیابی به صلح دشوارتر از پیروزی در جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/141231" target="_blank">📅 23:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frar6TydaKE_zFVvi311Z4-7QusTQVDpW3Nbu0PpzaeKrmyscXoMAPR_8LaEGEbc1kdURRO3S2rWFRefZJ14EFgeCWkuLWrlBTy7fu92HDP16k-6dKrSYHEJe5i7fC6oTPIz6ABfnunZ6CNTpAuHGdrD2Fgj5Uy6RzHu5BXYCmL3OtjOfzNCUmLWNPBhgruZEF1WcYIxnt43qgP1aNmiac26PWF9EwPDRsZ-B4ZhnpxhHO6SAsdpQ4zx7XmQUIq-4TnkOcXmkkcLJroXLGe_JS8DhS6U-dk6WVPKE7muzee-SWCa52ibyTTexV4rSt1ekNEQmvqqEvENfdp2kHEYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تعدادی پهپاد رو به سمت روسیه فرستاده، طبق ادعای منابع روسی، تخمین زده میشه حدود ۴۰۰ پهپاد بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/141230" target="_blank">📅 23:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141228">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر کشور پاکستان در جریان سفر به تهران پس از دیدار با همتای ایرانی خود اعلام کرد: پیام نخست‌وزیر و فرمانده ارتش پاکستان به رئیس جمهور ایران منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/141228" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141227">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfI804gtsWoLF-0k5Vgg8t3e1R4RDWLcv2FlKWYavANilfy1yibVSJvNngnrSj4sZfHRZctOsj4wygcqWcUisE3O7hRJjgHt1awtcA-OMEYgF-98C5Dtgyd-nBteJCwdmwPBPYZgG2L7NZ3LIovhAXesNyInqXGm3rU9EDL85ond6syXw7YKHMO2695wEwD2-QlNIMr9MXXp6PnAuv-SDm9HpwW2THNzzeklFoGTmyo1guCprqjgeEZzVWt_7noYBvtrQBSnieD40nyf0SJHb0cyNexW7t0PVlkfETVS1nAiPREGo7KdVWkCvuMmV9uGCEhBzbttKD6xIAvE2sQjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: مجتبی شش تندرو جدید را برای رهبری جنگ بعدی ایران منصوب می‌کند
با وجود شایعات فزاینده درباره سلامت رهبر عالی‌رتبه مجتبی خامنه‌ای، تهران ادعا می‌کند که او شش تندرو از رژیم را برای رهبری جنگ بعدی ایران منصوب کرده است؛ پیامی نگران‌کننده برای اسرائیل و ایالات متحده مبنی بر اینکه رژیم در حال تشدید تنش‌هاست، نه عقب‌نشینی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/141227" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141226">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7021b6ac.mp4?token=fkMzkvE-USg9eQ4J6aOd0W27RLZaJrXTWVtIycDKO2_AhXJxrxC_e27i99O7yYcAtYK6dsPCw17BjTWwOGMLizvb-vZUZX7r-SmS_ur4Zrd925Px1lviekCACQY5tDnbQslThEvnvXaegVBgbJzm6M0il9C0DHcWp3DgmnZrrihBU21MSDihDDnCYpS3vDBOa1gDyktm2JQjxvsx4Tq7R7F331IuDkAHmNQo_-EXZCXICzn0PBrFqorgjnVQXYZYoMaTZ27rLza9dC1qVlnUx2OpdBLc4zY_2_8_p_7AlnSSR5gSEsXWCoAeshcAl8S4wYwp4Ntj9JhTnfbnSJmgAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7021b6ac.mp4?token=fkMzkvE-USg9eQ4J6aOd0W27RLZaJrXTWVtIycDKO2_AhXJxrxC_e27i99O7yYcAtYK6dsPCw17BjTWwOGMLizvb-vZUZX7r-SmS_ur4Zrd925Px1lviekCACQY5tDnbQslThEvnvXaegVBgbJzm6M0il9C0DHcWp3DgmnZrrihBU21MSDihDDnCYpS3vDBOa1gDyktm2JQjxvsx4Tq7R7F331IuDkAHmNQo_-EXZCXICzn0PBrFqorgjnVQXYZYoMaTZ27rLza9dC1qVlnUx2OpdBLc4zY_2_8_p_7AlnSSR5gSEsXWCoAeshcAl8S4wYwp4Ntj9JhTnfbnSJmgAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار نقدی: بعد از جنگ، جمهوری اسلامی طرفداران زیادی در دنیا پیدا کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/141226" target="_blank">📅 23:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141225">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE-RzpMPTt_81eacMaOfXJEpUX_Y8MG4eXorCH2v-im6DkMCdtEfCMp7azi06EU2UBt1t6MdbXR2bVfkqMjAEYEfISpgz6pJOcUPBxqpdVNR9KweJP3yGbZqAF9Ysg22gqMLsNySHHrK1HlbGW-WIWtwEhh6ItSiFxBwPmfSf6wumR4ZMJ0Hu61yy0kfB764Xia0LFqIKoanM3u3W7oTGXEfHTAHuFniYa2UCe8yyroazKpgIUBXZg431UWFGML9UKgL-sqdzNkSEhcj6tvux-_5EVbMfDV3rt_a2lJQDp2x_9Kd0iALxAmMOt0klJmnQzWGRUKNker3MQzGY-bDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این وسط فیلم مسیح علینژاد و دوس پسر سیاه پوستش منتشر شده که.........
💢
مشاهده ویدیو</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/141225" target="_blank">📅 23:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141224">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ایشالا بعدی آقا مجتبی</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/141224" target="_blank">📅 23:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141223">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOSnIi3zyvD2VaRxHOmzhuCJIYlyS8e1fvHnJ2-r0OuZW-pZ_RC20v57R6XsaBrBc3v4CiQeVS29JiFpLrbAT6DZNQ1MPtOxo6sazpwwI9g8mJcSSc4h11qwj_AuRBO5-UfJr_DcFCOaL9Bcq6sUDqD0Je6BVURE-NiwWqIYoXTeyyAn5RwZEsm4zgrvG_Dy1NyHlUTYzPyBhOSTBxSkSTqsTpfApLUpNC2gaJ7myM66w54AQfdPbvh06X3f8oodInzWzG05syjV0geGwKZDDShtJIETPpgeJT9N7QGeIOVxuH0a-V7Dr_E7Rso91POof5Q21mNIJOyckb6WflM5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
کریس رونالدو با انتشار یک پست اینستاگرامی مشترک، خبر از ازدواج رسمی خود با جورجینا رودریگز داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/141223" target="_blank">📅 23:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141222">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac7e6c261.mp4?token=Z5PaYM3eloKxshfAZZZ34TgUDnDv82CP5ALf0gc0rmmzRhhBN_VmIGtbrVBBdapFARd5UttOBm5n-BpI-ArX2erWMIZ8IPouW-bi3SevrEhh-7KSE76pCsYpKymuQV-8qMuiJKOVsVF8tgvPjcYaaPnamhIFUWao0cjiabStE57bFap8sKIZv8HPBlwojl2ARAtJnvMeoggxPFwLyn_USCu4EgncUTCDSNX0KDQyU1aWkXoJmxSyBCWHQiYiwMI7_K6toivKngQ_95UGH7PFsP3PoMLmIQcn2UVkETdb9VDC6EKouFOa3e5VPuCmxdhTq7t_iz58uUofz7zZIF3vsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac7e6c261.mp4?token=Z5PaYM3eloKxshfAZZZ34TgUDnDv82CP5ALf0gc0rmmzRhhBN_VmIGtbrVBBdapFARd5UttOBm5n-BpI-ArX2erWMIZ8IPouW-bi3SevrEhh-7KSE76pCsYpKymuQV-8qMuiJKOVsVF8tgvPjcYaaPnamhIFUWao0cjiabStE57bFap8sKIZv8HPBlwojl2ARAtJnvMeoggxPFwLyn_USCu4EgncUTCDSNX0KDQyU1aWkXoJmxSyBCWHQiYiwMI7_K6toivKngQ_95UGH7PFsP3PoMLmIQcn2UVkETdb9VDC6EKouFOa3e5VPuCmxdhTq7t_iz58uUofz7zZIF3vsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۵تا زن یه مرد همزمان تولدش رو تبریک گفتن
#حرمسرا
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/141222" target="_blank">📅 23:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141221">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فاکس‌نیوز: پنتاگون خرید رهگیرهای پاتریوت و THAAD را ۱۰ برابر افزایش خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/141221" target="_blank">📅 22:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141220">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmS8jsqJTa_nPOzxVbRNlOfDJSPAixYUIHEQ36CSfkzvG8GAbwxJhvLVDWF8bqx_QUOTITioqHoJf_5Ukt6N4vjyc2xmlqD6DREmmmnw7s-C1f4RMnbCd6VIZpRHt9Dvp00UgT_pTWU3w2IXYC0rsk4S-eMVJDJ2QKGYR9_bMQI1lRg4CrhywFuPOOAFOq9sdWPpgPDHxN3vY5sKd1EN53teggo0WfofcfPDCkd6Dz4-vVs3o5PJqg8dJu-zpVnWvbukzrpYnQ7BQ2Fiyiw5q-ClsEW7Ik6oB3Ur62-AKtVdSObk3MZW_MnWMoPI_CuxsuQJBPFuT9HycCPrRbWC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام مدعی شد امروز سامانه هدایت کشتی تجاری (M/V Vela Nova) با پرچم پاناما را با شلیک موشک از کار انداخته است
🔴
این کشتی قصد داشت محاصره دریایی علیه ایران را بشکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/141220" target="_blank">📅 22:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141219">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
باراک راوید/آکسیوس: امید به توافق میان ایران و آمریکا در حال محو شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/141219" target="_blank">📅 22:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141218">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7qgiEHQhwGMI-dBCL2LrodnzaxwQ3EXlpVcORf_kEcsi6IE8jh_0yL3OCqWq9qU5eo9qmYigbdX8-Hh7GbsclpqqV3agjzUVuX3--cfiXX4RPpxSDkE4YDYczN0BTYpL4sjB2h-j1xVczqbhWG6tOqp-MMm1wCsC_T58SBYLpKin6Xu672yEkFT-tqYxOA-Ri5Y7QRUs-_EcpbV-kqhK-y1s3P7Qrz2G3Ro81GwxSUUn8ZGrmVtALBXHqle6UBFB7COykDc7lw_IcWfcx_DCPC-CMBXONVvAP7FlzBElazB9n00EtYF2rRFkBtUDalZXgPF1iDeCpspDNP2-49cHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای عجیب رحیم‌پور ازغدی: موشک‌هایی داریم که می‌توانند کره زمین را دور بزنند و هر نقطه ای از جهان را که بخواهیم بزنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/141218" target="_blank">📅 22:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141217">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سنتکام: از زمان تشدید محاصره بنادر ایران، ۵۵ کشتی تجاری تغییر مسیر داده شده، ۳ فروند از کار افتاده و ۲ فروند بازرسی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/141217" target="_blank">📅 22:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141216">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
اروپا با کمبود موشک‌های رهگیر پاتریوت مواجه است، زیرا اوکراین پیش از حمله زمستانی مورد انتظار روسیه، به دنبال صدها موشک است.
🔴
ذخایر ایالات متحده به دلیل جنگ ایران محدود شده است، در حالی که تولید جدید به موقع نخواهد رسید و کشورهایی مانند آلمان، لهستان، اسپانیا و یونان تمایلی به کاهش توان دفاعی خود ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/141216" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141215">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
عملیات تجارت دریایی بریتانیا:
ارتش آمریکا در ۴۸ ساعت گذشته ۴۲ ترانزیت از تنگه هرمز را تسهیل کرده است
🔴
فعالیت‌های سپاه پاسداران در تنگه هرمز طی ۴۸ ساعت گذشته ادامه داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/141215" target="_blank">📅 22:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141214">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">فرهنگ لغت جدید
دزد = تراستی
رابطه نامشروع = امر به معروف
موشک / بمب سنگرشکن = پرتابه
کمبود = ناترازی
تبعیض و پارتی‌بازی = برخورد مؤمنانه
اعتراض = اغتشاش
انتقاد = تبلیغ علیه نظام
روشنفکر = غربگرا
رفراندوم = تجمع خودی‌ها
طرفدار صلح = باسن‌لیس ترامپ
شلیک به هواپیمای مسافربری = خطای انسانی
قتل‌های زنجیره‌ای = نیروهای خودسر
اصلاح قیمت = گران‌کردن خارج از برنامه
مجازات نکردن خودی‌ها = برخورد مؤمنانه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/141214" target="_blank">📅 22:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141213">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭕️
⭕️
بخاطر افزایش قیمت دلار تا 200 هزار تومان  هدیه ما به شما عزیزان به مدت 15 دقیقه کانال vip  دلار و ارز را رایگان کردیم. بعد از 15 دقیقه اگه عضو نشدید باید با پرداخت 10 میلیون تومان اشتراک بگیرید.
👇
👇
👇
https://t.me/+t2df2MwRSAIyMWM8
https://t.me/+t2df2MwRSAIyMWM8
شانس کسایی ک انلاینن
☝️</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/141213" target="_blank">📅 22:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141212">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل در خبری اعلام کرد که مشاور حقوقی کابینه اسرائیل قصد دارد علیه مشاوران نزدیک بنیامین نتانیاهو در پرونده جنجالی «قطر گیت» اعلام جرم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/141212" target="_blank">📅 22:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141211">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hs-wchiubZHFccG2aB9it4-_mFxOkz7hZf7wbft0Nud2SZwpdyVKjrv6zx4yOY6EEH_-9zXXsrp2SDd17bfXTWL1Use5q7iqVSReOPl1WKwZg7c-KMo4aEWi1wz_p4bqVKmazfN4bdvj9d6KYEQ0-5f7fqwPP50EoKEg4mLUNYeeqevObFzmeeRwGKem6OEAa8pb2JiiixqaprcpPcjf5Wjrv2goUZ176mA5QqJfdanKmEypzP8y4-jOTP8wflDKCI0v_sdF1Ms-NCxMopmpceZsAFNDhD-IDcIqsps12loOeuETu4FhfplUz-xqMKySxHIVHUFe2vwgR6gCZW-mWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس انفجار در بنی حیان، جنوب لبنان تحت کنترل ارتش اسرائیل (IDF)، که احتمالاً ناشی از عملیات تخریبی ارتش اسرائیل است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/141211" target="_blank">📅 21:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141210">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
شبکه ۱۲ خبری اسرائیل: گزارش‌هایی مبنی بر وقوع انفجار در منطقه سیریک، در جنوب ایران، منتشر شده است؛ احتمالاً موشک‌هایی به سمت تنگه هرمز شلیک شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/141210" target="_blank">📅 21:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141209">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سخنگوی سپاه: درصورت وقوع مجدد تهدید علیه ایران، صدها هزار مایل خطوط انتقال انرژی، هزاران نیروگاه، همه سامانه‌های آمریکایی و غیر آمریکایی و حتی زیرساخت‌های جهانی متصل به اینترنت در معرض تهدید قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/141209" target="_blank">📅 21:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141208">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
صرافی نوبیتکس دقایقی هست کلا قطعه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/141208" target="_blank">📅 21:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141207">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbLrWo15zUxEYhc340I2N2h436G--4TqSihrxjIsQ-7AcDS_cTDL4I04aLv8uIHNx7MD49wQanJ4MhQ3g2VXQsoP7oj0fn56pTKpCMNcBRNKgv9PTGFIpZ8-F0gBSYQauwTY-CR6VtqpIU2-ccDcQiBLpfDItXr6phrnF-3GDFlHud0JjotJ05EN6zkkIoGC6WUm1CveaKPANhAU3y_eVtj8tUei3e8fc7dUaYzaS12Eu7CmES4txXTNjyFztU8-lIqyreYRUKASQBF_urBkChRQ7LPVOCZtTWpU2mmU484b_dvPLMmiE8RlSPv5812Rkt0OV1JrCFF1FhWBX4l65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال بازگشت تردد دریایی در تنگه هرمز به حالت نرمال تا پایان سال میلادی از نگاه پلی مارکت دقیقا ۵۰ درصد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/141207" target="_blank">📅 21:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141206">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / یمن اعلام کرد یک کشتی حامل تجهیزات نظامی عربستان سعودی را در باب المندب هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/141206" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141205">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
باراک بتش خبرنگار i24news: گزارش‌هایی مبنی بر وقوع انفجارهایی در جنوب ایران منتشر شده است. به گفته منابعی که با سپاه پاسداران مرتبط هستند، این انفجارها ناشی از شلیک موشک‌ها به سمت تنگه هرمز بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/141205" target="_blank">📅 21:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141204">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
هم اکنون حملات سنگین به جنوب لبنان در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/141204" target="_blank">📅 21:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141203">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ef63b346.mp4?token=fwGj9Ul1Qos-JJHUZR_znVb4Npogz4tVAoWOZ8KwqHSgxdDaPNyF6BJLxhIH9FjooLoxWKg73ylUm1DmlOZWSk7bk-U4fn-Nz11obPsM9xAkn03H3buGIDWNR-LDtxXDwzxLPlBUy8wkb7z2l4sMugx_0Ytp03YdUjJYyoSx47yKqn0AJm4vHEPHf_dD7kHXRtO94uEem_jj9B0JW-YdhhScGceCOEreYPTp-rcjcWsafdVd13x0L2OZAh9w8LgTxRpUi98GYzYUwdqBHGK22tRK7KuGK7Uuwhm5hGb7CRLx25iFMEccJK__e4ewhPDCuHAmU8zBL4PXo-gekOryGmcmCXgmsKDp1aXxMx4XHJ7SxFOIrEeLO0q53t7vb9UwHKC50eufxI2vVetYkfKTQCQzwSg_9giofryt8kfRdKSYj-H8J0EdngK8IX_tmXBP-gQdds4hDUZACrMB9ECYgAXsJTSjqACCrK2tbQ-drCu1dkL8tgGapx6Kop0CK9V0S6Z8-ne4Y5M0RCgal8PNVXoea7FG0ZQLv9lgKBeFaQGizyycfGzoIkiVVKHG2xqMmrkkpRefSNRQP6rLLaP46hTggmSTbvJqSym6GSKhwvm6vHTtxLG7kBWS26p7fQ4encl6dII-_43QfC-YDi_BUCRDSAIN-lg1pMTBUT1b_QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ef63b346.mp4?token=fwGj9Ul1Qos-JJHUZR_znVb4Npogz4tVAoWOZ8KwqHSgxdDaPNyF6BJLxhIH9FjooLoxWKg73ylUm1DmlOZWSk7bk-U4fn-Nz11obPsM9xAkn03H3buGIDWNR-LDtxXDwzxLPlBUy8wkb7z2l4sMugx_0Ytp03YdUjJYyoSx47yKqn0AJm4vHEPHf_dD7kHXRtO94uEem_jj9B0JW-YdhhScGceCOEreYPTp-rcjcWsafdVd13x0L2OZAh9w8LgTxRpUi98GYzYUwdqBHGK22tRK7KuGK7Uuwhm5hGb7CRLx25iFMEccJK__e4ewhPDCuHAmU8zBL4PXo-gekOryGmcmCXgmsKDp1aXxMx4XHJ7SxFOIrEeLO0q53t7vb9UwHKC50eufxI2vVetYkfKTQCQzwSg_9giofryt8kfRdKSYj-H8J0EdngK8IX_tmXBP-gQdds4hDUZACrMB9ECYgAXsJTSjqACCrK2tbQ-drCu1dkL8tgGapx6Kop0CK9V0S6Z8-ne4Y5M0RCgal8PNVXoea7FG0ZQLv9lgKBeFaQGizyycfGzoIkiVVKHG2xqMmrkkpRefSNRQP6rLLaP46hTggmSTbvJqSym6GSKhwvm6vHTtxLG7kBWS26p7fQ4encl6dII-_43QfC-YDi_BUCRDSAIN-lg1pMTBUT1b_QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار محبی
:
سرعت افول آمریکا بسیار زیاد است
🔴
آمریکا در همه اهداف خود، از جابجایی نظام تا چپاول ثروت‌ها شکست خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/141203" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141202">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
پرواز های فرودگاه هانوفر آلمان به علت مشاهده پهپاد های ناشناس بر فراز این فرودگاه به طور موقت لغو شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141202" target="_blank">📅 21:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141201">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8p-5i1KZNmo0-lVskcEfZhEpb3H2gCMB4zvJUtd2TQdaKzEJpaCNeSXw3fWjB-TIgYN5NpFkcDgPUYOi4dzt2PM0VOp1HLIrGImco4vmI75zq8tj0k1xvkFEj7grFu_DAxfTBkvTdpVYAbyziYkxEeQqWhn1yJxMerSa9LB2uNDrELWdYSv-tizE-1UTzmfWBZYm9kkolNGussNO3J_ck9_He4FiH9NbZDl9AouvC4Eeqxp45oePNfOeYgPTvz333M3e9PoTZLTC7YjtT4CjidpSSTIDKjMhVzhX7fMWrxSwSzfO-ZDj8Kc-K-VjzA6jFCFcVipWug6YGcbzOmFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرنگار الجزیره: یک موشک ضد کشتی از شهر سیریک ایران شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/141201" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141200">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de77474c70.mp4?token=CxvzdCuRz00gUYYEc8uag2aTYbyun7FkTFu5JqBPY__1UojvxoiWI0oEjPqGxwXTXz0RN3T-StDs5dZzOH-Ydnx9LHQWjRVwXjN56JJpD_5udfEiOq3GtMKvPKpzEjiV0zYErJaYsdPnMWZ4REcnq3dkfE2KN7DNb_NnNZ5HcfkSaEw0I8sLlpZbZJkKoObFrWkFKyWOZMhSVNaoIWG2w7uCG5S3DwLpcfraT4r-1MTHFncfUjXus7waadahm_TA9--NSFc94lGGwTvUqXSENSfjF9DPuR6T1jCrUmapDxFW5eUgUp2j97MWv_FHkoiC5LeH3E1MTvlv6HDt7reQQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de77474c70.mp4?token=CxvzdCuRz00gUYYEc8uag2aTYbyun7FkTFu5JqBPY__1UojvxoiWI0oEjPqGxwXTXz0RN3T-StDs5dZzOH-Ydnx9LHQWjRVwXjN56JJpD_5udfEiOq3GtMKvPKpzEjiV0zYErJaYsdPnMWZ4REcnq3dkfE2KN7DNb_NnNZ5HcfkSaEw0I8sLlpZbZJkKoObFrWkFKyWOZMhSVNaoIWG2w7uCG5S3DwLpcfraT4r-1MTHFncfUjXus7waadahm_TA9--NSFc94lGGwTvUqXSENSfjF9DPuR6T1jCrUmapDxFW5eUgUp2j97MWv_FHkoiC5LeH3E1MTvlv6HDt7reQQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی گسترده در درپالایشگاه نفت الزاویه در پی حمله پهپادی ناشناس!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/141200" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141199">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
هم اکنون/ دیدار وزیر کشور پاکستان با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/141199" target="_blank">📅 21:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141198">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea51341f01.mp4?token=JxvTaYVPdL4FO9txAuJnIPfaD6CUnBaKkOr32PrEyN3AFykjGlFx15U1nxK37PZpVy8ZsJapIc8ZNzmJjRX_vjLiEc4QP93p_0D1rQSjisdEikVhjaMem_ApZh33dx2BjBZtfHEzyGWG5ntggkOZe1gy_rD3MYbpcVNbKsPsZNVVmjF5eZxMC4xj-Xl6pb6CPse4xBjC7wZzisS6I5RYpdOGooA1_iW1RXm-CiPCrUxwt_-TFnLITHMNVbLRrjDjoGBaKepTz1KvUJk3p4okgYO7YIk02JLmW79B9qeq6RP4fePoMrP4OfLgE6twIzb_gBMQX---9ONvtP2sEvus4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea51341f01.mp4?token=JxvTaYVPdL4FO9txAuJnIPfaD6CUnBaKkOr32PrEyN3AFykjGlFx15U1nxK37PZpVy8ZsJapIc8ZNzmJjRX_vjLiEc4QP93p_0D1rQSjisdEikVhjaMem_ApZh33dx2BjBZtfHEzyGWG5ntggkOZe1gy_rD3MYbpcVNbKsPsZNVVmjF5eZxMC4xj-Xl6pb6CPse4xBjC7wZzisS6I5RYpdOGooA1_iW1RXm-CiPCrUxwt_-TFnLITHMNVbLRrjDjoGBaKepTz1KvUJk3p4okgYO7YIk02JLmW79B9qeq6RP4fePoMrP4OfLgE6twIzb_gBMQX---9ONvtP2sEvus4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه خلع سلاح گروگانیگر خیابان ولیعصر توسط پلیس نوپو
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/141198" target="_blank">📅 20:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141197">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf_nWPA7nkWHCr96U5v-qeMXX7UMrpyksKRHeh7rM3GNqyUM1Xee8w7mkpXqvJHCENmeGHR_yr5INaxgxb5y4uhmYq54k08IoNDCddHBMRuIRsFyVGI1O_SHI3EJEfDqfCgVNMtyW2DDZ1ny03_5dGLCJ0mqKEleDzMQNI_sXY0V6coRoexB6nCpjckDCIb5U1WD9XxLaq2NiCobW1Uys18bjIvFCsNXf7vesDf-6ZvpiiCo8pYhvep3wCowW2slfv2mBWRGeLODWKFE3s8dDJQrpbIt_PXxML2PfbAlgw0g1YjGXx_y0zziwH-t9ftxwBTqe_nMz4RVCYj3L3Z5ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میا خلیفه بازیگر محبوب هالیوود: تا آخر پشتیبان فلسطین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/141197" target="_blank">📅 20:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141196">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd248</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/141196" target="_blank">📅 20:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141195">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری / وقوع دو انفجار پیاپی در مأرب یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/141195" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141194">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
محسن رضایی: تا وقتی تو غزه و لبنان آتش بس نشه ، تنگه تنگ میمونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/141194" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141193">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
کوهن، رئیس سابق موساد : مأمورهای موساد برای اینکه بهتر بفهمن تأسیسات هسته‌ای فردو چطوریه
🔴
چندین بار از این سایت بازدید یا اونو بررسی کرده بودند
🔴
اینکه آمریکا فردو رو بمباران کرد، تحقق همه آرزوهای من بود
🔴
اورانیوم ۶۰ درصد غنی‌شده ایران هم هنوز با ساخت بمب هسته‌ای فاصله داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/141193" target="_blank">📅 20:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141192">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: سلاح و جنگنده به اروپا می‌فروشیم و آن‌ها در ارسال به اوکراین آزادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/141192" target="_blank">📅 20:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141191">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ: ما بر پول ایران کنترل داریم و کنترل کاملی بر آن اعمال می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/141191" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141190">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
میدل ایست آی: ترکیه معتقد است که گزارش اطلاعاتی اسرائیل در مورد طرح ترور ترامپ توسط ایران، یک عملیات فریب برای نابودی مذاکرات بوده
🔴
تل‌آویو گفته بود تهران با دوش پرتاب می‌خواسته هواپیمای ترامپ را در ترکیه هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/141190" target="_blank">📅 20:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141189">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
رسایی: چونکه نمیدانیم اسرائیل کِی حمله میکند مجبوریم جلسات مجلس را مجازی کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/141189" target="_blank">📅 20:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141188">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=e6qAf-UUi0BPs1UzrXUDe4Tjz0tgF92guW7BITI3O7cBNfu_KvOFTNcafGCDQOMPy8L78NmzZWEtpG76TUbv11pE14jgN9tKjEcX6e38iXREQK-B_URzNrs7atZ2RDixOowX0hXPU46i2F8OmAbFTmgRTRyrfsxN-iAABohHSw6D3lxnxZwNI9E8fq8PGmWOJ8dtL6BKw0RzxuoipJWWllrwTuZa7ouS31I9VutEVjfFpeID9GBM0DrEE7yuoZMRy_X3vVLwvctHHQlBVa7iiPnX8NStnAd3gawJWuQvyXKBuMYY-RhdcvVQsjr1D0FB1rBJqwMO06G722r3tqm3WW1oyIEPveo0reRkwGN9eOp2JO0fK8fz9wPwgw50cSTJWciMljzbQ-2wOHsfpxAswiyRStlde-cwLfNgD1vG4pV3epM3nY0Q3S02omVCubeYl_nXAsIZDEfz7TriLnARkrPtG1xZe-UPOurGEbVxhmsso7yTuzwzsE3NV_LR5lB40yJc9LZG03TVjGjVEVQCPh6AwigtycUI_GBPNMWWlBCVTGxXu312TyKBDjfB0-iXRASABc5hI_76Ztoad0NtIgK7RSiFpe0e9V4dB2gFwVGIIF6taa_tUCpDujESuLODhOO0ATR_ELcwPiWJJZRf_I1uq7cD1vGilcVY7qKwegQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=e6qAf-UUi0BPs1UzrXUDe4Tjz0tgF92guW7BITI3O7cBNfu_KvOFTNcafGCDQOMPy8L78NmzZWEtpG76TUbv11pE14jgN9tKjEcX6e38iXREQK-B_URzNrs7atZ2RDixOowX0hXPU46i2F8OmAbFTmgRTRyrfsxN-iAABohHSw6D3lxnxZwNI9E8fq8PGmWOJ8dtL6BKw0RzxuoipJWWllrwTuZa7ouS31I9VutEVjfFpeID9GBM0DrEE7yuoZMRy_X3vVLwvctHHQlBVa7iiPnX8NStnAd3gawJWuQvyXKBuMYY-RhdcvVQsjr1D0FB1rBJqwMO06G722r3tqm3WW1oyIEPveo0reRkwGN9eOp2JO0fK8fz9wPwgw50cSTJWciMljzbQ-2wOHsfpxAswiyRStlde-cwLfNgD1vG4pV3epM3nY0Q3S02omVCubeYl_nXAsIZDEfz7TriLnARkrPtG1xZe-UPOurGEbVxhmsso7yTuzwzsE3NV_LR5lB40yJc9LZG03TVjGjVEVQCPh6AwigtycUI_GBPNMWWlBCVTGxXu312TyKBDjfB0-iXRASABc5hI_76Ztoad0NtIgK7RSiFpe0e9V4dB2gFwVGIIF6taa_tUCpDujESuLODhOO0ATR_ELcwPiWJJZRf_I1uq7cD1vGilcVY7qKwegQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/141188" target="_blank">📅 20:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141187">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: روز یکشنبه ۲۰ میلیون بشکه نفت از خلیج فارس خارج شد که بالاتر از میانگین قبل از شروع درگیری است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141187" target="_blank">📅 20:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141186">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0160411b7b.mp4?token=QhldUZS83IDmxkQfgPufNeWg4nvdHDxxipqiTz7kPdN1tUTsc2yp5qg55L6c-hU7jxJa47bTQdvNJUTR9iq-wd7ygRwmJ12aSTu9OJvIzFZQUN_DEULo7ZLYQU2GA0CXP-fRKjlF_1yH4RPfgAGjN9f3A1CYHF9yz7qaR1qLhYuNtTyXZYu3wrFA3dJSdWFIJ8T26QENz6dDDPFgiV9sR0ojblXjdHneKAGuoqtLsOn4mv1jqCjlzYvtpNQgJqENNtmTLkEDfQcTgCEvo4cKbTCyis2QeZnTKA1HSG_v1xe124H6zBB5QO_mPe22mZ4uAQRsyhaAB2neIPtLudeWcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0160411b7b.mp4?token=QhldUZS83IDmxkQfgPufNeWg4nvdHDxxipqiTz7kPdN1tUTsc2yp5qg55L6c-hU7jxJa47bTQdvNJUTR9iq-wd7ygRwmJ12aSTu9OJvIzFZQUN_DEULo7ZLYQU2GA0CXP-fRKjlF_1yH4RPfgAGjN9f3A1CYHF9yz7qaR1qLhYuNtTyXZYu3wrFA3dJSdWFIJ8T26QENz6dDDPFgiV9sR0ojblXjdHneKAGuoqtLsOn4mv1jqCjlzYvtpNQgJqENNtmTLkEDfQcTgCEvo4cKbTCyis2QeZnTKA1HSG_v1xe124H6zBB5QO_mPe22mZ4uAQRsyhaAB2neIPtLudeWcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد اعتراض مردم فوجیساوا ژاپن به ساخت مسجد تو این شهر،دولت ژاپن اعلام کرد اسلام تو ژاپن جایی نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/141186" target="_blank">📅 19:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141185">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سی‌ان‌ان: کاهش ذخایر موشک‌های رهگیر آمریکا، نگرانی تازه کشورهای عربی خلیج فارس شده است؛ آنها نگران‌اند در صورت تشدید جنگ با ایران، توان پدافندی آمریکا برای مقابله با حملات احتمالی کاهش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/141185" target="_blank">📅 19:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141184">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
اسرائیل و ونزوئلا روابط کنسولی خود را از سر گرفتند
🔴
اسرائیل و ونزوئلا در سال ۲۰۰۹ میلادی روابط دیپلماتیک خود را قطع کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/141184" target="_blank">📅 19:51 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
