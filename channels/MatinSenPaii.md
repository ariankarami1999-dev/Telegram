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
<img src="https://cdn1.telesco.pe/file/saKyz1vZE3_BN26axOTIYuC6kgbJog57axlfZSc3lb15_Cp5tkmC6RgJ3D3mbiY9NkZuw3i8CiClAx_N0cuo1cAph8B4ckHQ2_CTi5PBAfCfPWPelMVy_LwUskoMeueRquGesvytGf4OgrTWw-ZE4M4qBd6hZqm2sQfOLiOd3JhrCqMMnO1uFOUuvwRIZFpdXZWp9K3sgc3b1FbhzpKIS33zf_qqZ70aJSj39j7Tfdws71edf3hfjMvE4TRCPvhZ0KBLCrGmuq-Sv-4z8fXRnu7ZvCMVu9u0i3Ni2dj9DifReMeaU19M6Itwx9kt4hVC_mXvnzEMVg5MysjBQ-m0LQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 19:04:30</div>
<hr>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QrEnYkgekLy_fukth4tJI8jPxFgRK5pkhZJMkPgatGtwvHYcSA4_n6DDYXCCEXv8hYaGc0wgTSnyglLnXfq-vwo-cELToA-64_MCn3AulXUBgDoc1j3zaMVD7fBZOn-zQHrkCIq33fQ44himPeHEh0jgo-OyBb7y2Mmla6qhmEa_rhDhpk7zDV5s3FrLS6NmXRLGC-L5e8PkSvEmfAAW4QtvYdzFkMrbTSjoTqgL210K4zyK0UvlGANUGvt_S7yJhz_6A86GmrHqn3P2Pq51zTJTmAvAuwmO9rfewaZnwXMQiBrrrpmPZ-BpODHW7x0nfXejLcGj_qF26w0GZS0nsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mKUIdFoGxzdscDgRiPbm1vuDi8wy5mQrvD8AtUG0Idqvuma7nkGOT9eXrWLeyQDfWymnJGzdbHQp47o16_lp4X3BLEnoqlgkAXfd6He_lNy1nzkKat_n_8s6VfwxrSjSPNIsI27nj1AIwX3qrI70TL7Q9_N9tQ4wedZU7XmNDGH7vSs6IrpcYK6N8XXi1iBcSJ7UqZJHY8TTGVvF5INFk1MQy6urSvEVDen4oh_a6_jajEiUTFVz5sONHUTO-ficI5fNjYZQu2sSqg_R_z8psHe9FBI2kmJAZeAhXCvlW7kZq6Ua166GHqfSmUZ-gckQ6mBoRUj3qQmJfsbT3fJLDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R9v8qr67IHzYg9ZoDNPVNZ_nclREidIpvoOxy3bwfKFxbnvznW3_olpmN-oHc--2VrwZK7QMaTq9LR6BTs6a6uRzAfQDkTwdxado6wouAOyimswTZrGsAWZD5AQx0WGz1B2_PDYSJPgL-xEih3PbTHwfNMtNz9QSZaNWsZRgBRY8hn6yApYGYQAWbw5PEkvKt3evhtkBUH6IimYlwVoLJaYxzrLtaLxQklfUe_9FhylEbU0Wr7sTn7-MA-gbMSGpLxO269IRqw8BHAwuMaHcDW9tcA-KotfYd-OfTaAE3mEFheD6Ru0QpCFZshoIg07ezK4Bgrpud3jU8DLpdSN5Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tx2cf82-2fzfGWPBxAObMFnfu4-Argvlyi-AH4dTPUP7aCpjhby4QDxgulybG8MYiBqpNOIXKI2BxA-57qLqeLYTw8qMt0PKnj7EpbPz2ORCKcc89Wa_o40i-ADoSzhqsRO1IX6nXZBqThcYLeT5cfR7U_wZ4o2I_GGNKkD-16tdxNePnJYz_MhBFcpTiSI5q0CBCoAKuSX9SnGH619ndkdoIyp9Y7U2IhAcJvo_3LsMevHDzzUnblW3suzo6T48yOBoCorMJgQzWqDrtzUWaV8DTa0qPHqvMx5Mwp_15QmdV0sG-IVCtqxHApPIIvgyllI7EAVb2-mdvNvuOQ1HpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XB-0MBnR-khzRRLYhIlNeQO3R9Hz8Ui1zC7DFzrw86MRHtsSy--_RsICGni68EmUgTx2b4XuMNNi_tqYvPp9vGvv-ETzqJS3zyRUpl5G31Yez8LipuBFgBwai6yZ1Yx4TiV95ehnUV4AuNv3g2VTn4Kcr9mJHGhZmT4-9g2wPxOnpTsr4-vnbU4_wOctKBm6OR12jlBRmCGbAdK8JATsNH4Di9BtYmZSQuLDUt5MQwjbd1UEgdrUTNCi1BZEb64J_4w1gcBT9lt25Lj1HT1Saw52sENlANyUoO9lHIOrbvOf3g8bYL_YcqLY6pgEd12-P26FDCBjDUUGV4q6HpdP-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=oujb5G3MVpSlPhSgewh-y5gTiAYxgTEq4uKhHIcpNh7V2wqHOkDgtvGUZOlMp9xYEhmGdrkD2MQJ3Swivgo7C2Yd4TM0yqPgrtO9zygBfSSm_FV7vi2-fFfdmlYsyTpGl54a8uLQb5VRES_GdE4Zvtxk0bduh28a54NHAIa6FAAAmp8hQXGmoIAyFDH_fNTJqIkDOE5ZooOl0Txy9nezkJEkemNGtS9UzgKvRVIhsnLqI2IpiA-ZqYOfTPtN3XOTDcWksz-5CB7CAUgXJsty-vRUWjIjLuKQOuqfszMfa7hFznJFgzfDY9q-HHw_26yXL0PtbvGe1bmztMgAKhVJDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=oujb5G3MVpSlPhSgewh-y5gTiAYxgTEq4uKhHIcpNh7V2wqHOkDgtvGUZOlMp9xYEhmGdrkD2MQJ3Swivgo7C2Yd4TM0yqPgrtO9zygBfSSm_FV7vi2-fFfdmlYsyTpGl54a8uLQb5VRES_GdE4Zvtxk0bduh28a54NHAIa6FAAAmp8hQXGmoIAyFDH_fNTJqIkDOE5ZooOl0Txy9nezkJEkemNGtS9UzgKvRVIhsnLqI2IpiA-ZqYOfTPtN3XOTDcWksz-5CB7CAUgXJsty-vRUWjIjLuKQOuqfszMfa7hFznJFgzfDY9q-HHw_26yXL0PtbvGe1bmztMgAKhVJDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-woGUZf8c0vYykYjYrMVSVPzPo0cpUWrrIfKxXCAVTEwxVUaJKhCcWMF174NVcxXIgXODJg0FbMGmdH3-5Zx_8O8U4FKPdShRORQtz4bD9-CHiP1EQjx0NmhRaWv0mz2XePFQPO5hhlk9KuuFq597amWesn3LyggSnh74u2CU03dXCEeakOG3CZ3usxZ3rlyY9_DYLKGaZw1s26o9O1sxn5HDYNZplydVOsXK-d7c4PZjR62lRAy2MOlfs18Chj3xXNkLOAEhZtSdvMqxBl2biZ5n8TfloA3aXEQvF4OVmwRlN2-GfHgd0-UdGVbyv-Kv8-bDo5skOQ2TRIcOThSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h4u68F0kNWso6ApHEcHBPxx9uDPrNpek3hmMGhFUUWb3PkAC7eti52ayz2UhwkcLP5Wc0yE5Afx5sG0vxIh7jYdKa0RR5XTZGMZE908i8GSGF7FQuH6Kr1I6rJZoz-BSmGCPej8EkndAm0AgvAdF2g3ULbqsPvUyE2rP5r8ApRNnyoZNqQLZXEvlio43JSLdCpo7pUjz50yz5HTImgWnDJ55D9pgtXSfqm9tRpthqRFDs9Qvnsi-kxP1Dtt8lW2bfk0HQbI_fHgxZKMUptT5GIFTqv8MeNkc7rRAXSuwewzgi1IyAr7Bxv3_0_lSh4jgrVC3lzeOezEiGz19lDW7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MC8xOqHOSfaGlLKlypNX0YUCpvsG6QabAgiHnZcQA4KnG6KJ1VLzjOuhXjUjXxAAzJmu3Do2eD8Wb6uhqDeX1pCmqjGIWsoiIzoQn1hk4aFakgFYIJHRQz--Wdb5CihbQwTelWIfTsPUma7PRxzMJlPtAfyRvvxw_r1Wj0LGLzOqmKfHZ0aR53A_YNNovnLBtOYzD_HTVvEHiyMZ69nnv85TW0a4H3IOfkdMryxmKjv_GoeHtKx3ROETvZ6SoPvta5v01CkGOAKJXwSxkA5Nbd6GCuEBrC2aYL176k3NNA9Xfx-1EN9hSN2wbOdHDcvQ9cnAh_uQ03x9a6g6R6_GMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzm77phY6L3_AKZOLXNRbsT7DhHpKLP0eyfCm9w6V1jTfltsPQMbjFXtbPD8j-bSiRPbF5OYzFrMGN4hykxoYkyKrbk3cxqWz-twajKl0lA6GHspaVGiY6kqY3vekbYFmF07y1eq3IheWNj1ys_olDGRqefJF9GvXgd73gOzwAayUMJM829eNcPRzD1vQ49hdPbbbdvSBbYvRk77rLuqOL_FWdvIBEMsHiH35N-O9b7yop9Xtzk-4mH-0r_N-8C5nT4jCkWgIM9J0cSdsXJRjBWwjW9yXPC6zVlWO5PUKRNouly7Dmnk4DJlk9i29QOnB1Zo4wMhIFRC53bzA0fO3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkP-4-P6thsgdgStcKoPOqWriOHQU7S_Pfa4q30uZw0sQKeb2PQXKV4Mt2gQd_5amRB-sLfydmWur5zMdXWLWLK_fP0W7LOfbI4JjltvzHF_bkguwYt03LXLEa90TkNcNtlHB4rTuEaMFwG93_ItmcPyTcPHAEtjq9OBE2odbELjccjBqPszuWWgD_HRy1vdugbnIVD56BxXpqyS8cv2qrKxGUElSqTQxvXDpHiPqZ5GRZrpUE6MPWXRlWAH1hU-6eqB34ao-SvBuvnrSMdpBP4fJhhDneXYbXFxjiolk_eBRegxPnOXBLJWppYf0-dtBHZttn7rwbKh2p_DYeiENQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BPGPrRbEv0uAdiWgUodCDgEcU6-JaZVtm4TzIvMqxjk_BXX2NRmo5jTsHUM6RGnU9tT67tGOJv1-ceDbECvc9TtZgnnNU76I0YoLViti-WTlAmZgui0hNocJ65QkhYpgYvyRishvqmP2qKNDA_8hE3aEHdFfaV1J5Pr5Nfh5HsX6fw923F4q_XhQpNs-MC6um0JlHGKDoMoHmoV1xbPfhp7cTHWrs1DldIYud0pJHB5agnkQyWFKj-Ro3jwOsUPh6jdm8RIO8ZQZKA0H5YqAs43AVkX6mQB1nmlXeldb_xeBeFXc8K97zLFspkyQOG8oHqVUhaFWm9H3ojvU0lywtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvxfo-qyA_QwXinBZmPSM17EzpBCGvscZTFN7k7SPQE0IawvrTL7K_oJRaUJL03lng8FB6OfFjtwbGZSrH51SwDu24lTdTUoPWb3xLMqpebELHrjYe6I903Z1IR6AgB5cVb-bkrCPqDLL8ikC6oT7DzNaIOWx_Eh3VFTUuEmoE7Y_88googsZnrZxhYCNvqId0kheHFlrvzI7VMwtvaC2AztBLO-fNtmEUAZeHSXLs0u1bO0rHv1E_mMbKaNqTqajdxCk_36Ov9WCWQHlQu_48_MUajBOLJW2Dq5hFfb8hc1W5HlxqpXQk2XnwRLqoG7RImcTCUFqaa2OryhJJ8ftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JhQ0wcZO6Cb9g05iZxaAWv9OFObhrdrSHAG-eelh0beVP-gT0lvZwoDD9afejrlDbg2aSthFR7Kq6p8_m60oav6DO1cCfxtrfc1tk_Ut5yWikmKgJt7sQFfYHtaDoa3q29Nh0F-bAT2wd8LuhAFGpG3gTL3G37q9H4oZl3cmS9OJ4ac6UQowkLuIcO1PQy2AAPpMy0qdDWVwJBqK4pj6uaf6ZE5Yn5RmxYM1kYy35rFmy2KUHddqSZ0NsTIOjBWCjCDBhSyEriJWblDJmigrPF6dt4WyacItz6PkBSI0i3UcY6XFNdysMDlKEnaiBzLQneIuG-9OspybUZl9NOQ6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=hdCddTM03QT7bzaDqZzZQ9gtyg1jAtJbmnCSZv_blFrV_Ok8JaSQ7_76QGxTgvUCIwFobOQrwZyGeSF0wrl_rtWbaCUra7ko08kd9EyLR7HwNCxIAqZ5dPk3p7rVy3U9PGnMZtJUIytF5CfSxW0fR2OSZVVfBHLqwSVkS1oDhfQ8LQqt9Frll-rgtLRWKkGK0pTgy8BMHZEfUJLN14KGATvitz9NLZK9GFnDYtX98s8XN9Vl10afQZkxCTU6CsYeWO1tm1p59-BpBLjYAfgF6Fnce854q29rPtPz-i21DEK00nZm3B2EwDFPL4uBnwnIeDe6HJgeODsCaqNQ4ronUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=hdCddTM03QT7bzaDqZzZQ9gtyg1jAtJbmnCSZv_blFrV_Ok8JaSQ7_76QGxTgvUCIwFobOQrwZyGeSF0wrl_rtWbaCUra7ko08kd9EyLR7HwNCxIAqZ5dPk3p7rVy3U9PGnMZtJUIytF5CfSxW0fR2OSZVVfBHLqwSVkS1oDhfQ8LQqt9Frll-rgtLRWKkGK0pTgy8BMHZEfUJLN14KGATvitz9NLZK9GFnDYtX98s8XN9Vl10afQZkxCTU6CsYeWO1tm1p59-BpBLjYAfgF6Fnce854q29rPtPz-i21DEK00nZm3B2EwDFPL4uBnwnIeDe6HJgeODsCaqNQ4ronUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ELEPJBsu4F1rnNRMMdqSt9ZOVDxuyUjxsB2vNl3OSOUDlcd6aAcA-D_Q6c3Iw28ZGu-B_MWbcl5E5XB6gVZMNvjOYXbZm2iyN8tMKD238G44OdDftF_qERRgr-wl5hypF00cXd74l7F54wkZNIzOWM69Up_1Gfbl1pZOXkw8pV1UqAX110GZUx2LL0DXA0JNt5Vggs5dvpTYRtrG3_wipbs3rhp_TaiV6NnU2ijD8WPUIvJEAiy80JUvefs2WkdWAYu5UKnPlNuH6beWkd_Lj98VT4IxOp51xpP9yACwF0DhpJLdhnW5Yn5-o-ohiKllFRkweT8nRmAeK764FBkeEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WEB6IyHjk5oXbJgwYEFOxUb438wivIjSGVbFrLQ16PZDRzLjx0RV2qULVb59EnXSu5JiPSBCUHxCJ4YjyYjisxwMZjcxZK3T6bJlWu3XaJrTFySeMvk4PRZvysecccPdBFnXMfyVAmSKcmpOMYan1I8HLQfkDsTtfADqVgmdpervvxSpxiRgTasRcmspiYu89FyDm6fJW5p_nSvsYZwFwRQOZC8AMRj2AZb74DspyRXc4U3ukPM5LZOfcJ38yqE0kUutR6uKkEfd53CABgCVs3nqmuc6XKjcQPkQurIAY4XCizH5CWWLQtN2L-8R8lx2USzdL-68feDV6PxSmm2U3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQhd3UjYiGyyzW3PZsAXJGvGXUPzj-D71vk_Lt33wv9HpewC17v2nn1d5cCF6DT_q_MIh1XZOrl7l6JOKgqFAZHgBicNPrnC5lEKsRBOam5_Wu2dIk1rbFjTczRVrQMCxpKIUwmVSIqyVGA9-vVlKyI_AKMhFsp7yLaTYaCTeFbz0ulyJFcRgjeaBzqAMxmXIpEtJyJHFBzOmTFCITebIb0OllqicELBDvgqGbJPyuj8t6mlfJeYB2kQVY-Jssmo5al-we2dcslt9ji95muXRfmKG6LyAPHRYh2Tu3ws8lkNW71nAqvgZDqhbDWkqmr0tWzUk2yjsjx3dR6SthO3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOnFpavr96Q6ooxC6Rj9pYSzBGS3hp9IxDsWo5kJm9zv1ZorL8PJyGQ3XzKayQIrSQomSzh_TJrC24TlkWiRtM3QDjflCb0luZrsFQo87wWmQzxZAk4JkeSkEpbdsAnHmpPtZzr6EhxPjDETdXpAyTS-bbj2IzWH7zfApodOcIOWKplCxF1yOT7TSivrVKday7GPDQRiXoc2_k0WLeKXW4xzoD9KzSFcWLdXABqfbp_uPuuyaQjKB1gz5pRCkD4_QX5fam0XIYT68noOsw99TWHVel-sGzee86D6rY0YheWoy6QxCM3ljjHIEXLgjarOeC5Sa_ba_w5gk8fvsZ7LUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FJbt7_Ibt4R0kn9w_AJpmt68s4bfSBqUpOmsNivpqM0wswdGCDbA_HcDK9MbI8ehd85MYND1_2srmeR9dt20e7iZAIAeZa5jZ-CIJViQsC2yLNXkad92CSfrv0RKt0LIwMElV2se4JiK3zF8oHK3QkZ4HZlzHnOenouBCtJQdRefPDEmyXnnZF1WMAQZy6YXqpdcm7CqYb8BnsC617QV7LPcfUOxllbdrCu5KwyPxELCafiZE25dkn_XXL_OPNbmTa2io0oWnB6TvqtheZHtDLB_4npM3UL8P_bqiAqMqko0fXnzBc5_BLzO3iBlupnuQaLwovuhv_4f37GCAEGGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nkgDXzv5-bQL_MA_kjFC8tqRWKylvw4_pKC1OlKPONxwSB9qjkKCvmvQ790ArB3QKW6ch7n9SUFbf2d9Ww3WiyLVrWhzKismOZQ5nLF-5KjIeUv_G6LNYcikzymhu05MmkO7N3Kw_B2t3hTZ9v8-3_uDqDqAtTkn-MxNd3-82-YID6DvcilfXIZSy9QMPnNyfy1bDAeqs8etvfkP0IFEzrsCaPMcFoKicFeOaHucgJ_x0APesiGGbI51t0dUCyQp8v4YODBIHhpn1ZDZKtSZgVCh2I-095WDCSV-tfIXJstGN-dOjuGK976WIL863b8sYsbr8NYTe0TfQi60SVVe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NlQFH881MEIcOSS7syBu9rB2OcyQte0j3BsKgdu_00eK6UOvEZ_J_n74VQ6DIJFqhh7vkMXn4uP4oea9GzUyEraqb12fDpFZyans-0vpppO61aPcCvSWUxJfuVRmOHIo_obZtwBmBwN_AjFkVR2wrQQu4LArE0vdfw4kqiOuFsPwDKA8KqauLvRARo8zrgrWe5rGlvX5f2Ws3fOuqpNRq1Xtvl1dXQfPtQx1mnKi8qigfrvt0P2jurHX_IJuyEUQ15T0gXK7ykNkgiy9NHDGqwbeaacAGQE_gnNlEKu63pyIJgBV1WiYXcDBc8_4mOcywGEvhBsPSnoBAw9TogYCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W-3No7AV9EKIwb6l0ruSEEpJuRuZhYNLi0caNhnTRnE_StehSHQw2pKpI-z9_ufZDjl0_MyQbnk8pmQ5N-YTm-ddFA79aVVh5WHK8WO2foGwgIXDjk7wzAevGT1GmxmwuYcguKZGzAGRqKrSAO2Bkm-IVt-1jglxTeTbMBPATR0n8gypcofqCaS-yXSPUYqzh8xMfQL8IBTbJ9nkYM6iT_pyq-GgWQS5t4hHcr9fudT-UtjAnl5qK-PTc8fM4mFRfJHNYtQrHF7M5cPGFkMr6qdCnTXOPCxl5RwimCnqCJl67K5OqmMk5BnsgEDZn4X-gynn7x1g-nygy_2dDz_oww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XEdCiKMma_AaOn_mO1s6xCB9YOdcWwrbLmtQNj291-KhjzUG9fPA6WbLctTlZ4e3z4ftByYBvpwC-ajsNObcgboBIm0SHpxUFKEY9CMqFatLUZMQc2D74_fPtrBLMaCJv2LFlEsWLGGZNmyxJhQlHDl7vFjpiacIPTejyr2MMDiRVV2AfhgHqGbceJzGC2W-yIneMle9eiU1bE-1j-uc_3qyjdqvZJ6CNsc4N__0k5EeWQMOOnyPpej-B7UstZTUN-yH0RVtMLGyIzQWxWtHVJ7QDfOBKa2j9i5KgPOAJvHnUXYEfuEXuGSpCjJepIL7YSt2haFxLV0BGXpJJny5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j4T4xJ9F0tkZjAEPFcB4YnWPtxXqPBsPgqQgxPhHk0kl7LvXE3thPxcaArxMVFoIJPvdHIv3MHzNIxf_NxNlcdKHw4SUZTCCogSv4CO7sQS0IOvLugs-YvidHZqON4cx1R2Eaq979p8bpPbNzos5VzyUdTXY2xkUuOKG-E4EItwGsVwsQmeNiv789_2jwr_oMkkhFZthFheHralQqrARef9hC5TiQXTm-H0jsSounEOUj8yCYBydw6P7iXXkGp-7HIrYoXWoABKoTmqpy5KX-BsnTtA1U0hdj9uaej_YQ3kHa4WNQrry4RuOgVzno0z6TpBsIm0MccE5kJ6_PSL0nA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EMVm_CoNXDnQjMIQwYUA0DCO7yn9LXEEXobGQBWIP1FzDXhLlpJzcwSNugVdGx-rwtF3dRJCce5lWO06TF3jOZqVF06utzXmyLlOU3Sv2IWt50HILdotUxqYGFtU6bMj-G9dHJKbf4jCYTEUyuUrjsiX-HzRGZz9VgyBy0dXRC7WzUkEdrnTlCO7rpnc5dTIegaCwcDMUHyIgQem04In1DUrrI_ueUuRBTtwABPApuSB1JKfypsA66skrbEKi3S4Y6Lz5OBzSIYZzt_0XQx_PGCq2ft_LhJeVCWgQQXnQhVhWBfURTKvoVUG9WTkClDNjvPB0s_5Ewb4UvvGi0Zu6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=ViLc4MyTbJxlT3UTpgXoSqNujKL25SZ5gA8IulHfvW9KxdT3sSbG9Sdc7ErtR2MBFvIZdeHMDdUBwWHQckXxBfNAwP5G3P-YmeciD6Dd8J-0AnFZeKxdUYnVTZT18U5trt0xfcbjU2pGsBmyHqCkG_clus4WRdwmokPhigJi1UqPMr1xw8WI1VFowTNfQCRIS5W7PirfOPteiXcS-WlgZmwBzWJDq87og0Kw3ej5rr7eY6rt4zlBIDDLUURQOIv1_To618yDqIkSFrggpyf3yydFbcHWWT66v9-2knQmSw3minNyl6ybuwZBJIpAJdQDqXM0S2LgmFl8l21ase7e-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=ViLc4MyTbJxlT3UTpgXoSqNujKL25SZ5gA8IulHfvW9KxdT3sSbG9Sdc7ErtR2MBFvIZdeHMDdUBwWHQckXxBfNAwP5G3P-YmeciD6Dd8J-0AnFZeKxdUYnVTZT18U5trt0xfcbjU2pGsBmyHqCkG_clus4WRdwmokPhigJi1UqPMr1xw8WI1VFowTNfQCRIS5W7PirfOPteiXcS-WlgZmwBzWJDq87og0Kw3ej5rr7eY6rt4zlBIDDLUURQOIv1_To618yDqIkSFrggpyf3yydFbcHWWT66v9-2knQmSw3minNyl6ybuwZBJIpAJdQDqXM0S2LgmFl8l21ase7e-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/duiIuX0C28COqQLY9Fm1d0N88tMpx8jizgTk2TUjNujwg5ePcUerLoXLCnrBXqNPI5GhsRD6LrYWYkN4T64oVuNYAkXojxbIoFfa-EjDHVWgzjE6i3fbw4ld5_QAAy9hXVX5UMr9bu9PebEXUP1gSS3H96-p2JDstaFy6rHaEZziKqNfMMethEOAINJI_Nzn9GYDmlQqFfz8Eooi2iQWZ5Pby_de_JzF7tG_EwNWExFB8bLXIztyiXUx1UQKtaoQdJ5S7c8li9mTZQsxj_7fr9gSA1FL9i8iBY9XKodVt82iAkQKxerKUKifiF5G0cDffDXgb9G7dN880GhfSdCK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8Semu4m3013oAU4QNhfLjZJZMrLJoJknR2DEzxe27EW4unwLgsFMEc-42R2DBJNnWdrPfjikjUzuS9F4vE4BchVtxLcIgr35Oj5FXhrWcQcDn2EUFv2nDujMtK1-mF9D0FkZbJFaFzVSw5kTadgV9EKJpPD26T8eBnJeEZwIH-y7h-9sW7AAsAzAQFJ00GK8NY7RijqpYI62Pok-L0KT7RwYb9Bi7Sgx2d8weu75FbSC6QvuWQDSXDxBlyohZNLVeRSZa--i2x1AWN9EGMTDMLwflIIQw3YBmcLvCyY49cGqMFX47Vw21L5FOHirkiY_ZNhhh3nBGQ0bgs7fuZgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CjJM_MkwRyfqhe3SJojkQOR2gzDIeCFQYvst3KG-Jz6YufatlmXzD4joRiMKiVJTTPY0XyEi27-FxmMAiumkjh5F-JxKirxzsEy0ZLzWInciggNTm30oFj51kq-umnCo0gjirsHEkDjzUgPPf8Y2aY_C5s4Vjtkmk3d3J1geRV5b-YoeHuiZwIEZtipao2Yo348EnHIB7okTBzFM0kaigMJkUAqkaaWdVfNOD16XQZqdMImKGDLknLFzPX65PKuMqQHpXIM-tnWabKRAHLG7tWJ13Q-QZ0Y4Y5arfT9i65vLcnd3hqrc_QNWAL6pJ9OpGb5UOmweoYgjmVivLZNt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wp29WnQXczCF-ZXekuBTWkLRWeoZUXq8hs73z-ZoBiTs2PtGSr3A9d_qFt7QnkdS9Oim4hQWetGo9iCdvWpcJ3ht_3rIbHINZ-yO9gF3lzO45w_BrYyTf1J00AOmDWnKjpBxgThRMjakAJUJCYQKXRZrx2MWDnSCp3N27CAG0kw8BfcFaaFPW0MAVHobbIU7ocgWpAhOKkjJ43eky9vdbMKQRt-rBidSS3wGOkXhYmm1IMEI_AtkHDz_OdXthKiq9DSqyruMQ3xyyInS4Nd0Ac95obPaqEt8hZSd3j7JP7F3T2oYsCiFQhD8SP303W-1kbDzqucOyoDDbHvt9gOSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ud1xtEjddE375snOcVq7sA4yFty0mVndm-Y5AyhBtpvEgRZeGkAkk4-0DJMnOQE_AiVbUUxARHcHDvH7Y3o3Gt8kWtn1BWYb0QMtIJRibgT6QJaRnGrdH3CipQUuAk_kH2yoFjkOg9xS6gAGg6ye19UofBKVHQCevQNhlTW_4aYXbzH6NKhCYKDUEe5LVqwNrWluxA1ETvDOyKUdDLdmrKTbVtvqF7BULLSjm6aQuEiHwQ5__rJjUMml2PawuPyJDnXjRJe4pMQX-vurMo8kED5i6EL_4ujYFNFTGOc3tu3W5Bc95fPPkoH_AwT7kP67L8K9X3NfSoq4RA7FcvomLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LXJQr18vwa8AapSoky3AEuxluIR2PmsZAy-0DRGGmqLO82Kv0vmOmFfnEWxteLemPeB2vM58eYNcLhUyCcdoFNLs1rIEC5wyLa3GHKCHuei-WP9IipAy2WfICmgYoUxAyjTQKsYSs-b1RXEV7nA8BM1YbA9igzbE0TgYNzfDK2ePc9v3CWNrFs4A4A7vFZ0RytIyZsk2JO_yr5G1AlnnxsWBACkS8OzoMYWd1SqrahIyLiUS92jNEQOuHIRzoBxCR9vK8w5wrLTQUevRlQ8iuiDvTuCIkIDxC2aTsTt0PoJpysKZZ-1hCV94q_4Mnnc4c-GeXc1Sy8aZB2-iew4Hrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S4Dc-oLcIYT3w9PBn6gwMIZDu9I6BRFmC8oZXhbnAJv50l1zFqWYWJwQWcR9tWlNQtbIdyNfpr1txZ3I2ZI1jpoPp-9zz7lhuyxFlyzsBokdHhvywFQ35nOs-qiQoWCyz2SPQLmHluz15Pr1YS0uD2_06zgWBKnUtYqqbTMJFuC92Z2dZVeDXIVBGf2WHcdQ2RfOVKqzhBVKZ6kxS3QneEJqnu4rnp9yw9W_TKt4aHcFnjShWl00Zk_swTA7iaUwFi7ty_kHv1muFi9KUJZ8VKiy175DEjaMVnkwTSDaDPZt6AaMACaIbkTzFDJ8pWX2wrHYYQe9QumPH4U7ZvgGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O0Ao6eW12mx-BwhBeKvM9Ql3YqeI6msdn1SwA58P0TjfmtJol38OKct_y_g9BiLLiOlEbbJ3oSPbq7du1_DTAOo-0orODf-6gJrOPrkxxTIDgdGdS20JPNK2tMuaWwvmlQVb_lmAkrZBI2KzO-6CFdTElvWsfOwoWBfNRbXRp1tIgLdwFRfOFSfoysQy900n7LfG-1Ic2Iv3VbxZZEdGJtn-7GBuARc9-HUZvuUhQ8rlxb0zgYnf22c-VyzLOV6F96Yr4_C0fTPFkH_6LD8XlEg6gIUnh3fH-ZWFbyILLvyOG1SAOquh-J1uuB1d8MjircsKbPBGiEFIe6e6pIQ9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kr9gtr4vkUf28PLrJj_7gsGQ9hUG6KvPS7s1CsHSnVt6lvweiFsSQm17Rqs21FvNh5a_ldiCQJVtWADIW_gOJK8ydudWwTOVWSjSgCswpwBfXOnigVvuf_1GO42m-xqBgq8xrK_jWmlBpB81hWwyXjUVCJWJTWqHurioDgRxXrOUEYRdmhcltaCDGIyBHckc8GC2Jt4Tz7nrD3O9ttpcM-DJBoIo9H9V6IxoXn0LjCCdcMi0mk7Og-9-MZipnfH0znFf-OFNo0kuZAGTYLJDv8lczQqdEyl_OUWDgq0HbqLR3WG1ar0wp3D-k2XrV8UrYXLx8h9LnZU-47p191St9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iV7LZ2mWS7NRTfYcOSOdgmtAKD43-DI3GOabd5LMKl9o6-1TOApf9VLXxwQ2mp7bPabZLdBJbcBUc8LMmh5zMHVtyHSYizgcg1ZAUMn9CaVxljhmh6T-NY-6UdfdzNU7xsDXTh3zi0WkMOikI5cGHfw5FxW9-SI4N_ni-hk7iul5YeM3q7wU-kNYqXNev6jfu_xz2ZhY9CBd3lHmkl8qlG2Ynlw3dgmsJK85DROkQAAt8JyIrjzLmnIBAUHzxkKFpTy73gYmTPbSfeE1lurOVJBXUo4yxpkCoR7RtpELluS-UmR_9dpUKG5lPGHM3Kdt48vCMleW5Ov3paGlfkCZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vEGheRspz45vmT8sBTbV242QDJCQTd1W_HWOKNoK9szu-PxsUmBIv0toF9oOkoqBAgVv8doSSfnKpfKGOXmkZ2mdZPMJggi7DZ61M0n7TGYK42Hw3lU0xsR4MB4pBou4XHynQrgHbRTar4uwDW5_q-x-Ya85MlJsT0CFw9uYB6UpUghUZpSMNzMyP0VmSwtg6tH8KUK-wBWbK46UdQe9hmg-9VlZAE3qaZpe4siMBoQHZGIQ-WACyTE4_6OLFtjonlH9D5hF95HJgfQlNdTrgROj7Q3v-KAnrS7hk1IrSvx8IONFAqzKxQ6oqb3X7SkF9Rd2_V1_4Una3jSiyOcNyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/od26X68AH3OFZJlMDr0xAgzwfg2WaPZywa-jLo_o5InrPvNiqZyID1pLBrqvcuTg6CLcipbMC2Fwb5Og_tSAq_uLA5vrhhoUDwGdJ8N76WEEeeQ_ts51V3hLfn1-kFd4iUG_AtjKsfn4v6Olj1959pIwdJvtP-W-tVKvoKzpgVqEbhfdJutS_IkWpol8bwvqPQ5kfGnCeO5VZsrjTU4oxUrwJpCjghn23yES14gCxW91htl9W_FpwUSLmjY-CQGXCljqVU0I_CBSGz8lairpQj4Hj3nABepERK9mYvqJ8GDbZgUFeKNVlYNVbQ5sCv6JpDcQ6TJ0zgvL3wXvotp8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FiOopNjX9c5usX1D_j6ttb0aoDx7HqhKgfaOMbgpOrA7ActNHI_ia8paI2qHCDp6b6HrfH6mK1RbAk1fLFYCYWab_L0o7UnqdGb6BzOOzPUENP6Leh4YShnMZDIQVv_HsPp0FkFwHEGKKpydA07rW8HZ5PM6zAuCiZJiRdlglEpkq0U8ZmojjYVxpmyOWdSoq5SbIKgeagoEco8M5Sg8blk65C88ZE-zJmhzPJTpd_so7pdBfiUFlhWVKQFB-pm2HZLVZWG9loHrT-K1LXLPdiJ37RoTllN2j281SgwMaS-HuO1wDwTEDDQ84avLNe-5JupQgpGs5HagXsXT_AXSvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r9mqR1HBsml1xLYoy_Q0lkxU7CwV98oE8WswuAxvlDwuoG99XTNCQizm8P5HzDoz-fM9cajLQyN8FOH-8AkpzIy77EI9-LJ9OAi1bsJ5nuzzcPPDWKLCoXaWLlQE1rVJ8WnWBvrxjxbmgK-IuWM9W8j2bHg7aqw_bOSKwbMz4wKNgqGbP1xPvHCBm0iAmbxk9c8czAXOmMOBfAaiMfHVGWt6vSO-ah1NocapoA4vWpqSkTcOLZ6znuSykZgnU3Tk9yotiJKGZPxqsfdmW50dLZcXr3gCU77xGvlutb76UknITrd2JT2Mp2U8p7tbMMUT3-lRtmiPl5E6O1hXJhdGsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s1-0qBZoMmhCs3h-9TruH1ntL5IwaozdVUIVXDrARqO5fRjOcQILj752XANEN-whwRBaDtnE7SAQmNEvsmrCXKP3wYLRl0FcKWeUgJ3hmhwzHsncl7kgfWG1P0AppKXhSvpRwPiQcFXsFufOcwSa7LJg8WpwuwHK2eNnNUqLq_6blwWSSqu9-dAj9P8oc3Gn2aIaxidY79x9qjRxyQvD50awOe2SltT7kj728RGIpZXVO48sVDPOIW2rhAO_FdxomqerXu3H7Hvpc6Q6RiduZth8rezJIffHCLJTax-fyY4mqEEYPhrhjFjeRURvHIBWSJkmkpaCKTExGqphUBXOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XDdSbYYwJ6jouMkPiAgJzPWR6Q7Jlnm70GtGN5WSjTujVoAvzD8LLNYu9GHJpMJt9ye70x4sSXPvsSSriPETTTa_spSPdooQs3JGL91viD4m9YhdY9HorwskfGGogRmcFI-oMxAU-_6cghaq47B3_hmVc2uDYR5ZK3BPzd-xXL9ACuzDsOA9C-VzCyvSYEKOdOLuaApMrZXsNmxeyXjFJnAUKnve7bX4I4hk37VZESZRG-8lyhyq7uFojb9oXEgvdDAvhNnBrA5o76Vlyqb6xtxZEGrMLf6aZAl0d3a2vUerrGh-JEYkZcSmSR_LZ_7gfCU48kiuxG9E0uT5I0OU3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PQZGBikoEcc5brtnkWXxqllk_HpjVlQzH4qyYEZ64XYRkuP58JWpot1A7kHWIGqkBjuBaZ5hANzzXfOi_tdbJDGlvdfefwjyaJ5qcpihNWaBHMJZ7FBauyCU7hrKs0FrXvS48fPYHnzhmrmV6fILKDMbVWkWELO2Yh9ubthvtX_Dufj2T8qp_vxnRjBJpL50j8Clb1eUyfyfflD75HZqhjCoielX-LoNNN3068hcht_DN9jn4cjzHqCkhr6EKo-BBrwT-QWjcqF5pmQm7IFCwvneOHr08h8-4KL2jqj45mDCBDxkx69k5A_3b-4hpYlg_vpdFGIjOeNMELiKSIgmDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sk1x369UKS2w-Pxt9Whz6SJpvsDSySNE6cdV99HZYu_8e2g4yUlUdlMCdKan5pxtUsfEnEjxKlsmvojImHEejq6egiDuybgu9qfQchTLv5kJWB_0REZ1w4M2eGsLYWC19D_J0VknSDzmgwIOcfk7VKGWzxeHmM4YjQSnUpSkB2X1bkqHk4agJPQl6RIyfVCrtZmwJ9z0OPacVEw0jZvUKv-4NBy51Z4BQB8DBFhd7-A8p91pxqTX4jE3Y0mRL5N_sgI-F5oTP2dLJGm9FKYWroLrWS0cERpF_nfDkreqA4LwGmJ9sju31dH--J7UWuT6I0b5GZwdQmMOBG5pWaFeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IAQscQQrTTUNmDCOxfOd2Cj6AMwYsb6Ig2Mn9nCrQcdFaXSIZ9P0RUPQGSveW9UPT2to_a9uRcN99lC4NMBv9B0uZbcwxnyRdxnPOTu2wtf2c4czle_ZkA3XRp20Vhv7v4L9sugTZUZ7LUojGSsR4p7ocGhRGD0K-ylREpaUEQgzbn7T2mxARCDWf52j2FjGnYy9r5bD4pPI-LVeKPQMCpaAzJkQmtk5TwADr8SBgSgqovdy9DlBhB2JJXYjun3ARgeGCwIhp8sqwLtHcOph_crqgTpH447JQMbnHvscAco-1XND65DKWbrxmccNSOBVSbCBPO9SRDhQvtn_SeUWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqy9PdrMWzC7LOcmjJX94ja83ext93KH53XzzIup7MMeGE9wjZYC62mVgccaCywD9upvbzyAf9VJeizKWCI2ekwsjuViDIniNqVAAKbW5lfwNnXnntd7RomTBaetOqQRrQBm6ZjQx4XAIb6HtmxY3vLv8jCWmLK69tdDoyIuRZkdW4XV8rnu_6IUPeAhf42uN1AAhmxYt7NjV6CMwOPZ9Wgfv5LstJCY8wHjKSjCWB59tHzLNLudIjIx7l5EkweZGTkzxSm419xAnumUG-Th7zdoCheg9n3dT8LqUWMrqSF2gDY1ohs2abOj6M0HSeZocU8JOhHv0v9CESEk28YgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGBJGOi4fefLp86W3vDGnlGzgHnQlZiINMrP-St2wMtCg6Jtg94ICrJD8qYxsn3yFWCoxYCynZnMkPUjUtkk2y_YE09NIB6cfbDeihgIP6rU6fD57hxIjmnUmy6CUuMZV9AaLzsCJukRwW0RkfNUHqIy9mF0rm7nRp1D9UyS-GCNE1b4e4ftsdpyN_LKm_xFvw24kW80xRTgJRwOvnpN0dZ367sjrPbnw1n6cSftsf8PfbpBfZ6viMY0KHdSf7dxYlTpwr8sheED7Q9E_u9J5-0gVHDidrm04th5de8GNgefe9F4Sd7iLyA_eY2QX6x49OJEHjrkl6cpouhWd7dhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n0brRbyauvpxvVePAn07VlpAkz_QPridjsxc-S_qFvaEQXlELFOWXmU1ZB6wfXFNj0DTApjfxAF5Tqj1KDcYdriSk8HBTQ4_BLCUmfKOpH4s83NsrPbwx5E7RerOSca6t1iQ_RV2gXt9OcvfmxW5_PCNkjhanEgBiwoJRL_5dnzvke0gcUtFuMhl38cL_fvvdhpmAVIj-1ZCy4YyIXeEOXmeY0Rrl4RWmujLJFuHvb8icIuHHiUFbMtnpvRbn6nqUk5LBs9rDP-ES0gqIxXWwzLfyMyNIkhX4iNXpS8TtiaDj_tnE7fS6wHKCly5OsuB4fD8ssVWpLaG_6HNXjPvEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZdVxTpjpSuQtNjNeKeJT0EXn67ESoKJfYFGwsMcqO37hDOYHme5TzJhkpa0UWTIEAoeSRXWwGeFZ3QMrmF04-BAj_7yEWFpsvoE2kcV6SMRy47NKn1ZXyEx1Xa5-sV3AfKt8V8Y62L_uN-EsIMr1qHZ2oJLaLTgnjTP6_nhI9hoSUqj71MZBN0GPMGV70cACEGSdxfk15ZBdZyjVOHKb5PPlyOisW1Nz0VigfLtzpg4iRH4fUfv3dwyMxPILVI8KoogisRSMpZb1gHP43gdAy_2domFUiIU-JODUpNXm7noX8Fpeswm7nZifhIgo05C2O6Ch0HCmKmKAhOpw-19vXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZD2LOBxAo3uaxDJDyU2ASLtfzUqo2t0CdG1uDFUJnzZ21NLxTBd_8YEAg8xCvWznYqIbupRzgGMbgNzrR8-rhEFKe6oqXrozdKIBPXX1dWlXIo_KB-JUCny-3eYMu6dBt6iCnWJGjNeoqf_LERhriPDMgdF1fS6F7brJWVaqtcM6MyHzlZdqSMmO44EOTqYEVzlfSZUnYp65voyLdUgOsmxUCJmCPLTkigWOc-qJNUE5KU3Xx8SkuCKARYbfcURjHQbD6W8zJF91g_9YvPQg9slddGHmJeU2jRvciI3J_0j77hoZnnPRj4wBZQSIVJ8AqsWM5jd3Mj30lVWL8K0O-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LqD6bii2JfoSzF4n9hG7ztnEWYYEZYu01zLScNQVRoMZErl6FIDHJ084AsJrgn0VOCfc-UKQE08c2OclImSBAgm7jbCiC3m50RTmhnd8bzTm4IiL8WCxZe35jylPp2gCqKveNr5cCeF6bvBi_OEEyjgmW2zzxakQ3kfvKvvV2svKCbgFDn99QYN7LR1vaNgIx8kRymPU-xwyzYb-iYxCl4mfKlfyX4yBCH_CKIe8A37oRigD9M_o95sZJtXQoiBXAGjFmarPBUhFDwotleqQ6SpKvvF7jQYtTC96JnsXSSI1gpdWanblWa5ETUHxZyysPmTNxjGVJpu1vjgoFSleRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_i4wmP9XN-IAvXrXaXiOFCYfafRoiVRvXt7a8XTzFmjQpaPTTGHAPchrBiWQyg8g64b2XuH5wlr_jkCNaQclrKp47bLlexX9Wp_XaacrdZWmCri6gN1jnKikuRtcJ_U1DNrWcw5PA0hLVlt6crjtOyeNOlmHW2ZsfNraPt0dDDGDRfBKrQL1J0vg8lx_5ypIfiFAEu6afkc4nIkkcn72jvEdoVbko_vAH-B47Koh0-nQ-DSLnxBCiWoXkZlFrX61CiLCRuY-gKNQbq7JmcgPFfklmrFyXWqIqzWz-9B2FYHyw5B5gfsjSIgEI9ThE0t2rAnIJ-n0N7Fblz28SFljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JSg5N_KT4DL3mL1rlbGvSthbDSgPylJmQEMpSsqriFCE8C-UGUc4c8TXSeBnra6cCCRb5IH2EH9NRGYezwQV51ttfEizsbsGnd6JHJKr1h3pB7itU9hDk5fNsvYrhdfG-4G6RmwCELfr3AvxNNgelg62d6dMWJCNgu8ewW-gLbXhOyFOUXKQfkCuHM5OVnkwpidx9kyCXhX2w1_JN2WA601SDpOGMUmSXMkskN2hQZt0M5oqBNy9v-jUlxU2sgo7_dm440zJGXODZuYNPmQBkL-srUqqUVNcj3kV4DzRGp8LLM2HLy6Q0eBxigOGSpOdPEMrd6xWv6OUJaFkT-qOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BY2_nIUhM9VHxZJmuxOof3MZ5zX4ONkf4WyEqLMZUhgEGZLdy0zy-bFpBcZB895oxovSo3lDyg8UiVCvlL5XT8HdqxwV4JIugd3cqzbc7pdQLWIDTK-_mWqxV_n35ymP563UYQ02DC5ShoK4aiZCwBSd9_HvVljcr1D-bPjUAgbBCwTKEU8vNjtqolTqzpqeyvc7TIjTSJl6hqOEdRFzS1T14Y5UudztWs10_wCB9VkUXqNGiIeGWeaezMOC8rpKRSKUkYsX76In0B7hLCRQo9bBKemLzNRcs0keSv9L9fZ93Im54irILwPH8fq8RZI-OODcQlrXwupVVEjBeeZJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b0r1ote8uGENT0xNA0qypTBvXAbdpb-Gu3OXd_OkKaibIp-FCxBWu90brmpJyFBoO9IkLqkF7ZHfL1Ct-g6zOkcmKoVOw4fJLCGpWygTcaTu8j8jYOu5EWXBcpHf-QjYQ5cHR0ACwy84xspbjd9mP3A93qtdgKIZxQLABxPAjy7eREHzAkxVEnwYZJgs7bUNPeo6LE4vorsrvSpd6czRqCCX_xa58PGvCE6_zXoYHuOxz2myOj27DvSS-VC0Z2Oc4RQAiqhALfXB1phIHJbCiD6Y9Rz0X5yp1mOPvi1QWfo2a_21K193QXaU4_EU6PXpnfwhtVCKGFAS1qbp_fe-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/URhV9bGxXzy_OPQrWQIocMaWCw4gzE2UOY4nHHP3kmjqpSMPJG8AbXWeSYMBp1Lg0gxMZ-IvHWaz1ZHe6KlauNoKBGXYi-q-Co8WjXlEEBk0d_Te-qevfn6Wacg7gHeIFhbHjWCfPP-K94rWnTNvJYE42yapnf6Q5-v4MuN67twXVYEPXamc7rnU7KavqGa7bNWIJkPQYwvnPZK0Dz8ZObU-QvMQUi7Pt4--PLqtKOWIVv6FwIhopcBqUZpMVBNe-o9ZRgTJ70aqlqxgAM-390371cjrUtrns5fDXVEFibyIMbkU8z0ac0GPBABMIoSsvzIItINNzqD1a-JXQ2my2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون
با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://aws.amazon.com/free/
میشید، و روی Create free account میزنید. بعدش سایت خودش شما رو هدایت میکنه به قسمت ثبت نام. VPN هم زیاد مهم نیست چی بزنید. من با کانفیگ‌های BPB رایگان رفتم که آموزش ساخت اون هم اینجاست:
https://www.youtube.com/watch?v=iAbYpjXyLpY
3- برای آدرس، یه آدرس فیک از سایت
https://www.fakexy.com
وارد کنید. شماره تلفن هم من گوگل ویس زدم اما نامبرلند و سایت‌های شماره مجازی، همه‌شون برای Amazon یه بخش مجزا دارن و زیاد هم نیست هزینه‌اش
4- یه ایمیل تأییدیه واستون میاد و تمام! 100 دلار کردیت رایگان میگیرید، بعدش هم با انجام دادن تسک‌های بخش Explore AWS که تصویرش رو گذاشتم، می‌تونید 5 تا 20 دلار دیگه بگیرید.
5- ممکنه محیط آمازون واستون گیج کننده باشه. نزدیک‌ترین بخش به یه VPS معمولی و راحت، توی محصولات قسمت Compute، بخش Lightsail هستش. چندتا نمونه قیمتی هم واستون گذاشتم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jbUCgR25VDWlmXg-E21mWqPTGbbc4GS1CJ9nCMI8qnv_s-EsXScCzx2RTsoxOuojRKpiIlX5V72waQJ_VzS5x7tVExPVZt8gO5mCo70B1Fk9qD3Fvka7vUetnuwVmerq39lnHGyrnf_oX7SkCYvleqnSmIeF75So1a9Tbtx00dFXqhsqwtH3WyACYd6iSIytczyfmzjfRhP8ER8aZDR9Gn9rnPgOfYoW8H5IQ-PN7HZsJyTHipYgZg43soot_Q9YjhxJs35SsL9QWfYy4-Efz8NTYH-_Fkq2kPRDLxlSqVIOUcc7YJHJA0szqUXo8MO0Xu-iAiXuZsNeM4adA1bsbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKDWUHvCTLh9ZGuIPzpKHfOzHYlaufiaMVn3KfKCo2u1SX_Wjkd64tAJDrLbvvImagKgbGJG8-YyxA7N6GaUgpus8QeZAILQOt7VsJOPW691Iyb4f2Rl6U6iZgR4Ta4VCjSw3W7MTb2eEbKbg3YnNpGGoJmd6Ih_bNE4jegQ_Xc_PFrkgIXRgRfAxkZUu7wJx6l_5miR1vJCeJ_nz_4-Fm2N9PdrK_08bOHqoYyW0-O-xW907wP4ZoBow6RgEMaA3cke-t_gl8gu8DcPzUQlStSJHqyokOGJ6PX1CcZpMgrc0hxEzf1BHyn7NLgCzXuCFE0X_c4ljcnu4DuZqSCuyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAf-IZSJMefgQXKyj3GZrRKKT6i8LHM3ZpUuZurKnu43Ys7iOxyJ1VC0Eq1-usRskzr6kwVKNXf8AzCMKEBGbYH9yMpVuU9952xUQW7NgYLT_ctq62WwfM-Ai-MLatCxb1FfHRw5Ym0T1cQ93DjFGUAXBtMVGmJmaumn4f8PC7J8bz0hBd1Ccx4k1j6QfTRc5C-M_a2iZUX21YxzNrDxrrdB7GQbjqT40Jz973FZ_y3wRpK8kLsB7ILfzz-jfu4ZmG_QMSuQM94uBHP4bUKuIjDd-zNXB3KrLxYcc1X31sElMU0BdgPIdfUDdUdD_yxJPA9Aq5ihkBc3bo0m6hQQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KfY3LsTQW56K_Bz1fMfWm0vkSo-VLd3F9pR1GdWoleO1y1Ul5mRa7Smlxp6wVajeFSpJv-LROec4rtJG3Noo6elBEZP1gDsUFUwZHC9a27RaPMjANrGK-Qa_KCVkDmpAkaS2xxvZhruS3r4qaPoOcU11t-n30FBm6Y8k7aHW9lGSk-l_rbh_XY10mHpzWU9aHf5qxhnfKGRMRtjgNj1zhLz0mjRYqGKCEap5Abt5aDk_HDnJPWVAKAd_mm3Ef4Pn9HJCatd8hm9l6s-1kax7xidE9sHeNDenDD81gMDPKL8dpXtXmEZ8A-eerE892BzLKwDNXvdNiE64gvRyZuoWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EtDYJGWUzSXjLrNwdIYTTvvfa0uJb3qD_rotsTMSuV_YrmTezGi2vo_5rcloS1SkN92JlgKwyzghDnLF9KMoqZoWC7UvUEsWk6RwiOd_5TMkbDZ1Kmk3YCtK74sbACwjvRngaHcZ1U54lGNb_WeX8SuG8ZbE-zrrP7o-HwgrDZcOi5E8AndKP8_3zWGnSyofNNmG6daS8pSUBqI4S1LzbeFcmL0gtwCbkZpqQ5d3NosPimxqis_wK5PB2RX12p1lfSx2QZGmrc18YQgWjANBqQobUO2N9saBf_9OYiDSg_fFWIuhytp8HgPbqXJJYnrHwpnaM3F1qcBT_i-TVcA7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zgp2UF166taqWurhN4ebDDwz_qSMjB4iUZRoJ3I41pUzQcHP55L5gbzJxrccm7ozyvndrLUjGcsD24o1IizsA7Yva7MMopcL2C_TG6l7DUxrk9a95XRQaIEtDRGFl8JTR4NC1os4CTb9k5s4YkHs_ESAcFjK6eg3aCT6r2vnApp-zgNDh9YhS3UBNKAQ-0hz8cGd4GV7qUEFrxZJw8PTQtRaNZa7GWJOMAC0Z7R2OXFb8Hg98YVNJGB2NrpWFvBj1M1yW7Lr0ZNlyG-gcIyoTblPJrOuy5ew6erEKOJ86Xjya4Kppg-tzW6HZ5kLZHLOMonRH4mHb6a6721vqrrhbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OMOOE5oRrMqMXm-X9kBVCjfx8rK4joxgTJ5EguoTWscmZPDsgmv441wtWlvx9Bj58OQLjj3KHIZryksPZ8mi2GmpNaedfP8zZ7pGFPWkG5R_pN4RUa2kwhpWQyjgOZVmsN5s4nwiG8pn2HzOrXEDBYXkhv3S06tRNQ5yeBYPitaztrUIxtYrNkZiF2QziRD2O-dhm4VygH0-0QQQrOYlsQnITkihF3p67IfVa0uV_jSLrTEL3uodaRmMXUQSI1QLnXnB2dJbQzjoaMZ0BmUwScKjTrk2kVvTAJO6v2I-1ynizk7q-okrnMp5Gw31LRKLxlXj2XMGZMSukGkaB625Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vUDYIKqkTFFYxFKqc2kT1LKDtSCM-BZs1EVFzis9hPzkvaSLSS9GsVWha_dE9pOh7yw1yJONUzWxkTQufgfbE7UqtgI6XyPfSpPERbA3TmguqxzmVZosGVjG6uf0oZzoj3FF4RY1gofYzb9r-zWIriT5rXr7iBCzkCAU1CKpuPHnPq0QxDEMgKW6FngUP1ouXuW_xZD1cx3ZltfbJGiDr9wDNOcGViP_kfnBqF9OUiVqrqfEqY5hwHfTihwef_UpobgPFafE94Hi0kS53P_oAGGpqSLTSeyu3BlGXWpKW0eYc75uJ0D1qXfyqOAr8AHHJ4h23p68LTrEZIMOuguSjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDGksT_LtbHj0FdMj60APAt2ASS4epWG110bqZGzo6rsQBBw-67379l6c97fa3fLM2MPti3Pc2p8Oj6VPVvHF9NwNJYYdPkJzc5z64hSxvkdkfuDXPdaDz_NKaeYlEHMve5ohOo3bbvbsnF0sWHl_KIYnSmIOTzccoiDUDMG43EhVKKyXFvEDSeqiDO-9YzWtu9OylOpkXAfdS3qpLQTpY5xWj32ap0JHeYuoSqhTTz60UMA4WNicL4Wd4Rr_u-dQ5_Odw7pMWC4GLCDC-pPNDBvSB_1ikOvgNAq4z45hrWCBjTkSjN8ZA29vd3pubPkmUNR1ItNLBOoobpYtMu5_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d5r0V6BzdZWBrfs48uwom4_XBl__QIKc3b0-ALA_zbNXsxi8hzScKacGpf83Y_FNXxecqVZhGN2lG8GMmAsSauNXvQ5VAfeLSw5SH5lVqzgTA3WzJdQE0r-wIZTiO4z-qUOVON2MgSAD9NYgyrwg0KZFXzGipm_U7c7ZDvKKYyU1a0xNt65XttOC8nUSOo5wnfH0gfjMUSWKwgzmiVrj8Q2uVr2hRIBfB4hf8dlphw8mUGsuv5oUAzDJyvaVYmwApg2P1gZtW6gPq8AIjgQUzpVsgzKSXMz5t-znYB8G_sJ1g3raG9FGR6K8aQRR6o1o_LgmQL44dcKal3yN_8PdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VehnMv7SVcTqZX4D1nswBRy017kGO6Z3OuJaFXFpQYmFYZRD89sq0AuPb-enKhIy6lJLKkTaQTBrBzNhqDaD3chDCLKdorIFO3x_u1imizDvvWxiDMZdYkRtSjidwy9_ROFatsc90JDZInxuBOYNUK9CTdztE7Yge0WvTXtBfPzxbAeN2KR6RI8C2aVziCa1D5MQwBG1DC41ZGiRezcCzVJbMBlkfvpmkMHO-wLGv_4xuMKNUtjX0ZmtwTdZ-iIQyji__zuUzuCkFbrKwNoVGsBBRDhzn2xSjWOWQ7zgFhf_UNJtZx4ETpihO3gc7OYisodHR9t7m_vuf2UCsuKszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
