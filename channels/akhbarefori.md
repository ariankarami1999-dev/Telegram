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
<img src="https://cdn4.telesco.pe/file/YN5dSGrgn0AFOgOhTqYhjotqu1Shrj9vDoyrF1FbTrIcMiygQk4FA9R-Gz5_oxmnXD_QJjvuKK9q3NjqcLTKw836_PETiz7awpsvsYv2jRjPBezkZFiuKcKcvycZzJt43y2wvwKSdm4V8tV84-PUpuu5FS9RwtNAMVYAppBd6Nsb6mUWXtXMT2c6ihzS4AAOlOYkB1pWW94gYOFhjz1y4yqpHsX7e6QNdEr6lmRfWkd8vZFZzq297_lxVkkwsy5rVpyarQ7gTTXHATa2KJ-7qebidp5hpYBLYfK6SdR7TlsEkJH9OwFlIDOieE1oLQdOffQ-qrH8a1mI5OlhhEYs3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 21:07:56</div>
<hr>

<div class="tg-post" id="msg-671086">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNad165tzvxwS-UhDp9HA_xHsIc785-EP0ezdOkunsLuKRqVk4hkTzw4yzFMVOJ5IQ2OKbJpRlW0wsogPDta3xYyOCh5mO4E7IfgqYFGQYKIX5Ghek7Req6fD7w_SEcm0l0rF76bmpB82oMZjfLLu6Nbsl-b_UiKbo3d6tJb8vXoDx1I9w558v1TMaGWECCrL95N66TilG_b43rEmP6UXaK_to6y6NCFi1haDqFPau8lhaFVnOF5_0ty2tUu7Q0UFQWC1kWV4Afo1CzOKGHlYWxGle7_uMCVryZAL6Y8ibZ_aBYv655vVBGVsEwBe_Bz-Fu2TKs4cjOKFFT3iq8rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار گسترده در جنوب لبنان
🔹
نظامیان ارتش رژیم صهیونیستی در ادامه تجاوزات خود به جنوب لبنان، عملیات انفجار و تخریب را در شهرک «کفرتبنیت» واقع در منطقه نبطیه اجرا کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/671086" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671085">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
توانیر: از فردا قطعی برق برنامه‌ریزی شده در شهر تهران آغاز خواهد شد
🔹
با توجه به افزایش شدید دمای هوا و رشد قابل‌توجه بار مصرفی در پایتخت، محدودیت‌های برقی و خاموشی‌های پراکنده در تهران از تاریخ ۲۴ تیرماه ۱۴۰۵ آغاز می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/671085" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671084">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmF_5C8TQs5M5fS3FFa8gyEfCTYmZhKwjK3YcxeVXgY1nhW-AwFTfwU0IQr6YxL-1Axyx1ICXDaFPZL-DJ86FavB8C9_DIV8I5kdmZgFGZph4WqJS5MOiegW7lmAJI3rasuTdYrWTyWgi9ayNpEjYIUf8c7g_K2_7jSVILOmfWeWRoYhoF-wXLMYKqhbIiNI6gbdBFZi8GIxB7bLLCrJaEFwSX8N_DnUZqcg7s4EiIkwN_ZDVHpJRp2v_WxLt-3s43nHccDHCeJfStiPlfYToa-IDfwG0HA-Wrz1gCLIP9atXkaflsYNw5h36kNRXl_3YaLT69zNZgG2YO6LjdZTNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیت‌ دِلُم خینه
🔹
چند روزی است که جنوب ایران آماج حملات نظامی آمریکا قرار گرفته و مردم غیور این دیار با صلابت و استواری در برابر این تجاوز ایستاده اند. آنان با وجود همه سختی ها از سرزمین هویت و عزت خود دفاع کرده و بار دیگر نشان داده اند که روح مقاومت در این خاک ریشه ای عمیق دارد. مردم نجیب جنوب با شجاعت و همبستگی مثال زدنی، صفحه ای ماندگار از ایثار و استقامت را رقم زده اند. ملت ایران نیز قدردان این پایداری و فداکاری است و باور دارد که نام و ایستادگی مردم جنوب همواره در حافظه تاریخی این سرزمین باعزت افتخار و سربلندی جاودانه خواهد ماند
🔹
هشتصدونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/akhbarefori/671084" target="_blank">📅 21:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671083">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adcbdf98be.mp4?token=pGN2sqhwgb25vOvtMektGa1XkyU3YKjxBJ2kY_c61PRcFRO_bxoWB96yHecXYN-9ypwr2EHwpntrJb2a5D2C9_73kASrDXTDrXWxguVMyr7oGK0OyvdtPfC6gcCj1Wyml8b5G16jfeYENRnG8_36SnTggunlp7WLKfXVrLpWRaswFtA78phCECUuYcIC0Yx9cIjg3oelBXV4JOh-NEtlcGP454TeQhaL6AhO1g3a3OKLGkMV7a0aIufiFcTml9VhuMIi_C0eJ0rHP_tJMaPRZGFAKYnE421JhIZ66XjmYAfaPz4EeCRSM_racWH6Dxj9AHoSjJrhfUOdyiBzUwtw1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adcbdf98be.mp4?token=pGN2sqhwgb25vOvtMektGa1XkyU3YKjxBJ2kY_c61PRcFRO_bxoWB96yHecXYN-9ypwr2EHwpntrJb2a5D2C9_73kASrDXTDrXWxguVMyr7oGK0OyvdtPfC6gcCj1Wyml8b5G16jfeYENRnG8_36SnTggunlp7WLKfXVrLpWRaswFtA78phCECUuYcIC0Yx9cIjg3oelBXV4JOh-NEtlcGP454TeQhaL6AhO1g3a3OKLGkMV7a0aIufiFcTml9VhuMIi_C0eJ0rHP_tJMaPRZGFAKYnE421JhIZ66XjmYAfaPz4EeCRSM_racWH6Dxj9AHoSjJrhfUOdyiBzUwtw1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در بحرین گزارش می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/671083" target="_blank">📅 20:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671082">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در بحرین گزارش می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/671082" target="_blank">📅 20:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671081">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d1312506.mp4?token=sYsOHn5f0kqXhDIHgGiX4Qxkjd8JXsn3iSr5e7ank7wcjElNj-rGyePj82vD8vEfX0LUpkdWWl-kI7HsyY9DMWgijqo5-QMRPx7spZxmsL-olIC6m8eb5n6Dj3RELhwbqvCrbqFddd1tne78S1yNy1iDLftdkjHXqXJteoqn4QQXqyh_MRu1oqpH8ZA1ANAAcNODsSFAfypcJcHHRCAZQSSpAoiGjw7rM-dxWBXMO7UGiK7EaDqoso5UI4rHJKt3ZcTmjMpfAT3kYuFrex2OeJLW0iLMPDUxL8ulezxOYEtYejbJtW-oOzeB_fCrXo9EwFl-Lyt7WUJJ1pWWojPIIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d1312506.mp4?token=sYsOHn5f0kqXhDIHgGiX4Qxkjd8JXsn3iSr5e7ank7wcjElNj-rGyePj82vD8vEfX0LUpkdWWl-kI7HsyY9DMWgijqo5-QMRPx7spZxmsL-olIC6m8eb5n6Dj3RELhwbqvCrbqFddd1tne78S1yNy1iDLftdkjHXqXJteoqn4QQXqyh_MRu1oqpH8ZA1ANAAcNODsSFAfypcJcHHRCAZQSSpAoiGjw7rM-dxWBXMO7UGiK7EaDqoso5UI4rHJKt3ZcTmjMpfAT3kYuFrex2OeJLW0iLMPDUxL8ulezxOYEtYejbJtW-oOzeB_fCrXo9EwFl-Lyt7WUJJ1pWWojPIIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی ارتش: تنگۀ هرمز وقتی باز می‌شود که در آن ترتیبات ایرانی اعمال شود
🔹
مطمئن باشید دربارۀ تنگۀ هرمز حتی به اندازۀ سر سوزنی کوتاه نخواهیم آمد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/671081" target="_blank">📅 20:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671079">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGmNsy33cyJx7NbTxmhjYaeCyoeSg9vx35Fk2mMuGYDtYaskhKjwmUd8MP_Lz61F2IIeSvmYFRr-oo04giYVoz_qwWMGM5MrxQbOv8ZY-gBcBznG1OiIFcEbGLO7Dc70NvaztIDbm7OG0wKEFY_Kmd5ZotJ7LZULmqr9dva9lO2o-wtPlEOOddghCLLcYpMLhD7nmyUKNzJzINMitBektwDlY5Jug-WcwSm_H8h-TrsirXqS7lh1OL00cy4c3uX8LaeI3iroqIaFzloRnkmvwIBj-xr9DpUSUv9bHOq8gYAU9xKgIRKKjwCVF2rYI9RcIMYozpER_LQXplw-ajUDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsK5InA-WnrqjODbqJz_6ZKwYyJsdMt0TXHVd-8mqA2NRaMDVWC1UXKBB7MTeAg3KQFxpb2xGIgLHSqKjUQPp2703A7tKEWBFKpxlaX4puUKjU32YYyoXcNkvIBajfasKLuEse9-VApOHp3hcsDrbXqdDYrLxBl_YbTpZr_raDyeNoGKScUsKIY581z3JLbwRegRJoG04LlsAqU3s_vgXOwRTwbhrIDZPEFpl6Gk9cm2eSJNh7IcbLvOnK1yGTZ6eaDGVv2fE3-MpyKTeE0A0R84ertIK-lFAu3_ygqCbb-mCy5NxVCegleObo9naMqhzBPlbJz2C8owfJ3XJ9aavg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در سایه جنگ
🔹
گشت و گذار مردم در سواحل سورو واقع در غرب بندرعباس.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/671079" target="_blank">📅 20:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671078">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
رئیس‌جمهور جنگ‌طلب آمریکا خطاب به نخست‌وزیر عراق: ما [سردار] سلیمانی و یک فرد بد از عراق (ابومهدی مهندس) را کشتیم؛ نمی‌دونم بهتون لطف کردم یا نه؟
🔹
نخست‌وزیر عراق: در آن زمان در سیاست نبودم …. ترجیح می‌دهم دربارهٔ آینده صحبت کنم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/671078" target="_blank">📅 20:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671077">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4lbNo1clkbBxhtdBlxsky9CcbwJzYAuIhmEVK4P28NB0rJX-l_oi91RbAld56x_z4-ktnXoJgjV9aHp_9B_IsLMg0yN1lQKkeOXj5iV_hUAI-eCRs-q4fDFUJcRpNXjsH3J2XJWBCSAI53LFCvh5SukoQ48IT4K14HpYS7PYfsNNnZQI007wsgYzPWVDKfnwIffhP1rOuCJpNNfX7cxkTiNtW7QYhPV1pBQ8i1D85NRwcUpZcZl7y8EwYGmpaCxgH34Rd6_B22RZ8rpZd6bUVyfRHG_U_mZtSeLoSdcZAhMTXyTUFTRFyvMSu_KuBpvwIjhe1erK3YAYztc-CCB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اخطار مالیاتی به بانک‌های مالک مسکن؛ ۵ بانک ۵۰۳۵ واحد را در اختیار دارند
🔹
بانک‌ها در مجموع بیش از ۶۷۰۰ ملک مسکونی مازاد دارند که ۵ بانک سپه، تجارت، رفاه، ملی و اقتصادنوین بیشترین سهم (۵۰۳۵ واحد) را به خود اختصاص داده‌اند؛ سازمان امور مالیاتی این املاک را مشمول مالیات دانسته و برای واگذاری آن‌ها تا پایان سال ۱۴۰۵ مهلت تعیین کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/671077" target="_blank">📅 20:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671076">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=PTjEQmRQOmOc0Yrzgj-B_z9lre7jEqon9f0_5Q5s0WmFTJ9xmlwIXfl6TqJn1FCBGL3sXoxIhiTtAlj7dsK7Sdhjy9R40fRIi0yDaJ0s8LSryKmYWdEXMVkvbKxn5FE1uK9ybZ0fS6UI-gvm8kaQzQ3k0IjEYsgYhheUvWzgBuGCGaqy5VwpxYUMPIA4lkt-_D_GeytTi_roaajd23o083GiiPuCO_0EMRD6vJouIbKJQZGZbJv3dKtSM7FD0S8fcs5uX0cEJe02_zONr6VdtPl0ZjGG_17Yk3uCit6JdgIDMA6UGQyS0grglylfM-Q-nlvosonhTpsLbSvTpOvhPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=PTjEQmRQOmOc0Yrzgj-B_z9lre7jEqon9f0_5Q5s0WmFTJ9xmlwIXfl6TqJn1FCBGL3sXoxIhiTtAlj7dsK7Sdhjy9R40fRIi0yDaJ0s8LSryKmYWdEXMVkvbKxn5FE1uK9ybZ0fS6UI-gvm8kaQzQ3k0IjEYsgYhheUvWzgBuGCGaqy5VwpxYUMPIA4lkt-_D_GeytTi_roaajd23o083GiiPuCO_0EMRD6vJouIbKJQZGZbJv3dKtSM7FD0S8fcs5uX0cEJe02_zONr6VdtPl0ZjGG_17Yk3uCit6JdgIDMA6UGQyS0grglylfM-Q-nlvosonhTpsLbSvTpOvhPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: لفاظی‌های ترامپ را در عمل جواب می‌دهیم و از وجب‌به‌وجب خاکمان دفاع خواهیم کرد
🔹
بی‌ادبی‌های ترامپ شایستۀ خود آمریکایی‌هاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/671076" target="_blank">📅 20:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671075">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آموزش‌وپرورش: حوزه‌های امتحانی نزدیک مراکز حساس و نظامی جابه‌جا شدند.
🔹
فراجا: نیروی انتظامی در جنگ رمضان ۳۶۱ شهید تقدیم ایران کرده است.
🔹
قوه‌قضائیه: حکم اعدام ۲ تروریست وابسته به داعش اجرا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/671075" target="_blank">📅 20:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671074">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88422be40e.mp4?token=lP-xzdkAlSuGkGJ_HgqaOCab_7suo22EaSVQXmd0WmQWbAwAaPny3RRQvPorc08h81DB7EIvC6vq-Px6HtUSKWjr9YZXdfG91wz7efYWTXIevD3coB7XeSr8aSpr69uIpqpxR6KLNARgl1js-BU0HRoTfr9c8buC6Np2Kex72FN3Kl38OlehNV6ahWXSnHKvJVqLWa8UboNJj5LWNlarfKefmbbjC2tdLx1UluydVaV5iJb5uWxviEhKyx8GVDdlEq1j-Y3MPrfhlJ6MQf625rVfDns2MhfMrU1tZ4WkQxvoUtlc8sqhRIDXnI3NoVO6tFlei0naafEg5d0Au1ifQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88422be40e.mp4?token=lP-xzdkAlSuGkGJ_HgqaOCab_7suo22EaSVQXmd0WmQWbAwAaPny3RRQvPorc08h81DB7EIvC6vq-Px6HtUSKWjr9YZXdfG91wz7efYWTXIevD3coB7XeSr8aSpr69uIpqpxR6KLNARgl1js-BU0HRoTfr9c8buC6Np2Kex72FN3Kl38OlehNV6ahWXSnHKvJVqLWa8UboNJj5LWNlarfKefmbbjC2tdLx1UluydVaV5iJb5uWxviEhKyx8GVDdlEq1j-Y3MPrfhlJ6MQf625rVfDns2MhfMrU1tZ4WkQxvoUtlc8sqhRIDXnI3NoVO6tFlei0naafEg5d0Au1ifQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پاریس
🔹
حریق گسترده در جنگل‌های فونتن‌بلو در جنوب پاریس، منجر به سوختن نزدیک به ۲ هزار هکتار از اراضی و تخلیه اضطراری ساکنان منطقه شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/671074" target="_blank">📅 20:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671073">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
اعلام آمادگی مقاومت عراق برای مشارکت فوری در حمایت از ایران
مسئول امنیتی حزب‌الله عراق:
🔹
در صورت آغاز جنگ علیه ایران، گروه‌های مقاومت به‌صورت فوری و قاطع در حمایت از ایران وارد میدان خواهند شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/671073" target="_blank">📅 20:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671072">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b95fb9dbc.mp4?token=GvrXfl7facNc2Pj0CMleLZVRCzvw7dgRhHPMKSUejLAU9JDiRs06n7VL6N7MO6d_3E6Pcc4lZIUAXlQrXAtnU2rFRReLrztQja-W0FdEblpnAaT9yk411J2TkVPBtOIofZtMG0rMn4dSqMHQJ0n2VHyBBVtv-C31WVWqwYnV46QuJocMx-2o_h1LlgFpcQiI3ZGlQze8mlEwU-dYJSuP7Fi6uMzTntDurn4a3S3FBiaNpRMhj0m-EunhXxaW7ZgllhlxILc9WWHomHsTIwutB_unU3hFjC5Qmv0x0wy63YF1NPuogNitcEgTSLF71sNtwU5XbNkgAH_Y4KuDlJ296Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b95fb9dbc.mp4?token=GvrXfl7facNc2Pj0CMleLZVRCzvw7dgRhHPMKSUejLAU9JDiRs06n7VL6N7MO6d_3E6Pcc4lZIUAXlQrXAtnU2rFRReLrztQja-W0FdEblpnAaT9yk411J2TkVPBtOIofZtMG0rMn4dSqMHQJ0n2VHyBBVtv-C31WVWqwYnV46QuJocMx-2o_h1LlgFpcQiI3ZGlQze8mlEwU-dYJSuP7Fi6uMzTntDurn4a3S3FBiaNpRMhj0m-EunhXxaW7ZgllhlxILc9WWHomHsTIwutB_unU3hFjC5Qmv0x0wy63YF1NPuogNitcEgTSLF71sNtwU5XbNkgAH_Y4KuDlJ296Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام مهم سپاه به مردم اردن/ تاسیسات مهم و محل استقرار دشمن آمریکایی در یک پایگاه هوایی در اردن هدف موشک های بالستیک قرار گرفت  روابط عمومی سپاه:
🔹
ملت شریف و مسلمان اردن؛  سحرگاه امروز رزمندگان اسلام در مرحله سوم موج دوم عملیات نصر۲ بارمز یالثارات الحسین…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/671072" target="_blank">📅 20:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671071">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
از آزار یک پیرمرد در کودکی تا نجات یک جوان؛ روایت عجیب از عالم برزخ
🔹
00:06:00 تغییرِ ناگهانیِ بوی خوش به تعفن، با شنیدن وحشتناک‌ترین جیغ
🔹
00:12:00  آزار و عذاب توسط موجودات انسان‌نما در تاریکی مطلق
🔹
00:17:00 حضور منجی و دور شدن موجودات عذاب‌دهنده با صلوات
🔹
00:37:30  هیچ آتشی، مثل شرم از خطا، جان را نمی‌سوزاند
🔹
00:42:20 ماجرای شنیدنی از جوانمردی دکتر شیخ مشهد
🔹
00:55:30 کمکی که مسیر زندگی جوان را کاملاً تغییر داد
🔹
01:10:45 بازگشت به دنیا با خوردن یک دانه انگور
🔹
قسمت اول (رنج و گنج)، فصل پنجم
🔹
#تجربه‌گر
: سعید اعمی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/671071" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671070">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
صدای انفجار در اندیمشک شنیده شد/ صداوسیما   #اخبار_خوزستان در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/671070" target="_blank">📅 20:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671069">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APtoIYg9n_79I5UJVkBJgt28r5uulFHlDi7hNsDP0nWA6GN1Lkf5nKnGxI586IWSUzdIYbD38RGy2kAtuvhtyhi6NqLIXDFJ8HqGklvp9x54wF-2Yi5hajRSzfC8Ia6_dUaPCxroZ2lSaKt4ggiL8K-nLE5fXNIhV7r6tYZvi5ihdrLIhtT8-s-5yq1LOq2LFwf-oTMuohLMoJjfcY9ISUXrmwrUkk6At4IXH067sinEQ7bBrUIYtLqENXS7joCIC2bvXCKQRpyY8DZq_E_LxUWucdEgpmcSqXyRL9bQWEcOg1YkkaRAIFAZKQORbJQ9BDTdE4WNGzd6_LyaGDgcyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام جدید دونالدِ متوهم و اشاره مجدد به اشغال کانادا توسط آمریکا
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/671069" target="_blank">📅 20:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671068">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
کویت انتشار تصاویر مناطق آسیب‌دیده در شبکه‌های اجتماعی را ممنوع کرد
🔹
ارتش کویت در اطلاعیه‌ای رسمی، از تمامی شهروندان و ساکنان این کشور خواست تا از تصویربرداری و دست زدن به بقایای موشک‌ها و پهپادها اکیداً خودداری کنند و نزدیک آنها نشوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/671068" target="_blank">📅 20:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671067">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
آژیرهای هشدار حمله بار دیگر در کویت فعال شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/671067" target="_blank">📅 20:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671066">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502efd69ee.mp4?token=HSHqLTMZ6hEFiIcwkdiafQb3pAWzU-Rs8KU6rmTN257MKQRoUfry-7NVeoXgj9fBfJ_1TBxHYzvS4octscMDvIkzwESu-HqV7jST_Bm1ajIGnyuyY6zFrKasPyRMcasJFYRKP9Fk8ywpgTMQhNBdXSGUsQfddoTwW1DWb8myBv7WqHtJeb8gVydFOpepDJpVqAczep028KIQ5h2msLVNX_ZRN-6Vz5LaZm11zDn0BbD91-flr-sR9Fsfu1O51VkxrgTlcVFGuvqY4RDxx3VKWFTs7eYn5KwL85RJuteHBWt0kZJms2JhseVxR_BMg7QCW2Ace8-hqfMg3Ja1E-JjcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502efd69ee.mp4?token=HSHqLTMZ6hEFiIcwkdiafQb3pAWzU-Rs8KU6rmTN257MKQRoUfry-7NVeoXgj9fBfJ_1TBxHYzvS4octscMDvIkzwESu-HqV7jST_Bm1ajIGnyuyY6zFrKasPyRMcasJFYRKP9Fk8ywpgTMQhNBdXSGUsQfddoTwW1DWb8myBv7WqHtJeb8gVydFOpepDJpVqAczep028KIQ5h2msLVNX_ZRN-6Vz5LaZm11zDn0BbD91-flr-sR9Fsfu1O51VkxrgTlcVFGuvqY4RDxx3VKWFTs7eYn5KwL85RJuteHBWt0kZJms2JhseVxR_BMg7QCW2Ace8-hqfMg3Ja1E-JjcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از غرق شدن کشتی حادثه دیده در خلیج‌فارس
🔹
بامداد امروز برخورد کشتی فله‌بر با یک شناور دیگر در شمال جزیره قشم، منجر به آب‌گرفتگی و تخلیهٔ اضطراری یکی از کشتی‌ها شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/671066" target="_blank">📅 20:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671065">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
غریب‌آبادی: باج‌گیری و ارعاب آشکار از سوی واشنگتن برای خفه‌کردن عدالت
معاون حقوقی و بین‌المللی وزارت امور خارجه:
🔹
واشنگتن برای حصارکشی دور مقامات و نظامیان رژیم آمریکا و اسرائیل، دولت‌های عضو دیوان کیفری بین‌المللی را به تحریم، لغو روادید و فشار سیاسی تهدید می‌کند تا همکاری با دیوان را متوقف کنند؛ باج‌گیری و ارعاب آشکار برای خفه‌کردن عدالت، پیش از رسیدن آن به متهمان آمریکایی-صهیونی.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/671065" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671064">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
حمله دشمن به شهرستان دشتی خسارت جانی نداشت
فرماندار دشتی:
🔹
در پی نقض تعهد و تجاوز دشمن به کشور، حوالی ساعت ۱۳ امروز یک مقر نظامی در شهر خورموج مورد اصابت چندین پرتابه دشمن قرار گرفت؛ در این حملات خسارت جانی متوجه شهروندان نشده است.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/671064" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671063">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
لیندزی گراهام، سناتور جمهوریخواه آمریکا به‌درک واصل شد| علت: بیماری کوتاه و ناگهانی! #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/671063" target="_blank">📅 20:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671062">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbQmOpJnYmJezkkEn6iax1J_7iQbAh4HUDIry2GultS_q53e6yYMp8Rn9n7TaLZMDDp9oNVputcxGYvSptslqW2HhHV8fMzLIFsv8xFPcelhQptatWCqLfsCmlqzlS8ctRa4UHmOGXdOhv5tr7h0FnVYEXxw8va3Xdrs7aqXhRwCSLjKYcbvKAWk3miyG6vRx01GYDaYesnCHTDel9bye7knyi8bKel8wC6B7eViScNCxALSH2rT6fR-0LPbV9EV9MJIZQ9RK0yq8Eh6t9D5Pdqchsi53NS9CLUqH-sWz5gMR0JmJ0xzSiBiRh1-VNUUGMQrph5tBwW_vTjJWPFqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/671062" target="_blank">📅 20:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671061">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
نیروگاه برق جزیرۀ کیش درپی حملات تروریستی آمریکا آسیب دید
شرکت مهندسی آب‌وبرق کیش:
🔹
در جریان حمله بامداد امروز سه‌شنبه آمریکا پرتابه‌ای در مجاورت سایت تولید آب و برق کیش منفجر شده و به‌دلیل نزدیکی محل انفجار به واحدهای تولید برق، برخی از پارامترهای فنی این واحدها دچار تغییر شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/671061" target="_blank">📅 20:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671060">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
شعار علیه سازشگر و پزشکیان در مصلی تهران؛ صداوسیما صدای جمعیت را دو بار قطع کرد/ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/671060" target="_blank">📅 20:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671059">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c285ace09d.mp4?token=D3AiiSoKAf2ve44zbtypvCFOG7q8o71VL3uNbnPZmY1EaNKZivoTuDCLxr23tHpg5OO01JqCbbhKjpSSG4SOn7n9_EG0W3sgfgW2bL5EkkWMybM6dE0SKvwuu36lwHGy9izEzmCEj0_Q-4HP-IB_MB5zP_0uaiwVvPcuNR4lO4is3euK5zNcIN2VwUzMN7xo8QwuKHKeESkzpiDNUH3RR9lU9WQ8sU6O5Juj7r9QNuUDMUag-aLkEeKmMPxCeMZ-f9JWZjNedOr-Smy5p3nOyqc_t7dSCDBvXc3eu7Pm5nS3uQx4p_snUGnuKRu361lTIYT_JkMjx926I9lxEirQcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c285ace09d.mp4?token=D3AiiSoKAf2ve44zbtypvCFOG7q8o71VL3uNbnPZmY1EaNKZivoTuDCLxr23tHpg5OO01JqCbbhKjpSSG4SOn7n9_EG0W3sgfgW2bL5EkkWMybM6dE0SKvwuu36lwHGy9izEzmCEj0_Q-4HP-IB_MB5zP_0uaiwVvPcuNR4lO4is3euK5zNcIN2VwUzMN7xo8QwuKHKeESkzpiDNUH3RR9lU9WQ8sU6O5Juj7r9QNuUDMUag-aLkEeKmMPxCeMZ-f9JWZjNedOr-Smy5p3nOyqc_t7dSCDBvXc3eu7Pm5nS3uQx4p_snUGnuKRu361lTIYT_JkMjx926I9lxEirQcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: حق ندارند در صداوسیما بین دولت و نیروهای مسلح
شکاف القاء کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671059" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671058">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7vfMcA67qKTMXYdUWkBQU1aTnLiFq4qg7fmEumFL4WzZwT7p9b0I4vb6k2rSgKi9d-nRqmNN9Yy610njNRo-ncSSUdnrcXQ2qNwpWlwVMyYKuSCR0Z81kqHv3_B3QGtNjfiN7jmLARlNQIOQYtI2h--c2o7EY2jBbeoOgxPJx_yD_K52Fa8Hnb3aY0oTfndQwoUOP0ZUYj5n4H_fTBzPfD8U2HyNR1zIvLPt200J0sshyEza6vu1Uutt7ypzziUTefAiV4JlInfuihsGFvDA2O64RvZ67Exs5ykltvI_szjX2oefox8YSHQ4fIXWpgSGhMAiHQUr22InGhlKTH5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی تصمیم‌ها... فقط یک بار قیمت دارن
💎
طلای اقتصادی با اجرت از ۳٪
🏦
بانک طلا؛ خرید تدریجی، بدون سود و اجرت
🔄
تعویض طلای سالم با عیار ۷۵۰
👰
مرجع سرویس عروس با تنوع بالا
✨
بدون مالیات ارزش افزوده
📲
جدیدترین مدل‌ها
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/671058" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671057">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
استانداری هرمزگان: ساعت ۱۹ چند نقطه در جزیره قشم مورد اصابت پرتابه‌های آمریکا قرار گرفت.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671057" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671056">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای سگ‌زرد در دیدار با الزیدی: نیازی به حضور نظامی آمریکا در عراق نیست #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/671056" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671055">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epELrf4bBUZXhdwH06OoWq7HHBrolWAEpj8hxUo3nuMTCIcGjNPY_pCVtJAYRiAI-WBQiceUcvTH8zkL7yljXlGpElz8x00uzsBzcyMnaUt0upk-xkW6th4PQSxXOmdcTTg8OcMnWPRidXOTXwpbD7A_zMjO3PvL0J4J0DNl4KbKKI0ZIer0OFuB0EjRGdH_oDx_Ej_56ICiyNBS5VG2gwVNPV0mFoboipUQTepmJrxX_NmivNJcR46FGTeT0fKwL389sFkA7Sc1MG3MGjh0rbIFLKvp8b929Ve-osx9dXAqgcloDHbNqJ5sGz3GcTt-dX8TvZv94U-KJ-zspV5Hfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ایرانی سالانه ۹۳ کیلوگرم ضایعات غذایی خانگی تولید می‌کند
🔹
مالدیو، عراق و پاکستان، بیشترین ضایعات غذایی خانگی به ازای هر نفر را در جهان دارند.
🔹
ایران با ۹۳ کیلوگرم در رتبه ۵۳ جهان قرار دارد و ضایعات غذایی آن از کشورهایی مانند چین، آمریکا، هند و روسیه بیشتر است.
🔹
کاهش ضایعات غذایی، علاوه بر صرفه‌جویی در هزینه خانوار، به حفظ منابع آب، انرژی و کاهش انتشار گازهای گلخانه‌ای کمک می‌کند.
@amarfact</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/671055" target="_blank">📅 19:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671054">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سرنگونی پهپاد پیشرفته «وینگ‌لونگ ۲» سعودی در یمن
🔹
سخنگوی نیروهای مسلح یمن از هدف قرار گرفتن و سرنگونی یک فروند پهپاد جاسوسی متعلق به ائتلاف سعودی در آسمان استان «البیضاء» خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/671054" target="_blank">📅 19:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671053">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
صدای انفجار در اندیمشک شنیده شد/ صداوسیما
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/671053" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671052">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
حملات جدید به کویت؛ صدای انفجارهای شدید و آژیر خطر به گوش می رسد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/671052" target="_blank">📅 19:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671051">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای سگ‌زرد در دیدار با الزیدی: نیازی به حضور نظامی آمریکا در عراق نیست #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/671051" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671050">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
دود شرق تهران ناشی از آتش‌سوزی یک منزل قدیمی در خیابان دماوند است
سخنگوی آتش‌نشانی:
🔹
دودی که در بخش‌هایی از شرق پایتخت مشاهده شده، مربوط به آتش‌سوزی یک منزل قدیمی در محدوده خیابان دماوند است.
🔹
اطفای حریق در حال انجام است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/671050" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671049">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
دیدار نخست وزیر عراق با ترامپ
🔹
علی الزیدی، نخست وزیر عراق که به واشنگتن سفر کرده، در کاخ سفید مورد استقبال ترامپ قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/671049" target="_blank">📅 19:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671048">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
صدای انفجار در قشم
🔹
صدای دست کم ۵ انفجار در جزیرهٔ قشم حوالی ساعت ۱۸:۴۵ شنیده شد. ماهیت انفجارها مشخص نیست.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/671048" target="_blank">📅 19:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671047">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i07g4P0Dy27NfslIgvpaAmLwaNqR95Dxpbsb_9GhrnSdy_7g_KbudiZOEul7Qkj-x5wU-qQazIql40LuqvM42NPupg7Xcnmv9Hztx1CChihrG7wyCdXeoMfIB9ftlxCIpcr5t0BkKj-xvgZ8yukYlaN53opDcFCdstG9f8rb9Jtjbd58YP1n2-lC7aK6tuTZiaprsUcHaMNnuBkd1EFWD4MXA7iEKkyTZN5TLSFuiVzYWDHEiDCRiMuJvGw8qjIq86dVjpXfgYRl-F79nqiSqMo9i2tQkj4UkpqdRmdQgR31-m-bjk5tPeKR6MUbw38G4p5rOutZf-w5LxN-lQocCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رامین رضاییان با کیف لوکس Hermès Birkin ۴٠ دیده شد
🔹
قیمت رسمی این کیف در بوتیک‌های هرمس حدود ۲۰,۵۰۰ دلار است و با نرخ فعلی ارز، ارزشی نزدیک به ۳ میلیارد و ۷۰۰ میلیون تومان دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/671047" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671046">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c82c869464.mp4?token=DfCrcpkfketfUE1IQtMUttQ0O3A8iJz7Ul-FhntU0GKy8EPny4_92RD0dKlOIeVkAiTCeVI8Md0VwZd0JRDtLO14s8YnUcGOBZkch2mDeBZjaOyZVswoK0Hzb4RF9Kol4TA9NQr7yLHRvrOUnSpkRnDryCnctuGQ2_TNIJuEKzgmNyO5WRyK_S0N0UiuTOne-6xXzYtNzL06Dk_xNUsSW9ujuwI49wNOaQdFL2Zbft7px7XrTWR1a75p4pM9hY7GGncDEPGohU1-6n7m8v0PQvZePXNkaLjRBw_Ou3qMsfOsxQ-b5JQAItc2-FkOcbGvxbVHQdnQdMSKaAuqW8o_P7v-OPc6DzsuU8sbqXzWD5tzs7F6WQUNgfiWlZs4lpf6YA0m5oTtkBw_TksYfOQMzJIcjeyeaVwL-xcrKMPOYDosqGZ7Nf_ptU0YZeLnoSNX1ExHgU_tQSlyR8nXPxaZ7q8VorqNeMr1GbG-SOZStWI3wYlBrfkFcOrul0X4gtXb_TOtsrozGVvmvbzq_RButWR-hoB8vOIEw6ES3bdOS5cRzS1GlxErBu39SgQruN3wHq0ojdfS-mRSBRVyqqAUxbGBAmzS_sEBiXy6E8ETjjzzjY5jiTMIZ-NQtS7g7fp5SwddopV9ddmhTQPNnYwG9SyGvbLIrNAzzIE78wH6ffg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c82c869464.mp4?token=DfCrcpkfketfUE1IQtMUttQ0O3A8iJz7Ul-FhntU0GKy8EPny4_92RD0dKlOIeVkAiTCeVI8Md0VwZd0JRDtLO14s8YnUcGOBZkch2mDeBZjaOyZVswoK0Hzb4RF9Kol4TA9NQr7yLHRvrOUnSpkRnDryCnctuGQ2_TNIJuEKzgmNyO5WRyK_S0N0UiuTOne-6xXzYtNzL06Dk_xNUsSW9ujuwI49wNOaQdFL2Zbft7px7XrTWR1a75p4pM9hY7GGncDEPGohU1-6n7m8v0PQvZePXNkaLjRBw_Ou3qMsfOsxQ-b5JQAItc2-FkOcbGvxbVHQdnQdMSKaAuqW8o_P7v-OPc6DzsuU8sbqXzWD5tzs7F6WQUNgfiWlZs4lpf6YA0m5oTtkBw_TksYfOQMzJIcjeyeaVwL-xcrKMPOYDosqGZ7Nf_ptU0YZeLnoSNX1ExHgU_tQSlyR8nXPxaZ7q8VorqNeMr1GbG-SOZStWI3wYlBrfkFcOrul0X4gtXb_TOtsrozGVvmvbzq_RButWR-hoB8vOIEw6ES3bdOS5cRzS1GlxErBu39SgQruN3wHq0ojdfS-mRSBRVyqqAUxbGBAmzS_sEBiXy6E8ETjjzzjY5jiTMIZ-NQtS7g7fp5SwddopV9ddmhTQPNnYwG9SyGvbLIrNAzzIE78wH6ffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله سیدمصطفی خامنه‌ای: صبر در این مصیبت بزرگ هیچ منافاتی با انتقام و برخورد با اشرار عالم که در این جنایتهای بزرگ دست داشتند نخواهد داشت
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/671046" target="_blank">📅 19:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671045">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbRcXEGitrx7heEKdaPsK1Z1gAljSmSj3IFaYFAxo4gGA10UAxBFIt6EEv-YxAKG33h_XYE-QBRXK2Ih6ahRDXepOdAoMaskrwqrFs2n-DLEa0bFQg_N7o1VWTweg6K7tJOCvmj_XPEKAIFLAA8rBGCL6SaabajkwvUtQB12QJnPGN3GVOTtMuIS4nGboSIQTlP7Ot_o0sHEUYgRwGB-LF9S2KrrzcWqh3lIsCRMorV8-6f95JoTW1E4x-kRGcYztOP2ylZPlwflRPQOTSDicIRpqHAaRt8yIZ8raR6xFWZLOwlUXdFkzCidGv6U_AG1NCrAAYqpCeoqY9F2O4wtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
خريد و فروش طلا
صندوق بانك گردشگري
صندوق اندوخته آميتيس
صندوق درخشان آميتيس
‎روبیس با دریافت مجوزهای لازم بستری امن و قابل اعتماد برای سرمایه‌گذاری فراهم کرده است.‌
https://rubisinvest.ir</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/671045" target="_blank">📅 19:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671043">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971cb6b758.mp4?token=iNEEOrTYgdW1c7jafq3m9RMq_-ASRCtA9CtCxtdlzxdkNppQwYetw8Zon0j3Ws-5aIKOxW4F2A3kV-HyOaV_TYK7vIB_cD_Jxt72FoRhI1n_GDPwJY7Sb9Zo0Ct9gWBwPXwVEhrx3nGKE4nUrGoTEqd1C3ukpkvw7hlg4xbG7_4p_fxJajOtcwXw9Wmit9JMci3_KgnrSwb5Aw-3eqNtQu08196lvc-vymfWFXgoZg0jBObI4IsjU4V4Is5v0xUBTf1xuYYcIyR7UsLmRe3Yw6JGqwnDC4Oqxzh9jPxn08QeBpEmc4r1Azph62aHhC0cSj7-sAvTGfpOxopbnrNDVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971cb6b758.mp4?token=iNEEOrTYgdW1c7jafq3m9RMq_-ASRCtA9CtCxtdlzxdkNppQwYetw8Zon0j3Ws-5aIKOxW4F2A3kV-HyOaV_TYK7vIB_cD_Jxt72FoRhI1n_GDPwJY7Sb9Zo0Ct9gWBwPXwVEhrx3nGKE4nUrGoTEqd1C3ukpkvw7hlg4xbG7_4p_fxJajOtcwXw9Wmit9JMci3_KgnrSwb5Aw-3eqNtQu08196lvc-vymfWFXgoZg0jBObI4IsjU4V4Is5v0xUBTf1xuYYcIyR7UsLmRe3Yw6JGqwnDC4Oqxzh9jPxn08QeBpEmc4r1Azph62aHhC0cSj7-sAvTGfpOxopbnrNDVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار قاآنی در مراسم بزرگداشت رهبر شهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/671043" target="_blank">📅 19:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671042">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
آسیب به تأسیسات برق کیش در پی انفجار پرتابه‌ها؛ احتمال خاموشی موقت
شرکت آب و برق کیش:
🔹
در پی انفجار پرتابه‌ها در نزدیکی نیروگاه برق جزیره، برخی تجهیزات فنی آسیب دیده و در حال بررسی است.
🔹
ممکن است برای انجام تعمیرات، تعدادی از واحدهای تولید برق از مدار خارج شوند که در این صورت خاموشی‌های موقت و زمان‌بندی‌شده اعمال خواهد شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/671042" target="_blank">📅 19:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671041">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
اطلاعیه دولت: مراسم بزرگداشت امام شهید انقلاب که مقرر بود روز چهارشنبه از سوی دولت جمهوری اسلامی ایران برگزار شود، به روز یکشنبه ۲۸ تیرماه، ساعت ۱۰ صبح موکول شد
🔹
این مراسم به میزبانی قوای سه‌گانه کشور در مصلای بزرگ امام خمینی (ره) تهران برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/671041" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671040">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در کویت
🔹
منابع رسانه‌‌ای از حمله موشکی به اهداف آمریکایی در کویت و شنیده شدن صدای انفجارهای پی در پی خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/671040" target="_blank">📅 19:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671039">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در کویت
🔹
منابع رسانه‌‌ای از حمله موشکی به اهداف آمریکایی در کویت و شنیده شدن صدای انفجارهای پی در پی خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/671039" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671038">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
صدای انفجار در قشم
🔹
صدای دست کم ۵ انفجار در جزیرهٔ قشم حوالی ساعت ۱۸:۴۵ شنیده شد. ماهیت انفجارها مشخص نیست.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/671038" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671037">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYuM30mASMz2XDniZLrvk4waHekZUuRyFaCKF1Xztm16nYLjPI3jP3npQpwB1OsOpGljorVmalJk-SDmxqTMsKz-bpthh6aKik8ea6twRPF1el92LA2HfeAGK3HnqNt0RLwcVaoO8nMuKYnzv-SSh3mKmN2f_aXzh1XOf3ehd6BSitB2fApBkYfEPmC47kjPK5ICqgtm3AZWqBOvYkO8waN7SlgAI14o29ymazITsmB7cP99zaONJFpy6VuAe4bRlelqVIxYlL9o6qMVNv6x5xBUoFlGusM4p4ypw2RV61D3HvyswklMc6lKUHkLJAakEcKjh96JObCA3SRx6TIEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/671037" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671036">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
خبرهایی درباره حمله به نفتکش اماراتی در سواحل عمان
🔹
این منابع گفتند نفتکش «البهیه» امارات در ساحل عمان هدف قرار گرفت و نهاد امنیت دریایی این کشور خبر داد سه نفر از سرنشینان این نفتکش مفقود شده‌اند.
🔹
در حمله بعدی هم یک نفتکش مستقر در امارات متحده عربی با پرچم لیبریا هدف قرار گرفته است.
🔹
امنیت دریایی عمان خبر داد که ۲۱ نفر از سرنشینان این نفتکش هم موفق به خروج از آن شده‌ و نجات یافته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/671036" target="_blank">📅 19:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671035">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4cv5DCJ-B0JoTXq0TQP42fFgkuMHCU7ccV2RIGVvomd04cUZxpBCgGNIC6q8CJDjQ50v_plVNovo_KO0G5b-DVSgKm6Gm8967ZMuucEW0DzktBJvRp84gidMdoRuvgsx64uUtIlOXzGBo0dukIJOjVZwIXdx4hB7OVul23Sj5Ml_Q_cmkIKwLEqg7_QzU5QSmIwEzR9LxeD7t6T5U4ZY-28Y5S_2RQiHKVIxc5uhz9fA-YNe7sQP2qauGLDVEzbdykPzO_EGuxw-NbKRybF0Oxz5lD3SfSNANI6Pr9HnjFo3_q4LFM2WoOfWbu9demuT4QR2uoLGjArdFdpjMaeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/671035" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671034">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abecbc4c7d.mp4?token=OiB2Mxv2WUTAgy9n5C_g-muhsPZjREp0p4RrqePs8iAdsxUEzA_JAhg8X6_Och1guKC3mro4CUUF6QjKfCflY9Ok6LSvBkm49NLFcLaBzid_Upuy2gqs0zZNpbfAeUKwyGBf9JvmOXuXVtrWQ-mY5uyWuyuSLGGfrdZ2hCqIbTHQnr19EZeDnOu7Ta5DJ90VJez_5oGMST-TjKFtMWASwqMa_7J40cmQdjFeetGQ1yxdW7Sv8XkzakIDDWP-5QtJeK5qY7-NeAWfj8RY68nOdWNGoae-ShFNH2XMbmRlRIVCKaMm2Y9lGyYdwDQw66lhj1I2llg_raLjVeXWes88mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abecbc4c7d.mp4?token=OiB2Mxv2WUTAgy9n5C_g-muhsPZjREp0p4RrqePs8iAdsxUEzA_JAhg8X6_Och1guKC3mro4CUUF6QjKfCflY9Ok6LSvBkm49NLFcLaBzid_Upuy2gqs0zZNpbfAeUKwyGBf9JvmOXuXVtrWQ-mY5uyWuyuSLGGfrdZ2hCqIbTHQnr19EZeDnOu7Ta5DJ90VJez_5oGMST-TjKFtMWASwqMa_7J40cmQdjFeetGQ1yxdW7Sv8XkzakIDDWP-5QtJeK5qY7-NeAWfj8RY68nOdWNGoae-ShFNH2XMbmRlRIVCKaMm2Y9lGyYdwDQw66lhj1I2llg_raLjVeXWes88mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار نخست وزیر عراق با ترامپ
🔹
علی الزیدی، نخست وزیر عراق که به واشنگتن سفر کرده، در کاخ سفید مورد استقبال ترامپ قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/671034" target="_blank">📅 18:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671033">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
پلیس فتا: احراز هویت خریداران در معاملات آنلاین الزامی است
پلیس فتا:
🔹
در هنگام ثبت آگهی در سایت‌های فروشگاهی و یا انجام هرگونه معاملات آنلاین، احراز هویت خریداران و واریز کنندگان وجوهات از سوی فروشندگان و یا ارائه دهنگان کالا و خدمات الزامی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/671033" target="_blank">📅 18:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671032">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a05e1e5a.mp4?token=LjGBogCv-YbWUPOSVg-zfiPtWUP3yoIrundI3284BBpgrm6b6-63Rdr2gMzFh5RFoIy-M3peYrJk6ond28AHXfaio0w9DPJvDOU9fWCZzv-gRcspF1HfB8his6Gg8_XoTsGZKcu1UE6nd2m2PdhiEo7muh_nmzPiAOX208LiJdcs3Ir7S1_gOep5DOtoV7LLGtJIadoS0ABSG2UgvV-RADel_QDIKG2WSfasfqGpxnvblBw-vc9rGiDJ5WQeIBA5GunVsQp_c4W0Iqnw9fY9rnek-czRfVyRCWhF7q0hx1UKkrG3Y-qZxsAmSKJkybX_oWZ-la0smYoJgpvEJJc8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a05e1e5a.mp4?token=LjGBogCv-YbWUPOSVg-zfiPtWUP3yoIrundI3284BBpgrm6b6-63Rdr2gMzFh5RFoIy-M3peYrJk6ond28AHXfaio0w9DPJvDOU9fWCZzv-gRcspF1HfB8his6Gg8_XoTsGZKcu1UE6nd2m2PdhiEo7muh_nmzPiAOX208LiJdcs3Ir7S1_gOep5DOtoV7LLGtJIadoS0ABSG2UgvV-RADel_QDIKG2WSfasfqGpxnvblBw-vc9rGiDJ5WQeIBA5GunVsQp_c4W0Iqnw9fY9rnek-czRfVyRCWhF7q0hx1UKkrG3Y-qZxsAmSKJkybX_oWZ-la0smYoJgpvEJJc8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«فکت‌چک» برنامه تلویزیون اینترنتی مدار برای کشف حقیقت از میان شایعات روز
🔹
تلویزیون اینترنتی مدار در روزهایی که اخبار و اطلاعات با سرعتی بی‌سابقه منتشر می‌شوند، با ساخت و پخش برنامه "فکت چک" راهی برای تشخیص واقعیت از شایعه باز کرده است.
🔹
«فکت‌چک» برنامه‌ای است برای بررسی و راستی‌آزمایی ادعاها، خبرها و روایت‌های مطرح شده در رسانه‌ها و فضای مجازی که در تلویزیون اینترنتی مدار تولید و پخش می‌شود.
🔹
در هر قسمت، با تکیه بر منابع معتبر، اسناد و شواهد، به دنبال کشف حقیقت و روشن شدن واقعیت‌های پشت پرده خواهیم بود.
اینجا مدار را تماشا کنید
👇
www.aparat.com/MADAAR_TV
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/671032" target="_blank">📅 18:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671031">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NceZuCnELZSvy6IFSDoLH0NzBrtdRr6ckqYQAGX8QU14idUhTEIy6v7mbx5TgFz3IDYOKnL81HUpktYaivCPqVY8hm2JCLw1ahlzSfAXLB3VBSQ_x-ZH7vUpDX89gH04qInc_xYxTCWrmYGf00tU80H8huV3cKNb-1w3DJv1MM3GS__OhPM8Df1DxCGf-xITpBblEIVsup76rilvcX1Ym1RWcb8jW-ORjXI0k9CQ7v-wSDxZjuZI7-p-oPDOi1sRsPdRP5uNmuXJRywQCjo5ymBdNdP44v6ocamtJOeUpLLJnX9-XUxTP21g9XRn5srz5fiqr2NIOgzWpRtnhEtTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار از عوارض ۲۰% تنگه هرمز عقب نشینی کرد
🔹
«تصمیم گرفته‌ام که هزینهٔ ۲۰ درصدی بازپرداخت ایالات متحده را با قراردادهای تجاری و سرمایه‌گذاری جایگزین کنم که کشورهای مختلف حوزهٔ خلیج [فارس] در ایالات متحده انجام خواهند داد. آن سرمایه‌گذاری‌ها بسیار کلان (عظیم) خواهند بود.»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/671031" target="_blank">📅 18:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671029">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np0LMYcl7o1vrOTjtHiv-YJxQyrY9kms9SoDwqVTzWU426oIS0eWrVWUdLhJv4GK89VpG229k8DQrxx3ytaVpAxJHsbsC5VodWfrwsGMIdjn82pHrMpdHxVryLIvvQobt1Pqa0MJp0VD7kSk58WHoAqhO4Uo31hZrp0cAgcBT5LCjjT6ARnSSmuvFnpqWppYDpK0Uw1ji3bG8DUViZBLG0czR5Ff0SO6-Bnt79gNYX4rv5VdZcmiAozQqNTuSR4DKVKJLQd18tU_-LkMlM4EO7iTBw5foKilkesHwsxSY5RLmWdVCBNTHWe-fmXNwcq6hgKBSvs3SyGMHG_pIEO6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاش خواهر زیدان، ایتالیا را ببخشد | نیمه‌نهایی؛ جایی که همه پیش‌بینی‌ها می‌میرند | فوتبال عادلانه نیست؛ راز جذابیتش هم همین است | فینال آرژانتین و فرانسه؛ تنها پایانی که جام را نجات می‌دهد | همه چیز درباره نیمه‌نهایی
🔹
حرف زدن از فوتبال آن هم در این‌ شب‌های داغ جام جهانی همصحبت خوب می‌خواهد. کسی که هم خاطره بصری بلندمدتی داشته باشد و هم پای ثابت فوتبال باشد و البته که فوتبال برایش فقط محدود به فوتبال نباشد!
در خبرفوری بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3230294</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/671029" target="_blank">📅 18:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671028">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e4352e2e.mp4?token=ifYine3JH5FMA2gOzAQLcUj708y7wF-OEqYYxqvKHBGMEOlbWFPIraNAldsr8OaSTxJo0h0ldm8Kg9TQl2XXDSHfZZ9-I-uzSD14BPXimjjSHFVFP5iMoEPI0Yhi3BxtEPJy9Q5ZwdZlqMX-77IFXRt_hO83qg040JWkIMp4KAoZgajT7E0MbF1MWMNhevG66-du3fkB5z9lCBLI1IDJc-kfIr7g__G1mDRewIf0qFBGIBcr8-pOG-10VZTg1Y-5Mkx5V4Kns5QCmu1NKe25vHdwwopWL7hfj01g8pp1pZGomyb6K4WkMtNOGAu0XNYjoZQS9krgp3fvQYtcCKUp5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e4352e2e.mp4?token=ifYine3JH5FMA2gOzAQLcUj708y7wF-OEqYYxqvKHBGMEOlbWFPIraNAldsr8OaSTxJo0h0ldm8Kg9TQl2XXDSHfZZ9-I-uzSD14BPXimjjSHFVFP5iMoEPI0Yhi3BxtEPJy9Q5ZwdZlqMX-77IFXRt_hO83qg040JWkIMp4KAoZgajT7E0MbF1MWMNhevG66-du3fkB5z9lCBLI1IDJc-kfIr7g__G1mDRewIf0qFBGIBcr8-pOG-10VZTg1Y-5Mkx5V4Kns5QCmu1NKe25vHdwwopWL7hfj01g8pp1pZGomyb6K4WkMtNOGAu0XNYjoZQS9krgp3fvQYtcCKUp5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف قزوینی؛ شاعر وطن‌پرست دوره مشروطه
🔹
عارف قزوینی فقط یک شاعر یا خواننده نبود؛ صدای خشم، وطن‌پرستی و آزادی یک نسل بود. با تصنیف «از خون جوانان وطن» نامش در حافظه ایران ماندگار شد. هنرمندی سرکش و میهن‌دوست که با شعر و موسیقی علیه استبداد شاهنشاهی؛ از…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/671028" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671027">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzx-UfkXroPRnd9DhxZyHp8gLwd4SJteQymfHMhPNtpmOWzVzyHNvmjzUEsQ98PgDNK8KNEr4LpCsdBBxW3XL48O-TsiinE5D0t4Y09i42KhGxHC2Wzq6PHeC-BIFvLs7Rd9BWOjqcMzBnmgMVIGSeDyKvvgTSCZkUL7KpdsYe4v0pjdCs4rpdWgjBZVQeL_xmD4EpP8K6xzXk_nK0R1m2TIZBFkR6-YSpKtcgP1QjCWsdVSS4CjGbH9oGsrOgwuDAqUfyDf2xmkGvFaiNWM7sG8Leg2pLBqpOL_o9VdGwiwBouVcxsU6k7iiztRHAWGpmgzJXfZPmbwsIUXTnXo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصطلاحاتی که بهتره وقتی میری کافه بدونی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/671027" target="_blank">📅 18:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671026">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
امکان تغییر محل آزمون پزشکی داوطلبان اهواز، بوشهر و بندرعباس
وزارت بهداشت:
🔹
داوطلبان حوزه‌های امتحانی اهواز، بوشهر و بندرعباس در صورت تمایل می‌توانند از ساعت ۱۴ روز سه‌شنبه ۲۳ تیرماه ۱۴۰۵ تا ساعت ۱۰ صبح روز چهارشنبه ۲۴ تیرماه، حوزه امتحانی خود را صرفا به شرحی که در ادامه آمده است تغییر دهند:
🔹
حوزه اهواز به لرستان
🔹
حوزه بوشهر به شیراز
🔹
حوزه بندرعباس به کرمان
🔹
آزمون فوق در حوزه‌های اهواز، بوشهر و بندرعباس همچنان برگزار خواهد شد و  این مهلت قابل تمدید نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/671026" target="_blank">📅 18:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671025">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
پاداش ورزشکاران مدال‌آور در بازی‌های آسیایی اعلام شد
کمیته ملی المپیک، پاداش پای سکوی ورزشکاران مدال‌آور در بیستمین دوره بازی‌های آسیایی را به این شرح اعلام کرد:
🔹
مدال طلا: ۳ میلیارد تومان
🔹
مدال نقره: یک میلیارد تومان
🔹
مدال برنز: ۴۰۰ میلیون تومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/671025" target="_blank">📅 18:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671024">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c0d02ae7.mp4?token=bunkqoLZlFwWRLHoc7lg2lkVfgSSnPScjVqS53ZJVpwMwo1YOhrLNSdJk1aJpT_wahUTn3S9e_evJWQIp00m-BAsmMWjhGhp2_tqCmJYIPhi3ZqVPAqGve9q3EeJ8WXSu3xRnr43l_6M6D_irtlkfxRnc2pelK47pHY-h-VIdI93EpEtjDQH0jlW4kRJxggZ_WDkdtXotmKRrkUVLjaQDQhdV77oE6qTX9YR3lYjMQLFten76pTQYgrI42euhzJnAEgg06x_FHOMZmDd4Lq6HmwqFDJuteVgT51GO1n2-9AlcLsuZQuURQ-gFxjnU7sKe52wbdB8_zNp8y1flGQULw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c0d02ae7.mp4?token=bunkqoLZlFwWRLHoc7lg2lkVfgSSnPScjVqS53ZJVpwMwo1YOhrLNSdJk1aJpT_wahUTn3S9e_evJWQIp00m-BAsmMWjhGhp2_tqCmJYIPhi3ZqVPAqGve9q3EeJ8WXSu3xRnr43l_6M6D_irtlkfxRnc2pelK47pHY-h-VIdI93EpEtjDQH0jlW4kRJxggZ_WDkdtXotmKRrkUVLjaQDQhdV77oE6qTX9YR3lYjMQLFten76pTQYgrI42euhzJnAEgg06x_FHOMZmDd4Lq6HmwqFDJuteVgT51GO1n2-9AlcLsuZQuURQ-gFxjnU7sKe52wbdB8_zNp8y1flGQULw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سفرای کشورهای خارجی در مراسم گرامیداشت رهبر شهید در مصلی امام خمینی(ره)
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/671024" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671023">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MM-xJCq3T84lv9tOpIM8mkRZgsNT4yEeWoNzcrBbOwBf9CCJVMLInyseneC2-RDBMstog_So6M6NQayxYrT10SYWdptaXAwe1oA6IVM7_6-jvTPZdH4g8bqMh1FueEP9vPNg0ekj8hTYULqmPge6xBJeUDTiHzJH28lW8q9hw6QCE0VP69BNWJFC4gO9VLuFxD0wpoNLaXXitkYL1GbHHLAdQMf1Uxn4AEMz6V9_UkoRXy-QGSYdXu49BI0nJptqakepHTmSFEpwVdXyM4ufyD1NFWfTKYz7bDtl_H-N-sBY_VDPP_TKTatATQSzK5a8p5YbzX7YQRUt1P3TS63TfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا تنظیم‌گری بازار آنلاین طلا به سرانجام نمی‌رسد؟
🔹
خبرگزاری فارس نوشت: ماه‌هاست مقررات این بازار میان دولت و بانک مرکزی در رفت‌وآمد است. تازه‌ترین اختلاف نیز به تفاوت میان مصوبه هیئت وزیران و ضوابط اجرایی بانک مرکزی درباره نحوه نگهداری طلای کاربران بازمی‌گردد.
🔹
بازاری که میلیون‌ها ایرانی در آن سرمایه‌گذاری کرده‌اند، بیش از هر چیز به مقرراتی شفاف، پایدار و قابل پیش‌بینی نیاز دارد؛ نه ابهام و تغییرات مکرر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/671023" target="_blank">📅 18:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671022">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl5yNTT7o9ZKJPwZCTLrTBmQg5t7rUJiGz8hcOyfs9t--xNhxpZfclvb_Ou_bJfc5AuuDR8FKBFq3EOtlFy4zzilT5DXRRvBVFITxl2ZNQfQ2K3nwo-lCQrutd74EcygLerABDNcxKhcyvwIS54_kgvYubuEsJOoyeP89vLBJFGlJ69TN8kmUG-YAzKE6MrS268blQV4EJY_D4zzmjYBn1AzRupWCRM3qJMSoeBf1-uaZLLzAWllGTnTex-AvqFjlm515Zi_LFWR-NmkWvoX0H3Osp2ZHQOKf967pe5f7Q-PUO3L5b-Hs871LSi9nGzTt-c0L0cMvIo7PIJAFyr5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک زرد ری‌پست کرد: جزیره خارک رو تسخیر کنید!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671022" target="_blank">📅 18:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671021">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
بریتانیا طرح ترامپ برای دریافت عوارض از تنگه هرمز را رد کرد
🔹
دولت بریتانیا پس از ادعای ترامپ مبنی بر کنترل تنگه هرمز و دریافت عوارض از آن، امروز اعلام کرد موضع خود را مبنی بر اینکه تنگه هرمز باید «بدون عوارض یا هزینه» بازگشایی شود، تکرار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/671021" target="_blank">📅 18:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671020">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03e544f40.mp4?token=cjUxx2_DZaQYG8jzSwVWsGNkxuNR8YuPujaAWwBYIsPFyLjGRvsxH-e_h7M30Lh_M3lzND1sAZ7Tz7klemkV8W-31iMgTLRRvm3UDX6HQXDsmzFvsC3EJ1CedqEHQQptlY8xMY67o3rKSzsPzfXk7Y1evnudPmnaQ92-9ZqCxZgictisz2eunJw5pR3ntqB0UaUP0tvjSH4a0ZkYf6TINgk0CeM3YpRPy4psl3tFQFvoWfDGfiRZsVDmw_nnQHSjwwnsvsOv3cLH-kIJZnD8xCVI8vwuLp3xL5-Au13gNEWWkqUOIcTy6WVeOBaoaX5I3ZoQFLALRCRQfxqZ3N-qZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03e544f40.mp4?token=cjUxx2_DZaQYG8jzSwVWsGNkxuNR8YuPujaAWwBYIsPFyLjGRvsxH-e_h7M30Lh_M3lzND1sAZ7Tz7klemkV8W-31iMgTLRRvm3UDX6HQXDsmzFvsC3EJ1CedqEHQQptlY8xMY67o3rKSzsPzfXk7Y1evnudPmnaQ92-9ZqCxZgictisz2eunJw5pR3ntqB0UaUP0tvjSH4a0ZkYf6TINgk0CeM3YpRPy4psl3tFQFvoWfDGfiRZsVDmw_nnQHSjwwnsvsOv3cLH-kIJZnD8xCVI8vwuLp3xL5-Au13gNEWWkqUOIcTy6WVeOBaoaX5I3ZoQFLALRCRQfxqZ3N-qZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت سه عضو خانواده یک محیط‌بان هرمزگانی در حمله آمریکا به دکل محیط‌بانی حاجی‌آباد
🔹
صبح امروز در پی حمله آمریکا به دکل محیط‌بانی منطقه حاجی‌آباد در استان هرمزگان، سه عضو خانواده یکی از محیط‌بانان این منطقه به شهادت رسیدند.
🔹
بر اساس گزارش‌های منتشرشده، دو فرزند پسر این محیط‌بان به همراه عروس خانواده در جریان این حمله جان خود را از دست دادند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/671020" target="_blank">📅 18:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671019">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
سازمان بازرسی آثار حمله سایبری به چهار بانک کشور را بررسی کرد
معاون نظارت و بازرسی امور اقتصادی سازمان بازرسی:
🔹
هدف اصلی سازمان در شرایط کنونی، کمک به بازگشت هرچه سریع‌تر ثبات به شبکه بانکی، رفع مشکلات ایجادشده برای مردم و پیشگیری از تکرار اختلالات ناشی از حمله سایبری است./ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/671019" target="_blank">📅 18:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671018">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f592965c1.mp4?token=QteRQtzTLKZLlcH159ZZhanrwBUOGbDAeIdcDi_QBzqwjVzx1CV_RVNv8rlF4apRJo5EXDh_xmsBbL_lhJdvM22eR0qS_2mhdaR01DqH9ZY2xGedJglxVNGYK7qDCqYY8O75j3sbVRWpGdz9O8EuogeC23V1fjdG0fmhqiLozDxa8jRMtoLXrDU1y1ZDNc9-Y2MU872qtwHBH7N_fKi-9pnvM7vvd63p7EAkOL05Hh88jGC0YvaENRZyRUqcX1rM-XJIqDthEVAxId1Iw0lr3L1x4s7kCHorPCXKUAlS3TWWhSzfCI42zg1HHlsjzOUP8IbIysegp-4mQVBMtEHyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f592965c1.mp4?token=QteRQtzTLKZLlcH159ZZhanrwBUOGbDAeIdcDi_QBzqwjVzx1CV_RVNv8rlF4apRJo5EXDh_xmsBbL_lhJdvM22eR0qS_2mhdaR01DqH9ZY2xGedJglxVNGYK7qDCqYY8O75j3sbVRWpGdz9O8EuogeC23V1fjdG0fmhqiLozDxa8jRMtoLXrDU1y1ZDNc9-Y2MU872qtwHBH7N_fKi-9pnvM7vvd63p7EAkOL05Hh88jGC0YvaENRZyRUqcX1rM-XJIqDthEVAxId1Iw0lr3L1x4s7kCHorPCXKUAlS3TWWhSzfCI42zg1HHlsjzOUP8IbIysegp-4mQVBMtEHyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
قطعی برق؟ تاریکی دیگه دردسر نیست!
🔦
چراغ شارژی خورشیدی
تاشو با طراحی کاربردی، مناسب برای خانه، سفر، کمپینگ و مواقع اضطراری.
✨
ویژگی‌ها:
✅
شارژ با نور خورشید و USB
✅
طراحی تاشو و کم‌جا
✅
نوردهی قوی
✅
مناسب برای قطعی برق، خودرو، ویلا و طبیعت‌گردی
🔥
قیمت قبلی: 1,598,000 تومان
❌
💰
قیمت ویژه: 1,098,000 تومان
✅
⏳
این تخفیف برای مدت محدود فعال است.
🛒
برای مشاهده مشخصات و ثبت سفارش، روی لینک زیر کلیک کنید:
👇
👇
👇
https://memarket24.ir/product/brief/47540/180124/</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/671018" target="_blank">📅 18:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671017">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e44ec578b.mp4?token=LtxX-xfjnmhHNyrvHcQhubmsL9WsTjy_Zk_H2JsELfB9xRv0R1v3Yxlbcui2ak5ifkXECRwmNhN133C93zlbX1T7nMv7t119G_QX_J0yDcQRcb7pkzYh-Zvd5GH6KcE3IeMRyLaA70yqxQT_GYjJEOdpuVKkEpvGi2ETVkAJYmiBd64km3Q9NbhjwZaSqFF1a-r_r8xami7AXt1VuSG0x9r2UFkybJOPlhxCDu3OYvANTbVuBjgxl9ElQuYZ0BCcuD9AhIN2LhucIXDF0ryb3hKwdyAV_kxQty3ezq3eHx-y1Luoe86PGwZ9wQNEH-lujLfP-PY8xS59ZPLdnvbl9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e44ec578b.mp4?token=LtxX-xfjnmhHNyrvHcQhubmsL9WsTjy_Zk_H2JsELfB9xRv0R1v3Yxlbcui2ak5ifkXECRwmNhN133C93zlbX1T7nMv7t119G_QX_J0yDcQRcb7pkzYh-Zvd5GH6KcE3IeMRyLaA70yqxQT_GYjJEOdpuVKkEpvGi2ETVkAJYmiBd64km3Q9NbhjwZaSqFF1a-r_r8xami7AXt1VuSG0x9r2UFkybJOPlhxCDu3OYvANTbVuBjgxl9ElQuYZ0BCcuD9AhIN2LhucIXDF0ryb3hKwdyAV_kxQty3ezq3eHx-y1Luoe86PGwZ9wQNEH-lujLfP-PY8xS59ZPLdnvbl9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد متخاصم با آتش پدافندی نداجا در بندرعباس
روابط عمومی ارتش:
🔹
بامداد امروز، یک فروند پهپاد متخاصم دشمن متجاوز آمریکایی، با رهگیری و شلیک موفق سامانه های پدافندی دلیرمردان نیروی دریایی ارتش، تحت شبکه یکپارچه پدافند هوایی کشور در بندرعباس، مورد اصابت قرار گرفت و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/671017" target="_blank">📅 17:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671016">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8ddd9019.mp4?token=VepxiCCcaNMefKjZfJXME8r3tbfKu1ed2W9j4Vht2IDm9_Egn_RiWV6Y6TK4EDHAD4NMp6ASgjwi4egkY0iwxph7_hbYYsqvtbGW31TnfosxwjfWq6qmC29wFDIYpzbWu6X-Krv4s8kv3R92tD9Y_0xDHWob9KNDeRIXnXziTdm2QHlIqgkgrYiOBDojq0FoWRibLnbUqyCcWtWcND2Kuf23QhHWlGT4KBZQBHwjT0wV0MKOrlbYnZYrznRTibYg87AR7RXscWGisb6OQ5jlF7RT_V0kaVLRpKKK_eyUbSuVggrEmZbVJI999Tn_26VLnbyCJWk4qxPl2uAeoj5hTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8ddd9019.mp4?token=VepxiCCcaNMefKjZfJXME8r3tbfKu1ed2W9j4Vht2IDm9_Egn_RiWV6Y6TK4EDHAD4NMp6ASgjwi4egkY0iwxph7_hbYYsqvtbGW31TnfosxwjfWq6qmC29wFDIYpzbWu6X-Krv4s8kv3R92tD9Y_0xDHWob9KNDeRIXnXziTdm2QHlIqgkgrYiOBDojq0FoWRibLnbUqyCcWtWcND2Kuf23QhHWlGT4KBZQBHwjT0wV0MKOrlbYnZYrznRTibYg87AR7RXscWGisb6OQ5jlF7RT_V0kaVLRpKKK_eyUbSuVggrEmZbVJI999Tn_26VLnbyCJWk4qxPl2uAeoj5hTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، تحلیلگر حوزۀ مقاومت: استراتژی چشم در برابر چشم دشمن را متوقف نخواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671016" target="_blank">📅 17:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671015">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c90c845ea.mp4?token=eCU_JYlDp8IFPBRC8gqssNg0Sd3j-qXXWl0UG6bidrYnlja2nZTAiW82Qfd2pdKKwfW-Qtxu-E_k8lipLkszzSA6OPjBvUjeUhaTwczmutvZx7C5RMvwsjcCNd26Ga8Sq68iowpTnUKjpL9v470mjYLk9jSnespc3XJcaMRdZqesuuZv-xarhwaj6PUlBkiCAUW9IULgB1Tvh0tDnw163RwM3Bu3LSCjgyiKi4NDDX0NRiMrLZPrtL6sQ1Dnf4USo315dLKVs5pvBsVTEPIskAUh5Z2EijT0cNCddGgOBZk1aAI-xkzTMsvAlE0EXh1gI1Gd_qPgPLnZzT-yc8L6wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c90c845ea.mp4?token=eCU_JYlDp8IFPBRC8gqssNg0Sd3j-qXXWl0UG6bidrYnlja2nZTAiW82Qfd2pdKKwfW-Qtxu-E_k8lipLkszzSA6OPjBvUjeUhaTwczmutvZx7C5RMvwsjcCNd26Ga8Sq68iowpTnUKjpL9v470mjYLk9jSnespc3XJcaMRdZqesuuZv-xarhwaj6PUlBkiCAUW9IULgB1Tvh0tDnw163RwM3Bu3LSCjgyiKi4NDDX0NRiMrLZPrtL6sQ1Dnf4USo315dLKVs5pvBsVTEPIskAUh5Z2EijT0cNCddGgOBZk1aAI-xkzTMsvAlE0EXh1gI1Gd_qPgPLnZzT-yc8L6wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسگر موجود در توپ جام جهانی ۲٠۲۶ چطور کار می‌کند؟
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671015" target="_blank">📅 17:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671014">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJIHQ6-yJdExoCDx4fq9_7DY3UgHvp04mYZnAJK75ZyhdNvigCeMKkyrhP2cSXRy_2zAEtkVT2AupIDsrEHe-W7V1HNOY3ZP7DZdHdrCl9gl99VGc10fH2OGsLP-6m_qh6fv-vo_Lb7I3BZOqjW7-v4AkUXQnvknhkns4JqyTwTJylmxjvOeX1oqeRcH_dguvkMqmpw5HW6erye99GsB3G9DItD5l-fNQrsLUAPRDQAJw1-icaxgUExoRgLbhqDbDv2z3GJckvb7DpYSsOSF9wiheQxckfvEVhaF4-IYUb7Yrxc7_is0ud7HH7YMwM3ONymIYpozSpnDepCttryuCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز پروژه تولید محتوای انگلیسی و عربی درباره ایران با امضای تفاهم‌نامه همکاری تلویزیون اینترنتی مدار و مؤسسه افق نو
🔹
تفاهم‌نامه همکاری فرهنگی و رسانه ای تلویزیون اینترنتی مدار و مؤسسه فرهنگی-هنری افق نو، امروز سه‌شنبه ۲۳ تیرماه برای آغاز پروژه تولید محتوای انگلیسی و عربی درباره ایران به امضا رسید. این تفاهم نامه برای ارائه تصویر بدون سانسور و واقعی از رویدادها، ظرفیت‌ها و نقش ایران در فضای بین‌المللی منعقد شده و در این همکاری چهره‌های فرهنگی اجتماعی اروپایی و آمریکایی در فرایند تولید محتوا مشارکت خواهند داشت.
مدار را اینجا دنبال کنید
👇
www.aparat.com/MADAAR_TV
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/671014" target="_blank">📅 17:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671013">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbYP5LBcb6kKkEonOM44GRX1If-QVhq-byR9RiLdyRZG7xxsiHiMLQMteWaUOYEY3wE37dMZF1z-EvPD2vD6iWscAslT2agqQxvA4bPwduzwGVdX-n7IsbwlFtXmxdWDpxFa8EsuS422FychrNrN0aXG1jhHWrH7anM7Qw6dTajbq57auHYVLIaB0R9W_EWTXhcTVSKrTdOaV3FDej6RpMvgQBekuBeAvRkrXK697PMzGsECxb3eDSh1LDpbvsXXeix5G0GS88DneZh04yS8BeZ9NxxzgvcXF8_A9GthaEGM7zlf1-kIQr5hfc_zkvLQRXY34TDX7aR7xLMiLwNHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خونخواهی رهبر شهید انقلاب یک مطالبه ملی است، نه شعاری مقطعی. انتظار می‌رود قوه قضاییه و همه دستگاه‌های مسئول، پیگیری حقوقی و قضایی جنایات آمریکا و رژیم صهیونیستی را با جدیت تا تحقق عدالت دنبال کنند.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/671013" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671012">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دادستان تهران: احکام پرونده‌های جنگ‌های تحمیلی و اغتشاشات دی ماه صادر شد
.
🔹
کاپوتاژ خودرو به کشور عراق از ۲۵ تیرماه ممنوع است.
🔹
فراجا: برای برگزاری مراسم سفر اربعین آمادگی صد در صدی داریم.
🔹
دادگاه عالی جنایی استانبول حکم جلب نتانیاهو را صادر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/671012" target="_blank">📅 17:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671011">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02bf47cb4.mp4?token=Nw5E2aQk4mhpfAPiQicdNgiPDQrgnSs4dc6ahYgKRJ9aL8nRT4F_waAx7ATf46-xzwp4Tf8qCNYmB6pgRvukueWORVJC9M_YQdR5p3pHs_Gy06N7YbwWk_-BvZOl15fN_Z15pYjn-X8HvmMmiDdbBZEg-zC5ad3CLE3uuyJ9kg_uxQ4wpSE334np4H44em7uU5r3EXobqR_MmYiuzHU48-jPmBVqkDj9nifucktoy8KuwwgqzKOop8AN2JSHaYXo47DGg25O2bppj8Sby64eBNufe3kGNDGaJVmJ3Qu_gptg-jl7sGsnXbNC-oV90K0IealLlVsgwgmsPGYAyhjDRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02bf47cb4.mp4?token=Nw5E2aQk4mhpfAPiQicdNgiPDQrgnSs4dc6ahYgKRJ9aL8nRT4F_waAx7ATf46-xzwp4Tf8qCNYmB6pgRvukueWORVJC9M_YQdR5p3pHs_Gy06N7YbwWk_-BvZOl15fN_Z15pYjn-X8HvmMmiDdbBZEg-zC5ad3CLE3uuyJ9kg_uxQ4wpSE334np4H44em7uU5r3EXobqR_MmYiuzHU48-jPmBVqkDj9nifucktoy8KuwwgqzKOop8AN2JSHaYXo47DGg25O2bppj8Sby64eBNufe3kGNDGaJVmJ3Qu_gptg-jl7sGsnXbNC-oV90K0IealLlVsgwgmsPGYAyhjDRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سه فرزند رهبر شهید انقلاب در مراسم بزرگداشت ایشان در مصلای تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/671011" target="_blank">📅 17:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671010">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07330a77b.mp4?token=ji2LM2vYzL89wAAWmI517WKWQtdsWaG7SeCLhAL7SfQi_O-KDC1Oe617WytcyEz8TWEjUuAxgyZv2jAYYVN9HcyQaR9HA3Z-pxqIw2rJGI8euwGhoQ_5xMzRxg8suhJASw8W2K3UwJHeKrS6VYsqUNDZcrZkZJyu3sUljiyGN6tQxWrXHDx0yR6HLw38noOJghSmCK3iD_ERt9gxIVRKyEwgb7xNYbVchpGjod9-uxq5fKeEL3MYZ76I54ZxmaK6HfEuL07KOYc_whVCukAM5we0XWt4xIBeaKmSZV_o_81kpMhvlsKlU61qfdn9tycZCnjo5RDo4ekBid-SvTzY_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07330a77b.mp4?token=ji2LM2vYzL89wAAWmI517WKWQtdsWaG7SeCLhAL7SfQi_O-KDC1Oe617WytcyEz8TWEjUuAxgyZv2jAYYVN9HcyQaR9HA3Z-pxqIw2rJGI8euwGhoQ_5xMzRxg8suhJASw8W2K3UwJHeKrS6VYsqUNDZcrZkZJyu3sUljiyGN6tQxWrXHDx0yR6HLw38noOJghSmCK3iD_ERt9gxIVRKyEwgb7xNYbVchpGjod9-uxq5fKeEL3MYZ76I54ZxmaK6HfEuL07KOYc_whVCukAM5we0XWt4xIBeaKmSZV_o_81kpMhvlsKlU61qfdn9tycZCnjo5RDo4ekBid-SvTzY_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل ویرانگر در روسیه؛ ۵۰۰ خانه زیر آب رفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/671010" target="_blank">📅 17:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671008">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
هشدار یمن به شرکت‌های هواپیمایی بین‌المللی
🔹
رسانه جنگی یمن، نسبت به عبور هواپیماهای بین‌المللی از حریم هوایی عربستان سعودی هشدار دادند.
🔹
تمامی شرکت‌های هواپیمایی از عبور پروازهای خود از آسمان عربستان خودداری کنند.
🔹
این هشدار تا زمان رفع محاصره فرودگاه بین‌المللی صنعا پابرجا خواهد بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/671008" target="_blank">📅 17:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671007">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re9sJ8pF9hRKnFIqWdn1mwtKNACktU_v_bhrvLLTKYAYd_xxIwGNX4yo3v6yDDYJ_n2HM77eHKiliKxqsF7ppwGefkom7qouc_cR5jMgdYzopUGYmUyVCL5nEBe30wnEUfKvj5x2YszgLVk46j-Tb0I0tBDU68YiKDJbYbsRRebBPIl96-CNmd3NJXMQgFf8wnyNym6PkxVK7nuuGuf1THO5BlopcwUHIXuz-SIgoMfhDu8706AhVGf96J-4_2SlVU1PvJ6C9lVAPWVEVr3FF7QvjB61aRQacG6U8K0UEyriUc33iFhkCJUg4nkHbntaBNL2WJtkkDi6ssFOWPOKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | قطعی برق خارج از زمان مقرر
🔹
اگر در محل زندگی یا محل کار شما برق خارج از جدول و زمان‌بندی اعلام‌شده قطع شده است، تجربه خود را برای ما ارسال کنید.
🔹
برای پیگیری این موضوع، لطفاً اطلاعات زیر را برای الو بنویسید:
• نام استان و شهر
• محله یا خیابان
• تاریخ و ساعت قطعی برق
• مدت زمان قطعی
• اگر از زمان اعلام‌شده متفاوت بوده، ساعت مقرر را نیز ذکر کنید.
🔸
گزارش‌های شما پس از بررسی، مبنای پیگیری و انعکاس این موضوع از سوی خبرفوری خواهد بود.
🔸
اطلاعات خود را از طریق شناسه زیر برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/671007" target="_blank">📅 17:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671006">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
تجاوز مجدد رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری گزارش دادند توپخانه ارتش رژیم صهیونیستی اطراف شهرک شبعا در جنوب لبنان را هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/671006" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671005">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
پاسخ یمن به حمله به فرودگاه صنعا؛ فرودگاه «ابها» عربستان هدف قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/671005" target="_blank">📅 16:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671003">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AephBRiwDLP2RI8QxMHQm6NnWL-z1I0I7ik25OnIQy0LAI8wUARZnUy0_aT84qNbgXfibI71WD8W68CFSD7Zs3EupjXjvaYJonFKkycTw8fh12dzNR3jeaLybZxFx4YIELh4Ps9kL5-T-8pTV-geq1xaJRj2u5E_W-Pf4ORDK8kl3ZCnxcqYlw7DRmInzr4NAsWREl3GAj6H3sqQN57x1wzFVtk9iCvGVVYJ89kLujpBBJEQN5gN7wSvnph8xOPM0nJW3OUozi7SoggOHVJN_nlx9hbAcDnOwTF143SkBt79tZjEsJWKFo9zVm2FTK2jup7ofimGD0mI4vcRbzuiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امید به زندگی ایرانیان در ۵۰ سال اخیر چه تغییری داشته است؟
🔹
امید به زندگی در ایران از ۴۳.۳ سال در ۱۳۳۹ به ۷۷.۹ سال در ۱۴۰۳ رسیده؛ یعنی طی بسش از ۶ دهه حدود ۳۴.۶ سال افزایش داشته است.
🔹
این شاخص میانگین سال‌هایی را نشان می‌دهد که انتظار می‌رود یک نوزاد، با فرض تداوم شرایط فعلی سلامت و مرگ‌ومیر، زندگی کند.
🔹
توسعه خدمات بهداشتی، واکسیناسیون و بهبود مراقبت‌های پزشکی از مهم‌ترین عوامل افزایش امید به زندگی در ایران بوده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/671003" target="_blank">📅 16:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671002">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM_GVZ2T2JCaUnb4TGnzVoF3ECLh7RiWvOvRqtlSYjfsrpwH5WNc20CnNeYvHuJIa_UcFISiLHJpt7N7zu7S8YEeh3t8Kh2V2j7V-uL7Y-RhM6TeerxLhDjfdjrRaWEQQ7zLJJYV1euspkvEMqFK92-xhSWX4T5WxeRyH4wi5CCwj_xs729wWfD29AaTM15u0NA_bawjSrnF8v4hM3XTDcCJpdnI3DyOljPR0QtDaRntMm40dT_ladV0HEjm4ljekJFJ6xCKVnOmNFjdtdUN7ZZZgyVQNprJA48eeFGOh5bbjk_tkfT4OIBZoySys08e3SfSjrBRsgJVPP7lhtDmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلعه بابک، آذربایجان شرقی
🇮🇷
#ایران_زیبا
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/671002" target="_blank">📅 16:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671001">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzjlEJj2SbFqVuokdqOkTKFZ2_UIuX_4zcYsfVv2fEjDuXw1Z6kFiZ8FFQIpKhO3mxUqPoDgztorOLfXxwgaEtKn9YH7LDpQhY1fMzAH8pJ4xzDt9Kjz28S2r97T0wRgUQvqyhd0g6inh9Lu66UHu6PAfAyG7QNOeRry3AvXbAgjx_HAKzOTFPuVqDneIEseijTzw7O3Gxynlq-uBkB3a4m8vp-i1_I7c4eO_1VA7DVOtnvJg2hMurq3Lqdw1w9HMBagE5ULELryZh9hteEJtCFp3KB_1bFPvpB1t480Hzg_ij9rFLFG5q3qpRBQw7ekcOqj2yrJWnC_fqEKupzlXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا در صندوق طلای «رز ترنج» سرمایه‌گذاری کنیم؟
🟢
خرید با حداقل ۱۰۰ هزار تومان
🟢
سرمایه‌گذاری امن در طلا با پشتوانه طلای فیزیکی
🟢
بدون پرداخت اجرت ساخت و مالیات
🟢
بدون دغدغه نگهداری، سرقت و تشخیص اصالت طلا
🟢
خرید و فروش آنلاین از تمام کارگزاری‌ها با جستجوی نماد «رز ترنج»
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/671001" target="_blank">📅 16:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670996">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIAk2n1vxixcxLDKhujqQajA7tRN58dtAABrXMolcNiULzzT80T-UgN0vXLZNADxZYUUJj75JiTSwKcWVqn15xAIMnuqBM1LXVeJQZIoZnfV4knnHtWQEO_Bg7umplf0Y-EVWxSRJyKOspfTCWzz1i6NU1egSgJpIn9JM7v9ib7NKKVhA7rqw7T3AGd3RkfhMsV88F8kd8VfRriRQfC3U2MO7vIZ4t9lTT1pf8JjWLjmxtnDflPsy86I6zs-_K5tSE6PZre7d7ZnbJVuDewa8CeQBikOXlQ_FnOU0RCWBab02PQpxbOzWYNfFtOOluNI1x5xX1gFCX0-q5Ox2wmxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوه کلنگ که ترامپ تهدید به حمله به آن کرد، کجاست؟ / تاسیسات مرموز ایران در قلب زاگرس
🔹
رئیس جمهور آمریکا در صحبت های اخیر خود به حمله به کوه کلنگ اشاره کرده است. اما این کوه کجاست و اهمیت آن در چیست؟
دراین‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3230219</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/670996" target="_blank">📅 16:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiM_sIKuXubF0UGOIuzDqdHsDxvfrI51UxyNT7JeZKNi1RftUf7Lg9V0QmbUgM9Pj1dqNEuMcTch6dg3UYiR4XfeOvHsnLjW55Z_G5bzFJKHPh5dV3vbMBVwMbeulnjsbtvPn1A26OeMvysk4-cQdWt25s6fsBwOvgHycSlSqFieutiUffgmSIZ_l9ciR8AfBN24ePumUA-NSmli37il8mZialnn_DUFAtXn2GovhAvnXVEBMLBFFMmfVA17QTrt8HpBejrMHruwp_kvytu8Ke7s8AmJYWWeC6iA-4aSm_rBUu0iShPjGFcEcVXwKQrl0ixG5vYdkEj0nUJrVPFlbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRCJPi1WtAt_G4VauOROIZM7X8xdR2hAzRnhTxA-ZSziNyLPsQwoAmmlwAlzdyUawpKClsdygVFJWBP7-sLV4aJ-GH4VKV82HEy4LoIP7qvEwEewO4oRAB2qwfdwvJcjY_a3qAdd1GylIWhLeZUSoXfukTvqMTZCx0UNG6P22XBjn5J1TS5xccnY-m7uG6iyZhDzRX_U4YdOy6RkwJD1_wo26HWEy0WrgYy51SXHObB4hMk19G2qg2N1EfsS8MZgWZ-Y0eo5VJBKV-TgIN029x6AaweWAjEwkwA9UYoRrbxjeg5vwq_C_KMj98MwQ7Xph_yg50NvJv9bo3pvyoSUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ks3Qv8IjX7BOikmBY2mJ4cD2dWBYevzW1zqRThTAPgfQWSHhI4ETOmAXS_pwxU-Bf7jJIj_BGQRgYyEC2hiA-3QB6x9skLHeBVsENGD67GrtYfQfwAenUu9tmZCEYuxedDqnpki7Ffl0jOqt7EfAAn9JYNJeva9n4Bi2ON7blPREkaHREIGHJeVHCruMBfLbaBcbce0uVoG_Xxo3dBXSH5z8saoQyquEWXBZXHPnXI1wJKY8-7Xa9590TAhXwxg5dnnapBVZq1hStPEhseNIoD_tiNqxwk51abTGqR7h8U4R1poYKfkqDIvf5n3p71naKx2ij10g8ghH9Fl0iLPfvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwApLXuYZDSgWTQq1Q51w3yV5quvhdiB0pUAiS8OfNK1aKMgk7fZiejzsyiWFOICwwHC8ep1oQU9abOknszoN45d3qTnm85o600hUYM0aU73EJzF3lARmM9nOgEIAYMMpQtpVNEsxSGmmS21TeJ6qe-jgKqplWarl7mmd-qOEYSi-5-lXwrc4RigKLnsP7nISXXKdAlQgZSHzBLqicnGsNP68MiyP1ulBBF8N0qOhUlcviYlS-qy2dP2Bli3PJ9b4I-5QdPXMWqqqQo7yGV7YNLUn4u7-N11nhRJ3VxIfrmADiiw9z62QRnlB6ArUht5b1t9psFOsrN9aXMcGIOX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHmHMXXyQ5AYr6v060CeoF24-gpNh-3vVVNnSV6XyOA59d9609DfOdx5tFZxdGsCgOdH0zOJd_kYzbyqFb8Me8_QkaAAuEkAMIJd3txpoN1M8BWys6bPSCJjFGNCrL96yUMlOiNYqzyKr9ZGZQr0-CVbCIdDR4pv-lduyF1javcVvuAVW15vPWmzp04DDIp47Fd0hRXTiBrVSixw4PvrCVgBPQLUU9u0ttG-WFOQCO5QkJIxtA8h-jWqprTT7vX21UcJmkujPuE25D65m38p-ZU4cMOt9mh_0xsxbKfCNCwgkV5pKZOTnxgz0_Wl5YANf5QkbwWjbtDY1RG0xlhrrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند اصل کلیدی پس‌انداز رو یاد بگیر تا پولت رو‌ هوشمندانه  ذخیره کنی
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/670991" target="_blank">📅 16:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670988">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_kkVK15tWZuSin8vWYd2VLUz6ZpSXNHD1m2lwvQ0h1dBWuihOSwUZwhMEvzB4Iu8-f7R_a-6KmfS4bf803S88eif9IFUgbeBG3-eK6T8Pk5uW17QtGrv2GjrCvYAMNFkHodBinhXtjqVhtGHvFcGolYdO-MleosuPdUw2C_nrJDLCRqejuz0u5v5918tQBsFENyz8HVmpDUkhuA7g8B10eR_iQ1pnXV-SLlKAre2aVfKyNHYgANIMG8L8T-6Xr0nsSdGBnFPquL9D8reSennG7eLRZtjPSHUSMbW0vfqpAxdjxpR_IoVP6WQzTxaoS32CBU_-pCHuOd_YUPljbSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
آخرین وضعیت ارائه خدمات بانک ملی ایران؛ از واریز سود سپرده‌ها تا وصول چک
🔹
با ادامه روند بازگشت خدمات بانک ملی ایران، بخش عمده‌ای از خدمات بانکی از جمله واریز سود سپرده، خدمات چک، پرداخت اقساط تسهیلات، انتقال وجه، خدمات کارت و مدیریت پرداخت‌ها به پایداری رسیده است. متخصصان بانک نیز همزمان در حال تثبیت پایداری سامانه‌ها و تکمیل بازگشت سایر خدمات هستند.
🔗
مشروح خبر...
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/670988" target="_blank">📅 16:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670987">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
چهار نقطه شهر بوشهر مورد اصابت پرتابه دشمن قرار گرفت  استانداری بوشهر:
🔹
در ادامه نقض آتش بس و تفاهم از سوی دشمن امریکایی ظهر امروز چهار نقطه شهر بوشهر مورد اصابت پرتابه های دشمن قرار گرفت./ ایرنا  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/670987" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670984">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
داریوش فرضیایی به سوگ مادر نشست
🔹
«داریوش فرضیایی» مجری و برنامه‌ساز شناخته‌شده تلویزیون که سال‌ها با نام «عمو پورنگ» در میان مخاطبان شناخته می‌شود، در غم از دست دادن مادر خود عزادار شد./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/670984" target="_blank">📅 15:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670983">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJSoSgTcWXnExsh8iDi6PkSoqqh1o44AYyZuN0FKkB94H6iFSFitTcfXkY_axrXnZVupWWRuXKekeGCm7OV6yrJw8CLWaD7zQKiPGlMEboMUnPx3iyGk242Shk9LwCGr4RxDDMGjEuarLRs52IdEe601bp-Md3VVnl_9qGkX-iz7YrOwk43F0D1mG-IX0Bp63PUid0eMNeZOGvBnmTXe6HG38HZPL6uFXRkgePPX5A6chLWrBXQ8Mm0dyXqM5HA4RXestSucWNize2qXhGqM9uqeJvyAEYX8JCHBJxnhB1R5lER7vxLfmuNc1k7_BqOrUvxnrqwRSUYzlqYD35385A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمپین بزرگ اسنپ‌مارکت با جایزه ۵ میلیاردی
🔹
اسنپ‌مارکت کمپین تابستانی خود را با جایزه نقدی ۵ میلیارد تومان برای یک نفر آغاز کرده و به ازای هر خرید، یک شانس در قرعه‌کشی نهایی به کاربران می‌دهد.
🔹
این کمپین با هدف قدردانی از همراهی کاربران طراحی شده تا خریدهای روزمره را به تجربه‌ای هیجان‌انگیزتر تبدیل کند؛ یعنی هرچه خرید بیشتر، شانس برنده شدن هم بیشتر.
🔹
به گفته اسنپ‌مارکت، فرآیند انتخاب برنده نهایی با رعایت ضوابط و در چارچوبی شفاف، طی مراسمی با پوشش سراسری برگزار و نتیجه آن به‌صورت رسمی اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/670983" target="_blank">📅 15:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670980">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
آزادی ۵۵ صیاد ایرانی از بازداشتگاه‌های امارات
سفارت ایران در ابوظبی:
🔹
۵۵ صیاد اهل سیستان و بلوچستان و هرمزگان که به دلیل اختلال در سامانه‌های ردیابی توسط گارد ساحلی امارات بازداشت شده بودند، پس از حدود دو ماه آزاد شدند و در حال بازگشت به کشور هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/670980" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670977">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzzYJMjm-6jKFEK6xThVQvjKvZ2jmzVMVZ9TAzXnBMFyH83CnMa7Oy8kqd16OyqDL7TITxUTOukplI3e0lh4i7TBCpYNamB_nw5vWULdYx-4oQbZXxV_XPQFAfeWC4eWQBqej6-paOfFXPeqwtRcs522pPZKl7Gfh5hJ-OD3ekStIvW1zAbsLYsFf1B3Y1nY_cLg7uaYZC1oW3WityME9snLzFoE9oDF_jf19svwAcRkLcmdd1En7BdLwIkeVKWU7d1hGOGOBaVTNW4iDwynqf-lSh_UpcyUnpMLQGz_cNIcyPpzs0nX-5ljontyFFgSxHcpS9GjGBSmN6QxTgSprw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7oaha0Sk3G6zvbMvo04LIQ2rJnbeqI1WLzCFvw_SyMXyMqBJP4qUj4lPn_fYTZ7zr9QdPHROnf_syv-GCCwHgXWd_oEG8jmeRxcvnBACkzCHjrdYX63HnW57WPE7jACN5ngZp_lugTwk5CB-YKoIsvp4Bf-30k9ba_fCxva_KWSzslw6WSjMkSXUX2lOWc_pbUMaf_lIkG-gBNAb49F2k9wvYhrNXoFNmierKMTwCID0kcuagdCGmuLTN9zHT8Xy_9sczeoHBDBjwb5l4NpxRt6C3NYCQOAOLbX6dwVAjIRN0m42IISgLQynNNjxSDtgd65-F_n3gcS4een5Rnghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iytoFO1O7vWk4i3j74K9ExrIQCIz8cydNVyrnNHaV7X_KJsF5ubEz-gTytIRLXsyOjZjt6Kl9XMTbSwuljFWu5AbkVTwmukr78tdY7A2qNoF8kbDkiTvr-8JRfb9dATMDSNNvJEEZg2v-HJsotk_uTtfSnQEn2Gxw-4PjDUdL_tdcFsT_E3SBVPIrP2qS80HOu_rj0nwO0jD6RTV4g5hGO8_pNWV3GKe54_qg6i9VcpNM4pyNud0mQIXMGBMzRLvDzIc8kM5X4t49T5J9esvIeRIudK-WCB4AXUcfZLSAp0HjXUnDsPDGCVfN3vuAkvid7bvxNymc_zVLyJhFFWl7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ظهور نقص فنی در نمایشگر گلکسی S26 اولترا
🔹
سامسونگ در پی گزارش‌های کاربران مبنی بر مشاهده هاله قرمز در مرکز نمایشگر گلکسی S26 اولترا، تحقیقات گسترده‌ای را آغاز کرده است.
🔹
کارشناسان احتمال می‌دهند این مشکل ناشی از نقص سخت‌افزاری در فناوری جدید «نمایشگر حریم خصوصی» باشد که با تنظیمات نرم‌افزاری قابل رفع نیست و می‌تواند منجر به تعویض قطعات شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/670977" target="_blank">📅 15:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670975">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
افسر ارتش صدام: روزی نبود که خبر ترور کسی را در خانه‎اش نشنویم؛ ایران بعد از جنگ هیچ‌کدام از فرماندهان و خلبانان بعثی زمان جنگ را رها نکرد و همه را حذف کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/670975" target="_blank">📅 15:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZF1WbLeTI1OR2QfhiX9uU-_jaDgOkXJAN4-vijbjjsqJ__pucTujDpXACCx-iLOXfVCCLd9ZVgMEao-0DZ_v-eyszk0o6jE7g9NSVVl3V7Ixj66c5JKAB4eEFL3CUk1h75gIszVbRjpPfvsG_dQkzZebKyNRjntpZxUl0mghizGBOq8KleHsKTR_VP6JeS-2QlEexZbXHOouT4u_cFbb3VjQPBe5rznhpwxmXOJ6m6U4VKfN4oMk0M1Yf5KPwrHAh1W9BAZGXDPgDMuJ-xbKHUk0XDZ0wJPF454nqyt7kRvfzZXL2-ACqIcfWk7IqCR9NFs6EfHa0cVAiN8qP9lcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احمدی‌نژاد با دوستان و همکارانش دیدار کرد
🔹
این اقدام پس‌از شایعه نیویورک‌تایمز مبنی بر حصر خانگی محمود احمدی‌نژاد صورت گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/670972" target="_blank">📅 15:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670969">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
روایت سرلشکر صفوی از بینش رهبر شهید انقلاب به مسائل منطقه‌ای و نظامی
سرلشکر پاسدار رحیم صفوی:
🔹
در سال ۷۶، ما ۲هزار موشک داشتیم، حضرت آقا در آن زمان فرمودند ۲هزار موشک کم است و باید به چند ۱۰ هزار موشک برای چندین ماه جنگ برسد.
🔹
۱۵ سال قبل حضرت آقا به بستن تنگه هرمز به عنوان یک ابزار نگاه می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/670969" target="_blank">📅 14:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670967">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1XUmTm5ak3YVpWAXl6gQHqk7S-bjMBlpGZfqnxQ1ORgw-nBhEHRw9cPpFuwXdJdrRxVv_H96KkAA3RaYmA0CmTzdFG20-oQs99VwnzSURR8LG9Af3XTV4csFEPhM6SYmC-3md0Z52FZ-yCcnSRYkONgZECVorY3XZVhNnmOAiUIoUGssSBCr6Y7Ntqfi5Cg_f3TOo7ewloCbqgf0bou7aAGPbtXcH6I-8vNKodjSjj5OCK1GMZJzVNyUMUv1FrqayvK9LZs4Vgk1Lnve-UPS8kUMZBCq8sMhQVgjXB936evll06zqqYFEZRfD7bzzmfq5zwB1aPzxgBbrhxjVRyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار بیمه‌ای؛ چالش بزرگ تأمین اجتماعی
🔸
برآوردها نشان می‌دهد سالانه حدود ۴۳۰ هزار میلیارد تومان فرار بیمه‌ای در کشور رخ می‌دهد.
🔸
بازگشت بخشی از منابع ناشی از فرار بیمه‌ای می‌تواند به تقویت منابع سازمان تأمین اجتماعی و بهبود مستمری بازنشستگان کمک کند.
@amarfact</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/670967" target="_blank">📅 14:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670964">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
اصابت چند پرتابه دشمن به غرب بندرعباس تأیید شد
🔹
استانداری هرمزگان برخورد این پرتابه‌ها را در حدود ساعت ۱۳ امروز تایید و اعلام کرد که اخبار تکمیلی در این خصوص به زودی اطلاع‌رسانی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/670964" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670963">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c662d108c6.mp4?token=ZmggD7SCf8hZeos6MNR1etkf72_gc6GMQ631WsfZFPbE6paQNPwVl_oPOj_VEB1Yg9LKgwoAN7JlVAkHe0JLqAFY9Y1Se0EgZsUIYKhvCploCgf_kk9rihOIy2uP9D6x5ieOHCSdE73oizCfaUeZktSQ5l_O2_rVMR881ncTH5_FpAqPxZie4KPMYxdBEcye3gDdopaaOTsETrvP7fs-HjzOh4xsrHibkAZKIsFdyjv3uB-v3dm3x6Lg9TJmjScocnuAjSsNeds308gHyQAhVfXZ3Bg9avPU173i2LEzqeQzSf4FdInZE_0UMBhooOs_z_fWjWOTzsXz0ZK_KZcQ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c662d108c6.mp4?token=ZmggD7SCf8hZeos6MNR1etkf72_gc6GMQ631WsfZFPbE6paQNPwVl_oPOj_VEB1Yg9LKgwoAN7JlVAkHe0JLqAFY9Y1Se0EgZsUIYKhvCploCgf_kk9rihOIy2uP9D6x5ieOHCSdE73oizCfaUeZktSQ5l_O2_rVMR881ncTH5_FpAqPxZie4KPMYxdBEcye3gDdopaaOTsETrvP7fs-HjzOh4xsrHibkAZKIsFdyjv3uB-v3dm3x6Lg9TJmjScocnuAjSsNeds308gHyQAhVfXZ3Bg9avPU173i2LEzqeQzSf4FdInZE_0UMBhooOs_z_fWjWOTzsXz0ZK_KZcQ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدئوی قتل مهاجر کلمبیایی به دست مأموران اداره مهاجرت آمریکا
🔹
تصاویر دوربین مداربسته، لحظات منتهی به تیراندازی مرگبار مأموران اداره مهاجرت و گمرک آمریکا (ICE) به یک مرد ۲۶ ساله کلمبیایی را در شهر «بیدفورد» ایالت مین به ثبت کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/670963" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670961">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e2326267.mp4?token=vfJhOjHOaLqYIsmPXlE9XFXD3Kkzjw2kstVm37AyUdpsvczitwxeS2-7_K6Le8EeWkdAbKDVMUW05yvl0Lhw_4H_F6lMLSGXhUkNNMzh3nUpNHPUedllukrW-j49--KdwyrJZtUMNEEJaptAmqJFVanbp9I5jr_kF6t5mg_nL-zZjBfLW2shF4oKxp4mFYSx5awdd7psshrkTO-bao3EIZhGZE7J1ge8jkzvUdPEi3mDw0IeTtj5qJYZd8kTntnhcnKOQ2zk00xfXpr9jQU7oyMbbOXeqB-qubGIKg8u8iKHRhHC6Ii696CTfx7xGowv5Kz9q67Y1pCMIJtvty9xzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e2326267.mp4?token=vfJhOjHOaLqYIsmPXlE9XFXD3Kkzjw2kstVm37AyUdpsvczitwxeS2-7_K6Le8EeWkdAbKDVMUW05yvl0Lhw_4H_F6lMLSGXhUkNNMzh3nUpNHPUedllukrW-j49--KdwyrJZtUMNEEJaptAmqJFVanbp9I5jr_kF6t5mg_nL-zZjBfLW2shF4oKxp4mFYSx5awdd7psshrkTO-bao3EIZhGZE7J1ge8jkzvUdPEi3mDw0IeTtj5qJYZd8kTntnhcnKOQ2zk00xfXpr9jQU7oyMbbOXeqB-qubGIKg8u8iKHRhHC6Ii696CTfx7xGowv5Kz9q67Y1pCMIJtvty9xzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصویر از آمبولانسی که در حمله به لار مورد اصابت قرار گرفت
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/670961" target="_blank">📅 14:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670959">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_9GFSslilqQnLBTu1sUrBzVa17VvTlGlypYEhttqR-_i_JH9pc2y1fiI8lCQdnL7rH1qr43cG5LrDD0O0oNKJDIQq34Ebnw2RItFH3gsksBDJvXLZyqnmTRVR0XOXDBX1-inqQvKhX6jjciLfEeu3r7jW_G5pRS8_xOLOf9JMRcDtLn_hjet6QE4v-qFWTDXQxPGNMq-ZF3KVdHwOp5U7KYgip6qHwD8WLr8XHl79eKiozjZBsYQ9QkyWkX_CvFIYpQejB4LQ937YORIc3XfJALVaeKC0TSQPJ0_QWHDCaWd5VvpLBtKYuchET_yWAWq8FPekMzF_lGPsNiD5Uyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۳ تیر ۱۴۰۵؛ ساعت ۱۲:۳۰
🔹
دلار امروز با ادامه روند صعودی به حدود ۱۸۳ هزار تومان رسید و نسبت به روز گذشته افزایش قیمت را ثبت کرد.
🔹
در بازار طلا و سکه هم سکه بهار آزادی با رشد روزانه، به حدود ۱۷۵ میلیون تومان صعود کرد.
🔹
روند امروز بازار ارز و طلا نشان می‌دهد که فشار افزایشی همچنان بر معاملات این دو بازار سایه انداخته است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/670959" target="_blank">📅 14:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670958">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
اصابت پرتابه به آبادان و حوالی ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔹
امروز سه‌شنبه ۲۳ تیرماه، در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔹
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/670958" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670957">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_cS6QaVO0b4lqK4EEBWUL70RQiQ7qRuF4VtEi39walfY_TlNO2QJ3aIpRRT4l7trLxFYZqNexQGbmFI9p9ojImmgBQVTepU0F0RhRRcTLO_D0pNJhUkCMFwBz85g0H8-Htyt7cNJmLdB3Zy55kFkMSyOMI3W0BLsA1Yhk-hiiDTqkPlDH1H5vOyfhURwrbSo6kJqZu4pKeC7_JT_VTCf9jnA8y-RZHnvBlZNMuazYMbLX1CS70AkKazG87E8VraU667ln9gs7fsWvwWTekDOV8PG7jFTCEgxQ0ALTXkxhLQmQUqWiKMP5nVYls4ZqLaSA2ATuapIuoZ4WM4ziLbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت همچنان صعودی است؛ ۸۷.۲۳ دلار به ازای هر بشکه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/670957" target="_blank">📅 14:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670956">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تیزر قسمت اول از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سعید اعمی که به دلیل پیدایش غده‌ای در بدن و عمل جراحی برای رفع آن، روح از جسم ایشان جدا شده و در عالم برزخ، عذاب و ثوابی که با مرور تمام امور زندگی از جمله اذیت فروشنده پیر در ۵ سالگی تا کمک به جوان در راه مانده در بزرگسالی را درک می‌کند؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سعید اعمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/670956" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
