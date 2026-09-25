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
<img src="https://cdn4.telesco.pe/file/hM5rYHFbH5Hy4hoUtW3tGtxrkQXvpGcloEQyEORrzs8SMzWNtlFBmw0ZKDMLTtANMuU5zcDl1LL-oim7L-ubYZUZOUQiv4SphL5SnHtm7OKX4mPrrJGBzL7Sy8rvDnFAfb3mxEXu-F5UEKzYt-aXPjudGCm5-6c4e7hZaPjQ9ct5MdFmDdYmsJD2YI29SD_kYmolJYBHRy6UTmozBh1nmcSARWxX1y9MM7YdMZ9vRohAj1Fkqrekj4MK5QXsZX2ZuIwm8zl0iTFzQK222ntOSbuIpLSM-Q9sHUyYPuLcq4zZf-nncacEorAjhe3RsT8220VuA6UlITMaTy0z1ApRWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 20:53:33</div>
<hr>

<div class="tg-post" id="msg-692968">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3ozC39XhtLzhKpLZ_0D_OsEVp5QsaTtTk_G84rrUVlcX8u75G05GQNPN3vP1hqdIe0sHYwWFH-g4w9KnGYKZYWtfOqwDPGN-1qGrT08Vk0iK3rqakf-tN-3pMAXOmoPJOwfZgiAIkWmo8tvIT7dK9Ym_PRteSUrlsGhPprmKZ1uw9z24zDZExkGOYSqbUOPl82qH0FWYKQznfrkGPtxGmgQZl3R6HyCOx1rs-45Z5gNTa6vg5RBm2ysGTW80D-9VKDduE2gz5oPS4ltvGKH46DgBFaI0vEfAScelRU8IbjDCEDgSebzkz423QJT4XkaXroK5pgIFHBdrUaFzmmvwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فروش کیف‌های اضطراری در آلمان از ترس حمله روسیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/692968" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692967">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17c8f0887.mp4?token=AS8D7hmfLnz71v1aePm4-ZMqTfZHn9XuopQrQgCoIScRplp-y_GslRzrYc4-CQGS20fBw61-VtEKEXbkLruO_2OQ2wZaIOgaeAG87nmzTXGvH1lVgNRop-lC3-nHPwcNEmC26J9AL3RCsP1Ys86pwfIWIUn2lmGnwoqTx3uyep92auRbO7c2Y9f6Fn0XQGQoESDAm7JvLDszjecvRFNipn-_iMkQmzcXIYi9rqhWKWWYdMOS5cweY18lkKEedx2otxnjkRqmhMQt-a0seP24cogu04Lt9i1vJEbNXh559F44BI9EYau8yr6HPOJUoB3SELvcdRgD2hxIc6SSHPgLL2LCvAPD9ssqzdC5Z5KCEMHiCJ6SJ_ZIgB8VdBDKjomgpjQK8Wu_kAW3m9nS_kCB3B9qaxz2gs3W6yYE5zVxhvGFOPCSnpbaY267_jJqVeAPMrdQpYIOqeEx5nGWxaGYlV8KthH9i49PPwkV_qvJ_3vdMR_DdFxq6duf8UCM68bjCfbFCxivJOURDFrq6UdVpkZTob4XU_cMXS0XfMID0gt7u_iPM0U5HBC7t9QvFU5p5iSJbM4bpNcQiGhE9dgkVnqYDrXRjH7GttTqG7IAv5AptFkKvWyLwz1t523P7uUTgS1YvNvEdJTRPOOxFPVbVrvyIv6EmAC10ECjdkxDe_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17c8f0887.mp4?token=AS8D7hmfLnz71v1aePm4-ZMqTfZHn9XuopQrQgCoIScRplp-y_GslRzrYc4-CQGS20fBw61-VtEKEXbkLruO_2OQ2wZaIOgaeAG87nmzTXGvH1lVgNRop-lC3-nHPwcNEmC26J9AL3RCsP1Ys86pwfIWIUn2lmGnwoqTx3uyep92auRbO7c2Y9f6Fn0XQGQoESDAm7JvLDszjecvRFNipn-_iMkQmzcXIYi9rqhWKWWYdMOS5cweY18lkKEedx2otxnjkRqmhMQt-a0seP24cogu04Lt9i1vJEbNXh559F44BI9EYau8yr6HPOJUoB3SELvcdRgD2hxIc6SSHPgLL2LCvAPD9ssqzdC5Z5KCEMHiCJ6SJ_ZIgB8VdBDKjomgpjQK8Wu_kAW3m9nS_kCB3B9qaxz2gs3W6yYE5zVxhvGFOPCSnpbaY267_jJqVeAPMrdQpYIOqeEx5nGWxaGYlV8KthH9i49PPwkV_qvJ_3vdMR_DdFxq6duf8UCM68bjCfbFCxivJOURDFrq6UdVpkZTob4XU_cMXS0XfMID0gt7u_iPM0U5HBC7t9QvFU5p5iSJbM4bpNcQiGhE9dgkVnqYDrXRjH7GttTqG7IAv5AptFkKvWyLwz1t523P7uUTgS1YvNvEdJTRPOOxFPVbVrvyIv6EmAC10ECjdkxDe_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ایران قربانی اقدامات غیرقانونی و تجاوزکارانه آمریکا و رژیم صهیونیستی شده است / هیچ‌یک از اهداف شوم متجاوزان محقق نشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/692967" target="_blank">📅 20:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692966">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
مقام ارشد ایرانی به رویترز: ایران در ازای بازگشایی تنگه هرمز هیچ امتیاز هسته‌ای نمی‌دهد
🔹
تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته باقی خواهد ماند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/692966" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692965">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
اردوغان، رئیس جمهور ترکیه: توافق دفاعی مکه ائتلافی علیه ایران و اسرائیل یا طرف ثالث نیست و هدف آن تقویت امنیت و ثبات منطقه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/692965" target="_blank">📅 20:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692964">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بهترین روش یادگیری، روش حاجی‌بازاریه!
🔹
بهترین شیوه یادگیری، مدل عملیه؛ یعنی از آدم‌های موفق الگو بگیری، دقیقاً مثل کاری که حاجی‌بازاری‌ها می‌کنن. دور هم می‌شینن و از کارهایی که کردن می‌گن و این‌جوری توی اکوسیستم خودشون شروع می‌کنن به یاد گرفتن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/akhbarefori/692964" target="_blank">📅 20:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692963">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4470da11.mp4?token=lJOmx_KDq8PAcv_uhyPNK1dhz4VWWDF2YIOGsMdREG8GVO8lkXgrKNv-BPQ9eQo5KDaGnP_yNEO4aSSErKQVVGXN3wJ8pToEJp0UGh88gA_xYipFbGwsfS33YRM8J63De_5f7Yx2X-GAhnyqMhoW1UXyFQVbcLYWRhSKKFuJEBNeUTmamGeP18yWIRXLpVofui57M4R-jqbk9Gx-abRwL6M9niIkocLJ-HTCkUnVpjSLoZGNhvxgRNm1WkM5mfdw93d8xH3VsUcGvpqyQmi7vgE19NcbGrYcQdqBNDDFSh1Hru-K2HrzYfqKzK0G2bKawSbCJoCV4KViqenBgfPBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4470da11.mp4?token=lJOmx_KDq8PAcv_uhyPNK1dhz4VWWDF2YIOGsMdREG8GVO8lkXgrKNv-BPQ9eQo5KDaGnP_yNEO4aSSErKQVVGXN3wJ8pToEJp0UGh88gA_xYipFbGwsfS33YRM8J63De_5f7Yx2X-GAhnyqMhoW1UXyFQVbcLYWRhSKKFuJEBNeUTmamGeP18yWIRXLpVofui57M4R-jqbk9Gx-abRwL6M9niIkocLJ-HTCkUnVpjSLoZGNhvxgRNm1WkM5mfdw93d8xH3VsUcGvpqyQmi7vgE19NcbGrYcQdqBNDDFSh1Hru-K2HrzYfqKzK0G2bKawSbCJoCV4KViqenBgfPBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مِتا مرز تماس تصویری را شکست: طرف مقابل، سه‌بعدی و زنده وسط خانه‌ات ظاهر می‌شود!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/692963" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692962">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff824d345c.mp4?token=IH9bNYahMmMgTuHrw45Rruoi1nckajjHd3z-byASZ4j3RM_-4VhV7jhKPnrlz3-GS4aFNIitC1nrFcRvTbzB-5hNxa5_JnRHdzmnxRDXMyNO6RLp1WxUmruoNthy-YQsFPqe8kLA5VAUiQa7u1DJp-YXd3b2bXJu-MplKTd-NbhedjEcJbAcA1OXhFYwXHYo_ah-IhebeWNWVDmxhVihbd7YlXjVzl75w8wa40jMtnxUPszwufUvDyzuq70puQOJ6lv5fWcicmIY9aL6eVxqHc6q5vCGKli7NripbpxzCwmf6C7PaXWMU2OoCjXUQEWb-stIoV7CyMhHtYJTSyFhuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff824d345c.mp4?token=IH9bNYahMmMgTuHrw45Rruoi1nckajjHd3z-byASZ4j3RM_-4VhV7jhKPnrlz3-GS4aFNIitC1nrFcRvTbzB-5hNxa5_JnRHdzmnxRDXMyNO6RLp1WxUmruoNthy-YQsFPqe8kLA5VAUiQa7u1DJp-YXd3b2bXJu-MplKTd-NbhedjEcJbAcA1OXhFYwXHYo_ah-IhebeWNWVDmxhVihbd7YlXjVzl75w8wa40jMtnxUPszwufUvDyzuq70puQOJ6lv5fWcicmIY9aL6eVxqHc6q5vCGKli7NripbpxzCwmf6C7PaXWMU2OoCjXUQEWb-stIoV7CyMhHtYJTSyFhuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرخ زندگی
🔹
از ایده تا اجرا؛ تجربه‌های واقعی فعالان و صاحبان کسب‌وکارهای خانگی .
🔸
داستان گام‌های اولیه و رمز موفقیت کسب‌وکارتان را با دیگران به اشتراک بگذارید. صدای خود را در یک پیام صوتی ۳۰ ثانیه‌ای همراه با عکس‌هایی از کار یا خدماتتان برای ما بفرستید تا با مخاطبان به اشتراک بگذاریم.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/692962" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692960">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
الجزیره: پس از دیدار ویتکاف و کوشنر، کارشناسان فنی به مذاکرات نیویورک پیوستند
🔹
آمریکا ابتدا به هیئت ایرانی روادید نداده بود، اما روادیدها به‌سرعت صادر شد و هیئت ایرانی به مذاکرات ملحق شد
🔹
طرح ایران برای بازگشایی تنگه هرمز طی هفت روز، در صورت لغو محاصره…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/692960" target="_blank">📅 20:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692959">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
الجزیره مدعی شد: مذاکرات ایران و آمریکا در نیویورک از تماس‌های اولیه دیپلماتیک فراتر رفته و وارد مرحله‌ای جزئی‌تر و فنی‌تر شده است؛ منابعی در تهران فضای مذاکرات را به‌طور فزاینده‌ای مثبت توصیف کرده‌اند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/692959" target="_blank">📅 20:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692958">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای اکسیوس رسانه حامی رژیم‌صهیونیستی: آمریکا به ایران اطلاع داده که ایران تنگهٔ هرمز را کنترل نمی‌کند، بنابراین نمی‌تواند در مورد آن شرط و شروطی اعمال کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/692958" target="_blank">📅 20:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692957">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh_rqjn2NsUCDWBjbgXoYY2DZqsdhdjLy476zqK8dFjw080hXB6PtBKNKPOl4KreGwe-sSc5xmyLBg8PglPNQ-KqgowA6Rel5D_QI9-0EwcRGBQYsar6nSC5Ew8FV8JTykE_3QsPOFYJ_A8g6lzrA-5NQ9meZ5Z2M_oZwtoYZYzqkvZtUskB4uCgUnOkyfOv48WPGGh62JASN2XHVTGxN7l1Dh5vKKBK_Rk9qBrb356tqy1RuX0EUQQjifUL8KyKX2UG0r6YaALwjNwM6uJIM3TAJOj8AI-kW0koqYOZAdaBl4DrO2EDvIeKKJMkUtGTg4qQWEnmuj78XZd97XsqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط نفت برنت به ۱۰۳ دلار با خبر مذاکرات فنی ایران و آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/692957" target="_blank">📅 20:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692956">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
فایننشال‌تایمز: انسداد هرمز تجارت خلیج فارس را بحرانی کرد؛ هزینه حمل تا ۸ برابر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/692956" target="_blank">📅 20:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692955">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXLmr6q0x8tkp_T7IyPhrIGcQE1BfQiyHICLBbOJ-Qa53mIT2aAya53FLmxL0BhAEB0WJjQn4_YUwnSiBUTSO2F2JlMjIa1C4MUwXAK9GBGiTDT2n1NRg5ZVVVnhim3QPyJ2hcrRGB0fPWDVaj8URu_nr_4jdeXjZiNFAMlTUs6aHklam2_VFcSbZG_AixOr1ISUEHwMOHnpreNHOk-X1J7nyoljIYt1hCTuK_0VJMn6EfNQGUTKisMzAwkKyA5DEJkLyFV3JvnwU0n272KYxPn6ZpZNlm5ppFFKa_z_DO7HBQA3l0R0lzD4gZDOpo41bqiaRPzrVe7OAr9Nl5bLlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتفع‌ترین قله در هر قاره
🔹
بر اساس داده‌های دانشنامه بریتانیکا، قله اورست (آسیا) با ارتفاع ۸ هزار و ۸۵۰ متر از سطح دریا، بلندترین قله جهان است.
🔹
پس از آن، قله آکونکاگوا در آمریکای جنوبی با حدود ۷ هزار متر و قله دنالی/مک‌کینلی در آمریکای شمالی با ۶ هزار و ۱۹۰ متر  در رتبه‌های بعدی قرار دارند.
🔹
البته اگر ارتفاع کوه‌ها به‌جای سطح دریا از «پایه تا قله» محاسبه شود، دنالی (مک‌کینلی) بلندترین کوه جهان خواهد بود.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/692955" target="_blank">📅 20:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692954">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">18-2 Ane Manaee (1404-02-03)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/692954" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هجدهم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
خلقت انسان با همه ابتلائات، بخشی از رحمت رحمانیه خدا و پلی‌ست برای رسیدن به رحمت رحیمیه الهی [00:00]
🔹
در عالم حق، مسخره‌کنندگان در تسخیر حقیقتی درمی‌آیند که روزی آن را به استهزاء می‌گرفتند [05:18]
🔹
عرضه فریبنده دنیا، تجلی رحمانیت الهی و محکی ست برای برون داد حقایق باطنی انسان و نیل به رحمت رحیمیه [09:44]
🔹
رحمت رحمانیه نه الزاما نشانه حقانیت ما، که گاهی بخشی از سنجش الهی و محک ایمان ماست! [12:59]
🔹
"امتحان در میدان جهاد"، "فریبندگی باطل"، "رفتار منافقانه برخی خواص" و "ابهامها و وارونگی‌ها در عصر فتنه"، مصادیقی‌ست از رحمت رحمانیه برای محک ایمان در انسان [19:55]
🔹
آیه ۳۱ سوره محمد صلی‌الله‌علیه‌و‌آله، بازخوانی درونی از امتحان الهیست، چلاندن بنده برای اثبات صداقت او در مسیر حق! [26:52]
🔹
حالات روحی امام حسین علیه‌السلام در کربلا، مصداق استخراج خبر از دل بندهِ‌ایست که به «نفس مطمئنه» رسیده [34:24]
🔹
تحلیلی از رابطه ایمان، انفاق و جایگزینی اقوام و ملل در آیات آخر سوره مبارکه محمد(ص) [42:45]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/692954" target="_blank">📅 20:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692951">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
مشاور و مدیرکل حوزه معاون اجرایی رئیس‌جمهور: قائم‌پناه، معاون اجرایی رئیس‌جمهور، به‌عنوان نماینده حاکمیت و طبق ابلاغ مراجع رسمی و ذی‌صلاح در مراسم روز ملی عربستان سعودی در تهران حضور یافته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/692951" target="_blank">📅 20:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLLG-fDf2YuJtmb-cAQEikYScqGbQkc4WSubZt8K13KopUhTgq9UyF7O-Rxmw4d1aJFbPIVFieSsjhJyEn3lmvE04H3zFr8lV0CrVww0F5_PG5tIPYlQqZohSHmE89Bo73cz1Rnj9ZRGxiABQCzugjergaXMb-uPMoU9kP8Ye8jw-3HZg8UfEtrSJa0iaup2josc0IoDPoR1CjWHyput-Sj79g_a_wYo3kROd6RTZ-nKdGxCDcxaqj3Rptsr-2lLGmSxEt70SdSRKp87fJO-WolQKpf7C2-bHnChwQF12cvuYN_uKvfvrW7aHCL5uJTJysPbjgK_BSEstktkU5M8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از عقب‌نشینی ناوهای آمریکایی به سمت اعماق دریای عرب از ترس هدف قرار گرفتن توسط ایران حکایت دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/692950" target="_blank">📅 19:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای اکسیوس رسانه حامی رژیم‌صهیونیستی: آمریکا به ایران اطلاع داده که ایران تنگهٔ هرمز را کنترل نمی‌کند، بنابراین نمی‌تواند در مورد آن شرط و شروطی اعمال کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/692949" target="_blank">📅 19:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e493231e18.mp4?token=RXVXMQtPWvshEg7uHt7k1cHIFPQfKVKOgUYKQ6IUOfmQELcE3MeW6eTwnbY4-QLEymOtdc6VHDDRCV8E4KMM7gqZQfgExADQ52UPFdvLuGO2wQ7VvYslAXoNpHEoadxhRA5iMXQfRTAu7nzO3OFDZPbxpmYQE5yNw0p3ceXC4Q__aUWpiuHHXCulb4e5c2Ip1Jd1XCyAHFF5-69FQq38OhUhqAeTnIc8ijL_stHjK5tK4qVCN2FB6ips47mXTZ0t9JXupgFA3TpHYX6H9niTcbwLAM6sX0TMtogz6TMjBkvUzsNuRypd2nJZTf3tuwpE_ftXclibJ80hNA8Wh7vSYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e493231e18.mp4?token=RXVXMQtPWvshEg7uHt7k1cHIFPQfKVKOgUYKQ6IUOfmQELcE3MeW6eTwnbY4-QLEymOtdc6VHDDRCV8E4KMM7gqZQfgExADQ52UPFdvLuGO2wQ7VvYslAXoNpHEoadxhRA5iMXQfRTAu7nzO3OFDZPbxpmYQE5yNw0p3ceXC4Q__aUWpiuHHXCulb4e5c2Ip1Jd1XCyAHFF5-69FQq38OhUhqAeTnIc8ijL_stHjK5tK4qVCN2FB6ips47mXTZ0t9JXupgFA3TpHYX6H9niTcbwLAM6sX0TMtogz6TMjBkvUzsNuRypd2nJZTf3tuwpE_ftXclibJ80hNA8Wh7vSYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: با رئیس جمهور چین درباره ایران گفتگو کردم
🔹
قصد دارم برای شرکت در اجلاس اپک در ماه نوامبر به چین سفر کنم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/692948" target="_blank">📅 19:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692947">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ترامپ: با رئیس جمهور چین درباره ایران گفتگو کردم
🔹
قصد دارم برای شرکت در اجلاس اپک در ماه نوامبر به چین سفر کنم.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/692947" target="_blank">📅 19:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cdb1e902.mp4?token=qYlHY4PPdUoqJ6_QjTjfKFpXnWD7D_KVJ3W08TuiFsqXjTwbKk6aI4MrCldfWZvPmzOb2B6tU1-q8RP5tZrMELt3xN_rcF9NIi1b1FpPcEyRtML2EBgSq4LD9Zs35Ey97NjQqe756hbyOCpJrabhQgdYE4lG7H3Ilcxduq5qgIs50cMctTGFglAqMABTYFP7Z0QpH5jl_xIlOOlc-F3cTqfSaZ-_8ZioSOjbVuzjOYQXFrkV975TyO1Jp3A9Ah0kMzqTluTPOixbF4CTbkwC-JTj4A_Ei4gwez3bIQtRhaSKgR5hItY8apz8yBp0ulOSy1ryYDAKRoyziAuzj6Ad3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cdb1e902.mp4?token=qYlHY4PPdUoqJ6_QjTjfKFpXnWD7D_KVJ3W08TuiFsqXjTwbKk6aI4MrCldfWZvPmzOb2B6tU1-q8RP5tZrMELt3xN_rcF9NIi1b1FpPcEyRtML2EBgSq4LD9Zs35Ey97NjQqe756hbyOCpJrabhQgdYE4lG7H3Ilcxduq5qgIs50cMctTGFglAqMABTYFP7Z0QpH5jl_xIlOOlc-F3cTqfSaZ-_8ZioSOjbVuzjOYQXFrkV975TyO1Jp3A9Ah0kMzqTluTPOixbF4CTbkwC-JTj4A_Ei4gwez3bIQtRhaSKgR5hItY8apz8yBp0ulOSy1ryYDAKRoyziAuzj6Ad3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عروسی عجیب با تم مرد عنکبوتی
🔹
تصاویری از یک مراسم عروسی در ایران منتشر شده که داماد با لباس مرد عنکبوتی در ارتفاع حدود ۱۲۰ متری ظاهر شده و عروس نیز با گریم این شخصیت در مراسم حضور داشته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/692946" target="_blank">📅 19:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692944">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
دیدار علی الزیدی،نخست‌وزیر عراق و ترامپ
🔹
دولت عراق پس‌از این دیدار اقدام به افزایش محدودیت‌های هوایی علیه ایران کرد!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/692944" target="_blank">📅 19:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692943">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9939e8cd05.mp4?token=CS6g5_z7i-QqvSr2a452Rnt6E-YtHURJaSRJPlI0Pw4CDRNeTIzh1R4Hn5MlONJy4GZcxkVBcycyhP-k7gVSnpfVdAuB0ipXHlGzr3v8S8VMUsNpqej0z9QHkuKYNDr1WbAzFGHVmnePpOERDYovu5eex-0pyuakQg2LcKtkd3gQL0KxIeNvThqA3i_PqR2TCGiPSA-aNvEbNVdRlS1b3si6MSRRCqqViY6lWMIvOcLjX2-fDlyEUP4KZWElzuslBFhow6AAbvjH6TRlF9gWAavGZO8L43DSQAbTp82hjJKP78Zjhk6C4vUH1qtTQ-zwlIWBo9CHUaS18xuzTDyha0HmuGjkovWzSMP250ivQbNGq5CPugpFwzzsFOvXP-dZKM5vI2z7CKvDgWEvqcdd79Ja6wVxme8nAGSgyhz-nCTIRY0ZDPzHrnsBeZq4d4vahDr9ckDHkAKh3MTVk4mOI_LN3vTE0q2jkGAJNb4V9vDfZ3JgcSy4Kjy3YnPHEGT5IJiyJRpwLlGj_r16ArPtqIyiyb9REXdC6zQy2Pmzah8PXYKMXcpnNw6s5UgNfXrCmFGjtB31pa_lQ9mBwrO8S5gK9miCdDwboQ0XMsqdUVggTIzuqHA3rP-lwSHGyO3--Eeq6yp4oBk1qfg-Q_otq9iLyJ6xoAKbCeZq6d2_CB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9939e8cd05.mp4?token=CS6g5_z7i-QqvSr2a452Rnt6E-YtHURJaSRJPlI0Pw4CDRNeTIzh1R4Hn5MlONJy4GZcxkVBcycyhP-k7gVSnpfVdAuB0ipXHlGzr3v8S8VMUsNpqej0z9QHkuKYNDr1WbAzFGHVmnePpOERDYovu5eex-0pyuakQg2LcKtkd3gQL0KxIeNvThqA3i_PqR2TCGiPSA-aNvEbNVdRlS1b3si6MSRRCqqViY6lWMIvOcLjX2-fDlyEUP4KZWElzuslBFhow6AAbvjH6TRlF9gWAavGZO8L43DSQAbTp82hjJKP78Zjhk6C4vUH1qtTQ-zwlIWBo9CHUaS18xuzTDyha0HmuGjkovWzSMP250ivQbNGq5CPugpFwzzsFOvXP-dZKM5vI2z7CKvDgWEvqcdd79Ja6wVxme8nAGSgyhz-nCTIRY0ZDPzHrnsBeZq4d4vahDr9ckDHkAKh3MTVk4mOI_LN3vTE0q2jkGAJNb4V9vDfZ3JgcSy4Kjy3YnPHEGT5IJiyJRpwLlGj_r16ArPtqIyiyb9REXdC6zQy2Pmzah8PXYKMXcpnNw6s5UgNfXrCmFGjtB31pa_lQ9mBwrO8S5gK9miCdDwboQ0XMsqdUVggTIzuqHA3rP-lwSHGyO3--Eeq6yp4oBk1qfg-Q_otq9iLyJ6xoAKbCeZq6d2_CB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید از «آکبند کردن» آیفون‌های دست‌دوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/692943" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692942">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای عجیب مدیر دفتر خاتمی، محمدعلی ابطحی: در سال ۸۸ در زندان گفتند اعتراف کن که خاتمی به اسرائیل سفر کرده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/692942" target="_blank">📅 19:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692941">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
نیشن: حمله به مدرسه میناب مخالفت با جنگ را افزایش داد
🔹
پس از جنگ با ایران و به‌ویژه حمله به مدرسه‌ای در میناب، تماس نیروهای آمریکایی با سازمان‌های حامی حقوق نظامیان و درخواست برای خروج زودهنگام از خدمت افزایش یافته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/692941" target="_blank">📅 19:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692940">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
پزشکیان: حاضر بودیم اورانیوم ۶۰ درصد را رقیق کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/692940" target="_blank">📅 19:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692938">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b0fbb38e3.mp4?token=QXPAFXn0DXvcFGmdqPEfvZLMQWcHSapQnG0gfmRNJFNFXyNpk80m7o_F-7MSYIiAMH2Q9x3_thJAR-X-GKTMkBH7ESealyXfzJ66xTymYKP3av_mm49Az0qFSYJmIKcrdDOOXrEWD-Z_E_0k4uBlwWJ8IhCHWRRvKbJQtGDKWxnJA4EPhP2kFct39LRPklb4QcOrfusRJDkkfiWUbkX-WpAQFUv0VVNpbO8crZGj-VV59qwwYYgcxt4QpAevLaXvARcE3pfNl8HqNZgW7jWNcf8uXEgfyWB_386_DnGT5S6kPXdFEMoSpkwzDEyEbmyoGcUcmNsps-lM5LrAvdwnyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b0fbb38e3.mp4?token=QXPAFXn0DXvcFGmdqPEfvZLMQWcHSapQnG0gfmRNJFNFXyNpk80m7o_F-7MSYIiAMH2Q9x3_thJAR-X-GKTMkBH7ESealyXfzJ66xTymYKP3av_mm49Az0qFSYJmIKcrdDOOXrEWD-Z_E_0k4uBlwWJ8IhCHWRRvKbJQtGDKWxnJA4EPhP2kFct39LRPklb4QcOrfusRJDkkfiWUbkX-WpAQFUv0VVNpbO8crZGj-VV59qwwYYgcxt4QpAevLaXvARcE3pfNl8HqNZgW7jWNcf8uXEgfyWB_386_DnGT5S6kPXdFEMoSpkwzDEyEbmyoGcUcmNsps-lM5LrAvdwnyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادی که هم پرواز می‌کند و هم شنا!
🔹
دانشمندان چینی پهپاد TJ-FlyingFish را ساخته‌اند که می‌تواند در هوا پرواز کرده و تا عمق حدود ۳ متر زیر آب حرکت کند.
🔹
این پهپاد ۱.۶ کیلوگرمی می‌تواند حدود ۴۰ دقیقه زیر آب بماند و برای جست‌وجو و نجات و تحقیقات دریایی کاربرد داشته باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/692938" target="_blank">📅 18:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692937">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhwzV1b0ktLNAWiI51zi8-gjL_9H1cx6_in7-P1s1BXddp2-L1UM_TmVYRiwY3dnbYa_Mkzw3jf8tR82-VaCLDGeEw-DBzkLbLoJFlrBQHs-6rzFHhAZfSCLq7SFho9Pwbs1w2mFfT64Bup_VTK9VzsgFLeLUt-RUaPQ9sPjptuEuAwG2ktCXUf7hoECTg4-ad0ceJ2XSINpZGr9ZXI6WMzn9ZlZxygTjd9LSzkhLk6xW7JM21kuJvYUqOLKY8lhpOHAcqenkJS-RjTR8rSvbZT-MFuu7L1H7IEXKJ8Y-E_44GwmYrv7PrGoOBkqQhDBFtebh3i2rXcOWFVdrUyQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بحران پلتفرم‌های طلا در تحویل طلا یا پول آن؛ جایگزین مطمئن چیست؟
جمعی از خریداران طلا در پلتفرم‌های آنلاین، با چالش جدی در تحویل فیزیکی و حتی تسویه ریالی مواجه شده‌اند.
ریشه این بحران روشن است: نبود نهاد ناظر، خالی‌فروشی، شفاف نبودن و سازوکار نقدشوندگی.
🔹
اما جایگزین مطمئن چیست؟
🔹
صندوق‌های ETF طلا که ۱۰ سال در بورس فعال هستند و طلای آن‌ها در خزانه‌های رسمی نگهداری می‌شود که حتی یک مورد شکایت نیز تا امروز نداشتند.
به عنوان نمونه، طبق آخرین گزارش سامانه کدال،
صندوق طلای «رز ترنج» بیش از ۴۱۱ کیلوگرم شمش و ۸۲۰۰ قطعه سکه در خزانه‌های رسمی دارد.
در حالی که پلتفرم‌ها در تسویه مبلغ ۱۰۰ میلیون هم ناتوان‌اند،
صندوق طلای «رز ترنج» در شهریور ۱۴ همت گردش معاملات داشته که بیانگر عمق بازار و نقدشوندگی آن است.
اعتبار این صندوق به اندازه‌ای است که امکان دریافت گواهی تمکن مالی و وثیقه‌گذاری برای دریافت وام در شبکه بانکی کشور را دارد.
📌
آموزش خرید صندوق طلا را اینجا ببینید
.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/692937" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692935">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fcdf5128.mp4?token=gTIoPZekdH-2z_TeEI4cvdWTJ6g2UkgnAHE_foyNdLWnPpY57ye4RjYRwFsKKRBVKIHp-zIdIvAijxykeJP4BgvsKes2qNSzsRFbeTvhhXPeRthqRbeR80Zaa1HJfieJNyUtXGeBQbF1W5-ypcVP4dJz3KNdAYrTGiC1Lo_JQAm2_VKofrzf60f1rjmVbVrzzVYrGOhGHs9Wlgmi4Cj8lPt69a5dPHiZZ8pCF1qgxqLfmkkn_dkcrmQZvOK2MXoPW_TXkvZzBtO_v3KX74G1HCCuv1UkD7xyy7fZfkVIX9XBr-VQZVM1SGki9IZUNjz32nahVR4HWuTqwVcg27YzYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fcdf5128.mp4?token=gTIoPZekdH-2z_TeEI4cvdWTJ6g2UkgnAHE_foyNdLWnPpY57ye4RjYRwFsKKRBVKIHp-zIdIvAijxykeJP4BgvsKes2qNSzsRFbeTvhhXPeRthqRbeR80Zaa1HJfieJNyUtXGeBQbF1W5-ypcVP4dJz3KNdAYrTGiC1Lo_JQAm2_VKofrzf60f1rjmVbVrzzVYrGOhGHs9Wlgmi4Cj8lPt69a5dPHiZZ8pCF1qgxqLfmkkn_dkcrmQZvOK2MXoPW_TXkvZzBtO_v3KX74G1HCCuv1UkD7xyy7fZfkVIX9XBr-VQZVM1SGki9IZUNjz32nahVR4HWuTqwVcg27YzYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیرکل ناتو اعتراف می‌کند پنج هزار عملیات هوایی از خاک اروپا علیه ایران هدایت شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/692935" target="_blank">📅 18:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692931">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsjKNvLY18U7Dy5NwOhekFoKmScNHWBhGns1GOjVl4mAmwu7XHxMvQp8dG3yRMQ6GBkxJFWTppxdxbJPuzovNbYp_Gtys4Zu-4-xzicLdnrzVI6umHHLDEOjAZRtyIeatYHeuK8C7ZZquLcdu2YYddTlLPVoduawVTGJ1163XSWULUKBpsRbJ0E5jCP7cqzxapeZSpEjDlDxL4RvdiA4Ksd2ByhwGK4aOv53Ap_DbkyA2wYH_JNRZJ78Kd2xSTtshHF5u9KXpQmw2qseezhCUU9bqUK0LC7VEWohzQtaT9JozoENfaHSmwiU4_nz2odq6isroesqLnzKurOSrkneIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOGsiV7fWMlYxBZbQ6pl5rYIVZg1yzk-cMZfw7pl7BohaMOnaQVJ6HCjR4bHDq4N7wBIGtu3BgfNpdxNO1zsT2IldczcJ9XRuPt-V5sqMlJS2SyWkzPZBm1fIVv4K0sJptmxWlLXNjWWE_ALXIvDb0Gmu4ot1aKcEiPcUwxoE8Ai9Prbotkxf6TI88nFhLjgFYWnhEPfsqgj15HWSJ1z8jQLTfceiTNFeFVpJjNho2Q4Y-sRX4Oh6rq-qzNYXEYbB5zITYpS21dFSCKuhqPQU4piBrwuaYLDV9o_9WOwgvLnvq56nG83eNfUfgnbMpr254baVMUNFVpmfIqEG5z5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Md5V3JOejWnLedQhhV_L4888ejBDvqbmzcV8Yw-dUshjDEbo_sscwNb1e98O0WwuQftNhUsLWs4dp-8AZ_K0UJiQAc7rQY-eiyilMgcev7YBvro-lmic5XOHl3MhQQy4HeSW24PsFJLjgEtniOygE8_WJc8PAJLRvyntfXn6ux1ZpkzjODcZzYh4sVe9TiA_bpnzFlL22K8raKPn4gIKGITlVJerhr1GRrEI58U5xdTkyDis1MXBKklzr8KdD-asdZ9en8hx7HiJDD-hTdyktj5KcrDl1VYp1-p0KN_fijxMDhthKGsr9JkiJTsdKXLOjSU3qzJb5_qvt8ZytTsDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYft2wCLRdib6R14RqQXt43NwvAvM0H3GTY82gHDOEVGzvYl6X9hfxmnWaXWcWTp7UNWmuKTD8mkhugtp58O_G_2iLO6SJTZkANzrv8HGqWlUxRqAPAmkyx6phSVHZVueEzxEgeygU49EXOSTbvUpv6UH4Bc3HELAL9tUewpgdXtubBlskrHmwh3zxUYkXYVSM8yNOkhf4Bfvb3_8bLNtQa4tve1tWabHIDILA1eQpxJ3ntXhYkszXloIH3-ln8XwmIv-S3w2aLTr-zp0OqWMyMbTJnNct8paE5rj6pbTjCGJ2tN_fX0zUoePZEj1cBecQ4zfs9iG0ViIuu-o08KSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند دمنوش مناسب عصرهای پاییزی
☕️
🔹
با سرد شدن هوا، این دمنوش‌ها می‌توانند گزینه‌ای گرم و دل‌چسب برای عصرهای پاییزی باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/692931" target="_blank">📅 18:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692930">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان درباره پشتیبانی اطلاعاتی چین از ایران  سی‌ان‌ان به نقل از ارزیابی‌های اطلاعاتی آمریکا:
🔹
تصاویر ماهواره‌ای و پشتیبانی اطلاعاتی چین به نیروهای ایرانی در رصد کشتی‌ها در تنگه هرمز و انجام حملات دقیق‌تر علیه پایگاه‌های آمریکا در منطقه کمک کرده…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/692930" target="_blank">📅 17:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692928">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KsftNR8ZhHrgG5AjVyXC7U4NDEg3MZjUISpERbOsosuMe5JuhM9tWu6_NCAqGlQAHzmDcbDAoGcxbCZTOA0OVM3rHDUbIqSi9tKOmzNLta5vc4MELC_2qmeQexEvsL9NdnoDyVR0ZKailXRWvfVwZc1GVlE0JwYGGRxGS0Pdo-_8-dBWJglig0BzxXmO_3_DS6wrrUH3__CFFyL0XElAxY87h5DGfcXmk8-UW80Bxc5hXo4nhvfVSGP-prJrYPK8u_rn96VXwce_jwNgYkWkrkB7BJSDBSkhNP-ZYRsBYChenk0n7L-ry3Hs8PPuGXKqzsGAl71lPP0YkiA3FscG5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6vEkFwHFuPZq7CQyd2W9FJ68OkVdWszP6ch7c_MTYVNRgJvB9Rud9MYoAnrEAsjAr_czh6nRCcZScbPbsW0IRJ8x0KpPVoJT98HdgXQT_Piv9FqS0dXq40H-yIBfWqTGt7zewKBE0qjp9R9Czm4klzWrK6f9wlHWMbm-5zFMhLgp6bFv0wc1MzMhFviD8Cv3zNkW188hcJCxDIDMDVKInnlDgXtf-YOOAvT7BeT7qqEiwHNTi2Wka5_VxdBtHwT2BID1b4rMfcX7CIltA2GlQTT8Pfd80VQ8nLfS-BNgzhGIuyjHma3g-HQHulnftWmMWtINjyTW-sHv9enc5tEbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بزرگ‌ترین تولیدکنندگان متانول در جهان
🔹
بر اساس آمارهای ICIS و MI، چین با تولید ۱۱۵ میلیون تن متانول در سال، با فاصله‌ای چشمگیر بزرگ‌ترین تولیدکننده این محصول در جهان است.
🔹
ایران با تولید ۱۶ میلیون تن در جایگاه دوم جهان قرار دارد و کشورهایی نظیر آمریکا ۱۰ میلیون  و عربستان ۹.۱۵ میلیون تن در رتبه‌های بعدی جای گرفته‌اند.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/692928" target="_blank">📅 17:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692927">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzGxYGtmzV92qTk7GaSkCfTIXnlOFJYb3J92TF36Xcd1Dnyp-JAjjmNC66L1JpI_neEUzzakmhH5RZfGkgEp1E3PkYa0PXLcnOo9xR4EisDOjfqg0udAL2G6SAWL4HPovfdDDoZ74nraHsua7NNh9QF9Fu1AJ22Wqipga622Iggn7wjVAciBr01fTQL9u_QNaskGIU40pIC12qUnSCYLXA1_tcX0xo_-eEuCH_Mu3HRBDIFyKDMWP7R0LMYFvOIcR_7q6_p-Jzx3a9tJJ5l0JqnY72kSghmUJiAwBQ943945h480rzP98yi1vTbGI0L63eaHv4H1GzInSWYjFOqP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قبانجی: عراق نباید تحریم‌های پروازهای ایرانی را اجرا کند
🔹
امام جمعه نجف تأکید کرد اجرای تحریم‌های آمریکا علیه هوانوردی ایران از سوی عراق صحیح نیست و از دولت این کشور خواست در این زمینه تجدیدنظر کند. / خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/692927" target="_blank">📅 17:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692926">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
عروسی عجیب با تم مرد عنکبوتی
🔹
تصاویری از یک مراسم عروسی در ایران منتشر شده که داماد با لباس مرد عنکبوتی در ارتفاع حدود ۱۲۰ متری ظاهر شده و عروس نیز با گریم این شخصیت در مراسم حضور داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/692926" target="_blank">📅 17:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692925">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjbJIqqaUN8nM97MCNnHSjb0dTNa4WntB7_wE3_av29wWQVeYjXhS-DQfz0l3mEiz5gUgGz335zkq7zwtpp51cICvDDSr4CWs4XtVGMMxY-yt2BvnRVJ8OcWm7ecVS-tT4_c7Bsqt3dy6lkql8pURpt6jrquEyRdhGRXaKp5k5mzvERlXPEzkKtY5kwEoQfzB4C3sYdZCB3_c5Tbuq0G879KgcdStBCWJ_FJjpoCY3UIhe7S-ljsc-Q_urxA-gPYPLg8l9J1PUxSX5WbvC1U4ghxpNs1tTpE00eBkmDhfk6EZlsxKnzlunENvZXDSJjGVKTUbGFLwvqpdAlZNdKkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: همه باید به‌جای «هوش مصنوعی» بگویند «هوش برتر»
🔹
از این به بعد، در همه اسناد آمریکا و امیدوارم در اسناد سراسر جهان، به‌جای واژه «هوش مصنوعی» (AI) از واژه بسیار دقیق‌تر «هوش برتر» (SI) استفاده خواهد شد. ببینیم این اصطلاح جا می‌افتد یا نه؛ خیلی بهتر…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/692925" target="_blank">📅 17:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692924">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
تصاویری از تسلط نیروهای مسلح یمن بر برج کنترل تردد کشتی‌ها در تنگه باب‌المندب در شهر مخا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/692924" target="_blank">📅 17:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692922">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i89Np1mwqpO3lWQVVjuWzu0lSpCXya1LjuP-DK61x4PuCi7PTH8K2ZHlOLAIx-wAIdZ8GdYsgSnzgJOpzy64xygGkMkL6KjRWjUbCGhJS4RrbsPNVkzX5FIV_fiQrmbv-AF3W5UThrOFuSxZIivoSDEkwhboyVhzHKA6zH-6CntXoFleRVEIQ4hf3cATtveio-IKkWE4cfGgrude-B7xEgF41T9hLZEvS9vpxsu59b7hPd671ns9_G89CK6w1UFfRD1SC10iqJ7rN7r5LLwx_CIv5SOlaOzHizc9V_lZi8eEj3iBNxTFtlmIdkNceJ-QH8eRApjUTR3vdFS1nn67EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدئویی از مراسم نود و ششمین سالگرد روز ملی عربستان سعودی در تهران
🔹
کیک سالگرد به حکم رسیدن آل‌سعود با همراهی معاون اجرایی رئیس جمهور بریده شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/692922" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692921">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
توقف فروش بلیت پروازهای عراق تا اطلاع ثانوی
سازمان هواپیمایی کشور:
🔹
در پی توقف پروازهای نجف، فروش بلیت این مسیر برای امروز و روزهای آینده متوقف شده و وجه بلیت‌های لغوشده باید بدون کسر جریمه به مسافران بازگردانده شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/692921" target="_blank">📅 16:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692920">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJTboKG_PGLbwTm2E7ST2NZvx0gI5cgodU_UlcKLseJidI_PS2OsKbWA3f5CeWN6YFOiPGAtI6Tbi9-xwAN2S1sEtkv0uFdC-QAOZqS6_ZdFc_o-Y8do6ZY9mdUQUlWpcrwHilm_v7efIUz_pLuDQokkcBpN2_yuO_pucvRnr5pVkGvIO0cS2WwMo7GWxvRYt22LGg8SB2sfmiKif2Lg5vfMk9wuHndG26PV6Wuy5taCZAaIC5e-DUVQFDHgS8cXto-uGg8ilKjbdPRmerKfDI9crh9-2u5p6lNFD_lnep2NG7qomOJvK_4gezy1Ads-V3L4apf2ZbCv5qvol69D7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چیکار کنیم که موخوره نگیریم!؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/692920" target="_blank">📅 16:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692917">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmkfXKoXgvMeaYGVp5W0ufKYePE5j3Pwdrzu5Y_fTgXNHe7pFIrdsrZnb0MW2SNK_jrp5Uz0wi3ZicA2xCTVe1qHrAqJgu19AuM8GTavKN0LmeAjK7BYIn0gAXU6yIZm_6lsNQYd0KZCVQVv_Btxd1i8WlBrByWJxaKiFgjVTvif-5XKLJ2f6R6yhKwpHkh_Ry-8a5bA1DncMGpOCvCU2S97yv78u7ZZe0hdaFo6582_8NwjQWjlWCAneV9BqwIN79IGLxeCk1PMx3aoZgbVhjQ6nGuSLAfAixakIStdA2x4TjoSiHihSSl5mo8QfTZ5pXw8tIBgb6dgD-fj3CyH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlEN8MynlloJ63oPwnoJYMSj3XLUv_hoM2qeUECWcmp5V99i1J2EioCxBFPITX967f0cwFsLlFGADsgs4kYWQkkRnhE7mzcaEktKax_SdUFrO9CimDp5VQn3QNdV2IhWiWiX2Wq6cnYcVic0yFZGdR2QzpTcsgW9_kraNs-JkPXQPh87BTrObCgwr_EmRvvWM-ppF13rFJ31a_RV4Ws2H_JEh8cqJgLCn-kuuIWj-UlXVN1nn99sJW-ka5__zeJIYKEN5GceK1nllzlCr2xj_Pesf0oa2D53No_gB0uAPJmzhxt1MCkMdWK4O8yjDUdXdrfJlHg7qcd0zmof_k_dIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4ZDECIRbRbgzfA3cdqlfhrlboTefmFLYmnC-6UFWseV0W3ZNOgHYt3q7rWUoOztYlHrxuYKap1VZYIMS4raVhiOLM3sjaYlm1CbP7ltXrYXKYxPPx6oTDCDtbo-k4aAAJT4louEBTHQMln3xVTZ8kzVoYoYGFNORNZ5bp3pDeKhnHQ4X5aKoGMlWGWn38-US0wQLmoNh9XY_chaUz5XyIWJdlLpdPJXck2SaXKvfok9C1VTBhbGGmg4awuK_lIYShMUbhtfAlB5vZGQn5JifwtxD8DXzRRk65h8zKDlBqt8lfQ3aQs_FENJ17koKpyNe4GVkD0cMs0h5wSqmsXg7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
میناب منطقه توریستی گردشگری نیست
🔹
عرفان کوچاری عکاس خبری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/692917" target="_blank">📅 16:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692916">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c889ef1f42.mp4?token=McbTw1P8vB7cJVEBe0WT6j05sVGj4GrJL26iwAHywi8VlyRwxZn2zW5T4uLXfh9JWglkcLVf7-u3yFUL_MDmiF0VRlhdo3U4paf-F0i1vWK-UT6qUXhXbnTMznprcc7f3HlP8YAu9QfcFThmJlekdrdkwxjORdkxi3FH6nibpwH-UXUYLVOvTAzqPGNBoyHVuq5vjoRzFrHAIpLcYgxhP8r2fETHcBR1w6t7eUNwIfw3LFhyIydQeJqxAYUFUte3qL9bdF4lFfcJtfzs4bQ2mEN6wyX-rrMcIQVi-eR_8Q_oDx5gm2vOMKmJxKHwaHGf9bJSPSTd3jI7qdOHPF6c9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c889ef1f42.mp4?token=McbTw1P8vB7cJVEBe0WT6j05sVGj4GrJL26iwAHywi8VlyRwxZn2zW5T4uLXfh9JWglkcLVf7-u3yFUL_MDmiF0VRlhdo3U4paf-F0i1vWK-UT6qUXhXbnTMznprcc7f3HlP8YAu9QfcFThmJlekdrdkwxjORdkxi3FH6nibpwH-UXUYLVOvTAzqPGNBoyHVuq5vjoRzFrHAIpLcYgxhP8r2fETHcBR1w6t7eUNwIfw3LFhyIydQeJqxAYUFUte3qL9bdF4lFfcJtfzs4bQ2mEN6wyX-rrMcIQVi-eR_8Q_oDx5gm2vOMKmJxKHwaHGf9bJSPSTd3jI7qdOHPF6c9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان در گفت‌وگو با فاکس‌نیوز: اگر دولت کنونی آمریکا بخواهد در چارچوب قوانین بین‌المللی به توافقی دست پیدا کند، خوب است
🔹
اگر نه، چه پیش از انتخابات و چه پس از انتخابات، چه تفاوتی برای ما دارد؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/692916" target="_blank">📅 16:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692915">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9537af776b.mp4?token=b3yov51-hy3JibTCXAgWM1nT-mIiBBiNB-G10uWrKPDURkP-4X5ghhdQfiFRyCFCPAdbV6PrxghGZzzIJK6-Yf4YT0Z1FNv6y77IXpkOzaWdpl3NJh38psw0EItuwSIf4ypdbqzboWQP8oZbH91U2kn-XHh_qqOxYlFj3ZIidNYKBWlv9rDZhL_3BOFGL5ILgjbbLvabXNbuxNdmyU3ml7Ql-vbP7Ur-VzMfxbIpJwz1rBLnejd8wJNeftCgFFOYH3ErCklSPVGgHFIRFBQgrCvjKRhdGe8I6wObLAgfZNJsxnB_zIs6QR1e7RMQNr0OvvfTRB0KveCrAdq12bEopg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9537af776b.mp4?token=b3yov51-hy3JibTCXAgWM1nT-mIiBBiNB-G10uWrKPDURkP-4X5ghhdQfiFRyCFCPAdbV6PrxghGZzzIJK6-Yf4YT0Z1FNv6y77IXpkOzaWdpl3NJh38psw0EItuwSIf4ypdbqzboWQP8oZbH91U2kn-XHh_qqOxYlFj3ZIidNYKBWlv9rDZhL_3BOFGL5ILgjbbLvabXNbuxNdmyU3ml7Ql-vbP7Ur-VzMfxbIpJwz1rBLnejd8wJNeftCgFFOYH3ErCklSPVGgHFIRFBQgrCvjKRhdGe8I6wObLAgfZNJsxnB_zIs6QR1e7RMQNr0OvvfTRB0KveCrAdq12bEopg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر پزشکیان: ما هرگز جنگ را آغاز نکرده‌ایم، اما اگر آن‌ها بخواهند به جنگیدن علیه ما ادامه دهند، ما به شدت پاسخ خواهیم داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/692915" target="_blank">📅 16:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692914">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22f1a729c.mp4?token=IP77DOZpmf0_ly3Mg2kEdntBxg1iOWo9ep8w3KkXohJjDag6WGgVcyT3p532X7zMX1IwmWAvBaGax7mEYO0HUCLCHh0kSMrT6T1bbsbpKF5rslnm1Uo1bRsVruZU9uZTVDqdobhyxOXBV9dQrdPkwGJWLJdFWlyLvsf4tXYGuhs4uLwMJdH7jUOD8NH_bAbikpDRJoRhhN2Ln1EMxBrLhHfROCx8z7RXtGJ2iu7Hd1Uyyvar52GciQLsoIr_SC3GEX0cz5I8bQdyNnZSzjWD_1uIaZK6iwTWxnORVKYLMWpOF3fcPfK0anZ5_oGy58pZ4xnSLc2_029opgPAANEg1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22f1a729c.mp4?token=IP77DOZpmf0_ly3Mg2kEdntBxg1iOWo9ep8w3KkXohJjDag6WGgVcyT3p532X7zMX1IwmWAvBaGax7mEYO0HUCLCHh0kSMrT6T1bbsbpKF5rslnm1Uo1bRsVruZU9uZTVDqdobhyxOXBV9dQrdPkwGJWLJdFWlyLvsf4tXYGuhs4uLwMJdH7jUOD8NH_bAbikpDRJoRhhN2Ln1EMxBrLhHfROCx8z7RXtGJ2iu7Hd1Uyyvar52GciQLsoIr_SC3GEX0cz5I8bQdyNnZSzjWD_1uIaZK6iwTWxnORVKYLMWpOF3fcPfK0anZ5_oGy58pZ4xnSLc2_029opgPAANEg1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون، مجری مشهور امریکایی: اسرائیل ۳ هدف در جنگ دارد
🔹
این اهداف شامل حذف ایران، تضعیف کشورهای خلیج فارس و خروج پایگاه‌های آمریکا از منطقه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/692914" target="_blank">📅 16:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692913">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7QK954JaZSf-dXnAMaN9SisJtObtHZHE9DNozXbIITA22AxWz1XJs6NGhjh_3PDq_5qKta-Mvpr8GdpBflo2DNXSlf39tk9wByylviHxyXFD5VNHtyAq_EdcNXoODgBJAkMeMKHJlEg9vODozV7Wa2o504DqfU4uo5-7lz7c3yY_x7Q5wW5H8BnBWjY8es7PCMqs64Fpmpf3gO0bgwYBZ5ZZEgixI5xqgeBVWWrKojfqqzzdSJbGMO9z_e7guc_uzBcC8ACMKCXFpTsa7dOdvq0uK1y7Xq5FrBE5FZj4LOWQAdv4NZwl1L3Z20woPqUpd2VQzWYfyboZ4oOIRRyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلمبیا به طور رسمی روابط دیپلماتیک خود را با ایران قطع کرد
🔹
کلمبیا در این بیانیه ایران را به آنچه «ارتباط با گروه‌های تروریستی بین‌المللی» خوانده شده متهم کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/692913" target="_blank">📅 16:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692911">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-MkgbW86BGYkbxseC5362QUBFKLZ-rZp5PdtSwL9vFXbqjXqAKFTuqXnu52zUqc53o8sLQZkkaRAzoOPS_Qp9yds2szqmom5JCcVXtgSmlDEeh_tSNEEDnvRJyyZ4JZRP_kGgxg-qIHLJP39mO1dsJaaXZrzMV3bYZAI4ZkwAE0lnWhoz2CwzZNhpFdasOY_h-Ob8FhWIGe8mRVQDMaQCyhp-sYq1XghDdcrpNVWblCE2BPoYu_prXLOzwrWmmWrDZppcOVBWUaVXTsez6pkpgiW4a_t7qi5O3MNQ1qPe8aNj3xjvg9ZhWjYA9oY5J58AdZyt518iUIMEFrdRwXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خروج نماینده دولت تروریست آمریکا حین صحبت‌های پزشکیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/692911" target="_blank">📅 16:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692910">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85bcc69018.mp4?token=sMK_8F4n2E4KN0ZrNTIg1uO2n6MHLN2i5MuCZqIYE2pnnQe-jYwaxx4p25rviFC77FjwIf9TAJXDlrYb7b4dwkQQyJvUyUq69G0eRGNvvNrRT6WSXxvxycvahLN51reknxodW-g0zFcZsoRm8PqWXDenQz9KqlYOzD1kZ4wT9kCSS2Id1ahhlummBjquw-RZPbYmpF3h5uuDQit4DdqHI_fPgpwMVuUsF87JYynmfg3bZ4PEBHA0Q0gHVcnKuBLF5gG_g0nfss03QEsWWKz9QzANJC-SFgzKGckk6I5-TGHen4aueHSGh9mZHyZC62QxUtYkHvXEdK_SDG1DTDRtYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85bcc69018.mp4?token=sMK_8F4n2E4KN0ZrNTIg1uO2n6MHLN2i5MuCZqIYE2pnnQe-jYwaxx4p25rviFC77FjwIf9TAJXDlrYb7b4dwkQQyJvUyUq69G0eRGNvvNrRT6WSXxvxycvahLN51reknxodW-g0zFcZsoRm8PqWXDenQz9KqlYOzD1kZ4wT9kCSS2Id1ahhlummBjquw-RZPbYmpF3h5uuDQit4DdqHI_fPgpwMVuUsF87JYynmfg3bZ4PEBHA0Q0gHVcnKuBLF5gG_g0nfss03QEsWWKz9QzANJC-SFgzKGckk6I5-TGHen4aueHSGh9mZHyZC62QxUtYkHvXEdK_SDG1DTDRtYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از نزدیک‌ترین محل به مقتل رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/692910" target="_blank">📅 16:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692909">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVSox7gv9sRpN13-4qzY2zCb_wO1E6wS_LUU74CzLuUShN2OhWx-P1ntUPIvUHfr6uyW8ZbggOmhGyWF50Z8QzieXpINPyG1mbTcGCYD2ccfoHVG34b1k-41YtHnixtdCuwwdrcV1Givt6nVbFWNqsXafTannCkvQ3gwvoc-b9oiQCfHOmYAPkkjTV4fg_-wbMjJFQJS_IOJ57NEkbc-YMJjlGZUTLt4uuJ_VIfeRVZSJiPqNsrWWc9A7lniSHM9aMD__E7wdW6OAxutCninl8fwalyRbTxrvNmmKqb9oGoW_EYzj3j0SDLoYr4R8bMvc0AT1WXcFplYipqLscKLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از خونریزی داخل مغزی؛ فشار خون بالا از شایع‌ترین علل بروز خونریزی مغزی به شمار می‌رود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/692909" target="_blank">📅 16:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692908">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj3GRJk0Kzl18Cyc1KEOYZdsn7C7bCgrwvKU_PntFITCLhl_hyKTMYKAY4vUzKztwvpLO2-XA6nG2kwqB_xlLc-lmdULWk3LQul-__kmLl4qwTzccF-WkzbJd1ncInf-2W6u0hWy8F_tvhnd3IM8CpJ4_Q3zAiKFdzrWbHDnyYHWDU73GEFF4_ZlMhgaJuhLbO5s4jP7h-PMe2sWq-l8uFwA89IMN7sWIJBHOPGSMezrhrT1Db6lLL3EjCabKaP96V5gcxJufKEctfnSEumI5qx4Lov4TqpIctIGWndlw3PTneKzfa487ZtneF8tVSvd1NS-Z3Ruqcx5JwOFtzX9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷۷ هیئت زمانی که نتانیاهو سخنرانی‌اش را آغاز کرد، سالن را ترک کردند  کشورهای عربی — ۱۸ کشور  سوریه فلسطین اردن لبنان عراق عربستان سعودی قطر کویت عمان یمن مصر سودان تونس الجزایر لیبی موریتانی سومالی کومور  آسیا — ۱۴ کشور  ترکیه ایران پاکستان افغانستان بنگلادش…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/692908" target="_blank">📅 16:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692907">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
نفت در بازار نقدی به ۱۲۵ دلار رسید
🔹
قیمت نفت برنت در معاملات امروز بیش از ۱۰۶ دلار بود، اما قیمت برنت نقدی (Dated Brent) به ۱۲۵ دلار رسید؛ فاصله‌ای حدود ۲۰ دلاری که نشان‌دهنده کمبود عرضه در بازار و اختلال در عبور نفت از تنگه هرمز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/692907" target="_blank">📅 15:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692906">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8afb82f10.mp4?token=jp1LCY3LFYYXqoKAQ0G-nReGIqJKcMIpyl6CRVsrPq-IINHnKZUGv9qQCiLrfsB6HQ_hMjr5cz3dXYuPKEMUFoyWo41x-qvPOAbBFIQggJ3hxI2OUS5aBi329vMGhXjLylqDmNQIM8MqILxzs60VX7he4go1iVGLTLcfc6klogMI_2fbE1Xr7u_Ps81rxnVvn8kg_UUkuHtfOnVgONIlTpNgABerbzrCtS4SbWDoTLYkCyIfkGwwIKvUTpM2x04ojUd8UhMmbzq6A8BbCZBLPIhz9Zwyo-eNe8cHQZ0InmpSxQaukEncLv76wzG0V5TqmxAxTPJ_zX2k-qV0TzrzLLs1oHAflQYRCovN-YTRWga0NLLl33PofA9I05LgTLWSePwxmK_75kM8d_gRVtIlExIiv1ckYvP3iaMbN47UaCMvaOmsuwDaHaU8n-7jPBYYFM7m64jAWyI8J5i6oL4yk7-ETbo1JM4q2_2WPTSDlfbishxVBZCPHL3p8d6L8o087DEYntkOW1xkDTi2fNIx6ZEQqkQt_OcXTc_jtKNqNRfW_9L8DYKmlA84_lAEiDc6zu8sZEsUH25NV9NeV4WdwHMjq8PprbTGI_KrCLELJ1swfpl4TzjtPsZGCfbSUE7gmvCslzF8Gx9bAJ1OJAeVv8eEpwDd8eJ6mcXppDtjkQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8afb82f10.mp4?token=jp1LCY3LFYYXqoKAQ0G-nReGIqJKcMIpyl6CRVsrPq-IINHnKZUGv9qQCiLrfsB6HQ_hMjr5cz3dXYuPKEMUFoyWo41x-qvPOAbBFIQggJ3hxI2OUS5aBi329vMGhXjLylqDmNQIM8MqILxzs60VX7he4go1iVGLTLcfc6klogMI_2fbE1Xr7u_Ps81rxnVvn8kg_UUkuHtfOnVgONIlTpNgABerbzrCtS4SbWDoTLYkCyIfkGwwIKvUTpM2x04ojUd8UhMmbzq6A8BbCZBLPIhz9Zwyo-eNe8cHQZ0InmpSxQaukEncLv76wzG0V5TqmxAxTPJ_zX2k-qV0TzrzLLs1oHAflQYRCovN-YTRWga0NLLl33PofA9I05LgTLWSePwxmK_75kM8d_gRVtIlExIiv1ckYvP3iaMbN47UaCMvaOmsuwDaHaU8n-7jPBYYFM7m64jAWyI8J5i6oL4yk7-ETbo1JM4q2_2WPTSDlfbishxVBZCPHL3p8d6L8o087DEYntkOW1xkDTi2fNIx6ZEQqkQt_OcXTc_jtKNqNRfW_9L8DYKmlA84_lAEiDc6zu8sZEsUH25NV9NeV4WdwHMjq8PprbTGI_KrCLELJ1swfpl4TzjtPsZGCfbSUE7gmvCslzF8Gx9bAJ1OJAeVv8eEpwDd8eJ6mcXppDtjkQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از مقوی‌ترین ترکیب‌هایی که تو زمستون هم میتونید بخورید
🥛
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/692906" target="_blank">📅 15:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692905">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7324ff78ff.mp4?token=jCZ4BljoqaDceGi08OTt9pFht5lHlz6Q-HKsgGGhKXVYhz-k-_GGUrVQ0wXX4qzsTfX4UPyAEFI-81e7wt9wIh1adU6-0bZvK1gJr-7X8ebXW1fhDupIX0fFWCpzZDXYPkKOM9YNfPGjiPq5hozuNLxmzsKYJgT-nn9N7tC0kfbL_Wl0Clk35sRf22xQ5DpzOTrkZVLdbQMKXQfeM-Giv_BBFCEby8WQ1DLUHYH4YNonHZrVy2GE0pnwyNJSjxAa25SsyzTM2efJKezMeQsTwT0YJKUeVcT-l5sgsEEB49HwYXzj8cKu8vb22M84F1E1YanJHjIk978hV9fmglQofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7324ff78ff.mp4?token=jCZ4BljoqaDceGi08OTt9pFht5lHlz6Q-HKsgGGhKXVYhz-k-_GGUrVQ0wXX4qzsTfX4UPyAEFI-81e7wt9wIh1adU6-0bZvK1gJr-7X8ebXW1fhDupIX0fFWCpzZDXYPkKOM9YNfPGjiPq5hozuNLxmzsKYJgT-nn9N7tC0kfbL_Wl0Clk35sRf22xQ5DpzOTrkZVLdbQMKXQfeM-Giv_BBFCEby8WQ1DLUHYH4YNonHZrVy2GE0pnwyNJSjxAa25SsyzTM2efJKezMeQsTwT0YJKUeVcT-l5sgsEEB49HwYXzj8cKu8vb22M84F1E1YanJHjIk978hV9fmglQofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
با اخلاقی‌ترین ارتش جهان آشنا شوید!
‎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/692905" target="_blank">📅 15:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692904">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
اختلال در چند مسیر ارتباطی اینترنت ایران ثبت شد
🔹
داده‌های پایش شبکه در روز جمعه سوم مهر ۱۴۰۵ از اختلال و افت کیفیت در چند مسیر ارتباطی اینترنت ایران خبر می‌دهد؛ هم‌زمان، اختلال اینترنت در استان‌های مازندران و مرکزی نیز در سامانه پایش مستقل آی‌اودی‌ای ثبت و تأیید شده است./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/692904" target="_blank">📅 15:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692903">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLUW74Azzsin9vYDdkiD4N2A59cVuYZrFR4QV-5hv2GXnSjQ8zayq9JQjRbgDSqVofxFJBV40C-O5YvUlYS7PIvDt0lz_iuQQN7IHznnOU9pTEr9w0pkrKlP4q7wUixEg9Vb_AjZYpLpbBnRO8oF2wsf9-dokRPD7L8v3p-ZHNmpc8XBZWcpKnks6GH_m2ttvBPx9GAHUY5So2rilwam0LSBuoGv5WoweVck1IlDXnojeVgCilyDoUWTWEcDnHjopoei3z6w1NA4BNpDDoyZTgtNvK8Gckcyx7ch77QLgY4uzX4JmLwF_aUSdwbEUQGE-4LcgObCfC3_GCdoK-p9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف کتیبه ۳۴۰۰ ساله مرتبط با پیمان قادش در ترکیه
🔹
باستان‌شناسان در هاتوشا، پایتخت باستانی هیتی‌ها، قطعه‌ای از لوح رسی و خط میخی مربوط به «پیمان قادش» را کشف کردند؛ معاهده‌ای که از قدیمی‌ترین پیمان‌های صلح مکتوب شناخته‌شده جهان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/692903" target="_blank">📅 15:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692902">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
نصرتی معاون عمران وزیر و رییس سازمان شهرداری ها و دهیاری های کشور از تشکیل دبیرخانه‌ای برای هم‌افزایی سازمان‌های همیاری شهرداری‌ها و سازمان‌های میادین میوه‌وتره‌بار و مشاغل کشور خبر داد و گفت: هدف از این همکاری، استفاده از ظرفیت‌های موجود برای عرضه بخشی از کالاهای اساسی، میوه‌وتره‌بار و مواد پروتئینی با قیمت ارزان تر، کیفیت بهتر و سرعت بیشتر به شهروندان است
🔹
در کشور ۱۶۲۸ میدان میوه و تره‌بار، ارزاق و پروتئینی فعالیت می‌کنند و در برخی میادین میوه و تره بار در شهرهای کشور، کالاها تا ۴۰ درصد پایین‌تر از قیمت بازار عرضه می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/692902" target="_blank">📅 15:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692901">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سمینار آبِ ناب مزدافر مؤمنی قسمت سوم</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/akhbarefori/692901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
آبِ ناب
؛
قسمت سوم
سخنران: مزدافر مومنی
🔹
02:40 آبی که درمان تمام بیماری‌هاست را بشناسید
🔹
18:00 افراد خاص و سران بزرگ کشورها از چه نوع آبی استفاده می‌کنند؟
🔹
26:40 آب حافظه دارد و اطلاعات را منتقل می‌کند
🔹
32:50 تأثیر ذهنیت انسان بر روی آب
🔹
37:00 شعور آب را تغییر دهیم و به بهترین شکل استفاده کنیم
🔹
قسمت دوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/692901" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692900">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2S1o8VmO1b0tZiBZIeirtlVTG-oWB3JLNiRn83UDUxWaRkjcvHbb07zlqNpzXp4EtGv4AnsCBkPrEeLvkpgoMrG5cSXArzkzgwEYJTtC1qkVGKJBco0NpPEtx5BXMGnWWSctuh7kpEbN6gtc8SAgCClWTNRdG-c7HXz79LX5IVLgsxIX8lYKYSTGBZeyNxEOKnYEcN97d6cNdZzM-mjt6TygdEIs8405w5snDxbWEPqjD3fG8BUbyh2L-wIGkRn3gLDgCJgC6WusrtxJCb5feLJqPiDi29eRObn5UfGycw1vH7eZ1LsejWKzdhjcRAT9_GIFxel2rkuloOdpa-Ldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | جشن فرشتگان
🔹
همراهان گرامی خبرفوری، شما می‌توانید با ضبط یک ویدیوی کوتاه از دانش‌آموزان خود با لباس فرم مدرسه، در این پویش شرکت کنید .
🔸
از کودکان خود بخواهید این جمله را بیان کنند: «کودکان شهید میناب؛ ما راهتان را ادامه می‌دهیم.»
🔸
ویدئو های خود را به آیدی زیر ارسال کنید
👇
#جشن_فرشتگان
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/692900" target="_blank">📅 15:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692899">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz3hRO-lj11KjrCatx_SPxOgx0ZWct7OneZ7paSjKbOC4AngLJi3-J3r1IXMQCAVvpR7fuJ0iTQXy1JGaUAxS5_xEb9r1cbdlnKcC4dab6MeUbPXjqqKKl9jbTn9lp2W2xwp74IPGX5EwT6XvG-Jw-tiIYThM2Z_hXSJBZGd5axzI23nYyXUa05xgAdmT_gHYoDYqPSNcoTdtk0jJ2fFiTlHSev9P9EEmJQPRGbbbZNbryGv8b4i7pTU7LXMzJE53IRrvX6dmhT4wNlrCIX15H_DNKy5xnW995CpsZorukZjp8M7AhlQqrU76eSwiGEiS_VdFz8opFrixl3rM5rxZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فکت‌هایی درباره تخم مرغ
🥚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/692899" target="_blank">📅 15:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692897">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
خاتمی، امام جمعه تهران: کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/692897" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692896">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ9asUvKCb8SkeyCIX1wxzIZ0KDiRspuU15GkIwIFFEd_Ia_pAVMqwBrxzQHz-FhC47VH0nSO58JBZsw2NX94URrYt2_bEwI09SvWcIb83LVmvw5iCNi22BzpXZWwp_H49II-aAw_mVfMYK7_WAi_G8h-3Hebbj8B8rW__H9hEmtoppUl1D6eZ_7sk2xvXXZqkuLkc2iec80Yll_cG6NlNnpYIlwGRdWuM2pxyFe2AQybsVOXzk4SQ8Bify7eRQkYMh_ciGlHgwbBR_jI3bwvaPwp1C7W-WgvBTA-hnXga6lJ5fHSryCdsiX8BQSaUxgHvOOOA8tAYqlhhR7DJvniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قبانجی: عراق نباید تحریم‌های پروازهای ایرانی را اجرا کند
🔹
امام جمعه نجف تأکید کرد اجرای تحریم‌های آمریکا علیه هوانوردی ایران از سوی عراق صحیح نیست و از دولت این کشور خواست در این زمینه تجدیدنظر کند. / خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/692896" target="_blank">📅 15:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692895">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1aTPufjNGNqMq1yHHOk3NwispYtOo6CeO0zFSJ37fbll-ZCRynDgJGrZIADL53AiATOvp7_7lcNKZxu_EDn3wfq5zZhZ6HneDdBzzRR7v9KejuNMCNo_qCwWYxcGvu4RtJq1ufao4DqT1i0DlZnS81OOHI7ekr4C7pUwefWLil6dM6jp0vicRMax3JDYHl7bIMAvOlUI_ss54CBmEUcSWdeD4rineN7rdl4UdzMne5yIIDfFO57oaFFf8ni2xk4LsRF5oL2HS4RfBYbvrUDuvxU_sDvPfRS-49rBvLF2xHkfp4i6sm3PP0pHxgHnl9A7rkiOi1Uwu0E3GmMp-Eo6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حضور وزیر راه و شهرسازی، پل‌های آسیب‌دیده هرمزگان به مدار تردد بازگشت
🔹
پل شهید مویدی (گریوه) به نمایندگی از هشت پل آسیب‌دیده در جنگ تحمیلی سوم، با حضور وزیر راه و شهرسازی به بهره‌برداری رسید.
🔹
بازسازی پل شهید مویدی، دو پل در محور کهورستان، پل نیمه‌کار، پل سه‌راهی منبع آب، دو پل محور بندرعباس - رودان و مسیر رفت پل رودخانه شور در مسیر بندرعباس ـ حاجی‌آباد به اتمام رسیده و زیر بار ترافیک رفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/692895" target="_blank">📅 15:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692894">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان درباره پشتیبانی اطلاعاتی چین از ایران
سی‌ان‌ان به نقل از ارزیابی‌های اطلاعاتی آمریکا:
🔹
تصاویر ماهواره‌ای و پشتیبانی اطلاعاتی چین به نیروهای ایرانی در رصد کشتی‌ها در تنگه هرمز و انجام حملات دقیق‌تر علیه پایگاه‌های آمریکا در منطقه کمک کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/692894" target="_blank">📅 15:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692893">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COFGBt-cGQzvzMNSjZCcuAAsn7Dd47CbfqxNaQw-tnrWVDcDIpO-vAgqv62zdDw75AY1KKlJ77GGPT-Ge1Q0wHSANn0l6fNG-zJoroXXdBmmXEftoCZa_Q1WoBdQv0JEA-UH9df1ovVvcywdkQAQk1f59Yj5BS3KLCTS4KTnJX-5DQfX9oaEvP_e6G6qGQK3JFjLlTjkOGewbDWiLiRlm8zjJwUHFnJUeOcVioFKNxFtp-gMXvWNmmZP5FZmV2H7TFBu68KQ9oM3P7hm_CDpQ633jm5jVGdKrGB6Ytp8fuyk7HQwJCkkVbnrdBP2VPtzKsw4tLnPlP7PfrdCDiEM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعلام اسامی محصولات غیرمجاز حالت‌دهی و رنگ مو
🔹
روابط عمومی سازمان غذا و دارو اسامی تعدادی از محصولات مراقبت، حالت‌دهی و رنگ موی غیرمجاز را که بدون مجوزهای قانونی در بازار عرضه شده‌اند، اعلام کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/692893" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692892">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ویدئویی از مراسم نود و ششمین سالگرد روز ملی عربستان سعودی در تهران
🔹
کیک سالگرد به حکم رسیدن آل‌سعود با همراهی معاون اجرایی رئیس جمهور بریده شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/692892" target="_blank">📅 15:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692891">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
قبانجی: عراق نباید تحریم‌های پروازهای ایرانی را اجرا کند
🔹
امام جمعه نجف تأکید کرد اجرای تحریم‌های آمریکا علیه هوانوردی ایران از سوی عراق صحیح نیست و از دولت این کشور خواست در این زمینه تجدیدنظر کند. / خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/692891" target="_blank">📅 14:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692890">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
شایع‌ترین علائم سرطان دهانه رحم از زبان متخصص رادیوتراپی
🔹
توصیه های بسیار مهم برای دختر های ۹ تا ۱۶ ساله؛ واکسن HPV تا چه اندازه می‌تونه از ابتلا به این بیماری پیشگیری کند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/692890" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692888">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: بن‌سلمان خواستار ادامه محاصره دریایی ایران شد
🔹
او اخیراً به مقامات آمریکایی گفته است که ایالات متحده باید محاصره دریایی علیه ایران را تا زمانی که تهران به امضای توافقی جدید وادار شود، ادامه دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/692888" target="_blank">📅 14:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692887">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5b367a5d.mp4?token=S6T-pVoI1HItjA0zfDz22uvJDYoi4wzcUCN8yXyjDRJyxsDOEk8UYu1OYTxxvB9DWD9d-uAGKyNrCQ7eRX_Zp9T4XZ2gbc1ljOU3_d0SmXsRAfwGUkSB_2ZzuKKb0c6CwoAaCFNHDCOf1JKQpcHsSH9HxeH0JbuU8X0HTxeFiE3m-oqsTrnTlT9rp-WTX3Z_dQwhIcPnwFbizWNaE8QzFf5JWu_sAmlYAQ9f3hnrXn9f-WxzbgfySpG5djQzX9vB0GqwAt7u4quuwvTYD2yVOsa7RBi9_9WQjhVnxrQ_HP3UJu0cJDNZV7aOHLuPSvD7tj8oJtJRNfVKlfWzQA_uiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5b367a5d.mp4?token=S6T-pVoI1HItjA0zfDz22uvJDYoi4wzcUCN8yXyjDRJyxsDOEk8UYu1OYTxxvB9DWD9d-uAGKyNrCQ7eRX_Zp9T4XZ2gbc1ljOU3_d0SmXsRAfwGUkSB_2ZzuKKb0c6CwoAaCFNHDCOf1JKQpcHsSH9HxeH0JbuU8X0HTxeFiE3m-oqsTrnTlT9rp-WTX3Z_dQwhIcPnwFbizWNaE8QzFf5JWu_sAmlYAQ9f3hnrXn9f-WxzbgfySpG5djQzX9vB0GqwAt7u4quuwvTYD2yVOsa7RBi9_9WQjhVnxrQ_HP3UJu0cJDNZV7aOHLuPSvD7tj8oJtJRNfVKlfWzQA_uiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از مراسم نود و ششمین سالگرد روز ملی عربستان سعودی در تهران
🔹
کیک سالگرد به حکم رسیدن آل‌سعود با همراهی معاون اجرایی رئیس جمهور بریده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/692887" target="_blank">📅 14:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692886">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
رسانه‌های عربی از شنیده شدن صدای انفجار در شمال فلسطین اشغالی خبر می‌دهند/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/692886" target="_blank">📅 14:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692885">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9464a14b0d.mp4?token=XrTMx_BXk0qVlsQziM3NGlTJNmbcLSgpoXFdo-3evmk1YxxgZTjVpWCHGOygXcKwwkIuZO19jThbC8ZYaHKc7z7ARg1-QNnIK-Nje5k4qf1ZzHKBv062Oh4rsq_j4tEjzHHhU2pBzENljsj8s18LLh8M203yaW7NJn1viFhO5xNctPIRt6Tdt-PLYUgzkGklHFD_vohnGOu1G7egNz2avioAh10T2nxk3BcH0DFwxQrMDsPfHTDQVC5V6Eq4CEdvkZvaM8ojGhyIiUdetQvYyl69W5RXM_DDLtIELEr0BD1xKfmKkW8eW7QP9FA-Fbw2a-IeuRvwHk06TKhBryOFcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9464a14b0d.mp4?token=XrTMx_BXk0qVlsQziM3NGlTJNmbcLSgpoXFdo-3evmk1YxxgZTjVpWCHGOygXcKwwkIuZO19jThbC8ZYaHKc7z7ARg1-QNnIK-Nje5k4qf1ZzHKBv062Oh4rsq_j4tEjzHHhU2pBzENljsj8s18LLh8M203yaW7NJn1viFhO5xNctPIRt6Tdt-PLYUgzkGklHFD_vohnGOu1G7egNz2avioAh10T2nxk3BcH0DFwxQrMDsPfHTDQVC5V6Eq4CEdvkZvaM8ojGhyIiUdetQvYyl69W5RXM_DDLtIELEr0BD1xKfmKkW8eW7QP9FA-Fbw2a-IeuRvwHk06TKhBryOFcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیرهای تنگۀ هرمز همچنان تحت کنترل ایران است
🔹
کارشناس شبکۀ ۳ با نقشۀ تعاملی بررسی می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/692885" target="_blank">📅 14:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692883">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/becf821128.mp4?token=mLt1JHUReor1QZ4Bp1Qz8nF5jo66b645nuBf-AdHxARs1JNK0Nu8mvK-XvqHJMOwpELzcGlhyySxzgFhzo5mGevOpmG54zftq5qaO8LkyZwPc123ZkOZ90Wf_0z3XatN2YI4DGgQAtTA65l1Nq6oMlAOjodcoj5xeu6kefjIHGF9YApakR0r40PxHz3dANd2nUSArQQstYg0iT4o095_fYjr5k94LHf1Ax9cpS1ZAmKJjjPUvVU8PkLJ5TG_43gI1WUn3RYhWDwWuljR_cr6LpU2t3jhj7F-b1tvmdgwsmN358wkadw3CrOsYRk7mXo0icsCVJ2blWC-HzU-JBBudw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/becf821128.mp4?token=mLt1JHUReor1QZ4Bp1Qz8nF5jo66b645nuBf-AdHxARs1JNK0Nu8mvK-XvqHJMOwpELzcGlhyySxzgFhzo5mGevOpmG54zftq5qaO8LkyZwPc123ZkOZ90Wf_0z3XatN2YI4DGgQAtTA65l1Nq6oMlAOjodcoj5xeu6kefjIHGF9YApakR0r40PxHz3dANd2nUSArQQstYg0iT4o095_fYjr5k94LHf1Ax9cpS1ZAmKJjjPUvVU8PkLJ5TG_43gI1WUn3RYhWDwWuljR_cr6LpU2t3jhj7F-b1tvmdgwsmN358wkadw3CrOsYRk7mXo0icsCVJ2blWC-HzU-JBBudw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال عجیب استرالیا از تیم‌ملی برزیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/692883" target="_blank">📅 14:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692882">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
وزیر بهداشت: کرونا نیاز به واکسن ندارد و شرایط تحت کنترل است
🔹
کرونا مثل یک سرماخوردگی در کشور همیشه وجود دارد و راه مراقبت هم این است که مردم توصیه‌های بهداشتی را رعایت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/692882" target="_blank">📅 14:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692881">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxa52ycJaY8xghlGaTnjIJItZFLGcYHV6VsUdreW6r3yUL9yHNWA1Y0zIIeWB5WtrhpqdQpBQbAVFPXTTMXk2275hrUWonVpUPX-zzLpZG7Gz3qMXlEVFGuETunD-e0c5Gd4kY6TCWntcEN5NPihflB8vxE43Rd_6n5dkdiZFznSrLTgfZT7ASYalvDdnSTkftjYkiwXH2TTnWwzHel7VY1d92mVy83o5JkVWH15qt1bJEiOgSoknjtTTqIzcOMWBlXzYMjtsAwfzCVnSGfTq8dLAprjXVyhrkSrCEWyyodjryZ6y3PWmDAnnhiaXW6KcR3GKfSF88LxrpaNR5IEHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر، مشاور رهبرانقلاب: پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/692881" target="_blank">📅 14:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692880">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
رئیس شرکت سعودی آرامکو: شرایط فعلی انرژی وخیم است و در بدترین وضعیت قرار دارد
🔹
وضعیت انرژی وخیم‌تر هم خواهد شد زیرا اختلال بسیار گسترده است و تنها به یک منطقه محدود نمی‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/692880" target="_blank">📅 14:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692879">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: میانجی‌ها از جمله قطر در حال فشار آوردن برای برگزاری دور جدیدی از مذاکرات بین ایران و آمریکا در اوایل هفته آینده در عمان هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/692879" target="_blank">📅 13:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692878">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی نجف در عراق، تمامی پروازهای رفت و برگشت به ایران را، از روز پنجشنبه، ۲۴ سپتامبر، تا اطلاع بعدی، لغو کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/692878" target="_blank">📅 13:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692877">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d985672499.mp4?token=XNadIY41Lj9EVC_NOz-Rm1k4wUmBNhtO823yGsMY-1XVwuflsmUYDQwcohM4yBaC-0royWILBLBa2RuLqt5xkmeKiL-3brV9a0S2LNmAizVUaJZkFofpwfkgC3WrKxIidQPdAoc4c6H4J5FbAY5UKbhNjY3U2xMG1siEnSD3YAZ5vfcHZrvgvjwuMW3Tf0DopnHlfc7GeYJo-QgzZD7KD9bbbZlS4jo6VdNISZEMlrB9gNwsjY3_RqDJ7_JA8mWTMW-h2pXNwKQVMHfi8qql5J6YcJmaAtqbrLR9kP2ApHfKCNvgN57QMtuipEhM6RwFrqCOwxKLiCqux9UVMZpzgXgU6CnzC9O6aLbjmpgmU82m3SL80IGMbgYBxkvClx6Che9BQO_1YW5blnV94qb-30xEnKmB7aMk51hvJFEzxi5NqGInaIG7EubzFkztQnjv4YbVtqOIfSUTOhlKkFihpor-uAKoj0aTCNPOYllwiPuY6HqgqXGizkmU_qilxe-aDBUlkKQesO5mlIcbGbgQP0Dn9bCdnOviiN7gdM_Q0TB7JoVVQ-XKyiJzy1J3k3VfI_VJ2uQ6M1-YgeNuIPPwoWLhngnV2Rv1Rq5NxVG2vYb93gTLwT3_TESjlNAH_5enshGjVKQX1CvrN1IEJ1dTMuctIxnOPu1eAjGxaeatxms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d985672499.mp4?token=XNadIY41Lj9EVC_NOz-Rm1k4wUmBNhtO823yGsMY-1XVwuflsmUYDQwcohM4yBaC-0royWILBLBa2RuLqt5xkmeKiL-3brV9a0S2LNmAizVUaJZkFofpwfkgC3WrKxIidQPdAoc4c6H4J5FbAY5UKbhNjY3U2xMG1siEnSD3YAZ5vfcHZrvgvjwuMW3Tf0DopnHlfc7GeYJo-QgzZD7KD9bbbZlS4jo6VdNISZEMlrB9gNwsjY3_RqDJ7_JA8mWTMW-h2pXNwKQVMHfi8qql5J6YcJmaAtqbrLR9kP2ApHfKCNvgN57QMtuipEhM6RwFrqCOwxKLiCqux9UVMZpzgXgU6CnzC9O6aLbjmpgmU82m3SL80IGMbgYBxkvClx6Che9BQO_1YW5blnV94qb-30xEnKmB7aMk51hvJFEzxi5NqGInaIG7EubzFkztQnjv4YbVtqOIfSUTOhlKkFihpor-uAKoj0aTCNPOYllwiPuY6HqgqXGizkmU_qilxe-aDBUlkKQesO5mlIcbGbgQP0Dn9bCdnOviiN7gdM_Q0TB7JoVVQ-XKyiJzy1J3k3VfI_VJ2uQ6M1-YgeNuIPPwoWLhngnV2Rv1Rq5NxVG2vYb93gTLwT3_TESjlNAH_5enshGjVKQX1CvrN1IEJ1dTMuctIxnOPu1eAjGxaeatxms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو پربازدید از کنسرت دیشب کاکوبند در جزیره کیش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/692877" target="_blank">📅 13:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692876">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e23ddb2a.mp4?token=Du7PcXzEi_9LTrLPRHoEd9nBY-tC6iYhvaJKwQvChewKK37hewGxobGES2kM6NrMd7qug8EN6WbUtlywUl9w9BZmqxU6wDk2FkvaXGrtsAv8beIq94WB7H7XcTieZx5OCQyR4t9acGlNXhDDQAyCKMyBIWNGV3qTBm_Dq20KFf8ETtnsGrRcrWx5Ha8ga6oh1WOKoVGEPk7g0LyzoNfdKUTL16txV9pKUM3btTV5M9_mc7xJcKfiZ5rjh1OfxzW-vkr6agU-p-_FJ33lsYUDGBGntBdsGuQgdJxNuKmyJe7FHMZqNmcYPmaWk_nLlg_QKnG8tuG4xpzKjUeOcRBmCjX2fGklxWw361S3KbuDF-G5JTgs6wu_YtoyO1qL3c0UyhczlINMG1wk3oqF0aGXroSQfQhBa_KJql_DEb5WwsfZTBfSAyjy8mnEm0ht116xc7Is2KgtUSYm-gwk44eIoA0SktleR7GkldlK7ulqznAgy4hM0-vN0Zwp87Vh2tECnw4W1I6wtCKFBWYvrceTVZsUvZXM-cK6fNYubYN6zjwEYUn9A3ltJDrxFhGHds-eTMc1eRF2jZuwi7sYiYF0s0XWsSeWMx2AQP9QZ03m9F9hdlpkqOZSzgMx9ZsXH40sOTbe_MbA1M3LUFvV7vTiS-HA7SNyT5Rcr_Sy0DdllYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e23ddb2a.mp4?token=Du7PcXzEi_9LTrLPRHoEd9nBY-tC6iYhvaJKwQvChewKK37hewGxobGES2kM6NrMd7qug8EN6WbUtlywUl9w9BZmqxU6wDk2FkvaXGrtsAv8beIq94WB7H7XcTieZx5OCQyR4t9acGlNXhDDQAyCKMyBIWNGV3qTBm_Dq20KFf8ETtnsGrRcrWx5Ha8ga6oh1WOKoVGEPk7g0LyzoNfdKUTL16txV9pKUM3btTV5M9_mc7xJcKfiZ5rjh1OfxzW-vkr6agU-p-_FJ33lsYUDGBGntBdsGuQgdJxNuKmyJe7FHMZqNmcYPmaWk_nLlg_QKnG8tuG4xpzKjUeOcRBmCjX2fGklxWw361S3KbuDF-G5JTgs6wu_YtoyO1qL3c0UyhczlINMG1wk3oqF0aGXroSQfQhBa_KJql_DEb5WwsfZTBfSAyjy8mnEm0ht116xc7Is2KgtUSYm-gwk44eIoA0SktleR7GkldlK7ulqznAgy4hM0-vN0Zwp87Vh2tECnw4W1I6wtCKFBWYvrceTVZsUvZXM-cK6fNYubYN6zjwEYUn9A3ltJDrxFhGHds-eTMc1eRF2jZuwi7sYiYF0s0XWsSeWMx2AQP9QZ03m9F9hdlpkqOZSzgMx9ZsXH40sOTbe_MbA1M3LUFvV7vTiS-HA7SNyT5Rcr_Sy0DdllYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترکیب زیبایی و ظرافت و تکنولوژی در ماشین؛ ۵۰ سال پیش
🚗
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/692876" target="_blank">📅 13:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHBj8I-4PXxQv8ZLujK268CplhHvPo5iH2MORYhEKBntioW6kY-YS02L9jT35F7vM2DxJ0-F7CSFZwBLguNVTHE-Jt2oTqJ8rHvlvW2pcS0TN4MjRbQnbzUtB0IO01USWELskBL1MrB-LsU4qEvuuxT6ipZi_hNQ-zDFaslnRN2uOuVYL3dAHStrx0z6XWeBAeCRQJUxELXEwQ5FrtGgdjpiFvhPEk_Ey0IOydIzWt7qR32FgT5854c9MdrqFpo81r5Yud57uQSHLyCTA1MUfgFTyZI0EqN_2ApZn18mBkfKusSK5SrucTuvNOJsAf7uJL10Aun1LZ3lE-pw2U8RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احمد ناطق‌نوری، رئیس اسبق فدراسیون بوکس و نماینده پیشین مجلس در ۸۹ سالگی درگذشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/692875" target="_blank">📅 13:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692874">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgZQjCIzKOqxxzXQzFOHxNjqBcqJqvCG6kAsicNbJyvkklQcM1R3kCy5NXJ-2IMMd8sPQcYM7wsuKgKTJrtocXdePCQEMxyZ5psaaL6vQdOZ1YT7fnu-eYw-Qw0i8nWJuctq9tHNNb3XmPsOU9wNziehCutpJzJeMvvcPecNMEQkwVj6SDyjMoy60I-lfRSi_rdyntx114ai5gpl4pUVyRBXzbin3tCoU5iaLWVIEQiEImIH0Y3R1DPzeysFopHyhWtWvXYe2FdjTW29RgilUFXfZWL182Lw2Djdvx5AP4VnML_NMc4wfEmrbMJXCmL3OPOXc7Ago_UF4YhnkIxh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
جمعه‌ها، دل بیشتر هوای آمدنت را می‌کند...
قاب کتیبه «یا صاحب‌الزمان (عج)»؛
یادمانی از انتظار، امید و ارادتی که هر جمعه تازه‌تر می‌شود.
✨
مناسب برای خانه، محل کار یا هدیه‌ای معنوی به دوستداران حضرت ولی‌عصر (عج).
💸
قیمت اصلی: ۲,۱۲۵,۰۰۰ تومان
🔥
قیمت ویژه: ۱,۸۷۵,۰۰۰ تومان
⏳
موجودی محدود
📩
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com
اللهم عجل لولیک الفرج
🤍</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/692874" target="_blank">📅 13:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692873">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
امام جمعه تهران: ترامپ بی‌شعور هنوز به این شعور نرسیده که ملت ایران ملت عاشورایی است
🔹
نطق پزشکیان سازمان ملل را به دادگاهی برای اسرائیل و آمریکا تبدیل کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/692873" target="_blank">📅 13:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692872">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
برنز به تیم بسکتبال ۳ نفره مردان ایران رسید
🔹
تیم بسکتبال ۳به۳ ایران در دیدار رده‌بندی بازی‌های آسیایی موفق شد با نتیجه ۲۱ بر ۱۰ فیلیپین را شکست دهد و به مدال برنز برسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/692872" target="_blank">📅 13:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692871">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dda635642.mp4?token=W4ioXVVHBmVRoGwC-uzZyC3yBjEU5QPHv_eIKNOx0nLu3NTeFXCh2oqxuuZpHsAnwJD_NEYt4rbtdrkqraMhkjqWxhb8T2S_Z2Ri5mNMCj907NhEz5iLyalh5PkrjEcl8LbyLijqtWON7RjUt_wsvy1YDXTExxdpp-GIhHuhG478KEbWAMSJWQ969AtXohhVpVHG93ZDaU_Ctkj-UR9mrJ9IHI1MTkKD6JrVIhfMS6ojTcqHwaHvyP82ttTyErquxFHaH8chzTdGmIOg4FAkzYUoPuiZYETt2MGWB7RDwS1Gg93ypIbLe99ftz8RD7P_KLZX5Np8jEvN-hshMZmwJoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dda635642.mp4?token=W4ioXVVHBmVRoGwC-uzZyC3yBjEU5QPHv_eIKNOx0nLu3NTeFXCh2oqxuuZpHsAnwJD_NEYt4rbtdrkqraMhkjqWxhb8T2S_Z2Ri5mNMCj907NhEz5iLyalh5PkrjEcl8LbyLijqtWON7RjUt_wsvy1YDXTExxdpp-GIhHuhG478KEbWAMSJWQ969AtXohhVpVHG93ZDaU_Ctkj-UR9mrJ9IHI1MTkKD6JrVIhfMS6ojTcqHwaHvyP82ttTyErquxFHaH8chzTdGmIOg4FAkzYUoPuiZYETt2MGWB7RDwS1Gg93ypIbLe99ftz8RD7P_KLZX5Np8jEvN-hshMZmwJoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند دمنوش فوق‌العاده برای سلامتی
🧋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/692871" target="_blank">📅 13:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692870">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ماجرای خانه‌نشینی احمدی‌نژاد از زبان قاضی‌زاده هاشمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/692870" target="_blank">📅 12:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692869">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سخنگوی سپاه پاسداران: در صورت حمله جدید، تسلیحات متفاوتی را به کار می‌گیریم
🔹
شناورهای آمریکایی از محدوده تنگه هرمز ۴۰۰ کیلومتر فاصله گرفته‌اند؛ این یعنی پیروزی بزرگ ایران.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/692869" target="_blank">📅 12:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692868">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0893dbc.mp4?token=T6rowx8kkHqkhKycb_Zq5tyy1p6AkZS3thK7gtszA6F1OyZiIPigA2itf9kVEX-_bYrObi_JgMk1o-FPnQatgGysBnPRLr1ha3tnN9huuAatT-lzklOrhtslWppOk7VGIA_2holk1lCvJy4bFAeRjZicpKHu3breqvgPG4h0vF2SbflbTMA8Rcol7xrtXCJg1DD1iFBgYcUcakDxRgLiCQ-2uIUQQJq868S8KADHTT1kRg7LIg16sAwfOXiOz70r-iHxyK0hRhv5LyTZs-kkJc-3-l2uiJ4ejTHk4uuqFPky70dO8TeKzcB08nJ_p1chrfb8qof5_u0v8VEw52cBag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0893dbc.mp4?token=T6rowx8kkHqkhKycb_Zq5tyy1p6AkZS3thK7gtszA6F1OyZiIPigA2itf9kVEX-_bYrObi_JgMk1o-FPnQatgGysBnPRLr1ha3tnN9huuAatT-lzklOrhtslWppOk7VGIA_2holk1lCvJy4bFAeRjZicpKHu3breqvgPG4h0vF2SbflbTMA8Rcol7xrtXCJg1DD1iFBgYcUcakDxRgLiCQ-2uIUQQJq868S8KADHTT1kRg7LIg16sAwfOXiOz70r-iHxyK0hRhv5LyTZs-kkJc-3-l2uiJ4ejTHk4uuqFPky70dO8TeKzcB08nJ_p1chrfb8qof5_u0v8VEw52cBag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاکلیدی متا، ابزاری مجهز به هوش مصنوعی
🔹
شرکت متا، مالک فیسبوک و اینستاگرام و واتساپ، جاکلیدی مجهز به هوش مصنوعی به نام میوز چارم را معرفی کرد که دارای نمایشگر ۲ اینچی، دوربین، میکروفون و حسگر اثر انگشت و قابلیت 5G‌ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/692868" target="_blank">📅 12:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692867">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33232af0f9.mp4?token=bMXiKAnYYFxTJjPEifIsnTMALCvPtOvJ6eEss4U8r11W85F29tOvYeBfuZVbQgc454jS7gptZz5ajexHhWY_Av6WmVysMTaCyW4ZiVqCPUp6skgtFb3VC1nYn6PheiLFzd-uIBeq3epAlYspy6IgIyiMZf-CakcL5oheyz3HQnWX9VKb-nki4_BSz0p08WWAE44uSjFE-U0R8L9Eoq0O-rGy-v1lPXLw7OqaoC9EchnpkokubAv2u-4YDwvZh4hSfCtUJLqN7OWk_yL9fQqns54U4a2VjYbrD4xYQyPvxP8OTcHktt2dKTFcrUoUO9FK9mCIik13DOyRqZzlqYh3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33232af0f9.mp4?token=bMXiKAnYYFxTJjPEifIsnTMALCvPtOvJ6eEss4U8r11W85F29tOvYeBfuZVbQgc454jS7gptZz5ajexHhWY_Av6WmVysMTaCyW4ZiVqCPUp6skgtFb3VC1nYn6PheiLFzd-uIBeq3epAlYspy6IgIyiMZf-CakcL5oheyz3HQnWX9VKb-nki4_BSz0p08WWAE44uSjFE-U0R8L9Eoq0O-rGy-v1lPXLw7OqaoC9EchnpkokubAv2u-4YDwvZh4hSfCtUJLqN7OWk_yL9fQqns54U4a2VjYbrD4xYQyPvxP8OTcHktt2dKTFcrUoUO9FK9mCIik13DOyRqZzlqYh3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های عجیب رزیتا غفاری در مورد مادرش: زیباترین لحظات زندگیم، لحظات از دنیا رفتن مادرم و پذیرش مرگ او بود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/692867" target="_blank">📅 12:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692865">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f1746d180.mp4?token=l_Xx5iB5DIsBtrJpOsbuGhFo02QokTj21G4aurzwQuZfCTbBPzr5Ewtj2BWXnGnOqVm5sgRm5Gi0lVtb-rVdlNrg4LUdkfiH3Sm-O83T95MMOLVVU3kQsp5sDq1l88ynZtQBGaWQc05YSLMinJnIpKYrZtkGqmAxyVkiMO0oNxfcLU9-dPshCGEVU5ugeyAdPixGnI1G-rhMqJhQ9h1jK-hPcMjIRPbyux5TMS6CsVI0GcX5VgqFaEN44tpmkBvGyZgpcrn0UhIQh8Z_y_2zLWN7gd8_bQ6CPjrIQEKNoJ8aBlNrjAlDqSU0Mg9NR05FVUfdi_UpUBU13MYjHgeQMwPODuopD8HgTQEYNdBasDdFd0G9RfUk27mfTPLwKq21H__o51xncpqWi0HRWN-fUUvrLeT02eEJgZiLkC0W3DejOcri9eCT_CqQLio7T2T40YY1eDjIzhKNT9I0MD5SwHHdm8PF6unJ3gnjv_O8VJnLcMUlVPabCzS-CW_lKxW7zO16dJauK9IKtsdMoAQC875hyaauc1NIALPokyvdXv4pjWpBkjAJabpGTO2Z2N3t25AWWLHbIzyM97GeOKJgvFx39wqM9hJ5ckRz6_CAajmFc_vGDTDPD67iQG3YNiYKkS0-PIbVUYRyP3ef5INZ3_unSRspC9Md3EpwADt8ImY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f1746d180.mp4?token=l_Xx5iB5DIsBtrJpOsbuGhFo02QokTj21G4aurzwQuZfCTbBPzr5Ewtj2BWXnGnOqVm5sgRm5Gi0lVtb-rVdlNrg4LUdkfiH3Sm-O83T95MMOLVVU3kQsp5sDq1l88ynZtQBGaWQc05YSLMinJnIpKYrZtkGqmAxyVkiMO0oNxfcLU9-dPshCGEVU5ugeyAdPixGnI1G-rhMqJhQ9h1jK-hPcMjIRPbyux5TMS6CsVI0GcX5VgqFaEN44tpmkBvGyZgpcrn0UhIQh8Z_y_2zLWN7gd8_bQ6CPjrIQEKNoJ8aBlNrjAlDqSU0Mg9NR05FVUfdi_UpUBU13MYjHgeQMwPODuopD8HgTQEYNdBasDdFd0G9RfUk27mfTPLwKq21H__o51xncpqWi0HRWN-fUUvrLeT02eEJgZiLkC0W3DejOcri9eCT_CqQLio7T2T40YY1eDjIzhKNT9I0MD5SwHHdm8PF6unJ3gnjv_O8VJnLcMUlVPabCzS-CW_lKxW7zO16dJauK9IKtsdMoAQC875hyaauc1NIALPokyvdXv4pjWpBkjAJabpGTO2Z2N3t25AWWLHbIzyM97GeOKJgvFx39wqM9hJ5ckRz6_CAajmFc_vGDTDPD67iQG3YNiYKkS0-PIbVUYRyP3ef5INZ3_unSRspC9Md3EpwADt8ImY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نان رول سیب‌زمینی با پنیر، ترد و خوشمزه
😋
مواد لازم:
🔹
سیب‌زمینی پخته
🔹
پنیر موزارلا
🔹
فلفل قرمز (پودر)
🔹
فلفل سبز
🔹
نمک
🔹
آب لیمو
🔹
نان تست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/692865" target="_blank">📅 12:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692864">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سفارت مالزی در ایران: پرواز مستقیم ایران و مالزی برقرار است و به‌ دنبال بازگشت ایرانی‌ها هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/692864" target="_blank">📅 12:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692862">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNXujUoFw2GBgsHtd527XTIc7Q7yHI3xDk66FAlZiMoHE0uCihPi45mPLzkWD09CtKTxZchnpaJznUamvKxpfsbtXDvx4z8FhkBqhG3DY-3hCSEoFKSsfmEwKkxmOgvdZpv-Ly0wjg2N34RE8M6P8mAHB_OIiKVppWD61NHaGC8LGSgr7t3V9WfTBEMfb-wYWg1j4BgggZpuR4xqwkZH33dRe0hfmkA8w291dj9puJqYZfDIuG0JNLuwQxZbM04F-li1JLskU9RX28VdcCCMC2OmZht8Qu7ZXl45sGpCNVOD-useAdPNJ87IjFDwHRYbxHXlvRbZm-dL2cCeXdz8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری پربازدید از صندلی فرسوده مجمع عمومی سازمان ملل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/692862" target="_blank">📅 12:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692861">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqWWBePmxXny-rkkDxyM3e7nPcGLyu8wy56C9bqJxqz4gMYMIkXL2GWQhhXpsdzW3Ggi5KU_H_2tkMCOWcbrUs12PgSuuWbAvN2yqfZnuNRFAEyLVRMGhMOSFNY71dcx6cNVxWC--a0CfwwIY1GFs0NKr373jJ2O6P_bVzpPV3Jah9pVqdzcCig28KMqn6WpKSFnkb_IlVW-Np1g7f9KusXZA5V-wgkNIy2FgcMraooKq8cDXn8hEz2JXcLK7qJywFeh8dnLTAu3_sHx55fqWRq8Hp8NZYqKMVOj0rYzjz_IiNOjfk4bAsntNLeApx4UrisRPDwXBP_mNMPiw6Q-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔷
دعوت به مشارکت در بررسی چاقی و سبک زندگی
کمتر از ۲ دقیقه از وقت شما می‌تواند به شناخت بهتر نیازهای افراد در مسیر مدیریت وزن و درمان چاقی کمک کند.
از شما دعوت می‌کنیم با تکمیل پرسشنامه «سنجش چاقی و عوامل سبک‌زندگی» در این بررسی مشارکت کنید.
🎯
پاسخ‌های شما کمک می‌کند نیازها و چالش‌های واقعی افراد بهتر شناخته شوند و مسیرهای مؤثرتری برای درمان چاقی طراحی شود.
⏱
زمان تکمیل: کمتر از ۲ دقیقه
برای شرکت در این بررسی، روی لینک زیر بزنید:
👇
https://survey.porsline.ir/s/yNDyEfGR
https://survey.porsline.ir/s/yNDyEfGR</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/692861" target="_blank">📅 12:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692859">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8066ae876a.mp4?token=QQQcfwlLG56wF--PCQSQog0HY-DuHuRENHmMAY5tXMpnW0WoHCKew4qJTkOK_aH7ixb8wSc_ZZ9lZrmlP2vnkE5vRoVkb1XhAh8pUMsNNFWB3gOi774wrQ_MDOa5MOg3Re0gObE-bfKBCD6a1z9I_f79tgT7C8GXBL5VZWWkjj-xKi2yi4yC3uvD399QFw2-tLUya7GL6Gt1td6y5xtlyujTXfmMLqc4U5Hdpw7S4gZlZF08K6hHIEwLjzFIwSRDkWzpCglItbKyFGXT2cVOh1Ip2g4vODcLdOdEI_oKY4hhHM0cV6lH8QfUCHg7xoUBakcjWSmKb0yKHI9BQ3-F2mI8FdpywedXvgju1HMhrFktJzdTkhNjPtv77Y0saIJR4xi6XK5riBQeV6KcQqYjSiQiTtMLDpHx81FIYTHfFTCcoWT5a6NbD2yckQHAoAVkcv0hwFzLgh-DqFsKANMmhUazdpL55i2q09789Dn5HfhvrraDu-9ePUg0H-uDbJjqlLHtsZjMqqSSTJkiYzrm3EE59LDsQf-wpch9rOOGLzM4MqEP7dTXmVR12orXcY4WYGowMtzZb4ZxnyWHy4U2ga4o3Wp0K1lT9tYAP282_Szjl0jSby3wLrY0GomWnL-2qo1PMCRYyt7A0U4E2jMshvSE6ILwTxuAF3umAQsXpdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8066ae876a.mp4?token=QQQcfwlLG56wF--PCQSQog0HY-DuHuRENHmMAY5tXMpnW0WoHCKew4qJTkOK_aH7ixb8wSc_ZZ9lZrmlP2vnkE5vRoVkb1XhAh8pUMsNNFWB3gOi774wrQ_MDOa5MOg3Re0gObE-bfKBCD6a1z9I_f79tgT7C8GXBL5VZWWkjj-xKi2yi4yC3uvD399QFw2-tLUya7GL6Gt1td6y5xtlyujTXfmMLqc4U5Hdpw7S4gZlZF08K6hHIEwLjzFIwSRDkWzpCglItbKyFGXT2cVOh1Ip2g4vODcLdOdEI_oKY4hhHM0cV6lH8QfUCHg7xoUBakcjWSmKb0yKHI9BQ3-F2mI8FdpywedXvgju1HMhrFktJzdTkhNjPtv77Y0saIJR4xi6XK5riBQeV6KcQqYjSiQiTtMLDpHx81FIYTHfFTCcoWT5a6NbD2yckQHAoAVkcv0hwFzLgh-DqFsKANMmhUazdpL55i2q09789Dn5HfhvrraDu-9ePUg0H-uDbJjqlLHtsZjMqqSSTJkiYzrm3EE59LDsQf-wpch9rOOGLzM4MqEP7dTXmVR12orXcY4WYGowMtzZb4ZxnyWHy4U2ga4o3Wp0K1lT9tYAP282_Szjl0jSby3wLrY0GomWnL-2qo1PMCRYyt7A0U4E2jMshvSE6ILwTxuAF3umAQsXpdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیمای ایرانی محدودیت هوایی آمریکا را دور زد
🔹
روز گذشته هواپیمای شرکت وارش به علت محدودیت هواپیمایی کشور واسط برای رسیدن به تاجیکستان یعنی ترکمنستان، مجبور به بازگشت به فرودگاه امام‌خمینی شده بود.
🔹
حالا خلبان این هواپیما در ویدئوی منتشر شده عنوان کرد که با همکاری‌ها و بررسی شرایط، انجام مجدد این پرواز به مقصد تاجیکستان موفقیت آمیز بوده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/692859" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692858">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی نجف در عراق، تمامی پروازهای رفت و برگشت به ایران را، از روز پنجشنبه، ۲۴ سپتامبر، تا اطلاع بعدی، لغو کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/692858" target="_blank">📅 11:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692857">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18d6e2a15.mp4?token=uMOkrjAaYcQ-sal4lesu-sshS8sLcb0E_E7t0dUWawKcaZf8CVkqsb4RX_j72SPHVvNr9ypVaB_nCUEOsaHFBV8Hd2HRZO7i8pgQMcVOCZ6NwtiaeXpKURIErwENwBr5j0DNEYPj3UNKLsLEpB02t3uxaM0Cn3XvLRZlIg3d8vGFSeUFcFy2d2SJo3dGSdTiw9Ia04WylAmTN9KvGHiRvZNFI9WnaWVRE5syFH4XwOgj_MDxoQ81Hx0cEXST07HOIGGhlKRtyJQvljVpNPN2hjBcclGes-vuIS79nFaKduluGRA9FDImFudtITiUnfxK6F_six1b_cY91rqu7311gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18d6e2a15.mp4?token=uMOkrjAaYcQ-sal4lesu-sshS8sLcb0E_E7t0dUWawKcaZf8CVkqsb4RX_j72SPHVvNr9ypVaB_nCUEOsaHFBV8Hd2HRZO7i8pgQMcVOCZ6NwtiaeXpKURIErwENwBr5j0DNEYPj3UNKLsLEpB02t3uxaM0Cn3XvLRZlIg3d8vGFSeUFcFy2d2SJo3dGSdTiw9Ia04WylAmTN9KvGHiRvZNFI9WnaWVRE5syFH4XwOgj_MDxoQ81Hx0cEXST07HOIGGhlKRtyJQvljVpNPN2hjBcclGes-vuIS79nFaKduluGRA9FDImFudtITiUnfxK6F_six1b_cY91rqu7311gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قلعهٔ کَنگِلو؛ عقاب پیر مازندران
⛰
🔹
قلعه‌ای باستانی بر فراز کوه؛ یادگاری از اواخر اشکانی و آغاز ساسانی است که از حمله مغولان جان سالم به‌در برد و بنا بر روایت‌های تاریخی، کارکرد مذهبی زرتشتی نیز داشته است.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/692857" target="_blank">📅 11:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692856">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e294a0242.mp4?token=RxeQc5OP2E5tdZm1Xs_CYxYtaFe6Jqrah2TR1agl9vZiMUUG3GOhGpatXWiFHbIuYBaeaKFVBhtz1UbyzwKuzVOsJPgwwGMgJaC-jQiYVkeoHTcM8wFQ7lXM8hKbx0IBtBYfUlEimBMdHaSac2AfWRbsP5JbzwYVQ0rzgK72FMrrRnWX0Pj6qZ19hGKfG-J4EzPL2E7lCwqEXbw4Lh7qeEAvqrIvX2Ad4Dj4SAMTiahCLOh557jt0eSdaRIDkkUvivxVRY_VZ5n2uQmCFM-dFneG_BQqBXrwO47300-JzJl4Oe9oHpnZ3Q-TUUJ4HoE0xCuI12bzZf212dn1LZGNmIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e294a0242.mp4?token=RxeQc5OP2E5tdZm1Xs_CYxYtaFe6Jqrah2TR1agl9vZiMUUG3GOhGpatXWiFHbIuYBaeaKFVBhtz1UbyzwKuzVOsJPgwwGMgJaC-jQiYVkeoHTcM8wFQ7lXM8hKbx0IBtBYfUlEimBMdHaSac2AfWRbsP5JbzwYVQ0rzgK72FMrrRnWX0Pj6qZ19hGKfG-J4EzPL2E7lCwqEXbw4Lh7qeEAvqrIvX2Ad4Dj4SAMTiahCLOh557jt0eSdaRIDkkUvivxVRY_VZ5n2uQmCFM-dFneG_BQqBXrwO47300-JzJl4Oe9oHpnZ3Q-TUUJ4HoE0xCuI12bzZf212dn1LZGNmIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای عجیب قهرمان کاراته پس از ورود به ایران
مرتضی نعمتی:
🔹
برای گرفتن معافیت، تظاهر به داشتن اختلالات روانی کردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/692856" target="_blank">📅 11:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692855">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a436787d0d.mp4?token=XA9w0VDu28Ke10p6Eedm_82gUv6sincpiBlan1478k1PJJ1l1uNQBg8myMYp_z7Lm-iSLsettqhGN4SldlN3QPhD9003rGJ-w1GZMJbXHUFI4elG5wZkceujWpbr_rnB4BafcdNYxUAjwF1f3oMu5uSS95IYlZMnNxkBC1BJZx14iWueUMxcNtvcC2pUYA70OdEfd3DXdbcgPR0owHo4B072Qran1S6Nwdf76jRwXzbUYvKBgKSwtU6tJTAFOI_7Pi7GWl6veD6uO8sokpjZMjep1kKM1aZDZaJBBJ4CTRAMN31ea2lmM8cWftcP1Pak6I4F5purqy1RWK0EzimwOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a436787d0d.mp4?token=XA9w0VDu28Ke10p6Eedm_82gUv6sincpiBlan1478k1PJJ1l1uNQBg8myMYp_z7Lm-iSLsettqhGN4SldlN3QPhD9003rGJ-w1GZMJbXHUFI4elG5wZkceujWpbr_rnB4BafcdNYxUAjwF1f3oMu5uSS95IYlZMnNxkBC1BJZx14iWueUMxcNtvcC2pUYA70OdEfd3DXdbcgPR0owHo4B072Qran1S6Nwdf76jRwXzbUYvKBgKSwtU6tJTAFOI_7Pi7GWl6veD6uO8sokpjZMjep1kKM1aZDZaJBBJ4CTRAMN31ea2lmM8cWftcP1Pak6I4F5purqy1RWK0EzimwOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: مشتی احمق را برای مذاکره با ایران فرستاده‌ایم!
سناتور آمریکایی:
🔹
ما بخشی از احمق‌ترین آدم‌های موجود را به اتاق مذاکره فرستاده‌ایم. ترامپ باید کمی فروتنی نشان بدهد و بفهمد قرار نیست آن پیروزی بزرگی را که آرزویش را دارد به دست بیاورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/692855" target="_blank">📅 11:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692854">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpmMK5LWM84XJQnpcYe1_GDIMZt5wLJFaVrYc6hjBuorVfWM6Xa3HWKUSSiIyZ_T6dfNUUmqTKVf-_IUZPwUEoHkCqpa38gf4ZnAMJgettBJzNlWnqoky50gBeiCtPICS1zw8WK6gQhS-pnX96_Fi0bdIEq77ON6N59vp_zHIuMiIvaTnzhK7capu1BZjadFauu3Iu8ncDyyN_GiFL_MMRIO07VCg6JH9cpOuB0KrSsvobJLR6_nyWHwUKJ8VI0TKINMr9W5_osQA5ns0l4xnpIFXcW6m8xT2BowfUKQAkTFJkSad3MStAwq5jGG71XhdJzY6X3A3i68_ARqj_Gwxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترند جدید؛ تصویر را برای ChatGPT یا Grok بفرستید و پرامپت زیر را وارد کنید
"Fill the bag with things that resemble me"
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/692854" target="_blank">📅 11:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692853">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS4bkWFZu_ZOE5j_njO8ojFhQ8I-IIly0kPwe9oZ2Y6j7N6q2PGSl06RrzH32zMKWxPdLE0Vpke9ATJ_xJnb1P6NxvFlmxwf3-KGvVsTn09xM3p3vCvPkXMoFNbERZA8Pb918DHfX80-pRf03e9MTdzEZ7Nu1bkgg3lZDfK4GstxQz5LVEmUxP5QppycQtNw5AH4V95fhRJY3gET9PKHU-WgmyJHk5Wz2XfuOxeo0LGqceOdN-LVK5Vl6dgQWRmJw5XRmNmIRhk6zpf8G7y-S1ZTHjmUY1QnBOhjYWUzHIBYYPXzik2cgmbbG-3sOHWy8oRfbg8j_b358u-yPVLWWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند نرخ باروری کل کشور
🔹
بر اساس آمارهای مرکز پژوهش‌های مجلس، نرخ باروری کل در ایران طی سال‌های اخیر روندی نزولی داشته و از ۱.۵۸ فرزند به ازای هر زن در سال ۱۴۰۰، به ۱.۴۴ فرزند در سال ۱۴۰۳ رسیده است.
🔹
این در حالی است که طبق پیش‌بینی برنامه توسعه هفتم، نرخ باروری کشور تا سال ۱۴۰۷ به ۲.۵ فرزند به ازای هر زن افزایش می‌یابد.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/692853" target="_blank">📅 11:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692852">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59fbb714f.mp4?token=ep5zwFGkG6Hk9GR-aaKITVgMDy_OJ047YV-zr2p7GXBJa7yuIVK1D1FhGV54Vj7wqMwv7G5_C4r4om53q1RUXZ39VwCN4HkK5ONJWlUUXc_WlbrdIo_kLayMYY56Gnh26rBJTxUmNEoJGSgBaa_GW88_CqQ_WYmvd7xAeytWgr-XmutDM_U93QMSQEUNo2yKarefG2Y1eAEd-gRaeqSbyDp1WgenD1vydgVq62AKZ_d8IkbOiCa1046oO7iHyYW9NKhBy6uy9psi_YPqkKkOECiYEZ1QZL4IkHl9EUc5FWw40ahZJXKddp_RofaEW_rInwo4FM9Nl5m7tmEzoIMdyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59fbb714f.mp4?token=ep5zwFGkG6Hk9GR-aaKITVgMDy_OJ047YV-zr2p7GXBJa7yuIVK1D1FhGV54Vj7wqMwv7G5_C4r4om53q1RUXZ39VwCN4HkK5ONJWlUUXc_WlbrdIo_kLayMYY56Gnh26rBJTxUmNEoJGSgBaa_GW88_CqQ_WYmvd7xAeytWgr-XmutDM_U93QMSQEUNo2yKarefG2Y1eAEd-gRaeqSbyDp1WgenD1vydgVq62AKZ_d8IkbOiCa1046oO7iHyYW9NKhBy6uy9psi_YPqkKkOECiYEZ1QZL4IkHl9EUc5FWw40ahZJXKddp_RofaEW_rInwo4FM9Nl5m7tmEzoIMdyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعجب مجری شبکه آمریکایی از اعتماد به نفس نماینده ایران موقع سخنرانی تهدید آمیز ترامپ
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/692852" target="_blank">📅 11:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692851">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879dae5f66.mp4?token=v-9-2fzbuGGmGaID0yyBAIEUqb_QfvdDABRHUhX9I-vmRRERxhoQWVzzr3XxiESKG8sXTvQFvbQJ5hrUG19V5ebdDU773tIP_u5LQiQJ0FujA1yR8RRJ_r9FDQS03_QQSH0Sfd3tRDkcU6tcrPbop7tQ2AqaT5NiXolOniotrwUdcCiOUUbmyKvq6d9e96G0u0s9Pb25wyqcT20vxKwKxm5fay6tRLL18MNVgBxlTz7L46FtQvrgJwSq_aRRTQUSPSj9aGRWGEl1x7vkVAOVg0ebn-d9Ff8-VQziMlx4WwLKYe-pWwEO_q5NWpJ-BgcHweY1HZ_Q_8VIWnGD55TIcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879dae5f66.mp4?token=v-9-2fzbuGGmGaID0yyBAIEUqb_QfvdDABRHUhX9I-vmRRERxhoQWVzzr3XxiESKG8sXTvQFvbQJ5hrUG19V5ebdDU773tIP_u5LQiQJ0FujA1yR8RRJ_r9FDQS03_QQSH0Sfd3tRDkcU6tcrPbop7tQ2AqaT5NiXolOniotrwUdcCiOUUbmyKvq6d9e96G0u0s9Pb25wyqcT20vxKwKxm5fay6tRLL18MNVgBxlTz7L46FtQvrgJwSq_aRRTQUSPSj9aGRWGEl1x7vkVAOVg0ebn-d9Ff8-VQziMlx4WwLKYe-pWwEO_q5NWpJ-BgcHweY1HZ_Q_8VIWnGD55TIcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده ایران در سازمان ملل متحد درباره نتانیاهو: سازمان ملل متحد برای حفظ صلح و اجرای عدالت تأسیس شده است، نه اینکه به بستری برای جنایتکاران جنگی تبدیل شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/692851" target="_blank">📅 11:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692849">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b117449cfe.mp4?token=QVm638ANhP8tf0OzPsWziaEoDWx7TU1gNCh-MSlTZryR9-jGcqB2Z420siyGAk8Olu_dtO5tjQbhSFYOa2WAiq0BxDOH_OywcFkL6qrxUDGrfHMk2FhMq8nQe3-iuad4QXhT84eXWHN7IG74fQ4eJJGzKfinMvr-vjgVsK4nH_p9ZIW_E1X9T8Fosg2FlALtdyfZmBx_LNLPHJuXA53JywFLreP2ThuWUkDNzq6wvahpKxSFE_C_VoxzTFFO6sQ_CRGBHxS7y2ylGTwh5fb8yHoYqzXqACKysc6IbI3V3A6plXqJgqjZfWN5hCnnUo7ZxhwFDBHUSOTpdsIqvBT7WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b117449cfe.mp4?token=QVm638ANhP8tf0OzPsWziaEoDWx7TU1gNCh-MSlTZryR9-jGcqB2Z420siyGAk8Olu_dtO5tjQbhSFYOa2WAiq0BxDOH_OywcFkL6qrxUDGrfHMk2FhMq8nQe3-iuad4QXhT84eXWHN7IG74fQ4eJJGzKfinMvr-vjgVsK4nH_p9ZIW_E1X9T8Fosg2FlALtdyfZmBx_LNLPHJuXA53JywFLreP2ThuWUkDNzq6wvahpKxSFE_C_VoxzTFFO6sQ_CRGBHxS7y2ylGTwh5fb8yHoYqzXqACKysc6IbI3V3A6plXqJgqjZfWN5hCnnUo7ZxhwFDBHUSOTpdsIqvBT7WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه باتری آیفون ۱۸ پرومکس و شیائومی ۱۷ پرومکس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/692849" target="_blank">📅 10:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692848">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dfff167.mp4?token=klQ5WwFb1pFdBXiioJdJGtRN7Wuz_RhC3OSlsyzk7r9l4o7L-FWRSeebJnnYIrEkRUFW35NB73GzTgDmGHL9qcrLd7YLbOg1cNTU-C2pOdcXQINlS57T1wYVmsyWDWX8Rlw-pBjCeYOIT85d8bgJK0PWccsYZgPd1cJKu1Wc-aTdjXHZLtuLpu58uJ5JP3cjrH28N9M3rrBSdu2Bpou7-3mcvh6gCOpW4wsvF23OGwmvbKatMpgziyQVA74SBN8c1Sb1-zLILmBqOJevn4ni5J3yr2QQnAwIJbL5glzR9PF6O-_z26uCUPiAsXO1wC9A0sIH2YvgzVWQAMg2fHRQJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dfff167.mp4?token=klQ5WwFb1pFdBXiioJdJGtRN7Wuz_RhC3OSlsyzk7r9l4o7L-FWRSeebJnnYIrEkRUFW35NB73GzTgDmGHL9qcrLd7YLbOg1cNTU-C2pOdcXQINlS57T1wYVmsyWDWX8Rlw-pBjCeYOIT85d8bgJK0PWccsYZgPd1cJKu1Wc-aTdjXHZLtuLpu58uJ5JP3cjrH28N9M3rrBSdu2Bpou7-3mcvh6gCOpW4wsvF23OGwmvbKatMpgziyQVA74SBN8c1Sb1-zLILmBqOJevn4ni5J3yr2QQnAwIJbL5glzR9PF6O-_z26uCUPiAsXO1wC9A0sIH2YvgzVWQAMg2fHRQJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: اردوغان دیکتاتور است/ آخرین کشوری که دروغ‌های یهودی‌ستیزانه منتشر می‌کند، ترکیه است. او می‌خواهد بر سوریه مسلط شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/692848" target="_blank">📅 10:48 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
