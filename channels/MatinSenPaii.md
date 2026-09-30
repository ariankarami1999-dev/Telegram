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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 13:22:45</div>
<hr>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HavspNSVUJwmDdQe2YiIoBiLsNwastHFquzjwNa_VkR-pV3lqYGvTqyvElfjS-u4LsCPX3gZVeYqpsyYsuYXtxpTkfZ6usw4f73odSRsdBoCtTEXmf5XsC5WqJsF7P6CSeAX4sDEKhUMze2bRn8ge345z9JPgBSm3NaBv2St4qRpaeB3cXeTgZA6UwNo0oo2eSFDwnohkGfxm2Umrm3Ix9XkflzIDkdkqiVFZoXbEL836sYvnxCZls9LkvSPL8C_eaudfrM_ZN_GYMh1UW6USmfrH5ag0gH0lzkQA3R68OySNwPk6AflFETWVWb5zcYtQTJelINcAAxZurafKyVChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HqEv2MnqEWfVF7XXfZh3i9jC2SvTOkhQf_YuWC5p0HasNlrFDSVL8gX-Oz2BhBSwdqoiwL-gdBko4UbM8kkuUNGTojrqd0SCX2I8b3W2PS2oBSIytb4zodFnvIfJNajHoh17fR_qIrZJLyGm5SHmzePM4PzYu7dUWXK6rgPGl2j1rqX7SQkorK1LjgKYsvUJMjlopWuVQ3kwxdjUiO2x3qEK5LjWHi82FSdkEz9UXoEi0-KMjfr30urZR81mk2jv6OXVgTAPuu7vp50K0bMfah9T1xiJnkkx2UybPCvjewwp1GTll_TpTMSJTcBK_2BmPGq-5TBlM3dZZoQLw6u9gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=uuxuuqy877Un0PVkbcSc956oMKyLcZijhTIMIunLf0tm8qEJp1GtmYaB6Z3xMHuiOxhvwSPRLF19KKqgYMGsxTrUFmM4GlAZ6EwQNto-3uzvZU-oqmzq_cCP3w6AoEsvgwYCkFycLLVzEL6r91KaY8_bo3N-ZZJmZML6xwssWfDQ0DpGXSzsF__4Nzsbbzx_RMTNqHtBzz3OCTFmiY7fdomJwUBkWWteXe2uiMOVoeG2txd_GhXlFz2M1ZMRFeCvfd0AqjqronZjQfXKiigBw99_9R7wRI-ufSTsYJHe85sL191bupcBHiHczpe8RQLXGCEd75PJjXbLTa64OLx7Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=uuxuuqy877Un0PVkbcSc956oMKyLcZijhTIMIunLf0tm8qEJp1GtmYaB6Z3xMHuiOxhvwSPRLF19KKqgYMGsxTrUFmM4GlAZ6EwQNto-3uzvZU-oqmzq_cCP3w6AoEsvgwYCkFycLLVzEL6r91KaY8_bo3N-ZZJmZML6xwssWfDQ0DpGXSzsF__4Nzsbbzx_RMTNqHtBzz3OCTFmiY7fdomJwUBkWWteXe2uiMOVoeG2txd_GhXlFz2M1ZMRFeCvfd0AqjqronZjQfXKiigBw99_9R7wRI-ufSTsYJHe85sL191bupcBHiHczpe8RQLXGCEd75PJjXbLTa64OLx7Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bDongujEVBS-YLm12hewHiT2bdyWJGNJsX57HW5fPlIQqgMqCvc2RyYnUtYh_TSEbgBS0SwfozUzMYjne9lnVZ7sXO6WyBtEM89it1-WJoRaMUuSlC7_1gUqAoRm48nTNLIgGLh5gCdhZe4NhQwwPM9zmMXN9lEu6O-p8xyNdX7Fc3ozYzYRq_c9R9k_DNBBPmIfEiijY6DiqTEA0rpWAhUQ5SG3piU60a36RA9HcRZM2wITnK5pF2GR7ptJXPEqlEs8ahF2Ol4jl4le4JQZnOxk6Awt7h02zztrqsQEiyV7a7BWVZbwZ3dZtrHz3p2ohU7C9tSfGl7vQtKv5cTccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bNbB6yxWHSF1elui_ggUR2oJV7eaJxn30O5GaU048MUDalWt6Ylrw49SHDpY_mBMVuV3N5QJrz0qeygaKUPDsSotG4qUK-ye03sc_oEFTp4ohy6lKAdYqaP44lvsmSkIbESRezaIa2B7CQPWzNpNFq-p61M6x-4wUg08BCB7DIw0gWhe8x1aZqjz_78JoMz3AV5QzbsT-hL4x11p-39qIHeUghgi06jjVZQ6vU2iEYzig2VCGTCFRa3eHLuw1BzujF5XeeXUqCu1SwdMJLIOPfazff7sSJDuyEtf4nom9jR0AnfVtqEG8Ojn4XQH7pnkWhiOzwSqdgWDdXE9pkOzoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LsBnhEZnfph9vAGmly47iHFFSHokCRuR4Niza4Dk2SxmrkH8Y4FSlgkkR9E-jzOvvrwMCukixmErEfI-58y0d2q7-v9oWKZEKPJOpppgtqc9Sj_yHiOzQjzkdrIujaWScRgajT5vdUPUt9SI3GPCUdilB021USFUH04h3ny7tEzDadCgUYQ5NGg6Fc3Yk8saWESPgjh7-TCg6lj16bIa6go5zwN4Pr6oMqwl8S9M2OVUsQxTI3CrYXZMKuObyJsQO7N4P8oNZ8tm8o9qzpaRarTu4rsXO4IkIJQKF71JQJSvPARSSCf0y9cdcWQMZnTPiqpDnpif5gRLr5HM-cWTpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=GN9xd0A0cMNL66OBq-PZ0lVUhFBddqZk0H4gapvEAtx1vvk4V253-zgLmgOHqHOZeh6GZJ4n3jaWMTQXh0EcS91e5nvUD7qUkAGXQ9snPlEY5U3z5jFNb3PNZhs_DLJBCel8LNOSOGZinShBkHSZ50k6bhL1SIRgC5S8t0SDRZDvCOcmpBf4ps3piXSRK4FOgfwVTWCoS6YBz7GFMDHxfgtWe92uNq6lX2huTs6F44HzR3fRc3NTFxahc8Dn4j-DCWBrDuwOggxFGNkQ002uLPbVJ_16OLI7GqJnfAXfF1L7oytqvzFUdIHuRUG3JvAqFFfT1E6P4AtLyVDle25nUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=GN9xd0A0cMNL66OBq-PZ0lVUhFBddqZk0H4gapvEAtx1vvk4V253-zgLmgOHqHOZeh6GZJ4n3jaWMTQXh0EcS91e5nvUD7qUkAGXQ9snPlEY5U3z5jFNb3PNZhs_DLJBCel8LNOSOGZinShBkHSZ50k6bhL1SIRgC5S8t0SDRZDvCOcmpBf4ps3piXSRK4FOgfwVTWCoS6YBz7GFMDHxfgtWe92uNq6lX2huTs6F44HzR3fRc3NTFxahc8Dn4j-DCWBrDuwOggxFGNkQ002uLPbVJ_16OLI7GqJnfAXfF1L7oytqvzFUdIHuRUG3JvAqFFfT1E6P4AtLyVDle25nUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tPGoc9FmS9noqUrBGBuv_AccTcVp2lGriO3svxIs-iH_uPB9LXZegJ76s1PoR8sDt38UWejqWLq4KGr521_4e7ffegZZAWyDczAlH4Y4Mq9vdr16INIXEhsZq7JpqyM0hIm8-hSWEgWUSjwmOGN2jcKBhW6LhiHw6RJ5Z6eycGmEyck_inoq5Zaj61W9fZcNVdZEuh1lCYliL1rQvX2KXca_8CgF8GHvXSuzXrf4RGI_kmbfn9wW5nQoETnpi0P_dP6FZruwr7t22sDfO0Wp_adKysgfxz7G0I4gCUd9PzYxOtgAQ9ZoO7LR8RmpYpb38DDCxGWGc2D-FhJoXAh7MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hFZUXk11NeuFJ-qTcpfYbBdsAMv1nRVl5MWJW5MEjXgS80G4-BGGh1p0T7O6kZgLePREoRM6Fca8J0Xg0Sp1ty0hqvEk69oZVH_hugA7ZoYwwebIatiD3IY1Pl7N7FpiZnk8cnCntiA2q14H6CMqXTX6cxeoPSh3IpSkym6OJhfUD1_lrVNpEUGBJMVDzuxT8tI-DF7p-Jp1mK9-5IZFJouKlZhlYetUcBHF9cCahxod8aWrKspShRfhZ9sH2E-GhAl8gx9kH5DA35MzH5yXeXztypD4rnT7EX-4_JQq_UkIJie2JAqsX9s-4GF6rbtG1VViQ_LaWJ-i-dqHycU8Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SNFuxA0taMZ_Ag6NIdz-AzU_YjfdfmOc0n50a2I8z_hm7QSvn1KETyUc0Wtc5SPTn_cItL1jQu3fYjGt4fZ5KVgXSOYwzTQZzdDvVKyF8dgbp8RvPtg6m8wC2pePTiMq1_Gy08qHkQARW3LjFR7MvSme_6ip-sj84kxuUhK_4wHxC6DWSRbdka_CQRIsMDlfrrNaa5gYBex2UM_3bZsio8momF52q5jibS17QpOIsbUkZjXE85EtPO-aPS6FfdZBolzNHp8woGgERezJ2OdYdsUcs2iHI4OHwZF-s_nwyoL5aGomqjdwalsN_KL8Ums2ze3BON7UZiFzzMJU4KnVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T7sm2fyw2L6hCgc5IHPv1JwY5LfJYZ9wwUZHzHN2YWwWYAqxgA7NJYSFhDeJs_TsfHvJZWR99ymrnJnCMfMeAjbsh7dQ3yMa9rT1MZ0wXg3DB2s2J-_U83D336e7kd8sAoHhSr8zTDSaXzQXvPu_VQJuXVsMkzDHbG1gq8v0nQLbpdUnA2wPXtYDkx7Dx6qLrO76lonkZGcV6Ji0-oUSjQoJhj5d0lXjtrrhsnoLyHbawI4a7IZ8wVi6tLsLX80QfPZhl2es5e6vwbZH9MKedsRtVri2eaaNgSUz6f2jKGY1nlFZLAeQS8FPNhPO3Ydeeim-ohbfTkgauiMYuPd_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k6p56_3c6wL1DD-WosAh9X6EItUbb6zcXFzf_3hUmQx6T4YfIlTJOYdKLt-jCeWW36AZjsbRBzRtPh0SeSm9P_I_vvMKERkra9eNvR_VfQ3ZiUAXLHDVrCaCr0ruD6s6ro7T7uOAXJI3Z9dG6FzNKkVhOqqIdpD18THxn2_BwXeiWGEa1E-nu4rwtBGlUz7Hdp_WIAhwZnUszQ5QhIhN3uKYy9iYEl5PfOGEur5-Rv1qp4J0Erdv3QRS-TLeHgDOTc1rUpsa2nz-x_GEPeMr2PGiQtfKL5yWKKtwWxl3Z858HKmcm4FFbsFBa02W4hYNPf98TG79PT-l3C1-P_5kew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ujj1r23CYQNl_s92AcFtXdbAhNi-UzLY4EefGpBjUh9LtKYbXrfx8e7z8aRC6L4lUvheFyfNM7RbAAWvwznCf54jE5A7QZRc-_aFSwxMdylgrPVDCgrMoCrShffsERjmtXSaIoyQkkQ4SYeFKCwrYMXOricYBla0CObeLoxGBNGcEGFgaVLV9tw7GEvKta8nWzyRpzEYLbeH4KE3yKDf3PaJ4eqzznueuD7KDGMaVGQpg0ETKyIaiCjsq-Lvubi5UOqZ8HijG1-vQvZs6hH_c4lmaQa9PYm9nfn_Vdp-8vWjaKieI9TUeD0u6RsBlihoEwsNYacUROdRnVLPtwUzbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DD99T2iygEQ3ZA3vypiOlsKu4mp3WRAzToAgKtHgBStFf0PxhtpRZ4N6hGDOFT5-QV4D3TdPObAXR5hk3rI2FelylsaL6sQX_aDzhPEbp7Xr9-W64bqrTYj8XXthJicfqgzmFukY7iEJp7hUrvpPHQTgxi9-3PSynhIE-xM6qkONyy7gbRIMEey2dF7i3Y0881ZoFJTjU8dV1TXiXQ_67QC7WbRZu2aSuom9krrIuapFLBAifpLDBW_L2DUWi6WdHRoroBmb3lgRKt8gmm6QWdd3fV79Vw5t0XGOk6A5mppxJv4TW0ZupIoo0vvylqSUGpr0s3dAR9DHaEX5Wf5-vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=tTVuYxYcPfBgXdajO0qu9zfliEPJIEZl3FldYKEALLwQam41P9yLViQrftoCukIonmTPGUTUSgi_ZD4K5prpOysXpREiIbhqHhCSf1UpldVwpXq5EnBNt4xv8etl6C4ACKzf1ZAhbLkChsMEbchfcEt_rkyCK4JowM-B1ZI-CVVnJoDo5XHoYjUybn1i2znL-xWPaeFWfSHrnK1AunnJvpLrEQrBlbSExPY0MtGeBcu2alNle4E_1V40Si2rDrBWwLxGcqjNgm9Zqm1bD8pKv7NYKhOVDo1gBVBl9SgRw-pd7edJfBHp3jU_6aYpN7hshoNS12FlsQ_Qfuvw1OmWtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=tTVuYxYcPfBgXdajO0qu9zfliEPJIEZl3FldYKEALLwQam41P9yLViQrftoCukIonmTPGUTUSgi_ZD4K5prpOysXpREiIbhqHhCSf1UpldVwpXq5EnBNt4xv8etl6C4ACKzf1ZAhbLkChsMEbchfcEt_rkyCK4JowM-B1ZI-CVVnJoDo5XHoYjUybn1i2znL-xWPaeFWfSHrnK1AunnJvpLrEQrBlbSExPY0MtGeBcu2alNle4E_1V40Si2rDrBWwLxGcqjNgm9Zqm1bD8pKv7NYKhOVDo1gBVBl9SgRw-pd7edJfBHp3jU_6aYpN7hshoNS12FlsQ_Qfuvw1OmWtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jvMdDHhGcv881dYLXQ1UWaejn4NFq2mOdoYzH5_-eqXEvZbliYkMrqNzlxHN3dYzTjhlQ4BWxhhX8crv69OGe58k4af6NhU1xGQvhJqa0xGOQlJzpMn0Ls7i_Al47jBW1purtGh5wLQdsEtCRrQtOW5dgA1Q7ws9suxepTfytT2z2t55NGTk3pbkwQPpkK1-2y8LeqYQCmXcIHe7jewtvJYYFhgrtlzLj1AtEeot431ExCuwKg99nVUeTm9CmMSpum_47sAF30_gxwVJjuRXBevSx_Tbe_jnjZfUXOP2jjCjPxA9aTZfxwC3frtiC0_L8Pl5wwBeFAh1xfwSy1MUUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J91qO1WaFstp4io1pw3yh8fUr6O-OsV7U-aLt-PkS6bsVjuAbkwwhpdCOofx09-UIUS7NGmvpp38rzRgkD2SdRjkzJY0ucJxz_DG36H-sjwLhZ3eSioQ4fpJXQr_uoxLKnHZypIi_XI_glespROBcuv8dyfrz2j-VnGbW-99PTMNyxAgu_wGuYCfpBBfPu4JNVpvmjwv2bJgxNJPc5HTcue6aBoo58wpbdExHRriDDefY-ppMm-t8LpbqWq_pm77ohCxgVuXtsW_kjuvfDMJ8UWVU-A0Zl3FkNaatzuTCJxdDHMyYVQQqMjkOEKpnLpPD_NR0OtnccaRdfuFNx816Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mzxNXMXhw3uUekcDh3rPFvHfda4gAZkZ6mQItH6t20yQ_JtdYTH3t42s1jJ6x5DVH_IbQOa37sl6CPT68XBG8VpINsDcxB1zajbgOKhJwwFruWxrK99ykTzRrOCYXch_FySldMaRUSOp8L9sq6s99d8UO7O_lkp6gjLv6m2JT7JN5A_g9T1DRduH-yfetYwUTfD8lqJd2UoGmx3NeWEP698uvsFYwMNd4Ba9RnfHbMsWS6MhuByc3eVjkojALqUojhFG1OavwlepAgbSQxAM4axrMdC-Dnr8Lz7TMSqNsGXLWwM2v-SfYSOkh-jUsPaktJiEWH0FoZsF69rEUi5W6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UXm8V3Zvr6GBafiTKFR4kyWI-mftHPLPy-LhJcwoP8xzFnGXGricXDjz0Lb3oBIpfmoGEriWMltmE22sV7ijWxPW09-Y2RfYho6dfeHX8qLcyoReCzSVdKxgL5yeuNlKxLILFgLDozy3751FoM89m0SBHeAwdQBbQgcBaevHCMd1dE9M1j6p7mOSxn5USG41ekWoohBXWsxdPBA7ZZKJbeFftlbyr2LfQo7QlCf5wP-f2Z56KKYiP6S4PLyJY3rkBEEvaqs302SlX5OIK1ZYqAWq0oV-7yhbCAtWjHVQQbm2VxTmci_jvvMcQmxYH85CSebpBbsemaVLHV1BLHczUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hHxLcMry5m6wFKzv1ubuQCQhdsOqykg3CDvGtsztHUP2lJ762O37vitn5o_fFfQLUsQJa9282G564cAYpKlpC6_Cecd0e54lTYgastV1OW-wgx5MakcvZJ-xtpWXIlaXoe6p_RjToGNiZWYy7hqEGAijHbMeDsXBAv8QFvoVFb-H1xrQhXIMI5ApHPOJPSqRxgoikcm-imXkgw6QGS3y2pYNhpTtMIB3f8y0Xkw6f9acUOOVlNZr08EJsNjUzvIOs2oROAPaoRWDy0vGgqcVmxqLGAtD-V1HSjpVx-MLB9YdSv5siZpfynvA64RzSur1z3Ht5z8J9VusEVQeDFPieA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZMh3V_FMF_dMIKpXHTNpMfEJ9M5QCyOfASCsizzSJiJqxcIn3RUBhmAJ9g4eo8U0nyPMffJuT82zFaCAkEr47sHKwxKQBW_GX9ceXt_mHXGZ8ytJhTyaj1cb4fXLQ-6A4BkpZP5rLmXOITcgYvlW8sSs4HSm244oR1NEFXL1JwJ9nO_r9ELDh5_uFt3US6entYqnODfRQYHexDRKA8A9Xae7sljmzDldzC7JPNQGCiSDjPCsFXIsqtwP20V9YnxPFUfJgWtv9c2WqzjyG_VSe7m5SlJ40eV3iFfEpoJ61vHkCY8nH_U1DKwDoDmRC1tvd2aaFylBjrbnO34PuQmkIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sBy2DbrOsz9RKQXZzS_MYH0L2nLcL7Fub3FvfzHbPoieswDtKuAjpEuA0sfMRqME1Ddk8sRalR-Kl7ZS4ycu9jV6P17k1LR5q-Reqchh73QKciU66ytsLrI3veNfKrivCEksfwv8fu59AI-xh4WlP3G1Y55UVNynMwk0cq2DXOE98_yOsdb3U_IQCZ-TdWXxWP6tFeWXk-9RJ0ysQsoXlVoOIMrCqYbPle6knVlB5h8Cpdmp4MaEyYHB-yRulfxABXrOuQ23PzCWAT49jmJre1dWEopM0aXaWZ44I2eFKDo83x1cuKhGkrB4s-_hVR3_HTmWDVStKFisE5xGIn0S0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeVKaBlQp5gYt7O-1Y4GueMpzlojaUwMyV65I_az07UbIHIwYPpvTR-GMVUPylDDDaw1iH1K290y8N5km2rx4MVoJNZSBKxv7R0XKCJPKitHhCQ5BTTiKDoZIXqYh4ZBok7nQUKNAvTTV4lIgjGJJLA-7m_M3XbkYKufd1AdzhGjy5Y9uPKSXbeHlfKbkPDPonyEJV_PYBu3wRbdYnf4tX8fxHplee_rzkZ9Xv1c0ZvmEQnwBbkQIOuIPopIPfOpHOdjekVa0a-_loPUbPkpz0TCmUkVRAYwakQWGMkLehnv3yLfvFCbo4QR8Kq7MOSL4dqy9nZ8Zhxa_M6i7QIEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iZEitaGN_Dpm54vaNnCPdpFcEvM7u_LWYzMESeyWYnOP3E0r8wgojVbysQSCb7xMExJ-NuvdxfErHs5IHPyuBRmCCDF3HnHw-Ztz8t8MEAfQ9D2Gq6HCsnb-0E8I2yVd72XfGLJ4-fa2HYv-7oyh_ushMwCrXM748RAOhhuUHmsBgbJQuVn1767ZlTjQK1ofv943JpuRDuBSEyB1H1t71SP9SQjhb1vsjG6YjHO6OLrMRnLq9NFrOFTnfaMO-JGQJu8VhLJ1_9IxyKW5jPRF9jBYTJT6Sb7lqs9S649nTB6wThUzFGhpbAiNRnxNlRbelMaV-9XHCAgTBHEBFFsUdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMyIkXJbOWSIf-DVkIIDHlyKFzwTiDRSrozKU2ZfMX-61vDj1h1GjXxM7KWB9ivTFEzBVbWSdfKzYaW3-nUe3QFpvC2B-bgRsqH0Nyv_tEVm5eu0VazbGchhhLkjAS71aQonEkaMPgZhEHnss4C7krI2C4IIYQKVnIk0A8qgjLYrQYXw1TgE7qHZ6izT3PUCGZugQNemntI7mCWLpeIK7ovG420yUj8izyJK_FJCciCLF5h41OEiU1aia7NCAukvKRFbnMyNbZNPxVlTa8w_KqTRiGbj7fs7yT_2H-LkuMk5zCMr1OcPxmkHqTKg1RgZLwP0zV5aw1RM1gK3W3PpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=dendvx6ighCiauzKI7XeHs5M28s1NvzZznRwELOO-mpGE101nS4I8o71NQWSF27L7s0lVHLbjS5s0t5Dm0bmPjxH_SFwTzZG9WjdeEsOSqWv01hMIBkcJ13QJ5jloKM6-q0Nj-Yrn5rju4-zUKXdywM4Vf7y3c4Luy4RX1rZXx3gKnJzUzYfB5c7hEQ-rK_H1IFDNnZAIhiyAysgWANXyJf6Lv6cAIe6b0R_StzUv3owh1GwFzw9Oq2tcXWAU8LYnZ0Y3xgiAZoksxkqAUjSz-w2sx5lUhEbM8ip4XpC2yquGfb6O6oyY0C-qr7y1WCBNuIv-RIGmEDqNRCQyOcXlwwkG2fWv8IyX3R7FYGm6cYUh_IDLimSdwvOXz0RXa8-MtaNKQfALEIBEqvyvtGPWUHhgzRsJxfhKtJyGHXFtwsVpY6RR3-9GTNhuNhJx8a-5b-R9QWiYPha2T56tKl7-bhr6s3DhWj5MUMaawgeCjK_iKP_X8rhMpj-Y3Kg0lJSuIIEUSuqSgW0aUdgVQ1CNVaRWcjGW9Oj1rY6L3ZJ1rgLXYlkC6GNv_vKE6Mh5l7cmejE21UH4TqkNDPbt7CmmITVTzGM_JQlFATbQoiaGxiWdVwGEbmPV7GGtt6RM0XCo9HAHn7LNtMwHPv180lx-eIYvhSJoSk1K3Grymnfzjw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=dendvx6ighCiauzKI7XeHs5M28s1NvzZznRwELOO-mpGE101nS4I8o71NQWSF27L7s0lVHLbjS5s0t5Dm0bmPjxH_SFwTzZG9WjdeEsOSqWv01hMIBkcJ13QJ5jloKM6-q0Nj-Yrn5rju4-zUKXdywM4Vf7y3c4Luy4RX1rZXx3gKnJzUzYfB5c7hEQ-rK_H1IFDNnZAIhiyAysgWANXyJf6Lv6cAIe6b0R_StzUv3owh1GwFzw9Oq2tcXWAU8LYnZ0Y3xgiAZoksxkqAUjSz-w2sx5lUhEbM8ip4XpC2yquGfb6O6oyY0C-qr7y1WCBNuIv-RIGmEDqNRCQyOcXlwwkG2fWv8IyX3R7FYGm6cYUh_IDLimSdwvOXz0RXa8-MtaNKQfALEIBEqvyvtGPWUHhgzRsJxfhKtJyGHXFtwsVpY6RR3-9GTNhuNhJx8a-5b-R9QWiYPha2T56tKl7-bhr6s3DhWj5MUMaawgeCjK_iKP_X8rhMpj-Y3Kg0lJSuIIEUSuqSgW0aUdgVQ1CNVaRWcjGW9Oj1rY6L3ZJ1rgLXYlkC6GNv_vKE6Mh5l7cmejE21UH4TqkNDPbt7CmmITVTzGM_JQlFATbQoiaGxiWdVwGEbmPV7GGtt6RM0XCo9HAHn7LNtMwHPv180lx-eIYvhSJoSk1K3Grymnfzjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CpJI4TjbdatnDQAl-CNOgKYc0O7LxqPjcYu9whblYQ3tqE4TGUTiAz9tyVFQDOvwGFLMAvewy3lTdVLzkujG-mJYXbAhLd5cdfqSjSv8GTFd_TEkV3a544bdThptw7-9ZKG5QLR7GU2Cnsqt1ywvNAFOA6w44t79uH5dKUxi4a4mxYU4Mx9z6N9NM8_7oPkAr-dT9b8K3JSNDqlMvhR0tPeiE5T3Lp52Y4yBcu5LFep2rB0AUlKo-NQxw3VnTq70AkCo9aMuki8w_Hw1cqo8ttipFE7k8k5YVJtvHw0trpw8nv6Si1zOOm_ppOOpFYR4Y0lU-oj5glHzg59zjcdp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtBbd02VUApk0QnIEQl-wAUNOaqAnxJaMEP67fVFS0j3WFz8x6ugoYC4ZyDKhmO1210rQI2a2Ge6mWOiUdqspXiZOK_Ff6eGcYAvWSkm6MvYVR_3mrBYycwT57Sl3AqG70TJFiTg__kU4OIZ4JKuMnBP7Tqc2mYFOcONUTPElobFBcoN1juVX2r9Toitk4KF2gp6al3Kiyg0OsBQ-0jjoMtkDXv8MwFV0PuGxxs16UUsJ35RGZkYkHYrbxu9R0AHAu4FNbvKxLLY6EcCB7lwDdhRFk0nzwfyhekLfmWkzmbYToXG0GZAhJi4-4K8yIPoQDtOMR47AGNbVzHgDXZzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ESblnEI1Pi62BipFZ3W-6e-hlX7AloHhrf7m9pZMVCfD2WeWuOWU75QwnIgsK-k1fK2ttUYCwn-eTK9i-d-uTsvn2iPifmnRgVwEF34OVlxvdRuu1dYM0sbfWCf6WguQsU5E-PW4YYcEQRwRTz-tn_tHHe-ABAL5e-glntPmAG0TomKce982AUuHFZWtlN4Jzx8oG3_Ja80OHiW9a4LZGUcsCbW78O3RWj4WNQVxuTTn1J3R042pCBjDV_jdQhePfAo4-t9kGcxUXyM-ePWvGn6fst5dgSPtJA0383JvCeYfj6shoMwfCDMTxzoQs3dOMB_gkqvNCHm_SydCXEj_aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWkCjpfaIw7iHU8svkR7e38q4SioE_yGjBa9nM17KvtBY_p8Jsfmq7FF2_SkkUInDaEshg4fNYFTDNExWJVRRC-9s-dDVRKOFYIXkUOY5xWBjWovB_TjJ3mnMD3oGJSqib4-O0o7wfPR9gQEAceMCb_JlDSpeqweYAsIejPTH55YijyxGJEFyNwFa4y1GGltYo2asJszjJx4-LKurKgX_OG3DNZCpDa4VrUzFtiN9qdHsn6Dbi2FG2YGpPdTujWR1_x8a86AMSq6OJ0LWy3Y9VeM1k91EFGyFRdJbUF6pT3qUU0s5A7rSXPnlP2Heo04iJhuJ5cCRXQPHqQAAxczBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JXJhWsZ0ssYrKEYOrgXypKOgAAi_Rp77yZwOFCGBRGN6mSPTnauT0NBAVxAXGov_Fe3ew8f9l-bRSlvHnZdwO0nOcR6My4t5JAw3a20bYIYNGzKPRYZ9fIm3XrzibaWYhklLEMgnw023v_Uuw8ESRQQ3AzLy7PqrWtjKTayA5srG7S-MaZr7HBerokJlvUul63fj7D3G6dH1qZX4_QVjUwpZpJjynIAk5tSEW9jf2XhKZDA0sCBHkvwPsc5z6wKWuv68YQSgDCHaYjigWJalCo33uXiltZq3c1WkO5p0thVVkan8v5eScOvy3nPTTPek__hPZYJnvhE51lV-u_fFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QmrbI1tLse0HfC83BkTf1iHluUG40JiVYAqIVv3MMs2Sa49b_dFGqL6GIuKjOQmZRBvRt1yhKCn0zb7cFjnvQ9MNKYpAvXiLBMJsgXstGT4TPbf8jR5TEqYZ7fkq5V4xuQCkY7K4HhQTiCkN0a-44FY_QaKc5HgDmbD8QOLowKOgqOG29lJwYcgZye_zdKBYqEyuDjNppjCtANb-CAF4wq2aDznGDdxD8lIfDf-36yb1rJJqTq-cHXW1TAejz085fq7erkh4WYyHv2nnQm8g7SFnVwVm5ziplVAHNQk070ZyVLMJy2p9MuoE1Ak9yxzvQBQ_jVsdKDTB4qBaI5dXsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=JgJZD_JyBrV7Bon5RP0V0pU4N6Eat7ZuApvTtsLAuZhK345s6r2KQzRJbRJXIq0KWo1QopxGrKMhaX3fY-d96-BGHn1N2Tk2G96hTjhZ5Og5SJVhs1PheBydbZw1qL915O6hotUHhur1Ue4A3S3v0fM8XKuErBN1KJkPwMjUtWlNtolyg1Z4C7rCFD0H1UaM-vV9i08wEFQwVMthobgytA62y3oeCccKIIvHosaXrq4RVnCSYVLn3KxXrTWIvskzGg-2kSrLXbeTFbhBQxogNtRbyN6cCokt9ISBKVP949xLvN6yZYU4yN_ky_VH1SOuZzxRR30W_6tSfGMB3PzjAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=JgJZD_JyBrV7Bon5RP0V0pU4N6Eat7ZuApvTtsLAuZhK345s6r2KQzRJbRJXIq0KWo1QopxGrKMhaX3fY-d96-BGHn1N2Tk2G96hTjhZ5Og5SJVhs1PheBydbZw1qL915O6hotUHhur1Ue4A3S3v0fM8XKuErBN1KJkPwMjUtWlNtolyg1Z4C7rCFD0H1UaM-vV9i08wEFQwVMthobgytA62y3oeCccKIIvHosaXrq4RVnCSYVLn3KxXrTWIvskzGg-2kSrLXbeTFbhBQxogNtRbyN6cCokt9ISBKVP949xLvN6yZYU4yN_ky_VH1SOuZzxRR30W_6tSfGMB3PzjAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gIVFpyRaAg4aBYArzwQPZas-FLTVGg4PD0q59ibfTscQ0HIqalpaZLGDn_WqRU2pSthfetXISull8y4v35zQqkUEkYgMHFipeTobt3K2zyGNmvajVvukN3LhKE-Lk05LZ016aaMWdvGi2K6QSScazQxb272aEQmiOgPq-tj3tcn7l0N-OFrmGlVPaFmuGPoExUA0kkUrTpy9Yhrr3jP-5p4aJRTmA_yd98xUfEbuJZtx0N2pHmJeYOQAmlTDog0j8X__-Lxh9MGXvcsZQtFihz-luWZCj0CcuYLRkEt_sDF8s8CRCaXs48DN80lgn0Bfk4dyvXu_Q3N0m-1xIDeDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YYvxXvaXM0FSuI0hhEsQb0x5qSXN0Sp1ukawITlEd_mcXXLC5jO_8L5WtqymDyi-TiNe7NDsxH3_nilNeRf-5znaGGmrF89Nl_r0prGygcWj0tHrUIaA1diyNfwMDtIKzfMcAd6SgD1uiSbdl8t4azHRVlHg8FCyJfxOr_XTVlFamvVsyJTG-oyJ9YCMKWSV7uaDXkr7kTGmRIKTy6cAUSvVczjoHJu5-7WWW0YhmO1lx102zLuIhJEHLvLCQo_cmazJpotR0r6tbygC-Mb90lMa1xY8KdlSC5PjNR98ENn0tB7J8SzsUaxfjxg-lPgtl7Nf_cnPGKMVyvpiJ1zdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UbNJI6I4qANH5eyh_LmcujaVXtfRWIYufqYjz3rL8ws-p8-YlcLXdYUO4GFxL188YIQP1wjoHl2sdJjXkESGYN7vetkrRTS7AQlgjFgt1f4o1C-gV6rqSYT-EOzWCgKsDCAoqYCyKaqguNLNsoLFHQd4i7DXkmK4-gKEUzAfVLVRR_e0jBHRGOHFVn_ybmtfs48x8xBzK0G4SO_czZQkFzDwHB1FmLGPPAUKfWNooqQAro7qg-_8MTKsJVFuLcwjYYF-FUY2MsHf96aFUh5wZmbHfSS-Plsmqn5-iuIv5TfQWWCraFU1K_G45Eo9p7HxSusXsvSmduC3b2VB98eG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RnMET8cz7pWh49Lv02h3pImyopRXO5gkB3Wrb-7QZ7hbSaPLodfuRFstUt5UuBafvhgYXio_g8pdx38RsS-PvN2U5GaoS93ZsPK-kloIL-ZgboY-_G83RYTHALvAl4XOxcFiocNRBlntW5rVJeCJMXHrmZ4SGXyG0Z_xSUk2u6mcpkfHeA1oFWwEb79jRi7Iz7VYpPo9RGipud1C7MAlpmWpQ9Y2yHdXFCFX5ENoUWriUjLWv2qu7_d9n81m75vzwpqwBdiXR-a0nV77iOdqjh9fAI0WEYlAYeW4jJyr06BoeRi4bLbvvbMXbwgIjhQOCRQmrAd_9rikKSWrSDxwdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZx2UaFJQDjjVKtJxAp4OSMUZrUniUWpeBmuG6U6Aa6Ci0bwic3uKNPK97lgkneiK_GFIWt6p67_NIjgRxxxFf1DpjWa3dV4XhNwjZCsHJtJM9USAN--nWlOx1XdxqVwW0u5eOE-4ncls39Ffqk_4u3mhLDBDGCd66-KQBGrYahmSa8yf06xjHlCG0HxLo3GOd5XZ1jHkGvlhGu3D6aVDL02LCILyovZqnIzqtURPjcnqStTgm23WdUwebUY19kSYJA2E1bLueQfhwPV6GnGLlc5StUJemOHx9jHmJXKxSC4kj29TXr9QorRVjUapV8iulZnbtXdyaul8uH9BhKoVRGl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZx2UaFJQDjjVKtJxAp4OSMUZrUniUWpeBmuG6U6Aa6Ci0bwic3uKNPK97lgkneiK_GFIWt6p67_NIjgRxxxFf1DpjWa3dV4XhNwjZCsHJtJM9USAN--nWlOx1XdxqVwW0u5eOE-4ncls39Ffqk_4u3mhLDBDGCd66-KQBGrYahmSa8yf06xjHlCG0HxLo3GOd5XZ1jHkGvlhGu3D6aVDL02LCILyovZqnIzqtURPjcnqStTgm23WdUwebUY19kSYJA2E1bLueQfhwPV6GnGLlc5StUJemOHx9jHmJXKxSC4kj29TXr9QorRVjUapV8iulZnbtXdyaul8uH9BhKoVRGl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=P0Ch8nBfxU-3LWhcQuVDVyQxUabu_1Ms3xaq5t3RCm2zvnJFis8Pl8nNNTjYUKkWhSYGDN_vkl3R5qeaH4k0QWFwtvfmMauoF5DDap9ul62HBeH5poN6afdYGfKZfXCRh-VCOjMGD79S8f_Brw0hUPodD7yXcI7oIyVtphUG4iAeUmxpWsEPWLitRs6FuRitOZi7kq90NCZPm_ngH9rJsQVY4xiUjmsC1M3LiuVKHDLRdq3qVWU4oKWD8l-ZGzWsvCyiE6yYe2BFei_MJ8NTyhzd7EasyO-RGytKWFD0t7CsYO9-thDbCkae2YjbqB73sk41JS6Q4meP_-2EZJZumw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=P0Ch8nBfxU-3LWhcQuVDVyQxUabu_1Ms3xaq5t3RCm2zvnJFis8Pl8nNNTjYUKkWhSYGDN_vkl3R5qeaH4k0QWFwtvfmMauoF5DDap9ul62HBeH5poN6afdYGfKZfXCRh-VCOjMGD79S8f_Brw0hUPodD7yXcI7oIyVtphUG4iAeUmxpWsEPWLitRs6FuRitOZi7kq90NCZPm_ngH9rJsQVY4xiUjmsC1M3LiuVKHDLRdq3qVWU4oKWD8l-ZGzWsvCyiE6yYe2BFei_MJ8NTyhzd7EasyO-RGytKWFD0t7CsYO9-thDbCkae2YjbqB73sk41JS6Q4meP_-2EZJZumw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CZHaS7iRxn00udP-oyJKVKaDGQP_gCMA2n3bwFxdLB5yPZZWT4XWa1awRl-avYO0Vp0ZeaddXB8zyG7SXoqLH1ximYO2Xt8QxOZLTdNQa_2ILE8IV6Ak0-EGwWgmCIuIcnkZRUVV6VEegNF1IFJIvbWnEfWATarjo8EDiVLLGLHm4HDxj1egYq4NKQwpZNMkcea0FGtYPkfMkoWr6Y8kgX8jjyLHhk-bYIpYZTLWuWxzeTFYzA8SGrlnyhCsaBxOO_JGJLDj0emHgG6YF5WH9ha5oAN83xcMGVEumFnrbPIu0soGnQjwddGGtTU_5ejIgtR89nXFdYjVdK-7WfBM7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nVNNX4NDzf9RofTFKESKaiz6rxr6kjsniCQqFkF7AGuQ4k09YHsxcMZRRrkLbaJnfMNYQTKrEAUYFbTMtq-BWfDRM2ZhcFuv3sHiyoAHeGTUYN_riwKCOhNI5qR1Z8Ef-fB17wDKy4HwHgJcl4GivTD_Xkl8T4tEgYAKXWy-l9OEtWaIj9_wI_rUp_tIBBMT4ZLT3fARdLIm6JtfTCxXBGnzMX8mv4W4v-MK206FM_hQzFx3cY3vAHCluuP0D0btGVwV5mNSSqfBzo_jXokuocR7i5lNTqfvWdCarA68kVqZBOMhQ4Os9m3uu_mX2WlGb-1sXJpGMJfNYTC_otHtJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKbZBQ9aohQbVbpp5PzTmFgThYlPgCAz859qJg5xJYxM6dMNCO219Kc-hFQHC7czv_DRUCjSZqf9yQZU0ZXHEW2rB_9tWUMTkgVIvysTHt6KvVZYDBep3LVrJ0fM-Mafml5N4AuS6eswtKSnmgREYfN4Y3nW5abQfxbfVeFIEXyToNmmzjtzX2SDP3Z-S2Ounth_UuNjU22wV22URSlX_gKc-RAfHjDwetqis3MranMJVg895RoPF_SZe7g1AovgRO7ABF75EBp1Cl_MU0-VqowajVd7_Jt2eAdC2wbyJpWcbm6oOzU8Jmdyi03RRMvjhh7ByQlmzIhnheMtER97sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWNBHD_3yG6Q9msH9vtdMfrAWB2XV414OZOLdNZ5j-VE--jgrEjfPMt0WxWBEzwKsFeyWVkBRY05L4fA96sy-Wc01U1P4012US8y-lwDEYplCPL79NrGMJNQ2bHq9iCzHQDWzWdADdUBZZQ6DSAV1R8tBFB8s_lB1a0tmtjihDRpWp79xJNCLLiDFkmvfudRVO9muahE1qhLHZRfOSN_RoMLFnf62_jG6gePIlxRRib2AsMh3YwQ2r-vxNceqoLr_drQqk1SzFNYmXtxKWOOjHmmINVIVQM_Je9DFvOluSCkC3jIPb7q6ad1HlzM72BTGPCK42szOxFAEhmAnsywBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd5lw2Xal2NL0CEibjfkVvSqVVlrDcPs-pgDqc8UETr9H_qWa85ltPl1tWijExFMJUa5s9gY2fAjYGLzmj4sOrDGebGD5MVo60UNpdssefm26xBPVQN0NJ9dbyS0WvmxAZ80P5hT9JCCs6tA2naKvkdzAoymgrgSRwivvXVNMqAf0THxVS9mRDzXrwozLckOWi97O4DLn4KGpTlWc3VGINHi9SPENKoA4dC8QKtP782NakJSfsWNb9gh8X7KsI4ByukDW9meGpazuNXjRuZGfDgGWpcarS45bNgNgLi9Tp-zUzPFN65kd6SZW1GEAnVj36bOwIuRipgyKIC9b7fUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TKIBOJJuC7cz75QcDrIptQ3ec3KaKVSJmSubiFj-BME-MVD6UWZGNfeEE9TnhMR8QfGJL8kjfC_JNiLqhhJtxfYJNjACT06O_Rbue9CeYgK7_6y3RnVJH6j6rN_1Orxl1NhxEeBPLZOMW03-4hWQ0E4PEY3BQmcUs1P_CO261NIVuZi1Kgl3P5REjoh_p9RcMj4w_SFBIzh5ByOdm66GX0o9UFkNlbBKe8kTi1Yw62f4ewtG39koCGNl6P3S6jZVU6-OyGA6CXiXf9EAru7Wimmv2o04dF5Cb4krKtS-nfMpYBztb64Pqu-KMW3jatZzw7VeOXtLhFF3K52Poj8wXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1V_O7Y93yxTYr59KcTii9_RcLlbIGrVwdmUwQOKMens6NbuaeWGauCvQPRFpGO8opiIPDijU2JGW2sG02K3-L92OR30OwRviHip2BXV96VtNyZ5oIKhwuxVbIoZ9fSNxi0ylPKg5LhpuHMdjzNJ2o7BQZIVYkFMMUsiDeJagurdb1xbmJGm9i0wL3I1VzsO_pKJxlOmL4moaC5ThPGv3ZaOgyv8BGhd2AILxMCjeqAGbwdgo0e_SQpw01zcYFXqdQZzMnH0cxqCWsK5xWhaCy5378Vmq_sruT1RZSXP09BN0AXF3fZBBJaoqg1gHXifiFLIaEJQFL5KXqdjaMCiIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dvXwpX_ht5DOu2Q_9Zu5C68tTiyAWPQhlL904nyG3FC80wU15APkTyGBxLDsqW9s15GrHfODSZWVqdBbToO6KsV9IjHGafTlU1gSyelU_fAbt3lufkqAZmiVCybg55qpDy1SCvwGni47qyk-84xDrpurJosxX7uifFMSFmFUVmzIMxww2s0ZME_Zq5EBilnIXs-29sz6zqIor44OK6vRYQJLO0eYNfAAL7Q_Vxr3sM8TkJNS36LQfyIYUPTBxsaY92dIm9vgsQ3Fr5rcpF-2QMM6cDvQ9LBtJGihVwsCt6AGK97xFhsejxwJ_Z3vFLToSQFfaLEg63mW5skyIMI6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=DZMZZN-mdotLw3FGmwjitM-sLQtm-knfJyQms6eQwx2-Cr7GP8A294KiTuFZbtCk3x1KI12_pPuMkosJvzBz4cMCSB4uz9kmwv_TIWhCgidfLjKvtQUTg7A4X--IHbkikdV3fL48utacPAbUVhH-XGxtSsoTAO8L0VCxlRmxTVJfXr2-cAkkMFd1F2PO1KYJNl1oJO5lV_AdFO9m2ivhWylOonupBTIyyamOeat8hW0QLHOuPwEhZXsHn9AHGI4Oxcvl1q3kr8sPAoeBLFCaeO0roVQwRy6riLPOwWr7fKDK1JBg05xRaJ5O6n92vCtzdALMJqW0eBoea0ED03_zIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=DZMZZN-mdotLw3FGmwjitM-sLQtm-knfJyQms6eQwx2-Cr7GP8A294KiTuFZbtCk3x1KI12_pPuMkosJvzBz4cMCSB4uz9kmwv_TIWhCgidfLjKvtQUTg7A4X--IHbkikdV3fL48utacPAbUVhH-XGxtSsoTAO8L0VCxlRmxTVJfXr2-cAkkMFd1F2PO1KYJNl1oJO5lV_AdFO9m2ivhWylOonupBTIyyamOeat8hW0QLHOuPwEhZXsHn9AHGI4Oxcvl1q3kr8sPAoeBLFCaeO0roVQwRy6riLPOwWr7fKDK1JBg05xRaJ5O6n92vCtzdALMJqW0eBoea0ED03_zIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rww_gnYnq1vTL1i0CczM_sT0LVw8p5hCAwIDVAKpkK_IHuLSiurkIdfaw0Z9BjR6X4CJqHFYp6Y-7pB9BVypYx8yTZ8PQS0B2siT3IhDeuk7PTK7zVOk-NbPU8IjDiynnGWk5U2W99GN2f4QS0G6yGhImE3lMcrBu2aWUCL315yxeh8vJ7x5Onur_l0qhs211SqMCE8WFY4UY6IeYrecULbq1tPu_Nx5jbZv4iSsh6lOsVCcHqEz7j59oA4TDR9TTBvakksQXEg_9Q7MPFawCfS_CTR2JfaLjXjGwpAItwupn-ClIN7hxRHT8xKqP_pLGcLcwjoBeaKHuAOeNH3zgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g-A2LD2OVZ-gjfo2D7BsBuTaV9JoQ1hhzpEmFVQuBi3R2yy3dNZgqss_x8V3g073rnq7vJfjXeHwOHUYKrDy9usHVyhsLmQeelNizWiFlS7JjTlH4c7QrX9oH72HuA8Ik2Bue3Q_YMdpKlMl3TKjQH6uMRnE0ipbKYoegdsh9iJYxDclr6Kem8kT07zICnwikeVQorGAmsWKGkwYv6YHLC9v8VOImET9P4AhrIdbrCKyLPTVi2GeYVgVq1xvLhQGbww8d1E1oVmGP6CkBRP6sngss63QDe_cUYbc6gOCjOYu4I2N9SOHH3cMUSRZKC_bt9jHk-OLCtuoW-jLzcr3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZFiXuiK7KxpnKKjzXPK60pVvx6MKUwOgxWQ-GyADArmd3_FsBNgONisMRjqneAzhIwDRq4Ph5hA6E5Bkaow3kGzVTazfhlIzoNvm6sjurZHjbZveUtjp5K7qb8CLt46t21DOiWBwBWeeh_as4CJ5qHmaXa6b9dUuaQZLOth6NC0J6k7uIIGUCQdxjg20X7DZsZUlMev34QN0OifIBCNgM1W9Sc7oIAlEeaZv6XJ-QkPbXUC1HCl9H-tqQoaeBLFoLzfSgQs5yh458ekjAMT1lcEz6R9YDWXSZN2gSBpOd5FNDe2foLaD0ryHX9-fD_fSVC7vrohUQiU239vnbEuVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LlBvqreGLI4Gz0mGjielGL1r0j7hu999i2AgNxCJaPEaPoYefNT5frtETVsvNQpW-RRsFeGQLJVI995yti1LLa_5F7L-6ACxOE5olq6PZNCsPGwEofR1v_V-zPcxmKD-f5buw2t2Y507uR1ZTjiSYDQ6mg8c1lA40ef2hfd8fi1BwOG2WFFiaVfIBB_sK3kH5tkwRa-jOI7VhTNJfzG6m0yyKSpV0dQ6zYWmOWLSgnmnyJiQ0C7HFx6B0KJhNVn04bJSDImYTGXBB0WGxK2mm8Zrc2Q5VH4y0zra0Kwm8mYxyLj0cUeyS8Lr08SgM4zfnGvbfkSY1071BWyG1-8B0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=QNHhLCh2C45CY32BWbLihq-YG4jWU_IRNGUswvnojbHx8BS_pvfRp0Oy0DX76LnJrWLo0pkZzanMOh_lxhVaX-HWl0cNeKdbKim61qkXCQpe0YUGZ7qE_Axl5mWODeDwJJT0UBEDDw3NehQxaUWHxdtDGTLH2qf1VmTJZF409EMmuuvgXC8DgiwM_Ah2GTBIJAgnRzEBSYctj10l5QMATYQ5xfWBp97ggyLKDVVYEqXzhakxYSPNu6IjbG9sTH9NWB-jbSyiYi8zhHoYqQrE-xPn2XtZiziRryABuMVt_FlqoCn1j2Na-Wkr3EMsnrMrskIWg9QtpQGWFd7UfYFbAg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=QNHhLCh2C45CY32BWbLihq-YG4jWU_IRNGUswvnojbHx8BS_pvfRp0Oy0DX76LnJrWLo0pkZzanMOh_lxhVaX-HWl0cNeKdbKim61qkXCQpe0YUGZ7qE_Axl5mWODeDwJJT0UBEDDw3NehQxaUWHxdtDGTLH2qf1VmTJZF409EMmuuvgXC8DgiwM_Ah2GTBIJAgnRzEBSYctj10l5QMATYQ5xfWBp97ggyLKDVVYEqXzhakxYSPNu6IjbG9sTH9NWB-jbSyiYi8zhHoYqQrE-xPn2XtZiziRryABuMVt_FlqoCn1j2Na-Wkr3EMsnrMrskIWg9QtpQGWFd7UfYFbAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1-boSBBAcy4XWJiIi1axrm-HsoCCEyzSbqwnB1L3UPASnQtjA6SsnfLkBo5hpah6DgwvcjW1jfTwF5J1k1hqDIXPyHb2fXerLLErPH_-EQrsesCHCEdB8epDDtW-jqcCSTyZ4vuTMsVCrBDq-SwJ4jm4KhDpeS1jxYs5ntrpTo_ytWRiy-kOcHjI6BhD_SROffOL9_CM-hMbPwppiMoRSZTtTP71p6jvYtYsySjCdBLGNq3luRRRufiuV-C_ZrRSZAIjqrkrgCohxW4fiKSiBAl7lQNMYY-3HSQYGgwCX5yEJmP3FQbvVUDU2GxDvxpT4cP-Jxmp5hSLxIHb1paaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=YymMLtmbp7iUeXAs1geXAEKGTcFdeOFy0Y0QMevTQTdAX7zFu7-7BY7QWuuY1MUA-t-8baoe0h74AnNhpJn-wlEpNOCFVEJLEgM0IXcfx6_5LaJKiAiRhDiarSVPEdrQr-ob0-c66sJDNyDqdfNMeuuJFV4KhY1Pp9vTrM6ZzC7f0sep4d21rbe3QaD_LLKjMT3lbQhLomkIG-yaRv3kjOmWGCuy_wZO2L6z1X9v6vjzi5JRIJkaKL95hSZFhQhH2tAFHPcYHaMx9U_hYnYYZBQP-XCmwhEGfvJyjPdZpmxzU-WLxyF-yNQ0uH3FeKFR6qmSETIja-i0KmafCsZdOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=YymMLtmbp7iUeXAs1geXAEKGTcFdeOFy0Y0QMevTQTdAX7zFu7-7BY7QWuuY1MUA-t-8baoe0h74AnNhpJn-wlEpNOCFVEJLEgM0IXcfx6_5LaJKiAiRhDiarSVPEdrQr-ob0-c66sJDNyDqdfNMeuuJFV4KhY1Pp9vTrM6ZzC7f0sep4d21rbe3QaD_LLKjMT3lbQhLomkIG-yaRv3kjOmWGCuy_wZO2L6z1X9v6vjzi5JRIJkaKL95hSZFhQhH2tAFHPcYHaMx9U_hYnYYZBQP-XCmwhEGfvJyjPdZpmxzU-WLxyF-yNQ0uH3FeKFR6qmSETIja-i0KmafCsZdOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
