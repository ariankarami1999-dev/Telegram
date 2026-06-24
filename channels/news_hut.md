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
<img src="https://cdn4.telesco.pe/file/h3vM_fUKgUKpaYxbpR4uK3RHcnHD6gfZFd0MdUIGVbVKyiPCU1QOIJlRPfwDa3Cl7pSzNGw7e4-PTuGx6moAxfaKLlhxqipOaMScn6vU6ci-B_ievdr3zyha1HTl3bVWxaEUB7Vi_Nk_2G7z4YtzgvvfDPpuOYAdio9ff4uhIxYUGszKBNcB2nDbOhNzhnzdfZCocpZCenho0Qyo6We8gONAvMo2IXwbRopfcQK7MOr1CCTLD1xAZSKwKK9wLOeo2LevY_38PzUKankYA9mZpkigkaf_MqpWTxfwT46w7HCx32jfqMA8h06ZtwTCe6xal9Qy00a5E_8ypvGCStsQzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 18:45:45</div>
<hr>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=LflIxP9SAN2TSeGk7J6vF0l9u_TrOKhEt8RJfIw1CMQOepXEn9Esq9zjBI7yUAgtoHJ7ls9Ne0y70HMsXQZw-on8iWDxLDDsBQpTmnKIkHrNXTlgRCTU9qYnoDb8P4fQLx9ivbDzIGYr9oS_ACXso9aM-FGvx2-rLHOLR1uNEWM2gjwOLPFwQDI6oyMtTfuukZKIgSxQGfEcTLCuspaIj-pTh6G4haRBHLi1aghpPhXCyBL00GMTJPCAK2NT3nBTtEmkPj0MLa3qBFYXEPsb8XpgGAGyB3DOstVlEaoylf2r-EvRGhS6f7W0umt8vfYlFMTy7dxfu9c-lXLefxdC9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=LflIxP9SAN2TSeGk7J6vF0l9u_TrOKhEt8RJfIw1CMQOepXEn9Esq9zjBI7yUAgtoHJ7ls9Ne0y70HMsXQZw-on8iWDxLDDsBQpTmnKIkHrNXTlgRCTU9qYnoDb8P4fQLx9ivbDzIGYr9oS_ACXso9aM-FGvx2-rLHOLR1uNEWM2gjwOLPFwQDI6oyMtTfuukZKIgSxQGfEcTLCuspaIj-pTh6G4haRBHLi1aghpPhXCyBL00GMTJPCAK2NT3nBTtEmkPj0MLa3qBFYXEPsb8XpgGAGyB3DOstVlEaoylf2r-EvRGhS6f7W0umt8vfYlFMTy7dxfu9c-lXLefxdC9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 499 · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Vqz7GmxMfop6bm6xnw73n3I_kfbOzAn5xD0f_707IbkwPxMIz9hWWl49MW-vUuW0cRBon3AOJzvBuzBVYnhMkw-icEg6WazeSBxabkoonexAgk1aLAeswh5BE10-0slunEQpfZe3QpafxMG5uMUpT_e5RlQ1r7bz4n2JrmOTpF3kMEVhNWpk1ZY8gvx6dRgXTHlIJ6urll-CQk1jiE-QJhwvGc5egN8VlTKYeASXrI522CJgN2B92GDGERaZbTwh6-3EA22aF0MeqrIuoQJl8sWix8clhnsSdB8kTHmb_ksaw7IHuMQ0eiL-stx9919oy8ZQJHulIoOkgTNLgf0d5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Vqz7GmxMfop6bm6xnw73n3I_kfbOzAn5xD0f_707IbkwPxMIz9hWWl49MW-vUuW0cRBon3AOJzvBuzBVYnhMkw-icEg6WazeSBxabkoonexAgk1aLAeswh5BE10-0slunEQpfZe3QpafxMG5uMUpT_e5RlQ1r7bz4n2JrmOTpF3kMEVhNWpk1ZY8gvx6dRgXTHlIJ6urll-CQk1jiE-QJhwvGc5egN8VlTKYeASXrI522CJgN2B92GDGERaZbTwh6-3EA22aF0MeqrIuoQJl8sWix8clhnsSdB8kTHmb_ksaw7IHuMQ0eiL-stx9919oy8ZQJHulIoOkgTNLgf0d5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 928 · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=faMJHgXKGAIzOj1nP3DUmbjvEFKwlkhmF489_4zgeibM0bsx0GNmrQa86UkBGxNr9iQyPc8c4YznEvR0bESs2-SOGms7IWAuQtkhNGXme_BWXz9MwEhoXjIBN3IKAzHZE31WkOwJVukzPruOQwXeBlIKJrIbgfIdQjs3u0e-sdtZxOY7vl_3fnRS_BXcbb1E6hmdUIAHOQgRRz_be6SSK6T8MaAqbZkiXwDo5yXLPEEmtbHV5tVValvOHhyWqwP0FPFHG25TAmKRqvl50_Uap6O0RSiqvD5W41EAeO-id1XS-gkqsxS78PudNMmXttH0ih68LADcZEvSWOdMgv9z0q5Lgxu_M2KQMYYT0IWfABcjgdbS6iEH59hHlWz3DrRknZ07Ly_rRSUegFglCiAyueJ4plHoNBUddy1hj2HQ3MZOeGZlWysI5CjpMXkokkBp-gsJ0lm_fiwJOHVUIgQO99FnApZA6t4ULtZgzVUox9AE1BeWIgfRGbXz-yImqWVY8g93oRFUR_SA3C77m0iDDk_zEsQ_yBIg25V6y3npspGwRNYMukizgdx8gM0VkYUeo34ijLkIM2O3ktjhiWywvem5lpLSdAOeMyVHXE-wA2ttHplxwnEsCESbP1_iyIQ9tmc7PiaYMe_vNQaQkBJkHwze-iuUS5WIW45nsPwuKUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=faMJHgXKGAIzOj1nP3DUmbjvEFKwlkhmF489_4zgeibM0bsx0GNmrQa86UkBGxNr9iQyPc8c4YznEvR0bESs2-SOGms7IWAuQtkhNGXme_BWXz9MwEhoXjIBN3IKAzHZE31WkOwJVukzPruOQwXeBlIKJrIbgfIdQjs3u0e-sdtZxOY7vl_3fnRS_BXcbb1E6hmdUIAHOQgRRz_be6SSK6T8MaAqbZkiXwDo5yXLPEEmtbHV5tVValvOHhyWqwP0FPFHG25TAmKRqvl50_Uap6O0RSiqvD5W41EAeO-id1XS-gkqsxS78PudNMmXttH0ih68LADcZEvSWOdMgv9z0q5Lgxu_M2KQMYYT0IWfABcjgdbS6iEH59hHlWz3DrRknZ07Ly_rRSUegFglCiAyueJ4plHoNBUddy1hj2HQ3MZOeGZlWysI5CjpMXkokkBp-gsJ0lm_fiwJOHVUIgQO99FnApZA6t4ULtZgzVUox9AE1BeWIgfRGbXz-yImqWVY8g93oRFUR_SA3C77m0iDDk_zEsQ_yBIg25V6y3npspGwRNYMukizgdx8gM0VkYUeo34ijLkIM2O3ktjhiWywvem5lpLSdAOeMyVHXE-wA2ttHplxwnEsCESbP1_iyIQ9tmc7PiaYMe_vNQaQkBJkHwze-iuUS5WIW45nsPwuKUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 898 · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caCvNyyKFqsy76GYzl04zVFmewxcsaej-Bg7Incf45UhzepV-Riz2cAHXpQALWmg7sGeH8DnZbzztcAPlKLWEyB56RDO6uo6OndGVhpHe75kbf0aGiaGd9eLoHhIgjdy3pQZdarP8NUHydkQKqoPR_mEXkGWWG3CqJWaXmSi4Tv6umqsEqZq8JicmxTGTvJhXUAAE-FhRn4tNyE6WxljnVSDSXy0mqMN7mrZqNCqGofxzyUQAsi82iLATCZ0Z8rZfFWDL1HD4kWWQoFaMacymgJeNwiLFYbcMAao6maDcX7e-A9TzUs3701dSpir1g-hcfx74ILCr-_daOb4vc_pTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=utVNQ4sY6eiF4SWrWWcFkjjLsWXhCNtxL-qy5-O9B9V_CEFxf9o16bCo93pvR_Co96qGtLSwWw6HfkGNCVpVNuLq3ZE2N_v7Sjer_6M3imWjtFhM4r2RBYr_eO8FkNXoi2FLfq4sOTWIuhFIbMOnL8iOA5YtySUWupt7q-3zRmasziRnQq4zUDspVHy7keIsXWUh4n8Msx6u6e3sdNh5fGiTl7Yx13NbFF5akawRosds5c-OkrjeQpt2Qb7P2JqIhkgGoL-j45OajYtr6CUP1ylM6DYHJhAqbuUVSZdJ0OxqfrT3LotKVOCYOrPt3WA4o5uqTrcc1GNbP1mfcJEHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=utVNQ4sY6eiF4SWrWWcFkjjLsWXhCNtxL-qy5-O9B9V_CEFxf9o16bCo93pvR_Co96qGtLSwWw6HfkGNCVpVNuLq3ZE2N_v7Sjer_6M3imWjtFhM4r2RBYr_eO8FkNXoi2FLfq4sOTWIuhFIbMOnL8iOA5YtySUWupt7q-3zRmasziRnQq4zUDspVHy7keIsXWUh4n8Msx6u6e3sdNh5fGiTl7Yx13NbFF5akawRosds5c-OkrjeQpt2Qb7P2JqIhkgGoL-j45OajYtr6CUP1ylM6DYHJhAqbuUVSZdJ0OxqfrT3LotKVOCYOrPt3WA4o5uqTrcc1GNbP1mfcJEHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=fQ1iwztyKWkzZoNox81DEwlIgJaY8aUZtfGxrR_Ul_BkEzLC5HNqb2dnwAPpWxPxyc-dnjUIJkQoEng7D_xnBrSSGItZR2s_eCg_G27JY6Qcdno2RglY0iZJQwpuW3GHJpfX5AJ6lYlWCDN9Ih1zgFY7U3k6eU7ea1ag96YGf6VucjRLgTvbeXdScQ5zlGepl52tIYyyiE7YP6WHF3bEonapHnUlh6iedNXGNoNhptM4_FtD7kFZ9VfZoVqJVTnAfoL9JYZB_ELiIXrRMih6KAWA9XwDU52vV1SvxIE6iivaVIrmYiM6TYa6YsyPimZeWjO6Nw_O66bvy34ssV0TVoNUstuInkQlo5YrzNUncCd_qHSjnLLQP8zM563lpR1K4UnbBkEbOfBI9-OV2ZCT6Fjng85veu60KLmcfp2DNGUV2rhXXZfWVFu5UgUwbBpoXxqHFq6eTCgwMyJyIPj25sMaF3fn3jEXniUyvF0nr8sAU1SLBdbi5r4z_j0r904yUdr5zgghZ14IkXJox4y6MTGMfd0japz5FWY-X_Da9ZPv6Yrvimj99C0j_xTu2CcBJRPvjw-D-TsUoUvCHl3eocefYgyorBvJOuh8VwinQq1Aq-hgN4TF823v3EylL8kQ2zG4IXTsKotFMGLQTpUAqvlja6uCkmKP3EBIXf5d2ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=fQ1iwztyKWkzZoNox81DEwlIgJaY8aUZtfGxrR_Ul_BkEzLC5HNqb2dnwAPpWxPxyc-dnjUIJkQoEng7D_xnBrSSGItZR2s_eCg_G27JY6Qcdno2RglY0iZJQwpuW3GHJpfX5AJ6lYlWCDN9Ih1zgFY7U3k6eU7ea1ag96YGf6VucjRLgTvbeXdScQ5zlGepl52tIYyyiE7YP6WHF3bEonapHnUlh6iedNXGNoNhptM4_FtD7kFZ9VfZoVqJVTnAfoL9JYZB_ELiIXrRMih6KAWA9XwDU52vV1SvxIE6iivaVIrmYiM6TYa6YsyPimZeWjO6Nw_O66bvy34ssV0TVoNUstuInkQlo5YrzNUncCd_qHSjnLLQP8zM563lpR1K4UnbBkEbOfBI9-OV2ZCT6Fjng85veu60KLmcfp2DNGUV2rhXXZfWVFu5UgUwbBpoXxqHFq6eTCgwMyJyIPj25sMaF3fn3jEXniUyvF0nr8sAU1SLBdbi5r4z_j0r904yUdr5zgghZ14IkXJox4y6MTGMfd0japz5FWY-X_Da9ZPv6Yrvimj99C0j_xTu2CcBJRPvjw-D-TsUoUvCHl3eocefYgyorBvJOuh8VwinQq1Aq-hgN4TF823v3EylL8kQ2zG4IXTsKotFMGLQTpUAqvlja6uCkmKP3EBIXf5d2ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=io1bu-xR-vR69_ij_TpOB6aWN2dnKgBW4i1SO27ArLLRvoH8kuXyDclIUWFwEFGHQq71kV-6WzBJxCanuIQ1BpeoDK5GhfXet0m5xenHxLCNluxm4HMyo-s_LpSVit3hFH7wmBgbMs_o3iF1XBnuDo2OzYz1kHrtRLQ8OAYvuXN1aMTm4Wku6ZiEvykdPDAAUMXYoc4-BMn5issHoBPa0gEoPc2LUllLb33tSNkmKaf-8ytx30xpuPQn0agx_ZbuVEU-Jq_Du9JLBK_5esqHdrLTc_qrUErjxJfIszaiiuX0t9zf6sSCN4NVQ2hWE-bRk0Lyy5JsI1XAwdGWXn05LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=io1bu-xR-vR69_ij_TpOB6aWN2dnKgBW4i1SO27ArLLRvoH8kuXyDclIUWFwEFGHQq71kV-6WzBJxCanuIQ1BpeoDK5GhfXet0m5xenHxLCNluxm4HMyo-s_LpSVit3hFH7wmBgbMs_o3iF1XBnuDo2OzYz1kHrtRLQ8OAYvuXN1aMTm4Wku6ZiEvykdPDAAUMXYoc4-BMn5issHoBPa0gEoPc2LUllLb33tSNkmKaf-8ytx30xpuPQn0agx_ZbuVEU-Jq_Du9JLBK_5esqHdrLTc_qrUErjxJfIszaiiuX0t9zf6sSCN4NVQ2hWE-bRk0Lyy5JsI1XAwdGWXn05LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=MqH8d-7tv6easOV-eHfl9ljVqsX9htBQAhDAGYjSwrX2RlZxNq4FQkPaZOP9oSty5CPoWvoxuRX4oZSj_cS0HB3GV-2oYMJyvsdVGCuRCL8o8NZjZjb9l7a-OfcNKjzhdzy3bTR5Iu41S89YoThuFW9g3Cl0-YrymQB6b4emc0GFtXKJuGb66M0GMQw8si0K4l-OYSHkYTSLw3VveJCxwLMkzJ_WvlBqBId45hCxccPQrm4sJIlT6HHL_G2SA_PcKz6WTKJ49bHNzsVPqyG4Gi6Fp5m1wdd4KZIS-WkdcACZToU4FEMhVbYDJ6pGkTtyBCYlRd_O4AzU17-rdTyDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=MqH8d-7tv6easOV-eHfl9ljVqsX9htBQAhDAGYjSwrX2RlZxNq4FQkPaZOP9oSty5CPoWvoxuRX4oZSj_cS0HB3GV-2oYMJyvsdVGCuRCL8o8NZjZjb9l7a-OfcNKjzhdzy3bTR5Iu41S89YoThuFW9g3Cl0-YrymQB6b4emc0GFtXKJuGb66M0GMQw8si0K4l-OYSHkYTSLw3VveJCxwLMkzJ_WvlBqBId45hCxccPQrm4sJIlT6HHL_G2SA_PcKz6WTKJ49bHNzsVPqyG4Gi6Fp5m1wdd4KZIS-WkdcACZToU4FEMhVbYDJ6pGkTtyBCYlRd_O4AzU17-rdTyDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=c7sCowRcMexMYFRQMA9VOTvqyrNBvs817Tui2mzDrvx6LEbhlzlki3ODGlMPYieMyie-9qkNJJ_t9HwZnY7yaGPLxKzOAmBlsFA4vBHWs1JVgt1fpPZ46RZdQKINAY79vmU2dl6j8pfXLL8Ku8h7lxmU2GhzdnM_Jm5qvNESBDmpgcTG1wT8jYdjc05zg-8T_5To-JLgDYtsVzVaZqxOdTdPKSsDY_gmDvj4KxbLrUZZ5dCvz7ONqN-0uPtuztYdS7P0SRJUMN_QTsdzk0INlbsL1Tm1i0p-mNGQPSR0LlbIj5H_bjwXY0hGG3q84lGacq1HmH4sJWtfTfBWb9TbZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=c7sCowRcMexMYFRQMA9VOTvqyrNBvs817Tui2mzDrvx6LEbhlzlki3ODGlMPYieMyie-9qkNJJ_t9HwZnY7yaGPLxKzOAmBlsFA4vBHWs1JVgt1fpPZ46RZdQKINAY79vmU2dl6j8pfXLL8Ku8h7lxmU2GhzdnM_Jm5qvNESBDmpgcTG1wT8jYdjc05zg-8T_5To-JLgDYtsVzVaZqxOdTdPKSsDY_gmDvj4KxbLrUZZ5dCvz7ONqN-0uPtuztYdS7P0SRJUMN_QTsdzk0INlbsL1Tm1i0p-mNGQPSR0LlbIj5H_bjwXY0hGG3q84lGacq1HmH4sJWtfTfBWb9TbZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do2hMvulqIdUaDQY9EXOPIqMEvqmk_yHohOAjHYmeYR2lxk7NU-QWWJtMKK4wrHR7r-9ooiehceB3NlTsvsdvjjqtDZk0o54OdbtK0j3s3BkxevdnWnYB8khkMjWpv66P_3Eq1jr6mscPdTTdnthScLZ5qf2R1gm91UJ5GNRKBAY7WrFbVqaMu3BdEsSX2eAgOKktEWYuzvAbuxAKLg7v1ZS9ZjZ9pA3pwASsoHMsPpqsVyvdx0DZ3A4Zrsoelrww8xzBzzUxE_YH2RxvUs429vPp4OTGkUH7j8qmjdTSYUmWSGzRXuYexV3j_uKKi9VUGTVpNcPoVxIH3xMLe0rnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcTN8lp9HAn4rgKtG_kdqimJETHVUzWGje00fVLmwunaek8yMPZinYpqBlzqydPJqXJ9uc3KZP5GihvyAlCLZF2nl6iV5YZ_mNm7nIkLHyRdePfXA0S7A6K5lC08Xk0klgwTl8AA03b6HJGbFKgUuQODcicrepMmsmBLhlMAT-vdBHzXspnKGJaNi2bp03oy7N4a1UQ8aUYV6Qg9o8q0pnyBysP4YLj4fbtLEXPB-CWtH-3FaRgEPQ021T_eMdO3d64WitWuVmqHLF7SYVLxTZ1pxwmZERY1Y_P0J_DEFd_BhE2IVIP63sT519-a2xPnTm3goNRmUD_eWOBZ-g9iyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=bU8RsgVogYP5B4mbAEsTS61OjAyE2W4dy59AFRuBap8U9illNdrszGBBRx_QkEdIqVuKKfq1jDKfiea7mqJCH2XKcLHf2694lKLnwNFKc2usNDFq-fzCrwixSD7VIXHIRwQH5j-5l8OwMjWGaCOidaqfxTa4P37pDrfvl3g2La7KvEt9SjwXA5tZWyBX8iWhz0yK5R9clvVOj53fVRyo4vBVb8eaiZgF-EM28LU4m_5df9N9G1MsG5Ye8kKxg6VTLBLByD_tlZCKucPQWYsZQclMwrRd4hTaK1Zi5z5T2GsHfkTfunPJWXKhFbZPYcBkXfCIzEL33Cc0VgmDp2r13g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=bU8RsgVogYP5B4mbAEsTS61OjAyE2W4dy59AFRuBap8U9illNdrszGBBRx_QkEdIqVuKKfq1jDKfiea7mqJCH2XKcLHf2694lKLnwNFKc2usNDFq-fzCrwixSD7VIXHIRwQH5j-5l8OwMjWGaCOidaqfxTa4P37pDrfvl3g2La7KvEt9SjwXA5tZWyBX8iWhz0yK5R9clvVOj53fVRyo4vBVb8eaiZgF-EM28LU4m_5df9N9G1MsG5Ye8kKxg6VTLBLByD_tlZCKucPQWYsZQclMwrRd4hTaK1Zi5z5T2GsHfkTfunPJWXKhFbZPYcBkXfCIzEL33Cc0VgmDp2r13g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b87jU_tvcpJZwuIr-YWhNCARNzjCraLgy6mhFH5FtDG8msJ8YbT5B8qp784Vmn9PCQ69g5CMhZL3My1HISAb7y9N19IDeZJulzN4rqCNWrjU5-e4JrDZhQwg_nECpgz9cdAGFsXqiRHfr2tyNOR1ns4ZDyO7Wqeg_0mIlZQDPSqnnxo9zXRsdURujx91DWYUPnC56AkP2NPJ3pUEEcHMeXaN89aWHD1qzuCMZMC_TGDyd0_nZYchi9p4Fg6PLoWzdlJYvqecC-fbqsHF5eNyhcDw2-uL4ywKquYtfBwlWp_wqJ4qfFpkgaBP-QAa8bcXoF94vnd9cquyhfQ35orUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BB0_aFOvEXcgPpEDamGZv-L_bvw6gxvJT62vvg9oLbEBss9qoMn-Tm3UgrJXNbmK2H_N4lRgfgd7aVZaJlaay6cn5kHo0c-4b4YUfLElBfIRQSgyxWwYh-_lVPOJfBh1yh2os4Qc1vUKVX2KUbDdZ994rlLRA1mANm97s8xlQY5lI-wY6lwOn6b9bqQ0GeDm9HhzwQUSWOVYHEUo9IWbrMQDfLbCQvozf9aljMjqYtl-pQ_Ymsq9-HHVSQciTYKeVxjP3uioKfLcNaqZPKJ9ZHVo5pfAU5t8tItlvbZ96c-X8dwvIKvdS3_2hv_OrtJhWWSMKjN7ab0KhTRyxS2QSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BB0_aFOvEXcgPpEDamGZv-L_bvw6gxvJT62vvg9oLbEBss9qoMn-Tm3UgrJXNbmK2H_N4lRgfgd7aVZaJlaay6cn5kHo0c-4b4YUfLElBfIRQSgyxWwYh-_lVPOJfBh1yh2os4Qc1vUKVX2KUbDdZ994rlLRA1mANm97s8xlQY5lI-wY6lwOn6b9bqQ0GeDm9HhzwQUSWOVYHEUo9IWbrMQDfLbCQvozf9aljMjqYtl-pQ_Ymsq9-HHVSQciTYKeVxjP3uioKfLcNaqZPKJ9ZHVo5pfAU5t8tItlvbZ96c-X8dwvIKvdS3_2hv_OrtJhWWSMKjN7ab0KhTRyxS2QSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=vagVfZ3GSjo2VhGwbX4vgMkw6MwjNjB6oK-EeSCmMrU3tygpzvid417b5Fyno0ZN0A7QWlgIQRvHcXqT-RTswoM6bMEltCkKc5AMwyF9QnRKwWoTBhMj9eGl50JnlY8APzNLs7oQ0lJpqEy4TkKGhiDnRhSorpgr6B8jgl3vNmjKs4paERJJ-7ZBV3tnsEe93mYaWI5VHmLHuEqxJsLLIc8fduSVUAEyaK_qHJnBAlYXKBjstzVmSkz0DY8fX18XkPuKkiYG19Am6Dy1b0risNbRMTVnL3Z9pcBJVI6HeC4J6PhUvQOXKGsxLoaYhJQM80i2Nh1NFcVY5JPp4-sYPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=vagVfZ3GSjo2VhGwbX4vgMkw6MwjNjB6oK-EeSCmMrU3tygpzvid417b5Fyno0ZN0A7QWlgIQRvHcXqT-RTswoM6bMEltCkKc5AMwyF9QnRKwWoTBhMj9eGl50JnlY8APzNLs7oQ0lJpqEy4TkKGhiDnRhSorpgr6B8jgl3vNmjKs4paERJJ-7ZBV3tnsEe93mYaWI5VHmLHuEqxJsLLIc8fduSVUAEyaK_qHJnBAlYXKBjstzVmSkz0DY8fX18XkPuKkiYG19Am6Dy1b0risNbRMTVnL3Z9pcBJVI6HeC4J6PhUvQOXKGsxLoaYhJQM80i2Nh1NFcVY5JPp4-sYPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=BHx6sl5oO_9B-kGBzq0g0mlVSRZxdgwKmdM8bR0_ItY3ZBCM7CyOY43BAOZN4Icod_XigW36FgV1sfeh5_XV4FLj3oYpviPV883cTZwy48eFc1cGgVoShjj9Mjzci8Drn9naEjjbe1L6qzgNmTW3NQB3WW4e8D1CVDT0pcWUs7g5FW0Lu4M6T3qt8zRpOk_hutVUMs_5l2wXsCQWNyOiO_g_WnY80w_5nxq114XtZXFA_ZfFXfWRNkrzsf5VPdl4DPM_hac8EWGWWdjtw68pgvkxFPNc1cBDMQNXeXwKKTYt4qYir5nuGKDYJnEMsXwiMI4siwiBlYGls_TimvB9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=BHx6sl5oO_9B-kGBzq0g0mlVSRZxdgwKmdM8bR0_ItY3ZBCM7CyOY43BAOZN4Icod_XigW36FgV1sfeh5_XV4FLj3oYpviPV883cTZwy48eFc1cGgVoShjj9Mjzci8Drn9naEjjbe1L6qzgNmTW3NQB3WW4e8D1CVDT0pcWUs7g5FW0Lu4M6T3qt8zRpOk_hutVUMs_5l2wXsCQWNyOiO_g_WnY80w_5nxq114XtZXFA_ZfFXfWRNkrzsf5VPdl4DPM_hac8EWGWWdjtw68pgvkxFPNc1cBDMQNXeXwKKTYt4qYir5nuGKDYJnEMsXwiMI4siwiBlYGls_TimvB9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=FAyhCZgI98A6aq0Rb4gj1eWqS9pmjou_GmbrI8Oq29wd5OKMxkyCUzovnjRlniRE56w1HOXR9icSK2N1SgToT2G24yeNhbVhkzzr0Wccvrg7EjzIQmFI3VmdX3FGmEJh2L3we_MUuMPLpnU0kWPqMZ-00VzwoOkcsRfZILMNG9SH_04wFv7zpT4nAjlCtEc-Lqe5N8ynGkHNH9WiD7Oyi-uLKbJxwOznG7YFp2t5V1Aw8nsWy7ZJnNVNvzXbTYUHdbGzyKsX_XaBany2BDgZk2sb4dK8fRbi2ix2Sj8GemHSHDbGnjg87SphiIzUesHCyWi-jTZUvWi44GbJtcoruA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=FAyhCZgI98A6aq0Rb4gj1eWqS9pmjou_GmbrI8Oq29wd5OKMxkyCUzovnjRlniRE56w1HOXR9icSK2N1SgToT2G24yeNhbVhkzzr0Wccvrg7EjzIQmFI3VmdX3FGmEJh2L3we_MUuMPLpnU0kWPqMZ-00VzwoOkcsRfZILMNG9SH_04wFv7zpT4nAjlCtEc-Lqe5N8ynGkHNH9WiD7Oyi-uLKbJxwOznG7YFp2t5V1Aw8nsWy7ZJnNVNvzXbTYUHdbGzyKsX_XaBany2BDgZk2sb4dK8fRbi2ix2Sj8GemHSHDbGnjg87SphiIzUesHCyWi-jTZUvWi44GbJtcoruA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=gebWfRYBtenaQGWCCe3qsaHkR50w-C8hFHdDyKdIJ_Al50vo6PZ57QlCs0d_TPnflZdONQXJ5ML8OgryIoFQyrQZ9KQbf81Zc8jzJPNd78u3KtDk-dBeSjsfpkuyxLnnRUMsRnBBxIzYx9ircmB5i5N5B6qKsEezbdRywNPAy4nEGSN4VBs6D7Y3-Gh6ae89OEl7xKAKm3L6Z3aB63fG8VMdCkspK5tQYPxPuCy4Gnqf9Ugkk2my7cBsmERklcesQ1_RUrULUWI93_G-2ic-5I59cx1g41odToe6L7_sqtOplQ3qSzSkzosOEPGLbzpxpeX-YhZ1TRQjKxLE_EcvmGsh-lz-ryNxsvHNkcV1dm9mllfbRPwtvym8FHdmHDdhsNsAhZpd2CW5PFkWhz3YqFejFZ1gMpD4IL687U-NozG4XYuTLXP6Bp55YDHusMusRpWJl2s2jfzgKpN0TXYIM5b1bojJu1UGko4qGdKNKf3YLNv030bjsROajUr7QNkXVOgYvwaYg1NT4v7xI3Ej6EM0zO1U4YzuJNt9g45NfK2ucjcNbUcsBqObwI6otFnaQUxjbrL9rekOZBxx-oxJwBJU8xEB-zOrTr2sLMMTES8Pc6uL9GcYsod9wG-7l4Lqn73oC8r8WAR-3Ogz4z3IIEsVzgUR12cFGlBz5dXsUGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=gebWfRYBtenaQGWCCe3qsaHkR50w-C8hFHdDyKdIJ_Al50vo6PZ57QlCs0d_TPnflZdONQXJ5ML8OgryIoFQyrQZ9KQbf81Zc8jzJPNd78u3KtDk-dBeSjsfpkuyxLnnRUMsRnBBxIzYx9ircmB5i5N5B6qKsEezbdRywNPAy4nEGSN4VBs6D7Y3-Gh6ae89OEl7xKAKm3L6Z3aB63fG8VMdCkspK5tQYPxPuCy4Gnqf9Ugkk2my7cBsmERklcesQ1_RUrULUWI93_G-2ic-5I59cx1g41odToe6L7_sqtOplQ3qSzSkzosOEPGLbzpxpeX-YhZ1TRQjKxLE_EcvmGsh-lz-ryNxsvHNkcV1dm9mllfbRPwtvym8FHdmHDdhsNsAhZpd2CW5PFkWhz3YqFejFZ1gMpD4IL687U-NozG4XYuTLXP6Bp55YDHusMusRpWJl2s2jfzgKpN0TXYIM5b1bojJu1UGko4qGdKNKf3YLNv030bjsROajUr7QNkXVOgYvwaYg1NT4v7xI3Ej6EM0zO1U4YzuJNt9g45NfK2ucjcNbUcsBqObwI6otFnaQUxjbrL9rekOZBxx-oxJwBJU8xEB-zOrTr2sLMMTES8Pc6uL9GcYsod9wG-7l4Lqn73oC8r8WAR-3Ogz4z3IIEsVzgUR12cFGlBz5dXsUGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=Nf5hgSkTbPXQr8CPDUONdLg2ql-FkcyDKJdaSr7EVv203zJ7mnnXDu3vMtUDCr9GAwlMEZAGHAsN0WDgcNXkrmE25fVX1IkVSqWzQ4CTUiDOeOLdI0SUp3oWXjEbOiiWdWySCSb7IS0yxbjOytDVzwG78mBmYURtLdiyTLusIsMTvwTW_UP4N5f1XxDfwYUhac_3uYPOZA3PgN27I2hceIbZ6d5cIxksVWc47a6cgeA7NbP_YtKpZ1mKA7S6E8wwwpG2WH-Ncs4414LtQuChl1ukm_s1mVXDMdc5PXr6yvXlnW4I45YXNPaHwnUvi-oNYEJsaPou6V4h5jJyrtkmxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=Nf5hgSkTbPXQr8CPDUONdLg2ql-FkcyDKJdaSr7EVv203zJ7mnnXDu3vMtUDCr9GAwlMEZAGHAsN0WDgcNXkrmE25fVX1IkVSqWzQ4CTUiDOeOLdI0SUp3oWXjEbOiiWdWySCSb7IS0yxbjOytDVzwG78mBmYURtLdiyTLusIsMTvwTW_UP4N5f1XxDfwYUhac_3uYPOZA3PgN27I2hceIbZ6d5cIxksVWc47a6cgeA7NbP_YtKpZ1mKA7S6E8wwwpG2WH-Ncs4414LtQuChl1ukm_s1mVXDMdc5PXr6yvXlnW4I45YXNPaHwnUvi-oNYEJsaPou6V4h5jJyrtkmxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=IE0jq0s24ChhE0NpUuupgXHQMD9Et1XBOq6QLGMSpDA2PLBF41t1UiYLyNbmUmqUWeEAyZfBGrEqIjfiWOP1c-ON0ZSPbfA4CUtqRumsmm3j60dcjwV5QvbL8S0knoAqBN6JiOcF21HOfl0u7Wk0GNabRMcELc1L6jV43fGNjDf2WWKUzb-UHOCftYO0XqnG9briJXtt8SmNhgXVQw3AbcAdXXmp9daVX-hHs-MiK1Et9HYwltioo0LabCbCyRinSXKm3i0ffChNc6nmg5lEdgUS_X9CXQr966XdKDZgkP7nXsGTC7D2Vr3DeeN3H2rhbiXa_bv_CHAkSdAT76-O0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=IE0jq0s24ChhE0NpUuupgXHQMD9Et1XBOq6QLGMSpDA2PLBF41t1UiYLyNbmUmqUWeEAyZfBGrEqIjfiWOP1c-ON0ZSPbfA4CUtqRumsmm3j60dcjwV5QvbL8S0knoAqBN6JiOcF21HOfl0u7Wk0GNabRMcELc1L6jV43fGNjDf2WWKUzb-UHOCftYO0XqnG9briJXtt8SmNhgXVQw3AbcAdXXmp9daVX-hHs-MiK1Et9HYwltioo0LabCbCyRinSXKm3i0ffChNc6nmg5lEdgUS_X9CXQr966XdKDZgkP7nXsGTC7D2Vr3DeeN3H2rhbiXa_bv_CHAkSdAT76-O0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ffyprLgY_gk3FCwrty6_8kT1wMutnDTXyXstwon8tuvrRgi08hxqjzVPqv-KceDj0phWj96Lvs0Qa2-sQVke7ascleyn6VTjIvn0gIx-dt3VmulX4g7bNqAAzcYlVilQwvG9g2z0VYJ17DdhLu5t2ybH6sjWR5aZwJpT9HS5WJTM9xRbqg3iE4ETI6-wm2TWW6znt56-oSJxml5qS2bSQaUaXJ38X2h_dhFCy9VqQDoe5-GCHBIioByq72GNSKnfd6u5VcWnRwu9S2hHNYx5pMF84ul7dbi0GPSzFxgQ_OQjBSe7b26CQbQCd3oYn_FzEByK2x-C6I2sT1m14RSoqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ffyprLgY_gk3FCwrty6_8kT1wMutnDTXyXstwon8tuvrRgi08hxqjzVPqv-KceDj0phWj96Lvs0Qa2-sQVke7ascleyn6VTjIvn0gIx-dt3VmulX4g7bNqAAzcYlVilQwvG9g2z0VYJ17DdhLu5t2ybH6sjWR5aZwJpT9HS5WJTM9xRbqg3iE4ETI6-wm2TWW6znt56-oSJxml5qS2bSQaUaXJ38X2h_dhFCy9VqQDoe5-GCHBIioByq72GNSKnfd6u5VcWnRwu9S2hHNYx5pMF84ul7dbi0GPSzFxgQ_OQjBSe7b26CQbQCd3oYn_FzEByK2x-C6I2sT1m14RSoqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qvwCVrgH0yFiEbCh08j8TY60llrkOnWJFlwo1DuKkuZ-TzdxUk_S-jqXIOnmuuTG_d1WuPUtjvPrRXGS1cWKezfAHmt21IGT2moI3ZyZilm6wZtnfDBQ9A__17jM5qmzXTV52caQaLaH90y9E5PXhJ6eI2L2PR3yFoTw6Ec9NHi2hbzjQIQ69w6qtLD36edVUMbm7dEPDhD7_ossBFMgybaWMDxwt_jcW30k-NejyVMZl7PhlN7bzBlDL9krHE8EpmdSiPXm30ia3qZk9dHhcVbCh2RVOwXy59ZDpy-XMkI9qOWm0MckT1avh1o3P8jNKw8xgZ9zLpAqUFscD1szjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=rri7U4MufiLkwLMhKU9YfS-AbfIf1mzJFypzM_6A6Xw51KrM19BPxBXJH0-hQdzVYLFNK6pnxli8v7w8MA7dpqw-Zu8mYtlUV9NrXqBR6S2ng0AZmbfEUaiJXfxyXNL-rmGUqadUs6TvISJgEcTzUV0my4tg91xPny3MRojQwq3YLK0BZNqVGG17jYxmw4ywIXXDIJF6aGGu3aUqgALCPkdGE0WLth_vul82xmjnLPnX_5Qvf34fmBYbZYiPXV-d0cBLuJlFgwAyqBaMVhJoRYan0zhkpvjU5ID8rV0SyngSiIl-KmBU8UAXV7bt-SoZTrDS5WkPjgmDDtadzikzEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=rri7U4MufiLkwLMhKU9YfS-AbfIf1mzJFypzM_6A6Xw51KrM19BPxBXJH0-hQdzVYLFNK6pnxli8v7w8MA7dpqw-Zu8mYtlUV9NrXqBR6S2ng0AZmbfEUaiJXfxyXNL-rmGUqadUs6TvISJgEcTzUV0my4tg91xPny3MRojQwq3YLK0BZNqVGG17jYxmw4ywIXXDIJF6aGGu3aUqgALCPkdGE0WLth_vul82xmjnLPnX_5Qvf34fmBYbZYiPXV-d0cBLuJlFgwAyqBaMVhJoRYan0zhkpvjU5ID8rV0SyngSiIl-KmBU8UAXV7bt-SoZTrDS5WkPjgmDDtadzikzEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=Va3AfEHQmpgo4wXTD63gaD32PRAtLKrqpMdeu0XIPBrUyPJhzh2tTDcJu6IwTVRb3DjgwquF1ngKIwf7lAxUOIdYV0H8fe3aR6sJw2LSSyT52ikIIT5Gd8GURxhTlh-9GqlE8OmxMCkW7vqXe489RHWdmqO3W4XjFByAKf94mOaDtp7zvgEY4LCX1cq13066bbUGzGL5893IPFkudQ-2yGaukPnV8c252LmYLGxQTmBsLnraSnxbH-XGmqGHHhepWrcFzAADGpQpKYF4tGyxmQgVakGSj5mskWkmDT2sDGQstXTQdLhS3GU0d1steGJtg0LWIfR89_um-DfFOmuj1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=Va3AfEHQmpgo4wXTD63gaD32PRAtLKrqpMdeu0XIPBrUyPJhzh2tTDcJu6IwTVRb3DjgwquF1ngKIwf7lAxUOIdYV0H8fe3aR6sJw2LSSyT52ikIIT5Gd8GURxhTlh-9GqlE8OmxMCkW7vqXe489RHWdmqO3W4XjFByAKf94mOaDtp7zvgEY4LCX1cq13066bbUGzGL5893IPFkudQ-2yGaukPnV8c252LmYLGxQTmBsLnraSnxbH-XGmqGHHhepWrcFzAADGpQpKYF4tGyxmQgVakGSj5mskWkmDT2sDGQstXTQdLhS3GU0d1steGJtg0LWIfR89_um-DfFOmuj1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=AZ7ckjmAoP7Cezt01D40Mvgbf7FLTTA6TbH70V8VnZtlAbsoE2wF8N-m5rPYFS6m_mv21XYxEBGV_k2tNFgGWnzaanZKc8eZ26rcl_1mlgvqd1zmlkCbDvEYamdSeksHiOBdRPHRFbWSDdVOzKqrtNMA5TBve77hoqPRli77JELGQfSAFHoLw58l4FEuchU0j_zTJFnldeiPalL7xYN9tASq4OaME8svklFHTXoc0B1qxh5ncuXfnyLlLUppLtnUHELXfs8vjfrE_EPTx7stuldqaN59-2Q690L20DCRtoF6SbNcKbWBuh1j5YK5Rwv4wlNHv5xkjDPa5ONlcgZ1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=AZ7ckjmAoP7Cezt01D40Mvgbf7FLTTA6TbH70V8VnZtlAbsoE2wF8N-m5rPYFS6m_mv21XYxEBGV_k2tNFgGWnzaanZKc8eZ26rcl_1mlgvqd1zmlkCbDvEYamdSeksHiOBdRPHRFbWSDdVOzKqrtNMA5TBve77hoqPRli77JELGQfSAFHoLw58l4FEuchU0j_zTJFnldeiPalL7xYN9tASq4OaME8svklFHTXoc0B1qxh5ncuXfnyLlLUppLtnUHELXfs8vjfrE_EPTx7stuldqaN59-2Q690L20DCRtoF6SbNcKbWBuh1j5YK5Rwv4wlNHv5xkjDPa5ONlcgZ1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=UxAVwlIajHVESTyw__aDZS3TjueH7H5nfK77mOp5YIhfGoOc-Pq-y1Sqqj0WZ_Iby6SUDwGUB_YWggsi64bkS_3_kc9hc2vRbDahKGSsFOCW40hGsCK0pfCswDV3yhF6U-Gv7dd1OegoPFpDI8kF-SGspwJxlqJbut4GmDGP5-ygAy4m9S7EyLuNiFTt9pEUNhUlYJhmU-OrtiIzF_SvmgWH5z2FGlOlTzCVwso77J6bETY1mYOL7St0Wc-BSqEj2pJNTVnjGBkCFiNl68Vb3k39knsGwq8Bs62yfFQUD3Sfx4IOMOVp1fidf11tzxnfTMzhUoW4X6wdMaTFxK903w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=UxAVwlIajHVESTyw__aDZS3TjueH7H5nfK77mOp5YIhfGoOc-Pq-y1Sqqj0WZ_Iby6SUDwGUB_YWggsi64bkS_3_kc9hc2vRbDahKGSsFOCW40hGsCK0pfCswDV3yhF6U-Gv7dd1OegoPFpDI8kF-SGspwJxlqJbut4GmDGP5-ygAy4m9S7EyLuNiFTt9pEUNhUlYJhmU-OrtiIzF_SvmgWH5z2FGlOlTzCVwso77J6bETY1mYOL7St0Wc-BSqEj2pJNTVnjGBkCFiNl68Vb3k39knsGwq8Bs62yfFQUD3Sfx4IOMOVp1fidf11tzxnfTMzhUoW4X6wdMaTFxK903w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=ZrffgWu72_XBiVtfGc34Xa9vItQKot1l1MHazA6AIhe7m1_mPEWZhBz70U9ZHUso5qxSivYW2KPZ4x30LJySGLvNoQkjj8SM0MSJeFr6YM8caM2ZmUx0bcOdZ_VqZq6EPnvH6JsOAjH4lHjUww1c88Hp9imlFbojpErYJS4d-8q9cvMJs6PTJ8_rexNZMxCkWsPtxsQWD2VvnSF9NWbgWzdqkW8thXuPzGuu1YAQiPVo7Y9SYTaaLn_-6H215TVF-uwKlvwfyNcC4h9HZUS28ufm6Qme5jF3dbTTODZCDS3zzo2rTDL-m1UjE5YICMmEmHbSGcGgvEbfhKyKB3ynKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=ZrffgWu72_XBiVtfGc34Xa9vItQKot1l1MHazA6AIhe7m1_mPEWZhBz70U9ZHUso5qxSivYW2KPZ4x30LJySGLvNoQkjj8SM0MSJeFr6YM8caM2ZmUx0bcOdZ_VqZq6EPnvH6JsOAjH4lHjUww1c88Hp9imlFbojpErYJS4d-8q9cvMJs6PTJ8_rexNZMxCkWsPtxsQWD2VvnSF9NWbgWzdqkW8thXuPzGuu1YAQiPVo7Y9SYTaaLn_-6H215TVF-uwKlvwfyNcC4h9HZUS28ufm6Qme5jF3dbTTODZCDS3zzo2rTDL-m1UjE5YICMmEmHbSGcGgvEbfhKyKB3ynKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=MjeHu6V8WKdCBGjVuLWRDBZHd_wshtLnGacC3k6ddabmZBJhPBKWSzAMwHAVjh8TPPwPZy2NF3ZuKbS3IH-SqqLSE_ZRRDs89m99v07EbXg2UvgWVjq7mZYsmL09jyiX0sqpM6fR4N-dGqeBecriSQGhrXTEq3VAoxdggac0uxjdJQ6FXcugm7IndFSuUIegAfjHxmNeALXyde9e9lFL-xGPbJ_Vjix9bWW3k6BWhW2OH_BYVUih0zZGktdv8Nwf4esmfGwiSatdW8XnV1SbRi7SFmglE0-ZuF3PluhsMabY1kh73UOLKVgjjYnxxBnLq6j3UhLfURPCFUv1i-k8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=MjeHu6V8WKdCBGjVuLWRDBZHd_wshtLnGacC3k6ddabmZBJhPBKWSzAMwHAVjh8TPPwPZy2NF3ZuKbS3IH-SqqLSE_ZRRDs89m99v07EbXg2UvgWVjq7mZYsmL09jyiX0sqpM6fR4N-dGqeBecriSQGhrXTEq3VAoxdggac0uxjdJQ6FXcugm7IndFSuUIegAfjHxmNeALXyde9e9lFL-xGPbJ_Vjix9bWW3k6BWhW2OH_BYVUih0zZGktdv8Nwf4esmfGwiSatdW8XnV1SbRi7SFmglE0-ZuF3PluhsMabY1kh73UOLKVgjjYnxxBnLq6j3UhLfURPCFUv1i-k8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=XH-kH0TomVJJhLoLIpZiQUCn7JcRsDishihQ88qMgCo1ExYLZy-wTKPW2Ar2F6q52gmsVAoJTtKMWkrWZR5KiloZmdYft3KcbH4QPv5NNZ2cLJrgcGuM6PEf4qJTn4rbkIPymUGxx5oL3Ytjqhp2lKdASLv6Jw-kp9Hm9PsWGgy7ZV-TC9S0uyz6k5J7lFENN-Zxf7eXVAA8l8iNpltempGOorSF7KknvXkHNMaAMd0fMSOHms1srf0BY8Er0QVWdYg3_vO1JztTIWleP0si28yFTTzJCA9jJwTrei0UZWbyxneRWRF0fzJ2-d33Yn0bWzLuRI3GUnmT3BZT_7DQZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=XH-kH0TomVJJhLoLIpZiQUCn7JcRsDishihQ88qMgCo1ExYLZy-wTKPW2Ar2F6q52gmsVAoJTtKMWkrWZR5KiloZmdYft3KcbH4QPv5NNZ2cLJrgcGuM6PEf4qJTn4rbkIPymUGxx5oL3Ytjqhp2lKdASLv6Jw-kp9Hm9PsWGgy7ZV-TC9S0uyz6k5J7lFENN-Zxf7eXVAA8l8iNpltempGOorSF7KknvXkHNMaAMd0fMSOHms1srf0BY8Er0QVWdYg3_vO1JztTIWleP0si28yFTTzJCA9jJwTrei0UZWbyxneRWRF0fzJ2-d33Yn0bWzLuRI3GUnmT3BZT_7DQZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=LKpt248pdO2x7oXOKgF5zsNWTbSwBbfHhmRd6GQ3e1XmcQY0AcX7syEiWQFsANXTry_3Ovaynac6HRZsRitdb7Q_XlFVHF7EQiyQOEBdIOdmYBDfiJMItHw6XhEvzkDkyq982kiCsA5VdUUMIT2F7lDmzvp5fwt2dz-IY5Y_xHOcbnqWFonIyDE26k8LeOg4yieYylaHlXAupabDhLmH7vOwWpHQnKxB-nki4Z07xQM31K6HS0q2f0_vO9ZV9eNuPqMQvn-x_dthfbbxOS7CLwmU8CVR0bf6C85aqGJwVclJBwtGrcWBQC4ptJeLMCiuEciaKKMFYP7OpEixHf0uBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=LKpt248pdO2x7oXOKgF5zsNWTbSwBbfHhmRd6GQ3e1XmcQY0AcX7syEiWQFsANXTry_3Ovaynac6HRZsRitdb7Q_XlFVHF7EQiyQOEBdIOdmYBDfiJMItHw6XhEvzkDkyq982kiCsA5VdUUMIT2F7lDmzvp5fwt2dz-IY5Y_xHOcbnqWFonIyDE26k8LeOg4yieYylaHlXAupabDhLmH7vOwWpHQnKxB-nki4Z07xQM31K6HS0q2f0_vO9ZV9eNuPqMQvn-x_dthfbbxOS7CLwmU8CVR0bf6C85aqGJwVclJBwtGrcWBQC4ptJeLMCiuEciaKKMFYP7OpEixHf0uBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=TvlMZQfqu9MLb1JWb3F_s7rn3M4EM1uG1TcPIUss5ie_7E4ofdea4qozIFOR_0HgViy-A48hx-2MrbvkyIkpIixadEfZxj58oBJdkvJv0RDElbTyv60GiPlVX6pBtWZoal1brn0YdXiPVajAMdrnMj4rAtyAenjVk-mdoVGpuXFcehQWUE_mu0POhxUWg2PHvBcWOX8ELFuzg7Ks1mGx8-e7pjaWTPnR8EQ7n9ZMqBTN1JlAjcQHkC_CmrIdkV5YykDh9G5myIugchaUVxvDiaecacL0aCtCsjtzfzMy5THZKMUh27lIwZ-18sfKOVhjwItj_lAenMvLN7b52TqNGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=TvlMZQfqu9MLb1JWb3F_s7rn3M4EM1uG1TcPIUss5ie_7E4ofdea4qozIFOR_0HgViy-A48hx-2MrbvkyIkpIixadEfZxj58oBJdkvJv0RDElbTyv60GiPlVX6pBtWZoal1brn0YdXiPVajAMdrnMj4rAtyAenjVk-mdoVGpuXFcehQWUE_mu0POhxUWg2PHvBcWOX8ELFuzg7Ks1mGx8-e7pjaWTPnR8EQ7n9ZMqBTN1JlAjcQHkC_CmrIdkV5YykDh9G5myIugchaUVxvDiaecacL0aCtCsjtzfzMy5THZKMUh27lIwZ-18sfKOVhjwItj_lAenMvLN7b52TqNGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=gL_Omjyjdt0o4VVuFSnlIC2Ip703QcwjATGGi1bK7-sBj0X0vqa-zUGih-xgB1U8-lhC-6FDTY8DHupcXuTq8q-0TxOfhctu2wYACRlS4rhAmcHe13BCZLaDGEe1Vr8OQbZ6Yi4W0rvvJeyjzMUTBwGMne5I8phFvOpe7_cRk6IEgLcb4iiDtZfEdNom0Il8a1LrTO736Wt-HMoBnoVYt5sl5cXMyE5Ye1j4czEy6lSv5N0nibxVWAPA3dvcHrU6JarUcsszJpIup7jHyQBSbJfCN71CK0OjRtNhUhMK-P5-4yNQ-thDqe9yWa0i1Dj2FfAsf32UkXZD9gDLBqWSKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=gL_Omjyjdt0o4VVuFSnlIC2Ip703QcwjATGGi1bK7-sBj0X0vqa-zUGih-xgB1U8-lhC-6FDTY8DHupcXuTq8q-0TxOfhctu2wYACRlS4rhAmcHe13BCZLaDGEe1Vr8OQbZ6Yi4W0rvvJeyjzMUTBwGMne5I8phFvOpe7_cRk6IEgLcb4iiDtZfEdNom0Il8a1LrTO736Wt-HMoBnoVYt5sl5cXMyE5Ye1j4czEy6lSv5N0nibxVWAPA3dvcHrU6JarUcsszJpIup7jHyQBSbJfCN71CK0OjRtNhUhMK-P5-4yNQ-thDqe9yWa0i1Dj2FfAsf32UkXZD9gDLBqWSKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8fuTg8pB9eMm9D_zK7LGyMb68T5svukMl2GH8FiJUEYRqMHYGkHYcbyIJ1KgOQyERY7_IxHauL980AqAtMLWciX0VlNpGOjCRQHWqkX5UqL70_o-npmKp31yrGJ18CsN6qG_ynnOkktOE4K9B96tZg8nlYQT_qYfTeKarjDsF2DGZnH6j50det_b5-9_Xlso6q1OpoXcPqgV-14VwP32m0vZqKNzoyWUOtDloaUmu3T41UIbdN7e_8r4jlSvMTl0974Exc51eBTPQ0Rw3WE92Xjf4J_mgv_8yTiN31BeHT7q1nzYlfoEdOP2hYp_fBeAunijdP5pqSwX_i7xcWcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UnrCCF7l_9UxMLh8NLUZZjsT0svMV3NFJmhR7TmC9CLgrpweBGw-o_ctgDabogHU9IptbOd7T_CKzOS-o56U2LxMv3SLZkbXZeQM2mwcxluGFwv9-tPe-zcf1hmCCwsK-FpuP9P0voDQOTVn6KkwRL8vJwUkcdqwsq5-i8eH6Lq17VnX7Wqeo2yZtg0N863Gvmyi_I99BqzjAKKR332cIsUGS6I9T6gMjeknpq6pHDvYLU25lUega_RYFLtvpemM85d4HlEEbjZC2H6QzI_Mglv448Kl2U7pk-NQQhpiPPD4C-uXCbZ-jwAIhJAhR7HJ83bjtHJVaArVk6GTH1ltdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=fhKwe8ZF6x6DrRptjdbBHxO0JtfUT0tI4DSehmoh8WDmjCdGkEGvEsBLPy6pEYPYQiIJrhvaXmSMV1IIoCm0JJ_Exr2tovJClWEoYOHQEpLfqDaefBack0bg4oh5t5BJeVxdb30I7jqzhHz_8sTFN-UADye6lWwNvtCr4gtGGmXq-n-T6chCuGRLpqA-eCzfImcYnQm_KDrKZiRB9gV2RN8NAPCw752agoO4HjvWtfndZdxdMsX7k3DGjWOCsXrCTc91RfV4_J-rvj4ydcjcKg9vOwPua_CHjDZhSfI9xDVO-MbCU8hTB0BdVysFHy2XBUbKBqOVUjtEPb04eVP1Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=fhKwe8ZF6x6DrRptjdbBHxO0JtfUT0tI4DSehmoh8WDmjCdGkEGvEsBLPy6pEYPYQiIJrhvaXmSMV1IIoCm0JJ_Exr2tovJClWEoYOHQEpLfqDaefBack0bg4oh5t5BJeVxdb30I7jqzhHz_8sTFN-UADye6lWwNvtCr4gtGGmXq-n-T6chCuGRLpqA-eCzfImcYnQm_KDrKZiRB9gV2RN8NAPCw752agoO4HjvWtfndZdxdMsX7k3DGjWOCsXrCTc91RfV4_J-rvj4ydcjcKg9vOwPua_CHjDZhSfI9xDVO-MbCU8hTB0BdVysFHy2XBUbKBqOVUjtEPb04eVP1Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=iaFPhvFaGqIB2xIzMJxFeWAn3a13f_b5-yd7qNNvZlWPcMxQn_XPkx1EutK4od-HVKsApHoIPzbjTaBK8FT_rG1t9FfWjv2RD8EZ6X-R5Ik6J4p1x9F2kDrcP_rRcvIRY584LepsmB3WV_4o3eB_2pV_xp8yr_ucUtrdOQ8_O6zX4G9Knf4qaa_dmlxqz2XS7KG72Nt1Y6opWYtVY8VUASR4Iz1pAjD1bWNyuLlqBh2a4kIQ99_0JBQ1TcnhK7a-DACYmYoB-8pF5I46Cmzo8Xo6U4Wx4DUWC79XgPynyeiNESSgEqwtxDLAp031-AGXNwG5v9tiqK0jE07EzyhG9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=iaFPhvFaGqIB2xIzMJxFeWAn3a13f_b5-yd7qNNvZlWPcMxQn_XPkx1EutK4od-HVKsApHoIPzbjTaBK8FT_rG1t9FfWjv2RD8EZ6X-R5Ik6J4p1x9F2kDrcP_rRcvIRY584LepsmB3WV_4o3eB_2pV_xp8yr_ucUtrdOQ8_O6zX4G9Knf4qaa_dmlxqz2XS7KG72Nt1Y6opWYtVY8VUASR4Iz1pAjD1bWNyuLlqBh2a4kIQ99_0JBQ1TcnhK7a-DACYmYoB-8pF5I46Cmzo8Xo6U4Wx4DUWC79XgPynyeiNESSgEqwtxDLAp031-AGXNwG5v9tiqK0jE07EzyhG9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=so5guiAGKKU_wpd-TVYhH5t61_RQaadxjOkGgQ7hHud21iPjRnt3_Q5hajaHKd2odvqvGXoDAww_kDUb38ZM-XcqmMHcvREcSVbwV_9lUvpzQcaslTFpC_0E5xY0w1z79aqMUSkLv2XbvJxJ1eUYfiFx49wPopsljSa_priXi4826xYs_QTgc6HyVxpue4XzqQODcn6T7LU04fXWftTPtwSgo93bCHqXciW0WeTly7528bW9N6aA073g5VvLC5z_V8lgMqt7GtcmyNblIU0JUz2TqL_4xGqcbVu_BVFKISFls6jeFpnb8QQANnyV3jYjzuCNGDMAwT9ZTVx0RauBiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=so5guiAGKKU_wpd-TVYhH5t61_RQaadxjOkGgQ7hHud21iPjRnt3_Q5hajaHKd2odvqvGXoDAww_kDUb38ZM-XcqmMHcvREcSVbwV_9lUvpzQcaslTFpC_0E5xY0w1z79aqMUSkLv2XbvJxJ1eUYfiFx49wPopsljSa_priXi4826xYs_QTgc6HyVxpue4XzqQODcn6T7LU04fXWftTPtwSgo93bCHqXciW0WeTly7528bW9N6aA073g5VvLC5z_V8lgMqt7GtcmyNblIU0JUz2TqL_4xGqcbVu_BVFKISFls6jeFpnb8QQANnyV3jYjzuCNGDMAwT9ZTVx0RauBiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=Y6cl77ZyKDHBoG5aXOy2NOuQljz-KjIIBadAOwKCJg84gYdP3wzxcOFAkix7yweHf7QrDofKor1rkzQ75FZ-vZfe58vtijOP0Fx9gzJz47PvSBSlbvmDIn5uTN9Ys1K6V4LgCfICwlJ4A2YUK2_cY0S8u5wiSUWPMUxXxMHOJ5JG5MeljxQq3t8-JwpUtjpGvtCjhoSDK08mDzXIvD1yMxf-E_EiwbDyNKXWXY7Sp-Qa2nabo6bsRi-03t9s3GghLOvYu2x8xINCFoPiWd8RDntAHuABsNP8e0KemD4iWJYHf2ZmY5078KMoSvh1c6sqij-Bto3vMObNeZzfQ_cAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=Y6cl77ZyKDHBoG5aXOy2NOuQljz-KjIIBadAOwKCJg84gYdP3wzxcOFAkix7yweHf7QrDofKor1rkzQ75FZ-vZfe58vtijOP0Fx9gzJz47PvSBSlbvmDIn5uTN9Ys1K6V4LgCfICwlJ4A2YUK2_cY0S8u5wiSUWPMUxXxMHOJ5JG5MeljxQq3t8-JwpUtjpGvtCjhoSDK08mDzXIvD1yMxf-E_EiwbDyNKXWXY7Sp-Qa2nabo6bsRi-03t9s3GghLOvYu2x8xINCFoPiWd8RDntAHuABsNP8e0KemD4iWJYHf2ZmY5078KMoSvh1c6sqij-Bto3vMObNeZzfQ_cAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXRYPwGBuxW7Z7hdrb4RpqIjY-8flSwJuLbBRI0tKo6R-BuIEW4HYlJBt4KKMkOEGcr5bHYO4aR9z_y_QZjWO3T23v47SYgHTZUHoLSmQc0WxYihL-RLvc-zrM_CxKtuQxO4sNB8M3vTE7CyFrxD0BFJUBchZm2YM0jEA67xjI6qanQ9DfW8uxvbzY4dCIRAN1MIF83DiVOHeAVMIJUCKNSaz2jDVRYYyu0LDVhuY0SbzjbBnTIWZ9ZqgC_QD7UWaMo6CWkWVCGtbQHn8RY3B1ssPYYssaiHJZhtdAm2lPOICPic0j1u4NBjo1R40qAAdAiNI-VmYNO1oCvOB74a3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4mGxsyRaSj_RN_LHyKmskQCWPuCiqujG9cDUMrLjVSXUCV7yKdR6U9aSRZdKEMuaDOcr3W3FfPyjv53A6xQKxmesDMQdGxnn3UNxG4FOgcMn_xVZHec2-wcKZJVXOEMZ4MacjL6HGKTey7T46VF5Ny-dm9Tz1sauyMKMASKope4jBplnSb-B0gB3Zp9i6Wphzn9_2950SGTqNph7zZo7vPzc1hnh_qwTOXIHBcRjpsyW2VGDsVSkfBZwNpF29sCsTOaRD1e1-8xVMmQ_gMYnudE7sSKbRBIuaQoIuTAIcOxtkO5rIEZhhMxSdY5vxoyM8XNXKS3oKRNeIIjAOnQaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9wjF5dH4xPV3ajzjg24L8bHtbvsDsHE01YyNYByTRTPv0kO1sl8gBpoTfg3DonggCuujIBKO7lMuEbbSB7rQMGi-UIq4DkWMKZMnPuEa6DvfJcz531e-0WMJc7YiuP4P3GYJJLTdWrKoN1165BZ2Q7Ju1evumpb4gIh5i2u5Zg9rXn0ToEHNZrhK7RfZS49jCfba4bk7RslxWtbDfJzpZdEK1fbk3uRT1dUrwlM0s1vWcaj5lokTHwSWJSQvlE4Rk9AJr67h6h8IevB-MhFPSuNoCt1iU62ImPxiq9G9UCXwi2gdRgiuTKNkg2Lso7fQUry9qSwY19W94d5EGlqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«با وجود اعتراض‌ها و اظهارات نادرست آن‌ها بر خلاف واقع، و همچنین هیاهوی مداوم رسانه‌های جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند، ایران به طور کامل و بدون هیچ ابهامی با بازرسی‌های هسته‌ای در بالاترین سطح و برای مدت بسیار طولانی در آینده (تا بی‌نهایت!!!) موافقت کرده است. این امر “صداقت هسته‌ای” را تضمین خواهد کرد.
اگر آن‌ها با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای در کار نبود! بر اساس این توافق و دیگر امتیازات مهمی که ایران در حال ارائه آن‌هاست، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی دیگری اعمال نشود.
با این حال، تمام کشتی‌ها در جای خود باقی خواهند ماند تا در صورت لزوم محاصره دوباره برقرار شود؛ هرچند در این مقطع چنین چیزی بسیار بعید به نظر می‌رسد.
پول‌ها و/یا منابعی که وزارت خزانه‌داری آمریکا آزاد می‌کند، در یک حساب امانی (Escrow) تحت کنترل ایالات متحده نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از خود آمریکا استفاده خواهد شد؛ از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما. ایران به شدت به این اقلام نیاز دارد.
این یک بحران انسانی است و من احساس می‌کنم که لازم است همین حالا کمک کنیم، پیش از آنکه خیلی دیر شود.
گفت‌وگوها به خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=lDrGPDHBnQLpZzpDoqD8wVcEIZc770IXtFrrclRfmQrInpsyoa7i93QtwZFSD-7kCG8UEqTM31WiO0Ux91Xs4NG5fJr_pZdjoohQYM0Etg7ysUjUd7x6GZdnVeZMcTdJG2-2Fgbd1-opo2XD2yHjkXAGF3scmpEmuITtilwEJyq7gvQDGhRkX0RNJjS-My7YeapdiRQqUFUsEHK6bi43TR3dfdm97A6UxeZybBo5NvRgRN7cluifFCGxCPNmNy3KmTDEOO6KewEfJ_olUvr1DI1EHI0Mn0qkK34PYytWx2BPbpU1uMSwFq0of7twpvnoo9RtLY0dQcvM5NkOkybUyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=lDrGPDHBnQLpZzpDoqD8wVcEIZc770IXtFrrclRfmQrInpsyoa7i93QtwZFSD-7kCG8UEqTM31WiO0Ux91Xs4NG5fJr_pZdjoohQYM0Etg7ysUjUd7x6GZdnVeZMcTdJG2-2Fgbd1-opo2XD2yHjkXAGF3scmpEmuITtilwEJyq7gvQDGhRkX0RNJjS-My7YeapdiRQqUFUsEHK6bi43TR3dfdm97A6UxeZybBo5NvRgRN7cluifFCGxCPNmNy3KmTDEOO6KewEfJ_olUvr1DI1EHI0Mn0qkK34PYytWx2BPbpU1uMSwFq0of7twpvnoo9RtLY0dQcvM5NkOkybUyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=LLXxX43K9tR61ns72edgyeXh5_8oIMVMt_TjPipy18CvjRgbl71pVS5vnQtg5T1pvAjw86owrpTB7TzTY4EZLuncx8c6Hf8jY-zfApJy9xkEcSkZ567DHJrT-7EMpbL672Dj7b9yHywSiTk85czR2bcz3elRSWKKCepqYjjEiAXVjU17MPWmzZWpYWxgFVOyEPA9o3wAvcfl7FAci_5tiDMXOs6HLiB9VKzVVJJHMOsoOccGseBb96Dyp1p8nCMWDZRhg0YNIoxc1dp6S8uevX8E-AGcXJceX1ICWTTGOIAYeaM0ze1tIyF-y4cY0O1y7LRC5s7urvzzqpsJCS_bTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=LLXxX43K9tR61ns72edgyeXh5_8oIMVMt_TjPipy18CvjRgbl71pVS5vnQtg5T1pvAjw86owrpTB7TzTY4EZLuncx8c6Hf8jY-zfApJy9xkEcSkZ567DHJrT-7EMpbL672Dj7b9yHywSiTk85czR2bcz3elRSWKKCepqYjjEiAXVjU17MPWmzZWpYWxgFVOyEPA9o3wAvcfl7FAci_5tiDMXOs6HLiB9VKzVVJJHMOsoOccGseBb96Dyp1p8nCMWDZRhg0YNIoxc1dp6S8uevX8E-AGcXJceX1ICWTTGOIAYeaM0ze1tIyF-y4cY0O1y7LRC5s7urvzzqpsJCS_bTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIqrRO7tEafVukh5DA7clB_4KoMraNR2DzV6BEXBbQYizAnCv4-mxlIbfENwYwDu7lB0TmINoASAV89ZlVZ1gVvDW38Ot1ub_1okZFlinyHDVleMBkH5uiSEpqHl_i_UhNu4UqFRhVP_6kz4eOaVMsOqBRHo-WUyTjHsYYLlhA63OcDXEz9iP0cqzfYSf6BqIwO9oOSqYATSpRb6xLq5S0zz-vfKJo2V6M9fPST39KYvir_FiWTefiTKKsm82eSkQStbHLAsNsdo4NG43cRyoSt5K6JQMdNuEHe0Ggey3-uM_I7FsxCcSFg5wZ6TNwZPp510CWXNmdQCF9XV_a1xmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=TYs521wh4VcBNz-uIoDdYxglWLqmp0CtwaRpNmmnc9i1R2vd3pn5U09Odayckurb3udHkKyZbDHn-K5KYu0JgbRmyWw1_JR8wYfUSN1At8rnbReWNf63iQWMSaFcsflqkp7hCHWv7xXj4uwg6F3cfTCWItw2j_ugEtpzF554blmi9i0a5pAjU4bUgX1qRbMCZjjvEPnczuhtM_xZ_p5LAl5fdrtjUxhjIrCoNLbz6w43oGuwKh77dWqbOveKKZB9fMni3jSUT2V6C7n_9HV_iZ8E_JipPAi9JJDCXAwxclBWJc2FYuF7Iav4zdvcNnyfcbt7wqZclKAteG5LDQbaL2nvVcsmvMOHnCMZqdPul4JGhe95e0i2MlQvfn0sy_cxAVXI-amUcJYQDGyIBUrmalIY87PD8llAk8ZqXH7Cqe5qpYTjxYwau25gpmMynZ233A14FMWyjUvKU-ba5jVZsn8SSZ6cUAeT_lUjR08imsp90TLox-uEqpy8t2FOYmCbE_rdIN8ujELtdAD49EKXplLZrBhghwHz3pDcv7QxflAabJF5ptUFbl8YJjJhQKFU3kA4lRrxWs1HKoirRT_45tUc1T3fMLb7fNQQ3Y14ro4Yv5ShCsv1krxGCoXgU4noVRbP1kruvxs6yDQtvGc0ZdR1ZnaD89LOIFir3yLkqJI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=TYs521wh4VcBNz-uIoDdYxglWLqmp0CtwaRpNmmnc9i1R2vd3pn5U09Odayckurb3udHkKyZbDHn-K5KYu0JgbRmyWw1_JR8wYfUSN1At8rnbReWNf63iQWMSaFcsflqkp7hCHWv7xXj4uwg6F3cfTCWItw2j_ugEtpzF554blmi9i0a5pAjU4bUgX1qRbMCZjjvEPnczuhtM_xZ_p5LAl5fdrtjUxhjIrCoNLbz6w43oGuwKh77dWqbOveKKZB9fMni3jSUT2V6C7n_9HV_iZ8E_JipPAi9JJDCXAwxclBWJc2FYuF7Iav4zdvcNnyfcbt7wqZclKAteG5LDQbaL2nvVcsmvMOHnCMZqdPul4JGhe95e0i2MlQvfn0sy_cxAVXI-amUcJYQDGyIBUrmalIY87PD8llAk8ZqXH7Cqe5qpYTjxYwau25gpmMynZ233A14FMWyjUvKU-ba5jVZsn8SSZ6cUAeT_lUjR08imsp90TLox-uEqpy8t2FOYmCbE_rdIN8ujELtdAD49EKXplLZrBhghwHz3pDcv7QxflAabJF5ptUFbl8YJjJhQKFU3kA4lRrxWs1HKoirRT_45tUc1T3fMLb7fNQQ3Y14ro4Yv5ShCsv1krxGCoXgU4noVRbP1kruvxs6yDQtvGc0ZdR1ZnaD89LOIFir3yLkqJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=XXGlIOaqcNgNoudUFN7Fx0MxmHzyDX5XJvw49HHJivCCS3JLuqPkVZJOwIGiSMPPH6XwPsnDbUlCpGbGI0J18W8n4zz10GmpMmvPm_HuFQVKRRwsVMXS3d8EIcm3eVZtpjWQTbb0gt7Nx7R0IZR8sOUvYQaLvCKRciF1Gyg56g-70XtcLyaOiBg_EY3Kh178hNwLmHwLs8Kzi0QNxy3DXner3yYgM31QHYh_zkVoXO2sUPje6qJ5CcKh5Ftmw33Q5sZZpnsfb7TwltUSFCf58B_lVRqBGmwUXEspXycYYiTtsAMQdFs4_KzP4Zhy8VLhFCFOpUoM2XaasiWvj_KCaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=XXGlIOaqcNgNoudUFN7Fx0MxmHzyDX5XJvw49HHJivCCS3JLuqPkVZJOwIGiSMPPH6XwPsnDbUlCpGbGI0J18W8n4zz10GmpMmvPm_HuFQVKRRwsVMXS3d8EIcm3eVZtpjWQTbb0gt7Nx7R0IZR8sOUvYQaLvCKRciF1Gyg56g-70XtcLyaOiBg_EY3Kh178hNwLmHwLs8Kzi0QNxy3DXner3yYgM31QHYh_zkVoXO2sUPje6qJ5CcKh5Ftmw33Q5sZZpnsfb7TwltUSFCf58B_lVRqBGmwUXEspXycYYiTtsAMQdFs4_KzP4Zhy8VLhFCFOpUoM2XaasiWvj_KCaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=hoBHJYD2hnqsI8Y_uDQsMYtQtHmLoj1ulszWKDs5dwZn8HVDn5BAwTAoqjbplUX1r5mOQV0YzJqHnqZwhDPOOeHzBPzBkeK45yBYLdcVn21YPuqCv_jcMrc9iw88zZQbXj6SzbZnZ646qpQ6kYudwe0NctDryTW7t1zT0FEagR8_qG-t9ekDo601U-siuGoBRmrLZkqpZoQ6MYLUl98MjlqcAEYqUp6kDDdNwOjLkTW8GNfKKQWZcUjLu6SvT4XxUDvXsJUM-QlMeL938MnZZDaxdKjcbNwuWrQjGVxCfBi-UUewv5XuGR58TZ7QJb-hGnw3K-daDAD-RfHm6zOqtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=hoBHJYD2hnqsI8Y_uDQsMYtQtHmLoj1ulszWKDs5dwZn8HVDn5BAwTAoqjbplUX1r5mOQV0YzJqHnqZwhDPOOeHzBPzBkeK45yBYLdcVn21YPuqCv_jcMrc9iw88zZQbXj6SzbZnZ646qpQ6kYudwe0NctDryTW7t1zT0FEagR8_qG-t9ekDo601U-siuGoBRmrLZkqpZoQ6MYLUl98MjlqcAEYqUp6kDDdNwOjLkTW8GNfKKQWZcUjLu6SvT4XxUDvXsJUM-QlMeL938MnZZDaxdKjcbNwuWrQjGVxCfBi-UUewv5XuGR58TZ7QJb-hGnw3K-daDAD-RfHm6zOqtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=CgHV0pWxo5XxmSg_19bJ0pCIwO0GB7j1hyZyrjnXvcdSku65E30pEha71Ngnh-u7BR5fBWFw8f0qqOwGFnH-1r5kqW40T2-R9RiTdStQ_otROPGIC1g3f1iojrzdZ93i3VEgGhPuoEQjWWOms8W_nLBf5QiIDMG3blIzG6m26pbxJL9USs0G7h5bRPBR4gPwv7LyRllaY6aZ1omUxJjTBF8AVvvpcZuX_N4abKjlaY9KyrlOZa4RjOQEgoeQR39U10X0x6zdEJcUoVW6TieI7STNS2SkQC_7XXA4rBgN68978vJPN0Wub__5EjOmZkTz0DbTwkOoIMqsWy1-58filg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=CgHV0pWxo5XxmSg_19bJ0pCIwO0GB7j1hyZyrjnXvcdSku65E30pEha71Ngnh-u7BR5fBWFw8f0qqOwGFnH-1r5kqW40T2-R9RiTdStQ_otROPGIC1g3f1iojrzdZ93i3VEgGhPuoEQjWWOms8W_nLBf5QiIDMG3blIzG6m26pbxJL9USs0G7h5bRPBR4gPwv7LyRllaY6aZ1omUxJjTBF8AVvvpcZuX_N4abKjlaY9KyrlOZa4RjOQEgoeQR39U10X0x6zdEJcUoVW6TieI7STNS2SkQC_7XXA4rBgN68978vJPN0Wub__5EjOmZkTz0DbTwkOoIMqsWy1-58filg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=LtN2JbezkGGe5JH0_yeNb_ht8h6VDgWB3TZjomhljTUomQBhzm0jVP1BmPEcxFYY7YGruQ79tJr8YSnd6Z7qNwIidIVhy-eCYI7JngoQtNtaAoDk1M3BlnnYOBV8w1TXwvVHJtlonNzQo47UtHnGjjdHkbjcjlza6L-TjB7Tq016oFsUnE1FzOlbqlTV4u5dF-fAyZJAMQbSXmQdc7-1YQyLIOCR6EGvCzy7CFAJeGNF4ZoEH5h49fSQ5aQj2l3nrtDU2OZJb4AfYGsc5a7NIhUvqFB6EZEf69qmK7AdLh-U7Iko6RGSygA2j2HP7Nupzacae4H_MVbzBupBRthZGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=LtN2JbezkGGe5JH0_yeNb_ht8h6VDgWB3TZjomhljTUomQBhzm0jVP1BmPEcxFYY7YGruQ79tJr8YSnd6Z7qNwIidIVhy-eCYI7JngoQtNtaAoDk1M3BlnnYOBV8w1TXwvVHJtlonNzQo47UtHnGjjdHkbjcjlza6L-TjB7Tq016oFsUnE1FzOlbqlTV4u5dF-fAyZJAMQbSXmQdc7-1YQyLIOCR6EGvCzy7CFAJeGNF4ZoEH5h49fSQ5aQj2l3nrtDU2OZJb4AfYGsc5a7NIhUvqFB6EZEf69qmK7AdLh-U7Iko6RGSygA2j2HP7Nupzacae4H_MVbzBupBRthZGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کریس رایت وزیر انرژی آمریکا: آلبرت اینشتن ۱۲۰ سال پیش مقاله ای منتشر کرد که...
🔴
ترامپ: برای هیچ کس اهمیت نداره
😂
🔴
کریس رایت: به نکته خوبی اشاره کردین قربان
.
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=Avqa98VMk3owOAW4yX2lbe7CLmgLFDtOpwhb2PGwMg-zDiKqE5rdLUyT626yOFfIrF5Od5r8yDGlo-hm-9qSDK6Mdh-ibOcdRPMp-4WwenbIrCg3PfGHH35Or31ELN1iv8FF4k4Hi0XoxOKp22FdmBOTu_cOzcQ2rB6tv7TAT62a2jJmH84HrToawD4yTnXAjuHJpmCwKDmAns8kopx8UtSa-5H7e3DA95TyDw25FdG9naiOMTGUdJn7yMuWrQmJ2a_flNf1z6Ip4nHonNm5xL7JAbFVCwy8H8fvqb5vIbrAR5r67NTNiaGP1bf8HPe28CsfRtvcuIlIcygPqOr_JmOX1AX-Sf6DNPmk1nHEtjQMdkywIgQBBBVb84V7EicAP8Oj85m9UfFAfMoBza5Z6znBgdE4ypH8TnWXkuAe9ZdYtdrGouM5f99McAEf6MjIgDPlWiuN9VmhSXZUeoia6KzU4Xl3haX2tXnG8zwQl9ZWxVsbx-ayUtS-TEhsmRVJu7G4ppDJ4DJ6ez4o9TmdyHVSaGVKI6w87-eYW_xlFGfYAoTUPuNkUVlQewX_eHpRP8SwxrZvahzDj5YIoROovBmKsQzIgtlJMD4BLJxqL-IrIcOlgJynjFib-OVamJ4kGFqpvAVYUJb-HUWrn4iMdR9ITnhmdgv512g9hNyrKsc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=Avqa98VMk3owOAW4yX2lbe7CLmgLFDtOpwhb2PGwMg-zDiKqE5rdLUyT626yOFfIrF5Od5r8yDGlo-hm-9qSDK6Mdh-ibOcdRPMp-4WwenbIrCg3PfGHH35Or31ELN1iv8FF4k4Hi0XoxOKp22FdmBOTu_cOzcQ2rB6tv7TAT62a2jJmH84HrToawD4yTnXAjuHJpmCwKDmAns8kopx8UtSa-5H7e3DA95TyDw25FdG9naiOMTGUdJn7yMuWrQmJ2a_flNf1z6Ip4nHonNm5xL7JAbFVCwy8H8fvqb5vIbrAR5r67NTNiaGP1bf8HPe28CsfRtvcuIlIcygPqOr_JmOX1AX-Sf6DNPmk1nHEtjQMdkywIgQBBBVb84V7EicAP8Oj85m9UfFAfMoBza5Z6znBgdE4ypH8TnWXkuAe9ZdYtdrGouM5f99McAEf6MjIgDPlWiuN9VmhSXZUeoia6KzU4Xl3haX2tXnG8zwQl9ZWxVsbx-ayUtS-TEhsmRVJu7G4ppDJ4DJ6ez4o9TmdyHVSaGVKI6w87-eYW_xlFGfYAoTUPuNkUVlQewX_eHpRP8SwxrZvahzDj5YIoROovBmKsQzIgtlJMD4BLJxqL-IrIcOlgJynjFib-OVamJ4kGFqpvAVYUJb-HUWrn4iMdR9ITnhmdgv512g9hNyrKsc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=VcwsbLDZLTfJI9BRHtQ1a3AF9zNmgjpi8Y9c6DpUV3wiS9CRdj8hc7cgedZU3vZzG-nPE-EAeNDRvZ6NU-K9PQyawq6tZo7XU6M_HYYpIzPaQgWyI0WEMxPeBVyLZq2b-RLYHJ6ZCw5UuK1UB5reKnJ3hVgUuPU8nL_D-Bgd9Sw_v3e3lrTWize__8FKI-kMttmwFIhRxuEh1ViqL0Ple2IH1X8RZ7fROdkpmEoOWDG84SR8anSyRx6wbYMzXz3Wu2VPJzJ6FWvy7oT4KVz9ICtNyUy6xs_XPWYflcvvWXeKkqlfrZIMgyf44j6Lco_e66JMnHwlks_A6UK0otPZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=VcwsbLDZLTfJI9BRHtQ1a3AF9zNmgjpi8Y9c6DpUV3wiS9CRdj8hc7cgedZU3vZzG-nPE-EAeNDRvZ6NU-K9PQyawq6tZo7XU6M_HYYpIzPaQgWyI0WEMxPeBVyLZq2b-RLYHJ6ZCw5UuK1UB5reKnJ3hVgUuPU8nL_D-Bgd9Sw_v3e3lrTWize__8FKI-kMttmwFIhRxuEh1ViqL0Ple2IH1X8RZ7fROdkpmEoOWDG84SR8anSyRx6wbYMzXz3Wu2VPJzJ6FWvy7oT4KVz9ICtNyUy6xs_XPWYflcvvWXeKkqlfrZIMgyf44j6Lco_e66JMnHwlks_A6UK0otPZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=UzCQmD35PjRFCKYtQY5ftZGUP13QOdMy6RzwhtdfWOQoc631L8aWVf4MzNHckAuLuS-em_rRKkuqPzLpfxqWV_nJD7NP_aT3wq7NwzxgEMXdNBi2_uGJt4VszaF5HKmLbdc6Eb9aLIROexU0VizCfFltbvtuArP8xgTzbeGS4qbNrEHW1Qyc714qD4tMQscKGXbGwJneNQ_0v-sgLmuNkYEk2_f7e-wkB_kyyYE-deI754XVaH2uVrXd8GVKSRXhCi4cwyXB2ZD5Swm3g2xUNCrLCwy1_4asHnkIaFvBltxP1dPREaz0uOnS53DdKxILjLKqm611ijYpNS8HL3DsIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=UzCQmD35PjRFCKYtQY5ftZGUP13QOdMy6RzwhtdfWOQoc631L8aWVf4MzNHckAuLuS-em_rRKkuqPzLpfxqWV_nJD7NP_aT3wq7NwzxgEMXdNBi2_uGJt4VszaF5HKmLbdc6Eb9aLIROexU0VizCfFltbvtuArP8xgTzbeGS4qbNrEHW1Qyc714qD4tMQscKGXbGwJneNQ_0v-sgLmuNkYEk2_f7e-wkB_kyyYE-deI754XVaH2uVrXd8GVKSRXhCi4cwyXB2ZD5Swm3g2xUNCrLCwy1_4asHnkIaFvBltxP1dPREaz0uOnS53DdKxILjLKqm611ijYpNS8HL3DsIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W64Od_SZ5wJYCvmQhcgaYkeSEdcdtkX6d-L--jlfUtSzKwePYb8PXEO7AfpS3OfgWwjqoAsuLYFf-lfoqjqN5JRuJnhi5fkMzW4OC48Fwjs_IyYYJ_HLnIhaulSPQuTVcozdNDgIBicSFBhvyllSC0lMJa55ocvmN0nXdn8FW5-QARzuGqrqZcOHn1JZ1xIGaNyqnZLCSxh8rSMNYsPr3rM5ISY5dFlXnO3Ln_z_tZLiPs3eG-MlfPUK05wtxv7Zu2vLRllP1Fll0hgPPtwKQlm9njn8Ae53PFDnoFVLL3SqrBFpbKGVSb6oVNaooyzLwnzIyuFocQbDW5i01fabNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=tcoDVNMaTCq9gE6oS2hoeIZW-DmgIpRr_GCckMRNw9G11GCtixa9me7CMAlc7zcFT6cut_YvgFQU_mXBBV4JE7eekI--t8t8cypHF71XRCYcg1L2xC6uTMq6T2gFy2v-eFSsGqk4CDQBP4gUCdyHDMw3wEGNOqNjZxAaKeKALY1yTsldFc2gyfceMz5X2f0gmpIufDw3SjeIXxJtDqL8W82_R-46SJOIVhERpJNfxIIyoWEZ2Icwvsbc9GLQWiD_h1OZ--bYj4aC9N6DFDWRAgzMbkdlCrZG-b2m9F90DoDlq_g_9naHpaa8quCEmLesr3M45zEXnCjcSW_KxD4ndg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=tcoDVNMaTCq9gE6oS2hoeIZW-DmgIpRr_GCckMRNw9G11GCtixa9me7CMAlc7zcFT6cut_YvgFQU_mXBBV4JE7eekI--t8t8cypHF71XRCYcg1L2xC6uTMq6T2gFy2v-eFSsGqk4CDQBP4gUCdyHDMw3wEGNOqNjZxAaKeKALY1yTsldFc2gyfceMz5X2f0gmpIufDw3SjeIXxJtDqL8W82_R-46SJOIVhERpJNfxIIyoWEZ2Icwvsbc9GLQWiD_h1OZ--bYj4aC9N6DFDWRAgzMbkdlCrZG-b2m9F90DoDlq_g_9naHpaa8quCEmLesr3M45zEXnCjcSW_KxD4ndg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=JWQNdppxYsB9Db1lUWt7E7AsvnkyYh8-clLxPirpkmTsdvyJnsIDbt_XOBTC2VtnlNat_KtpnnyTDJjcB1DC4p9-SELONvWeWEpCze1aks4u9NjD9WytcLEKquJZnFopxD3zX_13CxgCAzOQMB7k1hoqeyEXWIRgZNpc8WpqGkRd-QuT7dZZta2pyjSbs-HJSf_naBZ0NIUD7untoyeDqJDvik6jk0e2rgp4LuBQoIJYV9m7jQzWGUncBoBl25C3i3_2GudAIE10zG8bluqhLXUDmtNd5cB7x78J41MTJ951GUqDieyAO_FDfAH6Kxrgk0ROkdXKnJBsDwMl8JokXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=JWQNdppxYsB9Db1lUWt7E7AsvnkyYh8-clLxPirpkmTsdvyJnsIDbt_XOBTC2VtnlNat_KtpnnyTDJjcB1DC4p9-SELONvWeWEpCze1aks4u9NjD9WytcLEKquJZnFopxD3zX_13CxgCAzOQMB7k1hoqeyEXWIRgZNpc8WpqGkRd-QuT7dZZta2pyjSbs-HJSf_naBZ0NIUD7untoyeDqJDvik6jk0e2rgp4LuBQoIJYV9m7jQzWGUncBoBl25C3i3_2GudAIE10zG8bluqhLXUDmtNd5cB7x78J41MTJ951GUqDieyAO_FDfAH6Kxrgk0ROkdXKnJBsDwMl8JokXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4SAfKPea7VfhXXPVOoRIstpIsdCxQeg1wDukwfBvid6In-PSWpDt20x5ifqNj298Me_BwII6NRFuG55qlRjgP1SR0rmAhdH7egAzeEqTxot7zRFIWCl_bi9rpmHg08_B7h5IeqJ0ERE4LoIZ8PAYz7szsobYg_1BYlMF2RYGZg3Gys40f1CxQCucLwRlZh3xiKsVql0qCIabBupPwoHEoMjFo_iLmOulckW-LZHE6XNPWlQ9W_oyarjP61G2jovONJZuIJh0sifq5ZXeUkwSZDBkJmyi9MnXONQg-CcgRi8PqXP3pHzUw34lpARrT2JQcogxJqG6kHJQAkhHzTZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=havTLMgvVtP5KZfC4s5h_EFtwkHkSUD5dZ_x61RcCBuOR30q2awLt_g30fV04S44vnH29uS_GBdoeO0rpSlyQNUBhVMn_eFPRHU4cu3wzZKB26GP5mn7QHCXmu_nQx-p14m9R2VRDXLyDpRlxFenH1IxixthEqIjXLFhS99gjPAMWoff6gR5e8vfdouLqGfHMg127q1JPB6_t7ol2cuUFPXcHPil4xiuuCwri9w4CNGH4KUyXu2ebsLpHWx6lMuWMJ232FMg2wxQ4RVDdAp0R6RfBJeW_5XPW_VSZoMTC3bZ0lrx3JogbCE0Gl-E7GmLfgC_8HjAB347zZDKFwTcpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=havTLMgvVtP5KZfC4s5h_EFtwkHkSUD5dZ_x61RcCBuOR30q2awLt_g30fV04S44vnH29uS_GBdoeO0rpSlyQNUBhVMn_eFPRHU4cu3wzZKB26GP5mn7QHCXmu_nQx-p14m9R2VRDXLyDpRlxFenH1IxixthEqIjXLFhS99gjPAMWoff6gR5e8vfdouLqGfHMg127q1JPB6_t7ol2cuUFPXcHPil4xiuuCwri9w4CNGH4KUyXu2ebsLpHWx6lMuWMJ232FMg2wxQ4RVDdAp0R6RfBJeW_5XPW_VSZoMTC3bZ0lrx3JogbCE0Gl-E7GmLfgC_8HjAB347zZDKFwTcpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=qgTN4w4JmnKlAo1VMvzOCIVXujN3AZ95yh70LRdJEOKM3FkTR67xYuPYehUzWOhysiCD-LBJ7oaTNtU52JKDg3JCiq-GhIuxzjB1ZZH3rRQuGJNHgp7wVkslQ8QR6nHAkRLxN3B89q5j6oiwt48wZob20u3rKomNNYCdhzmEGeb1oh9zngWQrTsCdLkvc78a8VTb1fB4eaL6S_gMneevipz_ALuqCiANV-FsNL1clNv_pwkciAiK0HLbNGBNMow9CL7mnjRb0LdraTI5PXl66TU8LkZFu-BV3XNi1VN_v-z1s4lPqwytKHwh3yYdT9MxXRCYICu6hT6HgfxGpackPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=qgTN4w4JmnKlAo1VMvzOCIVXujN3AZ95yh70LRdJEOKM3FkTR67xYuPYehUzWOhysiCD-LBJ7oaTNtU52JKDg3JCiq-GhIuxzjB1ZZH3rRQuGJNHgp7wVkslQ8QR6nHAkRLxN3B89q5j6oiwt48wZob20u3rKomNNYCdhzmEGeb1oh9zngWQrTsCdLkvc78a8VTb1fB4eaL6S_gMneevipz_ALuqCiANV-FsNL1clNv_pwkciAiK0HLbNGBNMow9CL7mnjRb0LdraTI5PXl66TU8LkZFu-BV3XNi1VN_v-z1s4lPqwytKHwh3yYdT9MxXRCYICu6hT6HgfxGpackPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=tfJ4CHZiFRprmNelLLVeVVaJSx79qafc9eLKlpF5NCYMzGPPI1nNF0SrjYnrwoKS8btyjuRYzMaMsOgxDs8m3OHUTAgk5VX-K1rUziwDSDZyC7PGmGt1iJe9WEdFXdF8OKoooD40PC23-k8UqtLyzbNZZDfQ_hLi99HK0Cz1j3v3OQ6_NPaeS_hbgF62xg5bXNkIieLJvcjGbrvGHpuGVzu9V6n4sutn510xAOdQzKZRw-WQNTtthyO437860wGgI79T9S0OEfeCHCsaBSOg97kysLuqMA0I0C6hTLaoqsc2_pXP8YTLOGTiTP_tl30F86zLmuJtCH5XNBKhSXo7wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=tfJ4CHZiFRprmNelLLVeVVaJSx79qafc9eLKlpF5NCYMzGPPI1nNF0SrjYnrwoKS8btyjuRYzMaMsOgxDs8m3OHUTAgk5VX-K1rUziwDSDZyC7PGmGt1iJe9WEdFXdF8OKoooD40PC23-k8UqtLyzbNZZDfQ_hLi99HK0Cz1j3v3OQ6_NPaeS_hbgF62xg5bXNkIieLJvcjGbrvGHpuGVzu9V6n4sutn510xAOdQzKZRw-WQNTtthyO437860wGgI79T9S0OEfeCHCsaBSOg97kysLuqMA0I0C6hTLaoqsc2_pXP8YTLOGTiTP_tl30F86zLmuJtCH5XNBKhSXo7wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=R4WaB1kGKQbFewmbRY5fjQvAxU81PL_0lafpUOlAnnh4ZL28LaDeCSdF4WSjPyA1wFjwYTobBWmhXfulOyVm_F90AGKAqaxh5eyBhCMYqY197Uqt7YL2wXQduFRt4cvqvKMC1glkUBMRk1SsRFnWgt1zcqHBRzL0c3yXW6A_aR8BpRq4nN76XnIlINanamgNFTc5DikXQhXkQfy9GOX-AJqcLBmruCzg1ziADLgwtHd5SPpP6tS92KDd0wG_9i9npbYMeIxYYEOwlRx10vSUVHdeOvkh-HykDGcSvD7hx0cWLgGaTmkGVNzudlU4gbVkyKrBVdHoOQ-xtWqKNhLwjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=R4WaB1kGKQbFewmbRY5fjQvAxU81PL_0lafpUOlAnnh4ZL28LaDeCSdF4WSjPyA1wFjwYTobBWmhXfulOyVm_F90AGKAqaxh5eyBhCMYqY197Uqt7YL2wXQduFRt4cvqvKMC1glkUBMRk1SsRFnWgt1zcqHBRzL0c3yXW6A_aR8BpRq4nN76XnIlINanamgNFTc5DikXQhXkQfy9GOX-AJqcLBmruCzg1ziADLgwtHd5SPpP6tS92KDd0wG_9i9npbYMeIxYYEOwlRx10vSUVHdeOvkh-HykDGcSvD7hx0cWLgGaTmkGVNzudlU4gbVkyKrBVdHoOQ-xtWqKNhLwjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=UEovQe_WUQWuizmHNeKRY4Mvw0y9etP4Ho63skPyP71z9EhQMIHAdePqxciHRNaOXwxxCSs8t3WQez2Q9S7iwNKg7SkSr3oL5G1Upq-LKO6FxL4InGRYYwttSAJ7REoChGhL0NxzZBuQTnmfbJJ0ESVPCDKOFuQ8l0jNNl-HxnE03kDHHHPSLPt0AzTJ402x1TEUpLrQima4XTq3TfGq38pBLdZZSEKvX7IRxowGc0E4-uyxhRwbhhIvkqslcCseCuO8dm63MoI260K-MMffrn-erJjq-uihfPLHd-81NIkTBBRG5-78ryAEJshwQm4uPKMl4GcKfHzMSMt69tRIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=UEovQe_WUQWuizmHNeKRY4Mvw0y9etP4Ho63skPyP71z9EhQMIHAdePqxciHRNaOXwxxCSs8t3WQez2Q9S7iwNKg7SkSr3oL5G1Upq-LKO6FxL4InGRYYwttSAJ7REoChGhL0NxzZBuQTnmfbJJ0ESVPCDKOFuQ8l0jNNl-HxnE03kDHHHPSLPt0AzTJ402x1TEUpLrQima4XTq3TfGq38pBLdZZSEKvX7IRxowGc0E4-uyxhRwbhhIvkqslcCseCuO8dm63MoI260K-MMffrn-erJjq-uihfPLHd-81NIkTBBRG5-78ryAEJshwQm4uPKMl4GcKfHzMSMt69tRIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP7BX9nmZh5Gz--e3B5nfBfy25BQc0EkjEw994cmIg0b6PFtFUI3OiyEYcqLgF01aA6FpFramkvCNo0dX_Jkizi6JA7TGTBuDVWSQwkWNnAnhDm5ZU7_01OUPWeXMQjY-GthYhHKDOZtG2CLP23tnEn8ltqWE0T0SKW52KlJ_zp7eLw8ZSeq2URdHIesV--TXCO5qAiNi_QpXOeMHK0hSPUGF_OwxVF45twoslE7J2tWD_kcNDiUpGObujbnNuRpEnvL00jQoA3oCOaZ-zHueiOfkuzr_3e-X1az03X--XjMm8XwMySKO_5pIoqiGW5Nlx857Rp8bZv895r_PRJwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlD_IVhmn1R-BFj7FmFtYOx9WlexVZ5KCVOZZw6xnDubsEREr08lNWsDc11NI34-q_jTfwtjg-ELK2sQAMNzL39kZUWHh1m0N8PVQqn6z4h03nQNqnhdIkc1wO9dIWa-8D0YLOXy3rzMIuH5QotW6rQzIX8oRe1vIugTOdsfSzU21P3tTUIYRwhWIQRbUrU-aID37Nq2zh2O-c6cuRqE4oTIPKG3AtmkyMU0vjvab1hOKlC-l2T3T4V0rWsmCA2rjRprgpDlv28BcAPpUsrB53GsLOkPFU_UORlW-LhYHBF--eduEPCUsmVBNHNU-C09fiZd-0uE4LfSvGsFr1GBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsfquuKAyFr3YxjqWisQbtke6wE9JzG-Sn0okVmLdpCeBA5E5DuQtSAcS8BCMOMFvTXqvRzxzN5avZFVUA5F9W9UqPCZkzOXTLShxE3RG6XD8sfclUbMgw3gcUeC7vpnVxwHlf86DVAeuVVe-X5rVljg2kqDO4igWBohlLlnikdXjrEvs37FMMeu42x7R3iYFtFmEFcvHk6eWJh-gDXJtAanRJYYiPzWaTRDfTFvL-fPkWhLocQar_Chg852g6lkfTlQ8l3AOGnf0HpUDhOZP-EXpnUJDpAFkiZibQ2pQ9dHu7rm9D3a3UaXWtWo_adM_unkkLhWgjflAtY9z3QViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKhQvMIbCA-m0JXoJIySOh1pshf0TZ7P4hMaN_ClIf3PRtIB8SFY7LKomRVbsuCceDfvqdJ6GK7AzbFgLF_K6MTK4i6TJFHoho0lws-KwKckNjw0Ezm3Au2SW2DvdpA3mxdWFt9U6e7E228Yvn-kGYg-Pm8nNr_PjtbbySHSkrGNs3Bepyzd9a8nniOQTuYaKC1YUYrAfRSUxRTnGwv60wfcA4P79v-oJpselipjuqEwF92iSZHczJCrQUXa5EEGGBDbKVnWIc4R2XK6jlEvdBzG1x3zAzduzhLCDBoXKuvTLwXd8hVNzcGYkSne336GuRwjlLEOsc3LiEyyTS3W1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltp1jea5pKwLjMQx9D3vdr3C55SScvhzX5V61XT5pj5mnsIiDypL_eIuHfwEUnpO-M5clnLNZ0Q4qfhTEOPOTwF4ng6tLv9tL_EZsWr5W2Te-BzP4tziCCxLmAb5kwPlXJT4NOTVUsYlqtBSmVsBj43vvYt_pnykqCVhjKJ9YVSqtr2LQXk6aHTg-7YxsWr4qMo7S03Rde-v-CA8VidQbEQjRUFqT8StxrVSLRlgko_z8a8nlePLGWkhVakKHvLMcZY6lQ3GMxxt-YHYCiPWXsX5zFXBUvcogo-J5t0G6RGWnsD90ClCVMcS6IvaYMbrNoYD2EqGyyIwiVuvHRbmLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMokyOJVioEa9qpw2kHVsXXuqmrtZq7CrAzuz0KNACYPDNXg8tciJM-EIG3lWd_3KMTDaWt7W-StWaWylVkyo4HcQgUINpwzVOJFO6IZDtDaPgA7S416MZeBGtOMB6FEZ3EhGM1N4TSMMt55j4R4sadjSrkBCYvytBPjxsxrjTRSIKxsOZIF-4Gn2VQqA-ZCa2r61JmPChX7nYqMXqAylrVsu6LIbUu0n-TMvrF_dWXI9mz-3yZ9HGzfoC8x8FSwQlwRawY_j9KFJEIWZloSeGhGmVPYHt2iPNVUOLmaMN0XvDwxV6IeOtSg822--9nj9iknBwZRZj3R9YQSLuEhrD3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMokyOJVioEa9qpw2kHVsXXuqmrtZq7CrAzuz0KNACYPDNXg8tciJM-EIG3lWd_3KMTDaWt7W-StWaWylVkyo4HcQgUINpwzVOJFO6IZDtDaPgA7S416MZeBGtOMB6FEZ3EhGM1N4TSMMt55j4R4sadjSrkBCYvytBPjxsxrjTRSIKxsOZIF-4Gn2VQqA-ZCa2r61JmPChX7nYqMXqAylrVsu6LIbUu0n-TMvrF_dWXI9mz-3yZ9HGzfoC8x8FSwQlwRawY_j9KFJEIWZloSeGhGmVPYHt2iPNVUOLmaMN0XvDwxV6IeOtSg822--9nj9iknBwZRZj3R9YQSLuEhrD3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=iQzjCw9RxLJsMz5viZM0YiDFQAwKzwBa737kiM-QeTQJLqd0LaF2msIaQye9Dnqe0-IzMr0kGXbY46yfAw8EOUqUALG8u7-Ckxz3H7ZPBUsGPOY2CmoFDMxhqI5wqQ6bVJXiFJd6kD4_jgZ300JyDVHhD8LygRn3g2_EokcqtezXX2fKzf8FenNZna2CvfjcJhjuFfq26OxfSCFoGgyPnWZcqPdG6Aa5W247qkW-CjABl6g4_d-4CY1DcMKPRlFm6MOf5CnmUqORAU5B-s7NqXl3hBL-OPyaYLj2rSPwtb0O0gL5QhFGg_KsDpXgjdEszt0cXU4_f2p--wNpNZAyhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=iQzjCw9RxLJsMz5viZM0YiDFQAwKzwBa737kiM-QeTQJLqd0LaF2msIaQye9Dnqe0-IzMr0kGXbY46yfAw8EOUqUALG8u7-Ckxz3H7ZPBUsGPOY2CmoFDMxhqI5wqQ6bVJXiFJd6kD4_jgZ300JyDVHhD8LygRn3g2_EokcqtezXX2fKzf8FenNZna2CvfjcJhjuFfq26OxfSCFoGgyPnWZcqPdG6Aa5W247qkW-CjABl6g4_d-4CY1DcMKPRlFm6MOf5CnmUqORAU5B-s7NqXl3hBL-OPyaYLj2rSPwtb0O0gL5QhFGg_KsDpXgjdEszt0cXU4_f2p--wNpNZAyhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=G3pHq0SPH90Pkl50BLOVyfhBYMrbQaLlo5vaMKzrZrq966Lp48SH5qkCMvMpRNnwMunXJPAPZGdjsYfhk-5TZTICLiD8M6ASAaC5-UhcUvC96zH26TyBc_hkf1RU-MXUHK7N2dtWGUuoM4rAY50H4AlFiEkE598GIHDRppFIDmvEEvbJYhAcdokQX05tMspD1-LBGMFX042WDtKAMDrpSWp-6BIJ1ZC3R_FIjkd7O_ljqIKMtZMnDVIKS60SLUY24qmolrVQrRbh1_j7Ce5EiMGL0fF7ZuBENWZLGmr-wgUP_5Pemaiuxp22e-La08FPpiRqrpNOyrPAqKvLQf2qQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=G3pHq0SPH90Pkl50BLOVyfhBYMrbQaLlo5vaMKzrZrq966Lp48SH5qkCMvMpRNnwMunXJPAPZGdjsYfhk-5TZTICLiD8M6ASAaC5-UhcUvC96zH26TyBc_hkf1RU-MXUHK7N2dtWGUuoM4rAY50H4AlFiEkE598GIHDRppFIDmvEEvbJYhAcdokQX05tMspD1-LBGMFX042WDtKAMDrpSWp-6BIJ1ZC3R_FIjkd7O_ljqIKMtZMnDVIKS60SLUY24qmolrVQrRbh1_j7Ce5EiMGL0fF7ZuBENWZLGmr-wgUP_5Pemaiuxp22e-La08FPpiRqrpNOyrPAqKvLQf2qQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=Xj34HsVSaDCHInDV2wFoYHMW2S3-r2ocPPNOr64dknnqx6rf_KV849amPT05f30VRhLhbMF0GzsSEkVpfXzzi8c6L5_8kcqidH1WltaSzG87GSlKqU_7DpOmzvhozU6YNtTmyP31wginD_hNXRbc8y7b1iLJVxa1YnFtjMciqkK6D231S4GywPJm1vQTEL9hX1kt46SIyxUFuZYvK4pYzMklHzFN5d3t2X9BR0W6jOAALRxGi7e1dM-LwrnhTkqe0uVv9B9gf3_Lfy5Gza7FhavZ4_D00X0Il4rlszT7fHnBBuh45kLfQHbVTn2XldL8uu654WHUMwJDupKQ3eJRKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=Xj34HsVSaDCHInDV2wFoYHMW2S3-r2ocPPNOr64dknnqx6rf_KV849amPT05f30VRhLhbMF0GzsSEkVpfXzzi8c6L5_8kcqidH1WltaSzG87GSlKqU_7DpOmzvhozU6YNtTmyP31wginD_hNXRbc8y7b1iLJVxa1YnFtjMciqkK6D231S4GywPJm1vQTEL9hX1kt46SIyxUFuZYvK4pYzMklHzFN5d3t2X9BR0W6jOAALRxGi7e1dM-LwrnhTkqe0uVv9B9gf3_Lfy5Gza7FhavZ4_D00X0Il4rlszT7fHnBBuh45kLfQHbVTn2XldL8uu654WHUMwJDupKQ3eJRKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRHce6UvohUCqjvy5rAFVFn6KsGu6_IbQqKpAZJfW4YYYYOWVS_awEqtqaui2gLVlRd0J0my10a0ifrwwzd3argWXwMol54yDtqu_SRwI_5-Q5-w0QdpOI6KvJX6WqXNqqnZ-CKWJTuRhRMFW1mjrN3E_D2sdhH6r8OeU0j_ioHUKe-nf5tMjpA7g5619XvQwlroE5bHwcjY3A891YGC6UYcblaKSoC2o-o0g3AME-kWYCGsl0-C1kmSYOY4A8epsjpnEpJd0n7AO_JvReGLs1IUr1J9-8Df6y6IYu2ckgRCEhTcXLnEtJwrgQl3uptLPnddHhKjuflEHNHErV0zeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=VyND3NzBUTGZnPGmqAbraKQpMg1As4uKBYalC0QmCWkqYTT2oDXgEiGb616jJ3tSX6huOmtwECrCfTwr-o3QotsH3GlB8pcza_zgpnDNMUsFTKAXh6unXjO9G6Jrjo0-9a03D6D_oo3dwWHdExxkZMibdj6oGs208hFvIU7_J7DAExEb3HQP6ilsmFoBO2Ij1ZIbeqL_8b_57Y5IUNeBmW7EJS_yai6GrcaDVE99fW6Jg19VqDrhL55GqPLz7Sa6-ydnEooawf8Sb877GftackAJMP7uKmCAwSsz0RV7xtiZ_MSqbtw50vD9grfBib4aaLtp5l41Isu58IBOWJBWqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=VyND3NzBUTGZnPGmqAbraKQpMg1As4uKBYalC0QmCWkqYTT2oDXgEiGb616jJ3tSX6huOmtwECrCfTwr-o3QotsH3GlB8pcza_zgpnDNMUsFTKAXh6unXjO9G6Jrjo0-9a03D6D_oo3dwWHdExxkZMibdj6oGs208hFvIU7_J7DAExEb3HQP6ilsmFoBO2Ij1ZIbeqL_8b_57Y5IUNeBmW7EJS_yai6GrcaDVE99fW6Jg19VqDrhL55GqPLz7Sa6-ydnEooawf8Sb877GftackAJMP7uKmCAwSsz0RV7xtiZ_MSqbtw50vD9grfBib4aaLtp5l41Isu58IBOWJBWqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=EbRioeAZiZ6uZLhX76YIBDYA5AfY_Umj96O4YyTwEJF1FpCqMi9KzPgqta-3k5rQSjPlvRkkGgxFSimi9_heuiRjQ7-4QQ9sEJvXkWACE9Yqjxgq1BrU-PNAwCEBVoUorYBRh6FWKp76izgMPavn_JB-NTsx0ur5TAq3m10SpKWxNIYBB5rENK3tRcCnXgXB6hGgLjx06A4cmoWUYlsFqI5Elu6oG2h2uZUKA939pYEcy9ZrP6tVFGY31ywit4Xge8hIoN3feU0ImxGHXEesyabSr1ObRuSPBeJcfUqSBQqJElLwdZPfgZfNVBgvzVdg8osq1Y5y_x2s3bEUWp585Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=EbRioeAZiZ6uZLhX76YIBDYA5AfY_Umj96O4YyTwEJF1FpCqMi9KzPgqta-3k5rQSjPlvRkkGgxFSimi9_heuiRjQ7-4QQ9sEJvXkWACE9Yqjxgq1BrU-PNAwCEBVoUorYBRh6FWKp76izgMPavn_JB-NTsx0ur5TAq3m10SpKWxNIYBB5rENK3tRcCnXgXB6hGgLjx06A4cmoWUYlsFqI5Elu6oG2h2uZUKA939pYEcy9ZrP6tVFGY31ywit4Xge8hIoN3feU0ImxGHXEesyabSr1ObRuSPBeJcfUqSBQqJElLwdZPfgZfNVBgvzVdg8osq1Y5y_x2s3bEUWp585Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=F6HyvQaVNL_2x3EqXNYZHPj9IA8X9rz6WeSJg6b57FC_y-E-cmolgtUs60nnj4Dn9-XdrvlAlMjrwYbDIKjRoSINw1dAu1r7A57aPHImUNkHNzTJVjRzRgWbB1L7-Xx9e6pZwg0wDGGEV0UkGZIV9b8iPYd9i93ECEKqNeAwTAvY6jvPolT4xrs0ciEy78X_ELyrEy7wZj2JP-u4Ys0IVrcgz3i8_LL93vEH9eI2_FFSwkp3r7k3PH5x0I7pHoo18GnvRyr3pmlTDWXPF6mn5nJNYyBBU2gtji4TfUPCWl6YW9H5DwgB2orkyRzmpyvaJjg0f3GtW-3vmt_1CwdG4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=F6HyvQaVNL_2x3EqXNYZHPj9IA8X9rz6WeSJg6b57FC_y-E-cmolgtUs60nnj4Dn9-XdrvlAlMjrwYbDIKjRoSINw1dAu1r7A57aPHImUNkHNzTJVjRzRgWbB1L7-Xx9e6pZwg0wDGGEV0UkGZIV9b8iPYd9i93ECEKqNeAwTAvY6jvPolT4xrs0ciEy78X_ELyrEy7wZj2JP-u4Ys0IVrcgz3i8_LL93vEH9eI2_FFSwkp3r7k3PH5x0I7pHoo18GnvRyr3pmlTDWXPF6mn5nJNYyBBU2gtji4TfUPCWl6YW9H5DwgB2orkyRzmpyvaJjg0f3GtW-3vmt_1CwdG4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=U-d356IvuLOGKddkE8zyIEkqKaeqlLZtBlBZ_lv5kmYWWQMvwKo1FsHiQogEiGSG7JOb1Vyt7DqBVdEmBaDvX4FhoFv8VHdH46_9hLmFyeByPCHFxwF-BYINJ6eA5VWqC2x_RKepgpYfVI95NhN2dbsVknCscGNrasYxvpIh1x5ebW8iHdSTXU65Ttnbx0vVGDhjQ8awRnKuaA9PAKQ9ZQMUv1jPi-fKcTQLYS9-6IIMy9nx0jun1sErnfuGquCgcaz1_WnbXfNvPT9ArvYxk_gi4KYWDfpGxtsVZlpMQ8u2fgOKbeuetOxJDnG2TPHrJxUzD-G3TNS8V73Jq9v6VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=U-d356IvuLOGKddkE8zyIEkqKaeqlLZtBlBZ_lv5kmYWWQMvwKo1FsHiQogEiGSG7JOb1Vyt7DqBVdEmBaDvX4FhoFv8VHdH46_9hLmFyeByPCHFxwF-BYINJ6eA5VWqC2x_RKepgpYfVI95NhN2dbsVknCscGNrasYxvpIh1x5ebW8iHdSTXU65Ttnbx0vVGDhjQ8awRnKuaA9PAKQ9ZQMUv1jPi-fKcTQLYS9-6IIMy9nx0jun1sErnfuGquCgcaz1_WnbXfNvPT9ArvYxk_gi4KYWDfpGxtsVZlpMQ8u2fgOKbeuetOxJDnG2TPHrJxUzD-G3TNS8V73Jq9v6VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=ZXiDpJlPoxLl4OwWKS4Uv8wyKcoKu2h_EZ0G3_LyKRfLqvIMYMf3AaC14DECCkvNc4LDikHJPE3D_cQxruCBKA6WGHQzlmtvM8LVW54QCfosQjb0lwSr_lpiHTA_eVumW-AELpwg3b1qUYEljjyGbuhimgEU3SefEgDc7Sap2HqshQXzTfqYjXcvqhjFJDObji7BhJVKXprBO6-2Mxx3sa1etBthIcRC3ybXna5JJqw-F_kE8lWB0KZSWu2lPo0deWnmt-puYfHxQ34xuPINQDRRaKLVO_rwH9Kmi9Hp94MghcKiABQ-xeuBCR-erHwrul0WpwyGNqxjDUhcWAz4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=ZXiDpJlPoxLl4OwWKS4Uv8wyKcoKu2h_EZ0G3_LyKRfLqvIMYMf3AaC14DECCkvNc4LDikHJPE3D_cQxruCBKA6WGHQzlmtvM8LVW54QCfosQjb0lwSr_lpiHTA_eVumW-AELpwg3b1qUYEljjyGbuhimgEU3SefEgDc7Sap2HqshQXzTfqYjXcvqhjFJDObji7BhJVKXprBO6-2Mxx3sa1etBthIcRC3ybXna5JJqw-F_kE8lWB0KZSWu2lPo0deWnmt-puYfHxQ34xuPINQDRRaKLVO_rwH9Kmi9Hp94MghcKiABQ-xeuBCR-erHwrul0WpwyGNqxjDUhcWAz4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=EuC3yIUU9CZ9zykKb7qUUa7t0w2wyWSi-Crq0PDO-oSjCQT8-xYz5mAJNdmZZoohS8OYN0nsIKkqBTEy9yPXNaj4Xvq9GRqE_0x5GWx3foc88PdF7Mm69jErphS19tThRT-Rsi-6GvJl1L0jBrhomCnsJAnKWLZzvIcUNktVM9LFfc90NdgzRLPSpn_Kjk4HCb-s5neGXjO-UitSewBkmgjnvCfNrGoL2EIED2qxSELiATf7J_4fgf87mWs9ZXmOS9wTPRfjpUDT_jx48s7hDkMlxukm9zAA5yYFDwnY5QvrmmIo78Xpk6H_3lDLE7pPGc-1LAz5CRra81UIp2-HqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=EuC3yIUU9CZ9zykKb7qUUa7t0w2wyWSi-Crq0PDO-oSjCQT8-xYz5mAJNdmZZoohS8OYN0nsIKkqBTEy9yPXNaj4Xvq9GRqE_0x5GWx3foc88PdF7Mm69jErphS19tThRT-Rsi-6GvJl1L0jBrhomCnsJAnKWLZzvIcUNktVM9LFfc90NdgzRLPSpn_Kjk4HCb-s5neGXjO-UitSewBkmgjnvCfNrGoL2EIED2qxSELiATf7J_4fgf87mWs9ZXmOS9wTPRfjpUDT_jx48s7hDkMlxukm9zAA5yYFDwnY5QvrmmIo78Xpk6H_3lDLE7pPGc-1LAz5CRra81UIp2-HqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=EiRwdHHiONlfmaZ7X48teSdaqVEsKZA_y88aG4uB22u-4-05GQuaBtITqNebnUOKkpRb09Ltt3ya4wp_5c7nXZsKbdXG5yRESrkNp3gNStI8-f7AlYWxjdWZJVEuid6M5HNbRUsz1tpkXZUnuzVh9PDxQam7JkULHJqlhFdu4JKhsbnt-5r6wbxfSGMtonr7lAfI4OSn36HmQlDhl0VB_eojdsZGorzhRz1k3FL3ZBfKrMkG8Rd3R2pzklX1DZQDku8QRG-W-aGA3BnnvbkWlR32kgZhmjgIFG2sux7YkL_hVvU3oUIo4XsTajbWoM-Q6a2EIMuzuiiMCVhv7l9u2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=EiRwdHHiONlfmaZ7X48teSdaqVEsKZA_y88aG4uB22u-4-05GQuaBtITqNebnUOKkpRb09Ltt3ya4wp_5c7nXZsKbdXG5yRESrkNp3gNStI8-f7AlYWxjdWZJVEuid6M5HNbRUsz1tpkXZUnuzVh9PDxQam7JkULHJqlhFdu4JKhsbnt-5r6wbxfSGMtonr7lAfI4OSn36HmQlDhl0VB_eojdsZGorzhRz1k3FL3ZBfKrMkG8Rd3R2pzklX1DZQDku8QRG-W-aGA3BnnvbkWlR32kgZhmjgIFG2sux7YkL_hVvU3oUIo4XsTajbWoM-Q6a2EIMuzuiiMCVhv7l9u2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=VYFgYl1D798TMTUza_ZKQVMAtbFLILwPPi7_-4RDwksHxVfjApVV0OQcLBiwXs4mjbYGRhh0euzRw5a8hncSj2DakMVVFrfVl_m4sJWkpcKHRtBvH-Gtnf2hEkhuCfRApezSXE75IHAMho37K9DWdO7WIcYVn_YYcIC2Zy9_8tpOFC3DyUVRwJUldKTdghutSZ-NAdBOiXvrVaHTAm1Gq4QwVNABNL59aqG_Vzait4KOAZTxt4E5x1K8OezU--YC7j8ktVK6PV6mZfaoW3lM4EjgNN6Jpmk7mc9gzSMkpU7ynRy9-9dzRGyGUGjfLvgVisJ0r5DHIrg3Ib10MyuQ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=VYFgYl1D798TMTUza_ZKQVMAtbFLILwPPi7_-4RDwksHxVfjApVV0OQcLBiwXs4mjbYGRhh0euzRw5a8hncSj2DakMVVFrfVl_m4sJWkpcKHRtBvH-Gtnf2hEkhuCfRApezSXE75IHAMho37K9DWdO7WIcYVn_YYcIC2Zy9_8tpOFC3DyUVRwJUldKTdghutSZ-NAdBOiXvrVaHTAm1Gq4QwVNABNL59aqG_Vzait4KOAZTxt4E5x1K8OezU--YC7j8ktVK6PV6mZfaoW3lM4EjgNN6Jpmk7mc9gzSMkpU7ynRy9-9dzRGyGUGjfLvgVisJ0r5DHIrg3Ib10MyuQ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=Fc6RpD8Q07DH2eJLj8BLYrhfKkFK5skiZLXYyNUPo-GnD-LwiacOqHWuaMjquyqAkcfqHteZ3-wsoABriIA7zxRUTvr_EuPawooAknksZ-NJGNE_uA9kJNMXIpj_-H9CaanoSZqfxlrAK5SXAbEvVR93cguT-g8o5FijFvpNWxHSlqnfBUQ7zlsTZbB_rz9RtmzdHxmd8zokkj0PX8Dz8bPeK0BPTQz8J9tQbFdKc6rWfHwKFCPJ03h5BJLI431zAQiV3jlrJhN6OPvLqV56ugCEsUqeThJo4fhvSOY0IQYSrCGyvVFMq-GhlCnU7FAz_lbnlkMOJNhL1Ub1ZQ7OUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=Fc6RpD8Q07DH2eJLj8BLYrhfKkFK5skiZLXYyNUPo-GnD-LwiacOqHWuaMjquyqAkcfqHteZ3-wsoABriIA7zxRUTvr_EuPawooAknksZ-NJGNE_uA9kJNMXIpj_-H9CaanoSZqfxlrAK5SXAbEvVR93cguT-g8o5FijFvpNWxHSlqnfBUQ7zlsTZbB_rz9RtmzdHxmd8zokkj0PX8Dz8bPeK0BPTQz8J9tQbFdKc6rWfHwKFCPJ03h5BJLI431zAQiV3jlrJhN6OPvLqV56ugCEsUqeThJo4fhvSOY0IQYSrCGyvVFMq-GhlCnU7FAz_lbnlkMOJNhL1Ub1ZQ7OUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=cEcNoH_x-QfdJcO_J77850ca_6q85NU42zTZK4xifuGZ8-oBPRr9Ys8izNEV1wpst1ros-Az6jFsPWKXU5S-4zI6-b6ISe1ORzWQC1mmQCLgqaeA0MONqKfOCkW9UKZwDXV3kP_R74ylJpl8q1yKJct-fdYQZqbSVeb2nt0i7xYcZkimLAm2vNQ-_FZDMaXoa5dWMGNO46yLfa5l0WaPDputMhEhXmF-3DnfDT9xYg0AxvWigI3nv7YvEBUbu2O47hSMKOdotN4KRVTeOcZtQ4bNNkWpHrAg8yCbYazLdnliLsSCHpgY5VqSXHJN2bwP6DwqF9fW94AckMRA04gIIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=cEcNoH_x-QfdJcO_J77850ca_6q85NU42zTZK4xifuGZ8-oBPRr9Ys8izNEV1wpst1ros-Az6jFsPWKXU5S-4zI6-b6ISe1ORzWQC1mmQCLgqaeA0MONqKfOCkW9UKZwDXV3kP_R74ylJpl8q1yKJct-fdYQZqbSVeb2nt0i7xYcZkimLAm2vNQ-_FZDMaXoa5dWMGNO46yLfa5l0WaPDputMhEhXmF-3DnfDT9xYg0AxvWigI3nv7YvEBUbu2O47hSMKOdotN4KRVTeOcZtQ4bNNkWpHrAg8yCbYazLdnliLsSCHpgY5VqSXHJN2bwP6DwqF9fW94AckMRA04gIIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=PPRguOITLqV01gBAY87zjA5enEdPisxSTCkISYO89p01061AT6XXT_0WJxhDR6_Ubaw2kyDJKSHNgC2Ug0lxQxkFyfX6u_zcAk5d03sOtYDowdGT1CplMMJuznZdXmDWEYh483VBrOqaZ6S483id4tE3_YiPPRMNjwCo_H2xpZOzPowGw4fmi2V-TTxMQmN951ZpWsjRbxVWbjcmYLl65zn66H9_ACXLcu76IHPOE_Wi_c11T-z30GPqStc_6q2hfH27c32xij7bUYsuIiffDGwbVAAujwU726BmWW2a-Z1LoTJEGPHCzfBZSOHUqJ4W1B7lXxiJSs3UfIYatnSTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=PPRguOITLqV01gBAY87zjA5enEdPisxSTCkISYO89p01061AT6XXT_0WJxhDR6_Ubaw2kyDJKSHNgC2Ug0lxQxkFyfX6u_zcAk5d03sOtYDowdGT1CplMMJuznZdXmDWEYh483VBrOqaZ6S483id4tE3_YiPPRMNjwCo_H2xpZOzPowGw4fmi2V-TTxMQmN951ZpWsjRbxVWbjcmYLl65zn66H9_ACXLcu76IHPOE_Wi_c11T-z30GPqStc_6q2hfH27c32xij7bUYsuIiffDGwbVAAujwU726BmWW2a-Z1LoTJEGPHCzfBZSOHUqJ4W1B7lXxiJSs3UfIYatnSTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayQUajIpmCMvYRNWg9FAkjO1wqDLg93Lp8GRXiDT71QIfuNcmuHuj-du9v8lRSmSfnKOa60ZW2NnsN680GuqNvCO5XkNSmwjNuvXs_jktc5m1rlWeuu8dMlHGu1RY5OpHWreFOfyEhibkVQjrBWnkj2MHMzody9sCDIg-3tYOLkskWrFdaB3nqbHvq5cbsMmCUDrVFtjyFSGWdF65TVKObtdr-Gif1wPEGUMwSPC-ASInSB9L_wJ5mudkOXzv3l3JCkgTZvv2ho3vLHMXaKon1mDgJarA__Ov1KMjADmx8mlPCAJgbOJAGtidU20gc14BFOZM_9m0Cn28bNIVjfxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=PtAM_-6wXcf0TjV3r8jXRn87cuXNPRaFuzgdhFPPqlnDDK1KWVzC6nJPWrPoD7W67-ztpvhj0cpKLOlZLtHR_BYgXA1bKTiX10zpQy28oIOfYVQzVlgteE9_qpMPbY5SkvTdvAynCEwrpkGoNPS1aG3qKyCpavpkP7NxfEjt_Xq9wxHVH98xMPjQ9H3Cmyuztd0CvBp2A250jIE2fZXLHT9S_qZd-ygC30W2g9PuBib8P-4pMve55j11U6pK7yyGbsfSTZM7rILwEo02E6wPIIclo32QSAu03Ks-85af0dgEai_jrga2kiF3hQQbfw4wGwSTNDXoAvBqBXJe8seeDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=PtAM_-6wXcf0TjV3r8jXRn87cuXNPRaFuzgdhFPPqlnDDK1KWVzC6nJPWrPoD7W67-ztpvhj0cpKLOlZLtHR_BYgXA1bKTiX10zpQy28oIOfYVQzVlgteE9_qpMPbY5SkvTdvAynCEwrpkGoNPS1aG3qKyCpavpkP7NxfEjt_Xq9wxHVH98xMPjQ9H3Cmyuztd0CvBp2A250jIE2fZXLHT9S_qZd-ygC30W2g9PuBib8P-4pMve55j11U6pK7yyGbsfSTZM7rILwEo02E6wPIIclo32QSAu03Ks-85af0dgEai_jrga2kiF3hQQbfw4wGwSTNDXoAvBqBXJe8seeDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
روز اول جنگ آمریکا از طریق یک کشور اروپایی به ایران گفت مثل ونزوئلا تسلیم بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=C9J018YsoYyWHiFP5C-1bN0lNBHz1rsWT0krTDw8zrvYnfuA3GHYAg-zpEVJuaSCh1TiEmsrK9VvwUagBwFDndgAEoOwYRBsKmV6u2p2SM_BgEJgBhdW-jSPS3Zck_WooryAtwGL-RBlyLegsgvNPibJ3NVC8tolyxnI9y3HHvqjiWs3T8cq82TrBZwluwTNZg1hzF67nejzHkvf2ejS_HmNqFWifii1NwuxE_r5gEqsmqZ6jeXNn8BklatVrCmzqSDCHjHXNI0vQcedGa1buzMzLPr7Vil-rL1giX95_s2GJZnEmzhEPcdNPr2djYfBvpMG56JwbB8ZHy-gC5hcpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=C9J018YsoYyWHiFP5C-1bN0lNBHz1rsWT0krTDw8zrvYnfuA3GHYAg-zpEVJuaSCh1TiEmsrK9VvwUagBwFDndgAEoOwYRBsKmV6u2p2SM_BgEJgBhdW-jSPS3Zck_WooryAtwGL-RBlyLegsgvNPibJ3NVC8tolyxnI9y3HHvqjiWs3T8cq82TrBZwluwTNZg1hzF67nejzHkvf2ejS_HmNqFWifii1NwuxE_r5gEqsmqZ6jeXNn8BklatVrCmzqSDCHjHXNI0vQcedGa1buzMzLPr7Vil-rL1giX95_s2GJZnEmzhEPcdNPr2djYfBvpMG56JwbB8ZHy-gC5hcpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کاپیتان نفتکش وقتی میفهمه تنگه هرمز دوباره میخواد بسته شه:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f482273e.mp4?token=VbCJiylDS7-08FmrIUv9V5Z4a5o8JQ2BY9CxPYu-qcASlJCo2wN0A2zJwiotQymn096J5LK1820y7UfxipOTt4RbrbVsKUBvNzZiAOf6zwzn7hCqkbGBurTgo-cCdS_R0TdOC6PUUWaZZBH5iJ8G0AkvSQCmWHyzzWTc40k-Rurzk35kOWyqD72HxhIU6OnCHcH9EJMQu-IzHlrZQ3LCyuiNZZGHvykSH3QDyEnRKog98ht_av40HE9qlsm9elEM2dsqNxhQEehUHdbEmux2YcITgylL0rqZidUDVSKxlTYb_Qn4IU3jENyqxIq4QbI7v3Jo3zW7BtaR2Ym1xp_FTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f482273e.mp4?token=VbCJiylDS7-08FmrIUv9V5Z4a5o8JQ2BY9CxPYu-qcASlJCo2wN0A2zJwiotQymn096J5LK1820y7UfxipOTt4RbrbVsKUBvNzZiAOf6zwzn7hCqkbGBurTgo-cCdS_R0TdOC6PUUWaZZBH5iJ8G0AkvSQCmWHyzzWTc40k-Rurzk35kOWyqD72HxhIU6OnCHcH9EJMQu-IzHlrZQ3LCyuiNZZGHvykSH3QDyEnRKog98ht_av40HE9qlsm9elEM2dsqNxhQEehUHdbEmux2YcITgylL0rqZidUDVSKxlTYb_Qn4IU3jENyqxIq4QbI7v3Jo3zW7BtaR2Ym1xp_FTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
دلیل موفقیت رزمنده ها بخاطر پشتیبانی ما بود.
دولت بیست میلیون بشکه نفت رو داد به هوافضای سپاه تا بتونه خودشو تامین کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66668" target="_blank">📅 11:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66667">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NViXp_kB_fv1j51rTOP9sUN5B_UNErY30qfWDF733gz9puuf4m1e9ik9MLbB8d5OgmmwOviEfNPz4jxmGrnyKTqdbJAyfox_FjN1gjbBn2xHsnMKtP89PrvVHnkmEM3dqiDtJqIEUc8n2V5o_2SpfJv6PSuP3yLPvXbpF0kbtPFfbgFAALvzcoO1LUjMA67OxGNqhoFO1ld28urEzmsnxubrj_MliHZpKAYtTcAwGPNHa4Fwite83ICcPUWyFnh08oETqp9EokQlzTNqJqS-Ugb8EthpYezTKn8Udr8W71r2AqkrymiAv5LgqMwDej4MeVW9duwr7-9Pvk_vzDx5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
