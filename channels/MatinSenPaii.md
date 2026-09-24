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
<img src="https://cdn1.telesco.pe/file/CjuJa9ibHKnfijx7V32D2mHz2eGo_Qy9O6NMniELssZYsjKIl4DIai_4eW2cEZo0DwWBHvYoxVHwM8ERTJQHegRQ1IsBNd8iZylvv0lmP39aGyk2IJbJOg4ROzK8MIKOjQ1T8kPk0y_VJFsFkWeyZrTLAcIgpysoh6Ng-dhrfn1LBJmCdmu0MBqmU6Uoe_TgCAb-b8oT0UstjkmiYYc6yZp2dUkLtGFCCu5T7tb4mgCvDRhtP6dTu3a-wO3bTbNJ7VVu-BM0b9F65-DAk5oVQIlNsQZQCedbIwY0cE6MFe7JRrKooAvcnrTepEzF31424xdH1ofkIXmLozU6iLfvGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 04:08:43</div>
<hr>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uphR4Mc7L6eMRycy-EC9_-Rid_w7kEY6ZEoVRGXKdxu8gS7r95DbCGM0v8srBXTZEpatajUB6vBNd3d_Z-bF4kgGeA2YTAQB5BzzPeNG7RsdUS8WNDeHpN8J743SZ23jo-RNLVz--x4gMCr3yrvf4ro2HYHevG0aAgQ2c2rNik-5Czqru0nFZP5n7ZHlOmEt36Lmaeb11jUQ-boiGVGUnYuKQWgpKQb0XRRW_IrlAX_HZgxxAXpzD28tIBbzby8J9mkqV_tEg1u3jYqvgv6e_ztRmah1OeDq1X6Fac76C-ocKxst3UY_efX4aT8lP9G85mhn4otV318H_V10cv4pxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=h0Glq1AqzPqsAMDvXumxkSU69H9j62MS89lsv1FFpieSW5OhOVedB0V-8Fqznf0FvXJ9NfFjBK__UxHV-bmeA--mBqB_f1W4IjGYqWLAL79TBbepF7n7yWGuaEwK20OD_OcXPA7wQ_4i8sH_AtDpMymW7UcD8JEQDqpuKCFn14Qn2rIx1iwtce9xBzM7qj6uAN58E8Mi3H8f40_X8CUIwgTIdUoMcTI9Chgz8011RqmSfhAgrtCerLWwTH5igJjyjfd0JXlDxsrzut0XX0fxTj3ITe6aanoblDVh_x-eWL-DKNrbqjjgSiliECvGxcVpsfxYXHNdP3js7ePw3II6Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=h0Glq1AqzPqsAMDvXumxkSU69H9j62MS89lsv1FFpieSW5OhOVedB0V-8Fqznf0FvXJ9NfFjBK__UxHV-bmeA--mBqB_f1W4IjGYqWLAL79TBbepF7n7yWGuaEwK20OD_OcXPA7wQ_4i8sH_AtDpMymW7UcD8JEQDqpuKCFn14Qn2rIx1iwtce9xBzM7qj6uAN58E8Mi3H8f40_X8CUIwgTIdUoMcTI9Chgz8011RqmSfhAgrtCerLWwTH5igJjyjfd0JXlDxsrzut0XX0fxTj3ITe6aanoblDVh_x-eWL-DKNrbqjjgSiliECvGxcVpsfxYXHNdP3js7ePw3II6Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPL6xB5_jWUUNQJZ360Bfm0vdbmt_RvE3vfyBh9gQxOOnsdYX6Hj4ZQyYYPHX05bCYNR31lEA8TnH9yeFjJz8kSTmZxBvzNBiZyk1aela1on5hY4jBrK8nofBV2QuIpEEG1JiyNZSFk0BxKyYb-zld_R9TVqk77_QaK5vHRLB9ob72GMxRTWqWKePBKVYL3ARs2dhLNk2gjDEmqTa2g1uImQaEc6eRYGDTTbVLAJtSUr_tedxy24qYDKZZw2dFEfc8WVfimawozf_mEUBWlgaJlepl-Vecv-MolHv7JjQAVbZPljXhCTlVEK_R8_lT7j2C8XWgX5V5soTp5JaqmawA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=iKOBgMXkCez6dEsGLUTaHlr61WNHiOdC6aM4OBDHhBB3_U88839OaV5hteDXl8RAXP0_sJDZ6Q0eNBKwRGltXPpRMHsR5OIXYhb4MU7PhQ5LvxZhPEuGLsAvICcW1hZ_2RXmIKoWtltfiiPrlQjLiEhPV-qakZJlUp50BOJ1nIQ0OXTDc7zTW0BXjEASDGI9tCrBKpWbcw2YTfiPy5kE6ELHM1HnwB0ic2NpkBPD3DTLcZMs9A6ciIvilalEzgtjYXZMDw5kjl3nJxCFFvCn6ZFqacSyXY_IrrdifAphz4ta_VoWGOA-p4tP30jr_nTsyBtpwbAYBybrZT6B8YDtaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=iKOBgMXkCez6dEsGLUTaHlr61WNHiOdC6aM4OBDHhBB3_U88839OaV5hteDXl8RAXP0_sJDZ6Q0eNBKwRGltXPpRMHsR5OIXYhb4MU7PhQ5LvxZhPEuGLsAvICcW1hZ_2RXmIKoWtltfiiPrlQjLiEhPV-qakZJlUp50BOJ1nIQ0OXTDc7zTW0BXjEASDGI9tCrBKpWbcw2YTfiPy5kE6ELHM1HnwB0ic2NpkBPD3DTLcZMs9A6ciIvilalEzgtjYXZMDw5kjl3nJxCFFvCn6ZFqacSyXY_IrrdifAphz4ta_VoWGOA-p4tP30jr_nTsyBtpwbAYBybrZT6B8YDtaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ai_kVNVjA7XzX8ndpxz4bZOnCUmeMAF8tHvlByRAJRR2e-RqeiAKSku-Do_R1w1kCk6gy6eT49NJPP0LmL2PuorwYTJFiV0IuITPAFpbxh0KgZXaAuu-ndUlp7IR2KcvZKSKhEJMz5VhE3BdelC-IQUv9NukrzGDWwx-OTJnnH9A-Qix7QrQNT2EDg71zp1fTWAD5qmlB80gIXlOHKevxBUuE-DnjJiefTZXO7J1waykeZOSPTN23BFDzRiI1QXX9GKI-KIwgs9jZzBa6FMK6Yg_uqAQOkxpWCY4Z7k7wzo160CFqS3BmIx8Z1eQD_J7WQ3LiQRlCrTUUeFYbONsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jM3I117Y2L9chEEfjCNI0MVtfoAF40kMixMkJ0zEcSWC8dZX1rURI7LBZTsKppwpcABhynJTdDzG89aS1kZIsIQh6Xvt2W9W8og6V94XF-Jo2EMnOlwYTGQzPXIwTiMe9wyzbFOzDb8D4Z66B6Sz31GMm1jqUONrSAzNLoxAC6fxXRa7vjFtCQLM8RWmCGg5jEPhsy8sr4S9ccwkY6JhQU_J8CTFa8UhSXpLaN771_PM3SyUZHwXdIuu24oshSQ48uXMvsMJw_lBsCdqHXjfwOPXpdfzsnX2pyPPQV_nHK_BhopOE1fwJaF2bgaj45e3O3FCeBiWHAC3hoq69YV0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lvAXUMzWZKPcWoTvRezUvzWp76h4cZRMGKc6ZCCyUDBl1ndULjprlwTQKa8YZQPyQx-6D_htqOSjyv_PA6vJ1KIr6vJHCouuKkosiqanQT8FfzOOV71i9cBILYjV9QIZy4FDlYKppCH6YJ-uXbSJpRJgLOM6hXJ_KIv7T5rCDbVP6CDveqzJkArGJsLFct5t7qkZ030LfKUiso0wwQUEd0OxOWEonJVSH9QsKrZX784H62MBLpalHiDNfgPYDYS3yJShOi-l6qUJUIKvx1h9Dpw46JIYyoR_iDVUEA5GuAjDvtel6TEU5l6qs9jaSGMeWoqT7cEbp_s4u0894xMuAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MB9w3XSFviEGKd7Y1HSg3TTWAP480Zu_Loqwlly3TN8EssAzCCuilUcShYyEXzKFcLpglhYl_HYUfp1SBHcGHD0f311cmhUaW4zQtQoYnSeD3PdhY0nHNUl__O1MZ8Qzq6kMZ3TjRKPpveBW_j6UupuQrlCnlbA5WYgnmlJvqjrpmwmNzZ5TuevlrTj5XymV1gX8yN1GOBGMD42u92BzM0ImhrtxUSR18iZaiBpHc8NlI7up-vDXxLkiprbi6Il_78xlL7R9_bHLe5SxqXdMFlJyW6xWHvglAWfx5GbIF9jFpUCdbopnSTPn6KU-zdCbC0dLuwrB8NDtV5cyBl4bxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gdUYU9HukAlyDxiIXyIjSFo-nItd-fw8SvWssfhFMfoITuQbapQEl7k6gLoCzKK7wSWEzWW2G-mDQTCbNJocq1Ajy6elx1WbofsOIZ5w2rWCer4FKs_4ELZekfgtOUv7gWAfysc0_nQeTeakpPxoBIUpzYAidB4DaOA9LGI7pJkk4xUenBmijFFiELjEtINbCK5bjlzMVyGNr6DDz0CCx7gUkyAoZLtwxViIvdK9BWX0ey65FX8v9Z060CyFqKjBjnrkwxpXZWGm0JUAwnIzBAutfWhqor7p8niCORqMGwJIYyK3XxRlPo9J4PynYbGIhUuD51H6TJt6oiS6jtDkbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kwFyK0Nck7dmTpnagI3W27GtjJADRbKhz7mVZSsOz2WLkk0yPHLeJT6Z3v_XRsq9M66dwWVli_SIp8PEONyS_v18me1_RJO8rzZem-IkDfwjw5SwjI3MZ1FXUY4ItrYEznZlkOijLtc5fjodHfJ2AF4c2Bp_TxUxu_mdO6AxEFCapkSlvVBDOg7XqDQqctYhnz3jXIRCjhg9fxbICtzO5Hxbc8TBslTSLxvOXDNzcqd212BzPRUsEn09_rxuosU9sbFKkeWqZ8Ehq8I1ButRhlz85tToQZROKX3U14vh2O7bpzGcFb5E6EVknwD-V13RUE-nqcp8pfk8aJ-GYPPliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T5zZun_nZ5vIhXjqtC6xKUvErmRjj_ut0tBaGUwSwT72YwBgpWFHD8wiMs2VqtVLL18hUZxeosi94Zm55DlEPxBHRNlZ3H5gujyCh_7djHY5Z5iUuhyMctH3S3JNAkHQOIP2ACpDYwBeLHIwbMk8o3u4oG10l7E7HrwvkVoARonO7uT4BM0LulylBG6rIeyTqfxU2-z7PiP9l1003qHDNb_Z6ef8cg11qzbr763JaBKQv_lX8Kc-QoBEmRhq1nkfV5B4VFg4avOH3w6JqaYAIFe3IM-klLPdZoijxUrc2ErzHmkXMqzF08b9P4fajgSv_2nfzsbY21g6HgA6X7_AAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E8_wRI3ucuXr4N7Nl7dkXtQZkVH14cl7FATpMAPKakmzIlVbjLOOx-dd8ukl915GJ4P3cUiWInm1SMTKwfW5NYWhgCTvCQG8zRVjtMHCDad7cQp1tQsb9cLGmGvpGDHsZsF1nDkS88rzc6iNU9aTIpRSfmbUoDNHfoDqyt6NNdFHmOUmiW9ZEgLEtLgMR6KIPmS2sA4EgAyoyUhnfZXJ9ty7scQ0-AiKc1k36gLYMxqiM4jn4AyyiM9SrZz4q6533fd4ld2VpKkJylfXWf_62OF3HBd8mmmxqBFsk50dA4mqxvcF0AeBDsdDnz06DQ4jZKBSTpO7dD6MLRdBppT25A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev  توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev از برادر کوچیکم دعوت کردم بیاد کمی راجب…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xw-KsWruSaAqQCJ_RJ-XXkmgobW_MdrSZbh0nBpLpBlvId8fO1HtdUXWy1umfAcU_s8jSr-Bf_F5GpKX45jA-lFPoQ3NTDvFQCm3xxZEl9wzXftRzBbRKtFK7Ks_iYWG6HSXTEPo7qxEbPvoPXeI9unF5dsatDrRv_mQk5UrhWptPheBHR2Tl2X0qcqdED9_MqKgWIYt8N2suOm2p-TPaIBG0riIHsJ5X1bzGyHuz71C3Gtypf6rUoWczJK8dydkRnlexfZLF8B69nvgnU08oM8fX2sHmQ7Lg3jo3iPMNcGr6EY9BG9LrrPXYXAM6kPhkpO8ou-w09TAFSXgLUqdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frWaqarSSLqKMAvxJPG8ufjRwj6ou_nmAD6GFqIaqWfkZ8p1U2LEbSx7NBgIDYyzRw1ewn04eFqnv12JXYFD_HWaYg-9JMl7I0jV3ZeAf60OH_pbPfoQYvroploNkj9nUSTmToYxDjmL_vD-RJDfhHABLLBjkwtOA8rcTd2B-7rmvJsm0rMSN7nuRYvunxWmX5gciN5sLozhca8Yp2SbBfGhHhv7ui5SPnGI8S_ZkKhd5jCYIL8TTVs3t29YuFKdgG2Bk6aJWtWUZNzbOlbpI-8UiIIlp-oLtAUFg6LT1gfEJj-VKHH5CeJOW6oZPd7z7ckAR2NgTnq71qogKAJwJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jyOZgDDQckYnOotbtoIhzEOE8X-bv1JYgLOA-tDTao8eMHFjd4PRm0u9c9yZ7kaVM9d_rw2IpHsDxX5HFqem3dkUj18qt46Y7kKLSVfubi-l62Qqy6zCDHzOq1djpKVe1EEjjToxzCEMzX11_ANmX7JAdMGpsvTEgb0yUabGgk9T5b63pikTLmbmpS4Q3nE8ceuapAYQRQoe5RVeuCf344MhD9k_eQTftlo6uLFfEjh8pocVf1ntsZWTRUTeH43ahfGQ7di2wIOpUA87tS4WJuBiBYw_Fv-tcCgKlkmRjzuRf3VYu4cNbA1bZwNYvn-Rn-_xvz0aIThx7E8-OYdchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S3iqWljCXMkB6_nmX36rKR0wndVcNTqbsiblutOv7NSnsFHZBUANhXvLVkVLIRuAWEDzKoorL6ES1_YaTexKoEKkQoqrwQLLaABt2PsO8GXXyCu8KdECVGOg94RZ31P152k0ucprGebNEjrxC-h4xynf67y1klYkCHIjTtk3V6vK1Rdc8-oMjA9AEZaXU_G46oM11Wf_qXbLH8RGRkKhErghR8a8dJqOb3MNUPf-qrdXmmOodJHBTi4jwoTMpH81oRKbt53uEk7SB4U_vZm6TyrBb88IMs8ST2EXxwRio8jzEU8j_GSaUggzffZaSTBiHryPjWmzXxdvb6SBoIrDrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LwH-hNDDsdPqtnNi8BbN1HF2mTwSP431tRR1e6dTIWGUxPGOeOKsSZpQ3CwjdOcX5ZpN3nGh8W1JHvGcejItfdw3stwGIxsY40QtPK-gVLDG8hypqvA_IA-jLxMMowtVZwa5CcRGCGQTT9DrAATPPYQpb7rLVPeaAg4KyDKi-BYEkIn5dOjTwQB3ihHOpTrHdMRhD69OoN4dFDpIgL54cSjNdjSHz87EZ5zdCnWuG0ZD37Ih0Pvwz0LwKSG-9GxzfZ8KiGmOvhXvNT_cMoW-B-PlZJ8ef5ilZzuf8A3I5zu3BRZH-BHCj5TUHGUkjm_gBdlzlkmJBxzNFqppACGh8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی 9Router ارور
HTTP 403: [403]: {"type":"error","error":{"type":"FreeTierError","message":"Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"}}
می‌گیرید از اوپن کد، علتش آپدیت نبودن 9Routerتون هست.
برای آپدیت کسایی که با npm نصب کردن، از دستور
npm i -g 9router@latest --prefer-online
استفاده کنن، و کسایی هم که با داکر نصب کردن از
docker pull decolua/9router:latest
docker rm -f 9router
docker run -d \\
--name 9router \\
-p 20128:20128 \\
-v "$HOME/.9router:/app/data" \\
-e DATA_DIR=/app/data \\
-e JWT_SECRET="change-this-to-a-long-random-secret" \\
-e INITIAL_PASSWORD="your-strong-dashboard-password" \\
decolua/9router:latest
استفاده کنن(با پسوورد و JWT دلخواه برای JWT_SECRET و INITIAL_PASSWORD)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FAt0XWpClB7slKX1cDllFbkYfHfl4P8fmFSOBWUOMkmI664TIpZAZs_AlR9i3-SyBJzXsxc528yEK11BjRveYCLjm3nIDJtfNqwZgrn7P8k823n79x57h9-xsHL6KT70XhZNFrN3T97cOKGGGyVEqxYspJ4kFJvFB2xPskaRuwq8C5HZQLc7Rqxpe9ferNV-5gwAg4A8Q5AX65izOUWUWArjr8yWzGbg2vF7E3XdQYXT_FSgkA6aEVM8e81vvChOXp1LxnePNapsdG55_veDp8ehQXY6WrJNSq_A30mqMHWmBC_J-qxzdWhDAcelQLjIysnGYFUpqs89xltjrYY1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dHo4LKiXZqLj2vvfJXrNL3we_h-7BFQNEGWLrjOdsv5i3tV4T6s3Ey_cY1dUiZo9uF-j9Sl-6gCzpJNcR69efLPu6UYFfSgDU3f7vz652WvqdSp5vrdHu467pDWFrKLMgkA8sdWtnLS6XAHA22f87hvsR3PL0B6SpZgA-mWE9kSqBwJH1_siIDqbV1n7NNeVyB6cTJ832efNKu2I9M4oIMAYRk7qVyoNsPHOjO4QZxxs72LI_UG7kX1km2Uc_X2LdnMEiUnMm91Os11bV14WU6UBTP8-qUWlhlShe3YowC9dfwD2MkHA5QVbfQXc_SEP8afsBERgfiZP6MCA3Cs-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev
توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev
از برادر کوچیکم دعوت کردم بیاد کمی راجب خود ماینکرفت توضیح بده و کاری که ادعا شده ai تونسته انجام بده.
همینطور در مورد Jev صحبت می‌کنیم و اینکه اصلا چه نیازی به این معماری حس میشه در کنار LLM ها؟
و می‌ذاریم ai ای که کدشو نوشتیم، ماینکرفت بازی کنه برای خودش ببینم چه اتفاقی میفته
😂
لینک سایت Typesafeai برای گرفتن 5 دلار اعتبار رایگان:
https://console.typesafe.ai
لینک سایت هوشیار24 برای تخفیف 90 درصدی API از GPT 6 Astra:
https://houshyar24.ir/?ref=B2N4W9SS
پروژه رو هم توی ویدئوهای بعدی که تکمیل‌تر کردیم می‌ذارم گیتهاب واستون
🥰
📹
تماشا در یوتوب:
https://youtu.be/l-o_fQM_9AI</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مدل
Grok 4.7؛ آپدیتی که بیشتر ناامیدکننده بود تا پیشرفت
ببینید Grok 4.5 نسبت به قیمتش واقعاً مدل فوق‌العاده‌ای بود؛ سریع بود، کارکردن باهاش حس خوبی داشت، قابل‌اعتماد بود و به‌عنوان مدل پیش‌فرض عملکرد خوبی ارائه می‌داد.
مدل Grok 4.6 از نظر من یه قدم اشتباه، البته قابل‌درک، برداشت. کندتر و گرون‌تر شد و برای انجام هر تسک، توکن خیلی بیشتری مصرف می‌کرد؛ درحالی‌که فقط یه برتری جزئی از نظر هوش داشت.
البته دلیلش رو می‌شه فهمید؛ بالاخره تیم سازنده باید خودش رو توی بنچمارک‌ها بالا بکشه.
اما بخشیدن Grok 4.7 خیلی سخت‌تره.
1-
مصرف توکن برخلاف وعده‌ها بیشتر شده:
گفته بودن مدل جدید توکن‌بهینه‌تره، اما توی استفاده‌ی واقعی بین ۳۰ تا ۸۰ درصد بدتر عمل می‌کنه.
2-
بنچمارک‌های ضعیف‌تر:
توی چندین بنچمارک، امتیازش از Grok 4.6 پایین‌تره.
3-
سرعت و تجربه‌ی کاربری بدتر:
کندتر شده و کارکردن باهاش دیگه مثل نسخه‌های قبلی لذت‌بخش نیست.
4-
هزینه‌ی واقعی خیلی بیشتره:
هزینه‌ی استفاده‌ی واقعی از Grok 4.7 بیشتر از دو برابر Grok 4.6 درمیاد و حتی از هزینه‌ی Astra هم بالاتر می‌ره.
با توجه به این‌همه تبلیغاتی که برای این مدل شده بود، باید بگم واقعاً ناامیدکننده منتشر شد.
البته بنچمارک‌ها همه‌چیز رو نشون نمی‌دن و Grok 4.7 توی بعضی کارهای مهندسی واقعی همچنان تجربه‌ی خوبی ارائه می‌ده؛ ولی درمجموع حس می‌کنم هنوز خیلی به مدل‌های سال ۲۰۲۵ شبیهه.
مشکل اصلی، قابلیت‌های Frontendـه:
عملکردش توی کارهای Frontend به‌شکل غیرقابل‌قبولی بده. قابلیت‌های 3D تقریباً وجود ندارن و مدل دائماً توی حلقه‌های تصادفی شبیه Gemini گیر می‌کنه.
حرف آخر:
این انتشار واقعاً ناامیدکننده بود. امیدوارم تیم SpaceXAI این موضوع رو بپذیره و توی نسخه‌ی بعدی بتونه دوباره ما رو غافل‌گیر کنه.
✍️
theo</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kFLRtfg6LQsErXTbMIedmqr-T7Xq_9Sn5ssY0_IstV0hVmCLAMsjPzW95-OeTk3n-yotDYh2fiFE98Y_6gBZ9Ip_bfUrhs9sQ5cihQcg1AOFRhNsv_mjggBXM4xS3rQ5dq9SqP-DgGb-yBRWfzlpiwuxxv-M-n579vNC4vSHp1higz5KZ1sU7VebrT2o9BOQH-fs5pK3fZxD3-afuk1mRY475jT8k750u0buaHltc5qK17LslpBKAIls0zt9gTbVCiFQkldONRNyjPeO3BzsI8z1_7zxHUwjc-bVjuiLn3lmoQCXuGFvm4woXGrmCROxfzuD7Ir372v665zWnseNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZZvaqRlZzAk5ZxH3Lt958yFghQEAQrV6L7aQhom5dk6TBjnh9Ctk5nXUDu78oySqbICkGe_W98SNN6g3vAfPMcH2JHRu128yo-4pLaPB9M52jxGbPC6pXldf6sBYBdt9Rik8S0jlIcLW_MsdRLrwON_EGzT41ICd44vY4hZoiafntDejx-XwwqqGj4gCsqbCFIZKm8aVbe_kiwbFF2l4266bWir7hCt5yT4C_2ja_QXeR55ugILYRSpVmJtBZqeK51MGzxl4JfS_WEk33y9nogaDnKF1v1-E55cVLknzorxkInHIYPwEjcxUsP8nHSfbHQnWLosBjZ5xHKIaclhHEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cfK-6iTdmuX6EnKDS2QDugKFGxHupVNsGDT8bmg7JfRa-FsWM05UzYW0BhCQhUnaloo6J0zgJqwNjRTIwueLOKSutIFxEOLqxchOB7B2LcB3vqu01pcva6nLHTQGhNNfzBbiVdrqrdAphGY_NPtFOGdWx1OpSvMzcvvSMgSNcCtzQh66exnB_k8J4MytHrsiIiaM4iGJc0KLD5GdiZENk9_yEGJwjbc20h5A5ge73phoQiRHA1sRMhkiRQCY_8e0UmY-0gL-_T6_TI08WNEuPFo5MTW8zWZtny-uV8EHlsfhSHv6i5Omzcs3aiEgMS9N6HUWwcX4RzwJhJyS1qqLYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-JklT-o1Xt9i6u7mSH6UYx6GFkitm63qq9OjVpYwBsxsqyBJQH-c3kgZ4mA_B-YoOsht_3N1nWtYSCE7rPEcr4b8s2wSakMnlwRMC3A2Qjg10slwATzbxlWfJVomnzN4SoNLqMZBx7Zy775ildmVpb6UxgOxfns3L6eesm4fqve-7qQK2lRnyobO1nwb78c7daMYbMCP4iOW4EYHiWUY1u8LbIzJfCcRidHW2MEt455mgpH8utSl6vcHWna2QmwdTc0wIGynNWgM9Nq2l1KqKfEFJBrLDxwfLSbERHYyfv6HTuKyi1WjdennR8t1ASpjn-XLwXZa90FadlKlVEoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e0Z96A6q9Bz9PRS-y0mc-tNYMZyS63GtKHQuaeRZIp54mz4pOj4WL8duIh9MjYBFUdySXJyK09cZLHEzUuula0_IduA4qkSFv3Tvrge6VB0p-ujkJI9F8_W0N6cg0Aa47_MFhBWnX5QPkUC8NeH_E55s6_xRjk4zCACZRfIszKEKkZ8y0E2ZTVI9Un3BLsxQ6g9cpYs1TMdTKFE2VWSQpTzkhbf8aw6a487XCKn4NI_p0uE2NUdj9TZstce9YhQ6LCAGkt0aR9nmae5UaDu63u7TfucVm6JFnurtdNxfkhloOXwn6EeSxdN9yEaRHKdnpzpNVuzTsTA90CKggZQyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kn79wDUciEAhkLrJbDp3vd1cS7WwNmuEUe9M-MZHlXEyFUkhZmOYzpEFGSbKQmEChvdGxJNc5pzOV0HCQBfxdGcWdaq1Uh5Kdrn1I81fWMyKj49LDfR9eeIr_fGnVTWa3vlugYOBBMHyAQssiHMt8nJTZbLmG1WBRMKXCRtB2Q9cADtNXKZKGKHRrn1yd5tw92PtFxR4tsnxhC9QfmD3mh8-YTaqaaWpkQ9vG1_WG_tEmSu8qmPGRNgEZ-zXU7idvxcP7GPgEkOMpSd3KWkOtn04Wn4wr_scz48QFy8aXteFIcViL6VkctxjRSW40wgIzyPAi_Na2Rxe0VKXvTGT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fgNj2FE_7zJEkeMwS8cvbdeOb31Xt1G_acKzD44V_E9oiEWkz7ufLuwFkhOIkya8Ngjsu-TRiu3VdudXG71_F6bWzaPVTmc1x4jYf9Gl35Eg3-PJiq_QoDETo3TQMauHySf7s5acrbONEX2l6GD5LVwwzeLnWkgAYx4aEnHixTpkCsveoNxBiC1N9uJs6cYVUEAyPvaRHkcctnSgGnXKfBC8qSf7kM_oaUNdqm8w7umQsi_sAc7nS0muEuRFfdpoPU6N75PxgBBN4YxDZUlXymDpmlH9LK38cwNoQ7aNjdma7CEW_aMcm_lTrANBcbzYoqBxP1VQn2xq2bkaf8X-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uWDzFnPKWT03PSynpqv8yOhMJM--j8N5dFx5U04fTjf0fE3DjA6mKRQc98n3ofHU7j62PdJnC7neQ6pffzS-Ca6Hc1DnmDUeC1aOFR2KiyGm8RZwTwAg00Qb25OoUZX0-Q2KJu8Y0seg7IXlGzM-86nDxtuzms6IzMbZScUHQBmViePuKawEEtOpynW-YIo0SXZtzbHVGu6XdKREuSb9LDa0pZ4of9oh2CWkEHbVdEjPbJGi102pbi-oqY-3K7saVaH6HvCv2TvdFjdt7tRHqg1uvRf7pW0MAVapD7rxLQo5mg_ibFF3R-GhjFcX92yu74CDc1I2hU1G5KICrIaLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FEgQwl46R6s3f28EEp08hdxqoIWW5qr4LkjIb5ePzAIOHYIZP8VAA3QNiukvWWI4eJVKNQLGt7iZnTwEUz7P-8AuHcO5UM17orP3HVJK_23mHjXITUWXMS3O9OYo5ON15pWRw2F4yyFi_otKMHfYvUaEWYFgxJ3dRU00GvACLSPxUCtJvvlNmRvTIcVd-saXJ2e4EyMet__UAgwDGm7vYpCxEigO_d-kqQBDag4Me10iVSPUiVugW8mQHoykrLA00UYk7DYt1AospssAHEuZdsKsT261DXwBtbvAIa8NLn8mNELHJSf51QecX66KxF7H6feG7SHildGafXZbK51z_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PuvctYMuCqhXF_0nhma1p8wAKepvjsELBMohoyiJ8cwQB5mHN0C_cmUch6N1bqH5cfmHhsfW_Hw7fm-O576yGFKeAc94iv84PwnHA7VvUY5mhFS7bwaR5EhQAmnOeuWQGJMVGWFwkfAVR-AtjEZZFa205CMpBDt9NVuh4DWKmuPyaYVhx30jtAeU5dtUavlLE3cMGRwka3yNATLcVELuAZAidf46WHLTsdY63mdjoainO32g-wbwh1poWfhwgK1F6MQH9ttszkVaG36dc78pKwY_h_8OLDaBwFNQZgru4_MvXnP_ELEJ8sHo0tXpuGphjWURlp3NY4OD2syWSzW4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه
هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن
به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم
، سعی کردیم با
یزدان عزیز
با استدلال و تجربه‌ی خودمون به این سؤال جواب بدیم. چیزهایی که بررسی می‌کنیم:
— چرا بیشتر بحث‌های این حوزه توی شبکه‌های اجتماعی «حکم» بدون دلیله
— فرق AI با یه ابزار ساده مثل ماشین‌حساب چیه
— تفاوت نوآوری (Novelty) و خلاقیت (Creativity) و اینکه AI کدومش رو داره
— جایگزینی شغلی و تحلیل آینده
— چیزهایی که هنوز دست آدمه و AI نمی‌تونه جاش رو بگیره
— بحث کاهش نیمه‌عمر مهارت‌های تخصصی
— ۵ تا کار عملی که باعث می‌شه بازار کار هنوز بهتون نیاز داشته باشه
📹
تماشا در یوتوب:
https://youtu.be/x8V0w3I9g10</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcgrSzskwgcGtqjkmisIEJYeVEuIQJfAcJGh-krChZzTHq5meRTdL4WTpPwhCLjTH9Xj9jjOGkXyTQBGig2aZAjYh8tSYFa4amSaAhKhmZbuYWQ7Sw-wyXTyJYUfxo3fw3C2e6Ag_7CNdGS1HXHzj6UXiLBYeNEa9gEa6_Yr03w-QDrHuP77BOUfWA62H13dMSoWzKNlnIaHy-Zh-CkqRTL4d-wbLU2EUVS9fOaKw6rNnbIZE_0zU6L07wMSfFuvdKa7CL5Idtk8Z2iRiaICN1rR-bdQDMzKe5eCaXZgTNaloGhgGsTz-S4o9fUWz15Trj86Jmh7_d60zxkjserzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=keV5Q3gnENTZ-ZidLgrwvXYE02vqCQyEoEVTqxGhkYkquq2nbyKlnx4ILETLPKVz7uJ5m36VEh_gETl3wjNqQy2qbUPCMLuYEJ_Zxx8bGjYbu_msrZ-3RdKOGjvKh8LLhsCrI4vfgme1B0R_XlO10ZTCetX3W49NVdhtKGxMAIKAYWOzfiCrVl4Y3mdkiR8ehlvFMGEavUnteCGfYqqBcvMxtqfP-PyEtT_XsQrbFOs38aIQnE5fPlK20pm5aFC50SV79-p4WLbGn6ZW2GJdghk83Rnke3nRjepcc3h5c_jw_JQ05mSxhUULRny5EDpEw0j6-PXNAvBj6pSfdvzV7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=keV5Q3gnENTZ-ZidLgrwvXYE02vqCQyEoEVTqxGhkYkquq2nbyKlnx4ILETLPKVz7uJ5m36VEh_gETl3wjNqQy2qbUPCMLuYEJ_Zxx8bGjYbu_msrZ-3RdKOGjvKh8LLhsCrI4vfgme1B0R_XlO10ZTCetX3W49NVdhtKGxMAIKAYWOzfiCrVl4Y3mdkiR8ehlvFMGEavUnteCGfYqqBcvMxtqfP-PyEtT_XsQrbFOs38aIQnE5fPlK20pm5aFC50SV79-p4WLbGn6ZW2GJdghk83Rnke3nRjepcc3h5c_jw_JQ05mSxhUULRny5EDpEw0j6-PXNAvBj6pSfdvzV7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=DDOjM9CbeJ2WY6PiqFsTMSvm9Izwty8ChYk4TiPt8L2hxKptKdISIV_LqlKs21ykd_jSS9BZUFluqtgp9yI-kqkEeXKe2hZ3JU8HnSbZN1yUH9VuQuFe927O555Gof7dgjNdYngrMUB83kBhaOqQXBJ9difBOCSOSm3kIe8wbEf4EoVscus_9wIuvS0BbqkhsvxhVqup5aQrzaXcNv1fYYrIQAyMaGdxZL-ptVgn74huTqOXVK8FcInuf3gkffIyeBZzI3MkDsvr8wpq7QD39AK321wvj6YdRY9arbfwAjj8IACpo3lqciVuQW5CX5tE79FseNt1A5S57PAw1bFruA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=DDOjM9CbeJ2WY6PiqFsTMSvm9Izwty8ChYk4TiPt8L2hxKptKdISIV_LqlKs21ykd_jSS9BZUFluqtgp9yI-kqkEeXKe2hZ3JU8HnSbZN1yUH9VuQuFe927O555Gof7dgjNdYngrMUB83kBhaOqQXBJ9difBOCSOSm3kIe8wbEf4EoVscus_9wIuvS0BbqkhsvxhVqup5aQrzaXcNv1fYYrIQAyMaGdxZL-ptVgn74huTqOXVK8FcInuf3gkffIyeBZzI3MkDsvr8wpq7QD39AK321wvj6YdRY9arbfwAjj8IACpo3lqciVuQW5CX5tE79FseNt1A5S57PAw1bFruA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bXcCCH15WmAg_N4QprqOgMTXxqZ6k9BO3VFUzNfPZPGZ-56XL_sfLNGuzOB5hIM-bUmtfetalUwAQQSP8xE8bO3JijfMTzA_YuIVuTQ4lOq-_1Jsx8ANaffAImbjJGnpJASepn4SsQMNNC6SXVmHfAGEzsCqrcJ6VCUHABdJZjYKNlgvwgTk8pzoFR74QYUG6Tr_wNbpj3uXgrsz4sX1AiKJNY-SCcbMCpwW77YrMB3B1zQKkTvoEJ8HSrx7z7cEc1D2kN1pSpLgiIMeFYhq-q1KCtppwODgbDqitjUqB09Sxsb-A8nJBGNdbibWoP-kzU4lbG14ufwcsWr5Dbc3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iL_MSpzxI-k-vLJG0SaC6KZTQDdj3byUxEHWNmtTRCrX1WYHCU7hTbGWhqaO-wBpDgbtmTWlhcJCmYNt6Lnfdzf5brhVaKCc6sRqH5bDpsnSyFWidPqJWS9rmyTOPKdnHmG2sMsWq44yFZ4Ysu1BuFQron-Mp76PueA-WUfYtavE_jskGXufvd_pmKGet7wbNleO168_G7O-pcJ51BjbNmpUFQ3lSM3iImmrf-liU522JypZvdN1K1LA_KxRogLPnFWMFvpH8Ok_T9tXGXTHp1Y3H6-XxWOVscX4RaALJ1rZxFZyaMFYT7mVb-VILchF2qQALtJt5rVn-tyqI_0_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=AjNAQQmpURj_x8jS3CqC58sGysaWo72hmgxwHxSPjGEnPlEugY9bvioP6mVW-zUVIqG3vW79edKWuwKy7SqyZ-bdj1brMupf0FLUZw2tUGDyrmVAZNt0fCqyBhgZOj5iRrtJ5VtiL-L3ADiIyCRZtgQqETg2nP_zweZpOiLEqbDPRQg7HazLSnhEutOsJU4BMoconaWY4KwJ8kaDuPMb52J4ncf0EbrwavFenOFZlrMkKlXGIqBb8-yzWxTSyRd7TRL6U54rdrv1e6nH2sFPTxYLStLhspGfN5CwP3P7eK2MnPKeAbSkSxXBoeeiwuWn1U0FZEpyhFpjduUxElL-Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=AjNAQQmpURj_x8jS3CqC58sGysaWo72hmgxwHxSPjGEnPlEugY9bvioP6mVW-zUVIqG3vW79edKWuwKy7SqyZ-bdj1brMupf0FLUZw2tUGDyrmVAZNt0fCqyBhgZOj5iRrtJ5VtiL-L3ADiIyCRZtgQqETg2nP_zweZpOiLEqbDPRQg7HazLSnhEutOsJU4BMoconaWY4KwJ8kaDuPMb52J4ncf0EbrwavFenOFZlrMkKlXGIqBb8-yzWxTSyRd7TRL6U54rdrv1e6nH2sFPTxYLStLhspGfN5CwP3P7eK2MnPKeAbSkSxXBoeeiwuWn1U0FZEpyhFpjduUxElL-Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektCtmwCHrh54Xi60kLtmbTZGgdWdyWXbdZ2tGKEnW7JhFinLoOwn30I2saeULzISOf55qVUqWgqpxiq1GhHstWbvuMaXV1KeGaR5xcTiFk26lHyFKhmiM-7yQ1fj8OLygSSz4mpw2FbWD0bKloCLDw_UPijBo5q9wQ7SM-LnFu2h0a-UU-5L0BRmgPSWc3AuvaksgqCyK7j0wO-vINg5nzoO2RVjEqTbnFES3nrFs5hzXWDSnpvkhLykwL1CUG0KOQdfqLs0FM6xXeSnYkiyiRkQjjyFvfr6875vQPyPRBhth-IlTKsrqgyRIOusYmi8SgqnM_LLYNz1Ml5Zrnf7Nz3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektCtmwCHrh54Xi60kLtmbTZGgdWdyWXbdZ2tGKEnW7JhFinLoOwn30I2saeULzISOf55qVUqWgqpxiq1GhHstWbvuMaXV1KeGaR5xcTiFk26lHyFKhmiM-7yQ1fj8OLygSSz4mpw2FbWD0bKloCLDw_UPijBo5q9wQ7SM-LnFu2h0a-UU-5L0BRmgPSWc3AuvaksgqCyK7j0wO-vINg5nzoO2RVjEqTbnFES3nrFs5hzXWDSnpvkhLykwL1CUG0KOQdfqLs0FM6xXeSnYkiyiRkQjjyFvfr6875vQPyPRBhth-IlTKsrqgyRIOusYmi8SgqnM_LLYNz1Ml5Zrnf7Nz3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y_yFOG8p5L85mYDEslSoASTJfgZsJJTtUfXisBR1s9gURTGzCWXmXdCLbeeQWdTFFBgjTtUl2JJTAPMzHVbKhgZ6-FflKB6XR4Z7vgLtWbwORBGEPF03LtaVsLLAXpMImXjXWbtQczqYFPuwZ5bgSXlNL0ZVQvOHD7gsyZ_3wdd4beVbtciFJ1k0QJqgjgGRlpg2cmc1hM_LcdQLStfcVuiB41ZQvjsLm0kFWYeAYP9D1RMnSFrD6bNbSZnkg7a5z0HyW2EmWRC89kjxYGfMg_lvOO78ihK9F4InW32AkJtKhh-6tzOgQZ7kN2BpvmiI1dvCH1a4hftwWFluNnP9uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bqp3DrwWXANxrl0TGqWn8Cn-tpuYmDf4joquAtIIYhYsf2--9ca6py-mFqni-8NDzHYNkr5himwZf16LGcFL3mQ_1kaklKQhAw4A_HxhW4Q6H2SeGMWGj6EgzayrJcgMxP5Mlb3MmzELrHVTeMy2pHK_vjEC7Fb6WaN-W-nYwAQU3yzwlFhwph6ky6mCyt733jNfI0ydrRUzBbq96f5ibYAye7IQ-ilwUBeEM45BhNop6s-P6xl8NiqI18T6JNkgc1pzNiW07rWcXGEShgbqY1YDrxl1C_nAEkePHrpKhX0Y8Zym1Nvbq2wR9MVHHGWchRt6IJNlSRaetvjm_DgGmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sIFWlQEkXTLVYr0Sj21sRH_jMr7yNJvtL6b5nMC0zx472ANj6SqJl4XEcXYCXf0V2kNJNZs3IjugADvsb96TOcvUW-mYqkfbITqahUNKRSJRJqvufr6T8kgZGrgeJjVwEG45fAQcC317tc0b6_cP96NspSn-8tzWxtMkOyn8uLflHe7Lh3uNIZmXj3hkQs0Nkxf1Dqp4wmm6_d3lfA6hfjdkVre6BDUkBztsKgLGg4e3fX8dwyssWX_26ITj1EK2ysdwaXYC5U5rSYKunC6uFnsoGbmwrSQ7FcKefx1wrCVuGgcIihq_VwJ5LJWYsy9liz0Nx9JAH8U22jwXw_W10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iq_zlK386-dJb5fYgk68VyTo-kOlkrPSsLC1K7HR2I59sf3dhkVlNt-kg_unoy1rNYqs82BxrtUe51BUYC9ois11RPHOeFmwMk_HQJJTeMiLyIyVrhuXzsD2YXcdM6FsZKrCx3GUdxaIwHJF0mgMG-6gjOJvSjDWYsznWzAm_W3IUEY592pWzrTMM13X1IibAA4-4w6o2ghnh8W7A9KqV9vXNMMYyjYTcs-Nzc0IvckHlYP-XXQTuBBrIJuw5_V0DR21UFbP5xUHRJsbHj0CWu-YExOrMH8JqHsN1g5dJA3m1IPZu1TIvc245QdQFWM7665mj6CWm23-wvmA-x1zPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IJhOP3xvJJJfd7AFQ2dTawvJWApWgfu6eQIlyhaGkciQHPo256UuVNB4JpSESJNzxUUkEOClTuO6bngPd60fe6icpmwBFOlQSioJuxFcmp6IccxsEUDkOgvMAdnQP-XF5GiuyA-PAbWn8RN7kN3rsc3FoRkkXweftL0S85odgXLM_Kfvkd7QrTOd6q9mB6Y-iieA2YGhdfhX0PfYB--jagGNC4uO4eKlE2qQZ2thKFK-HMoMvzeUYv4TTKgjZKh01a2x5fX3cdJO59xFYckZhs8HViTalqNN45G-JWCcW8sBGDGPQo7Pbu0gguafr6B8LQNzanwhnxXPmt8Wy_mRSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EngWBgrqnf0OvvnKjf8WdT79t6-DWKZkpjBhdLOCN8YIF5tchEo8k7DVA5V-56WCXxlN32SjpSgVDzJTQ6l3kF0lN6PZH4JUuA7ZGi-GeBaQcCvgsGjorfz3rikiIh3j-m9VElrS5--Au-VMldsqtkqwrsOpeNZHmNPg6qjQklSkCLdd0QwZcY6OqMZ7s9C0PA0WxEd_HEf2KLRFoAhxOEQHN22oJuR0_yROpAtCBGplDQ7R5VXNnfj1ArhhuhUNDJBrt8Ks3g7yP-zPuiaoWJQBLttZriEkmFBvHDG0lI4o1gSvYaVPV6_8Lo-Hc98ST4buy0JDzSVc6E8RCMcHew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XwVtrNBJ4xEBe_uJl6sTESILaJUKsOchj1eP-J8pq_iZB09Aj18geAAkrB4u2Seq3tprYxnBKaf4z9XvyxjmJc_bOzbKJiIwAWyHNnMGL-bZe7J5G4GqYK4yMTRRlIJWX6hM1Hw5ShwH1nxdXgOVArYGPQ0tPWwZei57FsOV7lQg49X46cAPE4XIkI7x4y6SQd9uQ8pWlNngy1nnbmLVAO28_X9P4ZIp1-vHs3JiwHzzu3X75WVvXvkDEfByK23BBdF_Kz49MjWvN3RLtxFsw7fLGVyCdmeLP0xxX7TfrgWtLG-MwfA4EKjZBvaPz8bycvyj3koKb5mxKEsxC-K22w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i1uJIIfc3A64yDJzAIv8pDkpt3lqgjKHSGBPcRZHbpf-xrwPZXXkU3cpXA-WyQ26dxv2zcijKZmUi8tDFDoEeLUTFkyY9Ir_E9gvlkpEOfs59KBCwX7xS_RVJf2my0_CvAFJg9XCsQe7oa1tjevtdcZy7clZjDg9uJzNMT4R1i_PcuBgxz1rEnl-phM5JCrEO_uhEZQRyHvAw_OPLmmwWMAP0yF7_z9NzVbrJdxpLm-g45NKZWGMbfdMrcjmeF85D9x_GeYUXAY1waXUYSFA1LRsd6mimWY5ySMqee65iyso9NJ_kAHjYX0AnG0KE1rqPMbMGgXEZYv924lbekV4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PTE_p53gz0I3HfH8ihqjJ-6Z3khQwcFLXFcwXC1e5_46UJPg3Cydz8Yed9cVKwI3-8rGqgR38Cx-MWlMEAegFG9K6MKnHmpTIDmNZTIwH7IbXtgXLEmIro9U-hd0HYJbmO30U9CThJwDRy8xn-BhUf2KZ6NuUbE8zVxSBSsNQQfXf9YXAt5bnjHv_xVfcscM5-6BS3QesL3rVVd2Y19Tsfk1IWmdysIXGtMWnw4YrvxiEddQE_rJ1bCaaYA4B-6BHXA_XUbMqMylVcq-KiAYhBe5UVdEvTDCw2pb2n6JNLmT_-Qzd7r55k91-dKOt_Wee4WS8ZEUjrr7HaDvK5YqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yr6oOXj1HE5-51TPwD68EUJNtHjhMp1MXqipN1dRmTV6aBxRta18PU0wCRisb4TpytNuv0Nun8a6oiKOvlHPJT9oQzlL_PJJRP9VideW46v5o5xngwJZWfIxxxUdY7faQLUqRoixhv52sj_6aMSgE6WuekHCTKfQfe662x3hA5x9eqIGwC5ljRBt0qgd_VyoeFnIarlwVFZPnXu2Ad5M69PAjPRv6PrtC6qWBiSJvAxmJDReWF87l-chkPtSlaJA1rURoc6Bko2dmsSHbvCi52SCAGCJNkZHg359nLw-aDrJsTGg8GTgZLPyhFeNIiXd2tcdwQO44bV5k3JXviQ1jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmjDWEOiw7QaYieamJ7DKr8_O5X7__DSLVzg2BsaYon6PxQKxlG0KlYUoXXvyASlbnZNn9if69tR23vzELvxqL6-1n8W8Mz-rxEqQkomthJQ1Uhx9cQfSIbhGY26rFRyWfKY8dXq4Z0NwAr_x84YlI0N-QhdCvkCqYARll1qBniLe7He6ROgSeGumQh1tnolwYTwha2o73nQv3W1sjx_00GzUudzpmCoDMvNan6WlIOJR9kveqHw2rAVAnaDUtuY7zmcIpT4eN6Nqq62E3G2CYBU4csoiHOpEO6fq2FgFUOjdWOC7yq6C42aAaC3wGhg13BbQqHqlq3bMD86MNMJ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyzRtRqvnMFnnDz6F1efjslfvBOIebZAQs7gXC4VPQOtCyGg6nC69tRBjY50kf-tWaRR1Rh5RXOFmIwFDXw9YTznSxsljtg-U9uYdZbjZiQXyi1E5HF92Tr_2EFgHA-GZ_CnGYS2qoNFUayZqG6Mjlgv5Tp_HtdNtgIfk1tHwelkZFN-vum8hrhqw-TqpupGXoqyywGjHIMKjCuY1zZFICDvFpO-mAI4z1aWdoMTRg7DedHbnJCRQuQZKWLu27EUcREZv_v7K77BNIQABk-yLBTTsQusEnKhQ8dPuUIHgF0Ju3r64r58VcSUdcDKe0ldCtR2LiOEmOXWL0VcNMdRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZTdR52CIZB5Rvz2f3YG21p3-gYSR0cqDfTA1EPDfJKa9O-hqlhsgAC9lx-PnZ0KZloNZlHisdoxCYjaremzwmZ8NhTGIw3AKDkAHWUc-v41wiRFGlIMvhJWPq1-qOfsegM9-byxV5UjdRjXf-XW5UBwKJVBOJRczkPhmgg7LIsiyMHj3bGcFRloc0ekXuh-MYgMSOW4TJKZ3OsHN1jAYjHJD6B4AG9eDW7c1mNZWpUr99-tDGzmKhflNSujMCDIz18CqTp1Ing8PXBkwJIsLlt--l58GkNgDT6kvyX2npKoDKbXHZUTDjyth1vnVs0VyV2li5AyOcRbDRb8sw5Zy0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gZukz4yM4RWlCo1lyB5wwrPu-VrBU77L3RU3qzIRSqOIrlX9HfCmX3nIIDNfzAtSSWr8rKqEQXQZ_djcZ8Po9AdQ_kDgZLpmpD9ooG_-1HAVqyDdQ8wY_gHLo7Am4544JFPiClZIqCJExxzzbAZ6sXT_6PqaJryFyatxdlFcsWZReCo57q8O7cvaXOlvGFOI_iMAlJpxJ0shyQ8T1RdnOFztfC7ZPumPxULhNqa407QAEyrpufTnCewMt6u9DzioirAMjAXfNeOgmXrO8vr1ut-v1sdZNc57zasyFDrcNpdXqrMTE--IsY5vodyKgJ5Gw8ay8W3WV4Zao35wXWvE2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bL7zeVoo7yZdq69zbx4DHlxnGSTqI2C9ddCm7P-nbp27DwsML7V-YFHJvMGiB_LSCqyPW3EAr1erEccGV3O5rONzoZDZvGeyNPQujoPDEhOvw-ffMrN88F32pzQb4voZ1EphKSCGZWZS9mr5x0BsL5h4t85oAf0KAIrZVFlEQXoR1NbHdhVWLfbYTPh7jcTQZX_ia9sM93pPWEibaBkpJ9tg4KAz86llUBvrSovDOLeSZuGIHIHSDwVgilvxAiQuo3ZwN0U1sPC-sGm5nUOJpbT3nQDieLeySHygKPf7XO-cBY2KJAkOJ0kgVtun6GROmfPs-Utk6Tv4aZtUhcoEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8t36BU1kZAM6pGadBbsFsmAqkUE_pOZyw9psTviiOx1jnul_KkgKWNOYk2GX6ox93J8MbJybCjeOhQfnubtGj8Tw5g9qjFhr59NoW4aAC1Lhl3jPNCoFLob1bzQVeH-0pj5Pq3STSE4Bt-dIsrV5hVegvHAuqDj0co28v7FN9C3UtMQuFoxp0FRq9VWwkw53KAO_C5GQuXdQnRL69flj5t7SEVZ-sb2IJIHa8KS1CSLLDAJFWOBy0DKcyIhozBull0RT3yCM5RJ8SfOtsgzK-yn7wdRZUl0W6SvAadmPT9wLvZwMXitkdqa_9I22PDgxFB9ihLzsSf5gYPxGg6_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cVFYb2LJQPWN6gIAG37KNgaN6AsmCVtMi5NvYT7TrtUCkrHMQOXmFzk-jtPL2PMXn_hxS4niO4KQf034tNvFNLEGFs-IpcJgrxxRSJJ-UxfZKDOaS9u0cInZD8IdXVeISbuxTt6eP3Am23e2wu2q1gfW5EZHR33F6ht7ulgLZfMgYQ-SkbqGWd0KuM9NjgQWl_PMHuPr0WuyVFFEKTW9WRsDQyD0noEupKjstC-ueCEyVapuws_qT-NNN2miNT_2nnTmUyHE8ENDEeF9RNHV4rF8gdsMYCYhV6Zh_Ja58yAg9GhsVNhHavyZEjooVO8XCZmvCPqzyse2LE9PuE3iaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=v3OpvHdH4QbByCzxEjN2gHa3VMk7VciZznZQ1WIWa_yuIzEhp5zClDvyITuF8e83gVNUWkk14Cnf0ptxCyeLTBL4ZtkUxlQ6g8OBenNsNBluE-9ol1aFG-Fmukx9Mwxrt3IClUU7xVYtmFkw7SWkwojHAnD4VUkZRBylrdE_4biatbXCoK_Djzi6NPXP_AiFfSwL1YimaT7sCYr8peUZulcs1tTNEdjehc9IGOFAd7nbAEfSvt-Q0OrYkEKU5s0tGK9DKnEC8Ang7-pdkgJFIxrMhwm8CLVjEleW2lpoaon-92VGLyjhmCBHZDngF6913LobNtRTmYKq0QFonmp3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=v3OpvHdH4QbByCzxEjN2gHa3VMk7VciZznZQ1WIWa_yuIzEhp5zClDvyITuF8e83gVNUWkk14Cnf0ptxCyeLTBL4ZtkUxlQ6g8OBenNsNBluE-9ol1aFG-Fmukx9Mwxrt3IClUU7xVYtmFkw7SWkwojHAnD4VUkZRBylrdE_4biatbXCoK_Djzi6NPXP_AiFfSwL1YimaT7sCYr8peUZulcs1tTNEdjehc9IGOFAd7nbAEfSvt-Q0OrYkEKU5s0tGK9DKnEC8Ang7-pdkgJFIxrMhwm8CLVjEleW2lpoaon-92VGLyjhmCBHZDngF6913LobNtRTmYKq0QFonmp3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b0Zm0hRS_6GSwYG4x4CcbPc_-QZLSkJr_uMOx7wWefkRbCCfnJoWhKO3YPlN_u3NpLxBqRaHNW64i5DJbdmEiToE9cxxMeC_EGAl1Z4Pm2nbiQXl5agRIp2R4A0zV3tT189VYcHBcUvalrAaFCyevhlpaXCKzc_buPN8oObq_3Y46_wSFoTenOOa38LewVwOCXF-8RalDzlR3x3UFM6h9VXkIfQYWMqwZCNq42Cpo098oG6WKyutvFVnKijmUQuaJi0BWaBNsJE3CHKTXinB7nHoMd3eVZfYIQYHXjpqEnNqJEETJSODsQsDBByX6G8mYdghH2jXd8lF104CpPBWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a7yCUk0NVeD4XgqUL6y1NRULc9qVYZe1HXB88N2LxgKrQ4rwXhay9oO3tLrb4Y7x04K7qovqpwNML8ccpWfaDKugx_WPJEjQUS6UE8re2EqQRe3GwS0ehOoGQEZb98jP3zNned9ZvA2fnLjroS4w5UBcNmddCPznqznJINBN95ZY7CxD-JjEcpnHuDa9ImeBhsc7ab0fGuwgYVOCmMM1LPjtk4t_NqbYm9o7ufXbGj2G9BNRaPCEZnH3IWPDAEaoI9gvSYZ5XzEybC5rGZiGMUx5WwBvBpGeieyvPDBsUV9dKpi8Ncw6ea1eatRg6yX16KZWhU-vSlJ_qo5x2RiJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIMbuzxVvs2p_vXWDCETqhiwRVY9r3bVTeq_PPi9WK2q0doEYbRrFb2ppNUrw5KhaG9JoNWncwxxegOzry4ebAkv4ZNVLVJtfkGY50WEPVS950EcUSm01Ul_7qSulSp7jUcgntnneaQi6uoG-9Rp8scUC7YYNv6O6v_51BcEiL_FGEOXo35qqTTlBZ2DGyyUQQ1hDbTYBWvKdXwDoYReKS_IJvYxfHi1WBYU1i9cUGu0XCU7Ug9BcwSzKmk9gUIg74fWXxsfSsQgf0zjW5R189AnYhDYRYTb_l_Y2-WB6f80y0GoLIZAntuMO6_iKR3rlkGRNcfKDOzukZGHpqPPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=co5m05n3obj4mSqIxRX5WQPjEoeVX2O0vvHk_AQ-VzJLJlSLuKnSCSDTTgob5Es-bTjcvAaiHlaAOSw6EAkXYV1wc8HfQzNPGibYh_8rlwH7V8e_zp4zwwjO1Qe7IWNtpqtr4W1OilzAJkx9YMx3kCXkURGC-VpkFTcnv3vHIDQBcjmpMR3aLZVYDtKLRCIhSCmi6W9VUp3jwe0TZ41BhtEhMwN2JpYMOhkpM5Jr56Hbl1jA3GZ0a9HaMg2FiFSfByN4KrBDg0RaD0HMeXSmIWAhtl5kVbuljWnbz_mubGp-FJtH_9scXYvP9B4HlC0tTCwXPn1Ea4hE3cVQ9-qN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=co5m05n3obj4mSqIxRX5WQPjEoeVX2O0vvHk_AQ-VzJLJlSLuKnSCSDTTgob5Es-bTjcvAaiHlaAOSw6EAkXYV1wc8HfQzNPGibYh_8rlwH7V8e_zp4zwwjO1Qe7IWNtpqtr4W1OilzAJkx9YMx3kCXkURGC-VpkFTcnv3vHIDQBcjmpMR3aLZVYDtKLRCIhSCmi6W9VUp3jwe0TZ41BhtEhMwN2JpYMOhkpM5Jr56Hbl1jA3GZ0a9HaMg2FiFSfByN4KrBDg0RaD0HMeXSmIWAhtl5kVbuljWnbz_mubGp-FJtH_9scXYvP9B4HlC0tTCwXPn1Ea4hE3cVQ9-qN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLWrp_j_u1UpAGR0bY-IMnoujXc8ypviiJzz7rpVK9IoDNiSHuRnpWUdF3XQySDpPL2xA5JOxcGldnXmTRW_rbM8QX4ykettIfebYfrc4727zDG2KzYqtBJ611SLzxMYxh-NyB2ySsqkIo7tqRWiFEOZi14lx3sqyGzoZ_IOQGqNDFTiQ7tUTHaFpY9PXF5KWkA1HfVraZ9bWM0Dlyrt_VxV_bP8o9j4tD_-8qDMKEKCoVNDT3i9mB5fepJqHwlTrRaAvRbrrgpRB0YUJtDWV0Gck7TAV3x9Gugti6DiRyIUstvBKntTZ59xSnmvvU2e0VMDoPkwclTGgQlIJTLflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HpuN2t6p4oEpzANZA8fViTIz5xNjI89oeGmd796exvF7YtjbRHdW4EvmiGD-qHz0iUVisB_uvXcSj_DVjcY8eEnU1ckg2bhsclCBU3J5wD2IZzJkkyv4rqof4RgydrD_1bzWAZgismDCozRDUfTpkTzB2X3q8bkHYa-kVOy1WD1ach171lrNS8PoEzsEahjbUI0btFPjoQiw6NwotkgGZ2wYiophjInU0XraOlhNopKZC9rL4YcidhwRUcjpvz7sDwAvTtXy3GpxI5DdRuS63Q70ae_UF5bjoEEBI-C5oTP6rYVb0BBxgtNK7dHimJDnvNdRRE-JT2bFxOSxPskKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v1kpy03lQ6MZPsSD0uIBGxyKV_aRraqgpD0dSvyMYGyCyR5sr-K8Dykj-m5q37AW_Lj08GJGsiKMU-Hz_V7gLgsYBzS6xm10KPLdLBtFHkncf0dtF8di9mtxnrzORcRJz5CGdun05Tjz5Xp7eN3JCzF-m9vZG_Y7twQ4diaZlg3djYcqdUSEDh3rBANC_PyJCyHpYXCCm-5i7s0n0T_5uD8_yvOPBOI3-tFCpQk3Zl_xodTZsuU1FSq-jrJBjc8Pp88IhlJ9mZr_1WJEvu-CoeDNVXy67CLzluH4l8DRhpr9v_Cc4N1A5Jq3qTFiAbXqaLEIn0jrwvU8qT4-NhoZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K-y6IR-io3zXnIjEV-cclEuAUbPprAey2F2sbMFFGAZhS89NWVG07_Fto_GijoVWIoyZuKncXlxfk7hngWMwXIt62a0A1M7_NM5a2d7VPhpeVHCec7vXtcTe6xtnnheJbVUaGRC8nBRh3ae6JQbxWskaz97HAp5QVoPFjMRy0enWNPIeqE0RpLK7-ozSO2TVJicufYHVNWpej5iZ1JwR9oP0wnp4x4k7RvpXJL7SOP9lnVMbNTCxdKXEn9wHlcrgTNyc8Y-Fv7v7m6Aybf3YqgYs0ivdmwzy-J94ytDaWmKbmQC-VGfQ0muIu5gqLW_bn8qSRdRRl_kc7QJxke2iUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s226WlarzlN5AHUPBFQKVx8onjqkoyZfykE4T7C1uUo9TVKB6wMAw9N34OWluGATJTrSLhEA_-2Zg3KCAnZQKAcjgYkb4uRmCK7Gkl0GDAwIx8QlOQOjxyETRom26VSGfUQrwHjVOyXhaG6cutIMpbtWNCbaL-mNT6IyyA-fNZmZR3MQWhC5JvQE90GaJyq7QeMmHGQj0T2AuoutlrUwF0rqgLfHCVemguE3Tcv0xeCzQN-JyNs112XzzRocA8UNQQ-fl4MrAkdOONQ2f4XuymvTW9VR2PTJ2GluKZ2FEzJTTgaFqzRqQalPw3OXKSfcxXw0tSP79WQ884RELqGK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Au00VbPmPf7lsuoDOmGc9JVFKdqr_8HQZVp9SxVymCnOv1nU63sVZMyGBJbZ2cpGekEDDVpcFAAkJp8quaNoAT6FbzLuXtca90or22Tfnjscb108XUR9_Jj50g8g1lVjSc5h_-hOYXOPdRnH4zN5_0JRQUOMzCfCtvYdNha8oFFSxYpl32hTigYdQLi09bv0E7LLx3rdK4q1NHN-q9J71lVe6EEyLIRfPOfgGqkQNZA30nlbSVoq3KcFqqSMmDr6tdVBLYJ1kminoqNrPADxE_UEdH0cbDfqSOr0Ajhv1f7tPcXJHNKuhA8ahu2lb-G06DnQFOBm3WQGAg-MYnRIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=aj_l8UddYdS3paCcysxlQHD-qfpyEoSoTpmBZirhYIxwdUcRLM5_yqziybSe8sPvQakVtsXCdmPZtksst7US3ENb9wCTnXQvyUYvIzGwmzz-_sX30KqzGYp-QNEgiM0Nm9wdoK3IE56oH-DPv2qf68rORd018S7iGGRnM4TYfUVHa3UPXQiU9sr7-5YhCZKvxhrovji7W0dBNoUcmeaX_CPEVMugblHdND3TXZ2Gp-bp8xk-tXhJQTVUsZVwJNDfqr0Vt4EG55kZhjyETQYGOCs6-sxwqf-kHMImTkcJ2D86j3YUxX-Oi7gtqD3Pq9sWBhnpSYk4Bg3ErN33Q1MdIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=aj_l8UddYdS3paCcysxlQHD-qfpyEoSoTpmBZirhYIxwdUcRLM5_yqziybSe8sPvQakVtsXCdmPZtksst7US3ENb9wCTnXQvyUYvIzGwmzz-_sX30KqzGYp-QNEgiM0Nm9wdoK3IE56oH-DPv2qf68rORd018S7iGGRnM4TYfUVHa3UPXQiU9sr7-5YhCZKvxhrovji7W0dBNoUcmeaX_CPEVMugblHdND3TXZ2Gp-bp8xk-tXhJQTVUsZVwJNDfqr0Vt4EG55kZhjyETQYGOCs6-sxwqf-kHMImTkcJ2D86j3YUxX-Oi7gtqD3Pq9sWBhnpSYk4Bg3ErN33Q1MdIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m2oMzVdgcA9HGa_uqo4MCOlItmh8QXB6qyH8au5ua7IFVoahtd8_npyCLSoiCsMwR-df63nxyHdww7-PnDyF2GdDkaWbr32U3KYtVfoc5JQjzsipfdwOq_eavulXXyr74XdvnxWqxUmXxSxcxYFI9yAgSFK0Fy02uOp-9ghOWE1seZz-2r3bBKyS5LIkDSyCFj6d6z2LdmzienWZH6klCRV-0xUTtrpwVpP2CZx3fhU97PqIQkElvttNYSjUakqkVPKxVRPIuyq1nmtPB3E7jf5zEUx0ey-0_w48AbAqOwamEg-r-rGGVuLvBnyiW9Nik3aCU2GZGHxO7h7Xzc613w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tbqX_FQI8KfKqBXrNKU9WMv64LjX9YXOpXH-SD1p9wxVohy-_WK3hDHfsJuvvOhzPB0JwPTLhsWDDtN-RxwJw679SENIsxJzlvsgZc5u5l51n2ZO6CfdtsCEEYy_hqiap3RxIO9E_D9xnmCJmEUqqYkI2SM1dTYy9BHK_5e8dgxSt5XlAcLk9vqDZx-5dMLjT5JGFp2f6Y0uaT5rxSjZ7DCWLInkRbOJG20LK9myeIbb-_RqGjy6iH_NBVArj8Ab0Ukbyp4L2Kcmw2croD9xHtNZfrxzHrlYjebI41wozuSY2H1eabxVqb7sMuw7BiPIewHg7PdR2JKjM0PtDnudAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M96Xae6xxk5qcKjbyMgrBf6cCrJK-ykyaU6omlUXwnzapKJi5xScowoOTO0AjrkZXOWWY0g3XqgzZaghflWIeIGJ4RBtnnJ0aVVbWPdArGWpx1Xz3EroI0gMxsUrz3WzoyCB78HFd8T0_r4BMLKZ5-2qVztLzchrFeUlgh8-cqwd6nXfwZmt8HrwPPnZ2NSZeZNO9nBNu3cqpkCY_y3pdoML0kOe9GmFcW37ns1MxvCLnxgNTxFM2rCUfKd6xxBpPN3nV4Lr8z6SQMTZZyO1wFecL8vPcuLu9Ib37aOi8pS5we__uxvHh3E2kWDXfx2vAreTqj1Z3EdtNLcg2qTh8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
