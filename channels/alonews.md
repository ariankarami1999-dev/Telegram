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
<img src="https://cdn4.telesco.pe/file/IhvyOaqUacOi1_M3f_487NVX9KJCyfcXHPI3fho1Hw93Em7lMDlKgYpBoSxp89C0m9LPi82cTTyaxXey7gY9GrWvahBtJoy8mDUBd2yx8E4_1ZtqQ3fW8rh64eC4SOcjFgPkU1eVPZnm_EGoXMkwMgokZRTEzjxWYhIclf5QLAkuSOC00Ob5t0b73fS5lKcNYrqJBwDI8jWhR63hd0ovL2yryW8CObHqhuIS4W3M9Z_TbLzgTQr-DStuA9QXQNkGxVWhMQAKw3Rmv7Hq4kff1jm3KtelyHkGyew2pMJHeqI_yB2FXh3lC5uJqZVmKE6G2TlAuttLJKAF6cqABbrN9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 929K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 14:04:32</div>
<hr>

<div class="tg-post" id="msg-123024">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4d523ec4.mp4?token=XDIHFHM788nNVLZpq1XRMzkFv40vcxrM9TvrbovsxSxm6uuUGZxK7Ys3xE1RtMgj77fy3ETxzogo-2zkjSxs-_N5x9rfkC5bF-s16zM10ogDnznazbgmY5WY4acejKl1gfC36V23ejVmVFvo_44bujpThJpgsb8m2ufBiClMGanVAABCyfUTOO0KrGJqo_tKJiukGES0rPYys1lyVychmfSqG-40rQLDNu63rq-sQzjBp69N-S0JqgkXEo5CBCCy7Z4olUsgnPPHksB-yFAzx_hW89kJ5FFr0hkbbsGbAqpETvjMFmxNo69rRDsxotcycfvZuDD3TtsWJwT46t7ttg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4d523ec4.mp4?token=XDIHFHM788nNVLZpq1XRMzkFv40vcxrM9TvrbovsxSxm6uuUGZxK7Ys3xE1RtMgj77fy3ETxzogo-2zkjSxs-_N5x9rfkC5bF-s16zM10ogDnznazbgmY5WY4acejKl1gfC36V23ejVmVFvo_44bujpThJpgsb8m2ufBiClMGanVAABCyfUTOO0KrGJqo_tKJiukGES0rPYys1lyVychmfSqG-40rQLDNu63rq-sQzjBp69N-S0JqgkXEo5CBCCy7Z4olUsgnPPHksB-yFAzx_hW89kJ5FFr0hkbbsGbAqpETvjMFmxNo69rRDsxotcycfvZuDD3TtsWJwT46t7ttg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
70 میلیارد نخ سیگار در طول یک سال در کشور مصرف می‌شود
...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/alonews/123024" target="_blank">📅 14:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123023">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GZc8-Hyodji2MTykAzXnkH2wWQQGq7X1oyCmCufaQphs39O3HLssfTs5ItPkLFyllAxbAqkhVS9oY35tyNDfOu1jqMDlZmxH2U7tCyhARKfMX9vXEktVenqYF0TeBKT94e78q7JpnpcxV_IhhD-RMrnWXJRBZUSSdChJvYHy7PrPhnr4JSS-T9bemc7B68o47yNk4RvH5w_p_2os0qlbI93ZU8Qhqk9o_pZBPMlukdvgFlH4tN-VEXEt0HLw9obf6Baj3QCFyTT-SDA4k11gWM-eWK_9y-NxGG_MQ2X5nizG-GCHIOv5zZepQ_BM74HVneczdTUlCNoQooa6-8Lc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همراه اول امروز در پیامی به کاربران اینترنت پرو اعلام کرد در صورت تمایل می‌توانید اینترنت خود را به حالت قبل برگردانید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123023" target="_blank">📅 13:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123022">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCZg8BT4o7j23sfXjPVgRoaQK_TTrqh6Vftx6pZCC5UZ-tTv9c2d0reOZmYNW358rRWyhYzayIqsTEDd8Xlc9gMN6QDvMfeyABMehx_dl3ZASuWwzX1-tbUOxJxOsWb8VVwtzewGX_hP3pTJAXzb4P2wYJzFetX4z0DIHebMle4QQHOPmDpsybFxS2pGpqoUBRB3xEAz9ozPdUZxOovu-yUNpoNss8v-oeTnpZMkddUuqYdn3EvBr9nsPLMcxTO4jUS6pHLzytNVlOAdOubmXJjthhaHpV9qo-10bu9OcGqzG8_5rxpmAFbJaSmoMpI0GWIy7IOUdzPUBXcSqXwe5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده در حال کاهش حجم نیروهایی است که برای اعزام به اروپا در مواقع بحران برنامه‌ریزی کرده بود؛ این اقدام، گام جدیدی از سوی دولت ترامپ در راستای کاهش حمایت‌های نظامی خود از متحدان ناتو محسوب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123022" target="_blank">📅 13:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123021">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رسانه I24 NEWS: نیروهای دفاعی اسرائیل (IDF) و فرماندهی مرکزی ارتش آمریکا (سنتکام) در حالت آماده‌باش بالا باقی مانده‌اند، در شرایطی که احتمال شکست مذاکرات میان واشنگتن و تهران و صدور دستور اقدام نظامی از سوی رئیس‌جمهور دونالد ترامپ وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123021" target="_blank">📅 13:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123020">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maLklGh-qeJeMb1i1mT0W42eUUE-ZHDvQDenCTHPquT1zRFvqh1nxKpBr2xscXfaB8SG8VpQPLx8ZFgsaiDheEfBc4eWfTdX2XafWWh-mkCsTA5wwAFfMU_Dz2byruDBmX-1yMIkdlPxwFEZ0yjx7ZOrk3a0wx444_pvn-HqDjHsJ2EeL7fmamwubzu8WJFr4Y7Sj5ydjaNMJJZ-ZeCNTvZgh44LzFW1QbCN2PSog5wiRKN2tohXA_nhAubYoAZz4TlDsfLbrOWEHTSOPewabHHKisxXYi_VL1bZhtdTQzv-zjR0VoByYLEz118M9UDQ6aC6h7CMfqbAPuI0vj93sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با تصاویر ماهواره‌ای سنتینل-۲ ناو آبی‌خاکی تریپولی آمریکا رو تو دریای عرب دیده شده
🔴
الانم با اسکورت یه ناوشکن داره حرکت می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/123020" target="_blank">📅 13:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123019">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
پارلمان مجارستان امروز قانونی را تصویب کرد که عضویت این کشور در دادگاه کیفری بین‌المللی را حفظ می‌کند، و بدین ترتیب تصمیم دولت سابق اوربان در سال ۲۰۲۵ برای خروج از این دادگاه را معکوس کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123019" target="_blank">📅 13:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123018">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نتانیاهو دیشب در جلسه کابینه: محدودیتی برای حملات در بیروت نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/123018" target="_blank">📅 13:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123017">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
امتحانات پایه‌های هفتم تا دهم به صورت غیرحضوری و از طریق سامانه جدید شاد برگزار می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/123017" target="_blank">📅 13:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123016">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fda00612.mp4?token=kKYtw8vvpQEeUVWpXlYxWXDSLWDUl7_hFkEQook-A3o7lNzHeu6G57gLVWUUADw1rzoO1sKSpU_oZubnEVLMJNUR2CF7BjY3Cj0z4_P6Av5We4Us1GcdKVX1aY9u10unhjRe4qq-QsdLy-x6eUCgQxshfmUzdkTDeHTzRCSaFB-pS69NepD0_kEGgUQpoJBH6FWQK_BQLMxR1M2PgaV5cUwV3_-kacdttTNuIA44szL4RGEbtApEu7QiEO2ztHxIQv_x4G5d_Hjea9xwEB8FFTFtls194WPi_kO47OETSnd-GDIq_B_MLtYCN0k5EQSofRr2ZgVIQ2PEz_8DVG0VDSS7LNUmos3p6pd8vJ47ftV6149P5KukOOi0aXYJt2MzswQIW4k8Y0TBXrBxw3QwlrvflkRjg2nMcn3bTA42zr-bKRbPkq698uuAZ2sONFrCRLpOl_HxwwK-RUrRHNFzRPwYPcHNed9OCPaaKOF42O0GqLDSI5XWrBfoqQRul6XrD4nlfXsoW3ethoadgeHcuq53bByIKGpO8AUDnJZOqj1xsO5ey0uQ8ExmSgW5uTHI8OCOTPNQs3QKOnZfd5CivofBR1wdEJ2os26mBQMbBKWcaSuN7SoZSsFeSbR5NK6hcoXGnRR37mFmd0ebZ5fth3_KGLL675e5fyxHB_IzXN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fda00612.mp4?token=kKYtw8vvpQEeUVWpXlYxWXDSLWDUl7_hFkEQook-A3o7lNzHeu6G57gLVWUUADw1rzoO1sKSpU_oZubnEVLMJNUR2CF7BjY3Cj0z4_P6Av5We4Us1GcdKVX1aY9u10unhjRe4qq-QsdLy-x6eUCgQxshfmUzdkTDeHTzRCSaFB-pS69NepD0_kEGgUQpoJBH6FWQK_BQLMxR1M2PgaV5cUwV3_-kacdttTNuIA44szL4RGEbtApEu7QiEO2ztHxIQv_x4G5d_Hjea9xwEB8FFTFtls194WPi_kO47OETSnd-GDIq_B_MLtYCN0k5EQSofRr2ZgVIQ2PEz_8DVG0VDSS7LNUmos3p6pd8vJ47ftV6149P5KukOOi0aXYJt2MzswQIW4k8Y0TBXrBxw3QwlrvflkRjg2nMcn3bTA42zr-bKRbPkq698uuAZ2sONFrCRLpOl_HxwwK-RUrRHNFzRPwYPcHNed9OCPaaKOF42O0GqLDSI5XWrBfoqQRul6XrD4nlfXsoW3ethoadgeHcuq53bByIKGpO8AUDnJZOqj1xsO5ey0uQ8ExmSgW5uTHI8OCOTPNQs3QKOnZfd5CivofBR1wdEJ2os26mBQMbBKWcaSuN7SoZSsFeSbR5NK6hcoXGnRR37mFmd0ebZ5fth3_KGLL675e5fyxHB_IzXN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان: ان‌شاءالله این دیکتاتور به نام نتانیاهو، درسی که شایسته‌اش است را از مسلمانان جهان خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/123016" target="_blank">📅 13:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123015">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ecf0a6d3.mp4?token=J12B5weDUUfo9bVKTC3_m_YJk-UeCdjkHlhXuRztffODp8VqKopWb1LTR50e5MmvilthapDjLeqhyM7qUf58GmML3RHhTvMO3AipXl4S283sERZny0TbdWdwr2YGw7WV1cLfBU5klza-LruksoXjGEpD-o2CVCBvGSAHMyTbp4tAsptte8hFXf0suB-MG4lsl9RCOLiBFd3jQSU8ovCmxw1I3EenGVPi-4UwmC_aCsyTwYuySY1NIjS34f9lL28a1Fq1EIVZhwuUdf4PnzGASj_nHUhTJRpbm1-h4oNzNk40l0WH9e_jnYt76UUkcLutgVEtqJUfIdZFz1H3X44cfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ecf0a6d3.mp4?token=J12B5weDUUfo9bVKTC3_m_YJk-UeCdjkHlhXuRztffODp8VqKopWb1LTR50e5MmvilthapDjLeqhyM7qUf58GmML3RHhTvMO3AipXl4S283sERZny0TbdWdwr2YGw7WV1cLfBU5klza-LruksoXjGEpD-o2CVCBvGSAHMyTbp4tAsptte8hFXf0suB-MG4lsl9RCOLiBFd3jQSU8ovCmxw1I3EenGVPi-4UwmC_aCsyTwYuySY1NIjS34f9lL28a1Fq1EIVZhwuUdf4PnzGASj_nHUhTJRpbm1-h4oNzNk40l0WH9e_jnYt76UUkcLutgVEtqJUfIdZFz1H3X44cfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه هدف قرار گرفتن انبار تسلیحاتی پایگاه شکاری دزفول در ایام جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123015" target="_blank">📅 13:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123014">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqbwHtRwKjMkKvfS9Z4CwAZhILGy3XjrV1hpEb6R0lqgeKTHc41jk1MrK6apus0yDoSdVfv0NvJ9uEpZw2PLvIEvguvXNOiwCPXhpQkglBIG467a-Cph93doCe3iVFOWl3JbiPSaAwtAW4uIa6ZP5eXi1L9HuRRSPd6Q9AxTDh-oWNsWz_a2ox0W1TQC2_lgrgs-ryKO6hwuJMNWcTGQzYWqJVtHDCXJrQY27siPSpzlPMcx3z_s2skMc8h_W2EVf1_Uw7VL0BDUr_pW8nRpktyns2xSg9cqU7MjK2Bgf2S8T_6wYe0y9az3Y7oYZq_2KTJFWHJHpSj1mOyZNoTsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سالود کارباجال، نماینده کنگره با انتشار نظرسنجی مبنی بر اینکه ۷۷٪ آمریکایی‌ها معتقدند سیاست‌های ترامپ زندگی را گران‌تر کرده نوشت:
🔴
«مردم آمریکا به‌حق از این موضوع ناراضی‌اند که قیمت خواربار، بنزین و دیگر کالاهای ضروری به دلیل جنگ غیرقانونی ترامپ سر به فلک کشیده است. این دولت خانواده‌ها را زیر فشار گذاشته بدون اینکه پایانی برای آن در چشم باشد، و جمهوری‌خواهان هم دارند اجازه می‌دهند این اتفاق بیفتد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/123014" target="_blank">📅 13:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123013">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
معاون وزیر امور خارجه روسیه: ما آمادگی خود را برای انتقال اورانیوم غنی‌شده از ایران به واشنگتن اطلاع داده‌ایم و این پیشنهاد همچنان روی میز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/123013" target="_blank">📅 12:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123012">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
منبع آگاه نزدیک به تیم مذاکره کننده:
منابع بلوکه شده ایران که باید در طول مذاکرات آزاد شود، ۲۴ میلیارد دلار برآورد شده
🔴
ایران تاکید دارد که نصف این مبلغ باید با شروع اعلام یادداشت تفاهم در دسترس قرار گیرد و بقیه در طول ۶۰ روز منتقل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123012" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123011">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Phmf5INqbxdOQ2ryl0qYlb56vKySGomuoQSsN6DxETaKNkxAAcO3BkryXcW3_xI5BC7SlZ0Tn9Xqzeq0KYJegroMHnv64WdF6-RBZAJTqqokRmhbhw4OwgrUm4P_yEKOvwoSC0iNNZLYFazcWcBK_OajuJhEVC0hWe-GdcY_LxgsUn5n4A4bkY_-TXGJZkmzd9noc_p7KOP9vGsRV6ckredScbcaSjTdoJygmZ0so9SjLVNAoIq9l4wWPNYNN5lRai3J6vKJ9vmfP_3zMqrWsrkzrF1jFWMcLDhE28dfCrnuAnO25bKJ3ulUOBOntIJUZQzV3sBIFRsk_yWcmKbE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / منتسب به تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123011" target="_blank">📅 12:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123010">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
کانال ۱۲ عبری تهدید پهپادهای بمب‌گذاری شده خطرناک‌تر از آن است که «اسرائیل» تصور می‌کند، و راه‌حل‌های فعلی مانع فاجعه بعدی نخواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123010" target="_blank">📅 12:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123009">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است
🔴
ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123009" target="_blank">📅 12:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123008">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت امور خارجه کره جنوبی: احتمالاً یک موشک ایران اوایل این ماه یک کشتی باری کره را در تنگه هرمز هدف قرار داد.
🔴
ما سفیر ایران را احضار خواهیم کرد و خواستار اتخاذ اقدامات مسئولانه برای جلوگیری از تکرار این حمله خواهیم شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123008" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123007">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
یدیعوت آحارونوت: وتوی آمریکا مانع حمله ارتش اسرائیل به بیروت شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123007" target="_blank">📅 12:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123006">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4512e82014.mp4?token=bPfEsyDGuFVX1K_BYd26HKDNUC0n5zzSVR12XEouXFzsd08AeyTeqM0YLC-Ulx_ddP9fMD8VXn5aI9aa6RM8PIEPmWKt3RRUBAsUGqDH_w9IKOsefMAxZECOhg69nhzZ7AIdeMGurqGDCszGKAyXPDcqDpFvc0d2YklZWCVkrL1XidQJo8EdhUPu52C7YcfTyWEojViGsjmbQjGk2qTZvJ-2R8YTzz5fqMRnE08XHR7qwHMaM9E9g8Q08SHqREvVjFT8C2kA3T0PVOU3rbveydatNH_6qz5GAFWDM8eoRzgO2d-aoMH714Z0DcpS2ODHTHkDExtic7CDSppmZYAh5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4512e82014.mp4?token=bPfEsyDGuFVX1K_BYd26HKDNUC0n5zzSVR12XEouXFzsd08AeyTeqM0YLC-Ulx_ddP9fMD8VXn5aI9aa6RM8PIEPmWKt3RRUBAsUGqDH_w9IKOsefMAxZECOhg69nhzZ7AIdeMGurqGDCszGKAyXPDcqDpFvc0d2YklZWCVkrL1XidQJo8EdhUPu52C7YcfTyWEojViGsjmbQjGk2qTZvJ-2R8YTzz5fqMRnE08XHR7qwHMaM9E9g8Q08SHqREvVjFT8C2kA3T0PVOU3rbveydatNH_6qz5GAFWDM8eoRzgO2d-aoMH714Z0DcpS2ODHTHkDExtic7CDSppmZYAh5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زهران ممدانی، شهردار نیویورک، گفت مردم در سراسر آمریکا، از شرق تا غرب کشور، هر ماه با استرس پرداخت اجاره خانه زندگی می‌کنند و نمی‌دانند می‌توانند اجاره را بپردازند یا نه
🔴
او تأکید کرد: چشم‌انداز ما شهری است که مردم نه تنها توان پرداخت اجاره، بلکه رویای خانه‌دار شدن را هم داشته باشند.
🔴
ممدانی افزود: بیشتر صحبت‌های سیاست فدرال ربطی به نگرانی واقعی مردم ندارد؛ نگرانی واقعی مقرون‌به‌صرفه کردن شهر و ساختن مسکن قابل دسترس است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123006" target="_blank">📅 12:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123005">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
شبکه NBC News به نقل از معاون رئیس‌جمهور آمریکا: «من خوش‌بین هستم که ایران در هر توافقی، با عدم توسعه سلاح‌های هسته‌ای موافقت خواهد کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123005" target="_blank">📅 12:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123004">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
جی‌دی‌ونس در گفتگو با ان‌بی‌سی:
فکر می‌کنم پرسش دشوار این است که آیا ایران با سازوکار نظارتی و اجرایی‌ای موافقت می‌کند که به ما اطمینان دهد در آینده توافق را نقض نخواهند کرد یا نه؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123004" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123003">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی  همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN  @NetAazaadVPN</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/123003" target="_blank">📅 12:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123002">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hKDrNuf4HQW4azkEQ1oh8wF5QTCMv4ys3_v_Aq5ua5sJ7a_ZjH9-zq75NdciYwAK3RKB75_MQrI0TJuTwk0z1Cp9F79MVp0sAVufTAJAjQyiUa8GO_H065tvtuJkX1so7sHAlXhj0ndQkBAnNJ-Q73QopX-oU7SApMRIlD3K6H4XG5gMPumTnsm9mJyohUG1OEC8N65TjbIqXyVoKFeJAhYdxw3tgF25kQJ5cxxrQxE0FYfNmsi8zcKiZ1s57kkKPz5Dy_4W8HeYQoG8LbIj55wl3SpzPjOjPGZYv9-5kBHgyiR1Y_RBHt2ViLXPFubcQ9ozBiseX3Z5pV5rNTyDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی
همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN
@NetAazaadVPN</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/123002" target="_blank">📅 12:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123001">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: ارزیابی‌های اطلاعاتی حاکی از آن است که برنامه حمله به ایران از دستور کار خارج شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123001" target="_blank">📅 12:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123000">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ef47a108.mp4?token=TOPCgQ90Rjra2vzPG2COPCK92TnpPoIWNHjdVQzVarg9y_Cv28vEIqUfgmVLubfDg_ycXuPr6ih-Cb7bN6TKbiJ6_I0baKPJw2qqOdDUJv1J7rhCkMqOSVa9HKrHX2BnxjQwHHVpgWrYvS9IdrGgPy_nJXU9e-i6JTjSTuALTuHj7Edj6lJR9Lwndc522M2oH8bO6o-GKNZylT7bcNcAcXdMI9tFpBz0BD15uj-HkdTez7W23GAABiUQ1i3220zZ5luqexl6wDAPgZToMnSxR9FRToJdElXrZdnddiT1QpwVNtOb6ts11DmnZoyIL8XkjLNxr8jP53MSBbDZxc7xyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ef47a108.mp4?token=TOPCgQ90Rjra2vzPG2COPCK92TnpPoIWNHjdVQzVarg9y_Cv28vEIqUfgmVLubfDg_ycXuPr6ih-Cb7bN6TKbiJ6_I0baKPJw2qqOdDUJv1J7rhCkMqOSVa9HKrHX2BnxjQwHHVpgWrYvS9IdrGgPy_nJXU9e-i6JTjSTuALTuHj7Edj6lJR9Lwndc522M2oH8bO6o-GKNZylT7bcNcAcXdMI9tFpBz0BD15uj-HkdTez7W23GAABiUQ1i3220zZ5luqexl6wDAPgZToMnSxR9FRToJdElXrZdnddiT1QpwVNtOb6ts11DmnZoyIL8XkjLNxr8jP53MSBbDZxc7xyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور صربستان در سفر به چین، از یک کارخانه ساخت ربات‌های انسان‌نما بازدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123000" target="_blank">📅 12:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122999">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کره جنوبی: اعتقاد بر این است که حمله به یک کشتی کره جنوبی در تنگه هرمز در این ماه با موشک ایرانی انجام شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/122999" target="_blank">📅 12:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122998">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
جاده چالوس بازم شلوغ شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/122998" target="_blank">📅 11:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122997">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ریانووستی به نقل از معاون دبیر شورای عالی امنیت ملی ایران نوشت: ایران و ایالات متحده هنوز در مورد رفع انسداد تنگه هرمز به توافق نرسیده‌اند.
🔴
ایران و عمان در حال مذاکره درباره رویه جدید عبور کشتی‌ها از تنگه هرمز هستند.
🔴
تماس‌های غیرمستقیم میان ایران و آمریکا ادامه دارد.
🔴
ذخایر اورانیوم غنی‌شده ایران در دستور کار مذاکرات نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/122997" target="_blank">📅 11:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122996">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sb4HBEQ7vgwh4B8dpJz-81UT5ZPZVvRONBVprMJGQ84MF17Dm892jKBIY_yzlo0WYAESv1c_aEpdK_ZdeWnqytm6y5c_mgc6kI3uqLukZBy57_RdgRKLsPaI5lDldBviGyHyFgyn6Xsu41zEuMK8kDxYkcE2rUAdoGlcFFuS8AEmzC-0JepUQdroPfyj-YFuixPmbMpNW_F1BmuWVh3G3oxEIy0YQOIW6ZJdi7LYXBKTUqVJSu8dwxBhc-08gJyB-m_Z7qzwrHvpKhDFr6TcojYhY9fdwWHo4XBThFL0oq66mfUe2eV_3uGT40j_yX0mJi_vmFVzyvTmRjyj5ud6fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یزدی‌خواه، نایب رئیس کمیسیون مجلس:
مسئولای بالا به این نتیجه رسیدن که فعلاً اینترنتو کامل باز نکنن بهتره؛
مردمم خیلی با قطع اینترنت مشکل خاصی ندارن و فقط به یه سری قشرایی که لازم داشتن، اینترنت بین‌الملل دادن.
الانم کشور تو وضعیت حساسیه، نه جنگه نه صلح؛ واسه همینم بخاطر مسائل امنیتی فعلاً قرار نیست اینترنت آزاد واسه همه وصل بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/122996" target="_blank">📅 11:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122995">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
«مردم ایران از سلول انفرادی به بند عمومی منتقل شدند.»
🤔
اینترنت جهانی برنگشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/122995" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122994">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فارس: بیش از ۲۰۰ فروند کشتی در یک هفته گذشته از تنگه هرمز عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/122994" target="_blank">📅 11:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122993">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OI-rUjX7I46v1zr73YAzNgN3y9Z4az7VTFK4zLr13rRicQzS3D_xLxrQQgZlAEemFMSBAvU5KpwQvsB_u0EUxFXoNVrRldoRdz5lqAsF0RPd-mvdxBlr0VyA-GWsbRyFguu7QAxbuulAA8RspOHI7Ghnotm3A34dzex-j5VYLZ54WqdsouWXH7fAfzj9UaDMcEpJaRiuIYs3IkIlAucLJRRCIg5z9yt5A-wlUH8GKM92OQDN5VDK1bVM6U9S7yNdIfolMF3cNh2BwIBs2_k28i10PnX5ECSclIPp0oRhecW0LHWh1hhbePqHRhwH1QR3sE5S5aRdS7yI_iP598Ntag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید کاخ سفید، : مامویت سادست؛ صلح از طریق
قدرت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/122993" target="_blank">📅 11:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122992">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3d5d9df2.mp4?token=F0Yvd5KwdoHt-s4wrv96jjkeMaBBHtqUDxCTPu4ZhE9WpMT4fUCJ0p0f5esEFF07sbt0AQ7tkFX7fkmbOOQ2o6ZlTyKyw-SnqEyRlPjP1X8eOrceayptu-SDO_QSTcm6o6hExnE75twVVkzI5Tnw6D4Hu_SvyzP5gNjTdnb12pQeVW8W22UWrahkuPJN9A4NFi_sTDVQNabVK-SuaI6Z_0Ll92YRenar91XUagb5jFor6ASag65_keSFit-7d1Xgx7wuKjGPScMtb2A1yBp6ecZ0vl_7EsS30Obr1XbPyVQxVNPbRDubMe9NWRszrMAA7WoPAEe-QrKq4nkR0wPVBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3d5d9df2.mp4?token=F0Yvd5KwdoHt-s4wrv96jjkeMaBBHtqUDxCTPu4ZhE9WpMT4fUCJ0p0f5esEFF07sbt0AQ7tkFX7fkmbOOQ2o6ZlTyKyw-SnqEyRlPjP1X8eOrceayptu-SDO_QSTcm6o6hExnE75twVVkzI5Tnw6D4Hu_SvyzP5gNjTdnb12pQeVW8W22UWrahkuPJN9A4NFi_sTDVQNabVK-SuaI6Z_0Ll92YRenar91XUagb5jFor6ASag65_keSFit-7d1Xgx7wuKjGPScMtb2A1yBp6ecZ0vl_7EsS30Obr1XbPyVQxVNPbRDubMe9NWRszrMAA7WoPAEe-QrKq4nkR0wPVBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انهدام یک قایق توسط ارتش آمریکا در اقیانوس آرام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/122992" target="_blank">📅 11:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122991">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RIf8UxMS33SYIKJgX0Ipb3ggzWltexO1SqlRU3cCMEm9-4A8JmsHo-idnbrGadynoiidoENaPwhe9iFNIm1Wou0NiU_kktwhJx88ybbm2A-K9neDyfpOw7b0ZVfj-aNXmz_QjRAw_V_e5t-2VOvy5Q7h3qeo0Zc2h4pk9Hu3ebyBS-D0UOU0-FThnPI3-E4V60OX3wdjVe5Hid0O9iDwQYkOKD2fsaq77WyEk_jB04SxF06CiCztxMFHR-9_c_FxIPGt24a-HM3OXuHYJ4n5aqiEdSEYUQiIK7SjS-HbsgvBhjowREsi7hgWfY-iKEOu3RM7XmYrudcrak8fSOhZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع امنیتی به وال استریت ژورنال گفته‌اند که روسیه ممکن است به زودی تلاش کند در زمینه بحران با ترامپ انسجام ناتو را آزمایش کند
🔴
روسیه بزودی به یکی از کشورهای بالتیک یا جزایر سوئد و دانمارک حمله خواهد کرد
🔴
پوتین می‌خواهد فرمان یک بسیج عمومی صادر کند که برآورد این است که بسیج فقط برای جنگ در اوکراین از نظر او به منزله اعتراف به شکست تلقی خواهد شد پس قطعا حمله ایی در نزدیکی قطب شمال انجام خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/122991" target="_blank">📅 11:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122990">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رویترز ادعا کرد: وزارت جنگ آمریکا (پنتاگون) و شرکت اسپیس‌اِکس بر سر هزینه اجرای طرحی برای فراهم‌سازی دسترسی مستقیم کاربران ایرانی به اینترنت ماهواره‌ای استارلینک، بدون نیاز به تجهیزات زمینی، دچار اختلاف شده‌اند ولذا این پروژه متوقف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/122990" target="_blank">📅 11:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122989">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e84f6895e.mp4?token=Af1UjIuD5SfEXyriCghU1MgHnMlh8aVE9LubEx-BPEzRx1O_WHzaRgT88FyDpNWO9VVFmzgqY9i670RClknb2Kjrd9b0gOzD2ro7dhTkPkZ2ICOSW-GRSZUIyLCzgXe8_nRa7OrbRBV_Zqa3AiCm0YtmCcZ7T7Qq-UtJnwuxybYj4E-XzSd2zvxiuFr9Rm7tiBQE_u3w7YSKrWojG56iVBzF-jm0Od6OCxrmngaJ6XeqQo76755-XyefNAWsIRZHfNMUmvRQ0pDuoK6e-uqFASvUEhaQWwyt8b3WcVtmCqTio9oqpcFx5psiBOgGr2ZdyA7jDm3RTV_T-btjjstTsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e84f6895e.mp4?token=Af1UjIuD5SfEXyriCghU1MgHnMlh8aVE9LubEx-BPEzRx1O_WHzaRgT88FyDpNWO9VVFmzgqY9i670RClknb2Kjrd9b0gOzD2ro7dhTkPkZ2ICOSW-GRSZUIyLCzgXe8_nRa7OrbRBV_Zqa3AiCm0YtmCcZ7T7Qq-UtJnwuxybYj4E-XzSd2zvxiuFr9Rm7tiBQE_u3w7YSKrWojG56iVBzF-jm0Od6OCxrmngaJ6XeqQo76755-XyefNAWsIRZHfNMUmvRQ0pDuoK6e-uqFASvUEhaQWwyt8b3WcVtmCqTio9oqpcFx5psiBOgGr2ZdyA7jDm3RTV_T-btjjstTsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای که محمد عوده و فرماندهان شاخه نظامی حماس ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/122989" target="_blank">📅 11:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122988">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
در حالی که به‌روزرسانی فوری نرم‌افزارها پس از بازگشت اینترنت بین‌الملل به‌عنوان یک ضرورت امنیتی اعلام شده، شماری از کاربران از عدم امکان اتصال به گوگل‌پلی و مشکل در دریافت آپدیت اپلیکیشن‌ها خبر داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/122988" target="_blank">📅 11:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122987">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
یک مقام سپاه می‌گوید احتمال جنگ مجدد با ایالات متحده کم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/122987" target="_blank">📅 11:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122986">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS2sVVjtS3JSqAyQFqyQN14pJ_B4_p7KOsTvmReCYIORAqmEOzoM4BZ4ZM5XjpU9lwlQbXh2GWDvtX-g_wFFU_LgN6fIHL5vI6a9Lv56Cw18pAuCM7O-fzaeC6mZP8XX5qJmn5fLXFe4tJWBAJWdIMoVSzg1GoGzu55nb6kOg8A6woppJmM_CAilb9jImAuU089ZZ2M6BeAgGtqAKbvFpZSb9ntJcmiRfAQrDE2ud-4mNhe3TCQKfZ_qM5JK5Tnn9No-MzwlDzlAB__wIzmFZB3yIWRYmRH1SW7ajXzRLLdc-fsmdNaycjjdFigxt4PkDGsc6oWhuwVZHXFkEt7MSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از موافقت سپاه ، نفتکش متعلق به شرکت کاسکو، هوا لین وان، اکنون از تنگه هرمز عبور می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/122986" target="_blank">📅 11:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122985">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFtDtoOmcfsEW66CgEzx0BgDGLOyCsRiCQJrL4nt4nS47Ywo4s6eJFDlbwsX6XkRaJWW0_VATvCQLzMko1xUl9cOCxBArXr5nlLdbC8WjMgyTpstzU-WFCHZfnGQBx6DCF6f7WWF1U1BTB1q-MawvO4t7xxMTLroSj05RjMPsxtbWs3XHr6yfHqFweE83z8dY3q5GJOddLX9_C-6ujEOkwnuz84r-mJC7gnAVYDDFGRV2lAjgh3Zz_uQ_qAcGVep0Z62Tfrp-cr2jrGSSpD7rQ1UqyJmO4RoPA3aCipShBYJuASK-YhTNJkvPlgPdhFmXT4OnR9xRC1ztvCx-ek8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۷.۱۷ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/122985" target="_blank">📅 11:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122984">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رئیس اتحادیه صنف خواربارفروشان تهران: پاک کردن قیمت روی کالا تخلف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/122984" target="_blank">📅 11:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122982">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رویترز: پاکستان از میانجیگری عقب‌نشینی می‌کند در حالی که قطر به مرکز اصلی بین تهران و واشنگتن تبدیل می‌شود و تمرکز بر دارایی‌های مسدود شده ایران در دوحه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/122982" target="_blank">📅 11:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122981">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Jm8FzgV_d_q5vH5zdhE7VICUyv6hJf7eOor7vOoAXu9Fv0iGUHO4pomp4FlWjKPzhkc6fuxpAXh2kPXLs1pV-MmrHzNxhaXEb1bvqQJ9OTq8uFrOGia53xLHgDlCk21eS8W1Nt4W0PoLpId_c_2WCp9NSjegYb8uBf40vY1UraYgnTy8zO53fhQtJav_EzeXa4e7guj62LhbAz8KXgpdLApEGQ3vv19dTf4qzWqHMrG1KeLHQw9vX57eAL8UmX9EQY_CbWCXwiLi0f3G6x1FETludQSJ-eCMnp33WqYxdRXVd_h9hD7UVuDv7pKEudn4hzJhZPHqZzR_tIvVQ9IwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا الفت‌نسب، رییس اتحادیه کسب‌وکارهای اینترنتی ایران: اینترنت فقط چند اپلیکیشن نیست؛ زیرساخت کار، زندگی و امید میلیون‌ها نفر است.
🔴
ایستادگی در برابر فشارها برای
باز نگه داشتن ‎اینترنت، دفاع از اقتصاد مردم است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/122981" target="_blank">📅 10:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122980">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAXxiS2pNjzHEUzpVrW_63ysqDVxZl-ee_mKE4Dzin8Qw-c6gqgMSDXQmU3wPFvi6SR06APYz4HrOT5I3EFEztbPT854f1jxewE5tjlUiV1CpKA0K0_2LK7yiei27UEmOJquT_J_jtsnedFksQ9V5sFbxbmvWBpNwgfLsvB83pWZ1i1zPj6Un-FJ3afOb_h8M0kM56AAxBX0Y2gSvBwvWPbSshOLT_K7-enZWSz-EPgMHARURiw_i4sp4KYL221JpfsqRsQGuM9A5du17QxBZkVDB36BYlSumHJvCvbGCQ7q4xlHlLcTaL5VHEK73-yRkZnzK3NLBC6qzmFaWz62yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی ان بی سی نیوز:  بازارهای اروپایی با بازگشایی مختلط مواجه می‌شوند، در حالی که معامله‌گران آتش‌بسِ شکننده میان ایالات متحده و ایران را ارزیابی می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/122980" target="_blank">📅 10:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122979">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رسانه‌های لبنانی گزارش می‌دهند که صدای انفجارهایی که چندی پیش شنیده شد، بوم صوتی بود!
🔴
برخی گزارش‌های رسانه‌ها همچنین ادعا می‌کنند که در زمان انفجارها هیچ پروازی بر فراز پایتخت وجود نداشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/122979" target="_blank">📅 10:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122978">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
شماری از کاربران پس از بازگشت اینترنت بین‌الملل، از عدم امکان اتصال به گوگل‌پلی و مشکل در به‌روزرسانی اپلیکیشن‌ها خبر داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/122978" target="_blank">📅 10:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122977">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83bb329e51.mp4?token=NqRDA3MnVp-SDA1pvz65Rhq9R-2h6g6Im1Nk1VYbC4sFCPbqF2Bq8v5wAKDR8EDXrNxf1VoTiCCjuw5e-46-LdTbf0-HtHgEUaSzRwLBdBJnEBCe0VirQfFFneDr_Y-glC436-VzzpJIQEThQbaenIXna4RQ-DwKJAI2PuVJP8Qswzwm3T6jQFX3ENT4PXnddjUndFMyktGsoYMD7BonRsNRVbk8ZO3U2aFsc3IkmclgkcPxc-j9V8x3qGD5SB-MTJbQ5OrK1GEEbi1-ZNt-27e5UaQyGhFs9ioSjfBgE_cgOV9sGrj1F7oAmnU0ej-3MoItAx0C_RHTGePm1FsGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83bb329e51.mp4?token=NqRDA3MnVp-SDA1pvz65Rhq9R-2h6g6Im1Nk1VYbC4sFCPbqF2Bq8v5wAKDR8EDXrNxf1VoTiCCjuw5e-46-LdTbf0-HtHgEUaSzRwLBdBJnEBCe0VirQfFFneDr_Y-glC436-VzzpJIQEThQbaenIXna4RQ-DwKJAI2PuVJP8Qswzwm3T6jQFX3ENT4PXnddjUndFMyktGsoYMD7BonRsNRVbk8ZO3U2aFsc3IkmclgkcPxc-j9V8x3qGD5SB-MTJbQ5OrK1GEEbi1-ZNt-27e5UaQyGhFs9ioSjfBgE_cgOV9sGrj1F7oAmnU0ej-3MoItAx0C_RHTGePm1FsGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز:جمهوری اسلامی درخواست ۲۴ میلیارد دلار برای هر توافقی با آمریکا کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/122977" target="_blank">📅 10:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122976">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
مجلس سوئد ازدواج فامیلی رو ممنوع کرد؛
🔴
طبق این مصوبه، از اول ژوئیه 2026 دیگه ازدواج بین بچه‌های "عمو، دایی، عمه و خاله" تو سوئد ممنوعه.
🔴
دلیلشم جلوگیری از خشونت‌های ناموسی، فشار خانوادگی و ازدواج‌های اجباری اعلام شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/122976" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122975">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
بلومبرگ: خانوارهای بریتانیایی شاهد بیشترین افزایش هزینه‌های انرژی از سال ۲۰۲۳ خواهند بود، زیرا جنگ در ایران هزینه‌های عمده‌فروشی گاز و برق را افزایش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/122975" target="_blank">📅 10:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122974">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-rR-0vS6mjYlTvz1GmTYNfbRn-h45mXP2lQmrGl3I8bRnuhVznF2EIRFBONMYgYezXr6u8yMRQgfXf5w44g1K7sQrkHFpuMdqBlsM5ci6m5Kyo_WKNLsFLdcQQOup-El699nS8AdKSNW3oqec4QFjbWIZB5fKBk1-ZxNej36mZyyeH26v41vBwtCPvkoyT5AkEpG05Ppo6kO-b8OAJaC45_qMKHLAfy7qGLux3s1iEJB83VZxxgnu70Fx-sE81ueXoMgMO_6hnS_DKS7OGfYPhEXltsvM8i4xC0V4D5pvhMDayGJC3vz52jeLFKgR3uyoyOauqxNy8oD1QSv998mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: ایران ۱۰ ملوان هندی را پس از رایزنیهای دیپلماتیک آزاد کرد!
🔴
مقامات کشتیرانی هند اعلام کرده اند که ۱۰ ملوان هندی ساکن در یک نفتکش که از ژوئیه ۲۰۲۵ در ایران بازداشت شده بود، پس از «رایزنی دیپلماتیک مستمر» آزاد شده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/122974" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122973">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
تهدید بمب‌گذاران انتحاری خطرناک‌تر از آن است که اسرائیل تصور می‌کند و راه‌حل‌های فعلی مانع فاجعه بعدی نخواهند شد، طبق گزارش کانال ۱۲ عبری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/122973" target="_blank">📅 10:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122972">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1c3bd49e7.mp4?token=hj7ygibvkDWpXZCS3hQzsEpgFPdRHjfQNq7EKG1T9gyW2MsCFRuTPpuik95G510t1nd8iUZ2TgffMYC5r5WWtSdyRVfSNgiSZLBF8P4OI4X_cOmIXsRRAKU5Hzo9QefzBwWF71vWgo5sDXrh0zF_s6fSzlal3Bh4CPf8qpa07kvRvmKQINjUEi2OYNtuMMrWMVWhA7yKYVCaUd2E1ASZtFEHIrnhistYeii8AeW-471rN3a_JvNagxKsfX64qQI-MqENuqsI-67iExH2I4wW4uzUlRdcapgqLQUGEP0oxDTIz4u0aeLtgD8y6zpiN2R-JvKr1bl2qf26rPK3dHnodoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1c3bd49e7.mp4?token=hj7ygibvkDWpXZCS3hQzsEpgFPdRHjfQNq7EKG1T9gyW2MsCFRuTPpuik95G510t1nd8iUZ2TgffMYC5r5WWtSdyRVfSNgiSZLBF8P4OI4X_cOmIXsRRAKU5Hzo9QefzBwWF71vWgo5sDXrh0zF_s6fSzlal3Bh4CPf8qpa07kvRvmKQINjUEi2OYNtuMMrWMVWhA7yKYVCaUd2E1ASZtFEHIrnhistYeii8AeW-471rN3a_JvNagxKsfX64qQI-MqENuqsI-67iExH2I4wW4uzUlRdcapgqLQUGEP0oxDTIz4u0aeLtgD8y6zpiN2R-JvKr1bl2qf26rPK3dHnodoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه کوبا: روبیو دروغ می‌گوید؛ او طراح اصلی محاصره کوباست
🔴
وزیر خارجه کوبا در پاسخ به ادعای مارکو روبیو، وزیر امور خارجه آمریکا، مبنی بر اینکه علت رنج مردم کوبا، غارت منابع این کشور توسط «رژیم کوبا» است، گفت: روبیو یکی از طراحان اصلی تشدید محاصره علیه کوبا در همه زمینه‌هاست.
🔴
وزیر خارجه کوبا تأکید کرد: او مدام دروغ می‌گوید و قصد دارد افکار عمومی آمریکا و جهان را فریب دهد. من بارها از او شنیده‌ام که می‌گوید محاصره وجود ندارد، در حالی که خودش طراح اصلی آن است.
🔴
وی افزود: روبیو در کوبا به دنیا نیامده، کوبا را نمی‌شناسد و هیچ چیز از کوبا نمی‌داند. این اظهارات به عنوان اقدامی تأسف‌بار به درک مردم کوبا از وزیر خارجه آمریکا اضافه شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/122972" target="_blank">📅 09:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122971">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فایننشیال تایمز
:
صندوق رسمی «هیئت صلح» ترامپ، علی‌رغم وعده‌های کلان برای بازسازی غزه، یک ریال هم پول ندارد و هیچ پروژه بازسازی‌ای آغاز نشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/122971" target="_blank">📅 09:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122970">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نخست‌وزیر قطر در تماس‌های جداگانه با مقامات عربستان، اردن، مصر و امارات، راه‌های هماهنگی منطقه‌ای برای پشتیبانی از میانجی‌گری پاکستان میان تهران و واشنگتن را بررسی کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/122970" target="_blank">📅 09:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122969">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/122969" target="_blank">📅 09:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122968">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
هاآرتص: عربستان سعودی و قطر نسبت به درخواست ترامپ برای پیوستن به توافق‌های ابراهیم محتاط هستند؛ این موضوع نیازمند تعهد به تشکیل دولت فلسطین است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/122968" target="_blank">📅 09:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122967">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وال‌استریت ژورنال: در مذاکرات با ایالات متحده، ایران می‌خواهد کنترل بخشی از حدود ۱۰۰ میلیارد دلار دارایی‌های مسدودشده توسط غرب را دوباره به دست بگیرد و همچنین به بازارهای جهانی نفت دسترسی پیدا کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/122967" target="_blank">📅 09:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122966">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
طی روز‌های اخیر حدود ۱۰۰ اداره و بانک به‌دلیل رعایت نکردن الگوی مصرف، مشمول محدودیت برق شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/122966" target="_blank">📅 09:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122965">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc255b611f.mp4?token=DfEM3EdM4Wyb9rmgQwLQmSfnpI39HujLG0fehokjkKpekEnW2gL0c1xXGSq4X1v2X35bDzudtKojpBngtHDKPdXH9sLfI2rdvM3Rmz0nbUE75TsakxDwde8a-d7tF9qr5Nt-4h8I8JyP1yEmXQHd7qXc_AHrHRPpjTEJH21E3M9I9zShTWJDVvCUrWnZg6IYpnqtr_j9q9LKY0fVFmy9dcCqiEwohG7YCzoSCf0qV9pPnJ3SFiaNbE-uLwiBrQvck6HQ-fdZPZt3hn0whbpzErybFgFiiaRQyGrNCRF5Lrad6swbFiFtrhRHTfAvv4k24EO8V8OVtVDs9_DhoTM9IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc255b611f.mp4?token=DfEM3EdM4Wyb9rmgQwLQmSfnpI39HujLG0fehokjkKpekEnW2gL0c1xXGSq4X1v2X35bDzudtKojpBngtHDKPdXH9sLfI2rdvM3Rmz0nbUE75TsakxDwde8a-d7tF9qr5Nt-4h8I8JyP1yEmXQHd7qXc_AHrHRPpjTEJH21E3M9I9zShTWJDVvCUrWnZg6IYpnqtr_j9q9LKY0fVFmy9dcCqiEwohG7YCzoSCf0qV9pPnJ3SFiaNbE-uLwiBrQvck6HQ-fdZPZt3hn0whbpzErybFgFiiaRQyGrNCRF5Lrad6swbFiFtrhRHTfAvv4k24EO8V8OVtVDs9_DhoTM9IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار مخزن مواد شیمیایی در ایالت واشنگتن
🔴
در پی وقوع حادثه‌ای صنعتی در ایالت واشنگتن آمریکا، دست‌کم 1 نفر جان باخت و 9 کارگر دیگر همچنان مفقود هستند.
🔴
این حادثه چهارشنبه در یک کارخانه تولید کاغذ و بسته‌بندی رخ داد و نگرانی‌هایی درباره نشت مواد خطرناک شیمیایی به وجود آورده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/122965" target="_blank">📅 08:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122964">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASNj97kw99xjFnxVunrygYD5wHCUNoB5W1TjWDnv12YBaY9o8U7frV-0TTBtIBddoaD1r2-x6jv_22C04X630ipfzPV9qcaEP5a_6lN4ACNyzBSn0EKIoTy43bIGqaFMZ5h7MTwtV0ZIoegNmi7_ir4Sm52hHhyi_31Bi5AQg7r_zvqi_o9g_ocHkpnl5-uHJFv_Rn7_brEH5Q17M_Sp1J2Ufw15VSZyXO49pl2tMIiZ58FWwJUwbkLEJ6WIY6QX6ddCS5edIlHyN92FkQb6OG1916gkD5oYrlo4m6k1B0ditq6qX-R31DoFZ5usnBu6Gg-Kri0XG7tjX7tiSzjBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهپادهای اوکراینی پایگاه هوایی تگانرونگ در روسیه را هدف قرار دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/122964" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122963">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G30aN265ZppTrFr23-EJ1CS5vcLMl9bJwq7EAKk-LgfvfspwK3tMQcyBPlcfmYaTxhFgET6HC5zi6Qxu2Szk6mig_xRjQZ7UA2N-_q7cWc-xgekxExPgVYJ2bdKcKQTnmBzo8E_jQRh55KaiOrn5pyef3yjbx9QdwsE71uMNz3qHeR9sTGK12GrueJL8z0vggdahC2z3UhR26ne5ZR2WyIpP-76dtHCOIuvue6-87Cx5yqCioz3wHCPrJ0QLAnUjK9S2-1qKlrqkGcthdt_rV9Q1ifosyizEY67tkMUjogXNXUNaEdsxNsjfmL6BWvUdbNkNM3fVZ3N4a0opX3SNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر روز رویترز از کشتی های پهلو گرفته در نزدیکی تنگه هرمز، سمت ساحل عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/122963" target="_blank">📅 08:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122962">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
فرودگاه بین‌المللی تبریز بازگشایی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/122962" target="_blank">📅 08:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122961">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فارس: بیش از ۲۰۰ فروند کشتی در یک هفته گذشته از تنگه هرمز عبور کرده‌اند
🔴
اولویت عبور برای کشتی‌های فله‌بر و حامل کود است، اما برخی تردد‌های مجوزدار را به‌نوعی آزادسازی عبورو مرور از این آبراه تلقی می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/122961" target="_blank">📅 08:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122960">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
زنگنه، نماینده مجلس: آمریکا حق غنی‌سازی، حاکمیت ایران بر تنگه هرمز و رفع تحریم‌ها را پذیرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/122960" target="_blank">📅 08:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122959">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مدیر عامل شرکت برق: برق 100 اداره در تهران رو به‌دلیل عدم‌رعایت الگوی مصرف قطع کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/122959" target="_blank">📅 08:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122958">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7664471564.mp4?token=d5dOBDFK3puoYjz26JQ0A8sYtlGscK7s7-lpEUNeXgFz9L9_tb14ZpIcMnlzmpm_lm94qqpVSDI2XsrOYkelQp2MXc4Wvt_0Ix3D7NFuk4SZHuK7YIS7kwigj312c93d2GyBiC0RtOgdpPF7Np7xunw3Fmf4ewZDX0MSNJrP9TrRL_BsByKNwWzyiE3Tex-8gd_PvL7J7F4jAQYb2SLjjJ5V1N3n8m37IwMiN9eoiW9zzDPhqA2I9fMy_2MtqynIAJp00PxNVXGGxsMYisWMCazJxnRmFWnNbwfDCMsUgdsrfNVaAs9BlbMYxA0S3ZjB5z3ZOBgU-hUmTWHuw7HDjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7664471564.mp4?token=d5dOBDFK3puoYjz26JQ0A8sYtlGscK7s7-lpEUNeXgFz9L9_tb14ZpIcMnlzmpm_lm94qqpVSDI2XsrOYkelQp2MXc4Wvt_0Ix3D7NFuk4SZHuK7YIS7kwigj312c93d2GyBiC0RtOgdpPF7Np7xunw3Fmf4ewZDX0MSNJrP9TrRL_BsByKNwWzyiE3Tex-8gd_PvL7J7F4jAQYb2SLjjJ5V1N3n8m37IwMiN9eoiW9zzDPhqA2I9fMy_2MtqynIAJp00PxNVXGGxsMYisWMCazJxnRmFWnNbwfDCMsUgdsrfNVaAs9BlbMYxA0S3ZjB5z3ZOBgU-hUmTWHuw7HDjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات اسرائیل به سُهمور در دره بقاع در لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/122958" target="_blank">📅 02:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122957">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کی‌سی‌ان‌ای، رسانه دولتی کره شمالی: کره شمالی آزمایشی از سیستم پرتاب موشک چندمنظوره جدید انجام داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/122957" target="_blank">📅 02:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122956">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رسایی: بازکردن اینترنت اشتباست و خیانت به رهبر شهیدمونه.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/122956" target="_blank">📅 01:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122955">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-O4m3tGPvmoUJzZsmYWr63O_5ydtAiHo9dhPmU5jyexPlbbw4qMG__H-GGRrJ9AcL6uPe77twX_tXFv6xspyu4aL1O4YSk4QGwYiPTgeIjeipHSqGSCY2G0CwWf8MPVzkMfDIhraqts-zWtUEUwSPlX9-l8kNG-9VLYk_uTZLHNKD4Gqy4LZ91abJ54ySKlprb8mq6Bn0iURjgoal7CfPbkeOS0JGQc3hZ83vIiZw3sjc_iUxT5bR7sp9JTBxr-8kr8hvnureE9JUxy9w29ZuPXj5zEsetSFePDR2d05cH6B_03Pfi-t0DxwUp3z8i26qYarVBM7jKmnUAF_VAeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: بازکردن اینترنت اشتباست و خیانت به رهبر شهیدمونه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/122955" target="_blank">📅 01:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122954">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
چین: توافق پایان جنگ ایران و آمریکا باید به شورای امنیت ارائه شود
🔴
وانگ یی، وزیر خارجه چین گفت که پکن معتقد است توافق پایان جنگ آمریکا و اسرائیل علیه ایران باید به شورای امنیت سازمان ملل ارائه شود. وانگ گفت پکن امیدوار است طرف‌های مربوطه بتوانند به دنبال کردن آتش‌بس متعهد بمانند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/122954" target="_blank">📅 01:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122953">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3n9tO1yG0gtIdRc2QWKdtJeiSQOzxVouNWMwsuZDUKJHx06f2ORuD-WBMr1bTraM0TH0FixnpsLMQMHrxhBaQuAYwAwTnGscZ6uaC1aRl2NFgcvsX9gErcVJT7VcAEsZcB464VIo3DjIbEIm1uNwCgvRrs7wBetMnVRJZdaHHkyHKF1Bjs0B6laxqKnKBUMDyqpUBVuk9GHabR95-6mBcuh7ar7DYn-ZVDoEgB7eidKUCvVqxJ32Neir9dqp9sU3LUpHOfvTvDnasGPW2yNrk4a04KPwXnBK_aIqrJN7jSzeu5kG8CZcfUYgdUwhRRKfP8PUzu22525PBaeJM4KUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته شده برای حضور تیم ملی ایران تو خاک آمریکا ویزای ساعتی صادر میشه یعنی اعتبارش تا پایان یک بازیه بعد بازی دوباره باید ویزا بگیرن
😐
🤣
@AloSport</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/122953" target="_blank">📅 01:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122952">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgNVe9DujAoGO-TnrIYttj5SuRWwDtBZQQ_SMDdeHBtA9my7U14p8j8yImGIbQ-DhITfPvtXlZdKtOHZg0HeV2GMRuy8usINh05wGbN-_mISiWaMMiq5wR0cbZDpUdSQdVvj-WTmyvcM2h-pwS4e7TjAZ7BbHWL9nUnJd65rsW_wJdu-PkxmgueyFN8cjqEBu3FoVCR71LbQ_la9LtuCukEk7FaGK3bqAmr_FlxuBu8P-GpJ8y3jkzk_Bs9R8udLfXIx0M7qKCSBgvQO0p82Qqw703Zr5K63jYFVzSdHXqScbe1cJE6vlz5kbGdpyR3dak7U_7Bk66zZtJ03ELkO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
و کسایی که دیگه هیچوقت آنلاین نشدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/122952" target="_blank">📅 01:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122951">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کارشناس صداسیما :
وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/122951" target="_blank">📅 01:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122950">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411f1a7cb7.mp4?token=iGki1A6C6q7JsUQEM2MTSQdbU77LLaYxnAmuxE3uBdvQKL5DtcvmlxjjYudE4RSHNOQ7OgppAxMnhPJyujuTBQjrL1dHMXevqJkhsvXGWOYhWlBdjvCYe8LCRPorGzzeVJLhMQTB_f38Wa1nCrM3wmEQMC3QjVp6nz_QAiQ-bze-DChcnE5NxPkC60LUpGBnPKre_ghbLpwyH9TmPC8vWC2a9sq9LecavGktFchQnlDJesQoyLCskqJPCnnEcNKBNWckejtLljZN0avyruNKyVx89SXKMfv2olxvksQQ28ed9SXZL3IU4a-cttJHXQP0Vd8gjZjF2OuobxevMPEs8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411f1a7cb7.mp4?token=iGki1A6C6q7JsUQEM2MTSQdbU77LLaYxnAmuxE3uBdvQKL5DtcvmlxjjYudE4RSHNOQ7OgppAxMnhPJyujuTBQjrL1dHMXevqJkhsvXGWOYhWlBdjvCYe8LCRPorGzzeVJLhMQTB_f38Wa1nCrM3wmEQMC3QjVp6nz_QAiQ-bze-DChcnE5NxPkC60LUpGBnPKre_ghbLpwyH9TmPC8vWC2a9sq9LecavGktFchQnlDJesQoyLCskqJPCnnEcNKBNWckejtLljZN0avyruNKyVx89SXKMfv2olxvksQQ28ed9SXZL3IU4a-cttJHXQP0Vd8gjZjF2OuobxevMPEs8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساخت و ساز برای رویداد UFC Freedom 250 که در ۱۴ ژوئن برگزار می‌شود، در چمنزار جنوبی کاخ سفید آغاز شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/122950" target="_blank">📅 01:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122949">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTe8ajRK1W2NSbUPQ92aTC8raDzjS-eUWS0rQ55y2WZhqI60RQrumtH9-8H2xR--7zYvLM00PXcPjoIo5nJSBfMeZN8eeJQd32NvtkH5HsyZmu-4PyL93IXspffZXxzFx3SfSaEkQ4uiPkf4J0fXShYa7zqkTO1CNVHwJnMmjlRpnK6sYcxexC6-J4cDHhuuNLlZHtcxMkvx_91alZO-fThHMHzTTtsvkaPAImnKERfJLHWanuHo-hEZHNU1P6Osh3tlH29Jk3109W3XWranE4mjHS7_48uIp3eHxPL1KDXCA236kvDzEPrmOHobDq11Y_aVz3BlfgsKx6oA_-6DBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس سازمان بهزیستی:
بیش از یک میلیون کودک بازمانده از تحصیل در کشور داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/122949" target="_blank">📅 01:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122948">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBelLeUH4WXGSt_AZawupCaAs4BOTmbAHpfiYnZfH0yOdGFLQwkBGbld2C9hVdCz4nnfubzY6QHSA24CgehfhY9GQLpXseLVDwY55gUd5aVo7fYQtaHzhx1qbRtEuIWwKuINlBNVdrm41n8wFPr1t_TTqOWs_pvLzYvmo1fWSb3kx33X8sW30BEuitXAkHn1AR94d_ZRWQmAsyFoElADgxWedoPhG4tqXHgnMll5tlZFlkGKx6C45crUnkBATmCEDXaVfn5jaORGMu4_OUFGkfDkkOrMTWE2UMziv0p8C3iFsyUHsB8fUmzxg_rwV_y4S-Pv43fWney7eD15UpKp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه
:
اقدامات تقویت شده دفاع از آسمان در عربستان سعودی فعال است تا زیارت حج را در برابر تهدیدات ایرانی محافظت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/122948" target="_blank">📅 01:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122947">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vil3WSfTu1yvWeAt_Sq9bXYPftPiKyceyKndypBEPAAkhlgzDL1YbqV1emKAfG1V-7KMtGqNW9P5pNqBW_hRNS6Ou6Ray-JZCzu-AsYQnhqLfw0Cpv1VDsBxMCpp7ftX9gn9n3Xe4Hg6wVzM22s2CacWOx9Q9x2StARNAqX0ZPgcElIl9FfVK0_YqPIYfOYKHHZ0ZdVd_KjM7mJNckYVEHswl_vkBvst3IbhLRPfXrXn_NyHue-HpPgmInMhEIagdKhK1xrrxasAl9U5Sb3m8DgziUgj8ylbq3IiBllQPzxV8pxgLmdVk9iHNZ4uMvgth4kv2Zjfs5XN7Eexj1nthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیج فیک متعلق به انقلاب شیر و خورشید
🔴
رفتار سایبری ها رو بهتر بشناسید.
🤔
پایگاه مقداد مقیم خارج نتونست جلوی خودش را نگه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/122947" target="_blank">📅 01:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122946">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: همه چیز انجام شده، چیزی باقی نمانده جز [امضای توافق]
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/122946" target="_blank">📅 00:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122945">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4r_mhS4mNGOam0GsNyRG1M5uKs8XDmzka3YC2KpEixasAdCyYUg9Jlrwha2PT6y1enZkVc4jeSs5WELIas1iUgXfZQHqKXGZArGTCenA7OWQEbf3KFZ4bRQ-8zvWldfdGANDZYRheZEhEIs09QrdBWDA_vNPM8ZnpIoAqHkoev1OVfj9oZiFDOhD_x_sPB_o-_fGDgOXu1LQxz_N0Ign6wHP68-MpjDkgZD9M6Dv6pBBd4OA6oKo1ITx-fa3nnM5M6160Eq6NLDa72Dqf48aG6V2P2f6rLE8ZHhUtyYaB-ylMC9VzjixxHwSDmzaN89seNjzrL9M5J_TiyRgNPaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه آمریکا :
- عملیات «خشم حماسی» هیچ توجیهی برای حملات بی‌دلیل ایران به نیروهای آمریکایی تو منطقه نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/122945" target="_blank">📅 00:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122944">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLPPIUlAHDDqms6xNwjaBtHsF7MH3kvXDKGDzAqXpJ9_tjnY8_AbO6nOTVNx4qwYvmLoQ2g-Qxz9hVaONtHowRx47S1sI8yzIlbe-sHBSWBg7gScQZRMUKLhSrasUNO5cToaXwCERGRyyTqnorJyDFpN4pJc2bj6Y5z5gLfEjgviHuaTE-Rb_w1wgXbxSdGrx-7Ba_bEWS4CFupASGB-SQFamvLp6fICXVVyVXAb8XnH8MksyAElrn7AJ9TUZUIHEyHa3lrgYkONNG4UFttUknr3qGNfMVsuWvUhpRV5DWD2VZscG0yIJBgWB3Oa4iBUD60u8042FJmsR7skK5X21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صادق الحسینی: رئیس‌جمهور مملکت حتی برای باز کردن اینترنت بعد از چند ماه هم اختیارات کافی ندارد! این چه وضع حکمرانی است؟! ‎
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/122944" target="_blank">📅 00:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122943">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کاش ما هم مثل اینترنت به وضعیت قبل دی ماه برمیگشتیم.  [@AloTweet]</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/122943" target="_blank">📅 00:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122942">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6b923b91.mp4?token=a8Clft5TsDXPiYGAz2tbzFpfCeLfKjyvscFh7tDxtqDO4LnSu4oAqJDcl-JTL_79fcg3ahWpIwKqITWyqdb2WIHJHHbcKvaPSZcbNN--7CHdnCC43rGum5iXZsUbxScuAskFcmWr0aMln2mCDDoVNOQhcW1ASoJKjZtHzgbYiTkwKW6YNrIo9F698TNUZQjVYza1Dt-XWBiMLgq7aLcC7gKwb9mJ-F6Q3W0GKn749HXGkrsO_U4MDBrIy5DVj-xAH8U7kvPMsMnueLslMqZw5yhoCF9jQ_en0c5ugbTRaBSAlA3MFVO-LP-ZZRD8d3QbHM4_ZVQqGEn32-kZzdsQXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6b923b91.mp4?token=a8Clft5TsDXPiYGAz2tbzFpfCeLfKjyvscFh7tDxtqDO4LnSu4oAqJDcl-JTL_79fcg3ahWpIwKqITWyqdb2WIHJHHbcKvaPSZcbNN--7CHdnCC43rGum5iXZsUbxScuAskFcmWr0aMln2mCDDoVNOQhcW1ASoJKjZtHzgbYiTkwKW6YNrIo9F698TNUZQjVYza1Dt-XWBiMLgq7aLcC7gKwb9mJ-F6Q3W0GKn749HXGkrsO_U4MDBrIy5DVj-xAH8U7kvPMsMnueLslMqZw5yhoCF9jQ_en0c5ugbTRaBSAlA3MFVO-LP-ZZRD8d3QbHM4_ZVQqGEn32-kZzdsQXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز:
جمهوری اسلامی درخواست ۲۴ میلیارد دلار برای هر توافقی با آمریکا کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/122942" target="_blank">📅 00:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122941">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
حزب الله امروز تصاویری منتشر کرد که نشان می دهد یک Fpv به طور مستقیم به یک وسیله نقلیه نظامی اسرائیلی که سربازان ارتش اسرائیل را در بنت جبیل ، جنوب لبنان حمل می کند ، حمله کرده است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/122941" target="_blank">📅 00:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122940">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
جمهوری اسلامی چقدر مردم رو فقیر و بدبخت نگه داشته که بخاطر یدونه مرغ صدقه‌ای اینجوری صف کشیدن.
🔴
کشوری که روی بزرگترین منابع طبیعی قرار داره.
🔴
خمینی: شمارا به مقام انسانیت می‌رسانیم.
🤔
ویدیو یه نکته‌ داره ببینیم میتونید پیدا کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/122940" target="_blank">📅 00:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122939">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEgSX2YlvPxtp7PNMo4dIuj3lJpQF7tE9smtxc73GKltcMVVE2XpNZYjU-4Q4AghP1VreX5nfiH7UXUpza500F_M85MqLLcpoxBGW8AIvcqGGH9n9wY4InHxr8rzUMyyBXyi32iSFhKlCRMKRnPOHI-zCHNzNG1SPobfI9NewqAg_x56cCPBmm1cG68gb_zrNX0ezu4QNpEhjafaJrbVL-660Cea-22PzawEwAB2UnWe76d9OoodJcVNKQq-A9TarROiycz2TvBqJj7i70IbAnFsf2063BeYIIZAB4o4rSQmrZ4UconAO9XVfJt4XPTb-iFVi1QM0fDMUns_MR1qjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : فردا جلسه کابینه تو کاخ سفید برگزار می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/122939" target="_blank">📅 00:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122938">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWIb1mVMu0-kVLR5rFFozjJNG82MFqDbNqMkIj9-TQ8gxfu88TXtmsHadDkbmeT0tscSul5IELDurDd4IWjclj3V33uLPPnKxEQNHCULpIi8Yj2X4lQBBOxlZNc0I4Xw5F7uiq8w10W20L653idh6IQkuewryqfcRDvmb68JRdEUtTFbNHTXnlVxX5JeqCtNZAPNDnbViSVxc4SoAzjT-9yN4Qr4_qSUa6MSFSt_4IhfEedCuY0xe93TR3PzUGA8iY3Wn3gJzARbLwC6iDCLpX8eSszF_AVGLqmqQ2IlDjz7mpffkjRqz91A7GDH5MHUToWInlnf0L2Dpyla2PQavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: از افراد درون این عکس(فرماندهان حماس) هیچکس زنده نمانده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/122938" target="_blank">📅 00:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122937">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WJ6KfJuYLk1ujbhWL7Taj05ap82i_OvDueHKw2YnXVwzW9f7JOdRB5YSZ0hYc2PQg16RqjzZIelq-o0TJgVUvMcbVnSeS0uPOEVtxOhaCFqm_UkPOL9TUBP5lg4iLx26Bs1xS5FtJnOufWFzI7dHzgzXkIJXWixtSCTCrgDlaYETyjR8FFJQpavqTq_8uz4gsWc8V2pZKtBjlt3kr-AP5gBOU8mq5XHwcmsAv-GvYxRJqmMkFx0BQitagWjsxLdKt4z_KO142vLiaFslEukHjzfE-ojqm6mhg1LtBAhbxFcKoDvkDsSPAXU18LEM9CZ8WKak4EmZkFbUXZvA7Yv7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از محمد عوده، فرمانده شاخه نظامی حماس که ساعاتی قبل در غزه ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/122937" target="_blank">📅 00:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122936">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWIlsEvkivqcqJ3AgwgwIBp3ikw9xNVJn4mqDubHl6Sn7yOmKRYecf8YwxFmQ74shwCycpQ5QF75t7eRo0Hkn74J4Tk15qlt6NJC90jmC1Rl1j3_PpzVyejbtxQ5XAw5wVc0UBOpHWBz_JQ15uyokaRuac3OS-ND2XHTqHNSEVzjNb3VHo_Ic9BhpljWRcQUAQQev5Yv6pGA0mHvjXIh2a2LBxTM-8476hTKuhd07Tlzm_E_WbjTUPdSAprxZSHwoyZlEbw5NKKSprG381_nF4vOj7KqXQury3TzEQUiYLGrfSWYHTqlNzTowle7LHXSEnsZSDxqjMgKW9swJQzM_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: میتونیم بمب اتم درست کنیم و بجای اینکه بزنیم تو شهرها، بزنیم تو پایگاه‌های آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/122936" target="_blank">📅 00:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122935">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
حالا مردم خودشون آنلاین شدن و دارن می‌بینن این حرام زاده های «سیم‌کارت سفید» تو این سه ماه چه مزخرفات و چرندیاتی رو به اسم مردم ایران جعل کردن و نشر دادن تو رسانه ها.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/122935" target="_blank">📅 00:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122934">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1005c8d36a.mp4?token=hH-8CutCEyD_CBi0zGdxHUTBMHhaxJw5b7LlzKtdf4mBK3sfkypBBD7ZGSNFWZXT-NGRntEFmsQ6pCldefLvmtkYuYClgXHIMSRJhoK9Dlafu4FRr_XmdnEtgL-iKITp3VJbuXpU_Zoew_X5rg-H4s4jm6GiXB1-zqqh81souuOzv69EcciNfgeAu1py4Vf0J4D0C0P0t-mNyCReFmplkNqFnBtQbrm_nHLlumSZJ8VJWwK5gt3zMmr-MUyVoEzJWCuNbk_8rXM1MbmQ76FspN33uR1neBnVkX5LHnSaFzss_oQaTf3eJQerNnQ3q-5PpE4ey88jZgFRxdpk-5Peyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1005c8d36a.mp4?token=hH-8CutCEyD_CBi0zGdxHUTBMHhaxJw5b7LlzKtdf4mBK3sfkypBBD7ZGSNFWZXT-NGRntEFmsQ6pCldefLvmtkYuYClgXHIMSRJhoK9Dlafu4FRr_XmdnEtgL-iKITp3VJbuXpU_Zoew_X5rg-H4s4jm6GiXB1-zqqh81souuOzv69EcciNfgeAu1py4Vf0J4D0C0P0t-mNyCReFmplkNqFnBtQbrm_nHLlumSZJ8VJWwK5gt3zMmr-MUyVoEzJWCuNbk_8rXM1MbmQ76FspN33uR1neBnVkX5LHnSaFzss_oQaTf3eJQerNnQ3q-5PpE4ey88jZgFRxdpk-5Peyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از کسایی که تو تجمعات شبانه شرکت کردن دارن میپرسن نظرتون با قطع دائم اینستاگرام چیه؟
🔴
و اما جواب حامیان حکومت:
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/122934" target="_blank">📅 00:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122933">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: ایران به دنبال توافقی است که بدون واگذاری پیروزی به ترامپ، موجب آرامش اقتصادی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/122933" target="_blank">📅 00:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122930">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f4740d27.mp4?token=mF7QbHyVMudaKmTd9APKqEO4PL6EyU-Wzh_p6PicTajGGRjQVEY-RebbFXNcG5UeB1JRdXmsRwvTCKZPvNWKaNyg1n6SFE3d_aDexWB4eAuVHw85IywU76aWYXSv4YOD-oPSeiWYCB6f6InLnj86XJMI1N6KeRQmYOiqBgwTJxkjG0pAVSHUnEshjo2YsYeviHj_ZlsgXnChGnIMFmftX4ZG4niLq5rXxa362Ufz_0oUflln_mKk0IlFMIHy-ao49RhjHk76iI677uGzbWtMe_9s-R62upc2A9q1u4DKvgBAshuD_nMNLZxIpSXHsURHzzfGPCO9eC5z-jGA8f-8nnp9N75X-O5fGAx0w8etME7M_BEqR2JNH0bfw31IM5k6Y8T9TuAE_BL_fJUKGuz6vWuj85v7OL34M3KOCTYPFodHG0SQxoFsUmIN2d6W2eE6_TM2a2Yf03J1zboweHqZ7Z9d3mbdpdf4EsjSdugDb1Q2bSCUCYMr7tyHG7ytOuBF51EXSjBfPW8Pdh-JtUgLynvWVhAADWHzg0YXsU7n9fTHrTBIAc4rUUYTanZx6FTLWmHBXBIv2_emKoPG2X4KBjnKcj5NZV5awSwcRnuxS2TgoOBIgCT-15xJZIPOFgW16M8t8qRiURCuTXiVVSucxm8uZBBl0gX0V23Mp3BEQPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f4740d27.mp4?token=mF7QbHyVMudaKmTd9APKqEO4PL6EyU-Wzh_p6PicTajGGRjQVEY-RebbFXNcG5UeB1JRdXmsRwvTCKZPvNWKaNyg1n6SFE3d_aDexWB4eAuVHw85IywU76aWYXSv4YOD-oPSeiWYCB6f6InLnj86XJMI1N6KeRQmYOiqBgwTJxkjG0pAVSHUnEshjo2YsYeviHj_ZlsgXnChGnIMFmftX4ZG4niLq5rXxa362Ufz_0oUflln_mKk0IlFMIHy-ao49RhjHk76iI677uGzbWtMe_9s-R62upc2A9q1u4DKvgBAshuD_nMNLZxIpSXHsURHzzfGPCO9eC5z-jGA8f-8nnp9N75X-O5fGAx0w8etME7M_BEqR2JNH0bfw31IM5k6Y8T9TuAE_BL_fJUKGuz6vWuj85v7OL34M3KOCTYPFodHG0SQxoFsUmIN2d6W2eE6_TM2a2Yf03J1zboweHqZ7Z9d3mbdpdf4EsjSdugDb1Q2bSCUCYMr7tyHG7ytOuBF51EXSjBfPW8Pdh-JtUgLynvWVhAADWHzg0YXsU7n9fTHrTBIAc4rUUYTanZx6FTLWmHBXBIv2_emKoPG2X4KBjnKcj5NZV5awSwcRnuxS2TgoOBIgCT-15xJZIPOFgW16M8t8qRiURCuTXiVVSucxm8uZBBl0gX0V23Mp3BEQPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی گسترده شهری در فیلیپین را درنوردید و 489 خانواده را تحت تأثیر قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/122930" target="_blank">📅 00:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122929">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPGGh7Xlzmnt10A5OMJ49T9vxwVu8QlktB1h_zwgGULeMGAurZyxjmVr0OevQsVfmqPaA2hKWPXEQgRCAPPVArswl0hsoXfM4QnGD0480z0YlN4lnp8S9C8Pd581KZUF5edCOBsHQW1g7aru00oZHLS7MIfK2D387Hn_TKuevXzo_sPLtwyyKY5ukihJqpIetLLGfTl_ggrgtkxbEeTFNzPRHYhAY_8jUyB8MOwQ2wQ6rsvIf0gbS5IJD0w4CS4F2RkHB_XW0zcn1j3nT5OOLLL_24l4sVvpgRB8pCX92ONF53SeekYT3_cNVXrV1OWLdKb7EOt0nDqK566YuIA0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت زمین و مسکن در ژاپن همچنان از سقف تاریخی خودش در اوایل دهه ۱۹۹۰ کمتر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/122929" target="_blank">📅 00:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122928">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlM6UkFIxXrZ7YqXggSSZwuSDIa1VcPcidwnYE7b8HS38qHGmH4uyS6bIVAih2CQqCN_MxF80xKmHNRiGFkQAxzcC2H0Pdg_gWgSXHe0d4O4j9Tnwtc6sqe1NLfNWmLjpp-JalLuCustlIfH8OCNiLcFziqBFQWMMIF8xb5Tp8B_ctzoHU6V3ZqUj5Dzr5nRV2iDnDFHLSy-hdtzuWXBciFfSTG3hd-EF-SKjS5YFPjbrXEVtTUij7Hjl6GI8MJJYDtp4NZSH-JdZmDyNd9NgW-1q7XJxqyQvxQF94_RbQfbfvPivPuGmvqitOYDZ5F1WdQI1Ga0D6m3vXT6gfkT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانفیگ فروشا:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/122928" target="_blank">📅 00:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122926">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kp4uq4mA1zNm04OrixAVDVj-VVXaDtOdhN_qRWlHNqNEbJ17ymmVAUwrQq67eIR916zixiAygk4JPqa3Rd8aNmnvpExdVxR8s2fqsronXTWqzy_Ke4oSnh46KHLrLwjhjxHqMP8aw5mRy1S05RNfjoeFqkgtVuI5pjVGSuLYI47OQRNXYN-ykUXC3Js7goVFue_3FpGECZF0YaRJzrh1utbduqoQ9NEFmvLuD-nkVNJZbL8_BMnWP126-xLyObl_7-E_rioIs_sBt9jqmbK5wF5JGM4-JCfdb5GMBRM_CLkcLhpG4-KKCcLFD-MrQdWB_UKaB64fBVKe4PkDheBukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fI3NrN0uS-NM0hf230ienyphRP3nQoMbU3_2b4hy8gzce4mA9Y78jBvpripq54bX1gcOqBj-n0b2dDcJxe7idsUO3Oj34Zw2HK4kCWUkcDSZWThBjEYyA8He4PR84qW17uuciKGSK3BBaT9_kXx_1oIcKfwyJXVnRCdDpT8dggclGM4AHqooWCcxnA59lOp7VFVxkGyvTNcD2PRWGpYlRihqF-BSeBsAbrKnG_L10xlbw9VG2b-SXroOpeKqjV_h63Isa9zVeynQ6pHzzyWdOFUbSWEMGXM5n4pJvOyjCGfTHV_t47a0vjXSgQU4yV17s_CDSM7wVB3DC4Idz8oYgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
همچنان در جهان ۲.۱ میلیارد نفر دسترسی به آب شیرین ندراند و مجمع جهانی اقتصاد تخمین می‌زند که نیاز جهانی به سرمایه‌گذاری کل تجمعی تا سال ۲۰۴۰ در زیرساخت‌های آب ۱۱.۴ تریلیون یورو است که ۶.۵ تریلیون یورو بیشتر از سطح سرمایه‌گذاری فعلی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/alonews/122926" target="_blank">📅 00:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122925">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3695a24bdc.mp4?token=tkW0uqFkiXczWq_JH41WKth5um5EKoI5ikiH4e3fxOW1WvLdWrhnMvecWvP-GtJ5cBCrIs8eg_E3vHBfZpc5mZxAuhcIAgZXTUa_0eUr69L2RHjXRr8_cPqWNMP9Kqs5BWDq_nLDBgJYwmrK4hpUZ3D23Sxoh_LNckRzDvEpwk0-uTwQfR6v1-HRd8JpjwUNIhPZ7U9uVsgG2lS-KLDv5XZLEB06GzCgjfQMJN0Nh1VhoYwUT_plqFn_lKg8tFnwsDsjwXPmoEC9S-JvyFNIobPtL7Hg4uPwkX3nSCIfk9g-crgi5clEibxm10xOJk8zFBlFij8TjpGXXrf8CWvW2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3695a24bdc.mp4?token=tkW0uqFkiXczWq_JH41WKth5um5EKoI5ikiH4e3fxOW1WvLdWrhnMvecWvP-GtJ5cBCrIs8eg_E3vHBfZpc5mZxAuhcIAgZXTUa_0eUr69L2RHjXRr8_cPqWNMP9Kqs5BWDq_nLDBgJYwmrK4hpUZ3D23Sxoh_LNckRzDvEpwk0-uTwQfR6v1-HRd8JpjwUNIhPZ7U9uVsgG2lS-KLDv5XZLEB06GzCgjfQMJN0Nh1VhoYwUT_plqFn_lKg8tFnwsDsjwXPmoEC9S-JvyFNIobPtL7Hg4uPwkX3nSCIfk9g-crgi5clEibxm10xOJk8zFBlFij8TjpGXXrf8CWvW2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیوی تازه‌ای از پیکر جوانان جان‌باخته در دی‌ماه ۱۴۰۴ منتشر شده؛ تصاویری از سردخانه‌ای در خرم‌آباد، همراه با فریاد دردناک مردی که می گوید: « دو برادرم رو از ما گرفتند.»
🔴
این تصاویر فقط روایتِ درد نیست؛ یادآور بهایی‌ست که جوانان این سرزمین برای آزادی پرداختند.
🤔
صدای یک ملت خاموش نمی‌شود. راهی که با امید و ایستادگی آغاز شده، با آزادی و پیروزی به پایان خواهد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/122925" target="_blank">📅 00:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122924">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
طبق رسانه‌های عبری، ساختار امنیتی اسرائیل از کشته شدن محمد عوده، رئیس ستاد تیپ‌های عزالدین قسام، اطمینان دارد.
🔴
هنوز هیچ تاییدیه رسمی منتشر نشده است، اما انتظار می‌رود که منتشر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/122924" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122923">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdHkkXZRvMBRzIyjfkacxUtjCPyyROdDLdROapUWm_hCRrbUFqXkFOxfp2-Kl_8aYLjcLwdrKoOT-CVt23a8897T_Tdcge-LhF7qsY34A7j7r9rHbxUC_-8AQKSNKv6iS_K-Y3Afs4D5eOMfDw4mjerYG_kQo4JtXvoOuKkU8GwxgjjRE0ssmj65ptjK9cCYLrAg76gkIdaQ14_2g_VXacofW_Z1t7E-dN4NJPdLtgZoG9L0fSSJXjxbezUSFdKsup5XkKHuAcou-2R2L8lgJKl22U3Juxsj6QafjB4pTlTMr2nIatpKg0_4wPly_U1JgGXSj0c1x_uxoYaFdHQKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: جهان اکنون به‌شدت محتاج توافق میان آمریکا و ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/122923" target="_blank">📅 23:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122922">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : تو نهاد امنیتی، ترور محمد عودة تأیید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/122922" target="_blank">📅 23:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122921">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
چین توافق پایان جنگ ایران و‌آمریکا برای تأیید به شورای امنیت سازمان ملل ارائه خواهد کرد
🔴
چین: معتقدیم که پس از دستیابی به توافق، برای تأیید به شورای امنیت سازمان ملل ارائه خواهد شد تا مشروعیت و اقتدار داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/122921" target="_blank">📅 23:32 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
