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
<img src="https://cdn4.telesco.pe/file/groI5xTpwv63gfZoi6J4nCDzOlcRYiL7alhPvmfSys8QS9iuFLn3N4KNX-dCNvym4v7j0bdQxS-ogrXW9QKkfhpqlFGC3LOOBlCFSi8DRxzRuhYuE12uKp8IWm5Q8oYnn5Dd6VABPOEdQ4RbRomkd5R03bDxF0BH2YU7It7nbLOcUU9Cvz57HF-l9sqznIzP27GAnZa4Wd98L-up_IT86s7Q0swHckr9_HxE5knU8gqfbWkSkbl1uv0dmCtMAmd5XZjW_L0lexBSNtKYIUgxAC_TWi6gkWzI0GZNdqQS4Ab_2Urlor3LYszHLvS5KhYuyEDAEpu4KLX0Q9TxtVkY0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 09:00:12</div>
<hr>

<div class="tg-post" id="msg-69341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/69341" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69340">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ubIFrIVmfrTWHnuCtbRzu9qoW7Z-60em047zEXd40AcIRseJ5178qUKDUbLuEsoQu4v4e1C1EGV0rV9aXC2UNR64NuWSAGkWJun1LEXmDPE5JDqSQrZD2yY0Qx7Zqfh5ktVWg2TV0pJJbZVUe5ujp6XAcfy-jQPw3XjSwvEHway5b0XoA12PgJLTnQNL1LlzKNkyffKgatA12xmYiAjsk8e-QHrYmeMJOZtJoNYcTz20rRvxdXr37MQidt3rO8TTw3tbW2sAodSCUnfOmGNPgBjrK8mY0iGB55CRTqYBp2rRparGohcKAI7pQEf2Tme6XaFOcN231ukuodXk5v_bKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ubIFrIVmfrTWHnuCtbRzu9qoW7Z-60em047zEXd40AcIRseJ5178qUKDUbLuEsoQu4v4e1C1EGV0rV9aXC2UNR64NuWSAGkWJun1LEXmDPE5JDqSQrZD2yY0Qx7Zqfh5ktVWg2TV0pJJbZVUe5ujp6XAcfy-jQPw3XjSwvEHway5b0XoA12PgJLTnQNL1LlzKNkyffKgatA12xmYiAjsk8e-QHrYmeMJOZtJoNYcTz20rRvxdXr37MQidt3rO8TTw3tbW2sAodSCUnfOmGNPgBjrK8mY0iGB55CRTqYBp2rRparGohcKAI7pQEf2Tme6XaFOcN231ukuodXk5v_bKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/69340" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69339">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس لیست اهداف انرژی منطقه رو منتشر کرد:مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی؛
❌
میدان نفتی غوار در عربستان
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
❌
تأسیسات ابقیق و خریص عربستان
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
❌
پالایشگاه الرویس و میدان نفتی زاکوم در امارت
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
❌
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
❌
میدان نفتی برقان کویت
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
❌
پالایشگاه ستره و تأسیسات المعامیر بحرین
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
❌
میدان‌های گازی لویاتان و تامار اسرائیل
ویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69339" target="_blank">📅 02:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69338">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWQ29HRBg2z_Mw4KjL5ZfryP8yLHViGyhftSRAaouPLohKcXCmw2kYOIh-BsWkOSihQEL8TIVQ06kQkEV3KEcS0ZGcRIYV1YtwyZAMcCpkjTPf0OrogLpeJMu9jukaibvjkl44zKehvEyiFdQpg5wARB1hz721fL3ZLhVlbH06iVY4qpLzcAkjT3gL0uAVj0hm8Yj3NkwKKpvGYp_En9OaXVnJA7_8nB51t-PBiiSoPzuJoBuUkyCFny1z9RbHmh_7jFz4QY_YshHgjTMGVebIR9jCFd893jUWlEGpqOXCPuwJQhk_6tz9DIs7BG-ETCduP23fGzagKSPstPLobh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:یه مقام ارشد امنیتی به ما‌گفته؛اگه آمریکا یا اسرائیل بخوان به زیرساخت‌های ایران حمله کنن؛
ایران از قبل یه برنامه گسترده برای جواب دادن آماده کرده.
به گفته این مقام، توی این برنامه، زیرساخت‌های حیاتی اسرائیل و تأسیسات انرژی آمریکا تو منطقه هم جزو اهداف در نظر گرفته شدن.
نیروهای مسلح ایران توی جنگ 40 روزه و اتفاقات هفته‌های اخیر نشون دادن هم توان انجام چنین عملیاتی رو دارن و هم برای انجامش اراده لازم رو.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/69338" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7lHQXPE7qKFL0HhEJRxcvfFziZckvIFNzPAgfmoiej3hdAatRjjD4TSqyz2U76QudfbRnIGTbVFNhYbktPVob4TutvcBed0TvocL6P_DxXv1bt3vFBB790PineDaVkuhwEtxp5kkf7tNjKPYOP91SavAr3StiEVAbS6Ik0YJT5VgItc93cIIT9lpaLLR9fXXxpd05VcQs6jJLuH7tC_8L44_kMFn12cyHDCI0jV3FEYUutlWdC-k9RcQigvglytQdQIZLdi23di2FY9hwClmVj3iFm8MPoDFo5jjNPDWPfD292LhYNyTBHEEoqOv6hQDYojZwtPJgyl5nf5eHsNsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛آکسیوس:ترامپ در حال بررسی حمله به تأسیسات انرژی ایران ظرف چند روز آینده است.
یک مقام آمریکایی روز جمعه به «اکسیوس» گفت که رئیس‌جمهور ترامپ به‌طور جدی در حال بررسی انجام حملاتی علیه تأسیسات انرژی ایران در چند روز آینده است، اما هنوز دستور نهایی برای اجرای آن را صادر نکرده است.
این حملات همچنین ممکن است برای نخستین بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدید تنشی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین بار درباره حملات احتمالی گزارش دادند.
ترامپ در آغاز جلسه روز جمعه کابینه، با اشاره به حمله احتمالی گفت: «خب، ما ضربات بسیار سختی به آن‌ها وارد خواهیم کرد و می‌دانید، بالاخره زمانی فرا می‌رسد که آن‌ها خواهند گفت دیگر تاب و تحملش را نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69337" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69336">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh6iPzDhPdwlduq07g7itP38E8Ac_7vc7XMh7-VLJrcqiZOdNzAD_li_JdygVvKTDTFkBzYvqI8ao4HLIcH9h3ZxF0aH5uU5SASFnXVoVjOknPI3uGBAqApCMv0O0-t7Fa3O66337dY-0_DtBLPyPuArKVrbtA4zJsbmZ_nwTAXrXJAwsfzBBUKKRyRG7g8YeX5Gp_6tjF8JwuGJ0mGaUlPiCbWa3RwFFsFOAiW_r1BZQHUGW68K_Ip9FbQJDCOnbNZERnIzPAZN7Bro2-pGC4dlF-P4ckw2JSnqAiDouPuOe0HNhtY4uV5yiSPjjeWd3YvkP_IrzUUNU1g2B15Row.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
سی‌بی‌اس نیوز:
ایالات متحده و اسرائیل در حال آماده‌سازی یک کمپین بمباران مشترک بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده است، اما حملات ممکن است این آخر هفته آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69336" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69335">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5040574e14.mp4?token=SH7JVFr2wPhWBiSL2IQfVV0QOVFlg9bVaMA3Rid1L9f8izYpnvj-u8wZc98tUVixCnVU6bHFyjNFqbRC8QZoUIROG9Rk_4wyowVgkAaTbViLEdbW8H7Bj7BwYHgNz-VMWtZB9BzhhunKMBtkUFxVbPeEb7tUFZxKVh27ST2IuRrOvrdRYO3bQfuDTNI0IoFgDe_fgsUgwsyV7dWUa8LfJguo11dMIbdYJBThyl1PL1BG6zb9qjVgKWtpI4L2fORSsv2mWuq8je8j9m3W76BAXnMsaCgcZcFcYjoIJ9Dlpn3RvsC_URbzdzzk7eAq2xmdYdUHVRDA_N-er84E0pbAIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5040574e14.mp4?token=SH7JVFr2wPhWBiSL2IQfVV0QOVFlg9bVaMA3Rid1L9f8izYpnvj-u8wZc98tUVixCnVU6bHFyjNFqbRC8QZoUIROG9Rk_4wyowVgkAaTbViLEdbW8H7Bj7BwYHgNz-VMWtZB9BzhhunKMBtkUFxVbPeEb7tUFZxKVh27ST2IuRrOvrdRYO3bQfuDTNI0IoFgDe_fgsUgwsyV7dWUa8LfJguo11dMIbdYJBThyl1PL1BG6zb9qjVgKWtpI4L2fORSsv2mWuq8je8j9m3W76BAXnMsaCgcZcFcYjoIJ9Dlpn3RvsC_URbzdzzk7eAq2xmdYdUHVRDA_N-er84E0pbAIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مهاجر مراکشی درحال رفتن به منطقه برون‌بومی اسپانیایی «سئوتا»
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69335" target="_blank">📅 01:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69334">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.   مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69334" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69333">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQMQFNbbmuyn5It6LttqdteVTwTKCG-w26gU5jT7pNz3xIYNdC7BIVMybMleVphQpoo3sB4PAAwd3PENK30M5SQCELb6ys0g88mPY-iefrPW8fcTSXUus0K64j2qEYyn5dh9cvuRG4GDTGM_KsNfv2jA8Li9CaY5-3bD9VYTOPcBZUAvBbbYH14yBrnxpRnAPH-yQ02EfL5OPW3L_Nd9d_7lxkdBV94hn5gTSYVhN--oxgNp0QQ6jLc6n4Ck55TOV0wY-qhL3cnd71OTL_fYaAVSd9xz9CrAxjbVlqVukAcyGLvShiulBhJ7DUk6b2VR_qsCpxeAZHOcbf43w_ukoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.
مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند روز به طول انجامد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69333" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69332">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">چندین منبع به CBS News گفته‌اند که حملات ممکن است در طول آخر هفته انجام شود</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69332" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69331">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=Jv1ted1NckymnvPw9h5hsSRTepCH6f6Ofk0MfLoUvWWLJZTjDnf_zgJGIORhdkqYc3w4DxSE8Kv-bRVDB7quZgje__qBNHRSLRD-bjyXSJuEQC6rTb4w4qMRdEA_A1XwcUXstUUmB-7KwW490M9x0P9tsin2muEisrHnizy-9f5lyqe-KF47UBkvRBRfQ8ma9k8qMdkCuackarbiXx4D5bNmTXMuEW5zPn86L5FKYbSSzzirF82KpFGmNPZAjmciXTk-pTLW7TKnM2hz6lmovAGzq-BK-sWeYAjdPy9Jg_E4ng2PqCDhFnP01UFeBTOFKV9goO_Q9rxjdsDeUowGyS3Tqlz2-ECj3AUo1Wo-mNIgnh5QKi80xcttXec3Y5hZ3hUOQA0COtxheFMfjVRmwX-oFeTO8YL6E_27_22ac9UYHmLGNOKYeMEl8s8znXzaUnv0oBCgzxUN0bQtMN691I3Bfxb9qN_eeO9WVB1IZCtuLovxXLJLyOTN_hf_OePdTZUv8-BLhXMoQtLCnlu02wBSKXPtUjfBGP-X1fmGDWzX9y-TFP5G44QOa1_rSUZGBa-MN8QTPpeoPzt4IAeFEcmIEfDWeCZqGfQYZiuRfiJv2NxFUckCFwp-D22yIxgQugR563TKpQF-PhWoWapLR4HMcN6cOkZ93W_75RcDWX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=Jv1ted1NckymnvPw9h5hsSRTepCH6f6Ofk0MfLoUvWWLJZTjDnf_zgJGIORhdkqYc3w4DxSE8Kv-bRVDB7quZgje__qBNHRSLRD-bjyXSJuEQC6rTb4w4qMRdEA_A1XwcUXstUUmB-7KwW490M9x0P9tsin2muEisrHnizy-9f5lyqe-KF47UBkvRBRfQ8ma9k8qMdkCuackarbiXx4D5bNmTXMuEW5zPn86L5FKYbSSzzirF82KpFGmNPZAjmciXTk-pTLW7TKnM2hz6lmovAGzq-BK-sWeYAjdPy9Jg_E4ng2PqCDhFnP01UFeBTOFKV9goO_Q9rxjdsDeUowGyS3Tqlz2-ECj3AUo1Wo-mNIgnh5QKi80xcttXec3Y5hZ3hUOQA0COtxheFMfjVRmwX-oFeTO8YL6E_27_22ac9UYHmLGNOKYeMEl8s8znXzaUnv0oBCgzxUN0bQtMN691I3Bfxb9qN_eeO9WVB1IZCtuLovxXLJLyOTN_hf_OePdTZUv8-BLhXMoQtLCnlu02wBSKXPtUjfBGP-X1fmGDWzX9y-TFP5G44QOa1_rSUZGBa-MN8QTPpeoPzt4IAeFEcmIEfDWeCZqGfQYZiuRfiJv2NxFUckCFwp-D22yIxgQugR563TKpQF-PhWoWapLR4HMcN6cOkZ93W_75RcDWX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«قیمت‌ها حسابی اومده پایین، به‌جز نفت.
دو هفته پیش، وقتی همه فکر کردن توافق نزدیکه، قیمت‌ها مثل سنگ سقوط کرد.
ولی ما یه
توافق واقعی
می‌خوایم، نه یه توافق الکی.»
🎙
استیو گروبر:
درباره ایران، فکر می‌کنید چقدر طول بکشه تا این ماجرا تموم بشه؟ یه ماه؟ یه سال؟
🇺🇸
ترامپ:
«پیش‌بینی کردنش همیشه سخته.
ما ماجرای ونزوئلا رو توی کمتر از یه روز جمع کردیم.
اگه می‌خواید همه‌چیز خیلی سریع تموم بشه، کافیه به یه عده سلاح هسته‌ای بدید!
اون‌وقت همه‌چیز خیلی سریع تموم می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69331" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=W5KUXZGiyEahOEexxHfoWgFUpNhHJzvcSjfEZUuwafcc8uNBxOJT579EwuZk-hyy8cTL2z0Su-hAAKc5_dwQVYk3XmzP8nsyZuM2Lw5AJj3Q6cjKj4etmhznfjALtHEzCjtoAjO1t6kGCzPMQ1nBKbhStdSmQhzxpXLiMpvkDkMK_DboDnzHKeFLk2qMu22hPWyligrMCrkQjaLkh9YE6E58kJf798bYMRHHXYtvVV_VJpxvux0_pJ5ws6dGllBQPRh2FwQNpKVqQ2iXqkrCj63HezVdP7bTe-2oZV-cyypwCZM4Ni7X9wb2UD3ej4IKIlMQndOyNP96lCljI2bzCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=W5KUXZGiyEahOEexxHfoWgFUpNhHJzvcSjfEZUuwafcc8uNBxOJT579EwuZk-hyy8cTL2z0Su-hAAKc5_dwQVYk3XmzP8nsyZuM2Lw5AJj3Q6cjKj4etmhznfjALtHEzCjtoAjO1t6kGCzPMQ1nBKbhStdSmQhzxpXLiMpvkDkMK_DboDnzHKeFLk2qMu22hPWyligrMCrkQjaLkh9YE6E58kJf798bYMRHHXYtvVV_VJpxvux0_pJ5ws6dGllBQPRh2FwQNpKVqQ2iXqkrCj63HezVdP7bTe-2oZV-cyypwCZM4Ni7X9wb2UD3ej4IKIlMQndOyNP96lCljI2bzCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توی درگیری با ایران، بسته به اینکه چه آماری رو حساب کنید،
16 تا 18 نفر
از نیروهامون رو از دست دادیم؛ که همین هم خیلی زیاده، چون حتی از دست دادن
یه نفر هم زیاده.
جنگ ویتنام
21 سال
طول کشید. ما تازه وارد
ماه پنجم
شدیم، ولی همون‌ها که آمریکا رو 21 سال توی ویتنام نگه داشتن، حالا می‌گن "چرا ماجرای ایران این‌قدر طول کشیده؟"
من الان دارم کاری خیلی بزرگ‌تر از چیزی که اول گفته بودم انجام می‌دم. قرار بود فقط وارد بشیم، توان نظامی ایران رو نابود کنیم و برگردیم.
ولی بعد دیدم اگه فقط این کار رو بکنیم و بریم، دوباره خودشون رو بازسازی می‌کنن. برای همین باید یه جور
کنترل و نظارت
هم وجود داشته باشه، وگرنه دوباره همه‌چیز رو از نو می‌سازن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69330" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=vpeGMwv53HQhGesQIAO9U8eFWUUyYHkpS61dbBVHziRAPt7KZy2N4wVYVbDL7JBYEVR0D8jo9zNuxFvtEOtXqjQOlBZcuChxXet26AjOii6pAUJyTxDPFgzeUGICGUkB1JrHWQ2d2skSboNzf4OgT8O6rkbQmb8Yjx6FhuOZfWWUqHekgpotjh1dF-oynomIVraufQLmD8fUzd9JXsUreUbPMVoLrDKgxt-QdQJ13Q7AuET1U6YD_dYl9I4K_J3udJrit0MyBCeitxRfVj-U2d_QZ8hD1ceuMAWW2zY7HJeIB1e1xWMoTs-QCDua2ti6uDSbAguuysXmsqFHXlH5uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=vpeGMwv53HQhGesQIAO9U8eFWUUyYHkpS61dbBVHziRAPt7KZy2N4wVYVbDL7JBYEVR0D8jo9zNuxFvtEOtXqjQOlBZcuChxXet26AjOii6pAUJyTxDPFgzeUGICGUkB1JrHWQ2d2skSboNzf4OgT8O6rkbQmb8Yjx6FhuOZfWWUqHekgpotjh1dF-oynomIVraufQLmD8fUzd9JXsUreUbPMVoLrDKgxt-QdQJ13Q7AuET1U6YD_dYl9I4K_J3udJrit0MyBCeitxRfVj-U2d_QZ8hD1ceuMAWW2zY7HJeIB1e1xWMoTs-QCDua2ti6uDSbAguuysXmsqFHXlH5uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه هموطن که تو خونش کره خر نگهداری میکنه و بردتش رو تردمیل تا دلتنگی بیرونو نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69329" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXk1itqMaVm3o8CBdTqlkSC06THVgXuYb8ONC1DeiHRl4UY9NRJHGoygdf1jWk-wVXY3AmIsQS95OK2N168PUZVmOgAov2AeQwQYpnQK9RJSn4OG9hFWrtZRJl04rcs4_UgLMupowA7yFznAhLzob75dtdg-KtvdOu7bsc4JLDuzM96O3jt8XW0ZJytIExm64OKWymxl-8SOVtI8nbtUWzLJ3TQzAuPqUG6f2mlQRG40W5s45vfPXyVNQUh_fSfCgti5GNoVryOcQDZBuJ4ToaHuuvFPGKUlRZXTjHlXzDJoWdooUCWpnE3xw5XHO66IsnNsdaEfJVkyc6OSpnJKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=ppQqpHC5xYGw14vLcFyJSmrIx0NSGZE5U7I5aZf0ublpv0ZM0dtDki_kfRsRTuEyDfSjlSVtT12NrKvv1-9YT1buAcn6InmNIMV-XBGaXwr-Rt0Qh8kC2G7reDObkMOOLRhOpzRKgPb18PXVcxsvNT0i4ToclVuBYXbVViT4JyBiph7YCKKIWliIHQshiQdrxaWv_XRET8kO2h9eewb3PUedOtE7vx2iSJmP5wT9ZvcvTqKkKGz_AjUrQVYHStVWfLOjQSki-5XrsO5GMP_73s8YNE-LK3vpKoHEF6wEBymYbvWKRWN3UhKeDNTCVsBb9SB8wNoI4V9c2-Gd8XPJqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=ppQqpHC5xYGw14vLcFyJSmrIx0NSGZE5U7I5aZf0ublpv0ZM0dtDki_kfRsRTuEyDfSjlSVtT12NrKvv1-9YT1buAcn6InmNIMV-XBGaXwr-Rt0Qh8kC2G7reDObkMOOLRhOpzRKgPb18PXVcxsvNT0i4ToclVuBYXbVViT4JyBiph7YCKKIWliIHQshiQdrxaWv_XRET8kO2h9eewb3PUedOtE7vx2iSJmP5wT9ZvcvTqKkKGz_AjUrQVYHStVWfLOjQSki-5XrsO5GMP_73s8YNE-LK3vpKoHEF6wEBymYbvWKRWN3UhKeDNTCVsBb9SB8wNoI4V9c2-Gd8XPJqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=G7HQJSjJuUVAyW9zSVnhH6kt_DBxQR21bgtWE1A8MehMz-Zh07qBz6oZhjlcJCJuWfotWBNAZL16qcTRxf3dgx8AVYebDNpJKKTFuqAtbRM5EJ5u2MjyFeRgwCLwYWEY2QSCTHyYEpFTbdUIPblqyzZjrfBRB3Pvf1CaJeWRTDCzG9Ptpe076Lh02hfm-9B37uZ8B_5vT2IAgiXgJA1UA6M-Y7J0UBZ5a6Pl6sOW9OZbIBSJvp9Im2k33RsbW9snUF16_Ofa3Ni32AJj1oK4DncuAsM22_lhw4SgG6NrxUVZTuI5W8w1Lf4M7gi8krifg4t3hJcbE03FJ2Tl8K0giQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=G7HQJSjJuUVAyW9zSVnhH6kt_DBxQR21bgtWE1A8MehMz-Zh07qBz6oZhjlcJCJuWfotWBNAZL16qcTRxf3dgx8AVYebDNpJKKTFuqAtbRM5EJ5u2MjyFeRgwCLwYWEY2QSCTHyYEpFTbdUIPblqyzZjrfBRB3Pvf1CaJeWRTDCzG9Ptpe076Lh02hfm-9B37uZ8B_5vT2IAgiXgJA1UA6M-Y7J0UBZ5a6Pl6sOW9OZbIBSJvp9Im2k33RsbW9snUF16_Ofa3Ni32AJj1oK4DncuAsM22_lhw4SgG6NrxUVZTuI5W8w1Lf4M7gi8krifg4t3hJcbE03FJ2Tl8K0giQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUVBrwJwvItfhBxOzHC3vBF6I9kA75xgRWTImU1cvbzisGlt9XIBiTTtSAvKvtg_CZH9E1d7yrj6DXL34Q02GnkIPY8q8CY9v9aVz9d6WsvtxI9e3S7r4DO53dq6xJlXLbMj4yheIoeZ7LeYVPMBz7SjtubyqgDVZdaPUcl93WmQmXrzRRpGV3t8sSZnSAnYG_Axrw4KBqgiHfoacpcB_hxNTtLVayBzDhy-sFdJ6Lumd1rJtYfnZCh5FFqgsqxV5hldTrMFH9vAaKKEXkRYUKVOZgo2uNjRCgR6Wf9AZAz-iv_--vusLWzql5XwEWdi7K9uBIkxAUFNTSbtWMnoj8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUVBrwJwvItfhBxOzHC3vBF6I9kA75xgRWTImU1cvbzisGlt9XIBiTTtSAvKvtg_CZH9E1d7yrj6DXL34Q02GnkIPY8q8CY9v9aVz9d6WsvtxI9e3S7r4DO53dq6xJlXLbMj4yheIoeZ7LeYVPMBz7SjtubyqgDVZdaPUcl93WmQmXrzRRpGV3t8sSZnSAnYG_Axrw4KBqgiHfoacpcB_hxNTtLVayBzDhy-sFdJ6Lumd1rJtYfnZCh5FFqgsqxV5hldTrMFH9vAaKKEXkRYUKVOZgo2uNjRCgR6Wf9AZAz-iv_--vusLWzql5XwEWdi7K9uBIkxAUFNTSbtWMnoj8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=WCoK8amzfKwice_gIVbB-qnZxyYsNBaF-UzlQodkVpUqYECwXVJS-ibF0uxQjZ45oqpLsnHWg1XiQ3_flbuwJhFIgzcAHNb1eRZiY1SiY4FxPucxBxAHRJR9e-rfKXQP0FCuseCV9fPif9j_sgoWvT1s89F5gySAi8ftkHCr5ShRwhj6D1IE2iT3N5me2gwOtRhrHDxqzC_u8K-bfjX2I0FtNhb0tNybZTZPZrxXdsjpPN2au__0eccBEt-tvRpfwpaV4mqFGSPja4OqkaALasM2205l7NGON3npIjkihQ9a18rllqVNg_GPfapkmQR3qaLYvV-DACeD51pEP48lODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=WCoK8amzfKwice_gIVbB-qnZxyYsNBaF-UzlQodkVpUqYECwXVJS-ibF0uxQjZ45oqpLsnHWg1XiQ3_flbuwJhFIgzcAHNb1eRZiY1SiY4FxPucxBxAHRJR9e-rfKXQP0FCuseCV9fPif9j_sgoWvT1s89F5gySAi8ftkHCr5ShRwhj6D1IE2iT3N5me2gwOtRhrHDxqzC_u8K-bfjX2I0FtNhb0tNybZTZPZrxXdsjpPN2au__0eccBEt-tvRpfwpaV4mqFGSPja4OqkaALasM2205l7NGON3npIjkihQ9a18rllqVNg_GPfapkmQR3qaLYvV-DACeD51pEP48lODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=EV0Bdw8Kn9-FXOcHtc4FCx9FQNPegxE2exNLb5EPav0MbsMuFkn7eYjva_B3-qtvaExou0KlYBrHQ5C69nfHZXByiX6X5d-gAe8p2huw-qkz_JQ_TFpxzMP0lnN8hj4j-wqCrfUC9pXwyaEo502chBhYqHhP0nM5aus0Idd4DtIHrqe5YBRl7byDqk2qIL7g8hOCW7DbV4MmnwSrWX45Jo2Pb2WPT9k8U44V-USU3lL2vfEkVp1qsUoIuwfvVBLrCg__IKf_9F-Gc319xi9HpQM9PSuEkKrF14ye1mJPkWwLCm4TA8keigALnRcW_fnjm1cZS5KiPy5bwf0EXHD5Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=EV0Bdw8Kn9-FXOcHtc4FCx9FQNPegxE2exNLb5EPav0MbsMuFkn7eYjva_B3-qtvaExou0KlYBrHQ5C69nfHZXByiX6X5d-gAe8p2huw-qkz_JQ_TFpxzMP0lnN8hj4j-wqCrfUC9pXwyaEo502chBhYqHhP0nM5aus0Idd4DtIHrqe5YBRl7byDqk2qIL7g8hOCW7DbV4MmnwSrWX45Jo2Pb2WPT9k8U44V-USU3lL2vfEkVp1qsUoIuwfvVBLrCg__IKf_9F-Gc319xi9HpQM9PSuEkKrF14ye1mJPkWwLCm4TA8keigALnRcW_fnjm1cZS5KiPy5bwf0EXHD5Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=r7cRMtTeCWbZJ4kZWDh2Z3ct1NnaUcXOcEulVJJ6NYocBzr8menBqWsl1QzTm0OK1-aUf1loxYh16Yetu2_UOxe8y0LcOS9P7Yu33Shxmm7CmlzWJT8Kcb52gIMSjhfru4T7TZeEtcBBRsfzBM6eLBQnynmeFgUJFA45cOLIt7yNYsIYqYvFQPD-pEv2NWHoSt7CIuNokzewAMvHAGS8vO2SOv-afDC58fKvlv-sorMa9Ng06aAP2ik0krKIg-QEjF9AOgxPpsR11GXImdta7khgFXp4MiYEiYZpi5n-A5Uah66Bt64cxTZgftR60lxTKsO24rsnn-7BFfnw6aiXQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=r7cRMtTeCWbZJ4kZWDh2Z3ct1NnaUcXOcEulVJJ6NYocBzr8menBqWsl1QzTm0OK1-aUf1loxYh16Yetu2_UOxe8y0LcOS9P7Yu33Shxmm7CmlzWJT8Kcb52gIMSjhfru4T7TZeEtcBBRsfzBM6eLBQnynmeFgUJFA45cOLIt7yNYsIYqYvFQPD-pEv2NWHoSt7CIuNokzewAMvHAGS8vO2SOv-afDC58fKvlv-sorMa9Ng06aAP2ik0krKIg-QEjF9AOgxPpsR11GXImdta7khgFXp4MiYEiYZpi5n-A5Uah66Bt64cxTZgftR60lxTKsO24rsnn-7BFfnw6aiXQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=cT3thCzfMd9g_iU8skLsj3NIa_2mgFXa9D-UfZNtX1euqhPDya-1uOjZkUAV1xZJLt5gsINjPlxByi2jxK3UaPKS65LTTXsB8nfL7IUHvujvTDeTfE92fzHC-cLeY5G55QLYpvHtAK3_xZIB4IONFbD7e2KE5NY1ZQidHhH3NQVhM3gKmdOLdkJUv0d7IDcPeKyL1o5R6QaWkxqF1G7zER6qqzhFzP8yF0BRPuOIRDi5CSdK9jrOYi1AuuP9WEPRMuNPIhWCarbjQ6Pb17mNCZ84Orjbr4svqRpUDgBgUGbDIH5116Yz7gdgYQ0YeougnGDsM4th6dcv9S1PuVh1og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=cT3thCzfMd9g_iU8skLsj3NIa_2mgFXa9D-UfZNtX1euqhPDya-1uOjZkUAV1xZJLt5gsINjPlxByi2jxK3UaPKS65LTTXsB8nfL7IUHvujvTDeTfE92fzHC-cLeY5G55QLYpvHtAK3_xZIB4IONFbD7e2KE5NY1ZQidHhH3NQVhM3gKmdOLdkJUv0d7IDcPeKyL1o5R6QaWkxqF1G7zER6qqzhFzP8yF0BRPuOIRDi5CSdK9jrOYi1AuuP9WEPRMuNPIhWCarbjQ6Pb17mNCZ84Orjbr4svqRpUDgBgUGbDIH5116Yz7gdgYQ0YeougnGDsM4th6dcv9S1PuVh1og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=K8IvaZmIS0xg-y3_Y6MwLfWnTGAeG1no0EosFkmWNOvQ--48mDmDQzHzWNHdt2BMhX-FUxMprBEzLh19Xn1szEhH4dmxF5D9JyBIUGLt2FUn6Yo180bLknNzpIpjiSwFr6sQG32SNrcU4iLQ4REaw4E7ekIDuoxc0Y-GIZWqe2a6LgbOmHh7NavxMPijyLFhTvysuO0eyu1PGPY2pWo1Xi9sZnuVRISW_zdNUwaTCprXmswtxs_kP6utNKhF6-HstqUcuwTvIEgm4jKsjLssErQPAwPNokwTnF2wvRO2YW4s9m7faldrteSrQEym8LdQ0Cv7fd7sNN62Zqrl-yPcFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=K8IvaZmIS0xg-y3_Y6MwLfWnTGAeG1no0EosFkmWNOvQ--48mDmDQzHzWNHdt2BMhX-FUxMprBEzLh19Xn1szEhH4dmxF5D9JyBIUGLt2FUn6Yo180bLknNzpIpjiSwFr6sQG32SNrcU4iLQ4REaw4E7ekIDuoxc0Y-GIZWqe2a6LgbOmHh7NavxMPijyLFhTvysuO0eyu1PGPY2pWo1Xi9sZnuVRISW_zdNUwaTCprXmswtxs_kP6utNKhF6-HstqUcuwTvIEgm4jKsjLssErQPAwPNokwTnF2wvRO2YW4s9m7faldrteSrQEym8LdQ0Cv7fd7sNN62Zqrl-yPcFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=p5h6HFPJ-h3qurqFbs5tXVHmCsbUpNGYUCIYg2LMWDmpIcDsVYFvDfqn0xFviyj9Mtbirz5E0VWDp4eWBAosfcLJJ-FeTpjuSv8kPn_dECko4ePhpRtGkGCUGA8puerxUYsrMmIlyb0-FoHtNj-4VpzQsdDBwNCasm7URLdwgIHYtTha4qZ7zQnlTyOoC7xkjI4z_lv7fwFMVNWvjjFmGHy1rQ7vGjnxgxMo3ks2clhJSTTsa2HF4QFUKZE3vGGWDo8lmXRZVb2cLDoQWG1_ns51kvSWoIZji1KaJvxffdTmgHBbO9kr8FQp5dqmzx52vIfD-rknF5JAgrEvDg-DKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=p5h6HFPJ-h3qurqFbs5tXVHmCsbUpNGYUCIYg2LMWDmpIcDsVYFvDfqn0xFviyj9Mtbirz5E0VWDp4eWBAosfcLJJ-FeTpjuSv8kPn_dECko4ePhpRtGkGCUGA8puerxUYsrMmIlyb0-FoHtNj-4VpzQsdDBwNCasm7URLdwgIHYtTha4qZ7zQnlTyOoC7xkjI4z_lv7fwFMVNWvjjFmGHy1rQ7vGjnxgxMo3ks2clhJSTTsa2HF4QFUKZE3vGGWDo8lmXRZVb2cLDoQWG1_ns51kvSWoIZji1KaJvxffdTmgHBbO9kr8FQp5dqmzx52vIfD-rknF5JAgrEvDg-DKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=rbh0zvpl9ThWI-rrtsq3kSF_QPRcaveSIBCXFPO2YjKtg8c5w-Ws6lIB0samv3jK3-k_Dr_OsFeoqfUazvC5kBSbqSb1n7Na8xHBHGgnB545YnvOESz7T9axGYHxfDxTRJ2uLsLpylCwdkQyIxI-OUMmYRDvrVSCOGi1M3nOlLUpSgJy2hRpgWZK3ATL0N0V-dlsznGUc148_pg5B0S71GIodHz-AB5qIdU1CNx7BM_Y6d5HKSNe8IHFQ96h33wgskVdbMRKktCvEnx8vUmevgzkEG0iVNkKza7ad55-OhyVUXDrmv8zsrvdpnmlyDze_pj92uXB12kVpZL9SKkRUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=rbh0zvpl9ThWI-rrtsq3kSF_QPRcaveSIBCXFPO2YjKtg8c5w-Ws6lIB0samv3jK3-k_Dr_OsFeoqfUazvC5kBSbqSb1n7Na8xHBHGgnB545YnvOESz7T9axGYHxfDxTRJ2uLsLpylCwdkQyIxI-OUMmYRDvrVSCOGi1M3nOlLUpSgJy2hRpgWZK3ATL0N0V-dlsznGUc148_pg5B0S71GIodHz-AB5qIdU1CNx7BM_Y6d5HKSNe8IHFQ96h33wgskVdbMRKktCvEnx8vUmevgzkEG0iVNkKza7ad55-OhyVUXDrmv8zsrvdpnmlyDze_pj92uXB12kVpZL9SKkRUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=IYUBdSWLoYbnN1aaWJb_b-g4YoQh43KraozN3YglwvMSp3XvME8ioHA9OfPaYzoZ00x64BPAOTresDjS3lhTWgy4KGIRgqjpqPTSlVX5hAEXEE7H7OAftXn67ou7vDmV0iM8hdJ7S8USwAcb-eIGlEj7BVDPKwuHcph_7ZKcN_ImEfbMCOBqJPSw0CKrFtakmI-dq5wkFCYouuI_hSLzBaKW6BWCpknPEeSV7G07U7rk0mY5dyinxxSOKFenvva2RMmgUTp-wrUOmXWS3lqRNx2YmxQApniZLeePRKP4Y51BkVIOT34MkaThG0_P3yAypmhOoI4025HBAWY7HAy9zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=IYUBdSWLoYbnN1aaWJb_b-g4YoQh43KraozN3YglwvMSp3XvME8ioHA9OfPaYzoZ00x64BPAOTresDjS3lhTWgy4KGIRgqjpqPTSlVX5hAEXEE7H7OAftXn67ou7vDmV0iM8hdJ7S8USwAcb-eIGlEj7BVDPKwuHcph_7ZKcN_ImEfbMCOBqJPSw0CKrFtakmI-dq5wkFCYouuI_hSLzBaKW6BWCpknPEeSV7G07U7rk0mY5dyinxxSOKFenvva2RMmgUTp-wrUOmXWS3lqRNx2YmxQApniZLeePRKP4Y51BkVIOT34MkaThG0_P3yAypmhOoI4025HBAWY7HAy9zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmuTjTzr9f_QpAeVluqmrqFjwfxiWgcilaJ6ENQkeYbV5VQCCHS2uQhmoSNbPpAbSodzCav2q9q1JKhNWU98-Bpo7_bqVU9gcDszDg7uW9gruAjJ07dUoadCbJJcfMMp8n-Y74oEkE7ll8o92M5SyUwUhFjXASRrAyoP3r-T8lYfrA5lDW2abkTxoGNz96YJpAtllbGIwWKhqBieblm7eHWQcFiPFxTg9tVQSRx9LfkHpd_tuddkZmaDfVjibTZ_EI6EU6uvZypjtOvEpwcXRo64T4LAyWpMGecO2MOEZIzCbZXWIv8SyJS68QA-lFZNwLYs9FTBuc5a2RI3qeTYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=CJivoSzLY7TDX9tCRdoHU3JG4cqxY7Zj7t8Fpj-fu4_EGxgPIrMR0mhzjpWbxL8TmqakaYZ9pDyh6xxXMZz9DCkkay-R5JQl6JR9z5OuS7N0wCBywteHWl953fpcEJNJwdF0TIVrW7DKfMEJnVL-q6DFolm4M8bpW7yebaMEToZyV8v1grzNOSbVEReZs-SA18OVcM6ZMtnB-95HMGvjUZ8SB5j-OFtvLOAakWAW_ZijVzuDG-4YyvixWDd71zx_zZ6XaTo6Dw4Y1YJeKmF2FvUf5ULnqd8lyFOjHeOV3nsoj6Cqyso2ydknyM5ix8vYN9A-O6C8lI7bFXJcqf5_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=CJivoSzLY7TDX9tCRdoHU3JG4cqxY7Zj7t8Fpj-fu4_EGxgPIrMR0mhzjpWbxL8TmqakaYZ9pDyh6xxXMZz9DCkkay-R5JQl6JR9z5OuS7N0wCBywteHWl953fpcEJNJwdF0TIVrW7DKfMEJnVL-q6DFolm4M8bpW7yebaMEToZyV8v1grzNOSbVEReZs-SA18OVcM6ZMtnB-95HMGvjUZ8SB5j-OFtvLOAakWAW_ZijVzuDG-4YyvixWDd71zx_zZ6XaTo6Dw4Y1YJeKmF2FvUf5ULnqd8lyFOjHeOV3nsoj6Cqyso2ydknyM5ix8vYN9A-O6C8lI7bFXJcqf5_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsXHRYOOlpUYPgaeV43_XWQ7vAUZ7QCopbyJr21fEioSUVesDuq9toswSsBl9xyBPxnbb17xsYtbBIeFHlbyWfw3SXBpu6BvDVySw-KrKZP275xT575Tk1y-DUh2G8b-10jCl6iqN9lRz33ibvH9uW85xVko4zY609G199j4QRjwKIzksao9JK2IJO8WItZJWH7GhpMn5QYSuDwQfMKYZHPIYPnvd8SkN9mWlHJ93WEUsu7ALkyuXuD1rD6bhLBj4DBy2yW-ZhoS1mn6e6AkTVExvIORikBGmPU3sG5TeBydW7nNDBnzCYv0wO1NOoFHvmJeporo-9wIghMYHM8oew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=dBQoE7n5smGblSwSBM4Qh-pP3-xOwVNf4ttkOHrdEmD_luoNcEEEIik_hlm-ZN55aUeodFKWgE_Y5bQHXRTIxhjRut5qdMQPUcSqdmmsKlU5BE54cEg7KZw7U-BI2A4_0sZoW1gjPrr4KP25teXgNZeMIgsqQwh5mR9ChbbxDfrTsfZLi4yoduJ6SnYCdZHre_4DyHFSRLonlfvU-JbCd6kDQXZFPE33SRAnceDLxJgA-4TdzHHvo2rkHw7BQFbAE5gSuYULcf63k0cHSdnZ4TCSYRXTqliNTaNhPAJvW2LlKZRyocUvTX3Skl610lOMu9RI8Hw34eQQ_UuKExpKqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=dBQoE7n5smGblSwSBM4Qh-pP3-xOwVNf4ttkOHrdEmD_luoNcEEEIik_hlm-ZN55aUeodFKWgE_Y5bQHXRTIxhjRut5qdMQPUcSqdmmsKlU5BE54cEg7KZw7U-BI2A4_0sZoW1gjPrr4KP25teXgNZeMIgsqQwh5mR9ChbbxDfrTsfZLi4yoduJ6SnYCdZHre_4DyHFSRLonlfvU-JbCd6kDQXZFPE33SRAnceDLxJgA-4TdzHHvo2rkHw7BQFbAE5gSuYULcf63k0cHSdnZ4TCSYRXTqliNTaNhPAJvW2LlKZRyocUvTX3Skl610lOMu9RI8Hw34eQQ_UuKExpKqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=EI0auyaRKEFckshP2k9Ver8Yx7di4M8qGjkRZBqLjRuSe3-GfLDCsWfeNsIyYiejifPWXdorL98NEm6bf7DZKhkvBST1kvW94TpmC-xJia9EjD7C03luLWowxWIEP6OTYFRTTqBDZc8aCRPR_463J_ZM6WZaEvdDZwvNGo5fFOrbiBrWrSXIHMHLIU9YoKRbwwmnwLsaGZUQL4T2RteyoPFpejYW90NQGktCXoFlzY9v2926sQoK-4tC1sqJ4Plnlf9bKP-yM6f6vw0wT7deBgq_TY_kqciTB259gH-UQ_g-hrzXb3uFxujum88gFgvqSYtKA6JqFKEXNYATRKLMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=EI0auyaRKEFckshP2k9Ver8Yx7di4M8qGjkRZBqLjRuSe3-GfLDCsWfeNsIyYiejifPWXdorL98NEm6bf7DZKhkvBST1kvW94TpmC-xJia9EjD7C03luLWowxWIEP6OTYFRTTqBDZc8aCRPR_463J_ZM6WZaEvdDZwvNGo5fFOrbiBrWrSXIHMHLIU9YoKRbwwmnwLsaGZUQL4T2RteyoPFpejYW90NQGktCXoFlzY9v2926sQoK-4tC1sqJ4Plnlf9bKP-yM6f6vw0wT7deBgq_TY_kqciTB259gH-UQ_g-hrzXb3uFxujum88gFgvqSYtKA6JqFKEXNYATRKLMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSXBLqVaTEa8Gitv5WJzFk5yzHNgkz9aQADYG9rcG8PDndxLsjUEqCQEBJhqbIde8NpxiM11LN9tLHqYsVmneNUzOQeG0jFCmygkyBz6NYBjYkWftW-F0NuIqWb2sH8h2mZaMKcRAavrtQO274oRkzxXNlcTgYsQyI1lz_t-oEAbVhCfUCPSoqaYQNoA9CQqZYkMCQnvxp1St7117UpzbVSeBahUSFhXbdcv6MU3mBe50fgGx9IL6kfUNPMPoR8DhX3kTB4ah8CZ7in9k5fFQFPNGqljGK3WCYkz-G7EBdrmYowGmGE8NVgi-9eWzFLsIn3SQEdXpHrQ-JW2zjxyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFZvqgXfFFWxORaJ4bEZRPVnpNBjDuYfigsrOUX46e8SebZRJDaa8IGHQcITnpXZIQ3dCdVWMBUaciZjvKS5eLjKtmvXCH1nfjNn8u-JvXqzXRp64TsQYfja48_GaPIZ2X_HgquHrbI22NGzRFrf21cMqSBGDeNqBLPxLL9nuyAr0gvYbNAyqW2NDtHCc5LSIMK0RTVz4lbgGDQGkLtGjQC__vjB7c9Ae56-cmEvbvhxdgWGy2poP5cpb4m5vb8eF6O82oY-0ThEhN0KPiO7oOep9eQniOakDEHPIVKn5NSmUgEL-LKCLD2c2D6qQ_ndeNPjZV62ZzMr13MVt-nQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxD2H-4ASmUDG19A1-2GQLSH-YGT6ZmpDgiQKu2_oguBnHEEN2_FHw4AjMYrCh9EXy6ylF58uSEnGnUxz2aMQ1FDt_MTFREAA35q0Ycnw-ApVB3ESSi-6oj-MqJDdVZJstX3wpOq7viq4fJT0pUB4L8_YPcBpvF_YGWs2ssctDiKXyVATrS7saHrrw46cftR8WpBhOX_rUWb3qS9f1cs69Dt8GGS2pltgjjaM2OX7FC-aCGI2ceoVvsR7wfi1suiAssAKaMyvayFYz494P7MgEaYH3JXiffdfBXfo7iO--wzHmsRJfTrAq4Kwqx2C826b6bZu9mPxPjZM_mKF3RGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=XO7HBvM-TNCjRjMS81QY0b83PCgZp7f_JP1VFsU_53H_DkxKJVkAn7ku_572V8qdzeuAMPM3FFbLDrau7j7GVwDLmRr4xIbrqaL-as0zjV0oW9ldQ16ErrWHCHubY_H8qqEZnQ7ICC4yFKwmlofSIB2HzwTGPbR4A_h0y9gPj2m-N48kf4-KCGQeJvQOup3Plcrt7OqA69SVHad9CEFvdUWUdxEtt3_NMyKG-pogt0xCjzcJFNt1Tls3OhHBwrYB-9Q6MvroW6r_pvT-J6_bM4f7W2TEQIvbauTJo2_J_EidbqYFpZnaeIbTFhW6HMnntNqA0fmem-OL57fixtqHbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=XO7HBvM-TNCjRjMS81QY0b83PCgZp7f_JP1VFsU_53H_DkxKJVkAn7ku_572V8qdzeuAMPM3FFbLDrau7j7GVwDLmRr4xIbrqaL-as0zjV0oW9ldQ16ErrWHCHubY_H8qqEZnQ7ICC4yFKwmlofSIB2HzwTGPbR4A_h0y9gPj2m-N48kf4-KCGQeJvQOup3Plcrt7OqA69SVHad9CEFvdUWUdxEtt3_NMyKG-pogt0xCjzcJFNt1Tls3OhHBwrYB-9Q6MvroW6r_pvT-J6_bM4f7W2TEQIvbauTJo2_J_EidbqYFpZnaeIbTFhW6HMnntNqA0fmem-OL57fixtqHbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=ZmZDa-capg04atyebCe75fMt8xkUcXwooAn4JZzh5mMEfWJduRCgNZzq1-K1sSwqGz-oZccKrFZQTHqYuX9NJGdg234HpfsNlH2YiVbtl0kOgUT7yTk6_E5EHLRaWDrRjysLayV24Ma1DG1eA4HDeykHpYiMdJnUvA9j1oMe3CqChq9zkYvlb7FzRrCAx4hYKlEcbpc3EuqqwNGxhswc_e662a6-SHdghrhW9SCXUwFO0AgQtPb8BgS54KouY8KpdubUNYoFLGxIL-yWAg3ZE6LzsnSetVWMZ8kOvp6MzHopEprPRR1-4UUgNwje0KK0heIYw_fm2r0Z2N-HGIbsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=ZmZDa-capg04atyebCe75fMt8xkUcXwooAn4JZzh5mMEfWJduRCgNZzq1-K1sSwqGz-oZccKrFZQTHqYuX9NJGdg234HpfsNlH2YiVbtl0kOgUT7yTk6_E5EHLRaWDrRjysLayV24Ma1DG1eA4HDeykHpYiMdJnUvA9j1oMe3CqChq9zkYvlb7FzRrCAx4hYKlEcbpc3EuqqwNGxhswc_e662a6-SHdghrhW9SCXUwFO0AgQtPb8BgS54KouY8KpdubUNYoFLGxIL-yWAg3ZE6LzsnSetVWMZ8kOvp6MzHopEprPRR1-4UUgNwje0KK0heIYw_fm2r0Z2N-HGIbsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UaSjIcEHBpPBALe97hh7cKGOGI0AJdVBylX7Nh8r8E1iRQcndV28zLBb1vv4Hjzs6K-FIZpQ6HFWK0SbTqBu-4UT7aNbnrK6aX71A3p5Q2_THpgERdtyxITm5Y43mRGyK2t94vrHKd30IWYr9jd2Cbx2YXCDdWC7nyHKyETXYCIZlmT_gcMbAo3mK-q8tjtxpzoXVs3LYnD9O0f2nSNjjuP40uIzCKTifvqQ9GWXizhFCmhyc2PUzPRS-AE8gZ5s1z9K0KQp3YqHyRCfKrpnqABVbYO5j9NHj_Y9iTtBIQoWRDA0TUT-DPNYPKY8YjOHASfv-xe2jULpY4MjHEKNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=bhJhEznU-jsHps5U_xWBEwWVfSLCU0zfxaAAMG2o0NTRHbvqYSrTBKL4hxP9p4OL2qaE8f3wr0lmSW54Uf6criEabHf7ErTAO-diwCE0rkKvNYJBepoz6TXxgOYYAE3awQQ7vBbMxzFMlAmJmc0JJyXaoI_BVjpbfn0FtvnK4OmnGYv3CWjvYOLbfBoH3rMNdLDUoh0Y59Jq9RfUYWcwb1dUAPy3hQ9C6zQIyFLTzOm-1FXmb0wvnzbwVHdp_AE9y3PWXWGtYsvK_HDDnBXEbbJDeBBi5naeeuqBtCRydNMoUBujc-cN3ymNPcQV3Jwdd5QuaEgFMYqrVtgIvgKPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=bhJhEznU-jsHps5U_xWBEwWVfSLCU0zfxaAAMG2o0NTRHbvqYSrTBKL4hxP9p4OL2qaE8f3wr0lmSW54Uf6criEabHf7ErTAO-diwCE0rkKvNYJBepoz6TXxgOYYAE3awQQ7vBbMxzFMlAmJmc0JJyXaoI_BVjpbfn0FtvnK4OmnGYv3CWjvYOLbfBoH3rMNdLDUoh0Y59Jq9RfUYWcwb1dUAPy3hQ9C6zQIyFLTzOm-1FXmb0wvnzbwVHdp_AE9y3PWXWGtYsvK_HDDnBXEbbJDeBBi5naeeuqBtCRydNMoUBujc-cN3ymNPcQV3Jwdd5QuaEgFMYqrVtgIvgKPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DS0xc2dsLSRI3NYAoQhkYvAUtMssuIf7_sLnJBVkriQVb0DjNu56Z77FTjlBovYoKzAvL1Fd3yBqYmRl1ya_lny865ruAa-39PeRRieMT81b87-t7hQBd0QolViNHlssRoLB0tDtgTdDhu5kseluo0e8j7xnlwqWZMP2OJmfKewaKhUM-ZBR5TAASzhXVY5SAWMYlujgcGYcXVs8CZX-sijKpwmmSqB7nRbDJbsohgx3Pn8lyrkQqPf-igv4LAbAEpxpEyN4sDiY-MrRk-rAnOevNLqSGKRmZyI9LcAD0nYyX4xs5qfBE5pkYZjxZkd8XJ6i8aTORgKuWPFM01PEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqpst0CYiCjs-P_rdSA2B2smcK6QpWE0N0GlhKcl1ALLqaET_5VbOHhfxtaFFAngCoqrmVJ3wJ60THzxi8b0JH_eEk8qHu3kC-IoX6AVbDjgV5h42r2jgcPPx8LDdrfJV960RCby-AsTXrXwZlrSo53GXLT7ONCsfjfgr1EVNbT_XFPIlvrWcc49nZ37ichyFg5wp4IjZHg9h4tfDAlXYEG-8Lct-1f0GSVCwvWMm9BmVFG6_rcZGw9GzGu7qjpnwy7lIfxcOs31Ixpyd3t6E2qeuPfsxJlzsnW7wH5U8q7uPLTHX-7-fvovUojmtM-VavQpsDITF_urgJvTgjLQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=OeAxx2i6i4cUmOqT6_SFadrNwHTQLDzU-tRygvObm4FtEiGufyRPDy7SvfLMWQfKM8aTj9GMxRzBmA_rN6G9ryTtVjqpdhkovkZm8qwGn3M7mgSU7ysOWqsNo6vHpWoyyztcLG2OYs0HEfELgw66EndpPxXH1mIaGg5YPWk4r7gmBky8-QS0GtWJEbqmthkliD3CBSWuXyXmgfkXKYLLWtu3CxKgyIXhlcfthrGOymEY1Ekl_Wp13Vb0QpemDycR8fUzeMn-haLF4xI1U30yC40ZtSW1y-Ab-ERgt3LJ-HlhjlLSnYJwXiWmFmASmtVkzKkuL2GgE_C4UwJVt0PYeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=OeAxx2i6i4cUmOqT6_SFadrNwHTQLDzU-tRygvObm4FtEiGufyRPDy7SvfLMWQfKM8aTj9GMxRzBmA_rN6G9ryTtVjqpdhkovkZm8qwGn3M7mgSU7ysOWqsNo6vHpWoyyztcLG2OYs0HEfELgw66EndpPxXH1mIaGg5YPWk4r7gmBky8-QS0GtWJEbqmthkliD3CBSWuXyXmgfkXKYLLWtu3CxKgyIXhlcfthrGOymEY1Ekl_Wp13Vb0QpemDycR8fUzeMn-haLF4xI1U30yC40ZtSW1y-Ab-ERgt3LJ-HlhjlLSnYJwXiWmFmASmtVkzKkuL2GgE_C4UwJVt0PYeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TynheDDwRlyQlRy3OtMM7JxPAwCrBVegNEptWGFlB0PShhVLsOvsnTjQx_VriowjkdsEcVjtmbizldzs4R_2TR8VOywPMYrXVrtzkCT883AeH-vB46tKI-9pt8H7iU4U6ryKIi29H_O9uwuj6poWPxp4qNwNhe3muphJwzEW7YT1h4p3DK60bXLMiE77UxdvpxmiciJ1i7FCZBruPcZhBFNiNTc-OB3VkAnYgpKRSTVwteFCUr2uvpAbmHog6mnlVXOUydN1VrKMbIxLN0ex3tOHcJV6aAnwaz2WcSvgoN3tISrd_660ckc04443dpad9MLmMS48N5cqfV7HE93rgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=SniHgbAgS2fPKkiaDps_KydpCy3HeQBSs43miyHCka42ItoAC1_MwQ7eJfmMRl3ULKnAIPls9BRHdy5WkwRA6qRAF32ZWbqBEsT9EIiJtkjtwIcXGUTArRCf4SuJ2QnebsFU-LxgWl6FWCXSTFSzWQRVU0NAC-jBANKZ7z3BARLsQr8M4ywY3WFuz0_KCGqcN2IVZ9C7otY85W-ekn_2jS1NnfEIuzjjr2KHbnGrCCVk1TcAIbO1Hnr0vyG0DD4vxS6OvuV2VyAbMkyD7zHqQTk-yaB68EJ-1bJiAdqJh594EVvWV7Xggk35cGPoxgKl3LjgnccPoYsK4I5g-S6bGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=SniHgbAgS2fPKkiaDps_KydpCy3HeQBSs43miyHCka42ItoAC1_MwQ7eJfmMRl3ULKnAIPls9BRHdy5WkwRA6qRAF32ZWbqBEsT9EIiJtkjtwIcXGUTArRCf4SuJ2QnebsFU-LxgWl6FWCXSTFSzWQRVU0NAC-jBANKZ7z3BARLsQr8M4ywY3WFuz0_KCGqcN2IVZ9C7otY85W-ekn_2jS1NnfEIuzjjr2KHbnGrCCVk1TcAIbO1Hnr0vyG0DD4vxS6OvuV2VyAbMkyD7zHqQTk-yaB68EJ-1bJiAdqJh594EVvWV7Xggk35cGPoxgKl3LjgnccPoYsK4I5g-S6bGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=mdZK3I1vCP-lr3bb19LhlWu8OvuXHqw5aRjuAlMhpvtidmIlVGCXHIlizXNca0e0LWMNJnwMuHYX31nVBjhuYgPYRPbLiVjRtTEzygPekMQP7mdOivV9zKM-NI3Rb1NR_mkDRJv4-RSR-y5VGarrfDONfLMMfJIBvca_TphSr3IWrHy06_4JNi4A68-4VlkJf6EDpg3ZYtlt5ePX_TL1GyIhnf4ic_94ukZ24clK4LgNDs7EtZHxN8odp3ODUAHzQSlD4snVqfx1Bf8lxFxmxkCA2RxoTDFPzIws1P4DmZBvLjEvv-gRzS4h0gMwdmRbllaNABZO7EWYshlXW2WTxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=mdZK3I1vCP-lr3bb19LhlWu8OvuXHqw5aRjuAlMhpvtidmIlVGCXHIlizXNca0e0LWMNJnwMuHYX31nVBjhuYgPYRPbLiVjRtTEzygPekMQP7mdOivV9zKM-NI3Rb1NR_mkDRJv4-RSR-y5VGarrfDONfLMMfJIBvca_TphSr3IWrHy06_4JNi4A68-4VlkJf6EDpg3ZYtlt5ePX_TL1GyIhnf4ic_94ukZ24clK4LgNDs7EtZHxN8odp3ODUAHzQSlD4snVqfx1Bf8lxFxmxkCA2RxoTDFPzIws1P4DmZBvLjEvv-gRzS4h0gMwdmRbllaNABZO7EWYshlXW2WTxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuA7Kh-8eeBCDyLKfhYWP3tm-vKs7H2gBXyqQ0dtb0mFYKxHKnI51E6mjmhGHYYsS7m0X6NlHCXkElavo0iB4YlHvits2eA1ctLCI4AiGfc3BA0agSxZ_XpSLRhjMogFII7juxyTY8IPxCZ36T4g1eoQ5NUlaIGzyctTw2rkizyZw_CcusNLShqNBE_CwN_Zv4KWzREomQVvrG4fFLfPHeApJ1AQ4YGIu-eU3m6RuSGrqOVNNLwayHEweEIrhJuucpkHzt3XvQjZF9WQ8EQNCtWrdScmYGjNwn1lg30ER0oTWYIYylo_JhZCn2piQXpLD2YcOlvnP2ju7LXeUlkYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYG-cMNgLsggLE9EFozgAv4EGxu9dKhubbFCzzQlTdiSWYKEK3V2rTtUDgq_KqRG-envUMtDoOWkT5l00IGx_TAMTmMdKdUaEv9SR8sPzPG25oQEEvhPiAMtjm0lAGqCYZDlZsdHtsyfGxWjsNHkRY-a02V0W-2oUWluLLgGivwb78SQ0EXUwPRkJZsvhqnmAFTbsJeka_ArZN_1nLuMi-u3T0Od-S-CNqpZQ5EwmJzXmDjgIH1MiRX8zZPs2ibdaEYMw5vB5Xl0LD7WaRLyJMUmnI6c2Lu76DM_5UzUV24buNAOWmEr3aCCiLyQ2UTHD0KUm9zPVY-3jOxpkO4CeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=u8hT-DG6Ew9dmZhbwXzrKNzjNr1NiaLdQ57mF7Tfpg-HAgmM3gj3cexl-hlsEXZyHVLcNB0KT0tVQAxQfwvBRrkmlahhHofou5npaza_f-HgWOBVsL-649x7V_yCNoFtMy4Xiw8N05cV09fYOYoxDj6GihDRk9njogUqt76CvEwzrU3wqzcwHWVkyi7Lv5QIbZtJwbGHIPsgUvlTtaQCAn-YkWxZ5_Z9j3-n1M4n73Y7hpUXyxlMcwFX4O7apXmYC9fohN648Pe7vhnGmOm7DA3_m0WZr75cg4aI89RPyFxCGO1b-fFU3r6mBfcwdLyJwJfQFlFJh0VGNHazwHLdcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=u8hT-DG6Ew9dmZhbwXzrKNzjNr1NiaLdQ57mF7Tfpg-HAgmM3gj3cexl-hlsEXZyHVLcNB0KT0tVQAxQfwvBRrkmlahhHofou5npaza_f-HgWOBVsL-649x7V_yCNoFtMy4Xiw8N05cV09fYOYoxDj6GihDRk9njogUqt76CvEwzrU3wqzcwHWVkyi7Lv5QIbZtJwbGHIPsgUvlTtaQCAn-YkWxZ5_Z9j3-n1M4n73Y7hpUXyxlMcwFX4O7apXmYC9fohN648Pe7vhnGmOm7DA3_m0WZr75cg4aI89RPyFxCGO1b-fFU3r6mBfcwdLyJwJfQFlFJh0VGNHazwHLdcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfAmVPtWdritEsEFMKA12P6o7uqt_-rt3t2yrfClK7XEkZOLvAIo9ugnnuBS0d4NBYnc4dInYHaFC18yTcqxzdyxaU9aLi1yff_LmER0j806-Qoz97_kRSURE0pEG3FjYXpm4AMchBLjRXQ9Jxjb91voqi9DZRM4H0g4ejdR4G3wG4YhwmEim2nRQlcTanWsBFg7H86X3pBRh1MV3wVmKbzu8feMIuAmXpgiHeW5eIDDokwk39SQky4C7Ebu0R7Fz5pINosJhh9jpii-1jsCtamzGR-tU2rY7A0AyPXZ0xX1rWwZ7s6IbEmJaph-bu3fwnTb7drS_Ch5ZzsttJDvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=V7k7KNiNRt5EwItuzZXPU1sW7soG0nNs7L9O1v68jGri8It60wJY0aEPd4lMZ1zB_u65tQYo5ct--VnRE7Vvo9gA7uI5vuZ5aVPWW1wZNe6tq_NEOKh74lC8AwZuZFgUFmDz-LojN2tY8ehwA5aZrTl4h3XS2tmiJMJ1OugsW9DDxWYLGINFzuXz5m0-2naSgX96T8E0sgHRfO3trhTBKOt1tgbL47GHMq1KYea112jrU5N0PsYtsq44uFtReztLlDbgp5RbXDVouTWVf7bT9eFK6xQ1cV3FZQk7jttXYBhJphdzbiMNitlKQEjQywkzi3nfWOePzJkmc40Z6RTYAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=V7k7KNiNRt5EwItuzZXPU1sW7soG0nNs7L9O1v68jGri8It60wJY0aEPd4lMZ1zB_u65tQYo5ct--VnRE7Vvo9gA7uI5vuZ5aVPWW1wZNe6tq_NEOKh74lC8AwZuZFgUFmDz-LojN2tY8ehwA5aZrTl4h3XS2tmiJMJ1OugsW9DDxWYLGINFzuXz5m0-2naSgX96T8E0sgHRfO3trhTBKOt1tgbL47GHMq1KYea112jrU5N0PsYtsq44uFtReztLlDbgp5RbXDVouTWVf7bT9eFK6xQ1cV3FZQk7jttXYBhJphdzbiMNitlKQEjQywkzi3nfWOePzJkmc40Z6RTYAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5ILnu_OXqMQGyw_D8UKm6cJar9r95gi5-3gcMpAdScMpKNuLhFUeEeiq4O6sY5vI2dm44IuWNoRkyjG1Y3Hnrwf697gGVgcLd2z_uSFyZOtt-jaRlbAN860BVn4UPR7IMZDl2aW3r8twAAVCrJoigDOAY2xAQk24CdtxAsECNMtCaekn1lAsKaqe37OEvThTzBTHVFUl4_fxo9dFg7wO-SFo0W9GIXpM_Sy07zQVgSdsm9NVToYBLKwV6m3sCcLaHfsW_BzSMO-3kMCL7cuWmyLQyEgkcp1UGWlCoutO-vaQepKQAeqMUdiIAuxVm9snd5GOXkcoko72xOm8otc9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=HL0Ar_AbUhqDXB4jLnUeT-4CDjzk0KWlLYdQKlWy32GWu_Li2uqVpGO-Iif2mECMR_irCd1Cdai9ompUoD5PzGZGqFHle_2smGx--hgE0tjFYvCb2DwbLaQPfSBuspufoAxvglDs4UpapepFGlXsLlr_Y4Vk_stmTsj35M9VpKf_0qYx-IEcFoZ3rG0cYhbs4HfaRy6xmBzlZm9OLF-gIbvKEf3QZ5qb8kTVMuVkdXcdzHutJyE8eHuhA5kbT42mJidmgJ6qARn6vtf7B9Vy9Y-7orelayvK4r8jyQaxPhsPOfzyzRNZy_aICq4RpU1Kft9Knqp-j49FZ0pqxcBQxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=HL0Ar_AbUhqDXB4jLnUeT-4CDjzk0KWlLYdQKlWy32GWu_Li2uqVpGO-Iif2mECMR_irCd1Cdai9ompUoD5PzGZGqFHle_2smGx--hgE0tjFYvCb2DwbLaQPfSBuspufoAxvglDs4UpapepFGlXsLlr_Y4Vk_stmTsj35M9VpKf_0qYx-IEcFoZ3rG0cYhbs4HfaRy6xmBzlZm9OLF-gIbvKEf3QZ5qb8kTVMuVkdXcdzHutJyE8eHuhA5kbT42mJidmgJ6qARn6vtf7B9Vy9Y-7orelayvK4r8jyQaxPhsPOfzyzRNZy_aICq4RpU1Kft9Knqp-j49FZ0pqxcBQxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=UvPQmo-HnV3BJZX3O4k6oOee94_WHYP5udjzqE4MmbueYzIg0S32Bq3AZ7AlvIRFccAm3EInsO3DAfzLV52sycj5quyfUDji5fSdMychTTTA5BaaAEtjo0U5YeBPvzYkPgEO2FIttPGGVAfkpaQ5y4K6_NBH0s9QPdvZBJEViWGSssk3aUAR1f8iYZ3FNDdgpRFVaWzzRux6qHhjoHu3V0dOCB-9R-guIGq2ewkAfjxVrsH7zQOE9Ty3_1IIpTJUPgB2J_pW6og8FNZ1-moA-FLKSWH-auhV-aU5HAVqBmwW9Z4FRDzcd9x4GtCqVzzM1RNB0wLrESMK7dY5kfXlMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=UvPQmo-HnV3BJZX3O4k6oOee94_WHYP5udjzqE4MmbueYzIg0S32Bq3AZ7AlvIRFccAm3EInsO3DAfzLV52sycj5quyfUDji5fSdMychTTTA5BaaAEtjo0U5YeBPvzYkPgEO2FIttPGGVAfkpaQ5y4K6_NBH0s9QPdvZBJEViWGSssk3aUAR1f8iYZ3FNDdgpRFVaWzzRux6qHhjoHu3V0dOCB-9R-guIGq2ewkAfjxVrsH7zQOE9Ty3_1IIpTJUPgB2J_pW6og8FNZ1-moA-FLKSWH-auhV-aU5HAVqBmwW9Z4FRDzcd9x4GtCqVzzM1RNB0wLrESMK7dY5kfXlMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz5aLvsXJU9VCGUdmHMLQuyRTbY_I91Xf274eRAKI1GeSwjs88G2V-XQ6rxP1x9t-TAPW1H9lvBfCGvylUoJW1sXZ-cR7wQx9k7p_AWx_BAxKDYeGnVZa6XJATBdhQmU5v_r_SXZ_jCGNAqe7qIQpWg2wJ0HLTs6vhneJC7PuGBZdqM9YpjEmgaJH0fBRWtb2Eea4NKH_N57uA5LXJNXHIJl_YEcknKdZ1D9mKTAeDDfDFMxxFlTx3pBxlNIcGDR0ouSBKfoK7q4YvmSFm8ImFcXEFkLiR4TcYLf6M39PDUOGwEINKJPlKNFCwyLZHkvkn__yu5gAAWilveH5a4ncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7Zhlt-aFfI46m-vzO07ryPnaUo9guqplQVVfWY7Al7Gmt9vqY72Q6UPTzDeCPOs7ISxAMZoYMRwjXS4hr894Kq0GPNZRH9C_T1sD-Y2Vl_ZPV7dHq1j6VMfNaS1v-lXBpF58LbPHOOl4gKP_OetRf-7P7tuqhoGLIU-nqfM2cBL_UNUvYOZ34Wd42uEoojHyLTYvRBxQg_-DWMRAfV0FXMkMTZyxLvLmk6P5XD6uhMR1UtQ8qICGEX1dVQP2_9QnZIjfWySqX19xkgQrX1HUI4PDh1hH2hxEA6VAOZX5fiHv3CyieDNiT-a9vnjvulRqgEhz-cHjEsLUmq3mUu_6vj4xE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7Zhlt-aFfI46m-vzO07ryPnaUo9guqplQVVfWY7Al7Gmt9vqY72Q6UPTzDeCPOs7ISxAMZoYMRwjXS4hr894Kq0GPNZRH9C_T1sD-Y2Vl_ZPV7dHq1j6VMfNaS1v-lXBpF58LbPHOOl4gKP_OetRf-7P7tuqhoGLIU-nqfM2cBL_UNUvYOZ34Wd42uEoojHyLTYvRBxQg_-DWMRAfV0FXMkMTZyxLvLmk6P5XD6uhMR1UtQ8qICGEX1dVQP2_9QnZIjfWySqX19xkgQrX1HUI4PDh1hH2hxEA6VAOZX5fiHv3CyieDNiT-a9vnjvulRqgEhz-cHjEsLUmq3mUu_6vj4xE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1vLwk-h90Y3lxkP_Dr7l_6nqQgCxjoTnrskl_MwwfyLyb04_bhPl7xiTkl2aV5ho69RfLK4xs3CP6dw_hApZDtpSJAjV0kl9olUZPsWDzX4vSMdJWEMaz2z_xKpnjHUoI5MIGv7Ha7-TSsOKhgOhjgDscDeaAEvjlJvXIpvccAac1gUrlksTGLtk0_rAEBrxg0Q9ZR98jyk33cJ9Op_G0DUtoNi3rtGwqgqMpoALny1qtnhYIvV2K0nZKQ3D5Z6ChUU2dwu9i6QpZgz9y170kY6wEE8gt8iNB85jWuIX1-gpzSpiYPY9oRuPKEqJd1g3BJ_d_pljNTINCYYwgWC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D9u4Yt5ETL7zuPn9IGc57zJZRqSV54xNPeqX24i3k0iL1TD-keKhFBsn9_BrX0NuIUFzZvTfd97PpkxoXLSqVyR4MRJhNv7j1OcX4zvW7xtwN54cL4Lj74ysVEx5-TcwES9-3wK6SYn5yaAlLLVTY7J2_igUHUXQFTeZVW0Yigtm_z9IjSUxYZ5-kSPHAjWg3Ml5FFmrWs17dJdfa14qHjEJp8LjMYCLFfiUIhbqEIgK2V4dhpJFwy9z1Qy3PlBQvz-hZQ4Yy7GGQNUopsCADMi5Y7x9HF9ldnpqLginLaw2nGbWft5l8VzdwWDep8m7Kj7CV0HKJ11Q-s8cc0BkZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=dt0drV3vAAylvsfAi2apYQdr2O2bwPQd8LfBfFbAyPye5qnP68FOEoegFKDY9pShz66ke-xDE0G0K4XbmuLa5GbVDWzCYM7vnPJPxfVCEIiNeXpatPd7nwE7wr8nCrI6KkM7TxK1qX2tI4Bv62Ny79nR8eyCyOsR77cIVGn4wul1qYKmoy06-wILcMNgkjhUA4rpldGftwECvfYQlgYA5KjikZYpRGMqfZ3-HJCK4Bqa3exV_LdcC4HhZ57yrKX_NOoJZgFWVpC2-t0FsOoLEpEoupamlpFgQvW3tSflm9f5ceqtuHqkuEIMHgy_VNd6l_Dcoq4e6lyqyvXHDHYIoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=dt0drV3vAAylvsfAi2apYQdr2O2bwPQd8LfBfFbAyPye5qnP68FOEoegFKDY9pShz66ke-xDE0G0K4XbmuLa5GbVDWzCYM7vnPJPxfVCEIiNeXpatPd7nwE7wr8nCrI6KkM7TxK1qX2tI4Bv62Ny79nR8eyCyOsR77cIVGn4wul1qYKmoy06-wILcMNgkjhUA4rpldGftwECvfYQlgYA5KjikZYpRGMqfZ3-HJCK4Bqa3exV_LdcC4HhZ57yrKX_NOoJZgFWVpC2-t0FsOoLEpEoupamlpFgQvW3tSflm9f5ceqtuHqkuEIMHgy_VNd6l_Dcoq4e6lyqyvXHDHYIoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MnMCBruDkaS5tJmM1rf3RpBfsEE1XDSMhsydqCzQrraPfY_5K08iOismLQRW0uqUcMHH4fKSBpAB-sW6-QqF9kBDtGOUKz6y2qXZArEZKDNbcmAJWFJKm4cSe-7Y2bkh9Mrw--lT4yB8CKjT13m5eqoWB8d389lIA4p5tkE5tTSdfNY_GhfJ2SYW9HnFQV9BquHhUrkqFa_3THo930YduuaAle2flQ8MMTYxd8Pn4OL1tIBTgEsGobW_oy2K8OUVok42XKW5C26XSGNQpmIKMGH6ohpYcRSVCFhrQw0TGB46FYBTAheCCbOqGyety3bFKYZ5dxOernVFM6e2Wh5HMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MnMCBruDkaS5tJmM1rf3RpBfsEE1XDSMhsydqCzQrraPfY_5K08iOismLQRW0uqUcMHH4fKSBpAB-sW6-QqF9kBDtGOUKz6y2qXZArEZKDNbcmAJWFJKm4cSe-7Y2bkh9Mrw--lT4yB8CKjT13m5eqoWB8d389lIA4p5tkE5tTSdfNY_GhfJ2SYW9HnFQV9BquHhUrkqFa_3THo930YduuaAle2flQ8MMTYxd8Pn4OL1tIBTgEsGobW_oy2K8OUVok42XKW5C26XSGNQpmIKMGH6ohpYcRSVCFhrQw0TGB46FYBTAheCCbOqGyety3bFKYZ5dxOernVFM6e2Wh5HMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=dFhRqjEhaNCXSNt7uPPMJ08TNraVqaCKEhXC6zy1Vz_HVwUtBItzfhnSP41pjZqv4GnCMY-pcCRRsJK0zCtu11-5OcxX7X8b0TfX5EU4UPqPAb2z7trWrIFW9Z23LlMFTkWm7YW9oSvSSaaG8cXSkl9Z6eY6u7om6qvxpAv37xgQOL9AJckNjvEyS6ymneKsrBlmp5bIasKsRonmhpLyUtLsexsxHTigBlu-xWiJLF5IW6fXPn-zdUREnT4Ns4ffOc2hD3bnkob8EjPK2sQfZW2NkKNyK8VY-XYqqkYRIXLtumaLsZf50Oj-sJHNBz7n49r8igiTctwCY2EULS9CCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=dFhRqjEhaNCXSNt7uPPMJ08TNraVqaCKEhXC6zy1Vz_HVwUtBItzfhnSP41pjZqv4GnCMY-pcCRRsJK0zCtu11-5OcxX7X8b0TfX5EU4UPqPAb2z7trWrIFW9Z23LlMFTkWm7YW9oSvSSaaG8cXSkl9Z6eY6u7om6qvxpAv37xgQOL9AJckNjvEyS6ymneKsrBlmp5bIasKsRonmhpLyUtLsexsxHTigBlu-xWiJLF5IW6fXPn-zdUREnT4Ns4ffOc2hD3bnkob8EjPK2sQfZW2NkKNyK8VY-XYqqkYRIXLtumaLsZf50Oj-sJHNBz7n49r8igiTctwCY2EULS9CCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=unwvNZkVmfxJpYD1NyKJE3RjPeaV-PL63qt-tC_8tcNC69Z0qGnfIxSAQtBVIiFtpNgBR0CRU7eEjMOxA3-o1mFu95BWu3gPk4hPbQvAxphuSO4tB1ldayNdJUr44mFGQEd-qrTHHJSSC9qEbx3d8g8TY3qvUqQ47B22OdbsEBE2gc82bRmyak2EDRY9gCFbUv8oagr_jS217P0QzzU-mWIHTXzcN1OxpDjHKNT6G_-aXiCvOD_7Q_Mb9RR57dGHnvn28Tyf2VVb9E5wgLKOX0zOIyxJBY8uUuWOQ2OPjqH_M7S8AJDbQNkdb_esv9czAKzBoI5b7cwFvpV5RronJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=unwvNZkVmfxJpYD1NyKJE3RjPeaV-PL63qt-tC_8tcNC69Z0qGnfIxSAQtBVIiFtpNgBR0CRU7eEjMOxA3-o1mFu95BWu3gPk4hPbQvAxphuSO4tB1ldayNdJUr44mFGQEd-qrTHHJSSC9qEbx3d8g8TY3qvUqQ47B22OdbsEBE2gc82bRmyak2EDRY9gCFbUv8oagr_jS217P0QzzU-mWIHTXzcN1OxpDjHKNT6G_-aXiCvOD_7Q_Mb9RR57dGHnvn28Tyf2VVb9E5wgLKOX0zOIyxJBY8uUuWOQ2OPjqH_M7S8AJDbQNkdb_esv9czAKzBoI5b7cwFvpV5RronJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8IV9oSHjRFHh3V6hKGrtaKw8tDVMECvbbroKJgB_w4PQHcE_7YclLfq7ACCaR0nMikY8pmAcgfkdg2wsCVEQ7OZ-3C1Ftb7St9FDTYI-jrq2hM6fzBhRt6usVNzC27801EuW7_wiZKSLj1dUAtn222hfRCICbHkqNoXmXuek6iYb3pzWnYxoHV6Nk9QNQq6i1V51Zu9oMo3IiD1XMZctUPNmn_asN_cEPZFgsmJFL17AHUKgDmBDrwFRIV2UCdgLptET-4SBQyS1rMUcktjn9w3qwmVPgaULnkUsfbfl0WuCxEv8wsGWCqNBtfpPqu-Yr0sFOCtLP3hhM6LRJdO4Vxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8IV9oSHjRFHh3V6hKGrtaKw8tDVMECvbbroKJgB_w4PQHcE_7YclLfq7ACCaR0nMikY8pmAcgfkdg2wsCVEQ7OZ-3C1Ftb7St9FDTYI-jrq2hM6fzBhRt6usVNzC27801EuW7_wiZKSLj1dUAtn222hfRCICbHkqNoXmXuek6iYb3pzWnYxoHV6Nk9QNQq6i1V51Zu9oMo3IiD1XMZctUPNmn_asN_cEPZFgsmJFL17AHUKgDmBDrwFRIV2UCdgLptET-4SBQyS1rMUcktjn9w3qwmVPgaULnkUsfbfl0WuCxEv8wsGWCqNBtfpPqu-Yr0sFOCtLP3hhM6LRJdO4Vxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=s-IsVSHAP5j9rOl3uEp7KGXfk4IOVQpx3QkrnZVdTRc4Q0EXDsed9eE7Y80qsX8xcJ0c9XgH7zp4EUm9QzeTH2nyJn-zqLjc4B33YDtDOpM1zC0QfdukVdvCIYuI3IpdjP9zZBW-ykU7sg1shC6IlyY3imdy4ZvHaw2dFtKPiU4I-eZKm14dWZw8WA0FgOU1jLVq65NKFFCeTC8eVaCJxu9IkLgasVxSZTEsH-yY1ShOhTgtDi_PsJAfAS6gMN10Sp15OzexsHajr10xUrNQu21HWmmmHEUMBgnW5S3Mini-CmdsNzEktFh3IQX1DCFQhRfHFgNBCGVxabCWegAi5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=s-IsVSHAP5j9rOl3uEp7KGXfk4IOVQpx3QkrnZVdTRc4Q0EXDsed9eE7Y80qsX8xcJ0c9XgH7zp4EUm9QzeTH2nyJn-zqLjc4B33YDtDOpM1zC0QfdukVdvCIYuI3IpdjP9zZBW-ykU7sg1shC6IlyY3imdy4ZvHaw2dFtKPiU4I-eZKm14dWZw8WA0FgOU1jLVq65NKFFCeTC8eVaCJxu9IkLgasVxSZTEsH-yY1ShOhTgtDi_PsJAfAS6gMN10Sp15OzexsHajr10xUrNQu21HWmmmHEUMBgnW5S3Mini-CmdsNzEktFh3IQX1DCFQhRfHFgNBCGVxabCWegAi5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=Mwj2K5h9L7Z1-Zgnt-k0wgJuRjdy4CYtgOZvq3TrKQLV0p0VsZhhol71QUjS6nAec92mlK97awUa9wJH2nKOf7xVXcKH5XXP7WpofqltVBQK-wybUwdEd9GvcTKtkGweIE8mtVLp0MbCMHpJl0ROSGhERK2V3ZbDpWNrDIsJbl72cd1PH2Bgkh_GdIMeoJqhOkuV0mtPD73Hv-3bnTdShNDhEAN4LbFlnBwl4E_olXwMCNLEFjd4PaRMBe57cpKyNYM51STS6se-DSvglsRqJsx66p6PV5cqeCfZnynXldw0RDU7hWrrCm1KovWDBsrx5nc1ujba7M6h1xs5Ka2Udg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=Mwj2K5h9L7Z1-Zgnt-k0wgJuRjdy4CYtgOZvq3TrKQLV0p0VsZhhol71QUjS6nAec92mlK97awUa9wJH2nKOf7xVXcKH5XXP7WpofqltVBQK-wybUwdEd9GvcTKtkGweIE8mtVLp0MbCMHpJl0ROSGhERK2V3ZbDpWNrDIsJbl72cd1PH2Bgkh_GdIMeoJqhOkuV0mtPD73Hv-3bnTdShNDhEAN4LbFlnBwl4E_olXwMCNLEFjd4PaRMBe57cpKyNYM51STS6se-DSvglsRqJsx66p6PV5cqeCfZnynXldw0RDU7hWrrCm1KovWDBsrx5nc1ujba7M6h1xs5Ka2Udg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdPGbXuujf0gAXCejaA4FgWE5oYVkgbY4yApkNfXAIuYtoiGu-qImzGS1rJ1dPYDGN9l7c0J6M9_JexR88oa5CLKTpPpu3iMzJMxKZ06zz6XYV9blnwQ5NzVH8VPlDqPfVy1H0OZ0o-4jHJCI80TwNNYgecFwjcCC1N99CslNRMwdyLUW035BOiWyFtLPXO-ER8Al2vkM7Uu3XCFFd_PdCzPmJMq1C1tD09WRjEXKDzaPR6PiNsdY1km5ztebOVfANjO7vV0MOgcFsMp8RjjPRocmWLnWicoD2Nu6mbpSidWjefXygYIJ2dtDDe4QSfEgUfRtDJYtKv__PyNKoNPZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W05ktMeuJHkEkjjSlrWVM8-JSUqiEeyDPENiCo4xJzJ0WjemAJHnz1NfhV2eRO9NdaitBf_VyrSEV-JgltMdoH6XfkCjm3dKth2z5e440FVgPuFCM34Ka2ygHcxDg14ftor_8b_9t-USjsUVlOUh_PgTgWLc7FbmQN1PxRUAKhODt2r8Rhg6ghD15APTN22rHpb3ddPxs_nCQ8re2HH4nkssZq06yR8AvauXBPH5HxJJHKRy23GW8fF-hZYP53Iw2KCz6fbYEKU6Evs-8OZ08JGJjd28-3_Evc788Zmvwg0n0QnydjeTgVSL6xIoWC3IQXVktT8KKFQNKoQJuiWjVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=HisNBsGaJbiYvu43lzh2yz-qmcTQUZmIsgDvztz7ak2oyOqAiBLg3UjHxTc4voVpNvYHAuO9XaRXne54BP7amCqSUAIqpq0M3YCUlOa5S2ZOSkDSitb17U1EaAclstP5v5iz-1cJgSi7V4m-tlMuW5A0sS0WtuN1DTZhFawNtuL6MSY-sRDyQP4HxaZQBRPxffGk8g_OTnlCtb294wlqmMvYWSD-leE8Kscjl_85PAgTzHn7FJH1PEboF9lKS5XAENUVaAA0GTOPHU9gMV5u_9KeOt8yDnUwZGH8556InKPN1uD2Ncua_KDRcuIfqHXdadj98T9LHG0mYNPKgzBEvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=HisNBsGaJbiYvu43lzh2yz-qmcTQUZmIsgDvztz7ak2oyOqAiBLg3UjHxTc4voVpNvYHAuO9XaRXne54BP7amCqSUAIqpq0M3YCUlOa5S2ZOSkDSitb17U1EaAclstP5v5iz-1cJgSi7V4m-tlMuW5A0sS0WtuN1DTZhFawNtuL6MSY-sRDyQP4HxaZQBRPxffGk8g_OTnlCtb294wlqmMvYWSD-leE8Kscjl_85PAgTzHn7FJH1PEboF9lKS5XAENUVaAA0GTOPHU9gMV5u_9KeOt8yDnUwZGH8556InKPN1uD2Ncua_KDRcuIfqHXdadj98T9LHG0mYNPKgzBEvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=XoaUz6OdqP69wmEjOaWa5-2WRnPZ9-CLe1_bRDT2olk9Ql_KwuOGqQBJLRrUSBSN7Cw64ZoRlR2tNuK7GNOhvAFUcijJV9fQNL7M2_TzRmSjdTxqpb66w_2BqtVL_622MWtlUI3mBEEfWIW22b34yVJSonIUBCp2Oyuk9lgi1Iqd1EO3-Z05EDUMebEc7lukuuHa9Zd1unpnDIyyTgleV-fv58rM3fYVZZH88LINqjGFvwQeSvlBDtHptEzGtGQhylF2jLNHAhqqH5yQTuRgZZ4zpihLTxhm8d1QjrdtJZdRpCqS8lp4E-YmDv2fr3Ec2ZQcoPEsdKwkufZatPRQsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=XoaUz6OdqP69wmEjOaWa5-2WRnPZ9-CLe1_bRDT2olk9Ql_KwuOGqQBJLRrUSBSN7Cw64ZoRlR2tNuK7GNOhvAFUcijJV9fQNL7M2_TzRmSjdTxqpb66w_2BqtVL_622MWtlUI3mBEEfWIW22b34yVJSonIUBCp2Oyuk9lgi1Iqd1EO3-Z05EDUMebEc7lukuuHa9Zd1unpnDIyyTgleV-fv58rM3fYVZZH88LINqjGFvwQeSvlBDtHptEzGtGQhylF2jLNHAhqqH5yQTuRgZZ4zpihLTxhm8d1QjrdtJZdRpCqS8lp4E-YmDv2fr3Ec2ZQcoPEsdKwkufZatPRQsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=KeyZN4Hbk0I8OjLXdVdvTIHYPB1yqCkGAXu05KOojntYhLpe5NjS92rx_6WHp8Seq-6kNvd7u5aaIcJ4W8vgh_8uGG32lpkIipkIY4bNh9oDYDkPxgZ2Zs3yB1FacZt_hwghN9GFh_6tsneKw1XyYFILR6lBWlnboN23xzLPFWMnHDTGWIeRY2sc0mIBBOyxCqdpHrdEHUOE8kOQZOs2u-12Xxdo4B4wObvVCrVmjgN3oo_nx0HvFk1Ckju6izzj7-60_F_Ok7tDkWIEJRP3rOJXLdVVaysiSCFE1Seo8yiaZ2LG789YzDA0DEHr5Pam7Ug6UnFOFUjO5_hotHTrGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=KeyZN4Hbk0I8OjLXdVdvTIHYPB1yqCkGAXu05KOojntYhLpe5NjS92rx_6WHp8Seq-6kNvd7u5aaIcJ4W8vgh_8uGG32lpkIipkIY4bNh9oDYDkPxgZ2Zs3yB1FacZt_hwghN9GFh_6tsneKw1XyYFILR6lBWlnboN23xzLPFWMnHDTGWIeRY2sc0mIBBOyxCqdpHrdEHUOE8kOQZOs2u-12Xxdo4B4wObvVCrVmjgN3oo_nx0HvFk1Ckju6izzj7-60_F_Ok7tDkWIEJRP3rOJXLdVVaysiSCFE1Seo8yiaZ2LG789YzDA0DEHr5Pam7Ug6UnFOFUjO5_hotHTrGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=AN_Dl0hGVxtk6smjEtXpjSzPv0Js5CDBc7OxU2z2UuOTmpYQ3_5FUhS-VcqC52AE3c4T710fh27YDiAvEATtH9s77FvPerSFgmF6NUNWhWh2m0052s1hcwWvqCj7NYBMOMInas-0rIK7De5eg_971pQqNhqJzBia8zwpw1a8HvAYnFqFMcQocmmwowzQJ5PT8Q_2YAQekO3t9Fu0z6cDdZQX53noRbPY0cBxYpqeDhwd-c7LqddioDOS5qdBw8LQb2ghOrsm_TYylOxckxEXF_LTrmRpMLFoH6-ZPU9fsl1-zLON81zHeg94NjkiE2wo0ZlAVx2O1Q2qi_qgjy9o-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=AN_Dl0hGVxtk6smjEtXpjSzPv0Js5CDBc7OxU2z2UuOTmpYQ3_5FUhS-VcqC52AE3c4T710fh27YDiAvEATtH9s77FvPerSFgmF6NUNWhWh2m0052s1hcwWvqCj7NYBMOMInas-0rIK7De5eg_971pQqNhqJzBia8zwpw1a8HvAYnFqFMcQocmmwowzQJ5PT8Q_2YAQekO3t9Fu0z6cDdZQX53noRbPY0cBxYpqeDhwd-c7LqddioDOS5qdBw8LQb2ghOrsm_TYylOxckxEXF_LTrmRpMLFoH6-ZPU9fsl1-zLON81zHeg94NjkiE2wo0ZlAVx2O1Q2qi_qgjy9o-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=VmHU_c5oawg-kly91h-srK7GwGq5XJin7kCufNj1gzveVAf7zHHvWFk4wghKVzifCleuo1_2ZcdJDlC3B96W0mVuhSPK6sZz0T_PcVOMbJ5eNiSB-cca-0WG41RtcCU6R64ahXv7sSNrOIpxelgpm_v5sQDCaGgxYt4Q73uHM27NaMQaWeACjc4oppunyrcteT0v96JnVk4007TH2tOINnmlYS0U_att2Fr74wqKdZOpeEgJvUVZEAYJQZ7r1dbMp53QxUTVytxsOXKB1jtQ97TNw1Dfh9TVJNXBHCACZgTdkk_OahzvRy9jGgujTm4s0jksmF69X4VKjRjJg3jN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=VmHU_c5oawg-kly91h-srK7GwGq5XJin7kCufNj1gzveVAf7zHHvWFk4wghKVzifCleuo1_2ZcdJDlC3B96W0mVuhSPK6sZz0T_PcVOMbJ5eNiSB-cca-0WG41RtcCU6R64ahXv7sSNrOIpxelgpm_v5sQDCaGgxYt4Q73uHM27NaMQaWeACjc4oppunyrcteT0v96JnVk4007TH2tOINnmlYS0U_att2Fr74wqKdZOpeEgJvUVZEAYJQZ7r1dbMp53QxUTVytxsOXKB1jtQ97TNw1Dfh9TVJNXBHCACZgTdkk_OahzvRy9jGgujTm4s0jksmF69X4VKjRjJg3jN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CVq97w7CMZ07_TANW0qo1Xjcmnu-UT-t-kwiWQO7HQ1U-39L0UN4OKgYy5RuAH7OnpU-ZQnSW1Ks7dUjxlIOHjOdVTaHkJz7D6ap8DyX4PwrkoLicBrXGaR3I93yQhzAf-oyRMdTl-hIwxkbcnxokriySdd4f_S2SwGHFF1n9AzgwXuZ39b9uthjpmApi8sV20961NC9qN-fbI3-F4GWDkDpf__LBh0zeCeevAoiXR-oFmI_69VbOqvzJvvcx8TzEjAVqYA7UGXbxZaaGWGHb3YgDMqh5_V1L_J_P50Qn419mfHvx1XA5VdMFGHJWNtcy9kHy4HKcbYmOV9kxVy6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=kkgX7INrrBq9QQeCnq7zUaTKoH_JHKxURMbTNbGpteS5GvDuldT1s1eFian8T1x_Ai5xNadx9ygAfzOSE_dN9fVEhKHDrL-BkQmJqsXCVEm2pc-dGg16pyX8N5BSLKlA8UvJKs4cZLa1O2qqhtSIwChv_hXB6JcGe_Mq7C82rFy9ahVmcmwsk_JvSHKeq03bna9BOsYc_hmQmYuA3G7XMUDT03rf9ca5D4Tz3SIiBN8i6Z9x5NToE7RBB7iCpFMY1z5XfNAGZxbRMW2r8CT1pr8F9LIVcZsbhRn2eLRdqZYbwOcmgIVVjvZwOc7Bn-wb2tVp-XTyDEnrIgywqfbQnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=kkgX7INrrBq9QQeCnq7zUaTKoH_JHKxURMbTNbGpteS5GvDuldT1s1eFian8T1x_Ai5xNadx9ygAfzOSE_dN9fVEhKHDrL-BkQmJqsXCVEm2pc-dGg16pyX8N5BSLKlA8UvJKs4cZLa1O2qqhtSIwChv_hXB6JcGe_Mq7C82rFy9ahVmcmwsk_JvSHKeq03bna9BOsYc_hmQmYuA3G7XMUDT03rf9ca5D4Tz3SIiBN8i6Z9x5NToE7RBB7iCpFMY1z5XfNAGZxbRMW2r8CT1pr8F9LIVcZsbhRn2eLRdqZYbwOcmgIVVjvZwOc7Bn-wb2tVp-XTyDEnrIgywqfbQnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=K0SMo1lAGFdpHSj81F-lxfHvSbHKt0GxLIRtimDhiwRf1HrsrLSShT_SbaOtwJ-FlzZk4Uvek_jZq-JW0eUp3G1-69iKfXHHaLlWA9Wbxd4Yq6fB-r3sY51CNgiahurnUmRCyjFcKdBNuHkjqHtdIS2MJE_Ov-MxIBCQgx8FmTTsGI3ae4eGjg7yN7U9FGjALY9dpQGI5TiSRJfW2nPEFXrl_-49t-P0iOLTb3pcP0RGqLhLO1q_vSfUODb522DySCZ0STQmDepc3Tsbiig6zVx3rruVnLd1Hp5xUVkoHD-PgkVNYEIp4JQ3NT2u1Z6K53KUqw6vcxI2WeCTfElefw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=K0SMo1lAGFdpHSj81F-lxfHvSbHKt0GxLIRtimDhiwRf1HrsrLSShT_SbaOtwJ-FlzZk4Uvek_jZq-JW0eUp3G1-69iKfXHHaLlWA9Wbxd4Yq6fB-r3sY51CNgiahurnUmRCyjFcKdBNuHkjqHtdIS2MJE_Ov-MxIBCQgx8FmTTsGI3ae4eGjg7yN7U9FGjALY9dpQGI5TiSRJfW2nPEFXrl_-49t-P0iOLTb3pcP0RGqLhLO1q_vSfUODb522DySCZ0STQmDepc3Tsbiig6zVx3rruVnLd1Hp5xUVkoHD-PgkVNYEIp4JQ3NT2u1Z6K53KUqw6vcxI2WeCTfElefw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW8tTtFud71Q-UHEIxqHeMBSzrzjJkDeKKkej78oaxzkVxbRfhcqa7oHGGmzlaiH6QHVt6fss0pQBErJEl-KZ1eldMvIQivoCulsL-u2eQalw2X71gDQCVxO7cc7yAjjDjvlMG8XMDtSisMOiKw49vpI8x4JcBSJPbeo7lrfod_ePZIH-gSWfDwX-X27KIORCXkdAMSjOqc-5K5mdZ9WjWp-8JswF7stM0pUxOseMNsxGtHLPHGjmLQGMxnJ_aMoEs1NkmAPNL2WSgPcwxuSTBQ_BibY1h2HKqV7zQYhcT-YKi_0gOjV8LxAlwKT9DT9EuY76WDJzg4Xm4W9-_EVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=iTJnOocs0_auWKWeh8K8dPwDGaQB3TZFnQ854NGU_Rwngigw014r3rfug51ZJQknz_8BHK8y2jLMprlZEqNWLOcVo68ln1-DF9-bJz6u9UvWnc_kGvErJUlAKRZq2AmCznbmWgFRna3GX_ngGDAh5FktozE2hJeGwKpI3nWe75Iq0fpch9bCb8pkbnjHp5ooCWPs5Zph8BZn7Av3dtQcGh00GL1e9wqpVfxq19Mrgvd0cin9iqOhspFGjud4V958hBCzzaW26L2qVAxEJUDvXnEhwao71aLHJ67Kw5T24CizSlxGjAkHs4cGhRELXvqhGo63Z42A8exyypJyKi2e2qayH2OvVGeNt0zTX-pp0MdI0vQjjO9ud4FLdf1Guva1Qi8S5abP-6zz9SvH3rlK5IUP792T1NEw-NoX3ru1TWgx_FjQnpFa6Y092k9ueZMxkZ0j7D0nP76Tk8Ph2re7RufanBhrw_5jNZdt_bCIgs5kDiBoWrOhBsfmY5CI5O5wA3SQec-JvvmsnnL8ZYJQ57xmEAM3jcu3Phx3kmnUoZTkHDZE5ZewAXGdYRlb3gkpzu_kciHkQTAtV4WzLRaQUouDe33HE4Zlod6p__O9h0k9pm_nJYBzmVeO8plfN3GjwMOS9ETl4S8U1B0U9z5qQs2bYS6CUgM9k01f78TU5x8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=iTJnOocs0_auWKWeh8K8dPwDGaQB3TZFnQ854NGU_Rwngigw014r3rfug51ZJQknz_8BHK8y2jLMprlZEqNWLOcVo68ln1-DF9-bJz6u9UvWnc_kGvErJUlAKRZq2AmCznbmWgFRna3GX_ngGDAh5FktozE2hJeGwKpI3nWe75Iq0fpch9bCb8pkbnjHp5ooCWPs5Zph8BZn7Av3dtQcGh00GL1e9wqpVfxq19Mrgvd0cin9iqOhspFGjud4V958hBCzzaW26L2qVAxEJUDvXnEhwao71aLHJ67Kw5T24CizSlxGjAkHs4cGhRELXvqhGo63Z42A8exyypJyKi2e2qayH2OvVGeNt0zTX-pp0MdI0vQjjO9ud4FLdf1Guva1Qi8S5abP-6zz9SvH3rlK5IUP792T1NEw-NoX3ru1TWgx_FjQnpFa6Y092k9ueZMxkZ0j7D0nP76Tk8Ph2re7RufanBhrw_5jNZdt_bCIgs5kDiBoWrOhBsfmY5CI5O5wA3SQec-JvvmsnnL8ZYJQ57xmEAM3jcu3Phx3kmnUoZTkHDZE5ZewAXGdYRlb3gkpzu_kciHkQTAtV4WzLRaQUouDe33HE4Zlod6p__O9h0k9pm_nJYBzmVeO8plfN3GjwMOS9ETl4S8U1B0U9z5qQs2bYS6CUgM9k01f78TU5x8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=CpUxiXsYLCH8dSnjCk0YIkt5iwDTcMfQkkEcaqCNJy0TZ2-mJccTSZBuT1xunWNAkX7x2T9b0biqYGotW-hWqbOvPHdzVpeUQQJOxbLyFD6oNE0CTy-ryd2H06QgKjkmaS97Q6kYPk66YcmfjnkSqHbXoAUX7xpPghyusx9DjZeN5LMrTNiK7DCIe6_7Jab6yJGgs_BjWGBsj8YaCH2e0GVV8Ndj1zWizxWoCgl1z8HiePiQ1-UjsuZ5-w3pcFRIa13u_ai2NSP05vUdm38Pn9HKHf4WUcplkgP06uV-fRVIQaHzd7o0H5l2tPfToSHwbpwEmdpAcM_e_cIGXGlRGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=CpUxiXsYLCH8dSnjCk0YIkt5iwDTcMfQkkEcaqCNJy0TZ2-mJccTSZBuT1xunWNAkX7x2T9b0biqYGotW-hWqbOvPHdzVpeUQQJOxbLyFD6oNE0CTy-ryd2H06QgKjkmaS97Q6kYPk66YcmfjnkSqHbXoAUX7xpPghyusx9DjZeN5LMrTNiK7DCIe6_7Jab6yJGgs_BjWGBsj8YaCH2e0GVV8Ndj1zWizxWoCgl1z8HiePiQ1-UjsuZ5-w3pcFRIa13u_ai2NSP05vUdm38Pn9HKHf4WUcplkgP06uV-fRVIQaHzd7o0H5l2tPfToSHwbpwEmdpAcM_e_cIGXGlRGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0sdw3iwWtl5N8fQFuCEwaGGzvlhTFKRIFNjznWMu12DPajTgY4CtDajxMhC-WKruWJ0zJ6xy7Eb7ESZYj0ae28sSSB_CXVfqHsQ709UZmtDjUS88iTtV9KgPR3s2g0MGFAAQV-EOYDyYk0t1n8rLqWzn3kjmjYxqLXsVXPKamGMSNcGRawIBnHzmpzWH3rhe6xEgCZGQvAaBYjMPekDFx6QV7J-uF-RW7YPPMGS12KZ7Iou4KfJQs5cxIICSZp1iK_IKFBY6Rz9VEjqh0KxPHS3v7Pvpq-Q8cQFzRtBXfgzxo0ildoDl2aXAe4KZrhts7u_W1GUGI1Woba_Lvn4FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVQY6ncWBkhaWgU2HbDVUTYNYtp7RVLZmPhf99ko3YQM5CdeKyLzSBxl30sLzJM3oKuWfz0mkBnnZx6VZY0haBWssEPEjO1heGN4agWT0NFZi1rF3Kj1fy20OwejgRPiW7Sm6WEhECz9ljXc17e0IrJ0OWmNGJx5IznWG-dMtASQMKo3YvVZys2thGivAiWv_FCF8uQOHnNlpGnyr2bDntzffTrXAOU88Jo2KHX9WVPw23DcZhl-AvD4CSDoEL8iMDPOsjjS7Ns3BoP3dxW3G7D1Xi4LSBJWI0VkFNGHx9fzl_o0OCIYaBO2LiA4AOUfRgiwzIkhakTEArmE6DLDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=ugjIeKMwGEP_TTHKLLCaqvMAHKtZYE37n3MFzm6QU83UeEkt8OQd0-aXbnajJdXmmpBQz16_U7AtIvrKL2idS4y67pMiFVNonnOxq8GPB272_VdAiW5DRt95tvkj8llCTpwszjru7-Sf_R8OTJbUmru-k0A0Nyinc6sgYnz1hnaTzut-MKKs3a3EAhe3GM_NRs0P7nut0rw6LWMvmxA5Cs0KPxcz0cxpVmvWARd_shw2ruxqytq2sD5RPUelLqnTye0MBPmPh3LMLbNNYdnE2e5IXt2qT6BvolugTpUvXaaiWRicoAzQcQm3KTjk7AYtd5GEMEkG57cX57il4f6DvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=ugjIeKMwGEP_TTHKLLCaqvMAHKtZYE37n3MFzm6QU83UeEkt8OQd0-aXbnajJdXmmpBQz16_U7AtIvrKL2idS4y67pMiFVNonnOxq8GPB272_VdAiW5DRt95tvkj8llCTpwszjru7-Sf_R8OTJbUmru-k0A0Nyinc6sgYnz1hnaTzut-MKKs3a3EAhe3GM_NRs0P7nut0rw6LWMvmxA5Cs0KPxcz0cxpVmvWARd_shw2ruxqytq2sD5RPUelLqnTye0MBPmPh3LMLbNNYdnE2e5IXt2qT6BvolugTpUvXaaiWRicoAzQcQm3KTjk7AYtd5GEMEkG57cX57il4f6DvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=POo3HidftHVRl9cJnZmfX_LVQ8MvEp4OA-om6Ot8DM0XeEapMEVBkgqzITVOUY53n25ihFnY4WJe3WAl6wO9f3sQ2Dnj7TXL_d_vqNwu5fYswdxJaNUgylXBfziJ17b7DztJ3fUYEnsiVppT40BvWfRiKNbKtO9rynzshGBm3sIYYi5khpqpULuz-UqouiUSF_YEANiNqsCQZ_yvOVGcMw_vMnqhcdO7O59aYs79RSCNTQX1rxkMxyzFrddP-rzTZtZ_w-3PyaU2yH2R4ClTDuLasIfcbS8_Hqj3xIvG50f9TCB85PdHD6DxgXoanMxcgA3unDGY86oZdr0S0Dc6fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=POo3HidftHVRl9cJnZmfX_LVQ8MvEp4OA-om6Ot8DM0XeEapMEVBkgqzITVOUY53n25ihFnY4WJe3WAl6wO9f3sQ2Dnj7TXL_d_vqNwu5fYswdxJaNUgylXBfziJ17b7DztJ3fUYEnsiVppT40BvWfRiKNbKtO9rynzshGBm3sIYYi5khpqpULuz-UqouiUSF_YEANiNqsCQZ_yvOVGcMw_vMnqhcdO7O59aYs79RSCNTQX1rxkMxyzFrddP-rzTZtZ_w-3PyaU2yH2R4ClTDuLasIfcbS8_Hqj3xIvG50f9TCB85PdHD6DxgXoanMxcgA3unDGY86oZdr0S0Dc6fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=esuPW10c3DYKh-lWtjapAIl2G0bUMDyJJMEI4qRz8lq-ihrdEpGtD88-W3tXgDLmN54hUMiNY-ADgzmvCtgHOzOEsBJRPUkCYzdufbnCsBmlTnbS7xCvtVhZQBoSl_Fl6_hIenOvcaz46zOI4b16zfIYK2SX7ksOc0NQqyBU7Nwb3Q7_IbMIg3KqFzHWEfEsGuDJgCeGbug54-rwr5ADcfgpju_YTxLgmkvshaV1E7XrzJVOwoj9ygT6cYQcPo7_H9C5nYidholIGIe4ZDVB9H2AlahDYhzAxsYxam5Mzd478PDEg9RNsA8CFtPWRGZFbJJAE5oYi_6fpVwUKRD0mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=esuPW10c3DYKh-lWtjapAIl2G0bUMDyJJMEI4qRz8lq-ihrdEpGtD88-W3tXgDLmN54hUMiNY-ADgzmvCtgHOzOEsBJRPUkCYzdufbnCsBmlTnbS7xCvtVhZQBoSl_Fl6_hIenOvcaz46zOI4b16zfIYK2SX7ksOc0NQqyBU7Nwb3Q7_IbMIg3KqFzHWEfEsGuDJgCeGbug54-rwr5ADcfgpju_YTxLgmkvshaV1E7XrzJVOwoj9ygT6cYQcPo7_H9C5nYidholIGIe4ZDVB9H2AlahDYhzAxsYxam5Mzd478PDEg9RNsA8CFtPWRGZFbJJAE5oYi_6fpVwUKRD0mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djyq6QAxhDl0FhiS8Umlr58_RWS0rkcp0_sUciRl3AULLcAGiA8szEy9_HoxNfpQ4nnF-CldnXDNNi26FA62gG1VeLzHAvqagYJkozhO5mg_TTrqP4TLjXEjY0esNMrrzG0V8mn-TDw2xlUNrO08351ging8B6NBq-ydvOKY6ceGNqfoXCnHguWwNwTm2GyfLIb7kFVI_Af9GytgRzAVMV0Gds-z89kyO3qObOGttdQt-DT9HzLEWVEFmdc2TjoZkJMOtf1833t8L6tTAeN3iDv2_BKX0l5Px_5gw0guskL0aH1UZZFjqp_9ZueirGf7LRgXLt8eYjjY07udYYNXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=IyeezgW_4Mb_91Itd9l2DPS9sUS2bvphnXYPX_DYEYMcwKUNBdbeX91FSMTel7LsuaBF1biuNcVrCsMKAJ0s8CFjg_tS5wtY_Lt3P5v4YhhhQScpghinvCqVgnBrvEf_g3RvFEfIBwfEpVSGln9hamUxKzQaWHSeO_pb2nBXLtjtYGg5GCFGfdlip32yIeAJoDv7OSXBSyAPr6BaODF-BECL8xXZ5CAU2CRmLAMdPasSR7FYivym0xOUT65dJUylQOU6PoWRtK02JAtTm89Cz4fEx9Mj-3bbg7ENgkLw3fGer13ex9V8EGPIFBWtJEawqku7iDwtFYi04GsK3Tc_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=IyeezgW_4Mb_91Itd9l2DPS9sUS2bvphnXYPX_DYEYMcwKUNBdbeX91FSMTel7LsuaBF1biuNcVrCsMKAJ0s8CFjg_tS5wtY_Lt3P5v4YhhhQScpghinvCqVgnBrvEf_g3RvFEfIBwfEpVSGln9hamUxKzQaWHSeO_pb2nBXLtjtYGg5GCFGfdlip32yIeAJoDv7OSXBSyAPr6BaODF-BECL8xXZ5CAU2CRmLAMdPasSR7FYivym0xOUT65dJUylQOU6PoWRtK02JAtTm89Cz4fEx9Mj-3bbg7ENgkLw3fGer13ex9V8EGPIFBWtJEawqku7iDwtFYi04GsK3Tc_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=C0d0wqKanKFO0iUIK0cJZTNa3mvwE3LaemF-EF7LMZE_CPOF4c8SzBH9n08_RBgcS4MTMYgtbp2uETqCMp5fyaEtwwgekbz3e3SGq0_w8t_LDam9_VAs5RF8wxjcrwhA-gb_hxWXNBgRfQeaBm0G1flF9Z6PbscpsGVFsJYv-8B0-aBY3ohVyxD40FAaaQ3y3_U5FUxSRMLqj4CrWzJUFH9Ru2m-Zqhi45LbjSrxkBFJSRz1ufaWPmBiXBa5m_Wsp23JjAK_q8H9lvXO0d12aPxnNDIeAE7te4IL2nIY5mDfgGp8riNGckB_Ikn3wWrrT14Irg4E1ice0AIbX0q62w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=C0d0wqKanKFO0iUIK0cJZTNa3mvwE3LaemF-EF7LMZE_CPOF4c8SzBH9n08_RBgcS4MTMYgtbp2uETqCMp5fyaEtwwgekbz3e3SGq0_w8t_LDam9_VAs5RF8wxjcrwhA-gb_hxWXNBgRfQeaBm0G1flF9Z6PbscpsGVFsJYv-8B0-aBY3ohVyxD40FAaaQ3y3_U5FUxSRMLqj4CrWzJUFH9Ru2m-Zqhi45LbjSrxkBFJSRz1ufaWPmBiXBa5m_Wsp23JjAK_q8H9lvXO0d12aPxnNDIeAE7te4IL2nIY5mDfgGp8riNGckB_Ikn3wWrrT14Irg4E1ice0AIbX0q62w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=qBdGfrPCzk5IA7SvrSaBFfqaQZuSnn9td6LcaMrOWoeEskpzvKCoDmYIY2cPjaqpxzAxMsk6EtN5ioyPa1LB3o22mKj9DYzs9eVqsfE5FTu8N3csrq3vffE96WauTXYHXnGYBdllJP445LdjUKTFYkvc8o97LHKyj7mJoi1TUjfrjla7pX3_MOgy7JYb0OG6RAmavzq_9OW8bxSqcsoWHvGIoVau57iJkvYIKTdbOGs24uSSe2hiWM9KiXx4qcpem1evL-aNea2ahX0h43pQQI0ChFhFCm7OSLC5ikIGVrMfAgOBC9FBK7HZSkjsBx3FYIGRBMk4Yow2kyiMx5hGRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=qBdGfrPCzk5IA7SvrSaBFfqaQZuSnn9td6LcaMrOWoeEskpzvKCoDmYIY2cPjaqpxzAxMsk6EtN5ioyPa1LB3o22mKj9DYzs9eVqsfE5FTu8N3csrq3vffE96WauTXYHXnGYBdllJP445LdjUKTFYkvc8o97LHKyj7mJoi1TUjfrjla7pX3_MOgy7JYb0OG6RAmavzq_9OW8bxSqcsoWHvGIoVau57iJkvYIKTdbOGs24uSSe2hiWM9KiXx4qcpem1evL-aNea2ahX0h43pQQI0ChFhFCm7OSLC5ikIGVrMfAgOBC9FBK7HZSkjsBx3FYIGRBMk4Yow2kyiMx5hGRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ncA7agQS9ihO-CQZoKoRXPPO8htqVCpUc55bQhFDZ1O9nRwK1vWlnFehTsqc-crgDT1tNm13D2EEHgg7GfEDE9cdry5hSbuTL6JAsvTBi0DO4O93ecGhFNkU2zE3Yk_ZbAlSuZmBSS2PXQY8SkHZXI9GaWvgzW_aIvruBvRnA3rxS9RqSBCxgY1d50PtsYVRJAwjpexLFmgJ8evh01NPrbDqaPQbPoCSSiTbW1z2vvmVkfza7fn9kyRkdoJFwy1P3oLaHEYQw2gYObsFhQfV-QNqzNYP6JV02Pn3tf13dvZUFIuhyobIYq-xOgqB_rWJxWQYcMNpVGjID6BDNgAyhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YpskRftUJ_NIEJOGKPgdyXS2i_lpx8tEWArjrGm_FWpbsEgqjhpukSRms6sUPfw9_jDYC8ZUUC9IoApBGim190dECi08_lhBpXzOEfQtAgQtfQ_ZCfYSTnfS9IsUyviVfjo-fclTt8KEFDfKemU1mEqMYtpioR76R_QINqJ04rMSmGruIi9xV4lKjcZ57oNfV0DxDx8raNQozc4NCoHsJmg4EA4F_bPluSLaGpXNZOE4M7fH3ZGl-5gtzLKZV0AbOJAGGWoRlxAZrDf2_Oz2T13YxRbR8NYqumbiPNcdR2TJC0slk5NSwrR7RDdanqj4RGFZ_nQuOXQyk598vrmlJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQDaTyEpUFf_WZx7ar3aHH1h7F3SmXM2XUTnJJA4SVCKdRtp0yo7wj0uoUV23vj1qH2nn5mpdiZKXz6hieboNgUXPV4Lmsv3Jk1gqrh-nVeuivwpzcFF-rJ4FhekuPXO3kO8iFEMVibQFhLl6tNIeQegVRcgq8v7secLivmytM6X6wf2yI2Ba7G2WZbZyJud4qRTp2oMaLSCXZx6OlpvkWSed3d__MNonTZojk5d0BkCbDfMGVu2ONzKletmEnvXIh0U8l9U-R0V0_zfYbbQo40elbVd0xzQcKtSO_frRDsKPzfYcXzV-zuSy1NZa5f_r1Mo1kxI--pPF-emF9P6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
