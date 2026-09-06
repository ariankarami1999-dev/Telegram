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
<img src="https://cdn4.telesco.pe/file/L0Q1rnirt1lR6QEbjfZjDCq9aA1iQFD32S75Hd2uGRId5ri0zxgRpfd4QuOoePyZ1amM6EEuz8mkmNt0Ket1bd4p_yapk-oU0kqjirMF-ak4U0soLBPM3STg7ip0PyM7SI8rmoiZMGRf0dcSPxEweIMlrSZed4A6ht3YokSKFoerWD79Ix_UWngkVVJAZhtYrYNgqVGbqjEU3ZssIfGO1UOhI7-64eqqMDZOrtfNdthEa8RoErk5IxxjyPzu6QjcOXX5zbJqYXx8LI2XqoGek0lDZNMc9zAA34HYJvbs61xafctF5DcA_DpG0Vz9kKOhpxOW85d1Yh2I9ELeCwgEMQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 448K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 16:29:26</div>
<hr>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">روزهای بسیار حساس در انتظار پرونده هسته‌ای ایران
؛ نشست فصلی شورای حکام آژانس بین‌المللی انرژی اتمی از فردا با حضور نمایندگان ۳۵ کشور برگزار می‌شود و پرونده هسته‌ای ایران یکی از محورهای اصلی آن خواهد بود. آمریکا و سه کشور اروپایی در این نشست چندروزه به دنبال تصویب قطعنامه‌ای برای ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل متحد، به دلیل عدم پایبندی تهران به تعهدات پادمانی خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای هستند
@WarRoom</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/22429" target="_blank">📅 16:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/22428" target="_blank">📅 15:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nguGJjayuI_y0S1UO1ASmUjKNfGU6GquzCrDI-sVSJOfemtGOnxLRJWZnau2_IOab3WxHbNb187OPDebaushMi-oEPHckBGg3k3y9FnHrVVOqpHQXVBCtSl04W_UloIt2TV4RRyDuvYjIZ1N_M2E443Gm07ECRtmCnVqO63rCllIEw1iy9PgMgJJhOO1HxCIxH1DrPSpRTcSpXb5gHhVGuD5mRin0VqPTOkVVvQKNrp2wUIwKOf7a2X8K9OKnr4Vhl10CV12EEqBy29BgNLee5HEkF6F50vSPqGADkWzj4JP0Ydu_-uLT3gnZKmDGWoMtOvBd2W5xi-t3tQd9j3VWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت جوری شده که حتی اوستاد هم نمیتونه تحلیلش کنه
😂
خدایاااا بسته دیگه
@WarRoom</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/withyashar/22427" target="_blank">📅 15:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS9rrTZMFA5MLk6AgaanHJXCVzHSDqIiuIZzhzorElR3g31TZZ_4odAcMWm0GfFJI_MDZKTto5N-kN1FVOyrnnBKBoA4JBeNVUAQUEhTJ6-WurmyMk1JIzTSPdv1ri5auNOCJCCSN7OI2n_alwX7RM8bYufK6TruFXcvfIbTY_lJJeLWMxEquAeAOppE3lQZzkau6tLhkZhp2XHLKJh9qEKK8BPVrTyx1m99L4WQYp931f4Ovpxg21HJgERBdH3ypf0y3pPpLCD7WVczEahb6eX0mjoQy6WNqrZJXLWxEXc9lZx_52JN2P2El2BVKTWCmbLE1hkXyGJUfW6o0KUe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک جت جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در حالی که نیروهای سنتکام همچنان به اجرای
محاصره دریایی علیه ایران ادامه می‌دهند
، بر فراز آب‌های منطقه‌ای گشت‌زنی می‌کند. تا امروز ۱۵ شهریور، نیروهای آمریکایی 92 کشتی تجاری را تغییر مسیر داده‌اند، 3 کشتی را غیرفعال کرده و 2 کشتی را توقیف کرده‌اند تا از رعایت دقیق این قوانین اطمینان حاصل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/22426" target="_blank">📅 15:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">منچ‌ اوسینت : از صبح امروز دست‌کم ۳ نفتکش هنگام تردد در مسیر جنوبی تنگه هرمز، پس از شلیک هشدار نیروی دریایی سپاه، تغییر مسیر داده و برگشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/22425" target="_blank">📅 15:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز:
اوپک‌پلاس امروز در حال بررسی حفظ سیاست فعلی تولید نفت برای ماه اکتبر است و انتظار می‌رود افزایش بیشتر تولید پس از ماه سپتامبر متوقف شود. رویترز می‌گوید
جنگ ایران و اختلال در صادرات نفت از تنگه هرمز
یکی از عوامل مهم این تصمیم است؛ در عین حال اعضای اوپک‌پلاس همچنان پایین‌تر از سهمیه‌های تعیین‌شده تولید می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/22424" target="_blank">📅 14:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرگزاری i24:
ارتش اسرائیل امروز یک رزمایش ناگهانی و چندجبهه‌ای با نام
«Breaking Dawn 2.0»
آغاز کرد. این رزمایش به دستور رئیس ستاد ارتش اسرائیل انجام می‌شود و هدف آن سنجش آمادگی نیروها برای سناریوهای همزمان در چند جبهه و تقویت توان ارتش برای مقابله با تهدیدهای ایران عنوان شده است. پیشتر افشا شد که
ایران در حال آماده‌سازی یک حمله هماهنگ و چندجبهه‌ای علیه اسرائیل
است که از نظر ابعاد و هماهنگی، با حمله ۷ اکتبر مقایسه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/22423" target="_blank">📅 14:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c2c28d2cd.mp4?token=RB2OOQ51UCZ2Deyg0oG01mFX9oIQlWfUaG0l9jjSHMNuVnTFeAYNJzSdv4czkfuGiMgIxKpy6Bms4odzxWmV3G2pLcWf1ovINJRJkt_1FdgnyXOLzT-jmO2N2OgChFxyxrVE0vaB8yGCJNDssl9oTJLzGtnCGVydVMiXimYTsyrm9VikiPMbYBtwsy3H9sUexBgx5jZr6x2Kz08vg1z6TLZbttAgWtASXPothKbdxZNDgWNSSxgumvUZbEbTLk7L725ft-VjpysZOiFBbqzgYueJryMt0SQ7FAPCBtXE31wh9gUbPQhVijZJsui4bi-VHDnnW6ycBvVSCTvgpSSA7ZRb-I4vm67Y4ya8clh0PgpRew8w7Up7zuco1lgvxI8S22zZ0GzsfFLrr8gUp4L4SM9Ng9Tk67czfMyH5-sKNhXhjflCAcOfxWcR4LIoGA2x7Zi7Wilm3bYP-s-HSZfnJM8iSop0M4ke4c1VA8Z6BEQAI1h9I8E9ZS1ahqMjd8ynGWJYv2BY9xvV-_sYXrVvmHCc13IU7tfeSof7HgncHbm-PikiLwOj3kbs8Sb8h272IM8CjvidMU_tdk8xemuJufr8bB0Znwra6WVA5hiOsqEbum4Lmg8Fz6ysa5GbZhN4dWxHis-8GHpJspQTP2eO6v4OlmtwadB5q-DPo9CB9co" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c2c28d2cd.mp4?token=RB2OOQ51UCZ2Deyg0oG01mFX9oIQlWfUaG0l9jjSHMNuVnTFeAYNJzSdv4czkfuGiMgIxKpy6Bms4odzxWmV3G2pLcWf1ovINJRJkt_1FdgnyXOLzT-jmO2N2OgChFxyxrVE0vaB8yGCJNDssl9oTJLzGtnCGVydVMiXimYTsyrm9VikiPMbYBtwsy3H9sUexBgx5jZr6x2Kz08vg1z6TLZbttAgWtASXPothKbdxZNDgWNSSxgumvUZbEbTLk7L725ft-VjpysZOiFBbqzgYueJryMt0SQ7FAPCBtXE31wh9gUbPQhVijZJsui4bi-VHDnnW6ycBvVSCTvgpSSA7ZRb-I4vm67Y4ya8clh0PgpRew8w7Up7zuco1lgvxI8S22zZ0GzsfFLrr8gUp4L4SM9Ng9Tk67czfMyH5-sKNhXhjflCAcOfxWcR4LIoGA2x7Zi7Wilm3bYP-s-HSZfnJM8iSop0M4ke4c1VA8Z6BEQAI1h9I8E9ZS1ahqMjd8ynGWJYv2BY9xvV-_sYXrVvmHCc13IU7tfeSof7HgncHbm-PikiLwOj3kbs8Sb8h272IM8CjvidMU_tdk8xemuJufr8bB0Znwra6WVA5hiOsqEbum4Lmg8Fz6ysa5GbZhN4dWxHis-8GHpJspQTP2eO6v4OlmtwadB5q-DPo9CB9co" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولودیمیر زلنسکی : «روسیه اجازه نداد هیئت آمریکایی با هواپیما وارد اوکراین شود، با وجود اینکه فرودگاه‌های ما برای ورود آن‌ها آماده بودند.»
@WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/22422" target="_blank">📅 14:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گاردین:
لئون پانه‌تا، وزیر دفاع پیشین آمریکا، امروز هشدار داده جنگ ایران ممکن است
شش ماه دیگر نیز ادامه پیدا کند
. او سه مسیر احتمالی برای ترامپ مطرح کرده: عقب‌نشینی، ادامه جنگ فرسایشی و حملات مقطعی، یا تلاش برای به‌دست گرفتن کنترل تنگه هرمز.
@WarRoom</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/22421" target="_blank">📅 14:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e392ac131d.mp4?token=UmAgEoiFk22qQ1bIouowO3o1_URPtSpvkur10QVp3ZsUZH0YaaKcpl6-7LuULbrkhrErPlhYJzIgpoGY5bN3-ppmYC6rCmqcAAJQ5rqQHpXnNtazwyKawd-cYA5eP52LtNTfmXHwUSEH-jDc8_FDzdMeclsFPucbTvGVyMKbgnMq2EDXBNtvJREmQxcTC0k9_4vkuKdlzCMSg4SkCpgIXNjBgRfxFogBlrIL9EBiIV0ebMWHrpr45pVG1Ol-mvXh4W8BsOrqpIG0ItgO69yDy3Rq6Dq13rJQrAl-rPnuWKNe4OfmZmh_qqauv4SyGZEclKh-O7K2bInYB7r86IRy3oUfBbBRdd9eL_qPei9b0bMoJ6RlSewk-8GOKZ_vKlpDXcWUq6lR1XR3ubYv06KgIyL5dSCY1jpAvwmhwJS4rCl9OJJHsssDUnTq-tOLtD6CnowmyBxi6n_Vd83NL39qcInPB0moN0fGmK4IhO0NZLysa0KYbXXqy6TnfW_0dxJzMkVemNfyeRh9gCjYoVgDJA8EfTjmyxjZGiQ7djJmyLyD_rt5W9KJ4Hc9e7iXPhtfNbZglr3FlW04b3RJbFWYpammHGo0BkFbQ5_FNSEPMdyrlxqaic65uyizYq9bRinNaIdfsw5Xx8IxSk4_80vhaiYUStQ1YXk4OVfHhCz-pG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e392ac131d.mp4?token=UmAgEoiFk22qQ1bIouowO3o1_URPtSpvkur10QVp3ZsUZH0YaaKcpl6-7LuULbrkhrErPlhYJzIgpoGY5bN3-ppmYC6rCmqcAAJQ5rqQHpXnNtazwyKawd-cYA5eP52LtNTfmXHwUSEH-jDc8_FDzdMeclsFPucbTvGVyMKbgnMq2EDXBNtvJREmQxcTC0k9_4vkuKdlzCMSg4SkCpgIXNjBgRfxFogBlrIL9EBiIV0ebMWHrpr45pVG1Ol-mvXh4W8BsOrqpIG0ItgO69yDy3Rq6Dq13rJQrAl-rPnuWKNe4OfmZmh_qqauv4SyGZEclKh-O7K2bInYB7r86IRy3oUfBbBRdd9eL_qPei9b0bMoJ6RlSewk-8GOKZ_vKlpDXcWUq6lR1XR3ubYv06KgIyL5dSCY1jpAvwmhwJS4rCl9OJJHsssDUnTq-tOLtD6CnowmyBxi6n_Vd83NL39qcInPB0moN0fGmK4IhO0NZLysa0KYbXXqy6TnfW_0dxJzMkVemNfyeRh9gCjYoVgDJA8EfTjmyxjZGiQ7djJmyLyD_rt5W9KJ4Hc9e7iXPhtfNbZglr3FlW04b3RJbFWYpammHGo0BkFbQ5_FNSEPMdyrlxqaic65uyizYq9bRinNaIdfsw5Xx8IxSk4_80vhaiYUStQ1YXk4OVfHhCz-pG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تفنگداران دریایی و ملوانان ناو آبراهام لینکلن، مشغول عشق و حال در کلابهای  پاتایا، تایلند.
@WarRoom</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/22420" target="_blank">📅 14:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فایننشال تایمز:
آمریکا طی چهار ماه گذشته یک عملیات پرخطر و محرمانه برای مین‌روبی تنگه هرمز انجام داده؛ این عملیات با مشارکت نیروهای ویژه، قایق‌های رباتیک و زیردریایی‌های مجهز به سونار انجام شده است. با وجود اعلام ترامپ درباره پاک‌سازی تنگه، کارشناسان هنوز درباره ایمنی کامل مسیر تردید دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/22419" target="_blank">📅 14:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز:
ایران اعلام کرده نیروهایش یک شناور بدون‌سرنشین آمریکایی را هنگام تلاش برای ورود به تنگه هرمز هدف قرار داده‌اند. آمریکا هنوز این ادعا را تأیید نکرده است. این اتفاق یک روز پس از حمله آمریکا به سه نفتکش ایرانی رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/22418" target="_blank">📅 14:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">افزایش ۲۰ هزار تومانی نرخ دلار  دولتی:
۱۰۰۰ دلار با کارت ملی نرخ ۲۲۰ هزار تومان
@WarRoom</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/22417" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025828335d.mp4?token=rTB-OzzHHNZqJuT0CqtJWk0rnIZkq7maWIhhm_qyzS3iEJ0ytZX8R1tdsvY2ExAEwkXW3aMFJ_uF0gl_PMrWJ-OUZ3PIrtio9fZk9yNKz3bT-SXHMEC9jhj4cQorYW7A80xFVbDlhbvdj99Ent_IaspNm0qn_eEiYE3a6ibgyZG9HtitN18GDa9IOggUm_F6X334H9q92gM4A97YIN3S7aSMJBZpjqvdBvsUgYVJjL7Q84HY5Wu7LbVuLR0TJTOt4aBaSr6t5QOurULZ3UAvFBGuJ4c-sXVGg_Cj_o5V2x5ISXY3I7EGpwcAxqfq_2lwI9ESPmdiVqeI9-Z0m3E7UamrzULNGPv9FfbHX3L81FibtONUCSa7o2TBO1IkXwdrZuZ_BfkOHw0PXQUru5f0yRHHs8hbDB02amQT5LgHMXfCBCH9J4M5m4ZJRu2_s9MJYAtTEUyNJFRkFSTl8HlMV_DCRLexbnloDySYAXL5DGqGmzwjUJAqilQw80krICAoMQi_GgQLmPqWyJGtoVH5K4NchpbHD7piuy6Onp1RKJQEzyJre2KnoZzOBuHo98jFEohqpcoK_oh12CPco35FrBcDAqZ8dVxUevDHjbFSMwOtejsFd6-mrfYtfz-WQPuL70Ahb8WK4si1_nY5QzSOUF4AnfUOEbEXcJfb4oKSS0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025828335d.mp4?token=rTB-OzzHHNZqJuT0CqtJWk0rnIZkq7maWIhhm_qyzS3iEJ0ytZX8R1tdsvY2ExAEwkXW3aMFJ_uF0gl_PMrWJ-OUZ3PIrtio9fZk9yNKz3bT-SXHMEC9jhj4cQorYW7A80xFVbDlhbvdj99Ent_IaspNm0qn_eEiYE3a6ibgyZG9HtitN18GDa9IOggUm_F6X334H9q92gM4A97YIN3S7aSMJBZpjqvdBvsUgYVJjL7Q84HY5Wu7LbVuLR0TJTOt4aBaSr6t5QOurULZ3UAvFBGuJ4c-sXVGg_Cj_o5V2x5ISXY3I7EGpwcAxqfq_2lwI9ESPmdiVqeI9-Z0m3E7UamrzULNGPv9FfbHX3L81FibtONUCSa7o2TBO1IkXwdrZuZ_BfkOHw0PXQUru5f0yRHHs8hbDB02amQT5LgHMXfCBCH9J4M5m4ZJRu2_s9MJYAtTEUyNJFRkFSTl8HlMV_DCRLexbnloDySYAXL5DGqGmzwjUJAqilQw80krICAoMQi_GgQLmPqWyJGtoVH5K4NchpbHD7piuy6Onp1RKJQEzyJre2KnoZzOBuHo98jFEohqpcoK_oh12CPco35FrBcDAqZ8dVxUevDHjbFSMwOtejsFd6-mrfYtfz-WQPuL70Ahb8WK4si1_nY5QzSOUF4AnfUOEbEXcJfb4oKSS0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارگران تایلندی لایه‌هایی از جلبک را از ناو هواپیمابر آبراهام لینکلن پاک کردند این ناو هواپیمابر پس از استقرار طولانی در خاورمیانه، به طور کامل تمیز شد و بازدید خود از بندر لائم چابانگ تایلند را به پایان رساند و به جنوب چین باز میگردد تا در مسیر خود به سمت سن دیگو بازگردد.
@WarRoom</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/22416" target="_blank">📅 13:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وال استریت ژورنال : ‏
در نبرد محاصره، زمان دیگر به نفع جمهوری اسلامی نیست
.‏ ایالات متحده به کشورهای خلیج فارس کمک می‌کند تا مقادیر قابل توجهی نفت را از منطقه خارج کنند و در عین حال مانع از انتقال محموله‌های تهران می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/22415" target="_blank">📅 13:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قشقاوی در گفتگو با الجزیره: جنگ فعلی برای ایران یک جنگ موجودیتی است. ایران درخصوص پاسخ به حملات آمریکا به نفتکش های ایرانی ذره‌ای تردید نخواهد کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/22414" target="_blank">📅 12:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22413">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیویورک‌تایمز: دولت ترامپ در حال بررسی طرحی است که بر اساس آن،
خانواده‌های متأهل با یک والد خانه‌دار
نیز بتوانند از یارانه فدرال مراقبت از کودکان استفاده کنند.
این کمک‌هزینه حدود
۹ هزار دلار به ازای هر کودک در سال
خواهد بود و از یک صندوق فدرال
۱۲ میلیارد دلاری
تأمین می‌شود که در حال حاضر عمدتاً برای کمک به والدین کم‌درآمد جهت کار یا تحصیل استفاده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/22413" target="_blank">📅 12:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بیش از ۵۰ هزار نفر شامگاه پنجشنبه در مراسم مذهبی «سلخوت» در محوطه دیوار غربی (دیوار ندبه؛ بخشی از دیوار حائل محوطه کوه معبد در اورشلیم) گردهم آمدند و به دعا پرداختند. بنیاد میراث دیوار غربی اعلام کرد که از آغاز ماه «اِلول»، بیش از ۵۰۰ هزار نفر در مراسم سلخوت…</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/22412" target="_blank">📅 12:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22411">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم ! @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22411" target="_blank">📅 11:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بسنت: محاصره و تحریم‌ها قدرتمندترین فشار اقتصادی تاریخ علیه ایران است تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز آن را خریداری نکرده، این مقدار به زودی تمام می‌شود و دیگر نفتی نیست که چین بخواهد بخرد @WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22410" target="_blank">📅 10:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بسنت: محاصره و تحریم‌ها قدرتمندترین فشار اقتصادی تاریخ علیه ایران است
تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز آن را خریداری نکرده، این مقدار به زودی تمام می‌شود
و دیگر نفتی نیست که چین بخواهد بخرد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22409" target="_blank">📅 10:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv8k1jyCPVuvmlycsIBfn3fMyFJkaspTuyTwUBfuiyVkNQdEfskFZC2g4MpQYffS7RGYKzlWatwmINjn3M0LQ66Shy_xhp4TmNSgmg7OJgHJiufzv7ztk1v3E8-mu6JpxzZ0JcfiaNFr5d-7HuxEGtZhnpqhOG3Qu0AfgeluHY1CjmACY92vUJ2XWIyO-ONJEMRpQAIVQ6AK9ZWdtz1BvK42e3O18s8cXcvmKMiCAuFLCn8HXNDPILiH9PAYk98cLQGPbP94jKMqpKFQlP5q18bBOdpLUnwzy3nRjCW_YZmnOJPcTEx5YE7ZDa6WsCx3_xVO8znj6omtuofw4bId4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بسیار تأسف‌بار است آنچه در اسپانیا در حال رخ دادن است؛ کشوری که
ه
یچ کنترلی بر
مرزهای
خود ندارد. واو!
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22408" target="_blank">📅 10:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دنیس راس، مذاکره‌کننده و فرستاده پیشین آمریکا در خاورمیانه، هشدار داده است که
احتمال دارد تنش‌ها در خاورمیانه به‌زودی تشدید شود
.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22407" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مارک لوین در واکنشه حمله آمریکا به نفتکش در جزیره خارگ : «در حال نزدیک شدن به مهم‌ترین هدف اقتصادی در ایران؛ منبع مادر ثروت.»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22406" target="_blank">📅 07:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نیویورک‌پست:ارزیابی‌های اطلاعاتی اسرائیل حاکی است ایران با هماهنگی حزب‌الله، حوثی‌ها و شبه‌نظامیان عراقی در حال تدارک حمله‌ای چندجبهه‌ای و مشابه ۷ اکتبر علیه اسرائیل است. به‌گفته جروزالم‌پست، سپاه پاسداران رزمایش مشترک با نیروهای نیابتی و تولید پهپاد و موشک را افزایش داده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22405" target="_blank">📅 06:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مقام اسرائیلی : برای تحویل جسد اعضای حزب الله در تپه علی الطاهر، حزب‌الله باید پول موشک های شلیک شده را بدهند
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22404" target="_blank">📅 06:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آکسیوس: سپاه پاسداران در حملات اخیر خود در مجموع ۶ کشتی را هدف قرار داده است
؛ سه نفتکش و سه کشتی. بر اساس گزارش آکسیوس، سه نفتکش در حال عبور از مسیرهای غیرمجاز یا خارج از مسیر تعیین‌شده در تنگه هرمز هدف حملات موشکی قرار گرفتند و سه شناور آمریکایی نیز هدف حملات ایران قرار گرفتند. در آخرین مورد، ایران موشک‌های بالستیک به سمت دو ناو نیروی دریایی آمریکا شلیک کرد که به گفته سنتکام، یک ناو هواپیمابر و یک ناوشکن مجهز به موشک‌های هدایت‌شونده توانستند از این حملات عبور کنند و آسیبی به نیروهای آمریکایی وارد نشد. در واکنش، نیروهای آمریکایی سه نفتکش ایرانی را هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22403" target="_blank">📅 06:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هم اکنون ۲ پرتاب از سیریک
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22402" target="_blank">📅 00:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ecaf8975.mp4?token=j3ILgDU5H5Lcs3blR_C8WZpWkwaJ8US8yXUZd18lC0vfLi9bgIPf2nHO57rP1XmJd3scFVaYw2PoKgHFklGIekGTt-uX018nhxeXrUwFEZpODjOTuDouRZK2XEAkS1SIFH0IkR1MzrZ8mzCOJsMcs0ZyWVEq28hY2t8u02C06wkRfsu94VLTbkRdnaPd31iA7czTza9beWKa-albWJ9Gh_EuauiIkbf9zSf32CZZtRkbkzUhkXT2HYRvf8xsgtjwpvntWGaKlYGsh05cTg5nIcSBftOhQV6G2MaTlaTVYwSGsfRahreNYOprrCaipzOuU45hNYfPexBavh8x2EetkF4DLW5FAuOspI3U8kIHbUA-g_I2Li6NPwbsxcbPpheCM7gtdcHTMxTDYKeEii6DqsqIRRnF1zWU_B88fTTG0AocJbdGq2SU-h7fMMXmnn-uIy6jiwFNoGwOjrRoVkWOlJUPDcrHSXzyDTy4K5FWAbSmdbcKmBTlqD15J3wnAj_RbiOh3uQNxHD-9tGMrLHH2pjsaXSFoOeYfbkdgF1M-OKXELXzwVQw-QWfsl9gAuI--Lc_wC93o0UxCe64YOL6kZBx6HxSMayVW3cGHpdavhRCb-diBeZh2pre-CajHknlYUADKDHiaxKeiKb43PnaZg-1ZWEdENPrjGgDwLwI-pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ecaf8975.mp4?token=j3ILgDU5H5Lcs3blR_C8WZpWkwaJ8US8yXUZd18lC0vfLi9bgIPf2nHO57rP1XmJd3scFVaYw2PoKgHFklGIekGTt-uX018nhxeXrUwFEZpODjOTuDouRZK2XEAkS1SIFH0IkR1MzrZ8mzCOJsMcs0ZyWVEq28hY2t8u02C06wkRfsu94VLTbkRdnaPd31iA7czTza9beWKa-albWJ9Gh_EuauiIkbf9zSf32CZZtRkbkzUhkXT2HYRvf8xsgtjwpvntWGaKlYGsh05cTg5nIcSBftOhQV6G2MaTlaTVYwSGsfRahreNYOprrCaipzOuU45hNYfPexBavh8x2EetkF4DLW5FAuOspI3U8kIHbUA-g_I2Li6NPwbsxcbPpheCM7gtdcHTMxTDYKeEii6DqsqIRRnF1zWU_B88fTTG0AocJbdGq2SU-h7fMMXmnn-uIy6jiwFNoGwOjrRoVkWOlJUPDcrHSXzyDTy4K5FWAbSmdbcKmBTlqD15J3wnAj_RbiOh3uQNxHD-9tGMrLHH2pjsaXSFoOeYfbkdgF1M-OKXELXzwVQw-QWfsl9gAuI--Lc_wC93o0UxCe64YOL6kZBx6HxSMayVW3cGHpdavhRCb-diBeZh2pre-CajHknlYUADKDHiaxKeiKb43PnaZg-1ZWEdENPrjGgDwLwI-pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سه پا : آبرومون امروز رفت فعلا این
تصاویر منتشر نشده از رصد و اقدام علیه شناور های متخلف
رو ببینید
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22401" target="_blank">📅 00:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec62b949f8.mp4?token=hgGyPs9QXFXWJwQm2bNpD5OaAhrFX4rXWdt0Ufqv9Q3SwPCWZcP40PfMxGYYiK1rL3RZDrGCVLWEhhtJ3VUpdWKW5x9_m-ucejak4AsLgna4toHfAHqJ30Bk9uyBvm1A3c45iacww9LzUtmpzKivCBHCh5AHQ1FdZo-Q01WAPZB2bVWSxVywFu2_yBNTTY7rwmJ5OYGiTQRL9aqi6aIJxevJxpePHG9kxbvzEXsDkvlVwm1s5rfpS2ml6FrCyHKjxcV2N5Cy3htHbPCdGSOSuro6tAF5VE_g9XX-PHbMI9lRk-YKAgj5kF7dhVSzoLPMPE73GQF3RHVWKUVLVrJl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec62b949f8.mp4?token=hgGyPs9QXFXWJwQm2bNpD5OaAhrFX4rXWdt0Ufqv9Q3SwPCWZcP40PfMxGYYiK1rL3RZDrGCVLWEhhtJ3VUpdWKW5x9_m-ucejak4AsLgna4toHfAHqJ30Bk9uyBvm1A3c45iacww9LzUtmpzKivCBHCh5AHQ1FdZo-Q01WAPZB2bVWSxVywFu2_yBNTTY7rwmJ5OYGiTQRL9aqi6aIJxevJxpePHG9kxbvzEXsDkvlVwm1s5rfpS2ml6FrCyHKjxcV2N5Cy3htHbPCdGSOSuro6tAF5VE_g9XX-PHbMI9lRk-YKAgj5kF7dhVSzoLPMPE73GQF3RHVWKUVLVrJl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیران آمریکایی، ویتکاف و کوشنر، پس از سه ساعت مذاکره با پوتین، کاخ کرملین را ترک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22400" target="_blank">📅 00:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رسانه های رژیم : تمامی افرادی که در کلیپ رژه طرفداران سازمان تروریستی مجاهدین خلق در کوچه پس کوچه های‌کرج، حضور داشته‌اند، توسط نیروهای امنیتی شناسایی و دستگیر شدند
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22399" target="_blank">📅 00:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رئیس اداره اخبار مجلس:
۵۰ روز است که یه بشکه نفت هم نفروختیم.
هیچ کالایی هم از جنوب وارد کشور نشده‌. محاصره اقتصادی بدجور دستمونو بسته.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22398" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">زاکانی: وصیت نامه آقا با خودش تو بمبارون از بین رفته
@WarRoom
😁</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22397" target="_blank">📅 23:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نتانیاهو: «اگر ما علیه ایران اقدام نمی‌کردیم، ایران امروز بمب‌های اتمی داشت که قصد نابودی ما را داشتند.
حالا آنها دوباره تلاش خواهند کرد. آنها دوباره تلاش می‌کنند و دوباره تلاش خواهند کرد تا محوری را که ما شکستیم، بازسازی کنند.»
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22396" target="_blank">📅 23:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قالیباف : بستن تنگه هرمز به ضرر ایران شد.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/22395" target="_blank">📅 23:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پرتاب۳ موشک از سیریک سمت تنگه ( رادار ندارن موش کور شدن ول میدن )
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22394" target="_blank">📅 22:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صدای انفجار از تنگه ، امشب تنگه گیسو گیس کشیه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22393" target="_blank">📅 22:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22392">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : آنچه سنتکام امروز ، تأیید کرده این است که سپاه پاسداران به سمت
دو ناو آمریکایی
موشک بالستیک شلیک کرده و سنتکام هم می‌گوید
ناو هواپیمابر و یک ناوشکن
موشک‌ها را جاخالی داده‌اند و هیچ نیروی آمریکایی آسیب ندیده است. در واکنش، آمریکا به سه نفتکش ایرانی حمله کرده است. بنابراین رسانه های زرد که به دروغ نوشته‌اند
«جورج واشنگتن به‌دلیل موشک‌های ایرانی عقب‌نشینی کرد»
، اصلا در خبر رسمی
نیامده
کدام ناو بوش یا واشنگتن
وبعد هم اگر
تغییر موقعیت عملیاتی یا دور شدن تاکتیکی ناو از محدوده خطر
انجام شود هم نرمال است ولی سنتکام چیزی‌نگفته است که ناو منطقه را ترک کرده یا به‌دلیل اصابت/ترس از موشک‌ها عقب‌نشینی کرده باشد !!!
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22392" target="_blank">📅 22:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عضو هیئت‌رئیسه مجلس : هم اکنون احتمال حمله به اسرائیل هم وجود دارد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22391" target="_blank">📅 22:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22390" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اتاق جنگ با یاشار با افتخار عرزشی سوز ترین چنل تلگرام
🙌🏾
😁
💥
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22389" target="_blank">📅 21:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromUTA</strong></div>
<div class="tg-text">یاشار  ناموسا سگ میرینه بهت؟</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22388" target="_blank">📅 21:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=jLL_5lvIugp-A-DVdXsMNXL3NOLQrpje5vqg5QKf1hyq1hQoVRd2NniNwV_nBvMKfcnOkNg_SX4ggooIGNuDkSvlB4tayadk6rXyY-lDbEILNwbmcY98lZX7IK84S15FmOCNBpzTyMh_Z23att75yZdUUTwX_5bZxvXza5azeP8o8RX6drNz4_nO6zSPaBhQJYxg_P3yKOyvPjuern-NPEoZrmM74ZwWHKTBfhG9gnsR7hh1z7mj-bDxVMv1Ct0I-NACuYloSdWdsd6wkg2V_41vTi1WkYPhtWeynsdgI-FdACxccM8Y4QQMiP_RkmL548R4Bk94220iset7ZFsq3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=jLL_5lvIugp-A-DVdXsMNXL3NOLQrpje5vqg5QKf1hyq1hQoVRd2NniNwV_nBvMKfcnOkNg_SX4ggooIGNuDkSvlB4tayadk6rXyY-lDbEILNwbmcY98lZX7IK84S15FmOCNBpzTyMh_Z23att75yZdUUTwX_5bZxvXza5azeP8o8RX6drNz4_nO6zSPaBhQJYxg_P3yKOyvPjuern-NPEoZrmM74ZwWHKTBfhG9gnsR7hh1z7mj-bDxVMv1Ct0I-NACuYloSdWdsd6wkg2V_41vTi1WkYPhtWeynsdgI-FdACxccM8Y4QQMiP_RkmL548R4Bk94220iset7ZFsq3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom
تنبیه</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22387" target="_blank">📅 21:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش ۲ انفجار جدید جاسک رأس ساعت ۸ @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22386" target="_blank">📅 21:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قرارگاه خاتم‌ :جون مادرتون نزنین
قرارگاه مرکزی خاتم‌الانبیا: به ارتش آمریکا هشدار داده می‌شود که در صورت ادامه اقدامات خصمانه، ایجاد ناامنی، مزاحمت برای کشتی‌های ایرانی و محاصره دریایی ایران، ضربات نیروهای مسلح جمهوری اسلامی علیه شناورهای نظامی آمریکا در منطقه شدیدتر از گذشته خواهد بود و امکان گسترش دامنه آن نیز وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22385" target="_blank">📅 21:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d6f60dbf.mp4?token=oEBsibjpivk-6BoGT0J0EWzeGtVPwJiia1dMCGM1DYQpeCr5cJ9f7FwqNIPnoPk23VNGUcKo5Vi9Ij1uJdA8o_o31OJp442OCKTVkVb7Ktyi90zZSH840_qFWpkU7oOtaa-JERZYoJsWir8v29Z7QYPZ3FF6fDOr1D1-JNryRXLUK9_fUxGxfpIrI_-g6iVpB9UXuquOH1nNVPsO2McqzoSBlp73bpQZ3bffVduyGh8N-VtHph3o7ZXMl-i1942784l2DHGvveP-tzWKN8cCeuExmaw1kIDhUSDcfjAYw2GoE3tvaFe6VNcLOsmjBdqlGsp8x83zUBOxq9Ew9eisFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d6f60dbf.mp4?token=oEBsibjpivk-6BoGT0J0EWzeGtVPwJiia1dMCGM1DYQpeCr5cJ9f7FwqNIPnoPk23VNGUcKo5Vi9Ij1uJdA8o_o31OJp442OCKTVkVb7Ktyi90zZSH840_qFWpkU7oOtaa-JERZYoJsWir8v29Z7QYPZ3FF6fDOr1D1-JNryRXLUK9_fUxGxfpIrI_-g6iVpB9UXuquOH1nNVPsO2McqzoSBlp73bpQZ3bffVduyGh8N-VtHph3o7ZXMl-i1942784l2DHGvveP-tzWKN8cCeuExmaw1kIDhUSDcfjAYw2GoE3tvaFe6VNcLOsmjBdqlGsp8x83zUBOxq9Ew9eisFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین، نشست خود را با ویتکوف و کوشنر، نماینده ویژه ایالات متحده، آغاز کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22384" target="_blank">📅 20:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q20vxzodiO27jBFdRbTxv7AUG-aa1yaxWgPoDB4HGKdrpKEBKKiDWRIxbhJyLHwB1-o-E9uFwfbxRLmkcHh3cR8jWg31ykqBh93-dBqO-_928bDKGd92kEO24t5aLnzknwtRWAgiq8YktlCOFDtDr5hJ0rFPPo3yxd4qzOPDVOE5XCcky_K-SjIsTixg8BSOoDqTV5gRYJ9Q2noj5m_q-uYkPR0s8AKczgGVg4hecmRnVLAIkdh4D9PLgAmxsR8Ftf4BfkoXf-fQJwtXBpzl4gZKccs7czhcMpRY9fIFzLl0_GrzaBfH79YU9swJArjZd3Za6mfyLmLJDfXZlAkx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78ca28583e.mp4?token=nY7EBd0_wRUpTFDiB8a2LHNCbt7xo_r3caF8lwYkfAUC2lxBwFgxZ5vwYPPeZa1y8m3evSr_-h0HKPwStT66nx9htDDCFj9bLuifNGOA_GcgbfyvzvAtGsYlnMJYuRVsRePNbvtEkxAPoiuU8C0DXouGjGHvvyXxdVvvjFxNJWWsbOd6PNSD3TyxXTGtlaBEuBmdkkK55AK2QC9S7nRjQDw_QPXrUcjttbRjQmd8-yStGKNntg5rQ-D9JsoVp5Jj1q9WlX3Ao3jb0uCdilJJrNUEGVffLURqUq--T7aAGBVMswFNiwyoY2b2Ybi9Az0VkDnQj0ujS4U_9DcQBLf39w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78ca28583e.mp4?token=nY7EBd0_wRUpTFDiB8a2LHNCbt7xo_r3caF8lwYkfAUC2lxBwFgxZ5vwYPPeZa1y8m3evSr_-h0HKPwStT66nx9htDDCFj9bLuifNGOA_GcgbfyvzvAtGsYlnMJYuRVsRePNbvtEkxAPoiuU8C0DXouGjGHvvyXxdVvvjFxNJWWsbOd6PNSD3TyxXTGtlaBEuBmdkkK55AK2QC9S7nRjQDw_QPXrUcjttbRjQmd8-yStGKNntg5rQ-D9JsoVp5Jj1q9WlX3Ao3jb0uCdilJJrNUEGVffLURqUq--T7aAGBVMswFNiwyoY2b2Ybi9Az0VkDnQj0ujS4U_9DcQBLf39w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7 نفر زنده زنده سوختن و جونشون رو از دست دادن...
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22382" target="_blank">📅 20:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارش صدای دو انفجار قشم از سمت تنگه ، ۲۰:۰۷ دقیقه
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22381" target="_blank">📅 20:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اتاق جنگ با یاشار : با وجود ادامه درگیری ایران و آمریکا ولی هم‌زمانی با
مذاکرات صلح روسیه و اوکراین و آتش‌بس سه‌روزه میان دو طرف، بیت‌کوین هم‌اکنون از ۸۰ هزار دلار عبور کرده است.
در صورت موفقیت مذاکرات و اعلام پایان جنگ روسیه و اوکراین، کاهش ریسک‌های ژئوپلیتیکی و افزایش اشتهای سرمایه‌گذاران برای دارایی‌های پرریسک می‌تواند موج تازه‌ای در بازار ایجاد کند؛ به‌گونه‌ای که
عبور بیت‌کوین از ۱۰۰ هزار دلار نیز می‌تواند به یکی از سناریوهای جدی بازار تبدیل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22380" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83eb31b467.mp4?token=huP5Nek7rdAnw1t0hQAI0WNxqmXga5YCNLD1oPcMMFmYMwnWEV9yNEBKDUSEAMJ1vCj3j6-aOsT41OX4YPDDoJfdE4XgLeJZZci9QhOmZlq9ZN0SPA2hWehP3lF8s2kG08tx5xIQM1lG8nFtw9au1nW_NplWlgKPr5YbwjD4Em59ny4TCrmO7-SmFRdDwuc0N1G5XkKGRKd7BW9P2SaMwkYk6UIp7Qb02Xf8O4a9L1prmfj7xZ-4HnsoIc1C4MEIf5qeNofe-tjGM7ZH949fmsCcN9teuloSFQD5CW7sD4fRET_irC3HzPEgPRzq6dpB9Z_MCQ24heRYLLJUz2zVFzAyEJl22kxCA4fe79LkDIHwvwdJC8gJ0sqaEkjOrnTHI72-Bm8c2oIVncSE6MRZYrDO3MipHgzourgNIQRTnjE4vcl563wmlg4c4rglpCjH6T12Lw37TbafkRjpKg8AjmLlwqskIzGbsmK1RD34DX5-mvR6iXSSG7GrOoO49yMJT2pklvMhSeIt5Q2TL4rkw_zhW3okDuy402ul7YLLlrP2U70ZfOeP3OPFlfvVJQB9NwmGx6xErPGL2B4Cab4mn4DGsAk10LxNX9alDvrL3j-Ucp3zfhv4BHx3Hl7GNJD-eMuoST5gsHXXzme_L0m9M49e4NXjedgTPoOhhSQEXE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83eb31b467.mp4?token=huP5Nek7rdAnw1t0hQAI0WNxqmXga5YCNLD1oPcMMFmYMwnWEV9yNEBKDUSEAMJ1vCj3j6-aOsT41OX4YPDDoJfdE4XgLeJZZci9QhOmZlq9ZN0SPA2hWehP3lF8s2kG08tx5xIQM1lG8nFtw9au1nW_NplWlgKPr5YbwjD4Em59ny4TCrmO7-SmFRdDwuc0N1G5XkKGRKd7BW9P2SaMwkYk6UIp7Qb02Xf8O4a9L1prmfj7xZ-4HnsoIc1C4MEIf5qeNofe-tjGM7ZH949fmsCcN9teuloSFQD5CW7sD4fRET_irC3HzPEgPRzq6dpB9Z_MCQ24heRYLLJUz2zVFzAyEJl22kxCA4fe79LkDIHwvwdJC8gJ0sqaEkjOrnTHI72-Bm8c2oIVncSE6MRZYrDO3MipHgzourgNIQRTnjE4vcl563wmlg4c4rglpCjH6T12Lw37TbafkRjpKg8AjmLlwqskIzGbsmK1RD34DX5-mvR6iXSSG7GrOoO49yMJT2pklvMhSeIt5Q2TL4rkw_zhW3okDuy402ul7YLLlrP2U70ZfOeP3OPFlfvVJQB9NwmGx6xErPGL2B4Cab4mn4DGsAk10LxNX9alDvrL3j-Ucp3zfhv4BHx3Hl7GNJD-eMuoST5gsHXXzme_L0m9M49e4NXjedgTPoOhhSQEXE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ویدیویی که امروز از بنیامین نتانیاهو در شبکه‌های اجتماعی منتشر شده، در واقع مربوط به
سال ۲۰۲۰ و دوران کرونا
است. نتانیاهو در این موزیک‌ویدیو در کنار
عدن بن زِکِن (Eden Ben Zaken)
، خواننده مشهور اسرائیلی، آهنگ
«یش بی آهاوا» (Yesh Bi Ahava)
را اجرا می‌کند. این ویدیو با هدف
جمع‌آوری کمک برای سالمندان نیازمند و مقابله با تنهایی آنها در دوران قرنطینه کرونا
منتشر شده بود.
@WarRoom
😁
یاشار : باید یه فیت باهاش بدم بعد از جنگ</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22379" target="_blank">📅 20:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22378">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش ۲ انفجار جدید جاسک رأس ساعت ۸
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22378" target="_blank">📅 20:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم ! @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22377" target="_blank">📅 20:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سخنگوی سابق مجلس: پیش نویس قطعنامه جدید آژانس، کد رمز برای حمله مجدد به مراکز هسته ای ایران است. ترامپ اعلام کرد ممکن است خیلی زود به کوه کلنگ حمله کنیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22376" target="_blank">📅 19:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر جنگ آمریکا: اگر ایران به کشتی‌های آمریکایی شلیک کند، ما ناوگان حامل نفت ایران را که فاقد تجهیزات دفاعی است، نابود خواهیم کرد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22375" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph-Zj6Ju-GslI6ixnrcblYm19RAHQc_Etu3qNfI1G0tOirOYEFygBNtI9cLp76zGQ5ZFjGzSPJlCzAk7W6siAqY3eqBMebtEYPzjXfaRV_xJ9G7fzAeAyCM9phEoD3M9ebxVqExp7NKysO16Q1pE5gQVbe6baXamoUmXfbYFk_aDGyUw7N58bbrmDKsmB7LG8Z49Z_mJRk_t7W_vaj1j4R4qIWixraXhzr1gv4qp4r-3Qf9VXaKDA8erfWEfupDG8kNxosKz30gmNAcTeAbhFE_4JpYykySyNOMErCDHb4zMSi8NyuTdVA5ObLU6u5fstCoAw6lyQCJHa5n9w8AEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای سنتکام نفتکش M/T Downy در نزدیکی جزیره خارگ و نفتکش M/T Stark 1 در نزدیکی جاسک را به‌طور دائمی از کار انداختند. همچنین نیروهای آمریکایی نفتکش خالی M/T Kylo، معروف به «Noxen»، را در دریای عمان به‌طور کامل منهدم کردند؛ این نفتکش پس از آن هدف قرار گرفت…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22374" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اتاق جنگ با یاشار : در عملیات‌های طولانی بر فراز خلیج فارس، به‌ویژه در مأموریت‌های مرتبط با ایران، استفاده از هواپیماهای سوخت‌رسان اهمیت زیادی دارد؛ زیرا جنگنده‌ها می‌توانند بدون بازگشت به پایگاه، با
سوخت‌گیری هوایی ساعت‌ها در منطقه عملیاتی باقی بمانند
. این روش علاوه بر افزایش زمان ماندگاری در آسمان، نیاز به فرود و برخاست مجدد را کاهش می‌دهد؛ چرخه‌هایی که فشار قابل‌توجهی بر سازه و ارابه فرود هواپیما وارد می‌کنند. همچنین بازگشت مکرر به پایگاه‌های منطقه‌ای می‌تواند زمان‌بر و پرریسک باشد؛ به‌ویژه در شرایطی که
موقعیت پایگاه‌های مورد استفاده افشا شود و این پایگاه‌ها در معرض حملات موشکی و پهپادی قرار بگیرند
. از طرفی، جنگنده با سوخت‌گیری هوایی وابستگی کمتری به یک پایگاه مشخص دارد و می‌تواند
مسیر و مدت مأموریت خود را با توجه به شرایط لحظه‌ای تغییر دهد
. به همین دلیل، تانکرهای سوخت‌رسان نقش مهمی در حفظ
حضور مستمر، انعطاف‌پذیر و ایمن‌تر جنگنده‌ها در منطقه
دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22373" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیروهای سنتکام نفتکش M/T Downy در نزدیکی جزیره خارگ و نفتکش M/T Stark 1 در نزدیکی جاسک را به‌طور دائمی از کار انداختند. همچنین نیروهای آمریکایی نفتکش خالی M/T Kylo، معروف به «Noxen»، را در دریای عمان به‌طور کامل منهدم کردند؛ این نفتکش پس از آن هدف قرار گرفت…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22372" target="_blank">📅 18:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22371">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ql79ia_QSa7McTr0WtpY3pGyOgX0dGZI5n8CKdIzaHv2iHzpkjlQ7rwC5DPtlMWLH4XRtHrnj_XstMFoRgl27vt1eg1Q1ufYA0zRjO7NT8a6-fnsRmxhEOscIw5202BxgDfCS8MVOsN8SuwixKNSxosRrBYz2_9cv-s_cWh54rNB4l7h6UyY_49BR0tQnU3JSiZ3iYqNBgHjQUlGpHEfU86_iJ_0j7liOns_SecxkMj-FiD89iWzUOKeKRVbNPuPpYDkMKE1A14j7ZR7nnIrAjkpr79daxoZiHdyvo8-YGWgumN_Av9AfHjNGh7T401S9IY4IP6uO3ZfZhnnbrmrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم ! @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22371" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ززززدن گزارش های زیاد از صدای انفجار جدید از خارگ و جاسک
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22370" target="_blank">📅 18:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم !
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22369" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیروی هوایی آمریکا به خدمه کشتی ایرانی ۳ دقیقه وقت خروج داد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22368" target="_blank">📅 18:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c9c110ff.mp4?token=Esxf7pyTqLkMJP2Vq5syg5NFZ0yT0Tv-aTJines_ZG3b6VCzEqOZm7xcKqmEXTx_RbxnJv_804hkVPkIHNpyg5KwHOJEoTzIv8Qi1TGmYjCzcspeQ5ShKBlYbBHf7LlWjgXEqbyhBSsUa8d7RA_lHnYeOdmbNvACrwTbC8bkHAPm3A3ElPC92yMK7RQxGyzYxvTEJPON13n1lc3dD5duUkSvZPLghoCxJJ8Z3ZqVeJXYAywl5iMHBEYhqroonVRulqHC2C7zGp4c8-G5o4SIVgsBI-v7AtyGp61m2pWPrK0SU27AtKa38KSOBXWX7TuX5s30oTgTcJoyC_uZbQgroRdSzlEQdN1xx6ws4SlktiQ61AKoW7Ib6hZxevB9svbZ35FGqsMAD2q3T4FUzXn2v3fmxxL4XEyjV1zA9ZsFfywnEGAy-iRx9xbT5ZXtC4SqsJtMNkz7aNyHaUODmw150smcRXs24VpcuYieFAb_mgCa4vuGnol1Kg1B9oEr7gPsNFRC-ouiNcGht40Zf9oSvAY0vfPgf1pYPdzDO4PylMUI_PTkqmGB8JafhcXhzrhCl9HcvGq_DxKBS9ibm0QNpGdseWYtFE4aGN_mnXDZ_pYCrLcZ3Io0TQxaMJGqU7bOsxZEERuE2gF84kfIeOBN5wQITkHGp40VkDrefLNAS8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c9c110ff.mp4?token=Esxf7pyTqLkMJP2Vq5syg5NFZ0yT0Tv-aTJines_ZG3b6VCzEqOZm7xcKqmEXTx_RbxnJv_804hkVPkIHNpyg5KwHOJEoTzIv8Qi1TGmYjCzcspeQ5ShKBlYbBHf7LlWjgXEqbyhBSsUa8d7RA_lHnYeOdmbNvACrwTbC8bkHAPm3A3ElPC92yMK7RQxGyzYxvTEJPON13n1lc3dD5duUkSvZPLghoCxJJ8Z3ZqVeJXYAywl5iMHBEYhqroonVRulqHC2C7zGp4c8-G5o4SIVgsBI-v7AtyGp61m2pWPrK0SU27AtKa38KSOBXWX7TuX5s30oTgTcJoyC_uZbQgroRdSzlEQdN1xx6ws4SlktiQ61AKoW7Ib6hZxevB9svbZ35FGqsMAD2q3T4FUzXn2v3fmxxL4XEyjV1zA9ZsFfywnEGAy-iRx9xbT5ZXtC4SqsJtMNkz7aNyHaUODmw150smcRXs24VpcuYieFAb_mgCa4vuGnol1Kg1B9oEr7gPsNFRC-ouiNcGht40Zf9oSvAY0vfPgf1pYPdzDO4PylMUI_PTkqmGB8JafhcXhzrhCl9HcvGq_DxKBS9ibm0QNpGdseWYtFE4aGN_mnXDZ_pYCrLcZ3Io0TQxaMJGqU7bOsxZEERuE2gF84kfIeOBN5wQITkHGp40VkDrefLNAS8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستون دود اتوبان آزادگان
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22367" target="_blank">📅 18:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM-aawi2xQL1VLqc3N6K3mTCW0Xu9M5WCSxgdlv54BQioC-xrF0f6beEH_WdYAGYt9gQd4SrqqqzJBYNzYOuVwYOKcVgJt5kWOtJrs6eRhfVYjRvtQvesCcWrF1Ujleb5jf7qq5eG5CbHHDliH7-1nqHh4R9NZU6yg3EpvLjSyNze0iJ2uYwazIol3jo56Bj0lNnjOn2FsgHDvButuKvuuqk5Tvw5PCKgLmCP9TGOZllDaNb71B_lPBRfjNz6MOkTW0RuZVh5H4x404z3e3Z9YE0S_ejujH1Kfxs-kxzMfv7PDoQqCJCoeOf3n1TzSLEVh5k8KVT909e0UNucqeuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز:
روسیه از سال ۲۰۲۳ در قالب برنامه محرمانه
C430L
به ایران برای توسعه موشک‌های کروز مافوق صوت کمک کرده است؛ تحقیقات این روزنامه بر پایه مکاتبات افشاشده روسیه، سوابق سفر متخصصان و اسناد ثبت اختراع نظامی نشان می‌دهد کارشناسان موشکی روسیه در توسعه
پیشران رم‌جت
به ایران کمک کرده‌اند؛ فناوری‌ای که می‌تواند موشک را با سرعت چند برابر صوت به پرواز درآورد و برای موشک‌های ضدکشتی و حمله به اهداف زمینی به کار رود. این همکاری حتی در جریان جنگ آمریکا و اسرائیل با ایران در سال ۲۰۲۶ نیز ادامه داشته و در صورت تکمیل، می‌تواند توان ایران برای تهدید ناوهای هواپیمابر و دیگر شناورهای جنگی آمریکا در منطقه را افزایش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22366" target="_blank">📅 18:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22365">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش صدای انفجار جدید جاسک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22365" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سفارت آمریکا در بحرین: آمریکایی‌هایی که در حال حاضر در خاورمیانه هستند باید نهایت احتیاط را رعایت کنند و از احتمال لغو پروازها، بسته شدن حریم هوایی و اختلالات سفر آگاه باشند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22364" target="_blank">📅 17:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دریاسالار
برد کوپر، فرمانده سنتکام
، گفت: پیام ما به سپاه پاسداران باید روشن باشد:
اگر به دو کشتی ما شلیک کنید، ما هزینه اقتصادی بسیار سنگین‌تری به شما تحمیل خواهیم کرد؛ با از کار انداختن سه کشتی شما.
ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم،
ناوگان محدود و آسیب‌پذیر نفتکش‌های ایران را منهدم خواهیم کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22363" target="_blank">📅 17:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967738cda4.mp4?token=reocLdGFVJ2jBhB_cm1gUS25rBKGAEu6EMdJuB9uyexVZ1bZ1i49DWiTSQlUW9SpDpq_Gturk6Fl0deIztMpCtjhKcUX4GN5-AdosahphQeDiUhDBu9uSqXPGvcN7eE6zii_sPL9tGjC8Dxy5Ji54YecFTdPfzNeY15fenUEjXBQUDNXnkvVBju0j4IydwhCtv8OOrDAvW4W1WY7Dx3rKtpWF0lh81NaF-xZTBgVOs2u8iCx5rrN-i5WcR1kTlFWFHm35ekoRcDTbv8YzWOMWAS6Srpo84BOT0D1Muhau8xUS9rnrp884QbBxBOCaziWxIl7rfGiicC8Lvj_7PotQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967738cda4.mp4?token=reocLdGFVJ2jBhB_cm1gUS25rBKGAEu6EMdJuB9uyexVZ1bZ1i49DWiTSQlUW9SpDpq_Gturk6Fl0deIztMpCtjhKcUX4GN5-AdosahphQeDiUhDBu9uSqXPGvcN7eE6zii_sPL9tGjC8Dxy5Ji54YecFTdPfzNeY15fenUEjXBQUDNXnkvVBju0j4IydwhCtv8OOrDAvW4W1WY7Dx3rKtpWF0lh81NaF-xZTBgVOs2u8iCx5rrN-i5WcR1kTlFWFHm35ekoRcDTbv8YzWOMWAS6Srpo84BOT0D1Muhau8xUS9rnrp884QbBxBOCaziWxIl7rfGiicC8Lvj_7PotQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای سنتکام
نفتکش M/T Downy در نزدیکی جزیره خارگ و نفتکش M/T Stark 1 در نزدیکی جاسک را به‌طور دائمی از کار انداختند
. همچنین نیروهای آمریکایی
نفتکش خالی M/T Kylo، معروف به «Noxen»، را در دریای عمان به‌طور کامل منهدم کردند
؛ این نفتکش پس از آن هدف قرار گرفت که به خدمه آن دستور داده شد کشتی را ترک کنند و نیروهای آمریکایی با اصابت به
چندین نقطه حیاتی کشتی، آن را غیرقابل استفاده کردند
. سنتکام اعلام کرد این
سه نفتکش ایرانی بخشی از یک شبکه چندمیلیارد دلاری انتقال پنهانی نفت
هستند که منابع مالی سپاه پاسداران و نیروهای نیابتی آن در منطقه را تأمین می‌کند و مدعی شد
ایران توانایی دفاع از این نفتکش‌ها را ندارد
.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22362" target="_blank">📅 17:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد که پس از شلیک موشک‌های بالستیک سپاه پاسداران به سمت 2 ناو جنگی نیروی دریایی آمریکا که در آب‌های منطقه در حال گشت‌زنی بودند، نیروهای آمریکایی
3 نفتکش ایرانی را هدف قرار دادند
یک ناو هواپیمابر و یک ناوشکن موشکی آمریکایی با موفقیت از چندین حمله ایران عبور کردند و
هیچ نیروی آمریکایی آسیب ندید
.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22361" target="_blank">📅 17:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وال‌‌استریت ژورنال
:
ایده
«تغییر رژیم» در ایران بار دیگر در واشنگتن جدی شده
است. این نشریه می‌نویسد در داخل دولت ترامپ، این دیدگاه که جمهوری اسلامی یک واقعیت دائمی در منطقه است، دوباره در حال کمرنگ شدن است و برخی مقام‌ها به امکان تغییر بنیادین وضعیت سیاسی ایران توجه بیشتری نشان می‌دهند.بر اساس گزارش‌های وال‌استریت ژورنال، دولت آمریکا هم‌زمان روی
فشار اقتصادی، تحریم‌ها و محاصره دریایی
به‌عنوان ابزارهایی برای تشدید فشار بر تهران حساب باز کرده است؛ هدف این است که فشار اقتصادی به اندازه‌ای افزایش یابد که جمهوری اسلامی به تغییر رفتار یا پذیرش خواسته‌های آمریکا وادار شود
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22360" target="_blank">📅 17:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22359">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26928dc53.mp4?token=uzvr40PUsp4g1n8e4c4lVdiDXDl4Zkq67xubnBh68__h7SbwgO9cKwUVWutozvgss9k1RXOdwbCVQioPUOXTmXAHwk9ZzyqyEN-nLtWsH2_p8Mec72-FItinIT5FmxNP3hBMrdaRmUBbMJmqOw9K79H_uBJdEB8WsfpwDv55pui5fNyYSNab45bONtjv2oenY2Kp0VJQjElxVdugeGh0uwzjjiFwyhFvi9m3AemwcFF1ZxGvede-L7hEJ3MpGl7RZ4-_vlQGfpp4OtniIbR_jzaqUwJZ0HLBMyxOstlgLuOjg89HrERAALorGEHcxIw3JHE63Q4dCKgOXKGdqFRF3lh7B2zFf_Q6gZ1A9Gzf1a_ZzL8_IylxOz7msoUZ-x0lYsmKXef5fLIX7El5ehgSSu5Lp63dXZnYXBlXBCkE0ZgfshGRQ74miRE6GhBO1nYFsocC3nizn6Mf55V12ZBXApnoA7HhhI4KdKm-fASjbt_Y8nD7l_qx1edQxvn8nDFh7j4ItArfuB9OEI7wsBgmPAdFgxGkXocOS7dHBZVExg8tBblUTRIVlAmZHPNOr7zC6Wcjz-tWukhBnC5t_xqm2xmnmnJR-FllyddDZT2nVXh9RGh6U0c_srz4nFSpFjqI9-rZ_TcbqKg6FNpYjlwJB_-qPigHBZeonGVq9lRdHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26928dc53.mp4?token=uzvr40PUsp4g1n8e4c4lVdiDXDl4Zkq67xubnBh68__h7SbwgO9cKwUVWutozvgss9k1RXOdwbCVQioPUOXTmXAHwk9ZzyqyEN-nLtWsH2_p8Mec72-FItinIT5FmxNP3hBMrdaRmUBbMJmqOw9K79H_uBJdEB8WsfpwDv55pui5fNyYSNab45bONtjv2oenY2Kp0VJQjElxVdugeGh0uwzjjiFwyhFvi9m3AemwcFF1ZxGvede-L7hEJ3MpGl7RZ4-_vlQGfpp4OtniIbR_jzaqUwJZ0HLBMyxOstlgLuOjg89HrERAALorGEHcxIw3JHE63Q4dCKgOXKGdqFRF3lh7B2zFf_Q6gZ1A9Gzf1a_ZzL8_IylxOz7msoUZ-x0lYsmKXef5fLIX7El5ehgSSu5Lp63dXZnYXBlXBCkE0ZgfshGRQ74miRE6GhBO1nYFsocC3nizn6Mf55V12ZBXApnoA7HhhI4KdKm-fASjbt_Y8nD7l_qx1edQxvn8nDFh7j4ItArfuB9OEI7wsBgmPAdFgxGkXocOS7dHBZVExg8tBblUTRIVlAmZHPNOr7zC6Wcjz-tWukhBnC5t_xqm2xmnmnJR-FllyddDZT2nVXh9RGh6U0c_srz4nFSpFjqI9-rZ_TcbqKg6FNpYjlwJB_-qPigHBZeonGVq9lRdHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: من به قطر حمله کردم
من آن را بمباران کردم و هم در طول جنگ به آنها حمله کردم، و آنها به من حمله کردند.
کل این ماجرای قطر یک بلوف بزرگ است. قطر یک کشور متخاصم است، اما قطر کشوری نیست که چیزی را به ما دیکته کند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22359" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نرخ دلار ۲۲۵،۶۰۰ تومان(سقف تاریخی) دلار کف بازار :حدود ۲۳۰ هزار تومان! تتر ۲۲۴،۶۰۰ تومان (سقف تاریخی) بیتکوین ۷۹،۶۴۶ $ انس جهانی طلا ۴،۴۲۷ $(آخرین قیمت) نفت برنت  ۹۶،۲۸$(آخرین قیمت) @WarRoom
🚨
🚨
🚨
🚨
۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22358" target="_blank">📅 15:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرگزاری تاس:
ویتکاف و کوشنر، فرستادگان ترامپ، با پوتین گفت‌وگو کردند.
پوتین دستور توقف حملات به اوکراین را صادر کرد
به‌مدت سه روز هیچ حمله‌ای به کی‌یف انجام نشود؛ این تصمیم در چارچوب مقدمات سفر هیئت آمریکایی اتخاذ شده است
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22357" target="_blank">📅 15:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نرخ دلار ۲۲۵،۶۰۰ تومان(سقف تاریخی) دلار کف بازار :حدود ۲۳۰ هزار تومان! تتر ۲۲۴،۶۰۰ تومان (سقف تاریخی) بیتکوین ۷۹،۶۴۶ $ انس جهانی طلا ۴،۴۲۷ $(آخرین قیمت) نفت برنت  ۹۶،۲۸$(آخرین قیمت) @WarRoom
🚨
🚨
🚨
🚨
۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22355" target="_blank">📅 15:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f970801a4.mp4?token=fRCrDITwZnwryPULOm1sCNx9BIGhCE5wxnnf4266q4pXD0YgKq0bIK8uNWI2_Huf6pzWpQUfahIYfQoAdH07wFtCkaOOhPrI1bQo7QbV0QovVJzMXuRF_fDiGnqHJY39RELHubqu4vREYK-S8ATtTCHINMawguTG46x7MaOTBwWGSDEj3BwMSdu64jpIPF4UvNPq1xhIzbcgwsXcfNXGb2RWBSbGca46zxleDqMv7rt0O7EX4fjyfIlSRmfeKgS315SFgSIt4wShRkZY6MXYCdaB6i0xzebM-dFRL3eg4lTcix55IsMhqAWtdK1NUhkHIov52Nl-sbkKoi2diGK4sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f970801a4.mp4?token=fRCrDITwZnwryPULOm1sCNx9BIGhCE5wxnnf4266q4pXD0YgKq0bIK8uNWI2_Huf6pzWpQUfahIYfQoAdH07wFtCkaOOhPrI1bQo7QbV0QovVJzMXuRF_fDiGnqHJY39RELHubqu4vREYK-S8ATtTCHINMawguTG46x7MaOTBwWGSDEj3BwMSdu64jpIPF4UvNPq1xhIzbcgwsXcfNXGb2RWBSbGca46zxleDqMv7rt0O7EX4fjyfIlSRmfeKgS315SFgSIt4wShRkZY6MXYCdaB6i0xzebM-dFRL3eg4lTcix55IsMhqAWtdK1NUhkHIov52Nl-sbkKoi2diGK4sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : درصورت پیروزی در انتخابات رژیم ایران را عوض میکنم
نتانیاهو: سوال اصلی در این انتخابات این است: چه کسی کارهایی را که باید انجام شوند، به پایان خواهد رساند؟ چه کسی بالاخره این رژیم را در ایران نابود خواهد کرد؟ چه کسی بالاخره حزب‌الله را نابود خواهد کرد؟ چه کسی بالاخره حماس را نابود خواهد کرد؟
مخالفان سیاسی من در برابر هر فشاری تسلیم می‌شوند. آمریکا به آنها می‌گوید "نه"، و آنها بلافاصله می‌لرزند.
آیا آنها این کار را انجام خواهند داد؟ نه. آنها این کار را انجام نخواهند داد. ما این کار را انجام می‌دهیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22354" target="_blank">📅 15:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5ab34899.mp4?token=of0nM-CdKOpIEb2QS1AQqSg2EFCFoDjBDceIL5lwYcm_GqqW0RdYXrIj96GiSGvnyHiULWzy6_AZdRzC10ULmK-TIdIEdBhrt6NIAL_bXRcGTqD9gY3SHhL3NE2hb0F6AowadE9ekAiaLxwEY6nCRowS-MFwJ-Fu6x_cKOGmmZkTQaNe3va5n9jx9DUfrGE8gklYXCz9I9eKcv47vfuRSUfJ6d89cIfd6FpWh7TUFBRqgvXpaEcT2luodZSQLuzjDB4yHmDXP2foEr7m-ML6CE73taGZCVuXe7JkdtCAtm-4GUKVWngoyb1iYHI8LJlnsO0ezC2Vwc4b7CKEosPlqYEvjmragJw_UvtWZx6KfudV8T8tum2prDIlmBnxgxDo3sXMRzGBKio0M-fwY2jkRpljca_jctOMQr3cYiDUCodhIKxFf9zfaVPr-jpQxAvWYm4QbGqHoqSlZ-QqucPe_j9_7KTDj50-pKq80BxNQ5i-AIIl3IFPL0-BQKhrNa3P1vNIKeurR9LSXie9rEgelrVa10-gnFFIV4fUeYHXcWkbJHrDDrjufpBRcCuQOMwb23UFREqIGPc50e-fiNA29piAU8je56eSuWgsXUsyK3ZptVr3dfEAORivfVuPP8Yj13Z-FWZ1KM_MsW6Dnuhs3rYU3gziCqGXyOdPM8RvQWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5ab34899.mp4?token=of0nM-CdKOpIEb2QS1AQqSg2EFCFoDjBDceIL5lwYcm_GqqW0RdYXrIj96GiSGvnyHiULWzy6_AZdRzC10ULmK-TIdIEdBhrt6NIAL_bXRcGTqD9gY3SHhL3NE2hb0F6AowadE9ekAiaLxwEY6nCRowS-MFwJ-Fu6x_cKOGmmZkTQaNe3va5n9jx9DUfrGE8gklYXCz9I9eKcv47vfuRSUfJ6d89cIfd6FpWh7TUFBRqgvXpaEcT2luodZSQLuzjDB4yHmDXP2foEr7m-ML6CE73taGZCVuXe7JkdtCAtm-4GUKVWngoyb1iYHI8LJlnsO0ezC2Vwc4b7CKEosPlqYEvjmragJw_UvtWZx6KfudV8T8tum2prDIlmBnxgxDo3sXMRzGBKio0M-fwY2jkRpljca_jctOMQr3cYiDUCodhIKxFf9zfaVPr-jpQxAvWYm4QbGqHoqSlZ-QqucPe_j9_7KTDj50-pKq80BxNQ5i-AIIl3IFPL0-BQKhrNa3P1vNIKeurR9LSXie9rEgelrVa10-gnFFIV4fUeYHXcWkbJHrDDrjufpBRcCuQOMwb23UFREqIGPc50e-fiNA29piAU8je56eSuWgsXUsyK3ZptVr3dfEAORivfVuPP8Yj13Z-FWZ1KM_MsW6Dnuhs3rYU3gziCqGXyOdPM8RvQWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در مورد سوء قصد علیه پسرش یائیر:
فقط می‌توانم بگویم که چنین سوء قصدی وجود داشته است. این یک اقدام قابل توجه بود. سرویس‌های امنیتی به سرعت اقدام کردند.
آنها حتی نیروهای کمکی از نیروهایی که در ایالات متحده داشتیم آوردند تا او را به سرعت از ایالات متحده خارج کنند. این کاملاً واقعی است.
و این اتفاق در نتیجه رفتار غیرمسئولانه - واقعاً بی‌ملاحظه - چندین روزنامه‌نگار و افراد دیگر رخ داد که مکان یائیر را به صورت زنده افشا کردند: آدرس دقیق محل اقامت او، عکسی از آپارتمان، شماره طبقه، شماره آپارتمان.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22353" target="_blank">📅 14:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/175ac48990.mp4?token=Fgf4SrDJgaF_yvW9mCOlGR4uGlJh7wT_6zPrMDysZJIK70KMlfHfGQPDdee9tl5l1QE_3tmbUUuDzUVdyqfFAgY9caHWSZnW4O35xfmZdT4OksId3Tsz7_Qia99sMoUgng7lwtdk7PqCQieB0nF0LRj_-rfoOeNEKKo5poXC9TBFikRG-YSMUJ-caM134SnicQHvXXAFfiTNiR3D3jj2WHFfRZpLDDVRNkX736c7pft6SB6ab-ZKSDAyTuypg3MNZxnqalQlqAT5wV18NpoG8GutP-h1ykQ7WLPONL0SSCI7jvQ80Bp30VyWuZhL-Jhbe2FylG0YqkQf6aZtgXQZFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/175ac48990.mp4?token=Fgf4SrDJgaF_yvW9mCOlGR4uGlJh7wT_6zPrMDysZJIK70KMlfHfGQPDdee9tl5l1QE_3tmbUUuDzUVdyqfFAgY9caHWSZnW4O35xfmZdT4OksId3Tsz7_Qia99sMoUgng7lwtdk7PqCQieB0nF0LRj_-rfoOeNEKKo5poXC9TBFikRG-YSMUJ-caM134SnicQHvXXAFfiTNiR3D3jj2WHFfRZpLDDVRNkX736c7pft6SB6ab-ZKSDAyTuypg3MNZxnqalQlqAT5wV18NpoG8GutP-h1ykQ7WLPONL0SSCI7jvQ80Bp30VyWuZhL-Jhbe2FylG0YqkQf6aZtgXQZFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نِتانیاهو درباره ایران: چه کسی در تاریخ ۷ اکتبر فکر می‌کرد که ما چهره‌ی خاورمیانه را تغییر خواهیم داد؟ من فکر می‌کردم.
نیت من این بود که در نهایت با ایران درگیر شویم
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22352" target="_blank">📅 14:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22351">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMett</strong></div>
<div class="tg-text">سلام یاشار
روزت بخیر
این صحبت درست نیست
خودروهای لوکس از منابع ارزی فردی که در حجم بالا ذخیره داره خارج میشه و معادل همون مقدار بابت ترخیص پرداخت میشه و از این طریق به جیب دولت کمک میکنه
اون دارایی اگر بابت پورشه ۹۱۱ نره قفل توی کشو هستش
واقع بینانه باید پذیرفت ج.ا. در راهبردهای نظامی و اقتصادی در شرایط فشار حداکثری موفق بوده و در مورد اجازه واردات خودرو لوکس هم تصمیم درستی گرفته</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22351" target="_blank">📅 14:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو درباره غزه: بازسازی غزه فقط در صورتی امکان‌پذیره که ابتدا خلع سلاح انجام بشه. هنوز نمی‌تونم بگم چه نوع بازسازی‌ای انجام خواهد شد، چون در حال گفت‌وگو با دوستان آمریکایی‌مون درباره این موضوع هستیم. گاهی اوقات دیدگاه ما با آمریکا یکیه، اما گاهی هم اختلاف نظر داریم. وقتی اختلافی وجود داشته باشه، آمریکا منافع خودش رو مطرح می‌کنه و من هم از منافع اسرائیل دفاع می‌کنم
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22350" target="_blank">📅 14:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d1a681e.mp4?token=P5iq3fM2QamFyOeUtGR9RP7dM5Y0qnYSOKXuYOq_kABzuefqY_sjPu1I4px18fZJkcwnMYd7IcdMroUVEhNTaL9TPKJaeSBlzpEQtcWzQTYTw1KjQtR4PbxgWEbSqCV9bYQqv96pKmsG0BcDgZVOd42_0napZoiQMMMC8o-OxBYS84PgZxBUGYBHnWnNebDCueK18RJqenEBjjF1zpcYisQylVgO8hMIOvUoMErZ2Qkg4JH6Ul3PVpMWr2NGfwYTvhF1Q1HAtJXcWoX7qjBcyp1HSlUhE8clwRxJgNwbi15ONNoCAe3NP4RILxnRr7IT6PFNDdYtQ70faipOxIowGaZ3G0YjJatTIyx_MMlfZzprZR1r_QzRtBZDqyIydJ2BtTuMD5ztvFy9VgIaqpdjGImV2wm4r43kRM7QYxQjTjqIR6T3mkJJKdVVou05hIubq_RDIHJ4dZcau9UKE3dT9mKBRaeuXz8IObJDRj1p-fqR5wUuOYww5pwj33u8oo--KTXSR8N5dhj_G04aoj9lqcJ08dnXB3PQC8M-onIYQmh7GGFBBinO-j5H5S-Pfzhih5gECRH2exa_eK4gVh4KWTGW95F8GcCu7xUwYVbCsGnFpcVHibEPFJfAQmiYBSXSdS6zpYlR9Kn0_NSnvFwloJxKCw6iv_ORzSWupacB4DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d1a681e.mp4?token=P5iq3fM2QamFyOeUtGR9RP7dM5Y0qnYSOKXuYOq_kABzuefqY_sjPu1I4px18fZJkcwnMYd7IcdMroUVEhNTaL9TPKJaeSBlzpEQtcWzQTYTw1KjQtR4PbxgWEbSqCV9bYQqv96pKmsG0BcDgZVOd42_0napZoiQMMMC8o-OxBYS84PgZxBUGYBHnWnNebDCueK18RJqenEBjjF1zpcYisQylVgO8hMIOvUoMErZ2Qkg4JH6Ul3PVpMWr2NGfwYTvhF1Q1HAtJXcWoX7qjBcyp1HSlUhE8clwRxJgNwbi15ONNoCAe3NP4RILxnRr7IT6PFNDdYtQ70faipOxIowGaZ3G0YjJatTIyx_MMlfZzprZR1r_QzRtBZDqyIydJ2BtTuMD5ztvFy9VgIaqpdjGImV2wm4r43kRM7QYxQjTjqIR6T3mkJJKdVVou05hIubq_RDIHJ4dZcau9UKE3dT9mKBRaeuXz8IObJDRj1p-fqR5wUuOYww5pwj33u8oo--KTXSR8N5dhj_G04aoj9lqcJ08dnXB3PQC8M-onIYQmh7GGFBBinO-j5H5S-Pfzhih5gECRH2exa_eK4gVh4KWTGW95F8GcCu7xUwYVbCsGnFpcVHibEPFJfAQmiYBSXSdS6zpYlR9Kn0_NSnvFwloJxKCw6iv_ORzSWupacB4DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هواپیمای نظامی آمریکایی در فرودگاه بین‌المللی اربیل در اقلیم کردستان عراق فرود آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22349" target="_blank">📅 14:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9102f4bd1c.mp4?token=COfrtfRynmEasuqpPi6dCuDXx75lwgAA8v9Zk2oPGErWXri1fQjlzcH4RCeHf90G196ie4kg1f1er6Vmi1YHdYI5wBQLkpOu12bQ05W_4wkgNDOZ0sGAKRY5j5VYhdsXs4DYsuaq8zBkN8c1aIFy_qfx2ZNmsfe1L1hoIQ2sszYK_RK9DMzcj1snaExpwcVeDVOSv23AbqfeS3x-x47lbdJjZaCX78rxYjvJXnZpc80og5vXR_WPP_AyzCRMBjcVUOiEhfO9z44SkvUI2h998hGMCg-qR8QYn2QEt3bVp1wbHJmEYbfHf8Wjp4mhO8ebX0GEUgF0MABsp4kONMJMdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9102f4bd1c.mp4?token=COfrtfRynmEasuqpPi6dCuDXx75lwgAA8v9Zk2oPGErWXri1fQjlzcH4RCeHf90G196ie4kg1f1er6Vmi1YHdYI5wBQLkpOu12bQ05W_4wkgNDOZ0sGAKRY5j5VYhdsXs4DYsuaq8zBkN8c1aIFy_qfx2ZNmsfe1L1hoIQ2sszYK_RK9DMzcj1snaExpwcVeDVOSv23AbqfeS3x-x47lbdJjZaCX78rxYjvJXnZpc80og5vXR_WPP_AyzCRMBjcVUOiEhfO9z44SkvUI2h998hGMCg-qR8QYn2QEt3bVp1wbHJmEYbfHf8Wjp4mhO8ebX0GEUgF0MABsp4kONMJMdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران
: اونا می‌تونن به ما حمله کنن و ما هم پاسخ می‌دیم.
متوجه شدید ایران داره به همه شلیک می‌کنه؟ به کی شلیک نمی‌کنه؟ فقط اسرائیل.
چرا؟ چون دقیقاً متوجه حرف من هستن؛ تا وقتی من نخست‌وزیرم، چنان ضربه‌ای بهشون وارد می‌شه که حتی نمی‌خوام جزئیاتش رو بگم. این ضربه از قبل آماده شده.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22348" target="_blank">📅 14:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نرخ دلار ۲۲۵،۶۰۰ تومان(سقف تاریخی) دلار کف بازار :حدود ۲۳۰ هزار تومان! تتر ۲۲۴،۶۰۰ تومان (سقف تاریخی) بیتکوین ۷۹،۶۴۶ $ انس جهانی طلا ۴،۴۲۷ $(آخرین قیمت) نفت برنت  ۹۶،۲۸$(آخرین قیمت) @WarRoom
🚨
🚨
🚨
🚨
۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22347" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405d38bbbf.mp4?token=ErEMqsD4z2R4CYoMXYN8AHpYZIdwJU8ds3soRhi-ZmWsrMC2Hm4rSbSpAVOJqtQTO1VXxL0ABCwLoajCRiJ9idWQEGMhoFZzdhryEZuOun2fUS2bJfvtBmKojKEEemlYt0IJK7ebfHCUV_mnXaJMQDylhuzkwqpSlYDWi56biDfw2lY7eLJC-pDOjY-7Ztt42o_pWiNVTDlR6ANwOnU-ki_JsW-moq0hAMJpLooz9hacVh7cFkG05HPc1UxZkSoK2sd8pGUnntXKCjuvage6hZJ1x9foQgBvssg22SiSdj7DD5JFM0Zajx5Kg1SmFCbtwy3NWC2Cf0-nadV00p4f0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405d38bbbf.mp4?token=ErEMqsD4z2R4CYoMXYN8AHpYZIdwJU8ds3soRhi-ZmWsrMC2Hm4rSbSpAVOJqtQTO1VXxL0ABCwLoajCRiJ9idWQEGMhoFZzdhryEZuOun2fUS2bJfvtBmKojKEEemlYt0IJK7ebfHCUV_mnXaJMQDylhuzkwqpSlYDWi56biDfw2lY7eLJC-pDOjY-7Ztt42o_pWiNVTDlR6ANwOnU-ki_JsW-moq0hAMJpLooz9hacVh7cFkG05HPc1UxZkSoK2sd8pGUnntXKCjuvage6hZJ1x9foQgBvssg22SiSdj7DD5JFM0Zajx5Kg1SmFCbtwy3NWC2Cf0-nadV00p4f0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آکسیوس گزارش داده است که استیو ویتکوف و جرد کوشنر، فرستادگان دونالد ترامپ، این آخر هفته به مسکو و کی‌یف سفر می‌کنند تا تلاش‌های دیپلماتیک آمریکا برای پایان دادن به جنگ روسیه و اوکراین را از سر بگیرند. طبق گزارش آکسیوس، قرار است ویتکوف و کوشنر شنبه با ولادیمیر…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22346" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وال‌‌استریت ژورنال:
محاصره دریایی آمریکا از تیرماه صادرات نفت ایران را تقریباً متوقف کرده و بستن تنگه هرمز از سوی ایران نیز ترامپ را به پذیرش شروط تهران وادار نکرده است. طبق این گزارش، رهبران ایران انتظار دارند وضعیت کنونی و فشارهای اقتصادی ناشی از آن حدود
پنج ماه دیگر
ادامه پیدا کند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22345" target="_blank">📅 13:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پارلمان پاکستان برای نخستین بار به عاصم منیر اختیار قانونی فرماندهی هر سه نیروی ارتش، نیروی دریایی و نیروی هوایی را اعطا کرد
دوره فرماندهی او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت
وی در مقام «فیلد مارشال»، مصونیت قانونی خود را تا پایان عمر حفظ می‌کند و برکناری او تنها با رأی دو سوم پارلمان امکان‌پذیر است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22344" target="_blank">📅 13:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نرخ دلار ۲۲۵،۶۰۰ تومان(سقف تاریخی)
دلار کف بازار :حدود ۲۳۰ هزار تومان!
تتر ۲۲۴،۶۰۰ تومان (سقف تاریخی)
بیتکوین ۷۹،۶۴۶ $
انس جهانی طلا ۴،۴۲۷ $(آخرین قیمت)
نفت برنت  ۹۶،۲۸$(آخرین قیمت)
@WarRoom
🚨
🚨
🚨
🚨
۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22343" target="_blank">📅 13:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر جنگ اسرائیل :
منتظریم ایران به تصرف تپه "علی الطاهر" واکنش نشون بده و حرکتی بزنه تا از غل و زنجیر و محدودیت‌های ایجاد شده توسط ترامپ آزاد بشیم.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22342" target="_blank">📅 13:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">صحبت های زیبای یک کاربر درباره پست قبلی
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22341" target="_blank">📅 13:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اتاق جنگ با یاشار : سوی دیگر فشار اقتصادی ، نمایشگاه های کشور های خلیج فارس با کمبود خودرو هایی مواجع شدند که در لیست واردات ایران قرار‌ دارند و تا مواردی برای لکسوس ال اکس ۶۰۰ تا ۲۰،۰۰۰$ قیمت این خودرو در بازار افزایش یافته ، بعد از صحبتم با یک نمایشگاه دار قدیمی ، وی گفت جنگ فشار بالای به ما وارد کرد ولی در ۳۰ روز گذشته ۲۰۰ خودرو فروخته ام و در تعجبم از این بازار تمام خودرو هایم که به ایران میرفت فروخته شده ، چند روز پیش خودرو جی۶۳ و پورشه ۹۱۱ هم به لیست واردات اضافه شدند ! پیغام واتس اپش را که نشان داد شخصی در حال مذاکره برای خودرو جی کلاس ۶ چرخ (6x6) بسیار لیمتد بود از وی ! و پرسید چطور پس میگویند کسی پول ندارد ؟! دلار در این لحظه ۲۲۵،۰۰۰ تومان است !
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22340" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81fbb27ca2.mp4?token=W4ABjkYGzvVOD5Sq1m7cdCLpNUIcFqzCCQAskH-cDFd9WN1MarcubVwiEpv356Cy_AKM5I_dTCnR_KhT8IPNEIfCcV49f9LACVKXTVr0oavWJLK2yyWonuEb1BRF8XwchHvk0x9h2LpDLjJswN7VJyzBbuXVBu4TPBCoZhhAjbyPXIW9Pq404ngGPMIJyLlkinPakwH7Pq6QpGnPx5wyWWlLlNHJlaJyFm0g0dkIzPS_tABzzV5YYpIRTBwxC-1CFvprIQH_F94Tap1SLLJA-sjFAWA6Bih_xJ1-il7zvkba0FiWRkL6YmnH_nM_BIEuUU6ZlaSeI8ifLqHipH5mYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81fbb27ca2.mp4?token=W4ABjkYGzvVOD5Sq1m7cdCLpNUIcFqzCCQAskH-cDFd9WN1MarcubVwiEpv356Cy_AKM5I_dTCnR_KhT8IPNEIfCcV49f9LACVKXTVr0oavWJLK2yyWonuEb1BRF8XwchHvk0x9h2LpDLjJswN7VJyzBbuXVBu4TPBCoZhhAjbyPXIW9Pq404ngGPMIJyLlkinPakwH7Pq6QpGnPx5wyWWlLlNHJlaJyFm0g0dkIzPS_tABzzV5YYpIRTBwxC-1CFvprIQH_F94Tap1SLLJA-sjFAWA6Bih_xJ1-il7zvkba0FiWRkL6YmnH_nM_BIEuUU6ZlaSeI8ifLqHipH5mYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از نفتکش هدف قرارگرفته توسط آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22339" target="_blank">📅 12:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نفتکش ایرانی در جزیره خارک هدف حمله موشکی آمریکا قرار گرفت بنابر گزارش منابع محلی به خبرگزاری دانشجو، یک نفتکش ایرانی در جزیره خارک هدف موشک نیروهای آمریکایی قرار گرفته است. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22338" target="_blank">📅 10:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22337">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa-B8YIgjHlHWPMnQepyMWuzvO7uJLWnznq6HTMJT7lr5qvTkb77mWA5Sbc75RTu1XQ4u2RT1Eg4zyWLMRa4ymXI_fvOFLaurNYfG8Dh1a8tLBNUBLpqCPN60TsvftqdP6fwf3ONqX54lV0zlDFBXH2_ZCDcIYtk2so7bwgK7K83KdbYoVUJ8UopDxkA7rmQL7n63e5-AlgExH60LUbKGHXqpRd-GddiGXrnkRrT8Ct9VCouaJLAcPI9oHupLONpAxpo1TvQvGrA4yRxGk0Ji9LFlZdney1ZqRVuk8eL0eRtVQyvNb-6SmFkqIzIvC5dINaeYtEjzX09ykWos0Mw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای روسیه احتمالا دارد نیرو های روس را از عسلویه بوشهر خارج میکند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22337" target="_blank">📅 10:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParsaTUNZ🛸</strong></div>
<div class="tg-text">یاشار ی انفجار جدید شنیده شد
🚨
(جزیره خارک)</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22336" target="_blank">📅 10:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22335">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAb Mh</strong></div>
<div class="tg-text">یاشار دوباره هم صدای انفجار اومد ۲ تا بود ایندفعه صداش خیلی شدید تر بود</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22335" target="_blank">📅 10:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUgwmZKM5x1sv3HjmiHVhOWdOrmsx4QYv42jH4uFDrd5CqQ8TQT3ZBkkpY18lZXYct7v_FpiMBCXmQ_gSz-a2HYED57qvnrgAt0W_FJYxLPu1LwHSKWla3ZyMdcTU77_9KP-N9_eHYR6Yl3aB6wDpovFQMtNbMusTbtgYoleDDNLw4lR8r5E1GJ_MAMwU4JNE_zo3pO5KsSxmfhSmSOG4ogCsAnZUxof0Sb1VOJb06rkf-wMZqpVPAAR69iWYevxyRhCCOK7tP_Do7IC_zYSe1XcnUryJu9PoEla8CjWN1SdHF_2rzlote2ZRYPhyby3wY41Ij0nMYtP1_0o9-9l8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش انفجار ،  پایگاه نظامی حیدر کرار در محدوده شهرستان دماوند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22334" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-text">یاشار سلام داشتم می‌رفتم دلی جان یه دفعه پشتم ترکید فکر کردم لاستیکمه پشتمو نگاه کردم دیدم دود بلند شده از لای کوه می‌دونم چی اونجا بود زدنش</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22333" target="_blank">📅 10:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c67d702f0.mp4?token=Jz28EBmIiMwLteQ1FVXW2Gr4W9L0ZrWkgP0eOQfWpOa-rnkyNYj8dNyIl2D6bW6T9kw7G8dQAJa7homXThRHGnNLhL02uDxqbsEJrHlfIHfwhaIr1TzvNlzacDKrKGITvBiR2O2_fWJdDhYcOXXVusUyDyVWNYC7xuNIswZIb5KvhR8gHcWKjpkmlfLcVwPLFC_EjZgI2xi45X0qALc_f0KtRvFwiQxM5r4Dnju6WlbW4zyJs3Fg9Z75DGOrPBXxwcg34537baVsMnRgkTg_k21S8Iw_Je8S3oHVM-mIb-GffdmNl_SjhI-Y8MEJ3q0JZ0agm5GrnLWOb4h7LQSm5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c67d702f0.mp4?token=Jz28EBmIiMwLteQ1FVXW2Gr4W9L0ZrWkgP0eOQfWpOa-rnkyNYj8dNyIl2D6bW6T9kw7G8dQAJa7homXThRHGnNLhL02uDxqbsEJrHlfIHfwhaIr1TzvNlzacDKrKGITvBiR2O2_fWJdDhYcOXXVusUyDyVWNYC7xuNIswZIb5KvhR8gHcWKjpkmlfLcVwPLFC_EjZgI2xi45X0qALc_f0KtRvFwiQxM5r4Dnju6WlbW4zyJs3Fg9Z75DGOrPBXxwcg34537baVsMnRgkTg_k21S8Iw_Je8S3oHVM-mIb-GffdmNl_SjhI-Y8MEJ3q0JZ0agm5GrnLWOb4h7LQSm5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : خوب مشخص نیست دوره ولی شناورا دارن آب میریزن روش
صدای ۳ انفجار جدید
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22332" target="_blank">📅 10:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش صدای انفجار جدید جزیره خارگ
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22331" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">طبق گزارش منابع محلی به صدا و سیما رژیم:
نفتکش هدف قرار گرفته‌شده در جزیره خارک، یک نفتکش کوچک بوده است.
بر اساس این گزارش، این حادثه تلفات جانی نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22330" target="_blank">📅 10:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🌋</strong></div>
<div class="tg-text">نیم ساعت پیش فکر کردیم بوشهرو زدن خارگ ۴۵ کیلومتر فاصله داره صدای سه انفجارش تا اینجا رسید</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22329" target="_blank">📅 10:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKbsJq9KLG0jHRzIG1WBzjPl30lnz7vbSZV0OHEWzp3tRonFwbGFPWhOaqnbfhKaUyyeFygfPN4In3SrzkahmPC42C3KoxOhkcXkIF61jRyjmh3vQb82DtYKtZcfhX8ghKp6sh43nAh-klMzfWL6XGlbANf_MaeCH2XY3rIOxSiLiEzKxcEDrR5B5xZLeDll12MtZaBnOJiupFGCFpks54CBdCKd8s6XHxf4fUR0_2lIVxBUsTcWPa7b_2GQxPi0_njWU1GvwiW_szTOhpYrj04peHgKXny2lqOp-Ic8yEo4JBLs9xl3vqazu5vd0hsgWfq6GmBnT5hepueZGc-Bjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوه صفه اصفهان
💨
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22328" target="_blank">📅 10:13 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
