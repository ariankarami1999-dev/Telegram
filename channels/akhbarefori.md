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
<img src="https://cdn4.telesco.pe/file/Ps-Lj4siS2NW9JMPFU7CIEXdxb3Q91K0zBsXb-KFCuNPH09DCoNifX2ycnGuDe_RsweuG7gp57CmyJVKN2Exq-omU_RFn1ROC2WPjZSVM72y9tCYYPamNBFzu8eoSssOy3aI1RbdCvy6BFDkg3t2SX-jV09RW_a41Iz67J11xwgYeAfFI5jrGX9_mfYpk-EtDs_2eVQYQTTFuib4Kr_En4357Jw1S_bzEe2WllecsLIwGq-h0L3HmynaYUE4eX8PnhFPp-pGJFCDBIQdxbzPts7WijDpBIt8OKu0atA3QJHdVkc0qB8zBKqS95wvhzrSCSWGOFXxC2A2iZg7slvNSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-688281">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
هشدار عربستان به ساکنان شهر ابها/عکس و فیلم نگیرید!
🔹
در پی فعال شدن آژیر هشدار، مقامات عربستانی با انتشار هشدارهای فوری، از شهروندان خود در منطقه «ابها» خواستند از هرگونه تجمع در مکان‌های باز و فیلم‌برداری از محل حملات خودداری کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14 · <a href="https://t.me/akhbarefori/688281" target="_blank">📅 21:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688280">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d5430a50.mp4?token=FGoZBlAZ1DOUEMSxK2OMCKYNrMZORCYx73knoZB977m3aPfK8ZCvzdiGOg5YB0y-xxoJ_jlFRS-qux7jqvIaRJtAqWX_DbvljklxK_8ZYNy0JSdGtiap5ZTA4nq_KfSoMQQXYWcLq-J07QeUTVNWPS_1D41rZeG4YIIQYwG6MV7IbgZO05cyGwsE6dxegXmao5tHIRCVtjDGBOENAUwy31BNnH6oMID0dgc6sMW56B-GZni6xpCG9RSeEz30DXIZQz3yMI6joADUpRWO-sFRxucID2Zz3w7lPJHXyV0iIPGEyIAuk64C8RCdW5GHv3yn0L8MDkPy_rZV96jRnAPryA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d5430a50.mp4?token=FGoZBlAZ1DOUEMSxK2OMCKYNrMZORCYx73knoZB977m3aPfK8ZCvzdiGOg5YB0y-xxoJ_jlFRS-qux7jqvIaRJtAqWX_DbvljklxK_8ZYNy0JSdGtiap5ZTA4nq_KfSoMQQXYWcLq-J07QeUTVNWPS_1D41rZeG4YIIQYwG6MV7IbgZO05cyGwsE6dxegXmao5tHIRCVtjDGBOENAUwy31BNnH6oMID0dgc6sMW56B-GZni6xpCG9RSeEz30DXIZQz3yMI6joADUpRWO-sFRxucID2Zz3w7lPJHXyV0iIPGEyIAuk64C8RCdW5GHv3yn0L8MDkPy_rZV96jRnAPryA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا دیده بودین رعد و برق از بالای ابرها چه شکلی دیده میشه
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/688280" target="_blank">📅 21:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688277">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
از انکار واقعیت‌های اقتصادی تا دلاریزه‌شدن انتظارات مردم؛ چرا مردم به پول ملی اعتماد نمی‌کنند؟
🔹
سال‌هاست سیاست‌گذاران وعدهٔ کاهش نرخ ارز می‌دهند و مردم را به سرمایه‌گذاری در سپرده‌های بانکی، بورس و صندوق‌های سرمایه‌گذاری دعوت می‌کنند؛ اما در تمام این سال‌ها، کسری بودجه و چاپ پول بدون پشتوانه، ارزش ریال را کاهش داده و مردم را بیش از پیش به سمت دلار سوق داده است.
🔹
در این ویدئو بررسی می‌کنیم که چگونه انکار واقعیت‌های اقتصادی به دلاریزه‌شدن انتظارات جامعه انجامیده و چرا دلار به معیار اصلی قیمت‌گذاری در کشور تبدیل شده است؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/688277" target="_blank">📅 21:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688276">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142daa5f1e.mp4?token=NC1pwAJr0XE8LGsM4niaCnEj5PV37AUAQ2BlzIkJc4MtfEmZwA5Ypd5nIiD7lHrU-aHKtVNHwbrO3OehQ4Ny4NcWyNjoFK2IhXKIOHlz5Idbs7kIqGDC3DxP8CUgDVsIUbz63B98jbndr3Duf4C74mkgTu0k3FTzNbRaaWxP2m-8jfVO-vYAkDRS3Cuf2BDe9auS0PW4yE0c1CvYq5t2dC0RuWh35J54u3B9xjDzQYDkgrAlxPLTMQpeBKwa-cJW4FmU0f72ToE2eetLTFEOqn080UT2S8pTam63LSJzNy0wKqQ37sW1GtfeT93kwBxhTjQvAEpaPFNomARGHGtugQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142daa5f1e.mp4?token=NC1pwAJr0XE8LGsM4niaCnEj5PV37AUAQ2BlzIkJc4MtfEmZwA5Ypd5nIiD7lHrU-aHKtVNHwbrO3OehQ4Ny4NcWyNjoFK2IhXKIOHlz5Idbs7kIqGDC3DxP8CUgDVsIUbz63B98jbndr3Duf4C74mkgTu0k3FTzNbRaaWxP2m-8jfVO-vYAkDRS3Cuf2BDe9auS0PW4yE0c1CvYq5t2dC0RuWh35J54u3B9xjDzQYDkgrAlxPLTMQpeBKwa-cJW4FmU0f72ToE2eetLTFEOqn080UT2S8pTam63LSJzNy0wKqQ37sW1GtfeT93kwBxhTjQvAEpaPFNomARGHGtugQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرانی بنزین در آمریکا صدای کامالا هریس را هم درآورد
🔹
کامالا هریس در پمپ بنزین: سلام به همه، من اینجا در شارلوت هستم. از زمان آغاز جنگی که ترامپ انتخاب کرده، هر بار که باک خودرویتان را پر می‌کنید، ۱۵ دلار بیشتر هزینه می‌پردازید
🔹
قیمت گازوئیل هم از زمان آغاز جنگ ۸۰ درصد افزایش یافته و بدون شک این افزایش قیمت روی هزینه کالاهایی که با کامیون‌های سنگین جابه‌جا می‌شوند نیز تأثیر خواهد گذاشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/688276" target="_blank">📅 21:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688275">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz9MpRuJJffBlIX8DDZlaKbMNLdrgPp_Uwvtd8mQU_1WexMqH8tnxuI3n1r_pEgQ7C1iYeKl1ZFsjjwlpUmWxUGiQ-xE7ZNDqmonKBSGp8E6o8A6Iu2CVDvxmHt1r7BPV5FBqhVEeDJ-_QNgQGrvZKEyS_8nZ64eLPAz8G12xE3VHqz4agmdORva5tXq9sdzfEzbpmHlnZGFZ562Ch_JPig20bZ64rxViQ8hIfGORDJE3ND_9hK-R0ZPlfRglFTwphOvnd0N3AInaEqo7YOA-nAuvV_YknbAGdyljOrAjSdF9YVExyLhubvLzDdzoX9Criv0wSsP_5p83vp2txamEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
سرنوشت طلا، دلار و باقی بازارها
در ۶ ماه آینده؟
🔴
امشب اکواحسان (بزرگ‌ترین رسانه اقتصادی ایران)
🔴
برای ۴ میلیون مخاطبش لایو داره و پرده از ۲ تاریخ مهم سیاسی-اقتصادی تا پایان ۱۴۰۵ برمی‌داره
✅
این لایو حیاتی؛ امشب؛ رایگان توی اپ اکوتراست برگزار می‌شه
⏰
زمان دقیق لایو فقط توی «اپ اکوتراست» نوشته شده. همین الان نصبش کن تا جانمونی:
https://ecotrust.ir/app/live-stream?utm_source=ArshiaYar&utm_medium=TelKhabar&utm_campaign=live-ehsan-0606&utm_term=socialproof</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/688275" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688274">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrCro0SkVM3D2BDT-v15kfZqT-vl0MTOUHSag4_YQYXSDqxptI9s3FC5kUXLkpU1zpDYnMNSHr8K0_WrGnMhTAJMT15EOq421Ok2mUJ1MTHiSMDjYXZSkupPnsOxCsiJ9KpiFObc4z7HnGBu_uuJVBrhESwK79QQZzepHpPcuPae2AsECRswYvR4iQm1dMKZK3J2TT-eJpiSARVeqqPcjSlyBuqsww5OgbyEIX_PqnShULu1N45EDwb4ug_cxpoVAFwhUbAmH8-l7eO5MkHb34IM88mUPv5LUnjwRkqVG2phJGkvmHByhLJ2aHvdPt0A-bw_rRlgNPuvnKUlT0xUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با هفته دولت و در آیین «یک ایران متصل»؛
بیش از ۵ هزار پروژه شرکت مخابرات ایران با حضور رئیس‌جمهور افتتاح شد
https://www.tci.ir/portal/home/?NEWS/235300/235321/575208/
@tci_iran
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/688274" target="_blank">📅 21:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688273">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
وزیر نیرو: رفع خاموشی‌ها در جنوب کشور در اولویت است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/688273" target="_blank">📅 21:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688272">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
دستاورد تازه شرکت ارکان سازه در سریع‌سازی پروژه‌های ملی
🔹
بار دیگر بخش خصوصی در اجرای پروژه‌ای
ملی و ماندگار
، رکوردی تازه و متفاوت در سرعت ساخت، همراه با کیفیت و نوآوری به ثبت رساند. مجموعه‌ای
هوشمند با ۳۵ هزار مترمربع زیربنا
، تنها در مدت
۲۲۰ روز
، به سفارش فراجا و با اتکا به توان مهندسی و اجرایی شرکت ارکان سازه احداث و با حضور رئیس‌جمهور به بهره‌برداری رسید.
🔹
مجتمع شبانه‌روزی آموزشی و فرهنگی سپهبد شهید محمد باقری با ظرفیت
۱۲۰۰ دانش‌آموز
، مجموعه‌ای جامع از کلاس‌های هوشمند و آزمایشگاه‌های عمومی و تخصصی شامل
هوش مصنوعی، الکترونیک و مخابرات، پهپاد و رباتیک
تا مجموعه‌های فرهنگی، ورزشی، اقامتی و رفاهی را در خود جای داده و با برخورداری از فناوری‌های نوین و استانداردهای روز دنیا تجهیز شده است.
🔹
این پروژه، نمونه‌ای از
ظرفیت بخش خصوصی برای اجرای سریع، یکپارچه و باکیفیت پروژه‌های بزرگ ملی
است؛ ظرفیتی که می‌تواند در مسیر توسعه زیرساخت‌های کشور، نقش مؤثری ایفا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/688272" target="_blank">📅 20:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688271">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
دلیل رسمی کم شدن سرعت اینترنت ایران در ساعات اخیر اعلام شد
معاون وزیر ارتباطات:
🔹
کندی اینترنت ناشی از قطعی فیبرنوری در ارمنستان است و تیم‌های فنی در حال پیگیری و رفع این مشکل هستند./ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/688271" target="_blank">📅 20:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688270">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpS7ieWQtRVNd9FCtpcYYuvLh4P0uVMP01qBMazjRYuVO51oAirCfiRQS48OVrxd_zRGUFA9Z5c9jhxAPp_8L4WFtyHyd1F6tQ4wusUpJY5sSW1Y_MJXobsa67BzJYi-dcUI7GHzkVnK9KqPy_IqrJZ8zsqHoqMXr8TrCp9cvdMU7ErK-mSlhQH9ZFm9kYxVo2NvI51IGWOSv20_OGWUtRrJnMWDp6rtKTu9gMSCjhJ4vYNuKCFDo3BizaOlCvr7ZK2fFlJqNLQgm9UuTKCmYdkx_SEcM1aZTxpY51cs-RdvY2aFkoparNS6hj0swxCqeFgjcTzUVdhz0eXd1EhmvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر راهبردی نفت آمریکا باز هم کم شد
🔹
درحالی‌که قیمت نفت امروز به مرز ۱۰۰ دلار  رسید، آمار جدید ذخایر راهبردی نفت آمریکا که لحظاتی پیش منتشر شد نشان می‌دهد که این ذخایر ۱.۲ میلیون بشکه دیگر کاهش یافته و به ۲۸۵ میلیون بشکه رسیده.
🔹
میزان این ذخایر از عدد بحرانی ۳۰۰ میلیون بشکه هم عبور کرده و درحال نزدیک‌شدن به کف عملیاتی ۲۷۰ میلیون بشکه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/688270" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688269">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d03ce3a78e.mp4?token=H894K20lnruGjpFYiEdPaBT92uayfrQMfLpzYG9ieBJjYb6LJ4nMTM514jzaLeuJFWmnmlRinCBDlx8iw_HAw5j5QaPgfKflxSUs5Vq-IGwDLn1EDMqzWOIGepKftLCdZhxDEIW34Tw5nZa8TOCj1XV9a3y18u4KqjitVFXQ_KrUx-FqS2qdOPr1WOEEj3dKsUNow_aVS5IzU2gGGPgVN0DRSIXAolvL40Gpd0JejJLevJgZfJohrh2SjR8tM6tVkb29E2Wwe2lof3dcZ8BJF86wJJC3C3FwonhZcTfaqtVGkciiHOW-xWjdGqD22E0tn6LX12qXR7je19fsWpBjyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d03ce3a78e.mp4?token=H894K20lnruGjpFYiEdPaBT92uayfrQMfLpzYG9ieBJjYb6LJ4nMTM514jzaLeuJFWmnmlRinCBDlx8iw_HAw5j5QaPgfKflxSUs5Vq-IGwDLn1EDMqzWOIGepKftLCdZhxDEIW34Tw5nZa8TOCj1XV9a3y18u4KqjitVFXQ_KrUx-FqS2qdOPr1WOEEj3dKsUNow_aVS5IzU2gGGPgVN0DRSIXAolvL40Gpd0JejJLevJgZfJohrh2SjR8tM6tVkb29E2Wwe2lof3dcZ8BJF86wJJC3C3FwonhZcTfaqtVGkciiHOW-xWjdGqD22E0tn6LX12qXR7je19fsWpBjyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از لحظه رهگیری و انهدام پهپاد متخاصم MQ1 دشمن آمریکایی توسط پدافند پیشرفته نیروی دریایی و نیروی هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/688269" target="_blank">📅 20:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688268">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
هشدار اضطراری در منطقه ابها
🔹
سازمان دفاع مدنی عربستان سعودی با فعال کردن سیستم‌های هشدار زودهنگام در شهر «ابها»، وضعیت اضطراری اعلام کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/688268" target="_blank">📅 20:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688265">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در منطقه جازان عربستان سعودی
🔹
برخی منابع غیر رسمی از حمله موشکی یمن به این منطقه خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/688265" target="_blank">📅 20:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688264">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAB2hMsWsGM2fGoyA6QEThrg6vMwE88ZYz4Nfi-VYnUIi94bvzTzRVIj5UAu3Zg3_KrG-4eSNCogE0218ixfayUKFQJAEfisQVKaHDErTc5H0cz4JQCFdS-fhGPJJh9Of5kFFdCMqTWRsIZmv-v1b2YwQghkaETKn_7KL6deTI5JpXkKuX16JoiVIw8UMsdJhX4SUdAtpm7in12ETB-HFnBqG5Q366BkbAOKGMv7n2OwXCrb0rpQSv9SkH6lXSHbglYizwxNaA-zUQIzIzQIq4LXpsN_QtU-GfKr8xyiCQiS3jiGaB1N0rUI9fxmMCZWsV6Ff0D_BI5MziaooGrygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمک میلیاردی یک خیر برای جبران خسارات جنگی مدارس و دانشگاه‌ها
🔹
یک خیر به صورت داوطلب با همکاری جمعیت هلال احمر متعهد شده است مدارس و مراکز دانشگاهی خسارت دیده از جنگ را تا سقف ۱۵ میلیارد ریال بازسازی و مرمت کند.
🔹
مدارس و مراکز دانشگاهی واجد شرايط می‌توانند با ارائه مستندات و مدارک مربوط به میزان و نوع خسارت های وارده درخواست خود را جهت بررسی به دفتر مدير عامل جمعیت هلال احمر استان‌های سراسر کشور ارائه نمایند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/688264" target="_blank">📅 20:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688263">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632c2a3605.mp4?token=mSC6V0wmXhOF1nLDk9pOd0S4sq1ixycdG8m6Hw2Nd4P2AK92z3hDKqfS1O1cgBTuxgW1S6HBdOte6Ik9DVHO07aEtrU0469tHIJUEkJL5N5vksmvpxeypwULBdOPw1YOVFZ98G2GWBaRC_7p1xMrv96V29nKktE_5SmuG6CAb2XW-h9IhqEacPoLzZHn3vyKX2PM9D52I3Gi1eBIJTObZVfpYYvA2ZPftPYw0F9Lodk1ULsOhA4RzbkQ_63Gy30uGI0dF6AJycrR4THA7elbgHM-oFJGyFnn8EJDb4qkylf53zLR_X9ep4guFu3COn2H17_ydtRpeMbVAjVjEzKxkxP_SKmYCbLT0I4uqxx-wu0ewdswQ_YqcpbEqtLRV1K7fMMAewUAAaLJVZrMke6n5X2rkag4r_TtQLFL97Gz11KmFPDk-fMAUlVLQvAhRsYRjg4plSihF2CK7ckc5wMlc-3Dpv8pP_nGoOjZwsKhoxd-tDIhhqH6Q1CNIYd3zAY6Esj2CNr5c-Sd4LZ1Ox8B82JthPQJhxF4nwSnCiVRgneeegZugtfmwNEyi5IE4UUEASzpZhBOWiuEIJdk6La8DRZeRxSdQ2lauLGNhPdtH85mKgyfDeWcU5e_4z05Bc5KdOPDpKgHEnnC3p0G_jY84QWec6_xu1D5bgF0E_3Fo3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632c2a3605.mp4?token=mSC6V0wmXhOF1nLDk9pOd0S4sq1ixycdG8m6Hw2Nd4P2AK92z3hDKqfS1O1cgBTuxgW1S6HBdOte6Ik9DVHO07aEtrU0469tHIJUEkJL5N5vksmvpxeypwULBdOPw1YOVFZ98G2GWBaRC_7p1xMrv96V29nKktE_5SmuG6CAb2XW-h9IhqEacPoLzZHn3vyKX2PM9D52I3Gi1eBIJTObZVfpYYvA2ZPftPYw0F9Lodk1ULsOhA4RzbkQ_63Gy30uGI0dF6AJycrR4THA7elbgHM-oFJGyFnn8EJDb4qkylf53zLR_X9ep4guFu3COn2H17_ydtRpeMbVAjVjEzKxkxP_SKmYCbLT0I4uqxx-wu0ewdswQ_YqcpbEqtLRV1K7fMMAewUAAaLJVZrMke6n5X2rkag4r_TtQLFL97Gz11KmFPDk-fMAUlVLQvAhRsYRjg4plSihF2CK7ckc5wMlc-3Dpv8pP_nGoOjZwsKhoxd-tDIhhqH6Q1CNIYd3zAY6Esj2CNr5c-Sd4LZ1Ox8B82JthPQJhxF4nwSnCiVRgneeegZugtfmwNEyi5IE4UUEASzpZhBOWiuEIJdk6La8DRZeRxSdQ2lauLGNhPdtH85mKgyfDeWcU5e_4z05Bc5KdOPDpKgHEnnC3p0G_jY84QWec6_xu1D5bgF0E_3Fo3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا و اسرائیل نتوانستند دستاورد راهبردی علیه ایران ایجاد کنند/ ایران همچنان یک قدرت منطقه‌ای باقی مانده است
دکتر گاردونیو، تحلیلگر و استاد روابط بین‌الملل دانشگاه UNAM در
#گفتگو
با خبرفوری:
🔹
ایران پس از ماه‌ها جنگ توانسته هدف اصلی خود یعنی حفظ ساختار سیاسی و ادامه حضور منطقه‌ای را دنبال کند.
🔹
آمریکا و اسرائیل هنوز به یک دستاورد راهبردی تعیین‌کننده در برابر ایران نرسیده‌اند و نفوذ منطقه‌ای تهران همچنان پابرجاست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/688263" target="_blank">📅 20:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688262">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت شرکت ملی پخش فرآورده‌های نفتی: کسانی که کارت سوخت ندارند با مراجعه به سامانه سوخت من، یک روزه کارت سوخت دریافت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/688262" target="_blank">📅 20:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688261">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
منابع عربی: پروازها در فرودگاه جده متوقف شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/688261" target="_blank">📅 20:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688260">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
منابع عربی: پروازها در فرودگاه جده متوقف شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/688260" target="_blank">📅 20:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688259">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52aab7547.mp4?token=dfbZc7_yRUK-gRwF_pDl99IgnP1VhsD5eunJtUFhCavqqH0cOOh7ag1A-UPYprIAJFOlgaUnwIwfMoSPXxQ8k8_W_qCi2wIjSG-Q_qEvH5bf0RJFYiDmu3mTgNqcjJDVwat_QkPSCYB1pbLkFyJ3J8shENDsCbVLQBcGEfmyEg3NbIy1xLEkfDjrVXuyg2NlNtjWEIa2aD9MrAgxcywUsrFQAHAAQKS8vRQHoVRUlRARgA5CiqSeoqlGIOkqHC5taLwVjvuA5HQgE4Ibpl66jJG0at0p8RAsBN111YC4EHR3-qYAODeJstvmnJ3CCmc8Q6-iY2QQAz9CYqarKoFUig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52aab7547.mp4?token=dfbZc7_yRUK-gRwF_pDl99IgnP1VhsD5eunJtUFhCavqqH0cOOh7ag1A-UPYprIAJFOlgaUnwIwfMoSPXxQ8k8_W_qCi2wIjSG-Q_qEvH5bf0RJFYiDmu3mTgNqcjJDVwat_QkPSCYB1pbLkFyJ3J8shENDsCbVLQBcGEfmyEg3NbIy1xLEkfDjrVXuyg2NlNtjWEIa2aD9MrAgxcywUsrFQAHAAQKS8vRQHoVRUlRARgA5CiqSeoqlGIOkqHC5taLwVjvuA5HQgE4Ibpl66jJG0at0p8RAsBN111YC4EHR3-qYAODeJstvmnJ3CCmc8Q6-iY2QQAz9CYqarKoFUig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت: در خصوص انتقال کارت‌های سوخت به کارت بانکی، طرح شناسه‌دار کردن کارت‌های اضطراری را کلید زدیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/688259" target="_blank">📅 20:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688258">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8dcWAFSd5-9DzjYasmbM0T0LkzOA1vjRvL55rP-3AXp2wXs7J6JsaQjCsgTj4lVjIijRJkNYRUzkV5T8vt19xGG56G1-AysHgH8pCRL8XrOe191aXvQ73d0zxET8ZVzig6OP7hvPfvEjzuDRKpSYiLfkGoIw7r-9TV7YoWLWKCHQJC_KIc8uMp9N4N59JZBOjPoWof7zbEU3rF0s61uYlaF_Yha7SkUl-nZpNu7UGlRlbsYBX6TGnfGr3Op899Em-x6tsLRGcg3Y2ftZ6QPveQVlVOLJakZSA0VCD8llyLMdCh3982q3jHmlJNE4r__XtDgWc2DCRtYjoOq4jIA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حملۀ اشتباهی جنگندۀ سعودی به مواضع خودی در یمن
🔹
وبگاه خبری «الخبر الیمنی» گزارش داد که یک جنگنده سعودی روز گذشته مواضع نیروهای «العمالقه» را در استان تعز بمباران کرده است.
🔹
طبق این گزارش، ده‌ها تن از مزدوران وابسته به ریاض در این حمله کشته و زخمی شده‌اند.…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/688258" target="_blank">📅 20:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688257">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">13 Ane Manaee (1404-01-27)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/688257" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه سیزدهم
حجت‌الاسلام امینی‌خواه:
🔹
وقتی تقابل حق و باطل به مرحله" بود و نبود" رسید، مذاکره با قاتل یعنی ساده انگاری سیاسی!  [01:06]
🔹
تقابل نظامی و هیاهوی رسانه‌ای دشمن، نشان استیصال او و گواه قدرت ماست. [11:15]
🔹
اهمیت شناخت و مقابله با “مُرجفون” به عنوان عوامل اصلی جریان تحریف  [18:10]
🔹
مهمتر از اِذن رهبری برای مذاکرات، هشدار رهبریست درباره عدم تکرار تجربه برجام!  [31:30]
🔹
"پایتخت"، سنگر مقاومت!.. نقش رسانه  در تقویت یا تضعیف باورهای دینی و انقلابی.  [36:20]
🔹
اِهمال در تحقق خواسته‌های رهبری، گواهیست بر شکست‌های ناشی از موانع درونی و نه الزاما دشمنان بیرونی! [43:10]
🔹
مسئله فلسطین و غزه، تکرار تقابل تمام ایمان است در برابر تمام کفر، و هر اقدامی دراین میدان، معادل عبادت ثقلین! [46:30]
🔹
تبیین شرایط حساس جنگ اُحد و نقش تاثیرگذار حمایت های کوچک در میدان های بزرگ  [1:15:00]
🔹
پشتوانه الهی؛ برگ برنده جبهه حق در تقابل میان جریان‌های مختلف و تضمین ظفر نهایی [1:31:35]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/688257" target="_blank">📅 20:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688256">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4XP6QpZfK-fvviO_Ixsk5PsOR3UBaMZjuBs3WlX_wAzLuABh5mFiIoANLwK5ZXG77JtT1FiXxEX8oa-KNrDkkAInlH-EFFhKRbyFXMpTuEYR9UQWEbv9fREb258gXouImX-A8qL4_T5qXttM5ZoW4a3VFFFS29R4x0fo-p3IGYt94kzZGLoLvzsxhXjAwFB15Us54e6XCm4MGJ_SJrq8RBv37xVikk_7_l8RmAA8wxBAiCA_vrLeWo9fY3f8-NDM8fL4Oc3I5nGV6sa8W5NXNypWuRGvate8BGZnwx_YjRLbgT0Fyix8ClgFDWFyPkbUfPzWBrfEC1EA7jwhULRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفند پلمپ کردن برای نگهداری طولانی مدت برنج
😍
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/688256" target="_blank">📅 20:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688255">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV0ZcOLF--0P7fJ7VeYaARLl7_Tq_Fh_So4N5-hU5qGGAhuAP76sCvSNfC6qkvgsbVNp5GOSPwRHSGjcy5F7uSDJwfVM_FAUGiMxdvcTZvwdz6V5_575m_2fBUr_kLORtlPjWo_abqAERDNl6A8ctPA_C6i478jgOFBdMqZZ2A0PhLDlH6Lm_dTEhQCf7TGHPuHonh0bZenT-tk38whVPWJ0IC_0xavC3B16_k-hifJ8rS4cpfSE4wEhtu0q3jmGwhL8U7VSOBOyRHxARw9yLeL8HRLo_7KnNdreJS4NUvEoVi_9KcYiPQqc09gSw34FtdPSU9dXcOCf9VCL00BQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیر سطحی هوشمند Dive-LD یک زیردریایی خودکار آمریکایی با توان ۱۰ روز فعالیت زیر آب و عمق عملیاتی اعلامی ۶۰۰۰ متر است که برای شناسایی، نقشه‌برداری، کشف مین و پشتیبانی ضدزیردریایی طراحی شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/688255" target="_blank">📅 20:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688254">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7emZFsuKC1VkJ0KcxcNH2-EwuzVW7gWJRncWdyy7Yko9IJpOeqb-y5eaPlZZyM31Desp3bgwEfdXnSdyFr38CdDCrZTwJCgPRMIlgVBxqBG2kH0xBvQdse3mAn15Sqs-3nkOD8h9Cp61mN3mduv3_se1UNci9JfRIhRFH-XDNInEPVUUoMf3p8255gZBeUXso2Athwp5VdCbqDM8MDSRhcVbPaQC85g0BfX-rojU7J3dmf-WR21ERYdjj-nkvn9tYTF_wc2rT-dZiMD-X9_9VDzuG3wP8x7QSb1juJ5Rp_QggixN8PyRKVsE88Yp7MD8xCd8SnGJ98vOs_V2UsNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون علمی ریاست جمهوری : دوران صرفا «شرکت‌سازی» تمام شد؛ فناوری باید به بازار و ثروت برسد
🔹
حسین افشین، معاون علمی رئیس‌جمهور، در نشست شورای اقتصاد دانش‌بنیان خراسان شمالی
از تغییر رویکرد معاونت علمی در حمایت از زیست‌بوم دانش‌بنیان خبر داد.
🔹
او تأکید کرد حمایت‌ها دیگر صرفاً بر افزایش تعداد شرکت‌ها و توسعه کمی متمرکز نیست و باید به سمت
شکل‌گیری زنجیره‌های ارزش و بازارسازی برای فناوری
حرکت کند.
🔹
به گفته افشین، ظرفیت‌های علمی و صنعتی باید از مرحله پژوهش و فناوری عبور کرده و به
تولید، صادرات و خلق ثروت
منجر شوند.
🔹
در این رویکرد، اتصال
شرکت‌های دانش‌بنیان به دانشگاه، صنایع بزرگ، بخش خصوصی و بازار
برای رشد شرکت‌ها و بالابردن سقف اقتصاد دانش‌بنیان کشور در اولویت قرار دارد.
🔹
پیام معاون علمی روشن است:
زیست‌بوم دانش‌بنیان با تعداد شرکت‌ها بزرگ نمی‌شود؛ با رشد شرکت‌ها، ساخت زنجیره ارزش و تبدیل فناوری به بازار و ثروت بزرگ می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/688254" target="_blank">📅 20:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688253">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCHUTCOswoRRuB95BIWO8H4EMa2OQwUa2Uutbomi8kUAsqMSOQTBSPTPC_Twg1Uf2FlkkPJIEmAKUipiIwpuN98X1x_pdzgCNTwSQQRIHJuLiQBPcIg245YysEpMuotoXuiuEMji2H9vtbty8zEspzkptwT1Rdk-kMx2GY31jxnDFCWI6axNkS3LNKTcnxXegdb8o-BDesFMJORRnbIUAeEu5kwESW8cMa2hANII4DWTmx2HEsRPsZMYpQgJwYmc3oyMA0w8wzQrSZyPEF1wP6onkrr3UuSTXD2ZoKJwkbvIW3H6ETBQ2OVY1i8yjDZKDsJNNZbRIPflqlvDxlk6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتمین نمایشگاه توانمندی‌های صادراتی جمهوری اسلامی ایران  با مجوز رسمی سازمان توسعه تجارت ایران
در شرایط کنونی اقتصاد و تجارت بین‌المللی ، مسیرهای تجارت بین‌المللی را با چالش‌هایی مواجه کرده، این نمایشگاه می‌تواند فرصتی برای حفظ ارتباط با بازارهای خارجی، یافتن بازارهای جدید و تقویت مسیرهای صادراتی کشور باشد.
با توجه به تغییر مجری این دوره، ستاد برگزاری تأکید کرده است متقاضیان حضور، ثبت‌نام خود را صرفاً از طریق مسیرهای رسمی اعلام‌شده از سوی شرکت نمایشگاهی نبراس انجام دهند .
جهت کسب اطلاعات بیشتر و ثبت نام با ستاد برگزاری نمایشگاه در ارتباط باشید
02192002799
09127989492
https://iranexportfair.com/</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/688253" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688252">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw8wuB7NXXG0AaoLQnQixaWhU3xz3eKCNCBeyntM5y3fagmzTb0S5MkcCvPQXhAbjinGrLEV5wUesdFaxwwJP8NDc6wx7THM43AUSOngo1acBBGP_sav2umbwHyLRI2D42KdM7Mfjai17tX8Uexu0dKuJPeg6Hc9aXyVZk1QfWbXDH-u-0cRvEczUFCVODxSJoVnME_59WTDQ6a-MugogJWkUWxVjNiikv0A2NgRegK0WbcYoKaxm6Vqmy7vGEAtVpW7lPRh_29ZDXX-DP2d2K0kE2tfJ4IrbPR_Mr5QJbUrLnhhBdCriachRBixVpOsDGEYLCdovbapjRovFdMQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای آمریکایی :چطور ممکنه چنین چیزی بشه؟ مگه ترامپ نگفته بود که تنگه هرمز در اختیار آمریکاست؟ من هم فکر می‌کردم ترامپ گفته بود توان نظامی ایران کاملاً نابود شده.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/688252" target="_blank">📅 19:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688251">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0aa8cbfc5.mp4?token=NRPQysIRMq8deBZpbRxQD7PN3MtX2JaCijGGbWcPszuBoSqqPKBZj7MvB0MOWRNyyPpvZn2WLwaomJamSzu4MnHH98Vhon9cMXIE4cmTHK1QempIVMeeA-zhPn82ENZZ9aGAUbdiOqFrVEvtBd6XctshWpszXBn2curbvs1lMgN5EFwTg4h0CdDMx-CgEH9LA0bmOS_wlB0bpspAxnaZGYehl4M9paAY2aWjIMXlMAYr69KEWpv0_oCzyC-naIIUgeU1JEXyYoQV_8Hzk5CVxGuOgGJbjMgtrFOP3_NjiOrwhDVFI927SCgxF_J04K5xOS8O9Px8S_xV_4wbOVEZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0aa8cbfc5.mp4?token=NRPQysIRMq8deBZpbRxQD7PN3MtX2JaCijGGbWcPszuBoSqqPKBZj7MvB0MOWRNyyPpvZn2WLwaomJamSzu4MnHH98Vhon9cMXIE4cmTHK1QempIVMeeA-zhPn82ENZZ9aGAUbdiOqFrVEvtBd6XctshWpszXBn2curbvs1lMgN5EFwTg4h0CdDMx-CgEH9LA0bmOS_wlB0bpspAxnaZGYehl4M9paAY2aWjIMXlMAYr69KEWpv0_oCzyC-naIIUgeU1JEXyYoQV_8Hzk5CVxGuOgGJbjMgtrFOP3_NjiOrwhDVFI927SCgxF_J04K5xOS8O9Px8S_xV_4wbOVEZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیشه دودی‌های جدید در چین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/688251" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688250">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فروش برنج کم شد
محمد مختاریانی، رئیس انجمن تولیدکنندگان برنج در
#گفتگو
با خبرفوری:
🔹
برخلاف انتظار فصل برداشت قیمت برنج کاهش نیافت و همچنان حدود ۵۰۰ هزار تومان برای بهترین کیفیت برنج باقی مانده است، علت اصلی افزایش نرخ ارز و فضای تورمی است که کشاورزان را به مقاومت در برابر فروش با قیمت پایین ترغیب کرده است.
🔹
با وجود تولید خوب و واردات منظم تقاضا در بازار پایین است و مردم توان خرید ندارند، همین ضعف تقاضا باعث شده قیمت‌ها بیشتر از این افزایش نیابد، در غیر این صورت نرخ‌ها بسیار بالاتر می‌رفت.
🔹
درحال حاضر کمبود برنج نداریم ولی کشاورز تمایلی به‌فروش محصول خود ندارد، زیرا کشاورز معتقد است قیمت حال حاضر برای محصول خود کم است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/688250" target="_blank">📅 19:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688248">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjJ-vDL12N8f3FlFb86sKu3t9gEP3yjUY0QqvDqiGHy0VBJxp4MYg8NHmj_yxpaHBw_ABrmYX_nVEC5OAjV_d0QzLVpEpnA2ht-UJhfUCqck2NdpcSzjNUJ_cbNEOJVmkHarzjSKeYTack7tuJOXo5Me_NvQZlIGDmJE_IcNbVfKR9nYBfCW9xZuBnWpzOFLZ0FULBiydg9iyYvWfykZTGkVrLv0x9JYf-dNzAxgYaq45vjP3r_GPJQayvhJfjbk6lfaBo-4bcwC_y_Iqu2WYaOHLtbH-Z0i_ObnW2tYcva_-E7txgXBiEJC5XMjfDwDumWjL9o96dQppFY_5iWJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۲ کشور خواستار محدودیت تجارت با شهرک‌های غیرقانونی اسرائیل شدند
🔹
فرانسه، بریتانیا، کانادا و ۹ کشور اروپایی دیگر در بیانیه‌ای مشترک از اعمال یا حمایت از محدودیت‌های تجاری علیه کالاهای شهرک‌های اسرائیلی در کرانه باختری خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/688248" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688239">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ei1sElqJV-Kr8NCe4sYVz38zu_6PemwJcCkmOICKNMotBtPRPr-YeA8wNKwuc8dm0MdTOtbTz_I3hydHkghIzNr4uZobGO5T8TgmrAv4-0RYdymN5lTKuxMEEigZ-jq41QFZTXhvirhLFoA0Zw5QG56TZU8ILyKYxBAk4q1Gh6buB6I_dzhP3UeL_QQ8D0Wrh3k8Un8FYEH9fL-0RiCbIeZo4cpvLy2pVcJxQwetylBLgb_9R7QUghrJf-_a3BaMFQzrJL0Tfs9pIpSHDkyqEPLRhVPs5yvwbDCl8XZLh-9zH8hTiAomywd7QZYLQ0wMmxbiXl3dpX7l6tHm8jO5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFxMa1nhgoAUvf_8p6xVXNxZH9oQ5HmfXPXAw6A7enboLjIL4WT1HL70JqlZFa2U_fIe0qzWN3pG626LFxwJtAowux_sn5nJ4140jjPXgttaKdAjfnOsG5bySq_i9xwgXvruuAeNP5RgOwZWu1Qtekwf-Yl2LUpo8tqoFxIs13rNq4tb-Y9BTPHCfvwDJjjVllupO0YAubAtVBN3rpsAuKfTmczep1vajNMo1l29q8oXqB8Kq4bJgoVNy-MALYM4OlaNXTUzN1yGqvVaWymqDcrlXFf6p-Dhu8iND4CCywYQR0cKf2Ei4rWmuMbLPvGfjHLqFskniP7y5w2SceM4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZKCQFe1brgBFFEq1knL4nI7arZ3QhyA7AVXlPHNpuhzG04eXHIabf9j9BwJ9ZlWrazmqEO7gDKBswweqUl6fZ2nnmJ2zqUNbeir19BLPmHK3QhuyBZlcY0sDP77WSKJFuC2jRfCTFjN7JNozX1Mk6L4ijthO-69z9x7Txgp02YHAcRZx61ezJKhHxizdU_Q0HZ-hPBk3bt1dJxtkIp9L9F4RToHELTAZHQy9ECQQx_y9J6yFBj_xptyapnReaaMPTGttOqvGyzzTzAmtMPJU_Z6yFmD80vT8eeMWbDrOZEkt6VXUkBEnqiuSl_yaqK38MJ-_GYgEiSvelxl_Gv6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGeleim8YrH7fP95qaXVeUNLWxQc1fetFyElhVQcE4yzHPLkVDWfzrGLiawv1mQwAi0JrGKw_P5m7PQQzgQBzxR99LtKkWIw0--ItI0scJV1I9-FXMV6nc5gIQeOeImyfuN3F-9ihUEDw6FwkEmj5-sxoYESsSNuz2EzPe2fLdsKj8ZCCwcCq0-LzR-gZ5FBZ4fVDoLfSeb15h1OwxiVXWV4IGkzVbZ1VKO27acI5Db6U5Cnfc2w6UsP1kb49uk5232lw7VXgGGWsGBHQc0RgQ65mX8GYTCDWJCzyeIJm5YmYMxF3Dpn-d7ii4DJ1G5SlhEDFXLn4-Rza-LawI_Xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vSfSHfpCEv4g5WZR5NYcrJqUE_a6pzDTm2d_fKe-IbNZolUq-QaEFTZolTXmnv7ac9jOKhCPy_MwIB_xW8vkGtvEOcru3OqQ10s_0nsL5t81qUOFok_zjfuOiyeiUDbRHUXr6e2_nLheOAxX9ZimvgNVKzRwdQDFpHl6GYZA7CUJwptzzSAg96YALnQKwDsG2ccoHJGZhdVsW2TojF9Ozc0lVzaSGfJMkSwTYcBhigUk8YQPw_r8iEqabgRbKUrcJyBAtbOlDkdzANRwK1EM3a4sEqJhjxT-3AooOWwATsZ_VCpQYn8UsuuTR-A6hNPy6l6mpK-4cxJRmHKlRivU4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRMDE-5Ci1YpT0BIPh-5Sr2xhyridpVP41Y7glyXDwY6iFFcEzVbssGTm8EpTrw2EUu7JNKBXT7umS6PNVKmkTPkP8pMCScvXXS7uBwcJbzNyHRWSDng1byEO1SDvxwxgs95Y2Pij8lamCMi5idQj3aZLOnXcQLuUDr6V095_EGMxx1hEw73xa-BXexseDdB9H7bg6GZH_p05I7QFjvT_PKKV47UfX5K4Io2xMzryNaiBx1xKxhFimRR8z2kM_9mmiC6rnrQozuQtPLUYmxDGpgu1sUR70mVbMDK9S5iMyCp7kw4sNsgUZ06unEkAUaVB6Yh4N6vGr6akD9xNWzHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwWm6Zl-Fl8CI5oRoKkGh5xaVlGCau7XzD1ixAFXMGM1XBJdXU9FFtjuk8i8xlQpUgZkRZ9tL8xjbnQWNKRr1SR9ChrogeivvgEYPr3yyFpBUmiItJ43ed3uiRvc-YSivamHH0tA2dpED4X_nk-l8jSPD4WsMhAREIah9Xp7aO3PU5XHvf7IfYXjyrCmm8HnlzEeUyQDd2Cn1yw4Nf_ivdBOJ163DUh6ArTR8SXkDtVi7vPh2TQYV09s4BDasIWpFpqEPrXOJ-pD8eiy4IJqSnM8a0b-1LClMUxikOJh4kiQdhRxTc4mChSF4922FXwIMQTYiIFsCBOdmO-Ad4sjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCubNeHvJBE5B4imhBBxUfKawuJaeNeitMaXG2tVS-zCQzA9BDVoRPG1-5L9hxeRHZ_Ii9uNRQvgAVK9MiZX0KVJ-87knfhCk257pMKx2H40H-wOFHbZTCIJW1sFl-iDaq-MwHgLrPwLnOezcoYz-PP-aZT3znpFZ8EmfmYTRS-shfGLQT2EC5pM8hohBjBlaGJlcs-l7kFoiv81elMhgsIy27-zLEp2KDZSZcgwOTX3j-F0H7Hz0RHI6yy_nqhyeAazFwJSvxNVQ0cAnf7Zdz_zPJ-lsHsWMiedyCatPncpAkNhc7h1BMpyuqKfL7L1ZxiAW_ej97szbVg1GQv2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-_oIGZgKlNbJEI--4zJNMdnseGiedfmDi5mF8Kcoe2OSz4pvHt06myoe8gdv1WLBoGmIwZ_lg2N_ixn2kwVsAbd2Yyq0XE167ulaY8KWUetiw6wr-eu4vmlX4B3w-9fLGB0jb_zT21DA6NPo1p13LSKCZ3kXWCWkQBiExatpcJCOWuAJVSdZxGPkNAaq7wfQmCQlA8Y_cH8u2OTgfAZpyDu_V3D73cx1WI-sR3KpH4qrPNqVnWjmkys4RycRz2RTaIkXr5tqZzmh6RQpZeQv8foaM3nsY8u4MEZj3Wt0yfMTz6Gg8kvN_U5fjocIhC4mOYeFgqtUEWjntGapFnogg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
انعکاس پیام‌ها و مشکلات مخاطبین الوفوری در آستانه بازگشایی مدارس.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/688239" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688238">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ایران و روسیه برای ساخت نیروگاه‌های هسته‌ای جدید همکاری می‌کنند
🔹
مدیرعامل روس‌اتم از برنامه ساخت نیروگاه‌های جدید و نیروگاه‌های هسته‌ای کوچک در ایران خبر داد؛ هم‌اکنون نیز فازهای ۲ و ۳ بوشهر در حال ساخت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/688238" target="_blank">📅 19:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688237">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سهمیه بنزین خودروهای نوشماره و وارداتی چگونه است؟  سخنگوی کمیسیون انرژی مجلس:
🔹
خودروهای نوشماره و وارداتی طبق روال قبل سهمیه‌های خود را دارند و برای آنها محدودیتی در نظر گرفته نشده ولی باید هزینه نرخ سوم را بپردازند.
🔹
در مناطق آزاد، نرخ سوم برای خودروهای…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/688237" target="_blank">📅 19:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688236">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4550cf9175.mp4?token=ZaVmfbSyu8OXOat7VgOfFMD7y17drniKxKiRvA9x7MnSowjNYmH7oF_hbCAQE-ypKrPRJy7w8MsYnr3AtLQ-O12AxS1-aBlxe841y3CJ3nvFUsYo2SO0nlh8JnDsI74ehtc-dRHwsmxYpjyv8-zK1bjZe7BQKafMn3YwqioXjkSF2kss1ZrNQACG8lUPP-B5X2VjolRupUw0s4Livgc3ocYEualKXuWZ50VhNf8srSyX8sH90Y5UVqQzHaUpQ3r_Jd5pmLvm4sxgIA3LgUGb4Tf93VDxTppr479I5n9knK4Qbvqr4tLldQ-znJKAxSVCKSs6z-Msa3MJGGMfMphhIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4550cf9175.mp4?token=ZaVmfbSyu8OXOat7VgOfFMD7y17drniKxKiRvA9x7MnSowjNYmH7oF_hbCAQE-ypKrPRJy7w8MsYnr3AtLQ-O12AxS1-aBlxe841y3CJ3nvFUsYo2SO0nlh8JnDsI74ehtc-dRHwsmxYpjyv8-zK1bjZe7BQKafMn3YwqioXjkSF2kss1ZrNQACG8lUPP-B5X2VjolRupUw0s4Livgc3ocYEualKXuWZ50VhNf8srSyX8sH90Y5UVqQzHaUpQ3r_Jd5pmLvm4sxgIA3LgUGb4Tf93VDxTppr479I5n9knK4Qbvqr4tLldQ-znJKAxSVCKSs6z-Msa3MJGGMfMphhIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گران‌ترین موتورسیکلت اسکوتری در ایران BMWc400GT
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/688236" target="_blank">📅 19:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688234">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/489bbfab88.mp4?token=YtoMxidaJd6QD0uaJ2sm7OGc4A9QoWed47WCRa7DU5Bf0QcoREjYRMYIukRTM5MAHV429wYis-0KHxLC_orm7ED_oMRREbG0OloM3RXWG1UkbDF3Ka6DpyLTcLmBHrizYiJkB1V6M5iRlPd8V8wg0MARkz9nGgyBMyHxC5my1d_e_kUkQrNoAfiZAKXe7mr5R5chMPRMpzNJvD112I2iuh63t5D7mpt6phpOScbX4VtsnjXt5SmDPC8-fYjujSpcSMBlHFJ2XJOnOnrF8ObMimL2YTxQhHsApLPvfd_y1DUJRyhtRf6lHxVyATvuOEtH2wBSK0Nj2jeI80FP4Ko47A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/489bbfab88.mp4?token=YtoMxidaJd6QD0uaJ2sm7OGc4A9QoWed47WCRa7DU5Bf0QcoREjYRMYIukRTM5MAHV429wYis-0KHxLC_orm7ED_oMRREbG0OloM3RXWG1UkbDF3Ka6DpyLTcLmBHrizYiJkB1V6M5iRlPd8V8wg0MARkz9nGgyBMyHxC5my1d_e_kUkQrNoAfiZAKXe7mr5R5chMPRMpzNJvD112I2iuh63t5D7mpt6phpOScbX4VtsnjXt5SmDPC8-fYjujSpcSMBlHFJ2XJOnOnrF8ObMimL2YTxQhHsApLPvfd_y1DUJRyhtRf6lHxVyATvuOEtH2wBSK0Nj2jeI80FP4Ko47A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آبگرفتگی شدید معابر رشت| هم‌اکنون  #اخبار_گیلان در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/688234" target="_blank">📅 19:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688233">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlHoaMKxjoqLQD1NoU1WRACLQyxqPFnRXlonaRyKhygHukzsPHtJMnVbzILOEvgz2QdK9J1Rndcl2dw0Kr-rjakurthG5_q9Uu51LcpmlVBnPtTK7-p2tirpifNDHmSe4APxvvGE_uiPuBqvWEdVL-IQ-F8Rb5-z-Ayyxo7lS7nBxPC0CvsgCAPe12oyJEMGyuQqQ1tzJZGn87s2mPuXhWFn9esBJCpx5HXWJ7r9_xtGaUu-H8MGezq_rn0xo1P4eS2pYu3uAq2SotS1lmUaRI5w-yMB1wW5kYIpxWADRe3MPgjPkWCY45ubxifBXdY16oBQ_ST2qa8aTl4ZEpH8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار مجلس درباره وضعیت بازار لوازم خانگی: قدرت خرید مردم به شدت افت کرده است
علیرضا سلیمی، عضو هیئت رئیسه مجلس شورای اسلامی:
🔹
بازار لوازم خانگی بیش از هر چیز از افت توان خرید مردم آسیب دیده است؛ ادامه این روند مستقیماً به کاهش تولید کارخانه‌ها می‌انجامد.
🔹
مردم خرید کالای بادوام را به زمان دیگری موکول کرده‌اند. وقتی سفارش کاهش یابد، هزینه ثابت کارخانه بالا رفته و فشار به تولیدکننده مضاعف می شود
🔹
فروش اقساطی باید احیا شود؛ البته نباید به شکلی باشد که هزینه نهایی برای مردم بیش از حد افزایش یابد. منابع اعتباری باید حتماً به سمت خرید کالای تولید داخل برود.
🔹
حمایت از مصرف‌کننده فقط با کنترل و سرکوب قیمت رخ نمی‌دهد؛ اگر درآمد خانوار متناسب با هزینه‌ها رشد نکند، حتی کاهش قیمت هم مشکل را حل نمی‌کند./ خبرگزاری میزان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/688233" target="_blank">📅 19:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688232">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T59agTXvkJSr_y7cSu6SYqZ2e8ySVcS8Cjco-Ep3TBuH3tNzr-tAJB7ubDAhuB8yZ5fY0Fxo8JPIMn4Bl5RsXQ39GXWhxXtiZXQg_KNGdbMxaStnQ-mmOqdQ3mJ0EaIHJdr7aaQRRzM_CAETOwkrQqC0dBnvWtomfy5BoY7ATLoykM7c6E02QLUIWnGts086NQ4XC8cChbSTgbt0UQhf6ZxzwEEf_71xRiF8n9OTeDLqupr_jF9mswwcnUdO6lebxa4oYAPBaxotdegpr8DQcPxYnq47VVEAFtDRax54tRKu_7uF0CtfmsJlNIv1j6halJLAThLunW3bWrnC3C8P2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در فهرست تحریمی جدید آمریکا نام ۲۷ شرکت هواپیمایی مسافربری به چشم می‌خورد  وزیر خزانه‌داری آمریکا در بیانیه‌ای:
🔹
اجازه بدهید این یک هشدار برای کسانی باشد که با بقیه شرکت‌های هواپیمایی ایران کار می‌کنند: شما در معرض خطر قطع شدن از نظام مالی دنیا قرار دارید./…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/688232" target="_blank">📅 18:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688231">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUnVmuHKWCVabwnBrMAO1FPOYRdbPzVXTWJ30XHpMgrLv5T4vTf9O8pxhUiD8CUEy0Fxpo5M6Vszc_UEWq3Xb0WPIY-nwTY5xhe3DIyXECIwGpPXK8_iVkNNMogFcrWkIxMXDpCX2wTfDCnpQgvEUeDo5yGZz1XhlX8w5z3Z-HaHzy3KiXP1K5edjiqhxjmo-qbCVlstzZTjIwCtBkb3PltnUHGY8ng_yTSeozSDjvOJn3fcFEGdAs9A3LcOPZSR24WnCyth-v4kgaV-uY9KN2PTrXjd4gyRbPUTN89ZlIGSvYfOOB6zh4cQ31xVSjkE3F4nG3y-MStv5N7cWUa2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حمل‌ونقل عمومی در کلان‌شهرها ناکارآمد است؟
🔸
در این نظرسنجی بیش از ۲۳ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۸، بله ۲۴ و تلگرام حدود ۱۸ درصد بوده است.
🔸
حدود ۳۳ درصد شرکت‌کنندگان ضعف مدیریت و زمان‌بندی و بیش از ۲۵ درصد هم فرسودگی ناوگان را از علل مهم ناکارآمدی حمل‌ونقل عمومی در کلان‌شهرها می‌دانند.
🔸
ناکارآمدی حمل‌ونقل عمومی در کلان‌شهرها معمولاً حاصل مجموعه‌ای از چالش‌های مدیریتی، زیرساختی و عملیاتی است که موجب کاهش کیفیت خدمات و افزایش زمان و هزینه سفر شهروندان می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/688231" target="_blank">📅 18:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688230">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ترامپ خطاب به ایران: آنها دیگر هیچ شانسی برای دستیابی به سلاح هسته‌ای ندارند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/688230" target="_blank">📅 18:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688229">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65032f5532.mp4?token=fsn6TvF7_5HcupPzMv_AvcHSH57Yqc90y_OdcnuyBpUHXzyXWjV0nBB-Q7fvGifrb02q5aAjxNuUd_5X3j3m0OMNSxvt6o1P5LN-Xq4R2gptbo5f-ZASKk-wmSX1_nJCzo4I_lO8xT5x_FHUmGT62FYG3usu57dLWqahOSkviZCDInml7H0pYjS_z_17pE_Ic_H5TtaPCXLdJ_zfKYC6Jz7lJrEdQK_nqf6Q1w61XoCausx8H4tbp1dugy0ko8_VLP6uzbFaNkpzbYChhIq0wED279CNBym8bqkX71cKqvaE_XlSjwOeSnSu_JgwsYxPBzk3CHIrIIh1FzTigEkrMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65032f5532.mp4?token=fsn6TvF7_5HcupPzMv_AvcHSH57Yqc90y_OdcnuyBpUHXzyXWjV0nBB-Q7fvGifrb02q5aAjxNuUd_5X3j3m0OMNSxvt6o1P5LN-Xq4R2gptbo5f-ZASKk-wmSX1_nJCzo4I_lO8xT5x_FHUmGT62FYG3usu57dLWqahOSkviZCDInml7H0pYjS_z_17pE_Ic_H5TtaPCXLdJ_zfKYC6Jz7lJrEdQK_nqf6Q1w61XoCausx8H4tbp1dugy0ko8_VLP6uzbFaNkpzbYChhIq0wED279CNBym8bqkX71cKqvaE_XlSjwOeSnSu_JgwsYxPBzk3CHIrIIh1FzTigEkrMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ خطاب به ایران: آنها دیگر هیچ شانسی برای دستیابی به سلاح هسته‌ای ندارند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/688229" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688228">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBN3XvaQik00tqnKV3c_XvyPUGg-INjro9EcB3Moh5ziH6gwppcugKrp1rNtQ4qsPUOjNNpZnA9PeNIL8gYbkoCHO-JtkT18s35ybnsghM10E9M10-WTRGsAeJ1OaJUj4nIE_-sM04h1QnvqiThpw-f_yjmXgY18kcVYpCbH3PoKwT7ob8v4fS6qf362wGE4Yk77V8zntF5iJnqihKZbmy_4oayE4H3ILh1wh6nplCnqqagu1yeFJLxdSRGzX4C6DY7Lltraf__zTHh4Yc89Rv8ttHLAMiSxHsW-6OyZoR8IiFZZ_wH7c0xzpddhbGXDHvYJmfNheANiaSFbsMOH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور «مسی» در بین نامزدهای بهترین بازیکن سال فوتبال مردان از سوی «فرانس فوتبال» برای مراسم توپ طلا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/688228" target="_blank">📅 18:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688227">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
آنچه باید بدانید؛ Dive‑LD؛ زیردریایی هوشمند و بدون‌سرنشین آمریکا
🔹
زهپاد، Dive‑LD یک وسیله زیرسطحی خودکار بزرگ یا Large-Displacement AUV است که ابتدا توسط شرکت Dive Technologies ساخته شد و پس از خرید این شرکت، توسعه آن در مجموعه Anduril Industries ادامه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/688227" target="_blank">📅 18:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688226">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3d8b7e68.mp4?token=n3KKbSepkzG4AtXePGD5FuGJ4h31fjXxd4Sp_YO-yBns-EZwAWAP-G03z1PdbMpty7q92hY3Pa3umhZoWeUBZpVHF6P3WBhZLsul73k6CeHhDDo3DYkbTPHxgEPRKzYb7xM6BfY1j7weV16zW_1NU6HG8luj-wHKHQ-mKXoO8GqcIpQ_4_oefWPcLeM4BmwUJkUBanvvpnwOzMng7TjpvNi5GFUAl9VQa6oKs6FVXfJq5aYSa02X3vFrwfGbvH6FO3ExWA3FzIP_RDG03YLL-3PCafI9IBch4qmuqj1Zy4LVpuwJ0BrrJgOJ-QRFmrnbEtv_w60-pO59a0Ru00uuYqSYW1TBbJ89NRzLroD9DLSxpvOCGgM4QoDnINm7COvhOnufD2K3QCQN7nr8kI8xqkqYztq1xonQtLapdMJ1suwGRdjvNk-wQ89H3hxv360PiZSbul_6TxvlQ3ELOXeG03-q3-p6VCSIptycl0_TR8gA8MNgikuSaJlX6uOmk2oBG4-dpWrtPzWY-v9oi_Atfnj-7JbuuChfeoqy3VbD-JgzdO8sMrZuPz8XhwFFJPQIpXFbx2-CpcdGD8jM4TGrntF2jVoZZVrC3Yh-7fIUltUZaoxUuo2yYjZw-OBQfoujTpDrjGeOHaU4DLx4IXg2Hz3zmVdC_ufNlIiG05DceoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3d8b7e68.mp4?token=n3KKbSepkzG4AtXePGD5FuGJ4h31fjXxd4Sp_YO-yBns-EZwAWAP-G03z1PdbMpty7q92hY3Pa3umhZoWeUBZpVHF6P3WBhZLsul73k6CeHhDDo3DYkbTPHxgEPRKzYb7xM6BfY1j7weV16zW_1NU6HG8luj-wHKHQ-mKXoO8GqcIpQ_4_oefWPcLeM4BmwUJkUBanvvpnwOzMng7TjpvNi5GFUAl9VQa6oKs6FVXfJq5aYSa02X3vFrwfGbvH6FO3ExWA3FzIP_RDG03YLL-3PCafI9IBch4qmuqj1Zy4LVpuwJ0BrrJgOJ-QRFmrnbEtv_w60-pO59a0Ru00uuYqSYW1TBbJ89NRzLroD9DLSxpvOCGgM4QoDnINm7COvhOnufD2K3QCQN7nr8kI8xqkqYztq1xonQtLapdMJ1suwGRdjvNk-wQ89H3hxv360PiZSbul_6TxvlQ3ELOXeG03-q3-p6VCSIptycl0_TR8gA8MNgikuSaJlX6uOmk2oBG4-dpWrtPzWY-v9oi_Atfnj-7JbuuChfeoqy3VbD-JgzdO8sMrZuPz8XhwFFJPQIpXFbx2-CpcdGD8jM4TGrntF2jVoZZVrC3Yh-7fIUltUZaoxUuo2yYjZw-OBQfoujTpDrjGeOHaU4DLx4IXg2Hz3zmVdC_ufNlIiG05DceoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چجوری حافظه قوی‌تر داشته باشیم
؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/688226" target="_blank">📅 18:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688225">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE_-D0ehDU5z-K1FKCR6cs9TeBW7dNO0Mf3eXGz0lbfuvp98-sFE6_n-ghF7qWpJPEGRiim3EzcMhCPZ-pJzD5nitz1QkJ8qgn4C-gS3ynYur7tSQN1knEehsvlffnpGqk1JHxGvWA6oxC0x5QUsosqp6n0uetuBmtoD9FGlaZpt59gP4XHg9ntkM1NOsR7CgZSLgOpvhSd_jVY0KmRN0WiWinq-CWxYnmvHTg3pLwUhGCWtksi8Wfe7YKBJrR3952BKU1wLe_jKTK1OcM4Lk4URIUkkHJ-VP54dh0nis1t0YjxTYHNEHdRdhiV5gVX9qkun0MDqZ9E9cFfDW8swXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا طلا در بازار، قیمت‌های مختلف دارد؟
🔹
دنیای اقتصاد در گزارشی به بررسی ماجرای اختلاف قیمت طلا در بسترهای مختلف نوشت: حجم معاملات، میزان عرضه و تقاضا، نقدشوندگی، موجودی فروشندگان، هزینه‌های معامله و حتی انتظارات فعالان بازار می‌تواند برای یک دارایی مشابه، قیمت‌های متفاوتی ایجاد کند.
🔹
در روزهای پرنوسان، این اختلاف بیشتر دیده می‌شود؛ چون هر بازار با سرعت متفاوتی به تغییرات واکنش نشان می‌دهد. به همین دلیل، مقایسه صرفِ قیمت‌ها بدون توجه به شرایط هر بازار، تصویر کاملی از واقعیت ارائه نمی‌دهد.
🔹
بازارهای آنلاین، یک تابلوی واحد با یک قیمت واحد نیستند؛ هر کدام بر اساس شرایط معاملاتی خود قیمت را شکل می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/688225" target="_blank">📅 18:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688224">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
خزانه‌داری آمریکا: مجوز موقت برای صادرات مجدد برخی هواپیماهای مسافربری به ایران را به طور نامحدود به حالت تعلیق درآوردیم  دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری:
🔹
۳۶ نهاد و موسسه را به دلیل حمایت از بخش هوانوردی ایران تحریم کرده است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/688224" target="_blank">📅 18:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688223">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/688223" target="_blank">📅 18:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688222">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/688222" target="_blank">📅 18:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688221">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-5Hi_ZznZar8uqiTlJNAXluatr6AYovEWKRugzArkRh7CWj_rIBZsoijlWWh7m_ugp16MlaeW81loycFagSdsc5q1wFAJjmza9nepQy3OeoVYPoRWphpAd7na9sW9o-yUBLfeN_Z6BWlaCxMVm4Jevk0qpxaA4VNKmtcTvuP_8DjoZdTge6kIaAjygzSi5qF5dULYTXGuf3tnaOtIpbGVrIFuTWMbt3vKoeDGqSSGusEmfVsJeMZ39IAxc3nm5RTxUQXC6nXXBNiIQgYjtxsO7WUoJVlGJ18esc2jSBp5XrHNq7SrJEuAZVVHV06fjrFZ3e-vtOnRCf_ANFDQ5ovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز
نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز طی یک اقدام پیچیده اشراف اطلاعاتی و عملیاتی در سحرگاه امروز به دام انداختند.
🔹
این زیر سطحی هوشمند از جدیدترین تکنولوژی در حوزه زیر سطحی در دنیا برخور دار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش تروریست آمریکا تحویل شده است.
🔹
گفتنی است این زیر سطحی  اکنون به غنیمت گرفته شده و طی ساعات دیگر تصاویری از آن منتشر خواهد شد.
وما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/688221" target="_blank">📅 18:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688220">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
توافق ایران و روسیه برای تقویت همکاری‌های مالی و تجاری
وزیر اقتصاد:
🔹
در سفر به روسیه درباره همکاری‌های مالی و ارزی، تأمین مواد اولیه، تکمیل کریدورهای تجاری و زیرساخت‌های لجستیکی توافق و رایزنی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/688220" target="_blank">📅 18:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688219">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
وزارت خزانه داری دولت تروریستی آمریکا در ادامه اقدامات خصمانه علیه ایران از اعمال تحریم‌های جدید علیه ایران خبر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/688219" target="_blank">📅 18:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688218">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTLPey3QAN8K22ZjoVbOHIiZIjaTgDJX-wWIv_srCvcD0vJtGPpM4kWZ4obnZ7GtFXm-eVRvOcSKq0ZzcVA-9CZ1A5kW12YTUgKjxqO_CXDilbC1XyHSrI0pstf3uhA3dckTTD50wBf74qXC4xnjaGWRfKQRdTXfyNnMp3Cs15BZdVCPp_eSYvPgUHMiXvQ887_T1KLTa4CFl2ppc3hJvG1NzWUOh7_FE2edRixtqgS3L0u6avG0qlEtCr8jRkuGCylrne1-AKDcTTnF0cUcBt84ap_QFD84e_Svf499vFWLsfM6fPd5wLrO25j6U3q3hF76sjBeYco-IyWsu1n0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور «مسی» در بین نامزدهای بهترین بازیکن سال فوتبال مردان از سوی «فرانس فوتبال» برای مراسم توپ طلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/688218" target="_blank">📅 18:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688217">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09e5fd2e2.mp4?token=DBDqs_xeGudilZiaB2phAZDQkVF0eOZWXgcucKPp-mgBZiY7_F_sZIo1slV_TxZaSwTX0FOXMmXFzMH-cg9UH-YB4j6lxAbyFGzf1WcA0V4K-LP2MncCaAYYdGRbIDmiX5S_s0NgGULV34WGGh-xxuZVYAE2wa_oPPGk03P254G-RoNYeWImOz0Rr7AK2oxA7SAO5vTmO-uZ6ywQ3mwabnrF7VSrPqs5F_ypmPeX0Tgqj5slSp-h_qLAPjbpM4JGkzlkZ_2DVchgOEocK1bnCF4KdIyoS_b4dJDxL6Bp8NkZ56fZMpPZPiHOeeml4d4TBpgNyW7AQ7IAfujlblBtOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09e5fd2e2.mp4?token=DBDqs_xeGudilZiaB2phAZDQkVF0eOZWXgcucKPp-mgBZiY7_F_sZIo1slV_TxZaSwTX0FOXMmXFzMH-cg9UH-YB4j6lxAbyFGzf1WcA0V4K-LP2MncCaAYYdGRbIDmiX5S_s0NgGULV34WGGh-xxuZVYAE2wa_oPPGk03P254G-RoNYeWImOz0Rr7AK2oxA7SAO5vTmO-uZ6ywQ3mwabnrF7VSrPqs5F_ypmPeX0Tgqj5slSp-h_qLAPjbpM4JGkzlkZ_2DVchgOEocK1bnCF4KdIyoS_b4dJDxL6Bp8NkZ56fZMpPZPiHOeeml4d4TBpgNyW7AQ7IAfujlblBtOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقاله‌نویسی با کمک این پنج ابزار هوش مصنوعی می‌تونه خیلی راحت‌تر بشه! #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/688217" target="_blank">📅 18:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688215">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IH5yvRNoGpX_CjOXDCUqG0h7pa6ODtNPRADmEtw3FoKUPL-HuUNRg3Cdme0nELN_IQYbQJJG-hjDOtrIi94NNtPPY1nKXUXeNJjsLn8wW775x1O0iwzK0CAIA2YsHCCohc6OfOYPQxMNtQDaHzS6J6iM72XgQ7jMt-27Ck1gz50ByloLn-6abmefwwmDDzJXIifem7zcx_Us4UOlzbl0xcpLL_RgXN5AtPUyfUyk76-Ruz0Y2mmGEijN1P4tDlLPW6KX5wx96FpQRxILSe7zNBAzZpY69QF0N7JPIppCbBOm--fG63dDkYLGjDiVBxZJsqmGRQWOIu7OGcyIo3Wu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/688215" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688213">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
وزارت خزانه داری دولت تروریستی آمریکا در ادامه اقدامات خصمانه علیه ایران از اعمال تحریم‌های جدید علیه ایران خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/688213" target="_blank">📅 17:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688212">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c404bd4f3b.mp4?token=kCsCRWLs6Uy2aDp2ZHhxxbHute8eyXBhfhjA-_ni8YIQKcLXLQmsfMmYiyYIIU7dBJn5mQeBsCSGIzBvsrpZBDkopZFTTCFEz28o1Ryj3gj9ZjOqqE4t4-GvcWW7Z8WutfeYBGFC4MAQ-YWYPUa0qxto7uRFYBUeWdIuBG1o3MiR96lM8tkVyCRecepXWBTThDCf-PRIM0IVy05aWanFVxWzBwwTRt9wlo3KC0bawNgUO5J5XvmcEJpt9_bsADseJ6KEFASBLJ7ESJsdmOgUif3tUwUDHE-hzG2IUiFSGyOlUs9CNcy8bwFS-xwAxaF1cPsMv_jpdFmopYaX5897E4tScLmtqDuwhzXKk7Bw8HQuk4wEWfpaJgZtfhvK04jhV-c1sHA5JuKCp9MCFP4xmcMn7LBX1VGo-htq2NdLerKdf2y6LdTYgcVkIdX1m5nnRGTngfAoPzzJIUQ1K6xxbqZW-NbMNhoactyBQVhX6PquA2tNkphJIoRZPD4gyyMHIJBA5fQM_1CnZIEK3qxhar6AWD7pfpeRthpIwCSChUWQ2eKwH8QoBOrsu1z76nQgMKsXiDD8FNaVsnJVCIPXZ2Rjh2r1WrAA4DXB7Tvnft46eFeOoszTW_BycxectF_z2o-0Ic7X8SFFK2AtzruryQ2kIQOvZo3zA9ut2T7TJK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c404bd4f3b.mp4?token=kCsCRWLs6Uy2aDp2ZHhxxbHute8eyXBhfhjA-_ni8YIQKcLXLQmsfMmYiyYIIU7dBJn5mQeBsCSGIzBvsrpZBDkopZFTTCFEz28o1Ryj3gj9ZjOqqE4t4-GvcWW7Z8WutfeYBGFC4MAQ-YWYPUa0qxto7uRFYBUeWdIuBG1o3MiR96lM8tkVyCRecepXWBTThDCf-PRIM0IVy05aWanFVxWzBwwTRt9wlo3KC0bawNgUO5J5XvmcEJpt9_bsADseJ6KEFASBLJ7ESJsdmOgUif3tUwUDHE-hzG2IUiFSGyOlUs9CNcy8bwFS-xwAxaF1cPsMv_jpdFmopYaX5897E4tScLmtqDuwhzXKk7Bw8HQuk4wEWfpaJgZtfhvK04jhV-c1sHA5JuKCp9MCFP4xmcMn7LBX1VGo-htq2NdLerKdf2y6LdTYgcVkIdX1m5nnRGTngfAoPzzJIUQ1K6xxbqZW-NbMNhoactyBQVhX6PquA2tNkphJIoRZPD4gyyMHIJBA5fQM_1CnZIEK3qxhar6AWD7pfpeRthpIwCSChUWQ2eKwH8QoBOrsu1z76nQgMKsXiDD8FNaVsnJVCIPXZ2Rjh2r1WrAA4DXB7Tvnft46eFeOoszTW_BycxectF_z2o-0Ic7X8SFFK2AtzruryQ2kIQOvZo3zA9ut2T7TJK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشورهای خلیج فارس بر سر نحوه مواجهه با ایران دچار دودستگی شده‌اند
دکتر گاردونیو، تحلیلگر و استاد روابط بین‌الملل دانشگاه UNAM در
#گفتگو
با خبرفوری:
🔹
عمان و قطر به دنبال گفت‌وگو با ایران هستند، در حالی که برخی دیگر از کشورهای خلیج فارس به اسرائیل نزدیک‌تر شده‌اند، کشورهای منطقه نگران گرفتار شدن در میانه تنش و درگیری میان ایران و اسرائیل هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/688212" target="_blank">📅 17:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688211">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
رسانه‌های عربی از شنیده شدن صدای سه انفجار در تنگه هرمز خبر می‌دهند/ صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/688211" target="_blank">📅 17:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688210">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
۵ محل هزینه‌کرد درآمدهای تنگه هرمز مشخص شد
سخنگوی کمیسیون امنیت ملی:
🔹
درآمدهای حاصل از اجرای طرح مدیریت راهبردی تنگه هرمز، ۱۰۰ درصد برای کالابرگ و معیشت مردم، تقویت دفاعی و زیرساختی کشور، استان‌های درگیر جنگ و جزایر راهبردی، پدافند هوایی و معیشت نیروهای مسلح اختصاص می‌یابد./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/688210" target="_blank">📅 17:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688209">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/688209" target="_blank">📅 17:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688208">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
پرداخت خسارت اثاثیۀ منزل به آسیب‌دیدگان جنگ از شنبه
رئیس کل بیمه مرکزی:
🔹
با توجه به اتمام کارشناسی و ارزیابی خسارت حادثه‌دیدگان جنگ ۱۲ روزه و جنگ رمضان، پرداخت خسارت از شنبه توسط شرکت بیمه ایران آغاز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/688208" target="_blank">📅 17:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688206">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06f962ce1.mp4?token=ehgqrWmWyp0JVFEdn-ASh8HinHxfn6Tj9SiUNt3gYdIoT7eNmiGRiYPcQSkeMVbtEaTRLgb8SB77qlUMn1YMWb0RtGF4NOJJ9zOCZtHwIotFW9_kFrdMhCYtlixhM02iO5vIwmw4X9wsJdK9p4lLXThYFslioejf7l1_o9kNm5fHlu7x3J_kXSbPt4DQuRHaDVr8CBqH4hQqIU_ha1VJf7P9ZInDNvwsnwUgKcBPtHMZpWFYJuqFdKiGzo7Qen_LMCLEdUmSco0fk6PrGoa_ai8UB1PQEFZpUoRAsCMKXjXw0GKf6j4gOU0wJzGHllaP6XQqwesoMGaSJcAq8-RmRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06f962ce1.mp4?token=ehgqrWmWyp0JVFEdn-ASh8HinHxfn6Tj9SiUNt3gYdIoT7eNmiGRiYPcQSkeMVbtEaTRLgb8SB77qlUMn1YMWb0RtGF4NOJJ9zOCZtHwIotFW9_kFrdMhCYtlixhM02iO5vIwmw4X9wsJdK9p4lLXThYFslioejf7l1_o9kNm5fHlu7x3J_kXSbPt4DQuRHaDVr8CBqH4hQqIU_ha1VJf7P9ZInDNvwsnwUgKcBPtHMZpWFYJuqFdKiGzo7Qen_LMCLEdUmSco0fk6PrGoa_ai8UB1PQEFZpUoRAsCMKXjXw0GKf6j4gOU0wJzGHllaP6XQqwesoMGaSJcAq8-RmRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش شدید باران و جاری شدن سیلاب در متل قو  #اخبار_مازندران در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/688206" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688205">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbdab0b12.mp4?token=b2LHm1d-P1FzUHDbWGZJKRAXeNs1Cq3K5YzSpMjGyuADooVbKKPI1h4AwCrHBrL3q-TngOFkSDCcjmDZhxXN5FgXiUAFXRoXo5cweRR86cmY86_iZHNOvQGwqttsrIFrwHL3Gxengh0zwveGxudG8JKLi4FGvyJNH3-r0w_WxtFWY0I2h8celBDdpJUGi5f4A2aKseqsZQNWRlcUmSooS4WMpmWkOiLWtZqCb3wF7GMBYg5_KvTFBm1_FZiHbHo8mjFxk7U1BWUuGmqyaf2uplK18XjPrwr8iDPtuuipxxglq9iY2dB_YHfYtjTY4slvyup-sQVNASs8vlg4cj0J3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbdab0b12.mp4?token=b2LHm1d-P1FzUHDbWGZJKRAXeNs1Cq3K5YzSpMjGyuADooVbKKPI1h4AwCrHBrL3q-TngOFkSDCcjmDZhxXN5FgXiUAFXRoXo5cweRR86cmY86_iZHNOvQGwqttsrIFrwHL3Gxengh0zwveGxudG8JKLi4FGvyJNH3-r0w_WxtFWY0I2h8celBDdpJUGi5f4A2aKseqsZQNWRlcUmSooS4WMpmWkOiLWtZqCb3wF7GMBYg5_KvTFBm1_FZiHbHo8mjFxk7U1BWUuGmqyaf2uplK18XjPrwr8iDPtuuipxxglq9iY2dB_YHfYtjTY4slvyup-sQVNASs8vlg4cj0J3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیائومی یک کراس‌اور هیبریدی را به خانه‌ای متحرک تبدیل کرد؛ با چادر سقفی برقی، صندلی‌های عقب تخت‌شو، نورپردازی محیطی و کف گرم‌شونده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/688205" target="_blank">📅 17:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688204">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان به نقل از یک مقام آمریکایی: پایگاه سیا در عربستان بر اثر حمله ایران عملاً منهدم شده و مقام‌های نظامی و اطلاعاتی آمریکا درباره کاهش نیروها و تأسیسات این کشور در منطقه گفت‌وگو کرده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/688204" target="_blank">📅 17:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688203">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86665a0b71.mp4?token=S5qubseNa4wGisj9uuu69oK8BryimbHUCtM4UzK1-gfqeIxwKGW-XQ30WhgvcqVeMj08hQHUo6CZe_M-YFVo9-Ms0ntor3pXev3M414YpJDonliPYJ9P2ZmucBbq9ep96DpZI2rNQMpfXPEFXN4RhVNRprFJOYUoKyH1fDj4fqylyi0LSmI5717lKCH-nnJOr5a9xG_-uGLATFcsS33lBWS_frx2ISKAyb5OktKji3WIxQTINSOvMVlFavsXAqjKA0YctORqSVHWkS_6-FnjAHS-OLupimvlRyuU_7nk0oFbTtg-ANDndl5owg2ANJg7r2x4SyJ4U6R924eOPD_bNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86665a0b71.mp4?token=S5qubseNa4wGisj9uuu69oK8BryimbHUCtM4UzK1-gfqeIxwKGW-XQ30WhgvcqVeMj08hQHUo6CZe_M-YFVo9-Ms0ntor3pXev3M414YpJDonliPYJ9P2ZmucBbq9ep96DpZI2rNQMpfXPEFXN4RhVNRprFJOYUoKyH1fDj4fqylyi0LSmI5717lKCH-nnJOr5a9xG_-uGLATFcsS33lBWS_frx2ISKAyb5OktKji3WIxQTINSOvMVlFavsXAqjKA0YctORqSVHWkS_6-FnjAHS-OLupimvlRyuU_7nk0oFbTtg-ANDndl5owg2ANJg7r2x4SyJ4U6R924eOPD_bNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده لاشه یک گونه نهنگ در سواحل بندرعباس
اداره محیط زیست هرمزگان:
🔹
علت مرگ این نهنگ، آلودگی نفتی یا گیر افتادن در تور و ادوات ماهیگیری اعلام شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/688203" target="_blank">📅 17:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688202">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نوبت دوم مزایده جذاب املاک بنیاد
با 30 درصد پیش پرداخت و اقساط بلندمدت
مشاهده لیست املاک:
https://mfamlak.ir
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/688202" target="_blank">📅 17:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688201">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
معاون‌اول رئیس‌جمهور: افزایش مبلغ کالابرگ به‌زودی اجرایی می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/688201" target="_blank">📅 16:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688197">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApwIRUCzOZnyPqbgHvpa8zackAVsLWLwkcLirNn2L4xo0kXtA6CwdonRbVt1DCT6gTGp1G4moTpuF0oDzbx1XD1RONm6RxAOeDfXaOQXGHz9d6o1-gH-qhg6NlOwSzBmW-i3MreuN_8U8QBPv8iM38lyAuOlcESt2SxU6ab9oFfpZLaKUJeyKLL7I9Ec6n6iFOFab0pxSqxTcVhgMbKbAAG5ODolPCdmnXJ8uCU-3zsh45vlt4Fnc3vHpUm-PCAztQx8WXbmz3YZ6n3TU6OaxMd7fTP1hraKZSbPLW4lTmegZ7meLuCI_KHDevHVfcwvLu0k9zi_tMJbBbzjBD2QYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bW5dnZQ1ae6YY-azzGEGsDyfozD89Qc7LxMcDWvmUKHjRzfe6dmhk_gN8z0zRwp0monm-xJzX3Md7_KxtwOfxmXzKE_EryH5KlB8PqHRR83gFEmZax5fhepcGXMkWxV2jk4qhr4Kh3ToRqteqNkltU-7k6XXIVNWHUWdV7un4uSao7CjVh5_8YGrkPVR8e2zP_Df5Vj7yQ_-TZ-fqwoFkf-mDtL1sQmDgReUUV1P5gwjOiGtlI99KtU5Tur0gwyy2UtdM7JDCuQAhK18mwHMvZvvcKFHeBEK_UDNYVGqd0YthP4Vh1wfMRs6chCwmvvGp5TzAz64T8wL8FcoV8dW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iB2P25ocfwEo0DskWO-1N-gOnRuiz46IlfbeT_PDiynlxhgZB3mauRaqWkUmEA8RdP-4t9LTd3dPAUQUpIybXafcxHxm2jzz0LtADoddWBmR7NeZimMuBjDw7xBqJ79i8Rez8AJLGuF4i4VQjgXqX8XBUk9WQ__40D1h5izIHIhVijI4V5Ob6Mcs71k6Gib0TPqIqBQOiMauQ00qTj3bf_DGVpMMWWNgI9w8LMaZTAe3CFevMxpOQnm5fHKIv962w6nJzQvsjjUnIsszSjn9r2bXvqhRWAJl2l1S1ipNxxzOFBl3D5q-YoF7b8YiK2_hoqsSKgFkk3WiyviqAICXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9Qz_F-cCz-jBqqmUN7AFnmE6JRSajtSbJE-9Si29EYOvNYVIuNXNxZRXXuYw-z3GbmTZ_muF6L3eL-9jkIPsP01wIIsroHpHTvFPnfqqQhcS_uH8H_a4N9Loolnurtr7M0zmFlGYOTelsTv0VUWcx0LjoyrIiZtlutPtnOjpqCl_NZ_YKs_I_TEu9bfcfvVBxN_Q5cidYrPFXK6PQRabnU0GbggcHRX5uiQniGevp6hwZlbQNr0LDH2XJEvutTUs5_HlocrZvm6xXw7yZW3TI0SxQWi6EtHODKMYOWL1WHi44eN9nKZ5k-1foMc4cKn4TpUWpLyAqiPccUhzNIS4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هرپولی که در حساب‌تونه برای ترید کردن مناسب نیست، قبل ترید حتما این نکات رو در نظر بگیرید  #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/688197" target="_blank">📅 16:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688196">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHt55ucWDOEGv6GAiY0NujJ1phBcCVPNoZFRv1CgtfRQYYuUYGBZVpQBXE85EKx94cjUGYEbsuspYZmWk2eSM_kJkcrSMrhRkoy7W7xFOwfIj34brRc0d7jvVQxU9a3c0heIkJv82lAAJbuuKFVhyb4Gias6XHCIIlfxCjjgW4dAp-e9M5Jmrg5T-pLeXt238fub7QqdtIqGJwiKV8tkc_0KA4LUanWvY20RpiM_V8V-gNz2WyiMoa4TT7njm2jbgIgvr4kuLafxblIL9dvExh-_Ms8UxLa_Wo4LteIc8LcFcfrMg5lmqRxETKA9P9d00C3q_kEWOTHgLNJ-VT-Fpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلون میزراحی: تصور «اسرائیلی متفاوت» یک سراب است
آلون میزراحی، تحلیلگر سیاسی و فعال رسانه‌ای اسرائیلی-آمریکایی:
🔹
تصور «اسرائیلی متفاوت» یک سراب و ترفند تبلیغاتی است و اوضاع به‌تدریج و برگشت‌ناپذیر بدتر خواهد شد تا در نهایت به پایان برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/688196" target="_blank">📅 16:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688195">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
شکار یک پهپاد آمریکایی بر فراز تنگهٔ هرمز
🔹
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق ارتش جمهوری اسلامی ایران شناسایی شد و هدف قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/688195" target="_blank">📅 16:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688194">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ایران: آمریکا و رژیم صهیونیستی اساسنامه آژانس اتمی و قواعد ایمنی هسته‌ای را بمباران کردند
🔹
جمهوری اسلامی ایران در نشست شورای حکام آژانس بین‌المللی انرژی اتمی با محکوم کردن تجاوز آمریکا و رژیم صهیونیستی به تأسیسات هسته‌ای صلح‌آمیز و تحت پادمان کشورمان تأکید…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/688194" target="_blank">📅 16:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688193">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJCumezvQEDVVMqN7HN7lwWevkSr6DKZA7jZMSU0gQkTsiNiU9_Ii6WV69eJNyY9bV7DTFL9MDqMKuHlxBHUleW8IIfSoIoTfMoxsmVEN2wkv488fqplVOKLyPzc7OUE-bnv164Ui7_Cuo98ZULAmKKjX8ms3nUb8OE625ZANDVNqAkp0uzO73UUKuEPYv_zREhnwoBi1jvRlpGCjZ_9Tk6xWqREAdac5F2i1qm9qdRbhV-eENSiuhlRmg9eECnHqT1zqUGCHc3Rj8jzuCgsm5HRe9_UbVrAXUUOsDRVtYT6U_z-2fRY_2h0rqDmaRTJWe8Np-azRuo3BInmAGxNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بن گویر: من از نخست‌وزیر بنیامین نتانیاهو می‌خواهم علیه بریتانیا تحریم‌هایی اعمال کند
🔹
وقت آن رسیده است که دولت اسرائیل به‌طور علنی سرزمین‌های آرژانتین را به رسمیت بشناسد؛ بریتانیایی‌ها آن را به‌زور و خشونت از مردم آرژانتین غصب کرده‌اند.
🔹
بریتانیایی‌ها تنها به اشغال این سرزمین بسنده نمی‌کنند، بلکه در آنجا عملیات حفاری نفت نیز انجام می‌دهند و پول مردم آرژانتین را به سرقت می‌برند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/688193" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688188">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rrq-dSKTrmEKTc4vnH8GQsMiEDXHuTDW8rzmHq7_5UUiYSr-4J9KxTeGg7cE6ZDQHSpY4qNo78FqlPgLIJdaJPc6rAG7BmEqGBxjKwo9z7XMQ6IsPQRYA49aJV9cuHBsAKzfXx6Q44bLPUlIuUFrUGDzUkZXTh2lOnNzpiezi9_YM84P7EPnkzmEBcR2JJmcpgl79SQZzTJYbL1DBTDHf8nf7d4D88OOxASpQaCnUHGfbNZI7a8kHJK-7M55Uj0bQoaOwEHiufIK5DHslhDf9gZyxQx04sbnwrvvmYxxjF1FiVrKlqCBJKD5sjSaucNKG1ffeobDnciMgCCxj_D9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2gF4bXQTNKFLnX1_UEtxmzSgNj0jwRuRre1tcnfIuA-RzKul9d4r4hixItDFc4sbrBYWgq9A-xrRGbqxAzvy_LS4euMEZTIuuuvKfYujOvPxHCsm904HaC4dK87T2efXYd2ZCp98v4QtNu8eD1gQV2Xvs__bbwp1nSsghHZyKNrSxOdqt40f1u8ePaHTwYZYptn-sb1bGJAOm1vpjMCj6DloVly2kwcDlXVxw8hfyfdBlr401iZhydgEFBdn5n9GK6D8NklgRHIHujzzAXwijqEaJrbXET1ZSV1Vqlgcpo0XLZSACNkXIQJuFleK-HXf-zMMr0-NRob1tVkW1fnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtMlu5Vqkl_SFY2XohT2isFQ01NsxALV5WBs7RYAj27GzweCf4m3yARnEztu2ulxOtJZeQfm7HZhK_-v2GnFLvQIuI_gdbgyjrievtAfZCzs_oAD_xI8whb6EYwAqJkzze2xL2yyrZ7JPWW3vI94S7VZNZOX3fbSgmzUISes2k7yNO13clyPDZZ4m4xouCLVG8bG5rOrqXX2v2xrRmRKSUOFBwWhiBrUpwqC97by0RQ8e31k1keN2M6djO0MnVZR907aPcqL8xd86BESnoIPBrbYQRvT1ffR_wRFl9qs9qxcnsCcwY3-xYlgAAyQoJBQQFK2VkHQ8Jig46gUCpdLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NaKi8ISQiFiMTRMNVrbFI0GdimxVPqZSJQBlzXo614hOGCOo-1Yq0lZ0UeLu2xC8O8lRpc1k_-9r8QsQI9q9GkDizZ1syaTi5Y6u1eK4uBixq6mHGqubF8ABECyrrIWdBzcDYT_lo_2dEwiu6z6Rnj2_W-6wEYzGD_01EfAkw4V5uVNL3zhi1ELjOSXWMBOadXb1tM1x-xXzMxSimCo017c4t2sF9hArOoO8j3mWEmIEmLMvs-e7VSA9tz-SWLAytCSaAIp-p4wGR_MiGVtYWCiizpNAc2_uPnPK2QeovEl_zPjyIjZcWiRw4c4Gna6PH9tVqL8dFhmIqCE9os7Qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZw0RQYNjcMkTQAZTnOteLmxhWHWlmQIt4dD-8vZrG5Xaf1DSwdvCQQeNmO6nOjQoIa81v_NVEnm7uUtQP8UODjJ5ACFfkJ2F3mPozROxAVmhwOBmlPFydz4N4GX9gCGGxz_d_yIpjckldu5azDGxWZyqdoepBwyWeHtxBtJFv_DKpqrMacryf494PKErDIr18Brtx-ovJ-i9hYyWh18-FBlD_Qk83Gy4P9Sj5ACp33SbcL3FnFzNsq1ZbSThyD0kGqYxE1NRq8bOR6dXXFCMxQZ_ANQe-Wl3d2TnH5KzoebktD-VWBYv4LeRKaxIDYLuceGLcx-yqibUAipkUtOLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند گروه غذایی مهم که باید در رژیم غذایی‌تون حتما داشته باشین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/688188" target="_blank">📅 15:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNgG6UgOUsvB-zmhnE3Zo4pf1_3j25FJ6NbxXITvTTizvZdg-2urxDnwZ2a3t763ip0ymfU883tAhKYmtllbTuVv1MZlXrjRa3eNM_yD21HjtOacdSV20BeOG3q-Qb_Db-Ik7ZGV88h4eYj8qdrCWKLIOMXj42UQAGvZMqE02A-dwFHeE8qRXeDXTKKHdxSL9hCjSkur-zQC0JVlzKShzxv_EkHwlsmZ3_MzURVrhs4zqsAD4ZlM1mfKTMcH_t3wgvA94LVgkL2ImZG8o4mPKvyN5kDXhYs-xu5QTLhE_EUAkyZZiRxE2u61kPLo5QuqB-EYjeOsjquCsixO0TwErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ، مارس ۲۰۲۶: «ما آن جنگ را بردیم.»
ترامپ، سپتامبر ۲۰۲۶: «ما در جنگ نیستیم.»
ترامپ، سپتامبر ۲۰۲۶: «ما باید آن جنگ را ببریم.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/688182" target="_blank">📅 15:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688180">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سی‌ان‌ان: خسارت ایران به پایگاه‌های آمریکا «سنگین و قابل‌توجه» بوده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/688180" target="_blank">📅 15:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688176">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/404dd357f1.mp4?token=FbgzJdin2ITAo56NI9dJlvwNUcycuAYqL5JtDLkjoTi5qntJncTDSSfGZnknaf_5YiLpp6xJ3ELiEgQggAPt52sXQ9HcLJ8betIbfUDH-5xXjbZW4GEmAPehMrRF38vz6chyrIX38Uus6yi2lgGLSCK-MRw08zFkVK03Ods0MOSLZkk9A1n9S67M04gfDGak59Wn-LY59zu1gfs-C5IF8EE2tugPLIpyxr6btSHvZz3dWcW3SXXHRmBA2yGfHZYJMMZ--FChP6GNYD2OCNv-AhWBP6kaNPDwi5Zhk3Fp74HfNsWHdnfSHNjbJHpCYyUvkql4XbynEKe_b5WVXa_8uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/404dd357f1.mp4?token=FbgzJdin2ITAo56NI9dJlvwNUcycuAYqL5JtDLkjoTi5qntJncTDSSfGZnknaf_5YiLpp6xJ3ELiEgQggAPt52sXQ9HcLJ8betIbfUDH-5xXjbZW4GEmAPehMrRF38vz6chyrIX38Uus6yi2lgGLSCK-MRw08zFkVK03Ods0MOSLZkk9A1n9S67M04gfDGak59Wn-LY59zu1gfs-C5IF8EE2tugPLIpyxr6btSHvZz3dWcW3SXXHRmBA2yGfHZYJMMZ--FChP6GNYD2OCNv-AhWBP6kaNPDwi5Zhk3Fp74HfNsWHdnfSHNjbJHpCYyUvkql4XbynEKe_b5WVXa_8uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل بی‌سابقه‌ و شدید در ناگویای ژاپن
🔹
سیلاب شدید در پی بارش بی‌سابقه باران، بخش‌هایی از ناگویای ژاپن را دربرگرفت و مقام‌های محلی هشدار سطح ۵، بالاترین سطح هشدار، صادر کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/688176" target="_blank">📅 15:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688175">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
قیمت بنزین در آلمان به بالاترین سطح در تاریخ رسید
🔹
متوسط قیمت هر لیتر بنزین به ۲.۲۱۵ یورو افزایش یافت که بالاترین قیمت در تاریخ آلمان است و رکورد قبلی ۲.۲۰۳ یورو در مارس ۲۰۲۲ را پشت سر گذاشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/688175" target="_blank">📅 15:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688174">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0abd22e45c.mp4?token=ExQsBorwma4SK35f3Bzt-4nSoJxnEUWiLkCyYjVhQMQJUJ_b0-4FBq0NKmPuED8VPayaZVlbwDfmDjAlNbGeVH9YMOKbZmJ9msFCZkjh-Qem7riJz3Mx_v3ZjaSTKGbpDeAAj9_Z5E98RNcWjEdi3sbWSOzxTRJ7SmVLpOv9q-juL-lX2RyflLm0fKto8LSJnQ_4gcVczDewJNzlDzRiXLc3EkpZuUYoQuj9VPf-R34MbhmdOPg6OA3OnLvN-URNwJNkayNzR2sRhHQVZH4zKU8DbWYCB4F3pXfM3LqrgKudgEZrh9iuv_Cae18Vi5D_Gm1h-NZPnDk8qDYOWf7OcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0abd22e45c.mp4?token=ExQsBorwma4SK35f3Bzt-4nSoJxnEUWiLkCyYjVhQMQJUJ_b0-4FBq0NKmPuED8VPayaZVlbwDfmDjAlNbGeVH9YMOKbZmJ9msFCZkjh-Qem7riJz3Mx_v3ZjaSTKGbpDeAAj9_Z5E98RNcWjEdi3sbWSOzxTRJ7SmVLpOv9q-juL-lX2RyflLm0fKto8LSJnQ_4gcVczDewJNzlDzRiXLc3EkpZuUYoQuj9VPf-R34MbhmdOPg6OA3OnLvN-URNwJNkayNzR2sRhHQVZH4zKU8DbWYCB4F3pXfM3LqrgKudgEZrh9iuv_Cae18Vi5D_Gm1h-NZPnDk8qDYOWf7OcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جغرافیا پر از تضادهای جذابه؛ چیزهایی که درست در نقطه مقابل هم قرار دارن، اما بدون هم شاید معنایی نداشته باشن #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/688174" target="_blank">📅 15:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
کانادا در واکنش به تعرفه‌های ترامپ، رسماً تعرفه‌های جدیدی تا سقف ۵۰٪ بر صدها محصول وارداتی از آمریکا اعمال کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/688173" target="_blank">📅 14:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff8f7f6820.mp4?token=B50ekW3Uhy126Kr6ShoissFnrX0iBNot-N6syLDsBQb6L5PB-gqLchEJIdoVCFs_v8SeKLDMVm2rWEugk5QplqAUj2HbgL2mYwEkASfd5po1AZkSKRha90flP13V1SJ9ilhUZNUMZG1L_4tpyy5ndj6wmJq2qJizBtbdmoBySk0LD8L76KM3nT1e_EBVdZIcnKnrHeDQgyjrRiJDxHdWccn17OfU0E2S58-qUW-pRGLy821w1dXvtde4PENjdTfwX1XiOtAaEIXxoAoA_GJDSy-4HMVgsoTzEejrcQv33KPtMAdHDrmKTausrCcNSMOOU2-9VUzupCJ6WbFuwW0Rrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff8f7f6820.mp4?token=B50ekW3Uhy126Kr6ShoissFnrX0iBNot-N6syLDsBQb6L5PB-gqLchEJIdoVCFs_v8SeKLDMVm2rWEugk5QplqAUj2HbgL2mYwEkASfd5po1AZkSKRha90flP13V1SJ9ilhUZNUMZG1L_4tpyy5ndj6wmJq2qJizBtbdmoBySk0LD8L76KM3nT1e_EBVdZIcnKnrHeDQgyjrRiJDxHdWccn17OfU0E2S58-qUW-pRGLy821w1dXvtde4PENjdTfwX1XiOtAaEIXxoAoA_GJDSy-4HMVgsoTzEejrcQv33KPtMAdHDrmKTausrCcNSMOOU2-9VUzupCJ6WbFuwW0Rrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: دشمن مخازن سوخت را زد تا سوخت به استان‌های شمالی کشور نرسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/688172" target="_blank">📅 14:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db201c6e1c.mp4?token=j6IkeJ1Stq7qH8-aDkCgKZm0H19L1pEb-vcmbzu9aW9lB0w0o3kBzgB_uGRVaOVHTjiTC1bpS_mmWPeHPS_gzqajulnW6lp4wcgzG2wONY93Q3qCGgWaYsImC-Xzq-SRmYL3koY5ZtaZla1QNLdRuD7FyhDdzQedUOTO14B2X001giUVWbOV97Q--Yj8PyIFiKG36rP0hfv0svHwP17lJjGk9cAGwuo51ztadGL45Oo3om1sBVTvA-io74Pw97tcZXrq8WQpJRXhQ1vARVx89MucmQJj03GtlNTDszoRdJ5Ef6EBKQvXOFgt4RPquCstnANQqeoh6yvBkE7jfgp8ETZIr96Jvr6-lXgaRFStKtMsJLQLn2x6JsttHq6GF9UcAuM51EVZFKSMJLd0PPiDiR44dOAvZvHrI_sBul5RL7jBbJMyF6uMRkxf--j2gzSVJBh3R1MBbYi6rQn9HUoR9uciyos6ysgap-2C_fF43stlTiOx-wUiIDhgKPvr84o0zNDyYsZv9WAczpGbPFmdonvoM3DUweKzFvnSbLEuPVeEWXlm0fmc_VPOc5SBDAIMXXBHAHjCG9lKQ0er1azXKF7o9GWXd3d8M8OyYJ7fZZAxAWhmw1PmrGZtfYxu_3oseggOuLOzNL9WrekZyKKUS8QlRTir0v2reSHA7dTa1w4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db201c6e1c.mp4?token=j6IkeJ1Stq7qH8-aDkCgKZm0H19L1pEb-vcmbzu9aW9lB0w0o3kBzgB_uGRVaOVHTjiTC1bpS_mmWPeHPS_gzqajulnW6lp4wcgzG2wONY93Q3qCGgWaYsImC-Xzq-SRmYL3koY5ZtaZla1QNLdRuD7FyhDdzQedUOTO14B2X001giUVWbOV97Q--Yj8PyIFiKG36rP0hfv0svHwP17lJjGk9cAGwuo51ztadGL45Oo3om1sBVTvA-io74Pw97tcZXrq8WQpJRXhQ1vARVx89MucmQJj03GtlNTDszoRdJ5Ef6EBKQvXOFgt4RPquCstnANQqeoh6yvBkE7jfgp8ETZIr96Jvr6-lXgaRFStKtMsJLQLn2x6JsttHq6GF9UcAuM51EVZFKSMJLd0PPiDiR44dOAvZvHrI_sBul5RL7jBbJMyF6uMRkxf--j2gzSVJBh3R1MBbYi6rQn9HUoR9uciyos6ysgap-2C_fF43stlTiOx-wUiIDhgKPvr84o0zNDyYsZv9WAczpGbPFmdonvoM3DUweKzFvnSbLEuPVeEWXlm0fmc_VPOc5SBDAIMXXBHAHjCG9lKQ0er1azXKF7o9GWXd3d8M8OyYJ7fZZAxAWhmw1PmrGZtfYxu_3oseggOuLOzNL9WrekZyKKUS8QlRTir0v2reSHA7dTa1w4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا چیزی که یک روز آرزومون بود، بعد از مدتی عادی می‌شه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/688171" target="_blank">📅 14:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40c923721.mp4?token=uKve8nQ-0pFjQqiYLygnZlqCU6xYphuUehFVGirnKQXP4T148H-5nnOcSWt3uELn1pSDtDMF49WJIvydZAi60BX-8XeZXe6msU60onMKn_zeuQcUPmrBAiZlmTs5dQTyKipWuU_lpj9GXfp-a7ztdDcjN8SgsgV0q8ipgUZPJYkSGNwZ68EmPl1luFRw2karWxQ7AuRTzB4YeqegyoWLFP2Da6yUuDsGnSn_aVhborvk0vvRs8I4-3Yjvdc0pCVUhiO4T7C686j6htcQ3-IUl4JR66Uu9k3aFQXeL1Gesxe2dXaCa0-a89LCNUAob7v_p1pzQGH0AOt9q_Ugj4KoOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40c923721.mp4?token=uKve8nQ-0pFjQqiYLygnZlqCU6xYphuUehFVGirnKQXP4T148H-5nnOcSWt3uELn1pSDtDMF49WJIvydZAi60BX-8XeZXe6msU60onMKn_zeuQcUPmrBAiZlmTs5dQTyKipWuU_lpj9GXfp-a7ztdDcjN8SgsgV0q8ipgUZPJYkSGNwZ68EmPl1luFRw2karWxQ7AuRTzB4YeqegyoWLFP2Da6yUuDsGnSn_aVhborvk0vvRs8I4-3Yjvdc0pCVUhiO4T7C686j6htcQ3-IUl4JR66Uu9k3aFQXeL1Gesxe2dXaCa0-a89LCNUAob7v_p1pzQGH0AOt9q_Ugj4KoOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات حامد کرزای، رییس جمهور پیشین افغانستان در خصوص آمریکا: از آمریکایی‌ها پرسیدم اگر موشک شما، کودکان افغانستانی رو بکشد؛ تروریسم است یا نه؟ گفتند: خیر
🔹
آمریکایی‌ها گفتند تروریسم یعنی زمانی که منافع آمریکا به خطر بیفتد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/688170" target="_blank">📅 14:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
وزارت خارجه قطر: به گفت‌وگوها برای پایان دادن به تنش‌ها در منطقه ادامه می‌دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/688169" target="_blank">📅 14:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
انگلیس مدعی گسترش محدودیت‌های اعمال‌ شده علیه ایران شد
🔹
دولت بریتانیا در راستای تشدید فشارها بر تهران، مدعی توسعه و اعمال تحریم‌ها و محدودیت‌های جدیدی شد که بخش‌های کلیدی خدمات مالی، تبادلات تجاری و صنایع هوانوردی ایران را هدف قرار می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/688168" target="_blank">📅 14:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688167">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8taVivsN2TGL7e94ojb_5XsU3J79FyY8qRhGsDUzfBvA5yZm2pSpyKWMdJtY759YTk9tNliuGzRbvVV9xe8k2yUNlOqrkks7AL_s1ar1mius0AEJqV6htdkp4WcC5mycC_wy06VfwBToYBZ7i1f2v2Z-WnLcblxANcQcmHnJ7WyIz1sT2CfDniA_IdYCqgtDEV2A8-kQFA0bXb5iwtL6PxhKQrBW-otDgygX0FAiC87ygDAzRKKKgiChlmYB8Gt4PE0hoHxD_eT59zbCxKDNuD0fKlGBEzMyk5_0R7CWaoKPBigyOvAncnKNSp01F4dH3ua9bbM9sTtk-_2T3An3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی از گروک پرسید: «ترامپ تا امروز چند بار در جنگ با ایران اعلام پیروزی کرده است؟»
🔹
گروک: ۶۶ بار!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/688167" target="_blank">📅 14:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688166">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd9ddb3a8f.mp4?token=uDBW5v91q-uR0NbR0KUOdW4djlbsZpO3gUrbWyabBJ7hcHls248-TqolyRhTFSl_VxHBurVUGlidBrxNd91TW2jcId3mHhWVjwKhP3hOVpWDnG850XEJt8-dhgN0UzGvipXA-nphA3dv57I72s1GdsKgQrLYHUbQeXec2e8M51oBhhxTsW-u287Ht5wZSkM9RZ3al-ofI_nmHpmCBGR7Dif8Io5-jMAT2DUz_JtCMie0ZINPG4AOgbBirakONk4GKgWcMlkNqW6SgZPhzRbywCXeVWX7JorkKxvTYb71l-mCc65ufmKVCxTVcus8txznNv1b4j3W-s8VziO_9bvFdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd9ddb3a8f.mp4?token=uDBW5v91q-uR0NbR0KUOdW4djlbsZpO3gUrbWyabBJ7hcHls248-TqolyRhTFSl_VxHBurVUGlidBrxNd91TW2jcId3mHhWVjwKhP3hOVpWDnG850XEJt8-dhgN0UzGvipXA-nphA3dv57I72s1GdsKgQrLYHUbQeXec2e8M51oBhhxTsW-u287Ht5wZSkM9RZ3al-ofI_nmHpmCBGR7Dif8Io5-jMAT2DUz_JtCMie0ZINPG4AOgbBirakONk4GKgWcMlkNqW6SgZPhzRbywCXeVWX7JorkKxvTYb71l-mCc65ufmKVCxTVcus8txznNv1b4j3W-s8VziO_9bvFdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ای نفس‌گیر در جنگ اوکراین؛ سرباز زیر تانک ماند و زنده بیرون آمد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/688166" target="_blank">📅 14:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1156a18747.mp4?token=mUSN8wgiiFoAw5-Ywfauzxs1Rgs5RiznkRNOmfAKLz43bHXiOTRNZttNEAeHYquCpIjpa-iQdPLHqczXAe0cF01rcU2qOBIMtpKieBS0AI2MuF6ZfrC3x9xdsZXkmJ9Ti2rRoQuYWwvclsZ3twJFTJ1ZyGPlQMWmXq4mOjf7kxfzv4VlwyhqMG0HMbv1Pdq1r0jHZU0eByKpIuW1xkMwezatK73rJsOWTg9f1Sz4GLeYoIatNZC4Yt3QVwGbaemdzRKyJ9m1XeBYIFCwkPKfBQEWm6jlsdqU39L1xL3TDNSyh4ih-AcCm3-T1met_usmnG1OHNkca-RMOdy-ZIGjTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1156a18747.mp4?token=mUSN8wgiiFoAw5-Ywfauzxs1Rgs5RiznkRNOmfAKLz43bHXiOTRNZttNEAeHYquCpIjpa-iQdPLHqczXAe0cF01rcU2qOBIMtpKieBS0AI2MuF6ZfrC3x9xdsZXkmJ9Ti2rRoQuYWwvclsZ3twJFTJ1ZyGPlQMWmXq4mOjf7kxfzv4VlwyhqMG0HMbv1Pdq1r0jHZU0eByKpIuW1xkMwezatK73rJsOWTg9f1Sz4GLeYoIatNZC4Yt3QVwGbaemdzRKyJ9m1XeBYIFCwkPKfBQEWm6jlsdqU39L1xL3TDNSyh4ih-AcCm3-T1met_usmnG1OHNkca-RMOdy-ZIGjTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شور و شوق بچه‌ها در اجتماعات شبانه میادین تهران با حضور میزبانان برنامه محفل ستاره‌ها
🔹
محفل ستاره‌ای‌ها در روز های آینده نیز در میادین تهران حضور خواهند داشت.
🔹
سه‌شنبه ۱۷ شهریور در میدان ونک
🔹
چهارشنبه ۱۸ شهریور در میدان شهدا
🔹
پنجشنبه ۱۹ شهریور در فلکه دوم صادقیه
🔹
جمعه ۲۰ شهریور در میدان شهرری
🔹
شنبه ۲۱ شهریور در میدان شهید طهرانی مقدم
🔹
یکشنبه ۲۲ شهریور در میدان خراسان
🔹
دوشنبه ۲۳ شهریور در میدان نبرد
🔹
سه‌شنبه ۲۴ شهریور در نازی آباد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/688165" target="_blank">📅 14:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688160">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgzrT3XqQKkLMToBD-gWjNGYoKBdqlxtEc7RhAa7dppWw8wlBQ9ySeYND1h-68qOA1viR3RRXlqM-iQZzIvMA33WCf4IdFcJa0doNUhgNel8oLVvA2zU62hvu5_5rdlT1fTeB4bvtSO7CKuPg4pXEh6Pw90hLFXBryd9gWmoE_LBRaz-ALZ9PZCtz-MPBmPAZAfqDzCXOq8digf6P68BxRZfaNtJTB4bgHc2OM5yMbc-06mvfta6CPRdTGq8kM9xDnRXDkBP6dl0CZQaFv1X6GQ_gmpKF0KrZcRtLL0RGhK9F_tCxvuHC349-NPfC2q3Gh5eMUVMdKXiSSzGJOTjbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMfYjar1iPSSoITtvMIzK3R2tS1ZWxjoBpXB0Xw8yRDZS9kUmQhta99mMnwYvcQU08m4lY0OYZW6C8OwyEHx4WvBclKx4NFG3Bevtdp-sX3OWqNBooz3n7WTlUVs1Bw4AId7x9lpFbOpJV0UsZj0UAxC1FZ8pUwm9ADu3HBZJNF5PSkmFOs-q8t2u4DLnh-6wPpFggfFDRfAK2Eqk_hLez-uZIFHtQDjhdZETn9oSy4WIBpZrH6wBtMHI9ryk8VGAIKIFJQrcLTRuH2PQllwGAhw_puETsMc3V6kb2g8kYguLLYJDGGV6FeQtXXMHtwvIBTiU143nmPbxcXjhrFHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnigBhDXSpTlZ9bQIvN2yvF-2PyfI2pE5GY2VGkgtLBT8UWNvO8AlgAHLDzyzhSuOFKUbcMK399aH5nWJe_N7j8R7fA3ySMuxTnjl8WBAQTF0lRQgDlrpr4BXHbXk5BmLmMeRmzXN7ZWFOfy4t0Hrbw5iV9kN8pVI05nzcv8JMo0rIf6FvOkPyWB9oC8pU93oJ8JPjoGEFQEs3AqUo-LVMrAYhfWkgrXLmdmOau0DppVV8e30fssqVyB0XGmUfdYN4-Hkl-IzcFTeiS-e5fzcl8PndpPoYCO7YTT1Yb1kLJf-OlsxkFkSOURovG4bXPhX4nKu01qKoRijmJY4vbIzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/So8mbK86svQu55mlXjb8XPKFP65jO5bNRDxO2FultrLDB09xbgidTB9MCNMt9_doEVXxHrFjNJrIZJksz9kjVRemnQGRzsu49GBqKZ-owMsONrwFUZLqKktjNn5jYFpATJ9o0eoXcOYJmrbE7foKKv7LUeJn2OZZ3AYTiH8krTxBnDefrsv0bh2nWpcrV-yQwVGuUgV-FcoM-ALNAcFcpwF6b5bSTpHz2j0pbXUdgwXea4DSdvrQs-Gsh1fTWKi8mdK9yn-x_TvvOOr0OyAAf1XkP7SL1ZWxY3DxBtTiviQxBL8a9INDinSidQ7khy8Pg-h_rlDVsLH28QyRdKGvrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvyyoZBGIhk-RmYf5URbsJjEvtfsc9MuG_7LK4GG_3z694vrat7zc576OaSYvTC6EaBGoBow47OQqmiG5XoprlWQcyGPgh6zVvcCLBuBmFz8yiahaeD4SpiM3FHwewYw3z6AIRNkhFZeqMO_mT-a2VcrEWVZ9hHqu0Eg_sm1_AXw_9QAWqVBdWk-EbGdHAKxy9OTAE-raLlM2cn91EubUoeoVdrxmNzeT6v7ophlaB2DMU9HVU5UyEvnmJD0nnQtAUdp-cMGZoTH8Kvkx5v8uOrmGMcRwbxGE6gasYmM1xho2EjtpzcrHsd4WAwNG32PudoqQXJ3ENrjgxkYPIyynQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت ربات‌های صنعتی در جهان
🔸
طبق آمارهای فدراسیون بین‌المللی رباتیک (IFR)، بازار ۱۶.۵ میلیارد دلاری ربات‌های صنعتی هم‌اکنون ۴.۲ میلیون ربات فعال دارد که سالانه ۵۵۰ هزار دستگاه به آن اضافه می‌شود.
🔸
چین با اختصاص ۵۲ میلیارد دلار بیشترین سرمایه‌گذاری را دارد، اما کره جنوبی با ۱۰۱۲ ربات به ازای هر ۱۰ هزار کارمند، بالاترین تراکم رباتیک جهان را ثبت کرده است. صنایع الکترونیک ۲۸ درصد و خودروسازی ۲۵ درصد نیز اصلی‌ترین خریداران این ربات‌ها هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/688160" target="_blank">📅 14:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688158">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcacdf7197.mp4?token=ZTLcpjC1aGZX-PMUIHy2fkOyCU_LqkMrOGLiwEKpjggjuN7ZX2ALJG67Bp9wGAIJYLjMGK66YI-vrXKteFNiG_GfIvENYBz-h2O7rKos_ccv5HaS5c2K-6je3HE-gB9AA4xpbv_fnprhu95IwqtPbNvIQHB2rKw7ujohxwEnPrkLHTcQN8I_oSgSqcQH0aprmOt2-AvDbTwXF5RTpU84fA2dTZMsKglSmfSh_twgfd2SNNyb2SM8toJMbfGhzUn5bL-K6pNa5UEjiQK2m6lzbjHLms7BV2vnaqOlvb6kyiZUnyErNmZNbEEuodvhkQnMscenIM9_3Z3IGvGsiaim7qT-3fDU0ks21KFxq858RsRGyIQazxkchjGi_LzjGdNGOagSaUP2Lfrz2yhOhu8P2SLR0MXnDkU3Hb8j50IY4-tA4wc8yEYvj_BLvM7t7UcV9jbh4-KY8b-B1oWW4S4hun0FrN5YfCLQamvW_CP1h4RVxafKjPq7-rGqBr-qr1AaSzDhf9XOHDwyNZ8KiwQwRYD-tx3g3TRpCi6gQ315eNEbrBDnSV6EclV8y9CwozD9zdocux3keiFYmb9ck4irA0XizDOUwUsIDdzkMmFDpxKZMQRv8IGrtll7DiiraSnbZa3Jh8hpWfdE_74rZUGNyDduir6xkLAOqupipXpmKSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcacdf7197.mp4?token=ZTLcpjC1aGZX-PMUIHy2fkOyCU_LqkMrOGLiwEKpjggjuN7ZX2ALJG67Bp9wGAIJYLjMGK66YI-vrXKteFNiG_GfIvENYBz-h2O7rKos_ccv5HaS5c2K-6je3HE-gB9AA4xpbv_fnprhu95IwqtPbNvIQHB2rKw7ujohxwEnPrkLHTcQN8I_oSgSqcQH0aprmOt2-AvDbTwXF5RTpU84fA2dTZMsKglSmfSh_twgfd2SNNyb2SM8toJMbfGhzUn5bL-K6pNa5UEjiQK2m6lzbjHLms7BV2vnaqOlvb6kyiZUnyErNmZNbEEuodvhkQnMscenIM9_3Z3IGvGsiaim7qT-3fDU0ks21KFxq858RsRGyIQazxkchjGi_LzjGdNGOagSaUP2Lfrz2yhOhu8P2SLR0MXnDkU3Hb8j50IY4-tA4wc8yEYvj_BLvM7t7UcV9jbh4-KY8b-B1oWW4S4hun0FrN5YfCLQamvW_CP1h4RVxafKjPq7-rGqBr-qr1AaSzDhf9XOHDwyNZ8KiwQwRYD-tx3g3TRpCi6gQ315eNEbrBDnSV6EclV8y9CwozD9zdocux3keiFYmb9ck4irA0XizDOUwUsIDdzkMmFDpxKZMQRv8IGrtll7DiiraSnbZa3Jh8hpWfdE_74rZUGNyDduir6xkLAOqupipXpmKSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهر رشت، دیشب
با چاشنی شوخی‌های جالب یک شهروند!
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/688158" target="_blank">📅 14:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688156">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc033f18c.mp4?token=AtEjcnaV69D6178ZayXDE6jscETwltAGY_iP-4xZ2_2_ILh2j9E3gubGeA5KzuaafstkyXYGEhRRSeg27bSQ8cYdsVqCH_o2FT5rwiJl9jhaLQsdmM0gsrptmUnQsIHCP_QqIIRPzEq9jKmBmvkUoSuCR8umWcc6KrPKHtDNK08d9Ydx57SS-TAhL-tiDkCkKiatuzpfPeZUamw9YZeR7Fw2kqhqNC25TkzQnHCzA2wK-y2LJ9M8DbwA3lMSVWm6qH-otRAv8pzedUk9WUyp0sdSkvX3xIRllOTeHKTM5LMfYntUgyzdA90iAiOjwm-681IO-bDUQaZu_sOpzXEyqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc033f18c.mp4?token=AtEjcnaV69D6178ZayXDE6jscETwltAGY_iP-4xZ2_2_ILh2j9E3gubGeA5KzuaafstkyXYGEhRRSeg27bSQ8cYdsVqCH_o2FT5rwiJl9jhaLQsdmM0gsrptmUnQsIHCP_QqIIRPzEq9jKmBmvkUoSuCR8umWcc6KrPKHtDNK08d9Ydx57SS-TAhL-tiDkCkKiatuzpfPeZUamw9YZeR7Fw2kqhqNC25TkzQnHCzA2wK-y2LJ9M8DbwA3lMSVWm6qH-otRAv8pzedUk9WUyp0sdSkvX3xIRllOTeHKTM5LMfYntUgyzdA90iAiOjwm-681IO-bDUQaZu_sOpzXEyqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری هولناک از رانش زمین در شرق چین
🔹
بر اثر وقوع چندین رانش زمین و گل‌ولای در شهرستان سوئیچوان استان جیانگشی در شرق چین، تاکنون ۶ نفر جان خود را از دست داده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/688156" target="_blank">📅 14:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688152">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MILeleeo4kYH6ZkT786hR9TayCAGUCvZ1Mz4yUPmzkEE8z52V7FxMXRVVdtvGoRD8BrHXnHRf7kMou-soIXgz_LaJ5YKsfdaTcOx8IF7AMm7iKAOBwZ2lqfIu4SX6cqGxiidInvcsHk_ExGa_0X0qJrgCMkK1vi5oWVL5UTPSJcdSzUbho9ZgvG8OmvJQ3cr5svch6lF52R9RE3742S_4qeJJ9586cx9Yz8ASP1OjCT4s0dboSOEHXnfvngtiKPvs3Lo0IdlgNfY355UZYhzxRzGv58I37j5la0hCf4w9LX3iM9JCSr0QQpIg6FIhqfdcnKoTNn6M5SBkHSL5Bpi1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QyG1TRvWZlyxbZ7g68T-5NCYO91jLbnBK2uQVZ-aNTCQr7RMGNMjLb9Wl-8AV300eGnQkP-75KB1geish5zdCPW6vY1ZiwFtThFlKWwtkS6QlVXwFhm2UvwXhos-8ICwKESe8uKtqB9m28QOf11WhrXD-7NY8emOVMsf1vnpsjpAD6vkp-RfJ2jpjYSJuW7Q4V2VLL76bv-Yh4lLnUVEwB68wLfxiC_F40tZhWvfa9EeVDe5DofDqXn_Z8VY3MkEmp2AeLSdeLsgoSLgv5mUyXWdEwK2IinG8W3-vUBXoMksuQ-TQ0lNYy4B3hEtrv9w_s8Zelg1B-XIaHp629tb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqzqOPD7etc1kzKkGB_aqkAGiXOJiVDz17VIkkgefY1pjVV54WAQORxZQrjCrhP_p2MEygtpTCYRXrliE7Au8SSfkjcjeUcHQOCPyTNVdNYEoqQLXxzti_5_IffTrVXM891toj9GA5k6fHG131jSdyRGlfDIDj-DBnAHDP5fpbCUcSVdIK6nhFQN8qH8AommCP2gwCgVNLbhYqMxpguZfgcw5syhkF_CQboKNKfrenjttAGSvGGg2gU4d8k5cTNKfxT_vULJ2V50WJP6cZqc0xxMFrBjql7XNXWAmtF2VUkq5s8VEo4atE9TDB786oRpsjlyljmz0e6o0-byz6bzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Li7zVdi_zlpUH0fxFoqkrxYfqqdK5-7GynTyCzYX4b7Ii_jcfAuZR3msIk0gglGLJpshnqN2vmkUCsoPdjDhsBSUiWmFrhGTWnF0VIdYsy-Tp0fR4ZGPMZ_Chr5vuKHY_Lqtj7RqkSLfN5U75wAAczskczF2CWRpQVHr-GkGQRrOtg00rd83LYPzKm_HhVjHMv971XgXd60O5DvG5sDEGsAtKJ1U1dMSd59sn-cUPS2-O92ph17SRd0I5ALtIfFyFKlMIdBwja15617KnBpP0o4KUgl5164byAwk9QCisS1KikGPn7J8y3k2-j6Njjpru9tvk4ObaXIX7jzxUt54jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این ۴ رنگ شال، با چه رنگ‌هایی ست میشه؟
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/688152" target="_blank">📅 14:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688151">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-fiFoWF3dPloCBsafmI_dH5ZQHYr39a-S_xeNizRVNyoroxmA_CRIjYwFZe8NjUyHsblsfSjCAZcyyuF86IH_ElaC0FltsvL9ZmCUnVRkmD83RuSXoirQQB9N18RAvxUQoh6IQR7T3UYXm4M3enQLc3cLnmBxiFWq1cKfQrVkg4K3nNkOeGq-r1tmJohqSfQCVr5FmIA0Gs6sX12P8muOI5gTwO6Ucmn-vO5_kN4mo28ju6FCHi1WcRy2_7Z3jlOLrTCQgmiFHU4oQ5WbdHvTu9qXl9tqA2VfDLCYlJKka3OjgyAY0lvuLSDNy5ZNBElARHLZ1Vt7Fwn2wVPuLwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_خودرو
| قیمت روز خودرو های بازار کشور؛ امروز ۱۷ شهریور ۱۴۰۵
🔹
بازار خودرو امروز در واکنش به روند نزولی بازارهای طلا و ارز، فاز اصلاحی را تجربه کرد.
🔹
با این حال، این افت قیمت‌ها فراگیر نبود و تنها به چند مدل محدود شد؛ بخش قابل‌توجهی از بازار همچنان مسیر صعودی روزهای اخیر را دنبال می‌کند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/688151" target="_blank">📅 13:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
توزیع واکسن آنفلوآنزا از مهر
رئیس سازمان غذا و دارو:
🔹
سازمان بهداشت جهانی تغییری در واکسن آنفلوآنزا ایجاد کرده و تامین واکسن از ۴ به ۳ ظرفیتی تغییر کرده است.
🔹
به دلیل دیر کرد در تولید واکسن آنفلوآنزا در تمام دنیا واکسن از مهرماه توزیع و اولویت اصلی گروه‌های در معرض خطر هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/688149" target="_blank">📅 13:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9579f2362.mp4?token=GgDxriqqPLriKprl5caCIaBWMS35VXcb6EvCItshFcV-vq1Xq5Dq5VMWOSrMgz3m5gG7fFH3c33BeGeT5pkrlw5z-IluH6vlyEd432zJL9wkIjaWMQeFoJQJGjRvfA67ckKfa0qICVwZE7K1q1awwRuJiApatn86OosQ2uFbeKZ95DrKUXPKKf7ekjJlet0uNacA9Se9LNnRXpnt8B4qE4-w9NbgXNJsFbFuH4sHAj_A8BnMCAYcyCRXmfqv9oSmxgeuES0bZKVlFcJPE35uhCDNQ76L221msShGmIutWu1paBAjugce1-TuDjQ1eNrnf1cvX8zyiwFIYh3jv-jCvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9579f2362.mp4?token=GgDxriqqPLriKprl5caCIaBWMS35VXcb6EvCItshFcV-vq1Xq5Dq5VMWOSrMgz3m5gG7fFH3c33BeGeT5pkrlw5z-IluH6vlyEd432zJL9wkIjaWMQeFoJQJGjRvfA67ckKfa0qICVwZE7K1q1awwRuJiApatn86OosQ2uFbeKZ95DrKUXPKKf7ekjJlet0uNacA9Se9LNnRXpnt8B4qE4-w9NbgXNJsFbFuH4sHAj_A8BnMCAYcyCRXmfqv9oSmxgeuES0bZKVlFcJPE35uhCDNQ76L221msShGmIutWu1paBAjugce1-TuDjQ1eNrnf1cvX8zyiwFIYh3jv-jCvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دشت رؤیایی اسب‌های وحشی گیلان، جیرسر
🐎
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/688147" target="_blank">📅 13:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688145">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXy94v3Z5k6QpmixGyDc4Gq92heMSGd6reXCDt7ealN__jKPbpqBdqkfGGHfBexu-lYTSsoa2trcPg0Q0_rRMZA2JFimtFjMtUXsfOyfbfo7XXS79DCRkJESznREAs4W1QUvLzVZD9jNxqw9nKM-LSSXFbLKS3CGrtmJUwwGvngXSyb5C0r4JPtM8r-IG27CeDZ8b_NT5nWEmmTNL9bxj-1ySxFk83S-A_YpJm5A3xyLeWIeeaaipR8FAiEtBfUA1sQrC15oDu14zPcPFiITEY1cIInbeQKvqIhZtagluJyoa88jViuxwvnbllor2RBEcWA2zBnA6DYXxrWLxcJrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نویسنده سیاسی یمنی: سپاس و ستایش خدایی را که عربستان سعودی را پر از نفت کرد و به ما کبریت داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/688145" target="_blank">📅 13:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688144">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcPcACRU_ZZdfVKTHrjE-NOVweEF_deddVdepqTb1-xvtWuWpJqUCQtFUdhFgv39GkdT2ZUtMQoj_Ka1MMo-QFWmX32u0C7MJqEPgWKsO0kFfd1M81sgmaEobF7acDOj5ZKeiMKT9cQz6GMS8VNMMxX4im_DK2ElrpDWHCvg1uc5kP6tdFmj-WOy51msChStbFWtEEuexOHfGb1HOEmCFtdh3D3eCu9uT4CBz-9Efa5EugkboOqngoD6Vhn3T3q9KqyLVbqJWymV83c1uAqHuWK5PYvfy4nctcq8agtI3FD9NTqgi4P01XKF6ijJ49UzUdoUnMMKl7s25y9xqaJkuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۷ شهریور ۱۴۰۵؛ ساعت ۱۲:۵۵
🔹
دلار آزاد امروز با رشد دو هزار تومانی به کانال ۲۲۴ هزار تومان برگشت و در آستانه ورود به کانال ۲۲۵ هزار تومان قرار گرفت.
🔹
عقب‌نشینی دیروز این ارز که حاصل مداخله گسترده بازارساز بود، دوام نیاورد و با بازگشت تقاضا به بازار، دلار بار دیگر مسیر صعودی را در پیش گرفت./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/688144" target="_blank">📅 13:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688143">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA2-CfgAqxUxl6Phnu9HcJTvxd2_4CRKzLyErB2CnF4lBF_QFlpZPlNAeh2c-4Ot7Wud8Zg9KGmhgRbZ-hC4afCUnkYrKEG4rFrC_Mubgdbg2YZh17BkUR9HFh6J1-eo4sXNOaSzYXSpNXwz0d4CtLHc01m1UM37L99F9t7GimZCJjc7tEcuDT6nqD3QcUnE3d2OdbllR-K9EwO8d9exJwEegQ8frp7zs_Y0eOPNaKQgr3qrTxC39Dyn6Mo3vOYPCmwo5axzNrFlX9WVliCU0lim7_kmmbdvZzgLtJQsLof7SWje4HcUKUIiXEIaUxtQAreWtOneT_1RxPT3yn4BEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دست‌نوشته رهبر شهید انقلاب برای آیت الله سید مجتبی حسینی خامنه‌ای
🔹
این کتاب ارزشمند را به نور چشم، عزیزم مجتبی حسینی هدیه می‌دهم که خداوند اسلام و مسلمین را بوسیله او منتفع سازد. و او را هدایت کند و از خطا و لغزش در گفتار و کردار دور باشد. الاحقر علی حسینی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/688143" target="_blank">📅 12:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688142">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBjsIg7BnJkPmO2hq_RftI2IfJfzIwl3IzmziiOQl91iz63V7aG8dGSAuiM2AGQF2CoBRPnrNi0HnCoG691mUFI5-UYaI6G87rTkORaH_ABh2KXQTbHgPejchtj0SOeOyh8NBw43LNtpbnPpPihJExPtmwriPQP1XERDmr_EsGvmCV36dFaKJ24IW5vem1KL0Akkz1VIKttx31--yBQhnoUtONqloMCBiNMo3mBdZgi6z-Lv7eEcFiQhARUfhCRv5L2ePsPM1QdKzSTdME4ThTrqH7g_NS7-T61-oIDpsMy-v14jXTpevcHXtSKSpY9pt4b85XFPtxBE2tXGnmyPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
قاب فرش اشک حرم حضرت عباس (ع)
یادگاری نفیس از حریمِ وفا و ادب.
این قاب، جلوه‌ای معنوی و چشم‌نواز از حال‌وهوای حرم حضرت عباس (ع) را به فضای شما می‌آورد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۴.۵ × ۲۰ سانتی‌متر
▫️
جنس قاب: PVC
▫️
طراحی شکیل و مناسب دکور
▫️
انتخابی ارزشمند برای هدیه و یادمان معنوی
💰
قیمت:
۱.۳۹۰.۰۰۰ هزار تومان
✅
قیمت با تخفیف ویژه
۱,۲۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/688142" target="_blank">📅 12:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688141">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p05PZQzdrmKeXwF4G0D61ty3hwDvEkDIOnV3v_xHx6ZVSb4FoNmIuY_-csMPniOPkUS9CwMcjfeLJ0vRyugCvX9ddKwxfEhEjbzQp65wGnDNKLmUFcXXqfbtbP8PT7lrt4RRK9zhFLlaf2sSBWG5fijiqrC5teUF4cI7kDb_5WGvK2NaubKgXNn8DqH87FyVPaGvemhe7brbwQquv3ByhxIjuW7cVVoXMnrKtKQWZTFs8BQIZ4hksmUm2rQTbVHBkFKW3Rbva82v6lRoToItppoqBWwWVQUf8G8hQfpqQfCmhRp6owsGJRiaFZagDVBs2B2igUd5cjdnmy2GSFPH6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ به مقاله وال استریت ژورنال اشاره کرد که در آن ادعا شده: سران ایران خواستار پایان جنگ شدند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/688141" target="_blank">📅 12:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688139">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سخنگوی دولت: قیمت بنزین سهمیه‌ای افزایشی نخواهد داشت و فعلاً همان ۱۰ هزار تومان خواهد بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/688139" target="_blank">📅 12:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688138">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای خبرگزاری آر‌تی: آمریکا پیشنهاد جدیدی را از طریق میانجی‌ها به تهران ارسال کرده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/688138" target="_blank">📅 12:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688137">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/224582e68f.mp4?token=c-EeQpfznJakXIALRJJFtFxl1d21mItdw1xhLHes7mzOufWSESJ0130lSBhyge1WCCg2a9-V1zzWlViH6I9ds3AcDNJev-hDY67aMhpCzxUWWzNl6jbpD2xggnDMPP6dWDUrD095oUuYtb2U2v92ftlID40VC7jY6MjDqZbQvTIY3Rv5DcFvqYQ8LqiJb5gmCxx2qMJWl64vspflGumVdk_v1A4zCJCIXHV0kInLh__zIjLgl9VC9u6GiW1MefGBx9uWNM5snmG793aKoFrIZJTkopANskRPuUIN2lDHvsehmGSodQTH6Bim8aGJGaKN20L7OH3s5VOAVOsTc59uEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/224582e68f.mp4?token=c-EeQpfznJakXIALRJJFtFxl1d21mItdw1xhLHes7mzOufWSESJ0130lSBhyge1WCCg2a9-V1zzWlViH6I9ds3AcDNJev-hDY67aMhpCzxUWWzNl6jbpD2xggnDMPP6dWDUrD095oUuYtb2U2v92ftlID40VC7jY6MjDqZbQvTIY3Rv5DcFvqYQ8LqiJb5gmCxx2qMJWl64vspflGumVdk_v1A4zCJCIXHV0kInLh__zIjLgl9VC9u6GiW1MefGBx9uWNM5snmG793aKoFrIZJTkopANskRPuUIN2lDHvsehmGSodQTH6Bim8aGJGaKN20L7OH3s5VOAVOsTc59uEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ عجیب هوش مصنوعی به این سؤال: اگر شیطان بودی، چطور مردم را بدون اینکه متوجه شوند از دین دور می‌کردی؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/688137" target="_blank">📅 12:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688135">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHIUTibyW8NaR5ESNCkVbHaClEk_Ir_KtgdQxeL1UGytrSnSd2fb2V_OIc114aK8Wb1YCCMY9BANN7aKh3BM9idj2F9nKsZBJIBU-71pe2Id0xBYJB9Dta2gkuCEVqfqa7dlor-Hd3gKY_MEmO7l5dO3pGGlN1koZSLT2Vy6CPjDdxHD-RuGcLjRO6lgkr0LG_Xy4H-jJV0gRXNBjpIidnBETOaJPyb8fO0UD4nhqBstXZXruhl4GB-pjomb-P3ZAxpKPtAIwqaB6up6rUb0lyvoKGKJwTeaQzY-X5zjHBLIRaH_UkxZOgKTimP1bO950_07Vf4e5C4J5CBxi46RBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/101d1a835a.mp4?token=CPogoVFBxJBRvPts2F-TmSs_iMiyz_9s0o5hikA-3U5smuBMnimzwW4n8PC_y7gShvbZDYrWjkHKKY7JpEbUn2nv4ie8rTh46-tdnT8RxtQu-UlHEo7HIf4jmnO4lFH5E7-vDyuNgCpLaU53V6mmTUESLGS166kyK054rG0LphOPnFu5pL6l-1PXjX02bJM0-WBldvg99jRBuCN_ariOfxoVnoCLnZxTSN82ESw4I-040N1b-Jl22ZNA5axOwIzPQr5wa_pCBf2bkqEFVp0MHYEarpsKr5ImuydhyOr_hXglsYS-XHd3DyLA8MgWRjXlwI-ikx6ld2MT63cVBiEcYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/101d1a835a.mp4?token=CPogoVFBxJBRvPts2F-TmSs_iMiyz_9s0o5hikA-3U5smuBMnimzwW4n8PC_y7gShvbZDYrWjkHKKY7JpEbUn2nv4ie8rTh46-tdnT8RxtQu-UlHEo7HIf4jmnO4lFH5E7-vDyuNgCpLaU53V6mmTUESLGS166kyK054rG0LphOPnFu5pL6l-1PXjX02bJM0-WBldvg99jRBuCN_ariOfxoVnoCLnZxTSN82ESw4I-040N1b-Jl22ZNA5axOwIzPQr5wa_pCBf2bkqEFVp0MHYEarpsKr5ImuydhyOr_hXglsYS-XHd3DyLA8MgWRjXlwI-ikx6ld2MT63cVBiEcYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: شرکت نفتی آرامکو و پایگاه هوایی خمیس‌مشیط را هدف حملات متعدد قرار دادیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/688135" target="_blank">📅 12:24 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
