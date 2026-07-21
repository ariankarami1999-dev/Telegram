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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 22:35:21</div>
<hr>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhspRjEojEV8PG2r8UxMAe2vctmlZ72-y0HqNMrydiGPwS8jZbSILED-odMqbiqSYhU297aANDUvknewmSHgpYV9ksrjYx80DEOOdoYzNnhdUK8HVjYHRk9YYb3XqXXl_3-J5s45HeUSH4I039dX5mxYVwpYIMMH8JStzkpuzYkDkAIBVsVFcNFOs_v3m3jk2xkkgr_a6LtMDE-WMQWsOaljOKIX9q07NCDY9ISvTLGfIR2n8kadQSxY_lq6PKOFn3QVamM56tlCszZJtcuEU3_xU57L2fTYoE83VBkKY_XeoyfCzR4WYcrljdeReExgzcC7K71tD-kwNAmB-WjQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp-IFPpLYLD6EYUN64DvswImvVuhq91JoClI4-zw8rXJL3hvZbiuuRpfrYhBkOcxG2gYwl_ZU98LSTH7aRgDZHGqRxss0axx1fOPPFkc5dDJmB6PDsXEypN8ZtjI06GRrYxyLmJJxUIEI79rCcF-W-rT-Ub-FVCMMUtfjn1pYy-LCkqST4dgCam6bchoovX97ste-e1CO_UAeXXH0X8YAZ0v3E5Nj2YssQ9_C0pyFGkFnXgbwcaoEfGnQH2LFzdZAeNqpyeBDd66oFW2rD01tkdAGX8isYX46qrKh-fZwxQH4CWyT9dCfgMQm96rCDmCyhJ6otkrwAYIvzRNhX_mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=m42MWXHAEWCHTqS2cF2gNOGt3uHT3URjGsGSXttOE2Chx_n5nCGnDJlMabVD2d-0SAJdZFeRIsQai8fxSKxE1N9mXHoNkD-0pOuOM0alm6IwsnJoWXb9TW5ZfcuJkzG4o8ieCQg4Wcq2QcyIpsAbrU9lXbEdTZcwT8HEbbxYrBluptcBUn5FMh0QNBnuQZwO2wVTihegIIHCz220rQG3br3GPcOHZE8KsrGzqaIyzrMsqyezGeW__0vK9NnNQUFel-12_6QkwtSuUYTUSvmj7PiMMGlnZg4Or9AQAiLZMk8YhLKqINarNWdvvnCJCnWGDCNI-5VPOpPUDyGbU6rquw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=m42MWXHAEWCHTqS2cF2gNOGt3uHT3URjGsGSXttOE2Chx_n5nCGnDJlMabVD2d-0SAJdZFeRIsQai8fxSKxE1N9mXHoNkD-0pOuOM0alm6IwsnJoWXb9TW5ZfcuJkzG4o8ieCQg4Wcq2QcyIpsAbrU9lXbEdTZcwT8HEbbxYrBluptcBUn5FMh0QNBnuQZwO2wVTihegIIHCz220rQG3br3GPcOHZE8KsrGzqaIyzrMsqyezGeW__0vK9NnNQUFel-12_6QkwtSuUYTUSvmj7PiMMGlnZg4Or9AQAiLZMk8YhLKqINarNWdvvnCJCnWGDCNI-5VPOpPUDyGbU6rquw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Y5FN2y2Gp3jIIqPX29_9kwh_OLN0RVeq_wBW1jwlVMgCqP1_6xRJa9rhr-QxDo2xiLCwul0h7jTmWbdOD29MmVtQO6XvnJhvKktWSGvOJxagtJckpCNipscIhUjy6AoLYxskpvvJtDqVx-u0vxRznziromuM8DozpdmqPx1GS5YGXuwnJcssUYWDKlJhO6LhdguJ4e5LPFAZ7fouwJOUVbGqEvUQggOrehIncUSU8JGuYLwUYuqtkmGGlOmkqZxtHGaFCGLxk6JvCOkR2r9Kb1r9zusQyADv1Il_AHlbXafyt1Mnz4nmf-WEGdxHmf2oyDbn6dI_UYC2TQiIZbxHoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Y5FN2y2Gp3jIIqPX29_9kwh_OLN0RVeq_wBW1jwlVMgCqP1_6xRJa9rhr-QxDo2xiLCwul0h7jTmWbdOD29MmVtQO6XvnJhvKktWSGvOJxagtJckpCNipscIhUjy6AoLYxskpvvJtDqVx-u0vxRznziromuM8DozpdmqPx1GS5YGXuwnJcssUYWDKlJhO6LhdguJ4e5LPFAZ7fouwJOUVbGqEvUQggOrehIncUSU8JGuYLwUYuqtkmGGlOmkqZxtHGaFCGLxk6JvCOkR2r9Kb1r9zusQyADv1Il_AHlbXafyt1Mnz4nmf-WEGdxHmf2oyDbn6dI_UYC2TQiIZbxHoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgwEm9Q4IwAMIWJ2eIrYpZ8KTYKw0O2SHAJ_VlQWbc1sSFk2sxgecz4nN-WgheF7OASn8w-ROE0krBsnPeH7wd4-67ArT6sLsPdpQwd9NKdC7pyjPdLr8FDoMmKaoF20OugCZOKYNlSTuiZnzm7eGpAWy-NiOxuCDtmk2bd95L6tUMd_W99JhpV5GXHXVLorI0cIwZ_DiPeUkiJGfRl7If_gRFoSfzQuy_ZXF1O1GzLOMzXF49MvJ7BXc-oF8SqMr45TU9L9OdvAd13hsLVRb1UMaXohn4PcXXlLAukShVWFgO8nTU6qHzO1mUWt-0oqkcFGAhwmnWA_KrIuVhvEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZxxCUvw4IY4Smjf28UmKzRNRjl0GFjL4z9wbfAD4ZjXv-T_KYMemi4S-DN_GrznAtrqvv-3-x8UUDHpl-YE80v7QKYrt5qM48lZQiyezO9-f1AO0BG0ILCDMIBkwryz0x_9VSuaF68Ol47Yiqcm7hQWBKpjlePx0IIBtyRWTIgMFsWakzRSUn8bCikjWg3WHQeqMJhpFSUqQjzqxCIstsrQ4FfJnGJ9dGecKVQWu91uKYbbg5O79rpUK_DIU2emNYJBgWzSXId9z4zn_Oc7PzlM48U29zw2hHxCflzg-FSInc9mg97Clkw4m1-wcrhsIlBOQSrDOumbMv9cfPqlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ww7T6jywREUxxEOC91DdcnXzxswNa59Z1NGzH7-uGZUkAYMuOUgteCcHMFLSCC2NTUkf4KH5_uROGOwhOJATICqF0LeVhd5W85570w8Kg2m5JAmGDq2qfC7h9jbbwxayc1zbPJhEGEiUAtuIqJne2p_PbNyf_Z0vyfu1uGjzuq1W0X3tCIeu6HXS1tMfcQ6zbGkDgQ5IUtgn4GTzTYDNSinI90aTowZOZ1FBF_BzySQokc2v4i7zccVAJiPOxWW5NE4p0FLvkeyChBqwu63KQgFWd3vrZ2oyI9dudh7MdtnC9BQGt5lwSzYwNXsXKux6vBYNNmR6x5I1jNHhhvL8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZRkcQojfa6pNsGJmnOK2FUHK0GPDwarfLmnEpuF7PYbQR4KhD5BQxcldwbAFjBNum9CmXgyTlqb95rqP0pOWUr2q-zrP6IeIPZmU5_64KemgdkUeyj15G_dTZyodZW787PJiGZwXjOWHBs6E0LBPyvQLp-03wDse5hr893RvMGlnHfHS1JKG4deAP6ci5Rg0EYBCNn2uwuoYVDZv2g1xNi2vB164ZDWbXHlQRXFHt7qbpdtFGYaZ2YBYlhyCRglO6zdDmdmlO7jwC9TxlqgGi_AqVzld1NsIrH6L7iJZzMNZwNkALYOI4bvgyHQ9q4gtfFiMsiSM-_-V-EN9o1s3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG5KgieNzoZtyVWcswxReVsb2pMjyuaDT5TfWkg8QYyuQMOc_1BtIsoRVVetH1uJN7g5brwHNX4BgoX66TchuvLN6Pq8vDqBP4iR6I4YzVqwq5bjYBGuGFx8LyhsBPgA0Dh3UhGnCkpOAQBG1O_ehBQcDNIl5pF6B2fl2fPCujCwyGVAwSKNH1gcUQ0MMKGgZn7TJ0uHpaZWlEwXGj-Pqdb3-sxP2NmXXtOxSfH1yoBn1IdBYDgNe-pVIsZcUH6zUMWV_f-VutyU2BHnGUrgRSzD67H97BBf0DFbA6aFigb24hYJ6JAjxZzrulUHP20GiRDOfMSKg7cblCnKcEz33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnE7FNJ_ddneNgi8-HipzNqRn7wfCe6ZaSLHKrUWVR6wNG_xXH2kWN68Bz9kP1JF45ulrJgOlzpWBzeKpMJqU83n9GFX7lfYaf3SwPLlpMw9xDWh0mhk5JOHR-PP1haRV3J4JCAfsOl6vTp_hQVUD2eDUrMZTiPu6DUDTaBezgpavTIllzSihLvY5zyGLx2FmYtgRB2yvtCB3lk1l-1xhYdN1iwi28j5yuikRdHIVVwX_Lvhx8n4CNrYixoTdKNRCWEoZxpUf1myc9U8EG_T92o2tbT4ibGBdd9zqHi9B3dNViJXnJoCDo7wGz76aMhd3aXfShvcWnkxQd2zacNfIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=Z0WQRobpubhGVnw90s6bsML7Yhe_cTnUG-G5lpHxczdVEDYZb4WN5u-lnNRNnQphXZ4ZEnIOHlZjypqzNM5ee7zppSHetauwukVj8aa950ZEetZyf-H-AlluL4QT6cLLXEkOhrCFxP9GC4Gj3UvhT65wND900PEVGJcoLX38M_qsg5sUHNwgKAqWkuYbfnS4hG_vAHFfWr47YtRc8Szoz5LgzXKVi9lCnz8gIdiX04JZJGPAZTTXKXst_tPTCas5i6fBQnmVq-PMHMT95fMlqFnRLSRFixTOR-AWzfEt9FluHTaTJFzEtHQ7chdgbMJT3IEBfpwj0WTZ5-4vyQ0myXZ3Y9Je7b9GjpmZddP6yYNxcKqT_dAKSyw8OkZrz0ujIhJBn4wuEeqKgybMVRPlXQRT_DmesPcdy_nArmZBS6EdxavPuUg8jyXKf-weOyz7BTAxJ_UFLEWUcU-1KLE2Ux90l1ttKz_iDib7P6MQntGeTVfGvazr7QPny_njFCuoPNmKd4LUq7MDVXQJQng3Acb6d2onTn8swcqcSJhfnFT3r6qUpbFyVpIc06ZzJcJTtJPwVSGTaphdXRkeHJHCqXdUktFyx6dFxSTobiFWu-mPGiMh3KED03Uj24uwdRnpZp_bJZZuExOdT6TQvUbhxc433_s0sc-nXHGkeyW0jos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=Z0WQRobpubhGVnw90s6bsML7Yhe_cTnUG-G5lpHxczdVEDYZb4WN5u-lnNRNnQphXZ4ZEnIOHlZjypqzNM5ee7zppSHetauwukVj8aa950ZEetZyf-H-AlluL4QT6cLLXEkOhrCFxP9GC4Gj3UvhT65wND900PEVGJcoLX38M_qsg5sUHNwgKAqWkuYbfnS4hG_vAHFfWr47YtRc8Szoz5LgzXKVi9lCnz8gIdiX04JZJGPAZTTXKXst_tPTCas5i6fBQnmVq-PMHMT95fMlqFnRLSRFixTOR-AWzfEt9FluHTaTJFzEtHQ7chdgbMJT3IEBfpwj0WTZ5-4vyQ0myXZ3Y9Je7b9GjpmZddP6yYNxcKqT_dAKSyw8OkZrz0ujIhJBn4wuEeqKgybMVRPlXQRT_DmesPcdy_nArmZBS6EdxavPuUg8jyXKf-weOyz7BTAxJ_UFLEWUcU-1KLE2Ux90l1ttKz_iDib7P6MQntGeTVfGvazr7QPny_njFCuoPNmKd4LUq7MDVXQJQng3Acb6d2onTn8swcqcSJhfnFT3r6qUpbFyVpIc06ZzJcJTtJPwVSGTaphdXRkeHJHCqXdUktFyx6dFxSTobiFWu-mPGiMh3KED03Uj24uwdRnpZp_bJZZuExOdT6TQvUbhxc433_s0sc-nXHGkeyW0jos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=m6aKfUmKRZo8am-wLVpYbw5IZZGFhMd6wKNhb1TlWmKSNgpYjrVWolkPPyt5djnXgZ5pyqpG5V3gh3feR3NR1PlCOr3s8SRSgPDRgbo8citoJGFJ3cW5K_MPmxjbYQ0LIPEb-NdFu9YXyzcb_V8gRCMmuGBmmn4vnU51w0OlCJ1DM8n6cikX7jtJ2lE-LMSKM_70M1DLm33yQ8p6Vy3v9C9VLcpZ7cYf2OWa3-xFA9vJVuJa7YitN373rNrNVFvYQXgPumsUJIhFwTPOY7uKoWfmHuF0FOKPQetes9SAqHBqYZqLMoS5bQEwvtoInF7KTj02NgHRRh-HU1LuhzTy5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=m6aKfUmKRZo8am-wLVpYbw5IZZGFhMd6wKNhb1TlWmKSNgpYjrVWolkPPyt5djnXgZ5pyqpG5V3gh3feR3NR1PlCOr3s8SRSgPDRgbo8citoJGFJ3cW5K_MPmxjbYQ0LIPEb-NdFu9YXyzcb_V8gRCMmuGBmmn4vnU51w0OlCJ1DM8n6cikX7jtJ2lE-LMSKM_70M1DLm33yQ8p6Vy3v9C9VLcpZ7cYf2OWa3-xFA9vJVuJa7YitN373rNrNVFvYQXgPumsUJIhFwTPOY7uKoWfmHuF0FOKPQetes9SAqHBqYZqLMoS5bQEwvtoInF7KTj02NgHRRh-HU1LuhzTy5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMwBqqfCyNMLVU_B1I4f-0uL4p-CsXyNcYg5P78mgZ_U6bQCZNIRDnpumfo6n-sppu85uCFNQLUvhItu6DmoICMGiqIP7vWyaK5kxEMyjvJk5bkfm-rWY80Nz0TQlBga-DTQn3o31PyD8OgaBgjMUas8kgUX9JZivWsdkNAC57N8Hg2xLoWfdL7bYa9Dj56izcuLxpAa2wUYqRqJFXzvVSRbjtWF5OI3rS8MB0I8qqkIQfnD4PRLnrgSOuqTyP35dVcFDWM5UXdPPXBEKHvUn35VLGLvY4HfjMGEyS7OoEgfR5K11JcItr10iNp2yA6VjvrLDDVt69lywc9hlsMeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL5LxuRDeXpIwtOVrr_5mEBcUCGR_QvOFW64gdb-0_de94yKX-p3MCd-iyYWnv7pZeHYBiGhgcsCo-ECU6ZAbcNNAHzfNVo_0rO4GUaclNnwPzvVwsTsZefGt-RQ4dVy-YPk9bGHH4g6_0fUeFobVexwVJoNSbNlBDQKvIfwDEtxsK9gRR3D9jCH36n-hRBpv46bJ9z-Cj0ijyvjJYs2IUOfVBDs4FBTGlXrxv-9OoHOoKSqp4oTwGUU3tIuopqnEqh5LL2Z7ETxSSyDqVJNTIX2kWM5shoxFhBBfU0K__ddqME62kgZlbF2QKJTjoZMuzX0XZuMHr75h7RtzjGuXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNT7Wr_tq1l3eixzVDlzH6k1xQcHxtUcXnW-mKeYjF-JI_cA2WwT_HTNbRk5r9fqG_IYpgQlEK_bZG-IArRnBQluFltMwMk2Ku12yV6TJ0d8ZWVYSodRSX6WVMma_aU041PWyV6Sdh_tHeLHveWxPgLLh4EcSh-3AP2hC0eb55-Won8HbV8ubhziTmx-eo6HFeRW8B3llNjctlF7yBnipYZxFBNmxr7eif1dXLy9FpQ4i14nb-WQowY24Y9r-Dgw8K1CTJW94EX6I9h0nIYQsmq4Lmms-Q2IoPRFHRR3lkGj51jHTKuSwj1OjSANRSqiWUmgEFbedzjxHb78so56pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YoY7Y7fbjtcocptJupOqSD7kbq7FezTFGTWZyfHPAEi8_gRANR55_JP7FpLhkMsMFPGN77neZPaQHcMDj3SOmuO1mojmYeQjNshve1BVJ1Eany883Wg4OhTArIgfoFNTRrEvaTf6nmjtwf0AugDsiUdXp1wVqKZPpcZujyYJHx2SjLjLQx7D_0Je9iJRe04Ih7ocz5cMHSl5qNalm6u6Rx4F7Zzj5DFBxTd1S3DnO8iXKZF0fQ8r7oFSOhLz9tl8GSUJFeVS64V4_oyUbEtUlsd2GEuQDeDqgGB9zIIupya9tRbUQ44Z8Sl17dpiRexbHbi0VX9eMdI4ZRwZ65w8UA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBap3SGB0IiMsH1k0rX_TzIYupoJC6ho46Se_1_xaiJoOTUv9Sh1QWzU31Uybuaz5uN2VfVx9-JX8MPeTafMcralVeta-fdyhkiAyrkHpC3X360bvbOBMFt0P5APbQgsmhtpidAGfNGuzBfH9l6yDj1JcD4o5hu7IqauntuZmWiqioFkshqjxsI5LCqILc2YiWcsM6LCIts-W-EGDv6T4fkOE7w-vrqN5_g5KcZoUy1AgVDkn94OvsFWC2PdD4YkzxY7MM56YgEsnZKv0QEMyesHkufDFJLF83rJYn_TlKwlKSpianvds5nisPCZKepFThhwLFK5V1uRjInEdhZZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrJniJpNAuZIOca4bsSoKhKSfjqWocvJXcSXMuObTxxWUc62dhX1HpnuIAzBJF3GbLKkareEUTmnZq-jxrPazFewRmm1rzyugIBRNWyyPXQzw3Obwub7YdSS4ZBnf2n3Bvo9cE97Isv2QfKwMyNZsc8DqyHGZnaC-GOwiObLmpXeaREJp82OM5f4ziLXalvmFhQiaw5Xa3wPsH23AqvS_xvsq7ge9bA3z0e_vhGgFx5KikTrgKgjB9J5z6COG6gshFPOnwYfdfUZdK4hXooutcKYGi0rXDW51RK6T3OF7uJQkkkeKWDofYbK9prS9ulSWPTrwZZekbZXDM3C5mtqpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTgQkL65kqJHs8Sju5WM1SMtYMnqq7aYn-5FusRyb_6uamRmQP9-hw-wwYeM9CbnEh2LQYHjkzLO3_WOP0a-BJFy3mwqxmuAfIujAfHfo27QIRSeM4XqIE8t5XCeTJJKNu9Jb96-1i3A1MFTPeccJHY32iwfMeZdxUOZPbgWWE3pyljxOVsRf-_528gxjZqJPl2bXpvdflQOFsoPCIVMArkb0qF8S9L2fyXWJ6PHCCBOT0F_gpcHBcecr8gWMp6-v66VRJL_G_QAvdATWM29hyVOu6hmtHdSXfuXV2Bo0ZCObg7s2MoOV2ibrRn8j9yJatNprONbQJcsVGJ82M6XTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=vfWDVGDewuYFPpyp1x1EseVnWs14qZuu1TbsYi7S8Loi9riwweUowjUVuxPKZ3ZchOoLqWYLI7cXMV9LvoJkl8rSGSRbQPXB4APfC0LoS0si6sWe-_ZfFbflwUCkjw7ACR8YzvJZsPNRv_22Wd43Y2OUqK5chpsgqZ5g08iIQgrKEOqx4qF5SOZi5UXe3fpCZMvkvMqe3F2GcHe7FkWXeXJ4P3aEZu-Qs0h_j79e-PLwm7nuiWA6iZVo2CEH5rCDvgm-LchcV8GLd_li-4QmLOlud9ioXcP-iv73Cpx71PQ_ZnVbK2oS_8ASGcUNhGD9gMRWGHKirZeOGdTjGL8hDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=vfWDVGDewuYFPpyp1x1EseVnWs14qZuu1TbsYi7S8Loi9riwweUowjUVuxPKZ3ZchOoLqWYLI7cXMV9LvoJkl8rSGSRbQPXB4APfC0LoS0si6sWe-_ZfFbflwUCkjw7ACR8YzvJZsPNRv_22Wd43Y2OUqK5chpsgqZ5g08iIQgrKEOqx4qF5SOZi5UXe3fpCZMvkvMqe3F2GcHe7FkWXeXJ4P3aEZu-Qs0h_j79e-PLwm7nuiWA6iZVo2CEH5rCDvgm-LchcV8GLd_li-4QmLOlud9ioXcP-iv73Cpx71PQ_ZnVbK2oS_8ASGcUNhGD9gMRWGHKirZeOGdTjGL8hDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0VMBCnGWdMV_GHmI_7GppoDUaZ1c9VwIljx3Kb5RhWHfA4N86LQRfyjIJP43XWYY_clu4a6uS9ThEUn6HgNrQV_L9U6x1YXP3jFgl9jbleap2DSnMuu2eOOv4xo3u7sH9LjAQqOa581vi8g6yPJy3iqTlD0GfIqlZ5DK2ur9zJOTkIujBa19vJa6p1RrfIUF1ldiL-JUwlhj7PthS2wY-DT5fKjzsHKpOaJJD0vZbPHjP5QuM4_JtmXa1cytIsB2-lcUbVFooWeF-B_gT1P_WdDWQ6969GhhYEgMXg-SXxe45pJerJFFYTlgmqDfr8gHlHfBUylmuB8vKfb1jVhlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=XlWE68600016C7CH5OCTCyjo6qPx7WwiGpS727N0zEuA0Dmz2zta4OEplLMGeNvCeyW9aIOG8OoChltZAgycFxqI1YbFSZuaODvasAUMLCK2y2pf89Ctd33NVYRhZhYBZII2WEsznROBGUP-RbJav9lZ1lg-pStFnmpo4WgGDILE57r4JiT4OmwFqZ54QWP1oyvWdf3Pf_LMC4VUQ_n-5KaHVSrTU9Xf2N9b4uJM8DSQRrI3FDwhhb-R7NEJX5Pk2aObfQ5zYOiQteJAHgJESU2g8gKC-X7IbRGwys5tqPaWfsPRZzFaRyqXbMjVd2ldfopt2vUollLRe8MAAsCKZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=XlWE68600016C7CH5OCTCyjo6qPx7WwiGpS727N0zEuA0Dmz2zta4OEplLMGeNvCeyW9aIOG8OoChltZAgycFxqI1YbFSZuaODvasAUMLCK2y2pf89Ctd33NVYRhZhYBZII2WEsznROBGUP-RbJav9lZ1lg-pStFnmpo4WgGDILE57r4JiT4OmwFqZ54QWP1oyvWdf3Pf_LMC4VUQ_n-5KaHVSrTU9Xf2N9b4uJM8DSQRrI3FDwhhb-R7NEJX5Pk2aObfQ5zYOiQteJAHgJESU2g8gKC-X7IbRGwys5tqPaWfsPRZzFaRyqXbMjVd2ldfopt2vUollLRe8MAAsCKZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYIYbnAuI-gBh1S4v7OoSXj0kZog0A9_4rLQH7hmObGLKD4fuSZPAwGW5WkBw4y7GdomXXSUZ-tiez5lkC7GoW8ohZuDTtwcqthPtKlitRFDQh5f97dtcDXyyaElIPzMIzbhJOz5BguldnkXJpT2-9u8CavbV48oqW-lFTueeMKYGDtWa5YU78nd_7IWZaw7r-DhCDRo5_OJcOCtaJ1cpfoCic5wy4s12KvRkfQRGXi7ydQ7H1qZSA7aQSEb8X7a09lNtlGkOtFwakn90Zv9wAhAlg1XFmk5Bp8t6CA8Wax1p6ChcAJkYT-B73Q9PrdU3trtG1TgXGN4WIYjPF4_5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=r7LkZBavyEC59LXEbFAY3F0pyRfkYsbinxtDLBK93-PSEnPsLkh6fOOZ7-YG2oVRhsc3FRCC9iqyTk4sLLz6Ll_gjw1nT_GzmXOrsBjRBLlvNdRdQlCEYw9_PLXTi76yf2jtIMa-UFGtVlyIUGy62GM27n4ElaTcD35CUbPU1XRemrgrVsw-eIpcc_5DOwS7oaBWPHdc-jzF_15-mfWjSVyS2vIG4FNQvlv7A99BKbSG5S8zIGsQnRSpb0d6MXIckN8PPZKX29otTZCunMYEoIK0gqPXOhaMR4ETqdgq5e_WPHYCSXvbezrXsmEUtYQFApE8PFcC4JM42Zlrnati7g4wn0ur8gSMsMqw-yLFPVTo_cHwdi3vVD37OCbQubnXC8AfwCgl_Q2iq1ltME1qaO2FuepTgl_MSrJjSfve_Mznc-RncUCgPjtY956CfqPFpCho867QySNJpBhLhqjBMebgp3PKa_rHQITzQfHqzXpjllIeLq9-hjPLASSIJZEa-OHPrpkuHOc-E7LsDQh8ujC3D6wYc9VqE0KmjEqsTtQYPn6nsGt8SIgbs1o0Drx3UJ24ZJr88F5jIpEtlRWkfL9fok2mqKQlio-G5Oet2D2uX28TqsTas1J3MLovrWKXYvnNyHy7DBzyP2or0lNe4oS6M1EMufCIJsORCB1y-xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=r7LkZBavyEC59LXEbFAY3F0pyRfkYsbinxtDLBK93-PSEnPsLkh6fOOZ7-YG2oVRhsc3FRCC9iqyTk4sLLz6Ll_gjw1nT_GzmXOrsBjRBLlvNdRdQlCEYw9_PLXTi76yf2jtIMa-UFGtVlyIUGy62GM27n4ElaTcD35CUbPU1XRemrgrVsw-eIpcc_5DOwS7oaBWPHdc-jzF_15-mfWjSVyS2vIG4FNQvlv7A99BKbSG5S8zIGsQnRSpb0d6MXIckN8PPZKX29otTZCunMYEoIK0gqPXOhaMR4ETqdgq5e_WPHYCSXvbezrXsmEUtYQFApE8PFcC4JM42Zlrnati7g4wn0ur8gSMsMqw-yLFPVTo_cHwdi3vVD37OCbQubnXC8AfwCgl_Q2iq1ltME1qaO2FuepTgl_MSrJjSfve_Mznc-RncUCgPjtY956CfqPFpCho867QySNJpBhLhqjBMebgp3PKa_rHQITzQfHqzXpjllIeLq9-hjPLASSIJZEa-OHPrpkuHOc-E7LsDQh8ujC3D6wYc9VqE0KmjEqsTtQYPn6nsGt8SIgbs1o0Drx3UJ24ZJr88F5jIpEtlRWkfL9fok2mqKQlio-G5Oet2D2uX28TqsTas1J3MLovrWKXYvnNyHy7DBzyP2or0lNe4oS6M1EMufCIJsORCB1y-xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=RcF1mcoNKNx6Z3o8Bo5mmax2t-PbLyPSTFU7L-QWty8zPjYdexXSTpt_LH1lUFt2rTQqNmxwLvW7FyH4mgYFHjVW4I85NTHG2_QwuWaLRErLSFZX3pK5hmqiGqZnlA8vIgv-FTD7UTKWI-YExhcMU-63c_D7k3VwY61ETuDOKHi2hg3Ytg-ZEZ6YwW2z2UxGnsHR_r0G2uhrLUKKrbxC7w4TVHQP71I2o96PNp90yrYXVmNLpVm0zNa-YMXhwTa61ytyFNgMlJ0l5-00hppBN_4hbZQrJLGmCKY8oMqYMbbx5z2cNaXrljhrIYI1TP3HvfMPt37zNmzGdgHLbSonVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=RcF1mcoNKNx6Z3o8Bo5mmax2t-PbLyPSTFU7L-QWty8zPjYdexXSTpt_LH1lUFt2rTQqNmxwLvW7FyH4mgYFHjVW4I85NTHG2_QwuWaLRErLSFZX3pK5hmqiGqZnlA8vIgv-FTD7UTKWI-YExhcMU-63c_D7k3VwY61ETuDOKHi2hg3Ytg-ZEZ6YwW2z2UxGnsHR_r0G2uhrLUKKrbxC7w4TVHQP71I2o96PNp90yrYXVmNLpVm0zNa-YMXhwTa61ytyFNgMlJ0l5-00hppBN_4hbZQrJLGmCKY8oMqYMbbx5z2cNaXrljhrIYI1TP3HvfMPt37zNmzGdgHLbSonVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BbGwYH03MdaG1wy80XVLGXrSXuUIS33Xpot0NWESB8NuFB9A16oq36JIL62OvA6oOPHm7yjmzMbkamG4yAzDQ6KB18_UYtuELr3RZm0DpE0IVqLf8HLE0ZO_EEqlESFC00ugPeRHTvp0zO4I4ZWwTFmnhzlGGvx-mG3En1V9PKhJIxH0YoMvtXmXgc2LScZE6HWdfLzv3_TxV7Ub0EvwEUizOA1_X_R1jt86-f0l6R_0Z3JNkmA2fCLkQ59z6P_pJ4CcxBdFQD72GPjzU4bvg0WolbdGch9tHON_GWMhA4hUthNsKkTASs59x_O4DMbgaoIDtOkHxhzb9gQUUoa434c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BbGwYH03MdaG1wy80XVLGXrSXuUIS33Xpot0NWESB8NuFB9A16oq36JIL62OvA6oOPHm7yjmzMbkamG4yAzDQ6KB18_UYtuELr3RZm0DpE0IVqLf8HLE0ZO_EEqlESFC00ugPeRHTvp0zO4I4ZWwTFmnhzlGGvx-mG3En1V9PKhJIxH0YoMvtXmXgc2LScZE6HWdfLzv3_TxV7Ub0EvwEUizOA1_X_R1jt86-f0l6R_0Z3JNkmA2fCLkQ59z6P_pJ4CcxBdFQD72GPjzU4bvg0WolbdGch9tHON_GWMhA4hUthNsKkTASs59x_O4DMbgaoIDtOkHxhzb9gQUUoa434c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMJlRVDjOpaTo0tUs2KaW6xse1e1ZEyLM7B_aVw4PMM9-Mw78l-POevk1VIzkQbKBQUj6Cp0asNK2Dckku9FIoaVM_nyJqlrjuZL-1WkBCqNgoAF6d-Wslal5NGiWVNjGaHsYasPOaqhTZ7jFhaFUg5UyyZd_Zl7fQZGwfcz1dvAbbEBtf9Ushwk9d2qZIZayg4Gt1Dz9AcH8MEpiR8_gQy8FC7zqHLnT3OIZocUrWonI__BbrsTYaKHGb85MgvAb90yUdJLpscOih1NYn9m8cQSVIoDYnrDn7VZhdG95_0DPYvpQPLmJjxZfjQsfrKCcVdIrKec4kP-kcp7KBbaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etxo2lXD5ZahyrQdX_etAx26Konv4ro5elZyDlrgETtwgW0X9m_cMSq2rHj7JpSKcRO5Am4Dq8CZOk_3jX0xDPCWIbk1ebtn0DuytFhlzcfGJS7DLQvpphSS-zFxaouugTkpk2OjSB1ehbzciSCdgomlkL8vOYZSP5BVQ5BGO8FawWTzq76tvKq_u7aLIy5_BEARBLxZk3Cm5urpATHByYug4hJ6SdpHmwXjxG2fQANE23aiMcd7E_PPbxOobCmUBBHvzayhGkBW5OqjhE_gPe4Y_Aq4Pwlr5G-aQX-AyMUMBB_Vq9o9WCfliMYIY8IYs0kpCQj8Ys_jKi3XDuSZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IH-kgOB5fURSl3f1fNgAYRSScYOB-pnj53JN9kP7bXrywf6HmxSQhcbrDfaZnD9msM7-Kawf3FtIaFKa0UJpN9HmBZEGsj4tJQqnByQDz7GQxFnCDz2xNrIQU3S8hkEBjp5AhvlpzYysbx4yxxOFiXQFnmUUblR0BhXwez6_GbOL5v22jgwrf-wKWviXoLTbnhIfDYGY9lW98T4uTC8wq1T1sDT3SW11wZ4P_q1SazY6vtHTqkkmMF_BroTaJTTFW9befEaqSqeC3d-ebeOXODFKN0YbH4SUy7-FYKuRfjpT2YDwlAY0mz_cj_VrKkcVw9D0l08vl41TnyDTRuTGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0yYV6Z8PXGTLkznyo4wjw84NZ4TDBhsKAtPMozo8Macv35aTXUbIG5wg_sNH1QdKNg-gqJ0e7tPS2PnEAItPxe445fx6CJ7QqFobqRm9a4ZCI-QTAuDiAfAqCiHKqICBmESQupWTd_pCmJCe4vANXjMLuavkxc2-WcdNlRFOsRVBJgVkXdHnpwwG3TBvSyQ37jRae93GsiLI-q3I0ALVD8bvpjgvhfQwgcKw26Yis_Y9GOD7ARWRrgeu8zwmfkZKxrzXTc8JkG203lJ3B_YdTnDhqWirz92OXJsjN0WUCP9UG6jore2-tziyEC40eBPKehcPPrzKosT5T02MvIp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtZcRL_tHycMEWkFmJQ7Vb5IZpUTO950vNy7Vk7OUW9JySP7oUoT2X1Hht3b5_KqigeAy3S0KDiyvBAcDcy-nWnyATIl1jIoSnpb_ZmToZP-gRKb4GkRstEnM58cSvnvQOF4FUi2X5d5XKUdG1QbNUoC-nbb4NV789Okpdvas1tKtAX6vY_-8tIpfOuisa0xjYFiPJ7tZNbhyNjPwh7vCVUCyfjEPSAxzoo1jt9vvZOgbtQ-Qb78mbug7caEiXtvuRLEhUT2E61DeMSYTBD5DyF6m2p2lruC5ZJXKdlo5Y5rf6kMHoR9RqsvjC7yYiCl9c3YZdeWqacW--pqrydCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGtjPLqhnSdA3Rjorzqbaq0HrhIyaL9xk1s_kfozlHPPSGee19UAiuBuxZZVauTY4WQbkWcmdnM4MMkYNqPX0eNWaEJiDm1XxV7gVJ5QybBs8UyeZTVfHiZ5V_QrBDxIRQStLkda833YdDOsTKkx84Ra-lqDoUo2uXt_gQeZaNefpiKIu7_kpcog7F_FnkzoWN6BzHU1dFIGmbQmyM4fE-Iuu5-hVB6K217vyasIGoNZ7ZjGoY2nbHv8ngzp7LZfo0vY5sNQW6KhlCUn_Srjf_7RN9jVbLBHeTVablLETgOMYPLV8s6587bKs-76YQt0rBTZQZHPgzhFJ44c0suqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT1_77B2XZIe-NXEyXW4fmdSPu02OBxe2ozAgpm3sHvvZn0EKu7-nim9h_YFrPIocHkmeRCi-uV1304cYrpn3995aUBb6Mj5Ark_yvC11oVgdIJBnI4BJVmTrF-BxjprmtXYyacJPRGcsrHheF-K4mPsHehRbdDZO-gRvff_8SIqxwx1bDcqWmtI-7FWRtKqSty-op0BwR6xbZ8MlHmmaJzAT4gCe2f0tYfaE4HVDTetRpli-CFOmGh_2Rtrj6hnHNVgsl0x8gqyC0HvB2FFign4ZR4mLilLH1MLW6sAyXBb1jwWMgMPfGabft-qTPjKo3YX0RSU9u8KW6rbjoDEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui_oyhoFyejF2ndY6RIVAGuSuyg-xVVdlOCS6-qvgq7A_nmLQiByOk2h-5ajBiZALb6ut5AyUDund1d1OH0_OGDRY2TIPgjWiYq_FpgzV0M2gZOgO7MVuxHpa6U3dr1F16CyDC11wIj0PnwOW5U1AHPeK6MvnSKczz0xN-lgyZQSzQh9D0GNw4f9hCH3ungdccR7QfdczMZoeraY0erMSNXB7iupHGp4S3bDCf3OtFq8qKASpQUWBQIjcAxkPtaQbu0oZW2XO7MJnz1JB4dl-L-8Y8KtxOcAscBpinIXVFmK0CnAGQLPd_5IbWJ71UHQ2QMNsd3PT3MiOho8rgIYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBAOUGQbWBc5T8qOdg_XNTjZEDlDsaZslkpo1jRlAAlfS4UBZLhyTk4hrBoo4v98okTpn6jBAs8jR0Vdd3eJapIw92D3cb7THgshzNzFNWN9l9iFYQ01qkPxKvj2W9gLeTSA7kv-aHPZuLBsV0vH_cRlpsiEZ53qwgKkmBz4UOfnZqQTYjmX86dreHHQgVifkRSE4CpwQg2yK16DdY_g85QtDlkcRExMllzxQLkcT6fxEbTtGR1YbfVbIQfhD5XENtKOiJ_X1aKGRCQRCJRJkOAMx27Xe4bDD49hJ6H3MOjdUJaujn_V1riAwA5ezyaxrcJpYkF8dC8z9lwC0BLkNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiQfLpWHsjrIiVY1VZkU47MsYNX0JZqJT6jxBXywzJi82JQAB7FTf3nNfLN4CiErf1GNKtDuuyJyJaQ__Mlyi9upDPawfVtzooMOWzb2kbgaGThkfEmsk9baw_yHgcdv5bIwfdtgOWfBU2gnrSt9TZP2YqPypKHvvs5WmgtYZFCo1Y1KZQn_sfPzjFCRUryMEFhAQUPBE8P4L-ag9t_4XNtevm7kQ6au6RYTCIugIjhDfPt3IL3R4cPTxOQ74ZSwbm59YHfo0pjdFjfgNKVfw-2N4UWov0g6yvEZRapc_S8RQjde4CEzaZXU9oCXnzkbnrR1sEqCoUNeg5BFeQ4zpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upKc-QI1KXhS21ljkAUCN4bFYlXWqdkf8wZph_jS4YkbMwzbc2-KeCksnortC-GuJg5f0nvRf7uq3PPVEwFzwjULAFdv1nUHUR7dTQbK-lMaRRUv5d09uVuKe2WqK2y5YVekV_Vl91wK2bv9PtR40KGgfNsER8PGK4gl2M2ucD2V0Ol0en1a1TnQemv7dMIHNSDx03oYUFrDP46b6P8PhiuOV6lbMP0U0pMMAPpS_C55Mubd9PjbzXXOLV-CiupEwMHTcKYeUVVXqF94USi_UD17lkAoeLt439OhrrDFFfBfdK8Lf6xBaLFuPUMSzlm4pqQGHL4585affe6hULIt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5ABHP81zgqIqZB9hNVSh8gNO3L550faXUrRieHJoMXtKuWyQTBofk09V6COvwq2ZsceTDWYhk2CrkQ32SIR3zTNBU2Yy0axb8yKR6GfCgFHvDx0qUBKjbc4NJb-Dq4k7qMzCztMh4_CPqxSJDFPcJSa-kKGm856YdZgNU7egzcYDRiDBxNtgMJZyRClSBCunWttKHRNDvWQoN1WGlcVwtea_ZR6hCCRvKfzEOLIcgQWonlJqwjNvsM8I_vznETlt70n_gsMGt5twoydknXjolgW2m9KNSpVF-y6xnyaX0TZEBIy8apd-ris9KcLplT9ip3CrlYSt-7bxWlJFDZi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMHxR2ZyKWbFmpyDUkyZ1J_k6edwHlQdoEY8tfuUNv-Sr27bKNc8dsZ4ngvSofrQ4zxFRDNE6cA7uiqH2nGaAZOw-IJI_EYwUTY_OXTu9Y68k0D-96sI4kp_zqgd_EGj2BU18jMwFFyKJypCfbOrMQfsdSOpae4IcxPa2urbs5A2JEgSd-nFjes0uHTnEjlhePTKw6kHQ20nwH26YxzjvokEDox5se1zaYVz2fuNpWlzLfMnDEklesmpge3O9YelmRo7gSwjzcrUTwPMG3rdwylMd8IdC-m5u72G4KdE06Ead5HG-dFCUebyTRlM7JJzwE0y6UIQhNRCg_d27eMfxWSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMHxR2ZyKWbFmpyDUkyZ1J_k6edwHlQdoEY8tfuUNv-Sr27bKNc8dsZ4ngvSofrQ4zxFRDNE6cA7uiqH2nGaAZOw-IJI_EYwUTY_OXTu9Y68k0D-96sI4kp_zqgd_EGj2BU18jMwFFyKJypCfbOrMQfsdSOpae4IcxPa2urbs5A2JEgSd-nFjes0uHTnEjlhePTKw6kHQ20nwH26YxzjvokEDox5se1zaYVz2fuNpWlzLfMnDEklesmpge3O9YelmRo7gSwjzcrUTwPMG3rdwylMd8IdC-m5u72G4KdE06Ead5HG-dFCUebyTRlM7JJzwE0y6UIQhNRCg_d27eMfxWSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=nNCc9UXH_WSsLVX_nCoLNCgrVgWeu5M4FNME_WIId0wfbYkoA2_ZDBBO9gvW6Fy1c7LDtKWkZP_fTfomqXnTM9m1YQexsBMb35ZjZDEtbZU1ee438jhQfwhDvORgTK_MvxxFNbtQHVUDppMjHnrNf4tDNROtbq_yG5HfeR7AFj9JlL5k2Q3bnqDv5YCpgTcu-YQLkavU5E4TUdjXP2_XQTd9G0-2Lwe4juO2ApIrbPQ2lSJoT-rgtu5DNRW12r2wjrXk1WKfc_9q24i_tyMFltrUp1IjlMyBrxPlUl_vHnPs8gACB-mUoOwDmQEkErcOpVQXNpvEfVIXaJP5UM24jgEAwn0QVoNxV38Q2S1O8TRHDaB-BJM821j8laGr8bE7lx9qONFPrswhkgsHIFatlTSZPqSJS6e8HDkvB_Kz7PvVJEOx4kTLI3lG2YdFZLtkYP7zQX6q3hTY5ckhJRWb-8LEL35B8tRXoWnw7GymOxE48X_iKfpSuKLPddlWinOrWlXJwuC6IKFre-WEH24aweU5jj3KfBOO-eoX_OvACaQKpR7vrTh5uH5Fik-GU6rkF7B94vrrFyP5MLHar-LeI46Ra6tS2UyhOcwuihBMYXAiLnhSMe8iHTl2szBnq9fiPwZz1lKHcrrMA1Ahpcx8NfxQCMYgZApkyiGDfSIa3yY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=nNCc9UXH_WSsLVX_nCoLNCgrVgWeu5M4FNME_WIId0wfbYkoA2_ZDBBO9gvW6Fy1c7LDtKWkZP_fTfomqXnTM9m1YQexsBMb35ZjZDEtbZU1ee438jhQfwhDvORgTK_MvxxFNbtQHVUDppMjHnrNf4tDNROtbq_yG5HfeR7AFj9JlL5k2Q3bnqDv5YCpgTcu-YQLkavU5E4TUdjXP2_XQTd9G0-2Lwe4juO2ApIrbPQ2lSJoT-rgtu5DNRW12r2wjrXk1WKfc_9q24i_tyMFltrUp1IjlMyBrxPlUl_vHnPs8gACB-mUoOwDmQEkErcOpVQXNpvEfVIXaJP5UM24jgEAwn0QVoNxV38Q2S1O8TRHDaB-BJM821j8laGr8bE7lx9qONFPrswhkgsHIFatlTSZPqSJS6e8HDkvB_Kz7PvVJEOx4kTLI3lG2YdFZLtkYP7zQX6q3hTY5ckhJRWb-8LEL35B8tRXoWnw7GymOxE48X_iKfpSuKLPddlWinOrWlXJwuC6IKFre-WEH24aweU5jj3KfBOO-eoX_OvACaQKpR7vrTh5uH5Fik-GU6rkF7B94vrrFyP5MLHar-LeI46Ra6tS2UyhOcwuihBMYXAiLnhSMe8iHTl2szBnq9fiPwZz1lKHcrrMA1Ahpcx8NfxQCMYgZApkyiGDfSIa3yY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpmX_RlVl2WL1N-AyigLc8X1llK61CtnRvDfYmkx74xNwl6KMeZebBg0D0tDGTltC9vxlPxeJ2X0Sf7ln7P9vQsCJV7ABXWYAsM1eUCK6tlh1nZaWaOZ-zdWn0i1eTCGC7aJAht_iODr-WNCwhOO0FDFHoaJSfjQ6peaA2fGORkpErSymJ8DkA3xAu3icdd9yJnnrGJbAfH81N8vhWTLo6KJrRJ2ODdREUNbjCsb9VojEhE-4SydBFq77YXjw71I0qLyHjVJu1LWzRdGLGK8oAtAJtsdvnAjOn20ynI4wu6H4vdLqp7SwJ0r4--c59JJP6rMuYmyAswNHmdOsfBpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=ixbANgHwErBp0MCHqX2vN2FRAkoS3tp_jr2Co7vE7Ggn8IZL5JNjWQwfhBwwckHYGvWe8k2FE3sF8iLmp4eai00hVl1V29nUG6lY_xMKPktIgK7WuxQ7VS954R3B7lqJBa4J0ZH5rLH6Y4W1YnHUgEQzNJ8sz-FyeCDXSY654sQa12zHDCLSBgqO1FPvVPpfAJFaD8wstVhKMGhUHMlXrO24oN_jTiKKw2E73uq40wWsiI06mziAVey1aW6mXc5Xp4wazpDYXy559w0Wqa0BJK4UQKx_STQ4aaVWebIylx8iaS6PS9oJgYsaYp9o9tbekHhkgdeFM1j_3t_pV9sG0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=ixbANgHwErBp0MCHqX2vN2FRAkoS3tp_jr2Co7vE7Ggn8IZL5JNjWQwfhBwwckHYGvWe8k2FE3sF8iLmp4eai00hVl1V29nUG6lY_xMKPktIgK7WuxQ7VS954R3B7lqJBa4J0ZH5rLH6Y4W1YnHUgEQzNJ8sz-FyeCDXSY654sQa12zHDCLSBgqO1FPvVPpfAJFaD8wstVhKMGhUHMlXrO24oN_jTiKKw2E73uq40wWsiI06mziAVey1aW6mXc5Xp4wazpDYXy559w0Wqa0BJK4UQKx_STQ4aaVWebIylx8iaS6PS9oJgYsaYp9o9tbekHhkgdeFM1j_3t_pV9sG0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
