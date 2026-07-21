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
<img src="https://cdn4.telesco.pe/file/hziKWeiA2wK22W0eCCwDIfYEYvGrN46JQv5JJTNpuMkZesU6G1spW-Uq0CFj8I67KPRMvPi5uPOB6Bl-tM2qWXy1z2w2wFc_ghkU8jKKU2yyATISBA923Y76mBimrlSnsPV2EI57QQBAsKWj1V8vXoBb4F3iWO6i3Et-92tnw3bEivn-MHQGja7W5EOpsFCtSiBNA1Mlvs38BIXMJNcXYv8-Ib40jzoYdznJ5a8TR7PUxPWW65UO3aNmVYD3uTCGVeUwY8eAXTW3BxjJzcA1jtecTcLNTRoHJkGBwqW9R3IiM7i6-13yFbdBh7BZHzNPUPpvle6pppxs7WAg_KLMZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 21:20:10</div>
<hr>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhspRjEojEV8PG2r8UxMAe2vctmlZ72-y0HqNMrydiGPwS8jZbSILED-odMqbiqSYhU297aANDUvknewmSHgpYV9ksrjYx80DEOOdoYzNnhdUK8HVjYHRk9YYb3XqXXl_3-J5s45HeUSH4I039dX5mxYVwpYIMMH8JStzkpuzYkDkAIBVsVFcNFOs_v3m3jk2xkkgr_a6LtMDE-WMQWsOaljOKIX9q07NCDY9ISvTLGfIR2n8kadQSxY_lq6PKOFn3QVamM56tlCszZJtcuEU3_xU57L2fTYoE83VBkKY_XeoyfCzR4WYcrljdeReExgzcC7K71tD-kwNAmB-WjQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=KIMUmB1VUCi0TCeFG3UkijWn6YAQYy_31sC9h54jnJU8rwRoV2zQfinq_ljTD4GNu9wn886evp8BXY9bYTkXX7jGdWos74I78FK3dh2G6-ky7ndMLWrjCOnlQ8JmOxcobV2JExf2PkQz0YRxsbpR7kMJNt4VmjWcR9XrdYJ83A4f6MnFctHLkT7w8jVgrmlSfspLNIp0RTSVZtOpnzEInkkgG40b0mgw_6rxlmmNbxHQDNRS5KsA37sbuPLbn-07vJM72MdMVLAB3Qlc3wivLZfGWQppFWoi05_4mkfGqAleHAjJUo9a531JKqTa8LxjXt8mHp-4Ihb5jgS--fslwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=KIMUmB1VUCi0TCeFG3UkijWn6YAQYy_31sC9h54jnJU8rwRoV2zQfinq_ljTD4GNu9wn886evp8BXY9bYTkXX7jGdWos74I78FK3dh2G6-ky7ndMLWrjCOnlQ8JmOxcobV2JExf2PkQz0YRxsbpR7kMJNt4VmjWcR9XrdYJ83A4f6MnFctHLkT7w8jVgrmlSfspLNIp0RTSVZtOpnzEInkkgG40b0mgw_6rxlmmNbxHQDNRS5KsA37sbuPLbn-07vJM72MdMVLAB3Qlc3wivLZfGWQppFWoi05_4mkfGqAleHAjJUo9a531JKqTa8LxjXt8mHp-4Ihb5jgS--fslwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=mdfQz1fW1OAcXpjG_eKBEyFU8uOhPX8bc5f7NXAGcugJR22rT_kJA3djHf6fUYyfLZBovknggf3HGxoT1rnaGRIDp0MQEir8MhK0aToaok0th5xG5iKjpxXTsCqWtv4NC2aqPVDq_u0tCmyXJCl1NCWTzlNJkWx4mVPyJupypfD4A_jgXzdhBZZOcjq1FDACArOlqx8JaN0MzZs6B5qnhVvgm2ODKH8RzULJhj1vBtzSdKdaDDW1TwIBovcMWQwGBJECVnaq0Gr7CfVP_jJAXpyORCdTn-zYk2RB8j4CAVbL2m8eeojFtgbU7iTtOsOb9FGURaB-gcZsAHcRvtx9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=mdfQz1fW1OAcXpjG_eKBEyFU8uOhPX8bc5f7NXAGcugJR22rT_kJA3djHf6fUYyfLZBovknggf3HGxoT1rnaGRIDp0MQEir8MhK0aToaok0th5xG5iKjpxXTsCqWtv4NC2aqPVDq_u0tCmyXJCl1NCWTzlNJkWx4mVPyJupypfD4A_jgXzdhBZZOcjq1FDACArOlqx8JaN0MzZs6B5qnhVvgm2ODKH8RzULJhj1vBtzSdKdaDDW1TwIBovcMWQwGBJECVnaq0Gr7CfVP_jJAXpyORCdTn-zYk2RB8j4CAVbL2m8eeojFtgbU7iTtOsOb9FGURaB-gcZsAHcRvtx9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=QJGLOtRqEQeXAGr0zyoWO1H1CJUONR_E-nl6cJbDVvthsYAZ5ZR8GUULzMWNTbxJfI_MkSFmBDXnWiLOrijZKNMqaCOInB9rYVUwqJ2ae7qEs02vRry1zIPRgB2FgqazdeGNv3ZpV33k3rzJOLZTsPDbfAFi9Rq2wsZhapNttyb0SraRvQOugHzuvqnNfocOZj1TJJL1WGVwrwBfVcLQCmTvB8GLPh8_PjgKJYARwoxBTGQj6LCP2qHk93SVQmpgDtGxioyHB-KUBmaTT1ebgvUKAqQC5kAIr1ZwkUM5aGyUZ0XETInG7AxeCVXWHB7FdD_gGotl4J7armZPdQ-Mhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=QJGLOtRqEQeXAGr0zyoWO1H1CJUONR_E-nl6cJbDVvthsYAZ5ZR8GUULzMWNTbxJfI_MkSFmBDXnWiLOrijZKNMqaCOInB9rYVUwqJ2ae7qEs02vRry1zIPRgB2FgqazdeGNv3ZpV33k3rzJOLZTsPDbfAFi9Rq2wsZhapNttyb0SraRvQOugHzuvqnNfocOZj1TJJL1WGVwrwBfVcLQCmTvB8GLPh8_PjgKJYARwoxBTGQj6LCP2qHk93SVQmpgDtGxioyHB-KUBmaTT1ebgvUKAqQC5kAIr1ZwkUM5aGyUZ0XETInG7AxeCVXWHB7FdD_gGotl4J7armZPdQ-Mhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp-IFPpLYLD6EYUN64DvswImvVuhq91JoClI4-zw8rXJL3hvZbiuuRpfrYhBkOcxG2gYwl_ZU98LSTH7aRgDZHGqRxss0axx1fOPPFkc5dDJmB6PDsXEypN8ZtjI06GRrYxyLmJJxUIEI79rCcF-W-rT-Ub-FVCMMUtfjn1pYy-LCkqST4dgCam6bchoovX97ste-e1CO_UAeXXH0X8YAZ0v3E5Nj2YssQ9_C0pyFGkFnXgbwcaoEfGnQH2LFzdZAeNqpyeBDd66oFW2rD01tkdAGX8isYX46qrKh-fZwxQH4CWyT9dCfgMQm96rCDmCyhJ6otkrwAYIvzRNhX_mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=m42MWXHAEWCHTqS2cF2gNOGt3uHT3URjGsGSXttOE2Chx_n5nCGnDJlMabVD2d-0SAJdZFeRIsQai8fxSKxE1N9mXHoNkD-0pOuOM0alm6IwsnJoWXb9TW5ZfcuJkzG4o8ieCQg4Wcq2QcyIpsAbrU9lXbEdTZcwT8HEbbxYrBluptcBUn5FMh0QNBnuQZwO2wVTihegIIHCz220rQG3br3GPcOHZE8KsrGzqaIyzrMsqyezGeW__0vK9NnNQUFel-12_6QkwtSuUYTUSvmj7PiMMGlnZg4Or9AQAiLZMk8YhLKqINarNWdvvnCJCnWGDCNI-5VPOpPUDyGbU6rquw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=m42MWXHAEWCHTqS2cF2gNOGt3uHT3URjGsGSXttOE2Chx_n5nCGnDJlMabVD2d-0SAJdZFeRIsQai8fxSKxE1N9mXHoNkD-0pOuOM0alm6IwsnJoWXb9TW5ZfcuJkzG4o8ieCQg4Wcq2QcyIpsAbrU9lXbEdTZcwT8HEbbxYrBluptcBUn5FMh0QNBnuQZwO2wVTihegIIHCz220rQG3br3GPcOHZE8KsrGzqaIyzrMsqyezGeW__0vK9NnNQUFel-12_6QkwtSuUYTUSvmj7PiMMGlnZg4Or9AQAiLZMk8YhLKqINarNWdvvnCJCnWGDCNI-5VPOpPUDyGbU6rquw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=f7fLfgYFlJalowTZgWZcTJZN-sSTZ5sESgQHdCeGg4tNiENL-XkIRvA6B6uEd7efehGU6ICJCJ4oO_HPvjf_Rr_OP7vMuNkzTYhg8ch68cnT7Bs7o1unjDDvJVHK3gmZXWB92q0PujfdBUubJNak2pLpqwRwpRnp7WUYjtB3zvOAD6g78Bfuc8Vd4-P5WMG-7rV7dlCxSei4QLs5dKTbPtnFUudWm7Z-NV6bNKHWbXdM48cnJR9_OoXbu-8qXSmDxWQaV0qUeeL8rNPPjRAI10yBLyz9i88VMfejb_4lqx52kmf_aYLh21FaR9Lh8EhSJX7u3esrh0B2S3XzlHTgww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=f7fLfgYFlJalowTZgWZcTJZN-sSTZ5sESgQHdCeGg4tNiENL-XkIRvA6B6uEd7efehGU6ICJCJ4oO_HPvjf_Rr_OP7vMuNkzTYhg8ch68cnT7Bs7o1unjDDvJVHK3gmZXWB92q0PujfdBUubJNak2pLpqwRwpRnp7WUYjtB3zvOAD6g78Bfuc8Vd4-P5WMG-7rV7dlCxSei4QLs5dKTbPtnFUudWm7Z-NV6bNKHWbXdM48cnJR9_OoXbu-8qXSmDxWQaV0qUeeL8rNPPjRAI10yBLyz9i88VMfejb_4lqx52kmf_aYLh21FaR9Lh8EhSJX7u3esrh0B2S3XzlHTgww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=ZnE4dY4ibWaGHrO7Pj55jNwfUNuMPlf7BUxtWUaids4v_cdncB2v1Gg3xCsA_gnupUL-4FIwWpkySNbRNPGYlu5faVS5quRx1sMNdkK7Cz5Kc0heehWh2jVzE60kOX-4jVwwaJWJnkARFf_Q2DDDGDoj0bnJPATQkpk1Yx90Hcnn8j8sw6oDN_0i5TYmsn0NOWjl5JcW3mwS9oN_QgvCGzwBhfoZJ6L0ulJYaMfsMSaV6jL1Z1A7MDCmOZ0-rNKSkRX2YAWH5uhkr5XnO2q8ByfivRF0Tu4C4Af0egd36Pj2q6tXkmOIagIo6qFG8YvAZdyTFpEkiYa-CFHXTi1Cww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=ZnE4dY4ibWaGHrO7Pj55jNwfUNuMPlf7BUxtWUaids4v_cdncB2v1Gg3xCsA_gnupUL-4FIwWpkySNbRNPGYlu5faVS5quRx1sMNdkK7Cz5Kc0heehWh2jVzE60kOX-4jVwwaJWJnkARFf_Q2DDDGDoj0bnJPATQkpk1Yx90Hcnn8j8sw6oDN_0i5TYmsn0NOWjl5JcW3mwS9oN_QgvCGzwBhfoZJ6L0ulJYaMfsMSaV6jL1Z1A7MDCmOZ0-rNKSkRX2YAWH5uhkr5XnO2q8ByfivRF0Tu4C4Af0egd36Pj2q6tXkmOIagIo6qFG8YvAZdyTFpEkiYa-CFHXTi1Cww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=TvWOLLfIEy2U_vkaA4KgEG_FL-Rmz1qDHMBueSPNyhcCoH_wn7W3yseuC1fSdnlCHeIEHKUHbKYMsUGxdmx_UVRJ551MB8L5IrvwndrOcLxPLlOlQRYXCyoh2LNzrPYbHzm6uQPSe--hi9ouZHBuMoEiXNG1LNqKkse3_A2D53l7k615cyiDye0E9pUSYdyo_HH3yt9jWjf1mQFO2uob9YhgK7jUqfDLR9VWXH_mTY5fo49SIXpCAEOO7Lrh8JstDiVXLeiwPesrUvpxhWJFv0fgxJIWT6Bc-25kTZB7DMG83qmSMaOlFzJk8KbMbd82WfqeKh3o86ODAV_E0XJgbKIM8_bPGZnAoclar80j--RXRZRvzpwdeeYeE3gMRxBHb6nTA3L1hsSlyS6ndTpUCM4-IN8VStPhljZzOMDdLqmskVSDEI78Pn80PlaFe-ytZgka8Vu7AOfkZ1ruQxrhd-HgBVTBTVTGpUpb3P8HCdzVvMAX3p5nvoH126sQBhzpSA7hogMnExlNKdvF8T_-TImxqOEPe0XYK-DHvIIqKExGoan9LRfIB8RyYdiq9jAuSoiFsKoNYldSJz5r0d5JwepMRofj9HrTHmeKKV-3sA6yVWH7R4NqgKNj6pfWrsi-h8peGIQJNDrLT5PT3Vx0QMRobqMTl368Kuxfjw6jv7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=TvWOLLfIEy2U_vkaA4KgEG_FL-Rmz1qDHMBueSPNyhcCoH_wn7W3yseuC1fSdnlCHeIEHKUHbKYMsUGxdmx_UVRJ551MB8L5IrvwndrOcLxPLlOlQRYXCyoh2LNzrPYbHzm6uQPSe--hi9ouZHBuMoEiXNG1LNqKkse3_A2D53l7k615cyiDye0E9pUSYdyo_HH3yt9jWjf1mQFO2uob9YhgK7jUqfDLR9VWXH_mTY5fo49SIXpCAEOO7Lrh8JstDiVXLeiwPesrUvpxhWJFv0fgxJIWT6Bc-25kTZB7DMG83qmSMaOlFzJk8KbMbd82WfqeKh3o86ODAV_E0XJgbKIM8_bPGZnAoclar80j--RXRZRvzpwdeeYeE3gMRxBHb6nTA3L1hsSlyS6ndTpUCM4-IN8VStPhljZzOMDdLqmskVSDEI78Pn80PlaFe-ytZgka8Vu7AOfkZ1ruQxrhd-HgBVTBTVTGpUpb3P8HCdzVvMAX3p5nvoH126sQBhzpSA7hogMnExlNKdvF8T_-TImxqOEPe0XYK-DHvIIqKExGoan9LRfIB8RyYdiq9jAuSoiFsKoNYldSJz5r0d5JwepMRofj9HrTHmeKKV-3sA6yVWH7R4NqgKNj6pfWrsi-h8peGIQJNDrLT5PT3Vx0QMRobqMTl368Kuxfjw6jv7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=CRbA9oe1eXeCSz_ytIQzA9lTz1UmSfYGWRXOm6vYiy1BkjccXBoPcbqkwiI-5-7vxrCkwtmSMMAKSZcUnRdd05VjWnGfb1zITElBmjpialSdb80t3qvNBv3IyCYisAtGcI71qa-uBVgI9WD-HS5p8GpaKiXQWHMUkqZ7ZsyYW-8SHxiEit9TZWceueB5JMoacY4BmfR5wjyG_w4b_0NODWdAnOq9IO_Ll0r1-Lex1OnhhA_BdhBoQ2vkJy9w9VLfTVSTHLzt_ehh7UKSKdkEJbuuaUHLJybDV4qx9fcV7k69YmNHRuBfad2C7Gee-KEG4cn6ber09n_UK7HG1DlAuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=CRbA9oe1eXeCSz_ytIQzA9lTz1UmSfYGWRXOm6vYiy1BkjccXBoPcbqkwiI-5-7vxrCkwtmSMMAKSZcUnRdd05VjWnGfb1zITElBmjpialSdb80t3qvNBv3IyCYisAtGcI71qa-uBVgI9WD-HS5p8GpaKiXQWHMUkqZ7ZsyYW-8SHxiEit9TZWceueB5JMoacY4BmfR5wjyG_w4b_0NODWdAnOq9IO_Ll0r1-Lex1OnhhA_BdhBoQ2vkJy9w9VLfTVSTHLzt_ehh7UKSKdkEJbuuaUHLJybDV4qx9fcV7k69YmNHRuBfad2C7Gee-KEG4cn6ber09n_UK7HG1DlAuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Y5FN2y2Gp3jIIqPX29_9kwh_OLN0RVeq_wBW1jwlVMgCqP1_6xRJa9rhr-QxDo2xiLCwul0h7jTmWbdOD29MmVtQO6XvnJhvKktWSGvOJxagtJckpCNipscIhUjy6AoLYxskpvvJtDqVx-u0vxRznziromuM8DozpdmqPx1GS5YGXuwnJcssUYWDKlJhO6LhdguJ4e5LPFAZ7fouwJOUVbGqEvUQggOrehIncUSU8JGuYLwUYuqtkmGGlOmkqZxtHGaFCGLxk6JvCOkR2r9Kb1r9zusQyADv1Il_AHlbXafyt1Mnz4nmf-WEGdxHmf2oyDbn6dI_UYC2TQiIZbxHoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Y5FN2y2Gp3jIIqPX29_9kwh_OLN0RVeq_wBW1jwlVMgCqP1_6xRJa9rhr-QxDo2xiLCwul0h7jTmWbdOD29MmVtQO6XvnJhvKktWSGvOJxagtJckpCNipscIhUjy6AoLYxskpvvJtDqVx-u0vxRznziromuM8DozpdmqPx1GS5YGXuwnJcssUYWDKlJhO6LhdguJ4e5LPFAZ7fouwJOUVbGqEvUQggOrehIncUSU8JGuYLwUYuqtkmGGlOmkqZxtHGaFCGLxk6JvCOkR2r9Kb1r9zusQyADv1Il_AHlbXafyt1Mnz4nmf-WEGdxHmf2oyDbn6dI_UYC2TQiIZbxHoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgwEm9Q4IwAMIWJ2eIrYpZ8KTYKw0O2SHAJ_VlQWbc1sSFk2sxgecz4nN-WgheF7OASn8w-ROE0krBsnPeH7wd4-67ArT6sLsPdpQwd9NKdC7pyjPdLr8FDoMmKaoF20OugCZOKYNlSTuiZnzm7eGpAWy-NiOxuCDtmk2bd95L6tUMd_W99JhpV5GXHXVLorI0cIwZ_DiPeUkiJGfRl7If_gRFoSfzQuy_ZXF1O1GzLOMzXF49MvJ7BXc-oF8SqMr45TU9L9OdvAd13hsLVRb1UMaXohn4PcXXlLAukShVWFgO8nTU6qHzO1mUWt-0oqkcFGAhwmnWA_KrIuVhvEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZxxCUvw4IY4Smjf28UmKzRNRjl0GFjL4z9wbfAD4ZjXv-T_KYMemi4S-DN_GrznAtrqvv-3-x8UUDHpl-YE80v7QKYrt5qM48lZQiyezO9-f1AO0BG0ILCDMIBkwryz0x_9VSuaF68Ol47Yiqcm7hQWBKpjlePx0IIBtyRWTIgMFsWakzRSUn8bCikjWg3WHQeqMJhpFSUqQjzqxCIstsrQ4FfJnGJ9dGecKVQWu91uKYbbg5O79rpUK_DIU2emNYJBgWzSXId9z4zn_Oc7PzlM48U29zw2hHxCflzg-FSInc9mg97Clkw4m1-wcrhsIlBOQSrDOumbMv9cfPqlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Y3Sq0ge5wkSXwnaCLRVbvLNob5qftXeARuCaX80EIfg0f9DSeu0eZVNrV1GZ0DTxD_qP6mK-4EIiuKnBPv49RP528AmVG6ZQ3cxjXI7FNCgkBc0pqN66wm5KItbp4QDnR_nVqEup3YBzKyQrLmZqWLuacYk5dZR8vSzfCyarIGwpxoIOBZPbiJmE4C6t2eC5Eg7ZrhZ9luUgOKhLzROVH0WzU_JA2SIJ62Jjtob65E4NGu451n8VQTZUhfzqmrRtHPfvVzfW-4m6183ztldQjsFYiu2bRBhVjNG8sJ9foV4GcXv_LWHsM1dF8eNb6JKzdtxgsxU9GwNzuK5izNWp5H9rBwTpYLLuwKMcIpE8rucgx-5o9i3KzABa9bl_p_r3IZdLS8mwJqkRkhEmXvHZO6ZKKDUs8XquKAXxIAjcf1DWVJJDoZjL-qW-qKUe7Oqd-OLWbbyPJSZJYzeuZJduCXeYFeujOZkli7wyURM14cae_E3TX_Udyc4UoQ1ZMMIR0gdZyvpiCpFAYMUvk5Ru2NYaJuWugGY92LA_8mg9n-4uvcNiRkQ2OhVzkaozFExZiI2l03VK5-4DlbD0xOPNo9eyt_OqyoOpJ_Hy3zX4nRjrIm4HF2CuFGoDk07hCj9J11_LYew-6fR_q4L43A3MQKez3hzaUORIUoD07r7ERlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Y3Sq0ge5wkSXwnaCLRVbvLNob5qftXeARuCaX80EIfg0f9DSeu0eZVNrV1GZ0DTxD_qP6mK-4EIiuKnBPv49RP528AmVG6ZQ3cxjXI7FNCgkBc0pqN66wm5KItbp4QDnR_nVqEup3YBzKyQrLmZqWLuacYk5dZR8vSzfCyarIGwpxoIOBZPbiJmE4C6t2eC5Eg7ZrhZ9luUgOKhLzROVH0WzU_JA2SIJ62Jjtob65E4NGu451n8VQTZUhfzqmrRtHPfvVzfW-4m6183ztldQjsFYiu2bRBhVjNG8sJ9foV4GcXv_LWHsM1dF8eNb6JKzdtxgsxU9GwNzuK5izNWp5H9rBwTpYLLuwKMcIpE8rucgx-5o9i3KzABa9bl_p_r3IZdLS8mwJqkRkhEmXvHZO6ZKKDUs8XquKAXxIAjcf1DWVJJDoZjL-qW-qKUe7Oqd-OLWbbyPJSZJYzeuZJduCXeYFeujOZkli7wyURM14cae_E3TX_Udyc4UoQ1ZMMIR0gdZyvpiCpFAYMUvk5Ru2NYaJuWugGY92LA_8mg9n-4uvcNiRkQ2OhVzkaozFExZiI2l03VK5-4DlbD0xOPNo9eyt_OqyoOpJ_Hy3zX4nRjrIm4HF2CuFGoDk07hCj9J11_LYew-6fR_q4L43A3MQKez3hzaUORIUoD07r7ERlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toPXHueYptr9BNc6b2ueCXVn3YoNO4R70bWxGbKPhSGkKdbq9JFCEyGsaLM-16QBoHn3oyu_PvBU9kW6WsigFIFdPiIOWaTPErFVzG47TD6xOqpL2DVRcDXEcKP90czPp-bEP0bFd1J4eaK5lJfYciumF6H1_DeJoi-xhIH9CKAXgr-HpdoUC0ZyNR_gaBCZ_bzhNW6tv54Q6fsX90RydmuBGqo4DzW67qRB7h8f8IYy0MswxxaCgA0H1sq2bJoXA3getT7UCOpRX6woPx5tpaTMxU4HaaQ-DdUkEkoXHy49tDpfoZrWlD3dabazIafYw1i64pBjxihrZvG081dLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hzs8weidHW31wa98MyyIiyg-LOVtqrP_pjExvU8fcMAxhBlb9wqGAddwnHX8g6duiD-OSzS_zimiu6skJ9YoEWAa-LDI-SqvahiZSQGnZ9EA1j6A5j0y3i0g7Wrmjbz_kA37Mixj7uYja8U7R7aaiLQju9nkNlP7dsoA08SdyzHDZ6g1v4jVUJ6dUIT-rglrbbs2QLC0C7VuhFmAeGNS3Q5vqfgKntD91aKMBkDQ3NwSQPO9uPG4w6AOYcQVLVOta9LIsXoYGNMx7qd2EeglJwBc6D_Zp_IU3j6t_t1KlRQ9ushPVumwAOM8omUcrGyudXGQU-NO4NXqwp-QPT7f-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9mPgPuXNQeJXiBSOTUdgxl_fYg7KrXAv7a9OZLsTnhlpwg0BH8qT6hovAflMOmpfYuN0rn_n9X8cbAymm_Iq-9SPxwpM9p6QLtlptTGHI48ZfV30rzpe2GUur7Lv26bhCPTFG8rc2KOO5Einy9pU_2eFA-aWj9Bmey3uv02jwCSeRfJRtSIsS1pGHsAVFRHNKs2iV3WaDqW2r6UH7L2RdkyBNAhz0vfZDJZH8E2DdeTDJ8fDaMDAjFf1XiuhviSkaWCtEn4RZ-j9NgWRdXPccDUjJobAejF3DxUAgOtOXLGG6oAI4IRTwshW0om3AymtdLgXL2AwKakgiIuBq_LIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHkAvYOjkvhZp2iGwk9oe9Is7BnIAFpQoRbb4anXLE3uUlYTqNd714s-lEBuOqtBfxEzMRfY74mxB2BSFleYCkM3nikjAwQs8In8LwBn7oeVHU7FymMc5TdJNmkjm7GMwZhS6x5vQWvhJ7zeXy01TO8Uif7v-MxccAALZHALPoSOuvqvIj8DcqZD9QUN-yesYnf3fVhWoNprtgvWS9BOQpuVKXjRK0uwXBUhlfniMRTJAh5JH96lEidymnJzLtGMA0DX22tz1kWLMl4TbllMpDq-2EMDj349aNbz2rjw3m2r6fdTBZ9mVYrC77FAhOM7mJY7aY1z00-poXO9LaLCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=JjQ2YFXvtpEUBbrkWON2ywIGWsgMme6iLiAIJEJ1MW6NtSSZ89GBKfe_ji3akPqn6Bf0b1AAo1uPIK1wv6YZuukdGTi5XcZrqS0_sLCDWjZiSwjwtcpXWU9O014KFK90v-7YPj3r8jo1DQOX7EKYyEqvd2TAhlbrIOnuFFj618GHGKTRGznLmr2PZze6Jrk8QteBMg8rAldtwbPWja_urfmIe7ihJ0uMetCO2MXzwVtJsSKTgeacCaxQMtfxL6OqkWuxw1tWU10p06fJKUqGWgSzHGjphDdcFfXj6iTospfTTMZ13Tik_BU1AemHgamHILLuVD-NVr6daFIpeQ-AsqAvqMk6lm9zfZIDORGiBgkjgZO0tnIVvxUU0ms5nLbkNKu0L3_Zy1OOW45X3fTcUAf3XxESTeSGIZbQTOoldjMZ3axKxq_ABiBnY__C_N0-AfCovlhrFVWOBs91PriRhxmQmhbRZAeKcn7TdcjxOVewJYZ9D06-r6h3AnuI8i8uaMzprF1T9tCcTRYw6RMiuQUVZgGG1W7QvpJ7Hd1H-YHA0knXKIg9wV-UCdHdMWKS6MOAWHzG43w3MXO1FYN9HjL5akMGgtlqNKH3mfBCp6GATXtAzUpmFWqw-PaOroUy6-ibMiS1b3YGeWzVf9mmdxVyxPuFUz8KKzMHZRFcSMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=JjQ2YFXvtpEUBbrkWON2ywIGWsgMme6iLiAIJEJ1MW6NtSSZ89GBKfe_ji3akPqn6Bf0b1AAo1uPIK1wv6YZuukdGTi5XcZrqS0_sLCDWjZiSwjwtcpXWU9O014KFK90v-7YPj3r8jo1DQOX7EKYyEqvd2TAhlbrIOnuFFj618GHGKTRGznLmr2PZze6Jrk8QteBMg8rAldtwbPWja_urfmIe7ihJ0uMetCO2MXzwVtJsSKTgeacCaxQMtfxL6OqkWuxw1tWU10p06fJKUqGWgSzHGjphDdcFfXj6iTospfTTMZ13Tik_BU1AemHgamHILLuVD-NVr6daFIpeQ-AsqAvqMk6lm9zfZIDORGiBgkjgZO0tnIVvxUU0ms5nLbkNKu0L3_Zy1OOW45X3fTcUAf3XxESTeSGIZbQTOoldjMZ3axKxq_ABiBnY__C_N0-AfCovlhrFVWOBs91PriRhxmQmhbRZAeKcn7TdcjxOVewJYZ9D06-r6h3AnuI8i8uaMzprF1T9tCcTRYw6RMiuQUVZgGG1W7QvpJ7Hd1H-YHA0knXKIg9wV-UCdHdMWKS6MOAWHzG43w3MXO1FYN9HjL5akMGgtlqNKH3mfBCp6GATXtAzUpmFWqw-PaOroUy6-ibMiS1b3YGeWzVf9mmdxVyxPuFUz8KKzMHZRFcSMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=lbBN2rBNjNI2HDM2fgHaUXqNJLQQYMxybtZ_2DkpMzLEqLYR8fSrroQHYXUP7DAQkfhDOb_siMNiz0OjXuOu5y1jVwPLDcAjaMCzJdOcsGlEqZS1JokuO1i9Pv2yTRSb8EoStpRffUANhAhndhfbGOEVG3T1zwxNe_p160uvmq4uDh3ubWioxKot0FoUcaxNbIn6AJRrj-zKn9KOjPKtT1FpruZbayRwPFWLvLoWOZKzr1bQbD8IohFeTNkZrjHxDdb1QevjvO4J8S3FO-T_695uKROsaCluWEUI3ENuteoAmoupstNZlvX98qHdFbWkJoyfbDB1wOp1Rwh_YoBllg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=lbBN2rBNjNI2HDM2fgHaUXqNJLQQYMxybtZ_2DkpMzLEqLYR8fSrroQHYXUP7DAQkfhDOb_siMNiz0OjXuOu5y1jVwPLDcAjaMCzJdOcsGlEqZS1JokuO1i9Pv2yTRSb8EoStpRffUANhAhndhfbGOEVG3T1zwxNe_p160uvmq4uDh3ubWioxKot0FoUcaxNbIn6AJRrj-zKn9KOjPKtT1FpruZbayRwPFWLvLoWOZKzr1bQbD8IohFeTNkZrjHxDdb1QevjvO4J8S3FO-T_695uKROsaCluWEUI3ENuteoAmoupstNZlvX98qHdFbWkJoyfbDB1wOp1Rwh_YoBllg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABbzlcY8xApE2h2X0_WJzZ0zmEIxVaEGqBmiT_8UBpTeDDCPSDVMSujZQkQkX1o4QgqXeMIYZpXWRYA6eJCcBDH2UcBVl5iKnMZy2F8-BFWiTfd_F9fQnqi30Ze90sqpPYIaN_oUt7rkIjRKc66cQ-Sa-yTc0zdsqdFQ-jOWtgfBJ_oJVSWaOhUrDQTNF8aE9kWLuxUglgkxamO2fIr7rFoSemYH7KyzDyKANEDTXgdfw2Lrs_xqahQyrGZpGmHnFZLIu7ggs7jf-1f4njJlMTnWQTHznrRUyRR2CbzuQRPFlJ_Pb3hF2mgOgwylTq38KsOz_eM_objGBHWpwibpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQSmoZEWuZyVHIIGNypanM01Su5-9IT4XAoQV2m9RQXjIZ3GX4chvGlskaN7aDI2YSrswQ78dcO_KRTqtfMqy_ZUrsPAb424wMObOdrLrYwYVenjzlUS0KjlzKuM4Z9OXOdIPH8pxZHtNkLXrRFtZBNsdI4ZB6Tzuitv6NIEaFQbSk3KGcfGCKEXYI-dcqHK4m3xTamYBWDJOtaxre9qEsJnugoVgnxHSiEd3JOBUd_Lo2_nLONeGfu45uW5IQciJk0JpRmVGnUQTKwrZD6GK2BZG9oWKYuqrnyUjH6tc0NR4cSf16SC5edE8FEECeXBqAPvZFCsVod9eQ6N3_vrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHGkDWLECpNREialmT6VarG3ItW-F9oSpJkBEDknccl5xEA5xmFw8urBJStwC3ggmTXPeykkEz3CzmWT5BlJVLUcxclNDfY3TEYbEOZ1uSvMZ1Nc4tCq6Ul5a2X04YyQBomsvRHPcLTHj01UOswWvQSrlUWGuxbZwK_t6LJ70GRtgrjFmlavUmbr0AXOalE54dGXRijf0pF6tnYUwfjYRayz42yhy3mzVrkO4ms2E4dMonTmR3mTEXeN00yZp0FlurGzpkDJ2Q_HMnLvmlDiX0zBiLRgxQhme0rsYaCf6ZYscc7YKnT3nz-NxLWf0lqTOLFiMuKjsn3U00DxtM4zsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ne9YxDMf2iyWG70RSFsNXvwqadpnee_wisKZ0Xgl-J2wlJNeSqexqnhLVU4ec0tUxfqGRZhJiDy8BGffBuJbAvJkOP1jCnU-2hgF2FVSeQY6qmjd2ngHL8U_ed1iE5rKt5QwWXzYsgepnyGKKNAlgZVz8K4O-bNrFzTex4PzeuRERVpg0fZqkF1HfQaClgLcnLr1gCB5Bv6GWrqyhP9nC259W_e3o4tqapYUqeDxywI8Sh54hlZ494kuwsLMHqy04nDx5crZIGxngbQ_WxBvKqxfBbIMuAeAt-m0PucQzFoYptLmChIeC_uQwgmlg20gtv38wBW5TfrUF68nXfwBgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN4Cdl8K7t2XPxM3W1Cl77UYrho78-j0U3wqJrz92mwX2D2Y6mydRfVtWJ2Q-8ffL0x2FwF0nCaSLzLhnGGMWEhNeLK0aJOC5bZVycm6Z9xcNf6Bf2t13_paly-i672zvDFX6kfj2uJGDeQlPBSGtz-z9RR-N4Ekugiouc7Q5UbcLftLkTWiC02RVQqNdX8OAhQ_wEnRwo6rE1F8DxS3Jxdk3KYzJb1bC6ndWhClAaGtS2lw81B9qndXw9aXd9xzL_QlPGVl77lR4DlT5-n8yRsdLr1D54cIQ3QPXBo8RMKoCihcQTLcj6SuqcBNkZ9BK4ZZcbeIswTSGmQr0PbEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgqrxmqLZsq16eC3MujokIAEM7vZanf5PLcbJSICxP59oljYbfqvVA_nGgd2Hv5h4cLwAC6RB1VNYgCvMgWd9bRmdlUCeYnC7Qr4mxAatMW4iehO4thvYieEXQcG_7qD4H7kro9yzUM1nNo11R4n38lud63RexW0_3fERbrV_RvC3VISgFfX5CeWDxgrvA72LDFPNn-WmY33Xhc70Pv1QBColrpaBB6mCfFBq9wFLOhbffmVK6Mc8y_5umCU7R8PhKrMTx5nTfTvchK62PHHexfBYQjdMEjuA8TWL2hsgr8IeIRuNyfPzj_wssOfw5pQOc6epDUD-19kmAe-CXSpOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9Yr3XWI4OCLiixrEae99nva1RzhTXv6Z8LFMO3tu_Oc0fcBVH6BTEWq3EMBxXgYckjk18MYUe_0--bfq1grbCg6ptaVHCHxZzkYH1wgJkXKzwWls7g6FrXtAbY5l-Ep7zgjaMtBZwawgmY0sXhUbZ03CbifLQeyjBYQZKpIG7EbKUNRUIPz9Idu2Zd7tItv7Q0V1ByEPEClRVnXdRxexPnLmm3xA40UPwpkcWt9RKJWNnvTh304Cqzk-VMquqDcWiz-9-DCK5agOtXjK6Rv9WWQSdCBYQdYPHbPSWVciySi2Ts26w0mWYZr5iHWQc0gP0kkJB-3SUzaKmBiLmJ27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=iaYgqR3dKPy7lrL5eyxQbupmeGt9_aDmC4Dj_HqFoprCGYkCqt1qmPYEj-2wK8DGEzZVdWTRJY4t84rZW-sVxXueh-0m-S0pIjDXS9TCuAApusgs5PXjitWkuZNZgGeI7DySBVIoa4-T79l_pReQ6uafCQPs_tOHrjlQw5DKtP8hB_lUzPLrxyLnD1G8pQPc06s9qSmZ1fJ_ENYXAe7E75NrG3C_sZykB3GT_qjR36mIjRZ5GSnRiLx0Em30f3rG48gHgETSWqZr90FnfqaDU1vWwf9Ps4_SGosxh1GKXxN5jS5nwUTz4EUHTbKQmYij_PgcRQuzTiGRnpbYGs42pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=iaYgqR3dKPy7lrL5eyxQbupmeGt9_aDmC4Dj_HqFoprCGYkCqt1qmPYEj-2wK8DGEzZVdWTRJY4t84rZW-sVxXueh-0m-S0pIjDXS9TCuAApusgs5PXjitWkuZNZgGeI7DySBVIoa4-T79l_pReQ6uafCQPs_tOHrjlQw5DKtP8hB_lUzPLrxyLnD1G8pQPc06s9qSmZ1fJ_ENYXAe7E75NrG3C_sZykB3GT_qjR36mIjRZ5GSnRiLx0Em30f3rG48gHgETSWqZr90FnfqaDU1vWwf9Ps4_SGosxh1GKXxN5jS5nwUTz4EUHTbKQmYij_PgcRQuzTiGRnpbYGs42pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQeMSWGAieGfIlISvjrjT40HoV_n0-fzGD7p5v31vmF7mmjpBCN6gTzi4V1Hqv9j0KxKM9chynd6h69douSRx8FqT5Mm40ewoXoKnw3YQsGEzZn1GWzfYMpl0GGCpTsUdGxkEgR6E4JiIfei6I45eqsT76iwkWe1YJ6l1Z7Nltja0uMC_VXKZaHGlBTLAL3KKDpYXaCwISDF0G5LQQBGzEb8mMOpLwRbpJqH5Ylxzw4xjNj1ZzVRTq1thj-ZWVfbftkl6Mj96JayUpTiwWuxqF9Q_tyQOQJMZZD1QoStVrQxAukeJqAhH9uQevRXxtQe1W0ToD9r8UqtfZBOoqvzuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=llxyIFLRofwGk7KcYcQ_7irpOB_1AkIclNwxaEiVUcGZ5jkJREbhuHwAV_tfh0CayJB6Y1QQlOW8UH5kGcZ6X6a-lkEACUprZPp0TDpuo9lEU2qR5T8CX7c7NPZBGfMAMEJb-ZtkhmIEYJ-llj43zKPIL9sf2GS6TmXi0Bpspm1qi8zwgkOyUP7hCFbDo5gWnGzhobKfLCnfZC-YRwWjssBpsjTLlSHLgPyheRoB11tQnxKkGP2wfnboBRUfvmt6NRiuE399WXRtVILzBnLDlVkKD1N7dnYLpCBv32Mg3fmu4qzXnAw63V6e_4FhJEYZUCOWIl19KVOlbOfoMcCm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=llxyIFLRofwGk7KcYcQ_7irpOB_1AkIclNwxaEiVUcGZ5jkJREbhuHwAV_tfh0CayJB6Y1QQlOW8UH5kGcZ6X6a-lkEACUprZPp0TDpuo9lEU2qR5T8CX7c7NPZBGfMAMEJb-ZtkhmIEYJ-llj43zKPIL9sf2GS6TmXi0Bpspm1qi8zwgkOyUP7hCFbDo5gWnGzhobKfLCnfZC-YRwWjssBpsjTLlSHLgPyheRoB11tQnxKkGP2wfnboBRUfvmt6NRiuE399WXRtVILzBnLDlVkKD1N7dnYLpCBv32Mg3fmu4qzXnAw63V6e_4FhJEYZUCOWIl19KVOlbOfoMcCm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkcxq-UxhoKPtWp1r03ANwKBNEOd9KgkYpTMC2DVMhNtnNcdse4rWpCNIEiGqNQ7iuww9rS6DEBBYEmVeit7xrO7oSQwKyox4DKmtS9nm3eyKq4JyyTxrZNWN23XPR6GZW7SiY8bGgpQYbGXlZu7Djr2QBPS0zfkl_RuOJwTYvwMjoc_5pHOwYxaDWgqOLYZs2JpMjuf07Te_ftoTnuveirheu1S4tfL10xAyIShdGj8lSseSoavwty0coOFXStzwjGhTZrMzVnavWZte3H3C92XKI-YQde86e35XaQGI92Asjef2BpReGVj-sesAOuVuaKf4-dL2uEOKVQctCRJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=r7LkZBavyEC59LXEbFAY3F0pyRfkYsbinxtDLBK93-PSEnPsLkh6fOOZ7-YG2oVRhsc3FRCC9iqyTk4sLLz6Ll_gjw1nT_GzmXOrsBjRBLlvNdRdQlCEYw9_PLXTi76yf2jtIMa-UFGtVlyIUGy62GM27n4ElaTcD35CUbPU1XRemrgrVsw-eIpcc_5DOwS7oaBWPHdc-jzF_15-mfWjSVyS2vIG4FNQvlv7A99BKbSG5S8zIGsQnRSpb0d6MXIckN8PPZKX29otTZCunMYEoIK0gqPXOhaMR4ETqdgq5e_WPHYCSXvbezrXsmEUtYQFApE8PFcC4JM42Zlrnati7nuFl9e6VehMe770DfVVuPh_qk7tDJg0cdjegdgNSMiHNiqgG-LWMFJpiWo8jadKIZhaVcfbxInzYQfrc8r5bMFSeTcgkslhf3PQ1qv5jCTUg4A_gz_TeYrU6l-5XXpoxHqAKgaof2MSPfWob6paatr0Tq8Ot51Vn39Z2Xw4_rOuirDVwyAop88nNo6aI6hJCZ3sGudZ818IfJb1rsx3sLLkw3bnrE3AfI6IgzlpV1TtF4AzYQIVgDpMfqDYvvzTCRDQSLBlvoxCmxX6FFEgLBNJeDJX8Z5iejVN3Pl4QKnT7XJ9teyODZkDkxHvUzmDyJTx20FhBpC_lqfaBB5DLKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=r7LkZBavyEC59LXEbFAY3F0pyRfkYsbinxtDLBK93-PSEnPsLkh6fOOZ7-YG2oVRhsc3FRCC9iqyTk4sLLz6Ll_gjw1nT_GzmXOrsBjRBLlvNdRdQlCEYw9_PLXTi76yf2jtIMa-UFGtVlyIUGy62GM27n4ElaTcD35CUbPU1XRemrgrVsw-eIpcc_5DOwS7oaBWPHdc-jzF_15-mfWjSVyS2vIG4FNQvlv7A99BKbSG5S8zIGsQnRSpb0d6MXIckN8PPZKX29otTZCunMYEoIK0gqPXOhaMR4ETqdgq5e_WPHYCSXvbezrXsmEUtYQFApE8PFcC4JM42Zlrnati7nuFl9e6VehMe770DfVVuPh_qk7tDJg0cdjegdgNSMiHNiqgG-LWMFJpiWo8jadKIZhaVcfbxInzYQfrc8r5bMFSeTcgkslhf3PQ1qv5jCTUg4A_gz_TeYrU6l-5XXpoxHqAKgaof2MSPfWob6paatr0Tq8Ot51Vn39Z2Xw4_rOuirDVwyAop88nNo6aI6hJCZ3sGudZ818IfJb1rsx3sLLkw3bnrE3AfI6IgzlpV1TtF4AzYQIVgDpMfqDYvvzTCRDQSLBlvoxCmxX6FFEgLBNJeDJX8Z5iejVN3Pl4QKnT7XJ9teyODZkDkxHvUzmDyJTx20FhBpC_lqfaBB5DLKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=AEJPbNllD3x7aWgsSfl2onrhvKKNIzZ-LUqP2E-kDS1OM3XVMysWOmqVYd7tacXMcEASH98qen0aNRJGdIXBW79805ujjRmMzQHU9akc8HRCYSp9b2p9_vM_oCiLvXU2gH0KvoOZ_k8L9_DTWwtyoaOWLWLbSfEEPLrabvFjQ0Yn3ti3bTsRHHzwo2P4xFrG6DBTHoxyQRnXcsUe7CRtjI_X7GowfzHk-D4f8Uu_TWxFOCMXgju1N5KUmtSZoWI8tedvFXaCIG_FVEg6Lv7ahfK3K5zkeEN1tMNiBJv0Ya4WrLTsTrXJonhq0IWqmXLY0VggXSgdlRqzjWbSUiht3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=AEJPbNllD3x7aWgsSfl2onrhvKKNIzZ-LUqP2E-kDS1OM3XVMysWOmqVYd7tacXMcEASH98qen0aNRJGdIXBW79805ujjRmMzQHU9akc8HRCYSp9b2p9_vM_oCiLvXU2gH0KvoOZ_k8L9_DTWwtyoaOWLWLbSfEEPLrabvFjQ0Yn3ti3bTsRHHzwo2P4xFrG6DBTHoxyQRnXcsUe7CRtjI_X7GowfzHk-D4f8Uu_TWxFOCMXgju1N5KUmtSZoWI8tedvFXaCIG_FVEg6Lv7ahfK3K5zkeEN1tMNiBJv0Ya4WrLTsTrXJonhq0IWqmXLY0VggXSgdlRqzjWbSUiht3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BR3ZAYYNucAe32ZNTk_ak3yB1xM-L-JCUp1VYdManK8hoKZYtmFSurAH3VBsahQ4tKgBhzHZh0VGNSYv_K-GoGEy2sQTviJ_t228J6_X9YEfGunIlRIoGKV7-U3ny6b_eKlWXoOJRyUzTJYnKKiInxW6B1FSjWCly4Z03rHZoLgqp4I-btBGl42114GK2Pd3zMNprfAOZV1B8Bvn1BSicDB9wE6ERKznnTOEvQUDmuQZiZv4hOGEU0dI7EQWYzhbbexOvktX0efV_4nd9WL1-MQ3joJUIKFCQlraV0vXMFSHuHY6vSUMxC4nVb2OQP3ac5HItlB5_1dSJ21bU0BYJ60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BR3ZAYYNucAe32ZNTk_ak3yB1xM-L-JCUp1VYdManK8hoKZYtmFSurAH3VBsahQ4tKgBhzHZh0VGNSYv_K-GoGEy2sQTviJ_t228J6_X9YEfGunIlRIoGKV7-U3ny6b_eKlWXoOJRyUzTJYnKKiInxW6B1FSjWCly4Z03rHZoLgqp4I-btBGl42114GK2Pd3zMNprfAOZV1B8Bvn1BSicDB9wE6ERKznnTOEvQUDmuQZiZv4hOGEU0dI7EQWYzhbbexOvktX0efV_4nd9WL1-MQ3joJUIKFCQlraV0vXMFSHuHY6vSUMxC4nVb2OQP3ac5HItlB5_1dSJ21bU0BYJ60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POEcr8EdQwIdDjDtKsn6LvKvi32wapwHa35qIoY3vYcmkz-30PDaXhP4fEtbbftsz_iOc7a8hMxQk7BUmp3sayaDixUkEugGZtru-JvKgXj1HGLwfHRxJ2jN9wpMIeibiTHtWtdbwi3_Lv98QI0g2Cxv8CCgjxLyl3RukJ-5zyCNhrU2NmSyaR-rV8omFcS00nGUrdrnaJKqdcCXRIiardxo7GcsVhPlK2V_jiu8fTHyOGw-lob6xHWswIfGoVG4jSks07DwL3z0_mkU0NuT3MsnXWGPTp7Fh5n3HwcnhsANZzUYJqkUhYuswM2MGYLl6EK2d6Ter3tog42GTufC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2jLZIp5cXYrOvvQGW0oRbasCbAjBC3TEmsOzd5aG13PkP0j0LCJcxbeLvfj4up8MApdpcoHR942Ex5e9rSAWw-7ZMLPVXgjHd4ndr9dRKnAHApDt_BmMp1sUb7zct9qO08Ctyo4lRyLytdXFKzztkqUriwg0pSHmWQwhWMhkFf8e5rvaY0oiOeHxB0hvhSH6Ar0rDoBzV4rXCjnwRefQAA7tFdNTsJVoXAPOcYB8sw-0ghM8dP8iVcbbfiwJRhlYNHV-n932E7JO8xGmPBCjuSCPgQJx9I90yIVAWE1FT4nFUYiuwaMtLxi0_lyVO8tz6DgoNyHSg2Sck4IlhPLvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB8MH2-H8HJAevnVSX8v6f0C0_BcXnA3cAH7ErATp-fuznpcK0RyRZqRbd3950QCwu34t4vL-5wmxUptF3z4fIA6RS6ouDu0_ELQczmKbFltzbkwCEag-XgvvzFyqhpqRHfqWY4SMJ23jX1IfkZ6BbH6T0rtrfdTmZ4TCyyKId0RmrdTajgDmtmOBp7G7-aHJmFHn2wdf06PG6i6cAxyHztNOn6FEJuWzp6_fzlViEvSyHnPoIrVWR1cSC6dP0TTb4_QJVrMkit474x3E_Tb1TTulE_uskG1I7OAqe9ACm4D6KtFzMA4GQrX3LZ5up5BycfWkjHE_TeZJTvQugrw8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1aOlIhRZoVqSsVrlL6t28QQZZKjzrezNvvCGEhEXum4hFWpPydyNceKgjR3MRHdYORRzkHWDGLoVAzIucZLN9-QsAyJWyehoPZ5t7URciSx0GvtE_xGN_qfZXWJIRJ1dKYoc9KDcJ_L7SeFEN9x6yOKP8MWdNe_pJtXLVoG3-npIZvKeweH9pVsMlzEPStS-q9JdaWdit49UbzJsaamck5Aav9oJPdvkdjaBXvP3Emb5E9VDry5g-xcwZIwpVFNLZBNC_LET1u7AqCKlydbCzywYVGuy_eTbAZsrtzDcqxHnj8nu-WuGjHMVfOZKJJD8OvWZ0f8TnwdlL712H5Bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMIXtQK6aXNblOpMHfM36RhZy2wVSi6Z20AqDh7D87Xuk_egyLfa9GL5yQ-hupGLJCPeVW23FR_n93984sBm5dJBhl-ylk3lg8XboOTP_EmOF3yxNcjq32uDbQJ2aBAglYsGAFeaeZNPuTA7HIYwXuj_T8qQ-ytyJJ13XHBTD3qiPJBVwjP0c-cjz6Iu5h9YgbwR_qyzT4zO1DKnN13YQ97fPy3p1-ORHBQ7_UE_h3a3SE7sjrT5aBPMxBVzhr9xCDsFXC2M_TSjS1UQBV3dTVv2O4EtsXNmbb1vA_khoJtkqLcNybBvgb3CI_AnW7b0ZT6SW_UF3QW7PIR22Osk1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqHIIt0npIO3Ezkz1FgV8n1bjOrxT17hiHVE8Wh4IO2oCRDwMlRW_z3Isc8hHmlQ9JyoN-5DFnuU-mFEfNerg7zrJ3uXMsqdOH5bNpIEellSbuIqk0VO9oF4jWmN8ljpgCN3-EvltLlSZahTxNkP_vmJcLt-B9sBz2FN6rTllDIkrZdNHNUR_btWT0DNnN_14D6his2RwEHTST4xYiZAY_IaqTSce3nuTSSWCkNRiA4LK9u2mzYkwzEcFaD62Ptn9Zt0uzrpj83XWyLlPE-ra1DRq2Wyoim8MtyLsVe7a3BLuMh0TbC9P7rtRbM8rfrkdj8rx2336goi4RX78LDzaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSnVE3Tq-QfwfB9vwjtNGz31hPyaEfHZujcwjzK-7OI4xW4VD5JtyLKQFk9mnHS6ffkHoRW2KbCKlHb0AW9R01cNTIqVwu9ignDrPyGx-FSV2ltOVIr6yVTZCe0ctcwQHpk-9H4_dvPMf0mhj2OzHq0w-WweevN_RaDJgUh6dUzxA11HJt1tCo4AGwL_9w6Li4UHwSvOp0V-MTzii_qUTLqIXu3WMH2ns56efhtwoClGoqBAM4In65zYE2xk74BSuqm15oYWWwfF84mK-G_Xd7lb_nswSw55vy10uzHpztwhO2cy1OrXYnC2cnFjEB-VlidfCRdtIgotWIfxIs5NmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjXFAX4DyHnh4tW3uvC6hsbqyp3Z3wO_BeWte9ZF-IXK9aJraqNXxS_l-QqTB3SwSWQwibew70ieTXj-1HlSUyUX5xE1mmR2ANY-f-357EYoXc3m5fDmTWl1_PkTbMobP2VZ07dZLD-HUuXbUva6cqokLqakbR5nTAxlKXFlqLKp06-nu9vhIqyz95jYfsSBpVvpChgKJusa2s7Ghca6_uWVLhzGZtmdizliWdIrqNu4y5poDjBkHcGgWSmdFXe07Umzpv2vUS7bpMUnqT2itwYCvES5vizaBftpbOOIcTRV3tQeuvKiRgxF8RaA5LwT1KbF5QfdjuaWbFp1j6qgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owWLWw42SMPqOW_B9KxR0cIwB9mPWnEe5d_OTuPo2J7xK7nyDanMottoSgxGyu7aKKiLYe57feYge3dhVZLEjdIx94JlUY6mhJ4Xtz5mLksKGAMIY5NDbToAjjOFdzQ3EZy--Byua7IL-XC4GnNKm5zDU3nD83KDhkYlfNTZAu37rMDx-_TYm3tOC1CMqoBDzFfvCA8STwxAO_9Qy3w4tWyzzLqQXde_ajxD8H4sCHiHXqcHzDn4USviQk_FTdFQslEJ6ESAwbT8xYqXQIQsUbyW71s6OZc5K3d8-nrDtRHp1qKlOkbPm14urCJvivxJM97w6bqnM0jIh0I-fuwBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijnwQBPTDnKR7Lv1_Es18INdm6rtD58E2HZXCCIVIYjfU2nckOlr69NaSpf84HC_QP75WQZmzl3xCeMNCDmiZIidFqhojIQ-FryWukyFiQ5FI8yQm-EX3aDBU4mTgXbr_X7U1JUBijZQM4qw6s1NDeQQPggjb7PbPdt7IFu6p_rB1QKVjE9CzWu2637nJoqk2GlGPbfCKZHPoxfiz2XK2BILhVm_BTxDr8xfKATdcHQwi23W6k4RDNTAy-G3I4av3hwRYwTd_txzUj_M3II-LgwXct3zsNCKWMY4bTjeNGawePQT335i-WIiCXpTm2naDKudVhMChDlYlCBXufbOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU6siMZfUs5kIO9Z0rfOCnTfjQjQ05A3PASjEZmIZIl-FsUjumHG4SPQQ8JB_ok5zcw4fiuFVdc0jRXQSTZPlwz8ryRSMxw0snB0PSBzoW3KBfFrZ7_h95tqB9XhPgQFhe894PQDRHNVpT3BR9HQBEmNKSEMokqjrcTGj5seRH0DGZUyFm7zojOH1C5Ve0pNtB9E6Bkx7YgP5VkRhZCewtDhNH7cptIUVEbQizIIXmyqXvppY3aoZcpToH901ob7Wo5f_tBDzq7dLaF0NCtEaGklWWQNm-rb4c-FPGFVQjgJo6vTn9khs4Ldg2Auk17q6SQPwengOBEus7hSThof-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUSx5uAqH5rT03cru4W04HORD0dwXLGHttql-_VpXZGVK0OA2_1Hr5ibPsOVW2dk7Ro3X7eniADkd_qW4bueEhQWzKAK3g_9Z1rBduKRrxRQAx-UZwR4csLAQlO77Ya1FK4lrnRQ2vofNZGUyjJ0r-6xKZMnyaRu_k9dDUe4fDHnslqaJInE7AgWaravSOmPI1FqojMGuft-krXoVBOYJXF4LnYLY7dU1FVJQ3kD0eD5bZMXWy5kZVq0AV-LJyzOzgg0ufb3sGLpxPpc6xKgq2jhF_4Nz5QUOF-E3rjVkuVoQRPMEFeQ8u5PM5G4a9xq3xI7VbxmF_fWtExF1O35iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMGj1dsQfKOXgN0i_FV5qI4u8Ug_A788O8-MLA4dmOAKquBiN4oxK2PbBCEu_NoEhfZUA_jdqWeYKbt1UKELNDFj1bDGuJRNRr_790zRIhKC7rrSQqGlR0yk2qlOK5WB7_FWXXdrLsL4xQz91KUPVyagob4fWouwHOWgUpWk05225wMQohCNcxsf1t5PfCE8oKefc1qVnWKdpzjpBO6fX9p-wVmbYiMMrOKhF5U4yqu5GMFJZMBGcojaz4rhr_Q-NTeFoXSGEZsalni7Qejllkr7tQNgxPxZgDv_O4V5xRKLYrucOwsBt__CgIS8Xn6HVVatI9vUeaA-h0p5-tUw-sBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMGj1dsQfKOXgN0i_FV5qI4u8Ug_A788O8-MLA4dmOAKquBiN4oxK2PbBCEu_NoEhfZUA_jdqWeYKbt1UKELNDFj1bDGuJRNRr_790zRIhKC7rrSQqGlR0yk2qlOK5WB7_FWXXdrLsL4xQz91KUPVyagob4fWouwHOWgUpWk05225wMQohCNcxsf1t5PfCE8oKefc1qVnWKdpzjpBO6fX9p-wVmbYiMMrOKhF5U4yqu5GMFJZMBGcojaz4rhr_Q-NTeFoXSGEZsalni7Qejllkr7tQNgxPxZgDv_O4V5xRKLYrucOwsBt__CgIS8Xn6HVVatI9vUeaA-h0p5-tUw-sBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=PoPMsj0-gmNWkMDxvjHw-ees35eWVBkQfRONuJ0ggDY7qS7TvsicIVjwQA94tY0cxdkQ_QfZCDbqaAL2x6D1c42GCe3EwKQ3wDJfZWvSbp4AhZUva47iGtXDlVGfiZ0WB2Et5K7v3SAROpuvovkb46VQ3L0XMyzwzCjaWLUh7Y3G1KADuiP9_yiU_HN8gvfuEnDtjBtut9vtEzx-y_GifZHoV6Z5QgVsKhOyxF7AckuOD5-5aWMapW9NTcz12NJp3ML88VGoNy-Tvq5HvkI_gc3_2oz4vjBLI8sUh60-ac50ZZ3osh_1cmTDS3SOrdp6vrbsgsg2mEBLC-1R71WjzHft6ICF5-6ORJGc6rcnedRnD0fq662CLOsCbgxi-tpmXlog2sBCzZg5WhLy9BA7uoaBlYNINdq5nLZj49MWnqoYX7JkpCmB1PwlG6ssYVlmhUOFBqIHR--qTnaLqGTna5lLEc0Q_CTP0pViBq0oqNEMQKRsELGKPMToz6_jP60qtgJq-xQ66MBJbrS-zrJhkZkb5b1Ah8hxbew-hPk-uv0g2G87F8EXUHBLjbf0yBrpBiGM17AEQp6WaP0_W90ej_qQGJEUUV44R_GWzRHCcUT5IQ7y3mv9Pg4NF1mHCT5J_BIV7ur9QFVaUsTowuHb_wGafUd9Q4RAb2YYBXuEN4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=PoPMsj0-gmNWkMDxvjHw-ees35eWVBkQfRONuJ0ggDY7qS7TvsicIVjwQA94tY0cxdkQ_QfZCDbqaAL2x6D1c42GCe3EwKQ3wDJfZWvSbp4AhZUva47iGtXDlVGfiZ0WB2Et5K7v3SAROpuvovkb46VQ3L0XMyzwzCjaWLUh7Y3G1KADuiP9_yiU_HN8gvfuEnDtjBtut9vtEzx-y_GifZHoV6Z5QgVsKhOyxF7AckuOD5-5aWMapW9NTcz12NJp3ML88VGoNy-Tvq5HvkI_gc3_2oz4vjBLI8sUh60-ac50ZZ3osh_1cmTDS3SOrdp6vrbsgsg2mEBLC-1R71WjzHft6ICF5-6ORJGc6rcnedRnD0fq662CLOsCbgxi-tpmXlog2sBCzZg5WhLy9BA7uoaBlYNINdq5nLZj49MWnqoYX7JkpCmB1PwlG6ssYVlmhUOFBqIHR--qTnaLqGTna5lLEc0Q_CTP0pViBq0oqNEMQKRsELGKPMToz6_jP60qtgJq-xQ66MBJbrS-zrJhkZkb5b1Ah8hxbew-hPk-uv0g2G87F8EXUHBLjbf0yBrpBiGM17AEQp6WaP0_W90ej_qQGJEUUV44R_GWzRHCcUT5IQ7y3mv9Pg4NF1mHCT5J_BIV7ur9QFVaUsTowuHb_wGafUd9Q4RAb2YYBXuEN4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtjAk0TRT1giKRZ2bPVDHql0syHgSe0_umgdbzrL5SjUlws6WXmqrSJSx6_BTZtcPVrX-vfRQGKUL0UQ-euhQe_xnJuiI1u-BTZOmhlc0Or8DnJ47PL9GFWUoLKfo56QC-U5yRPXK-L2yt8nFyWRydJU0P_gbaIVcTLm0CWL9n0GdukUgsFHxhB9SvQavem_5-O0IV-B5JhMY8WEd7ZFnqsF6SVDrO6QPKcmwN8iZt66rYE-NZbUpAOeX5FsXc_f7e2fquQUM2MX1_f2tZQNSkSY14S0ufG4SunPFRH8leGQOCR3x6IJwPrUtsEZv0QtgIMeAEBybiXyBhKIQfaXVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=LnPlXpnlJ4qn4M4ugQEeJfQmsFQh6TgyAWZX0EPtHHeDC9ontaZSlIWNdbmlTxQGTy2rvRvegghohvB9R-epvHiVMkS4xn-q-Nd2YeH6G8d3iuYtoLgdhGQbWq_L5iL8AZbagEInrFzkjnGqIFoKh25H22m5Ba5ZQxbPnCTJhjGX36bRmEzBBJfOApRfuTZ6eu04-GRIYnisPDS0KC363TzcxlwPHhGHn_RaqL6JhStr0N3wH6Kfk73Sh63YIxZ7XiSPcXnAMl4iSp64UKXa3wNOBb4c9CeRWYh0khKt5d77yRuTMBO5iqNsLg3Iz_ZPMY3eNQp1kkOH4wnpm6m_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=LnPlXpnlJ4qn4M4ugQEeJfQmsFQh6TgyAWZX0EPtHHeDC9ontaZSlIWNdbmlTxQGTy2rvRvegghohvB9R-epvHiVMkS4xn-q-Nd2YeH6G8d3iuYtoLgdhGQbWq_L5iL8AZbagEInrFzkjnGqIFoKh25H22m5Ba5ZQxbPnCTJhjGX36bRmEzBBJfOApRfuTZ6eu04-GRIYnisPDS0KC363TzcxlwPHhGHn_RaqL6JhStr0N3wH6Kfk73Sh63YIxZ7XiSPcXnAMl4iSp64UKXa3wNOBb4c9CeRWYh0khKt5d77yRuTMBO5iqNsLg3Iz_ZPMY3eNQp1kkOH4wnpm6m_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=fZwtRr_bVSireng1NlJnkxun4swT8j3c67K0PSDyYCg1W76xRe8WVnmA09AJ6eCIlkZN66R1BVPCrou3CTdRYPh3jBMKjv_6QYLwSsw4GRcx7I6anG2EHGwvUlvIIwkLQOSIlkKd9PXk3vZj4k-hok_jFIaqc29aK9n_qZ4kOH-juEO4HABa6PPXff0_rMYQ_fVeBGw8UvWao_HKBxsdDaJo5k_TTA98WxuYSDCUAHNjilylCpHBWyjshrSFgstqDc6incKjhJDvRbbLJYssA3dS7QFpf7IJPsHctsVPUWqKEOuzloSsK9_0YDsCAAP3J9y1IV0D1SF3MpJKXVjR5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=fZwtRr_bVSireng1NlJnkxun4swT8j3c67K0PSDyYCg1W76xRe8WVnmA09AJ6eCIlkZN66R1BVPCrou3CTdRYPh3jBMKjv_6QYLwSsw4GRcx7I6anG2EHGwvUlvIIwkLQOSIlkKd9PXk3vZj4k-hok_jFIaqc29aK9n_qZ4kOH-juEO4HABa6PPXff0_rMYQ_fVeBGw8UvWao_HKBxsdDaJo5k_TTA98WxuYSDCUAHNjilylCpHBWyjshrSFgstqDc6incKjhJDvRbbLJYssA3dS7QFpf7IJPsHctsVPUWqKEOuzloSsK9_0YDsCAAP3J9y1IV0D1SF3MpJKXVjR5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
