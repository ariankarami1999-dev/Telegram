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
<img src="https://cdn4.telesco.pe/file/DWOw1fVnu9-oT9hLaH8nzZ9yw8HjzLKd6S9ZDBVuc5cynjVP4qvMj2MRaHeEMwV811ml-4HIRDBYYKwGm8WdrgMyCisOx58zpBYIAMS-vlGiCBJU-iN1p4sERNTFHWS5wQ539VZdGeMkdQftGm8ZpLchFewXzBMxx7eI7aIo_1RUCw9jOCDxKuZkxXB0-KQOsvgi8QwKT5j1KVznupxhii0mMXoZEq9YrwPeXNOCc5X3u6OYGC5KIji2plJ6j89q0OMcgUfzwTHHLx0wg8H62oQUzh3hCLrV5BCfX98CUnXEA9Tn64kPYu53iD7UEac-0J-cgECpCi3xuTqMeOZx9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.22M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 11:39:10</div>
<hr>

<div class="tg-post" id="msg-680522">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqFQol-Ymy8-bu88HnshFpdybL0W0qV7qvoyL6_8ZjEvWCwUi7f3oaJtOV6l70pckK22CwQwOQtZ9Prc4iNaB68JpDkpShdXAovcr4OQ8MftTo9tVHaCe3LqzOUByF_GlZSa1WgZjxxxPY2KHxXFFahPggjCxB7msOwY33Z5nHFlUZkFJ0X5IWbxgJGKxHtC67PDoqkt9KBSrFhw37IpeEZ3ISvXMI7-gj8Bboab5BfaCJhSZ411dhHYrt1xCandNiRl6S2tUAIdmJol_f9kvkMYXRFlM-SDH3jHAb-M9p49hczusoutscZuUHG2Fqu6PogYoizUWrxz3hDnB1r5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af677bab1b.mp4?token=nNJRO7HKCJagM0iMMo5LIjbIsPufdn6rc5xH5-xiH4MHzKsqb_EIAY_0e2baRgLfMEEhhKaACvKkmZ68j4puWJxVTnPfN2BtR_qI30ZprgGjxRFwb3KRKFLz61fOxBzdlZRliTdXd3h4JuSdzGjpkiKZX37OUcD4UzTrsNoqDvE7GSp7cmhWis6iC-KLHNos9HRRNMr6W1NAtY_Gm4pZjaRMoPQlo-0Oyg0lCo8N6OEg9736Hi7Y6RlzKt0XSXsevD0_i7tlxno4sjYVfkBqf4qSpPIwPl3Mh7AvQyGDZB8SrBvMmlkB3-Y2ci3--p227VCaSPPfv7S7SYojgEQSQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af677bab1b.mp4?token=nNJRO7HKCJagM0iMMo5LIjbIsPufdn6rc5xH5-xiH4MHzKsqb_EIAY_0e2baRgLfMEEhhKaACvKkmZ68j4puWJxVTnPfN2BtR_qI30ZprgGjxRFwb3KRKFLz61fOxBzdlZRliTdXd3h4JuSdzGjpkiKZX37OUcD4UzTrsNoqDvE7GSp7cmhWis6iC-KLHNos9HRRNMr6W1NAtY_Gm4pZjaRMoPQlo-0Oyg0lCo8N6OEg9736Hi7Y6RlzKt0XSXsevD0_i7tlxno4sjYVfkBqf4qSpPIwPl3Mh7AvQyGDZB8SrBvMmlkB3-Y2ci3--p227VCaSPPfv7S7SYojgEQSQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شهادت پیامبر اکرم (ص) و شهادت امام حسن مجتبی (ع)
🥀
خلقت چه لایق است که صاحب عزا شود
عالم عزا گرفته و صاحب عزا خدا ست
@Heyate_gharar</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/akhbarefori/680522" target="_blank">📅 11:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680521">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
پاکستان: تلاش‌ها برای پایان بحران خاورمیانه ادامه دارد  وزارت خارجه پاکستان:
🔹
اسلام‌آباد برای پایان بحران خاورمیانه و برگزاری مذاکرات میان طرف‌های درگیر تلاش می‌کند و همزمان کانال‌های مستقیم و غیرمستقیم ایران و آمریکا را فعال نگه می‌دارد.
🔹
وزیر کشور پاکستان…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/680521" target="_blank">📅 11:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680520">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZoHcGFkhI41INdZnvEzk6DOEGDolFL8ytZmV9S8VKAWtizo4QRAFOZCA90yr-f_j3DhrU9UjCsgBiToGWgKEXjV2z781C6hVs1r53wL4pgDcSYGdOkg-0k2V2m_afDTIX05p9fOu5_hOIQ16ZZUV053ipExOMkdZHZj4AHT0zT-GFxKMCOgZstIlllFWC-q4iE6i7Q0GI0GfXC_76lLNxsfxr2QFwIqkzhF_wA4DCmgldQjeKXcTW2CdoJSOVWT94axfnqd5uqmMlC4G3-_Oi85nQjotuNVO8lWqddUb1rtOdduAZz5zJj5XCPCI2AaNYyZF5jmKH-l0SfWryQmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دادستان قشم فرمان مهار فوری آلودگی نفتی سواحل جزیره را صادر کرد
🔹
دادستان عمومی و انقلاب شهرستان قشم با ورود فوری به موضوع آلودگی نفتی مشاهده‌شده در بخش‌هایی از سواحل این جزیره، دستگاه‌های مسئول را مکلف کرد ضمن شناسایی منشأ آلودگی، عملیات مهار، جمع‌آوری…</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/680520" target="_blank">📅 11:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680519">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس ستاد مرکزی اربعین: ۴ میلیون نفر از داخل ایران و سایر کشورها وارد مشهد شده‌اند.
🔹
ادعای اردوغان: توافق مکه علیه هیچ کشوری نیست.
🔹
وزارت دفاع روسیه از سرنگونی۵۰۲ پهپاد اوکراینی طی شب گذشته خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/680519" target="_blank">📅 11:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680518">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCMJgwoqg-ONbDE1lDcPZM0KPHIBDorDfhR5SxYsGuzX7lTbpNrV6uYcneMJD5JsZLKmtDu3SoURfZu4kF87TeEHcjfv_jq9kFPP6X9__SXHfyBZdhbn85X7X2Db53Q0nWLf7fz3IMN0chyTkF_ACkh6yAiTe_i2erZs2zwU2qTD6A5e4LTGdEe7E4eLMb6x-OnIY3yFaduGv25voLaEtDjY0yh5uaGGdMowfS-j_m6uVpaN_Y4w9yArng93bzdWWpTTjPkWIOQwf9ucPnS-BYJhnUTH_xTktXy8iHy-Mb9x3gMkLejc8F30S2a3bQTZqBIbISYb-khOv8bltUh5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید انقلاب به روایت خودش: من بیست‌و‌هشتم ماه صفر به دنیا آمدم
🔹
من در شهر مشهد، مرکز استان خراسان، در جوار آستان امام هشتم، علی بن موسی الرضا علیه‌السلام، در یک خانواده روحانی به دنیا آمدم. زادروز من، بیست و هشتم ماه صفر سال ۱۳۵۸ هجری قمری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/680518" target="_blank">📅 11:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680517">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p674YY1Pv4yAwXR9RT7g_aqdv_ZckjxawrR4O8CMTo4REEiWiUpYFr0D0rRlqkru7KrZiRPEAvUYj6lGDibwF73kes0h4kCQLebDsHSL4ND0zJcQILYFvsUpwTQjB-S9ii7HDDan3isTYznRTSdPXNhrOULA4Dyhk3xP9d2vV0xTAE0-NYXhGox9xwIbkOauNDt7lgjBn_o2T5SLjAl_Eo84Kmk0dGXqfjfCHctzmdP0rnhUE0tdiy0dghUmcI3Y2zQtE-BeXVTV3SSccKoQmh7uRm5hgLwFeAd8AXf_DOvfQkQJhb0tqQwKHTIEHXP1dpDgYkbk-BGoGtOKqkvJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
مراسم عزاداری ایام پایانی ماه صفر و اربعین رهبر شهید
◼️
سخنرانان:
آیت الله کازرونی؛ حجه الاسلام دکتر رفیعی؛ حجه الاسلام پناهیان؛ حجه الاسلام علیزاده
◼️
مداحان:
حاج مهدی رسولی؛ حاج احد سبزی؛ حاج سید محمود علوی؛ حاج امیر کرمانشاهی؛ حاج محمدرضا طاهری؛ کربلایی حسین طاهری؛ کربلایی حسین ستوده
سه شنبه ۲۰ مردادماه الی پنج شنبه ۲۲ مرداد ماه از ساعت ۱۶
و ویژه برنامه شام شهادت امام رضا(ع) ساعت ۲۱
📍
بلوار سجاد ابتدای بلوار اخوان ثالث</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/680517" target="_blank">📅 11:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680516">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
پاکستان: تلاش‌ها برای پایان بحران خاورمیانه ادامه دارد
وزارت خارجه پاکستان:
🔹
اسلام‌آباد برای پایان بحران خاورمیانه و برگزاری مذاکرات میان طرف‌های درگیر تلاش می‌کند و همزمان کانال‌های مستقیم و غیرمستقیم ایران و آمریکا را فعال نگه می‌دارد.
🔹
وزیر کشور پاکستان نیز با هدف حمایت از امنیت و صلح منطقه‌ای به سفر خود به ایران ادامه می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/akhbarefori/680516" target="_blank">📅 11:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680515">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3162146fd7.mp4?token=TWkM38slmAEj-AMAvURp-RRTcaDIRSJzx3s_eMeIIbkjC41lO75xVzAo9-WIb0zxCuoHfPU2lx8v0hMkcsGDMqKQvVOGxcHkVQUqe7l2Or8yWE5a06ptmbCX40yGluYIrgWFD6TX-hx8KiQxS50lNhE-qEIH7LORK0Ytrzy9-l-0uxzcSXh4BsIR0fpg3NaTQ9PptyZzHe_gIYo09Vi_8RhSlskO8stwjfLPnzec4YS2aCAEqWBUIrUjDUvR9_FJeNz1XQtQO-OMO-VmQbS2Ja7r4u1KwhzXG1JtecLaASu-22lA9zbudC311NLNZsbcOuEAdCZV7AZzWoqENLGEoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3162146fd7.mp4?token=TWkM38slmAEj-AMAvURp-RRTcaDIRSJzx3s_eMeIIbkjC41lO75xVzAo9-WIb0zxCuoHfPU2lx8v0hMkcsGDMqKQvVOGxcHkVQUqe7l2Or8yWE5a06ptmbCX40yGluYIrgWFD6TX-hx8KiQxS50lNhE-qEIH7LORK0Ytrzy9-l-0uxzcSXh4BsIR0fpg3NaTQ9PptyZzHe_gIYo09Vi_8RhSlskO8stwjfLPnzec4YS2aCAEqWBUIrUjDUvR9_FJeNz1XQtQO-OMO-VmQbS2Ja7r4u1KwhzXG1JtecLaASu-22lA9zbudC311NLNZsbcOuEAdCZV7AZzWoqENLGEoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استهبان؛ بزرگ‌ترین انجیرستان دیم جهان
🔹
استهبان با بیش از ۲ میلیون درخت انجیر در ۲۴ هزار هکتار، بزرگ‌ترین انجیرستان دیم جهان است و برخی درختان آن بیش از ۴۰۰ سال قدمت دارند.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/akhbarefori/680515" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680514">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlefbayesafar | الفباى سفر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyqUX58I42yxUjoWt7-csV3o9GFdg_LneH5WTILCoS50mX71xFPhdQLXDAkXj3S8STaUFdpSifb1d5a2COiFiKWiapeigG3w5ik52bAbJYaVSdCPrSv3kAio9RjKh9SNaTgk_owXOsK5R2au_xQy0XgEULCQKWNDmte3IL9dXVi7KR62h1hFGPJgBAFnGTxVbM5n7y55vY64hMolE4i--ftYNsfYzWnFDV6vSPjBZlCm9oaDpnfd8ABCWnVoWPdus2vvwSWfpJwfGKRoA7FaxztVrLrr2z7JMSgJVcjRvkC2W9MdGb3N7ujSeKZ0-079Dehy0OkQHVU2N1e_Vnv-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
آفر لحظه‌آخری مالزی | تخفیف ۲۰ میلیونی!
این آفر رو از دست نده
🇲🇾
قیمت پرواز از
۱۱۹ میلیون و ۹۰۰ هزار تومان
به
۹۹ میلیون و ۹۰۰ هزار تومان
رسیده؛ یعنی
۲۰ میلیون تومان کاهش قیمت!
🤑
🚨
این آفر فقط برای
۲۴ مرداده
؛ تا ظرفیتش پر نشده، رزرو کن!
✈️
پرواز با
ایران‌ایرتور
✅
حرکت از
۲۴ مرداد
✈️
مدت سفر:
۸ روز
💸
شروع قیمت تور:
۲۲۵ دلار + ۹۹ میلیون و ۹۰۰ هزار تومان هزینه پرواز
🛫
برای اطلاع از
هتل‌ها، شرایط تور و رزرو
همین الان با الفبای سفر تماس بگیر
با ما حرفه‌ای سفر کنین!
سایت الفبای سفر
💻
اینستاگرام الفبای سفر
📱
تلگرام الفبای سفر
❤️
☎️
۰۲۱-۴۹۳۵</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/680514" target="_blank">📅 11:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680513">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
امیر سرتیپ شیخ: حضور نظامی فعلی آمریکا یک تظاهر نیرو است
معاون اجرایی ارتش:
🔹
ایران در تقابل اخیر، جنگ نامتقارن مقابل آمریکا را با موفقیت پشت سر گذاشت و دشمن به‌دلیل توهم قدرت تصور می‌کرد با یک ضربه کار تمام می‌شود.
🔹
ایران به‌دلیل موقعیت ژئوپلیتیکی همواره با جنگ و تهدید مواجه است و صلح یا توافق، زنگ استراحت بین دو نیمه است.
🔹
شیخ گفت ایران قدرت برهم‌زدن معادلات را دارد و مدیریت تنگه هرمز با مدیریت و نظارت ایران پیش خواهد رفت؛ نیروهای مسلح نیز پشتوانه دیپلماسی هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/680513" target="_blank">📅 10:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680512">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پهپاد ناشناس پروازهای فرودگاه هانوفر را مختل کرد
🔹
مشاهده یک پهپاد ناشناس در حریم ممنوعه فرودگاه هانوفر المان، پروازهای این فرودگاه را حدود دو ساعت مختل کرد؛ دست‌کم ۶ پرواز مسافری تأخیر داشتند و یک هواپیمای باری نیز به نورنبرگ تغییر مسیر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680512" target="_blank">📅 10:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680503">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAZlCrRSokDkbPku_QvOg5nzodYhoe7QE7rcoJcHsijoi5s9wObbW_fyCEq4267BCOsN6B0zenb4Hpvui0lCBF3x7dkyK04JYxI4C4Eljz6Tt5JvhDx-8fGDinEz0sfaOfs4STeEAWflU6ovTxKffWscZlMAuY2sXWX3oa_ajsugEzqsLJ7FLsDT4aaFOPt0k4eZudaOYAU7orW1zwMW04dqjXqxHyRgFwOa9l2OhffEr4ISpmpyihX3Wek54MklMFuuhhYFTZdsj7d4LUrLJJYX0BPExu6IK0bFzFFuoEAgc25_SLczaxVPwQttHRld6SLsg1OPjzwZbix01oLuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nok5ACmBs6MwGsWt7ieiT4veoTMegRu0KgEbHVjr-UndNm77q3n559_bnP3qBEpxo4DAYtVo_HdcCG2dKyrGqUnPBoRy-zQJNt9PgTVB60cRoDqL1Szb_Nr2krkNp3u8UlUz9HgPFIPvTjtqcT-6VEsfgjDNd9t0yDL8RdT-GVo78T4ZGy7m-12yuTCtsD18bIWM6zzdr5yrB9DzD8BiIym4H_0yEyTbrMduRjRCMcmY4OzkTrrmn2myvRSJnGsVmOZKX4Hl8FB25JoCFQjMFCsrr0lYAANBqAORkMhhpEAlmh2xfWNTCBv1jzqeoEf3KBX9kcOU5A5qltpt9_fa3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxu_9w4ADb0W34dHLwLhUuQVgtLs5RAHSNgTtkEfnbYQeAOs5qiy5lXmO7awMv1n811yCv7cuEUSWk3s0BK859yuCCjvdm5twTR1l_ZMThejLPaBmfPD7BTcAZT9MbNN0XXO_cN9txZAbDs61lfGx4ak6QjxvtVA3PbRjCiBYKuoY_kANCD-c0nLg80XjWPe7rASTxhV_FuBy6yquCt9lNBf4eKym0pN9w42B2uBtLkkj4vB42wp53AJbkK6HBr-fIkSK2BITTX5sLjQphALb7djJHX59al_eSxMCwR224i_4N6E52FIqx8eqjbJSpcMSgeKTnSC7pqfZUa0Bi5LCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OnLTM19Xv_vYRV1B7aCF1iFGr3Kz1TFATYIdmk16JmOWln-DuFKVnJDLS9bR4xpIBjMU3knFnQvBUqhzvbnu8DlfmmY2iRDqbS4zNF8JUZ3bGrYc6Rj7Nm84t0AHtPYtU6KfUoMfJrEYwcEqVB51FeIoouNcMaS5NsrUtc2xRn3oMUQh5y0UETgKVKsODPBrSQtsRqD1AhXVeX-PQxViKV_N7pBtJOrSnF3nz5RK_nUTyiVZ8615U--3wvMSGTl2SIgUBVApvPyXHGd_YICwKVpZ4nvrPvEqlqkzpD54Zbudq9AnEYrimUBP2U37FlZg1YdnajoGWxcVla-RETPoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BquNF3fZtSZSJYXwTj4HQgpiLGdSp1jAnFsSib5-iPZRSzPDX3wAfRhcu_De8N_EkSZRclSVEA08Ut1Q-pYclXuYlIi7Y-GFfwnP4cr5N1PBgQAwoVQyQ183uQExQi9atBolYwQHAx0bEPK4MQIf93WotjirZ_OOF-Co-uhDocRo9HKGpbHrzppUe_lDHQWDrg2eSXZXt79HzuRt8mzt7uKlKyYjtPvsRSmolBRz4pTxEhFJsV2vWzLEHCyCzWyCDornNpCCC0bbhmQeYDrTT7ACpL1g19ROZfV_n1jUFzWEloEbIkXhf8iu6FPwJpSzdg6xmCpg9Et1keE6Dbl1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoUM03krx41EGl11n6muV5qy_LIsk8BJPHWClBM6Pbc3O93OT4fWZkKR_g6AZrw0DrVX0QRyLvpg5nvNBP79dnRGSXw6IBcMH-YZftZkxauv-4qGW7aLU2gVJoBu_c00J6hxS2zMDfwV9nHlyr2C_bQR_o-jOYvyAKHQc9Nqb50-BYjKw8ApiHEpUV9BGfwooYWHov-fVzmwrCT9bhwT7DHA8ckuxv7yCKBflrlKfQtBfJ33LlZt1U6vK5voosfyrbudDmMG0AFbcs9JgE9Srvi_91WS2VbzLHzqFZhAL5KHrzJZJX2FaE_UF6T5KooOp-_abqFKYHkwDo0f-BWn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbKsnEZxMdnNozvkCfV01m5crUaamcKJrH5UhYKbrqtG6Radds_gaBPcudIBwUqxH5HfnGjecFFfLPfZe4T2VxodOHPzHqvrfEUQjlwTyTi5PDEGW71EjjxDTcS2K6KrKCLyOyCa-MQeAZ8Rj6rV6WrdveWTVePHfwWa2o0vdD_SKa-2S8TdyZwARtBZD1iYPV2QHzrc7Szw17jjhEzhR1DAOeqxGHs1nZnYnJKBxvYjxvqU8QedVuLjcqgooxLbRrfyEdq14ieN9i2ELOd01OeXMz7Dg0x3lEzymoWN2DJTmP_xfJKupwjew4LOQe5Cz1ae0sWKaI4N2n_fb2Ddrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUKYIlVD-wkllzoajN-3bOywzWK8ZWY5aZF1dapTXaKjW3ntq04WNjYGhlik9C9FGsonY3gw4eMX_d1KFPfQrU_Qj3h5cYI4jNXj-crk5mbM6GIoTyzTjf2FikyV_A9smph_GqUlhbO3hMGzytBz7lwSXNX-BcLFp0pd8VAuSn9N9ABcETXAl9l9R-K-pE81I6CdoypNo6DNqdw44afSaIqHlMZF1U5WQIJ2tCVLS-cz--UVPF04PcPzFYjCLinKD38oZM2TPulj-y3zFsOtaRv7hC4ftQBDVrNhC49uS6Zehw3CYROzB4ZR_Q2FlA6-t5ArerWvSA6j2CwkMwZDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0CXKio3N83yvMmnQohatqdkkoyhr3VZCddA3Q5dKK00lg2xo-MajPsxqjfrpqS2WQuOnJbqZ2Mcq1YIeFViZRFDR6ee8DichIuSw8koYS0Ot_-Kzy_f54v6Pb0FgFfSpx5yiT7trYmmOKvVB0ahGY5GdOJCSKrdSXXzB1kfHHfCNp4FZfeA4TzQGGraHYZFcnkwrA1k3tNsDtSrQXBoacrYyHk0h2GHcm1TO2HQ4UPKX9iCZyR4ZrdDBAk38gimL-9W2tWpliCZBFMKI4tF05h-SIkciYcTuBCqfYeDwY-hMbD6diTYsUFVBPzCtDHgEvzJ5UmaRKFsvunot30xbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خدمت‌رسانی به زائران پیاده امام رضا(ع) هم‌اکنون در مسیرهای ورودی به مشهد
🔹
در موکب هیئت قرار و کانون سلام در محل تپه سلام منتظرتان هستیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/680503" target="_blank">📅 10:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680500">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b12093c5.mp4?token=KBJNYf6jbUrj81FSzpg0eRuafI_UDHBlyFEY1dHsl0nJ9NNx4ecmyHMf2_79Q6VYjpiC9xa9f4Rp_o2OU-x1-NAVeH5nKZwOZMbu7rxLMChXEOMkKVynmRW2Xeb6_ddK4X21teqwJn3q7SUyeXqQNp444RFGm28tHMFWga_-1Q0me995MMHU3PugvCxrcQx3ju4hW6X0fJI1D1Lra0ehu_EeEtvaPVLBZ0NcIsLdx8nFLWSH4Aqoe4MOHDj3WD0LAEL8QxplmKSemfytuL3JqtmHlbrJEFTOWjlo9jiXOloMF2o-vvT7Ln4sTWU6HRYgl8L31TdGyHCvTXN-Wwl_gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b12093c5.mp4?token=KBJNYf6jbUrj81FSzpg0eRuafI_UDHBlyFEY1dHsl0nJ9NNx4ecmyHMf2_79Q6VYjpiC9xa9f4Rp_o2OU-x1-NAVeH5nKZwOZMbu7rxLMChXEOMkKVynmRW2Xeb6_ddK4X21teqwJn3q7SUyeXqQNp444RFGm28tHMFWga_-1Q0me995MMHU3PugvCxrcQx3ju4hW6X0fJI1D1Lra0ehu_EeEtvaPVLBZ0NcIsLdx8nFLWSH4Aqoe4MOHDj3WD0LAEL8QxplmKSemfytuL3JqtmHlbrJEFTOWjlo9jiXOloMF2o-vvT7Ln4sTWU6HRYgl8L31TdGyHCvTXN-Wwl_gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک کشتی مسافربری در سواحل بالی آتش گرفت
🔹
۱۳۱ نفر در این کشتی بودند؛ اکثر مسافران توسط کشتی‌های عبوری و امدادگران نجات یافته‌اند، اما تخلیه همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/680500" target="_blank">📅 10:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680499">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مذاکرات ایران و آمریکا درباره تنگه هرمز به نقطه اول برگشت
ادعای خبرنگار الجزیره در تهران:
🔹
مذاکرات ظاهراً به نقطه آغاز بازگشته و توپ در زمین واشنگتن است؛ تهران ممکن است به این نتیجه رسیده باشد که نحوه عبور از تنگه هرمز نمی‌تواند صرفاً بر اساس خواسته‌های آمریکا تعیین شود.
🔹
با این حال، تلاش‌های دیپلماتیک و میانجی‌گری‌ها ادامه دارد و احتمالاً در روزهای آینده نقش مهم‌تری در مسیر مذاکرات خواهند داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/680499" target="_blank">📅 10:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680498">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12f75205e.mp4?token=be3nSY7sWOPCApxtCjBvilv0EWE6AuqoLoRAgZV8R-epgcjIL0_UWUOJwRR-Fj5YnSGKpswnM9PbEXTSxsCeZHAn0_uwAuOSiFE_Ao8p7Rr2V21tN8RY8fXPYLk8PN92nOmedB_zI0SQT2NKAEfMu6OVlsl9yf7lfaiIG8WiSmNS4r-Jcc2OBZTVaht_UvxwYurXsknfqLZEF0SSSvEdQY-fN07_7R7HPSXgQgblEoqWI5IAsafXBo4dww9xKfF0u7Y0jJwnaEISuLGX6064dQfhQgRo2VcsDAJ7L3vGFXXPh6f0jR9mU7lcjDXCnLxDLhuJmWWTK8-7M2TMi8OLKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12f75205e.mp4?token=be3nSY7sWOPCApxtCjBvilv0EWE6AuqoLoRAgZV8R-epgcjIL0_UWUOJwRR-Fj5YnSGKpswnM9PbEXTSxsCeZHAn0_uwAuOSiFE_Ao8p7Rr2V21tN8RY8fXPYLk8PN92nOmedB_zI0SQT2NKAEfMu6OVlsl9yf7lfaiIG8WiSmNS4r-Jcc2OBZTVaht_UvxwYurXsknfqLZEF0SSSvEdQY-fN07_7R7HPSXgQgblEoqWI5IAsafXBo4dww9xKfF0u7Y0jJwnaEISuLGX6064dQfhQgRo2VcsDAJ7L3vGFXXPh6f0jR9mU7lcjDXCnLxDLhuJmWWTK8-7M2TMi8OLKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطار مغناطیسی چین در ۵.۳ ثانیه به سرعت ۸۰۰ کیلومتر رسید
🔹
مدل آزمایشی ۱۱۱۰ کیلوگرمی قطار مغناطیسی چین در آزمایشی روی مسیر یک‌کیلومتری، تنها در ۵.۳ ثانیه از حالت سکون به سرعت ۸۰۰ کیلومتر بر ساعت رسید.
🔹
این آزمایش همچنین موفقیت سیستم ترمز اضطراری را نشان داد و قطار پس از رسیدن به سرعت ۸۰۰ کیلومتر بر ساعت، در کمی بیش از ۲۰۰ متر متوقف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/680498" target="_blank">📅 10:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680497">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/680497" target="_blank">📅 10:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680496">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: من به ایران اعتماد ندارم، من آخرین کسی هستم که به ایران اعتماد می‌کند، آنها دائما به من دروغ گفته‌اند  رئیس‌جمهور آمریکا مدعی شد:
🔹
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آنها کنترل آن را ندارند؛ ما کنترل کامل را داریم.…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/680496" target="_blank">📅 09:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680495">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2685de5d44.mp4?token=LB3VkCIA1Vo3bjeOddbpjph_1nGxM3ksGBTEmZpp6FBYT6Kp1FcLYubVBJcZPHzYtLchgUZNbTlxYcsM_OaFkabnnqNQ81_jtVELUNs62WHW6-65nGXcAklGertEKKh0PNeERxT-_jtxrEDrRYl5Nu3cLr2tplbhP8h-08p2FRPGa8TtdVUqXXlWya0Ptvs_lmPx6Myg80ffj1O-vjRxWQzURtYjGLY5jGvMP0V7l7xs4pFjjzRb0wV0usx37tcrLKnhQcjJ8shsMm305oVpnET9Ka4WLAwLXgEv0H4FRI-yDz4-LtPcHeKLhEn0vWrUkf3AXTzPi4TwG4daRyZHmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2685de5d44.mp4?token=LB3VkCIA1Vo3bjeOddbpjph_1nGxM3ksGBTEmZpp6FBYT6Kp1FcLYubVBJcZPHzYtLchgUZNbTlxYcsM_OaFkabnnqNQ81_jtVELUNs62WHW6-65nGXcAklGertEKKh0PNeERxT-_jtxrEDrRYl5Nu3cLr2tplbhP8h-08p2FRPGa8TtdVUqXXlWya0Ptvs_lmPx6Myg80ffj1O-vjRxWQzURtYjGLY5jGvMP0V7l7xs4pFjjzRb0wV0usx37tcrLKnhQcjJ8shsMm305oVpnET9Ka4WLAwLXgEv0H4FRI-yDz4-LtPcHeKLhEn0vWrUkf3AXTzPi4TwG4daRyZHmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون استقبال از زائران امام رضا(ع) در مسیر پیاده‌رویی زائران به سمت مشهد در موکب هیئت قرار و کانون فرهنگی سلام
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/680495" target="_blank">📅 09:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680494">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba5nZrCMotMlu5BKBqk1QsersaDNcLBkqSNQY-g2UoTW-R5YjmEbaLeKFoiAp1IcMhB_g-cJMahKTHAFqio4Nm1rcVbO3LJyWZuglq7N75j8NobC516m46uBmWKEafoWV_YmI38DzgFbb5jH-2A5SgQbqICkxxPZivi0eIB1A-ebf9WRsIkegJuD3WraAYZ0O35guNsTdZ2EEXVsSvdZAvj12tfUHYls08-grDDwpmG7Ixb1YBA0TN3LLgP03MkLF7Y8FiZfTEM8gB8KTKMs3lNW7T3gRxP-JWBl3_y2FkTMmAnGZVrkYgYFCsEMVMmQktiL9BAPwjDKuq1IXTHtwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ، آخر هفته در زمین گلف خود در بدمینستر، در کنار یک سامانه پدافند هوایی کوتاه‌برد AN/TWQ-۱ اونجر (SHORAD)، گلف بازی کرد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/680494" target="_blank">📅 09:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680493">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDgusxUAH8YLKqUHCTRyrdS5ljdUJPWRpmkkR51zj7pbPKF_-yTfLN2ZOfLifYO_W2dm3bLiw7TarU9dMnXG4ZEpxhOs1TdiurAMjwjYl2AR-UmbI0lkhnyvM7UFl7LhvTmIRobdK6-kuxFecOV1zyRfn5bAznIy_JF1G07hZUNT4B73RK9CVu9ci6z1FrJK9BtBz8A263_-vmZdyC92KU0rv5kJCnrdGvXoBcLOl4k3ncY3loItCaZ_rDm9hntth86dvBbTbDNOTQWhYTrwWIn19UwWN6KmH5F2r2bkMH1m1P7N_bbZLOX-nTgyrUBLs5dkBjpS5T4tPW-RANbehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار مصرف همزمان مکمل‌ها
🔹
کلسیم جذب آهن را کاهش می‌دهد و زینکِ دوزبالا هم روی سطح مس اثر می‌گذارد؛ برخی مکمل‌ها را نباید هم‌زمان مصرف کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/680493" target="_blank">📅 09:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680492">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
حمله پهپادی به اربیل
🔹
الجزیره از اصابت ۴ فروند پهپاد به استان اربیل در اقلیم کردستان عراق خبر داد.
🔹
به گفته این شبکه این حملات تلفات جانی نداشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/680492" target="_blank">📅 09:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680491">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qi_NY2HxA4V7Y4iYdq4k6jJ5Z2ijE5oeXyBeSiCBHPxDqKdQmk71bHSNQB1HYVi4E1DTKaOJ0kefl-rPeIwYiUzGMQzLAhh1gH3OEJPVstifkq-FEW_XHQAqJ6i3rMU8RSoSXo658O4jhwyUvuL5Ig3vaxgpo0jhkdbN7z-LE66f2ihPf6SFVOhJQWM1JXIfh41kP_tLipODZ1mv_Z5mfXxeu5yLIYqftcoIIhcy-srOszfLOgjpW2UlHs7CDgTqPVS3A0o0Fcp2TvG0u1HHNYLrM0y_26jQ3Zyhqm4SsFf3AvFg-o8KYlNNdzD7A0vxy9BSOZmcVgh_WHnbL2MFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت تتر ۱۸۷,۸۷۸ تومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/680491" target="_blank">📅 09:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680489">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqBkdZHnuILTHWZ2PEAtIp7hcxxJGe_57OH5CD4YyL8C6PGINeURH5cs2xye2KZvx2BiFSYk0T7CkV-fJqjidKu-H2IzebTv6iAP8OZlUNzAI2QlO6j4Lkw3wX0hDRoYowJCe5cI2TQy3e6Jbs4luW84yHyZdv_7FRd66-1HVKQjxCQu2rTmHV-DUXc9iE2qfv6NNKz2PytEo9AUloEo9zq_830xY6QCAfc-f3RBW_JuP9x0oBlRwAJ8HqtCKrQDKEkEJWi6TS5D8vYC5Kij-fJI68nhBUvVbcTr_sUywQg4dAKTVKhfGGid89dvlcmYVNwjUE2fP7Gpv_Jj-mg2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردم مونته نگرو هم به جوامع متنفر از رژیم صهیونیستی پیوستند
🔹
پایگاه خبری عبری زبان بوحل در گزارشی در این رابطه اعلام کرد، رویکرد ضد اسرائیلی مردم مونته نگرو آنقدر گسترده شده که رهبران جامعه صهیونیست مقیم در این کشور را نگران کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/680489" target="_blank">📅 09:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680488">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5zmpkY3wqADoyU4nwEtsziNFYQEfN5z7mUOG0q5oLeuqHJaNhgd1S_F3kDc43wcyPsjkiJtL-SMuxf-uq0Ovs60ERFZVTKaFFCXXysP7JBc0yuUnwsoq5VoIOfavEmxIu1HrM21m4YIutLLzFGfPhXlN0ziicVAGh60twjW6OqBCGus32OCih4kcNqDrRxo07VcZ2w98eHptSALTqxQ0b4P6Mer53Qj5keTPzyvifPA2j6KRrud8DjVw0pr9x0OaWPDFqkbbMwaAzyVFoAG9_hLclnvlxwRFfB1A0ysE23bBN8QcLvrowpfgait9K_6KHvB_5EGUHfqqEcOfIgVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برچسب انگشتی، پایش مداوم داروی پارکینسون از طریق عرق را ممکن کرد
🔹
پژوهشگران یک برچسب نرم برای نوک انگشت ساخته‌اند که بدون نیاز به باتری، میزان داروی «لوودوپا» را در عرق بیماران پارکینسون به‌طور مداوم اندازه‌گیری می‌کند. این فناوری می‌تواند به پزشکان کمک کند تا دوز دارو را به‌طور دقیق‌تر و شخصی‌سازی‌شده تنظیم کنند و بیماران را از بستری‌شدن در بیمارستان بی‌نیاز سازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/680488" target="_blank">📅 09:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680487">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d40c15cc.mp4?token=EmM1KNh9aSQvj3up_pm5g_WYNQZZzxdVTzjFFGXJ1Vie7Iw_RoeAYMN0IIcj9GQcLTO7cLE_Anrn7yI3kA-B5bPuog_N8eUlwdvdPx6Pc6li1UAZh17eV0vyT3DJ9IQabfSoGMMw3hABKgEpWCjxSUqYeWNicy8wHgA3kZBdnqPWMfNJzmoG4jYfsvdOXir2KQmJXdA0Ewk9X1I7PvNNDJEUWcVPdFyfibKjziq3ph_4ZPVprUaZL1uFSYfi_1Ez_Tp1X9zjN2rhVJid3soR8sLmV8aKb683us2On07ShJKPYqd461DnZBTg9-9Ap4faR7PTYi885wZJFgwp6sSgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d40c15cc.mp4?token=EmM1KNh9aSQvj3up_pm5g_WYNQZZzxdVTzjFFGXJ1Vie7Iw_RoeAYMN0IIcj9GQcLTO7cLE_Anrn7yI3kA-B5bPuog_N8eUlwdvdPx6Pc6li1UAZh17eV0vyT3DJ9IQabfSoGMMw3hABKgEpWCjxSUqYeWNicy8wHgA3kZBdnqPWMfNJzmoG4jYfsvdOXir2KQmJXdA0Ewk9X1I7PvNNDJEUWcVPdFyfibKjziq3ph_4ZPVprUaZL1uFSYfi_1Ez_Tp1X9zjN2rhVJid3soR8sLmV8aKb683us2On07ShJKPYqd461DnZBTg9-9Ap4faR7PTYi885wZJFgwp6sSgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله توپخانه‌ای رژیم صهیونیستی به ارتفاعات لبنان با گلوله‌های فسفری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/680487" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680486">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
هشدار سازمان غذا و دارو: با توصیه هوش مصنوعی دارو نخورید
🔹
حتی دارویی که برای یک بیمار کاملاً مناسب است، ممکن است برای فرد دیگری به دلیل تداخل دارویی، منع مصرف، حساسیت یا شرایط خاص بالینی نامناسب و حتی خطرناک باشد. بنابراین نمی‌توان یک پاسخ عمومی تولیدشده توسط هوش مصنوعی را معادل نسخه یا توصیه دارویی شخصی‌سازی‌شده تلقی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/680486" target="_blank">📅 09:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680484">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
جاده چالوس به سمت مازندران به‌دلیل ترافیک سنگین یک‌طرفه شده و تردد از مسیر شمال به جنوب تا اطلاع بعدی ممنوع است؛ سایر محورهای ورودی مازندران نیز ترافیک سنگینی دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/680484" target="_blank">📅 09:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680483">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed5443e66.mp4?token=SHsLuOwgdJEajbMj6E02j7C4A6hBDWQuKvPqMNWTt6Gf_Y4obi5H-m07VfOtgAUEKkSLcwFipc3OQLUovQjSEwcBUFyLjDYdu1N-8_ndXC1J_qIqib482fEf4STFFWlyApAUwTABsF20maTje3v6fbD2cy8CsiP9y9hOjcTBwsZ9CZGI_b3hKcmbY72pcS82iDzotZiiriSzj3phTMQifnTKCu5T0cuNrd2K10Lnsw0Yzd0o36t9uQU9L6_9-PblUkSOO5H3arJZ6UzrP5Hdje_NQFV8o52O8u5muPsASrDmbJ7Mv05CbK0D_e2mSeWjmY0Lf9mX_G2JdXgByiqJDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed5443e66.mp4?token=SHsLuOwgdJEajbMj6E02j7C4A6hBDWQuKvPqMNWTt6Gf_Y4obi5H-m07VfOtgAUEKkSLcwFipc3OQLUovQjSEwcBUFyLjDYdu1N-8_ndXC1J_qIqib482fEf4STFFWlyApAUwTABsF20maTje3v6fbD2cy8CsiP9y9hOjcTBwsZ9CZGI_b3hKcmbY72pcS82iDzotZiiriSzj3phTMQifnTKCu5T0cuNrd2K10Lnsw0Yzd0o36t9uQU9L6_9-PblUkSOO5H3arJZ6UzrP5Hdje_NQFV8o52O8u5muPsASrDmbJ7Mv05CbK0D_e2mSeWjmY0Lf9mX_G2JdXgByiqJDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعداد کشته‌های زلزلهٔ کلمبیا به ۲۲۴ نفر رسید
🔹
تعداد کشته‌شدگان زلزلهٔ ۷.۴ ریشتری دیروز در کلمبیا به ۲۲۴ نفر رسیده است. کلمبیا این زمین‌لرزه را «فاجعهٔ ملی» اعلام کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/680483" target="_blank">📅 09:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680482">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
خورشیدگرفتگی کامل در راه است/ روز در کدام نقاط زمین شب می‌شود؟
🔹
چهارشنبه این هفته، برای اولین بار در دو سال اخیر، خورشید گرفتگی کامل در بخش‌هایی از گرینلند، ایسلند، شمال اسپانیا و شمال شرقی پرتغال قابل رویت است و برای دقایقی، با ناپدید شدن کامل خورشید،…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/680482" target="_blank">📅 08:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680480">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
عراق اقدام کلمبیا در به رسمیت شناختن حاکمیت اسرائیل بر بلندی‌های جولان را محکوم کرد
🔹
وزارت امور خارجه عراق تصمیم کلمبیا برای به رسمیت شناختن حاکمیت رژیم اسرائیل بر بلندی‌های جولان اشغالی سوریه را به شدت محکوم کرد و افزود که این تصمیم هیچ اثر قانونی ندارد…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/680480" target="_blank">📅 08:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680479">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade0fc751a.mp4?token=sJyfWrWG7n6jXADmwSidMJgNFMpOPPTi4Ogl8ob52T87N9hatRlaiYxGh9oWk1rfI9WKjmiOrUgN_hbkELpRs3eWYJRmC0vJpxuOtvD8fT1l4LwwceKnmRxSsbPBV3_remYLv-cNjBYNZ42uwq4_eQq_XhVzMEBIIeZIzprOIPgctfctjUnQkn1A59KULT3N8oxslwcD2DWdr0PcNK-V-8fWA8i4qC6dxinhODeHZIV1ehZxzedIv9l2ZrePjNaagM3tpBPKwWVES4DhFscBWgXKdHBq8VtUx39thqekjdvEHzEM31k8R3-hxAwIqwfepqrwwVFWaYC5BQv39Wb5NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade0fc751a.mp4?token=sJyfWrWG7n6jXADmwSidMJgNFMpOPPTi4Ogl8ob52T87N9hatRlaiYxGh9oWk1rfI9WKjmiOrUgN_hbkELpRs3eWYJRmC0vJpxuOtvD8fT1l4LwwceKnmRxSsbPBV3_remYLv-cNjBYNZ42uwq4_eQq_XhVzMEBIIeZIzprOIPgctfctjUnQkn1A59KULT3N8oxslwcD2DWdr0PcNK-V-8fWA8i4qC6dxinhODeHZIV1ehZxzedIv9l2ZrePjNaagM3tpBPKwWVES4DhFscBWgXKdHBq8VtUx39thqekjdvEHzEM31k8R3-hxAwIqwfepqrwwVFWaYC5BQv39Wb5NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم مراقب خرید طلای آبشده باشند
رئیس اتحادیه تولیدکنندگان و صادرکنندگان طلاوجواهر:
🔹
برخی به دلیل کارمزد کمتر اقدام به خرید طلای آبشده می کنند که به دلیل نامشخص بودن عیار آن، خطراتی به همراه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/680479" target="_blank">📅 08:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680477">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وزیر خارجه رژیم صهیونیستی: تا زمان جمع‌آوری تمامی سلاح‌ها از غزه، رفع تهدید و پایان حکومت حماس، بازسازی نوار غزه آغاز نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/680477" target="_blank">📅 08:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680476">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: من به ایران اعتماد ندارم، من آخرین کسی هستم که به ایران اعتماد می‌کند، آنها دائما به من دروغ گفته‌اند
رئیس‌جمهور آمریکا مدعی شد:
🔹
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آنها کنترل آن را ندارند؛ ما کنترل کامل را داریم. تنگه هرمز مال ماست.
🔹
شاید در مقطعی آنها دست به کاری بزنند و آن وقت نابودشان می‌کنیم. اما در حال حاضر، ما در موقعیت بسیار خوبی قرار داریم.
🔹
ما با کشوری روبه‌رو هستیم که ۵۰ سال قلدر خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال است، درست است؟ ما چهار سال است که می‌گفتیم ۴۷ سال. اما آنها دیگر قلدر خاورمیانه نیستند/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/680476" target="_blank">📅 08:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680475">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9061d1aea.mp4?token=UOisl5nO1qZoZl4lFDivWDM9QAppXFtiqSprelu3_psNJgBvIP-Bxj-C5tdAqTocoU33h7aZCckvPaJOmvns5v022HhD10gxvGKK6blpAqRoPPPuNY2qMOwDig2gOWK7R35BrxaZznrEoAsMHcnyQDfnFNGvxoZHGiM5eIH4bFfg-1RVIbJyfNv5qu7AEsJbW5cAtXQYnI-p-GitHX2bBv6yK6MHp_eIe2e_Yt8See4uUVvOd8tGWD4xivFDgOys1SWpepJJOYI6LwHgl0ms0sIk__y69dvKp6qmPR4HgGuvo4qEYF11e3nN7c0yD7Ej2-pYutzmY6o8FrgCY20icBtkACU0JFxX9tQwKWscpumLgE4rd2ro85_nswCiNj66VREe_RXXviIc5vLQA-lbSTV5OqaP4J-Bwx5a3Ny-M1brW9MFQ7roaiPPwyqffOmY_lKgwfjkHUZV7qdtPEdQ_bw0TlBqzU_ATyEGVyN7tbD6gGch2eVlGPvSNSAXd04ev-U0AcULbl2zQXRRZ9NY1-uHB7uZkwtbr7cCG4akrJSzKCut2Z9_zeqR2Lt5tYkk78cQ3Da-ZEujr8SMKfyJtHe-9nSuFxiAtWBXqxSz8SAlvjEaBgaHZLv6mO0AONaJXmj9IFmHb0Czu5hFxkYqdtb0-yQEwAmcEz8NUD0EhAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9061d1aea.mp4?token=UOisl5nO1qZoZl4lFDivWDM9QAppXFtiqSprelu3_psNJgBvIP-Bxj-C5tdAqTocoU33h7aZCckvPaJOmvns5v022HhD10gxvGKK6blpAqRoPPPuNY2qMOwDig2gOWK7R35BrxaZznrEoAsMHcnyQDfnFNGvxoZHGiM5eIH4bFfg-1RVIbJyfNv5qu7AEsJbW5cAtXQYnI-p-GitHX2bBv6yK6MHp_eIe2e_Yt8See4uUVvOd8tGWD4xivFDgOys1SWpepJJOYI6LwHgl0ms0sIk__y69dvKp6qmPR4HgGuvo4qEYF11e3nN7c0yD7Ej2-pYutzmY6o8FrgCY20icBtkACU0JFxX9tQwKWscpumLgE4rd2ro85_nswCiNj66VREe_RXXviIc5vLQA-lbSTV5OqaP4J-Bwx5a3Ny-M1brW9MFQ7roaiPPwyqffOmY_lKgwfjkHUZV7qdtPEdQ_bw0TlBqzU_ATyEGVyN7tbD6gGch2eVlGPvSNSAXd04ev-U0AcULbl2zQXRRZ9NY1-uHB7uZkwtbr7cCG4akrJSzKCut2Z9_zeqR2Lt5tYkk78cQ3Da-ZEujr8SMKfyJtHe-9nSuFxiAtWBXqxSz8SAlvjEaBgaHZLv6mO0AONaJXmj9IFmHb0Czu5hFxkYqdtb0-yQEwAmcEz8NUD0EhAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای زائران رضوی در مزار رهبر شهید انقلاب، در شب شهادت رسول اکرم(ص) و امام حسن مجتبی(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/680475" target="_blank">📅 08:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680474">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/680474" target="_blank">📅 08:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680473">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
هشدار آبگرفتگی محلی، و سیلاب در حاشیه و بستر رودخانه‌های مازندران
🔹
مدیریت بحران مازندران با اشاره به هشدار سطح زرد هواشناسی اعلام کرد که خانواده‌ها از اسکان و توقف در حاشیه و بستر رودخانه‌ها و مسیرها خودداری کنند.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/680473" target="_blank">📅 08:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680470">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e163d5cec.mp4?token=eJ9fMa2anCaTa7c-7gC8BlLXgO-h5j_JzwveON-NPnApRrsdVOY7gjau9gsjOZ4v2B34uzlWbMncZJzRlooIeUwznJ2YX3hM1Qar459LI85NYu3it3Ss6e222qIykkW6H8OEOA6VP1KtN6rRm8R1PTIdr64sCTKM6MMVWL585bBtVlujroRBcZp1KNv36vWWeQhCEY7AoI7S1jV-cbCDIDABM3GhkNXUWSLG_jsMFcc1zOYxe2GLwzZ85XBhBN3lEmQdvpxGC6xLArb_6qaCugLfBCaKmAOdBNVm8D45Ut8sqL1oysdvDb02Hp23GjBWAYWE9vBHC15e9NtkGT--Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e163d5cec.mp4?token=eJ9fMa2anCaTa7c-7gC8BlLXgO-h5j_JzwveON-NPnApRrsdVOY7gjau9gsjOZ4v2B34uzlWbMncZJzRlooIeUwznJ2YX3hM1Qar459LI85NYu3it3Ss6e222qIykkW6H8OEOA6VP1KtN6rRm8R1PTIdr64sCTKM6MMVWL585bBtVlujroRBcZp1KNv36vWWeQhCEY7AoI7S1jV-cbCDIDABM3GhkNXUWSLG_jsMFcc1zOYxe2GLwzZ85XBhBN3lEmQdvpxGC6xLArb_6qaCugLfBCaKmAOdBNVm8D45Ut8sqL1oysdvDb02Hp23GjBWAYWE9vBHC15e9NtkGT--Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار و مفسر سیاسی آمریکایی: مردی که خودش را در کنار جورج واشنگتن و قهرمانان جنگ آمریکا می‌دید در یک خودروی آشغال پنهان شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/680470" target="_blank">📅 07:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680469">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e17cd8159.mp4?token=PkNkjExrRoS3USkb_7mO4n0jEm33ZF2gHsOn7H0DtDzd6sTeoaYXopWtexeWnJT5whuBaGJAXh_m8rVbkNSfSTE_p2SFs7eQ5-mb_ITnfH1ynKD3jEilVkSr0-2aaMNGlazG1hnfNxygxDA9biFFXnKK0TtKodYzhW7PrCVgX_K8Pqwtz-uJrm7ENaC6nBxk505R_hxxdsrIFGKOTQjxSQqj5mMq8D_FT4g8ePlRrXCBnNyNpKcoeZnMAlewSA6YazH3a2gOXQZVmUuvr3EMMSK_vaCFxA2VEkmRgHiaN_sHy4BDCYQ2tzEVm1KSjMbAmvcWB4Oefw1P_8r_AIrOLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e17cd8159.mp4?token=PkNkjExrRoS3USkb_7mO4n0jEm33ZF2gHsOn7H0DtDzd6sTeoaYXopWtexeWnJT5whuBaGJAXh_m8rVbkNSfSTE_p2SFs7eQ5-mb_ITnfH1ynKD3jEilVkSr0-2aaMNGlazG1hnfNxygxDA9biFFXnKK0TtKodYzhW7PrCVgX_K8Pqwtz-uJrm7ENaC6nBxk505R_hxxdsrIFGKOTQjxSQqj5mMq8D_FT4g8ePlRrXCBnNyNpKcoeZnMAlewSA6YazH3a2gOXQZVmUuvr3EMMSK_vaCFxA2VEkmRgHiaN_sHy4BDCYQ2tzEVm1KSjMbAmvcWB4Oefw1P_8r_AIrOLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش کاربران خارجی به مخفی شدن ترامپ در کامیون آشغال
📲
🇮🇷
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/680469" target="_blank">📅 07:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680468">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQNuVJ-elCdEjts9ONdEEAdnDdjMBF0vSX-T_6b75kobWu_GDZNa7Vsrs-ZREv-belWu6ekOIixwexQdeWXJZqCsGNQubm-ps9mA9MgbHn6Xi2oeF9Trs5Mw3et1e3C6DvYmCuepQ9ud0FLNfXMJLquVLfxG3OKyhz4STm5IoewwCtUouNk-OLhgljIb6Wi3qYz-ViihjOCc-_WmMbqugIH0RAqmLzSyDr1WPPBhrsH4GPfyQ0BmbQSY7dz1Vn9zEjFHrTca6lZqKveNS_xsYYCOlP426APw11BmGiLN9S3OGtsigqYu2wN-A1AP92gN1GJrE8AarCtEg1BbZUVgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو: کوبا باید کاملا با آمریکا هماهنگ باشد
وزیر خارجه آمریکا:
🔹
کوبا تا پیش از پایان دوره ریاست‌جمهوری دونالد ترامپ، وارد آینده‌ای کاملاً متفاوت خواهد شد.
🔹
واشنگتن خواهان آن است که کوبا کشوری امن و باثبات باشد و در هماهنگی کامل با آمریکا زندگی کند.
🔹
این کشورها حدود سه تا پنج سال زمان نیاز داشتند تا به وضعیت کنونی خود برسند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/680468" target="_blank">📅 07:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680465">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
پنتاگون پس از یکسال تایید کرد که بر اثر حملات آمریکا به یمن در سال ۲۰۲۵، حداقل ۱۵۰ غیرنظامی کشته و ۲۵۰ نفر زخمی شدند.
📲
🇮🇷
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/680465" target="_blank">📅 07:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680464">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
واکنش کاربران خارجی به مخفی شدن ترامپ در کامیون آشغال
📲
🇮🇷
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/680464" target="_blank">📅 07:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680463">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAtlFrZK6ER2_WB8_sfDxgBd4XlvAId--W6hwV4E81dtjRTnxPCtAkPmX0QCfDedS45kSsv65FcXYUSvifTi5tiOMCtijJbNfkRncyX8ce99LHWcI1qcbdv7-BSNeK7Kke3SDq09CCoU52GMK_ZPetoo8xN18Zm6Rgsco7uUIG5OCV-d0XGvTs0yIFgKm3ydnJu5zLFlrXeF_1ohbNbdrhXt9WJgsIYFZR5gnymiCUjjgfHMQNjJ85wfc4jdOpQiMqM0VDmGVnfG1gFV_RJFip9Lyy3482hfc7LIPvJ6mGbwkga4Zxnhj5MKUgndSEXt-2XXcZcrDoshmutXHvujXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۱ مرداد ماه
۲۸ صفر ۱۴۴۸
۱۲ آگوست ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/680463" target="_blank">📅 07:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680462">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbERKI8qK_pZjKx6k9AoNjPDeR5OE29GI-TAxz1pvV2dEm5GuT0BPwqQwmdKNlWyLTsmeY_PV00MY1SwEWKcJF_NC4nzZgmJWKrVO5OrP36i3iV73Dvpx0ao3QBBV-xYzuXerD5Vztise4pBkBgrF6aXxmmMhAe7BOLzDUgsV9RimHr8webABRtK9MHejSfQZn5D-xtYd18I8H_mlzJ-6ph5M4jiiNMdOegBcJ_AVY3X5vy_PIQbiFkP2dpb0bYEEUhD8PuSvLuL-IeU2vh50VfuNcTmkfzxKCzG7UGhusBE_64UxJrCut0u9Tfe2nCDdroysdMScpoeAuEPs7aKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه‌ی حملات توپخانه‌ای رژیم صهیونیستی به غزه، اردوگاه البریج
🔹
منابع خبری فلسطین از حملات توپخانه ارتش رژیم صهیونیستی به مناطقی در شرق محله الزیتون در شرق شهر غزه خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/680462" target="_blank">📅 02:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680461">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وقوع آتش‌سوزی بزرگ در نزدیکی فرودگاه شارل دوگل پاریس
🔹
آتش سوزی منجر به بسته شدن ۲ باند فرود و تعلیق فعالیت های آن شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/680461" target="_blank">📅 02:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680460">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
طبق گفته برخی منابع انفجار یک تانکر سوخت در خیابان‌های اربیل، مرکز منطقه کردستان عراق تا الان علت آین اتش سوزی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/680460" target="_blank">📅 01:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680458">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a75ee87df.mp4?token=HwIgBuHoMRNVDSOssAzAuDXpnvB2RriB11J8FLWhcTj-gGGQhOBubZT9J67nSpgPvP4WKzeMDVYwkC11wfsHed1K53VxZ-0gjUvUsifMcTB-B-TmpVgxozcTjJL7KeX09Lq6Xowc60t2tx8iCkJaP-A9eKm0A7pEfzWlJ_qjg34UZ_FC7xkiiMoRQkmLfxShrcU0erw0ZBdsES6hZMx3vzA1ehN82xcwn6j52JIv1IP_WBH_G6D39DRZD2eqGJbQlOL4lxXw-5dMKzRlV3VF1PNFhw4YW0qzft2TOcqZspWopvTEQSZVB0pOxbCKlqMiElEC-LjLRhdVoM6IVkUQTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a75ee87df.mp4?token=HwIgBuHoMRNVDSOssAzAuDXpnvB2RriB11J8FLWhcTj-gGGQhOBubZT9J67nSpgPvP4WKzeMDVYwkC11wfsHed1K53VxZ-0gjUvUsifMcTB-B-TmpVgxozcTjJL7KeX09Lq6Xowc60t2tx8iCkJaP-A9eKm0A7pEfzWlJ_qjg34UZ_FC7xkiiMoRQkmLfxShrcU0erw0ZBdsES6hZMx3vzA1ehN82xcwn6j52JIv1IP_WBH_G6D39DRZD2eqGJbQlOL4lxXw-5dMKzRlV3VF1PNFhw4YW0qzft2TOcqZspWopvTEQSZVB0pOxbCKlqMiElEC-LjLRhdVoM6IVkUQTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر نزدیک از آتش‌سوزی گسترده‌ای که در مرکز استان اربیل، در شمال عراق، رخ داده است
🔹
گزارش‌ها حاکی از آن است که یک تانکر حامل سوخت در این آتش‌سوزی شعله‌ور شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/680458" target="_blank">📅 01:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680457">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f5bc3a1c.mp4?token=o6XEOKg3d27qM_G9uev2G8_ePT_oORllUpX9K2X1TiT3NjLudwusNq81N8FHOrIiYO5BLqABxcVAbTDAIaOHyCEgzK7sMV9UA1jWVnL2kSELPX0u-5Oa75DSb9hH-K4Ow2sOaJBtgFakAQTaf94sxgw8mEu4DvRIZZSUcGwwLwYsg-ZVxh_p-D_PoJt9pjiHfyD2V-VXjHPqwvk1lNojzaOywZUtnphSXh2tuSrs7RyCq0O70TQQIGN5XtPOZ1v4fB8NsJTMNVRDZHLOJ00lzjZclQirKyKNZ_Tzq0SxNumX2XV7h6OMJTEAeEUVvjZCs5-ZsHRf4x1K_2vtbZo6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f5bc3a1c.mp4?token=o6XEOKg3d27qM_G9uev2G8_ePT_oORllUpX9K2X1TiT3NjLudwusNq81N8FHOrIiYO5BLqABxcVAbTDAIaOHyCEgzK7sMV9UA1jWVnL2kSELPX0u-5Oa75DSb9hH-K4Ow2sOaJBtgFakAQTaf94sxgw8mEu4DvRIZZSUcGwwLwYsg-ZVxh_p-D_PoJt9pjiHfyD2V-VXjHPqwvk1lNojzaOywZUtnphSXh2tuSrs7RyCq0O70TQQIGN5XtPOZ1v4fB8NsJTMNVRDZHLOJ00lzjZclQirKyKNZ_Tzq0SxNumX2XV7h6OMJTEAeEUVvjZCs5-ZsHRf4x1K_2vtbZo6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش سوزی بزرگ در اربیل عراق
🔹
علت حادثه مشخص نیست.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/680457" target="_blank">📅 01:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680456">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5171ee4322.mp4?token=PNP5eQpDWG5ZJaC2aCLMtnsx3CAAKfYd3uHOUFUHRrP7hBP24Frp1fIaMdHyUPNGkWNRKRV2cBKCQkj6eUWTzNzHau5OOsorDCECf46qbpamzT3iq99ZIOI_VFYMgBe7TWjmH903JeYi6b5EGjfWq6MJbT-Pq72zCOhd7uD6Murm8KwcMROxL-gan7nIV5XnG4dNVK7v5ts6sFZp5IgyrbH3TRuASzXVj93ZGeN5-EwJ77yAviAUHMpH2TPT6QNVAaeG6SwYlK6OyU_ys-fNs6mSbUyyja8ii5X2lg9dNMfKM927lqNeqHspX6IyuWUoKsU0QVppss_E3jJyrwpU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5171ee4322.mp4?token=PNP5eQpDWG5ZJaC2aCLMtnsx3CAAKfYd3uHOUFUHRrP7hBP24Frp1fIaMdHyUPNGkWNRKRV2cBKCQkj6eUWTzNzHau5OOsorDCECf46qbpamzT3iq99ZIOI_VFYMgBe7TWjmH903JeYi6b5EGjfWq6MJbT-Pq72zCOhd7uD6Murm8KwcMROxL-gan7nIV5XnG4dNVK7v5ts6sFZp5IgyrbH3TRuASzXVj93ZGeN5-EwJ77yAviAUHMpH2TPT6QNVAaeG6SwYlK6OyU_ys-fNs6mSbUyyja8ii5X2lg9dNMfKM927lqNeqHspX6IyuWUoKsU0QVppss_E3jJyrwpU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش سوزی بزرگ در اربیل عراق
🔹
علت حادثه مشخص نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/680456" target="_blank">📅 01:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680455">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-q5aft8N8AggG0ih-WwRg05oUuvuQK2pNX8cmTebvQXsB3QoflhIQAsV93-cwYwe2_M1wAb0LWwXzsyQGDaVg6QZqRE0RbBp3JTpNl2RyOohAOo7pj7P0IWcfBUGVRJfU5gl2HBSj6mCOowstJF0t-hbKD5Yh0pykI9DuhrZ_Gd_F0QtKMECeijtaoRHVvXth_H6tM4joOWeWSZ0MKrfrm-R1TgAU7Ix5ulI5vQNcpf53WX5pchr80nIAWrLoMrFOrAoc8MqaqveMfViE-8--MUJYzLMNJxw3chw-rlE_Dti6ncZQE_r_h9MffQ_3EPW6OG2Vi_pZh9MCiZmw6sEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: کاش رئیس‌ جمهوری داشتیم که بزرگترین جوک و مایه تمسخر تمام جهان نباشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/680455" target="_blank">📅 01:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680454">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04361bf871.mp4?token=uAtZP8vB6bABoBAHTXncd0NGig_HYQD5qkz_ZWRTH6z14Ivq9hOKVwvjj0AanNPPqbdxDDJOZ8NXiEqxnxHzxBPQBLpoOkrai62DDQ6r8ptvOPexCsBp_Pr6tLAyzZa9xHHIypnqqOziWn9sgb__SjskCInPb5bJC5T2WgpeeaSrCCm8BXdYPbtiv8aAhZhYRL99iZkQkqigUJie5OPY9_Ri6_mO9v5WMGbrRW4phDJgccTFWsKviho0uuN72qvFQ8rHHCiVh6y4WuiAU2ngyxq_Noop6HJuat-sBElLJT8YFxbpsx2fXZyOhseV465IM-BujQOmy4zu6LTW9HvdFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04361bf871.mp4?token=uAtZP8vB6bABoBAHTXncd0NGig_HYQD5qkz_ZWRTH6z14Ivq9hOKVwvjj0AanNPPqbdxDDJOZ8NXiEqxnxHzxBPQBLpoOkrai62DDQ6r8ptvOPexCsBp_Pr6tLAyzZa9xHHIypnqqOziWn9sgb__SjskCInPb5bJC5T2WgpeeaSrCCm8BXdYPbtiv8aAhZhYRL99iZkQkqigUJie5OPY9_Ri6_mO9v5WMGbrRW4phDJgccTFWsKviho0uuN72qvFQ8rHHCiVh6y4WuiAU2ngyxq_Noop6HJuat-sBElLJT8YFxbpsx2fXZyOhseV465IM-BujQOmy4zu6LTW9HvdFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دمام‌زنی زائران مشهدالرضا(ع) در خیابان‌های منتهی به حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/680454" target="_blank">📅 01:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680453">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
اخبار غیر رسمی از انفجار در منطقه سیده زینب (س)
🔹
منابع عربی از شنیده شدن صدای انفجار و تیراندازی در منطقه سیده زینب (س) واقع در جنوب دمشق خبر می‌دهند.
🔹
تا این لحظه گزارشی از ماهیت این رویداد منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/680453" target="_blank">📅 01:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680452">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPzaGxNajwcm_Y0JhuKcHKBzBrhxWES2iDxN2RFC89Oq_L4tpB818Vk7qpx_KzwFCpu7K_p-33hb0qzq5PZ7dYBMlJMD1xyZTK3f3_nkksLeS8eMYfRSE2xj40nuCDBMrP53lA4BwFXyAZTgtWehMUgZXwettixfX5DviDPGmX0FCxntDcqCk4emK9BIsoU--y-qThGjOxreTZYuc8O8xRFyUzMEBugeEEtTrHYAh0x1fX11T8dBKa7Ge9sHZdRmIDkI_4SmEgnqGVKjQXwZRHZZkYCl6cmbrFf4py8qrI3_FU6m0182WVuaYQ0GdQk_xb-lgAcekJKRG5ogzpCOtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر ژئوپلتیک آمریکایی: توازن قدرت در خاورمیانه به‌طور دائمی علیه آمریکا تغییر کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/680452" target="_blank">📅 01:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680451">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
حملات توپخانه‌ای اسرائیل به مناطقی در غزه
🔹
منابع خبری از حملات ارتش رژیم صهیونیستی به مناطقی از شهر خان‌یونس در جنوب نوار غزه گزارش دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/680451" target="_blank">📅 01:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680450">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c3772001.mp4?token=WK0lvIkscEJ8ug4Fd5pzzP0au9cYhUuh0y8L81_o-D0N2TeXQ7dwkjS85eTpHlDctHmwVUZ9ziwsn6wnKYTuFFzBitZhms8PHRsEYf4KQKtbbLy4bwYwe6DEQhr3-QjOEsIrZdIbdSvA8CTU21qVKTYpBkOhAvGKIjr8A52ixrvWCdKHgcQLZCVk8nHbxVbtbfv20WAVrvmsXQGguSsTxv20FvvUEBIYwmvb-K24Y1wBukhJ2EY1AVK5Dp7uJvBHu95yPOHDnbBINjUb5G2FqA4N19KQ6h9KNGHZeHOtATeaam8NZr0zo2ItZ7PGZCuj1RIe2rUvzGMHObtEtmTXwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c3772001.mp4?token=WK0lvIkscEJ8ug4Fd5pzzP0au9cYhUuh0y8L81_o-D0N2TeXQ7dwkjS85eTpHlDctHmwVUZ9ziwsn6wnKYTuFFzBitZhms8PHRsEYf4KQKtbbLy4bwYwe6DEQhr3-QjOEsIrZdIbdSvA8CTU21qVKTYpBkOhAvGKIjr8A52ixrvWCdKHgcQLZCVk8nHbxVbtbfv20WAVrvmsXQGguSsTxv20FvvUEBIYwmvb-K24Y1wBukhJ2EY1AVK5Dp7uJvBHu95yPOHDnbBINjUb5G2FqA4N19KQ6h9KNGHZeHOtATeaam8NZr0zo2ItZ7PGZCuj1RIe2rUvzGMHObtEtmTXwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر صهیونیست: نمی‌گذاریم غزه بازسازی شود
🔹
«گیدئون سعر» وزیر خارجه رژیم صهیونیستی با بیان اینکه یک سال است که غزه بازسازی نشده، گفت که نابودی تمام سلاح‌ها در این باریکه یکی از پیش‌شرط‌ها است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/680450" target="_blank">📅 00:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680449">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3b82593b.mp4?token=iRyBsajB1p7PNKUI6AeLCeYyeUOBMz54DAG6JQ8untjNQjcHUjG2LDu4911qaH2oRgKtiIR2DdTflAkSc_AU1ToFsYOj-m0EbfIY_OR1iUtvNitoaUxnV8xXoa_cBeI6uNy6Dr4XeI3OatjHpA7KKmI7b5ReZw5yNxFjs5X5WxGpO8oOnqpxjB4ae_ftYaADYmBpESrlWU3u2blgFK6shaB0mXQJzeViXqkS2ATgNeV_RPEBoPnah-R73_VMOEYFockylAhaQK3TsAsrRCq9gVk3uw7aUaevGqlyPPCoyJEXk-mjUu364_Blwb1AdXyWt40Dcx_dB7MtK4fuBsD9qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3b82593b.mp4?token=iRyBsajB1p7PNKUI6AeLCeYyeUOBMz54DAG6JQ8untjNQjcHUjG2LDu4911qaH2oRgKtiIR2DdTflAkSc_AU1ToFsYOj-m0EbfIY_OR1iUtvNitoaUxnV8xXoa_cBeI6uNy6Dr4XeI3OatjHpA7KKmI7b5ReZw5yNxFjs5X5WxGpO8oOnqpxjB4ae_ftYaADYmBpESrlWU3u2blgFK6shaB0mXQJzeViXqkS2ATgNeV_RPEBoPnah-R73_VMOEYFockylAhaQK3TsAsrRCq9gVk3uw7aUaevGqlyPPCoyJEXk-mjUu364_Blwb1AdXyWt40Dcx_dB7MtK4fuBsD9qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک یک سرباز روسی که با استفاده از یک سیستم شلیک همزمان، به یک پهپاد اوکراینی که در ارتفاع پایین پرواز می‌کند
🔹
این سیستم مستقیماً بالای کامیون‌ها نصب شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/680449" target="_blank">📅 00:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f933dd533.mp4?token=p4oBf9Ba0XFNhVOhpvZUJOnCVL34PIbOVVvhO1iQFfNTucUf4BHzOI6lgIhj955Xah0RaViWW6R174glOZxLXEuAKfrikk23NGnEE5ErBJmfFLpYrn5DhZTYDf_BfCEYrn9FtYT7HI34VvzTnx_7nhf-GyZY9sB2wdJ_Ec6161_LGdh3O91eWxMG1Yc8hptSxNfZ3EY_zmal6vY3CSVrpZF44mJm8PJ39hLKfTQyiCUR-ai6_pXDrmoDtvmrNkJmtRoyDq4AwudyGxlByxWidXdydh-lGW5T7fAoPa86EdHj1DNQn7IKdPdNhr1ummphTXSKSN4TAyxmy2IkjSVYvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f933dd533.mp4?token=p4oBf9Ba0XFNhVOhpvZUJOnCVL34PIbOVVvhO1iQFfNTucUf4BHzOI6lgIhj955Xah0RaViWW6R174glOZxLXEuAKfrikk23NGnEE5ErBJmfFLpYrn5DhZTYDf_BfCEYrn9FtYT7HI34VvzTnx_7nhf-GyZY9sB2wdJ_Ec6161_LGdh3O91eWxMG1Yc8hptSxNfZ3EY_zmal6vY3CSVrpZF44mJm8PJ39hLKfTQyiCUR-ai6_pXDrmoDtvmrNkJmtRoyDq4AwudyGxlByxWidXdydh-lGW5T7fAoPa86EdHj1DNQn7IKdPdNhr1ummphTXSKSN4TAyxmy2IkjSVYvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پارسال همین شب‌ها؛ خادمی سردار شهید تنگسیری در حرم رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/680448" target="_blank">📅 00:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27b1027df.mp4?token=P-cVOjHBWyYs3UQ-d3wqAUmMBaJXs_IfnGeWMnygTEv1HENUshZt7i_KJ13gQpZxkMjARDYNFiYOiKXE87L08FBNcKLfO2u2IUZh4zVAL6UIl3AGlqNW4OuDpXQ14-S1QlJHTtX4NwNrhq8QhqQePzs3TxgeDN4PoJJjvZNAWIP5RFg-zztaA0W7kdiDTIraqqlO8SYi_63zFpUtyemfufSU4AK53Wugs_uZS9rOOWOOcwW0eyPbKZr_C6xigHVOolOhvXfpR01CPM3O7-MDAABTBf-7vM0HM9I9A8jdb-OBe-HwwHL2cvJHmM3lhKOc832StTU7inal4hs4faSo9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27b1027df.mp4?token=P-cVOjHBWyYs3UQ-d3wqAUmMBaJXs_IfnGeWMnygTEv1HENUshZt7i_KJ13gQpZxkMjARDYNFiYOiKXE87L08FBNcKLfO2u2IUZh4zVAL6UIl3AGlqNW4OuDpXQ14-S1QlJHTtX4NwNrhq8QhqQePzs3TxgeDN4PoJJjvZNAWIP5RFg-zztaA0W7kdiDTIraqqlO8SYi_63zFpUtyemfufSU4AK53Wugs_uZS9rOOWOOcwW0eyPbKZr_C6xigHVOolOhvXfpR01CPM3O7-MDAABTBf-7vM0HM9I9A8jdb-OBe-HwwHL2cvJHmM3lhKOc832StTU7inal4hs4faSo9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند گاز خونت را مثل روز اولش کن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/680447" target="_blank">📅 00:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680446">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
درخواست محرمانه عربستان از یمن برای پایان درگیری
🔹
در پی ضربات موثر انصارالله به مواضع ارتش و مزدوران سعودی در یمن، ریاض در پیامی محرمانه به هیئت مذاکره کننده یمنی ابراز داشته که خواستار پایان درگیری و بازگشت به توافق سال ۲۰۲۲ ریاض-صنعا بوده و این درخواست را به هیئت یمنی منتقل کرده است.
🔹
این درخواست با مخالفت مقامات انصار الله روبرو شده است. صنعا پس از دریافت پیام عقب نشینی ریاض از مواضع خصمانه اخیر تاکید کرده است که به دنبال دریافت تضمین‌های جدی و واقعی برای تامین منافع ملت یمن به ویژه در مورد پایان محاصره، دریافت غرامت و پایان دادن به مداخلات عربستان در امور داخلی یمن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/680446" target="_blank">📅 00:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680445">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
پاکسازی در موساد؛ ضرورت امنیتی یا تسویه حساب سیاسی؟
شبکه المیادین:
🔹
دستگاه جاسوسی رژیم صهیونیستی در مقطع کنونی با بحرانی چندلایه مواجه است.
🔹
بحران کنونی موساد، با برکناری دو مقام ارشد این سازمان، فراتر از کنار گذاشتن چند مسئول اطلاعاتی است و به ماهیت رویکرد امنیتی این دستگاه مربوط می‌شود.
🔹
فاش شده است که موساد در طرحی برای ایجاد بی‌ثباتی و تغییر ساختار سیاسی ایران، از شبکه‌ای از عوامل و نیروهای داخلی و همچنین نیروهای کرد در مناطق مرزی استفاده کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/680445" target="_blank">📅 00:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680444">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8e4ebf62b.mp4?token=FlGi4qYQYwAjshmdnKVcu7ffNJnYeoB2dz5sSDWGvC7h83LM4ElJUeEejDOwO005eqiMHh-18ftjV3ucXJcZMg0iHikiVkEMm02cOfzcSLNFsptenHlBmLtCLbGkD_RzodaS1PrXrMzxmA6rNlphMpGyMLYQd_tK93EcN8RqSdvaKXKVsjhlz6LM4u2SvB6x_QvGKstF_whK3obkET3nc53qzY7JwnRPTsQ9lrypWQy79WQDKk-HrxocmnfmFNsYAjHFg1joBBK3LnL__bqsFiIEhaw4S8IvZ8p4aqLIjDScU0NPpexiqDBOYMnUAdp9THEBSqfnB3zdxxLmLX16JX3LRAwDtM1_piD4GzA3__S_-hwreb_LrBdQ-tmGF2x2Q71Q-GHv3mW5iqLez3WaBE04Qr0Fyk7z3TTcu3W8Kq-Vps9VMQiw-bV8jqer7yliuMyoFs3vvipEHlgaBzOY6d-Xs9gaxx2A0lk77Vcf8PZFYd16ROUQx7I0BHRzxznkgLpMTd4BWFpyfDns8pXjkzXrw0TwpkWcKzMTzPrIS8lArPQk_u3dJBCLKAd6U5jCzO72AlY69VPzZvkvblpWPbIHKjuysuSROaFLEKs6vS4fxpxuevAq8zi48724xTCBFC3B7Potn7m0gqe85eAWqfdBuL9mFbGF5ghzu3ANzOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8e4ebf62b.mp4?token=FlGi4qYQYwAjshmdnKVcu7ffNJnYeoB2dz5sSDWGvC7h83LM4ElJUeEejDOwO005eqiMHh-18ftjV3ucXJcZMg0iHikiVkEMm02cOfzcSLNFsptenHlBmLtCLbGkD_RzodaS1PrXrMzxmA6rNlphMpGyMLYQd_tK93EcN8RqSdvaKXKVsjhlz6LM4u2SvB6x_QvGKstF_whK3obkET3nc53qzY7JwnRPTsQ9lrypWQy79WQDKk-HrxocmnfmFNsYAjHFg1joBBK3LnL__bqsFiIEhaw4S8IvZ8p4aqLIjDScU0NPpexiqDBOYMnUAdp9THEBSqfnB3zdxxLmLX16JX3LRAwDtM1_piD4GzA3__S_-hwreb_LrBdQ-tmGF2x2Q71Q-GHv3mW5iqLez3WaBE04Qr0Fyk7z3TTcu3W8Kq-Vps9VMQiw-bV8jqer7yliuMyoFs3vvipEHlgaBzOY6d-Xs9gaxx2A0lk77Vcf8PZFYd16ROUQx7I0BHRzxznkgLpMTd4BWFpyfDns8pXjkzXrw0TwpkWcKzMTzPrIS8lArPQk_u3dJBCLKAd6U5jCzO72AlY69VPzZvkvblpWPbIHKjuysuSROaFLEKs6vS4fxpxuevAq8zi48724xTCBFC3B7Potn7m0gqe85eAWqfdBuL9mFbGF5ghzu3ANzOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: ایران عضو بانک بریکس می‌شود
رئیس‌کل بانک مرکزی:
🔹
مهم‌ترین نتیجه همکاری‌های کشورهای عضو بریکس، تاسیس بانک توسعه نوین (بانک بریکس) است که کشور ما نیز به زودی عضو این بانک خواهد شد.
🔹
همکاری‌های خوبی بین کشور ما و هندوستان در زمینه‌های پولی، بانکی و اقتصاد دیجیتال آغاز شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/680444" target="_blank">📅 00:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680443">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای وزیر انرژی آمریکا درباره صادرات نفت در تنگه هرمز
وزیر انرژی آمریکا:
🔹
میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.
🔹
میزانی از نفت از طریق خطوط لوله و تاسیسات صادراتی ارتقا یافته‌ از منطقه خارج می‌شود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/680443" target="_blank">📅 00:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amq3TYxnD71vXd83DZc5UHPvDoLVwccrf8MHOP7an1qHYGtu6N59Ea9o5RovnU_STOBkNUJ27hN8CrJF9ub_qBLO_LBRYuLCcWMxibNSKENY71OSk6lOvJmm1M8SylZZKqsmfDV5SYomN4BrDore_7GoSQbmgPLKfXo8cO8xXAY4COCtu0qyg_JOSwRgiBJZWOJe4NCwoj72utGuaXpsnH7K4kYaqNKaH2yugC2jI-ReWT84bOpP0_ttGl2mKtl6gxZXAMJE4tDFpuG9K73PpOEQ2PHm8pTsZAzKIIrumBZv1Ojqzvi6lGffXB225zm01fiDIZudfjcCan4LYsT1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/680442" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680441">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
فرماندار شهرستان قشم، پرواز هر نوع بالگرد آمریکایی در محدوده شهرستان قشم را تکذیب کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/680441" target="_blank">📅 23:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680440">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRNwf8HAC-njTNSoYsHxSZZcapowxgf_r67SVy8lFupd26d1U3tExnWJyFxhujrT6aeG_1iiKItrkSjLC0cfBWGKCERXguz5YpaJvVG3lOUjcRp5mb7AcZ2b-Ly8oHVv_CnPGFNtHvVvni_U9opzKNqOSWNkz5gn42DVYNHfhoUP1bSvVJSzNbz2IiqttunB7ifAnwgLhYlrKsdKb_D4MpKmMAPjzX8QmHHgKM8Xlz4Z85F6ahgT5X2z9RS80iX1bgUexy6ysRiFQ2-TboAjdqTLeMqABsGFwQ5ynUE17Pq5uaRtEf9Pe2DErGP5XR05m30TIz9sSjQCZHoLzFaOAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع خبری از حمله‌های هوایی، توپخانه‌‌ای و تخریب خانه‌ها در نقاط مختلف جنوب لبنان از سوی رژیم صهیونیستی خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/680440" target="_blank">📅 23:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680439">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ویدیویی از دیدار وزیر کشور پاکستان با رئیس‌جمهور پزشکیان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/680439" target="_blank">📅 23:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680438">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PubGat7UsvIYF7q5N8seiPobqCL8p6Jg2QHDh6iVZtT3SH0lpEb1zuMnJyGOn4SYMEHw_mtfEeYhcxK9uJxVGI8rAZ-qULw4fpkk4m4Kd07OuFzIGWjXpYXWi8EPtthUCmwY9NAMaT33ruzXgU0vaDvnY20klg2yDO4IWqPvIv9wbw_GeiNzoPWJl_EqLKosWv7W8NUabrL0xe6RAZSQdyhmfjI1H5Tp7Hd8116HyW7bofywf-n1XkK-98xHBU-lCnPyL7JIN2fRq6rbBv62cQlwyQQpofHhtQjL-JlCa0tBPm_MJJEtgpB_VVX6666Y-C3TfKEVT86eKLrv2uVKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌سوزی مشکوک در نزدیکی فرودگاهی در واشنگتن
🔹
رسانه‌های آمریکایی از آتش‌سوزی در نزدیکی فرودگاه اسپوکین در ایالت واشنگتن آمریکا و توقف فعالیت در این فرودگاه خبر می‌دهند.
🔹
آمریکایی‌ها تاکنون علتی برای این آتش‌سوزی مخابره نکرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/680438" target="_blank">📅 23:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680437">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgYkK3MDz99iKf-qyckGGS3qhtvT88W8PSw0Y9xJLfMGqzQvAbKSLsFV26pWa-oVdXeTyOmYHRet6GjOOui1N6SM3vBwlm82icnx59CTR6_bRi09IiXBaYwCAM7yWETEIrJvXW4n4G6-U3fFrbBcyL5jxvXHqJwf9yqZSyRMh0dHE8yXT5QS6keUYUZMWoHb_D4czkYZPcd8Imk-eAc0MWsMrEyE2QhMTIAxrR_8wLpycr4_Id50eHJH3L0ngpT9Q1zMMwrJJmvQYmKlDAV4iIPcyna4g41Up7_dIkRvc96ukgfnCU_kX2-N9yLubM-NBH3MYOssfyxbYLNo5UqiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار فعالیت سامانه بارشی جدید؛ تداوم موج گرمای شدید در یک استان
کارشناس هواشناسی:
🔹
سامانه بارشی جدید از روز چهارشنبه در چند استان کشور همراه با رگبار، رعدوبرق و وزش باد شدید آغاز می‌شود، همچنین موج گرما تا روز جمعه در استان یزد تداوم خواهد داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/680437" target="_blank">📅 23:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680436">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به جنوب لبنان
🔹
شبکه المنار گزارش داد که جنگنده‌های رژیم صهیونیستی دره الحجیر در اطراف شهرک دیر سریان را بمباران کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/680436" target="_blank">📅 23:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680435">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMfrp02HC8psO1WI13fupOZH1Eoz6G4vQrYOU5C20iuZAF_z08RgLpfzi35mhQodL85n-Haz0nSulkqzlaRjTWGmNIqpg8jMrm7fL0Eii9fKxwGAhvRwx2uceTN1HLJGfgR2b-3wFNWz9DDPzpeFRPRzvfoN3fYkakC4aOG2LRCY2sdEkp-SAluSNO6IBybZduS4YH-GCO5qaGK_WWgxsD121MkvUOY3IrGfUMbD9WraTe0FzkB-oLhurTr34CA5EtHtIzjsBR0JCAKmsWKrmtXnTIAM4bW8BKdthfXsKZK_GeoeFB7xk16WnIDos_2GiFGQS0SGI-bm7dQU8aHDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه بقائی به آمریکا؛ آیا جهان در حال بازگشت به دوران «غرب وحشی» است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/680435" target="_blank">📅 23:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680434">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سردارنقدی: تولیدات موشکی و پهپادی ما تمامی ندارد
🔹
ما بیش از نواخت شلیک موشک‌های بالستیک تولید می‌کنیم و به دست رزمندگان اسلام می‌رسانیم. در حوزهٔ پهپادی نیز قابلیت تولید ما بسیار بیشتر از نواخت شلیک است.
🔹
اگر جنگ چند سال هم طول بکشد، باز هم موشک‌های بالستیک…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/680434" target="_blank">📅 23:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680432">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5981ac86.mp4?token=kc51Et97SxnEeoz0DsEINHVmEByflJbVMJkQH1s1Q32e3tX5wj1OhDUffdCY0iOKydK6LLO4Gd_Q-32kZ9UyCDKNfVgZ-K5piMON2uGt9p9KulXl_EPl3BO81uYWmTr4BuNpagWfrrpCM6NsNwi_h20WUWoe-VxvJgUmq1zdXgwcyKozLRfxG4UIfU3rr1W-lvIz2ReDGeT0kdXhLGATtyNkYIHX5dO7r8BGk9WQPVFgigMYVgsNLr_3puAZEBqRE9xLw2T8hEsKq1IPDC5rAA-Rgik7MODrLgmknZC2JqmssMyKODi23jQr8ccKYXIg5uNciGhzuVSg1hSj7uKqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5981ac86.mp4?token=kc51Et97SxnEeoz0DsEINHVmEByflJbVMJkQH1s1Q32e3tX5wj1OhDUffdCY0iOKydK6LLO4Gd_Q-32kZ9UyCDKNfVgZ-K5piMON2uGt9p9KulXl_EPl3BO81uYWmTr4BuNpagWfrrpCM6NsNwi_h20WUWoe-VxvJgUmq1zdXgwcyKozLRfxG4UIfU3rr1W-lvIz2ReDGeT0kdXhLGATtyNkYIHX5dO7r8BGk9WQPVFgigMYVgsNLr_3puAZEBqRE9xLw2T8hEsKq1IPDC5rAA-Rgik7MODrLgmknZC2JqmssMyKODi23jQr8ccKYXIg5uNciGhzuVSg1hSj7uKqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت سالروز شهادت امام رضا (ع)| حاجت‌روا
🔹
صداهایی از جنس امید؛ روایت شما از کرامت و نگاه ویژه امام رضا (ع) در زندگی.
🔸
الوفوری را دنبال کنید
👇
#حاجت_روا
@Alo_fori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/680432" target="_blank">📅 23:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680431">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSJ6VPfK7UN7zgJuArVzchuabRlG9W-m2dIRyluHQR1iZ6n9MVE9btCwGDKz9hHJsVZvcZbMtloYHDEFHQ4iXZVa6_XGbWejXbQeWOkXfghZ6Nm4G2nbEy30TDqYbFCgZgYXoYeXgO-Tili5_sgaEht_BlL2-0snI-SwQ44INTUT4OUyeQBQt_3y_WENNvtm-dYwFU7xPmWdeqmPkqpYdlUppbY_u5cYweNb2sV4i3IgaqPrtyoOd_6m0b2sMxDSbKdQHzN-tw9mLy5ULJAX-7QZGBabhyBK3q8IOW0AjisG94VjXXmGONCXkUWJ2GzJ9McYpwfbkydabIiT10dAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ری اکشن جالب یک مخاطب به رفتار دیوانه وار ترامپ
🔹
بزار ببینم‌ درست متوجه شدم ؟
🔹
ترامپ صدها دختر دانش‌آموز را کشت، سربازان آمریکایی را کشت، صدها نیروی نظامی زخمی کرد، قیمت بنزین را سر به فلک کشید، ذخایر موشکی ما را مصرف کرد.
🔹
همه این کارها برای این بود که در نهایت به ایران اجازه دهد کنترل تنگه هرمز را به دست بگیرد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/680431" target="_blank">📅 23:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823f7565ed.mp4?token=qBrBToiMtckkbJTe1WucKYwWb-c6_a0m8S14fibkedCBJVPVhTE17pczTVJAcRtcdJ5DFoOXShOgqDLH7shmPV1bRbPoEZfbTXqrk5M119xEJ41I1EPw1D4Ty9OrFAuJSZeWfpFHWKgOqBWaIpWJUkZavtRn00c3AlUFjoECyZzdDj8jX9vzvDoAeeXP390kxxQUYruxsGVS3f-BvyEv3tOaZ4JTb52IKiC8vlO7XWsuRF8tcjntumq2Hm_7yLviwuvz-lATMZxwAqmwId2EZvAUfuS9rEccJFT1LvEh_8EMzEsbEJQBODRP4llCjWo7m66r-keoK03zSirONqTSQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823f7565ed.mp4?token=qBrBToiMtckkbJTe1WucKYwWb-c6_a0m8S14fibkedCBJVPVhTE17pczTVJAcRtcdJ5DFoOXShOgqDLH7shmPV1bRbPoEZfbTXqrk5M119xEJ41I1EPw1D4Ty9OrFAuJSZeWfpFHWKgOqBWaIpWJUkZavtRn00c3AlUFjoECyZzdDj8jX9vzvDoAeeXP390kxxQUYruxsGVS3f-BvyEv3tOaZ4JTb52IKiC8vlO7XWsuRF8tcjntumq2Hm_7yLviwuvz-lATMZxwAqmwId2EZvAUfuS9rEccJFT1LvEh_8EMzEsbEJQBODRP4llCjWo7m66r-keoK03zSirONqTSQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: پیروزی ما حاصل حضور مردم در میدان و نفوذ در جهان بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/680430" target="_blank">📅 23:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680429">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5tYcpeTkLQKidzLjfUnfKiTMiCpL14x2rYKjM7qgU3MX1xnO5S-OKnfSjB0bMEfEGIdF1M2PgKhaFlxWQRyC8N60ocCqqdeTYqPCauTEMtJSX5r31qhKR783xYEYtFnuwHs-FvNem7w4lDEi4ptEppwuKKVIaD3oLmMzKJaQ-0Hf5UD5C_gta4ITGDrLINT2fHXzu2aXLJcVqRyKqofcGVm9g9Kk_LxSKa-A76_8GGhWOBkmu8bP3ISeBlxmF00Et3snZWMlGSzCcLkZscQKsLZs81bUhfJuTZbuZfGIUYdIQnKttjAcbm4LAD2-Y4aTAdHirMqk19zt-3sLhTYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست اینستاگرامی رونالدو برای ازدواجش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/680429" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680428">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
محسن رضایی شروط بازگشایی تنگه هرمز را اعلام کرد
👇
khabarfoori.com/fa/tiny/news-3237163
🔹
ترامپ چگونه در یک عملیات مخفی از ترکیه خارج شد؟ | فرار با کامیون غذا
👇
khabarfoori.com/fa/tiny/news-3237044
🔹
عکس های خانوادگی حمیدرضا رجب زاده مداحی که به قتل رسید
👇
khabarfoori.com/fa/tiny/news-3236968
🔹
محاصره دریایی از جنگ هم بدتر است و باید بشکند
👇
khabarfoori.com/fa/tiny/news-3237132
🔹
بشار اسد به اعدام محکوم شد
👇
khabarfoori.com/fa/tiny/news-3237066
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/680428" target="_blank">📅 23:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200c140ffa.mp4?token=N6q7YURVHJiRh1spcRxhVzS13_chJRXwT2VSXfst-LjYwy2JoUptc4dtPaCrc2kCreQV_CaROk0zH6sbb4wfNW9sUuPPpsLDBAFNAR9_zjmE_ITSzuWSwQ997i3OQBzlv2-HsZt2602yx_VuT_ax-jFWBdD-FNYKIbCfPWBu3GVb50krVk857jRKhDtcsD19VMK0o8AnCrT0FKKb66ynDJNKVlcAzv3LITUPjpsnzImxy7GxQ_XADsw7i7JjelzEoPWEqPnKFLVkB2VXXIOQIcr_BljDZo42q2kFESVgJ_fXAbXcF5HI87jFVyuxpW44C4TAPZNIf3um6rlZIcV8TDXPcHuzE17VKtg01Yh7yJqNesX-RgdsL6J-8odzE79UtQVg2d9tMn5JTqla-MHuGq1sOqfZYQ693ds_NncFQTSy3tTliGBbwrggmEfwCyK4p7CUfERyCaC6C2gUo9mpN6AXYhaOR7ORR0oRuuGEeUqCjdw2ze199vZqhAJRB-XgHYckwUjvm1ssRB_daAlFfTfTSOn96h76vmtn8tF48Gq0ZOlj9C9pJF7jIvLN5Sg5HzJFeyr6itJzJhgAtbhxsRLFXqJmMeUVl1pUWRwC08CF2eYZaASjTiXFyTq7g-RINKp3UpWPbZbAKx41rzY9egO-BjCZ1Py9NRze7-YGUcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200c140ffa.mp4?token=N6q7YURVHJiRh1spcRxhVzS13_chJRXwT2VSXfst-LjYwy2JoUptc4dtPaCrc2kCreQV_CaROk0zH6sbb4wfNW9sUuPPpsLDBAFNAR9_zjmE_ITSzuWSwQ997i3OQBzlv2-HsZt2602yx_VuT_ax-jFWBdD-FNYKIbCfPWBu3GVb50krVk857jRKhDtcsD19VMK0o8AnCrT0FKKb66ynDJNKVlcAzv3LITUPjpsnzImxy7GxQ_XADsw7i7JjelzEoPWEqPnKFLVkB2VXXIOQIcr_BljDZo42q2kFESVgJ_fXAbXcF5HI87jFVyuxpW44C4TAPZNIf3um6rlZIcV8TDXPcHuzE17VKtg01Yh7yJqNesX-RgdsL6J-8odzE79UtQVg2d9tMn5JTqla-MHuGq1sOqfZYQ693ds_NncFQTSy3tTliGBbwrggmEfwCyK4p7CUfERyCaC6C2gUo9mpN6AXYhaOR7ORR0oRuuGEeUqCjdw2ze199vZqhAJRB-XgHYckwUjvm1ssRB_daAlFfTfTSOn96h76vmtn8tF48Gq0ZOlj9C9pJF7jIvLN5Sg5HzJFeyr6itJzJhgAtbhxsRLFXqJmMeUVl1pUWRwC08CF2eYZaASjTiXFyTq7g-RINKp3UpWPbZbAKx41rzY9egO-BjCZ1Py9NRze7-YGUcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر مقاومت کردید، آن وقت قلّه را فتح خواهید کرد؛ کاری که از بعد از زمان رسول خدا تا امروز انجام نگرفته، این کار، کار شما است.</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/680427" target="_blank">📅 23:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680426">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6cb1de1d.mp4?token=M7ev7awuO_1RUqYl2jRFUcjJGqXe5AxUrljIYevPSGuHwSFClujLipd9ZSl2M01OwC53POuWFnvu_4KhuAz6bGo8GTnDIfWolB-anVtlaiJd1fpaqiauNxZUwK4goAswdv9KKRrh1xjE3aC_7jIZ1U0KDW8oJL4G4DzQ75EX7hZP3VXCjHE_8wWZ4Ps_BxxXnicqeSK9PA8hhbH295Ka2BD4Hn2rFUvzf7y7hBlTR7eXzQP28cOsg9VkZuWnH7NAfoTZlPjzv4ZDhjAXgpR80WlThlhCqIxIXl8kXISl34rXPcGhpfU4jS8rvRRmjOLflI5QhCEO2Ce8gMo5uYrP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6cb1de1d.mp4?token=M7ev7awuO_1RUqYl2jRFUcjJGqXe5AxUrljIYevPSGuHwSFClujLipd9ZSl2M01OwC53POuWFnvu_4KhuAz6bGo8GTnDIfWolB-anVtlaiJd1fpaqiauNxZUwK4goAswdv9KKRrh1xjE3aC_7jIZ1U0KDW8oJL4G4DzQ75EX7hZP3VXCjHE_8wWZ4Ps_BxxXnicqeSK9PA8hhbH295Ka2BD4Hn2rFUvzf7y7hBlTR7eXzQP28cOsg9VkZuWnH7NAfoTZlPjzv4ZDhjAXgpR80WlThlhCqIxIXl8kXISl34rXPcGhpfU4jS8rvRRmjOLflI5QhCEO2Ce8gMo5uYrP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه پاسداران: سپاه باید آماده عملیات هوشمندانه در خاک دشمن باشد
🔹
هر موقع اقتضا کند و فرمان صادر شود، باید بتوانیم عملیات را به خاک دشمن، به سرزمین‌های دشمن بکشیم و دور از سرزمین خودمان بتوانیم عملیات انجام دهیم.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/680426" target="_blank">📅 23:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680425">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac585917.mp4?token=DIBfvQpPoylk2etr_Avck46CH3SQ_jq7qwuZXjBxB4jLwgkuN-oCLog4bK30SIWvHt2Qx4Z-rxNzRf7aZJWWT6COzFI4T6b_y5A0ChXOlkV3oUSced20IIjUBScUrztlhpoRlbOW3BCKKhmnEF3XSK7gVerAMFopBuXrAaiNeBhRE86tm2-kxGSiepPEyigunUSS5gCtA-ZC9WlTFKuyg7D5HtaE7FWrpY5RYctYuD-2nOmH22LrYZoEcTJylsuTAM-paJYuvbv0bqTTHBPbouxGO0zJkDorsAdUasP53QcFI_BYC21DJTvhoeV1fBITeKHudIlaG4QIwmWswSQpzLhHWmbPTMpjxILQ_T2Xo8queSIgRnehO5AKuONyumQVCskxChiZqBprVg3EHen4O5QN2sWnjUqikufetCWehVYW_rtqM0lsn6KM0Hm3-Zm5B5ZPDMOeXbmK7nBPTBbVMmoDlx5UZzyFe-0TKAKcbjwwvBwzezojQsKGhljkLEHv_gOAKBEayR-CHQJQFtCoJXLbFgthDts1TrWeBHfYSXRxFVG4RVjTLN2VE1UTPIEU-SKdwNJs0ENsFbVfcYJzt9_XRni3pgwbGeYeT1Z-1wu9GxsoRxxhUjPzsEKFZpgEo78I2m1BPJ3R-l0SQeqdilMrpDMiEuk8_fRzugAr-Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac585917.mp4?token=DIBfvQpPoylk2etr_Avck46CH3SQ_jq7qwuZXjBxB4jLwgkuN-oCLog4bK30SIWvHt2Qx4Z-rxNzRf7aZJWWT6COzFI4T6b_y5A0ChXOlkV3oUSced20IIjUBScUrztlhpoRlbOW3BCKKhmnEF3XSK7gVerAMFopBuXrAaiNeBhRE86tm2-kxGSiepPEyigunUSS5gCtA-ZC9WlTFKuyg7D5HtaE7FWrpY5RYctYuD-2nOmH22LrYZoEcTJylsuTAM-paJYuvbv0bqTTHBPbouxGO0zJkDorsAdUasP53QcFI_BYC21DJTvhoeV1fBITeKHudIlaG4QIwmWswSQpzLhHWmbPTMpjxILQ_T2Xo8queSIgRnehO5AKuONyumQVCskxChiZqBprVg3EHen4O5QN2sWnjUqikufetCWehVYW_rtqM0lsn6KM0Hm3-Zm5B5ZPDMOeXbmK7nBPTBbVMmoDlx5UZzyFe-0TKAKcbjwwvBwzezojQsKGhljkLEHv_gOAKBEayR-CHQJQFtCoJXLbFgthDts1TrWeBHfYSXRxFVG4RVjTLN2VE1UTPIEU-SKdwNJs0ENsFbVfcYJzt9_XRni3pgwbGeYeT1Z-1wu9GxsoRxxhUjPzsEKFZpgEo78I2m1BPJ3R-l0SQeqdilMrpDMiEuk8_fRzugAr-Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان فرار مخوف شرور مسلح در عملیات مشترک پلیس
🔹
معاون مبارزه با شرارت پلیس امنیت عمومی فراجا از دستگیری شرور مسلحی خبر داد که پس از شلیک به یک شهروند، با تهیه گواهی فوت جعلی تا مدتی با هویت جعلی در ایران زندگی می‌کرد اما سرانجام در عملیات مشترک پلیس امنیت عمومی و پلیس فتا دستگیر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/680425" target="_blank">📅 23:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/894ec0af40.mp4?token=m4nHRzyYAYpmhOQ9fuUb36lJ5pCMmeTCIyM5wrIw2YMCmvqk6FP5uNIODWJOFrmOUF8gfHxh3PPOB7sKYnA5cnxf6wWUtGn5RVYgmaEwZOpK7m8JU1UGHvHwO85MZb4qsRrI7iULHX47ny7R0gcs0R7fXwCIIozbqVZg5fgf8hvI010mvbaSV8PYIG2AJKQguNathZP2CF4IGCyCBVCaBIbBu7-K_c1I9AnbY1nPZa3-t3_bIN7_x4uHLPojxRQaP1NPdu6ZxVL7cx8ahpzohwlGEcWbjrFfy6HXHFPE542MOKdsVRaNng3fYL3Ax4DLP3XE_Z46GrT0GgibrfYUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/894ec0af40.mp4?token=m4nHRzyYAYpmhOQ9fuUb36lJ5pCMmeTCIyM5wrIw2YMCmvqk6FP5uNIODWJOFrmOUF8gfHxh3PPOB7sKYnA5cnxf6wWUtGn5RVYgmaEwZOpK7m8JU1UGHvHwO85MZb4qsRrI7iULHX47ny7R0gcs0R7fXwCIIozbqVZg5fgf8hvI010mvbaSV8PYIG2AJKQguNathZP2CF4IGCyCBVCaBIbBu7-K_c1I9AnbY1nPZa3-t3_bIN7_x4uHLPojxRQaP1NPdu6ZxVL7cx8ahpzohwlGEcWbjrFfy6HXHFPE542MOKdsVRaNng3fYL3Ax4DLP3XE_Z46GrT0GgibrfYUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه پاسداران: سپاه باید آماده عملیات هوشمندانه در خاک دشمن باشد
🔹
هر موقع اقتضا کند و فرمان صادر شود، باید بتوانیم عملیات را به خاک دشمن، به سرزمین‌های دشمن بکشیم و دور از سرزمین خودمان بتوانیم عملیات انجام دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/680424" target="_blank">📅 23:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
عراق اقدام کلمبیا در به رسمیت شناختن حاکمیت اسرائیل بر بلندی‌های جولان را محکوم کرد
🔹
وزارت امور خارجه عراق تصمیم کلمبیا برای به رسمیت شناختن حاکمیت رژیم اسرائیل بر بلندی‌های جولان اشغالی سوریه را به شدت محکوم کرد و افزود که این تصمیم هیچ اثر قانونی ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/680423" target="_blank">📅 23:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7f7e509f.mp4?token=PU3gkR1_J2KP3zRMXWZvj424Vh89jACp0qCaSwOHRAghWEikf5XW-vSi-x0Md4ppNVW6ayCs79eTvdtjJCtHhKJu7uxyKEUzXGRMTsu1FZ9B6E33-wh9ZyE-ENCZi8I4f53KRIb7DjSCujU70xBumAeRgPAMlxdddXVEWFIy8ePSgtXha2UEhQCzUxJ44N_DjYf92GXMAfJUfPpy5PyGpe2Emp1VzTOk4eCM4BMT1GmimYTZFKpHAT16-lHRUAFihasTPHsKZsvJDaE6veuRU5jgDK_3p7hNS8rBpOQxcfynk3991irjMy2AMZSj0y4DcrbcbGT0IqZceeL2qXH-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7f7e509f.mp4?token=PU3gkR1_J2KP3zRMXWZvj424Vh89jACp0qCaSwOHRAghWEikf5XW-vSi-x0Md4ppNVW6ayCs79eTvdtjJCtHhKJu7uxyKEUzXGRMTsu1FZ9B6E33-wh9ZyE-ENCZi8I4f53KRIb7DjSCujU70xBumAeRgPAMlxdddXVEWFIy8ePSgtXha2UEhQCzUxJ44N_DjYf92GXMAfJUfPpy5PyGpe2Emp1VzTOk4eCM4BMT1GmimYTZFKpHAT16-lHRUAFihasTPHsKZsvJDaE6veuRU5jgDK_3p7hNS8rBpOQxcfynk3991irjMy2AMZSj0y4DcrbcbGT0IqZceeL2qXH-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: تشییع رهبری اگر در نیویورک و لندن هم انجام می‌شد، میلیون ها نفر شرکت می‌کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/680422" target="_blank">📅 23:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680421">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ده ها کشته و زخمی در میان مزدوران سعودی در حملات ارتش یمن
🔹
سرتیپ یحیی سریع سخنگوی نیروهای مسلح یمن از حملات موفق موشکی و پهپادی به مقرهای مزدوران عربستان سعودی خبر داد.
🔹
نیروهای مسلح یمن با تعداد زیادی موشک بالستیک و پهپاد، محل تجمع، انبارهای تسلیحات و مقرهای فرماندهی مزدوران سعودی را در منطقه المخا در هم کوبیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/680421" target="_blank">📅 22:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
روایت نیویورک‌تایمز از راز نخستین آتش‌بس ترامپ با ایران
🔹
روزنامه آمریکایی نیویورک‌تایمز در بخشی از گزارش مفصل امروز خود (سه‌شنبه) درباره نحوه تحول و تکامل تاکتیک‌های نظامی ایران در جریان جنگ رمضان به ارائه جزئیات جدیدی درباره یکی از عوامل موثر بر تصمیم دونالد ترامپ برای اعلام آتش‌بس دو هفته‌ای  با ایران در فروردین‌ماه پرداخته است.
🔹
جزئیات ارائه‌شده در بخشی از این گزارش حاکی است سرنگونی جنگنده اف-۱۵ئی آمریکایی بر اثر شلیک آتش نظامیان ایران در ۱۴ فروردین‌ماه (سوم آوریل) یکی از دلایل تصمیم ترامپ در این زمینه بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/680420" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680418">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/839e31ae75.mp4?token=NOWhgm0Z_wL7N2WiajSzZKamRMcOZILFyrUe3Vs3Gz7xbuksY_Ukh9hyedqQJFEyU-ctRIy6Xa_CHUZOoFqQk7WoJI4yQkEdltr0OZp_vegdZUx1PaRpP8sfZRCCUH9zP55u4vP5nqYqw2qZQSIwxhvfFxBnaTyhG1OGA8O0oShj9efcXVzHGCjAN9iHedu3mdbvL0IEvx_JT7KriDiS4b8O10dKlMvcKtQjOx_0cm7J5jv_ZCb-ZudSupLtOpuoq-rP9Y2m7y-HAfEocL5QAi_qxVINOHZ7DETo3H8oVzBOuZM8eJzSX5EnO_QPKtv3IkImhO8dVQotLuUGrvIK6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/839e31ae75.mp4?token=NOWhgm0Z_wL7N2WiajSzZKamRMcOZILFyrUe3Vs3Gz7xbuksY_Ukh9hyedqQJFEyU-ctRIy6Xa_CHUZOoFqQk7WoJI4yQkEdltr0OZp_vegdZUx1PaRpP8sfZRCCUH9zP55u4vP5nqYqw2qZQSIwxhvfFxBnaTyhG1OGA8O0oShj9efcXVzHGCjAN9iHedu3mdbvL0IEvx_JT7KriDiS4b8O10dKlMvcKtQjOx_0cm7J5jv_ZCb-ZudSupLtOpuoq-rP9Y2m7y-HAfEocL5QAi_qxVINOHZ7DETo3H8oVzBOuZM8eJzSX5EnO_QPKtv3IkImhO8dVQotLuUGrvIK6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردارنقدی: بعد از جنگ، جمهوری اسلامی طرفداران زیادی در دنیا پیدا کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/680418" target="_blank">📅 22:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680417">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
برخی منابع از وقوع ۲ انفجار مجدد در مواضع مزدوران سعودی در مأرب یمن خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/680417" target="_blank">📅 22:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680416">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
۲ مقام آمریکایی: ایران تنها در یک روز آمریکا را به شلیک ۵۰ پاتریوت مجبور کرد
🔹
۲ مقام آمریکایی امروز در گفت‌وگو با نیویورک‌تایمز خبر داده‌اند که تنها در یک روز از ۵ روزه نبرد میان ایران و ایالات‌متحده، آمریکا مجبور به شلیک حدود ۵۰ تیر موشک پاتریوت شد که هر کدام حدود ۴ میلیون دلار قیمت دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/680416" target="_blank">📅 22:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680415">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdcee01ee6.mp4?token=sas4b2Rwv2zFn3oF4TMZ4Qp8lFeZe-5csFwzWCQ4rdjIFuqWAN1Crc5QOCqL8MrZkVpvtM7EB5i56WE44bdJfXpEUeBZx7G4EmgKBkSGSXQ6DGNmp6uTF_BfVvu4jiT912PbOKLnITUAVfYXzyR3BB4TrCrng8Bw19jQwKk8RXVHnntIm5wIZg3cS_56YpI8gi564tZja1grefJ_GkB-MAkCZxhUPGQBvI-MeSSe_ii6q9WHtnZfcAOYRhaEF7WoFDUrE0tEdBeoWwmuGcVmanMLbm8vhRXBMjNTTJA5rkHjNk9iYqHePb7kcTNL8aM39arFgZirTGilXnbtGBDkKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdcee01ee6.mp4?token=sas4b2Rwv2zFn3oF4TMZ4Qp8lFeZe-5csFwzWCQ4rdjIFuqWAN1Crc5QOCqL8MrZkVpvtM7EB5i56WE44bdJfXpEUeBZx7G4EmgKBkSGSXQ6DGNmp6uTF_BfVvu4jiT912PbOKLnITUAVfYXzyR3BB4TrCrng8Bw19jQwKk8RXVHnntIm5wIZg3cS_56YpI8gi564tZja1grefJ_GkB-MAkCZxhUPGQBvI-MeSSe_ii6q9WHtnZfcAOYRhaEF7WoFDUrE0tEdBeoWwmuGcVmanMLbm8vhRXBMjNTTJA5rkHjNk9iYqHePb7kcTNL8aM39arFgZirTGilXnbtGBDkKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: آن‌چه ما را برای جنگیدن متمایز می‌کند و دشمن آن را ندارد، ایمان است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/680415" target="_blank">📅 22:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680413">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFklQHzTPMdfSIq_qYSPhQt76emKEFzBW8gkIzHwOdazk-MoYz2L3KqqjMDbZxF6nJ1r_nLBQ979uNEIcO6tSeSTy36YAGpnNDppTNYUYMPNZwktasui_fE_8E4Ol793RoRVad9IXAphu5JNaqKGEE2rbxjukrvjSG1UUxm3YuTYUWt-CYC-ZRKqhMSK1pXHWkymVoW5XAhPfJRZNjg2BOPTALU4IXM-UGBykJcqb1K1vQqmc9bxL96iZWoKCGMD3-FJLU3vw43Xzd1RL0ccYBgym7ZwEgbyQYXnagzUTqwrGYE1ofwDI6F1pZqGmtRcLC90iqAAYucBT_5gp-ydPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hI4xUoIC5rcaVK-TbW2nBtZ2y4V6Dt225etlvYlgYrckNV1HXdkD48YGtVDQxoNIGDZivrkDNR4SMjZboKMIIejUxoqRkHwREVGRSP1qftr4sqlCSEubv5Nfgu8zukVMjK-JmcVlkPFB14LOyXe4XnQnqXBWU6u6IiCAv4oWj2aixDltoka-31GsjnsCaqsMKpxqTHUajHbvYNEgbIr1R3-NDMJUn31uq9PNdafu3kMwk9hRfI_e08rptoSyPM2Cf8Bi3vauZsjC2b8B7F0ykjbyvtQeLbGiyk6NXPY450zYlAZ53-uGvmRrMi_f-4YVATk2aUKL8g6TkgVH1oOEIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/680413" target="_blank">📅 22:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680412">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbEKAjbRrWHblzm81dc7YAS0R1W1WthYO3gvtuWqSmWqg_O2EhIkxzOHlIO2kCnnVYDiERet9lRM_2r64WULqgqZCbiUIeoK5C3bRBoo7CwScro51KUrrWs2V4x_zNsIOXUSAuM72U2Mc10JO9HHeVkIdqv331UXnvnfR_1JEhmhehM-BXhzE5p75Cl54hbVnt9Mc3zsVRySBN_ixA1kxfvqZP9jM3tLsqHFlipOY8TINLw7HggpCssNOz_g65crFBoajj93eknRdcgpFJrE6W9gLH5EC6Vr2Fti51sdvAcObB2bBCTYW0ieWCWqGBbNBsBBQR3eaymjqIzv_ykdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/680412" target="_blank">📅 22:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680411">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c873ad6ef.mp4?token=FdlJYD1R3Uu3UEW5CVtOn5zRTRJ1r1MiJ3m5bGEXhLk9DNWAgOMq9SqNCEQEJt-7YfkHdo6j9o3QVmW_e1WF5en02myoy34rkPMa1SqrCV8G4avVJSBOS8hcPaoF6LHvgfkIv7uK3845t6pVL3iv1NK9Ja1tmp92pRI1FlB620vcKpttok3INPCrpnJaT3QLmCniMG3shz5Br98EX1XWHVb1LHAUF-ZU68xMR1HIsQrS7GMYTZxi1Y8A7iy-XaV7T4nQmQZ-O5r0KFPX422cSRfUVxCCf8OW90QVa8Pj1vILLOlb_tksGqwCSiLrLoyG21pk7C7So06W94WQ7XP2_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c873ad6ef.mp4?token=FdlJYD1R3Uu3UEW5CVtOn5zRTRJ1r1MiJ3m5bGEXhLk9DNWAgOMq9SqNCEQEJt-7YfkHdo6j9o3QVmW_e1WF5en02myoy34rkPMa1SqrCV8G4avVJSBOS8hcPaoF6LHvgfkIv7uK3845t6pVL3iv1NK9Ja1tmp92pRI1FlB620vcKpttok3INPCrpnJaT3QLmCniMG3shz5Br98EX1XWHVb1LHAUF-ZU68xMR1HIsQrS7GMYTZxi1Y8A7iy-XaV7T4nQmQZ-O5r0KFPX422cSRfUVxCCf8OW90QVa8Pj1vILLOlb_tksGqwCSiLrLoyG21pk7C7So06W94WQ7XP2_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: آن‌چه ما را برای جنگیدن متمایز می‌کند و دشمن آن را ندارد، ایمان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/680411" target="_blank">📅 22:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680410">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
حسین پاک، کارشناس جبهه مقاومت: رژیم صهیونیستی هنوز نتوانسته بر تأسیسات مقاومت در منطقه علی‌الطاهر تسلط پیدا کند/ صهیونیست‌ها با آتشباری و حملات شیمیایی به دنبال کشف ورودی‌های این تأسیسات هستند/ ۷۷ روستا در جنوب لبنان تحت اشغال است و ۵۵ روستا به‌طور کامل از بین رفته‌اند/ صهیونیست‌ها برای کشف ورودی‌های تأسیسات علی‌الطاهر، فناوری‌های جدیدی از جمله سنسورهای حرکتی به کار گرفته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/680410" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680409">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1527d44c1e.mp4?token=RETPPdezjgSRnSKY8TipAt7DQmDhx3_Csz1Y0P65Qmb18WAzMpnLYmqcHcZqPpGnTTRXBpG29-W8u2aQ6TeuJAJ7Otonhi42SuP-pXBsiCyneSagtoAroj0jhRqF9g3_cwNuKnbP1nPAqppxpUgQwqzV7qgcuVPoG4yIroElvNUSOAU-Q8d1HHTmcWlpyD2iEYboxLFFvjvaPhkn4bOIvUzcuove7wpZ9ezryZ-4eYvuRteL1_GqTEjgQh4e18eTnRP7dijMrmJ0UorXKwxADx4k6AsWdsJPHWHx5HvSz2ngL_TpYjKUBbAGF-Cj-BnSgcqNXwjVWa1GFHuPUa_uDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1527d44c1e.mp4?token=RETPPdezjgSRnSKY8TipAt7DQmDhx3_Csz1Y0P65Qmb18WAzMpnLYmqcHcZqPpGnTTRXBpG29-W8u2aQ6TeuJAJ7Otonhi42SuP-pXBsiCyneSagtoAroj0jhRqF9g3_cwNuKnbP1nPAqppxpUgQwqzV7qgcuVPoG4yIroElvNUSOAU-Q8d1HHTmcWlpyD2iEYboxLFFvjvaPhkn4bOIvUzcuove7wpZ9ezryZ-4eYvuRteL1_GqTEjgQh4e18eTnRP7dijMrmJ0UorXKwxADx4k6AsWdsJPHWHx5HvSz2ngL_TpYjKUBbAGF-Cj-BnSgcqNXwjVWa1GFHuPUa_uDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: همه تسلیحات نظامی ما بومی هستند
🔹
ارتشی که الان ما با آن می‌جنگیم صد برابر بودجه سالانه نیروهای مسلح ما بودجه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/680409" target="_blank">📅 22:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680408">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9565fe8c.mp4?token=VKCn7j4cMQyWWu3WGrP8htIup3U3xwHyXPjxuSLacZA7zDB5gZdbIWrOU0D9fP1JtY3tSd5rnuYGRA7n2BfsoPaq7X5I6BncekYbxTGqGfyksBC8ZSqAeT3LkYW0tyOD9rmG-NJtjHiAetqgYBdSI0depxiYxA03-pavjm8C_cZ3JGp-66NSVVVIMPbUA8bLd1OR7Vj-z32fvl9wQlv32hZTPBVZ1CLwFmg7wfobUpA_eJrDPj29dpNcQbDH4wtNGQxnvmBXw78Yi7w2fRqr9k-XzziMtHJj-ZhElnbI1kIR2Lje-vyVTslq6Nz7GDGn4_RqXzliNKARQcZCXh7_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9565fe8c.mp4?token=VKCn7j4cMQyWWu3WGrP8htIup3U3xwHyXPjxuSLacZA7zDB5gZdbIWrOU0D9fP1JtY3tSd5rnuYGRA7n2BfsoPaq7X5I6BncekYbxTGqGfyksBC8ZSqAeT3LkYW0tyOD9rmG-NJtjHiAetqgYBdSI0depxiYxA03-pavjm8C_cZ3JGp-66NSVVVIMPbUA8bLd1OR7Vj-z32fvl9wQlv32hZTPBVZ1CLwFmg7wfobUpA_eJrDPj29dpNcQbDH4wtNGQxnvmBXw78Yi7w2fRqr9k-XzziMtHJj-ZhElnbI1kIR2Lje-vyVTslq6Nz7GDGn4_RqXzliNKARQcZCXh7_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان عقیدتی سیاسی فراجا: در صورت حفظ یک جزء از قرآن کریم، اضافه خدمت سربازان بخشیده می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/680408" target="_blank">📅 22:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680406">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ایران فقط نیم ثانیه به خلبان جنگنده اف ۱۵ سرنگون شده آمریکا، فرصت هشدار داد
نیویورک تایمز:
🔹
در آوریل ۲۰۲۶، ایران یک فروند اف ۱۵ ایی آمریکایی را بر فراز جنوب ایران با یک موشک زمین به هوای دوش‌پرتاب سرنگون کرد.
🔹
به نظر می‌رسد ایران از با استفاده از پهپادها برای ارائه موقعیت مکانی، سرعت و جی پی اس  به فرماندهان ایرانی در هدف قرار دادن آن  جت کمک گرفت.
🔹
خدمه هواپیما قبل از اصابت به هواپیمای ۶۰ میلیون دلاری، تنها حدود نیم ثانیه فرصت هشدار داشتند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/680406" target="_blank">📅 22:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680405">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2wKvtFLLupv-aR8EVHitUPpRWpGiPiuu9JFZdyuNGVkhAgmA10lU7l91v4_YSiv1JxRNKekaqIGugnEAJlTOVVL5XNzBoW-tC1ql6M6XcpZfoMJkvbdf2ua41cc8EMBwM9YTq0KECLbCEVrqNBFolhYuXxZkkw1ESeMm33ReI6mplN327X4CXYB1tzCK6f9CM5Um618gqKaNnycmKe3MRHOn2rpx0jIOLiGB_MRUTWaEYo3RKLfkNujUAVuh1iludOQ-Sr-OHboc6ERPxCQWNtLLJwSFQDhROH5lPvc_sweKIXpQ_OriXSsSQmNmnB-kjcvFYzKMe3UeySY9GSQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از انفجار در منطقه بنی‌حیان در جنوب لبنان منتشر شده که تحت کنترل ارتش اسرائیل (IDF) قرار دارد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/680405" target="_blank">📅 22:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680404">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1944e2df.mp4?token=HMglYr3pTIUGR6iumiBLPGQGTVOHg5bGlDRU5gxBnpBfW_OhJoNehAGGtzosVj2R8Bh89CNNrMlbsvfFKKqOSiUwv4015w4_TFdeVaZsPmj82_YLxdYLl3viR1wQ7OxYm3We8-as9aN5UCkSwVcys5XdZKqCEadrLth2sy-vcBbXqceESqqlHp7m-xtBHlkBgpcab9VJwUOW4iWRSkxHS4k0o8Hx9Z00HMs8kEVd6kgFeAbPjlImIwFfFBTzg3ecqt6iN8oF9yOa0Kb12iYiv6qeUMMd_rQoSdNcrKSA_prWsfjTVGhj65JmgNNXsaW1FV0Tzhbvj9K7NlE_nseNWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1944e2df.mp4?token=HMglYr3pTIUGR6iumiBLPGQGTVOHg5bGlDRU5gxBnpBfW_OhJoNehAGGtzosVj2R8Bh89CNNrMlbsvfFKKqOSiUwv4015w4_TFdeVaZsPmj82_YLxdYLl3viR1wQ7OxYm3We8-as9aN5UCkSwVcys5XdZKqCEadrLth2sy-vcBbXqceESqqlHp7m-xtBHlkBgpcab9VJwUOW4iWRSkxHS4k0o8Hx9Z00HMs8kEVd6kgFeAbPjlImIwFfFBTzg3ecqt6iN8oF9yOa0Kb12iYiv6qeUMMd_rQoSdNcrKSA_prWsfjTVGhj65JmgNNXsaW1FV0Tzhbvj9K7NlE_nseNWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در سالروز رحلت پیامبر(ص) مدینه سیاه‌پوش نمی‌شود
🔹
هم‌زمان با سالروز شهادت پیامبر اکرم(ص)، مسجدالنبی مملو از زائرانی از سراسر جهان است؛ اما در مدینه خبری از مراسم عمومی سوگواری، نوحه‌خوانی و سیاه‌پوش‌شدن اماکن نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/680404" target="_blank">📅 22:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680403">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
زلنسکی: برای خاتمه جنگ با روسیه طرحی ارائه کرده‌ایم
رئیس‌جمهور اوکراین:
🔹
پیشنهادهایی را برای طرحی با هدف پایان دادن به جنگ با روسیه به مذاکره کنندگان آمریکایی ارائه داده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/680403" target="_blank">📅 22:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680402">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jklkQvmSAzAJ4JRY32MPL1ZojZr1T6E-yi-3ruD21nr5IDlOM87QL6pkN8GRbeYc19jwet4or9T9AaX73JnhWI68jVMGl5ykvPs_y5bRRzsHCCl0lZpzKYgkJjTCR4JoaT1uNXsmM2Ff91dLXemUw50Pd6cGUEbuscQZt6qqakeYBgFfBSZR88dU9pzdful3Bj8NUi2qJFdyK7BZmPpLsHXjILl_kNXmSknzuvniFpJGBFHr8MFtsmQGplU-0riO88R4JZrc08UwIaKPMKzoHq5zqubOgefTuJl0qmrfP4mlsimZIVnwUUtab7GE_CgdTP_lNl4X4LOMRRHFukSrUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبر فقط تحمل سختی نیست؛ گاهی یعنی ایستادگی در برابر چیزی که دوستش داری
🔹
امام علی(ع) در حکمت ۵۵ نهج‌البلاغه، صبر را دو گونه معرفی می‌کند: صبر بر آنچه انسان از آن ناخشنود است و صبر در برابر چیزی که به آن میل دارد. گاهی دشوارترین صبر، نه تحمل رنج، بلکه کنترل…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/680402" target="_blank">📅 22:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
شرط سنگین رامین برای پیوستن به فولاد
🔹
طی ساعات اخیر شایعاتی درباره پیوستن رامین رضاییان به فولاد خوزستان مطرح شده اما پیگیری‌ها نشان می‌دهد که این بازیکن هنوز قراردادی با باشگاه خوزستانی به امضا نرسانده است.
🔹
رضاییان در مذاکراتی که با مسئولان باشگاه فولاد خوزستان داشته، خواستار قراردادی به ارزش ۲۰۰ میلیارد تومان شده. رقمی که مورد موافقت باشگاه فولاد قرار نگرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/680401" target="_blank">📅 22:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680400">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/badcdc31e6.mp4?token=G-stGWTJlHvxCRU7gvqFj6NHBWSwPZdcx7eMGleI1ptQNcqKLRGTNVZLndy4JreWIux2g_s_teDleJl8G4HcWrC76lC2veex63hIBIh5s-8sB5sv0TtbFmrUrhfJggQcXdw7F1hRm5zYikP1iFD8LVL5lmCM6TtvWXfgweCPUacazh2OL6uwpiBPDNs4AaeD-p9W7H6sXzefQTOUYa_1lPDJV4ez_r0u0Idnfz1laomKKW1GZCwHYOMYPtMelM6dMPHacm_WdzyBdGSf0LU-nbDLN7muZ3FOT1LYU2qoglCM_cEBVCHQnSgKA_tq0R-HgBz6KG7HcWb3cg4R3nUazA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/badcdc31e6.mp4?token=G-stGWTJlHvxCRU7gvqFj6NHBWSwPZdcx7eMGleI1ptQNcqKLRGTNVZLndy4JreWIux2g_s_teDleJl8G4HcWrC76lC2veex63hIBIh5s-8sB5sv0TtbFmrUrhfJggQcXdw7F1hRm5zYikP1iFD8LVL5lmCM6TtvWXfgweCPUacazh2OL6uwpiBPDNs4AaeD-p9W7H6sXzefQTOUYa_1lPDJV4ez_r0u0Idnfz1laomKKW1GZCwHYOMYPtMelM6dMPHacm_WdzyBdGSf0LU-nbDLN7muZ3FOT1LYU2qoglCM_cEBVCHQnSgKA_tq0R-HgBz6KG7HcWb3cg4R3nUazA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان و سیل شدید در استان ژجیانگ در شرق چین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/680400" target="_blank">📅 21:56 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
