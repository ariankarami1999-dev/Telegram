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
<img src="https://cdn4.telesco.pe/file/psBNEYzGOhjKhtYICya7om-37gmzpbKANDXURoXRMeFfAEZF2YOyKiQNskRRB4_DMW3dHM6vEMbfUKP4ti3bVJdJ-FeKkP6vyipk4cSN8f-aNGSliXYFSCoR5NxhUoMff5U57Tf5jc6G_llnDMhts9NA88gBmDt-ut89zdeerCs8uAkSA9foawYYgmMNxLBW98nHK5lg1zZ9HqhFNqkZxbD9UhBgRwkh3gw6BuIrsZdEapD1hzgV9hg5ccQDP-a5qr8mHI-3xv7DfWK_-R7NO0ve59edjAjSq9BFQ7F2MhkhKPp7CmXb6u_urgd-lEatSsNgbiBEoZ-AAnmMXcP0_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 379K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-17785">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزارت امور خارجه تروریست های حوثی‌ها در یمن اعلام کرد که «رژیم سعودی اعلام جنگ کرده است - و باید مسئولیت کامل آن را بر عهده بگیرد.» همچنین اظهار داشت که «رژیم سعودی در چند سال گذشته برای افزایش محاصره و به راه انداختن یک جنگ اقتصادی فراگیر تلاش کرده است، در تلاشی برای به بردگی کشیدن مردم یمن در خدمت صهیونیست‌هاست»
@withyashar</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/withyashar/17785" target="_blank">📅 15:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17784">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیروهای مسلح یمنی مورد حمایت عربستان سعودی: باند فرودگاه صنعا را هدف قرار دادیم تا از فرود هواپیمای ایرانی جلوگیری کنیم
@withyashar</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/withyashar/17784" target="_blank">📅 14:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17783">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسکای نیوز : دولت بریتانیا، سپاه پاسداران انقلاب اسلامی (IRGC) را به عنوان یک سازمان تروریستی معرفی کرد.
@withyashar</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/withyashar/17783" target="_blank">📅 14:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17782">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/withyashar/17782" target="_blank">📅 14:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17781">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">افشاگری ۸ سال پیش زم @withyashar</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/17781" target="_blank">📅 14:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17779">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش تکان‌دهنده در نیویورک تایمز:
بر اساس این گزارش، احمدی‌نژاد در اوایل سال 2024 برای مذاکرات سری در بوداپست، پایتخت مجارستان، با مقامات اطلاعاتی اسرائیل دعوت شد. او به بهانه‌ی یک کنفرانس علمی به آنجا فراخوانده شد و طبق گزارش، دو بار در سال‌های 2024 و 2025 با مقامات موساد دیدار کرد. منابع آمریکایی و ایرانی به این روزنامه گفتند: "این بخشی از یک تلاش چند ساله اسرائیل برای پرورش احمدی‌نژاد به عنوان یک دارایی اطلاعاتی است، که در زمان مناسب، بتواند به رهبر جدید ایران منصوب شود." این در حالی است که احمدی‌نژاد، در دوران ریاست جمهوری خود، برنامه هسته‌ای ایران را تسریع کرد، خواستار نابودی اسرائیل شد و انکار هولوکاست را مطرح کرد.
در سال 2024، حتی ددی بارنع، رئیس موساد، شخصاً به مجارستان سفر کرد تا با احمدی‌نژاد ملاقات کند. موساد، این جلسات را به سازمان سیا (CIA) آمریکا اطلاع داد.
بر اساس گزارش، اسرائیل به طور پنهانی مبالغی را به احمدی‌نژاد پرداخت کرد و مقامات اطلاعاتی اسرائیل در چندین نوبت با او دیدار کردند.
این تلاش‌ها در اواخر فوریه امسال، در روزهای اول عملیات "غرش شیر"، به اوج خود رسید، زمانی که یک عملیات جسورانه برای انتقال احمدی‌نژاد به یک مرکز امن موساد، به عنوان بخشی از طرح سرنگونی رژیم، اجرا شد. این طرح شکست خورد.
در 28 فوریه، روز آغاز عملیات، یک حمله هوایی اسرائیل به محوطه اطراف خانه‌ی احمدی‌نژاد انجام شد و هدف آن ساختمان‌هایی بود که محافظان و خودروی زرهی او در آن قرار داشتند. پس از حمله، یک خودروی پژو مشکی به محل رسید و او را به سرعت از صحنه حادثه خارج کرد. رانندگان این خودرو، ماموران موساد بودند که احمدی‌نژاد را به یک خانه امن و مخفی در ایران منتقل کردند. با این حال، احمدی‌نژاد که از این عملیات نجات به وحشت افتاده بود، تصمیم گرفت خانه امن موساد را ترک کند، اما جزئیات این اتفاق هنوز مشخص نیست.
موساد به درخواست نیویورک تایمز برای اظهار نظر، پاسخی نداد.
@withyashar</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/17779" target="_blank">📅 14:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17778">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یک هواپیمای دیگر ماهان‌ایر ایران در حال پرواز به سوی یمن  @withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/17778" target="_blank">📅 14:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17777">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg0N5HJam4CxR18NO7GcyuvWNcFbbDjtENLzLhKxUgRRiHDMCEFetla2F2KiUbCR_x6C6MZmMAj5X1AgyMa1Xg0y9-XfwQsNTpzv6dDY8XptcLFrk2UVSrqLYku7TvZrwUm98w3NJ6rskL4k0YhCqJw9xPBbEFa36z72mO8ZNrhB0eH5Ur8sZuJV7u_004ehVzrhcOMPbl7-5MtZN00gJLf9a4UCXMBj3ttC10PSOIb8uhaY-xRTRzpEFuLFR-d4dRglal40p5a1wBu_MrR2VTOSJ1kg6kwb5ce6N57bvMnNPHygm6sYfuVQiYfaKD6zDzcmaFG9L4uVXzwdC4nlaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود یاشار
۴ انفجار هم‌اکنون در پایگاه موشکی چمران جم بوشهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/17777" target="_blank">📅 14:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17776">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga8mWO4XLM3m8_QR3LZzMLLDQuLMJL0GngwECE1-uLjXA1MOsgIc0lwTQLRvfVxFeGlH7lz-8Md9mv0kILA0Kgg4ibnpuIdDbJrk37pPSa-BlMuLbh0gqN6Xiov9YhHihYVSM4ojdvl-p0zq36jfsWGngy4gFwpvFPtNsssJqPThEGmmLjjg2eVNc6V3WE6naQE8Xd2z_7Bf2iNFwJbkQ0X5nz-qKG0ZEaVTfoqkaLtwmxDCMpe_4hDnGxxgVqKTH9ywiGeahf7rGMDqu-lnNUx0EaIhxsycsAiPiZYX7Lov1lcCBF9_XfcjjHjKigDpwQqxLEY2kmz4drL0o1WinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای دیگر ماهان‌ایر ایران در حال پرواز به سوی یمن
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/17776" target="_blank">📅 14:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17775">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e8ca3a0a.mp4?token=MpvOMm-wSlhcfRqC_jI1RbFRaOCPGmJWd9rRM-lyLetmyngIQlsmB5WWdsV_1j4YFmytqbaWYKRogwPQ6BAEx1-AnKcnrmzyWc1DrCsW1ilsZEviqfCvvQBXn31lucDmiYQUqPXmLbw-K6dUK-uJjiJyuB3pBXr6CBh8my5nSow8ZloCq2f0HF8-c3a380U7Sm9dVOLQeVRp2PDnUDOmaqzbOiS-cs-GlxjKqW_MsWthCFXiILikPrJkslkcQ7Da2Mzk2-Jq4ozjlp6jCk_kMBYEN6ob4VA-Kawm_sCaQAuz54D7SshtbJ2r8BzMDmFaaYqJznul3wmeWdtG86hsGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e8ca3a0a.mp4?token=MpvOMm-wSlhcfRqC_jI1RbFRaOCPGmJWd9rRM-lyLetmyngIQlsmB5WWdsV_1j4YFmytqbaWYKRogwPQ6BAEx1-AnKcnrmzyWc1DrCsW1ilsZEviqfCvvQBXn31lucDmiYQUqPXmLbw-K6dUK-uJjiJyuB3pBXr6CBh8my5nSow8ZloCq2f0HF8-c3a380U7Sm9dVOLQeVRp2PDnUDOmaqzbOiS-cs-GlxjKqW_MsWthCFXiILikPrJkslkcQ7Da2Mzk2-Jq4ozjlp6jCk_kMBYEN6ob4VA-Kawm_sCaQAuz54D7SshtbJ2r8BzMDmFaaYqJznul3wmeWdtG86hsGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت هوایی جنگنده ها آسمان اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/17775" target="_blank">📅 14:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17773">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rt1xIjIiyLX21VnOiEG0NrnQANLApVT8BnL8_1qMW1vzHbpS32XgdQixWBTfCT_JpDklsBkp6iLooX_Ghwoqt0e9sn-vGcI2OKtWuTxM6hRxeGQ20gAvFfDKwQ9TPrihtHZOqbDblMz7Y38oVrZlslM8NfZcHWn90KvKcc1-_uriBQG50SBpLsHwM_OhFKbNzW7xj3Wp5nW58_Mj5oSrl8k6_2W2bTuaoyUtahThXA5PgYBsUDlmP2WHNpH-Dl-X2hR0Sfw9fCP54Z0oiawACI1teucBUYPRHle6BU85E40H_wFw4PU52gziGW5ar9UiaOj5CU9sPp7USvxf8zULBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhslbFvosOyW63_qYOCprMirTZVMJ792w0XYJv6wWYUIZirUDqMh2rbjuzL_VMlqUA9tW0Mf34Vua4v99mlAfyoGAPysq0HWb2mA5IsORWdFrAKjVMRiCe-txznGzBnBxd6xDW9AAs--oufOlmuW2eqKl8sXqGPxVPASl_hxFRVqzaCEZPauD9wFbWIxmkur7NOAu4WA-doEjy5MHz1RRiyHghp5XsnbfxDkOBlXEcuRdOaWKQJ11T3a_7AkiYAfFioChLaeeOaDoJIMd_J4KL0J1OLviABIyd01MYsV7Oj8Cib5Er53UOxpLNlzmkYwfDGw5Hma1xiVB5KlHTMiPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتوبان تهران قم , انفجار بسیار شدید بعد از فرودگاه امام دودش تا ۲۰ کیلومتری قم هم پیداست
@withyashar</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/17773" target="_blank">📅 14:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17772">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش زیاد از صدای انفجار آبادان
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/17772" target="_blank">📅 14:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17771">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شلیک موشک‌های کروز از جزیرهٔ قشم به سوی کشتی‌ها و ناوهای جنگی آمریکا در تنگهٔ هرمز
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/17771" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17770">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ارسالی : سلام از زندان قزل الحصار پیام میدم همین الان ۵نفر رو بردن واسه اجرای حکم اعدام
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/17770" target="_blank">📅 13:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17769">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتانیاهو در گفت‌وگو با شبکه فاکس‌نیوز اعلام کرده است که به‌زودی مقدمات ادغام پنتاگون و ارتش اسرائیل آغاز خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/17769" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17768">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">در آب‌های خلیج فارس و تنگهٔ هرمز درگیری رخ داده و صدای انفجارها ناشی از درگیری دریایی است
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/17768" target="_blank">📅 13:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17767">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تنگه دعوا شدددددد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/17767" target="_blank">📅 13:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17766">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دقایقی قبل پایگاه شکاری بندرعباس مجددا مورد حمله سنگین قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17766" target="_blank">📅 12:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17765">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁮</strong></div>
<div class="tg-text">داشتن همه شنا میکردین دریا دیگه صدا زیاد گفتیم بریم خونه با خانواده خطر داره</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17765" target="_blank">📅 12:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17764">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehdi_sp</strong></div>
<div class="tg-text">بندر رو بد زدنننن یاشارررر</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17764" target="_blank">📅 12:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17763">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دستگاه قضایی عراق از توقیف املاک و کارخانه‌هایی به ارزش 69 میلیارد دینار در پرونده معاون وزیر نفت این کشور خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17763" target="_blank">📅 12:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17762">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ارسالی از حدود ۲۵۰ پیام : سلام بندرعباس طرف پایگاه هوایی رو الان باز زدند. بعد از آتش بس بار اوله این وقت روز میزنن.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17762" target="_blank">📅 12:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17761">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بندر عباس رو زدننن الان شدیدددد
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17761" target="_blank">📅 12:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17760">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">امروز  هم رفتیم امتحان دادیم...
به امید خدمت کردن و ساخت ایران فردا موشک هارو ستاره فرض کردیم.....
💫</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17760" target="_blank">📅 12:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17759">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یک یگان از ارتش اسرائیل، همراه با دو بولدوزر، از "خط زرد" در نزدیکی اردوگاه باربره در منطقه الشقوق در شهر رفح عبور کرد و در حالی که به طور متناوب شلیک می‌کرد، عملیات تخریب با بولدوزر انجام میدهد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17759" target="_blank">📅 12:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17758">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزارت امور خارجه ایران: صحبت‌هایی درباره درخواست ايران برای مذاکره، بخشی از جنگ روانی است که ایالات متحده انجام می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17758" target="_blank">📅 11:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17757">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17757" target="_blank">📅 11:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17756">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">استانداری اصفهان: در پی حمله آمریکا به یک پایگاه نظامی در محدوده شهرستان نایین، ۱ نفر شهید و ۷ نفر مجروح شدند
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17756" target="_blank">📅 11:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17755">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ارسالی : سلام یاشار جان
دیشب پایگاه امام حسن کرمانشاه هم مورد اصابت قرار گرفته بود
دیشب صداش رو شنیدیم
خارج از شهره برای همین خبری پخش نشده فکر کنم
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17755" target="_blank">📅 11:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17754">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ارسالی : یاشار جان آمار گرفتم بهبهان رو رادار ماغر رو زدن. یکم از بهبهان دوره و صداش توی شهر نمیاد
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17754" target="_blank">📅 11:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17753">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نیروهای اسرائیل هم اکنون شهرک حداثا در جنوب لبنان را هدف حمله قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17753" target="_blank">📅 10:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17752">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجار سنگین دیشب در امیدیه @withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17752" target="_blank">📅 10:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17751">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش های از مشاهده پرواز موشکهای کروز تاماهاک از آسمان شاهین شهر در‌ ارتفاع پایین
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17751" target="_blank">📅 10:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17750">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcgD_6fB-jYaD6HcuXnW1ae1wbTGmQSUNsoDIuMSvjrxf2rRp7b-30m7NJJ-j2slCvn6E79YhMCSNzjilo1GNevP0C9TkmOIl8Gxu5gl2upaHtjxrCrNCkv60kvINLVfBUQtdQSUBpeXU5MPPT6EKPUZcUqv4MTNK_P24NrtUuhcSyLzZt0r3fhzzUZxkgH1ChPGkF9yX5yiUmDcHa-S4Z3_D_AP2cOEdGEwmxlClvNCoT-rNYrgJ5Rouev48hQOgG4uMRWAwrCofUn8Au1KULLvBvBduDu74iRNgq89p3Rq4BQFnQcq1qTdMcHLFaCx2NvnVE5PQQLbKpfpOIkofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار سنگین دیشب در امیدیه
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17750" target="_blank">📅 10:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17749">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f7f8cbe.mp4?token=rdBZb9_KVa5po_4vb1MTqXMniVdpfKvOKbFIk0MF4jVsveDFf1jxBLNLkD9um60sm2ni0-zO6DGKBAgJ7LwETc-hS3ycaa3eNEXhddJn42MnlbjGY1oibA_hq_eYpO8uEwEX9t1DKFjGSNZDUeWxgaSQNzk-vZqQDfkJeblb5Ea_XvFBzDC1B-NiFe6zFIDzqNsvk3BxrZivaX0X7OVv6ihzd9K-QbrF4JcACmz5z0iRDTRdVEW28jylyDhNoGKmoYKUn8yCPVv8iyPs0OAAb5GdCLVcb81UHTLi0VmEXyfWY6mvXq-MxuDW9b3PaBi36aEWDdS98x5fuNuZ7fmptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f7f8cbe.mp4?token=rdBZb9_KVa5po_4vb1MTqXMniVdpfKvOKbFIk0MF4jVsveDFf1jxBLNLkD9um60sm2ni0-zO6DGKBAgJ7LwETc-hS3ycaa3eNEXhddJn42MnlbjGY1oibA_hq_eYpO8uEwEX9t1DKFjGSNZDUeWxgaSQNzk-vZqQDfkJeblb5Ea_XvFBzDC1B-NiFe6zFIDzqNsvk3BxrZivaX0X7OVv6ihzd9K-QbrF4JcACmz5z0iRDTRdVEW28jylyDhNoGKmoYKUn8yCPVv8iyPs0OAAb5GdCLVcb81UHTLi0VmEXyfWY6mvXq-MxuDW9b3PaBi36aEWDdS98x5fuNuZ7fmptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : شلیک پهپاد شاهد (بهبهان)
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17749" target="_blank">📅 10:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17747">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جمهوری اسلامی پهپاد شاهد داره میفرسته …
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17747" target="_blank">📅 10:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17746">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZl77-mJlwD9W4RPEWe4aQPqF3idvL3HjTfWjUpNy2yXgFifGO_ukLPf-l8-ye9LlrLZdD8kcJCBDWZXXu_3Mv-wm91pOFJInLS4jr6iMik7m--3Psm8q38v5X-v9xZzpSUoJN0_appY8Omltpn2Ta63posLpamjx8LR6gjxYqbhhzpjJf--pyjqUhGGlOPs7nkcuO-b8Lb0By43ef-myIdNNLrNfLOzLml3weT_f8LtILQMTdlXN_GHRT1E4q4wA3O6LvgBVWjh1hGtr95DfDJrdNnJsFt-ixf1_Gw9_b5_jTJb3wV_STFmzGZ4_c_D6QePfxE2SqiAzja2VazpAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر کوهستانک , دیشب
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17746" target="_blank">📅 09:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17745">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL6iVMyy_5iRqaxCqpBOl0ISU09CvPkpd4AcoBwHbdPfF0eayoqobdTP7kwd4BOc7bw0qYWXKYOegQpmv3K9ST3H1Q2qs4z6CoZGeUEqY5oVi0pYZjTN8kx8uEnxH2-rb4zi2WMOhodF93-2Mg5FJrwKAqQ3lZFmc1_RODAEpvlLedxmlu0R5KhK_7o8C-pVrp4wSdMRP35wioWGyq8lNWPErqcTQM7y7wPbpj_YwV9h_8Y-RdFkdXARa6oaLUYSZMHrIN2SkVZZxQtlh_aNWMPe6sk1nlYtbffC_4iTMtagjSpwo0pjftxZ74Dk9b4_XKdM5G0NrNyDk4pZxmv1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17745" target="_blank">📅 09:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17744">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شرکت کپلر اعلام کرد روز یکشنبه تنها ۶ کشتی از تنگه هرمز عبور کردند که کمترین تعداد در پنج هفته اخیر است.
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17744" target="_blank">📅 09:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17743">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجارهای مجدد در  بحرین
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17743" target="_blank">📅 09:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17742">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش انفجار بندر دیر
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17742" target="_blank">📅 09:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17741">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دفتر پزشکی قانونی واشنگتن: لیندسی گراهام بر اثر پارگی آئورت ناشی از بیماری قلبی‌عروقی ناشی از تصلب شرایین جان باخته است.
پس از تکمیل آزمایش‌های سم‌شناسی و بررسی‌های میکروسکوپی، علت رسمی مرگ و نحوه طبقه‌بندی آن به‌صورت نهایی مشخص و در گواهی فوت ثبت خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17741" target="_blank">📅 09:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17740">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">روابط عمومی سپاه پاسداران انقلاب اسلامی:
تاسیسات و زیرساخت‌های ارتش آمریکا در بحرین، رادار دوربرد هوایی FPS و رادار کشف شناوری در پادشاهی عمان منهدم شدند
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17740" target="_blank">📅 09:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17739">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VueM-ByCER0uEs_8VAxkblRqCxQZ7eiNpq7TWakG9Hp5MF6GawOFOry1tYyH8uMnyaSxa6yras4vlJmbYf66qzbuv4hpcxH2axwLlsRt6_1hG_cfEl5VOPZ_azY2DtfnQdUXOlJ5-cWeArHviwP7a-UylZWXlPlwUmf8HNIn_bIuG_QmFpf9Uqa56RdwABcHdeQTqK_PwK2UE7wu4CVI1nd83qlNfhkqS14ANy60XmOpwTf5h8h9M86JYR0Cn-NFI7N-umrYdgNUL6gmSMtC53OEwBaKMGKCy78BBQQ5qqSzBCWex7qinat_uLN125Q-FSOimwfefcHXXdKkE4Lxzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث عکسی از لیندسی گراهام منتشر کرده با کلاهی که روی آن نوشته :
«ایران را دوباره با عظمت کن»
Make Iran Great Again
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17739" target="_blank">📅 08:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17738">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">https://t.me/boost/withyashar
امکان ترجمه اتوماتیک و ایموجی‌جاوید شاه رو از دست دادیم یه حل بدید ، اگه پرمیوم دارید!
اگه ندارید به دوستانون بگید</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/17738" target="_blank">📅 03:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17737">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبرگزاری سی‌بی‌اس:  حملات امشب آمریکا علیه ایران تموم شد @withyashar</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/17737" target="_blank">📅 03:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17736">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بندر صدای انفجار جدید
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17736" target="_blank">📅 03:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17735">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۵ انفجار در خورموج
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/17735" target="_blank">📅 03:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17734">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبرگزاری سی‌بی‌اس:  حملات امشب آمریکا علیه ایران تموم شد
@withyashar</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17734" target="_blank">📅 03:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17733">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8ecf8e41.mp4?token=ORaP1vX3XC2YkJJIrgEbyFrRfv27GQAAQz83ON5l15n9bJwy8v4_r4Sg7HgMiqH9zkCfunuChaDpbqfTZa4Fz0dYGclqN8_fLG-5E5eVQu28ITLmcGPGbwhv0nzDJ2S_6OvvTlrp4OQvbHQjxKKtyMvyZpReIDcbPHkuBtsG5tq48bHcxHIzJXDwJrrztZE8qPz2PX7m3XNK5Pm50nA7nQ6L7LcOmd-xWJ_XXFeDgm5IDZpHvaSLG94l9P--nNlaBJSbIQCZFfG-84MGCxnZYm11B0EVdm6NSp2qdEN3UqKAOdjX2V5awwTTdruYdy_PpUTxUa3L_FQAy_bZzdKqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8ecf8e41.mp4?token=ORaP1vX3XC2YkJJIrgEbyFrRfv27GQAAQz83ON5l15n9bJwy8v4_r4Sg7HgMiqH9zkCfunuChaDpbqfTZa4Fz0dYGclqN8_fLG-5E5eVQu28ITLmcGPGbwhv0nzDJ2S_6OvvTlrp4OQvbHQjxKKtyMvyZpReIDcbPHkuBtsG5tq48bHcxHIzJXDwJrrztZE8qPz2PX7m3XNK5Pm50nA7nQ6L7LcOmd-xWJ_XXFeDgm5IDZpHvaSLG94l9P--nNlaBJSbIQCZFfG-84MGCxnZYm11B0EVdm6NSp2qdEN3UqKAOdjX2V5awwTTdruYdy_PpUTxUa3L_FQAy_bZzdKqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیدیه @withyashar</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/17733" target="_blank">📅 03:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17732">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRxUVB4WexyZNO9NdDbCVo2RZ1tzPZy07DSZK2ymm7xAG1iKqPPfKaEUIt_l9lvnwuPjH1jXhgsS_UlKeX0BQ-HYbBiAP9YqcxGw99LqRPmXCel7vhO62tFuBdVyrpGvATdeMHj0F-wMOJTBpJBcL1ai3gx_nGA_AEuuxr2n7LEQh4z37Tjg9JjFb4KMo3t-EnS4QWgqTPoXxoIwlX9EnTT4PaT0dc9CdaL-kCjg1MMmYOh6RwI4SENWdITRYM_Wb44RkiAWHvW2a9S5ZU1qQVWG5J-kSBzzvitN5Jdq2NdYUbKCD0L6dqDmD6-CjWc6CtUs4LMHzt8lXUrTiMvBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۹ سوخت رسان در حال انجام مأموریت
@withyashar</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/17732" target="_blank">📅 03:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17731">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAnq4jRl_Jr0UgYqeKOgR9OuS0WUCv6x5Ondy9q-Oj_lGj4QYm1kqY-nQrjaToRSXSluvXDIlH_kYdlebIY8_zQ8XIRH63lboLS3QMQDAFuy9suC2IPBkH1EYR2N0f0iH4_b56al9HCj3m9mHhVlxJuZBWebsxb4PGD3zHWVaAAmAbjqnb61Z0CFJNmq03A_IS6Jy46drwjFytsDmZxBl0Dm60sT8z-sJednlxsh5da_YgTCTRkw-wmUPN6xA6oA6MkVbyy1BX-VUexVJ_4nYi12TPiY5Q9qNrAtyeDWntKtDMl7VMR_GMrUF7zwy9iDNTSJk0iNEQboSXErrCF_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدیه
@withyashar</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/17731" target="_blank">📅 03:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17730">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">افشاگری ۸ سال پیش زم
@withyashar</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17730" target="_blank">📅 03:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17729">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سوخت رسان جدید از ریاض عربستان بلند شد و به منطقه می آید
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/17729" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17728">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842f62bc5a.mp4?token=CqKfdrrh7K0onfd6OucBD58KkgQk_SzCSwiakO4aj2WZDEikl1Y8xGh0PpApQKaDk7ABDxxOluIf8yTBLhYZyTMTwzYMIZ4omVexLip4c-3bJpVKPfjPeCHVi1EKa635i-smiE01oGtfsKoTO6OXFx7DPQ2Ie7w0hNCdtqjNXaJQkVTq5EB-KrrIrIJAVnp_UWr72l2EgzWjnRzpE0BZ43BSB8nSXgx-5GddmSfyzYi7qVGZVeOPFF1hsbi5JcU5hR_mk3NiuZdKlwCwMAMu2qqGqnbc7Y_d6e4EtpR5mszS17_RTXJsRQsFMPW15IDvrwnO-JS9URyn9fAHVdN6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842f62bc5a.mp4?token=CqKfdrrh7K0onfd6OucBD58KkgQk_SzCSwiakO4aj2WZDEikl1Y8xGh0PpApQKaDk7ABDxxOluIf8yTBLhYZyTMTwzYMIZ4omVexLip4c-3bJpVKPfjPeCHVi1EKa635i-smiE01oGtfsKoTO6OXFx7DPQ2Ie7w0hNCdtqjNXaJQkVTq5EB-KrrIrIJAVnp_UWr72l2EgzWjnRzpE0BZ43BSB8nSXgx-5GddmSfyzYi7qVGZVeOPFF1hsbi5JcU5hR_mk3NiuZdKlwCwMAMu2qqGqnbc7Y_d6e4EtpR5mszS17_RTXJsRQsFMPW15IDvrwnO-JS9URyn9fAHVdN6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی از اهواز، لحظاتی پیش، آتش سنگین را در فاصله‌ای دور از حملات هوایی آمریکا نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/17728" target="_blank">📅 02:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17727">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شهر هایی که مورد حمله ارتش ایالات متحده آمریکا قرار گرفته اند
💥
قشم
💥
سیریک
💥
بندرعباس
💥
جاسک
💥
بوشهر
💥
خنداب
💥
بندر ماهشهر
💥
بهبهان
💥
اندیمشک
💥
دزفول
💥
اهواز
💥
آبادان
💥
خرمشهر
گسترده تر شدن حملات ارتش آمریکا نسبت به حملات اخیر
@withyashar</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/17727" target="_blank">📅 02:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17726">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مقام آمریکایی:
باید انتظار حملات گسترده‌تری از سوی ایالات متحده علیه ایران را امروز، نسبت به روزهای گذشته داشته باشیم.
@withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17726" target="_blank">📅 02:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17725">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۳-۴ سوخت رسان جدید از تل آویو بلند شدند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17725" target="_blank">📅 02:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17724">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">برق‌ اهواز رفت
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17724" target="_blank">📅 02:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17723">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حمله به پالایشگاه بهبهان و قطع برق در سراسر شهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17723" target="_blank">📅 02:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17722">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsgrvaL8JBIY8AWXbcfNwXfXXky0oI1ckI8kmBK7DE4YwlPvpNtNRafXSTiblntnSACMli-C2aAdwUO_wnPtiX5qa50HqZCRh2ofHvFDagTvzlAtItcDDXNzTF89WBmswjFY2e315OL7R4jGuqv1X7M3cUQly4nXofhgNbR_yqEJKZSLNwUwvLrOk5adW6MFVT-p6u3BmEc3Xwby4eyHs1Ro1eXce-zmeZ2kEoy1iIFlIrYuXemPNYq1IJp0Kp3ec_YLZRyr2Zj26w2Z6WvFDhkMEzQ77Aafv88r4PNJR61IxfBqWahU2trn88XQLVAXOUwbhnnkVHRdxs-8tmieZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر از پایگاه باکری دزفول
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17722" target="_blank">📅 02:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17721">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دزفول پادگان قدس رو هم زدن
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17721" target="_blank">📅 02:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17720">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دزفول پایگاه باکری را هم زدند
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17720" target="_blank">📅 02:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17719">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پایگاه شکاری‌ دزفول رو زدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17719" target="_blank">📅 02:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17718">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">استاندار
اهواز
: به فردوگاه اصابت نکرده، اطراف محدوده شهر بوده
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17718" target="_blank">📅 02:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17717">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جنوب کلا زارتان زورنان شما در نظر بگیرید
🚨
🚨
🚨
🚨
خسته شدم</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17717" target="_blank">📅 02:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17716">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرنگار المیادین در تهران: حملات آمریکا مناطق صنعتی و اقتصادی از جمله صنایع پتروشیمی را هدف قرار می دهد.
حملات آمریکا خطوط حمل و نقل استراتژیک، بنادر اساسی و زیرساخت های حیاتی را هدف قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17716" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17715">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دزفول الان زدن سنگینم زدن
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17715" target="_blank">📅 02:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17714">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cd857a54.mp4?token=SS0Lh4x_EfeixfvmJNu6O4bow9x28DxAWFtxC2FCg0SUStq9cehBd0Yet_ODyOZ7wy70U42lZ-8_bI_kfcLrsPzNr-Tm1ry9-Dh4QK3sziuWqtUgfJcd6JyHe0rsM4XTGl89SNYViMJFgaZwe0SJ7y4OzaYkFIqY9zCfM-Oxi-ldvS6oU4fVFxc8Ercm7bh8Wc5sgrtqeuDSU-aQqebvSBnl3oGTz_X085H0_jDQOQo-LtAH5xuMLTacojTKWURo-JdKzSyGm-wR1r8t2FFYSyxD4ex1IDbYWhEq-wrW6OFuWBM1adv5F7m-YK49LLpxAd2Q04xh3MRnZIWpNRqJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cd857a54.mp4?token=SS0Lh4x_EfeixfvmJNu6O4bow9x28DxAWFtxC2FCg0SUStq9cehBd0Yet_ODyOZ7wy70U42lZ-8_bI_kfcLrsPzNr-Tm1ry9-Dh4QK3sziuWqtUgfJcd6JyHe0rsM4XTGl89SNYViMJFgaZwe0SJ7y4OzaYkFIqY9zCfM-Oxi-ldvS6oU4fVFxc8Ercm7bh8Wc5sgrtqeuDSU-aQqebvSBnl3oGTz_X085H0_jDQOQo-LtAH5xuMLTacojTKWURo-JdKzSyGm-wR1r8t2FFYSyxD4ex1IDbYWhEq-wrW6OFuWBM1adv5F7m-YK49LLpxAd2Q04xh3MRnZIWpNRqJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز رو فک کنم بمب افکن زد بدددددددددد @withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17714" target="_blank">📅 02:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17713">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قشم سنگینننننن زدن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17713" target="_blank">📅 02:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17712">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش‌هایی از انفجار در شهرهای بهبهان و دزفول در خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17712" target="_blank">📅 02:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17711">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYanC_pulR9GRsJBysUY3um2b0dTsmgVca_KZXrtHi6Yxu-6BTemPJiSKuXa85DuAVeYFQIaR9jWXcSS9zGfeX-bCDHjmO9vCU_DebrDAmMCozTdMooPFBNkLtGMPstyieetoYqI94v-n9C5KAQEdKRL47XJ1UQ3jgkw7FASBwkKJ7Xm4anJjqM0CSMTTJVaIng8TS1sY95xxpCWcdWOvbkvbpaJBjhHIexX6eBDyZDZ0EtCqv7Z15vNn5hHYvQwfkZzw2ULkGGsTc5fHbMLoRZvyHidTo417g6mbtyds0I-6_t_da6yzowHeM1XNDm0gGrNGLWXF0Yet2WKvnPuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتسب به فرودگاه اهواز
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17711" target="_blank">📅 02:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17710">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مثل همون انفجار  سنگین، این بار در ماهشهر
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17710" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17709">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اهواز رو فک کنم بمب افکن زد بدددددددددد
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/17709" target="_blank">📅 01:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17708">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شلیک موشک از کویت به سمت ایران
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/17708" target="_blank">📅 01:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17707">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen.ah ♤6♤</strong></div>
<div class="tg-text">یاشار جان شما بی نظیر هستین
❤️
❤️
❤️
رفیقم جاسک سربازه اگه هشدارهای به موقع شما نبود الان رفیقم در قید حیاط نبود ممنونم از زحماتتون نمیدونم چطور ازتون تشکر کنم
🙏
🙏
🙏
🥹
🥹
🥹</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/17707" target="_blank">📅 01:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17706">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فرودگاه اهواز
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17706" target="_blank">📅 01:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17705">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آکسیوس: ایران به چند کشتی در تنگه هرمز حمله کرده است!
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17705" target="_blank">📅 01:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17704">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجار میناب دوباره
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17704" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17703">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش ‌انفجار اهواز
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17703" target="_blank">📅 01:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17702">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJCfArCWw8CsP0M611_Yu3xDUWGeu7SoVy7DAnmYxOQnK0v5P8Zow9H4AFgepOJ4oMPl2NuZ-L2oP8Ua6MosgiW1saJkurNWK7Aii99nNZoX5pFM9ZYtxPiAdIGBpniEUX-PJDsFc2l8R8B3KffvGcOJ2yxNthiKYLas2F3XA8j5Vv1cO7EtwftTs9RC2-Vi_DdJSgXpWK8CDcd-6Netm-ELCTMEoR9fO7bXN5MFCg7D3h7Ty7L-ClGu_43Aaruuel4YNyMIrnpWnmdUKDn8Lhdk3TCVbegPivZSsS1-HVdVfR-SNX0JY0Qb--JpqkNjq6bN_lo0rXe_H3b1Giyv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور مک میچ کانل که صبح شایعه شد و گفتن سکته کرده، عکس منتشر کرد و گفت بخاطر زمین خوردن رفته بیمارستان چند هفته و سالمه.
البته من گفتم قبلش به شما
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17702" target="_blank">📅 01:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17701">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17701" target="_blank">📅 01:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17700">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17700" target="_blank">📅 01:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17699">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgE8A5r4szA8_szD58z75hoU8vStPgpHNwW5PQ22BTgaCw2Wlr5V5SRXdE1uHnc6dkWkm7vQt6vH-oe90Fu3dyhE_eFa0AsMsMVqBTcXw9wd2Mc0z5_qVlG13G50_iyQGSyTtX0SlwRPXJwV9fNzW4KPIM0xVFP571Z45lIzmXFZdmhnHZuFkDjKEUdKzdFyurvcNXAW9OpF1l1LsKa1Iag53NzjzrU5KuJUrPzu6SCyP-L4i3G5vL0o80Usn47Xy2g9p63UUPNF2OyIDDYEyTSePFwhd5qF8-cb6hQnhl8WhnxjpXKMj4YLp8cLn0OgNbXlbrJN-BlbQuN_RmippA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17699" target="_blank">📅 01:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17698">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارها در جابر، جنوب شرقی ایران!
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17698" target="_blank">📅 01:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17697">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شبکه سی‌ان‌ان با استناد به تیم هاوکینز، سخنگوی فرماندهی مرکزی، گزارش می‌دهد که نیروهای آمریکایی یک موشک کروز ضد کشتی و یک پهپاد را که به سمت کشتی‌های در حال عبور از تنگه هرمز شلیک شده بودند، سرنگون کردند.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17697" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17696">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">درگیری نیروی دریایی سپاه با یگان های ارتش آمریکا در منطقه تنگه هرمز!
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17696" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17695">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb166f70c.mp4?token=imu8cDRSZzWILewkLNMpqh67Pfz358lsrrdntEPm7LbGuWvAE0sAPU9580h6c_7HeTc3_2SHEKxKA3RaoMUKEdTi68okBW1T2_Ta45jVpSvlUIqdl-PHmDi9XOKMwENz2deuYCutdecX5cP_KTCr0amjZtr3wrJmoBBI6iGqjecKT_MekIVs_fW3U6xw3-A8iYNnJMjU2ReAFRqyXWLz5joEAQsiY9ECvAoS5R4fLng4NN2yvCOGU0VaYvxXbub7TySbEj3ftbPw4GRG3BHU8fDv3bN1VMpNZEW71OF5m-GH6bbEhLtMmO7hJTmnf2VcIzIJuc6l3u1m3xJDavbRqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb166f70c.mp4?token=imu8cDRSZzWILewkLNMpqh67Pfz358lsrrdntEPm7LbGuWvAE0sAPU9580h6c_7HeTc3_2SHEKxKA3RaoMUKEdTi68okBW1T2_Ta45jVpSvlUIqdl-PHmDi9XOKMwENz2deuYCutdecX5cP_KTCr0amjZtr3wrJmoBBI6iGqjecKT_MekIVs_fW3U6xw3-A8iYNnJMjU2ReAFRqyXWLz5joEAQsiY9ECvAoS5R4fLng4NN2yvCOGU0VaYvxXbub7TySbEj3ftbPw4GRG3BHU8fDv3bN1VMpNZEW71OF5m-GH6bbEhLtMmO7hJTmnf2VcIzIJuc6l3u1m3xJDavbRqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17695" target="_blank">📅 01:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبرگزاری صدا و سیما: گزارش‌های اولیه حاکی از آن است که حمله امشب یک دکل مخابراتی در نزدیکی روستای طاهرویی در سیریک، استان هرمزگان را هدف قرار داده است - همان مکانی که در حملات قبلی نیز مورد اصابت قرار گرفته بود
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17694" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17693">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دکل سیریک رو زدن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17693" target="_blank">📅 01:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17692">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50699388f.mp4?token=UuDJ_oByeRU4mjzZX7mwUK5cw0BCZ7nCH_yWON41D5ivpyl03FpV6ZV_Qn9e_42ij1AmyGv9cDYgGD_KzwsavOorn_OsGtasRSHUMbqz-36DFrCQjocXrt3CSCEW2qpqsrucg4i6aaFr-ojg8lZkMQhV0NxhrOHh5qHFsSEci6FG5tbazc3PTOCp5_GPfkth4XS4bp4RdrSJAB2Ub7K3C7dFvKYuaRCMVrNXAgx27sRwaahbgzBnvZI3-2nQl88ERJtmKVtidq_KyqwoIfMG4f9rQ6fcIa3J2k6lXl44ymROjqYOkp2JkSTzwh2wv2udJtzl0A_QSYXt3NKAYyf9HIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50699388f.mp4?token=UuDJ_oByeRU4mjzZX7mwUK5cw0BCZ7nCH_yWON41D5ivpyl03FpV6ZV_Qn9e_42ij1AmyGv9cDYgGD_KzwsavOorn_OsGtasRSHUMbqz-36DFrCQjocXrt3CSCEW2qpqsrucg4i6aaFr-ojg8lZkMQhV0NxhrOHh5qHFsSEci6FG5tbazc3PTOCp5_GPfkth4XS4bp4RdrSJAB2Ub7K3C7dFvKYuaRCMVrNXAgx27sRwaahbgzBnvZI3-2nQl88ERJtmKVtidq_KyqwoIfMG4f9rQ6fcIa3J2k6lXl44ymROjqYOkp2JkSTzwh2wv2udJtzl0A_QSYXt3NKAYyf9HIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به جایی در جنوب الان ، فیلمو داد نتش قطع شد
🥲
💥
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17692" target="_blank">📅 01:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17691">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آب سنگین خنداب ‌اراک رو زدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17691" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17690">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پایگاه امام علی سپاه در چابهار هدف قرار گرفت  ۴ انفجار سنگین
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17690" target="_blank">📅 01:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17689">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">۲ انفجار بندر
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17689" target="_blank">📅 01:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17688" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فقط عکس بدید و فیلم هچ چیزی‌نفرستید
🙌🏾</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17687" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17686">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17686" target="_blank">📅 01:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKVc_XBot7ejpVs5F_2mRBGTx_NBLUQ3wuz1rtHaFvH6np3vcjNN8ob1sxcbyY-lojFdCHDoMV4hIHcaymhe9YKm3T8fAf4esSwkra8m-khYicEKkXTRf8MgRlH0tpNOFaoxx53nu0Jm_fsMM9uKUFwSNhQNOxStVVBRGAeocB6k-sYkTLEgQsS3vdP8gNRroUf89v9XHuZa_OmuzFonWG_Kc0mL9jKOO0jVB3ZcvyYSapQbJ-1rsZKIPGLy55r9JaQii9TD1skn7GhwLTB3LghlkGj1a1hVMHrFhbCyDhBH9bkJtJ4sqmkTv-0l0BJPDc0o51nlTZ1mkHLCz8Ah6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار شدید و سنگین سیریک طاهرویی روز شد !
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17685" target="_blank">📅 01:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17684" target="_blank">📅 00:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">همه جارو دارن جنوب میزنند دایرک هنگکرد
😭</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17683" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
