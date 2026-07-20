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
<img src="https://cdn4.telesco.pe/file/muQNAevQnzCpyE6TwLUaFcwc77yvDswawaAvRoEzAL3HdtvFRZScQv13OhImWgsuf5x0mwx-UzPHflXzdcvU8nPHxIIWyMd2SG96HhcbUDIYKAedV1F1PpoAZd3Tm88smepCgW_NMPlxOo7KV1pjtDvQ9nZQbGB5ehnxS909mhc2Kq72TtqHLMnpt9CvMAPJLsAagcqsHsbpswbcjUZ9w0yRBZP98hn01ev_RVhD6fWZO5F2eYK7azai4gWO_TYkQtNRMh_yNta26tRTLNxNE0CeOr67MEFXL67RA8Av3R_QDN-UhhjZeJyhDh2Rcws2L6OGgmRPm54QcY4dWRAIwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 16:52:31</div>
<hr>

<div class="tg-post" id="msg-136040">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flaH2AZ7EkZv71Luwy55y9BZVUB6PbuCEzqTW41EcbzFjJPDZUPSW3qBXVqnXR8-T6kuBXGqVnHAjEbpYLAlDOuPLJdSV4FRgvv4rLbxhZswlrYwD6is-uhj0Hd-Z4fXzv2tixOaRHPUIvUe8APtv9nRf6O6HbuKdkH5gTLqkehAubcTZmzHQ9sFaHStXp3fSETsv-CSUyvns7uI0YOKbzDA8BGaWW8GxsJiI6z_BP5P4qlTfdBmfToFMjQabxuNsZipu1BB-FAm5YmHy7FZkko8isJWASJG9rYzal6zJJSPrlfTlqsW3MEBtqpUHylkJaAHOzrNzHFqiZ64syJ9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستوان یکم تایلر جیمز فیهان، ۲۵ ساله، اهل اوا بیچ، هاوایی، به عنوان یکی از سربازانی که روز شنبه در اردن کشته شدند، شناسایی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/alonews/136040" target="_blank">📅 16:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136039">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/empD6fwNIFBlAOvVtsFcwArV6wdbR41fpbHDJ39-n-9PuHjKQ4SUgSztE-PDl6K-r4fWBS4CNANl9avgf2kSHqphu_wQ4I2ReXeHsIBcnEQV5IWXtYOLasfaFOa8Ma1jrXD9Us4WfyFeDH8heskX5ElQmctfMuNh1YOlZbtO1VupuMIgE8Jx-p7N1gwU_Q1cb5FoudMOOT5WgB6HFMGpdHaJhHLr14zfUUl_UjhbVbEpAyo_5jE0Vo--GJE6OWgFOhjSvKfQXeqcN53qed0fG3XblY_sNxv7J_nPZrpWZGGSZCSa2Mt_xU7T7zzpYLlYQqfWNZWRo9B3pMFMD35T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی: حملات آمریکا نباید متوقف بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/136039" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136038">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4x59ofCjLQkoK2Xy2mGZvitIjkTj3wte7T23dvfDRASNceRxX8dyimPBoslZjQsQi7g6zNkuy7p_vA5v87v2VI2SzbCOM5xvC5DGeEDsN8ircxKG8SQ85WFr_1lMF1mW0IEUhz1YAOpRmu0xVlO-I6DY7o02MehB3NDH9YbQxraxCNt_KZe0-R2xj00O96nTNFbLFojtf5RCvPqUCELW3kfU-oqzImuRPseZ55e1xm_jaFwZIggbTj5xvYf_H4UzBWT8szqFHpWjJ5-HbVjg9LoEkuxA4wh6moucUVJijghsSs_xoCQtCQcvq1csqEJJMBZw8-VnagfDwz00xqktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از سرباز آمریکایی ۱۹ ساله که در حمله ایران به اردن کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/136038" target="_blank">📅 16:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136037">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldp_dMZ0DPYn9UuxTLcPau43zKzQQvqOTOlrqBSVgwarmQm3qwbvEKIEHwYhEdRMW4KaB8huNGdCcuaZl0J7xZBvCkEAkW4tt6l0WlE8x5EWCTbs5SNZ1FjX7MMs3lcanXxBYFnKHyo2TT36Flci6S8YE_K2Jvba2e33I4I1jxUwrkPBd-_XLzBuhszTzEmMFPjqfeKdOqj3B8MpEQfAn0zycQjfXzjLM-hho5HpgTwjmaRIomoYrH9566cKixxEesBu1dFmrA-OH7m1coYoCGCRkjKIFCOWBmAT_7CI3jTIqswZetYtoB86yATJYwBzyHYx5zOLqCQPnxKuc_FWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت معاملات آتی نفت همچنان در حال کاهش است و قیمت نفت برنت از مرز 87 دلار به ازای هر بشکه پایین‌تر رفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/136037" target="_blank">📅 16:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136036">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/136036" target="_blank">📅 16:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136035">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏
👈
فرماندهی کل سپاه: با همه وجود، هم‌صدا با ملت بزرگ ایران، فریاد «لبیک یا خامنه‌ای» را از ژرفای جان سر می‌دهیم
🔴
ما سبزپوشان حریم ولایت در سپاه پاسداران انقلاب اسلامی، پیام حضرت‌عالی را فرمانی نافذ، میثاقی الهی و نقشه راهی روشن برای استمرار رسالت دفاع از عزت و استقلال کشور می‌دانیم و با همه وجود، هم‌صدا با ملت بزرگ ایران، فریاد «لبیک یا خامنه‌ای» را از ژرفای جان سر می‌دهیم.
🔴
میثاق می بندیم که پیوسته امنیت، استقلال، عزت و پیشرفت این ملت را ستون‌های ایمان، توکل، خوداتکایی، اقتدار ملی و تبعیت از ولایت پاسدار باشیم و هرگز سرنوشت این سرزمین را به وعده دشمنی کودک‌کش که کارنامه او آکنده از عهدشکنی، فریب و کینه با ملت ایران است، گره نزنیم. تجربه‌های بزرگ این ملت، ایمان ما را به این حقیقت راسخ‌تر ساخته است که راه عزت، از مسیر مقاومت، هوشیاری و اقتدار می‌گذرد.
🔴
فرمان حکیمانه حضرت‌عالی را نصب‌العین قرار داده‌ایم و اینک که آمریکای جنایتکار بار دیگر راه خطا، تجاوز و ماجراجویی را برگزیده است بر این میثاق استواریم که ، «درس فراموش‌نشدنی» را که نوید آن را فرمودید، با قدرت، قاطعیت، حکمت و اقتدار به او خواهیم آموخت؛ درسی که هر متجاوزی را از تکرار خطا بازدارد، هر طمع‌ورزی را در هم بشکند و حقیقت اراده شکست‌ناپذیر ملت ایران را در حافظه تاریخ و ثبت کند و مسیر حکومت جهانی مستضعفان را هموار سازد.
🔴
در اجرای تأکید حضرت‌عالی بر حفظ وحدت و انسجام ملی سپاه پاسداران انقلاب اسلامی در کنار سایر نیروهای مسلح، صیانت از همدلی ملت، استحکام جبهه داخلی، پاسداری از سرمایه اجتماعی انقلاب و جلوگیری از هرگونه رخنه دشمن در صفوف به‌هم‌پیوسته مردم و نظام اسلامی را از مهمترین وظایف در منشور پاسداری از انقلاب می‌شمارد و بر این باور است که اقتدار دفاعی، در پرتو وحدت ملی، استوار و نافذ خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/136035" target="_blank">📅 16:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136034">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری/آژیر حمله موشکی در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/136034" target="_blank">📅 16:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136033">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gwq__qZVu1YIhAXeJEA97tE9QwYyE7Pl7fZkp5GyoFEzSrjK5-5bibACLaS9ZKMPHVChwKtsJlDlQuCgbsWu0g76-4D-UYBkdhuJAyBvWEsnF-3IyfPqyOARDykrridNEcbEF6bUX-pATkG42CpiKQz9SazPibxWtm3ONYW3-LED0BpgQKGSyIn0FXILboEN9RzWZbAXqZoiRyzApoeJownuQOjHN2QY256Fi44LPqNxCEHuplGEhx2nFxWEDsdmH4JJJJ9NBnA9NZrZEpiwEwnoW81Sdru5iZGILSru-9V9CUOJXyef4YdRAms0bYAH4Twf-1rO-PB6H0SORUJpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری تند حامد لک علیه بیرانوند
@AloSport</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/136033" target="_blank">📅 16:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136032">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYMncsJXheDGBy9rFU-tyuO5W7t68C9trAjcfPMLKRu4vQ9nFMQzVjuM4bm4aomX94EJrleK2pAtVswhxu4QZzGPN9VhtkvRA-LZ_Fqa5Yfmj1FcPXQzc2_sp9Ry4r-2-GO2nDDqSshw9v0le9an-N7f4_uJp0gj1QNspO5IvJTBvSPiv659rEDQM-fum5THYOhXZVM1E2Pxu2tdUkp-mbqtLG-V7Mz3rr5myv7iw68k8jp7v_p78XAmW4MDGpvdPljHrvWUVSMf9-NZ_L5saTdiNdFLj5mEnK_juYbs9VhyBKCYvYfaxvQ8RTBVztsQ1kvASEHXFytMGmkzggcnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلمب تعدادی از کافه رستوران‌های خیابان‌های سنایی و ایرانشهر در تهران
🔴
از صبح امروز تعدادی از کافه رستوران‌ های خیابان‌های سنایی و ایرانشهر در تهران پلمب شدند.
🔴
جو کافه، ۱۴۰۱، سام کافه، دو بار، نووک و تئوری از جمله مجموعه‌هایی هستند که تعطیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/136032" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136030">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مارکو روبیو ساعاتی قبل : ایران کشوری بسیار غنی و با پتانسیل بالایی است اما حکومت آنها علاقه زیادی به حمایت از گروه های تروریستی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/136030" target="_blank">📅 16:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136029">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEMwaPhazZ6hesxqbFIhM2e8RUedFxviywVnZqytbuwLeY0BbSl0rZaTeh06akBpZX713txW6vBhg7ZC8wSnMdlZ7SIDe1M2BVbWRctYd2dPGBvfSdw7dnh1bqJWZCzrXRnR3TXsXaGbG6llfaPgcOXmpLrKrvgzbmdXkqwohi6jfUV0hVPfVdCAXttiQOMTGHNV2sYHoNsj5yOaaEneWv1_b7Y5KyMyRjZ_U6ooYHjXX8YkO69TRegiB40vkEDWGwLoYpJ82rw4ZIZG7AjlPyCWWikIUuGMUdci9nDy_sF_Ek6KAOQHAIZQiPAyxTjvu5cQE6YJgvj8UAvXpZfPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیلی‌بست: ترامپ بالاخره مجبور شد اعتراف کند که هواپیمای ۴۰۰ میلیون دلاری که قطر برای استفاده به عنوان ایر فورس وان به او داده است، به اندازه مدل‌های قدیمی‌تری که بارها از آنها انتقاد کرده بود، امن نیست
🔴
️پیش از این وزارت دادگستری آمریکا دو خبرنگار نیویورک‌تایمز را به خاطر افشای این موضوع، احضار کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/136029" target="_blank">📅 16:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136028">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
دلار تا کجا میریزه؟
این تحلیل عجیب رو بخون
😳
/
کلیک کنید</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/136028" target="_blank">📅 16:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlS1bds-lvJ65hvcMTSp_g538xPUgjSvNBdwUv5f4HdV_P1zZrVPrKbdlSYLPxYSzNMzeaAEUHGq4eyG1iAbFDBZYInEinIwLw19SeZjauoCPTHQ_v4NJR4Bm_vK9mryN6TXDTY0wvRy5iK8c6b-O653kS82u2Z5vpucK7lHhDa5cDBAlmPeK1a4twOiVvitehChNl2jEiZeGnkuusX3IGN7oKRxSgulEEFkaIwQEasEnZfjfn1FIpF3pdfoIZ_fRB2OXhFRO34nPDR2edVtQd14TVIT3bFAbVSyT-S-luQFHKEHBmr9mqgvYauNbEO1X12GUAi1C9YeUgEr1quXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه: پس از آنکه ایران اعلام کرد به دنبال ازسرگیری مذاکرات با آمریکا است، قیمت نفت برنت و نفت خام آمریکا کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/136027" target="_blank">📅 16:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
دلار در بازار آزاد تهران: 188,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/136026" target="_blank">📅 15:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136024">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Kv10zWldvzx3uPp03QQd-HbCnCFNbcvzx7B4JrsYCv-qvpD7YJYP3sqISGWMwMLX6Gqja__GzzcSJ4xTT7vH-ECJpFYVI9NVR9bm4LTzhmS1pJDXN3si80x5CLpYKyBk4DIS4z8EtySKcezPQmkmR_JZ6vO-w0U_jT9mwWZ8fHWCklHHZ1MzWtfdCiUYDuQRrvWPzGgsgFZpcQSq8oyZm0uvThtlIw27uByLE1ypt48cS8kBxi2OuGRvisOw9uWzGFqWwwWIGItKUbiTySx_sxzeGEFMSdilVMjnhlEOOfPVSG4BMj4DNy8D1s8yTAvLWcFkqmhFnimg1t53raqpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/txjBB87yTIKBd9kWAkAgBE78UaZG0xHeOgPjoJ-k78Df9i-a8lm-MszIn8ISmRT7tEFrz6B8EKy6U1t60uZLAdxJHcVToUgQH26J5JFeR6x9WBUCTX-lfpl0z9-J0fwXkzXcM0J2aDVAJuqYmlwYAUr8biJdCDy42McHfiLW7hyYbWTjvm1cQHBTCO5aGMnFOZ6AVftk7lRF3gK23cVNEAsy5mV_7VBllCxx_faHOSggS8vkkPc5DaUSZruD7ThdEepBomNqit0MC344_90t55uG2sqYVxO_h95MWgNrA9IzaeNQduSlgf5Ad1KuKaEMSyU3vQspW4QVH8pS8NtHng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
داده‌های تصویری افزایش چشمگیر فعالیت پهپادهای شناسایی اسرائیل بر فراز لبنان، به‌ویژه جنوب این کشور و ضاحیه جنوبی بیروت را تأیید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136024" target="_blank">📅 15:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136023">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0efe0662e9.mp4?token=Zi98If2CSQEnF9WL5pSaTerHTtIuOCe2oZVBELOfrbnUVzCgmXRas43Ou3qX8pW4ieHZabBDiN9AQQ6MF3MS7qZNRaYYDvelanJ5_r03nQ7OeegZ68qe6DNlkCKh9dtpjlCZTQ6G_js4769aNMs7efQ3nvv_sfQQ333yTGJXT065L1JqOFWZdXrLrvIvMDH-z5zbnzkGsn6TgPcBrxFUqB0x3WiX-ukhGnKvUKNCuZXSUmKh8QCqiKiYUg38RppPimvBa0inpUTNiePKzNbhrWIJdCpt5-bjQP9CAK4FbjsRxofizkGDarHCJN3TjszRgXzoevr2LOYGYFM5mu7895RkrTvD6dIHYyg5MlH0okNn6l3liVqWg0V1FBr2W6IDwpZPxFEpdcZWoovfHAYag5UGp4rFNsvN5-Rf6kgz3czMmNbFQPnTkvybtrEOCBoYs1eNYeitROnvXhGu5dpHIhCQ3doJ0rzUiV8xUjJmHxZHjxH5Ewy44KXpNGlkzSjaZ-d78mZJD31INdx8rVHrGsFy25eazx38CzAZewdrTOd5Pc6aLNt6PTOhv_hhOAY7zw67RMYaEKzqKdFLveu4ZhHVeANu8gfIKihDTUhcqM1WoTFZc-hpSqFrIWAJbWI2m-T0uwzoISpNWXRtu0qYjL10bTenFrcOHISHdtD4tSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0efe0662e9.mp4?token=Zi98If2CSQEnF9WL5pSaTerHTtIuOCe2oZVBELOfrbnUVzCgmXRas43Ou3qX8pW4ieHZabBDiN9AQQ6MF3MS7qZNRaYYDvelanJ5_r03nQ7OeegZ68qe6DNlkCKh9dtpjlCZTQ6G_js4769aNMs7efQ3nvv_sfQQ333yTGJXT065L1JqOFWZdXrLrvIvMDH-z5zbnzkGsn6TgPcBrxFUqB0x3WiX-ukhGnKvUKNCuZXSUmKh8QCqiKiYUg38RppPimvBa0inpUTNiePKzNbhrWIJdCpt5-bjQP9CAK4FbjsRxofizkGDarHCJN3TjszRgXzoevr2LOYGYFM5mu7895RkrTvD6dIHYyg5MlH0okNn6l3liVqWg0V1FBr2W6IDwpZPxFEpdcZWoovfHAYag5UGp4rFNsvN5-Rf6kgz3czMmNbFQPnTkvybtrEOCBoYs1eNYeitROnvXhGu5dpHIhCQ3doJ0rzUiV8xUjJmHxZHjxH5Ewy44KXpNGlkzSjaZ-d78mZJD31INdx8rVHrGsFy25eazx38CzAZewdrTOd5Pc6aLNt6PTOhv_hhOAY7zw67RMYaEKzqKdFLveu4ZhHVeANu8gfIKihDTUhcqM1WoTFZc-hpSqFrIWAJbWI2m-T0uwzoISpNWXRtu0qYjL10bTenFrcOHISHdtD4tSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی ها (انصارالله) اعلام کرد که به عنوان پاسخی به محاصره و حملات انجام شده توسط ائتلاف تحت رهبری عربستان سعودی، فورا یک تحریم دریایی علیه این کشور اعمال خواهد کرد.
🔴
جنبش حوثی همچنین هشدار داد که هرگونه تشدید تنش بیشتر از سوی عربستان سعودی، با یک واکنش "جامع و قاطع" مواجه خواهد شد، و در عین حال خواستار بسیج سراسری شد و از حامیان خود خواست تا برای تمامی سناریوهای ممکن آماده شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136023" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136022">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206a60f2dc.mp4?token=NKEr3EFTt9dFj8r2MUg4WoK3tcBD2cW6_D08fu1rRDSxOW8qeHw8wgu6dQAXVFZbfkV4pPY1gMhTxLi6BOLc12BUtbOphANfCOvqmzEzNsiXhCKzV704jZVMsdboYoxdxUMz81tzcE_NXaQ0d-Lfczb2hdvaq9Ew-LUXp6k-ApEnUMO12H7CQJYfKArWQuMs7XzMukMkCugikbNjxBDqofTGFDHgFVbzKta-H9dON4Ud9rhH7PAkpkrcInSuNRZ4JIQCttVIO3FhfVk8N18V9mXs_xU2Wso16RvA9HpH_Tpc_ppqkJmAtLuadGgmUXdKnVvS_ktVb8r_9yBcOEGcbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206a60f2dc.mp4?token=NKEr3EFTt9dFj8r2MUg4WoK3tcBD2cW6_D08fu1rRDSxOW8qeHw8wgu6dQAXVFZbfkV4pPY1gMhTxLi6BOLc12BUtbOphANfCOvqmzEzNsiXhCKzV704jZVMsdboYoxdxUMz81tzcE_NXaQ0d-Lfczb2hdvaq9Ew-LUXp6k-ApEnUMO12H7CQJYfKArWQuMs7XzMukMkCugikbNjxBDqofTGFDHgFVbzKta-H9dON4Ud9rhH7PAkpkrcInSuNRZ4JIQCttVIO3FhfVk8N18V9mXs_xU2Wso16RvA9HpH_Tpc_ppqkJmAtLuadGgmUXdKnVvS_ktVb8r_9yBcOEGcbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / نیروهای مسلح یمن محاصره دریایی علیه عربستان سعودی اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136022" target="_blank">📅 15:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136021">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
حوثی‌ها از هوادارانشون خواستن برای همه سناریوها آماده باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/136021" target="_blank">📅 15:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136020">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع آگاه: پیشنهاد آتش‌بس و بازگشایی تنگه هرمز به مدت ۱۰ روز تا دو هفته، هم‌اکنون در دست بررسی و بحث است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136020" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136019">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
شمار مصدومان زلزلهٔ کرمانشاه به ۱۰ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136019" target="_blank">📅 15:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136018">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سخنگوی ارتش: جنگ تا دست‌یابی به بازدارندگی کامل ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136018" target="_blank">📅 15:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136017">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_Q9CenPnn1PsoIOkaQEYWAHmjmZp2ejvFXSasdSVir8BpbzrDHshjuq5K0B6sDGFD-7ujV0pXe690cAa_PQPlmtq1sFyaNtSbpoO8GZy2CRgJxBDoPtvx6qYvnyLZ7ZVBkZ-HQnzWv7S97YRD3rjndzgEA2Zycm_LYv6DOALjvRuHvAgkReAmQOWyR1oNVy2T8q_ohKgr6QZ7n7z0h0TKCSwtZlEnDdmFMt50hrB8zAwXinasMoSnDx6lS8crPW0Ai2pj-1Y1zK5y6kqo1o46OTMiL8mfwGe3PF-4RbNX_qtXQsf2uYHHTrbUHANiwPv7kCxILyilg2A9tOihyiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماس خليل الحيه را به عنوان رئیس دفتر سیاسی حماس و جانشینی یحیی السنوار را اعلام کرد.‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136017" target="_blank">📅 15:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136016">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نیویورک‌تایمز: پنتاگون اطلاعات مربوط به حملات اخیر ایران به اردن را که منجر به زخمی شدن ده‌ها نظامی آمریکایی و آسیب دیدن بالگردها شد، مخفی نگه داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136016" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136015">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پاکستان و قطر امروز دوشنبه پیشنهاد مشترکی ارائه کردند و در آن از ایران و آمریکا خواستند به عنوان گام اول برای ازسرگیری مذاکرات، به مواضع خود قبل از ۹ ژوئیه (۱۸ تیر) بازگردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136015" target="_blank">📅 15:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136014">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سخنگوی ارتش: جنگ تا دست‌یابی به بازدارندگی کامل ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136014" target="_blank">📅 15:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136013">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e7c4c5e6.mp4?token=i367gjp_aqwasy2rzqfgCMB4O4hx8p5MWRsM4saXjESFbDxByUvQPqc5f9-qo7_CWfWJLoAv0mTv5efIexXYTk7QqJSg3I_djMmXk0V6PtjHMuFB8c-nBtNPZW9FIWC3V4cRAOmxYS9dqM7nmdyR-AuuZRORaPOO8ApjykNxWY31veLsknOIFA78gn4IVvWulwseKWj36Ym_r3t6ggt-itPZ84E_RX0z7GUQz6_r04qx1k5iiLnW-hUpF7iZNh-tBocmJ48kkWKeUQtBnLpywL4EU7iWJNs0jguyyMnJ1I84Pmtzjl8dc4veMxFJ1pl37xgYrOIxLVxit4TrE6iW_k0L8U3sZDzdZDUCGtK0LN3vf4ReNu2GG9M2DdKqJRgAIn3iA3PZAUPmVVn1-AWEnvQe5lFGsgysJbpmjBkKVBlIiKWOlbF6yX-GpeSEtUPHePG8fGPOkQjsoP3rHlWL1OeWLjs1MSj7uivJPBInSQECfEO6iqIJ6wkDzvgViiN3orfWV9phlac1gC6BHt30GsU-dAe5Fr-qhHncVQpuyE_HOr2ZUXVVCED1_Sn6YsUcA7whqGKre-svmGiUR3ptfHZCYIWLVWDiz27cHa2Ed_jC4VWrGzRUlMAkspHnOCZe0bWDsh5pDwFT82env_zx0opLSKTdsiUPsZlU3l75edA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e7c4c5e6.mp4?token=i367gjp_aqwasy2rzqfgCMB4O4hx8p5MWRsM4saXjESFbDxByUvQPqc5f9-qo7_CWfWJLoAv0mTv5efIexXYTk7QqJSg3I_djMmXk0V6PtjHMuFB8c-nBtNPZW9FIWC3V4cRAOmxYS9dqM7nmdyR-AuuZRORaPOO8ApjykNxWY31veLsknOIFA78gn4IVvWulwseKWj36Ym_r3t6ggt-itPZ84E_RX0z7GUQz6_r04qx1k5iiLnW-hUpF7iZNh-tBocmJ48kkWKeUQtBnLpywL4EU7iWJNs0jguyyMnJ1I84Pmtzjl8dc4veMxFJ1pl37xgYrOIxLVxit4TrE6iW_k0L8U3sZDzdZDUCGtK0LN3vf4ReNu2GG9M2DdKqJRgAIn3iA3PZAUPmVVn1-AWEnvQe5lFGsgysJbpmjBkKVBlIiKWOlbF6yX-GpeSEtUPHePG8fGPOkQjsoP3rHlWL1OeWLjs1MSj7uivJPBInSQECfEO6iqIJ6wkDzvgViiN3orfWV9phlac1gC6BHt30GsU-dAe5Fr-qhHncVQpuyE_HOr2ZUXVVCED1_Sn6YsUcA7whqGKre-svmGiUR3ptfHZCYIWLVWDiz27cHa2Ed_jC4VWrGzRUlMAkspHnOCZe0bWDsh5pDwFT82env_zx0opLSKTdsiUPsZlU3l75edA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرویس امنیت ملی اوکراین (SBU) اعلام کرد که یک حمله با استفاده از پهپادها علیه یک مرکز متعلق به سرویس امنیت فدرال روسیه (FSB) در منطقه خرسون انجام داده است.
🔴
این حمله شامل استفاده از 13 پهپاد بود که به این محل امنیتی مورد توجه، که گفته می‌شود حدود 100 نفر پرسنل و بیش از 70 خودرو در آن مستقر بودند، حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136013" target="_blank">📅 15:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136012">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نیویورک تایمز: تهران و واشنگتن در آستانه یک «لحظه سرنوشت‌ساز»  بر سر جنگ قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136012" target="_blank">📅 15:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136010">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TC6gBMAG8FYSeb8w-1sixRPtn5HQ7eX4yAjgVeRy79xZknK2iZ1lU4_eunU5ULM--hynKGEEMeYdJ06dV_nNvrONhyRZkyGw0a82k0AHeulqHl2jDGvkNi4-AZMBqhomd_bHQRH8KEn8lE5Qp64RS-eFIIpYw7RRvC-Bixu0KrpDTj0qMSUjgCEeSAuBWXeQLWFHlahJAIgliatX-F8tOFhRPFk8sS5XomNRR5U-fWCE1KS914l7rdkdbajl6CJhOEItn44leL0vk1_CLHmnXHQ2fwOpIiC43gLim9bT6t6CMwRyIgnl9oZUsm9A0QN-MI60GR9ZPU6W9I2lWG4Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0vweA4-xejzDWpSBgXlKXdZvRN9FBPIm53kpBqtQv8b2B3EpspWAUtXwcD1Guxop5Xlf4BcIMqPfxFrnNaSSrkvbcNJwDtGBnijNYc2rIHKuVtlvzmm2RxkUgsQdwRC-dG04w4eCzMHX8zZrrdhefjW-dNCMQHVNCRBi3cFcnuXFVKubSbeQI7AQCc4jjOyJoR-2ib_7lIeSDz2Hw1Q_Lz1bsZFnB7tns-hjdmlKWjhUPJ8nFYB_34ZBGAI-zwmebu5ArV2sa6JcT4MLShNgIFsJkMgxc3pg463ZDnSqX52plvkwz3mSp6oFw-u3tXKtf6BYvnuNrrFzMFYewhaPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تغییر  مسیر پرواز های MQ-4   تریتون ، یکی از نتایج حملات ایران به اردن !
🔴
طی حملات گذشته ایران به پایگاه شاهزاده حسن واقع در اردن ، این پایگاه برای استقرار هواگرد هایی همچون MQ-4  تریتون ناامن شده و آمریکا دست به تغییر محل استقرار این هواگرد زده و آنها را به  پایگاه سیگونلا  سیسیل ایتالیا منتقل کرده !
🔴
تا قبل از این حملات ایران به پایگاه شاهزاده حسن ، پهپاد های تریتون از این پایگاه پرواز و بر فراز خلیج فارس گشت زنی میکردند و اطلاعات جمع آوری میکردند.
🔴
برای اولین بار پس یک هفته توقف در عملیات پهپاد تریتون ، این پهپاد از سیسیل ایتالیا به خلیج فارس برای جمع آوری اطلاعات برمیگردد. در نتیجه پرواز های بلند مدت این پهپاد و مسافت طولانی بین ایتالیا تا خلیج فارس ، باعث میشود که زمان جمع آوری اطلاعات در خلیج فارس کاهش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136010" target="_blank">📅 15:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136009">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccca6e59cf.mp4?token=PnNEY_dbF80PIrQY8w-nDxo9jb3kN3TrynnQQsCKXlSC4Iuqc7Sb2MYrs5LE6QbrWZBdCi3RHkvzhpgRfHIxwcRlc_EUJk72OpqH0GvkddClDqko9HnBSlMcyZ1X9lZE-zvLr7gtqoxkETj_8KiZZrY-n8vEpzppxmXLhki7O2_uO8gaK5Npe8-ypPbWdOoUv-i48qrXcKVEKQQ9VBfAxTIVgr_2dI0vIqCkkruY9-r3uGYu1N_oZIhM7IlgqP9P8qZLPmOQ8aDTK6kbxF1LGmEKNFgY_HU2t7QpDw3yV57Uqd9VzMV3p6WPOpVVaR_TyQzYUm59vDaeR-y4AeVNxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccca6e59cf.mp4?token=PnNEY_dbF80PIrQY8w-nDxo9jb3kN3TrynnQQsCKXlSC4Iuqc7Sb2MYrs5LE6QbrWZBdCi3RHkvzhpgRfHIxwcRlc_EUJk72OpqH0GvkddClDqko9HnBSlMcyZ1X9lZE-zvLr7gtqoxkETj_8KiZZrY-n8vEpzppxmXLhki7O2_uO8gaK5Npe8-ypPbWdOoUv-i48qrXcKVEKQQ9VBfAxTIVgr_2dI0vIqCkkruY9-r3uGYu1N_oZIhM7IlgqP9P8qZLPmOQ8aDTK6kbxF1LGmEKNFgY_HU2t7QpDw3yV57Uqd9VzMV3p6WPOpVVaR_TyQzYUm59vDaeR-y4AeVNxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پدیدار شدن و حرکت علنی زیردریایی هسته‌ای اسرائیلی در آب‌های تحت سیطره این دولت، شگفتی و نگرانی اسرائیلی‌ها از رویدادهای پیش رو را در پی داشته است.
🔴
موقعیت و تحرکات زیردرایی‌های اسرائیلی، محرمانه و غیرعلنی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/136009" target="_blank">📅 15:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136008">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رویترز : یک منبع ارشد ایرانی می گوید که میانجی ها برای ایجاد فرصتی برای احیای توافق هسته ای موقت بین ایران و ایالات متحده، توقف 10 روزه حملات را پیشنهاد کرده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/136008" target="_blank">📅 15:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136007">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_LKOxPZ2Vn76jWMhSwye0ck4jLTA9le69023hpcmulXUxj93NkqH3pPR8m-KHUKhNECHAGZGF8QhbHkTV9veqNaXczV3BDt8SRRaH_Tt5w7QhNTIcjsU2PtyzMnOMP8QLKENJc8Id-ms04MvwqzyeHHEGAJgrJEAM-TTSV58hA1SUlAvznnfXlaMz1UlZuGG3vunlwFIlqtroaF6tcMtuxH1NVAJTPzwrpXDeitk30F0tDfwyDGsRuPEGmfoXvh_jcPIL4Aj8SLggUhiHntIHZgP82BVP2criFaUw1Uj01TaI5gyo_KZLjCHvmLbnaC0EX4n0HmqbSmikb7MyLEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اندی برنهام نخست وزیر جدید بریتانیا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136007" target="_blank">📅 15:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136006">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزارت امور خارجه چین: ما با حملاتی که هدف آن تأسیسات غیرنظامی در کشورهای خلیج فارس است، مخالفت می‌کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/136006" target="_blank">📅 15:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8728c0e607.mp4?token=OBlAeBRSlPvpXSWFyq3zY32qYiFFPGOaM9c0oCiAY1K70KXIG27dR_E385CxrFDa291hMPUrNicVhi1Ze7SvMVBbawonzAHVraxLWlM97CbJDcQBlsz3YbjiyjUg988j1JAqpiyHoDO0MWnT9XZtxFVntKKum3TWIQMzuSODRB5fblr2RJs0oMtLwSBqDW3CEIyZcfUTbIfLnZp2G4ec1WQPaOSY0O9nfEcn64LvuEfdMlsp-C_Mvsg6whiXxDk811OuQMqSERC9IcbBp93uMim8Y8hj-NxTpw2PsOG-42gYwQYjKuzNKGo1FrzKFWM20FUN2NVw3zd7dppqR46IJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8728c0e607.mp4?token=OBlAeBRSlPvpXSWFyq3zY32qYiFFPGOaM9c0oCiAY1K70KXIG27dR_E385CxrFDa291hMPUrNicVhi1Ze7SvMVBbawonzAHVraxLWlM97CbJDcQBlsz3YbjiyjUg988j1JAqpiyHoDO0MWnT9XZtxFVntKKum3TWIQMzuSODRB5fblr2RJs0oMtLwSBqDW3CEIyZcfUTbIfLnZp2G4ec1WQPaOSY0O9nfEcn64LvuEfdMlsp-C_Mvsg6whiXxDk811OuQMqSERC9IcbBp93uMim8Y8hj-NxTpw2PsOG-42gYwQYjKuzNKGo1FrzKFWM20FUN2NVw3zd7dppqR46IJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یادی کنیم از درخواست کمک خمینی از آمریکا جهت مداخله نظامی و سرنگونی حکومت.
🤔
وطن پرستای الان هم، همین کارو کردن چرا ناراحتین پس؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/136005" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkeNh5CNoGSjInFd5Q_10sUUCNl72wENpFR6hPc0G6-xfo6aTUaNjydQ4i69tDzgdGRtMpxRjNJcPvU67G96VSNEDdSgSynf8BUmtP-bOtFjCoM2L-vcNE6M2zk0ajFzekiaPxUAMiVwW1F2s0u92nOgnS7hsv-iTsR1sbrioOPDn8VGZMR9-ZQB4avu7zzNydNUO0QyEG9GbnUrTHyYsb82pjl3Jv2bJtHxGuCTnFRf8AyAAUoNlxUcsPVHIpNyY_t32yPIsDoF-zIpTo7qMp9aiLqfcu2PX8yCK0t_dCL_aNe-Qs0QG4cBYxr8ZsXQ3gBgr6ZSRd6Kc392TjNI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگ‌اند
🔴
آمریکایی‌ها روی هوش ما اندازهٔ آی‌کیوی مختصر خودشان حساب کرده‌اند.
🔴
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136004" target="_blank">📅 14:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxO_DDqnlXrcvWdRnkpBqsyhorJ_bDdGQBELBUPlADhOahuOz5QA4a-FCY_XWi2UcvPpxNMPpLvlW04jC4pqN6ol7PDAutVuu3o76ZMoMRba7c6Bge_f53qV6bHT4ZFupbAhwMA9wAEgnB3yYVNPwr7g4S5DkijS1PGDNiDClp2Io8hAh46Q1ctr0HsYoVAmdBaKMkDtGhSCjPPWXdS2qCgnhM96FuF5-DjVN34i2GqWYWGZXUKxXs94xdqeCR6nlh2P9YlXRgnt5TgfKQlH47m11qECoTBezdZ_-RUsR8wEWuG4dZm6Ee1PVb0uii18QXefhQJhNrUtNxHwrYJAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ با انتشار این نظرسنجی مدعی شد که اکثر مردم آمریکا از توافق با ایران حمایت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136003" target="_blank">📅 14:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پنتاگون هویت 2 نظامی کشته‌شده آمریکا در حمله ایران به اردن را اعلام کرد
🔴
وزارت جنگ آمریکا (پنتاگون) هویت دو نظامی آمریکایی که در حمله ایران به پایگاه هوایی موفق السلطی در اردن کشته شدند را اعلام کرد.
🔴
بر اساس این بیانیه، «تایلر جیمز فیهان» 25 ساله و «ایزابلا گونزالس» 19 ساله در جریان حمله روز جمعه کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136002" target="_blank">📅 14:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136001">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اداره هواپیمایی غیرنظامی بحرین اعلام کرد که پهپادهای ایرانی، سامانه‌های ناوبری هوایی غیرنظامی این کشور را هدف قرار داده‌اند، اما این حمله، فعالیت‌های ترافیک هوایی را مختل نکرده است.
🔴
این اداره اعلام کرد که این پهپادها، تجهیزات ناوبری هوایی را در منطقه اطلاعات پروازی بحرین هدف قرار داده‌اند و افزود که مقامات، بلافاصله و مطابق با رویه‌های عملیاتی و امنیتی، به این موضوع واکنش نشان دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136001" target="_blank">📅 14:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136000">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
مقام آمریکایی به سی‌بی‌اس:
تشدید تنش به زودی آغاز خواهد شد،
هواپیماهای ترابری و سوخت رسان آمریکایی به صورت پی در پی و بی سابقه در حال ورود به خاورمیانه می‌باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136000" target="_blank">📅 14:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135999">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ایلی کوهن، عضو کابینه امنیتی اسرائیل: اگر ایران بار دیگر به ما حمله کند، پاسخ اسرائیل از واکنشی که در رویارویی اخیر شاهد بودیم، شدیدتر خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135999" target="_blank">📅 14:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135998">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cdf507a0.mp4?token=L9jQO4zix5WvjOPW1I6OfwqeTkRrynD0ALHlhiu8-eY3SugH24dGYlE9oGJbV51f7zOS1Tlacn5esrk4Mxd6EUIJGMmW5lbBkup_B_vDme8GjWlpXUyEmYohH21mafAlDKGuyifPwimD1BkDmTodw310hDMdWrqr1hmcD8_uvpU9JH0HjrMHxAEcY2ZG6IvznCaAMZbKyf9ym95KPzliremxJ0okCIPWMq8bzsu8RjpfaBe4pfXkK61R14kYnDxSC2nTxKGf7H0UK2o_lv8fXMz7ovJE8MTKCv0d12LXL1L1xYgqj1YQEWIuWxBeBhk0J6P_Yn6ENxhvGzk7UXWf_jA46a6Iprqvxo_6eIhMzKuyf9KXsmeuEi7pUbAi8qISaxw90iVs6vXPlzQgFKSAi8ro2cxCpGpVoxNiDvA8Mpln9UC6hZ8tvGy4dIGv6YMg7VSB6tGtnHLJe9-pvicW9Mgkdy7BgP_CpteisZ36H4IGolF7Adk04hcb2cAlIHLpxPpFrIw4r846ItpC85jWpw6xRWb6Y3wtV3gyV6MiPtk470sHiELaxWbKMP9Cu2fN6NoisfGGmydsZwqQv7ofdwYiRA9vKdfbbjz0cYO8aSBVqLrY6K5ptBD20Gu9WP2aWswzAO_zxddNnfKsqt6k3rIYUZThEmTWjZBJ3JMl53M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cdf507a0.mp4?token=L9jQO4zix5WvjOPW1I6OfwqeTkRrynD0ALHlhiu8-eY3SugH24dGYlE9oGJbV51f7zOS1Tlacn5esrk4Mxd6EUIJGMmW5lbBkup_B_vDme8GjWlpXUyEmYohH21mafAlDKGuyifPwimD1BkDmTodw310hDMdWrqr1hmcD8_uvpU9JH0HjrMHxAEcY2ZG6IvznCaAMZbKyf9ym95KPzliremxJ0okCIPWMq8bzsu8RjpfaBe4pfXkK61R14kYnDxSC2nTxKGf7H0UK2o_lv8fXMz7ovJE8MTKCv0d12LXL1L1xYgqj1YQEWIuWxBeBhk0J6P_Yn6ENxhvGzk7UXWf_jA46a6Iprqvxo_6eIhMzKuyf9KXsmeuEi7pUbAi8qISaxw90iVs6vXPlzQgFKSAi8ro2cxCpGpVoxNiDvA8Mpln9UC6hZ8tvGy4dIGv6YMg7VSB6tGtnHLJe9-pvicW9Mgkdy7BgP_CpteisZ36H4IGolF7Adk04hcb2cAlIHLpxPpFrIw4r846ItpC85jWpw6xRWb6Y3wtV3gyV6MiPtk470sHiELaxWbKMP9Cu2fN6NoisfGGmydsZwqQv7ofdwYiRA9vKdfbbjz0cYO8aSBVqLrY6K5ptBD20Gu9WP2aWswzAO_zxddNnfKsqt6k3rIYUZThEmTWjZBJ3JMl53M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت امور خارجه چین: تایوان، بخشی جدایی‌ناپذیر از خاک چین است. این، اجماع غالب در جامعه بین‌المللی است.
🔴
پیام ما به مقامات حزب دموکراتیک پیشرو (DPP) کاملاً واضح است: روند تاریخی غیرقابل توقف است و استقلال تایوان، راهی به بن‌بست است.
🔴
تلاش‌های مردم چین برای مقابله با جدایی‌طلبی و استقلال‌خواهی در تایوان و دستیابی به وحدت ملی، روز به روز درک و حمایت بیشتری را به دست خواهد آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135998" target="_blank">📅 14:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135997">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
موگویی: «ترامپ درباره مشهد درست گفته بود، مشهد سقوط کرده بود.»
🔴
یادتونه ترامپ اون شب چی توییت کرده بود: یک میلیون نفر در مشهد تظاهرات کردند!
🔴
یک میلیون نفر در یک شب فقط در مشهد  اومدن بیرون، جمهوری اسلامی قتل عامشون کرد و هنوز داره تک به تک جوون‌ها رو اعدام،…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135997" target="_blank">📅 14:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135996">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزارت خارجه کره جنوبی به بازدیدکنندگان کوتاه‌مدت توصیه کرد «فوراً» خاورمیانه را ترک کنند، «مگر آنکه دلایل قانع‌کننده‌ای برای ماندن داشته باشند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135996" target="_blank">📅 14:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135995">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
بقائی: حقوق حاکمیتی ایران بر تنگه هرمز غیرقابل‌مذاکره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135995" target="_blank">📅 14:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135994">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0792b06244.mp4?token=iG3bQjljLOTVy0H6rbERPbs5FJkgcpAgUTrk8tsJ3a36L1ogiEIHR8jlyCdfeASvcBMMCKB_cTzTjikYT7eJZjRr4LFdoPgazIeFkHAPa2nbdosviaDjR8HyxtTjNoVMzbtR5F-iv1kkbt-uo1b6cbP04b8lGbdh2GGdpygBVqKQ-BEp6EbHiRgbn6zXn9AIpyMshV2KM2USZ3FVd5JN7_MbFQ_Hq1WvsCa6KPUHwAcpr_8PU1KirY8hL5K1dRDta4JGBmo6ze2h8bcxiwRLPau7xAEXk6ASn7DQxuhx6szt3PX_AAeB5NDweoORqLzmRWlL2ZQL9YpbzzCFluv9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0792b06244.mp4?token=iG3bQjljLOTVy0H6rbERPbs5FJkgcpAgUTrk8tsJ3a36L1ogiEIHR8jlyCdfeASvcBMMCKB_cTzTjikYT7eJZjRr4LFdoPgazIeFkHAPa2nbdosviaDjR8HyxtTjNoVMzbtR5F-iv1kkbt-uo1b6cbP04b8lGbdh2GGdpygBVqKQ-BEp6EbHiRgbn6zXn9AIpyMshV2KM2USZ3FVd5JN7_MbFQ_Hq1WvsCa6KPUHwAcpr_8PU1KirY8hL5K1dRDta4JGBmo6ze2h8bcxiwRLPau7xAEXk6ASn7DQxuhx6szt3PX_AAeB5NDweoORqLzmRWlL2ZQL9YpbzzCFluv9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد اوکراینی بامداد امروز به ساختمانی در شهر مسکو، پایتخت روسیه، اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/135994" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135993">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m31Ah6JeKuDZvfxuHirIHax4ahOPjJlrEHfSmcAfrpqRVx8e-WRB6vyplI9zZATFFRy7PtLCsPOhrskgdOkNyDFrCrpxkK_eTyVaixgWlUww8yWdezhsJX3I3O_5uVE5eI4DOLcWvqGtP9Kg-uMaeC56OZmZMc7EDPHOtWYX3jmYbq8s8UZFMLmq3IA2F24qKjxalEEwW2bEXKJHuCAiSqN5qwyisgoC5QQjQ-idsyN-KoDm7rrbwRy_sVPAFQqTTbH3cxWViWSo7R4-Ao1zQqhytvrotnumC3vjReqcIsocujEwjau22hKAHwTq-5EweVI3h8S_e2q10Wvej8oauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پادشاه چارلز سوم، استعفای کیر استارمر را به عنوان نخست‌وزیر در کاخ باکینگهام پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135993" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135992">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b2fcbad5.mp4?token=IlEFieB-3yAgDwHFcn116XfKL2aMIGe26lMOFgWzIzjvCY92Cdb2dhN2A97JXR09-AtipErT3mTWQrRLP6lrp0X-rnZOIPIx-hLsuK-BWIsXngs3e67lVOQQZ3hXYND1n6sb1QM52n6hWVrwyL7PCJ3Y3s015brzipOxLOVD53G18rN1d68h9klckhdrIoeHOwYEMRkHtbBcC4HRngsfYiW7PVtvVYFJHNG3C7NIqQvZsw3yPlvOL6N754ZRIJXljLLaTg2EdITjrelfNRfzBOEe8GZ85oY60xnQfOJrl0sigXz2D3baz-hDLl_kBGxr9pg4aJDYRjkyUwHIz842DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b2fcbad5.mp4?token=IlEFieB-3yAgDwHFcn116XfKL2aMIGe26lMOFgWzIzjvCY92Cdb2dhN2A97JXR09-AtipErT3mTWQrRLP6lrp0X-rnZOIPIx-hLsuK-BWIsXngs3e67lVOQQZ3hXYND1n6sb1QM52n6hWVrwyL7PCJ3Y3s015brzipOxLOVD53G18rN1d68h9klckhdrIoeHOwYEMRkHtbBcC4HRngsfYiW7PVtvVYFJHNG3C7NIqQvZsw3yPlvOL6N754ZRIJXljLLaTg2EdITjrelfNRfzBOEe8GZ85oY60xnQfOJrl0sigXz2D3baz-hDLl_kBGxr9pg4aJDYRjkyUwHIz842DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایزاک هرزوگ، رئیس‌جمهور اسرائیل:
ما نوادگان پادشاه داوود هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135992" target="_blank">📅 14:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135990">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1ddfa795.mp4?token=JsNeMczEXNg4ppQYoJwsasIAsdjCvDBykDMM1KFoqGQVsBJaB7Xn6_zDLjVNsTo2vCcw_jM3TgJKHfNikiFGkfs8w2gzQhmXdchXFqG-OUTiVP0tsBPLx92LkUJoC5pKrpwXQG-SXjj9j0YN3gluAFL6YVIKIlmbdo5BG5KBSPmk3M4FbXfJOHCYDgwzNmdrW_J-c8GQx6nF0PTUyuHn5e88FdOH5ZRoRPkkHEIPpCRSH53amVUkXA_nagzqmE_cCAD2aLads-kNXRDfmseFvzCMbUO3w3CwO4jDs4JCWzvmWFnlc_kDSMJSM2CfugIQlxeoJLTp0B-1c2FaYi4cUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1ddfa795.mp4?token=JsNeMczEXNg4ppQYoJwsasIAsdjCvDBykDMM1KFoqGQVsBJaB7Xn6_zDLjVNsTo2vCcw_jM3TgJKHfNikiFGkfs8w2gzQhmXdchXFqG-OUTiVP0tsBPLx92LkUJoC5pKrpwXQG-SXjj9j0YN3gluAFL6YVIKIlmbdo5BG5KBSPmk3M4FbXfJOHCYDgwzNmdrW_J-c8GQx6nF0PTUyuHn5e88FdOH5ZRoRPkkHEIPpCRSH53amVUkXA_nagzqmE_cCAD2aLads-kNXRDfmseFvzCMbUO3w3CwO4jDs4JCWzvmWFnlc_kDSMJSM2CfugIQlxeoJLTp0B-1c2FaYi4cUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی پیش، یک پهپاد اسرائیلی به یک خودرو در شهر غزه حمله کرد.
🔴
گزارش شده است که حداقل ۱۴ نفر مجروح شده‌اند و برخی از آن‌ها در وضعیت وخیمی به سر می‌برند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135990" target="_blank">📅 14:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135989">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca140d784d.mp4?token=edepPKHo5kaYgcyOTbzovtQKr58lokpXv5eNRq4EhiGv1D1UFenVN8xKdQUtJtKsKhHnIPu8_poesgUC7rvUiuZm4XqGWSGI9v4czyHrlpLv-H5UtRvM5SLPE0K_EMFL8RjLCzCMoGjGuwXgSsvYiKOlMsfuaiuaO1uZW1E3aVaj0rHDc5EQw3N8vJZ2AMoecCP04JX0hGxIBXL6AEOqFtxTsetwxNhabTegWMYVz9CuWAYUdgGpWpmawXjtmSZ6Kh1zPo3EEzfGcxCwuki7BtWPOWcyvO7Axx4JHDDk87acn23X4tFqFZhESb8uUByTmdfqjLa-RziYwxaOp-uckna07DDD7VbrC6JmnFlYhf6AEW1C-t2GAi8eUL0jdLGOvaAz1oeNqAVsbwZ_XeyqpOP_-VM-qG2qyj6DMilZqLQH61OfgWaD4KoX4_CrhcMsaVYS5mxSoOHeIKu0QdZV79GXuS4Ov-YfA8ztn6-Rw08VwD2dUOFoNIFFtXCA73Xb8lZ7eTCFZDJuXjslc0WyfpVSbzLjdawlDh8-cbpE4TL3B7nM24Y6KzBZImkQyiIkWU0-rTtfOkxdJ22ycge2tIQ_pf8g7ZNKe4wsq3cEUFOKmBDIKi8U4jL7GsMulP33R4vtISrYXJIiLwYsN46EEN5-PcpUUX6QmZcuXouV_Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca140d784d.mp4?token=edepPKHo5kaYgcyOTbzovtQKr58lokpXv5eNRq4EhiGv1D1UFenVN8xKdQUtJtKsKhHnIPu8_poesgUC7rvUiuZm4XqGWSGI9v4czyHrlpLv-H5UtRvM5SLPE0K_EMFL8RjLCzCMoGjGuwXgSsvYiKOlMsfuaiuaO1uZW1E3aVaj0rHDc5EQw3N8vJZ2AMoecCP04JX0hGxIBXL6AEOqFtxTsetwxNhabTegWMYVz9CuWAYUdgGpWpmawXjtmSZ6Kh1zPo3EEzfGcxCwuki7BtWPOWcyvO7Axx4JHDDk87acn23X4tFqFZhESb8uUByTmdfqjLa-RziYwxaOp-uckna07DDD7VbrC6JmnFlYhf6AEW1C-t2GAi8eUL0jdLGOvaAz1oeNqAVsbwZ_XeyqpOP_-VM-qG2qyj6DMilZqLQH61OfgWaD4KoX4_CrhcMsaVYS5mxSoOHeIKu0QdZV79GXuS4Ov-YfA8ztn6-Rw08VwD2dUOFoNIFFtXCA73Xb8lZ7eTCFZDJuXjslc0WyfpVSbzLjdawlDh8-cbpE4TL3B7nM24Y6KzBZImkQyiIkWU0-rTtfOkxdJ22ycge2tIQ_pf8g7ZNKe4wsq3cEUFOKmBDIKi8U4jL7GsMulP33R4vtISrYXJIiLwYsN46EEN5-PcpUUX6QmZcuXouV_Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که یک ستون دود غلیظ از بندر الاحمدی در کویت به هوا برآمده است، این اتفاق پس از حملات اخیر رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135989" target="_blank">📅 14:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135986">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVUycls9NIDyFXIVLMl86HhTkwPIQZ7wx_f-5vRUprJ54BR2fsuqms4eLBN4DZZwXpzi6MZXTgY_0Cyj0O8dVaVfKPeh07L9LiyiQhjUwBVZK5g6Rh6hhwceS83uAx7J50h250quPNoRUhP4PSmSgcHkLuI-6QH3e_afR50oHlbT1hk2B--TjwVF5_aKwKLb6S7-CJ6kK_RM3hQVb9sANTLTvzvuxvxCpxMSuyVLgZM8iv9XHu5a8rRmjTuo37LSGjUIH8VupdrLCwz3W4T529lCAh-IBKuUQMZHanKlOPXDchjoAWaiGd1urLGkQKyCcldh2znS6klrw2nXqcqRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iW78NF03Eb18nn6-gp-t7XDiGr42NA_cRXuZ-J2dljTcTj0utiWsk6zG_w_44r8mLHd7XeFPeaiR593VD8XHzWqz3IWE4kXfnDcMajvgeC0EwzlaDm_VBwqJYFEN37UnF12ypnk6iAErE9T6-34PJishorF_t2Si2_bTgYLZsU2EfpyIQvG6OI2KB-Z1MFEKQxTuzeE_0TkE792LpI60v5nT1dMQ4yykYP6DTJ2yeCyFcz4hr4pVDxWEN077znHschXR1KOcN8sIuL10YQSdy3xP2r1FKBh-kZcV-ZnEJdQEDcNoampbCwPcPJivAE5VyeZibk040YBVe29LyJIY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B33nsMJ6ZrxMgS9HEE_1i9WeXNMmUwcFyWxxVlHjWxPBDhGfVAjAcGFTlX-ddT1wEAhO0_phymGyfLo7UkJUbSIN6cNKQWyXDG1Sq1is4AHrIYFN076A2TT_E3OCBaMWwtyykHS-7_iN8R_s9yD2bbv3reJ0IazGRW9h5o8V6Fe4GELESI4qtIGWZ6gdcz7t07UdZnbhZbqPN5dorvCJ81fq-v1drqE6dw54Ceb934kbIGTnvZtFZtum5mSMc-xC81i-qefYPDBv2OH7Ik4nZ1pf1i8JbB2GlMeMxu9NRKbEs6PKQl-dx3xg3IZwLdse0Xf9l68oMXR-ySmBzoyFKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدیدی که توسط ماهواره‌ها گرفته شده، ویرانی‌های گسترده‌ای را در پایگاه "الأزرق" در اردن نشان می‌دهد. در این تصاویر، تخریب محل‌های اقامت سربازان آمریکایی، به همراه انبارها و محل‌های نگهداری هواپیماها، به وضوح قابل مشاهده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135986" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135985">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93c584a72.mp4?token=Ynvwj_6xz-UjdYHVKdha0pylTByLdWTD6IuK0cpbHhN8tzvDVuQXo_KLoune6JB5aTePKgxgogvoMTP5GhPG3szy9u2alBUop89a6XFTHKGBSlViN-Ya4pL6P5-LzqGSXwTSvuxDuksxuDibav32UcwsYzKS9aPTXE-2Pta9hgOEg3N9yLRu4dX5tapGNrENveCN6yRygvYJo51ZpHPifCsfE7NI_ELYlK14sSiq9mfTYF87xgldXZa5Yja0VucfZV5HqVV-b0OPVuxtHQWr9YQyRpp_HtFe5nhUnAJycEaHIzWj8FOf5YpWqiP18zXGi8HgcDzaDyeueMtPSYjRNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93c584a72.mp4?token=Ynvwj_6xz-UjdYHVKdha0pylTByLdWTD6IuK0cpbHhN8tzvDVuQXo_KLoune6JB5aTePKgxgogvoMTP5GhPG3szy9u2alBUop89a6XFTHKGBSlViN-Ya4pL6P5-LzqGSXwTSvuxDuksxuDibav32UcwsYzKS9aPTXE-2Pta9hgOEg3N9yLRu4dX5tapGNrENveCN6yRygvYJo51ZpHPifCsfE7NI_ELYlK14sSiq9mfTYF87xgldXZa5Yja0VucfZV5HqVV-b0OPVuxtHQWr9YQyRpp_HtFe5nhUnAJycEaHIzWj8FOf5YpWqiP18zXGi8HgcDzaDyeueMtPSYjRNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزها که شرایط جنگیه و پدافندا هم تو اکثریت مواقع  کار نمیکنن؛
پیشنهاد میکنم این ویدیو رو یه گوشه‌ای ذخیره کنید، بعداً حتما یه جایی به کارتون میاد :
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/135985" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135984">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh7Qw89i_dZIsQz3AxnghPSPd2_kc799KTb5KQ-mOlrPHKP7Hj7hoo8hZ9taeG1z3jmnmaaYl6Bqmv-4_lNuPP-vwRQdVaW3QAiCiKRHd-fwLNmwIYCeiQM46mCMMptpk76NjN4lgeSIXpdi0yw-QnW_KYDPX3LTBWtP5WGdpA2BV6MTLeYJaDhX_kiJhC3ybjzrNrbnCOWe9GI7Fc247bigs2_bbdttaLFAkB7-bY4ys0vNvmS9HNHeHNGsF-Kj6_ij1akqW_nBeC1wiqe7uxEcRp6420gFcgFjBALhO1FbtwLprsqy0Mb8M8v9SvN5pKqdK4xAduXkEdYLV5XMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
فیروز کریمی :
میمیک صورت مسی رو ببینید داره الکی گریه میکنه چون دید رونالدو گریه کرد و وایرال شد اونم همینکارو کرد !!
@AloSport</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/135984" target="_blank">📅 14:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135982">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrHpnVquIcq09ldEOXdkJASBE6pCJoyBNFHZWZyyItKIsF4aWbogtwr3iDZAaaeutVKzebvgvNbkBkl9OmunQtWAF6FddB-mV4yDb49EbkMJBh02u1gd1MQXLzWQWhVQXawWlHZ1zJ_3bcOn5dkQhH9oKjEEDLWhWOzrayMnjeT0v8h7C4SKiw7url8zyvn1Z_msc9KSDOjrWLjvbyXzFKXAZlG2yksdrs30RWKMSTmQrP0NDvUM_JBuROTBHwYBFy90IqdUf4GOfkKNi83M4BL2esaDhCCHDFisGKvwa73IhGdhAJK_z0P9Uswez3gFSnw-dhVGRxZm3p5GAnLIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBmMLcI0U9bW7ZHpqcK-N2trnquh_vrD0bQjjg8CFutpjpZreiNsiNNzUkwV6wS8uYxd939PHbVIYvtuOdu3YW121UdvxrgkfdvRJsit-Gtz9pisNxs4ntzNOB3eN9fVAAqwJPX-9hIxeKFZ04prQ5hTuEWakTTkuLOgUuuf_-qTwm1PRU8J20Gr3IKLe0BgQd0baJq3_BGJ343FoNnFBO0sU6JWGEkCrrfzV62rK98WCQ2Xs2YP5AHAJZNYptG6T8nDhJkJyOexWuLsg6eEqEbz_dGPK9Ge9_lbCKGEy7-zoJfetjy5cSX3DO609cylSP-JB5hrTYewYAORewV5Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کامران غضنفری با شکایت حسن روحانی به حبس محکوم شد!
🔴
دادگاه بدوی کامران غضنفری، نماینده مجلس را بابت هریک از دو عنوان توهین و افترا به پرداخت پانصد میلیون و یک ریال جزای نقدی و بابت نشر اکاذیب رایانه‌ای به سیزده ماه و شانزده روز حبس تعزیری محکوم کرده بود. دادگاه تجدیدنظر اعتراض متهم را مؤثر ندانست و حکم را عیناً تأیید کرد. این رأی قطعی است و مجازات اشد قابلیت اجرا دارد.
🔴
کامران غضنفری، حسن روحانی را به «جاسوسی برایMI۶»، « ارتباط با سرویس‌های خارجی»، «داشتن تابعیت انگلیسی» و «افساد فی‌الارض» متهم کرده بود. دفاع او این بود که مطالب مطرح‌شده را از برخی اعضای کمیسیون امنیت ملی مجلس یا گزارش‌های مربوط به مسئولان دوتابعیتی شنیده و ردصلاحیت روحانی در انتخابات مجلس خبرگان نیز مؤید ادعاهای اوست.
🔴
دادگاه این دفاع را نپذیرفت و تصریح کرد که هیچ‌یک از این انتساب‌ها در مراجع رسمی و قانونی به اثبات نرسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/135982" target="_blank">📅 14:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135981">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1232873fbd.mp4?token=EtqaW0iS2Fnv5FGi-et-oV1AWIBGRB7NkAFQrk4hJdYguGj1oopyTaC6Xbth1VQNLoJfScnAe4fW4oBsAU7Hk2gc-4yhGkpRmQEG59-TSjKlPSTcNJKbyBiRc028s9K-5qiYLz8unu_X2RJPzA_LLbjugUdnJnhB_ySIt6eHo_M3E4uppwVIwUxivnutSbzQi-EIgJTSvRSP58_xpxsdvqfsQy01Mni0RF-wqA_T0yMFiAMjlP5GXwMpqFD1InhD7WgCcrcA4N3cp0OKJX1EyVoX5B1pqBduIH3JLkDlgibT_VFsI7mx-26dLRaMsO3qOzebjEIzvTUU2JS0pWcCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1232873fbd.mp4?token=EtqaW0iS2Fnv5FGi-et-oV1AWIBGRB7NkAFQrk4hJdYguGj1oopyTaC6Xbth1VQNLoJfScnAe4fW4oBsAU7Hk2gc-4yhGkpRmQEG59-TSjKlPSTcNJKbyBiRc028s9K-5qiYLz8unu_X2RJPzA_LLbjugUdnJnhB_ySIt6eHo_M3E4uppwVIwUxivnutSbzQi-EIgJTSvRSP58_xpxsdvqfsQy01Mni0RF-wqA_T0yMFiAMjlP5GXwMpqFD1InhD7WgCcrcA4N3cp0OKJX1EyVoX5B1pqBduIH3JLkDlgibT_VFsI7mx-26dLRaMsO3qOzebjEIzvTUU2JS0pWcCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بندرعباس - دی ماه ١۴٠۴، حرومزاده های حکومتی که جلوی چشم بچه به پدرش حمله میکنن!
🤔
بعد مارو از نیروهای خارجی میترسونن. نیروی خارجی با مردم معترض کاری نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/135981" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135980">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پزشکیان: درست نیست افرادی که هیچ مسئولیت اجرایی و نقشی در مدیریت مستقیم امور ندارند، خارج از فرآیند تصمیم‌گیری صرفاً بگویند که باید به شکل دیگری عمل می‌شد. طبیعی است اگر همه واقعیت‌ها و محدودیت‌های موجود بیان شود، بسیاری از این قضاوت‌ها نیز تغییر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/135980" target="_blank">📅 14:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135979">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پزشکیان: امروز در شرایط جنگی قرار داریم و اداره کشور با همان قواعد و رویه‌های معمول گذشته امکان‌پذیر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135979" target="_blank">📅 14:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135978">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پزشکیان: زمانی که تصمیم می‌گیریم در برابر دشمن ایستادگی و مقاومت کنیم، باید پیامدهای این تصمیم را نیز بپذیریم و نمی‌توان انتظار داشت که در شرایط جنگ، جامعه با هیچ‌گونه دشواری مواجه نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135978" target="_blank">📅 14:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135977">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
پزشکیان: فشارهای اقتصادی می‌تواند به دستاوردهای نظامی ما آسیب بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135977" target="_blank">📅 14:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135976">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
پزشکیان: از هیچ‌یک از بندهای ۱۴ ‌گانه عقب‌نشینی نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/135976" target="_blank">📅 14:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135975">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پزشکیان: امروز بیش از هر زمان دیگری به وحدت، همدلی، تصمیم‌گیری مبتنی بر خرد جمعی و همراهی همه ارکان کشور نیاز داریم و دولت نیز با بهره‌گیری از همه ظرفیت‌ها، اصلاح ساختارهای ناعادلانه و خدمت به مردم را با جدیت دنبال خواهد کرد.
🔴
پزشکیان با اشاره به مسیر دیپلماسی و توافقات انجام‌شده: برخی بدون توجه به واقعیات، مطالبی را مطرح می‌کنند که از اساس مبنای درستی ندارد. گاهی نیز ترجیح می‌دهیم پاسخی به این اظهارات ندهیم، زیرا بسیاری از این سخنان با واقعیت‌های موجود فاصله دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135975" target="_blank">📅 14:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135974">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859193bada.mp4?token=JojL1lwNQXUxV3f5_itf4e6pTSANNor87dhnTEIv0RCGfXNvJpJknAwoO_JXGVWbpIvibSvFMcE-JiLW3CYOGYht_dOz-33V7dQe52Ktco6k_w9P_QRzogex7N5ezG3wFAl1elx-qaN6_HkBOiP9YvRtTqpOwZogwu8kFtw9uT2jpsIXu091624BgPmWTHcKy8i8b8qAjZzLNnteZQO2K4hplruCEFhDdtpDtCwKDP_3wmNme1T1Yr5tdRbSyhbHq7NIN-GbvKkiUvMHplzVQ_lWLor3bUggCQ2l4kRvbIFFZTu5920HnQGLbfg6mdkZMT8jjjlmgkS23BiRLIdBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859193bada.mp4?token=JojL1lwNQXUxV3f5_itf4e6pTSANNor87dhnTEIv0RCGfXNvJpJknAwoO_JXGVWbpIvibSvFMcE-JiLW3CYOGYht_dOz-33V7dQe52Ktco6k_w9P_QRzogex7N5ezG3wFAl1elx-qaN6_HkBOiP9YvRtTqpOwZogwu8kFtw9uT2jpsIXu091624BgPmWTHcKy8i8b8qAjZzLNnteZQO2K4hplruCEFhDdtpDtCwKDP_3wmNme1T1Yr5tdRbSyhbHq7NIN-GbvKkiUvMHplzVQ_lWLor3bUggCQ2l4kRvbIFFZTu5920HnQGLbfg6mdkZMT8jjjlmgkS23BiRLIdBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیِر استارمر : من برای اندی برنهام آرزوی موفقیت دارم. او از حمایت کامل من برخوردار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135974" target="_blank">📅 14:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135973">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494c3c2054.mp4?token=PZetjf2MpKeS-zYavTOk3aLw6tXzX5EO7jbcob0dvYwrP3HoX3Y70slqh0syDl7TGIqW3bsRwWKiotYtXVJ_aIgDAJQ0-RzWw8fcUH8TQIemjIdK2hE64fw17mAb_QmSxhbxQ5nFvQIPQz3QLMg9oEf6UDoiFDa7E5BI6cLBjaFZkjSqAyKKHoKkFENKiXBIz6I8Ux5lEnA0ANo1k93d9jdeIVGDAqouZPKMPk6C8mva9ebJ3_yNz2v_C-3B4BNPPjybKKY_ieu0cNCJWvNSfG8FtpbDw7LuxOhjzRKaCX31rW4kk1IgBLDvG4Iv3oa3DE0txmToRv2e9UCX1E-Cxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494c3c2054.mp4?token=PZetjf2MpKeS-zYavTOk3aLw6tXzX5EO7jbcob0dvYwrP3HoX3Y70slqh0syDl7TGIqW3bsRwWKiotYtXVJ_aIgDAJQ0-RzWw8fcUH8TQIemjIdK2hE64fw17mAb_QmSxhbxQ5nFvQIPQz3QLMg9oEf6UDoiFDa7E5BI6cLBjaFZkjSqAyKKHoKkFENKiXBIz6I8Ux5lEnA0ANo1k93d9jdeIVGDAqouZPKMPk6C8mva9ebJ3_yNz2v_C-3B4BNPPjybKKY_ieu0cNCJWvNSfG8FtpbDw7LuxOhjzRKaCX31rW4kk1IgBLDvG4Iv3oa3DE0txmToRv2e9UCX1E-Cxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیِر استارمر، نخست‌وزیر بریتانیا (در حال ترک سمت): من با آرامش، با لبخند و با افتخار از دستاوردهایی که به دست آورده‌ایم، این سمت را ترک می‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135973" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135972">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / الحدث اعلام کرد که هواپیمای نتانیاهو حریم هوایی اسرائیل را به مقصد نامعلوم ترک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135972" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135971">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت بهداشت جمهوری دموکراتیک کنگو اعلام کرد شمار جان‌باختگان ناشی از شیوع ویروس ابولا در این کشور به ۹۳۰ نفر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/135971" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135970">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXgc6BJdY33FtxUh3_Pivm0wy5hjpb37s4VL4UKbppWZsCBzIN08FzmTu24dAYAqO16j6BFKAhjFfLd72oOrJ7e22VjcXaa68HWqc9NwhGp0FKzfgAm0Tcfv_QOYMsH8tYo-HazoXeZFdEg7kYJAMTjkTQn1A_OownRNtDQG00em-C2C0QWl18uYga6pHs-43dLMdzc9JnoS1V4sLFsDKL3cHq3m9MA80iTPybUG50GzaFpeD59RNp-qQPioQZE32_utt6dsDAGrnPevjhbn2301ru6o_6XxSPQtWpU7S04lRtQIz42Jfj-ALz6mN_9jsjKI8qgsKn0EV4opESaU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از چهره مسی هنگام دست دادن با ترامپ که در فضای مجازی وایرال شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/135970" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135969">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0116054239.mp4?token=Jh7NtsHcBa6C4LRsdYQ2qY2Si-ljJNiJqu8TA4A5hUttaiDy7iqnMsg1R6iyTBqKIc0gFxqop08lI3f245nqnBq3HX4mDqFd3qzuvCShygRrrcThVMIEySTMOSbTWZgkqhsRLKw2x9cFwJRPdZNqW7QWN-utaEktNiAj_B6Qdr_IW6o1WVPisFl4hiPVSIhFWNvdtMMN_6B14y40s80VbfQOdurzGcz8WJhqQjDsJemafh9m9REBMlcjyd3MgHFUxkiyQtXYT3TKP-ABulJ0HuEqH72SWuSfbzWOLQOwpaG66HfumbwaTZGH1o0me_ycALs_fDb--WBOZu01hUADag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0116054239.mp4?token=Jh7NtsHcBa6C4LRsdYQ2qY2Si-ljJNiJqu8TA4A5hUttaiDy7iqnMsg1R6iyTBqKIc0gFxqop08lI3f245nqnBq3HX4mDqFd3qzuvCShygRrrcThVMIEySTMOSbTWZgkqhsRLKw2x9cFwJRPdZNqW7QWN-utaEktNiAj_B6Qdr_IW6o1WVPisFl4hiPVSIhFWNvdtMMN_6B14y40s80VbfQOdurzGcz8WJhqQjDsJemafh9m9REBMlcjyd3MgHFUxkiyQtXYT3TKP-ABulJ0HuEqH72SWuSfbzWOLQOwpaG66HfumbwaTZGH1o0me_ycALs_fDb--WBOZu01hUADag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: ادامه فعالیت بانک ها ناسالم و ناتراز را تحمل نمی کنیم/ مهم‌ترین ماموریتی که برای همکارانم در بانک مرکزی تعریف کردم، کنترل ناترازی بانک‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/135969" target="_blank">📅 13:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135968">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a594ec6809.mp4?token=ZGaI1_J7BC3F5ZXnjDmA_uVwHx4mtL_HAwvZYUV8OHSzCmhZpbk4h_0nGsc7-Iy1XQ3TkPFAy64K5_rrI_DfRIFgUknME8tIg-R5at0DgtH-Z42dp-G369VlV6a27mad3cQsDsFQQpWFVdangGKqwcasVyk0KEFBvpoP5HexZyyZM8CpivvlQaO3ICqtDqjN4e6EiGWnNuSJ2lInZx9dumlu1VeBSsIu0xAp1r2P-77uQsUg76Ctw9TSK9ZryS7wUHNme7Uj1hrZRwTCQJqkWBcX3PU6s_mAnbNlUmL2M3uMg86a4lCzNof_N4AMP4_t5CmXaVwx3OHGjULge4S2PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a594ec6809.mp4?token=ZGaI1_J7BC3F5ZXnjDmA_uVwHx4mtL_HAwvZYUV8OHSzCmhZpbk4h_0nGsc7-Iy1XQ3TkPFAy64K5_rrI_DfRIFgUknME8tIg-R5at0DgtH-Z42dp-G369VlV6a27mad3cQsDsFQQpWFVdangGKqwcasVyk0KEFBvpoP5HexZyyZM8CpivvlQaO3ICqtDqjN4e6EiGWnNuSJ2lInZx9dumlu1VeBSsIu0xAp1r2P-77uQsUg76Ctw9TSK9ZryS7wUHNme7Uj1hrZRwTCQJqkWBcX3PU6s_mAnbNlUmL2M3uMg86a4lCzNof_N4AMP4_t5CmXaVwx3OHGjULge4S2PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: اجازه اضافه‌برداشت به بانک‌ها نمی‌دهیم و هرگونه اضافه‌برداشت منجر به عدم صلاحیت مدیران بانکی خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135968" target="_blank">📅 13:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135967">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpeae-hDnThBUinMiXAkd9Lkl9Gx7JugfE9TAyF7KuTAnd_nSEVa0fp9mXfyrzwUzYuc0MZ3ccZaETTOeo5xAoYIJUUyVdbCkO_GNC5LA621LsypP4WEJJmwfuvYuybF1CH_WqSrN3MGdusvzC5PpkK3V0KbhQnMLdutES7SIydTJn3PiunlfYlldBdG9idBNO14v8lY1qw_RNkdMlbYslTrlafI2Zm14t8KEZX_X8z-tMdPDJ-YEW-Keqkxk5TY_Hw9XV_9I5-QJJjWNXEH4Yvlp8yVQ0-PyRZa9C1Rn9b5kn1UR7kR0ERiRGxw0yvvSxsE18-NOBCFqSaQOcCGiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرپرست وزارت دفاع: جنگ و تحریم، موتور جهش فناوری دفاعی ما هستند. در جنگ ۱۲ روزه که یک جنگ فناورانه بود، با وجود بهره بردن دشمن از بزرگترین شرکت های فناوری دنیا ، ما پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135967" target="_blank">📅 13:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135966">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTcX_v9GFtgoSfsoU9u1PviXslhMxD3HeEZPVE3jm3HnqqdcTN0Khrof1tihDujMYIk4VRWEWFyB51BihY1sLvTnhqj2Kl7IsDm2QAayVo5o0msztWBZN_p71pRHIImSFyeUSab7Sp103cfayYJIzck0rce829vw4Wz0jwfAhti5pUXzUHxfp_hV11ZLPywgu3mKdBnKKhD9CK6r1QvgyIEDJhp8hCLc4f1CWuXV5UAc9CLwdf_Vc-i9X4TF1hlXBoIPjmeIrE46g9zmRykiJj5CC7NFDumcA6-yW7XMGCMEow30nbbJBLsVsrve_dTwodyGaMfcY2O9tUtdZ2OutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز دمای احساسی زیر آفتاب تو تهران به ۵۰ درجه تو قم به ۵۷ درجه، خوزستان ۶۰ درجه و هرمزگان ۵۸ درجه رسید و روز گرمی تو اکثر نقاط کشور داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135966" target="_blank">📅 13:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135965">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نیروی دفاعی بحرین از رهگیری و انهدام حملات امروز هوایی ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135965" target="_blank">📅 13:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135963">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I61yWgSDBAcOTxty6vzUD5gxMrkAvE0yWBCPFNd357c9ljFIZGoqoCNxMF3qto5IeJjpXB0ShQ7zfvS_mCkwcZMuMKmzZAfvBmnUlMnOUYwmGoFp0yTyPCQC8YPQcWUrBhL5CN393gn2HIvwyFS67phGv-4VtoT_-7fNfWWHSCKBaL-4Gjyj6G8HwRA7BIiti6nENeGREGs7OQYeYu3v0L1kHKyD0C2ctC1Rm1evZjHjWEByncOKNo35huSMVHNDI4rkMPzT8PL4SSQEQvoq3NTXJZkunuqrsGaBBpnyf3y1o_YfmDwZkAgeJekmBya_lfkGF_5vKIPctavKDTpp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219af3c8de.mp4?token=vCNm29v-nMBlc_FEKKZOT9urky2zFnv5Ikg3WjyizaiQcZZSKvgEPcsdKKOyLwfYHh-QF1U2XWBZNet9OOZ4_qC8ZuEDBxstYxZmrTyIZ2g-IQ9YTLgWHm4x8s1Z-kIcHjOYKFGgnO2GfG4pW3Q8IDRTJzkuVcE7f6SYWyYHGNOcaUnTXowvcwPlMD_UFOQUCQUhK-T0JJT8vf67Mqtr23VE_07xpu167fIfkVQmqTFAXNo0AFxw2YoxyGeMLO1chvH6dG9lP-u_8-q7a76b5MtdHXc_OieaV6Ys7PbdU0ykez8JQvsUyfmL1xjWGu6pU0voBQDEUBGaJlVpXdJLqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219af3c8de.mp4?token=vCNm29v-nMBlc_FEKKZOT9urky2zFnv5Ikg3WjyizaiQcZZSKvgEPcsdKKOyLwfYHh-QF1U2XWBZNet9OOZ4_qC8ZuEDBxstYxZmrTyIZ2g-IQ9YTLgWHm4x8s1Z-kIcHjOYKFGgnO2GfG4pW3Q8IDRTJzkuVcE7f6SYWyYHGNOcaUnTXowvcwPlMD_UFOQUCQUhK-T0JJT8vf67Mqtr23VE_07xpu167fIfkVQmqTFAXNo0AFxw2YoxyGeMLO1chvH6dG9lP-u_8-q7a76b5MtdHXc_OieaV6Ys7PbdU0ykez8JQvsUyfmL1xjWGu6pU0voBQDEUBGaJlVpXdJLqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های ارتش اسرائیل به غزه در جریانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135963" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135962">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aafbeec7dc.mp4?token=LYnpdTtBhP2HhO8RaBcDGTn5IIb-vFawgn0E6lbSJ942ln5Ubl28RNnwhMV6hKUCuy-7jZbiVlHH6FbX_AWXCPWREuJMGdFJln6tbk-i5FMCLpi-wNKbDGl0Ub2-LCOZWgmTPnN0tuTr7JSRcgvbB_wsTaS2uKw6whGgMUMiVjmlJ6zgl-r9gyI1JTf4swRcGBK9cSO0N20HH0ZcRcFxXH9fnSYDn6XZ-Qnl8Y_bMY9BvLBBH1PZM7IDEkS-h4eykbw4dgFxrfSN4H93qSY5lifcc-JTN7hSvfHpN085Vr29Y84A71--4KsK7tHtkFNkn6HYY43QGp5PBAbpDn2Fm4cvULcv8AUqoTb9U1zPQBoRLdl3HnmDoh61uvEnRQ3AugD9NqOba8yQOdb3GaFxBk5VOdd2rhAjFU2W37BWvKakch0MFIRShIgUaCwu63LonbZj7K_BCwEHegoaXTt6y1Jvdr_j6Hhbbp8x6H7QhIKMXYa4Y_iKt3IXUMxelX74eZ2tGWTOMa39a_uuoTnph7nZ2uEQDaoAFb4oLHpfR4um9DdWZi7rhAx0DwaHms7cBTmtztXaFtFDo4XDXQUaXvHzAkLIeksOqqOOKGT8eGpOR9NXOPwJguMgRGLgO0aSKEeN-CQ9H4y9UzOFTyNEuHXdESuJRqPsLZc-obbIjqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aafbeec7dc.mp4?token=LYnpdTtBhP2HhO8RaBcDGTn5IIb-vFawgn0E6lbSJ942ln5Ubl28RNnwhMV6hKUCuy-7jZbiVlHH6FbX_AWXCPWREuJMGdFJln6tbk-i5FMCLpi-wNKbDGl0Ub2-LCOZWgmTPnN0tuTr7JSRcgvbB_wsTaS2uKw6whGgMUMiVjmlJ6zgl-r9gyI1JTf4swRcGBK9cSO0N20HH0ZcRcFxXH9fnSYDn6XZ-Qnl8Y_bMY9BvLBBH1PZM7IDEkS-h4eykbw4dgFxrfSN4H93qSY5lifcc-JTN7hSvfHpN085Vr29Y84A71--4KsK7tHtkFNkn6HYY43QGp5PBAbpDn2Fm4cvULcv8AUqoTb9U1zPQBoRLdl3HnmDoh61uvEnRQ3AugD9NqOba8yQOdb3GaFxBk5VOdd2rhAjFU2W37BWvKakch0MFIRShIgUaCwu63LonbZj7K_BCwEHegoaXTt6y1Jvdr_j6Hhbbp8x6H7QhIKMXYa4Y_iKt3IXUMxelX74eZ2tGWTOMa39a_uuoTnph7nZ2uEQDaoAFb4oLHpfR4um9DdWZi7rhAx0DwaHms7cBTmtztXaFtFDo4XDXQUaXvHzAkLIeksOqqOOKGT8eGpOR9NXOPwJguMgRGLgO0aSKEeN-CQ9H4y9UzOFTyNEuHXdESuJRqPsLZc-obbIjqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جمهوری اسلامی نقض آتش بس کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135962" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135961">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر نیرو: آب‌ شیرین‌کن‌های جنوب کشور همگی فعال هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135961" target="_blank">📅 13:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135960">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نیویورک تایمز: پنتاگون، ده‌ها مورد از جراحات سربازان آمریکایی را که در جنگ با ایران رخ داده بود، پنهان کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135960" target="_blank">📅 13:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135959">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoE8k20Dp9X3Qp5SMRasZs7aDBCvzT_m5_Sia62FiLnuqAX2iEWlZJlmWoQYKZ6e5YZKzu3WdU32adTeqA4CbQcc47tnO1y-oN_11yNvzLPZ5RhDxBac7RTHf8dv29Jkp6XK4srPU0Z4Ukf9neaeEYmGi0rmAvC0zoI3ATooMWbKcpl5OvdIX0bBZ-8yPoENrgolWdyY_BMVBJfb05MWC4Y07ml7pVk_y3t6wQjs_weCQbXsv6Z3FAeLSf7fUUwZVEtqK7SoNy1U2vqR0DDZhMo6V7_1kMlahKEVvC_NYxzlTlLIlXNffaDGAMWw101rY8j2x3_8CBHChSeumK3Pdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ دیشب در جشن قهرمانی اسپانیا، تا لحظه آخر، قاب قهرمانی و بلند کردن جام را ترک نکرد تا اینکه اینفانتینو اومد بردش!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/135959" target="_blank">📅 13:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135958">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b53f8115.mp4?token=kNqt7qsWvKQCjQ00vAkXQB0CGURtWRCSvb6CyBzAmJdiA-bPFkKLID9Y7-loigdLKKnT3J2_14yegedJYPE_YLd_mlfxmW-jRDdWdEzijXF2ZnNwkxRfOWVH2uLqpVx2mB5knnwlLf-ySV3oIPuZepmicaM4FCYO8fZERWeZzKwQgy69b0knKMwyMTW0NBrDFvMHd-ExEmpCAOW6YIN6vPtHStMV7utnd_ItYJ-ZfcBbhkpTCXkq0K8UysJNYii3Ge-ZH42v4uYPjNL1xGV943s8jKiX0PjjzHyTjWcqh4p5CYkdWZ6Z1h2-qfMQ4H2t52TO1Fc4Ff8UZ1l1AmwM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b53f8115.mp4?token=kNqt7qsWvKQCjQ00vAkXQB0CGURtWRCSvb6CyBzAmJdiA-bPFkKLID9Y7-loigdLKKnT3J2_14yegedJYPE_YLd_mlfxmW-jRDdWdEzijXF2ZnNwkxRfOWVH2uLqpVx2mB5knnwlLf-ySV3oIPuZepmicaM4FCYO8fZERWeZzKwQgy69b0knKMwyMTW0NBrDFvMHd-ExEmpCAOW6YIN6vPtHStMV7utnd_ItYJ-ZfcBbhkpTCXkq0K8UysJNYii3Ge-ZH42v4uYPjNL1xGV943s8jKiX0PjjzHyTjWcqh4p5CYkdWZ6Z1h2-qfMQ4H2t52TO1Fc4Ff8UZ1l1AmwM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیکه‌های سنگین عادل به قلعه نویی
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/135958" target="_blank">📅 13:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135957">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90c8a06ce.mp4?token=g5C7GiBxLVo448SJlm4sGiYJ-g-9pOVbmVHemNFxDO3c0l_BRtt6uTrRfjNV7mVOz_G6gS7MpMFUvCdAZnZJ6RdOmkYqYMFhS9gjZirtxabX7vRL-gWDCryumUmoc_txyDKj9t4RHf3Qh-lYNSzb7-_luA0n4SlzFaK7unBUMMYYCBxpf1VfntGtE4tLIpbNRaYNCepMq3kPdzLfWcxbrdbzrf1lsFIGyp-ca9V-vjk_ivMWsI_g1xt9BfSs3O2FzjU9tNUe3prv0_2lJu5Qzia7k0B1vGuZMmQjg46QhhPyQ8qm4i1Qs1rLXGu_PS84cco6nZsN3-fsdfVeTVwnxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90c8a06ce.mp4?token=g5C7GiBxLVo448SJlm4sGiYJ-g-9pOVbmVHemNFxDO3c0l_BRtt6uTrRfjNV7mVOz_G6gS7MpMFUvCdAZnZJ6RdOmkYqYMFhS9gjZirtxabX7vRL-gWDCryumUmoc_txyDKj9t4RHf3Qh-lYNSzb7-_luA0n4SlzFaK7unBUMMYYCBxpf1VfntGtE4tLIpbNRaYNCepMq3kPdzLfWcxbrdbzrf1lsFIGyp-ca9V-vjk_ivMWsI_g1xt9BfSs3O2FzjU9tNUe3prv0_2lJu5Qzia7k0B1vGuZMmQjg46QhhPyQ8qm4i1Qs1rLXGu_PS84cco6nZsN3-fsdfVeTVwnxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: «ایران کشور ثروتمندی است. یکی از دلایل نابسامانی وضعیت ایران این است که هر پولی که این حکومت به دست می‌آورد ـ چه از طریق کاهش تحریم‌ها و چه از محل فروش نفت ـ صرف حمایت از حزب‌الله و حماس می‌شود... آن‌ها باید میلیاردها دلار را صرف آبادانی کشور خود کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135957" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135956">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a75666bc36.mp4?token=pr69wj7QXBWNOIFssda_-U4x-pthdxbrrxrrOINcKhJSTnmcnEMCtlBH3o0sV8CVu7pZa9Ojm737iXUhp0k9D7ZBEI44yIomwbwnP8EN-h1F3EinEYBN-Cx2dGHzMn4nuKkyy82At4Iu5z3BmjB5xoELJZHEnXsYc_CxXKuv_1fqjvTacrQjTMnS9A8S61qPoBGPg6Pl7i3_TEMd6CX7pV2hQcatBmVTlBvMnDbacG3RLThAsND0eaw-oLd2dUAD1aK6T0EfVTUiiL6C-iGWWFFILGN-A-nISC49kH--7mCOcqJl6vqRXxli7Au8_1275G4ap_nH-tFfrb1oNys9cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a75666bc36.mp4?token=pr69wj7QXBWNOIFssda_-U4x-pthdxbrrxrrOINcKhJSTnmcnEMCtlBH3o0sV8CVu7pZa9Ojm737iXUhp0k9D7ZBEI44yIomwbwnP8EN-h1F3EinEYBN-Cx2dGHzMn4nuKkyy82At4Iu5z3BmjB5xoELJZHEnXsYc_CxXKuv_1fqjvTacrQjTMnS9A8S61qPoBGPg6Pl7i3_TEMd6CX7pV2hQcatBmVTlBvMnDbacG3RLThAsND0eaw-oLd2dUAD1aK6T0EfVTUiiL6C-iGWWFFILGN-A-nISC49kH--7mCOcqJl6vqRXxli7Au8_1275G4ap_nH-tFfrb1oNys9cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه امریکا: فکر می‌کنم جهان به نقطه‌ای رسیده که مشخص شده ایران — حداقل برخی از افراد در ایران — می‌خواهند تنگه‌ها را کنترل کنند و از آن به عنوان اهرم فشار علیه جهان استفاده کنند
🔴
و جهان باید تصمیم بگیرد که آیا می‌خواهد یک آبراه بین‌المللی تحت کنترل کشوری مثل این قرار گیرد یا نه.
🔴
این کاملاً غیرقانونی، ناقض قوانین و غیرقابل‌قبول خواهد بود.
🔴
آمریکا به انجام آنچه برای محافظت از کشتیرانی جهانی لازم است ادامه خواهد داد، اما کشورهای دیگر باید شروع به گام برداشتن کنند و چه با تجهیزات و چه با تأمین مالی، به تحمل این بار کمک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135956" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135955">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hn9mJQiCMUkckIW1SwD5jkToUOFYo9KFZlAcHw0d-KFMejKYt11ELUmvrNIwpZXF16EjQGVMK1gbzUgUIWRkoj5N9Ah3utzA-W1hhSuZdWWCaAmJ2HOOYfQ_ojomxTaXeueErbqzShajnpdrNrICkbSalZaapAU7cajy6vlias206u4T5ueGKy1D8k5Q9VSF6IEaJyVj0q7pak1LCPxdzQdNeN_Qqmi3OkX4doW6xuvCZQzMbsQDf9x595ySnRrHK9JE9TQBKZISxa6AzuJvprjTc31Mu5i5bfjErfN7zZmzd80ndAIASIcc-CLFIe2PkZ5iRrqHAg4TZw2lGrz7tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو یکی از جاده های اصفهان زمین لریزید بعد این دود بلند شد
🔴
مشخص نیست دقیقاً چیه این
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135955" target="_blank">📅 12:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135954">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a6ff1db.mp4?token=jYYE_UhYpwAhuzkDMIxGWcv_wYD5QAzxhAXJPLxcaJr9FSXxfZrhfex5hsb8bXjkA4U1iwtoTaqE7yXhzhcXGTcyHNk5f772yj7I5q_M2r3zu69Hq6ElK5_pTNLGrOI713lYulV3HXjobhUuQic00Mdh9Phn0PykaER7KR6Fl-VII662LjStaUrqs3lvDybJhGNURfnYUxAK3hGy7b-edguhfxmTTyAHcHpx4BGhKXUjvdGNFRmviVpxF07oAA4fkld7P2fkiB-zrGk2uY-5_VjWb2Ak3YIjVG8ltSFMdReEhzYHtSE8qM7lgWBITYKdw9fY3FbZ-6fn1bMrbuKwdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a6ff1db.mp4?token=jYYE_UhYpwAhuzkDMIxGWcv_wYD5QAzxhAXJPLxcaJr9FSXxfZrhfex5hsb8bXjkA4U1iwtoTaqE7yXhzhcXGTcyHNk5f772yj7I5q_M2r3zu69Hq6ElK5_pTNLGrOI713lYulV3HXjobhUuQic00Mdh9Phn0PykaER7KR6Fl-VII662LjStaUrqs3lvDybJhGNURfnYUxAK3hGy7b-edguhfxmTTyAHcHpx4BGhKXUjvdGNFRmviVpxF07oAA4fkld7P2fkiB-zrGk2uY-5_VjWb2Ak3YIjVG8ltSFMdReEhzYHtSE8qM7lgWBITYKdw9fY3FbZ-6fn1bMrbuKwdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانیانی که تا کنون با برند dior همکاری کردن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/135954" target="_blank">📅 12:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135953">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
یدیعوت آحارونوت: نتانیاهو، امروز بعدازظهر جلسه‌ای اضطراری با کابینه امنیتی برگزار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135953" target="_blank">📅 12:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135952">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سازمان دریانوردی بریتانیا:
هم اکنون حمله موشکی ایران به یک نفتکش عربستان سعودی در تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135952" target="_blank">📅 12:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135951">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2Me5L7yyXUYd3C10o4voDqkDmn8SQnn6_VQFKDYZZSh30rZHqQzli-EVkr45dwd1kRV0RkdgT12BElVPAwuTr6yewC3EeLc9jMwWr4ZrrjpnBnNjoLDi4jlYqIZ4MwqY0oNj8JRrbN0oNtxpyCkTiO9jZhparu9LCYEElbzOuxoM5YV4aqgCOzvBEM1Evez_oF2pA00rnYTaKoNQ-rdERWyHBlASbUdywLkXyNN9HHU8nMfbjZ5stMgRA3__1YYBeM9iLc3-IOA49_LoDk1b8ozNLq8rQpYpIyg4Rp0-7XG2jeBGiBafthu1_UghAGf1khCD1eN0QV8wbysxJ6iNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستوان‌دوم مهرداد پاشایی، از نیروهای پدافند ارتش، بامداد امروز در پی حملات آمریکا به تبریز جان خود را از دست داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135951" target="_blank">📅 12:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135950">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpOnfV137U9DGWq_6xIFWphZxj2iMwI0lU_AiUxhYsFqMVitsLHFYU5TV1jr3pGFZiuJ3wY-z51XjLbsS0RKbzkIHBnjPvRAebieeFWO0hjXZdkf2DYzi-tQYC_KAcx1p5Irg4kErIA9QqDbPpxzjl410bRKud0AYtD2EykzMY3FJ3hZhxOW8hYbuBgcFnu8mRWsOWo3x4OvzwB2KPvZSu11Z8VDxssX4m684PHYATHWSCePAed5ZP-pv_rbQ6HcZgQ51YUB33WGKxPs6evCg72pWr8PdXMdGxrvrL8iCzPdHQRfWb8IC563lCL5MUz9SGAt107EKG598jVVpXkjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
چطور شما حرام زاده ها به ورود حشدالشعبی، فاطمیون، حزب الله اعتراضی نکردین ولی از ورود نیروی زمینی آمریکا مثل سگ ترسیدین؟</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/135950" target="_blank">📅 12:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135949">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
روسیه: آماده‌ایم میزبان گفت‌وگو بین ایران و کشورهای عربی باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/135949" target="_blank">📅 12:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135948">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRQs6tPqLpcxwLH43cB4cLZn_if4Ir4Fv8GUWsaDGcN3jzd1NeKgpAzEAI5pYYal_PCvMglDeqBGowT300RpSFcPv-Iv9HQ0NqagkAptwHc8g1dpby7iKa2LMOg5xPd7Lqzv1CrwU5tUVLwcbU4IsKqJX8x3NBVLGTEzVFwIQZAJTTsmUNXOqySRKLeUUQW-ddVnFYmlAFXjj-o8_veUYg4vw7mNNDZD3z28kncKmacwU-w9ZaH-n-Y-Vy0SGQllNVuS49GqYkXsF4RuwAVR43CbB8-QFbXFLzuzv3WnaQqOuwN1YMJ62MS0ZLzcaEKki4eq9ES7-g34xGSxuxmSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با رشد ۵۸ هزار واحدی به ۴ میلیون و ۸۱۳ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135948" target="_blank">📅 12:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135947">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae713a91f.mp4?token=F5S1EK7P9kXkSbJ8dJkgkBv9bs5lStklbIpozxY4cwV-89yn2cXmkmko3QnAx3LSZfTVwH4uURB8D9Kv7yPHfc0SetQdnlg_IKcqH7spgO4-wsa_2rkhw_D2rgsvfieaMRNuZd2y4KINebLY-DoNhkG9oa8AoCkDR4hNML7MlbtLi9yFmhFy0wBY2DeBhJzQMneyAo8BVKRW2g9fogmnJ4g5hDWaVx_yymLOHkpeM6AurJIAlB6AzQwilbmhZPEsVE5jWtktoclgJjDdcpps3vs5WFqYWGU_Qte2GczVtyrfu7kloqVRBEaoaET0lngXg_zsjmxYkHpXluePa-LhuWvV7b62Pp0uJT6FJOaO_qAYXlYpVnG6ltRARPLqzp4_sB_hQYFpnzqlLOcRZQaqV0DCtQDbWVxnmb11-e9eU2-2lDoMcE-3jz6ps1uC8gU-s5xmkA9L_wEes8iCXiGmCogFz2a8vpH8hIbAOHAHXxePvs9YkBFiXv8vVUI2YRrc7fZjHsQgeiT5nMLEwyp-rOAh-l1vP1B0UdNbLSSIdOvn7dFdzc0hhaesLX7jKCJPbe385PtTT61EQ1XzgzzM55JByXVJa-6eCUknySt8nw1srI6rc7LovoVhiVhRh3hjJ4esioO-FOKl-wNLUklQ3rT5pm2gnaLTK0PCaZteM-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae713a91f.mp4?token=F5S1EK7P9kXkSbJ8dJkgkBv9bs5lStklbIpozxY4cwV-89yn2cXmkmko3QnAx3LSZfTVwH4uURB8D9Kv7yPHfc0SetQdnlg_IKcqH7spgO4-wsa_2rkhw_D2rgsvfieaMRNuZd2y4KINebLY-DoNhkG9oa8AoCkDR4hNML7MlbtLi9yFmhFy0wBY2DeBhJzQMneyAo8BVKRW2g9fogmnJ4g5hDWaVx_yymLOHkpeM6AurJIAlB6AzQwilbmhZPEsVE5jWtktoclgJjDdcpps3vs5WFqYWGU_Qte2GczVtyrfu7kloqVRBEaoaET0lngXg_zsjmxYkHpXluePa-LhuWvV7b62Pp0uJT6FJOaO_qAYXlYpVnG6ltRARPLqzp4_sB_hQYFpnzqlLOcRZQaqV0DCtQDbWVxnmb11-e9eU2-2lDoMcE-3jz6ps1uC8gU-s5xmkA9L_wEes8iCXiGmCogFz2a8vpH8hIbAOHAHXxePvs9YkBFiXv8vVUI2YRrc7fZjHsQgeiT5nMLEwyp-rOAh-l1vP1B0UdNbLSSIdOvn7dFdzc0hhaesLX7jKCJPbe385PtTT61EQ1XzgzzM55JByXVJa-6eCUknySt8nw1srI6rc7LovoVhiVhRh3hjJ4esioO-FOKl-wNLUklQ3rT5pm2gnaLTK0PCaZteM-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هرگونه شانس ایران برای دستیابی به موشک هسته‌ای را از بین بردیم
دونالد ترامپ درباره ایران گفت:
«ما در ابتدا فقط در حال انجام اقدامی برای جلوگیری از دستیابی آن‌ها به یک توانمندی خاص بودیم، اما اکنون کار را به پایان رسانده‌ایم.
🔴
بنابراین، موضوع کاملاً متفاوت است. کاری که اکنون انجام داده‌ایم این است که هرگونه شانس ایران برای دستیابی به یک موشک هسته‌ای را از بین برده‌ایم.
🔴
اگر فقط یک هفته و نیم یا دو هفته بعد به نتایج نگاه کنید، نه چهار هفته بعد، خواهید دید که ما آن‌ها را متوقف کردیم؛ احتمالاً... البته نمی‌خواهم از واژه "احتمالاً" استفاده کنم.»
‎‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135947" target="_blank">📅 12:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135946">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662307f341.mp4?token=JKW9a3inSyxfNweItiWDaqt--eNxkaCeTM8zXQPd9OszOb1ZUtu7_GY5C_uKaMaRX94lfz5XdMXnBZM-bng_kE5pFQ6t9u1Z5v48DNUPqNe8aM9dCzEdvHXTASoyrOsIUnOdVETszfA7ycaOVDlVYmO23_Ip2aB5TpfqfMk9LJ4F40su-0qNSKEDsKUOr3Pha5Gew6TsiQBCBOq53Aa9TSrhkK6zGDO1EIahkQIohLWihKMWZNOkdZHUOVKe01ZUUslTaqnhR83QI5tEHDZgVBqsi98uVe7RfHK0448ySzOU1xbOoXFDFY_VihOsqis0bwXP78aCUCzP3-NDk_EeWUGMH_LQb4R-Wjuw9X-EO6sxJIezZb-N7lhm17FlCQnMLlWAh-G7Pa3dl4P-tTmI5sOjIARlPg4Q86l9_uiXdtdJmg7OYgecJ3HIP5GKdKFyDFNMh3uWOEAFeZu1mXM2Y2CVrUxZtOAHfNzoHRro6U25hLDdnaXGlUNNlri7TBOyxrOJW79hNp1TgjmuoU41mGszft6EOUsd033kqj34xlaVVoeM7sC_E0EYk9SiQ2QTYmWGY6tRdIH9KXCikZtcNBQ2FCvAUTVUcm4aRobKVH_jzehBzJwZI9uPUgHLorMykIn4RaDMVgM1GqYtzY3HCWEaIqXtGtXp0_k1-1R_OYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662307f341.mp4?token=JKW9a3inSyxfNweItiWDaqt--eNxkaCeTM8zXQPd9OszOb1ZUtu7_GY5C_uKaMaRX94lfz5XdMXnBZM-bng_kE5pFQ6t9u1Z5v48DNUPqNe8aM9dCzEdvHXTASoyrOsIUnOdVETszfA7ycaOVDlVYmO23_Ip2aB5TpfqfMk9LJ4F40su-0qNSKEDsKUOr3Pha5Gew6TsiQBCBOq53Aa9TSrhkK6zGDO1EIahkQIohLWihKMWZNOkdZHUOVKe01ZUUslTaqnhR83QI5tEHDZgVBqsi98uVe7RfHK0448ySzOU1xbOoXFDFY_VihOsqis0bwXP78aCUCzP3-NDk_EeWUGMH_LQb4R-Wjuw9X-EO6sxJIezZb-N7lhm17FlCQnMLlWAh-G7Pa3dl4P-tTmI5sOjIARlPg4Q86l9_uiXdtdJmg7OYgecJ3HIP5GKdKFyDFNMh3uWOEAFeZu1mXM2Y2CVrUxZtOAHfNzoHRro6U25hLDdnaXGlUNNlri7TBOyxrOJW79hNp1TgjmuoU41mGszft6EOUsd033kqj34xlaVVoeM7sC_E0EYk9SiQ2QTYmWGY6tRdIH9KXCikZtcNBQ2FCvAUTVUcm4aRobKVH_jzehBzJwZI9uPUgHLorMykIn4RaDMVgM1GqYtzY3HCWEaIqXtGtXp0_k1-1R_OYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ گفت: «هوای ما به‌شدت بر اثر آتش‌سوزی‌های کانادا آلوده شده است.
شاید کانادا باید به ما غرامت بپردازد، یا شاید هم باید تعرفه‌هایی علیه آن‌ها اعمال کنیم.
کسب‌وکارها در حال تعطیل شدن هستند، چون مردم نمی‌توانند این هوا را تنفس کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135946" target="_blank">📅 12:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135945">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: وظیفه ایالات متحده این نیست که برای همیشه از کل سیاره محافظت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135945" target="_blank">📅 12:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135944">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1a0b1aed.mp4?token=ChaMIO8mnW8ocg7xQF5WTteEwoX2ddATNSSPLk6YNl2UrbPl5FQ9Gv9F5LjYVfdkBd8qgBM3ovm6cX_PZAm2HGy9J4f-_U6NteDPW7-chNVVraqyLs8tzMqjOXFn4ZR3gkWA04Tn6-XHBJ8w4qh9FZGsS8Ao_Ulujhvok-Cwdh-veaRFXF8yxUJD-cWVGl9wHo-jKGsiiQ5EvuMQ7cNU-Vq0en3iOMSfmEKR0wsiZ4rXdhFwqKULSJsZR9GKkFxkfbnE9Bi93NpT608u1TupywM6fPeD1smdkYgPwLuNUtZwiJAd7560Kjs0NwWHXnaHlDLSH6IkEqAb3sLYzKjd4ZSskAQKrGwLFvrVfBlYMW1vE9I4fAjrSEXKcKF9vO2Hsy1neklTeM7P0AMUT6wM6ZdfD61Pu8NLn2ZrOia2NE69lPHl5yzdD9G6f13r7U3R0MSMNcGrNFFxZY_2svFCQwSYUVwdp28NE4OIX9iMue47QdgIw8P2Qlj8-cBNkrKrJY4zT-nDjHOWylQKOsjLAKhPD5TFSNcZKECyc--8Imp6xPS0BYLO2E15Pmc-jzfj9Miy8gnu19nGFhcza_eLXNIE6QR2jhrOUW7FyGFSsQ252k2jxJRZtG_NszZZ7yW_QQwyTGaiJFX_YkX10toUBv3YM9_FOT54wkquepLCSvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1a0b1aed.mp4?token=ChaMIO8mnW8ocg7xQF5WTteEwoX2ddATNSSPLk6YNl2UrbPl5FQ9Gv9F5LjYVfdkBd8qgBM3ovm6cX_PZAm2HGy9J4f-_U6NteDPW7-chNVVraqyLs8tzMqjOXFn4ZR3gkWA04Tn6-XHBJ8w4qh9FZGsS8Ao_Ulujhvok-Cwdh-veaRFXF8yxUJD-cWVGl9wHo-jKGsiiQ5EvuMQ7cNU-Vq0en3iOMSfmEKR0wsiZ4rXdhFwqKULSJsZR9GKkFxkfbnE9Bi93NpT608u1TupywM6fPeD1smdkYgPwLuNUtZwiJAd7560Kjs0NwWHXnaHlDLSH6IkEqAb3sLYzKjd4ZSskAQKrGwLFvrVfBlYMW1vE9I4fAjrSEXKcKF9vO2Hsy1neklTeM7P0AMUT6wM6ZdfD61Pu8NLn2ZrOia2NE69lPHl5yzdD9G6f13r7U3R0MSMNcGrNFFxZY_2svFCQwSYUVwdp28NE4OIX9iMue47QdgIw8P2Qlj8-cBNkrKrJY4zT-nDjHOWylQKOsjLAKhPD5TFSNcZKECyc--8Imp6xPS0BYLO2E15Pmc-jzfj9Miy8gnu19nGFhcza_eLXNIE6QR2jhrOUW7FyGFSsQ252k2jxJRZtG_NszZZ7yW_QQwyTGaiJFX_YkX10toUBv3YM9_FOT54wkquepLCSvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران گفت: «ایران آسیب بسیار، بسیار شدیدی دیده است. آن‌ها از نظر نظامی تقریباً همه چیز را از دست داده‌اند و چیز زیادی برایشان باقی نمانده است.
🔴
آن‌ها هنوز تعدادی موشک و پهپاد دارند و تا حدی توانایی تولید نظامی دارند، اما نه چندان زیاد.
🔴
ما کنترل تنگه را در اختیار داریم؛ آن‌ها کنترل هیچ‌چیز را در دست ندارند. باید ببینیم چه اتفاقی رخ خواهد داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135944" target="_blank">📅 12:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135943">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjEiiUaOuTUtx5e9sz5Z6cXyVBYKfTZbNOhv_dSiBOM6_GIXEgImNmeWJVsR7sdoLPELXWVspfgRczvd-qrCuU8vBEqyOi5Hhk4HuL_7jnz8I5TTWA0FcCPVa2bg_7rOdo7-iLcLUrxcoVPrmcSzGV5lP2GIPx1VPi2D5IWBhxUh00BAnsvIMwBtqHWKFWznpeRBHU9Xea3IprJ3DAOKTnzuUsXJ4aE3wuyRkDr548Gzbtl4Ew-v2Ss3cCvyHAF7nYTAGGQOQObgDFLuoYD169sgnGs83uKrj5uGZXW7E2LlnbSfa8mEQ6xpYJrF1Hg4lRSJq-RmbKOJlZp_s6Iapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دانشگاه علوم پزشکی لرستان: لحظاتی پیش طبقهٔ همکف یکی از بلوک‌های بیمارستان درحال ساخت نیایش خرم‌آباد دچار آتش‌سوزی شد که با حضور به‌موقع نیروهای امدادی مهار شد.
🔴
دود مشاهده‌شده در خرم‌آباد مربوط به این آتش‌سوزی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135943" target="_blank">📅 12:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135941">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXXIhfCFL_8PXT1gVv_FZSuHCJIuRAcFrw6JeWOdSDuqHEbpVbouGSMBlfGib40Y2VxjbW5aO3Bg7YmhpqkgO3ahuQKY-18F3Ib9YjkoIK2E8ZTWVYSkptrmUTpgACHPkaCV-qk6ZYKJtm_7XckksXXDPeYTtkS-lsKLBQWQyRrs67w-c1TMo8j_aUtT-Q0EQ8gOR6hASLOB6eDkArQ_gi-LTb5ZPHxDAxZ4xFE-1eQygMqoZUeSAECJpTm-8gaj72j55RXotUpWxXX_llRyX3cowHocALdfy7ECK1JDxISvc6eKF0fSjQnKTxZCkkNygyZgFh_cK5hSVTM2pd6pKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXcQszNckonLueOn0QCVenIHlb8uG9MdHzE8Ej5OXj8SPxDJykzH6JPBpxm5WZm-lHZYknyrrwgyXLyJlmYSyfv17Id4yjbGAwbhoPM_XkzBl0iPYE0j-wRMAnGsfmTOAWduQVYKjMhKZaW_LpaZoAI4H5k_lQg9ye5pGwBnlViqbqa17fZoGp4nYBJFE1S7kVwogVXVsDbYDcRUbGUTG2mYznUptya0Tnb59Ub-CV7l9LnfLIxQFe-HTON5CdFx41kBdLc2_QG5Wzk-EjCYE_3yidd_H2riNhaGV0n_F2QvVFP1HSeZIeYbYtuQXYlqctYgj8WMorbJ2rvniWxkNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کامران غضنفری با شکایت حسن روحانی به حبس محکوم شد!
🔴
دادگاه بدوی کامران غضنفری، نماینده مجلس را بابت هریک از دو عنوان توهین و افترا به پرداخت پانصد میلیون و یک ریال جزای نقدی و بابت نشر اکاذیب رایانه‌ای به سیزده ماه و شانزده روز حبس تعزیری محکوم کرده بود. دادگاه تجدیدنظر اعتراض متهم را مؤثر ندانست و حکم را عیناً تأیید کرد. این رأی قطعی است و مجازات اشد قابلیت اجرا دارد.
🔴
کامران غضنفری، حسن روحانی را به «جاسوسی برایMI۶»، « ارتباط با سرویس‌های خارجی»، «داشتن تابعیت انگلیسی» و «افساد فی‌الارض» متهم کرده بود. دفاع او این بود که مطالب مطرح‌شده را از برخی اعضای کمیسیون امنیت ملی مجلس یا گزارش‌های مربوط به مسئولان دوتابعیتی شنیده و ردصلاحیت روحانی در انتخابات مجلس خبرگان نیز مؤید ادعاهای اوست.
🔴
دادگاه این دفاع را نپذیرفت و تصریح کرد که هیچ‌یک از این انتساب‌ها در مراجع رسمی و قانونی به اثبات نرسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135941" target="_blank">📅 12:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135940">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
دلار هم اکنون 189,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135940" target="_blank">📅 12:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135939">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d6385f7a.mp4?token=dq4TAzQYOmyV75OM-B6u1Fd9UzpvdvVDArHZ6HWPfxtLcWvEpTY8ss_bn0UBDhg1khXLZ-vtwAEvs-aqSYzZSLF1Ghg3UMkuGRf9H6-L_UFBs9eYD80hW_bv8azFdDOWEBgatEmlnktVu-GZOYnoYm9LD4gD70hwbzpCyUkN1WN0RyOgXgkIBpZfeKeahBRWiO-IdD3ZO6y1qAEioXvknksbKM69N5IbB1Icg1Hb2pO-QHGfe5x8S263lNuchFYisjLI0JGjoYOKGx7QUGqR1KUbfDr-ZLBrnJKUQtQviaQ_ESK8_7zISCLQ0GHXYSQ5RQT4RUi7hI7UMUuTRFIJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d6385f7a.mp4?token=dq4TAzQYOmyV75OM-B6u1Fd9UzpvdvVDArHZ6HWPfxtLcWvEpTY8ss_bn0UBDhg1khXLZ-vtwAEvs-aqSYzZSLF1Ghg3UMkuGRf9H6-L_UFBs9eYD80hW_bv8azFdDOWEBgatEmlnktVu-GZOYnoYm9LD4gD70hwbzpCyUkN1WN0RyOgXgkIBpZfeKeahBRWiO-IdD3ZO6y1qAEioXvknksbKM69N5IbB1Icg1Hb2pO-QHGfe5x8S263lNuchFYisjLI0JGjoYOKGx7QUGqR1KUbfDr-ZLBrnJKUQtQviaQ_ESK8_7zISCLQ0GHXYSQ5RQT4RUi7hI7UMUuTRFIJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: هیچ بهانه ای برای پیمان شکنی آمریکا وجود دارد. دشمن فریبکار، خدعه‌گر و وحشی است، اما این دلیل برای عقب‌نشینی نیست
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135939" target="_blank">📅 12:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135938">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بیانیه نیروهای مسلح یمن در خصوص اعلام موضع مهم خود، 3 ساعت دیگر منتشر خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/135938" target="_blank">📅 12:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135937">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a798b7b085.mp4?token=o5wPZmwoWOS_cSRWhoMwqPQe9m9nf4a-d3XsuHddBwPVMcifPckpHlcmi2LJsYCPG58Lwofi2pngkUwCQAddJkM4a8ytf1dYntITMQbnLyvbkM3M4q4zbnLVa3DnQq9dDphV2LFfGq9lkCFtpPaIcfB5K0J5ngLONGQXYh2cLsuSlCQ1d3qpYUzrw7oTxwyiGMARRS8FIcET4PQfvoUShzW6vqphEL5YnlxnSMON6WxdSiWROoAKuY0QJuFNR_bh-zMIZgW6kxPbaxup6dZKkkzY_rKrEA2oTiorRGGCeUjFgsN6DwK1AUkcDo6u_WuCg5smTyYksdtA0gw4_ev9kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a798b7b085.mp4?token=o5wPZmwoWOS_cSRWhoMwqPQe9m9nf4a-d3XsuHddBwPVMcifPckpHlcmi2LJsYCPG58Lwofi2pngkUwCQAddJkM4a8ytf1dYntITMQbnLyvbkM3M4q4zbnLVa3DnQq9dDphV2LFfGq9lkCFtpPaIcfB5K0J5ngLONGQXYh2cLsuSlCQ1d3qpYUzrw7oTxwyiGMARRS8FIcET4PQfvoUShzW6vqphEL5YnlxnSMON6WxdSiWROoAKuY0QJuFNR_bh-zMIZgW6kxPbaxup6dZKkkzY_rKrEA2oTiorRGGCeUjFgsN6DwK1AUkcDo6u_WuCg5smTyYksdtA0gw4_ev9kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فراموش نکنیم که بندر عباس در دی ماه ۱۴۰۴ مورد تهاجم دشمن قرار گرفت.
🤔
زمانیکه که حرام زادهای لباس شخصی جمهوری اسلامی، مردم بندرعباس رو با گلوله جنگی می زدند‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135937" target="_blank">📅 12:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135936">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HscERCZNTLpkqUz_Wla46Z_sgDaWrQ-QrI2FuoEJCByYW6nREOWlUGLenp1dc_VcaMLlcqeuP7iD6iv5GbZv3GXC1F7OF8XmvADaIbA92odbOfCS6olUUvnW8VrbmcbdKy8pYCakauPjCsUkL7fUK3aia4Is-qa2jJpwtFtwiLp37-N5B6LmF_awP2W2m9CE4I8BzG_QdFy5sSbEyoIbfFosqHqMCEjeeSalfL87SRZJrz3fVSZzqEOakAx5yalpoHaexXxAeypkIbwhnbObVmTd6fR8KnaBYzJx7SwW0bDBnHFJw6WSPmEjsY4o5PYOmf910dV_Iu3yVN_vi6RtRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های تجمیعی مربوط به ترافیک مصرفی کشور در ۲۴ ساعت گذشته، که در IRIX منتشر شده، نشان می‌دهد در زمان برگزاری مسابقه فینال حجم ترافیک کشور به ۷.۳۷ ترابیت‌برثانیه رسیده که نسبت به سایر ساعات پیش و پس از پخش این رقابت یک افزایش قابل توجه را نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135936" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135935">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a0663cc2.mp4?token=akpe-bQJSfS4C7X6iLLQtG3kn2SFKcxLyiFvYrfswijQ-rqlIX1HUq37oRfXs1P9l0mLYb0t5J3jLrJ5ylbBYXqAhhBrcDgXqJz4kn91PIfftiRpA-VbFoySyTbfm2Hjr5fpTWeXoeo9iDmhfQ9WXqTjgzbWkY0NMihBGZGiXevG6o2DVf2wgGzryay4wr35f3ta4nGOa3IELAlCwRtma8kxqHb5SI1-FLqz4DrU0_rFAwfct5ODCHtwWhW4EOXgosL3REF6AKnIL5mP9yJFe1Tx8URs3Tasg10cofy7J_g2oz2DEXLBHbb5hvcghQPJMiWCWx8i36o-YPljRLqYzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a0663cc2.mp4?token=akpe-bQJSfS4C7X6iLLQtG3kn2SFKcxLyiFvYrfswijQ-rqlIX1HUq37oRfXs1P9l0mLYb0t5J3jLrJ5ylbBYXqAhhBrcDgXqJz4kn91PIfftiRpA-VbFoySyTbfm2Hjr5fpTWeXoeo9iDmhfQ9WXqTjgzbWkY0NMihBGZGiXevG6o2DVf2wgGzryay4wr35f3ta4nGOa3IELAlCwRtma8kxqHb5SI1-FLqz4DrU0_rFAwfct5ODCHtwWhW4EOXgosL3REF6AKnIL5mP9yJFe1Tx8URs3Tasg10cofy7J_g2oz2DEXLBHbb5hvcghQPJMiWCWx8i36o-YPljRLqYzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایران پیام مذاکره می‌فرستد، اما همزمان موشک و پهپاد شلیک می‌کند
🔴
مارکو روبیو، وزیر خارجه آمریکا: "ایالات متحده همواره برای دستیابی به یک راه‌حل دیپلماتیک آمادگی دارد. ما تاکنون چندین بار تلاش کرده‌ایم با ایران وارد گفتگو شویم و این تلاش‌ها را ادامه خواهیم داد.
🔴
اگر آن درِ گفتگو گشوده شود، از این موضوع استقبال خواهیم کرد. آن‌ها همچنان پیام‌هایی ارسال می‌کنند که نشان می‌دهد خواهان گفتگو و مذاکره هستند، اما آنچه ما به آن واکنش نشان می‌دهیم، رفتار آن‌هاست و این رفتار شامل شلیک موشک‌ها و پهپادها به سمت کشتی‌هاست؛ از جمله همین امشب."
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135935" target="_blank">📅 12:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135933">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71469609f.mp4?token=TvnjbzCkS1Fm4SP6RE8nFW8DDyZIKqy-mnS0zjoyXuj5OapYbVo085OzWLjJ69JFtZ7ejhrTfF1b4bg8wSMxdByTjfC0IbFcDwl1DSAJiz0yurhxWZfPKHOezXMYFip60HM5qigKfICZZVs6HSkH4LU8nBWWYgv7Nw6Jy3OgJoy-UMay-oDm9RK6ozOaqxm5k-LGgkQA-VEuLlqZolymkBprzKtWMIxDCvTIMmpCSZL0ue7dcCqODxRFaXOzQ9Ddcl8Bq2VKpZU6LC76tQPz1Ezg-Qvbi0OsZQQ5-JtLzLOqB4pBUuU-6R2JSMJ6w7xQr6bkhTvuAZx7BA-W9BfKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71469609f.mp4?token=TvnjbzCkS1Fm4SP6RE8nFW8DDyZIKqy-mnS0zjoyXuj5OapYbVo085OzWLjJ69JFtZ7ejhrTfF1b4bg8wSMxdByTjfC0IbFcDwl1DSAJiz0yurhxWZfPKHOezXMYFip60HM5qigKfICZZVs6HSkH4LU8nBWWYgv7Nw6Jy3OgJoy-UMay-oDm9RK6ozOaqxm5k-LGgkQA-VEuLlqZolymkBprzKtWMIxDCvTIMmpCSZL0ue7dcCqODxRFaXOzQ9Ddcl8Bq2VKpZU6LC76tQPz1Ezg-Qvbi0OsZQQ5-JtLzLOqB4pBUuU-6R2JSMJ6w7xQr6bkhTvuAZx7BA-W9BfKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خداداد شیلنگ رو گرفت رو قلعه نویی
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135933" target="_blank">📅 12:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135932">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0kgBq5LBoNYBkTjANwtcWDxh7vf8_JYW7WzbyUFmtihWdWUKC7orrSzDNlTFWOcZaEHntcMeBFqSs5wSAAHr-2OXDk8auq8LYyKqGaxt1dBx54FE-GNWM0JNR_0YojoUtl0gg-1ei-Rp2nqkJ36xVl2sbdoJEeI8lkuyEla_h4Nh7pFs3BTGdC_26aSDeVPfxqA52IOr5hC4pB00OJdpNWLi1AArVNwfdWRE8lv_fyY2ipAVpXWTrx6qi9VEg28q9TfbiGKp2Ar-_Rw_-k5mLLwKflxREFOMZM8QpMwqy04g52NedOL2wr-6lpXFDa4i9E0XDAPUsibJ3V5i_7mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: موفقیت تیم ملی فوتبال اسپانیا و کسب عنوان قهرمانی جام جهانی در کمال شایستگی را به ملت و دولت این کشور تبریک می‌گویم.
🔴
شادمانی ملت و دولت دوست اسپانیا شادمانی ملت و دولت ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135932" target="_blank">📅 12:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135931">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5bf2b8b2.mp4?token=U5sqoHge5ptUqcE5rznDV-N8DuokNAvmp3fsmbHmoulMI4RGuotGJ1woxz2iAJ70m8cyNvHGgEQwja_Vjiqfe9aBBll2Bqoj_x_9gXvXG4c_blvofBrmuZPhlaUwKXY3htrxHZTdbkCCViCM87FGDMACI-bHca5THxwqGSpb845ANmu5di_IgiwjLNrATHOxcFPpcsoU6Xdq0Xmiwf4cZHSf_zk8HHWENEvP-3B6wM93rWw5K7W4xzCRmrMuFJ4Nj9zJhJWxVwZXPT8NPQZ9KCOcRIQ5odMfrwoSOrCZ90UEi-g0gU2KLAK1sLyGPJZlw_58aV3eBDLuejPyxBGCNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5bf2b8b2.mp4?token=U5sqoHge5ptUqcE5rznDV-N8DuokNAvmp3fsmbHmoulMI4RGuotGJ1woxz2iAJ70m8cyNvHGgEQwja_Vjiqfe9aBBll2Bqoj_x_9gXvXG4c_blvofBrmuZPhlaUwKXY3htrxHZTdbkCCViCM87FGDMACI-bHca5THxwqGSpb845ANmu5di_IgiwjLNrATHOxcFPpcsoU6Xdq0Xmiwf4cZHSf_zk8HHWENEvP-3B6wM93rWw5K7W4xzCRmrMuFJ4Nj9zJhJWxVwZXPT8NPQZ9KCOcRIQ5odMfrwoSOrCZ90UEi-g0gU2KLAK1sLyGPJZlw_58aV3eBDLuejPyxBGCNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که یک منطقه وسیع در یک اردوگاه مخالفان ایرانی در شهر سلیمانیه عراق، به دلیل حملات، به طور کامل سوخته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/135931" target="_blank">📅 12:00 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
