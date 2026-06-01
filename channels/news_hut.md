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
<img src="https://cdn4.telesco.pe/file/TpWO_3R1vur3Yz5hUGcKB9A6Jojr64b5B7XB9vE5X7A1xqLOxCRlj3fd8Jnvk1YdWwjKIuSVLndlctfbCVSn4ZZ82072sUvzqHvZ18q36aZ12qgG05QvD84pK2wNZBIK2GeRThArbIbyPDwznQ93MRW9696ElbdVQklxdHZm1zQMZG8Af_E5Q2t71aChRAxtEMqX_4Poj94zxaTRkWdtHahdqirKC51lH3-e6NSUPs8enyy5HDm-DJ6f1rytDq9Xp3R3rHTaupjXxa6gQX60ZvhaVzbrYkBp9TN7Ec9wx0SoHem5LjhjQZUSGWdNxBLfbiq-VHXqJyMB1qinlayY8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 191K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HKguuF7--CRyLFvjw1K7oqpBt84N7hqM66sbRZCysg_D4s2Uo4KKIsF3x_69HMws5_JkiiMC9kwYY_VCyryFQ0THKupl6xO6sfH1F2rvHDmE5REt2geXvB9O7_QBmBEHwqp5gul6K3DqUCzCC-dZ-J2igknP4uN7fj8T_KiMi4E8amJ-EK2xJ8LEdRip3fY2NXvefczn1O0QYmVNlGddI-69oKwBz66q349Kafxxl2hvSPOXEP2rN9fsVQ1lnkTKqXnfNBoSsq85DyHUJz-4E005VueO329f2ZZZPlJZl62EUTHNzSHplacrcOC_YRaqlpxiLPBzOuozFxyfmb9elA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyKnq7Y2aJsZyj0nPJpNAbod-nKoLUTcazkLmPIcgtN20Mp56KmcOsNk6XCxcN3YYhIYJ24MvccZYyPp5K7cS9BfWi-njxYTsDEIAEKbTla3rP8oqk48qlEENwnuh8KnnI15QFb1ZDuPMmfltuoG24bBTDL2zD1FUvE63cUQlLc2PfYa1h5cEIxPmLhr3IhCy_ogObcAABzdFJiI_a8CAt2IbmRCBWyZtORWFHYck19ixMFMDTS9ba_XzB5oVeySiSkq77IO7i8fcX1wIhcQbl1HsWvbXN5nnB1spZHGgKYRWtMmDlkx7a4R9OAb0b9iityfmsHfBxcBMSi_-JDBqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3xSzT0lg8HzWxemYwG0oihUTwpo_PlUxwXafOij8XXaGkJqpsdyjoUtoStEKJwezEQ_GS2dvy_mCmncau0vpwQK6lnxyQ6tXWXNjmwwkg1UV7xFqwvrCgftujfO0k5y85M-GMr4fbt8IXHwHdblPWT2wPWcjiuyBX_cHiooxNLMDAFGp4E497X1s5GVPBAg_Afgiszp-K7HMJTPHB-4fzqCgl_P2hih-F5M4cy4D7Kh24M3TV-qcmW377OVS5-Clh1gi3pT17tTJzDCwPOV35b8ocpGI-jbvXsreKfuNbecQVMn2CLyoByPHL7WkLKEW3C1opt3DHOCAuO0WU6VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhxllV6SEUFYM-NeBUqKJxZE4c8pwmEp92fFJllfEIyn8GV6xrfRvkcFPeBYP5pcdNQtYSjfWXuV3-Ha3_rwcBPNBOap3glSkh6Aei0tzn1ZTc8JlmlcAF1Qq4uOfqulb6KseZL_3Js6Pr0msudJtnttNsmAEpEXBqlnIMfFamg4ppXVt37KNqY-tDho0SOWhUdTkNEjGGLk-vSUMVAVnhtdyjbj0LuQ4z_zWD7mwMmL9L1F76noq-YqNPmbYBG3BZ1dZSRXOaq4ntFtnJs_HjPieuddtm-mmhPqWjKYtifTSlaH3sA1HH8K5jchKlYPzk_EA21_KU3mdWLmtgz47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjUigbcdUKAFwsqR_BPh-PC6aQZW4kLxhAmCBTDvmo8_s70iiA-Q-JrFbWwK258bLV2HHDYbUK7ZEufPBnq2vAvlALFIE9y6L1m3kR8IBVR_jwSL_koj9OpOkBOB2HOO1k_WasDDAT4x4KgUCdIuW20B5U8FVu5-ZE9gfNP-ARtqytN4xCE1wMAjAgk18569fIfUaPcn8Yx81a7fF906kaWQaDhbpO8pDKtyRetRwVDSFE4J01x0fGk6PEy63B-fKusYwkQ971FSTzYJw_RDpKnbMDbF-TT93Dqx7CfyMtGOBHZ3RGvYdNboYHN3zQCbhmmuzI3rTk26SWtJSnzCmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CITB5Dq0KRKYet24iiZcPuzjFXN4G8oGkn2Qd1CgZvc0-YrUB9Ee0dEyAZ87SnqTEQEz2Qq66P4MvieFh18C9HOe4Ngr_64fARxRlNHLXlOzp88y_FhuhPnA3YFKXecYcHZdMeJQCbEtf60XsT7_8qtXikqGwoMryXoJKooynDVTLUAnJjbvrpWoiWIqGV919edsbpLG6rCnpIC4hzYWu2xM0hPp51s8G5HT99ABuK9I9BlxYCEJN4G53-w9xvx7hfcZVxMYm8EnFPMlEJ1txeg4eeeg67mDbeO4pw95NmBsHPXyEXdvsb9ulLmG9E9QJDeJhuPtc0R1rLvBQibuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=e5dJbSl1KkjR7ir3WAJGc0Gk7VfFI-MMzF2gcU6wH1RULCYF_qA4Kj2CkPY-xSIjlkJiHFlmKj43NTDcZLhoeXGw0VhRsYjtOr8xQF_Eaf1yHpk_R6WzB2k7Gs_mfUkfh02H0ts_cjCOs1iR7kBziwDe89TL_jkLfJrL4oeqwcTdTJtO4rN-CUOdYHssldfWy6OaH4kcm69VCvLA_BnuVHXqQgu6e_k5wKWo0u3JFB_w-jcWsRZwxLPjWhDZmgXvOyRLm6mdSqoFRsVdFh8Uz9rSdHIcCA0D42pSZf5-x7wPgINSSYHNZvvI8x9EaAwryWsxtESbZInBCf57YmO2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=e5dJbSl1KkjR7ir3WAJGc0Gk7VfFI-MMzF2gcU6wH1RULCYF_qA4Kj2CkPY-xSIjlkJiHFlmKj43NTDcZLhoeXGw0VhRsYjtOr8xQF_Eaf1yHpk_R6WzB2k7Gs_mfUkfh02H0ts_cjCOs1iR7kBziwDe89TL_jkLfJrL4oeqwcTdTJtO4rN-CUOdYHssldfWy6OaH4kcm69VCvLA_BnuVHXqQgu6e_k5wKWo0u3JFB_w-jcWsRZwxLPjWhDZmgXvOyRLm6mdSqoFRsVdFh8Uz9rSdHIcCA0D42pSZf5-x7wPgINSSYHNZvvI8x9EaAwryWsxtESbZInBCf57YmO2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmkPjX4rJ_XOZHYxysSPUn8udhU_MHZd8d1ZOWTV4CjueZQZwisT6aTSILSACk_Vl4pN2T1HiBukcgbrVmB6aqoSTdbLk6A8IdkJXVlqjmeTFR1Qoa9hrnbm-4J60KfU0CXFLrWGDZ78GRGC4PmvrboGRGFy_HZRUdCgwWUEPs1yyhWjV2_rza809oVSfmXzMK1JEiqnTyqIjUqWV42lCmD1qZyGgZKlYrEiq0XZUkCtN3QQR2pOgOgNmfYf5yO8T2TIVYg_IRuY9DdZGMdfZk3oI9BTAoRB8AhBo66vqSPExj2iRGwcnOhjyYIpHP4ulSvarmSH-G27nWEBr25HFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYl1AiOuKPkLjuT2Ct1yzcaBbp7dDRIU3s_ZeLwgAMCFaCDIFrnRTa3uF4fil6cg_VQogvq2KvZHOgDgcPGniVtlobUe1seNzvucI273xwlvPOSzbacCrNnKiLxdygy_oktqA_TU14BFueUh1bnfRsNtZGFH1-JN8DSYcMfgdAxbZrIvoNepbwfSWXsmIDp_yfvfHsiF5sKqDVHtxobF0-t-3FuKe_cTE1RFTetmqSzDYbtJq8l3kAhN64Cet0DzSifQq9ne3hln4pyv0nTwQ6ibAHOGL4NbrHZ8bZko27LuUwLPZTxUNou5VJ8qg6YDyCcIpXVBeGvJdgVYzq2xCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HaYhVCjtcFWj46Lt-VDElFHVewPaXwXwjLsDs1vXOfCw11Iqch-phFjT7g51uorJ4bKtMYjfDnMSt3WHZbHMYaCmhi562uqhd-QrH_g0arZSDuN2kMKK3hDbXB6EKTSuWTK0wyEBAdIRSXqDMQ_Fu7-kF-0lCpUcdvi1p1xifTBQYsIP3KXdpZlQLw5fv9jE8ctHpEXYsX6gR9my6v0ELUpsbrUUKsVGSkIFNMgpe7z1FTCWR9metQySq2CiMiT3ZMrVzHNSRgrkkOuGU3Jl2CanuCY6l3YdQidDqODXpBCq6efHKWCEGY_LD4cHXEjuBjKhn8QHwxFfrxly6YSP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-fRhUhXmtDv2qlu2ZzKP-rEQGzCXZLxrdhqo1saxD5ySN_E5DakLgUTQMMIMhkhVVDOJOv54raPoNmKsKuZ3ZtBXSlet1WT2DdRWeHqlprKqvhc8Y65SJRfE582hk6ntcMZf3N2gtpcfx-59Bletn6KEVt0jbMmMeLaiYiV0V7EIBZYLLKjBBIXS8ZrIHCnwlwRNVmO6eVhUJRCoJ_gVcgEc7vKZMiE_UYGsNKgnY_ROGSo6q6nHmn7P0XQn0XKHcSgKTakadlHVyw3RZV8enbWx_2kjSkGCdIYecvWiCHUFk7BIJaKFNqTKXP6yGYPw_0KGYVxYrvx9lO8syFp3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=rsqITjzt4T3MkDtDZIGnX9ruFkWdl7bEIWNzkB52QDYns-NtLeoic0dDT3O75SnpI0pQUnsrchlnREObbfg99E8HM2HRTi7pirG74zBogt3xdwHd-d4sR5uCiWN04CbhSsBbzlzjRTe3IfiL3XBiUNFkA-a-tUus96Yh7iP8sC4vt-cn0sNQdoAC2mSSq1GsYE6mVWJZn8qHL7gs55M-fZsOk5FZnGgHkhdbrhfekq42tHtEQiW_4knXphTUeoeanvnnzWUj5OgmoQXytGVEMZ8GTeCRQw88QN3Xj4PjlzJtc2P52OLuelt5h4zrhBA-ruSQp14bIIS8YHG-Dn2mWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=rsqITjzt4T3MkDtDZIGnX9ruFkWdl7bEIWNzkB52QDYns-NtLeoic0dDT3O75SnpI0pQUnsrchlnREObbfg99E8HM2HRTi7pirG74zBogt3xdwHd-d4sR5uCiWN04CbhSsBbzlzjRTe3IfiL3XBiUNFkA-a-tUus96Yh7iP8sC4vt-cn0sNQdoAC2mSSq1GsYE6mVWJZn8qHL7gs55M-fZsOk5FZnGgHkhdbrhfekq42tHtEQiW_4knXphTUeoeanvnnzWUj5OgmoQXytGVEMZ8GTeCRQw88QN3Xj4PjlzJtc2P52OLuelt5h4zrhBA-ruSQp14bIIS8YHG-Dn2mWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8E0EBLc1Z4_EJZpzyHYyc67LKOfy2De6X5uDXiSrx1q5tSl__fm-0JIpRum07Mf3-G6xEbmWq68OIzcGfW7kWMuxZfqTsFHCcLZ4ggTAXhJGj_MWG4nxKGN4MB3CChLvavai37ffS-04eZhUyVoVNYbhmRbx_mmkWj0CuCPdeCz8Fiv-p_NELdQbmVUqQ54T0rk1J5lOplnDxN2dPrLLKgEseNAllXVXCdvkjUeYZTdMvYSJ6XTwjiixSmgBtCZk3jC9BA8i16uBQTS6wu-dMUg0IgeE5nNLmqGSa9ASiY7gSE4-jq3oluxAIC9ZWtOUwN3jFrdUdDlPKIiPqTzCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=XMO0tZr1_EO8qfLtWmx09KLFgUggxTUYfmfuDjtTj6TuP3T2irIUDk5XTJ8_Xu7roTthe3koDGBc1TIN2kZZVdddVBfSnpz7oAtXFZs7TCYeGodSTg5Z8x0xsGOQQmBoi3Jq6Tk-aLWHxUwmY9Kg2lSudGtgbonirPg5TDqGEbR5sBrKyFQY8sHFw4z7aCOGHS04kt2qNi6qdmai9kw3rRdUIpjj-v3E2M87BXnaTuSQu7gruWbO0oEoqT77lVoJugErSnlpiEX9vdFQVAJ7vfTr267u6ZnPoxaZkOphSdOv0PhWm7Hy6XxkX-jzyEuegQ_oHYq_BcBUep8xX18erQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=XMO0tZr1_EO8qfLtWmx09KLFgUggxTUYfmfuDjtTj6TuP3T2irIUDk5XTJ8_Xu7roTthe3koDGBc1TIN2kZZVdddVBfSnpz7oAtXFZs7TCYeGodSTg5Z8x0xsGOQQmBoi3Jq6Tk-aLWHxUwmY9Kg2lSudGtgbonirPg5TDqGEbR5sBrKyFQY8sHFw4z7aCOGHS04kt2qNi6qdmai9kw3rRdUIpjj-v3E2M87BXnaTuSQu7gruWbO0oEoqT77lVoJugErSnlpiEX9vdFQVAJ7vfTr267u6ZnPoxaZkOphSdOv0PhWm7Hy6XxkX-jzyEuegQ_oHYq_BcBUep8xX18erQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/be4-A6RCCgAf2c-hW240D2pCLmx6E1NCxEt3yWduSwU4OviirQCvVwOu46NVtEdnIZpAFFf0L0RIp6qaorh7h01NaXLZEasX0G51VrTB8RwbWkn6BviTHZvhT0M7lg6C1v6ghPJKbcXErBhL7Mx_aX2Vpf95siICcfs8MJxQDMJCdbpMiqaxkZkXwahBrrIVR_BmAUfnCIUivkyxIeHGhBGP9XgiY115kt8KImWk2vQjURRH62WBRUSrBbevDmkOlbXUKlBl4ihOpmx7KJPrVZ7S8STN94-4FnoZUPsnluOyfjMtjQemYKn-bUoa-4WyZf95ZHplJijp887qtW2O7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=eS2u0WCDvDz77zTDWOfxkI-nDlZyX8fXodXkSisaR67ByhqqrQOCsjZk8_Mnxwv7y5Am7E8ibay_m8kR5MAc-2Rr0gpkEj1TQ4FPmlP-YX9mfmqK10XaJKY2UrOfTtjCU8YUPUHDfHwrt-zSWCHgGDbnpfNBbxjDXpaE2qMcT5E0B4MpZ4owThLoN-S52AINuHrX49RRFaGj8FYNXdf40YlBp82EUxlUk5r8_AFf2jUIaEUfuZmN68_kqns1SlRmmweWR5jN-SplWs8iAauBJZJbnbyOxLGr5LBZGc30VoWz5qWbhq44IoY3ejvCkCXRsRwlx10cfxcn9nyc2WyOGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=eS2u0WCDvDz77zTDWOfxkI-nDlZyX8fXodXkSisaR67ByhqqrQOCsjZk8_Mnxwv7y5Am7E8ibay_m8kR5MAc-2Rr0gpkEj1TQ4FPmlP-YX9mfmqK10XaJKY2UrOfTtjCU8YUPUHDfHwrt-zSWCHgGDbnpfNBbxjDXpaE2qMcT5E0B4MpZ4owThLoN-S52AINuHrX49RRFaGj8FYNXdf40YlBp82EUxlUk5r8_AFf2jUIaEUfuZmN68_kqns1SlRmmweWR5jN-SplWs8iAauBJZJbnbyOxLGr5LBZGc30VoWz5qWbhq44IoY3ejvCkCXRsRwlx10cfxcn9nyc2WyOGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=Qg34Xi_sj2sboUOUpkhgK26CJ6eJvl8s6qX3dc6Z-MTJcbAQW7KwhuBcRmVgvLcMigp0yv_k2uFBvDStC5XsBnSMUDN8Cvg1lHH7XWaLZIaclInY6cjDzja-cr4i2sTAmDkNZSOSbc632z0agU1FmYu3Gyyo5feXyaW79TZh3XH3iIpUWRGVYrtWXsE1KOkggffyVm6pQYv3k2BwbyfPST6FP_8yUE93tL_YVEVHcRcxT-3e0nwX79bAb6kFgeo5YhGjPlKxrRbFCRQsMIaEtpqpy_pXnsQSdu3aIDQHApnXykP_mve5XCnW8754xdg7kNuFjhutyAQPhvXKEQw4Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=Qg34Xi_sj2sboUOUpkhgK26CJ6eJvl8s6qX3dc6Z-MTJcbAQW7KwhuBcRmVgvLcMigp0yv_k2uFBvDStC5XsBnSMUDN8Cvg1lHH7XWaLZIaclInY6cjDzja-cr4i2sTAmDkNZSOSbc632z0agU1FmYu3Gyyo5feXyaW79TZh3XH3iIpUWRGVYrtWXsE1KOkggffyVm6pQYv3k2BwbyfPST6FP_8yUE93tL_YVEVHcRcxT-3e0nwX79bAb6kFgeo5YhGjPlKxrRbFCRQsMIaEtpqpy_pXnsQSdu3aIDQHApnXykP_mve5XCnW8754xdg7kNuFjhutyAQPhvXKEQw4Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=n9RZyw2xmzsxGIsqPL4AXO8NGZBNhJIfzOAZ4O7dQIgR92di6U85F9M5LXkJHJweO6YhAUZjb4XDmXcM8I1lDL3KzLvKBPnLkorXnoxS9d5N0rO8vAnbiAxayEsjJ8W6R7_zB0p-s_LkQsofIV-Wmv69aDtRtgmh3xOu3JUYjchdn4CeFZU_sl6tuw02Y9wLybkW0ZnMufnbkYcr43M-3RsfwHJtsF2aAlX9qbF1ATE0LRfM4bcxjWnvLNvTtS7tEKfS5Dqhj_tVunL1_xlGDqGpO_S07hWkcrxyShfE6ywAg7VKCg4UabCBjQXk2o6uST2cg3sU0y4Gvw9jewX7bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=n9RZyw2xmzsxGIsqPL4AXO8NGZBNhJIfzOAZ4O7dQIgR92di6U85F9M5LXkJHJweO6YhAUZjb4XDmXcM8I1lDL3KzLvKBPnLkorXnoxS9d5N0rO8vAnbiAxayEsjJ8W6R7_zB0p-s_LkQsofIV-Wmv69aDtRtgmh3xOu3JUYjchdn4CeFZU_sl6tuw02Y9wLybkW0ZnMufnbkYcr43M-3RsfwHJtsF2aAlX9qbF1ATE0LRfM4bcxjWnvLNvTtS7tEKfS5Dqhj_tVunL1_xlGDqGpO_S07hWkcrxyShfE6ywAg7VKCg4UabCBjQXk2o6uST2cg3sU0y4Gvw9jewX7bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TgbQ0Tss6gylG6wXH5LEaIpghgT5N6NbcLaMSlvuGB_vlFNkcFwVW3I11tREzPNuwP199TKBQWj23owA4l_zQDNNy9Ha0SIupj5SOgxdz3jZAArCt1nwUexlMMF0apV3GVdUGbvV62M_rrIoUAtMJKeygCuooZNimijV1F_dRKqLBz07Qxuoj6-ZgmHKrWZOdQAJJGlxSdB7msJwt6b4CiNBoBjKzbEucJM4APXePW5Wc7dPDZDeOcZ3XLd6RORp0dGfa4yv6et6Bmy0WTOxuvu9fOpLHppLgKxd1mqx5mx1Y__Wn26naLF8cR1H4BsOQHz8wtsDBOBeKvZB8oRnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LRPseH_P8vXnvQvDLIlUlxHlJvnB1BXmmLyjWVuZt7R-Ow-2ob7xeWo6raAg8f6jbyVf3Ylia8CROY1UWv7LmYzmPdl6dNmJrluHAqu_2gK8N-HG2MKbOZMrpLaFdfD48QIs628HJ3SftUqU5iRizLY8eBGR8EkbFWgD89S1Dc1ON4Xqqk1DGfdae3Vgv1vzIEJ-avB8ylSwzGL0Lo0EhubaJBm9zcuVJRZLjyuSgeOkYmtpO0e9jtT40h-lyIi7kBznhs3QM7OXTqZz4exd_qYd4GaKF_Xefbafrrt1NHtfr2WYOoryqBRO7mZj4EYGAFbt4HK6fEad-c2X00rDjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=m8wcG-UZ_gYcXb6WRBFP3NQcefqRUlD9Ua7TEdIQXY05opZsoYMOSc5fjcKZTuSuXiE7nb2SHdZREmmQ1NHvIVooaUuCjz8uct2FUY_aILa42TRZsoSwIdbW8xyd_KMcsDr5XTfVALbEIpyoCaXdg00mpmodd7K9BlDQsopu4g9ICejiy7OpjRrgQp1IjeYJt_an4ltvy8nLWusxJj7H8xzKkyKOTyP0V76PJoLgzidH9eSr7fchaPDSMbOGA2ylYZp6N6UXMd_hWocsB8Bw_HCQUux8DX2K_9uQno-hT4ElxtHScHL77xlmZl8exnLWIRYGFlMBCyFAqQ_2R--ZyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=m8wcG-UZ_gYcXb6WRBFP3NQcefqRUlD9Ua7TEdIQXY05opZsoYMOSc5fjcKZTuSuXiE7nb2SHdZREmmQ1NHvIVooaUuCjz8uct2FUY_aILa42TRZsoSwIdbW8xyd_KMcsDr5XTfVALbEIpyoCaXdg00mpmodd7K9BlDQsopu4g9ICejiy7OpjRrgQp1IjeYJt_an4ltvy8nLWusxJj7H8xzKkyKOTyP0V76PJoLgzidH9eSr7fchaPDSMbOGA2ylYZp6N6UXMd_hWocsB8Bw_HCQUux8DX2K_9uQno-hT4ElxtHScHL77xlmZl8exnLWIRYGFlMBCyFAqQ_2R--ZyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=drS2-noQDH9sAZ94vHwo9TK37ljxxGfkXS-IDa-UwMjS8yI6ecGH98_C8uznS-x_SqxBIlsmfh2VYrm3uKguqXTt3jM-98jhmU0yI6_LCZP4krlPv_AroxtTcPOyOokKUdx1jYoUyuLKg3vuppQqQn2ciF2hybRVMQ-xRLiisbrDJKGO2F2nt2wX79lr7mhRS6Tibge_8lTW92MPL3vFDh0V7oFfcCN7w65ADSL7EzUnYHvxO7AT0Vh9D5AJAYzIdIPMg4whqZIZCG6wLWNl8qJ3raKEgMNisi2OXtfdanKJLLrg2b418ANB-jlxvUOU2Oxx2CTrTXhQH3erlFS01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=drS2-noQDH9sAZ94vHwo9TK37ljxxGfkXS-IDa-UwMjS8yI6ecGH98_C8uznS-x_SqxBIlsmfh2VYrm3uKguqXTt3jM-98jhmU0yI6_LCZP4krlPv_AroxtTcPOyOokKUdx1jYoUyuLKg3vuppQqQn2ciF2hybRVMQ-xRLiisbrDJKGO2F2nt2wX79lr7mhRS6Tibge_8lTW92MPL3vFDh0V7oFfcCN7w65ADSL7EzUnYHvxO7AT0Vh9D5AJAYzIdIPMg4whqZIZCG6wLWNl8qJ3raKEgMNisi2OXtfdanKJLLrg2b418ANB-jlxvUOU2Oxx2CTrTXhQH3erlFS01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qO4GOjAGihHcARh2ThNsFTaIn5DyTEu16vGPexEKT2hjSmzDKGtDGH_USjayHVXeoIl6MiZcJ2IvwFBaE00LvPI7RYyHpMWCCc-IZAh9OPlmxGzOHMqzcfRf9iREZiWWluhnQ_6eodmoRY6AXHVTr-dbSZaM9_NQvSKo9uBIUPcXT0HLsfvUDMPCIsbxnTxPFKCvTIXwU41V_dllUt4snIcSuXy_kNTPd8r6e_jqBD-uFrEwPYuXGm5zQdoRQSmta2UrHlC1k_AoL5_BN7ixybljEJeZl8YJOxhQ32C1XxyCTkjGQJWKVhKnfUTz1xrT6lE7Z1CgaEaV-3NlMCaYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzCm9P_dNGkZcr-CglR78yC3-73S2W-Airn1D0cZ8fTRQPPkClAqbyhxLu8n0qHBJJ-29WdHALvBhcyquRAIcvMsmLtFh2bGBP_G8O5zh2No1a7re6hJckelK7gSioQZT1s7cq8cdubVQTnh1PobTZq9b9xUITNBc0ItDuXW0IbqPahtI28OkAEoqRC1YVUlM_LqdF2sbs7kBEZZ7-n4GVfsQyd3jl-3W-Z2UdCBR8JW7uq6TRS37iH2vQuescUaCCPyheyFtDTB7UX2oKJO3bRyU8-2JnLmZktjkQLF-dXLz7LaM1DuHVWEOBe33nz8SESieQfZq17c7chhuBkjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uCW2515BEt_K8x_idxo_ddNPHVfmPbm1s9Av_-Z9rPVUn62S36ZOp6lJc1bYmR34l-vOu7MkTXq7Bx3SveD9PLlXXKQTsaROYT7nKUVLZHTPOfqcBEPDjpUPWpEe2Sv6GtlMc_FxE1CFY0FRdxrNfIOepRPAHczKw7TFlJ1WExJ9G92KML0pomSD7mSc_hVyEpuAdz_YrZvOXDnqD9d_cLPLnNiEuNWeVelO0rY0Y98lZxGYXze3VwdcOLU_FYWpJ6OVR1cdUAn4li_Ma7PRVjB03LGEp_Lc-vPdOqjGCUqE6ZHLcoWiV7VyZjmOr1kEKpgmqGVwWVpITS6taq5K8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zd22TH8g_jSRINiUuK3666eRw9ZpYVBb5Q7HYoZUhh3_tWbdbiVITJWZE0JPcqwBUtrU5sNX0OB7xQZ0WWaEZiA4iB3ei0JvFFPa4SAfeLmPYUZB_rmeUh9BP4Anu1pZBxPG13ZXc9f2vqSq1G6vbZ5INDCi4gMQOPo4gvRcTeSzvxw85j6uAsJ0BzxVAPmOtcAMsVhH-Ttyrd2LiFtQtRLfXGrDzh5vwKecBRhIYUfeaTFGgeSp12az8YNYQMkTVOsbx-08IyKmP0zxjCn1O1Z6JuyYh8XiNRkhZUuEXvBGF3jOWMqFo6Q_lqPcP6xKeYdXWrcHfKNAFkG2SXrNJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryI3I7W1cyiQqGiZZm14WhUpK8L7KW8EcECuFsBu8DipoDzXTjzWvZwIUpmqX_eWZu0uVjAIClMPeAwODqs8SfM-uVkEe0_fNEYNEZuISv8tNJv-Z9AyvsT115fjAsNokuLdGFJW-GE5nq_7hgtNLx3wLmLKp5DESeAUZnyHZ8NRJW31wYmQV3FzcseYv9HIS-H_4vCdrAvUEq6mNAl6fnuu-VLlsaKOol4Yhm3FqDABCVzrw7sLSGf8twhFeQotDxuWP1CJe9lE7g_2Om6bx7NKQO2EQfGolEJPUJ__Rp9wbJkuooIJ0ovdIEntPtrBVz1S2DJpyKW_QlE-OEo-2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9UG3stYrG5inxJS-1PHqAwz6_PFT1QP15n59R5O3jBGnyHqvR6qKldWL70oa0NzAYcNWHuhBgnzd9JflGuugz93LAwJ0jy7WzPKIWh9kBhBfcBBEqQuPh-d2Q3xANieLcaLQ6u70E5RoDr2e-_s6WokGtnAEbKzMrM7GE-_igb6lBE5GrjvdxtnBIicEF7jVkIoDi3qDoRAhJoTPHm9Wgp8WR4kxjSAV5BZ6Xd556M248GoFKb0UoFYlLrci1_92FxEHwwJyj78n2CHgv3P0hYUNHZ1KBibU7GS5Rkp8xp4-pMdi4QH-hu4fGvVKxZReCizVgcn46weaWbMHCIRrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=hGSCAUiR5uqzQPhCT0UDQshjnDrhe5DK-BJUgkd8zUhkrPqqgtDlCdknZnDkDzH0H_V9PrYP6_bmxCzwh0uUMT7Iwb9eGCNuttrgWTQCEsSYvVO6EJ7zj7aKMsEaEcPrYSmOgHSFXL6G6Rn8sF9VYcJka8iqzBr5ZPgsdoALSpid_QlS9nk-oe2Y8ANfoApx3NSJ-GyB-68BQLlcCKm8xFT4q5To2bt2vNnjWH7VoTVO6Pq-x7LVfwckmlQ-xbv3vx-tfvWesoUFB7dkGWcgcqvWsy6SL7copkhlUoM2eyoCwJHlPCSm7ZjOJjvBj9AsGErQ_5qqJ39bSGTQeq0k8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=hGSCAUiR5uqzQPhCT0UDQshjnDrhe5DK-BJUgkd8zUhkrPqqgtDlCdknZnDkDzH0H_V9PrYP6_bmxCzwh0uUMT7Iwb9eGCNuttrgWTQCEsSYvVO6EJ7zj7aKMsEaEcPrYSmOgHSFXL6G6Rn8sF9VYcJka8iqzBr5ZPgsdoALSpid_QlS9nk-oe2Y8ANfoApx3NSJ-GyB-68BQLlcCKm8xFT4q5To2bt2vNnjWH7VoTVO6Pq-x7LVfwckmlQ-xbv3vx-tfvWesoUFB7dkGWcgcqvWsy6SL7copkhlUoM2eyoCwJHlPCSm7ZjOJjvBj9AsGErQ_5qqJ39bSGTQeq0k8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZyJ22ttDXaT9P_lzd3djOgdnP5xzRGbZWr1ZPXduQP0lLah24154_yHpq0BmByZH_K5R3Lf1EnbN_-VIa13wz3GrujGv8yDDbSlrCICohBt3osaD1zmKt204FVRyHlGM2DOoYHGv2rB337ZXWyu71i-UNb8wr_MIDx-HV37hsX7n9cK3MpYr2f71FBjuBn2MOwyZv-FHmk18WY195LxeSE8J4em6HCkT6fCy-xqgvro_QOztJEMusMVmfd-PKa6TNDWtzwniXOUjqw0dPTEZ2Di_BDwq7tXmM7ZezWRwOOKEnv8ZvQPnhNXR0uGoQCjVw38h84mQHSH47Zyiz_0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGXymNLeDvK-fHOTlPGAwsCsKNBv575qrv3fvVq3lvJelcRSZHTBB7K2reTlzErTGSTg1xUSdBOujbv-VEQ1OsYkluDBRcHaj5S9QpeyC9Z4SQc1FSIoEiIYOKf2u65oEZad3p-udD2Cb0K-LGM5glG2HHhxpQWk2m8xeOP_Vke-pkvd1Hr0-UyAOaR9V--Rzc1KQ3PS9zCG2bmveXumu9yMyrV-1aiahSktoFXL92Fcudcd3J_cO1Ib60iVztSC7NUiEagN9kxuPrnnQGYCw0_AbhYf1MA7jybcATv36W8FmOXLv_zxKKg8Th05FAOtXaRJpgY2SK-0cRDMP_lk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpPRVZ7kCtWirGrNkQl_3xvhmrwWzjoKSceYwLZe4cB-g-GN9IM3cs1f5Q_4sl1u_TwBNX-qVtc43C_MhPpOqlUHa8b1A-Wy0q0R6aR21qOfeyKZ-cEwZZ1bBBOg7UYKWw1D6Z0gEOB5blg8wHVe_bUA_7JkAX523G7i5bQ_5t4EGTANT6C-NiBNUdC8mWfhdmVkFbmauZHM0gJjn_Qehekfyctt-uDm7I1qcvOGJCzUS8jCVwM3BAxraygm8vLKUyMYOjWwk5OGkYSYMkW-USMBwenjvQBj1KEWkDwRwNvnGpC40JI7axLRBDGRd4sH70ScOYJndHoqjYt_Iaa9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⭕️
🇺🇸
🚨
🚨
ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5uVs5yw3s1HtHGskJEWEHdDIp2XcK1Fp_Oj1SYwhg7xTcYsjK5Kh8oSq463ljBetxpnFzU6dRWT6Gx5CzxDxXxhWTUkt5qjPz-NoHkLjONiAp8irg_oCD5Rq_f0Xg7QfVd3W4ckyxjHcvh71wuIOSaE-vqC1noo3ygZ_SUvfeP2d8QAvDlJAy4qU6U95LaCFk8pERfn1fo8n1QQjHyqPf7y1vuFk4yjVojfXpgnI_ykhXiGLvB9CVM3frgY-jDAcAbU-HfZtGQbyltsG9zhSKFb4Tb3b0Tmv9E5HFZ-HVy6wYxb4BVlmHMbEbPCvk8QmZBKGUBAguSYKrnfiLg4bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cADD8Cd2hhYndGklLVRwfkK0-ktYAqwTlNiWvbFm7r2S2fIGD417lYVeb7ssKjzGdnGJarvW21AArXABlyGHFPDHQVpZ9hdHT7EqE3bdMc8UPT_ue531Rjn444Bk1czOs7UNGVtwpICzTpJkJhiNXtOuZpTqEqNh6zNm-PYokqvmJk_2azF2_R0lxyfhP-a5p-I1LYufBd7b8FH7OJ1bAI2YAWz6gF6WQY0kJYvbZ_ONBOJhGJhxkdoDveMBf3kpEgTetojeOFeVa4FT9mwVIqZJzYL6tWXVjlXBN_2lhhL_-MGXt93FySBvAB7772igQA96vDnAhkMh5APJ42OgJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX2mUaIRvPSRab6h4CEGGdI3-JVdkHWQXBkEdlIgUaYFgLVL0X17RjtxkQT34gGL7YkoZKthE3R46KGEwxLKxFeJKvVP11a4aT1fqRjGCDlzt5Smp-rHL544bfYYKFqlATqGjKbp2y-zTdxAan4ZdStWN7xAGcPjGiF0nKzKJqYZgUP92q-NXgeAh_EOKcI0Ci4fSQiigLYln341GtXLsrk4DklAmjj9pAQ8H_TFiO2ttcQZ_CGyl-XsGZSVwfKblGqqK36xM1CuQNhME3NTgsiGJXJVBaoCFqVfZS58nWL8WkU3cO7udORwVoI_QozanFFOmApv7khUfZBMNRmyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=PHlzMfQVb2OR_Srilnue8mcP0y9eFd-vkElGeXoXU8ZGFpUd07XnNchdzK_5ezPGfVZNpDSS_4kfVEp9oXo-0IhrDySuOG7S49D6s64MGVwCP2r34i1JZAI2gsxAl8s6nGHhbg5jnhLOiDEOl0Ng5df8EMBpOTNldbweK3dr7Szk28-p5ZLyxy3FG2zvvFCj6SC1Ey7lBOG93eoh97Dn3XJkSBVynaMiB-kaUhxe3qdbdhIV7Zkj-WHI6EHkMZ0aSF82hRogNwILut4WL2ZEcC_mKUG7qkvjzCb4VJ8zmcMtDi4kZ6DsdJCahdFlPmXcvmxBBJqxqO83kr0W3LbYYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=PHlzMfQVb2OR_Srilnue8mcP0y9eFd-vkElGeXoXU8ZGFpUd07XnNchdzK_5ezPGfVZNpDSS_4kfVEp9oXo-0IhrDySuOG7S49D6s64MGVwCP2r34i1JZAI2gsxAl8s6nGHhbg5jnhLOiDEOl0Ng5df8EMBpOTNldbweK3dr7Szk28-p5ZLyxy3FG2zvvFCj6SC1Ey7lBOG93eoh97Dn3XJkSBVynaMiB-kaUhxe3qdbdhIV7Zkj-WHI6EHkMZ0aSF82hRogNwILut4WL2ZEcC_mKUG7qkvjzCb4VJ8zmcMtDi4kZ6DsdJCahdFlPmXcvmxBBJqxqO83kr0W3LbYYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWhcYy3QINJ1YD5QdHY9ftaieqjZVsOKW4bF98SgqIjQh4wHBROv74Nb02ybB7bEtSZsYSZ6qe-mwWAeBUt1nS0E8PAQ3Yys4qcbSykgZd2v-aIj5qzohu-pXEP9zvV11qBQHOy-mRJGyMQBtNo4_g5CDnQfk9A822eXyx2wLE8ITG2_Eii5BKa8Ztsig0w8QFDLMgbZaUE5ky_hAYSE6uEAYVBl81DYvNYy3n2Qz2yOSPL4jZ9TbomFD1fBiNfJIKzaY7XiUaPDItuVYnWJtIAARDQSymlDi7F6XcwxkJtX4vG7f_UQdM7Ju8lQXW13_fb6XTLC6ssZhTFutvqKLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=n6ss5UCgA9q0KYsKU4z2MdMTfYALCV2ZF7MXkyN108Bi5_CzEogIixKrS2EuNQ4ypmkaYcLxUjzuZVq8x7YSuMcvCwwxVgs7LYRcWbefmM8SYLbyTDwKwJswEDOuS7VaxSwFeTBY8DXFsYRv8B24as12XvE94u7Ke2USDAHsH-LEFPVgL3w89lVXhZyv78Ype0qKAp1DkXPyBB0QMHZjVACrtSHEKgepNCceWP24e1gVBff2mFPzIlTZK-mkYDgXR1zroYYk_lNBTwWAqZuBUAzykRouxi0ufxPG-d4tDq2W4cZOVZliGLgPwFc_8jiD2UUzcy4Hkk-k6SSxelwJbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=n6ss5UCgA9q0KYsKU4z2MdMTfYALCV2ZF7MXkyN108Bi5_CzEogIixKrS2EuNQ4ypmkaYcLxUjzuZVq8x7YSuMcvCwwxVgs7LYRcWbefmM8SYLbyTDwKwJswEDOuS7VaxSwFeTBY8DXFsYRv8B24as12XvE94u7Ke2USDAHsH-LEFPVgL3w89lVXhZyv78Ype0qKAp1DkXPyBB0QMHZjVACrtSHEKgepNCceWP24e1gVBff2mFPzIlTZK-mkYDgXR1zroYYk_lNBTwWAqZuBUAzykRouxi0ufxPG-d4tDq2W4cZOVZliGLgPwFc_8jiD2UUzcy4Hkk-k6SSxelwJbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtQxigjH1MO8Hd16peLjPeZCd9ogP2es6i_q0rxOM3gBa37x6jvNxL4QOYnOgrk7LFUu0V2GOP6nlfJ_K369ExEi317Yyxe9wPIiMw8m5CUNoEjjSQWkxldNacrcjNAGM1yS8RqlX3XOpysmF4i2GArHCaKU1-wPTNyLLsthnr_53Z9U0U6cIgWDGmkyV7pfBmUcLbWoJ3fwh70vTxVf31fC5T-nTriVUQLIuEr_cf5aTKFZxVVB5MNx046S0VS5yLPb74Qfkzfi4vlf9pzyXm4A5JynNWoWY0aMlNStGTA7EdsGmATmHIM2rXbZPQvk7MObg6tc9fAvRIR8CO_tNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=riJHCWnPEnAgY_qElpWqeRinZ5Ry_5jOC7FfZtd13HiMN1JXP0uch6bZkj9-iPAyxSzsOZeHrK1zXv5Au_zbb4cX7nCxKxtCZkHo0CQC235kgD2hY9U7e6mBi_cVdDCKtPZtaoTZQrKIVCl2q3t3bv3_vdz1iiQ3J4OhWcAqaizL2uuvxpi2xDiMmGB0i9PmOsg4JdZsOH7yNG5ug4nXVEtNJRy0n_hoGRhFRO3whWESxIKC8gdI5PjqXxOO8nagJpJdeKgM_FWzKU_V2UlJMfDgKBrBbZymlWpWGZc0ZBfbg20pFIw2ap5IEojGCPSGrYmxHsy6f8VDi-u2t7T56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=riJHCWnPEnAgY_qElpWqeRinZ5Ry_5jOC7FfZtd13HiMN1JXP0uch6bZkj9-iPAyxSzsOZeHrK1zXv5Au_zbb4cX7nCxKxtCZkHo0CQC235kgD2hY9U7e6mBi_cVdDCKtPZtaoTZQrKIVCl2q3t3bv3_vdz1iiQ3J4OhWcAqaizL2uuvxpi2xDiMmGB0i9PmOsg4JdZsOH7yNG5ug4nXVEtNJRy0n_hoGRhFRO3whWESxIKC8gdI5PjqXxOO8nagJpJdeKgM_FWzKU_V2UlJMfDgKBrBbZymlWpWGZc0ZBfbg20pFIw2ap5IEojGCPSGrYmxHsy6f8VDi-u2t7T56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=cUlpGq2tNJTH6Ubt23D5IasLYEsFSf2fueWs6-0FH0TJFjeJ0CuskTIOjb8oDvwYlbCUzsfakZhFbHVVP9kFE5WM3a9uScdtBfMNaXwnSUrAudBE8WHMSi2m0c7AWI1hdZt66KJCZwxSrL5Z6uAUqYhA_nfem_9YHhp5YN6ABvNXrIjfeRN1FMC81YYeMom5rjA3qYjVXfTaVeE4eZ4PUHtC35ykuezcfL2pWYndp2EFunOP76uzCdJL0d8lYk7qOnEUu8bhsRg3gzvKzTh8zFP5rSWnmsh_EymURqBz-k1uVqweYeg9wJ0yEZmM70xg3bURfSVl3xQzfacJel27dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=cUlpGq2tNJTH6Ubt23D5IasLYEsFSf2fueWs6-0FH0TJFjeJ0CuskTIOjb8oDvwYlbCUzsfakZhFbHVVP9kFE5WM3a9uScdtBfMNaXwnSUrAudBE8WHMSi2m0c7AWI1hdZt66KJCZwxSrL5Z6uAUqYhA_nfem_9YHhp5YN6ABvNXrIjfeRN1FMC81YYeMom5rjA3qYjVXfTaVeE4eZ4PUHtC35ykuezcfL2pWYndp2EFunOP76uzCdJL0d8lYk7qOnEUu8bhsRg3gzvKzTh8zFP5rSWnmsh_EymURqBz-k1uVqweYeg9wJ0yEZmM70xg3bURfSVl3xQzfacJel27dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQvqThnBrCJzG8Y7dcwDPsJB5VJEvCx3NooEuscL-At5402Tx3rcGBzd4xwTdOGoWeSSIzXPb354DwjNzmJPy-Q1QGK2y9zRJp1QSP81ZlSxgXAX256-vNA9dBtLmbVdHLd1Bcr-JURwBTVQ6jsx0avBg-jy0c1Qmj5sOBL2BvGx419DmKZNcQzHspuzJoTKsO605Bb809Bc4M8rtaBEa3EBP49aZ03TIB3eMtGwzm441UM5dscgKpAx7YAPOdWtd3aMcl9OBmOiV3izolPmSnNgKeWfpiFIvkZkmJ4s0DhFbQO-FnFoCYpcdkRO5XvwKBHswrpdhNqj3bxRRQoW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9-KDJbk4NZzP07Y1Q5lBYzskqO9prmP8moXAac02uY-uwhAMx6wXKLIWPDSA4wlr74se3xbiNRkVipB0YP7CX_cqbF3NxsWrw4beV2FRNpT7U1Gfqa7iRkvaCyLoP-XX44gj-V817TndsgsArTF236VHOCtFbfgEB_MlSSwN4DjTch8j9Q-lQDudP-tFM5EkXlQS0tkdy2FF40PaMaOOSr_elFrYZHKJeTmzLU-qutRKYEP2Ori-pocRN6eXCpbXXw_WiCmmBCHtbWaTodAtoJ4RpwZpQ7Pv6lznMVluD-0rElZ8BaU0jwPQdkkBlG-M81JmwS4Y9sI3qOgraWbcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9lwddVb79mZCV27ABlp2qP3m_YLTeoogS7MpSlYCoSvtlM3U0vBaLt4YUyP3O_mcI06t8b5MvIO7YGF6v0VG9AwuXKJIdq7CXMCJdTTBFw1O8nF_ey8T1P84M4dfTdbfR9nzAdfu6ZvZrf5uznVZoyU0htqaSDextjnU0U3u2duIGJ2dOT2UVVwbT3yLGWTdtKqztGEjG6ODw0cXMwmModgfycoD0CRpRQnY3gYrOudNuuTuKTgm6jOnGJrshsLW7q-DwyZUeemc5GQx7tQSOGzstw9KZKX_MofNL_X29nuI4A8G1QmYRUTzJ8YuOfHK_sO4Nu5aYWPsVxy7AEV7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FllSXOYTS88ik6O-WiVrSrfIlgI-ueHvax_xkulJH_n00KO80kweVUQrT6r4XGB_A5RljGy_0NYQ-ajaX_02wc3Peo_QTxTGPCP3KLTrdvsMda3ms7_zdKnX2quiXUeQzWFlfcJqXG175eSak7DbG-ifi-ko23sYUP29fjjAPDwLNtKkhduTxwuVf_U3Mijqxqz8bZxvw8Z9nsDxg4bUBYDQdlyg-uUVoN60Y6WWXqWzs6sxjBj-Ru_54NU2AoZRNWDCmL0NQGAHIEVKjlBhYqVVPmZyEbmW6Wvtl2AqDJ1BXGBcY62ppvXl6zU630tjKCiWjeeufBtkTr8kKpd1tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCBD26kAM8EnArNbBQR_HH1tOu8iv8OMl-GyIp3eJ1qtxsopFsprWQupvQjQ6U137EzrMWoH-LTfEcE6OeUJwk3-yFkpRBbTEnO_-Xo1aGsy1zk9ATN8x_lEnkr9GoXVJ_wDf-TsDAEr-J1BCiHSqVe7lgOoUcriwdhaZ2SNTGuk-Flir685YUxqfpDDSCcvec2rC3pVgY8ifRbqCGPcH3Ogi9vmOj5pwubcIbcKRQO0BRFnEgJhuCeu9KUWOCr0JcJfsjRXJFqRE0nJ_M6-wWyF5GRtCsmEhu-Uv014lPX2_-ykWXaW27UNfbTmQbTyAI_PGcbjpXq59jRma0e6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GkvsE5wwdI1KLawmvsMq1wu2V6zsUCQbFLiLa6RjLVHzC7j_jkRNCwJQxnXC4Nabc5VcEmnKy6miDnWoksQ1tNexPtXD19iAbU49B0rZKUV8hu0rVncQIy8rnZTfOzRZPObYfAsvgQTzk5KXyedB88EgdIcjq74LkZxE-2xdTN-_ZlvWjgYwD-IaiMHnVlzJQ9C_egoomR5vod57vxJpoXUmGF4uh4M7S2LsMsuUBvuWP4G9ejjgsTtdBZfpsEeAJmvdlDQzvy_UUrT-2RgK7PCtlZU4bKTfE5i9xADnDiCApmoqSb0JcVvUcPKbi4jPxe11K8Pz5aELjM6d77ANTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id3j0vHwIRCoo42RX_76g--fkhPr_NMIB82jsWMVXg5NcqAw71GeRSp9b-z37xUTuxMxorfCfd81iF4ageYljsGZatMzc9AK5KxVrLJ8Y0xFQRa1fBmWLYcZ4kHPqXYODYw8qS1qAfpy-hkX1zDhbWCSoHU-yCMthRk41rzHBnBVrLbMBDVqhA32_8FZK17j_kMSyPl7nY_3NkcbC2y27-bpUUQWHh1e_xZXp6Nl7oCCzKD_R2PK4k4S823YKEz4GSp-DvgNGa-t0Z8GBtTxGwoOwE9GmLwP9rsHtYmjeQe7AcVPtu2Kfr2uJGjtrWiLDy7nE2T0IYxwB3XML_Pyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نت خونگی.npvt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/news_hut/65089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
کانفیگ‌ها و سرور هایی که بصورت منطقی براتون وصله
،
در صورت عدم اتصال می‌تونید گوشیتون رو بزارید رو حالت هواپیما و بعدا امتحان کنید
.
🌐
‌ ‌
لینک دانلود NPV با نت ملی
🛒
‌ ‌
لینک دانلود مستقیم برنامه از گوگلپلی
🛒
‌ ‌
لینک دانلود مستقیم برای آیفون - 𝐍𝐩𝐯 𝐓𝐮𝐧𝐧𝐞𝐥
🚨
🚨
🚨
تعدادی از کانفیگ های V2RAY متصل منطقه‌ای؛ یکبار کلیک کنید همه رو کپی کنید.
vless://392c0d0a-157f-4fe0-b528-11586477cbe0@185.213.165.81:38024?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.80.73:2096?path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%258%D8%B97%25B3%2540WangCai2%3D&security=tls&encryption=none&insecure=1&host=sni.jpmj.dev&type=ws&allowInsecure=1&sni=sni.jpmj.dev#%40HutNewsPlus%20VPN
vless://e0a98968-eb18-417a-87e7-c8933aac5f13@31.59.40.53:52729?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
🚨
🚨
🚨
پروکسی‌های متصل منطقه‌ای با نت مخابرات:
https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
@HutNewsPlus</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbKlxR1b-qdD90L47KB8ez6bSBjjwf4ZncuYuI8a-KvmoZrfHAUjs2TVY1xKPrmUStIV0KnptxaYFuPC3l3Qqc5h7lp1srv4V84pM70rXtiZv426b7G58tGqqrUTB5iUghqTWBAkKMH8iXHi3S6eRJEDeNqTqHkCMdSRGAiBNiXiOcHC1HlZPDC3NBT5YXqTnkqfORJMEAFrnvTnFn5pPcrRGKFaLA1zMGdkvtU72T1wd_3t9jVC2NKN_umgjhbkn9-edJ3m7nJo00D-NxZzhQWFhRo36_RbUayY00nUvUDPgNrRnz2k-KEK_8QNC9TID70sI080QcUmS0uT6kY9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=omkvtRCq8o-1MD9UERkcXUwrffjHbwmh4zwteBVsl-Wamt-C4f_h6Q15CUMxGjc7ZOg0be8Pvrw_HIWSFOH7czA5Dn1x8M-v_ISrIxrpm6cJNyHJF4unsqf8nRFoY6p6BzFpzLuW6wVuWA_-soI3Xy78BGP2nZnX7HSXxwD9tHapTxDLliTfnpJVAaR5aLXxVdNFF57iN5neCkK7WDFO5yOmJOkBjw4O8E7uk0Y9nJkrE2NvXzSAGPET3IzFCSXO2LIHyBTgG6Z1EJtLKVOWcKssTtLQKm2_tmryaA0GosETOL4kzw_E5n-kHU0az6nKzPKgngYqyaCLev1PHrQR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=omkvtRCq8o-1MD9UERkcXUwrffjHbwmh4zwteBVsl-Wamt-C4f_h6Q15CUMxGjc7ZOg0be8Pvrw_HIWSFOH7czA5Dn1x8M-v_ISrIxrpm6cJNyHJF4unsqf8nRFoY6p6BzFpzLuW6wVuWA_-soI3Xy78BGP2nZnX7HSXxwD9tHapTxDLliTfnpJVAaR5aLXxVdNFF57iN5neCkK7WDFO5yOmJOkBjw4O8E7uk0Y9nJkrE2NvXzSAGPET3IzFCSXO2LIHyBTgG6Z1EJtLKVOWcKssTtLQKm2_tmryaA0GosETOL4kzw_E5n-kHU0az6nKzPKgngYqyaCLev1PHrQR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9KOmjAYeuuGK3eW7MzAHkAKy56fRciJ-bYxYSKAfcZjAe8uUBqzoTKwoA3Iq35QRc92IHmfX8LcoM8Cfb6LKrKrzb9iZNR2RK4kDFOSkhmTYPbQsoY5x4y4D0W_LF0l8MrVRCl4Hv-I4mBdk3lqPCtc27B_jtoCqtRhcokZcLuovrDufB39Q4fowjfcXcMlzP-47IgTVoXXOn2o8z-OmNvjGB1i_gq6P4NzAD3rYQJEQWwbbCRwzdw-XaiNIMxbTur9aNB-MlsrsfqnNZk4e2rBQFPde-BZX9omKveVoeTAU6VWzZ1H_dAvQOyoPHQglGYv09AvezNTALwnRbouNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmdi</strong></div>
<div class="tg-text">درود
کسانی که نت مودم دارن میتونن با jump jump به اینترنت وصل بشن
ما هم بعد از سه ماه قطعی به جهان برگشیتم
بر باعث و بانیش لعنت
به امید آزادی ایران جونمون
❤️</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65080" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65079">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65079" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65078">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju25bZDj_605H9xTjmLJiuklREM3Ky3rAC3LPCLNh2VT8-fyHTbHJ1lm_yufh2DKyCjiDmjWx6kskUA4_uOiWIDQp75AJ2qMW8dSkxXs6wSig7rAZuIbLXcuF88Ljmj-qJU9gS0zFCI3enKhFgSmvWrcXBSgMVP-90dEn4RtrFrBnjLHrRJn0NKBNSEU93C7yZ-MpxsqtNxafhCmHVlbBk3-UOTpbqetFy9m3ZjWsEMoCydw4AqAx3K9HCz10NaMumwXUc0sPYQ0b9ljMXhxr-NyILqwpjY7H7KEfrVf5UdYuWjBeSq9MAPKi12hqqxNnTWC-KIky6X6C3Lcm-Mihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65078" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65077">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.   این چهار حروم‌لقمه عبارتند از: رضا تقی پور، نماینده مجلس کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی رسول جلیلی،…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65077" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65076">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2QiGhDW-THxWzeodtIymKUmYVkUru-NOTDfpiY3wjkjXbjPRDrRjGxGMPqCKGCow4fmLryRpF2HWR6f_sEnSKe0lZkOfjz6PRrHhQKIG3l_IBox9Ejyr5BxQy2ka7gjDHIFDglWXRMNBaeXMrxgQAXqNzVg7dmXO7jKlXZPwMtjKjPn2DVYvktOe_7s_NTZD7_i5Y9FpcvkRHSfGEO_0s_BXBbJcZsIlfeBF_jEdfWnKr4tGszqSPDj2gFPpZFZ4ZyfTh0j-xpxom3arGxLPCEqjvvBvKwQgNrBWMNXT2Ul5pJlmcQMubg-AeY6rg9690Hs6l4YMmvbtbw1baSQ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.
این چهار حروم‌لقمه عبارتند از:
رضا تقی پور، نماینده مجلس
کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی
رسول جلیلی، برادر سعید جلیلی و عضو شورای عالی فضای مجازی
محمد حسن انتظاری، عضو شورای عالی فضای مجازی
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65076" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65075">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه  @News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65075" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65074" target="_blank">📅 12:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65073">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=IJUhOroEopRzm6jaOC5-hmH6xvLE0VphVgs9ykcKo44hkE4X7Y-devD60htM2HfV7XD9xGMoQ7rts2PliCAv-dSL5i4FHV1wBaCGVlecuGR4DKplwb00qZANXXqOOKK-Ma0i7cdsJteoKSbxN6XTf5bA9NcKFW1u9dyPtRkfLpw963CPgSExKYuLPRJ_krzF_RfrjNUlBZAUsKff1YEWWqLu1F3ngKfUP9Nz3QYTMIe3byYdGljv0Upm0IyTh6tT_eUZIIo6F0sOYVqMuTumk_tE-1Z9Psz6RtfiLVYMi4diWWuzFQFBFhjIG1tUdOJwa_Jx81bnD0ekAzDlSGBoEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=IJUhOroEopRzm6jaOC5-hmH6xvLE0VphVgs9ykcKo44hkE4X7Y-devD60htM2HfV7XD9xGMoQ7rts2PliCAv-dSL5i4FHV1wBaCGVlecuGR4DKplwb00qZANXXqOOKK-Ma0i7cdsJteoKSbxN6XTf5bA9NcKFW1u9dyPtRkfLpw963CPgSExKYuLPRJ_krzF_RfrjNUlBZAUsKff1YEWWqLu1F3ngKfUP9Nz3QYTMIe3byYdGljv0Upm0IyTh6tT_eUZIIo6F0sOYVqMuTumk_tE-1Z9Psz6RtfiLVYMi4diWWuzFQFBFhjIG1tUdOJwa_Jx81bnD0ekAzDlSGBoEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65073" target="_blank">📅 11:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65072">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رهبر سوم جمهوری اسلامی: سه چارتا جنگ کردیم همه دشمنان‌مون رو تا ناموس شکست دادیم جوری که ویران و حیران شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65072" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65071">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
رهبر سوم جمهوری اسلامی: پدرم، علی خامنه‌ای خلف پیامبر بود و بعثت الهی یافته بود(از طرف خدا مبعوث شده)  @News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65071" target="_blank">📅 11:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65070">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65070" target="_blank">📅 11:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65069">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LvdJLHLjZsHHFkR_EFA25PRplss1P7h0yr4cQuHM31ahDZkxspY4M6yyY-kd_SlSgs5ePzQQ5QI3aVtUW_KPp7KO9Lv07p6r2nsJvirm5yMEKWl0JabGMeLk3ZB9GJsYjE683wpf0TkhONfdTcO4KIWlUl2Wp2NjKRDpGv1mWvrTNFTvAZzbjPFZFIWmSnPd2DP_YMvChyD58el3w0FqR5dCx-wOTPWAAgd-mTAre0wRq9nfh8Y_8YPS6PQvuskS08gseXzf-RKWNv_UBcs2scBH6s7sOTEL4RfNKW7mUoEymi6fpTC1UnzEd78FHQ2MmyCAxJwWCLx1Z6qn51N2ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65069" target="_blank">📅 10:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65068">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A0N3iYAjQ_lMEnYPnPaS7qYV60Ip3-ygp7lYD-lxuO8jX0w3OvlLWPwG6Dd9UQSLy-q-ab1huPQIyBlm2QSUdkA4ViS80cR-AzuWtPDRkQccsR5lJAp6WTpYQHLi5lGsdgINvBQdDnzx5f84vz2Yc8jmk4yKRFDVJ2VbL55Mj2SmVFrpR-awEk9ZNmHMP4jWcJ6kuOL_pgN-i07H8vZjQ679guWw2v9zepC2Fzb_fz5sVjX-8Syh5weXXrogXJNSIUUfhXthkSljRZ0KfRJV8cPboyDxP6H3HmjReqQEJ-pKztqdGFRG_mk5r_d2XcADBrR3m0OvKq6F2h9fzXD52g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65068" target="_blank">📅 08:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65067">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S705iu6D_Rss1DKNZAnSiIrm2TH17ySIeaPtgzvwwvmMH8UiUp6HsD9B8ZXUAmkMScO4roAmpEn6Wq4ltLdhGD5qE2XMhJSDacHMvzQnD_BXLUbmq0NfqdcqyFlBiEej_Z5lkoQf6xQsm5UuuI5V4xN-J4BGrb0tQqQaBZK1FKfTNzRebZ8I3CEP9u_qJGDqc9gcTWcRl6Srar3hSAt_onckL-p28W95u967mnlIAg554CxONySi5QxC8X-DtdT4M8QvTQyztxM_IBLX0l7WgGYPi5Lydf5grK2RqjKtzlA80xVJ6daVa3dXEx1L7AuCxxzlt2vo-ml5HjMYHjtGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65067" target="_blank">📅 01:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65066">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">صابرین‌نیوز: امریکا دو قایق تندرو سپاه رو با جنگنده زده و ۴ نفر هم کشته شدن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65066" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
