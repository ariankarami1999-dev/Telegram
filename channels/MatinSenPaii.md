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
<img src="https://cdn1.telesco.pe/file/bFAY_kp8dqGUputKJ9y6sBAK-D93MXqt5reeLeGXXrKQii0k5vhQ2GaHWXA7XFXJFBF5uLCn20R53qDMbrWQXZXxz4ML8FmbhaILgrn_VFTv8Yb4Rer0MLeTvp5WfDYuahdhAxSrZ1q1B4WDVqZJMc_wLMx7-21u8bVdbVIVRDy7s8N0LvZEPMgkvROV6amx0W6bwzinZSGEYA8cuHWHu5Yk8OUCl9yUHOBpLtxRwYUyubRbAxbToIuZtqAZT_MG9en_l9yzQ2SgF9l7psVSEL7uC44RqQzQuxpKOwt2yux0iojicGqUhQFN91UlEYgGRHLfTinF6we8Z0MYmulQ-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J9-bNHHlfk_pF34iIV1bt2iLgJGLC8K3ke1KoikUewDq1gJLxXZsKQV0AP1DahwgWFy1dfOKmqO5vi-g86lVv4EWWOqk-qTRMrHffE0Tok9SfzhgkMffEWvNQojpRgND8SUKpujkuBrShfFPEhOmuxL3XiVaMAsICVPvIIJcdv_urUwAR-bMPtHQmwCJaoVumS-3LW9cI3mmQ4t3sZreDnYPnkjWND0jK7RZyroo9lzmyRqYMHzJEXQiqpxSrrP72uph4EpYhcNUg4ebetL7ZD-CJeWFaqyIXwmctmDcrxMIx7Fct42zCzJ9gdYZZCBxzl7cpzqIVhO3fT367EKUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-poll">
<h4>📊 کدوم ایده رو با هم بسازیم؟</h4>
<ul>
<li>✓ تمرین انگلیسی با Shadowing</li>
<li>✓ زمین بازی سیستم‌دیزاین</li>
<li>✓ تبدیل کانال تلگرام به وب‌سایت</li>
<li>✓ ایده‌ی خودت رو بگو💡</li>
</ul>
</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hGB2PMNSIdxe1zJBZ6X9UBBEsnm9eDqlGY17Kj83A0h_Y2CXCIRFAVn6wiB3pObfQ10z9JJdJ--tUynNvtpxhVYM7VMFf1ig7qgBSC0j6lEsIVjegGKIexOjPP3ySPHOowAm0ykOCiJxberDUSmg3YrKblEF0nwEYbvgaxTktTvjjTg4XDHpdHHd3hoLN3K_iU9tG8N-CwoslgkZxSUK0MBKZWYXugvPwmyGKSy-d16cTMxNjRIkMqtmbLqMKUc_k3aeu1tQbpBv9gR45EabwsjrSj6O7P6yt_whJitMk3IKrjbrsmrUWSs10ra0qs0lmIhVvKZQr_t7IyQOHtMing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kgWfmQGC021aueyBcB2hmVOvp4PTMVp-OEDbUWpumQxxjfe-g-MyUfbKzFc6_UP6Cr1CTTvQ0jn8WHobbb5mjWRhHi2OzhV_fOpHIYHFKUE3CHdAMHdRuaAvlX1cz6p4-I6Jj-QroxCtLznpI5Yz-tl6CJJxYfVzP5j_DX4D_gLBcfGQP5eXbO5rQlVGWBMs_NomcFEi-LPgQmD9VSI8gvhQvCwXg3zxU_HfmTLz1gl9GYUDFfZWwl9UoLTdj3Bae1i0c-lqoRQzmwP8MhIJ6pDDuuGRhCHRtIIRomWIbtvdcdGnTD678g_yYdAF-1wZFUIQlJ6NJKJc30AGJW5J9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HavspNSVUJwmDdQe2YiIoBiLsNwastHFquzjwNa_VkR-pV3lqYGvTqyvElfjS-u4LsCPX3gZVeYqpsyYsuYXtxpTkfZ6usw4f73odSRsdBoCtTEXmf5XsC5WqJsF7P6CSeAX4sDEKhUMze2bRn8ge345z9JPgBSm3NaBv2St4qRpaeB3cXeTgZA6UwNo0oo2eSFDwnohkGfxm2Umrm3Ix9XkflzIDkdkqiVFZoXbEL836sYvnxCZls9LkvSPL8C_eaudfrM_ZN_GYMh1UW6USmfrH5ag0gH0lzkQA3R68OySNwPk6AflFETWVWb5zcYtQTJelINcAAxZurafKyVChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HqEv2MnqEWfVF7XXfZh3i9jC2SvTOkhQf_YuWC5p0HasNlrFDSVL8gX-Oz2BhBSwdqoiwL-gdBko4UbM8kkuUNGTojrqd0SCX2I8b3W2PS2oBSIytb4zodFnvIfJNajHoh17fR_qIrZJLyGm5SHmzePM4PzYu7dUWXK6rgPGl2j1rqX7SQkorK1LjgKYsvUJMjlopWuVQ3kwxdjUiO2x3qEK5LjWHi82FSdkEz9UXoEi0-KMjfr30urZR81mk2jv6OXVgTAPuu7vp50K0bMfah9T1xiJnkkx2UybPCvjewwp1GTll_TpTMSJTcBK_2BmPGq-5TBlM3dZZoQLw6u9gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=uuxuuqy877Un0PVkbcSc956oMKyLcZijhTIMIunLf0tm8qEJp1GtmYaB6Z3xMHuiOxhvwSPRLF19KKqgYMGsxTrUFmM4GlAZ6EwQNto-3uzvZU-oqmzq_cCP3w6AoEsvgwYCkFycLLVzEL6r91KaY8_bo3N-ZZJmZML6xwssWfDQ0DpGXSzsF__4Nzsbbzx_RMTNqHtBzz3OCTFmiY7fdomJwUBkWWteXe2uiMOVoeG2txd_GhXlFz2M1ZMRFeCvfd0AqjqronZjQfXKiigBw99_9R7wRI-ufSTsYJHe85sL191bupcBHiHczpe8RQLXGCEd75PJjXbLTa64OLx7Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=uuxuuqy877Un0PVkbcSc956oMKyLcZijhTIMIunLf0tm8qEJp1GtmYaB6Z3xMHuiOxhvwSPRLF19KKqgYMGsxTrUFmM4GlAZ6EwQNto-3uzvZU-oqmzq_cCP3w6AoEsvgwYCkFycLLVzEL6r91KaY8_bo3N-ZZJmZML6xwssWfDQ0DpGXSzsF__4Nzsbbzx_RMTNqHtBzz3OCTFmiY7fdomJwUBkWWteXe2uiMOVoeG2txd_GhXlFz2M1ZMRFeCvfd0AqjqronZjQfXKiigBw99_9R7wRI-ufSTsYJHe85sL191bupcBHiHczpe8RQLXGCEd75PJjXbLTa64OLx7Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h944mrpZEbpdZJqUX4QSHwYDAD7LRNW9udTQ_QoZDHa3OSfqd_mMLAzuefiPspEJGe5smPiVbqxxVUn6bknYz7P5YThBvtPMuPIOoPxhV1WdMfthXbfhP6W_C5t7wAw5_7-f3afouWIOC7X5c_PiUfQSYAEycLN1nUiPRi-kk_VesxAhqZ-TByR9cMMq58KFeEXBuzMlZbHZkTBNPbZDKQuPTv7iFzp6QKm9457PlTf5Gu0ZDJCozCJPqQv9Kdieggss7c0-6ySEvFGvpTGD0QFGaMA9ZPzj7npZsVVI2Ljlrij-3oDgSKonf9Q7QHBJZHJGFqV5XMIMZeYUB2xjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ubkc2tL822Bo6IZgRHDAEL6PppbhwTmB3wrIgggtRCSTLTE6veDuoA1iGDG73t4WH2g96AFHSzIh9b-TER46lWxtPXUyTWEIksSJxKvhbhG6NuzF7JU8lrnAsGgHFd3kiHNM1R-s0j4lVlaSDiQTyhJWdJWFiLhUYHbION4iSwpgjVnv4dYxVzIT2xVZYbCVt6FZ6DK5RVFMBe7YdfHCLw-njqBpMN5bUCFpMAlj_g8VRNZrVGvl99lKcL8EEZqM72l-fhsoDzI-DIOGIf3xPVy_s7EEGSETxDbNkVDEajBkDoW5EEBBHlz4PT-pVTQd6Wt2i69yWXJElWYgxobD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oWDMTXCdaPwqYW2AjDnsZ0APT92GUaaNnlyUjN7qkNLzo36YiLpCJaEb5A8WrCrQ9rCXZ88Qc90Bn_Daj6n-RPZmTPGqEMNDoku5NrluA3NNJ9xgRN3i85jVQOLtFq795JCNDSv2HE-Dx7cBvIAbrjGMWWP1idtzhEFdiMDmnEKszwIJpLPd54AufI9Kk7FKvg3gCZeheD0AKTla8V64GAv1kBKEUWjquTBOuMKjAZP0gDznmrzwDoF6G46nsQ_2dB77y2BBOMsHYTVKkspkma9KYz5Cpgo3pfgCx5eGsJHi2mxRHLki3SR6ZDReM7OLTe4dnUaUm7ySaBD-tlP0Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZdBhicqChYmo6nDRmpJYFbPyNqa4fwaZR5KXKPBk4cvf-8idsO2hZT7do8phnKCUc0pssUiJ5fNsK0MIs8Px9PWs50Up30g5uNf2NHngV5C_Md4D3DI2SDWSuIoNlIDQstiMRLU1Mrk32qHKT5nt7mbArBUQYDdrx8O14Aagq-ac6fI0wUybyWgNAtIrxvHXYrafw_wlRv1H2dAtzLmfl12qeFSq4B3IskKXHyDew9Eea3IrMB2PKva5DtLlB4TrhGefD7hTiVRm9Spb9DXTvgYwmKwxVrdIxgayAO1kLb9M5x7k1iHhB8ANMjBdLYGqeH4tuzTkFgIxNLapEPvbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار جدید ماریسا مایر فقط از روی عکس‌های گوشیت می‌فهمه کی هستی
ماریسا مایر، مدیرعامل سابق یاهو، بعد از راند ۸ میلیون دلاریِ seed بالاخره Dazzle رو معرفی کرد:
یه دستیار AI که برخلاف Muse و Instinct، نه خبرنامه‌ات رو می‌خونه نه تقویمت رو؛ کل context از Camera Roll می‌آد. از روی عکس‌ها می‌فهمه چی دوست داری، آخرین سفرت کجا بوده و بچه‌هات به چی علاقه‌مندن.
مثلاً از عکس‌های خود مایر فهمیده خانواده‌اش escape room دوست دارن و چند جایی که نمی‌شناخته پیشنهاد داده
😂
😂
کمی ترسناکه حقیقتا
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=oG627_BDzmYHlE3PFpajYxSj3OVB7wIi2j4ErgABPbTLD0K2hnfVupI-WYSQuTYECrz99fxfW5kA6Za3jve0ySbBAlGJXOQ69fxgtWDWkfL8ll9nv-Ppz0RMKrfpPcUqMNLFpIAOVayO_wb6QzJqV6TUoR4-_iOy2T6mzN0XM5O5XxWBfpPnObPIvGLqtAeC6zbUi1Yurg2gm_SPUNa7Kwy58z4q4lybjWyIQXekdoFijKV763Kbg3Szh56HLSlmrlLvjOQHn6QQddefW9JML7MLTPMVvFy7avclwFUWcYG_Yo-_cDUJDNG0oAFfCOtI5thhBF-9Md97rV9IJYllDw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=oG627_BDzmYHlE3PFpajYxSj3OVB7wIi2j4ErgABPbTLD0K2hnfVupI-WYSQuTYECrz99fxfW5kA6Za3jve0ySbBAlGJXOQ69fxgtWDWkfL8ll9nv-Ppz0RMKrfpPcUqMNLFpIAOVayO_wb6QzJqV6TUoR4-_iOy2T6mzN0XM5O5XxWBfpPnObPIvGLqtAeC6zbUi1Yurg2gm_SPUNa7Kwy58z4q4lybjWyIQXekdoFijKV763Kbg3Szh56HLSlmrlLvjOQHn6QQddefW9JML7MLTPMVvFy7avclwFUWcYG_Yo-_cDUJDNG0oAFfCOtI5thhBF-9Md97rV9IJYllDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=Lq6LYCHPz8S8Kc4F9BfR13dtkrmCfickLL0r2vZTdPBhll-OIzQOzme_uWYkEm4g2YbTDk-nmcwOVtb1TzsxZy-QewdDZPQfO0meMFwDr2NV9doGykbAG8zCGVD9FtRBd8fTZ2x2Chsltz0ELNZvYcZuZ5OEjIlV1Ogw4HObB91h-gnoWHr8elU-XzEFZe-8_NgjTTdnNHBu3zGxv61LEYLDT-X_GyJlKGqo3Nu4UQE8h0l9MBw4srXJ2O2ed6yW1rxCVO6kqg8gQoeT9Llsmle561oDM3-0iIUZWrSvQpbphnmHZri0Ns8l9m8qZNv0nsn3K8s0j3HfwnT_pcc47w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=Lq6LYCHPz8S8Kc4F9BfR13dtkrmCfickLL0r2vZTdPBhll-OIzQOzme_uWYkEm4g2YbTDk-nmcwOVtb1TzsxZy-QewdDZPQfO0meMFwDr2NV9doGykbAG8zCGVD9FtRBd8fTZ2x2Chsltz0ELNZvYcZuZ5OEjIlV1Ogw4HObB91h-gnoWHr8elU-XzEFZe-8_NgjTTdnNHBu3zGxv61LEYLDT-X_GyJlKGqo3Nu4UQE8h0l9MBw4srXJ2O2ed6yW1rxCVO6kqg8gQoeT9Llsmle561oDM3-0iIUZWrSvQpbphnmHZri0Ns8l9m8qZNv0nsn3K8s0j3HfwnT_pcc47w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Claude sonnet ۵.۵ توی بنچمارک Terminal-Bench 4.0 نمره‌ی ۷۰.۶٪ گرفت.
بعد این پرامپت معروف بهش داده شد:
«یه کد به HTML بنویس که یه انیمیشن دوبعدی از یه پلیکان سوار دوچرخه رو با گرافیک SVG نمایش بده. نیازی به تست اضافی نیست.»
توی حالت xhigh: یه SVG سالم توی ۴۱ ثانیه، به قیمت ۰.۰۵۷ دلار.
اما توی حالت max: تمام ۱۲۸ هزار توکن خروجی کاملا خرجِ فکر کردن شد، ۱.۲۸ دلار سوخت، و SVG‌ای هم در نیومد.
گاهی سطح Effort/Reasoning بیشتر، فقط یعنی «شکست» با هزینه‌ی بیشتر.
پس الکی درجه‌ی Effort رو بالا نذارید. برای مدلهایی مثل sonnet، همون High-medium کافیه واقعا
🔗
‌
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MfI2OesaThKs1_XgmebnxeMrLZnwlImwsh-VaC69AGZdZqSFqF_RYSxlW0kOmMn6VeH7znAAbkdd048WsDJwGh3kZMApLwqcqYD9nzcTcCY9jhgIJDKmHOMBoG22lZ_RDKDeSQfzK0lfcKbHqay0NF9hGU6S1Fe-W5EQbGQTdsCLL9HbHuajUUBq7lHJG1BdskstqjrSkGrzVmQb0egKFiHTTOpzuD5ILZH16vmtQ-W8QaAbWQM3JSVE_ilkOucf0cN-OKy_6jABOgxSS9p9v7a0kkmHKoXUbAMFRLa0HX_2ooRBa926fS9uMlPyAJdp4hCdz6JMSplziYNw-Bw9qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hFZUXk11NeuFJ-qTcpfYbBdsAMv1nRVl5MWJW5MEjXgS80G4-BGGh1p0T7O6kZgLePREoRM6Fca8J0Xg0Sp1ty0hqvEk69oZVH_hugA7ZoYwwebIatiD3IY1Pl7N7FpiZnk8cnCntiA2q14H6CMqXTX6cxeoPSh3IpSkym6OJhfUD1_lrVNpEUGBJMVDzuxT8tI-DF7p-Jp1mK9-5IZFJouKlZhlYetUcBHF9cCahxod8aWrKspShRfhZ9sH2E-GhAl8gx9kH5DA35MzH5yXeXztypD4rnT7EX-4_JQq_UkIJie2JAqsX9s-4GF6rbtG1VViQ_LaWJ-i-dqHycU8Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/o5TIPP6LArpD8sUlSjtGupujI2sPTH6G72pplzxWYknMK0L5Sjd0kcxa8GtYHuF6bbRqwLMuEw02Y9eOJgqz6LqBQUztEGJQWZtgZnvZg0iRspXM5FibK4-t0_EtGmrUy49vcUhL-fAWFyzxjNIdN2UvN3McBSppN4FI7nrRF_zKfzVcAqnZCvtjjspSAXW4iVhnI3GD3VKMxMS4FlqBA6wT0G6hdGilUsmEB9XQrmUbstIqT6lgl-wBruNsxdmHJiQ68QzpHdy6ZIezyKybTIPS_qUvyDZ9mVvCJIpnN0G_gR23NfL0dntj_dy_yR3J449mJkj9hdKAN7GdhJ1RCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a4ZGj1OD3XlQRQ5A3id02ajC9kDqY_XE7ATCPm0niRg7JN17__hrVEWs96MEDyFddu6uhn9D-_gi2ljafsyMF8U4DpmFEwGFMXSYb5oofrcez_vOt2cuNd8MNikd3hrOtEXumTA0sGYCGn-NoyBSHC_YwnqaDGo_6YnwEip_0pK5v7gZ4dZ3RTSvZKBi96ZfNU-9t2sH_Cbptqcer0zPvNjhUwXNlquFO1n7V0XahUWQIy9fCN94-lT-hQlWKbcweo-kTH3yDdVVvrfMsZdQUh6duPnnMpv8Sa25mQjoUxwQmoKf6m24kmR5CtBUy5NgHt1apDRqbanJleljnIoIcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T7sm2fyw2L6hCgc5IHPv1JwY5LfJYZ9wwUZHzHN2YWwWYAqxgA7NJYSFhDeJs_TsfHvJZWR99ymrnJnCMfMeAjbsh7dQ3yMa9rT1MZ0wXg3DB2s2J-_U83D336e7kd8sAoHhSr8zTDSaXzQXvPu_VQJuXVsMkzDHbG1gq8v0nQLbpdUnA2wPXtYDkx7Dx6qLrO76lonkZGcV6Ji0-oUSjQoJhj5d0lXjtrrhsnoLyHbawI4a7IZ8wVi6tLsLX80QfPZhl2es5e6vwbZH9MKedsRtVri2eaaNgSUz6f2jKGY1nlFZLAeQS8FPNhPO3Ydeeim-ohbfTkgauiMYuPd_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k6p56_3c6wL1DD-WosAh9X6EItUbb6zcXFzf_3hUmQx6T4YfIlTJOYdKLt-jCeWW36AZjsbRBzRtPh0SeSm9P_I_vvMKERkra9eNvR_VfQ3ZiUAXLHDVrCaCr0ruD6s6ro7T7uOAXJI3Z9dG6FzNKkVhOqqIdpD18THxn2_BwXeiWGEa1E-nu4rwtBGlUz7Hdp_WIAhwZnUszQ5QhIhN3uKYy9iYEl5PfOGEur5-Rv1qp4J0Erdv3QRS-TLeHgDOTc1rUpsa2nz-x_GEPeMr2PGiQtfKL5yWKKtwWxl3Z858HKmcm4FFbsFBa02W4hYNPf98TG79PT-l3C1-P_5kew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qK6DuLFnXZ4w2rERZzb5LVssbVBbqWlmzZLNVGKo4SJOSf2hNpav4cVxT1dINX3NlECVevTcRRvcL5eQRHtREolCFfJjKFUGMT3on6gT23N93kUov0wpAFBmVohktM4z2MY18Vq44pVllWbgN_e_Xdsj-Sn-CxCe1HDYzhW0UMYgRcvR_-87qlNLv85j858nu0QoCCqHNc3Y_V5La6DjodFI_ZNfBUTTSIjuykKFGDraU6bMQ-YCTNBLZUOArxQXRJxjm15xmX-PAU-H-U7gXxFHZBLXomzThIc3rdboPOhd9D5S2V44DLHje6SCdyBDchhQHjjk35MLaFIHXsE0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DD99T2iygEQ3ZA3vypiOlsKu4mp3WRAzToAgKtHgBStFf0PxhtpRZ4N6hGDOFT5-QV4D3TdPObAXR5hk3rI2FelylsaL6sQX_aDzhPEbp7Xr9-W64bqrTYj8XXthJicfqgzmFukY7iEJp7hUrvpPHQTgxi9-3PSynhIE-xM6qkONyy7gbRIMEey2dF7i3Y0881ZoFJTjU8dV1TXiXQ_67QC7WbRZu2aSuom9krrIuapFLBAifpLDBW_L2DUWi6WdHRoroBmb3lgRKt8gmm6QWdd3fV79Vw5t0XGOk6A5mppxJv4TW0ZupIoo0vvylqSUGpr0s3dAR9DHaEX5Wf5-vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=HdvnuoweLI50do4wqSDjsU8WHTB2EvD8b93eR3WzmWP00QZwo9mxbX6wy15lLxIxUe3NfMKO_PqmAppK9B66CZFWAePfVQUehrrgHUzmG5L2gEXWmyPRzpYpI0kXavP0XtpjED14LyfYUnMjTAz8j0vc5a2NbsbUbQJT3xl6gny62LsS18JQdo4QNNQGhOyhVTMPwqI5eshcXlXwD_Q1kkgjRafyYl84BxWhRqNQwMSk0GOHlO8e5X9Q7UDMODq8SUUJowytU-o_qbm4sYZX4h3_X_BXR8axHdU-o9wYiKJDwjivmf1MWIWOx7B35Tza-Z_0gkJxRFxRh-IE51QQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=HdvnuoweLI50do4wqSDjsU8WHTB2EvD8b93eR3WzmWP00QZwo9mxbX6wy15lLxIxUe3NfMKO_PqmAppK9B66CZFWAePfVQUehrrgHUzmG5L2gEXWmyPRzpYpI0kXavP0XtpjED14LyfYUnMjTAz8j0vc5a2NbsbUbQJT3xl6gny62LsS18JQdo4QNNQGhOyhVTMPwqI5eshcXlXwD_Q1kkgjRafyYl84BxWhRqNQwMSk0GOHlO8e5X9Q7UDMODq8SUUJowytU-o_qbm4sYZX4h3_X_BXR8axHdU-o9wYiKJDwjivmf1MWIWOx7B35Tza-Z_0gkJxRFxRh-IE51QQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dNhaKGaCWo8evbW63aAzJpkLfEF0408F3Ef5i921mv7OkRJ0P8gsTn37sJGbKG6XjhnSg1ukHKNE5k4euBHz480l5W0w9zMn3zx85QRhfKs4rOYKvUrgNSJDfPSc_Vfvc9rYXuWSukm-moA40kuoVislBvBYnpE0WZfAH6GMtM_82zP0boLS1b1MMgqA0BMih6vlvX2IDltJsLinf0mhfMmPIkOaFSdt_4p4blzLvwrkjOZX9u5KNv65h9N9EG3M-yQv3WWVJznPNG-NO2jtrYJBfbIoNFPzQ4rrrWPSr42fV6eAvA2NKJMiOXl8NgwT8N8iehZxkN-d3yGsCjo8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه‌ی Hermes: از
MEMORY.md
متنی تا گراف دانش
نویسنده این پست ردیت گفته بودش که مثل خیلی‌ها به دیوار
MEMORY.md
دو هزار و دویست کاراکتری خورده بود (۹۹٪ پر و مدام درگیر نوشته‌های کهنه‌ی توی کانتکست). پس برای همین تصمیم گرفت plugin مربوط به ارائه‌دهنده‌ی حافظه‌ی Hindsight رو توی یه کانتینر Docker جدا راه بندازه؛ بعد از کلی تنظیمات مختلف، اولین اجرا و تجمیع گراف تموم شد.
که این باعث میشه:
1- دیگه محدودیت
Memory.md
رو نداشته باشیم
2- سرعت خوندن از حافظه وحشتناک بالا بره
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OBnbRifHr08eE6JmP5P-wgwp5AeoHAcCToYTAnRCGICiz92fRm-yeNoxcltKBBzQ8heIqtOqkjiaUvUyz-A_q2eHLgjvop9cq_wAd7aH-1qL47B_lzRtOGkb0EPzUg8YGn5vhPnupmhLGetL3RcX9Agr5uC_lw7gco2Ts7kzFx5vQVOBEW7VGLRaWh02q7P--DdLCI3_r7GmPJjuhWGhphkCyuUiTiQnKTOq3r7VlyEsldADtgUiCcYWstqnmFbWxB36c6JvHseU-zChaJOkhD8R473bUcWDWY9iVhWk6ECl87VJskhWS4GulkaZp7aCWFy5L8c7SQRcb06bgxyKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YC1mO4YSU9V39Hxfod4z9r3VdiJ0IMSe54uu8gksBh3VWVOdkQCN_uCCHih5qv-6ERuKswORXbzlX8iEf4DorTx1F1g-cuFsUv66WRvJCxoGkgABJfjhU_rIqbxMC7S4ELBRFOQHopEe8-STFAuwtqvk8AdqYFUvHO9UgmCJ3NQomhfi8RgEZTaHqBU1i1qMxHgeQwgGjb6pgaL8zttokx7PTlsYyB-FSJoDFrHvRmeD1aEscavIc5UY9ITQicFT-N9sMDcEzL_f5LXluJhed6-1qxFvNOvfTh0AGVk8_e64yoUxTWJa9YxQvyIBj3N08FeGZkKlQFI7D8uiEymWWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sYhMEeLBXF6aMUMI6JMFIboSCS0L0pA3FeEmJXa54KLKCl2hzQppicxzi7Qzhj2vqJHNZhD_EGj0oFVnknr4p5oi7LRl1rKkIQ2RLtZ1DQ6pZZUvokQwTjYe0o6CFRe8jDQi3g3uydPQ27_63TQYx4q7eYumCZQh53Q3m7LeAyDj4rjgs5tRP_vtwvBTBvTUZns-z_vsmU1u-X__FBjWLzYC52w6ylHnzGqdSoJDNX9zUYXkDl2LcOGrsozxLhXCY68-qpsg4uJy0eZoP-7h3o8dQjg2ZH0-zbZ-d4kqqOarBGf7l6uzrC1kkK9j4LnJMXdGyds6ql0uWrLNcboGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JsIUUYIs1oLW1svZv_XOMnR_y9dsBiBMVHLylo655OeQQV_YnqAT1j9fWbci7jHCGsG6uVTZteWfABzMDCiFmkr84yNnKTqazypliZdqBh8eHrut5Zr9tuNWRVe7kRaxNxfP0SHJu7BRiEMwaCUAj6J0b45wSDpPFnedjfpKXg3kS4sGS-a_YDWfYueEk9_DxBaugKmPBVFH6pvYwFXK9qmFql_b5osQ9ckKyNqiEnTQIa6eteGd1W5VS4PTdRTE8iba69mNTZUYlg3GJnnGHgw_tlDYP1TUZy9YLMXGS-0S7VHe4JoE6QhTAhMIuObhZGuoI2uvDjzxrWwdPytzWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHXBKWP4z3VsI-Vd0tDR4p6ojA6Ms7fRGfcwe9YVHUpTodoTwxJ2vjegiSu8QVm6X2jJ_ybGCwEisuxnBlW4O68lpfcIALpyNbbteVFK2OrRX9Akuza1ss87QACbPYYZnpOQLjqLB_O4CqwUUmQ8GidV3g7bSFG2fq7BvYGMvIMv357SImQULAbNfFZQwDcKf0V6v2S-qmMeIDl3z4QS2wLF705DO6mipelMnPEiTCUUgmWEeeC-R-UtAvr0MCufBYcZFO85X1So9UwZWNQmnVWaYwMWXbYnCTt9RnszvYXTUdGF-W5PtEcS8GhjPuyDSFpCHnesTSw0MRRTN6GVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IW4N5X5XwBqSKAma9X0MAxhc4uVmgUJs9EzP_ScIO-wncuT9ddYuBbSuAdJHL6-1TL9ZW_wX27bH7Mtw_hnmVq6OZiD39Epwb1oDQ1SywEIiqqlUI1bA2ZV1Bl9sj09c0HgdeanIIMqbRh1QhjClVyKq7qs8VWoL7y5yqLqUqsoRlZJKpZPruPOgl7S_E4gdugYj1sBuve3atNfmtss0BUG2yblO0zvqFOdHXZhDsOZ6mI8dTNBA_dkprqHiVJfJWkaqXUT_P35vosmxUCUK5aFYwcuy2vdCFVH89h99C2BBNcYKu4dZn1Mj2FXUGXEpHQhzBBqE5Cw96zA-8gncnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwVVti6wqjUNpCNVQ60cPqyZ9BFGWUo4E9J9BZW3m5I64erMPmtA6R7g8xkrmhm3w47Ykv0iKYaBq8uHpAuhvUyAVWui8xuKt57yQFmP0oCohtjdNvs5jGb-CJPnxn9ailAMl204pDP6RoKgKHVH5hC3Oj3CINHinOIwANJ3PVY1t7X5dT1wA1N6UvgWBcwCqHTAJTLeLym1nJV00BgtlWuC9bMQaCUZ2OK5tW9MTI1HdFCymwv_GmCyzKH8bYUvVFYrXnmduIC0L-x5e78LB_f9QVZ6e9cIeEpRaGVIA-x0NY70mJ0RXAbqAHc_37db2AzLuDpiu4IWHgp4KAciXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A3DhvAbD97nx8sWhfgT-wWycCXi7Nv4R2hYO1wAaoDVo0ChmHho2lZMGi9YX0PKnMYYS5_RBuAGhwDX42-40-u9z1MlIMQ8VFlnNk0jOjACaDzk7aApcMtmjxrBad6t66JFh2-DZ5kJEjMyDdgCBX0HtiuXclqeQHurAZSPBO8QCT2SK663XZxL90AqEEUGMpuhBIxqBmIfPeQGC-G0woQf902HmsIAbanlz71xEUEomT81j99A-KbZh5F8stWDBVvODuA0PWCi6aFHROe-Fp7ALJMmLljndTbzBOF64nlrq2eo2oiLYqOpjHZNi40enjXN1OvdPSmWi8wTbPQRFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حس می‌کنیم هر مدل جدیدی که میاد، انقدر از مدل‌های قدیمی قدرتمندتره؟
باید بگم که این بیشتر از منطقی بودن، «کلک» شرکت‌هاست برای مارکتینگ
اگه یادتون باشه، 2 هفته پیش همه‌ی این بنچمارک‌ها(خصوصا سه بعدی) جوری از GPT Astra تعریف می‌کردن و چیزای خفن می‌ساختن که انگار خدای همه‌ی مدل‌هاست.
بعد که Claude Opus 5.5 اومد، خروجی‌هاش رو جوری نشون دادن انگار اون مقابلش پیامبره.
حالا این قضیه برای هر دوی اونا در مورد Gemini 4 Pro داره تکرار می‌شه
به این کار اکانت‌های بنچمارک و Ai Enthusiast ، قضیه‌ی Strawman Fallacy می‌گن. یعنی مغالطه‌ی آدمکِ پوشالی
توی فلسفه، Strawman fallacy یعنی از رقیب قدرتمندت، یه فرض پوشالی بسازی جلوی مخاطب، شکستش بدی، و بعد خودت رو پیروز جلوه بدی
هم خود کمپانی‌ها، هزینه می‌کنن که اکانت‌های توییتری/ردیتی این کار رو انجام بدن؛ هم خود آدما خیلی وقتا این کارو سر هایپ و ... انجام می‌دن.
چه شکلی انجام می‌شه؟
1- مدل رقیب با پرامپت ساده یا بد تست می‌شه، ولی مدل خودشون با پرامپت بهینه‌شده.
2- قابلیت‌های رقیب مثل reasoning، ابزارها یا context بلند خاموش می‌شه.
3- هایپرپارامترهای رقیب به درستی تنظیم نمی‌شه ولی مال خودشون با دقت tune می‌شه.
این شکلیه که می‌گم هیچوقت به بنچمارک‌های این شکلی توییتری، نمی‌شه اعتماد کرد.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTO1IP5dc0wN9YU2yGNGJmNuKiGnNI-9Azx4tFNQ2BjbHlkG-NX-FwYjDI5Cd2rUzP_JLDZk0a60hIF09RIPe04x-ClZIMyMDMzGL3ETBUH7oBWO2foVKTXdSGFMQeC5mApQSHjPpRQzOFj_9hE23dTMPVqdnBeVuCWCPPoXSJd9wksvEF5gk-3FfwD344ARLairX1fx5NaMXAlFOl-i_0W0SjlceKhECkOQGFYuDcKza0LsKyYZlzUu9SRvZxcY4KVarheOHJn-dgJK4AHBt3ljD6uRtVxlBkLoab3MyrJoO3w8M19dQR8aYBmSEug9dgCkxzWj8lzxSlUtt5Qp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=QCqX0VlWwLVPE2Awmx3L-GzFVOUio_6SxsZVqcIWTAl7X6c4EIbFs1oxH0s5UfZd8dt7WPAYZps8vDXykw6ZgxwoDDo3mB4XeEy6D-g9i5bu6hdZtNEqF1tOS34kPqLPixxAsoCPL1ujyaAOeMjTYFWjUFJzsWt7TybX81CWbPGuzKWfeep1jwakIuqolP00amJGRHt3aZDFNYv-J9f0A2_r8DmkEzu7mmKJJFyj3db4aZDNS4Qiop0jZTBw_sVjZsYeEGaW9UBRKbWJJQFWyKt_VodJOWDaA1jHWxTmbizJ7iZhE0e7tVtDdpJJ2a04BRdS-629q56t-9CAy_OZR4-dtL_g1YbFiRcudZj7m7SUCQmggnS7iNpVBIjrRgYzT023pZ8e9KdDfqenWSd_XusV4dFwr_Fy-rz_AuDNbDeg1AvY9wzXjD3ILHNv8OKactE6JdJQlw20-tDgeKXpAeuvgz9_zL1VMoUk7NyqPqCRb-Jcj0FVqxC6JIfNYMSlCaPbqm9KMezSZlkM5SFMMRQeJSUg9kcDithZdJmuMQpQ-b060TzoWKa9UprzNKu-m4ww1LdLCv369u7_BLkv5oRcPd0M5BDaeKYyThdvFuh2oP31LAMoyuJnWUOeA8gGc5b_mq5pddoDm4WwfUd78XIlg1qHF0AvtIQpHx1F7i0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=QCqX0VlWwLVPE2Awmx3L-GzFVOUio_6SxsZVqcIWTAl7X6c4EIbFs1oxH0s5UfZd8dt7WPAYZps8vDXykw6ZgxwoDDo3mB4XeEy6D-g9i5bu6hdZtNEqF1tOS34kPqLPixxAsoCPL1ujyaAOeMjTYFWjUFJzsWt7TybX81CWbPGuzKWfeep1jwakIuqolP00amJGRHt3aZDFNYv-J9f0A2_r8DmkEzu7mmKJJFyj3db4aZDNS4Qiop0jZTBw_sVjZsYeEGaW9UBRKbWJJQFWyKt_VodJOWDaA1jHWxTmbizJ7iZhE0e7tVtDdpJJ2a04BRdS-629q56t-9CAy_OZR4-dtL_g1YbFiRcudZj7m7SUCQmggnS7iNpVBIjrRgYzT023pZ8e9KdDfqenWSd_XusV4dFwr_Fy-rz_AuDNbDeg1AvY9wzXjD3ILHNv8OKactE6JdJQlw20-tDgeKXpAeuvgz9_zL1VMoUk7NyqPqCRb-Jcj0FVqxC6JIfNYMSlCaPbqm9KMezSZlkM5SFMMRQeJSUg9kcDithZdJmuMQpQ-b060TzoWKa9UprzNKu-m4ww1LdLCv369u7_BLkv5oRcPd0M5BDaeKYyThdvFuh2oP31LAMoyuJnWUOeA8gGc5b_mq5pddoDm4WwfUd78XIlg1qHF0AvtIQpHx1F7i0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t9YdJCbqNnLswedUVUKa7ADTrlgR6k93QCVJvLMlgLnESJdwfHlRlfV-mf5m50oO47hS4A0FGi217CzyZspRByNJ9y277HJZTa3ZU0MNdMww8XsbbBFl7XLwp89x0hoV15g9cVIpILoVRB7vxmgNF58DEb61OxT2iOAIw604A_o7W-Bg9yDasDPZyR4cSb7R296Uh47dh5zPJDy-JaoKO77OGJ_5dVJ-jOWfWh_s4Z65D0aq4DU-JcM2RV_bKXUzx6PA_M-Gf3c69LRotYAijs5XOhH1PbtQ1Ml4137hU7KxZH7SlUzBEXs8AFYjlONLwcdasBjQVR5XPUIQfMIIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoPDz2IewRQcGgoTZe4qQKO7oxUb8t-vAtbEftXD-ELHkAfLiFxutxDmCeTN9Rs6hixjaRZreBhqU7-wf54w58_Jk77PnffRLLaGwesPd7yolLIR0ImNVp3q6y8OWWBFMIXIesmOAF4VfITcMpswcgXXlG72Xchykg1ip7MyIHRBFvduAQYE1BEHBcW90ly9cZ3tULSaGkXf2v1td_QLyBstkjQTLagvMjWdqhOPMi9xGzfMCaRlLZvsljQL8AG5fkEoRDEee44GPHBnde0L26hyI5tF1bGZH5SdlDO1wYHjyGZSjK6MW96_9471yrMWJ4bSgViG7hihMjI6IX5nWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bo_YS5SFXo4D--_92T2ac9ZUY0thq5a3y8ElJg_gKXUV_dqP6HX09Zgxfrb5mW1iBfAbeXW2Z65635_45cDthpwhaz_KolcvmIeNrJiSBqb0dTpGXSgv-LHVS7wosyUwR1XyCyPUdWsSWd5RPH2yG7vnNkSsFKmAfv43LwbzHlIXUfpA2ol1D8IA_1LX3RxggDQpQKnAztXq9C0_Bc1u_zINoLW7vsjZwVxk1whmuh6QWfWk0wqy7nzOKyH2hyy8VFcdxZL-4iVm3p-SQnQgSdfzOX99J_KJ5_AZREF8-3JO-oAP4jqTLcT5YBHcbs0iwCk88nM9KhHVsaG4Inj4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFcBiZwhtCx0sPn2rLPNBxR-jRcNuf6kXB_KeNUVLjXiHSOpjk8J97RhRoteba9biCQ28gens6HowsPNnv36kACDU-9cw3ZVwE-S8rBaossxI01bOF0r8XpPMdQII7XX2Gsgzz2qhjhqrbk5WSJ233UuludAWcqxSTZt2-lSchlXo1iJf7WBRN6h4MAAlYqhmmghpSZLlcRKZtBkdl93aeF73VNynZnbobJ8EbGPyZcSAf1URBIXSgqxuFuqTA_5hkCv8j4Mp2jMwQ0X9sXJDZwH9lnJERX_gdFNvMtl7KrdoI76qiNLWbknxI_YKKA2USqIJHn7O9CFiyShk35g5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hF6fOyApzpGBOV1q3VTrwlqB3hxjYEnrceSh5pa-wy38Jbi_TuCKbU9hb2RIaXd5eirL0O3cOob2xDLsERiVq1hVNxFwLWxO5lIUu2aYLxqheFPQSh4jF7q0zVQmQ6jiZR3rbtLLH_xN5cFlDF4Ip4g48s0JS5ZfxJqZtCIH0WP3J-mqxmsGUKkXZrmYZLHoyIvcyLyGFhZBKwqVoTzlOWegl-RfV6yo76Nv74kTS66Cv4Cc_OEJTEGzMuXDeMqo5LgF787TrVTKndZo_-lcmrsWFpBD0r5ZIxUnch-2qubOydUnKSJOaewiIaTfv4nkqWG_C6dMJvcFBm9yDkb-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErUbvYM3cBeWuecxmNvJRHGqn_XgMALuxxmYJplmdntSiMawq-NCBLU-Oe2DNb8YJQQUD-xhca1xglVJFzmKVC4zrLWKvHodOxzsQxwLqSnzwyprOztTCjGdCbYaEDxPdIlo-QgeQa0UmCDvvnQZQmlMTAKVx2ZdUt1YHSzHTjgKv-eI8B2pbrlJ4MN8UqkT6RuX_wxZc7nm1OxvAKXGK_q0xMbTU-hjIFNmVSUQ9LKQA_IwCwVZYT_YkuEWJ_dnLQc8oM3uFe5XPhe9EJPdPCZYn11A1NaSDyPOSs6JvllEe5ctyYnnEH332lcPJDPcoodrNcalzbR6_x9VtN3kwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سایتی رو برای ایجنت‌ها به API تبدیل کن، بدون Browser Automation
💪
یکی از توسعه‌دهنده‌ها توی ساب ردیت هرمس ابزاری به اسم
agent-data.dev
معرفی کرده که ایده‌ی جالبی پشتشه.
حرف اصلیش اینه که برای خیلی از کارهای تکراری وب، مثل چک کردن قیمت پرواز هر روز صبح، دنبال کردن آگهی‌های شغلی جدید یا سرچ توی یوتیوب، browser automation رابط مناسبی نیست. ایجنت باید سایت رو باز کنه، بفهمه چی روی صفحه‌ست، هی کلیک و اسکرول و اسکرین‌شات بگیره، و هر بار که لازم شد کل این چرخه رو از اول تکرار کنه. وقتی کار در اصل «این سایت رو با این پارامترها سرچ کن و نتیجه رو بده» هست، خیلی منطقی‌تره ایجنت یه API call بزنه و JSON ساختاریافته بگیره.
حالا این agent-data چیکار می‌کنه؟
1- یه کاتالوگ از APIهای آماده برای سایت‌هایی مثل X، Reddit، Zillow و کلی سایت دیگه داره
2- اگه API مورد نظرت نبود، URL رو می‌دی و توضیح می‌دی چه دیتا یا عملیاتی می‌خوای؛ خودش API رو می‌سازه و نگهداری می‌کنه
3- از طریق HTTP، MCP یا CLI قابل استفاده‌ست، پس برای ایجنت شبیه یه tool call معمولی می‌شه
نکات فنی:
😟
به‌جای HTML selector، endpointها رو روی همون network requestهایی می‌سازه که خود سایت برای لود دیتا استفاده می‌کنه؛ برای همین با تغییر layout کمتر می‌شکنه
📱
خود APIها مرتب تست می‌شن و خرابی‌ها خودکار شناسایی و برای تعمیر صف می‌شن
💰
زیرساخت proxy و CAPTCHA رو خودش هندل می‌کنه(باید برم ببینم کپچا فارمش چطوری کار میکنه)
سازنده‌ش گفته قراره نشون بده این روش در مقایسه با browser automation چقدر سریع‌تر، قابل‌اعتمادتر و از نظر مصرف توکن بهینه‌تره.
🔗
وبسایتش:
agent-data.dev
📌
ردیت
اصلی پست
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=sFqmdKN9PbH3uNTMG_MzOGfKUY2HFKKUQP2WivA0Cz35nrUQydiOIMFXgrun2emS5Qo4V8fMwOMr8yVO495AxqEcTaXplq4vYWioNrsS3S0Z5YyXPxI-SyLP_xtbt9yDmyh4M8nFRUK9O-Al_odDqwV9_VR_O65AR6xIkoI8w6nrI8wKce-dCSIuXN2-q2L9S8SLVz97ckq-cKeH6rykNsNbISpjvzRqkWyK9s7sC2S6MF7g5eUO2Rl4-u_FRUhz1yfLnm6qLiSiR6uVQp9PgT1k9cSrwwf_RAAtBP_vTKx6AuZcggkEaaJevDthDJRnbsL2I7x8XYzIoL_qT2iN_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=sFqmdKN9PbH3uNTMG_MzOGfKUY2HFKKUQP2WivA0Cz35nrUQydiOIMFXgrun2emS5Qo4V8fMwOMr8yVO495AxqEcTaXplq4vYWioNrsS3S0Z5YyXPxI-SyLP_xtbt9yDmyh4M8nFRUK9O-Al_odDqwV9_VR_O65AR6xIkoI8w6nrI8wKce-dCSIuXN2-q2L9S8SLVz97ckq-cKeH6rykNsNbISpjvzRqkWyK9s7sC2S6MF7g5eUO2Rl4-u_FRUhz1yfLnm6qLiSiR6uVQp9PgT1k9cSrwwf_RAAtBP_vTKx6AuZcggkEaaJevDthDJRnbsL2I7x8XYzIoL_qT2iN_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DQplX8iEXXO4uyq2zvpylVoJJ1j5V4tYyqU6tumSIHeO7PSlDPFZiFFxzyydcfpEC-8u-xmRPz7b-sTA4IRR3k3OX0QoPhFZmetf41p7ooFxJESmCmUqMDdOBIGvNJPMkoVe_N6RkD-z3PN-xofTvuZvlky9E7WvyGyptmKZRmnB2HisQwR-d9pgce0INNDsXwDux92rBxOrDgCDUHN5If8Z99y3QBRcLAn3tKyuVje8EKlsjssAHh177jIDn3ptvOEZn-awz0Pswz2Az6rveavYjVD8ex7dSTYqt5hIH4rlCVBY60GEw0IjeFM6dnJdOZKKE17CQ45xizKmqCWUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sYyZCGsB4gmCx6X3OA8VY_I5GYmjUZ0QlOB7sFd71tmS0_lTqKljpIcbK10AO9Rcl7b3nywfGmOjvtxA6UbVgIUKmdldKjKcLxIY7u7PVa4QWSc1ujT32btAtIKReHWY319LdN-JzxJAhrWW3sMMZWUsSZN9vxrYFoGrE3k8FcE8OISJrXaNTuuxLspmc0jnQs3t9GEm2j9s0IBgOGhfGYFuBHSn-8dpcJ1jpv9G_ZwYWTWFtX2zlBa_MYoo0UvSU6W5KSH_0d-yraw_-pv7Z2KP_V1AgVSg2Q3n_-GozxGsw1qrRQQ3PsEYWg7lFc_zG33mJjpp4qvS-BT1KUwhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W9iWU6AkjaNyWwFKtaBX8UpF5I3LZhFKP9R6FmbV_nKXj2w0gLzVNzSPROoiqzW4frWIM0z31k-Ze_8qDcseDdzPLuqK1yFkYpnvaqMvokKkSlwlsOIPPf_O6uYNCLENzU4rZ4tsbWW3G_8eX0wRtHjDzSzJc38zd2QX3apsUv8BB3mI9vB3vGWsKNkWG5tsdM2-To_nt7MYx2pb9I_XGgQK6eDJJrbkudXl_P_0HRFj175IaZEvVYWY-FZTlAD6akiUwEIpVEoMD9iTpCLp33LkFr1gXoCxcAYY3XIppbyI_YtQ-F89Z-_dqxSrzL5y5TvCcAIvxo1uMjaSvQ8lhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/amgWgzXeNQtfHRCyIbkRFFHboj8fLCWAeXJU3PG-YaFy2oOq4IwxXoaHhF4qafT8aukIQdDy2WjrHq23F6FIgLr10eUEsAATyOGfj81vqnlUeqpf1ASz2SYfjpYsMZfxLXGvqHRpk4IO99phc27m_sPFVZiGy7Fe1nIs3mWialObroJ7Ze-MPF7ARCyCCV_ATPx5SFdhgJVmdsKqc_bI0_JPn7QdX1nirExU6SPWzWluyGFU_AMp03kn81WGidSt0iBIN3utxBTsJlKE3BFU53xDA7L1AS13aC2_l0kRGxXqU9AlKHIrDbV-5ttVfU2qdhctD7ocXkfES7KbTh-nag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اروین از توییتر
یه سایت بهم معرفی کرد شبیه به Mpay، اما بیشتر برای بیزنس‌ها یا کسایی که تراکنش نسبتا بالا دارن؛ با قابلیت برداشت مستقیم از کارت و کارت‌های تبلیغاتی برای کارهای حساس مثل تبلیغات گوگل ادز یا تراکنش‌های سنگین و گرون
از اینجا می‌تونید ثبت نام کنید:
https://finup.io/?code=MATINSENPAI
لینک، رفرال هست. اگر دوست نداشتید میتونید کد آخرش رو پاک کنید. برای شما سود یا ضرری نداره
نقاط قوت:
1- برای ساخت کارت، MasterCard داره به جای Visa(شانس قبول شدن آفرهای رایگان معمولا بیشتره)
2- قابلیت برداشت ازش وجود داره به ولت کریپتو(هنوز تست نکردم که KYC می‌خواد یا نه اما توی مستنداتش چیزی ننوشته بود که احراز می‌خواد یا...)
3- آدرس BIN آمریکا داره
4- از ارزهای مختلف برای واریز پشتیبانی میکنه برخلاف mpay که فقط تتر داشت
5- دو نوع کارت بیزنس و تبلیغاتی(هزینه‌شون یکیه) که کارت Advertising شانس پذیرش بالایی برای کارهایی مثل تبلیغات Adsense گوگل و تیک‌تاک و متا و... داره
6- کارمزد رایگان روی برداشت و تراکنش کارت‌ها
نقاط ضعف:
1- هزینه اولیه ساخت کارت 10 دلار هستش
2- برای KYC شرایط ثابتی نداره اما توی تراست‌پایلت نمره‌ی خوبی داره
3- حداقل هزینه واریز به خود کارت(نه ولت)، 50 دلاره
و اروین گفتش زمان واریز مراقب باشید از صرافی‌هایی که امریکا تحریم کرده نزنید. ترجیحا بریزید توی تراست ولتی، جایی و بعد بزنید به ولت این سایت
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZxwDap6ooCONu4P5pO8NB6vFN0zxL8ywhrqdbCvfzUazQte8QO8U6g2Kt3Ta-2I5aRzDQ5HoLwyshyRM-r1HjZHVXTVxNB6FXDbEIfajfvx4GS7zJUawNzahGREy_NpcoC3B19fPS7B5ANHs-_0CH_fhjcG28t_FXhlpoVB9yA2gZi9bf_xnKlSJla-wTi58k9Inuxo0zOeyEl5l2tTZn8K3c_ihzmlUv9BkKMPlbSMh0yE9N6Djqih0ikqpCRDuhIUZAL6Xpy6DWIGPHrbHBFDq0ir1xWv259x2Au4iUzbnOJJ11RbPANdxoWrLZV7Rq3pN4C3X802Fedg8xYaJWgfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZxwDap6ooCONu4P5pO8NB6vFN0zxL8ywhrqdbCvfzUazQte8QO8U6g2Kt3Ta-2I5aRzDQ5HoLwyshyRM-r1HjZHVXTVxNB6FXDbEIfajfvx4GS7zJUawNzahGREy_NpcoC3B19fPS7B5ANHs-_0CH_fhjcG28t_FXhlpoVB9yA2gZi9bf_xnKlSJla-wTi58k9Inuxo0zOeyEl5l2tTZn8K3c_ihzmlUv9BkKMPlbSMh0yE9N6Djqih0ikqpCRDuhIUZAL6Xpy6DWIGPHrbHBFDq0ir1xWv259x2Au4iUzbnOJJ11RbPANdxoWrLZV7Rq3pN4C3X802Fedg8xYaJWgfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=OX2ccAPiWdVfyHrTWhidKg9uIvx39-NxwH-tn7hjYe6n-QYZsjaIA-tM5Rm4pgwO44B0V4TwSebOrZixUTqU0t_dQZ33b8avhP0RgrMk5LURznyApJi5w5zjuKYg5uEgyhqSZGCkLw9w88A5EJSkSA0RA52kdqqA_Bf_g4kXlOFvRH1Z-F2Jn-nnLPolfWaY04mGXmJ9R5KQ876iLSWMfe6Y3W7VTKHVLBKK7zzBdVcFuLaLp0hI5-zj1tti0WxApgm5XJbcnTx60KoHG9-wvnI6zHh9VXJWEx5oCu1XuzWMZm0ox7lUs2PWsbkbKlC6-xqowB2kQC-K6rl0IL83Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=OX2ccAPiWdVfyHrTWhidKg9uIvx39-NxwH-tn7hjYe6n-QYZsjaIA-tM5Rm4pgwO44B0V4TwSebOrZixUTqU0t_dQZ33b8avhP0RgrMk5LURznyApJi5w5zjuKYg5uEgyhqSZGCkLw9w88A5EJSkSA0RA52kdqqA_Bf_g4kXlOFvRH1Z-F2Jn-nnLPolfWaY04mGXmJ9R5KQ876iLSWMfe6Y3W7VTKHVLBKK7zzBdVcFuLaLp0hI5-zj1tti0WxApgm5XJbcnTx60KoHG9-wvnI6zHh9VXJWEx5oCu1XuzWMZm0ox7lUs2PWsbkbKlC6-xqowB2kQC-K6rl0IL83Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mZwr--mD0V04BQBiMOP7QalgDs34omklv91EBfaQVFKrH4kLl887x-ELCSPrvq507eY1y2JecIMcTlWnoXcOXn9_jsPdVBnz3d-uxeibo6y4e6UfJPZ87_bqa0aG6pU2CTqSEMnL9MHjhA5G2v8MUS_67wmQndWutd51Fw_e9PSpzyHcdBQwfFBSxDwCFTdR0phXWA5AD1GU7B-q6ujWNU-fbTxPoD2tb3fyGSuQWGMoUhbfPF-1iuhvdsVJ9WlvjfZocUX4Op_oTcWUotjE5b8z1XNzwrgLvQgW15Fg_wInHOrtlah9-4dC0JKIn6IIcx8ObDkX_n9Ja286UH05nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s7dGj3JGmhm5QayayxA9wBvDoSe3jACCTvQNjGWhta8sf9HEGvhjw_C01NpcjrPL9hwmnjMH8-vUxzRc2SkmH4rjQlbb6Jeab4QpHJRF7CWZp3roUn6GhF90BXWHb5rsUwGKKBwnZTs6Vid3MuE6MJp6m-sZdaZgOLOz53hMo9QA7T10EDgp2xgxqj3KLzrM3AmLD9K75G89IAOkitlMg4G272PxWgJ0FavU-kDYTzljkM0bnHtTZWe73ne-M9KqWUEum51tsCowt0IY4ak_O7pM6iWScPiSBWK9XGpTJ6dglwFg1bWX9vdGvP9CXpksXtJDY6l1-d5rTifYzqPMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">زبان‌های برنامه‌نویسی توی عصر AI چی می‌شن و چه بلایی سرشون میاد؟
خوزه والیم، خالق زبان زیبای Elixir، یه مقاله‌ی فکری نوشته درباره‌ی اینکه وقتی ایجنت‌ها بیشتر کد رو می‌نویسن، سر زبان‌ها، ابزارها و کامیونیتی‌هاشون چی میاد.
چند تا نکته‌ی خلاصه از صحبت‌هاش:
۱-
کامیونیتی:
هر زبانی دور یه سری سلیقه‌ی مشترک شکل گرفته؛ پایتون «یه راه واضح برای هر کار»، روبی «خوشحالی برنامه‌نویس»، لیسپ «تغییر خود زبان». وقتی دیگه خودمون کد نمی‌نویسیم، حس تعلق به این کامیونیتی‌ها چی می‌شه؟
۲-
اکوسیستم:
فاصله‌ی اکوسیستم‌ها کم می‌شه، چون پورت کردن کتابخونه‌ها یا پیاده‌سازی الگوریتم‌های یه مقاله با ایجنت خیلی ارزون‌تر شده و زبان‌های کوچیک‌تر سریع‌تر به بزرگ‌ترها می‌رسن. ولی از اون طرف، وقتی ساختن یه کتابخونه ارزون باشه، چرا کسی بیاد روی یه کتابخونه‌ی مشترک همکاری کنه؟ خودش به ایجنت می‌گه دقیقاً همونی که لازم داره رو بسازه.
۳-
سینتکس:
سینتکس‌های خوشگل (مثل optional chaining به‌جای چند تا null check) دیگه اولویت نیست، چون ایجنت از boilerplate خسته نمی‌شه و از دیدش همه‌چیز توکن ورودی و توکن خروجیه. به نظرش زبانی که ادعا کنه «برای ایجنت‌ها ساخته شده» و تمرکزش روی سینتکس باشه، داره حول محدودیت‌های امروز مدل‌ها طراحی می‌شه.
۴-
کامپایلرها از بین نمی‌رن:
اینکه ایجنت مستقیم اسمبلی بنویسه منطقی نیست؛ کسی نمی‌خواد برای هر معماری یه نسخه‌ی جدا نگه داره. تازه هیچ زبونی توی همه‌چیز خوب نیست؛ Rust، زبان‌های اثبات قضیه مثل Lean، Erlang/Elixir برای سیستم‌های توزیع‌شده، SQL، هر کدوم تضمین‌ها و سطح انتزاع خودشون رو دارن.
۵-
تضمین‌های قوی‌تر:
اگه ایجنت کد می‌نویسه، می‌شه trade-offهای زبان رو بازنگری کرد. مثلاً type inference برای آدم‌ها خوبه چون نوشتن تایپ حوصله‌سربره، ولی ایجنت حوصله‌اش سر نمی‌ره. نوشتن صریح تایپ‌ها اطلاعات بیشتری به کامپایلر می‌ده و دست زبان رو برای تایپ‌سیستم قوی‌تر باز می‌ذاره. به نظرش زبان‌ها در آینده با این متمایز می‌شن که چقدر تضمین می‌دن: از طراحی‌ای که حالت نامعتبر رو غیرممکن کنه، تا تایپ و اثبات، تضمین‌های runtime، و تست و fuzzing.
۶-
دیتابیس برنامه به‌جای LSP:
پروتکل LSP برای IDE و آدم‌ها طراحی شده و با فایل و خط و ستون کار می‌کنه، که ایجنت‌ها دقیق دنبالش نمی‌کنن. پیشنهادش اینه که اطلاعاتی مثل سیمبل‌ها، رفرنس‌ها و call graph به شکل یه دیتابیس با زبان کوئری در دسترس باشه. آدم حال نداره برای پیدا کردن رفرنس یه تابع کوئری بنویسه، ولی ایجنت راحت می‌نویسه، حتی کوئری‌هایی مثل «همه‌ی مسیرهایی که یه مقدار می‌تونه nil بشه». برای همین هم جادوهایی مثل monkey-patching که کد رو غیرمحلی می‌کنن، بیشتر مشکل‌ساز می‌شن.
۷- در نهایت
Observability به‌جای دیباگر:
breakpoint گذاشتن و خط‌به‌خط جلو رفتن کار آدمه. ایجنت می‌تونه سریع کد رو instrument کنه، trace جمع کنه و اطلاعات رو کنار هم بذاره. پس باید runtime و state سیستم رو جوری در اختیارش بذاریم که بتونه برنامه‌نویسانه کوئری بزنه، حتی روی پروداکشن. اینجا هم طبیعتاً یه اشاره به Erlang VM می‌کنه که این قابلیت‌ها رو از اول داشته.
جمع‌بندی خودش: زبان‌ها قرار نیست از بین برن، ولی سؤال اصلی عوض می‌شه. اگه دیگه برای «آدمی که کد می‌نویسه» بهینه‌شون نکنیم، برای چی بهینه‌شون کنیم؟
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r15UxULGiNzlJqe4agC6rBVlzdkrh8q-96xB8FYBIecY8q_eiusfmlC6oXnZotx0G1k8Pb2NZA4n6nYy4SY2uw4-jMyU3nAqb3WVcaPxkIDiwdSXn6bM9Netyhc-Z7Um7-r-MS3jndT6u5H0UOMOMzJMue6GWOpkL_-yYEtcrkQuUGC12PTMLOMDyHJariI9kzgJ9pgn8j-Pk40ZcuEtq5UcekwcoHVcPSJJWzgCsmcuGd_YQwV0kplP5jLb2636CVaTKStGhq6ygDRFwqHRlpmmZquYp8twik5HwwRC8eYZxOHyMnfO6zh4aylKj0jPVo-tRM2bwBhkvAxtAdiWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت
توی 18 دقیقه
هیچ ابزار خاصی هم نصب نبود جز ffmpeg
و اینم پرامپتش:
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
که یه کم بالاتر داده بودم.
روشی هم که ساختتش اینه:
۱. هر فریم فقط تابعی از زمانه
کل ویدیو یک فایل HTML به اسم showreel.html هست که یک تابع renderFrame(t) داره. این تابع زمان رو به ثانیه می‌گیره و همون لحظه رو می‌کشه. هیچ حالتی بین فریم‌ها ذخیره نمیشه و حتی موقعیت ذرات هم مستقیم با فرمول از t حساب میشه. به خاطر همین میشه هر فریمی رو با هر ترتیبی دقیق رندر کرد. تیکهٔ «Rewind» هم ساده بود: فقط renderFrame رو با زمان‌های قبلی صدا زدم.
۲. حرکت‌ها از چند اصل کلاسیک انیمیشن میان
- Easing: فرمول‌هایی مثل outExpo برای ورود تند، outBack برای کمی رد شدن از مقصد و outElastic برای حالت فنری.
- Squash & stretch: نقطه موقع افتادن کشیده میشه و وقتی به زمین می‌خوره پهن میشه.
- Anticipation: قبل از جمع شدن شکل، اول یک لحظه بزرگ‌تر میشه (inBack).
- Stagger: حروف و ذرات هرکدوم با کمی تأخیر نسبت به قبلی حرکت می‌کنن.
- Motion blur ارزون: به جای نقطه، برای هر ذره یک خط از موقعیتش در t - 0.02 تا t کشیدم.
۳. تکنیک هر صحنه
- ذرات: کلمهٔ «FLOW» رو روی یک canvas مخفی نوشتم، پیکسل‌هاش رو نمونه‌برداری کردم و هر پیکسل مقصد یک ذره شد.
- سه‌بعدی: بدون هیچ کتابخونه‌ای. چرخش و projection پرسپکتیو رو خودم با فرمول ریاضی نوشتم.
- مایع: با metaball ساخته شده و داخل یک WebGL shader اجرا میشه. هر حباب یک میدان r²/d² داره و جایی که مجموع میدان‌ها از ۱ بیشتر بشه، سطح مایعه. نورپردازی براقش از روی گرادیان همین میدان حساب میشه.
- جلوه‌های نهایی: یک shader دیگه chromatic aberration، grain فیلم، vignette و فلش رو روی تصویر اضافه می‌کنه. شدتشون به ضرب‌آهنگ‌ها وصله.
۴. صدا هم کامل با ریاضی ساخته شده (audio.mjs)
هیچ فایل صوتی آماده‌ای استفاده نشد:
- Kick: یک موج سینوسی که فرکانسش سریع پایین میاد.
- Clap و hi-hat: نویز سفید که فیلتر شده.
- Reverb: با چند delay که بازخورد دارن ساخته شده.
- Sidechain: صدای بیس موقع هر kick کم میشه تا ضربه‌ها گم نشن.
- زمان‌بندی صدا با تصویر یکیه (۱۲۰ BPM، هر بیت نیم ثانیه)، برای همین همه‌چیز روی ضرب می‌شینه.
۵. رندر نهایی (render.mjs)
اسکریپت Chrome رو بدون پنجره (headless) باز می‌کنه و برای ۹۰۰ فریم (۱۵ ثانیه × ۶۰ فریم) renderFrame رو صدا می‌زنه. هر فریم به صورت PNG مستقیم به ffmpeg فرستاده میشه و ffmpeg اون‌ها رو با صدا به MP4 تبدیل می‌کنه.
۶. کنترل کیفیت
وسط کار فریم‌هایی از هر صحنه رو رندر کردم و کنار هم گذاشتم تا ببینم. صحنهٔ سه‌بعدی زیادی کشیده و شلوغ شده بود، برای همین طول ردّ حرکت و زمان‌بندی تبدیل شکل‌ها رو کم کردم تا واضح بشن.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JKtIXBMMsYChr61U2Zn_wxfot36noTGJUGE58Bt04FjA2CwVHpAXOBxEc8AQ1HkA-lQhkY8jtJQWkKM3ij7SWwyYSv9I8iyFKG-F32D64n8yBuLRfmDltgnSjIWVi7xifJJcOPXEow-6Yx9OsfMIaqXDpMAEUtsiH96QCh9LAHy9LJwvvYv65n_QbpQntZmX33UBA9QZPUfg3hHaG1rMM06zBnENjXnlewKeHachp7DGkApHS4mhaq2VaeVC_a6Yu1LoYC1OEF6ThxY4JgKp2mCSmkuOuN-cVCgG6GSrplQJJS41YFhSOgOED24Me_E_U-KO6SoBAaNtXeYayw9uug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUsAM8Yq0UBLDn0hF9jsKtKrt06jY56usmT9Q8y9Lf7CYelfs2werLZQelVm8XO2fggYHCDZnfNnULiWRg_x1jSDfqweWMa6fCnl1oAroVYpvYcOLvHMHZRR1Tag8OOfMEegt8jlR7t68_lbNAFEQKQtODqwr2Nd3eNiJTdcMg0khBYJctBWr9SfLfPVLeZPLlV_LHdvSWKalIVK7tBDTYG-ypXFgsCpHnZDSzzu9AWZEmqGBMI3peGmWfJNPmfx_c8z17kKM1vGp0SgDf0EymDWzdN64T7Na8CvD5PoSn7TqUrCCyC15-cbRxHBbxCY5uWOpR-Lsj6_QJrD8vhnlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TtGZCr3-kCPVZULX87G_Qvk4G_G9BPpD09bmgFRSNOnPcQt0CyKS2bKa2m94fZWYDn5LGbjesHJRxD6EnE_JPA2e2mA3nQUXqJ2vFp13SfOSWtJRa98r2LLSNAUk3E_nJBmMBus6pYeDfAPoqCaFSeqefBKqLYRhyQl5w105HhHHSLzpMgdm0HDJMR1ndax5HzBi0Sbs7A6JKy0KwnE-UnE0Zpr9N1j38wp9dIfK6qJzyUFT4rJ9ibdDG20H9XSdR4WwHFhQ7k-3TgyX68Ek8aguFMM7fVWxxDaWmH_KQDjbGEtGV9AuY-vW-DwKV54uE0H804C6lVv3gkBjjwhMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0ki6-NWVdGKx0yQbrGcznd2qt4NNJR3L1P_JmE5G9QRi4i5NNF_cXZi7Do_UvuToJxtub0mJ7HRry0tiXLnvWYs1EbhagiABSwqnsYoM1aHnmXL_u9Y3XsOU5uYaPqBzN6T2GSlUg571tP_Vfm4VmnzKbP1Ury9YER4ANNMNH4hpEoDVB2f5G0ExGOoqh8I5H5REKxwruDK2wwpTbTx4sLZ2D5PV-QIVsyzjq7zHno0-NJvWBsUUI8raEtuHbTvXsB31DUnpWoNdOZkvp5iufe_UEDgb5TkZiF10xJF58S_wCM2slU6i4txxmLnFzPRPKNB-Ev12I0mCI4wH5cpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aTK4qgNlu9t4rna6-EQDzijxBhCRtr-VOCX27tjZlzgWQPrtF9CeLpzsoEYT_wqVPeOL4jYvl1Y4hePn1SKh53pWqvbrp6hTSGadG_hZh0KYvIsRyuovenSkAR9cw6C9ajOeznVCT15Ezn-YxwhPHjyd3UMUn0C9kPcr-p2bYYQPLFSycYedaWIPSJEk8fK9H7JBdQAg8STzrFOgoJZptqGDZLDCB8TwyTXL2rNMdWLZrnCDKvbX7_GhLZEWflkubgk-swdojPhRJvRiLBbq8hLYzQcsPrqDXDyh9-3iH3CljyjjEOtVETcNeAsMVmFTWB_2udCdMcT5-UlMYlX0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=FNWluxRfcsjFcLm938dcePBskwiyorqNDTvSdvTK79Dcc4WRtJ-Gpd8uoLRNfEAfe3Ohi5as7i7hnMrJ-xRch3dJ-ezxpljMPLEB0uDtIrKdkDJPyli08eLIx4drDJNzevDUKbJkh2i4QgaPM3He4dGDDkUYtZgBbjaPtaGFZFsgZFPUTeK28d3RONwQ64Q_8PMPtC6wCH4Hfk9K4wG1XlTI7ClvIgpBrFhIOC8ejiyAneYuLW_Ts6mQAYYTgi0AHgjht7aADiyHTgmf-XWeg912umGQaaS2b7k08PusnOWXkvJpxS3h1COD4rQg2SsnfO4OIYfcSu0LoVi4bdi3EA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=FNWluxRfcsjFcLm938dcePBskwiyorqNDTvSdvTK79Dcc4WRtJ-Gpd8uoLRNfEAfe3Ohi5as7i7hnMrJ-xRch3dJ-ezxpljMPLEB0uDtIrKdkDJPyli08eLIx4drDJNzevDUKbJkh2i4QgaPM3He4dGDDkUYtZgBbjaPtaGFZFsgZFPUTeK28d3RONwQ64Q_8PMPtC6wCH4Hfk9K4wG1XlTI7ClvIgpBrFhIOC8ejiyAneYuLW_Ts6mQAYYTgi0AHgjht7aADiyHTgmf-XWeg912umGQaaS2b7k08PusnOWXkvJpxS3h1COD4rQg2SsnfO4OIYfcSu0LoVi4bdi3EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، Jev از زمان عرضه داره روی GitHub منفجر می‌شه و همهههه راجبش حرف می‌زنن؛ و اینا چیزای باحالیه که مردم تا حالا باهاش ساختن و شما هم می‌تونید بسازید:
- پروژهjev-trader — ربات معاملاتی واقعی که سفارش‌های limit زنده روی هر بلاک ۳۰۰ میلی‌ثانده‌ای Monad می‌ذاره و فقط Jev تصمیم می‌گیره. ۱,۹۱۱ استار
github.com/jarrodwatts/jev-trader
- پروژه jev-ultrafast — ایجنت مرورگر که هر کلیک رو خودش انتخاب می‌کنه و فقط وقتی واقعا باید تایپ کنه، مدل متنی صدا می‌زنه. ۱۶,۷۵۸ استار
github.com/browser-use/jev-ultrafast
- پروژه jev-doom-agent — Chocolate Doom واقعی کامپایل‌شده به WebAssembly؛ دو موتور روی یک نقشه، Jev هر فریم تصمیم تاکتیکی کلان می‌گیره.
github.com/lukaske/jev-doom-agent
- پروژه jev-t-rex-runner — همون دایناسور کرومه که هممون هزار بار بازیش کردیم، حالا کامل توسط Jev بازی می‌شه: بپره، خم شه، یا ادامه بده.
github.com/joshlarsen/jev-t-rex-runner
- پروژه‌ی typesafe-chess —خود Jev در برابر یه موتور جست‌وجوی واقعی، دو بازی با رنگ‌های جابه‌جا. موتور جست‌وجو هر دو رو برد، ولی حدود نیمی از حرکت‌ها نظر اولیه‌ی Jev رو وتو کرد.
github.com/TholeG/typesafe-chess
- پروژه jev-drone — یه کوادکوپتر شبیه‌سازی‌شده فقط با دوربین مسیر مانع پنج ایستگاهی رو رد می‌کنه و Jev نیم‌ثانیه‌ای یک‌بار وضعیت رو قضاوت می‌کنه.
github.com/RomanSlack/jev-drone
- پروژه tax-doc-classifier — فرم‌های مالیاتی IRS واقعی رو با دقت ۱۰۰٪ روی ۲۶۱ فرم دسته‌بندی می‌کنه، با هزینه‌ی تقریباً ۰.۰۰۱ دلار هر صفحه.
github.com/kyotofin/tax-doc-classifier
- پروژه killmyidea — ایده‌ی استارتاپی‌ت رو توصیف کن، Jev از هر زاویه‌اش امتیاز می‌ده و بعد kill، fix یا ship برمی‌گردونه.
github.com/monteduro/killmyidea
- پروژه jev-curate — ردیف‌های Parquet و JSONL رو با قضاوت‌های typed با سرعت ۱,۵۰۰+ ردیف در ثانیه پردازش می‌کنه و فقط چیزایی که از حد رد بشن نگه می‌داره.
github.com/AkashPriyadarshii/jev-curate
- پروژه pg-jev — افزونه‌ی PostgreSQL که بهت اجازه می‌ده به Tableهای خودتون سؤال انگلیسی ساده بپرسید و جواب واقعی بگیرید.
github.com/realZachi/pg-jev
✍️
imryven
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/erAM9B4wgWryDw2D3OnZm_16-iLJw_5v7NfBfS4RNdiIMtggsvkeGTmQM4-bgjQ6n99eVIShNxXwURdUMNL6MixW7jLHisMEt1waBIUdUixyRyyOOfMnqWKcYeNM8uFjHGwfdsBBOpIoMj8uA0iAlY7jmQg6yzmILIXtqIdzPlDxOBxez2TRSlEfs-o2MxmJhRorGb9qzb9SD0Rk-iwQliyFxHJRQmgfwHK9mxcDhR_zrciemRDAR0KaByAjCf1lAPiJxkwiR2qWCwCnK01XHGco_1Cto0nB2UIuOsS355-1K9Rmaw7PQtIQzk0H-d9qQPdmNNHlYS89ThF-kA8I8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هکرها چطوری ChatGPT و Gemini رو کردن دستیار کلاهبرداری
🥸
یه تحقیق تازه از Vigilance Security نشون می‌ده یه کمپین گنده (اسمش رو گذاشتن Dark Sourcery) داره جواب‌های ChatGPT، Gemini و Google AI Overview رو مسموم می‌کنه.
قضیه اینه که: کلی پست و PDF و صفحه‌ی پشتیبانی فیک می‌سازن که با تکنیک GEO بهینه شدن، که هوش مصنوعی شماره و ایمیل تقلبی رو جای «اطلاعات رسمی» بهت تحویل بده.
تا حالا دست‌کم ۳۷۴ شرکت قربانی شدن؛ از Fortune 100 گرفته تا Delta و Lufthansa و Bank of America.
چطوری این کار رو می‌کنن؟
1- شماره‌ی فیک رو با فاصله و نقطه و ایموجی می‌نویسن که فیلتر اسپم نگیره، ولی مدل راحت درش میاره
2- شماره‌ی تقلبی رو قاطی شماره‌های واقعی می‌کنن که معتبر به‌نظر برسه
3- محتوا رو فوری می‌نویسن (جابه‌جایی پرواز، قفل شدن حساب) که هول کنی و سریع زنگ بزنی
4- پست‌ها رو می‌ریزن توی LeetCode، اینستاگرام و حتی PDFهای سایت‌های دولتی و دانشگاهی
پاک کردنشون هم فایده نداره؛ کمپین اتوماتیکه و روزی هزاران پست جدید می‌زنه.
بدترین قسمتش؟ Google گفته این خارج از scope‌شونه(
😂
😂
😂
😂
) و OpenAI هم گزارش رو بسته، به این بهونه که reproducible نیست. چون عملاً به سیستم خودشون حمله‌ای نشده؛ فقط خروجی AI دستکاری شده.
۹۱٪ آدم‌ها جواب AI رو چک نمی‌کنن. شما جزوشون نباشید؛ شماره‌ی پشتیبانی رو فقط از سایت رسمی خود شرکت‌ها بردارید
چون به زودی شاهد همچین افتضاحی توی ایران هم خواهیم بود متأسفانه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ro8M1COOSdGXYBc3jUZ79k9Ib3DO7sGIPAiNtccdQd5elt_bFDaWMYRL-OBQ2fbv1ZlxIqJPIILK382U6M2TcGqK3f4AHq_ab7gb5MbDhR3ijNNUZCZMd8BYHWrksbY2fdFhjBdLJS9mJCvfJdEI7yBt3XNsPUO7k-2gJ3LvZ-SdtlGinM5DyhNWh4tao0FmQxrwulEthzTD9vJ3ikzTH10QagwKQ_1k5_lq-Ni2DfQiDY7NOVg99wYsNj6ghRYjDBLP-ndSd9jSdENO9Elz38fndQyWtqJOAUM98KPvM5HZhBztqXiDfNhF4fESgyVmvCCPMnZ2lagZsz-iZd807Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WydhBziaJb9o54IBTd0qHYDjc8gRWdxwVUDG81YvK3YogWrTjbTE72wqnXqIzrj7HVlQooiob3CTYr7Q1YQgj0tfdatP0I9ot9boF9QmuSBg4_1vZysNzo4zF_IBKaI0D3lBsEs-viGGlRRzdxigKvOhC2DXxmEuYPmx9T-Y_8xnH3D7_-TI-ZdufXKrvRaTxEcVJwOt7yZmI30jSOUzJFdfzOikp40qK04owwR5nUQ-TSsr9NH5DIIYYyJc-d7anTiSj02jxHP-FXWBj9NWMpYv87z3YQiIqhUUtPwLNqk02hWfQisVz_udctBiumoSpxPqd8jI-xE4A6El_kqxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m9fvwKDehqJIBvAjSbXwWUxVKueS9pfx6kqVZZCzczIksxT6T4f2XTykJXpA2x1ie9MePdb8HSmCzAb9zo6Y11yd1Wm28emcxdfIqNPTp2XAzw06bZxYgR_wTyiVUUjBj_8fxvXBg2rUr0WWiUrdlNtOBuFESIIuCVCbpdMUfyC8gxueDFD_ugN1HOZx1PiycgLnQ4hAwCzm_xfQNTz8OMEaqZhtm79rypjAHeZHFX4I8Tp9nG-UtEvOwtV06dUtF-O_B2I1RCAX9waoojSyQtp3qekfWeNgBsT6oAqzIXrohwCoAanHm71jKv-S_FOd5SFF2qA3v7TF8qUc0-NfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
