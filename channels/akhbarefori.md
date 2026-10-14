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
<img src="https://cdn4.telesco.pe/file/daod1d4Wue_iz8u3xmlOfT_TLsv-Qre6VeXckLwOpN14gi2VUcevQHE2_R47G82mZ79MFzpNwmwUIzybp7zh-xP7RaFK3OV3eTra56fOJYc0kgFOO_UZ5ZLIpCNZ0nuLBwgLosptUU5PjtIKZWTsMd7IbV_n99ns8wFJC48ufb0Vr-WphB_wvq1vf2pvMGRMVb0ljVfWxS946g7Qf9K4vXb64gm3tsMImvBR7OlNp0sYMsxVtWw0QyUxvblEOM2A1DBG_nv5x53yiV5MRIexSYZyOcrwpuOWfEp9IueyNOo9BKnUmEDSr5oMj0f8htTtIOzdaE-r-BYnfsXutYV24A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-698492">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
قالیباف: تفاهم علاوه بر بازدارندگی به نیروهای نظامی ما کمک کرد تا قوی‌تر شوند، تاب‌آوری اقتصادی آن‌ها بیشتر شود، حزب‌الله لبنان قوی‌تر شود
🔹
ما با این تفاهم فرصت و منابع کافی پیدا کردیم که مولفه‌های قدرت خودمان را قوی کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/akhbarefori/698492" target="_blank">📅 21:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698491">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24e20cf932.mp4?token=SXJOU4Yeso3CzAeRHEpJYlvoV3thgPvWjBCfxSzN7T1Sn-ewWUO1GQyNJj81imi8XBrolht0Kw6d-c9-3NHemxPKV586L-MaouRYWeiM8WqQDZwuO4OLOGzXWrFaM9qEZ8UnrPdhJcs1qPqzVbAEI3r2UX8jg-nQ-L7_LtH_fTf9qSi2moWI-Kw9XayE4svStnQBDD8dXQ4pyxafojwJCNZpdtMYDiuqjQBb43whv-Iec4qkUxx-9-hinchfX3av3amEfM6h2rVC-KPxW8X4OtxwQY15RXHSdS-KfF_z7e2co-vEaS9L1u73fYMLXwicxRkDJmbC6sSusdzXMu1hb0jDNS77Bgi7ULsV0BZj5beFTW56wBiap_TecgZLXXRuue0oMty8nmy4irW-eYGM_28lhGrMg4Duui6l53E8FGGq_e31vIjPaF8CoDMuHc4NGNpE8GYXJedWoo7kn-b-B6GqPcEtQs69xKwA9L53IrAmccwQZ_wbadkrx7YmRFnR3BLOT5O5QATGLGPkAuQAow7ft0zpj3z9gLtxeBb6bQmPBnSC1Y5KfNN8GgFMlNF0-Jgd5L16xVtoRrFkGMjkOEwCmyouqZCI9HbKDZk3ffsmwfu_6FKRyTQI3KYL9HGyfD2rU8Rq0kQ1jNaPO02GTN_cUXkwsRxKQAsK1ZVnZRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24e20cf932.mp4?token=SXJOU4Yeso3CzAeRHEpJYlvoV3thgPvWjBCfxSzN7T1Sn-ewWUO1GQyNJj81imi8XBrolht0Kw6d-c9-3NHemxPKV586L-MaouRYWeiM8WqQDZwuO4OLOGzXWrFaM9qEZ8UnrPdhJcs1qPqzVbAEI3r2UX8jg-nQ-L7_LtH_fTf9qSi2moWI-Kw9XayE4svStnQBDD8dXQ4pyxafojwJCNZpdtMYDiuqjQBb43whv-Iec4qkUxx-9-hinchfX3av3amEfM6h2rVC-KPxW8X4OtxwQY15RXHSdS-KfF_z7e2co-vEaS9L1u73fYMLXwicxRkDJmbC6sSusdzXMu1hb0jDNS77Bgi7ULsV0BZj5beFTW56wBiap_TecgZLXXRuue0oMty8nmy4irW-eYGM_28lhGrMg4Duui6l53E8FGGq_e31vIjPaF8CoDMuHc4NGNpE8GYXJedWoo7kn-b-B6GqPcEtQs69xKwA9L53IrAmccwQZ_wbadkrx7YmRFnR3BLOT5O5QATGLGPkAuQAow7ft0zpj3z9gLtxeBb6bQmPBnSC1Y5KfNN8GgFMlNF0-Jgd5L16xVtoRrFkGMjkOEwCmyouqZCI9HbKDZk3ffsmwfu_6FKRyTQI3KYL9HGyfD2rU8Rq0kQ1jNaPO02GTN_cUXkwsRxKQAsK1ZVnZRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کرباسچی: باید نگرانی های آژانس اتمی را رفع کنیم! / مجری: همین یک سال قبل رفع کرده و آنها هم تائید کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/698491" target="_blank">📅 21:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698490">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQny0l1d9MNNBw-O1vk-IiArB0x3s1-g7Y3B3hJVkKCKPFcU_JwVVW9NZvkqiglVm6LMAGIEuPRyCIMcuwZh1znCebRyCkmD7Kj-o9DcBalvC99lkGhEH7-noHzYj_jP_4zwBzwIG0li5aeRu7BZ90UT8Yri62TvA6oWIB7pAQ-5yzu8Pm_Zbh-9tB_ybRYhGOnfz1du-cH5AgfLDozdK805O9EtZAkgO5u9gwNn6-5nrQYWdUfK7PwapAg5pbJDF7cposNh0tXesQpGAn09MVPyWAruxxBXA-FBKVlZ-N0wsmly-ez0vPqiTPxFHUbT8Zu0SwRgp4IBZjOFNOo25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پروازهای مشکوک اسرائیل بر فراز سوریه و عراق | آماده‌باش در آسمان منطقه | آیا اسرائیل در حال آماده‌سازی مسیر حمله به ایران است؟
🔹
پروازهای مکرر جنگنده‌های اسرائیلی در حریم هوایی سوریه و عراق، در صورت تأیید گزارش‌های مربوط به این تحرکات، می‌تواند بخشی از آماده‌سازی عملیاتی برای سناریوهای نظامی احتمالی علیه ایران باشد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3252460</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/698490" target="_blank">📅 21:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698489">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c8409f67.mp4?token=fpj--uHXJsaOi0q84ia-bUMTDiwNJIkNjwlT1x39O-OyTCnQhfTC0NqvCT0bidBY4GMZW5HKmtafs6c-99CAw9eMCVnlCgiZRpYYQKo5dJlefwgUx4kXiMmm0qje_wO2pyUwYotcd_XK0rRW40p_onsdV8kTrmanArfQO-YLwCDuMJXDSDOL9969WtmX2ND_iYquthwvMaL8wGGSYrMWEcHc9ANl9rnlKM28iJZFyBpY_6mwS7sN5sqTaY50oxrbPxuhh2cyTZJR2g35ear5sYn5IcuO5gy7SKZ1vvUW_rgoEf6D-DlgYbttvEUwvELnflBeQD-xt1mOoIy3CdTccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c8409f67.mp4?token=fpj--uHXJsaOi0q84ia-bUMTDiwNJIkNjwlT1x39O-OyTCnQhfTC0NqvCT0bidBY4GMZW5HKmtafs6c-99CAw9eMCVnlCgiZRpYYQKo5dJlefwgUx4kXiMmm0qje_wO2pyUwYotcd_XK0rRW40p_onsdV8kTrmanArfQO-YLwCDuMJXDSDOL9969WtmX2ND_iYquthwvMaL8wGGSYrMWEcHc9ANl9rnlKM28iJZFyBpY_6mwS7sN5sqTaY50oxrbPxuhh2cyTZJR2g35ear5sYn5IcuO5gy7SKZ1vvUW_rgoEf6D-DlgYbttvEUwvELnflBeQD-xt1mOoIy3CdTccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد تلویحی کرباسچی به نوشیدن جام زهر  کرباسچی:
🔹
باید با یک توافقنامه و ارزیابی غیراحساسی جنگ را تمام کنیم. امام خمینی (ره) در زمان پذیرش قطعنامه فرمودند که من جام زهر را نوشیدم و با خدا معامله کردم.
🔹
اینکه شما هر شب در تلویزیون کارشناس بیاورید و بگویید…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/698489" target="_blank">📅 21:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پیشنهاد تلویحی کرباسچی به نوشیدن جام زهر
کرباسچی:
🔹
باید با یک توافقنامه و ارزیابی غیراحساسی جنگ را تمام کنیم. امام خمینی (ره) در زمان پذیرش قطعنامه فرمودند که من جام زهر را نوشیدم و با خدا معامله کردم.
🔹
اینکه شما هر شب در تلویزیون کارشناس بیاورید و بگویید پدر آمریکا را درآورده‌ایم دردی از مردم ما دوا نمی‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/698487" target="_blank">📅 21:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698486">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk8FMLtJr1iqlgkLgE44od3O1GxpF-LtOVObH6bF-pyq1Idiu1nhJ4Q8XZHeVQie6_s1QzcOZ_tEBDDsLJy7pP5xgTztbQzS8OU83v_QZe9aASemkvzG5HbXf07u344_FcsdPNhUz9p1iJ0oBTEnphgtCeMq76OjDUFH5JxpZMfbkOrU_7bIMqCMFFt3kFQVaMmfqB6GIigetzdZ_52kfj-NZ7xXcyimVgECxLLaA8tT4jZH30JNCb-C2ZIg_eaVu_NE0L_KHrOlov7BAfPyJ5PiwVnIoDa_leFF4H2vSjR-b4GgTqurdlmXC6NpnHZFrNsn9nhFDaDXAQsOdJHIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف در واکنش به ضرب‌الاجل‌های بی‌نتیجه وزیر خزانه‌داری آمریکا برای فروپاشی اقتصاد ایران: به وزیر خزانه‌داری آمریکا نوبل فیزیک بدهید! او با پیش‌بینی‌هایش توانسته بی‌معنی بودن مفهوم زمان را ثابت کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/698486" target="_blank">📅 21:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698485">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoHICnsmbJC4oB77xePza0NfiNUpUjflS9a7dHA67cOzPCj8oK4lahBI7dAZszg1Bhg6HlSvuqAYMBUb9IK9zDltJxbVlDQc4ixQCIEMyqhUGklpt5Xp89FqK3r4BDCYzDAeWzD1dTp6eLViweVUTY3Q2vCEx1VHNcMiCRTE1DSxHPzuJe79JL-by0MHVuy6A71ICsorzG06eRWtrQEI5n35ulBFcIjAm9CfOlIscfHozMjFXZ1i8DPI22cIYYpd5u9oJx6YfGDDvyZwrhCkj8plAGRDwNbcsOO16o7SDV59A_XXn10HCaiAiNDvHJsVqpviCexuVyi71tihlw4Jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفر رئیس اف‌بی‌آی به روسیه پس‌از ۱۳ سال
رسانه آمریکایی ام‌اس‌نَو:
🔹
کش پاتل، رئیس اف‌بی‌آی، برای مذاکره به روسیه سفر کرده است؛ سفری که نخستین سفر رئیس این نهاد به روسیه از سال ۲۰۱۳ محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/698485" target="_blank">📅 21:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698484">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
قله تفتان؛ آتشفشان نیمه‌فعال ایران
🔹
دومین قله آتشفشانی نیمه‌فعال ایران، قله تفتان با ارتفاع ۳۹۴۱ متر است که دو شاخۀ آن، بلندتر از سایر قله‌های منطقه‌اند و از دهانه‌های آن گازهای گوگردی متصاعد می‌شود. این آتشفشان در سال‌های ۱۳۴۹ تا ۱۳۵۰ آخرین بار فوران کرده است.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/698484" target="_blank">📅 21:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698483">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1U96rBst8Ow_-1LN0fnT2IuSmdSVESm5C-zAQfUiz1-5-k_i_zVHMzmBBvf4XjpuPkmk08mKLoS23sth2H3w_kJCynUq_6ZKV2W2aQQ_Uu2YosQI8II3qkvmXzfRte4BYjEa_QjhlzEoePFbx_RdaE64_RIFgXn-PLnTLbEATKGY2zpSuLMeJRV1w_iFqRnaa-lYIbK1fbMdj7mXLZ_Gg4Nbq56lES-Dj_AVyoj3i35rk-SZQFpQwn0UcgKtVfYDZEwUq7LhvSzujbeRpYy9l4jzLNG6u7txxrhqtUzNZff5u7ykYuuRhWZlt9_dMSgUh2ecKIzKW-KEQboZqquVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امکان دسترسی‌پذیری نابینایان به محتوای فیلیمو فراهم شد
🔹
در راستای تحقق اهداف مسئولیت اجتماعی و ترویج فرهنگ دسترسی‌پذیری دیجیتال نسخه اپلیکیشن و وب فیلیمو برای کاربران نابینا و کم‌بینا، به طور کامل دسترسی‌پذیر شد.
🔹
با فراهم شدن این امکان، کاربران نابینا نیز می‌توانند محتوای مورد نظر خود را از طریق پلتفرم دنبال کنند. همچنین با توسعه زیرساخت در این حوزه، بخش‌های ورود و ثبت‌نام، جست‌وجو، تماشای فیلم و سریال، دسته‌بندی محتواها، حساب کاربری و... در نسخه اپلیکیشن و وب این پلتفرم به طور کامل دسترس‌پذیرتر شد.
🔹
دسترس‌پذیری یعنی همه افراد، با هر توانایی یا شرایط جسمی، حسی و ذهنی، بتوانند تا حد امکان راحت و بدون مانع از همه ابزارها و فضاها (دیجیتال و غیردیجیتال) استفاده کنند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/698483" target="_blank">📅 21:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698482">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjFFpUcd1QZYpPWFVfBhNJjyWgaCz2hHaR5wtFl4T_rYEsnJkVO7lf78u13JCOEPyvwa9qH4YBIHB8VXun8KIhcK30-SpuihI-EsLSp6zPDzVz0DLXa_yjsNMC3bGFZxKql5DVnqm4-nGzBpwZBpamcFcMehPR6pmchUMHtLTyuUWtMLfyZrcxfqg3UqDAWesxX-3oUz3OIYnv-5EUrcU8EwyfWVdaGmBfimkn9ODEFfqX1kQeiqPsgHsGaM9d3EFZs4brvNciLeqvWAK38WLKMgABwziaK4e0yg7s6iU3ZjBYNlW2Bpbl3KETrr6-usFe5nhMXWnHCs2DM4ItwWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط تلفن سازمانی ۴ و ۵ رقمی نکسفون
راهکاری برای حرفه‌ای‌تر شدن ارتباط تلفنی کسب‌وکارها هستند:
🔢
شماره‌ای کوتاه و آسان برای به خاطر سپردن
📞
نمایش شماره ۴ یا ۵ رقمی سازمان در تماس‌های ورودی و خروجی
⭐
امکان انتخاب شماره دلخواه از میان شماره‌های قابل ارائه
🏷️
فرصت ویژه مهرماه برای خرید خطوط ۴ و ۵ رقمی نکسفون با تخفیف‌های ویژه
🔎
دریافت مشاوره و درخواست شماره‌ی دلخواه:
https://isp.nexfon.ir/khabarfori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/698482" target="_blank">📅 21:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698481">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d0c8a57f.mp4?token=XhNgj4xIQ-jmmpblBOu-AX1V91yW1vqZkz8a8t2WGvSPjlKTHznXr2LKo-KHtvWKebbrTdFEYek9ZabtcQu1g3jwnvG4fYXcYuCaiRxWhAJ96847ROykFKhp8jWsmOFmOveBdgD4Jm6gBvKAMuU1xuixvK7bfn3mw136LsGpnl14sx_xehVq6LsW7IMqM1BE5sOxI5ptF-0BzUrM1uimkPiO4MeFQAEjJ7nM0lJxP5j811kv9lYeoGLpawEE90rgM1mzoK_wX0LasR1TeHcEFbSi_VQ4-hCPVoD23Pe-7EkDEWLXe_xn3YZhOZc80VE2mOpkXYmcE4YXePrtvnrH_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d0c8a57f.mp4?token=XhNgj4xIQ-jmmpblBOu-AX1V91yW1vqZkz8a8t2WGvSPjlKTHznXr2LKo-KHtvWKebbrTdFEYek9ZabtcQu1g3jwnvG4fYXcYuCaiRxWhAJ96847ROykFKhp8jWsmOFmOveBdgD4Jm6gBvKAMuU1xuixvK7bfn3mw136LsGpnl14sx_xehVq6LsW7IMqM1BE5sOxI5ptF-0BzUrM1uimkPiO4MeFQAEjJ7nM0lJxP5j811kv9lYeoGLpawEE90rgM1mzoK_wX0LasR1TeHcEFbSi_VQ4-hCPVoD23Pe-7EkDEWLXe_xn3YZhOZc80VE2mOpkXYmcE4YXePrtvnrH_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سه نشانه که بیان میکنه یک نفر به شما احترام نمیذاره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/698481" target="_blank">📅 21:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698480">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
قالیباف: هم می‌جنگیم و هم مذاکره می‌کنیم
🔹
یعنی در زمان لازم با تمام توان می‌جنگیم و آمادگی خود را بالا می‌بریم، وقتی می‌گوییم هم می‌جنگیم و هم مذاکره می‌کنیم منظور این نیست که جنگ بی‌پایان انجام می‌دهیم، یا مذاکره همیشگی، بلکه منظورمان این است که جنگ می‌کنیم تا دشمن مجبور شود به خواسته‌های ملت ما تن دهد و اگر نداد، شکست را بپذیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/698480" target="_blank">📅 20:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698479">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a3ba8961.mp4?token=S-_pMzQVX9ukoYZnNs52zCoiZl8ykHrFd4SzWLudFhJ8q_xkEDclfORsx0pAv90_Kd2jEIpyOQzVlJd1FGs652B1nMTkJkfu8pHKw5votWGxXaqwkfANcO_ImRBf6_cCllW2CVy-j27jq7AbP4Kwght-1DYCadJ3LyHH4sqTnrUzNBvUODVQuhIlqPhxqZWyvGpe52JwBBFHKGrbXpyx4RzB44Kev--DrmAGc0qqsvTLaUA9uLNvsyXoxrsdeMTUdoXf3PgSjuEUhMxpE5cu22Sjb8cMMgaXVhxMIF3tRTyLrFxHiUjT0TwLPZnIamoBZs9W7fPI9dGrw0vs4kegYRIDXYIdT_NXPvysAHbPKQtuNGxV3G-VYt4UOSYyY9VOwvSNlZ9fiMXxYahMKcT5UMDLz3tAFL5uPr28s3ej02mUfnUVPU-t_RlO70sjhwwxdfOotQbSoHWzkK0ZfEgvS6dC8Ke9FWHtF4_RA3cQ64MFtPeErrVA0nOVbxCAfCP60dZCaXsUkQxjaUXwElHdcNl4Wn3n3Ce45EwxzBe7L8WXZOgRaNs2HafNhW2o2ufy-LPqMHwwYapQYtpXjZt0ifAS-GTPedlVJ4WvCdUgAYk8bKhj35v-r1JWCTSm93f3G_HlaLSPHZKQyw4NqTVmKIc7Nv2P0ZWWcsNhP9wzzXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a3ba8961.mp4?token=S-_pMzQVX9ukoYZnNs52zCoiZl8ykHrFd4SzWLudFhJ8q_xkEDclfORsx0pAv90_Kd2jEIpyOQzVlJd1FGs652B1nMTkJkfu8pHKw5votWGxXaqwkfANcO_ImRBf6_cCllW2CVy-j27jq7AbP4Kwght-1DYCadJ3LyHH4sqTnrUzNBvUODVQuhIlqPhxqZWyvGpe52JwBBFHKGrbXpyx4RzB44Kev--DrmAGc0qqsvTLaUA9uLNvsyXoxrsdeMTUdoXf3PgSjuEUhMxpE5cu22Sjb8cMMgaXVhxMIF3tRTyLrFxHiUjT0TwLPZnIamoBZs9W7fPI9dGrw0vs4kegYRIDXYIdT_NXPvysAHbPKQtuNGxV3G-VYt4UOSYyY9VOwvSNlZ9fiMXxYahMKcT5UMDLz3tAFL5uPr28s3ej02mUfnUVPU-t_RlO70sjhwwxdfOotQbSoHWzkK0ZfEgvS6dC8Ke9FWHtF4_RA3cQ64MFtPeErrVA0nOVbxCAfCP60dZCaXsUkQxjaUXwElHdcNl4Wn3n3Ce45EwxzBe7L8WXZOgRaNs2HafNhW2o2ufy-LPqMHwwYapQYtpXjZt0ifAS-GTPedlVJ4WvCdUgAYk8bKhj35v-r1JWCTSm93f3G_HlaLSPHZKQyw4NqTVmKIc7Nv2P0ZWWcsNhP9wzzXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا مطلبی: انعام فقط پول اضافه نیست؛ احترام به زحمت آدم‌هاست، و اصالتت رو از رفتارت با کسانی بشناس که برات کار می‌کنن
🔹
برای ثبت نام همایش بزرگ استاد مطلبی در مشهد از کد تخفیف BMT72 در لینک زیر استفاده کنید
👇
https://evand.com</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/698479" target="_blank">📅 20:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698478">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b81b63d6.mp4?token=g5bhV5vc2bv3owryNdzNcqnOOifzxOYHo7quN5CzZj-D6TO9kyjIT2Uuu454o9b-q3XeRTY0zOn5n38K8wQq5-h8PTLvvh9GyC_psmGVJNYo_yZS2t3szdxDY23OGcBUyhVnZVH1GOy7tbxlGnXl8JQhtQUQJuAzkwyNIhNxbnoG5Ww5IYVj_pypvqBzYt0GNJrlT3YxUJVmE9nBkfLbdR7_jgNJ-GoAjTolBF6rHYfTOgj-Pe_kMqVNFPdcJGYW32Kdkb7k4caBqTpMa6xfFFRVc3sxDIV3z3UgydAbKxb0gCm4CvycL7n82XN1BVtLWQR1yztaAnEinXwOU9yvRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b81b63d6.mp4?token=g5bhV5vc2bv3owryNdzNcqnOOifzxOYHo7quN5CzZj-D6TO9kyjIT2Uuu454o9b-q3XeRTY0zOn5n38K8wQq5-h8PTLvvh9GyC_psmGVJNYo_yZS2t3szdxDY23OGcBUyhVnZVH1GOy7tbxlGnXl8JQhtQUQJuAzkwyNIhNxbnoG5Ww5IYVj_pypvqBzYt0GNJrlT3YxUJVmE9nBkfLbdR7_jgNJ-GoAjTolBF6rHYfTOgj-Pe_kMqVNFPdcJGYW32Kdkb7k4caBqTpMa6xfFFRVc3sxDIV3z3UgydAbKxb0gCm4CvycL7n82XN1BVtLWQR1yztaAnEinXwOU9yvRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلنسکی: رئیس جمهور روسیه درخواست ترامپ را جدی نگرفته است
🔹
روسیه شب گذشته و ۲۴ ساعت بعد از اعلام آتش بس ترامپ با موشک‌های بالستیک به تأسیسات انرژی CHPP-4 در کی‌یف، پایتخت اوکراین، حمله کرد، یکی از زیرساخت‌های کلیدی تأمین انرژی این شهر.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/698478" target="_blank">📅 20:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698477">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHXCmGSS_VL3TCf808A-MYUxSZllPG2MitCWWHyNbE2ChRGfSavdunepQ-L04Afd4r7TZl2pq5FZedJSoawo4g4UXMv-4TkqCHW9ZZzJv1fWkGIMj6OlNN4BKM4xj2VgoUe7l5VYoLWHgVcAaeEKycZxK_7ebtNSnaHwmwV7iEZhRhnjEs1wtw2pr57CaR2skuCntG89o0apavf4TO-ykdmqfBsl3yBIyq0jd2TFlacNv8BFg4h1ZD8j9lZ7DIa8bD2htOurn7kD43SqKpJi3MCct_VTs8h2TIo4shNyce4-_nSgWvv-zz7w1wchtE-brcixYKnPcR0addae36frng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناخدای هرمز
🔹
در روزهای اخیر، افزایش موارد اصابت به نفتکش‌های خارجی متخلف در تنگه هرمز، معادلات موردنظر واشنگتن را با چالش جدی مواجه کرده است. برخلاف ادعاهای مقام‌های آمریکایی، تحولات میدانی نشان می‌دهد که شرایط منطقه لزوماً مطابق خواست کاخ سفید پیش نمی‌رود. تداوم تنش‌ها و اصابت‌های دقیق ایران در این گذرگاه راهبردی و عبور قیمت نفت از مرز ۱۰۵ دلار، نشانه‌ای از نگرانی بازارهای جهانی نسبت به آینده امنیت انرژی است. در چنین شرایطی، دونالد ترامپ شامگاه گذشته با لحنی تند اعلام کرد که صبر آمریکا به پایان رسیده است. اظهاراتی که می‌تواند بازتاب‌دهنده افزایش فشارهای سیاسی و اقتصادی بر واشنگتن باشد.
🔹
هشتصدوهشتادوششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/698477" target="_blank">📅 20:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698476">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IudZzyDP0EJNcPDb6-CbQgCYC2nrOJ1LdQawVru4nruYdviZB9eZZl0-C9esmE1O8Zjxryca4JjO3UYPMONKx-tmHHcTkDmR12P1b46BkDSPrf0dkLZw56IDL605aXm3AtDuNcqNUkymaHr4XkrAsMivvI8GjpYL2TR0n1dysAhuls9tuxGi-sl0EeQNl9LjZQWW6KgRzlGSioM_F6_j3kVhU06D5txCIt68m0rWricmS-ciODZQnHypdugkSwcyaBmMA2tvlwbSY2x8zwiJy7H4L4Mx5C_bTqmJnu-UbezGcGNeKUcHl28handsHbQprAGnIs9t4Wy7i-0_IapzwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰۰ ابزار کاربردی هوش مصنوعی!
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/698476" target="_blank">📅 20:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698475">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKhnhlR0X3RcxF4Efi-Dy_Eu9N9FY5pvxD-xpJu94HZiXnuJnmYod-f1pVVrILBRCNagg0ZOWMNh0Jy-uKo5V52djqvo9BIGbUK266DJaWn_HAg6KDy-Dcwj0TipdFX9Y58Dti8YyNN_OBFdXQM0vZndmRJIxVIPTa6GjTuTo79aoLOkmlVXRlLjEt0Jkm7XXfmIR5Q-_Fyj1imyfaOS-aTqaOUlMGCtPdxJqnKjrrvFWD3rl6HBFd0mUjmAAkO9R1vEezTJhR9WyymJJ4OBZpN1LP--ZC1GJcq4EGn7qQ7UE4VfGs1TIJcC7QkWTI7sTcC8w_ZqIvzZocVF7iko-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روش‌های محبوب دم آوری قهوه
☕️
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/698475" target="_blank">📅 20:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698474">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e081c75715.mp4?token=p96oweBADphvcGMA01zI4F6QPmZswbluHHSShgOa-ES2-l4dMexWCNbe2910SlNIMANJl8WvBIv6rwhdrUB0Uas6AXI_dt5kFgmHhxxljNJydpoUGOTXwXHfmJDzRb_pj847wt56zU_nhcULp30C5gyCcgP4gmLNLRp68FzI2FOt2XMWRB0Scj1ee9tmX7MXrcjUaC4V4Rx91R_AY_8XVTUr3XT5-ViN6f2iCpuxZeFelTIDx_EiDbaO1LRsf2ll-sb1-y2bxO7a0GdtGkvl8z4PZRx-IVsOhfe-YWMeEhI2r3UkvqrqiaHfV5hPCN3t_DSZdV6Vrl1ykPNRKi1pxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e081c75715.mp4?token=p96oweBADphvcGMA01zI4F6QPmZswbluHHSShgOa-ES2-l4dMexWCNbe2910SlNIMANJl8WvBIv6rwhdrUB0Uas6AXI_dt5kFgmHhxxljNJydpoUGOTXwXHfmJDzRb_pj847wt56zU_nhcULp30C5gyCcgP4gmLNLRp68FzI2FOt2XMWRB0Scj1ee9tmX7MXrcjUaC4V4Rx91R_AY_8XVTUr3XT5-ViN6f2iCpuxZeFelTIDx_EiDbaO1LRsf2ll-sb1-y2bxO7a0GdtGkvl8z4PZRx-IVsOhfe-YWMeEhI2r3UkvqrqiaHfV5hPCN3t_DSZdV6Vrl1ykPNRKi1pxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: نیرو‌های مسلح حمله دقیقی با استفاده از موشک‌های بالستیک علیه تاسیسات ارامکو در ظهران و ریاض و همچنین فرودکاه ملک خالد ریاض انجام دادند؛ تمام اهداف با دقت مورد اصابت قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/698474" target="_blank">📅 20:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698473">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">26-1 Ane Manaee (1404-02-15)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/698473" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وششم؛ بخش اول
🔹
"إِنَّ الَّذِینَ ارْتَدُّوا..."عِقاب و عِتاب الهی پس از تبیین کامل هدایت و اتمام حجت خداوند.  [01:08]
🔹
تحلیل مفهوم "تسویل نفس" و نقش نفس و شیطان در پدید آوردن تصویرهای ذهنی غلط و سناریوسازی‌های نابجا  [04:12]
🔹
خودفریبی و توجیهات ذهنی در مسیر مراقبه و محاسبه. ..اصلِ فریب، باور بی‌چون و چرای ماست به حقانیت خودمان. [16:40]
🔹
بت شکنی حضرت ابراهیم علیه‌السلام ؛ لحظه‌ی بیداری وجدانها، و نقطه عطف خودآگاهی به اینکه "ریشه ظلم‌ها در خود ماست."  [19:12]
🔹
از منظر قرآن بازگشت به خویشتن و مراقبه دائم نفس لوامه، عامل رشد و بیداری، اما در فرهنگ غربی نشان بیماریست. [26:50]
🔹
توصیه آیت‌الله شبیری زنجانی به جایگزینی اخلاق و انصاف به جای فضای تهمت‌زنی و بدگویی در حوزه‌های علمیه [37:10]
🔹
شهادت عمار یاسر در صفین، روایتی از نقش القائات و تصویرسازی‌های باطل در وارونه‌نمایی حقایق  [42:45]
🔹
انکار نفس و خودبرتربینی، ریشه همه جنگ‌ها و نزاع‌های بشری از قابیل و هابیل تا تاریخ اسلام و ادیان. [ 48:10]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/698473" target="_blank">📅 20:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698472">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDyTLRr8cEtSxDt044PibirEGlptA5DUnXqgna7ga-G79txuT-1gvIDMYQttAxOjDNa9kBT0pXIdbcnvDQW8D509MVF2MuDDwAoklcs0aJpEKwwDgfOTktF816ykQWydg2O0mcV3rg_YyoxuZjDQMB5T9JgmmhTCVLAsrOnZE5f6lp1m3Et10NP9PNtDcW_Q76bUuyfx4iO4_80dkhNuYYHtCNzQ05ZvYs2RZGQYmERjT_1i50g_BXecYbBOUH5St4uYJeFbGhrVdk2lW1bCly6nW-qm1V9X-kQGDRhpAS01wGLi1VSE5gOSi6MPzpDdICfRcIrjch430oCxeJxTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر رزمنده اسلام یاسر باقری، اهل بم که امروز در درگیری با گروهک تروریستی در منطقه کورین زاهدان به فیض شهادت نائل شد  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/698472" target="_blank">📅 20:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698471">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxy9p13rEfn95LFc7Sc4Mk-LWYSEiz3fNk-C7KgTn5jIjDQWWtqyisPdb44MuZ_m8UhP68tMYeN21qa0LmQbPRbkF5V0QDUqSU2K9ML8PczHKc0g9WBuYXofk7H85x9gJUWetzM8H3FCq3pAMXI0IJXNsWKwoUTM1cQhcKrrwq18Ae8pmJQ6TCfLKijyy8WigpNfrn8PA1CgIBkRR7Buz6Gtx7ym5BQ_bxoCRZulQew8BqicsGU-z73iTSY5yqP1-bxpeXBu9h6TwQ7HzrTBNvA2Yk94DZKOcv1Z85VqLtbKwa_1M1ZBePNM8P89VbV5ifKY-B1lpb7LSyyTvJWixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ چگونه سعی می کند از
شکست نظامی
،
پیروزی شناختی
بسازد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/698471" target="_blank">📅 20:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698470">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb10134b1c.mp4?token=knoAOCB0Azut8ZHnve8tOw0IYE9OKMsGI8fYfiwExFryuoIgqHM_EiNMRQ8bkEQUGMjDRogimc5cD2_ulUOK5ePswipvSxjks3YC-CdwkpZPVzb0VPFXyO56k6bqWEvGRChNLVGIXZUH6nD_JXSWkd1bbKHig1PefYMc6vogVafw9nv181lseatsSRd0o4aFJWj6d4qlhPP9abV4rzt2A8MyqmvRdTP2jAoDYDABRqE4N4gRQ-oVCmWega9eBactgqHm_NKG977RjuNjmQv_pW6uS5z6KZaiC58kyNK1ii_nYhPZS-I_dQiQv0hTmjUN5nLxkmAFjKyrI8PpABGtiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb10134b1c.mp4?token=knoAOCB0Azut8ZHnve8tOw0IYE9OKMsGI8fYfiwExFryuoIgqHM_EiNMRQ8bkEQUGMjDRogimc5cD2_ulUOK5ePswipvSxjks3YC-CdwkpZPVzb0VPFXyO56k6bqWEvGRChNLVGIXZUH6nD_JXSWkd1bbKHig1PefYMc6vogVafw9nv181lseatsSRd0o4aFJWj6d4qlhPP9abV4rzt2A8MyqmvRdTP2jAoDYDABRqE4N4gRQ-oVCmWega9eBactgqHm_NKG977RjuNjmQv_pW6uS5z6KZaiC58kyNK1ii_nYhPZS-I_dQiQv0hTmjUN5nLxkmAFjKyrI8PpABGtiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی سفیر جدید آلمان در تهران از آغاز فعالیتش در ایران؛ «از کوچه برلن تا چای با نبات»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/698470" target="_blank">📅 19:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698469">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
فرود اضطراری پرواز تهران - استانبول در تبریز
🔹
پرواز شماره ۹۷۰۰ ایران‌ایرتور با ۱۱۶ مسافر که از تهران عازم استانبول بود، به‌ دلیل نقص فنی ساعت ۱۸ امروز در فرودگاه تبریز فرود اضطراری کرد.
🔹
تمامی مسافران در سلامت کامل به سالن ترانزیت منتقل شدند و اقدامات برای رفع نقص فنی یا تأمین پرواز جایگزین درحال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/698469" target="_blank">📅 19:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698468">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
‏
سردبیر میدل ایست آی با اشاره به جنگ احتمالی بعدی: ایران اینبار همه را به جهنم می‌برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/698468" target="_blank">📅 19:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698467">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f171fea18d.mp4?token=WTEor_ULN6RrmbocrnaEIn9D-THJnPRyfHhuU-qeNhT_1h4FFwGmFVOt03yWuxb-4JbsRoiJA5CBmVvCj3vBQN8atnUtnR-3tcd9LIM_iS6LhTzZZKrfiwFFIFj9x7PW3BOD4lz8ROMqJ9TqWUVGmTkGh9LnpeJpI1YO5zYPdi9dqwAQWb-KXAvGJVAHP7DC5MPmeWr3HfDzzXJBLeXoCRPjcsEldCezElTT2YwsyAPyORDnj1gI5YeH0TOpPgn_6fLMINkA9kwt6t3KEBJ8r-R2NUORH7iphPAqvitxt0jaOuv8wNZqc4YUgovd2TNAFsm0Li6HeOpkCUusei4uiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f171fea18d.mp4?token=WTEor_ULN6RrmbocrnaEIn9D-THJnPRyfHhuU-qeNhT_1h4FFwGmFVOt03yWuxb-4JbsRoiJA5CBmVvCj3vBQN8atnUtnR-3tcd9LIM_iS6LhTzZZKrfiwFFIFj9x7PW3BOD4lz8ROMqJ9TqWUVGmTkGh9LnpeJpI1YO5zYPdi9dqwAQWb-KXAvGJVAHP7DC5MPmeWr3HfDzzXJBLeXoCRPjcsEldCezElTT2YwsyAPyORDnj1gI5YeH0TOpPgn_6fLMINkA9kwt6t3KEBJ8r-R2NUORH7iphPAqvitxt0jaOuv8wNZqc4YUgovd2TNAFsm0Li6HeOpkCUusei4uiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به آتش کشیده شدن تأسیسات سری استارلینک در بلغارستان
🔹
یک نماینده پارلمان بلغارستان از اقدام خرابکارانه دو فرد ناشناس در تخریب و به آتش کشیدن تجهیزات ماهواره‌ای مرتبط با جنگ اوکراین در نزدیکی صوفیه خبر داد.
🔹
افراد نقاب‌دار ۱۱ آنتن از مجموع ۱۷ آنتن استارلینک را در یک تأسیسات سری در نزدیکی صوفیه به آتش کشیدند. این آنتن‌های ماهواره‌ای از خطوط ارتباطی مورد استفاده در جبهه‌های جنگ اوکراین پشتیبانی می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/698467" target="_blank">📅 19:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698466">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_oRg_SEWOhWm8_4LRf5K2NP2uSpiXW1kSvn-N3vc50r45LVOD3t4GN_7t_pSrS6nhkvZD2k-jntj3kuRdB-Uakh4D2Jbl2I07J5klQXBg88tyCTXg1Us1-1DAtv-VLLDAMyZdqMOI8GLJhy4Dse_gRp3GqymHa-mvSp-BQjUiIdgLfSvhkLwG6Nb8oYRMTOjFRDoIZwQbh0HVNK6ZK51Kbo0L4r7R-CKzSZTr5mZ03An20mnmWhnfZdSm8nwAeewsXsqKR9fIVMlJGFaX3E8esiTyVHEloigxLdf3nsWi348CtCfgYrjKxLMpb2dK7x8nWO0vTI7JZvKmakp6AqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلاش تمام شهرداری کرج برای روز فرهنگی ایران کوچک/ مسیری آغازگر برای احیای هویت این سرزمین
مهرداد کیانی، شهردار کرج ضمن گرامی‌داشت روز فرهنگی کرج و تبریک به اقوام گوناگون ساکن در این شهر:
🔹
امسال شهرداری کرج با همراهی اعضای شورای اسلامی و هدایت فرمانداری ویژه شهرستان، تمام ظرفیت خود را بر برگزاری باشکوه روز فرهنگی کرج متمرکز کرد.
🔹
این شهرداری اقدام به برپایی ۵۴ غرفه ارائه انواع محصولات گیاهی، صنایع دستی و... در محل محوطه تالار شهیدان نژاد فلاح کرد که اولین نمایشگاه تخصصی عرضه محصولات بومی محسوب می‌شود.
🔹
همچنین هرشب برنامه مفرح استیج با گویش کرجی میزبان شهروندان ایران کوچک بود. عصر شعر نیز در دوبخش شعر کرج و شعر با گویش کرجی به‌عنوان یک جشنواره تخصصی برگزار شد.
🔹
مجموعه این اقدامات و تکرار هدفمند آن منجر به احیای کلانشهر کرج از منظر فرهنگ و هنر خواهد شد که در عمل آغازگر مسیری برای بازشناسی فرهنگی ایران کوچک محسوب می‌شود.
🔹
روز فرهنگی امسال تجلی اراده همگانی دستگاه‌ها، ادارات و اقشار مختلف مردمی بود که توانست حول محور معرفی بیشتر ظرفیت‌ها، فرهنگ و تاریخ کرج قوت پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/698466" target="_blank">📅 19:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698465">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سخنگوی سپاه: احتمال وقوع جنگ جدید کاملاً وجود دارد/ آماده‌ایم به هرگونه تجاوز، با قدرتی بیش از هر زمان دیگری پاسخ دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/698465" target="_blank">📅 19:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698464">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaU92x88Q4E_QllGqJ9aEKHdnx2ikKVOYfkVG_0c_S2TYljJSa1u5pxK7WLc5v2mvjsw5UtHAYgS2uz5GVN8-nnn8fvoIQLz6u2QwaLTM4kr1e69sBeG1Nbzq34AAHeIbR-cR4w9KBVXVz0Zh-6eHm3xQ6Asui9eAglHE26QMufeZohB64Msl1eXuPn5tuXv6oY-sfro1SYYP0iR8jhDVTYFBLcw7G8ko1HawuDTlL1Ao4Zcr133rME_fL_KPiy9k8Tlg0FkrspKToDYRUwV_EmECWlET4ANkZ6-PUTfiwDPsOBTS8dmb0tDnzK3ci4ApsTMFzNssP2-z6o5cB1k5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از دیدار امروز الهام علی‌اف رئیس‌جمهور آذربایجان با رئیس‌جمهور اسرائیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/698464" target="_blank">📅 19:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698463">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac361504bf.mp4?token=FRgzkmAhCEFaqQZLmwM9RooQ3kdO4OTRhDZdMnjFYTW0sGNJVV8xO7m76irBbXnBCm2GFgUoIs2l5p1bIsY7N0EqfVcn8Bzh_nqiJPQgA1w2RnxBaJessDH7AWdEoySqBl9AQe8n6wFrSI4H00x1NXsAWl8eh2auggiwjavakXozZ0JosfrVmP99sFkVeXUe5t4lCZLXH5kvclTXj8XEmUfXfwtAW6cr3Ip5xVHAj04VZ6g4TRkT2aRRXbfvVbKgFk7pYpHlGjqXoGRNdSTQqfmQLumc-Fg4VsHrEPF_535a37JLAVmVtWbz82gZFiLgHE4Nc4Pg4WUDbLGYUVegww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac361504bf.mp4?token=FRgzkmAhCEFaqQZLmwM9RooQ3kdO4OTRhDZdMnjFYTW0sGNJVV8xO7m76irBbXnBCm2GFgUoIs2l5p1bIsY7N0EqfVcn8Bzh_nqiJPQgA1w2RnxBaJessDH7AWdEoySqBl9AQe8n6wFrSI4H00x1NXsAWl8eh2auggiwjavakXozZ0JosfrVmP99sFkVeXUe5t4lCZLXH5kvclTXj8XEmUfXfwtAW6cr3Ip5xVHAj04VZ6g4TRkT2aRRXbfvVbKgFk7pYpHlGjqXoGRNdSTQqfmQLumc-Fg4VsHrEPF_535a37JLAVmVtWbz82gZFiLgHE4Nc4Pg4WUDbLGYUVegww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعید لیلاز: آمریکا پیش از جنگ به ایران پیام داد، کنترل نفت ایران
را به ما بدهید تا به شما حمله نکنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/698463" target="_blank">📅 19:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698462">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c371b5163a.mp4?token=EUWQaEzAkL8iBRu5RXDpdPEW6sQXhIYPTZR5G1xfJIDNHNQ_2l4PWbPeRE0YHjNFrgGcUZJls5ROdp5-rMGtxPV4XFI3rlv1h-taZET1YhToaaZCWmxmmXvSz5DmBX-tP52tVu6GOkUQakFGP5kFS19cVeWC7l1nzeBefE8-vBZENfwND83ePDItIELKbkeH6WMTEYAbFpm4QBNK9lhWG3Suce-jpMN7KejIdiUCmZ-fKaLxjHNrvR0-D0CAH3wbzeICSSrysfJt1reECTYP6pX-2bGsCnatbThOXfu387-ikQTi_zJjuWWgqVg26g1NL8sQFr-gGw_6kJJv_BrVC7dFJqXqOvOzRZcdCU7X_65FsrK3n_07KAhS-ntDK5faFior4mZCoQoBo6i2hkUEbvqEQ8uZp1shXCPehpaO6J74SyfO2NLT0X93R06o97TPKgGKbDXROiyOzP3ZJo1SG-qgGBiTrORXgkPyEtsixMjsPLIVEEzFtjcGnZlEMM_GymAKR7y0mIU_xONacQ09wCvTWV8_C9FJ0OCf8oU3JDUuV6InZtxEoixuATKtuwi399inILDubWhCrH4GCva9v4nQRbPX9XNNWsYq2eS6u-JwD15wZkOuAWgkdqp8jU8DqQsR6_9aCbWecL7VzcxYmbOmqrGxUldjbSo9gP0LFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c371b5163a.mp4?token=EUWQaEzAkL8iBRu5RXDpdPEW6sQXhIYPTZR5G1xfJIDNHNQ_2l4PWbPeRE0YHjNFrgGcUZJls5ROdp5-rMGtxPV4XFI3rlv1h-taZET1YhToaaZCWmxmmXvSz5DmBX-tP52tVu6GOkUQakFGP5kFS19cVeWC7l1nzeBefE8-vBZENfwND83ePDItIELKbkeH6WMTEYAbFpm4QBNK9lhWG3Suce-jpMN7KejIdiUCmZ-fKaLxjHNrvR0-D0CAH3wbzeICSSrysfJt1reECTYP6pX-2bGsCnatbThOXfu387-ikQTi_zJjuWWgqVg26g1NL8sQFr-gGw_6kJJv_BrVC7dFJqXqOvOzRZcdCU7X_65FsrK3n_07KAhS-ntDK5faFior4mZCoQoBo6i2hkUEbvqEQ8uZp1shXCPehpaO6J74SyfO2NLT0X93R06o97TPKgGKbDXROiyOzP3ZJo1SG-qgGBiTrORXgkPyEtsixMjsPLIVEEzFtjcGnZlEMM_GymAKR7y0mIU_xONacQ09wCvTWV8_C9FJ0OCf8oU3JDUuV6InZtxEoixuATKtuwi399inILDubWhCrH4GCva9v4nQRbPX9XNNWsYq2eS6u-JwD15wZkOuAWgkdqp8jU8DqQsR6_9aCbWecL7VzcxYmbOmqrGxUldjbSo9gP0LFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی آیة‌الکرسی به عنوان ضد طلسم در موزه‌ای در آلمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/698462" target="_blank">📅 19:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698461">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8513fdb997.mp4?token=chYEgqvE14z5B7tezVo8CEnWeiaJHA7DYI5GAT3ZW7w2zSDYFZrHKXatMySnSEMVB2IaivW4jTRSJkeHyxFXJOvIP4RRwfu-VZbbgfHugiz6aYhbsNqAXeXIFxYx0FUROWY4h-UStjghRMQwd4NzGCr64IIZ5cBeMGbjlK8GbQCr4e-zw1RUvayY7rY28lgdhxAoVAlZT09djScLTW8ac2FeylpYkQWebZYolSL2Dk0vXVavlwUpmkvXSWKwooXvXZ5G4DXKW4WJgWoJZjnDu7yDtGIYdANDcpJ4fUUFgnn96y2U33BCcyI5237Egk4losD5nOHWImnTlMtnNH97nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8513fdb997.mp4?token=chYEgqvE14z5B7tezVo8CEnWeiaJHA7DYI5GAT3ZW7w2zSDYFZrHKXatMySnSEMVB2IaivW4jTRSJkeHyxFXJOvIP4RRwfu-VZbbgfHugiz6aYhbsNqAXeXIFxYx0FUROWY4h-UStjghRMQwd4NzGCr64IIZ5cBeMGbjlK8GbQCr4e-zw1RUvayY7rY28lgdhxAoVAlZT09djScLTW8ac2FeylpYkQWebZYolSL2Dk0vXVavlwUpmkvXSWKwooXvXZ5G4DXKW4WJgWoJZjnDu7yDtGIYdANDcpJ4fUUFgnn96y2U33BCcyI5237Egk4losD5nOHWImnTlMtnNH97nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا هوش مصنوعی جای فعالان صنعت بیمه را خواهد گرفت؟
🔹
فناوری و هوش مصنوعی در حال ایجاد تغییر بنیادین و تحول اساسی در بخشی از فرایندهای صنعت بیمه هستند؛ تغییری که می‌تواند نقش شبکه فروش را نیز وارد مرحله‌ای تازه کند.‎
🔹
علی الیاسی در گفت‌وگو با برنامه سیمای خانواده شبکه یک، با اشاره به روندهای پیش‌روی صنعت بیمه، توضیح داد که با توسعه فناوری، بخش بیشتری از فعالیت‌های اجرایی و اداری می‌تواند به ابزارهای دیجیتال سپرده شود. در این صورت فعالان صنعت بیمه فرصت بیشتری برای تمرکز بر بخش‌هایی مانند مشاوره، ارتباط با مشتری و خلق ارزش خواهند داشت.
🔹
در این ویدئو، علی الیاسی از چشم‌انداز ازکی‌سلر برای آینده صنعت بیمه و نقش فناوری در توسعه شبکه فروش می‌گوید.
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/698461" target="_blank">📅 19:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698458">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVHV1gatxGYJz69rLvnc_JFxKKa43eqLgvPGpAONpornEqOFC6R8ApQH88FnbyeyU_s0gtcua5uUdf9FihsIMTvlsfATRc0MjdJog2Awec-i4VduQuRkSZ9soGNW-HOc4EA3JEhn9m8iy1UcixsgZ8sMbtOKfNnDZhacWLDuLae_qjrf_wthdqldyWsynGtkNcyrOV2ph8wyZyAcGyyLzAVVvLdzTZG7jdToZoo2SfO-01QQIkwwu2vjugQTyQxv1waXsKyv3fcax-5G6WUXphyl9x10ZlLE37t27XZclP2mRZBLXCmFEjMefuU9GszoYbwDPZ1z47WF8dQZEMUDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFxtf-uZMsY-jLO_K0uy6UWU1k3MWXoeu-5szI5CLAQwNc5uGALktcTpra1bUwuETHyVkN09TN9uohkQONhr_HynJ-1la9saNDDlLHa70joQIJcfRQWzD7egBqfd8aD59DkBkanYPLCiU-r-uDSkQ-8jBL0xcCMOLNK6YGUwCqUhLdo7jLXp6ovtk-tZ2diHnlJfY0koqxLcgEPfNCO_JnbkFwXLhybGUAgwo8hp6_dePLW1Hc7SvWQCbxuqPmy5VZ652QJSdR7NLyoc2qmNKjZrOkPNqwtxEoEe6Fwb8RnIgV_bf4huyHb7OkS_sTK5IsBvVMmM4af8ch074DPdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVp8JxKyJkPhpwc6qBOBGIeoadD-w0ROO_kcgOJ8OUFy-JlVNWpycBIwpyk0J-1Fs46Knj-EyaggUVaSnIO3RitMvHApAHMr12aJCRDd-eAp6o9l3xunkzI3lO8EchUiKjcgRFTlewYziUTGX_3_l0FZEpR8OzDhX-Ntehu2YfLTCUIL-SwOJAPEy6Z1QiWfO2RWSVXwOYV1gCre2USjXNqfSkcbz3aOkeTMtYf6MDK-SjwIdvY90mJ_KgIOiRKY9GVp1YDKUkvL-N3dVk-NQlM3HMXk5ODy5Qkm76H80_SbBXL93aU2Ewwez5cDDGac0JnngMiNCOuLrwpr7sDz_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روستای تیونویک؛ حدود ۷۰ نفر در آن زندگی می‌کنند و آنقدر دور افتاده است که به آن، انتهای زمین می‌گویند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/698458" target="_blank">📅 19:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698457">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOb4MlbTxG-gFCeXJb7CQDOA5LpVZ5u1uIpK9FvxRvghlki4JhuP4yYIxDDRyEncXFqPKZN4cLpVg8DQlh73Hrtu2a3zZduqua6GIiX2CYOUr5bQKRsQL7T3fxn8UlR-c9M3_Ai3lGcJSoq7lWQj8_jYqmLrh7wnMoQ0TL1tt1r9s__aYa30L-McsEDfF-nsh-tNoEpVaPeaXYKeZiaO2KlTgh_AE-48gQej-BPvi1Aui_HHEZIqxOnR_HGc1KoP2U0plhRRYViWSCO2B5xNlMoCUR5DtbGJedb7qTPT1624tYD4AKF9igLW9vAWfNSbe84_xme_-AVszA8_jc6WuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انگلیس و آرژانتین در آستانه جنگ/ قدرت نظامی بریتانیا بیشتر است یا آرژانتین؟/ آیا لندن با این سلاح کوچک غافلگیر می‌شود؟
🔹
بریتانیا در جزایر فالکلند حدود ۵۰۰ تا ۲۰۰۰ نیروی نظامی، یک اسکادران جنگنده تایفون، سیستم دفاع هوایی اسکای سابر و یک ناوچه نیروی دریایی مستقر کرده است. این نیروها برای مقابله با هرگونه تحرک محدود آرژانتین کافی به نظر می‌رسند.
مقایسه تانک‌ها، جنگنده‌ها و ناوهای لندن و بوینس‌ آیرس را در گزارش خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3252451</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/698457" target="_blank">📅 19:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698456">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlYtxgaf0mviHO6SHSLbpkoCJyymqdOAHoJb5nB19lKcFrywzH1qssL5zvRkDyDg08fdMVULaOTYAo__lxYEZZHuQfyqRa3PyukZgjGUUGrUkUKDL5yvc1JFgrlwZ5B18A0ExY-Aa1dWvhDc9ACZJEfFEDAVo6F6gTZ_qzD9uGPTG97aQTeVF7TEDCNlJCNe7SIWrAMD7HgJyI6k_YZfZSXdfX2qzOUzYQDHOIRKMGn11lrEVu6_wEN-PwhsBlTlEuTCRr89K6FiGCRCidZ4TrJPinKRtXoj3KQCSMJf1Haet8SGW1bA878h41cZqYrMKq9gyme4rSvr30n6slB5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار خیبر و پرسپولیس نه گل داشت و نه برنده
🔹
خیبر ۰ - ۰ پرسپولیس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/698456" target="_blank">📅 19:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698452">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVTcwz4xYX538QBINoYSArOjOHglN_oYRsn-Gtcgp5L-eikJGk8rxFFXsvDgP2rSU74oNm1qMT3OAckvw6MANIJWbIat3mPscWcQBq1PiG3b76MwQheW6oyWGXQ3x0MRjVISgvfwEWGsqUpi7nTmYUCD4XHDXt8WMJvuPCHd4soIBSK1Ac6_2UfhZr0J1TY_TXq19igvUT_GuuoFpHI-V2aVoH5sx-HFQRrMUjUP0ueaZHdrNvdzfwl0KTPIU1WqyGYWufFKQO4Na5K0Z5o2ETT2EBJcPV-_FOdZfnaSxg8CKAigZRrpfIYVM9D934HcXFTxB7LLA_VjxEx3K5U5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ygl0jvwQqwgYZxY1lq4SxM3KMpexzUwgYUpEfSZ9F7Jo7R1wWy1fvC7Z5wly1ooem6NN8_CJ1kYLfycYzsQWmYw--ZQcMDrW3or8Sgbp1bgmZGwl8MH_5kcOYGF6NLcR7paDxA0ZzXJ-Owiq7fg5YSP-TSex_3orvTi1EsFvjh6QDItyGn3FyK8EjGdDCDxe1XwtFm7Z8jNdVa9RGMGosDE6YasPmqkNVpbilinAIyphEfIN5T3UnWstYpAjmSqDSNCM20dzNk9OXwujTs0hcr_fNw0HeiEAbKQKHyCdEcf-iNoy_b4VAULppRfiyMOaj1OST7LgJyv5sd0TBDNjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knw9x6YXEtmyNIkgNJB7Zimre1e7haluk5xdGy3XDVfPXTpzpi3F13c8SBsyCXe7xKnHd7r-rHoVpXrL1hffYx6Ow5DP3-7BZ6EHLd7YyNSbtO9T6rB68KViltDBhuPX_eH3t9R779YX5lB3vO3L7PYp7QvpgDqhb0oXVEpngIDx-4jLrFswDtQYezGoievo1nG1a1bGYwC0NWcFpZlAp3Y9oReIJUhMadQYVkEvrzIqfZ9anvy24A9IYWGO2ltwuJ3uleDBKyyJySPtp3Y4ugWn-qIuNV_oo0vG7O6uIW1n_IQLCP2ZkP6jJrPjY4jN0OIpjIzIcrlith__aLR5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LH1vfoFPLdpA210LbKSnadMu6NDKI-ASukCBvvim5ORsQBqP3oPwkR5UrbSxNgUN7ai7BWQApkQCpoUjqfJ0Ggr1UjbonaGbaCacRqjJj5Ds1G5MZ-dlvD60ergBi86INwWVNB_diO8dDmJquldOC57LICVUKIgTiuKNjH8FrNCYMr6BZvDoUbG8MxPP4jXtSBrpyz6HUkltXRbkBo2hxhH_FkMqtGlKIx0OWAd2AtUaMziBU9WL9K3MiP2ru_iIx_x3QCCkaVs7kSvm5rdMvJwLkr0n_gBqZ2JuaGzV8rtG7J3Qowb8nytgx6fZ5zyGet2PLYXi0ehkId-AeS67pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا سبدهای سرمایه‌گذاری باید نقد شونده باشند؟
🔹
انتخاب سبد سرمایه‌گذاری فقط به میزان بازدهی بستگی ندارد، نقدشوندگی دارایی‌ها هم یکی از معیارهای مهم تصمیم‌گیری است.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/698452" target="_blank">📅 19:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698451">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
المیادین: ارتش یمن ارتفاعات مشرف بر شهر «تعز» را آزاد کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/698451" target="_blank">📅 19:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698450">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba056aa6e.mp4?token=JOHEYnDJS7coZDWwk8p6lajJEi4HiPOhpeAkVLc-9D7qXj2Cq4K1gjmxA7L3FkeaIYuGvCHUE_J78IiUDTTiPaP8jD3KTzKwmQlKN4k2DbX9qqZxzBGxkHqEDJqxS8vvllZIxnIrUli-g0GD3j0OAM3wGOmTSwB5YJpIS5U6C7TP_gTq3_ZTa0GJ9DDgrIbidUlWD_TafE_aN893lnmuM4hVW7mV1-FVnphegqnzGQ-uwcmgJ84quwzplNzhNh_xJZED6Oor1TSxL5k9ztPQgUefxUM_6Y8dhnWLG1rfAluAn8gpot9Z3C4LukmsFCb6zgcJerBVzsAlAQtHk5XxwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba056aa6e.mp4?token=JOHEYnDJS7coZDWwk8p6lajJEi4HiPOhpeAkVLc-9D7qXj2Cq4K1gjmxA7L3FkeaIYuGvCHUE_J78IiUDTTiPaP8jD3KTzKwmQlKN4k2DbX9qqZxzBGxkHqEDJqxS8vvllZIxnIrUli-g0GD3j0OAM3wGOmTSwB5YJpIS5U6C7TP_gTq3_ZTa0GJ9DDgrIbidUlWD_TafE_aN893lnmuM4hVW7mV1-FVnphegqnzGQ-uwcmgJ84quwzplNzhNh_xJZED6Oor1TSxL5k9ztPQgUefxUM_6Y8dhnWLG1rfAluAn8gpot9Z3C4LukmsFCb6zgcJerBVzsAlAQtHk5XxwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبدیل یک ستون ساده به المانی چشم‌نواز با کمی خلاقیت
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/698450" target="_blank">📅 18:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698449">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">همیشه یادتون باشه، ما صاحب داریم</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/698449" target="_blank">📅 18:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698448">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
نام برج میلاد تهران تغییر کرد
🔹
بر اساس حکم صادرشده از سوی علیرضا زاکانی، برج میلاد تهران به شرکت گردشگری و تفریحی میلاد تهران تغییر نام داد.
🔹
در حکم شهردار تهران، ساماندهی و توسعه گردشگری شهری، معرفی ظرفیت‌های تاریخی، فرهنگی، گردشگری و تفریحی پایتخت و احیا و بهره‌برداری بهینه از میراث فرهنگی و تاریخی، از مأموریت‌های این شرکت عنوان شده است.
🔹
همچنین عباس حیدری که پیش از این مدیرعامل برج میلاد تهران بود، بر اساس این حکم به‌عنوان مدیرعامل شرکت گردشگری و تفریحی میلاد تهران منصوب شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/698448" target="_blank">📅 18:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698447">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
سازمان دریانوردی سنگاپور: دو کشتی‌ کانتینری طی دو روز گذشته هنگام عبور از تنگه هرمز، مورد اصابت پرتابه‌های ناشناس قرار گرفتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/698447" target="_blank">📅 18:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698446">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QP8LFkytJwEpaljUI2osCFzgR7MTf47ccJXwxsFuVz0w-MfSXTovJd7_NxvjaJQ7bmNl2ITP4-7b9syGtpD1ejbu492_XFwciDi_ssRGc8FZZylyp-zKWu6zmL8aUqzu8cA5JvW3Za1H86WiORGgdUVH018ON8kKRLqFSXx1NA5hbq8ZNDPKt-OkmRb5qQGaiVr8z5cZ5IS07-cYOiYCWEDFrbkupaRqnxUq0w-l2l6XczzcXfhpONOXEdyblIzpJ1Z6jahUrGATHJ_kql42Y84stwUQCFj1e4JuPWAVThrG5dvMyE5zyKYSomBa8aJGlv1srbB2gczlgc6jBJ9nog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور وزیر پیشنهادی دفاع در منزل شهید نصیرزاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/698446" target="_blank">📅 18:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698445">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Y-oODL4pLc3TaN2FULH_76aCi0UsokC0flKy3jvJ7PQ1BdE1a6dA9WyF6o6Le8AWMAbCDIbBJDyivOqaUVeyxuNM108SD1_NP145BwGK83KOJjlR4BxDj0bcO4XK1FfG8Q-XwPsT4g6YLC6_Ucd6m6-yVHJOE_3AnCSw-5ZcOdLlj9Ue_KRBCqbQT0YL0TdXlbqzrY585hOj9RyiJZfi-ufX3BR1013aY6ljdOGIYRlDLwg3x3NZlhmxVsBokL0090_aDSmSgGEO5oGChv_cfxUma1ts-k3tB8RI6zynFxu7QJDzC_03PUK4f0g-UkyUGCw3jqUfNhSc2Zf5IIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تورم آمریکا در سپتامبر به بالاترین حد خود در سال رسید: ۳.۷ درصد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/698445" target="_blank">📅 18:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698444">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظرتان بزرگ‌ترین مانع تردد مستقل نابینایان در شهر چیست؟</h4>
<ul>
<li>✓ پیاده‌روهای نامناسب</li>
<li>✓ حمل‌ونقل عمومی</li>
<li>✓ موانع و وسایل موجود در مسیر</li>
<li>✓ بی‌توجهی شهروندان</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/698444" target="_blank">📅 18:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698443">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
عراقچی: توقف حملات رژیم صهیونیستی و پایان اشغال لبنان اولویت اصلی ماست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/698443" target="_blank">📅 18:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698436">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSNYiHdBuv8IbvBkSFGtw465EgsFPDygkbhN0cRIMe4f-bO0mivH3hL9CAYxqKba4V4S0Pv0s3l0VtbjPgNnIfJo90yEGpwNiOadn_prBRyJ1R2m8Eqf6Gr9N2_7PD2xk3PSKq-aumtkUfhZAopD58Ufa3JOKa4TS8x-7OE0yzFrvPkxmh1N3ZDGhiC-BZe3dBdqO5A5JhuZh-gvxAdrExnqqDL2orY_8eOxx7SyNPl_74bEYBm9Iq14DzUYYRLA4ZZrNpVXnleh1fjPovRX_5sKo16341HlC3wf6ohMR-gwxlViZBAEe12HtSgePdJaR3qqs9N-xLj5tun-x8NDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSm4uRmv_KG9orh-zW9kCnCMDfUXQHRkn5nZGdVBNPp3nDQAJ9giXtKq4H-n73T8HYvIhSlhdrQGQggMLvdC68LiZF-8XjaGNls7m0l-i1hPHuuY5pZJQByfFB83VdicYRj_myqMke6XbVcDTVgRhJVczFqXLsdw1r-pV9U9nnXKVihMoLANmzQN0T94cNoLdOfLy2wzDqyLj9gQBSyJw17h-dCzR8tb_7bSDqRiS1lqwPSnnRH9qp8p6jbN__058Tyeic2yQFc10xXzdsZqe6vlft-iB1t-OH1GfNLwRwNyCFlneCRCO5oTaG_iVlG8qm1n3gtQgrJTJNGJKBNVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhZchwybymKQQLCRvumqzJ64hNVBPL9YVuo2vZL-fOC0_BW7kh98VID_-hs9kqD4ElbEyxDXUBmtiMtTAf6zh_Da-rCE1ADxoRmWRFzBLGue9fA6BeIeWv-j3XQndWfZmfH963CDHFloKtjv1v5z4oQVpE4rNuHt5Gj8L47IoaDbNmFTnzvfWS5e4cncTDIBW2OHR0Dr54OWG7xTjyt5VjklzM-RYvFRyC3KVtm-MKbpMFzbN_01EHk4--XxC0xstf2K1nN99De6ffQK6pXIgNVZAsyg8hB_AZKu5PyyPnEZE5BAbGxoc-rGV3jJrQWNx5JQ7mYP6MjptKYWwFTcyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-RoG2xHMLnbvm-t04J5MWTyiDDI90xHuNdxujM_DI7ohbsI6yRgQCCEQsHB_41pwqLGBcOUE3vOb7MTPk3Wmj50gDs5Cm-PfuGfP4jMhu4Hz4nSLS7_m0_lGiO_sMq2IKr0mkOwTH6V8kCRiS2hMJ6cH2L2eBWc1XxIi8zMVldnw9pKqmiWXxFTcJHTvgPfhUCytGs-mHow89XUM-F91TLrATVpvn_GDEJH5GfgWbknBS0_TeytVuv1HaNaE4Bw_LRpuDFAVHoj5bjT3ldC6-Ngeo1lYsuAMZnSc7DUUE4c9HfjWvGomoeHwDxSWuhFlbAA44fjtae1rDygPQV6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1oZ6PE-7ZrHFy0xsuXag6MILk1XitRvymVJXFRAgchR1J1CEbdyuaxYkhNNuS662MjoQUlx7FCOiPm4UwcAROSvOpLQwzkdD6ptleHnJb4YD3_iHRrQO3yNdnRUniB7iZ9EzbnX_JaG7D5WEZfV4NZ4bu0cnIuQKy8NUCl-qcVwpHV2TGZpapHGveM8w4XDIrlk31v5SRbFiHuoWXTP5vEdyaGvVtrcaKSXWg4fjATFLxrx9yDTy9R_cTMI8f4NXaxIx-S-X5CmE8nZlEEAzmqvGdXZVtFjurXZduOmidwXI9Y49FZciNahCZzqQw22XwmV1WdSuNdARL5uvBkSVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmU83yOf8Po8B92yrdYbK-HWxA0sI3HjGTc895rwR9YTmnYWujOWUTxpqeRTrbVOQiw53p6-evJatv_6n3r6Z1M5yo20ji0fcQivFD9_aa9lAHtJUZR-ZkuIPIkKiOauZY6QpprfwFk5RcdmhzV0BuyHRqOnaNAVOlJIguJ8AT7ppSanHlxLqIfyOF7p6OG64zW5vW96zsxxd1nIlak46DRjwjovb6RQ0UhLfDFdEZVqYrSU4Q64SXQXWEgMLpawZhI1D5vptNGP8qd24JWUzuHzXSe6Uc8GxLwt8-x58Mo0hyBFOmSM3W63Xw_mHrtHK-dwBkooxQ1e2-YvTQRsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVKMONllGdT3Dz_xsxZQ0aTorrBNAK6NLpMrMUKjWtLrzL-WSU9XUIZhtRipHPIRAue3TT0izHgDBll-I2DBGcLG1AF0Ktv2vQBtXDtxqfz5Y6NHv1jav0kel3vXfzNwUbMj5eOxLV2mESwBEjh02ciINJN1aNJiwrxeGwJAm1SdIBIazAgqAVzAn6TmVzoMDhvrLaZkriEWCCkEBW3FG8jbN46XMNZCWyuDN_QkJMMpfEguQ8B00nA105OP7AG0tZcM1Xl0jDyoO_Q51sWEWZ2fvh3HsTEsdBoTMvbHoAGPZEDkFwCkJ5GmX_CO31AmTe1cVLWWWRFTjgCLHv7AqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرهنگ لغت آشپزی؛ معنی ۷ اصطلاح پرکاربرد که شاید ندانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/698436" target="_blank">📅 18:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698435">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
بازدید شهردار منطقه ۲۱؛ محسن امیدیان از شهر خودرو تهران
🔹
مرکز ثقل صنعت خودروی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/698435" target="_blank">📅 18:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698434">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFAKOOR | فکور صنعت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e637c05d77.mp4?token=T-9rjmRQu5Lx7mroAUCszl3Ot0N9dvr9bWWpBuy5MzwsBjikct5VI8zD89oFPAaun_mEK0Zk0H9eAcwIxy5vNlwEJ3ush0Fj6DVP6xjipk3y4s5wgSbHpN_qhSbm6gad4peG1CMHx9NdS_4qijay4p5LMnxz8X0YtzGEgLHFOJil6CjQJEsfKGw3_VzqdlaflGtYp08FTO31h7DywNXykOGyIN9wurjwBXoaQvXln4NosLHw-nsQ7sXiByqh6akXNIymKchYi6PfhVyUu2l_LDi4mNxgSc_IdP4ojduCHuUKVn_nCY0_UzuBOaMhDMzzJfcGCNJDiDmUQt7X4aTSFhvZI67lqTlH-VjYoLxGuerJ4xOxXg8A_WGhvd8knJcKz5V8rCcIcbWc8bPOCGzsGgZWoTQUtu7G9_BWZf8yewdN9q3H6Fr4I7zJ6D9Zuojzwtjbvsrhhkq0IcdcEe1qH0AQGmQEbEcc7ojZqdog5Ct4Ba7qaV6_vLjsUAt7tXYgswl88n0zSUq9iOt4pDMazOPUOiP0iBHrVhhI88rJ96l3eH1DLkU1VSNIRuYIUQw-zpxT3n223RIcNeEavo6HRhfn-4yEt7WVcubb7SUOpqYmCXlK9pYAnvrlk32tneQEuEQZSedETlBjOWUjRSEeDpTUhy38eadGSt0__uiGKkk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e637c05d77.mp4?token=T-9rjmRQu5Lx7mroAUCszl3Ot0N9dvr9bWWpBuy5MzwsBjikct5VI8zD89oFPAaun_mEK0Zk0H9eAcwIxy5vNlwEJ3ush0Fj6DVP6xjipk3y4s5wgSbHpN_qhSbm6gad4peG1CMHx9NdS_4qijay4p5LMnxz8X0YtzGEgLHFOJil6CjQJEsfKGw3_VzqdlaflGtYp08FTO31h7DywNXykOGyIN9wurjwBXoaQvXln4NosLHw-nsQ7sXiByqh6akXNIymKchYi6PfhVyUu2l_LDi4mNxgSc_IdP4ojduCHuUKVn_nCY0_UzuBOaMhDMzzJfcGCNJDiDmUQt7X4aTSFhvZI67lqTlH-VjYoLxGuerJ4xOxXg8A_WGhvd8knJcKz5V8rCcIcbWc8bPOCGzsGgZWoTQUtu7G9_BWZf8yewdN9q3H6Fr4I7zJ6D9Zuojzwtjbvsrhhkq0IcdcEe1qH0AQGmQEbEcc7ojZqdog5Ct4Ba7qaV6_vLjsUAt7tXYgswl88n0zSUq9iOt4pDMazOPUOiP0iBHrVhhI88rJ96l3eH1DLkU1VSNIRuYIUQw-zpxT3n223RIcNeEavo6HRhfn-4yEt7WVcubb7SUOpqYmCXlK9pYAnvrlk32tneQEuEQZSedETlBjOWUjRSEeDpTUhy38eadGSt0__uiGKkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت فعالان بازار سرمایه از عرضه فکور| حسین عبده تبریزی
حسین عبده تبریزی، عضو سابق شورای عالی بورس، ورود فکور صنعت به بازار سرمایه را اتفاقی مثبت ارزیابی کرد و ابراز امیدواری کرد این تجربه، مسیر حضور گسترده‌تر شرکت‌های پیمانکاری در بازار سرمایه را هموار کند.
🌐
www.fstco.com
⚙️
@fakoorsanatgroup</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/698434" target="_blank">📅 18:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698433">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
مرکز فرماندهی نفت عربستان به خارج منتقل شد
رویترز:
🔹
در پی حملهٔ موشکی شب گذشته به مقر اصلی شرکت ملی نفت عربستان (آرامکو) در شهر ظهران، بخشی از وظایف این شرکت به دفاتر آرامکو در نقاط مختلف جهان منتقل شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/698433" target="_blank">📅 18:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698432">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6c5f4dd8a.mp4?token=dFK9hKppar_Evu8mE84DJCM9vAeNmVTaOwj5F9PbLO3Du3waozRRA5s1RRAzYbfjleRBtgu38K98WOrTtTsFv9VcprS4aJ8rAkkU0386EabzKSiRI5X-VHWjs0ya4pfV2aRcTwQkBsRSojGMr6lykBd6gzYxtcx2PuhdfrCagMiD-33wLtRXRHrrqrsIkDkHe3uIxkzafJnoiH8Rmtd0hrn6y3zEjUrS4A1gLNYY5-HTn7LmqaZ19cv9OqHCqan0Yjp1rqGZGZRTVcD3cH3FbUjVFXZvaMcUqiPYUW9YXQ3avzVO3YVAj1aovZyEVMiM9sLdYiyrHuM2-TUgE2phwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6c5f4dd8a.mp4?token=dFK9hKppar_Evu8mE84DJCM9vAeNmVTaOwj5F9PbLO3Du3waozRRA5s1RRAzYbfjleRBtgu38K98WOrTtTsFv9VcprS4aJ8rAkkU0386EabzKSiRI5X-VHWjs0ya4pfV2aRcTwQkBsRSojGMr6lykBd6gzYxtcx2PuhdfrCagMiD-33wLtRXRHrrqrsIkDkHe3uIxkzafJnoiH8Rmtd0hrn6y3zEjUrS4A1gLNYY5-HTn7LmqaZ19cv9OqHCqan0Yjp1rqGZGZRTVcD3cH3FbUjVFXZvaMcUqiPYUW9YXQ3avzVO3YVAj1aovZyEVMiM9sLdYiyrHuM2-TUgE2phwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنرانی پیت هگست، وزیر جنگ آمریکا در طول یک رویداد، طی پنج دقیقه، چهار بار متوقف شد
🔹
معترضان فریاد می‌زدند « کودکان در غزه گرسنه هستند! او یک جنایتکار جنگی است!»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/698432" target="_blank">📅 17:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698431">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جامعۀ مهدوی/ج۵</div>
  <div class="tg-doc-extra">استاد علیرضا پناهیان</div>
