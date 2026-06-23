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
<img src="https://cdn4.telesco.pe/file/s73OxbUgeHhi1hI_EkwWq0sheupmSsFPzMJFr_VHlblDHjfbXrUnOUkjYV2F84nlJ7VFlBe36B4vTAYqGy4QpgGQYyXB7vPIj-xYUe6VnBy36gd_-QcNl3urG-Sb1u-SRESqNQ-wC8K47YrQVpLkFmtr1mc8RGf9Koz-LH0MRAdgH3r4nemyS0FJeC6491y4Yy8N5yjJbftemyxJaSfb87fERfAKJhKtBUtaHzWmMJcJPSgCyKJU_kp1V6km_9FLe4MJ_tFwE3GAX5IB67a368NeDXBTp1e10Zq1g4yaxtI-AM7nBQcue5856jPjuK5f72o_4sfA-blKZdtahM_3aA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 17:59:56</div>
<hr>

<div class="tg-post" id="msg-17944">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/SBoxxx/17944" target="_blank">📅 15:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17943">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر سابق اسرائیل درباره ایران:
هر بار که اعتراضاتی رخ می‌دهد چه اتفاقی می‌افتد؟ اینترنت را قطع می‌کنند و سپس هیچ ارتباطی وجود ندارد.
پس کاری که من شروع کرده بودم، فرایند تهیه و قاچاق ده‌ها هزار گیرنده استارلینک به ایران بود که اجازه می‌داد اینترنت و شبکه‌های اجتماعی وقتی قطع می‌شوند، ادامه داشته باشند و به اعتراضات امکان هماهنگی و در نهایت سرنگونی بدهند.
متأسفانه، دولت ناکارآمد فعلی اسرائیل این کار را متوقف کرد، همانطور که تقریباً هر برنامه خوبی که ما شروع کردیم را متوقف کردند.
و وقتی اعتراضات رخ داد، آن زیرساخت وجود نداشت.
@kakhresaneh</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SBoxxx/17943" target="_blank">📅 15:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17942">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SBoxxx/17942" target="_blank">📅 15:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17940">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTTORljklYbS9GXO9Ui24ola2ihkxf8FeZMsrvHGOp-rqQyMU7YPhwPR_3JhGJFqM6WeUB0qXyYRHad99eli8J-c03T5UwEY_AcMtQ2s-J053sHWln9cpEoXzW154tiTsQWGBb8kY65kG5nQ6BxYNlZ_KF45uYwzuEWxllQm4QZdJEmxphV_EdBn1_av2PmR3dsKGkp3c48pGen3sPAJPm2MBsiEyAt22wLPW3HHYA6E4vyGStqGX_-jLFsyZkO0zB6dOQXLKPeu26TM7CPvqSXysrbmlFPjTK0EviGp_NaLCNVTPEmh0B4iEOGV0oHzpEMqIFjqdWh01TShRoLJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8j_zlwPWv3pmcEA9LV_U7V-Ez7_-C3omCTidCQF_BGX1VVSr5kEkeeGQiN4v7L7i6OPBcHT6hCUmnxYohvo49uRaElgFqPyljUduWL5tQsNtI8G1xA-b-pbHHV9mc66KIOIfxo70S3nXraryovjeJ8nYA49WocE4gLspNk6blKInUCxV9uIUZVKwzbaueaLAKx-zLtu-vOiUo-XSKs6i1gH2upBVNY2ShTAIGwk_hcvmB_UWhPLPRmLAJKAfLGObs_Qm_qTALDGRLZgWochrRL4Kp3MfnBqURfE8HQ9et_UWKL_gCmiTfKx6uT6mC3-mL-RG_V0oXdhLP7V0H5UDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چه جلو میرویم داستان رابطه مسعود با شهباز
دارک و دارک تر
می‌شود
پناه بر خدا!</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/17940" target="_blank">📅 15:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏
امیر پوردستان: آمادهٔ عملیات پیش‌دستانه هستیم
رئیس مرکز تحقیقات راهبردی ارتش:
🔹
در دکترین تهاجمی، عملیات پیش‌دستانه نیز تعریف شده است و چنانچه مصلحت نظام ایجاب کند، ممکن است با انجام عملیات‌های پیش‌دستانه در عرصه‌های ناشناخته، دشمن را به‌شدت غافلگیر کنیم.
🔹
نیروهای مسلح هنوز بخش مهمی از توانمندی‌های خود را عملیاتی نکرده‌اند و دشمن می‌داند که در صورت ارتکاب هرگونه خطایی، با پاسخی فراتر از مرزها و تنگهٔ هرمز مواجه خواهد شد.
🔹
در یک ‌ماه اخیر، ما چند نوبت تا پای جنگ با رژیم صهیونیستی رفتیم؛ لانچرها آماده و دست‌ها روی ماشه بود تا در صورت عدم عقب‌نشینی اسرائیل، جنگ آغاز شود.
🔹
تهدیدات قاطع ایران سبب شد تا آمریکا برای جلوگیری از گسترش جنگ، به رژیم صهیونیستی برای توقف تجاوزات به جنوب لبنان فشار بیاورد.</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/17939" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">توییت ترامپ در مورد ایران:
با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
اگر آنها با این موضوع موافقت نمی‌کردند، مذاکرات بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات عمده‌ای که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی بیشتری اعمال نشود. با این حال، همه کشتی‌ها در محل باقی می‌مانند تا در صورت لزوم محاصره دوباره برقرار شود، که در این مرحله بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، در حساب امانی تحت کنترل آمریکا قرار می‌گیرد و صرف خرید غذا و تجهیزات پزشکی، به طور انحصاری از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما خواهد شد.
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود!</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/17938" target="_blank">📅 14:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17937">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🟢
طبق اعلام معاون اول مسعود پزشکیان ، در راستای برگزاری مراسم بزرگداشت رهبر فقید جمهوری اسلامی ایران ،  13 و  14 تیرماه استان تهران و 15 تیرماه کل کشور تعطیل خواهد بود</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/17937" target="_blank">📅 14:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/17936" target="_blank">📅 12:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپارادوکس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=cAAn2IP2LMfZg4g0crRHaxGFaE_zhzohh9wQyU5Dg09nsnqgfzPGLZvpGwS9s-wjynltM3FTB4MB8CMPzGUG98HcItUTLEr5VQ0erhPAyOGsaKzTSYgiowyDi4MCirLMvX5lbdjoGqtERO6GzhIDNHV_fPD2gjIT4PG7TPn2qLUOXVs5ONkej-sb69BzZSbwkQRwTL7eK4iq8nn8ZW3iiYpljf9jrwCB-Jnk-i_4Hh5XYRT3X8iIyHqgvHstxQlWAW6oai2D3cL11dme7KmKj6fBy0E0-mkZrntqsFwirW4u0q6TXuxBI9LjOEve5Un2q4NnAj_U4Ut_H21xyNL6wwQQy4HuEs5DF7Sv_oCKLGZ7KavO_p5wQXkFXGWpbY35TsueennpJtTGucFxg-PVIFlZRSXqFMSdBkg_oW7ReuQpZdDEgYf_RDtemTmq82PYsipCpFSkltTPVvbdlgc4lXD4u7ke9GiB-blttTkEtVlv0WeFvvV_8fmVmLn24Btn50fwZjWNwyRORMusRqXmZx1aO7TlYkOPSW9FKqFinpeqvk-ZgxpQa1nwShL6HePAHFH0QItuZNHZUnPcr34j9qif2vYAHEjSo-3jV9MZufheaTvU0I8puJFElooxOfuF-cbsibJcpN_im1O98xkQs25z6CQ8J7Bxi_beu0UMhU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=cAAn2IP2LMfZg4g0crRHaxGFaE_zhzohh9wQyU5Dg09nsnqgfzPGLZvpGwS9s-wjynltM3FTB4MB8CMPzGUG98HcItUTLEr5VQ0erhPAyOGsaKzTSYgiowyDi4MCirLMvX5lbdjoGqtERO6GzhIDNHV_fPD2gjIT4PG7TPn2qLUOXVs5ONkej-sb69BzZSbwkQRwTL7eK4iq8nn8ZW3iiYpljf9jrwCB-Jnk-i_4Hh5XYRT3X8iIyHqgvHstxQlWAW6oai2D3cL11dme7KmKj6fBy0E0-mkZrntqsFwirW4u0q6TXuxBI9LjOEve5Un2q4NnAj_U4Ut_H21xyNL6wwQQy4HuEs5DF7Sv_oCKLGZ7KavO_p5wQXkFXGWpbY35TsueennpJtTGucFxg-PVIFlZRSXqFMSdBkg_oW7ReuQpZdDEgYf_RDtemTmq82PYsipCpFSkltTPVvbdlgc4lXD4u7ke9GiB-blttTkEtVlv0WeFvvV_8fmVmLn24Btn50fwZjWNwyRORMusRqXmZx1aO7TlYkOPSW9FKqFinpeqvk-ZgxpQa1nwShL6HePAHFH0QItuZNHZUnPcr34j9qif2vYAHEjSo-3jV9MZufheaTvU0I8puJFElooxOfuF-cbsibJcpN_im1O98xkQs25z6CQ8J7Bxi_beu0UMhU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
⭕️
چگونه نام تاریخی و ریشه‌دار دریای کاسپی (Caspian Sea) با یک ندانم‌کاری آقایان پر مدعا خدشه‌دار شد؟!
یکی از تلخ‌ترین لحظات تاریخ معاصر، روزی که حیدر علی‌اُف، رئیس‌جمهور وقت جمهوری باکو، به ایران آمد و در دفاع از نام «خزر» سخن گفت، حال آنکه سید محمد خاتمی، رئیس‌جمهور وقت ایران، نتوانست با تکیه بر اسناد و مستندات تاریخی، از نام‌های اصیل و ریشه‌دار این پهنهٔ آبی همچون «دریای مازندران»، «دریای طبرستان»، «دریای قزوین»، «دریای گرگان» و یا نام بین‌المللی «Caspian Sea» پاسداری کند.
او در برابر آن ادعا سکوت پیشه ساخت و حتی با صدور بخشنامه‌ای شرم‌آور، این دریای کهن و ایرانی را به نام قومی وحشی و بیگانه، «خزر» نامید؛ نامی که هیچ پیوندی با هویتِ تاریخی و فرهنگی ایران‌زمین ندارد.
⚜️
@paradox_p
⚜️
پارادوکس
⚜️</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/17935" target="_blank">📅 11:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqbpFmIaMqgkNYUzZjGqLCkQHIEXwpldKAsIcOfVWLayDMfAIoeTRJ09wgVYJyc09LXynCFhKQztmXdLsJZvrWxt3oFVgz00_4gVXWhA3WZ8dTA7ATnKpQQkbR2Tdptcx8peNcTwDMXkb19gRUzRI5fylzHURlQdYOvCJetL4P6viqRCRnHTfDrmX5puVlawShZ6m60R7edl0MmeVpTJwuUmGtHbBOSf_3ATcwfSTg7QMw8EgaaEp_ftGHR2ZbewA5TWd-bFytKXWOpkk0EzGMAX65mLItWVSn0mtwozR96sV5nffLwwk_iF4HYydau91obxa88s-xpK0JdmmWEfOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت استاد!
از تبیین کوانتومی آفرینش و پایان هژمونی دلار با ظهور بریکص رسیده اند به رفع نیاز جنسی با دوغ!</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/17934" target="_blank">📅 09:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/17933" target="_blank">📅 07:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/17932" target="_blank">📅 07:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزیر خارجه عمان:    به قانون بین‌المللی و تضمین عبور امن و بدون اخذ عوارض از تنگه هرمز پایبندیم.</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/17931" target="_blank">📅 07:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:   آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.  اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.  ما می‌خواهیم شاهد همکاری ایران با کشورهای…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/17930" target="_blank">📅 07:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrMUN1O6bIiHo7llR5TWEq_RsbMM_pnJl7Cm3MXf6j6WL4Z5G7Y9ZxUVnRFu5HPy9AJGgQkV0sbPvieHxDD2izjVfZZdOFo_zREhEibk3MQTT9vkbU1Q5r9-y7rOqHHJe56Sg_6rjzb6I8IEZB_9NOcxCsX9ntaMKXlMv_et4SzuIp7jwQOK17AGmhMHA0EI6EuNsgrSFjztY9IECWrVsldRlHCfHm7OoWdMaN2gXUkdeGUb4wMSkwAZB86o_Kf29AryaZRyfjeD7fVWmvoRlhqG7PljuxULkVFuSbxrTU7kiecC16-bmzonGp0rQq_S1OcoDWeRucoW0pdumrPTvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی رئیس بانک مرکزی:  ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17929" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17928">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/17928" target="_blank">📅 01:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17927">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.  به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17927" target="_blank">📅 01:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17926">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل :  بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17926" target="_blank">📅 23:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17925">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل
:
بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17925" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17924">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU2MoxL6sAdQ9Yy_TX0M3PN6-84ZFy_0I4p7odV2O7Ym2ZY9zZJygSypAnLZB95QK4fypQLGVQAiYg-T6R8watgPc6--cms6RTZUQk3rHgYAaRBLzFW6OhtAkKPS7wH7U3256Y4japmxWSarWsvVpJZifYwRIOd7DA7OhTR22dKEir5YpZhCA4AWHBm9roq543cqthcer3YFD7Ni5hlVZxqwesCkLx3PoIfvRNpxGFDuSDAsab0xdQ28yU0Nmi0FptjQD3SyxuSMMiuaUygKtFIbxjs-dOBqr5elXOFdCPQXMdqhpHo6TTgFQg_1HrD7U7pdFV2DOi9Nu7fQW0R88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوستالژی هر ساله ما آغاز شد…
جای کیان رویگری خالی…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17924" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17923">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">المیادین: هیأت ایرانی تا زمانی که ترامپ عذرخواهی نکند و اسرائیل از جنوب لبنان عقب نشینی نکند، به مذاکرات باز نمی گردد!   ایرانی‌ها اکنون تنها خواستار توقف تجاوز نیستند، بلکه خواستار خروج (نیروهای اسرائیلی) از جنوب لبنان هستند.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17923" target="_blank">📅 22:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17922">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هند قصد دارد موشک های کروز سوپرسونیک BRAHMOS را به ارمنستان ارسال کند</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17922" target="_blank">📅 22:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17921">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ:
همه کاملاً آگاه هستند که ایران موافقت خواهد کرد تا بازرسی‌های نظامی انجام شود تا «صداقت هسته‌ای» را برای مدت طولانی در آینده تضمین کند.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17921" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17920">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خوش‌چشم، کارشناس صداوسیما:
آمریکا خودش تاسیسات ایران را نابود کرده است و حالا می‌گوید در بازسازی آن‌ها سرمایه‌گذاری می‌کند تا در سود این صنایع شریک شود/ به جای خسارت دادن می‌خواهند ایران را استعمار کنند و ۵۰ درصد سود صنایع ایران را کسب کنند</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17920" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17919">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مرندی:
🔻
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی‌به ایران صورت نگرفت</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17919" target="_blank">📅 20:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17918">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17918" target="_blank">📅 20:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17917">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMoTuyRKyBcD6uqJHj4buXqvV1pgVMZgYi6E1Qrptgpw6o9gc37cp8LApYgx75akWQafNZysjsFskUoDAZ2P2G-k-MT9fU9MEJSqpMsSC3b1acKj2cdZa7KN4IlFbaWDR4tSoNQiRCGfjMK6Ji2TRiVqV9to5nzf5zfA5zB6Jzvdjeon7wzZwYmaZ8TEdM4zYxkMOxxu19dcy6w_k0LiVJlajKVgiEjWLQurxfz4tIIG5Q7EiVzZEGSwLpW8uO8gaiq69GmShVnokUfWmUz0PoTqnZsS2AtDB-4c3ha4OzSmK8eCAsxDzjdAqruOuN7QAfRLEYKNS56CzqOawxSj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17917" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17916">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خردمند کسی نیست که بتواند میان خوب و بد، خوب را برگزیند، بل کسی است که توان تمییز خوب از خوب تر و بد از بدتر داشته باشد.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/17916" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17914">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZayAZ97oZ5TgLQSuHXHV8LJgIHbM4h8YkDmR5cp8yu9XFpbJIsHRQk5iM60VKk6B-eiPKD3oh0qDyUGOIQysrgT_FzWUr40AKbU1qEX0FF5drcZyeHCSRdl0XdHSxH6k8p8BpZqvTH628va6jp9kkX27DPg7JQcVA3FV4bTDtjZL9Y7B9KumAqh7vhxV4SAMSNdu8NQxnI2SalAsvoC-4VlpfV126RwQoAaKbGKCbf_fJGAbrfQSSHCcSBGDL4-ZYLkode336pfRQuMaq7YBWSS_ja46ZUONMAe8KhYeY3CfM0N6NqNm4o1oKNv5FxVxX1wfarW8koR2w1oYAzNgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UnzoBQJjggwwzC54ao9K9eKFp0WEzVgAUEO2CuvHO2Gw8IUjH_38CJ7CK3CDrxHRnuWOYx0A4KIMHIbDdlbwS1aeEVXN3WUE9wiFf32n7Ss1Tb_H1JEqaj6VxWXLl8rGHSY0Ejnw8LH_tUatkjzIedTFgmaHhBCrIWxI2Dycv5PWz12e-OMSjNDMnIbggPwY_OK3O2kOFn73Ib6WAVZeyIyOuaccwcvNIGr6Oiaej9lVvK6HyIWUo06I5N0g8A_MuZSyWeKunH8zogcrnjendEMZWaAfjs2XGujr-Ttg27hSGZqHOPaZ4jejXVPjPYjd-NIXv27uSSxJNtAiwog8gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمیگذاریم اسراییل بزرگ تشکیل بشود اما خودمان دنبال توران بزرگ هستیم و این نشان می‌دهد چقدر مادرقحبه هستیم.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/17914" target="_blank">📅 19:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17913">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیدالله کریمی پور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO40qRQWcJEK9Yr56s40oAzDRr2E5zLolDAOBB60AR1aovEZ_TRK1Xt2fmr6P-3UldBACphkWbMOnax8VkEDTR3Qw_JvVHnOltNfbBt8OcqLeq15NWzJHamZNktjANO8afBNCZlTIuNUk8wxnB5Dmm2rTWhibS7fXVPz74OpIyb1sgkzB1vsvBAfLslTx1iI_gObgvLUB-7DRoJSE_R13xIGffQjxrLrtlBH6Td_VHepvklV5UDuIRIh5GkXA3v4q1eBMsv6KaetnqRkmowpkxllo2I-1igwuPgU7NWxd-p5sakrqtCMD-2CZM_cgEYJ_LRx2Up22OpIA7bjpl0ECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو دشمن اصلی ایران
این‌نقشه، راهنما و توضیحاتش امروز یکم‌ تیرماه(۲۲ ژوئن)‌ از یک کانال تلگرامی نظامی اخذ شده است. بر نقشه و راهنما متمرکز شوید:
"کوریدور خیانت؛ تمام حملات هوایی به تهران و حومه، از این مسیر و به طور روزانه انجام میشه... آذربایجان، ترکیه"
کاملا درست ترسیم کرده و نوشته است. باور کنید در جنگ‌های ۱۲ روزه و ۳۹ روزه، تقریبا هر شب و روز‌جنگنده ها از بالای سر من میان البرز می گذشتند.
ولی این کمترین سزای حکومتی است که حاضر به گوش دل دادن به پژوهش های بیطرفانه نیست.
بیش از ۲۵ سال پیش، پژوهش های طولانی مدت و استراتژیکم طی دو جلد کتاب با عناوین: مقدمه ای بر ایران و همسایگان (منابع تنش و تهدید) و کتاب: مقدمه ای بر تقسیمات کشوری(ج یکم)‌ منتش شد . کتاب هایی که نه تنها سرداران آن را خواندند، بلکه مقدمه ای شدند برای اجرای پروژه اطلس استراتژیک ایران. پروژه ای که بارها برای سرداران فیروزابادی‌، شمخانی، باقری، سلامی و ...سرلشگران زنده گزارش شد.
میدانید چکیده کتاب ایران و همسایگان چیست:
دو دشمن پابرجا و اصلی ایران ترکیه و جمهوری آدربایجان هستند.
ولی کو گوش،شنوا.
#یدالله_کریمی_پور
#karimipour_k</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17913" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17912">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzhFmQpzbtIizcgfPVz7LasSj65IzeqQsZg5yom4b0Aqlq0Bk43_Oz_sgmiLbuGeVKPg969RaGWc_yAeEAWoYJirqJKdSGnIq-34erqoUlIJUOg1pP2FHPFi7EkBako9JY7KDt_5QOZhJLQ_GVhvk8PyY7xGxB601sDqjgXZazBLcg6sg8dz4X8umC9U6uqaCDs4-Q9TUf2tJ8of49rRN09Q0AsnC2nvgPiH6OR3BbE6Ffe5ztq9ajoYhurVh9Ot_-xnleZjWSmFlEuTha42SJVfeqR9UzoJ9Wf3U_YvHhfRhubSnY3zMMQ10jIccJxErdYQdK8fa3YlxI8c4gUF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/17912" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17911">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/17911" target="_blank">📅 18:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17910">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17910" target="_blank">📅 18:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17909">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17909" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17908">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5_0MlWV3XbNY-SBlnV1TUfg7dhaZ7Ig5fWJMoQtMvLP_s8MRvRzmXxyXbGFU0seSm25sbJbxIVvjSaYwNhAr51yDdNyq-l8VhJqVEaBLOSiqtEULbugnNeMy49BPfhj5eARS-CQkVedtAASAG1wc5HmDy-JRdrVSI9JNYs6qlhZnbr7oUi-o_iyfq9naA4xJsKbTzKsXqHPGp_u5CGXSdoDhUI_E5rlgJOEdQ-NyyVnQzTLjQfvPYESl1BfL5b_V-cfIjoE5fjhK19aOFFwVQsVl8xnknAmsZRQGFvffp_cxG0hepxd4KzpUCkx51LCMT9kJDpVTJpL_na4CrrY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
یادداشت تحلیلی: آینده بازار نفت در شرایط جدید ژئوپلیتیکی
بازگشایی تنگه هرمز و توافق آمریکا و ایران می‌تواند فشار عرضه نفت را کاهش دهد، اما بازگشت تولید به سطح عادی زمان‌بر خواهد بود و رقابت تولیدکنندگان دیگر را تشدید می‌کند.
در سمت تقاضا، رشد اقتصادی جهانی در برابر ریسک‌هایی مثل دلار قوی، نرخ بهره بالا و تنش‌های ژئوپلیتیکی قرار دارد و همین باعث می‌شود بازار نفت وارد یک دوره نوسانی و چندعاملی شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/17908" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17907">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:
آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.
اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.
ما می‌خواهیم شاهد همکاری ایران با کشورهای خلیج فارس در سطح بالایی از اعتماد باشیم.
مقدمات برگزاری نشست‌های خلیج فارس در دوره آینده برای بحث در مورد امنیت منطقه‌ای در حال انجام است.
موضع اصولی قطر رد هرگونه تغییر در وضع موجود تنگه هرمز نسبت به آنچه قبل از جنگ بود، است.
چشم‌انداز ما برای تنگه هرمز، باز بودن آن و آزادی عبور و مرور از آن است.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/17907" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17906">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9ViME2spWlkmJPVKx4wxkWbi86BT7fPjUBsEhV_uHftsUm6ohova8bY2_eHP6ocPrmudrCrHaeeG_qr5m_u8Kw7hetbIt0oT_yNByr_MVfrdSqCikk5YruVVrxwEUGndNbn9YUUDgJw4lEifDNzR94BxJlSYEP3zmcdPVGbUw9EUbSJux3AMwr8tptFhAHyjikPqId1EXEMzt6CK8zQ3th6Tuus2DekpjlkH-SfFt467AS0_hiU9M0Lh_aYUilwZ6r6CP_ufdnTY3JvPjBE_mpTSG68i5SwgDyoXXEbtWqHBPvxg5UumwKwLTXEw_BLmtO8HxCoL_jCvgp21Gf-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش احتمال وقوع رکود اقتصادی در آمریکا به ۱۵ درصد پس از توافق با ایران طبق تحلیل موسسه گلدمن ساکس !</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/17906" target="_blank">📅 15:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17905">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/17905" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17904">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!  سبحان الله!</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/17904" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17903">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جی دی ونس:  آنچه جرد کوشنر و قطری‌ها و کل تیم انجام دادند، به نظر من، یک توافق کلاسیک ترامپی است. اگر دارایی‌های ایران آزاد شود، کشاورزان آمریکایی را ثروتمندتر می‌کند و به تغذیه مردم ایران کمک خواهد کرد.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17903" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17902">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">روزنامه وال استریت ژورنال:  آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17902" target="_blank">📅 15:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17901">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جی‌دی ونس: ایران مذاکرات را ترک نکرد؛ ترامپ به اظهارات تهران پاسخ می‌دهد
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره گزارش‌های مربوط به خروج هیئت ایرانی از مذاکرات گفت:
«ایرانی‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم چنین تهدیدهایی در شبکه‌های اجتماعی مطرح شد، اما آنها مذاکرات را ترک نکردند.»
او همچنین درباره واکنش‌های دونالد ترامپ به اظهارات مقام‌های ایرانی افزود:
«دیروز به ایرانی‌ها گفتیم وقتی وارد چیزی می‌شوید که نسل ما آن را "کری‌خوانی" می‌نامد، نباید انتظار داشته باشید ترامپ پاسخی ندهد.»
ونس ادامه داد:
«وقتی آنها حرف‌هایی می‌زنند که درست نیست، ترامپ هم به آن پاسخ خواهد داد.»</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17901" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17900">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17900" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17899">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17899" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17898">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را بازگردانند</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17898" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17897">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17897" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17896">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17896" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17895">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17895" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17894">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">— یک منبع اسرائیلی به سی‌ان‌ان گفت:
«اسرائیل در حال بررسی اعلام عقب‌نشینی‌های نمادین از مناطق جنوب لبنان است.
عقب‌نشینی‌های نمادین شامل عقب‌نشینی برخی نیروها از مناطق اطراف خط زرد خواهد بود».</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17894" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17893">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">استارمر نخست وزیر چپگرای انگلیس استعفای خود را اعلام کرد.
دو ضربه بزرگ به چپ جهانی در کلمبیا و بریتانیا در یک روز!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17893" target="_blank">📅 12:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17892">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17892" target="_blank">📅 08:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17891">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجار قطر بحدی شدید بوده که در بحرین دیده و شنیده شده</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17891" target="_blank">📅 08:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17890">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بیانیه قطر و پاکستان در مورد آتش‌بس در لبنان چه می‌گوید؟
طرفین (ایران و ایالات متحده) توافق کردند که یک «واحد کنترل درگیری» را بین خود و جمهوری لبنان با میانجی‌گری تسهیل‌گران تأسیس کنند تا از پایبندی به توقف عملیات نظامی در لبنان طبق مفاد تفاهم‌نامه اطمینان حاصل شود.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17890" target="_blank">📅 07:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17889">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
بیانیه مشترک قطر و پاکستان در مورد پایان اجلاس بورگن اشتوک
بیانیه مشترک قطر و پاکستان:
🔹
اولین جلسه مذاکرات سطح بالا تحت چارچوب تفاهم‌نامه اسلام آباد در بورگن اشتوک سوئیس با حضور نمایندگانی از جمهوری اسلامی ایران، ایالات متحده آمریکا و دو طرف میانجی، دولت قطر و جمهوری اسلامی پاکستان، به پایان رسید.
🔹
اجلاس دریاچه لوسرن در فضایی مثبت و سازنده برگزار شد. پیشرفت‌های دلگرم‌کننده‌ای از جمله ایجاد سازوکاری برای مذاکرات فنی بیشتر حاصل شده است.
🔹
بر اساس این تفاهم‌نامه، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
🔹
مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
🔹
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.
🔹
علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17889" target="_blank">📅 06:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17888">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
عراقچی
:
🔸
میانجی‌گری خستگی‌ناپذیر پاکستان و قطر باعث پیشرفت‌های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔸
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصره دریایی برداشته شد، برخی از دارایی‌های مسدودشده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
🔸
اولین آزمون واقعی: واحد رفع درگیری‌ها در لبنان</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17888" target="_blank">📅 06:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17887">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گوستاوو پترو، رئیس‌جمهور کلمبیا، نتایج انتخابات این کشور را به رسمیت نمی‌شناسد و اسرائیل را به دستکاری در نرم‌افزار انتخاباتی کلمبیا متهم کرد</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17887" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17886">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رییس جمهور چپگرا و معتاد کلمبیا امشب شکست خورد و جایش را به یک راست گرا داد.  قاره آمریکا در حال یک دست شدن است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17886" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17885">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دونالد ترامپ، پس از ونزوئلا، اکنون کلمبیا را تهدید می‌کند و گوستاوو پترو، رئیس‌جمهور کلمبیا، را «قاچاقچی غیرقانونی مواد مخدر» خواند.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17885" target="_blank">📅 02:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17884">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=g5VWPv1omJj3Q6NJ2gz7TrgodoYosEdkn6BlTWTs9DqATaOA9g8My2Yt9npkTYdVjUv4U-tPLAh71wYfZ2NrSyJsfX_0loUDTBWLiLns-rh2CmC-qll1t8bH7NOPtDpEE_-ZDITsmsJR0mLKMs7eelm-XORO9kwB_-zW9EoUC-ENpVZEy3yjosTFQWkLWkAUplf1IJJQRO9z1whr38zlSU9anIpbmSF0Yvm1Op5GYkRPYOmPvh771Pf4_nIvd5IoVHr-X4MLApnGVJmU6Wc-c8Uiqu4RN_RJ1lXDDy0S_hP7VV-HNJt4GHPGFuKSFhbiKtjZDJuFyOHbCM8UtiMVqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=g5VWPv1omJj3Q6NJ2gz7TrgodoYosEdkn6BlTWTs9DqATaOA9g8My2Yt9npkTYdVjUv4U-tPLAh71wYfZ2NrSyJsfX_0loUDTBWLiLns-rh2CmC-qll1t8bH7NOPtDpEE_-ZDITsmsJR0mLKMs7eelm-XORO9kwB_-zW9EoUC-ENpVZEy3yjosTFQWkLWkAUplf1IJJQRO9z1whr38zlSU9anIpbmSF0Yvm1Op5GYkRPYOmPvh771Pf4_nIvd5IoVHr-X4MLApnGVJmU6Wc-c8Uiqu4RN_RJ1lXDDy0S_hP7VV-HNJt4GHPGFuKSFhbiKtjZDJuFyOHbCM8UtiMVqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهراب سپهری به جای طارمی؛
😂
راه حل خیابانی برای گل مردود ایران به بلژیک
🏆
در قسمت دوازدهم برجام رونمایی شد
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17884" target="_blank">📅 02:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17883">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به نظرم تنگه هرمز را بدهیم بیرو ببندد و خودمان برویم تنگه مالاکا را ببندیم!  آبش را هم بدهیم آقای میثاقی بخورد!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17883" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17882">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17882" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17881">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkEXTsI288Lej4gX_T4OKmFMl0mlIaHPSqDSkC5r3pwAnD60oT1B-vSfJafDl2ZJG40ns11TEDSwpoOElvLOPGoqt7ZfRzYvAWOtZRP3quPDeW_EwRAynhVfm-0kzNj4WEy57cylEIEWa_x7scsg4xAdzzTNEol-v6PDGZ3QON6QbYjFDfJTacLDaly-kRslhQXa-kWZr67Qzx-SlDqoZ1sqKWUF9pWlMcHGVQ3jy7lB8ReQxRTtl90itTP1pv4lCr0Vspwk60ntyvHtAu33zVSdOg5AVpv_neMzQhlDmAigjV6mMauhEgoJAi-Pbgy5s2dOADMFsKuozWnWOwp0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!  انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17881" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17880">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_G_NJDfTsJ5ALfaoND1uavpvgq-2N_MYrPw_sHmY1Sj-wNFpGjASWQQYhiJ9VQY4n4S-Q7NK-vh52OXB5OkuIGMuyVNcF5xGqee_xa1YuDOgDL-XqepjRDwULpnNGGKSrLNnQSonmkkXuTqao0z3_vFKIMEV0IdQsbmDBeNO3pB0bq3Ke9rjhN45f8ZZNGGv3pcjfd5FH-1pDVA8UKy5MjCbhx1Rc0hiwMT_qnsvZ6qLUBS5Sh0GCo5h_lvijXB-KLQrBJ8zmBYJhk8ClptbqphUjLFlA8AZFNHffEOOLRAQ2Sdo5Oe6dS0h0xvIPscy4YEVsktyAEYdHmw-FdNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!
انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17880" target="_blank">📅 00:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17879">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=MkA1aeBoU7ukBJUGic-qaxpUiYfwWuDEIz1HAqmvczci2hLshx_ajzJSC0_dX_a-bXA-2HcHpiAH9CMAdWYQ6hmcndzmUN7b9owzCSpPxk9MMraPDVbE_BQI9__AMkv1wTlZi5LQE8sV3f2_8UZ_3zYxOahJqcM2j1y4mIcy41WOeCC-8H9XSBq-WezjeQRZdtv4L4my8DwS8_i1P6OvaqoGr7NRZRmoN_XiNerApYgmscMMezA0JH7o94WnCxCA--p1NfdRFZDFX-dWRfqUhXQiiByx0WMrgLhfaQiC7df0_8KZZdqueCZhBm73ftgiprhFGmGkzVRUJ0EMxH8swQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=MkA1aeBoU7ukBJUGic-qaxpUiYfwWuDEIz1HAqmvczci2hLshx_ajzJSC0_dX_a-bXA-2HcHpiAH9CMAdWYQ6hmcndzmUN7b9owzCSpPxk9MMraPDVbE_BQI9__AMkv1wTlZi5LQE8sV3f2_8UZ_3zYxOahJqcM2j1y4mIcy41WOeCC-8H9XSBq-WezjeQRZdtv4L4my8DwS8_i1P6OvaqoGr7NRZRmoN_XiNerApYgmscMMezA0JH7o94WnCxCA--p1NfdRFZDFX-dWRfqUhXQiiByx0WMrgLhfaQiC7df0_8KZZdqueCZhBm73ftgiprhFGmGkzVRUJ0EMxH8swQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دلال های محبت فاکستانی را ببینید!
شهباز شریف از عراقچی التماس می‌کند تا با ونس ترنس دست بدهد اما عراقچی پشت کرده و می‌رود و بعد شهباز شریف و عاصم منیر شروع به ماله کشی برای آمریکایی‌ها می‌کنند!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17879" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17878">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">راس الفان همان منطقه ای است که ایران تاسیسات گازی قطری ها را در مارس به آتش کشیده بود</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17878" target="_blank">📅 23:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17877">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرنگار صداوسیما:
هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17877" target="_blank">📅 23:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17876">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزارت کشور قطر:   انفجار داخلی در یکی از کارخانه‌ های منطقه صنعتی راس لفان رخ داد و تیم‌های دفاع مدنی به محل حادثه اعزام شدند و هیچ گونه آسیب جانی یا نشتی ثبت نشده است.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17876" target="_blank">📅 23:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17875">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇶🇦
🇧🇭
— گزارش‌هایی از انفجار در قطر و بحرین.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17875" target="_blank">📅 23:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17874">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇶🇦
🇧🇭
— گزارش‌هایی از انفجار در قطر و بحرین.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17874" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17873">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHWnsAk6LNjvndNKp1M_3x8qu_q7u-hjQDoxrMh2Ilh8Kmb1OrNis6zj50JBj_BH0hEI4sbWV8-qNMgdaNlt8YkFYqPqkrqnYKhyrrPkgrlkJ7vIkzuIsvDh_MbKzX0wy_WJhg7ZMwGFYTrc1ewsFn8_m7acO8UuPyv6w4z3ZC_ndR9DEd-yEVAJfbG3TH5y8-Rphd68IogeOupFLVID9PeghJZUoadoel3pvg9MpcvPQFX7akCqhdFWlBe8XyacOrACCNr-g0MefcwE-Jvx1mNVcYZ-XB66UwctT83HmFgsWIv4jjWg9hZ1oCfmd9IWBqHcpLksoKWkybO7tMuRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به جای طارمی، سهراب سپهری رو میذاشتن نوک خط حمله ایران، الان ۱-۰ از بلژیک جلو بودیم  》Keyvan《  @OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/17873" target="_blank">📅 23:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17872">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">اگه به جای طارمی،
سهراب سپهری
رو میذاشتن نوک خط حمله ایران، الان ۱-۰ از بلژیک جلو بودیم
》Keyvan《
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17872" target="_blank">📅 23:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17871">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">به اندازه قهرمانی پرسپولیس در آسیا از بلژیک جلو بودیم…
لعنت بر پرچم کمک داور !</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17871" target="_blank">📅 23:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17870">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تیکی تاکای عالی از بچه ها !
منتهی در محوطه جریمه خودمان</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17870" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17869">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">از نادر محمدخانی به اینور هر چی مدافع تیم ملی داشته امشب فیکسه.
》Footfun《
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17869" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17868">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">با نتایج درخشانی که همسایگان بیابانگردمان در عراق و عربستان و قطر گرفتند، فشار روحی از روی بچه ها اندکی برداشته شده و امشب با خیالی آسوده تر می توانند برینند.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17868" target="_blank">📅 22:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17867">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17867" target="_blank">📅 22:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خواننده Secret Box مدتهاست که از این طرح آگاه است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17866" target="_blank">📅 21:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17865">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اسرائیل در حال بررسی عقب‌نشینی محدود نیروها در جنوب لبنان است.
— کانال ۱۲ اسراییل</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17865" target="_blank">📅 21:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17864">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17864" target="_blank">📅 21:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17863">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17863" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17862">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">💢
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.   @StrategicNews_ir</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17862" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17861">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استراتژیک</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=MU_qbHqTE1Mv0KgBoXYBabk4fuzsnLK6u6C5CCJcu8OGunnLgp77ZO9nYbMwOMYplCahjp8HGw9CG2XmOVEBpgP7HmLDnnenhJihfdDi0nIzlgVlCIFkO1aLmiPabXNPTihkBb6JYkjT2q8JU4mufDMCZaE7SL-dTw761qLJTqCmJ1BPKvp4X5-XmciOoWHE9vvXi8clILr_3QWU-PrJB9V75wNFfqWvpJG4Mydol3atCAmGv6SAmlRi9iHB98luHcnPgm5mT4Minvtx7mojb4QYLRDALEVnZ5M7K36OiwaoR9Cj5Tz2pgjrHsXdFCTjX3HSmPKprjqC8QK5q0hVZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=MU_qbHqTE1Mv0KgBoXYBabk4fuzsnLK6u6C5CCJcu8OGunnLgp77ZO9nYbMwOMYplCahjp8HGw9CG2XmOVEBpgP7HmLDnnenhJihfdDi0nIzlgVlCIFkO1aLmiPabXNPTihkBb6JYkjT2q8JU4mufDMCZaE7SL-dTw761qLJTqCmJ1BPKvp4X5-XmciOoWHE9vvXi8clILr_3QWU-PrJB9V75wNFfqWvpJG4Mydol3atCAmGv6SAmlRi9iHB98luHcnPgm5mT4Minvtx7mojb4QYLRDALEVnZ5M7K36OiwaoR9Cj5Tz2pgjrHsXdFCTjX3HSmPKprjqC8QK5q0hVZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@StrategicNews_ir</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17861" target="_blank">📅 19:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17859">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ درباره لبنان:  من ناامیدم که اسرائیل نمی‌تواند حزب‌الله را از بین ببرد. آنها بدون خراب کردن ساختمان‌ها نمی‌توانند کاری انجام دهند.  من نزدیکم که این کار را به سوریه بسپارم چون او کار دقیق‌تری انجام می‌دهد</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17859" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17858">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به گزارش الاخبار، جولانی در جلسه‌ای محرمانه وعده داده که از حزب الله انتقام خواهد گرفت. وی گفته :  «حالا نوبت حزب‌الله است و ما انتقام خود را فراموش نخواهیم کرد»  به نظر می‌رسد  که در صورت حملات آمریکا به ایران، جولانی از وضعیت برای باز کردن جبهه‌ای علیه لبنان…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17858" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17857">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">من دقیقا نمیفهمم روی چه چیزی به جز پایان موقت ۶۰ روزه جنگ توافق شده؟!  لبنان؟! تنگه هرمز؟! موشکی؟! نیابتی؟!</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17857" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17856">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ:  اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17856" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17855">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قراردادهای میان کشورها تحت فشار (Under Duress)  در حقوق بین‌الملل، قراردادها و معاهدات میان کشورها باید بر پایه رضایت آزادانه (free consent) منعقد شوند. مفهوم Under Duress یا تحت اکراه زمانی اعمال میشود که یک طرف با تهدید غیرقانونی، نیروی نظامی، فشار اقتصادی…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17855" target="_blank">📅 17:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17854">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مدیر Secret Box از اعضای تیم دیپلماتیک کشورمان ممنون است و به شرافتشان درود میفرستد!</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17854" target="_blank">📅 17:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17853">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2mIfxHQVP4d__Nyqbq8KmKneu1SQVydJQqgAL7mSZpNUbWg55SpeJcveR4u1iYoKh_-XlUSJaoFKmJYdbOsC3y2phDkifLgBDnDZs4Je7Wdq0BG5DghA_CVm_0wdQwWAOI5GrSHjoZEY8OoA-wSHh-ZCEe6d832c3ZIii3rJRd9BA45XY13j4pm9MMa2lUkOMZpqjyIOrs8iZPbKheqfJcXHatv3NIbQ6O1kcWE74pXJuDIQuNel3iiq1hD0GKRvnnIB3Fequog8nlwHfrSi-x77lVIBwFXP91uNEfqSeOZoQxz392snBvqRpSfTVJKhvYo24tdqdJiXf8UAHNgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه یمنی ها در باب المندب فعال شده اند.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17853" target="_blank">📅 17:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17852">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ:  اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17852" target="_blank">📅 17:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17851">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ:
اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17851" target="_blank">📅 17:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17850">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">— وزیر دفاع اسرائیل، کاتز:
"هیچ محدودیتی برای سربازان ارتش اسرائیل در لبنان برای اقدام به حذف تهدیدها وجود نداشته و وجود ندارد.
آتش‌بس دیروز اعلام شده، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که جوامع شمال اسرائیل را محافظت می‌کند، باقی می‌گذارد.
همانطور که نتانیاهو و من روشن کرده‌ایم: اسرائیل از منطقه امنیتی در لبنان عقب‌نشینی نخواهد کرد".</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17850" target="_blank">📅 14:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17849">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDqC-G3ao_lPdi1YKzC6T807dRwts9r_dlV_HRr7Dsq4O8-60WdVVcYqKSFjKgQ-_hT3TainwcaRsAmDPzLXQWW89dt3Y28h9yfV9N7Gs8t4UuHVggLgt3BU1RanIE2aaGK5yOHrhA781GxpmgApBwLRDkzu4XV7VrNuANqNRMfN2kABowfF6Kxl0nTgwFKQre7Yvc3ASXZcBSUUhi4JvC1s-enl57auu6Gye2pT-GIzzt0ai1J8mpIyLRJSYWAKOfb_ujUQgE_M7aHKLjO1yHfeyiziOJatFrHkzWDg-sbBkRbi8h0ODByShZDcigqhk1QLza0ix-kjQifI_G7TiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
فدرال رزرو و پیام Hawkish به بازارها
در نشست فدرال رزرو آمریکا در ۱۸ ژوئن ۲۰۲۶، نرخ بهره بدون تغییر باقی ماند، اما لحن سیاست‌گذاران به‌وضوح
Hawkish
بود.
✔️
اعضای کمیته
FOMC
تأکید کردند که ریسک تداوم و حتی تشدید تورم همچنان بالاست. همچنین داده‌های
Dot Plot
نشان داد که بسیاری از اعضا احتمال یک مرحله افزایش نرخ بهره در ماه‌های آینده را منتفی نمی‌دانند.
اگرچه در داخل
FOMC
اختلاف‌نظرهایی وجود داشت، اما دیدگاه غالب این بود که
Rate Cut
در شرایط فعلی چندان مناسب نیست و در صورت لزوم حتی گزینه
Rate Hike
نیز می‌تواند مطرح شود.
🔽
واکنش بازار سریع و قابل‌توجه بود؛ پس از انتشار بیانیه،
USD
تقویت شد و انتظارات معامله‌گران نسبت به سیاست‌های انبساطی کاهش یافت.
نکته مهم اینجاست که بازار انتظار یک
Full Hold
(ثبات نرخ بهره بدون هیچ‌گونه سوگیری مشخص) را داشت، اما فدرال رزرو با اتخاذ یک
Hawkish Hold
نشان داد که همچنان نسبت به تورم نگران است و برای حفظ سیاست‌های پولی انقباضی آمادگی دارد.
🕯
جمع‌بندی:
فدرال رزرو برخلاف انتظارات بخش قابل‌توجهی از بازار، سیگنالی انقباضی ارسال کرد. این موضوع باعث افزایش تقاضا برای
USD
شد و تا زمانی که فشارهای تورمی به‌طور محسوسی کاهش پیدا نکنند، می‌تواند از دلار حمایت کند.
💬
برای کسب اطلاعات بیشتر، با آیدی آموزش (
@CWedu
) و یا شماره تماس 09908006002 در ارتباط باشید.
@CyclicalWaves</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17849" target="_blank">📅 12:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17848">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⭕️
رئیس سازمان بازرسی کل کشور
:
سرویس اینترنت پرو متوقف شد و مبالغ کاربران باید عودت داده شود</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17848" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17847">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🗯
دونالد ترامپ ؛ رئیس دولت آمریکا
:
آنتروپیک دیگر تهدیدی برای امنیت ملی آمریکا نیست
وی در مصاحبه جدیدی اعلام کرد که پس از اقدامات اخیر شرکت آنتروپیک، دیگر این مجموعه و مدیرعامل آن را تهدیدی برای امنیت ملی آمریکا نمی‌داند. این موضوع پس از آن مطرح شد که آنتروپیک در پاسخ به دستور دولت، دسترسی کاربران خارجی به مدل‌های پیشرفته Fable 5 و Mythos 5 را مسدود کرد
اگرچه ترامپ از سرعت عمل و رفتار مسئولانه مدیرعامل آنتروپیک تمجید کرد اما همچنان احتمال استفاده از اختیارات اضطراری قانون تولید دفاعی را برای خود پابرجا نگه داشت. در‌همین‌حال، شرکت آنتروپیک نیز بر تعهد خود برای همکاری با دولت آمریکا جهت حفظ امنیت زیرساخت‌ها و پیشتازی در این فناوری تأکید کرده است</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17847" target="_blank">📅 12:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17846">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbvxgVhZ5qPNTaz7Ws4rjrqgc5QkOiwmA65D288T1qGy6dSItonek54ESeaDgBvjBr0NwZ3hCF2rKsPnyCrqBI1Wy9rup5DFsvgi0LdEIAZLAwvWfPP7NMyUA7VotBXxiplqHw5rffnlZeeskC7Hsdk0faFCx8FrjqPexgDuKXyPekhPeQmvDjO83nusauKM3_BIGSiWeT2NaZH-4G7n_C-R6CdBl3lUoAl8xgmsCRmBM36OD6Vw3N4Rx_WTBpA6pS07b_Y567IcRd-n_BK1_vnrYMxOzOLdInW3Gnln8SQ4UHBmTdHEm1sXIJnT7VRZU-4g87ujpyCo9vPjKKn5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدانم ولی اگر بیعت کرده قطعاً مصعب سرش کلاه گذاشته بعداً</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17846" target="_blank">📅 11:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17845">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پزشکیان:  تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم؛ این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17845" target="_blank">📅 11:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17844">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پزشکیان:
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم؛ این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17844" target="_blank">📅 11:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17843">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حسین شریعتمداری: مسئولان نظام برای بازگرداندن  بحرین به سرزمین اصلی ایران اقدام کنند  حسین شریعتمداری نوشت: «هموطنان بحرینی‌مان بارها اعلام کرده‌اند که خواستار پیوستن به ایران یعنی وطن اصلی خود هستند و انتظار آن است که مسئولان دست‌اندر‌کار نظام این خواسته…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17843" target="_blank">📅 11:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17842">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17842" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
