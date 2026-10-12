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
<img src="https://cdn4.telesco.pe/file/aDRmO3NZzgxaVfRk9jagTLRmv0MpmbkQFhixgaqJx4_wnCwABufaAnZ47PZmD3PreB3qJZpA92ARjyUebxDUZa3J46iwOSO8Zqg-_Sr_VnqxRUoNXPl8BGXYdLmUEXwyDiDAON6ncqwu5dHwTxz5nCbDLnm6_hxqiSyO1mkYq-0Cny2OOqavDcOaegwjZsa8CPtJQaF9vAfeypOJHH08ln4Rg2md-vYTVsLcl5rcrFzdjdKxkm-0VdJKaVB_xozIoeY39GGZS6fXaj-Hm3p69do-YiWm4pE8rJ0GSQdIMeDiBZrtLEFITnai5MyfequVW7ingUYPYuMvLypysAkO_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 04:57:01</div>
<hr>

<div class="tg-post" id="msg-152215">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران تحصیلات | irantahsilat</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8D9FyEAPc1pOZdsyv5JJG-qKAD7UI6oB2VtcsK0B-ce4Alki0Y6PO2KkLqM6XLUbg6CcH9G7UAvDLcD2dXlvccGV_MoQ6nud8ptrOZ8EzPCKS5cmmmqDCfHhI70E-1H5OdM22Puw9lOl6qffk92nhMMrf6PnuKJ6KrZotkjH9ay8THzvd28z0wNQVaChLJgpqGn3C3rnjh3nC3f6i3hIUa-DFg4k2PeSscjvURL7difz6uxrPiFGUe8m_HVh6y58WSTB_STXVKqM6apFJLflvnu7pmTSFfkfD2j_fvQhE8I8OpZX_kWSXZsCw-rNXHraVpH1pqqJQwbVpqd25AshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
مدارک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_support
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/152215" target="_blank">📅 01:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152214">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b482f6d3d9.mp4?token=YIOtzKT1KP6hpxYtRJYwof4BScenjCSWtMD0Hwdfzs8qDa-JDdSI3EWp0fNunQz-gIPzPWLEQA7LDT71CdVjwUQJa_12rWGCWeEZSueQ6KtfAeBvBU_htQ6S6uuSDH6Y_ZDrRANrhHKYQNYJ-x1kpGyz8W-XyTY79FMY04uWD3GEWlXVpjag3DcO3AEZ3Av2VheQ10AULm3L_MHRsqNWBhjc1UnD3Tvn3pD17-_8OtVw_2yVZkHDbfEoJdu6vEqJRNBn_vQuYSaGcrRPuKz54-Z3qZuPZRd4QvwCb8GtUn6-xRjC52EvteEGwJnhPdSnjdAv0MQqG_lN-VE-_SRP94S050M0pXQdxHnPKfQyriesFvw41hyxhM1SgEXYcj7xPtJtZl1FBxCS1c9JPfAN9IfpBaO3IgN1opJzgzbc8u6_VbZ3crWexdhICPHPTutH6gTpD3rjsCnms9JyVTNWOgB4Q4cH4lWknTdT2vdJyoRS8MfrccVV9ht3pfMfT7VtcLpN3y-juaAJGmVOPC_s4n2u__K9q732sZEFUfIQGreNR_9zHHLUdNic6C5lH9OEiln9_dJIHL8Uo_U0gRTEsYAtNVerLtocoy4uvWAceCF7Wmq1Vhwa4On5HkJ78NyoJrsQMADVxwzZ_K5aWmmXSf0O7LlsuJ_Z_Qjk4v-J4ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b482f6d3d9.mp4?token=YIOtzKT1KP6hpxYtRJYwof4BScenjCSWtMD0Hwdfzs8qDa-JDdSI3EWp0fNunQz-gIPzPWLEQA7LDT71CdVjwUQJa_12rWGCWeEZSueQ6KtfAeBvBU_htQ6S6uuSDH6Y_ZDrRANrhHKYQNYJ-x1kpGyz8W-XyTY79FMY04uWD3GEWlXVpjag3DcO3AEZ3Av2VheQ10AULm3L_MHRsqNWBhjc1UnD3Tvn3pD17-_8OtVw_2yVZkHDbfEoJdu6vEqJRNBn_vQuYSaGcrRPuKz54-Z3qZuPZRd4QvwCb8GtUn6-xRjC52EvteEGwJnhPdSnjdAv0MQqG_lN-VE-_SRP94S050M0pXQdxHnPKfQyriesFvw41hyxhM1SgEXYcj7xPtJtZl1FBxCS1c9JPfAN9IfpBaO3IgN1opJzgzbc8u6_VbZ3crWexdhICPHPTutH6gTpD3rjsCnms9JyVTNWOgB4Q4cH4lWknTdT2vdJyoRS8MfrccVV9ht3pfMfT7VtcLpN3y-juaAJGmVOPC_s4n2u__K9q732sZEFUfIQGreNR_9zHHLUdNic6C5lH9OEiln9_dJIHL8Uo_U0gRTEsYAtNVerLtocoy4uvWAceCF7Wmq1Vhwa4On5HkJ78NyoJrsQMADVxwzZ_K5aWmmXSf0O7LlsuJ_Z_Qjk4v-J4ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی پشم ریزون از جنگ ۴۰روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/152214" target="_blank">📅 01:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152213">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSfmxdYWBdIdF5hA_IPRNCu9btlq7ZB45iiSn6cM30T6EbV68loRW0CNDNQUa3v1OokRj593CxNXhkGMBBeV1JaGXVm_spyX6YxBX3hD5Bmo5t4UcBU6srj-thB81XeGoi5LR1L49Q4AKxWaLSIpL8BlWuUaf_0akWzWSDGjB1wsqOgWpGlaT256cSesqpSfnYlgYufGouJ30LwD3bXrBmF6Jcgv13MQF4OMCHqZte2lvD58sZ7XbN8UJdXw8d5_wNcYQ6b2CMSNYwtRyH6ila7LsSD_6LolkBJzyf4H_g0v76782tRhlXObJ-YriF2mOpZYwzsBTYZgpuGibv2JoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روحانی: حجاب اجباری بی فایده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/152213" target="_blank">📅 01:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152212">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90ad219cbc.mp4?token=fZgzJtdr9herGIS8ywBogr3kfj9ubPhUMXPiHWjSr5e4AkL0uLC-TFzbRBpnUf6ItO31Ud7fQeJEWXrkHOePjfQWWs6oJ8iCsZTeAKSLHJxROz940erLaFk8Uc9LFaLCbl5NzT3PMQaO-tebKCc6U97D2kZRBYmJum2NLVSp7wY9uJgyDQzTZISbzXJ5N4gaOAr9VHlGV2qmm9MN6HGgTQgmrWQ7IB5RC6sFKTktZSkH9VP9IK98g7SUbrZbUlxgndB7CSfvEpCAMLY8IexUxNgqxI9u8SbhzHJNAsQWRd80eEjvfXvq4Gy-05h-xNIc-g2ThqppLyYkq-DE5VlTjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90ad219cbc.mp4?token=fZgzJtdr9herGIS8ywBogr3kfj9ubPhUMXPiHWjSr5e4AkL0uLC-TFzbRBpnUf6ItO31Ud7fQeJEWXrkHOePjfQWWs6oJ8iCsZTeAKSLHJxROz940erLaFk8Uc9LFaLCbl5NzT3PMQaO-tebKCc6U97D2kZRBYmJum2NLVSp7wY9uJgyDQzTZISbzXJ5N4gaOAr9VHlGV2qmm9MN6HGgTQgmrWQ7IB5RC6sFKTktZSkH9VP9IK98g7SUbrZbUlxgndB7CSfvEpCAMLY8IexUxNgqxI9u8SbhzHJNAsQWRd80eEjvfXvq4Gy-05h-xNIc-g2ThqppLyYkq-DE5VlTjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روز شنبه دکتر مهرآئین که به دلیل انتقاد از ج.ا به ۸سال حبس محکوم شده بود، راهی زندان شد
🔴
با آرزوی سلامتی برای این مرد بزرگ و فرهیخته
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/alonews/152212" target="_blank">📅 01:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152211">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnafMA_FutbWFaJEDcCUSA5dHACpozU7HcKvsq30_eaRDqcsHUvu5hxePwpo-SSZnmdFHyldpSoskNOFn3yQp6puXlmGOhCsEM_MoVEQUcV0Uz17HqgJikaa4l9wvzSez_AYjQfp84gs-Xi6wI22qiZj7fgTgd9joYbSmGzrpEsLbsYdcpWLyvX9W6YH5YSWPQXfR4leCyz1qruhE_Lwt0yPsu19hrw60DVE0mc6nF2o4fmcgfqdGfwvfklUXpBvgTDT4YA5d0F0vFX7DqcckQHegSOQ_s5eCJ1rYC4rFNSUBIrI1VGLQlVu87TwhBK9zvsVWbkwEG5U6HOoRB0U-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند جنگنده چندمنظوره F-15 نیروی هوایی ایالات متحده (USAF) در حال پرواز تمرینی حمله به ایران بر فراز عراق مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/152211" target="_blank">📅 01:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152210">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👀
اگه دنبال کانفیگ ارزون و پرسرعتی
کلیک کن
🔗</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/alonews/152210" target="_blank">📅 01:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152209">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رصد ۹۲ هواپیمای نظامی در منطقه طی ۲۴ ساعت گذشته
🔴
۱۶ هواپیمای ترابری از خارج منطقه وارد شده‌اند که شامل ۱۲ هواپیمای آمریکایی، ۲ هواپیمای فرانسوی، یک هواپیمای بریتانیایی و یک هواپیمای ایتالیایی بوده‌اند.
🔴
همچنین ۵ هواپیمای ترابری نظامی منطقه‌ای، ۳۴ هواپیمای سوخت‌رسان، ۱۵ هواپیمای جاسوسی، ۲۱ هواپیمای ترابری نظامی که در داخل منطقه جابه‌جا شده‌اند و یک بالگرد نظامی رصد شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/alonews/152209" target="_blank">📅 01:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خبرنگار حوادث:
پارسال همزمان با شروع جنگ تو نهم اسفند یه زن بعد مفقود شدن شوهر میانسالش میره اگاهی و اعلام میکنه شوهرش ناپدید شده
و حالا بعد چند ماه که هیچ ردی از شوهرش نبوده یکی از فامیلای این خانواده خیلی اتفاقی استوری یه زن جوون رو میبینه و متوجه میشه این مرد گمشده همراه این زنه
حالا که پای پلیس به ماجرا باز شده مرد اعتراف کرده بعد از فرار از دست زن و بچه اولش رفته هویت خودشو کامل جعل کرده و بدون اینکه چیزی از زن اولش بگه با یه زن ثروتمند ازدواج کرده و ماه هاست داره با اون زندگی میکنه
😐
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/alonews/152208" target="_blank">📅 00:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152207">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
باهنر خبر داد: زینب ابوطالبی مجری جنجالی «مملکت مال حزب‌اللهی هاست، هر کس نمی‌خواهد جمع کند از ایران برود»، از کشور رفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/152207" target="_blank">📅 00:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152206">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEX3YaITzXywSl5LJfTg7Yq9HgY_WmwoouOwfZcraoJAT06sbcvYnnGrb5hNqCVjr873RjnNwAiDiIaDYLZnZ4uX_cIbGaamLlmpyaTfzyAX1OkJfe9_xCHI0-YGmSKXnGQYjislIahQtOfEz8-bp2aYnj4LEDP6eOV6vaa_JwKyD5p6pxkddFNwxT2sG19Ce7upKwkdso7bcmk4IG_zuENVhsYDUPXZ-wrWWMytFdVq0v_j6pfSOeHPIWYGj8zC1TkuTpA0SbXHaha741jLV3NrfOd-_IJVKM5kAAHmECQ5JXRjhhu0eqfUQc_6pzA8D-HC4QGXYaabKoiu1xVnaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال: ایالات متحده با برخی از هفت شرط ایران موافقت کرده است، اما ما پاسخ آن را ناکافی می‌دانیم. دیپلماسی ایران تغییر کرده است و دیگر به وضعیت سابق باز نخواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/152206" target="_blank">📅 00:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152205">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b8846312.mp4?token=mnDORjTqeEAmAUPHc7WdzOYaeW4EkzaYXauztyC9_c10c0IkU4szmyZ3jdewb_1FFjIjqCgUe_da4QN0OFSWx7_kvE14pYlT8qhxWq4EZ6riXvq5JNETkpJsNensrt-Q7JRAn5c4rXWwLLHiPCxOqXK1wFKKkt3NZndX1Yo_FA49ue_q3dkuyj2bQd0lPSZanMA07xGHY53bBPXHVSDNlXbmOeBWEhyMxKd-iCMcatP_97gPYejnLbjNDSN_GYz8kfUfT0Ut1-LWwU-N706wPVtaZVQ2LcgVlzAUzaDX53KZPikGv-XhEzSqBSpC2ba-h-pFOuyx5lVoWWjLW2el0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b8846312.mp4?token=mnDORjTqeEAmAUPHc7WdzOYaeW4EkzaYXauztyC9_c10c0IkU4szmyZ3jdewb_1FFjIjqCgUe_da4QN0OFSWx7_kvE14pYlT8qhxWq4EZ6riXvq5JNETkpJsNensrt-Q7JRAn5c4rXWwLLHiPCxOqXK1wFKKkt3NZndX1Yo_FA49ue_q3dkuyj2bQd0lPSZanMA07xGHY53bBPXHVSDNlXbmOeBWEhyMxKd-iCMcatP_97gPYejnLbjNDSN_GYz8kfUfT0Ut1-LWwU-N706wPVtaZVQ2LcgVlzAUzaDX53KZPikGv-XhEzSqBSpC2ba-h-pFOuyx5lVoWWjLW2el0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی دیگر از هدف قرار دادن غیرنظامیان در فرودگاه ملک خالد ریاض توسط حوثی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/152205" target="_blank">📅 00:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152204">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کاش تو این ۴۷سال حداقل یه کوچه بنام کوروش یا خشایار شاه میکردید بعد فاز تاریخ ایران دوستی میگرفتید  [@AloTweet]</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/152204" target="_blank">📅 00:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152203">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNsP0P_NpgkUAdsOWoNU-4xbYdIqsiK_cDH6zrJok-MuZCNc0QYzsoB6iWxvoM32lmCkTa-p7AonMX9NF56XgBX6Fv2y_nAEKeoW_K7y_xgWmr1x5nJ-4j6xWV4Dr7ydriV_qrQaEekKta-F0PAzdFqY7gsG_FtBDoYxKszzlG3S2S1lmtBW45KyydhGg7k6LKQjSkitcx-HOb689b7AO1zBgMx5m8xsCRIp8-XgYpiA4NhY1oLT7fhWscCsRH9hWL_3jHhwQZia_gVS9tNAkoXurruIMY3YQ-qyqXrjfEE8V26-vgvVhH8UVwB8fbq5idBIB6GiMK_3-Vrh4x3v7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف: هرجور شده باید با آمریکا توافق کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/152203" target="_blank">📅 00:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152202">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22245fb3c7.mp4?token=YAlfGWpcLI8s5amo9oQwTKYVcir7rMUdlEBaCKw02eRgCtLxO4fAsyFmFx7heM-wxYaH131LjrW9zDiwue4PQdPRaHNKuPQTR7U5r-eZwBCOh4qWimMf-H6f3TUsnFAD4-LOm9vQwAGEQ8yGwShUTdljthznYVAnuVTNm6v0F_HADYrSycHUDCxHavUaU2IDKDXqbgnZBUGb7KUgGw7-QHlPgXstDWPBAnuNhe0K8onlGAek70vT-Uz5AthKCCFsV_jsoMP3H5FpsL8xeACOCB0fDDPatqM-U0EmbGuuc2PNlFFcm2ll1IV6Wxp5ePdNQwbOp7SB4ujCqDLa25z9bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22245fb3c7.mp4?token=YAlfGWpcLI8s5amo9oQwTKYVcir7rMUdlEBaCKw02eRgCtLxO4fAsyFmFx7heM-wxYaH131LjrW9zDiwue4PQdPRaHNKuPQTR7U5r-eZwBCOh4qWimMf-H6f3TUsnFAD4-LOm9vQwAGEQ8yGwShUTdljthznYVAnuVTNm6v0F_HADYrSycHUDCxHavUaU2IDKDXqbgnZBUGb7KUgGw7-QHlPgXstDWPBAnuNhe0K8onlGAek70vT-Uz5AthKCCFsV_jsoMP3H5FpsL8xeACOCB0fDDPatqM-U0EmbGuuc2PNlFFcm2ll1IV6Wxp5ePdNQwbOp7SB4ujCqDLa25z9bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی پیش روسیه به نیروگاه برق خارکیف اوکراین حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/152202" target="_blank">📅 00:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152201">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👀
با پول یه بستنی، vpn یه ماهتو بیمه کن
کلیک کنید
🔗</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/152201" target="_blank">📅 00:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152200">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fd15c39b.mp4?token=KZWtfErM-dUg40tdbhHEDpTowaKnC7llA-WlRFaUedI_XtPFIr9MvY1_S0kp6Ugzzflw49QW03z4UgwwYDbXfgjND0Zpm-zCGdhNM2nep8BJgG971BFNbWtVyFyFlmHpx8lm8W2WmYmQ_Sdjk0EyqNMMhu97AQvOB3Eh-Q4RJpxgmDdhwWHheoD-hTcipGh6K9pO7q1jiV-9UlqVq1rafvsaI-hAlFoAZCYMVO-aZGgg6a6yHdY_jelhxamEOENUduHmPx2EY5CUkvQDYVuqlCi_r04aLmysvpxWob6VBzrMidW7x9x9Lh94ssVf-YTW3JDGlaWzsHkIphV_dN2iZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fd15c39b.mp4?token=KZWtfErM-dUg40tdbhHEDpTowaKnC7llA-WlRFaUedI_XtPFIr9MvY1_S0kp6Ugzzflw49QW03z4UgwwYDbXfgjND0Zpm-zCGdhNM2nep8BJgG971BFNbWtVyFyFlmHpx8lm8W2WmYmQ_Sdjk0EyqNMMhu97AQvOB3Eh-Q4RJpxgmDdhwWHheoD-hTcipGh6K9pO7q1jiV-9UlqVq1rafvsaI-hAlFoAZCYMVO-aZGgg6a6yHdY_jelhxamEOENUduHmPx2EY5CUkvQDYVuqlCi_r04aLmysvpxWob6VBzrMidW7x9x9Lh94ssVf-YTW3JDGlaWzsHkIphV_dN2iZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون وزیر ارتباطات درباره تعرفه اینترنت: مردم با گرانی دیگر چیزها مقایسه‌اش کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/152200" target="_blank">📅 00:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152199">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
خبرگزاری دولتی عربستان سعودی:
وزیران امور خارجه عربستان سعودی و ایران درباره تشدید اخیر تنش‌ها در منطقه گفتگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/152199" target="_blank">📅 23:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152198">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
تصاویری نشان می‌دهد که در دیروز، یک موشک بالستیک متعلق به گروه حوثی (انصارالله) به ترمینال شماره 3 فرودگاه بین‌المللی ملک خالد شهر ریاض اصابت کرد.
🔴
این حمله منجر به کشته شدن حداقل 13 نفر و زخمی شدن بیش از 300 نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/152198" target="_blank">📅 23:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152197">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اکسیوس به نقل از یک مقام کاخ سفید:
«ترامپ واقعاً عصبانی است. او احساس می‌کند زلنسکی آمریکا را بدیهی فرض می‌کند و قدر حمایت‌های آن را نمی‌داند.»
🔴
استیو ویتکاف و جرد کوشنر، سفر برنامه‌ریزی‌شده خود به مسکو را به تعویق انداخته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/152197" target="_blank">📅 23:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152196">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf-DMIhIxcdD0TKWfND06JPWmMqTJzrYsNRql7V8IuZgf3O9clI1nEQLklBChurVEczQaZITgSNfgSjdr223nzL4MPRcBEpMpczqW9RNXa6Pp4-1LOKNEita7wr6x_rS3wVxSaTmC2r6JSElDpv1S8yxN_CmbmGJBKspj0D1Mt2L_Vp6o3yamC9dwf4zF_NPGgDnHoJjZ2yyd1F3LqREwG47aY62QONgzTSgI6waAa3IBHJM_CdP4qyI0pX7lalWF6ehpZmuq8uMiChQCLQ6nSdncrWzXoh4gM4a-Z3vmloJPf6MDw4DO-OvrVAALh7wX2JYlh7w-yi-fkF4a7-xmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی سپاه با انتشار تصویری در فضای‌مجازی نوشت: ما منتظریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/152196" target="_blank">📅 23:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152195">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
به گفته یک مقام کاخ سفید: ترامپ انتظار دارد که زلنسکی به آتش‌بس پیشنهادی در زمینه انرژی پایبند باشد و در ابتدا حملات اوکراین به پالایشگاه‌های نفت را متوقف خواهد کند
🔴
توقف حملات به پالایشگاه‌ها می‌تواند راه را برای یک توافق گسترده‌تر که شامل نیروگاه‌ها و شبکه‌های برق نیز می‌شود، هموار کند
🔴
روسیه همچنان در حال بررسی پیشنهاد دونالد ترامپ مبنی بر برقراری آتش‌بس در حوزه انرژی است
🔴
ترامپ واقعاً عصبانی است. او احساس می‌کند که زلنسکی، ایالات متحده را دست کم می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152195" target="_blank">📅 23:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152193">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/493ee04b61.mp4?token=rQAM9ZLsCLb-N_Q56STvOmWo2hhHh-bL6khwdPHvQHt37xvFePFE3xPWuNgtBLNtxAV2YbCX-_XyvvCN7fObw2xSWhnh8gJGdESwYSAodVEgFqer2ta3OZe-sBRMm5mXvfl--q7-WwQ86X98uttXGWf3EgfAfjxvc1bpqs39qgmPOytae7Lpv--S0eRZqPswNvi9I5Atsr3fQ0y7shf0w2rcuMbu-723_wcGfIGVQKAfylM0HtYLWA8MWgd8DN4ollwbCVBel6gIBD2QdnlHnpJzO1FwPuOPut2T2ecFgyU1MVdpHjmvHpShfKTXIcr_DrxnWuELnz46AVxuxSxWbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/493ee04b61.mp4?token=rQAM9ZLsCLb-N_Q56STvOmWo2hhHh-bL6khwdPHvQHt37xvFePFE3xPWuNgtBLNtxAV2YbCX-_XyvvCN7fObw2xSWhnh8gJGdESwYSAodVEgFqer2ta3OZe-sBRMm5mXvfl--q7-WwQ86X98uttXGWf3EgfAfjxvc1bpqs39qgmPOytae7Lpv--S0eRZqPswNvi9I5Atsr3fQ0y7shf0w2rcuMbu-723_wcGfIGVQKAfylM0HtYLWA8MWgd8DN4ollwbCVBel6gIBD2QdnlHnpJzO1FwPuOPut2T2ecFgyU1MVdpHjmvHpShfKTXIcr_DrxnWuELnz46AVxuxSxWbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران جنوب لبنان توسط اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/152193" target="_blank">📅 23:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152192">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کانال۱۳ عبری: ارتش اسرائیل در آماده باش بسیار سطح بالایی قرار دارد و خود را برای سه سناریو آماده می‌کند:
🔴
۱- حمله مستقل به ایران.
🔴
۲- عملیات مشترک با آمریکا.
🔴
۳- مقابله با حملات احتمالی موشکی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/152192" target="_blank">📅 23:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152191">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزارت خارجه مصر: ۵ تن از شهروندان ما در حمله روز گذشته به فرودگاه ریاض مجروح شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/152191" target="_blank">📅 23:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152190">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b25c7ce1.mp4?token=R2K-BsJuVA-vKoiwJE-JzIoTCl5doXYu5W16apPd28R7K8xI1kvD0SSln22TPQJdQuDwfZc3y1d5zqqeFJirIv9Jl8fgVE7GS9g4wQsuWQNeJo3Vl9HFJMYEB9Tc-rcsp16sYmb4wQ275Xwv65b6eK5QDryC1sDhSAxD_rNiMHmr7FSXG-MoijUR0pmw4df6jzuolg_qqJR8nrWanS9pReIbFNcXg91qaE21ihO6rpPUswSFOlVPTZT5XBVvTCmZXVKuExfToQIJl3htwRs8o1zJEYJTJk75PH8to6ysbiUW-IGDt5aQZFMh5PNobhnZ4oV9ygFcDdd6La9pLZrXRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b25c7ce1.mp4?token=R2K-BsJuVA-vKoiwJE-JzIoTCl5doXYu5W16apPd28R7K8xI1kvD0SSln22TPQJdQuDwfZc3y1d5zqqeFJirIv9Jl8fgVE7GS9g4wQsuWQNeJo3Vl9HFJMYEB9Tc-rcsp16sYmb4wQ275Xwv65b6eK5QDryC1sDhSAxD_rNiMHmr7FSXG-MoijUR0pmw4df6jzuolg_qqJR8nrWanS9pReIbFNcXg91qaE21ihO6rpPUswSFOlVPTZT5XBVvTCmZXVKuExfToQIJl3htwRs8o1zJEYJTJk75PH8to6ysbiUW-IGDt5aQZFMh5PNobhnZ4oV9ygFcDdd6La9pLZrXRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز جنگنده در آسمان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/152190" target="_blank">📅 23:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152189">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
باشگاه انقلاب تهران به دلیل بی حجابی و تحریک امت معکوس شده تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/152189" target="_blank">📅 22:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152187">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/av52jsiO4ZDyIN5E2495hNk0NBg8IZ_DXLZkyt3JGp39aWYp2JfhZNZxl1HE5ldo3JLkfut7t3aO-W_FiSxeSpfkfwKaTsVzNk-WBDMF1yUfNiHn_9WRBWNFqTfRUwuAba5ryW8_j6CZhBMMPJx805Vn5EVsEBCto5R8MEypW9IoLoyKhKDOl8rbsjH07E1OwhlWbPfzMSsiD7cmXI7UyfJAFxhD_9O4u4JHr5AqyJI1kTYffBCsUSNjY3AbBt0Ze0fY0Mi4_H6T_ozwpQi6BbjWUUDBxclpLb3wJnyC6Eg78e33VqLpZ6zQy1lcT-0VAlNUvGQ_GtmPSsEbl9MfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41fea1af6.mp4?token=i5evj9dwnXrNGpYyPEsDDEDAIgL6tDZY3KTk6GdJqR4HrLkDRCcqs_1N-4nt1xQIVtsZD7TvE3POZe0NCJQYBEOmX30ZM7D-VKc3aOjJ6udkHbE0tGBKpGIgN9AG6oNx_SFABDc6OBazYe-_rAFNQwxVjGET7pAAw1UfalNUIBUW8BNlvm2ilX0OMTlO7lgBNB8NkJ9IccCaAvZ-PgJ0eFtkbn_Bh2LGxI8V6Z9VV9jcfrE-Vr9WANUTzLBwx6AUkZUyx-jFxePQ7orYCwEmfg1ZJeXQgofF7ZNFdvcAMKhZ7wi47Wx7NaFHvYYlDJn4xnow3RXbRUqtotXFxOf_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41fea1af6.mp4?token=i5evj9dwnXrNGpYyPEsDDEDAIgL6tDZY3KTk6GdJqR4HrLkDRCcqs_1N-4nt1xQIVtsZD7TvE3POZe0NCJQYBEOmX30ZM7D-VKc3aOjJ6udkHbE0tGBKpGIgN9AG6oNx_SFABDc6OBazYe-_rAFNQwxVjGET7pAAw1UfalNUIBUW8BNlvm2ilX0OMTlO7lgBNB8NkJ9IccCaAvZ-PgJ0eFtkbn_Bh2LGxI8V6Z9VV9jcfrE-Vr9WANUTzLBwx6AUkZUyx-jFxePQ7orYCwEmfg1ZJeXQgofF7ZNFdvcAMKhZ7wi47Wx7NaFHvYYlDJn4xnow3RXbRUqtotXFxOf_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستون‌های دود از تأسیسات سعودی پس از هدف قرار گرفتن آن‌ها به هوا برمی‌خیزند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/152187" target="_blank">📅 22:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152186">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449533f768.mp4?token=fV_0iGNwFAM6nxmBblpqM2la4W3iEFA4_zn49JczZAQIfhWfwODpOA_r3tVMePO0hnNWRA2KEqy4Z73c_Wn9WpJp6l-LozewknpP1325pjOGWujqmnQcecVQ-O8h2GSmhtNZ1KrsW_sNVN6MJvKlNbDO0CrJHHFj-yfVd5DXDKkDEYmX0fn1-RV2IDvIvkucovBZgetZTBM3WwjqnuyDb15Eg_HCeDXw-u1FEaBqRdNKEfLCtxZczdWlIA8bD5WwcOtQkQUD-D6_PS94MeDEXpBSaLCu93bdeAyBb8Izd0CDHZLjadXnQ7BnL4MM08DBM7xC2QCkFqEj58Bc_3UhIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449533f768.mp4?token=fV_0iGNwFAM6nxmBblpqM2la4W3iEFA4_zn49JczZAQIfhWfwODpOA_r3tVMePO0hnNWRA2KEqy4Z73c_Wn9WpJp6l-LozewknpP1325pjOGWujqmnQcecVQ-O8h2GSmhtNZ1KrsW_sNVN6MJvKlNbDO0CrJHHFj-yfVd5DXDKkDEYmX0fn1-RV2IDvIvkucovBZgetZTBM3WwjqnuyDb15Eg_HCeDXw-u1FEaBqRdNKEfLCtxZczdWlIA8bD5WwcOtQkQUD-D6_PS94MeDEXpBSaLCu93bdeAyBb8Izd0CDHZLjadXnQ7BnL4MM08DBM7xC2QCkFqEj58Bc_3UhIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز تو تهران یه پسری به مناسبت روز دختر برای دوست دختر ۱۹ سالش ماشین لکسوس خرید و بهش هدیه داد:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/152186" target="_blank">📅 22:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152185">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
معاون عراقچی: در حال بررسی پاسخ آمریکا به شروط هفتگانه خود هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/152185" target="_blank">📅 22:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152184">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 300 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/152184" target="_blank">📅 22:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152183">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkGxl9ElGT_Zvo28IPYnDaL_AYqQJ_rxaMt0QgkF_ErVJhXDFzYV4eWl0btx6RdCAjsvRKXmrwmATQLY91yvD2UxzBkzpukkChbS1wQcVdBryG24C762khRd_hk9mEMzjetsqfjbRHlxaNvZtFl_9UHn-GTctT9Ib_lcyHJP9pmewUc0Hp4DmF65enDg-kaPt8ThptY4c2BMw2_qDzLL3jKvudF6KWQcXUvjuEUufOnlnO5jQMuhd8F5x82KpfySelM1r7yPKArWFypObjzOEFlu3uTJZWD0Q6lT7MkCXf4A0bfwfaCgkHqHSm5Hf4e_GjwSVToi_WkjJ6gPYld1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک بهترین شهر دنیا در سال ۲۰۲۶ شد
🔴
تهران با افت شدید در رتبه 462 قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/152183" target="_blank">📅 22:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj_XKqJvXFAhmu_l6fHKIkfQYbLrAxDUCRSJPDfwYkcdzyJvLbk_bW-MQkdGParLvCwBToVlFT3gL03ipFYyLE6U621TvzMQc_uD5L5H6K_6x6J1yYXtezlf5_iKQYbX5YjR1su6msa_7e86hGnDacQ11Lw--N0kvPew6U2CtQaYlYmZNNLNmRWzIM32jjQbFDV6puW82cUv6yOa9IVbSzQYnNd6H3OG8d4UKdQFJ3RQ58ag0kOqM_JU7iRzeSDayYobkvQHtN44o33zfVpNR6F3bnlcyxja8t-lLLVIPAPUsLESw42_0Cv6A-OHOcsoPIQqppZLZ6GDBCwNOiTX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باشگاه انقلاب تهران به دلیل بی حجابی و تحریک امت معکوس شده تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/152182" target="_blank">📅 22:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152181">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی درباره وقوع حادثه‌ای برای یک نفتکش در نزدیکی بندر صحار عمان دریافت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152181" target="_blank">📅 22:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152180">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PKiu6Wlvp_lo4Wk5i52LbjDw0wtXqLgjX7PJqMH-jKqttnZOCW4K5c2rtrQjD7VqK561u5HJwEpcDuQHIGcubIKqY_YpH2lSKPr3MR2RSjt2yb07r8s2jHSGBL7-N_FycnaQlN44NcmSEeFC6WzHqUXRmjNfctnxO9u3WgqvCfVDiauILvunSKr5rQAtigR7S0FYpCk2DC9gBtVuOtTGa7ereIOqiUakhdF0_nb0qkMOmvVf4a6o6lw1h95zLYLyif-_FvasxwlRBVbZXnsDxEyh_eaPkxKcGNLV2bOfPztkw3lg7JUNecxTpm_zJkZ8KXSLiKmTFow1QiIM0Jr7sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان هوانوردی غیرنظامی عربستان سعودی، وقوع حمله‌ای به فرودگاه بین‌المللی شاه فهد در شهر دمام را تأیید کرد و اعلام نمود که ارزیابی خسارات و بازرسی‌های ایمنی در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/152180" target="_blank">📅 22:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152179">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سپاه: از امشب هر کشتی که در تنگه هرمز، سیستم‌های ناوبری و شناسایی خود را خاموش کند، به آن حمله خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/152179" target="_blank">📅 22:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152178">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
باشگاه انقلاب تهران به دلیل بی حجابی تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/152178" target="_blank">📅 22:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152177">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
گزارش‌ها از تمرین جنگنده‌های اسرائیلی بر فراز عراق با شبیه‌سازی حمله به مواضع جمهوری اسلامی در همین لحظات حکایت دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/152177" target="_blank">📅 21:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152176">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: بنیامین نتانیاهو نخست وزیر در این ساعت نشست ارزیابی امنیتی با مقامات ارشد امنیتی برگزار می کند. در این نشست همچنین به پرونده ایران در میان تنش ها پرداخته می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/152176" target="_blank">📅 21:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152175">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
میلی گلد: پول همه مردم رو دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/152175" target="_blank">📅 21:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152174">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
زلنسکی: روسیه پس‌از اعلام آتش‌بس انرژی توسط ترامپ، به تأسیسات انرژی اوکراین در کی‌یف و خارکیف حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/152174" target="_blank">📅 21:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da4f9104c.mp4?token=v34oLCYqfPxkwpZwPL79hGNc635A_ui_qWiekmbHqkGhz3AZkZWyVW6GCICVBGAdd51OhckR2q5bsGIGAaiseukJjwvc1MMYtUE8G7Jaq5eiIoUMZP96V2UhKW4Y9YWRaCEtVHtOWWqmKu2WIC2D-ZfcQsCRAFzDhHbIxExj0rtzIy1oKKgWMf3yBfa1_ecQemjnBgpm_NB_Z-RmYT5llasUpNUfeqU1UB-JXs3m9VO5wCqxC58oMIpIg1eA0kWqa8xs1zW4EnEmP3wHIeuItI-8VWCp1bqYj9gqaX_hZpVkUkKzjxYP3yMI0TtSkNYmNNkr1GPyDTBK02BpGFoHlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da4f9104c.mp4?token=v34oLCYqfPxkwpZwPL79hGNc635A_ui_qWiekmbHqkGhz3AZkZWyVW6GCICVBGAdd51OhckR2q5bsGIGAaiseukJjwvc1MMYtUE8G7Jaq5eiIoUMZP96V2UhKW4Y9YWRaCEtVHtOWWqmKu2WIC2D-ZfcQsCRAFzDhHbIxExj0rtzIy1oKKgWMf3yBfa1_ecQemjnBgpm_NB_Z-RmYT5llasUpNUfeqU1UB-JXs3m9VO5wCqxC58oMIpIg1eA0kWqa8xs1zW4EnEmP3wHIeuItI-8VWCp1bqYj9gqaX_hZpVkUkKzjxYP3yMI0TtSkNYmNNkr1GPyDTBK02BpGFoHlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی سپاه: دومین سوپر نفتکش با مین دریایی در تنگۀ هرمز برخورد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/152173" target="_blank">📅 21:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fb405cce0.mp4?token=E3hLPFYNuB9tgPWILd-sWCqrQV_YDIJf3TiIlIY-NZO3oCJNv6zIgJLLOTNysOU53J1ZB5YQqQB2AHYpCMnsGqKCmTyJJYpfVm7vGtsMAwnm2Yz5kifNzETLO6O_lJLyj5J0klaYPKzlDo3nVQ3acMkN-wzCHj5BCOzLzBAzj21mluZb6Kyo8lCOC142oCTmunzkKN8uhl2mPZzvXflWrlltrSSLRrVbLogIZ7l1QhRsR-QJMo1oXzSMJkTKJbfN8_EFcDffFOGAXGI8432lSRLfjR79F2q4V25dTJ2F1-vsMkcWn7Lg4INMOm5YpZamZcdPA2V9OeXvgEqWhMf0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fb405cce0.mp4?token=E3hLPFYNuB9tgPWILd-sWCqrQV_YDIJf3TiIlIY-NZO3oCJNv6zIgJLLOTNysOU53J1ZB5YQqQB2AHYpCMnsGqKCmTyJJYpfVm7vGtsMAwnm2Yz5kifNzETLO6O_lJLyj5J0klaYPKzlDo3nVQ3acMkN-wzCHj5BCOzLzBAzj21mluZb6Kyo8lCOC142oCTmunzkKN8uhl2mPZzvXflWrlltrSSLRrVbLogIZ7l1QhRsR-QJMo1oXzSMJkTKJbfN8_EFcDffFOGAXGI8432lSRLfjR79F2q4V25dTJ2F1-vsMkcWn7Lg4INMOm5YpZamZcdPA2V9OeXvgEqWhMf0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دعوای گروهی دختران تینیجر سر پسرای ۴۰کیلویی در رضوانشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/152172" target="_blank">📅 21:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d829e5c716.mp4?token=Ha42xqSI_tgrKzPu5Rqcr2qibVQmLGd-U1FOmwO0HW1yLjXy9BPc79SbpgyiaP-EOMx1UEzcaSPhLAtN8uclOhI9o7E6_eAB76es7bIX4by1qn7Fvp7FQwOjYmXryo3GKW1vdY5ewUfKoOWQ3RCvRvy6MNv8wZ0j4HJqHQxrqKayHLs0KbjwVIq_zkHi7bOYlOqJ_osuuJAxLk7NsGxuYiRJ22zLOmvNWYIWbFQ9ygdjr7OnkzTMmPc39u6QKsOGz2RO075pognzgMgwp7OwxAylxGOGQXdYTTdUlG9B8PZkQwDnrCwijzmByxOOXil_NQBovx_AvX1cSpQ8f8dmbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d829e5c716.mp4?token=Ha42xqSI_tgrKzPu5Rqcr2qibVQmLGd-U1FOmwO0HW1yLjXy9BPc79SbpgyiaP-EOMx1UEzcaSPhLAtN8uclOhI9o7E6_eAB76es7bIX4by1qn7Fvp7FQwOjYmXryo3GKW1vdY5ewUfKoOWQ3RCvRvy6MNv8wZ0j4HJqHQxrqKayHLs0KbjwVIq_zkHi7bOYlOqJ_osuuJAxLk7NsGxuYiRJ22zLOmvNWYIWbFQ9ygdjr7OnkzTMmPc39u6QKsOGz2RO075pognzgMgwp7OwxAylxGOGQXdYTTdUlG9B8PZkQwDnrCwijzmByxOOXil_NQBovx_AvX1cSpQ8f8dmbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ظریف:
اگر لازم باشد باید برای بقای کشور به توافق‌نامه‌ای شبیه ترکمنچای تن بدهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/152171" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152170">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
هیمتی: اقای بسنت وعده ای که دادی چیشد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/152170" target="_blank">📅 21:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152169">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
بیانیه مشترک عربستان سعودی، ترکیه، پاکستان و مصر: ما حملات مداوم شبه‌نظامیان حوثی به عربستان سعودی را محکوم می‌کنیم
🔴
این حملات تشدید خطرناک تنش‌ها است و ما از پادشاهی [عربستان سعودی] در اقداماتی که برای مقابله با آنها انجام می‌دهد، حمایت می‌کنیم.
🔴
ما شبه‌نظامیان حوثی را مسئول این حملات می‌دانیم و از آنها می‌خواهیم که فوراً آنها را متوقف کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/152169" target="_blank">📅 20:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152168">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نخست وزیر پاکستان: ۶ تبعه پاکستانی در حمله به فرودگاه ریاض زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/152168" target="_blank">📅 20:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152167">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfVox9u0VlG4K0IqbsSlArPfJvlF0Cn6zJ_Or1gtBUQ-Lu8amTV1KJ8np5zYjgORn_42bheKgf9XNh5ly0yF4uN4Im8Dh7fWzf7KuEweE8HF2iZMdtOc80Q9NnCMoR6abPVRH8M55JC0TpImAPuezyOe7fRaENRgru5BwvgF6wRp3xO_ANXo09m5D8WgmIZ9o509ASRMikiTzYkOp1RZRMmATmu1zruLAGJqQA983iUuAM120p3UfoqEJGciOJWsC_1O1ICOj4J6DKM_i4G_kLk_nslKjHy_i5I8YhNNW4UBLKdtgyRZ_uYd7QxMcN2LZcrLKRt8uBxncsHAcwUzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باهنر خبر داد: زینب ابوطالبی مجری جنجالی «مملکت مال حزب‌اللهی هاست، هر کس نمی‌خواهد جمع کند از ایران برود»، از کشور رفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/152167" target="_blank">📅 20:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152166">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آیا دلار 300هزار میشه
⁉️
تحلیل عجیب نوستراداموس ایرانی
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/152166" target="_blank">📅 20:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152165">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/604f2b0c98.mp4?token=GyZG1URhR1p0h9WEK8lVE93y1pvnHMOastwzi3SgUb1gnWxc3aNtFd6DRn9wU40mn-Py_S5D4pJ6hRj7Pzs1DSWdncJ-4SlWs66i6xO6uKcghPuM9Q10FgnHCcaC34B_Jk3Su9p6ZZLXVgRTWyW_T6KKhSuQsYUOryYSyTJcM-QaPvAMmxXqBytwWAMpCCyftgfpoGXTvNhkHyuI5xN01iUMuMw5KsOpImFIvBiKRKnf5k92sgyCZpl2rHSnoABU4dHdAgDF1ueXeVn7QBkDpVgVgvA7PYaL8AAa487-xvdmAUZEAIth4Gui961jLxqZK0OzWZtQo3E007ahwO18_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/604f2b0c98.mp4?token=GyZG1URhR1p0h9WEK8lVE93y1pvnHMOastwzi3SgUb1gnWxc3aNtFd6DRn9wU40mn-Py_S5D4pJ6hRj7Pzs1DSWdncJ-4SlWs66i6xO6uKcghPuM9Q10FgnHCcaC34B_Jk3Su9p6ZZLXVgRTWyW_T6KKhSuQsYUOryYSyTJcM-QaPvAMmxXqBytwWAMpCCyftgfpoGXTvNhkHyuI5xN01iUMuMw5KsOpImFIvBiKRKnf5k92sgyCZpl2rHSnoABU4dHdAgDF1ueXeVn7QBkDpVgVgvA7PYaL8AAa487-xvdmAUZEAIth4Gui961jLxqZK0OzWZtQo3E007ahwO18_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرشایمر، نظریه پرداز معروف آمریکایی: ترامپ با امضای تفاهم‌نامه اسلام‌آباد سند شکست آمریکا را امضا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/152165" target="_blank">📅 20:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152164">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdvtSG18k0dhx7Y81AjLeUsIpvh-sc9aqExuqvYT9BpHbhN5foPk3NqsLdC5Wg8mgwbZn0SBCdM0cDOXILXhe6ZyNP4tEC6GbUt16S4WPXLsFurlWtyhmAxua2bTE-EDl7Jg1p746clrfITRl2ZTnyuSMYirn06BdcthsiuxgYqMNyfQB2XePK6C3-PF8GO4DlmsrdaNhtdeGb6GTc8kLC7c3AgJqFSX3YX_qFqE8g6Y3aAEZjDO3nzcdwqAMfsxPtAtG3ZLaU3kznLYcZxHW30YABM_mSjvYqd5yL3Sr22XvoTHZ7DHCdms10VIbcNJbx3AWm-IjewDGTbl4B-FUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ در تروث سوشال:
اگر ممدانی می‌تواند با ترامپ به خوبی کنار بیاید، چرا شومر و جفریز نمی‌توانند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/152164" target="_blank">📅 20:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
اسرائیل امشب در مورد ایران جلسه امنیتی برگزار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/152163" target="_blank">📅 20:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/189ea383a3.mp4?token=AssNwKAZkkLZ5h5NcmMfsz6EzjJBqowNAf5etjYHOUjIAH5STd_CTZyCnbxqB3vw6m1ZOUPP5do6qIaVaCj2Pm_ZY67ZBaJjxBaK-pDbt7kb2W0nHOMpOdVDBPnDlvG71MlP2uSzkTkEld6BcEiVDAfksYStV0VcPcsDSYvQZG0xnWv_vCzlnOno7VCrDgYUmwICU1sDsJbGvdPi4VvS2NCGhvJ5GBydaVZcFzySmyFmzhxOQfXI_rntj7PSCiYsRSikL8a3l4iRf_Dr06Ewpl4gRc1pMXSSsyDlHLHXioWxeBs_YzwuvkabONPQdpRR9kJiT4Ig4cUXmLOhmUwMKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/189ea383a3.mp4?token=AssNwKAZkkLZ5h5NcmMfsz6EzjJBqowNAf5etjYHOUjIAH5STd_CTZyCnbxqB3vw6m1ZOUPP5do6qIaVaCj2Pm_ZY67ZBaJjxBaK-pDbt7kb2W0nHOMpOdVDBPnDlvG71MlP2uSzkTkEld6BcEiVDAfksYStV0VcPcsDSYvQZG0xnWv_vCzlnOno7VCrDgYUmwICU1sDsJbGvdPi4VvS2NCGhvJ5GBydaVZcFzySmyFmzhxOQfXI_rntj7PSCiYsRSikL8a3l4iRf_Dr06Ewpl4gRc1pMXSSsyDlHLHXioWxeBs_YzwuvkabONPQdpRR9kJiT4Ig4cUXmLOhmUwMKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان روحانی و ظریف علیه حجاب اجباری
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/152162" target="_blank">📅 20:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152161">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از مقامات ۵ سازمان اطلاعاتی اروپایی گزارش داد روسیه در حال گسترش برنامه‌های ترور مدیران ارشد صنایع دفاعی، به‌ویژه تأمین‌کنندگان پهپاد برای اوکراین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/152161" target="_blank">📅 20:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: دیگر پاسخی به پیشنهاد های آمریکا برای توافق نمی‌دهیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/152160" target="_blank">📅 20:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزارت دفاع روسیه: ما یک مرکز لجستیکی در میکولايف و یک کشتی باری نظامی که به سمت بندر چورنومورسک در حرکت بود را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/152159" target="_blank">📅 20:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن (حوثی ها): از آسمان فرودگاه‌های سعودی دور شوید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/152158" target="_blank">📅 20:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152157">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7Kr2zAge10P_GjRZ4if9wzyNnKaDlMSZLv8rCw8-N08dpep6G6o0gHL-n3JVXrcb3hif2nh6fxteSPUuTIXgDCvNEp187Ec91Q3fBHerpJ-PJ7UTXvjYTItV_-uT9XgzAtag421F1MiIZ4qt6oHTBDINVRhz84prlJbg1eOAgUjfcpdNKca-4iRRrbz5iP8Gzu3O4nWpJO8cWxNJ-QFqq8vPNGK83P2p1cg6EMTJGaADxOkQnLi16X9oUGYB4SR0GBHEWwlML9ux6cYLacnK-mgq3ipPnEQiA4PjGgHZIsMxPNkxSdM7hY1RqWyNoKLMbOx-5baads7AYyN8mMrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ده سال پیش با ۳۵ تومن میتونستی پژو پارس بخری، ولی امروز با ۴۰ تومن میتونی داشبورد پژو پارس رو بخری
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/152157" target="_blank">📅 19:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152156">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
هم اکنون گزارش شلیک موشک از جنوب ایران به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/152156" target="_blank">📅 19:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152155">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
انفجارهای جدیدی در شهر ریاض، پایتخت عربستان سعودی، رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/152155" target="_blank">📅 19:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152154">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
زلنسکی: هم اکنون با مقام‌های ایالات متحده صحبت کردم، اوکراین از آتش‌بس انرژی حمایت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/152154" target="_blank">📅 19:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152153">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: می‌توانستیم تنگه هرمز را کاملاً ببندیم، اما به دلایل انسان‌دوستانه این کار را نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/152153" target="_blank">📅 19:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152152">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
دونالد توسک، نخست‌وزیر لهستان، می‌گوید مردی که مشکوک به توطئه برای حمله به او است، دستگیر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/152152" target="_blank">📅 19:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152151">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
المیادین: نیروهای مسلح یمن به ۷ کیلومتری شهر تعز رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/152151" target="_blank">📅 19:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152150">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تهران به رویه‌های دیپلماتیک گذشتۀ خود باز نخواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/152150" target="_blank">📅 18:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152149">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
👈
فیلد مارشال محسن رضایی: آمریکا دارایی‌های بسیار گران‌قیمتی در امارات و پیرامون تنگهٔ هرمز دارد که ما هنوز آن‌ها را در میان اهداف خود نگنجانده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/152149" target="_blank">📅 18:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152148">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: اگه دوباره جنگ بشه اینبار به تاسیسات هوش مصنوعی و دارایی های ایلان ماسک تو منطقه هم حمله میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/152148" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152147">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سراج نماینده مجلس: ۹۰٪ مردم خواهان انتقام از دشمنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/152147" target="_blank">📅 18:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152146">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین درباره خاورمیانه: همه می‌فهمند که به دلیل جنگ در خاورمیانه، قیمت‌ها در حال افزایش هستند. آن‌ها به دلیل جنگ در خاورمیانه و مسدود شدن تنگه هرمز افزایش می‌یابند.
🔴
همه این را می‌فهمند. اگر می‌خواهیم با مردم به‌صورت منصفانه صحبت کنیم، اگر می‌خواهیم شفاف باشیم، اگر می‌خواهیم با ملت‌هایمان به‌صورت بازگشایی صحبت کنیم، مردم باید واقعیت را بشنوند
🔴
با مردم بازی نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/152146" target="_blank">📅 18:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152145">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1924f0c44.mp4?token=egHkD9bfqtXkwqbgojXWRTCBE3UZEReiC7QK0MV5zGvu_tCMImxvdc-ogzTQ0KkrMplE88gjxMPsgOrZYLkgTbcwvDPmE_Wg7075kCdGGD8N-7JUEND5CghAcpymBdwAbhOeBclTGE5AUBkUkEW_SWiHKOrFs5RJvNcLWAp0pdaLBPNlqwSmpO68qQgPdOD6AUsbXewEtScCRtr4BFdP6CERIN805M07Vf6s4bekkRE0FCyounImadtkszpKcY94LV19ik4uuoI57OOUtjHWWZH71kp2LrXVyFu3Ht3hdBNtZjm5nT2nOiK09vbYjkk5E5VCWcBBgm_DhiWiDLVSSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1924f0c44.mp4?token=egHkD9bfqtXkwqbgojXWRTCBE3UZEReiC7QK0MV5zGvu_tCMImxvdc-ogzTQ0KkrMplE88gjxMPsgOrZYLkgTbcwvDPmE_Wg7075kCdGGD8N-7JUEND5CghAcpymBdwAbhOeBclTGE5AUBkUkEW_SWiHKOrFs5RJvNcLWAp0pdaLBPNlqwSmpO68qQgPdOD6AUsbXewEtScCRtr4BFdP6CERIN805M07Vf6s4bekkRE0FCyounImadtkszpKcY94LV19ik4uuoI57OOUtjHWWZH71kp2LrXVyFu3Ht3hdBNtZjm5nT2nOiK09vbYjkk5E5VCWcBBgm_DhiWiDLVSSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از فرماندهان جوخه نوخبا که در ربودن اسرائیلی ها در 7 اکتبر شرکت داشت در عملیات مشترک ارتش اسرائیل (IDF) و شین بت کشته شد. او یکی از رهبران حمله به پاسگاه کیسوفیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/152145" target="_blank">📅 18:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152144">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f80c226d.mp4?token=ieUYGwZt-VaalxiPc5aP31b2-i7GkNhBWi_q2VBkavtc-Qf_AORizeYGGrc-Vh-YlDL6LXxitYIsKq6p1JnudVpsOc3GihTFoaN7SB53PmXAk8yDOTXHJLaDClULgyzChnL-r1AU572VARF4rHM0eu9IexzIcd1w2dXC49EhfamichRQQ-09Fa4qYISdxL5Ly1e1a6LSOJRVoH_k_FqkRNDeziO1RTKvEr5sHOWY4wj6j9dIrstce-YNMkUDKvmpVkQN_rykGB-6JTPceA8asVJyfQtlRvha1s5tHjHLRbFD2p8LgdD-u4lJFq9fA1Z_8wcwb9-xKHldq2vEeylr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f80c226d.mp4?token=ieUYGwZt-VaalxiPc5aP31b2-i7GkNhBWi_q2VBkavtc-Qf_AORizeYGGrc-Vh-YlDL6LXxitYIsKq6p1JnudVpsOc3GihTFoaN7SB53PmXAk8yDOTXHJLaDClULgyzChnL-r1AU572VARF4rHM0eu9IexzIcd1w2dXC49EhfamichRQQ-09Fa4qYISdxL5Ly1e1a6LSOJRVoH_k_FqkRNDeziO1RTKvEr5sHOWY4wj6j9dIrstce-YNMkUDKvmpVkQN_rykGB-6JTPceA8asVJyfQtlRvha1s5tHjHLRbFD2p8LgdD-u4lJFq9fA1Z_8wcwb9-xKHldq2vEeylr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین:
ترامپ گفت که اوکراین به یک رئیس‌جمهور جدید نیاز دارد.
🔴
با تمام احترامی که برای رئیس‌جمهور ترامپ قائلیم، انتخاب رهبر به عهده مردم ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/152144" target="_blank">📅 18:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152143">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f92ae82a3.mp4?token=vJbi3PABjdQxua7yKubCM2wYJYx_a2zcAKSLF4n99jMHrbERBp78txEPxgJc00cEn6j2xjL8WXDlPQuB9TYKzivmALiVc0n1iijsoYseDPB0vyzLpa6QZHL_rdarBEOxLjSo33-jBPncz3-KMFHM35_D2j6IsY3wfb03XXrNpeFPi9mQzP20LNlvlgbrO03RPrmoicL3ceMYISZkbWVL1Mj3ATv11yyNZuiJt_WBA404pXeB8X3AsJ54pKCjkUOdHAFk37qaKlBQTg4p7T0G9k_gQYJ-OwQ84Cbv9QAkMXh5lCCi0KvoMOrJuyQYwhJOLBnd0JqbSunDlFSeQbnY6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f92ae82a3.mp4?token=vJbi3PABjdQxua7yKubCM2wYJYx_a2zcAKSLF4n99jMHrbERBp78txEPxgJc00cEn6j2xjL8WXDlPQuB9TYKzivmALiVc0n1iijsoYseDPB0vyzLpa6QZHL_rdarBEOxLjSo33-jBPncz3-KMFHM35_D2j6IsY3wfb03XXrNpeFPi9mQzP20LNlvlgbrO03RPrmoicL3ceMYISZkbWVL1Mj3ATv11yyNZuiJt_WBA404pXeB8X3AsJ54pKCjkUOdHAFk37qaKlBQTg4p7T0G9k_gQYJ-OwQ84Cbv9QAkMXh5lCCi0KvoMOrJuyQYwhJOLBnd0JqbSunDlFSeQbnY6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین:
اگر ترامپ واقعاً می‌خواهد انتخاباتی در اوکراین برگزار شود، لطفاً به پوتین بگویید: به ما دو ماه، ۶۰ روز آتش‌بس کامل — ۶۰ روز — بدهید و ما انتخابات را سازماندهی خواهیم کرد
🔴
البته، ما برای هر انتخابی از سوی مردممان آماده خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/152143" target="_blank">📅 18:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152142">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68a497b55.mp4?token=sUVxWwcosuP4LBrZm-tBrMnkzw1PbxcdM4mdNDfMgFjKXQwMCiIyO_sEGeaqYS1z7l1MKrTUKisHOomufRhseTpUQ52T0S5IqNz5uWLdaoaTQhO7FqNT78gOrpRuSUO8gh6V-xLtYXeGi1mONDFyIA40oZ8ql-xirQ-SoxQqrX2JU6wWzyUwUSVAyNQiQTlXv-PdfZLEWS-S6qOHkGmPDcYe1imDC9RgAzeLPB2blt7xBvu4dcLbukVH40BtVOXFjuGBEm18wK3lMokkRWN6aNTX1p3c_fwIziR7_ZeYw6S4sMC0bRZvW9nF25Y8WLXsCcdlPamPTqeJ8BnOiE7naA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68a497b55.mp4?token=sUVxWwcosuP4LBrZm-tBrMnkzw1PbxcdM4mdNDfMgFjKXQwMCiIyO_sEGeaqYS1z7l1MKrTUKisHOomufRhseTpUQ52T0S5IqNz5uWLdaoaTQhO7FqNT78gOrpRuSUO8gh6V-xLtYXeGi1mONDFyIA40oZ8ql-xirQ-SoxQqrX2JU6wWzyUwUSVAyNQiQTlXv-PdfZLEWS-S6qOHkGmPDcYe1imDC9RgAzeLPB2blt7xBvu4dcLbukVH40BtVOXFjuGBEm18wK3lMokkRWN6aNTX1p3c_fwIziR7_ZeYw6S4sMC0bRZvW9nF25Y8WLXsCcdlPamPTqeJ8BnOiE7naA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین
:
اگر به دنبال آتش‌بس انرژی هستند، ما برای این موضوع آماده‌ایم
🔴
ما را حمله نکنید؛ بچه‌هایمان را نکشید. ما حمله به دیزل شما را متوقف خواهیم کرد.
فکر می‌کنم این یک توافق منصفانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/152142" target="_blank">📅 18:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152141">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
اسکات بسنت : ترامپ انتظار نداره تا حداقل بعد از انتخابات میان‌دوره‌ای، شاهد درگیری‌های نظامی جدی باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/152141" target="_blank">📅 18:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152140">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری / سخنگوی ائتلاف به رهبری عربستان سعودی اعلام کرد که دقایقی پیش یک پرتابه به ترمینال شماره 4 در فرودگاه بین‌المللی ملک خالد شهر ریاض اصابت کرد.
🔴
در حال حاضر، مقامات در حال رسیدگی به آتش‌سوزی ناشی از این حمله هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/152140" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152139">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa_TGxrsGzdVVLBMNMasCGy7zqtusIQAjUNtAj8GN7WBBRGi_zkD6TYa-efnfcdXPnwq8LtfImGr9wouPxHXcdFyaf2a_rxs6RKWBxm3isxBLUQtPG5__JpOx3pWIZPWH4ZZ0ZxYGr6AFOFlDInIJbN3ETfGhprbj9uZErL7CD5uDI4OHhlKeQ-uJkurvaemEp0UURbqxo95gWnaajD8VsH7dTjH0lDdeJIGhnEaRvCS5MWGW5AdiRF-XXjhVKG5yxFf3rSMuoge80hExEKFLqOT7QTu_FiPDTgsJ0Po0uYzXPbVkuGmqRXlGqSsendC6_CncQYZxkotUdQb61HGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: اسرائیل چشم‌انداز یک خاورمیانه‌ی قوی را در نظر دارد؛ خاورمیانه‌ای که در برابر تهدیدات متحد باشد، از مردم خود محافظت کند و آینده‌ای از امنیت، همکاری و رفاه را برای تمامی مردم منطقه رقم بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/152139" target="_blank">📅 18:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152138">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6sIy6HgtY4m2-tcnQYMVfNNqma799Bc991UF1THZv-IkUFZUJEopEFzC0aNf9w86WceFh0bbGg2uRi3W-f42RCk4eFW22JErKdu3gEb-0uN5Q-_zlFVU9gKLU2pcuLZFrheNLhsPWbpKp3XI7rj62RtvRXWMXEfJM4KpeB8hqaNTFBwfDZk3pH9PYFPQfWwkPPoqouXIVZLi2tU3Q-U6QywPZp0SwgbDGeFYfBmcpOTubAX2es3DuizWm383yW4AW-9ONzbz4YMeEIZyDhjYYFWK0ryY_pbzFDUsdyLybJnOjTLsv4_JuTNz-psov5wU31g3xYYaghhjRCHUDl5_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: از این لحظه به بعد، یک "توافق آتش‌بس انرژی" در جنگ بین روسیه و اوکراین برقرار می‌شود.
🔴
هر دو طرف با این موضوع موافقت کرده‌اند. لطفاً این توافق را نقض نکنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/152138" target="_blank">📅 17:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152137">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
اسکات بسنت :
ترامپ انتظار نداره تا حداقل بعد از انتخابات میان‌دوره‌ای، شاهد درگیری‌های نظامی جدی باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/152137" target="_blank">📅 17:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152136">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=krqdB9xM0TJehzHAlFz3pzZr0a3TiGAmWzcNKRC8XS1t41Qe74CT3jKwOjper_RkT_Rr511S7IJK6dkySsj_4N3srcCeHaedmbQn40E39DN1Fa0HZ17TP7z9KhztD-fIU_CGRXzGig3MyG8LViHB57eXP2DtMgTVOtsuUlysSEyURxBJkXEt5VGBENUPBDeKCpGdKLkNNI4hdRJcL8PEx6oIUzWdePbFWGuCCdR2vW4wtBOOMrKlsbHy23y2kxr-VE5zOmNMFYou3idU8_CfMG8LNS8jsCF1Cgor_bhS52aoMmWLZspGXmdXsV5e3HgWVosQazRyXjizDrDU5AzFGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=krqdB9xM0TJehzHAlFz3pzZr0a3TiGAmWzcNKRC8XS1t41Qe74CT3jKwOjper_RkT_Rr511S7IJK6dkySsj_4N3srcCeHaedmbQn40E39DN1Fa0HZ17TP7z9KhztD-fIU_CGRXzGig3MyG8LViHB57eXP2DtMgTVOtsuUlysSEyURxBJkXEt5VGBENUPBDeKCpGdKLkNNI4hdRJcL8PEx6oIUzWdePbFWGuCCdR2vW4wtBOOMrKlsbHy23y2kxr-VE5zOmNMFYou3idU8_CfMG8LNS8jsCF1Cgor_bhS52aoMmWLZspGXmdXsV5e3HgWVosQazRyXjizDrDU5AzFGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
بزرگ‌ترین بازنده در اینجا رژیم ایران است.
آن‌ها سعی کردند یک نقطه گلوگیری بر تنگه هرمز داشته باشند. این کار جواب نداد.
آن‌ها سعی کردند نقطه گلوگیری بر قیمت دیزل داشته باشند. حالا این هم جواب نمی‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/152136" target="_blank">📅 17:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152135">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=MbU6lFCXV2AAGJHAtwUxPZz_BHOL_34ofRPBAwNNhc_QUdevGavnLLRMtUQF10vKj5xcZX35vwj8U7YENRCZsyvUrw84cbhNLzvAtlbieIKZtgLrvbAhEfGRgFsIlMxsFi8ByQPyCKK903N2GmvDjnAj2gWMXKdAtC3Sot9SJS9okW8qsWirQ2Xq3f1RUJubkhYUmqaEOWcrOnJDmmD_FFMIyEOb2xD9useOC11vGQvrN02-p49E8GLaWeCI5MAcKREP8nXEzM6ya9urcUKL49n6-AtmWe9Ym53KmWhOtRustqjl9ESBNRgqq0yf5mdyI2MNmqrQ4rMVw-aa88fs_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=MbU6lFCXV2AAGJHAtwUxPZz_BHOL_34ofRPBAwNNhc_QUdevGavnLLRMtUQF10vKj5xcZX35vwj8U7YENRCZsyvUrw84cbhNLzvAtlbieIKZtgLrvbAhEfGRgFsIlMxsFi8ByQPyCKK903N2GmvDjnAj2gWMXKdAtC3Sot9SJS9okW8qsWirQ2Xq3f1RUJubkhYUmqaEOWcrOnJDmmD_FFMIyEOb2xD9useOC11vGQvrN02-p49E8GLaWeCI5MAcKREP8nXEzM6ya9urcUKL49n6-AtmWe9Ym53KmWhOtRustqjl9ESBNRgqq0yf5mdyI2MNmqrQ4rMVw-aa88fs_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
اگر این ایرانیان کشورشان را دوست دارند، تبریک می‌گویم، می‌توانید آنجا بمانید.
این موضوع به نخبگان ضربه می‌زند. آن‌ها نمی‌توانند به دیدن خویشاوندانشان در لندن، دوست‌دخترانشان در پاریس یا پول‌هایشان در سوئیس بروند.
آن‌ها از جهان قطع شده‌اند. ما فشار را ادامه خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/152135" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152134">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سفارت استرالیا از شهروندان خود در ریاض خواست که در محل امن بمانند و پناه بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/152134" target="_blank">📅 17:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152133">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فاکس نیوز به نقل از وزیر خزانه داری آمریکا: ایران دیگر نفتی در کشتی های خود ندارد و جریان نقدینگی آن منفی شده است.‌‌
🔴
پس از کمپین فشار حداکثری علیه ایران، اکنون به سمت کمپین انزوای کامل رفته ایم.‌‌
🔴
کمپین انزوای کامل با هدف قطع روابط ایران با جهان خارج…</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/152133" target="_blank">📅 17:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152132">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فاکس نیوز به نقل از وزیر خزانه داری آمریکا: ایران دیگر نفتی در کشتی های خود ندارد و جریان نقدینگی آن منفی شده است.‌‌
🔴
پس از کمپین فشار حداکثری علیه ایران، اکنون به سمت کمپین انزوای کامل رفته ایم.‌‌
🔴
کمپین انزوای کامل با هدف قطع روابط ایران با جهان خارج است.‌‌
🔴
با مصادره ارزهای رمزپایه و تشدید محاصره دریایی به ایران فشار خواهیم آورد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/152132" target="_blank">📅 17:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152131">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فارس: با پایان دو هفته، وعده بسنت درباره فروپاشی اقتصاد ایران محقق نشد و دلار از ۲۷۲ هزارتومان به ۲۶۵ هزارتومان رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/152131" target="_blank">📅 16:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152130">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52393bf294.mp4?token=lVzD_fWXfccI7lNIDDBbJF3q2u0OkhPhtLqDicTBShipHl4qUMB4cNVAowCsfUxfYRJiawor-G5O7aEhjvrqtI2Vd4UpeRXdX9KvCexs44Zme9qOtth2oLdsXdCVsdtc4rBoGVISsSbfhJiiWccr58q0fUoEy2t6C5tLdwkbpAovT9C3le9EJnQZpFrqcW2WlGiYq2XOMwhoG1VCxuHnw9uUjryVUivtGE0FeXbG3kgoQJOxFjhnexLuYZNq3kp4vij7HwJeQgIVNmOMixNg49g-QGU1DUh7vif7DqUEFTdciPPgXIOqPzqapnMKVVpRBB_lzRYfbG4eljVB9riJfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52393bf294.mp4?token=lVzD_fWXfccI7lNIDDBbJF3q2u0OkhPhtLqDicTBShipHl4qUMB4cNVAowCsfUxfYRJiawor-G5O7aEhjvrqtI2Vd4UpeRXdX9KvCexs44Zme9qOtth2oLdsXdCVsdtc4rBoGVISsSbfhJiiWccr58q0fUoEy2t6C5tLdwkbpAovT9C3le9EJnQZpFrqcW2WlGiYq2XOMwhoG1VCxuHnw9uUjryVUivtGE0FeXbG3kgoQJOxFjhnexLuYZNq3kp4vij7HwJeQgIVNmOMixNg49g-QGU1DUh7vif7DqUEFTdciPPgXIOqPzqapnMKVVpRBB_lzRYfbG4eljVB9riJfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار امروز بسیجی‌ها مقابل سفارت فرانسه:
🔴
مکرون حیا کن دانش آموز رو رها کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/152130" target="_blank">📅 16:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152129">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
صداوسیما:
درود به شرف اعتراض کننده های فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/152129" target="_blank">📅 16:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152128">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: با پاکستان و ترکیه همکاری می‌کنیم تا همه مسیرهای زمینی ایران را قطع کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/152128" target="_blank">📅 16:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152127">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
حسام الدین اشنا:
راننده تاکسی بازنشسته سپاه بهم گفت شما اینقدر نامردید و لج منو در اوردید، که از لج شما می گویم رضا پهلوی
تا بسوزید و این بلارو شما به سر من اوردید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/152127" target="_blank">📅 16:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152124">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sC_PUqHDvbKuvinN1OJNyioOSrhLq14IG0hZpGsMeuBBO-Pcx3G4mchvPCrU7UuzV7c9ZwSgebVRe_2Hloa3aGwGHkeeN_vbKVJzrnu2osekLEGvWFNre9ep5T56Ui3z-CLymJjCqeKETIf0QcwXPUyue5VVXH6HviWAh3yFUow3bJeh49CEKTqkqPT7f0g5V5IQAq_qHiSpgDVtcs-NBPOYVNdVN8_yIyiq5M5Qo9H6kv8pnSUNOACS2OBk1Rc0KG1j0HRaR-NKYCyFFmJgXBDQDCfVUqVFPAkqWGpUZdj-_YkztIYzN_FAJO0C9sLadsuQQoZN3DQXlqfw9gt36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9MI13mPAepaPrtMwkhGqHv25myT87xTZkNOgzvtKBtMGN2RgTzbOUG7gn9nlaWTa-f7F1oX2bj__mB8S52SG-gxR7jkkXte5mwhkdIc0G-WWbAD1teIiJkjNuSym3mrKQCwSM2hdz_Vr5Pt9Fu65fyTITlzxQ9CkKIThSFC6GGviFcuD0Amwgf9e8Sx_H3lr1W9EOnP130EkkV7mocfGMyFORbX_dAHBj85WUCQ_4VU1m56YC1qSSiI1BEyRV3TEEG_yOdPUbM_qbDkDGKUzbd-KIcFRPgCRXJ4EKte5I-ep-BAgiVbI8kl4go-eIgMxtu4GmTG2j-vcbUJRdm95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKDcvqk6XS1IJXNAcoKPDt58OfV__OdyEpnfHIJ028zBgVyNCGRevZAyNPdy9A1Bvpg_F46coYxxaBx4zkJWjEk65QBm_cmRGo2nllNI7AFLPJPC8V2iJTrdPh9FZeKMRM63iC4UOjPpmYvGcWxwXcs49gv30hXUvXV3QwYQwr6zRBjZli_Dp8A9s_a5DSAod5p19atLXqS0WH3tLYx-oJgnJqLFYNLbEk6mZXW9UtKHquy-lXEmeOhKHTvj7PoPZmNdc8BKiWOmJmKRJzDPc3GDh1Xe9OL4NPRtybgi5tAUiq4xc-wWdrqs3BVu91ozGMK--8E6vM7iaOvmYSm_PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هوای تهران امروز خیلی تمیز شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/152124" target="_blank">📅 16:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152123">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فلای‌دبی به‌ دلیل تداوم شرایط ناپایدار امنیتی، لغو پروازهای خود به مقصد و از مبدأ تل‌آویو را تا پایان اکتبر تمدید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/152123" target="_blank">📅 15:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152122">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cf041a409.mp4?token=gWKjZFiRKOn55CrOyEANtfl8yw-IpXCeIS797HgIpxBSIr-d2bZNvjdQXURkPcvL8pz91pQURAOSmOea6v5col80QJnUo-zMrQ1GE4KSIljt3xAS4v2yF4DPAMIWhtQSfkSpTzVqUSa8jkl3OzAz11vrdVDWFOZTZV2McRLzi2hRpF_cxuxUR9dOhe5C2GzapyVCnOMXfcCRHfww7DqwC-8SGuNt0lZN2stLhxtf7XbBxdUDf3kmozls1V9t_hIBiITQevYjjIra8ybMssUx0bvmAWWFpb6sZy1Oo1Gc-Gxa8MRPT2QN12-BI5tkOsdTvOl7p23u9n-Le_pP4CWKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cf041a409.mp4?token=gWKjZFiRKOn55CrOyEANtfl8yw-IpXCeIS797HgIpxBSIr-d2bZNvjdQXURkPcvL8pz91pQURAOSmOea6v5col80QJnUo-zMrQ1GE4KSIljt3xAS4v2yF4DPAMIWhtQSfkSpTzVqUSa8jkl3OzAz11vrdVDWFOZTZV2McRLzi2hRpF_cxuxUR9dOhe5C2GzapyVCnOMXfcCRHfww7DqwC-8SGuNt0lZN2stLhxtf7XbBxdUDf3kmozls1V9t_hIBiITQevYjjIra8ybMssUx0bvmAWWFpb6sZy1Oo1Gc-Gxa8MRPT2QN12-BI5tkOsdTvOl7p23u9n-Le_pP4CWKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر جدید از حمله به فرودگاه ریاض که دیروز رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/152122" target="_blank">📅 15:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152121">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
گفته می‌شه آمریکا پیش از شروع جنگ، نیروهای نخبه‌اش رو برای عملیات‌های خاص تو ایران مستقر کرده. هنوز هیچ مقامی این ادعا رو تایید نکرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/152121" target="_blank">📅 15:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152120">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
مرکز آمار: جمعیت فعلی ۸۷میلیون نفر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/152120" target="_blank">📅 15:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152118">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQRVaSirYta2EHyg6vjoKy4Iva_2kcKqVLf0Qu3rKZzDEZZDsVlAfqrUgi9poqXM7pfvReUt1wzK74tFae55kpShr-9rbybe4I1kXHhpivlEZEbM2xmQVACeC5yAawWUkqrDkNbYX6xZ0TF7wVxsRMZVaUryHhsPlWxRvJ0Zpw1FlODqr9l-hqLErHbF5p1vwfoOcBufcTiDxzJkvLVWGyJOYe3YVTYGnE8RiBPXa-Pdb-mi8jmfE9uDZL_xAocIAwQkbQCl3Bc5i0jIl_vEXcuhcpGSLxFupipPzUKoQKhzrYe82TuwJp18EKd11fQybHSzv58NHvTCv4U7-OxoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U29ugYadJ62psep8NeGpIPTPerDFcib02TxYC0JxM263_rmPKM-8yD1t3lhREOcfMuiTY7BvIg0u8_LZieo75YWqD-Picj2T1HQR0JUu-PTqZTiESIG4mfDAOA14V13gPtjxtQPjSksQxzvtf1u-MyWidjzBbkpIdNjZeECON39bQpJQflfRCyBpkb4-QrWfVkUCZSXvSOKSE7hYU462bhNyTCUGhQKYFpepL82hu7X1pco_tNvJFIz4gP5bckAY1qGprZnFDsE2-vCxGjg_QScmOd216EqXF1j6bvVKQ23tamQXzlwpyAJsO-JQma-ivHvNsWrynLNAiuOeUxOIpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر وایرال شده از رزمایش امروز جانفداها تو خراسان جنوبی و استفاده از کودکان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/152118" target="_blank">📅 15:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152117">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
شرکت فلای‌دبی لغو پروازهای خود به تل‌آویو و از تل‌آویو را تا پایان ماه جاری تمدید می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/152117" target="_blank">📅 15:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152116">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
خبرنگار رویترز: آمریکا ممکن است نیروهای نخبه را برای عملیات های خاص قبل از شروع جنگ در ایران مستقر کرده باشد.‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152116" target="_blank">📅 15:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152115">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea388dc62.mp4?token=MDJGKdbWxXZRT5KX2JPC4LOSklG0XqfP8LDaAIlasUjX6rOzkqnBbjfIBWwEJD-Fa2RlxTn4dyC5VMDlYfnNdgnGsR7h3qKDGA4P245vvi5aXYwV5kjeR9P4TRZBKTL5R2HweI5UxdmDBEq7wEqWoAmb48DjpiqeekWtw8hrV2OwVJtXi8dzs7RyYArypTa3qE5cR_QnNWIGBHv7FwHYz6cmjDs-SV3s3ZltUSfbQH30A5lg5oFHkaI_7f7CacDQA9YkUiGAVqr9jklYszw2GvCVhihO4xdo4d50s20d0Rd0sWm1xnF4j-E173zgipHG8FoiqMDTb2rE0N6XUFPMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea388dc62.mp4?token=MDJGKdbWxXZRT5KX2JPC4LOSklG0XqfP8LDaAIlasUjX6rOzkqnBbjfIBWwEJD-Fa2RlxTn4dyC5VMDlYfnNdgnGsR7h3qKDGA4P245vvi5aXYwV5kjeR9P4TRZBKTL5R2HweI5UxdmDBEq7wEqWoAmb48DjpiqeekWtw8hrV2OwVJtXi8dzs7RyYArypTa3qE5cR_QnNWIGBHv7FwHYz6cmjDs-SV3s3ZltUSfbQH30A5lg5oFHkaI_7f7CacDQA9YkUiGAVqr9jklYszw2GvCVhihO4xdo4d50s20d0Rd0sWm1xnF4j-E173zgipHG8FoiqMDTb2rE0N6XUFPMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای آتش‌سوزی‌ای را در سواحل عمان در پی هدف قرار گرفتن یک کشتی ثبت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/152115" target="_blank">📅 15:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152114">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
لبنان بزودی به پیمان ابراهیم خواهد پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/152114" target="_blank">📅 15:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152113">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
احتمال تماس تلفنی اعلام‌نشده پوتین و ترامپ
🔴
دیمیتری پسکوف، سخنگوی کرملین، اعلام کرد که ولادیمیر پوتین، رئیس‌جمهور روسیه و دونالد ترامپ، رئیس‌جمهور آمریکا، ممکن است تماس تلفنی دیگری داشته‌اند که به‌صورت عمومی اعلام نشده است.
🔴
پیش‌تر، یوری اوشاکوف، دستیار پوتین، درباره تماس اخیر دو رئیس‌جمهور گفته بود که هیچ‌کس نمی‌خواست اولین نفری باشد که تماس را قطع می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/152113" target="_blank">📅 15:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152112">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMXuJwL4MPK-MYPS05Uk53Joctqt_Hr6mwWdsSIuDcGZ30fzpAVSstMOU-kwXaLdau8eXT0JKKOAj5syts2V1IdHgSS6ziTpkHqI8pWQ0P2gUEXpXAUuqmb4dcjDGQBitFzkmU09JgQUNYBsp7UMfTf2_w_tZdWilqL3NAWICPD_SkGUz8AwuyTBGluo36aP7xExhc3xZ1K0NOYMXKHB2MAZMT1rW6wt_EaVnrXBX7SprI7yslrLFhDITF8oa531FlDHWNGDtUms_3Sv6qE1AUuEuZVEfyXGxI_LINGoD0LcrMDNyRjGrow3e_WZe2vr6KBvRl0SRhPctFLDcCzwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: در میان 8 کشور، کویت، لبنان و سوریه در صدر گزینه‌ها برای گسترش توافق‌نامه‌های ابراهیم (عادی‌سازی روابط) قرار دارند؛ طبق گزارشی از شورای امنیت ملی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/152112" target="_blank">📅 15:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152111">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUlo84umKfmQchJ35Mnueidmc79lWLlzoSpByNOIy2S1vuPuUCjzwgkgsuFSLX8q66ow2T0e5yeenSkzoSxWh2XdNSdKwpf1pCOWxEfyejiX3xzq3fdYd6m2QRPuF8MvxA8ay4uwfExHyHhOYxHH5lCRAXGJ1KXIw4d03WaLmTs67c8B7UNr7H1zt-h_nsq6AvAt-UASlGLj6Qu4rDZZV_UocvXTHIjd0c6vc1kbf4VUQjZJDdJz_q8g0qt-L13qhO6b2USzRPf0FRZE0ktBXClRTidQZe01eTtgcBjzo2mU8qJcZCV5sUpp7h9donBhtBS-HMKSzkymQFGd_YeylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌زمان با هدف قرار گرفتن یک کشتی در تنگه هرمز، آتش‌سوزی در این تنگه در فاصله 25 کیلومتری از سواحل عمان مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/152111" target="_blank">📅 15:04 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
