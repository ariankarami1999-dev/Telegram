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
<img src="https://cdn4.telesco.pe/file/IneErGZv4QmiBZWoqkdC5QVDewi_CXjRNhA98r2ou6B8t6Zzo3rYfPodQlbVVtnesRz3XrJQ6X-er5cMu_nUUs_jLnq8qzitOg1BaCX14xfKcIaxbqx187YvQ-E08lFOXZ3KXqqxGg8zj1danBEYZXkSQ9Nm7igGUyY3Ne4QKIDOkkJ0gv9r59GpUwiPLrUtY-tFL0WzD3PWC7W0aRcKkx3DFTg-nOhA4Fhuy6xOBIqZArF5JE4NU-4pnLgi5sH9y4lVBWyWJuQ8u7H_1DrEUl0qB32z80IG5LVBZfuU68NYFMaeTEU0p5SBWnLLJ3ZLx1-yIjmg-17RN4qVcR9StQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 15:12:48</div>
<hr>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9A-v9wbyl0UxMfufyme9Y7dV1xIX79ALbikF1noLO03NUWlb9Qlk8IlTSaXaObeLBoFf8Mt6KnDABYPwVBomTIAaip7DuypKKQlPPsAMvy16n2rr6tQXZcko6DCvxF_U-FVS3sClxRqNNE1x37uKft1sKSsfFT-JiJmZAh3NUjkC3-Tb8S5ce9P-oVfQlYMKWvDzYuIY3YkBlPTcXWcB_8JwGMKKaZgQtoyuqz-4ZGl3C4_EZMMVWd-jyrN_RiZrQvUt9b90LPf-0OJ3RQz9lYyYW-lSF_2JzVXRQTX1_EPSjQTwOjj5ffcpAXC-dBZcTaUJ33Fulqy_ZHm-Re1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 125 · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=CxPpmPp5VR5wpLIOGaNYEHL33_14XYMlG6X-YevKUQIuxdrPsvvEXa18F6xM0Xp0RnySsDI-2CQb2ksqxp2o-ADYlmxZxF9FeJbLuLD9k3uGnlMzlaupkP2birkbJ4EDbXBRZ58Rgz2N6hplpyjTFMkN-grHvUurXjLGoO-bapXQErm8fXKkRDKbCDkiry2LqdujxdzjZ-5jJRo5tOA9KHh_8WD4J4udaoK7CmLPLbKlpvyWSRemnTeClAY1zb7kQKbkljI_Opm1w2pRMb8ctLQWTb4F-MgfUJlzSE5mAQp_20-jeAlYninKRAPIXuOd-hyNO7KP_OqH7EFYPPzBSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=CxPpmPp5VR5wpLIOGaNYEHL33_14XYMlG6X-YevKUQIuxdrPsvvEXa18F6xM0Xp0RnySsDI-2CQb2ksqxp2o-ADYlmxZxF9FeJbLuLD9k3uGnlMzlaupkP2birkbJ4EDbXBRZ58Rgz2N6hplpyjTFMkN-grHvUurXjLGoO-bapXQErm8fXKkRDKbCDkiry2LqdujxdzjZ-5jJRo5tOA9KHh_8WD4J4udaoK7CmLPLbKlpvyWSRemnTeClAY1zb7kQKbkljI_Opm1w2pRMb8ctLQWTb4F-MgfUJlzSE5mAQp_20-jeAlYninKRAPIXuOd-hyNO7KP_OqH7EFYPPzBSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxq8wiJouZdUybB-E-_oW64PQsAD9ODxyxcZQdLjL9rh1RnueRu97bK6rF-todr1iZLKCopQ2QrQDtagnHXMx4Ga_7jqfLOVw_JMLWqF15ZJhPMKYOQpSz0KQv8l6NzRx_jvKqKIHRCybBtqjQfSC86lXmX-L5D-UFJb48NGExYm2Tu03ur6DWOFyTnV7tYQf-j2cQthIg5ICeR6XNtOl4nUEFBM0bJMApryZ-IMiszpgNHyOt2-Z1vQEEsy3D54T0sIzoeKzyvL0J8lDiK2pz8rKo8EX3bZtX7hT6er2oWRJSQuLqEFE-dVAhnbCG3T34EorRSjV3nzJxK_nHGMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65311">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65311" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
#
آپدیت
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/news_hut/65311" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65310">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/news_hut/65310" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=hnfVR3DZNbnj4EYJTPUWjMZdrP6Mj8EIW4AZo5BoAk158XPnaOXbZnuzKJu2jK7ZCE-40MAZcbuawi9XcxDtHHIkh3I75quGyROX2q6Y6qRxhjwP_9HwRn4pYlBKsfHwaaNGQEuMS3jYFqL5j_spASkIs8fjFgrMjRUwMrTvjeenPpAmdAcQGmRPKFNUCmVUfXhitJ-XqkNCHyDZ-epSNZQL1ZgYXr1JwvodgETl1MnJj1ou9TDOaOUytrmxyVliw9pepiRO1S_SHwsXy8_iKvY7MmzatF2qaKdkf9SZ_1CPhBgeexGN3Wmfve8T2wPEwp-3mDMuHooD2_V2LsqEvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=hnfVR3DZNbnj4EYJTPUWjMZdrP6Mj8EIW4AZo5BoAk158XPnaOXbZnuzKJu2jK7ZCE-40MAZcbuawi9XcxDtHHIkh3I75quGyROX2q6Y6qRxhjwP_9HwRn4pYlBKsfHwaaNGQEuMS3jYFqL5j_spASkIs8fjFgrMjRUwMrTvjeenPpAmdAcQGmRPKFNUCmVUfXhitJ-XqkNCHyDZ-epSNZQL1ZgYXr1JwvodgETl1MnJj1ou9TDOaOUytrmxyVliw9pepiRO1S_SHwsXy8_iKvY7MmzatF2qaKdkf9SZ_1CPhBgeexGN3Wmfve8T2wPEwp-3mDMuHooD2_V2LsqEvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=K6NOwj2MmwidB69elEj1Zt0TUnl1ePiAeeSw3DIskRkh41f3EQVyz_A2dI3FgB3GD6tnkBGflY258l3zV59e6fgzLB5vG9FbYlEhLM1L7c98gLw0-8SZbC3FUfOzYl6i2iBz0Z0Mvir6O1d42MKp94OJbV4H1Q-IYs-vhzuZRK2h9XWOftKgk0qmxUO0aKrja3JmEV4lxKXwAMgOw7btPonVZw1zh6exh9jfUrUwvaMYmgB193OxGP_9OKOAfmGyfzwD6_LUrH8mwXekU-3y5QpNUjo0hUvWDPnc4Mm2PEXxuB2-kHKxQ7DS9Nin2u39K57GRmKSxP2OJ8AbwojpOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=K6NOwj2MmwidB69elEj1Zt0TUnl1ePiAeeSw3DIskRkh41f3EQVyz_A2dI3FgB3GD6tnkBGflY258l3zV59e6fgzLB5vG9FbYlEhLM1L7c98gLw0-8SZbC3FUfOzYl6i2iBz0Z0Mvir6O1d42MKp94OJbV4H1Q-IYs-vhzuZRK2h9XWOftKgk0qmxUO0aKrja3JmEV4lxKXwAMgOw7btPonVZw1zh6exh9jfUrUwvaMYmgB193OxGP_9OKOAfmGyfzwD6_LUrH8mwXekU-3y5QpNUjo0hUvWDPnc4Mm2PEXxuB2-kHKxQ7DS9Nin2u39K57GRmKSxP2OJ8AbwojpOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=J4HXdAOYDOUWE0-LG5seD5Wwpw8u94YnJAUFQv40SjgrNspW5wyF0HSDQTY2bSvpV4nBwRNbuz3cIgZKXcgQEy0TpYlXnMCHIBJYCv1cTeBEpdpVi4OLDukMmSVSWvHcD3oPFszS-eP9-2EJV7ReUgdcPW-KdSqZwqW8qeSo4l1TJOCuS3tI5Fr0kuv24WkrRPiBFTE4pIqqMFSIFmNwfMgkS6UNybGDgkBwLA75ZJRu3xBCd7ZwJrxMLj_FxpS0kj9OM0InlA4_AKVgUrQUpunRDLCBakbl_e9q1EpTzpiMDpznLlS6TlzU3O4GWMdWA4_BKbif6hIJRLA2MQ2Eow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=J4HXdAOYDOUWE0-LG5seD5Wwpw8u94YnJAUFQv40SjgrNspW5wyF0HSDQTY2bSvpV4nBwRNbuz3cIgZKXcgQEy0TpYlXnMCHIBJYCv1cTeBEpdpVi4OLDukMmSVSWvHcD3oPFszS-eP9-2EJV7ReUgdcPW-KdSqZwqW8qeSo4l1TJOCuS3tI5Fr0kuv24WkrRPiBFTE4pIqqMFSIFmNwfMgkS6UNybGDgkBwLA75ZJRu3xBCd7ZwJrxMLj_FxpS0kj9OM0InlA4_AKVgUrQUpunRDLCBakbl_e9q1EpTzpiMDpznLlS6TlzU3O4GWMdWA4_BKbif6hIJRLA2MQ2Eow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=Ap6140bYd5a3sFYWYPUgJ7T9p1EesHVwr8kZho0Yuvtd-MX9wfVVR6nMTsk9hgXaWF_LcBDUhH0K8wP9jd6fuGozwwnBnXY4wsAw0Wmmbrgu8KIoWVEm24fcQeOc9OT1NAcjytVvmzwBG9uEZXNQfPSASGRZmRbVu5FDo4yotifOw2UqlbnECBWUMjR45SeST0NCwIpSZd4eUK166q26i_Fr3W6YnZKk7fFg8bvKJyfs2Rws3SHDnDdKtApxzHgmBnXN2RMPFJRov6kELql7Yph_QOu6niK5t8L5WdhjyUcKcWWXXjkxp2vxa2RaPUhUfGDbaxx28SN8_FUQwVyvBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=Ap6140bYd5a3sFYWYPUgJ7T9p1EesHVwr8kZho0Yuvtd-MX9wfVVR6nMTsk9hgXaWF_LcBDUhH0K8wP9jd6fuGozwwnBnXY4wsAw0Wmmbrgu8KIoWVEm24fcQeOc9OT1NAcjytVvmzwBG9uEZXNQfPSASGRZmRbVu5FDo4yotifOw2UqlbnECBWUMjR45SeST0NCwIpSZd4eUK166q26i_Fr3W6YnZKk7fFg8bvKJyfs2Rws3SHDnDdKtApxzHgmBnXN2RMPFJRov6kELql7Yph_QOu6niK5t8L5WdhjyUcKcWWXXjkxp2vxa2RaPUhUfGDbaxx28SN8_FUQwVyvBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=H930gsDod75IUkNhCfJP02QgtkOoOmuo5_GJ-8RvsctnmoWcEQpp7yrwjSnVqGcckJ2v77DkXvLVoUQPWxseBPoaBZ_z25afQh5MmEQakepR8EWVWOjX_vy3YQyiOmQ7WmLWYrfKYMv8UjotkGJ4UmMHqO2QRKdwQhH7BYJtzgELdBybfl9q-IqKQZrILzbyTBeaviiJ3QWr1d9wJ3SgTPo9xuCArnn6w8Ut2doIw-mItC6EsEnbYQxsv0xJ52daHXgTP0E4cpd2Qa3fJPbvXUaRSQtBpXSx71LEyQJly39WcW0eCK2yHKyo6nLVJvPI2DIsUwD4iTO3ygLwt0b97Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=H930gsDod75IUkNhCfJP02QgtkOoOmuo5_GJ-8RvsctnmoWcEQpp7yrwjSnVqGcckJ2v77DkXvLVoUQPWxseBPoaBZ_z25afQh5MmEQakepR8EWVWOjX_vy3YQyiOmQ7WmLWYrfKYMv8UjotkGJ4UmMHqO2QRKdwQhH7BYJtzgELdBybfl9q-IqKQZrILzbyTBeaviiJ3QWr1d9wJ3SgTPo9xuCArnn6w8Ut2doIw-mItC6EsEnbYQxsv0xJ52daHXgTP0E4cpd2Qa3fJPbvXUaRSQtBpXSx71LEyQJly39WcW0eCK2yHKyo6nLVJvPI2DIsUwD4iTO3ygLwt0b97Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=WV0N_F45SE9PO6ElXZc4Fzmc7glKZ9QydKt8LgifxREzhBmdcDZHwmjkvny94HjB2DNJNZORpQ-BL3IopxkoIN96stJ0SsXCx9IiLpAdxkNwNRPnYh8oUGv8lRrfYyItMwmTPeVCFHiWTemlLR0dRZ_5-NH1ZkQPOmyMPTSXsXirweyRLHqxU8lhUXVTNzOVutLPIYBfgZYuCj4CAWq3ayTAvs0seR1HR2trYB-1KxTAH-Kt-nSVHEbw3BIaFms2YAoPSKKx4_GmHwZxLaS0SS57SgLkomk-2fRDxyE0mSwsMdtfXwBWUxsZ9A2P6xSnFkinXa_fglEukmEhiV06yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=WV0N_F45SE9PO6ElXZc4Fzmc7glKZ9QydKt8LgifxREzhBmdcDZHwmjkvny94HjB2DNJNZORpQ-BL3IopxkoIN96stJ0SsXCx9IiLpAdxkNwNRPnYh8oUGv8lRrfYyItMwmTPeVCFHiWTemlLR0dRZ_5-NH1ZkQPOmyMPTSXsXirweyRLHqxU8lhUXVTNzOVutLPIYBfgZYuCj4CAWq3ayTAvs0seR1HR2trYB-1KxTAH-Kt-nSVHEbw3BIaFms2YAoPSKKx4_GmHwZxLaS0SS57SgLkomk-2fRDxyE0mSwsMdtfXwBWUxsZ9A2P6xSnFkinXa_fglEukmEhiV06yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW6QzzcH7sAByDqhnIgzfXAKywLp0F2OzgdNHxw_cECxT7S695axbNurYpxtNjzH6CypwR4r8gktUzOpZ394LzVo0DTLvfLLS2DXXMnKhGNJDBeUVXpD6DupzdJUZR5k7xUIQkU8tU_q17ZznZPRlVdRqFMvmN2DEPTOtGgHlACQrMSYT4nDSeHX-JmJMTv8_HWV5r2avL4NCHQhOwbeGMI2rI1Vx_YUGZYe-Hbpb2sAczwCqOqTOQqfFkTgA3KQoukS7-TUtrbpD38XyClw6qDUPPEdXMxtynEucxPziULYOxN0IG71-9MCJrSq8WZPPjb7EbC2faSquHLgjmlwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsiWpIoiWa59JCirB-yWGcp1RYcec4qOhsHaCDZI-ACRkhio3gHWYx8LQYrYEWCAVmMFKzKPZwQoalFkVx2uBAjapbw3dnM72phchMMKQ2jo8PoVLK8yMvCwvp3olmdsPTAguLub27THsX9UGLzBvzsWRsFFf80JzT5qqfW0He2fosXL9TXhp0KlWYP2ePhQ84w0N7qwY_vcRe3xqKTI0mrFGgOWqxWBleBVTRu0AFTRJHwISY6JSnaUu8W12RtgZBGiiR8HQzktoxBwtj1TxTsaep-0WyyHGuTSvxkLizv-HMtInhWl2gRdVxwGLFNmx0Zpm7GRJvdOkkML7722WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSpLB7R954pqKR3nK0GbeGDKpAeTShzqNCzb5Bkem596pQ1aEmK5Mc4TZRozoL3wxbObScv7xkCEWcxD8FU3r2Rc0pcMYWfob4F1MKzs9Ft-EdD8BqDbyehStx_QLhU42SeDTW-tECbH1vtSmmGMTjdgYjN5QeEdTPlw2NjY7hstg3iBrQKrisQYYqoBFj5-D8lb_L_N8KInGRR6SuxjF5KVRM0I0Q4N7QD8qeusUi0Y9DLe1yTqg0uSht98LHzMHV2RTsyScbmYWQxYnjR8AKN98DTYQUKUsKHVg8JSgyPbr_AMvqGyl8HtQ8N6ZI6ykNLOmW5JNmUNCQMxa84iRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=fybURIH05ezZ_KU9Ax9L6PW2EK18upX27p8MccGlRt2_x9n_RT6TDsKCXO6TCxbAYqG8MULPdv6BlXh1kllhsMvyeguMyvok_-rkvY5YOs6YcJfeF4mqpQbH4BpK5HGarQ4YIVxcBQTFpOwxi5bI8WGWTEyor0Q3smNa8N5u-y_mc5Mh6hwyHxDIYxLKCdifU-VzpJLZQr-J2xuD2iVXKdJV7_n0Hg2SdijzprVmHG9B2mLqKwUhf5BylaJxX4z-mv2d-bSom7R8zt4JEE6BUY_1sqvy77oeAeQVPQF22gyZg48PInvBVlB9TwUrEr_LCOXzR3sToymotDxicdF--w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=fybURIH05ezZ_KU9Ax9L6PW2EK18upX27p8MccGlRt2_x9n_RT6TDsKCXO6TCxbAYqG8MULPdv6BlXh1kllhsMvyeguMyvok_-rkvY5YOs6YcJfeF4mqpQbH4BpK5HGarQ4YIVxcBQTFpOwxi5bI8WGWTEyor0Q3smNa8N5u-y_mc5Mh6hwyHxDIYxLKCdifU-VzpJLZQr-J2xuD2iVXKdJV7_n0Hg2SdijzprVmHG9B2mLqKwUhf5BylaJxX4z-mv2d-bSom7R8zt4JEE6BUY_1sqvy77oeAeQVPQF22gyZg48PInvBVlB9TwUrEr_LCOXzR3sToymotDxicdF--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt5BlmMY1rl23oiPymSG8BHNVOtBKTjGkfjBSYOLLdvwpZx_6dyv6nwKJz2IEZinSnDhnjnyr835Uj_NxvSveyCud5Q3YLuNXpjVocLx8-DzDKwFbStMp5JPco0b2C1rwLTsdPCuUfgN4ROPzBZuDqlT7hFDdECRsF2ewUj8B8pvQBumHyq4OXrED9QAWwTMBn9DcHxwRFRIxGG5zHYXFwpCS7D4OTm-O1BKcD1DlnvY2EWqoTTg1RTZzF33D5POoJrZNuwHEgAmaJljkAzmnwHTVgFwos6P4-0gz9cZKzsIgKvradLGUqkf1wlZ_1Pctr2vR6jp56ZmmKzv_-OV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt7nduve4exKx4-lsPAwZVO_ec_yezO0Z21lqvcdXt7xXLOPhwIXzfmBJdvjRwG95rhZfAfApO5d_gC6bm3v4-W-OFYHB8bdfqhbL3rXRUzBOHN1QUhkqEe1TYqpRK6h9bMotPOlViZ6gsAbx3TdNYTxJqo7qbApxeY0hZfmh5I5lAF2DFPbAR0znmbYcUzIkYbSQ3h99SuX6S1_Z9_kA_TCFmLoOnAvRXu0OJ4Cn2o5MFezjVE9_18HDzyN_Ca5wlRzCCZqBwoC2Prtys92eOG_pEXuBw_XyA6tUeOiwXprGFSxNve8xUL5ymx759mbBvHbQ_nOYrjVWTvw8P7K6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlWqJHnUTJwIsAfpUOBHQyiFV2V1C_8PcQtZ8KHq6mAmN-b5Y6nlzvUIVVN0TL0JRtH8yjxTH2NIEKVu3GshZMh1oOhc5yqaVZPT_9_b055v4QOCnD6u2ohZjOsLgNWU8EGqFb-rzRqkxxH_9pdlrpr0XvIKDNhMchYXLfkrmHKgPvI8fjQf5x8sMdP1rsLY3zAdClK6ptpvRBnTDpEJoa9INACWRQEcFIOoz1Q8OmzEstyvrPnNocTbRREAEPqba7Fbxa9cddfUE3b4CGKuJt7Jg-7F6G9tByXvOXlWKFrnMW82AHVwAbokZsyCo6sTWTPN_4cJH5ML4HilZE9PRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=BK0YrjNjVL6LTQGQg-xLXygIab96eoI61uztA0HnJvBtr_dKLvtJ_2jBbPBNdbiaw1ECgTMsbysA54tNlo5Uki7HDNV4HyecwBfLpK8pPqNYx633j9VfZf-YQolJmPVl5q2bq5DQvLiq4ozrKHLA6EPkQV8OOIbU8bTJuJiegF9AsOLtx3NCpPCOaZ6FxtvLWWxGg-pr_wK_kUnYEW2MV64iwGd00jRR8_XEZ_tgsNnf1Fu7OId05edB0Bo09OGl7dwfHQxNy9fJevLgQj-cuCJEkMKOikrPxQNEi9-JocVsOyFYTxeJI6zwzWBezyBgNgKPqDjBqwSnyu8LRVsYLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=BK0YrjNjVL6LTQGQg-xLXygIab96eoI61uztA0HnJvBtr_dKLvtJ_2jBbPBNdbiaw1ECgTMsbysA54tNlo5Uki7HDNV4HyecwBfLpK8pPqNYx633j9VfZf-YQolJmPVl5q2bq5DQvLiq4ozrKHLA6EPkQV8OOIbU8bTJuJiegF9AsOLtx3NCpPCOaZ6FxtvLWWxGg-pr_wK_kUnYEW2MV64iwGd00jRR8_XEZ_tgsNnf1Fu7OId05edB0Bo09OGl7dwfHQxNy9fJevLgQj-cuCJEkMKOikrPxQNEi9-JocVsOyFYTxeJI6zwzWBezyBgNgKPqDjBqwSnyu8LRVsYLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=kuRFKVI1ubI9vVZ_Dz4w_OUBuKbJDnc_YV4oSUFN6MCWLAvz3QN5fY4t2MzRef4oCIsgdD1oP6cUkXXtCBZqqIsrZTwv3AHTulGbF1Gbrue4Ey-6ihiSAh8XW73EHgB4r2USAsq3vt89Od-lXC-1TGH3MC_tbqE34Q54BkqCR0YA7dm8XfA1KFQkaFjWOrdidKLeBm3Bg2uquJLgcDDATT1X1bD-Z_Rcv2O4p9dan9ZJ47UsHA9lmdnMXsSvOXCgMsYkJUXZdamufERkQa_wsc_XEumu_zIe5yEYuwfZbW_y60jYJdDTA0QQzaInSt74q9gbFCuDF4M80znTlVxoOjqR4m7oHKahVvhP2gqcGoDptuFTMH4zPqRWbNUv9zMlr8AWi8b_rZznhy4lFPN9oRBZMS4R7C4ucnrOzGWHu1ZqXXKq8YlImSXLtdegJkoOJ_bow6WtocoaXzMVhW9rJTia2kOmfTzAQ6-ISc3EeZ35CRs1yl6g4gghUyQ2bM4LXqHp-fodBQ97-3C4tZXdYFbH50S8DVG4zRlbeA8jAg8cilRPQA6MbxmCv9FzC9cRceYgbXKsjpGvTx5Icj4ZhTsTpB9Ta30K29FCZD4vAujAX-carFlPcLqsiKMQRyWDkZgEByETYE5Ep5Gaz36siFyY1T34Y7E6Un9PsbTcAoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=kuRFKVI1ubI9vVZ_Dz4w_OUBuKbJDnc_YV4oSUFN6MCWLAvz3QN5fY4t2MzRef4oCIsgdD1oP6cUkXXtCBZqqIsrZTwv3AHTulGbF1Gbrue4Ey-6ihiSAh8XW73EHgB4r2USAsq3vt89Od-lXC-1TGH3MC_tbqE34Q54BkqCR0YA7dm8XfA1KFQkaFjWOrdidKLeBm3Bg2uquJLgcDDATT1X1bD-Z_Rcv2O4p9dan9ZJ47UsHA9lmdnMXsSvOXCgMsYkJUXZdamufERkQa_wsc_XEumu_zIe5yEYuwfZbW_y60jYJdDTA0QQzaInSt74q9gbFCuDF4M80znTlVxoOjqR4m7oHKahVvhP2gqcGoDptuFTMH4zPqRWbNUv9zMlr8AWi8b_rZznhy4lFPN9oRBZMS4R7C4ucnrOzGWHu1ZqXXKq8YlImSXLtdegJkoOJ_bow6WtocoaXzMVhW9rJTia2kOmfTzAQ6-ISc3EeZ35CRs1yl6g4gghUyQ2bM4LXqHp-fodBQ97-3C4tZXdYFbH50S8DVG4zRlbeA8jAg8cilRPQA6MbxmCv9FzC9cRceYgbXKsjpGvTx5Icj4ZhTsTpB9Ta30K29FCZD4vAujAX-carFlPcLqsiKMQRyWDkZgEByETYE5Ep5Gaz36siFyY1T34Y7E6Un9PsbTcAoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5XPltFwgTUggrvJqKBvVt0mmXd6pXbNXdGl3jMrZP3bOmIvc8X7QS3i98F29BDRKmxk0RuqEE4lcyuICjdvrs7RIlrB7xslDCtmWCXe6lfwVoNPx_U_q_PZubsYydceUsbf7dXaXFsZK9_AX2J_Jnsai9HHcakRf9F5Do2iTGSZQY6fRcAmrW7D5grkyqoiKClhu5kLJusxdblwTecDLx9BSm7-TVoS86ajuvmQzxG1UoDs82ZmG97rar3HoU0OfjfIfk0XaTS0LM70sp0TgfkDUuIfmdBR1cu7frDAzHr445qGdKfdutzYBouANwVZTT4VL7dOXTNLK3H4tvQU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=Ma-ycWx_iN3MUaZ6sm3xQEcFfbUg3kk_tk8iJ0jLC1cgthV9Wsa2YC0eI8RNzwOpqKOomS7PzcSi7AKV9pq4m2EJN3HmdPV5rlJc0gp_li-Gf4jQYBtLL59KuTuP52VvCh3lk_yfeTNdfoO7gk7w0xMzghij9SIswHPhVP47s_q8A75a0vcSxM4tU0IClAQjpJvsuh9V2_QMwy1i6RarE3fSPsoo_5tbqZ2MhFZjuJVkIXn5mQM010sUb5593CqrX7bgjZz9I_oaugxq-raPSSzE529P1_RfWfV5pGj0OQJ_KZqvycxrWGy6ieLS1PIxgyFvhcDtLP1nFoo3wMNPIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=Ma-ycWx_iN3MUaZ6sm3xQEcFfbUg3kk_tk8iJ0jLC1cgthV9Wsa2YC0eI8RNzwOpqKOomS7PzcSi7AKV9pq4m2EJN3HmdPV5rlJc0gp_li-Gf4jQYBtLL59KuTuP52VvCh3lk_yfeTNdfoO7gk7w0xMzghij9SIswHPhVP47s_q8A75a0vcSxM4tU0IClAQjpJvsuh9V2_QMwy1i6RarE3fSPsoo_5tbqZ2MhFZjuJVkIXn5mQM010sUb5593CqrX7bgjZz9I_oaugxq-raPSSzE529P1_RfWfV5pGj0OQJ_KZqvycxrWGy6ieLS1PIxgyFvhcDtLP1nFoo3wMNPIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYnco-oNGMTBsbPALlMIVSOPsOU9hL9CKWo0EmhEMolAq0WmXyshbHAuIZnvmvMQbrSWW1tJynk710cp5VqXCReShqOAY2rGiW37thh878N47sncPPzaZ3IvqUnwIEC4auuueqfOmgHIn3iuikekxyL3NU4ilTEjYfk7ziq3X1LH9HsLD27Ke2HNv9U4voJsE0U902D2Pl-YsOBwvjQwe3b2DWQU1vAnw52_Ee0bKk0DIRH0yxw4NJMTH_OqRZc4YHVq-KeGv_b7_pQ4ZeCkFvaBV70RFUxDPycWmGigQr2tZgTctoQ275nhhSdFRDY3wPrsbB-FllDBTXm4pn8uGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=IpvPSYVmD1wWSCyZ3TbFRz-Q34UA9bzsAK7trAYs8HBNWOO76tUNU8fL3hQIN3TEMIyNcl6Ud9iqyK1hl9-fs0uRGqb_r6VGDpo9Zd_Y23EOLpaUydDGemEoWrZGD2YnVibOjN0stR7A00u8YG8pqSmn7NzGYTN9vQ_iirj65S97ykgtpxvRxokYyCFcBVtQKo8U2nL6DAJn--aW-BdCkdESUfQUlWhJ-uxEHkdOpzaGjGaJiIrHO4R29B86n7VPZU7ZDr3vS5vAdi5RTqmWSvYtlpFGZjyvScJvsvX07fh9iJchDTdYas2QGu1WaxjxsdbTh_2Sv7Fvfz6QLN6GFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=IpvPSYVmD1wWSCyZ3TbFRz-Q34UA9bzsAK7trAYs8HBNWOO76tUNU8fL3hQIN3TEMIyNcl6Ud9iqyK1hl9-fs0uRGqb_r6VGDpo9Zd_Y23EOLpaUydDGemEoWrZGD2YnVibOjN0stR7A00u8YG8pqSmn7NzGYTN9vQ_iirj65S97ykgtpxvRxokYyCFcBVtQKo8U2nL6DAJn--aW-BdCkdESUfQUlWhJ-uxEHkdOpzaGjGaJiIrHO4R29B86n7VPZU7ZDr3vS5vAdi5RTqmWSvYtlpFGZjyvScJvsvX07fh9iJchDTdYas2QGu1WaxjxsdbTh_2Sv7Fvfz6QLN6GFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpSp3cM8q8brPkjZTlR7IzDtRQErx8oqsm98EoKVhSlklXOo4sr6KmBwUA07ElYVWT1NxdhM6c8zfpBhPdsqRUXUWJmaxCwaOeOr7KMgGgNv1nNx0YiRnY96PYmG3Qgb9j2HKnzBUjBFFu5fqRm_uF19zXash7vYmzZhdI7RBYEATaS5zrSKlhWx8szhA_MIyV0bYtF_ZKPNVma-I7sw-aHzkiBPnarfKNTyVcgEz6qyJPdIkLeib4Z--Lkiy8p-HKpnJPAYxpoNWu0dJ44HeJPRZOonRLeVZXZzGtVNuYedM3IVfoTKS1J2esRzOmazBBwf6SMmLf9yvJvZzUXU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=QeMAgmMR2Oouu3JdfEJWf3VTMrFxgjZs9opoXn0fl821a7qzzcM67KAbnTau9xhur8bjJJZdP4yYSnab8_sjOG3j4ZfZ3Tl3a4g72gSUsM6Kb2DEUIDbHmwAfYTgV78yQPd8-huJZY9NmZRe32GsWC9yk4hodbPau3KUO9nJXZDSuE9qO5UE3MAEbA7YapqXi7JP7u2Jp5M9_yH0hZLvvzitniFkW9WLr7ds72B2xtjWuatNJ4kmtxeBPPh4kx4u574nVp3DJZ8UrStoHp94Ug2TtBCP23hgKVcvMHs7JOekvnwJfkea1ZT-Q8Sl1BolbJ0ay3s4kDz24hZcC7iZIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=QeMAgmMR2Oouu3JdfEJWf3VTMrFxgjZs9opoXn0fl821a7qzzcM67KAbnTau9xhur8bjJJZdP4yYSnab8_sjOG3j4ZfZ3Tl3a4g72gSUsM6Kb2DEUIDbHmwAfYTgV78yQPd8-huJZY9NmZRe32GsWC9yk4hodbPau3KUO9nJXZDSuE9qO5UE3MAEbA7YapqXi7JP7u2Jp5M9_yH0hZLvvzitniFkW9WLr7ds72B2xtjWuatNJ4kmtxeBPPh4kx4u574nVp3DJZ8UrStoHp94Ug2TtBCP23hgKVcvMHs7JOekvnwJfkea1ZT-Q8Sl1BolbJ0ay3s4kDz24hZcC7iZIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=PVENTUUJr9MCddnMh_HV_vgjHP2_8uW8QmFjcI89h-jLts_BZionda7thUPdnR-JAn0GljXpI-hDidqnEiFxbuJxqXpt8gB6HLJSlCUDAiwAqqPW7NMNP_ud2d6vCC8mi60hMXrnT5KSkXUdiB082ZYXHdOcnMI_N8r7LH27-bfQjIeOrfnwAgN4_YiwTJ_VUBLLhzTiNaQ94yi3kqNTUMAPeViBO8jar3r968hQ63weQdPWqkJSB6HbjXXZugcKwCnfaAk79xV1kb92oIa3UX2hmfHKXJPiLTNCH07sduBKJrwfF-fEHitaxHaDnUvtgUWK9MZc8_kPqhUDYLHqsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=PVENTUUJr9MCddnMh_HV_vgjHP2_8uW8QmFjcI89h-jLts_BZionda7thUPdnR-JAn0GljXpI-hDidqnEiFxbuJxqXpt8gB6HLJSlCUDAiwAqqPW7NMNP_ud2d6vCC8mi60hMXrnT5KSkXUdiB082ZYXHdOcnMI_N8r7LH27-bfQjIeOrfnwAgN4_YiwTJ_VUBLLhzTiNaQ94yi3kqNTUMAPeViBO8jar3r968hQ63weQdPWqkJSB6HbjXXZugcKwCnfaAk79xV1kb92oIa3UX2hmfHKXJPiLTNCH07sduBKJrwfF-fEHitaxHaDnUvtgUWK9MZc8_kPqhUDYLHqsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLNUnwdPR-wheXI235kEz8fH-7WWdfK_qIsAqJZ9Zwo089U4CCVlyt9qr4_w9Ci-qEKFppZGtVUW_6YeIQvG4kecNjB2KVpjy7N4UMxD2Og1at_46OzeC4gf1Q11b7tTfdYyPSKua9tdYdzKcAk8DdvwORZGaGodmmlxk04ey2BemenTxQ8gjvF8_5pmVDc-eQ2Sgh31hb3Me4vojkE4T5n_yyriRzQBdRd8A_IsEgKgyqFJwz45BsWh91h-oYzb8etwDJId5k7siptNWkdiqVadwglrKCcT9s9rkAwYTsKYkPcsLbt-dkhkBSCpp-IiVcf1o6lvI2MoDPbZ1_dfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=Z5XL540PtwQPS3x4M9nEZWFheE2T349FGw249jhudzihKoc8QNnYalx5FNcIB1BNZgwPMw_04f02u0h6rVSqw2tpHYEZuvL-O6-PDZUs2--PnfCqE0Ean7Sg4ME3w7ai96RR-YGnEmD6bOCJZMuz8SRb1dLV-smcOXhPye_FoW1ZuzYDSF2K3ZGkjS25YcpOj3KXeK0mxP20TtSUJohkQ4oJOOwA89XO_XknO2v29TCBHG3PzdpOFd-79xhVtCmAi3vQF6JY1rioyYb-bVWXyxkgnAzMa-BhpFWSi587Z3-E4dBaUqi55exDoeycVzby-Y4-BrR1KMWLJmsHFXpMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=Z5XL540PtwQPS3x4M9nEZWFheE2T349FGw249jhudzihKoc8QNnYalx5FNcIB1BNZgwPMw_04f02u0h6rVSqw2tpHYEZuvL-O6-PDZUs2--PnfCqE0Ean7Sg4ME3w7ai96RR-YGnEmD6bOCJZMuz8SRb1dLV-smcOXhPye_FoW1ZuzYDSF2K3ZGkjS25YcpOj3KXeK0mxP20TtSUJohkQ4oJOOwA89XO_XknO2v29TCBHG3PzdpOFd-79xhVtCmAi3vQF6JY1rioyYb-bVWXyxkgnAzMa-BhpFWSi587Z3-E4dBaUqi55exDoeycVzby-Y4-BrR1KMWLJmsHFXpMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIPRdr3O4lZIsuC4OrqoutsJlOoTB74LyqOp2o3DO9yZfjcb-RtwvNVmvoNCHHinFaW6Pcr3VVc6MZHJ8OdvkGg-pJfpaTnILWjsPbWdi-3ivkc7LBPAv5iDpiB4U-iurduN4hqOuag2AYOSsMMMFWAN1HTKZP1gGXOTXpEQTmUt6CxmH1U917ydbTiWNF1H_FYImR3HrnqIo7ZZ1FNyZyX_MkNk9g-vDpLwjfRTaQCU7_uVx_Ae-qPU_kcpvZNvwmmLqa40qQCAzwJ2Bk55iCY4_pS8ZqfjiUnDZfYe8EhMGGd-9neUHhkSTKwmCe3U8pxFbToO2zZZvCn6q7qiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=dWqiTsIACV4ZcCBWWDpk6qXNbAFxzfKbOev-JkcCMQ9YRwkEQ23iRXkGDWywcslYeAE2Z83ws9xi0pbdok8SFhhMnw3KWFl_7r2miPPaN75T2hn9cnjfpDE9Nsmtnc4PFHkPAKcWJVqFsb3vL8SOn5XEUwvIoTInjgZFXwq6QWNMbQacJPRGoe0b23naQTKkvXNd8__3wLaJ7hWUubvAD0toPVM5pDAneBn78MBJ9qaptk6PhE74h2ZJsQADqawRB8uNxcisTdgREH6h2F4quFqpr-DoGdlieklBHIqZrxnYZHPleqgLrUvbCRWD8nOX5OsqmMPxg1RO_fZKC2dGRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=dWqiTsIACV4ZcCBWWDpk6qXNbAFxzfKbOev-JkcCMQ9YRwkEQ23iRXkGDWywcslYeAE2Z83ws9xi0pbdok8SFhhMnw3KWFl_7r2miPPaN75T2hn9cnjfpDE9Nsmtnc4PFHkPAKcWJVqFsb3vL8SOn5XEUwvIoTInjgZFXwq6QWNMbQacJPRGoe0b23naQTKkvXNd8__3wLaJ7hWUubvAD0toPVM5pDAneBn78MBJ9qaptk6PhE74h2ZJsQADqawRB8uNxcisTdgREH6h2F4quFqpr-DoGdlieklBHIqZrxnYZHPleqgLrUvbCRWD8nOX5OsqmMPxg1RO_fZKC2dGRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=J0bmDtQXWktUb7-oDobbyBswWKQ__1xd3pmoh6DTMbbOD25gJmMYQJPF2xbvwcRIDdz9pmt8rI7a4E0K3FoBsdxjeBipp8LiSJ2TwOF6YaCTLcalUVm5DxIkPhfL0RDlozWtU4XC8KthED9oBxcOfeaHfoI_s6q60BJRS4qT38KziK-GZEG_wL5crJQ8os4KF4ZOmKfytWkL_cxo8n9fwgMSLD-pNsCYUgy8pWicsmAfOjrym7EEQOSP45VHmUpmdyZ7gYUWija2guvDvMmmzHgy7dlXZsW2lY7kgFZu2zV7mTfc932veqU6kIXLfGm4JRd1fFJdlJ0LoOMmz3j-hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=J0bmDtQXWktUb7-oDobbyBswWKQ__1xd3pmoh6DTMbbOD25gJmMYQJPF2xbvwcRIDdz9pmt8rI7a4E0K3FoBsdxjeBipp8LiSJ2TwOF6YaCTLcalUVm5DxIkPhfL0RDlozWtU4XC8KthED9oBxcOfeaHfoI_s6q60BJRS4qT38KziK-GZEG_wL5crJQ8os4KF4ZOmKfytWkL_cxo8n9fwgMSLD-pNsCYUgy8pWicsmAfOjrym7EEQOSP45VHmUpmdyZ7gYUWija2guvDvMmmzHgy7dlXZsW2lY7kgFZu2zV7mTfc932veqU6kIXLfGm4JRd1fFJdlJ0LoOMmz3j-hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=XUVqpg-UvZxfSmIU9vEt5E2p8PT9DJb9X6Qqd105K7kT8BgWfsETrCHvkaTk-yuEnK9R-JqVDjhWM97gJX7iwefdOHU5e6-06ah42ZGUlwZV2zd21Rd2LBClZXQrfhn3H1VdSXL73O4wioCMk1l3DA-_NTxzLu-_CByqhvFvE6-PMoWbcS1s6CXRAOgzRrZblCNS4aLiURAxRhpVJJPKGPyVPFCYhzBKFotmM4-H7Ya2SQlC3hSS3eZTaKdA84QQref8CDJ5phYg_si9PGrdlwaAS4kKt7pmZk8lUMG-4mQzsoVDUJE0LrTWCtxs-tEuLEXKyEQj-2EQrnU-2RA89w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=XUVqpg-UvZxfSmIU9vEt5E2p8PT9DJb9X6Qqd105K7kT8BgWfsETrCHvkaTk-yuEnK9R-JqVDjhWM97gJX7iwefdOHU5e6-06ah42ZGUlwZV2zd21Rd2LBClZXQrfhn3H1VdSXL73O4wioCMk1l3DA-_NTxzLu-_CByqhvFvE6-PMoWbcS1s6CXRAOgzRrZblCNS4aLiURAxRhpVJJPKGPyVPFCYhzBKFotmM4-H7Ya2SQlC3hSS3eZTaKdA84QQref8CDJ5phYg_si9PGrdlwaAS4kKt7pmZk8lUMG-4mQzsoVDUJE0LrTWCtxs-tEuLEXKyEQj-2EQrnU-2RA89w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=ilNy_gUFAYJ_8El4yv3RR7PYO3hegE3IBmqher7RHvi847okzo_nBsNAWSWpvNfsVR3Gu8xx3E-AdK3xShwdx28lsG9bM0oA1hEKf7zxcj9rQJUBG8-Da6mLfQTEkaMOKOd_BNa5FHO_lUx66wIBbf9S-Wzdj-Per3fO9TehLfNiU4CdCCu8Za5E8XiPfm4CtFNNmZXsadvwmH0ZZxEXuS2Pi1-URxYYEAbX6QvGfWCuo10FJc_WY2_ld88PQ8dapCRiFpmiRU4Quxgw7cXSJrFLW_aerBOvupAfTDX5ofk6w_CevNLNRhNwvebjhwY7ZGHQ93Srq2CN3JGyrpjF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=ilNy_gUFAYJ_8El4yv3RR7PYO3hegE3IBmqher7RHvi847okzo_nBsNAWSWpvNfsVR3Gu8xx3E-AdK3xShwdx28lsG9bM0oA1hEKf7zxcj9rQJUBG8-Da6mLfQTEkaMOKOd_BNa5FHO_lUx66wIBbf9S-Wzdj-Per3fO9TehLfNiU4CdCCu8Za5E8XiPfm4CtFNNmZXsadvwmH0ZZxEXuS2Pi1-URxYYEAbX6QvGfWCuo10FJc_WY2_ld88PQ8dapCRiFpmiRU4Quxgw7cXSJrFLW_aerBOvupAfTDX5ofk6w_CevNLNRhNwvebjhwY7ZGHQ93Srq2CN3JGyrpjF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncqPKO42H8JQMbbCrUuiFRePQSWx-pbsGvDx_p9FhdBqfyTobx7Ao6ROLBqm76QkfNjjmBwb1XUPzjjNWkoAK6xQh1LhOQlVwPTfP_m2qcTrAhnZ5TPo0X0UylK_DWDD4jncude-VkU5ok8NWJFKj2YF8RFVgdxmWgVmgBUy3CR8t0oJIZnun8oO5ljtlVdkQU4_0CGjxcbCkdOfaKX3nf366XKvEXt5XONM3W1VDfgktjebJ9YDqQUfOtEFUDqpHLGEcwUPsVtyYFM0J9PmUI-LcJ3pjlCF_rAEg9De7USmg9GQwC4XSoGK7n81akKegtdk9kAy3dUak0OZuneA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FRKnK4z7bT_7uc9fPSoJZ42QlGmlAeD6JxwnWxARS-Jvmet6mRfMtH9aDpTk0KcVG7YOan18Fnfk1ttXAwfqqtNaKhTgVdKqHZaXqDgyGqEYeS0cXDl9fyrmkS4CoypAKNAV91vQyObr4XYeQMnty2m3KEfr-eba4_x5oZMmAsDZP_j7FkqHRTZhZFZxvMQbIMzGrA0EO0bXVx0a2ghhRzI20Hf1ZmtrV7PV6IZ9HB7fX5Q3dhFUD8-IeYlsHj8n992Rzv0UKNZxLo9oIu9HFnyTWOdHTZQ9emUEcPAG1Mw2OxjkySC-8A0p1VxD5zV9aHh7LfJiLInFw8KrRGcZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSOMGCUF6UJbuvI7W8dtsr_6hPic99AawLurKkX-zMzz6aWQMORzXE71LRk_29qpfB8OH2sZrIynI8tV-q63Grh_vEzQACW1pJYss2VnqDS6M9bLMc_wrqNyCBgcBw_cV33lBs6-2TLhDbegKdNqs4h4Lv8zu41HM06oVcFDM-m2B88uMDr7rICU_AAkqyneiN7mRpCBgA4bO-QlUKKKC0zA0Sfaqbe2l6RUwUotfjOtPoUnPpyshFX3jBL3sucUmGJsgOJcKJh4wB5McsJRW4ndDpbm6vL7-MgfDsNUJd2uU4hpVopS_bdb-yYbtRscZ7Uu6doTFQviK5LzwEb6gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJwL20QhAGVMOxcDGNIIVZrxoJ_AntkbKInISEcgnw63o764gzOyDqeY-QmIJR8QHakcqdGH94zMX-j_E-hciTKJdXsqspiXL7yhUPJ_z2ZMu_JIqBZggf3H2sTf96IFON_1G0ZlDX4ihm4JhZzHWj_ZsZBvOAVMoAbftGBPyuotlGLAJNaQkKI7N_goLTSY8KvNnp81Va4luE_L8SxClnG3PE-2vPg7EU2-WbO_vv-mhPJr4wr7nfMRweUVUSo_8j_1Sgzr1soC-KP10GmScd03MJU71QddbtRHIrNKDR7vn4k6R9uvFD6p2SynfeN84djvm0pmUThqVCnxxFW2Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpC7hSdRlYnUqiWVD7X80J4EvffTCj9gBeDlsPn7b5Cek-mxzgf_Y3zxvLv2ungizFCahiG73BNfcvJi7j-StlnaRUtUTaoaV9-esTGS-CSOemYbR5tFacxAqLPoZQdxNacQD889hBysFSZPbDK-uX4ebd9swMm3sCf8ioIBne-x-oxpasLDch-qa0i7g4Yqe_WUlbiwtlq3t0zZvxKrUZiPPehUifKPEv7uMzr71s4xIJMLvxRq69pBSxADNJcTHbidgIzudTUQDppz4uW59piqq7KCjboT6jmp1EwhiFeZurPETgIvokoQ1bWfHnvo_s4db41V-vYRJQ5S3l-NyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=vSEpvGoOzHx9FwlbAIJfKxW1kSMGj3kWPhS5bosLFo9n2JZLnFZnUogn64fq3oEoTs6b8RwXFcRsCIdszXg1Gxkzjmo9dAVrHkTkRDZrDY4D2CNydbf1t2CVGDDaCxv2X1xC7FaEK8_5ZJXmfEyVtiaS4ZWkl4o7_nvTrFupnvTnnXhUCv4Sxho4RIil2kN9wVLwkC2UqlhXtUN71ab_SVWEsD76qrGYiixM01RLgNAqdvN2Vfz_NJnQ2V7dqTuIFnZ2pJJDvdXoFN1AVmFOTSKN7UYeS00ctLrd033Kdtslg2x1cF19CWnHzZZohekQ5NWnDwMH6d5irG9K9KZtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=vSEpvGoOzHx9FwlbAIJfKxW1kSMGj3kWPhS5bosLFo9n2JZLnFZnUogn64fq3oEoTs6b8RwXFcRsCIdszXg1Gxkzjmo9dAVrHkTkRDZrDY4D2CNydbf1t2CVGDDaCxv2X1xC7FaEK8_5ZJXmfEyVtiaS4ZWkl4o7_nvTrFupnvTnnXhUCv4Sxho4RIil2kN9wVLwkC2UqlhXtUN71ab_SVWEsD76qrGYiixM01RLgNAqdvN2Vfz_NJnQ2V7dqTuIFnZ2pJJDvdXoFN1AVmFOTSKN7UYeS00ctLrd033Kdtslg2x1cF19CWnHzZZohekQ5NWnDwMH6d5irG9K9KZtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fLFnjCBr4wAhqpgI4z4kfvgn6Kvkua8Uw_7TTSa3JZ50reeOBgWhy-oqlm8n4-lwvnWwx5g8BFGNOKqTmfm9umtIJ3-KWa1DMotSGyG6p5hsy3KyOcBfUApsBuKc9pYdZ4ebHZGuXEpvn539K3xnla8-RuJfEB3CUhxIf0SJYjuYDx2XUAXznd2lu-jZglNcILtQ83nIrGnR6gt44AskauUp7dkOgJBBw9oqhMORi4tkQQeqgcDHLHY20k1Sy5_BVo_kpcr5Uqu-fMdKA0xt_g6jA_WiO6cXnKBAFLcZ1GkMRmJxu6SBd_lXEUO5o8XpdzsbrD45BWHacaFtV7aiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zfe-KhaKEpDU2FFHtWy3pQ_TCTuv_NuikhvCPydgoLJXwgwJ1mt6O5RERPOyGsXWZL2wYrkkbpziL6wY3bCRRvlfJo29GVtGclfv6jxViJqC-x2E7LVQ-izQqRLEUOVrlMv_AnUiqvyrqjF7yrOWhikXuQd3lIZ24lDdM6iG-rCmGhXGigRZCi5YRKXk-_xTiRkMbrQz2_Ti-UmhmWPNyVW56iNAgTqH8YDvoXXY2gzcdV2-wvZlaUGSq6B5nS_Zuu_hqn8OFYVZVrtN5Ym_58dXG_fKj-xAKYYg8pRzyCQR9UcSx6Xn902CRtJNcnX4sY5leGPI-hZyw1n1SSkUTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cySUK3L_QXX90IjrnY5clKnheVcsQ3Woao9MHf_THzMUFtNWjKoGDXsJLq7xk-SgvGICLMzo4ZRHubRQaWArWvfjNr1Am5DKv71FCEC5BdFsfKTW6iMO3ABfN5RUCj2zdvLaR_gS1NMuVLBhv-LrT91rgzTN06zCypUP-fEiaN40Xj4tFRKIfU7MnNn2mRnYbdMxVQmqZp0ux8yL4FVPBvmytDOv0w5T1HnUWb4VWW_VooWTPIKrf0_3WvCi2_RK2G7HHX9UsFWPtQy3PVPplBTH2GnryD4mDJiwoBgXj_e-L_UJ9y6pgGblIzWro7iMoNG1PBOjB3Tf5XMxN3nqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mT9_MhPz2QN9mgvkDt1ghUrgM6b6WRVjB1q4ltLqmkenaLfIXwSjUd9R1dYFpLY2FEtJwVgCIee0BcFvEXhbOj009x7RIL8lDVIY_zD5-d88jdLa6xjm5k4jM6OALeHTvOsqteEn-8g1heScB2hEk1mgFGUkFjXjaxw-Fnlyz8TndCPNYDim5munNzORUeg9NjjPkxHsZr9-dplFMzJRtogTvSCR8MfupWqbAOQfBJNVdD4szPGfH5QvRVBOeGhI08GVf-RNXR-Z9A0jnFa1AkN-_nRbFBleAQNOgITUsK6Fgv8OWUg4G6nXgtOhfXjqqqczzZwhlAecqKT7nBuYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaeaDzUijqNV0grd1OsKmRpK0sJNu8FMQMdZ-D06bU8PXxBkm3mzsftJ8pLrrsJwMyJIYsSjChj4UBgMqPMqGSpgGAGxwN5xvZ1Sa4zV1tUAdGjYLvtx-T4vu9gPMbmHMW7dTCo0yYSXg0UvPdXfX_emr4d7rfwy_ruUte53zXxXGUQE-7rZIz_qRcTIkGv3QL_0bJjCmA7Ef11j0vTrfZRd-eovxOuLrHc8LKB3ttxZk8w7OK7we_iAxAH43exoNhmJp2sJIn7mgD6jxcKL1PKN_iXuTXC6Oi8M8SqwSuwJbmY2BAwxqgsJBuSq13uW8osMtQuIcscrUGB3dmUBdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrIxaEPZ5o6ZhWoFw-wzGUqLg27T7Er3kzQUjRqogQvQiMsXPVyTjYzrp2OJqbHjZOnEvT1O6bBT0wIazm0EGg-t1b-EUWddmSdQabnhAiKy71532NP1b9FbcW2_lM6JmiRj1jUsjesTpZSLDQaoxv4pLt9UGeezdC1Q5bD03ZRtyEzmTYjFLfUOe54Z4umSSwUhBTzRUhJRGt19jA6u_DpN4ffx24hOfCudSUrKLyZp_-DSOfqbzGmvAZUw0DNSfDq3nekfOQmbei3H6MqM8_6yIDvVc7C7iYn9jESjjB4insdgsxRL9ZcDo7kfxJBCA50w-oucSM1mBNYR_q0ArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=sJjZuNbfugF9UQfnS8ox92Zfx34Um5Of_pmfkItjlB5VZ-2Raho7LUmF4VtJOxZY_0TAkd9mPaEEqXbMQSkz50PT1uPnHrHF9ugeFYpV4XeLCTc3_EmpSt4i5R5bT3PB2PncX7xTWgnGDGK9rjXeENJHOcgrLdcruQvWPC_UYeQMqnUMs7b5OW3VOY-cFEkg2-458F1lWon1VvH4Gdr8n-FAUukmUu2zYxhAZZbLId986klpYK7f5oHuuVdZtmdrfpxUG_PPo4n6a3_y2fqbaoL3DmOd0zTJS3rrz4ppG8wxyxEcEDrd_3uDi-SjvNzT-iYxi_Ah3do7Q9GluS-Ypw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=sJjZuNbfugF9UQfnS8ox92Zfx34Um5Of_pmfkItjlB5VZ-2Raho7LUmF4VtJOxZY_0TAkd9mPaEEqXbMQSkz50PT1uPnHrHF9ugeFYpV4XeLCTc3_EmpSt4i5R5bT3PB2PncX7xTWgnGDGK9rjXeENJHOcgrLdcruQvWPC_UYeQMqnUMs7b5OW3VOY-cFEkg2-458F1lWon1VvH4Gdr8n-FAUukmUu2zYxhAZZbLId986klpYK7f5oHuuVdZtmdrfpxUG_PPo4n6a3_y2fqbaoL3DmOd0zTJS3rrz4ppG8wxyxEcEDrd_3uDi-SjvNzT-iYxi_Ah3do7Q9GluS-Ypw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=mzX3X2J8Hj9YEo_NAmE-eUOz-0ySZ7WxY4hMvuo_e-soqNhj8J-ut7AjGKQ4KVmuqg7otQ2BrZ4w4I1v7lYz-xwedfEgPYV0rKWvnOSzGy0YYGOj1QfVP2mDO2Fsu-nFGE7QMOJYlnmOil35pmIFb8cklC_nKsUsFnc5wdnxayVpzoaj4Qrj_4gDlZedceyFvAYyJ8VvcC85TRQp_Uk_lAcMMCSd9zeDAQpbqcAxl-WGJDLewQBN7ji9IQHyqCsWmkDPKuik8UaUPsNJwUU42zoMj5_aR3KXC4PVimvRGReoWOskmbXfh1ZGpdEbbvUWTqUdMSeR_vXzdzjGUoqbeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=mzX3X2J8Hj9YEo_NAmE-eUOz-0ySZ7WxY4hMvuo_e-soqNhj8J-ut7AjGKQ4KVmuqg7otQ2BrZ4w4I1v7lYz-xwedfEgPYV0rKWvnOSzGy0YYGOj1QfVP2mDO2Fsu-nFGE7QMOJYlnmOil35pmIFb8cklC_nKsUsFnc5wdnxayVpzoaj4Qrj_4gDlZedceyFvAYyJ8VvcC85TRQp_Uk_lAcMMCSd9zeDAQpbqcAxl-WGJDLewQBN7ji9IQHyqCsWmkDPKuik8UaUPsNJwUU42zoMj5_aR3KXC4PVimvRGReoWOskmbXfh1ZGpdEbbvUWTqUdMSeR_vXzdzjGUoqbeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=r7t1PeGlw5kcSJkRNZoKo2ljoK8mMvzfe8tS7r0eSnZ64dpIGoB2GcSaopNzI5m0udkyOUY8e69kxGc-vagFKeaCJSizaL0YpS3aWerc3mj37o4elQsvynZCWME43qRjDik743fQwgvrVDD0SNhU5Qc_REGhNWnQtc6FphqMSXh1msYxQRpzxY4Nxi9KQl4-4i0sVkUs0IBLFlUIkKQp_OZ5ZfktskPUYJAGNagbMqB7B3q6HZnztt2nFY3ujg8_KY6PMScPuoZoseXwHDV2hEaQsWFAxOVCSTd_hX2t6VHBrQ3zKtho8sQpb0Ui8ouns3VGsBJM-JLoaEzlL67hJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=r7t1PeGlw5kcSJkRNZoKo2ljoK8mMvzfe8tS7r0eSnZ64dpIGoB2GcSaopNzI5m0udkyOUY8e69kxGc-vagFKeaCJSizaL0YpS3aWerc3mj37o4elQsvynZCWME43qRjDik743fQwgvrVDD0SNhU5Qc_REGhNWnQtc6FphqMSXh1msYxQRpzxY4Nxi9KQl4-4i0sVkUs0IBLFlUIkKQp_OZ5ZfktskPUYJAGNagbMqB7B3q6HZnztt2nFY3ujg8_KY6PMScPuoZoseXwHDV2hEaQsWFAxOVCSTd_hX2t6VHBrQ3zKtho8sQpb0Ui8ouns3VGsBJM-JLoaEzlL67hJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1Lzqf7AP6yqMxCGiGy86zXfypIaczxv2ph8riq_TUDjJMFXxPB5L08ZIADYYcu8NMhEnf3pSnKIOsCnlxU0dn8Z6Mss1zgOXUGexXZWH3xu0QGg4CUO6qbcwa0iANU4qBURatw6QEgYQlem2Hz5ZfZCwDi3BGHlkjgpddCHZ72WsmetzAM1hQI1fTougKbglYHyPMq790Y3fAm0zlBt4_h0N-Iv_hCYBcdyiVA-QKm24ZHb_F1-tmN_jX5g-6628sBjADs0FENmJEp8N968lgztGaj9yq4qZfA6YtepEEv3gPCcW69I3BREy4OmzyrbNrFsGUn-suE8snKAw5dALg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=h8PlfXbvf7yyiAhqUhHomHOmCFPTGYDAm7Sl61jbZmPf5HpRi21ZeYngRF2c_6_Svdga38l9co9tVKBtYuDh5ZgkseegKj8LraGJXEITmpAidbrk0pv0_9uGIlgZbwJtA21ShhGtA3KsUvFI6xtYsepIPk8NKNPnrxzPQ-xJdrcSX_zEaux1oAuePXy89IgXikYhYusU8pZDyxBDvWVAH82LKqukqkqlbb_jhme4YCRtAE4ugRlBifouRBP9Y6VlXYJ7GbXu43SQ-s2mfNoQf4Z8b19W8tiSjz0Uf74evMT9SCUZwc3bJTqhHHIToQIdoVZCxBmj2akQP7T2yMA-mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=h8PlfXbvf7yyiAhqUhHomHOmCFPTGYDAm7Sl61jbZmPf5HpRi21ZeYngRF2c_6_Svdga38l9co9tVKBtYuDh5ZgkseegKj8LraGJXEITmpAidbrk0pv0_9uGIlgZbwJtA21ShhGtA3KsUvFI6xtYsepIPk8NKNPnrxzPQ-xJdrcSX_zEaux1oAuePXy89IgXikYhYusU8pZDyxBDvWVAH82LKqukqkqlbb_jhme4YCRtAE4ugRlBifouRBP9Y6VlXYJ7GbXu43SQ-s2mfNoQf4Z8b19W8tiSjz0Uf74evMT9SCUZwc3bJTqhHHIToQIdoVZCxBmj2akQP7T2yMA-mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=HV8mMZ4Th7RLJBNTsvMmuhUrcXy8r1_67xekg94kMnmVi_wbd3jnsaGiE6CHovR3Ecqn45ELtNMW189gLVEUVQnfb05_g2lkenMGi6jaDQAmTDLOSgkjWncp60LXhN-E3mBqZAWRoux1bM8er-y0vQrXzmg2Wz1fdu6ZkvX4rWJmnQsZQGBuCmMWqd9YmtMkHSAFsusxD2EUgDRqtlswy8_ncBGUNqD3g0yiIvUmF-hUCsB8U2dH0ky6cj3wXbJjILaZIbboCcYN0U7gb7unvifo4UDyP41oqyc1K_AJzNwh9a8f5trjpWcfa08H2xK7bqKXvA6CWo5m_FO_gxsbFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=HV8mMZ4Th7RLJBNTsvMmuhUrcXy8r1_67xekg94kMnmVi_wbd3jnsaGiE6CHovR3Ecqn45ELtNMW189gLVEUVQnfb05_g2lkenMGi6jaDQAmTDLOSgkjWncp60LXhN-E3mBqZAWRoux1bM8er-y0vQrXzmg2Wz1fdu6ZkvX4rWJmnQsZQGBuCmMWqd9YmtMkHSAFsusxD2EUgDRqtlswy8_ncBGUNqD3g0yiIvUmF-hUCsB8U2dH0ky6cj3wXbJjILaZIbboCcYN0U7gb7unvifo4UDyP41oqyc1K_AJzNwh9a8f5trjpWcfa08H2xK7bqKXvA6CWo5m_FO_gxsbFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=s86ds7aREcjqnxojlZ6Cw3coMpVK5m99H1NS2p7et-SVlZdzq3IWgD2mkiMH1c3TFEAUQen79pysC5dQRthyMNtjAnE4mF2JMzdpL0afbxKZk68bkHbxMG9v5sTmjhQPgZWGXHtScEaTIhNVcE1a7muOsqMDdLXxIViiE-tXTXrnxzbZmV99W60IYo6JvVytVNz_XXWi-NSISPI7VoMiwPF2iQgdsAngu8eSI-eP99LpKYGidSqkCYje6IXDgB_Wc9-gulq_11pmxqGt4Tg32YISrXgmOl40gpq7QJstknb1Gc85w7FKqrbdqu_gcjOpUMKgkNxL-WPSeMq1FHtDHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=s86ds7aREcjqnxojlZ6Cw3coMpVK5m99H1NS2p7et-SVlZdzq3IWgD2mkiMH1c3TFEAUQen79pysC5dQRthyMNtjAnE4mF2JMzdpL0afbxKZk68bkHbxMG9v5sTmjhQPgZWGXHtScEaTIhNVcE1a7muOsqMDdLXxIViiE-tXTXrnxzbZmV99W60IYo6JvVytVNz_XXWi-NSISPI7VoMiwPF2iQgdsAngu8eSI-eP99LpKYGidSqkCYje6IXDgB_Wc9-gulq_11pmxqGt4Tg32YISrXgmOl40gpq7QJstknb1Gc85w7FKqrbdqu_gcjOpUMKgkNxL-WPSeMq1FHtDHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=DQXEML3UyWk_pHjtP2GwmC8ocWjLZpLRL0BLkm-t9KhPpUIqzRzXQGSPeh3_K2nye6yKknu4nggYE4iCUuGGRVApAxzBnqYRX43fP67GovALDBLKs6begVbpPZD5PDrWUtH53HHD55DK9XNalk0BfSSoXR7FK5MkQkn0PjZe_Im-oqBntH279j43-kLHCde3JitMlFkCvy0erbmxexngnQubJ6a2L1qxOfAgI6vlGGwJSrXYGpZXWhZNxmP8oJ92sYoNs-ZN2-eJWKlWtsUBgnv4-KjTa8_dx9UmPjrX3KALbmWxp90MFcbe__nPwgy1rQAcACU5-uCFeveUcAspQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=DQXEML3UyWk_pHjtP2GwmC8ocWjLZpLRL0BLkm-t9KhPpUIqzRzXQGSPeh3_K2nye6yKknu4nggYE4iCUuGGRVApAxzBnqYRX43fP67GovALDBLKs6begVbpPZD5PDrWUtH53HHD55DK9XNalk0BfSSoXR7FK5MkQkn0PjZe_Im-oqBntH279j43-kLHCde3JitMlFkCvy0erbmxexngnQubJ6a2L1qxOfAgI6vlGGwJSrXYGpZXWhZNxmP8oJ92sYoNs-ZN2-eJWKlWtsUBgnv4-KjTa8_dx9UmPjrX3KALbmWxp90MFcbe__nPwgy1rQAcACU5-uCFeveUcAspQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xsyd4BYUbk1AQ52PZY36v4v3PxMIs638SwQEr_bsUIZ53Q4zh_TJN_xkFOA6cP6pY4iakx9EHFX3IW2c_veKVcXsXV_qHGea4rJsQz_LS_DmZFcSDZUHtfdaMm0xvuyiKTz3uzes1bPw--HpusZQ3zrL4Rchr8s5YJ5ndEvFcIa_9FveEBqLcNi7gefcz1yM3792U3frpsO_AoOUjvmEkoypz1_QgX5T6W1XZgrGMrPyxM_6rYgiMRaFpufmpIJTuDm12I9me77JxPWXU_jmXQhzxwUwQjXGoGutwbQYctwKzKEoQOKknVmDXUVhI8s_jONNXE8mPlS7PADql3_rew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q0y_-9UvwgUSOHSC7fdZMGFBaAGzK0FB6VchuaOv8AQOdrmnp7s6ieuWO3cMM-g7kOWvO6fAORasuFyUByG7Hc9DOlwRWqQRNdypHxqpCuM1obBhRjKvInbyTqret1YCvoEZCNYT1cEemrTAmncMmeAxKrjscWMTFII_IVU8-O-lCZ7HV_Sy_Ze8EVKCWdbuEosp7f8v4rvfADQK8z2PH-lCaALyQyFkMu6fjTueptAvN_YN49WSlU2Y5Xhm9COOtKVOBiIqP2rXNJTdkuBkPLNh2llH99Fv1s2AGBUu6efdD3aLag0KOvmqtKLtb3H6Bw4-W5kD7NL18eKLIWNOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIUPIrYeSvy1-WBCXfX_2uf8W8yPu0bpq7Kw1l4f0UJ_tH9kBOryRsnamzpWXgambMm0a6NMPYz_MJhzr0U2EHl4LT8ZcBQvL26_DNlHDrTqT84mwhgy2x6kiimLbEzEQ-thOvTAYs1IjEaUjjDIyVjSkEPemAwtKtbToFzReggaHNxjebb1iMM4v93kxMSMYLGArmSOW_AGK3nkHuz1KboVhpUWn0icFaH7A7DroRUCszpVmTELZbBh91wH215vCRgRNLQGh9TbysAXDu8Q5fGwTgOvF7JmR4S9b7TEo-Z3Ld9ka0xNr4zYBURvYxQ42P_lqu2JHMPfjrmZoAcr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DEuJLuvVt4lLNz1jl4YZ0TabSv4o0aafEzfGdUDPU7xF7d-WmlMFdV8LE9gbTFNyZGUdQL6jY-yUpxmclKgpEB062JT2FlDIcxpeAm2_fTP73Vo46jGJUffyGjB5N-23WgVMMTfP_a0gIcfFW2RsOwzV-A2iuiWCHcHKz21y2MLUip9tn4CPq0JHl8XKlAHIu8_mG7Dml1KnLomH_jnw2MAapwbh9TFynuLl7XreBg5vadA2CoQsDDZPgGl2pg5CD0-vLmghA3aOepU_xdNLwE6gm1KNxEpb8hZkxlvBuPWgcmXKAkMi0ddFI9LyblRisF-RrjieR6LrQu-tyhtI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2fPp6CeswM5sq1T9vwMynmrFWJBQdkRNbvuRIjJfB1v-4vRELfBpW-ePAdiM1e1agqnUtENmrTmcd3BoBAqmKw6Ut6EzuMgt5jQ7zYUnltf82mkhM2FEB6wrfASve67Tndc7QeoGITkhuNG5cNRBW9KdqA-WzuQTV3WMfq-MV6wT2PC_khI0_WKyTg_NP2hHQD1FXTo9U8ksE4WDQ7yy29QnKJDf_ITZldBYxQ7ZREHmG4hyofU54X2hc63_eCRuzMRBKIzOiIG0OidrSuCD5H9PGc4fKYsDvrMhh6K7UDwBd-NMjWctQ57qT5Jg_5DG5yEckYaCCKF7V4MDWWdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEIKCgrNgTzRawgFek1SBeY5bnqUCviL53fwBPTmA8Xr6fWxyCqAXrYbus43fZJFdkpN_55NwIJUxXWpVMwHLMuKKxqk48BxvP0haJRo9nxbttqPw1Wx7mQPwhqj8Dp-smLIrKy1tce1Uhu4TZuJUzJhJIRQaFxExPD9kULj0UvTBnENQuJSZg1SGul3T_A-xbvKlTaKAR-KjN2-bhh9E_Lp6xOlLysfhJl-tdEjwnkgYw14kr1hSEUcGt5hRFWhX0xCp8feRpx3DatSZJe3I1zyilgFyx3Jhy1xRde-JUB2W1h_pMLwbaXBrFZ5VOtqTmWQeoSdDMP9M21GaHVA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIbQOxuwnDXPZNqE42I6Q59IhFkfTbl-_qZWp3mwZpT5JiimLN7MhlH15_kT_vLsZzE67swDUs7Otbig0MgOiTIP9kHS0_t1f6M0Xg54yUEcCt935dd6gwkX0UcjB0USHEByaTsNxWd_2n_0DfCulrCq35z4OLqMn_3ATlVFvgNrU7yxE7-58uR2vLDvSCh6kuy9-ek2cHpHPfNRE5Zs9yRQWOjVUzrDLWZEy7AwDIJOXwnKwjUNnzchIcIGxFygV7Qlu3wdLq9lJs47sx1Gsb8MGe6mLGaQVXosRV-FNgmVrIKnuYWTrnHiOy8-nXiQXEoAYMhQNmlJFikBU4VUCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u58iF7DPwE1Dn-6XH4ZeU5KGcsmM20mNWFusMzwqaVzgbcQJpKFhjoiFu-fXszZSMQSRWC-8E7jNt2XV9RnAgX78ky3ufN9PG-X2zCKCOmJDVcp53i_8uihHGwTSRdo9i3PmLayL-DH9Xu1xUZl02X32yovN8zyr1C6ynXv-clh0x1d-cCGkJjannCkdh03yNFUFfUKZFPRmhkGgWV6_T5JbCMpS2SxeMY1avKsDCOERaczmHBMSlmNG3nHdQxLZymgjdkXdxK0Ck01ReGy4DjXNX2AQXFwrRNz7a6uWrBNroFtLzx-kbzpa1Gs0QpIDb2BMuPHHgRZ7FB7qspsOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYIgXpfsKR1jA57NrZtIO-aNrcOLxyni8qJA1Tk3RA_sjFNxc9Gdg79XSo1vnjeMdme_4y8cGdK9IeTBb3oOXjDrO-NJbf7pWTvr3TJlZuY7Pht6qIgdKYJuJeIiREa1OIzUItRvc_sr0QBoHd5LP3Re61b4iIejeis3IeymYPWvIY_ogD7-cOudP2EQDXcrsemA4lTYwspVjVPKfzZQhxktJhbOSUoy7K_oRRgfVZDSz-MUgcLkhkgik4Vuhn_GW1VN86H0-xqLPkjwhlpDGvp0jLk8Zo2ZfZL7_I60F0OKQPnCfPEEo17MUzwe5btTPW6v5Cde-R0hjclDSUJTJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=USDyhYuTryL-wK9fxW7I8GS9u7OhYW8lfdEdgPWvAOLjQ1BUby4xGPJuHCrLaeFtsqTDbjzJH5H74qrubjo_RAfEr9aw2cOzhUbZOfZGokNg7EYo1tjXWEU-QJPbSEChYv9cTkMI4PkyEpJ1U-OwVSUXyPF7ZOoTvi60kG79yufxrX1XtHz2pVtM0ykqNGZlzdfrnOUXAF3M6guk0zoMJlHnTSdCZTVhAHIAglqnlPW9GM5MGofRtmLcq4auD9gKVjEPBST_0LQchCBNZwNHnwlGf-alUPkx5mR2-Q397XGQgkIPnRPB7IMbv5TLIwLNWuV21-dR4fVxtyAuC3gyOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=USDyhYuTryL-wK9fxW7I8GS9u7OhYW8lfdEdgPWvAOLjQ1BUby4xGPJuHCrLaeFtsqTDbjzJH5H74qrubjo_RAfEr9aw2cOzhUbZOfZGokNg7EYo1tjXWEU-QJPbSEChYv9cTkMI4PkyEpJ1U-OwVSUXyPF7ZOoTvi60kG79yufxrX1XtHz2pVtM0ykqNGZlzdfrnOUXAF3M6guk0zoMJlHnTSdCZTVhAHIAglqnlPW9GM5MGofRtmLcq4auD9gKVjEPBST_0LQchCBNZwNHnwlGf-alUPkx5mR2-Q397XGQgkIPnRPB7IMbv5TLIwLNWuV21-dR4fVxtyAuC3gyOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOR1ZpKJaIGOYMilk1Kw58zFUZ_aXYjGsSdl4NHy60ImfQueBv78lpv-w6RNom99rBs0-Y6928bD6ejjZJJ6dno2LgRiyXHsW5AyYLwEzAOmYfwBEZ-T-PvyLaHg8z9dOBJPOWulozeMnATvtjcL5SNG7mPE1LbsNXOnWgdFdMTapsWxXYo9DEnJQlWtQUSNMMl7bHNNKFEIPkeqqOKjpC2ZSKVWKYC83VdPOfA8aQmH7a1F2zuks34c9-IZadfvlBslM5AmUf7ESFK7hVYertYrNJr-rRCAcJ14y-zeAR6Hu9Yz_14FLsWUju2ojpu2pSnseRnaQrgHB_-4VDpjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ql0nELAmoe7n_YhfI6sSZfgnoR8F607Wq4YdRTPHfYvbnVnVtqcFoObtK6kp_jR0YR9CxZ-SCltBcPQ4vPb1Ke9I6OXPR0Thuyn4UQ5R8cAi8URuxBANYABVmdu01I9_jkpBuNWOk3RLT6YbsPNNpfYWg1KnxGl8P9HX9kngW1XqRjoa0rM9SDy3_rW1QI6yEsRGCXj_FH4iUmstAaNDg_I3WZclm5Wm46323mSrGumXpgSm3FdCaSxa-40zCPJvOA5ni9QEg0j8fOOGw4K99Ut_es67PLmqSbMxTUKvO5cuf_NFMqipRBY6iRz7likFVIIl-stdnOPDgVpn9FYYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSqTbQKrTqi4wVIj7R9o7xjlVc5l1Z74jGDxxeyeFmOtplSGpRnQhWHAWWwN1PTZcr5Ckz4-3j9qI_D4Ba6o97SfGljehuOizJjwlprla6rdHNwMmvk3zaCtovuMQDMqr89hvE05cPG1I4XKC_T-y0ORKcNGO_bGmB7z7D1oRD5icl6ivgxAV3N73BAXZhlZFPKjC3iZUJCe8u974UCGcUxzWPYXUilJEWt9xT2hUUBqW-Cx_w8MsrDWT-zvYrTlfcpIrqVQpB9UBm8pKHF4q8xx_jth2XcrBqHI7mz9iJpry5DyIezSREUiygOTls-Ry84dbpqBHZ6e7ooH_FVvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZT6cUilIaH3TtmQIw0psJNfFAChzMdo6L_iTDOxy9Z_ItIo-5ZkUzi1nSpKr4VDesdygULvcuzBbBDtZ5u1AzZkwjcQPaRNDEi9oGYivYYavnQCLKqRo0fvD_UXzOiO9t2SufsZ7ZWZ6N9jnru7eo_TTD74oQ2hx1wpag8QVkf8t_6euICppuLBYo7SF1hdZAW5xQ99H7UP2QAV9ezwD06HW02gvIOKxYGCR1ieilyjPzhJv7VpCqJzDLIvDi4AdpqjOvPSfvIP-II2n7NPC4CF6MougnFaw-Zy8VK9Q4cV5ytDo6PGjkJlSetlWJoy8A3tDVDr_ugmbyH_qo0YiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=U-VBjFKotR_-PVIZj9M4v5dwfamPQyz1_xCFjj9sRxY_azgkMzoLbdxzSW-LFo5eLYBcNRkkthcQ0u9yWoLI2IEWp_G_mHnKSknewL9jw4NQDfOAnJDpV_DyLJZFUyN-uQBirSQcstXegeBBta2gTmqr-9KgJkxkIb3djIh2EUueAxvDuDHCiK4VhgSQK3LH6ihqna9gQ6J6qYzIRx_yYvU3Ia40xP_3--OEAoRmISKkhlOKVcaO5eOY15y55Y56PWC892az0TuM3WBSlUygw3tGxZ02i6oHmCrwDer1nfVCFtNX4eLJffOfCKDok3ni0D6zwYomeky3jEFOEUN-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=U-VBjFKotR_-PVIZj9M4v5dwfamPQyz1_xCFjj9sRxY_azgkMzoLbdxzSW-LFo5eLYBcNRkkthcQ0u9yWoLI2IEWp_G_mHnKSknewL9jw4NQDfOAnJDpV_DyLJZFUyN-uQBirSQcstXegeBBta2gTmqr-9KgJkxkIb3djIh2EUueAxvDuDHCiK4VhgSQK3LH6ihqna9gQ6J6qYzIRx_yYvU3Ia40xP_3--OEAoRmISKkhlOKVcaO5eOY15y55Y56PWC892az0TuM3WBSlUygw3tGxZ02i6oHmCrwDer1nfVCFtNX4eLJffOfCKDok3ni0D6zwYomeky3jEFOEUN-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wk7LX_B-AAwTEmnyTpm8HKeZjICWaZaAiF_jttJFTKTX94uzYMgSZivTXw1ZIY1iMe4MYzjyUQdua-7X9mQ4q-A3U3zgxAKktwyweFkIHXCOOR3T-dj4fcRNc-djVd7QShJlzz8_W5SSvWX-J82frr5g3AvvXkIivDhqsrUkQJncAX1Qg5_J5lgPG8bIZZeF9-vE6VCeR4hckHugsi1Ede41ROqOUkRDfPWnKNYyVa1Fqf_yAXq-jvdWIBP-SonSYHIkSDnf_DR5reMAtjJ7ZMT9ixyIGzF5s7kYSDMGmqQpZ-vC0sgTmE8C4uGjrCTTggMOAkwE1hMC7pNWJsyK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
