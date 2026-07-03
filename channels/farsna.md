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
<img src="https://cdn4.telesco.pe/file/RphuTCfrxuxxe6lK-0EJ-_tqfcS_xT4QZ6cnUajj8RB4WSj2cLqX2mlmeFTMYkzS2Qisd8bmt1_IeHlbcGrLxjigrfNEvuaYQpdGvP3TNpwK7Gpbit6vnQjQNmMqNOwmblgTt3e7RqnTtgBovIbDkjXjdnSVaZ3G1-ND6_d5_jz-bIwtEOwwgVKjFPsXQLRrM-D5M-S6kLOInxOhWSXRblQEHu8ipkd_xzLRv0p-Vg5wv3cbHD2Ar6yJ60yjKUqLKAmkoF-G8exAyIZdl1UqZr-VEJzq6K9zk3npqgsY-zuXhlFMZ03ud4ywOwXnvUzpbYvrUPe0nWmMgqXpXqCaLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 19:49:21</div>
<hr>

<div class="tg-post" id="msg-446377">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پلیس فتا: فریب اخبار جعلی دربارۀ مراسم تشییع را نخورید
🔹
رئیس پلیس فتا: دشمن با انتشار اخبار جعلی به نام برخی مسئولان و رسانه‌های معتبر خارجی، در تلاش است فضای مراسم را ناامن جلوه دهد و آرامش روانی مردم را برهم بزند.
🔹
از مردم می‌خواهیم به پیام‌های ناشناس، اخبار غیرموثق و محتواهای مشکوک در شبکه‌های اجتماعی اعتماد نکنند و از بازنشر آن‌ها خودداری کنند.
🔹
تنها مراجع معتبر برای اطلاع از مسیرها، زمان‌بندی و اطلاعیه‌های مراسم، رسانه ملی و خبرگزاری‌های رسمی هستند.
🔹
مردم در صورت مشاهدۀ اخبار جعلی یا محتوای مشکوک، موضوع را از طریق شمارۀ ۰۹۶۳۸۰ یا وب‌سایت رسمی پلیس فتا گزارش کنند.
@Farsna</div>
<div class="tg-footer">👁️ 302 · <a href="https://t.me/farsna/446377" target="_blank">📅 19:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446376">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4820db050.mp4?token=aXd4mRiFnTOgmxxYElZthuU7lv_fjvno_-oRr8SurmXepc-NVVU0gxiHAq39OLw1eF4j6OA9aOwe8ujhIaWf5o4k_ofTPMBpD7a07dNcTMVXmnVxUfHE4YUZUQuPxpAaR2_s-Vh7Y-9H0ujby48eT2EDmL1xre2-tptG95oiKYE8wCBqjqEobJ_NAKtmFne11_r6knO6LmJFrVL0dcQ_bLmGfjHbqtso_mzNKdsEDfY-VJoDiSZrrH5kwew0lINLhbYsPZAmyIgkyl8bVdcgTyp5ZIVZ694srJ0j2Fk1mE02OMEw8J3SCSqyELGL1lork8xITWWTaqIpwrT5eDusd0FLsSmnByfj9FMwjSZqzpQYPPTvhRny71Z5ZZ37TMqtcVhjy7ydMazYzoOy9rPcnfh2ujU0u5anYnykKlyplrvR-nuzBRpiZcMPRZBfp8Ie0qEA8_BiqM-nlinnqvmbYJhZGuENUSqKmn52cse8T7WnXE5PXAOKLBcTfhc9KcwRJYtVA0FsxDhhUNoY17dhE-gdj3kK-2oJYGDwUfAaT2R6PPld928cittsWJWyMvTzttL9FMqTZv5u4xAt1VBeEJfYeU1tFXHWPzg2xCcxaLmpmPHp8k7_slctn9CR7SbQ0YYqkYmlIHQs_c1XejVNj6HhtcdbyCsQPqrBhnT_svA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4820db050.mp4?token=aXd4mRiFnTOgmxxYElZthuU7lv_fjvno_-oRr8SurmXepc-NVVU0gxiHAq39OLw1eF4j6OA9aOwe8ujhIaWf5o4k_ofTPMBpD7a07dNcTMVXmnVxUfHE4YUZUQuPxpAaR2_s-Vh7Y-9H0ujby48eT2EDmL1xre2-tptG95oiKYE8wCBqjqEobJ_NAKtmFne11_r6knO6LmJFrVL0dcQ_bLmGfjHbqtso_mzNKdsEDfY-VJoDiSZrrH5kwew0lINLhbYsPZAmyIgkyl8bVdcgTyp5ZIVZ694srJ0j2Fk1mE02OMEw8J3SCSqyELGL1lork8xITWWTaqIpwrT5eDusd0FLsSmnByfj9FMwjSZqzpQYPPTvhRny71Z5ZZ37TMqtcVhjy7ydMazYzoOy9rPcnfh2ujU0u5anYnykKlyplrvR-nuzBRpiZcMPRZBfp8Ie0qEA8_BiqM-nlinnqvmbYJhZGuENUSqKmn52cse8T7WnXE5PXAOKLBcTfhc9KcwRJYtVA0FsxDhhUNoY17dhE-gdj3kK-2oJYGDwUfAaT2R6PPld928cittsWJWyMvTzttL9FMqTZv5u4xAt1VBeEJfYeU1tFXHWPzg2xCcxaLmpmPHp8k7_slctn9CR7SbQ0YYqkYmlIHQs_c1XejVNj6HhtcdbyCsQPqrBhnT_svA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع با پیکر شهید مصباح الهدی باقری کنی داماد رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/farsna/446376" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446375">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249dde3f7a.mp4?token=Fq7bF5479i7opLDaomsfgKlyAe9V-n7VGOAXVdad9R4L-gjPq3_HrCOvWX2fJtlwNa7N8gZXYtogTrae9we5qyiQHrU7JzxTDtQknXsTABi7AqG_rts1jzsYKhgBWXaEoI5acKDx_kkeM3ICbFPsJmC2jEjCBfgz-Ew8rCtZgAaA3bg2wzs79hpF_VktZMtxhmfcJnL-uK-o04CiOduKOyIjs5opnbB1mTgnM9YBCMYKJkBY8LY5lSSviAcEcVgKGP1SZRJ-83KcT6M5oXnRyHegUbuw9iru2-1_oWEtFPgsMhbvtH-1Hgcag4CN-0EC_BerS2D9te7mFmwej0fdGmUvI1jy7W--NDU8SGViaKea0tFcA7oNPhhD5iFc-SodjI0cVohCutc37GDxxZ50zMKm23EhIQADCHX2-4-momlZw0ds44ffkXU_CKoiJ6FrBNKTULefKYiZ-TcABc66DEghiyuTziCOBNzCJXdylbUQY_EfjnqewaZEMTSdJZ-_tyvWqij2yUwr24zHPyQkqrZK2vqzDdyuJa9HkqZeCwKi6IqDJg1g9I1LpU9ofHHI7hJVrCL0sJoWnxFmGJ5drqoZZkWGVAbLzq0KMors73TfywfQ90c1mMcJJfi0d_cgz21u85p05O3pUWEx9W0H-cdkOTyPJAE2TmuAs1pmBww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249dde3f7a.mp4?token=Fq7bF5479i7opLDaomsfgKlyAe9V-n7VGOAXVdad9R4L-gjPq3_HrCOvWX2fJtlwNa7N8gZXYtogTrae9we5qyiQHrU7JzxTDtQknXsTABi7AqG_rts1jzsYKhgBWXaEoI5acKDx_kkeM3ICbFPsJmC2jEjCBfgz-Ew8rCtZgAaA3bg2wzs79hpF_VktZMtxhmfcJnL-uK-o04CiOduKOyIjs5opnbB1mTgnM9YBCMYKJkBY8LY5lSSviAcEcVgKGP1SZRJ-83KcT6M5oXnRyHegUbuw9iru2-1_oWEtFPgsMhbvtH-1Hgcag4CN-0EC_BerS2D9te7mFmwej0fdGmUvI1jy7W--NDU8SGViaKea0tFcA7oNPhhD5iFc-SodjI0cVohCutc37GDxxZ50zMKm23EhIQADCHX2-4-momlZw0ds44ffkXU_CKoiJ6FrBNKTULefKYiZ-TcABc66DEghiyuTziCOBNzCJXdylbUQY_EfjnqewaZEMTSdJZ-_tyvWqij2yUwr24zHPyQkqrZK2vqzDdyuJa9HkqZeCwKi6IqDJg1g9I1LpU9ofHHI7hJVrCL0sJoWnxFmGJ5drqoZZkWGVAbLzq0KMors73TfywfQ90c1mMcJJfi0d_cgz21u85p05O3pUWEx9W0H-cdkOTyPJAE2TmuAs1pmBww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرخ است افق، خون تو پاشیده بر افلاک
@Farsna</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/446375" target="_blank">📅 19:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446374">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAQVJ1yrGPKaaicmHK79SuoNl2Fq1hSYCHJTJCB9FhIy97qMonSq8_Q8fOOiwdpRBHj8vrCHPpOiN1kh6ETOcmEkVMdYnE179tkP-ijjkg2G7vYpaxyl1duMLbMv8BA4FQw39a14VknfoJo2WqCtn22fJGXieuZsAtqRs91Ab_v7Cu3u2Fyd9A4rIK7a08AjvVgn2nw3ouyARITVTthTVM0vyTvtu05XeKX35S6lboyKwUC4v1T9cvfZgLoLMSg9krEYwL2nZRGZY0h3nGuFEeKIizMTAUi4ycLEy8LojB_M3yehbIjvsecW2BiLh5HZioJ9agR4p3HYGHXnH-pB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نقشۀ زائرشهرهای تهران برای اسکان زائران استان‌ها
@farsna</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/farsna/446374" target="_blank">📅 19:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446373">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Svyq7j0tggyAHdBUpkbztEKe72MrEcXq1QD6QC4nch92k_tTgcDVWl7GuFO-jXuurJR01EGBQehDknEhncbkAs2gBgg0wQjLQCEMpEejFqF29Yz33PUCp_9Z-FUHARBNlhSipa8Ii5tzs3Dffh_TP_hc_2ekpt4-sIkJm6knhmBqs0vWU2vHN_zhKbMsgphzJ7cbOS4Zl6whUGll0XsXXFr-e212pNdvFEFRei0cOqw99ImxmqrTXeP5YRVYoXVtnvPO0Oi7h06Ex70UVXZcCH_oRkwmGqcmj7BoNoas5fqfGnkcGEBBSuRnmG1l6yNa9cS9iIl2GlBtNh9QggHVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
متفکر الجزایری: نوۀ رهبر ایران را تمدن اپستین کُشت
🔹
یحیی ابوذکریا متفکر الجزایری : آمریکا، دموکراسی، تمدن و حقوق بشر... دختر فرشته‌گونه زهرا، نوه آقای خامنه‌ای را با موشک، نه، با تُن‌ها موشک کشت. این تمدن شماست، ای فرزندان اپستین.
@Farsna</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/farsna/446373" target="_blank">📅 19:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446372">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8accf60db.mp4?token=YPMOE-BHH_ZoVFnnkAmiqq-of2tPFy-jdiRF3n_8LssMWIs1njM12wn6BNBHIZrMvQaRh6aktikWIeikASI9VwsgMpvptduUWFC3tDC6ZXAoSc45fG9ndEjaumUEYfSfb_4alJM0HT84FLET1My9dle13Xap6zXNTTr8aMMCbEXV-5DSaybNCa4au1WGACzqGMoqmuwONiMucngINjhPs-4wNJwGkGPI9HTZKsdFaGRF0mWn1c-4FRuvf_kYobKvlPLKCAo7Y2AMG9Aq3kEH5nS07p2x1ToIRHsK2iDcAxCDrsgJKViRX5BzJcQZhvRRrCl--eG__tIf24Vrk7I0aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8accf60db.mp4?token=YPMOE-BHH_ZoVFnnkAmiqq-of2tPFy-jdiRF3n_8LssMWIs1njM12wn6BNBHIZrMvQaRh6aktikWIeikASI9VwsgMpvptduUWFC3tDC6ZXAoSc45fG9ndEjaumUEYfSfb_4alJM0HT84FLET1My9dle13Xap6zXNTTr8aMMCbEXV-5DSaybNCa4au1WGACzqGMoqmuwONiMucngINjhPs-4wNJwGkGPI9HTZKsdFaGRF0mWn1c-4FRuvf_kYobKvlPLKCAo7Y2AMG9Aq3kEH5nS07p2x1ToIRHsK2iDcAxCDrsgJKViRX5BzJcQZhvRRrCl--eG__tIf24Vrk7I0aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنجرۀ متفاوتی به مراسم امروز ادای احترام نمایندگان کشورهای خارجی به پیکرهای مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/446372" target="_blank">📅 19:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446371">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎥
سلام بر تو ای وعده‌ی تخلف‌ناپذیر خداوند
@Farsna</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/446371" target="_blank">📅 19:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446370">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7abad4ed.mp4?token=ePDw167T_C697gHQgdxIeplefOLZsRDVrHnDdlEbkQcq0AdbsvV8CpcGuitNuIVHlc6cG7hTX8FTH5m891mIpVOXoZXblnk5sM4us0tsPMlXxuECVRCjHdHRjt0M23gw4pj-hq6wjXwwpKJWA27z4qNo-n78_nS78uvMFv_XquV7mlFd88gPfI3Z822zCkznYKBfa2Kkpv3aT6teRnkEOmZwVgRI8ZniukmEtfirLaTpm93OMOkoYsBSzCBxbiIP3ybnmQghsSKtaJQXvVH6WrIuqmm8DXqSxO5IsjrHNvg7056mWE6tpUKT1rLDXWNqfw-dgCeXZxXtOP3ta7a1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7abad4ed.mp4?token=ePDw167T_C697gHQgdxIeplefOLZsRDVrHnDdlEbkQcq0AdbsvV8CpcGuitNuIVHlc6cG7hTX8FTH5m891mIpVOXoZXblnk5sM4us0tsPMlXxuECVRCjHdHRjt0M23gw4pj-hq6wjXwwpKJWA27z4qNo-n78_nS78uvMFv_XquV7mlFd88gPfI3Z822zCkznYKBfa2Kkpv3aT6teRnkEOmZwVgRI8ZniukmEtfirLaTpm93OMOkoYsBSzCBxbiIP3ybnmQghsSKtaJQXvVH6WrIuqmm8DXqSxO5IsjrHNvg7056mWE6tpUKT1rLDXWNqfw-dgCeXZxXtOP3ta7a1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدا دلم ز تو نگشته ناامید...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/446370" target="_blank">📅 19:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446369">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a69858ce4.mp4?token=Zk7JFCYjN-z2GcZvj_j6rzPGEM0ClEM9ewvGSEm_EHL_pWlUDoRQilRmiWbcFqMyi8UDTtGm5oInvKmp4fi4KuDsYiW8_n26aDkW1j9DMMA88wHmiHLv6t6Gvoo-hCzuePDYS9O2fIyBt3xBhnzdcg8en_kMToB1BIAlNiuiH3Pn_fR0s4rMbt9UN9cpUoLXvd1nP-zM_esoOa9g5PDZ3qGndIDz5rFIfkt_WCS3gi2OPCvvvyl5KAqHzlwNlQkW4EAxPO2Fjx-pTsf3xDR9DC1m63DDgm6Bf3hNutn56GwOX4yys1X2-Ee3N8qJFA4wxZGujwJ2zYUvegHvFh1Fkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a69858ce4.mp4?token=Zk7JFCYjN-z2GcZvj_j6rzPGEM0ClEM9ewvGSEm_EHL_pWlUDoRQilRmiWbcFqMyi8UDTtGm5oInvKmp4fi4KuDsYiW8_n26aDkW1j9DMMA88wHmiHLv6t6Gvoo-hCzuePDYS9O2fIyBt3xBhnzdcg8en_kMToB1BIAlNiuiH3Pn_fR0s4rMbt9UN9cpUoLXvd1nP-zM_esoOa9g5PDZ3qGndIDz5rFIfkt_WCS3gi2OPCvvvyl5KAqHzlwNlQkW4EAxPO2Fjx-pTsf3xDR9DC1m63DDgm6Bf3hNutn56GwOX4yys1X2-Ee3N8qJFA4wxZGujwJ2zYUvegHvFh1Fkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه کامیون‌هایی می‌توانند در شهر تهران تردد کنند؟
@Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/446369" target="_blank">📅 19:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446368">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bef907830.mp4?token=HSBMcJ67JEgN5bRfQeTrRKohLpt0pc6GuLrQrQaT2SoGln9hmvqhRX3YYure0iTUQ2GnGPhhItz6ES4vuo9-nn3U7WYBg-tCoEiibljPZ3QDsMmUaLQtxgct4xecd-cb2JLxujxWi-8NSxVez0FZQbVvRyPnNDM7o2EvGJkFJ7hf7Q7_jAX6Lntw-8halT38eiB90M74JRod0aOjlwqj4Uqd4Hyqlj0uriLVitIFV1eUMAdMUheVRxX4lv-5On86TvOTPsl1VDzAqw22eIuAIdJ4OthFMAoBkcjZA9q9stsNPwa6wFGKPU2IYBorV8Dxoj2vKoUMPYggARgysEryt0DGxIzgv4vABkpcY4vhvTsRRbn35aM7Fjfc0OyNHZKxT06nC77bKh0LIUyuIyRWeg7SrWpQnvemS2S4Y-z60yHNsW20EyTlPj-OIEj6rRLef6Q6p5eGR4VjbCHeqMf2D73TgTppWQeLgHkCTeY6bXIuVePdmg-SznpA0Rd34_4TW5yx7fGBkJeUvUMuMTaTMNIGFRHoOXtrbL2RYhMAGn24aFBxtcdbojchaRZgicMHTNGOIv96vh0DxqEBbDXCs17iDxMxIrWu2wVJqEDAHGoryx_V-V3EziIEuICP3lk1P1iEEZtOhMA9Ci6d_BrXNx_CgUtafjv2RwNiIE1Fq-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bef907830.mp4?token=HSBMcJ67JEgN5bRfQeTrRKohLpt0pc6GuLrQrQaT2SoGln9hmvqhRX3YYure0iTUQ2GnGPhhItz6ES4vuo9-nn3U7WYBg-tCoEiibljPZ3QDsMmUaLQtxgct4xecd-cb2JLxujxWi-8NSxVez0FZQbVvRyPnNDM7o2EvGJkFJ7hf7Q7_jAX6Lntw-8halT38eiB90M74JRod0aOjlwqj4Uqd4Hyqlj0uriLVitIFV1eUMAdMUheVRxX4lv-5On86TvOTPsl1VDzAqw22eIuAIdJ4OthFMAoBkcjZA9q9stsNPwa6wFGKPU2IYBorV8Dxoj2vKoUMPYggARgysEryt0DGxIzgv4vABkpcY4vhvTsRRbn35aM7Fjfc0OyNHZKxT06nC77bKh0LIUyuIyRWeg7SrWpQnvemS2S4Y-z60yHNsW20EyTlPj-OIEj6rRLef6Q6p5eGR4VjbCHeqMf2D73TgTppWQeLgHkCTeY6bXIuVePdmg-SznpA0Rd34_4TW5yx7fGBkJeUvUMuMTaTMNIGFRHoOXtrbL2RYhMAGn24aFBxtcdbojchaRZgicMHTNGOIv96vh0DxqEBbDXCs17iDxMxIrWu2wVJqEDAHGoryx_V-V3EziIEuICP3lk1P1iEEZtOhMA9Ci6d_BrXNx_CgUtafjv2RwNiIE1Fq-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
زائرشهرهای بوستان ولایت برای میزبانی از میهمانان آذربایجان شرقی آماده شد/ بازدید دو عضو شورای شهر از روند آماده‌سازی
✅
اعضای شورای شهر تهران، از روند آماده‌سازی زائرشهرهای بوستان ولایت توسط معاونت مالی و اقتصاد شهری شهرداری، بازدید کردند.
آقامیری رئیس کمیته عمران شورای شهر:
🔺
۱۰۰۰ نفر از نیروهای شهرداری تهران و داوطلب، به میهمانانی که در بوستان‌ ولایت مستقر می‌شوند، خدمات می‌دهند.
پیرهادی رئیس کمیسیون سلامت، محیط زیست و خدمات شهری شورای شهر:
🔺
اقدامات بسیار خوبی توسط سازمان بازنشستگی شهرداری تهران و شهرداری منطقه ۱۹ برای میزبانی از هم‌وطنان آذری زبان انجام شده است.
🔺
در کنار امکانات اقامتی و بهداشتی، وضعیت ایمنی و رفاهیات نیز برای میهمانان اندیشیده و اجرایی شده است.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/446368" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446367">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggERNEGGroBzaGW4mOpJGh3alm6woFfh7gc2giVQWcNvBu78PgUT8TneCMQ5o5sT5XjheGGkGbl1ITHVMAP9flFc4SiwjjsUx8vSy73wH1rPcjjAZnB1ZqKOELmI-UE2VH8c-TK_zRumQTqwyhFZSBAc_X0euXmeUSNFk9PqIT4Y1EwW7EK4tUMS_RhkCnp92UKaefgYsqBkYxFCPDayweUZR8GVBYUpNX9Dd9TU9vnmpCS7RVlpwR1I2dLNOtGQqI7GJGwIPE2mQTG31txJy1p6NBHPBMfThNSB4SUI1048WUAY6dVZvWLrIgznzGZ6xzrBk8soNE0A8ZvEiO5zOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
آمادگی کامل بانک رفاه کارگران برای خدمات‌رسانی به شرکت‌کنندگان مراسم وداع و تشییع رهبر شهید
🔹
بانک رفاه کارگران با بسیج همه امکانات برای خدمات‌رسانی به شرکت‌کنندگان در مراسم وداع و تشییع رهبر شهید انقلاب اسلامی در آمادگی کامل به‌سر می‌برد.
🔹
با هدف تکریم سوگواران و تسهیل در ارائه خدمات، این بانک در استان‌های تهران، قم و خراسان رضوی، اقدام به برپایی موکب خواهد کرد.
🔹
همزمان با مراسم تشییع پیکر رهبر شهید در روز دوشنبه ۱۵ تیرماه در تهران بزرگ، موکب‌های بانک رفاه کارگران در نقاط مختلف این شهر ازجمله پشت ساختمان وزارت تعاون، کار و رفاه اجتماعی (خیابان اردبیل)، ساختمان ستادی بلوار کشاورز، ساختمان اداره آموزش و توسعه دانش (دروازه دولت)، مدیریت شعب منطقه سه تهران(صادقیه)، مدیریت شعب منطقه دو تهران (روبه‌روی مهدیه تهران)، شرکت داده‌پردازی (استاد نجات‌الهی) و برخی از شعب بانک رفاه کارگران، برپا و مشارکت و حضور اثربخشی در برگزاری این مراسم خواهد داشت.
🔹
همچنین همزمان با تشییع پیکر قائد شهید در شهرهای قم و مشهد مقدس به ترتیب در روزهای سه‌شنبه ۱۶ و پنج‌شنبه ۱۸ تیرماه، موکب‌های بانک رفاه کارگران در نقاط مختلف این شهرها برپا خواهد شد و به شرکت‌کنندگان در این مراسم خدمات‌رسانی می‌کنند.
🔹
جمعی از مدیران و کارشناسان بانک رفاه کارگران با حضور در ایستگاه صلواتی بانک در این مراسم‌، پاسخ‌گوی سوالات حاضران خواهند بود.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/446367" target="_blank">📅 18:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446366">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/446366" target="_blank">📅 18:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446365">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ceae37eac.mp4?token=E6N2an31XTrUtr0U_Wf69TOqstW38U0oPWHEXnLOqvLjf-KF0yHMmSCMBCaElWH5q1axa5yPjrE1ajkSvGxb0HPmhy9CWUqb0wr_USS_ugQB8KvrQwzgi_738eMGCZSMDEupqdG0J5lsib8Bqa3R1SqxYkRseSNGhkg9vT-v-e72bpx1z45ZdtHQNoOZ-mE0dxfPC6xPTFqPv2UYAvkBXoQ-pRdlSzqzXLrJpxGELf71QS2IFZUulUyxSaY2Au1T6YNnS4gQ-HpG_PE-2wmjg7CJBcAbPtUbAnm_T296pBjzyfvkYpl_MrZqrOumCBek3MbdqKo4rRvCQDzqKNd8Xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ceae37eac.mp4?token=E6N2an31XTrUtr0U_Wf69TOqstW38U0oPWHEXnLOqvLjf-KF0yHMmSCMBCaElWH5q1axa5yPjrE1ajkSvGxb0HPmhy9CWUqb0wr_USS_ugQB8KvrQwzgi_738eMGCZSMDEupqdG0J5lsib8Bqa3R1SqxYkRseSNGhkg9vT-v-e72bpx1z45ZdtHQNoOZ-mE0dxfPC6xPTFqPv2UYAvkBXoQ-pRdlSzqzXLrJpxGELf71QS2IFZUulUyxSaY2Au1T6YNnS4gQ-HpG_PE-2wmjg7CJBcAbPtUbAnm_T296pBjzyfvkYpl_MrZqrOumCBek3MbdqKo4rRvCQDzqKNd8Xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درد دل‌های دخترانه با پدر شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/446365" target="_blank">📅 18:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446364">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cee7d6c7e.mp4?token=jisvjd71luBvlltcYuK8KdbupneU83284t-HHeVkp040VzthUqmbMiKXoyaS4em8hO6nDMEi5Xx6uDMHKUzKz63Qe-2rGezvya5lbi8jyc8CGvnJZ0kc-E6_BgfBQVnFEH48te3XrCcW7tcD13Eo3D5ePJkH5Vgini3E_QE7hX95EcaHG3kpbaOK-3KZCCT0SQvP-wD0dI4o_o2yQCmDE02Dlp7QtoctSzAPD-44ZbZpko68JBKFrswHd0LImn5H0veU-JzzlN_mcL54KBcRcLLTNY1Q5tkr_TE9TG_w1oV-FuHx8pSmhyGJCmGqxXbJItzDR9xDeS1lyoxRx1ydxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cee7d6c7e.mp4?token=jisvjd71luBvlltcYuK8KdbupneU83284t-HHeVkp040VzthUqmbMiKXoyaS4em8hO6nDMEi5Xx6uDMHKUzKz63Qe-2rGezvya5lbi8jyc8CGvnJZ0kc-E6_BgfBQVnFEH48te3XrCcW7tcD13Eo3D5ePJkH5Vgini3E_QE7hX95EcaHG3kpbaOK-3KZCCT0SQvP-wD0dI4o_o2yQCmDE02Dlp7QtoctSzAPD-44ZbZpko68JBKFrswHd0LImn5H0veU-JzzlN_mcL54KBcRcLLTNY1Q5tkr_TE9TG_w1oV-FuHx8pSmhyGJCmGqxXbJItzDR9xDeS1lyoxRx1ydxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از پیکرهای مطهر رهبر شهید انقلاب به همراه شهدای خانواده ایشان در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/446364" target="_blank">📅 18:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446362">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: از اقدام جمهوری اسلامی ایران برای شکستن محاصرۀ عربستان، انتقال بیماران، افراد گرفتار و نیز هیئت‌های رسمی و مردمی شرکت‌کننده در مراسم تشییع پیکر «شهید سید علی خامنه‌ای» قدردانی می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/446362" target="_blank">📅 18:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446361">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: محاصره و محدودیت‌های اعمال‌شده بر فرودگاه بین‌المللی صنعا باید پایان یابد. @Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/446361" target="_blank">📅 18:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446360">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: تمامی یگان‌های نیروهای مسلح آمادگی کامل دارند تا هر تصمیمی را که رهبر جنبش انصارالله بگیرد، اجرا کنند و برای شکستن محاصرۀ عربستان و بیرون راندن اشغالگران آماده هستند. @Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/446360" target="_blank">📅 18:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446359">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: ادامۀ محاصرۀ «سعودی-آمریکایی» علیه یمن را برای مدت نامحدود نخواهیم پذیرفت و برای پایان دادن به این محاصره، از تمامی اقدامات مشروع استفاده خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/446359" target="_blank">📅 18:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446358">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: اگر عربستان یک‌بار دیگر حریم هوایی یمن را نقض کند پاسخ همه‌جانبه می‌دهیم
🔹
صبح امروز (جمعه) ساعت ۵:۲۰، چند فروند جنگندۀ ائتلاف سعودی با نقض حریم هوایی یمن تلاش کردند مانع فرود یک فروند هواپیمای غیرنظامی ایرانی در فرودگاه بین‌المللی…</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/446358" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446357">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: اگر عربستان یک‌بار دیگر حریم هوایی یمن را نقض کند پاسخ همه‌جانبه می‌دهیم
🔹
صبح امروز (جمعه) ساعت ۵:۲۰، چند فروند جنگندۀ ائتلاف سعودی با نقض حریم هوایی یمن تلاش کردند مانع فرود یک فروند هواپیمای غیرنظامی ایرانی در فرودگاه بین‌المللی صنعا شوند؛ هواپیمایی که بیش از ۲۰۰ شهروند گرفتار، مجروح و بیمار یمنی را جابه‌جا می‌کرد.
🔹
این تلاش با رهگیری جنگنده‌های سعودی توسط پدافند هوایی یمن ناکام ماند و پس از شلیک چند موشک پدافندی، جنگنده‌ها مجبور به ترک حریم هوایی یمن شدند.
🔹
به عربستان هشدار می‌دهیم از تکرار هرگونه نقض حریم هوایی یا تجاوز علیه یمن خودداری کند؛ در غیر این صورت، پاسخ همه‌جانبه‌ای دریافت خواهد کرد که فرودگاه‌ها و مراکز حیاتی آن در خشکی و دریا را هدف قرار خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/446357" target="_blank">📅 18:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446356">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eda90d158.mp4?token=VCm0Gy6VXDTT0JV1L2kphUSrWyfcfCPxVrgPVo1f9YzfkHHEtHiVAqxjwbGM88u_fL7PW4oH5ZWItonOD-9Bl8IVZgr299ms8XkJ1_Oa4TosN3HOaI88QM72XuLnrZV8-TECQ6QsqTAWWyvmiW2YzKTBsO9T-g8Nbl9CZjLR8Utir8kuNAJD0V9EhSlL_V3knenVtoo_wPwlWwLtnowk75QPRnXggf4XycuX0ZSRJ1zvkRsbDbAln-DviSS77wEi2Jvw0mj4MRsdsjPj2VAPhmCJXKpTgp2adsrW7R4rEzok46VFZe4MHuTIFQZRBK5xz5vspdIlG7af9kdu6wjdtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eda90d158.mp4?token=VCm0Gy6VXDTT0JV1L2kphUSrWyfcfCPxVrgPVo1f9YzfkHHEtHiVAqxjwbGM88u_fL7PW4oH5ZWItonOD-9Bl8IVZgr299ms8XkJ1_Oa4TosN3HOaI88QM72XuLnrZV8-TECQ6QsqTAWWyvmiW2YzKTBsO9T-g8Nbl9CZjLR8Utir8kuNAJD0V9EhSlL_V3knenVtoo_wPwlWwLtnowk75QPRnXggf4XycuX0ZSRJ1zvkRsbDbAln-DviSS77wEi2Jvw0mj4MRsdsjPj2VAPhmCJXKpTgp2adsrW7R4rEzok46VFZe4MHuTIFQZRBK5xz5vspdIlG7af9kdu6wjdtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از تابوت شهید زهرا محمدی، نوه رهبر شهید انقلاب در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/446356" target="_blank">📅 18:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446355">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/212b46c594.mp4?token=mZr3NxxqKpp1XQj4klnsctaalAYdWfrJzbxwlRCnzFXMVtH-u3bcWRLctxDoJB7eidMu7fJko5LW4osBRMeqf8qbdrMKpSdD9HrpOhrUUJn7B-w4nYy7SYbbTDCe0rr0N8lVmvueXfbdZBt5a_1Yu1d7lXr2JHUo2TiKj0hftKhSiXg1Gl9hdtxclKEuw8PukLh-sjJku8eJJEDqP8qIqoPdtKRdPZW2bLvkncdFG5QT4iIiMMIaEuKVXvGikm492yU2etwUGVydFN1Go6GDm_rhTEax5Yy6rKZe7exgoUzW4An_BdpW_88P1jOfwCkUzWcwGde5Jmj-cmQ85QK4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/212b46c594.mp4?token=mZr3NxxqKpp1XQj4klnsctaalAYdWfrJzbxwlRCnzFXMVtH-u3bcWRLctxDoJB7eidMu7fJko5LW4osBRMeqf8qbdrMKpSdD9HrpOhrUUJn7B-w4nYy7SYbbTDCe0rr0N8lVmvueXfbdZBt5a_1Yu1d7lXr2JHUo2TiKj0hftKhSiXg1Gl9hdtxclKEuw8PukLh-sjJku8eJJEDqP8qIqoPdtKRdPZW2bLvkncdFG5QT4iIiMMIaEuKVXvGikm492yU2etwUGVydFN1Go6GDm_rhTEax5Yy6rKZe7exgoUzW4An_BdpW_88P1jOfwCkUzWcwGde5Jmj-cmQ85QK4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این روزها چه محدودیت‌هایی برای تردد خودروها در تهران وجود دارد؟
@Farsna</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/446355" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446354">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📹
#فیلم | آغاز مراسم تشییع پیکر داماد رهبر شهید انقلاب، شهید مصباح‌الهدی باقری‌  #باید_برخاست   @rahbari_plus</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/446354" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446353">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=Ty9nH4eUPRyGYe1nRGCZdH3ZcZWzTxTgg7kT6aSiCll5CRAyyJ0nbiljnVHCvOYz8eRQmlH1Hl5POCNKbGWzwm7NGyTmrxXqDqQLQp65pWL6_u1sOt1YH1pMQGX1uNqXXkFdasY3iRHmt7lVu_VzBpudiozYgMOxJMtOI5x7XQVom3cwMKKK8kMmGstvd-B4_1XOvQ_xSms76MawMkRYODbTt0MXrf9W_8zomS_okfyEVjhVyYQplj6PsdUZxlt0liyG64ciLQbXVgxYv1ydR7P2NebbWi7ktGLWDeqBvhhjWUJUq-uMnsjEENGn3J4yB_uDT_Hhbn-zE4_zUSdFCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=Ty9nH4eUPRyGYe1nRGCZdH3ZcZWzTxTgg7kT6aSiCll5CRAyyJ0nbiljnVHCvOYz8eRQmlH1Hl5POCNKbGWzwm7NGyTmrxXqDqQLQp65pWL6_u1sOt1YH1pMQGX1uNqXXkFdasY3iRHmt7lVu_VzBpudiozYgMOxJMtOI5x7XQVom3cwMKKK8kMmGstvd-B4_1XOvQ_xSms76MawMkRYODbTt0MXrf9W_8zomS_okfyEVjhVyYQplj6PsdUZxlt0liyG64ciLQbXVgxYv1ydR7P2NebbWi7ktGLWDeqBvhhjWUJUq-uMnsjEENGn3J4yB_uDT_Hhbn-zE4_zUSdFCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام دبیرکل سازمان همکاری اقتصادی اکو به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/446353" target="_blank">📅 18:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446343">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqxMQZbu5FbfIAJlGg9yM1y4KOMrkFy5aDhVQyLuUo-0x6s0aMl_0-GQ5okoWVbxvL61Ci9Wct1KojUsuV4ttGk8jJcqrf0j7SgWswa0oDOYlQskOOZRhapDar2dl7Mt3dFGJcYcTFDA6II5vopdVb2p-DeYlfSVuDxZRC0MRsQ-Ur4cCRuQU0fZl_emNM01ZUQ77I5TgBAtUcuoCCLYs1hwM14xWkuD1AeHy6xAiXUjnY4Ao5zcJG1A-yPIQG20UU3PEGfBT2rSCYKtrC6oB9aNDXtV267uvQ1-mLRyfgg0KbLPbKPRnbr_NpT379KPLUOhTrcE4nEo4dCq2Wt01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5l2E6jViu6vm69W3d9E45R3LwNTo3OceEXfIeULLsAriuSJYa2uK3kSRNxLmsavklXmv0vfplG5MlVxER8BwIgvpC90irutG5WdIr6Z8LzNsgG5BxEqPryoaXEpVwFhDzr7jlzX0nFHGHx70pPSGTIIR0aJmIRJbFliqX9KKQJxCyVWTecryZJmfjNReHtuzp-9_XeJqwa3v2zmKT953TpXi-BpivA4nwM6Ry1U2iFCuMZSTDi0coa49G_t1aB9uCyUM-z5Wl-qvNin3WD8ihe8JwgyfczWkbUtNjUzoZdLpu9K05UhwwOnS8LC8ZVfjSPqtPwNgtE3ayoIFfa1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3MOiPHNz2GIHs5wfDMSnkhwUYZqKOB9zaUC8QUr9KqgqIk91DyHab2oG68MhUZ0Vtuv7DOL-HO9t9TRULXXjYc2aH36WxpgCaNZW2IdxqSX_rdfUGbbTW_0kPivytlavyVjngzVOk_8spkqwz3I0yqMYMgOv8zYLgUV0y_yX8nCvbpwx64bUjImGj9-9XtZiIGteS2ncYH85T0SuYmUyymj6dOCx6m8QTNIvcwOdneDaWgjqSk8gPEqdpMcrs0AhY5NAfIwopHyY82MOFAyuerDifs-ZhfCZHMaNqPr8tKlCd_7kBMFEFe030-uTNiZaWb-US0QhguNyATFOjlBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IPpk3_tN1HiOM95Vd8Rwv0aCsH4yEF1Y66auKpCmCSh9BCWe8FOAtkdtnDHLeOHuhOrd4A0kSO5BmtKuMw5eeylkdK6ayHO5rnAmiPkuYghwDKwvFmi0YY9jMsNKw_H2YliP3CkfoyyjWoWR4DAlnhJdie3RgMJ0IOYLqCCv0AtFgQClMeE7DUEaZ2W9PA6NKMhLh81cXfDLz2K-HhwwnVeNo-H96WX9MhidJFFpjBrUIOiLU3C-lKxC5dCAVlRumfpSm5NkTU6dN4P_8BBZ-78nUfKXoIopy7jqqFU0QyYCFHbYmq4mER2i2I913stJksGnskbH-ZfHQXBptZ7xmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuwCVrHtE0LZnP3JWY94clsxE3ztP58RZqOC2q5jlmjYRET4EMvLF5uw_ANRL1Y2l3b0thz1CnahKtxVgZ3h0THy69W3uAzCAV58omHnT75gcO_Po8PT0D6JREElpY2HkRTi-OXEZRN8gOoKCIGy54F2OAS7LhrVxg9WjntejlBmTDxZ3vdyo7eHv6LplLagtMFfBCv-tTkH-_OadzTejRHkRxPh_IcR5Oh8v5ULOLqrEhe82PCMPAJNoQ0-XqVfKzP88rpAzY01ShbUMbsiO-aWg0yPUUOb69WTcaSRfoPxgtlgg5rX76saU2DRHrZ1vKKDPkJc4Evujmz_a6fGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsCLxJX1ZuV3-UmHzt4TZDJj4kDxJGAp6Z6r2yj9umTes92qKfVyA0lGknau_XO5Zhlyd8N7XeBFcoCLHrYtQ8c-IOOregePcnEu-x_U3TkoiKbZVC7CbfTIGoKce-Bks2qA5L3MmYHovHLYXnOF3aUaQhr8z7RuSovY5T-8m6JT6ATAlf93NbzSBolwPDvC2TFQgUrqG_rpbpxJRhHRet0WHWIWO9PrvySKedyizD9jewHxa5FqL5ZNLhpPsLEzbePVz-fYdtG3UJ6Op3Ujamatq6AU9WRKN3Ewvp-yh4IFYBQFFk_czkW1UL3cpUXFCvSAIBmVXzohOxbTKlCDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnZ2C7WzTxrbltW6WPKowmls-5hv7_9ircjVhCJ3ca6_VoVUTZoIkxkjAehFyNXIMsgTmpFX4c2o-GRdm17HDS12SRXDh88t77_OLiINPQzaiB0XQVz7IZcfPSsJSdy-Y9KH_eaCg0SXBZV4cZ72YH61K_pfvpwHe1X8kaqfs79ahoxi7aJJMRI906869PqnmhdzTXBZhz3xZDZ1qXqncZPubxix0l_hXI38w0uIzS4k5mKVvQSA8MdmGqn_PkYSDHDF7NMwcE-0DTQHG-LVTTNllJHYxW3OKj_suCh8n-yVA8xsrcU0GKwJA4Tqf66Z1WnIRzbxPu58wBIEDTK-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VPAu7Y4A5eFYZPLQZVTg-j1ut75ieRPGftgf5Y19hvl2WA0eOpQ76FyIYtnBdeLPBlzVmR2lnZ9npZQ-u4sR3oozIwYblqD3NMIu8ursp8ku28msI8paRnvZ7DcBc4rmhjOhzpX4IXWvBXEH2Se_hJSa3AXWQOieiXUkkRpEInohlW4MsguWG3tJ-XSEfuYjnrGQZF7_F6TqLFsQgElzN9hWAPNnrxsC8IX_Oh2rp0Mh3wxRrM4v4-kWogK0mG5ihKiL2hCXRPWlMpHrrmHJDEXCTAXqTG55yJeGHkXdnCJwTVHVEf4d8UogC9L1TVrEHW7JK6aRF8ZTcfmg-J4T2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WglvQQUVea02AyluHnU7zzNavlR0otfLDThfgM9xQCM7knGngwzk-2TGf2me6TXojX8bcf8JBBTWBXcJxyFaX-CrecQ5175aH5JA6VMNnFZRUsw-mOz9c7-0US6v6WI62YnGFNhPegKHvp-H9TAWJXYkbBCQLqe8y_uneM7X9Nz9PQUQ8t92ddJG0K26KR_6VCb6e21M_GGPMgBiFC3HjYP39KnSDyZ_2cL9MxgQIoOxmN3_1cPtc4cZKzFV_ZSu4VaAfT3gSezPQ-CvHd-6xdYEG8bmrfIV7N_G1lpQ9Sm8S9v1s5DwKz1f-WPodg2w_Aa44IlHIYYXJKL3-6k8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-TLCROR29YJB2ZNs5BTyj0Wh4jNADJnCbcP03_qjQDUwVxZNtTGPjj3WnurqQl7T_aj3F8RFd_R3CzMfh960OQiEzW0sYySqys0hI-WtS1s_YSHR4wFBYi2IdOASEzrtX7fdpCaQFW9BZXdRl6QW5oDtBVfJwiE9OhKFwXClhAcUEVDEUsSz9zvKgIztiToP5EhPpv4jC-pNhV49hUBjnktSR28V_Z_jv5ZhLFzoNX5l3PlOhcxnk8IY54p8Ntw6g15Qfv27473Qw-gSzBo_jk2_4d4IDtc2BdrvtPE2LXtK75dYNXTlc8gZFbyC7BrpFC7_QAlRO6QID-tbOPFnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور سران قوا و مسئولان نظام در مصلای امام خمینی تهران برای استقبال از مهمانان خارجی
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/446343" target="_blank">📅 18:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5765e1db.mp4?token=Mf3_lfMEz6iYp1rNIAg-cSulZNQPkY1cPc0HOOfeK53sft6P72n6Nut-o9JO7oVLqXN_S8wiQUJp-xqSrewP4Q0t2UsQy24XNAPwPJIlYgcZgvC40qzc1yWKigNwjLHnZKdiBQrCf6rDPz1saohm4rewDtQ4x6f7udw8GJ9iK2Dd3m702xsNHSun83wsab9CsuT6s9gs7eagseSAus4AzeoshP22mqqYCSY_ii2w3_mX3--4decAbnQ9iAbu7-mIVNvaHE7_SBfwkPIkHyesPuUB-0Vj9CMjsLiZcyE6tuPCff-3XSKlawo9Ax-Y5JC-SJVbQnnVVSOIQ6ziqTjA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5765e1db.mp4?token=Mf3_lfMEz6iYp1rNIAg-cSulZNQPkY1cPc0HOOfeK53sft6P72n6Nut-o9JO7oVLqXN_S8wiQUJp-xqSrewP4Q0t2UsQy24XNAPwPJIlYgcZgvC40qzc1yWKigNwjLHnZKdiBQrCf6rDPz1saohm4rewDtQ4x6f7udw8GJ9iK2Dd3m702xsNHSun83wsab9CsuT6s9gs7eagseSAus4AzeoshP22mqqYCSY_ii2w3_mX3--4decAbnQ9iAbu7-mIVNvaHE7_SBfwkPIkHyesPuUB-0Vj9CMjsLiZcyE6tuPCff-3XSKlawo9Ax-Y5JC-SJVbQnnVVSOIQ6ziqTjA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندۀ ویژۀ دولت تانزانیا به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/446342" target="_blank">📅 18:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446341">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48a3b17bba.mp4?token=mGJPRn-iU3y5niVnUXQBIAr_RDH-xM93xkuPLXTEtjTDdElelmv5aUIFErXffyYRncmBxqARc0SscJocCsZUpO4uYCBmRhw-SgVE-gx5QGi8BqX06a-Dt_FAT1wmhmSf1mOKQFqYXXaRDGY7HeGzKkbxeFlrGIVwfj2YbPgwTB2n3Ch95_zPDcVs6WzKMqzv-6bYeREsk2RN2IH2cpKJnZ0JZdE0H2CareqyGmnGdGNjIT-4ZZNcFqH7rkdHo34dXtTUg7UACfJ0YKoFeWaIPxX60NiDAzpoiIi8V65HqkxdNcc_n_QVr68Wyr-6s7SPTA-KJ7SGpazeHPV-N1ZXaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48a3b17bba.mp4?token=mGJPRn-iU3y5niVnUXQBIAr_RDH-xM93xkuPLXTEtjTDdElelmv5aUIFErXffyYRncmBxqARc0SscJocCsZUpO4uYCBmRhw-SgVE-gx5QGi8BqX06a-Dt_FAT1wmhmSf1mOKQFqYXXaRDGY7HeGzKkbxeFlrGIVwfj2YbPgwTB2n3Ch95_zPDcVs6WzKMqzv-6bYeREsk2RN2IH2cpKJnZ0JZdE0H2CareqyGmnGdGNjIT-4ZZNcFqH7rkdHo34dXtTUg7UACfJ0YKoFeWaIPxX60NiDAzpoiIi8V65HqkxdNcc_n_QVr68Wyr-6s7SPTA-KJ7SGpazeHPV-N1ZXaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با این روش از آخرین وضعیت ترافیکی تهران مطلع شوید
@Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/446341" target="_blank">📅 18:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446340">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8671d75c.mp4?token=P29NYZBcgWLKDTQR_0KmO2A_quafcw3D6JUxCQaTIHq_Y5TYxDGewawwqweXARFCXJRZrlH4Zlh7IIbuUsuSaEnsLD2K_J-p7yNSl1WFBt_JXVHbQ01zrq93-KSW50qbA0PiNYNX4Uu-lG5dVhugbAwPTkg5xjxQQXAOssAvPzJN2FaycwTetfzN7hUQgz9t-JJPCZrpcHgUnyAhnOHKaxq3Z4Ry-PM_wxuwH_KBf1TpLX8w6ebdWDVqYbnbsjZcidUC7N8_m8lsyov1U6yYsi0k2kA5grEuZXgK5sm9Eqgz9brEQ7hVDgGsiZ3qnoBBOZ1qh0taAyDZqCNMumJMYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8671d75c.mp4?token=P29NYZBcgWLKDTQR_0KmO2A_quafcw3D6JUxCQaTIHq_Y5TYxDGewawwqweXARFCXJRZrlH4Zlh7IIbuUsuSaEnsLD2K_J-p7yNSl1WFBt_JXVHbQ01zrq93-KSW50qbA0PiNYNX4Uu-lG5dVhugbAwPTkg5xjxQQXAOssAvPzJN2FaycwTetfzN7hUQgz9t-JJPCZrpcHgUnyAhnOHKaxq3Z4Ry-PM_wxuwH_KBf1TpLX8w6ebdWDVqYbnbsjZcidUC7N8_m8lsyov1U6yYsi0k2kA5grEuZXgK5sm9Eqgz9brEQ7hVDgGsiZ3qnoBBOZ1qh0taAyDZqCNMumJMYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوشته‌های مهمانان مراسم ادای احترام به رهبر شهید انقلاب
در دفتر یادبود
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/446340" target="_blank">📅 18:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446339">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c077414a9.mp4?token=MTZSw3y7uqPU9q2kAkdLmB9mjGBdyWMiCcrveMlOi8TaN26r6cf7mKocagBeB_rvWZdp5OrEjPKxc8RAWGQnAN8IRyYEuO1Am7GyW-ep0xgJjTHFXbR6_gZAxRxUoD_vi_xwFJVCMlnjDfT7IsFkl_L3sKLVHUxMeyUFmbWT6uO0FZ8Z5ZTYa31qfLCCnXumiW7apZ04iHuhsBcIEw2-Uu0Q4NG6MfUVIOohDKSDFXA7Y5qrJFDbVyoNCiZ7ZFnfsmfYit8ms2JLm8SSo2kWyixNfQhvbX7bCSiDdOTEXvMhqUxd8qDhnVE7ceSi6wcMfXKU75jLIUiA1PlNChhKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c077414a9.mp4?token=MTZSw3y7uqPU9q2kAkdLmB9mjGBdyWMiCcrveMlOi8TaN26r6cf7mKocagBeB_rvWZdp5OrEjPKxc8RAWGQnAN8IRyYEuO1Am7GyW-ep0xgJjTHFXbR6_gZAxRxUoD_vi_xwFJVCMlnjDfT7IsFkl_L3sKLVHUxMeyUFmbWT6uO0FZ8Z5ZTYa31qfLCCnXumiW7apZ04iHuhsBcIEw2-Uu0Q4NG6MfUVIOohDKSDFXA7Y5qrJFDbVyoNCiZ7ZFnfsmfYit8ms2JLm8SSo2kWyixNfQhvbX7bCSiDdOTEXvMhqUxd8qDhnVE7ceSi6wcMfXKU75jLIUiA1PlNChhKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک‌های قالیباف هنگام وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/446339" target="_blank">📅 18:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446338">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=b2XtSF9jWwB4gPUxFSTGMrTtXIOrwac1VHo6f2hqmD1DrmuMHQMkDtXPxj0iOyhB48VFDuzXIMjExKJSFoX68OscwzLLafi3l_C4DYWt2VbHllGbeUt3Q0AYf8AlCtGVHq_ik6hR3xaOLomIdrLQTfCwvyysdGmRT_0_tllDGkPS9uiN85qlOkhhAqJRFcIKrFYkvmK-smQkv760PSfoe2gwDOamWsCcgTWLdaOMvS4R9vO553ZrdFEiChXoTpfPtRIRVafcabDGW36x2vrpZmkhdSWrqU2MvkcE201Vwo1Cxn_4imjAWjlt67lS_MIkj4YnhTr2D11vX1b2BwZodw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=b2XtSF9jWwB4gPUxFSTGMrTtXIOrwac1VHo6f2hqmD1DrmuMHQMkDtXPxj0iOyhB48VFDuzXIMjExKJSFoX68OscwzLLafi3l_C4DYWt2VbHllGbeUt3Q0AYf8AlCtGVHq_ik6hR3xaOLomIdrLQTfCwvyysdGmRT_0_tllDGkPS9uiN85qlOkhhAqJRFcIKrFYkvmK-smQkv760PSfoe2gwDOamWsCcgTWLdaOMvS4R9vO553ZrdFEiChXoTpfPtRIRVafcabDGW36x2vrpZmkhdSWrqU2MvkcE201Vwo1Cxn_4imjAWjlt67lS_MIkj4YnhTr2D11vX1b2BwZodw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندۀ ویژۀ دولت هند به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/446338" target="_blank">📅 17:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446337">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA1-eTVf7KbZiXnbXbEktveHEwtl1zrqX5kflNhVpVQL69GcbbI82ByK9qowkrCyI8bkpmI_4EqoXZeKkWmr64ziyUOwu8B3Sqwk8N7D4rj1QDWsjILe3L4_D71Ir_wnEkoJnHqdGTPTw6Ygn3bQrUvIYCYEhxvtUkzJNzn90YYJvr8GxU3k87Kk9TznlASQfiB-QKgZmCIdZPR3XyngPLhTCXscoLoW3oK4kFGJhNbFzbz0eRPOSetqvC4d45GILUlsCBmXzYBogPOiKCiZoJgg0nRXz4FBN8EgrPEERiYSYZ7KjbSIOAOlYN0KZyjKEqY9wwsdgPTNmz69GBCZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر شهید شدم به آقا می‌گم برایت موکب زدیم
🔹
از همان وقتی که خبر تشییع چند میلیونی آقا، دست‌به‌دست شد، تندی به دلش افتاد که خانه‌شان را زائرسرای مشتاقان کنند و حالا بی‌صبرانه منتظرند تا چراغ خانه شان روشن‌شود.
🔹
مابین شلوغی آماده‌سازی خانه برای میزبانی از زائران، محمدجواد ۶ ساله با حرفی همه را میخکوب می‌کند: من مدرسه‌ای رفتم که ممکنه دشمن موشک بزند؛ اگه شهید شدم و رفتم پیش رهبر، حتما می‌گم خونه‌مون رو تمیز کردیم تا از مهمون‌های تو پذیرایی کنیم.
🔗
حرف‌های شنیدنی محمدجواد و روایت میزبانی خانواده‌اش را از
اینجا
بخوانید.
@farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/446337" target="_blank">📅 17:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=sgJAZeUthsHQnS1M45hTlckE3sTNTqegmxx6vADanktHAbAzrlFZGKJC9hXuJfCQBk2KvfjDTFrHJU2NJOHVFtOGUKw8243dCDdROQLLNQAt5h5IWZmDpmKAZKxYAw-k6n6hII3VXNKqcnqrEBjQePTTF8nZUl7pXpquErsax2TI8vbevIhCpFcuUnJcnqPUFEwn68CJ1wdWpVVtcpEEL3Mk_Ez6z6SWC5QGR5kY5Mt60Wt-oTxdskTQetNpl64ecaRXxBMmMjq3D7Y9hyxq1PRy2IswEsHO1IkxSzeQ68RAxOmm8uU6I6Sxs-vUdh6vofjgRsD__cI4uB34SKp8NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=sgJAZeUthsHQnS1M45hTlckE3sTNTqegmxx6vADanktHAbAzrlFZGKJC9hXuJfCQBk2KvfjDTFrHJU2NJOHVFtOGUKw8243dCDdROQLLNQAt5h5IWZmDpmKAZKxYAw-k6n6hII3VXNKqcnqrEBjQePTTF8nZUl7pXpquErsax2TI8vbevIhCpFcuUnJcnqPUFEwn68CJ1wdWpVVtcpEEL3Mk_Ez6z6SWC5QGR5kY5Mt60Wt-oTxdskTQetNpl64ecaRXxBMmMjq3D7Y9hyxq1PRy2IswEsHO1IkxSzeQ68RAxOmm8uU6I6Sxs-vUdh6vofjgRsD__cI4uB34SKp8NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندۀ دولت تونس به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/446336" target="_blank">📅 17:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446331">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNAUtgMgpAS8J5KedvGVE-bOrbTfqgiU3j2YoPmdHANm9xN79c7doWfGWBdvoVA9Grd6YnUuJrcuhoCZ1zAwMQ6qBMJWkYPg8kRcUdEL98Yus4bdauMLRudbN9RiGiKtdNpc2UaN2x8mOkqlv2hIONNUdHLaeEb_Y4blZqkKsAwhbCKS6yfwfXUm1cwicOBjbuH7uUe6WjK9U4iLglTPIpib6tgZ5mZp7RvbZafVBTrzxW1st4B4NLICVIeQpYqWy_DE3jBjgQ8_qlmCl1OASjQiPmihjVy4zcvr6M-aAkomo14xj-cgKM3CZmv-U0LGGEigwXCA_AwHRa8A7pne3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pC4w3A_qeNvNH7uECN8Y-1TOUDb2K_h2awWBPru5yw6FdEvKCkyY8zQoDkCn_xVCEKIF0yQJ-hrrv2fB9V3ClIy9kbNLAUUWjhpa4PtTQ8H-8UN1J0QeR58j-lBm5NMsfVTRYIsflW6ayutwAV8C4goJQdkIvZi1rLT3ydsbHoGPWdwtfms9cBNadlE-lAs4X00RvRssHTbHoN1Bzp3Sc-SVNBlBogaRZ5ClnSZ41HLOto8gt5iHQRLVFPipd3hVvmvicCKctRZrNOJ31s3RYX632sjGJ5im95NX7UAsBQXC_WI4S1iJAfs7WNS8uzcttMmktD0ytQWrDz7z5nLVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNAO2O84qUO948o95O6Mnh7Adjes5V_vLfG-9-u9WT8ZfX4w8x5EvxElKh8UbbSf3igFu_1puT-8bAXZUuj2vg7uONd5bYa0Rieo5NmpIGxf2PMmOcGvf77KoFFKj6enJ7pZQBQK489iAM7ELb2xyXvbVothmHqs3RHrgb8Q2bZNLQP64i6uOf6MKHABx7QyKvjQ-nq_9FVlyP11bnQ_WgvavurUIrXZm1rRzW_1CQ_BS2YxhujC5l6WsMX5TpNltaLZ0cczAErTUQxCiG_8CyS8dY_6OCshjFOAjDaMPhk2noQd_tPvLSoS3VDsb-6n8nvnTlfinRAuV0KMElcSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTv_BnbFZt1ATG3ESg1fvKUbw79itHYy3bP2sbLXSr2ELfSwP70doTBKeTTGDUtBu4xJ7ioigaDyk_Q_IPbz9KP2W8PiowvF4xN3PEdPoRDoYVzRRBIvOCDtT68jiwSi4hLI6ygtKmOnmMWrMUtkBP-kNCVc4D2edssrM8FaObxJqQmSX0EoSw5niVQDe5tNFu5o4nPsP_FSaTkBrzEOvshm6HdTrVEnM5CvHLc1zFGCDN0gfrjPU7QD7xqzKo99p8AGcROvsTtHhXMhhetuIViGUWmpBStrmfE2wwAAHOyRhCWfftH82kAeoY3SFoLX8-vPvlyJzHNHyn5zvmaIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRikUrhwOauQMoVYKcfeKPqi9pIm5BcNyts6N-FYxcw64_Et6ze2yZXAfmyExVvBU-qoijFtjGPWcJffMGxjjxy3_kCRUBiW8A1Lz4UlshOchEBfECQIFO7jguEkRQdry2qwaVvMoTVPS2o6axXpyKcn_W3vWkeoxWIIOFa0m6Aog_yfApIth-DGz8TfORerbPJmbJXv6anb1Iz5OdHk5Of2byuexhM-Q-n4BQdRTDxvnCfvLKhTIwlI2RRtD6d4lYzsbQTAHJPBS9qqTfxuAmV-zj7q-mR4PU21I0vU_b5bZBFMU6ckUR2mNhZe-keyvVufl3EXWX2xlAMZHc3F0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گلباران محل شهادت ۲۹۰ مسافر هواپیمای ایران توسط آمریکا در سال ۱۳۶۷
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/446331" target="_blank">📅 17:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446330">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=ol5DNicAVONYSM6dEAN5AMM8nCc6yqxYIz7VGR0sKZiJqYA4k4MtdXidLbn73vgdl_70MmbXHLOYMO5yOq3yYVlUzyNW-C_wHxGCp4Ja4EE0r01A86Ks1wa8Z0318hXFbeW_HmXLQvgv8z9p90XVJwKqXNxe11cs62eRYkhj4d04CkUzLhncM48xHRJRLSHVkgiZrXOREsRhGRPsKb4ZrJXhra43pXC5Zqs83NnW16o_gHidrq4wI-oIf9f_nIq2jscajuE8aoijvD301Z2fpuMF9aTR_WL22mXu-gNAR65ur03XeApVcyY7EKdbR4yJLagew21Nai85m5Ch9dBCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=ol5DNicAVONYSM6dEAN5AMM8nCc6yqxYIz7VGR0sKZiJqYA4k4MtdXidLbn73vgdl_70MmbXHLOYMO5yOq3yYVlUzyNW-C_wHxGCp4Ja4EE0r01A86Ks1wa8Z0318hXFbeW_HmXLQvgv8z9p90XVJwKqXNxe11cs62eRYkhj4d04CkUzLhncM48xHRJRLSHVkgiZrXOREsRhGRPsKb4ZrJXhra43pXC5Zqs83NnW16o_gHidrq4wI-oIf9f_nIq2jscajuE8aoijvD301Z2fpuMF9aTR_WL22mXu-gNAR65ur03XeApVcyY7EKdbR4yJLagew21Nai85m5Ch9dBCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندۀ ویژۀ دولت مالزی به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/446330" target="_blank">📅 17:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446329">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سردار سید مجید موسوی: جانفدایان امت در نیروی هوافضا خوشه‌های خشم را بر سر دشمن آوار کرده و خواهند کرد
🔹
پیام فرماندۀ نیروی هوافضای سپاه پاسداران به مناسبت تشییع رهبر شهید انقلاب: اینک که با دلی خون و قلبی محزون، رهبر شهیدمان، آن یگانه دوران را به جایگاه والای ابدی خود بدرقه می‌کنیم، با خدای ایشان عهد میبندیم، تا تحقق اهداف عالیه‌ای که در طول زعامت شریفشان برای جامعه اسلامی ترسیم کردند، لحظه‌ای از پا نخواهیم نشست.
🔹
خط ما همان خواهد بود که رهبر معظم انقلاب حضرت آیت الله سید مجتبی خامنه‌ای اعلام کردند: هر عضوی از ملت که توسط دشمن شهید میشود، خود موضوع مستقلی برای پرونده انتقام است.
🔹
سیلی‌های سخت و غیرمنتظره‌ای که دشمن دریافت کرد، پایانی ندارد، چرا که مسیر مبارزه حق و باطل پایانی نداشته و نخواهد داشت. و به امت شریف ایران اعلام میکنم، جانفدایان شما در نیروی هوافضا به نیابت از شما خوشه‌های خشمتان را بر سر دشمن آوار کرده و خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/446329" target="_blank">📅 17:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446328">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTujITnQG_HL_EkSmE6IFoxsPXVu4oAHVp2qXRjhqq9HDSsA_mHPFMuTEDsV2F2Zz5Sh3zE2ZrWPeHZ5l-CsQYD8_eOfVvEN4j87BDf20G6vMRbXDeol7OCaToQ2w-U0RSOy_f5IGx_deUqKtlUk8J0jp1pBHOrF0c4RLh346Xw3qGKsNlx6eSuR71MkCpmtXLcEva133GrQKte-sKuZNMvl0zlTi0TNVemt6LhyfXw7FwfJQUefTLPY2Xtaf9ejr1u-b_4IwwFvbAQrpcdaKULvTwD6_cfWdnnTq7ddf4ow4ulUIa2QoB6OrNa7TXRC1QCFQJ5pzO54VRsjGafQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
فهرست مجتمع‌های خدمات زائر در ورودی‌های شهر تهران برای زوار و شرکت کنندگان تشییع آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/446328" target="_blank">📅 17:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446327">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=rVAN8aXRoQz9bktmh_scnmrCWJVzqfF5EWeqs9kEvKXduijrtsTctFVtVbUAAaiJoO6WDNMkaK_ylA3uQmDYa3jcxI_vCaqc3Wwrp3X0Z0ugwh6NozprBPFZsfvk4ZEDm5ybdXi9paPhKiN9f7iIvA3uFh8wvYFWjxJDMw0EOfbYWqij0VmjOHMbrscFnSA9_Dw2fM-fAcgeJh7GZQXV8Cnau6_lE90JgZd5rRcssWdKzJMxS8fKRVrUs-mFjCtn0O7vbMwYwu5yOytMm3GSbkcK-tp33KlRjwj4CYYfdjl55YJ96E2Hu6fcn3qm5I5M9nHO_jUZDh_nc3R-ryoozQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=rVAN8aXRoQz9bktmh_scnmrCWJVzqfF5EWeqs9kEvKXduijrtsTctFVtVbUAAaiJoO6WDNMkaK_ylA3uQmDYa3jcxI_vCaqc3Wwrp3X0Z0ugwh6NozprBPFZsfvk4ZEDm5ybdXi9paPhKiN9f7iIvA3uFh8wvYFWjxJDMw0EOfbYWqij0VmjOHMbrscFnSA9_Dw2fM-fAcgeJh7GZQXV8Cnau6_lE90JgZd5rRcssWdKzJMxS8fKRVrUs-mFjCtn0O7vbMwYwu5yOytMm3GSbkcK-tp33KlRjwj4CYYfdjl55YJ96E2Hu6fcn3qm5I5M9nHO_jUZDh_nc3R-ryoozQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام معاون رئیس کنگرۀ ملی خلق چین به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/446327" target="_blank">📅 17:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446326">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=eEPU4fkeeBPGkECKC01BbUJIPbeh19oVZnUomOShf7jm4bOj56jPIfe0JWAt1Z17g22CLQbETt-z2hRCYcMhJT4VoT6IYar_yxGdFOd-ozck3pKTactNVGW9hlDpM9b1mqAWY5A-7b_VczkTfmwLtPf6RoM4-B3GbWtfTm2h3-cIFtMzUNQ76QPG8DZw0ZTrPzIEtaDZCONS0PorqEYfQS5F1k6WyBfU0RuYjvMlEGWOUPWB6j5ZzOwfrQ0M4lqQTHp6vbR3zI4wZqTjQPC7PTFsV5jqM4414QYyojkDspWOlC78zPIOYWm9WC6B7if1bIyNDr3jQPMNuGVMKyhV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=eEPU4fkeeBPGkECKC01BbUJIPbeh19oVZnUomOShf7jm4bOj56jPIfe0JWAt1Z17g22CLQbETt-z2hRCYcMhJT4VoT6IYar_yxGdFOd-ozck3pKTactNVGW9hlDpM9b1mqAWY5A-7b_VczkTfmwLtPf6RoM4-B3GbWtfTm2h3-cIFtMzUNQ76QPG8DZw0ZTrPzIEtaDZCONS0PorqEYfQS5F1k6WyBfU0RuYjvMlEGWOUPWB6j5ZzOwfrQ0M4lqQTHp6vbR3zI4wZqTjQPC7PTFsV5jqM4414QYyojkDspWOlC78zPIOYWm9WC6B7if1bIyNDr3jQPMNuGVMKyhV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام معاون دبیرکل سازمان همکاری اسلامی به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/446326" target="_blank">📅 17:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446325">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f186ac745.mp4?token=nO6X4tRCtWgYHsnc6H3qFzbaVoNl3ILqu7l2AOm-HWD2eZQ-uAno9cr0dYcRCUWtvnFw0tE0O3rfx4XyImWHWIdQZCVvxB8uFKbO2ncMyCIA3L9aMwzGNieLX72HSarPjI80OIiq8K5_eCtRSP2LEeIvJ16ObMuVqzkkej6twMOaOd0BB--WPL36mWWovU0fEbjMCh5S4NlyVs0Egtc4cHRVfe5dRekkUTM8XnGdGLXLi_wnSwF7zSV5OLEo9c34hDHq98N9H00zmwRWVdgnLKEh8Jt-EkvkgLHkQmwBOpf67yCd0pXDvUB2AENO9aJeT_MwXYvZBlgGZbz6UXHIFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f186ac745.mp4?token=nO6X4tRCtWgYHsnc6H3qFzbaVoNl3ILqu7l2AOm-HWD2eZQ-uAno9cr0dYcRCUWtvnFw0tE0O3rfx4XyImWHWIdQZCVvxB8uFKbO2ncMyCIA3L9aMwzGNieLX72HSarPjI80OIiq8K5_eCtRSP2LEeIvJ16ObMuVqzkkej6twMOaOd0BB--WPL36mWWovU0fEbjMCh5S4NlyVs0Egtc4cHRVfe5dRekkUTM8XnGdGLXLi_wnSwF7zSV5OLEo9c34hDHq98N9H00zmwRWVdgnLKEh8Jt-EkvkgLHkQmwBOpf67yCd0pXDvUB2AENO9aJeT_MwXYvZBlgGZbz6UXHIFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام دبیرکل سازمان همکاری اقتصادی D-8 به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/446325" target="_blank">📅 17:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446324">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/890cd49f92.mp4?token=EIaW0a85oZthgVViWYo-ZbBpSklfp8hJmLOcM6IwS3slyWyR5GPKylUXrNTdTr6_r10PVGBOlGvwzhwxdTn9--6KvxBtLa9WneqPcfu4pIDQLIuTkxF72YC6ABGWzSI8xQEjXgbYg_B1OfU8RVuVtKAyusKzIzI9rxRWaVRWXNZ5RpuxFvUjScuxq3oD3Mr7FEEOXezvUg1pzkDY_fRHsPoxwOEDWljkTAdwDXP20S81ESYVejd0g4nAzelTczquKclja6u-8Q_hxmMhiU3SvK43fa0rvQvMRtPEAnnUcy_IKkKg6puRuMpy_jj14WYrhlWGtyvbqugKAaoZ3Ff3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/890cd49f92.mp4?token=EIaW0a85oZthgVViWYo-ZbBpSklfp8hJmLOcM6IwS3slyWyR5GPKylUXrNTdTr6_r10PVGBOlGvwzhwxdTn9--6KvxBtLa9WneqPcfu4pIDQLIuTkxF72YC6ABGWzSI8xQEjXgbYg_B1OfU8RVuVtKAyusKzIzI9rxRWaVRWXNZ5RpuxFvUjScuxq3oD3Mr7FEEOXezvUg1pzkDY_fRHsPoxwOEDWljkTAdwDXP20S81ESYVejd0g4nAzelTczquKclja6u-8Q_hxmMhiU3SvK43fa0rvQvMRtPEAnnUcy_IKkKg6puRuMpy_jj14WYrhlWGtyvbqugKAaoZ3Ff3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
آغاز مراسم تشییع پیکر داماد رهبر شهید انقلاب، شهید مصباح‌الهدی باقری‌
#باید_برخاست
@rahbari_plus</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/446324" target="_blank">📅 17:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446323">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a0146f38.mp4?token=jERDAg7aGR8xyuqIQgw_BPUUnSQWBGPYXzT3CBPWyVE_9hQ9NFpVwNNmzHOvtepcWysNh7uGhtTGCRRgc9aNbl4DnTPD706yKOsEE0dzifPyhaanitgWotXTc7uAugvtmL1ktdUcYM6JE0wu_6j_nDrrwRlpk38fOJWrDfvQrARen8G8zVeqUke-5QHJ_N4bJLLycDxRDijtmXjhrvQvZcZkDL7Dwu_ED5bb7AJe_5xvNKj4zdlwA5RyHTjNKCKocD8aVhySoCVfT9EgL5YE76K6E-thwEx-u6OlRdi7dVic-hHIKZ_YlxZ2ASGe9ggAyNGLE_cvQ5muTEPbzkLn1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a0146f38.mp4?token=jERDAg7aGR8xyuqIQgw_BPUUnSQWBGPYXzT3CBPWyVE_9hQ9NFpVwNNmzHOvtepcWysNh7uGhtTGCRRgc9aNbl4DnTPD706yKOsEE0dzifPyhaanitgWotXTc7uAugvtmL1ktdUcYM6JE0wu_6j_nDrrwRlpk38fOJWrDfvQrARen8G8zVeqUke-5QHJ_N4bJLLycDxRDijtmXjhrvQvZcZkDL7Dwu_ED5bb7AJe_5xvNKj4zdlwA5RyHTjNKCKocD8aVhySoCVfT9EgL5YE76K6E-thwEx-u6OlRdi7dVic-hHIKZ_YlxZ2ASGe9ggAyNGLE_cvQ5muTEPbzkLn1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندۀ دولت و پادشاهی تایلند به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/446323" target="_blank">📅 17:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446322">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dcfe28f4a.mp4?token=Rprwm9JIutlZtT6QtgBCOVxWMGDiBljd2A68pHHxmfN0DPb0J5cdhPSlYvPL1sO1pI7NVvEfiFHbhNtVJWyH0wxdMhws4_mVvWKEISEg4YtvJfF5UARG8sjioWfxapzUju0t4fYX1JV8rAnXKUvlnHsFT87dLHYk-LtSyf0-lKJ2DPB_xkdA2NK_P_PL1vP8u7pvhpD-hVQZb70h07A9pWQ86116s20YLu0fvFoBAZPXmMRfGtO_ohjHaqs99SN45JClY8ntRvApgSh6KJseDX4rU6VxFCKUtfg_TppIMEX88YLxBwEpIr0Hwb6UuNUcb14trbjdkg9oX235Z01feg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dcfe28f4a.mp4?token=Rprwm9JIutlZtT6QtgBCOVxWMGDiBljd2A68pHHxmfN0DPb0J5cdhPSlYvPL1sO1pI7NVvEfiFHbhNtVJWyH0wxdMhws4_mVvWKEISEg4YtvJfF5UARG8sjioWfxapzUju0t4fYX1JV8rAnXKUvlnHsFT87dLHYk-LtSyf0-lKJ2DPB_xkdA2NK_P_PL1vP8u7pvhpD-hVQZb70h07A9pWQ86116s20YLu0fvFoBAZPXmMRfGtO_ohjHaqs99SN45JClY8ntRvApgSh6KJseDX4rU6VxFCKUtfg_TppIMEX88YLxBwEpIr0Hwb6UuNUcb14trbjdkg9oX235Z01feg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام فرستادۀ ویژۀ رئیس‌جمهور میانمار به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/446322" target="_blank">📅 17:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446321">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc21aa2be.mp4?token=idNOUY_gsL6INlccukhF9UNu5HEHKbo5pxuONFIMlpP75rn5iPKGZ-GTFXOFJfPhTWv0t7r4LzlH_GqQSs0xUfPMLOwqi5soAIDDDrQ7uWE8C8qM6fw_AmQxIF0vQMBbYG71EVwxnZ51JT0vMrW_pOHNMlxw8N-HVJKcyeJsEdJ66kLWMFVW07KkITloFFfN6l5g8prLOGSNbri7vDvXmIyi6Kzkpd1TCBQ_yOY9boIIJNqdvarcGzr6Td-88ySEXT_XAkct6wSrVFhetoffP_HyQCBcngBssN6cwMfExrfrXCDYhWAvqlgx0Aqshwx0bjwkp_C79zPzwSbu3bxJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc21aa2be.mp4?token=idNOUY_gsL6INlccukhF9UNu5HEHKbo5pxuONFIMlpP75rn5iPKGZ-GTFXOFJfPhTWv0t7r4LzlH_GqQSs0xUfPMLOwqi5soAIDDDrQ7uWE8C8qM6fw_AmQxIF0vQMBbYG71EVwxnZ51JT0vMrW_pOHNMlxw8N-HVJKcyeJsEdJ66kLWMFVW07KkITloFFfN6l5g8prLOGSNbri7vDvXmIyi6Kzkpd1TCBQ_yOY9boIIJNqdvarcGzr6Td-88ySEXT_XAkct6wSrVFhetoffP_HyQCBcngBssN6cwMfExrfrXCDYhWAvqlgx0Aqshwx0bjwkp_C79zPzwSbu3bxJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدودف وارد تهران شد
🔹
نایب رئیس شورای امنیت فدراسیون روسیه به عنوان فرستاده ویژهٔ پوتین، برای شرکت در مراسم وداع رهبر شهید انقلاب وارد ایران شد. @Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/446321" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446320">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08572f73b5.mp4?token=tnYet_9eZEsfCcvfo2mcTwVn5XBWJPHtkHKWyADgGg0jol8sRB0Q8ZAtU10y0LWDw9Ly4984fwv2UXyTTYKb6XC8bwmj1TCUHl52CjA2sV0uO8d7nNXWeBP65BOdagkQ18Yy2rgcJ9MbJVLOvLp3pdCKdVOBNz3RAB1RltQ68J6diiqOLWW_l0P9V6T1rp-vZuVE_SXrCSeo27kotZrovLPgDowhzLeIbSllcW5EMISZjwHou9zfAcDSudG-lTWYg0RLMxKM2X3CeXSX1hBtLlIAFRjIBGyEzq97MQsjSUe28TLcXbr-O46ybKjX6AMLBz2uu8iWWvzNF6euvxu5bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08572f73b5.mp4?token=tnYet_9eZEsfCcvfo2mcTwVn5XBWJPHtkHKWyADgGg0jol8sRB0Q8ZAtU10y0LWDw9Ly4984fwv2UXyTTYKb6XC8bwmj1TCUHl52CjA2sV0uO8d7nNXWeBP65BOdagkQ18Yy2rgcJ9MbJVLOvLp3pdCKdVOBNz3RAB1RltQ68J6diiqOLWW_l0P9V6T1rp-vZuVE_SXrCSeo27kotZrovLPgDowhzLeIbSllcW5EMISZjwHou9zfAcDSudG-lTWYg0RLMxKM2X3CeXSX1hBtLlIAFRjIBGyEzq97MQsjSUe28TLcXbr-O46ybKjX6AMLBz2uu8iWWvzNF6euvxu5bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام وزیر ارتباطات صربستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/446320" target="_blank">📅 17:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446319">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df855a6622.mp4?token=YncLd-BRVK8ivEdMj-OGCOn7kxOJbhBPpRAYrqSm1eEy73lX-s_zK4CEZ-UA4b1KLsusuxIhhdB7QIcJR2Al15_UwImnGlLhGM8zOziOQ2Kx-Ur1uV7Rhc0Er6vCNysH2ecDaqdANFsd74RboBh949EY3sX5m2bdJjFoV4MsxX7ZtZujVVAG42WZneGWzZamf6IqbQshl3r4Q25eM7x7wBOyGYkf5Szahu5IQP3LRAOW-5yjt1A3TvIYIxaZBsZXqKKnJzwYp6_6iSrcMst2g83vqn77ZcY2L-jKU-M2OhW8yoq6tu0Sv5zvIs6FXgoE1W-L7udlwPaWgNEj0VAEBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df855a6622.mp4?token=YncLd-BRVK8ivEdMj-OGCOn7kxOJbhBPpRAYrqSm1eEy73lX-s_zK4CEZ-UA4b1KLsusuxIhhdB7QIcJR2Al15_UwImnGlLhGM8zOziOQ2Kx-Ur1uV7Rhc0Er6vCNysH2ecDaqdANFsd74RboBh949EY3sX5m2bdJjFoV4MsxX7ZtZujVVAG42WZneGWzZamf6IqbQshl3r4Q25eM7x7wBOyGYkf5Szahu5IQP3LRAOW-5yjt1A3TvIYIxaZBsZXqKKnJzwYp6_6iSrcMst2g83vqn77ZcY2L-jKU-M2OhW8yoq6tu0Sv5zvIs6FXgoE1W-L7udlwPaWgNEj0VAEBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نایب‌رئیس جمهوری یمن به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/446319" target="_blank">📅 17:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446318">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1bbyHvVAqWgWERkHQz_nuIu8w6KES0Bn6WMv6lb8xRM2NBxly7tDcRD2OiJdyWB3-sIG7keojhdxPh8bMRqYTEk-Wqt3njF9GcK1wCVs7s3wKm_ubM4hyIDBKdyiIStR3uFadjHb9MKll8gxBI_kLkUtAW84j7T5ZiSCyZCtJ71GmIFdadkMcuLIN6n6UAQIrDNYmD24pbWDEptLbxjAVqssr2XdVsjGAtaU1Nfcl9h8MGVKpQ9hgYxVEpuh17KYTpl7BccvetF72Nb7a5TH_I3QziNI2EF8a6JfFaCO6uYRDrdA_VLELQd8bd21IwCmSbczllfEjeYN7POtMtCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های خارجی مدعی تحویل ۵ فروند بوئینگ به ایران شدند
🔹
رسانه‌های خارجی مدعی شدند که با تایید دولت امارات، شرکت ECT Aviation Support که در این کشور مستقر است، تاکنون پنج فروند بوئینگ به ایران تحویل داده است.
🔹
بر اساس این گزارش‌ها، این پنج فروند هواپیمای پهن‌پیکر دست‌دوم بوئینگ 777-268ER که پیش‌تر متعلق به شرکت هواپیمایی عربستان بودند، به شرکت هواپیمایی ماهان ایران تحویل داده شده‌اند.
🔹
گفته می‌شود که دست‌کم دو فروند از این هواپیما‌ها در فرودگاه مهرآباد تهران هستند.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/446318" target="_blank">📅 17:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446317">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=qcxjsbM9AQWYTh84FCXfWVt-nNx-61ULvyS8tkCLG8SpgevuU2AeiqdnVsyvYKNAl-k6RexGRfgwBjtCI2uO0AaoVTIUD9TEAiBQ5kZu8R_jq9Rtro9LkS2gNETtJdODXTUKteDaJBmmCaBNVxazB74bWsAAFZOBp-iHRGsdOjoC5vh0e0foUuGhDfrFpAYTfmlCTWXE19Ux7HLYPvBBDsBH00rSBTgRrpYYaLEISWN9HH1MRwWcECv0sms-Who6UKL45lLdfgaM1Px-zsAv_X5eCDEzzRsB-XXMKNk3ABS_XkxbhU-qPlRXC9OeUgH4o1DQljhgPpA_Yfqy7UWUPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=qcxjsbM9AQWYTh84FCXfWVt-nNx-61ULvyS8tkCLG8SpgevuU2AeiqdnVsyvYKNAl-k6RexGRfgwBjtCI2uO0AaoVTIUD9TEAiBQ5kZu8R_jq9Rtro9LkS2gNETtJdODXTUKteDaJBmmCaBNVxazB74bWsAAFZOBp-iHRGsdOjoC5vh0e0foUuGhDfrFpAYTfmlCTWXE19Ux7HLYPvBBDsBH00rSBTgRrpYYaLEISWN9HH1MRwWcECv0sms-Who6UKL45lLdfgaM1Px-zsAv_X5eCDEzzRsB-XXMKNk3ABS_XkxbhU-qPlRXC9OeUgH4o1DQljhgPpA_Yfqy7UWUPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام وزیر آموزش عالی گوام به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/446317" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446316">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3533d1cf.mp4?token=mzicqYbQCAuc7yoH_6jk7fYqrOOauk3z1OCdxd2H-wORqZ12aRIuEoQqtDES8Sn2HvHDwa83AUR9IkZQrZwUPym0XNJxFMJ2uJIgIE0WrIIXvLbrbRtY4XDb7wJ_y9YpT9Qj3Lwx5TBPxIvJoQYAdoG1nv9iUOgpM7y_irlA64xuVSrvZWBZRTcZo3KjvRBFWPmVYh1BQcEEEkU38-9BUZdvqMckl_9B1r9dl7F86rsyIgnXD7pzGeCSCtpjCpwasduziFwLObOIGjOV1i3-nEFTd3UB5KEWN65RCXG_xEH7Bg-2hKC-nndlLcfKmFE_NO70yr2NxT-7pXMszco1Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3533d1cf.mp4?token=mzicqYbQCAuc7yoH_6jk7fYqrOOauk3z1OCdxd2H-wORqZ12aRIuEoQqtDES8Sn2HvHDwa83AUR9IkZQrZwUPym0XNJxFMJ2uJIgIE0WrIIXvLbrbRtY4XDb7wJ_y9YpT9Qj3Lwx5TBPxIvJoQYAdoG1nv9iUOgpM7y_irlA64xuVSrvZWBZRTcZo3KjvRBFWPmVYh1BQcEEEkU38-9BUZdvqMckl_9B1r9dl7F86rsyIgnXD7pzGeCSCtpjCpwasduziFwLObOIGjOV1i3-nEFTd3UB5KEWN65RCXG_xEH7Bg-2hKC-nndlLcfKmFE_NO70yr2NxT-7pXMszco1Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس سنای پاکستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/446316" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446315">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de0472153.mp4?token=Yt0ozbFeDZGM4xam0W2FnJcRvSePHhQkSKKQOmu9IrCKrYvcZ0M6iVVlu8uGWcMeDcXJhhcMwBge5g-B8HYvYULFOJDOSCLucRhC_d4e1lvtARgCec-lx5xspqTTt9yB1EbYIvOF6Lr5NxYEMzhDqjkYXwQ3f2uQ9Hz2c4ojGz9cTw2e23ke9y2NDgtBMP-7jBDof35SXb6FnbL4PHdek0UPs7-_8s_SmS7zqqOcbq03EnnwnxDbtSyvUvn7XIcfQOfbWyGahGjQJCyIB78E6R8mZgW49oiep3V2OjXA06DEZVEr452wmC18ugYcbRYoPcIPNoBLUGKZvBa5gmRzlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de0472153.mp4?token=Yt0ozbFeDZGM4xam0W2FnJcRvSePHhQkSKKQOmu9IrCKrYvcZ0M6iVVlu8uGWcMeDcXJhhcMwBge5g-B8HYvYULFOJDOSCLucRhC_d4e1lvtARgCec-lx5xspqTTt9yB1EbYIvOF6Lr5NxYEMzhDqjkYXwQ3f2uQ9Hz2c4ojGz9cTw2e23ke9y2NDgtBMP-7jBDof35SXb6FnbL4PHdek0UPs7-_8s_SmS7zqqOcbq03EnnwnxDbtSyvUvn7XIcfQOfbWyGahGjQJCyIB78E6R8mZgW49oiep3V2OjXA06DEZVEr452wmC18ugYcbRYoPcIPNoBLUGKZvBa5gmRzlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام وزیر دفاع ملی لبنان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/446315" target="_blank">📅 17:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446314">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c43e53cb8.mp4?token=Cpk9Ll6KtKQvrjqZjudkOcoyCi22C-sNxegj9WUOPujjU7qP0cqoa--Q06ha0oeahM0JhOLNMluNkV9g5QuRQlXoFHdGksxIHLpiTx9ZfKObgkCJ_IzFODteuDX1izBmMd7m82f9XlzKqALjpV_7qRw4MIACkOALY0Ux2RbIriH1HZR834rnTnf9qEVJOXx0GlbCif7Wf7nOyLgMtXzSGDOX19AlL2YWNBi2ZZV1FqT45nVhJqZVhwFnWJ96vfrxzvEfTTTcVNMRI2GUPRR_f_-q-LDHlX6BBEeISDY4iBM7aByNvQn2GttvhOyQ_gAIU5U5HhYmrqYG12eNQxuqAjvwLkEmdUWyX2uvt8u5TjDLRWt9dG2hBKl5huP4FrEkUtba8-y_Sn_JJUlzVnp-vAK-FPA4ZAqFGmLHAKzBI9HpE6a1asZWGIPKinh1Z6k8K4WcirmvYhYLbJBcfY1hISwol2fP7PH3lCl4o5pAvl5XsflsuXmCLhEUewzDC_pmXdTT0NayFlLghUEmak-W8MHt4Apkrdj6YMop3jPrdg8Mp9xZ7usg2VwZBferPfbF-QksYHpyKwjAixPO2SBqQAZY1E4VznzqTd0qSniOcN16Ic0PBK7Wqp9hBTV_GHcuqLWz1stuAOyDy44WbJQgbx7Q_NXnQzMbLUVJUyRhTpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c43e53cb8.mp4?token=Cpk9Ll6KtKQvrjqZjudkOcoyCi22C-sNxegj9WUOPujjU7qP0cqoa--Q06ha0oeahM0JhOLNMluNkV9g5QuRQlXoFHdGksxIHLpiTx9ZfKObgkCJ_IzFODteuDX1izBmMd7m82f9XlzKqALjpV_7qRw4MIACkOALY0Ux2RbIriH1HZR834rnTnf9qEVJOXx0GlbCif7Wf7nOyLgMtXzSGDOX19AlL2YWNBi2ZZV1FqT45nVhJqZVhwFnWJ96vfrxzvEfTTTcVNMRI2GUPRR_f_-q-LDHlX6BBEeISDY4iBM7aByNvQn2GttvhOyQ_gAIU5U5HhYmrqYG12eNQxuqAjvwLkEmdUWyX2uvt8u5TjDLRWt9dG2hBKl5huP4FrEkUtba8-y_Sn_JJUlzVnp-vAK-FPA4ZAqFGmLHAKzBI9HpE6a1asZWGIPKinh1Z6k8K4WcirmvYhYLbJBcfY1hISwol2fP7PH3lCl4o5pAvl5XsflsuXmCLhEUewzDC_pmXdTT0NayFlLghUEmak-W8MHt4Apkrdj6YMop3jPrdg8Mp9xZ7usg2VwZBferPfbF-QksYHpyKwjAixPO2SBqQAZY1E4VznzqTd0qSniOcN16Ic0PBK7Wqp9hBTV_GHcuqLWz1stuAOyDy44WbJQgbx7Q_NXnQzMbLUVJUyRhTpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای بازگشت رهبر شهید از قم به مشهد به‌خاطر پدرشان
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/446314" target="_blank">📅 16:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446313">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135827909c.mp4?token=uvYjgZT_P2HRrYXRL2aiUqSOE50fTSN0DcjtwFLP8B4gxixg-kwV0wAIaijtNBocJY3sihe3dcrzCgRsMyHdFpfXofjiiNoH3Aaf95qAHFSvvIXJk2Ta246cF2CjR9d8fontt1LqG15weDXc0svbaIr2w6yzoz9CDtz56CA8fgtK7yM6_TgoAFsAG4yiGCpnrW3xO7taSeCmQ7RyWxp-OkzaX__oVT1RggeXSZxD5UZSokbJBbHwxcg8PXyB08MLY9wzV7hs6b-sQzLbe6p1evXEVULut_3EvM_UlSNIyU1JFbOtNYQ7ErOxvvHu460ziLKnivw4-JizIfZBJWHDIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135827909c.mp4?token=uvYjgZT_P2HRrYXRL2aiUqSOE50fTSN0DcjtwFLP8B4gxixg-kwV0wAIaijtNBocJY3sihe3dcrzCgRsMyHdFpfXofjiiNoH3Aaf95qAHFSvvIXJk2Ta246cF2CjR9d8fontt1LqG15weDXc0svbaIr2w6yzoz9CDtz56CA8fgtK7yM6_TgoAFsAG4yiGCpnrW3xO7taSeCmQ7RyWxp-OkzaX__oVT1RggeXSZxD5UZSokbJBbHwxcg8PXyB08MLY9wzV7hs6b-sQzLbe6p1evXEVULut_3EvM_UlSNIyU1JFbOtNYQ7ErOxvvHu460ziLKnivw4-JizIfZBJWHDIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام دبیرکل سازمان همکاری‌های شانگهای به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/446313" target="_blank">📅 16:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446312">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e65d36ac.mp4?token=v0hJxCVk79ZDWHk0Rnf14h1z1kIEvguTa0MlEP3sv7NN2eJTZ7eIbrfWrK02MYYwWAiFr03NtKgQMZyZmxvmvvtwkDbIpPgHOTXZJI0xdmkIiyGXiWeOlR6Zey2yBTxNLRrxfipDU0Mvlw1dhwir0J5_POLoL8v51HC6GFxOYtB5ohlc_wtMvp8ucd-iDN25dKOal2tT26yL_QoWt_jRiygSPUjbvl_ayTRE_FBBb1FVCLVUbxjkX-Y1kuI-IJNk4wT7_o_l_xZYsfUrjGIJIRkzn4AnMC8Pcu1tnpYjPm-23huG3H4s2uw9eoQWa4YXSLOq5OSDYuSCpseOjjhKWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e65d36ac.mp4?token=v0hJxCVk79ZDWHk0Rnf14h1z1kIEvguTa0MlEP3sv7NN2eJTZ7eIbrfWrK02MYYwWAiFr03NtKgQMZyZmxvmvvtwkDbIpPgHOTXZJI0xdmkIiyGXiWeOlR6Zey2yBTxNLRrxfipDU0Mvlw1dhwir0J5_POLoL8v51HC6GFxOYtB5ohlc_wtMvp8ucd-iDN25dKOal2tT26yL_QoWt_jRiygSPUjbvl_ayTRE_FBBb1FVCLVUbxjkX-Y1kuI-IJNk4wT7_o_l_xZYsfUrjGIJIRkzn4AnMC8Pcu1tnpYjPm-23huG3H4s2uw9eoQWa4YXSLOq5OSDYuSCpseOjjhKWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
من خود به چشم خویشتن دیدم
که جانم می‌رود
@Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/446312" target="_blank">📅 16:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446311">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0695c6fc2.mp4?token=Wa2tl88Kd4o3k6TeCmkNzcIAEPeWqY2_iBsc-9eUQtLMWr6GSRtD-HTQXkejYGEMrmuBnYGhbRcqSgRyanzO92ZnZYT-lnZ8LwBAmvEMdtBNX4HwAGaU6xW52HPx4buGg7I1j9CgNjCi0xrt9OuZa9LJddMs3ouGEa5YCXsdLhahtcuoQZhn_ZhSDrtRrzJ_SQStKmISRkwbZ3w3KkFLUIV2EzJRKfVec-p40yU-WlWqKopwYweh7wjub13zyMDebCDBpZ6mNB3kxvBNhJb_jd2ha30-XVMzsWbZsaytnPpjRrohg1OThnRfPBh8mnYLxo0HKID0uVO2adHwQNR56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0695c6fc2.mp4?token=Wa2tl88Kd4o3k6TeCmkNzcIAEPeWqY2_iBsc-9eUQtLMWr6GSRtD-HTQXkejYGEMrmuBnYGhbRcqSgRyanzO92ZnZYT-lnZ8LwBAmvEMdtBNX4HwAGaU6xW52HPx4buGg7I1j9CgNjCi0xrt9OuZa9LJddMs3ouGEa5YCXsdLhahtcuoQZhn_ZhSDrtRrzJ_SQStKmISRkwbZ3w3KkFLUIV2EzJRKfVec-p40yU-WlWqKopwYweh7wjub13zyMDebCDBpZ6mNB3kxvBNhJb_jd2ha30-XVMzsWbZsaytnPpjRrohg1OThnRfPBh8mnYLxo0HKID0uVO2adHwQNR56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام وزیر خارجۀ قزاقستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/446311" target="_blank">📅 16:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446310">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285c785f3b.mp4?token=HEN6GwRc7J8kLuD6gY0EK2s5HL_8BQrWN6JxdCbcWesXucIdlfYTC7IzvpygiNUu5O9yurbwbAdfDrLhBPWWk-wBtu8zLcq8IdvtrHCJaDv9Bd3sSo3MI_7-Il0GfOHxtFCleTRT7XrAmiHF3z7rM3oIWhq377CUjS9uYZWaDX1Q1-lNQ-8git0yFSuB1DrrkxZFTS6pKecIEXDazplljqMeTK9X2zcY0yJJf6BghAevAUB-GttIw8efLskXPaFEydRLUGEEtQvFAUSwXKHYAIQzE-vwA051PsXXH223dlKZjNubcffFSx8vkjiBPyjxjxqIGUd3sclk3mVDDuo0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285c785f3b.mp4?token=HEN6GwRc7J8kLuD6gY0EK2s5HL_8BQrWN6JxdCbcWesXucIdlfYTC7IzvpygiNUu5O9yurbwbAdfDrLhBPWWk-wBtu8zLcq8IdvtrHCJaDv9Bd3sSo3MI_7-Il0GfOHxtFCleTRT7XrAmiHF3z7rM3oIWhq377CUjS9uYZWaDX1Q1-lNQ-8git0yFSuB1DrrkxZFTS6pKecIEXDazplljqMeTK9X2zcY0yJJf6BghAevAUB-GttIw8efLskXPaFEydRLUGEEtQvFAUSwXKHYAIQzE-vwA051PsXXH223dlKZjNubcffFSx8vkjiBPyjxjxqIGUd3sclk3mVDDuo0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام قائم‌مقام وزارت خارجۀ عربستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/446310" target="_blank">📅 16:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446309">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e927a24458.mp4?token=NWs31exY-brcrgVl3s3A3aW0M7pZ4W3sRNj_qbAIMQh6ggGolHOf3cnEurA-LjBd7Toi-UkrntONlUWdJ2yfa9uNa3s8edpaB1cpImAeDCGejFpUCg-FPSMmaKfJ2XsSKnMI5-ZArAcObyqkVErpux0zAK74KaUUeDHUNTkJ4vREIbEYmKi9iVB7S6pa959szcwTSy8LdgT9xNmLHaodtT16DvrkZ6cRcgfFc9YbKaYgDAADxB43c1uypbBdxg6Ncgr9rBfhZ0IEufwHMNmz3vUrSdNxWu610VJR4ksN18SrAjFrGlPr5BOssxPBUQ_8SzyA6HOwohaaG8Fb4wxSgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e927a24458.mp4?token=NWs31exY-brcrgVl3s3A3aW0M7pZ4W3sRNj_qbAIMQh6ggGolHOf3cnEurA-LjBd7Toi-UkrntONlUWdJ2yfa9uNa3s8edpaB1cpImAeDCGejFpUCg-FPSMmaKfJ2XsSKnMI5-ZArAcObyqkVErpux0zAK74KaUUeDHUNTkJ4vREIbEYmKi9iVB7S6pa959szcwTSy8LdgT9xNmLHaodtT16DvrkZ6cRcgfFc9YbKaYgDAADxB43c1uypbBdxg6Ncgr9rBfhZ0IEufwHMNmz3vUrSdNxWu610VJR4ksN18SrAjFrGlPr5BOssxPBUQ_8SzyA6HOwohaaG8Fb4wxSgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نایب‌رئیس مجلس سریلانکا به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/446309" target="_blank">📅 16:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446304">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptE0pdovNZ8RgCjJ8Q9q_HNnN7PrI9wgGdXI6Y9_h8VKjsVTrSB7ksWeQD7yFmhqXAQcPrh3HyS3qN-bvcRU6ScCf3mNAR1FEDTwPU7odmq21hO4yR3rFF0Kg5wToj_hOjhCcc_fuDnWL3OLqvmg6jRF6Qg1a6ENE3uFNksKQxwpcyqUfaltulzWkesn5N2nPFNtitkZsoNH62RQLnLLydSB2_IeSsduZS-1O3W11EYdD9WH5gZchTOZrudHFygutRHr-Z5lGJEB-YLglMBGNqwEJ7aoMhLLOEcjsAb4UQjyDAvyTU9L3nwKGcb_UzS3GlcB8fU0-VUjGi6Glpy2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgpKKr5lJlBc-WceSDgcz_E_YSRaiLPZOamCy8kFiU9h5AuBOAvBZOpTtggc4qAhS7Irf3sJDe8mDtqbOAj86TEN4w6EyHCztQsmDj3VNao5P0oTvRjDlED9hdj--axuEp1jW3c7Gu4WeIqhtoKpX2_w9gn3hhPPxxXK60R-xXZ0S3VsRujiG8FVY-P-2jnfi0jw8iWSkHQY59yLl81lVHCEQ0OSt_yNL9z8WYv3md9KEosfVNX7Oz718gQ2f-hl_u19WyX5qbQggrBHyPd4BZjTWw2L-KdGPfJvd_pO9K8f7eTC4QGHFyBk8YanTfCDJj5QwUhADf0Ljb7Z0vkJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ay0CaV2pl5PsUJ_qWl0me3kqYW7c7TpyNkYq6LhuhhjNadoAaau1z9xXcRcMioZbopHrY32y3KWIvfyw5y0F1wRYGKQdzOFOqUPkWBVcvl_SbLTaNdvKDA1s12w9NPVGmCkwhCUtgsr94HyrK-d4dSIYN3ap6KdG-AytrapR08rGTQLPWXmN5MImCGrmw6b6Eqnjn1lfQT_fl9yMvRde1EPgOgwmhQ5Utp6VqhocKMmLC2XXtw4kMJsGp5SrRlrd7wVaPX8tPFwhF1ibUXWdhpTku_r_5CHQdF4d2ZlRxchjWoxtS27GTmyn62mSAUoPw_lXDxkTasVipkknbkEobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knvD9v4FAs3FdZ1DYmpk6fbk1RMHJ8sFfsEGki0_2kcOovhhGBk44AKIZZELru1WS5u6vyk6cfAEYCPa_EGuZShqxKpGiFFyF8TWcL-Eey2NFeYKPyh2c2qhDkrt0u5Ds7BhQyrEBfUnYdB8DG2u6m76JHcbp8Qn6uTgHsh53Kos5EAywx7vMHk-KxPcIgfABW1xHs6-Z7iJFWb0Qr2a6WMPZP6mvXSenxVqlnMq-9vvclPg013Jk5OoWjfxN4eMeLdpxlf1xBak4cdAl8T1di8qbf-290AtFRVGr5T0A_YrVKtE7YBE7tEReD55Sjl4LaIbQKz6g1JpZrG0yRWsmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKZy65gCpZFCuJlzbo-_QqqdPT7Fjhwb9YsqHdhGarQlGjpB3whyei3Rb6AYscinq9YMCOvfu1gOZgeX6SttyFMmH0UU0kekZhE9p-PkDZ055LHJ1iohs8M8Llp1VNGotLi1Seyag4Zbplca8iDe5u7eCxYub2aG2k-T-b2tyTsTV2DZoeLWjTwUTp9_7J3IVq95a3bTbItmlmmqEEDOZeNOCmVR29ktAZVgJflIQ6i825Vpau3axpSX_lq2jKT-uzpgUEkrHc5P711kjzloM3TQCkAryFFFX0VphZk3z8HlMFTgboSQphnBrfyrkIYnU6V_Fdp73qOIS8ZmBK-HrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ادای احترام مقامات و شخصیت‌های کشورهای خارجی به پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/446304" target="_blank">📅 16:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446303">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807a058ab8.mp4?token=tQZkswKnjBeewR7e_yujXuiGTDBJdrSNTd-Lm5yYcPFodaQSEgsz-aHyPsDHMNBdQXEcWWB2rAWSYf89WS-aNPQq_geGncqQAMBB00WEXVcuWLJJOvCg1zvP23hzZEJqQIrzZwVxKaI1clHvVqx0I8dkJx1LgxmmRHNxF4oaiBR4jsZyIUBuVPLiEcpGVE2EjH2sGOoqrblcJX48hZb4mpveDR17ueQOEkOINgS0HCNkPDozNVTBFssYX9rYe6FAcANaVuLiRkpv4RulWxlnXfyX0x8MmrEoKyJsdTt_Vsm8S_rR_fmO30palMouMRnBI3xNLeuc7mZDMisOVlTJeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807a058ab8.mp4?token=tQZkswKnjBeewR7e_yujXuiGTDBJdrSNTd-Lm5yYcPFodaQSEgsz-aHyPsDHMNBdQXEcWWB2rAWSYf89WS-aNPQq_geGncqQAMBB00WEXVcuWLJJOvCg1zvP23hzZEJqQIrzZwVxKaI1clHvVqx0I8dkJx1LgxmmRHNxF4oaiBR4jsZyIUBuVPLiEcpGVE2EjH2sGOoqrblcJX48hZb4mpveDR17ueQOEkOINgS0HCNkPDozNVTBFssYX9rYe6FAcANaVuLiRkpv4RulWxlnXfyX0x8MmrEoKyJsdTt_Vsm8S_rR_fmO30palMouMRnBI3xNLeuc7mZDMisOVlTJeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس قطر به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/446303" target="_blank">📅 16:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446302">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097c4fe92b.mp4?token=jNMQnlRwkwZVFPuMQwdiGu4I6XZvtPKYF-gjCXh9vU-mVNFrhjhTEWR0YoOCA_HRwTdS1rWtwOP0Ar3hvlo5l4nKObHGFH-i5CCRBQhEPxjFgaWO1qfQGgfGJqGKsUFLmmJOU7-hbi3wFK9JYOVCcSa5q5x16p2cWH1Wz0Jk8CHQdH7rKA_P9s10-Y1CaZpiWVoBzbWHZkFn6G7pHHHR0UBdqQh8nfWKJxTQddoKK_YvlU34Y6nBQazu2tln_5Q2MkoABbdQDrrTGXwyE7SyAdj5a9hCOGEi3dAR8p9XbAcDGq0aUxnI7dL-_ICntO61MVDM2Og3NVvl3GqBjXDWKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097c4fe92b.mp4?token=jNMQnlRwkwZVFPuMQwdiGu4I6XZvtPKYF-gjCXh9vU-mVNFrhjhTEWR0YoOCA_HRwTdS1rWtwOP0Ar3hvlo5l4nKObHGFH-i5CCRBQhEPxjFgaWO1qfQGgfGJqGKsUFLmmJOU7-hbi3wFK9JYOVCcSa5q5x16p2cWH1Wz0Jk8CHQdH7rKA_P9s10-Y1CaZpiWVoBzbWHZkFn6G7pHHHR0UBdqQh8nfWKJxTQddoKK_YvlU34Y6nBQazu2tln_5Q2MkoABbdQDrrTGXwyE7SyAdj5a9hCOGEi3dAR8p9XbAcDGq0aUxnI7dL-_ICntO61MVDM2Og3NVvl3GqBjXDWKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام معاون رئیس‌جمهور ترکیه به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/446302" target="_blank">📅 16:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446301">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b577b84a5f.mp4?token=ABOuc-Z3_-wK1FMIOTjNGPct0RcaXBBgSQ4ZScihmJUUz6L24QWFEIMYTgzqkqVy5lw2Rg8aqbfWC4tjFB1xgRFSOc5RU7Y9UKlbSld370Ay6fZ2cLr2qpAoXeqgexSnJSb92lk7Nzy7wox2MwHH2elMS0xw6vOtSPN1SUNvMkEGZqAvtEWxgKR3FA3fg_ucE7Abfxo9cEP7eMzS-EtwnjdLp5kbvMdL2n-hW-UvQrW_Hrg5RTOc6yLMOty4jQsbF8mIxV1xdxjvI6INr_odmjWRPz2XMCGI6d54hdAMXBn9HBOFam1Rn5hdcIzcHS104dhwu59GpMBsGPdSwSYL0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b577b84a5f.mp4?token=ABOuc-Z3_-wK1FMIOTjNGPct0RcaXBBgSQ4ZScihmJUUz6L24QWFEIMYTgzqkqVy5lw2Rg8aqbfWC4tjFB1xgRFSOc5RU7Y9UKlbSld370Ay6fZ2cLr2qpAoXeqgexSnJSb92lk7Nzy7wox2MwHH2elMS0xw6vOtSPN1SUNvMkEGZqAvtEWxgKR3FA3fg_ucE7Abfxo9cEP7eMzS-EtwnjdLp5kbvMdL2n-hW-UvQrW_Hrg5RTOc6yLMOty4jQsbF8mIxV1xdxjvI6INr_odmjWRPz2XMCGI6d54hdAMXBn9HBOFam1Rn5hdcIzcHS104dhwu59GpMBsGPdSwSYL0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدودف وارد تهران شد
🔹
نایب رئیس شورای امنیت فدراسیون روسیه به عنوان فرستاده ویژهٔ پوتین، برای شرکت در مراسم وداع رهبر شهید انقلاب وارد ایران شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/446301" target="_blank">📅 16:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446300">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9cddcc3e.mp4?token=emqExFJpxD8zxK9aIo0iawTCnhdNaXz5vvUK6MDN5LJvFBEUJweEadVOc2-6tCYZ9ETN3TG7_GpQjA7UisAQI-VOQOJMyE9U3iL_icJomUkHKLQUh1iTy5TS8FR_ARLBItYe0vYNnwXMtonqY3QrZB2rlRis71hy_6hbgpE1L7uJJyuCmw6znRct6-rTmNIlWbpH5WRMOlFrdwfb1NW8RaEmKbkkuLQ4He9eeNfuY8nPdro2v4c7q_b4HSn_pXWHWzZ3b8Xf7IzCLrdlyyGFSaMiO1ie5s33PtbugsEgaU59OKp5k0F7ip4TO6ghlBzxcIuu9GxUWChRtFDM_5-B8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9cddcc3e.mp4?token=emqExFJpxD8zxK9aIo0iawTCnhdNaXz5vvUK6MDN5LJvFBEUJweEadVOc2-6tCYZ9ETN3TG7_GpQjA7UisAQI-VOQOJMyE9U3iL_icJomUkHKLQUh1iTy5TS8FR_ARLBItYe0vYNnwXMtonqY3QrZB2rlRis71hy_6hbgpE1L7uJJyuCmw6znRct6-rTmNIlWbpH5WRMOlFrdwfb1NW8RaEmKbkkuLQ4He9eeNfuY8nPdro2v4c7q_b4HSn_pXWHWzZ3b8Xf7IzCLrdlyyGFSaMiO1ie5s33PtbugsEgaU59OKp5k0F7ip4TO6ghlBzxcIuu9GxUWChRtFDM_5-B8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام وزیر کابینۀ نامبیا به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/446300" target="_blank">📅 16:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446299">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a0eebaab3.mp4?token=XxgNqdDKqXBifiKkH-adBVFbnNF6LDY5PYuuHlIPpYZO0wTsYFhMJOYuGtVaRK5hXJvsSDGsgOt6WZlhD-UWHihSEEYn_S8akTYfD70ElrorAlr2WXLsR2lCTPQfM78rCUoNwOBzmShlito2rfay-ahhmUjfkw4FY8qNAvsNSzAzi9jfPCQp1Z6a3T54d2_Q_P5vDLpz2mUI5w1F8Dazn__a8SXc9hKZ3vEhdg06-NqpePuj-mhCfRZxGBc2XCgpGYvQQOpdujCRGchMxGj0gAqHuvkvP6T0l8xbnxoORVZjQTOza9lfEnvmPnjdC4hTaiblyb2DGnV1DFxj0pHV7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a0eebaab3.mp4?token=XxgNqdDKqXBifiKkH-adBVFbnNF6LDY5PYuuHlIPpYZO0wTsYFhMJOYuGtVaRK5hXJvsSDGsgOt6WZlhD-UWHihSEEYn_S8akTYfD70ElrorAlr2WXLsR2lCTPQfM78rCUoNwOBzmShlito2rfay-ahhmUjfkw4FY8qNAvsNSzAzi9jfPCQp1Z6a3T54d2_Q_P5vDLpz2mUI5w1F8Dazn__a8SXc9hKZ3vEhdg06-NqpePuj-mhCfRZxGBc2XCgpGYvQQOpdujCRGchMxGj0gAqHuvkvP6T0l8xbnxoORVZjQTOza9lfEnvmPnjdC4hTaiblyb2DGnV1DFxj0pHV7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام معاون رئیس شورای سیاسی حزب‌الله لبنان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/446299" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446296">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ev45wQP_8DD6RvS3e0_rvV8mPIaARAOknXA4WJKJytNHuUoxcJXz2OJ5WAqALoF1tON5TOPQHiKQc14NST1pKXqigmPoIv9lYzKVeIQNN-bBeseGxQS4BlDnaMqoIHEx1o8gt3xLyOiKz9ZV3rQydP0Col4OskGOCyAFfCqBbub-5tanaD54w5bgqqB6MKROpg8mS1k9i0UtbsX19B5alga7MKrE3MGtv7ZdUpMNOuOtO69vP2kThSSI6-75hc9FXUS2CIAg8CcDpv8d-TzWXn-CrSpPSrKs7BmRqZHnA_xzxEwtRvKPgxHIzRqjaA-HPBYRygNU4FHPUbP4Uv9soA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScaWVoM3K3GT_78yGCjjD-LQgn8C7LxM1FYQtIdFSRJgF7yUKm96znSBPox9nByf_eYgO1L0JE67ddgBFdgfqf9fJpfEVIt6UlT3DAwnFasqzXXr9EicGdoisw_qnwsPp_UkaLEWNMuCsNPyxmKoHia-vmlD0dliPjD91WNhO9njBBiodVPlJdShQJ_UFacxF8Ci8rXNFqr9NIaxf2y_qXVej9FvHBj_p-7m6SgVXNLzdbQkFf_H9kL7mVNGFqnVXiPxykSezdGDn0yFuVQxOgzj83igdFCYaudI5OqPn9ZSM4chX4LvdAlnns3kwuTj8hUYk6HKnHEQMlH0EEJQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1tuw8u3wNGugKOkmATotumWaLmfYCZQneaqVnE6o7xDesu5EuPbWsGYpnuRXiwqiQXAS0j8aYvqKBjQiS1Mw8ftePPEjyxA2HCA20A9bGE1q-x1yidTuUkNjzs3aTJWRxtHPfm_eqYoiDHF9qNQNrA3wPXmCXi-RHe-4M57AvN2e5u0mtizYOP0nG9gm302921-gwBq6guEemB32-0RW-XgDCfqX2ce3fRHa4RvtiLKehzzN_TtTKRmZNPK8l9wdcMmzX_LD0-3KrSJBh6jK-5crurSgCVKH6gTmzj1TJh31X7IH7iqKaVQHSclIDrnDw6asTfU91HFoQBJMCxifg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار معاون رئیس‌جمهور ترکیه با پزشکیان
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/446296" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446295">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e102375304.mp4?token=XDkpQ1L_xrAB0g6pl1okYy1tPjzE_ENuP0iGJJqgZhTR2s_JM02XcU9WxcL_lylfOZ6TKe19UvJ5y9FiO355DFArwIFpt0FS8Gwxmgd_qgKfmK2wMM9wzwq5qIHzrRXASx4Mv6t8mRatty3EyXyko_VYx7_GyauTscQPaq-VJ_1IDiMzmNwYO4adMYatO3XXtABlPIr3pLbxyXaoKfh5aWDvuOTK6qyjW-sgYgoRT_i-td04PioalgvHW9QKRS3f4Tfn8jT9EHgfHVuqvNICVtqxwGA--DSbqtgZO3EDpzux4SfprG8zpeN7C0vScmTkSL_qOb6GAxhL7abe_Q62uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e102375304.mp4?token=XDkpQ1L_xrAB0g6pl1okYy1tPjzE_ENuP0iGJJqgZhTR2s_JM02XcU9WxcL_lylfOZ6TKe19UvJ5y9FiO355DFArwIFpt0FS8Gwxmgd_qgKfmK2wMM9wzwq5qIHzrRXASx4Mv6t8mRatty3EyXyko_VYx7_GyauTscQPaq-VJ_1IDiMzmNwYO4adMYatO3XXtABlPIr3pLbxyXaoKfh5aWDvuOTK6qyjW-sgYgoRT_i-td04PioalgvHW9QKRS3f4Tfn8jT9EHgfHVuqvNICVtqxwGA--DSbqtgZO3EDpzux4SfprG8zpeN7C0vScmTkSL_qOb6GAxhL7abe_Q62uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام اعضای ارشد جنبش حماس به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/446295" target="_blank">📅 16:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446294">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf12cc6661.mp4?token=vp8TIgaJzbqZ5xm66iq96qtlunCXmhkpsVBRtLWUWx6LP7SfVkUh-R3WI0wIE3T6xvSIByQ5bZVHzui_XKTl4c6_d7MdOZP2Vu_BfOTgakxv5F_lPS9gJ8bU4Lh6F_gHuRQJ8WFSlq8Cy_-SbprIvWcbFwtpsSsnTd2L0Gih9nV5E60xYXej2JM3JGgr77PFTNi48azhzOHHLWKt229iSi4gMVqJjOMM5_WDDV5JbNk88aq1Pl4_W4aY4hrycVmoBvPAP0_Sy4uqXAlw8aL8PgjSB6igJstDW_uSK7Aj2NiSKFhAqOcc7vuxM0DEpGFK7szrgl_wqDd9YKUezZ9LAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf12cc6661.mp4?token=vp8TIgaJzbqZ5xm66iq96qtlunCXmhkpsVBRtLWUWx6LP7SfVkUh-R3WI0wIE3T6xvSIByQ5bZVHzui_XKTl4c6_d7MdOZP2Vu_BfOTgakxv5F_lPS9gJ8bU4Lh6F_gHuRQJ8WFSlq8Cy_-SbprIvWcbFwtpsSsnTd2L0Gih9nV5E60xYXej2JM3JGgr77PFTNi48azhzOHHLWKt229iSi4gMVqJjOMM5_WDDV5JbNk88aq1Pl4_W4aY4hrycVmoBvPAP0_Sy4uqXAlw8aL8PgjSB6igJstDW_uSK7Aj2NiSKFhAqOcc7vuxM0DEpGFK7szrgl_wqDd9YKUezZ9LAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عالم اهل سنت هرمزگان: تشییع رهبر شهید، نمایش اقتدار ایران اسلامی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/446294" target="_blank">📅 16:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446293">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1034b5518a.mp4?token=QGlxidn1Yss3nVaKy6-Jh0n8-MHceSWohXZDSIlhjYdmFddJ2rOu9Vh07EjgKd_MN0sQjEnZX857x6qoeE4NTu0QoDA7vn0l262U1Vgmyr4RJJCrR_mEsImvaaQ2zkrc7t2oMVcyg10B_pIa3yZnHDXyj3DTI_dCXtwMBVN54jAzVEWyb9TWskhtJuC5-2JPya6v8UuPwbbT7cx0QuMmeA1eT0VxcMyq-AKr2-fkKn-VQkZET8bMX5daRkRHyP70xdrZD9b2ao9nSQAF6gB4lNpZTuGUcD6rNOwSv-SAhZDVkpFmF8WivXhLXqEJmR0PbTrg-3CoD3SIpccn-8jE4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1034b5518a.mp4?token=QGlxidn1Yss3nVaKy6-Jh0n8-MHceSWohXZDSIlhjYdmFddJ2rOu9Vh07EjgKd_MN0sQjEnZX857x6qoeE4NTu0QoDA7vn0l262U1Vgmyr4RJJCrR_mEsImvaaQ2zkrc7t2oMVcyg10B_pIa3yZnHDXyj3DTI_dCXtwMBVN54jAzVEWyb9TWskhtJuC5-2JPya6v8UuPwbbT7cx0QuMmeA1eT0VxcMyq-AKr2-fkKn-VQkZET8bMX5daRkRHyP70xdrZD9b2ao9nSQAF6gB4lNpZTuGUcD6rNOwSv-SAhZDVkpFmF8WivXhLXqEJmR0PbTrg-3CoD3SIpccn-8jE4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام دبیرکل جنبش جهاد اسلامی فلسطین به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/446293" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446292">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28c14a665.mp4?token=d1yGsJQ1xRYMt-lnCdFLeAPWQ0vsqO8xFj7tlPsAJM3OueKstWvWocS6dclwF0laNbvA1CrCdvHaztYYHGUyvIK8Hf8qO4sPt8bjOwaDfZnIm0FuwoHgCIuTjBajhw6l0QFkbeJbM1n4PVrrHvL_IuYwNx4padxt3JlVOsh4_ERxRHHImrN7O2a28LKyo8RnQYIitBhUX4ismKbJF6vxse7SLWKFIgAQvGnuthegb1ni-CweQsQioEi-K8MQ_U5BLH7ArD2AqbyimMDpAWtSpR5mQFV9BT22u7o42NSJbGG-sAs145kQmocfVqTGfjT-epc42ZntrmoJg-Jb8wQ1Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28c14a665.mp4?token=d1yGsJQ1xRYMt-lnCdFLeAPWQ0vsqO8xFj7tlPsAJM3OueKstWvWocS6dclwF0laNbvA1CrCdvHaztYYHGUyvIK8Hf8qO4sPt8bjOwaDfZnIm0FuwoHgCIuTjBajhw6l0QFkbeJbM1n4PVrrHvL_IuYwNx4padxt3JlVOsh4_ERxRHHImrN7O2a28LKyo8RnQYIitBhUX4ismKbJF6vxse7SLWKFIgAQvGnuthegb1ni-CweQsQioEi-K8MQ_U5BLH7ArD2AqbyimMDpAWtSpR5mQFV9BT22u7o42NSJbGG-sAs145kQmocfVqTGfjT-epc42ZntrmoJg-Jb8wQ1Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمد مسعود: فکر می‌کنم زیباتر از این توصیف برای رهبر شهید پیدا نمی‌کنم؛ این‌که بهشتی زندگی کردند و بهشتی شدند
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/446292" target="_blank">📅 16:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446291">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c47bdcde23.mp4?token=otsF23LQrXwzzhBLVOVtXvrq37JHj1t_gdR45lup3_28YZSPF4lXsgI9N7ruOuxhCX8H9KzOGAXa9IGjDMcACrxDScDdyCQAC0QlI4dX8B111SRvz2htaoADLRUq2qQ3ddRaixNWRW2IIq9TS44MEg91A05xvc5PnHL6gY8xHvvp57laE9GqldRsshJocIFjsSQ5HMTSbRzdoJXZiCJ2Ol6pmUh1lB0KU2hVKrMX45vESY2vCCdGhl0ybFDqVyKmwxA1D1kTIjBdTG7Rxc1Zm2HfqANAJw6jlgrEN9QUEssbIiyuXKLaIPNN9JMMs1pLNgsUq3N5TEEut5jlcwF57Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c47bdcde23.mp4?token=otsF23LQrXwzzhBLVOVtXvrq37JHj1t_gdR45lup3_28YZSPF4lXsgI9N7ruOuxhCX8H9KzOGAXa9IGjDMcACrxDScDdyCQAC0QlI4dX8B111SRvz2htaoADLRUq2qQ3ddRaixNWRW2IIq9TS44MEg91A05xvc5PnHL6gY8xHvvp57laE9GqldRsshJocIFjsSQ5HMTSbRzdoJXZiCJ2Ol6pmUh1lB0KU2hVKrMX45vESY2vCCdGhl0ybFDqVyKmwxA1D1kTIjBdTG7Rxc1Zm2HfqANAJw6jlgrEN9QUEssbIiyuXKLaIPNN9JMMs1pLNgsUq3N5TEEut5jlcwF57Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس عمان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/446291" target="_blank">📅 16:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446290">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2117939ff8.mp4?token=oFB5TQvyDMJqi0T2clUiX3Ij-T_gDFk7CJPDJ5Y5k06XHs-Z4_GZnJ1tiYYFUExQ-fYFTp9JcEQaRcIU5M8nEtaIz9XX534s3_4yG-Zi804VlHtW1uhDCPh56Q_eGBujXYZ4WlCtrnqXsy4BNGftafzdLh_gFWC2waAbwxiuEuBsLbt4Ac0ju7B6BOXgbPGRTYVMJRXjyZq9esLqj7vW7fBsWl4DXtL9rs02rrOfgPYZcYJc3nTExsz8EZsQAyxlQAJWNpu61fNin3lCyTodQL7doqmenxE_k3wlYoB9nXxwedxrm7c1Bs9gwzjqk3iagbP0Qawq-68J02jj4q8bfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2117939ff8.mp4?token=oFB5TQvyDMJqi0T2clUiX3Ij-T_gDFk7CJPDJ5Y5k06XHs-Z4_GZnJ1tiYYFUExQ-fYFTp9JcEQaRcIU5M8nEtaIz9XX534s3_4yG-Zi804VlHtW1uhDCPh56Q_eGBujXYZ4WlCtrnqXsy4BNGftafzdLh_gFWC2waAbwxiuEuBsLbt4Ac0ju7B6BOXgbPGRTYVMJRXjyZq9esLqj7vW7fBsWl4DXtL9rs02rrOfgPYZcYJc3nTExsz8EZsQAyxlQAJWNpu61fNin3lCyTodQL7doqmenxE_k3wlYoB9nXxwedxrm7c1Bs9gwzjqk3iagbP0Qawq-68J02jj4q8bfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محل سقوط پرواز ۶۵۵ ایران‌ایر در خلیج فارس گل‌باران شد
🔸
۱۲ تیر ۱۳۶۷ هواپیمای مسافربری پرواز ۶۵۵ ایران‌ایر بر آسمان خلیج فارس هدف ۲ موشک شلیک‌شده از ناو آمریکایی وینسنس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/446290" target="_blank">📅 16:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446289">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd3019015.mp4?token=AEv6tyf0egtnO-hQhEJX5eH8piCWhFDhkc7_s-Aob-kHLQ51V6NOurZKRCFXvrvWJBbURUgh4dcF-BZvD7TLHwmqgk7y773Ie0SyNB0lecggteYXaSV4GLmdwrlUiTswCXMZ3hESWRakZehIgKdfdDlSCprwaU3KpUervhHXqQlYr7XKicxV0RqjE98NvQqsbCxV8ON8x7E9MxYYhm0dgzsTyWxO250gXhdiX2vhiERTdOHYMZQYnF3nu9KKvPWUQoFbrpNGcicoQx5ZZ8OxMWNrHXzA5voEBBv1WNrLNO1J6zrqQajtutxTVQazxLKNPuBJYL7OIgErdXsJaa253g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd3019015.mp4?token=AEv6tyf0egtnO-hQhEJX5eH8piCWhFDhkc7_s-Aob-kHLQ51V6NOurZKRCFXvrvWJBbURUgh4dcF-BZvD7TLHwmqgk7y773Ie0SyNB0lecggteYXaSV4GLmdwrlUiTswCXMZ3hESWRakZehIgKdfdDlSCprwaU3KpUervhHXqQlYr7XKicxV0RqjE98NvQqsbCxV8ON8x7E9MxYYhm0dgzsTyWxO250gXhdiX2vhiERTdOHYMZQYnF3nu9KKvPWUQoFbrpNGcicoQx5ZZ8OxMWNrHXzA5voEBBv1WNrLNO1J6zrqQajtutxTVQazxLKNPuBJYL7OIgErdXsJaa253g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام وزیر خارجۀ کنگو به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/446289" target="_blank">📅 16:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446288">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb5118438.mp4?token=p6LLa7drN41VtaqyuEp6jaxEuy5gpDFtVjSgU4HASLemii4B-XkjJvNgm8qCN59k3_Fc3wLJBX4BZnRD0zL6jvrPZUWwA5Xp-XchTVNC1tLWhZOBT4wCh2T4TiIZxnh0hfTqlDaOqYpvfjVNG8Zvx-ddpUvdqSwCatU2gQ3JSRYWRUWzQ_Jm-FjDg5bPMXv59USlAoVK3kNrvkOIO4Jy0LoHHQfwzFQJrcXKdbKWXQAo-aZo5HlgDw9l4kYUlWa4cdX7Io6tO5znkl1RN4fHmIfdjfojd52RfnfnSrWnHblsprzy4MFkyVrZGaWtZjQW0XdPMB96zZurFh_0ZyCFCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb5118438.mp4?token=p6LLa7drN41VtaqyuEp6jaxEuy5gpDFtVjSgU4HASLemii4B-XkjJvNgm8qCN59k3_Fc3wLJBX4BZnRD0zL6jvrPZUWwA5Xp-XchTVNC1tLWhZOBT4wCh2T4TiIZxnh0hfTqlDaOqYpvfjVNG8Zvx-ddpUvdqSwCatU2gQ3JSRYWRUWzQ_Jm-FjDg5bPMXv59USlAoVK3kNrvkOIO4Jy0LoHHQfwzFQJrcXKdbKWXQAo-aZo5HlgDw9l4kYUlWa4cdX7Io6tO5znkl1RN4fHmIfdjfojd52RfnfnSrWnHblsprzy4MFkyVrZGaWtZjQW0XdPMB96zZurFh_0ZyCFCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس‌جمهور گرجستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/446288" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446287">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a56aefedd.mp4?token=YzQd4DxEzp802H0PDJeBfgY9Zvl3ko8t_nnhijukci0zvc36m2PkdN_q1QHBTIQ4VgNRDdu4_F0_3kLVLPv4LUNPfqckweI_xYwUjoLFrSac4pawiTnWCT23n4vXTGI-_2Ce7fwl89WiV2YC2T_tkTwa-MEJZ93O_zFvI0jvfucQamahH9nG2skaHqsE9EJxCysIwW3JDF5kKRWelsMjUDEKua6fAuBvwZF9Ly1fzdjC98dwyJnYhn2v_bVC5XhybbxvJKujuMNEwq1DPkQE5zH_otoSuVzli6vIfdAOL6oaTa8XuN6g3Q5ruyY5CWM5nyTSeFg1M6UCXkLmXaTLAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a56aefedd.mp4?token=YzQd4DxEzp802H0PDJeBfgY9Zvl3ko8t_nnhijukci0zvc36m2PkdN_q1QHBTIQ4VgNRDdu4_F0_3kLVLPv4LUNPfqckweI_xYwUjoLFrSac4pawiTnWCT23n4vXTGI-_2Ce7fwl89WiV2YC2T_tkTwa-MEJZ93O_zFvI0jvfucQamahH9nG2skaHqsE9EJxCysIwW3JDF5kKRWelsMjUDEKua6fAuBvwZF9Ly1fzdjC98dwyJnYhn2v_bVC5XhybbxvJKujuMNEwq1DPkQE5zH_otoSuVzli6vIfdAOL6oaTa8XuN6g3Q5ruyY5CWM5nyTSeFg1M6UCXkLmXaTLAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام وزیر خارجۀ بورکینافاسو به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/446287" target="_blank">📅 15:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446286">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooQdQ16Az-2SaEEvZuswsguaoVWHLXiTXkszlPz2dtJHaoJWaBzW0KWlK8JBwpbAkPdrKib524JN4JxfHPm2D_t5fSFOdNk9SFQdxjT_HmW1afIiiHsELeAhadewi4UzVc9nP2Cwi1ehr7MKQf1IHlskKEjQUfCYJs1ca8WrdqPu_-fv1-mPYmR3TzYdpnf_FOxyxH5XVKmd3eLJatipi7FtNC6PRUeomaIQRK69HJuDnxjBsQ9fyLFSaUXA-s6SCmC_CMyAWKBcLx7qs0Fb-fhtkodz2knDrg2m2fGj-GR0U9SbGNp09fGSKNA2s1gsFQEdUd8bqXoPrIYUIkl8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب جمعهٔ تهران: خونخواهی رهبر شهید خواست همگان است
🔹
آیت‌الله‌خاتمی: جهان اسلام بزرگش را از دست داد و بزرگش را کشتند و این موضوع مسئله کوچکی نیست؛ امام مظلوم ما را با زبان روزه کشتند و طفل ۱۴ ماهه و خانوادهٔ ایشان را کشتند.
🔹
خون مظلوم از بُنِ صخره جوانه می زند؛ خونخواهی مقام معظم رهبری خواست همگان است.
🔹
مردم با حضور در آیین وداع و بدرقهٔ رهبر شهید انقلاب به تکریم از بزرگی می پردازند که آخرین لحظات عمرش با مشت گره کرده به دیدار خدا رفت.
🔹
این پیام استقامت است و پیام حضور ملت در این آیین در حقیقت پیام مقاومت و ایستادگی است و ملت ایران آمریکا و اسرائیل را بیچاره خواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/446286" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446285">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e3a8df95.mp4?token=FmNzMTHK6vhDPW5KMOdBIpiEvRRxRTqxAFpIOsCMPJLdUhZ_ks7dcoyqoOSrPucktWVSPF4q8H5OK9wAG9qbm8gukQscNSLK6eXzQkw_WBQkfIVmJdoAeP6tSQfcdvWf0u988EPQPc3CbYhEp0bHiizK0du6wKkt09EGUJJ4djNFKwNCsGnnlkt6R66kaAAyzjdoJ9hvTMXlHbhwEuAbgFwwGWBJgsnvGOpyTa4C4hc0Dg8WawjNwbyQTz9TYE0dhwTDPzQZzM1wKL9s2AziKxlTqFEP9G8zIVZpfKtliWFns6YhgTZq15qAiNzvr3jRHxxlvbKVeuGedLua5_wkZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e3a8df95.mp4?token=FmNzMTHK6vhDPW5KMOdBIpiEvRRxRTqxAFpIOsCMPJLdUhZ_ks7dcoyqoOSrPucktWVSPF4q8H5OK9wAG9qbm8gukQscNSLK6eXzQkw_WBQkfIVmJdoAeP6tSQfcdvWf0u988EPQPc3CbYhEp0bHiizK0du6wKkt09EGUJJ4djNFKwNCsGnnlkt6R66kaAAyzjdoJ9hvTMXlHbhwEuAbgFwwGWBJgsnvGOpyTa4C4hc0Dg8WawjNwbyQTz9TYE0dhwTDPzQZzM1wKL9s2AziKxlTqFEP9G8zIVZpfKtliWFns6YhgTZq15qAiNzvr3jRHxxlvbKVeuGedLua5_wkZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس اتحادیه میهنی کردستان عراق به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/446285" target="_blank">📅 15:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446284">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34e716852.mp4?token=n9sYjQimx87xSWYC_hSGXrz3HhisqZfYn7lUGL9PeYDAxcuAKcDs2qX99n_1Dwjo_bFzQmoXfwfivv4HcdKiGjEPckbDySGwSImHpbs8Mbqp4nulF06PbTHo-c64aKylNTgUEoF6nze6giKrKC1RqaG4u5IY-S4WFc2_aSmQb90pSOluaLgTCZ24l5IwXYegfjStWZu694NmxAAyPU1Gy4XcdFaUwhedE3GKXhgi0Are5ofnAKuocVgSdhgsWGFTEIedU9bj8FQwkIKyT5yaYOng0IdToOtVC4AVIlFEvLpYTwo0pWfvseAuxlCYbscEIyLc01iALWdooJIJTwlNKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34e716852.mp4?token=n9sYjQimx87xSWYC_hSGXrz3HhisqZfYn7lUGL9PeYDAxcuAKcDs2qX99n_1Dwjo_bFzQmoXfwfivv4HcdKiGjEPckbDySGwSImHpbs8Mbqp4nulF06PbTHo-c64aKylNTgUEoF6nze6giKrKC1RqaG4u5IY-S4WFc2_aSmQb90pSOluaLgTCZ24l5IwXYegfjStWZu694NmxAAyPU1Gy4XcdFaUwhedE3GKXhgi0Are5ofnAKuocVgSdhgsWGFTEIedU9bj8FQwkIKyT5yaYOng0IdToOtVC4AVIlFEvLpYTwo0pWfvseAuxlCYbscEIyLc01iALWdooJIJTwlNKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس مصر به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/446284" target="_blank">📅 15:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446283">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53048897d6.mp4?token=tAY_VsZ3x2-Y5v_H1lqFyPqSn6h0OE2HHqnB4vSca0Q_y7f4S5eqbx25TalFkBkyX7hmDgUREqsguPQfcBar5ZKDAwmxB_YFVNjHW4c1BB2AngmhkROkvO7Lixi0Xj5sdqHzilVWwPTfRH2b3xx2OkP6zTs8mZPTTBvD0RPqMgFjR8EV8eG3RIQHrE_28KSltDC0fZRc0WAj_C6mhXEaSjqfy0sfwcD9NrwQSs0Yp9jMNwddnUjOoccgSKmQSKMuCQk7ek5wq8UG96c25rXbnUrCwYThrwmrFpkO0maoOnQicSU-9AORb-G3C2OLjVHbnlc2uJusMeotMxyXOlmFEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53048897d6.mp4?token=tAY_VsZ3x2-Y5v_H1lqFyPqSn6h0OE2HHqnB4vSca0Q_y7f4S5eqbx25TalFkBkyX7hmDgUREqsguPQfcBar5ZKDAwmxB_YFVNjHW4c1BB2AngmhkROkvO7Lixi0Xj5sdqHzilVWwPTfRH2b3xx2OkP6zTs8mZPTTBvD0RPqMgFjR8EV8eG3RIQHrE_28KSltDC0fZRc0WAj_C6mhXEaSjqfy0sfwcD9NrwQSs0Yp9jMNwddnUjOoccgSKmQSKMuCQk7ek5wq8UG96c25rXbnUrCwYThrwmrFpkO0maoOnQicSU-9AORb-G3C2OLjVHbnlc2uJusMeotMxyXOlmFEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس‌جمهور عراق به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/446283" target="_blank">📅 15:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446282">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7755a7e7fa.mp4?token=cjeCe92lsqYcxOnidPixUPFnfZdCuAeYUE4neozy-JecmcgVb4qVFRcH8FIcfU44YXk1r8doRcO2noyXB44t1_FMN20FTCFdcZt_Wt4fHDxmVKXrJKv9KQyiyU9Ls4VmB2dUa_pBRP-gJGMqvwLRSW093XeD1i1yGRjzj4jCiJ93LeeIqPBqX7y1wTr6cY7-aWbuXmlwc_LQQMPUlhTXrbyDzTqN4wqINmuqYQu5pmtCz8iVMGmnUY9BU7SUxuRcd2xad2RYuWfqrpY9SCOxTaiNEt-C6G3rdQwFW2Nv8866rg0cHGiibhW59mDaHNqS3ja1VDHFsnwOj_n-392hnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7755a7e7fa.mp4?token=cjeCe92lsqYcxOnidPixUPFnfZdCuAeYUE4neozy-JecmcgVb4qVFRcH8FIcfU44YXk1r8doRcO2noyXB44t1_FMN20FTCFdcZt_Wt4fHDxmVKXrJKv9KQyiyU9Ls4VmB2dUa_pBRP-gJGMqvwLRSW093XeD1i1yGRjzj4jCiJ93LeeIqPBqX7y1wTr6cY7-aWbuXmlwc_LQQMPUlhTXrbyDzTqN4wqINmuqYQu5pmtCz8iVMGmnUY9BU7SUxuRcd2xad2RYuWfqrpY9SCOxTaiNEt-C6G3rdQwFW2Nv8866rg0cHGiibhW59mDaHNqS3ja1VDHFsnwOj_n-392hnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مجلس بنگلادش به رهبر شهید انقلاب ادای احترام کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/446282" target="_blank">📅 15:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446281">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4a52e5368.mp4?token=PJm6rYOVeo9tneVcKmE4EBcX6PbfhZkPV7q_KI11-pPMN2Y4VtqlrVnLTw4LGDdVYDpZITm_tGTMmaS6UyyBkMpgLaismUodyzcCTxj5bUqUj0Ee7zBFpouZiPgKRKK2NWrK5ZXH8v3Acreq1bAj6XOccSAkHiBiPOr_RFLdgUvAaoU0cWTSMlB0VcFDpleOuyHF7nFnebSmnQfAM4lvoS-JXvT5zGVTE1UFHfcevg8G1w3d4jjcvthcRAq6RqtH2hqpkOsrp9HL6tMMWPy7tjqbM26ygDjf3xzImbS_V5qSEMiga8EfZlujfbXbmsApqAHd4SJZ8yFO1Gn99AX_cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4a52e5368.mp4?token=PJm6rYOVeo9tneVcKmE4EBcX6PbfhZkPV7q_KI11-pPMN2Y4VtqlrVnLTw4LGDdVYDpZITm_tGTMmaS6UyyBkMpgLaismUodyzcCTxj5bUqUj0Ee7zBFpouZiPgKRKK2NWrK5ZXH8v3Acreq1bAj6XOccSAkHiBiPOr_RFLdgUvAaoU0cWTSMlB0VcFDpleOuyHF7nFnebSmnQfAM4lvoS-JXvT5zGVTE1UFHfcevg8G1w3d4jjcvthcRAq6RqtH2hqpkOsrp9HL6tMMWPy7tjqbM26ygDjf3xzImbS_V5qSEMiga8EfZlujfbXbmsApqAHd4SJZ8yFO1Gn99AX_cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام معاون رئیس‌الوزرای افغانستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/446281" target="_blank">📅 15:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446280">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9729b334cb.mp4?token=kvCV_XuQHroz8y-sOMC4cV0lesMl-BgMF1BgdBadW9Jo9hRu17frfa23X8YQBFI5dPKl6tjn-c9xzYzfpqgBGB3GKu5_dZ01h_oko2KcMAefmhBPnOybU1XcivZArT7m4L-vp1Znc-oFZDGdVzg7Hg-_BxRaI5WVeICHEgorKRy_7tQJ1sVZEpK7dbJvfjvol5Y7NXvAnfkl3gmHRzUAZLS_6ERQHyBDxQWKm8ruPxnBDeYTT_KfcdHZT-c2V3kM63G7dU8ZiDpV2ycq3RMg41r7aL5yvK8abAMOkHPhrBXu26ukP5lzvfIDmzeSUMYZTjDix0sfQZ20arVffGd6mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9729b334cb.mp4?token=kvCV_XuQHroz8y-sOMC4cV0lesMl-BgMF1BgdBadW9Jo9hRu17frfa23X8YQBFI5dPKl6tjn-c9xzYzfpqgBGB3GKu5_dZ01h_oko2KcMAefmhBPnOybU1XcivZArT7m4L-vp1Znc-oFZDGdVzg7Hg-_BxRaI5WVeICHEgorKRy_7tQJ1sVZEpK7dbJvfjvol5Y7NXvAnfkl3gmHRzUAZLS_6ERQHyBDxQWKm8ruPxnBDeYTT_KfcdHZT-c2V3kM63G7dU8ZiDpV2ycq3RMg41r7aL5yvK8abAMOkHPhrBXu26ukP5lzvfIDmzeSUMYZTjDix0sfQZ20arVffGd6mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام وزیر خارجۀ نیکاراگوئه به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/446280" target="_blank">📅 15:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446279">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaef1c1112.mp4?token=uOCi7sjx7PYi9kWahkNQYlPg2jFhaiFbvhzjoNLEsr8_gh5uQXUdAh2-EmGfTpwusVXhaxtLqzzvkLa76eauhwmTK5rmooPCJGUhC08ID1nMuzdtt2fHnRwlILpel-uAsws58spJmGAhQZhKjjV4PvkM6kJgbFWRHNUdXefM5JwDNcTE5cG9_9Buxn64vpQEUnue4q1_qkAKPTOMsA-fdl-ME1Xy6gl3n_b7gGZLudOkjL2ir4PFpujaqO6gTqvqMc2odvraez18EG14G6vk4j0AuHanxVx_7f2IIK64VFFrXTbY4v5pr3pCBLWCwNVwkVl1WskP-kt5P8m-iowrSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaef1c1112.mp4?token=uOCi7sjx7PYi9kWahkNQYlPg2jFhaiFbvhzjoNLEsr8_gh5uQXUdAh2-EmGfTpwusVXhaxtLqzzvkLa76eauhwmTK5rmooPCJGUhC08ID1nMuzdtt2fHnRwlILpel-uAsws58spJmGAhQZhKjjV4PvkM6kJgbFWRHNUdXefM5JwDNcTE5cG9_9Buxn64vpQEUnue4q1_qkAKPTOMsA-fdl-ME1Xy6gl3n_b7gGZLudOkjL2ir4PFpujaqO6gTqvqMc2odvraez18EG14G6vk4j0AuHanxVx_7f2IIK64VFFrXTbY4v5pr3pCBLWCwNVwkVl1WskP-kt5P8m-iowrSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد تشییع و وداع با رهبر شهید انقلاب: درهای مصلای تهران فردا از ساعت ۶ صبح به روی مردم باز خواهد شد
🔹
در صورت فراهم‌شدن امکان بازگشایی درهای مصلی از امشب، اطلاع‌رسانی لازم در این مورد انجام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446279" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446278">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda9a50f81.mp4?token=t1zXnpQd8PoSc_UIEnTsIxm22djQmGHAPoQrNrTADll5PwAs48z4blMHTeF-sdQ11_7m_Dr7ULiVMSLZU-0yartsXd-4LXITWRpe_h7AUmQM5RZeDUVtucta94bHSLvq_6ARDr1SgHwgcqlYi-54Rt4U3HufjgKCnKZrjuNNa9sSHs9-YMHsWggqaTmJiTkTnOFYHNw6qR6kyJgWg35CUGs6P2pFIe40h0Sq-qNRCtRDajeGWtCWCkBE9ZAnO3Hiqve-iAmhahaMxarVJweBsgT3JpgY5ISXAx6Mjb1e6lCp0gYTfh3xXu-GH5IoyY6_IhzIk6cjNE9fhWpduCVhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda9a50f81.mp4?token=t1zXnpQd8PoSc_UIEnTsIxm22djQmGHAPoQrNrTADll5PwAs48z4blMHTeF-sdQ11_7m_Dr7ULiVMSLZU-0yartsXd-4LXITWRpe_h7AUmQM5RZeDUVtucta94bHSLvq_6ARDr1SgHwgcqlYi-54Rt4U3HufjgKCnKZrjuNNa9sSHs9-YMHsWggqaTmJiTkTnOFYHNw6qR6kyJgWg35CUGs6P2pFIe40h0Sq-qNRCtRDajeGWtCWCkBE9ZAnO3Hiqve-iAmhahaMxarVJweBsgT3JpgY5ISXAx6Mjb1e6lCp0gYTfh3xXu-GH5IoyY6_IhzIk6cjNE9fhWpduCVhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهنمای اسکان و پارکینگ مراسم تشییع رهبر شهید در تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/446278" target="_blank">📅 15:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446277">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1UZqD2Jq_dxbkC7j3YuiQLw1rxq6FoJ09tvnM2DAJk4gVJQ6yz1egNHJrybiIbjGZ4Ho9kt8VdGTsNL5mUkXM3e2YIu-65MbnvYlGU30Z6angCt7SlPcxu6k8YMeZD99PsgrhBQVlXTKypDc-7dR8rcLuIaQTsujoP_y1qLI-llJD25-nesrMq79ckroICqpmQFXZjpTRwGfaxj98oz29AJ4XqxKYin1Zjt0QWjEiIwoT-urhJG_2Z0t7_h4aXYifruvjGItUIfNDrPcj6bNIWgfpgSYQWr-B7UD5WfE-UE0hAOd-KmId5TMxRO2psTYeERIJ1K7DfSlqXmMqJQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلی ۴ روزهٔ اتحادیه‌های صنفی تهران
🔹
رئیس اتاق اصناف تهران: با توجه به ابلاغیهٔ رسمی دولت برای برگزاری مراسم وداع و تشییع پیکر مطهر رهبر شهید انقلاب، اتاق اصناف تهران و کلیهٔ اتحادیه‌های صنفی پایتخت از روز شنبه تا سه‌شنبه تعطیل خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/446277" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446276">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7de078a47.mp4?token=Y6Zbl6AmcVwF8CMd8vdQJE72EE4oYOkv-dVj1Brxi1BAXFtmkRIfxcR4xqrbeMVbxd6wExJvWVmak04MhXJ7xLabWX29Xzu8AD_Kt8uijkD3Yh3FLFaLfJ5Fie66KVxSHmJuq9eKJM0ynhqcHBw9jLevk1baZweOnrqfdfBAV8uxY9PjYC8qTr4kZGAHQ8RYRITkgGlpMrIU1TD0Tt5-TO3_SWbLFOUHXf-xGnAbhi7HHZRgZ5hUqg-VN8T4rfdne7MetS9r89JgLwj9lny9kHzQtUO0LHSrVSsUeyt8TY6jiMNMAgEU05YMVmiuaDcgPrQIGtYIzfXc5kdDHmj34g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7de078a47.mp4?token=Y6Zbl6AmcVwF8CMd8vdQJE72EE4oYOkv-dVj1Brxi1BAXFtmkRIfxcR4xqrbeMVbxd6wExJvWVmak04MhXJ7xLabWX29Xzu8AD_Kt8uijkD3Yh3FLFaLfJ5Fie66KVxSHmJuq9eKJM0ynhqcHBw9jLevk1baZweOnrqfdfBAV8uxY9PjYC8qTr4kZGAHQ8RYRITkgGlpMrIU1TD0Tt5-TO3_SWbLFOUHXf-xGnAbhi7HHZRgZ5hUqg-VN8T4rfdne7MetS9r89JgLwj9lny9kHzQtUO0LHSrVSsUeyt8TY6jiMNMAgEU05YMVmiuaDcgPrQIGtYIzfXc5kdDHmj34g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس قرقیزستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/446276" target="_blank">📅 15:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446275">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5933555f6f.mp4?token=HqmUj8CnXgAkaoD06-Uj3DwEzGvhul13i_wWPFvoUwBrGZ4F7af4OKhTWvXv2Y5BuDhpK70Xc6fTug0qC30b88hadPwPehLIyeu1o66Mdvo6qy4-WzuaUPdSO2mq5YVOnSoivPR7ODxBD0n1g_Ig9blS9GDRYn3ApbYDoxnXLj6td3atmtalo-iEBy4KZd2Y2B7Tm-MMMsiheUAim1ci4Fuh2wg4uZPZmM3uc_sK8lThUFy79SuBMQDevou3cUjoW1yckV84d1jTIkKll1_gek4_RSD6UHamww6Z7RJWfxdWmxVu9begBbxpd1PoWsQpVgsMWJrf4ho0LEZjpYlRIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5933555f6f.mp4?token=HqmUj8CnXgAkaoD06-Uj3DwEzGvhul13i_wWPFvoUwBrGZ4F7af4OKhTWvXv2Y5BuDhpK70Xc6fTug0qC30b88hadPwPehLIyeu1o66Mdvo6qy4-WzuaUPdSO2mq5YVOnSoivPR7ODxBD0n1g_Ig9blS9GDRYn3ApbYDoxnXLj6td3atmtalo-iEBy4KZd2Y2B7Tm-MMMsiheUAim1ci4Fuh2wg4uZPZmM3uc_sK8lThUFy79SuBMQDevou3cUjoW1yckV84d1jTIkKll1_gek4_RSD6UHamww6Z7RJWfxdWmxVu9begBbxpd1PoWsQpVgsMWJrf4ho0LEZjpYlRIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس ازبکستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/446275" target="_blank">📅 15:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446274">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf4154ba.mp4?token=r4fHj2JL5TrcSYmR57hanqeQykmx2iGIRRqPKN3QZ8fCpeSZGnCYhdmplXDUxnhFjWrjJSif9EAO6zfJ1pMmwQsQCULEAnLVDr1pJWplbILr2w1OdzI6VfrfQkdLFoGrWG854CBj_gTgPo8rKVY1pPoVW7cLHQOczD5ujbn_tNxe8BCUl8gG41OhzpcuTLajsPPBROmvkKFPXLuxneFDM1wE-mwpZztkmCqjX8315yQB8NOnjuj4puTg_r_zjaWgpX7N6lK1rArsUfFQv_mLSzH9NUnfIUzNX8WnOR7NnLUK0-7XIxPKihP6V1GGwfky09mjxGPxJTvJZzbr9tD6gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf4154ba.mp4?token=r4fHj2JL5TrcSYmR57hanqeQykmx2iGIRRqPKN3QZ8fCpeSZGnCYhdmplXDUxnhFjWrjJSif9EAO6zfJ1pMmwQsQCULEAnLVDr1pJWplbILr2w1OdzI6VfrfQkdLFoGrWG854CBj_gTgPo8rKVY1pPoVW7cLHQOczD5ujbn_tNxe8BCUl8gG41OhzpcuTLajsPPBROmvkKFPXLuxneFDM1wE-mwpZztkmCqjX8315yQB8NOnjuj4puTg_r_zjaWgpX7N6lK1rArsUfFQv_mLSzH9NUnfIUzNX8WnOR7NnLUK0-7XIxPKihP6V1GGwfky09mjxGPxJTvJZzbr9tD6gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس منطقۀ کردستان عراق به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/446274" target="_blank">📅 15:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446272">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=P-LcBC1lV7Fmi6nbNm1IMJS8ys6QXzaUT_VXjn3IX0ObRL2Sm2GuhNx4T6khzc9Jpz8OxJQoETq7CDe69zNGJ0PPMHuWr-s8aCWUs6FOIjo7oifc6RHQv-CojihmsaN556tg6LBV1jhkyO5wSB-upy13OHx6PuYiNqcTz8KAoq-XPzzzLOkeywD4qWXOJPdZVitZuiTT3KJ1zNLxkAll9MTqlkwUqB0WcQnDm6P18eQtGp81FoZ1zHW5-70kNr1Xo-iZTPWDaIbB-BTUZ1a7yjoBpNqN3qVE-0877Av0t-S4znNYXgY2GnqPImLeXQfln7uTVIgZBMqGHk5p8Z-6hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=P-LcBC1lV7Fmi6nbNm1IMJS8ys6QXzaUT_VXjn3IX0ObRL2Sm2GuhNx4T6khzc9Jpz8OxJQoETq7CDe69zNGJ0PPMHuWr-s8aCWUs6FOIjo7oifc6RHQv-CojihmsaN556tg6LBV1jhkyO5wSB-upy13OHx6PuYiNqcTz8KAoq-XPzzzLOkeywD4qWXOJPdZVitZuiTT3KJ1zNLxkAll9MTqlkwUqB0WcQnDm6P18eQtGp81FoZ1zHW5-70kNr1Xo-iZTPWDaIbB-BTUZ1a7yjoBpNqN3qVE-0877Av0t-S4znNYXgY2GnqPImLeXQfln7uTVIgZBMqGHk5p8Z-6hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیدهادی خامنه‌ای برادر رهبر شهید انقلاب: شهادت مناسب‌ترین دستمزد ایشان بود
.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446272" target="_blank">📅 15:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446271">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7585a8203f.mp4?token=WzdGoFDZxnY67f9KAQ-c9SD2kFfpmHFoQT7uA797CiKkbXNcXG9FVZ9at1F4Y3vmDC04Mj8sChKfMKPs073ikmKkvcrZmfhWXJiSk-UF5mVbJoEzvKXBh65VOP1TxE_m7qzlwTzXvMcOcHCKNjXxh26xeHwvER6Z21XQeSAmZk2MQoSsoI9sMXy4AF6TImdhEt79b3neadXwLkfoY0PKb-lVGC9SkI2XcOBRISCeh1G0rTDqNzTtX8YyOZaVFsW1-bSEZNH_iM8yiogxWZrCwEGff7q-of1bSsW365qGdPnr-9ymamCcpv7XqPc7yvGccsjwpEYcl4YUDrfUfzL5cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7585a8203f.mp4?token=WzdGoFDZxnY67f9KAQ-c9SD2kFfpmHFoQT7uA797CiKkbXNcXG9FVZ9at1F4Y3vmDC04Mj8sChKfMKPs073ikmKkvcrZmfhWXJiSk-UF5mVbJoEzvKXBh65VOP1TxE_m7qzlwTzXvMcOcHCKNjXxh26xeHwvER6Z21XQeSAmZk2MQoSsoI9sMXy4AF6TImdhEt79b3neadXwLkfoY0PKb-lVGC9SkI2XcOBRISCeh1G0rTDqNzTtX8YyOZaVFsW1-bSEZNH_iM8yiogxWZrCwEGff7q-of1bSsW365qGdPnr-9ymamCcpv7XqPc7yvGccsjwpEYcl4YUDrfUfzL5cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نخست‌وزیر و فرمانده ارتش پاکستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446271" target="_blank">📅 15:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446270">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c32121a1ae.mp4?token=IV_z132mLv0LxtS67EaXBaudFiWP33JqHOt51RCXVJL9WrYaYIY5Ktf31OvLOTDlY0_Z8XCH2Z9n5tkrWBuBviw2ktpUUwqWheJBxb3ZO2tmhP8nEu3yDNfmxw5k7uU9RGbpxtzrdapPKPQcW2wX23_TKL0HYrd5PpWLNDSzg6o0yQd1SOTsOvSDlmX0An0fT0gof7RezEkqDfJ_FKkypfCVrjMnjOYf9yG3GPfBcEKadV-d0tFuqmMs0QXBgIp29KihnDOZKD2E1IbunpcZNl6ANzVYIUhShzYNzk050a25tSHq-GgTLIMJei3ugVReaIFPFzwOf85YoKfiswZrMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c32121a1ae.mp4?token=IV_z132mLv0LxtS67EaXBaudFiWP33JqHOt51RCXVJL9WrYaYIY5Ktf31OvLOTDlY0_Z8XCH2Z9n5tkrWBuBviw2ktpUUwqWheJBxb3ZO2tmhP8nEu3yDNfmxw5k7uU9RGbpxtzrdapPKPQcW2wX23_TKL0HYrd5PpWLNDSzg6o0yQd1SOTsOvSDlmX0An0fT0gof7RezEkqDfJ_FKkypfCVrjMnjOYf9yG3GPfBcEKadV-d0tFuqmMs0QXBgIp29KihnDOZKD2E1IbunpcZNl6ANzVYIUhShzYNzk050a25tSHq-GgTLIMJei3ugVReaIFPFzwOf85YoKfiswZrMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کدام هیئت‌های خارجی تا ظهر امروز برای وداع با رهبر شهید وارد تهران شدند؟
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446270" target="_blank">📅 15:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446269">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca3e80ab3.mp4?token=sdiTEreg0dAzmO_cGyHARoAg-e11MJKwLNWTkpRmzn1xqpNhRKxpX3cbLswjR5gXDlAQWH74uxxrL7o3Ws0EVXkUqKlupUIvUV1aVO2PRy7OTPyHMQ7fSgWDLv_wlgDjpjQdfwfwopvmifPh0JQ6G3erBrdI0R0fy7ZOvQ4GlJK2NuW4fNACuVHmLDZ2AE1soxKOXJ05BBBT99jXvV-AasK2uLBQSv9OnsNv_FQx5U50v__yEDAHF-N0YhjAhEP2vqV85ZBgHASPzQeIRAil2pH5mAIOQXyiE0JvUxe8EgHIKYOW-gaEqSQaSKwvVbPqXm1kbCYrDRCrsDFBmjZYow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca3e80ab3.mp4?token=sdiTEreg0dAzmO_cGyHARoAg-e11MJKwLNWTkpRmzn1xqpNhRKxpX3cbLswjR5gXDlAQWH74uxxrL7o3Ws0EVXkUqKlupUIvUV1aVO2PRy7OTPyHMQ7fSgWDLv_wlgDjpjQdfwfwopvmifPh0JQ6G3erBrdI0R0fy7ZOvQ4GlJK2NuW4fNACuVHmLDZ2AE1soxKOXJ05BBBT99jXvV-AasK2uLBQSv9OnsNv_FQx5U50v__yEDAHF-N0YhjAhEP2vqV85ZBgHASPzQeIRAil2pH5mAIOQXyiE0JvUxe8EgHIKYOW-gaEqSQaSKwvVbPqXm1kbCYrDRCrsDFBmjZYow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا گریه می‌کنی؟
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446269" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446267">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2XUPrewS2Fu9JOAsNh-ncO_UT-fo8fxpm9lEIt75XYWEKMOfjvwLS5J3__fMiTjtlOvlfcMW7_qVP3wQEIQlo2voJpUB42BP4017jL4d6SIXTUE0TjNBNOfF8361EP2Did5p_qBvc2Ty6rH3O7P8fUx1AX5V0ajKYZwmr21MGvKnTifE0GvDfylog-BnpAgOg-Mbvy_RSAxgt7YO9uMRQPniOQoI2ZLRGaRbuUNK1UMde2Q4PL55o-faQ80tjD8xtNDP2L2zvSv6OMmXnuNdwoXdoXcjA00b2uRDkPBJJrjdTorSdufYi0VzgAUa3X4v6IdtY9hcYLQD-9A--VXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixj19rfk0pT1z1fe1RqvT3m6elmMUC36LAQ3-szIzinSvNQG4n5CMfh1hMZc2M4061WHQ9ZYPDl2yJ5WjqN-C1utw9QbkiRQofxFTETzxJZmnZleYExXrtIltN489KhmnCgt9tDYW15rRyWVGqhyrnCUWjWy9gzF39yHHJ7y-gcheFLPaf3qfjozZltj0gC17u7GBaEfmLjBRrWck8pbhNdeQWPn6ycTrciHcLHMQ8GPqQqa9vLQ_z15x4yZpezIPYvZIh1KDr-VcIAkJzvBbritO4-4ZZL0i32VnIZhOCGkmCf4Lr1LJwHkCVegdypU8J90NGQyxgTJ7l2tRxud8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور علمای اهل سنت برای مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446267" target="_blank">📅 15:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446266">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af14934df.mp4?token=Ald5H5Zco9A1A_sX7lDTNV8wG824eduAbCARaxyRvy4AbYZk-jXHwg6d9Te_y6FVNkSgtcJPnzOpeAjGkeXIdqxVcJPJ6Dzp9Q_Ou5aMak84sYmvJREU5S_p_oVfOe357zA7uEy4r8Uud6EemxH_uYUZmOmMV_EKh7hsLKyUwE_CuCfbXntliYEuM6TqQ-9YLnvvulF6L9C9YryrHeWEqvJOCSXUF5jyOHJMJYNPYfO6QrPcctK4hHUQrgNZs03qKCKcPbt0KRj6IHqZo1jK-Y1fBTq9royu9am51G5xjtg02owvSLCbBuco2NkJiM0FwrMi8UkpPgegyJNDdC8NEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af14934df.mp4?token=Ald5H5Zco9A1A_sX7lDTNV8wG824eduAbCARaxyRvy4AbYZk-jXHwg6d9Te_y6FVNkSgtcJPnzOpeAjGkeXIdqxVcJPJ6Dzp9Q_Ou5aMak84sYmvJREU5S_p_oVfOe357zA7uEy4r8Uud6EemxH_uYUZmOmMV_EKh7hsLKyUwE_CuCfbXntliYEuM6TqQ-9YLnvvulF6L9C9YryrHeWEqvJOCSXUF5jyOHJMJYNPYfO6QrPcctK4hHUQrgNZs03qKCKcPbt0KRj6IHqZo1jK-Y1fBTq9royu9am51G5xjtg02owvSLCbBuco2NkJiM0FwrMi8UkpPgegyJNDdC8NEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی که اشک فیلم‌بردار حسینیهٔ امام خمینی(ره) را درآورد
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446266" target="_blank">📅 15:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446265">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514a7a3b42.mp4?token=WUL8RyUFWMVv18SlL3Xu2K9p2Ea_gCpRXfsuC3_fmOL91MhLnnThqCCtMGQqf9QGe2Lbuolsui0ao_Qz3i837_H7P15SvukwfGt4PdPVMWcxKWwp7i6xyjtA-MTNjeeAUuuCp-FrY6WpEBO9mBp9D-JNHYU1CquxXj_boWcUl1_suIeKYVh2WjJ7_v4c8PfS6J9im3KOaXeV49B_0uAdvTwJ23cVGAdpRSbk4hOkceQ99kJLPp17mxdzO47A0xLhxMKQcxa4x0RntznVDnoZuj_EZXbtTLk_IHILTLh9tRoW3yi3tuXcLAJOI8rkIuphXXCaDHWhFbNDyhc0-H-MqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514a7a3b42.mp4?token=WUL8RyUFWMVv18SlL3Xu2K9p2Ea_gCpRXfsuC3_fmOL91MhLnnThqCCtMGQqf9QGe2Lbuolsui0ao_Qz3i837_H7P15SvukwfGt4PdPVMWcxKWwp7i6xyjtA-MTNjeeAUuuCp-FrY6WpEBO9mBp9D-JNHYU1CquxXj_boWcUl1_suIeKYVh2WjJ7_v4c8PfS6J9im3KOaXeV49B_0uAdvTwJ23cVGAdpRSbk4hOkceQ99kJLPp17mxdzO47A0xLhxMKQcxa4x0RntznVDnoZuj_EZXbtTLk_IHILTLh9tRoW3yi3tuXcLAJOI8rkIuphXXCaDHWhFbNDyhc0-H-MqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس‌جمهور تاجیکستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446265" target="_blank">📅 14:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446258">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-wV5vkg5_YM50MS8KzqexEE5xUQt9WcokkBbMAEJnkTmKdr8ga_EBdUJKxXdjkRcvJqiJ6Pesk6tP51TU-UtjYoOr4QaU4RIeHJyI9Rw9AUYn5pYSNm-FXYnz0tEfhoMQsIQg_BkRektOUmEz0sxPrj8wzqI40qr8n9cEGk5N-gWVeB_d3NiENaBKrsaDA7WW_xwG7YQbKpuByKOYx6vMwVO0rayHfzXqRQP0hoThLpMafbSrZBbfyU_tgBM-7gbP_Qc5r7VX2p0ZT5TEBifAlnEYkXWSNs6Efor5c9UEPVD0v8o81N_MYa5T31HAoh8WkgJKRSSzwvOuTuWnKRxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9lgN8OPu8Kx_Mg4syZJT4EiYFUyh5Kl0HUinu3myiIOyA4RUhITrKmVGOpJ2NWYgRjoVISOGghzmz1_A43P2uP705pmJt1-NIRDPWIpuPIF7kax_cMJ7kvKEi4yfyqKZ39St6pyH6JHIaVzLXTDzRRxN-WO39si6mTwbUqK5btEA2gTGmDXU5mutlxTgcVUBoQHSGjEg2yXAWv65gyUIGV7UipqW3ew264sl6Ed_91wsCyju9g4nAiRlskSiXuF2s8edDpuEdXnx7svuk148zYHmcVakudbnkhapgX-uclMopJtjushElpFnBXwLbpDPPd82EAb4eAmtKXrcS5NmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxQaTUoR9zrCw59CAdDgXki4m4dgmIlWIfbEmUO4x6Y5WgItKLXBiqRAqYBdcF4d8g3j1RXoGQoDIaIqdbH4noTgmt40HBZWNWkh1hVcJ2Zi5yEy8Jm-JX9Ha1W6SPjn6nJnscoeEP5hURyJpGLhzzq7AKfWVR0vTBbIELksXGT0rbo06n4wI9vQvFFN1emPoWohx1IY56wGm0p1z2HyUG4x2UYfI8Q5oJjz4tkN8IEpBICfIgqmJ4RP9daUiiMtLI6OWz43oRAc_l5vFm99OT_CcbqW_0ajBW1LAbVdkecYuSCJZxnfoe0TOATuXjD9Zy0ZfP53zslZaVNj2MivuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ev_ka1XTESuGq4L0rQvKpNnHBjRuo1lceq86u13QzbQwkUTOFagfAthQK-3crKvf-SpOzecbneaofF3P0hfzyTBInWKPh7CjHWTu_3In-K-pgVBX4XkzbA_c7UAYHGqpBiAa86Y9F_pRhm878LrNl1ZieDC1U13mfz669QVSxn9Owbxc2dUHEJAzzFC0vnW57n9rWC27dVyvVofghx-8iIY3Up0weo9pJaIYstKXEl4YYMBqQSjLDofqbmJ9Vhf9OPiAmkRB-J_z20PbtXAh6VJGch0gucfbHPhuuqafZ6inxLZYGM2kUElESIxWOulfICY30rN5C-6z8F11ct6kCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXqs-1UQWjncq3O9uXhDRLAG6fPjwTms5luRv28336zbFKg8y0bJ7TB10yUb9SZHO39NISGUtTDMhVIBBtVBy6NkhkczV3sMgwnpiqZXCleJ2n4DqnZ8kqEYX4m_HsCIeuJ7ly-ZvdwbvyFRRx9Pd7RDy2w2qHTuTgFlkTerpBisU91vMbOJqu5Yc4OJoKYzfg42C4JohOgAl1lx9RbjTUutb1fn7cW52DC7BmpE6cprJY0brIRGMU4bGo8RuOMZZJgE5vpFZ2WGEgfSGkIvWEPIQk0c2UhmsJuwQfdWv2spp0YE8FErchff4KXnDm42VkvJ4loibClLrCVkLTRRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKpQbrODmbymLJaKH4WT891Z29JE_jjc0spGcjOKj9m0iIZFbi5z-DGiuPTU83Jip3CQkCoqDiVrF6fUtTZeJaaUCMoamqMLfI4h9iLoCP4PmCgqt8ffQ2F-kcsKWr9fC94Ob2fBaCQIgIys2NPk9rmk9izcrQmGGFW9SErqCrTbRldW-W7iMbKdLdY5jplQQ0Xgx5Gia_-kPuhhv02vXsI6XPM2KvvwSXpHDcscxGERMcAf8Cz5BU3vIKSSRNZSxrlaKOP5WpJIleXpXz8k1dItAvH0_E3J6ANvn33BQPK-5zwvNzjS2-Nmt7xDCaQ1Lo3AeR7YwI3Qi30fpMOIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2n8It_GGEHE5IPtdemAOysee8_2DAuSg1KvXmPr9EySWvaY9zzCwpPArOp3hpbRis9c6-1w-J2iz6rYe0hsFQUB7a1s0OKX3QaADg-v8e4xdSP63gI1lboPU2l5i-uKvCI666ff9ijC1DYnaPZ_bDseKt2jEcvreHyc61hjNblKipIZ08JKpfT-JLDgR1jN2vlQ51CMOtrKVeH_F5igmP8qUOcGZREW27SGq7x4rBc4-20vjEipOmRg-IGjUPsc5JRE63Ieedbn_SKdYd63s-UUiXnvxR-uxxlCg9n51lO5h5i5M1zQhzvySOuZ7k_prc0_p5k76ZQhFg-zINYTDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ادای احترام سران قوا و مسئولان ارشد کشور به پیکر مطهر امام شهید
عکس:
زینب حمزه لویی
@farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446258" target="_blank">📅 14:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446257">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtM9LjmOmww6v_ShYtbNwQhk1iUUZ00pckIGBZwtlruuaE3IGOf0q5ubRG7PhmUYcLJX3yQ7hvBaSAeowfq8NBis17JPrMFm2COOz8FTmUub-OxlIwRJFJIFLp8qlZbUlfy_uAOK_1h-OLZL0EcgyBeDRh4bFd4J5UzCwaBqut7qXGBiwHggAH0F-9J9U8OYHWv64ySR5VEmOx0NQz3Px598yHXUhTL8XUl5MBEyZe_ZWZMzzx_TXxaA-KsKFgr9S7xYWFihfFvNSDvm-CFEngkAKb1cXKvrXF6OWptpf3eGX7P1-TDc43GrxnThqoSRD819RuUUG0lA-JSNwHjxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دست‌نوشته‌ شهید مصباح‌الهدی باقری برای آقای شهید ایران
🔹
یا سیدنا القائد؛ به وجود پر از مهر و صفایت می‌نازم...
🔸
شهید مصباح‌الهدی باقری‌کنی، داماد رهبر شهید انقلاب، اسلامی در آغاز جنگ تحمیلی اخیر، همراه رهبر شهید بر اثر حمله جنایت‌کارانه‌ی آمریکا و اسرائیل…</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/446257" target="_blank">📅 14:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utyb80hlIv6o21Szy8Bu2GHRNPT56VClQAzVCn3tCNwxocmJbfZ_I2K112-PFTqDu2ksLblt7UwlvwLqvjfsGopYMiNL0q3KaLplHDRB961Lusdh_1y8e5eT5f_olCctr45ay2DpxzKgLCckdUBjpzpFTLCqoXsKgy12XrLE1-dJQkC3OUonvaVHcU_xR8jQbNftzpziSTMEp2Nuu0YHU12hMSToCo17aiVWS2BY4T95M7RfD24GzvYbDIpmggwqG3VATqlcJb6DWzX3TFAhHR62gXplx6KEJVbja-bpuJZSqocu-NbySN-qPV_RWckzmN9guE4Cpwbgw-QUMyxhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
یادبود بچه‌های مظلوم میناب در ورودی سالن ادای احترام مقامات کشورهای خارجی به پیکر مطهر رهبر شهید انقلاب در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/446255" target="_blank">📅 14:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446254">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e695d4c345.mp4?token=TkwZjksx5r7hPzOe2alAPYbwAmB3o67hfMciAUNBgwSMA11P0GMsP7ATJf3NEK8uDdCYj5rkLyDcTBRucmUg0eXK12uarPPTU2IC1I3bSoz9MHzJGFHRWMPpKr6OV6EgdszeK8IqCnD0gy7ZOKG_k-aLSzkSwRAa5Lfs-jtlPmu0-58RGqK4yIT-XYgcFbJjg0JIoHtOEEKEXiM7HOOa3p-p4-wC5Z74QspLBplx-ZTg_jP6FFfF0rFg4ba3cW8XBGSWNyETaOROjPWi7Y60qTXvlRiRDxSt7qOqs2oNZZ6SU7nevv4T2uaIdV79BuLAwO2SAYDifgOZhP6jz6Ex8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e695d4c345.mp4?token=TkwZjksx5r7hPzOe2alAPYbwAmB3o67hfMciAUNBgwSMA11P0GMsP7ATJf3NEK8uDdCYj5rkLyDcTBRucmUg0eXK12uarPPTU2IC1I3bSoz9MHzJGFHRWMPpKr6OV6EgdszeK8IqCnD0gy7ZOKG_k-aLSzkSwRAa5Lfs-jtlPmu0-58RGqK4yIT-XYgcFbJjg0JIoHtOEEKEXiM7HOOa3p-p4-wC5Z74QspLBplx-ZTg_jP6FFfF0rFg4ba3cW8XBGSWNyETaOROjPWi7Y60qTXvlRiRDxSt7qOqs2oNZZ6SU7nevv4T2uaIdV79BuLAwO2SAYDifgOZhP6jz6Ex8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجسمه مشت گره‌کرده رهبر شهید در میدان انقلاب نصب شد
@Fars_plus</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/446254" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446253">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa6057f04.mp4?token=I3kYSK88Mrtsk4Con9u51n64iP3NdJFVlaJQ8pe7jlgg8L9M_QFsdkedeIXKRDOdmsMTBqWkSOL-CZOLXsQrWSsUvuxqdHvDAczoe4rqfp-wEYnJL53f-vzLke-cl2GjFOh1YrSR_YnZOXgi3ZgK9_oJMAA1RCtpG7pkJY-WHkOvoKutX7uMhJZox49EDfHTNhJFZEBnLDhe5inRrZow34IuJNE1OOpBKIUusAYELlIEjQu7Bmvj8X0Jysbr4ClLcqoeDGjAewKiuk3RV7CCtMdJOoyJlBAYwLDx0PTLKZt6IRr1WmodPZyoLTfBFuj1gsoqHI1SPZeoJuRH_SX3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa6057f04.mp4?token=I3kYSK88Mrtsk4Con9u51n64iP3NdJFVlaJQ8pe7jlgg8L9M_QFsdkedeIXKRDOdmsMTBqWkSOL-CZOLXsQrWSsUvuxqdHvDAczoe4rqfp-wEYnJL53f-vzLke-cl2GjFOh1YrSR_YnZOXgi3ZgK9_oJMAA1RCtpG7pkJY-WHkOvoKutX7uMhJZox49EDfHTNhJFZEBnLDhe5inRrZow34IuJNE1OOpBKIUusAYELlIEjQu7Bmvj8X0Jysbr4ClLcqoeDGjAewKiuk3RV7CCtMdJOoyJlBAYwLDx0PTLKZt6IRr1WmodPZyoLTfBFuj1gsoqHI1SPZeoJuRH_SX3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس بلاروس به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/446253" target="_blank">📅 14:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446252">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caae8012d4.mp4?token=Qy2dyY6NVeggtj7Lcnb6KZ66UT5LVnbJ0PqVirwtVAYNETVXzRLcjyTFtQTMNqycrCSR_c8PHtVQR9qnj9NAR7kAk1BhoI3jc3M3f9fTcyfUyTV_hgVthjT0QXQZXvrYo0pqF6IqcwIij-9DboFfnLDFsBjtr0N_oQAPmlIdOHfIXnom5jBakxG5JabiQkfJrlCMf5DM2Qt498G4AvbmNdU1GEANJY7QKZF7Dl0LD1YwgIZ3nNUlhkGgcizlUWCQUY-n09xnlHkD7hQlZy8TgAURQWJr8X1QRroGOw_T-0pd54rcqwes28sXiUz_035ulmRp5cIwWx8f1zMGSYT8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caae8012d4.mp4?token=Qy2dyY6NVeggtj7Lcnb6KZ66UT5LVnbJ0PqVirwtVAYNETVXzRLcjyTFtQTMNqycrCSR_c8PHtVQR9qnj9NAR7kAk1BhoI3jc3M3f9fTcyfUyTV_hgVthjT0QXQZXvrYo0pqF6IqcwIij-9DboFfnLDFsBjtr0N_oQAPmlIdOHfIXnom5jBakxG5JabiQkfJrlCMf5DM2Qt498G4AvbmNdU1GEANJY7QKZF7Dl0LD1YwgIZ3nNUlhkGgcizlUWCQUY-n09xnlHkD7hQlZy8TgAURQWJr8X1QRroGOw_T-0pd54rcqwes28sXiUz_035ulmRp5cIwWx8f1zMGSYT8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نخست‌وزیر ارمنستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/446252" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446251">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e418570b.mp4?token=fmOCpKbEMvCOryCNPqiSUs_vBDagDwWKyg9lb-RJp1jWi6L22qDY745KD4TzZCIv2b0Agx5jKwE6lcg1VB9HpD158-0r7gSh_sBRs113UaWsI87Dc61HtLJvmchXm0xCa-eLaiFB8CjcQzGaYNBQBhvbQ2XlRJIqoh0WRm5A3iIPH-A8DkVpcDJ3jdCdddxZr98imQVlkUxmdWu3x0qRaq-7HTi2tQTFR45OMeVwc6ywjFPO9tHcrz-DITQQ5wcWdHB_ksn5Zs6AOoebsF7bFC3vgBlfNDt2Q4a2uC67Zc_mMqSDfORJPXk1zBJwxF0hTB--NkIg1lFB8wCElfy9-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e418570b.mp4?token=fmOCpKbEMvCOryCNPqiSUs_vBDagDwWKyg9lb-RJp1jWi6L22qDY745KD4TzZCIv2b0Agx5jKwE6lcg1VB9HpD158-0r7gSh_sBRs113UaWsI87Dc61HtLJvmchXm0xCa-eLaiFB8CjcQzGaYNBQBhvbQ2XlRJIqoh0WRm5A3iIPH-A8DkVpcDJ3jdCdddxZr98imQVlkUxmdWu3x0qRaq-7HTi2tQTFR45OMeVwc6ywjFPO9tHcrz-DITQQ5wcWdHB_ksn5Zs6AOoebsF7bFC3vgBlfNDt2Q4a2uC67Zc_mMqSDfORJPXk1zBJwxF0hTB--NkIg1lFB8wCElfy9-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس جمهوری آذربایجان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/446251" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446250">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41090b7f32.mp4?token=dSTnzA-R0uVzgH-AOdtzcE8gMFWXDvSCPI5sjAk17PVyzx81hpE_fGuj5d-ikDZpYS8S-aPunvTd7mgPgs1gDSZ7DRTrrIDgEKuw8G2_T8iuDWHQ3gPyb6YgQ7OA0N1T2l18RwBXL48FMimx-xPON6t6WYtYEglDdLYVps6IRx0pitAm1A5ffbh5SjctVWgyiqYT3_BLRIlpwedF5yp-qVpyJnEqKFubTp41r-_d07CxXzU_wmdfJFkEkekY9EyuemnZmgoY9o1Z4tgL9E3-wYBx1LHwmYFe_Cr6DqZLyeQXk2CnfWX2yBARJokclz0c6FWuzqL07td_hQkvlFA7tRB8jcIt8yaUB16MEt1q1X7on_KHksKb6BdvjPIqkUk2Fmz9Dlr5Hab-BLQfErsue8Hpy2Qo7Ac3VGLysfTUtMFLwNO-D4vt5DjVRkMIFuSNzgA9JUmqSDEsz50Dhkk7GzpF4wekO80C1ilhwblHZj-f4-ej1DowlwEeTumFUEJW9lDIDtxLECR399MsSx4rROy1cHV2uPW3A4um5Etstg0ICheUblOPj5RiRPO9g0ec49XiS-ghnQ8ONfvxeY-hjjbk2WVGI6i4Yv2UP51MXjFyPguUO_1A2V9IXwrqr_spx2RY-g-K0K8tp7-Qk3-JgIA4vDfx1quih9R5K8_FceU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41090b7f32.mp4?token=dSTnzA-R0uVzgH-AOdtzcE8gMFWXDvSCPI5sjAk17PVyzx81hpE_fGuj5d-ikDZpYS8S-aPunvTd7mgPgs1gDSZ7DRTrrIDgEKuw8G2_T8iuDWHQ3gPyb6YgQ7OA0N1T2l18RwBXL48FMimx-xPON6t6WYtYEglDdLYVps6IRx0pitAm1A5ffbh5SjctVWgyiqYT3_BLRIlpwedF5yp-qVpyJnEqKFubTp41r-_d07CxXzU_wmdfJFkEkekY9EyuemnZmgoY9o1Z4tgL9E3-wYBx1LHwmYFe_Cr6DqZLyeQXk2CnfWX2yBARJokclz0c6FWuzqL07td_hQkvlFA7tRB8jcIt8yaUB16MEt1q1X7on_KHksKb6BdvjPIqkUk2Fmz9Dlr5Hab-BLQfErsue8Hpy2Qo7Ac3VGLysfTUtMFLwNO-D4vt5DjVRkMIFuSNzgA9JUmqSDEsz50Dhkk7GzpF4wekO80C1ilhwblHZj-f4-ej1DowlwEeTumFUEJW9lDIDtxLECR399MsSx4rROy1cHV2uPW3A4um5Etstg0ICheUblOPj5RiRPO9g0ec49XiS-ghnQ8ONfvxeY-hjjbk2WVGI6i4Yv2UP51MXjFyPguUO_1A2V9IXwrqr_spx2RY-g-K0K8tp7-Qk3-JgIA4vDfx1quih9R5K8_FceU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KHAMENEI.IR – باید برخاست</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/446250" target="_blank">📅 14:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ab5e31a5.mp4?token=p6aNiolC_mQxdSvok5Ir41B67lFxnKqXkdUdvyc2jbO2oKTxCVhIMMRG4WLDCG73P8bsO7jtoA5A-fZARHbh686_GwPdaKUc_bGaPFkAYGbRa97kJTyAGFnv59GAZOPNzVOLzjPGiSKB1iX0cydix1IaNCBLylCRtST_m6gW8qjV7CqYANWu4xHNKUTXeueb5NOZjl88ZEMxiEXHnULiRnTTSwL03br78sVIRyg18X8fkNb0t4M4bnE5Vco77RVF1bfuE7zppndQGLQ770MOsS90o496z3QOhA4GHp5Z-5NVcehDbx0Zvpv1D8wZdyhFP2ZVjH9SzYjut9jTFi2_Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ab5e31a5.mp4?token=p6aNiolC_mQxdSvok5Ir41B67lFxnKqXkdUdvyc2jbO2oKTxCVhIMMRG4WLDCG73P8bsO7jtoA5A-fZARHbh686_GwPdaKUc_bGaPFkAYGbRa97kJTyAGFnv59GAZOPNzVOLzjPGiSKB1iX0cydix1IaNCBLylCRtST_m6gW8qjV7CqYANWu4xHNKUTXeueb5NOZjl88ZEMxiEXHnULiRnTTSwL03br78sVIRyg18X8fkNb0t4M4bnE5Vco77RVF1bfuE7zppndQGLQ770MOsS90o496z3QOhA4GHp5Z-5NVcehDbx0Zvpv1D8wZdyhFP2ZVjH9SzYjut9jTFi2_Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های تهران آمادۀ میزبانی از مراسم وداع با آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446249" target="_blank">📅 14:34 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
