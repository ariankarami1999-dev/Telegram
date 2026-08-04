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
<img src="https://cdn4.telesco.pe/file/IAp0lxosLpzmXajifemzV0lrtYevhYkhQGChPvGRd57HMR6sMQyEfKw3DXyE_S3eZGf0Va4qqSIMv7NP-K8-C3ow_sT935BmghzcPtOE55Z3s4SOcXu7P7n1KufUFDmso8R3xzeWRIMcrqcRpAogN96pIKtsuKjPNtk47E45V1xMJz1uaS6BOUacuqHHSBeBRk1JjtC0HE2tcC7epAZGccZm86GOB-D1YMgnrIQdtjBNefKpek94QydNrHhYxhfu5jnGkGUYud-AIqdJ7zv6bjO2a4BJmesqIleKW24frv_jl8vD7-XK3ZdAzon2yb3Eh4wZfl3mTtmfLUdw1jPJKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 135K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 19:37:34</div>
<hr>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=udYjkV5Q73nj2KLGQkgW5rKbuOfTEUojatsUKgNDDUH92ow0ekeyFdZZaYd4t1Au86sCjaM4pLVbuYPCKmiX72B769ICS9RO9h9sCdsAA4yxrSxxuIrEIShAf3FnZimlBLJLEr1c2nKDscBjE0wrS6ko-aPOQmmhSCtznb5FjtLEuuYBvvpLI3pBi7v5NH2Uzd2UkQlt4IG-PiQs-Ae5HF3nrUIVh7yial8Qfd-Wto4yYHzAB1PzOSdI6vI1UoEwa3nN6R5yHE5dGMNSLxUOCbme9pL6bUocrzV7GAQwFlZFAEdAeuSo4BHXQwQh-NSEyTfmmT0rV-9YgJqsX0lBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=udYjkV5Q73nj2KLGQkgW5rKbuOfTEUojatsUKgNDDUH92ow0ekeyFdZZaYd4t1Au86sCjaM4pLVbuYPCKmiX72B769ICS9RO9h9sCdsAA4yxrSxxuIrEIShAf3FnZimlBLJLEr1c2nKDscBjE0wrS6ko-aPOQmmhSCtznb5FjtLEuuYBvvpLI3pBi7v5NH2Uzd2UkQlt4IG-PiQs-Ae5HF3nrUIVh7yial8Qfd-Wto4yYHzAB1PzOSdI6vI1UoEwa3nN6R5yHE5dGMNSLxUOCbme9pL6bUocrzV7GAQwFlZFAEdAeuSo4BHXQwQh-NSEyTfmmT0rV-9YgJqsX0lBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
غنی‌سازی اورانیوم چطور انجام میشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj4oWJGfuT3lgY1BMLeyLdpNMPs5QMtrXd4uBoPBhfwGjCBjSvnkG55J3aAmxl5RRsp5LNeIHDvn_xliiC2DxmeTcTdhKlnllQ-3myQ1fPkhGEm2sSUMe-9yDn2s7hsxlDpzxGo2arzcCCOaQQisZIjL5W_JmAiZ5ALJ6pRbReOdGUmsbcCGkfFcJ8U7xdrM36D5gOahXXxhTjo41xRE_8rsUMcwzG-OZhF-5UR6sp4BWQ7shCwHtR1ZYiJ4dcmk4UE4pH_viYuGXm6HTcA9qYmg-csagYen7TTBQC-kUz4_CpCSd1MFobLqGH93jf_lzdG8Mk2pvEvenitPJbbErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=JpSG7mXjcGPV-kL5ijjm7Kvk4SBl0egzQx4zFsO6QqpO9Jnda8ydHlvZXC6BnVpwDu2qVlyZpsPxmkkrgs0gWtdxDLeDcNndcUth9T1lAChW8ts8LolIFPrxRHnIodSXhcZYVMZmEUvzIzvS_ED6wXU2hsHrHPEU3cO6mW1pA0pLQqi2CY5Qrpbqlh3HsEdDKbCBRwzKnLuawOjL1PnM-TuT_eJXTqCKEqyOruRR2H3mEF5eCiAzqwuCYz57msE5hd6vQnpvNxd-WtuJe4R-eZUbmJLi_kZ6jcAi0oN-TLNnzsewqv0H9aV3OrRAxPNCWrqVvT-GS1Anb9sVnbLZjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=JpSG7mXjcGPV-kL5ijjm7Kvk4SBl0egzQx4zFsO6QqpO9Jnda8ydHlvZXC6BnVpwDu2qVlyZpsPxmkkrgs0gWtdxDLeDcNndcUth9T1lAChW8ts8LolIFPrxRHnIodSXhcZYVMZmEUvzIzvS_ED6wXU2hsHrHPEU3cO6mW1pA0pLQqi2CY5Qrpbqlh3HsEdDKbCBRwzKnLuawOjL1PnM-TuT_eJXTqCKEqyOruRR2H3mEF5eCiAzqwuCYz57msE5hd6vQnpvNxd-WtuJe4R-eZUbmJLi_kZ6jcAi0oN-TLNnzsewqv0H9aV3OrRAxPNCWrqVvT-GS1Anb9sVnbLZjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:
کشتی‌هایی در حال عبور از تنگه هستند.
هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است.
تنگه باز است.
ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت و هم‌زمان با حرکت به سوی مذاکرات بلندمدت‌تر پیرامون خلع سلاح هسته‌ای، امکان عبور ایمن تعداد بیشتری از کشتی‌ها از تنگه هرمز را فراهم کنیم.
در مذاکرات برای بازگشایی تنگه پیشرفت‌هایی حاصل شده، اما هنوز توافق نهایی صورت نگرفته است.
ما امیدواریم که این توافق به‌زودی نهایی شود
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=ZGGgM-bfV7htQPE3RC4nuhPHIEVDepCabgepZp5RYX07Y90mfwzunpuhR2mxE-t4I5XL0drbPMXAYPScPxDbbeicu51F4GSqn6Wzb6QiehgAYyNVO2mv8qfBXm6ZI7_FxvUtdgTS11gQuG2bDrhapnk_WW-E3rAr5iboAIWMEQaVSXVs9vZQWcM2QeYjT5fVW1q7dzMyzFnh88GPulRUw-plBle3n7PE7z4Iauie_jG2XKmDrGJi6zbjKSkbfXW4X7dXmh2-0YOvHomWteD8FZF1pA1DOo_YcRgbvWZXSxWcorB7j2TYBdkSoBhwPCgEUWiY2mwkvUXIbYKbq-gdqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=ZGGgM-bfV7htQPE3RC4nuhPHIEVDepCabgepZp5RYX07Y90mfwzunpuhR2mxE-t4I5XL0drbPMXAYPScPxDbbeicu51F4GSqn6Wzb6QiehgAYyNVO2mv8qfBXm6ZI7_FxvUtdgTS11gQuG2bDrhapnk_WW-E3rAr5iboAIWMEQaVSXVs9vZQWcM2QeYjT5fVW1q7dzMyzFnh88GPulRUw-plBle3n7PE7z4Iauie_jG2XKmDrGJi6zbjKSkbfXW4X7dXmh2-0YOvHomWteD8FZF1pA1DOo_YcRgbvWZXSxWcorB7j2TYBdkSoBhwPCgEUWiY2mwkvUXIbYKbq-gdqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو پاکستان، یه تجمع ضد جنگ برگزار شده بود که وسطش یه گروه جنگی اومدن انتحاری زدن در رفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoLNxFjeTX0C1tbLnrdSFINayZ_ZZtb_95QG1_M1qOg-w60eisyV6mhV3v3C-YQJvl1KS1bctFzTCRlYi7IJKVmuaENoWjj6Zuyec5__VxC5m3m8p-ZxGuNFsaa3lrYQPyWRtG3pqwsRoBFqnces_7QzyLYTyw1iSO8tDU0527qUxB3EX3iAIZoFqI36bT-_Zz1YCywmrYgy2f2_xVYHnHk3UNrkH-xsR54wf29CrhEiRcEEAqEoIdvUm1-p9x0mb0GS0slxIdEsWRGXy_lMJ27JuIJiYrfFkbsbCMzSlq37b2AqIf5kN62pLdKfrURB4hnihJ_76UZ7Evw5gLI-fV7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoLNxFjeTX0C1tbLnrdSFINayZ_ZZtb_95QG1_M1qOg-w60eisyV6mhV3v3C-YQJvl1KS1bctFzTCRlYi7IJKVmuaENoWjj6Zuyec5__VxC5m3m8p-ZxGuNFsaa3lrYQPyWRtG3pqwsRoBFqnces_7QzyLYTyw1iSO8tDU0527qUxB3EX3iAIZoFqI36bT-_Zz1YCywmrYgy2f2_xVYHnHk3UNrkH-xsR54wf29CrhEiRcEEAqEoIdvUm1-p9x0mb0GS0slxIdEsWRGXy_lMJ27JuIJiYrfFkbsbCMzSlq37b2AqIf5kN62pLdKfrURB4hnihJ_76UZ7Evw5gLI-fV7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=e2DZR1gISX9m_ZUjeH7sz3ugPakAYt-vdsNrws2x0dNiKy9pORgKyxS39FPfrbqj3WMQa41sMsujtdeLfvlcAy_L_lMr8z3FVIdHCzdJBq5iBs0meAwlUpeoXrjvLYX0ZEDWrVFNJrYJBCUFNszEnCBRfqg0xAIps2f02Glg9btGJgxgrZub-WXFI7BbF9H_hL9sNZlOSBZn25Frb_IawuSBoczcZxkAfBizR3NL9sKQuKOmlQz7EGuUKSCFBd7Mx6CBTIwXE_FdDhHnruDST23WAaaOuffcPIcsO6kTsZFXacJiaXdtjTHlVR6whHzxFhi3vXSji71WwLXmAhs5Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=e2DZR1gISX9m_ZUjeH7sz3ugPakAYt-vdsNrws2x0dNiKy9pORgKyxS39FPfrbqj3WMQa41sMsujtdeLfvlcAy_L_lMr8z3FVIdHCzdJBq5iBs0meAwlUpeoXrjvLYX0ZEDWrVFNJrYJBCUFNszEnCBRfqg0xAIps2f02Glg9btGJgxgrZub-WXFI7BbF9H_hL9sNZlOSBZn25Frb_IawuSBoczcZxkAfBizR3NL9sKQuKOmlQz7EGuUKSCFBd7Mx6CBTIwXE_FdDhHnruDST23WAaaOuffcPIcsO6kTsZFXacJiaXdtjTHlVR6whHzxFhi3vXSji71WwLXmAhs5Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=LHH6ynFz_ilf12iVJya2kV8dwPjiR9GgKyCUspzU0A_PQr7Q62xSwxo-u3mURa-on_91k1R1GsB3fRJyC1VYysoJFRXQfDLHHtlMwev7GQ-9XvGuWyWV2wziI7Qp1gMDdCOVqxO9hA9eL2NWMiHk82kqYrIFP-G7zm98XzS5YixufwxiqMuhlRwZKzXigJ8hGbOCO1JPyQMmbDJv4zibpmrUCduDxj5iru73ulHZaaRPzR1D0brVAMmJ6jGv9YaN2xWxXYKFiODtVd6iK-az9AiHJQwIgJjjESl4aoPTXD8mtWmZGh1FTIKx7R0RJ1dESk4qxCKO4X8uOA1IeSDU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=LHH6ynFz_ilf12iVJya2kV8dwPjiR9GgKyCUspzU0A_PQr7Q62xSwxo-u3mURa-on_91k1R1GsB3fRJyC1VYysoJFRXQfDLHHtlMwev7GQ-9XvGuWyWV2wziI7Qp1gMDdCOVqxO9hA9eL2NWMiHk82kqYrIFP-G7zm98XzS5YixufwxiqMuhlRwZKzXigJ8hGbOCO1JPyQMmbDJv4zibpmrUCduDxj5iru73ulHZaaRPzR1D0brVAMmJ6jGv9YaN2xWxXYKFiODtVd6iK-az9AiHJQwIgJjjESl4aoPTXD8mtWmZGh1FTIKx7R0RJ1dESk4qxCKO4X8uOA1IeSDU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqaPPRCVQtksZkDyjCQdbkCJ15gKpF5yC7JuQjgCy20Z8hwHPnSpMkBNzfHhzwc0RTb8DPRb1kpy3IZaQ9BfmvHhqjr9QLIJYJv3Y_lRO1pwd22OznSjO021CvnNPg4Xu0TNRzIH22oJAF2PzqJPXtSMCJkNIsXUUdEKgaQYazrEvNhXro97TzpdBL9WEMnfP6EegScJOXJL501FnGY7ZiSyYhtBrcRVeVizcJAcGrU6p7Bh7Tmifkb2vypPb9FZuk2XOsueZTNYD2DzVv1HKPFXns0-MOfqrCZQUiqHes_IE7BGszhn5ogdEYntnqqFzGR82jYwOt5oAxKMKXDVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇺🇸
🇶🇦
🇮🇷
سخنگوی وزارت خارجه قطر:
تلاش‌ها برای دستیابی به یک راه‌حل کوتاه‌مدت میان ایالات متحده و ایران در جریان است و متن توافق احتمالی نیز تدوین شده است.
این پیش‌نویس هم‌اکنون میان طرفین در حال تبادل و بررسی است، اما هنوز دستور کار مشخصی برای مذاکرات مستقیم میان آمریکا و ایران تعیین نشده است.
تمرکز دیپلماتیکِ فوری، حل‌وفصل تمام اختلافات عمده نیست، بلکه هدف، دستیابی به کاهش تنش در کوتاه‌مدت است که بتواند راه را برای ازسرگیری مذاکرات هموار سازد.
برای بازارها، این تحول سیگنالی مثبت محسوب می‌شود؛ چرا که هرگونه توافقی می‌تواند خطر تشدید درگیری‌های نظامی را کاهش دهد، از تنش‌ها در تنگه هرمز بکاهد و فشار بر بازار نفت را تعدیل کند.
با این حال، همچنان باید جانب احتیاط را رعایت کرد: اگرچه پیش‌نویسی وجود دارد، اما هنوز مشخص نیست که آیا واشنگتن و تهران هر دو آن را خواهند پذیرفت یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muHoVZRUBudVyvw88WLl0GGfQEDMM3W-0bbIr6W3h9HBT5tRtUSE16gqMS7tLK0E9uqAvHX561_Z48gpjDwm0wbLRrdOdYZQTRlWy58-aH7F-h--5-NNYRsrVOsnzA_2JlVFh3jxJNZ-vQLrE_Amvl509rEjRkM_Q7W_a4TvJzU3zJPqPdzKkcXVds4UCWWjuCPtSutDMWf200EOHSem4_l8j7y1XF2Xpdxgb0SnB6n9iqKsOVzuV7ViHO07aQqNg6AnORwGVRD7M92eDeUNqMgQURGDr17l94eaIpSyQyb7Wgpk7jaWvv4KFZ0OMexotlRatiz6Ugr4b4WaRzXN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=rG04TriBqzoKWTf3jQieAQwSnnfSBVC5y9AAMt0dxWAHYzkNplfylTMM1YdmDgGZu0Af3ry7jPkQLczXOgF4RVeTKaEMXLMSSI-_SNMp7_0_MPhVrpimSbo_ogOX0JNn7bIFudeHWZN62zAcqqZ0AbkqKzxC-8UPLISTKM4x1sdY1c4GUdRxRFOs6xgSSE3RT3hVnXMg_BDWD6POwLSJDxWN76roZib_j8CjiLiZHqy8pPWz2MfT-QLkUfUnyPZ90tz0VptaLYmylEA52Xom47hM374ETVh-DpQpAFnp8FiwTYGhyYNGjqNr0vvTdQZu0gO22dXJgwjTxQp8bzzsmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=rG04TriBqzoKWTf3jQieAQwSnnfSBVC5y9AAMt0dxWAHYzkNplfylTMM1YdmDgGZu0Af3ry7jPkQLczXOgF4RVeTKaEMXLMSSI-_SNMp7_0_MPhVrpimSbo_ogOX0JNn7bIFudeHWZN62zAcqqZ0AbkqKzxC-8UPLISTKM4x1sdY1c4GUdRxRFOs6xgSSE3RT3hVnXMg_BDWD6POwLSJDxWN76roZib_j8CjiLiZHqy8pPWz2MfT-QLkUfUnyPZ90tz0VptaLYmylEA52Xom47hM374ETVh-DpQpAFnp8FiwTYGhyYNGjqNr0vvTdQZu0gO22dXJgwjTxQp8bzzsmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JssHPkVxuAnollLjV1VAcLzXGKWKkL2lZXXF7uDmqjG0oO6dcJUTwYg6VpbYpVIGiAfCG1wbqngC1Hy60trc3unY4ZHIW8CHXMgqHoj3asRDa8bcCoQlHh6trwAsYgEuldF4ldnT9xonEqVlIbfCUGLHlDXnqzPhM0VqwSp5_9tAtOA8w736TJt7uRXW5bHcz8BdG2DNZC9qHqkRMyfwFe7yCTYg1983xm1l7fwSbzEzSdqYVDwjmut4THX3E-dUVQ_uiYeeGxq3VhjJD2CR68mTaRvti06HjceCU6IDi3_0LXiiXizUtQSE-jsoJUKWJs6HSNjJ3vi_fiA0zqHYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-Ye0xTsyem0JczH7hw1FQvsAG_LGJwB8sC0HkKIXAHQnWh0qWM8qskqzm47iLrNSb-x-HTNb1XeJgJEfselW189fYSrKARMCNIwvjSdJ6B3sPmT3AQU7y7WtUB-nbVJ1A4gtdBoYVfpoOWpt4-5CyfmSfVorhfa4_JOlTDvIvtj4FUZ9UeS3PnYrgyLmwBwED-Scdo3vqMNQWJe7SGETig6Jf0me7u0knEYN9xKwHlMtsMIfESfzuKSOPN0TxI7kOyo382qbu1NOG1tcKmAFhfT8aaKsPrqYLTkujdXnaXiOMkmoWXibjaw8gsBngfzxXDDzbxEVWf9PNhg6V0b0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jApOcgs5F77Bf7bG5mD-pwJUfTnEHfOU06jm55lhl-oal36ydcS9o0jb9lNm7uuXDuTmZsi7-RKPZas2xrh1ebpGuRGKN2CNf23ivEi_bLx3Cf8tEeGKgJofk9YaaGGiFVkLhvhP44hiYkBM1bbKSh6-NUQZxfm_mYFXH2pPa331jSgvdeWXLSIpBhaRXz1B-0FIcFG94u0Q35BgfIISk0jPx1y2fINc-X4N0opadSyx_9H2RpB-fqKbCAw9NbwJ57tcfTZ98rJntTlhqC469ebBg9wYlWu_e_dPyElLY-HJEyP6XLmpExNNPoZLzrAy3HVMVJVm7oapzxiGEohH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dl-_HK9eR2rLMPKrKgP5Dq1Bqpv8g4xUVz7sTk3aaHvDMzq_flTyGMCqmyYxXUKODeMfjz-5-JVaumjuckzy4HU7tIjyED75U2lRBmR1rvgJVIkYAz56ZD5BPF8vyS1lWC-k4hMnNyjk_OgC1O3qm4iJmvHjhbJSU5WMCh8D142QU5XtBTm5Hv7u6hhrBoI8WkkBxu2c1MP0Ii8WZBI38vDfjpkTu_Wbyp4UOPHujsqPH7Jrp9ci83tDmHFHmMrZ8Jt9WhQ6LOhdcVfdvyTIE3vzFZISpZOssz5ZpGCEpqFRScoEvWpEGMTZuar5LxuMeXCcUcnhrCBzDCGNiob0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISZVKAc1Jjeqp6SmYE5IcBQ0AnLG1dgnUOBJmpJKD-TnOYAcxzwk0qRhsTF1X2tTgUfHAyfG4TkrdDCeD6MmprTm5Hzk940uijLzFCQi7U62sUKXwESj_vAMURsGUW5I_oLUi_7KLaIDS-1JJleRnT-SQ1JtbH65W1MqNYh7VCpKLaTC0bdhHs0siyA_SD-gjtfi3hk3fYrqDp4FiufyJaOcwQvwoMpVVz0VMdJq9QqDyO-GHEg11LQs-LPcMvpf-st_F3XOfdSd42dAiJ1oF6w2IpLmmpm75XF6CU1g8FfellOLaZmssda5_0TcIwBk7kYAOkQwFcNSD3mcoZJUqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=rW7i--O30wOSQFPMHYlApbc6meY7XNHqAQjbsUVRThHwOPq1dKWb9QDvdNFN8Pq1G1nnuJCy4nyVjx7Yus9jLdXYNjHh2vaM7u_42l2jF6PBjHLw-4ZtN2Njn4GfXdnNYC8G_ciHrARtADVAebJMs58RTyQRmPMLWuZSPSh9c87o07xm8nQ1xONQq5i1cFNVWCGRum0-hvtMZJSWDpZ0bvBgL8y4bUwNqqCxvm0Skh6O9wTi2Xd7zcqjbwPt1D9WMpEO3-t7DmucXj3VIeZ0UCirGWrzyDLNzxIEm7nvXBNmFXZtczSlt__ihBTmKDl_hrk7TeX8fWq8IErYOgHHEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=rW7i--O30wOSQFPMHYlApbc6meY7XNHqAQjbsUVRThHwOPq1dKWb9QDvdNFN8Pq1G1nnuJCy4nyVjx7Yus9jLdXYNjHh2vaM7u_42l2jF6PBjHLw-4ZtN2Njn4GfXdnNYC8G_ciHrARtADVAebJMs58RTyQRmPMLWuZSPSh9c87o07xm8nQ1xONQq5i1cFNVWCGRum0-hvtMZJSWDpZ0bvBgL8y4bUwNqqCxvm0Skh6O9wTi2Xd7zcqjbwPt1D9WMpEO3-t7DmucXj3VIeZ0UCirGWrzyDLNzxIEm7nvXBNmFXZtczSlt__ihBTmKDl_hrk7TeX8fWq8IErYOgHHEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=BqD7fjJVbxIXL1yDcnjNomvl7o0DzHi6j6meAoXmhWq6gZt0EDoWCFzb6rlTYq0waqs4TORqrCeysBYpnIU5Z56-gjCaZpvBg83zEFmpkgwMW-GMWJ7ZMa0OWzgS0B7BSj_Q7HOxq5l60FzpLuPH8lz0lQE5jA181NZWq7O9gT_JAarvN6udfGeQBiANWtd6gFmW8ZiJVoh0H1xK9OfotMyqYpCV-xYmHSm00qIMHHsVycBVbG77wm_IzRicmg_4iib5P3URohs7i_6mvPZyXrG9DfRh7Rswk1NfkkwCO9CQx4QXvM5rInFcsZ2E2DbmtC93UIFvw23fBZ5bqpYfkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=BqD7fjJVbxIXL1yDcnjNomvl7o0DzHi6j6meAoXmhWq6gZt0EDoWCFzb6rlTYq0waqs4TORqrCeysBYpnIU5Z56-gjCaZpvBg83zEFmpkgwMW-GMWJ7ZMa0OWzgS0B7BSj_Q7HOxq5l60FzpLuPH8lz0lQE5jA181NZWq7O9gT_JAarvN6udfGeQBiANWtd6gFmW8ZiJVoh0H1xK9OfotMyqYpCV-xYmHSm00qIMHHsVycBVbG77wm_IzRicmg_4iib5P3URohs7i_6mvPZyXrG9DfRh7Rswk1NfkkwCO9CQx4QXvM5rInFcsZ2E2DbmtC93UIFvw23fBZ5bqpYfkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=WRo13lpnP820ozHwxQhZorBz7P9RH3bM3OqdbrEYqWbO3twr3mLfv4ju4uYImchCsYTgqUfWklmlAzybkp2boDdMQlGrIfcWuqvbgQH3oHvngr5oIOzNhPZrb8amQc986DKtcEdKiGAlPQVs62guw8wfMuRUShkwO63faKYgyv4Hu1Kd4ngbqcgqg8zx1bUF65GngDi2EZ8clWR0al4xSNhrXHbSZbaryRRuXC1d94fVEfQcI3r92WMAL_cWYAG37ebL97h7tij_KXLaoo75BcW9oRZpysn770ONdF_dEDnZiSLWSpnrbU5PIisjr1zpChncC18zpnwQ_CEXhl9SxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=WRo13lpnP820ozHwxQhZorBz7P9RH3bM3OqdbrEYqWbO3twr3mLfv4ju4uYImchCsYTgqUfWklmlAzybkp2boDdMQlGrIfcWuqvbgQH3oHvngr5oIOzNhPZrb8amQc986DKtcEdKiGAlPQVs62guw8wfMuRUShkwO63faKYgyv4Hu1Kd4ngbqcgqg8zx1bUF65GngDi2EZ8clWR0al4xSNhrXHbSZbaryRRuXC1d94fVEfQcI3r92WMAL_cWYAG37ebL97h7tij_KXLaoo75BcW9oRZpysn770ONdF_dEDnZiSLWSpnrbU5PIisjr1zpChncC18zpnwQ_CEXhl9SxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuworvOLOqMd0dFQeiQk5DYDSa8C6VWrsAm3_AF6q-h5pQdLdvg3lGQgkO0K2KK191jwY0wDnpZDrU_pRJJ_HbsxRkcDWXvsWLPbhOT_3ndJz1Or2_SE6UtDrmfq1objqc9jQ97s4Ny6aQLkcmT0HIJ2WXH43PGMz9NsReGL9D8ia_GNtWPq5jIqbVz0S0BfKvb5b95tnS8Pd1173trSRi5ZC4FNnula_OfZtN21weT9URI1ap52_8YCnczo1RFttk7P_BweYlJo7qbkmwW5k0h_pINxMglP5WNHC-jsh6hrnaJd2wPu6ns0532H1aOQu8ImRZftP5jKCR0d2dy583Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuworvOLOqMd0dFQeiQk5DYDSa8C6VWrsAm3_AF6q-h5pQdLdvg3lGQgkO0K2KK191jwY0wDnpZDrU_pRJJ_HbsxRkcDWXvsWLPbhOT_3ndJz1Or2_SE6UtDrmfq1objqc9jQ97s4Ny6aQLkcmT0HIJ2WXH43PGMz9NsReGL9D8ia_GNtWPq5jIqbVz0S0BfKvb5b95tnS8Pd1173trSRi5ZC4FNnula_OfZtN21weT9URI1ap52_8YCnczo1RFttk7P_BweYlJo7qbkmwW5k0h_pINxMglP5WNHC-jsh6hrnaJd2wPu6ns0532H1aOQu8ImRZftP5jKCR0d2dy583Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=Hx812geP1WCzjwPutU1MmSZ23AUHYJEy0elJAGSzvt_lpsaebeOTnQJqUDfHfHu0Af6k24CN85kuHpvp151gn6cMdvPwmiPpbvZJFCG4IqJQ3DaewDS1_WN-3JziZrKmerO6JrJ-Eoa5flTxYwjtHeNgCITvT4QkfT2qQWcy2ghfqv4pue_icOUug3OsRaem5PUia0CKz_TdmmprVzicjOl0Y2mV8nYtpmxVUDR8TR2KLuv3KfSEnQRiE44UC574VrD6WJV__yayN_m9-64jXgr-tASlhs_rFRFBZ8CLc2GKBgmJSfzCKvIseOS3iPChdywLZzFAxntua5GXw_pHN4m27ofYwXxqQFz56CJu6woAXV5nBc7AIpkMURPRBdeD2SfiKT1YWXLQ1OiPhHAwJaQv66UWFP_YkX68RjOBQ0fTcdS1FggPUD-IN5D__9LRXBS0ki6wGcOrAqysu-GN-yGHEjXpObhhR35X8jGHRYz8cXDzg3h8-xd5fQ98y69o-JedEX0mdDU7gep4yPuQRl8oXxe7bJlUto92LL9R2-DcyCfJ6pyuRWHrGly0wd0J_1nuDX7_6sGLRjUcNJSj3ldM_D6hWgAWt3DeO1a67tnfqhN2iVowU9QDFxJUXE5G9-J5HL_s6wJ3nnxOZaw6VClYAVi8KBAuzCcLzgHQm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=Hx812geP1WCzjwPutU1MmSZ23AUHYJEy0elJAGSzvt_lpsaebeOTnQJqUDfHfHu0Af6k24CN85kuHpvp151gn6cMdvPwmiPpbvZJFCG4IqJQ3DaewDS1_WN-3JziZrKmerO6JrJ-Eoa5flTxYwjtHeNgCITvT4QkfT2qQWcy2ghfqv4pue_icOUug3OsRaem5PUia0CKz_TdmmprVzicjOl0Y2mV8nYtpmxVUDR8TR2KLuv3KfSEnQRiE44UC574VrD6WJV__yayN_m9-64jXgr-tASlhs_rFRFBZ8CLc2GKBgmJSfzCKvIseOS3iPChdywLZzFAxntua5GXw_pHN4m27ofYwXxqQFz56CJu6woAXV5nBc7AIpkMURPRBdeD2SfiKT1YWXLQ1OiPhHAwJaQv66UWFP_YkX68RjOBQ0fTcdS1FggPUD-IN5D__9LRXBS0ki6wGcOrAqysu-GN-yGHEjXpObhhR35X8jGHRYz8cXDzg3h8-xd5fQ98y69o-JedEX0mdDU7gep4yPuQRl8oXxe7bJlUto92LL9R2-DcyCfJ6pyuRWHrGly0wd0J_1nuDX7_6sGLRjUcNJSj3ldM_D6hWgAWt3DeO1a67tnfqhN2iVowU9QDFxJUXE5G9-J5HL_s6wJ3nnxOZaw6VClYAVi8KBAuzCcLzgHQm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=rJ_BqlSG_RlDF_Cz3n0KdsFzimbcJSRE0Dc5Y9nCzZxcDs--KGP4p07mLOmhNcJB9dZAeOUqV8eltgEAddbeVOVUCy0425SC0DKYvMm5QMtsC6uNmn5dc_nAr-l3Tu5Cf__1OcWO9d4IwiFuDjNF3l4yVThkzJX1RoDVrja9xH7UqgU3yodsVDXXcPyvfbQzgPiOFTCvNxvVxJB8MJ9yPd5-hdwBqpyUYBwk0x-qC5Bfyo6BkKcm02q1jALT_sxbPbN9O0OnSeL2e0hgWQ_xqb2mqnfCMkKs-d6qcL7JfiRPJ7lQ03ltxvytONs-jefwFNyHphpTMLsZWeSy4Jbk4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=rJ_BqlSG_RlDF_Cz3n0KdsFzimbcJSRE0Dc5Y9nCzZxcDs--KGP4p07mLOmhNcJB9dZAeOUqV8eltgEAddbeVOVUCy0425SC0DKYvMm5QMtsC6uNmn5dc_nAr-l3Tu5Cf__1OcWO9d4IwiFuDjNF3l4yVThkzJX1RoDVrja9xH7UqgU3yodsVDXXcPyvfbQzgPiOFTCvNxvVxJB8MJ9yPd5-hdwBqpyUYBwk0x-qC5Bfyo6BkKcm02q1jALT_sxbPbN9O0OnSeL2e0hgWQ_xqb2mqnfCMkKs-d6qcL7JfiRPJ7lQ03ltxvytONs-jefwFNyHphpTMLsZWeSy4Jbk4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
محمد باقر خرازی:
اگه پزشکیان یک بار دیگه استعفا بده، مجتبی خامنه‌ای موافقت می‌کنه
.
مسعود پزشکیان تا حالا نزدیک به 28 بار یا استعفا داده یا تهدید به استعفا کرده!
قراره ذوالقدر رو از دبیرکلی شورای عالی امنیت ملی دربیاره و محسن رضایی رو جاش بذاره.
مجتبی به عراقچی هم گفته دیگه به هیچ عنوان حق دخالت تو مذاکرات رو نداری.
همه اینا همیشه تهدید به استعفا میکردن ولی از وقتی مجتبی خامنه‌ای تهدید کرده، دیگه فیتیله‌ها رو پایین کشیدن.
ماشالله مجتبی خامنه‌ای خیلی سفت و بی‌تعارفه ، پدرش یکم تعارف داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69503">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhHt44KzSIpdvltLOfn0tp1otk3DRgYapxP2BiO4Z77mymxYd_5mxL4lkxRhOEeSLpwzAVbG0IFfVsOzzRBmOwlNUMwM7YlO6w0rjb2q2Vcs2qywg73IWv5St-IK7mqG_Pb4qY6yH9U1fCrqFmSxGlXaoroARCCYcuk8eiy_H96jdpYaY0WUzlHL6ujLX5F5z_Gf-fOV8VnkBRMogzr23V_mV228PKwf1bHp7Pn5EMQfbtDwOS6Ihh-vX8JnV-4E1a2tj77RwCcdjZchvn-bfZXrkbY6fndjpb-RFn0pdqdxO4HXCbniNuAeQR_Iq_9WTyTVG2TkPKboExmZMwAhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک کشتی باری در فاصله ۲۰ مایل دریایی شمال شرقی «الخصب» عمان، از طریق کانال ۱۶ VHF پیام اضطراری مخابره کرده و مدعی شده است که مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69503" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69502">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های حکومت از حمله به یک پایگاه آمریکایی در شمال کویت خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69502" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69501">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=n0IUl9Ite1h7pCzmgQFWcLgHL-7p3rfAcec5v8GBOXj37aarwOWgITBw_YMEO_viCb3MYc3bdH3-wE-CAtnucBz0zd8cas56dJpUKKDXFzSEY912dQbrriHSZjO939IVFaQ9Z7nB6ypq4lIIz6jyj9eVznt_uzQd8h_ODhvUHgoIELco9Ree_4waF1hHnOToeMkxueEACfK3JVwIZgcaYAdwgs8ji-heyL7jeaMY3fJMh27mRKoay2KnMPHAm146jZf321BTHSh2c7Vdpr4TltVtk7URIu1wfhyCOgunEnUzWW93BpNglKUlCgp5ROtOs72rKL1IgA5f9jVXi0MrvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=n0IUl9Ite1h7pCzmgQFWcLgHL-7p3rfAcec5v8GBOXj37aarwOWgITBw_YMEO_viCb3MYc3bdH3-wE-CAtnucBz0zd8cas56dJpUKKDXFzSEY912dQbrriHSZjO939IVFaQ9Z7nB6ypq4lIIz6jyj9eVznt_uzQd8h_ODhvUHgoIELco9Ree_4waF1hHnOToeMkxueEACfK3JVwIZgcaYAdwgs8ji-heyL7jeaMY3fJMh27mRKoay2KnMPHAm146jZf321BTHSh2c7Vdpr4TltVtk7URIu1wfhyCOgunEnUzWW93BpNglKUlCgp5ROtOs72rKL1IgA5f9jVXi0MrvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69501" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69500">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
منابع عربی:
شنیده شدن صدای انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69500" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69496">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r17Kqm6vYEHx43R6WXon7Vm3p5QAm5osoyeD0O6WTEkn9I2X3g9ZSrk1lnzRuro4BHXr3uY_HizA4Tie8wva9UdruT5t0Wl7fSPefbR-lcELIpkEohhvjaKjw4xs1dEMslilRdmVt5hhDvRbh0wldYS1SRAmOmnT81hCYQY4B7ToP77_44x-IAMLfaPBn2wezz5ZZiyFhTOao0HDqVRRVWYIO6IxIYEKIh4NcCBmA9xI-xx8yc_EQ-1CK5NTQngw2WJUKpuhkuLZiMg8E7p6Hh7djgKhaNMTFJycAmKuvWML9MX0wOWCvAdH_2BVE1H0fiXEbciaWxb9weLITSYJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=o46V5AxinO90jERJ6Yn2-BH4xAcobf3auSWPW44v8KXZmON59tCZl_VJsSB96yf_n-DgB88moHvd3mU8VoDKXnVZ_14CMrCEzwdZnmpqlE3hvVBqVxUP5nls8ThqWPfTffHCeeVujK14L7Bwt914eMgmdCK-7sOHwafom8bvPcEgmv-6bfbiHm2lKvgyZp7v5QmicQF72mzLIQQfEaZ5yJJir6OcoVilaNKSnM48CyH_tyAqPujucxgtKhZhcX1257HCV1L5NU_P0NWBhOqPNEnMA72PyTkCdRF_x25jOH29fbPsKCx-jdrwYRzJcft55Z1obsWpk6EKVTWfkC2_mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=o46V5AxinO90jERJ6Yn2-BH4xAcobf3auSWPW44v8KXZmON59tCZl_VJsSB96yf_n-DgB88moHvd3mU8VoDKXnVZ_14CMrCEzwdZnmpqlE3hvVBqVxUP5nls8ThqWPfTffHCeeVujK14L7Bwt914eMgmdCK-7sOHwafom8bvPcEgmv-6bfbiHm2lKvgyZp7v5QmicQF72mzLIQQfEaZ5yJJir6OcoVilaNKSnM48CyH_tyAqPujucxgtKhZhcX1257HCV1L5NU_P0NWBhOqPNEnMA72PyTkCdRF_x25jOH29fbPsKCx-jdrwYRzJcft55Z1obsWpk6EKVTWfkC2_mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقای سیاه‌پوستی که تو تصویر می‌بینید، رکورد ویوهای تیک‌تاک رو جابه‌جا کرده
👀
حالا کارش چیه؟ میره به شهرها و کشورهای مختلف و دخترها، زن‌ها و دوست‌دخترهای مردم رو بلند می‌کنه و باهاشون مثل دمبل وزنه می‌زنه!
جالب‌تر اینکه تو بعضی جاها، دخترا حتی صف می‌کشن تا نوبتشون بشه که ایشون بلندشون کنه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69496" target="_blank">📅 01:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69495">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b93335655.mp4?token=LkZvQR5t7z7LC23GN5cnTio_DUJGnYQ99C_duoIxHN_3l1t-FHf_t3a7BYwpjIbyYTw7GHCZx4CyyXFdoSwuL9qJ_b_I-6pux9tduAAuwpjAtHkZYbFDv4JVztPqAw2Vg0fQJNWKs9qpRpJ-fKB1vRLVAsoj4d9P-Aqh_VoJYRins2vVThGrtJ-lTck5kiXENWGWGtcedbWVTmZrjWORGN9bh6K5v-DioBwQXtD0qdzgPvS2W3WIo12JSQktp0EErBq9OC9O1WWmNzzZmnRkoJW6DwLTI1r6A-IPlWr8g_2GZP_ZK3LEvP3uDcK8iOT3pPpCec_2ir_PqpOQIqTOIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b93335655.mp4?token=LkZvQR5t7z7LC23GN5cnTio_DUJGnYQ99C_duoIxHN_3l1t-FHf_t3a7BYwpjIbyYTw7GHCZx4CyyXFdoSwuL9qJ_b_I-6pux9tduAAuwpjAtHkZYbFDv4JVztPqAw2Vg0fQJNWKs9qpRpJ-fKB1vRLVAsoj4d9P-Aqh_VoJYRins2vVThGrtJ-lTck5kiXENWGWGtcedbWVTmZrjWORGN9bh6K5v-DioBwQXtD0qdzgPvS2W3WIo12JSQktp0EErBq9OC9O1WWmNzzZmnRkoJW6DwLTI1r6A-IPlWr8g_2GZP_ZK3LEvP3uDcK8iOT3pPpCec_2ir_PqpOQIqTOIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دست فرمون پشم ریزون اوپراتور اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69495" target="_blank">📅 00:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69494">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLlEXUYjiMoybAJ9kVcPM6ERHkPR9NyX0jxRoabFJX_ZCWBHFu7IaecVtcaFsEfVRZz_4J3WFgk61YQAe4d2Y5c0iQnYfC3ucRywzGWVo2Tp7u552Wb29vB59Enl8nC6gJU7bEF-EgBfnly5cj4tn0VGN_uNV7Y9fKZ9RzFfsPB4RteBI4MpPaK21-ZGspzcEjdBBBpSWsY4KnirWM82odDrNN7q-YgsZJlVTCVchEp34j27zrWuk7dLaX6Wiw4Jr0FOLZFYRjDhz91CSgkwEwVwcoiID7YpS4J0A_DFIP1vMkhfUt4xjk-fVNYMn_uCc3EpQmqWUipkreS4xdyf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
ایران هیچ‌گونه قصدی برای مذاکره با رژیم ترامپ ندارد. هرگونه اقدام تجاوزکارانه با پاسخی کوبنده و قاطع از سوی جمهوری اسلامی مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69494" target="_blank">📅 00:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69493">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=HZA_c7SGuEYO4wRSjuAhq7Z79tAr5eMQvvTWaa87K_ks5nGttQICHfdSt9kvPwLc_K3Ss9hwRIvdu6yLyc9LFFQscza6OB4i-Ue_1m97xcEld9OOC7pfSDFanDywOSHvOqJAfDUrgcJD1_4WEljxhDII06bgiC2li9SxMtJhlSp5xDVPSjOF_qAvZfDYvOT7JAtCm_8uebkx-C5kCfWEYNx4jY6ieHRCBE_V3tYENRWEhcCphgcR-fUgaCYs9sxmnLYGocYc1gkVwD3anfPuxXN9CIzC0dr3gEpXUJz4wwPq90spvFSVnBtmlX42lioKDfFAz-9AIAf_eHOj12-Bcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=HZA_c7SGuEYO4wRSjuAhq7Z79tAr5eMQvvTWaa87K_ks5nGttQICHfdSt9kvPwLc_K3Ss9hwRIvdu6yLyc9LFFQscza6OB4i-Ue_1m97xcEld9OOC7pfSDFanDywOSHvOqJAfDUrgcJD1_4WEljxhDII06bgiC2li9SxMtJhlSp5xDVPSjOF_qAvZfDYvOT7JAtCm_8uebkx-C5kCfWEYNx4jY6ieHRCBE_V3tYENRWEhcCphgcR-fUgaCYs9sxmnLYGocYc1gkVwD3anfPuxXN9CIzC0dr3gEpXUJz4wwPq90spvFSVnBtmlX42lioKDfFAz-9AIAf_eHOj12-Bcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
آماده بودیم به ۳ نقطه از اوکراین حمله بکنیم ولی عذر خواهی کردن کنسل شد
پل های منتهی به هرمزگان رو آمریکا میزد که حمله زمینی بکنه ولی خب طرح هاشون ناپخته بود
تو ۱۷ روز با حملات شدید موشکی پهپادی ترامپ رو مجبور به شکست کردیم
آتش بسی وجود نداره داریم حملات معقولی انجام میدیم
تفاهم‌نامه با موافقت رهبری امضا شد
کویت رو ویران کردیم و فرماندهی سنتکام از قطر به اسرائیل منتقل شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69493" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69492">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571743cf02.mp4?token=N2yNQpps9ySjqZmE_HEwIgryzMxSOOqr1sg96oxzkh32FASImaRAhjjy6Z_zk-PchvgEoLii4E1WlWqGj_bRd48eKxigQ64mE0KhhoPlm2jvhpICrseQkEOtdALkpQ7SHoDmceetRjUokcqGQHvjolL5YOTq_DPyEzTMmBtaXvLjhA29b1o-xMjH_ujz6b401gNIuTy015oFtzuvu1iVW8gXL2dW-cFiAf6ZwKjCxfpVQLPvA77OlKIHP-imbPdJf-iHCN-iNxM57VLtQ0B7wHq1db8e3JGIFRgBJFvaH4nvsbKGg26e_78W-ks0KuxzpGdPIg_t4wNQlKNpxXsLXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571743cf02.mp4?token=N2yNQpps9ySjqZmE_HEwIgryzMxSOOqr1sg96oxzkh32FASImaRAhjjy6Z_zk-PchvgEoLii4E1WlWqGj_bRd48eKxigQ64mE0KhhoPlm2jvhpICrseQkEOtdALkpQ7SHoDmceetRjUokcqGQHvjolL5YOTq_DPyEzTMmBtaXvLjhA29b1o-xMjH_ujz6b401gNIuTy015oFtzuvu1iVW8gXL2dW-cFiAf6ZwKjCxfpVQLPvA77OlKIHP-imbPdJf-iHCN-iNxM57VLtQ0B7wHq1db8e3JGIFRgBJFvaH4nvsbKGg26e_78W-ks0KuxzpGdPIg_t4wNQlKNpxXsLXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی وایرال شده از موکب خدمه ام‌البنین که به زائرا آیفون ۱۷ و آیپد و گوشواره طلا میدن!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69492" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69491">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGCq-z4RZJ5MDFQ6SyZkhj4ZfD2xfLTpCrDKFAr7vt6Vy_3BWzkY0MWMXD_A_lZbseFVMz9PmTAWYkqNR9LJUV63_aWV7R8b49lMhMBf4ISbdEyAVwOjoJIj0uHe2OHivSdPCC_YMuD4_YVIq_NdBPjzoXCNLldHtc9k-iZ4fxIlCoA1KNykoU4AccObMV-oVJHQDiM9vnSwBOhuGUNXEnExXDQvRFPdL1kKsmL5idelbgF61eQmxCaMv7f9BFmDamNjQbbWmhk3yg2UNRD2Vv7z_LmQgZuUBLrZyj6Ma26gl8eztLDSX9B7eWJ7iCCTdnDyGGSobsBEdv1sleKe7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69491" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69488">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyIWpY1DmszBbyEVx_0kq1V7lcoNrnzq76IS0BS-m-NF16LImliu562zDm6cCfFbPkH6LjXUva4A2IbstpvbqtHWn-PGPgJ0hzRh3xG7-wdXgtGHXwlmbbnw8oBPzM7u2v5MX8nJHMNq-_l66S2n8VxvNcC7EFhy-ByoYL4vMYQqIXKzO26NsmkjuacGQctcTMHOJw0y_ugY27eQGcdeeu59IzSL9xu60kwrh46Z0Q4tr2TdmrcKxpEN2Oi6UMnGWeAn-cwW6ThQFT9_oSJoy0zpnvi9LPnABtuoblPNjoSU_UnTd6gy5egYHqKfh_rgXv_X2MSGskZoeFxMtwPADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/au5n3w2ZZ3Yb1ce-03ox6JhGoC_D7ItBNqmU2GkMDg7WZJvVBoAkxoTFQd_DHbFo3UmDD1Tny-XG1itezhkld5qJkG_uEXxvweGtQGxAkkmTQEPwL1w2xxFUC3WKrFinW-Ddp-P057oqgU43PcCXy99QYZ86V-0eRZnrLK70UYPlozPq-6JRIPYPbbP2PRWzxhnkHpp_TWJXRcUUwkrKvGPRRb1nBCpu18bf0vrzsbAfS-6A8JCiThFQWIPpBRbkyR7wjijSzBriAkUV7QwneKV_jryzqBfmFerNjkfqvaGrGQXIsCGQtCjkzEVTo22JZZ4CBDG-staVepdNXbobyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yu7oRBKaNHkYJzktiFPwTKAoeyAPuQXtIpzFp9S7Akm6sYZ0c8DIzUsiWSJMg7iCvBOdFr_Iw7rKcx8sJl-C-tmnus4KDCIRzXkJA99_6TBdBohwznquEk6C-ULEoh367mOrB0Sq6atFa_tlhv3b7KqaVfwvEpSvzIDRV8HtzylHWTaJPLQ_ZMqn8rmBx6JcvLPn5qZ-zzMePIVcM6ahbS7dM_84KNxnySSeGK8rep5JjxmYzaD5t0zTdd1r3SBoMfdf093qcOyEqVqg5qsb8EPq9BMgyexSu4EqnV-M8jXgXkxacHetkxDFPHfsfJan-vYZZUZqfFPOYdRDmIPC2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کامنت های دردناک مردم زیر قیمت PS5 تو سایت دیجی‌کالا
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69488" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69487">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=qfedzVseNwi03lJKnMeygjYl1j_gEdY-AWhF0uF5O0za_oTJ6_28PH8xNoi3aSK3dvUpJUMAmcstDQJg3Hl7rHiVQyrIpVluHzy8V-FEVTkMQcaYyxE2mj3N7qL7r4XbMZHD2iW-7MxdgTCjP0sVpqdjnI7WZ3T6F3wxYX8rFfbWhLOowSW0Boi8lWSSPuwKSwS5UWBa0IjLeoee_2P1vrQ6xDi7qeMA3is6A0i_M365CETmwWm45aN4yrgZ8UQGdX21pAkVeUWWQG5Y9dcpzm8VotRKq2gKPAU43ZrKypIvxlBPAAu6avWSt-w8nz5dfcPlJsfw0b9wE8UUhJ_mQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=qfedzVseNwi03lJKnMeygjYl1j_gEdY-AWhF0uF5O0za_oTJ6_28PH8xNoi3aSK3dvUpJUMAmcstDQJg3Hl7rHiVQyrIpVluHzy8V-FEVTkMQcaYyxE2mj3N7qL7r4XbMZHD2iW-7MxdgTCjP0sVpqdjnI7WZ3T6F3wxYX8rFfbWhLOowSW0Boi8lWSSPuwKSwS5UWBa0IjLeoee_2P1vrQ6xDi7qeMA3is6A0i_M365CETmwWm45aN4yrgZ8UQGdX21pAkVeUWWQG5Y9dcpzm8VotRKq2gKPAU43ZrKypIvxlBPAAu6avWSt-w8nz5dfcPlJsfw0b9wE8UUhJ_mQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
✈️
یک جنگنده F-16 نیروی هوایی اوکراین، یک پهپاد انتحاری روسی (Geran-2) را با شلیک توپ ۲۰ میلی‌متری ولکان (M61 Vulcan) در آسمان اوکراین سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69487" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69486">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22887d7155.mp4?token=AmsNKkz7OUfho5SBJNLcb5VHEfKsaZ9YEiHISATZWKIdp44iFPTYmWHhK3vu0uDzRfz1RxEyxmK58PJlfT4a87Gx0FBgn2cw8cc2hJaiGyLJsclNXfgG7YJOlU8fqjWFHGuebIhIOQksSc7ZsqGGlw7VeDGRg1Kyqwqko01EHEm9YxXUtm3VeDO2FiH9wZsIXtlCMH8cIkBFBa8D26CNciOlSNISD29fEhj8WSigoQzpLPtH-haJScjibeNT5z-kMo8SANumKMdTxVH9JESj_cZPKeJPC80JfIvdLgGR3Qe_w1CfbCFeGA0fTC3yQYy6HV8GJ2Ryn7pLEaAEvRmKdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22887d7155.mp4?token=AmsNKkz7OUfho5SBJNLcb5VHEfKsaZ9YEiHISATZWKIdp44iFPTYmWHhK3vu0uDzRfz1RxEyxmK58PJlfT4a87Gx0FBgn2cw8cc2hJaiGyLJsclNXfgG7YJOlU8fqjWFHGuebIhIOQksSc7ZsqGGlw7VeDGRg1Kyqwqko01EHEm9YxXUtm3VeDO2FiH9wZsIXtlCMH8cIkBFBa8D26CNciOlSNISD29fEhj8WSigoQzpLPtH-haJScjibeNT5z-kMo8SANumKMdTxVH9JESj_cZPKeJPC80JfIvdLgGR3Qe_w1CfbCFeGA0fTC3yQYy6HV8GJ2Ryn7pLEaAEvRmKdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که میبینید ۱۲۶ سالشه و اهل کشور برزیلِ؛ در زمان پایان جنگ جهانی دوم تقریبا میانسال بود
این بدبخت نمرد تا جنگ جهانی سوم رو هم ببینه و دبل کنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69486" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69485">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها با من تماس گرفتند و گفتند: «لطفاً حمله نکنید. ما توافق خواهیم کرد.»
این حقیقت محض است و همه آن را می‌دانند. چه کسی تماس نمی‌گرفت؟
کسانی که اطلاعات را به بیرون درز دادند کمک کردند، چون شدت حمله را فاش کردند و ایران هم از آن آگاه شد.
آن‌ها می‌دانستند چه چیزی در راه است.
قرار بود دیشب [حمله] انجام شود و مدت زیادی هم ادامه یابد، و [در نهایت] چیزی باقی نمی‌ماند.
اگر فرصتی داشته باشم که به افراد زیادی اجازه زنده ماندن بدهم، می‌خواهم آن فرصت را فراهم کنم.
بنابراین، هیچ محدودیت زمانی‌ای ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69485" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69484">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20068f370b.mp4?token=E1buJZCHNClo0LaXVEGr5ENg7ZTUhFvMWqQQAXM1rqrFj7uMR9AlF-UBjQ41hs_oBV1tZT5L49T1iO3zqxaEl5tpf5YNSVOWhhr808tWaesw-ZevlW2gQtVv90TJJSw7U8z8Yx4-O6jB05jBSw5cGdPaXOva034ea6ySK8x2u3CPizYdX11h_w51SoKypjw9ZD2JU5es51KkcIv_uwAvAxH96SWLV8rFunlBHFrE_mSP9e4FoJjqQCKIV7f_OZpo2J6GitSBl85IPzq4ZdQTa9UC1EDPLf3Nr3C9Jcgr_DGSiD65js6gMxSHea_rYH3mSZAfr5Tm_6yRTvpsrTR9Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20068f370b.mp4?token=E1buJZCHNClo0LaXVEGr5ENg7ZTUhFvMWqQQAXM1rqrFj7uMR9AlF-UBjQ41hs_oBV1tZT5L49T1iO3zqxaEl5tpf5YNSVOWhhr808tWaesw-ZevlW2gQtVv90TJJSw7U8z8Yx4-O6jB05jBSw5cGdPaXOva034ea6ySK8x2u3CPizYdX11h_w51SoKypjw9ZD2JU5es51KkcIv_uwAvAxH96SWLV8rFunlBHFrE_mSP9e4FoJjqQCKIV7f_OZpo2J6GitSBl85IPzq4ZdQTa9UC1EDPLf3Nr3C9Jcgr_DGSiD65js6gMxSHea_rYH3mSZAfr5Tm_6yRTvpsrTR9Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در مورد ایران:
می‌خواهم قبل از نابودی کامل، آخرین فرصت را به ایران بدهم.
امیدوارم سر عقل بیایند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69484" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69483">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T3mSVAUAp9RLT_ziU_fpBOhiXr842UmWts2agLNooKFYFxvwFLUN7NIQ3glPupges2jxoIL5N-WagBG4kOxuDICNdm45CrL4ehJvs-NRaU8q9SS8CPflhz0H_BCsqmFhE0TICB12sgnwM-T3fmG7rg2WwiDtiz7e-D5q-f-B9C_-NOOx1WWVm7klgNuvC3cJhtiaF7s2eq1-Xj-7prtxWWhxTQAq2b1wa4xMSJBer7NIsl18QTPGgKL0LvzxOyKEgVKI8_6Zc2mJs8h3XKamq0VPihIHAinADcdkdzw1sMBaqVLJqCQbiJMrIXIIREEo2d_AK4dDJ5FAMVLA4mVplR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T3mSVAUAp9RLT_ziU_fpBOhiXr842UmWts2agLNooKFYFxvwFLUN7NIQ3glPupges2jxoIL5N-WagBG4kOxuDICNdm45CrL4ehJvs-NRaU8q9SS8CPflhz0H_BCsqmFhE0TICB12sgnwM-T3fmG7rg2WwiDtiz7e-D5q-f-B9C_-NOOx1WWVm7klgNuvC3cJhtiaF7s2eq1-Xj-7prtxWWhxTQAq2b1wa4xMSJBer7NIsl18QTPGgKL0LvzxOyKEgVKI8_6Zc2mJs8h3XKamq0VPihIHAinADcdkdzw1sMBaqVLJqCQbiJMrIXIIREEo2d_AK4dDJ5FAMVLA4mVplR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران حاضر است به وضعیت آزادی کامل کشتیرانی در تنگه هرمز بازگردد؟
🇺🇸
ترامپ:
اجازه نمی‌دهم آن‌ها [بابت عبور] هزینه دریافت کنند. اگر قرار باشد کسی هزینه‌ای دریافت کند، ما خواهیم بود. ما کنترل کامل را در اختیار داریم.
ما سازوکاری در نیروی دریایی داریم که نوعی محاصره محسوب می‌شود؛ آن‌ها به آن «دیوار فولادی ایالات متحده» می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69483" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69482">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=A2535BmE3xrYzCo9t9FU52xk9DuttOKSDjMGLKK25h9oGeuxjgZMWDISSBnAvoB9I9v42T5frfiVy3L3mngvOBjzH-k0gZZ5RK2bH5DDFg6eWLwIHpHUteOrXi7VSe3ztxOlZasUdCq2zSu4s9VE9XyMrVkDMFvaYRxJ8PCjj5XyGq5ST1PdJLuUnco8LZAHXWh0oL85YB7MPtlQo8zfcJJwtu2pBQs26fQrMAxWB6va-FCTqXAJ3Rb0mjK9XbZtV93i_uqrvIpmhZbu2olfMzwkRJsA2f1ZgIolv1OwnmyXDWbaxKTXmqb7vD3FOWNNhD-2so3hBmfbPHUdBVviTxeZrhiYURwhgb5UuZ9S2OWT4ZkWQbK-b007xBFcTCotwDN-iJGOSKglPJvH9biC3Ji4WiRcM39xPDps9iizWHne9ZJJpj1zgcynvEt23z34sgVFktuR9V0C6kjbfe-AFMjZrAyKYiOVjn3h3D0osZQItKz4bkVKWra-GA3ubm7ul7iJ_K4thb3SABNDFvYg0pM4kBnTcT2tsfCM6QckCoEu0LmWP_JnIbSX6wbYyiPAA1jtT6e6-67SPlrDJID38822qtwiV8jU45QcP84EIYp6u5T9U-5z7FDqzoATTd3DNWloJTsIgWZ5USrLuut2IrfoSxYSWib6drR7s4mVQYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=A2535BmE3xrYzCo9t9FU52xk9DuttOKSDjMGLKK25h9oGeuxjgZMWDISSBnAvoB9I9v42T5frfiVy3L3mngvOBjzH-k0gZZ5RK2bH5DDFg6eWLwIHpHUteOrXi7VSe3ztxOlZasUdCq2zSu4s9VE9XyMrVkDMFvaYRxJ8PCjj5XyGq5ST1PdJLuUnco8LZAHXWh0oL85YB7MPtlQo8zfcJJwtu2pBQs26fQrMAxWB6va-FCTqXAJ3Rb0mjK9XbZtV93i_uqrvIpmhZbu2olfMzwkRJsA2f1ZgIolv1OwnmyXDWbaxKTXmqb7vD3FOWNNhD-2so3hBmfbPHUdBVviTxeZrhiYURwhgb5UuZ9S2OWT4ZkWQbK-b007xBFcTCotwDN-iJGOSKglPJvH9biC3Ji4WiRcM39xPDps9iizWHne9ZJJpj1zgcynvEt23z34sgVFktuR9V0C6kjbfe-AFMjZrAyKYiOVjn3h3D0osZQItKz4bkVKWra-GA3ubm7ul7iJ_K4thb3SABNDFvYg0pM4kBnTcT2tsfCM6QckCoEu0LmWP_JnIbSX6wbYyiPAA1jtT6e6-67SPlrDJID38822qtwiV8jU45QcP84EIYp6u5T9U-5z7FDqzoATTd3DNWloJTsIgWZ5USrLuut2IrfoSxYSWib6drR7s4mVQYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره مذاکرات با ایران:
امروز یا فردا متوجه خواهید شد که وضعیت مذاکرات در چه مرحله‌ای است.
مذاکرات به هر طریقی که باشد، به‌سرعت پیش خواهد رفت؛ موضوع پیچیده‌ای نیست.
ما درباره بازگشایی تنگه [هرمز] در روز آینده صحبت می‌کنیم؛ بازگشایی کامل آن.
سپس درباره توانمندی هسته‌ای ایران گفتگو خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69482" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69481">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=EDmoE8I_y_Ka7LAzHxTIO_NIWXhpmRaOCeb2yKqC1c0RN_Y-6-M18rFUNYfuPgcB82Ve-km86KLDyPTfypKmZbH0BnMq0fLxaUnNEIoVlAuJSvxK5CkVULzDLlxaVvKZDnyHtSLmmnImam6COlpYp05qCExCKkK2liEFrCkJ4qvrlkap1lOLgCF08nV3ppQjXov2HpSlqf2Q7LIAHfvfZemYs0C2uPll-_-Q2YwuEsyvxfqVRQs9jxkzti41V-6OunKtlqZwBlUrBpzxXkxuhxSCeiSgiCeXc5BA1oDUkU99siyUOCD8GcrQV3d1lAsXfBDOIkoUkOWezMKhiUurDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=EDmoE8I_y_Ka7LAzHxTIO_NIWXhpmRaOCeb2yKqC1c0RN_Y-6-M18rFUNYfuPgcB82Ve-km86KLDyPTfypKmZbH0BnMq0fLxaUnNEIoVlAuJSvxK5CkVULzDLlxaVvKZDnyHtSLmmnImam6COlpYp05qCExCKkK2liEFrCkJ4qvrlkap1lOLgCF08nV3ppQjXov2HpSlqf2Q7LIAHfvfZemYs0C2uPll-_-Q2YwuEsyvxfqVRQs9jxkzti41V-6OunKtlqZwBlUrBpzxXkxuhxSCeiSgiCeXc5BA1oDUkU99siyUOCD8GcrQV3d1lAsXfBDOIkoUkOWezMKhiUurDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک سند خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69481" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69480">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=dHwvrSIWnFa03XVuy7LXl8R1aj2Pg82hgi2MVtddLNxoOUWPdXmzfVS5ixLQ24t778Cpco1xIGPK18J-YM4Nuf-TAFrv_6qPFFN44qOv0iHNBn2EXU8waalfRzQUww3UbP_Fb8E-Dq2mOYMIeN7o2XrOXDOxuRr9rWbrOMc6tUO8bb2OF9oIBRGlmen6wfCZs2a8ojbvpkFpMpuvxR1-zk2GFLlAJNSp4WsiJHYQYGgCOVeCM54UQ5aXPBhNMMtto28yoRdg2q80tnr00JbqR3tjHmqcy9AbjmEiug-3WtJIe610HIMRPGrzCJOpefvzQAPW0rpPdOSqGxqaMwu6Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=dHwvrSIWnFa03XVuy7LXl8R1aj2Pg82hgi2MVtddLNxoOUWPdXmzfVS5ixLQ24t778Cpco1xIGPK18J-YM4Nuf-TAFrv_6qPFFN44qOv0iHNBn2EXU8waalfRzQUww3UbP_Fb8E-Dq2mOYMIeN7o2XrOXDOxuRr9rWbrOMc6tUO8bb2OF9oIBRGlmen6wfCZs2a8ojbvpkFpMpuvxR1-zk2GFLlAJNSp4WsiJHYQYGgCOVeCM54UQ5aXPBhNMMtto28yoRdg2q80tnr00JbqR3tjHmqcy9AbjmEiug-3WtJIe610HIMRPGrzCJOpefvzQAPW0rpPdOSqGxqaMwu6Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
قرار بود دیروز ضربه بسیار سختی به آن‌ها وارد کنیم؛ بسیار بسیار سخت.
سخت‌تر از هر حمله‌ای از زمان جنگ جهانی دوم. این اقدام بسیار بزرگی محسوب می‌شد و ما کاملاً آماده اجرای آن بودیم.
در حال حاضر، به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و بسیاری دیگر، مشغول گفتگو هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69480" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=SNrIoMwsLjKrQCaBN4LUIw1-ykvgqFmIH76t47Cq2P5KRKaisZFNTvj58lVM8Vpo2cM8UQxvfaXB0NJLFXFnn5pJvszKKa65wszDPzajf4ANWxPAnBwswuFgTHVeQfL1Q7EZi41yZ1ZfNHBUnFEuuljMg4h0BJiXoq59TP7oxPQohEDGyNJklDFd5Ip7Z2M_JRm-AAaTDYEdEhu-MVnpQfkU_a0n1L-r_vO617XSvPmykHO2sBL55zGrlZ-HaZRZGByMimRj_ZSeTfTG1_okXYMmbIQJjS60QGe3K5h4beUmNNgIpm03PMZk4C8TwSsG-2yJfdMkBHt5ifpXjnEXnXvfQxWFmTomb7ewz7x8n0kqJYiFhCC4F78nKxWydIMj-ic4KUwxS-0nQtb-7lLZgIEobNLpzL_a4ROM2Eb-d78k2vrOchMeWPxwy0BIYQElK6Xfnq1JGykT7nTj6-xwiUZqbmrFcletDVwKkDH57N5Hd0YDABoTDKd5Z0PQvxfl8HxpzqygXI1zXqjbRqeCLnUXjKSace0EVlTZHdYYuRi14gluCh0gAbCE_pM7nYFNPTbCKO-E151FlOvhl-Oq85d589AWMIP7Gr2Kp6AUi22O45aIQrovdrZDTCilaVesw4-nT39YfqTPmx4bERcWvTeNDSSM4PeFMEQP0Bqvw4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=SNrIoMwsLjKrQCaBN4LUIw1-ykvgqFmIH76t47Cq2P5KRKaisZFNTvj58lVM8Vpo2cM8UQxvfaXB0NJLFXFnn5pJvszKKa65wszDPzajf4ANWxPAnBwswuFgTHVeQfL1Q7EZi41yZ1ZfNHBUnFEuuljMg4h0BJiXoq59TP7oxPQohEDGyNJklDFd5Ip7Z2M_JRm-AAaTDYEdEhu-MVnpQfkU_a0n1L-r_vO617XSvPmykHO2sBL55zGrlZ-HaZRZGByMimRj_ZSeTfTG1_okXYMmbIQJjS60QGe3K5h4beUmNNgIpm03PMZk4C8TwSsG-2yJfdMkBHt5ifpXjnEXnXvfQxWFmTomb7ewz7x8n0kqJYiFhCC4F78nKxWydIMj-ic4KUwxS-0nQtb-7lLZgIEobNLpzL_a4ROM2Eb-d78k2vrOchMeWPxwy0BIYQElK6Xfnq1JGykT7nTj6-xwiUZqbmrFcletDVwKkDH57N5Hd0YDABoTDKd5Z0PQvxfl8HxpzqygXI1zXqjbRqeCLnUXjKSace0EVlTZHdYYuRi14gluCh0gAbCE_pM7nYFNPTbCKO-E151FlOvhl-Oq85d589AWMIP7Gr2Kp6AUi22O45aIQrovdrZDTCilaVesw4-nT39YfqTPmx4bERcWvTeNDSSM4PeFMEQP0Bqvw4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: مذاکرات با ایران حالا دیگه متوقف شده.
🇺🇸
املاکی: نه، همین الان هم مذاکرات در جریانه. واقعاً اتفاق عجیبیه.
این بار دیگه اصلِ مذاکره رو انکار نمی‌کنن.
فقط نمی‌دونم چرا، هر وقت دارن مذاکره می‌کنن، دوست ندارن بگن که دارن مذاکره می‌کنن.
با ونزوئلا یه درگیری داشتیم که خیلی خوب جمع شد.
الان هم با ایران درگیر یه پرونده هستیم و اون هم داره خیلی، خیلی خوب پیش میره.
شما هم دارید فوق‌العاده کارتون رو انجام می‌دید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69479" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=TfrDQrUVEJn2feqIHdgFgu9eD1GelmctXxQsfmy0D74E-Q2fGMLZXNfkgOdboM_Pnrlu8KhseKNL5o6V6H5dbiFC6THFwywFJ1djgM7uhcO1ijWrnLsinBT7a6quoFDz5ZODOFf5UPA2SfkuBoOR8TFciXaH_2Cm_zSwWTe4OMt-3HtdoZNJ983N1LprNj0B6W-IjFPk6G1KwBrvUz9MgbfWGfCobSUwjcZgwUkXa4WiZm0uPm_uJypifgUJLEl4_ruF3rD1Zybv2krFJTne2M7nubwrkpEmCR1X9q3DikkhKrlu5Ljd2iGbbRn1HOoA6Mu2f5RcncOvQ1t6u-zl2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=TfrDQrUVEJn2feqIHdgFgu9eD1GelmctXxQsfmy0D74E-Q2fGMLZXNfkgOdboM_Pnrlu8KhseKNL5o6V6H5dbiFC6THFwywFJ1djgM7uhcO1ijWrnLsinBT7a6quoFDz5ZODOFf5UPA2SfkuBoOR8TFciXaH_2Cm_zSwWTe4OMt-3HtdoZNJ983N1LprNj0B6W-IjFPk6G1KwBrvUz9MgbfWGfCobSUwjcZgwUkXa4WiZm0uPm_uJypifgUJLEl4_ruF3rD1Zybv2krFJTne2M7nubwrkpEmCR1X9q3DikkhKrlu5Ljd2iGbbRn1HOoA6Mu2f5RcncOvQ1t6u-zl2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
ما با ونزوئلا اختلافاتی داشتیم که به خوبی حل و فصل شد.
ما با ایران نیز اختلافاتی داریم، و این موضوع نیز به خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69478" target="_blank">📅 21:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=f6rCUSs3chUlxgrlMjAIAwjSpA_rJsoN6YBQvRHGQWZMRp_dpSztlT2nQR88Y-qJh9EYUBs3yzjVvSBTyOVVG2yueAcilToV611k3p1rwX4cOUyxXEWeJdvzOO30-tzS5IrLUrUQVpRCTZ__36J3zwT1ccicQgjwJCe47netVP9EwB6rClJgRtSBjq62B-1KF0qKbKmR-0Yftl1xB5CTcXe4i5umRo_XcCz59QPnubN4oPakUuw9grzyvbYJ-_Q0CkAymb4hmzZoBhDKccT57_ICUDUDrLYTFOoj1fN0edVdkNPqIZ9byhT5mRdBCJxSFtOCF8QcGeukSEsPBm5P3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=f6rCUSs3chUlxgrlMjAIAwjSpA_rJsoN6YBQvRHGQWZMRp_dpSztlT2nQR88Y-qJh9EYUBs3yzjVvSBTyOVVG2yueAcilToV611k3p1rwX4cOUyxXEWeJdvzOO30-tzS5IrLUrUQVpRCTZ__36J3zwT1ccicQgjwJCe47netVP9EwB6rClJgRtSBjq62B-1KF0qKbKmR-0Yftl1xB5CTcXe4i5umRo_XcCz59QPnubN4oPakUuw9grzyvbYJ-_Q0CkAymb4hmzZoBhDKccT57_ICUDUDrLYTFOoj1fN0edVdkNPqIZ9byhT5mRdBCJxSFtOCF8QcGeukSEsPBm5P3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فرماندهی مرکزی آمریکا (سنتکام) فایل صوتی مکالمه ناو آبی‌خاکی USS Comstock (LSD-45) با یک شناور ناشناس را منتشر کرده است. در این مکالمه که از طریق کانال ۱۶ رادیویی دریایی VHF (فرکانس بین‌المللی تماس و اضطرار) انجام شده، به شناور دستور داده می‌شود مسیر خود را تغییر دهد و هشدار داده می‌شود که در صورت عدم تبعیت، با استفاده از زور وادار به اجرای دستور خواهد شد.
ناو USS Comstock به‌عنوان بخشی از گروه آماده آبی‌خاکی USS Boxer (ARG) و همراه با یگان یازدهم اعزامی تفنگداران دریایی آمریکا (11th MEU) در منطقه مسئولیت سنتکام مستقر است و توانمندی اجرای عملیات آبی‌خاکی و واکنش سریع به بحران‌ها را در اختیار نیروهای آمریکایی قرار می‌دهد.
بر اساس آخرین اعلام سنتکام، نیروهای آمریکایی تاکنون ۴۴ کشتی تجاری را که به‌صورت داوطلبانه از دستورات محاصره تبعیت کرده‌اند، به مسیر تعیین‌شده هدایت کرده‌اند، دو شناور را برای اطمینان از رعایت دستورات بازرسی کرده‌اند و دو شناور متخلف را که با وجود هشدارهای مکرر از اجرای دستورات خودداری کردند، از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69477" target="_blank">📅 21:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACMrP0wRJNbAfNNOLGZ8BwqcYDmxnOsJfzG-vLHiJ-547mOViFWgd2q6G7hkz18qjQ67FgeCTED5S1KGGtcRV1fAT2urZgeD70HwSJCSTV_jDu1_XBsd4S7ZLRHcW4o4QbJv3hwN6FyVrtvpUBI-nsjWjweZeFr4aSbNgqOkd587lGeIPyAKbNlQ_NTLiPzWjVng4HzKGUPR-5Rw6Zvm6ZjrfEdLYPxHAeN3fB4DF-IrKTHPz9X2651EGyoBv15o7IObNNJVBPWzaLYdlywSublI0nd0mqKi8rrTtzQeXAyeQaFmVN9lhd4ORQs0wAY5r05G6VAMRCGvKKa9U7wIeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مارک لوین:
من از اسرائیل حمایت می‌کنم.
من از اوکراین حمایت می‌کنم.
من از تایوان حمایت می‌کنم.
من از مردم ایران حمایت می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69476" target="_blank">📅 20:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra1Ym4emAsj7OZCXU0_BE03XQ7G8pggnIVKVHucMIkIO3ORmBWyRS3lO4HOvcfUcdkrRUt6u-4Cys6YRhuYQRqUJbpZ8AOu9hwe3i3CKy_LGxqWziBoBWMQpLcq-oU8MPUEyRajQg2YIvtldDn5-GAuuYCh5Efd8p1GyoBuHrYcbTDrlt9Lr6Ywm0H20Xf66MXePTgbedYGoSrSDpHU5Ao2bvD1pgbwpRItXc6mYI8F4igfIJrUwjxfkWMuBPtn3Or3b6b0c8aLTat-AQ9mE8xEcyHsZMnOWCyvdlcqjbsBiXDqeUgujus-3R15XKVQyr70Du5NCJoscbBOEz0SYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ : رهبری ایران واقعاً یه جورایی دو‌رو و ریاکاره که باورنکردنیه؛
خودشون می‌خوان مذاکره کنن، بعضی‌ها حتی میگن التماس می‌کنن، مذاکرات شروع می‌شه، جلسه بعدی هم قراره به‌زودی باشه، بعد علناً و با افتخار میگن که هیچ مذاکره‌ای در کار نیست، هیچ صحبتی نمیشه و فقط با «عمان» کار دارن!
بعدش هم همون چرت‌وپرت همیشگی‌شون رو تحویل می‌دن که می‌گن تنگه هرمز رو با قدرت خودمون اداره می‌کنیم، در حالی که از قبل کاملاً تحت کنترل نیروی دریایی آمریکاست و همون «محاصره» یا همون‌طور که بعضی‌ها می‌گن «دیوار فولادی ایالات متحده»!
هیچی به ایران نمی‌رسه مگر اینکه ما بخوایم، و هیچی هم نخواهد رسید مگر اینکه یه توافقی بشه یا اینکه کامل تسلیم بشن.
فرقی نمی‌کنه ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم درباره‌ی راه‌حل مشکلی حرف می‌زنیم که خودشون دهه‌هاست ایجاد کردن، خیلی ساده‌ست:
ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69475" target="_blank">📅 20:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69472">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4129d878df.mp4?token=KJdmuEVYLZ8rk7wz0f0ZLydYUameYehHahEXNdIDy4fBWqj8WlqYmkc_7jjtpTrdisHogAVXkWZKckvwLi11tMq9JkeSfq85SJBN4_4zi68lxin7z3gbh-d_rbps3E4CbfIATsyry1zX-SLBKQJElszuSTIfvzZrLws6-0Z51RknWKGvQqMXXWHsxXg0wtcduH9hU_978blP3UuAHe4SGPH3ICn8KYF-qVcibzgP_8_v4p0KsE8zvoDXqh4LZUcSTggnxZwE9ULBAbbfCnh2J5EeNNWgSJ1_xiF1J7SxP3NaA8PGBEjDuVR5POu2dyrSHpSC0G2v6RuVTwgeId43Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4129d878df.mp4?token=KJdmuEVYLZ8rk7wz0f0ZLydYUameYehHahEXNdIDy4fBWqj8WlqYmkc_7jjtpTrdisHogAVXkWZKckvwLi11tMq9JkeSfq85SJBN4_4zi68lxin7z3gbh-d_rbps3E4CbfIATsyry1zX-SLBKQJElszuSTIfvzZrLws6-0Z51RknWKGvQqMXXWHsxXg0wtcduH9hU_978blP3UuAHe4SGPH3ICn8KYF-qVcibzgP_8_v4p0KsE8zvoDXqh4LZUcSTggnxZwE9ULBAbbfCnh2J5EeNNWgSJ1_xiF1J7SxP3NaA8PGBEjDuVR5POu2dyrSHpSC0G2v6RuVTwgeId43Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
درگیری عرزشی ها و پلیس عراق در کربلا:
توی عراق یه روحانی به اسم صادق شیرازی، مخالف جمهوری اسلامی و خامنه‌ای هست، اون معتقده که فقط باید گفت لبیک یاحسین، نه لبیک یا خامنه‌ای.
حالا عرزشی‌ها دیشب افسار پاره کردن و هجوم بردن سمت موکب این روحانی و شعار مرگ بر آمریکا و لبیک یا خامنه‌ای سر میدادن.
عرزشی‌ها شروع کردن به کتک زدن مردم عراق تا اینکه پلیس وارد شد و با شوکر و باتوم عرزشی‌هارو کتک میزد.
طی این درگیری بیش از ۱۰۰ نفر به بیمارستان منتقل شدن و عراقی‌ها میگن دیگه نباید ایرانی‌هارو راه بدیم، غذای مفت میخورن و مارو کتک میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69472" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69471">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=oDrXPw3Lx6AX8D_JRD5eg-Syh7tsvfbFB6u-HC7yVO0YLZ5ZtWHnZzVDovW5z0Mi_Wn28XQBnxESJOChocdZfCZEKpO9F1zd0CJlzAX8c2rC38XcCiKdJGNfCtjOiceVdL_7_mbQvhhVokBV62hQAcENq7qEj0ePdUOkvy25ZiEHZ3e43W3VHu130fb8DEGtiHgWsLAKgDSPqQlkxUXcCyrtkLW7-HLStigOeS1oCqLDIJTKUsmrW9fthrZ1BdAsvDgRGcO_4qlUh1hAEEhmJ_e7qM0P5Xuno6lScZaYa7t_F7QloyjnEIoIluifYr1wiHU8DSfXknQJHztzQACafhkA7SMPS6RRF5tZdr0Rl13YJXOeFm4SGWwVOcpyyEY0wimax_yMPORRqHcPPdNv-7xT6wvPKfybgEf8dGz6HAYhhhF5Z6tExzuF-kdSF587aii5AIBcnjA-Xh2xmF2vapJ_W1P5P4Q8jwiPSvqPyJDGKq2xCy8uWj4XkCJQXZQLS6SVV0EslYf3aBMjcfSk5LwME2cE5L8EEIKpmmrnfb6tPc19E_liTkXT0HplyPU2ZJWT_HN3IfFWesPVgybCSiAKF-cvJFJkQBE-8uJsFzFPcIz9Fx3eeUGWwgQ4_vCiSLkcNHrCbeof-VaFMCyzKqVd_SBN1o70Y3jHRR-gKKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=oDrXPw3Lx6AX8D_JRD5eg-Syh7tsvfbFB6u-HC7yVO0YLZ5ZtWHnZzVDovW5z0Mi_Wn28XQBnxESJOChocdZfCZEKpO9F1zd0CJlzAX8c2rC38XcCiKdJGNfCtjOiceVdL_7_mbQvhhVokBV62hQAcENq7qEj0ePdUOkvy25ZiEHZ3e43W3VHu130fb8DEGtiHgWsLAKgDSPqQlkxUXcCyrtkLW7-HLStigOeS1oCqLDIJTKUsmrW9fthrZ1BdAsvDgRGcO_4qlUh1hAEEhmJ_e7qM0P5Xuno6lScZaYa7t_F7QloyjnEIoIluifYr1wiHU8DSfXknQJHztzQACafhkA7SMPS6RRF5tZdr0Rl13YJXOeFm4SGWwVOcpyyEY0wimax_yMPORRqHcPPdNv-7xT6wvPKfybgEf8dGz6HAYhhhF5Z6tExzuF-kdSF587aii5AIBcnjA-Xh2xmF2vapJ_W1P5P4Q8jwiPSvqPyJDGKq2xCy8uWj4XkCJQXZQLS6SVV0EslYf3aBMjcfSk5LwME2cE5L8EEIKpmmrnfb6tPc19E_liTkXT0HplyPU2ZJWT_HN3IfFWesPVgybCSiAKF-cvJFJkQBE-8uJsFzFPcIz9Fx3eeUGWwgQ4_vCiSLkcNHrCbeof-VaFMCyzKqVd_SBN1o70Y3jHRR-gKKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
عملیات آزادی عراق؛
در ۱۷ مارس ۲۰۰۳، جورج بوش بزرگ رئیس جمهور آمریکا در یک سخنرانی تلویزیونی به صدام حسین و پسرانش (عدی و قصی) ۴۸ ساعت فرصت داد تا عراق را ترک کنند.
او هشدار داد که در غیر این صورت، حمله نظامی در زمان انتخابی آمریکا آغاز خواهد شد؛
پس از پایان اولتیماتوم، بوش در اتاق وضعیت کاخ سفید  او در آنجا دستور رسمی حمله را امضا کرد.
بیش از ۱۰۰۰ بمب که بعضی آنها ۱ تن وزن داشتند و ۵۰۰ موشک کروز تاماهاوک را به سمت مواضع ارتش صدام شلیک کردند، بین ۱۵۰۰ الی ۱۷۰۰ سورتی در ۲۱ مارس انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69471" target="_blank">📅 19:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69470">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=Vh8q1JUIj1TNkbH8PPrkljUukFMLLl87PrXaA7hc7arjy4bmgSJNHYVtMynYWUdGoSigtEjd6dIZaiSCyW6oglV9shvADawtgnh6uVXSts_9WhMZKnMlEI_iyUvV_1RxkpeL45oLTfLGxITHl7LCgAGbIrOybfY0ghDDeHSmkijfNmtr5kw_EWrkRB-hIa-oYhByaOBCma7GLQUKxWIyzJZEbwCwPNLtnthk51jzbdAttReyf79eeqg1J4jocSFfZ1xL_l332aAZSsZ4UoK-JIMrTJZA64mvGXKf1262_rmL23_LozZVownNQ0nBZ3HdT-LMg0O57Os1vGC65jaFVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=Vh8q1JUIj1TNkbH8PPrkljUukFMLLl87PrXaA7hc7arjy4bmgSJNHYVtMynYWUdGoSigtEjd6dIZaiSCyW6oglV9shvADawtgnh6uVXSts_9WhMZKnMlEI_iyUvV_1RxkpeL45oLTfLGxITHl7LCgAGbIrOybfY0ghDDeHSmkijfNmtr5kw_EWrkRB-hIa-oYhByaOBCma7GLQUKxWIyzJZEbwCwPNLtnthk51jzbdAttReyf79eeqg1J4jocSFfZ1xL_l332aAZSsZ4UoK-JIMrTJZA64mvGXKf1262_rmL23_LozZVownNQ0nBZ3HdT-LMg0O57Os1vGC65jaFVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
اکثریت قاطع ایرانیان، اسرائیل را تحسین می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69470" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69469">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=j3yPy6JdjwVfpHtdBKt_LscWziBAGlvME8ZikRI9av1cMqFXd2IPVQpQSEbtjfRzgtCtHbKsPFlnIdhDFaSu8x7q72EhTMtTGWPv-iHWn2up6s0KMZNkZb3u3Ah5k6Yo3hLBWZJk3BeOfLwCxT4RE8LQx9bwthTNuSgHquCH2yHNqgu8FIMYPWaFG_4SbyCs2Sg5ZNXbECzvx1FCy1zmI79TGKUjI1peI8ssaIzxm4UlfcQhJp5QQ7R-uOOOmi7sdEiivxW2tSsQWnJmyVq10QAIn6HR1dBHJ3d9ftKH5gMpUjdkqC5FQUkxTzsu4QswnBi8kkEu-HmH6hMOtHqHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=j3yPy6JdjwVfpHtdBKt_LscWziBAGlvME8ZikRI9av1cMqFXd2IPVQpQSEbtjfRzgtCtHbKsPFlnIdhDFaSu8x7q72EhTMtTGWPv-iHWn2up6s0KMZNkZb3u3Ah5k6Yo3hLBWZJk3BeOfLwCxT4RE8LQx9bwthTNuSgHquCH2yHNqgu8FIMYPWaFG_4SbyCs2Sg5ZNXbECzvx1FCy1zmI79TGKUjI1peI8ssaIzxm4UlfcQhJp5QQ7R-uOOOmi7sdEiivxW2tSsQWnJmyVq10QAIn6HR1dBHJ3d9ftKH5gMpUjdkqC5FQUkxTzsu4QswnBi8kkEu-HmH6hMOtHqHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
خاورمیانه دیگر آن خاورمیانه سابق نیست. ایران هم دیگر آن ایران سابق نیست. ضربات سنگینی به آن‌ها وارد شده است.
آن‌ها همچنان توانمندی‌هایی دارند، اما به یک ماه گذشته نگاه کنید؛ آن‌ها به سمت ما شلیکی نکرده‌اند.
چرا شلیک نکرده‌اند؟ چون می‌دانند ما می‌توانیم چنان ضربه سنگینی به آن‌ها بزنیم که بازدارنده باشد. اگر به ما حمله کنند، متحمل ضربه‌ای بسیار سخت خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69469" target="_blank">📅 18:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69468">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=NST3tULbUi9OV7scUUjxAnnuVPShQNy9XW1Uh-HmuAxnRQasuNsS4HIUV4wmbANoRs3bT_Lj0rl8FirZdFLe8Yd-xXppBW3SnjhpEab4x2q-v8aYNOYzs3F09f4hpD_CWUCwDBtM0Vb76Zvo1VRqZHWbETVxseQX2zXSRA3IL-7r_57FGxOmMCLTMIZqPP6PFdx0bQOYl9PIcAa31T97uAcoFy13EEofGsvTB0i4wIMChtWZkM37KwPJ4we6TF0sNVEQ5n_JUkzYHWAOC6qLk_tNt4z2AJztRmn5Q3kG9Khb6-XQ_SbW5viLDd0sSgEKPpSFa6arC81b32qYwMKP1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=NST3tULbUi9OV7scUUjxAnnuVPShQNy9XW1Uh-HmuAxnRQasuNsS4HIUV4wmbANoRs3bT_Lj0rl8FirZdFLe8Yd-xXppBW3SnjhpEab4x2q-v8aYNOYzs3F09f4hpD_CWUCwDBtM0Vb76Zvo1VRqZHWbETVxseQX2zXSRA3IL-7r_57FGxOmMCLTMIZqPP6PFdx0bQOYl9PIcAa31T97uAcoFy13EEofGsvTB0i4wIMChtWZkM37KwPJ4we6TF0sNVEQ5n_JUkzYHWAOC6qLk_tNt4z2AJztRmn5Q3kG9Khb6-XQ_SbW5viLDd0sSgEKPpSFa6arC81b32qYwMKP1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دیروز روسای دانشگاه تو جلسه‌ گله کردن که چرا حقوق اعضای هیئت علمی دانشگاه رو با تاخیر دادین؟
پزشکیان هم تو جلسه کلش خراب شد گفت:
نامه نمیخواد، اون گوشیو بده من بینم...
📞
«سلام؛ حقوق هیئت علمی دانشگاه‌ها رو ۱۰ روزه ندادین. خداوکیلی این درسته؟... بده دیگه... دستت درد نکنه، خداحافظ.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69468" target="_blank">📅 18:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69467">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04343db3da.mp4?token=JQ8FKBNegRTp1aLVsZc2u3dKqesYcT6iEG1w_HcwkTtIQIXgD1QYusGSQx3rr85PBsFF0OZkrN7PlCUJiwvEYkiAsSF4awReyqxmFuJhEtlSLBDI8a6JQyvJJxs-x2a4yMtDtm6KovZ6cfpiH_6Riir6QdKV_HpaZjdjlS4p1xKBlbfqtqNQJWWDFqgTdnmmWTkSEoXNnJZ4LaUUvkE2_pijL7gqgOVkXni83puB5wrVyVeXhvP0M8AifqrkfPp9syAFofN0OqXJfBiixlfYS07sWPQRcuMctn3i8D32KVSuXVt6Nd5pdx6Sq8TIrvhZ9dCHi0obu7Xt9rdNLNLCEYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04343db3da.mp4?token=JQ8FKBNegRTp1aLVsZc2u3dKqesYcT6iEG1w_HcwkTtIQIXgD1QYusGSQx3rr85PBsFF0OZkrN7PlCUJiwvEYkiAsSF4awReyqxmFuJhEtlSLBDI8a6JQyvJJxs-x2a4yMtDtm6KovZ6cfpiH_6Riir6QdKV_HpaZjdjlS4p1xKBlbfqtqNQJWWDFqgTdnmmWTkSEoXNnJZ4LaUUvkE2_pijL7gqgOVkXni83puB5wrVyVeXhvP0M8AifqrkfPp9syAFofN0OqXJfBiixlfYS07sWPQRcuMctn3i8D32KVSuXVt6Nd5pdx6Sq8TIrvhZ9dCHi0obu7Xt9rdNLNLCEYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو ای از یک طرفدار حکومت که میخاد ترامپ رو بکشه:
میرم خون رهبرمو از ترامپ بگیرم یه دهنی ازش سرویس بکنم از یادش نره
از لحاظ دفاعی یا هجومی همه جوره دهن ترامپ رو میارم پایین
حرکت های رزمی‌شو ببینید فقط
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69467" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69466">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfOiZd4hbIPMw-Aq_qgFA9z8Acq7BxDE_qcqT-v3J8t1UZNPf-0wKVFeiRB48EAkdgu86R4hdJY6eC566Kmh8uPf-LCp8UjGXaHWkjECRTGUPdw3wb0zO-4NVhkP-yzsM6nzOScB5jalpGEHzwnCdzuQSVgjab24CnQ7q_whI7-BVDhH7oGLXDjB24_X_8GvjV0vBoKVppadr3JL-QGia-CkcWEyioVk1ohA8_o_Ge1U8wsaKhHdvP0ZDwgCTaxmpYW1hj_4cfNj36wqm7YI3sHTPL838tx-RqXJMQj7GDMKdfHrP4gw42SOIlRbx8gfMMyds9o0Rj0ftGhke3qjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛المیادین به نقل از یک منبع ایرانی:
ایران در پاسخ به آخرین پیشنهاد آمریکا، با بازگشایی تنگه هرمز تا پیش از پایان کامل جنگ مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69466" target="_blank">📅 16:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69465">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z06cxnWnBBNMikYcrmbWTSSTG1oWGE0bxXepJrj9Z4cEa-SvRlaYuku1_q--UOvLAY2LP8qyuWWe2YT6xcMYXHenMXGLN6vunpPaer0jXpmV6KfvyI1f2HbgG0PNnqnioVvEKUwk4oKutX6r6IBYPQtU94YPxqwzmBB6_IAebkfYiC60lczXi3XJRm1KbyTD2qZMHliXc8_faTwPPbj-uOcMUpvce6vLKTah-Fc1RdkxEFEX1Q2fn5TVE7V93kqr9Nzx8T8i4SimpQI2M51l30SKZv__yELZPOIxIGpptScPOOEPXVek2A7mozQO_0-nmq007722Z9AAC70ouhKePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست میانگین IQ کشورهای مختلف تو سال 2026 هم منتشر شد
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69465" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69464">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863fff3357.mp4?token=dQUpO7nEQ1q6FFPphyIx8FtzKJwizJdfnZDGVVkdHKwOu8U1jt63wF7naNIRG-V2bSYVYv1Er-lVD7Eww3xs-XJBX5O0GAutwGU4TE-c2Fl0ktC9WgmJ_lbJAbU1bvQeBLnIayf7iVsaySdeE35YXEfxULLsjm-iMHJQ_C-x5m00PYq4jQlQ3DvqXwnVx3K2rGci3QWQX_ZeeHOX6rDBTf-uuwlBQFFIFaS50--KfEFfCVcKs059sS_4FhNlRdiQYpZBHDVdERHkEHt2oLQG62ZUwSiYknmUxr8_Cx3fEsKqYqmUmUdtY3p77fjjlH5BB2qDMy4FQ-s-8t7ILM_x8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863fff3357.mp4?token=dQUpO7nEQ1q6FFPphyIx8FtzKJwizJdfnZDGVVkdHKwOu8U1jt63wF7naNIRG-V2bSYVYv1Er-lVD7Eww3xs-XJBX5O0GAutwGU4TE-c2Fl0ktC9WgmJ_lbJAbU1bvQeBLnIayf7iVsaySdeE35YXEfxULLsjm-iMHJQ_C-x5m00PYq4jQlQ3DvqXwnVx3K2rGci3QWQX_ZeeHOX6rDBTf-uuwlBQFFIFaS50--KfEFfCVcKs059sS_4FhNlRdiQYpZBHDVdERHkEHt2oLQG62ZUwSiYknmUxr8_Cx3fEsKqYqmUmUdtY3p77fjjlH5BB2qDMy4FQ-s-8t7ILM_x8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مشهد یه دوره‌ی آموزشی گذاشتن برای افراد بالای 60 سال که توش مبانی اولیه‌ی استفاده از موبایل رو یاد میدن؛
موضوعات آموزش:
آشنایی مقدماتی با برنامه‌ی بله
آشنایی مقدماتی با اینستاگرام
وصل کردن فیلترشکن
ارسال لوکیشن
تماس تصویری
ویرایش متن تو واتساپ و بله
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69464" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69463">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda203069a.mp4?token=sUR6kVdgEq7uoYejuvg8oQRFdihmeHmJvpZ4sZfnRdNZ7zmV94WJVBOI1xGkj4TYWDG0q3ZRTmvvlIoYGZeDh2XPnVBoJtxGejym5Q7W9hv0iocfEKXd4bEUidIZz6UOm3_Wroekyr_syhKu-mzu7ZTW3mJerUtBiVsz8F4bd074MhQhC8KcL0ABNjDi4Dads9VNQqAACbxpOs557PeY40NnHySalIK2jwc6K3bEGsO-SsMovVnxWxzVWYRxYB_On2ZNYgDYx7ATNILbv1oQPT9GtjoMGqg35zsAw7R0xRNczVp_ae2hNmRj5An8T2HFMn1IYWrZfUYuPsI0JMA8CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda203069a.mp4?token=sUR6kVdgEq7uoYejuvg8oQRFdihmeHmJvpZ4sZfnRdNZ7zmV94WJVBOI1xGkj4TYWDG0q3ZRTmvvlIoYGZeDh2XPnVBoJtxGejym5Q7W9hv0iocfEKXd4bEUidIZz6UOm3_Wroekyr_syhKu-mzu7ZTW3mJerUtBiVsz8F4bd074MhQhC8KcL0ABNjDi4Dads9VNQqAACbxpOs557PeY40NnHySalIK2jwc6K3bEGsO-SsMovVnxWxzVWYRxYB_On2ZNYgDYx7ATNILbv1oQPT9GtjoMGqg35zsAw7R0xRNczVp_ae2hNmRj5An8T2HFMn1IYWrZfUYuPsI0JMA8CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
میزان شانس بقای جمهوری اسلامی از زبان مراد ویسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69463" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69462">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b293a286.mp4?token=Llv-sCGlvt2Tbbrb8jIg5lrAevNsqvXFvADuOh-CN0sMe8vPMvsC4JFHihbFy_IdxETdowEeaHyDVIg9knL7O25SX4u-ZE5UPFeH5NHub7xsVV2mCGCkcnSiQC1K4BDO-rOBeRgPUTvwXgEDXNLfrsQaKNts78Bz3VRnmxmcdntN30PLQ7Tdn9LL_qnjvfTS0XsF9eI_jLtSrYEXRTm_9H1XZbXKKw-WopO3usO9DKBiNCq7sf5LWUI_MpCHasvybzDB40EvAkLDAw6KJSAyfAIdgpT6AJor00XqldG4irUbKwDAPzAaiXz7rlYuweDaNK3WgZM_Fra5xbgF6mIfhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b293a286.mp4?token=Llv-sCGlvt2Tbbrb8jIg5lrAevNsqvXFvADuOh-CN0sMe8vPMvsC4JFHihbFy_IdxETdowEeaHyDVIg9knL7O25SX4u-ZE5UPFeH5NHub7xsVV2mCGCkcnSiQC1K4BDO-rOBeRgPUTvwXgEDXNLfrsQaKNts78Bz3VRnmxmcdntN30PLQ7Tdn9LL_qnjvfTS0XsF9eI_jLtSrYEXRTm_9H1XZbXKKw-WopO3usO9DKBiNCq7sf5LWUI_MpCHasvybzDB40EvAkLDAw6KJSAyfAIdgpT6AJor00XqldG4irUbKwDAPzAaiXz7rlYuweDaNK3WgZM_Fra5xbgF6mIfhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعترافات عبدالباری عطوان (تحلیلگر سرشناس جهان عرب) رو شنیدید؟ کسی که همیشه به مواضع خاصش معروف بوده، حالا لب به اعتراف باز کرده و از کابوس کشورهای عربی پرده برداشته!
عطوان در تحلیل اخیرش (مارس 2026 )به صراحت میگه:
اگر پسر شاه (شاهزاده رضا پهلوی) به ایران برگرده، با توجه به اتحاد استراتژیکی که با اسرائیل خواهد داشت ،ایران به چنان قدرتی تبدیل میشه که تمام کشورهای عربی منطقه باید جلوی عظمتش زانو بزنند و عملاً به نوکرهای ایران تبدیل میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69462" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69461">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=DStIy1PcIHlZcNUDQlnljD21evzJpwsreL9a2GjWWQSuwEgNIDnDh27Rln5hKUQxGGzMDe1keSL8H5jys8Bij1elTrlo2Yzh-MOZBRcGf6FclLYUtbi0blPMhC_B-XyjFUy9dsDYZToDcH6Bpgs_vx0g3_H7Yxk941Go3byqhbiTRrHkyXHpx6G4OkH7iME1eTAm1HzfiFhFphuwlOhBSqY1zZ9dnEkeGO7t8CPIKM7jvscC_Uj4DlQqGlwww21CcdWen9f-K6F1Efb2EGaBDs3B47LljYUCWFPFto7dPAXdE1rG697_biPsxc6v4u8zOJ5xQv1ngXA0pyXUjAl9Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=DStIy1PcIHlZcNUDQlnljD21evzJpwsreL9a2GjWWQSuwEgNIDnDh27Rln5hKUQxGGzMDe1keSL8H5jys8Bij1elTrlo2Yzh-MOZBRcGf6FclLYUtbi0blPMhC_B-XyjFUy9dsDYZToDcH6Bpgs_vx0g3_H7Yxk941Go3byqhbiTRrHkyXHpx6G4OkH7iME1eTAm1HzfiFhFphuwlOhBSqY1zZ9dnEkeGO7t8CPIKM7jvscC_Uj4DlQqGlwww21CcdWen9f-K6F1Efb2EGaBDs3B47LljYUCWFPFto7dPAXdE1rG697_biPsxc6v4u8zOJ5xQv1ngXA0pyXUjAl9Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
عراقچی داره میره اربعین و ماهم توی تهرانیم.
دوشنبه مذاکره ای نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69461" target="_blank">📅 13:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69460">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
از فرصت تفاهم‌نامه و لحظه‌به‌لحظه آتش‌بس نهایت بهره‌برداری انجام شد
در این مدت، واردات تجهیزات جدید، تعمیر و بازسازی سامانه‌های آسیب‌دیده و همچنین تولید سامانه‌های جدید در دستور کار قرار گرفت.
پهپاد‌های جدیدی که اخیراً از آنها استفاده کردیم نیز حاصل بهره‌گیری از فرصت ایجادشده در دوره آتش‌بس بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69460" target="_blank">📅 13:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69459">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08375903ec.mp4?token=lmpEokdN8Ls3C-mwMtMWt7YVgKqWudUw-YwD5pxvw-J2dz4DRaYYwryPvFmsuJijDSWidrB6ogAjqk9_HXrL6ilfs2SdCrWdyyrqVDYP6yP2EJlrXRKnHk4VPrS_-hl1QWtBvNtRxSxwhLcG2gl9ckvEe6KC3PpKsvQIs-WWlMQNmWIKLShvKdamPnwQV0R7lBb56pPUdCFXdyxZWKGyVAJJNkxPR1CWd0Y4-G5gUdx3XM0oKKy_3qvZAQaJ6nPBWXcSlY76YQIUhvTv28E8g3VPr9daqSVC5rn4o6tH7DU4mEvjup5wupwYXWFIXe-qjkOI7NTficy1z1ed6WDi5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08375903ec.mp4?token=lmpEokdN8Ls3C-mwMtMWt7YVgKqWudUw-YwD5pxvw-J2dz4DRaYYwryPvFmsuJijDSWidrB6ogAjqk9_HXrL6ilfs2SdCrWdyyrqVDYP6yP2EJlrXRKnHk4VPrS_-hl1QWtBvNtRxSxwhLcG2gl9ckvEe6KC3PpKsvQIs-WWlMQNmWIKLShvKdamPnwQV0R7lBb56pPUdCFXdyxZWKGyVAJJNkxPR1CWd0Y4-G5gUdx3XM0oKKy_3qvZAQaJ6nPBWXcSlY76YQIUhvTv28E8g3VPr9daqSVC5rn4o6tH7DU4mEvjup5wupwYXWFIXe-qjkOI7NTficy1z1ed6WDi5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نیروی تفنگداران دریایی آمریکا ویدیویی از تمرین‌های تیراندازی نیروهای خود منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69459" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69458">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olEqAjx_lJfaTKOt_y9n9Wqam85C3TNWRyxQQaPvyr2FDFSLt2I3ml31T_JsoRBpt69j6CCDa4BD1r4C41MsEwhzVkDijXr3KbaxVz2mpd0hU6FJJTmKzysJVBQTvVMGuRwRC3ZTeGOoXWtF9yrc2EjxEZqenInnrxGNmTzrJhP5WNivpe1aiFX3ni8Afjx4mSkY-AvxLRotix5xAS4hnAgpkiLB7jxtIZY2VK0nwJ9Ch81Z27RUaw54VrE0vIjg5wHQUlgF-_D_xmNM7IGGap4L-R7Qr0azL1Nm3mEuMJCPeyvYwr1MCofAsNtwLv-VpYWhfIr3oUuxYgg82I3YmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی، سخنگوی وزارت خارجه:
ما در حال حاضر هیچ‌گونه مذاکره‌ای با ایالات متحده نداریم و مذاکرات با عمان بر دستیابی به توافقی پیرامون عبور ایمن کشتی‌ها از تنگه هرمز متمرکز است.
هدف، تعیین مسیری موقت است که ایمنی کشتیرانی در تنگه هرمز را تضمین کند.
تا زمانی که محاصره دریایی و اقدامات ایالات متحده ادامه داشته باشد، هیچ تحول قابل‌توجهی در وضعیت تنگه هرمز رخ نخواهد داد.
🇮🇷
اسماعیل بقایی، در واکنش به ادعای جلوگیری عربستان سعودی از حمله آمریکا به ایران:
اینکه همه کشورهای منطقه اذعان دارند که از تحولات و شرایط آتی منطقه متأثر  شد، امری مثبت است.
جنگ ایالات متحده علیه ایران، جنگی علیه کل منطقه است.
طی پنج ماه گذشته شاهد بوده‌ایم که حضور ایالات متحده در منطقه، موجب افزایش ناامنی و بی‌ثباتی شده است.
طبیعی است که کشورها برای جلوگیری از تشدید ناامنی تلاش کنند، اما تجربه نشان داده است که هیچ‌چیز جز قدرت و توان بازدارندگی ایران، مانع دشمن نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69458" target="_blank">📅 12:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69457">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=KEHmIN7S8UxyHg9l5u1yYE6YcHG_9fCLcFJ0YIVPLs145ljmi1f_Y8rwH9kcU0FKWDHyzq9ooIOmJCM1Bvp7_3eXtUmYJZHDobVb8CSiobQgVYJtwfOe2dzT7l9zC96yZHOl_7WngeksyzYBVXvEK4yqMfIDKAz_Js0h8YFU9IWYMqxuFAseMb7ceiaAISAEdemIjp4ZxmeM7DzomTGq9zJRv4sORLjbvu-gXLPRs-EKkanAyff5gFw06aEltIVaPeUUDUbxczV71r88cVapFRf3CnmzA82ajuiNtc17Z5s0_6tGQ1BYl9fvmA8LfXVcGfwTeAvEpkhKmEmU8qkyfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=KEHmIN7S8UxyHg9l5u1yYE6YcHG_9fCLcFJ0YIVPLs145ljmi1f_Y8rwH9kcU0FKWDHyzq9ooIOmJCM1Bvp7_3eXtUmYJZHDobVb8CSiobQgVYJtwfOe2dzT7l9zC96yZHOl_7WngeksyzYBVXvEK4yqMfIDKAz_Js0h8YFU9IWYMqxuFAseMb7ceiaAISAEdemIjp4ZxmeM7DzomTGq9zJRv4sORLjbvu-gXLPRs-EKkanAyff5gFw06aEltIVaPeUUDUbxczV71r88cVapFRf3CnmzA82ajuiNtc17Z5s0_6tGQ1BYl9fvmA8LfXVcGfwTeAvEpkhKmEmU8qkyfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله پهپادی روز گذشته به مرکز لجستیکی عظیم شرکت وایلدبریز (Wildberries) در نزدیکی سامارا.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69457" target="_blank">📅 11:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69455">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTIV6HKh4UPzWsnS09LE-KuasCH7cTKpptpvHE-8ykEgzNf2Dit84P1q6QNf7joKM5YlLpBg5XrpWLzFsMVDJDYThiiwanu02a4NJIM2crq8yGRKXr5p8BKSUsmmhNnM1h4nvOZ5FJzEQ4nBmmokiuOgL_0LsFfD0YHvowHn-mSHezbREWf00EXiywk04ZIbIE73ztMuC5qWO8WpzXcbkuNzz1jLAcrEsztYQ4rKoZ6xhOebARQ25oeNXj_SYFNqwcewbjI0X7ze9Q5Dpm4YVXycwKoTb-wlX5oHoTlCnt059T1m9MNlYY362Xy-8E4KPsC3crAeje9hIwHk2Of8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=I0LQ0vdqQTYW3wh1QqaSBZ8xmctT8-JbXED3oqwr4cEokgjWXVt439LuX6RkX6GTrdQGZIY1xrAgpr_VJJkJGOLFyx1IrCKA9BmyPQaErZ1Zs7jI_ktgu6fdjOXSl6s9rzVeYYzwDpYTUUPtGWftj4r-2ij7QJXVur5t4cWaZ0rvqP4b3M-_9rp84S9xHRbzRvP2Uimo1ZUg1OsB943dp88wJlNKRV-JHVov5fhDpfGlYkPf5O68pHBYxxDYKzqg7YKMHU6g1DbhlQo0ZK1H5hgKM8K3vIZFPB1FialjZGvd42-o7Cp39e_ZRn8TCw7k0N8Mz2qXpMkJhUx_w12fsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=I0LQ0vdqQTYW3wh1QqaSBZ8xmctT8-JbXED3oqwr4cEokgjWXVt439LuX6RkX6GTrdQGZIY1xrAgpr_VJJkJGOLFyx1IrCKA9BmyPQaErZ1Zs7jI_ktgu6fdjOXSl6s9rzVeYYzwDpYTUUPtGWftj4r-2ij7QJXVur5t4cWaZ0rvqP4b3M-_9rp84S9xHRbzRvP2Uimo1ZUg1OsB943dp88wJlNKRV-JHVov5fhDpfGlYkPf5O68pHBYxxDYKzqg7YKMHU6g1DbhlQo0ZK1H5hgKM8K3vIZFPB1FialjZGvd42-o7Cp39e_ZRn8TCw7k0N8Mz2qXpMkJhUx_w12fsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده مردم در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69455" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69454">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=BtIOhcPU5Qp0VsxRjHp3kernRMfQsvT07spzMDu2XaAOhlj7X-OoIRmixhPhqQareLYX9cv_U1cJ7GtxeWz0U5_QX8aIPxeJsifCoQLb1EKnBBXV3dXjxhfBh7Cu_Y_4BNFHqdkOIolUR2rSBV4JXqiC9S437dLHzD1FFjccTYNh6quW239bSZesbIsX-5GQ-_dclr--Onr2REgeMDYF3CVmiITn7ryDwqxykYjjevdxxFFODs5U57DuvKi0cj11I39II6o7FIO_5KCPjlGdgAd9DwzIrSSYiXEK8iVh7LviPk7XA6kMY3ogIyo4B5QVpnAWQ8Jg8dchKxFP0GVzDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=BtIOhcPU5Qp0VsxRjHp3kernRMfQsvT07spzMDu2XaAOhlj7X-OoIRmixhPhqQareLYX9cv_U1cJ7GtxeWz0U5_QX8aIPxeJsifCoQLb1EKnBBXV3dXjxhfBh7Cu_Y_4BNFHqdkOIolUR2rSBV4JXqiC9S437dLHzD1FFjccTYNh6quW239bSZesbIsX-5GQ-_dclr--Onr2REgeMDYF3CVmiITn7ryDwqxykYjjevdxxFFODs5U57DuvKi0cj11I39II6o7FIO_5KCPjlGdgAd9DwzIrSSYiXEK8iVh7LviPk7XA6kMY3ogIyo4B5QVpnAWQ8Jg8dchKxFP0GVzDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای ازجواد موگویی که توی برنامش داره خیلی شیک و مجلسی جای همه فرمانده‌ها و مسئولان رو لو میده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69454" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=Um6moJbZkUmOu6aWocqVrXBYNOE3G_XkiKLOQH3bJOre209_-X6POKSSGEH1uGzD7jjhUEEuaa3L7N--sQXYNXsKZuH3267z_BQonsIymkyopQQgLyTN5iOErUC4DhYmiM53IrXPNq9aG62EwIR0wifETmtPr0MlRQh07op1l9LgfdXQzfXcOHIkJ1jzXyWdJeEueq7OvcQxYFmxSfad8j1HtpsneA2rO7WydvhvWtPs9CQlxAuewMUHMvQhdK3WrzKOJ8PmcDV_UQ6jdN4SsGff_YJPXahAP3aIAqvG2fItce_n2NIHMFUW0fX-thpbpbr4jlqOEUi5T-cC3LPy83PmPDyofr3CSGvlddAKS-RxApDfEJUh3h05qSkeNt8YXQC8pYSVVDeQGbgDCwLtIF9oGJhFo0FWuOy99gOf6wfDwK9bKcfTCwbyJBO3bhmbFjoM1c8L2Ptwtj2vVNmpKWf6Y8C33A4vbmFRq4dZyyvpkBALTGrA38qTJ32Wwdotkq19SCzdjrjnTl5-yAtO15uMnonE5qyEa4GYYEtWcz7S8KGfhGf7U8pKe6hB9xr6_r1E9nLPwnDtY293IjasdbNNlyZD1mws18E0RJjNJ2m_uZOO9VntLawDr8h1125dT6UVHvWbbL32Eli-kWO_tUp6Rx0N2J5o75UygtLB53k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=Um6moJbZkUmOu6aWocqVrXBYNOE3G_XkiKLOQH3bJOre209_-X6POKSSGEH1uGzD7jjhUEEuaa3L7N--sQXYNXsKZuH3267z_BQonsIymkyopQQgLyTN5iOErUC4DhYmiM53IrXPNq9aG62EwIR0wifETmtPr0MlRQh07op1l9LgfdXQzfXcOHIkJ1jzXyWdJeEueq7OvcQxYFmxSfad8j1HtpsneA2rO7WydvhvWtPs9CQlxAuewMUHMvQhdK3WrzKOJ8PmcDV_UQ6jdN4SsGff_YJPXahAP3aIAqvG2fItce_n2NIHMFUW0fX-thpbpbr4jlqOEUi5T-cC3LPy83PmPDyofr3CSGvlddAKS-RxApDfEJUh3h05qSkeNt8YXQC8pYSVVDeQGbgDCwLtIF9oGJhFo0FWuOy99gOf6wfDwK9bKcfTCwbyJBO3bhmbFjoM1c8L2Ptwtj2vVNmpKWf6Y8C33A4vbmFRq4dZyyvpkBALTGrA38qTJ32Wwdotkq19SCzdjrjnTl5-yAtO15uMnonE5qyEa4GYYEtWcz7S8KGfhGf7U8pKe6hB9xr6_r1E9nLPwnDtY293IjasdbNNlyZD1mws18E0RJjNJ2m_uZOO9VntLawDr8h1125dT6UVHvWbbL32Eli-kWO_tUp6Rx0N2J5o75UygtLB53k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مارک لوین:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69453" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998caf4317.mp4?token=MDKFn19x_138zbWShyxzO_vFxwUDubvwSxpULiyLukTfar706oERCtG1Qk_FgsN7DLl5gkwk2QQwh1RH4Rnkl_iH5rV30TslPjpmIyARPvQRQExaRqo5lyfCp3eewtHNJWBt2P4Qk8mavlJWK_RSFIB14ALSKdP-4M8KDh0IQ_Ry0pgV4luw_CRmFQq8vUwtU4x9VgpQI2VmxxPCxEHAvtLpTWPz6Ewb667TK6Ptab9d3nuphjNCy5CMjG1Q_oPDIlXrMdX3KhHqxaBDFcc62X_vX4FPI8UAQY1izuko1F-_t7FAkJmK333z3igu3o7nMwcKhWD95A7m74g5zd_wuVQ00_qamTmxAi9jBLPVOgaAX4DBwv_w4pihDJLCb1JWb8boo2aaUV4gQziPyw8huWwUNnWgEpJMaGDrqwJqk9mUlBLVSzPen1LLafSSaEuHll0OvLDx0Of5mFm6Wtw5FHboCNn6n5oEYh_UsfUxV5s1Td13UUY3PCzIdaEjHs3CSb0K3Wpx7j811yUYI1yXK63s4U7kxd4ZNM102d4VBxEO4j6dLJKHl59srfu7pY_ta-t8njOMSZhpp2SHVwbs81o8w_F9HGsKE0Xvhjt4V4wDLwTN7s1MD4MvKEnF8DRTtGYkPf4j65J0LwJEyRRKfI8Ya2-A8Y_wXmmReoGKDXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998caf4317.mp4?token=MDKFn19x_138zbWShyxzO_vFxwUDubvwSxpULiyLukTfar706oERCtG1Qk_FgsN7DLl5gkwk2QQwh1RH4Rnkl_iH5rV30TslPjpmIyARPvQRQExaRqo5lyfCp3eewtHNJWBt2P4Qk8mavlJWK_RSFIB14ALSKdP-4M8KDh0IQ_Ry0pgV4luw_CRmFQq8vUwtU4x9VgpQI2VmxxPCxEHAvtLpTWPz6Ewb667TK6Ptab9d3nuphjNCy5CMjG1Q_oPDIlXrMdX3KhHqxaBDFcc62X_vX4FPI8UAQY1izuko1F-_t7FAkJmK333z3igu3o7nMwcKhWD95A7m74g5zd_wuVQ00_qamTmxAi9jBLPVOgaAX4DBwv_w4pihDJLCb1JWb8boo2aaUV4gQziPyw8huWwUNnWgEpJMaGDrqwJqk9mUlBLVSzPen1LLafSSaEuHll0OvLDx0Of5mFm6Wtw5FHboCNn6n5oEYh_UsfUxV5s1Td13UUY3PCzIdaEjHs3CSb0K3Wpx7j811yUYI1yXK63s4U7kxd4ZNM102d4VBxEO4j6dLJKHl59srfu7pY_ta-t8njOMSZhpp2SHVwbs81o8w_F9HGsKE0Xvhjt4V4wDLwTN7s1MD4MvKEnF8DRTtGYkPf4j65J0LwJEyRRKfI8Ya2-A8Y_wXmmReoGKDXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇱
🇺🇸
ویدیویی جدید از لحظه بمباران خیابان فردوسی در زمان جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69452" target="_blank">📅 09:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKrZNEF3ox3SipdRoHHbdYqEe7MJwCOirDfF1_zc_MGUwas7ijWHCxyqVwMPaOjAZEvqtJcHclD-GIFCLnyOcldEdXLbn1GDqIq6KooRe84CPHZ-dyAdYtbub0XtF6RBdHEUziLebV12dF3mkJw6WxCln_RV1DfA1p0BCYPKEE7sDUl70sBc8ccIAkda5bsWaej7zcbuBkzd85mghAiCY2jDKk9Aw8CXxI-sdYXPyue1m34va4hytTfqPFnWQemiL6c6B6-0EjqLqnmmv36kLAaOoWqmgoahsKZa8QxrZ7KVF40qftn6iXASiBxJnfyWg2ip-ggpXrYSE3Js-GAPXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هگست وزیر جنگ آمریکا:
واقعیت.
وزارت جنگ آماده‌ی حمله بود - و همچنان آماده است - در سطحی که از جنگ جهانی دوم دیده نشده است.
قفل و بارگذاری شده(آماده اقدام).
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69451" target="_blank">📅 03:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LLL7fqcXvtjwUNif0vjBvEcg8lDRxkgH6dVqiGBMrg4dTNUOTMH8ZKD70zoaHbweV1IkKobGCdIwyNokeySRB_KG_mGF_9Q8Ye4v9TaS3GAYvAkthlq2seKTRgfTETO5sTNJmWLRU2ju9vIUxoRsf7xaQvMnvOcUGrksSA7zFJ9yovknFQoA3xhTuojqXyjPpw6n7esm6wKK80rR_87wsi8KVmu1KhQzk_APsuOVf1s9VKSNrUv1iJJic43RVUNgcosZ7ObEnOiixQrUMbaQfhVk0UgsN9No6zATZRwtJk-XXVI7qkvEnG2Zk1Vhm4ng1NmyFKUm1fsApnvt5S1eDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پست جدید کاخ سفید:
به ترامپ اعتماد کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69450" target="_blank">📅 01:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gluAB-TWwtVHNoku0A5MK0GzaplC7ulsCI70QVtC60JKjSe-8g1mIesysoJYuy5gSipg0-yCyOz51yLGU8pdbwO6n2mXC69JLKQNouOZNsVV64z5LQRxfxi-rBSonbR-Fdygh1DkDAPLaA_YUc4QZ1KqjssehMlL1OaQYm5_xuBZEKDFbpMWrvd9xrirjQPGo3lU21xp9CY-DbM8hifywPifMG7jEP_ErziOyLXVCM-9KjjZjOGMY-U6TytUInZQGSLK9WSFIFT3q8WQSlS6GaZmyXGgmNXUt7fJvIl_LP9nL352Cb7E1iCkOPSFluqSWSOajSl8erhEsn2dEskP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرقی خصبِ عمان دریافت شده است. مقامات در حال بررسی موضوع هستند و به شناورهای حاضر در منطقه توصیه شده است که احتیاط کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69449" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
وسط حرفای ترامپ یه کشتی تو تنگه هرمز هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69448" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=ucUpBd3nu5eqgC2eE79o8dKkbFFgjw-h36XaxNeXLTVm7Ygqq6ouWFXvqn7HdSfribVRbRBrRrS54KZqNyKC6n7NQW7cWb9W1WrCD7M_Bc-4ZtJBal4Oeypkx_m-pHUAKFRvWcVoqGkD2Kb9Yy_4O9mpMSZZy1s_S8ZMRyTuIlzwmcAEeeFnFj-kQdgSLCFcpUO7EQD-Yz57RfVevdn4PP3fgahO_x5jY3wp-DPupEU224_ExdS4K7T1BF24buYqXSZuI6M20I92toKTReIngF5TiBzLAoNMjM85nux1Cxc6-YmpP4rS_htE57UkQ0klgdFRWf5r3__--pF6e25KpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=ucUpBd3nu5eqgC2eE79o8dKkbFFgjw-h36XaxNeXLTVm7Ygqq6ouWFXvqn7HdSfribVRbRBrRrS54KZqNyKC6n7NQW7cWb9W1WrCD7M_Bc-4ZtJBal4Oeypkx_m-pHUAKFRvWcVoqGkD2Kb9Yy_4O9mpMSZZy1s_S8ZMRyTuIlzwmcAEeeFnFj-kQdgSLCFcpUO7EQD-Yz57RfVevdn4PP3fgahO_x5jY3wp-DPupEU224_ExdS4K7T1BF24buYqXSZuI6M20I92toKTReIngF5TiBzLAoNMjM85nux1Cxc6-YmpP4rS_htE57UkQ0klgdFRWf5r3__--pF6e25KpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
نمی‌دانید این حملات به کجا ختم می‌شود.
منظورم این است که آیا همسایگان ایران با هجوم سیل‌وار جمعیت به کشورهایشان مواجه خواهند شد؟
یک فاجعه. اتفاقات بد بسیاری ممکن است رخ دهد.
ترجیح می‌دهم توافق کنم. به دنبال کشتن آدم‌ها نیستم.
آدم‌ها می‌میرند؛ خیلی‌ها می‌میرند. ما چنین چیزی نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69447" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=qAA7-iet1JSHXz1kLHYiRuJ4CqjChjKuENORwJVHmoK7B1n7zmDlvHeTI0oEkU_osSWcvGNzqQxOMPbTqLiwVOARyqobvYhcT-hKCjfW9WJ5ZM0IKoxSoKwuva-09kPYgx6DL1pP8pK333IOKO9tgdPNiiZt6OKKUrUpH9G7G4Zzsyn74aHaLtnIdeXr9KTThrG6pThKI0jEDHeLawq0WYcCZInCYKWFnMqMRd-4HRrTXTeAYBUgosv87RPLmIhp9rPufmkB3QweghNb9_x1V2ACnfz5pYpd3VlAJnRK5MhQXoK_nQaL5RC0skAuk9VAwbONxau-smLJVoGuFRT9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=qAA7-iet1JSHXz1kLHYiRuJ4CqjChjKuENORwJVHmoK7B1n7zmDlvHeTI0oEkU_osSWcvGNzqQxOMPbTqLiwVOARyqobvYhcT-hKCjfW9WJ5ZM0IKoxSoKwuva-09kPYgx6DL1pP8pK333IOKO9tgdPNiiZt6OKKUrUpH9G7G4Zzsyn74aHaLtnIdeXr9KTThrG6pThKI0jEDHeLawq0WYcCZInCYKWFnMqMRd-4HRrTXTeAYBUgosv87RPLmIhp9rPufmkB3QweghNb9_x1V2ACnfz5pYpd3VlAJnRK5MhQXoK_nQaL5RC0skAuk9VAwbONxau-smLJVoGuFRT9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست.
آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69446" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=MtiT-vKNsE-DGRphXdyaG6QpgkY59cqAFrY1bzW31XyfKt7nLa_sIhz_UwRHMja1AkCpTqlh_PKsQD60dvOIRcP47NFzz0YJPXDFjAmA9UIt_07OAuCbdOhfn-bqKJDGU41qNlb3f6Fcc733SI8HPgnO_2ZmPDLt3dtmx9n0BZe2qPuTl92lIvpvXWjxYxRsU-dMc--MzGnCvv_QzLM_fpaHkOOr0104B1unVUQYGWOJAbm17m3E6sPLrm8P92ysKdrXkR_GsMZm1wcGjwCEqZDwR4IGtpSihAwUfC2aM2_04Nq1M0h6gTNo0fcTDloXC_-BUgUy2E8lZ5wPiTuV5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=MtiT-vKNsE-DGRphXdyaG6QpgkY59cqAFrY1bzW31XyfKt7nLa_sIhz_UwRHMja1AkCpTqlh_PKsQD60dvOIRcP47NFzz0YJPXDFjAmA9UIt_07OAuCbdOhfn-bqKJDGU41qNlb3f6Fcc733SI8HPgnO_2ZmPDLt3dtmx9n0BZe2qPuTl92lIvpvXWjxYxRsU-dMc--MzGnCvv_QzLM_fpaHkOOr0104B1unVUQYGWOJAbm17m3E6sPLrm8P92ysKdrXkR_GsMZm1wcGjwCEqZDwR4IGtpSihAwUfC2aM2_04Nq1M0h6gTNo0fcTDloXC_-BUgUy2E8lZ5wPiTuV5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایه‌هایشان هم همین را گفتند.
ما فقط می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69445" target="_blank">📅 01:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=dKdGCvEXtXq2qDwfwJump4KVkIuXI5oOXVktKfOjYsfJXKhd0aay13gnZsPwGOAdU6dn7byJocM0VWSzHNs0twfe8Uz0oNtB-1SEtYSSSMvavI6_tnAsJ4xS2sdwPaBQ-MUBaCbKfrAesz0h0sIP9KonlYoGFYiCdj9u2xlKNrJjkJQODjodd9-47lUE6QHxwsGLLaT3Njw04cCcSObhtaJWpjnALh9wS2jWqxq2dFqVhTWPICJCpyKq2nRfu3N1QCKNLsMCxEut1fANIzvDgx8GrmEfGk22gB0BJLEhuCUKbchwyidH8TnCT3nGouDb0ECq4ZSkdrSTGJ8ir97HoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=dKdGCvEXtXq2qDwfwJump4KVkIuXI5oOXVktKfOjYsfJXKhd0aay13gnZsPwGOAdU6dn7byJocM0VWSzHNs0twfe8Uz0oNtB-1SEtYSSSMvavI6_tnAsJ4xS2sdwPaBQ-MUBaCbKfrAesz0h0sIP9KonlYoGFYiCdj9u2xlKNrJjkJQODjodd9-47lUE6QHxwsGLLaT3Njw04cCcSObhtaJWpjnALh9wS2jWqxq2dFqVhTWPICJCpyKq2nRfu3N1QCKNLsMCxEut1fANIzvDgx8GrmEfGk22gB0BJLEhuCUKbchwyidH8TnCT3nGouDb0ECq4ZSkdrSTGJ8ir97HoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره بمباران ایران:
گروهی از افراد هستند که خیلی دوست دارند من این کار را انجام دهم—صرفاً انجامش دهم—و گروه دیگری هم هستند که نمی‌خواهند من این کار را بکنم.
🎙
خبرنگار: آیا ایران برای دستیابی به توافق ضرب‌الاجلی دارد؟
🇺🇸
ترامپ:
خواهیم دید. من به دنبال کشتن مردم نیستم.
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
🎙
خبرنگار: گزارشی وجود دارد که می‌گوید شما در حال خارج کردن نیروهای آمریکایی از کویت و بحرین هستید.
⏺
🇺🇸
ترامپ:
نمیخواهم در این باره اظهار نظر کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69444" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=mVNqKg2UhaFuUSz0zw17laKN1TciwBPXKBLkA4EWBUxCWFlyQB4aWjYHAlgu9NG5PanNT_E3zcFq06BAJ9Id4wnae5dQW6yYXrJbyCQ7ca52e48dS-pQYdpxSfLfJmgWYYfSGytaI2UEGPBCHzP0IGaUSF9e3ha0KkAGTi_dZA9wRFoaJ17jCYnoaOzbfUTlYI1t-pZCaADeqmnn0AHULkRKfHLJntSGAKP0gRkKRfpWOlKKPTJackzJUCh5o0RixU689DkS58lqVUHpEOlGSO_iSiaO1rREAVbGZZ6d-zXyWdLXXhrGRN84IZxIS-6v4VX88IwoNAa-JgoW7Mp9vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=mVNqKg2UhaFuUSz0zw17laKN1TciwBPXKBLkA4EWBUxCWFlyQB4aWjYHAlgu9NG5PanNT_E3zcFq06BAJ9Id4wnae5dQW6yYXrJbyCQ7ca52e48dS-pQYdpxSfLfJmgWYYfSGytaI2UEGPBCHzP0IGaUSF9e3ha0KkAGTi_dZA9wRFoaJ17jCYnoaOzbfUTlYI1t-pZCaADeqmnn0AHULkRKfHLJntSGAKP0gRkKRfpWOlKKPTJackzJUCh5o0RixU689DkS58lqVUHpEOlGSO_iSiaO1rREAVbGZZ6d-zXyWdLXXhrGRN84IZxIS-6v4VX88IwoNAa-JgoW7Mp9vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: در مورد ایران، حالا چه پیش می‌آید؟
🇺🇸
املاکی:
ما در حال گفتگو با آن‌ها هستیم. این گفتگوها از بعدازظهر فردا آغاز می‌شود. این کار جان‌های بسیاری را نجات خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69443" target="_blank">📅 01:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=AmJUA5gDQQSgjGx4pjpzurvzLq---PIsSpgSxXPHPw8fOOgPNVQpO4XixlemQ-Qt8s1wm-Yx5LJg2TbF63Wtrd9ez2VSS3Oi4Mpg-a76yDHQcZ9CqcWuMOBfVMnPEMe58mfy0KKdrqO_-V3BwwzyuJoIeF3zAyj4rBig02ffyy4VMJYbQMZNF-DyNRFKsqcl999TZ_pH_LhYq7xOEs9ALNst1LrlE6B2RNSRo5MFa7ccyPCYRQwhwHsp9HYE8jlr6Z9TDoMEiByIoGN9T-5PEozybUWaTqnCG3y-42fQ_VaHWhKaRSf8NxUVwQPmd4s3kqZt-Z5VWRVwQnRdVjQxzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=AmJUA5gDQQSgjGx4pjpzurvzLq---PIsSpgSxXPHPw8fOOgPNVQpO4XixlemQ-Qt8s1wm-Yx5LJg2TbF63Wtrd9ez2VSS3Oi4Mpg-a76yDHQcZ9CqcWuMOBfVMnPEMe58mfy0KKdrqO_-V3BwwzyuJoIeF3zAyj4rBig02ffyy4VMJYbQMZNF-DyNRFKsqcl999TZ_pH_LhYq7xOEs9ALNst1LrlE6B2RNSRo5MFa7ccyPCYRQwhwHsp9HYE8jlr6Z9TDoMEiByIoGN9T-5PEozybUWaTqnCG3y-42fQ_VaHWhKaRSf8NxUVwQPmd4s3kqZt-Z5VWRVwQnRdVjQxzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد ایران:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند که حملات را متوقف کنم.
حمله بزرگی می‌شد.
وقتی متحدان خواستند که آن را لغو کنیم، باید گفت: "خب، ببینیم چه می‌شود."
متحدان فکر می‌کنند که توافقی حاصل شده است. توافقی در مورد هرمز وجود دارد و توافقی در مورد هسته‌ای خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69442" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=besU869bgsdMX3a2eooZ2gVG2XlOeCXrCUk4FB-_xw76a9lHImEWSMDmAMyTgMsJ_FCuaXWLGJHS0kzwY5mwlmOjx13d0ZHWUmtHRuGfEOjreTWghNTsg-5iMciBIgeKK7JoPRbXt4MKbQrJZABBSAmlAvKnhCTxnMgA18OzWQTh5UogurqP1fNVVb-UX9cn17bJ9x1bMhnhY_ApzqetxZpxpoBg2J9z6NBfbpjdfeuKI3z4li2-B2KTNIY6m6x_VZXpDOoi0DjgpFRIqNnejb6qZwI0gCkY_kqBkS4f1IPQvmrzdWBV2BqCgcMP1wUhsLNsNdPQR2pJ_7XJCXUIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=besU869bgsdMX3a2eooZ2gVG2XlOeCXrCUk4FB-_xw76a9lHImEWSMDmAMyTgMsJ_FCuaXWLGJHS0kzwY5mwlmOjx13d0ZHWUmtHRuGfEOjreTWghNTsg-5iMciBIgeKK7JoPRbXt4MKbQrJZABBSAmlAvKnhCTxnMgA18OzWQTh5UogurqP1fNVVb-UX9cn17bJ9x1bMhnhY_ApzqetxZpxpoBg2J9z6NBfbpjdfeuKI3z4li2-B2KTNIY6m6x_VZXpDOoi0DjgpFRIqNnejb6qZwI0gCkY_kqBkS4f1IPQvmrzdWBV2BqCgcMP1wUhsLNsNdPQR2pJ_7XJCXUIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی وقتی می بینه دلار شده 190 هزار تومن و آب و برقم هر روز قطع میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69441" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93362f281c.mp4?token=LrDMk5OwywtitxG4KWxJOLH0CGaKjG4wSvS4gYwZ0Vnk77VvCrHDN6yE02Y4Omi-QQkoGHI6WTF6WK1E-C7TD-RdEzbos6AXL8QbnGyaSgX0iv7dI9FCAEYC47jG8U2bSyeDhPxCHBY7DqxJ8wOvfWPPcgKuiRIM5GICS8WhMWw4h-YgyQtpFCub5Zw1-aC8Omu0xfsG2irDYj77GMta4--Br_UUoDh7UucAqL_6WLQZtbogQy8r4vQAGxIfClq99IFVhpqo5USfoaCcSoAlVoFm_O-lWSCZcxUSTWcKSR1S9Liu3MBVCnZR0izWD-d1buaSNRwtg-bJhZpPbMFSWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93362f281c.mp4?token=LrDMk5OwywtitxG4KWxJOLH0CGaKjG4wSvS4gYwZ0Vnk77VvCrHDN6yE02Y4Omi-QQkoGHI6WTF6WK1E-C7TD-RdEzbos6AXL8QbnGyaSgX0iv7dI9FCAEYC47jG8U2bSyeDhPxCHBY7DqxJ8wOvfWPPcgKuiRIM5GICS8WhMWw4h-YgyQtpFCub5Zw1-aC8Omu0xfsG2irDYj77GMta4--Br_UUoDh7UucAqL_6WLQZtbogQy8r4vQAGxIfClq99IFVhpqo5USfoaCcSoAlVoFm_O-lWSCZcxUSTWcKSR1S9Liu3MBVCnZR0izWD-d1buaSNRwtg-bJhZpPbMFSWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
شوت برنده در مسابقات قهرمانی باشگاه بدمنستر! از تمام کسانی که شرکت کردند، بسیار سپاسگزارم.
من با امتیاز 70 برنده شدم و از این بابت بسیار مفتخرم، زیرا برخلاف سایر شرکت‌کنندگان، زمان بسیار کمی برای تمرین دارم، زیرا تمرکزم روی مسائل دیگری است.
این را "استعداد" می‌گویند و من آن را دارم، در حالی که آنها ندارند!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69440" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmlC9BsKxmmyiWw37FKXrafVP79kll8N4e-rD4avA9jvxPwccbjOCv2JDDVJFii3XbyieqfpIfoiOLnhcdrQ4xO_qFytRmr8OwKfGxKaNuWsdLVbegUkhJGrf8ofR7ni9kPZs-ZTaZqfy574HP8_NCmxQoHE6CLyJJvberhfodwuNxAB87AzcErTw-DbqEsr6I_3FlqkelwKTHkvTC2GHarhl0mX6sTx_F30T4lDnzPsWd5FtSVkQmCS8PSPAT9AHsee5Ri_6mW1XNSq9oRYCKGD_UK3r_qKFaLbZ9n1bJdFi-sQVhGgSMocqrzGy329s5pyN9inkvIhVjV4CqKdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پزشکیان:
تفاهم نامه که امضا شد حاصل خرد جمعی اعضای شعام بود
این تفاهم نامه ثقل روابط خارجی ما توی آینده هستش و باید دشمن رو وادار کنیم بهش پایبند باشه
امنیت کشور و منطقه و هم‌پیمانان با این تفاهم نامه ارتقا پیدا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69439" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69438">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⏺
شکار و هدف قرار دادن ۶۷ سرباز روس توسط مولتی روتورهای اوکراینی در اطراف پوکروفسک
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69438" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=XVRKghBLMtiVefIvNiWNx0hjVFKGrbuMjTtgySm1yup8rYakiElCbpkWIZHPHRg7qw9HmSj55R4MOxk1Es2oMDCZ7HLb90Gf_U4LM2fS8f1ozOxOrgCf1GCER5Rg1DGPaClj-7hmmiz7d4XaTgtCdtdC4ft1J0UbjoiYi1tSO5Od434uD1xm3C-s4DNLl18BeeKEkv7xLWxCe85VNiJi5CjNe-Td3ZCYLHOWQO1E1_Ch5MQaH2iFm3w6RYOejtilLG23I7HxiXnNPqTHFqMSPqxrd50VMVP5rRJhCEF9yuO1zohMrnwdo7-k9hdKGTT073qUOj4NakAUS6Jz9Z-Bt4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=XVRKghBLMtiVefIvNiWNx0hjVFKGrbuMjTtgySm1yup8rYakiElCbpkWIZHPHRg7qw9HmSj55R4MOxk1Es2oMDCZ7HLb90Gf_U4LM2fS8f1ozOxOrgCf1GCER5Rg1DGPaClj-7hmmiz7d4XaTgtCdtdC4ft1J0UbjoiYi1tSO5Od434uD1xm3C-s4DNLl18BeeKEkv7xLWxCe85VNiJi5CjNe-Td3ZCYLHOWQO1E1_Ch5MQaH2iFm3w6RYOejtilLG23I7HxiXnNPqTHFqMSPqxrd50VMVP5rRJhCEF9yuO1zohMrnwdo7-k9hdKGTT073qUOj4NakAUS6Jz9Z-Bt4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
‼️
روح الله قرهی رئیس حوزه علمیه:
«وقتی ماهواره به فضا می‌فرستیم، می‌توانیم سرش را کج کنیم و خود آمریکا را بزنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69437" target="_blank">📅 22:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69436">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKbjKHq3K_Axz4H6aUulNBOVInWXF0Wc4dihYKC7-L99UcZT1rrsDzFVFv-dSHwDc6xFU6m3AImrGZ7Y5mB0dtg7f4NWgLKVPxvy153LH8IjPEDvzyl9vjLyf-IMukvkmXze5NiyNfMgeDq0BZUd11jQWHx_mihO70yG9t6TEdUe9l5aTR6upy061mSn_HGXYfcQ1tG3ByXJue0m4qVASSGBpeLlfJc47or877Y3ht_GcA8Xg07eKoWBT0IwZWTQ7BMOlIaY5OcDYch75Tr_o8YHHUHSF250mt5mi4dU1HhGOTj8-xljm2OHlRfnnzVGNqmptZfWWBNU5uq6a5BOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کان‌نیوز به نقل از یک منبع امنیتی:
رفتار دونالد ترامپ — که منجر به لغو حمله گسترده به ایران شد — به توانمندی عملیاتی آسیب می‌زند و آن را تضعیف می‌کند.
این مقام امنیتی گفت: «این دومین بار در طول یک هفته است که ایالات متحده اسرائیل را در جریان حمله‌ای برنامه‌ریزی‌شده قرار می‌دهد که می‌توانست خاورمیانه را تکان دهد، اما آن حمله در آخرین لحظه و بدون هیچ توضیحی لغو شد.»
یک منبع اسرائیلی نیز افزود: «با وجود رفتار رئیس‌جمهور ترامپ، آماده‌سازی و تدوین جدی برنامه‌های آتی دشوار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69436" target="_blank">📅 21:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69433">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/G6Dlm_cFITKr7BbZlnVb6VwH0gmqB_Js6m40Iu5SQEs9IIDSL9071C4LiS2rxM-rqImoBE2y_2qNb27MqiXSurUn4vq2BMt1yTl6TgjyYxQN2QzYdq5_Aus62CT8qfV10FtEE2NMzP-MolcBjtE73EZoAODxL1EpvXPNR5QD6i7qzsGKuThAY6FfOCtEXYfxYRzXaMkj5YMH_ZPuydDmbnuzIOArCph_TdMW3lwcGPLBXX6Z76jZNNT8bjdVpcADKbW8tlX4wgUgXIoGHZ0xSi2wBU2IJSEjTRpg17XDbpynGRH-dCO21ZzYmisGG3PwTIqhPIw4UAHgA-EVN10QqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=OQhcakRrJwex1VTrx8tNHDqpnEwT24mYC9H5xwrR_t68aNjPgCfPdFLwDzksW1ypkWlehGeTMZWGMjILyg5TJZvJbA6vym8AhKyf_W-jVgoD3pT8shb7qEpgcyQJaAvKYAwN5Man8YIiWT1BSO5vCdc_Fd3Yiq8HTCu45_9lnZO7wkmVBIfxFhj_-6mZuLD7Znp9ptxWwr_OESHzDLJRlnX2F4093a1ejLjjIaKaOw1jPFeU4g_QSJkz0yoUb8pz2Cpa0GCIQo3IRSQ6Ujj198MGGn3TGAjWImQrv2GWB208nsvALuvRcPZpKkhl8ak6mzJ8BrgBZmdnLDygsTpGSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=OQhcakRrJwex1VTrx8tNHDqpnEwT24mYC9H5xwrR_t68aNjPgCfPdFLwDzksW1ypkWlehGeTMZWGMjILyg5TJZvJbA6vym8AhKyf_W-jVgoD3pT8shb7qEpgcyQJaAvKYAwN5Man8YIiWT1BSO5vCdc_Fd3Yiq8HTCu45_9lnZO7wkmVBIfxFhj_-6mZuLD7Znp9ptxWwr_OESHzDLJRlnX2F4093a1ejLjjIaKaOw1jPFeU4g_QSJkz0yoUb8pz2Cpa0GCIQo3IRSQ6Ujj198MGGn3TGAjWImQrv2GWB208nsvALuvRcPZpKkhl8ak6mzJ8BrgBZmdnLDygsTpGSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انبار شرکت Wildberries در منطقه سمارا دچار آتش‌سوزی شد، این اتفاق پس از حمله اوکراین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69433" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69432">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5208110eae.mp4?token=Xa7FtluvUbzFxmIEsWJK1i9Iv1IqIY_E-pMvIhPE9wxSzND6ELb-gnXbVAN-oGhPbNvXWPiCjBto4sHf37NbBPCpLYrcTOly_Dm1HGEbEkDmMZ-aH5p_RC6l0qQG9PmrtJq0v9bILgH-zeSua7C96i4dORs0HDdSsYXajHKmOd2kH_gsENoZ5Ia-pwWH68zsxLvcKPXRNZataoVHrQ1sa5fXbOH0v_n09gcQYRzMrAzxdZ10zPMQ5mfIFmhtraUNH7p8AnyLthGC5nxrU5AB5e7g15KNjZnORFB_ao6Fok5RxjXbXklBY9Hz09CuE710cfVTuwx_1bUQiCtKe8j71g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5208110eae.mp4?token=Xa7FtluvUbzFxmIEsWJK1i9Iv1IqIY_E-pMvIhPE9wxSzND6ELb-gnXbVAN-oGhPbNvXWPiCjBto4sHf37NbBPCpLYrcTOly_Dm1HGEbEkDmMZ-aH5p_RC6l0qQG9PmrtJq0v9bILgH-zeSua7C96i4dORs0HDdSsYXajHKmOd2kH_gsENoZ5Ia-pwWH68zsxLvcKPXRNZataoVHrQ1sa5fXbOH0v_n09gcQYRzMrAzxdZ10zPMQ5mfIFmhtraUNH7p8AnyLthGC5nxrU5AB5e7g15KNjZnORFB_ao6Fok5RxjXbXklBY9Hz09CuE710cfVTuwx_1bUQiCtKe8j71g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی امور خارجه، اسماعیل بقایی:
مدیریت آینده تنگه هرمز توسط ایران و با مشورت عمان انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69432" target="_blank">📅 20:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69431">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04acf28261.mp4?token=D_0effkMGHSFQk5dLN0oavIghzlmfQaUJ9CeR05HSinY-hdwZDxG_SQYadnNjgxsM7FLz2TJQnEDSvPp6P-6oDPjs7m9usyZChCf6cZ1cCjoduNQ64SXyJ6Jly7n2m8yChkEwOrAuXbWdIgdA59VdltOks_ckdFQq8-Ahi4niHFJHphRWOZOOU-ryY3ajHIBpdHyHAiD5t_kqacKz_FMzDa_xAxbjC46kgnkkWnunQGE5CW-fiJdijjy5ajF8g3J8BXoxZgUQQ3r1H0mcpQSAt5SbISlJmdISDTNsDDgofm7kUUM4GB9GNrbyK3cnpddx7lLYrLGWow75uVgL3HPhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04acf28261.mp4?token=D_0effkMGHSFQk5dLN0oavIghzlmfQaUJ9CeR05HSinY-hdwZDxG_SQYadnNjgxsM7FLz2TJQnEDSvPp6P-6oDPjs7m9usyZChCf6cZ1cCjoduNQ64SXyJ6Jly7n2m8yChkEwOrAuXbWdIgdA59VdltOks_ckdFQq8-Ahi4niHFJHphRWOZOOU-ryY3ajHIBpdHyHAiD5t_kqacKz_FMzDa_xAxbjC46kgnkkWnunQGE5CW-fiJdijjy5ajF8g3J8BXoxZgUQQ3r1H0mcpQSAt5SbISlJmdISDTNsDDgofm7kUUM4GB9GNrbyK3cnpddx7lLYrLGWow75uVgL3HPhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی وزارت خارجه اسماعیل بقایی:
توافق ایران و عمان بر سر مسیر جدید هیچ ارتباطی با بازگشایی تنگه هرمز یا حفظ بسته بودن آن ندارد.
مسیر جنوبی از طریق تنگه هرمز با ناامن کردن منطقه و آسیب رساندن به منافع ملی ایران همراه بوده است و تهران آن را نمی‌پذیرد.
مسیر مورد توافق نه مسیر شمالی و نه مسیر جنوبی فعلی خواهد بود. در عوض، مسیر جدیدی خواهد بود که هر دو طرف متقابلاً بر سر آن توافق دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69431" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69430">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=V9bp7YghVZLv_ZiMcBpmdCe7oFv-rVVHJWPsNv_CFX9e5T7feJpFLJ8mlUHVAQCOjdjg5x32Kskh0a0D6JrVMJjVp5jZEV7r3VkIimwoD3ORLjZr3mNFEEVtnX9yifNOzzVbjqBQDgyck-crYOihr3XVv8jVy6W-6aAHo0Ozk936r0xpJWLOXtjB6OlhgeNpcGvZXAhx9i3IszljPN3ejz2NdQcaofJs3dNRFdjG4n-n0OEMvTyOa9lexNNE5QCLXO-im92S3AehZ1tWj_uq3Brje2Bc_f8fIA0hsto_E8GTuiUQPPNXqbQUthCDoPtSseW4LmSgAPZ4Zij5F15qEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=V9bp7YghVZLv_ZiMcBpmdCe7oFv-rVVHJWPsNv_CFX9e5T7feJpFLJ8mlUHVAQCOjdjg5x32Kskh0a0D6JrVMJjVp5jZEV7r3VkIimwoD3ORLjZr3mNFEEVtnX9yifNOzzVbjqBQDgyck-crYOihr3XVv8jVy6W-6aAHo0Ozk936r0xpJWLOXtjB6OlhgeNpcGvZXAhx9i3IszljPN3ejz2NdQcaofJs3dNRFdjG4n-n0OEMvTyOa9lexNNE5QCLXO-im92S3AehZ1tWj_uq3Brje2Bc_f8fIA0hsto_E8GTuiUQPPNXqbQUthCDoPtSseW4LmSgAPZ4Zij5F15qEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کارشناس صداسیما:
مسعود رجوی (رئیس سابق مجاهدین خلق) فرد باسواد و کتاب‌خونده‌ای بود و قطعا خیلی باهوش‌تر از رضا پهلوی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69430" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69429">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=M9k94gCHnWGPLjfc6AmeoVVgGgxjxl7he0Pj7KgnNVVSr_rorGmn94D7j7N0tCLgEeZArAzN-OIZgCWr9C-pYSGcBW1BXBt-lqmKhTu1SPC45lFnpgtz0sQEB1L2PwxAGXSQcscuMs2C1ctEfQdo8Wt8lqxC6P8JbvnFrL7Xatpe93dYPrar_oEVmQ0j51mfGHFJlkKoldqY8tghFEidP_ZY6z_g7Uq0YrwVyH-VT2ZZQXCVvPdjyjVv1rQtztAnPO4cl4ylPGZkHszCO_WsUe54yT_9EEQTId8XiCmcbVgVzPMwhbAPxBwd-Vjzvl16ekDe9ymjvr01aDI2BclUHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=M9k94gCHnWGPLjfc6AmeoVVgGgxjxl7he0Pj7KgnNVVSr_rorGmn94D7j7N0tCLgEeZArAzN-OIZgCWr9C-pYSGcBW1BXBt-lqmKhTu1SPC45lFnpgtz0sQEB1L2PwxAGXSQcscuMs2C1ctEfQdo8Wt8lqxC6P8JbvnFrL7Xatpe93dYPrar_oEVmQ0j51mfGHFJlkKoldqY8tghFEidP_ZY6z_g7Uq0YrwVyH-VT2ZZQXCVvPdjyjVv1rQtztAnPO4cl4ylPGZkHszCO_WsUe54yT_9EEQTId8XiCmcbVgVzPMwhbAPxBwd-Vjzvl16ekDe9ymjvr01aDI2BclUHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
من یه مشکلی برام پیش اومد که گفتم نمی‌تونم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و غلامرضا رضاییان، رییس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69429" target="_blank">📅 19:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69426">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=ikWIi426q5OuDU49EcBWRKELbgO8Rgu5bJ0bQ6VJp76y8oQiBSG-ZFl0lk9HTdvT_vGMkKzTfSRXMmfC6jBVRUmiN1c88bDr6VdNEmR1tM2YSIUb0fdjMPp5J2oUhok9JXiscXVIru5g2a7GC5HUbuiEAlCS9DwGMPUkXEvtDx2H2iNg4Kjy8FduWfJg31wMwj30TGEzTZlfPBU7u2M5FYIRj8SWJ98gbQM2afP4eAKRf-vWwZi4TC9XNVrBmZAXYkwDIefvd-CNOopP8cTkazldEOwQu5ffh48siHPX6-VeR7jZ8fMkR5L-XUCmXAf3Z60E4272pJzaR6etVxt_JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=ikWIi426q5OuDU49EcBWRKELbgO8Rgu5bJ0bQ6VJp76y8oQiBSG-ZFl0lk9HTdvT_vGMkKzTfSRXMmfC6jBVRUmiN1c88bDr6VdNEmR1tM2YSIUb0fdjMPp5J2oUhok9JXiscXVIru5g2a7GC5HUbuiEAlCS9DwGMPUkXEvtDx2H2iNg4Kjy8FduWfJg31wMwj30TGEzTZlfPBU7u2M5FYIRj8SWJ98gbQM2afP4eAKRf-vWwZi4TC9XNVrBmZAXYkwDIefvd-CNOopP8cTkazldEOwQu5ffh48siHPX6-VeR7jZ8fMkR5L-XUCmXAf3Z60E4272pJzaR6etVxt_JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💋
🇮🇷
این جنده‌اینستاگرامی که خیلی ماجراش وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های
🔞
عجیب منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69426" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69425">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=Do7lV02c8yT8_pnQsct9-UnSyO7oEcgZNbvDmb4mGHx5pXXkRiQK_c5cA8cGvYE4s59Daa4BXHnbQWXfMwA141xkQWxfgN7ZCt7TeL5f_nVCWL0tQmNlHiEfxEH3HMLvJNn8hBgq9PG3GaC64Gq2PU4ys23H_tpT-PPMLaW6E6_s7m-8mJ8JABTwBVZrSRlNMQg6VcPIrnoY7zj6bG99CRcO96QayedqpJXc12Ykes3IPeh5c66UFfZeKjOumXETVZy4MttJGcbl8oj271pXJZu8DoN14STXOAKA01Oe3260alUG3MeRauz1IXKN3lMN5q0mWZhn1iMUaEs05h9CTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=Do7lV02c8yT8_pnQsct9-UnSyO7oEcgZNbvDmb4mGHx5pXXkRiQK_c5cA8cGvYE4s59Daa4BXHnbQWXfMwA141xkQWxfgN7ZCt7TeL5f_nVCWL0tQmNlHiEfxEH3HMLvJNn8hBgq9PG3GaC64Gq2PU4ys23H_tpT-PPMLaW6E6_s7m-8mJ8JABTwBVZrSRlNMQg6VcPIrnoY7zj6bG99CRcO96QayedqpJXc12Ykes3IPeh5c66UFfZeKjOumXETVZy4MttJGcbl8oj271pXJZu8DoN14STXOAKA01Oe3260alUG3MeRauz1IXKN3lMN5q0mWZhn1iMUaEs05h9CTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند پناهیان به پزشکیان و قالیباف:
همه پیامبران را مسخره کردند؛ از تمسخر نترسید و با عظمت صحبت کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69425" target="_blank">📅 18:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69424">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇮🇷
بیانیه سپاه پاسداران :
انتقام خون رهبر شهید و اسماعیل هنیه اجتناب ناپذیره
پاسخ این جنایت بشدت سخت و قاطع و سخت گیرانه خواهد بود
توطئه خلع سلاح حماس به نتیجه نخواهد رسید و از همین الان شکست خورده بدانید
دنیا بداند اراده ضد صهیونیستی ادامه دار خواهد بود و پیروزی نهایی فلسطین خیلی نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69424" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69423">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=CHkBqsHq4f3sGvgJKgDCbJ_PqXonXnccAlKOLdEq9cyO2xV-j10aq0fsXl5I9S2c5hz15w5X5RY8DnsbT8kInX4_uTrsMk51uYqRrGhqKJfvVTRSiFZ9JwYtFTDvYcMvi46D1KOA18z0ca2UxXIaJ-acctSFXVS23RD2hEj-csikoeiuCgHXmtTmhP1rfw-W-Wcc9oDiiVBD4nR9sVDd_yHyOLYBr_vqrXtyo2e2R0JWV3wFvmU-b_I77xV98Y-J3_Eq8haBBVzfhUX5lgu6Lk8szROT-_ge-kSxNWAdYBGsWML5aBAFv71rGJhi6zRcqm9PI_6a73gf7RdCrAQlGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=CHkBqsHq4f3sGvgJKgDCbJ_PqXonXnccAlKOLdEq9cyO2xV-j10aq0fsXl5I9S2c5hz15w5X5RY8DnsbT8kInX4_uTrsMk51uYqRrGhqKJfvVTRSiFZ9JwYtFTDvYcMvi46D1KOA18z0ca2UxXIaJ-acctSFXVS23RD2hEj-csikoeiuCgHXmtTmhP1rfw-W-Wcc9oDiiVBD4nR9sVDd_yHyOLYBr_vqrXtyo2e2R0JWV3wFvmU-b_I77xV98Y-J3_Eq8haBBVzfhUX5lgu6Lk8szROT-_ge-kSxNWAdYBGsWML5aBAFv71rGJhi6zRcqm9PI_6a73gf7RdCrAQlGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو هلیکوپتر آتش‌نشانی در حین مبارزه با آتش‌سوزی جنگلی در نزدیکی پساتا، یونان، در هوا با هم برخورد کرده و سقوط کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69423" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69422">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=sxVcB_ZPYlCROCgi_IxDMSVwFt232erUeCUGQWTaxYL6i7kWWYYtpRwioo-cNizSVovxX74oaE-quen0nKuq8e5IHyFBdfCNd2VmiWjgGR0RKNej5K8Jtd8lVyl28n_Pv2ayw9fgwWV69-jNJzR4FvyVnGCL1TefsVe4F7yIefEsRxUWhNwgrIHJxMmwevKzhFhWR0L222uHhi17CRdLbwMpFC3xI-47VMZ33bJlTs1ZTof5mlYEPVaFeXv0evqyfv-2MpLKIlZoSkwHvbbS1yq13yUIfck-CQdtodjS3jdlRBccUnFZ4tlqrNKfKHyfnZskExxTEOgCMZl6nlb0Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=sxVcB_ZPYlCROCgi_IxDMSVwFt232erUeCUGQWTaxYL6i7kWWYYtpRwioo-cNizSVovxX74oaE-quen0nKuq8e5IHyFBdfCNd2VmiWjgGR0RKNej5K8Jtd8lVyl28n_Pv2ayw9fgwWV69-jNJzR4FvyVnGCL1TefsVe4F7yIefEsRxUWhNwgrIHJxMmwevKzhFhWR0L222uHhi17CRdLbwMpFC3xI-47VMZ33bJlTs1ZTof5mlYEPVaFeXv0evqyfv-2MpLKIlZoSkwHvbbS1yq13yUIfck-CQdtodjS3jdlRBccUnFZ4tlqrNKfKHyfnZskExxTEOgCMZl6nlb0Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی اینو ببینید توی پخش‌زنده صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69422" target="_blank">📅 17:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69421">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLljrvSD_Vy5A-Xn5qelAuadZMWgC4bHZ2uBJi_HUU_6yk5Zh03QnTIg-sUmvp4nIX5cSN9z6mqRlX49GfFuQwQIrefmiwlpLFCg_3fkKkR7faMalNX_AGdIekzff8Eo5gy5nbHJiosPzPdG9VKD-aT7GKtMbyhuWCu-GPhtRYEohbqG4pea3uHgkS7Bj6GCiGTthcgTIsjEzwgLH-l8sJ-4IXko0xjSspi2J63zxf_BjJ1Kkci2WTrA6br765iVbl6AMm3QQbGou42pkHwXxeSVrPzgQIgx1gBjn84CXTk-CMZMOOXExAaW-O81P_w75SgUrVwiRmhVlugDlTi_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
نیویورک پست:به گفته منابع آگاه، در حالی که رهبران اعتراضات در تلاش برای دستیابی به سلاح هستند، انقلاب ایران ممکن است «هر لحظه» رخ دهد.
چهره‌های مخالف حکومت در تهران به نشریه «پست» گفتند که خیابان‌های ایران به دلیل اعدام‌های در ملأعام، فروپاشی اقتصادی و جنگی که بیش از پنج ماه است ادامه دارد، به مرز انفجار رسیده‌اند.
یکی از رهبران اعتراضات با اشاره به سرکوب بی‌رحمانه ماه ژانویه توسط رژیم — که به گفته رئیس‌جمهور ترامپ منجر به کشته شدن ۵۲ هزار نفر شد — گفت: «انقلاب ممکن است هر لحظه رخ دهد؛ مردم خواهان انتقام هستند.»
یک روزنامه‌نگار مستقلِ فعال در جریان‌های زیرزمینی ایران گفت که تدارکات برای خیزش بعدی هم‌اکنون در حال انجام است و فعالانی از تمامی اقشار جامعه مصمم‌اند تا ضربه‌ای نهایی و تعیین‌کننده به رژیم وارد کنند.
این روزنامه‌نگار گفت: «ما در حال بررسی اعتراضات ماه ژانویه و تشخیص این نکته هستیم که چه تاکتیک‌هایی مؤثر بوده‌اند و کدام‌یک نه؛ همچنین نقشه‌ها را تحلیل می‌کنیم تا امن‌ترین و خطرناک‌ترین مناطق برای تجمع را شناسایی کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69421" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69420">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btLz0VDI5QyFqo2j_8ggU7aZ9w7o2LbfiD03kcFngCOWA0Xl7tvy7gfBv7pre2IV2Qe0k1HZPidfMDUSDEkEYD4X0hYRQxPP8oGPrJHeWd0oq2OSuseXtyyGxcE_4uUmEGpYJiWMF9IugWdz_Mk0imZEKdzO4Kta0NZgKpxu8fGOFvX2_bFbsfLewUA4f3AkL6_9DEd_McXg2KgHhKyts8jbFNAIpnkXlcgoxIWfB125fJX41PhsDN9Bn5cFEzXJZfDQGERFJkxwFP1C3JoUL4f3BPkApcpzMc4FQmYkLgrCT-4sfyueD6u1U77eXAZbJNOKBmxKgwR44yI6BFlaow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
صفحه فارسی وزارت خارجه اسرائیل:
هفته خوبی از اسرائیل برای شما آرزومندیم!
💦
اسرائیل داغ‌تر از همیشه به نظر می‌رسد... و ما فقط در مورد آب و هوا صحبت نمی‌کنیم
😉
🇮🇱
☀️
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69420" target="_blank">📅 16:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69419">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=Z3yWV87F3NHTOwC8ZRkuJf7lQBNLNGEVJMNDXOHw8-0SubZqlBuHCIIadBjvxhOsqArqMAW-shqT84pd14KD5a-59gy3SyKGWSYyLvkiYxdnqkrf-Vooosy4513jXOCB5xed5WZCXj5UxX_FloGrHxNHbGGUOMcM_HsMiYwa7pznLojeSO-lZVD89Xt9U05aqwZOLI9TzHxzUM6zTSiSbEug39NA7TLgq48s9ISHPiN8vlKaK3U6TK5TZ2tKRmkjbGGwlFXV0zaeUm-q0ijuPDljViUO5VdsTFlOHOd1r7fdYH0sS7liNl9IbyBV6jrVi-CUUtuEf0khT5c2p7rBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=Z3yWV87F3NHTOwC8ZRkuJf7lQBNLNGEVJMNDXOHw8-0SubZqlBuHCIIadBjvxhOsqArqMAW-shqT84pd14KD5a-59gy3SyKGWSYyLvkiYxdnqkrf-Vooosy4513jXOCB5xed5WZCXj5UxX_FloGrHxNHbGGUOMcM_HsMiYwa7pznLojeSO-lZVD89Xt9U05aqwZOLI9TzHxzUM6zTSiSbEug39NA7TLgq48s9ISHPiN8vlKaK3U6TK5TZ2tKRmkjbGGwlFXV0zaeUm-q0ijuPDljViUO5VdsTFlOHOd1r7fdYH0sS7liNl9IbyBV6jrVi-CUUtuEf0khT5c2p7rBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از نیروهای سرکوبگر: تا تهش پای حکومت وایسادیم، بازم بیاین بیرون بهتون رحم نمی کنیم!
چون داریم دستور خدا رو انجام میدیم، شما اصلا کسی نیستین جلوی جمهوری اسلامی وایسین.
کل دنیا هم جمع بشن نمیتونن کاری کنن، پاینده جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69419" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69418">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f215b551.mp4?token=stN6-c3B9-4RuhAMGfO5RSEW_z0QCPMqTU36kXxPb5YwbJC_sEQVS4k11ZbSQP9LCNDrnVlPoVBbKpmbFpokU5HyAMUvZV1k9RsO3d9huRbPuuT-WNBlMCX9U63EVG5XgRAPZvIyTCHEcr25fn7eVzwj_QNgxyVziK-2vLfjlXBzZI3YsgiMelA0FSVqvvYroCetFD5Lhy5COPNaBluDZo-zjRxO2XpSm-hyQgYeBP0KXbRMqG9QZB9Y6l3rQY4bPc2vi1sO8x5434hGuXSsnrJuA27Ql2hnPlkykw6WwBQF8PKkTKZ4_RXP6vuh5nsnZQMGjix0LlP48JTxH9UwBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f215b551.mp4?token=stN6-c3B9-4RuhAMGfO5RSEW_z0QCPMqTU36kXxPb5YwbJC_sEQVS4k11ZbSQP9LCNDrnVlPoVBbKpmbFpokU5HyAMUvZV1k9RsO3d9huRbPuuT-WNBlMCX9U63EVG5XgRAPZvIyTCHEcr25fn7eVzwj_QNgxyVziK-2vLfjlXBzZI3YsgiMelA0FSVqvvYroCetFD5Lhy5COPNaBluDZo-zjRxO2XpSm-hyQgYeBP0KXbRMqG9QZB9Y6l3rQY4bPc2vi1sO8x5434hGuXSsnrJuA27Ql2hnPlkykw6WwBQF8PKkTKZ4_RXP6vuh5nsnZQMGjix0LlP48JTxH9UwBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو با اختلاف زیاد عجیب‌ترین و دارک ترین چیزیه که تا آخر هفته می‌تونید ببینید؛
هربار یکی از این خانواده رو دنبال کنید تا متوجه عمقِ نفهمیدن بشید...
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69418" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69417">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d8743494.mp4?token=v7qOkfCPB4TX9epzeo4XEwpcT3COkYR_8zDuyrCgX0pHYW2kp0JmSbAay0GsVScr3TctUAb2nybCbDwMsnR3Lped3sRtGfN6JwoARJvupG5_V86IQWPvQm9gwVIY5wBYppmcPqmwC_hdsfSxxoPX_PRayyTrv5is3K8GvhJVjz0HPCylaFB2ZRjtgTTTxMLbx5YfsQIvVvoRclVJP9ehz3dSJ-_K7JHfufPVz5Nh1FMGESyliwArJLvA80uMa6rk6cBXl6K_hb3Lnp6E_YybiUifUWX3XLEzygPb6u69ndorq2wOpmfu_RqUlMulsHOehICBjyk7uADgBL69ADWPHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d8743494.mp4?token=v7qOkfCPB4TX9epzeo4XEwpcT3COkYR_8zDuyrCgX0pHYW2kp0JmSbAay0GsVScr3TctUAb2nybCbDwMsnR3Lped3sRtGfN6JwoARJvupG5_V86IQWPvQm9gwVIY5wBYppmcPqmwC_hdsfSxxoPX_PRayyTrv5is3K8GvhJVjz0HPCylaFB2ZRjtgTTTxMLbx5YfsQIvVvoRclVJP9ehz3dSJ-_K7JHfufPVz5Nh1FMGESyliwArJLvA80uMa6rk6cBXl6K_hb3Lnp6E_YybiUifUWX3XLEzygPb6u69ndorq2wOpmfu_RqUlMulsHOehICBjyk7uADgBL69ADWPHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بر اساس تصاویر ماهواره‌ای، پایگاه هوایی شیخ عیسی در بحرین که مورد استفاده نیروهای آمریکایی است، اخیراً تخلیه شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69417" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69416">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=cIm9BSmq3_t89pJ1ngCtrOvi40FP2BB_HnBsue0ZFAf6cu5kd0tcS_gJHmfEH2ICRuyOKXd4Qw8zgUna1G1Djqki_ApA4h0ON0-1dA96RWQbHtNeRqdlCpH6K2S3xJkH18sFQZHyqBqKrq_wVHkJiHgl1McEGFAv1_fYYyLZAG4dmQS3Wte5CAmHHzpYu3ifnxXFkJg7jg0ZKHKdC0PZ-0vHQg0vW-rJJh3ZAupgntxP0l1vz1-1GHtHX5NmlGxtLlglFBkVzi7n80wMkLjCHGekqCUQEYx4rU0_ZG6jvWg52aMvZ-qtJS8i2qtNqCz5xRcI7_HRGx-G0OuGM6pkjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=cIm9BSmq3_t89pJ1ngCtrOvi40FP2BB_HnBsue0ZFAf6cu5kd0tcS_gJHmfEH2ICRuyOKXd4Qw8zgUna1G1Djqki_ApA4h0ON0-1dA96RWQbHtNeRqdlCpH6K2S3xJkH18sFQZHyqBqKrq_wVHkJiHgl1McEGFAv1_fYYyLZAG4dmQS3Wte5CAmHHzpYu3ifnxXFkJg7jg0ZKHKdC0PZ-0vHQg0vW-rJJh3ZAupgntxP0l1vz1-1GHtHX5NmlGxtLlglFBkVzi7n80wMkLjCHGekqCUQEYx4rU0_ZG6jvWg52aMvZ-qtJS8i2qtNqCz5xRcI7_HRGx-G0OuGM6pkjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر مارو خندوندی حاج اقا دارم پاره میشم
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69416" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69415">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇮🇱
بنسالل اسموتریچ، وزیر دارایی اسرائیل:
رژیم ایران در جریان جنگ سقوط نخواهد کرد.
مردم ایران در شرایطی که هواپیماهای اسرائیلی و آمریکایی بر فراز آسمانشان در پرواز بودند، به خیابان‌ها نمی‌آمدند؛ چرا که نمی‌خواستند در نظر دیگران، همدست دشمن به نظر برسند.
تأکید اصلی باید بر این موارد باشد: اقتصاد، اقتصاد، اقتصاد و باز هم اقتصاد. این همان عاملی است که در نهایت موجب سقوط رژیم خواهد شد.
به گمان من، رژیم ممکن است به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی چنین وضعیتی پیش بیاید، ترس دیگر مانعی نخواهد بود؛ آنگاه مردم به خیابان‌ها می‌آیند، قیام می‌کنند و رژیم را سرنگون می‌سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69415" target="_blank">📅 13:23 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