</div>
<a href="https://t.me/akhbarefori/698431" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جامعۀ مهدوی/ جلسه پنجم
حجت‌الاسلام پناهیان:
🔹
4:30 پیشرفت معرفت‌ها نشانه نزدیکی ظهور و فرج است
🔹
12:50 وضعیت مسئولین در دوره آخر‌الزمان چگونه است؟
🔹
18:30 اهمیت شناسایی نفوذیان داخل دستگاه مسئولین
🔹
21:00 دعا و توسل را رها نکنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/698431" target="_blank">📅 17:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698430">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d514d3eba3.mp4?token=Sny6JxJc3EpEfFJ78nTht_1pOW2TNIfPSNcBfMhX4LIxqdPzUjfwCFdKPmJ7CKXUv8BAgsvLVwM3Hc_NfOfrUFGrCkI7jRpsIozgP9iuXKdhwGRON8CQiZ7H6VivEV13omIEVhXSRipehbi8S_fs-bPJfDp3hkuwKtpQhrnGADwAmdYlHVwQMv9NCZifxO-N355tfadQg9qB555Zv6_77YrzVtZh31zPoWeJZ0zmyp3Zjlq1w4l_-bW-N8sDF2bwxCNnc48zt9_UsFiM6_iy9D7dNlaUF1MdINPWHXIbVNuHHLwfJ4Riz87Q0sqQAGZhYDC6wNO0-V8ab8rdOpQFeVbWNNCMZwb4XAcWnfyRzAkCiyjHNXtxeNCdlgMAGHJy6qsvPLlCLetukAm6coh3KTcKe2_y41sTFU6xMS1O_HwE9NaHjwqVEL4RVBGU8qTVRyRqNGIlUQ0WNV1OfrV8YEh9pnH_aoYHU6KMW74nNoojTgmeXMGwS43-KP2EAMjT6k0m_e3HnzGs5kq4aaMh6i8GGjniM22VWk90Q83jJBJJxPJ4uZbYSemnnzpq0Jg10EMvbCVkFnsaCzpSvN6uOLL4NT-M0U8-29MslAwVfjRtMSWUOWduO-9WOoS1lc6aea8Jpegi4FsK8MdRJAxG1UgiDY1Kf0H64Cg-nfW60NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d514d3eba3.mp4?token=Sny6JxJc3EpEfFJ78nTht_1pOW2TNIfPSNcBfMhX4LIxqdPzUjfwCFdKPmJ7CKXUv8BAgsvLVwM3Hc_NfOfrUFGrCkI7jRpsIozgP9iuXKdhwGRON8CQiZ7H6VivEV13omIEVhXSRipehbi8S_fs-bPJfDp3hkuwKtpQhrnGADwAmdYlHVwQMv9NCZifxO-N355tfadQg9qB555Zv6_77YrzVtZh31zPoWeJZ0zmyp3Zjlq1w4l_-bW-N8sDF2bwxCNnc48zt9_UsFiM6_iy9D7dNlaUF1MdINPWHXIbVNuHHLwfJ4Riz87Q0sqQAGZhYDC6wNO0-V8ab8rdOpQFeVbWNNCMZwb4XAcWnfyRzAkCiyjHNXtxeNCdlgMAGHJy6qsvPLlCLetukAm6coh3KTcKe2_y41sTFU6xMS1O_HwE9NaHjwqVEL4RVBGU8qTVRyRqNGIlUQ0WNV1OfrV8YEh9pnH_aoYHU6KMW74nNoojTgmeXMGwS43-KP2EAMjT6k0m_e3HnzGs5kq4aaMh6i8GGjniM22VWk90Q83jJBJJxPJ4uZbYSemnnzpq0Jg10EMvbCVkFnsaCzpSvN6uOLL4NT-M0U8-29MslAwVfjRtMSWUOWduO-9WOoS1lc6aea8Jpegi4FsK8MdRJAxG1UgiDY1Kf0H64Cg-nfW60NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرآن، معجزه‌ای جاودان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/698430" target="_blank">📅 17:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698429">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
یک منبع نظامی یمنی: به سهامداران شرکت آرامکو توصیه می‌کنیم سهام خود را بفروشند تا در روزهای آینده متحمل زیان نشوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/698429" target="_blank">📅 17:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698428">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
معاون وزیر خارجه روسیه: در صورت لزوم برای انتقال کامل ذخایر اورانیوم غنی‌شده از ایران آمادگی داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/698428" target="_blank">📅 17:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698427">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKQ8uF-7RJjYDcg1sR42gdj2feW5lx3RMDpbUQUxAEQfuS1x51oZ73h8cp0HJVCkMTm0GRiqSuU_mzZ_24Sy7KCuk6v0WQQ9b9C84aU_PIm6oAAy4XiqDFlj7fF4ejovYw7KxzIa9pe_EDdBSEXf43-cUTW2-DIk5_H1RC8UnE8oTU9uSUYiWE5Nly7cYFnUMcH6fVUtHZj2Zhq6l-qQtDkWS55-wo08H5fRkEU4eb0mlPrUsCZz7MEJClLKi7TSCj7LwRBgf0siINskft6sESHr16d7-SBWNPMYBKljyNV0nffqms9rt0C2alL62oCN9OnbbBr8JIPEuRQPW5uVKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع کم خونی و روش‌های درمانی آنها
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/698427" target="_blank">📅 17:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698426">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
عرضه مرغ بالای ۲.۲ کیلوگرم ممنوع شد
اتحادیه سراسری مرغداران گوشتی:
🔹
عرضه مرغ گرم به بازار باید حداکثر ۲.۲ کیلوگرم وزن لاشه باشد. ارسال و عرضه مرغ کامل با وزن بیش از ۲.۲ کیلوگرم به کشتارگاه‌ها ممنوع است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/698426" target="_blank">📅 17:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698425">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش عضو کمیسیون امنیت ملی به ادعای جدید سنتکام: ادعای انتقال ۱۹ میلیون بشکه نفت را تأیید نمی‌کنم
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
قبلاً ترامپ آمارهای مختلفی و چند میلیونی درباره عبور نفت از تنگه هرمز اعلام می‌کرد، حالا سنتکام همان ادعاها را تکرار می‌کند و ادعای انتقال ۱۹ میلیون بشکه نفت را تأیید نمی‌کنم.
🔹
هدف این آمارسازی‌ها، القای شکست محدودیت‌های تنگه هرمز و کم‌اهمیت جلوه دادن اقدام ایران است.
🔹
برخی نفتکش‌ها با مجوز و هماهنگی ایران و پرداخت عوارض عبور می‌کنند؛ برخی دیگر با خاموش کردن سامانه‌های شناسایی تلاش می‌کنند مخفیانه و به‌صورت قاچاقی عبور کنند، روزانه فقط ۳ تا ۱۴ تردد از تنگه هرمز صورت می‌گیرد و عبور و مرور کشتی‌ها ایرانی نیز در جریان است.
@TV_Fori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/698425" target="_blank">📅 17:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698424">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
قائم‌پناه، معاون اجرایی رئیس‌جمهور: هیچ مذاکره‌ای بدون تصمیم شعام و تایید رهبری شکل نمی‌گیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/698424" target="_blank">📅 17:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698423">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ثبت‌نام آزمون کارشناسی ارشد از ۱۶ تا ۲۲ آذر انجام می شود
🔹
آزمون کارشناسی ارشد پنجشنبه و جمعه ۱۶ و ۱۷ اردیبهشت‌ ۱۴۰۶ برگزار خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/698423" target="_blank">📅 17:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698421">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rejz6meN98sqBKPTa1L4NjWmZTpEnW-zJI0X_IQCkPor-RzFGQGmVA-3TPFaANfHLaeCena1VACKergfLChU-0Xn7eQ-Ph68ZhQGkKIvjU_ZN4OBhLK0K-ubeBlBMb9TGJVI8wklVPOLHAq8tnm601tdO2YzZmZ43HHCyWFJ2_3zdpctWsN56SPbITSwKbBlGBDrIa74agB32_ItO-KZXvx5UwQc2F4CwFwQheSMkxPBl17oNTkEqFD3Rol9PI5i5X_N2T3hJFBXI8kGjhNH_hPgHwIP7kXjGN2GW8rY-slErazDghWVf5bVhLwpQVX8lHYCFGAwvdrYolTkhacNRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cj8MP6XtlIwu0xu6BiI3ssbS5ujfT24ne5DxXvQ3hLzPqYJNu71l-xMhNCasNdaFtCAFWfzBNzjyh5LLQn9cajHXF9Dw1Qknz4kgm6TBK1Tetn5LyJI0F8Yo7khvxnS2iQvXxrHSBDNIhMM_DAUjY3UbDlrcLcnJBXjGO4XulnzRNa6MiIMaZ77PWq9Ouu3j3ulzBjNtcA-BgVExSVrhMcnzEX6euWlF-LZ0EDeQJK4_9qvQCfUK3wwa6wGL_QXjB56g8t6YnuoN924f1s_BYomjaOKa_62bBKbRIr6myQ08kAIq3-O1sFe7Gbf_rcqR5W0l3C18H-Qz1kHM0TWl4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیشنهاد ۹۰ میلیارد تومانی برای ازدواج با یک گربه ایرانی!
🔹
یک زن فنلاندی پس از دیدن یک گربه پرشین ایرانی، آن‌قدر شیفته‌اش شد که به صاحبش پیشنهاد عجیب ۹۰ میلیارد تومانی برای ازدواج با این گربه داد؛ پیشنهادی که البته از سوی صاحب گربه رد شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/698421" target="_blank">📅 17:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698420">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
عبور از چالش‌های مالیاتی در بحران با مشاوره تخصصی اتاق تهران
🔺
اتاق تهران با ارائه مشاوره تخصصی و رایگان در حوزه مالیات، به بنگاه‌های اقتصادی کمک می‌کند از ظرفیت‌های قانونی، بخشودگی‌ها و تقسیط بدهی‌های مالیاتی استفاده کرده و فشار مالی ناشی از بحران و پسابحران را کاهش دهند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/698420" target="_blank">📅 17:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698419">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیزرتگ گرا(شعبه تهران)</strong></div>
<div class="tg-text">💣
تفریح و هیجانی که تا حالا تجربه‌اش نکردی
🧨
🔪
آدرنالین بالا
درجمع دوستان،خانواده یاهمکاران
🔥
💎
باشگاه لیزرتگ گرا
💎
♨️
یکبار تجربه‌اش کافیه تا ثابت برنامه‌ات بشه
❤️‍🔥
⭕️
راستی!
تخفیف‌های افتتاحیه
هم رو به اتمامه
⏳
✅
همین الان
رزرو کن
که از دست ندی
❗️
📲
Instagram:
@lasertag_gera
🆔
@geragame3</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/698419" target="_blank">📅 17:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698418">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
کارخانه اینتل آمریکا در اسرائیل منفجر شد
🔹
رسانه‌های اسرائیلی از انفجار در کارخانه اینتل در کریات گات خبر دادند که بر اثر آن ۳ کارگر مصدوم شدند؛ حال ۲ نفر وخیم گزارش شده است.
🔹
این کارخانه با نام «فب ۲۸» از تأسیسات مهم تولید تراشه‌های نیمه‌هادی برای سرورها و رایانه‌هاست و فعالیت خود را از سال ۱۹۹۶ آغاز کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/698418" target="_blank">📅 16:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698417">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0gZlHA_vnaYx_6HvQiSpRTTN_65x1xcYfWHdw9FkZLTh5YYr9yPhuVOyicVM93Ny1HFRdrpBY7aI6Gx_Z5nYcrsR7eC5NDAfyF6WCW4eKJ1rgi9GQoBRIqjwm6kCoqJ6Kgpba8TzHeY5S0IQpPzYjPxS4is32v-DX431sZcjs-tSMKYHdSicl7-Wqd7bxfH8qcPAWHf-iMzmOqXMxI_kk5xplJPuyGOyMC3W0ahCubLC-BNQdOmmnk3xdEuIOgbQBy6wKZRiquSP2GnGodDDAcQ_q_Uuo1NbC9xw5qs5OGN3NXqNuQ2zaQWFp79egTXFaoz4tRFf6kjJsD49QkXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌ها حاکی از آن است که آمریکا به کشتی‌های تجاری توصیه کرده است سامانه موقعیت‌یاب خودکار (AIS) و رادارهای ناوبری را خاموش نگه دارند
🔹
ادعا شده که سامانه‌های نظارتی ساحلی ایران قادر به شناسایی و رهگیری امواج راداری این کشتی‌ها هستند.
🔹
این ادعا در حالی مطرح می‌شود که مقام‌های آمریکایی بارها مدعی نابودی تجهیزات راداری ایران شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/698417" target="_blank">📅 16:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698415">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24adb03833.mp4?token=rywuaUYfXQnsxVD7Jr5x-S8J35quFbRPHz_idKC6y_VTlw50_9m2vqZtTm-5jfBWpjSlepEThyJS2hjKYtTUlfhWKlNlhX-_2kINupuGuq6bHW6o3hGBTyGfTvsxnoCXlUhXV6z7s_0xarSUPeYyX7tthfXyg6BbGDF4ouT8d5gJjHL_LeXUh4phRArBn_-COBbFez2PH0eVPbLMOTlJxd1mahJNlVxg8FZyRvsD6d2nD_O2OnOgfBHjCtR0sy4EDd8c1qP23nvUkuoHAM0_LzGOthbqWt350lQ-EXy5QAGv1zG3iddzuTDSkpNbwus2en4ETeGES1z8JIQcrBIYLryfQrBe3bOsZl5-760VNvyTjVbGKvo1aUAwp14TioT5UJQg5WL2qlZzxUgQAlzd90Q3HxPzWvqJ7ZU-rYHcnU8yQluc4TGdqrt4je8-c1xyw5EDs_SHNIan9MkrMg3jap9ktc9amkBnLtfqfTSlPpf6hf_suh3-gZyZ_beJQGGyZTE86b1RF2Cb7GY9R0KFtIrn5n30aYhO6f92aTZNJtSPtNLowgyn8WANTDyrimoJeqUsr4yVT0xkPbSIK18cppg1aNshuUM76ewdXBLl7deB8H_5Li9uGjMSS63ors6_cYHI8nFe8FEfJis4f7neLLncA-hvf7z-H0PXGKHdSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24adb03833.mp4?token=rywuaUYfXQnsxVD7Jr5x-S8J35quFbRPHz_idKC6y_VTlw50_9m2vqZtTm-5jfBWpjSlepEThyJS2hjKYtTUlfhWKlNlhX-_2kINupuGuq6bHW6o3hGBTyGfTvsxnoCXlUhXV6z7s_0xarSUPeYyX7tthfXyg6BbGDF4ouT8d5gJjHL_LeXUh4phRArBn_-COBbFez2PH0eVPbLMOTlJxd1mahJNlVxg8FZyRvsD6d2nD_O2OnOgfBHjCtR0sy4EDd8c1qP23nvUkuoHAM0_LzGOthbqWt350lQ-EXy5QAGv1zG3iddzuTDSkpNbwus2en4ETeGES1z8JIQcrBIYLryfQrBe3bOsZl5-760VNvyTjVbGKvo1aUAwp14TioT5UJQg5WL2qlZzxUgQAlzd90Q3HxPzWvqJ7ZU-rYHcnU8yQluc4TGdqrt4je8-c1xyw5EDs_SHNIan9MkrMg3jap9ktc9amkBnLtfqfTSlPpf6hf_suh3-gZyZ_beJQGGyZTE86b1RF2Cb7GY9R0KFtIrn5n30aYhO6f92aTZNJtSPtNLowgyn8WANTDyrimoJeqUsr4yVT0xkPbSIK18cppg1aNshuUM76ewdXBLl7deB8H_5Li9uGjMSS63ors6_cYHI8nFe8FEfJis4f7neLLncA-hvf7z-H0PXGKHdSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله موشکی و پهپادی یمن به تأسیسات نفتی آرامکو
🔹
گزارش‌ها از حملات موشکی و پهپادهای انتحاری یمن به پالایشگاه نفت آرامکو در شهر جده عربستان سعودی حکایت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/698415" target="_blank">📅 16:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698414">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
لحظاتی پیش وزیر دفاع اسرائیل با حضور در جنوب لبنان تهدید کرد: اگر حزب‌الله به ایران در حمله احتمالی به اسرائیل بپیوندد، مناطق بیشتری را در جنوب لبنان، در مناطق نبطیه و رودخانه لیتانی، از دست خواهد داد
🔹
کل جمعیت شیعه جنوب تخلیه خواهند شد و دیگر اجازه بازگشت نخواهیم داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/698414" target="_blank">📅 16:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698413">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
احتمال گران شدن ۴۰ درصدی اینترنت از امشب
🔹
بر اساس اطلاعات دریافتی از سوی اپراتورها، تعرفه اینترنت از بامداد پنجشنبه، ۲۳ مهرماه، ۴۰ درصد افزایش خواهد یافت./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/698413" target="_blank">📅 16:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698412">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmCN-q1ubV2Vy5t91i5yPgn5hH98fLYtDVdFxdf83z2KkonsjcuniUpoBt2LLSRDF7irZnB6RBbULquQaFsIXxreRKaDxFIgsNRkRslUz1SYrYU9tEf2VdCWlzocuo_-iNyGkNznTEsX8gDWqcgkT9FSV8Ti778j15tn_pPrlRwdaa2e25L3AWRK-nFG6st-Pb8ezoYXm463n6KG7tVRpTNjrUd8cunCcM9XCJhxvzS0tWmEx6Sq_bQuastWNhkNYRPJqNqWUAHgvK6SUN5dx2oiOOTmiN47S0s8Qq6l1AfXwNHVj6XBb-Wtasa5PGegeFOtiGkKKXXkOUPjyIDyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلعه باقرآباد بافق، یزد
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/698412" target="_blank">📅 16:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698411">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
مجروح حملهٔ صبح امروز به لنج صیادی سیریک: درحال صید میگو مورد اصابت قرار گرفتیم  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/698411" target="_blank">📅 16:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698410">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
به زودی پروازهای عمان به ایران از سر گرفته می‌شود/ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/698410" target="_blank">📅 16:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698409">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91920d43b0.mp4?token=NTS-vtCBiN5gnTV8zKBhP4Z97t8Kn1K8ku0K5JAib-xUUdqH5fue3IwNiMVzC2hjZxV4Ea7cFvKokdIvKRhl1YsN2VsVTS3nmukcXIGoIxRisbbJC1ahBXrkPq-_JoWve19pB1fq6hATYuEwmvqckSNmrJlu5HU6El3bUU2IClR9JpiWDkQOWb3fOg4wdo7Rqtbp_plnHhgpza9w2mZGNaCMG0AT_wtXXCf3Y4fEh7LjD7CU92hhBI4GjQUrVLTjvFyy9YMzeITlDzzT_W9uHVAkfl4143b4Xms0VnO5AlRnBXAUbPoK2XRwIIwhgFfd2L52MLABTeybqM6qx41kYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91920d43b0.mp4?token=NTS-vtCBiN5gnTV8zKBhP4Z97t8Kn1K8ku0K5JAib-xUUdqH5fue3IwNiMVzC2hjZxV4Ea7cFvKokdIvKRhl1YsN2VsVTS3nmukcXIGoIxRisbbJC1ahBXrkPq-_JoWve19pB1fq6hATYuEwmvqckSNmrJlu5HU6El3bUU2IClR9JpiWDkQOWb3fOg4wdo7Rqtbp_plnHhgpza9w2mZGNaCMG0AT_wtXXCf3Y4fEh7LjD7CU92hhBI4GjQUrVLTjvFyy9YMzeITlDzzT_W9uHVAkfl4143b4Xms0VnO5AlRnBXAUbPoK2XRwIIwhgFfd2L52MLABTeybqM6qx41kYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو جنایتکار: آیا میدانید در بریتانیا، کشوری که اسلام گرایی در آن گسترش یافته چه اتفاقاتی افتاده؟
🔹
سه هزار نفر در بریتانیا به دلیل انتشار مطالب در شبکه‌های اجتماعی دستگیر و محاکمه شده‌اند.
🔹
البته، فقط از یک جناح. فقط از جناح راست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/698409" target="_blank">📅 16:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698408">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش نماینده مجلس به استفاده از عبارت دریای کاسپین در صداوسیما
غلامرضا شریعتی اندراتی، نماینده مازندران در مجلس در
#گفتگو
با خبرفوری:
🔹
موضوع درج عبارت دریای کاسپین به‌جای دریای خزر در بخش هواشناسی صداوسیما حتماً قابل پیگیری است و نباید در رسانه ملی چنین اشتباهی اتفاق بیفتد که فردا دستاویز دیگران شود.
🔹
ما ساکن مازندران هستیم و دریای خزر را می‌شناسیم، عبارت دریای خزر در زبان همه ما رایج است و دریای کاسپین در این زمینه غلط است و این موضوع  از طریق معاون حقوقی صداوسیما پیگیری می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/698408" target="_blank">📅 15:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698407">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای عجیب سارق خانم برای دفاع: یک سال است ماشین ندزدیده‌ام!
🔹
حضور یک زن با سابقه کیفری مشخص در زمینه سرقت خودرو، در پرونده باند ۴ نفره سارقان مسلح که با استفاده از ترفند طرح دوستی و اعتمادسازی بوده است؛ شگردی خطرناک که در آن با طعمه قرار دادن عواطف و اعتماد طعمه‌ها، زمینه سرقت خودروها فراهم می‌شده است.
🔹
او با وجود سابقه در کمال خونسردی مدعی شد:«من خیلی وقته دیگه سرقت نکردم؛ حتی یک سال است که هیچ ماشینی ندزدیده‌ام!»/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/698407" target="_blank">📅 15:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698406">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e13e23f8.mp4?token=DXiQMTiqmukJ9ccvELOp4dGK6KKb3__5402XVxrBS_6XS4gsnTloIqlIOJ3iNd767Lli6chgYCRxqm0PrZYwPcjIevGpzExFHW9ppCdpZcgRsY7i-P6IoDk5xTu9Zx5MmZ5sDAsjzccfUJ6NPMKvNkD1R2u3O0DZBxoDVbEuJLKNLEDWwsrPqFVOiXw1aNoVc-uY5aKAp6xGuHa6px9gLb1MXfvzLExdkt6uPt2RYo_-tHaEqyuknXbp0PV8SqDQwKeHPYC16IcWC_0U-D5gdImuaY4jNZ4hrvfApKXE76Wh6ml7dG2iwaRO1gXlgu2DT6bbFtPr50qsi-vefb-psA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e13e23f8.mp4?token=DXiQMTiqmukJ9ccvELOp4dGK6KKb3__5402XVxrBS_6XS4gsnTloIqlIOJ3iNd767Lli6chgYCRxqm0PrZYwPcjIevGpzExFHW9ppCdpZcgRsY7i-P6IoDk5xTu9Zx5MmZ5sDAsjzccfUJ6NPMKvNkD1R2u3O0DZBxoDVbEuJLKNLEDWwsrPqFVOiXw1aNoVc-uY5aKAp6xGuHa6px9gLb1MXfvzLExdkt6uPt2RYo_-tHaEqyuknXbp0PV8SqDQwKeHPYC16IcWC_0U-D5gdImuaY4jNZ4hrvfApKXE76Wh6ml7dG2iwaRO1gXlgu2DT6bbFtPr50qsi-vefb-psA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض دانش‌آموزان یک مدرسه به قانون ممنوعیت ورود دختران محجبه به مراکز تحصیلی آذربایجان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/698406" target="_blank">📅 15:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698405">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای نتانیاهو جنایتکار: نیروهای نیابتی ایران قصد دارند در روزهای آینده به اسرائیل حمله کنند
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/698405" target="_blank">📅 15:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698404">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ثبت‌نام آزمون کارشناسی ارشد از ۱۶ تا ۲۲ آذر انجام می شود
🔹
آزمون کارشناسی ارشد پنجشنبه و جمعه ۱۶ و ۱۷ اردیبهشت‌ ۱۴۰۶ برگزار خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/698404" target="_blank">📅 15:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698403">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959217c881.mp4?token=lyfbhnNxakoBv6UXaiiAvQwZbjZeid-xek05HCA4OhGdhh_7MmN8qTRkpK88piqCP1GL2hhzo4yz4k7oih-iBN1AaNpPP5bmGU5GOjMsfFgpGT_VoVCazh4cB4H010PW_TURC9Oj6ICMLhQG50A6iaaXnlUS1QKpAKfqBxD1uznrH6l3EV-ErzPx5WTYYjoYhE9mEZxTwTtAG9lxRcxGhTwrn6kQXTrqcdv57iUheAp3md0uIV0rvYX4QyC3fXt8QawI0jZPVRO1psTc71sSXKRSkpEKpFNUG0m2vGIkNQx21S3-IRuourNykyS9f7ivOiXm-eUX_-b0t99kKSikd4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959217c881.mp4?token=lyfbhnNxakoBv6UXaiiAvQwZbjZeid-xek05HCA4OhGdhh_7MmN8qTRkpK88piqCP1GL2hhzo4yz4k7oih-iBN1AaNpPP5bmGU5GOjMsfFgpGT_VoVCazh4cB4H010PW_TURC9Oj6ICMLhQG50A6iaaXnlUS1QKpAKfqBxD1uznrH6l3EV-ErzPx5WTYYjoYhE9mEZxTwTtAG9lxRcxGhTwrn6kQXTrqcdv57iUheAp3md0uIV0rvYX4QyC3fXt8QawI0jZPVRO1psTc71sSXKRSkpEKpFNUG0m2vGIkNQx21S3-IRuourNykyS9f7ivOiXm-eUX_-b0t99kKSikd4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجروح حملهٔ صبح امروز به لنج صیادی سیریک: درحال صید میگو مورد اصابت قرار گرفتیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/698403" target="_blank">📅 15:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698402">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9885e4f95.mp4?token=s5FYSfGJwDVC-AfHlHnFJS5ILoT0ke7VkT9eTuOvpHCrVxXFON8UtXfAHzQWUpgiadCmjaFx2dfM7zypNNCUGqybMI3DC8HBJA1BtplsEr8e6hant3u4R0OWkPGQWOKVtCTNMFYK1sWBdMqUOQzcNCxcNll7eowjh8A1e4lLGCbucpyDyTP7EPy1bJTsuFAGB4wysc6Y9Kqt-KhxxaXmFGDFOnk4-e9F3_xB-dnCKP-E_f8eszUH34ZD9dQiDMl5uQgEs-O-Wn1kLq2EuMpIwfKs2ifRBVqgjRyY5f-zgM0dGYLYLnrmGbSmzFXsF2NUuXXrrJC55jlaSJ4LKCn3uDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9885e4f95.mp4?token=s5FYSfGJwDVC-AfHlHnFJS5ILoT0ke7VkT9eTuOvpHCrVxXFON8UtXfAHzQWUpgiadCmjaFx2dfM7zypNNCUGqybMI3DC8HBJA1BtplsEr8e6hant3u4R0OWkPGQWOKVtCTNMFYK1sWBdMqUOQzcNCxcNll7eowjh8A1e4lLGCbucpyDyTP7EPy1bJTsuFAGB4wysc6Y9Kqt-KhxxaXmFGDFOnk4-e9F3_xB-dnCKP-E_f8eszUH34ZD9dQiDMl5uQgEs-O-Wn1kLq2EuMpIwfKs2ifRBVqgjRyY5f-zgM0dGYLYLnrmGbSmzFXsF2NUuXXrrJC55jlaSJ4LKCn3uDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیش‌بینی دقیق رهبر انقلاب از آینده فرانسه؛ آشوب، بی‌عدالتی، فقر و تورم و نقض آزادی‌بیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/698402" target="_blank">📅 15:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698401">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
برخی منابع عربی از حمله موشکی جدید یمنی ها به عربستان سعودی گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/698401" target="_blank">📅 15:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698400">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
تکذیب شایعه مشاهده پهپاد در آسمان نظرآباد/ پرنده مشاهده‌شده هواپیمای آموزشی بود
🔹
در پی انتشار شایعاتی درباره مشاهده یک پهپاد در آسمان شهرستان نظرآباد، مشخص شد پرنده مشاهده‌ شده یک هواپیمای آموزشی فوق‌سبک متعلق به فرودگاه پیام کرج بوده است.
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/698400" target="_blank">📅 15:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698399">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN-S60WVQeHDuDc42L2GDOLEOcPUQ2gTxGOPEQ5VFaswVGNmBAXiRSUMp-2u_SQF0XDyrflaRAcKFiQm3AHPdfjfc6tUpVfWhC57MnQ-G9ODbIxZjpvt5O6sb5rCBbizga0OmGyRLltLpRxuqHdMH-QiHP-MgCRjFsqOyCGTccvA3BWm_nuP69WLsbLVAQDTIlGzlhnS5YJ7qDnxDygzx5_iMul4gQSd1CDHMdXNTiI43Hfr8El_1zMCk1PyDcXvuLojHHfU9S8-TIwzO-0JU3X7VoZoIH3Mc9kvNo19UfWXEhaWtdDUBmOvUvYbUWLaWUVv6ezKuXwjIlyVn0PuzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نبویان: وضعیت صادرات و واردات کشور و فروش نفت عالی است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/698399" target="_blank">📅 15:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698398">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
جزئیات مجروحیت رهبر انقلاب از زبان رئیس اورژانس تهران
محمداسماعیل توکلی رئیس اورژانس استان تهران:
🔹
ایشان جراحت‌های سطحی در پیشانی و لب و پا داشتند؛ من هم بعدا از دوستانی که در صحنه حضور داشتند این را شنیدم.
🔹
پنجره اتاقم مشرف به پردیس حکومتی بود.با آقای کولیوند به محل دفتر آقا رفتیم اما فضای داخل بیت، فضای حضور رهبر شهید نبود.
🔹
از طریق وزارت اطلاعات متوجه شهادت رهبر فقید انقلاب شدیم.
🔹
بهم گفتند اینجا جلسه شورای‌عالی دفاع بوده، «پیکرهای اربن اربا» فراوان بود.
🔹
آقای لاریجانی را با موتور از در خیابان فلسطین خارج کردند.
🔹
آقا میثم[خامنه‌ای] آمد و برخی پیکرها را دیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/698398" target="_blank">📅 15:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698397">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
وزیر ارتباطات: در شورای‌عالی فضای مجازی مصوبه‌ای ۳۲ بندی را برای رفع فیلتر سکوها تصویب کرده‌ایم که باید اجرای آن پیگیری شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/698397" target="_blank">📅 15:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698396">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sta0RHChl0ModM41QuOJRd-_ICqglQAXMN5yIbgiOj0Sn7ZTt3ulGzbSwl5STDENVDyweJLWsy6mR8YlkUbBVUItDdM5VeAn6qDYGfRE3SOmFPVro8lbuR3DgSOkHb3YNTPH5NmOsk_J6h3QM7ilHBQGxVxB5VWS2qbFMLPyYLQgmbnygGKX5HBigWsjx4_crU8KsevsmGiowneYnKqltlCEne1_LFLjP8BJspExf2JZrhcHCbE8MXy13BrzGYMvgC1qt5zuQXh-9mTaRQVWEkw5t7qrkdThzk6OtfkKFCPEz0t6t2CJ2rhEqGmeewONZSQUfWBCis2rO5uMsjB5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شمارش معکوس برای پایان اسرائیل؟
🔹
پیش‌بینی جنجالی مورخ یهودی از فروپاشی اسرائیل؛ تنها دو سال تا موعدی که برای پایان عمر این رژیم تعیین کرده، باقی مانده است!
به توییتر خبرفوری بپیوندید
👇
https://x.com/akhbare_fori/status/2110329773155025085?s=46</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/698396" target="_blank">📅 15:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698395">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سایت عربستانی: احتمال تعویق یک‌ساله جام ملت‌ها
🔹
سایت عربستانی سعودی اسپورت در تازه‌ترین ادعای خود، از احتمال تعویق یک‌ساله جام ملت‌های آسیا ۲۰۲۷ به دلیل تداوم ناامنی‌ها در عربستان خبر داد. در صورت ادامه درگیری‌ها و برطرف نشدن نگرانی‌های امنیتی، برگزاری این رقابت‌ها ممکن است از سال ۲۰۲۷ به سال ۲۰۲۸ موکول شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/698395" target="_blank">📅 15:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698394">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d42391a9.mp4?token=R_iAdmjk5BOpVObBu-hjvsUXIMvV0t9FIFf7OYwf9M85QrAttM2NQzq6_rxiGVg8Mm2AnGOgeOujLP0sDRkIZb592Slp3iXN84R0suA0g9RB3R9gh18YWuz6n7FE5vpD9F5HKBDr9NEvkAy7wJQNTfE211HjLFPn1ktfM3KS8mew2wjbMb36NS7yL6OEVpn-klj8fulLhO01kS0YRsNo9MKBam3dRSVUiEBbEUxpYgAM3xtu7mZpwrfR6oIoAWqmXtewfs9H2kViIeVl5o6pxdOH_mKD7YddSQHPmkdM3K2vPKLOVI4eDJUvPUYmZdFL7XnUZMvfup_gfBCVU17dfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d42391a9.mp4?token=R_iAdmjk5BOpVObBu-hjvsUXIMvV0t9FIFf7OYwf9M85QrAttM2NQzq6_rxiGVg8Mm2AnGOgeOujLP0sDRkIZb592Slp3iXN84R0suA0g9RB3R9gh18YWuz6n7FE5vpD9F5HKBDr9NEvkAy7wJQNTfE211HjLFPn1ktfM3KS8mew2wjbMb36NS7yL6OEVpn-klj8fulLhO01kS0YRsNo9MKBam3dRSVUiEBbEUxpYgAM3xtu7mZpwrfR6oIoAWqmXtewfs9H2kViIeVl5o6pxdOH_mKD7YddSQHPmkdM3K2vPKLOVI4eDJUvPUYmZdFL7XnUZMvfup_gfBCVU17dfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس اورژانس استان تهران: شهید لاریجانی قبل از آغاز حملات برای آماده باش به من اطلاع داده بود که جنگ قطعی است
🔹
وقتی داشتم می‌رفتم، دستم را گرفت گفت دستت نلرزدها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/698394" target="_blank">📅 15:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698393">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef27580e36.mp4?token=hBL6u_bnxSV4SovOYPtV6FDpQJhtnnl94UR8BsYobeP31EWgvWjMfYobvjCh3kdMdNps1cOIw0bzzlEe-yu2FhY7_bHL7K9zS1M7W4btppp5A4uX_qqud1BbfgF916oJlPqKtxkQC6ZS3InfxH3oKUti7qJT1HrI7BBGyE03PasF7YFNIYv_lkDr5i6BonlGtLwKJFsouKY1oK644cZozT4msmv4WUZWBT94T6qlkpYh4OaaSgq9CPT1a3nKs71myZtveufNomiTGOkh4Bz4rRgqAEeFGi07S5sp5Hs37OkJSVyiUMh4rHl0NNrb-SxPg5DG6v1wMfy5FZpoo9AYtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef27580e36.mp4?token=hBL6u_bnxSV4SovOYPtV6FDpQJhtnnl94UR8BsYobeP31EWgvWjMfYobvjCh3kdMdNps1cOIw0bzzlEe-yu2FhY7_bHL7K9zS1M7W4btppp5A4uX_qqud1BbfgF916oJlPqKtxkQC6ZS3InfxH3oKUti7qJT1HrI7BBGyE03PasF7YFNIYv_lkDr5i6BonlGtLwKJFsouKY1oK644cZozT4msmv4WUZWBT94T6qlkpYh4OaaSgq9CPT1a3nKs71myZtveufNomiTGOkh4Bz4rRgqAEeFGi07S5sp5Hs37OkJSVyiUMh4rHl0NNrb-SxPg5DG6v1wMfy5FZpoo9AYtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو جنایتکار: این حکومت (ایران) تلاش خواهد کرد تا برنامه هسته‌ای‌اش را از سر بگیرد
🔹
تلاش خواهد کرد تا دوباره ما را نابود کند، حزب‌الله را بازسازی نماید و حماس را از نو بسازد
🔹
برای نابودی تمام این تشکیلات، ما نیازمند سرنگونی این حکومت هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/698393" target="_blank">📅 15:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698392">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvPH0yCkMjZPkOBwRCohxHgC35IzHh2qtd4RAq13ImZkBAzMb2n1auFTTwWHh-WxgE0yBy3DDAyE6P7_VZasXg9C7KR0yG2FQ_mtAkEsyJrJbOSClY-1ODQuOMrEJJ50qyj4zaFf2xOMG3rdW2v8stSuMNponqx-1Rl-HutbQvkjxxGaLiMElmKNrFD6rAzQ2Ibq1VrjIuyTbYfCP0KsPafMyeqUBO6lYknZVM5AOeRPjVsyKZkOCU8Fr2GwL3VWww2K01jqIB9UzBJa2YwFkqaZehSnC-EgpxNJADqQrkR8AEBN6HHp3nUrStCLxuN3dClYDybdBXl04kQI0CwkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت عجیب کارخانه برای ارزان‌ترین خودرو؛ پراید وانت یک میلیارد و دویست میلیون تومان!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/698392" target="_blank">📅 15:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698391">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی آموزش مفید</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzAMuxBlXZ2z0Gz7P_dvQMoQ9tn-SKYFpqhXVcsgT-N7D2wox7z5SIAIxLTNPkPYdPxKDKg5oK0LeX070q3KJxU_p2Wq-S6RjazjoltvfO9eFx0iXorKtOEZdSvRggwP4D2xFE9pnTDK6agb4tLwb4n80IbmtsOhiZF_4bcJtAgrRTRVEgTd8Edh3R3NsR4E95WEmNwid-UgymLYWmckzRSCXBtvLwoNgjFMa3N57_O3OVrRgtDbmLqVNpsCiq6PAEj--FDycdr5qo4Su66r7HUtMXYLkT9VSUIs2S_lOkSS-mrc4srID3AURVc3Q4uFAoQhK_Z3LPTs7A8qMTeIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای هفتمین سال متوالی
نشان طلای بورس‌های اروپایی-آسیایی به کارگزاری مفید تعلق گرفت
کارگزاری مفید در تازه‌ترین ارزیابی نهادهای مالی عضو فدراسیون بورس‌های اروپایی و آسیایی (FEAS) در سال ۲۰۲۶، توانست با پشت سر گذاشتن رقبایی از ۳۲ کشور جهان برای هفتمین سال متوالی نشان طلای بخش بازارهای سهام را کسب کند.
مفید طی مراسمی که در جریان مجمع عمومی FEAS در شهر مسقط عمان و با حضور نمایندگان بورس‌ها، تشکل‌های معاملاتی و نهادهای مالی عضو برگزار شد، بار دیگر در رتبه نخست این بخش ایستاد تا جایگاه خود را به‌عنوان برترین کارگزاری لیگ قهرمانان فیاس حفظ کند.
پیش از این در سال‌های ۲۰۲۰ تا ۲۰۲۵، کارگزاری مفید مدال طلای بخش بازارهای سهام را به خود اختصاص داده بود.
دهه چهارم مفید؛
تداوم اعتماد، پیشرفت و هوشمندی</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/698391" target="_blank">📅 15:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698390">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVPhb4X7m64psbMQrpYx2dzKBfGWLKuYKezQodjjjX_fP0DwYtTu7vW6J_r_4Bcrm5B_3iz7u-9-84hhUfvArLD_eDnGvz6j3SIgXemYC1QSIHh_sMwhMpM9FMmnoC92sQoTw0oTW04Q5LFzcDXIWKpE6zP6H1meEz1JTHaCll4iHb4hWbmiG4fIAky5Mtxa08OmEMpIDuWAmNC-UXIbXa3yFbp3HCLOf5XkkrSWO_kZ-qDD4snMm6FVaVVne2eDsDYGT3DZ5N8wxkrtSkhJson8wUKGmgze-lQvLocBhBxgCTsSiofOX0hEFibnFQlmh6-HXGWJ6NIxH9i2XWL8Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↗️
🙏
جهش معنادار بانک تجارت با رشد ۵۹ درصدی درآمدهای عملیاتی و تغییر مسیر ترکیب درآمدی
✔️
گزارش عملکرد ۶ ماهه بانک تجارت حاکی از جهش چشمگیر در شاخص‌های کلیدی، تنوع‌بخشی به درآمدهای پایدار و توسعه بانکداری کارمزدمحور در مقایسه با دوره مشابه سال گذشته است.
✔️
مجموع درآمدهای عملیاتی بانک با رشد ۵۹ درصدی از حدود ۷۵.۶ همت به بیش از ۱۲۰.۶ همت رسید. همچنین درآمد کارمزد با جهش ۶۹ درصدی از ۱۷ همت به بیش از ۲۸.۶ هزار میلیارد تومان افزایش یافت تا سهم درآمدهای کارمزدی به حدود ۲۴ درصد از کل درآمدهای عملیاتی ارتقا یابد.
✔️
مانده سپرده‌های بانک تجارت با افزایش ۶۹ درصدی به مرز ۱۸۳۲ همت رسید که در این میان، سپرده‌های ارزی با جهش خیره‌کننده ۲۱۱ درصدی به بیش از ۳۱۸.۱ همت دست یافت. همچنین مانده تسهیلات اعطایی با ۶۷ درصد رشد به بیش از ۱۵۳۸ همت رسیده است.
🌐
مشروح خبر
👉
📱
tejaratbankofficial</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/698390" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698389">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaf297e606.mp4?token=k5OKC43vR7e-esim98jSOtAIcTfS05Y8auIjo0yQ7QuTWLafS2-8xW6TLqamBoa7upviAnZtQd5yJBcsFYKFMNWQxeBKJMN7ss23UzjRw-mOT4212VrgNgeTU_L3i1xKEio9snfugrjEz2lho26i3Xx1hWeIfvmuGcG3xRM2j4ZAoJzoW6hXtxTh0JZutGFecfEbbdIPT5BehuuQV9O5s_Ky1HsiWjk06Htj3zRBNC0tvT8i3PUEztJI2N2vrzO10RtyDtn1kHVIE7pqzmSDqgf3vfncHfcoIkYiqv658ML5BfhCJbgC29SnFYqcXbxJmMhQFQsbi5r84TFbrR4DDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaf297e606.mp4?token=k5OKC43vR7e-esim98jSOtAIcTfS05Y8auIjo0yQ7QuTWLafS2-8xW6TLqamBoa7upviAnZtQd5yJBcsFYKFMNWQxeBKJMN7ss23UzjRw-mOT4212VrgNgeTU_L3i1xKEio9snfugrjEz2lho26i3Xx1hWeIfvmuGcG3xRM2j4ZAoJzoW6hXtxTh0JZutGFecfEbbdIPT5BehuuQV9O5s_Ky1HsiWjk06Htj3zRBNC0tvT8i3PUEztJI2N2vrzO10RtyDtn1kHVIE7pqzmSDqgf3vfncHfcoIkYiqv658ML5BfhCJbgC29SnFYqcXbxJmMhQFQsbi5r84TFbrR4DDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس سازمان بهزیستی کشور: ۴۰ هزار نیازمند هنوز پشت نوبت مستمری مانده‌اند/ یک میلیون و ۷۰۰ هزار نفر از بهزیستی مستمری دریافت می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/698389" target="_blank">📅 14:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698388">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNt-tAmuqYEc_goykdIrOFzzOM6G9aMh402b5WPO9qvJZx2YKL3eniKyYb-h_Pr07Ny4dPiAdvikPVS1VtjOlz_uAqpMEhQB93PMDz-jxybsibLzP_9i9s7TPuTXPsoc9CzRBQ8SbsiEFV8bCjOVcodGTQwush8yqP9q-N9dukNEErHoUE2d_alt2XGYZy99nKCJAwvdFF2-nkmpW4PIjBZ4R-xSAy13gTea9PFPnbgZjK7ENBFCHF4RjGG2-NToFhTsl1w6ToMdMmq1e6Ex7NVv5gP75IO4yUiWD12k5AXg5xYuCNQD9NS7XqWPjnLH5adWsH-VAptgsp6Gls_Cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای روزنامه جمهوری اسلامی: منابع غیر رسمی از قطعی شدن تغییر رئیس سازمان صداوسیما خبر می‌دهند
🔹
دوره مسئولیت پیمان جبلی پایان یافته.
🔹
اسامی افرادی برای عهده‌دار شدن این مسئولیت، مطرح است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/698388" target="_blank">📅 14:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698386">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAK1ZTW1JPuG0VbRqHTp7h_nA8RhJ-a7kDZJiR79a0OLuEmZNHU7OmyWyuBo3u3-xOyt2EQRBWAW_MCtqJeZbdBE1bnfhKRE6R7dzuFe3c6l3SLBcOrE3Fv8mTpt7chp1NmYWF14wjqeT4bIu5y2qVqqmBz3m2NvLlZ1SrqZDR92Fvrra0HiLqLM3tv2QzB-lRpKIFcpNL-V2SibfC_as8CSnxswuhho-VyiVNxRV6FFKn4qQ6vt_ZM0LvrXXcBAYaCUvgv8Mvw2Kw-b7PGZNk2WKI4N5kQv4cGLtESHJZ25rp-cbD9m2gz4GShgC-RtRU5Dzhtk-xAMKgtO3jaJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروی دریایی بریتانیا: یک کشتی باری دیگر را در تنگه هرمز مورد هدف قرار داده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/698386" target="_blank">📅 14:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qyCiO3-NuqheLCT8l0gnoHk3CF_NwRQPVdHNvvNq5JO2ByplpszPGLavlGkJql3ystGlQagmN-jzWEAAzOrl8XKc2hqs5UhJ2_AGdQCBUFB1JUAjYakeEacxzUVn2LfnSbWx7aobV79w1Dkx5sJiTwQ5qjPaV_OMSHVDXCgNDJVW2NPIxlLiIH0Sh8cxkRAE2a1c9rLa1rRg3RfNQ3cGbJUgYFWPioC6Xg2fF3sSEsXa97RDnvBwuOE8f8E6XB1ip-SL97HmJhJJ5SItE_2UEwMcbgx5Sp1VyZ_odOqJoywBKrHtFTHZCYOzgzIQEappEU4e8WKbENzcXxZl7uhWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvA7S-I5lWASQvXv1xEIp33TNgtLEEPyykZdXIjNiDnAKRt4JA-l6TXG5Y1jURMQy0qD6Ji_ZTqsJrBRmkGKXxyY5EYF0MnNV3f-3l6jpjNMFDOH35DtJeRfi0W6xq9amO8ZuT-xibEK-OQfMk9kN6ZOWxPAK-ocVP1QmuMAHwcRk7K-zDnkipC4n-ZfCGtYtpz18US-ng0pW2fnvYHZVmZXNApz0xveL54QpBbFPQi-d4KKD6YAvPlX8fUmU6v4nUXMjpzELX_-pLQ0O3_bfpjUDfV32-S0JgNcRl_sBIwpmFmcYxZoKVKTQvsnEtmnYIDscP4w9kRJeN_PncCL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQB0KCMLfNLiCtthOcUCcWG5nK-_FyyonWaXeUgZJyJMcWjzbzKitRI5miCXcakScp5Dzvv4921Nxn3aMGy4myshDxW2QY_BHgqRA0LKMDNb-gY_dA4B_hBUBzUeauxKU985ZHy3SkEK4aJpYnamtDSx1BnRV7ZAeyg-tkM4hKI8iDkD7KkB-DL4Zfv4gIBEq5l2P5hGFhUtbV-D3T-k_eHHgH0CAwCJFJjYvbpxpLT02cmLmMgC-5P804812opBZkelTjFnA3s_dJWR_1jVOJvdD4nJv4pjIxXkZEfDP5XDCB0huw-f70MR5veynRuLJVGx2rJyI2uz_kfaEXdlow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سه تصویر از خطر، هشدار و فرصت اقتصاد ایران
🔹
تداوم تورم بالای خوراکی‌ها زنگ خطر کاهش قدرت خرید خانوارها را به صدا درآورده است. از طرفی، ناترازی گاز فعالیت صنایع را با هشدار محدودیت تولید روبه‌رو می‌کند.
🔹
در مقابل، هدف‌گذاری تأمین مالی غیرتورمی ۷۰۰ همتی تا پایان سال، فرصتی برای تقویت سرمایه در گردش بنگاه‌ها می‌باشد .
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/698383" target="_blank">📅 14:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5bd5cc5d8.mp4?token=RSU5Ffwb54WXYFPbqYwQCCY0vkRaQSrmh-KyBtNhPEINwp-gI7GOWB4eMb5ejS4Ll5IIpi1GHEojoji3fY5MmEoC61X-3BtNTviyhtuSspTXKbdoS3gxzhoE32zZbMh7zpGAfwhyydm6BEH6P9LS4IdSe-gXADiUjRwA1n63fSBULqrZYZ51m83iEIpHN3gT9pbA5LAEV5-gWrZtQBlZCIPVCIBWa0OBsXPCImKvLMUPcKkhiHUMSyosHzAyR6qVzwtI3dKBGDfxH8bPthX1pGQqEc4aGhHsVvPBd9UCBTKPQx1njCxurs66KnK2FlEfXORPnLcIkZ7Ex1XwwivVgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5bd5cc5d8.mp4?token=RSU5Ffwb54WXYFPbqYwQCCY0vkRaQSrmh-KyBtNhPEINwp-gI7GOWB4eMb5ejS4Ll5IIpi1GHEojoji3fY5MmEoC61X-3BtNTviyhtuSspTXKbdoS3gxzhoE32zZbMh7zpGAfwhyydm6BEH6P9LS4IdSe-gXADiUjRwA1n63fSBULqrZYZ51m83iEIpHN3gT9pbA5LAEV5-gWrZtQBlZCIPVCIBWa0OBsXPCImKvLMUPcKkhiHUMSyosHzAyR6qVzwtI3dKBGDfxH8bPthX1pGQqEc4aGhHsVvPBd9UCBTKPQx1njCxurs66KnK2FlEfXORPnLcIkZ7Ex1XwwivVgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر قطر: باید برای بدترین سناریوهای ممکن آماده باشیم و همه، اعم از نهادها و شهروندان، مسئولیت‌های خود را بر عهده بگیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/698382" target="_blank">📅 14:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3CtaNc0kRGpURd680PE5xGEirr3TdismkYnZe2sBwfuxfUMSANpan427LnvJSOu4vqtvEo94-vtmJ0ZpMwJfE9qVO1bazqcojQDbhZRYJJBtiu-DosokySasAe8S8xTO_H7lmf5SWE3WWSZ90lz1axwS5jWdSNu6wiMC38DHqTOE5TK0DniNEZaUTVT2fiJTVESmDpYUwOHIgR_wWhbeedsp7VsFIdJfWaI5ajwStHpJ3JZ97yWEumBzLkKgyeHQH9oko6XTtDJBZRaHA-1xas7ZFOvw1e47I4T_KikhX7seHQH5w_AezJMt0_4_DY5IGqlORK8p7msPaoiOdDudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه‌کسانی از جنگ ایران سود می‌برند؟
🔹
مهم‌ترین پرسشی که جنگ ایران مطرح می‌کند، این نیست که این جنگ چه زمانی پایان خواهد یافت، بلکه این است که چه کسی از شرایطی سود می‌برد که در آن درگیری‌ها هرگز پایان نمی‌یابند.
اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3252158</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/698381" target="_blank">📅 14:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای نتانیاهو: با حمله پیش‌دستانه علیه ایران در آستانه برگزاری انتخابات در اسرائیل مخالف هستم؛ اکنون زمان مناسبی نیست
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/698380" target="_blank">📅 14:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nygb5bC4GbLXrB3LqUQNysW0FHoJqX6qBhnvU6jSnbLL3rsD5g6-rVTR-Wj_cOdH5aqfOekS10kcXeyETUbb1VEqXkZa7EK5cLPcq4mzEnKuNkQirNvrlr5NpBzFH1CtAo9NElQSWWNe2kR7nE1dhWg6-cvM_CQRwH0Iaumx-C0MTv_aFMrskhlKkCqlWO1_CK0PHpAKo7M3W8EGP309vK6Smfxv1u4FA7fApfXltTbhzu8B68PRtKhu7kmvx1lIjxD5paSU9RVTI9TtGncgGFeFJVGbemSWiWIt55Q-Pf2rBWJWGyaAirbdlQsnbjqKfkXdBHeB17iMC9_gLaDQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این کدها رو اول پرامپتت بنویس تا سبک پاسخ‌گویی ChatGPT رو مشخص کنی!
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/698379" target="_blank">📅 14:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698377">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyKyTOwcm2VF9NGGecu_66GGWtUhf5WKBX4IDG-aKK5VcDRI0DOtHOQSc-Ptz6ibheJaCrOt_IIXi9VxVpzMsWzFsfLeQPxhpX4-Bv_JeYRroBYekrxw3AktJpxg4AHweohHL-Nb2Ti6Z_Q24SpVOlK2tLhLIgx6DXDskEtEnimkU_Bf5AYF8C9bdsKJEh4epZLF2ydiBmeIgmEAXA3J2uGhuZLwRCpkHHY2yWPk2DQwRjKhpVZixiXDQOwBVVyOVxhJyaVXDeEB9g-iP-hbR5WkZCDSECuGSIHw3Ut1hx6NliBzsfkOUvnyOZvnjqDIt5DDe3Uc64YqO3WTe8qHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همراه اول به دنبال درآمدهای جدید/عبور از سیم‌کارت به اقتصاد دیجیتال
🔹
همراه اول در حال تغییر مدل کسب‌وکار خود است؛ بزرگ‌ترین اپراتور تلفن همراه ایران که حالا علاوه بر خدمات ارتباطی، روی سرمایه‌گذاری در کسب‌وکارهای نوآور، پلتفرم‌های دیجیتال و خدمات فناوری‌محور تمرکز کرده است. بر اساس اطلاعات منتشرشده در کدال، این شرکت با حدود ۹۴.۸ میلیون مشترک فعال و سهم ۵۴ درصدی از بازار موبایل، توسعه خدمات دیجیتال و متنوع‌سازی منابع درآمدی را در دستور کار قرار داده است.
🔹
از سرمایه‌گذاری جسورانه «حرکت اول» در کسب‌وکارهای نوآور تا توسعه خدمات ابری، کیف پول دیجیتال و راهکارهای سازمانی، همراه اول به دنبال گسترش حضور خود در اقتصاد دیجیتال است. با این حال، موفقیت این تغییر مسیر به یک عامل کلیدی بستگی دارد: اینکه این فعالیت‌ها تا چه اندازه بتوانند درآمد پایدار و سودآوری واقعی برای شرکت ایجاد کنند./ اقتصاد۲۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/698377" target="_blank">📅 14:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698373">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P45UDLVfr-p4dTuEuDcGJnIgThTzjmd9PMG1dbWf4oVuf8w6Jg5gT8qwnRWjstabESiMduDfo3_GFSqcTgJPW_4oZ4EeMNKZxdBk2FUUEIYtOCzy0wFtCjNb0o3WUovyFaQKylTqzzUDCQyw5HNdwrjVWsWFQ2635kItyEBD6A0v7SNGHfoT9IiGqhtmYjLok8DkaWNjq60g5y5i3M2ygWMPQUsSHf78A6rCfcLi3R5huZzWJmtNf6D28BVFDGEOWbK2pLxzZ_5Qp3Izm7CcxE_5jO4FzRM9zdc_iwNgvMyuMY_URslAyUupiujAdT7hcAQJkl1TybeMCnDs9JN0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibD9NJifqhaA7YNrKXbeZoxYRXbdqCN5GMbeew5waNta8MfcD1elnhAkwzJVHISx7VqZ0SSS0uig5Y9TdIg0YmsxxKJOk4ZQw3p9csfTFfdusrnr3puQwEDRhL6jPmIProXHSv3gJV27ychsYApXK47niCQPGmJlg_wwpe50DZ9hraML38tOXRJ4vmCqbgX0sAOr5uFxY4PoSWsQwo63pxDkp4FfbXCJZFGE4qcJe7cAk8S-rugIK5v8jmvk15IC-Okyje_Y4MFCECowo7ogIKzULvQHTMik_BLK8UF6vqQIedZU9jTr3xDf1KOIdGM05XzxacE04WFEJ85d5U140Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48ce43ce0.mp4?token=TLHnmHoe5WAYlUEYfv-j1ZQkLOryhoVGox2OzwFl1l-9L98x1pNIF1WPY41dDNNvm6lkKrEwWF3vj_ptBnJMEHvMuYhmXwMir26g1byUdbZ3QCHvlsYjl0z-l9zNjg1kzppewP5zos0SZ6NumkCw3HVVJXnuRW_K-N08dvNkgqHIE2PlEmpScRcUELpqoSMREsM8OKe8me0-ikkmkybSia_Sy4ZEUHGIwOuG54wb0B2EpPKU6yR1z4N1TPbSxcgg64CxIIhfVEFyZjihTyQtYIbtF6fccwDewQgZ40pGUW_kumOVOg-i62TcYxQXJXjYnjV4PBMYdPlXwnCqmL_7Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48ce43ce0.mp4?token=TLHnmHoe5WAYlUEYfv-j1ZQkLOryhoVGox2OzwFl1l-9L98x1pNIF1WPY41dDNNvm6lkKrEwWF3vj_ptBnJMEHvMuYhmXwMir26g1byUdbZ3QCHvlsYjl0z-l9zNjg1kzppewP5zos0SZ6NumkCw3HVVJXnuRW_K-N08dvNkgqHIE2PlEmpScRcUELpqoSMREsM8OKe8me0-ikkmkybSia_Sy4ZEUHGIwOuG54wb0B2EpPKU6yR1z4N1TPbSxcgg64CxIIhfVEFyZjihTyQtYIbtF6fccwDewQgZ40pGUW_kumOVOg-i62TcYxQXJXjYnjV4PBMYdPlXwnCqmL_7Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از کشتی کانتینربر متخلف با ۲۵۰۰ کانتینر که در جنوب تنگهٔ هرمز غرق شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/698373" target="_blank">📅 13:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698372">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
رییس پلیس راهور: پلاک اختصاصی منطقه آزاد بوشهر به زودی رونمایی می‌شود
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/698372" target="_blank">📅 13:48 · 22 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
