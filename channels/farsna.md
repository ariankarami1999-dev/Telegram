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
<img src="https://cdn4.telesco.pe/file/qOUYWIvdmetH9y2S2FoqTTUn8cTs727VQ3Ijv5azNGpO8pMowt_ZBT9JXM6hFwvR74K4u0toAT_DMT8O9HRnlEe_68X_Zf5BzbXB2UXkJ5uyml0gPBO1mjiafdh_0i9PCLRec9SbAP2qUGH8uoX8Tngu2cukfMi0PhlW3cm30sQnbNmt725ymjFzJsfCJlEvgYEF8ayvRD4Gk8FOdns4DvBhP6WCYGH-umL5lUHeVbsH1bzC3Tf5BMTeyddNUo_VsML4w9lgg7KiceCeN6C0aAvTwoTpvqiqxX2brAmZaTIewC0BIynrYbNoi3QbHJQG5xvxC_bvUYPMrDGfFkyJew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 01:33:15</div>
<hr>

<div class="tg-post" id="msg-435625">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzkPrjXNoylrpW7eMWKPxG-cSZZ7aiLz3MXtcphJ8M0Rb9rF3D419rTp-j13e5x1i2CSm5Z_7WpBsMdPVC08euMX2ujwL9KuOloCuxLoezJv4S6ZvJJn_qmccKynzw09czMtj9MSnpAWC9BSmlTC8NEqgq66-iaK_kwJMMOc_A4y7gM8CtTM_TFVdcwJ4tI732rJ7MTudFzLFevOycFkRV4gis3CwGV4SPw-I1KgkflIOr6HE1EX4-K5ETxNSM_26wr_1XB9HvHIVHLiPZnQ2TveyniQ6M6ZIEXTrd9nWjBns3kX1jQoKcf2jlHx2xXxpUvZvi4FHdneHeICZ_etjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شناسایی ۶ هزار موتورسیکلت احتکار شده در آمل
🔹
دادستان آمل: یک کارخانۀ تولیدکنندۀ موتور سیکلت در آمل، با سندسازی و صدور بارنامۀ جعلی اقدام به دپو و احتکار ۶ هزار دستگاه موتورسیکلت کرده بود.
🔹
این انبار با موتورهای احتکار شده پلمب، و پرونده در دست بررسی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 486 · <a href="https://t.me/farsna/435625" target="_blank">📅 01:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435624">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307d27fbb1.mp4?token=sKUMENr83-3T_8_NDXZ5yal7k5Hk7gaMp6-xCEkkIJKy3io0ECj_g0jNfE7h2Qaxhq-CBFhd7xCF5JcI4Z0gl4T4HyLx4LSoVMKXgY8uivQji7CAbYSsNR_ke0N9b4FkPBCN3ho8US54tiGcnuV53nJfa6DNV3802IWHTB6EsJZCSP6jLDjuio4FjkMaLQQW8d7-2TQG5AzSvTxhxJPgPCfh8KK3oE_VoRk4MZmQhwBbjz6kTK3HbtkO_xVAaFxAn27r-E6E2nZQ9tozEwM8fq6VPCqfNrLC_tf2t7c_jbAdp4Nr9DNHt_UMZkPJkuMCmC46QKjBLraP_tX6o8JuNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307d27fbb1.mp4?token=sKUMENr83-3T_8_NDXZ5yal7k5Hk7gaMp6-xCEkkIJKy3io0ECj_g0jNfE7h2Qaxhq-CBFhd7xCF5JcI4Z0gl4T4HyLx4LSoVMKXgY8uivQji7CAbYSsNR_ke0N9b4FkPBCN3ho8US54tiGcnuV53nJfa6DNV3802IWHTB6EsJZCSP6jLDjuio4FjkMaLQQW8d7-2TQG5AzSvTxhxJPgPCfh8KK3oE_VoRk4MZmQhwBbjz6kTK3HbtkO_xVAaFxAn27r-E6E2nZQ9tozEwM8fq6VPCqfNrLC_tf2t7c_jbAdp4Nr9DNHt_UMZkPJkuMCmC46QKjBLraP_tX6o8JuNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید حاج قاسم سلیمانی: فضا را برای همه نوع آدم‌ها باز کنید
🔹
خواهشم از خواهران و برادران متدین این هست که فضا را برای همه نوع آدم‌ها باز کنید؛ بگذارید همه نوع‌ها بیایند؛ بعضی از افرادی که ظاهرشان شاید ظاهر مناسبی نیست اما باطن خوبی دارند.
@Farsna</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/farsna/435624" target="_blank">📅 01:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435623">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
موج هفتادوپنجم حماسۀ مازندرانی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/farsna/435623" target="_blank">📅 01:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435622">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/255f024260.mp4?token=tR_UOp_vVQaknk0VsFCyUKYPZSA6Olo4QujTdmGObn0P4YoNd-WJVVkX7UKtHXT2l1fMW2_ETci8s7ifx1qYkwxHacNiFs6A634OJxxPuSgXjpiI4PMO3dE70CDYZtxI-oXzTmf94VhRVAcNz8YdrpkyC4-FufQzpIjDEpbaW3wzC2X6a83G5In4t6t9dun2lxRVIMs0GFCCKTcL4gM25rny5C-5Y89A_8NJZsuUSL0Ovh52n3AOhhPIrlfcxmySGmxnLbcE9lZVJF7G8PJ5bkatHfNbo3e-TUpLyDNKBvnOHG_5XEh45kIAq5K5nkSyz4DKoR3oM27ThHcnCsEPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/255f024260.mp4?token=tR_UOp_vVQaknk0VsFCyUKYPZSA6Olo4QujTdmGObn0P4YoNd-WJVVkX7UKtHXT2l1fMW2_ETci8s7ifx1qYkwxHacNiFs6A634OJxxPuSgXjpiI4PMO3dE70CDYZtxI-oXzTmf94VhRVAcNz8YdrpkyC4-FufQzpIjDEpbaW3wzC2X6a83G5In4t6t9dun2lxRVIMs0GFCCKTcL4gM25rny5C-5Y89A_8NJZsuUSL0Ovh52n3AOhhPIrlfcxmySGmxnLbcE9lZVJF7G8PJ5bkatHfNbo3e-TUpLyDNKBvnOHG_5XEh45kIAq5K5nkSyz4DKoR3oM27ThHcnCsEPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جو کنت، مقام مستعفی دولت ترامپ: وزیر خارجهٔ آمریکا گفته‌ که ما مجبور بودیم به ایران حمله کنیم چون اسرائیلی‌ها قصد انجام این کار را داشتند
🔹
در واقع اسرائیلی‌ها به ترامپ گفتند اگر او رهبر ایران را ترور کند، مردم ایران قیام می‌کنند و حکومت را سرنگون می‌کنند و این اتفاق بسیار سریع و آسان رخ خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/farsna/435622" target="_blank">📅 01:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435621">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d283bf7bc4.mp4?token=MNNbZymfWkgEthxaYOjr-DmfQB0qgX61QxjTmj_BGmXgbVlDA4iK5hJu0TLGc0IavM_xUxvhIiQqHwxlvYklj2RABxluVjPw4KYEMWSwX8zoAhp9x4pAmS0_ZzagmX9dm-hySw2XaH-WkemlCXxa153EK0ToMpQipswhNinV3fwHWcg8WGd8aUUhVRmMf-rOnvyG1axbWaYf5wOAR9YFDWxyjE_OtXN2kmiR0CPGpP4pB3OH9eHubzEwvZXqExu-z1oTabY-qaWbHwQ_8yrT9gcdfAEfXFV-U9MRq831UcgnPD51v8NyaWbZhF64T9hfkF4bNaPSu6PzLijlhbjiRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d283bf7bc4.mp4?token=MNNbZymfWkgEthxaYOjr-DmfQB0qgX61QxjTmj_BGmXgbVlDA4iK5hJu0TLGc0IavM_xUxvhIiQqHwxlvYklj2RABxluVjPw4KYEMWSwX8zoAhp9x4pAmS0_ZzagmX9dm-hySw2XaH-WkemlCXxa153EK0ToMpQipswhNinV3fwHWcg8WGd8aUUhVRmMf-rOnvyG1axbWaYf5wOAR9YFDWxyjE_OtXN2kmiR0CPGpP4pB3OH9eHubzEwvZXqExu-z1oTabY-qaWbHwQ_8yrT9gcdfAEfXFV-U9MRq831UcgnPD51v8NyaWbZhF64T9hfkF4bNaPSu6PzLijlhbjiRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیعت مشهدی‌ها با مشت گِره‌کرده
@Farsna</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/farsna/435621" target="_blank">📅 00:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435620">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
مردم شهرکرد، ۷۵ شب در سنگر خیابان
@Farsna</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/farsna/435620" target="_blank">📅 00:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435619">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv9pVA5Snkb_Rb69QETrYBnlzeIFkqm_Twn6Ja7XASGeGnMc4E0qDLFGWH8--dyAp4lZ9W4fZbdHFyS3QTlyS7yUMi6Lq2-9y9uyRiDwtarkhIPAxBRI4IscKDmue37i2e9w2V7sSWgHdTlBAiyVjETw9zOWoH9xuexvgqC4oxioYqJ-syAZkxmMxd9xEyCCo6hij2y1KP0NRDwC_Y21nxBL_s-6hwktFnPQp9PvyiDK0LCn8XwyLZWDYeeODxY61TWbdmSV8DWBOz8FKd30BZO19l3LK4ttBaUHsSUGZVc7YIpdjIWlzV01Pgdv9pkrybkke-Ubpkee04VNkxCFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از شهادت پدرم فهمیدم «شهیدان زنده‌اند» یعنی چه
🔹
فرزند سرلشکر شهید اکبر ابراهیم‌زاده در گفت‌وگو با فارس: پدرم همیشه می‌گفت «اگر احساس کنم جایی به من نیاز است، وظیفه دارم که به آنجا بروم.»
🔹
او برای این منظور، حتی علایق شخصی‌اش را هم کنار گذاشت. بعدها که بزرگ‌تر شدیم، از او ‌پرسیدیم «روحیۀ شما به نظامی‌گری نمی‌خورد، چه شد که این مسیر را انتخاب کردید؟» او پاسخ داد «گفتند به نیرویی مثل من نیاز است و اطاعت کردم.» فکر می‌کنم روحیه ولایت‌مداری و تکلیف‌گرایی او باعث شد چنین مسیری را انتخاب کند.
🔹
مهم‌ترین ویژگی اخلاقی پدرم «مهر» و «رواداری» بود. او هیچ‌گاه به ما اجازه نمی‌داد درباره کسی بدگویی کنیم یا قضاوت ناروایی داشته باشیم. حتی اگر با فردی اختلاف نظر سیاسی داشت، باز هم نمی‌گذاشت درباره او با بی‌احترامی صحبت شود.
🔹
پدرم نسبت به استفاده از امکانات اداری یا دور زدن قانون، فوق‌العاده حساس بود، هرگز اجازه نمی‌داد از موقعیتش کمترین بهره‌ای ببریم و حتی از ماشین اداره استفاده شخصی کنیم.
🔗
ادامه گفتگو را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/farsna/435619" target="_blank">📅 00:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435616">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zs6C9F8rk7Uq7nXEVoRSQJk2L9c6StdRmpMo5nxgHAdBy_sNgfK63bKak2jZ3lG9G1FOmwF_xChFFUHLtM9dS1CU34IBB5s_8CMMwYInOF6EegykQSG69od0_Q5YIbICtKw6GvwyuC8sac6mQusjrgytRJ9494y62dm22gIogg1KuuwshF3rYA1KG3DAUkDUP8ijV-I5Wp6GeJ3h4g2yiBhoRsCJGjP2KjUdFA-YBfEkfukIxu2Cuyd8LAzP2RuQ2aANyGdCg2cO1lCsZwxreJ-HeKPzmIjI2rz0Nad6Ubp3skbuwZlBgnvZzVK4MzA3Fmdz0pXOvhJUfqh_-v1UJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBw4W_dgeTwWX57Stiz4lN7qnw5bNJSoChLTph-E8uTgUzQSAQoF4BV56XLc2uxddvx3KiafWPFD7LEKW5l5rLgTcMZwuLQx1hWxrVXCxlXS6PiiidtZpaFN1H6KYG37bz0cMNO1ye5AreYoOGFD1hc_fQFZEDokyWhjs14fbTlmn-GhbgqBLMlG3I004OuUWvA_KbipZKn7LPrqxShoEvEUTClPYk2fSxxaZ-PTHy_vUEPecVbmQSlvfuDIqbdnea7vU23GhI8gJR263rGD48W7TP5PlZlZIOJWwLzeIE6curEV8s6CMO-zrp_riIPLpF10h6A769a7e8Sb4aTzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/izYwCmZTsZOyWKiWg_3GTxIFDZ7-nHvMHiKR60FHkeXYyFtf9YkPj2GaYLm0DhqWjVnFbaxz9rUZY_ixzPU1GluOrNYUzwo0ic6WeQfIVJF65H72gsEBAv2Uu70rp5gzqjiOWZCV4L5TxCR_2HYs0WNo6zAfFxPY01Gy5A61oUozzb-WpIdJq2jVC_j7W_EpyPkSHFl2A63JxWbpgfY6nEG079-3cO1j_k91wSIwAr_1wihhbxh0sQTxl2W4JRXyfrftu2B8UJc7VoXNzAvFqggjNM3Z6D_3hCipF8DQyrWhfNINHmoC11KnaV50mqHQnJDbEahpuWWxVjBD0qE8nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حنظله: مغز متفکر سفر نتانیاهو به امارات و معمار اصلی توافقات ابراهیم هک شد
🔹
گروه هکری حنظله اعلام کرد که با هک «ساموئل شای» طراح سفر نتانیاهو به امارات و معمار پیمان‌های ابراهیم، شبکۀ مخفی او را افشا کرده است.
🔹
به گفتۀ این گروه هکری، شای نه‌تنها هماهنگ‌کنندۀ اصلی تمام توافقات پشت‌پرده میان رژیم صهیونیستی و کشورهای حاشیه خلیج فارس است، بلکه تسهیل‌گر کلیدی روابط پنهان اقتصادی، سیاسی و امنیتی میان تل‌آویو و ابوظبی محسوب می‌شود.
🔹
براساس اسناد منتشر شده، شای، اپستاین را به «سلطان احمد بن سلیم» معرفی کرده و از این طریق بسیاری از حاکمان فاسد امارات در شبکۀ اپستاین گرفتار شده‌اند. موساد نیز از همین مسیر برای وادار کردن آن‌ها به پذیرش خواسته‌های خود استفاده کرده است.
🔹
گروه حنظله اعلام کرد امروز ۲۶۵ صفحه از تماس‌ها، شرکای مالی و ارتباطات محرمانۀ شای را به طور کامل در وب‌سایت خود منتشر کرده و تمام اطلاعات مرتبط با شبکۀ مالی او در کشورهای مقاومت را در اختیار سرویس‌های اطلاعاتی کشورهای دوست قرار داده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/435616" target="_blank">📅 00:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435614">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f20e0ec79.mp4?token=NHCT0_JP_mZvk0Iol2HO422q3lhTPJcU_cPI9peR5x82i5pPc5jGx9CLcm-n0iovWj26I-atYEQ5lmtGqyYupmc7091kBe7gpGqTtRVOmhruw9zDw9YbAdds3KYUUmoAXjS0r-taa2XH_3cDpX1vQ_iMxKgw9x9x93YQOJZpsz9l2A7r76r9o-BLnhVXbJg4Oz4ziet1CvynWEZYiIVpSprFM7kLkuSToJDwaWqYdHxaBowNDWaqi8rDwkRttDVfDt_0oDrl4rRo7sHUVOeqtcYeU1MYoDvUvAiHWzXNbFuR008NEvFcUVN8BiuBDnTrIEMBXbzSAZD_RbXU3FIOkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f20e0ec79.mp4?token=NHCT0_JP_mZvk0Iol2HO422q3lhTPJcU_cPI9peR5x82i5pPc5jGx9CLcm-n0iovWj26I-atYEQ5lmtGqyYupmc7091kBe7gpGqTtRVOmhruw9zDw9YbAdds3KYUUmoAXjS0r-taa2XH_3cDpX1vQ_iMxKgw9x9x93YQOJZpsz9l2A7r76r9o-BLnhVXbJg4Oz4ziet1CvynWEZYiIVpSprFM7kLkuSToJDwaWqYdHxaBowNDWaqi8rDwkRttDVfDt_0oDrl4rRo7sHUVOeqtcYeU1MYoDvUvAiHWzXNbFuR008NEvFcUVN8BiuBDnTrIEMBXbzSAZD_RbXU3FIOkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طفرهٔ فرمانده سنتکام از پاسخ‌گویی دربارهٔ پیش‌بینی بسته‌شدن تنگهٔ هرمز
🔸
هیرونو، سناتور آمریکایی: پیش از اینکه به ایران حمله کنیم، آیا این فکر به ذهن شما خطور کرد که ممکن است ایران تنگهٔ هرمز را ببندد؟
🔹
فرمانده سنتکام: یکی از مسئولیت‌های من ارائه طیف گسترده‌ای از گزینه‌ها همراه با خطرات و فرصت‌های مرتبط با آن‌ها به وزیر و رئیس‌جمهور است. فکر می‌کنم صحبت دربارهٔ اینکه آن گزینه‌ها دقیقاً چه بودند، نامناسب باشد.
🔸
هیرونو: بسته‌شدن تنگهٔ هرمز توسط ایران به ذهن شما خطور کرد؟ بله یا خیر؟
🔹
فرمانده سنتکام: تقریباً ۱۰۰ بار از تنگه عبور کرده‌ام. من تقریباً هر روز به تنگهٔ هرمز فکر می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/farsna/435614" target="_blank">📅 00:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435613">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679e1ebcfa.mp4?token=tC6fBWTvQjdLrgJH75Pp2QNpfHU3JReCDG2ElIsGR-j3iaX3yed2j-A3LVUzSoNxkis404AHuJY9aZPJXLGGqP2m4nLG8woJEZsetlv51dQRJxp7aUGYyzx7jk08gP033zUP8GNSPNTinyuptvOq2h4ZIsgDO4UhAGe2_dz8I-r_g__Vvg4ooUlHMhv-E3j-w4RcJr7si14woHCiQRE9LNSWdfLArU1MP1rjweOaA3TKseKHFBFCeey-yS_8pBIXloVFHNB-jSVx8URKdxVrxOkBsF7VXcaS-a2vjOaS5mqzkrlG0wGaq3GvLdzgYDVAXF_St0qSQYx8GKWRSZZcgatAV0Mv2pCI8uJ7DC9NHXYNLyfL9QXMi-jdjtbHw6h7JGSFq-gSewItqbDcuWDc0hzXqwLnQ4WawHTSML_gFx5zqq_2z0bt0jjwxxC8b70eRVxoqMEV6vnlXmLm0tnXqC8u4BU_vPvIxE0XzlGOlWL7H5b3t_Eov5MkMzyL-tX5cvG-7cCjZdZwg4CvQSCYeMKTTU-nmdk1SpgdIGiz5_TsrgRGRe1RcfMPfKmZqj1OuXapjc-5qgkciaEw-DXGVPWxoB4K096NBZKpJjZwNKMp2SlX11ZUZ-IuJZERdlT8K7h1hZAW5WihiLeDKKMCsiGmzDzE4ksiVL9ejouL9SY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679e1ebcfa.mp4?token=tC6fBWTvQjdLrgJH75Pp2QNpfHU3JReCDG2ElIsGR-j3iaX3yed2j-A3LVUzSoNxkis404AHuJY9aZPJXLGGqP2m4nLG8woJEZsetlv51dQRJxp7aUGYyzx7jk08gP033zUP8GNSPNTinyuptvOq2h4ZIsgDO4UhAGe2_dz8I-r_g__Vvg4ooUlHMhv-E3j-w4RcJr7si14woHCiQRE9LNSWdfLArU1MP1rjweOaA3TKseKHFBFCeey-yS_8pBIXloVFHNB-jSVx8URKdxVrxOkBsF7VXcaS-a2vjOaS5mqzkrlG0wGaq3GvLdzgYDVAXF_St0qSQYx8GKWRSZZcgatAV0Mv2pCI8uJ7DC9NHXYNLyfL9QXMi-jdjtbHw6h7JGSFq-gSewItqbDcuWDc0hzXqwLnQ4WawHTSML_gFx5zqq_2z0bt0jjwxxC8b70eRVxoqMEV6vnlXmLm0tnXqC8u4BU_vPvIxE0XzlGOlWL7H5b3t_Eov5MkMzyL-tX5cvG-7cCjZdZwg4CvQSCYeMKTTU-nmdk1SpgdIGiz5_TsrgRGRe1RcfMPfKmZqj1OuXapjc-5qgkciaEw-DXGVPWxoB4K096NBZKpJjZwNKMp2SlX11ZUZ-IuJZERdlT8K7h1hZAW5WihiLeDKKMCsiGmzDzE4ksiVL9ejouL9SY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین «حیدر حیدر» در اجتماع هفتادوپنجم مردم رفسنجان
@Farsna</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/435613" target="_blank">📅 23:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435612">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDF8lJFHRfpd5uW4QTdoGyBC_rd21yaSigxZ9aE331P9szWJS52DqQGEGx7cPmg1s1fKV7hKvEXxl8mnrgx9zc-BSOCLAA7JlQF2c_IiIp-fa0AGoY2Jw_QeOkahAVXPCtvxHToHpXV_gXvCXtxR4EkZqJgxXeehOfii60pJ2zRM-0i8ZyayYpcJAOo1SUjTMPr2gxlkQA858IbCbHWjEP8JOj651G0PwKrv42UyfBFMe91MOvnY4Lahy-UafJJ16nwuZbsQztorSkzwFm2Msxe5nTi8CfhtUo5dKajrsg39_yedlxJVlK2QNr0zpFcGj3U3XCcLmhbGQJREzfmNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: حداقل ۱۰ دانشمند آمریکایی کشته یا ناپدید شده‌اند  سلسله این حوادث از سال ۲۰۲۳ آغاز شد:
🔸
مایکل دیوید هیکس: دانشمند ۵۹ ساله آزمایشگاه پیش‌رانش جت ناسا (JPL) که در جولای ۲۰۲۳ درگذشت.
🔸
رانک مایوالد و مونیکا رضا: دو متخصص دیگر از JPL؛ مایوالد در سال…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/435612" target="_blank">📅 23:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c010d4779e.mp4?token=YaM1-jKB8nq5POZs-y-7GkK4LNfIA0IAOhyfxjlTVKRgcTeFCZN4w97qPBG7NRSqo7rWqd5ouVggVEDBC4tvQrJoxHpEUWcyPnj-gS0636ZvpwWJ35HCfGxmS0wGFcfFwpA0W19R7B4FSAKH5jQ-UYMqoO4l37F9qQIrlKjYCPj9tRqE5_nsTKK9rHUwXiAV5dh5VOLOELBwH8GvaMUUhLCdqmSGA_Ogg19EplW__gIGEs7rfhKkvHUlUoFxAK3JSXOMJ-HGLI3ZSu3KSHUsikr0oCzIqBNCwkMfLMR-xZVIjDx-B2GemGOL6Q3XG6C8nNUrd0pNTJybVvgk4-Md9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c010d4779e.mp4?token=YaM1-jKB8nq5POZs-y-7GkK4LNfIA0IAOhyfxjlTVKRgcTeFCZN4w97qPBG7NRSqo7rWqd5ouVggVEDBC4tvQrJoxHpEUWcyPnj-gS0636ZvpwWJ35HCfGxmS0wGFcfFwpA0W19R7B4FSAKH5jQ-UYMqoO4l37F9qQIrlKjYCPj9tRqE5_nsTKK9rHUwXiAV5dh5VOLOELBwH8GvaMUUhLCdqmSGA_Ogg19EplW__gIGEs7rfhKkvHUlUoFxAK3JSXOMJ-HGLI3ZSu3KSHUsikr0oCzIqBNCwkMfLMR-xZVIjDx-B2GemGOL6Q3XG6C8nNUrd0pNTJybVvgk4-Md9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم دامغان امشب هم شعار اتحاد و همدلی سر دادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/435611" target="_blank">📅 23:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZasWDh_D8azSt_0HIdlN2wCJwJmy-jKEFGJiChxANm6sZ4z4u6Wdv0dEnxyvWQ9TNy7R2Z6KPTm9AFQX9dP8dgxmmsppI2Z4ChB835fY0AlNbTZQ1USbR6YR7xV7nsNejU7WxOGwT_aD312W747vYebp3tv3-Y_sDAcVEtrjlL9Aup4OhOOe8GNDA9B2UoSGGL0B56w7pLg-La4MFLlHcLJDabIZdpfcmG2M-1KPYN3witsBFddoMM_ADO5DjROHMCROU_nHmwDDssJL9ysvMAYlXKPaXOtrSRxyU_1voZa_IutsxuAMLgSXqTjCT9SYEYz4MOTSx4hiPUlnV_ax3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش‌ قالیباف به رکوردشکنی نرخ بهرهٔ اوراق قرضهٔ امریکا
🔹
قالیباف با اشاره به خبر افزایش بی‌سابقهٔ نرخ بهره اوراق قرضهٔ آمریکا نوشت: پس شما درحال تأمین مالی هگست، مجری تلویزیونی شکست‌خورده، با نرخ‌هایی هستید که از سال ۲۰۰۷ بی‌سابقه بوده، تا او بتواند در حیاط خلوت ما در تنگه هرمز، نقش «وزیر جنگ» را بازی کند؟
🔹
می‌دانید چه چیزی دیوانه‌کننده‌تر از بدهی ۳۹ تریلیون دلاری است؟ این که برای تأمین مالی این جنگ‌بازی، نرخ بهره‌ای به اندازه دوران پیش از بحران مالی جهانی در سال ۲۰۰۸ بپردازید و در نهایت فقط یک بحران مالی جهانی جدید نصیب‌تان شود.
🔸
گفتنی است در روزهای اخیر بازده اوراق قرضه سی ساله آمریکا به بیش از ۵ درصد رسیده که این نرخ از سال ۲۰۰۷ یعنی سال پیش از بحران مالی جهانی بی‌سابقه است.
🔸
افزایش نرخ بهرهٔ اوراق قرضه به معنی افزایش انتظارات تورمی، افزایش نرخ بهره و بالا رفتن هزینهٔ وام‌ها و در نهایت وارد آمدن فشار تامین مالی جنگ با ایران به آمریکایی‌هاست. جنگی که با هدف تسلیم ایران آغاز شده بود حالا دارد اقتصاد آمریکا را تحت فشار قرار می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farsna/435610" target="_blank">📅 23:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435606">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/run7qsbuxvUXfJH-GrukODoGLV_sozXPEJsq-08sCAVHdyg8wwMqHHorelMIrREwA17CN_Kiu5BnRp55bzzwmjHhApi6nLOHW5FZPyputcQ3WNnefeyRBLKVyWix7ayMabOrk3mzyk3ryHCpLlEP6iQichkXJxsJx82NVEZHHDETklkd9BV7z_tiVgAFwdf87MijGb2bHowplqZd9MM9BOTN2bVhIP04gny6KNUhaoiabnkKw04XrNtniFbDDzBeYkYhS9FvW0vxLW9H56JcPncEWH4YFJfMZmJDUtgQkwN3T2F04Pau2YhLE50S3RZLDBexiDjA_YnZiMXUbgRX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jF78waXIQvFp5I5rYekk8EuSc7bH13WDGp6LmWDUbnMCapE3LSsTol-6HkqNgzuZ0lPXfAaucEglMU3ks5b1WqhAhGeum47WSH2HqI0zU5a-xko_r92EjEiOT0E9lZMGDqAxtyt5SX3zXCt5QR9r72rGTf4ea-fpIzj0_plgulxyRALfNqBb4uoswA2rSGb0jrSFqPYfmcPPLF0-BETiLwTo--P7Yj6Jkxa8l6zdgrE7-IlGr77rqGt_Pg-CrofHIn9DHax-qsoPYAuTyo20oy6n0TMwPYQckJp_CQmKSFLBPb1AfqgSgQC9LxhhDjGUS145up22JDH0ihgb1OAhnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqRgP1zJKlD6SZ-kDHeBx5W183MrXesP5tiF4LY6ApgVcnvJo-Yo0Oa4bWHiTXKCDtcxOltSPV2Bzc3srpoo_SMp8CIo_7J8Cytnwq3PplRSfOBhiaX7hFLxaDAz0gPu0YtHCH0y4GUWqzHeVsfJajoo_anfQqnSg_g0x2snz117044MEaSNJmtOlvmcXC7yNZ0htmlWsFhaw9zFIb1bLhk79Vl-fUNsFfAjCXq-ifaRM855WHvB8vg3rGd2D0M06cwydmfTO7ErYBOM5mOJz97uN607LCBXTDkSlh-xw8zmyHvltU5j_DIoxdf9X0-ySa7vcM5iTfJ_ehsoopTFLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amtFRAcJp9Kn7JuaFetMjpWtcGSOsAvlb6CGRbMRc8Ya8rKpTniN30oODmrg5o--XtFUwI5IYXJRXCktM4lzhwSMLfUaZxBhr3dQ7CSHFTJv2vggkACaBXutFp6ILoOAKtPBN2jerQiJpyhPz_T_8KoGcULaRFdOmed6S2MQPDY6blXzLYLFCZOR1jrUzQlSAoNyvt8qTK76EuNgzD7twHtEdB1nzTzqiNez1YD4CthuP__mJ4KjpzzZrZ6V-gT4WEnBsdHnDhQpB-K6DpXeqmCzniZBos9NCjNJxpaeri44EWtihI9J36Q12J_ZOowfSYb-7dt8M-SAS12HnbsvSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اربعین شهید سرلشکر سیدعبدالرحیم موسوی در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/435606" target="_blank">📅 23:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435605">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b9085ba5.mp4?token=LlL4QQ71XkeT1dLuyWJgYBpkHYY6q_AHFglZQh4PvedxFgNUBu56N7dfMRUvG3_c7TbjEVgAQ9HSSm5I_jBWH1eOD-ki0lXCWlF78HK3gYXvS1_M0DIuwbChluYJRBW62DfRuuSo0HmCL1077j9xhG1spAWpufqI7CkW9C09Lp8WnuWgHA8NC_eDSJLXfAAg14J2UaM23lkg1Qo56lkHvZ6wBVxCOD8Jm7qbPgQ4kmmDu5_oVgYnbdQlNlz31QKB6VUrcQLu3olgE5Y8UgYzfXz_lC2EIUHijJa8UsaEhlpkQ00sT0iF3HFx5a8FednEAz4IietYV7ePKFvro1G6RaZ2tpc-vxje0ZEhWTGBZPirCEGIusib8tt4u-mfGUYHy9lsGaNchcHhmxUeD5rSFg5VMeU7auxQ_wWdxTpb3g-CihPFn7Zh_8zA7kDD63k_-2stO59cIS5ccQ41pUYOVPXYGkfGyq_A78WB8qNXBPIDI5VD_FohRRtOvR4sgFYI9rtSg6Hkhp_assrlEgJHr3iOAJD2ulyVgfQGbuQ1LFk8libG8BsU0VzSvo3Yh-tL4jKEyaZFZQ-clqOlliPJ13SyLa3a52B73CZK32GYeAY8sNrwY850pKtf8bHhECHqP6AogF0zoUHEbu07AWS1iesNxfiJ7WkqzrdSIP0Mbqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b9085ba5.mp4?token=LlL4QQ71XkeT1dLuyWJgYBpkHYY6q_AHFglZQh4PvedxFgNUBu56N7dfMRUvG3_c7TbjEVgAQ9HSSm5I_jBWH1eOD-ki0lXCWlF78HK3gYXvS1_M0DIuwbChluYJRBW62DfRuuSo0HmCL1077j9xhG1spAWpufqI7CkW9C09Lp8WnuWgHA8NC_eDSJLXfAAg14J2UaM23lkg1Qo56lkHvZ6wBVxCOD8Jm7qbPgQ4kmmDu5_oVgYnbdQlNlz31QKB6VUrcQLu3olgE5Y8UgYzfXz_lC2EIUHijJa8UsaEhlpkQ00sT0iF3HFx5a8FednEAz4IietYV7ePKFvro1G6RaZ2tpc-vxje0ZEhWTGBZPirCEGIusib8tt4u-mfGUYHy9lsGaNchcHhmxUeD5rSFg5VMeU7auxQ_wWdxTpb3g-CihPFn7Zh_8zA7kDD63k_-2stO59cIS5ccQ41pUYOVPXYGkfGyq_A78WB8qNXBPIDI5VD_FohRRtOvR4sgFYI9rtSg6Hkhp_assrlEgJHr3iOAJD2ulyVgfQGbuQ1LFk8libG8BsU0VzSvo3Yh-tL4jKEyaZFZQ-clqOlliPJ13SyLa3a52B73CZK32GYeAY8sNrwY850pKtf8bHhECHqP6AogF0zoUHEbu07AWS1iesNxfiJ7WkqzrdSIP0Mbqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهرکردی‌ها در شب ۷۵ حضور خود برای جهاد صرفه‌جویی شعار دادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/435605" target="_blank">📅 23:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435604">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e145c4f6d.mp4?token=BXFn7wYnZdpFDHwPF4i-b9bmMTPjBu9QpC3BeH7ZXb5MiiV3tG6nm50McSU-ZwPIytZtnvYQ_AjfgPXVJFgiuDS-Pf9ylqtWfR79ktsOrwWm5gqjxFwvIeDSPnYNDfpVEjDsMFReKEFJtML-wdHOgudz6k8noYlLx5mexwukD85V7JMxVNj5tM2Gu0YKGyu6j8GfPxnaBZk7ZwygB4vyh9qMowGPmNeMCVT8SBQ7oKRX-megyrXFvUslOedDFfwR-3WbxFSgJGESBzsIyE3THssHTBZJMFyZaoOD69psXUvQYGItm2QlSTFVt8IemCXsOsGqVoNW2nDKTtdSchpiog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e145c4f6d.mp4?token=BXFn7wYnZdpFDHwPF4i-b9bmMTPjBu9QpC3BeH7ZXb5MiiV3tG6nm50McSU-ZwPIytZtnvYQ_AjfgPXVJFgiuDS-Pf9ylqtWfR79ktsOrwWm5gqjxFwvIeDSPnYNDfpVEjDsMFReKEFJtML-wdHOgudz6k8noYlLx5mexwukD85V7JMxVNj5tM2Gu0YKGyu6j8GfPxnaBZk7ZwygB4vyh9qMowGPmNeMCVT8SBQ7oKRX-megyrXFvUslOedDFfwR-3WbxFSgJGESBzsIyE3THssHTBZJMFyZaoOD69psXUvQYGItm2QlSTFVt8IemCXsOsGqVoNW2nDKTtdSchpiog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم میهن‌دوست محلهٔ زمزم و زهتابی در شب هفتادوپنجم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/435604" target="_blank">📅 23:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435603">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94c1849696.mp4?token=Z2KTwRshjq_UilANoa1ia7bXo5vqUGSaZ_wDn303wPJLcD4O48luuPZJ_GJQerKYpwk3g78u9DpWq0JANrrav-ZaFTqQUpX9thOyew6PpBhexgY_TR_ed91vTecC5HIujcMx4Ggp8GyTvkpkq-AM6Ea95puGiYlu2NmNOPxMnlEgAG6qpl5065UkNizdr1vT2OeWcf3OzDj3tRgFGG0TNY2IskPWE28Tpd0Z7fJ3QdL2XZBVEEkjAzf6K0GgxaOS3wj6eCyjUW9uRWCWO0vMcVFasrl6nlX9T-dNGgQux4QQO4acvPp8Lv7gwtqHDtq-jP_Sfdx6-sSRZ-RMsL_i-xevqi3nG4qD4y_NgrYl59oR7Z0k_jo1sTUPunwvMTZ76TJdNr7Cc5r2T4zVqeVW1xnaiBo3WR8S6jmMF_aXYuFTsRxZoEzSHbCpnkuI0xQCOncTARk6qrKeo_jYPZ76ffWZYhjl9QWGEqVsvO8t8VKMn6BMsSCSRVI4vf3emHMxsb1j3I2okXM9KU_D7bSc0LnluEbkl4lb_qYtUbp0HdY9Lbqh3uhhlEZzdxu3HCxZxsNzAbDivT9do21Gj6dhWMtFxIpE1SABl_tL-c_WevBgnul2bq_VKaNuPJsmeB_4H9g3G5MvtMsk5VjMWZYmn79z4TT7nfFoIdGP8OJZ6HE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94c1849696.mp4?token=Z2KTwRshjq_UilANoa1ia7bXo5vqUGSaZ_wDn303wPJLcD4O48luuPZJ_GJQerKYpwk3g78u9DpWq0JANrrav-ZaFTqQUpX9thOyew6PpBhexgY_TR_ed91vTecC5HIujcMx4Ggp8GyTvkpkq-AM6Ea95puGiYlu2NmNOPxMnlEgAG6qpl5065UkNizdr1vT2OeWcf3OzDj3tRgFGG0TNY2IskPWE28Tpd0Z7fJ3QdL2XZBVEEkjAzf6K0GgxaOS3wj6eCyjUW9uRWCWO0vMcVFasrl6nlX9T-dNGgQux4QQO4acvPp8Lv7gwtqHDtq-jP_Sfdx6-sSRZ-RMsL_i-xevqi3nG4qD4y_NgrYl59oR7Z0k_jo1sTUPunwvMTZ76TJdNr7Cc5r2T4zVqeVW1xnaiBo3WR8S6jmMF_aXYuFTsRxZoEzSHbCpnkuI0xQCOncTARk6qrKeo_jYPZ76ffWZYhjl9QWGEqVsvO8t8VKMn6BMsSCSRVI4vf3emHMxsb1j3I2okXM9KU_D7bSc0LnluEbkl4lb_qYtUbp0HdY9Lbqh3uhhlEZzdxu3HCxZxsNzAbDivT9do21Gj6dhWMtFxIpE1SABl_tL-c_WevBgnul2bq_VKaNuPJsmeB_4H9g3G5MvtMsk5VjMWZYmn79z4TT7nfFoIdGP8OJZ6HE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: کویت فراموش نکند که تنها در ۹۰ دقیقه توسط صدام تسخیر شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/435603" target="_blank">📅 22:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435602">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کشف ۲۱۰۰ تن برنج وارداتی احتکارشده در هرمزگان
🔹
سازمان جهاد کشاورزی هرمزگان: در نزدیکی بندر شهید رجایی بیش از ۲ هزار تن برنج وارداتی از کشورهای هند و پاکستان که به‌قصد احتکار و ایجاد بحران در بازار دپو شده بود، کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/435602" target="_blank">📅 22:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435601">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">مردم دیگر پس‌از وقوع حوادث به پمپ بنزین نمی‌روند
🔹
«یه پمپ بنزینمون نشه» جمله پرتکرار این‌روزها بین مردم در مواجه با حوادثی مثل جنگ یا زلزله است اما بررسی فارس نشان می‌دهد، پس از وقوع زمین لرزه در آخرین ساعات روز سه شنبه در تهران، تغییر در مصرف بنزین پایتخت اتفاق نیفتاده است.
🔹
از حدود ۲ سال پیش شلوغی پمپ‌بنزین رویدادی پرتکرار بوده که در روزهای ابتدایی جنگ ۱۲ روزه به اوج خود رسید.
🔹
صاحب یک جایگاه در مرکز تهران به فارس می‌گوید، میزان شلوغی و مصرف بنزین در هنگام حوداث طبیعی و غیر طبیعی بسیار کم شده و در زمین‌لرزه اخیر در بسیاری از جایگاه‌های تهران شاهد صف هم نبودیم.البته ممکن است در ساعاتی شاهد صف باشیم اما در جایکاه معدود برای زمان اندک است.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/435601" target="_blank">📅 22:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435600">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d401f8ad0.mp4?token=G2qhqOdpJ2ScZa5vxe0CdcSTF_czeStyyECimEMadT85_DxQK9xcxM6MmsDrKo_DJrioejfyfNzCbQ5qfr0E49dYDllLQEuF-k-zoP4sSsBquXW6mHGkQNgrhpRaNGj0lzYD-2BJ58awVfud3hwEe-YCGavkoQthCGcYm0fLicZlTySKr1CJr0MA-nbb7dTCKrLzHDHQq10TrQn-3BVeyC5ACi8P2XAuLTfLPYzNfOkIqbQOuwxa-iu_Snvvf246jkTFf8ThfHb1PEfOawFRq4MqBDCemJEvfESE91796N9INSU-dqOH-3j66_WhKmIkcsWMxvXwKZe-MaCBSsU16jRJzfVPo-CgXGFN1Fk27OTDEnIByc3jVvRXWoauKeTuPfc8vWAtHQ7mObOB0nm-upanqc8MpVxdGecgoJonkmBPcdDALlLkcFwQmQuO53UNKa_27RVbiRCIji0WtWsfaCUhS4feq2qSLp5MhEWaLrAIrvxNVlWpNwk2u-99TtamIvI4Eq3O6Htaji_IxTwqshcMzhAoOIwia19KwPgW_GxA-fjKObZ2j4npNd2806iElCCvthnqRCoq2_6hMMhsRwL0dOp5mBL4L3y0ONlYBNBNvW1-vvZg2pCq4kerCtW2epcH8ejCAgIC0wm-qi0O_FgXOCcPAUjL6MQoyjt7IJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d401f8ad0.mp4?token=G2qhqOdpJ2ScZa5vxe0CdcSTF_czeStyyECimEMadT85_DxQK9xcxM6MmsDrKo_DJrioejfyfNzCbQ5qfr0E49dYDllLQEuF-k-zoP4sSsBquXW6mHGkQNgrhpRaNGj0lzYD-2BJ58awVfud3hwEe-YCGavkoQthCGcYm0fLicZlTySKr1CJr0MA-nbb7dTCKrLzHDHQq10TrQn-3BVeyC5ACi8P2XAuLTfLPYzNfOkIqbQOuwxa-iu_Snvvf246jkTFf8ThfHb1PEfOawFRq4MqBDCemJEvfESE91796N9INSU-dqOH-3j66_WhKmIkcsWMxvXwKZe-MaCBSsU16jRJzfVPo-CgXGFN1Fk27OTDEnIByc3jVvRXWoauKeTuPfc8vWAtHQ7mObOB0nm-upanqc8MpVxdGecgoJonkmBPcdDALlLkcFwQmQuO53UNKa_27RVbiRCIji0WtWsfaCUhS4feq2qSLp5MhEWaLrAIrvxNVlWpNwk2u-99TtamIvI4Eq3O6Htaji_IxTwqshcMzhAoOIwia19KwPgW_GxA-fjKObZ2j4npNd2806iElCCvthnqRCoq2_6hMMhsRwL0dOp5mBL4L3y0ONlYBNBNvW1-vvZg2pCq4kerCtW2epcH8ejCAgIC0wm-qi0O_FgXOCcPAUjL6MQoyjt7IJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع شبانه مردم بجنورد با حضور کاروان زندگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/435600" target="_blank">📅 22:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435599">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b399cb7af.mp4?token=de0BEBMRAtyliWpdDyKRzNxhpCihtyM0_2K2-ZOkCTfQYw6DpSRKRTYrkPkuFEomDYJKJqftxa75AvtrKpgSJZxQz-TYmpqxEomhCMgatkD1PPZMLLeBsRejFTStg1tEc_R39tn9KLCsYa7hjljWZ90aKsPNmCw3RJIxYtiJTalEf79jb2o6oCMEEKSJwyJfJ3tkz4Xnq_pNNzBUQbfVXSLzlsqHEL9yLZAyUdtXo-IzBkXt9njBC11WA5wugY67xnssw-2Hl5oZix5lQuYKpm-9Ukd_yUKkdDbndXbT5o06FvUaycE9lsfu2gkx0T2ut62viLZf5zB1nOHsymL1Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b399cb7af.mp4?token=de0BEBMRAtyliWpdDyKRzNxhpCihtyM0_2K2-ZOkCTfQYw6DpSRKRTYrkPkuFEomDYJKJqftxa75AvtrKpgSJZxQz-TYmpqxEomhCMgatkD1PPZMLLeBsRejFTStg1tEc_R39tn9KLCsYa7hjljWZ90aKsPNmCw3RJIxYtiJTalEf79jb2o6oCMEEKSJwyJfJ3tkz4Xnq_pNNzBUQbfVXSLzlsqHEL9yLZAyUdtXo-IzBkXt9njBC11WA5wugY67xnssw-2Hl5oZix5lQuYKpm-9Ukd_yUKkdDbndXbT5o06FvUaycE9lsfu2gkx0T2ut62viLZf5zB1nOHsymL1Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت کارکنان بیمارستان میناب از مواجهه با انبوه دانش‌آموزان مجروح
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/435599" target="_blank">📅 21:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435598">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VramdMSD6wM4IWfCBUHz9ahRqZZOqeZUk195L2tvjDvdJ_pAxHjsR9yluGlqL2hhkVpcqars_lb6TvgVxMHj3bd_vNZUHnNIwcg1H6941B9lSabRBXkE9vtWaIAhljV1-CCCmjhFshqis5kIuN3NuY0sGQ5rSonsLKY35gplvAGN9gGnFRSYXpEQG1SXLMm1ptLok9JFFBHPsPXMyredfEZMYy3kIMhEkZ3WQTF2SQD9jAqrM61KkG4LbA5zCRo3jUgS5w_mpgvuGyWSSFyAtPDQd2kD26jm7PE5hTOuftHqGcN-mcqRCKtnlqc_Q5RCciUBpXvQg3WviP68oVRy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
علی الزیدی پس از سوگند یاد کردن، رسما به‌عنوان نخست‌وزیر عراق انتخاب شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/435598" target="_blank">📅 21:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435597">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d376cd237.mp4?token=koZB1qGFXeFe1yZh3NOYlW1RU9VyaFf2YHF349CHGpXKPq5UAE-vNASDN29efdITTQwuRpZLwss5Le6yxAJnsaJABt1ecza0WNeJhgOv9-MU7zRkvQqkmJ79_orenpN59GVpF_fNQvH-Zm5qGUs8nohMtWdbLXlRE9sX1dU6Oz4mwzFZqAKl_buCRiOOoZDfD9o3MkBTMceW9emcxnwxVYiiG_eduipUxtKdT6NhG6lcu95UBXE8QRvClcuMWaeA3PauZpSBR1ZmpdG882BeCOeQTxcoZgpCTb53ix7EiWoH_7qZCplbw6G2375p5aQ5EV1vscPoZYSYRQBFCSxULw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d376cd237.mp4?token=koZB1qGFXeFe1yZh3NOYlW1RU9VyaFf2YHF349CHGpXKPq5UAE-vNASDN29efdITTQwuRpZLwss5Le6yxAJnsaJABt1ecza0WNeJhgOv9-MU7zRkvQqkmJ79_orenpN59GVpF_fNQvH-Zm5qGUs8nohMtWdbLXlRE9sX1dU6Oz4mwzFZqAKl_buCRiOOoZDfD9o3MkBTMceW9emcxnwxVYiiG_eduipUxtKdT6NhG6lcu95UBXE8QRvClcuMWaeA3PauZpSBR1ZmpdG882BeCOeQTxcoZgpCTb53ix7EiWoH_7qZCplbw6G2375p5aQ5EV1vscPoZYSYRQBFCSxULw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برنامهٔ ترامپ برای ایران معکوس شد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/435597" target="_blank">📅 21:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435596">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186bafc9e9.mp4?token=HOnF-M6zmmztFppVzIDGSMGPnmzQj8hGuASI8e1SGllizInMIiL5k04gQpz7K7Z4Fx1tqkzI-P5xMu6XOYZHDo1eXFCTfebvb3Wau2KxPWysAzLyJR9jNn0h3iUFpDYAUX8f_VsgJYP0TrhPZxFUkpN0EPCyVxrTdgTrxYxUb_B8zZTarHejglhmSGw9Bj6b0QSGkWPiEX5yGdJXSj7JQRK-Kr8rjMBMwloV1dx-Dy5la8EtLoff3sOAHhXx420AUesZj7BlEuTkwVq6lf9VBkeLB32xX4JpNhJz2ZtjmwqU6vPK5ji9M8yUJ6OPJOTEf82gkA-FIpo4A8ohtcElWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186bafc9e9.mp4?token=HOnF-M6zmmztFppVzIDGSMGPnmzQj8hGuASI8e1SGllizInMIiL5k04gQpz7K7Z4Fx1tqkzI-P5xMu6XOYZHDo1eXFCTfebvb3Wau2KxPWysAzLyJR9jNn0h3iUFpDYAUX8f_VsgJYP0TrhPZxFUkpN0EPCyVxrTdgTrxYxUb_B8zZTarHejglhmSGw9Bj6b0QSGkWPiEX5yGdJXSj7JQRK-Kr8rjMBMwloV1dx-Dy5la8EtLoff3sOAHhXx420AUesZj7BlEuTkwVq6lf9VBkeLB32xX4JpNhJz2ZtjmwqU6vPK5ji9M8yUJ6OPJOTEf82gkA-FIpo4A8ohtcElWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی خطاب به امارات: ائتلاف با اسرائیل هم از شما محافظت نکرد
🔹
وزیر امور خارجه امروز در نشست وزرای خارجه بریکس در دهلی‌نو در پاسخ به ادعاهای بی‌اساس نماینده امارات گفت: ائتلاف شما با اسرائیلی‌ها نیز از شما محافظت نکرد و در سیاست خود در قبال ایران بازنگری…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/435596" target="_blank">📅 20:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435595">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بزرگترین توافق تبادل اسرای جنگ یمن انجام شد
🔹
دولت یمن از انجام توافق تبادل اسرا با دولت وابسته به عربستان خبر داد و آن را بزرگترین توافق تبادل معرفی کرد. رئیس کمیته ملی امور اسرای یمن با اشاره به اینکه «لیست اسامی ۱۱۰۰ اسیر و بازداشتی از طرف ما به امضا رسید» خبر داد که «در این تبادل، ۵۸۰ نفر از اسرای طرف مقابل از جمله ۷ اسیر سعودی و ۲۰ اسیر سودانی آزاد خواهند شد».
🔹
المشاط، رئیس شورای‌عالی سیاسی یمن ضمن تبریک این توافق گفت که «صنعا تمام تسهیلات برای تکمیل این پروندهٔ انسان‌دوستانه و آزادی اسرا را طبق اصل همه در برابر همه، ارائه کرده است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/435595" target="_blank">📅 20:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435594">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bae404a54.mp4?token=MTXKuLkShaIvNpNBBenGeqocjnA8SIwN6hPFR1LYEL6ky7Poxpvk2o7MH_eJ4fu82hrKK2k2hiZSg6swVPudxCjOh-xR0H6NGooI0tsPUocnqDoRj7CXYKwzNBpgPDS9tOEPvKaGOPCsWrshUOghtxzXk2BCyTvh40yH_py2PPWaNekQZWTPaKUx1bYHKtsEBhxnNe0en_MkO2rGVXgyg8-O-v53NG1rETKzzvwLIFD-24gXg8yMfo7fpmq4LjbHzCJ6UuLSHePyXeP8EbkzKxM8-0ta3hpE7kKqEYS3mzq35qyJXbAWLZ7ieONi3p9pXBCL5Emzb5uXBNr4G61miYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bae404a54.mp4?token=MTXKuLkShaIvNpNBBenGeqocjnA8SIwN6hPFR1LYEL6ky7Poxpvk2o7MH_eJ4fu82hrKK2k2hiZSg6swVPudxCjOh-xR0H6NGooI0tsPUocnqDoRj7CXYKwzNBpgPDS9tOEPvKaGOPCsWrshUOghtxzXk2BCyTvh40yH_py2PPWaNekQZWTPaKUx1bYHKtsEBhxnNe0en_MkO2rGVXgyg8-O-v53NG1rETKzzvwLIFD-24gXg8yMfo7fpmq4LjbHzCJ6UuLSHePyXeP8EbkzKxM8-0ta3hpE7kKqEYS3mzq35qyJXbAWLZ7ieONi3p9pXBCL5Emzb5uXBNr4G61miYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: هنوز هم روزانه یک میلیارد دلار صرف جنگ با ایران می‌شود
🔸
سناتور گیلیبراند: قرار است چند روز، هفته، ماه یا سال دیگر با ایران در جنگ باشیم؟
🔹
فرمانده سنتکام: ما در وضعیت آتش‌بس هستیم و مسیر پیش‌رو توسط سیاست‌گذاران تعیین خواهد شد.
🔸
سناتور…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/435594" target="_blank">📅 20:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435593">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727ca1076d.mp4?token=aQOtjbBcWRDUVnjWtYkR_KnmBPF-0ErN3uqNn4xiPKgyM0yCtjE-ynFX0dsIHrjznfFx_8P8G6vaN3BD1OPjjF5B72YG6kY1wtONPHxP-xB2-766ZyDpeFcpuyF6DqBLCwrRyIAi6woWcKwsAm9s4RYLSSBVk_gDUmG6ALGjIOzI2wlg4ZivcAzH9uZCsjHwsEd9OLlagnQUjlkfBtfiFkulBdc5UW3OvBS3S9nSjjSalcJqY-4gzrrO-mPssVF1_n6L6fIZnMV4bc5koJZVKxYG8k2QmC-41ksUrsu-ZyswokIQALuAseogzTpIBwOGMFx6qUBtXb1a19mdDqn7ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727ca1076d.mp4?token=aQOtjbBcWRDUVnjWtYkR_KnmBPF-0ErN3uqNn4xiPKgyM0yCtjE-ynFX0dsIHrjznfFx_8P8G6vaN3BD1OPjjF5B72YG6kY1wtONPHxP-xB2-766ZyDpeFcpuyF6DqBLCwrRyIAi6woWcKwsAm9s4RYLSSBVk_gDUmG6ALGjIOzI2wlg4ZivcAzH9uZCsjHwsEd9OLlagnQUjlkfBtfiFkulBdc5UW3OvBS3S9nSjjSalcJqY-4gzrrO-mPssVF1_n6L6fIZnMV4bc5koJZVKxYG8k2QmC-41ksUrsu-ZyswokIQALuAseogzTpIBwOGMFx6qUBtXb1a19mdDqn7ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: هنوز هم روزانه یک میلیارد دلار صرف جنگ با ایران می‌شود
🔸
سناتور گیلیبراند: قرار است چند روز، هفته، ماه یا سال دیگر با ایران در جنگ باشیم؟
🔹
فرمانده سنتکام: ما در وضعیت آتش‌بس هستیم و مسیر پیش‌رو توسط سیاست‌گذاران تعیین خواهد شد.
🔸
سناتور گیلیبراند: در حال حاضر، ما همچنان روزانه یک میلیارد دلار هزینه صرف جنگ با ایران می‌کنیم. مردم از این موضوع خشمگین هستند.
🔸
این رقم می‌تواند صرف کاهش هزینه‌های مسکن، کاهش هزینه‌های غذا، کاهش هزینه‌های درمانی و پایین آوردن مخارج روزمره‌ای شود که به‌دلیل جنگ در ایران مدام درحال افزایش است.
🔸
معنی قیمت بالای بنزین و گازوئیل این است که هر چیزی که آمریکایی‌ها باید برای خانواده‌هایشان بخرند گران‌تر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/435593" target="_blank">📅 20:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435592">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcfaecd0d.mp4?token=G_Kpb-9nuE7xKF23lm0RCjxnuKdT6QqFqPQwPqkevuHf5QFubxqBpdDbiXhGfDZbCkzP5OY_plK_EEHzOSa9CPZ1jZFu1AKr6XDTSmCt-WfzmZPs1ZEH-2n1Kxz4Shg2A17dHfuaxBliXoDyVngFw_C5aNeCyBgsVplCNo39We5YyeUmVad4YhGdCj9E1Ivy-OZ8MvG1JRqA8oYzOmf2B__zlMxN-IUENzn7KqFOl30SAXYKEMUUwLZcbp-gJQ-bW2LJ1xmEU1SYBykXf8E7NzNUe0V2Ynk8P3C-I_2KIkirLOGpn9wV1Guk9kvQjc_jr5y7GPWLG_57ztxsHEv-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcfaecd0d.mp4?token=G_Kpb-9nuE7xKF23lm0RCjxnuKdT6QqFqPQwPqkevuHf5QFubxqBpdDbiXhGfDZbCkzP5OY_plK_EEHzOSa9CPZ1jZFu1AKr6XDTSmCt-WfzmZPs1ZEH-2n1Kxz4Shg2A17dHfuaxBliXoDyVngFw_C5aNeCyBgsVplCNo39We5YyeUmVad4YhGdCj9E1Ivy-OZ8MvG1JRqA8oYzOmf2B__zlMxN-IUENzn7KqFOl30SAXYKEMUUwLZcbp-gJQ-bW2LJ1xmEU1SYBykXf8E7NzNUe0V2Ynk8P3C-I_2KIkirLOGpn9wV1Guk9kvQjc_jr5y7GPWLG_57ztxsHEv-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: حمایت آمریکا از دیکتاتوری پهلوی باعث وضع کنونی ایران شد
🔹
تیم کین: من بارها و بارها صحبت‌های ترامپ و وزیر جنگ را درباره اقدامات بد ایران از سال ۱۹۷۹ شنیده‌ام اما بخش زیادی از داستان هست که مردم درباره‌اش حرف نمی‌زنند؛ تاریخ از سال ۱۹۷۹ شروع نشده است.
🔹
آمریکا در سال ۱۹۵۳ (سال وقوع کودتای ۲۸ مرداد)، کودتایی را برای سرنگونی دولت دموکراتیک ایران رهبری کرد. آمریکا یک دیکتاتوری یعنی «شاه ایران» را سرکار نگه‌داشت و پلیس مخفی او یعنی «ساواک» را آموزش داد؛ سازمانی که هزاران ایرانی را شکنجه کرد، تبعید کرد، به زندان انداخت و کشت.
🔹
۲۶ سال بعد از آن، انقلاب سال ۱۹۷۹ رخ داد و بله، آن زمان بود که شعار «مرگ بر آمریکا» سر داده شد. حمایت آمریکا از یک دیکتاتوری و سرنگونی یک دولت منتخب دموکراتیک، منجر به ایجاد ایرانی شد که [با ما] بسیار خصمانه رفتار کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/435592" target="_blank">📅 20:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435591">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
اوباما درباره برجام: بدون شلیک یک گلوله برنامه هسته‌ای ایران را متوقف کردیم
🔹
رئیس‌جمهور اسبق آمریکا: ما بدون شلیک یک گلوله آن را متوقف کردیم. ۹۷ درصد اورانیوم آنها را خارج کردیم.
🔹
هیچ بحثی وجود ندارد که آن توافق را کار کرد و لازم نبود ما عده زیادی آدم بکشیم یا تنگه هرمز را ببندیم.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/435591" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435590">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsKGh16NS6iGQEq36m2TrOM3HjkgFIdbKBIaiirfRTb01vFiyfi_F7QmIl0YV0mPYPBq1WztsQScxNhQ0Av0oT4daeI6NU9WULRH6zOa9stwlsmlYzs2lLZqSZP2nuMGGnkv9IV8sDUDyIFAO_DHzT-zLsyDC8dvq0jkgwCNBchP7IlJnsQ0pvoYVtwFFKlbLnxGVZhrtNjOfKbY2ytYDOHQfL9qAE9i1xtfYkBpa-vENLlbj0ET_0tCq9hLNzwXyWd-l83AYMGIAKotHxTvHMhdse8o3aGcUJ1l0CRShItWVP3Jy5KrRJtZKO4v8eNXvL7cLiJPaKipDFo3Sm0AWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهاد صاحب‌خانه‌ها در میدان مسکن
🔹
در روزهایی که فشارهای اقتصادی بیش از گذشته بر دوش خانواده‌ها سنگینی می‌کند، پویشی مردمی شکل گرفته تا مالکان را به همدلی با مستأجران و پرهیز از افزایش اجاره دعوت می‌کند؛ حرکتی که می‌تواند در کنار مقاومت مردم در عرصه‌های دیگر، به کاهش فشارهای معیشتی هم کمک کند.
🔹
مردم این سرزمین هرگاه ندای عدالت و مساوات شنیده‌اند، از یاری یکدیگر دریغ نکرده‌اند. این پویش هم تلاشی مردمی است؛ دعوتی به همدلی با مستأجرانی که این روزها زیر فشار شرایط اقتصادی قرار دارند و چشم‌انتظار همراهی و گذشت مالکان‌اند.
🔹
اینجاست که نقش مالکان می‌تواند تعیین‌کننده باشد؛ کسانی که می‌توانند در این میدان هم همچون سرداران یک نبرد، با گذشت و همراهی، به مردم و جبههٔ اقتصادی کشور یاری برسانند؛ همان‌گونه که در سیرهٔ بزرگان دین و فرهنگ هم بارها دیده‌ایم که گذشت از منفعت شخصی، راهی برای سربلندی جمعی بوده است.
🔹
اکنون پرسش این است که شما در کجای این جبهه ایستاده‌اید؟ آیا مالکی را می‌شناسید که در این نبرد، با گذشت و همراهی، نام خود را در کنار مردم ثبت کند؟ نام او را همراه با روایت این گذشت خیرخواهانه برای ما ارسال کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/435590" target="_blank">📅 19:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435589">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59b3bde01.mp4?token=OeIe5rsdRk9bd67a3c6EUAgAv9-gC40x3CPFlJFXY7BCYzLBDPpkZ4oOfsC4Rf6XnFU2bLvFWuutD01gRXScw0uYZWUZ4FZnpAmWJKj5g-1zWfJuBEk6TmqG2O4wN6qWp9gTzh0qgg9U72_Bpm8-Ol1QbN0VPEWemkvNX_WuM5__vdL5RoEtOMusD4DZx_Uh8KrgOv-PdRo4ggtAOQDFNvWapsHyEPeTJnxGjHQwxcyCQAxnvteBg-b7_XtLqqCr1D5Bgv4h9jTAJU_KAxCXLDWevqzMTDHmnspJFq2ZBURYk40WHi3ypRcKtIBy851OYYuUkudgfyMPoa7Z-L3Zog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59b3bde01.mp4?token=OeIe5rsdRk9bd67a3c6EUAgAv9-gC40x3CPFlJFXY7BCYzLBDPpkZ4oOfsC4Rf6XnFU2bLvFWuutD01gRXScw0uYZWUZ4FZnpAmWJKj5g-1zWfJuBEk6TmqG2O4wN6qWp9gTzh0qgg9U72_Bpm8-Ol1QbN0VPEWemkvNX_WuM5__vdL5RoEtOMusD4DZx_Uh8KrgOv-PdRo4ggtAOQDFNvWapsHyEPeTJnxGjHQwxcyCQAxnvteBg-b7_XtLqqCr1D5Bgv4h9jTAJU_KAxCXLDWevqzMTDHmnspJFq2ZBURYk40WHi3ypRcKtIBy851OYYuUkudgfyMPoa7Z-L3Zog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جونی ارنست، سناتور آمریکایی: عملیات‌هایی که علیه ایران انجام دادیم بدون وجود شرکای فوق‌العاده در منطقه امکان‌پذیر نبود
🔹
ما شاهد بودیم که بار بزرگی بر دوش اسرائیل و اردن بود. ما کمک‌هایی از بحرین و امارات دریافت کردیم که حجم قابل توجهی از آتش حملات را متحمل…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/435589" target="_blank">📅 19:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435588">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b441fded1.mp4?token=TOXnq0IIiPpxr6TD1JfTUwsT0RbVX6xcrK2zp1OMnoYd7ugnOFPBpXbSQFs38tDrdYumdxzr4JOnjj2WyP4REFSWzIESQX1CDjbCQgvA7OiW0vTX5mj2lHPAdFD2qUEBo7uWquj_HvLWrIvCLTOMcHjxW1CZmTafOgVBQwGmimdVq4PGr_bF66V_fiiy7eChlTQNW3PVkUoeB0oPD9ZSl5AKbnuGvasf7PZSyT2_4-Msh9GP0boxqaHs2RBzkm0p9joyhVCmZ-dFPvdKO0pcx18uTrXMc1Z6ixxeA2hWYLFHysjI4PxyzqxUgNrxSfHvbGT14J8PddT3V7zgUMSpeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b441fded1.mp4?token=TOXnq0IIiPpxr6TD1JfTUwsT0RbVX6xcrK2zp1OMnoYd7ugnOFPBpXbSQFs38tDrdYumdxzr4JOnjj2WyP4REFSWzIESQX1CDjbCQgvA7OiW0vTX5mj2lHPAdFD2qUEBo7uWquj_HvLWrIvCLTOMcHjxW1CZmTafOgVBQwGmimdVq4PGr_bF66V_fiiy7eChlTQNW3PVkUoeB0oPD9ZSl5AKbnuGvasf7PZSyT2_4-Msh9GP0boxqaHs2RBzkm0p9joyhVCmZ-dFPvdKO0pcx18uTrXMc1Z6ixxeA2hWYLFHysjI4PxyzqxUgNrxSfHvbGT14J8PddT3V7zgUMSpeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جونی ارنست، سناتور آمریکایی: عملیات‌هایی که علیه ایران انجام دادیم بدون وجود شرکای فوق‌العاده در منطقه امکان‌پذیر نبود
🔹
ما شاهد بودیم که بار بزرگی بر دوش اسرائیل و اردن بود. ما کمک‌هایی از بحرین و امارات دریافت کردیم که حجم قابل توجهی از آتش حملات را متحمل شدند.
🔹
عربستان و قطر نیز تماشاگر نبودند و فعالانه مشارکت داشتند. دسترسی به پایگاه‌ها، لجستیک و همکاری‌های اطلاعاتی آن‌ها از نظر عملیاتی برای ما بسیار حیاتی بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/435588" target="_blank">📅 19:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435587">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e98740f13.mp4?token=bCSblqwfdPwbh7--0ra3Y0uu5rymZoObsH6w0oaQ2N7_P3L0okg4Cc69ObDZdvNFWYw5Bd4tRi2mxYbBcSzOpEI7U4rAVbWJfzNYB9UIt6tbIPCaejELxYrI9Sa3BAcAaML_ngbP4aDksay4Y21M1_S867oBHQO-nxRJx7fW7ebduVgJ1_YSYOXyC7noly4DtFFt85F6SQYeHf-_GE1TXdQqr2Ht-xp3uGOS9kYozH9LNraXcmzSzTyl6xZuxNay1HKaDXnoL6KCjho_VHwZxu7nsQjRgwykGlLLm-L9_1YfDJkknqNAwtiVv0IHfihGlLBuHAlKphjqZiGuMDCADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e98740f13.mp4?token=bCSblqwfdPwbh7--0ra3Y0uu5rymZoObsH6w0oaQ2N7_P3L0okg4Cc69ObDZdvNFWYw5Bd4tRi2mxYbBcSzOpEI7U4rAVbWJfzNYB9UIt6tbIPCaejELxYrI9Sa3BAcAaML_ngbP4aDksay4Y21M1_S867oBHQO-nxRJx7fW7ebduVgJ1_YSYOXyC7noly4DtFFt85F6SQYeHf-_GE1TXdQqr2Ht-xp3uGOS9kYozH9LNraXcmzSzTyl6xZuxNay1HKaDXnoL6KCjho_VHwZxu7nsQjRgwykGlLLm-L9_1YfDJkknqNAwtiVv0IHfihGlLBuHAlKphjqZiGuMDCADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الزیدی به عنوان نامزد نخست‌وزیری عراق معرفی شد
🔹
منابع عراقی خبر دادند که چارچوب هماهنگی شیعیان به‌عنوان فراکسیون اصلی پارلمان عراق، علی الزیدی، فعال اقتصادی عراقی را به‌عنوان گزینۀ نهایی خود انتخاب کرده است. @Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/435587" target="_blank">📅 19:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435586">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc997db7c.mp4?token=NPFL8_Msik92doO5jQ1PT5MhrcwSclfI81UCysxGyOA8MySDBuSrUWcn43vxePWPVJwyBYWiZHK50iZXUJnjX7IWTkmmVhA2oz6XhXr9cslV8PnAFJXnBpfp1_h_1RlhkstpbtsYWxZKiiswj66fp-vMP5UOcfsT8pQQ3Je7gc66EIIWaQx-pfSeHUk_ydQPW2XHCFB7RdD7j0vptE5mRvcGuGYGQoDWEZ0lJJVyb2eoSrHnmYJe00b8cTrOVZnTqAqR1vOczniT-STgXSEmR_bDmkUkiI7A18O2FJUxaJMsODYJtC2LMZSLnz0Ca2X8QeJ3xg9suiT38pXNqWaSNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc997db7c.mp4?token=NPFL8_Msik92doO5jQ1PT5MhrcwSclfI81UCysxGyOA8MySDBuSrUWcn43vxePWPVJwyBYWiZHK50iZXUJnjX7IWTkmmVhA2oz6XhXr9cslV8PnAFJXnBpfp1_h_1RlhkstpbtsYWxZKiiswj66fp-vMP5UOcfsT8pQQ3Je7gc66EIIWaQx-pfSeHUk_ydQPW2XHCFB7RdD7j0vptE5mRvcGuGYGQoDWEZ0lJJVyb2eoSrHnmYJe00b8cTrOVZnTqAqR1vOczniT-STgXSEmR_bDmkUkiI7A18O2FJUxaJMsODYJtC2LMZSLnz0Ca2X8QeJ3xg9suiT38pXNqWaSNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی فرمانده سنتکام را به چالش کشید
🔸
بلومنتال: آیا موافقید که در اختیار گرفتن اورانیوم‌های غنی‌شدهٔ ایران مستلزم حضور نیروی زمینی و تلفات قابل توجه برای آمریکاست؟
🔹
فرمانده سنتکام: با توجه به ماهیت محرمانهٔ برنامه‌ها، صحبت دربارهٔ برنامه هسته‌ای بسیار نامناسب است.
🔸
بلومنتال: دشمنان ما بسیاری از چیزهایی که ما می‌دانیم را می‌دانند. کسانی که از حقایق بی‌خبرند، مردم آمریکا هستند.
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/435586" target="_blank">📅 19:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435585">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dmygsr7yViADn1F4Xl29UoXsfpUysx4wiyCOgqvUb-Nwik1js3yR8S5SB70VmpVM70uF_eTumFsCcMmC-LBW3jD0cnUErEw1A6UA9YiPlqGoFn9FYG1IQ0rS6Yy86QJYc82_A03qEVYGfRy_qypZfbqt_-whcgOtEYAEY1P98DBbLFaLOu_upM4vtHzjbtWTlbrXqhlADfhJBGjydUpdKGoUGwBY2jqtfsBAY6NFKgHyoD-Hh6f0PqG2cUwCTJQPuk0af4n3WcPlFMDrwkhN9oiNQvRfFyhJlH2BvlNUFzv7xgu1bbF7jSmKVWSEsAhC2DOIxJPSi_zfeiB_2ys4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عراقچی در حاشیهٔ نشست وزرای خارجهٔ بریکس با مشاور امنیت ملی هند دیدار و گفت‌وگو کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/435585" target="_blank">📅 19:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435584">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69aba23e2a.mp4?token=qHvq06ZQva5W0AlFg1mIDNVUCsGvRB5xtCwYrPlGLDod8xx5IW3nXhY6BqaQP4wIchhSBDlDkqxaPT7pwoeFgs5EvyxMKESv_cSCdv1N6FJOxuxLlpLNuxyl-vs3J7Op7fJQCVOYMr8HSXv08K_FhKyu1KktKKCTp5GXizGGAIGYnwq8Uaug9VfIOxYjoE-ZoBEhWQsvdJAFcy7BOCLXSCDbwuB9dWOxi-uuQdyCKfW5ZC47SXgddJ_LPUG-OG5tNhagp9DZ81hvXzyfOfBOsyMx9pAZPvhpdpKT7JFbu6Sp97cqfP9iG9Nelg6tqU3UVld9Xe2pb1GTdgSt37ILqwA_FtlghNMrKBFZwvri6kPU0JfIEf8VGDYiC2Xv92Dtv4kdHeiDGANf4aOc5knPUkIiqHZl2oCU5KVLH6DgsX_mLVMQmX-mXaHxrOB-kqnujSWhi4hSACQ6tsYAg68L4dZVLvDkXbaUOG4f6hTcsy3ymiYhXlEnNjn_MSa-iSt0PNDxgbJnoLOzWG6RJuVSO47o83jZl9C_mg-ozOc1tlTu_dQz8AXHyV-riBPUbA44_uUhSqCz90O2nTmYu9OdOfKQaQJ8lZbYEA1J4TXmleVsPqJE0xQi_rWoYsPu1g2LCcctG1q_IG3HcW4nNJ-evX_SafR2JzQguHxpILH-PQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69aba23e2a.mp4?token=qHvq06ZQva5W0AlFg1mIDNVUCsGvRB5xtCwYrPlGLDod8xx5IW3nXhY6BqaQP4wIchhSBDlDkqxaPT7pwoeFgs5EvyxMKESv_cSCdv1N6FJOxuxLlpLNuxyl-vs3J7Op7fJQCVOYMr8HSXv08K_FhKyu1KktKKCTp5GXizGGAIGYnwq8Uaug9VfIOxYjoE-ZoBEhWQsvdJAFcy7BOCLXSCDbwuB9dWOxi-uuQdyCKfW5ZC47SXgddJ_LPUG-OG5tNhagp9DZ81hvXzyfOfBOsyMx9pAZPvhpdpKT7JFbu6Sp97cqfP9iG9Nelg6tqU3UVld9Xe2pb1GTdgSt37ILqwA_FtlghNMrKBFZwvri6kPU0JfIEf8VGDYiC2Xv92Dtv4kdHeiDGANf4aOc5knPUkIiqHZl2oCU5KVLH6DgsX_mLVMQmX-mXaHxrOB-kqnujSWhi4hSACQ6tsYAg68L4dZVLvDkXbaUOG4f6hTcsy3ymiYhXlEnNjn_MSa-iSt0PNDxgbJnoLOzWG6RJuVSO47o83jZl9C_mg-ozOc1tlTu_dQz8AXHyV-riBPUbA44_uUhSqCz90O2nTmYu9OdOfKQaQJ8lZbYEA1J4TXmleVsPqJE0xQi_rWoYsPu1g2LCcctG1q_IG3HcW4nNJ-evX_SafR2JzQguHxpILH-PQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف تلخ کارشناس اینترنشنال: رسانه‌ها برای مردم یک دروغ فانتزی از جنگ ساختند  مهدیه گلرو، کارشناس اینترنشنال:
✅
در این جنگ بچه‌‌های مردم کشته شده و خانه‌‌های مسکونی مورد هدف قرار گرفتند. رسانه‌ها برای مردم یک دروغ فانتزی از جنگ ساختند.
✅
جنگ بخاطر مردم…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/435584" target="_blank">📅 19:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435583">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0ea89f96.mp4?token=DHZaCopXGKqpmAr_nEFhNLPnSYfbIkU6qI7JgqUnYRVpqiTFqHdCb2iKsijbUJgcHrHLVo6zH8aTsRRgXgEdQTciQ-jovpem736Ik0ddjJv_YwtUthrBt3juX9bOIFkPPYsBzAl064JMTQrXycReEsRS0VFbPGBcNzpOHZWCbOoPm6wt9zXsyOysnb2lXQij-dApj0MkMXq4vyzlwAvMFRuqtSvjaKyqfF7j722wqkq7CX1-FfjZxszxMGoi7Y-wvnUe4LFSMU3JeELMmRdjStF47pXdYijIw2jL8tj2YOE42xBypZXntR4vYGDGSNW9E9d8pVEiqkHgXewri7hTNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0ea89f96.mp4?token=DHZaCopXGKqpmAr_nEFhNLPnSYfbIkU6qI7JgqUnYRVpqiTFqHdCb2iKsijbUJgcHrHLVo6zH8aTsRRgXgEdQTciQ-jovpem736Ik0ddjJv_YwtUthrBt3juX9bOIFkPPYsBzAl064JMTQrXycReEsRS0VFbPGBcNzpOHZWCbOoPm6wt9zXsyOysnb2lXQij-dApj0MkMXq4vyzlwAvMFRuqtSvjaKyqfF7j722wqkq7CX1-FfjZxszxMGoi7Y-wvnUe4LFSMU3JeELMmRdjStF47pXdYijIw2jL8tj2YOE42xBypZXntR4vYGDGSNW9E9d8pVEiqkHgXewri7hTNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: رئیس‌جمهور چین به من گفت پکن به ایران تجهیزات نظامی نخواهد داد اما در عین حال گفت چین به خرید نفت از ایران ادامه می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/435583" target="_blank">📅 18:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435582">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrBZ-Gy9HQ6XZV7z7WJYHWbDl3LznnobBELXk67wW8EThnl-sfC2sQwzIFeWqZexuR8mHj2-E8MzXtlmb6H3KWoABuXh_KZWfITnJkH8Z-gi9c-zBBMTPpiIyK0K4wlrL1LQ0Y3trpPjdpjIaIepPzcb4jGv6VUYPs6GBv32PLn225CswNrxECoXfE9Jy3cE9s-TSqo6Y-4WthCvCiAO1_oGWFCgBljkCXWb9fxmDDH9LGw9jMoyzQo7Z18otUXyUuBqjQmMxMYNqcJPH8PICdWMJ8eHh0v3KMFFWg4qOX-1YvXr-XLyEXEa6zCJRg-nUFRSiPcLdwysWWY3hzqxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه اسرائیلی: علت تکذیب سفر نتانیاهو به امارات، ترس از ایران است
🔹
شبکه ۱۲ اسرائیل گزارش داد که تکذیب سفر نتانیاهو از سوی مسئولان اماراتی‌ ناشی از ترس است؛ زیرا ابوظبی می‌ترسد به عنوان یک طرف در محور ضد ایران، ظاهر شود.
🔹
این شبکه با اشاره به ترس امارات از  تشدید تنش‌های منطقه‌ای، گزارش داد، ابوظبی نگران است که به خاطر روابط با اسرائیل، به هدف مستقیم حملات ایران تبدیل شود.
🔹
بنا بر این گزارش، امارات در تلاش است است که سطح حضور خود را در مورد روابط با اسرائیل نسبتاً پایین نگه دارد.
🔹
این شبکه می‌گوید اماراتی‌ها با این تکذیب به رسانه‌های اسرائیلی این پیام را دادند که روایت رسانه‌ای مربوط به روابط با اسرائیل باید کنترل شود.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/435582" target="_blank">📅 18:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435581">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-35.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/435581" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-34.pdf</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/435581" target="_blank">📅 18:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K100jYzRL7DeZ7IkxootdsZX5BtNKuPEOTZYNQrCJAVss92IHa_uUw7R0pWHvbJJbuCRks9IYTwsBHHp4pkPVa3Pnmny2uKSTIBs8-aLU5ZI6ZiI76bU_EuNLmoQ9vhsyUK8R7I2Vr0vrW3zYyJHnHsWsXMffuFWwa2dUgRjLNin5M7JdTmmj3NFeUWxEYQe5NdGX75ax4dtV4Wy2tlRMdzy-gaGwJtfwTwvlSc7qaQkNGCZfwzl3Dm9THVDYOFBk_qgiUmp7WXbYGwXavCn-6oJXP0GpvgI7lmc74bt3zdSxjVoNPvYrky_Fk5JiGgVi4t-yPZ4MyStV5ULtIpFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: مردم ایران نشان دادند راه گذر از مشکلات، همبستگی ملی است
🔹
همانطور که مردم در جنگ ۴۰ روزه کنار هم ایستادند، دوران بازآفرینی را هم با همدلی و وفاق پشت سر خواهند گذاشت.
🔹
من از همه مردم برای این میزان موقعیت‌شناسی، فداکاری، ایثار و تلاش سپاسگزارم، ایران را با هم می‌سازیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/435580" target="_blank">📅 17:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435579">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Za2c7RsyZYcsICAnSFI2Lwqxuk4kxGjWua_bhhZuj88h7dbn1E5vzmdcdFgCIGXUictrGJHzWOhMqtGhgCrvY-RRYEBRBxxLB8a2oGbhS9avDwXGMxo9ES5wgQz4CDLziI6t7kDI9mPq4fwVUtQswv3meYpFlIgUerieibVWIjco1XEsmgWnXAf5Obb8v9aF3XnH59xATycSf8hCSiXLfuO_Bk04h-RsPzVmO7xK2QTefdKeTCs1RXX0WjtvG3XpGmW_uakPSLxZyLY3TWbstNO7fLKtYUz0tbIG5FMIqLT2SXVUK0lpsxD0FPazXR2pgU1svWHfEzKU-S9VBy-OLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در دهلی‌نو با لاوروف دیدار و گفت‌وگو کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/435579" target="_blank">📅 17:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435578">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb2fdc28f.mp4?token=qg4pseYm5XGqrdLzY9vls7a3R_9uhs2ftE-GUJONAS_7-ZBVfZJiHX-XJcNG2EFRzlP4zxBjOYoeYgzf4Xf024M3G3Ecp7mt5yq3xDFMVXSzzgYtmkJsA55uH64qR0Eqnte57XqaWgVLHfBcLY1NE8Vvvf0zXRCzlGxMv6nFEBusoVaQc4lWgQsiYPEj3lp5ldEyNVsnafmR0AJNTIQL-5qHyLvtc-MhBO0-UrpVw6XtkrSp5Jp-9Tor_WNgE7OanxJVlX3LRAJMXK0yspR-6tAtO9Ac5M4GBlEI1JcpWBRZUY6VHtJ3BDqwB8qJ_jwBxIQbbYxBnx6IgshgSpBCbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb2fdc28f.mp4?token=qg4pseYm5XGqrdLzY9vls7a3R_9uhs2ftE-GUJONAS_7-ZBVfZJiHX-XJcNG2EFRzlP4zxBjOYoeYgzf4Xf024M3G3Ecp7mt5yq3xDFMVXSzzgYtmkJsA55uH64qR0Eqnte57XqaWgVLHfBcLY1NE8Vvvf0zXRCzlGxMv6nFEBusoVaQc4lWgQsiYPEj3lp5ldEyNVsnafmR0AJNTIQL-5qHyLvtc-MhBO0-UrpVw6XtkrSp5Jp-9Tor_WNgE7OanxJVlX3LRAJMXK0yspR-6tAtO9Ac5M4GBlEI1JcpWBRZUY6VHtJ3BDqwB8qJ_jwBxIQbbYxBnx6IgshgSpBCbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله تصاویر اصابت مستقیم پهپاد انتحاری به خودروی نظامیان صهیونیست را منتشر کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/435578" target="_blank">📅 17:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435577">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca48112cfe.mp4?token=qAevsJTDsww3IywZFaJxblJq0b8-wfrM35lLe5cWDMXfj2WNSy6kjNVF5gRGy1mV_P9xdx-z3k4zKDgTRC3giyq95a4aK9kCFvmkT-N8yxjMt3B1qmK8M1VUXIPywnbH63K4UkJuwcvUjW22-ajmeqXDwVlHFe7q0OxVWa8bWwZDTF2rUOXGy4oUm33cVWMsUS6gAamPb43g29zHeAjdJ-tzRm-vEsDqE9Ib0-dEHp4vrTwuNav7fIhRwXO4M_Ec7-UPFybkBA11WGUhWjt1qOb7Ft7BeinNzWxmrzNyPBXkfbRD-cE5mfBvm-kh6Xz2R5dHCqv--Djt6mKedw2f3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca48112cfe.mp4?token=qAevsJTDsww3IywZFaJxblJq0b8-wfrM35lLe5cWDMXfj2WNSy6kjNVF5gRGy1mV_P9xdx-z3k4zKDgTRC3giyq95a4aK9kCFvmkT-N8yxjMt3B1qmK8M1VUXIPywnbH63K4UkJuwcvUjW22-ajmeqXDwVlHFe7q0OxVWa8bWwZDTF2rUOXGy4oUm33cVWMsUS6gAamPb43g29zHeAjdJ-tzRm-vEsDqE9Ib0-dEHp4vrTwuNav7fIhRwXO4M_Ec7-UPFybkBA11WGUhWjt1qOb7Ft7BeinNzWxmrzNyPBXkfbRD-cE5mfBvm-kh6Xz2R5dHCqv--Djt6mKedw2f3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله تصاویر اصابت مستقیم پهپاد انتحاری به خودروی نظامیان صهیونیست را منتشر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/435577" target="_blank">📅 17:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435576">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl1_u8cUtDvBDLHI7ew7hvwkx2VV3rBnTKbhO2ZOAu_7Tl2_Fkd_lzRGuSjqtuxEecd-e8Q4oXVXslSaLXhFhbNy6jQoABBwlpeCoGCiiM-rJWnaPNowzuJVkzTy6oPNZutr3JlH5b9xBo8v0uAeflK5mQ1ryuMBnY_CLWQdhYpMZ15C1kMzIQLhaEg4mE8hKAsKJ-x3DSG6I4IPB8WGTiKxTAPqxnCgn245GVBw-Co1RyNETMph_3ixqQq8TmM9Cj2G_MUIgfhrKG5zFg6UI9gOTcPqD2e9ZCMPXRKYn-8beeuzsS2u4HAquTZ_XYFHyZMYyiqf5fmNGo1zYUafnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقچی: ما هیچ مانعی در تنگۀ هرمز ایجاد نکرده‌ایم
🔹
تنگه هرمز اکنون بیش از هر چیز از تجاوز آمریکا و محاصره‌ای که بر آن تحمیل کرده، آسیب می‌بیند.
🔹
از نظر ما، تنگه هرمز برای تمامی کشتی‌های تجاری باز است، اما آن‌ها باید با نیروهای دریایی ما همکاری کنند.
🔹
ما…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/435576" target="_blank">📅 16:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435575">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حزب‌الله: تجمعی از سربازان دشمن صهیونیستی را در شهر رشاف با گلوله‌های توپخانه هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/435575" target="_blank">📅 16:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435574">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVi-eiZ4hv3hNIH4TlrP0sutFTaT-z3uqlwL-_FhSLLX7_RmbKACnHIMs9ldOOvB3IxwQ13I_qdmBo5-FCSSsFWZD6a4JkIWn3CRcUD1J4aSJmdNhxakseEkt1hazNOTLQh9kK--81D-mLRqDwCFKTOhSbA8WScgwsAt05STzB2BWG1XvppA03DC_qCJyzduZVhP669sqlcm9W15jU97xUselILYunPJdLzsrkmR8SKvXr3YhFYOIwQx5EGVLsVUyOngK1TFcxeJv4zefma1Ote7Sd3qZDot8K2APYI0bLmLKQBsns4LP8IhuD8NEogzXSW2YTMZlvqSdokN1RZEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین پرونده کپی‌رایت ایران علیه آپارات
🔹
آپارات پس از ۱۳ سال فعالیت و انتشار بدون مجوز بخشی از محتوای صداوسیما، با پرونده‌ای مواجه شده که رقم خسارت آن به بیش از ۳.۶ همت رسیده؛ پرونده‌ای که از آن به‌عنوان یکی از بزرگ‌ترین دعاوی حقوق مالکیت محتوا در فضای دیجیتال ایران یاد می‌شود.
🔹
برای درک ابعاد ماجرا، اگر یک شبکه تلویزیونی دو سال شبانه‌روز برنامه پخش کند، حدود ۱۷ هزار ساعت محتوا تولید می‌شود؛ رقمی نزدیک به برآورد برخی رسانه‌ها از حجم آثار منتشرشده در آپارات.
🔹
یک منبع حقوقی به فارس گفته اختلاف صداوسیما و آپارات سابقه‌ای چندساله دارد و حتی پیش از ثبت شکایت رسمی در سال ۱۳۹۸ نیز تذکراتی درباره انتشار تولیدات تلویزیونی داده شده بود، اما روند انتشار ادامه یافت.
🔹
طبق رأی دادگاه، پخش بدون مجوز ۷۵۵ قسمت از آثار تلویزیونی در آپارات محرز شده، هرچند برخی گزارش‌ها تعداد کل برنامه‌های منتشرشده را حدود ۱۶ هزار قسمت برآورد کرده‌اند.
🔹
کارشناسان قضایی بخشی از خسارت را بر اساس حجم استفاده از محتوا، اثر آن بر درآمد تبلیغاتی و کاهش ارزش انحصاری برنامه‌ها محاسبه کرده‌اند؛ آن هم در شرایطی که مجموع درآمد سکوهای فعال کشور سال گذشته از محل ترافیک، تبلیغات و اشتراک به حدود ۱۳.۶ همت رسیده است.
🔹
آپارات در بیانیه‌ای اعلام کرده حدود ۶ سال پیش سامانه‌ای مشابه یوتیوب برای مدیریت حقوق محتوا راه‌اندازی کرده و از صداوسیما خواسته بود از این سازوکار استفاده کند، اما این پیشنهاد پذیرفته نشد.
🔹
در مقابل، کارشناسان حقوق رسانه معتقدند همان‌طور که آثار پلتفرم‌هایی مثل فیلیمو یا نتفلیکس بدون مجوز در سکوهای دیگر منتشر نمی‌شود، انتشار آثار صداوسیما نیز مشمول حقوق مالکیت است.
🔹
مطالعات جهانی نیز نشان می‌دهد عدم حمایت از مالکیت معنوی آثار کیفیت آن را کاهش می‌دهد و بهترین راهکار، ترکیب سامانه‌های هوشمند تشخیص محتوا، قرارداد رسمی میان پلتفرم‌ها و صاحبان اثر و تقسیم درآمد تبلیغاتی است؛ مدلی که هم از تولید محتوا حمایت می‌کند هم اختلافات حقوقی را کاهش می‌دهد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/435574" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435573">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4eaa8ed4.mp4?token=oqvtl74UEq3sR0CLVHzBU6gcC3b4SHMsj9gf4sJTK4zK_YNPTYzHYNrPCk78El5wP5Ay5NZ5HCcOb8hZXUDWBFypkycNjb5Kay6DdabFCH-B2-5PJhGMS3tNgtEHhIFpxlbe36rv-O_oZKON4IqbaLhUQT26pFdm6orCwR2M62OfYKxaKyDG_QQEhdCwsJhCacduuOkZhJBLHm8BzhvoWPMXDNL9HyUBm4Nfw9W-lwRv3soyZEbgX5zWCV9yfzZ8XiellWdwSymbK3C0YAwZLzVl4f9op7225aaiQBL254FJEeVbqLwehDFAroXpHaVwmlK9UKHRl-0FzoDjYjxrlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4eaa8ed4.mp4?token=oqvtl74UEq3sR0CLVHzBU6gcC3b4SHMsj9gf4sJTK4zK_YNPTYzHYNrPCk78El5wP5Ay5NZ5HCcOb8hZXUDWBFypkycNjb5Kay6DdabFCH-B2-5PJhGMS3tNgtEHhIFpxlbe36rv-O_oZKON4IqbaLhUQT26pFdm6orCwR2M62OfYKxaKyDG_QQEhdCwsJhCacduuOkZhJBLHm8BzhvoWPMXDNL9HyUBm4Nfw9W-lwRv3soyZEbgX5zWCV9yfzZ8XiellWdwSymbK3C0YAwZLzVl4f9op7225aaiQBL254FJEeVbqLwehDFAroXpHaVwmlK9UKHRl-0FzoDjYjxrlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستاده برای ایران…
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/435573" target="_blank">📅 14:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435572">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2a56d1d6.mp4?token=l697QViGp5cQh1YMs0DhcFpKmtNxaREVMEzAbof60HG1F2pDi6eBvboT9A6O0qnQovDfeRzEOFBkTdtEBZpzmO3g7SlRFIO2gWXGgRQJE_fe63ITEnGlUp8PpwZOdk4Fn-Xrup_6SH3Ai4UOsjeUvYD6JmV61cnBfr45bm9Zfgg6sE8TsaCBoSOs6V1HuCZqv2E36PZmor-8qZH0YwZlIgmP_zJFAxKlck5gDMk1XMhFejzr5NARuYdijSmy-EZDBDbzCNJXmoN3FEeKJXzJdFtB4XiL85cdFdJPUAJOXXI3ij5yVSNiY4cO-inexhmIaL1nYcDsWMJm9aBNSBePdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2a56d1d6.mp4?token=l697QViGp5cQh1YMs0DhcFpKmtNxaREVMEzAbof60HG1F2pDi6eBvboT9A6O0qnQovDfeRzEOFBkTdtEBZpzmO3g7SlRFIO2gWXGgRQJE_fe63ITEnGlUp8PpwZOdk4Fn-Xrup_6SH3Ai4UOsjeUvYD6JmV61cnBfr45bm9Zfgg6sE8TsaCBoSOs6V1HuCZqv2E36PZmor-8qZH0YwZlIgmP_zJFAxKlck5gDMk1XMhFejzr5NARuYdijSmy-EZDBDbzCNJXmoN3FEeKJXzJdFtB4XiL85cdFdJPUAJOXXI3ij5yVSNiY4cO-inexhmIaL1nYcDsWMJm9aBNSBePdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عارف: به هیچ قیمتی تنگۀ هرمز را از دست نخواهیم داد
🔹
اصلا تنگۀ هرمز مال ماست؛ ملک ما بوده حالا مدتی از ملکمان خوب استفاده نمی‌کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/435572" target="_blank">📅 14:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435571">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6fb1016c.mp4?token=vjX3yUnMrYIxuOw8tzXIWUZTFa2kSsoY7BanLpU_NlxfqbPI0Uw9YNXsysTyJoT0ux1W0Ok-cwDvUrS_IeF4BtgbU4bt2tv8M6dBa_orEgzJOXPvOfHp0ZjC0mwzss3t3mCqBZkQFTCZu0DdBDmJWQU2uIXBaUB_revQJWZG-9gi3RPlCaWo_SEG1Y2k3RqrzJII2T_lnH_rcKaRlLEP5YnlQI2RVH_pNJGVIk_4jg8FdXASnx1mECfSMnPRsqjpOJOf24IzBOoey02ncTu-UysQDx86Y5hew6AOvrPyf5ocmtdPSkr3GOibQMw3J2TbOAOWgob4zfOv238DD48lWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6fb1016c.mp4?token=vjX3yUnMrYIxuOw8tzXIWUZTFa2kSsoY7BanLpU_NlxfqbPI0Uw9YNXsysTyJoT0ux1W0Ok-cwDvUrS_IeF4BtgbU4bt2tv8M6dBa_orEgzJOXPvOfHp0ZjC0mwzss3t3mCqBZkQFTCZu0DdBDmJWQU2uIXBaUB_revQJWZG-9gi3RPlCaWo_SEG1Y2k3RqrzJII2T_lnH_rcKaRlLEP5YnlQI2RVH_pNJGVIk_4jg8FdXASnx1mECfSMnPRsqjpOJOf24IzBOoey02ncTu-UysQDx86Y5hew6AOvrPyf5ocmtdPSkr3GOibQMw3J2TbOAOWgob4zfOv238DD48lWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران، ترامپ را کت بسته به چین فرستاد
🔹
تصور کنید کاخ سفید، در میانه جنگی اقتصادی که به چین باخته، تنها برگ برنده‌اش را مشت آهنین ارتش می‌داند. آن‌ها می‌خواستند با حمله به ایران پیش از سفر ترامپ به پکن، یک پرونده بزرگ را با اتکا به ارتشی که ترامپ آن را افسانه‌ای…</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/435571" target="_blank">📅 14:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435570">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edbd824a7a.mp4?token=MrVe-b21ZUaXu9iL5UPBTvFbP7-xQtse25NClT1uyhecHePgBpFmiZro44xt702GrT8mTjp_ysoIh5OWMicmAikOBacG-kiHubDWPxvYP8uuJeGUWkHCfSlsXbxWaZuCffoOR9OvOUydPaBF2aZ4Tk5oFC9NlmD1YfFdhsT31IN3lOlD0RPx5e9Jm9D7k7-SQpdeXmzFVwFQ3YR2nsMJ9gzIPQjB5oZnm1gnwMEac35bkMHmaZgCJy1hCULwfRWsEKQcm_GOLmkrwLgvAe5v72hmFCO9aHszb9LhFEq4h8pXBM9BHFgIMxmvtkTv6eg6dUIkyVMTO8gUVzTpG6TJozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edbd824a7a.mp4?token=MrVe-b21ZUaXu9iL5UPBTvFbP7-xQtse25NClT1uyhecHePgBpFmiZro44xt702GrT8mTjp_ysoIh5OWMicmAikOBacG-kiHubDWPxvYP8uuJeGUWkHCfSlsXbxWaZuCffoOR9OvOUydPaBF2aZ4Tk5oFC9NlmD1YfFdhsT31IN3lOlD0RPx5e9Jm9D7k7-SQpdeXmzFVwFQ3YR2nsMJ9gzIPQjB5oZnm1gnwMEac35bkMHmaZgCJy1hCULwfRWsEKQcm_GOLmkrwLgvAe5v72hmFCO9aHszb9LhFEq4h8pXBM9BHFgIMxmvtkTv6eg6dUIkyVMTO8gUVzTpG6TJozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی خطاب به امارات: ائتلاف با اسرائیل هم از شما محافظت نکرد
🔹
وزیر امور خارجه امروز در نشست وزرای خارجه بریکس در دهلی‌نو در پاسخ به ادعاهای بی‌اساس نماینده امارات گفت: ائتلاف شما با اسرائیلی‌ها نیز از شما محافظت نکرد و در سیاست خود در قبال ایران بازنگری…</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/435570" target="_blank">📅 14:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435569">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d695d1f5.mp4?token=QLtDMeUcEU00HpHie397WWhvEJMla3-nHa_NxZYqR5yw751s7p9M0hrCroyCF6FuaUzUGYnQdO14XWnyoIarhPUQlLMJC-PE7LqQzWu2KKFemdA8BOhOA5BnzPQ8P2GBuRpF8H2_xTsOJ_oPs2-gSkM5hlNpODFoAMqzdv6xlrTKUD9GUaj496PIko7N8jQMYyPwG1Ib_g9rh3JKDAuxCDMnb67amsOcZAUvb-SAOSwNdtsW-X0SGnARqIDNDJjvTKp6fcBouiNfcsRzPNawzpy9DEUIycXBwa9-ygSvG5kyf6JvNMQ4Flnr_vrt5MQGjDZanVBwVq3wKR_Han8Bbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d695d1f5.mp4?token=QLtDMeUcEU00HpHie397WWhvEJMla3-nHa_NxZYqR5yw751s7p9M0hrCroyCF6FuaUzUGYnQdO14XWnyoIarhPUQlLMJC-PE7LqQzWu2KKFemdA8BOhOA5BnzPQ8P2GBuRpF8H2_xTsOJ_oPs2-gSkM5hlNpODFoAMqzdv6xlrTKUD9GUaj496PIko7N8jQMYyPwG1Ib_g9rh3JKDAuxCDMnb67amsOcZAUvb-SAOSwNdtsW-X0SGnARqIDNDJjvTKp6fcBouiNfcsRzPNawzpy9DEUIycXBwa9-ygSvG5kyf6JvNMQ4Flnr_vrt5MQGjDZanVBwVq3wKR_Han8Bbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آغاز عبور کشتی‌های چینی از تنگۀ هرمز از شب گذشته
🔹
به گزارش یک منبع آگاه، با تصمیم جمهوری اسلامی، امکان عبور تعدادی از کشتی‌های چینی از تنگه هرمز با رعایت پروتکل مدیریت ایرانی تنگه میسر شد.
🔹
بر پایه گفته‌های این منبع آگاه، پس از پیگیری‌های وزیر خارجۀ چین…</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/435569" target="_blank">📅 14:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435568">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabdb4251f.mp4?token=lVw1_DXbOmzQeSCu2rkIOgkROYIZFHGQ6w3vv2nkEzbFhbRhTj-6sGeYTdo4JTl7NFexkeNT3zQHQ7Jdz08d80FK75kEKFkrZ1qu05tgdD3iWhNbwY2wUq-8cL2sdGOtARObZXhe82hZVF9aiNDb75SyOF7AvpSYASGXkaBV04s-TfhUJhlPBNkLWzTlfLhMGqisuAqGD-cFOGwxFUsg9I0ZrTmfBKS3IyrKtAJ2PqPGDrP7AYPR1QcIniFrXPF-3bGh-2XCgoXA6I8dwYs3uNjwYCoEKnfZT9x2F0fVyPgVBpKKCz-fkP7iWySXl24vbQhpyNoJX_Dz4ok8JBb-7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabdb4251f.mp4?token=lVw1_DXbOmzQeSCu2rkIOgkROYIZFHGQ6w3vv2nkEzbFhbRhTj-6sGeYTdo4JTl7NFexkeNT3zQHQ7Jdz08d80FK75kEKFkrZ1qu05tgdD3iWhNbwY2wUq-8cL2sdGOtARObZXhe82hZVF9aiNDb75SyOF7AvpSYASGXkaBV04s-TfhUJhlPBNkLWzTlfLhMGqisuAqGD-cFOGwxFUsg9I0ZrTmfBKS3IyrKtAJ2PqPGDrP7AYPR1QcIniFrXPF-3bGh-2XCgoXA6I8dwYs3uNjwYCoEKnfZT9x2F0fVyPgVBpKKCz-fkP7iWySXl24vbQhpyNoJX_Dz4ok8JBb-7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خسوف اقتصادی برای دنیا با بسته شدن تنگۀ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/435568" target="_blank">📅 14:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435567">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">ایران، ترامپ را کت بسته به چین فرستاد
🔹
تصور کنید کاخ سفید، در میانه جنگی اقتصادی که به چین باخته، تنها برگ برنده‌اش را مشت آهنین ارتش می‌داند. آن‌ها می‌خواستند با حمله به ایران پیش از سفر ترامپ به پکن، یک پرونده بزرگ را با اتکا به ارتشی که ترامپ آن را افسانه‌ای توصیف کرده، ببندند و با توپ پر به چین سفر کنند.
🔹
حالا بیش از هفتاد روز از حمله‌ای که قرار بود نمایش قدرت باشد گذشته و آمریکایی که می‌خواست ۴ روزه پرونده ایران را ببندد، پشت در مذاکره التماس می‌کند که غنی‌سازی اورانیوم ایران کمی محدود شود.
🔹
رئیس‌جمهور آمریکا در میانه جنگ با ایران یک‌بار سفر خود را به امید پیروزی و سفر با دست پر به تعویق انداخت اما حالا با دستی تهی و موقعیتی شکننده‌تر از پیش از نبرد با ایران، راهی چین می‌شود؛ تحولی که بلافاصله خود را در زبان تهدید پکن بر سر تایوان نشان داد.
🔹
وقتی چینی‌ها آشکارا آمریکا را به جنگ تهدید می‌کنند، در واقع پیامی ژئواستراتژیک صادر می‌کنند؛ توان نظامی واشنگتن که تا پیش از ماجراجویی در ایران یگانه عنصر قدرتش در رقابت با ما بود، اکنون می‌تواند به نقطه ضعفی آشکار بدل شده باشد.
🔹
ترامپ در مواجهه با تهدید پکن تنها به رهبر چین می‌گوید که «چین زیباست و شما یک رهبر بزرگ هستید». همان ترامپی که تا چند ماه قبل آشکار پکن را تهدید نظامی می‌کرد. مقاومت ایران دیگر فقط یک مسئله محدود به غرب آسیا نیست؛ به پازل بزرگ‌تری گره‌خورده که در آن مهار آمریکا، از تنگه هرمز تا تنگه مالاکا امتداد دارد.
🔹
کارشناسان می‌گویند، چینی‌ها از ارزش مقاومت ایران آگاه هستند و اتفاقاً بعد از ۹ اسفند زمینه شراکت راهبردی بی‌سابقه بین ایران و چین را رقم خواهد زد.
@farseconomy
-
Link</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/435567" target="_blank">📅 14:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435566">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c9ce715d.mp4?token=Y2H6Yu6SDT5sWygNomi71txFlY7fY1Syig9acPP5dAAGaXMcwLOPaJir31DrpED0194Z7Qg5GyXshNVskF0XxLIcXk0uPaH-TbhmdfbfAIbvWqm9IzHCsbcCiAIOtSbtcn3xvGs9JsFqTiTZCRicWJFaXDwHGjzTNyGwjA1EwaY-VMlNtNkPsjerCmpZ1u7m7PJt-rorb6oiFShVLSW8jVW9It1mfoCdMaLaNcsk9qnLVRtxHiRoMvL1wTe0bc-QNLdSejBL7J7tWz9sb7u9T-e7xMa5r8CSJuZzvaT-Mum5KDI-Vs5_Hv6mNQ85aRoyRKSRBOjr2nWMkHJ-D_E7Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c9ce715d.mp4?token=Y2H6Yu6SDT5sWygNomi71txFlY7fY1Syig9acPP5dAAGaXMcwLOPaJir31DrpED0194Z7Qg5GyXshNVskF0XxLIcXk0uPaH-TbhmdfbfAIbvWqm9IzHCsbcCiAIOtSbtcn3xvGs9JsFqTiTZCRicWJFaXDwHGjzTNyGwjA1EwaY-VMlNtNkPsjerCmpZ1u7m7PJt-rorb6oiFShVLSW8jVW9It1mfoCdMaLaNcsk9qnLVRtxHiRoMvL1wTe0bc-QNLdSejBL7J7tWz9sb7u9T-e7xMa5r8CSJuZzvaT-Mum5KDI-Vs5_Hv6mNQ85aRoyRKSRBOjr2nWMkHJ-D_E7Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس کمیسیون جوانی جمعیت مجلس: وام ازدواج بعد از قانون جوانی جمعیت ۱۰ برابر شد
🔹
بانکی‌پور: صف وام ازدواج و فرزندآوری امسال
صفر
می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/435566" target="_blank">📅 14:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435565">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRwS-_QICb32PyIELAC3ZTtcZOcAJBAjNx11dJip-XHAagfPvG7FY6Thd2trAsUYdgNz08nNPOkW-pIS6psqE-UxTdJdEl05O5h1xuMdqqjna9GhreUcu5zlpimS-rSexNA1cjvxHNIVc_sBZXIGTFM94mk8wX78FdhD7PbPuqXOu9jJFvtO13azFfNrdLqoN4atgFsKZAMTVEjftoOUH8ytQcxNX92aqiM-wEhC8tGpdSsqE1TH_TBQ0IyN8GV2itlcAATBgDGbVMFgFCSF5WDApypaJz-V9SsXfRs04sxBBJeY6TFe1vJlMyB0LjbfT5vbJZst0ROt2TeINSuU9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وایرال شدن تصاویری از فیلم‌برداری ایلان ماسک در سفر چین و جذابیت دکور سقف «تالار بزرگ خلق» برای مارکو روبیو  @FarsNewsInt</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/435565" target="_blank">📅 13:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435564">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
آغاز عبور کشتی‌های چینی از تنگۀ هرمز از شب گذشته
🔹
به گزارش یک منبع آگاه، با تصمیم جمهوری اسلامی، امکان عبور تعدادی از کشتی‌های چینی از تنگه هرمز با رعایت پروتکل مدیریت ایرانی تنگه میسر شد.
🔹
بر پایه گفته‌های این منبع آگاه، پس از پیگیری‌های وزیر خارجۀ چین و سفیر این کشور در ایران، تسهیل در عبور و مرور کشتی‌های چینی بر مبنای روابط عمیق دو کشور و شراکت راهبردی دنبال و در نهایت جمع‌بندی شد که تعدادی کشتی چینی مورد درخواست این کشور پس از تفاهم درباره پروتکل‌های مدیریت ایرانی تنگه از این منطقه عبور کنند که این عبور از شب گذشته آغاز شده است.
🔹
کارشناسان معتقدند این اقدام که مبتنی‌بر پروتکل‌های داخلی ایران است، هرگونه بهره‌برداری سیاسی از ظرفیت تنگه برای اعمال فشار خارجی را خنثی کرده و جایگاه مدیریت هوشمندانه تهران بر این مسیر حیاتی را تقویت می‌نماید.
@Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/435564" target="_blank">📅 13:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435563">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz_JpqUBaejXfc2KEpXghcZFxyEDf_2d2SNQcLfMeORuYhxCW48tX--JG4fYXG-Q_DXf8jkQtF3mGL4J8gP99EHQr72GbPF87K8wvHJz26CBBruAb76i-HAN9dXpumL_v6Wrj9D2UNLYIyMwBEbc0ZHL7C_70xLrSm8PYlUwkWyzcPrcrCQlxFx1Wa9zEIrpEcw4EpTpn5LsGni62rfMK17-SwxAKV3ADtVwhjPR_oJygDu0XjjU8cBHHW7YrxPN58X4c1y4st_Sms9GLfAY_S45XBIqEt3bSoibJ2DPd3lP5K3SihmuQOaUV2ykYBsdZarXOhYOYrUJFnrXz2ycKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقری: هدف آمریکا از حمله به ایران، ضربه به هم‌گرایی آسیا بود
🔹
معاون دبیر شورای‌عالی امنیت ملی در نشست دبیران شورای امنیت ملی کشورهای عضو شانگهای: شخصیتی که امروز می‌بایست در چنین جایگاهی از طرف ایران قرار می‌گرفت و به گفت‌وگو می‌پرداخت برادرم آقای علی لاریجانی بود که ترور شدند.
🔹
در طول چهل روز تجاوز بی‌وقفه، شاهد ارتکاب جنایات وحشیانه‌ای از جمله ترور مقامات نظامی و کشوری، حمله به تاسیسات هسته‌ای صلح‌آمیز، زیرساخت‌های صنعتی، آموزشی و بهداشتی بودیم.
🔹
دقیقا هدف آن جنگ ضربه به همین هم‌گرایی آسیایی بود. جنگ با ایران آغاز حمله به جنوب جهانی است. این جنگ برای توسعه‌طلبی و اصالتا امپریالیستی است تا با ایجاد حوزه نفوذ و تسلط مطلق بر منابع انرژی خلیج فارس مانع از رشد آسیا و ظهور قدرت‌های میانی شود.
🔹
لذا این جنگ اگرچه با ایران شروع شد اما محدود به ایران نیست و در صورت انفعال و بی‌عملی در برابر آن، تسری و گسترش می‌یابد. هرگونه پاسخ ضعیف، دعوت به جنگ بیشتر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/435563" target="_blank">📅 13:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435562">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpNtm8Ooe2-nZgTOFCQjwG_u9dPXLvQ6jAt-PaH8DFrlBVa6C30Yq67_Kd2H2YnddAVduLf0AZ29sikUwghuZRKFnPUawFy3N80SPJa9rUYdfJzwLa9XMykb1-sFORCD9kfQtb_pyyBaasfmP2f8JihmnOFdYXkwSH-5aiFuQK8uwuNemGaX0IZVFo5zothoxdu-0LiWuYs_JtebrVpffV-UhNuZ9XOd0lA9X8J11ULpB7FAIo-TglFq875W_cETGqo4hakQtzCo5_9YgAytlWI5DGIqpBwZPNPuiL_3KukMbHOKCT3oWJSfuNbI0NvcRnovwuVuLHKLQ6g9nl0FAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی خطاب به امارات: ائتلاف با اسرائیل هم از شما محافظت نکرد
🔹
وزیر امور خارجه امروز در نشست وزرای خارجه بریکس در دهلی‌نو در پاسخ به ادعاهای بی‌اساس نماینده امارات گفت: ائتلاف شما با اسرائیلی‌ها نیز از شما محافظت نکرد و در سیاست خود در قبال ایران بازنگری کنید.
🔹
سیدعباس عراقچی افزود: من در سخنرانی‌ خود نام امارات متحده عربی را ذکر نکردم، به خاطر حفظ وحدت و ترجیح دادم به آن اشاره نکنم. اما در واقع باید بگویم که امارات مستقیماً در اقدام تجاوزکارانه علیه کشور من دخیل بود. زمانی که این تجاوز آغاز شد، آنها حتی از محکوم کردن آن خودداری کردند.
🔹
وی ادامه داد: آنها اجازه دادند از سرزمین‌شان برای شلیک توپخانه و تجهیزات علیه ما استفاده شود. همین دیروز فاش شد که نتانیاهو در زمان جنگ به امارات و ابوظبی سفر کرده بود. همچنین آشکار شد که آنها در این حملات مشارکت داشته‌اند و شاید حتی مستقیماً علیه ما اقدام کرده باشند. بنابراین امارات شریک فعال این تجاوز است و هیچ تردیدی در این باره وجود ندارد..
🔗
شرح کامل سخنان عراقچی را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/435562" target="_blank">📅 13:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHCCGYltsq01WGwldLAqNR-jTWl2MuMGOwl_n7MV0MYAAldtHubc7XVTuaVtoPTCOxqXuf9VdAWt2bZESdwiF8iYqlAYRt_070-bvaHEnd5GsC8OUxwZbW6dNepbwSBOqJviikZnndSCWfqMb1M9pPsd_9AJzH84YzMTP-Zq5WoFBau9UiidgDJe-jrfIWqoaGNfga_yBsO6s2IRDhhOkNAA1H-q9Bcav-SyyE9IafTIqjGT2X5NPz58sIyrDBqV2vDzdQZ3UxJBQBpXp57lEf19VyqXFe31a9kp6B8QjpJQyoBn8JbewKNs420qKOWfAbgbRIgURel4fRX-qG1kGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بازدید رئیس‌جمهور از آثار حملات و خسارات وارده به مجموعۀ ۱۲ هزار نفری آزادی  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/435560" target="_blank">📅 12:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
حزب‌الله: یک نیروی اسرائیلی را در داخل خانه‌ای در شهرک «دیر سریان» در جنوب لبنان با موشک و توپخانه هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/435559" target="_blank">📅 12:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یارانه اردیبهشت دهک‌های یک تا ۳ واریز شد
🔹
سازمان هدفمندسازی یارانه‌ها: یارانۀ مرحلۀ ۱۸۳ مربوط به اردیبهشت به‌حساب ۱۰ میلیون ۲۳۰ هزار و ۶۸۱ سرپرست خانوار دهک‌های اول تا سوم در سراسر کشور واریز شد و قابل برداشت است.
🔹
براساس دهک‌بندی اعلام شده از سوی وزارت رفاه ۲۷ میلیون و ۹۱۷ هزار و ۲۶۹ نفر در دهک‌های اول تا سوم قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/435558" target="_blank">📅 12:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
یدیعوت آحارونوت: درپی اصابت پهپاد حزب‌الله به محل استقرار خودروها در «راس الناقوره»، ۳ نفر مجروح شدند که حال ۲ نفر از آن‌ها وخیم گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/435557" target="_blank">📅 12:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435556">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">واکنش سخنگوی قوه‌قضائیه به دزدی دریایی آمریکا؛ توقیف کشتی‌های متخلف آمریکایی با حکم دادگاه صالحه و مستند به قوانین داخلی و بین‌المللی است
🔹
سخنگوی قوه قضاییه با انتشار متنی در فضای مجازی به روند توقیف حقوقی و قضایی نفت‌کش‌های متخلف آمریکایی در آب‌های ساحلی متعلق به کشورمان پرداخت و به راهزنی‌های دریایی ارتش تروریستی آمریکا و زیر پا نهادن همه قواعد حقوقی بین‌المللی در این دزدی ها اشاره کرد.
🔹
توقیف نفت‌کش‌های متخلف آمریکایی، امری مستند به قوانین داخلی و بین‌المللی است. توقیف این نفت‌کش‌های متخلف ناظر بر آرای متقن و قطعی محاکم صالحه ایران است که پس از طی فرآیندهای قانونی صادر می‌شوند.
🔹
ایضاً مراتب قانونی و مستندات تخلفات حادث‌شده از ناحیه نفت‌کش‌های مزبور نیز برای طرف آمریکایی ارسال می‌شود؛ علاوه بر این‌ها، براساس کنوانسیون حقوق دریاها ۱۹۸۲، کشور ساحلی می‌تواند کشتی‌های کشور دیگر را به سبب تخلف از قوانین و مقررات داخلی و بین‌المللی در قلمروهای دریایی خود و یا دریای آزاد توقیف کند.
🔹
اقدامات قانونی ایران در توقیف نفت‌کش‌های متخلف آمریکایی، برابر و همسنگ با رفتارهای خصمانه و چپاول‌گرایانه آمریکا در دزدی دریایی علیه کشتی‌های کشورمان نیست؛ رئیس‌جمهور آمریکا صریحاً به دزدی دریایی اعتراف و حتی مباهات کرده است.
🔹
رژیم واشنگتن همه حقوق و قواعد جهان‌شمول را به سخره گرفته است. ادامه سکوت سازمان ملل در قبال یاغی‌گری‌ها و طغیان‌های آمریکا، این سازمان را از معنا تهی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/435556" target="_blank">📅 12:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435553">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvrENRvAKrP5zTsWnlT1ePM53wCeAwERL_aMpXPXKjCZm_EJ4EsmNEhQ4h7QFB5xuo6Fme-9KQKb9Ou1fDvt9xzhr27-BabazKyWXJ_ELxMLFCFmQkjsFym686GBqaCeCjn3TIUCUuWJBjxgUwZBrrqfXrcflkzBJjwQT3fbyzzoSEg5Bo8jkNXuJHHpdoanxveihHuD0ExKLcemdHafc1V_giMvgjBCCGbPw4p0wMdp5DwXx07cKkcjKdOvGkseBQ4_7Yw9VGy_FPHFiEZ5MeKBxMxPp98Aa35SOhP95nSLcx_MFvfjDtVxi-2dWWXDAEZN0BvacE2dQVzr8FVV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxoAWWIHP1AFPJTTQzBPrEPuaOOFa-J5EkVP9EpifGQD-hXV_UWzkaNCq0pnT1J67v7E7zeSp1pL1hSayFT4R8xqpBcMwfCV8Kpf-zdDTEh9IFZodFpk01sUgFhVyN0u70gPaVzhVc7-uCveBNtnwbI6LxzKIS8A5_MK3enFEdp-QMigM-O7oluEhygrjYRHtMVu5SyKj6BjdfpoaWyI-JYgvbegN9DK4B4EUiV2XSgad3UTEexaKXJHe-3LHbKimG2rqL9nAyG2c70I2cH8qrAGCQmOFF0UQXTi9sUs7Z94lK-S1jpqzTrnF9fXwKYN0cpmV422vlmpG8cRWoMytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6hrCsEpdadiIxFg43V7UcSosyjnp-kvsizLSyii-saZ0exD8M5uOCrM-aTmucatJrCchekgIbZsVpll9Cpzsm--J7t_fGu7PfYJcsaOAah5Jl8LROs3u5B1oA2d8sdKgVUDuz0bZaMhijR-RM_w_qxXPiSjkNeyUsWbWt6XaTGc1CQrL330w7I_Sp3RPAIsBaOoQUAb0P-d09RvnyhdtlOGNtZwOL46U4O158Xnv5OCb-Q-kPtuJjax-WtLKXMlbS6JPjEbTSaTfw7I9o4f0t56wpF5I59L47bMZL9TXmeOM3ZjQGtcPgd3t1rPPXrLGZi-GGh0Yjjm6w4dSGG5MQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حملۀ موشکی آمریکا و اسرائیل به ورزشگاه آزادی
🔹
در حملۀ موشکی صبح امروز آمریکا و اسرائیل به سالن ۱۲ هزار نفری ورزشگاه آزادی تهران، کلیۀ بخش‌های سالن و ساختمان‌های اطراف آن تخریب شدند.
🔹
آمریکا و اسرائیل در روزهای اخیر بارها به مناطق مسکونی، ورزشی، بیمارستانی…</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/435553" target="_blank">📅 12:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435552">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03b2c65df.mp4?token=uVNa6e6klP_D7_xW3zK9N9K7CPcmndd2NA7_X_Is4WfOPb3NE6h9w8f1mx8-1kcKYC3JqQf908VPFBoXaPVx4H7aOi5XYl6Ar-2H53ONWVom31Gc0p3G2zF0WcqzdqL_QKKbPPD-nlvo27UMbCgq-niTQW8-wDh_lw0lmw7eRB9EqlQZ9gTZRf51Z4CmlPzEe43wfFmjch4lC3hZ46Q-bRNLunjz-Ga2ILb9CZXqpjFA34VNQq8p5UQHLwX0-ZGOrBF0ytnSpRgndLs4CYTuz4GANFKZb6PAjs8KajdaiqVg6W8TC66T82HXI9SQuGmahbvt1JOVMpCTBWwgpbfwY7O-FmlvWJrpj5gnQd6QWRdaR3IpEN_hdEN8lbC5mu5Coo5mSgA6TTabc7yRmoT11EhyDOT0en6oZz8QtdBH9RvUEnEwFf8qjX6syC92ne6D80F2bubXS-7JNt8HhFBd2EuemsmvD2WWBWJMQYwYwTEfwi7Gr6zcmfe-awmGvVNTsSICmsQvHj6qi8Hnjs2jHR87lUzdeRAW5AgmJY-9sTER0y_-SndxJj9MxANIksZqnCVBsIYX-cETZpYZaKoIAVF6umBJAsiFFZnZNHrLL5cE3soisEpiy9Ep2AEtVBpNbBt3BKefuP6RIUwUMGk5Hj9vOGjFDQ-C5UTdrHuQjNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03b2c65df.mp4?token=uVNa6e6klP_D7_xW3zK9N9K7CPcmndd2NA7_X_Is4WfOPb3NE6h9w8f1mx8-1kcKYC3JqQf908VPFBoXaPVx4H7aOi5XYl6Ar-2H53ONWVom31Gc0p3G2zF0WcqzdqL_QKKbPPD-nlvo27UMbCgq-niTQW8-wDh_lw0lmw7eRB9EqlQZ9gTZRf51Z4CmlPzEe43wfFmjch4lC3hZ46Q-bRNLunjz-Ga2ILb9CZXqpjFA34VNQq8p5UQHLwX0-ZGOrBF0ytnSpRgndLs4CYTuz4GANFKZb6PAjs8KajdaiqVg6W8TC66T82HXI9SQuGmahbvt1JOVMpCTBWwgpbfwY7O-FmlvWJrpj5gnQd6QWRdaR3IpEN_hdEN8lbC5mu5Coo5mSgA6TTabc7yRmoT11EhyDOT0en6oZz8QtdBH9RvUEnEwFf8qjX6syC92ne6D80F2bubXS-7JNt8HhFBd2EuemsmvD2WWBWJMQYwYwTEfwi7Gr6zcmfe-awmGvVNTsSICmsQvHj6qi8Hnjs2jHR87lUzdeRAW5AgmJY-9sTER0y_-SndxJj9MxANIksZqnCVBsIYX-cETZpYZaKoIAVF6umBJAsiFFZnZNHrLL5cE3soisEpiy9Ep2AEtVBpNbBt3BKefuP6RIUwUMGk5Hj9vOGjFDQ-C5UTdrHuQjNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منوچهر متکی خطاب به نماینده بحرین: شما در جنگ تجاوزکارانه آمریکا شریک هستید  رئیس شورای اجرایی اتحادیه بین‌المجالس مجلس: سخنان بی‌ادبانه نماینده بحرین به‌گونه‌ای بود که گویی عامل آمریکا، ایجنت آمریکا و اسرائیل سخن می‌گوید.  شهر کوچک بحرین، ۳ میلیون متر مربع…</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/435552" target="_blank">📅 11:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435551">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
دقایقی پیش زمین‌لرزه‌ای ۵ ریشتری در عمق ۸ کیلومتری بردسیر کرمان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/435551" target="_blank">📅 11:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435549">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5938e459bf.mp4?token=fQli62oBZl2xqH_1hZXAfaHfv7Savte6iizENBC8vEM-5kq3q2JpGaVR71DICIaM6FdM5JYeU0FykZRlDLKjmsa_JU1ZNW9KwOkThoP1iscv1sFKPkGJMkgvvlPISazSZcRpXZzuejVavPtBnwAEBX0wRf-zZCeJjzgaRQE7nJp3ZbA7EtoSZd8pFqipoWtG0td3ugjQhjhx5INVZI4JtDJVcNMViv1yI1cHdLpVw0auSaEKUStRmSAEiBNsBQXvt5aIhK6Yxxaehs0O5o4gO2vPAGOMoCGd6YNQzgbfg8Cf1-nLD-FSz-uHfWS1vnpY-X7E9spsPLH83f3m92ajyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5938e459bf.mp4?token=fQli62oBZl2xqH_1hZXAfaHfv7Savte6iizENBC8vEM-5kq3q2JpGaVR71DICIaM6FdM5JYeU0FykZRlDLKjmsa_JU1ZNW9KwOkThoP1iscv1sFKPkGJMkgvvlPISazSZcRpXZzuejVavPtBnwAEBX0wRf-zZCeJjzgaRQE7nJp3ZbA7EtoSZd8pFqipoWtG0td3ugjQhjhx5INVZI4JtDJVcNMViv1yI1cHdLpVw0auSaEKUStRmSAEiBNsBQXvt5aIhK6Yxxaehs0O5o4gO2vPAGOMoCGd6YNQzgbfg8Cf1-nLD-FSz-uHfWS1vnpY-X7E9spsPLH83f3m92ajyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وایرال شدن تصاویری از فیلم‌برداری ایلان ماسک در سفر چین و جذابیت دکور سقف «تالار بزرگ خلق» برای مارکو روبیو
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/435549" target="_blank">📅 11:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435548">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U21WyXKCaFIi4as67h6jbWN75D5FnTWg0S-WDPFKlBybZkHbd2hUFc6ifMwGTZww5SJlzXJWnio6dw-h1fprTDmJCxsG9iO5S1dWGNbjPaIHIadFEfNUGy9pZAdL8hxeVs8YMFOxZYNOodu5zO4LZv5D1txE7lnhm7YbL33rWsIpUPz5LRDWFwCusHUin-b7UdXW_gs6U0xooxWZjFjn_22Uf_PtZ0zXIzaBtFQaKQg8DZar2oR9kIudsUsjbV_e16uh53GOYzccP4kQqY6bdksEzQzBYc_nHr3DSZgdHhsbuzed2PK1Udgn4eml-lKaZ-7ynzErH36OKuRGoPoBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وقوع یک حادثه دریایی در نزدیکی فجیره امارات
🔹
منابع رسانه‌ی از وقوع یک حادثه دریایی و وقوع انفجار در پی حمله پهپادی به یک کشتی در سواحل فجیره امارات خبر دادند اما چیزی نگذشت که مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی درباره یک حادثه در ۳۸ مایل دریایی شمال‌شرقی فجیره دریافت کرده است.
🔹
این سازمان ادعا کرد که این کشتی هنگامی که در حال پهلو گرفتن در الفجیره بود، مورد تصرف قرار گرفت و هم اکنون در حال حرکت به سمت آب‌های منطقه‌ای ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/435548" target="_blank">📅 11:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435547">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTHypT4K10Hnj5GdX43pJcDFRC1bUkkAISHCUJnKd_oJgrcaOLqKeQVu9GWBblsRff5uFbHdEn-7lAb3czNU_p_JHwQa_D6UeLqFhxxZcqC5Z7kjvwnSNSdDqg9a0FAa7IuPlPSNyVCwj9erkgHyLCm3hq26ZpPRxi3bYJH1KxNcRu01mMnp7ErER1EOv-wO2rDurkBhKn9z88U5hL1NnJh52_kbboFVR3a4usQB58KOmaoKQqgC8N5-qae4Zsk-psDxwsC2j4hGSxH9YmndocrGYXrfHExHV0CZFRGw8J2xvWtHkSM_7BXSmT7zDDLf7BXM0HY3pjCjTAmMCayXnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارو ۳ برابر شده اما پوشش بیمه هیچ!
🔹
یه عمری پول بیمه دادیم تا سر پیری عصای دستمون بشه نه نمک روی زخم» این را پیرمرد بازنشسته‌ای می‌گوید که برای خرید پلاویکس، انسولین و داروهای فشارخون نزدیک به ۵ میلیون تومان پرداخت کرده؛ زیرا داروخانه با بیمه تأمین اجتماعی قرارداد ندارد و او نیز مجبور است که دارویش را از همین داروخانه تهیه کند؛ پلاویکس خارجی هم در همۀ داروخانه‌های سطح شهر پیدا نمی‌شود.
🔹
براساس تحقیقات میدانی خبرنگار فارس، در حال حاضر تعدادی از داروخانه‌ها و مراکز درمانی اقدام به قطع همکاری با شرکت‌های بیمه‌های درمانی کردند و خدمات و اجناس‌شان را به صورت آزاد به بیمار می‌فروشند.
🔹
تعداد دیگری از داروخانه‌ها نیز با بیمه همکاری می‌کنند اما دیگر داروهایی که درصد پوشش‌دهی بیمه‌اش زیاد است را از شرکت خریداری نمی‌کنند؛ انسولین و اسپری‌های تنفسی از دسته اقلامی است که مصرف آن برای بیمار حیاتی است اما داروخانه‌ها برایشان صرف نمی‌کند که این اقلام را بفروشند.
🔹
بهمن صبور عضو هیئت‌مدیرۀ انجمن داروسازان ایران می‌گوید که داروخانه باید پای بار پول شرکت دارویی را تسویه کند، به بیمار با پوشش ۹۵ درصدی بیمه دارو را بفروشد و حداقل ۶ ماه بعد پولش را از بیمه دریافت کند؛ آن هم با این تورم!
🔹
یکی از داوخانه‌داران مرکز شهر به فارس می‌گوید که در ۴ ماه گذشته قیمت برخی از دارو‌ها ۳ برابر شده و شرکت پای بار تسویه می‌کند، من چطوری می‌توانم با بیمه دارو بفروشم، ۸-۷ ماه بعد پولش را از بیمه بگیرم و با وجود تورم مجدد آن دارو را جایگزین کنم؟ مجبورم به بیمار بگویم من نسخه‌ات را آزاد حساب می‌کنم اگر نمی‌خواهید به داروخانه دیگری مراجعه کنید.
🔹
درحالی که به گفتۀ داروخانه‌داران پایتخت، دارو در ۳ الی ۴ ماه گذشته ۳ برابر شده، آخرین افزایش پوشش‌دهی بیمه‌های درمانی که شورای عالی انقلاب بیمه مصوب کرده برای ۶ ماه ابتدایی سال ۱۴۰۴ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/435547" target="_blank">📅 11:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435546">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
طباطبایی: معاون سیاسی دفتر رئیس‌جمهور در روزهای آینده معرفی می‌شود
.
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/435546" target="_blank">📅 11:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435545">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf24ab2a9.mp4?token=m5XpQpdRjkoCZ2wynBt7LZdTfOy8vdpecU3AGWqV5mieEi5IkJtK8tn6UJzu0un81_P0aqHQd19-tZHZx8vtxthSdrofiu7gT9GOEOA9YK0mphfTlrZfGTl7B-fYzuND-6A83AqKvQ2CEsj0HYjLI9o-coi6Ok_FKI2etm3LZzmSMee2IkuBMaRKVf9L4z7yyjWacXdIEXU6BlEBHKpIIsSwAIF9_n8QV-DQLGbPE8ppkxVt5_5M6EbqRVfQyxvCu2eo-i8aogx_-CkAN429xrzEBfXyfjGVbrLBlbZKWrFsAtqOSY2EApnqfT4DJMD07xGEC0OVSrMy9-K9da9CAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf24ab2a9.mp4?token=m5XpQpdRjkoCZ2wynBt7LZdTfOy8vdpecU3AGWqV5mieEi5IkJtK8tn6UJzu0un81_P0aqHQd19-tZHZx8vtxthSdrofiu7gT9GOEOA9YK0mphfTlrZfGTl7B-fYzuND-6A83AqKvQ2CEsj0HYjLI9o-coi6Ok_FKI2etm3LZzmSMee2IkuBMaRKVf9L4z7yyjWacXdIEXU6BlEBHKpIIsSwAIF9_n8QV-DQLGbPE8ppkxVt5_5M6EbqRVfQyxvCu2eo-i8aogx_-CkAN429xrzEBfXyfjGVbrLBlbZKWrFsAtqOSY2EApnqfT4DJMD07xGEC0OVSrMy9-K9da9CAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جعفر دهقان: بمباران مدرسۀ میناب توسط آمریکا قطعا عمدی بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/435545" target="_blank">📅 11:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435540">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPtrWXwWH8zSHSW5gt1HcY-vHx5YfZ_uFVKVbNN7dceIwpgbSgtL-e5fI65nUM8Eh1-TrJzysfQOKBpGt7oR5KtoXVbqAPYXxsPeYJPH3XjF6Jwjpi5P_IUDd6-b8c6vTXmh1OBYfWc9NkhlvRgacA7HRaVn4dlymsaUwM9HoM82hfai6gTE_TkRB15MUpzTSzXpWgvgLFWOVtBfqXOatvYFhQx-mgCjsWGC219LIITPuHZZ9cADQDXK070rsGvvGt-pb26J0Iz_AwS0-N2qXoCW2wKL3tngFOxQpNNtllwi_aWNhEQHAAzz5oVMApNry02ZoOcmQxHE9ojZi7UgQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c41m1E2W14KdrcxMUcViUVXw128VvpeBGBS7D9g2aacvs1NqMXqp_3gf8I1emYP67H_f06rGxkcBH9Zg55XZ7mxQhLzF0hlNH2eQNLNpbUm-tihxavYlsV00quPosuqEKacdy3S48lyVdOPai5dlSR-crSB53XxufBVL8sUxPzaJSprTFZ5CfqMlLwGG70D7cyEs_cFbnC2d7wpP7pI2VgyhcVWjV9CTzG9hLsOGERza3UI6yCT3NQIePyuzXWwlBiGubW92lbyn2PTPZ9ZhzsJ6TyP8k0p3nuEkYu5r7BFZhRxmxWlu3wQjsZcfKSXR1NM0IxOcr8sHN46XIt-oGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdBIsKEbCVijhtUy745J8YExw8gkn-D4WKBgcksenR2h2ldSa4dLbIH7n9jM6OYd18Ui7Gi5NOGhfWGt9rMRNv1kC_BP40QtiVRawXf_ymqSFmeLm2k6RysPHfo3uvfxqg62mUK4Wf93fzBLCg7BgeGRI21Xh5WiHD14f3d1tebP9a8GgtUD9O8mNUnHOS0s1IoaMvSvpZKX87EXnA_wWwifgAUHcpAiL6UKzBKFbnoM9j5IDWkYGMHPe6c2_9J0VHTn_0IeBAnRsmGXpAHZD2OI-X1flU4PPVNYhB1YMSAk6tkx9FlqtMALKOCiS-d9sBH9LoBxdkPn8MERd7tmQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hc5SrgP-DvBrCeZ0aFkNp1vmHeOEuGm3rGULI7YG32RWx2qcMwSFWGl43q_OCBU5oIEw4N2WQkrgT_e0Lx6wtrNduLcFubHdgKEx_o5OBykF3KID6L9uhq2ilaisw3X6ud40pwZC4ZXrUf9F1kruB3uvv223olK46J_MzMbdZ6jD5cS-Il1XH8i1xIqWHEgrfl87FiWkep5lWbjbGMBVqhnGM99HmpAkC4BQecAgMZWiE8rjEdNHpvRc9zcchZti8qsYK_wJb01zTY1acf-do1pjxoy1gRC9ZAbLCFSavaKcu-fxe2MgPZPpW0EsoRYB1JJdfg2z8a9hmGr2WKYUyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qye6Ysnywo9-ppSUEDpv8tScCnCYJg3SGQzQhJePBkUG6z_rUR9hDxh5XnZJzOPrV_R25ffv1xxTGB7C2JaJZgOqYk_Q3CKEBC0xgtvPXnQRIGl6n4m8W_NZqrrm4PmtnWV3apdmAENGDN-fxMddrMM1hMJnR3yS4I4CML1zz6WY1IGryhZiIcEI32qr_pbYrcH4K4ST9TokeWmHHP6YihyNLPVrtAx3G_6goobS-hfAbVx7whBVQQwuSv-IMzKHisjcqrHeCk-YfM4SmdCQFLlh_6xw-AV863-ftK7nQjEieToH_Cs46DwbtNSUZ8iRMxYU0PJjhtOKVHErbkydlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
ترامپ به سوال دربارهٔ تایوان جواب نداد
🔸
خبرنگار: گفت‌وگوها چطور بود؟
🔹
ترامپ: عالی بود. چین زیباست.
🔸
خبرنگار: آیا دربارهٔ تایوان صحبت کردید؟
🔹
ترامپ هیچ پاسخی نداد. @Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/435540" target="_blank">📅 10:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435539">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ece0d934.mp4?token=OosBsc_7e50bBCrxh8w6Z6T-GaAaDwMBH4T_2YORRQpRftCHxD1A4EZF5e5RyIQqjQyVjypCKRyu0jQGl2fgdDWCj3I_7-IeesfvuapYP3A30N3WwvwunBSIVDo_sy5A1Uhuy_0EYmmtwlYIafm7n2FJa2VdOsQpeWfiBDPjAq2J0-MsegMx6MnDrcg1Sp5wlYPuYQNagSQBsZQWnWL0bxZbGbi6WisyB1SqwfonZ-Y1CEsol3zeVesj_0VYCvyj6FHpyexRMWOwM0R2x9HlfEuv4eu1PF5xPZOJklVNk-d7JqBkZod5eIXSbOKEqvnFQKjxgp0iyLqpALRlYjzbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ece0d934.mp4?token=OosBsc_7e50bBCrxh8w6Z6T-GaAaDwMBH4T_2YORRQpRftCHxD1A4EZF5e5RyIQqjQyVjypCKRyu0jQGl2fgdDWCj3I_7-IeesfvuapYP3A30N3WwvwunBSIVDo_sy5A1Uhuy_0EYmmtwlYIafm7n2FJa2VdOsQpeWfiBDPjAq2J0-MsegMx6MnDrcg1Sp5wlYPuYQNagSQBsZQWnWL0bxZbGbi6WisyB1SqwfonZ-Y1CEsol3zeVesj_0VYCvyj6FHpyexRMWOwM0R2x9HlfEuv4eu1PF5xPZOJklVNk-d7JqBkZod5eIXSbOKEqvnFQKjxgp0iyLqpALRlYjzbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: زمان آن رسیده که زورگویی آمریکا به زباله‌دان تاریخ سپرده شود
🔹
برای تقریباً همۀ حاضران در نشست بریکس، مقاومت در برابر زورگویی آمریکا نبردی ناآشنا نیست. بسیاری از ما با شکل‌های متفاوتی از همین فشار و اجبار نفرت‌انگیز روبه‌رو هستیم.
🔹
اکنون زمان آن…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/435539" target="_blank">📅 10:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435538">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f88e62bfe.mp4?token=R-ubVC52C_ndnUqVJZPteRxmXt8_2uMeCgEX9ioVj8Scr7cmnyk28XW1JbrjsCRPPrVWiDXm8Of5iPU2NCiP7hyrBxZVAAMZVgjJkKZHv92MbBA76ELcUJUy4zCn6BJmKct4KXKIE0MokQCfj0svgKFCPuezLT2uW2C77Ls8F0e9sSHUqVoX3IAj-Mqyq07FP1G-i7dO_OabZ0XLjTtkos8tcM_HL_xREIF4kQguZPu7tnHI7JbJFo2vVyDhDSOEG5hpRN27foW9jHUeniObKqMIAO0X8Luj8x_l2PcU0s7LZtdcHKOipVjcXgOlMN_6KfAkf2XnJ0ZXQZpZTuoBkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f88e62bfe.mp4?token=R-ubVC52C_ndnUqVJZPteRxmXt8_2uMeCgEX9ioVj8Scr7cmnyk28XW1JbrjsCRPPrVWiDXm8Of5iPU2NCiP7hyrBxZVAAMZVgjJkKZHv92MbBA76ELcUJUy4zCn6BJmKct4KXKIE0MokQCfj0svgKFCPuezLT2uW2C77Ls8F0e9sSHUqVoX3IAj-Mqyq07FP1G-i7dO_OabZ0XLjTtkos8tcM_HL_xREIF4kQguZPu7tnHI7JbJFo2vVyDhDSOEG5hpRN27foW9jHUeniObKqMIAO0X8Luj8x_l2PcU0s7LZtdcHKOipVjcXgOlMN_6KfAkf2XnJ0ZXQZpZTuoBkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان و سیل در شمال هند با ۵۶ کشته
🔹
دست‌کم ۵۶ نفر در اثر طوفان شدید و باران‌های سیل‌آسا در شمال هند جان خود را از دست دادند.
🔹
به گزارش خبرگزاری PTI، بیش‌تر قربانیان زیر آوار دیوارها و سایبان‌های فرو ریخته گرفتار شدند.
🔹
گزارش‌هایی از زخمی شدن ۵۳ نفر، آسیب دیدن ۸۷ خانه و کشته شدن ۱۱۴ دام خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/435538" target="_blank">📅 10:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435537">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f501e44a.mp4?token=iTY_dA5G7s8-_fZZRjGXOtXkTYjAWfBf99STgStBiXg8laHK2raR7_QX4HHHtru2FJwmfKhNwAphjTOvnqgYD2wC9K8767hC3_xr6069dxiAqOkZULqK2QmOMuIXCbd7Lic0ILISrLou1GwRz6kFf-CbIqEbjZDp9Mx86KoGeYsf5s00G66hQj83-mcLfnYUCY2Jzpp5b3RCqfUWumud8fXYwxI2TQ1vRz1pFx61Re9QD1-8uGngMKUS5sb0ZEkQz31MwkABHFMUxXeUj-RUfVMHOsWjbLvAaI27sDnn9TY6neX86nQ2Hevew3ua7UNsp3nBTSbsVmp4PUjh9kVKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f501e44a.mp4?token=iTY_dA5G7s8-_fZZRjGXOtXkTYjAWfBf99STgStBiXg8laHK2raR7_QX4HHHtru2FJwmfKhNwAphjTOvnqgYD2wC9K8767hC3_xr6069dxiAqOkZULqK2QmOMuIXCbd7Lic0ILISrLou1GwRz6kFf-CbIqEbjZDp9Mx86KoGeYsf5s00G66hQj83-mcLfnYUCY2Jzpp5b3RCqfUWumud8fXYwxI2TQ1vRz1pFx61Re9QD1-8uGngMKUS5sb0ZEkQz31MwkABHFMUxXeUj-RUfVMHOsWjbLvAaI27sDnn9TY6neX86nQ2Hevew3ua7UNsp3nBTSbsVmp4PUjh9kVKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان اداری و استخدامی: ساعت کار اداره‌ها از ۲۶ اردیبهشت تا ۱۵ شهریور ۷ صبح تا ۱۳ خواهد بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/435537" target="_blank">📅 10:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435536">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfUc9jRMVXLlNLqcSKhxXn9QnwDDV-V9b72G5Ag8YWfLgcv9qGmrfuTdDTuGfrG321WQbZ52r6Boewr_Lwfhiq-Ldy2eALwXX_9IH99J9jZI1y3tM5omM6ulWQ0WDuvzOo138SsVut_M7iCvg3dkAgvCPBqE3IF9x1NpY0aOtm1mFUaZcsKNPvVKfGVi0TrmQy6F8gTxSuFYKwufPx9MTG7rpJ5JSE3MTzhqfY-6-XM-n_uDBPxFs4euuAHI_rr3r4hclazn5rSN_ZGe1wW1XIwws60GJYuk7t5qDOsPa1w30MEFora-qDZxXxHTZbn58gALxrF50SdDTzy7olp2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ملی‌پوشان و مردم باهم در میدان انقلاب سرود ملی خواندند  @Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/435536" target="_blank">📅 10:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435535">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9d0ac827.mp4?token=cNj0sb2_NfHs0LHy8Ky9NQTpPyAGKF6D6zt05O76QSYSeGSVm4W4-ptrwS4rKakFOS2765y4eNZ0AwzcBA6UvU6QOnnwLYHin28rl89VYJoHmvP3SYgbwQ_Qtag9NeP2cdrua6DA5_d-jGZ-bLVmCE9is9ONbbF622I1Oo69XMApSbD-u3kFum8Z0HimgDXSjxwoq6sieHvyRZNoiZZkSiS7JwtteGXjP8wvn5I7sPYY7w0abpf_ihs3bg6r3XkwYCAQyp6lgDofUb5Ep7pzsmSn473_LHzbp5G-9szEA1qZrcKccdA9nA93oZXetN3PO-ZC_KsSx7ABFOrWmKyvejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9d0ac827.mp4?token=cNj0sb2_NfHs0LHy8Ky9NQTpPyAGKF6D6zt05O76QSYSeGSVm4W4-ptrwS4rKakFOS2765y4eNZ0AwzcBA6UvU6QOnnwLYHin28rl89VYJoHmvP3SYgbwQ_Qtag9NeP2cdrua6DA5_d-jGZ-bLVmCE9is9ONbbF622I1Oo69XMApSbD-u3kFum8Z0HimgDXSjxwoq6sieHvyRZNoiZZkSiS7JwtteGXjP8wvn5I7sPYY7w0abpf_ihs3bg6r3XkwYCAQyp6lgDofUb5Ep7pzsmSn473_LHzbp5G-9szEA1qZrcKccdA9nA93oZXetN3PO-ZC_KsSx7ABFOrWmKyvejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکلیف نحوۀ امتحانات نهایی ۲ ماه دیگر روشن می‌شود
🔹
در حالی که پیش‌تر احتمال برگزاری دومرحله‌ای امتحانات نهایی شامل داخلی مجازی و حضوری کشوری مطرح شده بود، حالا وزیر آموزش‌وپرورش اعلام کرد «تا ۱۵ تیر برای مشخص‌شدن وضعیت امتحانات نهایی صبر می‌کنیم.»
🔹
به گفتۀ…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/435535" target="_blank">📅 10:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435534">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d0c1a06a.mp4?token=Nvt-2i8nlvoZVSH3Lq7S91XcFOcUoujpNj67XMxoO4uPdGHYHXjsB_w94uI-voaNuVyzlpRwDK5UMzNTqCxqZiZEd639V8tBfPrDO5An2RrezA2UBcjZ0YeVQwk8H5q87G4EVahxjW3ChqEBfg581zWLNTmc__qgebu13ct3NOQkjMRBK_KLorD_YDVMKnDVvaXZMWRlgHT5GzoVMKHlp1p8QmuX5ZtcEffNzipRfW08BZb-GaDEVgfS0GNMNJ2UytVCW_tsaQYk7bAA8W4R43VERn_MGgri0hRp_YTTZiOLzo81kdFaJqxviKqNGcrmhkMZMovkCcIpvuR8LAXkuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d0c1a06a.mp4?token=Nvt-2i8nlvoZVSH3Lq7S91XcFOcUoujpNj67XMxoO4uPdGHYHXjsB_w94uI-voaNuVyzlpRwDK5UMzNTqCxqZiZEd639V8tBfPrDO5An2RrezA2UBcjZ0YeVQwk8H5q87G4EVahxjW3ChqEBfg581zWLNTmc__qgebu13ct3NOQkjMRBK_KLorD_YDVMKnDVvaXZMWRlgHT5GzoVMKHlp1p8QmuX5ZtcEffNzipRfW08BZb-GaDEVgfS0GNMNJ2UytVCW_tsaQYk7bAA8W4R43VERn_MGgri0hRp_YTTZiOLzo81kdFaJqxviKqNGcrmhkMZMovkCcIpvuR8LAXkuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صفری: روابط ایران و چین درازمدت و راهبردی بوده و خواهد بود
🔹
سفیر اسبق ایران در چین: روابط ایران و چین بسیار درازمدت و راهبردی و استراتژیک بوده و خواهد بود. چین همواره به چهار عبارت مورد اعتقاد خود پایبند بوده و ما در مسائل حقوق بین‌الملل و حقوق بشر همراهی نزدیکی با چین در دنیا داشته‌ایم.
🔹
چین همواره منافع جمهوری اسلامی ایران را مدنظر داشته و ایران نیز منافع چین را. یکی از مسائل بسیار مهم، مسئله انرژی است؛ هم تأمین آن و هم امنیتش. چینی‌ها آگاهند که تأمین امنیت و سرویس‌دهی نفت در خلیج فارس و دریای عمان همواره از سوی جمهوری اسلامی ایران انجام شده و این سرویس برای چین برقرار بوده و خواهد بود.
🔹
سفر ترامپ به چین از جنس سفرهای عادی بین دو کشور است و اغلب اختلافاتی مثل تایوان، تعرفه‌ها و فلزات کمیاب مطرح بوده است. اما من معتقدم قدرت اقتصادی چین بسیار بالاتر از آمریکاست و با همین قدرت اقتصادی و تجاری، بهترین شریک برای آنها در منطقه در تمام زمینه‌های فرهنگی، امنیتی، سیاسی و اقتصادی، جمهوری اسلامی ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/435534" target="_blank">📅 10:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435533">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwBZrtzakYSl5_ZUu8bMOaBXt7ilaDFz2K2q9uyzoLEA0_y2yurWvAdRDrOc9YRfrS-KzB27VPUGAL_Nsd2DhASVFYIhnAbhKq_gK1KYF1IvM_T5VN50j3Jd3ZRabFgNT0xa5XPmtiTftJMeaXTww9pqmSO-UBi6mY4eaODmT9nI6WQMjiOM-vCTG7RUl_veD9AsC41fbM3OrppFIC9Lj7Mo_SwkefeZISL8dDftkPDs84ttYPpIvh-AMfBILfOhtsWFQ8A7XhqapOBWjm_JVoBKDlLCoYNlMTv9nWa7bmTzvgcAlhoY6-SInwaZORLjsNmOJv_KWVVmWVv-8ZlCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: باید برای همگان روشن شده باشد که ایران شکست‌ناپذیر است
🔹
سخنرانی وزیر خارجه در نشست وزرای خارجۀ کشورهای عضو بریکس: من از سرزمینی کهن می‌آیم؛ سرزمینی که رهبرانش با شجاعت در کنار مردم خود برای تحقق عدالت، استقلال، و دفاع از حاکمیت و تمامیت ارضی ایستاده‌اند…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/435533" target="_blank">📅 10:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435532">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اموال ۴۷ نفر از خائنین به وطن در همدان توقیف شد
🔹
با دستور مقام قضایی اموال ۴۷ نفر از خائنین به وطن و کسانی که علیه امنیت و ثبات کشور اقدام کرده‌اند، در راستای حفظ حقوق عامه به نفع مردم در استان همدان توقیف و ضبط شد. رسیدگی به پرونده این افراد در جریان است.
🔹
با دستور مقام قضایی اموال ۴۷ نفر از خائنین به وطن و افراد تاثیرگذار در شبکه همکاران دشمن در راستای حفظ حقوق عامه و اجرای قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونسیتی علیه امنیت و منافع ملی در استان همدان به نفع مردم و هزینه کرد برای بازسازی اماکن آسیب‌دیده از جنگ توقیف شد و پرونده این افراد در حال رسیدگی است.
🔹
در حال حاضر ۶ نفر از این افراد مقیم کشور انگلیس، ۲ نفر مقیم سوئیس، یک نفر مقیم روسیه، ۸ نفر مقیم آلمان،۶ نفر مقیم ترکیه، ۸ نفر مقیم کشور عراق، ۴ نفر مقیم آمریکا، یک نفر مقیم ایتالیا، یک نفر مقیم عمان،یک نفر مقیم کانادا، یک نفر مقیم عربستان، یک نفر مقیم ارمنستان، ۲ نفر مقیم غنا و ۶ نفر در داخل کشور هستند که دستورات لازم برای ضبط اموال آنها صادر شده است.
🔹
پیش از این نیز با دستور مقام قضایی اموال مهرداد ماهر که نقش موثری در شبکه همکاران دشمن و خیانت به وطن در استان همدان داشته، به نفع ملت توقیف و ضبط شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/435532" target="_blank">📅 09:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435531">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a382d07f.mp4?token=U4W-RZVawKuRzu2W-yBdnHTWeKSFTKqhZdxXQ06hgB63wUe-Teq3TUt-MYHioJvbbstzThhcoWuCuZLP_RFrifJ7E762hCQAwj5uzMyUB7uVUmwE5lvS7CpKp9fBl8DEB3IWN_h5C1MT4bKjd3Uxd2x8HcOPTB_SVwGX-A1XkSgK90-Ed8uHR4OF_X6FG3VuKpJUEYpVWz6gMDEO85de5ncvhgcm4VDlHVpiFUVp3nJeUwipnt9smF7zXgKqkCOlLpnHuDDUUetz-q6EQkOVViRhIo3ppBOJQOByCyILUwqHE3Xgig5gc4jNME2LPITy5FcybzMKBhNx4qOohF-kdqmgblDKYj7CbZMHhK8_UWg_u9cu6rCZKhddG7Eg9Fh_HGC1uZJ0NDHmE9y1GtmgUGmLeXvzU906fN_s0iw2jM2q940V5SEpkkK9zx3kwB97ebm-7sBJ5m7h2m07tZ6OkKmzWLxN0iVLqpcD7FvgDx3ioKuAcuElFzP039sNBmrNlQTMJMY4RTsrM_EWodVpYelIvb86z7ybNtlLEwvyANmUsxYBwOGwbLRJ1tbEjDikDlguhI_ghf8zkmHeTPzQHPKfMbmu5FWcuU624K-RKt20TVXIKZUN_koJchhsN4efJQ8JqEVc3WqKl1CVRiGLj4ELyPT7VmKob_3z8KCh-Eo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a382d07f.mp4?token=U4W-RZVawKuRzu2W-yBdnHTWeKSFTKqhZdxXQ06hgB63wUe-Teq3TUt-MYHioJvbbstzThhcoWuCuZLP_RFrifJ7E762hCQAwj5uzMyUB7uVUmwE5lvS7CpKp9fBl8DEB3IWN_h5C1MT4bKjd3Uxd2x8HcOPTB_SVwGX-A1XkSgK90-Ed8uHR4OF_X6FG3VuKpJUEYpVWz6gMDEO85de5ncvhgcm4VDlHVpiFUVp3nJeUwipnt9smF7zXgKqkCOlLpnHuDDUUetz-q6EQkOVViRhIo3ppBOJQOByCyILUwqHE3Xgig5gc4jNME2LPITy5FcybzMKBhNx4qOohF-kdqmgblDKYj7CbZMHhK8_UWg_u9cu6rCZKhddG7Eg9Fh_HGC1uZJ0NDHmE9y1GtmgUGmLeXvzU906fN_s0iw2jM2q940V5SEpkkK9zx3kwB97ebm-7sBJ5m7h2m07tZ6OkKmzWLxN0iVLqpcD7FvgDx3ioKuAcuElFzP039sNBmrNlQTMJMY4RTsrM_EWodVpYelIvb86z7ybNtlLEwvyANmUsxYBwOGwbLRJ1tbEjDikDlguhI_ghf8zkmHeTPzQHPKfMbmu5FWcuU624K-RKt20TVXIKZUN_koJchhsN4efJQ8JqEVc3WqKl1CVRiGLj4ELyPT7VmKob_3z8KCh-Eo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی: آمریکا درباره تایوان اشتباه کند، جنگ می‌شود
🔹
رئیس‌جمهور چین در دیدار با همتای آمریکایی خود در پکن در خصوص هرگونه تحرکات واشنگتن در خصوص تایوان هشدار داد و گفت که هر اشتباه آمریکا می‌تواند به تقابل آمریکا و چین منجر شود.
🔹
شی جین‌پینگ با تأکید بر این‌که…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/435531" target="_blank">📅 09:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435530">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPjsuMy4LqiZ4737-zkujXWWfhR40lKdDtHsjVfDy6comN_bpuaKpZhRtUBxcAEeBBTLdzm2d1ZEsD23bmUMUnIOmnKpYEp5PlMPFUNTUDrkCTTe1JoeQ12vJnpaRV1X5nm-4wrb3hjmv0ZATcD7gw72lxDHojwmCrr5wl-JBfr2WlmM-An-pkXHxmSRZ_rn3jX-JNf6NhQ-KRG3tlF-rfpUsZP65mSK6rGYzUW6fEG6IfGRd53Pw9Rd0VrwBC5CcR1zelQ84vWw02HxaIxb8WlhmadiH73X5AbmR6XokbH6FF37gAvqRhA2tBqww-yKKtgTr6tUBQajk-VNdAp3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عکس یادگاری وزرای خارجه بریکس در دهلی‌نو  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/435530" target="_blank">📅 09:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435529">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664d5121ba.mp4?token=nmPxLfhZLOL_A7v-WNqfEkiDDgYt_XTwelK7_4R8GBqIrlYLJPrKNBFluIOmQLJbNmZ5rnNgTO_VcbH0-zvZjHSEfI6UXh_1UFQ5VEM05BP3c_P9ZmL8vAPV22zUWT9VPlJUcI8uuEMbJbRJmHzCekrXHUqgADJPyH3yRaRTrVvZgp-osvWTkbmeJ09PYzFRyq5Zpgya0jFA7ksMYzlp0VsXNElpdIzlXhKq4_9SPSpzdY_n2u8HXEvJfmZlMZMYZKqw_N_c-svQNtrIgZdpuX8-Dmx1TV5tsQG-56ZqbOwz_5jSZBRK1cTSymPXiuvmwdl5Hs_cNJdT2LyDnKaw2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664d5121ba.mp4?token=nmPxLfhZLOL_A7v-WNqfEkiDDgYt_XTwelK7_4R8GBqIrlYLJPrKNBFluIOmQLJbNmZ5rnNgTO_VcbH0-zvZjHSEfI6UXh_1UFQ5VEM05BP3c_P9ZmL8vAPV22zUWT9VPlJUcI8uuEMbJbRJmHzCekrXHUqgADJPyH3yRaRTrVvZgp-osvWTkbmeJ09PYzFRyq5Zpgya0jFA7ksMYzlp0VsXNElpdIzlXhKq4_9SPSpzdY_n2u8HXEvJfmZlMZMYZKqw_N_c-svQNtrIgZdpuX8-Dmx1TV5tsQG-56ZqbOwz_5jSZBRK1cTSymPXiuvmwdl5Hs_cNJdT2LyDnKaw2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار فاکس‌نیوز: ماشین ما در چین ۲ دقیقه در محل «توقف ممنوع» ایستاد و بلافاصله پیامک جریمهٔ ۴۰ دلاری برای راننده آمد
🔸
اینجا دوربین‌ها در هر لحظه نظاره‌گر هستند و همه‌جا حضور دارند.
@Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/435529" target="_blank">📅 09:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435528">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP0cNl6Tffn00Qw0teSkkJBeYLFauJtGEb-KeWNCLhAr14q-5Z5AUJc0TJcNhngLQSnnS1WYkyuCSFHW0YZMKTOIdkCLrOyPPuFSW6BnWGQX0ktSW857TYR7E3yE0uy2xANi8gjHKne1LkROGaiKHO2Mi8Vp8W8cHz67DBNxpteltT35AMHoiNw6wo96Mvm09n8ZkFuPe3kBJcO4LqGjmVdXi7JcLzHSFgEpbSElYOvazo4mb1o16EmxymwCFE_WZ83bhqFhqSI-6YDr7RyVnmLVatW-lAV9x7cmjXSJdgqGRYnS3DkKgBDU7CeAk07582CbpQS-QiWA5H2nWxQzsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران و پکن روی دور تند ارتباط موثر
🔹
رابطهٔ ایران و چین در سال‌های اخیر از یک همکاری صرفاً تجاری به سطح «مشارکت جامع راهبردی» ارتقا یافته است.
🔹
در شرایط پساتنش‌های اخیر، تهران و پکن با نگاهی متوازن و مبتنی بر احترام به منافع یکدیگر، تلاش می‌کنند مسیرهای اقتصادی را بازگشایی و حجم مبادلات را افزایش دهند.
🔹
یکی از مصادیق عینی این اراده، تحرکات قابل توجه در آبراه استراتژیک تنگه هرمز در روزهای گذشته است.
🔹
طی روزهای گذشته، داده‌های ردیابی دریایی نشان می‌دهد دست‌کم ۶ نفتکش و کشتی فله‌بر با مالکیت یا عملیاتی چین از تنگه هرمز عبور کرده‌اند.
🔹
براساس تحلیل داده‌های موسسه «کپلر»، از میان ۳۷ نفتکش حامل نفت خامی که طی ماه مارس تا اوایل آوریل ۲۰۲۶ از تنگه هرمز عبور کرده‌اند، ۳۰ فروند منشأ ایرانی داشته و تقریباً تمام آن‌هایی که مقصد اعلام کرده‌اند، راهی چین بوده‌اند.
🔹
ایران با تضمین ایمنی مسیر و اعطای تسهیلات ویژه به کشتی‌های چینی، نقش فعالی در حفظ جریان تجارت انرژی شرق آسیا ایفا کرده است.
🔹
این اقدام عملی، نشان‌دهنده اراده تهران برای تبدیل چالش‌های امنیتی به فرصتی برای تحکیم روابط اقتصادی با شریکی است که در شرایط تحریم نیز در کنار ایران بوده است.
🖼
اما چرا ایران چین را شریک قابل اعتماد می‌داند؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/435528" target="_blank">📅 09:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435527">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYn6AokCBBqfh4JM_o_-xc6h70AmdrdIREBKMH5vllFCQPBMvbgwQbBOH9DWSN_iyvueVbWoyEcK38oePmoQj4PP0C96xvlu6HgFnZDqmVHsJV_sSfTKNshNpenxlpOcYMuC449glK2e8eAn-4EFbYytU9V-T3QCtgM_CJjs-qZqYgVbUj0t0cuBOYUrXk8MQQWvzSLec8hb1CeqosWvGmdtXglFx3sWTqLb7P-uA-CaSsoQEdz2nneoeUB2B7CogJm8jP9ce2y2iLHrgfvjnqFibUIX_i65hxzUttVy2NyQ6APreO9qd5eZqSBem_He4JJB4E6LdpvN2RYD6P12Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیباکلام ۳ ماه از انجام فعالیت رسانه‌ای منع شد
🔹
قوه‌قضائیه: هفتهٔ گذشته درپی مصاحبه صادق زیباکلام با یک خبرگزاری، دادستانی تهران علیه نامبرده و رسانهٔ منتشرکننده اظهارات او اعلام جرم کرد.
🔹
پس از تشکیل پروندهٔ قضایی برای نامبردگان، متهمان به مرجع قضایی مراجعه کردند و پس از دفاع، تفهیم اتهام شدند.
🔹
در نهایت با توجه به مستندات و تحقیقات صورت‌گرفته قرار جلب به دادرسی و کیفرخواست پرونده صادر شد.
🔹
همچنین قرار نظارت قضایی ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی به مدت ۳ ماه به صادق زیباکلام تفهیم و ابلاغ شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/435527" target="_blank">📅 09:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435526">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873e2d3fb9.mp4?token=Cm2b6JLL2zsFRLlPNtdjuCp8qeuivGiE8-EKQcKTPMud8oRbppWjPACzrhyTX4-KCrQg02KDjW8m0exC6aMWwVg00GGR33ed6cIRQw5cHbObofEwYe6tLVY7WV5FXXNFG6WNv767_sWMRWq4baVsed05IOjVEpZGGBHaCidaEgRT_Phs5-669HtpyJjM8u0PnqGEzhJG48cBvC-nmFdm7FhDNi6v0aYGc3kSCf-9oekEFZM2M1pyA9nl-txnooPzH7hz-p2cYoA2esadCjEouTyBbmIx_KMkmoFUhvYXp-SkTdnLn3A0qMTq2jt0oFEThKCmpO5mPYEzL4_zMfK3Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873e2d3fb9.mp4?token=Cm2b6JLL2zsFRLlPNtdjuCp8qeuivGiE8-EKQcKTPMud8oRbppWjPACzrhyTX4-KCrQg02KDjW8m0exC6aMWwVg00GGR33ed6cIRQw5cHbObofEwYe6tLVY7WV5FXXNFG6WNv767_sWMRWq4baVsed05IOjVEpZGGBHaCidaEgRT_Phs5-669HtpyJjM8u0PnqGEzhJG48cBvC-nmFdm7FhDNi6v0aYGc3kSCf-9oekEFZM2M1pyA9nl-txnooPzH7hz-p2cYoA2esadCjEouTyBbmIx_KMkmoFUhvYXp-SkTdnLn3A0qMTq2jt0oFEThKCmpO5mPYEzL4_zMfK3Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی: آمریکا درباره تایوان اشتباه کند، جنگ می‌شود
🔹
رئیس‌جمهور چین در دیدار با همتای آمریکایی خود در پکن در خصوص هرگونه تحرکات واشنگتن در خصوص تایوان هشدار داد و گفت که هر اشتباه آمریکا می‌تواند به تقابل آمریکا و چین منجر شود.
🔹
شی جین‌پینگ با تأکید بر این‌که…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/435526" target="_blank">📅 09:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435525">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/990f2cdf7b.mp4?token=ujcFAyRuu2i-T1tKW-wlVCEWo8ndV1RYVp9BpxrY-sPG_HVVDYNUUpVDIOTEqRPZutxlvPEv84Mo0JsVdsHTQNTnN9eINiahRZ_yvGDl0jw47OqnGbElK8CLBYa_j1bBFzIJsh_VazNlHy9WN1lPXv6FljzMRByHeI4FQJkHevsmGsU5MggTEAZ4zvuKeElxyRhdhW_9miih1KLMoQYp_-6ome0qp2s35oVUdnj1ZVJgBw-qqt-VLqQoxK5oX8fdx4frCTjCdSRyh8E3Uf-mPDG082bWyVKZSOaInL71Ju33jaJzvdw84STQpou3nrHzQ5AVSVLZ1s5nrqdqE41RRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/990f2cdf7b.mp4?token=ujcFAyRuu2i-T1tKW-wlVCEWo8ndV1RYVp9BpxrY-sPG_HVVDYNUUpVDIOTEqRPZutxlvPEv84Mo0JsVdsHTQNTnN9eINiahRZ_yvGDl0jw47OqnGbElK8CLBYa_j1bBFzIJsh_VazNlHy9WN1lPXv6FljzMRByHeI4FQJkHevsmGsU5MggTEAZ4zvuKeElxyRhdhW_9miih1KLMoQYp_-6ome0qp2s35oVUdnj1ZVJgBw-qqt-VLqQoxK5oX8fdx4frCTjCdSRyh8E3Uf-mPDG082bWyVKZSOaInL71Ju33jaJzvdw84STQpou3nrHzQ5AVSVLZ1s5nrqdqE41RRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
ورود عراقچی به محل اجلاس وزرای خارجۀ کشورهای عضو بریکس با استقبال وزیر خارجۀ هند   @Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/435525" target="_blank">📅 09:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435524">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e52d642c7.mp4?token=ADPykdYhC23CofXWylDnitA6NZjVJ8eILOCosbOYPTyM7rA6LPQGr1iWB1sSoNyoazfHA2HLOcjecLvyoux6OgaKA-mxl-oBhnwi5F_20dRvoOxJDN1Kd74aE7C7ihKp8-i-wVqDK0rPZORYG-wO5EgagQ69pj3dU96sJz7WrJKZqULRmucbDcnZEhmq9Rlb1Aw5gIr-ffL5cZ3BAYNXKgSQZJLYKO93ejVbmHCW5n6DJGTnmiPsUEGHgAi4Ejn5u-Le34L5Yz3vZSqQJ-mx30Czg9NsIsOahuac-h3DAMUVLyq5OBuzdpEoIxWz-Bp2Ddxh_YzNy_AyU4a2nKa0JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e52d642c7.mp4?token=ADPykdYhC23CofXWylDnitA6NZjVJ8eILOCosbOYPTyM7rA6LPQGr1iWB1sSoNyoazfHA2HLOcjecLvyoux6OgaKA-mxl-oBhnwi5F_20dRvoOxJDN1Kd74aE7C7ihKp8-i-wVqDK0rPZORYG-wO5EgagQ69pj3dU96sJz7WrJKZqULRmucbDcnZEhmq9Rlb1Aw5gIr-ffL5cZ3BAYNXKgSQZJLYKO93ejVbmHCW5n6DJGTnmiPsUEGHgAi4Ejn5u-Le34L5Yz3vZSqQJ-mx30Czg9NsIsOahuac-h3DAMUVLyq5OBuzdpEoIxWz-Bp2Ddxh_YzNy_AyU4a2nKa0JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: در استان‌های خراسان‌شمالی و رضوی، گلستان و سمنان هشدار سطح نارنجی صادر شده.
@Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/435524" target="_blank">📅 08:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435523">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn2Lp3wJ_vSxvXOhxoSBbjJEZvF3okB7yMD5TrUp8oLQvSI1_yVCj5gr4OKvVWIBpII9jZxj5qmuOMfGGCtGvJys_8DJuV66w3Mmoq7O63MZkzNvSSJfpvppMf2t_eev-kLdZzWlIi-L9K6L2s5Blx0RDtjMhb34-nhTTAHTbWKoUyEVh_defSiUjgKVuX_Y39MJaVTb8uXDT0eCgI6Fz4UrdN4ey-2ztuOMWe12l85zbgonnV2XhC8TnAY-6wdnAd7om4PRJaCjL1PXGS2mIIzjAQOPXGXLMyygBADzMjrdXWL5n4Og9IKaOmLM3MkeHiiQOQCkGbhxnZo_1SJ2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شی: آمریکا درباره تایوان اشتباه کند، جنگ می‌شود
🔹
رئیس‌جمهور چین در دیدار با همتای آمریکایی خود در پکن در خصوص هرگونه تحرکات واشنگتن در خصوص تایوان هشدار داد و گفت که هر اشتباه آمریکا می‌تواند به تقابل آمریکا و چین منجر شود.
🔹
شی جین‌پینگ با تأکید بر این‌که «استقلال تایوان با صلح در تایوان سازگاری ندارد»، ادامه داد «برخورد درست با مسئله تایوان به حفظ روابط دوجانبه بین چین و ایالات متحده کمک می‌کند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/435523" target="_blank">📅 08:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435522">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/489ae3154a.mp4?token=vM9HgHP2cGnZz2PE01S9W1Pzrj9Jyba57kEtTMQzjpbVDIGiIAtz4QkgbwNf-buuaV2YTu81wNW6j1fwar75Sgr1qJvVsS5AVih-T4OLtoodDdaNPqbWJe8_PmxNvHDevqi-CXgbekI43cFpbEDl6D2QQ640qGO58GqtCS3c4WduGpDa7GUXAfH8n-oohUXBOWu9jwERKzamKhRe3zOreFkGZlZtiwO7U_QdOjKtfV65jq9_yEuNOhxW8DKbK7a6YotFE0KLOWUpafN5jWFDgNnzFpJ6_ESdU5rBSsLpBd9k2z160Hq1ib0RvGNlUTJ3CkR-Q6CEwh4F3v8EdJ09pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/489ae3154a.mp4?token=vM9HgHP2cGnZz2PE01S9W1Pzrj9Jyba57kEtTMQzjpbVDIGiIAtz4QkgbwNf-buuaV2YTu81wNW6j1fwar75Sgr1qJvVsS5AVih-T4OLtoodDdaNPqbWJe8_PmxNvHDevqi-CXgbekI43cFpbEDl6D2QQ640qGO58GqtCS3c4WduGpDa7GUXAfH8n-oohUXBOWu9jwERKzamKhRe3zOreFkGZlZtiwO7U_QdOjKtfV65jq9_yEuNOhxW8DKbK7a6YotFE0KLOWUpafN5jWFDgNnzFpJ6_ESdU5rBSsLpBd9k2z160Hq1ib0RvGNlUTJ3CkR-Q6CEwh4F3v8EdJ09pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ به چین رسید  @Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/435522" target="_blank">📅 08:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435521">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muocio0G2KKhBqfT-ovg9BXs29ow37V0yHWIaX4fR8Uid2b34gOUJR4QeH--fwg0BbCp8CuZ8Fbj2VWzeBG6m_RpHUdQ5B-8KjyyRMo-wcsW01xkzlZ9H1Zf7uxWEoeet3RJi7z91e9mKKH6VQcPYLAyJwjaYwyO469cY4VU7lCpvopWgWddEtOHI6zP4pCrwG5CQO7WmkC7zhS7LuCd6Quc3LvIBdr6fiEZBFBdhqfW_HQBjAD8nqWR_uyMDj7szQnp2qXIpM3P_ikebkVtNKXF5jPxUwycobKYDuamdrQsQJUkqBpTODV-uV3wpP4lsq5o_5PFHWWimYFQlUCA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ورود عراقچی به محل اجلاس وزرای خارجۀ کشورهای عضو بریکس با استقبال وزیر خارجۀ هند
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/435521" target="_blank">📅 08:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435520">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed12c1373c.mp4?token=Lv0dZHz_Im94yufucBiswX3qJhoA9AkQfXzgf53Z6soFGV1oww2SAYkS9TQrkRPdLeMKMb1xuCyQ2X50hYTrVVBHbm5lxNJ_VGAwYWpAzbraG2174CbmADjiWALUt8zhh4qEMHIKyAptV5pB7833rm41N2botqRZmlX0m41V5Ec7v9YkT1_PciflMigl9sYiIKuWT1_YUzPwF6I_-bysF4kIp0nTvw1SNIcW8n9mYf_7vT1Ah6qeDAgSoXE5Oj-NHMdFV59XDIRg1qiqrsHJPf4PVSbZVkcbuBsi-OG5Pwq4WfApyNtzOAXxBgBfbEcxY-AXliAuInoi9soLOgVqtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed12c1373c.mp4?token=Lv0dZHz_Im94yufucBiswX3qJhoA9AkQfXzgf53Z6soFGV1oww2SAYkS9TQrkRPdLeMKMb1xuCyQ2X50hYTrVVBHbm5lxNJ_VGAwYWpAzbraG2174CbmADjiWALUt8zhh4qEMHIKyAptV5pB7833rm41N2botqRZmlX0m41V5Ec7v9YkT1_PciflMigl9sYiIKuWT1_YUzPwF6I_-bysF4kIp0nTvw1SNIcW8n9mYf_7vT1Ah6qeDAgSoXE5Oj-NHMdFV59XDIRg1qiqrsHJPf4PVSbZVkcbuBsi-OG5Pwq4WfApyNtzOAXxBgBfbEcxY-AXliAuInoi9soLOgVqtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله نوری‌همدانی با صدور فتوایی، پرداخت وجوهات شرعی مقلدان «رهبر شهید» به رهبر معظم انقلاب را مجاز اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/435520" target="_blank">📅 08:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435519">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آخرین وضعیت نحوۀ برگزاری امتحانات دورۀ متوسطۀ شهر تهران
🔹
آموزش‌وپرورش تهران از پیش‌بینی دو سناریو برای نحوۀ برگزاری امتحانات پایه‌های هفتم تا دهم خبر داد.
🔸
سناریوی نخست: در صورت تداوم شرایط فعلی، احتمالا امتحانات داخلی دانش‌آموزان پایه‌های هفتم، هشتم، نهم…</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/435519" target="_blank">📅 07:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435517">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFiuTv-WG-z4CCiEk80z-DlxRZ5q8efxh-Yww3Rc2h2rcKnW3nbVD9VbfnK0MGWWprunBBLGRODawvsUIZWpziG6P9510_WK7g4PAI97_oSWxA--r6ev1y6twPLPUZk-VlEf4ibmT9K1f_ISYfaFLflAi8Ferk4ZzdFAwL_jFsIwG9o26aXoEHMMu60jIEhQgETvDTDQseYtQUjGL9fohDk2jabZY7Pk4OOY9MfhLozczMgD4JDyt9mODKKldOUQNd2hH0Lnv-1gz87ghL8Bwciv8akNpuy8vhRt3XQ8eKx76oHEDMawuBIixSzkLL8dDBHiKho_Seq9SVxqk7TC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت نحوۀ برگزاری امتحانات دورۀ متوسطۀ شهر تهران
🔹
آموزش‌وپرورش تهران از پیش‌بینی دو سناریو برای نحوۀ برگزاری امتحانات پایه‌های هفتم تا دهم خبر داد.
🔸
سناریوی نخست: در صورت تداوم شرایط فعلی، احتمالا امتحانات داخلی دانش‌آموزان پایه‌های هفتم، هشتم، نهم و دهم از تاریخ ۹ خردادماه به صورت حضوری و مدرسه‌ای, با رعایت اصل پراکندگی (کلاس به کلاس) برگزار خواهد شد.
🔸
سناریوی دوم: در صورت ناپایدار شدن شرایط و بروز محدودیت‌های احتمالی، امتحانات داخلی این پایه‌ها به صورت غیرحضوری برگزار شود.
🔹
این موضوع پس از بررسی‌های دقیق‌تر و اخذ مجوزهای لازم، ظرف روزهای آینده  به مدارس ابلاغ خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/435517" target="_blank">📅 07:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435516">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJEBOhN2WjgDoEhIa9fp_OkGdADDD7aycegVybdPO0Y6O8NnWCSAd-tCxpNXcurmq1MwEMbnk9OpFNR3GbwOFHy6dgdPvyyajHW85m-YJHHkgR8EnrVC1cwPdclkAV4rX1qJvNcICWp4_i5RdYyWb7kijt_Ic86UReJRH3GEGkHGadlQu5pbA02VFnPuJiMDZTwX8uq9SMm_4iUphlwZZiFfuCs7BRMZStSzzgrVOLj_ttj4zDlaRkgX4R0uB8eOltHN-s0Hl4hYUkNdpY_N9sRzmFQT8eH-vURdTmDaUsI5Cv9S3eROFqewG6MqPPyW9dCv-L3jtbwWH6_v9dvTSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهمیۀ سوخت کشاورزان چگونه تعیین می‌شود؟
🔹
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی: در فرآیند تعیین سهمیۀ سوخت ماشین‌آلات کشاورزی، سه شاخص اصلی سطح زیرکشت اعلامی، میزان ساعات مورد نیاز برای عملیات زراعی هر محصول و ضریب مصرف سوخت ماشین‌آلات مبنای محاسبه قرار می‌گیرد.
🔸
سهمیۀ سوخت ماشین‌آلات کشاورزی در قالب سال زراعی، از ابتدای مهر هر سال تا پایان شهریور سال بعد تعیین می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/435516" target="_blank">📅 07:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435515">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ارائه کارنامۀ دبستانی‌ها از هفتۀ سوم خرداد
🔹
درحالی که سال‌های قبل کارنامۀ دانش‌آموزان ابتدایی در نیمۀ اول خرداد داده می‌شد و بعد از آن ثبت‌نام دانش‌آموزان در مدارس انجام می‌گرفت، امسال با توجه افزایش یک هفته‌ای زمان آموزش، کارنامه هم به نیمه دوم خرداد موکول می‌شود.
🔹
به گفتۀ معاون آموزش ابتدایی آموزش‌وپرورش، بعد از ارائۀ کارنامه و بررسی بازخوردهای احتمالی خانواده‌ها، نمرۀ نهایی تا پایان خردادماه ثبت می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/435515" target="_blank">📅 06:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435514">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqxJQNUCS7VQmMjzNeUJVFYwi1QXksZF1UFG_OqOwKUMBxeJCcaEmbkJw4V3o12J9bFXWyHnuWbjKJBKDP0dvrjvIu63KE9b3rlyCrLEHJI2d1sxJst4HTuhD-wnt34opAz2cI4L7otKAo8tlGM1ziTxBFXKHc75KctGgedqhQBZAytPziP4SVtsBDsg4rhoiHQ5pqyizksuJJURY-HN7vW_k8wVuH2qRYvWw7Zp2LZqZvpnWuA_Hphp10hDVhEPcqxlGYxDL4YcqMr4qoZ7ktf-BupI3_5qAFBGeqi5610KmnheIXiYydFbM5Y4f9dyFt5q0JsQFIJ6tPnSFoi5xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح جدید دولت برای حمایت از تازه ازدواج‌ها
🔹
مدیرکل توسعۀ اجتماعی وزارت جوانان از تشکیل کانون‌های ازدواج آسان خبر داد و گفت: در این طرح که از هفتۀ ازدواج کلید می‌خورد، خدماتی نظیر تالار عقد رایگان و تسهیلات ویژۀ خرید جهیزیه از طریق کانون‌های استانی در اختیار زوج‌های جوان قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/435514" target="_blank">📅 06:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435513">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آموزش‌و‌پرورش: احتمال دایر بودن کلاس‌ها در پنج‌شنبه، جمعه ۷ و ۸ خرداد
🔹
معاون آموزش متوسطۀ آموزش‌وپرورش: اگر دبیری احساس کند نیاز به رفع اشکال برای دانش‌آموزان وجود دارد، روزهای پنج‌شنبه و جمعه ٧ و ٨ خرداد، کلاس‌ها برگزار است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/435513" target="_blank">📅 05:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435512">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4sLaXtLffcPjOgxxqxr-A4Z7RV4F5VfxrZVaBbnJclZy8taM0mtCJD19c24MatG2CjsKWI0MZRrF3sM9UM7LPAuQhumwFRjQXBVm8vM9yvFQxHbERmvgH8z8_Ry-wXuM8XoFgxVPMr2Kf1g2JO_o0FdcfSDQZXoq-5fPaxZrP4RXHY4ApKMhPawMb9lvI3x6_fj4bN9pOIp0o9VBAHrSIZjI_ax4JDnVbMn79RiMFmZMhtJAzEqCFzc9W6G74KgKEO-bfB8JBe99slzEX8nMrxA0ddwGKTQqWKFCx4RVqjyuZbR7-yn1Cc-D_sDFknAZJLqQq_L_zI-nN8lqnE6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناوگان اورژانس کشور جان می‌گیرد
🔹
معاون وزیر بهداشت: در سال جاری، ۱۰ هزار و ۵۰۰ میلیارد تومان به حوزۀ اورژانس کشور اختصاص‌یافت تا فرسودگی ناوگان و مشکلات این حوزه مرتفع شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/435512" target="_blank">📅 05:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435511">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGfnWyA3rRHMutOi1h9j78c2g2fT2OlmXDVkoiuIENDJOoYsNGpZ3WvcItNY4m2-OmoEon54L7jO2LoHT7iRJ5aOPHRGwolmHpMduhftHh8ZpUqrIz2ArrFGqOKbs-IRPAa9nM3kcTN7BryHHzeVU-jQqNlREUqQGyQrUBiJPPsJYjsbBVBS4n3oMGAm6J5wSvuhKC-_HJd9_0MCf0HrCQcPiVjemz0sac8RCeFi3bB1KWyfR2jGcYwgjoV9nWnCkvEBAuPcwBlZgRwa7XJ3NDt2AOS-XUZAN93DNin0w0aoPBU3rTBbANNkPIBN5Yq91lPUNp2hxgao34SZOx7HZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپلمات آمریکایی در واکنش به درخواست ترامپ از ایران: خنده‌آور است! ایرانی‌ها با بمب تسلیم نمی‌شوند
🔹
یک دیپلمات اسبق آمریکا که گفته می‌شود سابقۀ مذاکره با ایران را دارد درخواست ترامپ در خصوص «تسلیم ایران» را خنده‌آور توصیف کرد.
🔹
رایان کراکر، سفیر اسبق آمریکا در منطقه که مسئولیت انجام چندین دور مذاکره با ایران را در کارنامه‌اش دارد گفته، ایرانی‌ها آدم‌های به شدت سرسختی هستند و تقریباً همه‌شان سابقۀ حضور در جنگ ایران و عراق را داشته‌اند.
🔹
خنده‌دار است که کسی تصور کند می‌توان ایرانی‌ها را با بمباران به تسلیم وادار کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/435511" target="_blank">📅 04:57 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
