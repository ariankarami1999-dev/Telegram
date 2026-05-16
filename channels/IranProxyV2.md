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
<img src="https://cdn4.telesco.pe/file/hE2kS-yKzn4xzKwDEMy-233a6ijXgXA2Ol6IfeR62RiEShqFp5abq7HI911D3a4x5cRC3O6UY9QLwemqZK2dZ5kaSjEgO5XuBpEfjNhUJTG_xxb9wztGdHtCJNQUVDxh4cTg_2_hFlIEzXFElwSHo3OrpLDE3knlUSofn32mILaU2mAEhhVdepGuV_vpofpk1IKKw4a4CfSnZqQ4XX8u9Z-UIBskEJM1DBmcF5NRRUIyDA8TrghyeUm9xwj17N4e3Hc8YX-E5LLwZW7mTLdVKkEkmslb2PPGvCar3J9BzycKJb7U9KKv-HzE2wEgUa3Ny2vTr4z4HpekB9NWGBKWKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 37.9K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 20:18:30</div>
<hr>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)
‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)
‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)
‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)
‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)
‏
✅
✅
❌
❌
✅
✅
❌
❌
❌
✅
❌
✅
❌
✅
❌
❌
❌
✅
✅
✅
‏۶ )
🥷
𝐑𝐚𝐝𝐢𝐧.𝐳𝟐𝟎𝟎𝟕: ‏(۱۲۳
❣
)
‏
✅
❌
✅
❌
❌
⚪
✅
✅
❌
❌
❌
✅
✅
✅
✅
✅
❌
⚪
✅
⚪
‏۷ )
🥷
Matin: ‏(۱۱۸
❣
)
‏
⚪
❌
⚪
✅
⚪
✅
⚪
✅
❌
✅
✅
✅
✅
✅
✅
❌
✅
❌
❌
❌
‏۸ )
🥷
𝘿 𝙀 𝙑 𝙄 𝙇: ‏(۱۱۵
❣
)
‏
⚪
❌
❌
❌
❌
❌
❌
✅
❌
✅
✅
✅
✅
❌
✅
✅
✅
⚪
✅
❌
‏۹ )
🥷
Paranoid: ‏(۱۰۸
❣
)
‏
✅
✅
✅
⚪
✅
⚪
❌
❌
❌
✅
❌
⚪
✅
❌
✅
✅
⚪
⚪
✅
⚪
‏۱۰ )
🥷
Robert: ‏(۱۰۲
❣
)
‏
⚪
⚪
✅
✅
⚪
✅
✅
⚪
❌
⚪
❌
❌
❌
❌
✅
✅
⚪
✅
❌
✅
‏۱۱ )
🥷
♧: ‏(۹۹
❣
)
‏
⚪
⚪
❌
✅
❌
⚪
❌
✅
✅
✅
❌
⚪
✅
✅
❌
❌
❌
❌
❌
✅
‏۱۲ )
🥷
Zaker: ‏(۹۷
❣
)
‏
✅
✅
✅
❌
⚪
✅
⚪
✅
⚪
✅
✅
❌
⚪
✅
⚪
❌
⚪
✅
⚪
❌
‏۱۳ )
🥷
✗ᏦℕiႺℍᎢ✗: ‏(۹۵
❣
)
‏
⚪
❌
✅
❌
⚪
✅
❌
❌
⚪
✅
❌
✅
✅
✅
✅
✅
❌
❌
❌
❌
‏۱۴ )
🥷
❥sheyda☙: ‏(۹۴
❣
)
‏
✅
⚪
❌
⚪
❌
⚪
❌
✅
⚪
⚪
✅
✅
⚪
✅
❌
✅
⚪
✅
⚪
✅
‏۱۵ )
🥷
Ахмед: ‏(۹۰
❣
)
‏
⚪
✅
❌
⚪
❌
✅
⚪
✅
❌
⚪
⚪
⚪
❌
✅
✅
✅
⚪
✅
✅
⚪
‏۱۶ )
🥷
Ali Moheb: ‏(۸۹
❣
)
‏
⚪
⚪
❌
✅
✅
❌
⚪
❌
❌
✅
✅
❌
❌
❌
❌
✅
✅
✅
⚪
❌
‏۱۷ )
🥷
Vista: ‏(۸۴
❣
)
‏
⚪
⚪
⚪
✅
⚪
⚪
✅
❌
⚪
❌
❌
✅
✅
❌
⚪
✅
⚪
✅
⚪
⚪
‏۱۸ )
🥷
ㅤ: ‏(۷۵
❣
)
‏
✅
⚪
✅
❌
❌
✅
❌
⚪
❌
⚪
✅
❌
⚪
❌
❌
❌
✅
❌
✅
⚪
‏۱۹ )
🥷
Mohammad: ‏(۷۴
❣
)
‏
⚪
⚪
⚪
❌
✅
⚪
✅
✅
⚪
✅
⚪
✅
⚪
✅
⚪
⚪
❌
⚪
✅
⚪
‏۲۰ )
🥷
✨
𝒫𝒶𝓇𝓂𝒾𝓈
✨
: ‏(۷۲
❣
)
‏
⚪
⚪
⚪
❌
⚪
✅
⚪
❌
❌
❌
⚪
❌
✅
⚪
✅
✅
⚪
✅
❌
⚪
‏
👥
و ۶۳ بازیکن دیگر با امتیاز (
❣
) کمتر از ۷۲
❤
خسته نباشید
❤
‏</div>
<div class="tg-footer">👁️ 360 · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 351 · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3rPlQcaPtPh8U4_ICqlXV44a-Fzuh1Yny4rIq5WJSuMK9d_XN65XBxA5xIC6UgRppWgqHPqmdw3fH31632N8TerC3kJvMtLBeBmEWzqW8fayeBqo-foEYhigZ-uoctJ5hekQ8X_icVinxPQQiLrqQXqYbZhDneR0aiQ7zMhVYdoB2Xqe7vSYLiNoMTzX2vIjM8OHjLTBWNX7gK1jH_L-ckPJl-b-RlcKG5OqcVQVoYUqbbSjyGi-UNE1noqOiao87-HzUO9wbgMp6X3JLMrURINjjz8mFgh4JTn_Ysy645N2pCpgQupH674P8dcTmfzbAZDs7pi4Z21QP8ZH-UEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8391">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/IranProxyV2/8391" target="_blank">📅 14:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=JYES9QLXFNskB4tWVxChLoSreMbr7xgmBKe8HIpRkN9__R5ii1m7HD5HUZDTPZQ6j8TxemdW5SLegkcrsABmChmH1U1SQ_HveXXQBWvhoUxoseRtBk4YX-h4-Pzgpx4ZRRZG5q5K7hJ8_KJ_48jQaMLg39omVRINNKW8KXueCXpyH9jF-okXSkktXBSaB2NUEFyJ-z4EsEJms9Ig95JHmAadqBt1iOe0jhJTG_TyIxogVYKxWO9Pvn7Sg6DRzF63KwjaradK6wo6-oDMDzlQjJ7y5RfsUYJXSMsuy2A8sGtsEQlMzo7Mny4b5swyYQSpSEWRn7aRDcHNCEqh58YC2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=JYES9QLXFNskB4tWVxChLoSreMbr7xgmBKe8HIpRkN9__R5ii1m7HD5HUZDTPZQ6j8TxemdW5SLegkcrsABmChmH1U1SQ_HveXXQBWvhoUxoseRtBk4YX-h4-Pzgpx4ZRRZG5q5K7hJ8_KJ_48jQaMLg39omVRINNKW8KXueCXpyH9jF-okXSkktXBSaB2NUEFyJ-z4EsEJms9Ig95JHmAadqBt1iOe0jhJTG_TyIxogVYKxWO9Pvn7Sg6DRzF63KwjaradK6wo6-oDMDzlQjJ7y5RfsUYJXSMsuy2A8sGtsEQlMzo7Mny4b5swyYQSpSEWRn7aRDcHNCEqh58YC2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=KtrAvclS45jr6fdO28MYv5f5Inrp77u3Q4VZOfV2wdM58RSG_AAzc0P90x-ZpOzXaLDjHpcRB9_UyaHwdb_QINaZwt7ZSaGtKapQDcuZ2bUeH1zwgko4M5TxBp3isehyWVx18ZKVuP1ivOGbf_8dhVH168dN1L42KhUEgR5Y78cfLB0syRlxbYlK8M5rYcSvOlApEk7fgTAk28kGDAdnYbaRy8DpigQwI6Dln8qJFBZeXuy0a1MeWc2NRlDUG1hYoqkOZ2TGbGgstYmnGfmKPU2FVrLeMtwX6fCoQQWzfXG0HJhkYKeKUFCmkk1WhpNzo4itqVYKZkmolczqOd24JU4Gl5l7OQWchJH81FPplPjHnw83TJnHiwj4QZxj52_yjy6gW_bAM026Ot2boFpr76P_l5PJd4Yvt15QFMXQI-kjVG5I6VqaiJTk_zG80uOWrU5HWSchkJXEYXqeE5-qGePAa2-qKEwfgdp2VkANbiaL6tqY8SBkeYSekYzY4D9tvXoBPE0A_6jR1J8s9lkKVyOFI9733UaGt1BzNFEGHkd_mJb8gdEahKBx6XgMyHUFCBGhJujRz0yYls-AIWMPPGoR1AeGiFmnWnKbx_YO5Ldmf77G2XA63TFFJ38M5Rh3qvRvpUM1lpiKfx54S-nkDI6lg5o_ASUoTnqoHFIZb7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=KtrAvclS45jr6fdO28MYv5f5Inrp77u3Q4VZOfV2wdM58RSG_AAzc0P90x-ZpOzXaLDjHpcRB9_UyaHwdb_QINaZwt7ZSaGtKapQDcuZ2bUeH1zwgko4M5TxBp3isehyWVx18ZKVuP1ivOGbf_8dhVH168dN1L42KhUEgR5Y78cfLB0syRlxbYlK8M5rYcSvOlApEk7fgTAk28kGDAdnYbaRy8DpigQwI6Dln8qJFBZeXuy0a1MeWc2NRlDUG1hYoqkOZ2TGbGgstYmnGfmKPU2FVrLeMtwX6fCoQQWzfXG0HJhkYKeKUFCmkk1WhpNzo4itqVYKZkmolczqOd24JU4Gl5l7OQWchJH81FPplPjHnw83TJnHiwj4QZxj52_yjy6gW_bAM026Ot2boFpr76P_l5PJd4Yvt15QFMXQI-kjVG5I6VqaiJTk_zG80uOWrU5HWSchkJXEYXqeE5-qGePAa2-qKEwfgdp2VkANbiaL6tqY8SBkeYSekYzY4D9tvXoBPE0A_6jR1J8s9lkKVyOFI9733UaGt1BzNFEGHkd_mJb8gdEahKBx6XgMyHUFCBGhJujRz0yYls-AIWMPPGoR1AeGiFmnWnKbx_YO5Ldmf77G2XA63TFFJ38M5Rh3qvRvpUM1lpiKfx54S-nkDI6lg5o_ASUoTnqoHFIZb7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA9K9YlmMMg7dShrWVsl7nLLCVNPHQ1O1wNZUB-TbJg178DRlA9MAlZD1h0Prrnyy0g05d0wBRSO5Sc9LGC3PKWxXKGHRo1VeuSc5h3mBCu1rS2tYubor1HrvwivSLrAknR1JfXbGabFXkEzyiFUCjyDh1uGP4FgnD1GM4fo3lMN8tAXt4eRxyj-3uhuiZQKkGSb7QbnbVwN8Asx_1C3Szf6jYnLio_3mVZb8VNiFtUz-J-SY5qNMuNlQ8KUgyET9NZYgyV7-3tfszzjte7lR13CprncvWA8rgZsJJPmZ5UokPsUyKuJxDmxkJmp70IX0i8Uvtcc-iXyZZBAJqAjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8385">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوستانی که در شرایط جنگی از ما سرور پروکسی تهیه کرده بودند، الان میتونن بصورت ازادانه برای همه پلتفورم ها بدونه مشکل استفاده کنند، مشکلتون برطرف کردم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/IranProxyV2/8385" target="_blank">📅 03:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjjgIT3TtlkwnN6CYKBgUZILRyGzq3GyRoBj3_t5nzu6WZ4BYF43ApWqGjni0noTpgXLvilsnacHAyN8ao_PBJXUMpFxtiYA2O9MYkr4H3o3MFPhAzngM17T7O-9mHkdquNILioYxfqe0oCvVkn3y_E3VwsbxR9KOpfMVtghSd2lEnwYcx6km7ZuKOqi-k1JdE0B8Je7lEb2dM_ZoUPN4XX14SQmzsIECj1U2kp4x4C6OSsolqq261ZHj0j4oG58fe1jRayENZvjhmm5dsklvANTOA00TWhbBbk2hq4gkMUJeSymcpN_D1n7iTxiKipffc1xj08dorcAG_jEprE76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم سفارشات خیلی بالاس عشقا اگه با تاخیر تایید میکنم به بزرگی خودتون ببخشید، الان همرو اوکی میکنم میام چالشو براتون برگزار میکنم
😘</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8375">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حجم سفارشات خیلی بالاس عشقا اگه با تاخیر تایید میکنم به بزرگی خودتون ببخشید، الان همرو اوکی میکنم میام چالشو براتون برگزار میکنم
😘</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8375" target="_blank">📅 23:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
کد تخفیف حذف شد برای راحتی قیمت هارو آوردم پایین راحتر بتونید خرید بزنید
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OqaPlUtJOZNYJrRLjjafBsgAtfOHna83csDTkHp0ud4QWA4rJ33eDRvZdOTUEDN8MZGnpxLv13bjrVsk-LReP0E09PgyKxlaX-c98SIudDQUvwWNcZ9r2YB1TzSjpodFik136mbOJpmu1edlBPloptsPz9cb82I0HMU9rj_jiME9OHbPPqfljMsunJ1ZtMuub2kePmQuhU6VRATaeE5Jjao3OPCRqnFvlzDkZ02t2JkBge_THK3-EKEVNNoN8b9r85_MAr_a0VxdUxm3XgKb0TKxd7cyY4Xo1l2cwElEdiUNbeKrT5uRuFQ8CzpcwhV5Eh518iQDWz0tM07XnqQdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8370">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بشدت، بشدت حجم سفارشات بالاس،صبور کنید دارم یکی یکی صحت سنجی میکنم و تایید میکنم قلبا
❤️</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/IranProxyV2/8370" target="_blank">📅 00:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=BS3xVzKyzJtIAnkmjWH0EU3YV_pj0VqL7DNXLqOX9uued8lGYDPFo_32KfLCEW6vPC9o1p82ZacTrDI-YCe4MzI1eU6eqDNfjKPvvRjY87sOslnxB1Bh-pefVz9iUb6uAURvCF7zVl2xfO-al0iE_lYg5M5R4C0BmEEFoEQpxrXEEJ72u2qMvgqEjYUSoKVBI1GeVD2mThRKnskAtWv8vu7w5PGUQD8Hf_EzgAHEEUpD1wkWEHTvCwpgwnS1PLMQklFXnp2sGMefsPCwsDkqzLO3HEBQizAx7kUe-amtCH1AnkALSjAFklVwMniUT26o01rpMmmSWvpoEUw0pRlkvxiQsvr34nfCBHy-8GCGbt7O5UQOjlfpffDz0ADSyT_3fPlSpZU8uxvwHJgRoeZT8xVH_S8Gb-3EfKuMHarHVeSde3dU_bd_Mer8k24o8Rg8wbVWxySmepgq0aqhUB5pL3ibT4ju0g0aMhks5pmDWv9Sh9_w-vVEt7UPnZ2MqqU1txIeMjikAEhEdy1sVJTtaUR5pbk4A9XyX5AQhHerZ9xGsDNRkam8eBuWdFok9IkGGe_aU_UxJH6HDq4fvFKhrcteEnfvLYejBsUcXStcdaCGaUrP_g0r8oyGhbbqO8NkhXQhm5wcgftx7I5FZ0CP82CQWJgc5Dg89jgizXU47ps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=BS3xVzKyzJtIAnkmjWH0EU3YV_pj0VqL7DNXLqOX9uued8lGYDPFo_32KfLCEW6vPC9o1p82ZacTrDI-YCe4MzI1eU6eqDNfjKPvvRjY87sOslnxB1Bh-pefVz9iUb6uAURvCF7zVl2xfO-al0iE_lYg5M5R4C0BmEEFoEQpxrXEEJ72u2qMvgqEjYUSoKVBI1GeVD2mThRKnskAtWv8vu7w5PGUQD8Hf_EzgAHEEUpD1wkWEHTvCwpgwnS1PLMQklFXnp2sGMefsPCwsDkqzLO3HEBQizAx7kUe-amtCH1AnkALSjAFklVwMniUT26o01rpMmmSWvpoEUw0pRlkvxiQsvr34nfCBHy-8GCGbt7O5UQOjlfpffDz0ADSyT_3fPlSpZU8uxvwHJgRoeZT8xVH_S8Gb-3EfKuMHarHVeSde3dU_bd_Mer8k24o8Rg8wbVWxySmepgq0aqhUB5pL3ibT4ju0g0aMhks5pmDWv9Sh9_w-vVEt7UPnZ2MqqU1txIeMjikAEhEdy1sVJTtaUR5pbk4A9XyX5AQhHerZ9xGsDNRkam8eBuWdFok9IkGGe_aU_UxJH6HDq4fvFKhrcteEnfvLYejBsUcXStcdaCGaUrP_g0r8oyGhbbqO8NkhXQhm5wcgftx7I5FZ0CP82CQWJgc5Dg89jgizXU47ps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBrS7bJUT47UW7IQQYqBq4At6AXD4Wx_hN1h0Lc4kiVblpQvHmDqPw9196f_I6RnYsHJ9iRBwilH2m-rxPwYFQZxHYeJpb3bd8f_z-bLPQgyjI1nM4u7xrq0Jh4lyKRMesOGQNOvqaTjz1jTeY4M6K1UCnT48dHqusHfsrbAcfau4s8KvodxdrJERGBvlbOuQvkbWnWucTjDwoJlPZl46zrLWrd3cIGK9_iItTbiPxWmUzvSQ-tfQli38bahwhaiQz-PawpxVQLJp0gT94tNRzcaL_A_n2Ac8S5Trc1y3jInyX3MIGVBMgvvANA5KnK8z6czMciiMG2qAkVXfNhrQuOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBrS7bJUT47UW7IQQYqBq4At6AXD4Wx_hN1h0Lc4kiVblpQvHmDqPw9196f_I6RnYsHJ9iRBwilH2m-rxPwYFQZxHYeJpb3bd8f_z-bLPQgyjI1nM4u7xrq0Jh4lyKRMesOGQNOvqaTjz1jTeY4M6K1UCnT48dHqusHfsrbAcfau4s8KvodxdrJERGBvlbOuQvkbWnWucTjDwoJlPZl46zrLWrd3cIGK9_iItTbiPxWmUzvSQ-tfQli38bahwhaiQz-PawpxVQLJp0gT94tNRzcaL_A_n2Ac8S5Trc1y3jInyX3MIGVBMgvvANA5KnK8z6czMciiMG2qAkVXfNhrQuOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
وضعیت سرعت سرورها
@RUSSIAPROXYY
🇷🇺
📌
آیدی ربات جهت ثبت سفارش
👇🏻
✉
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYno3fTGxvw4_g8-c0ZWw1ACf6uq0DTcFtFpGiEYtHGCch87VT4LHu3ah7M1XjLfpZhOlnVy6-2RstXL7mH40ArGEEeB7iAiYVQWize9ZyBkx7I6tEZPdBFVKe87AunMNQ6RRZkqqfRXrFSO55B2ZNOGEnVoUAKipGPPtg7dQOqBnvD2_rQQmXIBNAHioY0MexdddZ1XnKvL9Taz5wgjsho-2DMvBHeGGJl-aR0-Wg5lcIYIswcKFGp3Em2exVSpA-1pZ8LDq0piQhiVqFXuJCIumHvYjc9xVW6KcCOJ4-W3bcB3-IItkmYBG-7l5Cp1m4nNcRvXWSvTwFVn-neCpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL7wRHC1WJonoXFHsce8myXWeqhB3DjJvrRfy7CgVUEXNQderflj0t9sBk-4qxWdDaCpmt01HQURzYUiZJetTZxEXR22osYktqkJwAJxMQT3Z6U2Ljx3nChAndYzqKVX7IFE1VSB_9C4zaebTFadKmaDEOU0S7ftmLAWfaF1h3awZvgRHhQ3DKmWUoJLteH6HJiYaDzs7sfZxNqxL2BSkv7pbHggpfQFh24a9mvGho27E4I3MbxfLaagLAM4aQwpySCaF3Te_bPZGIdGIQ14rINHlsY-fheeaZ32MXH_FL11da0MQLDZEECOb1Xa_sbdhRDkImk3kTEFwzcGB9QC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=rREP8VWKaoj8wi4O9yKWxVy3eAKpWA67zktsSjWbkEkVMOejQec1maOovfkYGtLb3zERxa7Z_CQqxhhJiEybQoaYoiXDJMBu-3BhxFMybcIG_wEOs0_hEc1CkFTAxXljQ8rlAr005JnaggIZduWtvC2GyPTXdOPItGBY9aDQnwmD1M58xwVuwk2GIzzo5BLlzvoq474MabGrqjC-TWIrQ7WDR-Bim3UjTyKsOqqK5_v-QSoLftclYP5vG7USQb0Vf5FcM6zsXCnNu-xfU8-N6pfYmJloEHV1z7Yop1xVsjDftghEa99U_C2g0yHOPanIu0lWifjJHOdNpqIehkvgpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=rREP8VWKaoj8wi4O9yKWxVy3eAKpWA67zktsSjWbkEkVMOejQec1maOovfkYGtLb3zERxa7Z_CQqxhhJiEybQoaYoiXDJMBu-3BhxFMybcIG_wEOs0_hEc1CkFTAxXljQ8rlAr005JnaggIZduWtvC2GyPTXdOPItGBY9aDQnwmD1M58xwVuwk2GIzzo5BLlzvoq474MabGrqjC-TWIrQ7WDR-Bim3UjTyKsOqqK5_v-QSoLftclYP5vG7USQb0Vf5FcM6zsXCnNu-xfU8-N6pfYmJloEHV1z7Yop1xVsjDftghEa99U_C2g0yHOPanIu0lWifjJHOdNpqIehkvgpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xqopv3uHJvJ6_8qIpLk-ZP70LiNpIiopcAPotJkRWDHD_V3Y2qd_8b5bj0a9qJvPmv62GJvI0-7iNEjoEsitR5fD6JhvR2Ir0qgY2wpJFUD3K6ix-J66sl2njrhBAvidVm1mCU7qPou3R6NNsxyG4tdBq72cAJhbKy02K9V7bpTQvfSX3ygst1cPTaerAcmhnzDP0_58iZLAGg73Y84Pz0um0f-aQGSfqSyQxBtGnksFqK9J5XMDV7enDyNbsSUavQHs2b2lPisr4q98Tz2hYqlK2NKOQZdXS3dEFlxOcrI0dhVHnOD-EncQiuWpelzI3J-zgsFjfBoDfL9OJAr-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbTWTPoIn1DYdaLdMvUVoubQa77R9jj-AYNfFEH2-YLUKpQG-yIzAuXTkh_7W843vsUEXEG5rz9u7FzOlTKmeEsyt59wTV3E5-sMlKbtr8DIMxp8WG7Fz0vWLjD5qEJ6zp2uCG0dB6Hkt8ydNhzC-6jlDEdSbmskGlAR9V2jgOYUMpIQl-kr5On1B2ldYTsoHiSaznEOpHCB9PmO7COVzOxNn7GZOyu56MSW0f63etlJKBlkwQQCRJo-uK0ZF9A5qjv_Azthp3amvZHTjn5r-82vJmUqOAJKLKubYLI3QpW8F7HMIwnvY_g9xFXzNBWaendrqKVI4_ToSU4DKHVZhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq68a_0CAkhHeLgg9myVRKR0Akk77yJ94RNzuOSHQ-s3vkNTlltY2gIB9VfO_uDIllBtQWvsIHwGJH1EvlBVqHTjqFwbn-eUUahzXY-uh3JU_aYQbQSzpn6QyZ9lx8KfRQh0S2r635bTqUy7eoCK65CE7rdgSzQnTt2CVWfzW4MkUxdF3bFMkdTPLGgy6SVto9Kl7hwMO4ZaLYRF6-eRXMU9e9w-CovKRHZu0IlEZpCG32RE1XtAdPwBJ8Y0Pgkg6oD4TrLfhDup2wVLWunppJhV1SQ9CBdY65B5GRuFlxttFkpEn4kWn6hz7WMXW2tZkIMWzUuh5BIxi0D4hHYRKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قیمت‌ «سیمکارت سفید» و «اینترنت پرو» در بازار سیاه چقدر است؟
🔹
اینترنت پرو و دسترسی بدون فیلتر از طریق کانال‌های غیررسمی و بازار سیاه فروخته می‌شود.
🔹
قیمت ۵۰ گیگ اینترنت پرو در بازار سیاه تا حدود ۱۲ میلیون تومان اعلام شده است.
🔹
سیمکارت‌های سفید با وعده اینترنت بدون فیلتر با قیمت‌هایی بین ۴۴ تا ۱۲۰ میلیون تومان فروخته می‌شوند.
🔹
فقط اقشار مرفه توان دسترسی به اینترنت بدون محدودیت را دارند و این مسئله شکاف دیجیتالی را تشدید کرده است.
🔹
کسب‌و کارهای آنلاین و دیجیتال از محدودیت اینترنت و هزینه‌های دسترسی آسیب جدی دیده‌اند /اقتصادنیوز
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmFMgQrrcBWVt-kAaLMnW-K4E9HyuS3cD2wBSDK9pRC21gUEZBRSCmx3dVIyw4Qh67HmIM7hFckLkEfLbrPBo2GWfHOb_gNCn5IIvu8ryL5ROBr5mgjzlLj2351lv6gG839ViuLCLFNUEyf5agcBrkQQTWt7ZjRgDu-0J-twoUcYS6yUjkggqRVeCx3KB_RPYPf55Qxm1Ph1x0xq3DavUUjl9Z455rRyf52e5DR4aAd_HqmhyaLGNw797975-vmX9IAr2WnbxhQlFw8QJxROUeNvw6JwqwL1CoqQcNV1Mc-cBrWOM3mWxHLX0am0k_3X5ewomCF9pFdEJhmrHYliXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره،
دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول بدین صورته که شما کانفیگتون رو برای پشتیبانی ارسال میکنید و همون حجم باقی مانده براتون با ضریب دیگ چنج میشه به سرور ثابت البته با سرعت کمتری
2⃣
- روش دوم سرورتون تبدیل میشه به سرور تانل با سرعت بالا مث سرویس هایی که درحال حاضر در ربات هستند ولی، ما به تفاوتی باید پرداخت کنید بلا عوض
3⃣
- روش سومم اینه که کانفیگ هاتونو نگه دارین بعد از این شرایط نت از حالت ملی به حالت بین المللی تغییر کرد به ازای هرگیگ، ده برابر اضافه تر حجم دریافت خواهد کرد
🔻
@RUSSIAPROXYY_Admin
📌
به این آیدی جهت رفع مشکل پیام بدین
👆🏻</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbRQ5mIrgXSnAoY5DUvd6dZa737diJX7hCiPtWUla8I7ZS2pnQz-cSCYH6L7yNwjCMG-qzeN-8WetEQsEr5M3RVk4YEgn6rIU5jqrVUPnQOX-CycI9iKqDrfL7yyP3ZMVU30kkTqrGCTSchz-HZi4szN9v-ubBmjAHy-Trb26B670CbB5_WBzJqdRHdDEQczN629kSTAToiATFikQ7moIxBmGRdKTx4GuA9pvlVGEszSWV4Nb8-YpFgZYUIs3DedzN2YGXN41OWHsTalQmV3Q32arl0Jk9mtGs3B5XJYYqS7m8Sc9fUhP4yN7tW4XsLXSySudvS-ll8hgndmcTIlXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✈️
دوستان نهایت تا امشب سعی میکنیم سرویس سرور تلگرامو اوکی کنیم، هواتونو داریم همونطور که وقتی هیچکس وصل نبود تو دوران جنگ با کمترین قیمت ممکن و کمترین سود ممکن بهتون بهترین سرویس ارائه میدادیم، سعی میکنم از جیب خودم هزینه کنم تا مشکلتونو برطرف کنم نگران نباشید
✈️
سرورای ثابت برای نت بین المللی و کلیه اپلیکیشن ها و سایت ها و... براتون تو ربات با کمترین قیمت ممکنه قرار دادم بازم امروز
قیمت هارو کاهش
دادم که دوستانی که شرایط مالی مناسبی ندارن هم بتونن کانفیگ تهیه کنند.
✈️
🎥
📸
💬
👾
📞
🤖
🔍
🕹
📱
⚡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de826422e1.mp4?token=QwRDC6y7ckmeUEE-PdZMZD5EOPRV7LlsO7OvBQtnwEV7WFTOcBK_-4ca1v0tTkieMc61qU6wYsTj6eESM5NM0UhKH91nxL9mknqoMKKTFQkhLqg5KATptkUp26HhcsDwhlWct84BKE-IcCE2EhSZdhjyvGKiJq4J05qbb8AGXx93ZlNItPk4MvA34bspP0Zb1Ieho5i8crMfiRBxBMZDoF-MVC5_9YdV8jgzCH1BADEoznRIsDIlpQuj3wwjQODc4CsJAL4tpMVYjnB4fww47NdAW3BITzt9X6Yzkx9hweOH5jCvX2Rv9u9QAjj7xr-As1cuTetE-BW_ls6yAebEUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de826422e1.mp4?token=QwRDC6y7ckmeUEE-PdZMZD5EOPRV7LlsO7OvBQtnwEV7WFTOcBK_-4ca1v0tTkieMc61qU6wYsTj6eESM5NM0UhKH91nxL9mknqoMKKTFQkhLqg5KATptkUp26HhcsDwhlWct84BKE-IcCE2EhSZdhjyvGKiJq4J05qbb8AGXx93ZlNItPk4MvA34bspP0Zb1Ieho5i8crMfiRBxBMZDoF-MVC5_9YdV8jgzCH1BADEoznRIsDIlpQuj3wwjQODc4CsJAL4tpMVYjnB4fww47NdAW3BITzt9X6Yzkx9hweOH5jCvX2Rv9u9QAjj7xr-As1cuTetE-BW_ls6yAebEUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شهبازی مجری صداوسیما خطاب به مردم ایران:
اگه اینترنت 5G که افغانستان داره و مسترکارت که سوریه داره اینقد براتون مهمه؛ خب برین همون افغانستان و سوریه زندگی کنین!
﻿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8316">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⭕️
اطلاعیه:
وزیر ارتباطات گفت در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم.
همچنین طی پیگیری‌ از ISP اعلام کردند که اینترنت بین المللی شبکه خانگی متصل شده است اما هنوز زمان مشخصی در مورد اتصال دیتاسنترها به اینترنت بین المللی وجود ندارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8316" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8315">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=qLS0QqdGlHIgdg5Go9SHxp0_qmRznIuNnbQAs04PIDRv334zDr3DpYdlocUiVhugjrMRV4E_eQn9mPXr8AxdvhkHBjy6948PmDZalTOGAcgxcoZp88O4YkeO0va7TGnLlQoHIf9MRjL4-XmkymdBVsgajd29NYCJpwQa8Ux7v_IulTkHjEz7iTkJ27qY1zhiKKgbvZiCHjS274MYBV8Rwy_l2q2tkQNGvSyPLrW5iQobzSvyalcfdyKOFJOBWGu_Zb7Q-_0eVjA1m1_mPO68e1tfnnK4en-kvOAng1fON6kZKCafgbapghNYACcSjN-WDBcQgBrorbFswoJ21rPU8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=qLS0QqdGlHIgdg5Go9SHxp0_qmRznIuNnbQAs04PIDRv334zDr3DpYdlocUiVhugjrMRV4E_eQn9mPXr8AxdvhkHBjy6948PmDZalTOGAcgxcoZp88O4YkeO0va7TGnLlQoHIf9MRjL4-XmkymdBVsgajd29NYCJpwQa8Ux7v_IulTkHjEz7iTkJ27qY1zhiKKgbvZiCHjS274MYBV8Rwy_l2q2tkQNGvSyPLrW5iQobzSvyalcfdyKOFJOBWGu_Zb7Q-_0eVjA1m1_mPO68e1tfnnK4en-kvOAng1fON6kZKCafgbapghNYACcSjN-WDBcQgBrorbFswoJ21rPU8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی:
اینترنت حق مردم است؛ عصبانیت مردم کاملا درست است/ عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8315" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8314">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اژه‌ای: اینترنت پرو و سفید مثل پتک در ذهن مردم شده است
🔹
رئیس قوه قضاییه در جلسه با وزیر ارتباطات: مسئله‌ اینترنت پرو و سفید مثل پتک در ذهن مردم شده و باید با موارد خلاف قانون در این موضوع برخورد شود.
🔹
در این جلسه دادستان کل کشور و وزیر ارتباطات به رئیس قوه‌قضائیه گفتند با بررسی‌های صورت‌گرفته، احراز تخلف در قضیهٔ موسوم به «خط‌های سفید و اینترنت‌پرو»، قطعی و حتمی است./جماران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8314" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8313">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">vless://8b7dbddf-fe0a-4405-b8e9-bfac4d9439ef@185.143.233.235:8080?path=%2F&security=none&encryption=none&host=MHI.ARTARONA.IR&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8313" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8312">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">V2ray + Psiphon:
vless://3728fc28-910c-4a9c-888c-c08c3e2f4a06@snapp.ir:2052?encryption=none&type=ws&path=%2Freq2&host=snapp1.gptpersian.ir#musiclovers85
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8312" target="_blank">📅 10:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8311">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">احتمالا اکه پروکسیا درست نشه با کانفیگ های ثابت جاشو براتون عوض کنیم اطلاع میدیم خدمتتون بابت صبوریتون متشکریم</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8311" target="_blank">📅 00:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8310">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حجم سفارشات ربات بسیار بالاست موجودیش تموم شده بود مجدد شارژ شد، صبور باشین، دارم یکی یکی رسیدارو صحت سنجی و تایید میکنم با تشکر
❤️
💲
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8310" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8309">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CX3PvSkFkiaalUmIbQqH11LMQXLI6nYKTzbmPkvog_ElN14FOymcyM184w1hIi2E5LsRwDGnKDIRmsbB00H4B1p1i8wUUbQDLnzy7EC4eok5qPDetbGswffDBVHekDKqVO2neLxTEW1MNf7KDlL0f5EssGvGVwyKD0yvO5F6Neo28FwqkKLh1MaeOfxTfd3bnRxiy7ehEl6ZDK8L3Ll8G4gq7ZkjeteOaw_-7ryMTbsvmaYJo7hEaV_HvuSon2YkRRuEfRi3tirhlQGqr0ZqP-T2CTfGNyvJnnOWurbnU5NOV35_fxPodA6Xglkyz-Boyc75GyF4ijwg6QP7JDT5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه چالش دیشب، برد 2-0 بارسا درست پیش بینی کرده بود
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8309" target="_blank">📅 23:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8308">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
معاون علمی پزشکیان:
حتی در شرایط جنگی هم بستن اینترنت راهکار نیست، زیرا وقتی کامل بسته بود هم ترورها ادامه داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8308" target="_blank">📅 21:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8306">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚠️
ترامپ به فاکس نیوز:
‼️
در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8306" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8305">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=FiD8sGdGxXJ2S_qPwjS7JPzXu0N4MYmI9tKy-3A33d02p0tiWEfRf1Nn7dMLT8Fzub25KKv6wYZPCoGl4WTsmiefmOHvQ2I8G3vE-7ozX_QotVxg1eoKIPQBalFFDAmsWzk5GTLjQ7WS3rzyivF8oISp9TYAd-j_UfXxudI2HqM8780w42RGtOkXl30QLH04l7kW-jYBF6KwgGUkcFlQ56gtwLA4rFpz8o5bjLMzQqusHnXzlJawSiIC-LEJADBlH6Fa2-S4bv9tpXRhqPLlolxIhblLHCCZmabCBnSC2UTMIPdnddAzVATAa_ljvTA6g7imDGMW0nsXIGIo4gkPpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=FiD8sGdGxXJ2S_qPwjS7JPzXu0N4MYmI9tKy-3A33d02p0tiWEfRf1Nn7dMLT8Fzub25KKv6wYZPCoGl4WTsmiefmOHvQ2I8G3vE-7ozX_QotVxg1eoKIPQBalFFDAmsWzk5GTLjQ7WS3rzyivF8oISp9TYAd-j_UfXxudI2HqM8780w42RGtOkXl30QLH04l7kW-jYBF6KwgGUkcFlQ56gtwLA4rFpz8o5bjLMzQqusHnXzlJawSiIC-LEJADBlH6Fa2-S4bv9tpXRhqPLlolxIhblLHCCZmabCBnSC2UTMIPdnddAzVATAa_ljvTA6g7imDGMW0nsXIGIo4gkPpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت زندگی مغازه دارا و آنلاین شاپا بعداز ۷۴ روز بسته بودن اینترنت!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8305" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8304">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
تصمیم‌گیری درباره بازگشت اینترنت به وضعیت عادی در دستور کار دولت
افشین، معاون علمی رئیس‌جمهور:
🔹
در دولت یک کارگروه زیر نظر معاونت اول رئیس جمهور برای تعیین تکلیف اینترنت در حال شکل‌گیری است. احتمالاً در این کارگروه تصمیمات قاطع خواهیم گرفت.
🔹
وضعیت اینترنت در دولت در حال پیگیری است. نظر دولت بازگشت اینترنت به وضعیت عادی است. قطعی اینترنت قطعاً به رتبه علمی ما ضربه می‌زند. در زمان قطعی اینترنت رتبه علمی ما پایین می‌آید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8304" target="_blank">📅 16:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8303">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">dalage pezeshkian 2.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8303" target="_blank">📅 15:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8302">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">داریم بروز رسانی هایی میکنیم که  سرور های مخصوص تلگرام مستقیم وصل بشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8302" target="_blank">📅 13:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8301">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fni36B9Evh2UXqPH6yyBWnbwh3_mf-ZyIN6WBU33PqLmJmM8b3sUeDF1CAeKmPD4I6z1Io_kiz10WDVAB5COlfPf9yEmCzi4cED5yhQaRUdkhdbpo0TWdze352u7Unwy-ZSCNuAFgRqDbU3vPwuE7ssZn4F3WETxIvJ_P980_KRPwYY_NTaRjwNJmn0Ydjlbib7syTvjLcSDdNVevcVg7RTx5IdmB0ACaC9YDrekRGhba1SCoHKMa-ko7jQjuH5oh8Ab7avOP6UnKtOSZtvA6Cz4RNxML2zt9CzG6eBE7wZejIT5KI4dvWDwuoNfnykg_w2EY8t6Ek85_13FRGt1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
جهت اطلاع رسانی مجدد همچنان در تلاشم، که مشکل دیتاسنتر خارجمون رو برطرف کنم برای سرویس سرورای تلگرام، درحال حاضر همچنان فروش سرورای تلگرام از دیروز تو ربات غیرفعال شده، نگران نباشید برطرف خواهد شد
✔️
فعلا درحال حاضر سرویس های تانل با بهترین کیفیت و سرعت ، تنها سرویسمون که روی تمامی اپلیکیشن های
🎥
📸
✈️
💬
📞
🤖
🕹
📱
🔍
قابل استفاده میباشد و برای تمامی دیوایس ها واپلیکیشن ها اوکی هست، در پلن های (1 گیگ، 2 گیگ،3 گیگ و 5 گیگ) تو ربات موجود میباشد برای ثبت سفارش
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8301" target="_blank">📅 03:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8300">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
صدا و سیما:
ایران آخرین پیشنهاد آمریکا را رد کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8300" target="_blank">📅 01:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8299">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اختلال شدید در اینترنت داخلی
🔵
متاسفانه از دقایق گذشته اختلال بسیار شدیدی در اینترنت ملی ایران رخ داده به طوری که cdn آروان ؛ سیستم شاپرک ؛ سیستم همراه بانک برخی از بانک ها همچون بلو(سامان) و... قطع شدند یا دچار اختلال شدند.
🔵
بسیاری از سایت های ملی و داخلی نیز باز نمیشوند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8299" target="_blank">📅 00:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8298">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رفقا پروکسیا مشکل خوردن مدیر فنیم داره هر جور شده مشکل حل میکنه از صبوریتون متشکریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8298" target="_blank">📅 00:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8297">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8297" target="_blank">📅 00:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8295">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8295" target="_blank">📅 00:14 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8294">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARMZcejLNafHOpoZJdltt1Rgnui8O7JptEoXwoLaupGU6rGEvtUA8R-Xe7KAbfWyiA04x-xNeY4kl6UotTPQn0MUMkjnvdN6OWwoNeC0TSommpELYzD9PM2bGhrvM5kHyUqECSnenu61e1i3uEDWUfKCGSEKoLx5IknwW4X4NTwhty7Fgr7OQ_PPeZSuEZyLGDzsVv2PjvSkBpEAtXWrjfgOWBdToYWpeHN06FPR2aBaLMkuVcUbNmbeBd_LxBhd64H5h4viIFxgJ2l4wGCc4AejPS84g6MaZsubSnXKVryg77tKDiRFJ2bUo4i0S4QKl7WpF31QYFu7ohc6HAIqdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8294" target="_blank">📅 23:59 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8293">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8293" target="_blank">📅 23:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8292">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=SQoeLa-wqtqe0SK8kdlDwKLJ2SBl_vcUQSbJu0dgoZwzsaKnsnDxp4t8TDB8ZRwwZ3O2zpEZUta2yl0sOa2KNsVg0s9-K4LKpmGBMsFRMToziFPxFh_mcuWyADNEM6eEwtNdYAq5SfQO3Ahlwt3drXnfALXRlscTboxxb78ck5FwYCyelSkld2u8mQheKvz3_VAj5oV9lHMOFXBrpzBibDBxrIAf6k4rx_T4JXR7_7KyCBFcDu8kSVF67K08pfnu82LQiuI7PhWk_H3Py_aVby8vKU9Bf00A0jQuQTff5sUFnliJYi4FF0eoID_mFc6yL66-uiTPP1avFX8aKbAMFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=SQoeLa-wqtqe0SK8kdlDwKLJ2SBl_vcUQSbJu0dgoZwzsaKnsnDxp4t8TDB8ZRwwZ3O2zpEZUta2yl0sOa2KNsVg0s9-K4LKpmGBMsFRMToziFPxFh_mcuWyADNEM6eEwtNdYAq5SfQO3Ahlwt3drXnfALXRlscTboxxb78ck5FwYCyelSkld2u8mQheKvz3_VAj5oV9lHMOFXBrpzBibDBxrIAf6k4rx_T4JXR7_7KyCBFcDu8kSVF67K08pfnu82LQiuI7PhWk_H3Py_aVby8vKU9Bf00A0jQuQTff5sUFnliJYi4FF0eoID_mFc6yL66-uiTPP1avFX8aKbAMFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی و فرماندهای سپاه:
@
RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8292" target="_blank">📅 23:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8291">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ho4pkdDstqiOzxMZK1EA4MrGmZcmVlYiaq8xlykrL6p-jkNvqev3q4nnWq5NNRSxUhZVErbRbrOBDUeBjFlnpAfpvYONwZvqiXAE0GDx_z1RRba2KQ92qj6yNOyJVTqO6MhwIGzZ-XyheGeJJCL_zPcyk9_T0TZr8jBU_tXOJ3MwU5479v9KXy_KIg8QHXTLUvCyGIOOHN1Iy6I-9BEwzwBr-piuI1HrTT3KaTbkjofBag7OwKcBu3aaYy3vhRhGDXjISMbdp9TPc09WU5S0x8WpUb4n52-yRaq7YLi5bvh9Ln0OTJg6hJx_dln39pl-f0y9FTrSSn3j4p3WY3pjqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)  و سپس سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» آنها رسیدند.   او نه تنها با آنها خوب بود، بلکه عالی بود، واقعاً به طرف آنها رفت، اسرائیل و همه…</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/8291" target="_blank">📅 21:55 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTX9aRh8_QNW8RGSg05vMHUpJ9Hzq4q45AM8PV137YjmrG1hzvdjGs1i-wtIHk3Swy2kzE0dKOQ2_YkZvjvESmM-9EGGq0CqxHimqlintY5CZCIQ9xWIJifIo51kDuC5NiBL39AnXFTCUpJyL20JAjrVaQnSZsN39M_B2PT8Hn96xocHGplfoTsn1gp2RjO6jyPA2eCLN-Z0_QNjWLTOA18_qC0_WrhrHx6qiTAOVQow8WOtDLtC3WnKq5ckHBAnmP1a54lNQbJxqUwxAWXro8ELy2c_E2rFR1-az1Kmwcgl0d9VbayvLNkJV7rySzNKuwTvwndOhfU4zeBSFIw45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)
و سپس سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» آنها رسیدند.
او نه تنها با آنها خوب بود، بلکه عالی بود، واقعاً به طرف آنها رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت جدید و بسیار قدرتمند برای زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد.
هر بانکی در واشنگتن دی‌سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شد و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور آمریکایی ضعیف و احمق. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
به مدت ۴۷ سال ایرانی‌ها ما را «گول زده‌اند»، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8290" target="_blank">📅 21:51 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8289">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✈️
جدیدترین آپدیتِ تلگرام
🌐
[ ورژن : 12.7.2 ]
- لینکِ دانلودِ داخلی ( بدونِ فیلتر ) :
✉️
Telegram ( Direct ) [ v 12.7.0 ] :
https://uploadgirl.ir/d/c99c188e-57fe-469c-91ce-843a37e803f3
📌
خیلی مهم : فایلِ آپدیتِ نسخه ی Direct هست و در صورتی که نسخه ی Direct رو نصب دارید دانلود و نصب کنید ،
+ فایلِ نصبی داخلِ یه فایلِ Zip هست که باید استخراج کنید و سپس نصب کنید .
+ اعتبارِ لینکِ دانلود : 3 روز [ لینک آپدیت می‌شود . ]
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/IranProxyV2/8289" target="_blank">📅 20:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8288">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت…</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8288" target="_blank">📅 20:02 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8287">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_ypqdplDcZ_gKbl4D2zsavo6jRIFAPfOnKLgMS1gwBynfyX4NFUiQ70mqIo0MTNPkfqtN4FZuO2UBR4qG89SxSLomhKTf2RNgUPKEz2aOlIRv3c4WbK-40QLzUr-kc7oOw8ijIgbfarH6wYqBr4Kqo2RRwiabHJl6eAEEinFnk7a9RA7lMHq8ghZaGORiwaMXKpWBYf8RaUfsFL9r_K0UnAXaiSaB6ooHuacYeU8oz5r8od6-cTrZp566yy6y1-7L7N5JYuOW9DlptZf5Gq7OPJfpDQEOJ2ea6zHFst1-YYXY34UCUl8dwd2XII9lsrsu9iodQBLQeMUHVsL4AihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت مناسب قابل سفارش هست، برای استفاده در تمامی اپلیکیشن ها و سایت ها
📹
✉️
📷
🐣
🔻
@RUSSIAPROXYY_Bot
⚠️
پشتیبانی از فردا ظهر ساعت ۱۸ تا ۲ شب پاسخگویی سئوالات و مشکلات شما میباشد
❕
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/IranProxyV2/8287" target="_blank">📅 19:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8285">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5pZZxIFi9jFkpH04b-bHVJHF9BWTxfhaj20bQ2htaKsKccTs1Bt4wyACWqn9Csbk4yuW7tlTTuoDePha_5QvLDOcHOZNGu_KT38mmk6hkcUDtYhSnvHUZ-Tilp4B22GYVo7fCCJhDEMbuPK8-OJbnKawDqiLm4fyBTn0JdJ2N2cYUCTX1wDCILNr0lBCKK_Vv3J7VJvgI5Ss_Z-TYH2SqSG_RZtZZ95vG5kMeYQC0ueWpjInez92v5YM7olKMz60qY_XzfphzpdI9oBMJjhSn9Q_Uvz6QlwIaD2PEPF_VqgvAwnIK8lwY8CqtruI3wdd4tbqTCJTuQJgme3Qq--HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رییس کمیسیون انرژی اتاق بازرگانی:
سال گذشته هر هفته ۳ تا ۴ روز خاموشی ۲ ساعته داشتیم ولی امسال تمامی روزهای هفته ۲ ساعت قطعی برق خانگی، تجاری و اداری داریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8285" target="_blank">📅 13:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8284">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید
@RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/IranProxyV2/8284" target="_blank">📅 12:32 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8283">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کامنت هارو باز میکنم پست بعد حرف نزنید فقط نتیجه رو بنویسد به نفع کیه
از اونجایی که خودم بارساییم 3.1 به نفع بارسا میشه</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/8283" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8282">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یه چالش میزاریم هر کس اولین نفر نتیجه امروز الکلاسیکو رو درست بگه بعد بازی جایزه میدیم</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8282" target="_blank">📅 12:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8280">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">‎⁨الکلاسیکوو🔥⁩.npvt</div>
  <div class="tg-doc-extra">2.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8280" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8280" target="_blank">📅 12:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8279">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پزشکیان جوری اومدی ریدی تو نتا جلیلی تو خوابشم نمیتونست همچین چیزی ببینه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8279" target="_blank">📅 10:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8278">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118c9f04cc.mp4?token=az6u1Vt-s3TKHaw1txp_bBsIBTaha9Ejaxk-Y38_GNCHEl5rblbfV72oR-SVFVWimzrwXY1Y5I0y-vaNRKitQ57E0d5R6JnvIkVzK1oqeFPsA59_Hd4deTmFON-ixDhHj6hDpJ0hQLb2ehYjY5h5YAASA2uPb-7RsORqgy2HGzKLC2GHql0Fbgs_izzxdILhlHVBdA_B0Vqs4nTcY4WEE4uUKuJ1-WiVD8y9nAvvXwOqcuBsJ-yE9yWZPu6gA824GiFJ4wL3ZrLw7j43orZb2f6-ZTXEmASzgeWroE5RNSY6Irm7kpyxybURY3pPRACoyN6FL3O1zA50IRyoN7_uRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118c9f04cc.mp4?token=az6u1Vt-s3TKHaw1txp_bBsIBTaha9Ejaxk-Y38_GNCHEl5rblbfV72oR-SVFVWimzrwXY1Y5I0y-vaNRKitQ57E0d5R6JnvIkVzK1oqeFPsA59_Hd4deTmFON-ixDhHj6hDpJ0hQLb2ehYjY5h5YAASA2uPb-7RsORqgy2HGzKLC2GHql0Fbgs_izzxdILhlHVBdA_B0Vqs4nTcY4WEE4uUKuJ1-WiVD8y9nAvvXwOqcuBsJ-yE9yWZPu6gA824GiFJ4wL3ZrLw7j43orZb2f6-ZTXEmASzgeWroE5RNSY6Irm7kpyxybURY3pPRACoyN6FL3O1zA50IRyoN7_uRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری علی صبوری که میگه به مرز فروپاشی رسیدم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8278" target="_blank">📅 09:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8277">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqNsbUb8W77jpAHldHVX_Y3emrU5zGJxFv419imyl6wBm5KaONYq3L4uz3zv0Tc665j7y-cvKSRghe0cmD8hMee61ER-Yl7lRXrGXkI1v4NOqgbAeWy1Kw3S4LzZ_0itIcyIR3lOqjXr-Lz5cpMOTk3Po2INSLgXB3CMTrKdNZ9dudJOPHNdgHjVLf51FKwRlbbcR4LpRQKD-gLXuyaWVclk0OBfSC9wKwFsLszzWokZdssq-E44-ktqj2J87foDXM94fj-7KSZlvROi4GoLOpOkrMHs7dFt93hK5-qC0j4F3wxKRR9kLEts_zXiVODGalhaMOhrxSodqGkUrBX_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی صبوری بعد این که ویدیویی داد و فحش خار مادر به نظامو طرفداراش کشید
الان این استوری رو گذاشته و گفته بیاید منو بگیرید ببرید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8277" target="_blank">📅 09:52 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
