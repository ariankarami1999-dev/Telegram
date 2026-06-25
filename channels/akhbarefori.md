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
<img src="https://cdn4.telesco.pe/file/tSP6EFCatCb_T-cGtttEHt-aqJYScKiSYgTsXPhkrJKdzSJ55zxbuUvRX4jf1PdTKonG6SjJtcNgBVL7dnppdT-2qAarvLOoniM_-zc4oFzU8NS8KbANE7p9IKfZaof7E6JWEOat19BMEhQE8eowe-PtU4I4nAV7REtEgNfZAm2DqRmVLl3m4w7zF05d3M0R9Kgl-Z2dUZAKSF6AmhuZTo1_nzVpNewgcr_lxVVviovSwhJZDvfBbsJLS5qJm75JfsHFa4gxZXx598g3JDJCW27xNe3kzTK-zGnDxOhi35DMuRWkDATVcR5xUGT9EZ07M3oAy-nXpKoEOtFPEO3PqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 14:05:40</div>
<hr>

<div class="tg-post" id="msg-663144">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b9cf430a.mp4?token=MUzYruUc6FFBF2LAWHf-35mu_tqHEDWK9P19NbQ9bo9p5qciYRkUhPoBlGC4RNuznSil6SvVTCuE5eq7uUYgRO4MsUDSMM3h0ecu9F1u4CvIXOFz5-ipAPlGpZ2MMjNIdIflM5Of3z-LChX3DTto0lr-Npfzulx349r5PIwRjr_TNLo7PBr1C4zj6or5oWYpnIx1OBOE8Jpt8rK0ZjDdhNPcrra5s5PbBRX8AjwAWwc45h6LtbMOCtqS4valRX-SDCmRH0YuXYc5Yan5tBEXMCBCtVvC_xL9hGgrpidwGD_7AupU_WYgi3tdsvyTSP6jN1n3AkFYnMofykDN2bdXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b9cf430a.mp4?token=MUzYruUc6FFBF2LAWHf-35mu_tqHEDWK9P19NbQ9bo9p5qciYRkUhPoBlGC4RNuznSil6SvVTCuE5eq7uUYgRO4MsUDSMM3h0ecu9F1u4CvIXOFz5-ipAPlGpZ2MMjNIdIflM5Of3z-LChX3DTto0lr-Npfzulx349r5PIwRjr_TNLo7PBr1C4zj6or5oWYpnIx1OBOE8Jpt8rK0ZjDdhNPcrra5s5PbBRX8AjwAWwc45h6LtbMOCtqS4valRX-SDCmRH0YuXYc5Yan5tBEXMCBCtVvC_xL9hGgrpidwGD_7AupU_WYgi3tdsvyTSP6jN1n3AkFYnMofykDN2bdXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حداقل ۳۲ کشته و صدها زخمی در زلزله‌های ونزوئلا
🔹
طبق اعلام رئیس‌جمهور موقت ونزوئلا، ۲ زلزلهٔ پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور، دست‌کم ۳۲ کشته و ۷۰۰ زخمی به‌جا گذاشت.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/akhbarefori/663144" target="_blank">📅 14:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663143">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e10e228e.mp4?token=eTOXf15wux4KEjbLgfNCHSZf0iizfyxtRxoVmSuWjjoibdDNUndTqPORYH9zjWzfY4eGjp95l-GQcHycK2tZXAivHrD8ILon8wfIB9p_st5Dk1KVo7P0PARN56pmrsKqxoyd8iLTuMr1SLacqtA7EUjZJs4XLwNrokatH1LOhY2tr8KgYN8pUDpQLmEWgdWrCv0w8ldNboi9tjdfJPHKFtsJj3kcQsPV2BZhptBVbokOokcQ0cWXqr1c63uWKHU0exteppM48njmi6VuBP3XyY1Tx_5vPjPOaHUMSQJvVNnap0nKPTLzuupKk_LM3BouuvHHHJlKZnvZDH-D_h08Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e10e228e.mp4?token=eTOXf15wux4KEjbLgfNCHSZf0iizfyxtRxoVmSuWjjoibdDNUndTqPORYH9zjWzfY4eGjp95l-GQcHycK2tZXAivHrD8ILon8wfIB9p_st5Dk1KVo7P0PARN56pmrsKqxoyd8iLTuMr1SLacqtA7EUjZJs4XLwNrokatH1LOhY2tr8KgYN8pUDpQLmEWgdWrCv0w8ldNboi9tjdfJPHKFtsJj3kcQsPV2BZhptBVbokOokcQ0cWXqr1c63uWKHU0exteppM48njmi6VuBP3XyY1Tx_5vPjPOaHUMSQJvVNnap0nKPTLzuupKk_LM3BouuvHHHJlKZnvZDH-D_h08Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداری حسینی در شهر نیویورک آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/663143" target="_blank">📅 13:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663142">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCKw9GUL94BFBL9k3ZYwwdEPHWzvBGO2Is4nN2m2ti4LDZ7xLqc1N11X4OQ7_GcxpZYNswnuD7nRAYR2VZx6bc9UdbxIoJz3xHIAnGeJXpY96VSnaJSDGRQ8sd85_s3jyIJcqzE_7z-VSVTZd48LOR3gg2CPX5dVLfuIDuGLMxs01EOkQQ-U2wQ7mMUvL56Pyg0l8I2RdmPxhCaDpxJ2lSrizo6TwAHcWWdoHHRCDMFBNiHMcEUfJZDychVvhjT_3m8owJFJwaCgExU3j5_KqkmlWcQEnE0xfTwtNvaMdBX7HjZ7BpnzsDPMmYOmwQfdyeCy8zIJsdVT3haMQ9_pWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پلاکاردی عجیب در یکی از تجمعات
🔹
تصویر پلاکاردی در یکی از تجمعات شبانه اخیر، با مقایسه مردم ایران و کوفه و اشاره طعنه‌آمیز به«خرید ذرت و سویا از آمریکا» در فضای مجازی پربازدید شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/663142" target="_blank">📅 13:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663141">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔹
رویترز به نقل از مقام آمریکایی: اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/663141" target="_blank">📅 13:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663140">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آن نیم دیگر من که تصویرسازی می‌کند/به ازدحام فکر کن!
"زینبیه" بیت رهبری را نمی‌دانم چه‌طور و چه‌کسی نام‌گذاری کرده است، اما کدام‌مان تصور می‌کردیم که تبدیل به یک بلندی کنار گودالی شود که قتلگاه است؟ فکر کن!
به آن‌چه که اگر دیوارها نباشد پیداست فکر کن، به این فکر کن که نمای آن گودالی که انفجار درست کرده از زینبیه چه شکلی است؟ که یک نفر آن وسط تنها باشد، که ازدحام است، که موشک و دیوار و سقف و هرچه که تصور می‌کنی به یک نقطه هجوم برده است.
آن نیمی از من که تصویرسازی می‌کند سهم بیشتری از این چهل و دو سال گذشته را زندگی کرده است و همین حالا که نباید، از خواب بیدار شده و دارد این‌ها را مثل روز می‌بیند، دیوارها را برداشته است و از زینبیه به قتگاه نگاه می‌کند!
ایستاده‌ام و سرم بی اختیار به سمت جاذبه‌ای بزرگ چرخیده و جاذبه آنقدر زیاد است که دوسوم بدنم را دارد از چشم‌هام بیرون می‌کشد.
شب علی اکبر است و یکی با صداش توی گوش‌ام می‌زند:" یه لطفی در حق من می‌کنی؟! امشب منو دعا کن!" چه می‌گویی آقای محترم؟! من اینجا نیستم که! من کربلام!
علی اکبر ما بود پیرمرد
دنیا علی‌های زیادی از ما گرفته است، علی‌هایی که بخشی از زندگی ما بودند، علی‌هایی که نبودن‌شان حفره‌های بزرگی توی زندگی ما ایجاد کرد، علی‌های بزرگ و کوچکی که رفتن‌شان را به چشم دیدیم و آوردن اسم‌شان هنوز هم بغض را به گلوهای پیر شده ما دعوت می‌کند.
توی این همه علی اما بزرگ‌ترین داغ، مربوط به علی اکبر بود، بزرگ‌ترین علی که خلاف تمام آن‌چه که شنیده بودیم جوان نبود، که پیرمردی بود و حوالی خیابان کشوردوست زندگی می‌کرد، با محاسنی سفید و بلند و لبخندی که همیشه‌ به سمت ما نشانه‌گیری شده بود و اخمی که به سمت دشمن شلیک می‌کرد، همین بود که اشبه‌الناس زمانه ما(خلقا و خلقا) به رسول خدا شد.
از آن پیرمردها که فکر می‌کردی همیشه چای‌شان دم است، از آن‌ها که تصور می‌کردی هميشه منتظر مهمان است، پیرمردی با حیاطی کوچک پر از گل‌های عطری که بوی خوب‌شان را به همه تعارف می‌کنند.
گفتم گل عطری، یادم افتاد که یکی توضیح می‌داد گل‌ها که تشنه می‌شوند عطر خودشان را آزاد می‌کنند تا این‌شکلی آدم‌ها را صدا بزنند، بوی عطر توی تمام خیابان فلسطین، تمام خیابان کشوردوست، توی تمام خیابان‌های شهر و توی تمام شامه‌ها پیچیده بود، یکی داشت ما را صدا می‌زد و تشنه بود. هنوز تشنه بود.
ما اینجا مردیم
فصل مشترک تمام روضه‌خوان‌های شب هشتم یک شعر است که همه حفظ شده‌اند، که همه مثل اسم خودشان بلدند، که دو بیت است، که دو بیت است و قدر یک کتاب روضه دارد، که روضه‌خوان‌ها فقط اول‌اش را فقط می‌خوانند و مستمع باقی ماجرا را خودش بلد است، از آن روضه‌ها که به دهان و قلم من بزرگ است، کافی است یکی بگوید:" جوانان بنی‌هاشم..." و ما خودمان تا ته ماجرا را می‌خوانیم.
می‌خوانیم که علی اکبر ما را، همان پیرمرد سپیدموی را حرمت نگه نداشتند و چند روز دیگر باید برویم و "علی را بر در خیمه رسانیم..."
من نباید آن شب به زینبیه می‌رفتم، درست نبود که بروم توی قتلگاهی که خاک‌اش هنوز خیس خون است، حالا آمده‌ام کربلا تا سینه‌ام را بچسبانم به ضریح، شاید قلب‌ام آرام شود.
آن‌چه که ما توی روضه علی اکبرمان علیه‌السلام دیدیم و شنیدیم بزرگ‌تر از ظرف ما بود، اگر یک روزی خواستید روضه مرگ ما را بخوانید اینطور بخوانید که ما ته خیابان فلسطین مردیم، یک جایی نزدیک یک گودال!
به قلم مرتضی درخشان
@TV_Fori</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/663140" target="_blank">📅 13:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663139">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔹
پایتخت ونزوئلا بعد از ۲ زلزله ۷ ریشتری
🔹
تلاش‌ها برای امداد و نجات در ساختمان‌های ریزش کرده ادامه دارد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/663139" target="_blank">📅 13:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663136">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJMi-idwNWgEitv9IelnMvn6741rrsivKNk_TlgczBd4vJgCE1iYBLhl_wn2gKh-jOoOkzaRMDRDJoxUHt7lXfhVPKvqRI4SCJUqlQP52OaKWZXXyegvrfCBv8UI1uOWuznYz1lZxvFFgx1B9ew_tAz-hN0kMOJqB2vOHzT8CUa6TjLqGUpuknEfQ_DQPtsryOsy7XEtyZxQb5q2Q0os3FemarBRP2OaQ3inFJ5Uir9gNelfBiwp2atldIfiNf68JFljBgNBVMI1bbH5As6nCTCFw5_teegV3_fBuUaS6D-UuKlKwVTEOTplrhI4MWTq6XYFUPRikldAGYxCpFVB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvsOJ2tjQvozHSoeLMg9nD1VJSfcsqB95PNCx-URBR1DsJPXr3vtnp0-UTiYGSQ25DkKjRd_R2JjGwtrVc6Ymw9562OlKnNcsZ7PR_GlU2cO1-Yj3EU6nOhW7dRSFXxBH8U3X232jFiJRu1rHwsMXXrVw6H8WnPBm7hBeBmvm7OdEUeZpQSFEoLbGKCySEFltxCjsPIhycY7p12AShLkZowinB3rOefHsMAbP7pr3zSNAkKGgEFnBr_CtKP4ncNYzI_cg-ym1XP2K2MeZOfAXb9t6mYDyHmR1F78vGB2tq4F8RPL4wBV8_wbP4gTax5cVz3DlP6sWifrOfb9TKLEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmV8s4QXClr4f_ltbcKy2Eijx_8BSMGCXhFbOjns5YkR_HqzbYwmnQuPuv8zqynMH8J4XPgcpjs2wlDgMr4L7iLFZl4izRcQUJ9JC3phA8MdbjRr3ObLfZWKBZx5JQFJ5MTXQg0ojk_BKi0GU3Cx8od2mWqVZwdW_t3ZAlX9hYhDm8kDlsfl_JIpt5TOeku7sFAPBaYRTWrMx_gS98lOcyR1w4yTCJ5vCUMT70-p7MqYquAqZNRhEfO-_PJY_u6r8b4Wx6nVk401OqhhPMkWvZ8gatSwt_VNe7o5iI89fpJkD1Vv6YhvB1anYZ5wkSxKeuX6NZouTl0rvl7745KkJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
پس از هشدار سپاه، سه نفتکش که از طریق کریدور جنوبی از تنگه هرمز عبور می‌کردند، در حال دور زدن و بازگشت به خلیج فارس هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/663136" target="_blank">📅 13:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663135">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIKFG0Lj6KtHcoBhO-dqMBt81I3YsZeoQZXGOq02VuzuztsMScPpmoeQmhC9nskvJcOO5EeyOe0Wml03GCMqrEsp3Hm8WRy9dEJPTGWWREyvhXlng6XIAoJw3pMB25cTwa_WOALpxcYStEVimx0aXZpu6t1c3DxrtlYEXBRGAd7EG5EBwkPS-9sJjdUJgu4_ES0r93odI9cP5HFgqH12jSC779s90ccTxX7s5cC67n-tob1wcFvg4AET5HOP-wn_ls_ldrqAYWur2yCTGFo8O-zIEgquswUCk9oM5TG_EPVQ73Nu0K3TS4ntqKZXxpZESz8_IFWmHGjgDT-NM03b9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
علیرضا بیرانوند در جمع ۱۰ دروازه‌بان جام جهانی با بیشترین تعداد دنبال‌کننده اینستاگرام
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/663135" target="_blank">📅 13:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663134">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
قطر: کار فنی روی جزئیات توافق ایران و آمریکا آغاز شده است.
🔹
دبیر کمیسیون امنیت ملی: تنگه هرمز به شرایط قبل بازنمی‌گردد.
🔹
وزیر نفت: حمله به زیرساخت‌های ایران، جنگ علیه امنیت انرژی جهان بود.
🔹
سازمان ملل: ۵۷ کشتی طی سه روز(۲ تا ۴ تیر) از تنگه هرمز عبور کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/663134" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663133">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3efc1df48b.mp4?token=R45Jp-kzU2L6GVAzD1z_uxkBq7C9VWrmbwjcLigYccY48U7JwSHfBLo5rfcbv_1o5upXT8Ag0N0Er3ADNkETMnA7Yku_lMQ31leiYHFEZC1A7koMv9mKqySrCK1MDOAt9_sqaihX-Ca10QW5wU87qJJU4efB-JPlQXMK7l7PNFpjMU_ymlpiTEgn9Sk-PlIPB5WC_mYN4OomvZ6KV4HtW9E-oEgrG55cAfNCTQP-WU5gmE4g71H9aSyzIG4POodWDz3LCpf4-r2jhL3X7ZCI0mBFw4FX4wrNbKEzBVwng80OJjjIMjCGruEPsoIo7ptLIJiKTaJ0yYt70yzolHCGdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3efc1df48b.mp4?token=R45Jp-kzU2L6GVAzD1z_uxkBq7C9VWrmbwjcLigYccY48U7JwSHfBLo5rfcbv_1o5upXT8Ag0N0Er3ADNkETMnA7Yku_lMQ31leiYHFEZC1A7koMv9mKqySrCK1MDOAt9_sqaihX-Ca10QW5wU87qJJU4efB-JPlQXMK7l7PNFpjMU_ymlpiTEgn9Sk-PlIPB5WC_mYN4OomvZ6KV4HtW9E-oEgrG55cAfNCTQP-WU5gmE4g71H9aSyzIG4POodWDz3LCpf4-r2jhL3X7ZCI0mBFw4FX4wrNbKEzBVwng80OJjjIMjCGruEPsoIo7ptLIJiKTaJ0yYt70yzolHCGdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بهترین نوشیدنی حین تمرین چیه؟ حتما با دقت ببین و امتحان کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/663133" target="_blank">📅 13:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663132">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-LA7cPKk4mbNf0XYU5Vn-CoN0Yi0ATf24fwcQAiqciQFve_6KHzxSkBuBxevIRls3KHV1bEHnMdGteC3UVwviVMSJZz5MQDvePLFbvwOwyiHZNbcXa_pIZb8BcqNMuveP4tMr2ZUFlhvsEryhbS6hhYnAaw_598ZN2HnH6xzqvM5b-0R8G6PYutYqtFN-MqGMtoL_qDGjJzkWHPTPtZ-e7qmCRe_64qXw-e7tE5i-LFM4kA08vyi1GoaOpq-gyEzS1H4oqjJkBR7Ku-dZHSiMAW_6GH4v69q4OpenJ0eyjxe8AqG_kEfisekho4uSRYAhnopb61TfkjBqvDt4d3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هر یک از اعضای تیم ملی آرژانتین در جام جهانی، به مناسبت تولد مسی، پیراهنی پوشیده‌اند که روی آن عکس خودشان در کنار مسی چاپ شده است
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/663132" target="_blank">📅 13:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663131">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3cba0fe4a0.mp4?token=mCb2t165KXGSZC6YOeV4Z-2a3jM1mWU_Rqk05DGW-nuY-XB3yEunncURkNB49jjmEjE57JIPvWsr8PDdGdmZHc2jxi0vMxr-l8vZDHzomCDeZ7agomEFasWIjygEJHkFxirYuObhWbrqkcCPY5XkJT2acY0uuqRHLBn7hdOobjGe2PxzpFKw0TK1X7JBlrmCneC1tNPX-s-S3I2vr1ime-DX1ULeCiazhriZkDtqsqt_lHAXFJXB_FG0AVj0Od6xoDCnf0DIfwIV5wPExWBOzKzjThff6yOcqf9adTw9E_-JUHlLwZaBQDvcNmQyQDl79OIBoh9vzNZjz3_kSv9awg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3cba0fe4a0.mp4?token=mCb2t165KXGSZC6YOeV4Z-2a3jM1mWU_Rqk05DGW-nuY-XB3yEunncURkNB49jjmEjE57JIPvWsr8PDdGdmZHc2jxi0vMxr-l8vZDHzomCDeZ7agomEFasWIjygEJHkFxirYuObhWbrqkcCPY5XkJT2acY0uuqRHLBn7hdOobjGe2PxzpFKw0TK1X7JBlrmCneC1tNPX-s-S3I2vr1ime-DX1ULeCiazhriZkDtqsqt_lHAXFJXB_FG0AVj0Od6xoDCnf0DIfwIV5wPExWBOzKzjThff6yOcqf9adTw9E_-JUHlLwZaBQDvcNmQyQDl79OIBoh9vzNZjz3_kSv9awg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ادعای جنجالی درباره حضور نظامی آمریکا در عراق و استفاده از پایگاه‌ها در تنش‌های منطقه‌ای
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
آمریکا بر خلاف آنچه رسماً اعلام می‌شود، تنها پایگاه‌هایی نظیر حریر در اربیل، پایگاه بلد در نزدیکی سامرا یا عین‌الاسد را در عراق ندارد، بلکه مجموعاً حدود ۲۰۰ پایگاه نظامی در عراق در اختیار دارد.
🔹
همچنین رژیم نامشروع اسرائیل نیز خود اعتراف کرده است که حداقل دو پایگاه نظامی در عراق دارد و در جنگ علیه ایران، از این پایگاه‌ها و حریم هوایی استفاده شده است.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/663131" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663122">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0MFAWPkxo4ceJtHOUg7KQ7b7WJZaCZN8A-9b2vDuw7Sewt1M_e1njIZ0q-00NjDWT05jR-evU2UubOE3TV1RuoY6bA7D4La5V08BAf6enqwWpGp3BV-JnHYShC8sEkXl7F_6BMIhcMeVTaaC_WVRseI9lZPnvXtLSYDvO7-ViyPI5gXNFrxxw65uvPEpydwVx0x3-4zbeVolelG1ICte0RYooDu8lKybP4TVFA5QQHlx3piowf6sg5gf8WR-9SWAirvqT5Atma80GZDwRKVgzNEl4ozRnf-Kb0gp35r4gaKxoKWVyirhN4QlSyVzJeUNoOWCK0Wg0v-_7A0FIkklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6Uzx3HBTqhLCGG3DPN2v6FTq-cmjPHgxsZYALrWHRZQdtlvOBq41wWqVhTsAt5nKLCowZSZCNuKCbMeohj_1zBT21ULXPB5hliv0-T_zOXCRLZlFOQmxMIcClFJw9qw9CzhNA6FBjTuXAdakbtkdW--7XvNbcpi3wHjrqrg7IqhJayyDeRJ9kgxPRW0dte32Hie6zA3gptwXzJxgjnQWph1EQL9mlFeGv0WwvPndYLlvVRRv-JRTjorWxNAyanei41ciBwHJKYoiyd_L6lxNnl3iUURXKGfLsMu8wqWcuu-t0Stn2dK_n9AYN31MTNeRaKOY8vXW76YT5NMn9Uqmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2WjBOyjus462iVraEhu0xd1R0Q1b6Qv92Znf19Oymx5ySiY-l0qJ7NBypGlWktJ4ffwWovjaP3uYO0x4W3ozaWSUTGqKV4EDOVqzK5hrh5ADShP9NhWAnL0l2N3oNAYN5BfM-nMJ8l-Lr_5AoYLxYkjrPzt9AdJEC4bb40gNBzZV4uLOk6RlQWedUqGgcYvoEXv3nwRXZnHzF70ws7Fp3KuoeLA0UN8xelv1Ch7jaQGhxJb0UMFfZ-CrH8kwh1ieK4UxYjCfsA_-oW-Y1mv27A9_I660V5s5AvXXZ0AUabl3BsoJr176ELyY0EaSO7ergrrVWPYRdu4MzO1RK4VvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwwVthoIRRtj5aVfgtgTGdaQjd72UVSaMDPu7i4Xc_afT1lGuAPfPtqyQLK1J1NIGlxwZN3aWFLB0LQ12HWOwwAkzwupwyCRvSUVzAlmSzQvY01vqRkLVw8Jkv8Jsrf6oJx7TvBucVA-sXJwQ4AhRK4X7v-tSavoNRxC0Nni2dz9GdSREMWth67yVhk-X3BJy-NKwC7h0bAFKW8cu0PuQeLn0TzcwefnWj-r7VeMqtd1GuFggky3nCaN72zKCB3SVvGdxGdWhNLpkyxr6c0GvmBKdsJRshkMBhpUdhVa1ud9bq4yFJEzF4OejsJQojj8mNUFB1_FWe2Tu4KRThiZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCC_8T7PZWZqn320EmlNVI0DBtkCVkaXeLS4skZIigTyS7Pj9ZtewpO0CmQcqsZfzJc9BHy6tmXmIKw3DnY8Y5Mr7Dag4ckAFg9spjNYl-E_d047FoeqR5KUX9HYB94kZCLmUtpGSuK2qBBYYeGU_bRlkZlyCoAaZiVu3nkKYO4bK711SzuS10ZHkS89jinvWe8wlqeoUWvSxwW5tUhaH0gNdW543NAuWskPeWhnOab7BlFWEz0gTFgG8RIPlZiGJtM7n8OkCxK0mcC8jsYlekyNlP7HpcnFvwdhJkAdA0M1AOgi_wRQUoGmpHoNb6UXHuW4kLkvISdDIUI5lbEnvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZU2w_pmjNhdl_nj_o4K1QH3TA52sxttLP7Hp_lKCmjQamuVIv3HHpknBuIFlmewFxyHaJjeoHyCowvWNl2zd89ARDrRjz3-QwMZl5ssmwRUVp3qU0LZhLRFn8y1Unlz8zxDLnd2wTDQQIsltutRm6B8s-TFP6zjU9cAg88nD9Z3nB2VHULC3p1cDF2KnCg5kMj1MkxA_UiDJ3WimD37J7bIFeyQjFfHqUzI7l5P1dHaH4hC08gpy-W7oeWVF2LO28QkrsxZgwV6CTQvzBEx-KF4dgxHO9tvmLlF_J9zfzmBSlngy0CU9qxf6IsjCVxHvfoDAz5_CG5gAq-sBd20vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsnhF_WXlXAwc613RAfWoZvAXVjpmZLj7gilrkipJIcG6Ma6Gdwm1suV0rf5Ec39HYe6_Dhdj1rjJX6GiQ8DXFeqCwr0iHTr0A2ynaYvnNHFYdYu9o_vsz-YRcY6BDUahXsIXWSm8b777medcZi3r2Rmtltiv_RYbUQLJOmmy9Hs7r2fC5h8pykdc0tl8ysmcR0HGxbi1cE5lEzD0jQXSEq-5nccLtxUK1N2fv8rlUFueX9b-C3__cg9piHwTHShz-4mRHHLE6TScFlNsYK2CXovLCCSaniu3xTo6ATSLuN3NsVwe6FNb653ODExQHElXKfV_-Bfwre9KdGFdq8dxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klA9lPPrXP2XHjGobVnP30LWljGm09-iNoXgbs8zfOt3GVZPG9x62-n56sTFsbuky2Jnlnmjbb-CuZvCgxxJ-x5SvhDrs5uwj3f6pTIeJmb8mA6U7_ROV8nroZd0WwlYIjtQDK7BYQRORlhisSbTjW0bBPd8IGOsjW_FhOfRFGmUo_giO2T1Hyw9nG5xQiW35Sz3Eo3lv1yzktPhrpiJFW4rX-qq_tGe9emgF2QZ7FS_lEr43au14kBO2Ywu9yfKA1pjMbFrqPXiN7M7PmzdPkWMHLQYwaN_9-KKXwlYe3vZ06JKmneAOB1ucDmJ7Ouk8eL5dk5je7lwJQIvK55qcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ue_SR4QDmqo6yFOJF4FwEI5OX5c2wdWBUsP2L8TTNAQdDPebjJZT5Z_qMk-KWCD3iPq4IP8WLd0DHXKGy7maDWqn-osAZvo_Testud-FgV2wYQuaa1cXFt1C6QqJ0Jq2dKLE-re-TsStrKnMIpTRE_uKlwmu6X7aYVxXiEe220BFpjNxugq04WppNv4xGpUwMTxFq5UOKVlsWf8tS3OgsKJFJnHhDhtpDonXzGPXGBTG_8qWr0VqnXSZsbmJWvLqxKIuzVYkt8TY3zdt6CiqMMx6R6hX5RsyoDIwku8yp9p5qf14LgGEZPVqS7FHgrzHPh5UFXnjiSYRy8zvmZBHJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خادم حسینی
🔹
مخاطبان عزیز خبرفوری؛ اینجا محله شماست؛ تصاویری از شور حسینی و خدمت‌رسانی به عزاداران در ایستگاه‌های صلواتی که توسط شما برپا شده است.
🔸
عکس های خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/663122" target="_blank">📅 12:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663121">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c049db14.mp4?token=RYGO7reSJlDVKLTE5X7C9Mf46oW0tkyofbIOjC1Ha-O1QJb4l3huXqb48qcDiQCEJ9RUWPwd1W6AYVJ9mlaWpW89wWV4_cj4EwTmu9eamsFnK3OclGIvnqRTBOZ7gb0mPPn-KAQRnTDhqasCPwspQD2sl3U05SM391veyJu-faa2PGuQDJ3y0QGZmUI0NlolTKNrdvVY435D4q56B8o3P1H2b5BXGmPKzZK8h6dUiT0mMxLUnEItASIxU0MX51c6XkbO3j_wUjkFDwRxDP-TsHvhjisvYv76GEZ9r0RU6fBL8TnoFn4ibwekyNvv0RynnMAQ-HC8meYrktUAO9CPGCQL5suWTI6v9J7jGv98flkiEf9yjt6YxNNgmvwWP0U73E5mgtzmOVNYU_Si5XWbqdqHRzNdbDuHzrn-NKICg_YTsQcblVBRvDj-T_JN_mdoVZWNJvIrJs5A2QdihQJKx4bvFWI0We4KIsjcllDW6no6wjVgimP2LVIhfTUBIiztQu9dM6TKsBZFPOYxQdiVcIbt9A65Z5gVAsLKU4pb6tfe78ut5GM-GcLM9NNAkdASvpUgmr1LNM6hWN36r1GN4KTIbu8UBDn0-LWcJYshS06smZrZi7EG8dbguT7MTGs3HcZQ5sGVoDEcmD-aus3rU2KEo31HFahwNcR9dWiBAxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c049db14.mp4?token=RYGO7reSJlDVKLTE5X7C9Mf46oW0tkyofbIOjC1Ha-O1QJb4l3huXqb48qcDiQCEJ9RUWPwd1W6AYVJ9mlaWpW89wWV4_cj4EwTmu9eamsFnK3OclGIvnqRTBOZ7gb0mPPn-KAQRnTDhqasCPwspQD2sl3U05SM391veyJu-faa2PGuQDJ3y0QGZmUI0NlolTKNrdvVY435D4q56B8o3P1H2b5BXGmPKzZK8h6dUiT0mMxLUnEItASIxU0MX51c6XkbO3j_wUjkFDwRxDP-TsHvhjisvYv76GEZ9r0RU6fBL8TnoFn4ibwekyNvv0RynnMAQ-HC8meYrktUAO9CPGCQL5suWTI6v9J7jGv98flkiEf9yjt6YxNNgmvwWP0U73E5mgtzmOVNYU_Si5XWbqdqHRzNdbDuHzrn-NKICg_YTsQcblVBRvDj-T_JN_mdoVZWNJvIrJs5A2QdihQJKx4bvFWI0We4KIsjcllDW6no6wjVgimP2LVIhfTUBIiztQu9dM6TKsBZFPOYxQdiVcIbt9A65Z5gVAsLKU4pb6tfe78ut5GM-GcLM9NNAkdASvpUgmr1LNM6hWN36r1GN4KTIbu8UBDn0-LWcJYshS06smZrZi7EG8dbguT7MTGs3HcZQ5sGVoDEcmD-aus3rU2KEo31HFahwNcR9dWiBAxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صعود مقتدرانه برزیل در شبی که نیمار اشک ریخت
⬛️
🇧🇷
3️⃣
🏆
0️⃣
🏴󠁧󠁢󠁳󠁣󠁴󠁿
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/663121" target="_blank">📅 12:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663120">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhOW46K1xnGINKEmnwS4axCRmzB_6SJkv8e7yxpkVfVzX1M8pSPRAN_tISxDGAH7jNv24gEgjmUopTl7mS9njI4BKBvH30Xs-80BWjhD3IDMUxd6DR7NPi-jTHuu2WBKuqrSAWy4qwoummvnca1j3iMyddIhmDwSS9OF1pxXKE9K7BZ7jm6IzPIZMjGfAud-62L67CMZUHilUm5eyIdQkAePWvMjRSxiQoihe6xCPhBYAhRuVo1hn2UINksZYegI7fLd_wzKLEg1b6Ox4Ap4DfU24X7iWHLGo4tOlIv8ku1vAtdpVDeby17CvqRKWUM2rMpb1Ryn21CFd18kRVYr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دسته سینه‌زنی بزازها، سبزه‌میدان، یک‌سال پیش از ترور ناصرالدین‌شاه
🔹
عکس از: عبدالله میرزا قاجار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/663120" target="_blank">📅 12:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663119">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔹
رویترز به نقل از مقام آمریکایی: اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/663119" target="_blank">📅 12:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663118">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRRTNtdteVd666VSxkyLHWhusrLDE39a75GreUISzWf2pNSasxQzoiTp5zxYg3vFXhmeaC0HConGhu6DIEfbzY8o97eYi1Sq6athv1axicCgtvpqxoJYqTcL2kkylZkIox9CRNJYOhJytDYeGr5VT7AHSLqJ56rNDpcp4HspRxIlJvLF0MRfMIAbSw-mJN1cPdE5d5gBK2Bl84ODDULdkaGZaWLIC3CYShSD1_BTxPaJgNuIxuM6wwpFKqdoUfiF4Tng_Hktyc9oExc1DdFlAGm6oHWMnBCF5V6buf-I98v196_IGE61EsA6Jk10LfHp2VhHGwqtNzb0ujiXXbS5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
با این لیست ساده، مثل یک حرفه‌ای لکه‌های لباس را از بین ببرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/663118" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663116">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
اولین موج گرمای سال در اسپانیا جان ۲۱۲ نفر را گرفت.
🔹
سازمان پخش اسرائیل: آمریکا به درخواست اسرائیل، ۲۸ هواپیمای سوخت‌رسان را از فرودگاه بن‌گوریون خارج می‌کند.
🔹
پاکستان ادعای طرح موساد برای ترور عاصم منیر را رد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/663116" target="_blank">📅 12:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663115">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyAKGRcHAs3KWqkfzQ3QurIBniR403zjZ1R0Vi_zwBzT4xSxVAVTf4Rt5rJkixDvARcNtJpA_39O5oijD_Bt7qylS_YsPyiDGK3yVupBdbGYMnN5JKRJghasDkHRNUMJNbYdIZiGd4XKfBIMYvkb5-WUfO7C4SrgJM__HyVUt5euf2_a4oMeWqSRpQhTu2XbjzSVJ_Q0-5TBxoIhXl7WDHsBYiVPj6d48DhZ996f0E4sc9CyEqgv8KMBqxOEktBg2g6QWvyOSfADn_8w-2zhYduSDiUhxLHhLHnos5UvYb3NvkeF7MglrlybGxEFtzy3MqiZq0fuUu3BA_vQ2aafsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویر منتسب به حرم امام حسین علیه‌السلام در ۱۱۴ سال پیش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/663115" target="_blank">📅 12:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663114">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0f7344ff.mp4?token=OgBZzurU_nVJ8MnfgFBVoqKFXgYCCFhC22SYotgTcPgxGt9OfzutbbbY23oCzBU9Fz2sbvL799_KWwykXWZeBJCxaeqAsK4Iepj-idw14CURCeISNPQ37dWOaQBssF7jqFhqdH5UCDwfjDlS8Saesxa_8U-IT_9Fal4yPpB6uPg5xfDtNL8cNqeUbTrz8HAkPHYlzgCbsVUwz2wdtyoQMoaKrtSoqF9sWlHQO1p9SIXzW68h8-zpa9UgrV9BTNz0_CZjpEAhXE7Lc7Ia_JBcL25e1z0j3-_rixgp74Vw-WgmlhWiP4x1hftz54AVF8dXb4i2nemCTyRWu8tAENJhQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0f7344ff.mp4?token=OgBZzurU_nVJ8MnfgFBVoqKFXgYCCFhC22SYotgTcPgxGt9OfzutbbbY23oCzBU9Fz2sbvL799_KWwykXWZeBJCxaeqAsK4Iepj-idw14CURCeISNPQ37dWOaQBssF7jqFhqdH5UCDwfjDlS8Saesxa_8U-IT_9Fal4yPpB6uPg5xfDtNL8cNqeUbTrz8HAkPHYlzgCbsVUwz2wdtyoQMoaKrtSoqF9sWlHQO1p9SIXzW68h8-zpa9UgrV9BTNz0_CZjpEAhXE7Lc7Ia_JBcL25e1z0j3-_rixgp74Vw-WgmlhWiP4x1hftz54AVF8dXb4i2nemCTyRWu8tAENJhQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر خارجه آمریکا: هیچ کشوری حق اعمال عوارض عبور بر تنگه هرمز را ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/663114" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663113">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c08365c2.mp4?token=WEsMWL1WnUgruT_gbuI4e0mLHeaAHx_clGPdSMK_CqTU7UH-zNzKvVy1reAeOU6mn33eeRn4uVg7GC_PRVkWqERg-pe3VOQIn776cG95dJNdqFwm5l83JtjjMl-K5ffQjmIfw2WZzpUffliZUDAWvnBC7w72VEpXmDIE86_fzfSyZeIk1j4bYQ9Xrtz3rLF-0SwRKULO6zl1yHen-4_mGptoTquGdsyswY-4-xYgs14UplIFc0OUbPYkpI2oD0UVy6HPKtYxzkDV4kxCj8MazXqDjjqSIjuYc3ZVCAElz4DPQkVnkFJDVMHwCv7fRcOJUbaVVAUQM2dZIi-d__ibM36eIhAiZVzckgGWTBtKoAuTb87nWtaId7BFkf_RdHtw64kGYhFNnEmR3ebCrDa9vKJa69WLJuwVchL01Qj3yenZTNbdUfEtHnPpGu2oV2evYcvvDBYCwOxhDtN7jj7TYotbREtxuEMsFOW-Ab87iWGaDW8IfXP5ard2QDrnVugLGlhE-dBPEiyCKzBg9VwYv3m2dTLba9x6g3YJV9AVIP88qcWe1Sn8DApcFok01vJW5qSnsVsomZgEmtXUezm_ts5-eUCyiFwDR-XehaPU7BmcC1zaHZZbYQmxSb5r2S5XS-_RqpBgVBxO9fBPKJtw_YWeTvwenLTsOSjmMYcc6bE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c08365c2.mp4?token=WEsMWL1WnUgruT_gbuI4e0mLHeaAHx_clGPdSMK_CqTU7UH-zNzKvVy1reAeOU6mn33eeRn4uVg7GC_PRVkWqERg-pe3VOQIn776cG95dJNdqFwm5l83JtjjMl-K5ffQjmIfw2WZzpUffliZUDAWvnBC7w72VEpXmDIE86_fzfSyZeIk1j4bYQ9Xrtz3rLF-0SwRKULO6zl1yHen-4_mGptoTquGdsyswY-4-xYgs14UplIFc0OUbPYkpI2oD0UVy6HPKtYxzkDV4kxCj8MazXqDjjqSIjuYc3ZVCAElz4DPQkVnkFJDVMHwCv7fRcOJUbaVVAUQM2dZIi-d__ibM36eIhAiZVzckgGWTBtKoAuTb87nWtaId7BFkf_RdHtw64kGYhFNnEmR3ebCrDa9vKJa69WLJuwVchL01Qj3yenZTNbdUfEtHnPpGu2oV2evYcvvDBYCwOxhDtN7jj7TYotbREtxuEMsFOW-Ab87iWGaDW8IfXP5ard2QDrnVugLGlhE-dBPEiyCKzBg9VwYv3m2dTLba9x6g3YJV9AVIP88qcWe1Sn8DApcFok01vJW5qSnsVsomZgEmtXUezm_ts5-eUCyiFwDR-XehaPU7BmcC1zaHZZbYQmxSb5r2S5XS-_RqpBgVBxO9fBPKJtw_YWeTvwenLTsOSjmMYcc6bE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه به لحظه در عاشورا چه گذشت؟!
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/663113" target="_blank">📅 12:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663112">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeGaLYbuHDuytrUzFMxuJDtKfoFlS5pDRJ3hHFqLbkMV8JZILtiv1WUuDkyDco3izq85n8g8-koiTXjP4v4wLTGK9GTqAMbXl2ZDKHH9K_6O63-kwbqs_YYlFiDK_cDScG0WcbjFFosEwnbiI5YBrw1ZE9tKAuYki8rjhnRAdSbGycPmfu7x38bDD5EIMunujSi6rSuHxqlMqM26AhheIa9urJqOeMJnsKw4cuPDHVLfY6Zkkbp-opp9QdtA5w0frnGrxHSlsivzovOJRDf0gR31D0fG0CD2ZRoZpU4ION2f6_hLF8OXnsWh1ps8Chh15Mi-CdrLy_03wWQN7ZEKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فارین پالیسی: ایران شکستی بزرگ‌تر از ویتنام است
🔹
جنگی که به اختیار انتخاب شد به یک فاجعه راهبردی برای واشنگتن تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/663112" target="_blank">📅 12:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663111">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igyJ3YCBSfNwF8OQhlJfFT9RTLmVwDUsuZ7ASNO3Xm8cNT9PvsTNMPKrMwIArVJ8BRWt8YJLaSkn4qQpiBRQ5JRaHsjDoMdBGIgoAdGx2BWwQwfi3zAR1e3uK1JGrcEMZGCPzjGr3iEVrRPuIClH7eQv_tvtZEH6L8BWI264OmyeS7PNMUMoz8WOGcxz8PY2i9PQ6_2T1aMWd7lyZk5HVuJH0Q0w1K_QjPhn-eYctBkagHfLAsAyObL4jB6RrzBq1pTmZPNR0_RUyuf5MfXLmjWENjqJLygRaGFrn5fwLSN98JUsvdJobYXo18Ynr-2XxfX5LQuj0yclCVhRKqOr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
توصیه‌های بهداشتی برای توزیع غذای نذری در عاشورای حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/663111" target="_blank">📅 12:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663110">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4908ef9ba.mp4?token=SOkNSyrjn2pzQfXDqyddNj4_2ho2eIemgm1vAio5RuzjxtYcWSe34bVTE5o0HKYlzUbsPtMKN9IpQMd45jps4lp58PGwg2OPkcxn9fMk1IHGCP8P2tzgIMUQaD6HHnr1AV6PiG-8wSx_yq-O30ZWJm7pSIWnh-RcwgupzZeOuKBh6TYngwWvZI9RLEMV_QwoIzKHptLImmKPM2qSfiEFLG2sGeDnNkSK4Y7HOjc9J8iAsyLLJNOnl7AJKLTftnuzvjpG3EteUPMKPDjCB9EQ1r9ix9l1w4V_mhqFLx44l2uoU5h0T2xWTzxAZOpm6e3PfuaBjY74THfL5Prlm5Is84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4908ef9ba.mp4?token=SOkNSyrjn2pzQfXDqyddNj4_2ho2eIemgm1vAio5RuzjxtYcWSe34bVTE5o0HKYlzUbsPtMKN9IpQMd45jps4lp58PGwg2OPkcxn9fMk1IHGCP8P2tzgIMUQaD6HHnr1AV6PiG-8wSx_yq-O30ZWJm7pSIWnh-RcwgupzZeOuKBh6TYngwWvZI9RLEMV_QwoIzKHptLImmKPM2qSfiEFLG2sGeDnNkSK4Y7HOjc9J8iAsyLLJNOnl7AJKLTftnuzvjpG3EteUPMKPDjCB9EQ1r9ix9l1w4V_mhqFLx44l2uoU5h0T2xWTzxAZOpm6e3PfuaBjY74THfL5Prlm5Is84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
موکبی کوچک، بی‌سایبان؛ اما به وسعت دل‌های عاشقان اباعبدالله الحسین(ع). آبادان، زیر آفتاب سوزانِ حدود ۵۰ درجه؛ کودکی ایستاده تا عشق را معنا کند..
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/663110" target="_blank">📅 12:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663109">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔹
هشدار محسنی اژه‌ای به وحدت شکنان؛ با حرف‌هایتان دشمن را خیالاتی نکنید
رئیس قوه‌قضائیه:
🔹
مذاکره به هیچ‌وجه به معنای تسلیم در برابر آمریکا نیست.
🔹
گاهی برخی افراد، سخنانی بر زبان می‌رانند که دشمن را خیالاتی می‌کند و دشمن در توهم وجود اختلاف و انشقاق در داخل کشور فرومی‌رود.
🔹
دشمن از اتحاد ملت ایران، کلافه شده‌اند.
🔹
باید مراقب باشیم که خدای‌ناکرده در مسیر دلخواه دشمن حرکت نکنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/663109" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663108">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b805d990c5.mp4?token=W8NYNpKJXjVbXt52BJD32zLmrCLiXwVRtnul70CrBbsaiDpqo_U0Yc2wKTSyW-PvyZ2h2K0_bU6A3L9POB_Gl_7SOH93dcDtXVVwWG286QT_jF_ALssiMSJjzRyDpl_Ej5e_OgEFwkfxqvFrx1LJsPCc10K9DYn7hgkiRASTCmNORMf6YENEMdoILlw0V9gV-7tsIpJDkbj5rYMBse8MIC4pZGh9cWEZ9NFX6SKZ-d9m-NK0Gq9ltCKdgGJvFiBOBhpguFJL2_8-IVmw-ekqhMlRR9nsxgix0wqA9yzPAQ1_ISLNuEwC0rD16T41M5lpgvR23DS6FcR4cqt7txFuaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b805d990c5.mp4?token=W8NYNpKJXjVbXt52BJD32zLmrCLiXwVRtnul70CrBbsaiDpqo_U0Yc2wKTSyW-PvyZ2h2K0_bU6A3L9POB_Gl_7SOH93dcDtXVVwWG286QT_jF_ALssiMSJjzRyDpl_Ej5e_OgEFwkfxqvFrx1LJsPCc10K9DYn7hgkiRASTCmNORMf6YENEMdoILlw0V9gV-7tsIpJDkbj5rYMBse8MIC4pZGh9cWEZ9NFX6SKZ-d9m-NK0Gq9ltCKdgGJvFiBOBhpguFJL2_8-IVmw-ekqhMlRR9nsxgix0wqA9yzPAQ1_ISLNuEwC0rD16T41M5lpgvR23DS6FcR4cqt7txFuaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ایران در جنگ پنهان است؛ هدف آمریکا فشار، بی‌ثباتی و سناریوی ترور است
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
ایران هنوز در شرایط جنگی است و توافق‌های جدید صلح واقعی نیستند؛ این روند تنها یک وقفه برای افزایش فشار است و حتی سناریوهای بسیار حساس در سطح رهبری نیز در این چارچوب قابل تصور است، در حالی که بی‌اعتمادی میان ایران و آمریکا همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/663108" target="_blank">📅 12:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663107">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔹
آغاز نشست کشورهای عضو شورای همکاری با روبیو در بحرین
🔹
نشست سران کشورهای عضو شورای همکاری خلیج فارس با مارکو روبیو، وزیر خارجه آمریکا در منامه بحرین آغاز شد.
🔹
روبیو در این نشست گفت که آمریکا به دنبال توافق با ایران است اما «ما توافق به هر قیمتی را نمی‌خواهیم.»…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/663107" target="_blank">📅 11:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663106">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
بحرین: از تلاش‌هایی که به امضای یادداشت تفاهم میان ایران و آمریکا منجر شد، استقبال می‌کنیم.
🔹
سازمان جهانی بهداشت: خطر جهانی ابولا همچنان پایین است.
🔹
چین خواستار پایان فوری محاصره کوبا از سوی آمریکا شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/663106" target="_blank">📅 11:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663105">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8115e8a083.mp4?token=nCFAqPIpap922gQZ0vPXnX924J7t1n3wVt5E_fDEygBIkARV7mNrsW0YexONVM7Qer4Lt_KgWcbvS0Ae_bo2na6xZAzV5PI1oT0lyeCfM1cS-nwatfmliHo1TjmSqtQIn8o3Ufajj7yQ7F7jI51Oe4OZt-Br_oj3yFeF-mUaErQeAVdj8ZXbzZJn8xgFuk9IE_-gM6LgdTmArunip0eEnrIx6hBCCarbnTCtBWTKZJs-nqQqEQxLhNgozbvwb7rhYpSRUKkucr-Freg1Gi4tuiRTVmhBMCPUM1eIYqYu7fRm5L5-2NzwldSU5yF5KoCUTcKmZCLeXaNeyDuwDAQdew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8115e8a083.mp4?token=nCFAqPIpap922gQZ0vPXnX924J7t1n3wVt5E_fDEygBIkARV7mNrsW0YexONVM7Qer4Lt_KgWcbvS0Ae_bo2na6xZAzV5PI1oT0lyeCfM1cS-nwatfmliHo1TjmSqtQIn8o3Ufajj7yQ7F7jI51Oe4OZt-Br_oj3yFeF-mUaErQeAVdj8ZXbzZJn8xgFuk9IE_-gM6LgdTmArunip0eEnrIx6hBCCarbnTCtBWTKZJs-nqQqEQxLhNgozbvwb7rhYpSRUKkucr-Freg1Gi4tuiRTVmhBMCPUM1eIYqYu7fRm5L5-2NzwldSU5yF5KoCUTcKmZCLeXaNeyDuwDAQdew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ: ما در حال ارائه بزرگترین کاهش قیمت دارو در تاریخ با اختلاف قیمت ۴۰۰، ۵۰۰ و حتی ۶۰۰ درصدی هستیم
🔹
اگر نیم درصد کاهش قیمت را انجام می‌دادید، کسی می‌گفت شما نابغه هستید - ۴۰۰، ۵۰۰، ۶۰۰، ۷۰۰، ۸۰۰ درصد. هیچ‌کس چیزی شبیه به این ندیده است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/663105" target="_blank">📅 11:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663104">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACcui0G3ii9ZbnY7kfAWXxFJWJ5SySMVxNXcAvwcxRAGAQy1sqo-Cpdr331zvFhaYK4PT-Gvq3X8hHQ8Sh0c112zIWsM1mGiuou1AexLS6ASko9lIYUoBDEvfxHrhRRHMCQL1I7D9jN_AD5n0BCInjlQBTVV_a30vsLPvJJDdSTBaun6VD1yPKAz9UbDEb7weS5Im2vd_40tKs60DIdB5nA0Ibumf3esr4R2pzNC8xB86nM4zJEHMMPmsCwW1sVVwlHXuYUQgFqx5iodj8wAtihKNxDiSJPP_Qxsi5QOb-136ZSsTpHdAn9DNjji1TJN0c_x8FHLhd4k6fkLKtdm7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ردپای حیات باستانی در مریخ؛ کاوشگر ناسا مولکول‌های کربن پیچیده کشف کرد
🔹
مریخ‌نورد استقامت ناسا مولکول‌های پیچیده کربنی را در دهانه جیزرو کشف کرد؛ یافته‌ای که احتمال وجود محیطی قابل‌سکونت در مریخ باستان را تقویت می‌کند، اما هنوز نشانه قطعی حیات نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/663104" target="_blank">📅 11:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663103">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8f90b53.mp4?token=nLwpu672jDlMBmLni2xhp_7sW8cRDXsCGxeLl-IsAvviXX8xj3kqcA-4EEvxTc6vmyP2w1GyqKVLstE2_GRL4LPvp4-WNarX3WLgyUkFyDV6xyZIA84FN1mK2mnqnkh4j_sVx9EJgM8trOqjX4aoOtAwSVQ-zeTbgICMlWr6E9Wl-DsZ8p1zVqxD2hQdCdB-EK8TLbfub1ShAc5uBD75-KK_HlpyjW1vzKdpHW9PrGcpzNniEto9GVkaWal_IMEtrzPRPCIiW3h1njNckik1YYLeK8ZXSqvTayFih2dJVzDV5adnl2cmen8-X6Cew3kNVlQpDs8AZnSMMGqXzWKqsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8f90b53.mp4?token=nLwpu672jDlMBmLni2xhp_7sW8cRDXsCGxeLl-IsAvviXX8xj3kqcA-4EEvxTc6vmyP2w1GyqKVLstE2_GRL4LPvp4-WNarX3WLgyUkFyDV6xyZIA84FN1mK2mnqnkh4j_sVx9EJgM8trOqjX4aoOtAwSVQ-zeTbgICMlWr6E9Wl-DsZ8p1zVqxD2hQdCdB-EK8TLbfub1ShAc5uBD75-KK_HlpyjW1vzKdpHW9PrGcpzNniEto9GVkaWal_IMEtrzPRPCIiW3h1njNckik1YYLeK8ZXSqvTayFih2dJVzDV5adnl2cmen8-X6Cew3kNVlQpDs8AZnSMMGqXzWKqsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اين خوراک باميه بدون گوشت و مرغ انقدر خوش طعم و جا افتاده شده كه حتى گوشت دوست‌ها هم ازش نمی‌گذرند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/663103" target="_blank">📅 11:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663102">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNfmJn8IxwdWJV0QBRbJvzEoxOxkOKNEW0phkJ_Lt-pgiH6Ik2S-xxD3VAZx8tnJtr053OBdtEYn3SmdrqwkP74CfUVGg0zCYaJzBtz98Bl0uOZKK1LY5pQ_VH0yx8HfboLFRrME1EyUGFrVMIBEkYXZD_rBiRrbdKfQpybcKqSBqcf4YZWyZ1n2Pe8nD_gTBlGVX8dImrxxiAfNM45piuFtIgpRHXWMyTeb0mfhQc8_0BL4Rudthkwm5QnN2u1koqGIqr9oQJirodTSLNflemZ3HLT0huE1jS6sL1TwGm4VBejKDZRtpo7zqkoi2HWzj2YhaKTlsJAthJTu43opVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
آغاز نشست کشورهای عضو شورای همکاری با روبیو در بحرین
🔹
نشست سران کشورهای عضو شورای همکاری خلیج فارس با مارکو روبیو، وزیر خارجه آمریکا در منامه بحرین آغاز شد.
🔹
روبیو در این نشست گفت که آمریکا به دنبال توافق با ایران است اما «ما توافق به هر قیمتی را نمی‌خواهیم.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/663102" target="_blank">📅 11:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663101">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cac175f85.mp4?token=Cx7k-Fl4_uEvacc3H7L9WSOhDoG7YzxLyAQsmp2D3fSj-7FbvqqhdBH3PgmHiOdverUltNrr58db_GeMeypAuEPLNvPc5MYRYphMhy08YNGXVYRcwvuOa3LZI089vwZ4m4nYfFDHkCH5vCRW-InRJR6qH8yVnH7vDjfD-j5k5drhaxyBM_7bS-Colv7osOym9V_jiVr8zTCyZlc5D8L55edn37fUVzVtWheVNP6u7H3iXZqggHHBim4Sq5HdZf9WeDXGIiXz8fSn3Zx61rTky-LTOCW7FIexUHkptKvlGR_SnaSOuxtvYjIU1JnVsSYcHLkGgrZmm1Wiy7ajs8TA8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cac175f85.mp4?token=Cx7k-Fl4_uEvacc3H7L9WSOhDoG7YzxLyAQsmp2D3fSj-7FbvqqhdBH3PgmHiOdverUltNrr58db_GeMeypAuEPLNvPc5MYRYphMhy08YNGXVYRcwvuOa3LZI089vwZ4m4nYfFDHkCH5vCRW-InRJR6qH8yVnH7vDjfD-j5k5drhaxyBM_7bS-Colv7osOym9V_jiVr8zTCyZlc5D8L55edn37fUVzVtWheVNP6u7H3iXZqggHHBim4Sq5HdZf9WeDXGIiXz8fSn3Zx61rTky-LTOCW7FIexUHkptKvlGR_SnaSOuxtvYjIU1JnVsSYcHLkGgrZmm1Wiy7ajs8TA8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداری محرم امسال در کشمیر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/663101" target="_blank">📅 11:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663100">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-B4ZKK-FQkQAWCDppuirZa-iyscJYK7kmVNpuJ-mQlgsQGK6i1TH9wdM_8zBSWn_YhBOfJPk34E0wt0RztPj0k8lKe48ft4MPjrjIQyQ6uVZrz-mOPyeIUkkz1Pu8esGjIPEpDST_c6LlJ4y79wPBYn3MTwz37bY51pBZVpoQ0IUw20fxODmqtrJ0apUxMzboLQl-fUP1Yr_WFoUNKLbPdAL0JdaM7f0r-f3uC2d-aVn1sutacMYqQkIkwciTYfS0g73-mQNhm-9tsEfUQ1nqfmlvp6_tZ9hEmLSpeo1kcSt8SspiTx6L3thWAT1QQp9gMQpzP-yBzeinzdVUbTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهنمای ترکیب درست رنگ‌ها برای استایل آقایان شیک‌پوش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/663100" target="_blank">📅 11:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663099">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474ef034cf.mp4?token=r33MUYBz2ZJLl-aQOL3F6Sc833dDSQmjr29mdoPqzLrlX5AYz1AHkH946KGnlWSm52ynHULG-jBIbscHjk_B6IOtQDj9CBaqd2U6TbXJDnrdfJv3A_SP9ZhwxFJrSCGHjT4wHNrz9c0_H7W7nYTmyOwEezrETmEj5jy9lolU7L_gm0fksybCET1wsglq0HezXgLCPR4lWXTYnXMaBYOCv4ErmTUPAq7FWrRT9yz8-r84onJzOuOxjxJAU3b1ilOMvG6UV7NT0Zc9SEXWCqxjjz9l3daCBcJU5-pQbudadtLY9fFV4lZ7CNq78JD4lga61pjcsUFfzHfCPpX2uDAWeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474ef034cf.mp4?token=r33MUYBz2ZJLl-aQOL3F6Sc833dDSQmjr29mdoPqzLrlX5AYz1AHkH946KGnlWSm52ynHULG-jBIbscHjk_B6IOtQDj9CBaqd2U6TbXJDnrdfJv3A_SP9ZhwxFJrSCGHjT4wHNrz9c0_H7W7nYTmyOwEezrETmEj5jy9lolU7L_gm0fksybCET1wsglq0HezXgLCPR4lWXTYnXMaBYOCv4ErmTUPAq7FWrRT9yz8-r84onJzOuOxjxJAU3b1ilOMvG6UV7NT0Zc9SEXWCqxjjz9l3daCBcJU5-pQbudadtLY9fFV4lZ7CNq78JD4lga61pjcsUFfzHfCPpX2uDAWeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
موكبی كوچک اما به وسعت قلب‌های شيعيان در بعلبک لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/663099" target="_blank">📅 11:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663098">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10071cd098.mp4?token=Z4TtuhQ-iPbHxjy0ABZy6VWRfmiWxMinAPhlVOAaM39BmqfYzxXXepJ-UReYeB5-3v1OT14k-0hxDCLe7vP8l2uj_zoOK19xzPK3HQdz6mhXlhxQZWbWk85cpR2eXVfzURcc5H90Myz0TwM90FMKuKrY8yFKs9GFDMI6-CnPjIIUlsXQ_VIFHd5aMmMO4PqS6JStjDv6ZtuNWpuAQeeVyxs3yDcyekPWIkPlgztS3hn9fpr_sFLQRQXq-CpEljNlWna_6RL4WE_fX6aUY-BqkwrqnbeyNDXMpQUli9Qop1Y-N35zDanJCG5RjEW1KS8rMJa_8LvoczSDZ1GAugoHcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10071cd098.mp4?token=Z4TtuhQ-iPbHxjy0ABZy6VWRfmiWxMinAPhlVOAaM39BmqfYzxXXepJ-UReYeB5-3v1OT14k-0hxDCLe7vP8l2uj_zoOK19xzPK3HQdz6mhXlhxQZWbWk85cpR2eXVfzURcc5H90Myz0TwM90FMKuKrY8yFKs9GFDMI6-CnPjIIUlsXQ_VIFHd5aMmMO4PqS6JStjDv6ZtuNWpuAQeeVyxs3yDcyekPWIkPlgztS3hn9fpr_sFLQRQXq-CpEljNlWna_6RL4WE_fX6aUY-BqkwrqnbeyNDXMpQUli9Qop1Y-N35zDanJCG5RjEW1KS8rMJa_8LvoczSDZ1GAugoHcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توافق جدید با ایران صلح نیست، یک آتش‌بس موقت برای فشار بیشتر است
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
یک تحلیلگر سوئیسی می‌گوید توافق جدید با ایران بیشتر یک وقفه موقت برای مدیریت تنش‌هاست تا صلح پایدار؛ به‌گفته او، نبود اعتماد و تضمین امنیتی می‌تواند دوباره مسیر را به سمت فشار، تحریم و تشدید درگیری‌ها برگرداند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/663098" target="_blank">📅 11:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663097">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOFlBXufCjKuLVmJU38Jw2f1VID-Yh9Qt5vuecUqOXhMZX9jAXTBpLHOWbY8X9iELQYIuG_1CAUM76LyF0Jov5vReXxplkoPoUeWkOgBLhoJ4fosUxRWExl6Ehlt1GfNXEftdtUnm8E40wv2hmIEsaLgXXIu-kk4b1dtNBbJYAwfyfTP0bkpmJY4KpDkYF9KM9Rxc_088B6eeF8PjjKh2haa99kGXZD8rlgO43kxqRjuFM7iuHUL4DpyQhDQML9m75xxD0KW9I7GJgaCcd5Ba-Jv7ZomVQJ4Pn1GBsHbq8Y3h1FZvJFqncX5Upuz8OV_0y6YNOFLgmcPIWSX05r4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
لیست ثروتمندترین افراد جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/663097" target="_blank">📅 10:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663096">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
روبیو: معافیت‌های تحریمی نفت روسیه احتمالا تمدید نشود
مارکو روبیو:
🔹
آمریکا ممکن است معافیت‌های تحریمی نفت روسیه را تمدید نکند و صدور معافیت‌های جدید را هم متوقف کند؛ با این حال، تصمیم نهایی را دونالد ترامپ خواهد گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/663096" target="_blank">📅 10:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663095">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904754cbbf.mp4?token=TzwFlBPH0vPQIKkTKpxq8zkfcbWSL3mmzQLV0LwOQs3hUrU0hxWyOYyj6_cBingPFT9IolQZmUSJCHJtYWqhhqTYfa7e3GmJTAjALQIw7aeNB90PtC0S3F9JsFaJ_XfjDDzH-2Mfi2cco4Q_TUdLTJf0EXR0dQ29y1djFqhvrzG5iKOPpKm3ZsNiedYuL_njGS8mLsnbHcdHHJP56aV2QDrmgvZ9G7SyfgnxtNSliNObn7nqnXnPgmqommclG75PYq8sIyUP5TjmMJH2waZyQU79E2F4BfR1etOO-YeexK7dRd3q7KSRI5NZ4SzYAd9FEp-5rmN7mLs5pjdvAPq3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904754cbbf.mp4?token=TzwFlBPH0vPQIKkTKpxq8zkfcbWSL3mmzQLV0LwOQs3hUrU0hxWyOYyj6_cBingPFT9IolQZmUSJCHJtYWqhhqTYfa7e3GmJTAjALQIw7aeNB90PtC0S3F9JsFaJ_XfjDDzH-2Mfi2cco4Q_TUdLTJf0EXR0dQ29y1djFqhvrzG5iKOPpKm3ZsNiedYuL_njGS8mLsnbHcdHHJP56aV2QDrmgvZ9G7SyfgnxtNSliNObn7nqnXnPgmqommclG75PYq8sIyUP5TjmMJH2waZyQU79E2F4BfR1etOO-YeexK7dRd3q7KSRI5NZ4SzYAd9FEp-5rmN7mLs5pjdvAPq3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
یک ونزوئلایی هم‌زمان با وقوع زلزله از لحظه دویدن در راه‌پله ساختمان فیلم گرفته و شدت آسیب وارد شده به سازه در این ویدیو بسیار جدی و ترسناک دیده میشه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/663095" target="_blank">📅 10:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663094">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nr2PnrKx_Tm9Z8c9nmgbBd-H6NsgHTYTTZCsoLDr6ml7vQBOmh_ikrQ5m5vGPbU9fjWjcTY0aUVT-8I1qg96feI8lCSs40H5GkCFT7m4bM6ev6Ttp5vXrBgDefFcR2KW69j8OJQUaWc1elcCPHP6XDEPhXK93QaIXl3s57TRlVsOePZ0LALA5FWvAPX10vnitdcZ_jXme1CiFAeFpB5q-7xx9dtGLC9pr0qpHVAfNiCH5IgbZhW8cK02osTp4Mql_KxRwTfCKUxG_GdMmk5VppUkTXsiWUDFqQ48dv0T9CXibQPnWMMSfy5tvD9H4_FGSpF7eDfdW-mLFHfM5bLe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ایلان ماسک از جایگاه تریلیونری به زیر افتاد
🔹
ایلان ماسک در پی سقوط سهام تسلا و اسپیس ایکس در معاملات روز چهارشنبه که ارزش دارایی او را به ۹۷۰.۲ میلیارد دلار کاهش داد، عنوان «تریلیونر» را از دست داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/663094" target="_blank">📅 10:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663093">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/663093" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663092">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004eddcfe4.mp4?token=O50P92HwlKv_s4NpC83NjIfT70wZiVnXOv1tMSVjrDp_DX7oji6ICTWP4A36AK6nHPICgvhDsO7K2xy3vYrFK2A_YPxwp7AUqB1hKaqcH1ztAes6kurrrypDKUjUgkHm6k9VxJITq_fcmhmABqpb-74NsFPnDlk-i5o6YiLibDqPpcJe-I8ECtSIijawc5NAb8bstNP8llE-HlO0na2EQeXPexz4GjW5HEKlOmsXq3wsZSbuKTf7ObsQIjC5kcXdJPJVeoENftYp5f0IWa1cRV5EdEgmw8Qvvx6ByebISpvG5fgnIDYIaKQrkyg-6-FpNpBYYnMErNU3RE7Zucc7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004eddcfe4.mp4?token=O50P92HwlKv_s4NpC83NjIfT70wZiVnXOv1tMSVjrDp_DX7oji6ICTWP4A36AK6nHPICgvhDsO7K2xy3vYrFK2A_YPxwp7AUqB1hKaqcH1ztAes6kurrrypDKUjUgkHm6k9VxJITq_fcmhmABqpb-74NsFPnDlk-i5o6YiLibDqPpcJe-I8ECtSIijawc5NAb8bstNP8llE-HlO0na2EQeXPexz4GjW5HEKlOmsXq3wsZSbuKTf7ObsQIjC5kcXdJPJVeoENftYp5f0IWa1cRV5EdEgmw8Qvvx6ByebISpvG5fgnIDYIaKQrkyg-6-FpNpBYYnMErNU3RE7Zucc7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مکتب عاشورا؛ فراتر از دین و مرزها
حتی اگه مسیحی هم باشی، بازم به امام حسین(ع) ارادت داری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/663092" target="_blank">📅 10:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663091">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f444c745c7.mp4?token=Pmz6MLlviHLAIhycDPZg2AUyyc19MwLkLZC-SXF2f7VUMwhty3ni45kV_Wy08ErSrlULxoPjKIlj4g2A3yFfzFC_Apb7o9QfR1eWYsJ6g2sYqSvGshWKdvUrVx-5G698Uo-Gg3__9mB0sU8lsnYQMyoKUzZ548Sx6WFGdFgf8Bzpu-fvOD6s7IvakWSuGGhC3S3vDl70S0ppI2VXhMN6gDU6L_QuKfGd8KMzj-XHXft9sFAfaEa1B2g5d4I0OgsPjgjB25stQ6KjLAv2TgyENRmKXCiQMQwM2ZV8N8qkp_Gf_NssrMOlFydQjwFbFZoLEI-T7qTxJtzHXlIbahhHOGKMnwGkyab6mHGRfRt4FiQuAuY-cu6iCCBDesi-S4MoT2ulc6gl1JqHvimOaTfOmFiJAX6F8xEr26xETJH9V_ym0FZpZK_m4BiL4HMfXgw1FjmfcgFxjB7yT9nZRWCgf-Lw6z7GQkLWfmictTeiDof9Dkws4R-HoGNqYzybPEEVTSiRFVPDYBRQR3Hpy6Ye0OcVBnxmGsan7vCAnGa6bLGKpeNDhYRcjkstwV5wwCSY-5alurpzMi1bGpwhQ0Pd7idrB4QWvlZUF5xPMQ4bvtotLibwpf2t4bR4YZSB_VAKlrvgNEOuQIUIyP7MeeTMM3z3BXAAkdmdl4i2-5Lco2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f444c745c7.mp4?token=Pmz6MLlviHLAIhycDPZg2AUyyc19MwLkLZC-SXF2f7VUMwhty3ni45kV_Wy08ErSrlULxoPjKIlj4g2A3yFfzFC_Apb7o9QfR1eWYsJ6g2sYqSvGshWKdvUrVx-5G698Uo-Gg3__9mB0sU8lsnYQMyoKUzZ548Sx6WFGdFgf8Bzpu-fvOD6s7IvakWSuGGhC3S3vDl70S0ppI2VXhMN6gDU6L_QuKfGd8KMzj-XHXft9sFAfaEa1B2g5d4I0OgsPjgjB25stQ6KjLAv2TgyENRmKXCiQMQwM2ZV8N8qkp_Gf_NssrMOlFydQjwFbFZoLEI-T7qTxJtzHXlIbahhHOGKMnwGkyab6mHGRfRt4FiQuAuY-cu6iCCBDesi-S4MoT2ulc6gl1JqHvimOaTfOmFiJAX6F8xEr26xETJH9V_ym0FZpZK_m4BiL4HMfXgw1FjmfcgFxjB7yT9nZRWCgf-Lw6z7GQkLWfmictTeiDof9Dkws4R-HoGNqYzybPEEVTSiRFVPDYBRQR3Hpy6Ye0OcVBnxmGsan7vCAnGa6bLGKpeNDhYRcjkstwV5wwCSY-5alurpzMi1bGpwhQ0Pd7idrB4QWvlZUF5xPMQ4bvtotLibwpf2t4bR4YZSB_VAKlrvgNEOuQIUIyP7MeeTMM3z3BXAAkdmdl4i2-5Lco2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
یک ونزوئلایی هم‌زمان با وقوع زلزله از لحظه دویدن در راه‌پله ساختمان فیلم گرفته و شدت آسیب وارد شده به سازه در این ویدیو بسیار جدی و ترسناک دیده میشه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/663091" target="_blank">📅 10:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663090">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e27b871710.mp4?token=N_wn9DqHpCgRRnPnOCPCvOiUoHmF1EBBWrBI9PCfaM5UDFn8H5sodQ5z01ZqbZPjkEMnyVhExBKXhciRH41pFwDECC2_K2ZuWAkOIKV7hUM8ZGIizQHsOtFKAVxd4SSxjqjsbkAf2JXK4OddWjWQLC_1ngshSsrznYTjI6TzMKWdmLfI8PUBUiPI3djxHquJWOIUZY4ebhyw4rZKxwu1jDCi_Hl3swLlnxnGchjEz2yxZvnLxDEhkOYwbejcxejt19gcORRxVe6QKz46BUbsba9aYbu0x2WNXFHRfdFB9qCWoRyCxQKytwCN6DV-Mm_cOxier2KTRwFYsl8zONXalw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e27b871710.mp4?token=N_wn9DqHpCgRRnPnOCPCvOiUoHmF1EBBWrBI9PCfaM5UDFn8H5sodQ5z01ZqbZPjkEMnyVhExBKXhciRH41pFwDECC2_K2ZuWAkOIKV7hUM8ZGIizQHsOtFKAVxd4SSxjqjsbkAf2JXK4OddWjWQLC_1ngshSsrznYTjI6TzMKWdmLfI8PUBUiPI3djxHquJWOIUZY4ebhyw4rZKxwu1jDCi_Hl3swLlnxnGchjEz2yxZvnLxDEhkOYwbejcxejt19gcORRxVe6QKz46BUbsba9aYbu0x2WNXFHRfdFB9qCWoRyCxQKytwCN6DV-Mm_cOxier2KTRwFYsl8zONXalw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تحلیلگر عراقی: ایران نیازمند «خانه‌تکانی» در روابط منطقه‌ای و بازشناسی متحدان است
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
ایران باید با انجام یک «خانه‌تکانی واقعی»، دوستان واقعی خود را از نیروهایی که می‌توانند به تهدیدی علیه ایران تبدیل شوند، بازشناسی کند.
🔹
ادامه نگاه سنتی به برخی جریان‌ها دیگر کافی نیست و ایران باید با رویکردی انتقادی و همه‌جانبه، به‌ویژه در قبال جریان‌های شیعی و معادلات نوین، در روابط خود بازنگری کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/663090" target="_blank">📅 10:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663089">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b651e0520.mp4?token=WhlHBuQjWxjSXkzq03cDH-tFzINCTmetD_EqUGN-EY5wmGQwbe8lwwhmWdLYzhvf1COo_QM27XzF5CfxO-F5BjgqxXPv-8Q2aMTvPDWNqyYT-U31XoBYsW6MUP3s86fSsluV1kizt1ITFpksqXxjmteiOz4EQpT2L0LRuR5DVv9VIvn1s0CRD6dj8c9c5cecxgnru1jzNm4FNRaCrVQkB-2B6RQHEXm4CpnhNbok48Hzm0Y97ixrYZEiIiX6CFXBZIIoTA8TJ5t1dtwbrVhBy9Gd71gfHRx_SBgpVkWRQGG82DaGb4lC8uHWmP8xuwaHmdq5xUj5WR4BjhXJZAeRSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b651e0520.mp4?token=WhlHBuQjWxjSXkzq03cDH-tFzINCTmetD_EqUGN-EY5wmGQwbe8lwwhmWdLYzhvf1COo_QM27XzF5CfxO-F5BjgqxXPv-8Q2aMTvPDWNqyYT-U31XoBYsW6MUP3s86fSsluV1kizt1ITFpksqXxjmteiOz4EQpT2L0LRuR5DVv9VIvn1s0CRD6dj8c9c5cecxgnru1jzNm4FNRaCrVQkB-2B6RQHEXm4CpnhNbok48Hzm0Y97ixrYZEiIiX6CFXBZIIoTA8TJ5t1dtwbrVhBy9Gd71gfHRx_SBgpVkWRQGG82DaGb4lC8uHWmP8xuwaHmdq5xUj5WR4BjhXJZAeRSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
موکبی ساده که دل‌ها را برد
🥹
🔹
دو کودک با برپایی یک موکب ساده نشان دادند گاهی سادگی و اخلاص، از مراسم‌های پرزرق‌وبرق تأثیرگذارتر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/663089" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663088">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8oUQlYVrt77cSfN9RugZGDFBXca1USio0n9BPTmAIBHLLzT8uYVIalY2tFF0GQhEGvZyWCdJgmwbtrv-todF3_NJCe6LXmP54fjaZ4_u2YaPy85NUFuG2ensi9diqq6SF1RoSA1JjV-IbjZWHKeNfyQy2g6dvi-aGEzQOSn-a1lSdw4iWNLP6prvCGbDZme1vKIWBtO55aXDoT1g4IVzLrTR8gfvv_QZZ4vcs9906VG3s9idO83M7T7WFisARfHIHTVALYPH9qZvnWELaZ_rSl81guZXMLapkVwAH1c64ok-1kC1z8_xNVGFHrmbSQVC7xxkR9p4tiT_ZhAfp4n2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تاسوعا؛ روز انتخابِ ایستادگی
🔹
روز نهم محرم، تاسوعا، روزی است که فشارها به نقطه نهایی رسید؛ فرمان جنگ صادر شد، امان‌نامه پیشنهاد شد، و یاران امام حسین(ع) میان تسلیم و وفاداری، راه ایستادگی را برگزیدند. #به_وقت_حسین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/663088" target="_blank">📅 10:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663087">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWJ7XfFgKHQcBDTkLQZENuxZkbxvPsW2hqRSzgBp55idKBmDnO0xPdCnebdG5KnDPR6vQC0A_R3ipggIf0Q3KGrpjMu8Ow3bwNsmPwh7fKZ6fe8HyQi6lrxjGiEntTtCRB3fDo6sSDFcGBmRJ2RakdT8RCrhSsBRLyVmYGOkfPbvne0Dr6xIqNrcqAZpmCcVOP6q6uqx4J4ivVbfKevcMy6cowGROi2b0RR-Qt7LykIdRu0IXcJqvvo8QD1YnbkA3UZd2OrmVr1K4Xgh5pxSUQqVMBM25TRomu4kgFlAI3vxw5y478xRaReeubd2h4p2v9VQ-TAXanxTyFJCSb71yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
باز هم برزیل-اسکاتلند و باز هم زلزله‌ای تلخ
🔹
بار دیگر هم‌زمان با دیدار برزیل و اسکاتلند در جام جهانی، وقوع یک زلزله شدید در نقطه‌ای از جهان توجه‌ها را جلب کرد؛ موضوعی که برخی آن را تکرار یک «هم‌زمانی عجیب» با زلزله رودبار در سال ۱۹۹۰ می‌دانند
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/663087" target="_blank">📅 09:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663085">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlAbm1WMRiCaMe_Cs0lxTFoPGuAe4JpTtnanInVdLpfgVvH6PQvIsiSX5ws08evJllIkuGanZZH5w0OirbRK0YQ3zm3cKYmJ31dkaMx3zOaiZYZNVQhSuOLDbT_qs-irjduI_2kTj9nlf7M7DmS8MKEbsjVRQFJuAJ-15se-6pV48noRWLiDZPT7tKpe_Unh0L8_eJ1rZze0vqbB7_dJKAbNPTq5qBQ9VdnpnaKW1908_qx-SODvlKFvwFMKjHCOFjZ-R9rvL5UmzX3ZkfrV2qEuYFFlKMpKqA8rJ6D8W66XyACt-3Id7uZsrGbAj3DcvbDkgq802ShM4es8rnCVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruSV4pdTKgxWbisnsK26BvmWvxdIm7IaMdxxW6L_BQfXqXBCStiI1VyyHD5wFmL7Uhcf-Ek45pzQYZIO1tKewzgc0hZJH22z4QUgnaSMTuNm30_r5b1oGTJftAu-MEK7qdOk1DaInrjh9qI5abU8IoPCPMEV816e4c-8W-aHfjSwBxjJW9A3QUSlaI1JzVmgPfIwDAt1sIbqfUfavn3L3f4s_-oHCQYh5J4Ho3qi0t0KLtq0itR63sXXtX6yxwks-A54NcqpLqOWP4c3MbYZkGSuqAN58ZAmR0nxOVXEO4G2pGjHeKEhPniPeV6Y5CD-dltEBcHQSj6OMGhy7zBaag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم های راه یافته به دور بعد و نمودار حذفی جام جهانی تا پایان روز سیزدهم مسابقات
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/663085" target="_blank">📅 09:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663084">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
کاسبی جدید برخی جایگاه‌های متخلف سوخت به بهانه محدودیت کارت
شیرینی بده، بنزین بزن!
🔹
محدود شدن کارت‌های سوخت آزاد در برخی جایگاه‌ها باعث صف و نارضایتی رانندگان شده و طبق گزارش‌ها، در بعضی موارد متصدیان با دریافت مبلغی تحت عنوان «شیرینی» کارت جایگاه را در اختیار افراد قرار می‌دهند که تخلف محسوب می‌شود و موجب سوءاستفاده از شرایط و افزایش مشکلات سوخت‌گیری شده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/663084" target="_blank">📅 09:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663080">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsn6QkrX_lB_FvjGx-yj8D4yX9T3XLqvAdIwdKLmsccuK45WpJqkIhj1m7dyVW5bqQY93jCFDdzL6Q5pxG-tN21cHavZ4iE0WaMkjXD5WUTY5isvtoTqNR_2JHLJsobUKJ1Y6nMXEMfO4m00sM2GC9copS31kUYQW6li7bYpZRqV64_oS__mZAVtRktcOiIVFiZ9V4iRGIZT7HS04OpV3QwAXNpjxXcCjsm8_FWTHLnLMVAwUDJ0I9B8TaaO8ZVMsIoF8cPXCS6Bqw0z89ffGIrCBXOzwUhsgYNs8P2qRwy1fwJS9FpSXhzJnHyi2eUIRwy-1ca8RIbNMGEeyvbRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RP6eT5fEn48qGfdUm6dBKulQr5pTGI85CvkaskEAlZXdtTF5IFOe5e14x3wn-jqSW5LmoSHGQ9HwMkjFPf-1AXNo8s01cY8jwMNtG9tA3BjppWvFO6NshWJxcElYQ_EEpkE8OBpnjg9x5m3RW5ATPOTcN21LWU2ICs4qf07nhZ3nquuYXTBwUElCcEY8SrquDOFlBJs0sldSGwBu2U7GoSyqqKwPAdEPOjpZCvbcGx2-5E5-0y5e1FgWlAkLRKdQgzZs5gyuvIO5YcDQlyM7TX_sv4fYLf-VSvQWgWOZ3CqvCPCOirOZ7uncf1rVPbJ8ujDbxpL7mwb6XEnjLgZSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njzGSOKDvKKbEOdEwjZuOOEhLNadBkzyanDTplL7ebijLjTBS30hMEhigkru3A_eX-bnyqs2IVTCPA1LdHFmKJo81pX2m4HX7ARAOS4rNCOo43GKl31kVLkENPeqNl4rhoE1gnYsWVNvkLz-pVX6Qdbnr6D85erKYobmcbN_U1lkuSycENVsaO89II8q0F5Jp_xC3uwZT1dY9NniuqijUB_fAemqEF9fKI9Bn4XA2TIjwgj_QMcUQ4A3v1nYTa21nq2SLWIEcifebfKTTbGpoF1R-8uZ8NC_cTJetUPaiBiysZWa43Gp8Obhwt5zuDt2K-JeAMxBJ5sN04x71FypEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDHuQUFIsF1XavXL6n9y88GMp0N1wB3L271U3iA1gQEH562lkvoE1FjUosXuXgzq4Kx8s5CSH4RbpfFCZ53R9QJVz0UgGqQnEQnVjYDuDBAiL3o32UjCcyw08FAabwnJqzPcskTCgUkKIS78wkyZ4ahraWRDKhbtKscomMH3ygGNmJLbdw6fbiN715vhc7UR-_ZHE4EjYySd3eKRA433Zb6vexQIHShQfWKSPMhBkcAHOcq96ExXoLt-bEG_9jCC21m1f_8e_yCEdM5-RaQf7ntvYgaIZMyPN0oALynmcgJz72S-a16wIagLvfUjOFWkbAPPYOoPWnXTn-Rxv2fGhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
ادعای فعالیت یک گروه ناشناس برای «آزادسازی حیوانات» از مراکز آزمایشگاهی
🔹
گزارش‌هایی از شکل‌گیری یک گروه ناشناس با نام «جبهه آزادی حیوانات» منتشر شده که ادعا می‌شود حیوانات را از آزمایشگاه‌ها و مزارع صنعتی نجات می‌دهد. با این حال، هویت اعضا و صحت کامل این ادعاها مشخص نیست و جزئیات فعالیت آن همچنان مبهم و بحث‌برانگیز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/663080" target="_blank">📅 09:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663079">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOBhc9l-esOgEPL8iPIR0vOT_6-26s8LMRoYX-0dVB9b6DDonO5jLhrqggQfsS88KhHT-n-EJTYkXczXUbkptABLDvr9SI4p1rRnHN4LRPp2_nQM2P5NSnHMsq8v0sVkdea2s9P-2ta54c7sJBV84ahW908jC0KcuYyvYOwVxEJl9Prg3p2kCYy51lSboYngYcx7OTskr-LBNWCUr0eY0QzawIyNpT04DgNIn0i_A7Asfn8lfAjdMvS4h5zQsQdIv48uxVdWawIMzPzAEsxk4ziowzS_IMlB6S711iwvvXq_DaD8j7wmuVzzlOINqP9fjyjJsZ9_wN5CcYp4R3BB_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ویرانی آخرالزمانی ونزوئلا پس از دو زمین‌لرزه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/663079" target="_blank">📅 09:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663078">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_u-gy0mvBfTs5S72pK1DTCrd0P7Qc1N68Smuf9N29M1vkcp72O0JU-XctvkFKwS4Afz3LFgh48OduzlTua59XFe1jaN_s695kC5CVGgQ60fuGkg1uOJyeyF2boaOvLjISoc8vhlRpQ_THv3hNjfMU78c_xoD_i9LtmuQHvlxupYfTKUktLknkhGu1z65ZwWiT0sqKyY3do-GzPjYKheRIiCziP8OB15ZJsddo_j6pez9Byo-Q8BblARlfgdX_DumHXaCHp73zJ3XEjDhmiXd__q2B0jSLalE1X979AUteffaDMI2RzY1zVFeQD8iyxDyrMuAenMxZr4fDshqj-cXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت جام جهانی فوتبال ۲۰۲۶
🔹
همراهان گرامی خبرفوری؛ برای شرکت  در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و با لهجه شهر خودتان، پیام انگیزشی و انرژی‌بخش خود را به تیم ملی فوتبال ایران برسانید.
🔹
در ابتدای ویس، نام و شهر خود را بگویید و با صدای واضح و رسا، حمایت خود را از ملی‌پوشان کشورمان نشان دهید.
🔸
صدای شما می‌تواند انگیزه‌بخش تیم ملی در مسیر جام جهانی باشد
👇
#برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/663078" target="_blank">📅 09:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663077">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1d280aa80.mp4?token=l5MkK3S43eFycOoC8HDFpbvjvtbmlGqbbpktCWw3RaRiLm__HlnsjyBm9bsnDlVv7GEy8-u5xvziETInGIQ6gNG5AomshTQ0OJjzD4pt6IpmnsTSXIQ58QP9NmDkqVwNdYbzHNzElkSZbQsTs2qhhECDd1qy8JYsM7MzpvGrfFVRXFBsgDI9-KaoBFskeMxe10zSHJ89azHRKxzlj6hb-E443DXxfJClAmD3A1CO1odsDU7DgyMFBuMVjiWx1SRzr4zChZyFJQ38R1Ul3j-2_9quEty-2zMfVcvnxcpV19dDQ2FhKCE_ZyScAlYSLmWmeCiZpMqCCybZ7tkWzTQi6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1d280aa80.mp4?token=l5MkK3S43eFycOoC8HDFpbvjvtbmlGqbbpktCWw3RaRiLm__HlnsjyBm9bsnDlVv7GEy8-u5xvziETInGIQ6gNG5AomshTQ0OJjzD4pt6IpmnsTSXIQ58QP9NmDkqVwNdYbzHNzElkSZbQsTs2qhhECDd1qy8JYsM7MzpvGrfFVRXFBsgDI9-KaoBFskeMxe10zSHJ89azHRKxzlj6hb-E443DXxfJClAmD3A1CO1odsDU7DgyMFBuMVjiWx1SRzr4zChZyFJQ38R1Ul3j-2_9quEty-2zMfVcvnxcpV19dDQ2FhKCE_ZyScAlYSLmWmeCiZpMqCCybZ7tkWzTQi6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
پرفسور مطرح انگلیسی؛ ایران دستورکار خود را به واشنگتن تحمیل کرد، تهران با دست برتر پای میز مذاکره نشست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/663077" target="_blank">📅 09:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663076">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/221697eaf0.mp4?token=gP1nELkHKQbTL2wjUoX7nxpDOMGjlMRV9GzPo5PBR-DXWo7LlnzkC2xKUSc8ous2IDYS2QXcO2YUWZgc9u-m6RgWxYZxGXAaMDJJIz8bCrfrU6YQQC8RDfROvR5Lt05yq54LSLFvH7LXvxQe19CWvQ4BkuhSgXMZQ180JO4L0lQtBKo6q0xG9DEkWYAmI526G8o7kzVpyidnq1RQPkkSSv_mqezCDUA6C-KWl0pvFDWA8bWu5qV_B9Xt3jRxip_64hiKij7ySOHYFmeMi9pW3DQq19AZ9ldg0bn73qm4oRrRaujyfPfOXUAlnrhBSk318BUZq_KYD_ap_S0mKBwFrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/221697eaf0.mp4?token=gP1nELkHKQbTL2wjUoX7nxpDOMGjlMRV9GzPo5PBR-DXWo7LlnzkC2xKUSc8ous2IDYS2QXcO2YUWZgc9u-m6RgWxYZxGXAaMDJJIz8bCrfrU6YQQC8RDfROvR5Lt05yq54LSLFvH7LXvxQe19CWvQ4BkuhSgXMZQ180JO4L0lQtBKo6q0xG9DEkWYAmI526G8o7kzVpyidnq1RQPkkSSv_mqezCDUA6C-KWl0pvFDWA8bWu5qV_B9Xt3jRxip_64hiKij7ySOHYFmeMi9pW3DQq19AZ9ldg0bn73qm4oRrRaujyfPfOXUAlnrhBSk318BUZq_KYD_ap_S0mKBwFrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
آتش‌سوزی مهیب در پنسیلوانیای آمریکا
🔹
آتش‌سوزی گسترده در یک کارخانۀ قدیمی، شهر آلنتاون ایالت پنسیلوانیای آمریکا را به‌طور کامل در بر گرفت و مقامات محلی از ساکنان اطراف محل حادثه خواستند فوراً منطقه را تخلیه کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/663076" target="_blank">📅 09:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663075">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1130329983.mp4?token=K1BClWRM2ZNDm1cwR5f9a55aeOG1vWUCzDE3oyHPSWtIL6_NGF0whsmBy4xEuxska1aaozuoyltBjcgRgjITClvcf-8jY9pLFZl_kzO07TCAFiCxqEh56CBMYojw3MM6EX8C6q8xLp2sa8WmapgdJ_BVUcGPYMlFebaVrqx9vix8J3n8e06ozStQeKn1qlFH3NqQcfe9TkEZUo-hqwuH7P8o0xKOKwLMNS2np1cEqUdj5nU4B2eTS3cRnhUeOujLNzrujdo0fCYF7cb4BxAy4QGOxl_d0MxWI_cJBe4aN0jhJVU4jHl4n0W6hKwZSPUeX6FdY0WJjnKbQTQPLj7C6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1130329983.mp4?token=K1BClWRM2ZNDm1cwR5f9a55aeOG1vWUCzDE3oyHPSWtIL6_NGF0whsmBy4xEuxska1aaozuoyltBjcgRgjITClvcf-8jY9pLFZl_kzO07TCAFiCxqEh56CBMYojw3MM6EX8C6q8xLp2sa8WmapgdJ_BVUcGPYMlFebaVrqx9vix8J3n8e06ozStQeKn1qlFH3NqQcfe9TkEZUo-hqwuH7P8o0xKOKwLMNS2np1cEqUdj5nU4B2eTS3cRnhUeOujLNzrujdo0fCYF7cb4BxAy4QGOxl_d0MxWI_cJBe4aN0jhJVU4jHl4n0W6hKwZSPUeX6FdY0WJjnKbQTQPLj7C6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وضعیت کاراکاس، پایتخت ونزوئلا در پی زلزله ۷.۱ ریشتری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/663075" target="_blank">📅 09:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663074">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48a41c9af8.mp4?token=TlxgGTmXz5UELhOI2mUkOP_E2MyVCsOoGaLpXxVQSltba8kXj44iK8qryfoS2zKPH9rcs4SZ07Dz0ia0wvj_By8j0puj86hwjjsh2fDdvTKrJaJBQLb4dPqMIxgEOYppgEmNTV1-4NEgCkNA-E0FlRqbfYq7MyI50-5iQubQScRPu7a0jmRTPdq8R6Sm8tDx8cTwnUi9kBLf69hs1nSqgpZ709H3XBF0Z5rDaxHyqgKSO-d8dUlmaKAyLbet7yBv_ppfUCtmeybPOO-KrSFcqpHifP5QBn5xyHC04F-8953pYWpnmHL3uEzWDz4Jdu5PCG0FZ9oqHt8W7CATnzm6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48a41c9af8.mp4?token=TlxgGTmXz5UELhOI2mUkOP_E2MyVCsOoGaLpXxVQSltba8kXj44iK8qryfoS2zKPH9rcs4SZ07Dz0ia0wvj_By8j0puj86hwjjsh2fDdvTKrJaJBQLb4dPqMIxgEOYppgEmNTV1-4NEgCkNA-E0FlRqbfYq7MyI50-5iQubQScRPu7a0jmRTPdq8R6Sm8tDx8cTwnUi9kBLf69hs1nSqgpZ709H3XBF0Z5rDaxHyqgKSO-d8dUlmaKAyLbet7yBv_ppfUCtmeybPOO-KrSFcqpHifP5QBn5xyHC04F-8953pYWpnmHL3uEzWDz4Jdu5PCG0FZ9oqHt8W7CATnzm6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شرکت فرانسوی "سن لوران" از کفش‌ های جدید خودش با قیمت تقریبی ۸۰۰ تا ۱۲۰۰ یورو رونمایی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/663074" target="_blank">📅 09:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663073">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXi0c9J-721msXeVW2Jr-U_OFw0tIbNpboRAtAfivdAPWYfn5ZeIlJpJ2mV0BJPEXFG5Fl3mADgYdAEnXnihgeBrJRYFYGJI98ElhHQULc23j1jEYoFcqpo0SmmTV3u0uxWHiEsuAPdIN3PjCAD3QcZy5FjVkt5SVF0GUzeVePIhWv-Ez2dlL6yAa7fCVim0CwxoTlfukNSlUB2cs7gZF0MmzChkgrJq4EX1uzmZYcI4qK8_miU9_DZODHkRbAhaiWODtso8NTWTbw9RF526Msek9U7N4ze-IOIfuxeGo1rz0-Gh_3boAaHIRg0OSiK10uFQdQflYH1FK2QTPf3CIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخریب کامل ۱۱ هزار ساختمان در جنوب لبنان به دست اسرائیل
🔸
بر اساس گزارش سازمان ملل، از آبان 1404 در پی حملات اسرائیل به لبنان، ۱۱۰۹۵ ساختمان در جنوب این کشور به طور کامل تخریب شده است.
🔸
سازمان ملل ارزش این خسارات را ۱.۳۸ میلیارد دلار برآورد کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/663073" target="_blank">📅 09:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663072">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0406e617a2.mp4?token=QpyYn2K6M0zcRdcJKZ2rmWZdq7Tjk6H1Kan9jcET21d8kqqve_hhIdnKsVmPRrigz42xT5Zg0PAF13UByyhngYaK61T6Y2UZpuMXNlCp4rZ5zz6T4mImugtU7uveZXE39wH5N_DyekxaBxmyo-tMcNGoHlPnh60JAtDoJ_VQzBE3LvyzSnKvKE9NqWID0S9ISlwMJ3_QedRqeHreSwb7lBRri8o-VJNCVp3IZHJ1_cucf_xIcF7EJGwaP1mlMplIq91NZfU4sRE3ndWotPIKiuCLbsgSdviR-PTpx84FPzUYqU68_dZedq9jf9wIMqg8-HQrXYfXIJN9dMqThdBEiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0406e617a2.mp4?token=QpyYn2K6M0zcRdcJKZ2rmWZdq7Tjk6H1Kan9jcET21d8kqqve_hhIdnKsVmPRrigz42xT5Zg0PAF13UByyhngYaK61T6Y2UZpuMXNlCp4rZ5zz6T4mImugtU7uveZXE39wH5N_DyekxaBxmyo-tMcNGoHlPnh60JAtDoJ_VQzBE3LvyzSnKvKE9NqWID0S9ISlwMJ3_QedRqeHreSwb7lBRri8o-VJNCVp3IZHJ1_cucf_xIcF7EJGwaP1mlMplIq91NZfU4sRE3ndWotPIKiuCLbsgSdviR-PTpx84FPzUYqU68_dZedq9jf9wIMqg8-HQrXYfXIJN9dMqThdBEiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
روایت تحلیلگر سرشناس عراقی از سیاسیون عراق در زمان جنگ رمضان
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
پس از ترور رهبری خیلی از دوستان قدیمی ایران علنا اعلام کردن جنگ ایران ربطی به ما ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/663072" target="_blank">📅 09:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663071">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBL6Z08A_fOhC_vIPcdDyq3-Ma2hDvvEB6Gkcn1YR8xU1mu6t6BX5j8Mt04JyNg6Cb0THQQf5SXd9G6c2qhPf5Us5uIftxIix61PclKrz9Ppn0oGdCE85gFxhAGFcRE4lwLZF0w7oEOC-AK9bqUuavMXGKLF5-Ao-iPAZd5Q4YuXyc_zHoly5tBz0y7rG5xPyX4_EaBM1Ka_OBu7VeScspY34sJjd98-Xr3Dqg3zJdwexG5K9E4YAX1DZNg7SWGvTIWTWnAJS50Jon3KPfj45chR4T4O0ig5Xo-UY3BBgDTOcR5Sndw0A1_yNTR3xXRw1HoMNInm8tIrBvuPIaEsWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تلگراف: ترامپ ممکن است پس از انتخابات، خواستار توافق جدیدی با ایران شود
🔹
این موضوع به‌دلیل نارضایتی برخی جمهوری‌خواهان و مقامات اسرائیلی از تفاهم اخیر مطرح شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/663071" target="_blank">📅 09:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663070">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLEwwQTlNmUOLdMWXZG9MMipe0A-2A0F5gDpzC30jsAVmNyCQVzIaie3VPC-m0h0WS0Lja061S4nHc3-ZXPlBpR0ztEMb1HG8ACR2uvOhNRDk_ciUS5sop1YaNZ6efdS5Pew3Ro7C3AEG2-17oTQtZRSjncYykMiZMsMiiPz8FU-0vjrnEmwjXzWtqvm2jX7H1clIDHVQhrxFs8ZXOk7Xc-tArwTBhw8LmNrBw061hmL4U_TNoisPp4rubw0FcAu900btYfgs2ZkfNvPhOvfBPEX6l5vSQ736iKhBCgWhgp2gKdu1fGxcFl21s1rVGjU2nqO6EIDRErOnfxRWzxlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سازمان اسیران فلسطینی: وضعیت وخیم «مجاهد بنی مفلح» پس از آزادی، نشانه‌ای از شرایط سخت زندانیان فلسطینی در زندان‌های اسرائیل است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/663070" target="_blank">📅 09:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663069">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSBd7la1BodrdAunh8HMK-AMqDRpcJOjly0nbD1eQnx9jCrDR23DlqaplUK9KsmNOq3gvGaIFziKHKYyT5E_WilzfRy8FTAnwQWYSrlBcXwR3IjYSXF1_sSL68lqjtb57qc03ODqzvWqfIJxumSxsg0XtQSWCsoBrZMsUajkFXST5Z-iO_BHqXj78I14Gr173zuKs-pstG2kCFviBURRe824tGg_KQNQ1ubQ7dKbw9irpZ7T3oC8y9dOa_2PCfgOj76VJMbW0C9_kIGbZGpC7KI_J58zVc-8jkir8A0ZY1yOEtX543BiorGgE0mdwwBWtG5D3-kBJGFAjshWRll62w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور: نه ظلم کنیم، نه ظلم بپذیریم و نه مقابلش سکوت کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/663069" target="_blank">📅 09:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663068">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔹
آمریکا مدعی به هلاکت رساندن سرکرده داعش در سوریه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/663068" target="_blank">📅 09:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663067">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a56418e92.mp4?token=SdsDY9VRdVbVUWIkCjTTdtV-W23A2SQXWQHe-iyr-Ojrx4TTW9VdIa9pJYCmy7VR8jxsSIgYBlbeTO_p8pYWdfqjyO5IPvlbsMiMKdbVRDTCO6wccQZZnrpVo811pOeb_r5BYjZkyhwTEeg73o4EyUWTG223uNes3GOr0UOgyi7SxCZCgF1X_xwLjZtdGoytfybKQtoUE6sJEi8NjjAoStj-s0LEP7EaB36PgtYd8TdnAtC3M9ZhQcWcECQTIx-eGQt4kkBpOxfiY8AnMIjWaINN1pkuPuJoKuVkoP3hhJMj_TWccOKAcd4q2CcgDyG8jDCJrhOiEiLXk1N-_n9-hg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a56418e92.mp4?token=SdsDY9VRdVbVUWIkCjTTdtV-W23A2SQXWQHe-iyr-Ojrx4TTW9VdIa9pJYCmy7VR8jxsSIgYBlbeTO_p8pYWdfqjyO5IPvlbsMiMKdbVRDTCO6wccQZZnrpVo811pOeb_r5BYjZkyhwTEeg73o4EyUWTG223uNes3GOr0UOgyi7SxCZCgF1X_xwLjZtdGoytfybKQtoUE6sJEi8NjjAoStj-s0LEP7EaB36PgtYd8TdnAtC3M9ZhQcWcECQTIx-eGQt4kkBpOxfiY8AnMIjWaINN1pkuPuJoKuVkoP3hhJMj_TWccOKAcd4q2CcgDyG8jDCJrhOiEiLXk1N-_n9-hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مسی در گذر زمان؛ از کودکی تا ۳۹ سالگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/663067" target="_blank">📅 09:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663066">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ced688a1e.mp4?token=iZdHzPRYQeaRehDPn42o13gSLWjtIaMJJr5woPoWa9yL4ez-iRIZm2dFwGJNw3nYOx0NIthQtC7SCBFkl_AqhYrv9bSfeu00sJxO_feXtFynulU8cjAOIDz0-37nJpomcev8x1STizb2cEypTbGUEBwTK6FwH-MWIfwM0jEMu7atbi-RnwduWhhUkEJcCkrsDbcXNdGk01hj4gzksvvP2NjOJ3ii1PSce_suYPMavx-G-Tud0Qvb7NVnAoAqVqaWmwAf0K5E81ldrqGzD2KeUXJ59L3rrnF6V2uwf5DMGp-rpa375kacqu4ZHDGxijC1d8NKTXUGF6hZZnBpcuBnGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ced688a1e.mp4?token=iZdHzPRYQeaRehDPn42o13gSLWjtIaMJJr5woPoWa9yL4ez-iRIZm2dFwGJNw3nYOx0NIthQtC7SCBFkl_AqhYrv9bSfeu00sJxO_feXtFynulU8cjAOIDz0-37nJpomcev8x1STizb2cEypTbGUEBwTK6FwH-MWIfwM0jEMu7atbi-RnwduWhhUkEJcCkrsDbcXNdGk01hj4gzksvvP2NjOJ3ii1PSce_suYPMavx-G-Tud0Qvb7NVnAoAqVqaWmwAf0K5E81ldrqGzD2KeUXJ59L3rrnF6V2uwf5DMGp-rpa375kacqu4ZHDGxijC1d8NKTXUGF6hZZnBpcuBnGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
نخست‌وزیر پیشین اسرائیل: سران عرب اصلا دغدغه فلسطین را ندارند، بلکه تنها نگران افکار عمومی کشورهای خود هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/663066" target="_blank">📅 09:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663065">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔹
تاج رئیس فدراسیون: پس از اعتراض ایران به فیفا، برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شده و نمادهای مربوط وارد ورزشگاه نخواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/663065" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663063">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uk9GJuTvdgzYHGQV6V4z0EzxGSOdw7lUcpjALnSf6DacrxWcfaarXY2Z8BqoFC82NWQ3PRrmpY_E8jqJzZ06vOUOc0qVKPyT9-YhzNBc8cUx1Ny8KKy6bOyqib0mLpii7dOOIOgF5MsU2nxgBpqNboS2-kOW6hyBNjmvUkc479xWsDhO2LCrWuhxcQiRveZxsaiVHukFw7w6VCa7S9uqKU2_U6aoPz6hVO6fjPBtEui9X7sxcD4xnXVU2uOF3XO77hAWkJtb5YHj8ZiEvQK_YQd8wFilNI3dELCkX2Skspt-DSPYhHwIFHYjpPHroBi2u9B4L5YYeKk4jLzE4yo6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uW6HwMr3Raf_SAZlBBBrr9HjZUzmBI3mIrKuta-1NxnpL9Agz7ZbtkKY0QlyCP9B7RLYUyQs9v6CTXCynfnBbFcsaraDzR-WBlVqwhysBq4qp4atAvR0Kl9hcs_DU81BbLe5CADgeHmnGx00KVBw38rjhdlwViUoNOsWdiRPCJfxoGF2XiDeaS0rohZulm5Crqmrg8Gig84c4iszboCJtLcbOwhD-lX8CnmLcJjvKPBvCF_aOxHaGQCvtPlDSLQmIDaCO7h2q90js_FPzmk9Z5x1GPg-pxbg4Ux2sf_62baXL7EJ9uM8K1x2KjTVltuojlRY2Hu8KLxqCIDM0uIpVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
مادر شهید مسیحی لبنانی در جمع مادران شیعه؛ تصویری از همبستگی علیه اسرائیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/663063" target="_blank">📅 08:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663062">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c12e43cce.mp4?token=Nab_BxhuCGm6qWmSl6P3mJgCCnNdQHY1qD6xUU0tAVeBkGHYsT-W5EdudiyQmiypBCeTXWEiFd0KF8WrFojiT0GCQn5lzg1FGdx8xtL-Acwph-esM24LpLmk11SdGRtT2lWA-h1H-bFUXSsL75WI4oLTOXMd_PyFY85bAvqYyzYm0zN4AQiywYq1sGvo_CQZYmnDYL-7CBGmq363OZIbmi8qNo2D8KdLrlchwYzh28Y-SuK09h_UHTvoY9qpU6QWYcbKvQ81VWOOLsFkUmEce5U2xV2TI2Nd5hDd5AJnu-B1rRITB7Xdu0_cNuazi_sHma_PMg1wh40e1q2ZBI8wJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c12e43cce.mp4?token=Nab_BxhuCGm6qWmSl6P3mJgCCnNdQHY1qD6xUU0tAVeBkGHYsT-W5EdudiyQmiypBCeTXWEiFd0KF8WrFojiT0GCQn5lzg1FGdx8xtL-Acwph-esM24LpLmk11SdGRtT2lWA-h1H-bFUXSsL75WI4oLTOXMd_PyFY85bAvqYyzYm0zN4AQiywYq1sGvo_CQZYmnDYL-7CBGmq363OZIbmi8qNo2D8KdLrlchwYzh28Y-SuK09h_UHTvoY9qpU6QWYcbKvQ81VWOOLsFkUmEce5U2xV2TI2Nd5hDd5AJnu-B1rRITB7Xdu0_cNuazi_sHma_PMg1wh40e1q2ZBI8wJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مدل دویدن ارلینگ هالند بازیکن تیم ملی نروژ، سوژه رسانه‌ها شده
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/663062" target="_blank">📅 08:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663061">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
ادعای ترامپ: خاورمیانه در پی توافق «تاریخی» با ایران برای نخستین‌بار شاهد صلح خواهد بود
🔹
ترامپ مدعی شد خاورمیانه پس از توافق «تاریخی» با ایران وارد دوره صلح می‌شود و برای نخستین‌بار در ۳۰۰۰ سال گذشته آرامش برقرار خواهد شد.
🔹
توافقی برای پایان درگیری با ایران امضا شده و تنگه هرمز بازگشایی شده است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/663061" target="_blank">📅 08:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663060">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA03eS5S5FVuC0TPXoDEttGpGF7llvgo8IM0L937MDmNVYQ9AqWUI9uO-FOUnOuDqEUORzYnnN443iVnXhMgOvJaI--aF-Gb4ufeTaTkNcspBEwNf_f1wJ1-qE1PfbLJp6yTRrcsCC3-CsdQ1Kj6o2KJ-Oy4Hfn5ZIuXWdhG4OeGErT3VoRSPjdBYjrtqe1LQRdxgQJo5h13hKlO8pHgu_1DuFtqrzW9xHS4upyAqHbp1PuaX-zxvThsWMI1_NavpVogCzeEDC2JZOwrUYI5fJ2_iRcpmlEg-L9tOWHZlzgWK1enObRSkF7mbtENUvz8WgPdECAduilf0Z9k82sjoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تیم ملی ایران به سیاتل آمریکا محل بازی آخر مرحله گروهی با تیم ملی مصر رسید
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/663060" target="_blank">📅 08:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663059">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9de8b526.mp4?token=mSyNTobjKVD4Q8UnT2yGMYf8XDw3QLADZ5HmXS1pNns8EvBKFb0dXAhIu8e-YHSyCRRG_enF62s-mmtGgVt5_xtlAXsL1EfFM7DOerTbHflDCku6LiPzzsLl1Z_203suyiLtgEHZlQiDO7kYZSjzvk_0HTh7jsbPHm1oeJTwWDWFGQzAsEHxzpKaQI_QR202w4ruvcOCSvxPOQex9UMRpO23R2nZSYXkqHbvVRBcbJW8T_eJg6oltqOe7FxydfwVfANEKI4_A4aTj4PLCKXBbOfToA1UbgVbL4w-bcDdfFu4qN8vQTrG2OKHqIEULvusNl2cmyFA0BHric95mPeB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9de8b526.mp4?token=mSyNTobjKVD4Q8UnT2yGMYf8XDw3QLADZ5HmXS1pNns8EvBKFb0dXAhIu8e-YHSyCRRG_enF62s-mmtGgVt5_xtlAXsL1EfFM7DOerTbHflDCku6LiPzzsLl1Z_203suyiLtgEHZlQiDO7kYZSjzvk_0HTh7jsbPHm1oeJTwWDWFGQzAsEHxzpKaQI_QR202w4ruvcOCSvxPOQex9UMRpO23R2nZSYXkqHbvVRBcbJW8T_eJg6oltqOe7FxydfwVfANEKI4_A4aTj4PLCKXBbOfToA1UbgVbL4w-bcDdfFu4qN8vQTrG2OKHqIEULvusNl2cmyFA0BHric95mPeB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم برزیل به اسکاتلند توسط کونیا در دقیقه ۶۰
⬛️
🇧🇷
3️⃣
🏆
0️⃣
🏴󠁧󠁢󠁳󠁣󠁴󠁿
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/663059" target="_blank">📅 08:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663057">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twmRdOaTux4MUiDSf7Th8cAWk-w78PsqUgluMl5rjJ9O7vV0kcrkqpAljn7FwbZWgGqClQ7vOI1KrMkAjDV6Xhbe17AmErwl23LCDI_mWJQCNki2TmYm5yrt6nbIsUyNfYpHvqNFezyovzWk_2NSk8NAhWcTg6xSVXdZYcWHX3rIHUCG1BJYgFa9p7jO-TQHTdwTHjfEKpp_C3cZhXQG_a1rm01nr_TuPx2RFVsVs5cNON4kz75YpR3HT6B8iJPGU7fTDAE1t_Qtj9s6D3o9We3_EutERkepPwrQ255TUXpzM4mN5ssXZ-2xC7ZgKCaS-GPWt9wuccwguOnowvt3Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پوستر فدراسیون والیبال ایران برای بازی امروز مقابل آمریکا
🔹
هفته دوم رقابت‌های لیگ ملت‌های والیبال ۲۰۲۶
تیم ملی ایران امروز از ساعت ۱۸:۳۰ به مصاف آمریکا می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/663057" target="_blank">📅 08:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663056">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN2uoIkM9rfLL3d4DGqUskr9TZcpHwus_9MEFq_dR6m9t874NisMPv6T2FkzmHzRaf4-S46rW6uvCckh2nKdPDqjbU7KXPjAKJmlv9GKar_GPPM--X_Exf_tbi50makhdm0-Vo5MWchU0p0g6DkZGQ2MyIfKt8Yznusgpzfe6_34oXlygTYecmh2RYuyDkQiq_OxeGmXzCoH1WCLZeuGtAzm3syhCxFqAcYTT02TwIHu5HO5v0Ger51cFDR9syHQiQ-EfqRTp_tWKpPrZ8DM5OvExqy-KDNvRCI2L-Rd_Zv5SanbrmAeuZ7fO49oxZ_Uwr-Ew5HDY6Cwu_ZisBbGxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت آمریکا وارد کانال ۶۰ دلار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/663056" target="_blank">📅 08:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663055">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BgVK8hLATu0sMBwbbAy8oiesb_hu--bW86lgRAqtQMdE8OlfAE-esvLNFBC3UbJQFMl-9Krq8XGReF33yIuRdNbxEZB4E9TFNlCBhcEFTbB-2zris8l5ZmToWJBtIfW18O97k6f-qXOrs3ulryvYsAAvHkXtZvZZ2ZPdmAbGmrvuFNHe16it3ojy6cDAzz5BEt-zXCyTHSvrFuwaYYnMhcPwgkcTWG83sQtCfXE8ZVtOy3KrB4N_IdBPABMGbSjtP3hd8caJeN-BEJhxxdPxyoYdO7vktrHHhDPXk3bBXgalncA48Lzf5sQyk2vFQ0dPJuDaW8hi3Hj52b-MmHx9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عقب‌نشینی سنای آمریکا از بررسی قطعنامه اختیارات جنگی ترامپ علیه ایران
🔹
یک روز پس از تصویب قطعنامه محدودکننده اختیارات جنگی ترامپ علیه ایران، سنای آمریکا موضع خود را تغییر داد و طرح مشابه را رد کرد. ترامپ با استقبال از این رأی، آن را هشدار به ایران خواند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/663055" target="_blank">📅 08:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663054">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46cc6747c4.mp4?token=cUGGx5RUEL-Xq2piFj-5NpCFUdcA6I6WYT4u8cOcXIumHdq9SrCgesbNXM6WnA1RsmZh8oxX4qpzR20juH8Q64eHYjQTiHkhwq5G08O5gmqUGiHbJFJigwkzCNs55sklepg-l8PCav_-6D8Rc68nwsgdpoCOux1yEOrmW4ey0iGD-lFRdJugeBttG8VGaxiewD7t3q4sBPnD5Z-QCzG2vJxXj0kFJhcRci7XQ5lqLPqIf7jAvVdOnnga4ppAoJ_WKDx8RX3ZXdCTivwAqd1eekFoZ8rA_SPEuJD7q6kjo7EUJUf8C_KH-QF6Y1NDbmhNoOclVSV6q0tmaUEFRfn0AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46cc6747c4.mp4?token=cUGGx5RUEL-Xq2piFj-5NpCFUdcA6I6WYT4u8cOcXIumHdq9SrCgesbNXM6WnA1RsmZh8oxX4qpzR20juH8Q64eHYjQTiHkhwq5G08O5gmqUGiHbJFJigwkzCNs55sklepg-l8PCav_-6D8Rc68nwsgdpoCOux1yEOrmW4ey0iGD-lFRdJugeBttG8VGaxiewD7t3q4sBPnD5Z-QCzG2vJxXj0kFJhcRci7XQ5lqLPqIf7jAvVdOnnga4ppAoJ_WKDx8RX3ZXdCTivwAqd1eekFoZ8rA_SPEuJD7q6kjo7EUJUf8C_KH-QF6Y1NDbmhNoOclVSV6q0tmaUEFRfn0AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم برزیل به اسکاتلند توسط وینیسیوس در دقیقه ۴۵+۳
⬛️
🇧🇷
2️⃣
🏆
0️⃣
🏴󠁧󠁢󠁳󠁣󠁴󠁿
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/663054" target="_blank">📅 08:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663053">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
هر نوزاد ماهیانه چند قوطی شیرخشک سهمیه دارد؟
🔹
کودکان صفر تا ۶ ماه
🔹
۱۰ قوطی یارانه‌ای و ۴ قوطی غیریارانه‌ای
🔹
کودکان ۶ ماه تا یک‌سال
🔹
۸ قوطی یارانه‌ای و ۴ قوطی غیریارانه‌ای
🔹
کودکان یک‌سال تا  دوسال
🔹
۴ قوطی یارانه‌ای و ۴ قوطی غیریارانه‌ای
🔹
همچنین به‌منظور مدیریت توزیع، در هر مراجعه حداکثر ۲ قوطی شیرخشک به متقاضیان تحویل داده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/663053" target="_blank">📅 08:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663052">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1424dc9603.mp4?token=mCEs7QcpANHXeQzqGNr0_GegRKTx03DMPEWtfly6Eq9y_N3p11GaDid8ya2Ml1HibWO0Nmr7CVcg6IkfXqb59z3nyJ6XVj1gzqdAqZrPUH7fhEIAXpU2B-KgOq81W2UsPdaImH3Obc2R3E4f_lhWl8PooNu-s5M_nndestpz24iSNb6RHA2-TmP2HiaJ20RJchaLM3iWgmcIk9I07FW6h8ZLcGFxp4dgJP9dnLqYyllgScAGWYXppKnPr8KlM0JDlTyhOHbVXZuUSZaVDXWxqIf5Lpuc6uw4rAQ6uQmh5UwJ82kI54JH7SE17cwNx_OJ5FRibAyLhu1UyPvCBXC9-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1424dc9603.mp4?token=mCEs7QcpANHXeQzqGNr0_GegRKTx03DMPEWtfly6Eq9y_N3p11GaDid8ya2Ml1HibWO0Nmr7CVcg6IkfXqb59z3nyJ6XVj1gzqdAqZrPUH7fhEIAXpU2B-KgOq81W2UsPdaImH3Obc2R3E4f_lhWl8PooNu-s5M_nndestpz24iSNb6RHA2-TmP2HiaJ20RJchaLM3iWgmcIk9I07FW6h8ZLcGFxp4dgJP9dnLqYyllgScAGWYXppKnPr8KlM0JDlTyhOHbVXZuUSZaVDXWxqIf5Lpuc6uw4rAQ6uQmh5UwJ82kI54JH7SE17cwNx_OJ5FRibAyLhu1UyPvCBXC9-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گزافه‌گویی دبیرکل ناتو علیه ایران جلوی ترامپ
مارک روته:
🔹
کاری که ترامپ درمورد ایران انجام داد بسیار مهم است زیرا این کشور تروریسم و هرج‌ومرج را صادر می‌کرد و نزدیک به دستیابی به توانایی‌های هسته‌ای بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/663052" target="_blank">📅 08:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663051">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb06272b06.mp4?token=Lj_0e2vukh5G9QyFKRUmztxC2TBFhGDRANALQJdaiiCsI8lBNAOMoVVvRcPiQO3LGuM6k3Z80CCDCj-ctkWrocDDvLNPO9_V1VmpeLY-A0n3ASjpPiyJxe49Nvr9Cj_-NlFNk3V_Wk1g13S2hZsumfkGGW3CxdEEQKrhpqJK__tuwyWGrd8Bn9y1N1isaAgfN5OuTt7qjWoYOwMX5BbGKGi2DQisJrn-dlbsjGePo8x_dHykAGAHbl_LDGQzbx7jZUIVdaURiBYqMOw9o27V3L5W9q0JCMCMpbtE3tPxJSKFQNVqRXs5_2rBw5vLcaOvwGYpJYCnC5PvU6bkp7IE5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb06272b06.mp4?token=Lj_0e2vukh5G9QyFKRUmztxC2TBFhGDRANALQJdaiiCsI8lBNAOMoVVvRcPiQO3LGuM6k3Z80CCDCj-ctkWrocDDvLNPO9_V1VmpeLY-A0n3ASjpPiyJxe49Nvr9Cj_-NlFNk3V_Wk1g13S2hZsumfkGGW3CxdEEQKrhpqJK__tuwyWGrd8Bn9y1N1isaAgfN5OuTt7qjWoYOwMX5BbGKGi2DQisJrn-dlbsjGePo8x_dHykAGAHbl_LDGQzbx7jZUIVdaURiBYqMOw9o27V3L5W9q0JCMCMpbtE3tPxJSKFQNVqRXs5_2rBw5vLcaOvwGYpJYCnC5PvU6bkp7IE5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول برزیل به اسکاتلند توسط وینیسیوس در دقیقه ۷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/663051" target="_blank">📅 08:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663048">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5e817df0.mp4?token=tOovLb3FLQfnNI7TH0u42bXxUvU6uvMVjEKlZ38d3ETvWu7xlulmxwElkRnCvmBoSgfeQIeUVqJhcs0NvHfm7QiwFehYzVMcQ0KsYAP8IZxm85YG867HBHZ7Deg6TZpBbcUMKNG-XbsEph-GJUHDHBvAhjoyQd1b1I9pO8ZdD6-Nl2YYLYosmfSwOOjFXk5_-xSQR1YWo06Ky6HoEnfwvPnaDvw_nFNGD36qxM_DGgCzhtGx90iHmYSmVud94euRksaX6owGE7sx7pmlGcGQr0xoiwuRPg45nyqAKrI2_NdWP0mY-zNcoTTTpmhGWEw-8RTkDH0QLyv0exE69G10og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5e817df0.mp4?token=tOovLb3FLQfnNI7TH0u42bXxUvU6uvMVjEKlZ38d3ETvWu7xlulmxwElkRnCvmBoSgfeQIeUVqJhcs0NvHfm7QiwFehYzVMcQ0KsYAP8IZxm85YG867HBHZ7Deg6TZpBbcUMKNG-XbsEph-GJUHDHBvAhjoyQd1b1I9pO8ZdD6-Nl2YYLYosmfSwOOjFXk5_-xSQR1YWo06Ky6HoEnfwvPnaDvw_nFNGD36qxM_DGgCzhtGx90iHmYSmVud94euRksaX6owGE7sx7pmlGcGQr0xoiwuRPg45nyqAKrI2_NdWP0mY-zNcoTTTpmhGWEw-8RTkDH0QLyv0exE69G10og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وضعیت کاراکاس، پایتخت ونزوئلا در پی زلزله ۷.۱ ریشتری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/663048" target="_blank">📅 08:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663047">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔹
وزیر مهاجرت دانمارک: پخش اذان در مساجد به این کشور تعلق ندارد و نسبت به «غالب شدن اسلام در زندگی عمومی» ابراز نگرانی کرده است
🔹
در برخی مناطق هم به بهانه آلودگی صوتی، پخش اذان از بلندگوها محدود یا ممنوع شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/663047" target="_blank">📅 08:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663046">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔹
بقایی: ناتو باید برای همدستی در ارتکاب جنایت علیه ایران پاسخگو باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/663046" target="_blank">📅 08:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663045">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e661d3c68.mp4?token=VdqS3DReEFtBcmPk7o7VvtQIBXNpEcFPwugtzE796NcrZtom4hESSPzn0TeDOMWnFIG3q2r1ciofHhxJh1zDD6xWMgCyi21O3G58LqJEXN5LEwNIg9mhXLA4baEzB_JFeTks3yX10z7tN0lmVEF_PctBuULe5UADAUTH9lTzLlXmp3J_gMUw3y1uXH8FMLvCRa1sGFEbHN5PNHi_IY1QrS8ZO2M2PT0kBsa-K-bAAKL5TUa42r8KiQ-Lga6VrxRVLDPD5o47PF4cv7nrlbZwHGfXlsF_0Mvi0TnY6vgxn9QpMVmgCACXzJ01oKk7CA3aTG50FbTqfOH0xvbivKeP_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e661d3c68.mp4?token=VdqS3DReEFtBcmPk7o7VvtQIBXNpEcFPwugtzE796NcrZtom4hESSPzn0TeDOMWnFIG3q2r1ciofHhxJh1zDD6xWMgCyi21O3G58LqJEXN5LEwNIg9mhXLA4baEzB_JFeTks3yX10z7tN0lmVEF_PctBuULe5UADAUTH9lTzLlXmp3J_gMUw3y1uXH8FMLvCRa1sGFEbHN5PNHi_IY1QrS8ZO2M2PT0kBsa-K-bAAKL5TUa42r8KiQ-Lga6VrxRVLDPD5o47PF4cv7nrlbZwHGfXlsF_0Mvi0TnY6vgxn9QpMVmgCACXzJ01oKk7CA3aTG50FbTqfOH0xvbivKeP_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ادعای وقیحانۀ وزیر خزانه‌داری آمریکا دربارۀ معافیت تحریمی ایران
اسکات بسنت:
🔹
معافیت تحریم‌های نفتی ایران مانند دادن هویج (امتیاز) به آن‌ها است که هر لحظه می‌توان آن را پس گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/663045" target="_blank">📅 08:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663044">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔹
نیرودریایی سپاه: عبور ایمن از تنگۀ هرمز تنها از مسیرهای اعلامی جمهوری اسلامی ایران ممکن است
🔹
هرگونه مسیر جدید برای تردد در تنگۀ هرمز بدون هماهنگی با ایران، غیرقابل قبول و خطرناک است. تنها مسیرهای اعلامی جمهوری اسلامی ایران مجاز بوده و تردد خارج از آنها ممنوع است.
🔹
هماهنگی با سپاه از طریق کانال ۱۶ الزامی است و با شناورهای متخلف برخورد میشود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/663044" target="_blank">📅 08:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663043">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owELOHpOTemcXBrkjXNQm3rWY5w7IO5llnO6lsD0nW_aL7plycr7CE7nx1QLKmaxsBGTciVZfnFyk7lbX3xdT5sxV5pijw4oBn3b4dKebpiOCBH1OCukAOqayIqt4PYJ0-2i4ywf32IaZGt7wmbkVtgzdFPU81Vkr31eQpJhFz4ZCSAWj6i_X0qU_uGsCwmVz3zMiV90t13AYWdpFKbPyJBVcn7WzuowVeRfmnDrlYz-gdJ4rCEJaMIf7su0k_k-r3qpPeraUHeW5httLWY1dOh3vaLCo3yLfQ_jZyKcO3HpvOEaKDpcmPFZ4FzYvxDiMm1YbPntZOJhj3ECdOxoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۴ تیر ماه
۱۰ محرم ۱۴۴۸
۲۵ ژوئن ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/663043" target="_blank">📅 08:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663042">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔹
پایان ست چهارم والیبال ایران و فرانسه لیگ ملت ها
🔹
فرانسه ۲ - ۲ ایران
🇫🇷
۲۵ | ۲۳ | ۲۵ | ۲۴
🇮🇷
۲۱ | ۲۵ | ۲۱ | ۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/akhbarefori/663042" target="_blank">📅 00:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663041">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797a3a0159.mp4?token=fT0K0iFhoJcQv9NqPBIFRJ8Tbgjvo_9FQDORo7zBtqbG-Fd6TfznIU8s2zxtzwyYAtqM5jLnTOXRBW6rEi_75hIgk5X32bT86Oz4iRaM61wLBjwTMNkEsvl806yhnR6pNU8Cj60xwrc8B-vwXj68LzaGUEHMXGk-ul0sI1apb8D_iXyq8vJ5wECd9MzIFxm65Se3U94y-5g7kwApNGHZC7JiEhgR_wu957qhErPSxSYguQMA3ByirjtVsbnyahpLsMuZp0w2GCjx_yniVWvI0OuILQl1W0rHmPcnOh-_xSLn-179xKoo73tmn8lnypqqG9y2rv78QFqVIwFIfsNvKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797a3a0159.mp4?token=fT0K0iFhoJcQv9NqPBIFRJ8Tbgjvo_9FQDORo7zBtqbG-Fd6TfznIU8s2zxtzwyYAtqM5jLnTOXRBW6rEi_75hIgk5X32bT86Oz4iRaM61wLBjwTMNkEsvl806yhnR6pNU8Cj60xwrc8B-vwXj68LzaGUEHMXGk-ul0sI1apb8D_iXyq8vJ5wECd9MzIFxm65Se3U94y-5g7kwApNGHZC7JiEhgR_wu957qhErPSxSYguQMA3ByirjtVsbnyahpLsMuZp0w2GCjx_yniVWvI0OuILQl1W0rHmPcnOh-_xSLn-179xKoo73tmn8lnypqqG9y2rv78QFqVIwFIfsNvKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
چاک شومر اساسا فلسطینی شده است
🔹
شومر (رهبر دموکرات‌های سنا ) راهش را گم کرده است. او اساساً فلسطینی شده است. من درخواست کرده‌ام که یک لباس ابریشمی زیبا با لباس سنتی فلسطینی برایم ارسال شود. چاک شومر یهودی است. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/akhbarefori/663041" target="_blank">📅 00:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663040">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
لیگ ملت‌های والیبال، پایان ست سوم
🔹
فرانسه ۲ - ۱ ایران
🇫🇷
۲۵ | ۲۳ | ۲۵
🇮🇷
۲۱ | ۲۵ | ۲۱
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/akhbarefori/663040" target="_blank">📅 00:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663039">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8683ecaf49.mp4?token=p2rWkThUE_lyZpWE9jwoleLIrS05PJ1KK77p0OloUgcRqOc4mQG6zdKD_-wQShWZH8FfzGdkCkzNBPWwRxvx-mLmNa6b7DVlpzPsb1gXRjRn26iFI_37n9CqVODDOYJysYAk_rGBCH_hN4AcXbGBCw0RKllx-0zyTPrCzm-ftHOeb7yvjTLyTw--laJbj13MwzVnE74LzBEjdzPxSawEplJAvBtfBt_cAYsLUkWwcoBRiXq940rzbCdO9zPUmBtInyjYsely5evhJy6aaptjZTmYb1LqBv9UPWPgeZ85fZML06BPLk_FD5HwFGGFpFlhDp0L-2hrOd2mXIk1mknPlT7OxMA-qKeGiOnzZ7dMIby2XvplwipHMEND4R8qXPAdeVmdSSRoWYHPZEGDA3NiCRLyqMH-qfSGSX8kc_G2c_I954cf1cuEoCZ5TgtOX3TWe6r7uSM5Vdn0NNAT2MET95xDEJ0JJziaelFoEaDt0a7KC2uJo0L8N4T27cva3EIgOJYsDDrd17x7uPZ1jKgUImy9D8swExN8JKFu5C8xyGYXf1d_-84OEpxudjJC-UirmzWXfyhrkAM4ucLJXeyWGUIcn_qGmcuOpU1GzgVcQSN09uz9sv17nbf1gYUkT2H47pBtPPLjGyAmQClPyhkUES9F2HVpcrmkgG-rqTlpsKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8683ecaf49.mp4?token=p2rWkThUE_lyZpWE9jwoleLIrS05PJ1KK77p0OloUgcRqOc4mQG6zdKD_-wQShWZH8FfzGdkCkzNBPWwRxvx-mLmNa6b7DVlpzPsb1gXRjRn26iFI_37n9CqVODDOYJysYAk_rGBCH_hN4AcXbGBCw0RKllx-0zyTPrCzm-ftHOeb7yvjTLyTw--laJbj13MwzVnE74LzBEjdzPxSawEplJAvBtfBt_cAYsLUkWwcoBRiXq940rzbCdO9zPUmBtInyjYsely5evhJy6aaptjZTmYb1LqBv9UPWPgeZ85fZML06BPLk_FD5HwFGGFpFlhDp0L-2hrOd2mXIk1mknPlT7OxMA-qKeGiOnzZ7dMIby2XvplwipHMEND4R8qXPAdeVmdSSRoWYHPZEGDA3NiCRLyqMH-qfSGSX8kc_G2c_I954cf1cuEoCZ5TgtOX3TWe6r7uSM5Vdn0NNAT2MET95xDEJ0JJziaelFoEaDt0a7KC2uJo0L8N4T27cva3EIgOJYsDDrd17x7uPZ1jKgUImy9D8swExN8JKFu5C8xyGYXf1d_-84OEpxudjJC-UirmzWXfyhrkAM4ucLJXeyWGUIcn_qGmcuOpU1GzgVcQSN09uz9sv17nbf1gYUkT2H47pBtPPLjGyAmQClPyhkUES9F2HVpcrmkgG-rqTlpsKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اردوغان و شی و پوتین به درخواست من در جنگ ایران دخالت نکردند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/akhbarefori/663039" target="_blank">📅 00:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663038">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6384093be9.mp4?token=Snn-RPYsXHzlFEZpEqAddr_Gk3MAwSfbBUvKR4jCQXI32DK97yESXrXRr8Da0o9_0GtHf64GqZEnS9_vFoN9Hje2hAT3Rt8kSZRHOJoEsAP5rsmv82kxL4amU5NB-2tZysjhKAIBn_RR2T8YUaawdg2baHp1eOm9w6bA3k5HQAaFPGYWWd5JAmqJUzu_u_WxdBVWtjjuFSCN_bqBWJJDSp_Dw9aMg8QH5zFf_UP6LRZrF1kgbE9Yu_eJdJHi0WnvUnOT5P56avxoNDmB4AYIw3sUAxRNRZ6I7GxyCTtZOhwcRt_cTM8yjhykrzNAywPIOoVPqbhrpixl-88lhpIBAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6384093be9.mp4?token=Snn-RPYsXHzlFEZpEqAddr_Gk3MAwSfbBUvKR4jCQXI32DK97yESXrXRr8Da0o9_0GtHf64GqZEnS9_vFoN9Hje2hAT3Rt8kSZRHOJoEsAP5rsmv82kxL4amU5NB-2tZysjhKAIBn_RR2T8YUaawdg2baHp1eOm9w6bA3k5HQAaFPGYWWd5JAmqJUzu_u_WxdBVWtjjuFSCN_bqBWJJDSp_Dw9aMg8QH5zFf_UP6LRZrF1kgbE9Yu_eJdJHi0WnvUnOT5P56avxoNDmB4AYIw3sUAxRNRZ6I7GxyCTtZOhwcRt_cTM8yjhykrzNAywPIOoVPqbhrpixl-88lhpIBAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ مدعی شد بمباران مدرسه میناب و کشتار دانش‌آموزان کار ارتش آمریکا نبوده است #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/akhbarefori/663038" target="_blank">📅 00:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663037">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e068d317d5.mp4?token=DlTHyrWc0afRnH6uV2ZGUGVhZh5wXCy6BuI-x5HnOaZxp9igtSjDKnBdox2tp-daoMh8b3M1f2PFMtGiBj4OcKe7tIqhUKGO-fmsW5bgswR7X-dNgwWahmnZO40jXBl7HcWFxMq57vYalPl3ACeNM6gFQ1oTjOG0le5J9UoBpc-fIhTUZ7qx-ohSzAXHpsC_lzZBBgrWHjRqX88GYEPg7hveFGuR3Kb4PBMAQh7RPiojCju-yULeCth4Ky6fJ3FxqwRPmGSSlIhFO_BOl6W_Xxk0SgXLqZAJKqiLgG1zbl3-zb4_Xl3SN8ntMwrYutBFHftn3salfbGhqrJaT-eQVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e068d317d5.mp4?token=DlTHyrWc0afRnH6uV2ZGUGVhZh5wXCy6BuI-x5HnOaZxp9igtSjDKnBdox2tp-daoMh8b3M1f2PFMtGiBj4OcKe7tIqhUKGO-fmsW5bgswR7X-dNgwWahmnZO40jXBl7HcWFxMq57vYalPl3ACeNM6gFQ1oTjOG0le5J9UoBpc-fIhTUZ7qx-ohSzAXHpsC_lzZBBgrWHjRqX88GYEPg7hveFGuR3Kb4PBMAQh7RPiojCju-yULeCth4Ky6fJ3FxqwRPmGSSlIhFO_BOl6W_Xxk0SgXLqZAJKqiLgG1zbl3-zb4_Xl3SN8ntMwrYutBFHftn3salfbGhqrJaT-eQVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ از اروپایی‌ها در قبال موضوع ایران انتقاد می‌کند: من از ایتالیا ناامید بودم
🔹
من از بریتانیا ناامید بودم. ما از آلمان و فرانسه ناامید هستیم. ما از بیشتر آنها ناامید هستیم. اسپانیا یک نمایش وحشتناک است. اسپانیا حتی از دیدگاه شما هم وحشتناک است #Devil…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/akhbarefori/663037" target="_blank">📅 00:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663036">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c1037aa46.mp4?token=EINSHluP_sei-HsVzGyr43dKJ8MgUUQy1oXW4kOAqBy8yUnBalzKgfI0N0K-OmdQeL5BsGkqpF8C8wyhpQFM4QsfLc9mgW7C3HL8hLpHETPjeiXTA6KAU5eLTu37SIN2Ahpny8BcHlLF5vVABICJ82G5gpl6cFRyFPW2-eBlZAQTF6ksQzHMGLXQXAvgH22sehChb4-ea1_H3HW9jnMMoQ1ZbUOLHG0EiRl2xk6zK3hK6ERaKeqrxccPmBXnzwHW-C-C6J8vC_j8RXoeXHwwP80J5jCLfgFZiJUBjyPN9fvkb5YyHWpvWwRIFq0F-Vpu61nn39sv-KYSLtDeahTRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c1037aa46.mp4?token=EINSHluP_sei-HsVzGyr43dKJ8MgUUQy1oXW4kOAqBy8yUnBalzKgfI0N0K-OmdQeL5BsGkqpF8C8wyhpQFM4QsfLc9mgW7C3HL8hLpHETPjeiXTA6KAU5eLTu37SIN2Ahpny8BcHlLF5vVABICJ82G5gpl6cFRyFPW2-eBlZAQTF6ksQzHMGLXQXAvgH22sehChb4-ea1_H3HW9jnMMoQ1ZbUOLHG0EiRl2xk6zK3hK6ERaKeqrxccPmBXnzwHW-C-C6J8vC_j8RXoeXHwwP80J5jCLfgFZiJUBjyPN9fvkb5YyHWpvWwRIFq0F-Vpu61nn39sv-KYSLtDeahTRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توانایی هسته‌ای ایران تهدیدی برای جهان بود  مارک روته، دبیرکل ناتو:
🔹
واقعا می‌خواهم روشن کنم که کاری که شما در مورد ایران انجام می‌دهید چقدر مهم است. این، اول از همه، در مورد توانایی هسته‌ای است که ایران اساسا به آن دست یافته بود و این می‌توانست تهدیدی برای…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/akhbarefori/663036" target="_blank">📅 00:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663035">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d33de4e4d.mp4?token=D8R4O6BZrwv9q_dwrt0ciqH_ejtZH7ZD9lFBCACX4jIBr-5SRWERZLp89KhCBdlSVJR7Q9tIimZrG27E3NZJQzCoLUst3heq9RiHfa6z_Ws2sI5c3R9s5uGvWJV74zgWSywsTjhGxa9RK_vlObrbTIUjbVSc5R_ItwUAZ6OAtdQkrO0lX84wbSMnUhXQVXMMfc3GKzdDt5sNvHxBVMVyYfZLMI381X6d6E7iul-ckYc8IFhPZ51PGHtae07iEu-wv0nPO3UymBHrhpv4jY67KuqrKhEs-oVIPwr9A0045XGytS2D0YbEHpsDpqZc0lqgAIepKMhxvt-KzSOKGAe9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d33de4e4d.mp4?token=D8R4O6BZrwv9q_dwrt0ciqH_ejtZH7ZD9lFBCACX4jIBr-5SRWERZLp89KhCBdlSVJR7Q9tIimZrG27E3NZJQzCoLUst3heq9RiHfa6z_Ws2sI5c3R9s5uGvWJV74zgWSywsTjhGxa9RK_vlObrbTIUjbVSc5R_ItwUAZ6OAtdQkrO0lX84wbSMnUhXQVXMMfc3GKzdDt5sNvHxBVMVyYfZLMI381X6d6E7iul-ckYc8IFhPZ51PGHtae07iEu-wv0nPO3UymBHrhpv4jY67KuqrKhEs-oVIPwr9A0045XGytS2D0YbEHpsDpqZc0lqgAIepKMhxvt-KzSOKGAe9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود  رئیس جمهور آمریکا بامداد پنجشنبه در دیدار با «مارک روته» دبیرکل ناتو:
🔹
«[اردوغان] کاندیدای اصلی برای ورود به جنگ با ایران بود. شاید، از طرف ایران، زیرا طرفدار اسرائیل نیست. من از او (اردوغان) خواستم…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/663035" target="_blank">📅 00:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663034">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔹
ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود
رئیس جمهور آمریکا بامداد پنجشنبه در دیدار با «مارک روته» دبیرکل ناتو:
🔹
«[اردوغان] کاندیدای اصلی برای ورود به جنگ با ایران بود. شاید، از طرف ایران، زیرا طرفدار اسرائیل نیست. من از او (اردوغان) خواستم که [در جنگ ایران] دخالت نکند و او دخالت نکرد».
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/663034" target="_blank">📅 00:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663033">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔹
سفر در زمان به قلب تاریخ... جایی که تشنگیِ یک کودک، او را به خیمه‌های کربلا و قصه‌ عمو عباس رساند
این ۹۰ ثانیه را تا آخر ببینید
A journey through time to the heart of history... where a child's thirst leads him to the tents of Karbala and the story of Uncle Abbas.
Watch these 90 seconds until the end.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/663033" target="_blank">📅 00:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663032">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfqg74t70d1nff4yR5yVfKTklLuu_7ufZFFP7GDK_T5cacRZyXitiC1_mAezRQQO_ajTGIV5DbFTwqq5K9eWtgQ7AKjE0Oq8HN461ESLUs_pZ-18A4ljwazxoGX5bomdMwyRZzDWwpHFCZXEeAqpJRZcvK8P1uEeHmtEo5hOsXYqcDM041bpPgt6QtKGajtdJ7aot7V6CHOQGvyCM_-eWm3yPXb_hQ6TG64WLecTMnnka3U7D4PJZ5ws8lKsAf_65lcItahKWRyNSC4dJgxqi6Ta5zeFSY1n1d3by_C9IFPednyeinzWnBHTXUC-iVYCIfvmvwWfvH-vWdvxGr63rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/663032" target="_blank">📅 00:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663031">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔹
عجیب اما واقعی؛ به دلیل اشتباه تیم ایران در تعویض بازیکنان؛ امتیاز این ست از ۱۸-۱۸ تساوی به ۱۹-۱۶ به نفع فرانسه تغییر کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/663031" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663030">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔹
پایان ست دوم والیبال ایران و فرانسه لیگ ملت ها
🔹
فرانسه ۱ - ۱ ایران
🇫🇷
۲۵ | ۲۳
🇮🇷
۲۱ | ۲۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/663030" target="_blank">📅 23:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663029">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔹
پزشکیان: هر فردی بخواهد به هر بهانه‌ای وحدت را به هم بزند، آب در آسیاب دشمن ریخته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/akhbarefori/663029" target="_blank">📅 23:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663028">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
ایجادخط ارتباط مستقیم میان آمریکا و ایران
👇
khabarfoori.com/fa/tiny/news-3225360
🔹
چرا جی‌دی ونس برای مذاکره با ایران، یک استراحتگاه لوکس سوئیسی را انتخاب کرد؟
👇
khabarfoori.com/fa/tiny/news-3225366
🔹
راز جوراب‌های پاره بازیکنان جام جهانی چیست؟
👇
khabarfoori.com/fa/tiny/news-3225487
🔹
زنی که افشاگر فساد رئیس‌جمهور بود کشته شد
👇
khabarfoori.com/fa/tiny/news-3225365
🔹
وایرال شدن بیل زدن پزشکیان در اسلام آباد
👇
khabarfoori.com/fa/tiny/news-3225358
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/akhbarefori/663028" target="_blank">📅 23:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663027">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRAH-3cN_YoqEpJyv2BlJZ8tKnlVmayqk1ZeMRiJdmdKXN_MDbPRV9MGHA6H_g69zYD1syeqwm2R0K0Tcnn60ZHpwa6LzktefBZMNqwaPDSAj5DFAezpVEUSJlW0sDyPES0h2KPa3FYvDAOgtQsYelOzvsMb1KXnsG3o6BD91roYg89lSnmY7icclMIgARPcG8DNp31u7EfaoM740Bg8EMGcShD6s_B9a_y7vqaco5Lxfa_Igt8gA6MMJZVNL09gn_JeLvKbnMwvxSMXpFR4slbDsyNXmrUE1Pg6eGSE0IvBNQmvKO2aRMJqO32TWOKuSfz0Le3s4WPfdPTrxh0ARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بقائی: اظهارات ضد و نقیض مقامات آمریکایی درباره تفاهم خاتمه جنگ تحمیلی، کمکی به کاهش بدگمانی متراکم ایرانیان نسبت به آمریکا نخواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/663027" target="_blank">📅 23:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663026">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">کاروان کربلا در راه است...
❤️‍🩹
✍🏼
‌نوشتن از تو همیشه سخت است، به وقت دهم محرم از همیشه سخت‌تر... .
با کدام قلم باید از تو نوشت؟! با کدام کلام باید از تو گفت؟! در ساعاتی که کلمات به لکنت افتاده‌اند و جملات سرگردان شده‌اند.
اصلا چگونه از تو بگوییم وقتی که تو خون خدایی و خودش زیارت تو را به ما آموخته است... . آری گفتن و نوشتن از تو فقط کار خداست؛ ما فقط محض تسلی دل داغدارمان چند خطی می‌نویسیم امشب.
🌘
امشبی که هر سال آرزو می‌کنیم به صبح نرسد؛ که صبحِ فردا، معرکه‌ای در پیش داری عزیزِ عزیزتر از جانم... . معرکه‌ای که به قیمت شکستن چندبارهٔ تو، حق و باطل را برای همیشه از هم جدا می‌کند. فردا نه یک‌بار، که بیش از ۷۲ بار به شهادت میرسی پناهِ عالم... .
💔
گودال بهانه است؛ وگرنه کمرت پیش از رفتن به زیر سم اسبان، در کنار علقمه می‌شکند. و استخوان‌های سینه‌ات، با دست و پا زدن های اصغرت خورد می‌شود... . قلب نازنینت، پیش از تیر سه شعبهٔ مسموم، با پا بر زمین کشیدن‌های قاسم پاره می‌شود. پیکر مبارکت، پیش از گودال، کنار هر تکه از علی‌اکبرِ اربا اربا، از هم می‌پاشد. و پیش از آنکه تشنگیِ خودت تو را آزار دهد، فکر عطش کودکان حرم، تو را از پای در می‌آورد. و تصور جسم نحیف و زخمی رقیه، در اسارت این حرامیان بی‌رحم، برای تو هزاران بار از زخم‌های بی‌شمار پیکرت دردناک‌تر است.
😔
و زینب.... زینبی که فکر اسارت و جسارت به ساحت مقدسش، برای هزار بار رفتن جان از بدن کافیست.
🥀
و در نهایت تو، با تنی خسته و قلبی مالامال از درد و غم، به گودی قتلگاه می‌روی و داغی به وسعت همه تاریخ، بر دل زمینیان و آسمانیان می‌گذاری. می‌روی اما تمام نه، بلکه جاودانه می‌شوی. و خونت، آن خون پاک و مطهرت، در رگ‌های زمان جاری می‌شود و جانی به این جهان مرده می‌دهد. آری نبرد عاشورای تو در دهم محرم ۶۱ هجری شروع شد، اما تمام نه... .
🚩
خوب که بنگری عاشورا هنوز به شب نرسید‌ه‌ ست. و ما اگرچه عاشورای سال ۶۱ هجری را درک نکردیم اما در وسطِ میدانِ امتدادِ عاشورای تو ایستاده‌ایم. جایی که فرزندت با قلبی داغدار از ستم و جنایت همه شمرها و یزیدان تاریخ، هر روز ندای هل من ناصر سر می‌دهد که عاشورای تو، فقط با ظهور او به شب می‌رسد. شبی که به صبح دولت کریمه او می‌پیوندد. و به قول سید شهیدان اهل قلم «جایی برای ای کاش‌ها و اگرها باقی نمانده است. عاشورا هنوز نگذشته و کاروان کربلا هنوز در راه است. اگر تو را هوس کرب‌وبلاست، بسم‌الله ...»
@Heyate_gharar</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/663026" target="_blank">📅 23:43 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
